# IBM watsonx API Integration Guide

## Overview

This guide provides detailed instructions for integrating IBM watsonx AI into SmartClick, including authentication, API usage, prompt engineering, and best practices.

## IBM watsonx Setup

### Prerequisites

1. **IBM Cloud Account**
   - Sign up at https://cloud.ibm.com
   - Create a watsonx.ai project

2. **API Credentials**
   - API Key (IAM authentication)
   - Project ID
   - Service endpoint URL

3. **Model Access**
   - Ensure access to desired models (e.g., `ibm/granite-13b-chat-v2`)

### Environment Configuration

Create a `.env` file in the project root:

```env
# IBM watsonx Configuration
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_ENDPOINT=https://us-south.ml.cloud.ibm.com
WATSONX_MODEL_ID=ibm/granite-13b-chat-v2

# Optional: Rate Limiting
WATSONX_MAX_REQUESTS_PER_MINUTE=60
WATSONX_MAX_TOKENS_PER_REQUEST=2048

# Optional: Caching
ENABLE_RESPONSE_CACHE=true
CACHE_TTL_SECONDS=3600
```

## SDK Installation

```bash
npm install @ibm-cloud/watsonx-ai
npm install ibm-cloud-sdk-core
```

## Implementation

### 1. watsonx Client Wrapper

**File**: `src/main/services/ai/watsonx-client.ts`

```typescript
import { WatsonXAI } from '@ibm-cloud/watsonx-ai';
import { IamAuthenticator } from 'ibm-cloud-sdk-core';
import { logger } from '@main/utils/logger';

export interface WatsonxConfig {
  apiKey: string;
  projectId: string;
  endpoint: string;
  modelId: string;
  maxTokens?: number;
  temperature?: number;
  topP?: number;
  topK?: number;
}

export interface GenerationParams {
  prompt: string;
  maxNewTokens?: number;
  temperature?: number;
  topP?: number;
  topK?: number;
  stopSequences?: string[];
  repetitionPenalty?: number;
}

export interface GenerationResponse {
  text: string;
  tokenCount: number;
  finishReason: string;
  metadata?: Record<string, any>;
}

export class WatsonxClient {
  private client: WatsonXAI;
  private config: WatsonxConfig;
  private requestCount: number = 0;
  private lastResetTime: number = Date.now();

  constructor(config: WatsonxConfig) {
    this.config = config;
    
    // Initialize IBM Cloud SDK authenticator
    const authenticator = new IamAuthenticator({
      apikey: config.apiKey,
    });

    // Initialize watsonx.ai client
    this.client = new WatsonXAI({
      authenticator,
      serviceUrl: config.endpoint,
    });

    logger.info('WatsonxClient initialized', {
      endpoint: config.endpoint,
      modelId: config.modelId,
    });
  }

  /**
   * Generate text completion
   */
  async generateText(params: GenerationParams): Promise<GenerationResponse> {
    try {
      // Rate limiting check
      this.checkRateLimit();

      const response = await this.client.generateText({
        projectId: this.config.projectId,
        modelId: this.config.modelId,
        input: params.prompt,
        parameters: {
          max_new_tokens: params.maxNewTokens || this.config.maxTokens || 1024,
          temperature: params.temperature || this.config.temperature || 0.7,
          top_p: params.topP || this.config.topP || 0.9,
          top_k: params.topK || this.config.topK || 50,
          stop_sequences: params.stopSequences || [],
          repetition_penalty: params.repetitionPenalty || 1.1,
        },
      });

      this.requestCount++;

      const result = response.result.results[0];
      
      logger.info('Text generation successful', {
        tokenCount: result.generated_token_count,
        finishReason: result.stop_reason,
      });

      return {
        text: result.generated_text,
        tokenCount: result.generated_token_count,
        finishReason: result.stop_reason,
        metadata: {
          modelId: this.config.modelId,
          inputTokenCount: result.input_token_count,
        },
      };
    } catch (error) {
      logger.error('Text generation failed', { error });
      throw this.handleError(error);
    }
  }

  /**
   * Stream text generation (for real-time responses)
   */
  async *streamGeneration(params: GenerationParams): AsyncGenerator<string> {
    try {
      this.checkRateLimit();

      const stream = await this.client.generateTextStream({
        projectId: this.config.projectId,
        modelId: this.config.modelId,
        input: params.prompt,
        parameters: {
          max_new_tokens: params.maxNewTokens || this.config.maxTokens || 1024,
          temperature: params.temperature || this.config.temperature || 0.7,
          top_p: params.topP || this.config.topP || 0.9,
          top_k: params.topK || this.config.topK || 50,
          stop_sequences: params.stopSequences || [],
          repetition_penalty: params.repetitionPenalty || 1.1,
        },
      });

      this.requestCount++;

      for await (const chunk of stream) {
        if (chunk.results && chunk.results[0]) {
          yield chunk.results[0].generated_text;
        }
      }

      logger.info('Streaming generation completed');
    } catch (error) {
      logger.error('Streaming generation failed', { error });
      throw this.handleError(error);
    }
  }

  /**
   * Check rate limits
   */
  private checkRateLimit(): void {
    const now = Date.now();
    const timeSinceReset = now - this.lastResetTime;

    // Reset counter every minute
    if (timeSinceReset >= 60000) {
      this.requestCount = 0;
      this.lastResetTime = now;
    }

    const maxRequests = parseInt(process.env.WATSONX_MAX_REQUESTS_PER_MINUTE || '60');
    
    if (this.requestCount >= maxRequests) {
      throw new Error('Rate limit exceeded. Please wait before making more requests.');
    }
  }

  /**
   * Handle API errors
   */
  private handleError(error: any): Error {
    if (error.status === 401) {
      return new Error('Authentication failed. Please check your API key.');
    } else if (error.status === 403) {
      return new Error('Access denied. Please check your permissions.');
    } else if (error.status === 429) {
      return new Error('Rate limit exceeded. Please try again later.');
    } else if (error.status === 500) {
      return new Error('IBM watsonx service error. Please try again later.');
    } else {
      return new Error(`API request failed: ${error.message}`);
    }
  }

  /**
   * Test connection
   */
  async testConnection(): Promise<boolean> {
    try {
      await this.generateText({
        prompt: 'Hello',
        maxNewTokens: 10,
      });
      return true;
    } catch (error) {
      logger.error('Connection test failed', { error });
      return false;
    }
  }
}
```

### 2. Prompt Builder

**File**: `src/main/services/ai/prompt-builder.ts`

```typescript
export enum PromptAction {
  SUMMARIZE = 'summarize',
  REWRITE = 'rewrite',
  EXPLAIN = 'explain',
  ANALYZE = 'analyze',
  CUSTOM = 'custom',
}

export interface PromptOptions {
  action: PromptAction;
  context: string;
  customPrompt?: string;
  tone?: 'professional' | 'casual' | 'friendly' | 'formal';
  length?: 'short' | 'medium' | 'long';
  additionalInstructions?: string;
}

export class PromptBuilder {
  private static readonly SYSTEM_PROMPT = `You are IBM Bob, an AI assistant integrated into SmartClick. You help users with text-related tasks across any application. Be concise, helpful, and accurate.`;

  private static readonly ACTION_TEMPLATES = {
    [PromptAction.SUMMARIZE]: {
      short: 'Summarize this text in 1-2 sentences:\n\n{context}',
      medium: 'Provide a concise summary of this text:\n\n{context}',
      long: 'Provide a detailed summary of this text, including key points:\n\n{context}',
    },
    [PromptAction.REWRITE]: {
      professional: 'Rewrite this text in a professional tone:\n\n{context}',
      casual: 'Rewrite this text in a casual, conversational tone:\n\n{context}',
      friendly: 'Rewrite this text in a friendly, approachable tone:\n\n{context}',
      formal: 'Rewrite this text in a formal, academic tone:\n\n{context}',
    },
    [PromptAction.EXPLAIN]: {
      short: 'Explain this text simply:\n\n{context}',
      medium: 'Explain this text in clear, understandable terms:\n\n{context}',
      long: 'Provide a detailed explanation of this text, breaking down complex concepts:\n\n{context}',
    },
    [PromptAction.ANALYZE]: {
      short: 'Analyze this text briefly:\n\n{context}',
      medium: 'Analyze this text and provide insights:\n\n{context}',
      long: 'Provide a comprehensive analysis of this text, including themes, tone, and implications:\n\n{context}',
    },
  };

  /**
   * Build a prompt for a specific action
   */
  static buildPrompt(options: PromptOptions): string {
    const { action, context, customPrompt, tone, length, additionalInstructions } = options;

    let prompt = '';

    // Add system prompt
    prompt += `${this.SYSTEM_PROMPT}\n\n`;

    // Add action-specific template
    if (action === PromptAction.CUSTOM && customPrompt) {
      prompt += `${customPrompt}\n\nContext:\n${context}`;
    } else {
      const template = this.getTemplate(action, tone, length);
      prompt += template.replace('{context}', context);
    }

    // Add additional instructions if provided
    if (additionalInstructions) {
      prompt += `\n\nAdditional instructions: ${additionalInstructions}`;
    }

    return prompt;
  }

  /**
   * Build a conversational prompt with history
   */
  static buildConversationalPrompt(
    context: string,
    history: Array<{ role: 'user' | 'assistant'; content: string }>,
    userMessage: string
  ): string {
    let prompt = `${this.SYSTEM_PROMPT}\n\n`;
    prompt += `Selected text context:\n${context}\n\n`;
    prompt += `Conversation history:\n`;

    // Add conversation history
    for (const message of history) {
      prompt += `${message.role === 'user' ? 'User' : 'Assistant'}: ${message.content}\n`;
    }

    // Add current user message
    prompt += `User: ${userMessage}\nAssistant:`;

    return prompt;
  }

  /**
   * Get template based on action and options
   */
  private static getTemplate(
    action: PromptAction,
    tone?: string,
    length?: string
  ): string {
    const templates = this.ACTION_TEMPLATES[action];
    
    if (!templates) {
      return 'Process this text:\n\n{context}';
    }

    const key = tone || length || 'medium';
    return templates[key] || templates['medium'] || Object.values(templates)[0];
  }

  /**
   * Estimate token count (rough approximation)
   */
  static estimateTokenCount(text: string): number {
    // Rough estimate: 1 token ≈ 4 characters
    return Math.ceil(text.length / 4);
  }

  /**
   * Truncate context to fit within token limit
   */
  static truncateContext(context: string, maxTokens: number): string {
    const estimatedTokens = this.estimateTokenCount(context);
    
    if (estimatedTokens <= maxTokens) {
      return context;
    }

    // Truncate to approximate character count
    const maxChars = maxTokens * 4;
    return context.substring(0, maxChars) + '...';
  }
}
```

### 3. Context Manager

**File**: `src/main/services/ai/context-manager.ts`

```typescript
import { PromptBuilder } from './prompt-builder';

export interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number;
}

export interface ConversationContext {
  id: string;
  selectedText: string;
  messages: Message[];
  metadata: {
    application: string;
    timestamp: number;
    location?: string;
  };
}

export class ContextManager {
  private readonly maxContextTokens: number;
  private readonly maxMessages: number;

  constructor(maxContextTokens: number = 4096, maxMessages: number = 20) {
    this.maxContextTokens = maxContextTokens;
    this.maxMessages = maxMessages;
  }

  /**
   * Build context for AI request
   */
  buildContext(conversation: ConversationContext, newMessage: string): string {
    const { selectedText, messages } = conversation;

    // Calculate token budget
    const selectedTextTokens = PromptBuilder.estimateTokenCount(selectedText);
    const newMessageTokens = PromptBuilder.estimateTokenCount(newMessage);
    const systemPromptTokens = 100; // Approximate
    
    let remainingTokens = this.maxContextTokens - selectedTextTokens - newMessageTokens - systemPromptTokens;

    // Select messages that fit within token budget
    const relevantMessages: Message[] = [];
    
    // Start from most recent messages
    for (let i = messages.length - 1; i >= 0 && relevantMessages.length < this.maxMessages; i--) {
      const message = messages[i];
      const messageTokens = PromptBuilder.estimateTokenCount(message.content);
      
      if (messageTokens <= remainingTokens) {
        relevantMessages.unshift(message);
        remainingTokens -= messageTokens;
      } else {
        break;
      }
    }

    // Build conversational prompt
    return PromptBuilder.buildConversationalPrompt(
      selectedText,
      relevantMessages.map(m => ({ role: m.role, content: m.content })),
      newMessage
    );
  }

  /**
   * Add message to conversation
   */
  addMessage(conversation: ConversationContext, role: 'user' | 'assistant', content: string): Message {
    const message: Message = {
      id: this.generateMessageId(),
      role,
      content,
      timestamp: Date.now(),
    };

    conversation.messages.push(message);

    // Trim old messages if exceeding limit
    if (conversation.messages.length > this.maxMessages * 2) {
      conversation.messages = conversation.messages.slice(-this.maxMessages);
    }

    return message;
  }

  /**
   * Create new conversation
   */
  createConversation(selectedText: string, application: string): ConversationContext {
    return {
      id: this.generateConversationId(),
      selectedText,
      messages: [],
      metadata: {
        application,
        timestamp: Date.now(),
      },
    };
  }

  /**
   * Generate unique message ID
   */
  private generateMessageId(): string {
    return `msg_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }

  /**
   * Generate unique conversation ID
   */
  private generateConversationId(): string {
    return `conv_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}
```

### 4. Response Cache

**File**: `src/main/services/ai/cache.ts`

```typescript
import crypto from 'crypto';
import { logger } from '@main/utils/logger';

interface CacheEntry {
  response: string;
  timestamp: number;
  tokenCount: number;
}

export class ResponseCache {
  private cache: Map<string, CacheEntry>;
  private readonly ttl: number;
  private readonly maxSize: number;

  constructor(ttlSeconds: number = 3600, maxSize: number = 100) {
    this.cache = new Map();
    this.ttl = ttlSeconds * 1000;
    this.maxSize = maxSize;
  }

  /**
   * Get cached response
   */
  get(prompt: string): string | null {
    const key = this.generateKey(prompt);
    const entry = this.cache.get(key);

    if (!entry) {
      return null;
    }

    // Check if expired
    if (Date.now() - entry.timestamp > this.ttl) {
      this.cache.delete(key);
      return null;
    }

    logger.info('Cache hit', { key });
    return entry.response;
  }

  /**
   * Set cached response
   */
  set(prompt: string, response: string, tokenCount: number): void {
    const key = this.generateKey(prompt);

    // Evict oldest entry if cache is full
    if (this.cache.size >= this.maxSize) {
      const oldestKey = this.cache.keys().next().value;
      this.cache.delete(oldestKey);
    }

    this.cache.set(key, {
      response,
      timestamp: Date.now(),
      tokenCount,
    });

    logger.info('Cache set', { key, tokenCount });
  }

  /**
   * Clear cache
   */
  clear(): void {
    this.cache.clear();
    logger.info('Cache cleared');
  }

  /**
   * Get cache statistics
   */
  getStats(): { size: number; maxSize: number; hitRate: number } {
    return {
      size: this.cache.size,
      maxSize: this.maxSize,
      hitRate: 0, // TODO: Implement hit rate tracking
    };
  }

  /**
   * Generate cache key from prompt
   */
  private generateKey(prompt: string): string {
    return crypto.createHash('sha256').update(prompt).digest('hex');
  }
}
```

## Usage Examples

### Basic Text Generation

```typescript
import { WatsonxClient } from '@main/services/ai/watsonx-client';
import { PromptBuilder, PromptAction } from '@main/services/ai/prompt-builder';

const client = new WatsonxClient({
  apiKey: process.env.WATSONX_API_KEY!,
  projectId: process.env.WATSONX_PROJECT_ID!,
  endpoint: process.env.WATSONX_ENDPOINT!,
  modelId: process.env.WATSONX_MODEL_ID!,
});

// Summarize text
const prompt = PromptBuilder.buildPrompt({
  action: PromptAction.SUMMARIZE,
  context: 'Your selected text here...',
  length: 'short',
});

const response = await client.generateText({ prompt });
console.log(response.text);
```

### Streaming Generation

```typescript
// Stream response for real-time display
const prompt = PromptBuilder.buildPrompt({
  action: PromptAction.EXPLAIN,
  context: 'Complex technical text...',
  length: 'medium',
});

for await (const chunk of client.streamGeneration({ prompt })) {
  // Send chunk to renderer process
  mainWindow.webContents.send('ai-response-chunk', chunk);
}
```

### Conversational Context

```typescript
import { ContextManager } from '@main/services/ai/context-manager';

const contextManager = new ContextManager();

// Create conversation
const conversation = contextManager.createConversation(
  'Selected text from document',
  'Microsoft Word'
);

// Add user message
contextManager.addMessage(conversation, 'user', 'Can you explain this?');

// Build context for AI
const prompt = contextManager.buildContext(conversation, 'Can you explain this?');

// Generate response
const response = await client.generateText({ prompt });

// Add assistant response
contextManager.addMessage(conversation, 'assistant', response.text);
```

### With Caching

```typescript
import { ResponseCache } from '@main/services/ai/cache';

const cache = new ResponseCache(3600, 100);

async function generateWithCache(prompt: string) {
  // Check cache first
  const cached = cache.get(prompt);
  if (cached) {
    return cached;
  }

  // Generate new response
  const response = await client.generateText({ prompt });
  
  // Cache the response
  cache.set(prompt, response.text, response.tokenCount);
  
  return response.text;
}
```

## Best Practices

### 1. Prompt Engineering

- **Be specific**: Clear instructions yield better results
- **Provide context**: Include relevant background information
- **Set constraints**: Specify length, tone, format requirements
- **Use examples**: Show desired output format when possible

### 2. Error Handling

```typescript
try {
  const response = await client.generateText({ prompt });
  return response.text;
} catch (error) {
  if (error.message.includes('Rate limit')) {
    // Queue request for retry
    return 'Request queued. Please wait...';
  } else if (error.message.includes('Authentication')) {
    // Prompt user to re-enter API key
    return 'Authentication failed. Please check settings.';
  } else {
    // Generic error
    return 'An error occurred. Please try again.';
  }
}
```

### 3. Rate Limiting

- Implement request queuing for high-volume usage
- Show user feedback when rate limited
- Consider implementing exponential backoff

### 4. Token Management

- Monitor token usage to avoid exceeding limits
- Truncate long contexts intelligently
- Prioritize recent messages in conversations

### 5. Caching Strategy

- Cache identical requests to reduce API calls
- Set appropriate TTL based on content type
- Clear cache periodically to prevent stale data

## Testing

### Unit Tests

```typescript
import { describe, it, expect, vi } from 'vitest';
import { WatsonxClient } from './watsonx-client';

describe('WatsonxClient', () => {
  it('should generate text successfully', async () => {
    const client = new WatsonxClient({
      apiKey: 'test-key',
      projectId: 'test-project',
      endpoint: 'https://test.com',
      modelId: 'test-model',
    });

    const response = await client.generateText({
      prompt: 'Hello',
      maxNewTokens: 10,
    });

    expect(response.text).toBeDefined();
    expect(response.tokenCount).toBeGreaterThan(0);
  });
});
```

### Integration Tests

```typescript
describe('AI Integration', () => {
  it('should handle full workflow', async () => {
    const client = new WatsonxClient(config);
    const contextManager = new ContextManager();
    
    const conversation = contextManager.createConversation(
      'Test text',
      'Test App'
    );
    
    const prompt = contextManager.buildContext(conversation, 'Summarize this');
    const response = await client.generateText({ prompt });
    
    expect(response.text).toBeDefined();
  });
});
```

## Monitoring & Analytics

### Track API Usage

```typescript
class UsageTracker {
  private totalRequests = 0;
  private totalTokens = 0;
  private errors = 0;

  trackRequest(tokenCount: number) {
    this.totalRequests++;
    this.totalTokens += tokenCount;
  }

  trackError() {
    this.errors++;
  }

  getStats() {
    return {
      totalRequests: this.totalRequests,
      totalTokens: this.totalTokens,
      errors: this.errors,
      averageTokensPerRequest: this.totalTokens / this.totalRequests,
    };
  }
}
```

## Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify API key is correct
   - Check if API key has expired
   - Ensure proper IAM permissions

2. **Rate Limiting**
   - Implement request queuing
   - Add delays between requests
   - Consider upgrading plan

3. **Slow Responses**
   - Use streaming for better UX
   - Reduce max_new_tokens
   - Implement caching

4. **Poor Quality Responses**
   - Refine prompts
   - Adjust temperature/top_p
   - Try different models

## Resources

- [IBM watsonx.ai Documentation](https://cloud.ibm.com/docs/watsonx-ai)
- [IBM Cloud SDK for Node.js](https://github.com/IBM/node-sdk-core)
- [watsonx.ai API Reference](https://cloud.ibm.com/apidocs/watsonx-ai)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## Conclusion

This integration guide provides everything needed to successfully integrate IBM watsonx into SmartClick. Follow the implementation patterns, best practices, and error handling strategies to create a robust AI-powered experience.
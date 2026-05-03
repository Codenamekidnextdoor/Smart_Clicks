"""
IBM watsonx AI Client for SmartClick
Handles all communication with IBM Bob/watsonx API
Supports text generation, streaming responses, and context management.
"""

import os
import json
import logging
from typing import Optional, Generator, Dict, Any

# IBM SDK is optional — only needed for real watsonx; MockWatsonxClient works without it
try:
    from ibm_watsonx_ai.foundation_models import ModelInference
    from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
    from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
    _IBM_SDK_AVAILABLE = True
except ImportError:
    _IBM_SDK_AVAILABLE = False

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WatsonxClient:
    """
    Client for interacting with IBM watsonx AI.
    Handles authentication, text generation, and streaming responses.
    """
    
    def __init__(self, api_key: str, project_id: str, endpoint: str = None):
        """
        Initialize the watsonx client.
        
        Args:
            api_key: IBM Cloud API key
            project_id: watsonx.ai project ID
            endpoint: API endpoint URL (default: us-south)
        """
        self.api_key = api_key
        self.project_id = project_id
        self.endpoint = endpoint or "https://us-south.ml.cloud.ibm.com"
        
        # Default model
        self.model_id = "ibm/granite-13b-chat-v2"
        
        # Initialize credentials
        self.credentials = {
            "url": self.endpoint,
            "apikey": self.api_key
        }
        
        if not _IBM_SDK_AVAILABLE:
            raise ImportError(
                "ibm_watsonx_ai is not installed. Run: pip install ibm-watsonx-ai"
            )

        # Generation parameters
        self.params = {
            GenParams.MAX_NEW_TOKENS: 1024,
            GenParams.TEMPERATURE: 0.7,
            GenParams.TOP_P: 0.9,
            GenParams.TOP_K: 50,
            GenParams.REPETITION_PENALTY: 1.1,
        }
        
        logger.info(f"WatsonxClient initialized with model: {self.model_id}")
        
    def _get_model(self) -> ModelInference:
        """
        Create and return a ModelInference instance.
        
        Returns:
            Configured ModelInference instance
        """
        try:
            model = ModelInference(
                model_id=self.model_id,
                params=self.params,
                credentials=self.credentials,
                project_id=self.project_id
            )
            return model
        except Exception as e:
            logger.error(f"Failed to create model: {e}")
            raise
            
    def generate_text(self, prompt: str, max_tokens: int = None) -> str:
        """
        Generate text response from watsonx.
        
        Args:
            prompt: Input prompt text
            max_tokens: Maximum tokens to generate (overrides default)
            
        Returns:
            Generated text response
        """
        try:
            # Update params if max_tokens specified
            if max_tokens:
                self.params[GenParams.MAX_NEW_TOKENS] = max_tokens
                
            model = self._get_model()
            
            logger.info(f"Generating text for prompt: {prompt[:50]}...")
            
            # Generate response
            response = model.generate_text(prompt=prompt)
            
            logger.info(f"Generated {len(response)} characters")
            
            return response
            
        except Exception as e:
            logger.error(f"Text generation failed: {e}")
            raise
            
    def generate_text_stream(self, prompt: str, max_tokens: int = None) -> Generator[str, None, None]:
        """
        Generate text response with streaming (real-time output).
        
        Args:
            prompt: Input prompt text
            max_tokens: Maximum tokens to generate
            
        Yields:
            Text chunks as they are generated
        """
        try:
            # Update params if max_tokens specified
            if max_tokens:
                self.params[GenParams.MAX_NEW_TOKENS] = max_tokens
                
            model = self._get_model()
            
            logger.info(f"Streaming text for prompt: {prompt[:50]}...")
            
            # Stream response
            for chunk in model.generate_text_stream(prompt=prompt):
                yield chunk
                
        except Exception as e:
            logger.error(f"Streaming generation failed: {e}")
            raise
            
    def summarize(self, text: str, length: str = "medium") -> str:
        """
        Summarize the given text.
        
        Args:
            text: Text to summarize
            length: Summary length (short/medium/long)
            
        Returns:
            Summary text
        """
        length_instructions = {
            "short": "in 1-2 sentences",
            "medium": "in a concise paragraph",
            "long": "in detail, including key points"
        }
        
        instruction = length_instructions.get(length, length_instructions["medium"])
        prompt = f"Summarize the following text {instruction}:\n\n{text}"
        
        return self.generate_text(prompt)
        
    def rewrite(self, text: str, tone: str = "professional") -> str:
        """
        Rewrite text in a different tone.
        
        Args:
            text: Text to rewrite
            tone: Desired tone (professional/casual/friendly/formal)
            
        Returns:
            Rewritten text
        """
        prompt = f"Rewrite the following text in a {tone} tone:\n\n{text}"
        return self.generate_text(prompt)
        
    def explain(self, text: str, level: str = "simple") -> str:
        """
        Explain the given text.
        
        Args:
            text: Text to explain
            level: Explanation level (simple/detailed/technical)
            
        Returns:
            Explanation text
        """
        level_instructions = {
            "simple": "in simple terms that anyone can understand",
            "detailed": "in detail with examples",
            "technical": "with technical depth and precision"
        }
        
        instruction = level_instructions.get(level, level_instructions["simple"])
        prompt = f"Explain the following text {instruction}:\n\n{text}"
        
        return self.generate_text(prompt)
        
    def analyze(self, text: str) -> str:
        """
        Analyze the given text and provide insights.
        
        Args:
            text: Text to analyze
            
        Returns:
            Analysis text
        """
        prompt = f"Analyze the following text and provide insights:\n\n{text}"
        return self.generate_text(prompt)
        
    def custom_prompt(self, text: str, custom_instruction: str) -> str:
        """
        Process text with a custom instruction.
        
        Args:
            text: Context text
            custom_instruction: Custom instruction for processing
            
        Returns:
            Processed text
        """
        prompt = f"{custom_instruction}\n\nContext:\n{text}"
        return self.generate_text(prompt)
        
    def chat(self, message: str, context: str = None, history: list = None) -> str:
        """
        Have a conversation with context.
        
        Args:
            message: User message
            context: Selected text context
            history: Previous conversation messages
            
        Returns:
            AI response
        """
        # Build conversation prompt
        prompt = "You are IBM Bob, an AI assistant helping with text-related tasks.\n\n"
        
        if context:
            prompt += f"Selected text context:\n{context}\n\n"
            
        if history:
            prompt += "Conversation history:\n"
            for msg in history[-5:]:  # Last 5 messages for context
                role = "User" if msg['role'] == 'user' else "Assistant"
                prompt += f"{role}: {msg['content']}\n"
            prompt += "\n"
            
        prompt += f"User: {message}\nAssistant:"
        
        return self.generate_text(prompt)


class MockWatsonxClient:
    """
    Mock client for testing without API credentials.
    Returns simulated responses.
    """
    
    def __init__(self, api_key: str = None, project_id: str = None, endpoint: str = None):
        """Initialize mock client."""
        logger.info("MockWatsonxClient initialized (no real API calls)")
        
    def generate_text(self, prompt: str, max_tokens: int = None) -> str:
        """Return mock response."""
        import time
        time.sleep(1)  # Simulate API delay
        return f"[Mock Response] This is a simulated response to: {prompt[:50]}..."
        
    def generate_text_stream(self, prompt: str, max_tokens: int = None) -> Generator[str, None, None]:
        """Return mock streaming response."""
        import time
        response = f"This is a simulated streaming response to your prompt about: {prompt[:30]}..."
        for word in response.split():
            time.sleep(0.1)
            yield word + " "
            
    def summarize(self, text: str, length: str = "medium") -> str:
        """Return mock summary."""
        return f"[Mock Summary] This text discusses: {text[:50]}..."
        
    def rewrite(self, text: str, tone: str = "professional") -> str:
        """Return mock rewrite."""
        return f"[Mock Rewrite in {tone} tone] {text[:100]}..."
        
    def explain(self, text: str, level: str = "simple") -> str:
        """Return mock explanation."""
        return f"[Mock Explanation] This text means: {text[:50]}..."
        
    def analyze(self, text: str) -> str:
        """Return mock analysis."""
        return f"[Mock Analysis] Key insights from this text: {text[:50]}..."
        
    def custom_prompt(self, text: str, custom_instruction: str) -> str:
        """Return mock custom response."""
        return f"[Mock Custom] Processed with instruction: {custom_instruction[:30]}..."
        
    def chat(self, message: str, context: str = None, history: list = None) -> str:
        """Return mock chat response."""
        return f"[Mock Chat] Response to: {message[:50]}..."


def create_client(api_key: str = None, project_id: str = None, use_mock: bool = False) -> WatsonxClient:
    """
    Factory function to create appropriate client.
    
    Args:
        api_key: IBM Cloud API key
        project_id: watsonx project ID
        use_mock: Use mock client for testing
        
    Returns:
        WatsonxClient or MockWatsonxClient instance
    """
    if use_mock or not api_key or not project_id:
        logger.warning("Using mock client (no real API calls)")
        return MockWatsonxClient()
    else:
        return WatsonxClient(api_key, project_id)


# Example usage
if __name__ == "__main__":
    # Load credentials from environment
    api_key = os.getenv("WATSONX_API_KEY")
    project_id = os.getenv("WATSONX_PROJECT_ID")
    
    # Create client (will use mock if no credentials)
    client = create_client(api_key, project_id, use_mock=True)
    
    # Test text
    test_text = "Machine learning is a subset of artificial intelligence that enables computers to learn from data."
    
    # Test different operations
    print("\n=== Testing Summarize ===")
    summary = client.summarize(test_text)
    print(summary)
    
    print("\n=== Testing Rewrite ===")
    rewrite = client.rewrite(test_text, tone="casual")
    print(rewrite)
    
    print("\n=== Testing Explain ===")
    explanation = client.explain(test_text)
    print(explanation)
    
    print("\n=== Testing Streaming ===")
    print("Streaming response: ", end="", flush=True)
    for chunk in client.generate_text_stream("What is AI?"):
        print(chunk, end="", flush=True)
    print("\n")

# Made with Bob

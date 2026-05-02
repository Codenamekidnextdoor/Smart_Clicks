import { app } from 'electron';
import dotenv from 'dotenv';
import { logger } from './utils/logger';
import { registerAIHandlers } from './ipc/ai.handler';

// Load environment variables
dotenv.config();

export async function initializeApp(): Promise<void> {
  try {
    logger.info('Initializing SmartClick...');

    // Verify required environment variables
    const requiredEnvVars = [
      'WATSONX_API_KEY',
      'WATSONX_PROJECT_ID',
      'WATSONX_ENDPOINT',
    ];

    const missingVars = requiredEnvVars.filter(
      (varName) => !process.env[varName]
    );

    if (missingVars.length > 0) {
      logger.error('Missing required environment variables:', missingVars);
      throw new Error(
        `Missing environment variables: ${missingVars.join(', ')}`
      );
    }

    logger.info('Environment variables loaded successfully');

    // Register IPC handlers
    registerAIHandlers();
    logger.info('IPC handlers registered');

    logger.info('SmartClick initialized successfully');
  } catch (error) {
    logger.error('Failed to initialize app:', error);
    throw error;
  }
}

export function getAppVersion(): string {
  return app.getVersion();
}

export function getAppPath(): string {
  return app.getAppPath();
}

// Made with Bob

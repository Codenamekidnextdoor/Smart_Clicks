import { ipcMain } from 'electron';
import { getWatsonxClient } from '../services/ai/watsonx-client';
import { logger } from '../utils/logger';

export function registerAIHandlers(): void {
  const watsonx = getWatsonxClient();

  // Summarize text
  ipcMain.handle('ai:summarize', async (_event, text: string) => {
    try {
      logger.info('Handling summarize request');
      const result = await watsonx.summarize(text);
      return result;
    } catch (error) {
      logger.error('Summarize failed', { error });
      throw error;
    }
  });

  // Rewrite text
  ipcMain.handle('ai:rewrite', async (_event, { text, tone }: { text: string; tone: string }) => {
    try {
      logger.info('Handling rewrite request', { tone });
      const result = await watsonx.rewrite(text, tone);
      return result;
    } catch (error) {
      logger.error('Rewrite failed', { error });
      throw error;
    }
  });

  // Explain text
  ipcMain.handle('ai:explain', async (_event, text: string) => {
    try {
      logger.info('Handling explain request');
      const result = await watsonx.explain(text);
      return result;
    } catch (error) {
      logger.error('Explain failed', { error });
      throw error;
    }
  });

  // Analyze text
  ipcMain.handle('ai:analyze', async (_event, text: string) => {
    try {
      logger.info('Handling analyze request');
      const result = await watsonx.analyze(text);
      return result;
    } catch (error) {
      logger.error('Analyze failed', { error });
      throw error;
    }
  });

  // Custom prompt
  ipcMain.handle('ai:custom', async (_event, { text, prompt }: { text: string; prompt: string }) => {
    try {
      logger.info('Handling custom prompt request');
      const result = await watsonx.custom(text, prompt);
      return result;
    } catch (error) {
      logger.error('Custom prompt failed', { error });
      throw error;
    }
  });

  logger.info('AI IPC handlers registered');
}

// Made with Bob

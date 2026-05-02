import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  root: path.join(__dirname, 'src/renderer'),
  base: './',
  build: {
    outDir: path.join(__dirname, 'dist/renderer'),
    emptyOutDir: true,
    rollupOptions: {
      input: {
        overlay: path.join(__dirname, 'src/renderer/overlay/index.html'),
        setup: path.join(__dirname, 'src/renderer/setup/index.html'),
      },
    },
  },
  resolve: {
    alias: {
      '@renderer': path.join(__dirname, 'src/renderer'),
      '@shared': path.join(__dirname, 'src/shared'),
    },
  },
  server: {
    port: 5173,
  },
});

// Made with Bob

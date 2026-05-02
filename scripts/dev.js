const { spawn } = require('child_process');
const path = require('path');

console.log('🚀 Starting SmartClick in development mode...\n');

// Start Vite dev server for renderer
console.log('📦 Starting Vite dev server...');
const vite = spawn('npx', ['vite'], {
  cwd: process.cwd(),
  shell: true,
  stdio: 'inherit',
});

// Wait a bit for Vite to start, then compile and start Electron
setTimeout(() => {
  console.log('\n⚡ Compiling TypeScript...');
  const tsc = spawn('npx', ['tsc', '-p', 'tsconfig.main.json'], {
    cwd: process.cwd(),
    shell: true,
    stdio: 'inherit',
  });

  tsc.on('close', (code) => {
    if (code === 0) {
      console.log('\n🎯 Starting Electron...');
      const electron = spawn('npx', ['electron', '.'], {
        cwd: process.cwd(),
        shell: true,
        stdio: 'inherit',
        env: { ...process.env, NODE_ENV: 'development' },
      });

      electron.on('close', () => {
        console.log('\n👋 Electron closed. Stopping dev server...');
        vite.kill();
        process.exit(0);
      });
    } else {
      console.error('❌ TypeScript compilation failed');
      vite.kill();
      process.exit(1);
    }
  });
}, 3000);

// Handle Ctrl+C
process.on('SIGINT', () => {
  console.log('\n\n👋 Shutting down...');
  vite.kill();
  process.exit(0);
});

// Made with Bob

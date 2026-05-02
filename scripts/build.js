const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('🏗️  Building SmartClick for production...\n');

// Clean dist folder
console.log('🧹 Cleaning dist folder...');
const distPath = path.join(process.cwd(), 'dist');
if (fs.existsSync(distPath)) {
  fs.rmSync(distPath, { recursive: true, force: true });
}

try {
  // Build main process
  console.log('\n⚡ Compiling main process (TypeScript)...');
  execSync('npx tsc -p tsconfig.main.json', {
    stdio: 'inherit',
    cwd: process.cwd(),
  });
  console.log('✅ Main process compiled');

  // Build renderer process
  console.log('\n📦 Building renderer process (Vite)...');
  execSync('npx vite build', {
    stdio: 'inherit',
    cwd: process.cwd(),
  });
  console.log('✅ Renderer process built');

  console.log('\n✨ Build complete! Ready to package with: npm run package');
} catch (error) {
  console.error('\n❌ Build failed:', error.message);
  process.exit(1);
}

// Made with Bob

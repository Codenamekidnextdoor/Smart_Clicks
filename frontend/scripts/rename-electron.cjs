/**
 * Post-compile script: renames dist-electron/*.js -> *.cjs
 * Required because package.json has "type": "module" but Electron main
 * process must be CommonJS. TypeScript compiles to .js; we rename to .cjs
 * so Node loads them as CJS regardless of the package type field.
 */

const fs = require('fs');
const path = require('path');

const distDir = path.join(__dirname, '..', 'dist-electron');

if (!fs.existsSync(distDir)) {
  console.error('dist-electron directory not found. Did tsc compile successfully?');
  process.exit(1);
}

const files = fs.readdirSync(distDir);
const jsFiles = files.filter(f => f.endsWith('.js'));

if (jsFiles.length === 0) {
  console.log('No .js files found in dist-electron (may already be renamed).');
} else {
  for (const file of jsFiles) {
    const oldPath = path.join(distDir, file);
    const newPath = path.join(distDir, file.replace(/\.js$/, '.cjs'));
    fs.renameSync(oldPath, newPath);
    console.log(`Renamed: ${file} -> ${file.replace(/\.js$/, '.cjs')}`);
  }
}

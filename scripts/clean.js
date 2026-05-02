const fs = require('fs');
const path = require('path');

console.log('🧹 Cleaning build artifacts...\n');

const foldersToClean = ['dist', 'release', 'out'];

foldersToClean.forEach((folder) => {
  const folderPath = path.join(process.cwd(), folder);
  if (fs.existsSync(folderPath)) {
    console.log(`Removing ${folder}/...`);
    fs.rmSync(folderPath, { recursive: true, force: true });
    console.log(`✅ ${folder}/ removed`);
  } else {
    console.log(`⏭️  ${folder}/ doesn't exist, skipping`);
  }
});

console.log('\n✨ Clean complete!');

// Made with Bob

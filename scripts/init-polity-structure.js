const fs = require('fs');
const path = require('path');

/**
 * Script to initialize the GS Question Bank structure for Polity.
 * Run from the project root: node scripts/init-polity-structure.js
 */

const targetDir = path.join(__dirname, '../gs-question-bank/polity');

const folders = [
    'constitution',
    'constitutional-framework',
    'constitutional-development',
    'constitutional-amendments',
    'schedules',
    'important-articles',
    'fundamental-rights',
    'dpsp-and-fundamental-duties',
    'citizenship',
    'union-government',
    'state-government',
    'parliament',
    'judiciary',
    'emergency-provisions',
    'centre-state-relations',
    'federalism',
    'elections',
    'local-government',
    'constitutional-bodies',
    'non-constitutional-bodies',
    'landmark-judgements',
    'committees-and-commissions',
    'governance'
];

console.log(`Initializing structure in: ${targetDir}`);

folders.forEach(folder => {
    const folderPath = path.join(targetDir, folder);
    if (!fs.existsSync(folderPath)) {
        fs.mkdirSync(folderPath, { recursive: true });
        console.log(`✅ Created: ${folder}`);
    } else {
        console.log(`ℹ️ Already exists: ${folder}`);
    }
});

console.log('Polity structure setup complete.');
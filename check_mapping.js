const fs = require('fs');
const path = require('path');

const subjects = [
    { prefix: 'hindi', folder: 'hindi' },
    { prefix: 'sanskrit', folder: 'sanskrit' },
    { prefix: 'eng', folder: 'english' },
    { prefix: 'sci', folder: 'science' },
    { prefix: 'math', folder: 'mathematics' },
    { prefix: 'teach', folder: 'teaching-skills' },
    { prefix: 'psych', folder: 'child-psychology' },
    { prefix: 'social', folder: 'environmental-social-studies' },
    { prefix: 'gk', folder: 'gk-current-affairs' },
    { prefix: 'reas', folder: 'logical-reasoning' },
    { prefix: 'it', folder: 'information-technology' },
    { prefix: 'life', folder: 'life-skill-management' }
];

for (const subj of subjects) {
    const dirPath = path.join('up-assistant-teacher', subj.folder);
    if (fs.existsSync(dirPath)) {
        const subdirs = fs.readdirSync(dirPath, { withFileTypes: true })
            .filter(dirent => dirent.isDirectory())
            .map(dirent => dirent.name);
        console.log(`=== ${subj.prefix} (${subj.folder}) [${subdirs.length} dirs] ===`);
        subdirs.forEach((d, idx) => console.log(`  ${idx + 1}: ${d}`));
    } else {
        console.log(`=== ${subj.prefix} (${subj.folder}) NOT FOUND ===`);
    }
}

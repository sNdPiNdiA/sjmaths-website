const fs = require('fs');
const path = require('path');

// Define the mapping of old folder names to new folder names
const folderMapping = {
    '1-1-binary-numbers': 'binary-numbers',
    '1-2-indices-logarithm-and-antilogarithm': 'indices-logarithm-and-antilogarithm',
    '1-3-introduction-to-bhartiya-system-of-numeration': 'introduction-to-bhartiya-system-of-numeration',
    '1-4-clocks': 'clocks',
    '1-5-calendar': 'calendar',
    '1-6-time-and-work': 'time-and-work',
    '1-7-speed-distance-and-time': 'speed-distance-and-time',
    '1-8-seating-arrangement': 'seating-arrangement',
    '2-1-introduction-to-sets': 'introduction-to-sets',
    '2-2-subsets': 'subsets',
    '2-3-venn-diagrams': 'venn-diagrams',
    '2-4-ordered-pairs': 'ordered-pairs',
    '2-5-relations': 'relations',
    '2-6-mathematical-logic': 'mathematical-logic',
    '2-7-sequence-and-series': 'sequence-and-series',
    '2-8-arithmetic-progression': 'arithmetic-progression',
    '2-9-geometric-progression': 'geometric-progression',
    '3-1-functions-and-their-graphs': 'functions-and-their-graphs',
    '3-2-limits-and-continuity': 'limits-and-continuity',
    '3-3-differentiation': 'differentiation',
    '3-4-algebra-of-derivatives': 'algebra-of-derivatives',
    '4-1-combinatorics': 'combinatorics',
    '4-2-probability': 'probability',
    '5-1-measures-of-dispersion': 'measures-of-dispersion',
    '5-2-percentiles': 'percentiles',
    '5-3-correlation': 'correlation',
    '5-4-regression': 'regression',
    '6-1-interest-and-interest-rates': 'interest-and-interest-rates',
    '6-2-annuities': 'annuities',
    '6-3-taxes-and-utility-bills': 'taxes-and-utility-bills',
    '7-1-straight-lines': 'straight-lines',
    '7-2-circles-and-parabola': 'circles-and-parabola'
};

const baseDir = 'class-11-applied-mathematics';

console.log('Starting folder rename process...\n');

// Step 1: Rename folders
Object.keys(folderMapping).forEach(oldName => {
    const newName = folderMapping[oldName];
    const oldPath = path.join(baseDir, oldName);
    const newPath = path.join(baseDir, newName);

    if (fs.existsSync(oldPath)) {
        try {
            fs.renameSync(oldPath, newPath);
            console.log(`✓ Renamed: ${oldName} → ${newName}`);
        } catch (error) {
            console.error(`✗ Error renaming ${oldName}:`, error.message);
        }
    } else {
        console.log(`⚠ Folder not found: ${oldName}`);
    }
});

console.log('\n✓ Folder renaming complete!\n');

// Step 2: Update references in index.html
const indexPath = path.join(baseDir, 'index.html');
if (fs.existsSync(indexPath)) {
    let content = fs.readFileSync(indexPath, 'utf8');
    let updateCount = 0;

    // Replace all occurrences of old folder names with new ones
    Object.keys(folderMapping).forEach(oldName => {
        const newName = folderMapping[oldName];
        const regex = new RegExp(`./${oldName}/`, 'g');
        const matches = content.match(regex);
        if (matches) {
            content = content.replace(regex, `./${newName}/`);
            updateCount += matches.length;
            console.log(`✓ Updated ${matches.length} references: ${oldName} → ${newName}`);
        }
    });

    fs.writeFileSync(indexPath, content, 'utf8');
    console.log(`\n✓ Updated ${updateCount} total references in index.html`);
} else {
    console.error('✗ index.html not found!');
}

console.log('\n✓ All done!');
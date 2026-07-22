const fs = require('fs');
const path = require('path');

const reasoningTopicsList = JSON.parse(fs.readFileSync('reasoning_topics.json', 'utf8'));
const baseDir = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/reasoning';

const visualTopics = reasoningTopicsList.filter(relPath => 
    /figural|non-verbal|embedded|paper-folding|pattern-folding|venn|syllogism|visual|space-visualisation|blood-relations/i.test(relPath)
);

console.log('Visual Reasoning Topics requiring SVG re-generation (' + visualTopics.length + ' topics):');
visualTopics.forEach((t, i) => console.log((i+1) + '. ' + t));

visualTopics.forEach(relPath => {
    const indexPath = path.join(baseDir, relPath, 'index.html');
    if (fs.existsSync(indexPath)) {
        fs.unlinkSync(indexPath);
    }
});
console.log('✅ Cleared old files for visual topics to force SVG regeneration.');

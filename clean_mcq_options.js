const fs = require('fs');

const file = 'c:/Users/sande/Documents/GitHub/sjmaths-website/ssc-cgl/reasoning/analogies/semantic-analogy/index.html';
let content = fs.readFileSync(file, 'utf8');

// Strip "/ Hindi" in lang-en options and "/ English" in lang-hi options
content = content.replace(/(<span class="lang-en">\([A-D]\)\s*[^<\s/]+)\s*\/[^\n<]+/g, '$1</span>');
content = content.replace(/(<span class="lang-hi">\([A-D]\)\s*[^<\s/]+)\s*\/[^\n<]+/g, '$1</span>');

fs.writeFileSync(file, content, 'utf8');
console.log('✅ Successfully cleaned mixed slash option labels in semantic-analogy index.html');

const fs = require('fs');
const indexContent = fs.readFileSync('upsssc-lower-mains/history/social-aspects/index.html', 'utf8');

const regex = /<div id="tab-practice"[\s\S]*?(?=<div id="tab-pyqs">)/;
console.log("Match exists?", regex.test(indexContent));

const practiceIndex = indexContent.indexOf('<div id="tab-practice"');
const pyqsIndex = indexContent.indexOf('<div id="tab-pyqs"');
console.log("tab-practice index:", practiceIndex);
console.log("tab-pyqs index:", pyqsIndex);

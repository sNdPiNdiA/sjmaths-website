const fs = require('fs');

const tgt = fs.readFileSync('up-tgt-social-science/index.html', 'utf8');
const pgt = fs.readFileSync('up-pgt-economics/index.html', 'utf8');

function checkFile(name, content) {
  const matches = content.match(/href="(\/economics\/[^"]+)"/g) || [];
  let broken = 0;
  for (const m of matches) {
    const url = m.substring(6, m.length - 1);
    const diskPath = url.substring(1) + 'index.html';
    if (!fs.existsSync(diskPath)) {
      console.log(`[${name}] Broken: ${url} (File not found: ${diskPath})`);
      broken++;
    }
  }
  console.log(`[${name}] Total Economics links: ${matches.length}, Broken: ${broken}`);
}

checkFile('UP PGT Economics', pgt);
checkFile('UP TGT Social Science', tgt);

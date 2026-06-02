const fs = require('fs');
const path = require('path');

const PROCESSED_PATH = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed', '2026-06-01.json');

function check() {
  if (!fs.existsSync(PROCESSED_PATH)) {
    console.error("File not found:", PROCESSED_PATH);
    return;
  }

  const items = JSON.parse(fs.readFileSync(PROCESSED_PATH, 'utf8'));
  console.log(`Total processed items: ${items.length}\n`);

  items.forEach((item, index) => {
    console.log(`${index + 1}. [${item.source}] [${item.categories.join(', ')}] ${item.title}`);
  });
}

check();

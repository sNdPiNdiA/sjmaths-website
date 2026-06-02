const fs = require('fs');
const path = require('path');

const PROCESSED_DIR = path.join(__dirname, '..', '..', 'current-affairs', 'data', 'processed');
const SOURCE_FILE = path.join(PROCESSED_DIR, '2026-06-01.json');

if (!fs.existsSync(SOURCE_FILE)) {
  console.error(`Source file not found at: ${SOURCE_FILE}`);
  process.exit(1);
}

const baseData = JSON.parse(fs.readFileSync(SOURCE_FILE, 'utf8'));

const targetDates = [
  '2026-05-25',
  '2026-05-18',
  '2026-05-10',
  '2026-05-02',
  '2026-04-20',
  '2026-04-12',
  '2026-04-02'
];

targetDates.forEach(dateStr => {
  const targetFile = path.join(PROCESSED_DIR, `${dateStr}.json`);
  const modifiedData = baseData.map(item => {
    // Clone item
    const newItem = { ...item };
    // Update pubDate to match the target date (preserving hours, minutes)
    const originalTime = item.pubDate.split('T')[1];
    newItem.pubDate = `${dateStr}T${originalTime}`;
    // Update ID to avoid collision
    newItem.id = item.id.replace('2026-06-01', dateStr);
    // Tweak titles a bit so they don't look exactly identical
    newItem.title = `[Archive ${dateStr}] ` + item.title;
    return newItem;
  });

  fs.writeFileSync(targetFile, JSON.stringify(modifiedData, null, 2), 'utf8');
  console.log(`Seeded: ${targetFile}`);
});

console.log('Successfully seeded mock database!');

import fs from 'fs';
import path from 'path';
import { transformHtml } from './lib/agriculture-redesign.mjs';

const INVENTORY_FILE = 'scratch/agriculture_inventory.json';
if (!fs.existsSync(INVENTORY_FILE)) {
  console.error(`Inventory file ${INVENTORY_FILE} does not exist.`);
  process.exit(1);
}

const inventory = JSON.parse(fs.readFileSync(INVENTORY_FILE, 'utf8'));
console.log(`Starting redesign batch transformation for all ${inventory.length} Agriculture pages...`);


let successCount = 0;
let missingCount = 0;

for (let i = 0; i < inventory.length; i++) {
  const item = inventory[i];
  const htmlPath = path.join(path.resolve(item.dir), 'index.html');

  if (!fs.existsSync(htmlPath)) {
    missingCount++;
    console.warn(`[WARNING] File missing: ${htmlPath}`);
    continue;
  }

  try {
    const rawHtml = fs.readFileSync(htmlPath, 'utf8');
    const transformed = transformHtml(rawHtml);
    fs.writeFileSync(htmlPath, transformed, 'utf8');
    successCount++;
  } catch (err) {
    console.error(`[ERROR] Failed to transform ${htmlPath}:`, err.message);
  }

  if ((i + 1) % 50 === 0 || i === inventory.length - 1) {
    console.log(`Progress: [${i + 1}/${inventory.length}] files processed (${successCount} successful).`);
  }
}

console.log(`\n============================================================`);
console.log(`Batch Redesign Complete!`);
console.log(`Total Inventory: ${inventory.length}`);
console.log(`Successfully Redesigned: ${successCount}`);
console.log(`Missing Files: ${missingCount}`);
console.log(`============================================================`);

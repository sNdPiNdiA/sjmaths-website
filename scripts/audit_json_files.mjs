import fs from 'fs';
import path from 'path';

function walk(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  for (const file of files) {
    const full = path.join(dir, file);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      walk(full, fileList);
    } else if (file.endsWith('.json')) {
      fileList.push(full);
    }
  }
  return fileList;
}

const allJson = walk('upsc');
const baseNames = {};
const tabJsonNames = {};

for (const f of allJson) {
  const base = path.basename(f);
  baseNames[base] = (baseNames[base] || 0) + 1;
  if (f.includes(path.sep + 'tabs' + path.sep)) {
    tabJsonNames[base] = (tabJsonNames[base] || 0) + 1;
  }
}

console.log('Total JSON files in upsc:', allJson.length);
console.log('All JSON file basenames:', baseNames);
console.log('Tabs JSON file basenames:', tabJsonNames);


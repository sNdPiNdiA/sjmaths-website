import fs from 'fs';
import path from 'path';

function findFiles(dir, name, list = []) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      findFiles(full, name, list);
    } else if (f === name) {
      list.push(full);
      if (list.length >= 3) return list;
    }
  }
  return list;
}

console.log('Revision files:', findFiles('upsc', 'revision.json'));
console.log('Mains files:', findFiles('upsc', 'mains.json'));
console.log('Test files:', findFiles('upsc', 'test.json'));


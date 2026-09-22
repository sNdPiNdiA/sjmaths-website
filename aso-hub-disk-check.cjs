// Extract all topic-page links from the hub, classify pillar, compare with disk
const fs = require('fs'), path = require('path');
const hub = fs.readFileSync('upsc-aso/index.html', 'utf8');
const re = /href="\/upsc-aso\/([a-z0-9-]+)\/([a-z0-9-]+)\/"/g;
const PILLARS = new Set(['fluid-mechanics-machinery', 'aircraft-systems-instrumentation-maintenance', 'propulsion']);
const linked = {};
let m;
while ((m = re.exec(hub))) {
  const [_, p, s] = m;
  if (!PILLARS.has(p)) { console.log('NON-PILLAR LINK:', p + '/' + s); continue; }
  (linked[p] ||= new Set()).add(s);
}
const disk = {};
for (const p of PILLARS) {
  disk[p] = new Set(fs.readdirSync('upsc-aso/' + p).filter(d => d !== 'index.html'));
}
let hubTotal = 0, diskTotal = 0;
for (const p of PILLARS) {
  const h = linked[p] || new Set(), d = disk[p];
  hubTotal += h.size; diskTotal += d.size;
  const linkedNotOnDisk = [...h].filter(s => !d.has(s));
  const onDiskNotLinked = [...d].filter(s => !h.has(s));
  console.log(`\n== ${p} ==`);
  console.log(`hub links: ${h.size} | disk folders: ${d.size}`);
  if (linkedNotOnDisk.length) console.log('LINKED BUT NOT ON DISK (' + linkedNotOnDisk.length + '):\n  ' + linkedNotOnDisk.join('\n  '));
  if (onDiskNotLinked.length) console.log('ON DISK BUT NOT LINKED (' + onDiskNotLinked.length + '):\n  ' + onDiskNotLinked.join('\n  '));
  if (!linkedNotOnDisk.length && !onDiskNotLinked.length) console.log('hub and disk in sync');
}
console.log(`\nTOTAL hub topic links: ${hubTotal} | disk topic folders: ${diskTotal}`);

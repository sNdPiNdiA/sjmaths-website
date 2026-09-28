// Read-only pixel evidence for screenshot differences. This does NOT approve a
// visual change or relax the baseline capture's strict SHA comparison.
const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT } = require('./seo-html.cjs');

function comparePixels(before, after, width, height) {
  if (before.length !== after.length || before.length !== width * height * 4) throw new Error('Image dimensions differ.');
  let pixelsChanged = 0, maxChannelDelta = 0, totalDelta = 0;
  let left = width, top = height, right = -1, bottom = -1;
  for (let pixel = 0; pixel < width * height; pixel++) {
    let changed = false;
    for (let channel = 0; channel < 4; channel++) {
      const index = pixel * 4 + channel;
      const delta = Math.abs(before[index] - after[index]);
      maxChannelDelta = Math.max(maxChannelDelta, delta);
      totalDelta += delta;
      changed ||= delta !== 0;
    }
    if (!changed) continue;
    pixelsChanged++;
    const x = pixel % width, y = Math.floor(pixel / width);
    left = Math.min(left, x); right = Math.max(right, x);
    top = Math.min(top, y); bottom = Math.max(bottom, y);
  }
  return { width, height, pixelsChanged, maxChannelDelta, meanChannelDelta: totalDelta / before.length, bounds: pixelsChanged ? { left, top, right, bottom } : null };
}

async function main() {
  const [beforeLabel, afterLabel] = process.argv.slice(2);
  if (![beforeLabel, afterLabel].every(label => typeof label === 'string' && /^[a-z0-9-]+$/.test(label))) throw new Error('Usage: node scripts/inspect-screenshot-diffs.cjs before-label after-label');
  const directory = label => path.join(ROOT, 'scratch/refactor', label);
  const report = JSON.parse(fs.readFileSync(path.join(directory(afterLabel), 'comparison.json'), 'utf8'));
  if (report.comparedWith !== beforeLabel) throw new Error('Comparison does not use the requested baseline.');
  const browser = await chromium.launch({ headless: true });
  const results = [];
  try {
    const page = await browser.newPage();
    // Use the same tested comparator inside this isolated blank page. Keep RGBA
    // arrays in the browser rather than serializing millions of channel values.
    await page.addScriptTag({ content: comparePixels.toString() });
    for (const diff of report.differences.filter(diff => diff.issue === 'screenshot differs')) {
      const name = `${diff.id}-${diff.width}-${diff.theme}.png`;
      if (path.basename(name) !== name) throw new Error('Invalid screenshot name.');
      const pngs = [beforeLabel, afterLabel].map(label => fs.readFileSync(path.join(directory(label), name)).toString('base64'));
      const pixels = await page.evaluate(async pngs => {
        const images = await Promise.all(pngs.map(async png => {
          const img = new Image(); img.src = 'data:image/png;base64,' + png;
          await img.decode();
          const canvas = document.createElement('canvas');
          canvas.width = img.width; canvas.height = img.height;
          const context = canvas.getContext('2d'); context.drawImage(img, 0, 0);
          return { width: img.width, height: img.height, data: context.getImageData(0, 0, img.width, img.height).data };
        }));
        if (images[0].width !== images[1].width || images[0].height !== images[1].height) throw new Error('Image dimensions differ.');
        return comparePixels(images[0].data, images[1].data, images[0].width, images[0].height);
      }, pngs);
      results.push({ name, ...pixels });
    }
  } finally { await browser.close(); }
  console.log(JSON.stringify({ beforeLabel, afterLabel, results, reviewRequired: true }, null, 2));
}
module.exports = { comparePixels };
if (require.main === module) main().catch(error => { console.error(error); process.exitCode = 1; });

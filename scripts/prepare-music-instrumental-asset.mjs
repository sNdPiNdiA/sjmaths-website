import fs from 'fs';
import esbuild from 'esbuild';
import crypto from 'crypto';

const sampleFile = 'music-instrumental/avanaddh-vadya/bol-notation/kathin-layakari/index.html';
const content = fs.readFileSync(sampleFile, 'utf8');

const match = content.match(/<style\b[^>]*>([\s\S]*?)<\/style>/i);
if (!match) {
  console.error('No style block found in sample file!');
  process.exit(1);
}

const rawCss = match[1];
const cssTargetPath = 'assets/css/music-instrumental-topic.css';
const minTargetPath = 'assets/css/music-instrumental-topic.min.css';

const cleanCss = rawCss.replace(/\r\n/g, '\n').trim() + '\n';
fs.writeFileSync(cssTargetPath, cleanCss, 'utf8');
console.log(`Saved ${cleanCss.length} bytes to ${cssTargetPath}`);

esbuild.buildSync({
  entryPoints: [cssTargetPath],
  outfile: minTargetPath,
  minify: true,
  sourcemap: false
});

const minContent = fs.readFileSync(minTargetPath);
const hash = crypto.createHash('md5').update(minContent).digest('hex').slice(0, 8);
console.log(`Minified to ${minTargetPath} (${minContent.length} bytes) | Hash: ${hash}`);

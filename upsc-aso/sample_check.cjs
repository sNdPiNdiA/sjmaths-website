const fs = require('fs');
const html = fs.readFileSync('upsc-aso/index.html', 'utf8');
const linkRegex = /href="([^"]+)"[^>]*class="microtopic-link"[^>]*>([^<]+)<\/a>/gi;
let m;
const samples = [];
while ((m = linkRegex.exec(html)) !== null && samples.length < 8) {
  let href = m[1];
  if (href.startsWith('/')) href = href.slice(1);
  samples.push({ href, title: m[2] });
}
console.log(JSON.stringify(samples, null, 2));

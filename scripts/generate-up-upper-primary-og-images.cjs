const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT, rowsFor } = require('./lib/up-upper-primary-seo.cjs');
const { siteFiles } = require('./seo-html.cjs');
const rows = rowsFor(siteFiles());

const escapeHtml = value => String(value).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
function card(row) {
  const topic = escapeHtml(row.topic);
  const section = escapeHtml(row.context.toUpperCase());
  const size = topic.length > 60 ? 42 : topic.length > 40 ? 50 : topic.length > 26 ? 58 : 68;
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{box-sizing:border-box}html,body{margin:0;width:1200px;height:630px;overflow:hidden}body{font-family:Arial,Helvetica,sans-serif;background:#f5f6f0;color:#18332c}
    main{position:relative;width:1200px;height:630px;padding:54px 82px 52px 100px;overflow:hidden;background:#f5f6f0}
    .rail{position:absolute;left:0;top:0;bottom:0;width:18px;background:#087f5b}.ring{position:absolute;width:370px;height:370px;border:2px solid rgba(8,127,91,.12);border-radius:50%;right:-105px;top:160px}.ring:before,.ring:after{content:"";position:absolute;border:2px solid rgba(8,127,91,.11);border-radius:50%}.ring:before{inset:34px}.ring:after{inset:76px}
    .brand{display:flex;align-items:center;gap:15px;color:#087f5b;font-size:25px;font-weight:800}.mark{width:42px;height:42px;border-radius:12px;background:#087f5b;color:white;display:grid;place-items:center;font-size:21px}
    .eyebrow{margin-top:62px;color:#a15c13;font-size:18px;font-weight:800;letter-spacing:2px}.title{position:relative;z-index:1;margin:20px 0 0;max-width:930px;min-height:170px;font-size:${size}px;line-height:1.08;letter-spacing:-1.4px;font-weight:800;color:#18332c;display:flex;align-items:center}
    .rule{width:94px;height:6px;border-radius:3px;background:#d99736;margin-top:18px}.foot{position:absolute;left:100px;bottom:53px;font-size:20px;color:#50645b;font-weight:600}.url{position:absolute;right:78px;bottom:53px;font-size:18px;color:#087f5b;font-weight:700}
    </style></head><body><main><div class="rail"></div><div class="ring"></div><div class="brand"><span class="mark">S</span><span>SJMaths</span></div><div class="eyebrow">UP UPPER PRIMARY TEACHER &nbsp;·&nbsp; ${section}</div><h1 class="title">${topic}</h1><div class="rule"></div><div class="foot">Clear topic notes &nbsp;·&nbsp; Exam practice</div><div class="url">sjmaths.com</div></main></body></html>`;
}

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    const page = await browser.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
    for (const row of rows) {
      const output = path.join(ROOT, row.image.slice(1));
      fs.mkdirSync(path.dirname(output), { recursive: true });
      await page.setContent(card(row), { waitUntil: 'load' });
      await page.screenshot({ path: output, type: 'png' });
    }
    console.log(`Generated ${rows.length} unique UP Upper Primary social preview images (1200×630).`);
  } finally {
    await browser.close();
  }
})().catch(error => { console.error(error); process.exitCode = 1; });

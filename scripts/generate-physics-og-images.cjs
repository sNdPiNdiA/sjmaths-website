const fs=require('node:fs');
const path=require('node:path');
const {chromium}=require('playwright');
const {ROOT}=require('./seo-html.cjs');
const {rows,imagePath}=require('./lib/class11-12-physics-seo.cjs');

const htmlEscape=value=>String(value).replace(/[&<>"']/g,char=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
function card(row){
  const className=row.file.startsWith('class-11-')?'CLASS 11 PHYSICS':'CLASS 12 PHYSICS';
  const chapter=row.file.match(/chapter-(\d+)-/);
  const label=chapter?`CHAPTER ${chapter[1]}`:'COMPLETE CHAPTER GUIDE';
  const topic=htmlEscape(row.topic);
  const size=row.topic.length>34?52:row.topic.length>24?58:68;
  return `<!doctype html><html><head><meta charset="utf-8"><style>
    *{box-sizing:border-box}html,body{margin:0;width:1200px;height:630px;overflow:hidden}body{font-family:Arial,Helvetica,sans-serif;background:#f5f6f0;color:#18332c}
    .card{position:relative;width:1200px;height:630px;padding:54px 82px 52px 100px;overflow:hidden;background:#f5f6f0}
    .rail{position:absolute;left:0;top:0;bottom:0;width:18px;background:#087f5b}.ring{position:absolute;width:370px;height:370px;border:2px solid rgba(8,127,91,.12);border-radius:50%;right:-105px;top:160px}.ring:before,.ring:after{content:"";position:absolute;border:2px solid rgba(8,127,91,.11);border-radius:50%}.ring:before{inset:34px}.ring:after{inset:76px}
    .top{display:flex;align-items:center;gap:15px;color:#087f5b;font-size:25px;font-weight:800;letter-spacing:.2px}.mark{width:42px;height:42px;border-radius:12px;background:#087f5b;color:white;display:grid;place-items:center;font-size:21px;font-weight:800}
    .eyebrow{margin-top:68px;color:#a15c13;font-size:19px;font-weight:800;letter-spacing:2.6px}.title{position:relative;z-index:1;margin:18px 0 0;max-width:930px;min-height:165px;font-size:${size}px;line-height:1.08;letter-spacing:-1.5px;font-weight:800;color:#18332c;display:flex;align-items:center}
    .rule{width:94px;height:6px;border-radius:3px;background:#d99736;margin-top:20px}.foot{position:absolute;left:100px;bottom:53px;font-size:20px;color:#50645b;font-weight:600}.url{position:absolute;right:78px;bottom:53px;font-size:18px;color:#087f5b;font-weight:700}
    </style></head><body><main class="card"><div class="rail"></div><div class="ring"></div><div class="top"><span class="mark">S</span><span>SJMaths</span></div><div class="eyebrow">${className} &nbsp;·&nbsp; ${label}</div><h1 class="title">${topic}</h1><div class="rule"></div><div class="foot">NCERT concepts &nbsp;·&nbsp; Worked examples &nbsp;·&nbsp; Exercises</div><div class="url">sjmaths.com</div></main></body></html>`;
}

(async()=>{
  const browser=await chromium.launch({headless:true});
  try{
    const page=await browser.newPage({viewport:{width:1200,height:630},deviceScaleFactor:1});
    for(const row of rows){
      const output=path.join(ROOT,imagePath(row).slice(1));fs.mkdirSync(path.dirname(output),{recursive:true});
      await page.setContent(card(row),{waitUntil:'load'});await page.screenshot({path:output,type:'png'});
    }
    console.log(`Generated ${rows.length} page-specific Physics social preview images (1200×630).`);
  }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exitCode=1});

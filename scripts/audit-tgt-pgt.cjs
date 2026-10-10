const fs = require('node:fs');
const path = require('node:path');
const { chromium } = require('playwright');
const { ROOT, parse, siteFiles } = require('./seo-html.cjs');
const { createResolver } = require('./seo-routes.cjs');
const { routeRepositoryFixtures } = require('./lib/browser-fixture.cjs');
const { inspectInlineScripts } = require('./lib/inline-script-integrity.cjs');
(async () => {
  const files = siteFiles();
  const inventory = { files: files.filter(file => /^up-(?:tgt|pgt)-[^/]+\/.*\.html$/.test(file)) };
  const resolve = createResolver(files), missing = [], fragments = [], jsonErrors = [], scriptErrors = [], duplicateIds = [];
  const cache = new Map();
  const read = file => { if (!cache.has(file)) cache.set(file, parse(fs.readFileSync(path.join(ROOT,file),'utf8'))); return cache.get(file); };
  for (const file of inventory.files) {
    const $ = read(file);
    for (const script of inspectInlineScripts(fs.readFileSync(path.join(ROOT,file),'utf8'))) {
      if (script.syntaxError) scriptErrors.push({file,offset:script.offset,error:script.syntaxError});
    }
    const ids = new Set();
    $('[id]').each((_,el)=> { const id=$(el).attr('id');if(ids.has(id))duplicateIds.push({file,id});ids.add(id); });
    $('a[href],script[src],link[href],img[src]').each((_,el) => {
      const value = $(el).attr('href') || $(el).attr('src');
      if (!value || /^(mailto:|tel:|javascript:|data:)/.test(value)) return;
      const url = new URL(value,'https://sjmaths.com/'+file), result = resolve(url.href);
      if (result.external) return;
      if (!result.file) missing.push({file,value});
      else if (url.hash && result.file.endsWith('.html')) {
        const id = decodeURIComponent(url.hash.slice(1)), target = read(result.file);
        if (!target('[id]').toArray().some(e=>target(e).attr('id')===id)) fragments.push({file,value});
      }
    });
    $('script[type="application/json"],script[type="application/ld+json"]').each((_,e)=> { try {JSON.parse($(e).text());} catch(error){jsonErrors.push({file,id:$(e).attr('id'),error:error.message});} });
  }
  const width = Number(process.argv.find(arg=>arg.startsWith('--width='))?.split('=')[1] || 390);
  const report = { pages:inventory.files.length,width,missing,fragments,jsonErrors,scriptErrors,duplicateIds,browser:[] };
  fs.mkdirSync(path.join(ROOT,'scratch'),{recursive:true});
  const reportFile=path.join(ROOT,'scratch',`tgt-pgt-audit-${width}.json`);
  fs.writeFileSync(reportFile,JSON.stringify(report,null,2));
  console.log('Static:',JSON.stringify({pages:report.pages,missing:missing.length,fragments:fragments.length,jsonErrors,scriptErrors,duplicateIds}));
  if(missing.length||fragments.length||jsonErrors.length||scriptErrors.length||duplicateIds.length)process.exitCode=1;
  if(process.argv.includes('--static-only'))return;
  const browser = await chromium.launch({headless:true}); let next=0,completed=0;
  try { await Promise.all(Array.from({length:4},async()=> {
    const context = await browser.newContext({viewport:{width,height:844},reducedMotion:'reduce'});
    const page = await context.newPage();
    const evidence = await routeRepositoryFixtures(page,{root:ROOT,files});
    // Fonts and remote maths libraries remain real; no authenticated state is fabricated.
    while(next<inventory.files.length){
      const file=inventory.files[next++]; evidence.errors.length=0;evidence.missing.length=0;
      let error;
      try {
        await page.goto('https://sjmaths.com/'+file.replace(/index\.html$/,''),{waitUntil:'load',timeout:30000});
        await page.evaluate(()=> {
          document.querySelectorAll('.tab-btn[data-tab]').forEach(b=>b.click());
          document.querySelectorAll('.section-head').forEach(b=>{b.click();b.click();});
          const search=document.getElementById('search')||document.getElementById('dirSearchInput');
          if(search){search.value='zzzz-no-match';search.dispatchEvent(new Event('input'));search.value='';search.dispatchEvent(new Event('input'));}
          const submit=document.getElementById('btn-submit-test');if(submit)submit.click();
        });
      } catch(e) {error=e.message;}
      const state=await page.evaluate(()=>({overflow:Math.max(0,document.documentElement.scrollWidth-innerWidth),heading:!!document.querySelector('h1')})).catch(()=>({}));
      report.browser.push({file,...state,errors:[...evidence.errors],missing:[...evidence.missing],...(error?{error}:{})});
      if(++completed%100===0)console.log('Browser pages:',completed);
    }
    await context.close();
  })); } finally {await browser.close(); fs.writeFileSync(reportFile,JSON.stringify(report,null,2));}
  const findings=report.browser.filter(x=>x.errors.length||x.missing.length||x.error||x.overflow>2);
  if(findings.length)process.exitCode=1;
  console.log('Browser findings:',JSON.stringify(findings));
})().catch(error=>{console.error(error);process.exitCode=1;});

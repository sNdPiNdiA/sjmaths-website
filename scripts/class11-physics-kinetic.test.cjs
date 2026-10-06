const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const cheerio=require('cheerio');
const {chromium}=require('playwright');
const {fixtureFiles,routeRepositoryFixtures}=require('./lib/browser-fixture.cjs');
const root=path.resolve(__dirname,'..');
const route='/class-11-physics/chapter-12-kinetic-theory/';
const file=path.join(root,route,'index.html');
const html=fs.readFileSync(file,'utf8');
const $=cheerio.load(html);

test('Chapter 12 has all textbook concepts, derivations, examples and point-wise recap',()=>{
  assert.equal($('h1').length,1);assert.equal($('.tab').length,5);
  assert.equal($('#learn .ncert-section[id^="sec-12-"]').length,8);
  for(const phrase of ['Avogadro','Boyle','Charles','Dalton','P=(1/3)','PV=(2/3)','(3/2)kBT','equipartition','Mayer','Dulong–Petit','quantum','mean free path','gravitational potential','⟨v²⟩'])assert.ok($('#learn').text().includes(phrase),`missing concept ${phrase}`);
  assert.equal($('#learn .solved-example').length,9);
  for(let n=1;n<=9;n++)assert.equal($(`#learn .example-badge`).filter((_,e)=>$(e).text().includes(`12.${n}`)).length,1,`missing worked example ${n}`);
  assert.equal($('#sec-12-ponder li').length,5);
  assert.equal($('#learn svg').length,5);
});

test('All ten original NCERT exercises retain solutions, closed by default and linked to notes',()=>{
  assert.equal($('#exercise [data-exercise]').length,10);
  for(let n=1;n<=10;n++){
    const card=$(`[data-exercise="12.${n}"]`);assert.equal(card.length,1,`missing Exercise 12.${n}`);
    assert.ok(card.find('.ex-question').text().length>70,`incomplete Exercise 12.${n}`);
    assert.ok(card.find('.step-item').length>=2,`missing solution steps for 12.${n}`);
    assert.equal(card.find('.sol-toggle-btn').attr('aria-expanded'),'false');
    const target=card.find('.sol-toggle-btn').attr('aria-controls');assert.equal(card.find(`#${target}`).length,1);
    assert.equal($(card.find('.ex-prereq a').attr('href')).length,1);
  }
  assert.match($('[data-exercise="12.3"]').text(),/\(a\).+\(b\).+\(c\).+\(d\)/s);
});

test('Quiz, tests, SVGs, Three.js fallback behavior, page metadata and internal references are complete',()=>{
  assert.equal($('#quiz .mcq-card').length,27);
  $('#quiz .mcq-card').each((_,c)=>{assert.equal($(c).find('.mcq-option-btn').length,4);assert.equal($(c).find('[data-correct="true"]').length,1);});
  assert.equal($('#tests .test-card').length,27);assert.equal($('#revision .rev-card').length,7);
  assert.ok($('#kinetic-model').length);assert.match(html,/prefers-reduced-motion/);assert.match(html,/dispose\(\)/);assert.match(html,/DOMContentLoaded/);
  assert.equal($('link[rel="canonical"]').attr('href'),'https://sjmaths.com'+route);
  const ids=new Set();$('[id]').each((_,e)=>{const id=$(e).attr('id');assert.ok(!ids.has(id),`duplicate id ${id}`);ids.add(id);});
  $('[href^="#"]').each((_,e)=>assert.ok(ids.has($(e).attr('href').slice(1)),`broken anchor ${$(e).attr('href')}`));
  const hub=cheerio.load(fs.readFileSync(path.join(root,'class-11-physics/index.html'),'utf8'));
  assert.equal(hub('[data-keywords^="Kinetic Theory"] .tag-active').length,1);assert.equal(hub('a[href="chapter-12-kinetic-theory/"]').length,1);
  const index=JSON.parse(fs.readFileSync(path.join(root,'assets/js/search-index.json'),'utf8'));assert.equal(index.filter(x=>x.url===route).length,1);
  assert.equal(fs.readFileSync(path.join(root,'sitemap-class-11.xml'),'utf8').split('https://sjmaths.com'+route).length-1,1);
});

test('Key exercise calculations are consistent',()=>{
  const close=(a,b,t=.015)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*t,`${a} differs from ${b}`);
  close(Math.PI/6*(3e-10)**3*6.02e23/.0224,3.8e-4,.02);
  close(.03*(16*1.013e5/300-12*1.013e5/290)/8.31*.032,.1399,.003);
  close((1.013e5+1000*9.8*40)/1.013e5*308/285,5.26,.003);
  close(1/(Math.SQRT2*Math.PI*(2.026e5/(1.38e-23*290))*(2e-10)**2),1.1e-7,.02);
});

test('Chapter 12 tabs, closed solutions, quiz grading and responsive layout work', {timeout:90000},async()=>{
  const browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader']});
  const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'no-preference'});
  try{
    const page=await context.newPage();const evidence=await routeRepositoryFixtures(page,{root,files:fixtureFiles(root)});
    await page.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));
    await page.goto('https://sjmaths.com'+route,{waitUntil:'domcontentloaded',timeout:30000});
    await page.waitForSelector('#kinetic-model canvas',{timeout:20000});const modelToggle=page.locator('[data-model-toggle]');assert.equal(await modelToggle.getAttribute('aria-pressed'),'true');await modelToggle.click();assert.equal(await modelToggle.getAttribute('aria-pressed'),'false');await page.locator('#speedScale').fill('15');assert.equal(await page.locator('#speedReadout').textContent(),'1.5×');await modelToggle.click();
    await page.locator('.nav-btn[data-tab="exercise"]').click();const solution=page.locator('[data-exercise="12.1"] .sol-toggle-btn');assert.equal(await solution.getAttribute('aria-expanded'),'false');await solution.click();assert.equal(await solution.getAttribute('aria-expanded'),'true');
    await page.locator('.nav-btn[data-tab="quiz"]').click();await page.locator('#quiz .mcq-card').first().locator('[data-correct="true"]').click();assert.match(await page.locator('#quizProgressCount').textContent(),/1 \/ 27 Answered/);
    await page.locator('.nav-btn[data-tab="tests"]').click();const panel=page.locator('#testLevel0');for(const card of await panel.locator('.test-card').all()){const ans=await card.getAttribute('data-ans');await card.locator(`[data-idx="${ans}"]`).click();}await page.getByRole('button',{name:'Submit test'}).click();assert.match(await page.locator('#testResultBox').textContent(),/9 \/ 9/);
    for(const width of [390,768,1280]){await page.setViewportSize({width,height:844});await page.waitForTimeout(100);assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`horizontal overflow at ${width}`);}
    assert.deepEqual(evidence.errors,[]);assert.deepEqual(evidence.missing,[]);
  }finally{await context.close();await browser.close();}
});

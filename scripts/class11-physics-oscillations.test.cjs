const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const cheerio=require('cheerio');
const {chromium}=require('playwright');
const {fixtureFiles,routeRepositoryFixtures}=require('./lib/browser-fixture.cjs');
const root=path.resolve(__dirname,'..');
const route='/class-11-physics/chapter-13-oscillations/';
const html=fs.readFileSync(path.join(root,route,'index.html'),'utf8');
const $=cheerio.load(html);

test('Chapter 13 covers every section, proof, numbered example and point to ponder',()=>{
  assert.equal($('h1').length,1);assert.equal($('.tab').length,5);
  assert.equal($('#learn .ncert-section[id^="sec-13-"]').length,8);
  const learnText=$('#learn').text();
  for(const phrase of ['periodic motion','oscillatory motion','frequency','phase constant','Fourier','projection','π/2','v=dx/dt','ω²x','F=−kx','T=2π√(m/k)','conservation','½kA²','sinθ≈θ','simple pendulum'])assert.ok(learnText.includes(phrase),`missing concept or derivation: ${phrase}`);
  assert.match(learnText,/damping/i);assert.match(learnText,/forc(ing|ed)/i);
  assert.equal($('#learn .solved-example').length,8);
  for(let n=1;n<=8;n++)assert.equal($('#learn .example-badge').filter((_,e)=>$(e).text().includes(`13.${n}`)).length,1,`missing worked example 13.${n}`);
  assert.equal($('#sec-13-ponder li').length,9);assert.equal($('#learn .diagram-wrap svg').length,4);
});

test('All eighteen textbook exercises are retained, linked and collapsed by default',()=>{
  assert.equal($('#exercise [data-exercise]').length,18);
  for(let n=1;n<=18;n++){
    const card=$(`[data-exercise="13.${n}"]`);assert.equal(card.length,1,`missing Exercise 13.${n}`);
    assert.ok(card.find('.ex-question').text().length>60,`incomplete Exercise 13.${n}`);
    assert.ok(card.find('.step-item').length>=2,`missing solution steps for 13.${n}`);
    assert.equal(card.find('.sol-toggle-btn').attr('aria-expanded'),'false');
    const target=card.find('.sol-toggle-btn').attr('aria-controls');assert.equal(card.find(`#${target}`).length,1);
    assert.equal($(card.find('.ex-prereq a').attr('href')).length,1);
  }
  assert.match($('[data-exercise="13.4"]').text(),/sin³ωt/);
  assert.match($('[data-exercise="13.13"]').text(),/F\/k/);
  assert.match($('[data-exercise="13.17"]').text(),/ρlAg/);
});

test('Quiz, tests, revision, SVG/Three model and crawlable metadata are complete',()=>{
  assert.equal($('#quiz .mcq-card').length,30);assert.equal($('#tests .test-card').length,30);assert.equal($('#revision .rev-card').length,7);
  $('#quiz .mcq-card').each((_,c)=>{assert.equal($(c).find('.mcq-option-btn').length,4);assert.equal($(c).find('[data-correct="true"]').length,1);});
  for(const id of ['sec-13-1','sec-13-2','sec-13-3','sec-13-4','sec-13-5','sec-13-6','sec-13-7'])assert.ok($(`#quiz .mcq-card[data-concept="${id}"]`).length>=3,`quiz misses ${id}`);
  assert.match(html,/WebGLRenderer/);assert.match(html,/prefers-reduced-motion/);assert.match(html,/dispose\(\)/);assert.match(html,/Static spring model/);
  assert.equal($('link[rel="canonical"]').attr('href'),'https://sjmaths.com'+route);
  const ids=new Set();$('[id]').each((_,e)=>{const id=$(e).attr('id');assert.ok(!ids.has(id),`duplicate id ${id}`);ids.add(id);});
  $('[href^="#"]').each((_,e)=>assert.ok(ids.has($(e).attr('href').slice(1)),`broken anchor ${$(e).attr('href')}`));
  const hub=cheerio.load(fs.readFileSync(path.join(root,'class-11-physics/index.html'),'utf8'));
  assert.equal(hub('[data-keywords^="Oscillations"] .tag-active').length,1);assert.equal(hub('a[href="chapter-13-oscillations/"]').length,1);
  const index=JSON.parse(fs.readFileSync(path.join(root,'assets/js/search-index.json'),'utf8'));assert.equal(index.filter(x=>x.url===route).length,1);
  assert.equal(fs.readFileSync(path.join(root,'sitemap-class-11.xml'),'utf8').split('https://sjmaths.com'+route).length-1,1);
});

test('Representative exercise calculations are consistent',()=>{
  const close=(a,b,t=.02)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*t,`${a} differs from ${b}`);
  close(Math.sqrt(1200/3)/(2*Math.PI),3.183,.002);close(400*.02,8,.002);close(Math.sqrt(400)*.02,.4,.002);
  close(50*9.8/.2*.6*.6/(4*Math.PI*Math.PI),22.36,.002);
  close(2*Math.PI*Math.sqrt(1/Math.sqrt(9.8**2+(15**4/100**2))),1.9815,.001);
});

test('Tabs, closed solutions, quiz grading, oscillator controls and mobile widths work', {timeout:90000},async()=>{
  const browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader']});
  const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'no-preference'});
  try{
    const page=await context.newPage();const evidence=await routeRepositoryFixtures(page,{root,files:fixtureFiles(root)});
    await page.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));
    await page.goto('https://sjmaths.com'+route,{waitUntil:'domcontentloaded',timeout:30000});
    await page.locator('.nav-btn[data-tab="exercise"]').click();const solution=page.locator('[data-exercise="13.1"] .sol-toggle-btn');assert.equal(await solution.getAttribute('aria-expanded'),'false');await solution.click();assert.equal(await solution.getAttribute('aria-expanded'),'true');
    await page.locator('.nav-btn[data-tab="quiz"]').click();await page.locator('#quiz .mcq-card').first().locator('[data-correct="true"]').click();assert.match(await page.locator('#quizProgressCount').textContent(),/1 \/ 30 Answered/);
    await page.locator('.nav-btn[data-tab="tests"]').click();const panel=page.locator('#testLevel0');for(const card of await panel.locator('.test-card').all()){const ans=await card.getAttribute('data-ans');await card.locator(`[data-idx="${ans}"]`).click();}await page.getByRole('button',{name:'Submit test'}).click();assert.match(await page.locator('#testResultBox').textContent(),/10 \/ 10/);
    await page.locator('.nav-btn[data-tab="learn"]').click();await page.locator('#shm-model').scrollIntoViewIfNeeded();
    const canvas=page.locator('[data-shm-model] canvas');await canvas.waitFor({state:'visible',timeout:25000});
    const toggle=page.locator('[data-shm-toggle]');assert.equal(await toggle.getAttribute('aria-pressed'),'true');await toggle.click();assert.equal(await toggle.getAttribute('aria-pressed'),'false');
    await page.locator('#shmAmplitude').fill('15');assert.equal(await page.locator('#shmAmplitudeReadout').textContent(),'1.5×');
    await page.locator('#shmFrequency').fill('15');assert.equal(await page.locator('#shmFrequencyReadout').textContent(),'1.5×');
    for(const width of [390,768,1280]){await page.setViewportSize({width,height:844});await page.waitForTimeout(80);assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`horizontal overflow at ${width}`);}
    assert.deepEqual(evidence.errors,[]);assert.deepEqual(evidence.missing,[]);
  }finally{await context.close();await browser.close();}
});

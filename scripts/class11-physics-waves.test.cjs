const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const cheerio=require('cheerio');
const {chromium}=require('playwright');
const {fixtureFiles,routeRepositoryFixtures}=require('./lib/browser-fixture.cjs');
const root=path.resolve(__dirname,'..'),route='/class-11-physics/chapter-14-waves/';
const html=fs.readFileSync(path.join(root,route,'index.html'),'utf8'),$=cheerio.load(html);

test('Chapter 14 contains its full concept map, textbook examples and visual explanations',()=>{
  assert.equal($('h1').length,1);assert.equal($('.tab').length,5);assert.equal($('#learn .ncert-section[id^="sec-14-"]').length,7);
  const learn=$('#learn').text();
  for(const s of ['mechanical waves','electromagnetic waves','transverse','longitudinal','capillary','gravity waves','y(x,t)=a sin','k=2π/λ','v=ω/k','Newton','Laplace','superposition','constructive interference','destructive interference','rigid end','standing wave','normal modes','odd harmonics','beats'])assert.ok(learn.toLowerCase().includes(s.toLowerCase()),`missing concept: ${s}`);
  assert.equal($('#learn .solved-example').length,6);assert.equal($('#learn .diagram-wrap svg').length,3);assert.match(html,/WebGLRenderer/);assert.match(html,/prefers-reduced-motion/);assert.match(html,/dispose\(\)/);
});

test('All 19 source exercises have worked solutions and begin collapsed',()=>{
  assert.equal($('#exercise .exercise-card').length,19);
  for(let n=1;n<=19;n++){
    const card=$(`#exercise .exercise-card`).eq(n-1);assert.ok(card.text().includes(`14.${n}`),`missing 14.${n}`);
    assert.ok(card.find('.ex-question').text().length>40,`question text incomplete 14.${n}`);assert.ok(card.find('.step-item').length>=2,`solution incomplete 14.${n}`);
    const b=card.find('.sol-toggle-btn');assert.equal(b.attr('aria-expanded'),'false');assert.equal(card.find(`#${b.attr('aria-controls')}`).length,1);
    assert.equal($(card.find('.ex-prereq a').attr('href')).length,1,`concept link missing 14.${n}`);
  }
  assert.match($('#exercise').text(),/2\\sqrt\(x−vt\)|2√\(x−vt\)/);assert.match($('#exercise').text(),/Exercise 15\.11/);
});

test('Quiz spans every chapter concept; revision, tests, metadata and hub links are present',()=>{
  assert.equal($('#quiz .mcq-card').length,35);assert.equal($('#tests .test-card').length,35);assert.equal($('#revision .rev-card').length,7);
  $('#quiz .mcq-card').each((_,c)=>{assert.equal($(c).find('.mcq-option-btn').length,4);assert.equal($(c).find('[data-correct="true"]').length,1)});
  for(let i=1;i<=7;i++)assert.ok($(`#quiz .mcq-card[data-concept="14-${i}"]`).length>=3,`quiz misses section 14.${i}`);
  assert.equal($('link[rel="canonical"]').attr('href'),'https://sjmaths.com'+route);
  const ids=new Set();$('[id]').each((_,el)=>{let id=$(el).attr('id');assert.ok(!ids.has(id),`duplicate id ${id}`);ids.add(id)});
  $('[href^="#"]').each((_,el)=>assert.ok(ids.has($(el).attr('href').slice(1)),`broken anchor ${$(el).attr('href')}`));
  const hub=cheerio.load(fs.readFileSync(path.join(root,'class-11-physics/index.html'),'utf8'));
  assert.equal(hub('a[href="chapter-14-waves/"]').length,1);assert.equal(hub('[data-keywords^="Waves"] .tag-active').length,1);
  const index=JSON.parse(fs.readFileSync(path.join(root,'assets/js/search-index.json'),'utf8'));assert.equal(index.filter(x=>x.url===route).length,1);
  assert.equal(fs.readFileSync(path.join(root,'sitemap-class-11.xml'),'utf8').split('https://sjmaths.com'+route).length-1,1);
});

test('Numerical answers and condition-based classifications are consistent',()=>{
  const near=(a,b,t=.015)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*t,`${a} differs from ${b}`);
  near(Math.sqrt(200/(2.5/20)),40);near(Math.sqrt(2*300/9.8)+300/340,8.70);near((2.1/12)*343**2,20583);
  near(1700/(4.2e6),.00040476);near((.030/1.5)*180**2,648);near(340*(.793-.255)*2,365.84);
  near(427-5,422);near(324-6,318);near(2530*2,5060);
});

test('Reader interactions, reduced-motion fallback and narrow viewports work', {timeout:90000},async()=>{
  const browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader']});
  try{
    const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'no-preference'}),page=await context.newPage();
    const evidence=await routeRepositoryFixtures(page,{root,files:fixtureFiles(root)});
    await page.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));
    await page.goto('https://sjmaths.com'+route,{waitUntil:'domcontentloaded',timeout:30000});
    await page.locator('.nav-btn[data-tab="exercise"]').click();const sol=page.locator('.exercise-card').first().locator('.sol-toggle-btn');assert.equal(await sol.getAttribute('aria-expanded'),'false');await sol.click();assert.equal(await sol.getAttribute('aria-expanded'),'true');
    await page.locator('.nav-btn[data-tab="quiz"]').click();await page.locator('#quiz .mcq-card').first().locator('[data-correct="true"]').click();assert.match(await page.locator('#quizProgressCount').textContent(),/1 \/ 35 Answered/);
    await page.locator('.nav-btn[data-tab="tests"]').click();const first=page.locator('#testLevel0 .test-card').first();await first.locator(`[data-idx="${await first.getAttribute('data-ans')}"]`).click();await page.getByRole('button',{name:'Submit test'}).click();assert.match(await page.locator('#testResultBox').textContent(),/Score: 1 \/ 12/);await page.getByRole('button',{name:'Reset'}).click();assert.equal(await first.locator('button').first().isEnabled(),true);
    await page.locator('.nav-btn[data-tab="learn"]').click();await page.locator('#wave-model').scrollIntoViewIfNeeded();await page.locator('[data-wave-model] canvas').waitFor({state:'visible',timeout:25000});
    const toggle=page.locator('[data-wave-toggle]');await toggle.click();assert.equal(await toggle.getAttribute('aria-pressed'),'false');
    for(const width of [390,768,1280]){await page.setViewportSize({width,height:844});await page.waitForTimeout(100);assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`overflow at ${width}`)}
    assert.deepEqual(evidence.errors,[]);assert.deepEqual(evidence.missing,[]);
    await context.close();
    const reduced=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'}),reducedPage=await reduced.newPage();await routeRepositoryFixtures(reducedPage,{root,files:fixtureFiles(root)});await reducedPage.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));await reducedPage.goto('https://sjmaths.com'+route,{waitUntil:'domcontentloaded'});await reducedPage.locator('#wave-model').scrollIntoViewIfNeeded();assert.equal(await reducedPage.locator('[data-wave-model]').evaluate(el=>el.classList.contains('wave-static')),true);await reduced.close();
  }finally{await browser.close()}
});

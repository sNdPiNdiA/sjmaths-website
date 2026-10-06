const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const cheerio=require('cheerio');
const {chromium}=require('playwright');
const {fixtureFiles,routeRepositoryFixtures}=require('./lib/browser-fixture.cjs');
const root=path.resolve(__dirname,'..');
const route='/class-11-physics/chapter-11-thermodynamics/';
const file=path.join(root,route,'index.html');
const html=fs.readFileSync(file,'utf8');
const $=cheerio.load(html);

test('Chapter structure covers all 11 source sections, laws, proofs and distinctions',()=>{
  assert.equal($('h1').length,1);assert.equal($('.tab').length,5);
  assert.equal($('#learn .ncert-section[id^="sec-11-"]').length,10);
  for(const phrase of ['Concept-complete','All 11 NCERT sections are covered','Models initialise near view','complete exercise solutions and practice'])assert.equal($('#learn').text().includes(phrase),false,`editorial copy remains: ${phrase}`);
  for(const phrase of ['caloric','Rumford','Zeroth Law','Q=ΔU+W','Cₚ−Cᵥ=R','3R','extensive','intensive','quasi-static','PVᵞ','Kelvin–Planck','Clausius','irreversible','Carnot','1−T₂/T₁'])assert.ok($('#learn').text().includes(phrase),`missing ${phrase}`);
  assert.match($('#sec-11-5').text(),/Mayer.s relation/i);
  assert.match($('#sec-11-10').text(),/Carnot.s theorem/i);
});

test('All eight original numbered exercise questions and solutions are retained',()=>{
  assert.equal($('#exercise [data-exercise]').length,8);
  for(let n=1;n<=8;n++){
    const card=$(`[data-exercise="11.${n}"]`);assert.equal(card.length,1,`missing Exercise 11.${n}`);
    assert.ok(card.find('.ex-question').text().length>60,`incomplete Exercise 11.${n}`);
    assert.ok(card.find('.step-item').length>=2,`missing solution steps for 11.${n}`);
    assert.equal(card.find('.sol-toggle-btn').attr('aria-expanded'),'false');
    assert.ok($('#'+card.find('.sol-toggle-btn').attr('aria-controls')).length);
    assert.ok($(card.find('.ex-prereq a').attr('href')).length);
  }
  assert.match($('[data-exercise="11.3"]').text(),/\(a\).+\(b\).+\(c\).+\(d\)/s);
  assert.match($('[data-exercise="11.8"]').text(),/figure is needed/i);
});

test('Quiz, revision, tests, SVG diagrams, Three.js assets and discovery entries are valid',()=>{
  assert.equal($('#quiz .mcq-card').length,30);assert.equal($('#quiz .quiz-topic-group').length,10);
  $('#quiz .quiz-topic-group').each((_,g)=>assert.ok($(g).find('.mcq-card').length>=2));
  $('#quiz .mcq-card').each((_,c)=>{assert.equal($(c).find('.mcq-option-btn').length,4);assert.equal($(c).find('[data-correct="true"]').length,1);});
  assert.equal($('#revision .rev-card').length,10);$('#revision .rev-card').each((_,c)=>assert.equal($(c).find('li').length,3));
  assert.equal($('#tests .test-card').length,15);assert.equal($('#thermo-lab [data-thermo]').length,3);assert.equal($('#thermo-lab [data-thermo-play]').length,3);assert.ok($('#learn svg').length>=6);
  const ids=new Set();$('[id]').each((_,e)=>{const id=$(e).attr('id');assert.ok(!ids.has(id),`duplicate id ${id}`);ids.add(id);});
  $('[href^="#"]').each((_,e)=>assert.ok(ids.has($(e).attr('href').slice(1)),`broken anchor ${$(e).attr('href')}`));
  for(const [selector,filePath,attr] of [['link[href*="class11-physics-thermal.min"]','assets/css/class11-physics-thermal.min.css','href'],['script[src*="class11-thermo-three.min"]','assets/js/class11-thermo-three.min.js','src']]){
    const expected=crypto.createHash('sha256').update(fs.readFileSync(path.join(root,filePath))).digest('hex').slice(0,8);assert.ok($(selector).attr(attr).endsWith(expected));
  }
  const hub=cheerio.load(fs.readFileSync(path.join(root,'class-11-physics/index.html'),'utf8'));
  assert.equal(hub('[data-keywords^="Thermodynamics"] .tag-active').length,1);assert.equal(hub('a[href="chapter-11-thermodynamics/"]').length,1);
  const index=JSON.parse(fs.readFileSync(path.join(root,'assets/js/search-index.json'),'utf8'));assert.equal(index.filter(x=>x.url===route).length,1);
  assert.equal(fs.readFileSync(path.join(root,'sitemap-class-11.xml'),'utf8').split('https://sjmaths.com'+route).length-1,1);
});

test('Exercise mathematics and Carnot efficiency recalculate',()=>{
  const close=(a,b,t=.015)=>assert.ok(Math.abs(a-b)<=Math.abs(b)*t,`${a} differs from ${b}`);
  close(.05*4186*50/40000,.261625,.001);
  close((.02/.028)*(7*8.3/2)*45,933.2,.002);
  close(2**1.4,2.639,.001);
  close(9.35*4.19-22.3,16.8765,.001);
  close(1-300/600,.5,.001);
});

test('Chapter 11 tab, quiz, exercise solution, test grading and responsive layout work', {timeout:90000},async()=>{
  const browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader']});
  const context=await browser.newContext({viewport:{width:390,height:844},reducedMotion:'reduce'});
  try{
    const page=await context.newPage();const evidence=await routeRepositoryFixtures(page,{root,files:fixtureFiles(root)});
    await page.route('**/assets/js/require-auth*.js*',r=>r.fulfill({contentType:'text/javascript',body:''}));
    await page.goto('https://sjmaths.com'+route,{waitUntil:'domcontentloaded',timeout:30000});
    await page.locator('.nav-btn[data-tab="exercise"]').click();const toggle=page.locator('[data-exercise="11.1"] .sol-toggle-btn');assert.equal(await toggle.getAttribute('aria-expanded'),'false');await toggle.click();assert.equal(await toggle.getAttribute('aria-expanded'),'true');
    await page.locator('.nav-btn[data-tab="quiz"]').click();await page.locator('#quiz .mcq-card').first().locator('[data-correct="true"]').click();assert.match(await page.locator('#quizProgressCount').textContent(),/1 \/ 30 Answered/);
    await page.locator('.nav-btn[data-tab="tests"]').click();const panel=page.locator('#testLevel0');for(const card of await panel.locator('.test-card').all()){const ans=await card.getAttribute('data-ans');await card.locator(`[data-idx="${ans}"]`).click();}await page.getByRole('button',{name:'Submit Test'}).click();assert.match(await page.locator('#testResultBox').textContent(),/5 \/ 5/);
    for(const width of [390,768,1280]){await page.setViewportSize({width,height:844});await page.waitForTimeout(120);assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),`horizontal overflow at ${width}`);}
    await page.locator('.nav-btn[data-tab="learn"]').click();await page.locator('#thermo-lab').scrollIntoViewIfNeeded();await page.waitForTimeout(700);assert.equal(await page.locator('#thermo-lab canvas').count(),3);
    const play=page.locator('[data-thermo-play]').first();assert.equal(await play.isDisabled(),true,'reduced-motion should disable animation');await page.emulateMedia({reducedMotion:'no-preference'});assert.equal(await play.isDisabled(),false);await play.click();assert.equal(await play.getAttribute('aria-pressed'),'true');await play.click();assert.equal(await play.getAttribute('aria-pressed'),'false');await page.emulateMedia({reducedMotion:'reduce'});await page.waitForFunction(()=>document.querySelector('[data-thermo-play]').disabled);
    await page.locator('[data-thermo="carnot"] input[type="range"]').first().evaluate(e=>{e.value='350';e.dispatchEvent(new Event('input',{bubbles:true}));});assert.match(await page.locator('[data-thermo="carnot"] output').first().textContent(),/350 K/);
    assert.deepEqual(evidence.errors,[]);assert.deepEqual(evidence.missing,[]);
  }finally{await context.close();await browser.close();}
});

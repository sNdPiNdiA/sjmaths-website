const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const cheerio = require('cheerio');
const root = path.resolve(__dirname, '..');
const route = '/class-11-physics/chapter-8-mechanical-properties-of-solids/';
const html = fs.readFileSync(path.join(root, route, 'index.html'), 'utf8');
const $ = cheerio.load(html);
test('Solids retains all chapter topics, five placed examples and sixteen exercise questions', () => {
  const ids = ['8-1','8-2','8-3','8-4','8-5-1','8-5-2','8-5-3','8-5-4','8-5-5','8-6-1','8-6-2','8-6-3'];
  assert.deepEqual($('[data-concept]').map((_,e)=>$(e).attr('data-concept')).get(), ids);
  assert.equal($('[data-example]').length, 5);
  for (let n=1;n<=5;n++) {
    const e = $(`[data-example="8.${n}"]`);
    assert.equal(e.closest('[data-concept]').attr('data-concept'), n<=3?'8-5-1':n===4?'8-5-2':'8-5-3');
    assert.ok(e.find('.example-question').text().length > 80);
    assert.ok(e.find('.step-item').length >= 3 || n===5);
  }
  assert.equal($('#exercise [data-exercise]').length, 16);
  for (let n=1;n<=16;n++) {
    const e=$(`[data-exercise="8.${n}"]`);
    assert.equal(e.length,1);
    assert.ok(e.find('.ex-question').text().length > 70);
    assert.ok(e.find('.step-item').length >= 2);
    assert.ok(e.find('.sol-toggle-btn').attr('aria-controls'));
  }
  assert.equal($('#learn [data-exercise]').length,0);
  assert.match($('[data-exercise="8.12"] .ex-question').text(), /100\.5 litre/);
  assert.match($('[data-exercise="8.12"] .ex-solution-content').text(), /99\.5 litre/);
  assert.match($('#example-8-4').text(), /printed working shows 9\.4/);
  for(const n of [2,3,5]) assert.equal($(`[data-exercise="8.${n}"] .ex-body > figure svg`).length,1);
  assert.equal($('#learn table').length,4);
  assert.equal($('#quiz .mcq-card').length,18);
  assert.equal($('#tests .test-card').length,15);
  assert.equal($('h1').length,1);
  assert.equal($('link[rel="canonical"]').attr('href'),'https://sjmaths.com'+route);
  assert.match($('#sec-8-5-5').text(), /\\int_0/);
  assert.match($('#sec-8-6-2').text(), /Curvature relation/);
  assert.match($('#sec-8-6-2').text(), /48YI/);
  assert.match($('#sec-8-6-3').text(), /10\\,\\mathrm\{km\}/);
});
test('Every quiz/test answer is well formed and discovery links are active', () => {
  $('#quiz .mcq-card').each((_,e)=>assert.equal($(e).find('[data-correct="true"]').length,1));
  $('#tests .test-card').each((_,e)=> {
    const ans=Number($(e).attr('data-ans'));
    assert.ok(ans>=0 && ans<4);
    assert.equal($(e).find(`[data-idx="${ans}"]`).length,1);
  });
  const hub=cheerio.load(fs.readFileSync(path.join(root,'class-11-physics/index.html'),'utf8'));
  const card=hub('[data-keywords^="Mechanical Properties of Solids"]');
  assert.equal(card.find('.tag-active').length,1);
  assert.equal(card.find(`a[href="${route.replace('/class-11-physics/','')}"]`).length,4);
  const search=JSON.parse(fs.readFileSync(path.join(root,'assets/js/search-index.json'),'utf8'));
  assert.equal(search.filter(e=>e.url===route).length,1);
  assert.equal(fs.readFileSync(path.join(root,'sitemap-class-11.xml'),'utf8').split('https://sjmaths.com'+route).length-1,1);
});
test('Representative solved examples and exercise results are independently recalculated', () => {
  const close=(a,b,relative=0.015)=>assert.ok(Math.abs(a-b)/Math.abs(b)<relative,`${a} vs ${b}`);
  close(1e5/(Math.PI*0.01**2),3.18e8);
  close(1e5/(Math.PI*0.01**2*2e11),1.59e-3);
  close(0.0007/((2.2/1.1e11+1.6/2e11)/(Math.PI*0.0015**2)),1.8e2,0.03);
  close(1078*0.5/(9.4e9*Math.PI*0.02**2),4.55e-5);
  close(9e4*0.5/(0.05*5.6e9),1.6e-4);
  close(3000*1000*10/2.2e9,0.0136);
  const area=Math.PI*0.0025**2/4;
  close(98*1.5/(area*2e11),1.50e-4);
  close(58.8/(area*9e10),1.33e-4);
  close(980*0.1/(0.01*25e9),3.92e-7);
  close((50000*9.8/4)/(Math.PI*(0.6**2-0.3**2)*2e11),7.22e-7);
  close(44500/(0.0152*0.0191*1.1e11),1.39e-3);
  close(14.5*(9.8+(4*Math.PI)**2)/(6.5e-6*2e11),1.87e-3);
  close(100*1.013e5/0.005,2.026e9);
  close(1030/(1-79*1.013e5/2.2e9),1.034e3,0.001);
  close(10*1.013e5/37e9,2.74e-5);
  close(0.1**3*7e6/140e9,5e-8);
  close(3e8/(3e3*10),1e4);
});

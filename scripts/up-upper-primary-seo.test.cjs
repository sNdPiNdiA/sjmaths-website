const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { ROOT, BASE, rowsFor } = require('./lib/up-upper-primary-seo.cjs');
const { siteFiles, parse } = require('./seo-html.cjs');

const rows = rowsFor(siteFiles());

test('UP Upper Primary pages have unique, concise SEO metadata and social cards', () => {
  assert.equal(rows.length, 418);
  assert.equal(new Set(rows.map(row => row.title)).size, rows.length, 'titles must be unique');
  assert.equal(new Set(rows.map(row => row.description)).size, rows.length, 'descriptions must be unique');
  assert.equal(new Set(rows.map(row => row.route)).size, rows.length, 'routes must be unique');
  assert.equal(new Set(rows.map(row => row.image)).size, rows.length, 'social image URLs must be unique');

  for (const row of rows) {
    assert.ok(row.title.length >= 15 && row.title.length <= 120, `${row.file}: title length ${row.title.length}`);
    assert.ok(row.description.length >= 40 && row.description.length <= 320, `${row.file}: description length ${row.description.length}`);
    assert.ok(fs.existsSync(path.join(ROOT, row.image.slice(1))), `${row.file}: missing social card`);
    const image = fs.readFileSync(path.join(ROOT, row.image.slice(1)));
    assert.equal(image.subarray(0, 8).toString('hex'), '89504e470d0a1a0a', `${row.file}: invalid PNG`);
    assert.equal(image.readUInt32BE(16), 1200, `${row.file}: incorrect social card width`);
    assert.equal(image.readUInt32BE(20), 630, `${row.file}: incorrect social card height`);

    const source = fs.readFileSync(path.join(ROOT, row.file), 'utf8');
    const $ = parse(source);
    assert.equal($('head > title').first().text(), row.title, `${row.file}: stale title`);
    assert.equal($('meta[name="description"]').attr('content'), row.description, `${row.file}: stale description`);
    assert.equal($('link[rel="canonical"]').attr('href'), `https://sjmaths.com${row.route}`, `${row.file}: canonical mismatch`);
    assert.equal($('meta[property="og:image"]').attr('content'), `https://sjmaths.com${row.image}`, `${row.file}: social image mismatch`);
    assert.equal($('meta[name="twitter:card"]').attr('content'), 'summary_large_image', `${row.file}: missing Twitter card`);
  }
  assert.ok(rows.every(row => row.file.startsWith(`${BASE}/`)));
});

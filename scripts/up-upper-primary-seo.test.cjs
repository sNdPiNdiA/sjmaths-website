const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { ROOT, BASE, rowsFor } = require('./lib/up-upper-primary-seo.cjs');
const { siteFiles, parse } = require('./seo-html.cjs');

const rows = rowsFor(siteFiles());

test('UP Upper Primary pages have unique, concise SEO metadata and social cards', () => {
  assert.equal(rows.length, 419);
  assert.equal(new Set(rows.map(row => row.route)).size, rows.length, 'routes must be unique');
  assert.equal(new Set(rows.map(row => row.image)).size, rows.length, 'social image URLs must be unique');

  const actualMetadata = rows.map(row => {
    const source = fs.readFileSync(path.join(ROOT, row.file), 'utf8');
    return { row, source, $: parse(source) };
  });
  const titles = actualMetadata.map(({ $, row }) => {
    const title = $('head > title').first().text();
    assert.ok(title.length >= 15 && title.length <= 120, `${row.file}: title length ${title.length}`);
    return title;
  });
  const descriptions = actualMetadata.map(({ $, row }) => {
    const description = $('meta[name="description"]').attr('content') || '';
    assert.ok(description.length >= 40 && description.length <= 320, `${row.file}: description length ${description.length}`);
    return description;
  });
  assert.equal(new Set(titles).size, rows.length, 'page titles must be unique');
  assert.equal(new Set(descriptions).size, rows.length, 'page descriptions must be unique');

  for (const { row, source, $ } of actualMetadata) {
    const title = $('head > title').first().text();
    const description = $('meta[name="description"]').attr('content');
    const canonical = `https://sjmaths.com${row.route}`;
    assert.ok(fs.existsSync(path.join(ROOT, row.image.slice(1))), `${row.file}: missing social card`);
    const image = fs.readFileSync(path.join(ROOT, row.image.slice(1)));
    assert.equal(image.subarray(0, 8).toString('hex'), '89504e470d0a1a0a', `${row.file}: invalid PNG`);
    assert.equal(image.readUInt32BE(16), 1200, `${row.file}: incorrect social card width`);
    assert.equal(image.readUInt32BE(20), 630, `${row.file}: incorrect social card height`);

    assert.equal($('link[rel="canonical"]').attr('href'), canonical, `${row.file}: canonical mismatch`);
    assert.equal($('meta[property="og:title"]').attr('content'), title, `${row.file}: Open Graph title mismatch`);
    assert.equal($('meta[property="og:description"]').attr('content'), description, `${row.file}: Open Graph description mismatch`);
    assert.equal($('meta[property="og:url"]').attr('content'), canonical, `${row.file}: Open Graph URL mismatch`);
    assert.equal($('meta[property="og:image"]').attr('content'), `https://sjmaths.com${row.image}`, `${row.file}: social image mismatch`);
    assert.equal($('meta[name="twitter:card"]').attr('content'), 'summary_large_image', `${row.file}: missing Twitter card`);
    assert.equal($('meta[name="twitter:title"]').attr('content'), title, `${row.file}: Twitter title mismatch`);
    assert.equal($('meta[name="twitter:description"]').attr('content'), description, `${row.file}: Twitter description mismatch`);
    assert.equal($('meta[name="twitter:image"]').attr('content'), `https://sjmaths.com${row.image}`, `${row.file}: Twitter image mismatch`);
  }
  assert.ok(rows.every(row => row.file.startsWith(`${BASE}/`)));
});

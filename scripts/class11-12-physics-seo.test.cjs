const test=require('node:test');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const crypto=require('node:crypto');
const cheerio=require('cheerio');
const {ROOT}=require('./seo-html.cjs');
const {rows,imagePath}=require('./lib/class11-12-physics-seo.cjs');

test('All Class 11/12 Physics pages have unique, topic-specific metadata and previews',()=>{
  assert.equal(rows.length,30);
  const titles=new Set(),descriptions=new Set(),images=new Set(),index=require(path.join(ROOT,'assets/js/search-index.json'));
  for(const row of rows){
    const file=path.join(ROOT,row.file),source=fs.readFileSync(file,'utf8'),$=cheerio.load(source),route=`https://sjmaths.com/${row.file.replace(/\/index\.html$/,'/')}`,image=`https://sjmaths.com${imagePath(row)}`;
    const meta=(name,attr='name')=>$(`meta[${attr}="${name}"]`).first().attr('content')||'';
    assert.equal($('title').length,1,row.file);assert.equal($('title').text(),row.title,row.file);
    assert.ok(!titles.has(row.title),`duplicate title ${row.title}`);titles.add(row.title);
    const description=meta('description');assert.equal(description,row.description,row.file);assert.ok(!descriptions.has(description),`duplicate description ${description}`);descriptions.add(description);
    assert.equal($('link[rel="canonical"]').attr('href'),route,row.file);assert.equal(meta('og:url','property'),route,row.file);
    assert.equal(meta('og:title','property'),row.title,row.file);assert.equal(meta('og:description','property'),row.description,row.file);
    assert.equal(meta('og:image','property'),image,row.file);assert.equal(meta('og:image:type','property'),'image/png',row.file);
    assert.equal(meta('og:image:width','property'),'1200',row.file);assert.equal(meta('og:image:height','property'),'630',row.file);
    assert.ok(meta('og:image:alt','property').length>12,row.file);assert.equal(meta('twitter:card'),'summary_large_image',row.file);
    assert.equal(meta('twitter:title'),row.title,row.file);assert.equal(meta('twitter:description'),row.description,row.file);assert.equal(meta('twitter:image'),image,row.file);assert.ok(meta('twitter:image:alt').length>12,row.file);
    assert.equal($(`meta[name="description"]`).length,1,`duplicate descriptions ${row.file}`);assert.equal($(`meta[property="og:image"]`).length,1,`duplicate OG images ${row.file}`);
    const asset=path.join(ROOT,imagePath(row).slice(1));assert.ok(fs.existsSync(asset),`missing image ${asset}`);
    const png=fs.readFileSync(asset);assert.equal(png.subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.equal(png.readUInt32BE(16),1200);assert.equal(png.readUInt32BE(20),630);
    const digest=crypto.createHash('sha256').update(png).digest('hex');assert.ok(!images.has(digest),`duplicate image ${asset}`);images.add(digest);
    const searchRoute=`/${row.file.replace(/\/index\.html$/,'/')}`,entry=index.find(item=>item.url===searchRoute);assert.ok(entry,`missing search entry ${searchRoute}`);assert.equal(entry.title,row.title.replace(/\s*\|\s*SJMaths$/,''));
  }
});

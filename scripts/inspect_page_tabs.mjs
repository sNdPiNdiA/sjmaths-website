import fs from 'fs';

function inspectTabs(file) {
  if (!fs.existsSync(file)) return;
  const html = fs.readFileSync(file, 'utf8');
  const tabs = [...html.matchAll(/data-tab=["']([^"']+)["'][^>]*>([\s\S]*?)<\/button>/gi)].map(m => ({
    tab: m[1],
    text: m[2].replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim()
  }));
  console.log(`\n=== Tabs in ${file} ===`);
  console.log(tabs);

  // Check what JSON scripts exist in the HTML
  const jsonScripts = [...html.matchAll(/<script[^>]*type=["']application\/(?:ld\+)?json["'][^>]*id=["']([^"']+)["']/gi)].map(m => m[1]);
  console.log('JSON script tags:', jsonScripts);
}

inspectTabs('upsc/ancient-history/Age-of-Mahajanapadas/Administrative-Setup/index.html');
inspectTabs('upsc/art-and-culture/Miscellaneous/Places-of-Cultural-Interest/index.html');


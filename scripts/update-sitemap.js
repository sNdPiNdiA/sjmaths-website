const fs = require('fs');
const path = require('path');
const { promisify } = require('util');

const readdir = promisify(fs.readdir);
const stat = promisify(fs.stat);
const readFile = promisify(fs.readFile);
const writeFile = promisify(fs.writeFile);

const ROOT_DIR = path.resolve(__dirname, '../');
const CLASSES_DIR = path.join(ROOT_DIR, 'classes');
const SITEMAP_PATH = path.join(ROOT_DIR, 'sitemap.xml');
const DOMAIN = 'https://www.sjmaths.com';

// Priority Configuration
const PRIORITY_MAP = {
    'index.html': '0.9', // Chapter Notes / Class Index
    'exercise': '0.8',   // Exercises
    'default': '0.7'
};

const FREQ_MAP = {
    'index.html': 'weekly',
    'exercise': 'monthly',
    'default': 'monthly'
};

async function getFiles(dir) {
    const subdirs = await readdir(dir);
    const files = await Promise.all(subdirs.map(async (subdir) => {
        const res = path.resolve(dir, subdir);
        return (await stat(res)).isDirectory() ? getFiles(res) : res;
    }));
    return files.flat();
}

function formatDate(date) {
    return date.toISOString().split('T')[0];
}

async function parseSitemap(sitemapContent) {
    const urls = new Map();
    const urlRegex = /<url>[\s\S]*?<loc>(.*?)<\/loc>[\s\S]*?<\/url>/g;
    let match;

    while ((match = urlRegex.exec(sitemapContent)) !== null) {
        const fullBlock = match[0];
        const loc = match[1];
        urls.set(loc.trim(), fullBlock);
    }
    return urls;
}

async function updateSitemap() {
    console.log('Starting Sitemap Update...');

    // 1. Read existing sitemap
    let existingSitemap = '';
    let existingUrls = new Map();
    
    if (fs.existsSync(SITEMAP_PATH)) {
        existingSitemap = await readFile(SITEMAP_PATH, 'utf8');
        existingUrls = await parseSitemap(existingSitemap);
        console.log(`Found ${existingUrls.size} existing URLs in sitemap.`);
    } else {
        console.log('No existing sitemap found. Creating new one.');
        existingSitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n</urlset>';
    }

    // 2. Scan for files
    console.log('Scanning classes directory...');
    const allFiles = await getFiles(CLASSES_DIR);
    const htmlFiles = allFiles.filter(f => f.endsWith('.html'));
    
    console.log(`Found ${htmlFiles.length} HTML files.`);

    let addedCount = 0;
    let urlSetContent = [];

    // Preserving existing entries that are still valid (optional: verify existence)
    // For now, we regenerate the list to ensure cleanliness, but we could merge.
    // User requested "sitemap.xml are existing... duplicate SEO".
    // Strategy: We will keep existing entries to respect manual edits, but update lastmod if file changed?
    // Actually, safer to rebuild to ensure no 404s, but check against "existingUrls" to preserve custom freq/prio if meaningful?
    // Given the prompt "sitemap.xml are existing", user might have manual entries.
    // Let's iterate found files and check if they exist in Map.
    
    // We will build a NEW content list. 
    // If URL exists in old sitemap, use that block (maybe update lastmod). 
    // If not, create new block.
    
    const today = formatDate(new Date());

    for (const file of htmlFiles) {
        // Construct URL
        let relativePath = path.relative(ROOT_DIR, file).replace(/\\/g, '/');
        // Handle "index.html" -> folder path for canonical usually, but sitemap often lists full file
        // Current sitemap lists folders for index.html? Let's check sample.
        // Sample: <loc>.../classes/class-10/chapter-wise-notes/chapter-1-real-numbers/</loc>
        // Use directory path if filename is index.html
        
        let urlPath = relativePath;
        if (urlPath.endsWith('index.html')) {
             urlPath = urlPath.replace('index.html', '');
        }
        
        const fullUrl = `${DOMAIN}/${urlPath}`;
        
        let entryBlock = '';

        if (existingUrls.has(fullUrl)) {
            // Entry exists. 
            // Optional: Update lastmod? 
            // For now, keep it as is to preserve manual edits or specific lastmods.
            // But wait, if we never update lastmod, search engines won't know.
            // Let's use the file's mtime for lastmod.
            
            const stats = await stat(file);
            const fileModDate = formatDate(stats.mtime);
            
            // We can replace the lastmod line in the existing block
            let block = existingUrls.get(fullUrl);
            const lastModRegex = /<lastmod>(.*?)<\/lastmod>/;
            if (lastModRegex.test(block)) {
                // If file is newer than sitemap entry, update it?
                // Or just always update to file mtime?
                // Let's update to today if we are running the script? Or file mtime? File mtime is better SEO.
                block = block.replace(lastModRegex, `<lastmod>${fileModDate}</lastmod>`);
            } else {
                // Insert after loc
                block = block.replace(/<\/loc>/, `</loc>\n    <lastmod>${fileModDate}</lastmod>`);
            }
            entryBlock = block;
            
            // Remove from map so we know what's left (orphan check)
            existingUrls.delete(fullUrl);
        } else {
            // New Entry
            const isIndex = file.endsWith('index.html');
            const isExercise = file.includes('exercise');
            
            const priority = isIndex ? PRIORITY_MAP['index.html'] : (isExercise ? PRIORITY_MAP['exercise'] : PRIORITY_MAP['default']);
            const freq = isIndex ? FREQ_MAP['index.html'] : (isExercise ? FREQ_MAP['exercise'] : FREQ_MAP['default']);
            
            const stats = await stat(file);
            const lastmod = formatDate(stats.mtime);

            entryBlock = `  <url>
    <loc>${fullUrl}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${freq}</changefreq>
    <priority>${priority}</priority>
  </url>`;
            addedCount++;
        }
        urlSetContent.push(entryBlock);
    }

    // Add remaining existing URLs (could be non-class pages, root pages etc. that we didn't scan)
    // The previous scan was only CLASSES_DIR. 
    // But sitemap has root pages too.
    for (const [url, block] of existingUrls) {
        urlSetContent.push(block);
    }

    // Sort urls for consistency (optional)
    urlSetContent.sort((a, b) => {
        const getLoc = (s) => s.match(/<loc>(.*?)<\/loc>/)[1];
        return getLoc(a).localeCompare(getLoc(b));
    });

    const newSitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urlSetContent.join('\n')}
</urlset>`;

    await writeFile(SITEMAP_PATH, newSitemap, 'utf8');
    console.log(`Sitemap updated. Added ${addedCount} new URLs. Total URLs: ${urlSetContent.length}`);
}

updateSitemap().catch(console.error);

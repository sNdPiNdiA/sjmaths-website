const fs = require('fs');
const path = require('path');
const http = require('http');

const ROOT_DIR = path.join(__dirname, '..', '..');
const PDF_DIR = path.join(ROOT_DIR, 'current-affairs', 'pdf');
const DAILY_DIR = path.join(ROOT_DIR, 'current-affairs', 'daily');
const WEEKLY_DIR = path.join(ROOT_DIR, 'current-affairs', 'weekly');
const BIMONTHLY_DIR = path.join(ROOT_DIR, 'current-affairs', 'bimonthly');
const MONTHLY_DIR = path.join(ROOT_DIR, 'current-affairs', 'monthly');

const PORT = 8081;

// 1. Zero-dependency HTTP static server to serve files to Puppeteer
function startServer() {
  const mime = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.svg': 'image/svg+xml',
    '.woff': 'font/woff',
    '.woff2': 'font/woff2',
    '.ttf': 'font/ttf'
  };

  const server = http.createServer((req, res) => {
    let urlPath = req.url.split('?')[0];
    if (urlPath.endsWith('/')) {
      urlPath += 'index.html';
    }
    const filePath = path.join(ROOT_DIR, urlPath);
    if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
      const ext = path.extname(filePath);
      res.writeHead(200, { 'Content-Type': mime[ext] || 'application/octet-stream' });
      res.end(fs.readFileSync(filePath));
    } else {
      res.writeHead(404);
      res.end('Not Found');
    }
  });

  return new Promise((resolve) => {
    server.listen(PORT, () => {
      console.log(`📡 Local static server started on http://localhost:${PORT}`);
      resolve(server);
    });
  });
}

// Helper to scan for folders matching patterns
function getPeriodFolders(parentDir, pattern) {
  if (!fs.existsSync(parentDir)) return [];
  return fs.readdirSync(parentDir)
    .filter(name => {
      const fullPath = path.join(parentDir, name);
      return fs.statSync(fullPath).isDirectory() && pattern.test(name);
    });
}

async function printPDF(page, url, outPath, filterCategory = null) {
  console.log(`📄 Printing URL: ${url} -> ${path.basename(outPath)} ${filterCategory ? `[Category: ${filterCategory}]` : '[Full]'}`);
  
  try {
    // networkidle2 is much more robust and faster than networkidle0
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });

    // Apply print styling and filtering if category is specified
    await page.evaluate((category) => {
      // Hide default header, footer, breadcrumbs, search, toggle
      const selectorsToHide = [
        '#header-container',
        '#footer-container',
        '.ca-top-bar',
        '.breadcrumbs',
        '.btn',
        '.ca-card[style*="padding: 1.5rem; margin-bottom: 2rem;"]' // Topic pills card
      ];
      selectorsToHide.forEach(sel => {
        document.querySelectorAll(sel).forEach(el => el.style.display = 'none');
      });

      if (category) {
        // Show only matching category section, hide others
        const sections = document.querySelectorAll('.ca-category-section');
        sections.forEach(sec => {
          if (sec.dataset.category === category) {
            sec.style.display = 'block';
          } else {
            sec.style.display = 'none';
          }
        });

        // Hide MCQs completely on topic-specific PDFs
        const mcqHeaders = Array.from(document.querySelectorAll('h2')).filter(h2 => h2.querySelector('.fa-check-double'));
        mcqHeaders.forEach(h2 => {
          h2.style.display = 'none';
          if (h2.nextElementSibling) {
            h2.nextElementSibling.style.display = 'none';
          }
        });
      }

      // Inject print layout stylesheet
      const style = document.createElement('style');
      style.textContent = `
        body {
          background: white !important;
          color: black !important;
          padding: 1.5rem !important;
          font-family: 'Inter', sans-serif !important;
        }
        h1, h2, h3, h4 {
          color: #2c3e50 !important;
        }
        .ca-card, .ca-mcq-card {
          box-shadow: none !important;
          border: 1px solid #ddd !important;
          page-break-inside: avoid !important;
          background: white !important;
          margin-bottom: 1.25rem !important;
        }
        .ca-mcq-option {
          background: #f8f9fa !important;
          border: 1px solid #e9ecef !important;
        }
      `;
      document.head.appendChild(style);
    }, filterCategory);

    await page.pdf({
      path: outPath,
      format: 'A4',
      margin: {
        top: '20mm',
        right: '15mm',
        bottom: '20mm',
        left: '15mm'
      },
      printBackground: true,
      displayHeaderFooter: true,
      headerTemplate: `<div style="font-size: 8px; font-family: 'Inter', sans-serif; width: 100%; text-align: center; border-bottom: 1px solid #eee; padding-bottom: 5px; margin-left: 20px; margin-right: 20px; color: #888;">SJMaths Current Affairs Platform</div>`,
      footerTemplate: `<div style="font-size: 8px; font-family: 'Inter', sans-serif; width: 100%; display: flex; justify-content: space-between; border-top: 1px solid #eee; padding-top: 5px; margin-left: 20px; margin-right: 20px; color: #888;"><span>https://sjmaths.com</span><span class="pageNumber"></span> / <span class="totalPages"></span></div>`
    });
  } catch (err) {
    console.error(`❌ Failed to print PDF for ${url} (Category: ${filterCategory || 'Full'}):`, err.message);
  }
}

async function main() {
  console.log('Checking Puppeteer dependency for PDF generation...');
  
  let puppeteer;
  try {
    puppeteer = require('puppeteer-core');
  } catch (err) {
    try {
      puppeteer = require('puppeteer');
    } catch (err2) {
      console.log('⚠️  Puppeteer or puppeteer-core is not installed. PDF generation will be skipped.');
      console.log('To enable PDF generation, run: npm install puppeteer-core --save-dev');
      return;
    }
  }

  // Start the server
  const server = await startServer();

  if (!fs.existsSync(PDF_DIR)) {
    fs.mkdirSync(PDF_DIR, { recursive: true });
  }

  // Find all folders
  const weeklyFolders = getPeriodFolders(WEEKLY_DIR, /^\d{4}-w\d{2}$/);
  const bimonthlyFolders = getPeriodFolders(BIMONTHLY_DIR, /^\d{4}-\d{2}-h[12]$/);
  const monthlyFolders = getPeriodFolders(MONTHLY_DIR, /^\d{4}-\d{2}$/);

  console.log(`Found: ${weeklyFolders.length} weekly, ${bimonthlyFolders.length} bimonthly, ${monthlyFolders.length} monthly directories.`);

  try {
    const launchOptions = {
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    };
    
    // Check if Chrome is installed at the standard Windows path and use it if puppeteer-core is used
    const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
    if (fs.existsSync(chromePath)) {
      launchOptions.executablePath = chromePath;
      console.log(`Found system Chrome at ${chromePath}, using it.`);
    }

    const browser = await puppeteer.launch(launchOptions);
    
    const page = await browser.newPage();

    // A. Weekly PDFs
    for (const folder of weeklyFolders) {
      const url = `http://localhost:${PORT}/current-affairs/weekly/${folder}/`;
      
      // Full
      const fullPath = path.join(PDF_DIR, `weekly-${folder}.pdf`);
      if (fs.existsSync(fullPath)) {
        console.log(`ℹ️ Weekly PDF already exists: ${path.basename(fullPath)}`);
      } else {
        await printPDF(page, url, fullPath);
      }
    }

    // C. Bimonthly PDFs
    for (const folder of bimonthlyFolders) {
      const url = `http://localhost:${PORT}/current-affairs/bimonthly/${folder}/`;
      
      // Full
      const fullPath = path.join(PDF_DIR, `bimonthly-${folder}.pdf`);
      if (fs.existsSync(fullPath)) {
        console.log(`ℹ️ Bimonthly PDF already exists: ${path.basename(fullPath)}`);
      } else {
        await printPDF(page, url, fullPath);
      }
    }

    // D. Monthly PDFs
    for (const folder of monthlyFolders) {
      const url = `http://localhost:${PORT}/current-affairs/monthly/${folder}/`;
      
      // Full
      const fullPath = path.join(PDF_DIR, `monthly-${folder}.pdf`);
      if (fs.existsSync(fullPath)) {
        console.log(`ℹ️ Monthly PDF already exists: ${path.basename(fullPath)}`);
      } else {
        await printPDF(page, url, fullPath);
      }

      // Inspect active categories
      await page.goto(url, { waitUntil: 'networkidle0' });
      const activeCats = await page.evaluate(() => {
        const sections = document.querySelectorAll('.ca-category-section');
        return Array.from(sections).map(sec => sec.dataset.category);
      });

      // Topic specific
      for (const cat of activeCats) {
        const outPath = path.join(PDF_DIR, `monthly-${folder}-${cat}.pdf`);
        if (fs.existsSync(outPath)) {
          console.log(`ℹ️ Topic Monthly PDF already exists: ${path.basename(outPath)}`);
          continue;
        }
        await printPDF(page, url, outPath, cat);
      }
    }

    await browser.close();
    console.log('✨ All PDFs generated successfully!');
  } catch (err) {
    console.error('Puppeteer processing failed:', err.message);
  } finally {
    // Shut down server
    server.close(() => {
      console.log('🛑 Local HTTP server stopped.');
    });
  }
}

main().catch(err => {
  console.error('Fatal PDF generator error:', err);
});

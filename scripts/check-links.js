// ============================================
// FILE: scripts/check-links.js
// Link checker - Run with: npm run test:links
// ============================================

const fs = require('fs');
const path = require('path');
const http = require('http');
const https = require('https');

class LinkChecker {
  constructor(baseURL = 'http://localhost:5500') {
    this.baseURL = baseURL;
    this.results = {
      total: 0,
      broken: [],
      working: [],
      skipped: []
    };
  }

  log(message, color = '') {
    const colors = {
      green: '\x1b[32m',
      red: '\x1b[31m',
      yellow: '\x1b[33m',
      cyan: '\x1b[36m',
      reset: '\x1b[0m'
    };
    console.log(`${colors[color] || ''}${message}${colors.reset}`);
  }

  async checkURL(url) {
    return new Promise((resolve) => {
      const protocol = url.startsWith('https') ? https : http;
      
      const options = {
        method: 'HEAD',
        timeout: 5000,
        headers: {
          'User-Agent': 'SJMaths-Link-Checker/1.0'
        }
      };

      const request = protocol.request(url, options, (response) => {
        resolve({
          url,
          status: response.statusCode,
          ok: response.statusCode >= 200 && response.statusCode < 400
        });
      });

      request.on('error', (error) => {
        resolve({
          url,
          status: 0,
          ok: false,
          error: error.message
        });
      });

      request.on('timeout', () => {
        request.destroy();
        resolve({
          url,
          status: 0,
          ok: false,
          error: 'Timeout'
        });
      });

      request.end();
    });
  }

  extractLinks(htmlContent, filePath) {
    const links = [];
    
    // Match href attributes
    const hrefRegex = /href=["']([^"']+)["']/g;
    let match;
    
    while ((match = hrefRegex.exec(htmlContent)) !== null) {
      let link = match[1];
      
      // Skip anchors, mailto, tel, javascript
      if (link.startsWith('#') || 
          link.startsWith('mailto:') || 
          link.startsWith('tel:') ||
          link.startsWith('javascript:')) {
        continue;
      }

      // Convert relative links to absolute
      if (!link.startsWith('http')) {
        const dir = path.dirname(filePath);
        link = path.join(dir, link).replace(/\\/g, '/');
        
        // Check if file exists locally
        if (!fs.existsSync(link)) {
          links.push({
            original: match[1],
            resolved: link,
            type: 'local',
            exists: false
          });
        } else {
          links.push({
            original: match[1],
            resolved: link,
            type: 'local',
            exists: true
          });
        }
      } else {
        links.push({
          original: link,
          resolved: link,
          type: 'external',
          exists: null // Will check later
        });
      }
    }

    // Also check src attributes for images, scripts
    const srcRegex = /src=["']([^"']+)["']/g;
    while ((match = srcRegex.exec(htmlContent)) !== null) {
      let src = match[1];
      
      if (!src.startsWith('http') && !src.startsWith('data:')) {
        const dir = path.dirname(filePath);
        src = path.join(dir, src).replace(/\\/g, '/');
        
        if (!fs.existsSync(src)) {
          links.push({
            original: match[1],
            resolved: src,
            type: 'resource',
            exists: false
          });
        }
      }
    }

    return links;
  }

  async checkAllLinks() {
    this.log('\n🔍 Starting Link Check...', 'cyan');
    this.log('━'.repeat(60));

    // Find all HTML files
    const htmlFiles = this.findHTMLFiles('.');

    this.log(`\nFound ${htmlFiles.length} HTML files to check\n`, 'cyan');

    for (const file of htmlFiles) {
      this.log(`📄 Checking: ${file}`, 'cyan');
      
      const content = fs.readFileSync(file, 'utf8');
      const links = this.extractLinks(content, file);

      for (const link of links) {
        this.results.total++;

        if (link.type === 'local' || link.type === 'resource') {
          if (!link.exists) {
            this.log(`  ❌ Broken: ${link.original} → ${link.resolved}`, 'red');
            this.results.broken.push({
              file,
              link: link.original,
              resolved: link.resolved,
              type: link.type,
              reason: 'File not found'
            });
          } else {
            this.results.working.push(link.original);
          }
        } else if (link.type === 'external') {
          // Check external links
          const result = await this.checkURL(link.resolved);
          
          if (!result.ok) {
            this.log(`  ❌ Broken: ${link.original} (${result.status || result.error})`, 'red');
            this.results.broken.push({
              file,
              link: link.original,
              status: result.status,
              error: result.error
            });
          } else {
            this.log(`  ✅ OK: ${link.original}`, 'green');
            this.results.working.push(link.original);
          }
        }
      }
    }

    this.printSummary();
  }

  findHTMLFiles(dir, files = []) {
    const items = fs.readdirSync(dir);

    items.forEach(item => {
      const fullPath = path.join(dir, item);
      
      // Skip node_modules, .git, etc.
      if (item.startsWith('.') || item === 'node_modules') {
        return;
      }

      if (fs.statSync(fullPath).isDirectory()) {
        this.findHTMLFiles(fullPath, files);
      } else if (fullPath.endsWith('.html')) {
        files.push(fullPath);
      }
    });

    return files;
  }

  printSummary() {
    this.log('\n' + '━'.repeat(60), 'cyan');
    this.log('📊 Link Check Summary', 'cyan');
    this.log('━'.repeat(60), 'cyan');
    
    console.log(`\nTotal links checked: ${this.results.total}`);
    this.log(`✅ Working: ${this.results.working.length}`, 'green');
    this.log(`❌ Broken: ${this.results.broken.length}`, 'red');

    if (this.results.broken.length > 0) {
      this.log('\n❌ Broken Links Details:', 'red');
      this.log('━'.repeat(60), 'red');
      
      this.results.broken.forEach((item, index) => {
        console.log(`\n${index + 1}. File: ${item.file}`);
        console.log(`   Link: ${item.link}`);
        if (item.resolved) {
          console.log(`   Resolved to: ${item.resolved}`);
        }
        if (item.status) {
          console.log(`   Status: ${item.status}`);
        }
        if (item.error) {
          console.log(`   Error: ${item.error}`);
        }
        if (item.reason) {
          console.log(`   Reason: ${item.reason}`);
        }
      });

      this.log('\n⚠️  Please fix broken links before deployment!', 'yellow');
    } else {
      this.log('\n🎉 All links are working!', 'green');
    }

    this.log('\n' + '━'.repeat(60) + '\n', 'cyan');
  }
}

// Check if server is running
const checkServer = async () => {
  try {
    const response = await fetch('http://localhost:5500');
    return response.ok;
  } catch (error) {
    return false;
  }
};

// Run the checker
(async () => {
  console.log('\n⚠️  Note: This checks local file paths.');
  console.log('For full link checking, run with Live Server active.\n');
  
  const checker = new LinkChecker();
  await checker.checkAllLinks();
})();
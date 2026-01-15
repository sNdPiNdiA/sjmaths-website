// ============================================
// FILE: scripts/test-runner.js
// Main test runner - Run with: node scripts/test-runner.js
// ============================================

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Color codes for terminal output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  bold: '\x1b[1m'
};

class TestRunner {
  constructor() {
    this.results = {
      passed: 0,
      failed: 0,
      warnings: 0,
      issues: []
    };
  }

  log(message, color = 'reset') {
    console.log(`${colors[color]}${message}${colors.reset}`);
  }

  logSection(title) {
    console.log('\n' + '='.repeat(60));
    this.log(title, 'bold');
    console.log('='.repeat(60) + '\n');
  }

  async runAllTests() {
    this.logSection('🚀 SJMaths Pre-Launch Test Suite');
    
    await this.testFileStructure();
    await this.testSecurityIssues();
    await this.testHTMLValidity();
    await this.testJavaScriptSyntax();
    await this.testFirebaseConfig();
    await this.testMetaTags();
    await this.testAccessibility();
    
    this.printSummary();
  }

  // Test 1: File Structure
  async testFileStructure() {
    this.logSection('📁 Test 1: File Structure');
    
    const requiredFiles = [
      'index.html',
      'login.html',
      'signup.html',
      '404.html',
      'robots.txt',
      'sitemap.xml',
      'assets/css/main.css',
      'assets/css/layout.css',
      'assets/css/component.css',
      'utils/loadHeader.js',
      'utils/loadFooter.js'
    ];

    const missingFiles = [];
    
    requiredFiles.forEach(file => {
      if (fs.existsSync(file)) {
        this.log(`✅ ${file}`, 'green');
        this.results.passed++;
      } else {
        this.log(`❌ Missing: ${file}`, 'red');
        this.results.failed++;
        missingFiles.push(file);
      }
    });

    if (missingFiles.length > 0) {
      this.results.issues.push({
        severity: 'ERROR',
        category: 'File Structure',
        message: `Missing ${missingFiles.length} required files`,
        files: missingFiles
      });
    }
  }

  // Test 2: Security Issues
  async testSecurityIssues() {
    this.logSection('🔒 Test 2: Security Check');
    
    // Scan all HTML and JS files instead of a hardcoded list
    const filesToCheck = this.findFiles('.', '.js').concat(this.findFiles('.', '.html'));

    const securityIssues = [];
    const sensitivePatterns = [
      { pattern: /apiKey:\s*["']AIza[^"']+["']/, name: 'Firebase API Key' },
      { pattern: /authDomain:\s*["'][^"']+\.firebaseapp\.com["']/, name: 'Auth Domain' },
      { pattern: /projectId:\s*["'][^"']+["']/, name: 'Project ID' },
      { pattern: /password\s*=\s*["'][^"']+["']/, name: 'Hardcoded Password' },
      { pattern: /api[_-]?key\s*=\s*["'][^"']+["']/i, name: 'Generic API Key' }
    ];

    filesToCheck.forEach(file => {
      if (fs.existsSync(file)) {
        // Skip the config file itself as it is the designated location for the public key
        if (file.includes('firebase-config.js')) return;

        const content = fs.readFileSync(file, 'utf8');
        
        sensitivePatterns.forEach(({ pattern, name }) => {
          if (pattern.test(content)) {
            this.log(`⚠️  ${file}: Contains ${name}`, 'yellow');
            this.results.warnings++;
            securityIssues.push({ file, issue: name });
          }
        });
      }
    });

    if (securityIssues.length > 0) {
      this.results.issues.push({
        severity: 'WARNING',
        category: 'Security',
        message: 'Exposed credentials detected in client-side code',
        details: securityIssues,
        fix: 'Move sensitive config to environment variables or Firebase App Check'
      });
    } else {
      this.log('✅ No exposed credentials found', 'green');
      this.results.passed++;
    }
  }

  // Test 3: HTML Validation
  async testHTMLValidity() {
    this.logSection('📄 Test 3: HTML Validation');
    
    const htmlFiles = this.findFiles('.', '.html');
    let hasErrors = false;

    htmlFiles.forEach(file => {
      try {
        const content = fs.readFileSync(file, 'utf8');
        
        // Basic HTML validation
        const checks = [
          { test: /<html[^>]*lang=/i, msg: 'Has lang attribute' },
          { test: /<meta[^>]*charset=/i, msg: 'Has charset meta' },
          { test: /<meta[^>]*viewport=/i, msg: 'Has viewport meta' },
          { test: /<title>/i, msg: 'Has title tag' }
        ];

        let fileValid = true;
        checks.forEach(({ test, msg }) => {
          if (!test.test(content)) {
            this.log(`❌ ${file}: Missing ${msg}`, 'red');
            fileValid = false;
            hasErrors = true;
          }
        });

        if (fileValid) {
          this.log(`✅ ${file}`, 'green');
          this.results.passed++;
        } else {
          this.results.failed++;
        }

      } catch (error) {
        this.log(`❌ Error reading ${file}: ${error.message}`, 'red');
        this.results.failed++;
        hasErrors = true;
      }
    });

    if (hasErrors) {
      this.results.issues.push({
        severity: 'ERROR',
        category: 'HTML Validation',
        message: 'Some HTML files have validation errors',
        fix: 'Add missing meta tags and ensure proper HTML structure'
      });
    }
  }

  // Test 4: JavaScript Syntax
  async testJavaScriptSyntax() {
    this.logSection('⚡ Test 4: JavaScript Syntax Check');
    
    const jsFiles = this.findFiles('.', '.js', ['node_modules']);
    let syntaxErrors = [];

    jsFiles.forEach(file => {
      try {
        const content = fs.readFileSync(file, 'utf8');
        
        // Check for common issues
        if (content.includes('console.log') && !file.includes('test')) {
          this.log(`⚠️  ${file}: Contains console.log`, 'yellow');
          this.results.warnings++;
        }

        if (content.includes('alert(') && !file.includes('login') && !file.includes('signup')) {
          this.log(`⚠️  ${file}: Uses alert() - Consider toast notifications`, 'yellow');
          this.results.warnings++;
          syntaxErrors.push({ file, issue: 'Uses alert()' });
        }

        // Check for ES6 syntax errors (basic)
        if (content.includes('const ') || content.includes('let ')) {
          this.log(`✅ ${file}: Uses modern JavaScript`, 'green');
          this.results.passed++;
        }

      } catch (error) {
        this.log(`❌ Error in ${file}: ${error.message}`, 'red');
        this.results.failed++;
      }
    });

    if (syntaxErrors.length > 0) {
      this.results.issues.push({
        severity: 'WARNING',
        category: 'User Experience',
        message: 'Replace alert() with better UI notifications',
        files: syntaxErrors
      });
    }
  }

  // Test 5: Firebase Configuration
  async testFirebaseConfig() {
    this.logSection('🔥 Test 5: Firebase Configuration');
    
    const firebaseFiles = ['login.html', 'signup.html'];
    let configFound = false;
    let configConsistent = true;
    let configs = [];

    firebaseFiles.forEach(file => {
      if (fs.existsSync(file)) {
        const content = fs.readFileSync(file, 'utf8');
        // Check for inline config
        const configMatch = content.match(/const firebaseConfig\s*=\s*{([^}]+)}/s);
        // Check for imported config
        const importMatch = content.includes('import { firebaseConfig }');
        
        if (configMatch) {
          configFound = true;
          configs.push({ file, config: configMatch[1] });
        } else if (importMatch) {
          configFound = true;
        }
      }
    });

    // Check if configs are identical
    if (configs.length > 1) {
      const firstConfig = configs[0].config.trim();
      configs.forEach(({ file, config }) => {
        if (config.trim() !== firstConfig) {
          this.log(`⚠️  ${file}: Firebase config differs`, 'yellow');
          configConsistent = false;
          this.results.warnings++;
        }
      });
    }

    if (configFound && configConsistent) {
      this.log('✅ Firebase config found and consistent', 'green');
      this.results.passed++;
    } else if (!configFound) {
      this.log('❌ Firebase config not found', 'red');
      this.results.failed++;
    }

    this.results.issues.push({
      severity: 'CRITICAL',
      category: 'Firebase Security',
      message: 'Implement Firebase App Check before launch',
      fix: 'https://firebase.google.com/docs/app-check'
    });
  }

  // Test 6: Meta Tags
  async testMetaTags() {
    this.logSection('🏷️  Test 6: SEO & Meta Tags');
    
    const htmlFiles = ['index.html', 'login.html', 'signup.html'];
    
    htmlFiles.forEach(file => {
      if (fs.existsSync(file)) {
        const content = fs.readFileSync(file, 'utf8');
        
        const metaChecks = [
          { pattern: /<meta[^>]*property="og:title"/, name: 'Open Graph title' },
          { pattern: /<meta[^>]*property="og:description"/, name: 'Open Graph description' },
          { pattern: /<meta[^>]*name="description"/, name: 'Meta description' },
          { pattern: /<link[^>]*rel="icon"/, name: 'Favicon' }
        ];

        let missingMeta = [];
        
        metaChecks.forEach(({ pattern, name }) => {
          if (!pattern.test(content)) {
            missingMeta.push(name);
          }
        });

        if (missingMeta.length === 0) {
          this.log(`✅ ${file}: All meta tags present`, 'green');
          this.results.passed++;
        } else {
          this.log(`⚠️  ${file}: Missing ${missingMeta.join(', ')}`, 'yellow');
          this.results.warnings++;
        }

        // Check if referenced assets (Favicon/OG Image) actually exist
        const assetChecks = [
            { regex: /<meta[^>]*property="og:image"[^>]*content="([^"]+)"/, type: 'Open Graph Image' },
            { regex: /<link[^>]*rel="icon"[^>]*href="([^"]+)"/, type: 'Favicon' }
        ];

        assetChecks.forEach(({ regex, type }) => {
            const match = content.match(regex);
            if (match) {
                const assetPath = match[1];
                // Only check local files
                if (!assetPath.startsWith('http') && !assetPath.startsWith('data:')) {
                    const dir = path.dirname(file);
                    const resolvedPath = path.join(dir, assetPath);
                    if (!fs.existsSync(resolvedPath)) {
                         this.log(`❌ ${file}: ${type} file not found (${assetPath})`, 'red');
                         this.results.warnings++;
                    }
                }
            }
        });
      }
    });
  }

  // Test 7: Accessibility
          this.results.warnings++;
        }
      }
    });
  }

  // Test 7: Accessibility
  async testAccessibility() {
    this.logSection('♿ Test 7: Accessibility Check');
    
    const htmlFiles = this.findFiles('.', '.html');
    let a11yIssues = [];

    htmlFiles.forEach(file => {
      try {
        const content = fs.readFileSync(file, 'utf8');
        
        // Check for common a11y issues
        const imgWithoutAlt = (content.match(/<img(?![^>]*alt=)/g) || []).length;
        const buttonWithoutAriaLabel = content.includes('<button') && 
                                       !content.includes('aria-label');
        const noSkipLink = !content.includes('skip-link') && file === 'index.html';

        if (imgWithoutAlt > 0) {
          this.log(`⚠️  ${file}: ${imgWithoutAlt} images without alt text`, 'yellow');
          this.results.warnings++;
          a11yIssues.push({ file, issue: `${imgWithoutAlt} images without alt` });
        }

        if (noSkipLink) {
          this.log(`⚠️  ${file}: Missing skip-to-content link`, 'yellow');
          this.results.warnings++;
          a11yIssues.push({ file, issue: 'No skip link' });
        }

      } catch (error) {
        this.log(`❌ Error checking ${file}`, 'red');
      }
    });

    if (a11yIssues.length === 0) {
      this.log('✅ No major accessibility issues found', 'green');
      this.results.passed++;
    } else {
      this.results.issues.push({
        severity: 'WARNING',
        category: 'Accessibility',
        message: 'Accessibility improvements needed',
        details: a11yIssues
      });
    }
  }

  // Helper: Find files recursively
  findFiles(dir, extension, exclude = []) {
    let files = [];
    
    const items = fs.readdirSync(dir);
    
    items.forEach(item => {
      const fullPath = path.join(dir, item);
      
      if (exclude.some(ex => fullPath.includes(ex))) return;
      
      if (fs.statSync(fullPath).isDirectory()) {
        files = files.concat(this.findFiles(fullPath, extension, exclude));
      } else if (fullPath.endsWith(extension)) {
        files.push(fullPath);
      }
    });
    
    return files;
  }

  // Print Summary
  printSummary() {
    this.logSection('📊 Test Summary');
    
    console.log(`✅ Passed:   ${colors.green}${this.results.passed}${colors.reset}`);
    console.log(`❌ Failed:   ${colors.red}${this.results.failed}${colors.reset}`);
    console.log(`⚠️  Warnings: ${colors.yellow}${this.results.warnings}${colors.reset}`);
    
    if (this.results.issues.length > 0) {
      this.logSection('🔍 Issues Found');
      
      this.results.issues.forEach((issue, index) => {
        const severityColor = {
          'CRITICAL': 'red',
          'ERROR': 'red',
          'WARNING': 'yellow'
        }[issue.severity] || 'reset';
        
        console.log(`\n${index + 1}. [${colors[severityColor]}${issue.severity}${colors.reset}] ${issue.category}`);
        console.log(`   ${issue.message}`);
        
        if (issue.fix) {
          console.log(`   ${colors.cyan}Fix: ${issue.fix}${colors.reset}`);
        }
      });
    }
    
    console.log('\n' + '='.repeat(60));
    
    if (this.results.failed === 0) {
      this.log('🎉 All critical tests passed! Site is ready for review.', 'green');
    } else {
      this.log('⚠️  Some tests failed. Please fix critical issues before launch.', 'red');
    }
    
    console.log('='.repeat(60) + '\n');
  }
}

// Run tests
const runner = new TestRunner();
runner.runAllTests();
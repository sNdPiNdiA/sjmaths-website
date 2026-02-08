// ============================================
// FILE: scripts/security-check.js
// Security scanner - Run with: npm run test:security
// ============================================

const fs = require('fs');
const path = require('path');

const COLORS = {
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  cyan: '\x1b[36m',
  bold: '\x1b[1m',
  reset: '\x1b[0m'
};

class SecurityScanner {
  constructor() {
    this.vulnerabilities = {
      critical: [],
      high: [],
      medium: [],
      low: []
    };
    this.initPatterns();
  }

  log(message, color = '') {
    console.log(`${COLORS[color] || ''}${message}${COLORS.reset}`);
  }

  initPatterns() {
    this.credentialPatterns = [
      {
        regex: /apiKey:\s*["']AIza[A-Za-z0-9_-]{35}["']/g,
        name: 'Firebase API Key',
        severity: 'critical',
        description: 'Firebase API key exposed in client-side code',
        fix: 'Move to environment variables or use Firebase App Check'
      },
      {
        regex: /authDomain:\s*["'][\w-]+\.firebaseapp\.com["']/g,
        name: 'Firebase Auth Domain',
        severity: 'medium',
        description: 'Firebase auth domain visible (acceptable if API key is protected)',
        fix: 'Ensure Firebase security rules are properly configured'
      },
      {
        regex: /password\s*[:=]\s*["'][^"']{6,}["']/gi,
        name: 'Hardcoded Password',
        severity: 'critical',
        description: 'Password hardcoded in source code',
        fix: 'Remove immediately and use environment variables'
      },
      {
        regex: /secret[_-]?key\s*[:=]\s*["'][^"']+["']/gi,
        name: 'Secret Key',
        severity: 'critical',
        description: 'Secret key exposed',
        fix: 'Use environment variables and rotate the key'
      },
      {
        regex: /bearer\s+[A-Za-z0-9_-]{20,}/gi,
        name: 'Bearer Token',
        severity: 'high',
        description: 'Authentication token exposed',
        fix: 'Remove token and regenerate'
      }
    ];

    this.xssPatterns = [
      {
        regex: /innerHTML\s*=\s*[^;]+/g,
        name: 'innerHTML Usage',
        severity: 'medium',
        description: 'Direct innerHTML assignment can lead to XSS',
        fix: 'Use textContent or sanitize input with DOMPurify'
      },
      {
        regex: /document\.write\s*\(/g,
        name: 'document.write',
        severity: 'high',
        description: 'document.write can be exploited for XSS',
        fix: 'Use modern DOM manipulation methods'
      },
      {
        regex: /eval\s*\(/g,
        name: 'eval() Usage',
        severity: 'critical',
        description: 'eval() executes arbitrary code',
        fix: 'Never use eval(). Use JSON.parse() for JSON data'
      },
      {
        regex: /dangerouslySetInnerHTML/g,
        name: 'dangerouslySetInnerHTML',
        severity: 'high',
        description: 'React dangerouslySetInnerHTML can cause XSS',
        fix: 'Sanitize HTML before rendering'
      }
    ];
  }

  // Scan for exposed credentials
  scanExposedCredentials(content, file) {
    this.credentialPatterns.forEach(({ regex, name, severity, description, fix }) => {
      const matches = content.match(regex);
      if (matches) {
        this.vulnerabilities[severity].push({
          file,
          type: name,
          description,
          fix,
          occurrences: matches.length
        });
      }
    });
  }

  // Scan for XSS vulnerabilities
  scanXSS(content, file) {
    this.xssPatterns.forEach(({ regex, name, severity, description, fix }) => {
      const matches = content.match(regex);
      if (matches) {
        this.vulnerabilities[severity].push({
          file,
          type: name,
          description,
          fix,
          occurrences: matches.length
        });
      }
    });
  }

  // Scan for insecure HTTP resources
  scanInsecureResources(content, file) {
    // Only flag http:// in src/href (not in comments or localhost)
    const httpRegex = /(?:src|href)=["']http:\/\/(?!localhost|127\.0\.0\.1)[^"']+["']/g;
    const matches = content.match(httpRegex);
    
    if (matches) {
      this.vulnerabilities.medium.push({
        file,
        type: 'Insecure HTTP Resources',
        description: `${matches.length} resources loaded over HTTP instead of HTTPS`,
        fix: 'Change all external resources to HTTPS',
        occurrences: matches.length
      });
    }
  }

  // Scan for console.log in production
  scanDebugCode(content, file) {
    const debugPatterns = [
      {
        regex: /console\.log\(/g,
        name: 'console.log',
        message: 'Debug logs in production code'
      },
      {
        regex: /console\.debug\(/g,
        name: 'console.debug',
        message: 'Debug statements in production'
      },
      {
        regex: /debugger;/g,
        name: 'debugger statement',
        message: 'Debugger breakpoint in code'
      }
    ];

    debugPatterns.forEach(({ regex, name, message }) => {
      const matches = content.match(regex);
      if (matches) {
        this.vulnerabilities.low.push({
          file,
          type: name,
          description: message,
          fix: 'Remove or conditionally disable in production',
          occurrences: matches.length
        });
      }
    });
  }

  // Scan for weak Firebase security rules indicators
  scanFirebaseRules(content, file) {
    // Check if Firebase is configured without proper auth checks
    if (content.includes('signInWithEmailAndPassword') || 
        content.includes('createUserWithEmailAndPassword')) {
      
      // Look for common security issues
      if (!content.includes('setPersistence')) {
        this.vulnerabilities.low.push({
          file,
          type: 'Firebase Persistence Not Set',
          description: 'Auth persistence not configured',
          fix: 'Use setPersistence() to control session behavior',
          occurrences: 1
        });
      }
    }
  }

  // Main scan function
  async scanDirectory(dir = '.', exclude = ['node_modules', '.git', 'dist']) {
    this.log('\n🔒 Starting Security Scan...', 'cyan');
    this.log('━'.repeat(60), 'cyan');

    const files = this.getAllFiles(dir, exclude);
    let scannedCount = 0;

    for (const file of files) {
      // Only scan relevant files
      if (!file.endsWith('.js') && 
          !file.endsWith('.html') && 
          !file.endsWith('.jsx') &&
          !file.endsWith('.tsx')) {
        continue;
      }

      scannedCount++;
      const content = fs.readFileSync(file, 'utf8');

      // Run all scans
      this.scanExposedCredentials(content, file);
      this.scanXSS(content, file);
      this.scanInsecureResources(content, file);
      this.scanDebugCode(content, file);
      this.scanFirebaseRules(content, file);
    }

    this.log(`\n✅ Scanned ${scannedCount} files\n`, 'green');
    this.printReport();
  }

  getAllFiles(dir, exclude = []) {
    let files = [];
    const items = fs.readdirSync(dir);

    items.forEach(item => {
      const fullPath = path.join(dir, item);
      
      // Skip excluded directories
      if (exclude.some(ex => fullPath.includes(ex))) {
        return;
      }

      if (fs.statSync(fullPath).isDirectory()) {
        files = files.concat(this.getAllFiles(fullPath, exclude));
      } else {
        files.push(fullPath);
      }
    });

    return files;
  }

  printReport() {
    this.log('━'.repeat(60), 'cyan');
    this.log('📊 Security Scan Report', 'bold');
    this.log('━'.repeat(60), 'cyan');

    const total = Object.values(this.vulnerabilities).reduce((sum, arr) => sum + arr.length, 0);

    console.log(`\nTotal Issues Found: ${total}`);
    this.log(`🔴 Critical: ${this.vulnerabilities.critical.length}`, 'red');
    this.log(`🟠 High: ${this.vulnerabilities.high.length}`, 'yellow');
    this.log(`🟡 Medium: ${this.vulnerabilities.medium.length}`, 'yellow');
    this.log(`🟢 Low: ${this.vulnerabilities.low.length}`, 'green');

    // Print details by severity
    ['critical', 'high', 'medium', 'low'].forEach(severity => {
      if (this.vulnerabilities[severity].length > 0) {
        const icon = {
          critical: '🔴',
          high: '🟠',
          medium: '🟡',
          low: '🟢'
        }[severity];

        this.log(`\n${icon} ${severity.toUpperCase()} Severity Issues:`, 'bold');
        this.log('─'.repeat(60));

        this.vulnerabilities[severity].forEach((vuln, index) => {
          console.log(`\n${index + 1}. ${vuln.type}`);
          console.log(`   File: ${vuln.file}`);
          console.log(`   Description: ${vuln.description}`);
          console.log(`   Occurrences: ${vuln.occurrences}`);
          this.log(`   Fix: ${vuln.fix}`, 'cyan');
        });
      }
    });

    // Overall assessment
    this.log('\n' + '━'.repeat(60), 'cyan');
    
    if (this.vulnerabilities.critical.length > 0) {
      this.log('❌ CRITICAL ISSUES FOUND - DO NOT DEPLOY', 'red');
      this.log('Fix all critical vulnerabilities before going live!', 'red');
      process.exit(1);
    } else if (this.vulnerabilities.high.length > 0) {
      this.log('⚠️  HIGH PRIORITY ISSUES - Fix before deployment', 'yellow');
    } else if (total > 0) {
      this.log('✅ No critical issues, but improvements recommended', 'yellow');
    } else {
      this.log('✅ No major security issues detected!', 'green');
      this.log('Remember to always review Firebase security rules manually.', 'cyan');
    }

    this.log('━'.repeat(60) + '\n', 'cyan');

    // Security checklist reminder
    this.log('📋 Additional Security Checklist:', 'cyan');
    console.log('  □ Firebase security rules configured');
    console.log('  □ Firebase App Check enabled');
    console.log('  □ HTTPS enforced');
    console.log('  □ CSP headers configured');
    console.log('  □ Rate limiting implemented');
    console.log('  □ Input validation on all forms');
    console.log('  □ API keys rotated if exposed');
    console.log('');
  }
}

// Run the scanner
const scanner = new SecurityScanner();
scanner.scanDirectory();
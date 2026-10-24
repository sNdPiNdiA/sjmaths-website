#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const indexPath = path.join(ROOT, 'index.html');
let html = fs.readFileSync(indexPath, 'utf8');

const target = '<div id="footer-container"></div>';
const staticFooter = `<div id="footer-container">
        <footer id="site-footer" class="sf notranslate">
          <div class="sf-inner">
            <nav class="sf-mobile-legal" aria-label="Footer essentials">
              <a href="/pages/about.html">About Us</a>
              <a href="/pages/contact.html">Contact</a>
              <a href="/pages/privacy-policy.html">Privacy Policy</a>
              <a href="/pages/terms.html">Terms</a>
              <a href="/pages/disclaimer.html">Disclaimer</a>
            </nav>
            <div class="sf-grid">
              <div class="sf-brand-col">
                <a href="/" class="sf-brand-name"><span>&int;</span> SJMaths</a>
                <p class="sf-desc">Empowering students with authentic, concept-driven resources for CBSE Class 9–12 Mathematics, competitive entrance exams, and UPSC Civil Services preparation.</p>
                <div class="sf-social">
                  <a href="/pages/contact.html" class="social-link" aria-label="Contact"><i class="fas fa-envelope"></i></a>
                  <a href="tel:+919170940900" class="social-link" aria-label="Call"><i class="fas fa-phone"></i></a>
                </div>
              </div>
              <div class="sf-link-col">
                <h4>Trust &amp; Legal</h4>
                <ul class="sf-links">
                  <li><a href="/pages/about.html">About Us</a></li>
                  <li><a href="/pages/contact.html">Contact Us</a></li>
                  <li><a href="/pages/privacy-policy.html">Privacy Policy</a></li>
                  <li><a href="/pages/terms.html">Terms &amp; Conditions</a></li>
                  <li><a href="/pages/disclaimer.html">Disclaimer</a></li>
                </ul>
              </div>
              <div class="sf-link-col">
                <h4>Popular Resources</h4>
                <ul class="sf-links">
                  <li><a href="/class-10-maths/">Class 10 Maths</a></li>
                  <li><a href="/class-12-maths/">Class 12 Maths</a></li>
                  <li><a href="/class-9-maths/">Class 9 Maths</a></li>
                  <li><a href="/class-11-maths/">Class 11 Maths</a></li>
                  <li><a href="/upsc/">UPSC Exam Prep</a></li>
                </ul>
              </div>
              <div class="sf-contact-col">
                <h4>Direct Support</h4>
                <div class="sf-links">
                  <div class="sf-contact-item"><i class="fas fa-envelope"></i> <a href="mailto:support@sjmaths.com">support@sjmaths.com</a></div>
                  <div class="sf-contact-item"><i class="fas fa-phone"></i> <a href="tel:+919170940900">+91-9170940900</a></div>
                  <div class="sf-contact-item"><i class="fas fa-map-marker-alt"></i> <span>Uttar Pradesh, India</span></div>
                </div>
              </div>
            </div>
            <div class="sf-bottom">
              <p>&copy; 2024–2026 SJMaths. All rights reserved. Free, authentic educational learning platform.</p>
            </div>
          </div>
        </footer>
    </div>`;

if (html.includes(target)) {
  html = html.replace(target, staticFooter);
  fs.writeFileSync(indexPath, html, 'utf8');
  console.log('Successfully injected static footer into index.html');
} else {
  console.log('Target <div id="footer-container"></div> already populated or not found in index.html');
}


import fs from 'node:fs';

const staticFooterContent = `<div id="footer-container">
  <style>
    #site-footer.sf { background: var(--bg-subtle, #f8fafc); color: var(--text-muted, #475569); padding: 2.5rem 1rem 1.5rem; margin-top: auto; border-top: 1px solid var(--border-subtle, #e2e8f0); font-family: var(--font-main, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif); }
    #site-footer .sf-inner { max-width: 1200px; margin: 0 auto; padding: 0 1rem; }
    #site-footer .sf-grid { display: grid; grid-template-columns: 1.4fr 1fr 1fr 1fr; gap: 2rem; }
    #site-footer .sf-brand-name { font-size: 1.35rem; font-weight: 800; color: var(--brand-primary-dark, #0f172a); text-decoration: none; display: inline-flex; align-items: center; gap: .4rem; }
    #site-footer .sf-brand-name span { color: var(--brand-primary, #059669); font-size: 1.6rem; }
    #site-footer .sf-desc { color: var(--text-muted, #64748b); font-size: .88rem; line-height: 1.55; margin: .6rem 0 1rem; }
    #site-footer .sf-social { display: flex; gap: .8rem; }
    #site-footer .sf-social .social-link { color: var(--text-muted, #64748b); font-size: 1.1rem; text-decoration: none; }
    #site-footer .sf-social .social-link:hover { color: var(--brand-primary, #059669); }
    #site-footer h4 { font-size: .92rem; font-weight: 700; margin-bottom: .8rem; color: var(--text-heading, #0f172a); text-transform: uppercase; letter-spacing: .05em; }
    #site-footer .sf-links { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: .5rem; }
    #site-footer .sf-links a { color: var(--text-muted, #64748b); text-decoration: none; font-size: .86rem; transition: color .2s; }
    #site-footer .sf-links a:hover { color: var(--brand-primary, #059669); }
    #site-footer .sf-contact-item { display: flex; align-items: center; gap: 8px; color: var(--text-muted, #64748b); font-size: .86rem; margin-bottom: .45rem; }
    #site-footer .sf-contact-item a { color: inherit; text-decoration: none; }
    #site-footer .sf-bottom { margin-top: 2rem; padding-top: 1.2rem; border-top: 1px solid var(--border-subtle, #e2e8f0); color: var(--text-muted, #94a3b8); font-size: .8rem; text-align: center; }
    #site-footer .sf-mobile-legal { display: none; }
    @media (max-width: 768px) {
      #site-footer.sf { padding: 1.5rem 1rem 1rem; }
      #site-footer .sf-mobile-legal { display: flex; flex-wrap: wrap; justify-content: center; gap: .4rem .9rem; margin-bottom: 1.2rem; border-bottom: 1px solid var(--border-subtle, #e2e8f0); padding-bottom: .8rem; }
      #site-footer .sf-mobile-legal a { color: var(--brand-primary, #059669); font-size: .82rem; font-weight: 600; text-decoration: none; }
      #site-footer .sf-grid { grid-template-columns: 1fr; gap: 1.2rem; text-align: center; }
      #site-footer .sf-links { flex-direction: row; flex-wrap: wrap; justify-content: center; gap: .3rem .8rem; }
      #site-footer .sf-links li { display: inline; }
      #site-footer .sf-contact-item, #site-footer .sf-social { justify-content: center; }
    }
    body.dark-mode #site-footer.sf { background: var(--bg-surface, #1e293b); border-top-color: rgba(255, 255, 255, 0.08); }
    body.dark-mode #site-footer .sf-brand-name { color: #f8fafc; }
    body.dark-mode #site-footer h4 { color: #f1f5f9; }
    body.dark-mode #site-footer .sf-desc, body.dark-mode #site-footer .sf-links a, body.dark-mode #site-footer .sf-contact-item { color: #94a3b8; }
    body.dark-mode #site-footer .sf-bottom { border-top-color: rgba(255, 255, 255, 0.08); color: #64748b; }
  </style>
  <footer id="site-footer" class="sf notranslate">
    <div class="sf-inner">
      <nav class="sf-mobile-legal" aria-label="Footer essentials">
        <a href="/pages/about.html">About</a>
        <a href="/pages/contact.html">Contact</a>
        <a href="/pages/privacy-policy.html">Privacy</a>
        <a href="/pages/terms.html">Terms</a>
        <a href="/pages/disclaimer.html">Disclaimer</a>
      </nav>
      <div class="sf-grid">
        <div class="sf-brand-col">
          <a href="/" class="sf-brand-name"><span>&int;</span> SJMaths</a>
          <p class="sf-desc">Empowering students with comprehensive, authentic resources for CBSE Class 9–12 Mathematics, competitive entrance exams, and UPSC preparation.</p>
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

function transform(c) {
  if (c.includes('id="site-footer"') && c.includes('/pages/privacy-policy.html')) {
    return { type: 'already', content: c };
  }
  // 1. Empty container
  const emptyRegex = /<div id=["']footer-container["']>\s*<\/div>/i;
  if (emptyRegex.test(c)) {
    return { type: 'empty_container', content: c.replace(emptyRegex, staticFooterContent) };
  }
  // 2. Old footer tag (match <footer ...> ... </footer>)
  const oldFooterRegex = /<footer[\s>][\s\S]*?<\/footer>/i;
  if (oldFooterRegex.test(c)) {
    return { type: 'old_footer', content: c.replace(oldFooterRegex, staticFooterContent) };
  }
  // 3. No footer
  if (c.includes('</main>')) {
    return { type: 'after_main', content: c.replace('</main>', `</main>\n${staticFooterContent}`) };
  }
  if (c.includes('</body>')) {
    return { type: 'before_body', content: c.replace('</body>', `${staticFooterContent}\n</body>`) };
  }
  return { type: 'none', content: c };
}

const sample1 = fs.readFileSync('upsc/ancient-history/index.html', 'utf8');
const r1 = transform(sample1);
console.log('Sample 1 (empty container):', r1.type, 'len diff:', r1.content.length - sample1.length);

const sample2 = fs.readFileSync('agriculture/agricultural-botany/cell-biology/biology-of-cell/index.html', 'utf8');
const r2 = transform(sample2);
console.log('Sample 2 (old footer):', r2.type, 'len diff:', r2.content.length - sample2.length);

const sample3 = fs.readFileSync('class-10-maths/previous-year-questions/chapter-13-statistics/ogive.html', 'utf8');
const r3 = transform(sample3);
console.log('Sample 3 (no footer):', r3.type, 'len diff:', r3.content.length - sample3.length);


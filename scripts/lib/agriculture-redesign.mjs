import { agricultureRedesignedScript as upgradedScript, hydrateAgricultureRuntime } from './agriculture-runtime.mjs';

const customCss = `<style>
:root {
  --brand: #14532d;
  --brand-dark: #052e16;
  --brand-light: #16a34a;
  --accent: #15803d;
  --accent-hover: #166534;
  --accent-soft: rgba(21, 128, 61, 0.08);
  --accent-border: rgba(21, 128, 61, 0.24);
}
html.dark, body.dark-mode {
  --brand: #4ade80;
  --brand-dark: #86efac;
  --brand-light: #22c55e;
  --accent: #34d399;
  --accent-hover: #6ee7b7;
  --accent-soft: rgba(52, 211, 153, 0.14);
  --accent-border: rgba(52, 211, 153, 0.35);
}
.desk-only { display: none; }
@media (min-width: 640px) {
  .desk-only { display: inline; }
}
</style>`;

export function transformHtml(html) {
  let updated = hydrateAgricultureRuntime(html);

  // 1. Clean raw LaTeX dollars in text ($2n$ -> 2n, $A$ -> A)
  updated = updated.replace(/\$([^\$]+)\$/g, '$1');

  // 2. Replace brand mark SJ with mathematical integral symbol &int;
  updated = updated.replace(
    /<span class="brand-mark"[^>]*>SJ<\/span>/g,
    '<span class="brand-mark" style="background: linear-gradient(145deg, #14532d, #16a34a); font-family: serif; font-size: 1.35rem; font-style: italic; display: flex; align-items: center; justify-content: center;">&int;</span>'
  );

  // 3. Responsive header buttons
  updated = updated.replace(
    /<div class="header-actions">[\s\S]*?<\/div>\s*<\/div>\s*<\/header>/,
    `<div class="header-actions">
      <button type="button" class="theme-toggle-btn" id="btn-theme-toggle" aria-label="Toggle Dark Mode">🌙 Dark Mode</button>
      <a class="back-btn" href="/up-pgt-agriculture/" title="UP PGT Agriculture Tracker">← UP PGT<span class="desk-only"> Agriculture</span></a>
      <a class="back-btn" href="/up-tgt-agriculture/" title="UP TGT Agriculture Tracker">← UP TGT<span class="desk-only"> Agriculture</span></a>
    </div>
  </div>
</header>`
  );

  // 4. Ensure root CSS includes dark mode variables and desk-only helper
  if (!updated.includes('html.dark, body.dark-mode')) {
    updated = updated.replace(/<style>[\s\S]*?<\/style>/, customCss);
  }

  // 5. Replace script tag at bottom of body
  updated = updated.replace(/<script>[\s\S]*?<\/script>\s*<\/body>/, `${upgradedScript}\n</body>`);

  return updated;
}


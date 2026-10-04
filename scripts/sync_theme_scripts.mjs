import fs from 'fs';
import path from 'path';
import { upUpperPrimaryHeadThemeBootstrap, upUpperPrimaryBodyThemeBootstrap } from './lib/up-upper-primary-theme-bootstrap.mjs';

const baseDir = path.join(process.cwd(), 'up-upper-primary-teacher', 'hindi');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });

const headScript = `<!-- Theme & Palette Sync Script (Light / Dark Mode Persistence matching Homepage) -->
<script>
    (function () {
        ${upUpperPrimaryHeadThemeBootstrap}
        const savedTheme = localStorage.getItem('sjmaths-theme');
        const themePalettes = {
            green: { primary: '#059669', 'primary-dark': '#047857', 'primary-light': '#ecfdf5' },
            blue: { primary: '#2563eb', 'primary-dark': '#1e40af', 'primary-light': '#eff6ff' },
            purple: { primary: '#7c3aed', 'primary-dark': '#6d28d9', 'primary-light': '#f5f3ff' },
            orange: { primary: '#ea580c', 'primary-dark': '#c2410c', 'primary-light': '#fff7ed' }
        };
        if (savedTheme && themePalettes[savedTheme]) {
            Object.entries(themePalettes[savedTheme]).forEach(([k, v]) => {
                document.documentElement.style.setProperty('--brand-' + k, v);
            });
        }
    })();
</script>
</head>`;

let updated = 0;
for (const entry of entries) {
  if (entry.isDirectory()) {
    const file = path.join(baseDir, entry.name, 'index.html');
    if (fs.existsSync(file)) {
      let content = fs.readFileSync(file, 'utf8');

      // Inject theme head script if not present
      if (!content.includes('data-theme-preference')) {
        content = content.replace('</head>', headScript);
      }

      // Inject body dark-mode immediate class script
      if (!content.includes("getAttribute('data-theme') === 'dark'")) {
        content = content.replace(/<body([^>]*)>/, `<body$1>\n<script>\n    ${upUpperPrimaryBodyThemeBootstrap}\n</script>`);
      }

      fs.writeFileSync(file, content, 'utf8');
      updated++;
    }
  }
}
console.log('Successfully injected theme & dark mode persistence into', updated, 'topic files.');

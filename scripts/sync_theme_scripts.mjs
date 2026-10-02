import fs from 'fs';
import path from 'path';

const baseDir = path.join(process.cwd(), 'up-upper-primary-teacher', 'hindi');
const entries = fs.readdirSync(baseDir, { withFileTypes: true });

const headScript = `<!-- Theme & Palette Sync Script (Light / Dark Mode Persistence matching Homepage) -->
<script>
    (function () {
        const isDark = localStorage.getItem('sjmaths-dark') !== 'off';
        if (isDark) document.documentElement.classList.add('dark-mode');
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
      if (!content.includes('localStorage.getItem(\'sjmaths-dark\')')) {
        content = content.replace('</head>', headScript);
      }

      // Inject body dark-mode immediate class script
      if (!content.includes('document.body.classList.add(\'dark-mode\')')) {
        content = content.replace(/<body([^>]*)>/, `<body$1>\n<script>\n    (function () {\n        const isDark = localStorage.getItem('sjmaths-dark') !== 'off';\n        if (isDark) document.body.classList.add('dark-mode');\n    })();\n</script>`);
      }

      fs.writeFileSync(file, content, 'utf8');
      updated++;
    }
  }
}
console.log('Successfully injected theme & dark mode persistence into', updated, 'topic files.');

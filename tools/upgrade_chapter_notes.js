import fs from 'fs';
import path from 'path';

const classes = ['class-9-maths', 'class-10-maths', 'class-11-maths', 'class-12-maths'];

// Reuse standard mapping structures to map between folder names of notes vs other resources
const folderMappings = {
  'class-9-maths': {
    'chapter-1-use-of-coordinates': { ncert: 'chapter-1-use-of-coordinates', sheet: 'chapter-1-number-system', exemplar: 'chapter-1-number-system', test: 'chapter-1-number-system' },
    'chapter-2-linear-polynomials': { ncert: 'chapter-2-polynomials', sheet: 'chapter-2-polynomials', exemplar: 'chapter-2-polynomials', test: 'chapter-2-polynomials' },
    'chapter-3-world-of-numbers': { ncert: 'chapter-3-coordinate-geometry', sheet: 'chapter-3-coordinate-geometry', exemplar: 'chapter-3-coordinate-geometry', test: 'chapter-3-coordinate-geometry' },
    'chapter-4-algebraic-identities': { ncert: 'chapter-4-linear-equations-in-two-variables', sheet: 'chapter-4-linear-equations-in-two-variables', exemplar: 'chapter-4-linear-equations-in-two-variables', test: 'chapter-4-linear-equations-in-two-variables' },
    'chapter-5-circles': { ncert: 'chapter-5-circles', sheet: 'chapter-5-introduction-to-euclids-geometry', exemplar: 'chapter-5-circles', test: 'chapter-5-introduction-to-euclids-geometry' },
    'chapter-6-perimeter-and-area': { ncert: 'chapter-6-perimeter-and-area', sheet: 'chapter-6-lines-and-angles', exemplar: 'chapter-6-perimeter-and-area', test: 'chapter-6-lines-and-angles' },
    'chapter-7-probability': { ncert: 'chapter-7-probability', sheet: 'chapter-7-triangles', exemplar: 'chapter-7-probability', test: 'chapter-7-triangles' },
    'chapter-8-sequences-and-progressions': { ncert: 'chapter-8-sequences-and-progressions', sheet: 'chapter-8-quadrilaterals', exemplar: 'chapter-8-sequences-and-progressions', test: 'chapter-8-quadrilaterals' },
    'chapter-9-triangles': { ncert: 'chapter-9-triangles', sheet: 'chapter-9-circles', exemplar: 'chapter-9-triangles', test: 'chapter-9-circles' },
    'chapter-10-herons-formula': { ncert: 'chapter-10-herons-formula', sheet: 'chapter-10-herons-formula', exemplar: 'chapter-10-heron-formula', test: 'chapter-10-herons-formula' },
    'chapter-11-surface-areas-and-volumes': { ncert: 'chapter-11-surface-areas-and-volumes', sheet: 'chapter-11-surface-areas-and-volumes', exemplar: 'chapter-11-surface-areas-and-volumes', test: 'chapter-11-surface-areas-and-volumes' },
    'chapter-12-statistics': { ncert: 'chapter-12-statistics', sheet: 'chapter-12-statistics', exemplar: 'chapter-12-statistics', test: 'chapter-12-statistics' }
  }
};

// Helper to clean up titles for tabs
function cleanExerciseName(file) {
  const base = file.replace('.html', '');
  if (base.startsWith('exercise-')) {
    const parts = base.split('-');
    if (parts.length >= 3) {
      return `Exercise ${parts[1]}.${parts[2]}`;
    }
    return `Exercise ${parts[1].toUpperCase()}`;
  }
  if (base === 'misc-exercise') return 'Miscellaneous';
  return base.charAt(0).toUpperCase() + base.slice(1);
}

// Sidebar Dock CSS style to inject
const dockStyle = `
<!-- DOCK SYSTEM NAVIGATION STYLING -->
<style>
/* =========================================================
   DUAL DESKTOP-FIXED & MOBILE-FLOATING SIDEBAR DOCK SYSTEM
   ========================================================= */

/* DESKTOP MODE (≥768px): Fixed Top Navigation Bar */
.chapter-nav-wrapper {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.96);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-bottom: 1px solid #e2e8f0;
    box-shadow: 0 4px 20px rgba(15, 23, 42, 0.04);
    padding: 0.6rem 0;
    margin-bottom: 1.8rem;
    overflow: visible !important;
}

.chapter-nav-container {
    max-width: 1140px;
    margin: 0 auto;
    padding: 0 1.2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    flex-wrap: wrap;
    overflow: visible !important;
}

.chapter-nav-title {
    font-size: 0.9rem;
    font-weight: 700;
    color: #475569;
    display: flex;
    align-items: center;
    gap: 0.4rem;
    white-space: nowrap;
}

.chapter-nav-tabs {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    flex-wrap: wrap;
    overflow: visible !important;
}

.nav-tab-item {
    position: relative;
    display: inline-block;
    flex-shrink: 0;
}

/* Single Unified Pill Button */
.nav-tab-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.45rem 0.9rem;
    border-radius: 50px;
    font-size: 0.84rem;
    font-weight: 600;
    color: #334155;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    cursor: pointer;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    user-select: none;
    white-space: nowrap;
}

.nav-tab-pill:hover {
    background: #ffffff;
    color: var(--sj-p, #059669);
    border-color: #cbd5e1;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    transform: translateY(-1px);
}

.nav-tab-pill.active {
    background: linear-gradient(135deg, var(--sj-p, #059669), var(--sj-pd, #047857));
    color: #ffffff;
    border-color: transparent;
    font-weight: 700;
    box-shadow: 0 4px 14px rgba(5, 150, 105, 0.28);
}

.nav-tab-pill.unit-tab {
    background: #eff6ff;
    color: #1d4ed8;
    border-color: #bfdbfe;
}

.nav-tab-pill.unit-tab:hover {
    background: #dbeafe;
    color: #1e40af;
    border-color: #93c5fd;
}

.nav-tab-pill .chevron-icon {
    font-size: 0.7rem;
    opacity: 0.65;
    transition: transform 0.25s ease;
    margin-left: 2px;
}

.nav-tab-item.active-open .chevron-icon,
.nav-tab-item:hover .chevron-icon {
    transform: rotate(180deg);
    opacity: 1;
}

/* Floating Dropdown Card with Hover Bridge */
.nav-dropdown-card {
    display: none;
    position: absolute;
    top: calc(100% + 6px);
    left: 0;
    background: #ffffff;
    min-width: 240px;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    box-shadow: 0 16px 36px -4px rgba(15, 23, 42, 0.16), 0 4px 12px -2px rgba(15, 23, 42, 0.06);
    z-index: 9999;
    padding: 6px;
    animation: dropdownFadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1) both;
}

.nav-dropdown-card::before {
    content: '';
    position: absolute;
    top: -12px;
    left: 0;
    width: 100%;
    height: 12px;
    background: transparent;
}

@keyframes dropdownFadeIn {
    from {
        opacity: 0;
        transform: translateY(-8px) scale(0.97);
    }
    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.nav-tab-item.active-open .nav-dropdown-card,
.nav-tab-item:hover .nav-dropdown-card {
    display: block !important;
}

.nav-dropdown-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.55rem 0.85rem;
    border-radius: 8px;
    font-size: 0.82rem;
    color: #475569;
    font-weight: 550;
    transition: all 0.15s ease;
}

.nav-dropdown-item:hover {
    background: #f1f5f9;
    color: var(--sj-p, #059669);
}

/* MOBILE MODE (<768px): Floating Dock Bar */
.mobile-floating-dock {
    display: none;
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(15, 23, 42, 0.94);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 40px;
    padding: 0.5rem 0.8rem;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.3);
    z-index: 10001;
    align-items: center;
    gap: 0.35rem;
    width: max-content;
    max-width: 92vw;
}

.mobile-dock-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 52px;
    height: 42px;
    color: #94a3b8;
    border-radius: 20px;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: all 0.2s ease;
}

.mobile-dock-btn i {
    font-size: 1.1rem;
    margin-bottom: 2px;
}

.mobile-dock-btn span {
    font-size: 0.62rem;
    font-weight: 600;
}

.mobile-dock-btn.active {
    color: #ffffff;
    background: rgba(255, 255, 255, 0.12);
}

/* Mobile Drawer Overlay */
.dock-drawer-overlay {
    display: none;
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(4px);
    z-index: 10001;
}

.dock-drawer-overlay.active {
    display: block !important;
}

.dock-drawer-card {
    position: fixed;
    bottom: 20px;
    left: 15px;
    right: 15px;
    background: #ffffff;
    border-radius: 20px;
    padding: 1.2rem;
    box-shadow: 0 20px 40px rgba(15, 23, 42, 0.25);
    z-index: 10002;
    max-height: 70vh;
    overflow-y: auto;
    animation: drawerSlideUp 0.25s ease-out;
}

@keyframes drawerSlideUp {
    from { transform: translateY(100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.dock-drawer-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.8rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #e2e8f0;
    font-weight: 800;
    color: var(--sj-p, #059669);
}

.dock-drawer-close {
    background: #f1f5f9;
    border: none;
    width: 30px;
    height: 30px;
    border-radius: 50%;
    font-weight: 700;
    color: #64748b;
    cursor: pointer;
}

@media (max-width: 768px) {
    .chapter-nav-wrapper {
        display: none !important;
    }
    .mobile-floating-dock {
        display: flex !important;
    }
}
</style>
`;

// Sidebar Dock Javascript helper functions
const dockJsScript = `
<!-- DOCK SYSTEM NAVIGATION SCRIPTS -->
<script>
function toggleNavTabDropdown(button, event) {
    event.stopPropagation();
    var parent = button.closest('.nav-tab-item');
    var isOpen = parent.classList.contains('active-open');
    
    document.querySelectorAll('.nav-tab-item').forEach(function(item) {
        item.classList.remove('active-open');
    });
    
    if (!isOpen) {
        parent.classList.add('active-open');
    }
}

function openMobileDockDrawer(tabId, titleText) {
    var drawer = document.getElementById('dockDrawerOverlay');
    var contentBox = document.getElementById('dockDrawerContent');
    var titleBox = document.getElementById('dockDrawerTitle');
    var sourceCard = document.getElementById(tabId);
    
    if (drawer && contentBox && sourceCard) {
        titleBox.innerHTML = titleText;
        contentBox.innerHTML = sourceCard.innerHTML;
        drawer.classList.add('active');
    }
}

function closeMobileDockDrawer() {
    var drawer = document.getElementById('dockDrawerOverlay');
    if (drawer) {
        drawer.classList.remove('active');
    }
}

function switchTab(tabType, url, event) {
    if (event) {
        event.preventDefault();
        event.stopPropagation();
    }
    
    // 1. Update active tab pill state on desktop
    document.querySelectorAll('.nav-tab-pill').forEach(function(pill) {
        pill.classList.remove('active');
    });
    
    // Find the pill matching the tabType or from event target
    var targetPillClass = tabType + '-tab';
    if (tabType === 'pyqs') targetPillClass = 'pyq-tab';
    if (tabType === 'sheets') targetPillClass = 'sheet-tab';
    
    if (event && event.currentTarget) {
        var pill = event.currentTarget.closest('.nav-tab-item');
        if (pill) {
            var innerPill = pill.querySelector('.nav-tab-pill');
            if (innerPill) innerPill.classList.add('active');
        }
    } else {
        var pill = document.querySelector('.' + targetPillClass);
        if (pill) pill.classList.add('active');
    }
    
    // 2. Update active dock button state on mobile
    document.querySelectorAll('.mobile-dock-btn').forEach(function(btn) {
        btn.classList.remove('active');
        if (btn.getAttribute('onclick') && btn.getAttribute('onclick').indexOf(tabType) !== -1) {
            btn.classList.add('active');
        }
    });

    // Close mobile drawer
    closeMobileDockDrawer();

    // 3. Show/hide content panels
    var notesPanel = document.getElementById('notes-tab-content');
    var iframePanel = document.getElementById('iframe-tab-content');
    var iframe = document.getElementById('tab-iframe');

    if (tabType === 'notes') {
        if (iframePanel) iframePanel.style.display = 'none';
        if (notesPanel) notesPanel.style.display = 'block';
        if (iframe) iframe.src = '';
    } else {
        if (notesPanel) notesPanel.style.display = 'none';
        if (iframePanel) iframePanel.style.display = 'block';
        if (iframe && url) {
            iframe.src = url;
        }
    }
}

document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-tab-item')) {
        document.querySelectorAll('.nav-tab-item').forEach(function(item) {
            item.classList.remove('active-open');
        });
    }
});
</script>
`;

function processChapterFolder(classDir, notesFolder) {
  const notesIndexFile = path.join(classDir, 'chapter-wise-notes', notesFolder, 'index.html');
  if (!fs.existsSync(notesIndexFile)) {
    console.warn(`No index file found for ${classDir} -> ${notesFolder}`);
    return;
  }

  let content = fs.readFileSync(notesIndexFile, 'utf8');

  // Strip existing nav tags if present to prevent double injection
  content = content.replace(/<!-- DESKTOP FIXED TOP BAR [\s\S]*?<\/div>\s*<\/div>\s*<\/div>/, '');
  content = content.replace(/<!-- MOBILE FLOATING DOCK [\s\S]*?<\/div>/, '');
  content = content.replace(/<!-- Mobile Drawer Overlay [\s\S]*?<\/div>\s*<\/div>/, '');
  content = content.replace(/<!-- DOCK SYSTEM NAVIGATION STYLING -->[\s\S]*?<\/style>/, '');
  content = content.replace(/<!-- DOCK SYSTEM NAVIGATION SCRIPTS -->[\s\S]*?<\/script>/, '');
  content = content.replace('<!-- NOTES CONTENT START --><div id="notes-tab-content">', '');
  content = content.replace('</div><!-- NOTES CONTENT END -->', '');
  content = content.replace(/<!-- IFRAME TAB CONTAINER [\s\S]*?<\/div>/, '');

  // Strip Class 10 specific old bottom dock & overlay
  content = content.replace(/<!-- MOBILE FLOATING BOTTOM DOCK \([^\)]+\) -->[\s\S]*?<!-- MOBILE DOCK DRAWER OVERLAY -->[\s\S]*?<\/div>\s*<\/div>/, '');
  content = content.replace(/<div class="mobile-edge-dock"[\s\S]*?<!-- MOBILE DOCK DRAWER OVERLAY -->[\s\S]*?<\/div>\s*<\/div>/, '');

  console.log(`Processing chapter: ${classDir} -> ${notesFolder}`);

  // Determine equivalent folders in other resources
  let ncertFolder = notesFolder;
  let sheetFolder = notesFolder;
  let exemplarFolder = notesFolder;
  let testFolder = notesFolder;

  const mapping = folderMappings[classDir]?.[notesFolder];
  if (mapping) {
    if (mapping.ncert) ncertFolder = mapping.ncert;
    if (mapping.sheet) sheetFolder = mapping.sheet;
    if (mapping.exemplar) exemplarFolder = mapping.exemplar;
    if (mapping.test) testFolder = mapping.test;
  }

  // Chapter Number Extraction (from folder name)
  const chMatch = notesFolder.match(/chapter-(\d+)/);
  const chNum = chMatch ? chMatch[1] : '1';

  // 1. Scan NCERT Exercises
  let ncertDropdownHtml = `<a href="/${classDir}/ncert-exercise-practice/${ncertFolder}/" onclick="switchTab('ncert', '/${classDir}/ncert-exercise-practice/${ncertFolder}/', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-eye" style="color:var(--sj-p, #059669);"></i> Solutions Overview</a>`;
  const ncertPath = path.join(classDir, 'ncert-exercise-practice', ncertFolder);
  if (fs.existsSync(ncertPath)) {
    const files = fs.readdirSync(ncertPath).filter(f => f.startsWith('exercise-') && f.endsWith('.html')).sort();
    for (const f of files) {
      ncertDropdownHtml += `\n                <a href="/${classDir}/ncert-exercise-practice/${ncertFolder}/${f}" onclick="switchTab('ncert', '/${classDir}/ncert-exercise-practice/${ncertFolder}/${f}', event)" class="nav-dropdown-item"><i class="fas fa-list-ol" style="color:#059669;"></i> ${cleanExerciseName(f)}</a>`;
    }
  }

  // 2. Scan Worksheets
  let sheetDropdownHtml = '';
  if (classDir === 'class-12-maths') {
    sheetDropdownHtml = `<a href="#" class="nav-dropdown-item disabled" style="opacity:0.5; pointer-events:none;"><i class="fas fa-file" style="color:#2563eb;"></i> Coming Soon</a>`;
  } else {
    sheetDropdownHtml = `<a href="/${classDir}/worksheets/${sheetFolder}/standard.html" onclick="switchTab('sheets', '/${classDir}/worksheets/${sheetFolder}/standard.html', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-eye" style="color:var(--sj-p, #059669);"></i> Worksheets Home</a>`;
    const sheetPath = path.join(classDir, 'worksheets', sheetFolder);
    if (fs.existsSync(sheetPath)) {
      const files = fs.readdirSync(sheetPath).filter(f => f.endsWith('.html') && f !== 'index.html').sort();
      for (const f of files) {
        const name = f.replace('.html', '').toUpperCase();
        sheetDropdownHtml += `\n                <a href="/${classDir}/worksheets/${sheetFolder}/${f}" onclick="switchTab('sheets', '/${classDir}/worksheets/${sheetFolder}/${f}', event)" class="nav-dropdown-item"><i class="fas fa-file-contract" style="color:#2563eb;"></i> ${name} Sheet</a>`;
      }
    }
  }

  // 3. Scan Exemplar / PYQs
  let pyqDropdownHtml = '';
  if (classDir === 'class-12-maths') {
    pyqDropdownHtml = `<a href="/class-12-maths/previous-years-questions-chapter-wise/${exemplarFolder}/" onclick="switchTab('pyqs', '/class-12-maths/previous-years-questions-chapter-wise/${exemplarFolder}/', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-th-large" style="color:var(--sj-p, #059669);"></i> PYQs Portal</a>`;
    const pyqPath = path.join('class-12-maths', 'previous-years-questions-chapter-wise', exemplarFolder);
    if (fs.existsSync(pyqPath)) {
      const files = fs.readdirSync(pyqPath).filter(f => f.endsWith('.html') && f !== 'index.html').sort();
      for (const f of files) {
        const name = f.replace('.html', '').replace(/-/g, ' ').toUpperCase();
        pyqDropdownHtml += `\n                <a href="/class-12-maths/previous-years-questions-chapter-wise/${exemplarFolder}/${f}" onclick="switchTab('pyqs', '/class-12-maths/previous-years-questions-chapter-wise/${exemplarFolder}/${f}', event)" class="nav-dropdown-item"><i class="fas fa-tasks" style="color:#d97706;"></i> ${name}</a>`;
      }
    }
  } else {
    pyqDropdownHtml = `<a href="/${classDir}/ncert-exemplar-practice/${exemplarFolder}/" onclick="switchTab('pyqs', '/${classDir}/ncert-exemplar-practice/${exemplarFolder}/', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-th-large" style="color:var(--sj-p, #059669);"></i> Exemplar Portal</a>`;
    const exemplarPath = path.join(classDir, 'ncert-exemplar-practice', exemplarFolder);
    if (fs.existsSync(exemplarPath)) {
      const files = fs.readdirSync(exemplarPath).filter(f => f.endsWith('.html') && f !== 'index.html').sort();
      for (const f of files) {
        const name = f.replace('.html', '').replace(/-/g, ' ').toUpperCase();
        pyqDropdownHtml += `\n                <a href="/${classDir}/ncert-exemplar-practice/${exemplarFolder}/${f}" onclick="switchTab('pyqs', '/${classDir}/ncert-exemplar-practice/${exemplarFolder}/${f}', event)" class="nav-dropdown-item"><i class="fas fa-lightbulb" style="color:#d97706;"></i> ${name}</a>`;
      }
    }
  }

  // 4. Scan Chapter Test
  let testDropdownHtml = `<a href="/${classDir}/tests/chapter-wise/${testFolder}/test-1.html" onclick="switchTab('test', '/${classDir}/tests/chapter-wise/${testFolder}/test-1.html', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-vial" style="color:var(--sj-p, #059669);"></i> Start Test 1</a>`;
  const testPath = path.join(classDir, 'tests', 'chapter-wise', testFolder);
  if (fs.existsSync(testPath)) {
    const files = fs.readdirSync(testPath).filter(f => f.startsWith('test-') && f.endsWith('.html')).sort();
    if (files.length > 0) {
      testDropdownHtml = '';
      for (const f of files) {
        const name = f.replace('.html', '').toUpperCase();
        testDropdownHtml += `\n                <a href="/${classDir}/tests/chapter-wise/${testFolder}/${f}" onclick="switchTab('test', '/${classDir}/tests/chapter-wise/${testFolder}/${f}', event)" class="nav-dropdown-item"><i class="fas fa-check-circle" style="color:#dc2626;"></i> ${name}</a>`;
      }
    }
  }

  // Build Desktop Nav HTML
  const desktopNavHtml = `
<!-- DESKTOP FIXED TOP BAR (AUTO-INJECTED) -->
<div class="chapter-nav-wrapper">
    <div class="chapter-nav-container">
        <div class="chapter-nav-title">
            <i class="fas fa-layer-group" style="color: var(--sj-p, #059669);"></i> Resources
        </div>
        <div class="chapter-nav-tabs">

            <!-- 1. Notes Tab -->
            <div class="nav-tab-item">
                <div class="nav-tab-pill active notes-tab" onclick="switchTab('notes', '', event)">
                    <i class="fas fa-book-open"></i> 1. Notes <i class="fas fa-chevron-down chevron-icon" style="display:none;"></i>
                </div>
                <div class="nav-dropdown-card" id="src-notes">
                    <a href="/${classDir}/chapter-wise-notes/${notesFolder}/" onclick="switchTab('notes', '/${classDir}/chapter-wise-notes/${notesFolder}/', event)" class="nav-dropdown-item" style="background:#f8fafc; font-weight:700;"><i class="fas fa-home" style="color:var(--sj-p, #059669);"></i> Chapter Notes Home</a>
                </div>
            </div>

            <!-- 2. NCERT Solutions -->
            <div class="nav-tab-item">
                <div class="nav-tab-pill ncert-tab" onclick="toggleNavTabDropdown(this, event)">
                    <i class="fas fa-pen-nib"></i> 2. NCERT Solutions <i class="fas fa-chevron-down chevron-icon"></i>
                </div>
                <div class="nav-dropdown-card" id="src-ncert">
                    ${ncertDropdownHtml}
                </div>
            </div>

            <!-- 3. Worksheets -->
            <div class="nav-tab-item">
                <div class="nav-tab-pill sheet-tab ${classDir === 'class-12-maths' ? 'disabled' : ''}" onclick="${classDir === 'class-12-maths' ? 'return false' : 'toggleNavTabDropdown(this, event)'}">
                    <i class="fas fa-file-alt"></i> 3. Worksheets <i class="fas fa-chevron-down chevron-icon"></i>
                </div>
                <div class="nav-dropdown-card" id="src-sheets">
                    ${sheetDropdownHtml}
                </div>
            </div>

            <!-- 4. Exemplar / PYQs -->
            <div class="nav-tab-item">
                <div class="nav-tab-pill pyq-tab" onclick="toggleNavTabDropdown(this, event)">
                    <i class="fas fa-history"></i> 4. ${classDir === 'class-12-maths' ? 'Topic PYQs' : 'Exemplar'} <i class="fas fa-chevron-down chevron-icon"></i>
                </div>
                <div class="nav-dropdown-card" id="src-pyqs">
                    ${pyqDropdownHtml}
                </div>
            </div>

            <!-- 5. Chapter Test -->
            <div class="nav-tab-item">
                <div class="nav-tab-pill test-tab" onclick="toggleNavTabDropdown(this, event)">
                    <i class="fas fa-vial"></i> 5. Chapter Test <i class="fas fa-chevron-down chevron-icon"></i>
                </div>
                <div class="nav-dropdown-card" id="src-test">
                    ${testDropdownHtml}
                </div>
            </div>

        </div>
    </div>
</div>

<!-- MOBILE FLOATING DOCK BAR (AUTO-INJECTED) -->
<div class="mobile-floating-dock">
    <button class="mobile-dock-btn active" onclick="switchTab('notes', '', event)">
        <i class="fas fa-book-open"></i>
        <span>Notes</span>
    </button>
    <button class="mobile-dock-btn" onclick="openMobileDockDrawer('src-ncert', 'NCERT Solutions')">
        <i class="fas fa-pen-nib"></i>
        <span>NCERT</span>
    </button>
    <button class="mobile-dock-btn" onclick="${classDir === 'class-12-maths' ? 'return false' : 'openMobileDockDrawer(\'src-sheets\', \'Worksheets\')'}">
        <i class="fas fa-file-alt"></i>
        <span>Sheets</span>
    </button>
    <button class="mobile-dock-btn" onclick="openMobileDockDrawer('src-pyqs', '${classDir === 'class-12-maths' ? 'PYQs' : 'Exemplar'}')">
        <i class="fas fa-history"></i>
        <span>${classDir === 'class-12-maths' ? 'PYQs' : 'Exemplar'}</span>
    </button>
    <button class="mobile-dock-btn" onclick="openMobileDockDrawer('src-test', 'Chapter Test')">
        <i class="fas fa-vial"></i>
        <span>Test</span>
    </button>
</div>

<!-- Mobile Drawer Overlay Structure -->
<div class="dock-drawer-overlay" id="dockDrawerOverlay" onclick="closeMobileDockDrawer()">
    <div class="dock-drawer-card" onclick="event.stopPropagation()">
        <div class="dock-drawer-header">
            <span id="dockDrawerTitle">Resources</span>
            <button class="dock-drawer-close" onclick="closeMobileDockDrawer()">&times;</button>
        </div>
        <div id="dockDrawerContent" class="dock-drawer-body"></div>
    </div>
</div>

<!-- IFRAME TAB CONTAINER (AUTO-INJECTED) -->
<div id="iframe-tab-content" style="display: none; width: 100%; height: 90vh; border: none; margin: 0; padding: 0; overflow: hidden; background: #ffffff;">
    <iframe id="tab-iframe" src="" style="width: 100%; height: 100%; border: none;"></iframe>
</div>
`;

  // Inject Styles into </head>
  content = content.replace('</head>', `${dockStyle}\n</head>`);

  // Inject HTML markup into <body> right after header-container to render it in correct order (below site header)
  const headerIdx = content.indexOf('<div id="header-container"></div>');
  if (headerIdx !== -1) {
    const insertIdx = headerIdx + '<div id="header-container"></div>'.length;
    content = content.substring(0, insertIdx) + `\n${desktopNavHtml}` + content.substring(insertIdx);
  } else {
    const bodyStartIdx = content.indexOf('<body>');
    if (bodyStartIdx !== -1) {
      const insertIdx = bodyStartIdx + 6;
      content = content.substring(0, insertIdx) + `\n${desktopNavHtml}` + content.substring(insertIdx);
    }
  }

  // Wrap the rest of the original notes body inside <div id="notes-tab-content">
  const startMark = '<!-- IFRAME TAB CONTAINER (AUTO-INJECTED) -->';
  const startMarkIdx = content.indexOf(startMark);
  if (startMarkIdx !== -1) {
    const contentStartIdx = content.indexOf('</div>', startMarkIdx) + 6;
    const endMarkIdx = content.indexOf('<div class="nav-buttons-container"', contentStartIdx);
    if (endMarkIdx !== -1) {
      content = content.substring(0, contentStartIdx) +
                '\n<!-- NOTES CONTENT START --><div id="notes-tab-content">\n' +
                content.substring(contentStartIdx, endMarkIdx) +
                '\n</div><!-- NOTES CONTENT END -->\n' +
                content.substring(endMarkIdx);
    }
  }

  // Inject Script into bottom before </body>
  content = content.replace('</body>', `${dockJsScript}\n</body>`);

  fs.writeFileSync(notesIndexFile, content, 'utf8');
}

// Walk and upgrade all notes chapters
for (const classDir of classes) {
  const notesBase = path.join(classDir, 'chapter-wise-notes');
  if (!fs.existsSync(notesBase)) continue;
  
  const folders = fs.readdirSync(notesBase).filter(f => fs.statSync(path.join(notesBase, f)).isDirectory());
  for (const folder of folders) {
    processChapterFolder(classDir, folder);
  }
}

console.log('Successfully upgraded all chapter notes index pages!');

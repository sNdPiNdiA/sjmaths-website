# WebMCP Site Tools & Browser Omnibox Arrow Resolution

## 1. Root Cause Analysis

In the ChatGPT desktop app built-in browser (and Chromium with WebMCP flags/extensions):
1. **The Native Object Was Being Clobbered in `<head>`**:
   - The desktop app's built-in browser pre-injects a native `document.modelContext` / `navigator.modelContext` host bridge before scripts run.
   - The previous code ran `Object.defineProperty(document, 'modelContext', { value: defaultModelContext })` unconditionally, which wiped out the host browser's native C++/IPC bridge.
   - Because the native bridge was erased, the host browser never received any tool registration calls, so the browser omnibox action (the Gray Arrow for available Site Tools) never appeared.
2. **`registerTool` Was Never Executed on the Native Context**:
   - The previous initialization only populated an internal in-memory Map; it never invoked `document.modelContext.registerTool(...)` during page load.
3. **No Declarative HTML `<form>` Elements Existed**:
   - The W3C Declarative WebMCP specification defines `<form toolname="..." tooldescription="..." toolautosubmit>` for browser discovery. Without these in the DOM, the browser's declarative parser found 0 tools.
4. **The Root Homepage (`index.html` at `sjmaths.com`) Lacked WebMCP Metadata**:
   - The user navigated to `sjmaths.com`, where `index.html` had zero WebMCP scripts, meta tags, or tool definitions.

---

## 2. Changes Made

### A. Preserved Native `document.modelContext` & Registered All 13 Tools
- In `hackathon/webmcp/demo/index.html`:
  - Added detection of existing native `document.modelContext` or `navigator.modelContext`. If present, it is **never overwritten**.
  - Polyfill is only attached when native support is absent.
  - Automatically iterates over all 13 canonical tools and calls `target.registerTool(...)` with:
    - `name`, `description`, `inputSchema`
    - `annotations: { readOnlyHint: ..., untrustedContentHint: false }` (which signals to ChatGPT that tools like `get_curriculum_outline`, `get_topic_concepts`, etc. can run without prompting the user for destructive confirmations).
    - Standard MCP output format: `{ content: [{ type: 'text', text: ... }], result: ... }`.
  - Added listeners on `DOMContentLoaded`, `load`, and retry timeouts to catch late-injected desktop app preload scripts.
  - Dispatched standard `modelcontextready` and `toolchange` custom events.

### B. Added Declarative WebMCP HTML Forms
- In `hackathon/webmcp/demo/index.html` and `index.html`:
  - Injected hidden `<form toolname="..." tooldescription="..." toolautosubmit>` tags for all 13 curriculum tools.
  - Added form submission listeners supporting `e.respondWith(...)` for browser agents executing declarative forms.

### C. Site-Wide Availability on `sjmaths.com` (`index.html`)
- Created `hackathon/webmcp/src/webmcp-site-integration.js`:
  - Self-contained, lightweight runtime registering the 13 tools and lazy-loading the curriculum data on first call.
- Updated root `index.html`:
  - Added `<meta name="webmcp" content="ready">`, `<meta name="model-context" content="active">`, and `<link rel="model-context" ...>`.
  - Embedded `<script src="/hackathon/webmcp/src/webmcp-site-integration.js"></script>` in `<head>`.
  - Inserted the 13 declarative WebMCP forms in `<body>`.

### D. Parameter Flexibility in Tool Execution Engine
- Updated `hackathon/webmcp/src/webmcp-tools.js`:
  - Allowed `executeTool` to accept either `executeTool(name, params)` or object parameter dictionaries `executeTool({ name: '...', parameters: { ... } })`.

---

## 3. Comprehensive 404 & 301 URL Audit and Resolution

### A. Root Causes Identified
1. **Old WordPress/Spam Crawl URLs**: Legacy uploads and crawler attempts for `/wp-content/...` and `/images/...` are redirected safely to root (`/`).
2. **AHC RO/ARO `/hi/` Language Appending**: `ahc-ro-aro/index.html` and `ahc-ro-aro/syllabus/index.html` had a script that appended `/hi/` to all topic links, which was removed.
3. **UPSC Topic Renaming & Underscore URLs**: Older links and bookmarks to renamed subtopics (e.g. `Union-Executive-Legislature`, `First-Phase-of-National-Movement-1905-1917/Revolutionary-Activities-Abroad`, `Painted-Grey-Ware-PGW`) and underscore subject URLs (`modern_history`, `ancient_history`, etc.) lacked explicit, high-priority redirects.
4. **UPSC Tab Probing**: `upsc-renderer.js` probed all 9 tab JSON endpoints when `pageData.tabs` was undefined; this blind probing was removed.
5. **Class 10/11/12 PYQs & NCERT Exercises**: Trailing slashes on `.html` files and deep sub-paths now have comprehensive wildcard and `.html` normalization rules.

### B. 301 Audit Results
- **Total Unique URLs Checked**: 137
- **Direct 200 OK / Canonical Exists**: Verified
- **Redirects Resolving to Valid Endpoints (No 404s / No Broken Destinations)**: **137 / 137 (100% Pass)**

### C. Key Fixes Applied
1. **Rule Specificity Ordering in `_redirects`**:
   - Specific topic redirects (e.g. `/upsc/medieval_history/Mughal-Rule/The-Sur-Empire-1540-56/*`, `/upsc/modern_history/.../Revolutionary-Activities-Abroad/`) were placed **before** generic subject wildcards (`/upsc/medieval_history/*`).
   - Added both underscore (`modern_history`) and hyphen (`modern-history`) patterns to ensure direct 1-hop 301 resolution to canonical URLs.
2. **Canonical Topic Matching**:
   - `Mauryan-Empire/Sources-of-Information-Inscriptions/` $\rightarrow$ `Mauryan-Empire/Sources-of-Information/Inscriptions/`
   - `Mughal-Rule/The-Sur-Empire-1540-56/` $\rightarrow$ `Mughal-Rule/The-Sur-Empire/`
   - `Mughal-Rule/Aurangzeb-Marathas-and-the-Deccan-1687-1707/` $\rightarrow$ `Mughal-Rule/Aurangzeb-Marathas-and-the-Deccan/`
   - `Education-during-British-Rule/Administration-Central-Provincial-Local-Education/` $\rightarrow$ `Education-during-British-Rule/Administration-Central-Provincial-Local/`
   - `Pottery-Tradition/Painted-Grey-Ware-PGW/` $\rightarrow$ `Pottery-Tradition/Painted-Grey-Ware/`
   - `Visual-Arts/Post-Mauryan-Sculpture-Gandhara-Mathura-Amravati-School/` $\rightarrow$ `Visual-Arts/Post-Mauryan-Sculpture/`
   - `First-Phase-of-National-Movement-1905-1917/Revolutionary-Activities-Abroad/` $\rightarrow$ `First-Phase-of-National-Movement-1905-1917/Revolutionary-Activities/`
3. **Build & Bundle Validation**:
   - `node build.js` completed successfully. All CSS and JS bundles minified and version hashed (`Global Assets Hash: 74597047`).

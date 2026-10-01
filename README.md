# SJMaths - Master Mathematics

SJMaths is a comprehensive online learning platform designed for students from Class 9 to 12. It provides high-quality educational resources including NCERT solutions, chapter-wise notes, previous year questions (PYQs), and interactive quizzes.

## 🚀 Features

- **User Authentication**: Secure login/signup using Google via Firebase Auth.
- **Progressive Web App (PWA)**: Installable on mobile/desktop with offline support.
- **Responsive Design**: Optimized for all devices with a mobile-first approach.
- **Dark Mode**: System-aware dark theme with a manual toggle.
- **Dynamic Search**: Client-side search functionality for quick navigation.
- **Interactive Dashboard**: User profiles and personalized content access.
- **Automated Testing**: Custom scripts for security, link checking, and PWA validation.

## 📂 Project Structure

```text
sjmaths-website/
├── assets/              # Static assets (CSS, JS, Icons)
│   ├── css/             # Modular CSS files (main, layout, components)
│   ├── js/              # Core logic (auth, navigation, search)
│   └── icons/           # PWA icons
├── classes/             # Content pages for Class 9-12
├── components/          # Shared HTML fragments (header, footer)
├── pages/               # Static pages (About, Contact, Legal)
├── scripts/             # Maintenance & Test scripts (Node.js)
├── index.html           # Landing page
├── login.html           # Authentication page
├── service-worker.js    # PWA Service Worker
├── manifest.json        # PWA Manifest
└── firebase.json        # Firebase Hosting configuration
```

## 🛠️ Setup & Installation

### Prerequisites

- **Node.js** (for running test scripts)
- **Firebase CLI** (for deployment)
- A local web server (e.g., VS Code Live Server)

### Local Development

1.  **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/sjmaths-website.git
    cd sjmaths-website
    ```

2.  **Configure Firebase**
    - Create a project in the [Firebase Console](https://console.firebase.google.com/).
    - Enable **Authentication** (Google Provider).
    - Enable **Firestore Database**.
    - **Create the Configuration File**:
      Since `assets/js/firebase-config.js` is git-ignored for security, you must create it manually. Create the file and paste the following code, replacing the placeholders with your Firebase project keys:

      ```javascript
      // assets/js/firebase-config.js
      import {
        initializeApp,
        getApps,
        getApp,
      } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-app.js";
      import { getAuth } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-auth.js";
      import { getFirestore } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-firestore.js";
      import {
        getAnalytics,
        logEvent,
      } from "https://www.gstatic.com/firebasejs/12.8.0/firebase-analytics.js";

      export const firebaseConfig = {
        apiKey: "YOUR_API_KEY",
        authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
        projectId: "YOUR_PROJECT_ID",
        storageBucket: "YOUR_PROJECT_ID.firebasestorage.app",
        messagingSenderId: "YOUR_SENDER_ID",
        appId: "YOUR_APP_ID",
        measurementId: "YOUR_MEASUREMENT_ID",
      };

      const app = getApps().length ? getApp() : initializeApp(firebaseConfig);

      export const auth = getAuth(app);
      export const db = getFirestore(app);
      export const analytics = getAnalytics(app);
      export { logEvent };
      ```

3.  **Run Locally**
    - Since the project uses ES Modules (`type="module"`), you cannot open `index.html` directly from the file system.
    - Use a local server. If you have Python installed:
      ```bash
      python -m http.server 5500
      ```
    - Or use the **Live Server** extension in VS Code.

## 🧪 Testing

The project includes Node.js checks for SEO, runtime assumptions, and dependency security.

For preservation-first refactoring, see `REFACTOR_PLAN.md`. Run `npm run build:dry`
to compile and plan reference changes without writing files, `npm run build:test`
to exercise failed compilation and rollback, `npm run refactor:test` to check
asset extraction and generator output equivalence, and `npm run refactor:baseline` to
capture mobile/desktop browser evidence under ignored `scratch/refactor/`.
Asset builds prepare replacements before updating served files and retain old
outputs when compilation fails. `pages:build` builds the copied `.pages-dist`
artifact, so it does not rewrite source pages or minified assets in the checkout.

`npm run refactor:test:browser` exercises History's seven quiz question types,
keyboard tab activation, reset/retake, countdown expiry and submitted-timer cleanup.
It also checks an offline regenerated four-tab fixture without calling Gemini.
The UPSC check compares keyboard tabs, English/Hindi content and test submission
before/after style extraction, including the mobile study-footer overlap fix.
`node scripts/check-history-preservation.mjs --baseline=HEAD` compares every History
page against Git, allowing only the shared stylesheet/runtime tag replacements.
`node scripts/check-upsc-preservation.mjs --baseline=HEAD` similarly verifies the
UPSC HTML corpus, allowing only the exact shared-style and language-bootstrap
replacements. Browser comparisons use original asset fingerprints rather than
mutable HEAD fixtures, preserving current content and shared UI fixes after commits.
`scripts/benchmark-git-baseline.mjs` compares per-file Git reads with the shared
single-process reader. `scripts/inspect-screenshot-diffs.cjs before-label after-label`
provides read-only pixel evidence; it does not approve screenshot differences.
`node scripts/check-aso-preservation.mjs --baseline=HEAD` checks the ASO corpus
with the same exact-style policy. The ASO browser comparison covers keyboard
tabs, practice feedback, mini-test scoring, submitted-timer cleanup and mastery
storage. Read-only ASO maintenance commands are documented in
`scripts/aso/README.md`; legacy root commands remain compatible.

Chemistry's English generator and Hindi compiler now reuse pure modules in
`scripts/lib/chemistry-renderer.mjs` and `scripts/lib/chemistry-bilingual.mjs`.
Both language modes share `assets/js/chemistry-topic.js` at the original script
position. Frozen legacy fixtures support exact migration and translator hydration;
they are tooling inputs, not additional maintained browser runtimes.
`refactor:test` checks pre-move output hashes and complete question counts.
`refactor:test:browser` checks all five tabs, language/theme, quiz/PYQ feedback,
submission/retake and offline generated timer expiry without calling an API.
`node scripts/check-chemistry-preservation.mjs --baseline=41b8e41e51` verifies
all 718 pages; `node scripts/check-chemistry-authoring.mjs` separately proves
the original prompts, API/status orchestration and moved compiler bodies survive.
Those historical audits require the indicated Git commit; the fixture suites do not.
For a built artifact, set `SJ_REFACTOR_FIXTURE_ROOT=.pages-dist` when running
`node --test scripts/chemistry-browser.test.cjs`. Screenshot capture supports
`--filter=chemistry- --legacy-chemistry` to reconstruct the exact inline baseline
and clicks the actual local theme button for dark-mode evidence.

Agriculture uses importable `scripts/lib/agriculture-renderer.mjs` and
`scripts/lib/agriculture-redesign.mjs`. Its generator and legacy redesign batch
retain separate runtime variants because their selectors, feedback classes and
scroll offsets differ. `assets/js/agriculture-topic.js` serves 289 redesigned
pages; `agriculture-generated.js` preserves the generator's existing behaviour.
The migration command `node scripts/extract-agriculture-runtime.mjs` is read-only
unless `--apply` is supplied and never runs the content-changing redesign batch.
`node scripts/check-agriculture-preservation.mjs --baseline=41b8e41e51` checks
the complete 290-page corpus; `node scripts/check-agriculture-authoring.mjs`
proves the source move preserved prompts and orchestration. Both require that
historical commit. Offline fixture/hash tests and browser checks are included in
the refactor suites. For built pages, use `SJ_REFACTOR_FIXTURE_ROOT=.pages-dist`
with `node --test scripts/agriculture-browser.test.cjs`.

The exact five-tab controller used by English and Geography lives in
`assets/js/exam-topic.js`; both generators keep their independent prompts and
subject rendering. The English compiler is importable from
`scripts/lib/english-compiler.mjs`. `node scripts/extract-exam-topic-runtime.mjs`
performs a dry run; add `--apply` to replace matching scripts across both families.
`node scripts/check-exam-topic-preservation.mjs --baseline=41b8e41e51` covers
all English and Geography HTML. `node scripts/check-exam-topic-authoring.mjs`
proves the source migration retained generator and compiler bodies. Browser and
fixture hash checks are part of the `refactor:test` suites. For minified built
pages set `SJ_REFACTOR_FIXTURE_ROOT=.pages-dist` when running
`node --test scripts/exam-topic-browser.test.cjs`.

The ASO topic feedback and five-tab controllers are shared as
`assets/js/aso-topic-feedback.js` and `assets/js/aso-topic-tabs.js`.
`node scripts/extract-aso-topic-runtimes.mjs` previews the exact-only 94-page
replacement; use `--apply` to write it. `node scripts/check-aso-topic-preservation.mjs`
allows only those two exact classic-script replacements. Their fingerprinted
sources can be restored for fixtures through `scripts/lib/aso-topic-runtime.mjs`;
browser parity checks cover the mega-test and a standard structures topic at
mobile and desktop widths.

The Hindi topic-page controller is shared as `assets/js/hindi-topic.js` and
remains owned by `scripts/generate_hindi.mjs`. Use
`node scripts/extract-hindi-topic-runtime.mjs` for a dry run and add `--apply`
to migrate only the 102 pages matching the generator fingerprint; six Hindi
page variants remain untouched. `node scripts/check-hindi-topic-preservation.mjs`
checks the Hindi pages against Git after allowing only the exact runtime
replacement. Browser parity covers tabs, quiz, PYQ, theme and timed-test flows.

The Hindi Music Vocal topic controller is shared as
`assets/js/music-vocal-topic.js` and remains owned by
`scripts/generate_music_vocal_hi.mjs`. Use
`node scripts/extract-music-vocal-runtime.mjs` for a dry run and `--apply` to
migrate only the 201 pages matching its exact fingerprint. The preservation
check allows only this controller replacement; browser parity covers the four
tabs, MCQ/fill-in/short-answer feedback, manual and timed test submission, and
mobile/desktop widths.

The Hindi Music Instrumental topic controller is shared as
`assets/js/music-instrumental-topic.js` and remains owned by
`scripts/generate_music_instrumental_hi.mjs`. Use
`node scripts/extract-music-instrumental-runtime.mjs` for a dry run and
`--apply` to migrate only the 125 pages matching its legacy fingerprint. The
shared controller also makes quiz and test feedback visible using the existing
`.quiz-feedback.show` style; preservation and browser checks cover the four
tabs, MCQ/fill-in/short-answer feedback, theme, manual and timed test, and
mobile/desktop widths.

1.  **Run the complete release gate**

    ```bash
    npm test
    ```

    This runs JavaScript syntax checks, security regression tests, SEO regression tests, the repository-wide SEO and accessibility audits, and the production dependency audit.

2.  **Run the SEO regression suite only**

    ```bash
    npm run seo:test
    ```

3.  **Audit page metadata and local references**

    ```bash
    npm run seo:audit
    ```

4.  **Audit rendered HTML accessibility semantics**

    ```bash
    npm run a11y:audit
    ```

5.  **Run browser/runtime smoke checks**

    ```bash
    npm run seo:test:browser
    ```

    By default this uses local repository fixtures while exercising representative routes at mobile and desktop viewports. Set `SEO_TEST_BASE=https://sjmaths.com` to run the same checks against the live site.

6.  **Scan production dependencies**

    ```bash
    npm audit --omit=dev
    ```

7.  **Verify production runtime JSON dependencies**

    ```bash
    npm run seo:test:hosting:runtime
    ```

    This checks that question-bank and exemplar JSON files referenced by published pages are reachable from the live host.

For browser/runtime checks, serve the repository locally and open the affected routes in a browser; static checks do not replace interactive verification.

## 📦 Deployment

The production site is deployed through **Cloudflare Pages**. The repository also retains `firebase.json` for Firebase Hosting workflows.

### Cloudflare Pages

Use the following build settings:

- **Build command:** `npm run pages:build`
- **Output directory:** `.pages-dist`

The build command writes a pruned deployment artifact to `.pages-dist` while leaving the source checkout intact. It runs the asset build, preserves JSON files referenced by runtime pages, prunes generator data, and fails if the staged artifact is missing a runtime dependency, contains development-only directories, or exceeds the file limit. After deployment, verify the result with:

```bash
npm run seo:test:hosting:runtime
npm run seo:test:hosting
```

Both commands must pass before considering the release verified.

To inspect the preservation set without modifying the checkout, run `npm run pages:build:dry`. The staged build itself is intended for the Cloudflare build environment; it removes only the disposable `.pages-dist` directory before recreating it.

To verify an existing staged artifact without rebuilding it, run `npm run pages:verify`.

To deploy the verified artifact, authenticate Wrangler with `wrangler login`, set `CF_PAGES_PROJECT` to the existing Cloudflare Pages project name, and run `npm run pages:deploy`. The command verifies the artifact and Wrangler session before uploading it.

### Firebase Hosting

1.  **Login to Firebase**

    ```bash
    firebase login
    ```

2.  **Initialize (if not already done)**

    ```bash
    firebase init hosting
    ```

    - Select your project.
    - Public directory: `.` (current directory) or specific build folder.
    - Configure as a single-page app: `No` (since this is a multi-page site).

3.  **Deploy**
    ```bash
    firebase deploy
    ```

## 📄 License

Distributed under the MIT License.

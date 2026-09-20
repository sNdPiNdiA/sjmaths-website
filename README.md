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

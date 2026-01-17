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
    - Update `assets/js/firebase-config.js` with your project keys.

3.  **Run Locally**
    - Since the project uses ES Modules (`type="module"`), you cannot open `index.html` directly from the file system.
    - Use a local server. If you have Python installed:
      ```bash
      python -m http.server 5500
      ```
    - Or use the **Live Server** extension in VS Code.

## 🧪 Testing

The project includes custom Node.js scripts to ensure quality and security.

1.  **Run the Test Suite** (File structure, Syntax, PWA check)

    ```bash
    node scripts/test-runner.js
    ```

2.  **Security Scan** (Check for exposed secrets & vulnerabilities)

    ```bash
    node scripts/security-check.js
    ```

3.  **Link Checker** (Verify internal links)
    ```bash
    node scripts/check-links.js
    ```

## 📦 Deployment

This project is configured for **Firebase Hosting**.

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

# Pre-Launch Checklist Report

This report summarizes the findings from the pre-launch check of the website.

## 1. Security Vulnerabilities

### High Priority

- **Hardcoded API Key in `assets/js/auth.js`**
  - **File:** `assets/js/auth.js`
  - **Issue:** A Firebase API key is hardcoded directly into the javascript file. This is a critical security risk and should be addressed immediately. The key should be stored in a secure backend environment and accessed via API calls, not exposed on the client-side.
  - **Line with key:** `apiKey: "AIzaSyA0kGONQMQ3NBLfnOuDPTPN_tGCqM-ed2M"`

## 2. Broken Links

The following links were found to be broken, leading to "File not found" errors. These should be fixed to prevent user frustration and improve SEO.

| Linking File | Broken Link |
| :--- | :--- |
| `utils/loadFooter.js` | `/pages/sample-papers.html` |
| `utils/loadFooter.js` | `/pages/previous-years.html` |
| `utils/loadFooter.js` | `/pages/formulas.html` |
| `assets/js/search-index.json` | `/classes/class-12/sample-papers/set1/index.html`|

## 3. Empty or Incomplete Pages

- **Empty File:** `maths-mastery/calculus/index.html`
  - **Issue:** This file is currently empty. If this feature is not ready, the link to it should be removed to avoid leading users to a blank page.

## Recommendations

1.  **Immediately** remove the hardcoded API key from `assets/js/auth.js` and implement a secure way to handle authentication.
2.  Fix the broken links listed above by either creating the missing pages or removing the links to them.
3.  Address the empty file by either adding content or removing the link to it.
4.  A full, automated link-check should be performed on the entire site. The current manual check was not exhaustive. The `scripts/check-links.js` script in the project seems to be designed for this purpose.
5.  Other "pre-launch" checks like HTML/CSS validation, performance testing, and accessibility checks should be performed. The `package.json` file lists scripts for some of these (`validate:html`, `validate:css`, `lighthouse`).


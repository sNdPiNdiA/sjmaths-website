# Reusable Exercise CSS Implementation Guide

## Created Files

### 1. `/assets/css/exercise-shared.css`

**Contains:** Hero section, navigation buttons, dark mode toggle, floating controls, smooth scroll behavior, animations

**Includes:**

- Color variables (root & dark-mode)
- Global reset & scroll behavior
- Header styling
- Hero section with gradient
- Bottom navigation buttons (.nav-btn, .btn-prev, .btn-next)
- Floating controls (.floating-controls, .back-btn-floating, .theme-toggle-btn)
- Animations (fadeIn, slideDown)
- Mobile responsive breakpoints (768px, 640px)

### 2. `/assets/css/footer.css`

**Contains:** Minimal footer styling

**Includes:**

- .page-footer
- .footer-content
- .footer-bottom
- Dark mode support

## How to Apply to Other Exercises

### Step 1: Add External CSS Links

In the `<head>` section, add after Font Awesome:

```html
<link rel="stylesheet" href="/assets/css/exercise-shared.css" />
<link rel="stylesheet" href="/assets/css/footer.css" />
```

### Step 2: Keep Only Page-Specific Styles in `<style>` Tag

Replace the entire `<style>` block with ONLY page-specific CSS:

- .container
- .section
- .quick-nav
- .formula-box
- .solution-btn
- .solution

**Remove from inline styles:**

- :root variables (use shared)
- Header/logo/navbar styles (use shared)
- Hero section (use shared)
- .btn/.btn-light/.btn-outline (use shared)
- .bottom-nav/.nav-btn/.btn-prev/.btn-next (use shared)
- .floating-controls/.back-btn-floating/.theme-toggle-btn (use shared)
- Dark mode variables (use shared)
- Animations (use shared)

### Step 3: Update HTML Structure

Ensure footer matches this pattern:

```html
<!-- Bottom Navigation -->
<div class="bottom-nav">
  <a href="../index.html" class="nav-btn btn-prev">← Previous</a>
  <a href="./exercise-X.Y.html" class="nav-btn btn-next">Next →</a>
</div>

<!-- Footer -->
<footer class="page-footer">
  <div class="footer-content">
    <a href="/">Home</a>
    <a href="/pages/contact.html">Contact</a>
    <a href="/pages/privacy-policy.html">Privacy</a>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 SJMaths</p>
  </div>
</footer>

<!-- Floating Controls -->
<div class="floating-controls">
  <a href="/classes/class-10/" class="back-btn-floating">
    <i class="fas fa-arrow-left"></i> Back to Class
  </a>
  <button
    class="theme-toggle-btn"
    onclick="toggleTheme()"
    aria-label="Toggle Dark Mode"
  >
    <i class="fas fa-moon"></i>
  </button>
</div>

<!-- Scripts -->
<script>
  function toggleTheme() {
    document.body.classList.toggle("dark-mode");
    const icon = document.querySelector(".theme-toggle-btn i");
    if (document.body.classList.contains("dark-mode")) {
      icon.classList.remove("fa-moon");
      icon.classList.add("fa-sun");
      localStorage.setItem("theme", "dark");
    } else {
      icon.classList.remove("fa-sun");
      icon.classList.add("fa-moon");
      localStorage.setItem("theme", "light");
    }
  }

  // Check saved theme
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    document
      .querySelector(".theme-toggle-btn i")
      .classList.replace("fa-moon", "fa-sun");
  }
</script>
```

## Features Provided by Shared CSS

### 🎨 Hero Section

- Gradient background (purple to accent)
- Responsive typography
- Button styles (.btn-light, .btn-outline)
- Hover effects

### 🌙 Dark Mode

- Full dark mode support
- Smooth transitions
- All components included

### ⌨️ Accessibility

- Keyboard focus states on all interactive elements
- Outline indicators (3px solid)
- ARIA labels supported

### 📱 Responsive Design

- 768px breakpoint (tablet)
- 640px breakpoint (mobile)
- Floating controls repositioning on small screens
- Button text sizing adjustments

### ✨ Animations

- fadeIn (0.6s on page load)
- slideDown (0.3s on solution reveal)
- Smooth scroll behavior
- Hover transitions

### 🔘 Navigation Elements

- Bottom navigation buttons (prev/next)
- Floating back button & dark mode toggle
- Sticky positioning
- Glass-morphism effect

## Supported Across All Classes

- ✅ Class 9
- ✅ Class 10
- ✅ Class 11
- ✅ Class 12

## Color Customization

To customize colors for different classes, modify CSS variable overrides in the page's `<style>` tag:

```css
:root {
  --primary: #0d9488; /* Teal for Class 12 */
  --accent: #0f766e;
  /* ...other variables */
}
```

The shared CSS will automatically use the updated variables.

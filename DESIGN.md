# SJMaths interface design contract

This file is the source of truth for new and maintained UI work. Existing educational content and subject-specific illustrations may retain their own semantic accent, but shared navigation, controls, cards, forms, states and responsive behavior use these tokens.

## Principles

- Calm, readable study surfaces with one clear action per section.
- Emerald is the primary action color; amber is reserved for emphasis and examination focus.
- Ink and slate provide the type hierarchy. Decorative color never carries meaning alone.
- Content stays readable when browser text is enlarged. Components may grow vertically; they must not force page-level horizontal scrolling.
- Every interactive control has visible focus, hover, pressed and disabled feedback.
- Motion is short and useful. `prefers-reduced-motion` disables non-essential transitions.

## Tokens

```css
--sj-color-primary: #0f766e;
--sj-color-primary-strong: #115e59;
--sj-color-primary-soft: #ccfbf1;
--sj-color-accent: #b45309;
--sj-color-accent-soft: #ffedd5;
--sj-color-ink: #172033;
--sj-color-muted: #526174;
--sj-color-surface: #ffffff;
--sj-color-surface-subtle: #f5f8f8;
--sj-color-page: #eef3f3;
--sj-color-border: #d7e1e1;
--sj-color-success: #15803d;
--sj-color-success-soft: #dcfce7;
--sj-color-danger: #b91c1c;
--sj-color-danger-soft: #fee2e2;
--sj-color-focus: #0e7490;

--sj-font-body: Inter, system-ui, -apple-system, "Segoe UI", sans-serif;
--sj-font-display: Outfit, Inter, system-ui, sans-serif;
--sj-text-xs: 0.75rem;
--sj-text-sm: 0.875rem;
--sj-text-md: 1rem;
--sj-text-lg: 1.25rem;
--sj-text-xl: clamp(1.75rem, 4vw, 2.75rem);
--sj-leading-body: 1.6;
--sj-leading-tight: 1.2;

--sj-space-1: 0.25rem;
--sj-space-2: 0.5rem;
--sj-space-3: 0.75rem;
--sj-space-4: 1rem;
--sj-space-5: 1.5rem;
--sj-space-6: 2rem;
--sj-space-7: 3rem;

--sj-radius-sm: 0.5rem;
--sj-radius-md: 0.75rem;
--sj-radius-lg: 1rem;
--sj-radius-pill: 999px;
--sj-shadow-sm: 0 1px 3px rgb(23 32 51 / 0.08);
--sj-shadow-md: 0 10px 24px rgb(23 32 51 / 0.10);
--sj-motion-fast: 160ms ease;
--sj-motion-standard: 240ms cubic-bezier(0.16, 1, 0.3, 1);
```

In dark mode, `:root[data-theme="dark"]` overrides only the semantic color and shadow tokens: primary `#5eead4` / strong `#99f6e4` / soft `#123b36`; accent `#fbbf24` / soft `#3a2b14`; ink `#f1f5f9`; muted `#b2bfcc`; surface `#182635`; subtle surface `#203141`; page `#101a27`; border `#3b4b5c`; success `#4ade80` / soft `#173725`; danger `#fca5a5` / soft `#3b2228`; focus `#67e8f9`. Dark shadows use black at 28% (`--sj-shadow-sm`) and 34% (`--sj-shadow-md`).

## Universal color theme contract

### Preference and resolved theme

- The single preference is stored in `localStorage["sjmaths.theme.preference"]` and may be `system`, `light`, or `dark`.
- A first-time visitor uses `system`. In that mode, the active theme follows `prefers-color-scheme` and updates when the operating-system preference changes. Explicit light/dark choices persist across pages and visits.
- `html[data-theme="light"]` or `html[data-theme="dark"]` represents the resolved appearance. `html[data-theme-preference]` represents the saved preference, including `system`.
- CSS consumes semantic tokens for page, surface, text, muted text, borders, focus, and status colors. Brand identity and educational meaning remain intact; images, diagrams, and state colors are not globally inverted.
- During migration only, the shared controller may mirror the resolved theme to legacy `html.dark-mode` / `body.dark-mode` classes for styles that have not yet moved to tokens. Those classes are compatibility output, never an independent state source.
- Set the document `color-scheme` to the resolved theme so browser-provided controls match. Avoid animated transitions on initial paint; later transitions must respect `prefers-reduced-motion`.

### Controller and controls

- The shared `window.SJMathsTheme` API exposes `getPreference()`, `getResolvedTheme()`, `setPreference('system' | 'light' | 'dark')`, and `toggle()`. Legacy `window.isDarkMode`, `window.setDarkMode(boolean)`, and `window.toggleDarkMode()` remain compatibility wrappers during migration.
- The namespaced event is `sjmaths:themechange`, with both the preference and resolved theme in its detail. During rollout, the controller may emit the existing `themeChanged` event as a compatibility bridge.
- A two-state toggle changes `system` to the opposite of the currently resolved appearance. A settings control may additionally offer all three choices: System, Light, and Dark.
- A toggle's accessible name describes the action it will take; its pressed state reflects whether the resolved theme is dark. Reuse a page's existing toggle and do not inject a second global toggle when one is already present.

### One-time legacy preference migration

If the canonical key is absent or invalid, migrate the first recognized legacy value using this deterministic precedence:

1. `sjmaths-dark`: `on` → `dark`, `off` → `light`.
2. `sjmaths_theme`: `dark` / `light`.
3. `sj_theme`: `dark` / `light`.
4. `theme`: `dark` / `light`.
5. `sjmaths-test-dark`: `true` → `dark`, `false` → `light`.
6. `sjmaths-theme`: accept only the exact values `dark` / `light`, and only as a last resort.

The `sjmaths-theme` key is also used for named color palettes (for example `green`, `blue`, `purple`, and `orange`); palette values are not dark-mode preferences and must be left untouched. Once a valid legacy choice is migrated, write the canonical key and make it authoritative. Conflicting legacy values resolve by the precedence above because their write times cannot be reliably inferred. New theme code must never use legacy keys as its source of truth; any temporary compatibility writes are limited to keys confirmed to represent light/dark mode and are removed after all page families migrate.

### Rollout guardrails

- Update page-family templates, generators, and source assets before regenerating their HTML or minified bundles. Do not mass-rewrite generated pages independently of their source.
- Preserve the existing authentication overlay and educational-content behavior while theme state changes.
- Verify first paint, system changes, explicit preference persistence, route changes, cross-tab updates, keyboard use, text enlargement, contrast, and responsive layouts in each migrated page family before removing its legacy selectors.

## Component rules

- Primary buttons use `--sj-color-primary`, `--sj-radius-md`, a minimum height of 44px, and a 12px/16px horizontal padding rhythm.
- Secondary buttons use a surface background and `--sj-color-border`; they retain the same height, type weight and radius as primary buttons.
- Cards use `--sj-color-surface`, a 1px border, `--sj-radius-lg` and `--sj-shadow-sm`. Use emphasis through a border or accent strip, not extra gradients.
- Inputs use the same radius and border as cards, a minimum 44px height, and place validation text immediately after the invalid field.
- Modal, dropdown and tab changes use opacity/transform transitions and remain usable without motion.
- Mobile navigation is collapsed behind a labelled 44px menu button. Tab labels wrap into a two-column grid instead of creating page-level sideways scrolling.

## Page contract

Every indexable page should have one descriptive title, one useful description, a favicon, one primary action, semantic landmarks, and a one-line explanation of the page's value. Unavailable content uses an explicit empty state with a useful next link; it does not use filler such as “coming soon” or “being updated”.

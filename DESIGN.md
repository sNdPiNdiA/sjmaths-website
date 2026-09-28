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

## Component rules

- Primary buttons use `--sj-color-primary`, `--sj-radius-md`, a minimum height of 44px, and a 12px/16px horizontal padding rhythm.
- Secondary buttons use a surface background and `--sj-color-border`; they retain the same height, type weight and radius as primary buttons.
- Cards use `--sj-color-surface`, a 1px border, `--sj-radius-lg` and `--sj-shadow-sm`. Use emphasis through a border or accent strip, not extra gradients.
- Inputs use the same radius and border as cards, a minimum 44px height, and place validation text immediately after the invalid field.
- Modal, dropdown and tab changes use opacity/transform transitions and remain usable without motion.
- Mobile navigation is collapsed behind a labelled 44px menu button. Tab labels wrap into a two-column grid instead of creating page-level sideways scrolling.

## Page contract

Every indexable page should have one descriptive title, one useful description, a favicon, one primary action, semantic landmarks, and a one-line explanation of the page's value. Unavailable content uses an explicit empty state with a useful next link; it does not use filler such as “coming soon” or “being updated”.

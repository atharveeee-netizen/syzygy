# OpenDesign Contract (Design.md)
## Project SYZYGY: Master Visual Language & Anti-AI Slop Specifications

---

### 1. The OpenDesign Standard
OpenDesign acts as an immutable design system contract between autonomous AI agents and user interfaces. It prevents agents from falling back to generic, unstyled browser defaults or low-contrast AI slop.

---

### 2. Design Tokens

```css
:root {
  /* Surface Tokens */
  --bg-primary: #090d16;        /* Deep Space Obsidian */
  --bg-card: #0f172a;           /* Slate 900 Surface */
  --bg-hover: #1e293b;          /* Slate 800 Interactive */
  
  /* Border Tokens */
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-accent: rgba(99, 102, 241, 0.35);

  /* Typography Tokens */
  --text-primary: #f8fafc;      /* Pure slate text */
  --text-muted: #94a3b8;        /* Slate 400 metadata */
  --accent-primary: #6366f1;    /* Indigo 500 */
}
```

---

### 3. Typography & Spacing
- **Title Font:** `Outfit`, sans-serif (Weights: 600, 700)
- **Body Font:** `Inter`, sans-serif (Weights: 400, 500)
- **Code Font:** `JetBrains Mono`, monospace (Weight: 500)
- **Base Spacing Grid:** 8-pixel standard (`8px`, `16px`, `24px`, `32px`, `48px`)

---

### 4. Motion Physics (Motion Division Standard)
- **Spring Physics:** `stiffness: 350, damping: 28, mass: 0.8`
- **Transitions:** `cubic-bezier(0.16, 1, 0.3, 1)`
- **Hover Micro-Interactions:** `scale: 1.02`, `duration: 150ms`

# SYZYGY Canonical Technical Image Generation Harness

> **MANDATORY SPECIFICATION FOR ALL TECHNICAL FIGURE, DIAGRAM, AND SCHEMATIC GENERATION IN SYZYGY.**
> Every image generated across any project in this workspace MUST strictly follow this harness.

---

## 1. The Core Technology Harness

1. **Generation Engine:** Google DeepMind **Imagen 3** (`gemini-3.1-flash-image` via Antigravity native `generate_image` tool).
2. **Latent Conditioning (`ImagePaths`):** Pass an existing verified hardware/architecture schematic (e.g. `docs/figures/hardware_wiring_architecture.png`) into `ImagePaths` to condition the model on exact stroke weight, font scale, chip pinout aesthetics, and pastel technical fills.
3. **Deterministic Hybrid Overlays (Python PIL / Matplotlib):** Used for real simulation data (ANSYS, MATLAB, FEA/CFD) and metric gauges. Never allow AI to hallucinate simulation curves or data plots.

---

## 2. The 5 Invariant Engineering Principles

### Principle 1: Pure Paper-White Canvas (`#ffffff`)
- Every prompt MUST explicitly declare: `pure white background (#ffffff)` or `pure white canvas (#ffffff)`.
- Eliminates dark-mode glowing grids, cyberpunk neon lens flares, and muddy gradients.
- Matches IEEE Transactions, ACM, and Nature publication standards.

### Principle 2: Physical BOM Silicon Anchoring
- NEVER use generic terms like *"sensor"*, *"processor"*, or *"cloud"*.
- ALWAYS explicitly enumerate the exact physical silicon part numbers, interfaces, and pinouts:
  - Microcontrollers: `nRF52840 ARM Cortex-M4F @ 64MHz`, `ESP32-S3 Dual-Core Xtensa`
  - Transceivers: `SX1262 LoRa Sub-GHz RF (+14 dBm)`, `SX1302 8-channel Gateway HAT`
  - Transducers: `Dual SHT40 Temp/RH`, `Knowles I2S SPH0645LM4H MEMS Microphone`
  - Power: `3.6V 8500mAh Li-SOCl2 primary cell ER34615`, `20W Monocrystalline PV + 12V LiFePO4`
  - Edge Compute: `Raspberry Pi 3B+ Single Board Computer`

### Principle 3: Strict Zero-Text-Wall Enforcement
- Every prompt MUST explicitly mandate:
  `Strictly pictorial schematic and flowchart format. Absolutely NO paragraphs and NO bullet point lists.`
- Forbid bullet points, block summaries, and narrative paragraphs inside the image.
- Information must be encoded into:
  - **Component blocks** with pin/bus callouts (I2S DMA, I2C, SPI, UART).
  - **Directional signal paths** with quantitative tags (e.g., `4.2 km LoRa RF beam`, `16 kHz audio DMA`).
  - **Structured binary packet layouts** (e.g., `[Header 4B | FFT Energy 6B | Temp 4B | AES-MAC 8B]`).
  - **Micro-flowcharts** with math expressions (e.g., $S_i = \max(0, S_{i-1} + y_i - \mu_0 - k)$).

### Principle 4: Instrument Dials, Gauges & Scorecard Strips
- When displaying KPIs, performance, or competitive comparisons:
  - Use **circular dial gauges**, **linear thermometer bars**, **oscilloscope waves**, and **progress rings**.
  - Always pair target with achieved: `Target: < ±0.2°C | Achieved: ±0.1°C`.
  - Include verified status badges: `[PASS]` in crisp green `#22c55e`.
  - For competitive analysis, use a horizontal **Visual Scorecard Strip** with bold checkmarks ($\checkmark$) and crosses ($\times$) across physical capabilities.

### Principle 5: Deterministic Multiphysics Verification
- Simulation plots (ANSYS HFSS $S_{11}$, Icepak thermal CFD, Drop Shock dynamic stress, Fluent aerodynamics) MUST be composited from actual simulation runs using Python PIL/Matplotlib.
- Zero AI hallucination on stress contours, return loss curves, or eye diagrams.

---

## 3. Standard Canonical Prompt Template

```text
High-resolution technical engineering [diagram type: flowchart / schematic / comparison / dashboard] for [System Name] on pure white background (#ffffff). Modern clean IEEE engineering publication style with crisp black linework, pastel [cyan / blue / green / gray] functional blocks, component illustrations, circuit chips, waveforms, and directional data arrows. Absolutely NO paragraphs and NO bullet point lists.

[Section 1: Physical Component Layer]
- Explicit silicon part numbers, pinouts, and physical placement.

[Section 2: Processing & Data Pipeline Flowchart]
- Math formulas, latency tags, and memory footprint.

[Section 3: Telemetry & RF Waveforms]
- Link budget, frequency, range, and structured packet divisions.

[Section 4: Instrumentation Dials & Verification Badges]
- Circular gauges, target vs achieved readings, and green [PASS] verification badges.

Style: Clean technical IEEE whitepaper graphic, pure white canvas (#ffffff), dark technical lines, sharp vector iconography, zero decorative AI slop, zero text paragraphs, zero bullet lists.
```

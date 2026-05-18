# THESIS FIGURE GENERATION PLAN — Publication-Grade Visualizations

**Date:** May 4, 2026  
**Purpose:** Master plan for all publication-grade figures following `visualizations_protocol.md`  
**Status:** Ready to execute

---

## 1. Overall Strategy

We will generate **two sets of figures**:

| Set | Purpose | Location | Format |
|-----|---------|----------|--------|
| **Thesis Set** | High-quality figures for the final thesis PDF | `thesis_markdown/chapters/figures/` | PDF (300 DPI) |
| **Chapter-Specific Sets** | Figures embedded in each chapter's knowledge base | `chapters/[chapter]/figures/` | PDF + PNG previews |

All figures must strictly follow `visualizations_protocol.md`:
- 300 DPI minimum
- PDF vector format preferred
- Colorblind-safe palette (from protocol)
- Clear, readable fonts (minimum 9–10 pt)
- Professional captions with Devanagari where relevant

---

## 2. Recommended Figures by Chapter

### Chapter 3: Dataset Description (Already Partially Done)

| Figure | Title | Type | Priority | Status |
|--------|-------|------|----------|--------|
| Figure 3.1 | Entity Type Distribution (Mahānāma) | Pie/Donut | High | Needs regeneration |
| Figure 3.2 | Sentence Length Distribution (Mahānāma vs Pañcatantra) | Histogram | Medium | Pending |
| Figure 3.3 | Entity Density Comparison | Bar | Medium | Pending |

**Action:** Regenerate using the improved protocol (colorblind-safe, proper fonts, Devanagari labels if needed).

---

### Chapter 4: Methodology (Already Generated — 5 Figures)

| Figure | Title | Type | Status |
|--------|-------|------|--------|
| Figure 4.1 | DCS Sembank NER Extraction Pipeline (3 Attempts) | Flowchart | ✅ Done |
| Figure 4.2 | Training Strategy Evolution (Best NER → Final NER) | Diagram | ✅ Done |
| Figure 4.3 | QLoRA Architecture | Architecture | ✅ Done |
| Figure 4.4 | Evaluation Framework (D1 + D2 + D3) | Diagram | ✅ Done |
| Figure 4.5 | Overall Methodology Overview | Summary Diagram | ✅ Done |

**Action:** These are already good. Just verify they meet the final protocol standards (especially font size and colorblind safety).

---

### Chapter 5: Experiments & Results (Highest Priority — 8–10 Figures Needed)

| Figure | Title | Type | Priority | Notes |
|--------|-------|------|----------|-------|
| **Figure 5.1** | Learning Curve — Final NER vs Best NER | Line Chart | **Critical** | Must show diminishing returns clearly |
| **Figure 5.2** | Cross-Domain PROPN Recall Comparison (All Models) | Grouped Bar | **Critical** | Include M4, Final NER, Best NER, LLMs |
| **Figure 5.3** | Type Confusion Heatmap (Final NER) | Heatmap | High | Linguistic interpretation in caption |
| **Figure 5.4** | Performance by Text Genre (Radar/Bar) | Radar or Grouped Bar | High | Show Epic vs Vedic gap visually |
| **Figure 5.5** | Major Character F1 Comparison (Rāma, Sītā, etc.) | Bar | High | Highlight perfect recall on Rāma/Sītā |
| **Figure 5.6** | Data Efficiency — F1 at Different Training Sizes | Line + Annotation | Medium | Emphasize 25% and 50% data points |
| **Figure 5.7** | Error Distribution by Genre (Stacked Bar) | Stacked Bar | Medium | Shows where errors concentrate |
| **Figure 5.8** | Model Size vs Performance (Bubble) | Scatter/Bubble | Medium | Shows 594M vs 27B–31B comparison |

**Critical Note:** Figures 5.1, 5.2, 5.3, and 5.4 are **non-negotiable** for a strong Chapter 5.

---

### Chapter 6 & 7 (Future)

- Figure 6.1: Case Study — Annotation of a New Purāṇa Manuscript (Before/After)
- Figure 7.1: Future Roadmap (Timeline)

---

## 3. Execution Plan (Step-by-Step)

### Phase 1: Setup (Today)
1. Create central `figures/` folder (done)
2. Copy the best color palette and template from `visualizations_protocol.md` into a reusable Python script
3. Create `generate_thesis_figures.py` in `chapters/figures/`

### Phase 2: Chapter 5 Critical Figures (Highest Priority)
**Order of generation:**
1. **Figure 5.1** — Learning Curve (most important for data efficiency story)
2. **Figure 5.2** — Cross-Domain Comparison (shows the +16 pp gain visually)
3. **Figure 5.3** — Confusion Heatmap (shows low cross-type confusion)
4. **Figure 5.4** — Genre Performance (shows Vedic challenge)
5. **Figure 5.5** — Major Characters (highlights novel Rāma/Sītā result)

### Phase 3: Polish & Verification
- Run all figures through the quality checklist in `visualizations_protocol.md`
- Generate both PDF (for thesis) and high-res PNG (for preview)
- Add proper captions with Devanagari where relevant

### Phase 4: Integration
- Move final PDFs to `thesis_markdown/chapters/figures/`
- Update each chapter's LaTeX file to include `\includegraphics` commands
- Update List of Figures in thesis

---

## 4. Immediate Next Action

Would you like me to:

**A.** Create the master `generate_thesis_figures.py` script following the protocol (recommended)  
**B.** Generate **Figure 5.1 (Learning Curve)** first as a test  
**C.** First regenerate all Chapter 3 and 4 figures to ensure consistency

Reply with **A, B, or C**.
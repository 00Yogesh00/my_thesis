# VISUALIZATION PROTOCOLS — Publication-Grade Standards

**Purpose:** Single authoritative reference for all visualization standards and protocols for thesis and potential publication  
**Last Updated:** May 3, 2026  
**Applies to:** All figures in thesis (Chapter 3: Dataset Description, Chapter 5: Experiments & Results, etc.)

---

## Table of Contents

1. [Why Protocols Matter](#1-why-protocols-matter)
2. [Technical Specifications](#2-technical-specifications)
   - 2.1 Resolution & File Format
   - 2.2 Figure Dimensions
   - 2.3 Font Requirements
   - 2.4 Line Widths & Markers
   - 2.5 Color Requirements
   - 2.6 Caption Requirements
3. [ACL/EMNLP Style Guide Specifics](#3-acl-emnlp-style-guide-specifics)
4. [Recommended Color Palette](#4-recommended-color-palette)
5. [Figure Template (Python Code)](#5-figure-template-python-code)
6. [Recommended Figures for Chapter 3](#6-recommended-figures-for-chapter-3)
7. [Common Mistakes to Avoid](#7-common-mistakes-to-avoid)
8. [Quality Checklist](#8-quality-checklist)

---

# 1. Why Protocols Matter

Your thesis will likely be:
1. **Submitted to DIAT Pune** (M.Tech thesis format requirements)
2. **Potentially published** as a conference paper (ACL, EMNLP, COLING, ICON, etc.)
3. **Read by Sanskrit scholars** who may print it in grayscale

**Publication protocols exist to ensure:**
- Readability across different media (screen, print, grayscale)
- Accessibility for readers with color vision deficiencies (~8% of males)
- Professional appearance that signals research quality
- Consistency with journal/conference style guides

---

# 2. Technical Specifications

## 2.1 Resolution & File Format

| Requirement | Specification | Why |
|-------------|---------------|-----|
| **Minimum Resolution** | **300 DPI** (dots per inch) | Standard for print publication |
| **Preferred Format** | **PDF** (vector graphics) | Scales infinitely, crisp at any size |
| **Alternative Format** | **PNG** (300 DPI minimum) | For raster graphics (photographs, complex heatmaps) |
| **Avoid** | JPG, low-resolution screenshots | Pixelation when zoomed/printed |

**Python Implementation:**
```python
plt.savefig('figures/figure_name.pdf', dpi=300, bbox_inches='tight', format='pdf')
```

---

## 2.2 Figure Dimensions (Standard Academic Sizes)

| Size | Width | Height | Use Case |
|------|-------|--------|----------|
| **Single Column** | 3.25–3.5 inches (8.25–8.9 cm) | Varies | Most figures in 2-column format papers |
| **Double Column** | 6.5–7 inches (16.5–17.8 cm) | Varies | Wide figures, comparison charts |
| **Full Page** | 8.5 × 11 inches (letter) or A4 | Full page | Only for complex multi-panel figures |
| **Thesis Standard** | **6 inches wide** (single column) | Proportional | Safe for both thesis and potential paper submission |

**Recommendation:** Design all figures at **6 inches wide** — works for thesis (single column) and future conference paper (fits in single column).

---

## 2.3 Font Requirements

| Element | Minimum Size | Recommended | Notes |
|---------|--------------|-------------|-------|
| **Axis labels** | 8 pt | **10–11 pt** | Must be readable when figure is 1/2 page width |
| **Tick labels** | 7 pt | **9–10 pt** | Numbers on axes |
| **Legend text** | 7 pt | **9–10 pt** | Category names |
| **Figure caption** | 8 pt | **9–10 pt** | Below figure, in LaTeX document |
| **Data labels** (if any) | 7 pt | **8–9 pt** | Numbers on bars/pie slices |

**Font Family Recommendations:**
- **Sans-serif:** Arial, Helvetica, DejaVu Sans (clean, modern, Unicode support)
- **Serif:** Times New Roman, Computer Modern (traditional, academic)
- **Recommendation:** Use **DejaVu Sans** (built into matplotlib, supports Sanskrit transliteration)

---

## 2.4 Line Widths & Markers

| Element | Minimum | Recommended | Notes |
|---------|---------|-------------|-------|
| **Line width** | 0.5 pt | **1.0–1.5 pt** | Thicker lines = more professional |
| **Marker size** | 4 pt | **6–8 pt** | For scatter plots, line charts |
| **Error bar width** | 0.5 pt | **1.0 pt** | Must be visible |
| **Grid lines** | 0.25 pt | **0.5 pt** (light gray) | Optional; use sparingly |

---

## 2.5 Color Requirements

### Colorblind Accessibility (CRITICAL)

| Statistic | Implication |
|-----------|-------------|
| ~8% of males have color vision deficiency | Figures must be interpretable without color |
| Red-green deficiency is most common | Avoid red/green color pairs |
| Grayscale printing is common | Figures must remain distinguishable in B&W |

### Colorblind-Friendly Palettes (Use These)

| Palette | Best For | Example Colors |
|---------|----------|----------------|
| **ColorBrewer "Set2"** | Categorical data | #66c2a5, #fc8d62, #8da0cb, #e78ac3 |
| **ColorBrewer "Dark2"** | Darker, professional | #1b9e77, #d95f02, #7570b3, #e7298a |
| **Okabe-Ito** | Colorblind-safe | #E69F00, #56B4E9, #009E73, #F0E442, #0072B2, #D55E00, #CC79A7, #000000 |
| **Matplotlib "tab10"** | Default, acceptable | 10 colors, reasonably accessible |

**Recommendation:** Use **ColorBrewer "Set2"** or **Okabe-Ito** palette.

### Grayscale Compatibility Test

**Rule:** If you print your figure in grayscale and cannot distinguish categories, redesign it.

**Solutions:**
1. Use **patterns** (hatch marks: ///, xxx, ..., \\\) in addition to color
2. Use **different line styles** (solid, dashed, dotted, dash-dot)
3. Use **different marker shapes** (circle, square, triangle, diamond)
4. Use **direct labels** on chart elements (not just legend)

---

## 2.6 Caption Requirements

**Every figure MUST have a caption that:**

1. **Is standalone** — readers should understand the figure without reading the main text
2. **Includes sample size (N)** — "N = 66,960 sentences"
3. **Defines all abbreviations** — "PER = Person, LOC = Location, MISC = Miscellaneous"
4. **States the key finding** — "Person entities comprise 91.1% of all annotations, demonstrating severe class imbalance."
5. **Cites data source** — "Data from Mahānāma (Sarkar et al., 2025)."

**Example Caption (Publication-Grade):**

> **Figure 3.1: Entity type distribution in Mahānāma training data (N = 66,960 sentences).** Person entities (PER) comprise 91.1% of all annotations, Location entities (LOC) comprise 3.8%, and Miscellaneous entities (MISC) comprise 5.1%. This severe class imbalance (91.1% PER) necessitated oversampling of LOC and MISC entities during training to prevent model bias toward Person classification. Data source: Mahānāma (Sarkar et al., 2025).

---

# 3. ACL/EMNLP Style Guide Specifics

Since this work is in **Computational Linguistics/NLP**, follow **ACL conference standards**:

## 3.1 ACL Figure Guidelines

| Requirement | ACL Standard | Implementation |
|-------------|--------------|----------------|
| **Figure placement** | "Here" (not floating) | Use `[H]` in LaTeX: `\begin{figure}[H]` |
| **Caption position** | Below figure | Standard in matplotlib/LaTeX |
| **Caption format** | "Figure 1: Description." | Use `\caption{}` in LaTeX |
| **Font in figures** | Match document font | Use same font family in matplotlib |
| **Line width** | Minimum 0.5pt | Use 1.0pt+ for visibility |
| **Color** | Color is allowed (since 2018) | But must be grayscale-compatible |

---

## 3.2 Common ACL Paper Figure Mistakes (Avoid These)

| Mistake | Why It's Rejected | How to Fix |
|---------|-------------------|------------|
| **Tiny fonts** | Unreadable when printed | Minimum 9pt, preferably 10-11pt |
| **Cluttered legends** | Too many categories | Max 5-6 categories; use "Other" for rest |
| **No error bars** | Hides uncertainty | Always include error bars for model results |
| **3D effects** | Unprofessional, distorts data | Use 2D only |
| **Low resolution** | Pixelated in print | 300 DPI minimum, PDF preferred |
| **Inconsistent colors** | Confusing across figures | Use same palette for all figures |

---

# 4. Recommended Color Palette

## 4.1 Primary Palette (Okabe-Ito + Extensions)

```python
colors = {
    'PER': '#E69F00',      # Orange (Person entities)
    'LOC': '#56B4E9',      # Sky Blue (Location entities)
    'MISC': '#009E73',     # Bluish Green (Miscellaneous entities)
    'DCS': '#F0E442',      # Yellow (DCS Sembank)
    'Vedic': '#0072B2',    # Blue (UD_Sanskrit-Vedic)
    'UFAL': '#D55E00',     # Vermillion (UD_Sanskrit-UFAL)
    'Mahanama': '#CC79A7', # Reddish Purple (Mahanama)
    'Other': '#000000'     # Black (Other/Combined)
}
```

## 4.2 Secondary Palette (ColorBrewer "Set2")

```python
colors_set2 = ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3']
```

---

# 5. Figure Template (Python Code)

## 5.1 Standard Template (Copy-Paste)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
plt.style.use('seaborn-v0_8-paper')
sns.set_context("paper", font_scale=1.2)

# Create figure (6 inches wide for thesis)
fig, ax = plt.subplots(figsize=(6, 4))

# Your plotting code here
# Example: bar chart
categories = ['Mahanama', 'DCS Sembank', 'Vedic', 'UFAL']
values = [66960, 18855, 27182, 230]
bars = ax.barh(categories, values, color=['#E69F00', '#56B4E9', '#009E73', '#F0E442'])

# Add data labels
for bar, val in zip(bars, values):
    ax.text(val + 500, bar.get_y() + bar.get_height()/2, f'{val:,}', 
            va='center', fontsize=9)

# Labels and title
ax.set_xlabel('Number of Sentences', fontsize=11)
ax.set_title('Dataset Size Comparison', fontsize=12, fontweight='bold')

# Remove top and right spines (clean look)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add light grid
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.5, axis='x')

# Save as PDF (300 DPI)
plt.savefig('figures/dataset_size_comparison.pdf', dpi=300, bbox_inches='tight', format='pdf')
plt.close()
```

## 5.2 Colorblind-Safe Template with Patterns

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('seaborn-v0_8-paper')

fig, ax = plt.subplots(figsize=(6, 4))

# Data
categories = ['PER', 'LOC', 'MISC']
values = [0.911, 0.038, 0.051]
colors = ['#E69F00', '#56B4E9', '#009E73']
patterns = ['/', 'x', 'o']  # Hatch patterns for grayscale

bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=0.5)

# Add patterns
for bar, pattern in zip(bars, patterns):
    bar.set_hatch(pattern)

# Labels
ax.set_ylabel('Proportion of Entities', fontsize=11)
ax.set_title('Entity Type Distribution in Mahānāma (N=66,960)', fontsize=11)
ax.set_ylim(0, 1.0)

# Add value labels
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
            f'{val*100:.1f}%', ha='center', fontsize=9)

plt.savefig('figures/entity_distribution.pdf', dpi=300, bbox_inches='tight', format='pdf')
plt.close()
```

---

# 6. Recommended Figures for Chapter 3

## 6.1 Must-Have Figures (Priority 1)

| Figure | Content | Type | Priority |
|--------|---------|------|----------|
| **Figure 3.1** | Dataset size comparison (all 4 datasets) | Horizontal bar chart | **MUST** |
| **Figure 3.2** | Mahanama entity distribution (class imbalance) | Pie chart or stacked bar | **MUST** |
| **Figure 3.3** | Training data composition (74%/11%/15%) | Stacked pie or donut | **MUST** |
| **Figure 3.4** | UFAL PROPN distribution (52/230 sentences) | Donut chart | **MUST** |

## 6.2 Should-Have Figures (Priority 2)

| Figure | Content | Type | Priority |
|--------|---------|------|----------|
| **Figure 3.5** | UPOS comparison (UFAL vs Vedic) | Grouped bar chart (top 8 tags) | **SHOULD** |
| **Figure 3.6** | Vedic morphological diversity | Heatmap (Case × Gender) | **SHOULD** |
| **Figure 3.7** | Cross-dataset comparison | Radar/spider chart | Optional |

**Total Recommended: 6-7 figures**

---

# 7. Common Mistakes to Avoid

| Mistake | Why It's Problematic | Solution |
|---------|---------------------|----------|
| **3D charts** | Distorts perception, unprofessional | Use 2D only |
| **Too many categories** | Cognitive overload | Max 5-6 categories; use "Other" |
| **Inconsistent scales** | Misleading comparisons | Same y-axis scale for comparisons |
| **Decorative elements** | Distracts from data | Remove shadows, gradients, 3D effects |
| **Missing error bars** | Hides uncertainty | Always include for model results |
| **Tiny fonts (6-7pt)** | Unreadable in print | Minimum 9pt, preferably 10-11pt |
| **Low resolution (<300 DPI)** | Pixelated in print | 300 DPI minimum, PDF preferred |
| **Red/green color pairs** | Colorblind readers cannot distinguish | Use ColorBrewer or Okabe-Ito palette |
| **No patterns/hatching** | Grayscale printing fails | Add hatch marks for B&W compatibility |
| **Inconsistent styling** | Looks sloppy | Use same template for all figures |

---

# 8. Quality Checklist

Before finalizing any figure, verify:

- [ ] **Resolution:** 300 DPI minimum, PDF format
- [ ] **Width:** 6 inches (single column) or 3.25 inches (narrow)
- [ ] **Fonts:** Minimum 9pt, preferably 10-11pt
- [ ] **Colors:** Colorblind-friendly palette (Okabe-Ito or ColorBrewer)
- [ ] **Grayscale test:** Print in B&W — can you distinguish categories?
- [ ] **Patterns:** Hatch marks added for B&W compatibility
- [ ] **Caption:** Standalone, includes N, defines abbreviations, states key finding
- [ ] **Data source:** Cited in caption
- [ ] **Spines:** Top and right spines removed (clean look)
- [ ] **Grid:** Light, optional (not distracting)
- [ ] **Legend:** Clear, not cluttered (max 5-6 items)
- [ ] **File name:** Descriptive (`entity_distribution_mahanama.pdf`, not `fig1.pdf`)

---

# 9. Quick Reference Card

| Parameter | Value |
|-----------|-------|
| **DPI** | 300 |
| **Format** | PDF (preferred) or PNG |
| **Width** | 6 inches (single column) |
| **Font size** | 10-11 pt (labels), 9 pt (ticks) |
| **Line width** | 1.0-1.5 pt |
| **Color palette** | Okabe-Ito or ColorBrewer "Set2" |
| **Patterns** | Required for B&W compatibility |
| **Caption** | Standalone, includes N, defines abbreviations |

---

**END OF VISUALIZATION PROTOCOLS**

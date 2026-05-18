# CHAPTER 3: DATASET DESCRIPTION — PUBLICATION-GRADE STRUCTURE & PROTOCOLS

**Version:** 2.0 (Publication-Optimized)  
**Last Updated:** May 3, 2026  
**Purpose:** Authoritative guide for writing a publication-grade Chapter 3  
**Target:** ACL/EMNLP/COLING submission standards + DIAT Pune thesis requirements

---

## Table of Contents

1. [Critical Principles](#1-critical-principles)
2. [Recommended Chapter Structure](#2-recommended-chapter-structure)
3. [Section-by-Section Guidelines](#3-section-by-section-guidelines)
4. [Figure Integration Protocol](#4-figure-integration-protocol)
5. [Citation Standards](#5-citation-standards)
6. [Writing Standards](#6-writing-standards)
7. [What to Include vs. Exclude](#7-what-to-include-vs-exclude)
8. [Quality Assurance Checklist](#8-quality-assurance-checklist)

---

# 1. Critical Principles

## 1.1 Core Philosophy

**A publication-grade dataset chapter is:**
- **Transparent:** Readers understand exactly what data was used and why
- **Reproducible:** Others can replicate the data pipeline
- **Justified:** Clear rationale for every decision
- **Honest:** Limitations are disclosed, not hidden
- **Concise:** 8-10 pages maximum (ACL standard)

**A publication-grade dataset chapter is NOT:**
- An exhaustive dump of all available information
- A defense of every dataset considered
- A technical manual for data preprocessing
- A place to discuss results or methodology

## 1.2 The 80/20 Rule

| Focus | Percentage of Effort | Rationale |
|-------|---------------------|-----------|
| **4 datasets used** | 80% | These are what matter |
| **7 datasets excluded** | 15% | Justify briefly, don't over-explain |
| **Everything else** | 5% | Background, context only |

## 1.3 Success Criteria

A Chapter 3 is successful if a reader can answer:
1. What data was used? (Yes/No)
2. Why was it selected? (Yes/No)
3. How was it prepared? (Yes/No)
4. What are the limitations? (Yes/No)
5. Could I reproduce this? (Yes/No)

---

# 2. Recommended Chapter Structure

## 2.1 Optimal Structure (8-10 pages)

```
3. Dataset Description

3.1 Overview and Selection Rationale (1-1.5 pages)
    3.1.1 Dataset Selection Criteria
    3.1.2 Summary of Datasets Used
    [Figure 3.1: Dataset Size Comparison]
    [Table 3.1: Dataset Summary]

3.2 Mahānāma: Gold-Standard NER Corpus (2-2.5 pages)
    3.2.1 Source and Construction
    3.2.2 Entity Annotation and Distribution
    [Figure 3.2: Entity Type Distribution]
    3.2.3 Class Imbalance and Oversampling
    3.2.4 Data Splits
    [Table 3.2: Mahānāma Statistics]

3.3 DCS: Silver-Standard NER and Linguistic Data (1.5-2 pages)
    3.3.1 Corpus Overview
    3.3.2 Sembank NER Extraction (Silver Standard)
    3.3.3 Linguistic Training Data
    3.3.4 Quality Limitations
    [Table 3.3: DCS Statistics]

3.4 Cross-Domain and Morphological Extension (1-1.5 pages)
    3.4.1 UD_Sanskrit-UFAL (Cross-Domain Evaluation)
    3.4.2 UD_Sanskrit-Vedic (Morphological Coverage)
    [Figure 3.3: Training Data Composition]
    [Table 3.4: Cross-Domain and Morphological Statistics]

3.5 Datasets Considered but Not Selected (1 page)
    [Table 3.5: Datasets Considered but Not Selected]
    3.5.1 Selection Philosophy

3.6 Summary (0.5 page)
    [Table 3.6: Final Dataset Summary]
```

## 2.2 Page Allocation

| Section | Pages | Priority |
|---------|-------|----------|
| 3.1 Overview | 1-1.5 | High |
| 3.2 Mahānāma | 2-2.5 | **Highest** |
| 3.3 DCS | 1.5-2 | High |
| 3.4 Cross-Domain/Morphological | 1-1.5 | Medium |
| 3.5 Datasets Not Selected | 1 | Low |
| 3.6 Summary | 0.5 | Medium |
| **Total** | **8-10** | — |

---

# 3. Section-by-Section Guidelines

## 3.1 Overview and Selection Rationale (1-1.5 pages)

### 3.1.1 Opening Paragraph (3-4 sentences)

**Required Elements:**
- Clear statement of what datasets were used
- Total data volume (N = X sentences)
- Brief purpose statement

**Example:**
> "This study utilizes four datasets totaling 113,227 sentences: Mahānāma (66,960 sentences) as the primary gold-standard NER corpus, DCS Sembank (18,855 sentences) as silver-standard NER data, UD_Sanskrit-Vedic (27,182 sentences) for morphological training, and UD_Sanskrit-UFAL (230 sentences) for cross-domain evaluation. Dataset selection was guided by five criteria: task alignment (NER), domain relevance (classical Sanskrit), language coverage (Sanskrit only), annotation quality (gold or high-quality silver), and resource efficiency. This chapter documents each dataset, justifies selection decisions, and discloses known limitations."

### 3.1.2 Selection Criteria (5 principles, 1 paragraph each)

| Criterion | One-Sentence Definition |
|-----------|------------------------|
| **Task Alignment** | Priority given to datasets designed for or adaptable to NER |
| **Domain Relevance** | Focus on classical Sanskrit (Vedas, epics, śāstras) over modern usage |
| **Language Coverage** | Exclusive focus on Sanskrit; non-Sanskrit datasets excluded |
| **Annotation Quality** | Preference for gold-standard or high-quality silver annotations |
| **Resource Efficiency** | Given finite time, priority to highest-impact datasets |

### 3.1.3 Summary Table (Table 3.1)

**Required Columns:**
- Dataset Name
- Size (sentences/tokens)
- Type (Gold/Silver)
- Purpose
- Source

**Figure 3.1:** Dataset Size Comparison (embedded after Table 3.1)

---

## 3.2 Mahānāma: Gold-Standard NER Corpus (2-2.5 pages)

### 3.2.1 Source and Construction

**Must Include:**
- Source: Sarkar et al. (2025), EMNLP 2025
- Construction: 73,000 verses from Mahābhārata + Sørensen's 1904 Index
- Total: 109,000+ entity mentions, 5,500 unique entities
- License: CC BY 4.0

### 3.2.2 Entity Annotation and Distribution

**Must Include:**
- Entity types: PER (91.1%), LOC (3.8%), MISC (5.1%)
- **Figure 3.2:** Entity Type Distribution (embedded)
- Annotation format: CoNLL-U with CorefUD entity layer

### 3.2.3 Class Imbalance and Oversampling

**Must Include:**
- Problem: 91.1% PER → model bias (M2 achieved F1=0 for LOC/MISC)
- Solution: LOC ×5, MISC ×5 oversampling
- Result: Balanced training distribution

### 3.2.4 Data Splits

**Must Include:**
- Train+Val: 66,960 sentences (used for Best NER & Final NER)
- Test: 6,672 sentences (held-out, never seen during training)
- **Table 3.2:** Mahānāma Statistics

---

## 3.3 DCS: Silver-Standard NER and Linguistic Data (1.5-2 pages)

### 3.3.1 Corpus Overview

**Must Include:**
- Size: 650,000 sentences, 4,500,000+ word references, 175,000 unique words
- Coverage: ~400 Sanskrit texts (Vedic + Classical)
- Citation: Hellwig (2010, 2019)

### 3.3.2 Sembank NER Extraction (Silver Standard)

**Must Include:**
- Process: Extracted from DCS Sembank (originally for WSD)
- Raw: 12,942 examples → After oversampling: 18,855
- Limitation: Not designed for NER; instance relations include both mentions and references

### 3.3.3 Linguistic Training Data

**Must Include:**
- Size: 60,000 sentences (9.2% of total DCS)
- Augmentation: 5 tasks (S, SM, L, LM, SLM) → ~300,000 examples
- Purpose: 15% regularization signal

### 3.3.4 Quality Limitations

**Must Include:**
- Krishnan et al. (2020): 5.5% doubtful compound splits, 2% segmentation errors
- No homonymy index → lost sense information
- **Table 3.3:** DCS Statistics

---

## 3.4 Cross-Domain and Morphological Extension (1-1.5 pages)

### 3.4.1 UD_Sanskrit-UFAL (Cross-Domain Evaluation)

**Must Include:**
- Size: 230 sentences from Pañcatantra
- Entity distribution: 52 sentences with PROPN (22.6%)
- Challenge: Devanagari → IAST transliteration required
- Limitation: Silver standard (no gold NER labels)
- Purpose: Test generalization beyond Mahābhārata domain

### 3.4.2 UD_Sanskrit-Vedic (Morphological Coverage)

**Must Include:**
- Size: 27,182 sentences, 206,440 tokens
- Morphological richness: 8 cases × 3 genders = 24 feature combinations
- Task conversion: 5-task augmentation (S, SM, L, LM, SLM)
- Purpose: Extend morphological understanding beyond Classical Sanskrit

**Figure 3.3:** Training Data Composition (embedded)

**Table 3.4:** Cross-Domain and Morphological Statistics

---

## 3.5 Datasets Considered but Not Selected (1 page)

### 3.5.1 Summary Table (Table 3.5)

**Columns:**
- Dataset
- Size
- Primary Reason for Exclusion
- Category (Domain/Task/Language/Quality)

**Categories:**
- **Domain mismatch:** Naamah, Sampurner (modern focus)
- **Task mismatch:** Itihāsa, Sāmayik (translation), Sanskrit Sembank (WSD)
- **Language exclusion:** Naamapadam (no Sanskrit)
- **Quality concerns:** WikiANN (noisy silver, title-based)

### 3.5.2 Selection Philosophy (2-3 paragraphs)

**Key Points:**
- Prioritized classical Sanskrit heritage over modern applications
- NER task alignment was non-negotiable
- Gold-standard quality preferred over quantity
- Resource efficiency: 4 datasets sufficient for rigorous evaluation

---

## 3.6 Summary (0.5 page)

### 3.6.1 Final Summary Table (Table 3.6)

**Columns:**
- Dataset
- Size
- Type (Gold/Silver)
- Role
- Key Statistic

### 3.6.2 Closing Statement

**Example:**
> "These four datasets provide a rigorous foundation for training and evaluating Sanskrit NER models: gold-standard in-domain data (Mahānāma), silver-standard supplementary data (DCS), cross-domain evaluation (UD_Sanskrit-UFAL), and morphological diversity (UD_Sanskrit-Vedic). The following chapter describes the methodology for model training and evaluation."

---

# 4. Figure Integration Protocol

## 4.1 Figure Placement Rules

| Rule | Implementation |
|------|----------------|
| **LaTeX placement** | `\begin{figure}[H]` (Here, not floating) |
| **Position in text** | Immediately after first reference |
| **Width** | `\includegraphics[width=0.85\textwidth]` |
| **Caption position** | Below figure |

## 4.2 Figure Requirements

| Requirement | Specification | Verification |
|-------------|---------------|--------------|
| **Format** | PDF (vector graphics) | All 4 figures are PDF |
| **Resolution** | 300 DPI minimum | Code specifies `dpi=300` |
| **Width** | 6 inches (single column) | `figsize=(6, 4)` |
| **Font size** | 10-11 pt | `font_scale=1.2` |
| **Color scheme** | Okabe-Ito (colorblind-safe) | Consistent across figures |
| **Hatch patterns** | Required for grayscale | Added to all figures |
| **File naming** | `figure_3_X_description.pdf` | Descriptive names |

## 4.3 Caption Requirements

**Every caption MUST contain:**

1. **Figure identifier:** "Figure 3.1:"
2. **Description:** What the figure shows
3. **Sample size:** "N = X sentences/tokens"
4. **Key finding:** One sentence highlighting the insight
5. **Data source:** "Data from [Citation]"

**Example (Figure 3.1):**
> **Figure 3.1: Dataset size comparison across all datasets used in this study (N = 113,227 total sentences).** Mahānāma provides the largest gold-standard NER corpus with 66,960 sentences (59% of total), while UD_Sanskrit-Vedic offers the largest morphological training resource with 27,182 sentences (24%). Data sources: Mahānāma (Sarkar et al., 2025), UD_Sanskrit-Vedic (Universal Dependencies), DCS Sembank (Hellwig, 2010), UD_Sanskrit-UFAL (Universal Dependencies).

---

# 5. Citation Standards

## 5.1 Required Citations

| Dataset | Citation | BibTeX Key |
|---------|----------|------------|
| **Mahānāma** | Sarkar et al. (2025). "Mahānāma: A Unique Testbed for Literary Entity Discovery and Linking." *Proceedings of EMNLP 2025*. | sarkar-etal-2025-mahanama |
| **DCS** | Hellwig, O. (2010, 2019). *The Digital Corpus of Sanskrit (DCS)*. | dcs |
| **DCS Quality** | Krishnan, A., Kulkarni, A., & Huet, G. (2020). "Validation and Normalization of DCS corpus using Sanskrit Heritage tools to build a tagged Gold Corpus." *arXiv:2005.06545*. | krishnan-etal-2020-validation |
| **UD Datasets** | Universal Dependencies Project. https://universaldependencies.org/ | ud-project |

## 5.2 In-Text Citation Format

| Context | Example |
|---------|---------|
| First mention | "Sarkar et al. (2025) introduced Mahānāma..." |
| Subsequent | "As documented by Sarkar et al. (2025)..." |
| Data source | "Data from Mahānāma (Sarkar et al., 2025)." |
| Limitation | "Krishnan et al. (2020) report 5.5% doubtful compound splits..." |

---

# 6. Writing Standards

## 6.1 Voice and Tone

| Guideline | Correct | Incorrect |
|-----------|---------|-----------|
| **Active voice** | "We selected Mahānāma because..." | "Mahānāma was selected because..." |
| **Specific numbers** | "66,960 sentences" | "approximately 67,000 sentences" |
| **Transparent limitations** | "DCS has known quality issues..." | "DCS is a large corpus..." |
| **No hedging** | "This dataset provides..." | "This dataset might provide..." |
| **Justified decisions** | "Oversampling was necessary because 91.1% PER would bias the model toward Person classification." | "We decided to oversample for balance." |

## 6.2 Terminology (Use Consistently)

| Term | Definition | Example |
|------|------------|---------|
| **Gold-standard** | Human-annotated, high-quality | Mahānāma |
| **Silver-standard** | Automatically extracted, lower quality | DCS Sembank NER |
| **In-domain** | Same domain as training (Mahābhārata) | Mahānāma test set |
| **Cross-domain** | Different domain (Pañcatantra) | UD_Sanskrit-UFAL |
| **PROPN** | Universal Dependencies proper noun tag | UD datasets |

## 6.3 Numbers and Statistics

| Guideline | Correct | Incorrect |
|-----------|---------|-----------|
| **Commas for thousands** | 66,960 | 66960 |
| **Percentage to 1 decimal** | 91.1% | 91% or 91.12% |
| **Include N** | "N = 66,960 sentences" | "66,960 sentences (N)" |
| **Scientific notation** | 4.5M+ word references | 4,500,000+ word references |

---

# 7. What to Include vs. Exclude

## 7.1 Mandatory Content (Must Include)

| Content | Location | Why |
|---------|----------|-----|
| Dataset selection rationale | Section 3.1 | Justifies methodology |
| Summary table of 4 datasets | Section 3.1 | Quick reference |
| Entity distribution | Section 3.2 | Explains class imbalance |
| Class imbalance + oversampling | Section 3.2 | Critical for reproducibility |
| Quality limitations (DCS, UD) | Sections 3.3, 3.4 | Honest disclosure |
| Cross-domain protocol | Section 3.4 | Explains Devanagari → IAST |
| 5-task augmentation | Section 3.4 | Explains morphological training |
| 7 excluded datasets (brief) | Section 3.5 | Demonstrates rigor |
| All 4 figures | Embedded | Visual evidence |
| All required citations | Throughout | Academic integrity |

## 7.2 Content to Exclude (Do NOT Include)

| Content | Reason | Alternative |
|---------|--------|-------------|
| **Figure 3.4 (UFAL PROPN Distribution)** | Redundant; low information density | Mention in text: "Only 52 of 230 UFAL sentences contain PROPN tokens (22.6%)" |
| **Figure 3.6 (Vedic Heatmap)** | Too technical; adds complexity | Summarize: "Vedic data provides 8 cases × 3 genders = 24 morphological feature combinations" |
| **Detailed annotation guidelines** | Not relevant to dataset description | Move to appendix or methodology chapter |
| **Model performance numbers** | Belongs in Chapter 5 (Results) | N/A |
| **Technical preprocessing code** | Belongs in Chapter 4 (Methodology) | N/A |
| **Discussion of results** | Belongs in Chapter 6 (Discussion) | N/A |
| **Future work suggestions** | Belongs in Chapter 7 (Conclusion) | N/A |
| **Detailed analysis of excluded datasets** | Distracts from main datasets | 1-line rationale in Table 3.5 |

## 7.3 Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|----------------|------------------|
| **Mixing datasets with methodology** | Confuses reader; violates chapter boundaries | Keep separate (Ch. 3 vs. Ch. 4) |
| **Hiding limitations** | Reduces credibility; violates transparency | Disclose all known issues |
| **Over-generalizing** | "All Sanskrit datasets have..." | Be specific: "The datasets used in this study..." |
| **Missing citations** | Academic misconduct | Cite all sources |
| **Inconsistent terminology** | Confuses reader | Use consistent terms throughout |
| **Decorative figures** | Wastes space; reduces impact | Each figure must tell a story |

---

# 8. Quality Assurance Checklist

## 8.1 Pre-Submission Checklist (16 Items)

Before finalizing Chapter 3, verify:

**Content Completeness:**
- [ ] All 4 datasets documented with complete statistics
- [ ] All 4 figures embedded with proper captions
- [ ] All required citations included (Sarkar 2025, Hellwig 2010, Krishnan 2020, UD)
- [ ] Class imbalance issue explained with oversampling justification
- [ ] Quality limitations disclosed (DCS 5.5% doubtful compounds, UD validation failures)
- [ ] Cross-domain protocol documented (Devanagari → IAST transliteration)
- [ ] Morphological task conversion explained (S, SM, L, LM, SLM)
- [ ] 7 excluded datasets justified with balanced rationale (1-line each)

**Figure Quality:**
- [ ] No Figure 3.4 (excluded as redundant)
- [ ] No Figure 3.6 (excluded as too technical; summarized in text)
- [ ] Consistent color scheme across all figures (Okabe-Ito palette)
- [ ] Hatch patterns on all figures for grayscale compatibility
- [ ] Captions include N, key finding, data source

**Writing Quality:**
- [ ] Consistent terminology (gold/silver, in-domain/cross-domain, PROPN)
- [ ] Numbers formatted correctly (commas, 1 decimal place, N values)
- [ ] Active voice throughout ("We selected..." not "was selected...")
- [ ] No hedging ("provides" not "might provide")

---

## 8.2 Peer Review Questions (5 Questions)

Before submission, ask:

1. **Can a reader reproduce the dataset preparation?** (Yes/No)
   - If No → Add data pipeline description

2. **Are all limitations transparently disclosed?** (Yes/No)
   - If No → Add quality issues section

3. **Is the dataset selection justified?** (Yes/No)
   - If No → Strengthen Section 3.1 and 3.5

4. **Do the figures add value or are they decorative?** (Value/Decorative)
   - If Decorative → Remove or redesign

5. **Is the writing clear and specific?** (Yes/No)
   - If No → Revise for specificity and active voice

---

## 8.3 Final Sign-Off

**Chapter 3 is ready for submission when:**
- [ ] All 16 checklist items are checked
- [ ] All 5 peer review questions are answered "Yes"
- [ ] Total length is 8-10 pages
- [ ] All figures are publication-grade (300 DPI, PDF, colorblind-safe)
- [ ] All citations are complete and consistent

---

**END OF PUBLICATION-GRADE STRUCTURE & PROTOCOLS**

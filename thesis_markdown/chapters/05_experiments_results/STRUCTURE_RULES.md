# CHAPTER 5: EXPERIMENTS & RESULTS — PUBLICATION-GRADE STRUCTURE & PROTOCOLS

**Version:** 3.0 (Publication-Optimized, Critically Revised)  
**Last Updated:** May 4, 2026  
**Purpose:** Authoritative guide for writing a publication-grade Chapter 5  
**Target:** ACL/EMNLP/COLING submission standards + DIAT Pune thesis requirements

---

## Table of Contents

1. [Critical Principles](#1-critical-principles)
2. [Recommended Chapter Structure](#2-recommended-chapter-structure)
3. [Section-by-Section Guidelines](#3-section-by-section-guidelines)
4. [Table & Figure Integration Protocol](#4-table--figure-integration-protocol)
5. [Citation & Verification Standards](#5-citation--verification-standards)
6. [Writing Standards](#6-writing-standards)
7. [What to Include vs. Exclude](#7-what-to-include-vs-exclude)
8. [Quality Assurance Checklist](#8-quality-assurance-checklist)
9. [Common Reviewer Questions (Anticipate These)](#9-common-reviewer-questions-anticipate-these)
10. [Common Writing Mistakes to Avoid](#10-common-writing-mistakes-to-avoid)

---

# 1. Critical Principles

## 1.1 Core Philosophy

**A publication-grade Experiments & Results chapter is:**
- **Transparent:** Every number is traceable to raw prediction files
- **Critical:** Trade-offs, failures, and limitations are discussed honestly
- **Scholar-focused:** Every result is connected to its impact on Sanskrit scholarship
- **Narrative-driven:** It tells a coherent story of scientific discovery, not a list of tables
- **Balanced:** Both strengths and weaknesses are presented fairly
- **Reproducible:** Others can verify every metric from the provided raw files
- **Concise:** 14–18 pages maximum (ACL standard for results chapter)

**A publication-grade Experiments & Results chapter is NOT:**
- A dump of every experiment ever run
- A defense of every hyperparameter choice
- A place to hide negative results
- An exhaustive list of ablation studies without interpretation
- A place to repeat methodology details (belongs in Chapter 4)

## 1.2 The 80/20 Rule (Where to Focus Your Effort)

| Section | Effort | Rationale |
|---------|--------|-----------|
| **Error Analysis & Qualitative Insights** | 30% | **Highest priority.** This section separates a good thesis from an excellent one. Must contain real Sanskrit examples with Devanagari + IAST + linguistic analysis. |
| **Main Results (D1 + D2 + D3)** | 25% | The core contribution. Must be crystal clear, verified, and immediately connected to Sanskrit scholarship. |
| **Comparison with Baselines & LLMs** | 15% | Critical for positioning the work. Must explain *why* this matters for historical language NLP. |
| **Ablation Studies & Strategy Analysis** | 12% | Shows why the design works. Include "Implications for Sanskrit Scholarship" subsection. |
| **Learning Curve & Data Efficiency** | 10% | Practical implication. Connect to accessibility for individual scholars. |
| **Limitations & Threats to Validity** | 8% | Required for trust. Be honest, confident, and forward-looking. |

## 1.3 Success Criteria

A Chapter 5 is successful if a reader can answer:
1. What is the single most important finding? (Yes/No)
2. How does Final NER compare to all baselines across D1, D2, and D3? (Yes/No)
3. Why does the model perform well on Rāma and Sītā but struggle with Vedic? (Yes/No)
4. What are the practical implications for Sanskrit scholars? (Yes/No)
5. What are the honest limitations? (Yes/No)
6. Could I trust these results enough to use the model in my own research? (Yes/No)

---

# 2. Recommended Chapter Structure

## 2.1 Optimal Structure (14–18 pages)

```
5. Experiments and Results

5.1 Executive Summary & Key Findings (1–1.5 pages)
    5.1.1 The Core Narrative
    5.1.2 Main Results at a Glance (Table 5.1)
    5.1.3 Key Findings (3–4 bullet points)

5.2 In-Domain NER Performance (D1) (2–2.5 pages)
    5.2.1 Main Results (Table 5.2)
    5.2.2 Per-Type Performance (Table 5.3)
    5.2.3 Statistical Significance (McNemar, Bootstrap CI)
    5.2.4 Critical Analysis

5.3 Linguistic Capability Preservation (D2) (2 pages)
    5.3.1 Segmentation and Lemmatisation Results
    5.3.2 Comparison with Pure NER Models
    5.3.3 Why Linguistic Regularisation Matters

5.4 Cross-Domain Generalisation (D3) (2–2.5 pages)
    5.4.1 Pañcatantra PROPN Recall Results
    5.4.2 Comparison with All Baselines (Table 5.4)
    5.4.3 The Trade-off (M4 vs Final NER)
    5.4.4 Implications for Unseen Corpora

5.5 Ablation Studies & Strategy Analysis (2 pages)
    5.5.1 Contribution of Each Strategy (Table 5.5)
    5.5.2 Synergistic Effects
    5.5.3 Why the Combination Works

5.6 Comparison with Baselines & Large Language Models (2 pages)
    5.6.1 Full Comparison Table (Table 5.6)
    5.6.2 Why a 594M Model Beats 27B–31B LLMs
    5.6.3 Implications for Low-Resource Historical Languages

5.7 Error Analysis & Qualitative Insights (3–3.5 pages) ← Longest and most important
    5.7.1 Type Confusion Matrix
    5.7.2 Major Character Performance (Rāma, Sītā — Novel Finding)
    5.7.3 Error Analysis by Text Genre
    5.7.4 Qualitative Examples (Devanagari + IAST + Analysis)
    5.7.5 Linguistic Interpretation of Errors

5.8 Learning Curve Analysis (1–1.5 pages)
    5.8.1 Performance vs Training Data Size (Table 5.7)
    5.8.2 Diminishing Returns & Data Efficiency
    5.8.3 Practical Implications

5.9 Limitations & Threats to Validity (1–1.5 pages)
    5.9.1 Internal Validity
    5.9.2 External Validity
    5.9.3 Construct Validity
    5.9.4 Summary Table

5.10 Summary & Key Takeaways for Sanskrit Scholars (1 page)
    5.10.1 Final Statement
    5.10.2 Practical Recommendations
```

---

# 3. Section-by-Section Guidelines

## 3.0 Mandatory "Implications for Sanskrit Scholarship" Subsection

**Every major section (5.2 – 5.8) MUST contain a short subsection titled:**

> **"Implications for Sanskrit Scholarship"**

This subsection should answer (in 3–5 sentences):
- How does this specific technical result help a real Sanskrit scholar or student?
- What practical decision can a scholar now make differently because of this result?
- What does this reveal about the nature of Sanskrit texts or computational methods?

**This is non-negotiable for publication-grade quality.** Without it, the chapter reads as "we built a better model" instead of "we solved a real problem for Sanskrit studies."

---

## 3.1 Executive Summary (5.1)

- Start with the **single most important sentence** of the entire thesis.
- Present the three desiderata balance as the core contribution.
- Use a clean comparison table (Final NER vs Best NER).
- End with 3–4 crisp "Key Findings" that a reader can remember.

## 3.2 In-Domain NER Performance (5.2)

- Lead with the main result (0.8522 F1).
- Include per-type breakdown (Person, Location, Misc).
- Report statistical significance (McNemar test, Bootstrap CI).
- Be critical: explain why Final NER is slightly lower than Best NER on D1 but superior overall.

## 3.3 Linguistic Capability Preservation (5.3)

- This is a **unique contribution** — most NER papers ignore this.
- Show the catastrophic failure of pure NER models (D2 ≈ 0%).
- Explain why 15% linguistic regularisation restores capability without major NER loss.
- Connect to scholar usability.

## 3.4 Cross-Domain Generalisation (5.4)

- Present the +16 pp gain as a major result.
- Be honest about M4 having higher PROPN recall (85.1%) but zero D2.
- Frame the trade-off clearly: Final NER offers the **best balance**.
- Discuss implications for applying the model to new, unseen corpora.

## 3.5 Error Analysis & Qualitative Insights (5.7) — MOST IMPORTANT SECTION

**This is the section that will determine whether your thesis is accepted at ACL/EMNLP or published in a journal.**

This section separates a good thesis from an excellent one.

**Mandatory Requirements:**
- Full confusion matrix with **linguistic interpretation** (not just numbers)
- Major character analysis (Rāma, Sītā perfect recall) — explicitly frame as a **novel Sanskrit-specific contribution** that overcomes DCS Sembank limitations
- Genre-wise analysis with **deep linguistic explanations** (Vedic archaisms, sandhi resolution failures, compound noun ambiguity, ontological ambiguity in mythological beings)
- **Minimum 4–5 qualitative examples**, each containing:
  - Devanagari text
  - IAST transliteration
  - English gloss + entity annotation
  - Gold vs. Model Prediction
  - Critical linguistic analysis of the error/success
- Every example must answer: *"What does this tell us about Sanskrit NER challenges?"*
- Connect all errors back to **DCS Sembank extraction limitations** and real Sanskrit linguistic phenomena

**Scholarly Implication (Required in this section):**
After presenting the error analysis, include a dedicated subsection titled **"Implications for Sanskrit Scholarship"** that answers:
- Which types of texts can scholars trust Final NER on today?
- Where should they still apply manual correction?
- What does the perfect Rāma/Sītā recall tell us about the model's cultural knowledge?

## 3.6 Limitations (5.9)

- Structure by validity type (Internal / External / Construct)
- Be honest but frame as opportunities for future work
- Include a summary table
- Do not over-apologize — the work is strong

---

# 4. Table & Figure Integration Protocol

## 4.1 Required Tables

| Table | Title | Priority | Source |
|-------|-------|----------|--------|
| Table 5.1 | Final NER vs Best NER — Core Performance Comparison | High | thesis_verified_results.json |
| Table 5.2 | Per-Type NER Performance (Final NER) | High | eval_final_ner_raw.json |
| Table 5.3 | Cross-Domain PROPN Recall — All Models | High | eval_final_ner_crossdomain.log |
| Table 5.4 | Ablation Study — Contribution of Each Strategy | High | Training logs |
| Table 5.5 | Full Model Comparison (Including LLMs) | High | All raw JSON files |
| Table 5.6 | Confusion Matrix (Final NER) | High | eval_final_ner_raw.json |
| Table 5.7 | Major Character Performance | High | Manual extraction + raw JSON |
| Table 5.8 | Performance by Text Genre | Medium | Genre metadata + raw JSON |
| Table 5.9 | Learning Curve Results | Medium | Training experiment logs |
| Table 5.10 | Limitations Summary | High | Author synthesis |

## 4.2 Final Approved Figures for Chapter 5 (8 Figures)

| Figure | Title | File Name | Source | Priority |
|--------|-------|-----------|--------|----------|
| Figure 5.1 | F1 Score Comparison | `Figure_5_1_F1_Comparison_v3.pdf` | New v3 | Critical |
| Figure 5.2 | Learning Curve | `Figure_5_1_Learning_Curve_v3.pdf` | New v3 | High |
| Figure 5.3 | Cross-Domain PROPN Recall | `Figure_5_2_CrossDomain_Recall_v3.pdf` | New v3 | Critical |
| Figure 5.4 | Type Confusion Matrix | `Figure_5_3_Type_Confusion_Heatmap_v3.pdf` | New v3 | High |
| Figure 5.5 | Genre Performance | `Figure_5_4_Genre_Performance_v3.pdf` | New v3 | Medium |
| Figure 5.6 | Major Character Performance | `Figure_5_5_Major_Characters_v3.pdf` | New v3 | High |
| Figure 5.7 | Bootstrap Confidence Intervals | `FINAL_ACL_04_bootstrap_ci.png` | Old FINAL_ACL_ | High |
| Figure 5.8 | Bootstrap Distribution of F1 | `FINAL_ACL_14_bootstrap_distribution.png` | Old FINAL_ACL_ | High |

## 4.2 Required Figures

| Figure | Title | Priority | Source |
|--------|-------|----------|--------|
| Figure 5.1 | Learning Curve — Final NER vs Best NER | High | Training logs |
| Figure 5.2 | Error Distribution by Genre | Medium | Genre analysis |
| Figure 5.3 | Type Confusion Heatmap | Medium | Confusion matrix |

**Note:** All figures must follow `visualizations_protocol.md` (300 DPI, PDF, colorblind-safe, hatch patterns, clear captions).

---

# 5. Citation & Verification Standards

- Every number must be traceable to a raw file (`eval_final_ner_raw.json`, `eval_final_ner_crossdomain_raw.json`, etc.).
- Use footnotes or parenthetical citations like: "(Source: `eval_final_ner_raw.json`, 6,672 sentences, 8,188 gold entities, verified May 4, 2026)".
- For LLM comparisons, clearly state estimation method if exact numbers are not available.
- All claims about "novel contribution" (e.g., perfect Rāma/Sītā recall) must be backed by explicit comparison to DCS extraction limitations.

---

# 6. Writing Standards

- Use **active voice** where possible ("Final NER achieves..." not "It was observed that...").
- Every technical claim must have a **scholarly implication** sentence.
- Sanskrit terms should be in **Devanagari + IAST** on first use.
- Error examples must include Devanagari, IAST, and English gloss.
- Be critical but constructive — frame limitations as future work opportunities.

---

# 7. What to Include vs. Exclude

**Include:**
- All verified metrics from raw files
- Critical analysis of trade-offs (M4 vs Final NER)
- Sanskrit-specific linguistic interpretation of errors
- Qualitative examples with full context
- Clear connection to Sanskrit scholarship

**Exclude:**
- Every single hyperparameter tried
- Raw training logs
- Duplicate tables from Chapter 4
- Overly technical implementation details (belongs in Chapter 4)
- Defensive language ("Despite the limitations...")

---

# 8. Quality Assurance Checklist

Before finalizing Chapter 5, verify:

- [ ] All numbers match raw JSON files exactly
- [ ] At least 3 qualitative Sanskrit examples with Devanagari + IAST
- [ ] Perfect Rāma/Sītā recall is framed as a novel contribution
- [ ] M4's higher cross-domain recall is honestly discussed
- [ ] Vedic performance gap is explained linguistically
- [ ] Limitations section is structured and non-defensive
- [ ] Every table has a clear scholarly implication
- [ ] Chapter tells a coherent story from "problem" → "solution" → "evidence" → "implication"

---

# 9. Common Reviewer Questions (Anticipate These)

1. "Why is Final NER slightly worse than Best NER on in-domain F1?"
2. "How can you claim generalisation when cross-domain evaluation is only binary?"
3. "Why didn't you do a full hyperparameter search?"
4. "Is the perfect Rāma/Sītā recall just luck or a real contribution?"
5. "How would this model perform on Vedic texts in practice?"
6. "Why should scholars trust these results over a much larger LLM?"

---

# 10. Common Writing Mistakes to Avoid

- Starting with "We achieved X" without context
- Hiding the M4 trade-off
- Treating error analysis as an afterthought
- Using vague phrases like "reasonable performance"
- Forgetting to connect technical results to Sanskrit scholarship
- Over-apologizing in the limitations section

---

**END OF STRUCTURE_RULES.md — Chapter 5**

**This document is the authoritative reference for writing Chapter 5.**  
Follow it strictly to achieve publication-grade quality.
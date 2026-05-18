# CHAPTER 4: METHODOLOGY — PUBLICATION-GRADE STRUCTURE & PROTOCOLS

**Version:** 2.0 (Publication-Optimized, Critically Revised)  
**Last Updated:** May 4, 2026  
**Purpose:** Authoritative guide for writing a publication-grade Chapter 4  
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
9. [Common Reviewer Questions (Anticipate These)](#9-common-reviewer-questions-anticipate-these)
10. [Common Writing Mistakes to Avoid](#10-common-writing-mistakes-to-avoid)

---

# 1. Critical Principles

## 1.1 Core Philosophy

**A publication-grade methodology chapter is:**
- **Transparent:** Every design choice is explained with evidence
- **Reproducible:** Others can replicate the entire pipeline
- **Justified:** Every decision has a clear rationale backed by experiments
- **Critical:** Limitations and trade-offs are discussed honestly, not hidden
- **Scholarly:** Every technical decision is connected to its impact on Sanskrit scholarship
- **Narrative-driven:** It tells a coherent story, not a list of technical details
- **Concise:** 12–14 pages maximum (ACL standard)

**A publication-grade methodology chapter is NOT:**
- A technical manual of every experiment tried
- A defense of every hyperparameter choice
- A place to report results (belongs in Chapter 5)
- An exhaustive dump of training logs
- A place to hide limitations

## 1.2 The 80/20 Rule (Where to Focus Your Effort)

| Section | Effort | Rationale |
|---------|--------|-----------|
| **Data Preparation Pipeline** | 30% | Contains the **novel methodological contribution** (DCS extraction with 3 attempts). This is what makes the chapter publishable. |
| **Training Strategies & Evolution** | 25% | Shows how you systematically improved the model. Critical for credibility. |
| **Evaluation Framework + Statistics** | 20% | Bootstrap, McNemar, and agreement analysis give the chapter scientific rigor. |
| **QLoRA + Implementation** | 15% | Necessary technical detail, but do not over-explain. |
| **Reproducibility & Limitations** | 10% | Required for trust. Be honest but frame positively. |

## 1.3 Success Criteria

A Chapter 4 is successful if a reader can answer:
1. What models and data were used? (Yes/No)
2. Why was this experimental design chosen? (Yes/No)
3. How exactly was the data prepared, especially the DCS Sembank extraction? (Yes/No)
4. What are the trade-offs between in-domain performance and cross-domain generalisation? (Yes/No)
5. What are the known limitations? (Yes/No)
6. Could I reproduce the entire pipeline? (Yes/No)

---

# 2. Recommended Chapter Structure

## 2.1 Optimal Structure (12–14 pages)

```
4. Methodology

4.1 Research Design and Methodological Philosophy (1–1.5 pages)
    4.1.1 The Three Desiderata
    4.1.2 Why Fifteen Models Were Necessary
    4.1.3 Connection to Sanskrit Scholarship

4.2 Base Models and Architectures (1 page)
    4.2.1 ByT5-Sanskrit (594M) — Primary Model Family
    4.2.2 Gemma4 E4B (4.5B) — Decoder-Only Comparison
    4.2.3 Zero-Shot Large Language Models
    4.2.4 Gazetteer Baseline (M1)

4.3 Data Preparation Pipeline (2.5–3 pages) ← Longest and most important section
    4.3.1 Mahānāma Gold-Standard NER Preparation
    4.3.2 DCS Sembank Silver NER Extraction (Novel Contribution)
        - The Problem: Common Noun Contamination
        - Three Extraction Attempts (Full Transparency)
        - Final Method and Diagnostic Verification
        - Before vs After Examples
        - Known Limitations (Rāma/Sītā Low Recall)
    4.3.3 Linguistic Regularisation Data (15% S + L)
    4.3.4 Final Training Data Composition
    [Figure 4.1: DCS Sembank Extraction Pipeline (3 Attempts)]
    [Table 4.1: Training Data Composition Comparison]

4.4 Training Strategies (2–2.5 pages)
    4.4.1 Strategy Taxonomy (1+2+4)
    4.4.2 Evolution from Best NER to Final NER
        - Trade-off: In-Domain F1 vs Cross-Domain Recall
    4.4.3 Training Configuration Comparison
    [Figure 4.2: Training Strategy Evolution Diagram]

4.5 QLoRA Configuration & Implementation (1 page)
    4.5.1 QLoRA Hyperparameters (Constant Across Experiments)
    4.5.2 Quantisation Sensitivity (Critical Lesson — Callout Box)
    4.5.3 Tokenisation & Generation Settings (`max_new_tokens=256`)

4.6 Evaluation Framework (1.5 pages)
    4.6.1 D1: In-Domain NER (Mahānāma Test Split — 6,672 sentences)
    4.6.2 D2: Linguistic Capability Preservation (DCS Held-Out — 200 sentences)
        - Note on D2 Seed Inconsistency
    4.6.3 D3: Cross-Domain Generalisation (Pañcatantra — 230 sentences)
    [Table 4.2: Evaluation Dimensions Summary]

4.7 Statistical Analysis Methods (1 page)
    4.7.1 Bootstrap 95% Confidence Intervals (10,000 resamples)
    4.7.2 McNemar’s Test (Sentence-Level Pairwise Comparison)
    4.7.3 Cross-Model Agreement Analysis

4.8 Reproducibility & Limitations (1–1.5 pages)
    4.8.1 Reproducibility Checklist
    4.8.2 Guide’s Machine Notes (RTX PRO 4500 Blackwell)
    4.8.3 Critical Limitations & Methodological Risks
        - Single Test Set Limitation
        - No Systematic Hyperparameter Optimisation
        - Pretraining Asymmetry Confound
        - Entity Type Taxonomy Limitations
        - Exact Match Evaluation Limitations
        - Cross-Domain Evaluation is Binary Only
        - QLoRA Quantisation Sensitivity
        - ByT5 Generation Length Sensitivity

4.9 Summary (0.5 page)
```

---

# 3. Section-by-Section Guidelines

## 3.1 Research Design Philosophy (1–1.5 pages)
**What to Emphasize:**
- The **Three Desiderata** are the foundation of the entire thesis
- Why 15 models were necessary (systematic isolation of variables)
- Connection to Sanskrit scholarship (democratizing access to classical knowledge)

**What to Downplay:**
- Do not over-justify every single model (M1–M7, V2a–V4). Group them.

**Writing Tip:** Write this section **last**, after you have written the Training Strategies section. It will be more coherent.

## 3.2 Data Preparation Pipeline (2.5–3 pages — Most Important)
**What to Emphasize:**
- The **novel contribution**: The correct distinction between entity reference (column 0) and entity mention (column 1)
- The **three-attempt story** with full transparency (this builds credibility)
- **Before vs After** concrete examples (top entities before and after)
- **Known limitations** (Rāma/Sītā low recall, domain skew) — be honest here

**What to Downplay:**
- Do not over-explain the broken attempts (Attempt 1 and 2). One paragraph each is enough.

**Critical Callout Box:**
> **Important:** The DCS Sembank extraction methodology (including its limitations) is a reusable pipeline for future researchers. Document it clearly.

## 3.3 Training Strategies (2–2.5 pages)
**What to Emphasize:**
- The **trade-off** between in-domain F1 (Best NER 0.860) and cross-domain recall (Final NER +16 points)
- Strategy 2 (Linguistic Regularisation) is what preserved D2 capability
- Strategy 1 (Full Sembank) is what improved cross-domain generalisation

**Writing Tip:** Use a **Strategy Evolution Diagram** (Figure 4.2) to show the progression visually.

## 3.4 QLoRA & Implementation (1 page)
**What to Emphasize (Critical Lessons):**
- **Quantisation Sensitivity:** Adapters must be evaluated with the exact same 4-bit NF4 config used during training (otherwise F1 drops ~10 points)
- **`max_new_tokens=256`:** Using 64 causes truncation and large performance drops. This is a common mistake.

**Callout Box:**
> **Critical Lesson:** QLoRA adapters trained on 4-bit NF4 **must** be evaluated with the same quantisation configuration. Loading the base model in bf16 when the adapter was trained on 4-bit produces misaligned weights.

## 3.5 Evaluation Framework (1.5 pages)
**What to Emphasize:**
- D1 is the primary benchmark (6,672 sentences, gold labels)
- D2 has a **known inconsistency** (different random seeds across machines) — acknowledge it
- D3 is **binary only** (no gold PER/LOC/MISC labels) — acknowledge it

**What to Downplay:**
- Do not over-explain the D2 seed issue. One sentence is enough.

## 3.6 Statistical Methods (1 page)
**What to Emphasize:**
- Bootstrap 95% CI (10,000 resamples)
- McNemar’s test shows that even small F1 differences (0.008) can be statistically significant if error patterns differ
- Cross-Model Agreement shows that Best NER and Final NER are closely related but meaningfully different

## 3.7 Reproducibility & Limitations (1–1.5 pages)
**What to Emphasize:**
- Be **honest but positive**. Frame limitations as "known boundaries" rather than "failures."
- End with: "Despite these limitations, the core findings remain robust..."

**What to Downplay:**
- Do not over-explain every limitation. Group them (e.g., "Evaluation Limitations," "Data Limitations").

---

# 4. Figure Integration Protocol

**Required Figures (Minimum 5):**
- Figure 4.1: DCS Sembank Extraction Pipeline (3 Attempts) — **Most Important**
- Figure 4.2: Training Strategy Evolution Diagram
- Figure 4.3: QLoRA Multi-task Architecture
- Figure 4.4: Three-Dimensional Evaluation Framework (D1/D2/D3)
- Figure 4.5: Overall Methodology Architecture

**Caption Requirements:**
Every caption must contain:
1. Figure identifier
2. What it shows
3. Key finding
4. Data source + verification

---

# 5. Citation Standards

**Required Citations:**
- Sarkar et al. (2025) — Mahānāma
- Hellwig (2010, 2019) — DCS
- Krishnan et al. (2020) — DCS quality issues
- Universal Dependencies Project

---

# 6. Writing Standards (from STYLE_GUIDE.md)

- Active voice throughout
- Critical analysis in every paragraph
- Connect every decision to Sanskrit scholarship
- No hedging ("very/really/a lot")
- Every section ends with a "so what?" sentence for Sanskrit scholars

---

# 7. What to Include vs. Exclude

**Must Include:**
- All verification tags from `Methodology_Knowledge_Base.md`
- Before/After examples for DCS extraction (with top entities before and after)
- Strategy Evolution Diagram (Figure 4.2)
- Quantisation sensitivity lesson (Critical Lesson box)
- `max_new_tokens=256` requirement (bold warning)
- Honest limitations (Rāma/Sītā recall, pretraining confound, D2 seed issue)
- Complete reproducibility checklist
- Connection to Sanskrit scholarship in every section

**Do NOT Include:**
- Model performance numbers (belongs in Chapter 5)
- Training curves / loss plots (belongs in Chapter 5)
- Generic future work (belongs in Chapter 6)
- Detailed hyperparameter search justification (too technical)
- Over-explanation of broken extraction attempts (Attempt 1 and 2)

---

# 8. Quality Assurance Checklist

**Critical (Must Have — 12 Items):**
- [ ] All verification tags present
- [ ] Before/After DCS examples included
- [ ] Strategy Evolution Diagram present
- [ ] Quantisation sensitivity highlighted (callout box)
- [ ] `max_new_tokens=256` emphasized (bold warning)
- [ ] All limitations honestly discussed
- [ ] Reproducibility checklist complete
- [ ] Every section connects to Sanskrit scholarship
- [ ] Active voice throughout
- [ ] All numbers match `thesis_verified_results.json`
- [ ] Total length 12–14 pages
- [ ] All citations complete

**Recommended (Nice to Have — 8 Items):**
- [ ] Common Reviewer Questions section included
- [ ] Figure captions are scholar-focused
- [ ] No hedging language
- [ ] Every section ends with "so what?" sentence

---

# 9. Common Reviewer Questions (Anticipate These)

**Q1: Why no hyperparameter optimisation?**  
**Answer:** Computational cost + practical constraints. We prioritised systematic comparison across 15 models over exhaustive search on one model.

**Q2: Why only one test set (Mahānāma)?**  
**Answer:** It is the only existing gold-standard Sanskrit NER dataset. Cross-domain evaluation (D3) partially addresses this limitation.

**Q3: Why is D2 evaluation inconsistent across machines?**  
**Answer:** Different random seeds were used. We acknowledge this limitation and recommend re-evaluation for cross-machine comparison.

**Q4: Why does Rāma have low recall in DCS extraction?**  
**Answer:** Rāma is used as both descriptor and entity name in the Sembank. We accept this as a known limitation because Mahānāma gold data already covers these characters extensively.

**Q5: Why is the silver dataset so small (12,955 examples)?**  
**Answer:** Quality over quantity. The value lies in diversity (120 texts) and correctness (proper name only, no common noun contamination).

---

# 10. Common Writing Mistakes to Avoid

**Mistake 1:** Burying the novel contribution (DCS extraction) in the middle of the Data Preparation section.  
**Fix:** Make it a prominent subsection with the 3-attempt story.

**Mistake 2:** Over-explaining broken attempts (Attempt 1 and 2).  
**Fix:** One paragraph each is enough. Focus on the final correct method.

**Mistake 3:** Hiding limitations in an appendix or at the very end.  
**Fix:** Integrate limitations into the relevant sections (e.g., Rāma/Sītā recall in Data Preparation, D2 seed issue in Evaluation Framework).

**Mistake 4:** Forgetting to mention `max_new_tokens=256` and quantisation sensitivity.  
**Fix:** Use callout boxes. These are common reproducibility pitfalls.

**Mistake 5:** Writing the Research Design Philosophy section first.  
**Fix:** Write it **last**, after you have written the Training Strategies section. It will be more coherent.

---

**END OF PUBLICATION-GRADE STRUCTURE & PROTOCOLS**
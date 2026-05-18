# STRUCTURE & RULES — Chapter 3: Dataset Description

**Last Updated:** May 3, 2026  
**Target Length:** 10–12 pages  
**Style:** Publication-grade (ACL/EMNLP standard)

---

## Chapter Structure (Approved)

### 3.1 Introduction (3 paragraphs)
- Paragraph 1: What datasets + why (purpose + quality)
- Paragraph 2: In-domain vs cross-domain motivation + challenges
- Paragraph 3: Chapter organization + connection to research goals

### 3.2 The Mahanama Dataset (In-Domain Evaluation)
- 3.2.1 Source and Construction (4–5 paragraphs)
- 3.2.2 Dataset Statistics (4–5 paragraphs + table)
- 3.2.3 Train/Dev/Test Splits (2–3 paragraphs)
- 3.2.4 Entity Annotation Guidelines (2–3 paragraphs)

### 3.3 The UD_Sanskrit-UFAL-master Dataset (Cross-Domain Evaluation)
- 3.3.1 Source and Motivation (3–4 paragraphs)
- 3.3.2 Dataset Statistics (3–4 paragraphs + table)
- 3.3.3 Purpose in This Thesis (2–3 paragraphs)

### 3.4 Challenges in Sanskrit NER Datasets
- 3.4.1 Linguistic Challenges (3–4 paragraphs)
- 3.4.2 Dataset-Specific Challenges (2–3 paragraphs)
- 3.4.3 Comparison with Modern Language NER Datasets (3–4 paragraphs)

### 3.5 Qualitative Examples (4–6 examples)
- Devanagari + IAST + English gloss + entity annotations + analysis

### 3.6 Summary (3–4 paragraphs)

---

## Required Figures/Tables

| Figure/Table | Description | Priority |
|--------------|-------------|----------|
| **Table 3.1** | Mahanama Dataset Statistics (sentences, tokens, entities, PER/LOC/MISC distribution) | High |
| **Table 3.2** | UD_Sanskrit-UFAL-master Dataset Statistics (comparison with Mahanama) | High |
| **Table 3.3** | Entity Type Distribution Comparison (Mahanama vs UD_Sanskrit-UFAL vs CoNLL-2003) | Medium |
| **Figure 3.1** | Entity Distribution Pie Chart (Mahanama) | Medium |
| **Figure 3.2** | Sentence Length Distribution (Mahanama vs UD_Sanskrit-UFAL) | Low |

---

## Writing Rules (from STYLE_GUIDE.md)

- Every claim must have a citation
- Use placeholder citations until real citations are added
- Connect every section back to "democratizing access to Sanskrit knowledge"
- Use critical analysis (not just description)
- Include qualitative examples with Devanagari + IAST + English gloss
- End each major section with a "so what?" sentence for scholars

---

## Critical Requirements

- **No unsupported assertions** about dataset characteristics
- **Compare with established benchmarks** (CoNLL-2003, OntoNotes)
- **Explain why Sanskrit NER is harder** than modern language NER
- **Justify every design decision** (why these datasets, why these splits)

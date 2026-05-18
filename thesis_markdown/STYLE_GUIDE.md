# STYLE GUIDE — Publication-Grade Thesis Writing Rules

**Purpose:** This guide ensures the thesis meets the standards of top-tier venues (ACL, EMNLP, NAACL) and DIAT M.Tech thesis requirements.

**Last Updated:** May 3, 2026

---

## 1. Core Principles (Non-Negotiable)

1. **Every sentence must serve the purpose:** Democratizing access to Sanskrit knowledge for scholars, students, and practitioners.
2. **Domain fidelity is a strength, not a weakness.** Poor performance on modern/Western datasets is expected and positive.
3. **Use real data only from `source_data/`** — never hallucinate numbers, confidence intervals, or statistical results.
4. **Be critical but respectful** of Sanskrit tradition and previous scholarship.
5. **Every major claim must have a citation.** No unsupported assertions.
6. **Connect every technical contribution back to scholarly impact.** Never let technical details stand alone.

---

## 2. Critical Analysis Rules (Mandatory for Publication)

**Never just describe — always evaluate.**

### Required Sentence Starters for Critical Analysis:
- "While X achieved strong results on Y, it failed to address Z, which is particularly problematic for classical Sanskrit because..."
- "A critical limitation of previous approaches is..."
- "This finding is significant because it challenges the assumption that..."
- "However, this approach remains limited by..."
- "Unlike prior work, this thesis demonstrates that..."

### Rules:
- Every paragraph must contain at least **one critical judgment**
- Always explain *why* something is a strength or weakness
- Connect criticism back to your research gap when possible
- Avoid hedging: "It seems that..." → "We demonstrate that..."
- Be direct but respectful: "This is a critical gap" not "This might be considered a gap"

---

## 3. Thesis Positioning Rules (Required for Top-Tier Venues)

**Every chapter must explicitly answer: "Why does this matter for Sanskrit scholarship?"**

### Required Positioning Statements:
- **Literature Review:** "This thesis is the first to..." or "Unlike previous work, this thesis..."
- **Results:** Always connect findings back to scholarly impact
- **Conclusion:** Articulate contribution in 2–3 sentences maximum

### Rules:
- Never let technical details stand alone — always link to scholarly purpose
- Use phrases like: "This advances the field by..." or "This contributes to Sanskrit scholarship by..."
- In every chapter, end with a "so what?" sentence for scholars

---

## 4. Citation Style (ACL/EMNLP Standard)

- Use **natbib** with `plainnat` bibliography style
- In-text citations:
  - `\citep{AuthorYear}` → (Author et al., Year)
  - `\citet{AuthorYear}` → Author et al. (Year)
- Every major claim must have a citation
- Avoid citing the same source repeatedly in one paragraph
- Use "et al." for 3+ authors after first citation
- Never use citations in abstracts or figure captions
- All citations must appear in `references.bib`

---

## 5. Sanskrit Scholarly Conventions

### Terminology:
- Use **IAST** for all Sanskrit terms in running text: *sandhi*, *samāsa*, *Mahābhārata*
- Use **Devanagari** only for:
  - Direct textual quotations longer than 3 words
  - Terms being defined for the first time
  - Verse citations (with IAST translation following)
- Always gloss Sanskrit terms on first use: "sandhi (euphonic combination)"
- Be consistent: "sandhi" not "Sandhi" (lowercase unless proper noun)

### Text Citations:
- Cite Sanskrit texts with standard abbreviations:
  - Mbh. = Mahābhārata
  - Rām. = Rāmāyaṇa
  - BhG. = Bhagavad Gītā
- Example: "As stated in the Mbh. (1.2.3)..."

### Italics:
- Use italics for Sanskrit terms only on **first mention**
- Subsequent mentions: Roman type (e.g., *sandhi* → sandhi)

---

## 6. Paragraph Structure

- Each paragraph must have **one clear main idea**
- Start with a **topic sentence**
- Follow with **2–4 supporting sentences** (evidence, analysis, examples)
- End with a **transition or "so what?" sentence**
- Keep paragraphs between **4–8 lines** (avoid very long or very short paragraphs)
- Use subheadings generously — never more than 2 pages without a subheading

---

## 7. Data Presentation (ACL/EMNLP Standard — Mandatory)

### Required Reporting:
- Always report:
  - Mean + standard deviation
  - 95% confidence intervals (use bootstrap)
  - Statistical significance (McNemar test, p-values)
- Never say "significantly better" without statistical test
- Present results in tables with clear column headers and units
- Always include baseline comparisons
- Report effect sizes where appropriate
- All numbers must match `thesis_verified_results.json`

### Figure/Table Captions:
- Structure: "Figure X: [Short description]. [Longer explanation of what the figure shows and why it matters for Sanskrit scholars]."
- Never leave figures/tables "speaking for themselves" — always discuss in text

---

## 8. Limitations Handling (Builds Credibility — Required)

### Rules:
- Always include a **dedicated Limitations section** (never hide limitations)
- Be honest but frame positively: "While this approach shows promise, it has the following limitations..."
- Never say "our model has no limitations" — this signals lack of maturity
- Connect limitations to future work
- Top papers openly discuss limitations — this builds reviewer trust

---

## 9. Scholarly Voice (How to Sound Like an Expert)

### Required:
- Use confident language: "We demonstrate that..." not "We try to show that..."
- Use "we" consistently (collaborative academic voice)
- Be direct: "This is a critical gap" not "This might be considered a gap"
- Vary sentence length — mix short punchy sentences with longer analytical ones
- Avoid: "In my opinion", "I think", "It seems to me"
- Avoid: "very", "really", "a lot" — use precise academic language
- Avoid contractions: "it is" not "it's"

---

## 10. Abstract Writing (250–300 words maximum — Most Important Part)

### Required Structure:
1. **Sentence 1–2:** Problem statement + motivation (connect to Sanskrit scholarship)
2. **Sentence 3–4:** Method + innovation (balanced regularisation)
3. **Sentence 5–7:** Key results with numbers + confidence intervals + statistical significance
4. **Sentence 8–9:** Contribution + scholarly impact (democratizing access to Sanskrit knowledge)
5. **Final sentence:** Strong, memorable statement about broader impact

### Rules:
- Never use citations in abstract
- End with a strong statement — this is what reviewers remember
- Write the abstract **last**, after all results are finalized

---

## 11. Conclusion Writing (Last 2 pages)

### Required Structure:
1. **First paragraph:** Restate contribution in 2–3 sentences (no numbers)
2. **Second paragraph:** Key findings with numbers + confidence intervals
3. **Third paragraph:** Limitations (honest but brief, 3–4 sentences maximum)
4. **Fourth paragraph:** Future work (specific, not generic — name datasets, tasks, applications)
5. **Final sentence:** Broader impact on Sanskrit scholarship

### Rules:
- Never start Conclusion with "In conclusion" or "To summarize"
- End with a forward-looking statement, not a summary
- Connect future work to real scholarly needs (e.g., manuscript OCR, Purāṇic corpora, educational tools)

---

## 12. Common Fatal Mistakes (Will Get Paper Rejected)

| Mistake | Wrong | Right |
|---------|-------|-------|
| Over-claiming | "Our model solves Sanskrit NER" | "Our model advances the state-of-the-art in Sanskrit NER" |
| Hedging too much | "It seems that our approach might help" | "Our approach demonstrably improves..." |
| No statistical tests | "Our model is better" | "Our model significantly outperforms baselines (p < 0.01, McNemar test)" |
| Weak abstract | Reviewers decide in 30 seconds | Make every word count |
| No limitations section | Signals lack of maturity | Always include Limitations |
| Generic future work | "Future work could explore X" | "Future work will integrate this model with manuscript OCR pipelines and evaluate on Purāṇic corpora" |
| Starting sentences with "And", "But", "So" | Informal | Never do this in academic writing |
| Using "very", "really", "a lot" | Vague | Use precise academic language |

---

## 13. Final Polish Checklist (Before Submission — Mandatory)

- [ ] Every claim has a citation (no unsupported assertions)
- [ ] No placeholder citations remain (`[Author et al., Year]`)
- [ ] All numbers match `thesis_verified_results.json`
- [ ] All confidence intervals and p-values are reported
- [ ] Sanskrit terms are consistently formatted (IAST + Devanagari where needed)
- [ ] Every section ends with a "so what?" for scholars
- [ ] No contractions
- [ ] No "very", "really", "a lot"
- [ ] All figures have scholar-focused captions
- [ ] Literature Review has clear critical analysis (not just description)
- [ ] Abstract is 250–300 words and follows required structure
- [ ] Conclusion has dedicated Limitations paragraph
- [ ] Future work is specific (names datasets, tasks, applications)
- [ ] Every chapter connects back to "democratizing access to Sanskrit knowledge"

---

## 14. Final Reminder

**This thesis is not just a technical exercise — it is a contribution to Sanskrit scholarship.**

Every sentence, every number, every citation must serve the purpose of making classical Sanskrit knowledge more accessible to scholars, students, and practitioners worldwide.

If a sentence does not serve this purpose, revise or remove it.

---

**END OF PUBLICATION-GRADE STYLE GUIDE**

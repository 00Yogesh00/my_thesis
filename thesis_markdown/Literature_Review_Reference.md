# Literature Review — Critical Analysis & Improvement Plan

**Chapter 2: Literature Review**  
**Date:** May 3, 2026  
**Current Status:** Draft 2 (Rewritten)  
**Score:** 7.2/10 (Improved but not yet publication-grade)

---

## Critical Analysis

### Overall Assessment

**Strengths:**
- Much better critical tone than previous version
- Good flow and transitions between sections
- Stronger positioning in Section 2.7 (Research Gap)
- Better connection to purpose in Introduction and Conclusion
- Section 2.3.3 includes key finding (dual benefit of balanced regularisation)

**Weaknesses:**
- Still too descriptive in several places (especially 2.2, 2.4, 2.5)
- Citations remain weak (many placeholders)
- Lacks scholarly depth in critical engagement
- Some sections feel repetitive (especially 2.3.3 and 2.6)
- Section 2.4 (NER in Sanskrit) is still too short and underdeveloped
- Section 2.8 (Summary) is too generic and adds little value

---

## Section-by-Section Critique

| Section | Rating | Main Issues |
|---------|--------|-------------|
| 2.1 Introduction | Good | Strong opening, good purpose connection. Minor repetition. |
| 2.2 Sanskrit as a Computational Language | Weak | Too textbook-like. Lacks critical analysis of why these features matter for NER specifically. |
| 2.3 Previous Work | Average | 2.3.1 and 2.3.2 are descriptive. 2.3.3 is better but repetitive with 2.6. |
| 2.4 NER in Sanskrit | Weak | Too short. Lacks specific examples of existing systems and their failures. |
| 2.5 Byte-Level Models | Good | Better, but could be more critical of limitations of ByT5. |
| 2.6 Multi-Task Learning | Average | Good explanation, but overlaps heavily with 2.3.3. |
| 2.7 Research Gap | Strong | Best section. Assertive and well-positioned. |
| 2.8 Summary | Weak | Generic. Adds almost no new insight. |

---

## Key Problems (Critical View)

1. **"Telling" instead of "Arguing"**  
   Many paragraphs describe what exists ("X did Y") rather than critiquing why it is insufficient ("While X achieved Y, it failed to address Z, which is critical because...").

2. **Weak Critical Engagement**  
   The review rarely challenges prior work. A strong Literature Review should identify not just gaps, but why those gaps matter and how they limit scholarly progress.

3. **Repetition**  
   Sections 2.3.3 and 2.6 cover very similar ground (multi-task learning + balanced regularisation). This should be consolidated.

4. **Underdeveloped Section 2.4**  
   NER in Sanskrit is the core topic of this thesis, yet this section is only ~250 words. It needs to be much more substantial.

5. **Generic Summary (2.8)**  
   The Summary should not just restate what was covered — it should synthesize insights and reinforce the motivation for this work.

---

## Prioritized Improvement Suggestions

### High Priority (Must Fix)

1. **Rewrite Section 2.4 (NER in Sanskrit)** — Make it 2–3x longer with specific examples of existing systems, their limitations, and why they fail for classical texts.

2. **Consolidate 2.3.3 and 2.6** — Merge the multi-task learning discussion into one coherent section to avoid repetition.

3. **Strengthen Critical Analysis** — Add more sentences like:
   - "However, this approach fails to..."
   - "A critical limitation is..."
   - "This gap is particularly problematic because..."

4. **Improve Section 2.8 (Summary)** — Make it more insightful. End with a strong statement about why this work matters.

### Medium Priority

5. Replace placeholder citations with real ones from `references.bib`
6. Add 1–2 recent papers (2023–2024) if possible
7. Ensure every major claim is followed by a citation

### Low Priority

8. Minor language refinement
9. Ensure consistent terminology (Sanskrit NLP vs SCL)

---

## Final Verdict

The current version is **structurally sound and better than before**, but it is still **not yet at the level expected for an M.Tech thesis** — particularly in critical depth and scholarly engagement.

**Recommendation:** Do not proceed to the next chapter yet. The Literature Review is too important to leave in its current state. Fix the major weaknesses (especially Sections 2.4, 2.3.3/2.6 consolidation, and 2.8) before moving forward.

---

**END OF CRITICAL ANALYSIS**

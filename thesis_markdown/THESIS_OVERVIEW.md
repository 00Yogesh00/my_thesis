# THESIS OVERVIEW — Named Entity Recognition For Sanskrit

**Title:** ByT5-Sanskrit with Balanced Regularization for Sanskrit Named Entity Recognition  
**Student:** Yogesh (24-14-15)  
**Supervisor:** Dr. S.V.S.S.N.V.G. Krishna Murthy  
**Institution:** DIAT Pune  
**Date:** May 2026

---

## The Truth First (Ground Reality)

When we approach learning Sanskrit or exploring ancient Indian knowledge, we encounter many difficulties.

A person who is not a Sanskrit scholar and wants to explore the ancient knowledge from Sanskrit texts faces a major problem:

In every domain imaginable — from spirituality and philosophy to science, medicine, statecraft, and performing arts — there exists profound Sanskrit literature. However, most people only get access to **translated versions**. 

A significant amount of meaning, depth, subtlety, and wisdom is lost in the process of translation. Many concepts in Sanskrit do not have direct equivalents in other languages, leading to oversimplification or distortion.

As a result, people cannot access the **original knowledge** directly from the source scriptures. They are forced to rely only on the **opinions and interpretations** of those who have read the texts.

**This is the real problem we are trying to address.**

---

## The Value of Sanskrit Scriptures

Sanskrit literature contains some of the most important contributions to human civilization:

**Foundational Spirituality & Philosophy**
- The Vedas, Upanishads, Bhagavad Gita, Yoga Sutras of Patanjali, Brahma Sutras

**Epics and Narrative Literature**
- Mahabharata, Ramayana, Panchatantra, Kathasaritsagara

**Science, Medicine, and Statecraft**
- Sushruta Samhita, Charaka Samhita, Arthashastra, Aryabhatiya, Aṣṭādhyāyī (by Pāṇini)

**Classical Poetry and Drama**
- Works by Kalidasa, Natyashastra, Gita Govinda

These texts have contributed immensely to human knowledge and continue to offer wisdom that can benefit the world today.

---

## Our Bigger Purpose

To contribute to **Sanskrit Computational Linguistics (SCL)** so that **every person** (students, researchers, practitioners of Yoga/Ayurveda, seekers of spirituality, and anyone interested in ancient wisdom) gains the right to access the **original knowledge and wisdom** from Sanskrit scriptures directly from the source — without losing meaning through translation.

---

## Why We Are Doing NER (Problem NER is Solving)

**The Core Problem:**
Even if someone learns basic Sanskrit or uses translation tools, they still struggle to navigate and extract meaningful information from large classical texts. Important entities (persons, locations, concepts, events) are often buried in complex narratives, making it difficult to trace relationships, understand context, or build structured knowledge.

**What NER Solves:**
Named Entity Recognition helps identify and classify key entities (PER, LOC, MISC) in Sanskrit texts. This enables:
- Better navigation of large texts (e.g., tracing characters across the Mahabharata)
- Structured knowledge extraction
- Improved search and annotation of classical literature
- Foundation for higher-level tasks (relation extraction, knowledge graphs, semantic search)

**Critical Note:**
NER alone does **not** solve the full problem of accessing Sanskrit knowledge. It is only one piece of the puzzle. However, it is a necessary and valuable step that has been relatively underexplored compared to other NLP tasks for Sanskrit.

---

## Key Innovation (Technical Contribution)

We fine-tuned **ByT5-Sanskrit** (a 594-million-parameter byte-level model) by adding **Named Entity Recognition (NER)** along with **Balanced Linguistic Regularisation** (15% Segmentation + Lemmatisation tasks).

**Why we chose ByT5-Sanskrit:**
- Byte-level tokenization handles Sanskrit's complex morphology and sandhi better than subword tokenizers.
- Pre-trained specifically on Sanskrit corpora, giving it strong foundational understanding.
- Efficient fine-tuning possible even with limited classical Sanskrit data.

**Why we added Balanced Regularisation:**
- Many researchers focus only on improving NER performance.
- We wanted the model to **learn NER while actively improving** its core Sanskrit capabilities (Segmentation and Lemmatisation).
- This helps the model stay grounded in Sanskrit language understanding rather than drifting toward generic behavior.

**Results:**
- Final NER micro-F1 = **0.852**
- Linguistic Capabilities: Segmentation = **85.0%**, Lemmatisation = **93.0%**
- Cross-domain performance on Pañcatantra: PROPN Recall = **73.4%**

---

## Current Status (May 3, 2026)

- Structure corrected (Nomenclature before Chapter 1)
- Introduction updated with clearer purpose
- Literature Review (Chapter 2) still needs significant work
- All other chapters acceptable but need qualitative Sanskrit examples

---

**Next Priority:**  
We are in the process of improving `THESIS_OVERVIEW.md` to ground ourselves properly before moving to Literature Review (Chapter 2).

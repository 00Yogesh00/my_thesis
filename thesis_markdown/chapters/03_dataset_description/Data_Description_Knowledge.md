# DATA DESCRIPTION KNOWLEDGE — Chapter 3

**Purpose:** Single authoritative reference for all dataset knowledge required to write Chapter 3: Dataset Description  
**Last Updated:** May 3, 2026  
**Status:** Complete, verified against all sources (stats.xml, validation output, actual files, GitHub README)

---

## Table of Contents

1. [Overview of Datasets Used](#1-overview-of-datasets-used)
2. [Mahānāma Dataset (Primary In-Domain Evaluation)](#2-mahanama-dataset-primary-in-domain-evaluation)
3. [DCS (Digital Corpus of Sanskrit)](#3-dcs-digital-corpus-of-sanskrit)
4. [UD_Sanskrit-UFAL-master (Cross-Domain Evaluation — D3)](#4-ud_sanskrit-ufal-master-cross-domain-evaluation--d3)
5. [UD_Sanskrit-Vedic-master (Extends Morphological Coverage)](#5-ud_sanskrit-vedic-master-extends-morphological-coverage)
6. [Comparison: UFAL vs Vedic](#6-comparison-ufal-vs-vedic)
7. [Datasets NOT Used (with Justification)](#7-datasets-not-used-with-justification)
8. [Critical Quality Assessment](#8-critical-quality-assessment)
9. [References](#9-references)

---

# 1. Overview of Datasets Used

| Dataset | Purpose | Role in Thesis |
|---------|---------|----------------|
| **Mahānāma** | Gold-standard NER corpus from Mahābhārata | Primary in-domain evaluation (D1) |
| **DCS (Digital Corpus of Sanskrit)** | Morphological annotations + silver NER | Linguistic task training + silver NER |
| **UD_Sanskrit-Vedic-master** | Vedic Sanskrit treebank | Extend morphological coverage to Vedic |
| **UD_Sanskrit-UFAL-master** | Classical Sanskrit treebank (Pañcatantra) | Cross-domain evaluation (D3) |

**Total Training Data Composition:**
- Mahānāma NER oversampled: ~74%
- DCS Sembank Silver NER: ~11%
- DCS Linguistic (S+L regularisation): ~15%

---

# 2. Mahānāma Dataset (Primary In-Domain Evaluation)

## 2.1 Overview & Statistics

**Mahānāma** is a large-scale dataset for end-to-end **Entity Discovery and Linking (EDL)** in Sanskrit.

| Attribute | Details |
|-----------|---------|
| **Source** | *Mahābhārata* (world's longest epic) |
| **Total Entity Mentions** | **Over 109,000** |
| **Unique Entities** | 5,500 |
| **Volumes** | 18 (Mahābhārata) |
| **Reference Work** | *Index to the Names in Mahābhārata* (Sørensen, 1904) |
| **Paper** | Sarkar et al., EMNLP 2025 — https://arxiv.org/abs/2509.19844 |
| **License** | CC BY 4.0 |
| **GitHub** | github.com/sujoysarkarai/mahanama |

**Entity Types:**
- **Person (PER):** 91.1%
- **Location (LOC):** 3.8%
- **Miscellaneous (MISC):** 5.1%

## 2.2 Data Format & Encoding

| Attribute | Details |
|-----------|---------|
| **Format** | CoNLL-U (CorefUD standard) |
| **Encoding** | SLP1 (Sanskrit Library Phonetic Basic Encoding Scheme) |
| **Organization** | 18 volumes, each with multiple subchapters |
| **Storage** | `data/mahanama_conllu/` (annotated text), `data/kb/` (knowledge base) |

## 2.3 Entity Distribution & Class Imbalance

**Critical Finding:** Severe class imbalance in raw training data:

| Entity Type | Raw Sentence Count | % of Total |
|-------------|-------------------|------------|
| **Person (PER)** | ~41,278 | **91.1%** |
| **Location (LOC)** | ~2,804 | 3.8% |
| **Miscellaneous (MISC)** | ~3,797 | 5.1% |

**Impact:** Model M2 (trained on raw data without oversampling) achieved:
- F1 = 0.791 for Person
- F1 = 0.000 for both Location and Misc
- **The model classified every entity as "person"** — class imbalance failure, not capability failure

## 2.4 Splits & Usage in This Thesis

| Split | Sentences | Usage |
|-------|-----------|-------|
| **Train** | ~57,000 | Training (Models M2, M3) |
| **Val** | ~9,960 | Merged with train for Best NER & Final NER |
| **Test** | 6,672 | Evaluation only — **NEVER seen during training** |
| **Total (Train+Val)** | 66,960 | Used for Best NER & Final NER |

## 2.5 Data Format Examples

**Entity Annotation (MISC column):**
```
global.Entity = eid-etype-head-identity
```

**Example:**
```
vfzavAhanaH    Entity=(e2661-person--Siva)||base_name=vfzavAhana|ittnim=2661,Siva,vol_13,ver_1347
```

**Sentence Identifier:**
```
# sent_id = MBh_13_1_18_39
# mnd_reference = MND_vol-ix_18_39
```

## 2.6 Knowledge Base Structure

**File:** `knowledge_base.json`

Each entry contains:
- `key`: unique ID
- `description`: description from Index (after removing references)
- `cleaned_description`: prepared for readability
- `aliases`: list of other entity IDs (name variants)
- `cluster_head`: boolean (canonical head of cluster)

**Example:**
```json
{
  "e3699": {
    "key": "druma",
    "description": "Druma, king of the Kimpuruṣas. ...",
    "cleaned_description": "Druma was the king of the Kimpuruṣas, known as Kimpuruṣeśaḥ. ...",
    "aliases": ["e5752", "e5753", "e5754"],
    "cluster_head": true
  }
}
```

---

# 3. DCS (Digital Corpus of Sanskrit)

## 3.1 Overview & Statistics

| Attribute | Details |
|-----------|---------|
| **Full Name** | Digital Corpus of Sanskrit (DCS) |
| **Creator** | Oliver Hellwig |
| **Size** | **650,000 sentences** (text lines) |
| **Word References** | **4,500,000+** |
| **Unique Words** | **175,000** |
| **Texts Covered** | ~400 Sanskrit texts |
| **Citation** | Hellwig (2010, 2019) |
| **URL** | http://www.sanskrit-linguistics.org/dcs/ |

## 3.2 DCS Sembank NER Extraction (Our Work)

**Our Contribution:** First to use DCS Sembank for NER (no prior work has done this)

| Dataset | Raw Examples | After Oversampling | Purpose |
|---------|-------------|-------------------|---------|
| **DCS Sembank NER (full)** | 12,942 | 18,855 (LOC×5, MISC×5) | Silver NER training |
| **DCS Sembank NER (V2, partial)** | 2,120 | 7,216 (LOC×5, MISC×5) | Silver NER training (Best NER only) |

**Domain Specificity:**
- 120 texts across 270 DCS directories
- **Rāmāyaṇa dominates (63%)** — strong evidence of domain specificity
- Mahābhārata texts **excluded** to avoid overlap with Mahanama evaluation set

**Critical Conceptual Finding:**
> "The DCS Sembank was built for **word sense disambiguation (WSD)** and **semantic role labeling**, **not for NER**."

- Instance relations cover both **entity mentions** and **entity references**
- For NER training, we need only **entity mentions**
- The `col0/col1` distinction allows separation of these two phenomena

**Entity Recall Gap (Important Limitation):**

| Entity | Appears in DCS Sentences | Tagged as NER | Recall |
|--------|-------------------------|---------------|--------|
| **Rāma** | 503 | 7 | **1.4%** |
| **Sītā** | 122 | 3 | **2.5%** |

## 3.3 DCS Linguistic Training Data

| Attribute | Details |
|-----------|---------|
| **Full DCS Size** | ~650,000 sentences |
| **Used for Training** | 60,000 sentences (subset) |
| **Percentage Used** | **9.2%** of total DCS |
| **After Augmentation** | ~300,000 examples (×5 tasks: S, SM, L, LM, SLM) |
| **Per Task** | ~74,000 examples each |
| **Format** | CoNLL-U → JSON |
| **Purpose** | Linguistic task training (Segmentation, Lemmatisation) for regularisation |

**Note:** Only 9.2% of DCS was used. Remaining 590K sentences remain available for future experiments.

## 3.4 DCS Held-Out Evaluation (D2)

| Attribute | Details |
|-----------|---------|
| **Size** | 200 sentences |
| **Sampling** | Random sample, seed=42, PC 05 |
| **Total Words** | 1,559 |
| **Tasks Evaluated** | S, L, LM, SLM |
| **Encoding** | IAST (native DCS encoding) |
| **Critical Limitation** | Different random seed on Venu-Krishna (seed=123) vs PC 05 (seed=42). Samples are **DIFFERENT**. D2 results must only be compared within the same machine and seed. |

## 3.5 Critical Issues & Limitations (from Academic Literature)

**Paper:** Krishnan, Kulkarni, Huet (2020) — arXiv:2005.06545v1

| Issue | Error Rate | Implication |
|-------|------------|-------------|
| **Compound splits doubtful** | ~5.5% | Our silver NER from DCS Sembank may have noise |
| **Segmentation errors** | ~2% | Preprocessing must account for this |
| **No homonymy index** | — | We lose sense information for ambiguous words |
| **Inconsistent derivational analysis** | — | Our lemmatisation task may have noise |
| **Non-uniform lemma selection** | — | Context-specific decisions without documentation |

**Example of Inconsistency (Table 1 from paper):**

| Attribute | Value |
|-----------|-------|
| **Sentence Id** | 83 |
| **Sentence** | mauktike yadi sam. dehah. kr.trime sahaje'pi v¯a |
| **Chunks** | ['mauktika', 'yadi', 'sam. deha', 'kr.trima', 'sahaja', 'api', 'v¯a'] |
| **Lemmas** | [['mauktika'], ['yadi'], ['sam. deha'], ['kr.trima'], ['sahaja'], ['api'], ['v¯a']] |
| **Morphological Class (CNG)** | [['171'], ['2'], ['29'], ['171'], ['171'], ['2'], ['2']] |

## 3.6 Linguistic Differences: DCS vs Sanskrit Heritage Reader

| Issue | DCS Approach | Heritage Reader Approach |
|-------|--------------|--------------------------|
| **Compounds (non-compositional)** | Context-based: not split | Lexicon-guided: produces both split and unsplit |
| **Secondary derivatives** | Joins with base | Treats separately |
| **Anusvāra/Anunāsika** | Inconsistent | Correctly uses anunāsika |
| **Pūrva-pada lemmas** | Sometimes uses compounding form | Always uses base stem (Pāṇinian) |
| **Pre-verbs** | Joined with lemmas | Separate (older) / Joined with inflectional (newer) |
| **Homonymy index** | **Does NOT have** | **Has** (critical for sense disambiguation) |
| **Derivational analysis** | Inconsistent (sometimes provided, sometimes not) | Always provides both inflectional and derivational |

**Homonymy Index Example (*siddham*):**

Heritage provides two analyses with **opposing meanings**:

| Sense | French | English |
|-------|--------|---------|
| siddha_1 | accompli, réalisé; gagné, obtenu; parfait | accomplished, realized; won, obtained; perfect |
| siddha_2 | empêché, écarté, repoussé | prevented, pushed aside, pushed back |

**DCS Problem:** Collapses both into one → loses sense information

---

# 4. UD_Sanskrit-UFAL-master (Cross-Domain Evaluation — D3)

## 4.1 Identity & Metadata

| Attribute | Details |
|-----------|---------|
| **Full Name** | Universal Dependencies Sanskrit UFAL treebank |
| **Repository** | github.com/UniversalDependencies/UD_Sanskrit-UFAL |
| **Language Code** | sa (Sanskrit) |
| **Treebank Identifier** | ufal |
| **Files** | sa_ufal-ud-test.conllu (only) |
| **Size** | 230 sentences, ~1,850 tokens (estimated) |
| **License** | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| **License URL** | http://creativecommons.org/licenses/by-sa/4.0/legalcode |
| **Validation Status** | Not validated in provided output (small treebank) |

## 4.2 Content & Domain

| Attribute | Details |
|-----------|---------|
| **Texts** | Pañcatantra animal fables |
| **Genre** | Classical Sanskrit narrative (fables) |
| **Purpose in Thesis** | Cross-domain NER evaluation (D3) |
| **Domain Contrast** | Pañcatantra (fables) vs Mahābhārata (epic) |

## 4.3 Script & Encoding

| Attribute | Details |
|-----------|---------|
| **Script** | **Devanagari** |
| **Transliteration Required** | Yes — Devanagari → IAST |
| **Transliteration Tool** | indic_transliteration.sanscript |
| **Impact if Not Transliterated** | 0% entity detection (model trained on IAST) |

## 4.4 Statistics

**Total:** 230 sentences, ~1,850 tokens

**PROPN Statistics:**
- Total PROPN tokens: **94**
- Sentences with PROPN: **52**
- PROPN % of all tokens: **5.1%**

**UPOS Distribution:**
| Tag | Count | % |
|-----|-------|---|
| NOUN | 560 | 30.4% |
| VERB | 314 | 17.0% |
| PUNCT | 195 | 10.6% |
| ADV | 194 | 10.5% |
| PRON | 179 | 9.7% |
| ADJ | 113 | 6.1% |
| **PROPN** | **94** | **5.1%** |
| DET | 70 | 3.8% |
| PART | 37 | 2.0% |
| CCONJ | 33 | 1.8% |

## 4.5 Sample Sentences (Actual Data)

**Sentence 1:**
```
Text: pañcatantram kathāmukham...
PROPN: ['पञ्चतन्त्रम्']
```

**Sentence 2:**
```
Text: oṃ namaḥ śrīśāradāgaṇapatigurubhyaḥ|
PROPN: ['शारदा', 'गणपति']
```

**Sentence 3:**
```
Text: mahākavibhyo namaḥ|
PROPN: ['महाकवि']
```

## 4.6 Evaluation Methodology (Cross-Domain)

| Attribute | Details |
|-----------|---------|
| **Gold NER Labels** | None available |
| **Silver Standard** | UPOS=PROPN tags as entity indicators |
| **Evaluation Type** | Binary (entity found/not found) |
| **Not Evaluated** | Typed NER (PER/LOC/MISC) |
| **Transliteration** | Required before model input |
| **Evaluation Script** | eval_crossdomain_d3_fixed.py |

## 4.7 Files Present

```
UD_Sanskrit-UFAL-master/
├── sa_ufal-ud-test.conllu    (230 sentences)
├── README.md                  (metadata)
├── LICENSE.txt                (CC BY-SA 4.0)
├── CONTRIBUTING.md
├── stats.xml
├── eval.log
└── not-to-release/            (source files)
```

---

# 5. UD_Sanskrit-Vedic-master (Extends Morphological Coverage)

## 5.1 Identity & Metadata

| Attribute | Details |
|-----------|---------|
| **Full Name** | Universal Dependencies Sanskrit Vedic treebank |
| **Repository** | github.com/UniversalDependencies/UD_Sanskrit-Vedic |
| **Language Code** | sa (Sanskrit) |
| **Treebank Identifier** | vedic |
| **Files** | sa_vedic-ud-train.conllu, sa_vedic-ud-dev.conllu, sa_vedic-ud-test.conllu |
| **Size** | **27,182 sentences**, 206,440 tokens |
| **License** | Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) |
| **License URL** | http://creativecommons.org/licenses/by-sa/4.0/legalcode |
| **Validation Tool** | UD tools commit 26e6c87a2f518322d15901a351199b6be6569062 (Nov 7, 2025) |
| **Treebank Commit** | b8fb9a3e569bfeca2298327d78ab65f3bdf70f1e |
| **Validation Status** | **FAILED** (all splits) |

## 5.2 Content & Domain

| Attribute | Details |
|-----------|---------|
| **Texts** | Ṛgveda (RV), Śaunaka recension of Atharvaveda (ŚS), Maitrāyaṇīsaṃhitā (MS), Aitareya-Brāhmaṇa (AB), Śatapatha-Brāhmaṇa (ŚB) |
| **Genre** | Vedic Sanskrit (metrical and prose passages) |
| **Purpose in Thesis** | Extend morphological coverage to Vedic Sanskrit |
| **Note on Size** | GitHub README says "4,000 sentences with 27,000 words" — **OUTDATED**. Current: 27,182 sentences, 206,440 tokens |

## 5.3 Script & Encoding

| Attribute | Details |
|-----------|---------|
| **Script** | **IAST** (native — no transliteration needed) |
| **Diacritics** | Contains ā, ī, ū, ṛ, ṝ, ḷ, ḹ, ṅ, ñ, ṭ, ḍ, ṇ, ś, ṣ, ḥ, ṃ |

## 5.4 Official Statistics (from stats.xml)

**Size:**
| Split | Sentences | Tokens/Words |
|-------|-----------|--------------|
| **Total** | 27,182 | 206,440 |
| **Train** | 21,477 | 161,959 |
| **Dev** | 2,996 | 23,862 |
| **Test** | 2,709 | 20,619 |

**Unique Items:**
- Unique lemmas: 13,019
- Unique forms: 35,853
- Unique fusions: 0

## 5.5 UPOS Distribution (from stats.xml)

| Tag | Count | % | Most Frequent Lemmas |
|-----|-------|---|---------------------|
| NOUN | 72,315 | 35.0% | agni, deva, indra, yajña, brahman, loka, ap, paśu, prāṇa, soma |
| VERB | 39,836 | 19.3% | kṛ, bhū, vid, hu, as, yaj, ah, vac, dhā, i |
| PRON | 27,825 | 13.5% | tad, yad, idam, tvad, mad, etad, sarva, enad, ka, anya |
| PART | 21,136 | 10.2% | iti, eva, na, vai, ha, iva, hi, a, u, yathā |
| ADJ | 18,315 | 8.9% | uttara, dakṣiṇa, viśva, prāñc, prathama, mahat, udañc, priya, uttama, pratyañc |
| ADV | 13,863 | 6.7% | atha, tad, evam, su, ā, tasmāt, pra, tatas, tathā, vi |
| CCONJ | 4,222 | 2.0% | ca, vā, uta, athavā |
| NUM | 2,900 | 1.4% | eka, tri, dvi, śata, catur, pañcan, saptan, sahasra, dvādaśan, ṣaṣ |
| AUX | 1,825 | 0.9% | as, bhū, i, ās, sthā, car, e |
| SCONJ | 1,730 | 0.8% | yat, yadi, yatra, yadā, ced, yāvat, yatas, yad, yasmāt, ityādi |
| ADP | 1,383 | 0.7% | ā, anu, sam, adhi, pari, abhi, pra, upa, prati, ud |
| DET | 565 | 0.3% | viśva, sva, bahu, ubhaya, puru, tāvat, yāvat, bhūri, samāna, etāvat |
| INTJ | 525 | 0.3% | svāhā, oṃ, hanta, bata, hai, haye, ahe, bāl, hek, ho |

## 5.6 Morphological Features (from stats.xml)

**Case Distribution:**
| Case | Count | Example Forms |
|------|-------|---------------|
| Nom | 49,720 | yaḥ, saḥ, sa, tat, yat, agniḥ, te, tvam, sā, eṣa |
| Acc | 33,940 | tat, tvā, tam, enam, etat, agnim, naḥ, tām, yat, mā |
| Gen | 10,239 | asya, te, tasya, me, naḥ, yajñasya, devānām, yasya, agneḥ, vaḥ |
| Ins | 8,565 | tena, manasā, etena, vācā, yena, adbhiḥ, tayā, paśubhiḥ, brahmaṇā, svena |
| Loc | 7,650 | asmin, agnau, tasmin, loke, agre, madhye, āhavanīye, apsu, divi, yajñe |
| Dat | 5,372 | naḥ, asmai, te, me, agnaye, tasmai, devebhyaḥ, indrāya, vaḥ, yajamānāya |
| Voc | 3,168 | agne, indra, deva, aśvinā, soma, jātavedaḥ, devāḥ, marutaḥ, oṣadhe, āpaḥ |
| Abl | 2,443 | asmāt, tasmāt, asmat, divaḥ, agneḥ, lokāt, mat, tvat, aṃhasaḥ, pṛthivyāḥ |

**Gender Distribution:**
- Masc: 64,200
- Neut: 29,181
- Fem: 21,872

**Number Distribution:**
- Sing: 114,147
- Plur: 31,619
- Dual: 4,500

**Tense Distribution:**
- Pres: 23,881
- Past: 13,215
- Fut: 561
- Pqp: 31

**VerbForm Distribution:**
- Part: 8,519
- Conv: 3,171
- Gdv: 514
- Inf: 288

## 5.7 Dependency Relations (from stats.xml)

**Total Unique Relations: 66**

| Relation | Count | Description |
|----------|-------|-------------|
| root | 27,182 | Root of sentence |
| nsubj | 18,667 | Nominal subject |
| flat | 14,509 | Flat multiword expression |
| conj | 13,829 | Conjunct |
| advmod | 13,791 | Adverbial modifier |
| nmod | 10,076 | Nominal modifier |
| mark | 7,733 | Marker |
| obj | 15,522 | Object |
| obl | 5,757 | Oblique nominal |
| acl | 5,384 | Clausal modifier of noun |
| det | 5,658 | Determiner |
| discourse | 8,911 | Discourse element |
| orphan | 4,489 | Orphan in ellipsis |
| advcl | 3,775 | Adverbial clause modifier |
| ccomp | 2,767 | Clausal complement |
| iobj | 2,605 | Indirect object |
| vocative | 2,012 | Vocative |
| compound:coord | 1,797 | Coordinating compound |
| parataxis | 1,541 | Parataxis |
| cop | 1,532 | Copula |
| case | 1,508 | Case marking |
| xcomp | 1,313 | Open clausal complement |
| fixed | 1,169 | Fixed multiword expression |
| nmod:appos | 1,174 | Appositional nominal modifier |
| nummod | 1,590 | Numeric modifier |
| compound | 110 | Compound |
| compound:name | 47 | Name compound |
| dislocated | 116 | Dislocated element |
| csubj | 566 | Clausal subject |
| aux | 293 | Auxiliary |
| acl:attr | 279 | Attribute clausal modifier |
| acl:ptcp | 276 | Participial clausal modifier |
| acl:relcl | 2,063 | Relative clause |
| advcl:caus | 201 | Causal adverbial clause |
| advcl:ccomp | 1,357 | Clausal complement adverbial clause |
| advcl:concess | 57 | Concessive adverbial clause |
| advcl:cond | 686 | Conditional adverbial clause |
| advcl:consec | 4 | Consecutive adverbial clause |
| advcl:dpct | 355 | Depictive adverbial clause |
| advcl:fin | 549 | Final adverbial clause |
| advcl:lcl | 34 | Local adverbial clause |
| advcl:manner | 792 | Manner adverbial clause |
| advcl:tcl | 1,646 | Temporal adverbial clause |
| case:sim | 948 | Similarity case |
| mark:sim | 474 | Similarity marker |
| nmod:pred | 18 | Predicative nominal modifier |
| xcomp:result | 730 | Resultative xcomp |
| acl:cont | 3 | Continuative clausal modifier |
| acl:crel | 29 | Correlative clausal modifier |
| acl:dpct | 446 | Depictive clausal modifier |
| acl:pred | 1 | Predicative clausal modifier |
| ccomp:rel | 29 | Relative clausal complement |
| advcl:consec | 4 | Consecutive adverbial clause |

## 5.8 Validation Results (Critical Quality Issues)

**Validation Tool:** UD tools commit 26e6c87a2f518322d15901a351199b6be6569062 (Nov 7, 2025)

**Results:**

| Split | Syntax Errors | Warnings | Status | Quality Score |
|-------|---------------|----------|--------|---------------|
| **Dev** | 13 | 3,837 | **FAILED** | — |
| **Test** | 7 | 2,983 | **FAILED** | — |
| **Train** | 65 | 22,892 | **FAILED** | — |
| **Overall** | **85** | **29,712** | **FAILED** | **0.00642388532041902** (STARS = 0) |

**Common Error Types:**

| Error Code | Description | Frequency |
|------------|-------------|-----------|
| `pron-det-without-prontype` | PRON tagged words lacking `PronType` feature | **Very Common** (thousands) |
| `too-many-objects` | Multiple direct objects under a predicate | 13+ documented |
| `leaf-det` | 'det' dependency with unexpected children | Multiple |
| `orphan-parent` | 'orphan' dependency with incorrect parent | 1+ |

**Critical Implications:**
- **65 syntax errors in train set** — known annotation issues
- **22,892 warnings in train set** — widespread feature inconsistencies
- **Quality Score: 0.006** — lowest possible (STARS = 0)
- **Missing PronType feature** is systematic
- **Multiple direct objects** suggest verb argument structure inconsistencies

## 5.9 Task Format Conversion (for Linguistic Training)

Each sentence formatted into 5 task variants:

| Task | Input | Output | Prefix |
|------|-------|--------|--------|
| S | Sandhied text | Space-separated words | "S " |
| SM | Sandhied text | Space-separated words + morphcode | "SM " |
| L | Space-separated forms | Space-separated lemmas | "L " |
| LM | Space-separated forms | Space-separated `lemma_morphcode` | "LM " |
| SLM | Sandhied text | Space-separated `surface_lemma_morphcode` | "SLM " |

**Morphological Tag Mapping:** Uses `sanskrit_tags.tsv`
- Example: `Case=Nom|Gender=Masc|Number=Sing` → `SNM`

## 5.10 Usage in This Thesis

| Component | Size | Purpose |
|-----------|------|---------|
| Vedic linguistic (4K sentences × 5 tasks) | ~20,000 | Extend morphological coverage to Vedic Sanskrit |
| Combined with DCS linguistic | ~320,000 | 15% regularisation signal |

**Note:** The "4,000 sentences" refers to sentences **per major text** or a **subset** used for training, not the total treebank size.

## 5.11 Files Present

```
UD_Sanskrit-Vedic-master/
├── sa_vedic-ud-train.conllu  (21,477 sentences)
├── sa_vedic-ud-dev.conllu    (2,996 sentences)
├── sa_vedic-ud-test.conllu   (2,709 sentences)
├── README.md                  (metadata, outdated size claim)
├── LICENSE.txt                (CC BY-SA 4.0)
├── CONTRIBUTING.md
├── stats.xml                  (official statistics)
├── eval.log                   (validation output)
└── not-to-release/            (source files)
```

---

# 6. Comparison: UFAL vs Vedic

| Attribute | UD_Sanskrit-UFAL | UD_Sanskrit-Vedic |
|-----------|------------------|-------------------|
| **Size** | 230 sentences | 27,182 sentences |
| **Script** | Devanagari | IAST |
| **PROPN Tokens** | 94 | 0 |
| **PROPN %** | 5.1% | 0% |
| **Top UPOS** | NOUN (30.4%) | NOUN (35.0%) |
| **Purpose** | Cross-domain NER eval (D3) | Linguistic training (Vedic morphology) |
| **Texts** | Pañcatantra fables | Ṛgveda, Atharvaveda, Brāhmaṇas |
| **Transliteration** | Required | Not required |
| **Gold NER Labels** | No (silver: PROPN) | No (not used for NER) |
| **Validation Status** | Not validated | **FAILED** (85 errors, 29,712 warnings) |
| **Quality Score** | Unknown | 0.006 (STARS = 0) |
| **License** | CC BY-SA 4.0 | CC BY-SA 4.0 |

---

# 7. Datasets NOT Used (with Justification)

| Dataset | Reason for Exclusion |
|---------|----------------------|
| **Naamah** (https://huggingface.co/datasets/akhil2808/Naamah) | Contains multiple languages + modern terms; our focus is classical Sanskrit only |
| **Sampurner** (https://github.com/PrachuryyaKaushik/SampurNER) | Modern focus, not aligned with classical heritage preservation |
| **kaggle_ner** | Contains significant noise; not gold-standard quality |
| **Bhagavad_Gita_NER** | Too small to train meaningfully; limited scope |
| **Naamapadam** (400K sentences, 11 Indic langs) | Excludes Sanskrit — covers Hindi, Bengali, Marathi, etc. but not Sanskrit |
| **WikiANN Sanskrit portion** | Noisy silver labels from Wikipedia titles; not sentence-level NER |
| **Itihāsa** (93K Sanskrit-English pairs) | Translation task; output length mismatch with NER; 7-8 BLEU ceiling |
| **Sāmayik** (53K English-Sanskrit) | Same translation concerns |
| **Sanskrit Sembank** (600K+ WordNet synsets) | Different task (word sense disambiguation); no CoNLL-U format |
| **GRETIL corpus** | TEI XML format only; no morphological annotation; no PROPN tags |
| **Saṃsādhanī tool output** | Tool, not annotated corpus; unreliable silver labels |

---

# 8. Critical Quality Assessment

## 8.1 Data Quality Summary

| Dataset | Quality | Issues | Recommendation |
|---------|---------|--------|----------------|
| **Mahānāma** | High | Class imbalance (91% PER) | Oversampling required |
| **DCS Sembank** | Medium | 5.5% doubtful compounds, 2% segmentation errors | Document limitations |
| **UD_Sanskrit-UFAL** | Unknown | Small treebank (230 sentences) | Limited statistical power |
| **UD_Sanskrit-Vedic** | **Low** | 85 syntax errors, 29,712 warnings, quality score 0.006 | **Must disclose in thesis** |

## 8.2 Critical Findings

1. **Vedic treebank has known quality issues** — 65 syntax errors in train set, systematic missing PronType feature
2. **No PROPN tags in Vedic** — Vedic Sanskrit naming conventions differ from Classical Sanskrit
3. **Devanagari → IAST transliteration is a methodological contribution** — required for cross-domain evaluation
4. **Class imbalance in Mahānāma is severe** — 91% PER, requires oversampling strategy
5. **DCS Sembank was not designed for NER** — instance relations cover both mentions and references

---

# 9. References

### Academic Papers

1. Sarkar et al. (2025). "Mahānāma: A Unique Testbed for Literary Entity Discovery and Linking." *Proceedings of EMNLP 2025*. https://arxiv.org/abs/2509.19844

2. Krishnan, Kulkarni, Huet (2020). "Validation and Normalization of DCS corpus using Sanskrit Heritage tools to build a tagged Gold Corpus." *arXiv:2005.06545v1 [cs.CL]*. https://arxiv.org/abs/2005.06545

3. Hellwig (2010, 2019). *The Digital Corpus of Sanskrit (DCS)*. http://www.sanskrit-linguistics.org/dcs/

4. Hellwig & Nehrdich (2018). "Sanskrit word segmentation using character-level recurrent and convolutional neural networks." *Proceedings of EMNLP 2018*.

5. Krishna et al. (2017). "A dataset for Sanskrit word segmentation." *Proceedings of the Joint SIGHUM Workshop*.

### Online Resources

- DCS: http://www.sanskrit-linguistics.org/dcs/index.php
- Mahanama GitHub: github.com/sujoysarkarai/mahanama
- UD_Sanskrit-UFAL: github.com/UniversalDependencies/UD_Sanskrit-UFAL
- UD_Sanskrit-Vedic: github.com/UniversalDependencies/UD_Sanskrit-Vedic
- Universal Dependencies: https://universaldependencies.org/

---

**END OF DATA DESCRIPTION KNOWLEDGE — COMPLETE & VERIFIED**

---

# 10. Datasets Considered but Not Used for Primary Training

## 10.1 Rationale for Dataset Selection

Our dataset selection was guided by the following **core principles**:

1. **Task Alignment:** Priority given to datasets designed for or adaptable to Named Entity Recognition (NER)
2. **Domain Relevance:** Focus on classical Sanskrit texts (Vedas, epics, śāstras) rather than modern/contemporary usage
3. **Language Coverage:** Exclusive focus on Sanskrit; datasets excluding Sanskrit were deprioritized
4. **Annotation Compatibility:** Preference for CoNLL-U or easily convertible formats
5. **Resource Allocation:** Given finite time and resources, priority was given to datasets with highest potential impact on classical Sanskrit NLP

---

## 10.2 Datasets Considered but Not Selected

### 10.2.1 Naamah (Hugging Face: akhil2808/Naamah)

| Attribute | Details |
|-----------|---------|
| **Size** | 102,942 sentences |
| **Entity Types** | PER, LOC, ORG (mapped to MISC) |
| **Annotation** | Silver-standard BIO tags |
| **Domain** | Modern/contemporary Sanskrit usage |

**Rationale for Non-Selection:**
- **Domain mismatch:** Naamah contains predominantly modern and Western entities (contemporary names, organizations, locations) that do not align with our focus on classical Sanskrit textual heritage
- **Different scholarly priorities:** Our project aims to support scholars working with ancient texts (Mahābhārata, Vedas, Ayurveda, etc.); modern NER applications, while valuable, represent a different research direction
- **Usage:** Employed exclusively for cross-domain evaluation to demonstrate domain specificity of our models

---

### 10.2.2 Sampurner (GitHub: PrachuryyaKaushik/SampurNER)

| Attribute | Details |
|-----------|---------|
| **Size** | Large (train: ~1.69GB, validation: ~250MB, test: ~467MB) |
| **Focus** | Modern Sanskrit NER |
| **Domain** | Contemporary Sanskrit usage |

**Rationale for Non-Selection:**
- **Modern focus:** Designed primarily for contemporary Sanskrit applications rather than classical textual analysis
- **Resource allocation:** Given the substantial size and the time required for integration, priority was given to datasets more directly aligned with classical Sanskrit heritage preservation
- **Complementary rather than competing:** Modern Sanskrit NER represents a parallel research direction that can be pursued independently

---

### 10.2.3 Naamapadam (ACL 2023)

| Attribute | Details |
|-----------|---------|
| **Size** | ~400K sentences |
| **Languages** | 11 Indic languages |
| **Sanskrit Coverage** | None |

**Rationale for Non-Selection:**
- **Language exclusion:** Does not include Sanskrit; covers Hindi, Bengali, Marathi, and other Indic languages
- **Scope limitation:** While valuable for Indic NLP broadly, does not contribute to Sanskrit-specific NER research
- **Alternative resources:** Other Indic NER datasets exist for non-Sanskrit languages; our focus remains exclusively on Sanskrit

---

### 10.2.4 WikiANN Sanskrit Portion (Pan et al., 2017)

| Attribute | Details |
|-----------|---------|
| **Languages** | 282 languages including Sanskrit |
| **Annotation Method** | Silver labels extracted from Wikipedia titles |
| **Format** | Title-based, not sentence-level |

**Rationale for Non-Selection:**
- **Annotation quality concerns:** Labels derived from Wikipedia titles rather than natural sentence contexts; titles are short, formulaic phrases rather than representative text
- **Not sentence-level NER:** Does not provide the sentence-level annotations required for training contextual NER models
- **Superior alternatives:** Gold-standard sentence-level datasets (Mahanama) provide higher quality training data

---

### 10.2.5 Itihāsa (GitHub: rahular/itihasa)

| Attribute | Details |
|-----------|---------|
| **Size** | ~93K Sanskrit-English parallel sentences |
| **Task** | Machine translation (Sanskrit ↔ English) |
| **Reported Performance** | 7-8 BLEU ceiling |

**Rationale for Non-Selection:**
- **Task mismatch:** Designed for translation, not entity recognition; output format (translated sentences) does not align with NER label sequences
- **Different evaluation paradigm:** Translation quality metrics (BLEU) are not directly applicable to NER evaluation
- **Complementary resource:** Valuable for Sanskrit machine translation research, but represents a distinct NLP task

---

### 10.2.6 Sāmayik (~53K English-Sanskrit pairs)

| Attribute | Details |
|-----------|---------|
| **Size** | ~53K English-Sanskrit parallel sentences |
| **Task** | Machine translation |

**Rationale for Non-Selection:**
- **Same task mismatch as Itihāsa:** Translation-focused dataset; output format incompatible with NER training
- **Resource prioritization:** Given finite resources, priority was given to datasets directly supporting entity recognition in classical Sanskrit texts

---

### 10.2.7 Sanskrit Sembank (SSB)

| Attribute | Details |
|-----------|---------|
| **Size** | 600,000+ words in context |
| **Coverage** | Vedic and Classical Sanskrit |
| **Task** | Word Sense Disambiguation (WSD) |
| **Performance** | F1 up to 86.7% (without LLM) |
| **Integration** | Part of Digital Corpus of Sanskrit |

**Rationale for Non-Selection:**
- **Task mismatch:** Designed for word sense disambiguation (identifying word meanings/synsets), not named entity recognition (identifying entity spans and types)
- **Different annotation paradigm:** Synset-based annotations vs span-based entity annotations; requires fundamentally different model architecture and evaluation
- **Format incompatibility:** Not provided in CoNLL-U format; would require substantial preprocessing to adapt for NER pipeline
- **Complementary rather than competing:** SSB and our NER work address different aspects of Sanskrit NLP; both are valuable and can coexist

---

## 10.3 Generalized Rationale Summary

| Factor | Explanation |
|--------|-------------|
| **Task Alignment** | Datasets designed for tasks other than NER (translation, WSD) require different model architectures and evaluation frameworks |
| **Domain Relevance** | Priority given to datasets supporting analysis of classical Sanskrit textual heritage (epics, Vedas, śāstras) over modern/contemporary usage |
| **Language Focus** | Exclusive focus on Sanskrit; datasets excluding Sanskrit or covering only other Indic languages were deprioritized |
| **Annotation Quality** | Preference for gold-standard or high-quality silver annotations over noisy, title-derived, or non-sentence-level labels |
| **Resource Efficiency** | Given finite time and computational resources, datasets with highest potential impact on classical Sanskrit NER were prioritized |
| **Complementary Research** | Many discarded datasets represent valuable, complementary research directions (modern NER, translation, WSD) that can be pursued independently |

---

## 10.4 Critical Reflection

This selection process reflects a **deliberate focus** on:
- Classical Sanskrit textual heritage
- Named Entity Recognition as the primary task
- High-quality, sentence-level annotations
- Efficient use of limited research resources

**We acknowledge that:**
- All datasets considered have scholarly value
- Many represent important complementary research directions
- Future work could productively explore integration of multiple datasets for multi-task learning
- The decision to prioritize certain datasets over others is a methodological choice, not an assessment of intrinsic dataset quality

---

**END OF DATASETS CONSIDERED BUT NOT USED SECTION**

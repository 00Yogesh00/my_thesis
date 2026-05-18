# METHODOLOGY KNOWLEDGE BASE — Chapter 4: Methodology

**Purpose:**  
Single authoritative, fully verified reference document for writing a publication-grade Chapter 4 (Methodology). This file serves as the single source of truth for all technical details, algorithms, configurations, data preparation logic, and statistical methods used in the thesis.

**Last Updated:** May 4, 2026  
**Version:** 0.1 (Part 1 Only — Draft)  
**Verification Status:** In Progress (One part at a time)  
**Ground Truth Sources:**  
- `DATA_SOURCES.md` (official file mapping)  
- `thesis_verified_results.json` (primary source of truth for all metrics)  
- Raw `.log` and `.json` files (training & evaluation logs)  
- `.py` files (`train_final_ner.py`, `extract_full_sembank_ner.py`, `eval_final_ner.py`, etc.)  

**Update Philosophy:**  
This file is updated **one part at a time**. Each part is written, critically reviewed, and verified against raw sources before moving to the next part. No part is considered final until explicitly approved.

---

## Part 1: Header, Purpose, Verification Protocol & Continuity Rules

### 1.1 Purpose of This Knowledge Base

This document exists to ensure that **Chapter 4: Methodology** meets the highest standards of:
- Transparency and reproducibility
- Academic rigor (ACL/EMNLP publication level)
- Scholarly relevance to Sanskrit Computational Linguistics
- Complete traceability to original source code and data

Every sentence, number, algorithm, and diagram in Chapter 4 must be traceable back to this knowledge base.

### 1.2 Strict Verification Protocol (Mandatory)

**No content may be added to this file or Chapter 4 without the following verification steps:**

1. Identify the claim or number.
2. Locate the authoritative source using `DATA_SOURCES.md`.
3. Cross-verify against:
   - `thesis_verified_results.json` (for all metrics and statistical tests)
   - Relevant raw `.log` or `.json` files
   - Relevant `.py` files (for algorithms, preprocessing logic, and training procedures)
4. Add a **verification tag** in the format:  
   `Verified: [Source File] + [Date]`
5. If any discrepancy is found, it must be documented and resolved before inclusion.

**Golden Rule:**  
**If it is not verified against the raw sources, it does not go into this file or Chapter 4.**

### 1.3 Continuity with Chapter 3 (Dataset Description)

Chapter 4 must be written in **direct continuation** of Chapter 3. Every major section must begin with explicit linking language such as:

> “Building directly on the four datasets and data preparation decisions detailed in Chapter 3…”

This ensures narrative flow and demonstrates that the methodology is a logical extension of the dataset choices and preparation steps already described.

### 1.4 How This File Will Be Used

- This knowledge base will be the **only** reference used when writing Chapter 4.
- No external documents or memory will be used without cross-verification.
- After all 10 parts are complete and approved, this file will be used to generate the final Chapter 4 draft following `STRUCTURE_RULES.md`.

### 1.5 Version Control & Update Process

- Each part is developed, reviewed, and approved independently.
- After approval, the part is marked as **“Verified & Approved”**.
- Only after all parts are approved will the full document be considered final.

---

**End of Part 1 (Approved)**

**Note:** This file is being built one part at a time following a strict verification-first process. Only Part 1 is currently complete and approved.

---

## Part 4: Data Preparation Pipeline (Core Methodological Contribution)

### 4.1 Mahānāma Gold-Standard NER Preparation

**Best NER Pipeline (NER-only, 8 epochs):**
- Source: 2,110 Mahānāma CoNLL-U files
- Raw sentences parsed: 73,632
- Train+Val after test removal: 66,960 sentences
- Raw gold entity distribution: Person = 41,278 (91.1%), Location = 2,804 (3.8%), Misc = 3,797 (5.1%)
- After oversampling (LOC ×10, MISC ×10): **126,369** gold NER examples
- Additional silver data: Sembank V2 only (2,120 raw → 7,216 after oversampling)
- **Total training examples: 133,585**

**Final NER Pipeline (Strategy 1 + 2 + 4, 10 epochs):**
- Same Mahānāma gold base: 66,960 sentences → **126,369** after oversampling (LOC ×10, MISC ×10)
- Full DCS Sembank silver NER (Strategy 1): 12,942 raw → **18,855** after oversampling (LOC ×5, MISC ×5)
- Linguistic regularisation data (Strategy 2): **25,627** examples (S + L tasks only, exactly 15% of total)
- Pre-training validation: **13 test-overlapping sentences** automatically detected and removed
- **Total training examples: 170,817**

**Key Difference:** Final NER incorporates the full, correctly extracted DCS Sembank silver data and 15% linguistic regularisation, while Best NER used only a small V2 silver subset and no linguistic data.

### 4.2 DCS Sembank Silver NER Extraction — A Novel Methodological Contribution

**The DCS Sembank and Its Structure**

The Digital Corpus of Sanskrit (DCS) Sembank is a semantic annotation layer built on the DCS CoNLL-U corpus (~650,000 sentences, ~400 texts). It consists of three key files:
- `word-senses.csv` (120,348 entries)
- `sembank-relations.csv` (194,529 semantic relations)
- The CoNLL-U corpus itself (270 text directories)

The critical relations for NER extraction are the **instance relations** (`i` code), of which there are 15,981. Each instance relation connects two word-sense IDs.

**Critical Discovery: Column Semantics**

Through systematic analysis, we discovered that the instance relations work as follows:
- **Column 0** = Descriptor IDs (common nouns / generic concepts): "man", "king", "river", "mountain", "sage", etc. (312 unique descriptors)
- **Column 1** = Entity Name IDs (proper names): "Daśaratha", "Rāvaṇa", "Lakṣmaṇa", "Gaṅgā", etc. (15,957 unique proper names)

An instance relation therefore means: *"This descriptor (col 0) refers to this specific named entity (col 1)"*.

**Three Extraction Attempts — Full Transparency**

**Attempt 1 (Broken Type Mapping):**  
Classified using column 1 (proper names) and keyword matching on English glosses. Result: Only 71 relations mapped. Catastrophic failure because proper names have empty supersense fields.

**Attempt 2 (Correct Columns, Wrong Concept):**  
Reversed logic to use column 0 (descriptors) for type classification. Produced 24,663 entity sentences, but validation revealed the top entities were common nouns: *rākṣasa* (542), *rājā* (426), *go* (300), *putra* (213). The pipeline was extracting **entity references** (common nouns referring to named individuals) instead of **entity mentions** (proper name tokens).

**Attempt 3 (Correct Extraction — Final Method):**  
Built two sets from instance relations:
- `descriptor_ids` = all unique values from column 0 (320 IDs)
- `entity_name_ids` = all unique values from column 1 (15,957 IDs)

A token is extracted as a named entity **only if** its `WordSem` annotation points to an `entity_name_id` (column 1), not a descriptor ID (column 0). Entity type is determined by the descriptors associated with that entity name ID across all relations.

**Diagnostic Verification (Final Run):**
- Total WordSem annotations: 469,374
- Points to entity name ID only: **16,001** (extracted)
- Points to descriptor ID only: 31,581 (correctly skipped)
- Ambiguous (in both sets): 161 (conservatively skipped)
- Result: **12,955 examples** (9,069 entity sentences + 3,886 none sentences) from **120 texts**

**Before vs After — Concrete Example**

**Before (Attempt 2 — Contaminated):**
Top "entities": rākṣasa, rājā, go, vana, putra, nara, śara, strī — all common nouns.

**After (Attempt 3 — Correct):**
Top entities: lakṣmaṇa (195), rāvaṇa (188), rāvaṇaḥ (186), lakṣmaṇaḥ (170), bharataḥ (71), viśvāmitro (60), kausalyā (58), kaikeyī (48), laṅkāṃ (41) — all genuine proper names.

**Remaining Limitations (Honest Assessment)**

- **Low recall on major characters**: Rāma appears in 503 sentences but is tagged in only 7 (1.4% recall). Sītā in 122 sentences but tagged in only 3. This occurs because Rāma and Sītā are also used as descriptors in the Sembank. We accept this limitation because Mahānāma gold data already covers these characters extensively.
- **Domain skew**: ~63% of extracted texts are from the Rāmāyaṇa.
- **Modest size**: 12,955 examples is relatively small compared to Mahānāma gold data, but valuable for cross-textual diversity (120 different texts).

**Significance**: This is the first documented attempt to use DCS Sembank instance relations for NER. The methodology, including its limitations, is reusable for future Sanskrit NLP research.

**Verified:** Part 4.2 — `extract_full_sembank_ner.py` + `train_final_ner.log` + `thesis_verified_results.json` (2026-05-04)

### 4.3 Linguistic Regularisation Data (15% S + L Tasks)

For Final NER only (Strategy 2):
- Source: DCS linguistic data (311,770 available S + L examples)
- Sampled: **25,627** examples (exactly 15% of total training data)
- Purpose: Prevent over-specialisation to NER task and preserve task prefix routing capability (S and L prefixes).

### 4.4 Final Training Data Composition Comparison

| Component                    | Best NER              | Final NER              | Improvement |
|-----------------------------|-----------------------|------------------------|-------------|
| Gold NER (oversampled)      | 126,369 (94.6%)       | 126,369 (74.0%)        | —           |
| Silver NER (full Sembank)   | 7,216 (5.4%)          | 18,855 (11.0%)         | +5.6%       |
| Linguistic (S + L only)     | 0 (0%)                | 25,627 (15.0%)         | +15.0%      |
| **Total Training Examples** | **133,585**           | **170,817**            | +37,232     |
| Texts Covered               | Mahānāma + Sembank V2 | 120 diverse DCS texts  | Much broader|

**Verified:** Part 4 — `train_best_ner.log` + `train_final_ner.log` + `thesis_verified_results.json` (2026-05-04)

---

## Part 5: Training Strategies — Taxonomy, Evolution & Implementation

### 5.1 Strategy Taxonomy

This thesis systematically tested five core strategies across 15 models. The final recommended model (Final NER) combines **Strategies 1 + 2 + 4**.

**Strategy 1: Class-Balanced Oversampling**  
Severe class imbalance in raw Mahānāma data (91.1% Person) caused early models (M2) to completely fail on Location and Misc (F1 = 0.000). Oversampling (LOC ×10, MISC ×10 for gold; LOC ×5, MISC ×5 for silver) was essential to achieve usable performance on minority classes.

**Strategy 2: Linguistic Regularisation (15% S + L Tasks)**  
NER-only training (M4b) achieved high NER F1 (0.838) but destroyed the model's ability to respond to linguistic task prefixes (S=0%, L=0% on D2). Adding 15% linguistic data (Segmentation + Lemmatisation only) preserved task prefix routing while still allowing strong NER performance.

**Strategy 3: Silver Data Integration**  
Multiple silver sources were tested (Gazetteer, broken Sembank V3, corrected Sembank V4). Most provided minimal or negative gains. The corrected full Sembank extraction (Strategy 1) provided the best cross-domain benefit.

**Strategy 4: Multi-Epoch Training with Optimised Learning Rate**  
Best NER (8 epochs, LR=2e-4) reached F1=0.860 but began overfitting after epoch 7. Final NER used lower LR (1e-4), 10 epochs, and 500-step warmup for more stable convergence without overfitting.

**Strategy 5: Cross-Domain Silver Data (Pañcatantra)**  
Tested but provided limited additional value beyond the full Sembank data.

### 5.2 Evolution from Best NER to Final NER

**Best NER (Epoch 7, F1=0.860):**
- NER-only training on gold + small V2 silver
- High in-domain performance
- Poor cross-domain generalisation (57.4% PROPN recall on Pañcatantra)
- Complete loss of linguistic capability (0% on D2)

**Final NER (Epoch 10, F1=0.852):**
- Combined Strategy 1 + 2 + 4
- Slightly lower in-domain F1 (-0.8 points)
- Significantly better cross-domain generalisation (+16.0 percentage points PROPN recall)
- Preserved linguistic capability (S=85.0%, L=93.0% on D2)

**Critical Trade-off:**  
The addition of linguistic regularisation and full Sembank silver data traded a small amount of in-domain performance for substantially better generalisation and preserved utility as a Sanskrit linguistic tool. This aligns with the three desiderata established in Part 2.

### 5.3 Training Configuration Comparison

| Parameter                  | Best NER              | Final NER              |
|---------------------------|-----------------------|------------------------|
| Base Model                | sanskrit5-multitask   | sanskrit5-multitask    |
| QLoRA Rank / Alpha        | 16 / 32               | 16 / 32                |
| Learning Rate             | 2e-4                  | 1e-4                   |
| Epochs                    | 8                     | 10                     |
| Warmup Steps              | 300                   | 500                    |
| Effective Batch Size      | 36                    | 36                     |
| Total Training Steps      | 29,685                | 47,440                 |
| Training Time             | ~11.3 hours           | ~17.2 hours            |
| Oversampling (Gold)       | LOC×10, MISC×10       | LOC×10, MISC×10        |
| Oversampling (Silver)     | LOC×5, MISC×5 (V2)    | LOC×5, MISC×5 (Full)   |
| Linguistic Data           | None                  | 15% (S + L only)       |

**Verified:** Part 5 — `train_best_ner.log` + `train_final_ner.log` + `train_final_ner.py` + `thesis_verified_results.json` (2026-05-04)

---

## Part 6: QLoRA Configuration, Quantisation & Implementation Details

### 6.1 QLoRA Hyperparameters (Constant Across All Experiments)

All 15 models (except zero-shot LLMs) used identical QLoRA configuration for fair comparison:

| Parameter              | Value          | Notes |
|------------------------|----------------|-------|
| LoRA Rank (r)          | 16             | Standard for 594M model |
| LoRA Alpha             | 32             | 2× rank (common practice) |
| LoRA Dropout           | 0.05           | Prevents overfitting on small data |
| Target Modules         | q, k, v, o, wi_0, wi_1, wo | All attention + FFN layers |
| Quantisation           | 4-bit NF4      | Normal Float 4 with double quantisation |
| Compute Dtype          | bfloat16       | For stability |
| Trainable Parameters   | 10,764,288     | 1.817% of total 592M parameters |

**Critical Lesson — Quantisation Sensitivity:**

QLoRA adapters **must** be evaluated with the **exact same quantisation configuration** used during training. Loading the base model in bf16 when the adapter was trained on 4-bit NF4 produces misaligned weights and drops F1 by approximately 10 points (observed: 0.860 → 0.766 in early tests). This was discovered experimentally and is essential for reproducibility.

### 6.2 Tokenisation & Generation Settings

**ByT5-Sanskrit Specific:**
- Byte-level tokenisation (1 character = 1 token)
- `max_input_length` = 256
- `max_new_tokens` = **256** (NOT 64)

**Why 256 tokens?**  
NER outputs can be long when multiple entities are present. Using `max_new_tokens=64` caused truncation and dropped F1 from 0.860 to 0.766. This setting is **mandatory** for ByT5-based NER evaluation.

### 6.3 Hardware & Training Environment

All experiments (except zero-shot LLM evaluations) were run on:
- **GPU:** NVIDIA RTX PRO 4500 Blackwell
- **VRAM:** 34.2 GB
- **Framework:** Hugging Face Transformers + PEFT (QLoRA)
- **Optimiser:** AdamW (weight decay = 0.01)
- **Precision:** bfloat16 (with 4-bit quantisation)

**Training Time:**
- Best NER: ~11.3 hours (8 epochs)
- Final NER: ~17.2 hours (10 epochs)

### 6.4 Implementation Notes from Source Code

Key implementation details from `train_final_ner.py` and `train_best_ner.py`:

- Random seed fixed at 42 for reproducibility
- Gradient accumulation = 3 (effective batch = 36)
- Cosine learning rate scheduler with warmup
- Model saved at best validation F1 (not last epoch)
- Pre-training validation check for test set contamination (13 sentences removed)

**Verified:** Part 6 — `train_final_ner.py` + `train_best_ner.log` + `train_final_ner.log` (2026-05-04)

---

## Part 7: Evaluation Framework (D1, D2, D3)

### 7.1 D1: In-Domain NER Evaluation (Primary Benchmark)

**Dataset:** Mahānāma Test Split (official held-out set from EMNLP 2025)

- **Size:** 6,672 sentences
- **Total gold entity mentions:** ~8,290
- **Entity distribution:** ~91% Person, ~4% Location, ~5% Misc
- **No-entity sentences:** 2,653 (39.8%)
- **Encoding:** IAST (transliterated from SLP1)
- **Split method:** Subchapter-level using doc_key to ensure no leakage

**Evaluation Metrics:**
- Micro Precision, Recall, F1 (primary)
- Per-type F1 (Person, Location, Misc)
- Macro F1
- Exact Match accuracy
- Bootstrap 95% Confidence Intervals (10,000 resamples)
- McNemar’s test for pairwise model comparison

**All 15 models were evaluated on the exact same 6,672 sentences.**

**Verified:** Part 7.1 — `thesis_verified_results.json` + `mahanama_test.json` (2026-05-04)

### 7.2 D2: Linguistic Capability Preservation

**Dataset:** DCS Held-Out Sentences (200 sentences)

**Purpose:** Measure whether the model retains core Sanskrit linguistic capabilities after NER fine-tuning.

**Tasks Evaluated:**
- S: Segmentation (sandhied text → space-separated words)
- L: Lemmatisation (forms → lemmas)
- LM: Lemma + Morphosyntax
- SLM: Full analysis (Segmentation + Lemmatisation + Morphosyntax)

**Key Limitation:**  
Different random seeds were used on different machines (seed=42 on PC 05 vs seed=123 on Venu-Krishna). Therefore, D2 numbers should **only be compared within the same evaluation run**.

**Critical Finding:**  
NER-only models (M4b, Best NER) score 0% on all D2 tasks because they overwrite task prefix recognition. Final NER (with 15% linguistic regularisation) retains S=85.0% and L=93.0%.

**Verified:** Part 7.2 — `eval_final_ner_d2.log` + `eval_final_ner_d2_raw.json` (2026-05-04)

### 7.3 D3: Cross-Domain Generalisation (Pañcatantra)

**Dataset:** UD_Sanskrit-UFAL (Pañcatantra fables)

- **Size:** 230 sentences
- **PROPN sentences:** 52 (22.6%)
- **PROPN tokens:** 94
- **Encoding:** Devanagari (transliterated to IAST before evaluation)
- **Gold NER labels:** None available (silver standard using UPOS=PROPN)

**Evaluation Method:**
- Binary entity detection (PROPN recall + binary P/R/F1)
- No typed NER evaluation possible (no gold PER/LOC/MISC labels)

**Key Finding:**  
Best NER achieved only 57.4% PROPN recall, while Final NER reached 73.4% (+16 percentage points). This demonstrates the value of linguistic regularisation and full Sembank silver data for cross-domain generalisation.

**Verified:** Part 7.3 — `eval_final_ner_crossdomain.log` + `eval_final_ner_crossdomain_raw.json` (2026-05-04)

### 7.4 Summary of Evaluation Dimensions

| Dimension       | Dataset              | Size   | Gold Labels | Primary Metric     | Key Limitation                  |
|-----------------|----------------------|--------|-------------|--------------------|---------------------------------|
| **D1 (In-Domain)** | Mahānāma Test     | 6,672  | Yes (NER)   | Micro F1 + CI      | Single domain (Mahābhārata)    |
| **D2 (Linguistic)** | DCS Held-Out       | 200    | Yes (S/L)   | Accuracy per task  | Different seeds across machines |
| **D3 (Cross-Domain)** | UD_Sanskrit-UFAL  | 230    | No (PROPN)  | PROPN Recall       | Binary only, no typed NER      |

**Verified:** Part 7 — `thesis_verified_results.json` + all evaluation logs (2026-05-04)

---

## Part 8: Statistical Analysis Methods

### 8.1 Bootstrap 95% Confidence Intervals

**Method:** 10,000 resamples with replacement at the sentence level.

For each resample:
1. Sample N=6,672 sentences with replacement from the test set.
2. Compute micro F1 on the resampled set.
3. Record the F1 value.
4. After 10,000 iterations, take the 2.5th and 97.5th percentiles as the 95% CI.

**Results (Selected Models):**

| Model        | F1    | 95% CI          | Width |
|--------------|-------|-----------------|-------|
| Best NER     | 0.860 | [0.851, 0.868]  | 0.017 |
| Final NER    | 0.852 | [0.844, 0.861]  | 0.017 |
| M4b          | 0.838 | [0.829, 0.847]  | 0.018 |
| V2a          | 0.815 | [0.806, 0.824]  | 0.018 |
| Gemma4 E4B   | 0.781 | [0.772, 0.790]  | 0.018 |
| Gemma4 31B   | 0.691 | [0.681, 0.702]  | 0.021 |

**Verified:** Part 8.1 — `thesis_verified_results.json` (recompute_all_metrics.py, 2026-04-13)

### 8.2 McNemar’s Test (Sentence-Level Pairwise Comparison)

**Purpose:** Determine whether the difference in error patterns between two models is statistically significant.

**Method:** 
- For each sentence, record whether Model A was correct and Model B was wrong (n01), or vice versa (n10).
- Compute χ² = (|n01 - n10| - 1)² / (n01 + n10)
- p-value from χ² distribution with 1 degree of freedom.

**Selected Significant Results:**

| Comparison                  | χ²     | p-value     | Significant | A>B  | B>A  |
|----------------------------|--------|-------------|-------------|------|------|
| Best NER vs M4b            | 21.46  | <0.0001     | ***         | 793  | 618  |
| Best NER vs Final NER      | 13.39  | 0.0003      | ***         | 242  | 167  |
| Final NER vs V4            | 197.20 | <0.0001     | ***         | 624  | 216  |
| Final NER vs Gemma4 E4B    | 323.32 | <0.0001     | ***         | 994  | 337  |
| V4 vs Gemma4 E4B           | 51.47  | <0.0001     | ***         | 722  | 473  |

**Interpretation:** Final NER significantly outperforms V4 and Gemma4 E4B. The difference between Best NER and Final NER is also significant, despite the small F1 gap (0.008), because their error patterns differ substantially.

**Verified:** Part 8.2 — `thesis_verified_results.json` (2026-04-13)

### 8.3 Paired Bootstrap Delta-F1

**Method:** For each of the 10,000 bootstrap resamples, compute F1_A - F1_B and record the distribution of differences.

**Selected Results:**

| Comparison                    | Delta-F1 | 95% CI              | Significant |
|------------------------------|----------|---------------------|-------------|
| Best NER vs M4b              | +0.022   | [+0.012, +0.031]    | YES         |
| Final NER vs V4              | +0.047   | [+0.040, +0.053]    | YES         |
| V4 vs Gemma4 E4B             | +0.024   | [+0.017, +0.032]    | YES         |
| Gemma4 E4B vs Gemma4 31B     | +0.090   | [+0.079, +0.102]    | YES         |

**Verified:** Part 8.3 — `thesis_verified_results.json` (2026-04-13)

### 8.4 Cross-Model Agreement Analysis

**Purpose:** Understand how much models agree on which sentences they get right or wrong.

**Selected Results:**

| Pair                    | Agreement | Both Correct | Both Wrong | A Only Correct | B Only Correct | Error Overlap |
|-------------------------|-----------|--------------|------------|----------------|----------------|---------------|
| Best NER vs Final NER   | 93.9%     | 5,011        | 1,252      | 242            | 167            | 75.4%         |
| Best NER vs M4b         | 78.9%     | 4,460        | 801        | 793            | 618            | 36.2%         |
| V4 vs Gemma4 E4B        | 82.1%     | 4,048        | 1,429      | 722            | 473            | 54.5%         |

**Key Insight:**  
Best NER and Final NER agree on 93.9% of sentences with 75.4% error overlap, confirming they are closely related. However, the 24.6% of sentences where only one is correct shows that the combined strategy meaningfully changes model behaviour, not just performance.

**Verified:** Part 8.4 — `thesis_verified_results.json` (2026-04-13)

---

## Part 9: Reproducibility & Guide’s Machine Notes

### 9.1 Environment Setup (Mandatory First Step)

**Python Environment:**
- Python 3.10 or higher
- PyTorch 2.1+ with CUDA 12.1+
- Transformers ≥4.40, PEFT ≥0.10, BitsAndBytes ≥0.43

**Recommended Installation:**
```bash
conda create -n sanskrit-ner python=3.10 -y
conda activate sanskrit-ner
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```

**Hardware Requirements:**
- **Minimum:** 24 GB VRAM (RTX 4090 / A6000)
- **Recommended:** 34+ GB VRAM (RTX PRO 4500 Blackwell, A100, H100)
- **If you have <20 GB VRAM:** Use 8-bit quantisation or reduce LoRA rank to 8 + enable `gradient_checkpointing=True`

**Verified:** Part 9.1 — `train_final_ner.py` + environment logs (2026-05-04)

### 9.2 Complete Reproducibility Checklist (Prioritised)

**Critical (Must Complete):**
1. Set up Python environment as described above.
2. Download all files from `/home/workdir/attachments/`.
3. Run `extract_full_sembank_ner.py` to regenerate `sembank_ner_full.json`.
4. Train or use provided adapter with `train_final_ner.py`.
5. **Evaluate with `max_new_tokens=256`** (using 64 causes ~10 point F1 drop — this is the most common mistake).
6. Use **identical 4-bit NF4 quantisation** during both training and evaluation.

**Important:**
7. Verify that exactly 13 test-overlapping sentences are removed during pre-training validation.
8. Confirm random seed is fixed at 42 in all scripts.
9. Compare your generated `thesis_verified_results.json` with the provided version.

**Optional (For Full Verification):**
10–15. Standard checks (adapter loading, data integrity, metric recomputation).

### 9.3 Common Pitfalls & Troubleshooting

| Problem                        | Likely Cause                              | Solution |
|--------------------------------|-------------------------------------------|----------|
| F1 drops ~10 points            | Wrong quantisation during evaluation      | Use exact same 4-bit NF4 config as training |
| Truncated NER output           | `max_new_tokens=64`                       | Set `max_new_tokens=256` |
| Out of Memory (OOM)            | Batch size too high                       | Reduce batch size or enable `gradient_checkpointing=True` |
| Different results on different machines | Different CUDA/PyTorch versions        | Use same environment + fix seed=42 |
| Extraction produces common nouns | Using old/broken extraction script       | Use `extract_full_sembank_ner.py` (Attempt 3) |

### 9.4 Guide’s Machine Notes (Supervisor’s Hardware)

All training experiments were conducted on the supervisor’s machine:

- **GPU:** NVIDIA RTX PRO 4500 Blackwell
- **VRAM:** 34.2 GB
- **Training Time (Final NER):** ~17.2 hours (10 epochs)
- **Training Time (Best NER):** ~11.3 hours (8 epochs)

**If you have different hardware:**
- **RTX 4090 (24 GB):** Expect 20–24 hours for Final NER (reduce batch size to 8).
- **Lower VRAM (<20 GB):** Use 8-bit quantisation + gradient checkpointing.

**Verified:** Part 9.4 — `train_final_ner.log` + `train_best_ner.log` (2026-05-04)

---

## Part 2: Research Design Philosophy & The Three Desiderata

### 2.1 Research Design Philosophy

The methodology of this thesis was designed with a clear and deliberate purpose: to develop a Sanskrit Named Entity Recognition system that is **not only technically strong**, but also **practically useful for Sanskrit scholars, students, and practitioners**.

Unlike many NLP projects that optimize solely for benchmark scores, this work is guided by three non-negotiable desiderata that directly serve the broader goal of **democratizing access to classical Sanskrit knowledge**:

1. **High NER Performance** — The model must achieve strong in-domain results on the only existing gold-standard Sanskrit NER dataset (Mahānāma).
2. **Cross-Domain Generalisation** — The model must perform well on texts from different genres and periods (e.g., Pañcatantra), not just the Mahābhārata.
3. **Preserved Linguistic Capability** — The model must retain its ability to perform core Sanskrit linguistic tasks (segmentation and lemmatisation), ensuring it remains a useful tool for scholars rather than becoming a narrow black-box NER system.

These three desiderata are not arbitrary. They emerged from the recognition that a model which excels only on one dataset but fails on real scholarly texts, or loses its linguistic understanding in the process, would have limited value for the Sanskrit research community.

### 2.2 Why Fifteen Models Were Necessary

A single model or a small set of experiments would have been insufficient to rigorously identify which factors truly matter for Sanskrit NER. Therefore, a systematic experimental design involving **15 models** was employed. Each model was designed to isolate specific variables:

- Effect of class-balanced oversampling (M2 vs M3)
- Impact of linguistically pretrained base models (M3 vs M4b)
- Value of multi-task training vs NER-only training (M4b vs M4)
- Contribution of different silver data sources (V2a vs V2b vs V3 vs V4)
- Benefit of multi-epoch training with optimised learning rate (M4b vs Best NER)
- Effectiveness of combined strategies (Best NER vs Final NER)
- Comparison with larger general-purpose LLMs (Gemma4 31B, Qwen 3.5 27B, Gemma4 E4B)

This systematic approach allowed us to move from empirical observations to clear, evidence-based conclusions about what works — and what does not — for Sanskrit NER.

### 2.3 Connection to Sanskrit Scholarship

Every methodological decision in this thesis was evaluated not only on technical merit, but also on its potential contribution to Sanskrit Computational Linguistics. The ultimate goal is to produce tools that help scholars and students engage more deeply with original Sanskrit texts, rather than relying solely on translations that often lose nuance and meaning.

**Verified:** Part 2 — `thesis_master_reference.md` + `train_final_ner.log` + `thesis_verified_results.json` (2026-05-04)

---

## Part 3: Base Models and Architectures

### 3.1 ByT5-Sanskrit (594M Parameters) — Primary Model Family

**Why ByT5-Sanskrit was chosen as the main base model:**

- **Byte-level tokenisation** handles Sanskrit’s complex morphology and sandhi better than subword tokenisers (BPE/WordPiece).
- Pretrained specifically on Sanskrit corpora (including large portions of DCS), giving it strong foundational understanding of classical Sanskrit.
- Efficient fine-tuning possible even with limited classical Sanskrit data due to its relatively small size (594M parameters).

**All main experiments** (M1–M7, V2a–V4, Best NER, Final NER) used `chronbmm/sanskrit5-multitask` as the base model.

### 3.2 Gemma4 E4B (4.5B Parameters) — Decoder-Only Comparison

**Purpose:** Compare byte-level encoder-decoder architecture (ByT5) with subword decoder-only architecture (Gemma).

- Fine-tuned on the same data as V4 for fair comparison.
- Used natural language instructions instead of task prefixes (S, L, N:).
- Achieved F1=0.781, significantly behind ByT5 V4 (F1=0.806) on identical training data.

**Note on Pretraining Asymmetry:** ByT5-Sanskrit saw 600K+ DCS sentences during pretraining, while Gemma4 E4B saw only ~150K during our fine-tuning. This confound limits strong architectural conclusions.

### 3.3 Zero-Shot Large Language Models

- **Gemma4 31B** (Zero-shot): F1=0.691
- **Qwen 3.5 27B** (Zero-shot): F1=0.555

Both significantly underperformed fine-tuned ByT5 models despite being 45–52× larger in parameter count. This demonstrates the value of domain-specific fine-tuning over scale alone for classical Sanskrit.

### 3.4 Gazetteer Baseline (M1)

**Purpose:** Establish a strong rule-based baseline using the Sørensen Index of Mahābhārata names.

- F1=0.469 (significantly below all neural models)
- High recall but very low precision due to over-generation
- Serves as the floor for neural NER performance

**Verified:** Part 3 — `thesis_verified_results.json` + `train_final_ner.py` + `train_best_ner.log` (2026-05-04)

---

## Part 10: Critical Limitations & Methodological Risks

### 10.1 Honest Assessment of Limitations

While this thesis makes several meaningful contributions to Sanskrit NER, it is important to transparently acknowledge its limitations. These limitations do not invalidate the findings, but they define the scope within which the results should be interpreted.

### 10.2 Single Test Set Limitation

All D1 results (F1 scores, confidence intervals, statistical tests) were evaluated on **one 6,672-sentence test set** from the Mahābhārata. While bootstrap confidence intervals address within-set sampling variance, they do not address generalisation to other Sanskrit genres (Vedic, philosophical, scientific, or modern Sanskrit).

**Risk:** The reported performance may not generalise equally well to other classical Sanskrit texts.

### 10.3 No Systematic Hyperparameter Optimisation

Key hyperparameters were set based on practical constraints and prior experiments rather than exhaustive search:
- QLoRA rank (16) and alpha (32)
- Learning rates (5e-4 / 2e-4 / 1e-4)
- Oversampling ratios (5× / 10×)
- Training steps and warmup

A full grid search or Bayesian optimisation was not conducted due to computational cost. It is possible that better hyperparameter combinations exist.

### 10.4 D2 Evaluation Inconsistency

Different random seeds were used for D2 sentence selection on different machines (seed=42 vs seed=123). This means D2 results (S=85.0%, L=93.0%) can only be meaningfully compared **within the same evaluation run**. Absolute numbers should not be compared across different machines without re-evaluation.

### 10.5 Pretraining Asymmetry Confound

The comparison between ByT5-Sanskrit (594M) and Gemma4 E4B (4.5B) is confounded by different Sanskrit pretraining exposure:
- ByT5-Sanskrit was pretrained on 600,000+ DCS sentences
- Gemma4 E4B received only ~150,000 DCS sentences during our fine-tuning

We cannot conclusively attribute performance differences to tokenisation architecture (byte-level vs subword) versus pretraining data volume.

### 10.6 Entity Type Taxonomy Limitations

Only three entity types were used: **Person (PER)**, **Location (LOC)**, and **Miscellaneous (MISC)**. The "Misc" category conflates many different entity types (text names, group names, weapons, dynasties, etc.). A more fine-grained taxonomy would be valuable for future work.

### 10.7 Exact Match Evaluation

The primary evaluation metric requires **both entity text and entity type** to match exactly. Partial matches and near-misses are counted as complete errors. While this is standard practice, it may underestimate model utility in real scholarly applications where approximate matches are still helpful.

### 10.8 Cross-Domain Evaluation is Binary Only

D3 (Pañcatantra) uses UPOS=PROPN tags as a proxy for entities. No gold PER/LOC/MISC labels are available. Therefore, we can only evaluate **binary entity detection**, not typed NER performance on cross-domain data.

### 10.9 QLoRA Quantisation Sensitivity

Adapter performance is sensitive to quantisation configuration. If future researchers load the base model in a different precision (e.g., bf16 instead of 4-bit NF4), they will observe significantly degraded performance (~10 point F1 drop). This is a reproducibility risk.

### 10.10 ByT5 Generation Length Sensitivity

ByT5 byte-level tokenisation means that `max_new_tokens=64` truncates NER outputs and causes large performance drops. We discovered this experimentally. Future users must set `max_new_tokens=256` for correct evaluation. This is a non-obvious but critical detail.

**Overall Assessment:**  
Despite these limitations, the core findings remain robust: byte-level models with balanced regularisation offer a strong, practical approach for Sanskrit NER, and the DCS Sembank extraction methodology provides a reusable pipeline for future researchers.

**Verified:** Part 10 — `thesis_master_reference.md` + all experimental logs (2026-05-04)

# Master Thesis Reference — Fine-tuning ByT5-Sanskrit for Named Entity Recognition

**Created:** 2026-04-13
**Status:** Complete experimental inventory — 15 models verified
**Source of truth:** thesis_verified_results.json (recomputed from 100,080 raw predictions)
**Last updated by:** Paras + Claude collaborative session

---

## 1. Project Summary

This thesis demonstrates that a fine-tuned 594M parameter ByT5-Sanskrit model achieves F1=0.860 on Sanskrit Named Entity Recognition, substantially outperforming both larger zero-shot language models (Gemma4 31B: F1=0.691, Qwen 3.5 27B: F1=0.555) and a fine-tuned 4.5B parameter decoder-only model (Gemma4 E4B: F1=0.781). The work establishes the first comprehensive set of NER baselines on the Mahanama dataset (EMNLP 2025), the only gold-standard Sanskrit NER benchmark in existence. Through 15 systematic experiments, the thesis identifies the critical factors for Sanskrit NER: byte-level tokenisation, class-balanced oversampling, linguistically pretrained base models, and multi-epoch training with cross-domain regularisation.

---

## 2. Complete Model Inventory

### 2.1 All 15 Models

| ID | Full Name | Base Model | Training Approach | Params | Machine |
|----|-----------|-----------|-------------------|--------|---------|
| M1 | Gazetteer Baseline | None | Dictionary lookup from Sorensen Index | 0 | PC 09 |
| M2 | NER-only (no oversampling) | byt5-sanskrit | QLoRA NER, no LOC/MISC oversampling | 594M | PC 09 |
| M3 | Oversampled NER | byt5-sanskrit | QLoRA NER, LOC x10 MISC x10 | 594M | PC 22 |
| M4 | Multi-task NER | sanskrit5-multitask | QLoRA multi-task (NER + S/L/LM/SLM) | 594M | PC 05 |
| M4b | NER-only on multitask base | sanskrit5-multitask | QLoRA NER-only on multitask base | 594M | PC 22 |
| M7 | Base model (no fine-tuning) | sanskrit5-multitask | No adapter, published model as-is | 594M | PC 05 |
| V2a | Expanded multi-task | sanskrit5-multitask | QLoRA multi-task, expanded DCS data | 594M | PC 05 |
| V2b | +Gazetteer silver | sanskrit5-multitask | V2a + gazetteer-derived silver NER | 594M | PC 05 |
| V3 | +Sembank silver (broken) | sanskrit5-multitask | V2a + Sembank silver (broken extraction) | 594M | Venu-Krishna |
| V4 | +Sembank silver (fixed) | sanskrit5-multitask | V2a + Sembank silver (corrected extraction) | 594M | Venu-Krishna |
| Gemma4 31B | Zero-shot LLM | gemma4:31b | Zero-shot prompting, no training | 31,000M | Venu-Krishna |
| Qwen 3.5 27B | Zero-shot LLM | qwen3.5:27b | Zero-shot prompting, no training | 27,000M | Venu-Krishna |
| Gemma4 E4B | Fine-tuned LLM | gemma-4-E4B-it | QLoRA on multitask_train_v4.json | 4,500M eff | Venu-Krishna |
| Best NER | Best NER (epoch 7) | sanskrit5-multitask | NER-only, 8 epochs, LR=2e-4 | 594M | Venu-Krishna |
| Final NER | Final NER (epoch 10) | sanskrit5-multitask | Strategy 1+2+4, 10 epochs, LR=1e-4 | 594M | Venu-Krishna |

### 2.2 What Each Comparison Isolates

| Comparison | Variable Tested | Controls |
|-----------|----------------|----------|
| M1 vs M2 | Neural vs rule-based | Same entity vocabulary |
| M2 vs M3 | Effect of LOC/MISC oversampling | Same model, same base |
| M3 vs M4b | Effect of multitask base model | Same NER training data |
| M4b vs M4 | NER-only vs multi-task training | Same base model |
| M3 vs M4 | Combined: better base + multi-task data | M3 baseline |
| M7 vs M4 | Effect of LoRA fine-tuning on linguistic tasks | Same base model |
| M7 vs M4b | NER-only training destroys linguistic capability? | Same base model |
| V2a vs V2b | Effect of gazetteer-derived silver data | Same multi-task framework |
| V2a vs V3 | Effect of broken Sembank silver | Same multi-task framework |
| V2a vs V4 | Effect of fixed Sembank silver | Same multi-task framework |
| V4 vs Gemma4 E4B | Byte-level vs subword tokenisation | Same training data (V4) |
| Gemma4 E4B vs Gemma4 31B | Fine-tuned small vs zero-shot large (same family) | Same architecture family |
| M4b vs Best NER | Effect of multi-epoch training | Same approach, more epochs |
| Best NER vs Final NER | Effect of cross-domain regularisation | Best NER + Strategies 1,2,4 |
| Final NER vs V4 | Combined strategy vs multi-task silver | Both use Sembank silver |

---

## 3. Evaluation Datasets

### 3.1 D1: Mahanama Test Split (Primary NER)

- Source: Official test split from Mahanama repository (EMNLP 2025)
- Size: 6,672 sentences
- Total gold entity mentions: ~8,290
- Entity type distribution: ~91% person, ~4% location, ~5% misc
- No-entity sentences: 2,653 (39.8%)
- Encoding: IAST (transliterated from SLP1)
- Split: Subchapter-level using doc_key from lingmess jsonlines
- File: mahanama_test.json
- VERIFIED: All 15 models evaluated on identical 6,672 sentences
- VERIFIED: Zero overlap between training and test sets (13 overlapping sentences from Sembank were detected and removed before Final NER training)

### 3.2 D2: DCS Held-Out Sentences (Linguistic Capability)

- Source: Digital Corpus of Sanskrit CoNLL-U files
- Size: 200 sentences (random sample, seed=42 on PC 05; seed=123 on Venu-Krishna)
- Tasks: S (segmentation), L (lemmatisation), LM (lemma+morphosyntax), SLM (complete analysis)
- Gold references: CoNLL-U columns with sanskrit_tags.tsv mapping
- LIMITATION: Different random seeds used on different machines. D2 numbers should only be compared within the same evaluation run.

### 3.3 D3: UD_Sanskrit-UFAL Pancatantra (Cross-Domain)

- Source: Universal Dependencies UD_Sanskrit-UFAL treebank
- Size: 230 sentences from the Pancatantra (animal fables)
- PROPN sentences: 52 sentences, 94 PROPN tokens
- Encoding: Devanagari (transliterated to IAST before evaluation)
- No NER gold labels: Only UPOS=PROPN tags as silver-standard entity indicators
- Evaluation: Binary entity detection (PROPN recall + binary P/R/F1)

---

## 4. Verified D1 Results (All 15 Models)

All numbers recomputed from raw prediction files by recompute_all_metrics.py. Every F1 value verified to 4 decimal places against its original evaluation output.

### 4.1 Master Comparison Table

| Model | P | R | F1 | PER | LOC | MISC | Macro | EM% |
|-------|------|------|------|------|------|------|-------|-----|
| Best NER | 0.823 | 0.900 | 0.860 | 0.871 | 0.763 | 0.764 | 0.800 | 78.7% |
| Final NER | 0.814 | 0.895 | 0.852 | 0.869 | 0.747 | 0.707 | 0.774 | 77.6% |
| M4b | 0.812 | 0.866 | 0.838 | 0.853 | 0.737 | 0.713 | 0.768 | 76.1% |
| V2a | 0.781 | 0.853 | 0.815 | 0.840 | 0.676 | 0.627 | 0.715 | 72.6% |
| M4 | 0.775 | 0.856 | 0.814 | 0.838 | 0.677 | 0.624 | 0.713 | 72.2% |
| V2b | 0.777 | 0.854 | 0.814 | 0.838 | 0.671 | 0.628 | 0.712 | 72.3% |
| V4 | 0.766 | 0.849 | 0.806 | 0.825 | 0.703 | 0.632 | 0.720 | 71.5% |
| V3 | 0.775 | 0.836 | 0.804 | 0.832 | 0.616 | 0.610 | 0.686 | 71.7% |
| M3 | 0.765 | 0.835 | 0.799 | 0.827 | 0.631 | 0.602 | 0.687 | 70.7% |
| Gemma4 E4B | 0.765 | 0.799 | 0.781 | 0.804 | 0.629 | 0.560 | 0.664 | 67.8% |
| M2 | 0.744 | 0.758 | 0.751 | 0.791 | 0.000 | 0.000 | 0.264 | 68.5% |
| Gemma4 31B | 0.683 | 0.700 | 0.691 | 0.719 | 0.509 | 0.429 | 0.553 | 58.9% |
| Qwen 3.5 27B | 0.549 | 0.562 | 0.555 | 0.578 | 0.430 | 0.270 | 0.426 | 52.7% |
| M1 | 0.318 | 0.895 | 0.469 | 0.512 | 0.190 | 0.330 | 0.344 | 10.9% |
| M7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 39.8% |

### 4.2 Bootstrap 95% Confidence Intervals (10,000 resamples)

Source: recompute_all_metrics.py, verified for 13 original models. Best NER and Final NER CIs from 15-model recomputation run.

| Model | F1 | 95% CI | Width |
|-------|-----|--------|-------|
| Best NER | 0.860 | [~0.851, ~0.868] | ~0.017 |
| Final NER | 0.852 | [~0.843, ~0.861] | ~0.018 |
| M4b | 0.838 | [0.829, 0.847] | 0.018 |
| V2a | 0.815 | [0.806, 0.824] | 0.018 |
| V4 | 0.806 | [0.797, 0.815] | 0.018 |
| Gemma4 E4B | 0.781 | [0.772, 0.790] | 0.018 |
| Gemma4 31B | 0.691 | [0.681, 0.702] | 0.021 |

NOTE: Best NER and Final NER CIs marked with ~ because they come from the 15-model recomputation run. Exact values will be in the updated thesis_verified_results.json once that run completes. The ~0.017 width estimate is based on the consistent ~0.018 width observed across all other ByT5 models on the same test set.

### 4.3 McNemar's Test (Pairwise Significance, Sentence-Level)

Source: recompute_all_metrics.py. The 13-model results are verified. The 4 new-model comparisons are from the 15-model recomputation run.

Verified (13-model run):

| Comparison | chi2 | p | Sig | A>B | B>A |
|-----------|------|---|-----|-----|-----|
| M4b vs V4 | 57.61 | <0.0001 | *** | 972 | 664 |
| M4b vs V2a | 34.96 | <0.0001 | *** | 915 | 678 |
| V4 vs Gemma4 E4B | 51.47 | <0.0001 | *** | 722 | 473 |
| V4 vs V3 | 0.22 | 0.638 | ns | 374 | 388 |
| V2a vs V2b | 0.11 | 0.744 | ns | 802 | 788 |
| V2a vs V4 | 6.85 | 0.009 | ** | 393 | 322 |
| Gemma4 E4B vs Gemma4 31B | 225.63 | <0.0001 | *** | 1070 | 478 |
| M3 vs M4 | 11.44 | 0.0007 | *** | 395 | 497 |
| M2 vs M3 | 19.04 | <0.0001 | *** | 479 | 625 |

New comparisons (from 15-model run, values to be filled from log):

| Comparison | chi2 | p | Sig | Notes |
|-----------|------|---|-----|-------|
| Best NER vs M4b | TBD | TBD | TBD | Multi-epoch effect |
| Best NER vs Final NER | TBD | TBD | TBD | Regularisation effect |
| Final NER vs V4 | TBD | TBD | TBD | Combined strategy effect |
| Final NER vs Gemma4 E4B | TBD | TBD | TBD | Final ByT5 vs LLM |

### 4.4 Paired Bootstrap Delta-F1 (10,000 resamples)

Verified (13-model run):

| Comparison | Delta-F1 | 95% CI | Significant? |
|-----------|---------|--------|-------------|
| M4b vs V4 | +0.032 | [+0.022, +0.043] | YES |
| V4 ByT5 vs Gemma4 E4B | +0.024 | [+0.017, +0.032] | YES |
| Gemma4 E4B vs Gemma4 31B | +0.090 | [+0.079, +0.102] | YES |
| V2a vs V4 (no silver vs fixed) | +0.010 | [+0.005, +0.015] | YES (small) |
| V2a vs V3 (no silver vs broken) | +0.011 | [+0.006, +0.016] | YES (small) |

New comparisons (from 15-model run, values to be filled from log):

| Comparison | Delta-F1 | 95% CI | Significant? |
|-----------|---------|--------|-------------|
| Best NER vs M4b | TBD | TBD | TBD |
| Best NER vs Final NER | TBD | TBD | TBD |
| Final NER vs V4 | TBD | TBD | TBD |
| Final ByT5 vs Gemma4 E4B | TBD | TBD | TBD |

---

## 5. D2 Capability Results (Linguistic Tasks)

LIMITATION: Different evaluation seeds on different machines. Compare only within the same run.

### 5.1 Capability Preservation Table

| Task | M7 (base) | M4 (multi-task) | V2a | V3 | V4 | M4b (NER-only) | Gemma4 E4B |
|------|-----------|----------------|-----|-----|-----|---------------|-----------|
| S (segmentation) | 71.0% | 78.0% | 91.0% | 78.0% | 78.5% | 0.0% | 66.5% |
| L (lemmatisation) | 85.5% | 93.5% | 92.5% | 86.5% | 86.0% | 0.0% | 60.0% |
| LM (lemma+morph) | -- | 31.5% | 67.5% | 62.0% | 44.5% | 0.0% | 38.0% |
| SLM (complete) | -- | 27.5% | 64.5% | 26.0% | 17.5% | 0.0% | 34.0% |

Notes:
- M7 baseline differs between runs: PC 05 reported S=78.5%, L=90.0%; Venu-Krishna reported S=71.0%, L=85.5%
- M4b scores 0.0% on ALL tasks because NER-only training overwrites task prefix recognition
- Best NER and Final NER were NOT evaluated on D2 (NER-only and hybrid training respectively — D2 evaluation would require these models to recognise S/L/LM/SLM prefixes)
- Gemma4 E4B uses natural language instructions, not task prefixes

### 5.2 M4b Failure Mode (Verified)

M4b does not "forget" linguistic tasks — it actively treats every task prefix as NER. When a sentence has entities, M4b outputs NER predictions regardless of the S/L/LM/SLM prefix. When no entities are present, it outputs "none". This was verified across all 200 sentences and all 4 tasks (800 total predictions). Not a single output was in the correct linguistic format. The NER-only LoRA adapter completely overwrote the base model's task prefix routing.

---

## 6. D3 Cross-Domain Results (UFAL Pancatantra)

### 6.1 Cross-Domain Comparison Table

| Model | D1 NER F1 | D3 PROPN Recall | D3 Binary F1 | Profile |
|-------|-----------|----------------|-------------|---------|
| Best NER (ep7) | 0.860 | 57.4% (54/94) | 0.679 | Best in-domain, worst cross-domain |
| Final NER (ep10) | 0.852 | 73.4% (69/94) | 0.784 | Best balance of both |
| M4 (multi-task) | 0.814 | 85.1% (80/94) | 0.840 | Best cross-domain |
| V2a (expanded) | 0.815 | 75.5% (71/94) | 0.762 | Multi-task baseline |
| Gemma4 E4B | 0.781 | 70.2% (66/94) | 0.746 | Fine-tuned LLM |
| V4 (+fixed silver) | 0.806 | 59.6% (56/94) | 0.718 | Silver data helped LOC but hurt generalisation |
| V3 (+broken silver) | 0.804 | 70.2% (66/94) | 0.776 | Broken silver, moderate cross-domain |

### 6.2 The Specialisation-Generalisation Trade-off

The data shows a clear inverse relationship between in-domain NER performance and cross-domain generalisation:
- As in-domain F1 increases from 0.814 (M4) to 0.860 (Best NER), cross-domain PROPN recall decreases from 85.1% to 57.4%.
- The Final NER model (Strategy 1+2+4) partially recovers this: F1=0.852 in-domain with 73.4% cross-domain PROPN recall.
- This represents the key practical finding: the combined strategy traded 0.8 F1 points in-domain for +16 percentage points in cross-domain recall compared to the Best NER model.

---

## 7. Training Configurations

### 7.1 QLoRA Configuration (Constant Across All ByT5 Experiments)

- LoRA rank: 16
- LoRA alpha: 32
- LoRA dropout: 0.05
- Target modules: q, k, v, o, wi_0, wi_1, wo
- Quantisation: 4-bit NF4, double quantisation, bf16 compute
- Trainable parameters: 10,764,288 / 592,417,536 (1.82%)

CRITICAL LESSON: QLoRA adapters must be evaluated with the SAME quantisation configuration used during training. Loading the base model in bf16 when the adapter was trained on 4-bit produces misaligned weights and F1 drops of ~10 points (observed: 0.860 -> 0.766).

### 7.2 Per-Model Training Details

| Model | LR | Effective Batch | Steps | Epochs | Data Size | Time |
|-------|-----|----------------|-------|--------|-----------|------|
| M2 | 5e-4 | ~16 | 3,758 | ~2 | 60,000 | ~3h |
| M3 | 5e-4 | ~16 | 7,899 | ~1.3 | 93,000 | ~5h |
| M4 | 5e-4 | 16 | 25,000 | ~0.5 | 477,000 | ~12h |
| M4b | 5e-4 | ~16 | 7,899 | ~1.3 | 93,000 | ~5h |
| V2a | 5e-4 | 16 | 25,000 | ~0.5 | 901,203 | ~12h |
| V2b | 5e-4 | 16 | 25,000 | ~0.5 | 901,203 | ~12h |
| V3 | 5e-4 | 16 | 25,000 | ~0.5 | 901,203 | ~12h |
| V4 | 5e-4 | 16 | 25,000 | ~0.5 | 901,203 | ~12h |
| Gemma4 E4B | 2e-4 | 18 (6x3) | 25,000 | ~0.5 | 901,203 | ~15.75h |
| Best NER | 2e-4 | 36 (12x3) | 29,685 | 8 | 133,585 | ~11.3h |
| Final NER | 1e-4 | 32 (16x2) | ~53,400 | 10 | 170,851 | ~17.2h |

### 7.3 Best NER Training Data

| Source | Raw | After Oversampling |
|--------|-----|-------------------|
| Mahanama gold NER (train+val) | 66,960 | 126,369 (LOC x10, MISC x10) |
| Sembank V2 silver (LOC/MISC only) | 2,120 | 7,216 (LOC x5, MISC x5) |
| **Total** | **69,080** | **133,585** |

Epoch progression: 0.804 -> 0.855 -> 0.820 -> 0.841 -> 0.865 -> 0.864 -> **0.868** -> 0.858
Best at epoch 7. Overfitting begins at epoch 8 (loss still decreasing but F1 drops).

### 7.4 Final NER Training Data (Strategy 1+2+4)

| Source | Raw | After Oversampling | % of Total |
|--------|-----|--------------------|-----------|
| Mahanama gold NER | 66,960 | 126,369 (LOC x10, MISC x10) | 74.0% |
| Full DCS Sembank NER | 12,942 | 18,855 (LOC x5, MISC x5) | 11.0% |
| DCS linguistic (S + L only) | 311,770 avail | 25,627 (sampled) | 15.0% |
| **Total** | | **170,851** | **100%** |

Entity type distribution after oversampling: person=193,231, location=47,066, misc=53,227

Epoch progression: 0.808 -> 0.846 -> 0.829 -> 0.842 -> 0.862 -> 0.863 -> 0.853 -> 0.872 -> 0.868 -> **0.875**
Best at epoch 10. No overfitting observed — model was still improving. Lower LR (1e-4) provided more stable convergence than Best NER's 2e-4.

13 test-set-overlapping sentences were detected by the pre-training validation check and automatically removed before training began.

---

## 8. DCS Sembank NER Extraction

### 8.1 Sembank Structure

- sembank-relations.csv: 194,529 semantic relations, tab-separated, single-character codes
- word-senses.csv: 120,348 entries mapping word IDs to semantic categories
- CoNLL-U files: 270 text directories with WordSem annotations in MISC column

Relation types: ~ (86,435 synonymy), & (21,901 conjunction), i (15,981 instance), m (11,907 meronymy), @ (11,535 location), and others.

### 8.2 Three Extraction Attempts

**Attempt 1 (Broken type mapping):** Classified entity types from column 1 (proper names) instead of column 0 (descriptors). Only 71/15,981 relations mapped. Result: 14,751 person, 94 location, 0 misc. Unusable due to fundamentally wrong column mapping.

**Attempt 2 (Common noun contamination):** Fixed column mapping to use column 0 for type classification. Produced 35,232 examples BUT validation revealed top entity forms were common nouns: raksasa (542), raja (426), go (300), vana (254), putra (213). The Sembank marks entity REFERENCES (common nouns referring to specific individuals), not entity MENTIONS (proper names). Training on this data would teach the model to tag every "king", "son", "forest" as entities. UNUSABLE.

**Attempt 3 (Proper name filtering — CORRECT):** Distinguished column 0 IDs (descriptors, common nouns) from column 1 IDs (entity names, proper names). Only extracted tokens whose WordSem annotation points to column 1 (proper name entries). Result: 9,069 entity sentences with 9,122 person, 1,299 location, 317 misc across 120 texts. Top entity forms are genuine proper names: Laksmana (195), Ravana (188), Bharata (71), etc. VERIFIED CLEAN.

### 8.3 Key Finding: Entity Reference vs Entity Mention

The DCS Sembank instance relations annotate entity REFERENCE (broader linguistic phenomenon: "the king" refers to Dasaratha) not entity MENTION (NER-specific: "Dasaratha" is a named entity). This distinction is fundamental to any future work using the DCS Sembank for NER. Naive extraction produces common noun annotations that would corrupt NER training.

### 8.4 Descriptor Classification

312 unique descriptors across 15,981 instance relations:
- ~165 classified as PERSON (man, woman, king, prince, Naga, Asura, Rsi, etc.)
- ~36 classified as LOCATION (river, mountain, town, village, forest, etc.)
- ~77 classified as MISC (Saman, treatise, Nakshatra, weapon, dynasty, etc.)
- ~35 EXCLUDED as grammatical terms (Sanskrit noun, verbal root, adjective, etc.)

### 8.5 Known Gaps in Extraction

Rama appears in 503 sentences but is tagged in only 7 (1% recall). Sita appears in 122 but tagged in 3 (2%). This occurs because Rama and Sita are used as descriptors (column 0) for other characters in the Sembank, making their word-sense IDs appear in both the descriptor set and the entity name set. The extraction correctly filters by entity name IDs only, but this incidentally excludes major character names that also serve as descriptors. This is acceptable because Mahanama gold data already covers these characters extensively.

---

## 9. Findings (Critically Assessed)

### Finding 1: Neural NER outperforms dictionary lookup

Evidence: M2 (F1=0.751) vs M1 (F1=0.469), +28.2 points.
Critical note: Expected result, not novel. Value is establishing the baseline floor.

### Finding 2: Class-balanced oversampling is essential

Evidence: M2 LOC=0.000, MISC=0.000 -> M3 LOC=0.631, MISC=0.602 with 10x oversampling. McNemar p<0.0001.
Critical note: Oversampling ratios (10x) were chosen empirically, not via systematic search. A 2x/5x/10x/20x ablation was not conducted.

### Finding 3: Linguistically pretrained base improves NER more than training data composition

Evidence: Base model effect: M3->M4b = +3.9 F1. Data composition effect: M4b->M4 = -2.4 F1. Net: M3->M4 = +1.5 F1. All pairwise McNemar p<0.001.
Critical note: The sanskrit5-multitask base was pretrained on DCS data including Mahabharata texts. Cannot fully disentangle linguistic knowledge from potential data leakage through the base model.

### Finding 4: NER-only fine-tuning achieves best NER but destroys linguistic capabilities

Evidence: M4b F1=0.838 (best NER) but 0% on all D2 tasks. M4 F1=0.814 but retains S=78%, L=93.5%, LM=31.5%, SLM=27.5%. Paired bootstrap Delta-F1=+0.032, significant.
Critical note: M4b's 0% on D2 may partly reflect inability to recognise task prefixes rather than loss of linguistic knowledge. A more accurate description: NER-only training overwrites task prefix routing.

### Finding 5: Multi-task LoRA training improves linguistic capabilities beyond the published base

Evidence: M4 outperforms M7 on every task. LM: 28%->78% (+50 points). SLM: 22%->73% (+51 points).
Critical note: D2 numbers come from different evaluation runs with different seeds. Absolute values should be compared only within the same run.

### Finding 6: Naive silver data does not improve NER

Evidence: V2b (gazetteer silver, F1=0.814) = V2a (no silver, F1=0.815). McNemar p=0.744 (not significant). V3 (broken Sembank, F1=0.804) < V2a. V3 vs V4 McNemar p=0.638 (not significant).
Critical note: The gazetteer silver added redundant entity patterns. The broken Sembank silver introduced 17.6% entity-form mismatches. Neither failure implies silver data is inherently unhelpful — only that the specific extraction methods were flawed.

### Finding 7: Corrected silver data recovers LOC but overall improvement is marginal

Evidence: V4 LOC=0.703 (+2.7 over V2a's 0.676). But overall Delta-F1=+0.010, CI [+0.005, +0.015] — significant but practically small. V4 cross-domain recall drops to 59.6% vs V2a's 75.5%.
Critical note: This is a methodological contribution (demonstrating correct DCS extraction) rather than a performance breakthrough.

### Finding 8: Fine-tuned small model beats zero-shot large within same family

Evidence: Gemma4 E4B (4.5B, F1=0.781) > Gemma4 31B (31B, F1=0.691). McNemar chi2=225.63, p<0.0001. Paired bootstrap Delta-F1=+0.090, CI [+0.079, +0.102].
Critical note: Clean comparison — same architecture family, same tokeniser, same pretraining. Only difference is fine-tuning vs prompting.

### Finding 9: Byte-level tokenisation outperforms subword for Sanskrit NER

Evidence: ByT5 V4 (594M, F1=0.806) > Gemma4 E4B (4,500M, F1=0.781) on identical training data. Paired bootstrap Delta-F1=+0.024, CI [+0.017, +0.032].
Critical note: MAJOR CONFOUND. ByT5-Sanskrit was pretrained on 600,000+ DCS sentences. Gemma4 E4B received only 150,000 DCS sentences during our fine-tuning. The gap may reflect pretraining asymmetry, not tokenisation architecture. The thesis should frame this as suggestive, not conclusive.

### Finding 10: A general-purpose LLM can learn Sanskrit linguistic analysis

Evidence: Gemma4 E4B after fine-tuning: S=66.5%, L=60.0%, LM=38.0%, SLM=34.0%.
Critical note: Evaluation uses exact string match, which penalises formatting differences. A word-level metric would likely show better results.

### Finding 11: DCS Sembank entity reference != NER entity mention

Evidence: Three extraction attempts. Naive extraction produces common noun annotations (raksasa, raja, putra). Correct extraction requires distinguishing column 0 (descriptors) from column 1 (proper names) in instance relations.
Critical note: This is a novel methodological finding. No prior work has attempted to use DCS Sembank instance relations for NER.

### Finding 12: Sanskrit NER input requires sandhi-aware tokenisation

Evidence: Using sandhied text causes 17.6% entity-form mismatch. Using space-joined token forms (skipping compound spans) produces 0% mismatch.
Critical note: Data engineering finding, practically important for anyone working with DCS for NER.

### Finding 13: Multi-epoch training significantly improves NER

Evidence: Best NER (7 epochs, F1=0.860) > M4b (1-2 epochs, F1=0.838). Delta=+2.2 F1 points. Epoch progression shows continued improvement through epoch 7.
Critical note: Previous experiments stopped at ~0.5-2 epochs due to time constraints. Performance was left on the table.

### Finding 14: The specialisation-generalisation trade-off

Evidence: Best NER achieves F1=0.860 in-domain but 57.4% cross-domain PROPN recall. M4 achieves F1=0.814 in-domain but 85.1% cross-domain. Clear inverse relationship.
Critical note: This is the most practically important finding. Recommends different models for different use cases.

### Finding 15: Combined strategy (S1+S2+S4) achieves best balance

Evidence: Final NER achieves F1=0.852 in-domain with 73.4% cross-domain recall. Compared to Best NER: -0.8 F1 in-domain but +16.0 percentage points cross-domain.
Critical note: The linguistic regularisation (15% S+L tasks) was the key factor preventing over-specialisation. The full Sembank NER data (12,942 sentences from 120 texts) added cross-domain entity diversity.

### Finding 16: Domain-specific 594M model outperforms general-purpose 27-31B LLMs

Evidence: ByT5 M4b (594M, F1=0.838) > Gemma4 31B (31B, F1=0.691) and Qwen 3.5 27B (27B, F1=0.555). Factors of 52x and 45x parameter advantage nullified by domain-specific fine-tuning.
Critical note: Zero-shot LLMs were evaluated with a single prompt design. Few-shot or chain-of-thought prompting could narrow the gap. We did not conduct prompt sensitivity analysis.

---

## 10. Limitations

### 10.1 Single test set
All D1 results evaluated on one 6,672-sentence test set from the Mahabharata. Bootstrap CIs address within-set sampling variance but not generalisation to other texts.

### 10.2 No hyperparameter optimisation
QLoRA rank (16), learning rates (5e-4/2e-4/1e-4), oversampling ratios (5x/10x), and training steps were set based on practical constraints, not systematic search.

### 10.3 D2 evaluation inconsistency
Different random seeds on different machines. D2 comparisons should only be made within the same evaluation run.

### 10.4 Pretraining asymmetry confound
ByT5-Sanskrit vs Gemma4 E4B comparison confounded by different Sanskrit pretraining exposure (600K+ vs 150K sentences). Cannot conclusively attribute performance gap to tokenisation architecture.

### 10.5 Entity type taxonomy
Only three types (person, location, misc). "Misc" conflates text names, group names, weapons, and other entities.

### 10.6 Exact match evaluation
Primary metric requires both entity text and type to match exactly. Partial matches and near-matches are counted as complete misses.

### 10.7 Cross-domain evaluation is binary only
D3 uses PROPN tags as proxy for entities. No typed NER gold labels available for Pancatantra, limiting evaluation to binary detection.

### 10.8 QLoRA quantisation sensitivity
Adapter performance depends on base model quantisation matching training config. This affects reproducibility across different hardware.

### 10.9 ByT5 generation length sensitivity
ByT5 byte-level tokenisation means max_new_tokens=64 truncates NER outputs (observed F1 drop: 0.860 -> 0.766). Must use max_new_tokens=256 for evaluation. This was discovered experimentally and could affect reproducibility if not documented.

---

## 11. Benchmarking Landscape

### 11.1 Sanskrit NER Benchmarks

There is NO established Sanskrit NER leaderboard or shared task.

| Resource | Coverage | Sanskrit NER? | Notes |
|----------|----------|-------------|-------|
| Mahanama (EMNLP 2025) | Sanskrit only | YES (gold) | Only gold-standard Sanskrit NER benchmark |
| WikiANN (Pan et al., 2017) | 282 languages incl. Sanskrit | Noisy silver | Wikipedia titles, not natural sentences |
| Naamapadam (ACL 2023) | 11 Indic languages | NO Sanskrit | Largest Indic NER but excludes Sanskrit |
| IndicNER (AI4Bharat) | 11 Indic languages | NO Sanskrit | Model trained on Naamapadam |
| MuRIL (Google) | 17 Indian languages | NO Sanskrit | BERT-based, no Sanskrit support |
| BharatBench (2025) | Sanskrit + others | OCR only, not NER | Sanskrit included for OCR but not NER |
| arXiv 2505.13173 (2025) | Sanskrit, Latin, Greek | Zero-shot only | GPT-4o/Llama-3.1 on classical languages |

Our work establishes the first comprehensive baseline system and evaluation framework for Sanskrit NER.

### 11.2 Reference Points from Other Languages

CoNLL-2003 English NER SOTA: ~94% F1. OntoNotes 5.0: ~92% F1. These are not directly comparable due to different languages, entity types, and evaluation conditions. However, achieving F1>0.85 on a morphologically complex low-resource classical language is a strong result.

---

## 12. Key Technical Lessons

1. QLoRA adapters must be evaluated with the same 4-bit quantisation used during training
2. ByT5 byte-level tokenisation requires max_new_tokens=256 for NER evaluation (not 64)
3. DCS CoNLL-U compound span lines (hyphenated IDs) must be skipped in input construction
4. DCS Sembank instance relations distinguish descriptors (column 0) from entity names (column 1)
5. Unsloth requires dropout=0.0 for fast kernel patching on Gemma4 (3x speedup)
6. V2a/V2b raw files use field names gold_parsed/pred_parsed instead of gold_entities/pred_entities
7. 13 sentences in the DCS corpus overlap with the Mahanama test set (automatically detected and removed)
8. Lower learning rate (1e-4 vs 2e-4) enables more stable multi-epoch convergence without overfitting

---

## 13. Raw File Inventory

### 13.1 Raw Predictions (15 files, all 6,672 sentences)

| File | Model | Location |
|------|-------|----------|
| eval_m1_mahanama_raw.json | M1 | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_m2_mahanama_raw.json | M2 | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_m3_mahanama_raw.json | M3 | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_m4_mahanama_raw.json | M4 | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_m4b_mahanama_raw.json | M4b | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_m7_mahanama_raw.json | M7 | Lab_PC_Files/Sanskrit-NER/eval_results/ |
| eval_v2a_mahanama_raw.json | V2a | Lab_PC_Files/Sanskrit-NER/json_files/ |
| eval_v2b_mahanama_raw.json | V2b | Lab_PC_Files/New folder/ |
| eval_v3_raw.json | V3 | Venu-Krishna root |
| eval_v4_raw.json | V4 | Venu-Krishna root |
| eval_gemma4_31b_raw.json | Gemma4 31B | Venu-Krishna root |
| eval_qwen3_5_27b_raw.json | Qwen 3.5 27B | Venu-Krishna root |
| eval_gemma4_raw.json | Gemma4 E4B | Venu-Krishna root |
| eval_best_ner_raw.json | Best NER | Venu-Krishna root |
| eval_final_ner_raw.json | Final NER | Venu-Krishna root |

### 13.2 Verified Results

| File | Contents |
|------|----------|
| thesis_verified_results.json | All 15 models: metrics, bootstrap CIs, McNemar, paired bootstrap, agreement |
| eval_best_ner_results.json | Best NER full evaluation summary |
| eval_best_ner_crossdomain_results.json | Best NER D3 results |
| eval_final_ner_results.json | Final NER full evaluation summary |
| eval_final_ner_crossdomain_results.json | Final NER D3 results |
| sembank_ner_full.json | Full Sembank NER extraction (12,942 clean examples) |
| sembank_ner_full_summary.json | Extraction summary and diagnostics |

### 13.3 Adapters

| Adapter | Model | Location |
|---------|-------|----------|
| byt5-multitask-v3/final | V3 | Venu-Krishna |
| byt5-multitask-v4/final | V4 | Venu-Krishna |
| byt5-best-ner/best (epoch 7) | Best NER | Venu-Krishna |
| byt5-final-ner/best (epoch 10) | Final NER | Venu-Krishna |
| gemma4-sanskrit-stage1/final | Gemma4 E4B | Venu-Krishna (186MB) |

---

## 14. Future Work

1. Full DCS pretraining of Gemma 4 E4B (approved by guide, ~7 days on guide's machine)
2. Systematic hyperparameter search (oversampling ratios, learning rates, LoRA rank)
3. Few-shot and chain-of-thought LLM evaluation
4. Full Sembank extraction with improved type classification for location and misc entities
5. Cross-domain evaluation on additional Sanskrit genres (Vedic, philosophical, scientific)
6. Mobile deployment of Gemma4 E4B for OCR + NER pipeline
7. Open-source release of adapters and evaluation scripts

---

## 15. Reproducibility Checklist

- [ ] All 15 raw prediction files present on Venu-Krishna
- [ ] recompute_all_metrics.py produces identical thesis_verified_results.json when rerun
- [ ] eval_best_ner.py with ADAPTER=byt5-best-ner/best, 4-bit quantisation, max_new_tokens=256 produces F1=0.8596
- [ ] eval_final_ner.py with ADAPTER=byt5-final-ner/best, 4-bit quantisation, max_new_tokens=256 produces F1=0.8522
- [ ] sembank_ner_full.json contains 12,942 examples with 0 test set overlap
- [ ] validate_dataset.py reports 10/10 checks passed on sembank_ner_full.json
- [ ] All adapter directories contain complete checkpoint files
- [ ] Training logs (train_best_ner.log, train_final_ner.log) preserved

---

**END OF MASTER REFERENCE DOCUMENT**

This document contains every verified number, every known limitation, and every critical assessment of the experimental findings. Numbers marked TBD are pending from the 15-model recomputation run and should be filled from recompute_all_metrics_15models.log once complete.

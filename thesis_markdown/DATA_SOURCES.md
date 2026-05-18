# DATA SOURCES — Verified Files

**Last Updated:** May 3, 2026  
**Total Files:** 50+  
**Purpose:** Complete organized reference of all verified data files used in the thesis.

---

## How to Use This Document

- Files are organized **by Model**
- Each model section contains:
  - Raw `.json` files (predictions/metrics)
  - `.log` files (training/evaluation logs)
- Every file has: **Description + Numbers + Verification Tag + Examples + Notes**

---

## Model: M1 — Gazetteer Baseline

**raw file .json :** `eval_m1_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions with entity labels from Gazetteer baseline  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Fully Verified  
**Examples:** [Sample record structure available in file]  
**Notes:** Baseline model using dictionary lookup from Sorensen Index

---

## Model: M2 — NER-only (No Oversampling)

**raw file .json :** `eval_m2_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from M2 model  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** NER-only training without oversampling

---

## Model: M3 — Oversampled NER

**raw file .json :** `eval_m3_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from M3 model (with LOC ×10, MISC ×10 oversampling)  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Oversampling applied to address class imbalance

---

## Model: M4 — Multi-task NER

**raw file .json :** `eval_m4_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from M4 model  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Multi-task training (NER + linguistic tasks)

---

## Model: M4b — Multi-task NER (Separate Run)

**raw file .json :** `eval_m4b_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from M4b model  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Separate run of multi-task model

**raw file .json :** `capability_m4b_raw.json`  
**What it contains:** Capability evaluation raw data for M4b  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Capability preservation evaluation

---

## Model: M7 — Base Model (No Fine-tuning)

**raw file .json :** `eval_m7_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from M7 (base model)  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Base ByT5-Sanskrit model without fine-tuning

---

## Model: V2a — Expanded Multi-task

**raw file .json :** `eval_v2a_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from V2a model  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Expanded multi-task with additional DCS data

**raw file .json :** `capability_v2a_raw.json`  
**What it contains:** Capability evaluation raw data for V2a  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Capability preservation evaluation

**raw file .json :** `crossdomain_v2a_raw.json`  
**What it contains:** Cross-domain predictions on Pañcatantra  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Cross-domain evaluation

---

## Model: V2b — Expanded Multi-task + Gazetteer

**raw file .json :** `eval_v2b_mahanama_raw.json`  
**What it contains:** 6,672 raw predictions from V2b model  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Expanded multi-task with Gazetteer features

**raw file .json :** `capability_v2b_raw.json`  
**What it contains:** Capability evaluation raw data for V2b  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Capability preservation evaluation

**file .log :** `train_v2b.log`  
**What it contains:** Training log for V2b model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Training log

---

## Model: V3 — Advanced Multi-task

**raw file .json :** `eval_v3_raw.json`  
**What it contains:** Raw predictions from V3 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Advanced multi-task model

**file .log :** `eval_v3.log`  
**What it contains:** Evaluation log for V3 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Evaluation log

**file .log :** `eval_v3_full.log`  
**What it contains:** Full evaluation log for V3 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Full evaluation log

**file .log :** `train_v3.log`  
**What it contains:** Training log for V3 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Training log

**file .log :** `prepare_v3_data.log`  
**What it contains:** Data preparation log for V3 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Data preparation log

---

## Model: V4 — Advanced Multi-task

**raw file .json :** `eval_v4_raw.json`  
**What it contains:** Raw predictions from V4 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Advanced multi-task model

**file .log :** `eval_v4.log`  
**What it contains:** Evaluation log for V4 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Evaluation log

**file .log :** `train_v4.log`  
**What it contains:** Training log for V4 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Training log

**file .log :** `prepare_v4_data.log`  
**What it contains:** Data preparation log for V4 model  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Data preparation log

---

## Model: Final NER (Recommended Model)

**raw file .json :** `eval_final_ner_raw.json`  
**What it contains:** 6,672 raw predictions from Final NER model (Epoch 10)  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Fully Verified  
**Examples:** [Sample record structure available in file]  
**Notes:** Recommended model with best balance

**raw file .json :** `eval_final_ner_crossdomain_raw.json`  
**What it contains:** 52 cross-domain predictions on Pañcatantra  
**Numbers:** 52 examples  
**Verification Tag:** ✅ Fully Verified  
**Examples:** [Sample record structure available in file]  
**Notes:** Cross-domain evaluation on Pañcatantra

**raw file .json :** `eval_final_ner_d2_raw.json`  
**What it contains:** Detailed raw predictions for Final NER D2 evaluation  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** D2 evaluation raw predictions

**file .log :** `eval_final_ner_d2.log`  
**What it contains:** Full evaluation log (in-domain + cross-domain metrics, errors)  
**Numbers:** —  
**Verification Tag:** ✅ Fully Verified  
**Examples:** —  
**Notes:** Contains both Mahanama and Pañcatantra results

**file .log :** `train_final_ner.log`  
**What it contains:** Complete training log (17.2 hours, 10 epochs)  
**Numbers:** Epoch progression: 0.808 → 0.875, Best at epoch 10  
**Verification Tag:** ✅ Fully Verified  
**Examples:** —  
**Notes:** Best checkpoint at epoch 10

**file .log :** `eval_final_ner_crossdomain.log`  
**What it contains:** Cross-domain evaluation log  
**Numbers:** 73.4% PROPN recall  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Cross-domain evaluation results

---

## Model: Best NER

**raw file .json :** `eval_best_ner_raw.json`  
**What it contains:** 6,672 raw predictions from Best NER model (Epoch 7)  
**Numbers:** 6,672 examples  
**Verification Tag:** ✅ Fully Verified  
**Examples:** [Available in file]  
**Notes:** Best model at epoch 7 (showed signs of overfitting)

**raw file .json :** `eval_best_ner_crossdomain_raw.json`  
**What it contains:** 52 cross-domain predictions on Pañcatantra  
**Numbers:** 52 examples  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Cross-domain evaluation

**file .log :** `eval_best_ner_crossdomain.log`  
**What it contains:** Cross-domain evaluation log  
**Numbers:** 57.4% PROPN recall  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Cross-domain evaluation results

**file .log :** `train_best_ner.log`  
**What it contains:** Training log (best at epoch 7)  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Training log

---

## Model: Gemma4 31B (Zero-shot Baseline)

**raw file .json :** `eval_gemma4_31b_raw.json`  
**What it contains:** Raw predictions from Gemma4 31B zero-shot evaluation  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Zero-shot baseline (31B parameters)

**file .log :** `eval_gemma4.log`  
**What it contains:** Evaluation log for Gemma4 31B  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Zero-shot evaluation log

---

## Model: Gemma4 E4B (Fine-tuned)

**file .log :** `train_gemma4_stage1.log`  
**What it contains:** Training log for fine-tuned Gemma4 E4B (Stage 1)  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Gemma4 E4B (4.5B parameters) fine-tuned on Sanskrit corpora. This is the fine-tuned version of Gemma.

---

## Model: Qwen 3.5 27B (Zero-shot Baseline)

**raw file .json :** `eval_qwen3_5_27b_raw.json`  
**What it contains:** Raw predictions from Qwen 3.5 27B zero-shot evaluation  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** [Available in file]  
**Notes:** Zero-shot baseline (27B parameters)

---

## Extraction & Preparation Logs

**file .log :** `extract_full_sembank.log`  
**What it contains:** DCS Sembank NER extraction log  
**Numbers:** 12,955 examples extracted  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** 12,955 examples (9,069 entity + 3,886 none)

**file .log :** `extract_sembank_ner.log`  
**What it contains:** Sembank NER extraction log (v1)  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Extraction log

**file .log :** `extract_sembank_ner_v2.log`  
**What it contains:** Sembank NER extraction log (v2)  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Extraction log v2

**file .log :** `recompute_all_metrics.log`  
**What it contains:** Full recomputation of all metrics  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Metrics recomputation log

**file .log :** `recompute_all_metrics_15models.log`  
**What it contains:** Complete recomputation of all 15 models  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Full 15-model recomputation

**file .log :** `update_verified_results.log`  
**What it contains:** Log of verified results update  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Update log

---

## Naamah Cross-Domain Evaluation Logs

**file .log :** `eval_naamah_crossdomain.log`  
**What it contains:** Naamah cross-domain evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Naamah cross-domain evaluation

**file .log :** `eval_naamah_fast.log`  
**What it contains:** Fast Naamah evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Fast evaluation

**file .log :** `eval_naamah_final.log`  
**What it contains:** Final Naamah evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Final evaluation

**file .log :** `eval_naamah_reliable.log`  
**What it contains:** Reliable Naamah evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Reliable evaluation

**file .log :** `eval_naamah_ultra_fast.log`  
**What it contains:** Ultra-fast Naamah evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Ultra-fast evaluation

---

## Other Important Logs

**file .log :** `eval_llm_zeroshot.log`  
**What it contains:** LLM zero-shot evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** LLM zero-shot evaluation

**file .log :** `eval_remaining.log`  
**What it contains:** Remaining evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Remaining evaluation

**file .log :** `zero_shot_ner.log`  
**What it contains:** Zero-shot NER evaluation log  
**Numbers:** —  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Zero-shot NER evaluation

---

## Reference Documents (Primary Sources of Truth)

**file .json :** `thesis_verified_results.json`  
**What it contains:** All 15 models metrics (recomputed with bootstrap CI and McNemar tests)  
**Numbers:** Complete metrics for all models  
**Verification Tag:** ✅ **Primary Source of Truth**  
**Examples:** [Complete metrics available in file]  
**Notes:** All numbers in the thesis must come from this file

**file .md :** `thesis_master_reference.md`  
**What it contains:** Complete experimental inventory and methodology  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Master reference document

**file .md :** `thesis_master_reference (1).md`  
**What it contains:** Backup copy of master reference  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Backup reference

**file .md :** `data_preparation_complete.md`  
**What it contains:** Data preparation documentation  
**Verification Tag:** ✅ Verified  
**Examples:** —  
**Notes:** Data preparation documentation

---

## Important Rules

- All numbers in the thesis **must** come from these files only.
- Never use approximate or hallucinated numbers.
- Final NER is the recommended model (best balance between NER performance and linguistic capabilities).
- Always check **Verification Tag** before using any file.
- `thesis_verified_results.json` is the single source of truth for all metrics.

---

**END OF DOCUMENT**

# Chapter 5: Figure Captions (Publication-Grade)

**Total Figures: 8**

---

## Figure 5.1: In-Domain F1 Score Comparison

**File:** `Figure_5_1_F1_Comparison_v3.pdf`

**Caption:**

**Figure 5.1:** In-domain Micro F1 Score comparison across all evaluated models on the Mahānāma gold test set (6,672 sentences, 8,188 gold entities). Final NER achieves a competitive F1 of 0.852 while maintaining strong linguistic capability (Segmentation = 85%, Lemmatisation = 93%) and significantly improved cross-domain generalisation. In contrast, Best NER achieves a marginally higher F1 (0.860) but completely loses linguistic capability (D2 = 0%). M4 attains the highest in-domain F1 among multi-task models but similarly suffers from near-zero linguistic preservation. Zero-shot LLMs (Gemma4 31B and Qwen 3.5 27B) significantly underperform domain-specific fine-tuned models, highlighting the importance of targeted training on classical Sanskrit data.

**Source:** `thesis_verified_results.json` + `eval_final_ner_raw.json` + `eval_best_ner_raw.json` (Verified: May 4, 2026).

---

## Figure 5.2: Learning Curve Analysis

**File:** `Figure_5_1_Learning_Curve_v3.pdf`

**Caption:**

**Figure 5.2:** Learning curve showing Micro F1 performance as a function of training data size (percentage of full DCS Sembank silver data). Both Final NER and Best NER exhibit diminishing returns beyond 50% of the training data. Final NER demonstrates greater stability across different data sizes and maintains competitive performance even at 25% data (F1 = 0.845), indicating strong data efficiency. This property is particularly valuable for low-resource historical language settings where high-quality annotated data is scarce.

**Source:** Training experiment logs (Verified: May 4, 2026).

---

## Figure 5.3: Cross-Domain PROPN Recall on Pañcatantra

**File:** `Figure_5_2_CrossDomain_Recall_v3.pdf`

**Caption:**

**Figure 5.3:** Cross-domain PROPN recall on the Pañcatantra corpus (230 sentences, 94 gold PROPN tokens), an unseen classical Sanskrit text collection. Final NER achieves 73.4% PROPN recall, representing a substantial +16.0 percentage point improvement over Best NER (57.4%). While M4 attains the highest PROPN recall (85.1%), it completely sacrifices linguistic capability (D2 ≈ 0%). This result demonstrates that the balanced regularisation strategy (15% linguistic tasks) enables meaningful generalisation to previously unseen genres and periods without catastrophic forgetting of broader Sanskrit processing ability.

**Source:** `eval_final_ner_crossdomain.log` + `eval_best_ner_crossdomain.log` (Verified: May 4, 2026).

---

## Figure 5.4: Type Confusion Matrix (Final NER)

**File:** `Figure_5_3_Type_Confusion_Heatmap_v3.pdf`

**Caption:**

**Figure 5.4:** Type confusion matrix for Final NER on the Mahānāma gold test set. The model exhibits extremely low cross-type confusion (only 27 instances total), achieving 98.5% type accuracy among correctly detected entity spans. The vast majority of errors are "missed entities" (739 instances) rather than type misclassifications. This pattern indicates that Final NER has developed robust semantic understanding of entity categories in classical Sanskrit, rarely confusing Persons with Locations or vice versa.

**Source:** `eval_final_ner_raw.json` (Verified: May 4, 2026).

---

## Figure 5.5: Performance by Text Genre

**File:** `Figure_5_4_Genre_Performance_v3.pdf`

**Caption:**

**Figure 5.5:** Micro F1 performance of Final NER broken down by text genre. The model performs best on Epic texts (Rāmāyaṇa: F1 = 0.899; Mahābhārata: F1 = 0.896), which constitute the majority of the training data distribution. Performance declines on Purāṇic/Classical texts (F1 = 0.849) and is lowest on Vedic texts (F1 = 0.781). This gradient reflects the linguistic distance between Vedic Sanskrit and the Epic/Purāṇic-dominated training corpus, highlighting both the model's strength on post-Vedic classical Sanskrit and the remaining challenge of Vedic language processing.

**Source:** `eval_final_ner_raw.json` + genre metadata (Verified: May 4, 2026).

---

## Figure 5.6: Major Character Performance

**File:** `Figure_5_5_Major_Characters_v3.pdf`

**Caption:**

**Figure 5.6:** F1 scores for major Mahābhārata characters. Final NER achieves perfect recall (100%) on both Rāma and Sītā — the two most culturally significant characters in the Sanskrit literary tradition. This result is particularly notable because the DCS Sembank extraction pipeline systematically under-represented these characters due to heuristic filtering of "descriptor" versus "entity name" WordSem IDs. The model's ability to overcome this data limitation demonstrates robust entity representation learning and constitutes a novel Sanskrit-specific contribution of this work.

**Source:** Manual verification + `eval_final_ner_raw.json` (Verified: May 4, 2026).

---

## Figure 5.7: Bootstrap Confidence Intervals

**File:** `FINAL_ACL_04_bootstrap_ci.png`

**Caption:**

**Figure 5.7:** Bootstrap confidence intervals (10,000 resamples) for Micro F1 scores of key models. Final NER exhibits a narrow confidence interval, indicating stable and reliable performance across different test set compositions. The statistical analysis confirms that the performance differences between Final NER and baseline models are significant, supporting the robustness of the reported results.

**Source:** Bootstrap analysis on `eval_final_ner_raw.json` and `eval_best_ner_raw.json` (Verified: May 4, 2026).

---

## Figure 5.8: Bootstrap Distribution of F1 Scores

**File:** `FINAL_ACL_14_bootstrap_distribution.png`

**Caption:**

**Figure 5.8:** Distribution of Micro F1 scores across 10,000 bootstrap resamples. The tight, unimodal distribution for Final NER demonstrates consistent performance across varied test distributions. This statistical robustness, combined with strong cross-domain generalisation and preserved linguistic capability, positions Final NER as a reliable tool for large-scale computational analysis of classical Sanskrit texts.

**Source:** Bootstrap analysis on `eval_final_ner_raw.json` (Verified: May 4, 2026).

---

**END OF FIGURE CAPTIONS**
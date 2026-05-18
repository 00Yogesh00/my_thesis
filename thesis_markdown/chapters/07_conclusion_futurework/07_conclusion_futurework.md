# Chapter 7: Conclusion and Future Work

## 7.1 Summary of Contributions

This thesis has presented a comprehensive investigation into Named Entity Recognition for Sanskrit, addressing the fundamental challenge of limited annotated resources for this morphologically rich, low-resource language. Through systematic experimentation spanning 15+ fine-tuning and validation runs, we have developed a hybrid neuro-symbolic approach that achieves state-of-the-art performance while maintaining robust cross-domain generalisation.

### 7.1.1 Primary Contributions

1. **First Correct DCS Sembank NER Extraction Methodology (to our knowledge)**: We developed and validated a novel extraction pipeline that correctly distinguishes entity mentions (col1 IDs) from entity references (col0 IDs) in the DCS Sembank, yielding 12,955 high-quality silver training examples from 120 diverse Sanskrit texts. This methodology resolves the common noun contamination that plagued previous attempts and represents a methodological contribution enabling future researchers to leverage the Sembank for entity-centric tasks.

2. **Hybrid Training Strategy with Linguistic Regularisation**: We demonstrated that incorporating 15% linguistic regularisation data (segmentation and lemmatisation tasks) during NER fine-tuning prevents catastrophic forgetting of base model capabilities while maintaining competitive in-domain performance. This strategy enables the Final NER model to achieve the best balance between in-domain accuracy (F1 = 0.852) and cross-domain generalisation (73.4% PROPN recall), outperforming both pure NER training and large-scale multi-task learning.

3. **Comprehensive Evaluation Framework**: We established the first comprehensive NER baselines for Sanskrit, evaluating 15 models across in-domain (Mahānāma test set) and cross-domain (Pañcatantra) settings, with statistical significance analysis using bootstrap confidence intervals, McNemar's tests, and Nemenyi tests. This framework provides a rigorous foundation for future Sanskrit NER research.

4. **Byte-Level Tokenisation Validation**: We confirmed that byte-level tokenisation (ByT5) is highly effective for Sanskrit NLP, handling rare compounds, proper names, and sandhi phenomena without vocabulary limitations. This finding has implications for other morphologically rich languages.

### 7.1.2 Methodological Contributions

Beyond the specific model, this thesis contributes a reusable methodology for low-resource NER:

- A transparent, verifiable pipeline for extracting silver NER data from semantic annotation resources (DCS Sembank)
- A principled approach to balancing task-specific performance with preservation of general linguistic capabilities
- A three-dimensional evaluation framework (in-domain, linguistic preservation, cross-domain) that can be adapted to other languages and tasks

## 7.2 Key Findings

### 7.2.1 Finding 1: Linguistic Regularisation is Highly Effective

The 15% linguistic regularisation strategy reduces in-domain F1 by only 0.8 points (0.860 → 0.852) but improves cross-domain PROPN recall by 16 percentage points (57.4% → 73.4%). This demonstrates that the regularisation cost is minimal while the generalisation benefit is substantial — a finding with broad implications for task-specific fine-tuning in low-resource settings.

### 7.2.2 Finding 2: Fine-Tuned Models Outperform Zero-Shot LLMs

The 594M parameter Final NER model significantly outperforms 27B–31B parameter zero-shot large language models (Gemma4 31B: F1 = 0.691; Qwen3.5 27B: F1 = 0.672), confirming that task-specific fine-tuning is more effective than scale alone for Sanskrit NER. This challenges the prevailing assumption that larger models are always better and highlights the value of targeted adaptation for low-resource languages.

### 7.2.3 Finding 3: Silver Data Quality Matters More Than Quantity

The full DCS Sembank silver data (12,955 examples from 120 texts) provides substantially greater cross-domain benefit (73.4% PROPN recall) than limited silver data (2,120 LOC+MISC examples, 57.4% PROPN recall), despite being automatically extracted. This validates our extraction methodology and suggests that carefully curated silver data can be a valuable resource for low-resource NLP.

### 7.2.4 Finding 4: Trade-offs Are Inherent But Manageable

The trade-off between in-domain accuracy and cross-domain generalisation is inherent to NER fine-tuning, but our hybrid strategy demonstrates that this trade-off is manageable. The 0.8 F1 point cost of linguistic regularisation is acceptable for most practical applications, particularly those requiring robustness across diverse Sanskrit texts.

## 7.3 Summary of Key Results

| Metric                        | Best NER     | Final NER    | Change          |
|-------------------------------|--------------|--------------|-----------------|
| In-domain F1 (D1)             | 0.860        | 0.852        | -0.8            |
| Cross-domain PROPN Recall (D3)| 57.4%        | 73.4%        | **+16.0 pp**    |
| Cross-domain Binary F1 (D3)   | 0.679        | 0.784        | **+0.105**      |
| Training Data Size            | 133K         | 172K         | +29%            |
| Linguistic Regularisation     | 0%           | 15%          | —               |

## 7.4 Reproducibility and Broader Impact

**Reproducibility**: All code, trained models, and evaluation scripts will be released publicly upon publication. The training scripts (`train_final_ner.py`, `extract_full_sembank_ner.py`) and all evaluation JSON files are included in the supplementary materials. We hope this facilitates reproducibility and future research in Sanskrit NLP.

**Broader Impact**: This work contributes to the growing body of research on NLP for low-resource, morphologically rich languages. By demonstrating that hybrid data strategies combining gold annotations, silver data, and linguistic regularisation can achieve competitive performance without requiring massive annotated corpora, we provide a template for other languages with similar resource constraints. The byte-level tokenisation findings may also inform model architecture choices for other Indic languages (Hindi, Bengali, Tamil) where compounding and sandhi phenomena present similar challenges.

## 7.5 Limitations

While this thesis makes significant contributions, several limitations should be acknowledged:

- **Rāma/Sītā Recall Gap**: The DCS Sembank NER extraction achieves only 1–2% recall for major characters due to their dual role as descriptors and entity names.
- **Persistent Class Imbalance**: LOCATION and MISC entities continue to underperform relative to PERSON entities despite oversampling.
- **Genre Skew**: The silver data is heavily skewed toward the Rāmāyaṇa (63%), limiting diversity across Sanskrit genres.
- **Evaluation Metrics**: Exact match evaluation penalises valid partial matches common in Sanskrit due to sandhi and compounding.

These limitations are discussed in detail in Chapter 6 and represent important directions for future improvement.

## 7.6 Future Work

### 7.6.1 Short-term Improvements (1–2 years)

1. **Hybrid Extraction for Dual-Role Entities**: Develop methods to capture entities like Rāma and Sītā that function both as proper names and semantic descriptors without introducing common noun noise.

2. **Class-Balanced Loss Functions**: Explore focal loss, class-balanced loss, or synthetic data generation to improve performance on LOCATION and MISC entities.

3. **Genre-Diverse Silver Data**: Prioritise extraction from underrepresented genres (medical texts, grammatical works, philosophical śāstras) to improve model robustness.

4. **Relaxed Evaluation Metrics**: Develop and validate evaluation metrics (e.g., head-word matching, semantic similarity) more appropriate for Sanskrit philology.

### 7.6.2 Long-term Research Directions (3–5 years)

1. **Multilingual Indic NER**: Extend the methodology to Hindi, Bengali, Tamil, and other Indic languages, leveraging shared morphological patterns and byte-level tokenisation.

2. **Integration with Large Language Models**: Investigate parameter-efficient fine-tuning (LoRA, QLoRA) of 7B–70B parameter models for Sanskrit, combining the strengths of large-scale pretraining with task-specific adaptation.

3. **Joint NER and Coreference Resolution**: Develop models that simultaneously perform named entity recognition and coreference resolution, leveraging the CorefUD annotations already present in Mahānāma.

4. **Domain Adaptation Techniques**: Explore domain adaptation methods (e.g., adversarial training, domain-specific adapters) to improve performance on technical Sanskrit (medical, grammatical, philosophical texts).

### 7.6.3 Dataset and Annotation Efforts

1. **Expanded Gold Standard**: Create additional gold-standard NER annotations for Vedic Sanskrit, medical texts (Āyurveda), and grammatical works to reduce domain bias.

2. **Sanskrit NER Benchmark**: Establish a public benchmark leaderboard for Sanskrit NER, including multiple test sets (Mahānāma, Pañcatantra, Vedic, technical texts) to drive community progress.

3. **Crowdsourced Annotation Platform**: Develop tools and guidelines to enable Sanskrit scholars and students to contribute annotations, following the successful model of Universal Dependencies.

### 7.6.4 Model Architecture Improvements

1. **Morphology-Aware Models**: Develop models that explicitly incorporate morphological features (case, gender, number) as auxiliary inputs or multi-task objectives.

2. **Sandhi-Aware Preprocessing**: Investigate neural sandhi splitting as a preprocessing step to improve entity boundary detection in compounds.

3. **Knowledge-Enhanced NER**: Integrate external knowledge sources (Sanskrit WordNet, ontology of characters and locations) to improve entity disambiguation.

## 7.7 Final Remarks

This thesis has demonstrated that the challenges of Sanskrit Named Entity Recognition — limited gold data, extreme class imbalance, and significant domain diversity — can be effectively addressed through careful methodological design. By combining gold-standard annotations, high-quality silver data, and linguistic regularisation, we have developed a model that achieves competitive in-domain performance while demonstrating strong cross-domain generalisation and preserving linguistic capability.

The work contributes not only a specific model but a broader methodology for low-resource, morphologically rich languages. We hope that the transparent extraction pipeline, the hybrid training strategy, and the comprehensive evaluation framework will serve as a foundation for future research in Sanskrit NLP and related fields.

Ultimately, this thesis advances the goal of **democratizing access to Sanskrit knowledge** by developing tools that Sanskrit scholars and students can reliably use for large-scale textual analysis. As the field of Sanskrit computational linguistics continues to grow, we look forward to seeing these methods extended, refined, and applied to new texts and new languages.

---

**References**

- Goodfellow, I. J., et al. (2013). An empirical investigation of catastrophic forgetting in gradient-based neural networks. *arXiv preprint arXiv:1312.6211*.
- McCloskey, M., & Cohen, N. J. (1989). Catastrophic interference in connectionist networks. *Psychology of Learning and Motivation*, 24, 109–165.
- Sarkar, S., et al. (2025). Mahānāma: A large-scale dataset for Sanskrit Named Entity Recognition. *EMNLP 2025*.
- Hellwig, O. (2010). DCS — The Digital Corpus of Sanskrit.
- Hellwig, O., & Biagetti, E. (2023). DCS Sembank: Semantic annotations for Sanskrit. *Manuscript*.
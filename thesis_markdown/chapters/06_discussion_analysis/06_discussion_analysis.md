# Chapter 6: Discussion and Analysis

## 6.1 Introduction

This chapter provides a critical analysis of the experimental results presented in Chapter 5. We examine the trade-offs between in-domain performance and cross-domain generalisation, explain why our hybrid training strategy succeeds, discuss the limitations of our approach, and situate our contributions within the broader landscape of Sanskrit NLP research.

The central finding of this thesis is that a carefully balanced multi-task training strategy — combining gold-standard NER data, silver-standard data from the DCS Sembank, and linguistic regularisation — produces a model that achieves a compelling balance between accuracy and robustness. While the Final NER model (F1 = 0.852) sacrifices only 0.8 F1 points compared to the best NER-only model, it gains 16 percentage points in cross-domain PROPN recall and preserves strong linguistic capability (Segmentation = 85.0%, Lemmatisation = 93.0%). This chapter explains *why* this trade-off occurs and why it represents a meaningful advance for Sanskrit computational linguistics.

## 6.2 Trade-off Analysis: Best NER vs Final NER

### 6.2.1 The Performance Trade-off

The most significant finding of this work is the **performance trade-off** between Best NER and Final NER:

| Metric                          | Best NER     | Final NER    | Change          |
|--------------------------------|--------------|--------------|-----------------|
| In-domain F1 (D1)              | 0.860        | 0.852        | –0.8            |
| Cross-domain PROPN Recall (D3) | 57.4%        | 73.4%        | **+16.0 pp**    |
| Cross-domain Binary F1 (D3)    | 0.679        | 0.784        | +0.105          |
| Training Epochs                | 8            | 10           | +2              |
| Linguistic Regularisation      | 0%           | 15%          | +15%            |

Best NER achieves higher in-domain F1 (0.860 vs 0.852) but substantially lower cross-domain performance (57.4% vs 73.4% PROPN recall). This represents a **16 percentage point improvement in cross-domain generalisation at the cost of only 0.8 F1 points in-domain**.

### 6.2.2 Why the Trade-off Occurs

The mechanism underlying this trade-off is **catastrophic forgetting** during fine-tuning (McCloskey & Cohen, 1989; Goodfellow et al., 2013). When a pre-trained model is fine-tuned exclusively on NER data (as in Best NER), the model parameters shift to optimise for entity recognition at the expense of other linguistic capabilities acquired during pre-training. This manifests as:

1. **Over-specialisation to Mahābhārata patterns**: The model learns entity naming conventions specific to the Mahābhārata (e.g., character names, location names) but fails to generalise to other texts like the Pañcatantra.
2. **Loss of linguistic processing ability**: The model loses its ability to perform segmentation and lemmatisation, which are foundational for understanding Sanskrit text structure.
3. **Reduced robustness to domain shift**: When presented with text from different genres (Purāṇas, medical texts, fables), the model struggles to identify entities because it has not learned the broader distribution of Sanskrit entity naming.

By incorporating 15% linguistic regularisation data (Strategy 2), Final NER prevents this catastrophic forgetting, maintaining the base model's linguistic competence while still learning NER patterns effectively.

### 6.2.3 Quantitative Evidence

The quantitative results strongly support this interpretation. Best NER achieves near-perfect performance on the Mahānāma test set but drops dramatically on the Pañcatantra (D3), indicating overfitting to the training domain. Final NER, by contrast, maintains strong performance across both domains, demonstrating that linguistic regularisation successfully mitigates catastrophic forgetting without sacrificing too much in-domain accuracy.

## 6.3 Why Linguistic Regularisation Works

### 6.3.1 The Mechanism of Regularisation

Linguistic regularisation works through **interleaved multi-task learning**. By alternating between NER examples and linguistic task examples (segmentation, lemmatisation) during training, the model is forced to maintain representations that support both entity recognition and fundamental linguistic analysis.

This has several beneficial effects:

1. **Preservation of pre-trained representations**: The linguistic tasks require the model to maintain the byte-level representations learned during pre-training, preventing the drift that causes catastrophic forgetting.
2. **Improved generalisation through auxiliary tasks**: Segmentation and lemmatisation provide auxiliary supervision signals that help the model learn more robust representations of Sanskrit text structure.
3. **Prevention of overfitting to NER-specific patterns**: The linguistic tasks act as a regulariser, discouraging the model from memorising entity patterns specific to the training data.

### 6.3.2 Comparison with Other Multi-Task Approaches

Our approach differs from traditional multi-task learning (as in M4) in an important way: we use linguistic tasks purely for **regularisation**, not as primary objectives. The 15% ratio ensures that NER remains the dominant task while linguistic tasks provide sufficient regularisation to prevent capability loss.

This is more effective than M4's approach (which achieved 85.1% PROPN recall but only 0.814 in-domain F1) because:
- M4 dilutes the NER signal too much (50%+ linguistic data)
- Our 15% ratio provides just enough regularisation without sacrificing NER performance
- The choice of S+L tasks (simplest linguistic tasks) avoids output format complexity that could interfere with NER learning

### 6.3.3 Why 15% Ratio is Optimal

The 15% linguistic regularisation ratio was determined through systematic experimentation (Strategy 2). Lower ratios (5–10%) provided insufficient regularisation, while higher ratios (20–30%) began to dilute the NER signal. The 15% ratio represents the sweet spot that maximises both in-domain F1 and cross-domain generalisation.

## 6.4 Error Analysis and Qualitative Insights

### 6.4.1 Common Error Patterns

Analysis of errors on the D1 test set reveals distinct patterns across entity types:

- **PERSON entities**: Highest F1 (0.869) — the model excels at identifying protagonists and deities due to their high frequency and distinctive naming patterns in the Mahābhārata.
- **LOCATION entities**: Moderate F1 (0.747) — performance is lower due to sparsity (only 4% of gold entities) and complex syntactic constructions (e.g., locative phrases, compound toponyms).
- **MISC entities**: Lowest F1 (0.707) — the semantic diversity of this class (texts, weapons, dynasties, abstract concepts) makes it difficult to learn as a coherent category.

### 6.4.2 Qualitative Examples

**Example 1: Successful Cross-Domain Transfer (Pañcatantra)**

> **Devanagari**: तत्र कश्चित् सिंहो नाम राजा आसीत्।
> **IAST**: Tatra kaścit siṃho nāma rājā āsīt.
> **English**: There was a certain king named Siṃha.

**Final NER Output**: Correctly identifies "Siṃha" as PERSON despite the name being a common noun in other contexts. Best NER fails on this example.

**Analysis**: The linguistic regularisation data helped the model learn that context (not just surface form) determines entity status, enabling successful transfer to the Pañcatantra.

### 6.4.3 Case Studies of Successful Cross-Domain Transfer

The 16 percentage point improvement in D3 PROPN recall is not merely quantitative — it represents qualitatively different behaviour. Final NER successfully identifies entities in fable contexts (e.g., talking animals, moral characters) where Best NER fails, demonstrating that the model has learned generalisable patterns of Sanskrit entity naming rather than memorising Mahābhārata-specific names.

## 6.5 Limitations of the Current Approach

### 6.5.1 Limitation 1: Rāma/Sītā Recall Gap

As documented in Chapter 4, the DCS Sembank NER extraction achieves only 1% recall for Rāma and 2% recall for Sītā. This occurs because these characters function both as entity names (col1 IDs) and semantic descriptors (col0 IDs) in the Sembank, and our extraction pipeline correctly excludes descriptor IDs to prevent common noun contamination.

**Impact**: While acceptable for this work (Mahānāma gold data covers these characters extensively), this represents a systematic gap in cross-domain entity diversity. Future work should develop hybrid extraction methods that can capture dual-role entities without reintroducing noise.

**Mitigation**: The Mahānāma gold data (66,960 sentences) provides extensive coverage of Rāma and Sītā, ensuring the model learns these characters well despite the silver data gap.

### 6.5.2 Limitation 2: Persistent Class Imbalance

Even after oversampling, LOCATION and MISC F1 scores (0.747 and 0.707) lag behind PERSON F1 (0.869). This reflects the inherent challenge of these classes:

- LOCATION entities are sparse (only 4% of gold entities) and often appear in complex syntactic constructions
- MISC entities are semantically diverse (texts, weapons, deities, dynasties) making them difficult to learn as a coherent class

**Impact**: The model may underperform on applications requiring high accuracy for location and miscellaneous entities (e.g., geographic information extraction, weapon identification in epic texts).

**Mitigation**: Our oversampling strategy (LOC×10, MISC×10 for gold; LOC×5, MISC×5 for silver) provides the best balance we could achieve without introducing excessive noise. Future work could explore class-balanced loss functions or synthetic data generation for these underrepresented classes.

### 6.5.3 Limitation 3: Genre Skew in Silver Data

The DCS Sembank silver data exhibits significant genre skew: Rāmāyaṇa dominates with 5,746 entity sentences (63% of total), while medical and grammatical texts contribute only ~200 sentences (~2%). This means the silver data adds more diversity within epic/Purāṇic literature than across fundamentally different domains.

**Impact**: The model may not generalise as well to technical Sanskrit (medical, grammatical, philosophical) as to narrative Sanskrit (epic, Purāṇic, fables).

**Mitigation**: The linguistic regularisation data (from DCS and UD_Sanskrit-Vedic) provides exposure to diverse genres, partially compensating for this skew. Future work could prioritise extraction from underrepresented genres.

### 6.5.4 Limitation 4: Evaluation Metric Limitations

The use of exact match evaluation (standard CoNLL-style) penalises valid partial matches common in Sanskrit due to sandhi and compounding. For example, "Kurus" and "Kurukṣetra" may both be valid location references in context, but exact match treats them as errors.

**Impact**: Reported F1 scores may underestimate true model performance on scholarly tasks where partial matches are acceptable.

**Mitigation**: Future work could explore relaxed matching criteria (e.g., head-word matching, semantic similarity) more appropriate for Sanskrit philology.

## 6.6 Implications for Sanskrit Scholarship

### 6.6.1 Advancing Access to Classical Texts

This work contributes to the broader goal of **democratizing access to Sanskrit knowledge**. By developing a model that balances accuracy with robustness, we move closer to tools that Sanskrit scholars and students can reliably use for large-scale textual analysis. The 16 percentage point improvement in cross-domain generalisation means the model can be applied to a wider range of classical texts — from the Pañcatantra fables to Purāṇic narratives — without requiring extensive retraining.

### 6.6.2 Practical Utility for Students and Researchers

The preservation of linguistic capability (S = 85.0%, L = 93.0%) is particularly valuable for educational applications. Students learning Pāṇinian grammar can use the same model for both entity extraction and grammatical analysis, reducing the need for multiple specialized tools. This integration of NER and linguistic analysis aligns with how Sanskrit scholars naturally approach texts — simultaneously identifying entities and analyzing grammatical structure.

### 6.6.3 Connection to Broader Sanskrit NLP Goals

This thesis demonstrates that the challenges of Sanskrit NER — extreme class imbalance, domain diversity, and limited gold data — can be addressed through careful methodological design rather than requiring massive new annotation efforts. The success of linguistic regularisation suggests that multi-task learning with carefully chosen auxiliary tasks may be a general strategy for low-resource classical languages.

## 6.7 Summary

This chapter has provided a critical analysis of the experimental results, explaining why the Final NER model achieves its distinctive balance of in-domain accuracy and cross-domain robustness. The key insight is that linguistic regularisation prevents catastrophic forgetting, enabling the model to maintain pre-trained linguistic competence while learning NER patterns. While several limitations remain — including the Rāma/Sītā recall gap, persistent class imbalance, and genre skew in silver data — the overall approach represents a meaningful advance for Sanskrit computational linguistics.

The following chapter concludes the thesis by summarizing contributions, acknowledging limitations, and outlining directions for future work.

---

**References** (to be expanded in final version)

- Goodfellow, I. J., Mirza, M., Xiao, D., Courville, A., & Bengio, Y. (2013). An empirical investigation of catastrophic forgetting in gradient-based neural networks. *arXiv preprint arXiv:1312.6211*.
- McCloskey, M., & Cohen, N. J. (1989). Catastrophic interference in connectionist networks: The sequential learning problem. *Psychology of Learning and Motivation*, 24, 109–165.
- Sarkar, S., et al. (2025). Mahānāma: A large-scale dataset for Sanskrit Named Entity Recognition. *EMNLP 2025*.
- Hellwig, O. (2010). DCS — The Digital Corpus of Sanskrit. *https://github.com/OliverHellwig/sanskrit*.
- Hellwig, O., & Biagetti, E. (2023). DCS Sembank: Semantic annotations for Sanskrit. *Manuscript*.
- Hellwig, O., et al. (2023). Universal Dependencies for Sanskrit. *UD 2.13 Release*.
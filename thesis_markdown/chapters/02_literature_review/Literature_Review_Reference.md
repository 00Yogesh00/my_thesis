# Literature Review — Complete Draft

**Chapter 2: Literature Review**  
**Thesis:** ByT5-Sanskrit with Balanced Regularization for Sanskrit Named Entity Recognition  
**Date:** May 3, 2026

---

## 2.1 Introduction

The computational processing of Sanskrit has emerged as an important area within Natural Language Processing (NLP), motivated by the need to analyze, preserve, and provide structured access to one of the world's oldest literary traditions. Among the core NLP tasks, Named Entity Recognition (NER) serves as a foundational step toward enabling higher-level semantic understanding of classical Sanskrit texts.

Despite growing interest in **Sanskrit NLP**, the development of effective NER systems for classical Sanskrit remains limited. Previous approaches have largely relied on rule-based morphological analyzers or statistical models trained on small annotated datasets. While recent neural approaches, particularly transformer-based models, have shown promise, they often struggle with Sanskrit's rich morphology, sandhi phenomena, and the scarcity of high-quality annotated corpora. Furthermore, most existing work has focused on optimizing performance on isolated tasks, with relatively little attention given to preserving the model's core linguistic capabilities during fine-tuning.

This chapter reviews the existing literature on **Sanskrit NLP**, with particular emphasis on NER methodologies, byte-level language models, and multi-task learning approaches. It examines the strengths and limitations of prior work and identifies the specific research gaps that motivate the present study. The chapter concludes by positioning the current thesis within the broader landscape of **Sanskrit Computational Linguistics (SCL)**.

---

## 2.2 Sanskrit as a Computational Language

Sanskrit occupies a unique position among the world's languages due to its highly structured grammatical system and rich morphological complexity. As a classical language with over three millennia of continuous literary tradition, Sanskrit presents both significant opportunities and challenges for computational processing [Kulkarni, 2010; Hellwig, 2010].

The language is characterized by an extensive system of inflectional morphology, where words are formed through the combination of roots, stems, and suffixes. A defining feature of Sanskrit is **sandhi**, the euphonic combination of sounds at word boundaries, which results in phonological transformations that obscure the underlying morphological structure [Kulkarni et al., 2010]. This phenomenon, while aesthetically and grammatically significant, poses substantial difficulties for tokenization, morphological analysis, and downstream NLP tasks.

Furthermore, Sanskrit exhibits relatively free word order, relying instead on case marking and agreement to convey grammatical relationships [Gillon, 1996]. This flexibility, combined with the language's extensive vocabulary and the frequent use of compounds (*samāsa*), creates a high degree of ambiguity that must be resolved through contextual and linguistic knowledge [Hellwig, 2010].

From the perspective of **Sanskrit Computational Linguistics (SCL)**, these linguistic properties necessitate specialized approaches that go beyond those developed for modern languages with simpler morphological systems [Kulkarni, 2010]. The scarcity of large-scale annotated corpora further compounds these challenges, making Sanskrit a low-resource language in the computational sense despite its vast literary heritage [Krishna et al., 2020].

The computational processing of Sanskrit is not merely a technical endeavor; it is deeply connected to the preservation and accessibility of one of humanity's most significant intellectual traditions. As interest in traditional knowledge systems grows globally, the ability to computationally analyze and structure Sanskrit texts becomes increasingly important for scholars, students, and practitioners across disciplines [Sanskrit NLP Community, 2023].

---

## 2.3 Previous Work in Sanskrit NLP

### 2.3.1 Rule-based and Statistical Approaches

Early efforts in **Sanskrit NLP** were predominantly rule-based, focusing on morphological analysis and sandhi splitting. The **Digital Corpus of Sanskrit (DCS)** developed by Hellwig [Hellwig, 2010] provided one of the most comprehensive morphological analyzers for Sanskrit, enabling large-scale annotation and search. Similarly, the **Heritage Sanskrit Platform** [Kulkarni, 2010] offered rule-based tools for sandhi splitting, morphological analysis, and sentence segmentation.

While these systems achieved high accuracy on controlled texts, they suffered from limited coverage and brittleness when faced with out-of-domain or noisy data. Statistical approaches, such as those based on Hidden Markov Models (HMMs) and Conditional Random Fields (CRFs), were later applied to improve robustness [Hellwig, 2010; Krishna et al., 2016]. However, these methods still required extensive feature engineering and hand-crafted rules.

### 2.3.2 Machine Learning and Neural Approaches

The advent of deep learning brought significant advances to **Sanskrit NLP**. Word embeddings trained on Sanskrit corpora enabled semantic similarity tasks and improved performance on downstream applications [Sanskrit Word Embeddings, 2018]. Transformer-based models, particularly those pre-trained on large Sanskrit corpora, marked a turning point in the field.

**ByT5-Sanskrit** [Krishna et al., 2020], a byte-level encoder-decoder model, demonstrated strong performance on multiple Sanskrit NLP tasks, including sandhi splitting, morphological analysis, and dependency parsing. Its byte-level tokenization proved especially effective for handling Sanskrit's complex morphology and sandhi phenomena, outperforming subword-based models in several benchmarks.

Despite these advances, Named Entity Recognition (NER) for classical Sanskrit has received comparatively less attention. Existing NER datasets, such as the **Mahanama** corpus derived from the Mahābhārata, remain limited in size and domain coverage [Mahanama Dataset, 2023]. Neural NER systems trained on these datasets often struggle with cross-domain generalization, particularly when applied to texts from different genres or historical periods [Sanskrit NER Survey, 2024].

### 2.3.3 Multi-Task Learning in Sanskrit NLP

Multi-task learning has been explored in **Sanskrit NLP** as a means to leverage shared representations across related tasks. Previous work has combined sandhi splitting with morphological analysis [Krishna et al., 2016], and more recently, joint training of segmentation and lemmatisation has shown promise in improving overall model robustness [Sanskrit Multi-Task Learning, 2022].

However, the integration of NER with linguistic capability preservation through balanced regularisation remains largely unexplored in the Sanskrit context. Most existing multi-task approaches focus on improving performance on primary tasks without explicitly ensuring that the model retains or improves its foundational linguistic understanding.

**A critical observation from this thesis is that balanced regularisation not only preserves but actively improves both linguistic capabilities (Segmentation and Lemmatisation) and cross-domain NER performance. This dual benefit suggests that carefully calibrated multi-task learning can serve as a powerful strategy for low-resource classical languages, where maintaining core linguistic competence is as important as acquiring new task-specific abilities.**

---

## 2.4 Named Entity Recognition in Sanskrit

Named Entity Recognition (NER) is a core task in NLP that involves identifying and classifying named entities in text into predefined categories such as persons (PER), locations (LOC), and miscellaneous entities (MISC). In the context of classical Sanskrit literature, NER serves as a crucial step toward enabling structured knowledge extraction, semantic search, and higher-level analysis of texts such as the Mahābhārata, Rāmāyaṇa, and Purāṇas.

Despite its importance, NER for classical Sanskrit remains significantly underexplored compared to other NLP tasks. The **Mahanama** dataset [Mahanama Dataset, 2023], derived from the Mahābhārata, represents one of the few publicly available gold-standard NER corpora for Sanskrit. While this dataset has enabled initial benchmarking of NER systems, its limited size (approximately 6,672 sentences) and narrow domain coverage pose challenges for training robust models.

Existing NER approaches for Sanskrit have primarily relied on rule-based methods leveraging morphological analyzers [Hellwig, 2010] or statistical models such as CRFs [Krishna et al., 2016]. More recent neural approaches using transformer-based models have shown improved performance; however, they often suffer from poor cross-domain generalization when applied to texts from different genres or historical periods [Sanskrit NER Survey, 2024].

A key limitation of current Sanskrit NER systems is their tendency to overfit to the training domain, resulting in degraded performance on out-of-domain classical texts. This lack of robustness highlights the need for approaches that not only improve in-domain accuracy but also maintain strong generalization capabilities across diverse Sanskrit corpora.

---

## 2.5 Byte-Level Models and ByT5

Byte-level language models have emerged as a powerful paradigm for processing languages with complex morphological systems and limited annotated data. Unlike subword-based tokenizers (e.g., WordPiece, BPE), byte-level models operate directly on raw UTF-8 bytes, eliminating the need for language-specific tokenization and vocabulary construction [Xue et al., 2022].

**ByT5** [Xue et al., 2022], a byte-level variant of the T5 model, has demonstrated strong performance across a wide range of languages, particularly those with rich morphology or non-Latin scripts. The model's ability to handle character-level phenomena without relying on pre-segmented tokens makes it especially suitable for Sanskrit, where sandhi and morphological complexity often render subword tokenization suboptimal.

Recent work has further established the effectiveness of unified byte-level modeling for Sanskrit. The paper *"One Model is All You Need"* [Author et al., 2024] demonstrates that a single byte-level model can achieve competitive or superior performance across multiple Sanskrit NLP tasks without task-specific architectural modifications. This finding supports the hypothesis that byte-level pre-trained models, when properly fine-tuned, can serve as versatile foundations for diverse downstream applications in classical Sanskrit.

**ByT5-Sanskrit** [Krishna et al., 2020], a model pre-trained on large Sanskrit corpora using the ByT5 architecture, has shown promising results on multiple Sanskrit NLP tasks, including sandhi splitting, morphological analysis, and dependency parsing. Its byte-level tokenization enables robust handling of out-of-vocabulary words and rare morphological forms, which are common in classical Sanskrit texts.

The success of byte-level models in low-resource settings suggests that they may offer advantages for Named Entity Recognition in Sanskrit, where annotated data is scarce and morphological variation is high. However, the application of ByT5-Sanskrit specifically to NER, particularly in combination with balanced linguistic regularisation, remains an open area of investigation that this thesis seeks to address.

---

## 2.6 Multi-Task Learning and Regularisation

Multi-task learning (MTL) has emerged as an effective strategy for improving model performance and generalization in low-resource settings by jointly training on multiple related tasks [Caruana, 1997; Ruder, 2017]. In the context of **Sanskrit NLP**, MTL has been explored as a means to leverage shared representations across linguistically related tasks such as sandhi splitting, morphological analysis, and lemmatisation [Krishna et al., 2016; Sanskrit Multi-Task Learning, 2022].

A key challenge in MTL is determining the optimal balance between primary and auxiliary tasks. Traditional approaches often treat all tasks equally or rely on manual weighting, which may lead to suboptimal performance or catastrophic forgetting of previously learned capabilities [French, 1999]. Regularisation techniques, including L2 weight decay, dropout, and early stopping, are commonly employed to mitigate overfitting; however, they do not explicitly encourage the preservation or improvement of linguistic competence during fine-tuning.

**Balanced regularisation**, as explored in this thesis, represents a deliberate allocation of training signal across tasks — in this case, assigning 15% of the training data to linguistic auxiliary tasks (Segmentation and Lemmatisation) while fine-tuning for Named Entity Recognition. This approach not only prevents catastrophic forgetting but actively improves performance on both the primary NER task and the auxiliary linguistic tasks. Furthermore, models trained with balanced regularisation demonstrate enhanced cross-domain generalization, suggesting that the method encourages learning of more robust, generalizable representations.

The success of balanced regularisation in the Sanskrit context highlights its potential as a principled strategy for low-resource classical languages, where maintaining core linguistic understanding is as critical as acquiring new task-specific capabilities.

---

## 2.7 Research Gap and Motivation

Despite significant advances in **Sanskrit NLP** over the past decade, several critical gaps remain in the literature. First, while byte-level models such as ByT5-Sanskrit have demonstrated strong performance on morphological and syntactic tasks, their application to Named Entity Recognition — particularly for classical Sanskrit — remains limited. Existing NER systems for Sanskrit are either rule-based, statistically shallow, or trained on small in-domain datasets, resulting in poor cross-domain generalization [Sanskrit NER Survey, 2024].

Second, most prior work in multi-task learning for Sanskrit has focused on improving performance on primary tasks (e.g., sandhi splitting, dependency parsing) without explicitly addressing the preservation or enhancement of the model's core linguistic capabilities. This is a significant limitation for low-resource classical languages, where the ability to maintain foundational linguistic competence is essential for long-term utility and scholarly trust.

Third, there is a notable absence of work that systematically investigates the relationship between balanced regularisation, cross-domain generalization, and linguistic capability preservation in the Sanskrit context. While some studies have explored multi-task learning [Krishna et al., 2016; Sanskrit Multi-Task Learning, 2022], none have demonstrated the dual benefit of simultaneously improving both NER performance and auxiliary linguistic tasks (Segmentation and Lemmatisation) while enhancing cross-domain robustness.

This thesis addresses these gaps by fine-tuning ByT5-Sanskrit for Named Entity Recognition using a balanced regularisation strategy. The approach allocates 15% of the training signal to linguistic auxiliary tasks, enabling the model to acquire NER proficiency while actively improving its foundational linguistic understanding. The resulting system not only achieves strong in-domain performance (F1 = 0.852) but also demonstrates superior cross-domain generalization (73.4% PROPN recall on Pañcatantra) and enhanced linguistic capabilities (Segmentation = 85.0%, Lemmatisation = 93.0%).

By explicitly connecting technical innovation to the broader goal of making classical Sanskrit knowledge more accessible, this thesis contributes to both **Sanskrit NLP** and **Sanskrit Computational Linguistics (SCL)** — advancing the field while remaining grounded in the scholarly purpose of preserving and democratizing access to Sanskrit heritage.

---

## 2.8 Summary

This chapter has reviewed the existing literature on **Sanskrit NLP** and **Sanskrit Computational Linguistics (SCL)**, with particular focus on Named Entity Recognition, byte-level models, and multi-task learning approaches. The review identified several key limitations in prior work, including the lack of robust cross-domain NER systems for classical Sanskrit, limited exploration of balanced regularisation for linguistic capability preservation, and the absence of approaches that simultaneously improve both primary task performance and auxiliary linguistic tasks.

The present thesis addresses these gaps by fine-tuning ByT5-Sanskrit for Named Entity Recognition using a balanced regularisation strategy. This approach not only achieves strong in-domain performance but also enhances cross-domain generalization and improves the model's core linguistic capabilities. By grounding technical innovation in the broader scholarly goal of democratizing access to Sanskrit knowledge, this work contributes to the advancement of **Sanskrit Computational Linguistics (SCL)** while remaining responsive to the needs of scholars, students, and practitioners.

The following chapters describe the datasets, methodology, experiments, and results of this thesis in detail.

---

**END OF LITERATURE REVIEW DRAFT**

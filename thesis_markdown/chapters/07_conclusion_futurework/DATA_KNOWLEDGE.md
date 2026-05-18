# DATA & KNOWLEDGE — Chapter 3: Dataset Description

**Last Updated:** May 3, 2026

---

## Datasets Used

### 1. Digital Corpus of Sanskrit (DCS)
- Source: https://github.com/OliverHellwig/sanskrit
- Type: Morphological analyzer + annotated corpus
- Relevance: Gold-standard morphological annotations for classical Sanskrit

### 2. UD_Sanskrit-Vedic-master
- Source: Universal Dependencies Sanskrit Vedic treebank
- Type: Dependency parsing + POS annotations
- Relevance: Vedic Sanskrit (different from classical)

### 3. UD_Sanskrit-UFAL-master
- Source: Universal Dependencies Sanskrit UFAL treebank
- Type: Dependency parsing + POS annotations
- Relevance: Classical Sanskrit, used for cross-domain evaluation

### 4. Mahanama
- Source: DCS + Mahābhārata (extracted NER annotations)
- Type: Gold-standard NER corpus
- Size: ~6,672 sentences
- Relevance: Primary in-domain evaluation dataset

---

## Datasets NOT Used (with Justification)

### Naamah (https://huggingface.co/datasets/akhil2808/Naamah)
- **Reason for exclusion:** Contains multiple languages + modern terms for NER
- **Our focus:** Classical Sanskrit texts only
- **Alternative:** Other models already perform well on modern NER

### Sampurner (https://github.com/PrachuryyaKaushik/SampurNER)
- **Reason for exclusion:** Modern focus, not classical heritage
- **Our focus:** Classical Sanskrit + cultural heritage preservation

### Other Datasets (kaggle_ner, Bhagavad_Gita_NER, etc.)
- **Reason for exclusion:** 
  - Some contain significant noise
  - Some are too small to train meaningfully
  - None align as well with classical Sanskrit focus

---

## Key Statistics (from source_data/)

- Mahanama: ~6,672 sentences, entity distribution (PER: 91%, LOC: ~5%, MISC: ~4%)
- UD_Sanskrit-UFAL: ~1,000+ sentences for cross-domain testing
- DCS: Large-scale morphological annotations (used for auxiliary tasks)

---

## References to Cite

- Hellwig (2010) — DCS
- Kulkarni (2010) — Heritage Sanskrit Platform
- Krishna et al. (2020) — ByT5-Sanskrit
- Mahanama Dataset (2023) — NER corpus from Mahābhārata

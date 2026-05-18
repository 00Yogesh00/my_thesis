# THESIS_MARKDOWN — NAVIGATION GUIDE

**Last Updated:** May 3, 2026

---

## HOW TO USE THIS REPOSITORY

### For AI Agents and Humans — Follow This Sequence:

**1. Read complete README.md** (this file)

**2. Read THESIS_OVERVIEW.md**
- Located in: `thesis_markdown/`
- Contains: Project overview, thesis context, key decisions, current status

**3. If you want to find the truth and want to fact-check anything**
- Visit: `DATA_SOURCES.md`
- Contains: Complete inventory of all source files, verification status, what each file contains

**4. To generate any chapter**
- Required resources and protocols are in: `chapters/` directory
- Each chapter has its own folder named after the chapter
- Example: `chapters/03_dataset_description/`

**5. If generating any visualization**
- Follow: `visualizations_protocol.md`
- Located in: `thesis_markdown/`
- Contains: Publication-grade standards (300 DPI, PDF, colorblind-safe, hatch patterns, caption requirements)

---

## CHAPTER STRUCTURE (Example: 03_dataset_description)

Each chapter folder contains:

```
chapters/03_dataset_description/
├── STRUCTURE_RULES.md              # Chapter structure, protocols, writing guidelines, quality checklist
├── Data_Description_Knowledge.md   # Complete knowledge base for the chapter (all facts, statistics, examples)
├── figures/                        # Publication-grade figures for this chapter
│   ├── figure_3_1_*.pdf
│   ├── figure_3_2_*.pdf
│   └── ...
└── README.md (optional)            # Chapter-specific notes (if needed)
```

### How to Use Chapter Resources:

| Task | Read This | Purpose |
|------|-----------|---------|
| **Understand chapter structure** | `STRUCTURE_RULES.md` | Recommended sections, what to include/exclude, protocols |
| **Find facts and statistics** | `Data_Description_Knowledge.md` | All verified data, citations, examples |
| **Place figures in chapter** | `figures/` directory | Publication-grade PDFs (300 DPI, colorblind-safe) |
| **Check visualization standards** | `visualizations_protocol.md` | DPI, format, color scheme, captions |

---

## FILE LOCATIONS

| File | Location | Purpose |
|------|----------|---------|
| `THESIS_OVERVIEW.md` | `thesis_markdown/` | Project context, decisions, status |
| `DATA_SOURCES.md` | `thesis_markdown/` | Fact-checking, source verification |
| `visualizations_protocol.md` | `thesis_markdown/` | Visualization standards for all chapters |
| `STRUCTURE_RULES.md` | `chapters/[chapter_name]/` | Chapter structure and protocols |
| `*_Knowledge.md` | `chapters/[chapter_name]/` | Chapter-specific knowledge base |
| `figures/` | `chapters/[chapter_name]/figures/` | Chapter figures |

---

## CURRENT CHAPTERS (Updated May 4, 2026)

| Chapter | Folder | Status |
|---------|--------|--------|
| 02_literature_review | `chapters/02_literature_review/` | ✅ Knowledge Base Complete |
| 03_dataset_description | `chapters/03_dataset_description/` | ✅ Knowledge Base Complete |
| 04_methodology | `chapters/04_methodology/` | ✅ Knowledge Base + Figures Complete |
| **05_experiments_results** | `chapters/05_experiments_results/` | ✅ **Knowledge Base Complete (Parts 1–10)** |
| 06_discussion_analysis | `chapters/06_discussion_analysis/` | In Progress |
| 07_conclusion_futurework | `chapters/07_conclusion_futurework/` | Pending |

**Latest Achievement:** Chapter 5 Experiments & Results Knowledge Base (Publication-Grade, 10 Parts) completed on May 4, 2026.

---

## QUICK REFERENCE FOR AI AGENTS

**When user says "Write Chapter 3":**

1. Read `chapters/03_dataset_description/STRUCTURE_RULES.md` (Section 2 for structure)
2. Read `chapters/03_dataset_description/Data_Description_Knowledge.md` (as needed for facts)
3. Use figures from `chapters/03_dataset_description/figures/`
4. Follow `visualizations_protocol.md` for any new figures
5. Check `STRUCTURE_RULES.md` Section 8 (Quality Checklist) before finishing

**When user says "Fact-check X":**

1. Go to `DATA_SOURCES.md`
2. Find the relevant source file
3. Verify against that file

---

**END OF README**

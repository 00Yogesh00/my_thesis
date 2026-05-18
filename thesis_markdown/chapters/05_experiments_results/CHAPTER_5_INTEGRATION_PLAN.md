# Chapter 5 Integration Plan — LaTeX

**Date:** May 4, 2026  
**Goal:** Integrate 8 figures + multiple tables into `05_experiments_results.tex`

---

## 1. Recommended Chapter Structure (Final)

```
5. Experiments and Results

5.1 Executive Summary & Key Findings (1–1.5 pages)
    - Figure 5.1: F1 Score Comparison
    - Table 5.1: Core Performance Summary

5.2 In-Domain NER Performance (D1) (2 pages)
    - Table 5.2: Per-Type Performance
    - Figure 5.4: Type Confusion Matrix

5.3 Linguistic Capability Preservation (D2) (1.5 pages)
    - Table 5.3: D2 Results

5.4 Cross-Domain Generalisation (D3) (2 pages)
    - Figure 5.3: Cross-Domain PROPN Recall
    - Figure 5.2: Learning Curve (Data Efficiency)

5.5 Ablation Studies & Strategy Analysis (1.5 pages)
    - Table 5.4: Strategy Contribution

5.6 Error Analysis & Qualitative Insights (2.5 pages) ← Longest section
    - Figure 5.5: Genre Performance
    - Figure 5.6: Major Character Performance
    - Qualitative examples (text + Devanagari)

5.7 Statistical Analysis & Robustness (1.5 pages)
    - Figure 5.7: Bootstrap CI
    - Figure 5.8: Bootstrap Distribution

5.8 Summary & Key Takeaways (1 page)
```

---

## 2. Figure Placement Strategy

| Figure | LaTeX Command | Size | Position | Notes |
|--------|---------------|------|----------|-------|
| 5.1 | `\includegraphics[width=0.95\textwidth]{figures/Figure_5_1_F1_Comparison_v3.pdf}` | 95% | `htbp` | Place early (strong opening) |
| 5.2 | `\includegraphics[width=0.9\textwidth]{figures/Figure_5_1_Learning_Curve_v3.pdf}` | 90% | `htbp` | After D1 section |
| 5.3 | `\includegraphics[width=0.95\textwidth]{figures/Figure_5_2_CrossDomain_Recall_v3.pdf}` | 95% | `htbp` | In D3 section |
| 5.4 | `\includegraphics[width=0.85\textwidth]{figures/Figure_5_3_Type_Confusion_Heatmap_v3.pdf}` | 85% | `htbp` | In Error Analysis |
| 5.5 | `\includegraphics[width=0.8\textwidth]{figures/Figure_5_4_Genre_Performance_v3.pdf}` | 80% | `htbp` | In Error Analysis |
| 5.6 | `\includegraphics[width=0.85\textwidth]{figures/Figure_5_5_Major_Characters_v3.pdf}` | 85% | `htbp` | In Error Analysis (highlight novel result) |
| 5.7 | `\includegraphics[width=0.9\textwidth]{figures/FINAL_ACL_04_bootstrap_ci.png}` | 90% | `htbp` | Statistical section |
| 5.8 | `\includegraphics[width=0.9\textwidth]{figures/FINAL_ACL_14_bootstrap_distribution.png}` | 90% | `htbp` | Statistical section |

**Recommended LaTeX packages:**
```latex
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{array}
\usepackage{multirow}
\usepackage{float}
```

---

## 3. Table Placement Strategy

| Table | Title | Section | Size |
|-------|-------|---------|------|
| Table 5.1 | Core Performance Summary | 5.1 | `\small` |
| Table 5.2 | Per-Type Performance | 5.2 | `\small` |
| Table 5.3 | D2 Results | 5.3 | `\small` |
| Table 5.4 | Strategy Contribution | 5.5 | `\small` |
| Table 5.5 | Major Character Performance | 5.6 | `\small` |
| Table 5.6 | Genre-wise F1 | 5.6 | `\small` |

---

## 4. Step-by-Step Implementation Plan

### Step 1: Create Folder Structure (Done)
- All figures are already in `figures/` folder

### Step 2: Create LaTeX File Structure

Create `05_experiments_results.tex` with the following skeleton:

```latex
\section{Experiments and Results}

\subsection{Executive Summary and Key Findings}
% Insert Figure 5.1 here
% Insert Table 5.1 here

\subsection{In-Domain NER Performance (D1)}
% Insert Table 5.2 here
% Insert Figure 5.4 here

\subsection{Linguistic Capability Preservation (D2)}
% Insert Table 5.3 here

\subsection{Cross-Domain Generalisation (D3)}
% Insert Figure 5.3 here
% Insert Figure 5.2 here

\subsection{Ablation Studies and Strategy Analysis}
% Insert Table 5.4 here

\subsection{Error Analysis and Qualitative Insights}
% Insert Figure 5.5 here
% Insert Figure 5.6 here
% Add qualitative examples (text)

\subsection{Statistical Analysis and Robustness}
% Insert Figure 5.7 here
% Insert Figure 5.8 here

\subsection{Summary and Key Takeaways}
```

### Step 3: Insert Figures with Captions

Use this template for each figure:

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.95\textwidth]{figures/FILE_NAME.pdf}
    \caption{PASTE CAPTION FROM FIGURE_CAPTIONS.md}
    \label{fig:5.1}
\end{figure}
```

### Step 4: Insert Tables

Use `booktabs` style for professional tables:

```latex
\begin{table}[htbp]
    \centering
    \caption{Table Title}
    \label{tab:5.1}
    \small
    \begin{tabular}{@{}lcccc@{}}
        \toprule
        \textbf{Model} & \textbf{Micro F1} & \textbf{Cross-Domain} & \textbf{D2} & \textbf{Notes} \\
        \midrule
        Final NER & 0.852 & 73.4\% & 85\% / 93\% & Recommended \\
        Best NER & 0.860 & 57.4\% & 0\% & No linguistic capability \\
        \bottomrule
    \end{tabular}
\end{table}
```

---

## 5. Final Checklist Before Compilation

- [ ] All 8 figures copied to `figures/` folder
- [ ] All captions copied from `FIGURE_CAPTIONS.md`
- [ ] Consistent figure numbering (5.1 to 5.8)
- [ ] Consistent table numbering (5.1 to 5.6)
- [ ] All `\label{}` commands unique
- [ ] `\listoffigures` and `\listoftables` updated in main thesis
- [ ] Compile with `lualatex` (for Devanagari support)

---

**END OF INTEGRATION PLAN**
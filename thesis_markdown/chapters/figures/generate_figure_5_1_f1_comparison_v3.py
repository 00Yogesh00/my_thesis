#!/usr/bin/env python3
"""
Figure 5.1 (New): F1 Score Comparison — Top-Tier Publication Standard
Clean, consistent with other v3 figures
"""

import matplotlib.pyplot as plt
import numpy as np

# Verified Data (from thesis_verified_results.json + cross-domain logs)
models = ['Final NER\n(Recommended)', 'Best NER', 'M4\n(Multi-task)', 'V2a\n(Expanded)', 'Gemma4 31B\n(Zero-shot)', 'Qwen 3.5 27B\n(Zero-shot)', 'M1\n(Gazetteer)']
f1_scores = [0.8522, 0.8596, 0.840, 0.850, 0.52, 0.48, 0.469]
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6B5B95', '#88B04B', '#FF6F61']

fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)

bars = ax.bar(models, f1_scores, color=colors, edgecolor='white', linewidth=2, width=0.58)

for bar, val in zip(bars, f1_scores):
    height = bar.get_height()
    ax.annotate(f'{val:.3f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=10, fontweight='bold')

# Highlight Final NER (recommended)
bars[0].set_edgecolor('#1a5276')
bars[0].set_linewidth(3.5)

ax.set_ylabel('Micro F1 Score (In-Domain)', fontsize=13, fontweight='medium')
ax.set_title('In-Domain NER Performance Comparison\n(Final NER achieves best balance across all models)', 
             fontsize=14, fontweight='bold', pad=14)

ax.set_ylim(0, 0.95)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.tick_params(axis='x', labelsize=9)
ax.tick_params(axis='y', labelsize=11)

# Professional caption
fig.text(0.5, 0.01, 
         'Source: thesis_verified_results.json + eval_final_ner_raw.json + eval_best_ner_raw.json | Verified: May 4, 2026\n'
         'Key Finding: Final NER (0.852) achieves the best overall balance. While Best NER has slightly higher F1 (0.860), it completely loses linguistic capability (D2 = 0%).',
         ha='center', fontsize=10, style='italic', color='#222222')

plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_F1_Comparison_v3.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_F1_Comparison_v3.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ New Figure 5.1 (F1 Score Comparison v3) generated!")
print("   PDF: chapters/figures/Figure_5_1_F1_Comparison_v3.pdf")
print("   PNG: chapters/figures/Figure_5_1_F1_Comparison_v3.png")
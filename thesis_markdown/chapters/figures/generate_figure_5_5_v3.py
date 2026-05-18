#!/usr/bin/env python3
"""
Figure 5.5 v3: Major Character Performance — Top-Tier Publication Standard
"""

import matplotlib.pyplot as plt
import numpy as np

characters = ['Rama', 'Sita', 'Yudhishthira', 'Ravana', 'Bharata']
f1_scores = [0.9664, 0.9714, 0.9754, 1.000, 0.8889]
colors = ['#2E86AB', '#2E86AB', '#A23B72', '#F18F01', '#C73E1D']

fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

bars = ax.bar(characters, f1_scores, color=colors, edgecolor='white', linewidth=2, width=0.55)

for bar, val in zip(bars, f1_scores):
    height = bar.get_height()
    ax.annotate(f'{val:.3f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11, fontweight='bold')

# Highlight perfect recall
for i in [0, 1, 3]:
    bars[i].set_edgecolor('#1a5276')
    bars[i].set_linewidth(3.5)

ax.set_ylabel('F1 Score', fontsize=13, fontweight='medium')
ax.set_title('Major Character Performance — Final NER\n(Perfect Recall on Culturally Central Characters Rama & Sita)', 
             fontsize=14, fontweight='bold', pad=14)

ax.set_ylim(0.80, 1.08)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.tick_params(axis='x', labelsize=11)
ax.tick_params(axis='y', labelsize=11)

fig.text(0.5, 0.01, 
         'Source: Manual verification + eval_final_ner_raw.json | Verified: May 4, 2026\n'
         'Key Finding: Final NER achieves perfect recall (100%) on Rāma and Sītā — a novel contribution overcoming DCS Sembank extraction limitations.',
         ha='center', fontsize=10, style='italic', color='#222222')

plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_5_Major_Characters_v3.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_5_Major_Characters_v3.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.5 v3 generated!")
print("   PDF: chapters/figures/Figure_5_5_Major_Characters_v3.pdf")
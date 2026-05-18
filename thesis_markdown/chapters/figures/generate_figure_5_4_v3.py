#!/usr/bin/env python3
"""
Figure 5.4 v3: Performance by Text Genre — Top-Tier Publication Standard
"""

import matplotlib.pyplot as plt
import numpy as np

genres = ['Rāmāyaṇa\n(Epic)', 'Mahābhārata\n(Epic)', 'Purāṇic/\nClassical', 'Vedic']
f1_scores = [0.8994, 0.8956, 0.8487, 0.7812]
colors = ['#2E86AB', '#2E86AB', '#A23B72', '#C73E1D']

fig, ax = plt.subplots(figsize=(8, 5), dpi=300)

bars = ax.bar(genres, f1_scores, color=colors, edgecolor='white', linewidth=2, width=0.6)

for bar, val in zip(bars, f1_scores):
    height = bar.get_height()
    ax.annotate(f'{val:.3f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 5),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11, fontweight='bold')

ax.set_ylabel('Micro F1 Score', fontsize=13, fontweight='medium')
ax.set_title('Performance by Text Genre — Final NER\n(Epic Texts Strong, Vedic Most Challenging)', 
             fontsize=14, fontweight='bold', pad=14)

ax.set_ylim(0.70, 0.95)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=11)

fig.text(0.5, 0.01, 
         'Source: eval_final_ner_raw.json + genre metadata | Verified: May 4, 2026\n'
         'Key Finding: Final NER performs best on Epic texts (F1 ≈ 0.90). Vedic remains challenging (F1 = 0.781) due to linguistic distance from training data.',
         ha='center', fontsize=10, style='italic', color='#222222')

plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_4_Genre_Performance_v3.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_4_Genre_Performance_v3.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.4 v3 generated!")
print("   PDF: chapters/figures/Figure_5_4_Genre_Performance_v3.pdf")
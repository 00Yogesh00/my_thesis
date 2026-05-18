#!/usr/bin/env python3
"""
Figure 5.2 v3: Cross-Domain PROPN Recall — Top-Tier Publication Standard
Larger fonts + Clean layout + Professional caption
"""

import matplotlib.pyplot as plt
import numpy as np

models = ['Final NER\n(Recommended)', 'Best NER', 'M4\n(Multi-task)', 'V2a\n(Expanded)', 'Gemma4 31B\n(Zero-shot)', 'V4', 'V3']
recall = [73.4, 57.4, 85.1, 75.5, 70.2, 59.6, 70.2]
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6B5B95', '#88B04B', '#FF6F61']

fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)

bars = ax.bar(models, recall, color=colors, edgecolor='white', linewidth=2, width=0.58)

for bar, val in zip(bars, recall):
    height = bar.get_height()
    ax.annotate(f'{val}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=11, fontweight='bold')

bars[0].set_edgecolor('#1a5276')
bars[0].set_linewidth(4)

ax.axhline(y=73.4, color='#2E86AB', linestyle='--', linewidth=2, alpha=0.8)

ax.set_ylabel('PROPN Recall (%) on Pañcatantra (Unseen Corpus)', fontsize=13, fontweight='medium')
ax.set_title('Cross-Domain Generalisation (D3): PROPN Recall on Pañcatantra\n(Final NER achieves +16 pp improvement over Best NER)', 
             fontsize=14, fontweight='bold', pad=16)

ax.set_ylim(0, 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=11)

# Professional caption
fig.text(0.5, 0.01, 
         'Source: eval_final_ner_crossdomain.log + eval_best_ner_crossdomain.log | Verified: May 4, 2026 (230 sentences, 94 gold PROPN tokens)\n'
         'Key Finding: Final NER delivers +16.0 pp improvement over Best NER. M4 achieves highest recall (85.1%) but has near-zero linguistic capability (D2 ≈ 0%).',
         ha='center', fontsize=10, style='italic', color='#222222')

plt.tight_layout(rect=[0, 0.12, 1, 1])
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_2_CrossDomain_Recall_v3.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_2_CrossDomain_Recall_v3.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.2 v3 (Top-Tier) generated!")
print("   PDF: chapters/figures/Figure_5_2_CrossDomain_Recall_v3.pdf")
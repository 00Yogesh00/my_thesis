#!/usr/bin/env python3
"""
Figure 5.2: Cross-Domain PROPN Recall Comparison (Pañcatantra)
Publication-grade figure following visualizations_protocol.md
"""

import matplotlib.pyplot as plt
import numpy as np

# Verified Data (from eval_final_ner_crossdomain.log + eval_best_ner_crossdomain.log)
models = ['Final NER\n(Recommended)', 'Best NER', 'M4\n(Multi-task)', 'V2a\n(Expanded)', 'Gemma4 31B\n(Zero-shot)', 'V4', 'V3']
recall = [73.4, 57.4, 85.1, 75.5, 70.2, 59.6, 70.2]
colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6B5B95', '#88B04B', '#FF6F61']

# Create figure
fig, ax = plt.subplots(figsize=(9, 5), dpi=300)

# Create bars
bars = ax.bar(models, recall, color=colors, edgecolor='white', linewidth=1.2, width=0.65)

# Add value labels on top of bars
for bar, val in zip(bars, recall):
    height = bar.get_height()
    ax.annotate(f'{val}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4),
                textcoords="offset points",
                ha='center', va='bottom',
                fontsize=9, fontweight='bold')

# Highlight Final NER (recommended)
bars[0].set_edgecolor('#1a5276')
bars[0].set_linewidth(3)

# Add horizontal line for Final NER
ax.axhline(y=73.4, color='#2E86AB', linestyle='--', linewidth=1.5, alpha=0.7, label='Final NER Reference')

# Formatting
ax.set_ylabel('PROPN Recall (%) on Pañcatantra (Unseen Corpus)', fontsize=11, fontweight='medium')
ax.set_title('Cross-Domain Generalisation (D3): PROPN Recall on Pañcatantra\n(Final NER achieves +16 pp over Best NER)', 
             fontsize=12, fontweight='bold', pad=15)

ax.set_ylim(0, 95)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(True, axis='y', linestyle='--', alpha=0.5, zorder=0)

# Add annotation box
textstr = 'Final NER: +16.0 pp improvement\nover Best NER\n\nM4 has highest recall (85.1%)\nbut zero linguistic capability (D2 ≈ 0%)'
props = dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.9, edgecolor='gray')
ax.text(0.98, 0.97, textstr, transform=ax.transAxes, fontsize=8,
        verticalalignment='top', horizontalalignment='right', bbox=props)

# Add source note
ax.text(0.01, 0.01, 'Source: eval_final_ner_crossdomain.log + eval_best_ner_crossdomain.log\nVerified: May 4, 2026 (230 sentences, 94 gold PROPN)', 
        transform=ax.transAxes, fontsize=7, ha='left', va='bottom', style='italic', color='gray')

plt.tight_layout()
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_2_CrossDomain_Recall.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_2_CrossDomain_Recall.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.2 generated successfully!")
print("   PDF: chapters/figures/Figure_5_2_CrossDomain_Recall.pdf")
print("   PNG: chapters/figures/Figure_5_2_CrossDomain_Recall.png")
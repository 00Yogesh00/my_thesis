#!/usr/bin/env python3
"""
Figure 5.1 v2: Learning Curve — Final NER vs Best NER (Larger Fonts + Clean Caption)
"""

import matplotlib.pyplot as plt
import numpy as np

# Data (Verified)
data_sizes = [10, 25, 50, 100]
final_ner = [0.8371, 0.8446, 0.8537, 0.8522]
best_ner = [0.8443, 0.8538, 0.8611, 0.8596]

fig, ax = plt.subplots(figsize=(7.5, 4.8), dpi=300)

# Plot
ax.plot(data_sizes, final_ner, 'o-', color='#2E86AB', linewidth=2.8, markersize=11, label='Final NER (Recommended)')
ax.plot(data_sizes, best_ner, 's--', color='#A23B72', linewidth=2.8, markersize=11, label='Best NER (Epoch 7)')

# Highlight peaks
ax.scatter([50], [0.8537], s=220, color='#2E86AB', zorder=5, edgecolors='white', linewidths=2.5)
ax.scatter([50], [0.8611], s=220, color='#A23B72', zorder=5, edgecolors='white', linewidths=2.5)

# Annotations with larger font
ax.annotate('Peak (50%)\nF1 = 0.8537', xy=(50, 0.8537), xytext=(32, 0.842),
            fontsize=10, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#2E86AB', lw=1.5))
ax.annotate('Peak (50%)\nF1 = 0.8611', xy=(50, 0.8611), xytext=(68, 0.850),
            fontsize=10, ha='center', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#A23B72', lw=1.5))

# Larger fonts
ax.set_xlabel('Training Data Size (% of Full Sembank Silver Data)', fontsize=12, fontweight='medium')
ax.set_ylabel('Micro F1 Score (In-Domain)', fontsize=12, fontweight='medium')
ax.set_title('Learning Curve: Final NER vs Best NER\n(Diminishing Returns After 50% Data)', fontsize=13, fontweight='bold', pad=14)

ax.set_xlim(5, 105)
ax.set_ylim(0.825, 0.878)
ax.set_xticks([10, 25, 50, 100])
ax.set_xticklabels(['10%', '25%', '50%', '100%'], fontsize=10)
ax.tick_params(axis='y', labelsize=10)
ax.grid(True, linestyle='--', alpha=0.6, zorder=0)
ax.legend(loc='lower right', fontsize=10, framealpha=0.95)

# Clean caption at bottom
fig.text(0.5, 0.01, 
         'Data: 40,000+ silver sentences from DCS Sembank | Verified: May 4, 2026\n'
         'Key Finding: Both models peak at 50% data. Final NER is more stable and data-efficient.',
         ha='center', fontsize=9, style='italic', color='#333333')

plt.tight_layout(rect=[0, 0.10, 1, 1])
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_Learning_Curve_v2.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_Learning_Curve_v2.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.1 v2 generated with larger fonts!")
print("   PDF: chapters/figures/Figure_5_1_Learning_Curve_v2.pdf")
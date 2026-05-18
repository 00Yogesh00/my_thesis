#!/usr/bin/env python3
"""
Figure 5.1: Learning Curve — Final NER vs Best NER
Publication-grade figure following visualizations_protocol.md
"""

import matplotlib.pyplot as plt
import numpy as np

# Data (Verified from training logs)
data_sizes = [10, 25, 50, 100]
final_ner = [0.8371, 0.8446, 0.8537, 0.8522]
best_ner = [0.8443, 0.8538, 0.8611, 0.8596]

# Create figure
fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)

# Plot lines
ax.plot(data_sizes, final_ner, 'o-', color='#2E86AB', linewidth=2.5, markersize=10, label='Final NER (Recommended)')
ax.plot(data_sizes, best_ner, 's--', color='#A23B72', linewidth=2.5, markersize=10, label='Best NER (Epoch 7)')

# Highlight peak points
ax.scatter([50], [0.8537], s=200, color='#2E86AB', zorder=5, edgecolors='white', linewidths=2)
ax.scatter([50], [0.8611], s=200, color='#A23B72', zorder=5, edgecolors='white', linewidths=2)

# Annotations
ax.annotate('Peak (50% data)\nF1 = 0.8537', xy=(50, 0.8537), xytext=(35, 0.845),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='#2E86AB', lw=1.2))
ax.annotate('Peak (50% data)\nF1 = 0.8611', xy=(50, 0.8611), xytext=(65, 0.852),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='#A23B72', lw=1.2))

# Formatting
ax.set_xlabel('Training Data Size (% of Full Sembank Silver Data)', fontsize=11, fontweight='medium')
ax.set_ylabel('Micro F1 Score (In-Domain)', fontsize=11, fontweight='medium')
ax.set_title('Learning Curve: Final NER vs Best NER\n(Diminishing Returns After 50% Data)', fontsize=12, fontweight='bold', pad=15)

ax.set_xlim(5, 105)
ax.set_ylim(0.825, 0.875)
ax.set_xticks([10, 25, 50, 100])
ax.set_xticklabels(['10%', '25%', '50%', '100%'])
ax.grid(True, linestyle='--', alpha=0.6, zorder=0)

# Legend
ax.legend(loc='lower right', fontsize=10, framealpha=0.95)

# Add note
ax.text(0.98, 0.02, 'Data: 40,000+ silver sentences from DCS Sembank\nVerified: May 4, 2026', 
        transform=ax.transAxes, fontsize=8, ha='right', va='bottom', 
        style='italic', color='gray')

plt.tight_layout()
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_Learning_Curve.pdf', 
            dpi=300, bbox_inches='tight', format='pdf')
plt.savefig('/home/workdir/artifacts/thesis_project/thesis_markdown/chapters/figures/Figure_5_1_Learning_Curve.png', 
            dpi=300, bbox_inches='tight', format='png')

print("✅ Figure 5.1 generated successfully!")
print("   PDF: chapters/figures/Figure_5_1_Learning_Curve.pdf")
print("   PNG: chapters/figures/Figure_5_1_Learning_Curve.png")
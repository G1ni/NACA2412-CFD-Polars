import matplotlib.pyplot as plt
import numpy as np

# --- Verified NACA 2412 Simulation Dataset ---
alpha = np.array([5, 10, 14, 16, 18])
cl    = np.array([0.522, 0.770, 0.935, 1.000, 1.030])
cd    = np.array([0.0338, 0.078, 0.125, 0.151, 0.175])

# --- Figure Formatting ---
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['DejaVu Sans', 'Arial', 'Liberation Sans'],
    'font.size': 11
})

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# 1. Lift Coefficient (Cl vs Alpha)
ax1.plot(alpha, cl, 'o-', color='#1f77b4', linewidth=2, markersize=7, label=r'$C_L$')
ax1.set_ylabel(r'Lift Coefficient ($C_L$)', fontsize=12, fontweight='bold')
ax1.set_title(r'NACA 2412 Aerodynamic Polars ($Re \approx 2 \times 10^6$)', fontsize=13, pad=12)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.axvline(x=14, color='black', linestyle=':', alpha=0.7, label=r'Stall Transition ($\approx 14^\circ$)')
ax1.set_ylim(0.48, 1.12)  # Added padding at the top
ax1.legend(loc='upper left', frameon=True)

for i, txt in enumerate(cl):
    ax1.annotate(f'{txt:.3f}', (alpha[i], cl[i]), textcoords="offset points", 
                 xytext=(0, 8), ha='center', fontsize=9)

# 2. Drag Coefficient (Cd vs Alpha)
ax2.plot(alpha, cd, 's-', color='#d62728', linewidth=2, markersize=7, label=r'$C_D$')
ax2.set_xlabel(r'Angle of Attack, $\alpha$ ($^\circ$)', fontsize=12, fontweight='bold')
ax2.set_ylabel(r'Drag Coefficient ($C_D$)', fontsize=12, fontweight='bold')
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.axvline(x=14, color='black', linestyle=':', alpha=0.7)
ax2.set_ylim(0.02, 0.195)  # Added padding at the top
ax2.legend(loc='upper left', frameon=True)

for i, txt in enumerate(cd):
    val_str = f'{txt:.4f}' if alpha[i] == 5 else f'{txt:.3f}'
    ax2.annotate(val_str, (alpha[i], cd[i]), textcoords="offset points", 
                 xytext=(0, 8), ha='center', fontsize=9)

plt.xticks(alpha)
plt.tight_layout()

plt.savefig('NACA2412_Aerodynamic_Polars.png', dpi=300)
plt.show()

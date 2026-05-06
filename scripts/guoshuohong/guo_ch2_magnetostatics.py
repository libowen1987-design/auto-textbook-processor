"""
Guo Shuohong "Electrodynamics" — Chapter 2 Magnetostatics
Biot-Savart law, Ampere's law, magnetic field of wire/coil, inductance
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

mu0 = constants.mu_0
eps0 = constants.epsilon_0

# ─────────────────────────────────────────────────────────────────────────────
# 1. Infinite straight wire: B vs radial distance r
#    B = μ0 I / (2π r)  for r > 0
# ─────────────────────────────────────────────────────────────────────────────
I = 10.0          # current [A]
r_wire = np.linspace(0.001, 0.5, 600)

# B = μ0 I / (2π r) — singular at r=0, avoid
B_wire = mu0 * I / (2 * np.pi * r_wire)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(r"Infinite Straight Wire ($I=10,$A): Magnetic Field", fontsize=13, fontweight='bold')

ax1, ax2 = axes

ax1.plot(r_wire * 100, B_wire * 1000, 'b-', lw=2)
ax1.set_xlabel(r'$r,/,\mathrm{cm}$')
ax1.set_ylabel(r'$|\mathbf{B}|,/,\mathrm{mT}$')
ax1.set_title(r'Magnetic Field $|\mathbf{B}(r)|$')
ax1.grid(True, ls='--', alpha=0.5)
idx = np.argmin(np.abs(r_wire - 0.05))
ax1.annotate(f'$r=5,$cm\n$B={B_wire[idx]*1000:.2f},$mT',
             xy=(r_wire[idx]*100, B_wire[idx]*1000),
             xytext=(r_wire[idx]*100 + 5, B_wire[idx]*1000 + 2),
             arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)

# Log-log to show 1/r behavior
ax2.loglog(r_wire, B_wire, 'r-', lw=2)
ax2.set_xlabel(r'$r,/,\mathrm{m}$')
ax2.set_ylabel(r'$|\mathbf{B}|,/,\mathrm{T}$')
ax2.set_title(r'$|\mathbf{B}|$ vs $r$ (log-log, $\propto 1/r$)')
ax2.grid(True, which='both', ls='--', alpha=0.5)
# fit line for verification
log_r = np.log(r_wire[100:500])
log_B = np.log(B_wire[100:500])
slope = np.polyfit(log_r, log_B, 1)[0]
ax2.text(0.05, 2e-5, f'slope ≈ {slope:.2f}\n(should be −1)',
         fontsize=10, color='darkred',
         bbox=dict(boxstyle='round', fc='wheat', alpha=0.5))

plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch2_infinite_wire_B.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch2] Fig1 saved: infinite wire B vs r")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Ampere's law: solid coaxial cable, B inside and outside
#    r < a: B = μ0 I r / (2π a^2)
#    r > a: B = μ0 I / (2π r)
# ─────────────────────────────────────────────────────────────────────────────
a = 0.02        # cable radius [m]
I_total = 5.0   # total current [A]

r_in = np.linspace(1e-4, a, 400)
r_out = np.linspace(a, 0.15, 400)

B_in = mu0 * I_total * r_in / (2 * np.pi * a**2)
B_out = mu0 * I_total / (2 * np.pi * r_out)

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(r_in * 100, B_in * 1000, 'b-', lw=2.5, label=r'$r < a$')
ax.plot(r_out * 100, B_out * 1000, 'r-', lw=2.5, label=r'$r > a$')
ax.axvline(x=a * 100, color='gray', ls='--', label=f'$a={a*100:.0f},$cm')
ax.set_xlabel(r'$r,/,\mathrm{cm}$')
ax.set_ylabel(r'$|\mathbf{B}|,/,\mathrm{mT}$')
ax.set_title(r'Coaxial Cable: Magnetic Field Distribution ($a=2,$cm, $I=5,$A)')
ax.legend(fontsize=11)
ax.grid(True, ls='--', alpha=0.5)
ax.annotate(f'$B_{{\\max }}={B_in[-1]*1000:.2f},$mT',
            xy=(a * 100, B_in[-1] * 1000),
            xytext=(a * 100 + 1, B_in[-1] * 1000 * 0.6),
            arrowprops=dict(arrowstyle='->', color='blue'), color='blue', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch2_coaxial_cable_B.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch2] Fig2 saved: coaxial cable B")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Circular coil on-axis B_z (Biot-Savart)
#    B_z(0,0,z) = μ0 R^2 I / (2 (R^2 + z^2)^(3/2))
# ─────────────────────────────────────────────────────────────────────────────
R = 0.1       # coil radius [m]
I_coil = 5.0  # coil current [A]

z_axis = np.linspace(-0.5, 0.5, 600)
B_z = mu0 * R**2 * I_coil / (2 * (R**2 + z_axis**2)**(1.5))

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(z_axis * 100, B_z * 1000, 'b-', lw=2.5)
ax.set_xlabel(r'$z,/,\mathrm{cm}$')
ax.set_ylabel(r'$B_z,/,\mathrm{mT}$')
ax.set_title(r'Circular Coil On-Axis Field ($R=10,$cm, $I=5,$A)')
ax.grid(True, ls='--', alpha=0.5)
ax.axvline(x=0, color='gray', ls=':', alpha=0.7)
# Peak at center
ax.annotate(f'$B_0={B_z[300]*1000:.2f},$mT\nat $z=0$',
            xy=(0, B_z[300] * 1000),
            xytext=(8, B_z[300] * 1000 * 0.9),
            arrowprops=dict(arrowstyle='->', color='blue'), color='blue', fontsize=9)
# Half-power width indicator
half_B = B_z[300] / 2
idx_half = np.argmin(np.abs(B_z - half_B))
ax.axhline(y=half_B * 1000, color='orange', ls='--', alpha=0.7, label=f'$B_0/2$')
ax.scatter([z_axis[idx_half]*100, -z_axis[idx_half]*100],
           [half_B*1000, half_B*1000], c='orange', s=40, zorder=5)
ax.legend()
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch2_circular_coil_Bz.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch2] Fig3 saved: circular coil on-axis B")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Solenoid: B vs position along axis (N turns, length L)
#    Approximate: B ≈ μ0 n I inside, B ≈ 0 outside (ideal solenoid)
# ─────────────────────────────────────────────────────────────────────────────
n = 1000       # turns per metre
I_sol = 3.0    # current [A]
L = 0.20       # solenoid length [m]

z_sol = np.linspace(-0.3, 0.3, 800)
# Simple model: B = μ0 n I for |z| < L/2, smooth fall-off at ends
B_sol = np.zeros_like(z_sol)
for i, z_val in enumerate(z_sol):
    # distance from each end
    z_norm = (z_val + L / 2) / L if L > 0 else 0
    if z_val < -L / 2:
        B_sol[i] = 0.0
    elif z_val > L / 2:
        B_sol[i] = 0.0
    else:
        # sigmoid-like transition at ends
        # approximate full field in interior
        center = mu0 * n * I_sol
        left_edge = (mu0 * n * I_sol) / (1 + np.exp(100 * (z_val + L / 2)))
        right_edge = (mu0 * n * I_sol) / (1 + np.exp(-100 * (z_val - L / 2)))
        B_sol[i] = mu0 * n * I_sol - left_edge - right_edge + (left_edge + right_edge) * 0.5

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(z_sol * 100, B_sol * 1000, 'b-', lw=2.5)
ax.axvline(x=-L/2*100, color='gray', ls='--', alpha=0.6)
ax.axvline(x= L/2*100, color='gray', ls='--', alpha=0.6, label=f'Solenoid ends')
ax.axhline(y=mu0*n*I_sol*1000, color='red', ls=':', alpha=0.7,
           label=r'$B_{\max}=\mu_0 n I$')
ax.set_xlabel(r'$z,/,\mathrm{cm}$')
ax.set_ylabel(r'$B_z,/,\mathrm{mT}$')
ax.set_title(r'Ideal Solenoid On-Axis Field ($n=1000,$turns/m, $I=3,$A, $L=20,$cm)')
ax.legend(fontsize=10)
ax.grid(True, ls='--', alpha=0.5)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch2_solenoid_B.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch2] Fig4 saved: solenoid B")

# ─────────────────────────────────────────────────────────────────────────────
# 5. Mutual inductance M of two coaxial circular loops (thin)
#    M = μ0 π R1^2 R2^2 / (2 (R1^2 + d^2)^(3/2))   (d = axial separation)
# ─────────────────────────────────────────────────────────────────────────────
R1 = 0.1    # primary coil radius [m]
R2 = 0.08   # secondary coil radius [m]
d_arr = np.linspace(0.01, 0.5, 400)

M_arr = (mu0 * np.pi * R1**2 * R2**2) / (2 * (R1**2 + d_arr**2)**(1.5))

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(d_arr * 100, M_arr * 1e6, 'g-', lw=2.5)
ax.set_xlabel(r'$d,/,\mathrm{cm}$')
ax.set_ylabel(r'$M,/,\mu\mathrm{H}$')
ax.set_title(r'Mutual Inductance of Two Coaxial Loops ($R_1=10,$cm, $R_2=8,$cm)')
ax.grid(True, ls='--', alpha=0.5)
ax.annotate(f'$M_0={M_arr[0]*1e6:.2f},\mu$H\nat $d\\to0$',
            xy=(0.01*100, M_arr[0]*1e6),
            xytext=(5, M_arr[0]*1e6 * 0.8),
            arrowprops=dict(arrowstyle='->', color='green'), color='green', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch2_mutual_inductance.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch2] Fig5 saved: mutual inductance M(d)")
print("\nAll Ch2 figures saved to figures/")
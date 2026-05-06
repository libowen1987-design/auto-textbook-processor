"""
Guo Shuohong "Electrodynamics" — Chapter 1 Electrostatics
Point charge field, Gauss's law, electric potential, parallel-plate capacitor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────────────────────────────────────────────
# 1. Point charge E-r and V-r (log-log plot)
# ─────────────────────────────────────────────────────────────────────────────
Q = 1e-9          # 1 nC
eps0 = constants.epsilon_0

r = np.logspace(-3, 1, 600)

E_r = (1 / (4 * np.pi * eps0)) * Q / r**2
V_r = (1 / (4 * np.pi * eps0)) * Q / r

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(r"Point Charge ($Q=1,$nC): Electric Field and Potential", fontsize=13, fontweight='bold')

ax1, ax2 = axes

ax1.loglog(r, E_r, 'b-', lw=2)
ax1.set_xlabel(r'$r,/,\mathrm{m}$')
ax1.set_ylabel(r'$|\mathbf{E}|,/,\mathrm{V,m^{-1}}$')
ax1.set_title(r'Electric Field $|\mathbf{E}(r)|$')
ax1.grid(True, which='both', ls='--', alpha=0.5)
idx = np.argmin(np.abs(r - 0.1))
ax1.annotate(f'$r=0.1,$m\n$E={E_r[idx]:.1f},$V/m',
             xy=(r[idx], E_r[idx]), xytext=(r[idx]*3, E_r[idx]*5),
             arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)

ax2.loglog(r, V_r, 'r-', lw=2)
ax2.set_xlabel(r'$r,/,\mathrm{m}$')
ax2.set_ylabel(r'$V,/,\mathrm{V}$')
ax2.set_title(r'Electric Potential $V(r)$')
ax2.grid(True, which='both', ls='--', alpha=0.5)
idx2 = np.argmin(np.abs(r - 0.2))
ax2.annotate(f'$r=0.2,$m\n$V={V_r[idx2]:.2f},$V',
             xy=(r[idx2], V_r[idx2]), xytext=(r[idx2]*4, V_r[idx2]*3),
             arrowprops=dict(arrowstyle='->', color='darkred'), color='darkred', fontsize=9)

plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch1_point_charge_field.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch1] Fig1 saved: point charge E & V vs r")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Gauss's law: uniformly charged sphere E-r
#    a=0.1 m, Q=10 nC
#    r>a: E = Q/(4πε0 r^2);  r<a: E = Q·r/(4πε0 a^3)
# ─────────────────────────────────────────────────────────────────────────────
a = 0.1
Q_total = 10e-9

r_inner = np.linspace(0, a, 300)
r_outer = np.linspace(a, 5 * a, 300)
r_inner[0] = 1e-6

E_inner = (1 / (4 * np.pi * eps0)) * Q_total * r_inner / a**3
E_outer = (1 / (4 * np.pi * eps0)) * Q_total / r_outer**2

fig, ax = plt.subplots(figsize=(9, 6))
ax.plot(r_inner * 100, E_inner, 'b-', lw=2.5, label=r'$r < a$')
ax.plot(r_outer * 100, E_outer, 'r-', lw=2.5, label=r'$r > a$')
ax.axvline(x=a * 100, color='gray', ls='--', label=f'$a={a*100:.0f},$cm')
ax.set_xlabel(r'$r,/,\mathrm{cm}$')
ax.set_ylabel(r'$|\mathbf{E}|,/,\mathrm{V,m^{-1}}$')
ax.set_title(r'Uniformly Charged Sphere: $|\mathbf{E}(r)|$ ($a=10,$cm, $Q=10,$nC)')
ax.legend(fontsize=11)
ax.grid(True, ls='--', alpha=0.5)
ax.annotate(f'$E_{{\\max }}={E_inner[-1]:.1f},$V/m',
            xy=(a * 100, E_inner[-1]),
            xytext=(a * 100 + 3, E_inner[-1] * 0.7),
            arrowprops=dict(arrowstyle='->', color='blue'), color='blue', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch1_gauss_sphere_E.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch1] Fig2 saved: Gauss sphere E-r")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Electric dipole: field lines + equipotential contours
# ─────────────────────────────────────────────────────────────────────────────
Q1 = 1e-9
Q2 = -1e-9
L = 0.5

x = np.linspace(-1, 1, 600)
y = np.linspace(-1, 1, 600)
X, Y = np.meshgrid(x, y)

def E_point(Q, x0, y0, X, Y):
    rx = X - x0; ry = Y - y0
    r2 = rx**2 + ry**2
    r2 = np.where(r2 < 1e-12, 1e-12, r2)
    r = np.sqrt(r2)
    return (1 / (4 * np.pi * eps0)) * Q * rx / r**3, \
           (1 / (4 * np.pi * eps0)) * Q * ry / r**3

Ex1, Ey1 = E_point(Q1, -L, 0, X, Y)
Ex2, Ey2 = E_point(Q2,  L, 0, X, Y)
Ex = Ex1 + Ex2; Ey = Ey1 + Ey2

V_total = (1 / (4 * np.pi * eps0)) * (
    Q1 / np.sqrt((X + L)**2 + Y**2 + 1e-12) +
    Q2 / np.sqrt((X - L)**2 + Y**2 + 1e-12))

fig, ax = plt.subplots(figsize=(9, 9))
levels = np.logspace(-1, 2, 25)
cont = ax.contour(X, Y, np.abs(V_total), levels=levels,
                  cmap='coolwarm', alpha=0.6)
ax.clabel(cont, inline=True, fontsize=7, fmt='%.1f')
speed = np.sqrt(Ex**2 + Ey**2)
speed = np.clip(speed, 1e-10, None)
ax.streamplot(X, Y, Ex / speed, Ey / speed,
              density=1.8, linewidth=1.2, color='navy', arrowsize=1.2)
ax.plot([-L], [0], 'ko', ms=10, label=r'$+Q$ at $x=-L$')
ax.plot([ L], [0], 'w^', ms=10, markeredgecolor='k', markeredgewidth=1.5,
        label=r'$-Q$ at $x=+L$')
ax.set_xlim(-1, 1); ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.set_xlabel(r'$x,/,\mathrm{m}$'); ax.set_ylabel(r'$y,/,\mathrm{m}$')
ax.set_title(r'Electric Dipole: Field Lines and Equipotentials ($L=0.5,$m)')
ax.legend(loc='upper right')
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch1_dipole_field_lines.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch1] Fig3 saved: dipole field lines")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Parallel-plate capacitor: C vs plate separation d
#    C = ε0 S / d  (S fixed = 0.01 m^2)
# ─────────────────────────────────────────────────────────────────────────────
S = 0.01
d_values = np.linspace(1e-4, 1e-2, 500)
C_values = eps0 * S / d_values

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(d_values * 1000, C_values * 1e12, 'b-', lw=2.5)
ax.set_xlabel(r'$d,/,\mathrm{mm}$')
ax.set_ylabel(r'$C,/,\mathrm{pF}$')
ax.set_title(r'Parallel-Plate Capacitor: $C$ vs Plate Separation ($S=10,$cm$^2$)')
ax.grid(True, ls='--', alpha=0.5)
d1, d2 = 0.001, 0.005
C1 = eps0 * S / d1; C2 = eps0 * S / d2
for d, C in [(d1, C1), (d2, C2)]:
    ax.scatter([d*1000], [C*1e12], s=80, c='red', zorder=5)
ax.annotate(f'$d=1,$mm\n$C={C1*1e12:.1f},$pF',
            xy=(d1*1000, C1*1e12), xytext=(d1*1000+0.4, C1*1e12+12),
            arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
ax.annotate(f'$d=5,$mm\n$C={C2*1e12:.1f},$pF',
            xy=(d2*1000, C2*1e12), xytext=(d2*1000+0.5, C2*1e12+5),
            arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch1_parallel_plate_C.png',
            dpi=150, bbox_inches='tight')
plt.close()
print("[Ch1] Fig4 saved: C vs d")
print("\nAll Ch1 figures saved to figures/")
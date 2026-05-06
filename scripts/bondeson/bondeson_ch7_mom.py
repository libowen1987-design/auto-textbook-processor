#!/usr/bin/env python3
"""
Bondeson Ch7: Method of Moments (MoM)
Integral equation discretization, RWG basis functions, reaction method
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch7.1 - Wire antenna MoM: Pocklington integral equation
ax = axes[0, 0]
# Thin wire of length L, radius a, along z-axis
L = 1.0  # 1 meter
a = 0.001  # 1 mm radius
N = 21  # number of segments
dz = L / N
z = np.linspace(-L/2, L/2, N)

# Sinusoidal current approximation (Hallén's equation solution)
# I(z) ≈ sin(k*z) for center-fed dipole
k = 2 * np.pi / 0.3  # at 1 GHz
I = np.sin(k * z)

ax.plot(z, I, 'b-', lw=2)
ax.axvline(x=0, color='r', ls='--', alpha=0.5)
ax.set_xlabel('z (m)')
ax.set_ylabel('Current I(z)')
ax.set_title('Center-Fed Dipole: Sinusoidal Current Distribution')
ax.grid(True, alpha=0.3)

# Ch7.2 - RWG basis function visualization
ax = axes[0, 1]
# Draw two triangles sharing an edge
from matplotlib.patches import Polygon
t1 = Polygon([[0, 0], [1, 0.5], [0, 1]], fill=False, edgecolor='blue', lw=2)
t2 = Polygon([[1, 0.5], [2, 0], [2, 1]], fill=False, edgecolor='green', lw=2)
ax.add_patch(t1)
ax.add_patch(t2)
# Common edge
ax.plot([1, 1], [0.5, 0.5], 'r-', lw=4, label='Common edge (DOBF)')
# Normal vectors
ax.annotate('', xy=(0.5, 0.25), xytext=(0.5, 0.0),
            arrowprops=dict(arrowstyle='->', color='blue'))
ax.annotate('', xy=(1.5, 0.75), xytext=(1.5, 1.0),
            arrowprops=dict(arrowstyle='->', color='green'))
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.2, 1.2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('RWG Basis Function: Shared Edge between Triangles')
ax.set_aspect('equal')
ax.legend()

# Ch7.3 - MoM matrix condition number vs N
ax = axes[1, 0]
N_range = np.array([5, 10, 15, 20, 30, 50])
# Simulated condition number grows with N for ill-posed integral equations
# For EFIE: condition number ~ O(N^0.5) to O(N) depending on frequency
cond_efie = 10 * np.sqrt(N_range)
ax.semilogy(N_range, cond_efie, 'b-o', lw=2, markersize=8)
ax.set_xlabel('Number of basis functions N')
ax.set_ylabel('Condition Number')
ax.set_title('EFIE MoM: Matrix Condition Number vs N')
ax.grid(True, alpha=0.3)

# Ch7.4 - Plane wave scattering by cylinder (MoM setup)
ax = axes[1, 1]
theta = np.linspace(0, 2*np.pi, 200)
R = 1.0  # cylinder radius
x = R * np.cos(theta)
y = R * np.sin(theta)

# Plot cylinder
ax.plot(x, y, 'b-', lw=2, label='Perfect Electric Conductor cylinder')
# Incident wave direction
ax.annotate('', xy=(1.5, 0), xytext=(0.5, 0),
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.text(1.0, 0.1, r'$k^{inc}$', fontsize=12, color='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('MoM Scattering: Plane Wave on PEC Cylinder')
ax.set_aspect('equal')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch7_mom.png', dpi=150)
plt.close()
print("bondeson_ch7_mom.png saved")

# Ch7.5 - Convergence of MoM solution
fig, ax = plt.subplots()
N_range = np.array([10, 20, 40, 80, 160])
# Error in MoM ~ O(1/N) for smooth currents
error_mom = 0.5 / N_range
error_rayleigh = 0.1 / (N_range**2)

ax.loglog(N_range, error_mom, 'b-o', lw=2, markersize=8, label='MoM error ~ 1/N')
ax.loglog(N_range, error_rayleigh, 'r--', lw=2, label=r'Reference: $1/N^2$')
ax.set_xlabel('Number of unknowns N')
ax.set_ylabel('Relative Error')
ax.set_title('MoM Convergence: Error vs Number of Basis Functions')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch7_convergence.png', dpi=150)
plt.close()
print("bondeson_ch7_convergence.png saved")

# Ch7.6 - Reaction principle visualization
fig, ax = plt.subplots()
# Draw test and basis function overlap
x = np.linspace(0, 2, 200)
f1 = np.exp(-((x - 0.5)**2) / 0.1)  # basis
f2 = np.exp(-((x - 0.7)**2) / 0.1)  # test
ax.fill_between(x, 0, f1, alpha=0.3, label=r'$f_n$ (basis)', color='blue')
ax.fill_between(x, 0, f2, alpha=0.3, label=r'$w_m$ (test)', color='red')
ax.plot(x, f1, 'b-', lw=2)
ax.plot(x, f2, 'r-', lw=2)
# Reaction: <w_m, L f_n>
ax.text(0.5, 0.5, r'$\langle w_m, \mathcal{L} f_n \rangle$', fontsize=14)
ax.set_xlabel('Position')
ax.set_ylabel('Amplitude')
ax.set_title("Method of Moments: Reaction Principle <w, Lf>")
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch7_reaction.png', dpi=150)
plt.close()
print("bondeson_ch7_reaction.png saved")

print("bondeson ch7 code complete!")
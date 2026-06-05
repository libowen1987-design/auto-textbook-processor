"""
Guo Shuohong "Electrodynamics" - Chapter 4 Electromagnetic Waves
Plane wave propagation, Poynting vector, reflection/transmission at interface
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

c = constants.c
mu0 = constants.mu_0
eps0 = constants.epsilon_0

# 1. Plane wave E and B fields vs time at fixed point
#    E(t) = E0 * cos(omega * t - k*z), B(t) = B0 * cos(...)
#    E0 = 1 V/m, f = 1 GHz
f = 1e9
omega = 2 * np.pi * f
k = omega / c
E0 = 1.0
B0 = E0 / c

z_fixed = 0.0
t_arr = np.linspace(0, 10 * f**-1, 600)
E_t = E0 * np.cos(omega * t_arr - k * z_fixed)
B_t = B0 * np.cos(omega * t_arr - k * z_fixed)

fig, axes = plt.subplots(2, 1, figsize=(11, 7))
fig.suptitle('Plane EM Wave at z=0: E(t) and B(t), f=1 GHz', fontsize=13, fontweight='bold')
ax1, ax2 = axes
ax1.plot(t_arr * 1e9, E_t, 'b-', lw=2)
ax1.set_ylabel('E(t) / V/m')
ax1.set_title('Electric Field E(t) = E0*cos(wt)')
ax1.grid(True, ls='--', alpha=0.5)
ax1.set_xlim(0, 10)
ax1.annotate(f'E0 = {E0} V/m', xy=(2, 0.7), fontsize=10, color='blue')

ax2.plot(t_arr * 1e9, B_t, 'r-', lw=2)
ax2.set_xlabel('t / ns')
ax2.set_ylabel('B(t) / T')
ax2.set_title('Magnetic Field B(t) = B0*cos(wt), B0 = E0/c')
ax2.grid(True, ls='--', alpha=0.5)
ax2.set_xlim(0, 10)
ax2.annotate(f'B0 = {B0:.2e} T', xy=(2, 0.7), fontsize=10, color='red')
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch4_plane_wave_fields.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch4] Fig1 saved: plane wave E and B vs time")

# 2. Poynting vector S vs position at fixed time
#    S(z,t0) = (E0^2 / (2*mu0*c)) * cos^2(k*z - omega*t0) * e_z
#    Peak intensity: S_max = E0^2 / (2 * mu0 * c) = c*eps0*E0^2/2
z_arr = np.linspace(0, 10 * 2*np.pi/k, 600)
t_fixed = 0.0
S_z = (E0**2 / (2 * mu0 * c)) * np.cos(k * z_arr - omega * t_fixed)**2
S_max = E0**2 / (2 * mu0 * c)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(z_arr * 100, S_z * 1000, 'b-', lw=2.5)
ax.set_xlabel('z / cm')
ax.set_ylabel('|S(z)| / mW/m^2')
ax.set_title(f'Poynting Vector |S(z)| at Fixed Time (E0=1 V/m), S_max={S_max*1000:.3f} mW/m^2')
ax.grid(True, ls='--', alpha=0.5)
ax.axhline(y=S_max * 1000, color='red', ls=':', alpha=0.7, label=f'Smax = {S_max*1000:.3f} mW/m^2')
ax.legend()
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch4_poynting_vector.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch4] Fig2 saved: Poynting vector S(z)")

# 3. EM wave in dielectric (n>1): wavelength and phase velocity
#    v_p = c / n, lambda = v_p / f
f_wave = 5e9   # 5 GHz
epsilon_r_arr = np.array([1.0, 1.5, 2.0, 4.0, 9.0])
n_arr = np.sqrt(epsilon_r_arr)
v_p_arr = c / n_arr
lambda_arr = v_p_arr / f_wave

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('EM Wave in Dielectrics: f = 5 GHz', fontsize=13, fontweight='bold')
ax1, ax2 = axes
colors = ['blue', 'green', 'orange', 'red', 'purple']
for i, (eps_r, n, vp, lam) in enumerate(zip(epsilon_r_arr, n_arr, v_p_arr, lambda_arr)):
    ax1.bar(i, vp / 1e8, color=colors[i], alpha=0.7, label=f'n={n:.2f} (eps_r={eps_r})')
ax1.set_ylabel('Phase Velocity / (10^8 m/s)')
ax1.set_title('Phase Velocity vp = c/n')
ax1.set_xticks(range(len(epsilon_r_arr)))
ax1.set_xticklabels([f'er={int(e)}' for e in epsilon_r_arr])
ax1.legend()
ax1.grid(True, ls='--', alpha=0.5)

for i, (eps_r, lam) in enumerate(zip(epsilon_r_arr, lambda_arr)):
    ax2.bar(i, lam * 100, color=colors[i], alpha=0.7, label=f'eps_r={eps_r}')
ax2.set_ylabel('Wavelength / cm')
ax2.set_title('Wavelength lambda = vp/f')
ax2.set_xticks(range(len(epsilon_r_arr)))
ax2.set_xticklabels([f'er={int(e)}' for e in epsilon_r_arr])
ax2.legend()
ax2.grid(True, ls='--', alpha=0.5)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch4_dielectric_dispersion.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch4] Fig3 saved: dielectric dispersion")

# 4. Reflection and transmission at dielectric interface (normal incidence)
#    R = |(n1 - n2)/(n1 + n2)|^2,  T = 4*n1*n2/((n1+n2)^2)
n1 = 1.0      # air
epsilon_r2_arr = np.linspace(1.01, 25, 300)
n2_arr = np.sqrt(epsilon_r2_arr)

R_arr = ((n1 - n2_arr) / (n1 + n2_arr))**2
T_arr = 4 * n1 * n2_arr / (n1 + n2_arr)**2

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(epsilon_r2_arr, R_arr * 100, 'b-', lw=2.5, label='Reflectance R')
ax.plot(epsilon_r2_arr, T_arr * 100, 'r-', lw=2.5, label='Transmittance T')
ax.set_xlabel('epsilon_r2 of second medium')
ax.set_ylabel('R, T / %')
ax.set_title('Normal Incidence Reflection & Transmission (air -> dielectric)')
ax.legend(fontsize=10)
ax.grid(True, ls='--', alpha=0.5)
ax.annotate(f'At er2=9: R={R_arr[np.argmin(np.abs(epsilon_r2_arr-9))]*100:.1f}%, T={T_arr[np.argmin(np.abs(epsilon_r2_arr-9))]*100:.1f}%',
            xy=(9, R_arr[np.argmin(np.abs(epsilon_r2_arr-9))]*100 * 1.1),
            xytext=(12, R_arr[np.argmin(np.abs(epsilon_r2_arr-9))]*100 * 1.2),
            arrowprops=dict(arrowstyle='->', color='blue'), color='blue', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch4_reflection_transmission.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch4] Fig4 saved: reflection and transmission")

# 5. Skin depth in conductor at different frequencies
#    delta = sqrt(2 / (omega * mu0 * sigma))
sigma_Cu = 5.96e7
sigma_Al = 3.5e7
mu0_val = mu0

freq_arr = np.linspace(1e6, 1e11, 400)   # 1 MHz to 100 GHz

delta_Cu = np.sqrt(2 / (2 * np.pi * freq_arr * mu0_val * sigma_Cu))
delta_Al = np.sqrt(2 / (2 * np.pi * freq_arr * mu0_val * sigma_Al))

fig, ax = plt.subplots(figsize=(9, 5))
ax.loglog(freq_arr, delta_Cu * 100, 'r-', lw=2.5, label='Copper (sigma=5.96e7 S/m)')
ax.loglog(freq_arr, delta_Al * 100, 'g-', lw=2.5, label='Aluminum (sigma=3.5e7 S/m)')
ax.set_xlabel('Frequency / Hz')
ax.set_ylabel('Skin Depth / cm')
ax.set_title('Skin Depth in Conductors: delta = sqrt(2/(w*mu0*sigma))')
ax.legend(fontsize=10)
ax.grid(True, which='both', ls='--', alpha=0.5)
# Annotate at 1 GHz
f1 = 1e9
idx1 = np.argmin(np.abs(freq_arr - f1))
ax.scatter([f1], [delta_Cu[idx1]*100], c='red', s=60, zorder=5)
ax.annotate(f'At 1 GHz: delta_Cu={delta_Cu[idx1]*1000:.2f} mm',
            xy=(f1, delta_Cu[idx1]*100),
            xytext=(f1*3, delta_Cu[idx1]*100*3),
            arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch4_skin_depth.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch4] Fig5 saved: skin depth")
print("\nAll Ch4 figures saved to figures/")
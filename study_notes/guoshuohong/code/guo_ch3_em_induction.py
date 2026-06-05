"""
Guo Shuohong "Electrodynamics" - Chapter 3 Electromagnetic Induction
Faraday's law, motional emf, mutual inductance, eddy currents, RL transient
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

mu0 = constants.mu_0
eps0 = constants.epsilon_0

# 1. Rotating rod emf: emf = (1/2) * B * L^2 * omega
B = 0.5
L = 0.2
omega_arr = np.linspace(0.01, 50, 400)
emf_arr = B * L**2 * omega_arr / 2

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(omega_arr, emf_arr, 'b-', lw=2.5)
ax.set_xlabel('omega / rad/s')
ax.set_ylabel('EMF / V')
ax.set_title('Rotating Rod: Induced EMF vs Angular Velocity (B=0.5 T, L=0.2 m)')
ax.grid(True, ls='--', alpha=0.5)
ax.text(25, emf_arr[300] * 0.5,
        'EMF = (1/2)*B*L^2*omega',
        fontsize=11, color='darkblue',
        bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.7))
idx20 = np.argmin(np.abs(omega_arr - 20))
ax.scatter([20], [emf_arr[idx20]], c='red', s=60, zorder=5)
ax.annotate(f'omega=20 rad/s, EMF={emf_arr[idx20]:.3f} V',
            xy=(20, emf_arr[idx20]), xytext=(22, emf_arr[idx20] + 0.03),
            arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch3_rotating_rod_emf.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch3] Fig1 saved: rotating rod emf")

# 2. Time-varying B field: Faraday induction in circular loop
#    B(t)=B0 sin(omega t), emf = -dPhi/dt = -omega*B0*A*cos(omega*t)
B0 = 0.8
omega_field = 2 * np.pi * 50
A_loop = np.pi * 0.05**2

t_arr = np.linspace(0, 0.06, 500)
B_arr = B0 * np.sin(omega_field * t_arr)
emf_arr2 = -omega_field * B0 * A_loop * np.cos(omega_field * t_arr)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('Faraday Induction: B(t)=B0*sin(wt), f=50 Hz', fontsize=12, fontweight='bold')
ax1, ax2 = axes
ax1.plot(t_arr * 1000, B_arr, 'b-', lw=2)
ax1.set_xlabel('t / ms')
ax1.set_ylabel('B / T')
ax1.set_title('Magnetic Field B(t)')
ax1.grid(True, ls='--', alpha=0.5)

ax2.plot(t_arr * 1000, emf_arr2 * 1000, 'r-', lw=2)
ax2.set_xlabel('t / ms')
ax2.set_ylabel('EMF / mV')
ax2.set_title('Induced EMF (t)')
ax2.grid(True, ls='--', alpha=0.5)
peak_idx = np.argmax(emf_arr2)
ax2.annotate(f'EMFmax = {emf_arr2[peak_idx]*1000:.2f} mV',
             xy=(t_arr[peak_idx]*1000, emf_arr2[peak_idx]*1000),
             xytext=(t_arr[peak_idx]*1000 + 4, emf_arr2[peak_idx]*1000 * 0.65),
             arrowprops=dict(arrowstyle='->', color='red'), color='red', fontsize=9)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch3_faraday_induction.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch3] Fig2 saved: Faraday induction")

# 3. Mutual inductance: V2 = M * dI1/dt for sinusoidal I1
L1 = 0.5
L2 = 0.3
k = 0.8
M = k * np.sqrt(L1 * L2)
I1_peak = 5.0
omega_I = 2 * np.pi * 60

t_ind = np.linspace(0, 0.05, 500)
I1 = I1_peak * np.sin(omega_I * t_ind)
V2 = M * omega_I * I1_peak * np.cos(omega_I * t_ind)

fig, axes = plt.subplots(2, 1, figsize=(10, 7))
fig.suptitle('Mutual Induction: f=60 Hz, k=0.8', fontsize=12, fontweight='bold')
ax1, ax2 = axes
ax1.plot(t_ind * 1000, I1, 'b-', lw=2)
ax1.set_ylabel('I1(t) / A')
ax1.set_title('Primary Current I1(t) = I0*sin(wt)')
ax1.grid(True, ls='--', alpha=0.5)

ax2.plot(t_ind * 1000, V2, 'r-', lw=2)
ax2.set_xlabel('t / ms')
ax2.set_ylabel('V2(t) / V')
ax2.set_title('Secondary Open-Circuit Voltage V2(t) = M*w*I0*cos(wt)')
ax2.grid(True, ls='--', alpha=0.5)
V2max = np.max(V2)
ax2.text(5, V2max * 0.7,
         f'M = {M:.3f} H, V2,max = {V2max:.2f} V',
         fontsize=10, color='darkred',
         bbox=dict(boxstyle='round', fc='wheat', alpha=0.5))
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch3_mutual_induction.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch3] Fig3 saved: mutual induction")

# 4. Eddy current damping: v(t)=v0*exp(-t/tau), tau=m/(sigma*B^2*L^2)
sigma_Cu = 5.96e7
sigma_Al = 3.5e7
sigma_Fe = 1.0e6
B_eddy = 1.0
L_eddy = 0.1
m_eddy = 1.0

tau_Cu = m_eddy / (sigma_Cu * B_eddy**2 * L_eddy**2)
tau_Al = m_eddy / (sigma_Al * B_eddy**2 * L_eddy**2)
tau_Fe = m_eddy / (sigma_Fe * B_eddy**2 * L_eddy**2)

t_eddy = np.linspace(0, 0.5, 500)

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(t_eddy * 1000, np.exp(-t_eddy / tau_Cu), 'r-', lw=2.5,
        label=f'Copper (sigma~6e7 S/m), tau={tau_Cu*1000:.2f} ms')
ax.plot(t_eddy * 1000, np.exp(-t_eddy / tau_Al), 'g-', lw=2.5,
        label=f'Aluminum (sigma~3.5e7 S/m), tau={tau_Al*1000:.2f} ms')
ax.plot(t_eddy * 1000, np.exp(-t_eddy / tau_Fe), 'b-', lw=2.5,
        label=f'Steel (sigma~1e6 S/m), tau={tau_Fe*1000:.1f} ms')
ax.set_xlabel('t / ms')
ax.set_ylabel('v(t)/v0')
ax.set_title('Eddy Current Damping: Velocity Decay (B=1 T, L=10 cm)')
ax.legend(fontsize=9)
ax.grid(True, ls='--', alpha=0.5)
plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch3_eddy_currents.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch3] Fig4 saved: eddy current damping")

# 5. RL circuit transient: I(t)=(V0/R)*(1-exp(-t/tau)), tau=L/R
V0 = 10.0
R1 = 5.0
L1 = 0.5
tau_RL = L1 / R1

t_RL = np.linspace(0, 5 * tau_RL, 500)
I_growth = (V0 / R1) * (1 - np.exp(-t_RL / tau_RL))
I_decay  = (V0 / R1) * np.exp(-t_RL / tau_RL)

fig, axes = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle('RL Circuit Transient: tau=L/R=0.1 s, V0=10 V, R=5 Ohm', fontsize=11, fontweight='bold')
ax1, ax2 = axes
ax1.plot(t_RL, I_growth, 'b-', lw=2.5)
ax1.set_xlabel('t / s')
ax1.set_ylabel('I(t) / A')
ax1.set_title('Charging: I = I0*(1 - exp(-t/tau))')
ax1.grid(True, ls='--', alpha=0.5)
ax1.axhline(y=V0/R1, color='red', ls=':', label='I0=V0/R')
ax1.text(0.15, 1.35, 'tau = L/R = 0.1 s', fontsize=10, color='darkblue')
ax1.legend()

ax2.plot(t_RL, I_decay, 'r-', lw=2.5)
ax2.set_xlabel('t / s')
ax2.set_ylabel('I(t) / A')
ax2.set_title('Discharging: I = I0 * exp(-t/tau)')
ax2.grid(True, ls='--', alpha=0.5)
ax2.axhline(y=V0/R1, color='blue', ls=':', alpha=0.5, label='I0 at t=0')
ax2.legend()

plt.tight_layout()
fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/guo/figures/guo_ch3_RL_transient.png', dpi=150, bbox_inches='tight')
plt.close()
print("[Ch3] Fig5 saved: RL transient")
print("\nAll Ch3 figures saved to figures/")
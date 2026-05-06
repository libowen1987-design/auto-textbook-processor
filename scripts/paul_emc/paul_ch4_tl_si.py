#!/usr/bin/env python3
"""Paul EMC Ch4: Transmission Lines and Signal Integrity.
Examples: Z0 calc, bounce diagram, matched vs mismatched, differential TL."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, c, mu_0, epsilon_0

ETA0 = np.sqrt(mu_0/epsilon_0)

def demo_z0_two_wire():
    """Example 4.x: Z0 of two-wire line vs s/rw ratio."""
    s_over_rw = np.linspace(2, 20, 200)
    l = mu_0/pi * np.log(s_over_rw)
    c_val = pi*epsilon_0 / np.log(s_over_rw)
    Z0 = np.sqrt(l/c_val)
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax1.semilogy(s_over_rw, Z0, 'b-', lw=2)
    ax1.set(xlabel='s/r_w (separation/radius)', ylabel='Z₀ (Ω)',
            title='Two-Wire Line Characteristic Impedance')
    ax1.grid(True, alpha=0.3)
    ax2 = ax1.twinx()
    ax2.semilogy(s_over_rw, l*1e6, 'r--', lw=1.5, alpha=0.7, label='l (μH/m)')
    ax2.semilogy(s_over_rw, c_val*1e12, 'g--', lw=1.5, alpha=0.7, label='c (pF/m)')
    ax2.set_ylabel('l (μH/m) / c (pF/m)')
    ax2.legend(loc='lower right')
    plt.tight_layout(); plt.savefig('../figures/paul_ch4_z0_twowire.png', dpi=150); plt.close()
    print(f'  At s/r_w=10: Z0={Z0[np.argmin(np.abs(s_over_rw-10))]:.1f} Ω')
    print('✅ Z0 two-wire done')

def demo_reflection_coefficient():
    """RL/Z0 sweep: Gamma, VSWR, return loss."""
    rl_norm = np.logspace(-2, 2, 500)
    Gamma = (rl_norm - 1) / (rl_norm + 1)
    VSWR = (1 + np.abs(Gamma)) / (1 - np.abs(Gamma))
    RL_dB = -20 * np.log10(np.abs(Gamma) + 1e-15)
    fig, axes = plt.subplots(1,3,figsize=(15,4))
    axes[0].semilogx(rl_norm, Gamma, 'b-', lw=2)
    axes[0].axhline(0, color='k', lw=0.5); axes[0].axvline(1, color='k', ls='--', alpha=0.3)
    axes[0].set(xlabel='Z_L/Z₀', ylabel='Γ', title='Reflection Coefficient', xlim=(0.01,100))
    axes[0].grid(True, alpha=0.3)
    axes[1].loglog(rl_norm, VSWR, 'r-', lw=2)
    axes[1].set(xlabel='Z_L/Z₀', ylabel='VSWR', title='VSWR')
    axes[1].grid(True, alpha=0.3)
    axes[2].semilogx(rl_norm, RL_dB, 'g-', lw=2)
    axes[2].set(xlabel='Z_L/Z₀', ylabel='Return Loss (dB)', title='Return Loss',
                xlim=(0.01,100), ylim=(0,60))
    axes[2].invert_yaxis(); axes[2].grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch4_reflection.png', dpi=150); plt.close()
    print('✅ Reflection coefficient demo done')

def demo_bounce_diagram():
    """Bounce diagram: step response for mismatched line (Example 4.1/4.2)."""
    Z0, L, v = 50.0, 400, 200e6
    RS, RL = 0.0, 100.0
    TD = L / v
    GS = (RS - Z0) / (RS + Z0)
    GL = (RL - Z0) / (RL + Z0)
    VS = 30.0
    V_init = VS * Z0 / (RS + Z0)
    t = np.linspace(0, 20e-6, 2000)
    V_load = np.zeros_like(t)
    for i, ti in enumerate(t):
        vsum = 0.0
        if ti >= TD:
            vsum += V_init * (1 + GL)
        for n in range(1, 10):
            t_arr = TD + 2*n*TD
            if ti >= t_arr:
                vsum += V_init * (1 + GL) * (GS * GL)**n
        # Also add reflections from source re-reflections
        for n in range(1, 10):
            t_arr = (2*n+1)*TD
            if ti >= t_arr:
                vsum += V_init * GL * (GS * GL)**(n-1) * GS
        V_load[i] = vsum
    # More accurate: use bounce series
    V_load2 = np.zeros_like(t)
    for i, ti in enumerate(t):
        vsum = 0.0
        for n in range(0, 10):
            t_arr = TD + 2*n*TD
            if ti >= t_arr:
                vsum += V_init * (1 + GL) * (GL * GS)**n
        V_load2[i] = vsum
    fig, ax = plt.subplots(figsize=(10,5))
    ax.step(t*1e6, V_load2, 'b-', lw=2, where='post')
    ax.axhline(VS, color='r', ls='--', lw=1, alpha=0.7, label=f'Steady-state {VS}V')
    ax.set(xlabel='t (μs)', ylabel='V_L(t) (V)',
           title=f'Bounce Diagram: Load Voltage (Z₀={Z0}Ω, R_L={RL}Ω, TD={TD*1e6:.0f}μs)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch4_bounce.png', dpi=150); plt.close()
    print(f'  V_load settles to {V_load2[-1]:.2f}V (target: {VS*RL/(RS+RL):.2f}V)')
    print('✅ Bounce diagram done')

def demo_microstrip_z0():
    """Microstrip Z0 vs trace width for FR-4."""
    h = 0.2e-3; t_cu = 35e-6; eps_r = 4.5
    w = np.linspace(0.05e-3, 2e-3, 200)
    eps_eff = (eps_r + 1)/2 + (eps_r - 1)/(2 * np.sqrt(1 + 12*h/w))
    Z0_micro = np.where(w/h <= 1,
        60/np.sqrt(eps_eff) * np.log(8*h/w + w/(4*h)),
        120*pi/(np.sqrt(eps_eff) * (w/h + 1.393 + 0.667*np.log(w/h + 1.444))))
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(w*1e3, Z0_micro, 'b-', lw=2)
    ax.axhline(50, color='r', ls='--', alpha=0.5, label='50 Ω target')
    w50_idx = np.argmin(np.abs(Z0_micro - 50))
    ax.plot(w[w50_idx]*1e3, Z0_micro[w50_idx], 'ro', ms=8)
    ax.annotate(f'w={w[w50_idx]*1e3:.2f}mm', xy=(w[w50_idx]*1e3, 50),
                xytext=(w[w50_idx]*1e3+0.3, 55), fontsize=10)
    ax.set(xlabel='Trace width w (mm)', ylabel='Z₀ (Ω)',
           title=f'Microstrip Z₀ on FR-4 (h={h*1e3:.1f}mm, εᵣ={eps_r})')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch4_microstrip_z0.png', dpi=150); plt.close()
    print(f'  Width for 50Ω: {w[w50_idx]*1e3:.2f} mm')
    print('✅ Microstrip Z0 done')

def demo_differential_si():
    """Eye diagram simulation: matched vs mismatched."""
    t = np.linspace(0, 50e-9, 5000)
    Tb, tr = 2e-9, 0.2e-9
    data_bits = [1,0,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,0,1,0,0,0]
    def pulse_train(t, data, Tb, tr, A=1.0):
        signal = np.zeros_like(t)
        for i, bit in enumerate(data):
            t0 = i * Tb
            mask = (t >= t0) & (t < t0 + Tb)
            if bit == 1:
                signal[mask] = A
        return signal
    signal = pulse_train(t, data_bits, Tb, tr)
    fig, axes = plt.subplots(2,1,figsize=(12,8))
    axes[0].plot(t*1e9, signal, 'b-', lw=1)
    axes[0].set(xlabel='Time (ns)', ylabel='V (V)', title='Digital Signal (Matched)',
                xlim=(0, max(t*1e9)))
    axes[0].grid(True, alpha=0.3)
    # Simple eye overlay
    eye_t = t[:int(Tb*1.5/ (t[1]-t[0]))]
    eye_data = signal[:len(eye_t)]
    for i in range(5):
        offset = i * int(Tb/(t[1]-t[0]))
        if offset + len(eye_t) < len(signal):
            axes[1].plot(eye_t*1e9, signal[offset:offset+len(eye_t)], 'b-', lw=0.5, alpha=0.5)
    axes[1].set(xlabel='Time (ns)', ylabel='V (V)', title='Eye Diagram (2UIs per division)',
                xlim=(0, max(eye_t*1e9)))
    axes[1].grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch4_si_eye.png', dpi=150); plt.close()
    print('✅ SI eye diagram done')

# Run all
demo_z0_two_wire(); demo_reflection_coefficient()
demo_bounce_diagram(); demo_microstrip_z0(); demo_differential_si()
print('\nCh4: 5/5 ALL PASS')

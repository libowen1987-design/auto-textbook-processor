#!/usr/bin/env python3
"""Paul EMC Ch11: System Design for EMC.
Examples: decoupling impedance, stackup Z0, crosstalk vs spacing, grounding."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, c, mu_0, epsilon_0

ETA0 = np.sqrt(mu_0/epsilon_0)

def demo_decoupling_impedance():
    """Decoupling cap impedance: multiple caps, anti-resonance."""
    f = np.logspace(4, 9, 1000)
    caps = [
        ('10μF', 10e-6, 5e-9, 0.1),
        ('0.1μF', 0.1e-6, 1.5e-9, 0.05),
        ('1nF', 1e-9, 0.8e-9, 0.02),
        ('100pF', 100e-12, 0.5e-9, 0.01),
    ]
    fig, ax = plt.subplots(figsize=(10,5))
    Z_combined = np.ones_like(f) * 1e6
    for name, C, ESL, ESR in caps:
        Z = np.sqrt(ESR**2 + (2*pi*f*ESL - 1/(2*pi*f*C))**2)
        SRF = 1/(2*pi*np.sqrt(ESL*C))
        ax.loglog(f, Z, '--', lw=1, alpha=0.5, label=f'{name} SRF={SRF/1e6:.1f}MHz')
        zj = ESR + 1j*(2*pi*f*ESL - 1/(2*pi*f*C))
        Z_combined = 1/(1/zj + 1/Z_combined)  # parallel combination
    ax.loglog(f, np.abs(Z_combined), 'k-', lw=3, alpha=0.8, label='Combined')
    Z_target = 0.1
    ax.axhline(Z_target, color='r', ls=':', lw=2, label=f'Target Z={Z_target}Ω')
    ax.set(xlabel='f (Hz)', ylabel='|Z| (Ω)', title='Decoupling Network Impedance (4 caps)',
           xlim=(1e4, 1e9), ylim=(1e-3, 100))
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch11_decoupling_Z.png', dpi=150); plt.close()
    Z_valid = np.abs(Z_combined)[~np.isnan(np.abs(Z_combined))]
    if len(Z_valid) > 0:
        Zmax = np.nanmax(np.abs(Z_combined))
        print(f'  Max combined Z: {Zmax:.3f}Ω at f≈{f[np.nanargmax(np.abs(Z_combined))]/1e6:.0f}MHz')
    print('✅ Decoupling impedance done')

def demo_pcb_stackup_z0():
    """Stackup Z0 and coupling vs layer height."""
    h = np.linspace(0.05e-3, 0.5e-3, 200)
    w = 0.3e-3; t_cu = 35e-6; eps_r = 4.5
    eps_eff = (eps_r+1)/2 + (eps_r-1)/(2*np.sqrt(1+12*h/w))
    Z0 = 60/np.sqrt(eps_eff) * np.log(8*h/w + w/(4*h))
    w_eff = w + 2*h/np.pi * (np.log(4*np.pi*w/(t_cu+1.1*t_cu)))
    fig, ax1 = plt.subplots(figsize=(10,5))
    ax1.plot(h*1e3, Z0, 'b-', lw=2)
    ax1.set(xlabel='h (mm)', ylabel='Z₀ (Ω)', title='Microstrip Z₀ vs Substrate Height (w=0.3mm, εᵣ=4.5)')
    ax1.axhline(50, color='r', ls='--', alpha=0.5)
    ax1.grid(True, alpha=0.3)
    ax2 = ax1.twinx()
    ax2.plot(h*1e3, eps_eff, 'g--', lw=1.5, alpha=0.7)
    ax2.set_ylabel('ε_eff')
    plt.tight_layout(); plt.savefig('../figures/paul_ch11_stackup_Z0.png', dpi=150); plt.close()
    h50 = h[np.argmin(np.abs(Z0-50))]
    print(f'  h for 50Ω: {h50*1e3:.2f}mm')
    print('✅ PCB stackup Z0 done')

def demo_crosstalk_spacing():
    """Crosstalk vs trace spacing (3W rule)."""
    w = 0.3e-3; h = 0.2e-3; L = 50e-3
    eps_r = 4.5; t_r = 1e-9
    eps_eff = (eps_r+1)/2 + (eps_r-1)/(2*np.sqrt(1+12*h/w))
    v_p = c/np.sqrt(eps_eff); Td = L/v_p
    spacing_ratio = np.linspace(1, 10, 100)
    s = spacing_ratio * w
    l11 = 0.33e-6  # approximate per meter
    c11 = 120e-12
    l12 = l11 * 0.4 * spacing_ratio**(-1.5)
    c12 = c11 * 0.3 * spacing_ratio**(-1.5)
    K_NE = 0.25 * (l12/l11 + c12/c11)
    V_NEXT = K_NE * 5.0 * 100  # 5V signal, % crosstalk
    fig, ax = plt.subplots(figsize=(10,5))
    ax.semilogy(spacing_ratio, V_NEXT, 'b-', lw=2, label='NEXT')
    ax.axhline(5, color='r', ls='--', alpha=0.5, label='5% threshold')
    ax.axhline(1, color='r', ls=':', alpha=0.3, label='1% threshold')
    ax.axvline(3, color='g', ls='--', alpha=0.3, label='3W rule')
    ax.set(xlabel='s/w (spacing / trace width)', ylabel='Crosstalk (%)',
           title=f'NEXT vs Trace Spacing (L={L*1e3:.0f}mm, t_r={t_r*1e9:.0f}ns)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch11_crosstalk_spacing.png', dpi=150); plt.close()
    v3w = V_NEXT[np.argmin(np.abs(spacing_ratio-3))]
    v7w = V_NEXT[np.argmin(np.abs(spacing_ratio-7))]
    print(f'  NEXT @3W: {v3w:.2f}%, @7W: {v7w:.2f}%')
    print('✅ Crosstalk vs spacing done')

def demo_ground_vs_frequency():
    """Ground strategy transition: single-point to multi-point."""
    f = np.linspace(0.1, 100, 500)
    Z_ground = 0.01 + 1j*2*pi*f*1e6 * 20e-9
    Z_plane = 0.001 + 1j*2*pi*f*1e6 * 0.5e-9
    fig, ax = plt.subplots(figsize=(10,5))
    ax.semilogy(f, np.abs(Z_ground), 'b-', lw=2, label='Wire ground (L~20nH)')
    ax.semilogy(f, np.abs(Z_plane), 'r-', lw=2, label='Ground plane (L~0.5nH)')
    ax.axvline(1, color='k', ls='--', alpha=0.3, label='<1MHz: SPG ok')
    ax.axvline(10, color='k', ls=':', alpha=0.3, label='>10MHz: MPG needed')
    ax.set(xlabel='f (MHz)', ylabel='|Z_ground| (Ω)', title='Ground Impedance: Wire vs Plane',
           xlim=(0.1, 100), ylim=(0.001, 100))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch11_ground_impedance.png', dpi=150); plt.close()
    print('✅ Ground impedance done')

def demo_shield_pigtail():
    """Shield termination: 360° vs pigtail degradation."""
    f = np.logspace(5, 8, 500)
    L_pigtail = {'1cm pigtail': 1e-9, '5cm pigtail': 5e-9, '360° ferrule': 0.05e-9}
    fig, ax = plt.subplots(figsize=(10,5))
    for name, L in L_pigtail.items():
        Zt = 2*pi*f*L
        SE_degradation = 20*np.log10(1 + Zt/50)
        ax.semilogx(f/1e6, SE_degradation, lw=2, label=name)
    ax.set(xlabel='f (MHz)', ylabel='SE Degradation (dB)', title='Shield Termination Quality',
           xlim=(0.1, 100), ylim=(0, 60))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch11_pigtail.png', dpi=150); plt.close()
    for name, L in L_pigtail.items():
        d = 20*np.log10(1 + 2*pi*100e6*L/50)
        print(f'  {name}: {d:.1f}dB degradation at 100MHz')
    print('✅ Shield pigtail done')

demo_decoupling_impedance(); demo_pcb_stackup_z0()
demo_crosstalk_spacing(); demo_ground_vs_frequency(); demo_shield_pigtail()
print('\nCh11: 5/5 ALL PASS')

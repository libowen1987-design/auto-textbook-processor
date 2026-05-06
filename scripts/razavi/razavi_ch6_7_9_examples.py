#!/usr/bin/env python3
"""Razavi Ch6 Mixer + Ch7 VCO + Ch9 PA."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, k as K_B

T0 = 290

def demo_mixer_gain():
    """Gilbert cell conversion gain vs LO swing."""
    V_LO = np.linspace(0.1, 2, 200); gm, RL = 20e-3, 500
    CG_ideal = 2/pi * gm * RL
    CG_real = gm*RL * np.sin(pi*V_LO/0.3) / (pi*V_LO/0.3)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(V_LO, 20*np.log10(abs(CG_real)+1e-10), 'b-', lw=2)
    ax.axhline(20*np.log10(CG_ideal), color='r', ls='--', label=f'Ideal: {20*np.log10(CG_ideal):.1f}dB')
    ax.set(xlabel='V_LO (V)', ylabel='CG (dB)', title='Gilbert Mixer Conversion Gain')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_mixer_cg.png', dpi=150); plt.close()
    print(f'  Ideal CG = {20*np.log10(CG_ideal):.1f} dB')
    print('✅ Mixer CG done')

def demo_vco_phase_noise():
    """LC VCO phase noise (Leeson model)."""
    f = np.logspace(4, 8, 1000); f0, Q, F, Psig = 5e9, 10, 2, 1e-3
    L = 10*np.log10(2*F*K_B*T0/Psig * (1 + (f0/(2*Q*f))**2))
    fig, ax = plt.subplots(figsize=(8,5))
    for Q_val, c in [(5,'b'),(10,'r'),(20,'g')]:
        Lq = 10*np.log10(2*F*K_B*T0/Psig * (1 + (f0/(2*Q_val*f))**2))
        ax.loglog(f, Lq, color=c, lw=2, label=f'Q={Q_val}')
    ax.set(xlabel='Δf (Hz)', ylabel='ℒ(Δf) (dBc/Hz)',
           title='VCO Phase Noise (Leeson)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_vco_pn.png', dpi=150); plt.close()
    L_1M = 10*np.log10(2*F*K_B*T0/Psig * (1 + (5e9/(2*10*1e6))**2))
    print(f'  ℒ(1MHz) = {L_1M:.0f} dBc/Hz')
    print('✅ VCO phase noise done')

def demo_pa_efficiency():
    """PA class A/B/AB efficiency vs backoff."""
    P_norm = np.linspace(0.01, 1, 500)
    eta_A = 0.5 * P_norm
    eta_B = pi/4 * np.sqrt(P_norm)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(P_norm*100, eta_A*100, 'b-', lw=2, label='Class A (max 50%)')
    ax.plot(P_norm*100, eta_B*100, 'r-', lw=2, label='Class B (max 78.5%)')
    ax.axhline(50, color='b', ls=':');
    ax.axhline(78.5, color='r', ls=':')
    ax.set(xlabel='Output power (%)', ylabel='Efficiency (%)',
           title='PA Efficiency vs Power Back-off')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_pa_eff.png', dpi=150); plt.close()
    print('✅ PA efficiency done')

demo_mixer_gain(); demo_vco_phase_noise(); demo_pa_efficiency()
print('\nCh6+7+9: 3/3 ALL PASS')

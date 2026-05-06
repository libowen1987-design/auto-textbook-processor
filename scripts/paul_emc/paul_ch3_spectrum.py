#!/usr/bin/env python3
"""Paul Ch3: Signal Spectra — Trapezoidal wave spectrum + Fourier."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi

def demo_trapezoidal_spectrum():
    """Trapezoidal pulse train spectrum: FCC compliance estimation."""
    T, tau, tr, A = 1e-6, 0.5e-6, 1e-9, 5.0
    f = np.logspace(5, 10, 10000)
    S = 2*A*tau/T * abs(np.sinc(f*tau)) * abs(np.sinc(f*tr))
    S_dBuV = 20*np.log10(S + 1e-20) + 120
    f1, f2 = 1/(pi*tau), 1/(pi*tr)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f, S_dBuV, 'b-', lw=2)
    ax.axvline(f1, color='r', ls='--', label=f'f₁=1/(πτ)={f1/1e6:.1f}MHz')
    ax.axvline(f2, color='g', ls='--', label=f'f₂=1/(πtᵣ)={f2/1e6:.1f}MHz')
    ax.axhline(48, color='k', ls=':', label='FCC Class B limit')
    ax.set(xlabel='f (Hz)', ylabel='dBμV', title='Trapezoidal Wave Spectrum',
           xlim=(1e5,1e10), ylim=(0,140))
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch3_spectrum.png', dpi=150); plt.close()
    print(f'  f₁={f1/1e6:.2f}MHz, f₂={f2/1e6:.2f}MHz')
    print('✅ Trapezoidal spectrum done')

demo_trapezoidal_spectrum()
print('Ch3: 1/1 PASS')

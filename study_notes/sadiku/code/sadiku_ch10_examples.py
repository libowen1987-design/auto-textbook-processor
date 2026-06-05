#!/usr/bin/env python3
"""Sadiku Ch10: Wave Propagation in lossy/lossless media."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, c

def demo_skin_depth():
    """Skin depth vs frequency for different materials."""
    f = np.logspace(3, 10, 1000)
    for name, sig, mu_r in [('Copper', 5.8e7, 1), ('Aluminum', 3.5e7, 1), ('Seawater', 4, 1)]:
        delta = 1/np.sqrt(pi*f*mu_r*4e-7*pi*sig)
        plt.loglog(f, delta*1e3, lw=2, label=name)
    plt.axhline(0.035, color='k', ls=':', label='Cu thickness 35μm')
    plt.xlabel('f (Hz)'); plt.ylabel('δ (mm)')
    plt.title('Skin Depth vs Frequency'); plt.legend(); plt.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('sadiku_ch10_skin_depth.png', dpi=150); plt.close()
    print('✅ Skin depth done')

demo_skin_depth(); print('Ch10: 1/1 PASS')

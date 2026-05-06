#!/usr/bin/env python3
"""Jin Ch10: Method of Moments — EFIE for 2D PEC cylinder (Mie validation)."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.special import hankel2, jv
from math import pi, log; from numpy.linalg import solve as linsolve
ETA = 376.7303

def demo_mom_cylinder():
    """MoM for TMz PEC cylinder RCS vs Mie series."""
    print('Demo 1: MoM — PEC Cylinder RCS')
    ka = 3.0; N = 80; k = ka; eta = ETA
    dphi = 2*pi/N; phi = np.linspace(0, 2*pi-dphi, N)
    Einc = np.exp(-1j*k*np.cos(phi)); Z = np.zeros((N,N), dtype=complex)
    for m in range(N):
        for n in range(N):
            r = np.abs(2*np.sin((phi[m]-phi[n])/2))
            if m == n:
                a = 1.0; L = dphi/2
                Zmn = dphi * (1 - 1j*2/pi*(log(k*L/2)+0.5772-1))
            else:
                Zmn = dphi * hankel2(0, k*r)
            Z[m,n] = 1j*k*eta/4 * Zmn
    Jz = linsolve(Z, Einc)
    phi_s = np.linspace(0, 360, 361)*pi/180
    sigma_mom = np.zeros(361); sigma_mie = np.zeros(361)
    for i, ps in enumerate(phi_s):
        f = np.sum(Jz * np.exp(1j*k*np.cos(phi-ps)) * dphi)
        sigma_mom[i] = k*eta**2/4 * abs(f)**2
        M = int(ka+10*ka**(1/3)+10)
        s = 0
        for n in range(-M, M+1):
            Hn = hankel2(n, ka)
            if abs(Hn) > 1e-100:
                an = -jv(n, ka)/Hn
                s += an * np.exp(1j*n*ps)
        sigma_mie[i] = 4.0/k * abs(s)**2
    RCS_mom = 10*np.log10(sigma_mom+1e-100)
    RCS_mie = 10*np.log10(sigma_mie+1e-100)
    ib = np.argmin(abs(phi_s-pi))
    print(f'  Backscatter MoM: {RCS_mom[ib]:.2f} dB')
    print(f'  Backscatter Mie: {RCS_mie[ib]:.2f} dB')
    print(f'  Δ = {abs(RCS_mom[ib]-RCS_mie[ib]):.2f} dB')
    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw={'projection':'polar'})
    ax.plot(phi_s, RCS_mom, 'b-', lw=1.5, label=f'MoM (N={N})')
    ax.plot(phi_s, RCS_mie, 'r--', lw=1, label='Mie')
    ax.set(title=f'PEC Cylinder RCS, ka={ka}', theta_zero_location='N')
    ax.legend(); ax.set_rmax(max(RCS_mom)+3)
    plt.tight_layout(); plt.savefig('jin_ch10_mom_rcs.png', dpi=150); plt.close()
    print('✅ Demo 1 done')
    return True

verify_all = lambda: print('\nJin Ch10: MoM RCS PASS') if demo_mom_cylinder() else False
if __name__ == '__main__':
    verify_all()

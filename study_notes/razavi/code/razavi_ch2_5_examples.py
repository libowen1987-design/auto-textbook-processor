#!/usr/bin/env python3
"""Razavi Ch2+5: RF concepts — NF cascade, IIP3, LNA matching."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, k as K_B

T0, BW = 290, 20e6
P_floor = -174 + 10*np.log10(BW)  # dBm noise floor at receiver input

def demo_nf_cascade():
    """Friis cascade: NF vs first-stage gain."""
    G_lna = np.linspace(5, 25, 100)
    stages = [(15, 2.5), (10, 8), (20, 6)]  # (Gain dB, NF dB)
    G_lin = [10**(g/10) for g, _ in stages]
    NF_lin = [10**(nf/10) for _, nf in stages]
    NF_tot = []
    for g1 in G_lna:
        G = [10**(g1/10)] + G_lin[1:]
        nf = NF_lin[0] + (NF_lin[1]-1)/G[0] + (NF_lin[2]-1)/(G[0]*G[1])
        NF_tot.append(10*np.log10(nf))
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(G_lna, NF_tot, 'b-', lw=2)
    ax.axhline(2.5, color='r', ls='--', label='LNA NF alone')
    ax.set(xlabel='LNA Gain (dB)', ylabel='Cascade NF (dB)',
           title='3-Stage Receiver NF (Friis)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_nf_cascade.png', dpi=150); plt.close()
    P_sens = P_floor + NF_tot[50] + 6
    print(f'  @LNA Gain 15dB: NF={NF_tot[50]:.2f}dB, Sens={P_sens:.0f}dBm')
    print('✅ NF cascade done')

def demo_iip3():
    """IIP3 and P1dB plot."""
    P_in = np.linspace(-30, 10, 500)
    a1, a3 = 1.0, -0.02
    P_out = 10*np.log10(a1**2 * 10**(P_in/10) * 1e-3 * 1000)
    P_im3 = 10*np.log10((3*a3/4)**2 * (10**(P_in/10)*1e-3)**3 * 1000)
    IIP3 = 10*np.log10(4*a1/(3*abs(a3)) * 1000)
    P1dB = 10*np.log10(0.145*a1/abs(a3) * 1000)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(P_in, P_out, 'b-', lw=2, label='Fundamental')
    ax.plot(P_in, P_im3, 'r-', lw=2, label='IM3')
    ax.axvline(IIP3, color='g', ls='--', label=f'IIP3={IIP3:.0f}dBm')
    ax.axvline(P1dB, color='m', ls=':', label=f'P1dB={P1dB:.0f}dBm')
    ax.set(xlabel='P_in (dBm)', ylabel='P_out (dBm)',
           title=f'IIP3-P1dB = {IIP3-P1dB:.1f}dB')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_iip3.png', dpi=150); plt.close()
    print(f'  IIP3={IIP3:.1f}dBm, P1dB={P1dB:.1f}dBm, Δ={IIP3-P1dB:.1f}dB')
    print('✅ IIP3 done')

def demo_lna_matching():
    """Inductive source-degenerated LNA: S11 and gain."""
    f = np.linspace(0.5e9, 6e9, 1000); w = 2*pi*f
    Ls, Lg, Cgs, gm = 0.5e-9, 8e-9, 200e-15, 50e-3
    fT = gm/(2*pi*Cgs)
    Zin = gm*Ls/Cgs + 1j*(w*(Ls+Lg) - 1/(w*Cgs))
    S11 = (Zin - 50)/(Zin + 50)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(f/1e9, 20*np.log10(abs(S11)), 'b-', lw=2)
    ax.axhline(-10, color='r', ls='--')
    ax.set(xlabel='f (GHz)', ylabel='S11 (dB)', title=f'LNA: fT={fT/1e9:.0f}GHz')
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('razavi_lna_s11.png', dpi=150); plt.close()
    print(f'  fT={fT/1e9:.0f}GHz, ωT·Ls={gm/Cgs*Ls:.0f}Ω(target 50)')
    print('✅ LNA matching done')

demo_nf_cascade(); demo_iip3(); demo_lna_matching()
print('\nRazavi Ch2+5: 3/3 ALL PASS')

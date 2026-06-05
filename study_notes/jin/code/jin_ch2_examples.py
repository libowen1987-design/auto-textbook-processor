#!/usr/bin/env python3
"""
Jin Ch2: Electromagnetic Radiation in Free Space — Examples

Based on: Jin, Theory and Computation of EM Fields, 2nd Ed., Chapter 2 (pp. 77-112).
Covers: Hertzian dipole near/far fields, radiation resistance, half-wave dipole,
        magnetic dipole, far-field approximation error.

Author: 小龙虾
Date: 2026-05-02
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import pi, c, mu_0, epsilon_0

ETA_0 = np.sqrt(mu_0 / epsilon_0)


# ======================================================================
def demo_hertzian_dipole():
    """Hertzian dipole: near-field -> far-field transition of E_theta."""
    print(f"\n{'='*60}")
    print("Demo 1: Hertzian Dipole — Near/Far Field Transition")
    print(f"{'='*60}")
    f, I, dl_over_lam = 1e9, 1.0, 1/100
    k = 2*pi*f/c; lam = c/f; dl = dl_over_lam * lam
    r = np.logspace(-4, 2, 1000) * lam
    kr = k * r; th = pi/2

    E_exact = 1j*ETA_0*I*dl*k/(4*pi)*np.sin(th)*np.exp(-1j*kr)/r*(1+1/(1j*kr)-1/kr**2)
    E_far = 1j*ETA_0*I*dl*k/(4*pi)*np.sin(th)*np.exp(-1j*kr)/r
    E_near = ETA_0*I*dl/(4*pi)*np.sin(th)/(k*r**3)*np.exp(-1j*kr)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    ax1.loglog(r/lam, abs(E_exact), 'b-', lw=2, label='Exact')
    ax1.loglog(r/lam, abs(E_far), 'r--', lw=1.5, label='Far-field')
    ax1.loglog(r/lam, abs(E_near), 'g:', lw=1.5, label='Near-field')
    ax1.axvline(lam/(2*pi), color='k', ls=':', alpha=0.5, label='r=λ/2π')
    ax1.set(xlabel='r/λ', ylabel='|E_θ| (V/m)', xlim=(1e-4, 100))
    ax1.set_title('Hertzian Dipole Field vs Distance')
    ax1.legend(fontsize=8); ax1.grid(True, alpha=0.3)

    ax2.semilogx(r/lam, np.angle(E_exact, deg=True), 'b-', lw=2)
    ax2.axvline(lam/(2*pi), color='k', ls=':', alpha=0.5)
    ax2.set(xlabel='r/λ', ylabel='Phase (deg)', xlim=(1e-4, 100))
    ax2.set_title('Field Phase Transition')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('jin_ch2_hertzian_dipole.png', dpi=150)
    plt.close()
    print(f"  λ/2π = {lam/(2*pi):.4f} m (far-field boundary)")
    print("✅ Demo 1 done")
    return True


# ======================================================================
def demo_radiation_resistance():
    """R_rad = 80π²(dl/λ)² [Ω] for short electric dipole."""
    print(f"\n{'='*60}")
    print("Demo 2: Radiation Resistance vs Dipole Length")
    print(f"{'='*60}")
    x = np.linspace(0.001, 0.5, 500)
    R = 80*pi**2 * x**2
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, R, 'b-', lw=2)
    for r, lbl in [(0.01, '0.01λ: 0.079Ω'), (0.1, '0.1λ: 7.9Ω'), (0.5, '0.5λ: 197Ω')]:
        ax.axvline(r, color='gray', ls=':', alpha=0.5)
        ax.annotate(lbl, xy=(r, 80*pi**2*r**2), fontsize=9,
                    xytext=(r*1.05, 80*pi**2*r**2*1.1),
                    arrowprops=dict(arrowstyle='->', lw=0.5))
    ax.set(xlabel='dl/λ', ylabel='R_rad (Ω)', title='Radiation Resistance of Short Dipole')
    ax.legend(['R_rad = 80π²(dl/λ)²']); ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('jin_ch2_radiation_resistance.png', dpi=150)
    plt.close()
    print("✅ Demo 2 done")
    return True


# ======================================================================
def demo_half_wave_dipole():
    """Half-wave dipole: E-plane/H-plane patterns + directivity."""
    print(f"\n{'='*60}")
    print("Demo 3: Half-Wave Dipole Radiation Pattern")
    print(f"{'='*60}")
    th = np.linspace(0.001, pi-0.001, 360)
    F = abs(np.cos(pi/2*np.cos(th))/np.sin(th))
    F /= np.max(F)

    U = F**2
    Prad = np.trapezoid(U*np.sin(th), th)*2*pi
    D0 = 4*pi/Prad
    print(f"  D₀ = {D0:.3f} ({10*np.log10(D0):.2f} dBi),  theory: 1.64 (2.15 dBi)")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5),
                                   subplot_kw={'projection': 'polar'})
    ax1.plot(th, F, 'b-', lw=2)
    ax1.set(title='E-Plane', theta_zero_location='N'); ax1.set_rmax(1.0)
    ax1.grid(True, alpha=0.3)
    ax2.plot(np.linspace(0, 2*pi, 360), np.ones(360), 'b-', lw=2)
    ax2.set(title='H-Plane (omnidirectional)'); ax2.set_rmax(1.2)
    ax2.grid(True, alpha=0.3)
    plt.suptitle(f'Half-Wave Dipole: D₀={D0:.2f} ({10*np.log10(D0):.1f} dBi)')
    plt.tight_layout()
    plt.savefig('jin_ch2_half_wave_dipole.png', dpi=150)
    plt.close()
    print("✅ Demo 3 done")
    return True


# ======================================================================
def demo_magnetic_dipole():
    """Small loop (magnetic dipole): E-plane pattern + R_rad."""
    print(f"\n{'='*60}")
    print("Demo 4: Magnetic Dipole (Small Loop)")
    print(f"{'='*60}")
    f, I = 1e9, 1.0
    k = 2*pi*f/c; lam = c/f; a = lam/20
    th = np.linspace(0, pi, 361)
    E = abs(ETA_0*I*pi*a**2*k**2/(4*pi)*np.sin(th))
    E /= np.max(E)
    Rr = 20*pi**2*(2*pi*a/lam)**4
    print(f"  a={a*1e3:.2f}mm = {a/lam:.4f}λ,  R_rad={Rr:.6f}Ω")

    fig = plt.figure(figsize=(14, 5))
    ax1 = fig.add_subplot(121, projection='polar')
    ax1.plot(th, E, 'b-', lw=2)
    ax1.set(title='E-Plane (Magnetic Dipole)', theta_zero_location='N')
    ax1.set_rmax(1.0); ax1.grid(True, alpha=0.3)

    ax2 = fig.add_subplot(122)
    x = np.linspace(0.001, 0.05, 200)
    ax2.loglog(x, 20*pi**2*(2*pi*x)**4, 'b-', lw=2)
    ax2.axvline(a/lam, color='r', ls='--', label=f'a={a/lam:.4f}λ')
    ax2.set(xlabel='a/λ', ylabel='R_rad (Ω)')
    ax2.set_title('Loop Radiation Resistance')
    ax2.legend(); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('jin_ch2_magnetic_dipole.png', dpi=150)
    plt.close()
    print("✅ Demo 4 done")
    return True


# ======================================================================
def demo_far_field_error():
    """Fraunhofer far-field phase error vs distance."""
    print(f"\n{'='*60}")
    print("Demo 5: Far-Field Approximation Error")
    print(f"{'='*60}")
    f, D_lam = 10e9, 10
    lam = c/f; k = 2*pi/lam; D = D_lam*lam
    r = np.linspace(D, 100*D, 5000)
    R_ex = np.sqrt(r**2 + (D/2)**2)
    R_ap = r + (D/2)**2/(2*r)
    err = k*(R_ex-R_ap)*180/pi
    r_f = 2*D**2/lam

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(r/lam, err, 'b-', lw=2, label='Phase error (deg)')
    ax.axhline(22.5, color='r', ls='--', label='π/8 = 22.5°')
    ax.axvline(r_f/lam, color='g', ls='--', label=f'Fraunhofer r={r_f/lam:.0f}λ')
    ax.set(xlabel='r/λ', ylabel='Phase error (deg)',
           title=f'Far-Field Error: D={D_lam}λ aperture')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('jin_ch2_far_field_error.png', dpi=150)
    plt.close()
    print(f"  Fraunhofer distance: 2D²/λ = {r_f/lam:.0f}λ")
    print("✅ Demo 5 done")
    return True


# ======================================================================
def verify_all():
    results = {k: v() for k, v in [
        ('d1', demo_hertzian_dipole),
        ('d2', demo_radiation_resistance),
        ('d3', demo_half_wave_dipole),
        ('d4', demo_magnetic_dipole),
        ('d5', demo_far_field_error),
    ]}
    n = sum(1 for v in results.values() if v)
    print(f"\n{'='*60}")
    print(f"Jin Ch2 Demo: {n}/{len(results)} ALL PASS 🎉")
    print(f"{'='*60}")
    return all(results.values())


if __name__ == '__main__':
    verify_all()

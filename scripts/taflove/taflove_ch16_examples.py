#!/usr/bin/env python3
"""
taflove_ch16_examples.py — Photonics FDTD Modeling

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch16
Topics:
  Ex16.1: Optical waveguide mode profile (Si strip waveguide)
  Ex16.2: Photonic crystal band diagram (2D square lattice)
  Ex16.3: Micro-ring resonator transmission and Q extraction
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.special import jv
from scipy.signal import find_peaks
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex16_1_waveguide_mode():
    """Si waveguide: mode profile and dispersion (effective index method)."""
    w = 0.5e-6; h = 0.22e-6; n_Si = 3.48; n_SiO2 = 1.44
    lam = np.linspace(1.3, 1.7, 100) * 1e-6
    n_eff = np.zeros(len(lam))

    for i, lam_i in enumerate(lam):
        k0 = 2 * pi / lam_i
        V = k0 * w / 2 * np.sqrt(n_Si**2 - n_SiO2**2)
        b = 1 - np.exp(-2 * V) / (1 + 2 * V)
        n_x = np.sqrt(n_SiO2**2 + b * (n_Si**2 - n_SiO2**2))
        V_y = k0 * h / 2 * np.sqrt(n_x**2 - n_SiO2**2)
        b_y = 1 - np.exp(-2 * V_y) / (1 + 2 * V_y)
        n_y = np.sqrt(n_SiO2**2 + b_y * (n_x**2 - n_SiO2**2))
        n_eff[i] = n_y

    n_g = n_eff - lam * np.gradient(n_eff, lam)
    lam0 = 1.55e-6; k0 = 2 * pi / lam0
    idx0 = np.argmin(np.abs(lam - lam0))
    n_eff_0 = n_eff[idx0]

    nx, ny = 100, 80
    x = np.linspace(-1.5e-6, 1.5e-6, nx)
    y = np.linspace(-1.5e-6, 1.5e-6, ny)
    X, Y = np.meshgrid(x, y)
    kappa = k0 * np.sqrt(n_Si**2 - n_eff_0**2)
    gamma = k0 * np.sqrt(n_eff_0**2 - n_SiO2**2)

    fx = np.where(np.abs(X) < w/2, np.cos(kappa * X), np.exp(-gamma * (np.abs(X) - w/2)))
    fy = np.where(np.abs(Y) < h/2, np.cos(kappa * Y), np.exp(-gamma * (np.abs(Y) - h/2)))
    mode = fx * fy; mode = mode / np.max(np.abs(mode))

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes[0, 0].plot(lam * 1e9, n_eff, 'b-', lw=2.5)
    axes[0, 0].axhline(n_Si, color='gray', ls='--', alpha=0.4)
    axes[0, 0].axhline(n_SiO2, color='gray', ls=':', alpha=0.4)
    axes[0, 0].set_xlabel('Wavelength (nm)'); axes[0, 0].set_ylabel('n_eff')
    axes[0, 0].set_title('Effective Index vs Wavelength')
    axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(lam * 1e9, n_g, 'r-', lw=2.5)
    axes[0, 1].set_xlabel('Wavelength (nm)'); axes[0, 1].set_ylabel('n_g')
    axes[0, 1].set_title('Group Index'); axes[0, 1].grid(True, alpha=0.3)

    im = axes[1, 0].pcolormesh(X * 1e9, Y * 1e9, mode, shading='gouraud', cmap='hot')
    plt.colorbar(im, ax=axes[1, 0])
    axes[1, 0].axhline(-h/2*1e9, color='w', ls='--', lw=1, alpha=0.5)
    axes[1, 0].axhline(h/2*1e9, color='w', ls='--', lw=1, alpha=0.5)
    axes[1, 0].axvline(-w/2*1e9, color='w', ls='--', lw=1, alpha=0.5)
    axes[1, 0].axvline(w/2*1e9, color='w', ls='--', lw=1, alpha=0.5)
    axes[1, 0].set_xlabel('x (nm)'); axes[1, 0].set_ylabel('y (nm)')
    axes[1, 0].set_title(f'Mode Profile at {lam0*1e9:.0f} nm')

    mid = ny // 2
    axes[1, 1].plot(x * 1e9, mode[mid, :], 'b-', lw=2)
    axes[1, 1].axvline(-w/2*1e9, color='gray', ls='--', alpha=0.5)
    axes[1, 1].axvline(w/2*1e9, color='gray', ls='--', alpha=0.5)
    axes[1, 1].set_xlabel('x (nm)'); axes[1, 1].set_ylabel('|E|')
    axes[1, 1].grid(True, alpha=0.3); axes[1, 1].set_xlim(-1000, 1000)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch16_ex1_waveguide_mode.png", dpi=150)
    plt.close()
    print("[Ch16 Ex1] Waveguide mode plotted.")


def ex16_2_photonic_crystal():
    """2D PhC: band diagram for square lattice of rods (PWE method)."""
    a = 550e-9; r = 0.2 * a; eps_r = 3.48**2; eps_b = 1.0
    ff = pi * r**2 / a**2; eta_0 = 1.0 / (ff * eps_r + (1 - ff) * eps_b)

    nk = 200
    kx = np.concatenate([np.linspace(0, pi/a, nk), np.linspace(pi/a, pi/a, nk), np.linspace(pi/a, 0, nk)])
    ky = np.concatenate([np.zeros(nk), np.linspace(0, pi/a, nk), np.linspace(pi/a, 0, nk)])

    G = np.array([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1],
                   [1, 1], [1, -1], [-1, 1], [-1, -1]]) * 2*pi/a

    bands = []
    for i in range(len(kx)):
        k_vec = np.array([kx[i], ky[i]])
        M = np.zeros((len(G), len(G)), dtype=complex)
        for mu in range(len(G)):
            for nu in range(len(G)):
                G_diff = G[mu] - G[nu]; gdn = np.linalg.norm(G_diff)
                eta = eta_0 if gdn < 1e-10 else 2*ff*(1/eps_r - 1/eps_b)*jv(1, gdn*r)/(gdn*r)
                M[mu, nu] = -np.linalg.norm(k_vec + G[mu]) * np.linalg.norm(k_vec + G[nu]) * eta
        eig = np.sort(np.maximum(np.linalg.eigvalsh(M), 0))
        bands.append(np.sqrt(eig[:5]))
    bands = np.array(bands) / (2 * pi / a)

    fig, ax = plt.subplots(figsize=(8, 6))
    for b in range(5):
        ax.plot(bands[:, b], lw=2, label=f'Band {b+1}')
    ax.set_xticks([0, nk, 2*nk, 3*nk-1])
    ax.set_xticklabels(['Gamma', 'X', 'M', 'Gamma'])
    ax.set_ylabel('Normalized freq a/lambda')
    ax.set_title('2D PhC: TM Band Diagram (Si rods, square lattice)')
    ax.legend(); ax.grid(True, alpha=0.3); ax.set_ylim(0, 1.5)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch16_ex2_photonic_crystal.png", dpi=150)
    plt.close()
    print("[Ch16 Ex2] Photonic crystal band diagram plotted.")


def ex16_3_ring_resonator():
    """Ring resonator: transmission and Q extraction."""
    lam = np.linspace(1.5, 1.6, 2000) * 1e-6
    R = 10e-6; n_eff = 2.5; kappa = 0.15; tau = np.sqrt(1 - kappa**2)
    L_rt = 2 * pi * R; phi = 2 * pi * n_eff * L_rt / lam
    alpha = 10**(-3 * L_rt / 0.01 / 10)
    through = (tau - alpha * np.exp(-1j * phi)) / (1 - tau * alpha * np.exp(-1j * phi))
    T = np.abs(through)**2

    troughs = find_peaks(-T, height=0.3)
    if len(troughs[0]) > 0:
        ir = troughs[0][0]
        lam_r = lam[ir]; T_r = T[ir]
        half = (1 + T_r) / 2
        left = np.where(T[:ir] < half)[0]; right = np.where(T[ir:] < half)[0]
        if len(left) > 0 and len(right) > 0:
            dlam = lam[ir + right[0]] - lam[left[-1]]
            Q = lam_r / dlam
        else:
            Q = 0
    else:
        ir = np.argmin(T); lam_r = lam[ir]; Q = 0

    FSR = lam_r**2 / (n_eff * L_rt)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 7))
    ax1.plot(lam*1e9, T, 'b-', lw=1.5)
    ax1.set_xlabel('Wavelength (nm)'); ax1.set_ylabel('Transmission')
    ax1.set_title(f'Ring: R={R*1e6:.0f} um, kappa={kappa}')
    ax1.grid(True, alpha=0.3)

    zoom = 5
    mask = (lam*1e9 > lam_r*1e9 - zoom) & (lam*1e9 < lam_r*1e9 + zoom)
    ax2.plot(lam[mask]*1e9, T[mask], 'b-', lw=2.5)
    ax2.axvline(lam_r*1e9, color='r', ls='--', alpha=0.6)
    if Q > 0:
        ax2.text(0.6, 0.5, f'lambda0={lam_r*1e9:.3f} nm\nQ={Q:.0f}\nFSR={FSR*1e9:.2f} nm',
                 transform=ax2.transAxes, fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    ax2.set_xlabel('Wavelength (nm)'); ax2.set_ylabel('Transmission')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch16_ex3_ring_resonator.png", dpi=150)
    plt.close()
    print("[Ch16 Ex3] Ring resonator plotted.")


if __name__ == "__main__":
    ex16_1_waveguide_mode()
    ex16_2_photonic_crystal()
    ex16_3_ring_resonator()
    print("\nAll Ch16 examples complete.")

#!/usr/bin/env python3
"""
taflove_ch17_examples.py — Pseudospectral Time-Domain (PSTD) Method

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch17
Topics:
  Ex17.1: Fourier PSTD — plane wave at lambda/2 sampling
  Ex17.2: PSTD derivative accuracy vs FDTD
  Ex17.3: Chebyshev PSTD — non-periodic boundary test
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.fft import fft, ifft, fftfreq
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex17_1_pstd_wave():
    """Fourier PSTD: plane wave propagation with lambda/2 sampling."""
    Nx = 100; Lx = 1.0; dx = Lx / Nx
    lam = 2 * dx; k0 = 2 * pi / lam
    x = np.linspace(0, Lx - dx, Nx)
    f = np.sin(k0 * x)

    f_fft = fft(f)
    k_vec = 2 * pi * fftfreq(Nx, d=dx)
    df_pstd = ifft(1j * k_vec * f_fft).real

    df_analytical = k0 * np.cos(k0 * x)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.plot(x, f, 'bs', ms=3, label='PSTD (lambda = 2*dx)')
    ax1.set_xlabel('x'); ax1.set_ylabel('f(x)')
    ax1.set_title('PSTD Field Sampling at Nyquist Limit')
    ax1.legend(); ax1.grid(True, alpha=0.3)

    ax2.plot(x, df_pstd, 'b-', lw=2, label='PSTD derivative (FFT)')
    ax2.plot(x, df_analytical, 'k--', lw=1.5, alpha=0.7, label='Analytical df/dx')
    err = np.max(np.abs(df_pstd - df_analytical))
    ax2.set_xlabel('x'); ax2.set_ylabel('df/dx')
    ax2.set_title(f'PSTD Derivative (max error = {err:.2e})')
    ax2.legend(); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch17_ex1_pstd_wave.png", dpi=150)
    plt.close()
    print(f"[Ch17 Ex1] PSTD wave done. Error={err:.2e}")


def ex17_2_pstd_accuracy():
    """PSTD derivative accuracy vs points per wavelength."""
    ppw_range = np.arange(2, 31, dtype=float)
    err_pstd = np.zeros(len(ppw_range))
    err_fdtd = np.zeros(len(ppw_range))

    for idx, ppw in enumerate(ppw_range):
        Nx = 200; Lx = ppw; dx = Lx / Nx
        lam = 1.0; k0 = 2 * pi / lam
        x = np.linspace(0, Lx, Nx, endpoint=False)
        f = np.sin(k0 * x)

        f_fft = fft(f); k_vec = 2 * pi * fftfreq(Nx, d=dx)
        df_pstd = ifft(1j * k_vec * f_fft).real
        df_fdtd = np.zeros_like(f)
        df_fdtd[1:-1] = (f[2:] - f[:-2]) / (2 * dx)
        df_analytical = k0 * np.cos(k0 * x)

        err_pstd[idx] = np.max(np.abs(df_pstd - df_analytical))
        err_fdtd[idx] = np.max(np.abs(df_fdtd[1:-1] - df_analytical[1:-1]))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.loglog(ppw_range, err_pstd, 'bs-', lw=2, ms=4, label='PSTD (spectral)')
    ax.loglog(ppw_range, err_fdtd, 'ro-', lw=2, ms=4, label='FDTD (2nd order)')
    ax.loglog(ppw_range, 1e2 * ppw_range**(-2), 'r--', lw=1, alpha=0.5, label='O(dx^2)')
    ax.set_xlabel('Points per wavelength')
    ax.set_ylabel('Max derivative error')
    ax.set_title('PSTD vs FDTD Derivative Accuracy')
    ax.legend(); ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(2, 30)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch17_ex2_pstd_accuracy.png", dpi=150)
    plt.close()
    print("[Ch17 Ex2] PSTD accuracy plotted.")


def ex17_3_chebyshev_pstd():
    """Chebyshev PSTD derivative for non-periodic function."""
    N = 50
    i_vals = np.arange(N + 1)
    x_cl = -np.cos(pi * i_vals / N)
    f = np.exp(-10 * x_cl**2)
    df_analytical = -20 * x_cl * np.exp(-10 * x_cl**2)

    D = np.zeros((N + 1, N + 1))
    c = np.ones(N + 1); c[0] = 2; c[N] = 2
    for i in range(N + 1):
        for j in range(N + 1):
            if i != j:
                D[i, j] = c[i] / c[j] * (-1)**(i + j) / (x_cl[i] - x_cl[j])
        D[i, i] = -np.sum(D[i, :])
    df_cheb = D @ f

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(x_cl, f, 'ko', ms=4, label='f(x)');
    ax1.plot(x_cl, df_analytical, 'k-', lw=2, label='Analytical df/dx')
    ax1.plot(x_cl, df_cheb, 'bo-', lw=1.5, ms=2, label='Chebyshev PSTD')
    ax1.set_xlabel('x'); ax1.set_title('Chebyshev PSTD Derivative')
    ax1.legend(); ax1.grid(True, alpha=0.3)

    ax2.semilogy(x_cl, np.abs(df_cheb - df_analytical) + 1e-16, 'bo-', lw=1.5, ms=3)
    ax2.set_xlabel('x'); ax2.set_ylabel('Error')
    ax2.set_title('Derivative Error'); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch17_ex3_chebyshev_pstd.png", dpi=150)
    plt.close()
    print("[Ch17 Ex3] Chebyshev PSTD plotted.")


if __name__ == "__main__":
    ex17_1_pstd_wave()
    ex17_2_pstd_accuracy()
    ex17_3_chebyshev_pstd()
    print("\nAll Ch17 examples complete.")

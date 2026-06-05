#!/usr/bin/env python3
"""
Guo Shuohong "Electrodynamics" Ch7 — Charged Particles & EM Fields
===================================================================

Final Chapter! Closing the loop.

Demos:
1. Lienard-Wiechert potentials — uniform motion + accelerated radiation
2. Radiation damping — damped harmonic oscillator energy decay & linewidth
3. Thomson scattering & resonant scattering cross-section

Dependencies: numpy, matplotlib
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import os

# -------------------------------------------------------------------
# Global constants
# -------------------------------------------------------------------
c = 299_792_458.0           # speed of light [m/s]
eps0 = 8.854187817e-12      # vacuum permittivity [F/m]
e = 1.602176634e-19         # elementary charge [C]
m_e = 9.10938356e-31        # electron mass [kg]
r_e = e**2 / (4.0 * np.pi * eps0 * m_e * c**2)  # classical electron radius

plt.rcParams.update({
    'figure.dpi': 150,
    'font.size': 10,
    'axes.grid': True,
    'grid.alpha': 0.3,
})

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# =====================================================================
# Demo 1: Lienard-Wiechert potentials & fields
# =====================================================================
def demo1_lienard_wiechert():
    """
    1a) Field lines of uniformly moving charge (relativistic contraction)
    1b) Radiation pattern of an accelerated charge
    1c) Lienard-Wiechert potential angular dependence
    """
    print("=" * 60)
    print("Demo 1: Lienard-Wiechert potentials and radiation fields")
    print("=" * 60)

    # ---- 1a: Field lines of a uniformly moving charge ----
    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5),
                             subplot_kw={'aspect': 'equal'})

    beta_vals = [0.0, 0.6, 0.9]
    for idx, beta in enumerate(beta_vals):
        ax = axes[idx]
        gamma = 1.0 / np.sqrt(1.0 - beta**2)

        npts = 50
        x = np.linspace(-4, 4, npts)
        y = np.linspace(-4, 4, npts)
        X, Y = np.meshgrid(x, y)
        R = np.sqrt(X**2 + Y**2)

        nx = X / (R + 1e-15)
        ny = Y / (R + 1e-15)
        n_dot_beta = nx * beta

        # E = (n - beta) / [gamma^2 (1 - n*beta)^3 R^2]  (velocity field term)
        denom = gamma**2 * (1.0 - n_dot_beta)**3
        Ex = (nx - beta) / (denom * R**2 + 1e-30)
        Ey = ny / (denom * R**2 + 1e-30)

        E_mag = np.sqrt(Ex**2 + Ey**2)
        log_E = np.log10(E_mag + 1e-20)

        mask = R < 0.3
        Ex[mask] = np.nan
        Ey[mask] = np.nan
        log_E[mask] = np.nan

        ax.streamplot(X, Y, Ex, Ey, color=log_E, cmap='plasma',
                      density=1.2, linewidth=0.8, arrowsize=0.6)
        ax.plot(0, 0, 'o', color='red', markersize=6, zorder=5)
        ax.set_xlim(-4, 4)
        ax.set_ylim(-4, 4)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title(f'beta=v/c={beta}')
        ax.grid(True, alpha=0.2)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo1_wire_field.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 1b: Accelerated charge radiation pattern ----
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 200)
    THETA, PHI = np.meshgrid(theta, phi)

    n_x = np.sin(THETA) * np.cos(PHI)
    n_y = np.sin(THETA) * np.sin(PHI)
    n_z = np.cos(THETA)

    # n x (n x x_hat), acceleration along x
    cross_x = 1.0 - n_x**2
    cross_y = -n_x * n_y
    cross_z = -n_x * n_z

    pattern = (cross_x**2 + cross_y**2 + cross_z**2)
    pattern = pattern / np.max(pattern)

    ax = axes[0]
    th1d = np.linspace(0, np.pi, 200)
    p1d = 1.0 - np.sin(th1d)**2  # cos^2(theta), phi=0 section
    ax.plot(th1d, p1d, 'b-', lw=2)
    ax.fill(th1d, p1d, alpha=0.2, color='steelblue')
    ax.set_title('accelerated charge (phi=0)')
    ax.set_xlabel('theta [rad]')
    ax.set_ylabel('normalized intensity')
    ax.grid(True, alpha=0.3)

    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    Xs = pattern * np.sin(THETA) * np.cos(PHI)
    Ys = pattern * np.sin(THETA) * np.sin(PHI)
    Zs = pattern * np.cos(THETA)
    ax2.plot_surface(Xs, Ys, Zs, facecolors=cm.viridis(pattern),
                     rstride=1, cstride=1, alpha=0.85, linewidth=0)
    ax2.set_title('radiation pattern (3D)')
    ax2.set_xlabel('x'); ax2.set_ylabel('y'); ax2.set_zlabel('z')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo1_fields.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 1c: LW potential vs angle ----
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))

    beta_list = [0.0, 0.3, 0.6, 0.8, 0.9]
    th_deg = np.linspace(0, 180, 200)
    th_rad = np.deg2rad(th_deg)

    for beta in beta_list:
        gamma = 1.0 / np.sqrt(1.0 - beta**2)
        phi_lw = 1.0 / (1.0 - beta * np.cos(th_rad))
        phi_lw = phi_lw / np.max(phi_lw)
        ax.plot(th_deg, phi_lw, lw=1.5,
                label=f'beta={beta}, gamma={gamma:.2f}')

    ax.set_xlabel('theta [deg]')
    ax.set_ylabel('normalized scalar potential')
    ax.set_title('Lienard-Wiechert potential vs angle')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 180)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo1_lienard_wiechert_potential.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    print()

# =====================================================================
# Demo 2: Radiation damping — energy decay & spectral linewidth
# =====================================================================
def demo2_radiation_damping():
    """
    2a) Amplitude decay (analytical: damped harmonic oscillator)
    2b) Energy decay on log scale over several lifetimes
    2c) Lorentzian line profile and linewidth
    """
    print("=" * 60)
    print("Demo 2: Radiation damping — energy decay & spectral linewidth")
    print("=" * 60)

    # Parameters (visible light, lambda = 500 nm)
    lambda0 = 500e-9
    omega0 = 2.0 * np.pi * c / lambda0
    tau0 = (2.0/3.0) * r_e / c             # = e^2/(6 pi eps0 m_e c^3)
    Gamma = omega0**2 * tau0
    T0 = 2.0 * np.pi / omega0               # ~1.67 fs

    print(f"  lambda_0 = {lambda0*1e9:.0f} nm")
    print(f"  omega_0 = {omega0:.3e} rad/s")
    print(f"  tau_0 = {tau0:.3e} s")
    print(f"  Gamma = {Gamma:.3e} s^-1")
    print(f"  1/Gamma = {1/Gamma:.3e} s")
    print(f"  Q = omega_0/Gamma = {omega0/Gamma:.3e}")
    print()

    # ---- 2a: Amplitude decay (first ~20 cycles) ----
    t = np.linspace(0, 30 * T0, 3000)
    x0 = 1.0
    x_damped = x0 * np.exp(-Gamma * t / 2.0) * np.cos(omega0 * t)
    x_undamped = x0 * np.cos(omega0 * t)
    env = x0 * np.exp(-Gamma * t / 2.0)

    fig, ax = plt.subplots(1, 1, figsize=(12, 5))
    ax.plot(t*1e15, x_undamped, '-', color='gray', lw=1, alpha=0.5,
            label='no damping')
    ax.plot(t*1e15, x_damped, '-', color='C0', lw=1.5,
            label='with radiative damping')
    ax.plot(t*1e15, env, ':', color='red', lw=1, alpha=0.7,
            label='envelope exp(-Gamma*t/2)')
    ax.plot(t*1e15, -env, ':', color='red', lw=1, alpha=0.7)
    ax.set_xlabel('time t [fs]')
    ax.set_ylabel('displacement x(t) [a.u.]')
    ax.set_title(f'Radiative damping — oscillator amplitude (lambda_0={lambda0*1e9:.0f}nm)')
    ax.legend(fontsize=8)
    ax.set_xlim(0)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo2_amplitude_decay.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 2b: Energy decay (full lifetime) ----
    t_long = np.linspace(0, 6.0 / Gamma, 500)
    E = np.exp(-Gamma * t_long)  # E/E0 = exp(-Gamma * t)

    fig, ax = plt.subplots(1, 1, figsize=(10, 4))
    ax.semilogy(t_long*1e9, E, 'b-', lw=2)
    ax.semilogy(t_long*1e9, np.exp(-Gamma * t_long), 'r--', lw=1.5,
                label=f'E = E0 exp(-Gamma t), Gamma={Gamma:.2e} s^-1')
    ax.set_xlabel('time t [ns]')
    ax.set_ylabel('normalized energy E/E0')
    ax.set_title('Radiative damping — energy decay')
    ax.legend(fontsize=9)
    ax.set_ylim(1e-4, 2)
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo2_energy_decay.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 2c: Lorentzian line profile ----
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

    # Subplot 1: single Lorentzian
    dw = np.linspace(-5*Gamma, 5*Gamma, 2000)
    I_l = (Gamma / (2.0*np.pi)) / (dw**2 + (Gamma/2.0)**2)
    I_l = I_l / np.max(I_l)

    ax = axes[0]
    ax.plot(dw / Gamma, I_l, 'b-', lw=2)
    ax.axvline(-0.5, color='red', ls='--', lw=1, alpha=0.5)
    ax.axvline(0.5, color='red', ls='--', lw=1, alpha=0.5)
    ax.axhline(0.5, color='red', ls=':', lw=1, alpha=0.5)
    ax.annotate('FWHM = Gamma', xy=(0.8, 0.55), fontsize=10, color='red')
    ax.set_xlabel('(omega - omega0) / Gamma')
    ax.set_ylabel('normalized intensity')
    ax.set_title('Natural linewidth — Lorentz profile')
    ax.set_xlim(-5, 5)
    ax.grid(True, alpha=0.3)

    # Subplot 2: multiple damping ratios
    ax2 = axes[1]
    factors = [1, 3, 10, 30]
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(factors)))
    dw2 = np.linspace(-5*Gamma*30, 5*Gamma*30, 2000)

    for i, f in enumerate(factors):
        Gi = Gamma * f
        I_i = (Gi / (2.0*np.pi)) / (dw2**2 + (Gi/2.0)**2)
        I_i = I_i / np.max(I_i)
        ax2.plot(dw2 / Gamma, I_i, color=colors[i], lw=1.5,
                 label=f'Gamma/Gamma0={f}')

    ax2.set_xlabel('(omega - omega0) / Gamma0')
    ax2.set_ylabel('normalized intensity')
    ax2.set_title(f'Linewidth vs damping (Gamma0={Gamma:.2e} s^-1)')
    ax2.legend(fontsize=8)
    ax2.set_xlim(-30, 30)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo2_spectral_lineshape.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # Summary
    dlam = lambda0**2 * Gamma / (2.0 * np.pi * c)
    print(f"  +-- Summary -------------------------+")
    print(f"  |  r_e = {r_e:.4e} m                    |")
    print(f"  |  tau_0 = {tau0:.3e} s                  |")
    print(f"  |  FWHM d_omega = {Gamma:.3e} rad/s      |")
    print(f"  |  FWHM d_f     = {Gamma/(2*np.pi):.3e} Hz|")
    print(f"  |  FWHM d_lambda= {dlam:.3e} m           |")
    print(f"  |              = {dlam*1e9:.5f} nm       |")
    print(f"  +-------------------------------------+")
    print()

# =====================================================================
# Demo 3: Thomson scattering & resonant cross-sections
# =====================================================================
def demo3_thomson_scattering():
    """
    3a) Thomson differential cross-section angular distribution
    3b) Bound electron scattering cross-section vs frequency
    3c) Resonant cross-section comparison across different lambda_0
    """
    print("=" * 60)
    print("Demo 3: Thomson scattering & resonant cross-sections")
    print("=" * 60)

    sigma_T = (8.0 * np.pi / 3.0) * r_e**2

    print(f"  Thomson cross-section:")
    print(f"    sigma_T = {sigma_T:.4e} m^2")
    print(f"    sigma_T = {sigma_T * 1e28:.4f} barn")
    print(f"    r_e = {r_e:.4e} m")
    print()

    # ---- 3a: Angular distribution ----
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    Theta = np.linspace(0, np.pi, 200)
    # d(sigma)/d(Omega) = (r_e^2 / 2) * (1 + cos^2(Theta))
    dsig = 0.5 * r_e**2 * (1.0 + np.cos(Theta)**2)
    dsig = dsig / np.max(dsig)

    ax = axes[0]
    ax.plot(np.rad2deg(Theta), dsig, 'b-', lw=2)
    ax.fill_between(np.rad2deg(Theta), dsig, alpha=0.2, color='steelblue')
    ax.set_xlabel('scattering angle Theta [deg]')
    ax.set_ylabel('normalized d(sigma)/d(Omega)')
    ax.set_title('Thomson scattering angular distribution (1+cos^2)/2')
    ax.set_xlim(0, 180)
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.plot(Theta, dsig, 'b-', lw=2)
    ax2.fill(Theta, dsig, alpha=0.2, color='steelblue')
    ax2.set_title('Thomson (polar)', fontsize=11, pad=15)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo3_thomson_angular.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 3b: Cross-section vs frequency ----
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Bound electron with resonance at lambda=100nm (UV)
    lambda_res = 100e-9
    omega_res = 2.0 * np.pi * c / lambda_res
    tau0 = (2.0/3.0) * r_e / c
    Gamma_res = omega_res**2 * tau0

    w_rel = np.logspace(-2, 2, 2000)
    w = w_rel * omega_res
    w2 = w**2
    w02 = omega_res**2
    sigma_s = sigma_T * w2**2 / ((w02 - w2)**2 + w2 * Gamma_res**2)
    sigma_s_n = sigma_s / sigma_T

    ax = axes[0]
    ax.loglog(w_rel, sigma_s_n, 'b-', lw=2)
    ax.axvline(1, color='red', ls='--', lw=1, alpha=0.5)
    ax.axhline(1, color='gray', ls=':', lw=0.8, alpha=0.5)

    # Rayleigh regime annotation
    ray_idx = w_rel < 0.1
    ax.loglog(w_rel[ray_idx], w_rel[ray_idx]**4, 'g--', lw=1.5, alpha=0.7,
              label='Rayleigh: ~omega^4')
    ax.axhline(1, color='orange', ls='--', lw=1.5, alpha=0.6,
               label='Thomson limit')

    ax.annotate('Rayleigh\n(omega << omega0)', xy=(0.05, 1e-6), fontsize=8)
    ax.annotate('resonance\n(omega ~ omega0)', xy=(1.0, 1e8), fontsize=8,
                color='red', ha='center')
    ax.annotate('Thomson\n(omega >> omega0)', xy=(10, 2), fontsize=8,
                color='orange')

    ax.set_xlabel('omega / omega0')
    ax.set_ylabel('sigma_s / sigma_T')
    ax.set_title(f'Bound electron scattering cross-section')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3, which='both')

    # 3b(ii): zoom into resonance
    ax2 = axes[1]
    w_fine = np.linspace(0.9999, 1.0001, 2000) * omega_res
    w2f = w_fine**2
    sigma_f = sigma_T * w2f**2 / ((w02 - w2f)**2 + w2f * Gamma_res**2)
    ax2.semilogy((w_fine / omega_res - 1) * 1e6, sigma_f / sigma_T, 'b-', lw=1.5)
    ax2.set_xlabel('(omega - omega0) / omega0 [x 1e-6]')
    ax2.set_ylabel('sigma_s / sigma_T')
    ax2.set_title(f'Resonance peak detail')
    ax2.grid(True, alpha=0.3)
    peak = np.max(sigma_f) / sigma_T
    ax2.annotate(f'peak = {peak:.2e} sigma_T',
                 xy=(0, peak), fontsize=9,
                 arrowprops=dict(arrowstyle='->'))

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo3_scattering_cross_section.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    # ---- 3c: Multiple resonance frequencies ----
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))

    lambda_list = [50e-9, 100e-9, 200e-9, 500e-9]
    colors = plt.cm.turbo(np.linspace(0, 1, len(lambda_list)))

    for i, lr in enumerate(lambda_list):
        wr = 2.0 * np.pi * c / lr
        Gr = wr**2 * tau0
        wr2 = wr**2
        w_arr = np.logspace(-2, 2, 2000) * wr
        w2_arr = w_arr**2
        sig = sigma_T * w2_arr**2 / ((wr2 - w2_arr)**2 + w2_arr * Gr**2)
        ax.loglog(w_arr / wr, sig / sigma_T, color=colors[i], lw=1.5,
                  label=f'lambda_0={lr*1e9:.0f}nm')

    ax.axhline(1, color='gray', ls=':', lw=0.8, alpha=0.5)
    ax.axvline(1, color='gray', ls=':', lw=0.8, alpha=0.5)
    ax.set_xlabel('omega / omega0')
    ax.set_ylabel('sigma_s / sigma_T')
    ax.set_title('Scattering cross-section vs resonance wavelength')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, 'demo3_sigma_comparison.png')
    fig.savefig(path, dpi=150)
    print(f"  -> saved: {path}")
    plt.close(fig)

    print(f"  +-- Thomson cross-section ------------+")
    print(f"  |  sigma_T = {sigma_T:.4e} m^2")
    print(f"  |         = {sigma_T*1e28:.4f} barn")
    print(f"  |  sigma_T/2 @ 90 deg = {sigma_T/2:.4e} m^2")
    print(f"  +-------------------------------------+")
    print()

# =====================================================================
# Main
# =====================================================================
if __name__ == '__main__':
    import time
    t0 = time.time()

    print("=" * 60)
    print("Guo Shuohong 'Electrodynamics' Ch7")
    print("Charged Particles & Electromagnetic Fields")
    print("=" * 60)
    print("FINAL CHAPTER! Closing the loop. [clap]")
    print()

    demo1_lienard_wiechert()
    demo2_radiation_damping()
    demo3_thomson_scattering()

    elapsed = time.time() - t0
    print("=" * 60)
    print(f"All demos completed in {elapsed:.1f}s")
    print(f"Plots saved to: {OUTPUT_DIR}/")
    print(f"  +-- demo1_wire_field.png")
    print(f"  +-- demo1_fields.png")
    print(f"  +-- demo1_lienard_wiechert_potential.png")
    print(f"  +-- demo2_amplitude_decay.png")
    print(f"  +-- demo2_energy_decay.png")
    print(f"  +-- demo2_spectral_lineshape.png")
    print(f"  +-- demo3_thomson_angular.png")
    print(f"  +-- demo3_scattering_cross_section.png")
    print(f"  +-- demo3_sigma_comparison.png")
    print()
    print("  " + "=" * 20 + " GUO SHUOHONG COMPLETE " + "=" * 20)
    print()
    print("  Ch1: EM Laws")
    print("  Ch2: Electrostatics")
    print("  Ch3: Magnetostatics")
    print("  Ch4: Wave Propagation")
    print("  Ch5: Radiation")
    print("  Ch6: Special Relativity")
    print("  Ch7: Charged Particles + Fields   [THIS CHAPTER]")
    print()
    print("  The full journey, from Maxwell to QED's doorstep.")
    print("  " + "=" * 60)

"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter XII: Passage of Fast Particles Through Matter

Key equations (Landau §84-§86):
1. Ionization energy loss (Landau §84):
   -dE/dx = (4π e⁴ z² n / m v²) × [ln(2m v² / I) - v²/c² - δ - 2C²/z²]
   where n = electron density, I = mean excitation energy, z = projectile charge

2. For non-relativistic particle (Landau §84):
   dE/dx ∝ (z²/v²) × [ln(a v³ / z ω₀)]  where a ~ constant, ω₀ ~ atomic frequency

3. Bethe-Bloch formula (relativistic):
   -dE/dx = K × (z²/β²) × (Z/A) × [½ ln(2m_e c² β² γ² W_max / I²) - β² - δ/(2γ²)]

4. Range-energy relation: R(E) = ∫ (dE/dx)^{-1} dE

Landau §84: Ionisation losses by fast particles (non-relativistic case)
Landau §85: Ionisation losses (relativistic case)
Landau §86: Cherenkov radiation
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


def ionization_energy_loss():
    """
    Compute ionization energy loss dE/dx for a charged particle traversing matter
    using the Landau/Bethe-Bloch formula (Landau §84-§85).

    Parameters:
    - z: projectile atomic number (charge in units of e)
    - v: particle velocity
    - Z, A: target material atomic number and mass number
    - n_e: electron density of target
    - I: mean excitation energy (~10 eV × Z)
    """
    # Physical constants
    c = 3e10  # cm/s
    e_charge = 4.803e-10  # esu
    m_e = 9.11e-28  # g
    m_p = 1.67e-24  # g

    # Material: liquid water (similar to biological tissue)
    rho = 1.0  # g/cm³
    Z_target = 7.3  # effective Z for H2O
    A_target = 18.0  # g/mol
    I_water = 75.0  # eV  (mean excitation energy for water)

    n_e = rho * 6.02e23 * Z_target / A_target  # electrons/cm³
    print(f"[landau_ch12] Electron density of water: n_e = {n_e:.2e} cm⁻³")

    # Particle: proton, various energies
    z = 1  # proton charge
    energies_MeV = np.linspace(1, 1000, 300)  # MeV
    gamma = lambda E, M: 1 + E / (M * 931.5)  # M in MeV/c²
    beta = lambda g: np.sqrt(1 - 1/g**2)
    v_cm_s = lambda b: b * c  # cm/s

    def bethe_bloch(E_MeV, z, Z_t, A_t, rho_t, I_eV, relativistic=False):
        """
        Simplified Bethe-Bloch formula for dE/dx in MeV/(g/cm²).
        Returns dE/dx in MeV·cm²/g.
        """
        M_p = 938.0  # MeV/c² for proton
        g = 1 + E_MeV / (M_p * 0.9315) if not relativistic else 1 + E_MeV / M_p
        b = np.sqrt(1 - 1/g**2)
        b2 = b**2
        gamma2 = g**2

        K = 0.307  # MeV·cm²/g  (4π N_A r_e² m_e c² / u)
        w_max = 2 * m_e * b2 * gamma2 / (1 + 2 * g * m_e / M_p + (m_e/M_p)**2) * 1e6  # eV

        # Shell corrections (approximate)
        C = 0.5 * Z_t**0.37 if Z_t > 2 else 0.0

        # Term: ln(2 m_e c² β² γ² w_max / I²) - 2β² - ...
        arg = (2 * 511e3 * b2 * gamma2 * w_max) / (I_eV**2)
        term = np.log(arg) - 2*b2

        dEdx = K * z**2 * Z_t / (A_t * b2) * term  # MeV·cm²/g
        return dEdx * rho_t  # MeV/cm

    dEdx = np.array([bethe_bloch(E, z, Z_target, A_target, rho, I_water)
                     for E in energies_MeV])

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # dE/dx vs energy
    ax = axes[0, 0]
    ax.plot(energies_MeV, -dEdx, 'b-', lw=2)
    ax.set_xlabel('Proton energy (MeV)')
    ax.set_ylabel(r'$|dE/dx|$ (MeV/cm)')
    ax.set_title(r'Landau §84-§85: Proton ionization energy loss in water')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True, alpha=0.3, which='both')

    # Minimum ionizing particle (MIP)
    mip_idx = np.argmin(np.abs(dEdx))
    ax.axhline(np.abs(dEdx[mip_idx]), color='r', ls='--', lw=1.5,
               label=f'MIP ≈ {np.abs(dEdx[mip_idx]):.2f} MeV/cm')
    ax.legend()

    # Stopping power vs β²
    ax2 = axes[0, 1]
    gammas = [1 + E / 938.0 for E in energies_MeV]
    betas = [np.sqrt(1 - 1/g**2) for g in gammas]
    beta2 = np.array(betas)**2
    ax2.plot(beta2, -dEdx, 'g-', lw=2)
    ax2.set_xlabel(r'$\beta^2 = (v/c)^2$')
    ax2.set_ylabel(r'$|dE/dx|$ (MeV/cm)')
    ax2.set_title(r'$dE/dx$ vs $\beta^2$ (Landau §84)')
    ax2.grid(True, alpha=0.3)

    # Range-energy relation: R(E) = ∫ (dE/dx)^{-1} dE
    # Integrate from low energy up
    E_fine = np.linspace(0.5, 500, 200)  # MeV
    dEdx_fine = np.abs(np.array([bethe_bloch(E, z, Z_target, A_target, rho, I_water)
                                  for E in E_fine]))
    # Range in g/cm²
    range_g_cm2 = cumulative_trapezoid(1.0 / (dEdx_fine + 1e-10), E_fine, initial=0)
    range_cm = range_g_cm2 / rho

    ax3 = axes[1, 0]
    ax3.plot(E_fine, range_cm, 'r-', lw=2)
    ax3.set_xlabel('Proton energy (MeV)')
    ax3.set_ylabel('Range R (cm)')
    ax3.set_title(r'Proton range in water: $R(E) = \int (dE/dx)^{-1} dE$')
    ax3.grid(True, alpha=0.3)

    # Bragg curve: dE/dx along the particle track
    ax4 = axes[1, 1]
    R_max = range_cm[-1] * 0.95
    x_track = np.linspace(0, R_max, 300)
    # Interpolate dE/dx at each depth
    from scipy.interpolate import interp1d
    dEdx_interp = interp1d(range_cm[:len(dEdx_fine)], -dEdx_fine,
                           kind='cubic', bounds_error=False, fill_value=0)
    dEdx_at_x = dEdx_interp(x_track)
    ax4.plot(x_track, dEdx_at_x, 'purple', lw=2)
    ax4.set_xlabel('Depth x (cm)')
    ax4.set_ylabel(r'$dE/dx$ (MeV/cm)')
    ax4.set_title('Bragg curve: energy deposition along track')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch12_ionization.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch12] MIP dE/dx = {np.abs(dEdx[mip_idx]):.2f} MeV/cm at E={energies_MeV[mip_idx]:.0f} MeV")
    print(f"[landau_ch12] Proton range at 100 MeV: R ≈ {interp1d(E_fine, range_cm)(100):.1f} cm")
    print(f"[landau_ch12] Plot saved.")


def cherenkov_radiation():
    """
    Cherenkov radiation condition (Landau §86).
    
    Cherenkov radiation is emitted when a charged particle travels
    faster than the phase velocity of light in the medium:
    
    cos θ_c = 1 / (β n(ω))
    
    Threshold: β > 1/n  →  v > c/n
    
    The spectrum (Landau Eq. 86.7):
    d²E/dx dω = (e² ω / c²) [1 - 1/(β² n²(ω))] × [n(ω) + ω dn/dω]
    
    For Cherenkov in water (n ≈ 1.33), threshold β = 1/1.33 ≈ 0.75
    i.e., E_thr = 938 MeV × (γ_thr - 1) = 938 × (1/√(1-0.565) - 1) ≈ 360 MeV
    """
    c = 3e10  # cm/s
    e_charge = 4.803e-10  # esu
    n_water = 1.33

    beta_thr = 1.0 / n_water
    gamma_thr = 1 / np.sqrt(1 - beta_thr**2)
    print(f"[landau_ch12] Cherenkov threshold: β_thr = {beta_thr:.4f}, γ_thr = {gamma_thr:.4f}")

    # Energy for electron and proton
    m_e_MeV = 0.511
    m_p_MeV = 938.0
    E_thr_e = m_e_MeV * (gamma_thr - 1)
    E_thr_p = m_p_MeV * (gamma_thr - 1)
    print(f"[landau_ch12] Cherenkov threshold energy:")
    print(f"[landau_ch12]   Electron: {E_thr_e:.1f} MeV")
    print(f"[landau_ch12]   Proton: {E_thr_p:.1f} MeV")

    # Cherenkov angle vs β
    betas = np.linspace(beta_thr + 0.001, 0.9999, 200)
    theta_c = np.arccos(1.0 / (betas * n_water)) * 180 / np.pi

    # Cherenkov spectrum dN/dλ ∝ 1/λ² × [1 - 1/(β²n²)]
    lambdas = np.linspace(300e-7, 700e-7, 200)  # 300-700 nm
    omega_cher = 2 * np.pi * c / (lambdas * 1e2)  # cm -> nm
    # For simplicity: spectrum ~ 1/λ² × sin²θ_c
    n_lambda = 1.33 * np.ones_like(lambdas)  # approximate constant n
    dN_dlambda = 1.0 / (lambdas * 1e7)**2  # ~1/λ²
    spectrum = dN_dlambda * np.sin(np.radians(theta_c[100]))**2 * np.ones_like(lambdas)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    ax.plot(betas, theta_c, 'b-', lw=2)
    ax.axvline(beta_thr, color='r', ls='--', lw=1.5, label=f'β_thr={beta_thr:.3f}')
    ax.set_xlabel(r'$\beta = v/c$')
    ax.set_ylabel(r'Cherenkov angle $\theta_c$ (degrees)')
    ax.set_title(r'Landau §86: $\cos\theta_c = 1/(\beta n)$, $n_{water}=1.33$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax2 = axes[0, 1]
    ax2.plot(lambdas * 1e7, spectrum / np.max(spectrum), 'purple', lw=2)
    ax2.set_xlabel(r'Wavelength $\lambda$ (nm)')
    ax2.set_ylabel(r'Normalized Cherenkov spectrum')
    ax2.set_title(r'Landau §86: Cherenkov emission spectrum $\propto 1/\lambda^2$')
    ax2.grid(True, alpha=0.3)

    # Energy loss per cm due to Cherenkov radiation
    ax3 = axes[1, 0]
    beta_range = np.linspace(beta_thr + 0.01, 0.999, 200)
    # dE/dx ∝ ω [1 - 1/(β²n²)] × (n + ω dn/dω) integrated over ω
    # Approximate: dE/dx_cher ∝ 1 - 1/(β² n²)
    dEdx_cher = 1 - 1 / (beta_range**2 * n_water**2)
    dEdx_cher = np.maximum(dEdx_cher, 0)
    ax3.plot(beta_range, dEdx_cher * 1e3, 'orange', lw=2)
    ax3.axvline(beta_thr, color='r', ls='--', lw=1.5, label=f'β_thr={beta_thr:.3f}')
    ax3.set_xlabel(r'$\beta = v/c$')
    ax3.set_ylabel(r'Cherenkov $dE/dx$ (arb. units)')
    ax3.set_title(r'Landau §86: Cherenkov energy loss $\propto [1-1/(\beta^2 n^2)]$')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Particle types: electrons and protons
    ax4 = axes[1, 1]
    E_e = np.linspace(E_thr_e + 0.1, 100, 200)
    E_p = np.linspace(E_thr_p + 1, 1000, 200)
    gamma_e = 1 + E_e / m_e_MeV
    gamma_p = 1 + E_p / m_p_MeV
    beta_e = np.sqrt(1 - 1/gamma_e**2)
    beta_p = np.sqrt(1 - 1/gamma_p**2)
    ax4.plot(E_e, beta_e, 'b-', lw=2, label='Electron')
    ax4.plot(E_p, beta_p, 'r-', lw=2, label='Proton')
    ax4.axhline(beta_thr, color='k', ls=':', lw=1, label=f'Cherenkov threshold β={beta_thr:.3f}')
    ax4.axvline(E_thr_e, color='b', ls='--', lw=1, label=f'E_thr_e={E_thr_e:.0f} MeV')
    ax4.axvline(E_thr_p, color='r', ls='--', lw=1, label=f'E_thr_p={E_thr_p:.0f} MeV')
    ax4.set_xlabel('Kinetic energy (MeV)')
    ax4.set_ylabel(r'$\beta = v/c$')
    ax4.set_title('Cherenkov threshold for electron and proton')
    ax4.legend(fontsize=8)
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch12_cherenkov.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch12] Plot saved.")


if __name__ == '__main__':
    ionization_energy_loss()
    cherenkov_radiation()

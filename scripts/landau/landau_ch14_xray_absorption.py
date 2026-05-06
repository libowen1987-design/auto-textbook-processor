"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter XIV: Dispersion and Absorption

Key equations (Landau §97-§100):
1. X-ray diffraction in crystals (Landau §97):
   - Scattering amplitude f(θ) for free electron: f = e²/mω²
   - Structure factor: F_hkl = Σ f_j exp[2πi (h x_j + k y_j + l z_j)/a]
   - Bragg condition: 2 d_hkl sin θ = n λ

2. Dispersion of X-rays near absorption edges (Landau §99):
   ε(ω) = 1 - (4π n e²)/(m ω²) + corrections for bound electrons
   δ = 1 - (n e² λ²) / (2π m c²)  (refractive index decrement)

3. Photoelectric absorption (Landau §100):
   σ_ph ∝ Z⁴ / (ħω)³  (near threshold)
   μ = n σ_ph  (linear absorption coefficient)

4. K-edge: sudden increase in absorption at ω such that ħω = binding energy of K-shell

Landau §97: General theory of X-ray diffraction
Landau §98: Diffraction of X-rays in crystals
Landau §99: Dispersion of X-rays in crystals
Landau §100: Absorption of X-rays
"""

import numpy as np
import matplotlib.pyplot as plt


def bragg_diffraction_and_structure_factor():
    """
    X-ray diffraction: Bragg's law and structure factor (Landau §97-§98).

    Bragg condition: 2 d_hkl sin θ = n λ
    Structure factor: F_hkl = Σ f_j exp[2πi (h x_j + k y_j + l z_j)/a]

    For a simple cubic lattice with one atom at (0,0,0):
    - All reflections (hkl) are allowed
    - Intensity ∝ |F|² ∝ f(θ)²

    For BCC: reflections allowed only if h+k+l = 2n
    For FCC: reflections allowed only if h,k,l all even or all odd
    """
    # Physical constants
    h_planck = 6.626e-34  # J·s
    c_light = 3e8  # m/s
    e_charge = 1.602e-19  # C
    m_e = 9.11e-31  # kg

    # FCC copper lattice
    a_Cu = 3.615e-10  # m (lattice constant)
    lambda_CuKa = 1.54e-10  # m (Cu Kα radiation)

    # Miller indices to test
    hkl_list = [(1,1,1), (2,0,0), (2,2,0), (3,1,1), (2,2,2),
                (3,3,1), (4,0,0), (4,2,2)]

    # d-spacing for cubic: d = a / √(h²+k²+l²)
    d_hkl = np.array([a_Cu / np.sqrt(h**2 + k**2 + l**2) for h, k, l in hkl_list])

    # Bragg angle: sin θ = nλ / (2d)
    theta_bragg = np.arcsin(lambda_CuKa / (2 * d_hkl)) * 180 / np.pi

    # Structure factor for FCC (4 atoms per cell at 0,0,0; ½,½,0; ½,0,½; 0,½,½)
    # F_hkl = f × [1 + exp(πi(h+k)) + exp(πi(h+l)) + exp(πi(k+l))]
    # FCC: all even or all odd → F = 4f; mixed parity → F = 0
    def structure_factor_FCC(h, k, l, f=1.0):
        if (h % 2 == 0 and k % 2 == 0 and l % 2 == 0) or \
           (h % 2 == 1 and k % 2 == 1 and l % 2 == 1):
            return 4.0 * f
        else:
            return 0.0

    f_Cu = 29 * e_charge**2 / (m_e * (2*np.pi*c_light/lambda_CuKa)**2)  # atomic form factor
    F_vals = [structure_factor_FCC(h, k, l, f_Cu) for h, k, l in hkl_list]

    print("[landau_ch14] FCC Cu Bragg reflections (Cu Kα λ=1.54 Å):")
    print(f"{'hkl':>8} {'d (Å)':>8} {'2θ (deg)':>10} {'F':>10}")
    for i, (h, k, l) in enumerate(hkl_list):
        print(f"({h},{k},{l})    {d_hkl[i]*1e10:.4f}    {2*theta_bragg[i]:.2f}    {F_vals[i]:.4e}")

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Bragg's law visualization
    ax = axes[0, 0]
    h_vals = np.arange(1, 10)
    d_vals = a_Cu / np.sqrt(2) / h_vals  # for (h,h,h) family of FCC
    sin_theta = lambda_CuKa / (2 * d_vals)
    valid = sin_theta <= 1
    d_vals = d_vals[valid]
    sin_theta = sin_theta[valid]
    theta_plot = np.arcsin(sin_theta) * 180 / np.pi

    ax.bar(range(len(d_vals)), 2*theta_plot, color='steelblue', alpha=0.7)
    ax.set_xticks(range(len(d_vals)))
    ax.set_xticklabels([rf'$(hhh)$' for h in h_vals[valid]])
    ax.set_xlabel('Reflection family')
    ax.set_ylabel(r'$2\theta$ (degrees)')
    ax.set_title(r'Landau §97: Bragg angles for Cu Kα on FCC Cu')
    ax.grid(True, alpha=0.3)

    # 2. Structure factor
    ax2 = axes[0, 1]
    h_range = np.arange(0, 8)
    k_range = np.arange(0, 8)
    H, K = np.meshgrid(h_range, k_range)
    # All odd or all even → F = 4, else 0 (FCC approximation)
    F_grid = np.where(
        ((H % 2 == 0) & (K % 2 == 0)) | ((H % 2 == 1) & (K % 2 == 1)),
        4, 0
    )
    ax2.imshow(F_grid, cmap='Blues', origin='lower', extent=[0,7,0,7])
    ax2.set_xlabel('h')
    ax2.set_ylabel('k')
    ax2.set_title('FCC structure factor $F_{hk}$ (l=0 plane)')
    plt.colorbar(ax2.images[0], ax=ax2, label='F')

    # 3. Diffraction intensity pattern (Laue simulation)
    ax3 = axes[1, 0]
    theta_2theta = np.linspace(0, 90, 500)
    d_range = lambda_CuKa / (2 * np.sin(theta_2theta * np.pi / 360))
    # Intensity: I ∝ |F|² × (1+cos²2θ)/2 (Lorentz-polarization factor)
    LP_factor = (1 + np.cos(2*theta_2theta*np.pi/180)**2) / 2
    # Structure factor for different reflections
    I_simu = np.zeros_like(theta_2theta)
    for i, d_val in enumerate(d_hkl):
        mask = np.abs(d_range - d_val) < 1e-12
        hkl = hkl_list[i]
        F = structure_factor_FCC(*hkl, f_Cu)
        if F != 0:
            I_simu[mask] = F_vals[i]**2 * LP_factor[mask] * 0.1
    ax3.plot(theta_2theta, I_simu, 'b-', lw=1)
    ax3.set_xlabel(r'$2\theta$ (degrees)')
    ax3.set_ylabel('Diffracted intensity (arb. units)')
    ax3.set_title(r'Landau §98: Simulated FCC Cu powder diffraction pattern')
    ax3.set_xlim(0, 90)
    ax3.grid(True, alpha=0.3)

    # 4. Electron form factor
    ax4 = axes[1, 1]
    sin_theta_lambda = np.linspace(0, 1.5, 200)  # sin(θ)/λ in Å⁻¹
    # Atomic form factor for Cu: f(s) = f0 + Σ a_i exp(-b_i s²)
    # Standard parameters for Cu (approximate)
    a = [0.456, 0.362, 0.226, 0.076]
    b = [0.058, 0.656, 2.414, 9.623]
    f0 = 0.384
    s = sin_theta_lambda
    f_Cu = f0 + sum(ai * np.exp(-bi * s**2) for ai, bi in zip(a, b))

    ax4.plot(sin_theta_lambda, f_Cu, 'r-', lw=2, label='Cu atomic form factor f(s)')
    ax4.axhline(29, color='k', ls='--', lw=1, label='Z=29 (all electrons)')
    ax4.set_xlabel(r'sin$\theta$/$\lambda$ (Å⁻¹)')
    ax4.set_ylabel(r'Atomic form factor $f$ (electrons)')
    ax4.set_title(r'Landau §97: Atomic form factor $f_{Cu}(s)$')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch14_xray_diffraction.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch14] Plot saved.")


def xray_absorption_and_K_edge():
    """
    X-ray absorption and the K-edge discontinuity (Landau §100).

    Photoelectric absorption cross-section near threshold:
    σ_ph ∝ Z⁴ / (ħω)³  (for photon energy just above K-edge)

    K-edge energy: E_K = R_y × (Z-σ)²  (Moseley's law)
    where R_y = 13.6 eV (Rydberg), σ ≈ screening constant ≈ 1 for K-shell

    For copper: Z=29, E_K ≈ (29-1)² × 13.6 ≈ 8976 eV ≈ 9 keV

    The linear absorption coefficient:
    μ = (ρ N_A / A) × σ_ph  (cm⁻¹)
    where ρ = density, N_A = Avogadro, A = atomic mass
    """
    # Physical constants
    hbar = 6.582e-16  # eV·s
    c_light = 2.998e18  # Å/s
    hbar_omega = lambda E_eV: E_eV  # ħω in eV

    # Copper K-edge
    Z_Cu = 29
    E_K_Cu = 13.6 * (Z_Cu - 1)**2  # eV
    print(f"[landau_ch14] Cu K-edge energy: E_K = {E_K_Cu:.0f} eV")

    # Photon energy range (keV)
    E_keV = np.linspace(3, 30, 500)  # keV
    E_eV = E_keV * 1e3

    # Photoelectric cross-section (approximate)
    # σ_ph ∝ Z⁴ / (ħω)³ below K-edge
    # σ_ph jumps by factor ~ (Z-1)⁴/Z⁴ at K-edge
    def sigma_ph(E_eV, Z, E_K):
        """Approximate photoelectric cross-section (barns/atom)."""
        sigma_below = Z**4 / (E_eV/1e3)**3  # normalized
        # Below K-edge
        sigma = np.where(
            E_eV < E_K,
            sigma_below,
            (Z-1)**4 / (E_eV/1e3)**3  # above K-edge (K electrons gone)
        )
        return sigma

    sigma_Cu = sigma_ph(E_eV, Z_Cu, E_K_Cu)
    sigma_Cu_norm = sigma_Cu / np.max(sigma_Cu) * 1e4

    # Linear absorption coefficient for Cu
    rho_Cu = 8.96  # g/cm³
    A_Cu = 63.55  # g/mol
    N_A = 6.022e23
    n_atoms = rho_Cu * N_A / A_Cu  # atoms/cm³
    mu_Cu = n_atoms * sigma_Cu * 1e-24  # cm⁻¹ (1 barn = 1e-24 cm²)
    mu_Cu = np.maximum(mu_Cu, 1e-3)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # 1. Photoelectric cross-section
    ax = axes[0, 0]
    ax.loglog(E_keV, sigma_Cu_norm, 'b-', lw=2)
    ax.axvline(E_K_Cu/1e3, color='r', ls='--', lw=1.5, label=f'Cu K-edge: {E_K_Cu/1e3:.1f} keV')
    ax.set_xlabel('Photon energy (keV)')
    ax.set_ylabel(r'$\sigma_{ph}$ (normalized)')
    ax.set_title(r'Landau §100: Photoelectric cross-section $\sigma_{ph}(E) \propto Z^4/E^3$')
    ax.legend()
    ax.grid(True, alpha=0.3, which='both')

    # 2. Linear absorption coefficient
    ax2 = axes[0, 1]
    ax2.semilogy(E_keV, mu_Cu, 'orange', lw=2)
    ax2.axvline(E_K_Cu/1e3, color='r', ls='--', lw=1.5, label=f'Cu K-edge: {E_K_Cu/1e3:.1f} keV')
    ax2.set_xlabel('Photon energy (keV)')
    ax2.set_ylabel(r'$\mu$ (cm⁻¹)')
    ax2.set_title(r'Landau §100: Linear absorption coefficient $\mu(E)$ for Cu')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 3. Transmission through Cu foil
    ax3 = axes[1, 0]
    thickness_vals = np.array([0.01, 0.05, 0.1, 0.5])  # cm
    E_fine = np.linspace(3, 30, 300)
    mu_fine = n_atoms * sigma_ph(E_fine*1e3, Z_Cu, E_K_Cu) * 1e-24
    mu_fine = np.maximum(mu_fine, 1e-3)

    for d in thickness_vals:
        I_I0 = np.exp(-mu_fine * d)
        ax3.plot(E_fine, I_I0, lw=2, label=f'd={d*1e3:.0f} μm')

    ax3.axvline(E_K_Cu/1e3, color='k', ls=':', lw=1)
    ax3.set_xlabel('Photon energy (keV)')
    ax3.set_ylabel(r'Transmission $I/I_0 = e^{-\mu d}$')
    ax3.set_title(r'Transmission through Cu foil at various thicknesses')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. X-ray refractive index decrement
    ax4 = axes[1, 1]
    lambda_A = 1240 / E_eV  # λ (Å) from photon energy
    # δ = 1 - n = (n_e λ²) / (2π) × classical electron radius
    # For X-rays: n ≈ 1 - δ, δ ≈ 2.7e-6 for Cu at 10 keV
    r_e = 2.818e-13  # cm (classical electron radius)
    n_e_Cu = rho_Cu * N_A / A_Cu * Z_Cu  # electrons/cm³
    delta = n_e_Cu * r_e * (lambda_A*1e-8)**2 / (2 * np.pi)  # dimensionless

    ax4.plot(E_keV, delta * 1e6, 'g-', lw=2)
    ax4.set_xlabel('Photon energy (keV)')
    ax4.set_ylabel(r'$\delta \times 10^6$')
    ax4.set_title(r'Landau §99: Refractive index decrement $\delta = 1-n$ for Cu')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch14_xray_absorption.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch14] δ at 10 keV in Cu: δ ≈ {delta[np.argmin(np.abs(E_keV-10))]*1e6:.2f} × 10⁻⁶")
    print(f"[landau_ch14] Plot saved.")


def reflection_dispersion_regimes():
    """
    Reflectivity across different spectral regimes: X-ray, UV, visible, IR (Landau §64, §99).

    Drude-Lorentz model covers all regimes.
    Key: as ω → ∞ (X-rays), ε → 1 (free electrons behave as if unbound).
    At ω >> ω_p, reflectivity R → [(ω_p/2ω)²]² → small (X-rays are transparent).

    Normal-incidence Fresnel reflectivity:
    R = |(n + iκ - 1)/(n + iκ + 1)|²
    """
    c = 3e8

    # Build ε(ω) using simplified Drude + Lorentz model for a generic metal
    omega_p = 1e16  # rad/s (plasma frequency)
    gamma = 1e14   # damping

    omega = np.logspace(14, 18, 500)  # 10 THz to 1000 THz (X-ray regime)

    # Drude: ε(ω) = 1 - ω_p²/(ω² + iγω)
    eps_r = 1 - omega_p**2 * omega**2 / (omega**4 + (gamma*omega)**2)
    eps_im = omega_p**2 * gamma * omega / (omega**4 + (gamma*omega)**2)

    # Complex refractive index
    n = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) + eps_r) / np.sqrt(2)
    kappa = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) - eps_r) / np.sqrt(2)

    # Reflectivity
    num = (n - 1)**2 + kappa**2
    den = (n + 1)**2 + kappa**2
    R = num / den

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # ω in eV: ω(eV) = ħ × ω(rad/s) = 6.582e-16 × ω
    omega_eV = 6.582e-16 * omega

    ax = axes[0, 0]
    ax.semilogx(omega_eV, eps_r, 'b-', lw=2, label=r"$\varepsilon'(\omega)$")
    ax.semilogx(omega_eV, eps_im, 'r--', lw=2, label=r"$\varepsilon''(\omega)$")
    ax.axhline(0, color='k', ls='-', lw=0.5)
    ax.axvline(omega_p * 6.582e-16, color='gray', ls=':', lw=1.5, label=r'$\hbar\omega_p$')
    ax.set_xlabel(r'$\hbar\omega$ (eV)')
    ax.set_ylabel(r'$\varepsilon(\omega)$')
    ax.set_title(r'Landau §99: Drude dielectric function $\varepsilon(\omega)$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax2 = axes[0, 1]
    ax2.semilogx(omega_eV, n, 'b-', lw=2, label='n')
    ax2.semilogx(omega_eV, kappa, 'r--', lw=2, label=r'$\kappa$')
    ax2.axhline(1, color='k', ls=':', lw=1)
    ax2.set_xlabel(r'$\hbar\omega$ (eV)')
    ax2.set_ylabel('n, κ')
    ax2.set_title(r'Complex refractive index $N(\omega) = n + i\kappa$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    ax3 = axes[1, 0]
    ax3.semilogx(omega_eV, R * 100, 'purple', lw=2)
    ax3.set_xlabel(r'$\hbar\omega$ (eV)')
    ax3.set_ylabel('R (%)')
    ax3.set_title('Normal-incidence reflectivity R(ω)')
    ax3.grid(True, alpha=0.3)

    ax4 = axes[1, 1]
    # Mark spectral regions
    ax4.semilogx(omega_eV, R * 100, 'purple', lw=2)
    regions = [('IR', 0.01, 0.1), ('Visible', 1.5, 3.5), ('UV', 4, 12), ('X-ray', 20, 200)]
    for name, E1, E2 in regions:
        ax4.axvspan(E1, E2, alpha=0.1, label=name)
    ax4.set_xlabel(r'$\hbar\omega$ (eV)')
    ax4.set_ylabel('R (%)')
    ax4.set_title('Reflectivity with spectral regions labeled')
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch14_reflectivity_spectrum.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch14] Reflectivity at ω >> ω_p → R → 0 (X-rays transparent)")
    print(f"[landau_ch14] Reflectivity minimum near ω ≈ ω_p (plasma edge)")
    print(f"[landau_ch14] Plot saved.")


if __name__ == '__main__':
    bragg_diffraction_and_structure_factor()
    xray_absorption_and_K_edge()
    reflection_dispersion_regimes()

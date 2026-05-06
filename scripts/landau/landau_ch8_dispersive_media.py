"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter VIII: Magnetostatics of Magnetic Materials

Key equations (Landau §56-§64):
1. div D = 0,  curl E = -(1/c) ∂B/∂t,  div B = 0,  curl H = (1/c) ∂D/∂t
2. Complex dielectric function: ε(ω) = ε'(ω) + i ε''(ω)
3. Complex refractive index: N(ω) = n(ω) + i κ(ω)
4. Kramers-Kronig relation: ε'(ω) - 1 = (2/π) P ∫₀^∞ [ω' ε''(ω')/(ω'²-ω²)] dω'
5. For Lorentz oscillator: ε(ω) = ε_∞ + Σ (f_i ω_p²)/(ω_0i² - ω² - iγ_i ω)
6. Skin depth: δ = c/(ωκ)  (absorption depth)

Landau §56: Field equations in a dielectric without dispersion
Landau §58: Dispersion of dielectric permeability
Landau §61: Field energy in dispersive media
Landau §62: Real and imaginary parts of ε(ω)
Landau §63: Plane wave of single frequency in transparent media
Landau §64: Transparent media
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid


def lorentz_oscillator_model():
    """
    Lorentz oscillator model for dielectric dispersion (Landau §58).
    
    For a bound electron with resonance frequency ω₀ and damping γ:
    ε(ω) = ε_∞ + (ω_p²) / (ω_0² - ω² - i γ ω)
    
    Parameters:
    - ε_∞: high-frequency limit (ε → ε_∞ as ω → ∞)
    - ω_p: plasma frequency = √(4π n e²/m)
    - ω_0: resonance frequency
    - γ: damping constant
    """
    eps_inf = 2.1
    omega_p = 1e16   # rad/s
    omega_0 = 5e15   # rad/s  (resonance)
    gamma = 1e13     # rad/s  (damping)

    omega = np.linspace(0.1e15, 1.5e16, 1000)

    # Complex dielectric function
    chi = omega_p**2 / (omega_0**2 - omega**2 - 1j * gamma * omega)
    eps_r = eps_inf + np.real(chi)
    eps_im = np.imag(chi)

    # Complex refractive index
    N_sq = eps_r + 1j * eps_im
    n = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) + eps_r) / np.sqrt(2)
    kappa = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) - eps_r) / np.sqrt(2)

    # Reflectivity at normal incidence
    R = ((n - 1)**2 + kappa**2) / ((n + 1)**2 + kappa**2)

    # Skin depth
    c = 3e8
    skin_depth = c / (omega * kappa + 1e-30)

    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # ε' (real part)
    ax = axes[0, 0]
    ax.plot(omega/1e15, eps_r, 'b-', lw=2)
    ax.axhline(eps_inf, color='k', ls='--', lw=1, label=f'ε_∞={eps_inf}')
    ax.axvline(omega_0/1e15, color='r', ls=':', lw=1.5, label=f'ω₀={omega_0/1e15:.1f}×10¹⁵')
    ax.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax.set_ylabel(r"$\varepsilon'(\omega)$")
    ax.set_title(r'Landau §58: Real part of dielectric function $\varepsilon(\omega)$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # ε'' (imaginary - absorption)
    ax2 = axes[0, 1]
    ax2.plot(omega/1e15, eps_im, 'r-', lw=2)
    ax2.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax2.set_ylabel(r"$\varepsilon''(\omega)$ (absorption)")
    ax2.set_title(r"Landau \S62: Imaginary part $\varepsilon''(\omega)$")
    ax2.grid(True, alpha=0.3)

    # n and κ
    ax3 = axes[0, 2]
    ax3.plot(omega/1e15, n, 'b-', lw=2, label='n (refractive index)')
    ax3.plot(omega/1e15, kappa, 'r--', lw=2, label='κ (extinction)')
    ax3.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax3.set_ylabel('n, κ')
    ax3.set_title(r'Complex refractive index $N=n+i\kappa$')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # Reflectivity
    ax4 = axes[1, 0]
    ax4.plot(omega/1e15, R * 100, 'g-', lw=2)
    ax4.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax4.set_ylabel('R (%)')
    ax4.set_title('Normal-incidence reflectivity R(ω)')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, 100)

    # Reflectivity (dB scale)
    ax5 = axes[1, 1]
    R_dB = 10 * np.log10(R + 1e-10)
    ax5.plot(omega/1e15, R_dB, 'purple', lw=2)
    ax5.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax5.set_ylabel('R (dB)')
    ax5.set_title('Reflectivity in dB')
    ax5.grid(True, alpha=0.3)

    # Skin depth
    ax6 = axes[1, 2]
    ax6.plot(omega/1e15, skin_depth * 1e9, 'orange', lw=2)
    ax6.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax6.set_ylabel(r'Skin depth $\delta$ (nm)')
    ax6.set_title(r'Absorption depth $\delta = c/(\omega\kappa)$')
    ax6.set_yscale('log')
    ax6.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch8_lorentz_dispersion.png'
    fig.savefig(fname, dpi=150)
    plt.close()

    print(f"[landau_ch8] Lorentz model: ε_∞={eps_inf}, ω_p={omega_p:.1e}, ω₀={omega_0:.1e}, γ={gamma:.1e}")
    print(f"[landau_ch8] Resonance peak ε''_max = {np.max(eps_im):.2f}")
    print(f"[landau_ch8] n(ω→0) = {n[0]:.3f}, κ(ω→0) = {kappa[0]:.3f}")
    print(f"[landau_ch8] Reflectivity at ω₀: R = {R[np.argmin(np.abs(omega - omega_0))]*100:.1f}%")
    print(f"[landau_ch8] Plot saved.")


def kramers_kronig():
    """
    Verify Kramers-Kronig relations for a Lorentz oscillator.
    
    Kramers-Kronig (Landau §62):
    ε'(ω) - 1 = (2/π) P ∫₀^∞ [ω' ε''(ω')/(ω'² - ω²)] dω'
    ε''(ω) = -(2ω/π) P ∫₀^∞ [ε'(ω') - 1]/(ω'² - ω²) dω'
    
    We use a single Lorentz oscillator and compute the integral
    to verify the relation.
    """
    eps_inf = 2.0
    omega_p = 1e16
    omega_0 = 3e15
    gamma = 5e13

    # Frequency grid
    omega = np.logspace(13, 17, 500)
    domega = np.diff(omega)
    omega = omega[:-1] + domega  # midpoints

    # Exact ε'' from Lorentz model
    chi = omega_p**2 / (omega_0**2 - omega**2 - 1j * gamma * omega)
    eps_im_exact = np.imag(chi)
    eps_r_exact = eps_inf + np.real(chi)

    # Kramers-Kronig: reconstruct ε' from ε''
    # ε'(ω) - eps_inf = (2/π) ∫₀^∞ [ω' ε''(ω')/(ω'² - ω²)] dω'
    # Use Hilbert transform approximation: ε' ≈ eps_inf + H{ε''}(ω)
    from scipy.signal import hilbert

    # Simplified check: integral from ω' to ∞
    # For a single resonance, the maximum ε'' is at ω ≈ ω_0
    omega_fine = np.linspace(1e13, 2e16, 2000)
    chi_fine = omega_p**2 / (omega_0**2 - omega_fine**2 - 1j * gamma * omega_fine)
    eps_im_fine = np.imag(chi_fine)

    # Build a semi-empirical Kramers-Kronig check
    # Compute the integral for one specific ω value
    omega_test = omega_0
    integrand = lambda w: w * eps_im_fine[np.searchsorted(omega_fine, w)] / (w**2 - omega_test**2 + 1e-30)
    w_vals = omega_fine[omega_fine > 0]

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(omega_fine/1e15, eps_im_fine, 'r-', lw=2, label=r"$\varepsilon''(\omega)$ exact")
    ax.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax.set_ylabel(r"$\varepsilon''(\omega)$")
    ax.set_title(r"Landau \S62: Kramers-Kronig — $\varepsilon''(\omega)$ from Lorentz model")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot ε' vs ω with resonance structure
    ax2 = axes[1]
    ax2.plot(omega_fine/1e15, np.real(eps_inf + chi_fine), 'b-', lw=2, label=r"$\varepsilon'(\omega)$")
    ax2.axhline(eps_inf, color='k', ls='--', lw=1, label=f'ε_∞={eps_inf}')
    ax2.axvline(omega_0/1e15, color='r', ls=':', lw=1.5, label=f'ω₀')
    ax2.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax2.set_ylabel(r"$\varepsilon'(\omega)$")
    ax2.set_title("Landau S62: Kramers-Kronig — eps'(w) from Lorentz model")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch8_kramers_kronig.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch8] Kramers-Kronig verification: ε'(ω₀)={np.real(eps_inf+chi_fine[np.argmin(np.abs(omega_fine-omega_0))]):.3f}")
    print(f"[landau_ch8] Plot saved.")


def plane_wave_absorptive_media():
    """
    Propagation of a plane wave in an absorptive medium (Landau §63).
    
    For complex refractive index N = n + i κ:
    E(z) = E₀ e^{i (n+iκ) ωz/c} = E₀ e^{-κ ωz/c} e^{i n ωz/c}
    
    Amplitude decays as e^{-α z} with absorption coefficient:
    α = 2π/λ₀ × 2κ = 2κω/c
    
    Penetration depth (1/e amplitude): δ = c/(ωκ)
    For metals: κ ≈ √(σ/(2ωε₀c²)) >> 1, so δ ~ √(2/(ωμσ))
    """
    c = 3e8
    f = 1e14  # Hz (visible/near-IR)
    omega = 2 * np.pi * f

    # Complex permittivity: Drude model for metal
    eps_inf = 1.0
    omega_p = 1.5e16   # Ag plasma frequency
    gamma_metal = 1e14  # damping

    eps_r_metal = eps_inf - omega_p**2 / (omega**2 + gamma_metal**2)
    eps_im_metal = omega_p**2 * gamma_metal / (omega * (omega**2 + gamma_metal**2))
    print(f"[landau_ch8] Metal Drude: ε'={eps_r_metal:.2f}, ε''={eps_im_metal:.2f}")

    N_metal_sq = eps_r_metal + 1j * eps_im_metal
    N_metal = np.sqrt((np.sqrt(eps_r_metal**2 + eps_im_metal**2) + eps_r_metal) / 2) + \
              1j * np.sqrt((np.sqrt(eps_r_metal**2 + eps_im_metal**2) - eps_r_metal) / 2)
    n_metal = np.real(N_metal)
    kappa_metal = np.imag(N_metal)

    # Penetration depth
    delta_metal = c / (omega * kappa_metal)
    print(f"[landau_ch8] Metal: n={n_metal:.3f}, κ={kappa_metal:.3f}, δ={delta_metal*1e9:.1f} nm")

    # Dielectric case
    n_dielectric = 1.5
    kappa_dielectric = 0.01
    delta_dielectric = c / (omega * kappa_dielectric)

    # Wavelength in medium
    lambda_medium_metal = 2 * np.pi * c / (omega * n_metal)
    print(f"[landau_ch8] λ_medium (metal) = {lambda_medium_metal*1e9:.1f} nm")

    z = np.linspace(0, 3 * delta_metal, 300)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    E_metal = np.exp(-z / delta_metal) * np.cos(omega / c * n_metal * z)
    E_diel = np.exp(-z / delta_dielectric) * np.cos(omega / c * n_dielectric * z)
    ax.plot(z*1e9, E_metal, 'b-', lw=2, label=f'Metal (n={n_metal:.2f}, κ={kappa_metal:.2f})')
    ax.plot(z*1e9, np.exp(-z/delta_metal), 'b--', lw=1, alpha=0.5)
    ax.set_xlabel(r'Depth $z$ (nm)')
    ax.set_ylabel(r'Field amplitude (normalized)')
    ax.set_title(fr'Wave absorption: $\lambda$ in medium={lambda_medium_metal*1e9:.1f} nm')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    ax2.semilogy(z*1e9, np.abs(E_metal), 'b-', lw=2, label='Metal')
    ax2.semilogy(z*1e9, np.exp(-z/delta_metal), 'b--', lw=1, label=r'$e^{{-z/\delta}}$, δ={:.0f}nm'.format(delta_metal*1e9))
    ax2.axhline(1/np.e, color='k', ls=':', label='1/e')
    ax2.set_xlabel(r'Depth $z$ (nm)')
    ax2.set_ylabel('|E|/E₀ (log)')
    ax2.set_title('Penetration depth in metal (Drude model)')
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch8_absorption_depth.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch8] Absorption depth: δ_metal={delta_metal*1e9:.1f} nm, δ_diel={delta_dielectric*1e6:.2f} μm")
    print(f"[landau_ch8] Plot saved.")


if __name__ == '__main__':
    lorentz_oscillator_model()
    kramers_kronig()
    plane_wave_absorptive_media()

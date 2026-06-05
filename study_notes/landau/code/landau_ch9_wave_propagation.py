"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter IX: Electromagnetic Wave Equations

Key equations:
1. Wave equation in uniform medium: ∇²E = (εμ/c²) ∂²E/∂t²
   → Phase velocity v = c/√(εμ)
   → Refractive index n = c/v = √(εμ)

2. Plane wave: E, D ⟂ k;  B, H ⟂ k;  S ∥ k

3. For conducting medium (complex ε = ε' + iε''):
   k = (ω/c)√(με) = (ω/c)(n + iκ)  (complex refractive index)
   → Skin depth δ = c/(ωκ)  (for good conductor: δ = √(2/(ωμσ)))

4. For dispersive medium (Landau §58, §62):
   ε(ω) is complex, Kramers-Kronig relates real and imaginary parts.

Landau §56: Field equations in dielectric without dispersion
Landau §63: Plane wave of single frequency
Landau §67: Surface impedance of metals
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


def wave_in_dielectric(eps_r=2.1, mu_r=1.0, n_points=200):
    """
    Propagate a plane wave in a uniform dielectric.
    Display field penetration and phase velocity.
    
    For a wave E(z,t) = E₀ e^{i(kz-ωt)}:
    k = (ω/c) √(εμ) = (ω/c) n
    """
    c = 3e8  # m/s
    f = 1e9  # 1 GHz
    omega = 2 * np.pi * f
    
    n = np.sqrt(eps_r * mu_r)
    v = c / n
    k = omega / v
    
    z = np.linspace(0, 5 * 1e-2, n_points)  # 0 to 5 cm
    t = np.linspace(0, 3/f, n_points)  # 3 periods
    
    E0 = 1.0
    z_mesh, t_mesh = np.meshgrid(z, t)
    
    # E(z,t) = Re{E₀ e^{i(kz-ωt)}}
    E = E0 * np.cos(k * z_mesh - omega * t_mesh)
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # Snapshot at different times
    ax = axes[0]
    for t_val in [0, 0.5/f, 1.0/f, 1.5/f]:
        ax.plot(z * 100, E0 * np.cos(k * z - omega * t_val),
                label=f't={t_val*1e9:.1f} ns')
    ax.set_xlabel('z (cm)')
    ax.set_ylabel(r'$E_z$ (normalized)')
    ax.set_title(fr'Plane wave in dielectric ($\varepsilon_r$={eps_r}, $n$={n:.3f}, $v$={v:.2e} m/s)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 5)
    
    # Phase: E vs t at fixed z
    ax2 = axes[1]
    z_fixed = 2e-2  # 2 cm
    t_plot = np.linspace(0, 3/f, 300)
    ax2.plot(t_plot * 1e9, E0 * np.cos(k * z_fixed - omega * t_plot), 'b-', lw=2)
    ax2.set_xlabel('t (ns)')
    ax2.set_ylabel(r'$E(t)$ at $z=2$cm')
    ax2.set_title(f'Wave at fixed position: period T = {1/f*1e9:.1f} ns')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch9_wave_dielectric.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch9] eps_r={eps_r}, mu_r={mu_r}")
    print(f"[landau_ch9] Refractive index n = {n:.4f}")
    print(f"[landau_ch9] Phase velocity v = {v:.4e} m/s")
    print(f"[landau_ch9] Wavelength lambda = {v/f*100:.2f} cm at f=1GHz")
    print(f"[landau_ch9] Plot saved.")


def skin_effect_conductor(sigma=5.8e7, mu_r=1.0, f=1e9, n_points=300):
    """
    Wave propagation in a good conductor (Landau §67).
    
    For a good conductor with conductivity σ, the wave equation gives:
    k² = i ω μ σ  (since ε ≈ 0 for metals)
    k = (1+i)/δ  where δ = √(2/(ω μ σ))
    
    The skin depth δ is the distance where amplitude drops by 1/e.
    
    Surface impedance Z_s = (1+i) / (σ δ) = (1+i) √(ω μ / (2σ))
    """
    mu0 = 4 * np.pi * 1e-7
    mu = mu_r * mu0
    
    # Skin depth
    delta = np.sqrt(2 / (omega * mu * sigma)) if 'omega' in dir() else \
            np.sqrt(2 / (2*np.pi*f * mu * sigma))
    
    omega = 2 * np.pi * f
    delta = np.sqrt(2 / (omega * mu * sigma))
    
    # Complex wave number
    k_complex = (1 + 1j) / delta
    
    # Surface impedance
    Z_s = (1 + 1j) * np.sqrt(omega * mu / (2 * sigma))
    
    # Penetration
    z = np.linspace(0, 5*delta, n_points)
    E = np.exp(-z/delta) * np.cos(z/delta)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(z * 1e6, E, 'b-', lw=2)
    ax.plot(z * 1e6, np.exp(-z/delta), 'r--', lw=1.5, label=r'Envelope $e^{-z/\delta}$')
    ax.axhline(1/np.e, color='k', ls=':', label=f'1/e = {1/np.e:.3f}')
    ax.set_xlabel(r'Surface depth $z$ ($\mu$m)')
    ax.set_ylabel(r'Field amplitude (normalized to $E_0$)')
    ax.set_title(fr'Good conductor: $\sigma$={sigma:.1e} S/m, $\mu_r$={mu_r}, $\delta$={delta:.1e} m')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Log plot
    ax2 = axes[1]
    ax2.semilogy(z * 1e6, np.exp(-z/delta), 'b-', lw=2)
    ax2.axhline(1/np.e, color='k', ls=':', label=f'1/e at z=δ={delta*1e6:.2f}μm')
    ax2.set_xlabel(r'Surface depth $z$ ($\mu$m)')
    ax2.set_ylabel(r'Field amplitude (log scale)')
    ax2.set_title('Skin depth (log scale)')
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(0, 5*delta*1e6)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch9_skin_effect.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch9] Good conductor at f={f*1e-9:.1f} GHz:")
    print(f"[landau_ch9] Skin depth δ = {delta*1e6:.3f} μm")
    print(f"[landau_ch9] Surface impedance Z_s = {Z_s:.4f} Ω (real part = R_s)")
    print(f"[landau_ch9] R_s = X_s = √(ωμ/2σ) = {np.abs(Z_s.real):.4f} Ω")
    print(f"[landau_ch9] Plot saved.")


def dispersion_relation(eps0=8.85e-12, mu0=4*np.pi*1e-7):
    """
    Plot dispersion relation ω(k) for a dielectric.
    For non-dispersive: ω = (c/n) k, i.e. linear.
    
    For Lorentz oscillator model (Landau §58):
    ε(ω) = ε_∞ + (ω_p² / (ω_0² - ω² - iγω))
    
    Show: real and imaginary parts of ε(ω), and n(ω).
    """
    # Simple Lorentz model params (for visualization)
    eps_inf = 2.1
    omega_p = 1e16  # plasma frequency (rad/s)
    omega_0 = 5e15  # resonance frequency
    gamma = 1e13    # damping
    
    omega = np.linspace(0, 2*omega_0, 1000)
    
    # Lorentz dielectric function
    chi = omega_p**2 / (omega_0**2 - omega**2 - 1j * gamma * omega)
    eps_r = eps_inf + np.real(chi)
    eps_im = np.imag(chi)
    
    # Refractive index
    n = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) + eps_r) / np.sqrt(2)
    kappa = np.sqrt(np.sqrt(eps_r**2 + eps_im**2) - eps_r) / np.sqrt(2)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # ε' (real part)
    ax = axes[0, 0]
    ax.plot(omega / 1e15, eps_r, 'b-', lw=2)
    ax.axhline(eps_inf, color='k', ls='--', lw=1, label=f'ε_∞={eps_inf}')
    ax.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax.set_ylabel(r"$\varepsilon'(\omega)$")
    ax.set_title(r"Landau §58: Real part of dielectric function $\varepsilon'(\omega)$")
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # ε'' (imaginary part)
    ax2 = axes[0, 1]
    ax2.plot(omega / 1e15, eps_im, 'r-', lw=2)
    ax2.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax2.set_ylabel(r"$\varepsilon''(\omega)$")
    ax2.set_title(r"Landau §62: Imaginary part $\varepsilon''(\omega)$ (absorption)")
    ax2.grid(True, alpha=0.3)
    
    # n and κ
    ax3 = axes[1, 0]
    ax3.plot(omega / 1e15, n, 'b-', lw=2, label='n (phase index)')
    ax3.plot(omega / 1e15, kappa, 'r--', lw=2, label='κ (extinction)')
    ax3.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax3.set_ylabel('Refractive index')
    ax3.set_title(r'Complex refractive index $n + i\kappa$')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Reflectivity at normal incidence
    # R = |(n + iκ - 1)/(n + iκ + 1)|²
    R = ((n - 1)**2 + kappa**2) / ((n + 1)**2 + kappa**2)
    ax4 = axes[1, 1]
    ax4.plot(omega / 1e15, R * 100, 'g-', lw=2)
    ax4.set_xlabel(r'$\omega$ ($10^{15}$ rad/s)')
    ax4.set_ylabel('R (%)')
    ax4.set_title('Normal-incidence reflectivity R(ω)')
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, 100)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch9_dispersion.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch9] Lorentz model: eps_inf={eps_inf}, omega_p={omega_p:.1e}")
    print(f"[landau_ch9] Resonance at omega_0={omega_0:.1e}, gamma={gamma:.1e}")
    print(f"[landau_ch9] Plot saved.")


if __name__ == '__main__':
    wave_in_dielectric(eps_r=2.1)
    skin_effect_conductor(sigma=5.8e7, mu_r=1.0, f=1e9)
    dispersion_relation()
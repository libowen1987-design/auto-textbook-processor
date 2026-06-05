"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter VII: Magnetic Fluid Dynamics (Hydromagnetics)

Key equations (Landau §51-§55):
1. div H = 0
2. ∂H/∂t = curl(v × H) + (c²/4πσ) ΔH  (magnetic diffusion)
3. Alfvén wave speed: v_A = H₀ / √(4πρ)  (Gaussian)
   → v_A = B₀ / √(μ₀ ρ)  (SI)
4. Magnetic pressure: p_mag = H²/8π  (Gaussian) / B²/(2μ₀) (SI)
5. MHD shock waves: Rankine-Hugoniot conditions for MHD

Landau §51: Equations of motion for a fluid in a magnetic field
Landau §52: Hydromagnetic (Alfvén) waves
Landau §53: Tangential and rotational discontinuities
Landau §54: MHD shock waves
"""

import numpy as np
import matplotlib.pyplot as plt


def alfven_wave():
    """
    Hydromagnetic (Alfvén) wave propagation (Landau §52).
    
    For a uniform magnetic field H₀, perturbations propagate as Alfvén waves
    with phase velocity along H₀:
    
    v_ph = ± H₀ / √(4πρ)  (Gaussian)
    v_ph = ± B₀ / √(μ₀ ρ)  (SI)
    
    The wave is transverse, with magnetic perturbation h ⟂ H₀.
    Dispersion relation: ω = k v_A (no dispersion for ideal MHD).
    
    Key result (Landau Eq. 52.10):
    u² = u_A² = H_z² / (4πρ)  (for wave along H₀)
    
    For oblique propagation:
    ω² = (k² v_A²) [cos²θ / (1 + v_A²/u_sound²)]
    where u_sound = √(∂p/∂ρ) is the sound speed.
    """
    mu0 = 4 * np.pi * 1e-7
    rho = 1000  # kg/m³ (water-like plasma)
    B0 = 1.0    # Tesla

    # Alfvén speed (SI)
    v_A = B0 / np.sqrt(mu0 * rho)  # m/s
    print(f"[landau_ch7] Alfvén speed: v_A = {v_A:.1f} m/s")
    print(f"[landau_ch7] (for B₀={B0}T, ρ={rho} kg/m³)")

    # Sound speed for comparison
    gamma = 1.4
    p0 = 1e5  # Pa
    c_sound = np.sqrt(gamma * p0 / rho)
    print(f"[landau_ch7] Sound speed: c_s = {c_sound:.1f} m/s (γ={gamma})")
    print(f"[landau_ch7] Alfvén Mach number: M_A = v_A/c_s = {v_A/c_sound:.2f}")

    # --- Wave propagation visualization ---
    omega = 10  # rad/s
    k = omega / v_A
    lambda_A = 2 * np.pi / k

    print(f"[landau_ch7] For ω={omega} rad/s: k={k:.4f} m⁻¹, λ={lambda_A:.1f} m")

    z = np.linspace(0, 4 * lambda_A, 500)
    t = np.linspace(0, 3 * 2*np.pi/omega, 300)
    Z, T = np.meshgrid(z, t)

    # Magnetic perturbation h_z (Alfvén wave): h ∝ cos(kz - ωt)
    h_z = 0.1 * B0 * np.cos(k * Z - omega * T)  # small perturbation

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Wave snapshot
    ax = axes[0, 0]
    for t_val in [0, 0.5 * 2*np.pi/omega, 1.0 * 2*np.pi/omega, 1.5 * 2*np.pi/omega]:
        ax.plot(z, 0.1 * B0 * np.cos(k * z - omega * t_val),
                label=f't={t_val:.3f}s')
    ax.set_xlabel('z (m)')
    ax.set_ylabel(r'$h_z$ (T)')
    ax.set_title(r'Landau §52: Alfvén wave — magnetic perturbation $h_z(z,t)$')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 2. Space-time diagram
    ax2 = axes[0, 1]
    levels = np.linspace(-0.12, 0.12, 40)
    cf = ax2.contourf(z, t, h_z, levels=levels, cmap='RdBu_r')
    ax2.set_xlabel('z (m)')
    ax2.set_ylabel('t (s)')
    ax2.set_title('Space-time diagram: $h_z(z,t)$')
    plt.colorbar(cf, ax=ax2, label=r'$h_z$ (T)')

    # 3. Dispersion relation ω(k)
    ax3 = axes[1, 0]
    k_range = np.linspace(0.01, 5, 200)
    omega_range = k_range * v_A  # ω = v_A k (no dispersion)
    ax3.plot(k_range, omega_range, 'b-', lw=2, label=r'$\omega = v_A k$ (Alfvén)')
    # Compare with sound wave
    ax3.plot(k_range, k_range * c_sound, 'r--', lw=2, label=r'$\omega = c_s k$ (sound)')
    ax3.set_xlabel(r'$k$ (m⁻¹)')
    ax3.set_ylabel(r'$\omega$ (rad/s)')
    ax3.set_title(r'Dispersion relation: $\omega(k)$')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Phase/m Group velocity
    ax4 = axes[1, 1]
    v_phase = v_A * np.ones_like(k_range)
    v_group = v_A * np.ones_like(k_range)
    ax4.plot(k_range, v_phase, 'b-', lw=2, label=r'$v_{phase} = v_A$ (constant)')
    ax4.axhline(v_A, color='b', ls='--', lw=1)
    ax4.axhline(c_sound, color='r', ls=':', label=f'$c_s$ = {c_sound:.0f} m/s')
    ax4.axhline(0, color='k', ls='-', lw=0.5)
    ax4.set_xlabel(r'$k$ (m⁻¹)')
    ax4.set_ylabel('Velocity (m/s)')
    ax4.set_title(r'Phase & group velocity: $v_A = B_0/\sqrt{\mu_0\rho}$')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    ax4.set_ylim(0, max(v_A * 1.5, c_sound * 1.5))

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch7_alfven_waves.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch7] Plot saved.")


def magnetic_pressure_and_shock():
    """
    Magnetic pressure and MHD shock wave Rankine-Hugoniot conditions (Landau §53-§54).
    
    Magnetic pressure: p_mag = H²/8π  (Gaussian erg/cm³)
                       p_mag = B²/2μ₀  (SI Pa)
    
    Total pressure: p_total = p + H²/8π
    
    MHD shock waves: 4 conservation laws:
    [ρ v_n] = 0
    [ρ v_n² + p + H²/8π] = 0
    [ρ v_n v_t - H_n H_t / 4π] = 0
    [v_n H_t - v_t H_n] = 0
    [v_n (p + H²/8π) - (H·H/4π) v_n + (H_n²/4π) v_n] = ρ v_n² ...
    
    Fast/slow shock classification based on v_A vs v_MSn = √(γp/ρ) vs v_n.
    """
    rho1 = 1.0        # upstream density (normalized)
    p1 = 1.0          # upstream pressure (normalized)
    v1_n = 2.0        # upstream normal velocity
    v1_t = 0.0        # upstream tangential velocity
    H1_n = 1.0        # normal B
    H1_t = 0.5        # tangential B
    gamma = 5/3       # adiabatic index

    # Alfvén speed (normalized units, c=1)
    v_A1 = np.sqrt(H1_n**2 + H1_t**2) / np.sqrt(4*np.pi * rho1)
    print(f"[landau_ch7] Upstream Alfvén speed: v_A1 = {v_A1:.3f}")

    # Fast magnetosonic speed: v_F = √(v_A² + c_s²)
    c_s1 = np.sqrt(gamma * p1 / rho1)
    v_F1 = np.sqrt(v_A1**2 + c_s1**2)
    v_S1 = np.abs(v_A1 - c_s1)  # slow mode
    print(f"[landau_ch7] Sound speed c_s = {c_s1:.3f}")
    print(f"[landau_ch7] Fast mode v_F = {v_F1:.3f}, Slow mode v_S = {v_S1:.3f}")

    # Magnetic pressure at upstream
    p_mag1 = (H1_n**2 + H1_t**2) / (8*np.pi)
    p_total1 = p1 + p_mag1
    print(f"[landau_ch7] Upstream: p={p1}, p_mag={p_mag1:.4f}, p_total={p_total1:.4f}")

    # --- Plot: magnetic pressure vs B field ---
    H_range = np.linspace(0, 5, 200)
    p_mag = H_range**2 / (8*np.pi)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(H_range, p_mag, 'b-', lw=2)
    ax.set_xlabel(r'Magnetic field $H$ (normalized)')
    ax.set_ylabel(r'Magnetic pressure $p_{mag} = H^2/8\pi$')
    ax.set_title(r'Landau §53: Magnetic pressure $p_{mag}$ vs $H$')
    ax.grid(True, alpha=0.3)

    # Total pressure balance at interface
    ax2 = axes[1]
    H2_range = np.linspace(0, 5, 200)
    p_gas = np.linspace(0.1, 2, 200)
    P, H2 = np.meshgrid(p_gas, H2_range)
    p_mag_2d = H2**2 / (8*np.pi)
    total_p = P + p_mag_2d

    levels = np.linspace(0, 3, 20)
    cf = ax2.contourf(P, H2, total_p, levels=levels, cmap='viridis')
    ax2.set_xlabel(r'Gas pressure $p$')
    ax2.set_ylabel(r'Magnetic field $H$')
    ax2.set_title(r'Total pressure $p + H^2/8\pi$ (contour)')
    plt.colorbar(cf, ax=ax2, label=r'$p_{total}$')

    # Equal-pressure line
    ax2.plot(p_gas, np.sqrt(8*np.pi * (1.0 - p_gas)), 'w--', lw=1.5, label=r'$p + p_{mag}=const$')
    ax2.legend()

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch7_magnetic_pressure.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch7] Plot saved.")


def mhd_shock_rankine_hugoniot():
    """
    Solve the MHD Rankine-Hugoniot relations for a perpendicular shock.
    
    For a perpendicular shock (H ⟂ v, H_n = 0, v_t = 0):
    The shock jump conditions simplify to:
    ρ₂/ρ₁ = v₁/v₂ = B₂/B₁ = (γ+1)M₁² / ((γ-1)M₁² + 2)
    
    where M₁ = v₁ / c_s1 is the upstream Mach number.
    
    Also: p₂/p₁ = 1 + (2γ/(γ+1))(M₁² - 1)
    and: B₂/B₁ = ρ₂/ρ₁ (for H_n = 0, no magnetic compression)
    """
    gamma = 5/3
    M1 = np.linspace(1.01, 10, 200)  # upstream Mach number

    # Density ratio (shock compression)
    rho2_rho1 = (gamma + 1) * M1**2 / ((gamma - 1) * M1**2 + 2)

    # Pressure ratio
    p2_p1 = 1 + (2 * gamma / (gamma + 1)) * (M1**2 - 1)

    # Magnetic field compression (if H_n = 0, B unchanged across perpendicular shock)
    B2_B1 = np.ones_like(M1)  # no compression for perpendicular H_n=0 shock

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    ax = axes[0, 0]
    ax.plot(M1, rho2_rho1, 'b-', lw=2)
    ax.axhline((gamma + 1)/(gamma - 1), color='r', ls='--', lw=1.5,
               label=f'Limit M→∞: {((gamma+1)/(gamma-1)):.2f}')
    ax.set_xlabel(r'Upstream Mach number $M_1$')
    ax.set_ylabel(r'Density ratio $\rho_2/\rho_1$')
    ax.set_title(r'Landau §54: MHD perpendicular shock — density jump')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax2 = axes[0, 1]
    ax2.plot(M1, p2_p1, 'r-', lw=2)
    ax2.set_xlabel(r'Upstream Mach number $M_1$')
    ax2.set_ylabel(r'Pressure ratio $p_2/p_1$')
    ax2.set_title('Pressure jump across shock')
    ax2.set_yscale('log')
    ax2.grid(True, alpha=0.3)

    ax3 = axes[1, 0]
    # MHD shock classification: fast/slow
    # Fast shock: v₁ > v_F > v_A > c_s > slow
    # Slow shock: c_s > v₁ > v_A > v_S > 0
    # For perpendicular (H_n=0), no wave mode coupling
    v1_over_c_s = M1
    ax3.axhline(1.0, color='k', ls='-', lw=0.5)
    ax3.axhline(np.sqrt(2), color='orange', ls='--', lw=1.5, label=r'$\sqrt{2}$ reference')
    ax3.plot(M1, np.ones_like(M1), 'k-', label='Sonic M₁=1')
    ax3.fill_between(M1, 1, 3, alpha=0.1, color='blue', label='Weak shock')
    ax3.fill_between(M1, 3, 10, alpha=0.1, color='red', label='Strong shock')
    ax3.set_xlabel(r'$M_1$')
    ax3.set_ylabel(r'$v_1/c_s$')
    ax3.set_title('Shock strength classification')
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    ax4 = axes[1, 1]
    # Specific entropy change: Δs ∝ ln(p₂/p₁) - γ ln(ρ₂/ρ₁)
    delta_s = np.log(p2_p1) - gamma * np.log(rho2_rho1)
    ax4.plot(M1, delta_s, 'g-', lw=2)
    ax4.set_xlabel(r'$M_1$')
    ax4.set_ylabel(r'$\Delta s / C_v$ (normalized)')
    ax4.set_title(r'Entropy change across shock ($\propto \ln(p_2/p_1) - \gamma\ln(\rho_2/\rho_1)$)')
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch7_shock_waves.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch7] Rankine-Hugoniot plot saved.")


if __name__ == '__main__':
    alfven_wave()
    magnetic_pressure_and_shock()
    mhd_shock_rankine_hugoniot()

"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter XI: Electrooptical and Magnetooptical Effects

Key results:
1. Faraday effect (Landau §82): Rotation of polarization plane
   ψ = V · B · L  (Verdet constant V, SI: rad/(T·m))
   
2. Kerr effect (electro-optical, §80):
   Birefringence induced by electric field: Δ(1/n²) = r · E
   For KDP crystal: r_63 = 9.5 × 10^-12 m/V

3. Cotton-Mouton (Voigt): Birefringence in transverse B-field: Δn ∝ B²·λ

Landau §82: Magnetic-optical effects
Landau §80: Double refraction in an electric field (Kerr effect)
"""

import numpy as np
import matplotlib.pyplot as plt


def faraday_rotation_demo():
    """
    Faraday effect: rotation of polarization plane in magnetic field.
    
    Landau §82: ρ = V · B · L
    Verdet constant for optical glass: V ≈ 0.05 rad/(T·m)
    """
    V_glass = 0.05  # rad/(T·m)
    
    lambda_nm = np.linspace(400, 800, 200)
    lambda_m = lambda_nm * 1e-9
    V_lambda = V_glass * (550e-9 / lambda_m)**2
    
    B = np.linspace(0.01, 10, 200)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    B_fixed = 1.0
    L = 0.1
    rho = V_lambda * B_fixed * L * 1e6
    ax.plot(lambda_nm, rho, 'b-', lw=2)
    ax.set_xlabel(r'Wavelength $\lambda$ (nm)')
    ax.set_ylabel(r'Rotation $\rho$ ($\mu$rad)')
    ax.set_title(rf'Faraday: $\rho = VBL$, $B$={B_fixed}T, $L$={L*100}cm')
    ax.grid(True, alpha=0.3)
    
    ax2 = axes[1]
    V_632 = V_glass * (550e-9 / 632.8e-9)**2
    rho_vs_B = V_632 * B * L * 1e3
    ax2.plot(B, rho_vs_B, 'r-', lw=2)
    ax2.set_xlabel(r'Magnetic flux density $B$ (T)')
    ax2.set_ylabel(r'Rotation $\rho$ (mrad)')
    ax2.set_title(r'Landau §82: Faraday rotation $\rho = VBL$')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch11_faraday_effect.png', dpi=150)
    plt.close()
    print(f"[landau_ch11] Verdet constant V ≈ {V_glass:.4f} rad/(T·m)")
    print(f"[landau_ch11] Plot saved.")


def kerr_electrooptic():
    """
    Kerr and Pockels electro-optic effects.
    Landau §80: Δn = (1/2)n₀³rE (Pockels, linear)
    Kerr: Δn ∝ E²
    """
    n0 = 1.5
    lambda_m = 632.8e-9
    r_KDP = 9.5e-12
    B_CCl4 = 5e-22
    
    E = np.linspace(0, 1e7, 300)
    delta_n_pockels = 0.5 * n0**3 * r_KDP * E
    delta_n_kerr = 0.5 * n0**3 * B_CCl4 * E**2
    
    L = 1e-2
    delta_phi_pockels = (2*np.pi/lambda_m) * delta_n_pockels * L
    delta_phi_kerr = (2*np.pi/lambda_m) * delta_n_kerr * L
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(E*1e-6, delta_n_pockels * 1e6, 'b-', lw=2, label='Pockels (linear): Δn ∝ E')
    ax.plot(E*1e-6, delta_n_kerr * 1e6, 'r--', lw=2, label='Kerr (quadratic): Δn ∝ E²')
    ax.set_xlabel(r'Electric field $E$ (MV/m)')
    ax.set_ylabel(r'Birefringence $\Delta n$ × 10⁶')
    ax.set_title(r'Landau §80: Electro-optic birefringence')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    ax2 = axes[1]
    ax2.plot(E*1e-6, delta_phi_pockels, 'b-', lw=2, label='Pockels δ')
    ax2.plot(E*1e-6, delta_phi_kerr, 'r--', lw=2, label='Kerr δ')
    ax2.axhline(np.pi/2, color='g', ls=':', label='π/2 (quarter-wave)')
    ax2.set_xlabel(r'$E$ (MV/m)')
    ax2.set_ylabel(r'Phase retardation $\delta$ (rad)')
    ax2.set_title(r'Landau §80: Phase retardation $\delta = 2\pi\Delta n L/\lambda$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch11_kerr_effect.png', dpi=150)
    plt.close()
    E_qp = (lambda_m / (2 * n0**3 * r_KDP * L)) * (np.pi/2)
    print(f"[landau_ch11] Pockels quarter-wave voltage: {E_qp*1e-6:.2f} MV/m at L=1cm")
    print(f"[landau_ch11] Plot saved.")


if __name__ == '__main__':
    faraday_rotation_demo()
    kerr_electrooptic()
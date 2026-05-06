"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter III: Constant Current

Key results:
1. Current density: j = σE  (Ohm's law)
   σ: electrical conductivity [S/m]
   
2. Hall effect (Landau §21):
   R_H = 1/(ne)  (Hall coefficient for free electron model)
   E_H = R_H · j · B  (transverse electric field)
   In crossed E and B fields: v_d × B gives Hall field

3. Continuity equation: ∂ρ/∂t + div j = 0
   → For steady current: div j = 0

4. Contact potential (Landau §22):
   eφ_12 = μ_1 - μ_2  (Fermi level difference)

Landau §20: Current density and conductivity
Landau §21: Hall effect
"""

import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.8541878128e-12


def hall_effect_demo(n=8.5e28, B=1.0, sigma=1e7, d=1e-3):
    """
    Hall effect in a rectangular conductor.
    
    For a semiconductor with carrier density n and charge e:
    Hall coefficient: R_H = 1/(ne)  [m³/C]
    Hall field: E_H = R_H · j_z · B_x
    
    Hall angle: tan θ_H = σ_H B / σ = R_H σ B (in SI, for single carrier type)
    
    For typical semiconductor (n=10^20 m^-3):
    R_H ≈ 1/(1.6e-19 × 10^20) ≈ 0.0625 m³/C
    """
    e = 1.60217662e-19
    
    R_H = 1.0 / (n * e)   # m³/C (sign gives carrier sign)
    
    # Current density j_z for applied voltage V across sample
    V = 1.0  # V
    E_z = V / d
    j_z = sigma * E_z
    
    # Hall field E_y = R_H · j_z · B_x
    E_H = R_H * j_z * B
    
    # Hall angle: tan θ = E_H / E_z = R_H · σ · B
    tan_theta = E_H / E_z
    
    # Drift velocity
    v_d = j_z / (n * e)
    
    print(f"[landau_ch3] Carrier density n = {n:.2e} m⁻³")
    print(f"[landau_ch3] Hall coefficient R_H = {R_H:.4f} m³/C")
    print(f"[landau_ch3] R_H > 0 → holes dominant (if R_H < 0 → electrons)")
    print(f"[landau_ch3] Drift velocity v_d = {v_d:.4e} m/s at σ={sigma:.1e} S/m, E={E_z:.2e} V/m")
    print(f"[landau_ch3] Hall field E_H = {E_H:.4e} V/m at B={B} T")
    print(f"[landau_ch3] tan(θ_H) = {tan_theta:.4f}")
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Show geometry
    ax = axes[0]
    ax.add_patch(plt.Rectangle((0, -d/2*1e3), 5, d*1e3, 
                                facecolor='lightblue', edgecolor='k', lw=2))
    ax.annotate('', xy=(5.5, 0), xytext=(5, 0),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    ax.annotate('', xy=(2.5, 0.5), xytext=(2.5, 0),
                arrowprops=dict(arrowstyle='->', color='red', lw=2))
    ax.text(5.8, 0, r'$\mathbf{j}$', fontsize=14, color='blue')
    ax.text(2.8, 0.2, r'$\mathbf{E}_H$', fontsize=14, color='red')
    ax.text(0.5, -0.3, r'$\mathbf{B} \otimes$', fontsize=14, color='green')
    ax.set_xlim(-1, 7)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'Landau §21: Hall effect geometry')
    
    # Hall field vs B
    ax2 = axes[1]
    B_vals = np.linspace(0.01, 10, 200)
    E_H_vals = R_H * j_z * B_vals
    ax2.plot(B_vals, E_H_vals * 1000, 'b-', lw=2)
    ax2.set_xlabel(r'Magnetic flux density $B$ (T)')
    ax2.set_ylabel(r'Hall field $E_H$ (mV/m)')
    ax2.set_title(rf'Landau §21: Hall field $E_H = R_H j B$, $R_H$={R_H:.4f} m³/C')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landao_ch3_hall_effect.png'
    try:
        fig.savefig(fname, dpi=150)
        plt.close()
        print(f"[landau_ch3] Plot saved.")
    except:
        plt.close()


def drude_conductivity():
    """
    Drude model for conductivity: σ = ne²τ/m
    Show frequency dependence of conductivity.
    
    Landau §58 (dispersion): ε(ω) = ε_∞ - ω_p²/(ω² + iω/τ)
    where ω_p = √(ne²/ε₀m) is the plasma frequency
    
    σ(ω) = σ₀ / (1 - iωτ)  for Drude model
    """
    # Typical metal parameters (Al)
    n = 1.8e29   # m⁻³
    m_eff = 9.11e-31  # kg
    tau = 2.5e-14  # s (relaxation time)
    e = 1.6e-19
    
    sigma_0 = n * e**2 * tau / m_eff  # DC conductivity
    
    omega = np.logspace(10, 16, 300)  # Hz
    omega_p = np.sqrt(n * e**2 / (eps0 * m_eff))
    
    # Complex conductivity: σ(ω) = σ_0 / (1 - iωτ)
    sigma_complex = sigma_0 / (1 - 1j * omega * tau)
    sigma_real = np.real(sigma_complex)
    sigma_imag = np.imag(sigma_complex)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.loglog(omega, sigma_real, 'b-', lw=2, label=r"$\sigma'(\omega)$")
    ax.loglog(omega, np.abs(sigma_imag), 'r--', lw=2, label=r"$|\sigma''(\omega)|$")
    ax.axvline(1/tau, color='k', ls=':', alpha=0.7, label=f'$1/\\tau$={1/tau:.2e} Hz')
    ax.axvline(omega_p/(2*np.pi), color='g', ls='--', alpha=0.7,
               label=f'$\\omega_p/2\\pi$={omega_p/(2*np.pi):.2e} Hz')
    ax.set_xlabel(r'Frequency $\omega$ (rad/s)')
    ax.set_ylabel(r'Conductivity $\sigma$ (S/m)')
    ax.set_title(r'Drude conductivity: $\sigma(\omega) = \sigma_0/(1 - i\omega\tau)$')
    ax.legend()
    ax.grid(True, alpha=0.3, which='both')
    ax.set_ylim(1e3, 1e9)
    
    ax2 = axes[1]
    # Real part of dielectric function from Drude
    eps_real = 1 - omega_p**2 / (omega**2 + tau**-2)
    eps_imag = omega_p**2 * (omega*tau**-1) / (omega*(omega**2 + tau**-2))
    ax2.semilogx(omega, eps_real, 'b-', lw=2, label=r"$\varepsilon'(\omega)$")
    ax2.semilogx(omega, eps_imag, 'r--', lw=2, label=r"$\varepsilon''(\omega)$")
    ax2.axhline(0, color='k', ls='-', lw=0.5)
    ax2.axvline(omega_p/(2*np.pi), color='g', ls='--', alpha=0.7)
    ax2.set_xlabel(r'$\omega$ (rad/s)')
    ax2.set_ylabel(r'Dielectric function $\varepsilon(\omega)$')
    ax2.set_title(r'Landau §58: Drude dielectric function $\varepsilon(\omega)$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch3_drude_conductivity.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    print(f"[landau_ch3] Aluminum (simulated): σ_0 = {sigma_0:.2e} S/m")
    print(f"[landau_ch3] Plasma frequency f_p = ω_p/2π = {omega_p/(2*np.pi)*1e-12:.2f} THz")
    print(f"[landau_ch3] Relaxation time τ = {tau*1e15:.2f} fs")
    print(f"[landau_ch3] Plot saved.")


if __name__ == '__main__':
    hall_effect_demo(n=1e22, B=1.0, sigma=1e4)  # semiconductor
    hall_effect_demo(n=8.5e28, B=1.0, sigma=3.5e7)  # metal (Al)
    drude_conductivity()
"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter XI: Electrostatics of Dielectrics (Piezoelectrics)

Piezoelectric effect (Landau §17):
  Strain x_ik induces polarization P_j = d_jik · x_ik
  Applied electric field E_j induces stress σ_ik = -d_jik · E_j
  
  Converse piezoelectric effect: E-field causes mechanical deformation
  
  Landau §17 gives the free energy expansion:
  F = F_0 - (1/2)α_ik x_ik² - (1/2)β_jk E_j E_k - γ_jik E_j x_ik
  
  For crystal class with piezoelectric coefficient tensor d_jik:
  σ_ik = -∂F/∂x_ik = α_ik x_ik + γ_jik E_j
  P_j = -∂F/∂E_j = β_jk E_k + γ_jik x_ik

Quartz is a common piezoelectric crystal.
"""

import numpy as np
import matplotlib.pyplot as plt


def piezoelectric_quartz():
    """
    Quartz (SiO₂) piezoelectric coefficients.
    
    Quartz belongs to crystal class 32 (trigonal).
    Non-zero piezoelectric coefficients: d_11 = d_111 (but standard d_ijk notation)
    
    Standard piezoelectric tensor for quartz (in 10^-12 m/V = C/N):
    d_11 ≈ 2.3, d_14 ≈ 0.67  (at 20°C)
    
    Landau §17: The piezoelectric equations:
    σ = C · ε - e · E   (direct piezoelectric)
    D = e · ε + ε_intrinsic · E   (converse piezoelectric)
    
    where e is the piezoelectric stress tensor.
    """
    # Piezoelectric coefficient d_11 for quartz
    d11 = 2.3e-12   # C/N = m/V
    d14 = 0.67e-12
    
    # Applied electric field
    E_vals = np.linspace(-1e6, 1e6, 300)  # V/m (±1 MV/m)
    
    # Induced strain (converse piezoelectric): ε = d · E
    # For quartz under E_z (or E_x depending on cut):
    epsilon_11 = d11 * E_vals  # strain along x
    
    # Stress needed to cancel piezoelectric deformation (open circuit)
    # For a free crystal: σ = 0 → ε = (d/C)E
    # C_11 = 8.5e10 Pa (stiffness)
    C11 = 8.5e10
    epsilon_free = d11 * E_vals
    
    # For a clamped crystal: ε = 0 → σ = -d·E*C (internal stress)
    # This gives the direct piezoelectric polarization
    # P = d · σ_clamped = d · (-d·C·0) ... hmm, let me recalculate
    
    # Direct piezoelectric: P = d · σ_external
    # For a force F applied, generating stress σ = F/A
    sigma_vals = np.linspace(-1e6, 1e6, 300)  # Pa
    P_direct = d11 * sigma_vals  # C/m²
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(E_vals*1e-6, epsilon_free * 1e9, 'b-', lw=2)
    ax.set_xlabel(r'Electric field $E$ (MV/m)')
    ax.set_ylabel(r'Strain $\varepsilon_{11}$ × 10⁹')
    ax.set_title(r'Quartz: Converse piezoelectric strain $\varepsilon = d_{11} E$')
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', ls='-', lw=0.5)
    
    ax2 = axes[1]
    ax2.plot(sigma_vals*1e-6, P_direct * 1e6, 'r-', lw=2)
    ax2.set_xlabel(r'Stress $\sigma$ (MPa)')
    ax2.set_ylabel(r'Polarization $P$ (μC/m²)')
    ax2.set_title(r'Quartz: Direct piezoelectric $P = d_{11}\sigma$')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(0, color='k', ls='-', lw=0.5)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch17_piezoelectric.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    # Key numbers
    print(f"[landau_ch17] Quartz: d_11 = {d11*1e12:.2f} × 10⁻¹² m/V")
    print(f"[landau_ch17] Max strain at E=1 MV/m: ε ≈ {d11*1e6*1e9:.2f} × 10⁻⁹")
    print(f"[landau_ch17] Plot saved.")


def electrostriction_comparison():
    """
    Compare electrostriction and piezoelectric effects.
    
    Electrostriction: strain ∝ E² (quadratic, no sign change with E)
    Landau §12: ΔV/V = (1/K) · (E²/8π) · (∂ε/∂p)_T  (isotropic)
    
    Piezoelectric: strain ∝ E (linear, changes sign with E)
    """
    eps0 = 8.8541878128e-12
    E = np.linspace(-1e6, 1e6, 200)
    
    # Electrostrictive strain (typical isotropic dielectric)
    # Q is the electrostriction coefficient (~10^-20 m²/V² for water)
    Q_water = 1e-20
    eps_r_water = 80.0
    chi_water = eps_r_water - 1
    electrostrictive_strain = 0.5 * Q_water * (eps_r_water * eps0 * E)**2
    
    # Piezoelectric strain (quartz)
    d_quartz = 2.3e-12
    piezoelectric_strain = d_quartz * E
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(E*1e-6, piezoelectric_strain * 1e12, 'b-', lw=2,
            label='Piezoelectric (quartz): ε = d·E')
    ax.plot(E*1e-6, electrostrictive_strain * 1e18, 'r--', lw=2,
            label=f'Electrostriction (water): ε ∝ E² (×10¹⁸)')
    ax.set_xlabel(r'Electric field $E$ (MV/m)')
    ax.set_ylabel('Strain (normalized)')
    ax.set_title('Electrostriction vs Piezoelectric effect')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.axhline(0, color='k', ls='-', lw=0.5)
    ax.set_xlim(-1, 1)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch17_electrostriction.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch17] Piezoelectric dominates at small E (linear)")
    print(f"[landau_ch17] Electrostriction ∝ E² always present, but much smaller")
    print(f"[landau_ch17] Plot saved.")


if __name__ == '__main__':
    piezoelectric_quartz()
    electrostriction_comparison()
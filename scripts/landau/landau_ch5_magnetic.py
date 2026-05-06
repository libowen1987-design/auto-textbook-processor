"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter IV & V: Constant Magnetic Field & Ferromagnetism

Key results:
1. Magnetic susceptibility χ (tensor for anisotropic media)
   B = μ₀(H + M) = μ₀μ_r H
   For diamagnet: χ < 0, χ ~ -10^-5 to -10^-3
   For paramagnet: χ > 0, χ ~ 10^-5 to 10^-3
   For ferromagnet near Curie point: χ ∝ 1/(T - T_C) (Curie-Weiss law)

2. Demagnetization coefficients (Landau §27):
   For ellipsoid: H_inside = H_0 - N·M  (demagnetizing field)
   Sum rule: N_x + N_y + N_z = 1
   Sphere: N_x = N_y = N_z = 1/3
   Thin plate (field perp): N_z ≈ 1, N_x = N_y ≈ 0
   Long rod (field along axis): N_z ≈ 0, N_x = N_y ≈ 1/2

3. Ferromagnetism near Curie point (Landau §36):
   Below T_C: spontaneous magnetization M_s(T) ≈ M_0 √(1 - T/T_C)
   Magnetic susceptibility: χ = C / (T - T_C)  (Curie-Weiss)

Landau §30: Thermodynamic relations in magnetic field
Landau §31: Total free energy of magnetic substance
Landau §36: Ferromagnetics near the Curie point
"""

import numpy as np
import matplotlib.pyplot as plt

mu0 = 4 * np.pi * 1e-7  # H/m


def demagnetization_coefficients():
    """
    Compute demagnetization coefficients for ellipsoids.
    These are identical in form to the electrostatic depolarization coefficients.
    Landau §27.
    """
    def prolate_spheroid_N(a, b, n_pts=500):
        """Demagnetization for prolate spheroid (a > b = c)."""
        if a < b:
            a, b = b, a
        ratio = a / b
        ref_ratios = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 8.0, 10.0, 20.0, 1e10]
        ref_Nz = [1/3, 0.237, 0.173, 0.130, 0.100, 0.063, 0.044, 0.021, 0.014, 0.004, 0.0]
        ref_Nz = np.array(ref_Nz)
        ref_ratios = np.array(ref_ratios)
        if ratio <= 1.0:
            return 1/3, 1/3, 1/3
        N_z = np.interp(ratio, ref_ratios, ref_Nz)
        N_z = max(0.0, min(1.0, N_z))
        N_x = (1.0 - N_z) / 2.0
        return N_z, N_x, N_x
    
    # --- Demo values ---
    shapes = {
        'sphere':       (1.0, 1.0, 1.0),
        'prolate a/b=2': (2.0, 1.0, 1.0),
        'prolate a/b=5': (5.0, 1.0, 1.0),
        'flat disk':     (1.0, 1.0, 0.1),
        'long rod':     (10.0, 1.0, 1.0),
    }
    
    print("[landau_ch5] Demagnetization coefficients for various shapes:")
    for name, (a, b, c) in shapes.items():
        if a == b == c:
            print(f"  {name}: N_x={1/3:.4f}, N_y={1/3:.4f}, N_z={1/3:.4f}")
        else:
            # Prolate spheroid case
            n_z, n_x, n_y = prolate_spheroid_N(a, b)
            print(f"  {name}: N_z={n_z:.4f}, N_x={n_x:.4f}, N_y={n_y:.4f}  (sum={n_z+n_x+n_y:.4f})")


def demagnetization_field_demo():
    """Visualize demagnetization factor effect on internal field."""
    # For a sphere vs flat plate in uniform field
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Vary shape from sphere to flat plate
    aspect_ratios = np.linspace(0.1, 5.0, 100)
    n_z_vals = []
    for ar in aspect_ratios:
        n_z, n_x, n_y = demag_prolate(ar, 1.0)
        n_z_vals.append(n_z)
    
    ax = axes[0]
    ax.plot(aspect_ratios, n_z_vals, 'b-', lw=2)
    ax.axhline(1/3, color='k', ls=':', label='sphere limit')
    ax.axhline(0.0, color='r', ls='--', label='long rod limit')
    ax.axhline(1.0, color='g', ls='--', label='thin plate limit')
    ax.set_xlabel(r'Aspect ratio $a/b$')
    ax.set_ylabel(r'Demagnetization factor $N_z$ (along axis)')
    ax.set_title(r'Landau §27: Demagnetization factor $N_z$ for prolate spheroid')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.1, 5.0)
    ax.set_ylim(0, 1.05)
    
    # Internal field for magnetic sphere vs susceptibility
    chi_vals = np.logspace(-3, 3, 100)  # from diamagnetic to ferromagnetic
    H0 = 1e4  # A/m applied field
    
    # Sphere: N = 1/3
    N_sphere = 1/3
    H_in_sphere = H0 / (1 + N_sphere * chi_vals)
    M_sphere = chi_vals * H_in_sphere
    
    ax2 = axes[1]
    ax2.loglog(chi_vals, H_in_sphere, 'b-', lw=2, label=r'H_inside / H0 (sphere)')
    ax2.loglog(chi_vals, M_sphere, 'r--', lw=2, label=r'M (sphere)')
    ax2.axvline(1/0.01, color='k', ls=':', alpha=0.5, label='chi=100')
    ax2.set_xlabel(r'Magnetic susceptibility $\chi$')
    ax2.set_ylabel(r'Normalized field / M')
    ax2.set_title(r'Landau §27: Magnetic sphere: $H_{in} = H_0/(1 + N\chi)$')
    ax2.legend()
    ax2.grid(True, alpha=0.3, which='both')
    ax2.set_xlim(1e-3, 1e3)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch5_demagnetization.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print("[landau_ch5] Plot saved.")


def demag_prolate(a, b):
    """
    Demagnetization coefficients for prolate spheroid (Landau §27).
    Same as electrostatic depolarization factors.
    N_z: along major axis a; N_x = N_y = (1 - N_z)/2
    """
    if a < b:
        a, b = b, a
    ratio = a / b
    # Reference values from Landau tables for prolate spheroid (a > b, field along a)
    # Using the electrostatic depolarization values (same geometry factors)
    ref_ratios = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 8.0, 10.0, 20.0, 1e10]
    ref_Nz = [1/3, 0.237, 0.173, 0.130, 0.100, 0.063, 0.044, 0.021, 0.014, 0.004, 0.0]
    # Linear interpolation
    ref_Nz = np.array(ref_Nz)
    ref_ratios = np.array(ref_ratios)
    if ratio <= 1.0:
        return 1/3, 1/3, 1/3
    N_z = np.interp(ratio, ref_ratios, ref_Nz)
    N_z = max(0.0, min(1.0, N_z))
    N_x = (1.0 - N_z) / 2.0
    return N_z, N_x, N_x


def curie_weiss_law():
    """
    Curie-Weiss law for ferromagnet near Curie point.
    Landau §36:
      χ = C / (T - T_C)  for T > T_C
      M_s(T) ≈ M_0 √(1 - T/T_C)  for T < T_C (spontaneous magnetization)
    """
    T_C = 770  # K (approximate for iron)
    C = 1.0    # Curie constant (normalized)
    
    T = np.linspace(300, 1200, 200)
    
    # Susceptibility above Curie temperature
    chi = np.where(T > T_C, C / (T - T_C), np.nan)
    
    # Spontaneous magnetization below T_C (Landau theory)
    # M_s/M_0 = √(1 - T/T_C) for T < T_C
    t_norm = T / T_C
    M_s = np.where(T < T_C, np.sqrt(np.maximum(0, 1 - t_norm)), np.nan)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    ax = axes[0]
    valid = T > T_C
    ax.plot(T[valid], chi[valid], 'b-', lw=2)
    ax.axvline(T_C, color='k', ls='--', lw=1.5, label=f'$T_C$ = {T_C} K')
    ax.set_xlabel('T (K)')
    ax.set_ylabel(r'$\chi = C/(T - T_C)$')
    ax.set_title(r'Landau §36: Curie-Weiss susceptibility $\chi(T)$ for $T > T_C$')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(300, 1200)
    
    ax2 = axes[1]
    valid2 = T < T_C
    ax2.plot(T[valid2], M_s[valid2], 'r-', lw=2)
    ax2.plot(T[valid2], (1 - T[valid2]/T_C), 'g--', lw=1.5, label=r'Linear approx $1-T/T_C$')
    ax2.axvline(T_C, color='k', ls='--', lw=1.5, label=f'$T_C$ = {T_C} K')
    ax2.set_xlabel('T (K)')
    ax2.set_ylabel(r'$M_s(T)/M_0$')
    ax2.set_title(r'Landau §36: Spontaneous magnetization $M_s(T)$ below $T_C$')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(300, T_C)
    ax2.set_ylim(0, 1.05)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch5_ferromagnetism.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch5] Iron: T_C ≈ {T_C} K (simulated)")
    print("[landau_ch5] Plot saved.")


if __name__ == '__main__':
    demagnetization_coefficients()
    demagnetization_field_demo()
    curie_weiss_law()
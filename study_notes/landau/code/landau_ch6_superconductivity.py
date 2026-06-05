"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter VI: Superconductivity

Key results:
1. London equation (Landau §41, §42):
   ∇²B = B/λ_L²  where λ_L = √(m/μ₀n_s e²) is the London penetration depth
   
   For a superconductor in parallel field:
   B(x) = B₀ exp(-x/λ_L)  (Meissner effect)
   
2. Critical field (Landau §43):
   H_c(T) = H_c(0) · (1 - (T/T_C)²)  near T_C
   
3. Surface impedance of superconductor:
   R_s = (1/2) μ₀² ω δ / λ_L²  (Landau formula for clean superconductor)

4. Intermediate state (Landau §44):
   For H_c1 < H_0 < H_c2 in type-II: mixed state / flux tubes

λ_L typically ~ 50-500 nm for conventional superconductors.
"""

import numpy as np
import matplotlib.pyplot as plt

mu0 = 4 * np.pi * 1e-7


def london_penetration_depth(n_s=1e28, m=9.11e-31, e=1.6e-19):
    """
    Compute London penetration depth λ_L.
    
    λ_L = √(m / (μ₀ n_s e²))
    
    For n_s ~ 10²⁸ m⁻³ (typical metallic superconductor):
    λ_L ~ 30-200 nm
    """
    lamb_L = np.sqrt(m / (mu0 * n_s * e**2))
    return lamb_L


def meissner_effect(λ_L=100e-9, H0=1e4, n=300):
    """
    Display the Meissner effect: B(x) = B₀ exp(-x/λ_L).
    
    Landau §41: For a superconductor occupying x > 0, 
    in a parallel applied field H₀:
    B(x) = H₀ exp(-x/λ_L)
    
    The screening current density is:
    j_s(x) = -(H₀/λ_L) exp(-x/λ_L)
    """
    x = np.linspace(0, 5*λ_L, n)
    B = H0 * np.exp(-x / λ_L)
    j_s = -(H0 / λ_L) * np.exp(-x / λ_L)  # screening current
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(x * 1e9, B, 'b-', lw=2)
    ax.axhline(H0, color='r', ls='--', lw=1.5, label=r'$B_0 = \mu_0 H_0$ (applied)')
    ax.axvline(λ_L * 1e9, color='k', ls=':', label=f'$\\lambda_L$ = {λ_L*1e9:.0f} nm')
    ax.set_xlabel(r'Distance $x$ (nm)')
    ax.set_ylabel(r'Magnetic flux density $B(x)$ (T)')
    ax.set_title(r'Landau §41: Meissner effect - $B(x) = B_0 e^{-x/\lambda_L}$')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 5*λ_L*1e9)
    
    ax2 = axes[1]
    ax2.plot(x * 1e9, j_s * 1e-6, 'r-', lw=2)
    ax2.set_xlabel(r'Distance $x$ (nm)')
    ax2.set_ylabel(r'Screening current $j_s$ (MA/m$^2$)')
    ax2.set_title(r'Landau §42: Surface screening current $j_s(x)$')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 5*λ_L*1e9)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch6_meissner.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch6] λ_L = {λ_L*1e9:.1f} nm")
    print(f"[landau_ch6] Plot saved.")


def critical_field_and_intermediate_state():
    """
    Plot critical field H_c(T) and show intermediate state.
    
    Landau §43: H_c(T) = H_c(0) · [1 - (T/T_C)²]
    
    For type-I superconductor:
    - H < H_c: Meissner state (B=0 inside)
    - H > H_c: normal state
    - H ≈ H_c: intermediate state (alternating normal/superconducting lamellae)
    """
    H_c0 = 8e4  # A/m (for type-I, e.g. lead)
    T_C = 7.2   # K (lead)
    
    T = np.linspace(0, T_C, 200)
    H_c = H_c0 * (1 - (T/T_C)**2)
    H_c = np.maximum(H_c, 0)
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    ax = axes[0]
    ax.plot(T, H_c * 1e-3, 'b-', lw=2)
    ax.axvline(T_C, color='k', ls='--', lw=1.5)
    ax.set_xlabel(r'Temperature $T$ (K)')
    ax.set_ylabel(r'$H_c(T)$ (kA/m)')
    ax.set_title(rf'Landau §43: Critical field $H_c(T)$, $T_C$={T_C}K, $H_c(0)$={H_c0*1e-3:.0f}kA/m')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, T_C)
    ax.set_ylim(0, None)
    
    # Intermediate state structure
    ax2 = axes[1]
    # Show alternating lamellae (schematic)
    x = np.linspace(0, 10, 500)
    # Normal region when H_ext > H_c(T) * sin(πx/L) modulation
    H_ext = 0.7 * H_c0  # applied field
    H_local = H_ext * np.abs(np.sin(np.pi * x / 2))
    n_lamellae = 6
    pattern = np.tile([1, 0], n_lamellae)  # alternating S and N
    ax2.imshow([pattern], extent=[0, 10, 0, 1], aspect='auto', cmap='coolwarm',
               alpha=0.7)
    ax2.set_yticks([])
    ax2.set_xlabel(r'Distance $x$ ($\mu$m)')
    ax2.set_title(r'Landau §44: Intermediate state (alternating S/N lamellae)')
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch6_critical_field.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch6] Critical field at T=0: H_c(0) = {H_c0:.1f} kA/m")
    print(f"[landau_ch6] Plot saved.")


def london_equations_demo():
    """
    Compare penetration depth for different superconductor materials.
    """
    # Parameters for common superconductors
    materials = {
        'Al':  {'n_s': 6e28, 'm': 9.11e-31},
        'Pb':  {'n_s': 1.4e28, 'm': 9.11e-31},
        'Nb':  {'n_s': 5.6e28, 'm': 9.11e-31},
        'NbTi': {'n_s': 1e28, 'm': 9.11e-31},
    }
    
    lambdas = {}
    for name, params in materials.items():
        lambdas[name] = london_penetration_depth(**params)
    
    print("[landau_ch6] London penetration depths:")
    for name, lam in lambdas.items():
        print(f"  {name}: λ_L = {lam*1e9:.1f} nm")
    
    # Plot comparison
    fig, ax = plt.subplots(figsize=(8, 5))
    names = list(lambdas.keys())
    lams = [lambdas[n]*1e9 for n in names]
    bars = ax.bar(names, lams, color=['C0','C1','C2','C3'])
    ax.set_ylabel(r'London penetration depth $\lambda_L$ (nm)')
    ax.set_title('Landau §41: London penetration depth for different superconductors')
    ax.grid(True, alpha=0.3, axis='y')
    
    for bar, lam in zip(bars, lams):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{lam:.0f}', ha='center', va='bottom', fontsize=10)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch6_london_depths.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print("[landau_ch6] Plot saved.")


if __name__ == '__main__':
    λ = london_penetration_depth()
    print(f"[landau_ch6] λ_L (default n_s=1e28): {λ*1e9:.1f} nm")
    
    meissner_effect(λ_L=100e-9)
    critical_field_and_intermediate_state()
    london_equations_demo()
"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter II: Electrostatics of Dielectrics

Example 2: Effective dielectric constant of a mixture (Maxwell-Garnett).
(Landau §9)

For a dilute emulsion of spherical particles with permittivity ε_p
in a medium with permittivity ε_m, the effective permittivity is:

  ε_eff = ε_m + 3c·ε_m(ε_p - ε_m) / (ε_p + 2ε_m - c(ε_p - ε_m))

For c << 1 (dilute limit), this simplifies to:
  ε_eff ≈ ε_m [1 + 3c(ε_p - ε_m) / (ε_p + 2ε_m)]

Landau §9 gives the exact formula (9.5) for small Δε/ε:
  ε_mix ≈ ε - (1/3ε)(Δε)²
"""

import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.8541878128e-12


def maxwell_garnett(eps_m, eps_p, c):
    """
    Maxwell-Garnett effective medium formula for dilute mixture.
    
    Parameters:
        eps_m: permittivity of matrix (can be relative or absolute)
        eps_p: permittivity of particles (same units as eps_m)
        c:     volume fraction of particles (0 ≤ c < 1)
    
    Returns:
        eps_eff: effective permittivity of mixture
    """
    alpha = (eps_p - eps_m) / (eps_p + 2*eps_m)
    eps_eff = eps_m * (1 + 3*c*alpha) / (1 - c*alpha)
    return eps_eff


def bruggeman(eps_m, eps_p, c, tol=1e-10, max_iter=1000):
    """
    Bruggeman effective medium formula (self-consistent).
    
    c·(ε_p - ε_eff)/ε_eff + (1-c)·(ε_m - ε_eff)/ε_eff = 0
    → c·(ε_p - ε_eff) + (1-c)·(ε_m - ε_eff) = 0
    
    Actually the correct Bruggeman equation for dilute case:
    ε_eff = (1-c)·ε_m + c·ε_p   (Voigt-Reuss bounds)
    
    More accurately:
    c·(ε_p - ε_eff)·(ε_p + 2ε_eff) / (ε_p + 2ε_eff) + ... 
    = (1-c)·(ε_m - ε_eff)·(ε_m + 2ε_eff) / (ε_m + 2ε_eff) = 0
    
    Returns iterative solution.
    """
    eps_eff = (1-c)*eps_m + c*eps_p  # initial guess (Voigt upper bound)
    for _ in range(max_iter):
        f_p = (eps_p - eps_eff) / (eps_p + 2*eps_eff)
        f_m = (eps_m - eps_eff) / (eps_m + 2*eps_eff)
        eps_new = (c * eps_p * f_p + (1-c) * eps_m * f_m) / (c * f_p + (1-c) * f_m)
        if abs(eps_new - eps_eff) < tol:
            break
        eps_eff = eps_new
    return eps_eff


def mixing_formula_demo():
    """
    Demonstrate mixing formulas for water droplets (ε_p=80) in oil (ε_m=3).
    Volume fraction c varies from 0 to 0.5.
    """
    eps_water = 80.0   # water at low frequency
    eps_oil = 3.0
    
    c_vals = np.linspace(0, 0.5, 100)
    
    # Three bounds and estimates
    eps_upper = (1 - c_vals) * eps_oil + c_vals * eps_water     # Voigt (parallel)
    eps_lower = 1.0 / ((1 - c_vals)/eps_oil + c_vals/eps_water) # Reuss (series)
    
    eps_mg = np.array([maxwell_garnett(eps_oil, eps_water, c) for c in c_vals])
    eps_bg = np.array([bruggeman(eps_oil, eps_water, c) for c in c_vals])
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(c_vals * 100, eps_upper, 'r--', lw=2, label='Voigt upper bound')
    ax.plot(c_vals * 100, eps_lower, 'b--', lw=2, label='Reuss lower bound')
    ax.plot(c_vals * 100, eps_mg, 'k-', lw=2, label='Maxwell-Garnett')
    ax.plot(c_vals * 100, eps_bg, 'g-', lw=2, label='Bruggeman (iterative)')
    
    ax.set_xlabel('Volume fraction $c$ (%)')
    ax.set_ylabel(r'Effective permittivity $\varepsilon_{eff}$')
    ax.set_title('Landau §9: Effective permittivity of water-in-oil emulsion')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch2_mixture_eff.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    
    # Landau's result for small Δε/ε
    eps_avg = (eps_oil + eps_water) / 2
    Delta_eps = eps_water - eps_oil
    c_test = 0.1
    eps_lmu = eps_avg - (1/(3*eps_avg)) * (Delta_eps**2) * c_test
    print(f"[landau_ch2_mixture] For c={c_test}:")
    print(f"  Maxwell-Garnett: ε_eff = {maxwell_garnett(eps_oil, eps_water, c_test):.2f}")
    print(f"  Landau small-Δ approx: ε_eff ≈ {eps_lmu:.2f}")
    print(f"[landau_ch2_mixture] Plot saved.")


if __name__ == '__main__':
    mixing_formula_demo()
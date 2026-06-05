"""
第7章 - 矩形波导中TE/TM波的传播特性
Compute cutoff frequencies, propagation constants, and wave impedances.

From textbook (Section 7.2):
For rectangular waveguide with width a, height b (a > b):
TE_mn mode:
  Cutoff wave number: k_c = sqrt((m*pi/a)^2 + (n*pi/b)^2)
  Cutoff frequency: f_c = k_c / (2*pi*sqrt(mu*eps))
  Phase constant: beta = sqrt(k^2 - k_c^2), where k = omega*sqrt(mu*eps)
  Wave impedance: Z_TE = eta / cos(theta_c) = eta * k / beta
  where eta = sqrt(mu/eps), theta_c satisfies sin(theta_c) = k_c/k

TM_mn mode:
  Wave impedance: Z_TM = eta * cos(theta_c) = eta * beta / k

Dominant mode: TE_10 (lowest cutoff frequency for a > b)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, mu_0, pi

def intrinsic_impedance(mu_r=1.0, epsilon_r=1.0):
    eta_0 = np.sqrt(mu_0 / epsilon_0)
    return eta_0 * np.sqrt(mu_r / epsilon_r)

def k_c(m, n, a, b):
    """Cutoff wave number for TE/TM mode in rectangular waveguide"""
    return np.sqrt((m * pi / a)**2 + (n * pi / b)**2)

def f_c(m, n, a, b, mu_r=1.0, epsilon_r=1.0):
    """Cutoff frequency"""
    return k_c(m, n, a, b) / (2 * pi * np.sqrt(mu_r * mu_0 * epsilon_r * epsilon_0))

def cutoff_wavelength(m, n, a, b):
    """Cutoff wavelength: lambda_c = 2*pi / k_c"""
    return 2 * pi / k_c(m, n, a, b)

def beta(f, m, n, a, b, mu_r=1.0, epsilon_r=1.0):
    """Phase constant for propagating mode (f > f_c)"""
    k = 2 * pi * f * np.sqrt(mu_r * mu_0 * epsilon_r * epsilon_0)  # wave number in medium
    kc = k_c(m, n, a, b)
    return np.sqrt(k**2 - kc**2) if k > kc else 0.0

def Z_TE(f, m, n, a, b, mu_r=1.0, epsilon_r=1.0):
    """Wave impedance for TE_mn mode"""
    eta = intrinsic_impedance(mu_r, epsilon_r)
    k = 2 * pi * f * np.sqrt(mu_r * mu_0 * epsilon_r * epsilon_0)
    kc = k_c(m, n, a, b)
    if k <= kc:
        return None  # cutoff, evanescent
    b_val = np.sqrt(k**2 - kc**2)
    return eta * k / b_val

def Z_TM(f, m, n, a, b, mu_r=1.0, epsilon_r=1.0):
    """Wave impedance for TM_mn mode"""
    eta = intrinsic_impedance(mu_r, epsilon_r)
    k = 2 * pi * f * np.sqrt(mu_r * mu_0 * epsilon_r * epsilon_0)
    kc = k_c(m, n, a, b)
    if k <= kc:
        return None  # cutoff
    b_val = np.sqrt(k**2 - kc**2)
    return eta * b_val / k


if __name__ == "__main__":
    # Standard X-band waveguide: a=22.86mm, b=10.16mm
    a = 22.86e-3   # wide dimension
    b = 10.16e-3   # narrow dimension

    print(f"Waveguide: a={a*1000:.2f} mm, b={b*1000:.2f} mm")

    # Compute TE modes
    modes_TE = [(m, n) for m in range(5) for n in range(5) if (m, n) != (0, 0)]
    print("\n--- TE Modes ---")
    for m, n in modes_TE[:10]:
        fc = f_c(m, n, a, b)
        l_c = cutoff_wavelength(m, n, a, b) * 1000
        print(f"TE_{m}{n}: f_c={fc/1e9:.3f} GHz, lambda_c={l_c:.2f} mm")

    # Example from textbook: f = 10 GHz, a = 22.86 mm
    f = 10e9

    print("\n--- At f=10 GHz ---")
    print(f"Free-space lambda = {3e8/f*100:.2f} cm")

    for m, n in [(1,0), (2,0), (3,0), (0,1), (1,1), (0,2)]:
        fc = f_c(m, n, a, b) / 1e9
        l_c = cutoff_wavelength(m, n, a, b) * 1000
        z_te = Z_TE(f, m, n, a, b)
        print(f"TE_{m}{n}: f_c={fc:.2f} GHz, lambda_c={l_c:.2f} mm, "
              f"Z_TE={z_te:.1f} ohm" if z_te else f"TE_{m}{n}: f_c={fc:.2f} GHz (cutoff)")

    # Plot Z_TE for TE_10 mode vs frequency
    f_vals = np.linspace(5e9, 20e9, 500)
    Z_te10 = [Z_TE(f_val, 1, 0, a, b) for f_val in f_vals]
    f_c_10 = f_c(1, 0, a, b) / 1e9

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.axvline(x=f_c_10, color='k', linestyle='--', linewidth=0.8, label=r'$f_c(TE_{10})$')
    ax.plot(f_vals/1e9, Z_te10, 'b-', linewidth=1.5, label=r'$Z_{TE_{10}}$')
    ax.set_xlabel(r'$f$ (GHz)')
    ax.set_ylabel(r'$Z_{TE}$ (ohm)')
    ax.set_title(f'WG: a={a*1000:.1f}mm, b={b*1000:.1f}mm')
    ax.legend(); ax.grid(True, alpha=0.3)

    # Beta vs frequency for TE_10
    beta_10 = [beta(f_val, 1, 0, a, b) for f_val in f_vals]
    ax = axes[1]
    ax.axvline(x=f_c_10, color='k', linestyle='--', linewidth=0.8)
    ax.plot(f_vals/1e9, beta_10, 'r-', linewidth=1.5, label=r'$\beta_{10}$')
    ax.set_xlabel(r'$f$ (GHz)')
    ax.set_ylabel(r'$\beta$ (rad/m)')
    ax.set_title(r'$\beta$ for $TE_{10}$ mode')
    ax.legend(); ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch7_rectangular_waveguide.png', dpi=150)
    plt.show()
"""
第5章 例5.3.1 - 良导体中的趋肤深度与表面电阻
Compute skin depth and surface resistance for good conductors.

From textbook (Section 5.3):
Skin depth: delta_s = sqrt(2 / (omega * mu * sigma)) = sqrt(2 / (omega * mu_r * sigma))
  [in m]
Surface resistance: R_s = 1 / (sigma * delta_s) = sqrt(omega * mu / (2 * sigma))
  [in ohm]

Example from textbook: copper at f=3 MHz
  sigma_Cu = 5.8e7 S/m, mu_r = 1
  delta_s = sqrt(2 / (2*pi*3e6 * 4*pi*1e-7 * 5.8e7))
           = sqrt(2 / (2*pi*3e6 * 4*pi*1e-7 * 5.8e7))
           = 2.62e-5 m = 26.2 um
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, pi

def skin_depth(f, sigma, mu_r=1.0):
    """
    Compute skin depth in a good conductor.

    Parameters
    ----------
    f : float
        Frequency (Hz)
    sigma : float
        Conductivity (S/m)
    mu_r : float
        Relative permeability

    Returns
    -------
    delta_s : float
        Skin depth (m)
    """
    mu = mu_r * mu_0
    omega = 2 * pi * f
    delta_s = np.sqrt(2.0 / (omega * mu * sigma))
    return delta_s

def surface_resistance(f, sigma, mu_r=1.0):
    """
    Compute surface resistance (ohms per square).

    Parameters
    ----------
    f : float
        Frequency (Hz)
    sigma : float
        Conductivity (S/m)
    mu_r : float
        Relative permeability

    Returns
    -------
    R_s : float
        Surface resistance (ohm)
    """
    mu = mu_r * mu_0
    omega = 2 * pi * f
    R_s = np.sqrt(omega * mu / (2.0 * sigma))
    return R_s


if __name__ == "__main__":
    sigma_Cu = 5.8e7    # S/m (copper)
    sigma_Al = 3.5e7    # S/m (aluminum)
    sigma_seawater = 4.0  # S/m (typical seawater)

    f_vals = np.logspace(6, 10, 500)  # 1 MHz to 10 GHz

    delta_Cu = [skin_depth(f, sigma_Cu) for f in f_vals]
    delta_Al = [skin_depth(f, sigma_Al) for f in f_vals]

    Rs_Cu = [surface_resistance(f, sigma_Cu) for f in f_vals]
    Rs_Al = [surface_resistance(f, sigma_Al) for f in f_vals]

    print("=== Skin Depth Example (Textbook) ===")
    f_ex = 3e6
    ds_Cu = skin_depth(f_ex, sigma_Cu)
    Rs_Cu_ex = surface_resistance(f_ex, sigma_Cu)
    print(f"Copper at f=3 MHz:")
    print(f"  skin depth = {ds_Cu*1e6:.2f} um")
    print(f"  surface resistance = {Rs_Cu_ex:.4f} ohm")

    ds_Al = skin_depth(f_ex, sigma_Al)
    Rs_Al_ex = surface_resistance(f_ex, sigma_Al)
    print(f"Aluminum at f=3 MHz:")
    print(f"  skin depth = {ds_Al*1e6:.2f} um")
    print(f"  surface resistance = {Rs_Al_ex:.4f} ohm")

    # Plot
    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.loglog(f_vals/1e6, np.array(delta_Cu)*1e6, 'b-', linewidth=1.5, label='Cu')
    ax.loglog(f_vals/1e6, np.array(delta_Al)*1e6, 'r--', linewidth=1.5, label='Al')
    ax.set_xlabel(r'$f$ (MHz)')
    ax.set_ylabel(r'$\delta_s$ ($\mu$m)')
    ax.set_title('Skin depth vs frequency')
    ax.legend(); ax.grid(True, alpha=0.3, which='both')

    ax = axes[1]
    ax.loglog(f_vals/1e6, Rs_Cu, 'b-', linewidth=1.5, label='Cu')
    ax.loglog(f_vals/1e6, Rs_Al, 'r--', linewidth=1.5, label='Al')
    ax.set_xlabel(r'$f$ (MHz)')
    ax.set_ylabel(r'$R_s$ (ohm)')
    ax.set_title('Surface resistance vs frequency')
    ax.legend(); ax.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch5_skin_depth.png', dpi=150)
    plt.show()
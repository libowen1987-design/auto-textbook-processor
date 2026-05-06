"""
第2章 例2.2.2 - 均匀带电环形薄圆盘轴线上任意点的电场强度
Compute the electric field on the axis of a uniformly charged annular disk.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants from scipy.constants
from scipy.constants import epsilon_0, pi

def electric_field_annular_disk(rho_inner, rho_outer, sigma_ps, z):
    """
    Compute E-field on-axis for uniformly charged annular disk.

    Parameters
    ----------
    rho_inner : float
        Inner radius (m)
    rho_outer : float
        Outer radius (m)
    sigma_ps : float
        Surface charge density (C/m^2)
    z : float or array
        Axial distance (m)

    Returns
    -------
    E_z : float or array
        Electric field (V/m), z-component
    """
    # Result from direct integration:
    # E_z = (sigma_ps / (2 * epsilon_0)) * (1 - z / sqrt(z^2 + rho_outer^2))
    #       - (sigma_ps / (2 * epsilon_0)) * (1 - z / sqrt(z^2 + rho_inner^2))
    #     = (sigma_ps / (2 * epsilon_0)) * (z / sqrt(z^2 + rho_inner^2) - z / sqrt(z^2 + rho_outer^2))
    # For the special case where rho_inner = 0 (solid disk):
    # E_z = (sigma_ps / (2 * epsilon_0)) * (1 - z / sqrt(z^2 + rho_outer^2))
    # Note: The formula in the book uses ps (sigma) as surface charge density.

    z = np.asarray(z, dtype=float)
    term_outer = z / np.sqrt(z**2 + rho_outer**2)
    term_inner = z / np.sqrt(z**2 + rho_inner**2)
    E_z = (sigma_ps / (2 * epsilon_0)) * (term_inner - term_outer)
    return E_z


if __name__ == "__main__":
    # Example from textbook: annular disk with inner radius a, outer radius b,
    # surface charge density ps (sigma_ps), axis point P(0,0,z)

    a = 0.05   # inner radius 5 cm
    b = 0.10   # outer radius 10 cm
    sigma_ps = 1e-6  # surface charge density C/m^2

    z_vals = np.linspace(0.01, 0.5, 500)  # 1cm to 50cm
    E_z = electric_field_annular_disk(a, b, sigma_ps, z_vals)

    # Plot
    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z_vals * 100, E_z / 1e3, 'b-', linewidth=1.5, label=r'$E_z$')
    ax.set_xlabel(r'$z$ (cm)')
    ax.set_ylabel(r'$E_z$ (kV/m)')
    ax.set_title(f'Annular disk: $a={a*100:.0f}$ cm, $b={b*100:.0f}$ cm, '
                 r'$\sigma_{ps}=$' + f'{sigma_ps:.0e} C/m$^2$')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch2_annular_disk_Efield.png', dpi=150)
    plt.show()

    print("E_z at z=10cm:", electric_field_annular_disk(a, b, sigma_ps, 0.10) / 1e3, "kV/m")
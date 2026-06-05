"""
第3章 例3.1.5 - 同轴线单位长度的电容
Compute capacitance per unit length of a coaxial cable.

From textbook: coaxial cylinder with inner radius a, outer radius b,
filled with uniform dielectric (epsilon_r). Unit length capacitance:
C = 2*pi*epsilon_0*epsilon_r / ln(b/a)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, pi

def capacitance_coaxial(a, b, epsilon_r):
    """
    Compute capacitance per unit length of coaxial cable.

    Parameters
    ----------
    a : float
        Inner conductor radius (m)
    b : float
        Outer conductor inner radius (m)
    epsilon_r : float
        Relative permittivity of dielectric

    Returns
    -------
    C : float
        Capacitance per unit length (F/m)
    """
    return (2 * pi * epsilon_0 * epsilon_r) / np.log(b / a)


def electric_field_coaxial(r, a, b, U_0, epsilon_r):
    """
    Electric field in coaxial cable at radius r (a < r < b).
    E_r = U_0 / (r * ln(b/a))
    """
    return U_0 / (r * np.log(b / a))


def voltage_coaxial(a, b, U_0, epsilon_r):
    """Verify voltage distribution."""
    return U_0  # integral of E from a to b gives U_0


if __name__ == "__main__":
    a = 0.5e-3   # 0.5 mm inner radius
    b = 1.75e-3  # 1.75 mm outer radius
    epsilon_r = 2.1  # polyethylene
    U_0 = 100.0  # 100 V between conductors

    C = capacitance_coaxial(a, b, epsilon_r)
    print(f"Coaxial cable capacitance per unit length: {C*1e12:.2f} pF/m")

    # Plot E-field distribution
    r_vals = np.linspace(a * 1.01, b * 0.99, 300)
    E_r = electric_field_coaxial(r_vals, a, b, U_0, epsilon_r)

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(r_vals * 1e6, E_r / 1e3, 'b-', linewidth=1.5)
    ax.set_xlabel(r'$r$ ($\mu$m)')
    ax.set_ylabel(r'$E_r$ (kV/m)')
    ax.set_title(f'Coaxial cable E-field: $a$={a*1e6:.1f} µm, $b$={b*1e6:.1f} µm')
    ax.grid(True, alpha=0.3)

    # Plot capacitance vs epsilon_r
    eps_vals = np.linspace(1, 10, 200)
    C_vals = [capacitance_coaxial(a, b, er) * 1e12 for er in eps_vals]
    ax = axes[1]
    ax.plot(eps_vals, C_vals, 'r-', linewidth=1.5)
    ax.set_xlabel(r'$\epsilon_r$')
    ax.set_ylabel(r'$C$ (pF/m)')
    ax.set_title('Coaxial C vs $\epsilon_r$')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch3_coaxial_capacitance.png', dpi=150)
    plt.show()
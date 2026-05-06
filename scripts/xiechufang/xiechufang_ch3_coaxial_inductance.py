"""
第3章 例3.3.3 - 同轴线单位长度的电感
Compute inductance per unit length of coaxial cable.

From textbook (Eq 3.3.36): L = (mu_0 / (8*pi)) + (mu_0 / (2*pi)) * ln(b/a)
(The total L = L_inner + L_outer)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, pi

def inductance_coaxial(a, b, mu_r=1.0):
    """
    Compute inductance per unit length of coaxial cable.

    Parameters
    ----------
    a : float
        Inner conductor radius (m)
    b : float
        Outer conductor inner radius (m)
    mu_r : float
        Relative permeability of medium

    Returns
    -------
    L : float
        Inductance per unit length (H/m)
        L = L_inner + L_outer = mu_0/(8*pi) + mu_0/(2*pi)*ln(b/a)
    """
    mu = mu_r * mu_0
    L_inner = mu / (8 * pi)   # internal inductance
    L_outer = (mu / (2 * pi)) * np.log(b / a)  # external inductance
    return L_inner + L_outer


if __name__ == "__main__":
    a = 0.5e-3   # 0.5 mm
    b = 1.75e-3  # 1.75 mm

    L = inductance_coaxial(a, b)
    print(f"Coaxial cable inductance per unit length: {L*1e6:.3f} µH/m")

    # Plot L vs ratio b/a
    ratio_vals = np.linspace(1.5, 10, 300)
    L_vals = [inductance_coaxial(a, a * r) * 1e6 for r in ratio_vals]

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(ratio_vals, L_vals, 'b-', linewidth=1.5)
    ax.set_xlabel(r'$b/a$ (radius ratio)')
    ax.set_ylabel(r'$L$ ($\mu$H/m)')
    ax.set_title(f'Coaxial cable inductance: $a$={a*1e3:.1f} mm, $\mu_r=1$')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch3_coaxial_inductance.png', dpi=150)
    plt.show()
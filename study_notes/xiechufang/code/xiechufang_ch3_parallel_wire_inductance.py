"""
第3章 例3.3.4 - 平行双线传输线单位长度的电感
Compute inductance per unit length of parallel-wire transmission line.

From textbook (Eq 3.3.37):
L = (mu_0/pi) * [ (1/8) + (1/4)*ln(D/a) ]   [H/m]
where a = wire radius, D = center-to-center distance

For D >> a: L ≈ (mu_0/pi) * ln(D/a)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, pi

def inductance_parallel_wire(a, D, mu_r=1.0):
    """
    Compute inductance per unit length of parallel-wire line.

    Parameters
    ----------
    a : float
        Wire radius (m)
    D : float
        Center-to-center spacing (m), must have D > 2*a
    mu_r : float
        Relative permeability

    Returns
    -------
    L : float
        Inductance per unit length (H/m)
    """
    mu = mu_r * mu_0
    L = (mu / pi) * (0.125 + 0.25 * np.log(D / a))
    return L


if __name__ == "__main__":
    # Typical values: wire radius 1mm, spacing 10mm
    a = 1.0e-3    # 1 mm radius
    D_vals = np.linspace(3 * a, 50 * a, 500)  # spacing from 3mm to 50mm

    L_vals = [inductance_parallel_wire(a, D) * 1e6 for D in D_vals]

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(D_vals * 1000, L_vals, 'b-', linewidth=1.5)
    ax.set_xlabel(r'$D$ (mm)')
    ax.set_ylabel(r'$L$ ($\mu$H/m)')
    ax.set_title(f'Parallel-wire line: $a$={a*1000:.1f} mm')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch3_parallel_wire_inductance.png', dpi=150)
    plt.show()

    # Example computation
    D = 10e-3  # 10 mm spacing
    L = inductance_parallel_wire(a, D)
    print(f"Parallel-wire L (D={D*1000:.0f}mm, a={a*1000:.1f}mm): {L*1e6:.3f} µH/m")
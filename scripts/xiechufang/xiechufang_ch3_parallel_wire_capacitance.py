"""
第3章 例3.1.4 - 平行双线传输线的电容
Compute capacitance per unit length of parallel-wire transmission line.

From textbook (Eq 3.1.26):
C = pi*epsilon_0*epsilon_r / arccosh(D/(2*a))
  = (pi*epsilon_0*epsilon_r) / ln(D/(2*a) + sqrt((D/(2*a))^2 - 1))
For D >> a: C ≈ pi*epsilon_0*epsilon_r / ln(D/a)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, pi

def capacitance_parallel_wire(a, D, epsilon_r=1.0):
    """
    Compute capacitance per unit length of parallel-wire line.

    Parameters
    ----------
    a : float
        Wire radius (m)
    D : float
        Center-to-center spacing (m)
    epsilon_r : float
        Relative permittivity of surrounding medium

    Returns
    -------
    C : float
        Capacitance per unit length (F/m)
    """
    # arccosh(x) = ln(x + sqrt(x^2 - 1))
    x = D / (2.0 * a)
    acosh_x = np.log(x + np.sqrt(x**2 - 1))
    C = (pi * epsilon_0 * epsilon_r) / acosh_x
    return C


def capacitance_parallel_wire_approx(a, D, epsilon_r=1.0):
    """
    Approximate capacitance for D >> a: C ≈ pi*epsilon_0*epsilon_r / ln(D/a)
    """
    return (pi * epsilon_0 * epsilon_r) / np.log(D / a)


if __name__ == "__main__":
    a = 1.0e-3   # 1 mm wire radius
    epsilon_r = 2.3  # typical PE insulation

    D_vals = np.linspace(3 * a, 50 * a, 300)
    C_vals = [capacitance_parallel_wire(a, D, epsilon_r) * 1e12 for D in D_vals]  # pF/m
    C_approx = [capacitance_parallel_wire_approx(a, D, epsilon_r) * 1e12 for D in D_vals]

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(D_vals * 1000, C_vals, 'b-', linewidth=1.5, label='Exact')
    ax.plot(D_vals * 1000, C_approx, 'r--', linewidth=1.5, label=r'Approx: $\ln(D/a)$')
    ax.set_xlabel(r'$D$ (mm)')
    ax.set_ylabel(r'$C$ (pF/m)')
    ax.set_title(f'Parallel-wire capacitance: $a$={a*1000:.1f} mm, $\epsilon_r=${epsilon_r}')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch3_parallel_wire_capacitance.png', dpi=150)
    plt.show()

    # Example computation
    D = 10e-3  # 10 mm
    C = capacitance_parallel_wire(a, D, epsilon_r)
    print(f"Parallel-wire C (D={D*1000:.0f}mm, a={a*1000:.1f}mm): {C*1e12:.3f} pF/m")
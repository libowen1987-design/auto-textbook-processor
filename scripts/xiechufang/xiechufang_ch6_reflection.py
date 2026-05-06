"""
第6章 - 均匀平面波对介质分界面的垂直入射：反射系数与透射系数
Compute reflection and transmission coefficients for normal incidence.

From textbook (Section 6.2):
For normal incidence from medium 1 (eta_1) to medium 2 (eta_2):
- Reflection coefficient: Gamma = (eta_2 - eta_1) / (eta_2 + eta_1)
- Transmission coefficient: Tau = 2*eta_2 / (eta_2 + eta_1)
  (for E field; for H field: tau_H = 2*eta_1 / (eta_2 + eta_1))

Example: Air (eta_1=377) to dielectric (epsilon_r=4) => eta_2=188.5 ohm
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, mu_0

def intrinsic_impedance(mu_r=1.0, epsilon_r=1.0):
    """Intrinsic impedance of medium: eta = sqrt(mu/mu0 / eps/eps0) * eta_0"""
    eta_0 = np.sqrt(mu_0 / epsilon_0)  # ~377 ohm
    return eta_0 * np.sqrt(mu_r / epsilon_r)

def reflection_coefficient(eta_1, eta_2):
    """Reflection coefficient for E field at normal incidence"""
    return (eta_2 - eta_1) / (eta_2 + eta_1)

def transmission_coefficient_E(eta_1, eta_2):
    """Transmission coefficient for E field at normal incidence"""
    return 2 * eta_2 / (eta_2 + eta_1)

def transmission_coefficient_H(eta_1, eta_2):
    """Transmission coefficient for H field at normal incidence"""
    return 2 * eta_1 / (eta_2 + eta_1)


def standing_wave(E_i, Gamma, z, beta):
    """
    Total field for normal incidence with reflection.
    E_total(z) = E_i * exp(-j*beta*z) + Gamma * E_i * exp(j*beta*z)
    Instantaneous: E(z,t) = E_i * [cos(omega*t - beta*z) + Gamma * cos(omega*t + beta*z)]
    """
    return E_i * (np.cos(-beta * z) + Gamma * np.cos(beta * z))


if __name__ == "__main__":
    eta_0 = np.sqrt(mu_0 / epsilon_0)  # free space impedance ~377 ohm

    # Example: air to dielectric (epsilon_r=4), normal incidence
    eta_1 = eta_0                    # air: eta_1 = 377 ohm
    eta_2 = intrinsic_impedance(epsilon_r=4.0)  # dielectric: eta_2 = 188.5 ohm

    Gamma = reflection_coefficient(eta_1, eta_2)
    Tau_E = transmission_coefficient_E(eta_1, eta_2)
    Tau_H = transmission_coefficient_H(eta_1, eta_2)

    print(f"Medium 1 (air): eta_1 = {eta_1:.2f} ohm")
    print(f"Medium 2 (eps_r=4): eta_2 = {eta_2:.2f} ohm")
    print(f"Reflection coefficient Gamma = {Gamma:.4f}")
    print(f"Transmission coefficient Tau_E = {Tau_E:.4f}")
    print(f"Transmission coefficient Tau_H = {Tau_H:.4f}")

    # Plot reflection coefficient vs epsilon_r
    eps_r_vals = np.linspace(1, 20, 300)
    Gamma_vals = [reflection_coefficient(eta_0, intrinsic_impedance(epsilon_r=er)) for er in eps_r_vals]

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(eps_r_vals, Gamma_vals, 'b-', linewidth=1.5)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.set_xlabel(r'$\epsilon_{r2}$')
    ax.set_ylabel(r'$\Gamma$')
    ax.set_title(r'Reflection coefficient: air $\to$ dielectric')
    ax.grid(True, alpha=0.3)

    # Standing wave pattern
    z_vals = np.linspace(-5e-2, 5e-2, 500)
    beta = 2 * np.pi / 0.03  # at some frequency
    E0 = 100.0

    # At t=0
    E_total = E0 * (np.cos(-beta * z_vals) + Gamma * np.cos(beta * z_vals))

    ax = axes[1]
    ax.plot(z_vals * 100, E_total, 'b-', linewidth=1.5)
    ax.set_xlabel(r'$z$ (cm)')
    ax.set_ylabel(r'$E_{total}$ (V/m)')
    ax.set_title(rf'Standing wave: $\Gamma$={Gamma:.3f}')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch6_reflection_transmission.png', dpi=150)
    plt.show()
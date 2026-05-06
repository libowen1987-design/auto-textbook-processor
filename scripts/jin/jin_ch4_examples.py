"""
jin_ch4_examples.py
Jin CEM 2nd Ed., Chapter 4: Transmission Lines & Plane Waves
Examples: TL impedance transform, plane wave propagation, Fresnel reflection,
Brewster angle, polarization visualization.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
eta_0 = np.sqrt(mu_0 / epsilon_0)
pi = np.pi


def transmission_line_impedance():
    """
    Input impedance of a transmission line terminated in Z_L.
    Demonstrate quarter-wave and half-wave transformers.
    """
    Z_0 = 50.0  # Ohm
    Z_L = 100.0  # Ohm
    beta_l = np.linspace(0, 2 * pi, 400)  # electrical length
    
    Z_in = Z_0 * (Z_L + 1j * Z_0 * np.tan(beta_l)) / \
                 (Z_0 + 1j * Z_L * np.tan(beta_l))
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
    ax1.plot(beta_l / pi, np.abs(Z_in), 'b-', linewidth=1.2)
    ax1.set_ylabel("$|Z_{\\text{in}}|$ (Ohm)", fontsize=11)
    ax1.axhline(Z_0, color='gray', linestyle='--', alpha=0.5, label='$Z_0$')
    ax1.axvline(0.5, color='r', linestyle=':', alpha=0.5, label='$\\lambda/4$')
    ax1.axvline(1.0, color='g', linestyle=':', alpha=0.5, label='$\\lambda/2$')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_title("Transmission Line Input Impedance ($Z_L = 100\\,\\Omega$, $Z_0=50\\,\\Omega$)", 
                  fontsize=11)
    
    ax2.plot(beta_l / pi, np.angle(Z_in, deg=True), 'r-', linewidth=1.2)
    ax2.set_xlabel("Line Length $\\ell/\\lambda$", fontsize=11)
    ax2.set_ylabel("Phase (deg)", fontsize=11)
    ax2.axvline(0.5, color='r', linestyle=':', alpha=0.5)
    ax2.axvline(1.0, color='g', linestyle=':', alpha=0.5)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch4_fig_TL.png",
                dpi=150)
    plt.close()
    print("[OK] TL impedance plot saved.")
    
    print("=" * 55)
    print("Transmission Line: Input Impedance")
    print("=" * 55)
    print(f"  Z_0 = {Z_0:.1f} Ohm, Z_L = {Z_L:.1f} Ohm")
    print(f"  lambda/4: Z_in = Z_0^2/Z_L = {Z_0**2/Z_L:.1f} Ohm (transform)")
    print(f"  lambda/2: Z_in = Z_L = {Z_L:.1f} Ohm (repeats)")
    print()


def plane_wave_attenuation():
    """Plane wave attenuation in a lossy medium (sigma > 0)."""
    freq = 1e9  # 1 GHz
    omega = 2 * pi * freq
    epsilon_r_values = [1, 10, 80]  # air, dry soil, water
    sigma_values = [0, 0.01, 4]  # S/m
    
    z = np.linspace(0, 10, 500)  # meters
    
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    for eps_r, sigma, color, ls in zip(
        epsilon_r_values, sigma_values,
        ['b', 'orange', 'g'], ['-', '--', '-.']):
        
        epsilon_c = epsilon_0 * eps_r * (1 - 1j * sigma / (omega * epsilon_0 * eps_r))
        mu = mu_0
        gamma = 1j * omega * np.sqrt(mu * epsilon_c)
        alpha = np.real(gamma)
        beta = np.imag(gamma)
        skin_depth = 1 / alpha if alpha > 0 else np.inf
        
        E_z = np.exp(-alpha * z) * np.cos(omega * 0 - beta * z)
        E_env = np.exp(-alpha * z)
        
        label = f"$\\epsilon_r={eps_r}$, $\\sigma={sigma}$ S/m, $\\delta={skin_depth:.2f}$ m"
        ax.plot(z, E_env, color=color, linestyle=ls, linewidth=1.5, label=label)
    
    ax.set_xlabel("Distance (m)", fontsize=11)
    ax.set_ylabel("$|E|$ envelope (normalized)", fontsize=11)
    ax.set_title("Plane Wave Attenuation in Lossy Media (1 GHz)", fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch4_fig_atten.png",
                dpi=150)
    plt.close()
    print("[OK] Plane wave attenuation plot saved.")


def fresnel_reflection():
    """Fresnel reflection and transmission at a planar interface."""
    epsilon_r1 = 1.0  # air
    epsilon_r2 = 4.0  # dielectric
    
    eta_1 = eta_0 / np.sqrt(epsilon_r1)
    eta_2 = eta_0 / np.sqrt(epsilon_r2)
    
    theta_i = np.linspace(0, pi/2 - 0.001, 361)
    
    # Snell's law
    n1 = np.sqrt(epsilon_r1)
    n2 = np.sqrt(epsilon_r2)
    theta_t = np.arcsin(np.minimum(n1/n2 * np.sin(theta_i), 0.999))
    
    # TE (perpendicular)
    R_te = np.abs((eta_2 * np.cos(theta_i) - eta_1 * np.cos(theta_t)) /
                  (eta_2 * np.cos(theta_i) + eta_1 * np.cos(theta_t)))**2
    T_te = 1 - R_te
    
    # TM (parallel)
    R_tm = np.abs((eta_2 * np.cos(theta_t) - eta_1 * np.cos(theta_i)) /
                  (eta_2 * np.cos(theta_t) + eta_1 * np.cos(theta_i)))**2
    T_tm = 1 - R_tm
    
    # Brewster angle (TM zero)
    theta_B = np.arctan(np.sqrt(epsilon_r2 / epsilon_r1))
    
    # Critical angle
    theta_c = np.arcsin(np.sqrt(epsilon_r1 / epsilon_r2))
    
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(np.degrees(theta_i), R_te, 'b-', linewidth=1.5, label='TE (R)')
    ax.plot(np.degrees(theta_i), T_te, 'b--', linewidth=1.2, label='TE (T)')
    ax.plot(np.degrees(theta_i), R_tm, 'r-', linewidth=1.5, label='TM (R)')
    ax.plot(np.degrees(theta_i), T_tm, 'r--', linewidth=1.2, label='TM (T)')
    
    ax.axvline(np.degrees(theta_B), color='g', linestyle=':', alpha=0.7,
               label=f'Brewster={np.degrees(theta_B):.1f}$^\\circ$')
    ax.axvline(np.degrees(theta_c), color='orange', linestyle=':', alpha=0.7,
               label=f'Critical={np.degrees(theta_c):.1f}$^\\circ$')
    
    ax.set_xlabel("Incidence Angle $\\theta_i$ (deg)", fontsize=11)
    ax.set_ylabel("Power Coefficient", fontsize=11)
    ax.set_title(f"Fresnel Reflection/Transmission ($\\epsilon_{{r1}}=1 \\to \\epsilon_{{r2}}={epsilon_r2}$)",
                 fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.05)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch4_fig_fresnel.png",
                dpi=150)
    plt.close()
    print("[OK] Fresnel reflection plot saved.")


def polarization_visualization():
    """Visualize linear, circular, and elliptical polarization."""
    t = np.linspace(0, 2 * pi, 200)
    
    fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
    
    # Linear (45 deg)
    Ex_l = np.cos(t)
    Ey_l = np.cos(t)  # same phase
    axes[0].plot(Ex_l, Ey_l, 'b-', linewidth=1.5)
    axes[0].set_title("Linear Polarization", fontsize=11)
    axes[0].set_xlabel("$E_x$", fontsize=10)
    axes[0].set_ylabel("$E_y$", fontsize=10)
    axes[0].axis('equal')
    axes[0].set_xlim(-1.3, 1.3)
    axes[0].set_ylim(-1.3, 1.3)
    axes[0].grid(True, alpha=0.3)
    
    # Circular (RHCP)
    Ex_c = np.cos(t)
    Ey_c = np.sin(t)  # 90 deg phase lag -> RHCP (for wave traveling toward viewer)

    axes[1].plot(Ex_c, Ey_c, 'r-', linewidth=1.5)
    axes[1].set_title("Circular Polarization (RHCP)", fontsize=11)
    axes[1].set_xlabel("$E_x$", fontsize=10)
    axes[1].set_ylabel("$E_y$", fontsize=10)
    axes[1].axis('equal')
    axes[1].set_xlim(-1.3, 1.3)
    axes[1].set_ylim(-1.3, 1.3)
    axes[1].grid(True, alpha=0.3)
    
    # Elliptical
    Ex_e = np.cos(t)
    Ey_e = 0.5 * np.cos(t + pi/4)
    axes[2].plot(Ex_e, Ey_e, 'g-', linewidth=1.5)
    axes[2].set_title("Elliptical Polarization", fontsize=11)
    axes[2].set_xlabel("$E_x$", fontsize=10)
    axes[2].set_ylabel("$E_y$", fontsize=10)
    axes[2].axis('equal')
    axes[2].set_xlim(-1.3, 1.3)
    axes[2].set_ylim(-1.3, 1.3)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch4_fig_polarization.png",
                dpi=150)
    plt.close()
    print("[OK] Polarization visualization saved.")


def main():
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   Jin CEM 2nd Ed. — Ch4 Example Code               ║")
    print("║   Transmission Lines and Plane Waves               ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()
    
    transmission_line_impedance()
    plane_wave_attenuation()
    fresnel_reflection()
    polarization_visualization()
    
    print("All Ch4 examples completed successfully.")

if __name__ == "__main__":
    main()

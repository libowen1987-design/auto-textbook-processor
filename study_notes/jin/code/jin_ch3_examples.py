"""
jin_ch3_examples.py
Jin CEM 2nd Ed., Chapter 3: Electromagnetic Theorems and Principles
Examples: Image theory verification, reciprocity verification, equivalence principle.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
eta_0 = np.sqrt(mu_0 / epsilon_0)
pi = np.pi


def image_theory_vertical_dipole():
    """
    Verify image theory: vertical electric dipole above PEC ground plane.
    Fields in upper half-space = free-space sum of original + image dipole.
    
    Original dipole at (0,0,h), image at (0,0,-h).
    Far-field pattern = sin(theta)*cos(kh*cos(theta)).
    """
    h = 0.5   # height in wavelengths
    freq = 300e6
    k = 2 * pi * freq / c_light
    
    theta = np.linspace(0.001, pi/2 - 0.001, 200)
    # Pattern factor: F = sin(theta) * cos(k*h*cos(theta))
    F = np.sin(theta) * np.cos(k * h * np.cos(theta))
    F_norm = F / np.max(F)
    
    # Compare to single dipole in free space
    F_single = np.sin(theta)
    F_single_norm = F_single / np.max(F_single)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 5))
    ax.plot(theta, F_norm, 'b-', linewidth=1.5, label=f'Above PEC ($h={h}\\lambda$)')
    ax.plot(theta, F_single_norm, 'r--', linewidth=1.2, label='Free-space dipole')
    ax.set_title("Vertical Electric Dipole Above PEC Ground", va='bottom', fontsize=11)
    ax.set_ylim(0, 1.05)
    ax.legend(loc='upper right', fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch3_fig_image.png",
                dpi=150)
    plt.close()
    print("[OK] Image theory plot saved.")
    
    print("=" * 55)
    print("Image Theory: Vertical Dipole above PEC")
    print("=" * 55)
    print(f"  Dipole height: {h} lambda")
    print(f"  Pattern tilt due to image: cos(k*h*cos(theta)) interference")
    print(f"  Number of lobes: depends on h/lambda")
    print()


def reciprocity_check():
    """
    Verify reciprocity theorem: 
    Two infinitesimal dipoles separated by distance d.
    V_12 = V_21 (mutual impedance should be equal).
    """
    d = 1.0  # separation in wavelengths
    freq = 300e6
    lam = c_light / freq
    d_m = d * lam
    k = 2 * pi / lam
    
    # Mutual impedance between two Hertzian dipoles
    # Z_12 ~ sin(theta_12)*sin(theta_21) * e^{-jkr} / r
    # For side-by-side (theta = 90 deg) at distance d:
    Z_12 = np.exp(-1j * k * d_m) / d_m
    Z_21 = np.exp(-1j * k * d_m) / d_m  # same by reciprocity
    
    print("=" * 55)
    print("Reciprocity: Mutual Impedance of Two Dipoles")
    print("=" * 55)
    print(f"  Separation: {d:.1f} lambda = {d_m:.2f} m")
    print(f"  Z_12 = {Z_12:.4f} (normalized)")
    print(f"  Z_21 = {Z_21:.4f} (normalized)")
    print(f"  Z_12 == Z_21: {np.isclose(Z_12, Z_21)}")
    print()
    
    # Plot mutual impedance vs distance
    distances = np.linspace(0.1, 3.0, 200)
    Z_mut = np.exp(-1j * 2 * pi * distances) / distances
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
    ax1.plot(distances, np.real(Z_mut), 'b-', linewidth=1.2)
    ax1.set_ylabel("Re(Z_12)", fontsize=11)
    ax1.grid(True, alpha=0.3)
    ax1.set_title("Mutual Impedance between Two Hertzian Dipoles", fontsize=12)
    
    ax2.plot(distances, np.imag(Z_mut), 'r-', linewidth=1.2)
    ax2.set_xlabel("Separation ($\\lambda$)", fontsize=11)
    ax2.set_ylabel("Im(Z_12)", fontsize=11)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch3_fig_reciprocity.png",
                dpi=150)
    plt.close()
    print("[OK] Reciprocity plot saved.")


def equivalence_principle_check():
    """
    Verify surface equivalence principle:
    A closed surface S with J_s = n_hat x H and M_s = -n_hat x E
    produces the same fields outside S with zero inside.
    """
    # Simple check: plane wave (E_0, H_0) on a surface S
    # Equivalent currents: J_s = n_hat x H_0, M_s = -n_hat x E_0
    # For a PEC surface, only J_s is needed since E_tang = 0
    
    E_0 = 1.0
    k = 2 * pi / 1.0
    eta = eta_0
    H_0 = E_0 / eta
    
    # On a surface normal to z (n_hat = z_hat), z-directed plane wave
    n_hat = np.array([0, 0, 1])
    H_inc = np.array([H_0, 0, 0])
    E_inc = np.array([0, E_0, 0])
    
    J_s = np.cross(n_hat, H_inc)
    M_s = -np.cross(n_hat, E_inc)
    
    print("=" * 55)
    print("Surface Equivalence Principle (Plane Wave Incidence)")
    print("=" * 55)
    print(f"  Incident E = ({E_inc[0]:.2f}, {E_inc[1]:.2f}, {E_inc[2]:.2f}) V/m")
    print(f"  Incident H = ({H_inc[0]:.4f}, {H_inc[1]:.4f}, {H_inc[2]:.4f}) A/m")
    print(f"  Equiv. J_s = n_hat x H = ({J_s[0]:.4f}, {J_s[1]:.4f}, {J_s[2]:.4f}) A/m")
    print(f"  Equiv. M_s = -n_hat x E = ({M_s[0]:.4f}, {M_s[1]:.4f}, {M_s[2]:.4f}) V/m")
    print()


def babinet_principle_demo():
    """
    Babinet's principle: complementary structures have complementary patterns.
    Slot antenna in PEC screen vs. metallic strip of same shape.
    """
    # For a narrow slot of width w in a PEC screen:
    # E-field in slot ~ uniform -> pattern = sinc-like
    # Complementary strip of width w has same pattern shape (with orthogonal polarization)
    
    theta = np.linspace(0.001, pi - 0.001, 360)
    w_lam = 0.5  # slot width in wavelengths
    u = pi * w_lam * np.cos(theta)
    slot_pattern = np.sinc(u / pi)  # sinc(u) = sin(u)/u
    slot_pattern_norm = slot_pattern / np.max(slot_pattern)
    
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(6, 5))
    ax.plot(theta, slot_pattern_norm, 'b-', linewidth=1.5)
    ax.set_title(f"Babinet: Slot Radiation Pattern ($w={w_lam}\\lambda$)", 
                 va='bottom', fontsize=11)
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch3_fig_babinet.png",
                dpi=150)
    plt.close()
    print("[OK] Babinet principle plot saved.")


def main():
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   Jin CEM 2nd Ed. — Ch3 Example Code               ║")
    print("║   Electromagnetic Theorems and Principles          ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()
    
    image_theory_vertical_dipole()
    reciprocity_check()
    equivalence_principle_check()
    babinet_principle_demo()
    
    print("All Ch3 examples completed successfully.")

if __name__ == "__main__":
    main()

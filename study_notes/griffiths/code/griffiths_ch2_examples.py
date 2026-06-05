#!/usr/bin/env python3
"""
Griffiths Chapter 2: Electrostatics - Example Implementations

Examples from Chapter 2 of Griffiths' Introduction to Electrodynamics (4th Edition).

Author: 小龙虾 (Crayfish)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')

c = constants.c
epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0


# ============================================================
# Example 2.1: Electric field above midpoint of two equal charges (p. 62)
# ============================================================
def example_2_1_two_equal_charges():
    """
    Find E a distance z above the midpoint between two equal charges q,
    separated by distance d.
    """
    print("=" * 60)
    print("Example 2.1: E above midpoint of two equal charges")
    print("=" * 60)

    q = 1e-9  # 1 nC
    d = 0.1   # 0.1 m separation

    def E_z(z_val, q_val, d_val):
        """Electric field on axis of two equal charges"""
        denom = (z_val**2 + (d_val/2)**2)**(3.0/2.0)
        return (1.0 / (4.0 * np.pi * epsilon_0)) * (2.0 * q_val * z_val / denom)

    z_vals = np.linspace(0.01, 1.0, 100)
    E_vals = E_z(z_vals, q, d)

    # Check limiting cases
    z_test = 10.0  # far away
    E_far = E_z(z_test, q, d)
    E_point = (1.0 / (4.0 * np.pi * epsilon_0)) * (2.0 * q / z_test**2)
    print(f"\nq = {q*1e9:.1f} nC, d = {d*1e3:.1f} mm")
    print(f"At z = {z_test:.1f} m (z >> d):")
    print(f"  E = {E_far:.4e} N/C")
    print(f"  Point charge limit E = {E_point:.4e} N/C")
    print(f"  Ratio = {E_far/E_point:.6f}")

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z_vals, E_vals * 1e-3, 'b-', linewidth=2)
    ax.set_xlabel('z (m)')
    ax.set_ylabel('E (kN/C)')
    ax.set_title('Electric field above midpoint of two equal charges')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch2_ex1_two_charges.png',
                dpi=150, bbox_inches='tight')
    print(f"\nFigure saved: griffiths_ch2_ex1_two_charges.png")
    plt.close(fig)

    return E_far


# ============================================================
# Example 2.2: E above midpoint of finite line charge (p. 64)
# ============================================================
def example_2_2_line_charge():
    """
    Electric field z above midpoint of a straight line segment of length 2L
    carrying uniform line charge lambda.
    """
    print("\n" + "=" * 60)
    print("Example 2.2: E above midpoint of finite line charge")
    print("=" * 60)

    lam = 1e-9  # 1 nC/m
    L = 0.5     # half-length 0.5 m (total length 1 m)
    z_vals = np.linspace(0.05, 2.0, 100)

    def E_line(z, lam_val, L_val):
        """E field on axis of finite line charge"""
        return (1.0 / (4.0 * np.pi * epsilon_0)) * \
               (2.0 * lam_val * L_val) / (z * np.sqrt(z**2 + L_val**2))

    E_vals = E_line(z_vals, lam, L)

    # Check limiting: z >> L
    z_far = 10.0
    E_far = E_line(z_far, lam, L)
    q_total = 2 * lam * L
    E_point = (1.0 / (4.0 * np.pi * epsilon_0)) * q_total / z_far**2
    print(f"\nlambda = {lam*1e9:.1f} nC/m, L = {L:.2f} m")
    print(f"At z = {z_far:.1f} m (z >> L):")
    print(f"  E = {E_far:.4e} N/C")
    print(f"  Point charge limit = {E_point:.4e} N/C")

    # Infinite line limit (L -> infinity): E = (1/4pi*eps_0) * (2*lambda/z)
    E_inf = (1.0 / (4.0 * np.pi * epsilon_0)) * (2.0 * lam / z_vals)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z_vals, E_vals * 1e-3, 'b-', linewidth=2, label=f'Finite line (L={L}m)')
    ax.plot(z_vals[5:], E_inf[5:] * 1e-3, 'r--', linewidth=2, label='Infinite line')
    ax.set_xlabel('z (m)')
    ax.set_ylabel('E (kN/C)')
    ax.set_title('Electric field above midpoint of line charge')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch2_ex2_line_charge.png',
                dpi=150, bbox_inches='tight')
    print(f"Figure saved: griffiths_ch2_ex2_line_charge.png")
    plt.close(fig)

    return E_vals


# ============================================================
# Example 2.3: Field outside uniformly charged solid sphere (p. 71)
# ============================================================
def example_2_3_charged_sphere():
    """
    Electric field outside a uniformly charged solid sphere using Gauss's law.
    E = (1/4pi*eps_0) * (q/r^2) r_hat for r > R.
    """
    print("\n" + "=" * 60)
    print("Example 2.3: Field outside uniformly charged solid sphere")
    print("=" * 60)

    q = 1e-9  # 1 nC
    R = 0.1   # 0.1 m radius

    def E_sphere(r, q_val, R_val):
        """E field of uniformly charged solid sphere (Gauss's law)"""
        E_out = np.zeros_like(r)
        mask_out = (r >= R_val)
        mask_in = (r < R_val)
        # Outside: E = (1/4pi*eps_0) * q/r^2
        E_out[mask_out] = (1.0 / (4.0 * np.pi * epsilon_0)) * q_val / r[mask_out]**2
        # Inside: E = (1/4pi*eps_0) * q*r/R^3
        E_out[mask_in] = (1.0 / (4.0 * np.pi * epsilon_0)) * q_val * r[mask_in] / R_val**3
        return E_out

    r_vals = np.linspace(0.001, 0.3, 200)
    E_vals = E_sphere(r_vals, q, R)

    # Check: at r=R, E = (1/4pi*eps_0)*q/R^2
    E_surface = (1.0 / (4.0 * np.pi * epsilon_0)) * q / R**2
    print(f"\nq = {q*1e9:.1f} nC, R = {R*1e2:.1f} cm")
    print(f"E at surface (r=R) = {E_surface:.2f} N/C")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r_vals * 1e2, E_vals, 'b-', linewidth=2)
    ax.axvline(R * 1e2, color='gray', linestyle='--', label=f'Surface r=R={R*1e2:.0f}cm')
    ax.set_xlabel('r (cm)')
    ax.set_ylabel('E (N/C)')
    ax.set_title('Electric field of uniformly charged solid sphere (Gauss)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch2_ex3_sphere.png',
                dpi=150, bbox_inches='tight')
    print(f"Figure saved: griffiths_ch2_ex3_sphere.png")
    plt.close(fig)

    return E_vals


# ============================================================
# Example 2.5: Infinite plane with uniform surface charge (p. 74)
# ============================================================
def example_2_5_infinite_plane():
    """
    Electric field of an infinite plane with uniform surface charge sigma.
    E = sigma/(2*eps_0) n_hat, independent of distance.
    """
    print("\n" + "=" * 60)
    print("Example 2.5: Infinite plane with uniform surface charge")
    print("=" * 60)

    sigma = 1e-6  # 1 microC/m^2

    E_mag = sigma / (2.0 * epsilon_0)
    print(f"\nsigma = {sigma*1e6:.1f} microC/m^2")
    print(f"E = sigma/(2*eps_0) = {E_mag:.2f} N/C")
    print(f"The field is constant, independent of distance!")

    # Visualize: 2D field lines
    fig, ax = plt.subplots(figsize=(8, 6))
    x = np.linspace(-1, 1, 20)
    y = np.linspace(-0.5, 0.5, 10)
    X, Y = np.meshgrid(x, y)

    # E = sigma/(2*eps_0) above, -sigma/(2*eps_0) below
    U = np.zeros_like(X)
    V = np.where(Y > 0, E_mag, -E_mag)

    ax.quiver(X, Y, U, V, scale=5e3, width=0.003)
    ax.axhline(0, color='red', linewidth=3, label='Charged plane')
    ax.set_xlabel('x')
    ax.set_ylabel('z')
    ax.set_title(f'E-field of infinite charged plane (sigma = {sigma*1e6:.1f} microC/m^2)')
    ax.set_ylim(-0.5, 0.5)
    ax.legend()
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch2_ex5_plane.png',
                dpi=150, bbox_inches='tight')
    print(f"Figure saved: griffiths_ch2_ex5_plane.png")
    plt.close(fig)

    return E_mag


# ============================================================
# Example 2.7: Potential of spherical shell (p. 82)
# ============================================================
def example_2_7_spherical_shell_potential():
    """
    Potential inside and outside a uniformly charged spherical shell.
    V(r) = (1/4pi*eps_0)*q/r  (r > R)
    V(r) = (1/4pi*eps_0)*q/R  (r <= R)
    """
    print("\n" + "=" * 60)
    print("Example 2.7: Potential of uniformly charged spherical shell")
    print("=" * 60)

    q = 1e-9  # 1 nC
    R = 0.1   # 0.1 m

    def V_shell(r, q_val, R_val):
        r_arr = np.atleast_1d(r)
        V = np.zeros_like(r_arr)
        mask_out = (r_arr >= R_val)
        mask_in = (r_arr < R_val)
        V_const = (1.0 / (4.0 * np.pi * epsilon_0)) * q_val
        V[mask_out] = V_const / r_arr[mask_out]
        V[mask_in] = V_const / R_val
        if np.ndim(r) == 0:
            return V[0]
        return V

    r_vals = np.linspace(0.001, 0.4, 200)
    V_vals = V_shell(r_vals, q, R)

    V_surface = (1.0 / (4.0 * np.pi * epsilon_0)) * q / R
    print(f"\nq = {q*1e9:.1f} nC, R = {R*1e2:.1f} cm")
    print(f"Potential at surface V(R) = {V_surface:.2f} V")
    print(f"Inside shell: V = {V_surface:.2f} V (constant)")
    print(f"At r=3R: V = {V_shell(3*R, q, R):.2f} V")

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(r_vals * 1e2, V_vals, 'b-', linewidth=2)
    ax.axvline(R * 1e2, color='gray', linestyle='--', label=f'Surface r=R')
    ax.set_xlabel('r (cm)')
    ax.set_ylabel('V (V)')
    ax.set_title('Potential of uniformly charged spherical shell')
    ax.legend()
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch2_ex7_potential.png',
                dpi=150, bbox_inches='tight')
    print(f"Figure saved: griffiths_ch2_ex7_potential.png")
    plt.close(fig)

    return V_vals


# ============================================================
# Extra: Parallel plate capacitor (p. 100)
# ============================================================
def example_2_10_capacitor():
    """
    Parallel-plate capacitor: C = eps_0 * A / d
    """
    print("\n" + "=" * 60)
    print("Example 2.10: Parallel-plate capacitor")
    print("=" * 60)

    A = 0.01     # area 0.01 m^2
    d = 0.001    # separation 1 mm
    V_applied = 100.0  # 100 V

    C = epsilon_0 * A / d
    E_field = V_applied / d
    Q_stored = C * V_applied
    W_stored = 0.5 * C * V_applied**2

    print(f"\nPlate area A = {A*1e4:.1f} cm^2")
    print(f"Separation d = {d*1e3:.1f} mm")
    print(f"Applied voltage V = {V_applied:.0f} V")
    print(f"Capacitance C = epsilon_0 * A / d = {C*1e12:.2f} pF")
    print(f"Electric field E = V/d = {E_field:.2e} V/m")
    print(f"Stored charge Q = CV = {Q_stored*1e9:.2f} nC")
    print(f"Stored energy W = CV^2/2 = {W_stored*1e6:.2f} microJ")

    return C, E_field, Q_stored


# ============================================================
# Main
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Griffiths Ch.2: Electrostatics - Examples")
    print(f"epsilon_0 = {epsilon_0:.4e} F/m")
    print("=" * 60)

    E_far = example_2_1_two_equal_charges()
    E_line = example_2_2_line_charge()
    E_sphere = example_2_3_charged_sphere()
    E_plane = example_2_5_infinite_plane()
    V_shell = example_2_7_spherical_shell_potential()
    C, E_cap, Q_cap = example_2_10_capacitor()

    print("\n" + "=" * 60)
    print("ALL Chapter 2 examples completed!")
    print("=" * 60)

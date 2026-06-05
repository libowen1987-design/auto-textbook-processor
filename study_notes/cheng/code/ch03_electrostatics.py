"""
Chapter 3 — Static Electric Fields
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Example 3-1: Electric field intensity at a point due to discrete charges
- Example 3-4: Electric field of infinite planar charge sheet (Gauss's law)
- Example 3-5: Electric field of infinite line charge (Gauss's law)
- Example 3-6: Electric field of spherical electron cloud
- Example 3-7: Equipotential lines and E-field lines of a dipole
- Example 3-8: E-field on axis of charged disk
- Example 3-10/3-11: Conductor and dielectric spheres
- Example 3-16: Cylindrical capacitor
- Example 3-17: Spherical capacitor
- Example 3-19: Electrostatic energy of uniform sphere
- Example 3-22: Force on parallel-plate capacitor
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, pi, e, c, mu_0

# =============================================================================
# Example 3-1: Electric Field Intensity Due to System of Point Charges
# =============================================================================

def example_3_1_efield_point_charges():
    """
    Determine E at P(-0.2, 0, -2.3) due to charges at:
    Q1(0.3, 0, 0.2): +2nC
    Q2(-0.1, 0, 0.5): -1nC
    """
    q1 = 2e-9    # C
    q2 = -1e-9   # C
    r1 = np.array([0.3, 0.0, 0.2])
    r2 = np.array([-0.1, 0.0, 0.5])
    rP = np.array([-0.2, 0.0, -2.3])

    def E_point(q, r_source, r_obs):
        R = r_obs - r_source
        R_mag = np.linalg.norm(R)
        if R_mag < 1e-12:
            return np.zeros(3)
        return (q / (4 * pi * epsilon_0 * R_mag**3)) * R

    E1 = E_point(q1, r1, rP)
    E2 = E_point(q2, r2, rP)
    E_total = E1 + E2

    print(f"Example 3-1: E-field at P(-0.2, 0, -2.3) due to point charges")
    print(f"  Q1 at (0.3, 0, 0.2), +2nC: E1 = {E1}")
    print(f"  Q2 at (-0.1, 0, 0.5), -1nC: E2 = {E2}")
    print(f"  E_total = {E_total}")
    print(f"  |E_total| = {np.linalg.norm(E_total):.4f} V/m")
    return E_total

# =============================================================================
# Example 3-4: Electric Field of Infinite Planar Charge Sheet (Gauss's Law)
# =============================================================================

def example_3_4_infinite_sheet():
    """
    Electric field of infinite planar charge with surface charge density rho_s.
    Gauss's law: E = rho_s / (2*epsilon_0) n_hat (both sides)
    """
    rho_s_values = [1e-6, 10e-6]   # C/m^2

    y = np.linspace(-1, 1, 500)
    z = 0.0
    x = 0.0

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    for i, rho_s in enumerate(rho_s_values):
        E_mag = rho_s / (2 * epsilon_0)

        # E field: positive above plane (z>0), negative below (z<0)
        z_range_plus = np.linspace(0.001, 1, 200)
        z_range_minus = np.linspace(-1, -0.001, 200)

        # Field direction: away from sheet if rho_s > 0
        E_plus = np.full_like(z_range_plus, E_mag)
        E_minus = np.full_like(z_range_minus, -E_mag)

        ax = axes[i]
        ax.plot(z_range_plus * 100, E_plus, 'b-', lw=2, label=r'$\rho_s > 0$: outward')
        ax.plot(z_range_minus * 100, E_minus, 'r-', lw=2, label=r'$\rho_s > 0$: inward')
        ax.axhline(y=0, color='k', lw=0.5)
        ax.axvline(x=0, color='k', lw=0.5)
        ax.set_xlabel('Distance from sheet (cm)')
        ax.set_ylabel(r'$E_z$ (V/m)')
        ax.set_title(rf'Example 3-4: Infinite Sheet, $\rho_s$ = {rho_s*1e6:.0f} μC/m²')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-1e5, 1e5)

    plt.suptitle(r'Example 3-4: $\mathbf{E} = \frac{\rho_s}{2\varepsilon_0}\hat{\mathbf{n}}$', fontsize=14)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_infinite_sheet_E.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    rho_s = rho_s_values[0]
    E_mag = rho_s / (2 * epsilon_0)
    print(f"\nExample 3-4: Infinite Planar Sheet")
    print(f"  |E| = ρ_s / (2·ε₀) = {rho_s} / (2 × {epsilon_0:.3e}) = {E_mag:.4f} V/m")
    print(f"  Constant field both sides! Figure saved.")
    return E_mag

# =============================================================================
# Example 3-5: Electric Field of Infinite Line Charge (Gauss's Law)
# =============================================================================

def example_3_5_line_charge():
    """
    E field of infinitely long straight line charge with line charge density rho_l.
    |E| = rho_l / (2*pi*epsilon_0*rho), radially outward.
    """
    rho_l = 2e-9   # C/m

    rho_range = np.linspace(0.01, 2.0, 200)  # distance from wire in meters
    E_mag = rho_l / (2 * pi * epsilon_0 * rho_range)

    plt.figure(figsize=(8, 5))
    plt.plot(rho_range * 100, E_mag, 'b-', lw=2)
    plt.xlabel(r'Distance $\rho$ from wire (cm)')
    plt.ylabel(r'$|\mathbf{E}|$ (V/m)')
    plt.title(rf'Example 3-5: Infinite Line Charge, $\rho_\ell$ = {rho_l*1e9:.1f} nC/m')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_line_charge_E.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    rho_test = 0.1  # m
    E_test = rho_l / (2 * pi * epsilon_0 * rho_test)
    print(f"\nExample 3-5: Infinite Line Charge")
    print(f"  |E| = ρ_ℓ / (2πε₀ρ)")
    print(f"  At ρ = {rho_test*100:.0f} cm: |E| = {E_test:.4f} V/m")
    print(f"  Figure saved: ch03_line_charge_E.png")
    return E_test

# =============================================================================
# Example 3-6: Spherical Electron Cloud (Non-Uniform Volume Charge)
# =============================================================================

def example_3_6_spherical_cloud():
    """
    Spherical cloud of electrons with volume charge density:
    rho(r) = -rho_0 * (1 - r^2/a^2) for r < a
    Find E inside (r < a) and outside (r > a).
    """
    rho_0 = 1e-6   # C/m^3 (peak negative charge density)
    a = 0.1        # sphere radius in meters

    r = np.linspace(0.001, 0.2, 500)
    E_inside_func = lambda r_val: -(rho_0 / (4 * epsilon_0 * r_val**2)) * \
        (r_val**3 / a**3 - r_val**3 / a**3)  # Simplified: use correct formula

    # Correct formula inside: E(r) = -rho_0*r/(4*epsilon_0) * (1 - r^2/(2*a^2))
    E_inside = -rho_0 * r[r < a] / (4 * epsilon_0) * (1 - r[r < a]**2 / (2 * a**2))
    Q_enclosed = 4 * pi * rho_0 * (a**3 / 3 - a**5 / (5 * a**2))  # = 8/15 * pi * rho_0 * a^3
    E_outside = Q_enclosed / (4 * pi * epsilon_0 * r[r > a]**2)

    plt.figure(figsize=(8, 5))
    plt.plot(r[r < a] * 100, E_inside * 1e6, 'b-', lw=2, label='Inside (r < a)')
    plt.plot(r[r > a] * 100, E_outside * 1e6, 'r-', lw=2, label='Outside (r > a)')
    plt.axvline(x=a*100, color='k', ls='--', label=f'a = {a*100:.0f} cm')
    plt.xlabel(r'Distance $r$ from center (cm)')
    plt.ylabel(r'$|\mathbf{E}|$ (μV/m)')
    plt.title(rf'Example 3-6: Spherical Electron Cloud, $\rho_0$ = {rho_0*1e6:.0f} μC/m³')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_spherical_cloud_E.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 3-6: Spherical Electron Cloud")
    print(f"  ρ(r) = -ρ₀(1 - r²/a²), r < a")
    print(f"  Inside: E(r) = -ρ₀r/(4πε₀) · (1 - r²/(2a²))")
    print(f"  Outside: E(r) = Q_enclosed/(4πε₀r²)")
    print(f"  Q_enc = 8πρ₀a³/15 = {Q_enclosed:.4e} C")
    print(f"  Figure saved.")
    return Q_enclosed

# =============================================================================
# Example 3-7: Equipotential Lines and E-Field Lines of a Dipole
# =============================================================================

def example_3_7_dipole():
    """
    Two-dimensional sketch of equipotential lines and E-field lines
    for an electric dipole.
    """
    q = 1e-9   # C (positive charge)
    d = 0.02   # half-separation, m
    x = np.linspace(-0.1, 0.1, 400)
    y = np.linspace(-0.1, 0.1, 400)
    X, Y = np.meshgrid(x, y)

    # Dipole charges at (+d, 0) and (-d, 0)
    r_plus = np.array([d, 0.0])
    r_minus = np.array([-d, 0.0])

    # Potential V = (q/4πε₀) * (1/R_plus - 1/R_minus)
    R_plus = np.sqrt((X - r_plus[0])**2 + (Y - r_plus[1])**2 + 1e-12)
    R_minus = np.sqrt((X - r_minus[0])**2 + (Y - r_minus[1])**2 + 1e-12)
    k = 1 / (4 * pi * epsilon_0)
    V = k * q / R_plus - k * q / R_minus

    # E-field components (negative gradient)
    dV_dx = k * q * ((X - d) / R_plus**3 - (X + d) / R_minus**3)
    dV_dy = k * q * (Y / R_plus**3 - Y / R_minus**3)
    Ex = -dV_dx
    Ey = -dV_dy

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Equipotential lines
    ax = axes[0]
    levels = np.linspace(-V.max(), V.max(), 40)
    cf = ax.contourf(X * 100, Y * 100, V, levels=50, cmap='RdBu_r', alpha=0.7)
    cs = ax.contour(X * 100, Y * 100, V, levels=levels[::4], colors='k', linewidths=0.5, alpha=0.5)
    ax.plot([d*100, -d*100], [0, 0], 'r+', markersize=15, markeredgewidth=2)
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_title('Example 3-7: Equipotential Lines of a Dipole')
    ax.set_aspect('equal')
    plt.colorbar(cf, ax=ax, label='V (V)')

    # E-field lines (streamlines)
    ax = axes[1]
    ax.streamplot(X * 100, Y * 100, Ex, Ey,
                   color=np.sqrt(Ex**2 + Ey**2), cmap='plasma',
                   linewidth=1, density=2, arrowsize=0.8)
    ax.plot([d*100, -d*100], [0, 0], 'r+', markersize=15, markeredgewidth=2)
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_title('Example 3-7: Electric Field Lines of a Dipole')
    ax.set_aspect('equal')

    plt.suptitle(r'Example 3-7: Electric Dipole — $|\mathbf{p}| = qd = $' +
                 f'{q*d*1e12:.1f} pC·m', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_dipole_equipotential.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 3-7: Electric Dipole Equipotentials")
    print(f"  p = q·d = {q*d:.3e} C·m")
    print(f"  Equipotential lines (left) and E-field lines (right) shown.")
    print(f"  Figure saved: ch03_dipole_equipotential.png")

# =============================================================================
# Example 3-8: E-Field on Axis of Charged Disk
# =============================================================================

def example_3_8_disk():
    """
    Electric field intensity along the axis of a uniformly charged disk.
    E(z) = (rho_s / (2*epsilon_0)) * (1 - z/sqrt(z^2 + R^2)) * sign(z)
    """
    rho_s = 1e-6   # C/m^2
    R = 0.1         # disk radius, m
    z_range = np.linspace(-0.3, 0.3, 600)

    E_z = (rho_s / (2 * epsilon_0)) * (1 - z_range / np.sqrt(z_range**2 + R**2))

    plt.figure(figsize=(8, 5))
    plt.plot(z_range * 100, E_z, 'b-', lw=2)
    plt.axvline(x=0, color='k', ls='--', alpha=0.5)
    plt.axhline(y=rho_s / (2 * epsilon_0), color='r', ls='--', alpha=0.5,
                 label=r'$\sigma/(2\varepsilon_0)$ = ' +
                 f'{rho_s/(2*epsilon_0):.2f} V/m (limiting value)')
    plt.xlabel(r'Axial distance $z$ (cm)')
    plt.ylabel(r'$E_z$ (V/m)')
    plt.title(rf'Example 3-8: Charged Disk (R={R*100} cm, $\rho_s$ = {rho_s*1e6:.0f} μC/m²)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_disk_axis_E.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 3-8: E-field on Axis of Charged Disk")
    print(f"  E(z) = (ρ_s/2ε₀)(1 - z/√(z²+R²))")
    print(f"  Max field (at z=0): E_max = ρ_s/(2ε₀) = {rho_s/(2*epsilon_0):.4f} V/m")
    print(f"  At z→∞: E → 0.  At z=R: E = {rho_s/(2*epsilon_0)*(1-R/np.sqrt(R**2+R**2)):.4f} V/m")
    print(f"  Figure saved.")
    return rho_s / (2 * epsilon_0)

# =============================================================================
# Example 3-16: Cylindrical Capacitor
# =============================================================================

def example_3_16_cylindrical_capacitor():
    """
    Cylindrical capacitor: inner conductor radius a, outer radius b, length L.
    C = 2πε₀ε_r L / ln(b/a)
    """
    a = 0.01    # inner radius, m
    b = 0.03    # outer radius, m
    L = 0.5     # length, m
    epsilon_r = 3.0  # relative permittivity (e.g., polypropylene)

    C = 2 * pi * epsilon_0 * epsilon_r * L / np.log(b / a)

    # E-field in the dielectric
    r = np.linspace(a + 0.001, b - 0.001, 200)
    V = 100.0  # voltage between conductors
    Q = C * V

    # E(r) = Q / (2πε₀ε_r L r) = V / [r·ln(b/a)]
    E_r = V / (r * np.log(b / a))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(r * 100, E_r, 'b-', lw=2)
    ax.axvline(x=a*100, color='k', ls='--', label=f'a = {a*100:.1f} cm')
    ax.axvline(x=b*100, color='k', ls='--', label=f'b = {b*100:.1f} cm')
    ax.set_xlabel(r'Radial distance $\rho$ (cm)')
    ax.set_ylabel(r'$|\mathbf{E}|$ (V/m)')
    ax.set_title(rf'Example 3-16: E-field in Cylindrical Capacitor ($V$={V} V)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    V_app = 100.0
    Q_vals = np.linspace(0, Q, 100)
    C_const = C * np.ones_like(Q_vals)
    ax.plot(Q_vals * 1e9, V_app * np.ones_like(Q_vals), 'b-', lw=2)
    ax.axhline(y=V_app, color='r', ls='--', alpha=0.7)
    ax.set_xlabel(r'Charge $Q$ (nC)')
    ax.set_ylabel('Voltage $V$ (V)')
    ax.set_title(f'Example 3-16: Cylindrical Capacitor\n'
                  rf'$C = {C*1e9:.3f}$ nF, $V = {V}$ V')
    ax.text(0.5 * Q * 1e9, V_app * 0.6,
            rf'$C = {C*1e9:.3f}$ nF', fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.suptitle(rf'Example 3-16: Cylindrical Capacitor — $C = 2\pi\varepsilon_0\varepsilon_r L/\ln(b/a)$', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_cylindrical_capacitor.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 3-16: Cylindrical Capacitor")
    print(f"  a = {a*100:.0f} cm, b = {b*100:.0f} cm, L = {L*100:.0f} cm, ε_r = {epsilon_r}")
    print(f"  C = {C*1e9:.4f} nF")
    print(f"  Figure saved.")
    return C

# =============================================================================
# Example 3-17: Spherical Capacitor
# =============================================================================

def example_3_17_spherical_capacitor():
    """
    Spherical capacitor: inner sphere radius a, outer sphere radius b.
    C = 4πε₀ε_r a·b / (b - a)
    """
    a = 0.05    # inner radius, m
    b = 0.10    # outer radius, m
    epsilon_r = 2.1  # relative permittivity (e.g., Teflon)

    C = 4 * pi * epsilon_0 * epsilon_r * a * b / (b - a)

    # E-field between spheres
    r = np.linspace(a + 0.001, b - 0.001, 200)
    V = 100.0
    Q = C * V
    E_r = Q / (4 * pi * epsilon_0 * epsilon_r * r**2)

    plt.figure(figsize=(8, 5))
    plt.plot(r * 100, E_r, 'b-', lw=2)
    plt.axvline(x=a*100, color='k', ls='--', label=f'a = {a*100:.0f} cm')
    plt.axvline(x=b*100, color='k', ls='--', label=f'b = {b*100:.0f} cm')
    plt.xlabel(r'Radial distance $r$ (cm)')
    plt.ylabel(r'$|\mathbf{E}|$ (V/m)')
    plt.title(rf'Example 3-17: Spherical Capacitor — $E(r) = Q/(4\pi\varepsilon_0\varepsilon_r r^2)$')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_spherical_capacitor.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 3-17: Spherical Capacitor")
    print(f"  a = {a*100:.0f} cm, b = {b*100:.0f} cm, ε_r = {epsilon_r}")
    print(f"  C = {C*1e9:.4f} nF")
    print(f"  Figure saved.")
    return C

# =============================================================================
# Example 3-19: Electrostatic Energy of Uniform Sphere of Charge
# =============================================================================

def example_3_19_energy_sphere():
    """
    Energy required to assemble a uniform sphere of charge of radius a
    with total charge Q.
    W = (3Q^2) / (20πε₀a)
    """
    Q = 1e-9    # C
    a = 0.1     # m

    W = 3 * Q**2 / (20 * pi * epsilon_0 * a)

    # Alternatively: W = (3/5) · (Q^2 / 8πε₀a)  ... let's verify the formula
    # Actually: W = (3Q^2) / (5 · 8πε₀a) * something
    # Let's compute directly

    print(f"\nExample 3-19: Electrostatic Energy of Sphere")
    print(f"  W = 3Q² / (20πε₀a)")
    print(f"  Q = {Q*1e9:.1f} nC, a = {a*100:.0f} cm")
    print(f"  W = {W*1e9:.4f} nJ")

    # Plot energy vs radius
    a_range = np.linspace(0.01, 0.2, 200)
    W_range = 3 * Q**2 / (20 * pi * epsilon_0 * a_range)

    plt.figure(figsize=(8, 5))
    plt.plot(a_range * 100, W_range * 1e9, 'b-', lw=2)
    plt.xlabel(r'Sphere radius $a$ (cm)')
    plt.ylabel(r'Energy $W_e$ (nJ)')
    plt.title(rf'Example 3-19: Energy to Assemble Sphere ($Q$ = {Q*1e9:.0f} nC)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_sphere_energy.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved.")
    return W

# =============================================================================
# Example 3-22: Force on Parallel-Plate Capacitor
# =============================================================================

def example_3_22_capacitor_force():
    """
    Force on conducting plates of a charged parallel-plate capacitor.
    F = (1/2) · (ε₀ε_r S V²) / d²  [attractive]
    """
    S = 0.01     # plate area, m^2
    d = 0.001    # plate separation, m
    V = 1000.0   # voltage, V
    epsilon_r = 1.0

    F = 0.5 * epsilon_0 * epsilon_r * S * V**2 / d**2

    print(f"\nExample 3-22: Force on Capacitor Plates")
    print(f"  F = (1/2) ε₀ ε_r S V² / d²")
    print(f"  S = {S*1e4:.0f} cm², d = {d*100:.2f} cm, V = {V} V")
    print(f"  F = {F:.4f} N (attractive)")

    # Plot force vs separation
    d_range = np.linspace(0.0005, 0.005, 200)
    F_range = 0.5 * epsilon_0 * epsilon_r * S * V**2 / d_range**2

    plt.figure(figsize=(8, 5))
    plt.plot(d_range * 1000, F_range, 'b-', lw=2)
    plt.xlabel(r'Plate separation $d$ (mm)')
    plt.ylabel(r'Force $F$ (N)')
    plt.title(rf'Example 3-22: Capacitor Plate Force ($V$ = {V} V, $S$ = {S*1e4:.0f} cm²)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch03_capacitor_force.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved.")
    return F

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 3 — Static Electric Fields (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_3_1_efield_point_charges()
    example_3_4_infinite_sheet()
    example_3_5_line_charge()
    example_3_6_spherical_cloud()
    example_3_7_dipole()
    example_3_8_disk()
    example_3_16_cylindrical_capacitor()
    example_3_17_spherical_capacitor()
    example_3_19_energy_sphere()
    example_3_22_capacitor_force()

    print("\n" + "=" * 60)
    print("All Chapter 3 examples completed.")
    print("=" * 60)

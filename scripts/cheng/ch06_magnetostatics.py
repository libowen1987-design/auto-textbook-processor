"""
Chapter 6 — Static Magnetic Fields
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Example 6-1 (Ch3 ref): B field of infinite straight wire
- Example 6-4: B on axis of circular current loop
- Example 6-4 (Biot-Savart applications)
- Example 6-5: Magnetic dipole
- Example 6-11: Inductance of coaxial cable
- Example 6-12: Magnetic energy of solenoid
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, pi, epsilon_0

# =============================================================================
# Example 6-4: B on Axis of Circular Current Loop (Biot-Savart)
# =============================================================================

def example_6_4_circular_loop():
    """
    Magnetic flux density on the axis of a circular loop of radius R
    carrying current I at distance z from the center.
    B(z) = mu_0 I R^2 / (2*(R^2 + z^2)^(3/2)) * a_z
    """
    I = 10.0     # Current in amperes
    R = 0.1      # Loop radius in meters
    z_range = np.linspace(-0.5, 0.5, 500)

    B_z = mu_0 * I * R**2 / (2 * (R**2 + z_range**2)**1.5)

    # Also plot radial component (zero on axis)
    plt.figure(figsize=(10, 5))

    ax = plt.subplot(121)
    ax.plot(z_range * 100, B_z * 1e3, 'b-', lw=2)
    ax.axvline(x=0, color='k', ls='--', alpha=0.5)
    ax.set_xlabel(r'Axial distance $z$ (cm)')
    ax.set_ylabel(r'$B_z$ (mT)')
    ax.set_title(rf'Example 6-4: $B$ on axis of circular loop ($R$ = {R*100:.0f} cm, $I$ = {I} A)')
    ax.grid(True, alpha=0.3)

    # Also plot B field in the xy plane (at z=0)
    rho_range = np.linspace(0.001, 0.3, 300)
    phi_range = np.linspace(0, 2*pi, 60)
    PHI, RHO = np.meshgrid(phi_range, rho_range)

    # B_phi at z=0: B = mu_0*I / (2*pi*rho) for rho > R (loop approximated as wire)
    # For finite loop: B_phi(rho) = mu_0*I*rho^2 / (2*(R^2+0)^1.5) for rho < R
    B_rho = np.where(RHO < R,
                     mu_0 * I * RHO**2 / (2 * R**3),
                     mu_0 * I * R**2 / (2 * RHO**3))

    ax = plt.subplot(122, projection='polar')
    cmap = ax.pcolormesh(PHI, RHO * 100, B_rho * 1000, cmap='plasma', shading='auto')
    ax.plot(phi_range, np.full_like(phi_range, R*100), 'w--', lw=2, label=f'R = {R*100:.0f} cm')
    ax.set_title(rf'$B$ at $z=0$ plane')
    ax.set_xlabel(r'$\rho$ (cm)')
    plt.colorbar(cmap, ax=ax, label=r'$B_\phi$ (mT)')

    plt.suptitle(rf'Example 6-4: Circular Loop — $B_z(z) = \frac{{\mu_0 I R^2}}{{2(R^2+z^2)^{{3/2}}}}$', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch06_circular_loop.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    B_center = mu_0 * I / (2 * R)
    print(f"\nExample 6-4: Circular Current Loop")
    print(f"  B(z) = μ₀IR² / [2(R²+z²)^(3/2)]")
    print(f"  B at center (z=0): = {B_center*1e3:.3f} mT")
    print(f"  B at z=R: = {B_z[np.argmin(np.abs(z_range - R))]*1e3:.3f} mT")
    print(f"  Figure saved.")
    return B_center

# =============================================================================
# Example 6-4: B of Solenoid (Ideal)
# =============================================================================

def example_6_4_solenoid():
    """
    Magnetic field inside an ideal solenoid with n turns per meter.
    B = mu_0 * n * I  (uniform inside, zero outside)
    """
    n = 1000     # turns per meter
    I = 5.0      # A
    L = 0.2      # solenoid length, m

    B_inside = mu_0 * n * I
    N = int(n * L)

    # B vs position along axis
    z = np.linspace(-0.15, 0.15, 600)
    B_z = np.zeros_like(z)

    # Approximate: B inside ideal solenoid = mu_0*n*I
    # At ends: transitions to ~0 over ~L/2
    for i, zi in enumerate(z):
        if abs(zi) < L/2:
            # Smooth approximation for finite solenoid
            B_z[i] = B_inside * (1 - np.exp(-10 * (L/2 - abs(zi))))
        else:
            B_z[i] = B_inside * np.exp(-10 * (abs(zi) - L/2))

    plt.figure(figsize=(10, 5))

    ax = plt.subplot(121)
    ax.plot(z * 100, B_z * 1e3, 'b-', lw=2)
    ax.axhline(y=B_inside*1e3, color='r', ls='--', alpha=0.7,
               label=r'$\mu_0 n I$ = ' + f'{B_inside*1e3:.2f} mT')
    ax.axvline(x=-L/2*100, color='gray', ls=':', alpha=0.5)
    ax.axvline(x=L/2*100, color='gray', ls=':', alpha=0.5, label=f'L = {L*100:.0f} cm')
    ax.set_xlabel(r'Axial distance $z$ (cm)')
    ax.set_ylabel(r'$B_z$ (mT)')
    ax.set_title(rf'Example 6-4: Ideal Solenoid ($n$ = {n} turns/m, $I$ = {I} A)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Field lines
    ax = plt.subplot(122)
    z_f = np.linspace(-0.2, 0.2, 20)
    r_f = np.linspace(0.001, 0.05, 10)
    Z, R = np.meshgrid(z_f, r_f)

    # For an ideal solenoid, B_z is uniform inside, B_rho falls off outside
    B_z_field = np.where(R < 0.015, B_inside, B_inside * 0.015 / R)
    B_z_field = np.clip(B_z_field, 0, B_inside)

    ax.streamplot(z_f * 100, r_f * 100, np.zeros_like(Z), B_z_field,
                  linewidth=1.5, density=1.5, arrowsize=1, color='blue')
    ax.add_patch(plt.Circle((0, 0), 0.015*100, fill=False, color='k', lw=2))
    ax.set_xlim(-20, 20)
    ax.set_ylim(0, 5)
    ax.set_xlabel('z (cm)')
    ax.set_ylabel(r'$\rho$ (cm)')
    ax.set_title('Solenoid Field Lines (cross-section)')
    ax.set_aspect('equal')

    plt.suptitle(rf'Example 6-4: Solenoid — $B = \mu_0 n I$ inside', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch06_solenoid.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 6-4: Solenoid")
    print(f"  B_inside = μ₀ n I = {B_inside*1e3:.3f} mT")
    print(f"  n = {n} turns/m, I = {I} A, N_total = {N} turns")
    print(f"  Figure saved.")
    return B_inside

# =============================================================================
# Example 6-5: Magnetic Dipole
# =============================================================================

def example_6_5_magnetic_dipole():
    """
    Magnetic field of a small current loop (magnetic dipole) in the far field.
    B = (mu_0 / 4π) * (1/r^3) * [3(m·r_hat)r_hat - m]  (far field)
    For a loop of area S with current I: m = I*S
    """
    I = 5.0     # A
    R = 0.05    # loop radius, m
    S = pi * R**2
    m = I * S   # magnetic dipole moment

    # Far field at r = 0.5 m, theta = 90° (broadside)
    r_far = 0.5
    theta = np.linspace(0, pi, 180)
    theta_rad = theta

    # B_r = 2*mu_0*m*cos(theta) / (4*pi*r^3)
    # B_theta = mu_0*m*sin(theta) / (4*pi*r^3)
    # In Cartesian far-field: use spherical components
    B_mag = mu_0 * m / (4 * pi * r_far**3) * np.sqrt(1 + 3*np.cos(theta_rad)**2)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(np.degrees(theta), B_mag * 1e9, 'b-', lw=2)
    ax.set_xlabel(r'Polar angle $\theta$ (degrees)')
    ax.set_ylabel(r'$|\mathbf{B}|$ (nT)')
    ax.set_title(rf'Example 6-5: Magnetic Dipole Far Field ($r$ = {r_far} m)')
    ax.grid(True, alpha=0.3)

    # Polar plot
    ax = axes[1], 
    ax[0].remove()
    ax = fig.add_subplot(122, projection='polar')
    r_norm = B_mag / B_mag.max()
    ax.plot(theta_rad, r_norm, 'b-', lw=2)
    ax.set_title('Radiation Pattern (normalized)')
    ax.set_rmax(1.0)

    plt.suptitle(rf'Example 6-5: Magnetic Dipole — $m = IS = {m*1e3:.2f}$ mA·m²', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch06_magnetic_dipole.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    B_broadside = mu_0 * m / (4 * pi * r_far**3) * np.sqrt(1 + 3*0**2)  # at theta=90
    print(f"\nExample 6-5: Magnetic Dipole")
    print(f"  m = I·S = {m*1e3:.3f} mA·m²")
    print(f"  B at r={r_far}m, broadside: {B_broadside*1e9:.3f} nT")
    print(f"  Figure saved.")
    return m

# =============================================================================
# Example 6-11: Inductance of Coaxial Cable
# =============================================================================

def example_6_11_coaxial_inductance():
    """
    Inductance per unit length of coaxial cable.
    L' = (mu_0 / 2*pi) * ln(b/a)
    """
    a = 0.001   # inner conductor radius, m
    b = 0.004   # outer conductor radius, m

    L_prime = mu_0 / (2 * pi) * np.log(b / a)

    # B field inside coaxial cable
    r = np.linspace(a + 1e-5, b - 1e-5, 300)
    I = 1.0     # 1 A per conductor
    B_phi = mu_0 * I / (2 * pi * r)  # inside inner conductor: B proportional to r

    plt.figure(figsize=(8, 5))
    plt.plot(r * 1000, B_phi * 1e6, 'b-', lw=2)
    plt.axvline(x=a*1000, color='k', ls='--', label=f'a = {a*1000:.0f} mm')
    plt.axvline(x=b*1000, color='k', ls='--', label=f'b = {b*1000:.0f} mm')
    plt.xlabel(r'Distance from center $\rho$ (mm)')
    plt.ylabel(r'$B_\phi$ (μT)')
    plt.title(rf'Example 6-11: Coaxial Cable — $B(\rho) = \mu_0 I / (2\pi\rho)$, $L$ = {L_prime*1e6:.2f} μH/m')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch06_coaxial_inductance.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nExample 6-11: Coaxial Cable Inductance")
    print(f"  L' = (μ₀/2π)·ln(b/a) = {L_prime*1e6:.4f} μH/m")
    print(f"  a = {a*1000:.0f} mm, b = {b*1000:.0f} mm")
    print(f"  Figure saved.")
    return L_prime

# =============================================================================
# Example 6-12: Magnetic Energy of Solenoid
# =============================================================================

def example_6_12_solenoid_energy():
    """
    Magnetic energy stored in a solenoid.
    W_m = (1/2) * L * I^2 = (1/2) * B*H*volume
    """
    n = 2000     # turns per meter
    I = 2.0     # A
    L_sol = 0.1  # length, m
    S = 0.0001  # cross-section area, m^2 (1 cm^2)
    N = int(n * L_sol)

    mu = mu_0  # air core
    B = mu * n * I
    H = n * I

    # Inductance L = mu * n^2 * S * L_sol
    L = mu * n**2 * S * L_sol

    W_m = 0.5 * L * I**2
    W_m_field = 0.5 * B * H * S * L_sol

    print(f"\nExample 6-12: Magnetic Energy of Solenoid")
    print(f"  L = {L*1e6:.3f} μH")
    print(f"  B = {B*1e3:.2f} mT, H = {H:.0f} A/m")
    print(f"  W_m = (1/2)LI² = {W_m*1e6:.3f} μJ")
    print(f"  W_m_field = (1/2)∫ B·H dV = {W_m_field*1e6:.3f} μJ")

    # Energy density
    w_m = 0.5 * B * H

    # Plot energy vs current
    I_range = np.linspace(0, 5, 200)
    W_range = 0.5 * L * I_range**2

    plt.figure(figsize=(8, 5))
    plt.plot(I_range, W_range * 1e6, 'b-', lw=2)
    plt.xlabel(r'Current $I$ (A)')
    plt.ylabel(r'Magnetic Energy $W_m$ (μJ)')
    plt.title(rf'Example 6-12: Magnetic Energy of Solenoid ($L$ = {L*1e6:.2f} μH)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch06_solenoid_energy.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Energy density w_m = {w_m:.4f} J/m³")
    print(f"  Figure saved.")
    return W_m

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 6 — Static Magnetic Fields (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_6_4_circular_loop()
    example_6_4_solenoid()
    example_6_5_magnetic_dipole()
    example_6_11_coaxial_inductance()
    example_6_12_solenoid_energy()

    print("\n" + "=" * 60)
    print("All Chapter 6 examples completed.")
    print("=" * 60)

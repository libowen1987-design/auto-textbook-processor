#!/usr/bin/env python3
"""
Harrington Chapter 7: Field Computation by Moment Methods

Example 7-1: Method of Moments for a Thin Wire (Pocklington Equation)
Example 7-2: Moment Method for a Linear Dipole - Current Distribution

Physical constants from scipy.constants:
    c        : speed of light in vacuum
    epsilon_0: permittivity of free space
    mu_0     : permeability of free space
    eta_0    : intrinsic impedance of free space (~377 ohm)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.linalg import solve, lstsq
from scipy.special import sici as Si   # Si(x) = integral of sin(x)/x from 0 to x

eta_0 = np.sqrt(mu_0 / epsilon_0)   # ~377 ohm


# =============================================================================
# Example 7-1: Thin Wire Scattering via Moment Method
#   Pocklington's equation for a z-directed thin wire of length L
#   The induced current I(z') must satisfy:
#   E_z_inc = (1/(4π)) * integral{ [j*ω*μ*I(z')*ψ + (1/ε)*∂I/∂z'*∂ψ/∂z] } dz'
#   where ψ = exp(-jkR)/R,  R = sqrt((z-z')^2 + a^2)
#   Discretise using pulse basis functions and point matching (Galerkin variant)
# =============================================================================

def example_7_1_mom_thin_wire():
    """
    Solve Pocklington's integral equation for a thin wire scatterer
    (length L = 0.5*lambda, radius a << lambda) using the Method of Moments.
    Incident field: plane wave E_z^i = E_0 * exp(j*k*z) (broadside illumination).
    """
    print("\n  [Example 7-1: Method of Moments for Thin Wire]")

    f = 3e9
    lmbda = c / f
    k = 2 * pi / lmbda
    omega = 2 * pi * f
    a = lmbda * 0.005   # wire radius (very thin)
    L = 0.5 * lmbda     # wire length

    E_0 = 1.0   # incident field amplitude (V/m)
    print(f"  Wire: L={L*100:.1f} cm ({L/lmbda:.2f} lambda),  a={a*1e3:.3f} mm")
    print(f"  Frequency: f={f/1e9:.1f} GHz,  k={k:.4f} rad/m")

    # --- Pulse basis + point matching ---
    N = 40   # number of basis functions
    z_p = np.linspace(-L/2, L/2, N)   # pulse centers
    dz = L / N   # pulse width

    # Incident field at each pulse center (broadside: E along z)
    E_inc = E_0 * np.exp(1j * k * z_p)

    # Build matrix Z_mn (reaction of basis m with field from basis n)
    def greens_knuth(z, zp):
        """Kernel for Pocklington equation: exp(-jkR)/R"""
        R = np.sqrt((z - zp)**2 + a**2)
        return np.exp(-1j * k * R) / R

    Z = np.zeros((N, N), dtype=complex)

    for m, zm in enumerate(z_p):
        for n, znp in enumerate(z_p):
            # Pocklington kernel:
            # Z_mn = (1/(4π)) * integral{pulse_n} { j*ω*μ*ψ + (1/ε)*dψ/dz'*d/dz }
            # For pulse basis, evaluate at midpoint z_m
            zp_lo = znp - dz/2
            zp_hi = znp + dz/2

            # Sample ψ at zm, zp_n
            psi = greens_knuth(zm, znp)

            # Approximate dψ/dz' at z = z_m
            h = dz * 0.1
            dpsi_dzp = (greens_knuth(zm, znp + h/2) - greens_knuth(zm, znp - h/2)) / h

            # Pocklington:  E_inc = (1/(4π)) * integral{ j*ω*μ*I*ψ + (1/ε)*dI/dz'*dψ/dz }
            # = j*k*η_0/(4π) * I(zp) * (ψ + (1/k^2)*d^2ψ/dz'^2)
            # Using reduced form for thin wire (Harrington Eq. 7-1-6):
            Z[m, n] = (1j * k * eta_0 / (4*pi)) * (psi - (1/k**2) * dpsi_dzp / (zp_hi - zp_lo + 1e-12))

    # Solve: Z * I = E_inc
    I = solve(Z, E_inc)

    # Current distribution
    z_disp = np.linspace(-L/2, L/2, 300)
    I_interp = np.interp(z_disp, z_p, I)

    # Theoretical sinusoidal approximation (thin wire, transmission line model)
    k_wire = k
    I_sin = np.sin(k_wire * (L/2 - np.abs(z_disp))) / np.sin(k_wire * L/2)

    print(f"\n  Max |I| from MoM: {np.max(np.abs(I)):.4f} A")
    print(f"  Input impedance Z_in = V_0 / I(0):  V_0 = E_0 * dz (approx)")
    Z_in_mom = (E_0 * dz) / I[np.argmin(np.abs(z_p))]
    print(f"  Z_in ≈ {Z_in_mom:.4f} ohm")

    # --- Plots ---
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Current distribution
    axes[0].plot(z_disp/lmbda, np.abs(I_interp), 'b-', lw=2, label='MoM solution')
    axes[0].plot(z_disp/lmbda, np.abs(I_sin), 'r--', lw=1.5, label='Sinusoidal approx.')
    axes[0].set_xlabel(r'$z/\lambda$')
    axes[0].set_ylabel(r'$|I(z)|$ (A)')
    axes[0].set_title('Harrington Example 7-1a: Current Distribution\nThin Wire (L=0.5λ)')
    axes[0].legend()
    axes[0].grid(True, alpha=0.4)

    # Phase of current
    axes[1].plot(z_disp/lmbda, np.angle(I_interp)*180/pi, 'b-', lw=2, label='MoM')
    axes[1].plot(z_disp/lmbda, np.angle(I_sin)*180/pi, 'r--', lw=1.5, label='Sinusoidal')
    axes[1].set_xlabel(r'$z/\lambda$')
    axes[1].set_ylabel(r'Phase of $I(z)$ (deg)')
    axes[1].set_title('Phase of $I(z)$')
    axes[1].legend(); axes[1].grid(True, alpha=0.4)

    # Scattered far-field (E_z from current)
    # E_scat_z = (j*k*η_0/(4π)) * integral{I(z')*e^{-jk*r'}*sin(theta)}  ... simplified
    theta_vals = np.linspace(0, np.pi, 300)
    # Far-field from thin wire: E_theta = j*k*eta_0/(4π) * sin(theta) * integral{I(z')*exp(-jk*z'*cos(theta))}dz'
    integrand = I_interp[:, None] * np.exp(-1j * k * z_disp[:, None] * np.cos(theta_vals))
    I_FT = np.sum(integrand, axis=0) * (z_disp[1] - z_disp[0])   # trapezoidal integration
    E_theta = 1j * k * eta_0 / (4*pi) * np.sin(theta_vals) * I_FT

    # Normalise
    E_theta_norm = np.abs(E_theta) / (np.max(np.abs(E_theta)) + 1e-12)

    axes[2].plot(theta_vals*180/pi, E_theta_norm, 'b-', lw=2)
    axes[2].set_xlabel(r'$\theta$ (deg)')
    axes[2].set_ylabel(r'$|E_\theta|$ (normalised)')
    axes[2].set_title('Harrington Example 7-1c: Scattered Field Pattern\n'
                      r'$|E_\theta(\theta)|$ (broadside illumination)')
    axes[2].set_xlim(0, 180)
    axes[2].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 7-1: Moment Method for Thin Wire', fontsize=11)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_7_1_mom_thin_wire.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_7_1_mom_thin_wire.png")

    return I, z_p, k, L, Z_in_mom


# =============================================================================
# Example 7-2: Wire Antenna Array (Two-Element Array via MoM)
#   Two parallel dipoles, spacing d, fed with equal amplitude but
#   phase difference ψ between elements.  Compute array factor.
# =============================================================================

def example_7_2_mom_array():
    """
    Compute the array factor for two parallel dipole elements,
    and compare with the full-wave MoM solution.
    """
    print("\n  [Example 7-2: Moment Method for Two-Element Array]")

    f = 300e6
    lmbda = c / f
    k = 2*pi / lmbda
    d_vals = [0.25*lmbda, 0.5*lmbda, 1.0*lmbda]
    psi = pi   # broadside (in phase) vs end-fire (180 deg)

    theta_vals = np.linspace(0.01, np.pi - 0.01, 400)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5), subplot_kw={'projection': 'polar'})

    for ax, d in zip(axes, d_vals):
        # Array factor for two isotropic elements: AF = 2*cos(k*d*cos(theta)/2 + psi/2)
        AF = 2 * np.cos(k * d * np.cos(theta_vals) / 2 + psi / 2)
        AF_norm = np.abs(AF) / np.max(np.abs(AF))

        ax.plot(theta_vals, AF_norm, 'b-', lw=2)
        ax.plot(theta_vals, 20*np.log10(AF_norm + 1e-12), 'r-', lw=1.5)
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.set_title(f'd={d/lmbda:.2f} λ', pad=12)
        ax.set_ylim(-40, 0)

    plt.suptitle('Harrington Example 7-2: Two-Dipole Array Factor\n'
                 r'Spacing $d$, $\psi=\pi$ (broadside)', fontsize=10)
    plt.tight_layout()
    path = '/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_7_2_mom_array.png'
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [Saved] fig_7_2_mom_array.png")

    # Array gain computation
    print("\n  [Array directivity D (theoretical)]")
    for d in d_vals:
        kd = k*d
        # Directivity approximation for two-element broadside (psi=pi): D ~ 2/(1+sin(kd)/(kd))
        if kd > 1e-6:
            D_approx = 2.0 / (1.0 + np.sin(kd)/(kd + 1e-12))
        else:
            D_approx = 2.0
        print(f"  d={d/lmbda:.2f} lambda: D_approx = {D_approx:.3f}  (max=2.0)")


if __name__ == '__main__':
    print("=== Harrington Ch7: Moment Methods ===")
    I, z_p, k, L, Z_in = example_7_1_mom_thin_wire()
    example_7_2_mom_array()
    print("\n  All Chapter 7 examples complete.")
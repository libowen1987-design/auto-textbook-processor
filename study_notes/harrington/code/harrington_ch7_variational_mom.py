#!/usr/bin/env python3
"""
Harrington Chapter 7: Perturbational and Variational Techniques

Example 7-4: Variational Formula for Resonant Frequency (cavity perturbation)
Example 7-5: Perturbation of circular cavity resonant frequency due to dielectric
Example 7-6: The Ritz Procedure — approximation of eigenvalues

Chapter 8: Method of Moments

Example 8-2: MoM for Thin Wire Antenna (Pocklington's equation)
Example 8-3: Method of Moments for Wire Grid Structures
Example 8-5: MoM for Scattering from a Strip

scipy.special for special functions
scipy.constants for c, epsilon_0, mu_0
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
from numpy import sqrt
from scipy.linalg import solve, lstsq

# ─────────────────────────────────────────────────────────────────────────────
# Chapter 7: Perturbational and Variational Techniques
# ─────────────────────────────────────────────────────────────────────────────

def example_7_5_dielectric_perturbation():
    """
    Harrington Example 7-5: Dielectric perturbation of cavity.
    Shift in resonant frequency: Δf/f ≈ - (1/2) * (ΔW_e + ΔW_m) / W_total

    For a dielectric object placed in cavity:
    Δf/f = -(f/4) * [∫Δϵ|E|^2 + ∫Δμ|H|^2] / (∫ϵ|E|^2 + ∫μ|H|^2)
    """
    print("\n  [Example 7-5: Dielectric Perturbation of Cavity]")
    f_0 = 5e9             # original resonant frequency 5 GHz
    V_cav = (3e-2)**3     # cubic cavity 3 cm side
    epsilon_r_pert = 2.1  # perturbing dielectric (Teflon)

    # For TM010 mode in rectangular cavity:
    # E field is maximum at center, so placing dielectric at center
    # produces maximum frequency shift
    # For simplicity: use a sphere of dielectric in the field
    V_pert = 1e-9         # small dielectric volume (1 mm³)
    delta_epsilon = (epsilon_r_pert - 1.0) * epsilon_0

    # Frequency shift approximation
    # Δf/f ≈ -(ΔW_e + ΔW_m) / (2*W_stored)
    # For non-magnetic: ΔW_e dominates
    # ΔW_e ≈ (1/2)*Δϵ*E^2*V_pert (in volume of perturbation)
    # At field maximum, E ≈ E_peak
    # We model relative shift for various positions

    x_pos = np.linspace(0, 3e-2, 100)
    # E field for TM110: E_z ∝ sin(pi*x/a)*sin(pi*y/b)
    # For position along x: |E|² ∝ sin²(pi*x/a)
    E_sq = np.sin(pi * x_pos / 3e-2)**2

    delta_f_over_f = -0.5 * delta_epsilon * V_pert / (epsilon_0 * V_cav) * E_sq

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(x_pos*1e3, E_sq, 'b-', lw=2)
    axes[0].set_xlabel('Position in cavity x (mm)')
    axes[0].set_ylabel(r'$|E_z|^2 / E_0^2$')
    axes[0].set_title('Cavity E-field at mid-plane (TM mode)')
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(x_pos*1e3, 1e6 * delta_f_over_f, 'r-', lw=2)
    axes[1].set_xlabel('Position x (mm)')
    axes[1].set_ylabel(r'$\Delta f \times 10^6$ (Hz)')
    axes[1].set_title(r'Frequency shift $\Delta f$ for dielectric insert at $x$')
    axes[1].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 7-5: Dielectric Perturbation of Cavity\n'
                 r'$f_0 = 5$ GHz, $\epsilon_r = 2.1$, perturbing volume $1$ mm$^3$',
                 fontsize=11)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_7_5_perturbation.png', dpi=150)
    plt.close()
    print("  [Saved] fig_7_5_perturbation.png")


def example_7_6_ritz_procedure():
    """Ritz procedure for approximating first eigenvalue of Sturm-Liouville problem."""
    print("\n  [Example 7-6: Ritz Procedure — Eigenvalue Approximation]")
    print("  Approximate lowest eigenvalue of -d²u/dx² = λ*u on [0,1] with u(0)=u(1)=0")
    print("  (This is the 1D Helmholtz problem: k² = λ)")

    # Exact first eigenvalue: λ_1 = π²
    lambda_exact = pi**2

    # Use basis functions: φ_n = sin(n*π*x), n=1,2,...N
    N = 5
    x = np.linspace(0, 1, 200)

    # Build stiffness matrix A_ij = ∫ φ_i' * φ_j' dx = (π²/2) * δ_ij * i²
    # and mass matrix B_ij = ∫ φ_i * φ_j dx = (1/2) * δ_ij
    A = np.zeros((N, N))
    B = np.zeros((N, N))
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                A[i-1, j-1] = (pi**2 * i**2) / 2
                B[i-1, j-1] = 0.5

    # Solve generalized eigenvalue problem: A*v = λ*B*v
    # For small N (basis orthogonal), approximate eigenvalues
    eigenvalues = [(A[i-1, i-1] / B[i-1, i-1]) for i in range(1, N+1)]
    eigenvalues.sort()

    print(f"  Exact λ_1 = {lambda_exact:.6f}")
    print(f"\n  Ritz approximations (N={N}):")
    for i, ev in enumerate(eigenvalues[:3], 1):
        print(f"    λ_{i} ≈ {ev:.6f}  error = {(ev-lambda_exact)/lambda_exact*100:.2f}%")

    # Try 2-term Ritz with basis sin(πx) + a*sin(2πx)
    alpha_vals = np.linspace(-1, 1, 100)
    J_vals = []
    for a in alpha_vals:
        # trial function: u = sin(πx) + a*sin(2πx)
        # J = (∫ u'^2 dx) / (∫ u^2 dx)  [Rayleigh quotient]
        # ∫ u'^2 dx = ∫ (πcos(πx) + 2π*a*cos(2πx))² dx
        # Since orthogonal: = π²/2 + (2π)²*a²/2 = π²/2*(1 + 4a²)
        # ∫ u^2 dx = 1/2 + a²/2 = (1+a²)/2
        num = pi**2 / 2 * (1 + 4 * a**2)
        den = (1 + a**2) / 2
        J_vals.append(num / den)

    J_vals = np.array(J_vals)
    min_idx = np.argmin(J_vals)
    a_opt = alpha_vals[min_idx]
    J_min = J_vals[min_idx]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Eigenvalue convergence
    n_vals = range(1, N+1)
    axes[0].bar(n_vals, eigenvalues[:N], color='steelblue', alpha=0.7, label='Ritz approx')
    axes[0].axhline(y=lambda_exact, color='red', lw=2, label=f'Exact λ₁ = {lambda_exact:.4f}')
    axes[0].set_xlabel('Mode index n')
    axes[0].set_ylabel(r'Eigenvalue $\lambda_n$')
    axes[0].set_title(f'Ritz Procedure: Eigenvalue Approximation (N={N})')
    axes[0].legend(); axes[0].grid(True, alpha=0.4)

    # Rayleigh quotient vs a
    axes[1].plot(alpha_vals, J_vals, 'b-', lw=2)
    axes[1].axhline(y=lambda_exact, color='red', ls='--', lw=1.5,
                    label=f'Exact λ₁ = {lambda_exact:.4f}')
    axes[1].axvline(x=a_opt, color='green', ls=':', lw=1.5,
                    label=f'a_opt = {a_opt:.3f}, J_min = {J_min:.4f}')
    axes[1].set_xlabel(r'Trial parameter $a$')
    axes[1].set_ylabel('Rayleigh quotient $J(a)$')
    axes[1].set_title('Rayleigh Quotient vs Trial Parameter\n'
                     r'$u = \sin(\pi x) + a\sin(2\pi x)$')
    axes[1].legend(); axes[1].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 7-6: Ritz Procedure', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_7_6_ritz.png', dpi=150)
    plt.close()
    print("  [Saved] fig_7_6_ritz.png")


# ─────────────────────────────────────────────────────────────────────────────
# Chapter 8: Method of Moments
# ─────────────────────────────────────────────────────────────────────────────

def example_8_2_pocklington_mom():
    """
    Harrington Example 8-2: MoM for Thin Wire Antenna (Pocklington's equation)

    Pocklington's equation for thin wire of radius a, length L, driven at center:
        ∫_{-L/2}^{L/2} I(z') * G(z,z') dz' = V_inc / (j*ω*μ)

    Using Galerkin method with pulse basis and point matching:
        [Z]_ij = R_ij + j*X_ij
        V_i = V_inc at feed point, 0 elsewhere

    Green's function: G(z,z') = e^{-jk|z-z'|} / (4π|z-z'|)
    """
    print("\n  [Example 8-2: MoM for Thin Wire Antenna — Pocklington's Equation]")

    f = 300e6           # 300 MHz
    k = 2 * pi * f / c
    lambda_c = 2 * pi / k

    L = lambda_c / 2    # half-wave dipole
    a = 1e-3             # wire radius 1 mm
    N = 21               # number of basis functions (must be odd for center feed)
    dz = L / (N - 1)

    z = np.linspace(-L/2, L/2, N)   # observation points

    # Build impedance matrix Z_ij = ∫ G(z_i, z') * φ_j(z') dz'
    # Using pulse basis: φ_j(z') = 1 on segment j, 0 elsewhere
    Z = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            # Segment j center
            z_j = -L/2 + (j + 0.5) * dz
            # Integrate G from segment j: ∫_{z_j-dz/2}^{z_j+dz/2} G(z_i, z') dz'
            z_lo = z_j - dz / 2
            z_hi = z_j + dz / 2
            # Numerical integration over segment
            n_quad = 10
            z_quad = np.linspace(z_lo, z_hi, n_quad)
            for zq in z_quad:
                R = np.abs(z[i] - zq)
                if R < 1e-12:
                    R = 1e-12
                G = np.exp(-1j * k * R) / (4 * pi * R)
                Z[i, j] += G * dz / n_quad

    # Multiply by j*omega*mu for Pocklington
    Z = Z * 1j * omega(f) * mu_0

    # Excitation: V at center segment
    V = np.zeros(N)
    V[N//2] = 1.0     # 1 V delta gap source at center

    # Solve for currents
    I = solve(Z, V)

    # Input impedance
    Z_in = 1.0 / I[N//2] if abs(I[N//2]) > 1e-12 else np.inf
    Z_in_complex = Z_in

    print(f"  Frequency f = {f/1e6:.0f} MHz,  L = {L*1e2:.2f} cm")
    print(f"  Segments N = {N},  a = {a*1e3:.0f} mm")
    print(f"  Input impedance Z_in ≈ {np.abs(Z_in_complex):.2f} - j{np.abs(np.imag(Z_in_complex)):.2f} ohm")

    # Plot current distribution
    z_seg = np.linspace(-L/2, L/2, N)
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(z_seg*1e2, np.abs(I), 'b-o', ms=4, lw=1.5, label='|I|')
    axes[0].set_xlabel('z (cm)'); axes[0].set_ylabel('|I| (A)')
    axes[0].set_title(f'Half-wave Dipole: Current Distribution $|I(z)|$\n'
                     f'Z_in = {np.abs(Z_in):.2f} - j{np.abs(np.imag(Z_in)):.2f} Ω')
    axes[0].grid(True, alpha=0.4)
    axes[0].legend()

    axes[1].plot(z_seg*1e2, np.angle(I), 'r-o', ms=4, lw=1.5, label='∠I')
    axes[1].set_xlabel('z (cm)'); axes[1].set_ylabel('∠I (rad)')
    axes[1].set_title('Current Phase')
    axes[1].grid(True, alpha=0.4)
    axes[1].legend()

    plt.suptitle('Harrington Example 8-2: MoM for Thin Wire (Pocklington)',
                 fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_8_2_pocklington.png', dpi=150)
    plt.close()
    print("  [Saved] fig_8_2_pocklington.png")


def example_8_3_wire_grid_mom():
    """MoM for scattering from wire grid (2D periodic structure)."""
    print("\n  [Example 8-3: MoM for Wire Grid Structure]")

    # 2D wire grid: infinite array of parallel thin wires in x-direction
    # Spacing d, wire along y, incident plane wave E_x polarized
    f = 10e9
    k = 2 * pi * f / c
    lambda_c = 2 * pi / k

    d = lambda_c / 4     # grid spacing
    a = 1e-4             # wire radius
    N = 11               # number of basis functions per wire

    print(f"  f = {f/1e9:.0f} GHz, λ = {lambda_c*1e3:.2f} mm")
    print(f"  Wire spacing d = {d*1e3:.2f} mm, a = {a*1e6:.0f} μm")
    print(f"  Number of basis functions per wire N = {N}")

    # Build MoM matrix for single wire in infinite grid
    # Z_ij = (1/(4π)) * ∫∫ φ_i(z) * G(z,z') * φ_j(z') dz' dz
    # where G includes all wires (spectral domain)

    # Simplified: model current on one wire in presence of image wires
    x_positions = np.arange(-5, 6) * d   # 11 wires
    z = np.linspace(-lambda_c/2, lambda_c/2, N)
    dz = lambda_c / N

    # Z matrix for one wire
    Z = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            z_j = -lambda_c/2 + (j + 0.5) * dz
            z_lo = z_j - dz/2
            z_hi = z_j + dz/2
            n_quad = 8
            z_quad = np.linspace(z_lo, z_hi, n_quad)
            for zq in z_quad:
                # Sum contributions from all wires
                G_total = 0.0j
                for x_pos in x_positions:
                    R = np.sqrt(x_pos**2 + (z[i] - zq)**2)
                    if R < 1e-12:
                        R = 1e-12
                    G_total += np.exp(-1j * k * R) / (4 * pi * R)
                Z[i, j] += G_total * dz / n_quad

    Z = Z * 1j * omega(f) * mu_0

    # Incident field: plane wave E_x = E0 * exp(-jkz)
    E_inc = np.ones(N)   # at wire positions
    V = E_inc

    I = solve(Z, V)
    print(f"  Max |I| on wire = {np.max(np.abs(I)):.4f} A")

    # Reflection coefficient for wire grid (simplified)
    Z_0_grid = 377 / (1 + 2/(k*d))  # approximate grid impedance
    print(f"  Grid characteristic impedance ≈ {Z_0_grid:.2f} ohm")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(z*1e2, np.abs(I), 'b-', lw=2)
    axes[0].set_xlabel('z (cm)')
    axes[0].set_ylabel('|I| (A)')
    axes[0].set_title(f'Wire Grid: Current Distribution $|I(z)|$\n'
                     f'd = λ/4, N = {N} basis functions')
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(z*1e2, np.angle(I), 'r-', lw=2)
    axes[1].set_xlabel('z (cm)')
    axes[1].set_ylabel('∠I (rad)')
    axes[1].set_title('Current Phase Distribution')
    axes[1].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 8-3: Wire Grid MoM', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_8_3_wire_grid.png', dpi=150)
    plt.close()
    print("  [Saved] fig_8_3_wire_grid.png")


def example_8_5_strip_mom():
    """MoM for scattering from a thin conducting strip (2D problem)."""
    print("\n  [Example 8-5: MoM for Conducting Strip Scattering]")

    f = 10e9
    k = 2 * pi * f / c
    lambda_c = 2 * pi / k

    # Strip: width W, along x-direction, infinite in y
    W = lambda_c / 2
    N = 21               # pulse basis functions

    x = np.linspace(-W/2, W/2, N)
    dx = W / N

    # Electric Field Integral Equation (EFIE) for strip
    # Z_ij = (1/(4π)) * ∫_{-W/2}^{W/2} G(x_i, x') dx' * j*ω*μ
    Z = np.zeros((N, N), dtype=complex)
    for i in range(N):
        for j in range(N):
            x_j = x[j]
            x_lo = x_j - dx/2
            x_hi = x_j + dx/2
            n_quad = 8
            x_quad = np.linspace(x_lo, x_hi, n_quad)
            for xq in x_quad:
                R = np.abs(x[i] - xq)
                if R < 1e-12:
                    R = 1e-12
                G = np.exp(-1j * k * R) / (4 * pi * R)
                Z[i, j] += G * dx / n_quad

    Z = Z * 1j * omega(f) * mu_0

    # Incident plane wave: e^{-jkx} (x-polarized)
    E_inc = np.exp(-1j * k * x)
    V = E_inc

    I = solve(Z, V)

    # Surface current J_s = I/dx
    J_s = I / dx

    print(f"  Strip width W = {W*1e3:.2f} mm, f = {f/1e9:.0f} GHz")
    print(f"  Max |J_s| = {np.max(np.abs(J_s)):.4f} A/m")

    # Radar cross section: σ = (4/π) * |∫ J_s * exp(j*k*x) dx|²
    integral_J = np.trapezoid(J_s * np.exp(1j * k * x), x)
    sigma_norm = 4 / pi * np.abs(integral_J)**2   # normalized to (λ/π)
    print(f"  Normalized RCS ≈ {sigma_norm:.4f}")

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].plot(x*1e3, np.abs(J_s), 'b-', lw=2)
    axes[0].set_xlabel('x (mm)')
    axes[0].set_ylabel(r'$|J_y|$ (A/m)')
    axes[0].set_title(f'Strip: Surface Current $|J_y(x)|$\n'
                     f'W = {W*1e3:.2f} mm, N = {N}')
    axes[0].grid(True, alpha=0.4)

    axes[1].plot(x*1e3, np.angle(J_s), 'r-', lw=2)
    axes[1].set_xlabel('x (mm)')
    axes[1].set_ylabel(r'∠$J_y$ (rad)')
    axes[1].set_title('Current Phase')
    axes[1].grid(True, alpha=0.4)

    plt.suptitle('Harrington Example 8-5: MoM for Strip Scattering', fontsize=12)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_8_5_strip_mom.png', dpi=150)
    plt.close()
    print("  [Saved] fig_8_5_strip_mom.png")


def omega(freq):
    return 2 * pi * freq


if __name__ == '__main__':
    print("=== Harrington Ch7 & Ch8: Variational and MoM ===")
    example_7_5_dielectric_perturbation()
    example_7_6_ritz_procedure()
    example_8_2_pocklington_mom()
    example_8_3_wire_grid_mom()
    example_8_5_strip_mom()
    print("\n  All Chapter 7-8 examples complete.")
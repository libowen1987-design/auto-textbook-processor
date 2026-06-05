"""
Balanis Ch8 — Integral Equations, Method of Moments (MoM)

Implements:
  - Hallén integral equation for thin wire antennas
  - Pulse basis + point-matching MoM
  - Current distribution, input impedance, mutual impedance
  - Far-field pattern computation from MoM currents
  - Convergence analysis

References: Balanis 4E Ch.8, Harrington (1993), Gibson (2015)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import time

# Physical constants
C0 = 3e8                        # speed of light [m/s]
ETA_0 = 120.0 * np.pi           # free-space impedance [Ω] ≈ 376.99
MU0 = 4e-7 * np.pi              # permeability [H/m] ≈ 1.257e-6
EPS0 = 8.854e-12                # permittivity [F/m]
PI = np.pi

# Output directory
FIG_DIR = 'figures/ch08'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# MoM Core: Hallén Integral Equation with Pulse Basis + Point Matching
# =========================================================================

def build_hallen_matrix(N_segments: int, l_length: float,
                         a_radius: float, k_wavenumber: float,
                         n_quad: int = 41) -> np.ndarray:
    """Build the Hallén interaction matrix ψ_mn.

    ψ_mn = ∫_{segment n} e^{-jkR_m(z')} / (4π R_m(z')) dz'

    where R_m(z') = √[(z_m - z')² + a²]

    Parameters
    ----------
    N_segments : int
    l_length : float
        Total dipole length [m]
    a_radius : float
        Wire radius [m]
    k_wavenumber : float
        Free-space wavenumber [rad/m]
    n_quad : int
        Fixed quadrature points per segment

    Returns
    -------
    PSI : ndarray (N, N)
        Interaction matrix
    z_mid : ndarray (N,)
        Segment center positions [m]
    """
    delta_z = l_length / N_segments
    z_mid = np.linspace(-l_length/2 + delta_z/2,
                         l_length/2 - delta_z/2, N_segments)

    PSI = np.zeros((N_segments, N_segments), dtype=complex)

    for m in range(N_segments):
        z_m = z_mid[m]
        for n in range(N_segments):
            z_n_min = -l_length/2 + n * delta_z
            z_n_max = z_n_min + delta_z

            # Adaptive quadrature: more points when source ≈ observation
            dist = abs(z_m - (z_n_min + z_n_max) / 2)
            nq = max(n_quad, int(delta_z / max(a_radius, dist * 0.1)))
            nq = min(nq, 201)  # cap for performance
            qp = np.linspace(z_n_min, z_n_max, nq)
            R = np.sqrt((z_m - qp)**2 + a_radius**2)
            G = np.exp(-1j * k_wavenumber * R) / (4 * PI * R)
            PSI[m, n] = np.trapezoid(G, qp)

    return PSI, z_mid


def solve_hallen_mom(N_segments: int, l_length: float,
                      frequency: float, a_radius: float,
                      n_quad: int = 41) -> tuple:
    """Solve Hallén integral equation by MoM for wire antenna.

    Hallén equation (Balanis 8-31):
      ∫ I(z') e^{-jkR}/(4πR) dz' = C₁ cos(kz)
                                    + j/(2η) ∫₀^z E_z^inc(z') sin[k(z-z')] dz'

    For delta-gap at z=0 (V₀=1), the particular integral gives:
      -j/(2η) sin(k|z|)   (with correct sign)

    Enforcement of I(±l/2) = 0 determines C₁.

    Parameters
    ----------
    N_segments : int
    l_length : float
        Total dipole length [m]
    frequency : float
        Operating frequency [Hz]
    a_radius : float
        Wire radius [m]
    n_quad : int
        Quadrature points per segment

    Returns
    -------
    z_mid : ndarray (N,)
        Segment centers [m]
    I_current : ndarray (N,)
        Complex current distribution [A]
    Z_in : complex
        Input impedance [Ω]
    C1 : complex
        Hallén integration constant
    """
    k = 2 * PI * frequency / C0

    PSI, z_mid = build_hallen_matrix(N_segments, l_length, a_radius,
                                      k, n_quad)

    cos_kz = np.cos(k * z_mid)
    # Particular integral: -j/(2η) sin(k|z|) for delta-gap (V₀=1)
    exc = -1j / (2 * ETA_0) * np.sin(k * np.abs(z_mid))

    # Solve PSI·I = C₁·cos(kz) + exc
    # Method: I = I_p + C₁·I_h
    # where PSI·I_h = cos(kz), PSI·I_p = exc
    try:
        PSI_inv = np.linalg.inv(PSI)
    except np.linalg.LinAlgError:
        raise RuntimeError("PSI matrix is singular; "
                           "try different N or a_radius")

    I_h = PSI_inv @ cos_kz
    I_p = PSI_inv @ exc

    # Enforce I = 0 at z = -l/2 (first segment center)
    C1 = -I_p[0] / I_h[0]
    I_current = I_p + C1 * I_h

    feed_idx = N_segments // 2
    Z_in = 1.0 / I_current[feed_idx]

    return z_mid, I_current, Z_in, C1


# =========================================================================
# Mutual Impedance (two parallel dipoles via Hallén MoM)
# =========================================================================

def solve_two_dipole_mom(N_segments: int, l_length: float,
                          d_spacing: float,
                          frequency: float, a_radius: float) -> complex:
    """Compute mutual impedance Z_21 between two parallel half-wave dipoles.

    Uses coupled Hallén equations for two parallel wires.
    This is a simplified approach: use induced EMF from the MoM current
    on dipole 1 to compute the open-circuit voltage on dipole 2.

    Parameters
    ----------
    N_segments : int
    l_length : float
        Dipole length [m]
    d_spacing : float
        Center-to-center spacing [m]
    frequency : float
        [Hz]
    a_radius : float
        [m]

    Returns
    -------
    Z_21 : complex
        Mutual impedance [Ω]
    """
    k = 2 * PI * frequency / C0
    delta_z = l_length / N_segments

    # Self matrix for one dipole (standard Hallén)
    PSI, z_mid = build_hallen_matrix(N_segments, l_length, a_radius, k, 31)

    cos_kz = np.cos(k * z_mid)
    exc = -1j / (2 * ETA_0) * np.sin(k * np.abs(z_mid))

    PSI_inv = np.linalg.inv(PSI)
    I_h = PSI_inv @ cos_kz
    I_p = PSI_inv @ exc
    C1_drive = -I_p[0] / I_h[0]
    I_drive = I_p + C1_drive * I_h  # current on driven dipole (in isolation)

    # Mutual interaction matrix: field from dipole 1 observed at dipole 2
    # For two parallel dipoles offset by d in y-direction
    PSI_mut = np.zeros((N_segments, N_segments), dtype=complex)

    for m in range(N_segments):
        z_m = z_mid[m]  # observation on dipole 2
        for n in range(N_segments):
            z_n_min = -l_length/2 + n * delta_z
            z_n_max = z_n_min + delta_z
            # Distance between point on dipole 2 and source on dipole 1
            # R = sqrt((z_m - z')² + d² + a²) (add a to avoid singularity)
            nq = max(31, int(delta_z / a_radius))
            nq = min(nq, 151)
            qp = np.linspace(z_n_min, z_n_max, nq)
            R = np.sqrt((z_m - qp)**2 + d_spacing**2 + a_radius**2)
            G = np.exp(-1j * k * R) / (4 * PI * R)
            PSI_mut[m, n] = np.trapezoid(G, qp)

    # The induced current on dipole 2:
    # PSI_self · I_2 = C2·cos(kz) - PSI_mut · I_1
    # For open circuit: the induced dipole 2 has I₂ = 0 at its terminals
    # Standard approach: Z₂₁ = -I₁·PSI_mut / (I₁·cos(kz))

    # Simplified: mutual impedance from induced EMF
    # The open-circuit voltage on dipole 2 from dipole 1's current:
    # V_2 = -jω ∫ I₁(z') G(z=0, z') dz'  (at the feed of dipole 2)
    # For Hallén: the RHS of dipole 2 equation is C₂cos(kz) + exc_induced
    # where exc_induced(z) = -∫ I₁(z') · G_mut(z,z') dz'

    induced_field = PSI_mut @ I_drive  # this is the RHS modification

    # Solve for dipole 2 currents with I₂ = 0 at ends
    # PSI · I₂ = C₂·cos(kz) - induced_field
    # I₂ = I_h·C₂ - (PSI⁻¹ · induced_field)
    I_p2 = -PSI_inv @ induced_field  # particular solution for dipole 2
    C2 = -I_p2[0] / I_h[0]  # enforce I₂ = 0 at end
    I_2 = I_p2 + C2 * I_h

    # Mutual impedance Z₂₁ = V_{2,oc} / I₁_feed
    # For induced EMF method:
    # Z₂₁ = - (1/I₁_feed) * ∫ E_12(z') · I₂_h(z') dz'  (reciprocity)
    # Simplified: Z₂₁ ≈ -(PSI_mut @ I_drive)[feed] / I_drive[feed]
    # Actually: Z₂₁ = -(induced_field at feed)/I_drive_feed
    feed = N_segments // 2
    Z_21 = -induced_field[feed] / I_drive[feed]
    return Z_21


# =========================================================================
# Far-Field Pattern from MoM Current
# =========================================================================

def compute_far_field(z_mid: np.ndarray, I_current: np.ndarray,
                       theta_angles: np.ndarray,
                       l_length: float, frequency: float) -> np.ndarray:
    """Far-field E_θ from Hallén MoM current distribution.

    E_θ(θ) = jη·(e^{-jkr}/(2λr))·sinθ · Σ I_n · ∫ exp(jkz'cosθ) dz'

    Parameters
    ----------
    z_mid : ndarray
        Segment centers [m]
    I_current : ndarray
        MoM current [A]
    theta_angles : ndarray
        Observation angles [rad]
    l_length : float
        Dipole length [m]
    frequency : float
        [Hz]

    Returns
    -------
    E_theta : ndarray
        Normalized far-field pattern
    """
    k = 2 * PI * frequency / C0
    N_segments = len(I_current)
    delta_z = l_length / N_segments

    E_theta = np.zeros(len(theta_angles), dtype=complex)

    for i, theta in enumerate(theta_angles):
        sin_theta = np.sin(theta)
        if np.abs(sin_theta) < 1e-12:
            E_theta[i] = 0.0
            continue

        pattern_sum = 0.0 + 0.0j
        for n in range(N_segments):
            z_n = z_mid[n]
            z_n_min = z_n - delta_z / 2
            z_n_max = z_n + delta_z / 2

            # ∫ exp(jkz'cosθ) dz' over segment
            nq = 21
            zq = np.linspace(z_n_min, z_n_max, nq)
            phase = np.exp(1j * k * zq * np.cos(theta))
            phase_int = np.trapezoid(phase, zq)
            pattern_sum += I_current[n] * phase_int

        E_theta[i] = sin_theta * pattern_sum

    # Normalize
    max_val = np.max(np.abs(E_theta))
    if max_val > 0:
        E_theta /= max_val

    return E_theta


def ideal_sine_pattern(theta: np.ndarray, l_length: float,
                        frequency: float) -> np.ndarray:
    """Ideal sinusoidal current pattern for a center-fed dipole.

    I(z) ∝ sin[k(l/2 - |z|)], giving:
    E(θ) ∝ [cos(kl/2·cosθ) - cos(kl/2)] / sinθ
    """
    k = 2 * PI * frequency / C0
    kl2 = k * l_length / 2
    E = np.zeros(len(theta), dtype=complex)
    for i, t in enumerate(theta):
        sint = np.sin(t)
        if np.abs(sint) < 1e-12:
            E[i] = 0.0
            continue
        num = np.cos(kl2 * np.cos(t)) - np.cos(kl2)
        E[i] = num / sint
    max_val = np.max(np.abs(E))
    if max_val > 0:
        E /= max_val
    return E


# =========================================================================
# Example 1: Hallén Interaction Matrix Visualization
# =========================================================================

def example1_hallen_matrix():
    """Visualize the Hallén interaction matrix for a half-wave dipole."""
    print("=" * 60)
    print("Example 1: Hallén Interaction Matrix Structure")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    l_length = lam / 2
    a_radius = lam / 200
    k = 2 * PI * freq / C0

    N_seg = 9  # small for readability
    PSI, z_mid = build_hallen_matrix(N_seg, l_length, a_radius, k)

    print(f"  f = {freq/1e6:.0f} MHz, λ = {lam:.3f} m")
    print(f"  l = {l_length:.3f} m = λ/2")
    print(f"  a = λ/{lam/a_radius:.0f}")
    print(f"  Segments N = {N_seg}")

    # Also compute with larger N for structure visualization
    PSI_large, _ = build_hallen_matrix(51, l_length, a_radius, k, 31)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    im0 = axes[0].imshow(np.abs(PSI), cmap='viridis')
    axes[0].set_title(r'$|\psi_{mn}|$ (N=9)')
    axes[0].set_xlabel('Source segment n')
    axes[0].set_ylabel('Test segment m')
    plt.colorbar(im0, ax=axes[0])

    im1 = axes[1].imshow(np.angle(PSI), cmap='RdBu', vmin=-PI, vmax=PI)
    axes[1].set_title(r'$\angle\psi_{mn}$ (rad)')
    axes[1].set_xlabel('Source segment n')
    axes[1].set_ylabel('Test segment m')
    plt.colorbar(im1, ax=axes[1])

    # Symmetry check
    asym = np.abs(PSI_large - PSI_large.T)
    max_asym = np.max(asym)
    im2 = axes[2].imshow(asym, cmap='hot')
    axes[2].set_title(r'$|\psi - \psi^T|$ (max={:.1e})'.format(max_asym))
    axes[2].set_xlabel('Source segment n')
    axes[2].set_ylabel('Test segment m')
    plt.colorbar(im2, ax=axes[2])

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex01_hallen_matrix.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex01_hallen_matrix.png")
    print(f"  Max asymmetry = {max_asym:.2e}")

    # Print diagonal
    print("  Diagonal ψ_mm:")
    for m in range(N_seg):
        print(f"    ψ_{{{m}{m}}} = {PSI[m,m]:.6e}")

    return PSI


# =========================================================================
# Example 2: MoM Current Distribution
# =========================================================================

def example2_current_distribution():
    """Current distribution for l = λ/2, λ, 1.5λ using Hallén MoM."""
    print("\n" + "=" * 60)
    print("Example 2: MoM Current Distribution")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    a_radius = lam / 500
    N_seg = 101

    length_factors = [0.5, 1.0, 1.5]
    colors = ['b', 'r', 'g']
    labels = [r'$l=\lambda/2$', r'$l=\lambda$', r'$l=1.5\lambda$']

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    for lf, c, lab in zip(length_factors, colors, labels):
        l_length = lf * lam
        z_mid, I_cur, Z_in, C1 = solve_hallen_mom(
            N_seg, l_length, freq, a_radius)

        norm_I = np.abs(I_cur) / np.max(np.abs(I_cur))
        z_norm = z_mid / lam
        phase_I = np.angle(I_cur)

        axes[0].plot(z_norm, norm_I, f'{c}-', label=lab, linewidth=1.5)
        axes[1].plot(z_norm, phase_I, f'{c}-', label=lab, linewidth=1.5,
                     alpha=0.8)

        print(f"  {lab}:")
        print(f"    Z_in = {Z_in.real:.2f} + j{Z_in.imag:.2f} Ω")
        print(f"    |I_feed| = {np.abs(I_cur[N_seg//2]):.6f} A")
        print(f"    C₁ = {C1:.4e}")

    axes[0].set_xlabel(r'$z / \lambda$')
    axes[0].set_ylabel(r'$|I(z)| / \max(|I|)$')
    axes[0].set_title('Normalized Current Magnitude')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].set_xlabel(r'$z / \lambda$')
    axes[1].set_ylabel(r'$\angle I(z)$ (rad)')
    axes[1].set_title('Current Phase')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex02_current_distribution.png', dpi=150)
    plt.close()
    print(f"\n  → Saved {FIG_DIR}/ex02_current_distribution.png")


# =========================================================================
# Example 3: Input Impedance vs Dipole Length
# =========================================================================

def example3_input_impedance():
    """Scan Z_in vs l/λ from 0.1 to 2.0."""
    print("\n" + "=" * 60)
    print("Example 3: Input Impedance vs Dipole Length")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    a_radius = lam / 500
    N_seg = 51  # moderate N for speed

    l_over_lambda = np.linspace(0.1, 2.0, 150)
    Z_in_arr = np.zeros(len(l_over_lambda), dtype=complex)

    t_start = time.time()
    for i, lol in enumerate(l_over_lambda):
        l_length = lol * lam
        try:
            _, _, Z_in, _ = solve_hallen_mom(N_seg, l_length, freq, a_radius,
                                              n_quad=21)
            Z_in_arr[i] = Z_in
        except (RuntimeError, np.linalg.LinAlgError):
            Z_in_arr[i] = 0.0 + 0.0j  # placeholder for failed cases
        if (i + 1) % 50 == 0:
            elapsed = time.time() - t_start
            print(f"    Progress: {i+1}/{len(l_over_lambda)} ({elapsed:.1f}s)")
    t_total = time.time() - t_start
    print(f"  Total time: {t_total:.1f}s")

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(l_over_lambda, Z_in_arr.real, 'b-', linewidth=1.5)
    axes[0].set_ylabel(r'$R_{\mathrm{in}}$ (Ω)')
    axes[0].set_title('Input Resistance vs Dipole Length')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(l_over_lambda, Z_in_arr.imag, 'r-', linewidth=1.5)
    axes[1].set_xlabel(r'$l / \lambda$')
    axes[1].set_ylabel(r'$X_{\mathrm{in}}$ (Ω)')
    axes[1].set_title('Input Reactance vs Dipole Length')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex03_input_impedance.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex03_input_impedance.png")

    # Key values
    half_idx = np.argmin(np.abs(l_over_lambda - 0.5))
    wave_idx = np.argmin(np.abs(l_over_lambda - 1.0))
    print(f"\n  Key values:")
    print(f"    l/λ=0.50: Z_in = {Z_in_arr[half_idx].real:.1f} "
          f"+ j{Z_in_arr[half_idx].imag:.1f} Ω")
    print(f"    l/λ=1.00: Z_in = {Z_in_arr[wave_idx].real:.1f} "
          f"+ j{Z_in_arr[wave_idx].imag:.1f} Ω")

    return l_over_lambda, Z_in_arr


# =========================================================================
# Example 4: Mutual Impedance vs Spacing
# =========================================================================

def example4_mutual_impedance():
    """Mutual impedance between two parallel half-wave dipoles vs d/λ."""
    print("\n" + "=" * 60)
    print("Example 4: Mutual Impedance vs Dipole Spacing")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    l_length = lam / 2
    a_radius = lam / 500
    N_seg = 41

    d_over_lambda = np.linspace(0.1, 1.0, 15)
    Z_21_arr = np.zeros(len(d_over_lambda), dtype=complex)

    t_start = time.time()
    for i, dol in enumerate(d_over_lambda):
        d = dol * lam
        try:
            Z_21 = solve_two_dipole_mom(N_seg, l_length, d, freq, a_radius)
            Z_21_arr[i] = Z_21
        except (RuntimeError, np.linalg.LinAlgError):
            Z_21_arr[i] = 0.0 + 0.0j
        if (i + 1) % 5 == 0:
            elapsed = time.time() - t_start
            print(f"    Progress: {i+1}/{len(d_over_lambda)} "
                  f"({elapsed:.1f}s)")
    t_total = time.time() - t_start
    print(f"  Total time: {t_total:.1f}s")

    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    axes[0].plot(d_over_lambda, Z_21_arr.real, 'b.-', linewidth=1.5)
    axes[0].set_ylabel(r'$R_{21}$ (Ω)')
    axes[0].set_title('Mutual Resistance vs Spacing')
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(d_over_lambda, Z_21_arr.imag, 'r.-', linewidth=1.5)
    axes[1].set_xlabel(r'$d / \lambda$')
    axes[1].set_ylabel(r'$X_{21}$ (Ω)')
    axes[1].set_title('Mutual Reactance vs Spacing')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex04_mutual_impedance.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex04_mutual_impedance.png")

    print(f"\n  Selected values:")
    for dol, z21 in zip(d_over_lambda, Z_21_arr):
        print(f"    d/λ = {dol:.2f}: Z_21 = {z21.real:7.2f} "
              f"+ j{z21.imag:7.2f} Ω")

    return d_over_lambda, Z_21_arr


# =========================================================================
# Example 5: Radiation Patterns
# =========================================================================

def example5_radiation_patterns():
    """Far-field patterns: Hallén MoM current vs ideal sinusoidal current."""
    print("\n" + "=" * 60)
    print("Example 5: Radiation Patterns from MoM Current")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    a_radius = lam / 500
    N_seg = 101
    theta = np.linspace(0, PI, 361)

    length_factors = [0.5, 1.0, 1.5]
    colors = ['b', 'r', 'g']

    fig, axes = plt.subplots(1, 2, figsize=(14, 6),
                             subplot_kw={'projection': 'polar'})

    for idx, lf in enumerate(length_factors):
        l_length = lf * lam
        c = colors[idx]

        z_mid, I_cur, Z_in, _ = solve_hallen_mom(
            N_seg, l_length, freq, a_radius)

        E_mom = compute_far_field(z_mid, I_cur, theta, l_length, freq)
        E_sine = ideal_sine_pattern(theta, l_length, freq)

        lab_mom = lab_str(lf)
        lab_sine = f'Sine {lab_str(lf)}'

        axes[0].plot(theta, np.abs(E_mom), f'{c}-',
                     label=lab_mom, linewidth=1.5)
        axes[0].plot(theta, np.abs(E_sine), f'{c}--',
                     label=lab_sine, linewidth=1.0, alpha=0.6)

        E_mom_dB = 20 * np.log10(np.maximum(np.abs(E_mom), 1e-4))
        E_sine_dB = 20 * np.log10(np.maximum(np.abs(E_sine), 1e-4))

        axes[1].plot(theta, E_mom_dB, f'{c}-',
                     label=lab_mom, linewidth=1.5)
        axes[1].plot(theta, E_sine_dB, f'{c}--',
                     label=lab_sine, linewidth=1.0, alpha=0.6)

        print(f"  {lab_str(lf)}: Z_in = {Z_in.real:.2f} "
              f"+ j{Z_in.imag:.2f} Ω")

    axes[0].set_title('Normalized Pattern (Linear)', va='bottom')
    axes[0].legend(loc='lower right', fontsize=8)

    axes[1].set_title('Normalized Pattern (dB)', va='bottom')
    axes[1].set_ylim(-40, 0)
    axes[1].legend(loc='lower right', fontsize=8)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex05_radiation_patterns.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex05_radiation_patterns.png")


def lab_str(lf):
    """Generate LaTeX label for length factor."""
    if abs(lf - 0.5) < 0.01:
        return r'$l=\lambda/2$'
    elif abs(lf - 1.0) < 0.01:
        return r'$l=\lambda$'
    elif abs(lf - 1.5) < 0.01:
        return r'$l=1.5\lambda$'
    else:
        return f'$l={lf:.1f}\\lambda$'


# =========================================================================
# Example 6: Convergence with Segment Count
# =========================================================================

def example6_convergence():
    """Study Z_in convergence vs number of segments for λ/2 dipole."""
    print("\n" + "=" * 60)
    print("Example 6: Convergence Analysis (Z_in vs N)")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    l_length = lam / 2

    # Test different wire radii
    a_values = [lam / 200, lam / 500, lam / 1000]
    N_values = np.array([11, 21, 31, 41, 51, 61, 81, 101, 121])

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))

    for a_val, color in zip(a_values, ['b', 'r', 'g']):
        Z_vals = np.zeros(len(N_values), dtype=complex)
        a_label = f'a=λ/{lam/a_val:.0f}'

        for i, N in enumerate(N_values):
            try:
                _, _, Z_in, _ = solve_hallen_mom(N, l_length, freq, a_val,
                                                  n_quad=31)
                Z_vals[i] = Z_in
            except (RuntimeError, np.linalg.LinAlgError):
                Z_vals[i] = np.nan + 1j * np.nan

        good = ~np.isnan(Z_vals.real)
        if np.any(good):
            axes[0].plot(N_values[good], Z_vals[good].real,
                         f'{color}.-', label=a_label, linewidth=1.5)
            axes[1].plot(N_values[good], Z_vals[good].imag,
                         f'{color}.-', label=a_label, linewidth=1.5)

            final_val = Z_vals[good][-1]
            print(f"  {a_label}: Z_in(N_max) = {final_val.real:.2f} "
                  f"+ j{final_val.imag:.2f} Ω")

    axes[0].axhline(73.1, color='k', linestyle='--', alpha=0.4,
                    label='Theory (73.1)')
    axes[0].set_ylabel(r'$R_{\mathrm{in}}$ (Ω)')
    axes[0].set_title('Input Resistance vs Number of Segments')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].axhline(42.5, color='k', linestyle='--', alpha=0.4,
                    label='Theory (42.5)')
    axes[1].set_xlabel('Number of Segments N')
    axes[1].set_ylabel(r'$X_{\mathrm{in}}$ (Ω)')
    axes[1].set_title('Input Reactance vs Number of Segments')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex06_convergence.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex06_convergence.png")

    return N_values, a_values


# =========================================================================
# Example 7: Pocklington Equation via Integration-by-Parts
# =========================================================================

def example7_pocklington_ibp():
    """Demonstrate Pocklington IE using integration-by-parts.

    This uses the reduced-kernel approach:
    Z_mn = -1/(j4πωε₀) × [∂G₀/∂z' at segment boundaries + k²∫G₀ dz']

    where G₀ = e^{-jkR}/R.  The method eliminates the second derivative
    and only requires first-derivative endpoint terms.
    """
    print("\n" + "=" * 60)
    print("Example 7: Pocklington IE via Integration-by-Parts")
    print("=" * 60)

    freq = 300e6
    lam = C0 / freq
    a_radius = lam / 500
    k = 2 * PI * freq / C0
    N_seg = 101
    l_length = lam / 2
    delta_z = l_length / N_seg

    z_bound = np.linspace(-l_length/2, l_length/2, N_seg + 1)
    z_mid = np.linspace(-l_length/2 + delta_z/2,
                         l_length/2 - delta_z/2, N_seg)
    feed = N_seg // 2

    w = 2 * PI * freq
    pre = -1.0 / (1j * 4 * PI * w * EPS0)

    def dG0_dzprime(obs_z, src_z):
        """∂G₀/∂z' = +(1+jkR)(z-z')/R³ × e^{-jkR}"""
        dz_ = obs_z - src_z
        R = np.sqrt(dz_**2 + a_radius**2)
        return (1 + 1j * k * R) * dz_ / R**3 * np.exp(-1j * k * R)

    def int_G0(obs_z, z0, z1):
        nq = max(41, int((z1 - z0) / a_radius))
        nq = min(nq, 201)
        qp = np.linspace(z0, z1, nq)
        R = np.sqrt((obs_z - qp)**2 + a_radius**2)
        return np.trapezoid(np.exp(-1j * k * R) / R, qp)

    print("  Building Pocklington Z matrix (N=101)...")
    Z = np.zeros((N_seg, N_seg), dtype=complex)
    for m in range(N_seg):
        zm = z_mid[m]
        for n in range(N_seg):
            ep = dG0_dzprime(zm, z_bound[n + 1])
            em = dG0_dzprime(zm, z_bound[n])
            vol = int_G0(zm, z_bound[n], z_bound[n + 1])
            Z[m, n] = pre * ((ep - em) + k**2 * vol)

    # Solve with delta-gap excitation
    V = np.zeros(N_seg, dtype=complex)
    V[feed] = 1.0 / delta_z

    I = np.linalg.solve(Z, V)
    Z_in = 1.0 / I[feed]

    I_norm = np.abs(I) / np.max(np.abs(I))
    print(f"  Z_in(IBP) = {Z_in.real:.2f} + j{Z_in.imag:.2f} Ω")
    print(f"  I_ends = {I_norm[0]:.4f}, {I_norm[-1]:.4f}")

    # Plot comparison: Pocklington IBP vs Hallén
    _, I_ref, Z_ref, _ = solve_hallen_mom(N_seg, l_length, freq, a_radius)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(z_mid / lam, np.abs(I) / np.max(np.abs(I)),
            'b-', label='Pocklington (IBP)', linewidth=1.5)
    ax.plot(z_mid / lam, np.abs(I_ref) / np.max(np.abs(I_ref)),
            'r--', label='Hallén MoM', linewidth=1.5)

    ax.set_xlabel(r'$z / \lambda$')
    ax.set_ylabel('Normalized |I(z)|')
    ax.set_title(
        f'Pocklington vs Hallén: Z_in = {Z_in.real:.1f}+j{Z_in.imag:.1f} Ω '
        f'vs {Z_ref.real:.1f}+j{Z_ref.imag:.1f} Ω')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(f'{FIG_DIR}/ex07_pocklington_vs_hallen.png', dpi=150)
    plt.close()
    print(f"  → Saved {FIG_DIR}/ex07_pocklington_vs_hallen.png")

    return Z_in, Z_ref


# =========================================================================
# Main
# =========================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Balanis Ch8: Integral Equations, Method of Moments")
    print("Solver: Hallén IE → MoM (pulse basis + point matching)")
    print("=" * 60)

    # Example 1: Hallén matrix structure
    example1_hallen_matrix()

    # Example 2: Current distribution
    example2_current_distribution()

    # Example 3: Input impedance vs length
    example3_input_impedance()

    # Example 4: Mutual impedance
    example4_mutual_impedance()

    # Example 5: Radiation patterns
    example5_radiation_patterns()

    # Example 6: Convergence
    example6_convergence()

    # Example 7: Pocklington IBP comparison
    example7_pocklington_ibp()

    print("\n" + "=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)

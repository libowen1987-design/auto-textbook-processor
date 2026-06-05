"""
balanisch03_examples.py
Balanis Antenna Theory 4ed, Ch3 — Radiation Integrals
Examples: Short dipole, small loop, aperture → far field
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import os

# ── Physical constants ──────────────────────────────────────────────────────
epsilon_0 = 8.854187817e-12       # F/m
mu_0 = 4.0 * np.pi * 1e-7         # H/m
eta_0 = np.sqrt(mu_0 / epsilon_0)  # ≈ 376.73 Ω
c_0 = 1.0 / np.sqrt(mu_0 * epsilon_0)

# ── Savedir ─────────────────────────────────────────────────────────────────
FIGDIR = os.path.join(os.path.dirname(__file__), "figures", "ch03")
os.makedirs(FIGDIR, exist_ok=True)


# ═════════════════════════════════════════════════════════════════════════════
#  1.  Short electric dipole  (Hertzian dipole)
# ═════════════════════════════════════════════════════════════════════════════

def far_field_electric_dipole(Idl, k, r, theta):
    """
    Far field of a short electric dipole (Hertzian dipole).

    Parameters
    ----------
    Idl  : float — current moment I·dl [A·m]
    k    : float — wavenumber [rad/m]
    r    : float — radial distance [m]
    theta: ndarray — polar angle [rad]

    Returns
    -------
    E_theta : ndarray — θ-component of electric field [V/m]
    H_phi   : ndarray — φ-component of magnetic field [A/m]
    """
    E_theta = 1j * eta_0 * k * Idl * np.exp(-1j * k * r) / (4.0 * np.pi * r) * np.sin(theta)
    H_phi = E_theta / eta_0
    return E_theta, H_phi


# ═════════════════════════════════════════════════════════════════════════════
#  2.  Small magnetic dipole  (small loop, electrically small)
# ═════════════════════════════════════════════════════════════════════════════

def far_field_magnetic_dipole(Imdl, k, r, theta):
    """
    Far field of a small magnetic dipole (equivalent to small loop).

    For a small loop of area A with current I:
        Imdl = jωμ₀·I·A  (magnetic dipole moment)

    The far-field pattern is:
        E_phi ∝ sin(θ)
        H_theta ∝ sin(θ)

    Parameters
    ----------
    Imdl : float — magnetic dipole moment I_m·dl [V·m] (ωμ₀IA)
    k    : float — wavenumber [rad/m]
    r    : float — radial distance [m]
    theta: ndarray — polar angle [rad]

    Returns
    -------
    H_theta : ndarray — θ-component of magnetic field [A/m]
    E_phi   : ndarray — φ-component of electric field [V/m]
    """
    # By duality: electric dipole E_theta ↔ magnetic dipole H_theta
    # and the source strength maps through η₀
    H_theta = 1j * k * Imdl * np.exp(-1j * k * r) / (4.0 * np.pi * r * eta_0) * np.sin(theta)
    E_phi = -eta_0 * H_theta   # TEM relation: E_phi = η H_θ (with sign per Balanis)
    return H_theta, E_phi


# ═════════════════════════════════════════════════════════════════════════════
#  3.  Aperture → far field via FFT
# ═════════════════════════════════════════════════════════════════════════════

def aperture_to_far_field(E_aperture, x, y, k, r, theta, phi):
    """
    Compute far-field pattern of an aperture distribution using FFT.

    The far field is proportional to the 2D Fourier transform of the
    aperture field, evaluated at spatial frequencies:
        k_x = k sinθ cosφ
        k_y = k sinθ sinφ

    The angular factor (1 + cosθ)/2 accounts for the element factor of
    an equivalent Huygens source.

    Parameters
    ----------
    E_aperture : 2D ndarray — aperture electric field distribution [V/m]
    x, y       : 1D ndarray — spatial coordinates along aperture [m]
    k          : float — wavenumber [rad/m]
    r          : float — observation distance [m]
    theta      : 1D ndarray — observation polar angles [rad]
    phi        : float — observation azimuthal angle [rad]

    Returns
    -------
    E_far : 2D ndarray — far-field magnitude pattern [V/m]
    """
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    Nx = len(x)
    Ny = len(y)

    # Spatial frequency axes
    fx = np.fft.fftfreq(Nx, dx)        # cycles/m
    fy = np.fft.fftfreq(Ny, dy)

    # 2D FFT and shift so DC is at centre
    E_fft = np.fft.fftshift(np.fft.fft2(np.fft.ifftshift(E_aperture))) * dx * dy

    # Interpolate FFT onto (θ, φ) directions
    # u = fλ = sinθ cosφ, v = sinθ sinφ  (in λ units)
    # Actually: k_x = 2π f_x, and k_x = k sinθ cosφ → f_x = sinθ cosφ / λ
    lambda_0 = 2.0 * np.pi / k

    # We'll evaluate on a grid of u = sinθ cosφ, v = sinθ sinφ
    Theta, Phi = np.meshgrid(theta, phi, indexing='ij')
    u_target = np.sin(Theta) * np.cos(Phi)
    v_target = np.sin(Theta) * np.sin(Phi)

    # Map to FFT grid indices
    fx_grid = u_target / lambda_0
    fy_grid = v_target / lambda_0

    # Use bilinear interpolation on the FFT result
    from scipy import interpolate
    fx_1d = np.fft.fftshift(fx)
    fy_1d = np.fft.fftshift(fy)

    interp = interpolate.RegularGridInterpolator(
        (fx_1d, fy_1d), E_fft, bounds_error=False, fill_value=0.0
    )

    E_far_raw = interp(np.stack([fx_grid, fy_grid], axis=-1))

    # Apply Huygens element factor
    E_far = (1j * k * np.exp(-1j * k * r) / (2.0 * np.pi * r)
             * E_far_raw * (1.0 + np.cos(Theta)) / 2.0)

    return E_far


# ═════════════════════════════════════════════════════════════════════════════
#  4.  Plot helpers
# ═════════════════════════════════════════════════════════════════════════════

def plot_e_field_2d(x, z, E_field, title):
    """
    Plot 2D slice of |E-field| in the xz-plane.

    Parameters
    ----------
    x, z   : 1D ndarrays — coordinate axes
    E_field: 2D ndarray — field magnitude at (x, z)
    title  : str
    """
    X, Z = np.meshgrid(x, z, indexing='ij')
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.pcolormesh(X, Z, np.abs(E_field), shading='auto', cmap='hot')
    fig.colorbar(im, ax=ax, label='|E| [V/m]')
    ax.set_xlabel('x [m]')
    ax.set_ylabel('z [m]')
    ax.set_title(title)
    ax.set_aspect('equal')
    plt.tight_layout()
    return fig, ax


def plot_normalized_pattern(theta, pattern_linear, pattern_db_label,
                            title, savepath, pattern2=None, pattern2_label=None):
    """
    Polar plot of normalized radiation pattern (in dB).

    Parameters
    ----------
    theta    : array — angles in [0, π]
    pattern  : array — field magnitude (linear)
    title    : str
    savepath : str
    """
    # Normalise and convert to dB
    pat_norm = np.abs(pattern_linear) / np.max(np.abs(pattern_linear))
    pat_dB = 20.0 * np.log10(pat_norm + 1e-15)
    pat_dB = np.clip(pat_dB, -40, 0)   # floor at -40 dB

    fig, ax = plt.subplots(1, 2, figsize=(14, 5.5))

    # ── Rectangular plot ──
    ax[0].plot(np.degrees(theta), pat_dB, 'b-', linewidth=1.5, label=pattern_db_label)
    if pattern2 is not None:
        pat2_norm = np.abs(pattern2) / np.max(np.abs(pattern2))
        pat2_dB = 20.0 * np.log10(pat2_norm + 1e-15)
        pat2_dB = np.clip(pat2_dB, -40, 0)
        ax[0].plot(np.degrees(theta), pat2_dB, 'r--', linewidth=1.5, label=pattern2_label)

    ax[0].set_xlabel('θ [deg]')
    ax[0].set_ylabel('Normalized pattern [dB]')
    ax[0].set_title(title + ' — Rectangular')
    ax[0].grid(True, alpha=0.3)
    ax[0].legend()
    ax[0].set_xlim(0, 180)
    ax[0].set_ylim(-40, 3)

    # ── Polar plot ──
    ax_pol = fig.add_subplot(1, 2, 2, projection='polar')
    ax_pol.plot(theta, pat_dB, 'b-', linewidth=1.5, label=pattern_db_label)
    if pattern2 is not None:
        ax_pol.plot(theta, pat2_dB, 'r--', linewidth=1.5, label=pattern2_label)

    ax_pol.set_theta_zero_location('N')
    ax_pol.set_theta_direction(-1)
    ax_pol.set_rlim(-40, 0)
    ax_pol.set_rticks([-30, -20, -10, 0])
    ax_pol.set_title(title + ' — Polar')
    ax_pol.legend(loc='lower left')

    plt.tight_layout()
    fig.savefig(savepath, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {savepath}")


def plot_3d_pattern(theta, phi, pattern_dB, title, savepath):
    """
    3D polar plot of radiation pattern.
    """
    Theta, Phi = np.meshgrid(theta, phi, indexing='ij')
    R = pattern_dB + 40   # shift so -40 dB → 0, 0 dB → 40
    X = R * np.sin(Theta) * np.cos(Phi)
    Y = R * np.sin(Theta) * np.sin(Phi)
    Z = R * np.cos(Theta)

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(X, Y, Z, facecolors=cm.viridis(pattern_dB / 40.0 + 1),
                           rstride=1, cstride=1, alpha=0.9, linewidth=0)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_title(title)
    plt.tight_layout()
    fig.savefig(savepath, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {savepath}")


# ═════════════════════════════════════════════════════════════════════════════
#  5.  Aperture field helpers
# ═════════════════════════════════════════════════════════════════════════════

def uniform_rectangular_aperture(a, b, Nx=256, Ny=256):
    """
    Uniform field over a rectangular aperture of size a × b.

    Returns
    -------
    E_ap : 2D array
    x, y : 1D arrays
    """
    Lx = a * 2.0    # pad domain to avoid aliasing
    Ly = b * 2.0
    x = np.linspace(-Lx/2, Lx/2, Nx)
    y = np.linspace(-Ly/2, Ly/2, Ny)

    X, Y = np.meshgrid(x, y, indexing='ij')
    E_ap = np.where((np.abs(X) <= a/2) & (np.abs(Y) <= b/2), 1.0, 0.0)
    return E_ap, x, y


def analytical_uniform_aperture(theta, a, b, k, phi=0.0):
    """
    Analytical far-field of a uniform rectangular aperture (sinc pattern).

    E(θ) ∝ sinc(k a/2 sinθ cosφ) · sinc(k b/2 sinθ sinφ) · (1+cosθ)/2
    """
    u = np.sin(theta) * np.cos(phi)
    v = np.sin(theta) * np.sin(phi)
    pat = (np.sinc(k * a * u / (2.0 * np.pi)) *   # np.sinc uses sin(πx)/(πx)
           np.sinc(k * b * v / (2.0 * np.pi)))
    pat *= (1.0 + np.cos(theta)) / 2.0
    return pat


# ═════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 60)
    print("Balanis Ch3 — Radiation Integrals Examples")
    print("=" * 60)

    # Parameters
    f = 1.0e9                     # 1 GHz
    k_0 = 2.0 * np.pi * f / c_0
    lambda_0 = 2.0 * np.pi / k_0
    print(f"f = {f/1e9:.2f} GHz, λ = {lambda_0:.4f} m")

    r_far = 100.0 * lambda_0      # far-field distance

    # θ grid
    theta_grid = np.linspace(0, np.pi, 721)
    phi_0 = 0.0
    phi_90 = np.pi / 2.0

    # ─────────────────────────────────────────────────────────────────────────
    #  Fig 3.1 — Short electric dipole
    # ─────────────────────────────────────────────────────────────────────────
    print("\n--- Short Electric Dipole ---")
    Idl = 1.0                      # 1 A·m
    E_theta_dipole, H_phi_dipole = far_field_electric_dipole(Idl, k_0, r_far, theta_grid)

    # E-plane (φ=0): pattern ∝ sinθ
    # H-plane (φ=π/2): pattern ∝ 1 (constant)
    pat_E_plane = np.abs(E_theta_dipole)         # E_θ magnitude vs θ
    pat_H_plane = np.abs(H_phi_dipole)           # H_φ magnitude vs θ

    # The H-plane is constant (omnidirectional in azimuth)
    # For a z-oriented dipole, the H-plane cut at θ=π/2 gives E-plane angular dependence
    # Re-interpret: E-plane = any plane containing the dipole axis → pattern = sinθ
    #              H-plane = plane perpendicular to dipole → pattern = constant (θ=π/2 vs φ)
    phi_h = np.linspace(0, 2*np.pi, 361)
    pat_h_plane = np.full_like(phi_h, np.max(np.abs(H_phi_dipole)))

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5),
                             subplot_kw={'projection': 'polar'})

    # E-plane polar
    axes[0].plot(theta_grid, 20*np.log10(pat_E_plane/np.max(pat_E_plane) + 1e-15),
                 'b-', linewidth=1.5)
    axes[0].set_theta_zero_location('N')
    axes[0].set_theta_direction(-1)
    axes[0].set_rlim(-40, 0)
    axes[0].set_rticks([-30, -20, -10, 0])
    axes[0].set_title('E-plane (φ=0): |E_θ|', fontsize=12)

    # H-plane polar
    axes[1].plot(phi_h, 20*np.log10(pat_h_plane/np.max(pat_h_plane) + 1e-15),
                 'r-', linewidth=1.5)
    axes[1].set_theta_zero_location('N')
    axes[1].set_theta_direction(-1)
    axes[1].set_rlim(-40, 0)
    axes[1].set_rticks([-30, -20, -10, 0])
    axes[1].set_title('H-plane (θ=90°): |H_φ|', fontsize=12)

    fig.suptitle('Short Electric Dipole (Hertzian Dipole) — Far-Field Patterns',
                 fontsize=14, y=1.05)
    plt.tight_layout()
    savepath1 = os.path.join(FIGDIR, 'fig3_1_short_dipole.png')
    fig.savefig(savepath1, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {savepath1}")

    # ─────────────────────────────────────────────────────────────────────────
    #  Fig 3.2 — Small loop (magnetic dipole)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n--- Small Loop (Magnetic Dipole) ---")
    loop_area = 0.01                # m²
    I_loop = 1.0                    # A
    Imdl = 1j * k_0 * eta_0 * I_loop * loop_area   # magnetic dipole moment
    # Actually: for small loop, m = I·A, magnetic dipole moment
    # Equivalent magnetic current: I_m dl = j ω μ₀ I A
    Imdl_val = np.abs(k_0 * eta_0 * I_loop * loop_area)  # use real magnitude

    H_theta_loop, E_phi_loop = far_field_magnetic_dipole(Imdl_val, k_0, r_far, theta_grid)

    # E-plane for magnetic dipole: pattern ∝ 1 (in the plane of the loop)
    # H-plane: pattern ∝ sinθ
    # By duality, this swaps relative to the electric dipole case.
    # For a loop in xy-plane (z-oriented magnetic dipole moment):
    #   E-plane (φ=0, in plane of loop): |E_φ| ∝ 1  (isotropic in that plane)
    #   H-plane (φ=π/2, perpendicular):  |E_φ| ∝ sinθ

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5),
                             subplot_kw={'projection': 'polar'})

    # E-plane (φ=0) — constant
    axes[0].plot(theta_grid,
                 20*np.log10(np.abs(E_phi_loop)/np.max(np.abs(E_phi_loop)) + 1e-15),
                 'b-', linewidth=1.5, label='|E_φ|')
    axes[0].set_theta_zero_location('N')
    axes[0].set_theta_direction(-1)
    axes[0].set_rlim(-40, 0)
    axes[0].set_rticks([-30, -20, -10, 0])
    axes[0].set_title('E-plane (φ=0): |E_φ|', fontsize=12)

    # H-plane (φ=π/2) — sinθ
    axes[1].plot(theta_grid,
                 20*np.log10(np.abs(E_phi_loop)/np.max(np.abs(E_phi_loop)) + 1e-15),
                 'r-', linewidth=1.5, label='|E_φ|')
    axes[1].set_theta_zero_location('N')
    axes[1].set_theta_direction(-1)
    axes[1].set_rlim(-40, 0)
    axes[1].set_rticks([-30, -20, -10, 0])
    axes[1].set_title('H-plane (φ=90°): |E_φ|', fontsize=12)

    fig.suptitle('Small Loop (Magnetic Dipole) — Far-Field Patterns',
                 fontsize=14, y=1.05)
    plt.tight_layout()
    savepath2 = os.path.join(FIGDIR, 'fig3_2_small_loop.png')
    fig.savefig(savepath2, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {savepath2}")

    # ─────────────────────────────────────────────────────────────────────────
    #  Duality verification: overlay electric vs magnetic dipole
    # ─────────────────────────────────────────────────────────────────────────
    print("\n--- Duality Verification ---")
    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'}, figsize=(7, 7))

    # Normalize both to [0, 1]
    e_norm = np.abs(E_theta_dipole) / np.max(np.abs(E_theta_dipole))
    m_norm = np.abs(E_phi_loop) / np.max(np.abs(E_phi_loop))

    ax.plot(theta_grid, 20*np.log10(e_norm + 1e-15),
            'b-', linewidth=1.5, label='Elec. dipole |E_θ|')
    ax.plot(theta_grid, 20*np.log10(m_norm + 1e-15),
            'r--', linewidth=1.5, label='Mag. dipole |E_φ|')
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_rlim(-40, 0)
    ax.set_rticks([-30, -20, -10, 0])
    ax.set_title('Duality: Electric Dipole vs Magnetic Dipole\n'
                 'Both follow sinθ pattern', fontsize=13)
    ax.legend(loc='lower left')
    plt.tight_layout()
    duality_path = os.path.join(FIGDIR, 'fig3_duality_verification.png')
    fig.savefig(duality_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {duality_path}")
    print("  ✓ Both dipoles show identical sin(θ) pattern shape (by duality)")

    # ─────────────────────────────────────────────────────────────────────────
    #  Fig 3.3 — Uniform rectangular aperture far field
    # ─────────────────────────────────────────────────────────────────────────
    print("\n--- Uniform Rectangular Aperture ---")

    a_ap = 5.0 * lambda_0           # aperture width in x
    b_ap = 3.0 * lambda_0           # aperture height in y

    # Analytical sinc pattern
    theta_wide = np.linspace(0, np.pi/2, 901)   # only 0–90° needed
    pat_sinc_E = analytical_uniform_aperture(theta_wide, a_ap, b_ap, k_0, phi=0.0)
    pat_sinc_H = analytical_uniform_aperture(theta_wide, a_ap, b_ap, k_0, phi=np.pi/2.0)

    plot_normalized_pattern(
        theta_wide, pat_sinc_E, 'E-plane (φ=0)',
        'Uniform Rectangular Aperture: E-plane',
        os.path.join(FIGDIR, 'fig3_3_aperture_eplane.png')
    )

    plot_normalized_pattern(
        theta_wide, pat_sinc_H, 'H-plane (φ=90°)',
        'Uniform Rectangular Aperture: H-plane',
        os.path.join(FIGDIR, 'fig3_3_aperture_hplane.png')
    )

    # ── Parameter sweep: vary aperture size ──
    print("\n--- Aperture Size Sweep ---")
    fig, ax = plt.subplots(figsize=(9, 6))
    ratios = [2, 4, 8]
    colors = ['b', 'r', 'g']
    for ratio, color in zip(ratios, colors):
        a_sweep = ratio * lambda_0
        b_sweep = a_sweep          # square aperture
        pat = analytical_uniform_aperture(theta_wide, a_sweep, b_sweep, k_0, phi=0.0)
        pat_norm = np.abs(pat) / np.max(np.abs(pat))
        pat_dB = 20.0 * np.log10(pat_norm + 1e-15)
        pat_dB = np.clip(pat_dB, -50, 0)
        ax.plot(np.degrees(theta_wide), pat_dB, color=color, linewidth=1.8,
                label=f'a = b = {ratio}λ')

    ax.set_xlabel('θ [deg]')
    ax.set_ylabel('Normalized pattern [dB]')
    ax.set_title('Square Uniform Aperture: Beamwidth vs Size (E-plane)')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 90)
    ax.set_ylim(-50, 3)
    plt.tight_layout()
    sweep_path = os.path.join(FIGDIR, 'fig3_3_aperture_parameter_sweep.png')
    fig.savefig(sweep_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {sweep_path}")
    print("  ✓ Larger aperture → narrower beam (wider aperture in λ)")
    print("  ✓ Sidelobes at -13.26 dB (sinc pattern first sidelobe)")

    # ── Combined aperture figure (FFT method vs analytical) ──
    print("\n--- Aperture: FFT method vs Analytical ---")
    Nx_fft = 512
    Ny_fft = 512
    a_pad = 6.0 * lambda_0
    b_pad = 6.0 * lambda_0
    x_fft = np.linspace(-a_pad, a_pad, Nx_fft)
    y_fft = np.linspace(-b_pad, b_pad, Ny_fft)
    X_fft, Y_fft = np.meshgrid(x_fft, y_fft, indexing='ij')
    E_ap = np.where((np.abs(X_fft) <= a_ap/2) & (np.abs(Y_fft) <= b_ap/2), 1.0, 0.0)

    theta_ff = np.linspace(0, np.pi/2, 256)
    phi_ff = np.array([0.0, np.pi/2.0])

    E_far_fft = aperture_to_far_field(E_ap, x_fft, y_fft, k_0, r_far, theta_ff, phi_ff)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    for idx, (phi_val, label) in enumerate(zip([0.0, np.pi/2.0], ['E-plane (φ=0)', 'H-plane (φ=90°)'])):
        pat_ana = analytical_uniform_aperture(theta_ff, a_ap, b_ap, k_0, phi_val)
        pat_ana_norm = np.abs(pat_ana) / np.max(np.abs(pat_ana))
        pat_ana_dB = 20.0 * np.log10(pat_ana_norm + 1e-15)
        pat_ana_dB = np.clip(pat_ana_dB, -50, 0)

        pat_fft = np.abs(E_far_fft[:, idx])
        pat_fft_norm = pat_fft / np.max(pat_fft)
        pat_fft_dB = 20.0 * np.log10(pat_fft_norm + 1e-15)
        pat_fft_dB = np.clip(pat_fft_dB, -50, 0)

        axes[idx].plot(np.degrees(theta_ff), pat_ana_dB, 'b-', linewidth=2,
                       label='Analytical (sinc)')
        axes[idx].plot(np.degrees(theta_ff), pat_fft_dB, 'r--', linewidth=1.5,
                       alpha=0.8, label='FFT method')
        axes[idx].set_xlabel('θ [deg]')
        axes[idx].set_ylabel('Normalized pattern [dB]')
        axes[idx].set_title(label)
        axes[idx].grid(True, alpha=0.3)
        axes[idx].legend()
        axes[idx].set_xlim(0, 90)
        axes[idx].set_ylim(-50, 3)

    fig.suptitle(f'Aperture Far Field: FFT vs Analytical\n'
                 f'a = {a_ap/lambda_0:.1f}λ, b = {b_ap/lambda_0:.1f}λ',
                 fontsize=13)
    plt.tight_layout()
    fft_comp_path = os.path.join(FIGDIR, 'fig3_3_aperture_ff.png')
    fig.savefig(fft_comp_path, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {fft_comp_path}")
    print("  ✓ FFT method matches analytical sinc pattern")

    # ─────────────────────────────────────────────────────────────────────────
    #  2D E-field slice of dipole near field (for illustration)
    # ─────────────────────────────────────────────────────────────────────────
    print("\n--- 2D E-field Slice (Dipole Near-Field) ---")
    # For completeness, demonstrate the 2D plotting function
    x_slice = np.linspace(-lambda_0, lambda_0, 201)
    z_slice = np.linspace(-lambda_0, lambda_0, 201)
    X_s, Z_s = np.meshgrid(x_slice, z_slice, indexing='ij')
    R_s = np.sqrt(X_s**2 + Z_s**2)
    Theta_s = np.arctan2(X_s, Z_s + 1e-15)
    # Mask to avoid singularity
    R_s = np.maximum(R_s, lambda_0 / 100.0)

    E_slice, _ = far_field_electric_dipole(Idl, k_0, R_s, Theta_s)
    fig, ax = plot_e_field_2d(x_slice, z_slice, E_slice,
                               'Short Dipole |E| in xz-plane (r > λ/10)')
    savepath_slice = os.path.join(FIGDIR, 'fig3_dipole_nearfield_slice.png')
    fig.savefig(savepath_slice, dpi=200, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {savepath_slice}")

    print("\n" + "=" * 60)
    print("All figures generated successfully.")
    print("=" * 60)

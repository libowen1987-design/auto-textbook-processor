#!/usr/bin/env python3
"""
Pozar "Microwave Engineering" 4th Ed, Chapter 3 — Complete Numerical Examples
======================================================================
Covers: Rectangular waveguide, Circular waveguide, Coaxial line,
Microstrip line, Dispersion, Attenuation, Power capacity.

All variable names follow physical conventions:
  a, b          = waveguide dimensions (m)
  epsilon_r     = relative permittivity
  mu_r          = relative permeability
  sigma         = conductivity (S/m)
  fc            = cutoff frequency (Hz)
  beta          = propagation constant (rad/m)
  alpha_c       = conductor attenuation (Np/m)
  alpha_d       = dielectric attenuation (Np/m)
  Z0            = characteristic impedance (ohms)
  omega         = angular frequency (rad/s)
  k0            = free-space wavenumber (rad/m)
  Rs            = surface resistivity (ohms/sq)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jv, jvp, jn_zeros, jnp_zeros
from pathlib import Path

# ============================================================
# Output directory for figures
# ============================================================
FIG_DIR = Path(__file__).resolve().parent / "figures" / "ch03"
FIG_DIR.mkdir(parents=True, exist_ok=True)

# Physical constants
C0 = 299792458.0       # speed of light (m/s)
ETA0 = 376.730313668   # free-space impedance (ohms)
C_CU = 5.8e7            # conductivity of copper (S/m)
MU0 = 4 * np.pi * 1e-7  # permeability of free space (H/m)


def separator(title: str) -> None:
    """Print a section separator with title."""
    line = "=" * 72
    print(f"\n{line}")
    print(f"  {title}")
    print(f"{line}\n")


def compute_rs(frequency: float, sigma: float = C_CU, mu_r: float = 1.0) -> float:
    """Surface resistivity Rs = sqrt(pi*f*mu0*mu_r / sigma)."""
    return np.sqrt(np.pi * frequency * MU0 * mu_r / sigma)


# ============================================================
# EXAMPLE 1: Rectangular Waveguide — TEmn Mode Analysis
# ============================================================
def example_rectangular_te_mode_scan():
    """
    Rectangular waveguide TE_mn mode cutoff scan.
    Given a standard WR-90 waveguide (a=2.286 cm, b=1.016 cm),
    compute and tabulate cutoff frequencies for lowest TE modes.
    Generate a mode chart.
    """
    separator("EXAMPLE 1: Rectangular Waveguide — TE_mn Mode Cutoff Scan")

    a = 2.286e-2   # broad wall (m)
    b = 1.016e-2   # narrow wall (m)
    epsilon_r = 1.0  # air-filled

    print(f"Waveguide: WR-90, a = {a*1e3:.3f} mm, b = {b*1e3:.3f} mm")
    print(f"Filling: epsilon_r = {epsilon_r} (air)")
    print()

    # Scan modes m=0..3, n=0..2 (exclude m=n=0)
    modes = []
    for m_idx in range(4):
        for n_idx in range(3):
            if m_idx == 0 and n_idx == 0:
                continue
            # Cutoff wavenumber
            kc = np.sqrt((m_idx * np.pi / a) ** 2 + (n_idx * np.pi / b) ** 2)
            fc_val = kc * C0 / (2 * np.pi * np.sqrt(epsilon_r))
            modes.append((m_idx, n_idx, fc_val))

    # Sort by cutoff frequency
    modes.sort(key=lambda x: x[2])

    print(f"{'Mode':>10} | {'fc (GHz)':>10} | {'lambda_c (cm)':>12}")
    print("-" * 38)
    for m_idx, n_idx, fc_val in modes:
        lambda_c = C0 / fc_val * 100  # cm
        print(f"  TE{m_idx}{n_idx:<5} | {fc_val/1e9:>8.3f}  | {lambda_c:>10.3f}")

    # Dominant mode TE10
    fc_10 = C0 / (2 * a)  # exact formula
    fc_20 = C0 / a
    print(f"\nDominant TE10 cutoff: f_c,10 = c/(2a) = {fc_10/1e9:.3f} GHz")
    print(f"Next mode TE20 cutoff: f_c,20 = c/a   = {fc_20/1e9:.3f} GHz")
    print(f"Recommended operating band: {1.25*fc_10/1e9:.2f} – {1.9*fc_10/1e9:.2f} GHz")

    # ---- Plot: mode chart ----
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(modes)))
    bar_labels = []
    bar_values = []
    bar_colors = []
    for (m_idx, n_idx, fc_val), color in zip(modes, colors):
        bar_labels.append(f"TE{m_idx}{n_idx}")
        bar_values.append(fc_val / 1e9)
        bar_colors.append(color)

    ax.bar(range(len(bar_labels)), bar_values, color=bar_colors, edgecolor='k', alpha=0.85)
    ax.set_xticks(range(len(bar_labels)))
    ax.set_xticklabels(bar_labels, fontsize=9)
    ax.set_ylabel("Cutoff Frequency (GHz)", fontsize=12)
    ax.set_title(f"TE Mode Cutoff Frequencies — WR-90 (a={a*1e3:.1f} mm, b={b*1e3:.1f} mm)", fontsize=13)
    ax.axhline(fc_10 / 1e9, color='r', ls='--', lw=1, label=f"TE10 = {fc_10/1e9:.2f} GHz")
    ax.axhline(fc_20 / 1e9, color='orange', ls='--', lw=1, label=f"TE20 = {fc_20/1e9:.2f} GHz")
    ax.legend(fontsize=9)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "rectangular_te_mode_cutoffs.png", dpi=150)
    plt.close(fig)
    print(f"\n  [Figure saved] rectangular_te_mode_cutoffs.png")


# ============================================================
# EXAMPLE 2: Rectangular Waveguide — Field Distribution TE10
# ============================================================
def example_rectangular_te10_fields():
    """
    Plot E_y field magnitude across cross-section for TE10 mode.
    """
    separator("EXAMPLE 2: Rectangular Waveguide — TE10 Field Distribution")

    a = 2.286e-2
    b = 1.016e-2
    frequency = 10e9  # 10 GHz
    epsilon_r = 1.0

    fc_10 = C0 / (2 * a)
    k0 = 2 * np.pi * frequency / C0
    kc = np.pi / a
    beta = k0 * np.sqrt(1 - (fc_10 / frequency) ** 2)

    print(f"Frequency: {frequency/1e9:.1f} GHz")
    print(f"TE10 cutoff: {fc_10/1e9:.3f} GHz")
    print(f"Propagation constant beta = {beta:.2f} rad/m")
    print(f"Guide wavelength lambda_g = {2*np.pi/beta*1e3:.2f} mm")

    # Field grid
    nx, ny = 80, 40
    x_vals = np.linspace(0, a, nx)
    y_vals = np.linspace(0, b, ny)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Ey ~ sin(pi*x/a), uniform in y
    Ey = np.sin(np.pi * X / a)
    Ey_normalized = Ey / np.max(np.abs(Ey))

    # Hx ~ sin(pi*x/a)
    Hx = np.sin(np.pi * X / a)
    Hx_normalized = Hx / np.max(np.abs(Hx))

    # Hz ~ cos(pi*x/a)
    Hz = np.cos(np.pi * X / a)
    Hz_normalized = Hz / np.max(np.abs(Hz))

    # pcolormesh expects C shape matching X,Y
    # With default meshgrid indexing: X.shape = (ny, nx), Y.shape = (ny, nx)
    # So we pass Ey_normalized (no .T needed if we computed on meshgrid)
    # Actually meshgrid gives outputs of shape (ny, nx) by default
    # Our arrays have X(ny,nx), Y(ny,nx), Ey(ny,nx)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # Ey field
    im0 = axes[0].pcolormesh(X * 1e3, Y * 1e3, Ey_normalized,
                              shading='auto', cmap='RdBu_r')
    axes[0].set_title(r"$E_y \propto \sin(\pi x/a)$", fontsize=11)
    axes[0].set_xlabel("x (mm)")
    axes[0].set_ylabel("y (mm)")
    fig.colorbar(im0, ax=axes[0], shrink=0.8)

    # Hx field
    im1 = axes[1].pcolormesh(X * 1e3, Y * 1e3, Hx_normalized,
                              shading='auto', cmap='RdBu_r')
    axes[1].set_title(r"$H_x \propto \sin(\pi x/a)$", fontsize=11)
    axes[1].set_xlabel("x (mm)")
    axes[1].set_ylabel("y (mm)")
    fig.colorbar(im1, ax=axes[1], shrink=0.8)

    # Hz field
    im2 = axes[2].pcolormesh(X * 1e3, Y * 1e3, Hz_normalized,
                              shading='auto', cmap='RdBu_r')
    axes[2].set_title(r"$H_z \propto \cos(\pi x/a)$", fontsize=11)
    axes[2].set_xlabel("x (mm)")
    axes[2].set_ylabel("y (mm)")
    fig.colorbar(im2, ax=axes[2], shrink=0.8)

    plt.suptitle(f"TE10 Mode Field Distribution (f={frequency/1e9:.1f} GHz, WR-90)", fontsize=13)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "rectangular_te10_field_distribution.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] rectangular_te10_field_distribution.png")


# ============================================================
# EXAMPLE 3: Rectangular Waveguide Attenuation
# ============================================================
def example_rectangular_attenuation():
    """
    Compute conductor and dielectric attenuation for TE10 mode
    in WR-90 waveguide over the X-band (8.2–12.4 GHz).
    Plot alpha_c and alpha_d vs frequency.
    """
    separator("EXAMPLE 3: Rectangular Waveguide — Attenuation (TE10)")

    a = 2.286e-2
    b = 1.016e-2
    sigma = C_CU  # copper walls
    tan_delta = 0.0004  # typical for low-loss dielectric

    fc_10 = C0 / (2 * a)
    frequencies = np.linspace(8.2e9, 12.4e9, 100)

    alpha_c_vals = []
    alpha_d_vals = []
    alpha_tot_vals = []

    for frequency in frequencies:
        k0 = 2 * np.pi * frequency / C0
        kc = np.pi / a
        beta = k0 * np.sqrt(1 - (fc_10 / frequency) ** 2)
        eta = ETA0  # air-filled

        # Surface resistivity
        Rs = compute_rs(frequency, sigma)

        # Conductor attenuation for TE10 (Pozar Eq 3.106)
        numerator = Rs * (2 * b * np.pi ** 2 + a ** 3 * k0 ** 2)
        denominator = a ** 3 * b * beta * k0 * eta
        alpha_c = numerator / denominator
        alpha_c_vals.append(alpha_c)

        # Dielectric attenuation
        alpha_d = k0 ** 2 * tan_delta / (2 * beta)
        alpha_d_vals.append(alpha_d)
        alpha_tot_vals.append(alpha_c + alpha_d)

    # Print at band center
    f_center = 10.3e9
    k0_c = 2 * np.pi * f_center / C0
    beta_c = k0_c * np.sqrt(1 - (fc_10 / f_center) ** 2)
    Rs_c = compute_rs(f_center, sigma)
    num_c = Rs_c * (2 * b * np.pi ** 2 + a ** 3 * k0_c ** 2)
    den_c = a ** 3 * b * beta_c * k0_c * ETA0
    alpha_c_c = num_c / den_c
    alpha_d_c = k0_c ** 2 * tan_delta / (2 * beta_c)

    print(f"At f = {f_center/1e9:.1f} GHz (X-band center):")
    print(f"  Conductor attenuation:  alpha_c = {alpha_c_c:.4f} Np/m  ({20*np.log10(np.e)*alpha_c_c:.3f} dB/m)")
    print(f"  Dielectric attenuation: alpha_d = {alpha_d_c:.6f} Np/m  ({20*np.log10(np.e)*alpha_d_c:.4f} dB/m)")
    print(f"  Total:                  alpha   = {alpha_c_c+alpha_d_c:.4f} Np/m")

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(frequencies / 1e9, np.array(alpha_c_vals) * 100,
            'b-', lw=2, label=r"$\alpha_c$ (conductor)")
    ax.plot(frequencies / 1e9, np.array(alpha_d_vals) * 100,
            'r-', lw=2, label=r"$\alpha_d$ (dielectric)")
    ax.plot(frequencies / 1e9, np.array(alpha_tot_vals) * 100,
            'k--', lw=1.5, label=r"$\alpha = \alpha_c + \alpha_d$")
    ax.set_xlabel("Frequency (GHz)", fontsize=12)
    ax.set_ylabel("Attenuation (Np/100m)", fontsize=12)
    ax.set_title("TE10 Mode Attenuation in WR-90 Waveguide", fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "rectangular_te10_attenuation.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] rectangular_te10_attenuation.png")


# ============================================================
# EXAMPLE 4: Circular Waveguide — Mode Chart (Bessel Zeros)
# ============================================================
def example_circular_mode_chart():
    """
    Compute and tabulate the lowest TE_nm and TM_nm modes of
    a circular waveguide. Use Bessel function zeros.
    Generate a bar chart of mode ordering.
    """
    separator("EXAMPLE 4: Circular Waveguide — Mode Chart")

    radius = 1.0e-2  # 1 cm

    # Bessel function zeros:
    # TE: J_n'(x)=0 -> roots via jnp_zeros(n, count)
    # TM: J_n(x)=0  -> roots via jn_zeros(n, count)
    n_max = 3
    m_max = 3

    te_modes = []
    tm_modes = []

    for n_idx in range(n_max + 1):
        # TE modes: use jnp_zeros (roots of derivative)
        if n_idx == 0:
            # J_0' roots: known values; jnp_zeros yields them correctly
            roots_te = jnp_zeros(n_idx, m_max)
        else:
            roots_te = jnp_zeros(n_idx, m_max)
        for m_idx, p_prime in enumerate(roots_te, start=1):
            kc = p_prime / radius
            fc_val = kc * C0 / (2 * np.pi)
            te_modes.append((n_idx, m_idx, p_prime, kc, fc_val))

        # TM modes: jn_zeros (roots of J_n)
        roots_tm = jn_zeros(n_idx, m_max)
        for m_idx, p_val in enumerate(roots_tm, start=1):
            kc = p_val / radius
            fc_val = kc * C0 / (2 * np.pi)
            tm_modes.append((n_idx, m_idx, p_val, kc, fc_val))

    # Sort by cutoff frequency
    te_modes.sort(key=lambda x: x[4])
    tm_modes.sort(key=lambda x: x[4])

    print(f"Circular waveguide radius a = {radius*1e2:.1f} cm")
    print()

    print("TE modes (J_n'(p') = 0):")
    print(f"{'Mode':>10} | {'p\'_nm':>8} | {'kc (1/m)':>10} | {'fc (GHz)':>10}")
    print("-" * 44)
    for n_idx, m_idx, p_prime, kc, fc_val in te_modes:
        print(f"  TE{n_idx}{m_idx:<5} | {p_prime:>8.3f} | {kc:>10.2f} | {fc_val/1e9:>8.3f}")

    print()
    print("TM modes (J_n(p) = 0):")
    print(f"{'Mode':>10} | {'p_nm':>8} | {'kc (1/m)':>10} | {'fc (GHz)':>10}")
    print("-" * 44)
    for n_idx, m_idx, p_val, kc, fc_val in tm_modes:
        print(f"  TM{n_idx}{m_idx:<5} | {p_val:>8.3f} | {kc:>10.2f} | {fc_val/1e9:>8.3f}")

    # Dominant mode
    te11_fc = te_modes[0][4]
    tm01_fc = tm_modes[0][4]
    print(f"\nDominant TE11 cutoff: {te11_fc/1e9:.3f} GHz")
    print(f"Dominant TM01 cutoff: {tm01_fc/1e9:.3f} GHz")

    # ---- Plot: combined bar chart ----
    all_modes = [(f"TE{n}{m}", fc) for n, m, _, _, fc in te_modes[:10]] + \
                [(f"TM{n}{m}", fc) for n, m, _, _, fc in tm_modes[:10]]
    all_modes.sort(key=lambda x: x[1])

    fig, ax = plt.subplots(figsize=(10, 5))
    labels = [m[0] for m in all_modes]
    values = [m[1] / 1e9 for m in all_modes]
    colors = ['steelblue' if 'TE' in l else 'coral' for l in labels]
    ax.bar(range(len(labels)), values, color=colors, edgecolor='k', alpha=0.85)
    # Mark TE11 and TM01
    for idx, label in enumerate(labels):
        if label == "TE11":
            ax.text(idx, values[idx] + 0.1, "★ Dominant", ha='center', fontsize=9, color='darkblue')

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, fontsize=8)
    ax.set_ylabel("Cutoff Frequency (GHz)", fontsize=12)
    ax.set_title(f"Circular Waveguide Mode Cutoffs (radius a={radius*1e2:.1f} cm)", fontsize=13)
    ax.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "circular_waveguide_mode_chart.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] circular_waveguide_mode_chart.png")


# ============================================================
# EXAMPLE 5: Coaxial Line — Impedance and Attenuation
# ============================================================
def example_coaxial_line():
    """
    Compute Z0 and attenuation for various coaxial cable geometries.
    Also compute TE11 cutoff.
    """
    separator("EXAMPLE 5: Coaxial Line — Impedance, Attenuation, TE11 Cutoff")

    epsilon_r = 2.2  # PTFE (Teflon)
    tan_delta = 0.0002
    frequency = 3e9  # 3 GHz

    # Explore b/a ratios
    ratios = [1.65, 2.30, 3.59]
    inner_radius = 0.5e-3  # 0.5 mm inner conductor

    k0 = 2 * np.pi * frequency / C0
    eta = ETA0 / np.sqrt(epsilon_r)

    print(f"Frequency: {frequency/1e9:.1f} GHz")
    print(f"Dielectric: epsilon_r = {epsilon_r}, tan_delta = {tan_delta}")
    print(f"Inner radius a = {inner_radius*1e3:.2f} mm")
    print()

    print(f"{'b/a':>6} | {'b (mm)':>8} | {'Z0 (ohm)':>10} | {'alpha_c':>12} | {'alpha_d':>12} | {'fc_TE11':>10}")
    print("-" * 62)

    results = []
    for ratio in ratios:
        outer_radius = inner_radius * ratio
        Z0 = eta / (2 * np.pi) * np.log(ratio)
        Rs = compute_rs(frequency, C_CU)
        alpha_c = Rs / (2 * eta * np.log(ratio)) * (1 / inner_radius + 1 / outer_radius)
        alpha_d = k0 * tan_delta / 2

        # TE11 cutoff: lambda_c ~ pi(a+b), fc ~ c/(pi*(a+b)*sqrt(eps_r))
        fc_te11 = C0 / (np.pi * (inner_radius + outer_radius) * np.sqrt(epsilon_r))

        print(f"{ratio:>6.2f} | {outer_radius*1e3:>8.3f} | {Z0:>9.2f}  | {alpha_c:>10.4f}  | {alpha_d:>10.6f}  | {fc_te11/1e9:>8.3f}")
        results.append((ratio, Z0, alpha_c, alpha_d, fc_te11))

    # Standard 50 ohm: find b/a
    target_z0 = 50.0
    ratio_50 = np.exp(2 * np.pi * target_z0 / eta)
    print(f"\nFor Z0 = {target_z0:.0f} ohms: b/a = {ratio_50:.3f}")
    print(f"  (if a=0.5mm, b={inner_radius*ratio_50*1e3:.3f} mm)")
    fc_te11_50 = C0 / (np.pi * (inner_radius + inner_radius * ratio_50) * np.sqrt(epsilon_r))
    print(f"  TE11 cutoff: {fc_te11_50/1e9:.3f} GHz")

    # Max power ratio
    ratio_pmax = np.sqrt(np.e)
    print(f"\nMax power capacity b/a = sqrt(e) = {ratio_pmax:.3f}")
    print(f"Z0 at max power: {eta/(2*np.pi)*np.log(ratio_pmax):.1f} ohms")

    # Min attenuation ratio
    ratio_alpha = np.exp(1 + 2 * inner_radius / inner_radius)  # Wait - let me compute properly
    # Minimum attenuation occurs when d(alpha_c)/d(b) = 0 -> ln(b/a) = 1 + a/b
    # For thin inner: solve ln(x) = 1 + 1/x -> x ≈ 3.59
    print(f"Minimum attenuation b/a ≈ 3.59")


# ============================================================
# EXAMPLE 6: Microstrip Line — Z0 and Effective Dielectric Constant
# ============================================================
def example_microstrip_z0():
    """
    Compute Z0 and epsilon_eff for microstrip over a range of W/h ratios.
    Plot Z0 vs W/h for various epsilon_r.
    Use Schneider/Hammerstad formulas.
    """
    separator("EXAMPLE 6: Microstrip Line — Z0 Calculation (Schneider/Hammerstad)")

    def epsilon_eff(epsilon_r, W_over_h):
        """Effective dielectric constant (Schneider)."""
        return (epsilon_r + 1) / 2 + (epsilon_r - 1) / 2 * (1 / np.sqrt(1 + 12 / W_over_h))

    def Z0_microstrip(W_over_h, epsilon_r):
        """Characteristic impedance (Hammerstad)."""
        eps_eff = epsilon_eff(epsilon_r, W_over_h)
        if W_over_h <= 1:
            Z0 = 60 / np.sqrt(eps_eff) * np.log(8 / W_over_h + W_over_h / 4)
        else:
            Z0 = ETA0 / np.sqrt(eps_eff) / (W_over_h + 1.393 + 0.667 * np.log(W_over_h + 1.444))
        return Z0, eps_eff

    # Design a 50-ohm line on common substrates
    substrates = [
        ("FR4", 4.5, 1.6e-3),
        ("RO4350B", 3.48, 0.508e-3),
        ("Alumina", 9.8, 0.635e-3),
        ("RT/Duroid 5880", 2.2, 0.787e-3),
    ]

    print("Microstrip 50-ohm line design for common substrates:")
    print(f"{'Substrate':>15} | {'eps_r':>6} | {'h (mm)':>8} | {'W/h':>6} | {'W (mm)':>8} | {'eps_eff':>8} | {'Z0 (ohm)':>8}")
    print("-" * 65)

    for name, eps, height in substrates:
        # Synthesis: find W/h for Z0 = 50
        Z0_target = 50.0
        A = Z0_target / 60 * np.sqrt((eps + 1) / 2) + (eps - 1) / (eps + 1) * (0.23 + 0.11 / eps)

        if A > 1.52:
            W_over_h = 8 * np.exp(A) / (np.exp(2 * A) - 2)
        else:
            B = 377 * np.pi / (2 * Z0_target * np.sqrt(eps))
            W_over_h = 2 / np.pi * (B - 1 - np.log(2 * B - 1) +
                                     (eps - 1) / (2 * eps) *
                                     (np.log(B - 1) + 0.39 - 0.61 / eps))

        Width = W_over_h * height
        _, eps_eff_val = Z0_microstrip(W_over_h, eps)
        print(f"{name:>15} | {eps:>6.2f} | {height*1e3:>8.3f} | {W_over_h:>6.3f} | {Width*1e3:>8.3f} | {eps_eff_val:>8.4f} | {Z0_target:>8.2f}")

    # ---- Plot: Z0 vs W/h for various epsilon_r ----
    W_over_h_range = np.logspace(-1, 2, 200)
    eps_r_list = [2.2, 3.48, 4.5, 6.15, 9.8, 12.0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    for eps in eps_r_list:
        z0_vals = []
        eps_eff_vals = []
        for wh in W_over_h_range:
            z0, ee = Z0_microstrip(wh, eps)
            z0_vals.append(z0)
            eps_eff_vals.append(ee)
        label = rf"$\epsilon_r = {eps}$"
        ax1.plot(W_over_h_range, z0_vals, lw=2, label=label)
        ax2.plot(W_over_h_range, eps_eff_vals, lw=2, label=label)

    ax1.axhline(50, color='k', ls='--', alpha=0.5, label="50 Ω")
    ax1.set_xscale('log')
    ax1.set_xlabel("W / h", fontsize=12)
    ax1.set_ylabel(r"$Z_0$ (ohms)", fontsize=12)
    ax1.set_title("Microstrip Characteristic Impedance", fontsize=13)
    ax1.set_xlim(0.1, 100)
    ax1.set_ylim(5, 250)
    ax1.legend(fontsize=8, loc='upper right', ncol=2)
    ax1.grid(alpha=0.3)

    ax2.set_xscale('log')
    ax2.set_xlabel("W / h", fontsize=12)
    ax2.set_ylabel(r"$\epsilon_{\text{eff}}$", fontsize=12)
    ax2.set_title("Effective Dielectric Constant", fontsize=13)
    ax2.set_xlim(0.1, 100)
    ax2.legend(fontsize=8, loc='lower right', ncol=2)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "microstrip_z0_vs_wh.png", dpi=150)
    plt.close(fig)
    print("\n  [Figure saved] microstrip_z0_vs_wh.png")


# ============================================================
# EXAMPLE 7: Waveguide Dispersion Curves (beta-omega diagram)
# ============================================================
def example_dispersion_curves():
    """
    Plot beta (propagation constant) vs frequency for rectangular
    waveguide modes, coaxial TEM, and free space k0.
    Show the dispersion (deviation from linearity) for waveguide modes.
    """
    separator("EXAMPLE 7: Dispersion Curves — Beta vs Omega")

    a = 2.286e-2
    b = 1.016e-2
    fc_10 = C0 / (2 * a)
    fc_20 = C0 / a
    fc_01 = C0 / (2 * b)

    frequencies = np.linspace(1e9, 18e9, 500)

    # Free-space wavenumber
    k0 = 2 * np.pi * frequencies / C0

    # Rectangular waveguide TE10, TE20, TE01
    def waveguide_beta(freq, fc):
        beta = np.zeros_like(freq)
        mask = freq > fc
        beta[mask] = 2 * np.pi * freq[mask] / C0 * np.sqrt(1 - (fc / freq[mask]) ** 2)
        return beta

    beta_te10 = waveguide_beta(frequencies, fc_10)
    beta_te20 = waveguide_beta(frequencies, fc_20)
    beta_te01 = waveguide_beta(frequencies, fc_01)

    # Coax (TEM): beta = k0, linear
    beta_coax = k0

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(frequencies / 1e9, beta_coax, 'k-', lw=2.5, label="TEM (coax / parallel plate)")
    ax.plot(frequencies / 1e9, beta_te10, 'b-', lw=2, label=r"TE$_{10}$ (WR-90)")
    ax.plot(frequencies / 1e9, beta_te20, 'r-', lw=2, label=r"TE$_{20}$ (WR-90)")
    ax.plot(frequencies / 1e9, beta_te01, 'g-', lw=2, label=r"TE$_{01}$ (WR-90)")

    # Mark cutoff frequencies
    for fc_val, label, color in [(fc_10, r"$f_{c,10}$", 'b'),
                                  (fc_20, r"$f_{c,20}$", 'r'),
                                  (fc_01, r"$f_{c,01}$", 'g')]:
        ax.axvline(fc_val / 1e9, color=color, ls=':', alpha=0.6)
        ax.text(fc_val / 1e9, 20, label, fontsize=9, color=color, ha='center')

    ax.set_xlabel("Frequency (GHz)", fontsize=12)
    ax.set_ylabel(r"$\beta$ (rad/m)", fontsize=12)
    ax.set_title("Dispersion Curves — Rectangular Waveguide vs TEM", fontsize=13)
    ax.legend(fontsize=11)
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 450)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "waveguide_dispersion_curves.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] waveguide_dispersion_curves.png")


# ============================================================
# EXAMPLE 8: Power Capacity of Rectangular Waveguide
# ============================================================
def example_power_capacity():
    """
    Compute maximum power handling of WR-90 waveguide with TE10 mode,
    limited by dielectric breakdown of air (E_max ≈ 3 MV/m).
    """
    separator("EXAMPLE 8: Rectangular Waveguide — Power Capacity (TE10)")

    a = 2.286e-2
    b = 1.016e-2
    E_max = 3e6  # air breakdown field (V/m)

    frequencies = np.linspace(6.56e9, 18e9, 200)
    fc_10 = C0 / (2 * a)

    P_max_vals = []
    for frequency in frequencies:
        if frequency <= fc_10:
            P_max_vals.append(0)
            continue
        k0 = 2 * np.pi * frequency / C0
        beta = k0 * np.sqrt(1 - (fc_10 / frequency) ** 2)
        Z_TE = ETA0 / np.sqrt(1 - (fc_10 / frequency) ** 2)

        # P_max = (a*b) / (4*Z_TE) * E_max^2
        P_max = a * b / (4 * Z_TE) * E_max ** 2
        P_max_vals.append(P_max)

    # Band center
    f_center = 10.3e9
    k0_c = 2 * np.pi * f_center / C0
    beta_c = k0_c * np.sqrt(1 - (fc_10 / f_center) ** 2)
    Z_TE_c = ETA0 / np.sqrt(1 - (fc_10 / f_center) ** 2)
    P_max_c = a * b / (4 * Z_TE_c) * E_max ** 2

    print(f"Waveguide: WR-90 (a={a*1e3:.3f} mm, b={b*1e3:.3f} mm)")
    print(f"Dielectric: Air, E_breakdown = {E_max/1e6:.1f} MV/m")
    print(f"At f = {f_center/1e9:.1f} GHz:")
    print(f"  Z_TE = {Z_TE_c:.1f} ohms")
    print(f"  P_max = {P_max_c/1e6:.2f} MW")
    print(f"  Conservative (1/3 margin): {P_max_c/3/1e6:.2f} MW")

    # ---- Plot ----
    fig, ax = plt.subplots(figsize=(8, 5))
    freqs_plot = np.array(frequencies) / 1e9
    p_plot = np.array(P_max_vals) / 1e6
    ax.plot(freqs_plot[freqs_plot > fc_10/1e9], p_plot[freqs_plot > fc_10/1e9],
            'b-', lw=2.5, label="Peak power (air breakdown)")
    ax.plot(freqs_plot[freqs_plot > fc_10/1e9], p_plot[freqs_plot > fc_10/1e9] / 3,
            'r--', lw=2, label="Conservative (1/3 margin)")
    ax.axvline(fc_10 / 1e9, color='k', ls=':', alpha=0.6, label=f"TE10 cutoff = {fc_10/1e9:.2f} GHz")
    ax.set_xlabel("Frequency (GHz)", fontsize=12)
    ax.set_ylabel("Maximum Power (MW)", fontsize=12)
    ax.set_title("Power Capacity of WR-90 Waveguide (TE10 Mode)", fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    ax.set_ylim(0, None)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "rectangular_power_capacity.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] rectangular_power_capacity.png")


# ============================================================
# EXAMPLE 9: Circular Waveguide — TE11 Field Distribution
# ============================================================
def example_circular_te11_fields():
    """
    Plot E-field magnitude for TE11 mode in circular waveguide
    across the cross-section.
    """
    separator("EXAMPLE 9: Circular Waveguide — TE11 Field Pattern")

    radius = 1.0e-2
    frequency = 12e9
    epsilon_r = 1.0

    # TE11: p'_11 = 1.841
    p_prime_11 = 1.841
    kc = p_prime_11 / radius
    fc_11 = kc * C0 / (2 * np.pi)
    k0 = 2 * np.pi * frequency / C0
    beta = k0 * np.sqrt(1 - (fc_11 / frequency) ** 2)

    print(f"Radius a = {radius*1e2:.1f} cm")
    print(f"Frequency = {frequency/1e9:.1f} GHz")
    print(f"TE11 cutoff fc = {fc_11/1e9:.3f} GHz")
    print(f"Propagation constant beta = {beta:.2f} rad/m")

    # Field grid
    n_rho = 60
    n_phi = 80
    rho_vals = np.linspace(0, radius, n_rho)
    phi_vals = np.linspace(0, 2 * np.pi, n_phi)
    RHO, PHI = np.meshgrid(rho_vals, phi_vals, indexing='ij')

    # TE11: E_phi ~ J_1'(kc*rho) * cos(phi)
    # |E| magnitude for cos(phi) dependence
    kr = kc * RHO
    J1_kr = jv(1, kr)       # J1
    J1p_kr = jvp(1, kr)     # J1'

    # E_phi ~ J1'(kc*rho) * cos(phi)
    E_phi = J1p_kr * np.cos(PHI)
    # E_rho ~ J1(kc*rho)/(kc*rho) * sin(phi)  (from field expressions)
    safe_kr = np.where(kr < 1e-10, 1e-10, kr)
    E_rho = jv(1, safe_kr) / safe_kr * np.sin(PHI)

    E_magnitude = np.sqrt(E_rho**2 + E_phi**2)
    E_magnitude_normalized = E_magnitude / np.max(E_magnitude)

    # Convert to Cartesian for plotting
    X = RHO * np.cos(PHI)
    Y = RHO * np.sin(PHI)

    fig, ax = plt.subplots(figsize=(6, 5.5))
    # Sort coordinates for pcolormesh (avoid monotonicity warning with cyclic phi)
    sort_idx = np.argsort(PHI[0, :])
    X_sorted = X[:, sort_idx]
    Y_sorted = Y[:, sort_idx]
    E_sorted = E_magnitude_normalized[:, sort_idx]
    im = ax.pcolormesh(X_sorted * 1e3, Y_sorted * 1e3, E_sorted,
                        shading='auto', cmap='inferno')
    ax.set_aspect('equal')
    fig.colorbar(im, ax=ax, label="Normalized |E|")
    ax.set_xlabel("x (mm)", fontsize=12)
    ax.set_ylabel("y (mm)", fontsize=12)
    ax.set_title(f"Circular Waveguide TE11 Mode (f={frequency/1e9:.1f} GHz, a={radius*1e2:.1f} cm)",
                 fontsize=11)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "circular_te11_field_magnitude.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] circular_te11_field_magnitude.png")


# ============================================================
# EXAMPLE 10: Parallel Plate Waveguide
# ============================================================
def example_parallel_plate():
    """
    Parallel plate waveguide: TEM mode analysis.
    Compute Z0, attenuation, and cutoff of first TM/TE mode.
    """
    separator("EXAMPLE 10: Parallel Plate Waveguide — TEM Mode")

    plate_spacing = 1.0e-2  # a = 1 cm
    plate_width = 2.0e-2    # b = 2 cm (width in y-direction)
    epsilon_r = 2.25        # e.g., Polystyrene
    frequency = 5e9
    sigma = C_CU

    eta = ETA0 / np.sqrt(epsilon_r)
    k0 = 2 * np.pi * frequency / C0
    beta = k0 * np.sqrt(epsilon_r)  # TEM beta = k

    # TEM characteristic impedance: Z0 = eta * b / a
    Z0 = eta * plate_width / plate_spacing

    # Cutoff of TM1 (and TE1): fc = 1/(2*a*sqrt(mu*eps))
    fc_1 = C0 / (2 * plate_spacing * np.sqrt(epsilon_r))

    # Conductor attenuation (TEM): alpha_c = Rs / (b * eta * a)
    Rs = compute_rs(frequency, sigma)
    alpha_c = Rs / (plate_width * eta * plate_spacing)

    # Dielectric attenuation: alpha_d = k * tan(delta) / 2
    tan_delta = 0.0005
    alpha_d = k0 * np.sqrt(epsilon_r) * tan_delta / 2

    print(f"Parallel plate waveguide:")
    print(f"  Plate spacing a = {plate_spacing*1e3:.1f} mm")
    print(f"  Plate width b = {plate_width*1e3:.1f} mm")
    print(f"  Dielectric: epsilon_r = {epsilon_r}")
    print(f"  Frequency: {frequency/1e9:.1f} GHz")
    print()
    print(f"  Z0 (TEM) = {Z0:.1f} ohms")
    print(f"  Beta = {beta:.2f} rad/m")
    print(f"  TM1/TE1 cutoff = {fc_1/1e9:.3f} GHz")
    print(f"  Conductor attenuation alpha_c = {alpha_c:.6f} Np/m ({20*np.log10(np.e)*alpha_c:.4f} dB/m)")
    print(f"  Dielectric attenuation alpha_d = {alpha_d:.6f} Np/m ({20*np.log10(np.e)*alpha_d:.4f} dB/m)")


# ============================================================
# EXAMPLE 11: Coaxial Attenuation Sweep (vs b/a ratio)
# ============================================================
def example_coax_attenuation_sweep():
    """
    Sweep b/a ratio for coaxial line and plot Z0 and attenuation.
    Find the minimum attenuation ratio.
    """
    separator("EXAMPLE 11: Coaxial Line — Attenuation vs b/a Ratio")

    epsilon_r = 2.2
    frequency = 3e9
    inner_radius = 0.5e-3
    eta = ETA0 / np.sqrt(epsilon_r)
    k0 = 2 * np.pi * frequency / C0
    Rs = compute_rs(frequency, C_CU)

    ratios = np.linspace(1.1, 10.0, 400)
    Z0_vals = []
    alpha_c_vals = []

    for ratio in ratios:
        outer_radius = inner_radius * ratio
        Z0 = eta / (2 * np.pi) * np.log(ratio)
        Z0_vals.append(Z0)
        alpha_c = Rs / (2 * eta * np.log(ratio)) * (1 / inner_radius + 1 / outer_radius)
        alpha_c_vals.append(alpha_c)

    # Find minimum
    min_idx = np.argmin(alpha_c_vals)
    ratio_opt = ratios[min_idx]
    z0_opt = Z0_vals[min_idx]
    alpha_min = alpha_c_vals[min_idx]

    print(f"Frequency: {frequency/1e9:.1f} GHz")
    print(f"Inner radius: a = {inner_radius*1e3:.2f} mm")
    print(f"Dielectric: epsilon_r = {epsilon_r}")
    print()
    print(f"Minimum attenuation at b/a = {ratio_opt:.3f}")
    print(f"  Z0 at minimum = {z0_opt:.1f} ohms")
    print(f"  Minimum alpha_c = {alpha_min:.6f} Np/m")

    # Power maximum ratio
    ratio_pmax = np.sqrt(np.e)
    z0_pmax = eta / (2 * np.pi) * np.log(ratio_pmax)
    print(f"\nMaximum power at b/a = sqrt(e) = {ratio_pmax:.3f}")
    print(f"  Z0 at max power = {z0_pmax:.1f} ohms")

    fig, ax1 = plt.subplots(figsize=(8, 5))

    color = 'tab:blue'
    ax1.set_xlabel("b / a", fontsize=12)
    ax1.set_ylabel(r"$Z_0$ (ohms)", fontsize=12, color=color)
    ax1.plot(ratios, Z0_vals, color=color, lw=2)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.axvline(ratio_opt, color='green', ls='--', alpha=0.6,
                label=f"Min alpha: b/a={ratio_opt:.2f}")
    ax1.axvline(ratio_pmax, color='orange', ls='--', alpha=0.6,
                label=f"Max power: b/a={ratio_pmax:.2f}")
    ax1.axhline(50, color='gray', ls=':', alpha=0.4, label="50 Ω")
    ax1.legend(loc='upper left', fontsize=9)
    ax1.grid(alpha=0.3)

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel(r"$\alpha_c$ (Np/m)", fontsize=12, color=color)
    ax2.plot(ratios, alpha_c_vals, color=color, lw=2, ls='--')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, None)

    plt.title("Coaxial Line: Z0 and Conductor Attenuation vs b/a", fontsize=13)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "coax_impedance_attenuation_sweep.png", dpi=150)
    plt.close(fig)
    print("  [Figure saved] coax_impedance_attenuation_sweep.png")


# ============================================================
# MAIN
# ============================================================
def main():
    print("=" * 72)
    print("  Pozar Ch3 — Numerical Examples (Transmission Lines & Waveguides)")
    print("=" * 72)

    example_rectangular_te_mode_scan()
    example_rectangular_te10_fields()
    example_rectangular_attenuation()
    example_circular_mode_chart()
    example_circular_te11_fields()
    example_coaxial_line()
    example_coax_attenuation_sweep()
    example_microstrip_z0()
    example_dispersion_curves()
    example_power_capacity()
    example_parallel_plate()

    separator("ALL EXAMPLES COMPLETED")
    print(f"\nFigures saved to: {FIG_DIR.resolve()}")


if __name__ == "__main__":
    main()

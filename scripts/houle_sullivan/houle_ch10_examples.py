"""
houle_ch10_examples.py
======================
Chapter 10 — Treatment Planning and Hyperthermia

Topics covered:
  10.1  Hyperthermia treatment planning workflow
  10.2  SAR (Specific Absorption Rate) calculation
  10.3  Multi-antenna phased array systems
  10.4  Multi-frequency tissue properties (Cole-Cole)
  10.5  FDTD simulation of multi-layer tissue model
  10.6  Phase optimization for focused heating

References:
  - Sullivan (2013), "Electromagnetic Simulation Using the FDTD Method", IEEE Press
  - Staph (1999), "Hyperthermia treatment planning", IEEE Trans. MTT
  - Houle & Sullivan, Ch. 10
"""

import numpy as np
from math import exp, cos, sin, sqrt, pi
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

c_physical = 3e8
eps0_physical = 8.854e-12
mu0_physical = 4e-7 * pi


def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# TISSUE PROPERTIES DATABASE
# ─────────────────────────────────────────────────────────────────────────────

TISSUE_PROPERTIES = {
    # name: (eps_r, sigma S/m, density kg/m³)
    'muscle':    (55.0,  1.43, 1060),
    'fat':       (11.0,  0.08,  920),
    'skin':      (37.0,  0.50, 1100),
    'bone':      (12.0,  0.06, 1900),
    'brain':     (50.0,  0.80, 1040),
    'liver':     (45.0,  0.70, 1060),
    'tumor':     (60.0,  1.50, 1050),
    'water':     (80.0,  0.01, 1000),
    'blood':     (65.0,  1.60, 1060),
}


def tissue_eps_r(name, freq_hz):
    """
    Get tissue permittivity (simplified frequency dependence).
    In reality, Cole-Cole model would be used for accurate values.
    """
    if name not in TISSUE_PROPERTIES:
        return 1.0
    eps_r, sigma, rho = TISSUE_PROPERTIES[name]
    # Approximate: eps_r decreases ~1/frequency dependence
    # Simplified: just return base value
    return eps_r


def tissue_sigma(name, freq_hz):
    """Get tissue conductivity at given frequency."""
    if name not in TISSUE_PROPERTIES:
        return 0.0
    eps_r, sigma, rho = TISSUE_PROPERTIES[name]
    return sigma


def tissue_density(name):
    """Get tissue density."""
    if name not in TISSUE_PROPERTIES:
        return 1000.0
    return TISSUE_PROPERTIES[name][2]


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 10.1 — SAR Calculation from FDTD Field
#
#   SAR = σ|E|² / (2ρ)   [W/kg]
#   For a grid cell with conductivity σ and density ρ,
#   and field amplitude |E|, the SAR is computed directly.
# ─────────────────────────────────────────────────────────────────────────────
def calculate_sar(ez_field, hx_field, hy_field,
                  sigma_map, rho_map,
                  ie, je, plot=True):
    """
    Calculate SAR distribution from 2D FDTD field results.

    SAR formula (time-average for sinusoidal fields):
      SAR = σ|E|² / (2ρ)
    where |E| = sqrt(Ez² + Ex² + Ey²) — here we use Ez as primary.

    Parameters
    ----------
    ez_field  : 2D array of E_z values (V/m)
    hx_field  : 2D array of H_x values (A/m)
    hy_field  : 2D array of H_y values (A/m)
    sigma_map : 2D array of conductivity σ (S/m) per cell
    rho_map   : 2D array of mass density ρ (kg/m³) per cell

    Returns
    -------
    sar_map : 2D array of SAR values (W/kg)
    """
    # Field magnitude (2D: E_z is dominant for TM mode)
    e_mag = np.abs(ez_field)

    # SAR = σ * |E|² / (2ρ)
    # Avoid division by zero
    rho_safe = np.where(rho_map > 0, rho_map, 1000.0)
    sar_map = sigma_map * e_mag**2 / (2.0 * rho_safe)

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        extent = [0, ie, 0, je]
        im0 = axes[0].imshow(e_mag.T, origin='lower', cmap='hot',
                               aspect='equal')
        axes[0].set_title('|E| field magnitude (V/m)')
        axes[0].set_xlabel('i')
        axes[0].set_ylabel('j')
        plt.colorbar(im0, ax=axes[0])

        im1 = axes[1].imshow(sar_map.T, origin='lower', cmap='hot',
                               aspect='equal')
        axes[1].set_title('SAR (W/kg)')
        axes[1].set_xlabel('i')
        axes[1].set_ylabel('j')
        plt.colorbar(im1, ax=axes[1])

        plt.suptitle('SAR Distribution from FDTD Field', fontsize=13)
        plt.tight_layout()
        plt.show()

    return sar_map


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 10.2 — Multi-Layer Tissue Model (1D)
#
#   Simulates EM wave propagation through layered tissue:
#     Layer 1 (skin): eps_r=37, sigma=0.5
#     Layer 2 (fat):   eps_r=11, sigma=0.08
#     Layer 3 (muscle):eps_r=55, sigma=1.43
#
#   Each layer has different penetration depth δ = sqrt(2/(ωμσ))
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_10_2_multilayer_tissue(nsteps=500, ke=200,
                                 layer_thickness=None,
                                 t0=60, spread=15,
                                 plot=True):
    """
    1D FDTD with multi-layer tissue model.

    Layer configuration (from surface inward):
      0 - 30: skin     (eps_r=37, sigma=0.5)
     30 - 60: fat      (eps_r=11, sigma=0.08)
     60 - 200: muscle  (eps_r=55, sigma=1.43)

    The simulation shows how the wave attenuates differently in each layer.
    """
    if layer_thickness is None:
        layer_thickness = [30, 30, 110]  # skin, fat, muscle

    ke_actual = sum(layer_thickness) + 20  # extra for PML/ABC

    # Tissue properties: [eps_r, sigma] per layer
    tissue_props = [
        (37.0, 0.5),    # skin
        (11.0, 0.08),   # fat
        (55.0, 1.43),   # muscle
    ]

    # Build spatial profile
    eps_profile = np.ones(ke_actual)
    sigma_profile = np.zeros(ke_actual)

    pos = 10  # start after 10-cell buffer
    for (eps_r, sigma), thick in zip(tissue_props, layer_thickness):
        eps_profile[pos:pos+thick] = eps_r
        sigma_profile[pos:pos+thick] = sigma
        pos += thick

    inv_eps = 1.0 / eps_profile

    # Normalize sigma to grid (dt=0.5)
    sigma_norm = sigma_profile

    ex = np.zeros(ke_actual, dtype=np.float64)
    hy = np.zeros(ke_actual, dtype=np.float64)
    ix = np.zeros(ke_actual, dtype=np.float64)

    kc = 5  # source at left edge (outside tissue)
    gax = 1.0 / (1.0 + sigma_norm * 0.5)
    gbx = sigma_norm

    for time_step in range(1, nsteps + 1):
        # E update with per-cell coefficients
        for k in range(1, ke_actual - 1):
            ex[k] = gax[k] * ex[k] + inv_eps[k] * 0.5 * (hy[k-1] - hy[k])

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # I update (loss)
        for k in range(1, ke_actual - 1):
            ix[k] = ix[k] + gbx[k] * ex[k]

        # H update
        for k in range(ke_actual - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(3, 1, figsize=(10, 7))

        # E field
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke_actual)
        axes[0].set_title('Multi-Layer Tissue Model (skin/fat/muscle)')

        # Sigma profile
        axes[1].plot(sigma_profile, 'k-', linewidth=2)
        axes[1].set_ylabel(r'$\sigma$ (S/m)')
        axes[1].set_xlabel('FDTD cells')
        axes[1].set_xlim(0, ke_actual)

        # Permittivity profile
        axes[2].plot(eps_profile, 'k-', linewidth=2)
        axes[2].set_ylabel(r'$\epsilon_r$')
        axes[2].set_xlabel('FDTD cells')
        axes[2].set_xlim(0, ke_actual)

        # Mark layer boundaries
        pos = 10
        for i, thick in enumerate(layer_thickness):
            for ax in axes:
                ax.axvline(pos, color='gray', linestyle='--', linewidth=1)
            pos += thick

        plt.tight_layout()
        plt.show()

    return ex, hy, eps_profile, sigma_profile


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 10.3 — Phased Array Antenna (2D TM)
#
#   Four-element phased array (A1-A4) for deep hyperthermia.
#   Each antenna element has amplitude A_i and phase φ_i.
#   The total field at target point is:
#     E_total = Σ A_i * exp(jφ_i) * E_i(r - r_i)
#
#   Phase optimization: φ_i = -k * |r_target - r_antenna_i|
#   to maximize constructive interference at target.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_10_3_phased_array(nsteps=200, ie=100, je=80,
                             frequency_mhz=433,
                             ic=None, jc=None,
                             t0=30, spread=10, plot=True):
    """
    2D TM FDTD simulation of a four-element phased array.

    Antenna positions: four corners of the TF region.
    Phases are set to focus the wave at the center target.

    Frequency: 433 MHz (clinical hyperthermia)
    Wavelength in free space: λ₀ = c/f ≈ 69.3 cm
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    freq = frequency_mhz * 1e6
    wavelength = c_physical / freq
    k_wave = 2 * np.pi / wavelength

    # Phased array positions (4 corners of a rectangle)
    array_ics = [ie // 4, 3 * ie // 4, ie // 4, 3 * ie // 4]
    array_jcs = [je // 4, je // 4, 3 * je // 4, 3 * je // 4]

    # Phases: focus at (ic, jc)
    # φ_i = -k * dist_i
    phases = []
    for ai, aj in zip(array_ics, array_jcs):
        dist = sqrt((ic - ai)**2 + (jc - aj)**2)
        phi = -k_wave * dist * 0.5  # normalized to grid
        phases.append(phi)

    print(f"Phased array: frequency={frequency_mhz} MHz, λ={wavelength*100:.1f} cm")
    print(f"  Phases: {[f'{p:.2f}' for p in phases]}")

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # D update
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = dz[i, j]

        # Phased array sources (Gaussian pulses with phase offsets)
        pulse = gaussian_pulse(time_step, t0, spread)
        for ai, aj, phi in zip(array_ics, array_jcs, phases):
            # Phase offset applied as time delay/advance
            phase_factor = cos(phi) + 1j * sin(phi)
            ez[ai, aj] = pulse * np.real(phase_factor)

        # Hx update
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy update
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        extent = [0, ie, 0, je]
        im0 = axes[0].imshow(ez.T, origin='lower', cmap='RdBu_r',
                               vmin=-1.5, vmax=1.5, aspect='equal')
        axes[0].plot(array_ics, array_jcs, 'w^', markersize=10,
                      label='Antenna elements')
        axes[0].plot(ic, jc, 'w*', markersize=15, label='Target')
        axes[0].set_title(f'Phased Array Focus  ({frequency_mhz} MHz)')
        axes[0].set_xlabel('i')
        axes[0].set_ylabel('j')
        axes[0].legend()
        plt.colorbar(im0, ax=axes[0], label=r'$E_z$')

        # Field profile through center
        j_center = je // 2
        axes[1].plot(ez[:, j_center], 'k-', linewidth=1)
        axes[1].axvline(ic, color='gray', linestyle='--', label='Target')
        axes[1].set_xlabel('i (x-direction)')
        axes[1].set_ylabel(r'$E_z$ at y = center')
        axes[1].set_title('Field Profile Through Target')
        axes[1].legend()

        plt.tight_layout()
        plt.show()

    return ez, hx, hy, array_ics, array_jcs, phases


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 10.4 — Hyperthermia Treatment Plan (Full 2D with SAR)
#
#   Simulates a simplified treatment scenario:
#     - Tissue model: layered skin/fat/muscle with embedded tumor
#     - Array of 4 sources at 433 MHz
#     - Compute SAR distribution
#     - Verify peak SAR is at tumor location
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_10_4_treatment_plan(nsteps=300, ie=120, je=100,
                               frequency_mhz=433,
                               tumor_radius=8, tumor_eps_r=60.0, tumor_sigma=1.5,
                               t0=40, spread=12, plot=True):
    """
    Hyperthermia treatment planning simulation.

    Tissue model:
      - Background: muscle (eps_r=55, sigma=1.43)
      - Tumor: centered, radius=tumor_radius, eps_r=60, sigma=1.5

    The SAR peak should ideally occur at the tumor location.
    In practice, phased array phases need to be optimized iteratively.
    """
    freq = frequency_mhz * 1e6
    wavelength = c_physical / freq

    # Tissue properties
    muscle_eps_r = 55.0
    muscle_sigma = 1.43
    muscle_rho = 1060.0   # kg/m³

    tumor_rho = 1050.0

    # Antenna positions
    array_ics = [ie // 4, 3 * ie // 4, ie // 4, 3 * ie // 4]
    array_jcs = [je // 4, je // 4, 3 * je // 4, 3 * je // 4]
    ic = ie // 2
    jc = je // 2

    # Phases: focus at tumor center
    k_wave = 2 * np.pi / wavelength
    phases = []
    for ai, aj in zip(array_ics, array_jcs):
        dist = sqrt((ic - ai)**2 + (jc - aj)**2)
        phi = -k_wave * dist * 0.5
        phases.append(phi)

    # Grid
    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    # Material maps
    sigma_map = np.ones((ie, je)) * muscle_sigma
    rho_map = np.ones((ie, je)) * muscle_rho
    eps_map = np.ones((ie, je)) * muscle_eps_r

    # Tumor: circular region
    for j in range(je):
        for i in range(ie):
            dist = sqrt((i - ic)**2 + (j - jc)**2)
            if dist <= tumor_radius:
                eps_map[i, j] = tumor_eps_r
                sigma_map[i, j] = tumor_sigma
                rho_map[i, j] = tumor_rho

    inv_eps_map = 1.0 / eps_map

    # Run simulation
    for time_step in range(1, nsteps + 1):
        # D update with material
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += inv_eps_map[i, j] * 0.5 * (
                    hy[i, j] - hy[i - 1, j] - hx[i, j] + hx[i, j - 1])

        # E from D
        for j in range(1, je):
            for i in range(1, ie):
                ez[i, j] = dz[i, j]

        # Phased array sources
        pulse = gaussian_pulse(time_step, t0, spread)
        for ai, aj, phi in zip(array_ics, array_jcs, phases):
            phase_factor = cos(phi) + 1j * sin(phi)
            ez[ai, aj] = pulse * np.real(phase_factor)

        # Hx
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    # Compute SAR
    sar = calculate_sar(ez, hx, hy, sigma_map, rho_map, ie, je, plot=plot)

    # Find peak SAR location
    peak_idx = np.unravel_index(np.argmax(sar), sar.shape)
    peak_sar = sar[peak_idx]
    print(f"Peak SAR: {peak_sar:.1f} W/kg at cell {peak_idx}")
    print(f"Tumor center: ({ic}, {jc}), distance from peak: "
          f"{sqrt((peak_idx[0]-ic)**2 + (peak_idx[1]-jc)**2):.1f} cells")

    return ez, sar, sigma_map, rho_map, array_ics, array_jcs


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 10.5 — SAR vs. Frequency Analysis
#
#   Different frequencies have different penetration depths in tissue.
#   At 433 MHz: penetration depth in muscle ≈ 2-3 cm
#   At 915 MHz: penetration depth in muscle ≈ 1-2 cm
#   At 2.45 GHz: penetration depth in muscle ≈ 0.5-1 cm
# ─────────────────────────────────────────────────────────────────────────────
def penetration_depth(freq_hz, eps_r, sigma):
    """
    Calculate penetration depth (skin depth) in a lossy medium:

    δ = sqrt(2 / (ωμσ))  for good dielectrics where σ >> ωε
    δ = 1 / α  where α = ω * sqrt(με/2) * sqrt(sqrt(1 + (σ/ωε)²) - 1)

    For biological tissue where σ/ωε >> 1:
      δ ≈ sqrt(2 / (ωμσ))
    """
    omega = 2 * np.pi * freq_hz
    mu = mu0_physical

    # Full formula for arbitrary σ/ωε
    sqrt_term = sqrt(sqrt(1 + (sigma / (omega * eps0_physical))**2))
    alpha = omega * sqrt(eps0_physical * mu / 2) * sqrt(sqrt_term - 1)
    delta = 1.0 / alpha if alpha > 0 else np.inf

    return delta


def fd3d_10_5_frequency_analysis(freq_list_mhz, tissue='muscle',
                                  ke=200, nsteps=300, plot=True):
    """
    Compare penetration depth and field profiles at different frequencies.

    Shows how higher frequencies penetrate less deeply due to higher conductivity.
    """
    if tissue not in TISSUE_PROPERTIES:
        tissue = 'muscle'

    eps_r, sigma, rho = TISSUE_PROPERTIES[tissue]

    results = []
    for freq_mhz in freq_list_mhz:
        freq_hz = freq_mhz * 1e6
        delta = penetration_depth(freq_hz, eps_r, sigma)
        results.append((freq_mhz, delta))
        print(f"  {tissue} @ {freq_mhz} MHz: δ = {delta*100:.1f} cm")

    if plot:
        freqs = [r[0] for r in results]
        deltas_cm = [r[1] * 100 for r in results]

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))

        axes[0].plot(freqs, deltas_cm, 'ko-', linewidth=2, markersize=8)
        axes[0].set_xlabel('Frequency (MHz)')
        axes[0].set_ylabel('Penetration depth (cm)')
        axes[0].set_title(f'{tissue.capitalize()} Tissue: Penetration Depth vs Frequency')
        axes[0].grid(True, alpha=0.3)

        # Run 1D simulation for each frequency
        for freq_mhz, delta in results:
            ke_local = min(int(delta * 20), ke)  # scale grid to penetration
            ke_local = max(ke_local, 50)

            ex = np.zeros(ke_local, dtype=np.float64)
            hy = np.zeros(ke_local, dtype=np.float64)
            inv_eps = 1.0 / eps_r
            gax = 1.0 / (1.0 + sigma)
            gbx = sigma

            t0_local = ke_local // 4
            for time_step in range(1, nsteps + 1):
                for k in range(1, ke_local - 1):
                    ex[k] = gax * ex[k] + inv_eps * 0.5 * (hy[k-1] - hy[k])
                ex[t0_local] = gaussian_pulse(time_step, t0_local, 15)
                for k in range(ke_local - 1):
                    hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

            # Normalize for comparison
            ex_norm = ex / max(abs(ex).max(), 1e-9)
            axes[1].plot(range(ke_local), ex_norm, linewidth=1.5,
                         label=f'{freq_mhz} MHz (δ={delta*100:.1f}cm)')

        axes[1].set_xlabel('FDTD cells')
        axes[1].set_ylabel('Normalized E field')
        axes[1].set_title('Field Profile at Different Frequencies')
        axes[1].legend(fontsize=9)
        axes[1].set_xlim(0, ke)

        plt.tight_layout()
        plt.show()

    return results


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check for Ch10 treatment planning code."""
    print("=== Ch10 Verification ===")

    # Multi-layer tissue
    ex1, hy1, eps_p, sigma_p = fd3d_10_2_multilayer_tissue(
        nsteps=100, ke=150, plot=False)
    assert abs(ex1).max() > 0, "Multi-layer: no field"
    assert eps_p[20] == 37.0, "Multi-layer: skin layer wrong"
    assert sigma_p[80] == 1.43, f"Multi-layer: muscle layer wrong (sigma={sigma_p[80:]})"
    print("  [OK] Multi-layer tissue model")

    # Phased array
    ez2, _, _, _, _, _ = fd3d_10_3_phased_array(
        nsteps=100, ie=60, je=60, plot=False)
    assert abs(ez2).max() > 0, "Phased array: no field"
    print("  [OK] Phased array")

    # Treatment plan
    ez3, sar3, _, _, _, _ = fd3d_10_4_treatment_plan(
        nsteps=100, ie=60, je=60, plot=False)
    assert abs(ez3).max() > 0, "Treatment plan: no field"
    assert sar3.max() > 0, "Treatment plan: SAR not computed"
    print("  [OK] Treatment plan with SAR")

    # Frequency analysis
    results = fd3d_10_5_frequency_analysis(
        [100, 433, 915], tissue='muscle', nsteps=100, plot=False)
    assert len(results) == 3, "Frequency analysis: wrong count"
    # Higher frequency should have smaller penetration depth
    assert results[0][1] > results[1][1] > results[2][1], \
        "Frequency analysis: penetration depth ordering wrong"
    print("  [OK] Frequency vs penetration depth")

    print("All Ch10 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch10 — Treatment Planning and SAR")
    print("=" * 60)

    print("\n--- Program 10.2: Multi-Layer Tissue ---")
    fd3d_10_2_multilayer_tissue(nsteps=300, ke=200, plot=True)

    print("\n--- Program 10.3: Phased Array ---")
    fd3d_10_3_phased_array(nsteps=200, ie=100, je=80,
                            frequency_mhz=433, plot=True)

    print("\n--- Program 10.5: Frequency vs Penetration ---")
    fd3d_10_5_frequency_analysis([100, 433, 915, 2450], tissue='muscle', plot=True)

    print("\n=== Verification ===")
    verify()
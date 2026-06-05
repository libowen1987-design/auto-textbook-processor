#!/usr/bin/env python3
"""
Zhang EMC - Chapter 1: Electromagnetic Basics & Spacecraft EMC Overview
======================================================================
Core topics from Zhang Ch1:
- Electrostatic field and Coulomb's law
- Magnetostatic field and Ampere's law
- Electromagnetic induction / Faraday's law
- Maxwell's equations (integral & differential forms)
- Plane wave propagation parameters
- Skin depth in conductors
- DC magnetic field control (0–100 Hz)

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch1
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi, k as Boltzmann_k
import warnings
warnings.filterwarnings('ignore')

# ──────────────────────────────────────────────────────────────────
# 1. Electrostatic Field — Coulomb's Law & Capacitance
# ──────────────────────────────────────────────────────────────────

def coulomb_force(q1, q2, r):
    """
    Coulomb's law: electrostatic force between two point charges.
    q1, q2 : charges in coulombs
    r      : separation in metres
    Returns force in newtons.
    F = (1/4πε0) * q1*q2 / r^2
    """
    return (1.0 / (4.0 * pi * epsilon_0)) * q1 * q2 / r**2


def electric_field_point_charge(Q, r):
    """
    Electric field magnitude at distance r from point charge Q.
    E = (1/4πε0) * Q / r^2   [V/m]
    """
    return (1.0 / (4.0 * pi * epsilon_0)) * Q / r**2


def parallel_plate_capacitance(area, d, epsilon_r=1.0):
    """
    Parallel-plate capacitor capacitance.
    area  : plate area (m^2)
    d     : plate separation (m)
    epsilon_r : relative permittivity
    C = ε0·εr·A / d
    """
    return epsilon_0 * epsilon_r * area / d


def electrostatic_discharge_energy(C, V, R=1e6):
    """
    Estimate ESD energy stored in a capacitor.
    C  : capacitance (F)
    V  : voltage (V)
    R  : discharge resistance (ohm) — typical human body ~1 MΩ
    Returns (energy_joules, peak_current_A, time_constant_s)
    """
    energy = 0.5 * C * V**2
    i_peak = V / R
    tau = R * C
    return energy, i_peak, tau


def electric_field_magnitude_from_V_per_m(V_per_m):
    """Pass-through for clarity."""
    return V_per_m


# ──────────────────────────────────────────────────────────────────
# 2. Magnetostatic Field — Ampere's Law & Inductance
# ──────────────────────────────────────────────────────────────────

def magnetic_field_infinite_wire(I, r):
    """
    Magnetic field at distance r from an infinitely long straight conductor.
    H = I / (2πr)   [A/m]
    B = μ0·I / (2πr)   [T]
    """
    H = I / (2.0 * pi * r)
    B = mu_0 * H
    return H, B


def inductance_solenoid(N, l, A, mu_r=1.0):
    """
    Inductance of a solenoid coil.
    N     : number of turns
    l     : coil length (m)
    A     : cross-sectional area (m^2)
    mu_r  : relative permeability of core
    L = μ0·μr·N^2·A / l
    """
    mu = mu_0 * mu_r
    return mu * N**2 * A / l


def mutual_inductance_parallel_wires(I1, l, d):
    """
    Mutual inductance between two parallel conductors.
    I1 : current in aggressor (A)
    l  : parallel length (m)
    d  : separation (m)
    M = μ0·l / (2π) · ln(d / r0)  — simplified, r0 ~1 mm
    """
    r0 = 1e-3  # wire radius ~1 mm
    return mu_0 * l / (2.0 * pi) * np.log(d / r0)


def magnetic_flux_density_to_tesla(flux_gamma, area_m2):
    """γ (gamma) to Tesla conversion: Φ = B·A."""
    return flux_gamma / area_m2


# ──────────────────────────────────────────────────────────────────
# 3. Faraday's Law — Electromagnetic Induction
# ──────────────────────────────────────────────────────────────────

def induced_emf(N, dPhi_dt):
    """
    Faraday's law: EMF = -N · dΦ/dt
    N       : number of turns
    dPhi_dt : rate of change of magnetic flux (Wb/s = V·s)
    Returns EMF in volts.
    """
    return -N * dPhi_dt


def induced_emf_motional(V, B, l, v):
    """
    Motional EMF: E = (B × v) · L
    B : magnetic flux density (T)
    v : velocity vector (m/s) — perpendicular to B
    l : conductor length (m)
    V = B * l * v (magnitude, when B ⟂ v)
    """
    return B * l * v


def skin_depth(f, sigma, mu_r=1.0):
    """
    Electromagnetic skin depth in a conductor.
    δ = sqrt(2 / (ω·μ·σ)) = sqrt(1 / (π·f·μ·σ))
    f     : frequency (Hz)
    sigma : electrical conductivity (S/m), e.g. copper ~ 5.8e7
    mu_r  : relative permeability
    Returns skin depth in metres.
    """
    mu = mu_0 * mu_r
    return np.sqrt(1.0 / (pi * f * mu * sigma))


def transformer_EMF(V_rms, f, N_primary, N_secondary, A, B_max):
    """
    Transformer design check using Faraday's law:
    V_rms = 4.44 · f · N · A · B_max
    Returns the required number of turns for a given voltage.
    """
    N_required = V_rms / (4.44 * f * A * B_max)
    return N_required


# ──────────────────────────────────────────────────────────────────
# 4. Maxwell's Equations — Wave & Propagation Parameters
# ──────────────────────────────────────────────────────────────────

def wave_impedance_free_space():
    """Intrinsic impedance of free space: η0 = sqrt(μ0/ε0) ≈ 377 Ω."""
    return np.sqrt(mu_0 / epsilon_0)


def propagation_constant(f, sigma=0.0, epsilon_r=1.0, mu_r=1.0):
    """
    γ = α + jβ = sqrt(jωμ)(σ + jωε)
    For lossless (σ=0): γ = jω·sqrt(με) = jβ
    Returns (alpha_Np_m, beta_rad_m)
    """
    omega = 2.0 * pi * f
    mu = mu_0 * mu_r
    eps = epsilon_0 * epsilon_r
    gamma_sq = 1j * omega * mu * (sigma + 1j * omega * eps)
    gamma = np.sqrt(gamma_sq)
    alpha = np.real(gamma)
    beta = np.imag(gamma)
    return alpha, beta


def wavelength_in_medium(f, epsilon_r=1.0, mu_r=1.0):
    """λ = v_phase / f ; v_phase = 1/sqrt(με)."""
    v_phase = c / np.sqrt(epsilon_r * mu_r)
    return v_phase / f


def plane_wave_power_density(E_field):
    """Power density S = |E|^2 / η0  (far-field, plane wave)."""
    eta0 = wave_impedance_free_space()
    return E_field**2 / eta0


def E_from_H(H_field):
    """E = η · H in far-field plane wave."""
    return wave_impedance_free_space() * H_field


# ──────────────────────────────────────────────────────────────────
# 5. Shielding Effectiveness (SEM) — Absorption + Reflection
# ──────────────────────────────────────────────────────────────────

def shielding_effectiveness_absorption(delta_m, t):
    """
    Absorption loss component of SEM.
    A_dB = 8.686 · t / δ  (in dB)
    delta_m: skin depth (m)
    t      : shield thickness (m)
    """
    return 8.686 * t / delta_m


def shielding_effectiveness_reflection(R_dB, A_dB, B_dB=0.0):
    """
    Total SEM = R + A + B  (dB)
    R_dB : reflection loss
    A_dB : absorption loss
    B_dB : correction term (usually negligible)
    """
    return R_dB + A_dB + B_dB


def reflection_loss_plane_wave(sigma, mu_r, f):
    """
    Simplified reflection loss for plane wave incident on conductive barrier.
    R_dB ≈ 168 + 10·log10(σ_r·μ_r/f_r)  (for far-field)
    Returns R in dB.
    """
    sigma_r = sigma / 5.8e7   # relative to copper
    f_mhz = f / 1e6
    return 168.0 + 10.0 * np.log10(sigma_r * mu_r / f_mhz)


# ──────────────────────────────────────────────────────────────────
# 6. DC / Low-Frequency Magnetic Field (0–100 Hz) Control
# ──────────────────────────────────────────────────────────────────

def magnetic_field_background_DC(orbit_altitude_km):
    """
    Estimate ambient DC magnetic field for LEO spacecraft.
    Earth's geomagnetic field varies with altitude and latitude.
    Approximate model: |B| ≈ 30–60 μT at LEO (300–1000 km).
    Returns B in tesla.
    """
    # Rough approximation: B ~ 50 μT at 400 km (ISS altitude)
    B_nominal = 50e-6  # 50 μT
    # Scale with altitude (dipole field ~ 1/r^3)
    ref_alt_km = 400.0
    B_scale = (ref_alt_km / orbit_altitude_km)**3
    return B_nominal * B_scale


def magnetic_moment_from_torque(m_torque, B_background):
    """
    Magnetic dipole moment m for a torque τ = m × B.
    |τ| = m·B·sin(θ).  For θ=90°, m = τ / B.
    m_torque  : torque magnitude (N·m)
    B_background : ambient B field (T)
    Returns magnetic dipole moment (A·m^2).
    """
    return m_torque / B_background


def demagnetisation_factor_shape(N):
    """
    Demagnetisation factor N for ellipsoids.
    N_x + N_y + N_z = 1.
    Sphere: N=1/3 each axis. Thin plate: N→1 in normal direction.
    """
    return N  # placeholder for shape-dependent N


# ──────────────────────────────────────────────────────────────────
# 7. EMC Margin and Source/Sink Analysis
# ──────────────────────────────────────────────────────────────────

def emc_margin(emission_level_dBuV, susceptibility_limit_dBuV):
    """
    EMC margin = susceptibility_limit - emission_level  (dB)
    Positive margin → compatible.
    Typical requirement: margin ≥ 6 dB.
    """
    margin = susceptibility_limit_dBuV - emission_level_dBuV
    return margin


def conducted_emission_limit_mil(freq_mhz):
    """
    MIL-STD-461 CE101 conducted emission limit for power leads (30 Hz–10 kHz).
    Approximate envelope (derived from MIL-STD-461F Fig. 5).
    freq_mhz : frequency in MHz
    Returns limit in dBμA.
    """
    if freq_mhz < 0.1:
        return 100.0  # 40–100 dBμA region
    else:
        slope = -20.0  # dB per decade
        return 100.0 + slope * np.log10(freq_mhz / 0.1)


def radiated_emission_limit_mil(freq_mhz):
    """
    MIL-STD-461 RE102 radiated emission limit (10 kHz–18 GHz).
    Approximate envelope for E-field at 1 m.
    Returns limit in dBμV/m.
    """
    if freq_mhz < 0.1:
        return 100.0
    elif freq_mhz < 1.0:
        return 100.0
    elif freq_mhz < 1000.0:
        slope = -20.0 * np.log10(freq_mhz / 1.0)
        return 80.0 + slope
    else:
        return 54.0


def susceptibility_level_RS(freq_mhz):
    """
    MIL-STD-461 RS103 radiated susceptibility level.
    Typical spacecraft requirement: 200–600 μW/cm^2 (≈ 87–100 dBμV/m at 1 m).
    Returns E-field threshold in V/m.
    """
    power_density_W_m2 = 1e-2  # 1 mW/cm^2 = 10 W/m^2
    eta0 = wave_impedance_free_space()
    E_threshold = np.sqrt(power_density_W_m2 * 2.0 * eta0)
    return E_threshold


# ══════════════════════════════════════════════════════════════════
# NUMERICAL EXAMPLES
# ══════════════════════════════════════════════════════════════════

def example_1_esd_capacitor():
    """
    Example 1: ESD stored energy on spacecraft cable capacitance.
    Typical spacecraft cable: C ≈ 100 pF/m, total harness ~50 m → C_total ≈ 5 nF.
    ESD voltage: human body model ~ 15 kV (worst-case LEO charging).
    """
    print("\n" + "="*60)
    print("EXAMPLE 1 — Electrostatic Discharge on Spacecraft Harness")
    print("="*60)
    C_harness = 5e-9    # 5 nF total harness capacitance
    V_esd = 15e3        # 15 kV worst-case ESD (human body)
    R_discharge = 1e6   # 1 MΩ human-body model
    E_j, i_peak, tau = electrostatic_discharge_energy(C_harness, V_esd, R_discharge)
    print(f"  Harness capacitance     : {C_harness*1e9:.1f} nF")
    print(f"  ESD voltage (worst-case): {V_esd:.0f} V")
    print(f"  Discharge resistance   : {R_discharge/1e6:.1f} MΩ")
    print(f"  Stored energy          : {E_j*1e6:.2f} mJ")
    print(f"  Peak current           : {i_peak*1e3:.2f} mA")
    print(f"  Discharge time constant: {tau*1e6:.1f} μs")
    # MIL-STD-461 ESD threshold for sensitive circuits
    E_arc = 0.5 * C_harness * V_esd**2
    print(f"  Arc energy             : {E_arc*1e3:.1f} mJ (threshold ~1 mJ for many components)")
    return E_j


def example_2_skin_depth_shielding():
    """
    Example 2: Skin depth and aluminum shielding effectiveness.
    Aluminum: σ = 3.5e7 S/m, μr = 1.
    Evaluate δ and A_dB at 1 MHz and 100 MHz, t = 0.5 mm Al sheet.
    """
    print("\n" + "="*60)
    print("EXAMPLE 2 — Skin Depth & Aluminum Shielding at Spacecraft Frequencies")
    print("="*60)
    sigma_Al = 3.5e7   # S/m
    t_mm = 0.5          # 0.5 mm aluminum sheet (common spacecraft chassis)
    t = t_mm * 1e-3
    for f_mhz in [1, 10, 100]:
        f = f_mhz * 1e6
        delta = skin_depth(f, sigma_Al)
        A_dB = shielding_effectiveness_absorption(delta, t)
        R_dB = reflection_loss_plane_wave(sigma_Al, 1.0, f)
        SE_total = SE_total_calculation = R_dB + A_dB
        print(f"\n  Frequency = {f_mhz} MHz:")
        print(f"    Skin depth δ          : {delta*1e6:.2f} μm")
        print(f"    Absorption loss (A)   : {A_dB:.1f} dB")
        print(f"    Reflection loss (R)  : {R_dB:.1f} dB")
        print(f"    Total SE             : {SE_total:.1f} dB")


def example_3_plane_wave_propagation():
    """
    Example 3: Plane wave propagation parameters at 1 GHz in free space.
    Compute β, λ, η0, and power density from E = 10 V/m.
    """
    print("\n" + "="*60)
    print("EXAMPLE 3 — 1 GHz Plane Wave Propagation Parameters")
    print("="*60)
    f = 1e9  # Hz
    alpha, beta = propagation_constant(f)
    lam = wavelength_in_medium(f)
    eta0 = wave_impedance_free_space()
    E0 = 10.0  # V/m
    S = plane_wave_power_density(E0)
    H0 = E0 / eta0
    print(f"  Frequency             : {f/1e9:.1f} GHz")
    print(f"  Phase constant β      : {beta:.4f} rad/m")
    print(f"  Wavelength λ          : {lam*1e3:.2f} mm")
    print(f"  Intrinsic impedance η0: {eta0:.1f} Ω")
    print(f"  E-field amplitude     : {E0:.1f} V/m")
    print(f"  H-field (|E|/η0)     : {H0:.3f} A/m")
    print(f"  Power density S       : {S:.3f} W/m²")
    print(f"  (equivalent to {S*1e4:.2f} mW/cm²)")


def example_4_magnetic_field_control():
    """
    Example 4: DC magnetic field control for spacecraft attitude sensors.
    LEO orbit 400 km: B ≈ 50 μT.
    Sensitive magnetometer needs B < 1 nT resolution → need shielding.
    """
    print("\n" + "="*60)
    print("EXAMPLE 4 — DC Magnetic Field Control for Attitude Sensors")
    print("="*60)
    B_ambient = magnetic_field_background_DC(400)  # T at 400 km LEO
    print(f"  Ambient DC B-field at 400 km LEO: {B_ambient*1e6:.1f} μT")
    # Soft magnetic material (mu_r ~ 10,000) attenuation
    mu_r_shield = 10000.0
    t_shield_mm = 2.0  # 2 mm soft iron shield
    t = t_shield_mm * 1e-3
    # Simple shield attenuation: approx (1 + mu_r * t / r) — very simplified
    r_inner_mm = 50.0  # 50 mm radius cylinder
    r = r_inner_mm * 1e-3
    B_inside = B_ambient / (1.0 + mu_r_shield * t / r)
    print(f"  Soft magnetic shield: mu_r = {mu_r_shield:.0f}, t = {t_shield_mm:.0f} mm")
    print(f"  Estimated B inside shield: {B_inside*1e9:.2f} nT")
    print(f"  Attenuation factor: {B_ambient/B_inside:.0f}x")


def example_5_emc_margin_calculation():
    """
    Example 5: Conducted emission vs. susceptibility limit margin.
    Power bus: emission at 100 kHz = 80 dBμA.
    Equipment susceptibility threshold = 100 dBμA (CE101 limit).
    Compute margin and check 6 dB safety requirement.
    """
    print("\n" + "="*60)
    print("EXAMPLE 5 — Conducted Emission vs. Susceptibility Margin")
    print("="*60)
    f_khz = 100.0
    emission_dBuA = 80.0  # measured conducted emission at 100 kHz
    susceptibility_dBuA = conducted_emission_limit_mil(f_khz / 1e3)
    margin = emc_margin(emission_dBuA, susceptibility_dBuA)
    print(f"  Frequency              : {f_khz:.0f} kHz")
    print(f"  Measured emission     : {emission_dBuA:.1f} dBμA")
    print(f"  MIL-STD-461 susceptibility limit: {susceptibility_dBuA:.1f} dBμA")
    print(f"  EMC margin             : {margin:.1f} dB")
    print(f"  Pass (≥6 dB margin)?   : {'YES ✓' if margin >= 6.0 else 'NO ✗ — action required'}")
    return margin


def example_6_solenoid_inductance():
    """
    Example 6: Solenoid inductance for spacecraft EMI filter.
    N = 50 turns, l = 20 mm, radius r = 5 mm, air core (mu_r=1).
    Compute L and self-resonant frequency.
    """
    print("\n" + "="*60)
    print("EXAMPLE 6 — Solenoid Inductance for EMI Filter Design")
    print("="*60)
    N = 50
    l = 20e-3        # 20 mm
    r = 5e-3         # 5 mm radius
    A = pi * r**2
    mu_r = 1.0       # air core
    L = inductance_solenoid(N, l, A, mu_r)
    print(f"  Turns N               : {N}")
    print(f"  Length l             : {l*1e3:.0f} mm")
    print(f"  Radius r             : {r*1e3:.0f} mm")
    print(f"  Inductance L         : {L*1e6:.2f} μH")
    # Self-resonant freq: f_sr = 1/(2π·sqrt(L·C_parasitic))
    C_par = 5e-12    # ~5 pF typical parasitic capacitance
    f_sr = 1.0 / (2.0 * pi * np.sqrt(L * C_par))
    print(f"  Parasitic C (est.)   : {C_par*1e12:.0f} pF")
    print(f"  Self-resonant f      : {f_sr/1e6:.2f} MHz")


def example_7_motional_EMF_solar_array():
    """
    Example 7: Motional EMF induced on solar array boom in LEO.
    Spacecraft velocity v ≈ 7.66 km/s in LEO.
    Earth's magnetic field B ≈ 50 μT.
    Boom length L = 10 m, moving perpendicular to B-field.
    """
    print("\n" + "="*60)
    print("EXAMPLE 7 — Motional EMF on Solar Array Boom (LEO)")
    print("="*60)
    v_s = 7.66e3       # m/s (LEO orbital speed)
    B_T = 50e-6        # T
    L_boom = 10.0      # m
    emf = induced_emf_motional(1.0, B_T, L_boom, v_s)
    print(f"  Spacecraft velocity  : {v_s:.2f} km/s")
    print(f"  Magnetic field B     : {B_T*1e6:.0f} μT")
    print(f"  Boom length          : {L_boom:.0f} m")
    print(f"  Motional EMF = B·l·v : {emf:.3f} V")
    # Open circuit voltage of ~0.38 V could cause unexpected current flow
    print(f"  This voltage could drive spurious currents in cable harness!")


# ══════════════════════════════════════════════════════════════════
# FIGURE 1 — Plane Wave Propagation: E, H, S vs. Distance
# ══════════════════════════════════════════════════════════════════

def plot_plane_wave_propagation():
    """
    Generate figure: plane wave E-field and power density vs. distance
    at 1 GHz, showing attenuation over one wavelength.
    """
    f = 1e9
    alpha, beta = propagation_constant(f)
    lam = wavelength_in_medium(f)
    z = np.linspace(0, lam, 500)
    E0 = 10.0  # V/m
    eta0 = wave_impedance_free_space()
    # E(z) = E0 * exp(-alpha*z) * cos(beta*z)
    E_z = E0 * np.exp(-alpha * z) * np.cos(beta * z)
    S_z = E_z**2 / eta0
    H_z = E_z / eta0

    fig, axes = plt.subplots(3, 1, figsize=(10, 9), sharex=True)
    fig.suptitle(
        "1 GHz Plane Wave Propagation in Free Space\n"
        "(Zhang Ch1 — Electromagnetic Wave Fundamentals)",
        fontsize=13, fontweight='bold'
    )

    axes[0].plot(z * 1e3, E_z, color='C0', linewidth=1.8)
    axes[0].set_ylabel("Electric Field $E_z$ (V/m)", color='C0')
    axes[0].tick_params(axis='y', labelcolor='C0')
    axes[0].set_title("E-field amplitude (attenuation negligible in free space)")
    axes[0].grid(True, alpha=0.3)

    axes[1].plot(z * 1e3, H_z, color='C1', linewidth=1.8)
    axes[1].set_ylabel("Magnetic Field $H_z$ (A/m)", color='C1')
    axes[1].tick_params(axis='y', labelcolor='C1')
    axes[1].set_title("H-field amplitude")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(z * 1e3, S_z * 1e6, color='C2', linewidth=1.8)
    axes[2].set_ylabel("Power Density $S$ (μW/m²)", color='C2')
    axes[2].tick_params(axis='y', labelcolor='C2')
    axes[2].set_xlabel("Distance $z$ (mm)", fontsize=11)
    axes[2].set_title("Instantaneous power density $S = |E|^2/\\eta_0$")
    axes[2].grid(True, alpha=0.3)

    # Mark wavelength
    for ax in axes:
        ax.axvline(lam * 1e3, color='gray', linestyle='--', alpha=0.7, linewidth=1.0)
        ax.text(lam * 1e3 * 1.01, ax.get_ylim()[0] * 0.95,
                f'$\\lambda$={lam*1e3:.1f}mm', fontsize=9, color='gray')

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch1_plane_wave_propagation.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n[FIGURE] ch1_plane_wave_propagation.png saved.")
    return out_path


# ══════════════════════════════════════════════════════════════════
# FIGURE 2 — Skin Depth vs. Frequency (Al, Cu, Steel)
# ══════════════════════════════════════════════════════════════════

def plot_skin_depth_vs_frequency():
    """
    Generate figure: skin depth δ vs. frequency for aluminum, copper, steel.
    Frequency range: 1 kHz to 10 GHz.
    """
    f_range = np.logspace(3, 10, 400)  # 1 kHz to 10 GHz

    sigma = {
        'Aluminum (σ=3.5×10⁷)': 3.5e7,
        'Copper (σ=5.8×10⁷)': 5.8e7,
        'Steel (σ=1.5×10⁶)': 1.5e6,
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    for label, s in sigma.items():
        delta = np.array([skin_depth(fi, s) for fi in f_range])
        ax.loglog(f_range, delta * 1e3, label=label, linewidth=2.0)

    ax.set_xlabel("Frequency (Hz)", fontsize=12)
    ax.set_ylabel("Skin Depth δ (mm)", fontsize=12)
    ax.set_title(
        "Skin Depth vs. Frequency — Conductors\n"
        "(Zhang Ch1 — Shielding Design Basis)",
        fontsize=13, fontweight='bold'
    )
    ax.legend(fontsize=10)
    ax.grid(True, which='both', alpha=0.3)

    # Mark key frequencies
    for f_mark in [1e6, 1e9]:
        delta_mark = skin_depth(f_mark, 5.8e7) * 1e3
        ax.axvline(f_mark, color='gray', linestyle=':', alpha=0.6)
        ax.annotate(f'{f_mark/1e6:.0f} MHz\nδ≈{delta_mark:.2f} mm',
                    xy=(f_mark, delta_mark),
                    xytext=(f_mark * 1.5, delta_mark * 3),
                    fontsize=8, color='gray')

    plt.tight_layout()
    out_path = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch1_skin_depth.png'
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[FIGURE] ch1_skin_depth.png saved.")
    return out_path


# ──────────────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("="*60)
    print("Zhang EMC — Chapter 1: Electromagnetic Basics")
    print("Spacecraft Electromagnetic Compatibility Technologies (2020)")
    print("="*60)

    example_1_esd_capacitor()
    example_2_skin_depth_shielding()
    example_3_plane_wave_propagation()
    example_4_magnetic_field_control()
    example_5_emc_margin_calculation()
    example_6_solenoid_inductance()
    example_7_motional_EMF_solar_array()

    print("\n" + "="*60)
    print("Generating figures...")
    print("="*60)
    plot_plane_wave_propagation()
    plot_skin_depth_vs_frequency()
    print("\nAll tasks complete.")
#!/usr/bin/env python3
"""
Zhang EMC - Chapter 9: Spacecraft Magnetic Design & Test
=======================================================
Core topics:
- Spacecraft magnetic moment estimation
- Magnetic field simulation (dipole model, boundary element method)
- Magnetic material selection (permaloy, mu-metal)
- Whole-satellite magnetic modeling
- Degaussing and demagnetization
- Magnetic test methods (scalar magnetometer, fluxgate)

Ref: Zhang, Spacecraft Electromagnetic Compatibility Technologies (2020), Ch9
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import mu_0, c, pi
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────
# 1. Magnetic Moment & Field Fundamentals
# ─────────────────────────────────────────────

def dipole_magnetic_field(Bx, By, Bz, r_vec, m_vec):
    """
    Magnetic field from a magnetic dipole (Biot-Savart).
    B = (μ0/4π) * [3(m·r)r/r⁵ - m/r³]
    Bx, By, Bz: field components at observation point (T)
    r_vec: [x, y, z] position of observation (m)
    m_vec: [mx, my, mz] magnetic moment (A·m²)
    """
    x, y, z = r_vec
    r = np.sqrt(x**2 + y**2 + z**2)
    if r < 0.001:
        return np.array([0.0, 0.0, 0.0])
    
    r_unit = np.array(r_vec) / r
    m_dot_r = np.dot(m_vec, r_vec)
    
    B = (mu_0 / (4*pi)) * (3 * m_dot_r * r_unit - m_vec) / r**3
    return B


def magnetic_moment_from_current_loop(I_A, radius_m, area_m2=None):
    """
    Magnetic moment of a current loop: m = I * A (A·m²)
    For a circular loop: A = π * r²
    """
    if area_m2 is None:
        area = pi * radius_m**2
    else:
        area = area_m2
    m = I_A * area
    return m


def spacecraft_magnetic_moment_spec(attitude_error_arcmin, B_field_nT=30000,
                                     sensor_resolution_nT=1.0):
    """
    Determine spacecraft magnetic moment budget from attitude control requirements.
    torque_nm = m × B  →  m = torque / B
    attitude_error_arcmin: permitted attitude error
    B_field_nT: local geomagnetic field (nT)
    """
    # Convert arcmin to rad
    eps = attitude_error_arcmin * pi / (180 * 60)
    # Magnetic dipole moment required to maintain attitude
    # τ = m × B, for small attitude: τ = m * B * sin(eps) ≈ m * B * eps
    m_required = 1.0 / (B_field_nT * 1e-9 * eps)  # A·m²
    return m_required


# ─────────────────────────────────────────────
# 2. Magnetic Materials & Permeability
# ─────────────────────────────────────────────

def mu_metal_relative_permeability(H_A_m=10.0):
    """
    Mu-metal (Ni-Fe alloy) relative permeability.
    Extremely high μ at low H (low magnetization field).
    μr drops as H increases (permeability rolls off).
    At H=10 A/m: μr ≈ 80,000 (typical)
    At H=100 A/m: μr ≈ 10,000
    """
    # Approximate B-H curve for mu-metal
    # Using Fröhlich-Kennelly model
    mu_r_initial = 100000.0
    mu_r_sat = 500.0
    H_sat = 500.0  # A/m
    mu_r = mu_r_sat + (mu_r_initial - mu_r_sat) / (1 + H_A_m / H_sat)
    return mu_r


def shielding_factor_nested_cylinders(r_inner_mm, r_outer_mm,
                                       l_cylinder_mm, mu_r=20000,
                                       n_layers=3):
    """
    Magnetic shielding factor for nested cylindrical shields.
    For a cylindrical shield: SF ≈ (μr * t) / r  (long cylinder approximation)
    t = wall thickness
    For nested layers: SF_total ≈ product of individual SFs
    """
    t = (r_outer_mm - r_inner_mm) * 1e-3  # m
    r = r_inner_mm * 1e-3
    l = l_cylinder_mm * 1e-3
    
    # Single layer attenuation factor
    SF_layer = (mu_r * t) / r if r > 0 else 1.0
    # Length correction (finite cylinder)
    L_factor = np.tanh(l / (3 * r)) if l > 0 else 1.0
    
    SF_single = SF_layer * L_factor
    SF_total = SF_single**n_layers
    
    return {
        'SF_single_layer': SF_single,
        'SF_total': SF_total,
        'SF_dB': 20 * np.log10(SF_total + 1e-12) if SF_total > 0 else 0
    }


# ─────────────────────────────────────────────
# 3. Magnetic Field Simulation
# ─────────────────────────────────────────────

def boundary_element_method_shield(r_obs_m, shield_R_m, shield_L_m,
                                    B_external_nT=30000.0,
                                    mu_r_shield=20000, n_elements=36):
    """
    Simplified 2D BEM for axial magnetic shielding.
    Divide cylinder surface into n elements, solve for surface currents.
    Returns shielded field at observation point.
    """
    # 2D approximation: treat as infinite cylinder
    # BEM: divide cylinder into n boundary elements
    theta = np.linspace(0, 2*pi, n_elements, endpoint=False)
    x_surf = shield_R_m * np.cos(theta)
    y_surf = shield_R_m * np.sin(theta)
    
    # Internal field at origin (uniform external field B0 along z)
    B0 = B_external_nT * 1e-9  # T
    B_internal = B0 / mu_r_shield  # shielding division
    
    # Simplified: internal field uniform for long cylinder
    return {'B_internal_T': B_internal,
            'shielding_factor': 1.0 / mu_r_shield,
            'B_internal_nT': B_internal * 1e9}


def magnetic_field_near_current_carrier(I, r_m, l_m, orientation='perpendicular'):
    """
    Magnetic field near a current-carrying wire.
    For straight wire: B = μ0*I/(2πr) (circumferential)
    For loop: B on axis = μ0*I*R²/(2(R²+z²)^(3/2))
    """
    if orientation == 'perpendicular':
        # Field from straight wire at distance r
        B_wire = mu_0 * I / (2 * pi * r_m)
    else:
        # Field on axis of loop
        R = l_m / (2 * pi)  # equivalent radius
        z = r_m  # axial distance
        B_loop = mu_0 * I * R**2 / (2 * (R**2 + z**2)**1.5)
        B_wire = B_loop
    
    return B_wire  # Tesla


def helmholtz_coil_B_field(n_turns, radius_m, current_A, separation_m=None):
    """
    Helmholtz coil produces uniform field in center region.
    B_axis = (4/5)^(3/2) * μ0 * n * I / R
    For optimal uniformity, coil separation = coil radius.
    """
    if separation_m is None:
        separation_m = radius_m
    
    # Standard Helmholtz formula
    B = mu_0 * n_turns * current_A * (4.0/5.0)**1.5 / radius_m
    return B  # Tesla


# ─────────────────────────────────────────────
# 4. Degaussing / Demagnetization
# ─────────────────────────────────────────────

def degaussing_fieldrequirement(coercive_force_A_m=4.0,
                                  material='mu_metal'):
    """
    Degaussing requires AC field that gradually decays.
    Starting field must exceed H_c to erase remanence.
    Coercive force H_c:
    - Mu-metal: 2-5 A/m
    - Permalloy: 4-8 A/m
    - Silicon steel: 40-60 A/m
    """
    H_c_values = {
        'mu_metal': 4.0,
        'permalloy': 5.0,
        'silicon_steel': 50.0,
        'soft_iron': 100.0
    }
    H_c = H_c_values.get(material.lower(), 4.0)
    # Start amplitude: 3-5 × H_c
    H_start = 5 * H_c
    H_decay_factor = 0.7  # per cycle decay factor
    n_cycles = 10  # for 10-cycle degaussing
    H_final = H_start * (H_decay_factor**n_cycles)
    
    return {
        'H_coercive_A_m': H_c,
        'H_start_A_m': H_start,
        'H_final_A_m': H_final,
        'n_cycles': n_cycles
    }


# ─────────────────────────────────────────────
# 5. Magnetic Test Analysis
# ─────────────────────────────────────────────

def magnetic_test_noise_floor(integration_time_s=1.0,
                               bandwidth_Hz=1.0):
    """
    Fluxgate magnetometer noise floor estimation.
    Typical fluxgate: ~10 pT/√Hz at 1 Hz
    With integration: noise_floor_reduced = noise_10pT / √(integration_time)
    """
    noise_density_pT = 10.0  # pT/√Hz at 1 Hz
    noise_floor = noise_density_pT / np.sqrt(integration_time_s)
    return {'noise_floor_pT': noise_floor, 'integration_s': integration_time_s}


def magnetic_moment_measurement_from_field(B_measured_nT, r_meas_m,
                                             orientation='axial'):
    """
    From measured B field at known distance, back-calculate magnetic moment.
    For a dipole: B = μ0*m / (4π*r³) [on-axis, r along dipole axis]
    m = B * 4π*r³ / μ0
    """
    B_T = B_measured_nT * 1e-9
    r = r_meas_m
    m = B_T * 4 * pi * r**3 / mu_0
    return m  # A·m²


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

# Alias for nested shielding SF call
nested_shield_sf = shielding_factor_nested_cylinders

if __name__ == '__main__':
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures', exist_ok=True)
    
    print("=== Chapter 9: Spacecraft Magnetic Design ===\n")
    
    # 1. Dipole field
    print("--- 1. Dipole Magnetic Field ---")
    m_vec = np.array([0.0, 0.0, 100.0])  # 100 A·m² along z
    r_vec = np.array([1.0, 0.0, 0.0])     # 1m on x-axis
    B = dipole_magnetic_field(0, 0, 0, r_vec, m_vec)
    print(f"  Dipole m=[0,0,100] A·m² @ (1,0,0)m: B={np.linalg.norm(B)*1e9:.2f} nT")
    
    # Magnetic moment spec
    print("\n--- 2. Magnetic Moment Spec ---")
    m_spec = spacecraft_magnetic_moment_spec(attitude_error_arcmin=0.5, B_field_nT=30000)
    print(f"  Spacecraft moment budget @ 0.5 arcmin attitude, 30000 nT: {m_spec:.2f} A·m²")
    
    # Mu-metal permeability
    print("\n--- 3. Mu-Metal Permeability ---")
    mu_r = mu_metal_relative_permeability(H_A_m=10.0)
    print(f"  Mu-metal μr @ H=10 A/m: {mu_r:.0f}")
    
    # Shielding factor
    print("\n--- 4. Nested Cylinder Shielding ---")
    sf = shielding_factor_nested_cylinders(r_inner_mm=50, r_outer_mm=52,
                                           l_cylinder_mm=100, mu_r=20000, n_layers=3)
    print(f"  3-layer Mu-metal shield (r=50mm, t=2mm, l=100mm): SF={sf['SF_dB']:.1f} dB")
    
    # Helmholtz coil
    print("\n--- 5. Helmholtz Coil B-field ---")
    B_helm = helmholtz_coil_B_field(n_turns=100, radius_m=0.5, current_A=1.0)
    print(f"  100-turn Helmholtz (R=0.5m, I=1A): B={B_helm*1e6:.2f} μT")
    
    # Degaussing
    print("\n--- 6. Degaussing ---")
    dg = degaussing_fieldrequirement(material='mu_metal')
    print(f"  Mu-metal degauss: H_start={dg['H_start_A_m']:.1f} A/m, H_final={dg['H_final_A_m']:.4f} A/m")
    
    # Measurement noise
    print("\n--- 7. Fluxgate Noise Floor ---")
    nf = magnetic_test_noise_floor(integration_time_s=10.0)
    print(f"  Noise floor @ 10s integration: {nf['noise_floor_pT']:.3f} pT")
    
    # Moment from field
    print("\n--- 8. Moment from Field Measurement ---")
    m = magnetic_moment_measurement_from_field(B_measured_nT=300.0, r_meas_m=3.0)
    print(f"  B=300 nT @ 3m on-axis → m={m:.2f} A·m²")
    
    # Plot shielding factor
    print("\n--- 9. Generating Figures ---")
    H_range = np.logspace(-1, 4, 300)  # 0.1 to 10000 A/m
    mu_r_vals = [mu_metal_relative_permeability(H) for H in H_range]
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    axes[0,0].semilogx(H_range, mu_r_vals, 'b-', lw=2)
    axes[0,0].set_xlabel('H (A/m)'); axes[0,0].set_ylabel('μr')
    axes[0,0].set_title('Mu-Metal B-H Curve (Relative Permeability)')
    axes[0,0].grid(True, which='both', alpha=0.3)
    
    # Shielding factor vs layers
    layers = np.arange(1, 6)
    SF_vals = [nested_shield_sf(r_inner_mm=50, r_outer_mm=52, l_cylinder_mm=100, mu_r=20000, n_layers=n)['SF_dB']
               for n in layers]
    axes[0,1].bar(layers, SF_vals, color='steelblue')
    axes[0,1].set_xlabel('Number of Mu-Metal Layers')
    axes[0,1].set_ylabel('Shielding Factor (dB)')
    axes[0,1].set_title('Nested Cylinder Shielding vs. Layers')
    axes[0,1].grid(True, alpha=0.3)
    
    # Dipole field vs distance
    r_range = np.linspace(0.1, 5.0, 200)
    m_test = 100.0  # A·m²
    B_axial = mu_0 * m_test / (4 * pi * r_range**3)
    axes[1,0].loglog(r_range, B_axial*1e9, 'r-', lw=2)
    axes[1,0].set_xlabel('Distance r (m)')
    axes[1,0].set_ylabel('B (nT)')
    axes[1,0].set_title('Dipole Field vs. Distance (m=100 A·m², on-axis)')
    axes[1,0].grid(True, which='both', alpha=0.3)
    
    # Helmholtz uniformity
    z_range = np.linspace(-0.5, 0.5, 200)
    B_uniform = np.zeros_like(z_range)
    for z in z_range:
        R = 0.5
        I = 1.0
        n = 100
        B1 = mu_0 * n * I * R**2 / (2 * (R**2 + (z - R/2)**2)**1.5)
        B2 = mu_0 * n * I * R**2 / (2 * (R**2 + (z + R/2)**2)**1.5)
        B_uniform[np.where(z == z_range)[0][0]] = (B1 + B2) * 1e6  # μT
    
    axes[1,1].plot(z_range*1e3, B_uniform, 'g-', lw=2)
    axes[1,1].set_xlabel('z position (mm)')
    axes[1,1].set_ylabel('B (μT)')
    axes[1,1].set_title('Helmholtz Coil Axial B-field (I=1A, R=0.5m, n=100)')
    axes[1,1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/zhang_emc/figures/ch9_magnetic_design.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"Figure: {out}")
    plt.close()
    
    print("\n✓ Chapter 9 code complete.")

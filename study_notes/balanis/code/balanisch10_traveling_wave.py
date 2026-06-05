"""
balanis ch10 - traveling wave and broadband antennas

Covers:
  1. Long wire: traveling wave vs standing wave radiation patterns
  2. V-antenna: pattern synthesis for various tilt angles
  3. Rhombic antenna: free-space radiation pattern
  4. Helical antenna: axial mode design parameters
  5. Helical antenna: frequency sweep (HPBW, gain, input impedance)

Author: Xiaolongxia (subagent)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from typing import Tuple, Optional
import os

# === Constants ===
C0 = 3e8            # speed of light (m/s)
ETA_0 = 120 * np.pi  # free-space impedance (Ohm)
PI = np.pi
FIG_DIR = 'figures/ch10'
os.makedirs(FIG_DIR, exist_ok=True)


# =========================================================================
# 1. Long Wire Traveling Wave Pattern
# =========================================================================

def traveling_wire_pattern(theta: np.ndarray, kL: float) -> np.ndarray:
    """Normalized radiation pattern of a traveling-wave wire.
    
    F(theta) = sin(theta) * sin[kL*(1-cos(theta))/2] / [kL*(1-cos(theta))/2]
    
    Args:
        theta: polar angle array (radians), 0 = wire axis direction
        kL: electrical length (radians), kL = 2*pi*L/lambda
    
    Returns:
        Normalized field pattern magnitude |F(theta)|
    """
    psi = kL * (1.0 - np.cos(theta)) / 2.0
    # element factor
    element = np.sin(theta)
    # array factor (sinc-like)
    array = np.ones_like(psi)
    valid = np.abs(psi) > 1e-12
    array[valid] = np.sin(psi[valid]) / psi[valid]
    array[~valid] = 1.0
    return np.abs(element * array)


def standing_wire_pattern(theta: np.ndarray, kL: float) -> np.ndarray:
    """Normalized radiation pattern of a standing-wave (open-ended) wire.
    
    For a wire of length L along z-axis, current I(z) = I0 * sin(k*(L-z)):
    F(theta) = [cos(kL*cos(theta)) - cos(kL)] / sin(theta)
    
    Args:
        theta: polar angle array (radians)
        kL: electrical length (radians)
    
    Returns:
        Normalized field pattern magnitude |F(theta)|
    """
    numerator = np.cos(kL * np.cos(theta)) - np.cos(kL)
    denom = np.sin(theta)
    pattern = np.abs(numerator / denom)
    return pattern


def example_1_long_wire_pattern():
    """Example 1: Long wire pattern -- traveling wave vs standing wave."""
    print("=" * 65)
    print("  Example 1: Long Wire Pattern -- Traveling vs Standing Wave")
    print("=" * 65)

    f = 300e6  # 300 MHz
    lam = C0 / f
    L_by_lambda_vals = [1, 3, 5, 8]
    theta = np.linspace(0.001, PI - 0.001, 3601)  # avoid singularities
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8),
                              subplot_kw={'projection': 'polar'})
    
    for idx, L_ratio in enumerate(L_by_lambda_vals):
        kL = 2 * PI * L_ratio
        
        # Traveling wave
        F_trav = traveling_wire_pattern(theta, kL)
        F_trav_norm = F_trav / np.max(F_trav)
        
        # Standing wave
        F_std = standing_wire_pattern(theta, kL)
        F_std_norm = F_std / np.max(F_std)
        
        # Main lobe angle for traveling wave
        idx_max = np.argmax(F_trav)
        theta_max_deg = np.degrees(theta[idx_max])
        
        # Top row: traveling wave
        ax_t = axes[0, idx]
        ax_t.plot(theta, F_trav_norm, 'b-', lw=1.5)
        ax_t.set_thetamin(0)
        ax_t.set_thetamax(180)
        ax_t.set_title(f"Traveling L={L_ratio}lambda\n"
                       f"peak={theta_max_deg:.0f}deg", fontsize=10)
        ax_t.set_ylim(0, 1.0)
        
        # Bottom row: standing wave
        ax_s = axes[1, idx]
        ax_s.plot(theta, F_std_norm, 'r-', lw=1.5)
        ax_s.set_thetamin(0)
        ax_s.set_thetamax(180)
        ax_s.set_title(f"Standing L={L_ratio}lambda", fontsize=10)
        ax_s.set_ylim(0, 1.0)
        
        print(f"  L={L_ratio}*lambda: traveling peak = {theta_max_deg:.1f} deg")
    
    axes[0, 0].text(-0.4, 0.5, 'Traveling Wave',
                    transform=axes[0, 0].transAxes, rotation=90,
                    va='center', fontsize=13, fontweight='bold')
    axes[1, 0].text(-0.4, 0.5, 'Standing Wave',
                    transform=axes[1, 0].transAxes, rotation=90,
                    va='center', fontsize=13, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch10_ex1_long_wire_pattern.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch10_ex1_long_wire_pattern.png")


# =========================================================================
# 2. V-Antenna Pattern
# =========================================================================

def v_antenna_pattern(theta: np.ndarray, phi: np.ndarray,
                       kL: float, half_angle_deg: float,
                       plane: str = 'phi') -> np.ndarray:
    """Normalized radiation pattern of a V-antenna.
    
    The V-antenna has two arms at angles +psi and -psi from the z-axis.
    For the pattern cut at the plane bisecting the V (phi=0 plane),
    we compute the superposition of two traveling-wave wire patterns.
    
    Args:
        theta: polar angle (radians)
        phi: azimuth angle (radians)
        kL: electrical length of each arm
        half_angle_deg: half-angle psi of the V (deg)
        plane: 'phi' for phi=0 cut (plane containing both arms)
    
    Returns:
        Normalized field pattern magnitude
    """
    psi = np.radians(half_angle_deg)
    
    # Unit vectors along each arm (in the phi=0 plane)
    # Arm 1: at +psi from z-axis
    # Arm 2: at -psi from z-axis
    # The angle theta_i between observation (theta, phi) and arm direction
    if plane == 'phi':
        # For phi=0 cut (plane containing the V):
        # theta_1 = |theta - psi|
        # theta_2 = |theta + psi|  (or 2*PI - (theta + psi))
        theta_1 = np.abs(theta - psi)
        theta_2 = np.abs(theta + psi)
        # Handle wrap-around for theta_2 > PI
        theta_2 = np.minimum(theta_2, 2 * PI - theta_2)
    else:
        # For phi=90 cut (perpendicular plane):
        # Both arms symmetric: theta_1 = theta_2 = theta
        theta_1 = theta
        theta_2 = theta
    
    # Traveling-wave pattern for each arm
    F1 = traveling_wire_pattern(theta_1, kL)
    F2 = traveling_wire_pattern(theta_2, kL)
    
    # Superposition (coherent sum, phase approximately accounted)
    # For forward direction in the bisecting plane, the two patterns add
    pattern = np.sqrt(F1**2 + F2**2 + 2 * F1 * F2 * np.cos(psi * np.ones_like(theta)))
    # Simplified: just sum magnitudes for power pattern estimate
    pattern = np.abs(F1 + F2)
    
    return pattern / np.max(pattern)


def example_2_v_antenna():
    """Example 2: V-antenna pattern for various half-angles."""
    print("\n" + "=" * 65)
    print("  Example 2: V-Antenna Pattern Synthesis")
    print("=" * 65)
    
    f = 300e6
    lam = C0 / f
    L = 3 * lam  # 3 wavelength arms
    kL = 2 * PI * L / lam
    theta = np.linspace(0.01, PI - 0.01, 1801)
    
    half_angles = [20, 30, 40, 50, 60, 70]
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 9),
                              subplot_kw={'projection': 'polar'})
    
    for idx, psi in enumerate(half_angles):
        row = idx // 3
        col = idx % 3
        pattern = v_antenna_pattern(theta, np.zeros_like(theta), kL, psi, 'phi')
        
        ax = axes[row, col]
        ax.plot(theta, pattern, 'b-', lw=1.5)
        ax.set_thetamin(0)
        ax.set_thetamax(180)
        
        # Compute main lobe direction
        idx_max = np.argmax(pattern)
        theta_max = np.degrees(theta[idx_max])
        
        ax.set_title(f"psi={psi}deg, peak={theta_max:.0f}deg", fontsize=10)
        ax.set_ylim(0, 1.0)
        
        print(f"  psi={psi:2d} deg: main lobe at {theta_max:.0f} deg")
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch10_ex2_v_antenna.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch10_ex2_v_antenna.png")


# =========================================================================
# 3. Rhombic Antenna Pattern
# =========================================================================

def rhombic_pattern_phi90(theta: np.ndarray, kL: float,
                           phi_deg: float) -> np.ndarray:
    """Rhombic antenna pattern in the phi=90 (vertical) plane.
    
    The rhombic lies in the horizontal plane (theta=90 deg in standard
    spherical coordinates). In the plane perpendicular to its long axis,
    we model the four segments as two pairs of oppositely-directed
    traveling-wave wires.
    
    Args:
        theta: polar angle (radians), 0 = zenith
        kL: electrical length of one side
        phi_deg: rhombic half-angle (deg)
    
    Returns:
        Normalized pattern magnitude
    """
    phi = np.radians(phi_deg)
    
    # Segments 1,3: wires at angle phi from horizontal
    # Segments 2,4: wires at angle -phi from horizontal
    # In vertical plane cut (phi=90), the angles between observation
    # and each segment depend on theta and phi
    
    # For the segments tilted at +phi from the x-axis (in horizontal plane):
    # The direction cosines are the projection of unit vectors
    
    # Simplified model: four sources with appropriate phase centers
    # Each segment contributes a traveling-wave factor
    
    # Segment along +phi direction: observation angle from wire axis
    # cos(theta_wire) = sin(theta) * cos(phi - phi_wire)
    # For phi=90 cut and phi_wire = phi0:
    # cos(theta_wire) = sin(theta) * sin(phi0)
    
    theta_w1 = np.arccos(np.sin(theta) * np.sin(phi))
    theta_w2 = np.arccos(-np.sin(theta) * np.sin(phi))
    
    F1 = traveling_wire_pattern(theta_w1, kL)
    F2 = traveling_wire_pattern(theta_w2, kL)
    
    # Phase center offsets (half the rhombic at y = +- L*sin(phi)/2)
    # Phase difference: ky * sin(theta) where y = L*sin(phi)/2
    ky_offset = kL * np.sin(phi) / 2.0 * np.sin(theta)
    
    # Coherent sum of four segments
    # Seg 1: arm AB (direction +phi), phase center at +L*sin(phi)/2
    # Seg 2: arm BC (direction -phi), phase center at +L*sin(phi)/2
    # Seg 3: arm CD (direction -phi), phase center at -L*sin(phi)/2
    # Seg 4: arm DA (direction +phi), phase center at -L*sin(phi)/2
    
    # For the two segments pointing toward +phi:
    E_plus = F1 * np.exp(1j * ky_offset)
    
    # For the two segments pointing toward -phi:
    E_minus = F2 * np.exp(-1j * ky_offset)
    
    # Also account for remaining two segments at opposite phase centers
    E_plus2 = F1 * np.exp(-1j * ky_offset)
    E_minus2 = F2 * np.exp(1j * ky_offset)
    
    # At the terminating point, there may be a small portion of
    # residual reflection, but we assume perfect match for simplicity
    
    E_total = E_plus + E_minus + E_plus2 + E_minus2
    pattern = np.abs(E_total)
    
    return pattern / np.max(pattern)


def example_3_rhombic():
    """Example 3: Rhombic antenna radiation pattern."""
    print("\n" + "=" * 65)
    print("  Example 3: Rhombic Antenna Pattern")
    print("=" * 65)
    
    f = 300e6
    lam = C0 / f
    L = 3 * lam
    kL = 2 * PI * L / lam
    theta = np.linspace(0.01, PI - 0.01, 1801)
    
    phi_vals = [15, 25, 35]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5),
                              subplot_kw={'projection': 'polar'})
    
    for idx, phi_d in enumerate(phi_vals):
        pattern = rhombic_pattern_phi90(theta, kL, phi_d)
        
        ax = axes[idx]
        ax.plot(theta, pattern, 'b-', lw=1.5)
        ax.set_thetamin(0)
        ax.set_thetamax(180)
        
        # Find main lobe
        idx_max = np.argmax(pattern)
        theta_max = np.degrees(theta[idx_max])
        
        # HPBW
        half_power = 1.0 / np.sqrt(2)
        above_hp = pattern >= half_power
        # Find width of main lobe
        if np.any(above_hp):
            hp_indices = np.where(above_hp)[0]
            # Find continuous region around max
            center = np.argmax(pattern)
            left = np.searchsorted(hp_indices, center)
            hp_start = hp_indices[0]
            hp_end = hp_indices[-1]
            # Narrow down to region around the main lobe
            for i in range(hp_indices[0], center):
                if not above_hp[i]:
                    hp_start = i + 1
            for i in range(center, hp_indices[-1]):
                if not above_hp[i]:
                    hp_end = i
                    break
            hpbw = np.degrees(np.abs(theta[hp_end] - theta[hp_start]))
        else:
            hpbw = float('nan')
        
        ax.set_title(f"phi={phi_d}deg, peak={theta_max:.0f}deg\n"
                     f"HPBW={hpbw:.1f}deg", fontsize=10)
        ax.set_ylim(0, 1.0)
        
        print(f"  phi={phi_d:2d} deg: main lobe at {theta_max:.0f} deg, "
              f"HPBW={hpbw:.1f} deg")
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch10_ex3_rhombic.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch10_ex3_rhombic.png")


# =========================================================================
# 4. Helical Antenna Axial Mode Design
# =========================================================================

class HelicalAntenna:
    """Helical antenna in axial mode (Balanis Ch10.3)."""
    
    def __init__(self, C_over_lambda: float = 1.05,
                 alpha_deg: float = 14.0, N_turns: int = 10,
                 f0: float = 500e6):
        """Initialize helical antenna design.
        
        Args:
            C_over_lambda: circumference / wavelength ratio
            alpha_deg: pitch angle (degrees)
            N_turns: number of turns
            f0: center frequency (Hz)
        """
        self.C_over_lambda = C_over_lambda
        self.alpha = np.radians(alpha_deg)
        self.N = N_turns
        self.f0 = f0
        self.lam0 = C0 / f0
        
        # Derived parameters
        self.C = C_over_lambda * self.lam0  # circumference (m)
        self.D = self.C / PI                 # diameter (m)
        self.S = self.C * np.tan(self.alpha) # spacing (m)
        self.L_total = self.N * self.S       # total axial length (m)
        self.L_wire = self.N * np.sqrt(self.C**2 + self.S**2)  # wire length
    
    def hpbw(self, C_over_lambda: Optional[float] = None) -> float:
        """Half-power beamwidth in degrees."""
        C_ratio = C_over_lambda if C_over_lambda is not None else self.C_over_lambda
        return 52.0 / (C_ratio * np.sqrt(self.N * self.S / self.lam0))
    
    def directivity_dBi(self, C_over_lambda: Optional[float] = None) -> float:
        """Directivity in dBi."""
        C_ratio = C_over_lambda if C_over_lambda is not None else self.C_over_lambda
        D_lin = 12.0 * C_ratio**2 * self.N * self.S / self.lam0
        return 10 * np.log10(D_lin)
    
    def input_resistance(self, C_over_lambda: Optional[float] = None) -> float:
        """Input resistance in Ohms (axial mode, approximately resistive)."""
        C_ratio = C_over_lambda if C_over_lambda is not None else self.C_over_lambda
        return 140.0 * C_ratio
    
    def axial_ratio(self) -> float:
        """Axial ratio (linear), AR = (2N+1)/(2N)."""
        return (2 * self.N + 1) / (2 * self.N)
    
    def axial_ratio_dB(self) -> float:
        """Axial ratio in dB."""
        AR_lin = self.axial_ratio()
        return 20 * np.log10(AR_lin)
    
    def summary(self) -> str:
        """Print a design summary."""
        lines = []
        lines.append(f"  Center frequency:      {self.f0/1e6:.0f} MHz")
        lines.append(f"  Wavelength:            {self.lam0:.3f} m")
        lines.append(f"  Circumference:         {self.C:.3f} m  (C/lambda={self.C_over_lambda:.2f})")
        lines.append(f"  Diameter:              {self.D:.3f} m")
        lines.append(f"  Spacing:               {self.S:.3f} m  (S/lambda={self.S/self.lam0:.3f})")
        lines.append(f"  Pitch angle:           {np.degrees(self.alpha):.1f} deg")
        lines.append(f"  Turns:                 {self.N}")
        lines.append(f"  Total axial length:    {self.L_total:.3f} m  (L/lambda={self.L_total/self.lam0:.2f})")
        lines.append(f"  HPBW:                  {self.hpbw():.1f} deg")
        lines.append(f"  Directivity:           {self.directivity_dBi():.2f} dBi")
        lines.append(f"  Input resistance:      {self.input_resistance():.0f} Ohm")
        lines.append(f"  Axial ratio:           {self.axial_ratio():.4f}  ({self.axial_ratio_dB():.2f} dB)")
        return '\n'.join(lines)


def example_4_helical_axial():
    """Example 4: Helical antenna axial mode design (Balanis Ex 10.1)."""
    print("\n" + "=" * 65)
    print("  Example 4: Helical Antenna - Axial Mode Design")
    print("  (Balanis Example 10.1)")
    print("=" * 65)
    
    # Design at 500 MHz
    helix = HelicalAntenna(C_over_lambda=1.05, alpha_deg=14.0,
                           N_turns=10, f0=500e6)
    print(helix.summary())
    
    # === Plot: Normalized pattern ===
    # Approximate pattern: cos(theta)^n where n relates to HPBW
    hpbw_rad = np.radians(helix.hpbw())
    # n such that cos(hpbw_rad/2)^n = 1/sqrt(2)
    n = np.log(1.0 / np.sqrt(2)) / np.log(np.cos(hpbw_rad / 2))
    
    theta = np.linspace(0, PI, 1801)
    F_cos = np.abs(np.cos(theta)) ** n
    # Only valid for |theta| < PI/2 (forward hemisphere)
    F_cos[theta > PI/2] = 0.0
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Polar plot
    ax_polar = axes[0]
    ax_polar = plt.subplot(121, projection='polar')
    ax_polar.plot(theta, F_cos / np.max(F_cos), 'b-', lw=2)
    ax_polar.set_thetamin(0)
    ax_polar.set_thetamax(180)
    ax_polar.set_title(f"Axial Mode Helix\nN={helix.N}, C/lambda={helix.C_over_lambda:.2f}\n"
                       f"HPBW={helix.hpbw():.1f}deg, D={helix.directivity_dBi():.1f}dBi",
                       fontsize=11, va='bottom')
    ax_polar.set_ylim(0, 1.0)
    
    # Cartesian pattern
    ax_cart = axes[1]
    ax_cart.plot(np.degrees(theta), F_cos / np.max(F_cos), 'b-', lw=2)
    ax_cart.axhline(y=1/np.sqrt(2), color='r', ls='--', alpha=0.5,
                    label=f'HPBW={helix.hpbw():.0f}deg')
    ax_cart.set_xlabel('Theta [deg]', fontsize=13)
    ax_cart.set_ylabel('Normalized Pattern', fontsize=13)
    ax_cart.set_title('Axial Mode Helix - Cartesian', fontsize=14)
    ax_cart.set_xlim(0, 90)
    ax_cart.grid(True, alpha=0.3)
    ax_cart.legend(fontsize=10)
    
    # Add text box with design parameters
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.8)
    textstr = (f"D = {helix.D:.2f} m\n"
               f"S = {helix.S:.3f} m\n"
               f"N = {helix.N} turns\n"
               f"R_in = {helix.input_resistance():.0f} Ohm\n"
               f"AR = {helix.axial_ratio_dB():.2f} dB")
    ax_cart.text(0.95, 0.95, textstr, transform=ax_cart.transAxes,
                 fontsize=10, verticalalignment='top',
                 horizontalalignment='right', bbox=props)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch10_ex4_helical_axial.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch10_ex4_helical_axial.png")


# =========================================================================
# 5. Helical Antenna Frequency Sweep
# =========================================================================

def example_5_helical_freq_sweep():
    """Example 5: Helical antenna frequency sweep (HPBW, Gain, Zin)."""
    print("\n" + "=" * 65)
    print("  Example 5: Helical Antenna Frequency Characteristics")
    print("=" * 65)
    
    # Reference design at center frequency
    f0 = 500e6
    N = 10
    S = 0.157  # m (from Ex 10.1)
    D = 0.200  # m (from Ex 10.1)
    
    # Frequency sweep from 350 to 650 MHz
    f_vals = np.linspace(350e6, 650e6, 101)
    f_ratio = f_vals / f0
    lam_vals = C0 / f_vals
    C_over_lambda_vals = PI * D / lam_vals
    
    # Only valid for axial mode: 0.75 < C/lambda < 1.33
    valid = (C_over_lambda_vals >= 0.75) & (C_over_lambda_vals <= 1.33)
    f_in_band = f_vals[valid]
    C_ratio_in = C_over_lambda_vals[valid]
    
    # HPBW
    hpbw_vals = 52.0 / (C_ratio_in * np.sqrt(N * S / lam_vals[valid]))
    
    # Directivity (linear)
    D_lin = 12.0 * C_ratio_in**2 * N * S / lam_vals[valid]
    D_dBi = 10 * np.log10(D_lin)
    
    # Input resistance
    R_in = 140.0 * C_ratio_in
    
    # Axial ratio
    AR_lin = (2 * N + 1) / (2 * N)
    AR_dB = 20 * np.log10(AR_lin)
    
    print(f"  Frequency range: {f_in_band[0]/1e6:.0f} - {f_in_band[-1]/1e6:.0f} MHz")
    print(f"  C/lambda range:  {C_ratio_in[0]:.3f} - {C_ratio_in[-1]:.3f}")
    print(f"  HPBW range:      {hpbw_vals[-1]:.1f} - {hpbw_vals[0]:.1f} deg")
    print(f"  Gain range:      {D_dBi[0]:.1f} - {D_dBi[-1]:.1f} dBi")
    print(f"  R_in range:      {R_in[0]:.0f} - {R_in[-1]:.0f} Ohm")
    print(f"  Axial ratio:     {AR_dB:.2f} dB (constant)")
    
    # Plot
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # (a) HPBW
    axes[0, 0].plot(f_in_band / 1e6, hpbw_vals, 'b-', lw=2)
    axes[0, 0].set_xlabel('Frequency [MHz]', fontsize=13)
    axes[0, 0].set_ylabel('HPBW [deg]', fontsize=13)
    axes[0, 0].set_title('Half-Power Beamwidth vs Frequency', fontsize=14)
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].axvline(x=f0/1e6, color='r', ls='--', alpha=0.5, label='f0=500 MHz')
    axes[0, 0].legend(fontsize=10)
    
    # (b) Directivity
    axes[0, 1].plot(f_in_band / 1e6, D_dBi, 'r-', lw=2)
    axes[0, 1].set_xlabel('Frequency [MHz]', fontsize=13)
    axes[0, 1].set_ylabel('Directivity [dBi]', fontsize=13)
    axes[0, 1].set_title('Directivity vs Frequency', fontsize=14)
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].axvline(x=f0/1e6, color='r', ls='--', alpha=0.5, label='f0=500 MHz')
    axes[0, 1].legend(fontsize=10)
    
    # (c) Input Resistance
    axes[1, 0].plot(f_in_band / 1e6, R_in, 'g-', lw=2)
    axes[1, 0].set_xlabel('Frequency [MHz]', fontsize=13)
    axes[1, 0].set_ylabel('R_in [Ohm]', fontsize=13)
    axes[1, 0].set_title('Input Resistance vs Frequency', fontsize=14)
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].axvline(x=f0/1e6, color='r', ls='--', alpha=0.5, label='f0=500 MHz')
    axes[1, 0].legend(fontsize=10)
    
    # (d) C/lambda ratio (showing operating range)
    axes[1, 1].plot(f_vals / 1e6, C_over_lambda_vals, 'm-', lw=2)
    axes[1, 1].axhspan(0.75, 1.33, alpha=0.2, color='green',
                        label='Axial mode range')
    axes[1, 1].axhline(y=1.0, color='k', ls=':', alpha=0.3, label='C= lambda')
    axes[1, 1].axhline(y=0.75, color='gray', ls='--', alpha=0.5)
    axes[1, 1].axhline(y=1.33, color='gray', ls='--', alpha=0.5)
    axes[1, 1].set_xlabel('Frequency [MHz]', fontsize=13)
    axes[1, 1].set_ylabel('C / lambda', fontsize=13)
    axes[1, 1].set_title('Circumference / Wavelength Ratio', fontsize=14)
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/ch10_ex5_helical_freq_sweep.png', dpi=150)
    plt.close()
    print(f"  -> {FIG_DIR}/ch10_ex5_helical_freq_sweep.png")


# =========================================================================
# Main
# =========================================================================

def main():
    print("=" * 65)
    print("  Balanis Ch10: Traveling Wave and Broadband Antennas")
    print("=" * 65)
    
    # Example 1: Long wire pattern
    example_1_long_wire_pattern()
    
    # Example 2: V-antenna
    example_2_v_antenna()
    
    # Example 3: Rhombic antenna
    example_3_rhombic()
    
    # Example 4: Helical antenna axial mode
    example_4_helical_axial()
    
    # Example 5: Helical frequency sweep
    example_5_helical_freq_sweep()
    
    print("\n" + "=" * 65)
    print("  Ch10 examples complete.")
    print(f"  Figures saved to: {FIG_DIR}/")
    print("=" * 65)
    
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main())

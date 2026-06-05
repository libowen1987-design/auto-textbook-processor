#!/usr/bin/env python3
"""
Pozar Ch14 (4e Ch11) — Active RF Devices
==============================================
Comprehensive example code covering:
  11.1 Microwave Diodes (Schottky, PIN, Varactor, Tunnel, Gunn, IMPATT)
  11.2 Bipolar Junction Transistors (hybrid-pi model, f_T, f_max, S-params)
  11.3 Field Effect Transistors (MESFET/HEMT small-signal model, f_T, f_max)
  11.4 Microwave Integrated Circuits (transmission line comparison)

All variables follow physical-meaning naming conventions (e.g., C_j0, V_bi, f_T, g_m).
Figures saved to: figures/ch14/
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional
import os
from scipy import constants

# ---------- Physical Constants ----------
C0: float = constants.c                     # Speed of light [m/s]
K_B: float = constants.k                     # Boltzmann constant [J/K]
Q_E: float = constants.e                     # Electron charge [C]
EPSILON_0: float = constants.epsilon_0       # Vacuum permittivity [F/m]
T0: float = 290.0                            # Standard temperature [K]
V_T: float = K_B * T0 / Q_E                  # Thermal voltage ~0.025 V

# Output directory
FIG_DIR = os.path.join(os.path.dirname(__file__), "figures", "ch14")
os.makedirs(FIG_DIR, exist_ok=True)

# ============================================================
# §11.1 — MICROWAVE DIODES
# ============================================================

def schottky_iv_current(V_d: np.ndarray, I_S: float, eta: float = 1.08,
                        T: float = T0) -> np.ndarray:
    """
    Schottky diode I-V characteristic.

    I(V) = I_S * (exp(qV / eta kT) - 1)

    Parameters
    ----------
    V_d : np.ndarray
        Diode voltage [V].
    I_S : float
        Saturation current [A].
    eta : float
        Ideality factor (typically 1.02-1.10).
    T : float
        Temperature [K].

    Returns
    -------
    I_d : np.ndarray
        Diode current [A].
    """
    return I_S * (np.exp(Q_E * V_d / (eta * K_B * T)) - 1.0)


def schottky_junction_capacitance(V_R: float, C_j0: float, V_bi: float,
                                  gamma: float = 0.5) -> float:
    """
    Schottky junction capacitance under reverse bias.

    C_j(V) = C_j0 / (1 - V/V_bi)^gamma

    Parameters
    ----------
    V_R : float
        Reverse bias voltage [V] (positive magnitude).
    C_j0 : float
        Zero-bias junction capacitance [F].
    V_bi : float
        Built-in potential [V].
    gamma : float
        Grading coefficient (0.5 for abrupt, 0.33 for linearly graded).

    Returns
    -------
    C_j : float
        Junction capacitance [F].
    """
    return C_j0 / (1.0 + V_R / V_bi) ** gamma


def schottky_cutoff_frequency(R_s: float, C_j0: float) -> float:
    """
    Schottky diode cutoff frequency.

    f_c = 1 / (2 * pi * R_s * C_j0)

    Parameters
    ----------
    R_s : float
        Series resistance [Ohm].
    C_j0 : float
        Zero-bias junction capacitance [F].

    Returns
    -------
    f_c : float
        Cutoff frequency [Hz].
    """
    return 1.0 / (2.0 * np.pi * R_s * C_j0)


def schottky_junction_resistance(I_d: float, eta: float = 1.08,
                                 T: float = T0) -> float:
    """
    Small-signal junction resistance of a Schottky diode.

    R_j = eta * k * T / (q * I_d)

    Parameters
    ----------
    I_d : float
        Forward bias current [A].
    eta : float
        Ideality factor.
    T : float
        Temperature [K].

    Returns
    -------
    R_j : float
        Junction resistance [Ohm].
    """
    return eta * K_B * T / (Q_E * I_d)


def pin_forward_resistance(I_f: float, W: float, tau: float,
                           mu_n: float = 0.15, mu_p: float = 0.045) -> float:
    """
    PIN diode forward-bias resistance (I-region conductivity modulation).

    R_f ≈ W^2 / ((mu_n + mu_p) * tau * I_f)

    Parameters
    ----------
    I_f : float
        Forward bias current [A].
    W : float
        I-region width [m].
    tau : float
        Carrier lifetime [s].
    mu_n : float
        Electron mobility [m^2/V·s], default 0.15 for Si.
    mu_p : float
        Hole mobility [m^2/V·s], default 0.045 for Si.

    Returns
    -------
    R_f : float
        Forward resistance [Ohm].
    """
    return W ** 2 / ((mu_n + mu_p) * tau * I_f)


def pin_reverse_capacitance(epsilon_r: float, A: float, W: float) -> float:
    """
    PIN diode reverse-bias capacitance.

    C_R = epsilon * A / W

    Parameters
    ----------
    epsilon_r : float
        Relative permittivity of I-region (11.9 for Si).
    A : float
        Junction area [m^2].
    W : float
        I-region width [m].

    Returns
    -------
    C_R : float
        Reverse capacitance [F].
    """
    return epsilon_r * EPSILON_0 * A / W


def varactor_capacitance(V_R: float, C_j0: float, V_bi: float,
                         gamma: float = 0.5) -> float:
    """
    Varactor diode C-V characteristic.

    C_j(V) = C_j0 / (1 + V_R / V_bi)^gamma

    Parameters
    ----------
    V_R : float
        Reverse bias voltage [V] (positive magnitude).
    C_j0 : float
        Zero-bias junction capacitance [F].
    V_bi : float
        Built-in potential [V].
    gamma : float
        Grading coefficient (0.5 abrupt, >0.5 hyper-abrupt).

    Returns
    -------
    C_j : float
        Junction capacitance [F].
    """
    return C_j0 / (1.0 + V_R / V_bi) ** gamma


def varactor_tuning_ratio(V_R_max: float, V_bi: float,
                          gamma: float = 0.5) -> float:
    """
    Varactor tuning ratio.

    R = (1 + V_R_max / V_bi)^gamma

    Parameters
    ----------
    V_R_max : float
        Maximum reverse bias [V].
    V_bi : float
        Built-in potential [V].
    gamma : float
        Grading coefficient.

    Returns
    -------
    R : float
        Capacitance tuning ratio C(0)/C(V_max).
    """
    return (1.0 + V_R_max / V_bi) ** gamma


def varactor_quality_factor(f: float, R_s: float, C_j: float) -> float:
    """
    Varactor quality factor at frequency f.

    Q = 1 / (2 * pi * f * R_s * C_j)

    Parameters
    ----------
    f : float
        Operating frequency [Hz].
    R_s : float
        Series resistance [Ohm].
    C_j : float
        Junction capacitance [F].

    Returns
    -------
    Q : float
        Quality factor (dimensionless).
    """
    return 1.0 / (2.0 * np.pi * f * R_s * C_j)


def varactor_tuning_frequency(L: float, C_j: float) -> float:
    """
    Resonant frequency of an LC tank with varactor.

    f_0 = 1 / (2 * pi * sqrt(L * C_j))

    Parameters
    ----------
    L : float
        Inductance [H].
    C_j : float
        Varactor capacitance [F].

    Returns
    -------
    f_0 : float
        Resonant frequency [Hz].
    """
    return 1.0 / (2.0 * np.pi * np.sqrt(L * C_j))


def gunn_transit_frequency(v_s: float, L: float) -> float:
    """
    Gunn diode transit-time frequency.

    f_t = v_s / L

    Parameters
    ----------
    v_s : float
        Saturation velocity [m/s] (GaAs: ~1e5 m/s).
    L : float
        Diode active length [m].

    Returns
    -------
    f_t : float
        Transit-time frequency [Hz].
    """
    return v_s / L


def gunn_threshold_voltage(E_th: float, L: float) -> float:
    """
    Gunn diode threshold voltage.

    V_th = E_th * L

    Parameters
    ----------
    E_th : float
        Threshold electric field [V/m] (GaAs: 3.2e5 V/m).
    L : float
        Diode active length [m].

    Returns
    -------
    V_th : float
        Threshold voltage [V].
    """
    return E_th * L


def gunn_drift_velocity(E_field: float, mu_low: float, mu_high: float,
                        E_th: float, v_s: float) -> float:
    """
    Simplified Gunn diode velocity-field characteristic.

    Empirical piecewise model:
    v_d = mu_low * E                     for E < E_th
    v_d = v_s + (mu_high - mu_low)*E_th  ... simplified saturation

    Parameters
    ----------
    E_field : float
        Applied electric field [V/m].
    mu_low : float
        Low-field mobility [m^2/V·s].
    mu_high : float
        High-field (satellite valley) mobility [m^2/V·s].
    E_th : float
        Threshold field [V/m].
    v_s : float
        Saturation velocity [m/s].

    Returns
    -------
    v_d : float
        Drift velocity [m/s].
    """
    if E_field < E_th:
        return mu_low * E_field
    else:
        # Simple piecewise: linear decrease to saturation
        slope = (v_s - mu_low * E_th) / (3 * E_th)  # arbitrary slope
        v = mu_low * E_th - slope * (E_field - E_th)
        return max(v, v_s)


def impatt_transit_frequency(v_s: float, x_d: float) -> float:
    """
    IMPATT diode design frequency (transit-time mode, theta = pi).

    f_design = v_s / (2 * x_d)

    Parameters
    ----------
    v_s : float
        Saturation velocity [m/s].
    x_d : float
        Drift region width [m].

    Returns
    -------
    f_design : float
        Design frequency [Hz].
    """
    return v_s / (2.0 * x_d)


def impatt_efficiency(V_d: float, V_a: float) -> float:
    """
    IMPATT diode DC-to-RF conversion efficiency.

    eta = (1/pi) * V_d / V_a

    Parameters
    ----------
    V_d : float
        Voltage across drift region [V].
    V_a : float
        Avalanche breakdown voltage [V].

    Returns
    -------
    eta : float
        Efficiency (fractional, 0-1).
    """
    return (1.0 / np.pi) * V_d / V_a


def impatt_negative_resistance(J_0: float, A_j: float, f: float,
                               x_a: float, x_d: float, v_s: float,
                               epsilon_r: float = 11.9) -> complex:
    """
    Simplified IMPATT diode small-signal impedance (negative resistance estimate).

    A basic model assuming idealized Read diode.

    Parameters
    ----------
    J_0 : float
        DC bias current density [A/m^2].
    A_j : float
        Junction area [m^2].
    f : float
        Operating frequency [Hz].
    x_a : float
        Avalanche region width [m].
    x_d : float
        Drift region width [m].
    v_s : float
        Saturation velocity [m/s].
    epsilon_r : float
        Relative permittivity.

    Returns
    -------
    Z_d : complex
        Diode impedance [Ohm].
    """
    omega = 2.0 * np.pi * f
    tau_d = x_d / v_s            # Drift transit time [s]
    theta_d = omega * tau_d      # Drift transit angle [rad]
    epsilon = epsilon_r * EPSILON_0
    C_d = epsilon * A_j / (x_a + x_d)  # Depletion capacitance [F]

    # Avalanche resonance frequency (simplified)
    f_a = np.sqrt(2.0 * v_s * J_0) / (2.0 * np.pi * np.sqrt(epsilon * x_a * x_d))
    if f < f_a:
        return complex(0.0, -1.0 / (omega * C_d))  # Capacitive, no negative R

    # Simplified negative resistance from drift region
    R_neg = -(x_d ** 2) / (epsilon * v_s * A_j * theta_d) * (1.0 - np.cos(theta_d))
    X_d = 1.0 / (omega * C_d) * (1.0 - theta_d ** 2 / 12.0)  # approximate

    return complex(R_neg, -X_d)


# ============================================================
# §11.2 — BIPOLAR JUNCTION TRANSISTORS
# ============================================================

def bjt_transconductance(I_C: float, T: float = T0) -> float:
    """
    BJT transconductance.

    g_m = q * I_C / (k * T)

    Parameters
    ----------
    I_C : float
        Collector bias current [A].
    T : float
        Temperature [K].

    Returns
    -------
    g_m : float
        Transconductance [S].
    """
    return Q_E * I_C / (K_B * T)


def bjt_base_resistance(R_pi: float, g_m: float) -> float:
    """
    BJT base-emitter junction resistance.

    R_pi = beta_0 / g_m

    Parameters
    ----------
    R_pi : float
        Base-emitter resistance [Ohm].
    g_m : float
        Transconductance [S].
    Returns
    -------
    beta_0 : float
        Low-frequency current gain (dimensionless).
    """

    return R_pi * g_m


def bjt_f_T(g_m: float, C_pi: float, C_mu: float) -> float:
    """
    BJT unity current gain frequency.

    f_T = g_m / (2 * pi * (C_pi + C_mu))

    Parameters
    ----------
    g_m : float
        Transconductance [S].
    C_pi : float
        Base-emitter capacitance [F].
    C_mu : float
        Base-collector (Miller) capacitance [F].

    Returns
    -------
    f_T : float
        Unity current gain frequency [Hz].
    """
    return g_m / (2.0 * np.pi * (C_pi + C_mu))


def bjt_f_max(f_T: float, R_b: float, C_mu: float) -> float:
    """
    BJT maximum oscillation frequency.

    f_max = sqrt(f_T / (8 * pi * R_b * C_mu))

    Parameters
    ----------
    f_T : float
        Unity current gain frequency [Hz].
    R_b : float
        Base resistance [Ohm].
    C_mu : float
        Base-collector capacitance [F].

    Returns
    -------
    f_max : float
        Maximum oscillation frequency [Hz].
    """
    return np.sqrt(f_T / (8.0 * np.pi * R_b * C_mu))


def bjt_current_gain(beta_0: float, f: float, f_T: float) -> complex:
    """
    BJT short-circuit current gain h_21(f).

    beta(f) = beta_0 / (1 + j * f / f_beta)
    where f_beta = f_T / beta_0

    Parameters
    ----------
    beta_0 : float
        Low-frequency current gain.
    f : float
        Operating frequency [Hz].
    f_T : float
        Unity current gain frequency [Hz].

    Returns
    -------
    h_21 : complex
        Current gain at frequency f.
    """
    f_beta = f_T / beta_0
    return beta_0 / (1.0 + 1j * f / f_beta)


def bjt_miller_capacitance(C_mu: float, g_m: float, R_L: float) -> float:
    """
    BJT Miller (input) capacitance due to C_mu.

    C_miller = C_mu * (1 + g_m * R_L)

    Parameters
    ----------
    C_mu : float
        Base-collector capacitance [F].
    g_m : float
        Transconductance [S].
    R_L : float
        Load resistance [Ohm].

    Returns
    -------
    C_miller : float
        Effective input Miller capacitance [F].
    """
    return C_mu * (1.0 + g_m * R_L)


def bjt_unilateral_power_gain(S_params: np.ndarray, K: float) -> float:
    """
    BJT maximum available gain (MAG).

    MAG = |S21|/|S12| * (K - sqrt(K^2 - 1))

    Parameters
    ----------
    S_params : np.ndarray
        2x2 S-parameter matrix (complex).
    K : float
        Rollett stability factor.

    Returns
    -------
    MAG : float
        Maximum available gain (linear).
    """
    S21_mag = abs(S_params[1, 0])
    S12_mag = abs(S_params[0, 1])
    if S12_mag == 0:
        return np.inf
    return S21_mag / S12_mag * (K - np.sqrt(max(K ** 2 - 1, 0)))


# ============================================================
# §11.3 — FIELD EFFECT TRANSISTORS (MESFET/HEMT)
# ============================================================

def fet_transconductance(I_dss: float, V_gs: float, V_T: float) -> float:
    """
    MESFET transconductance (quadratic model).

    g_m = (2 * sqrt(I_dss * I_ds)) / |V_T|  for V_gs near V_T
    Sharp form: g_m = 2 * I_dss / |V_T| * (1 - V_gs/V_T)

    Parameters
    ----------
    I_dss : float
        Saturation drain current at V_gs=0 [A].
    V_gs : float
        Gate-source voltage [V].
    V_T : float
        Threshold (pinch-off) voltage [V] (negative for depletion-mode).

    Returns
    -------
    g_m : float
        Transconductance [S].
    """
    if V_gs <= V_T:
        return 0.0  # Pinched off
    V_p = abs(V_T)
    return 2.0 * np.sqrt(I_dss) * np.sqrt(I_dss * (1.0 - V_gs / V_T) ** 2) / V_p


def fet_f_T(g_m: float, C_gs: float, C_gd: float) -> float:
    """
    FET unity current gain frequency.

    f_T = g_m / (2 * pi * (C_gs + C_gd))

    Parameters
    ----------
    g_m : float
        Transconductance [S].
    C_gs : float
        Gate-source capacitance [F].
    C_gd : float
        Gate-drain (Miller) capacitance [F].

    Returns
    -------
    f_T : float
        Unity current gain frequency [Hz].
    """
    return g_m / (2.0 * np.pi * (C_gs + C_gd))


def fet_f_T_approximate(v_s: float, L_g: float) -> float:
    """
    FET f_T approximation from gate length.

    f_T ≈ v_s / (2 * pi * L_g)

    Parameters
    ----------
    v_s : float
        Saturation velocity [m/s].
    L_g : float
        Gate length [m].

    Returns
    -------
    f_T : float
        Approximate f_T [Hz].
    """
    return v_s / (2.0 * np.pi * L_g)


def fet_f_max(f_T: float, R_g: float, C_gd: float) -> float:
    """
    FET maximum oscillation frequency (simplified form).

    f_max ≈ sqrt(f_T / (8 * pi * R_g * C_gd))

    Parameters
    ----------
    f_T : float
        Unity current gain frequency [Hz].
    R_g : float
        Gate resistance [Ohm].
    C_gd : float
        Gate-drain capacitance [F].

    Returns
    -------
    f_max : float
        Maximum oscillation frequency [Hz].
    """
    return np.sqrt(f_T / (8.0 * np.pi * R_g * C_gd))


def fet_f_max_full(f_T: float, g_m: float, R_g: float,
                   C_gs: float, C_gd: float) -> float:
    """
    FET f_max with full expression.

    f_max = f_T / sqrt(4 * (R_g * (g_m * C_gd / C_gs + 2*pi*f_T*C_gd*R_g) + ...))

    Simplified common form:
    f_max = f_T / (2 * sqrt(2*pi*f_T*R_g*C_gd + g_m*R_g*C_gd/C_gs))

    Parameters
    ----------
    f_T : float
        Unity current gain frequency [Hz].
    g_m : float
        Transconductance [S].
    R_g : float
        Gate resistance [Ohm].
    C_gs : float
        Gate-source capacitance [F].
    C_gd : float
        Gate-drain capacitance [F].

    Returns
    -------
    f_max : float
        Maximum oscillation frequency [Hz].
    """
    denom = 2.0 * np.sqrt(2.0 * np.pi * f_T * R_g * C_gd
                          + g_m * R_g * C_gd / C_gs)
    if denom == 0:
        return np.inf
    return f_T / denom


def fet_drain_current_curtice(V_gs: float, V_ds: float, V_T: float,
                              beta: float, lam: float = 0.01,
                              alpha: float = 2.0) -> float:
    """
    Curtice quadratic MESFET drain current model.

    I_ds = beta * (V_gs - V_T)^2 * (1 + lambda * V_ds) * tanh(alpha * V_ds)

    Parameters
    ----------
    V_gs : float
        Gate-source voltage [V].
    V_ds : float
        Drain-source voltage [V].
    V_T : float
        Threshold voltage [V].
    beta : float
        Transconductance parameter [A/V^2].
    lam : float
        Channel-length modulation parameter [1/V].
    alpha : float
        Saturation voltage parameter [1/V].

    Returns
    -------
    I_ds : float
        Drain current [A].
    """
    if V_gs <= V_T:
        return 0.0
    return beta * (V_gs - V_T) ** 2 * (1.0 + lam * V_ds) * np.tanh(alpha * V_ds)


def fet_nonlinear_cgs(C_gs0: float, V_gs: float, V_bi: float) -> float:
    """
    Nonlinear gate-source capacitance.

    C_gs(V_gs) = C_gs0 / sqrt(1 - V_gs / V_bi)

    Parameters
    ----------
    C_gs0 : float
        Zero-bias C_gs [F].
    V_gs : float
        Gate-source voltage [V].
    V_bi : float
        Built-in potential [V].

    Returns
    -------
    C_gs : float
        Nonlinear gate-source capacitance [F].
    """
    return C_gs0 / np.sqrt(max(1.0 - V_gs / V_bi, 0.1))


# ============================================================
# §11.4 — MICROWAVE INTEGRATED CIRCUITS
# ============================================================

def microstrip_effective_permittivity(epsilon_r: float, W: float,
                                      h: float) -> float:
    """
    Microstrip effective dielectric constant (Hammerstad-Jensen).

    eps_eff = (eps_r+1)/2 + (eps_r-1)/2 * 1/sqrt(1 + 12*h/W)

    Parameters
    ----------
    epsilon_r : float
        Substrate relative permittivity.
    W : float
        Microstrip width [m].
    h : float
        Substrate height [m].

    Returns
    -------
    epsilon_eff : float
        Effective permittivity.
    """
    epsilon_eff = ((epsilon_r + 1.0) / 2.0
                   + (epsilon_r - 1.0) / 2.0 * 1.0 / np.sqrt(1.0 + 12.0 * h / W))
    return epsilon_eff


def microstrip_characteristic_impedance(epsilon_r: float, W: float,
                                        h: float, t: float = 0.0) -> float:
    """
    Microstrip characteristic impedance (Hammerstad-Jensen).

    Parameters
    ----------
    epsilon_r : float
        Substrate relative permittivity.
    W : float
        Microstrip width [m].
    h : float
        Substrate height [m].
    t : float
        Metal thickness [m] (optional, default 0).

    Returns
    -------
    Z_0 : float
        Characteristic impedance [Ohm].
    """
    epsilon_eff = microstrip_effective_permittivity(epsilon_r, W, h)
    Z_0_air = 377.0 * h / W  # Approximation for wide line
    Z_0 = Z_0_air / np.sqrt(epsilon_eff)
    return Z_0


def microstrip_loss_conductor(R_surf: float, W: float, f: float,
                              epsilon_eff: float) -> float:
    """
    Microstrip conductor attenuation (simplified).

    alpha_c = R_surf / (Z_0 * W)   [Np/m] (approximate)

    Parameters
    ----------
    R_surf : float
        Surface resistivity [Ohm/sq].
    W : float
        Microstrip width [m].
    f : float
        Frequency [Hz].
    epsilon_eff : float
        Effective permittivity.

    Returns
    -------
    alpha_c : float
        Conductor attenuation [dB/m].
    """
    sigma = 5.8e7  # Cu conductivity [S/m]
    delta_skin = np.sqrt(1.0 / (np.pi * f * constants.mu_0 * sigma))
    R_s = 1.0 / (sigma * delta_skin)  # Surface resistivity [Ohm/sq]
    alpha_np = R_s / (W * microstrip_characteristic_impedance(
        1.0, W, 0.8e-3))  # approximate
    return 8.686 * alpha_np  # Convert Np/m to dB/m


def microstrip_loss_dielectric(epsilon_r: float, epsilon_eff: float,
                               tan_delta: float, f: float) -> float:
    """
    Microstrip dielectric attenuation.

    alpha_d = pi * eps_r * (eps_eff - 1) * tan_delta
              / (sqrt(eps_eff) * (eps_r - 1) * lambda_0)   [Np/m]

    Parameters
    ----------
    epsilon_r : float
        Substrate relative permittivity.
    epsilon_eff : float
        Effective permittivity.
    tan_delta : float
        Dielectric loss tangent.
    f : float
        Frequency [Hz].

    Returns
    -------
    alpha_d : float
        Dielectric attenuation [dB/m].
    """
    lambda_0 = C0 / f
    alpha_np = (np.pi * epsilon_r * (epsilon_eff - 1.0) * tan_delta
                / (np.sqrt(epsilon_eff) * (epsilon_r - 1.0) * lambda_0))
    return 8.686 * alpha_np


def cpw_characteristic_impedance(epsilon_r: float, S: float, G: float,
                                 h: float) -> float:
    """
    Coplanar waveguide (CPW) characteristic impedance (quasi-static).

    Finite ground CPW approximation.

    Parameters
    ----------
    epsilon_r : float
        Substrate relative permittivity.
    S : float
        Center conductor width [m].
    G : float
        Gap between center conductor and ground [m].
    h : float
        Substrate height [m].

    Returns
    -------
    Z_0 : float
        Characteristic impedance [Ohm].
    """
    k = S / (S + 2.0 * G)  # CPW geometry ratio
    k1 = np.sinh(np.pi * S / (4.0 * h)) / np.sinh(np.pi * (S + 2.0 * G) / (4.0 * h))

    # Complete elliptic integral K(k) approximation
    def ellipk(kk: float) -> float:
        kk = max(abs(kk), 1e-6)
        if kk >= 1:
            return np.inf
        kp = np.sqrt(1.0 - kk ** 2)
        # Hilberg approximation
        if kk ** 2 <= 0.5:
            return np.pi / (np.log(2.0 * (1.0 + np.sqrt(kp))
                                   / (1.0 - np.sqrt(kp))))
        else:
            return np.log(2.0 * (1.0 + np.sqrt(kk)) / (1.0 - np.sqrt(kk))) / np.pi

    K_k = ellipk(k)
    K_kp = ellipk(np.sqrt(1.0 - k ** 2))
    K_k1 = ellipk(k1)
    K_k1p = ellipk(np.sqrt(1.0 - k1 ** 2))

    epsilon_eff = 1.0 + (epsilon_r - 1.0) / 2.0 * (K_k1 / K_k1p) / (K_k / K_kp)
    Z_0 = 30.0 * np.pi / np.sqrt(epsilon_eff) * K_kp / K_k
    return Z_0


# ============================================================
# PLOTTING FUNCTIONS
# ============================================================

def plot_schottky_iv() -> None:
    """Plot Schottky diode I-V characteristic."""
    V_d = np.linspace(-2.0, 1.0, 500)
    I_S = 1e-9  # 1 nA saturation current

    fig, ax = plt.subplots(figsize=(10, 6))

    for eta, style, label in [(1.05, 'b-', r'$\eta = 1.05$ (ideal)'),
                               (1.10, 'r--', r'$\eta = 1.10$'),
                               (1.20, 'g:', r'$\eta = 1.20$ (poor)')]:
        I_d = schottky_iv_current(V_d, I_S, eta)
        ax.semilogy(V_d, np.maximum(I_d, 1e-15), style, linewidth=2, label=label)

    ax.set_xlabel("Diode Voltage $V_d$ [V]")
    ax.set_ylabel("Diode Current $I_d$ [A]")
    ax.set_title("Schottky Diode I-V Characteristic ($I_S = 1$ nA)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(-2, 1)
    ax.set_ylim(1e-15, 1e-2)

    # Annotate key regions
    ax.annotate("Reverse bias", xy=(-1.5, 1e-12), fontsize=9,
                bbox=dict(boxstyle='round', fc='lightblue', alpha=0.3))
    ax.annotate("Forward conduction", xy=(0.3, 1e-4), fontsize=9,
                bbox=dict(boxstyle='round', fc='lightgreen', alpha=0.3))

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_1_schottky_iv.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_varactor_cv() -> None:
    """Plot varactor C-V characteristic and tuning."""
    V_R = np.linspace(0, 20, 300)
    C_j0 = 2e-12  # 2 pF
    V_bi = 0.8

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: C-V for different grading coefficients
    for gamma, style, label in [(0.33, 'g-', r'$\gamma = 0.33$ (linear)'),
                                 (0.5, 'b-', r'$\gamma = 0.5$ (abrupt)'),
                                 (0.75, 'r--', r'$\gamma = 0.75$ (hyper)'),
                                 (1.0, 'm:', r'$\gamma = 1.0$ (hyper)')]:
        C_j = varactor_capacitance(V_R, C_j0, V_bi, gamma)
        ax1.plot(V_R, C_j * 1e12, style, linewidth=2, label=label)

    ax1.set_xlabel("Reverse Bias $V_R$ [V]")
    ax1.set_ylabel("Junction Capacitance $C_j$ [pF]")
    ax1.set_title("Varactor C-V Characteristic")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_ylim(0, C_j0 * 1e12 * 1.1)

    # Right: LC tuning frequency
    L = 1e-9  # 1 nH
    for gamma, style, label in [(0.5, 'b-', r'$\gamma = 0.5$'),
                                 (0.75, 'r--', r'$\gamma = 0.75$')]:
        f_vals = [varactor_tuning_frequency(L, varactor_capacitance(
            vr, C_j0, V_bi, gamma)) for vr in V_R]
        ax2.plot(V_R, np.array(f_vals) / 1e9, style, linewidth=2, label=label)

    ax2.set_xlabel("Reverse Bias $V_R$ [V]")
    ax2.set_ylabel("Resonant Frequency $f_0$ [GHz]")
    ax2.set_title("LC Resonator Tuning ($L = 1$ nH, $C_{j0} = 2$ pF)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_2_varactor_cv.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_pin_diode() -> None:
    """Plot PIN diode forward resistance vs bias current."""
    I_f_vals = np.logspace(-4, -1, 200)  # 0.1 to 100 mA
    # Si PIN with different I-layer widths
    widths = [10e-6, 50e-6, 150e-6]  # 10, 50, 150 um
    tau = 1e-7  # 100 ns carrier lifetime

    fig, ax = plt.subplots(figsize=(10, 6))

    for W in widths:
        R_f = pin_forward_resistance(I_f_vals, W, tau)
        ax.loglog(I_f_vals * 1e3, R_f, linewidth=2,
                  label=f"$W = {W*1e6:.0f}\\ \\mu$m")

    ax.set_xlabel("Forward Bias Current $I_f$ [mA]")
    ax.set_ylabel(r"Forward Resistance $R_f$ [$\Omega$]")
    ax.set_title("PIN Diode Forward Resistance vs Bias Current ($\\tau = 100$ ns)")
    ax.grid(True, alpha=0.3, which='both')
    ax.legend()

    # Annotate typical switch region
    ax.axhspan(0.5, 5, alpha=0.1, color='green', label="Low-loss switch (ON)")
    ax.axhspan(1000, 10000, alpha=0.1, color='red',
               label="High-isolation switch (OFF)")

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_3_pin_diode.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_gunn_diode() -> None:
    """Plot Gunn diode velocity-field and frequency-length relationship."""
    E_field = np.linspace(0, 2e6, 500)  # 0 to 20 kV/cm
    mu_low = 6000e-4  # [m^2/V·s] = 6000 cm^2/V·s converted
    v_s = 1e5  # 10^7 cm/s = 10^5 m/s
    E_th = 3.2e5  # 3.2 kV/cm for GaAs

    # Velocities for GaAs
    mu_low_real = 0.6    # m^2/V·s (6000 cm^2/V·s)
    mu_high_real = 0.08  # m^2/V·s (800 cm^2/V·s)

    v_d = np.zeros_like(E_field)
    for i, E in enumerate(E_field):
        if E < E_th:
            v_d[i] = mu_low_real * E
        else:
            v_d[i] = v_s + (mu_high_real - mu_low_real) * (E - E_th)
            v_d[i] = max(v_d[i], v_s * 0.1)

    # Transit frequency vs length
    L_vals = np.linspace(1e-6, 50e-6, 200)
    f_t_vals = gunn_transit_frequency(v_s, L_vals)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: v-E curve
    ax1.plot(E_field / 1e5, v_d / 1e5, 'b-', linewidth=2)
    ax1.axvline(E_th / 1e5, color='red', linestyle='--', alpha=0.7,
                label=f"$E_{{th}} = {E_th/1e5:.1f}$ kV/cm")
    ax1.set_xlabel("Electric Field $E$ [kV/cm]")
    ax1.set_ylabel(r"Drift Velocity $v_d$ [$\times 10^5$ m/s]")
    ax1.set_title("GaAs Gunn Diode: Velocity-Field Characteristic")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(0, 20)

    # Annotate NDR region
    ax1.fill_between(E_field[E_field >= E_th] / 1e5,
                     v_d[E_field >= E_th] / 1e5,
                     alpha=0.2, color='red', label="NDR region")
    ax1.legend()

    # Right: transit frequency
    ax2.semilogy(L_vals * 1e6, f_t_vals / 1e9, 'b-', linewidth=2)
    ax2.set_xlabel(r"Active Length $L$ [$\mu$m]")
    ax2.set_ylabel("Transit Frequency $f_t$ [GHz]")
    ax2.set_title("Gunn Diode: Transit Frequency vs Length")
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 50)

    # Mark typical points
    for L_m, label in [(2, "2 $\\mu$m → 50 GHz"),
                        (5, "5 $\\mu$m → 20 GHz"),
                        (10, "10 $\\mu$m → 10 GHz")]:
        f = gunn_transit_frequency(v_s, L_m * 1e-6)
        ax2.plot(L_m, f / 1e9, 'ro', markersize=6)
        ax2.annotate(label, xy=(L_m, f / 1e9), fontsize=8,
                     xytext=(L_m + 2, f / 1e9),
                     arrowprops=dict(arrowstyle='->', color='red'))

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_4_gunn_diode.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_impatt_diode() -> None:
    """Plot IMPATT diode characteristics."""
    # Transit frequency
    v_s = 1e5  # m/s (Si saturation velocity)
    x_d_vals = np.linspace(0.5e-6, 10e-6, 200)
    f_design = impatt_transit_frequency(v_s, x_d_vals)

    # Efficiency
    V_a_vals = np.array([30, 60, 100])  # Breakdown voltages [V]
    V_d_ratio = np.linspace(0.1, 1.0, 100)  # V_d / V_a ratio

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Left: design frequency vs drift length
    ax1.semilogy(x_d_vals * 1e6, f_design / 1e9, 'b-', linewidth=2)
    ax1.set_xlabel(r"Drift Region Width $x_d$ [$\mu$m]")
    ax1.set_ylabel("Design Frequency $f_{\\mathrm{design}}$ [GHz]")
    ax1.set_title("IMPATT Diode: Design Frequency vs Drift Length")
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 10)

    # Mark bands
    for freq, label, color in [(10, "X-band", 'red'),
                                (35, "Ka-band", 'orange'),
                                (94, "W-band", 'green')]:
        xd = v_s / (2 * freq * 1e9)
        ax1.axhline(freq, color=color, linestyle=':', alpha=0.4)
        ax1.annotate(label, xy=(xd * 1e6, freq), fontsize=8,
                     ha='center', va='bottom', color=color)

    # Right: efficiency
    for V_br in V_a_vals:
        eta_vals = [impatt_efficiency(V * V_br, V_br) for V in V_d_ratio]
        ax2.plot(V_d_ratio * V_br, np.array(eta_vals) * 100, linewidth=2,
                 label=f"$V_a = {V_br}$ V")

    ax2.set_xlabel("Drift Voltage $V_d = V_d/V_a \\cdot V_a$ [V]")
    ax2.set_ylabel("Efficiency $\\eta$ [%]")
    ax2.set_title("IMPATT Diode: DC-to-RF Efficiency")
    ax2.grid(True, alpha=0.3)
    ax2.legend()

    # Theoretical max
    eta_max = (1.0 / np.pi) * 100
    ax2.axhline(eta_max, color='black', linestyle='--', alpha=0.5,
                label=f"$\\eta_{{\\max}} \\approx {eta_max:.1f}\\%$ ($V_d=V_a$)")
    ax2.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_5_impatt_diode.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_bjt_fT_fmax() -> None:
    """Plot BJT f_T and f_max vs collector current."""
    I_C_vals = np.logspace(-4, -2, 200)  # 0.1 to 10 mA
    C_pi = 0.5e-12  # 0.5 pF
    C_mu = 50e-15   # 50 fF
    R_b = 10.0       # 10 Ohm base resistance

    g_m_vals = np.array([bjt_transconductance(Ic) for Ic in I_C_vals])
    f_T_vals = np.array([bjt_f_T(gm, C_pi, C_mu) for gm in g_m_vals])
    f_max_vals = np.array([bjt_f_max(ft, R_b, C_mu) for ft in f_T_vals])

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.semilogx(I_C_vals * 1e3, f_T_vals / 1e9, 'b-', linewidth=2,
                label="$f_T$")
    ax.semilogx(I_C_vals * 1e3, f_max_vals / 1e9, 'r--', linewidth=2,
                label="$f_{\\max}$")

    # Annotate
    I_opt = I_C_vals[np.argmax(f_T_vals)]
    fT_opt = np.max(f_T_vals)
    ax.plot(I_opt * 1e3, fT_opt / 1e9, 'ko', markersize=6)
    ax.annotate(f"$I_C = {I_opt*1e3:.2f}$ mA\n$f_T = {fT_opt/1e9:.1f}$ GHz",
                xy=(I_opt * 1e3, fT_opt / 1e9), fontsize=8,
                xytext=(I_opt * 1e3 * 2, fT_opt / 1e9),
                arrowprops=dict(arrowstyle='->'))

    ax.set_xlabel("Collector Current $I_C$ [mA]")
    ax.set_ylabel("Frequency [GHz]")
    ax.set_title("BJT $f_T$ and $f_{\\max}$ vs Collector Current")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0.1, 10)
    ax.set_ylim(0, max(f_max_vals / 1e9) * 1.2)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_6_bjt_ft_fmax.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_fet_ft_fmax() -> None:
    """Plot FET f_T and f_max vs gate voltage."""
    V_gs_vals = np.linspace(-1.5, 0, 200)
    I_dss = 0.1  # 100 mA saturation current
    V_T = -1.0   # Depletion mode threshold
    C_gs = 0.3e-12  # 0.3 pF
    C_gd = 30e-15   # 30 fF
    R_g = 2.0        # 2 Ohm gate resistance
    v_s = 1.5e5  # m/s (InGaAs 2DEG)
    L_g = 0.1e-6  # 100 nm gate length

    g_m_vals = np.array([fet_transconductance(I_dss, Vgs, V_T)
                         for Vgs in V_gs_vals])
    f_T_vals = np.array([fet_f_T(gm, C_gs, C_gd) for gm in g_m_vals])
    f_max_vals = np.array([fet_f_max(ft, R_g, C_gd) for ft in f_T_vals])

    # Theoretical limit from gate length
    f_T_limit = fet_f_T_approximate(v_s, L_g)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(V_gs_vals, f_T_vals / 1e9, 'b-', linewidth=2, label="$f_T$")
    ax.plot(V_gs_vals, f_max_vals / 1e9, 'r--', linewidth=2, label="$f_{\\max}$")
    ax.axhline(f_T_limit / 1e9, color='green', linestyle=':', alpha=0.6,
               label=f"$f_T$ limit ($L_g = {L_g*1e6:.1f}\\ \\mu$m)")

    ax.set_xlabel("Gate-Source Voltage $V_{gs}$ [V]")
    ax.set_ylabel("Frequency [GHz]")
    ax.set_title("MESFET/HEMT $f_T$ and $f_{\\max}$ vs $V_{gs}$")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(V_gs_vals[0], V_gs_vals[-1])
    ax.set_ylim(0, max(f_max_vals / 1e9) * 1.3)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_7_fet_ft_fmax.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_transistor_technology_comparison() -> None:
    """Plot technology comparison: f_T vs f_max scatter."""
    technologies = {
        "Si BJT":      (50, 70),
        "SiGe HBT":    (350, 400),
        "GaAs MESFET": (80, 100),
        "GaAs pHEMT":  (200, 350),
        "InP HEMT":    (600, 1000),
        "GaN HEMT":    (100, 250),
    }

    fig, ax = plt.subplots(figsize=(10, 6))

    for name, (fT, fM) in technologies.items():
        ax.plot(fT, fM, 'o', markersize=12, label=name)
        ax.annotate(name, xy=(fT, fM), fontsize=8,
                    xytext=(fT + 15, fM - 10),
                    arrowprops=dict(arrowstyle='->', alpha=0.5))

    # Diagonal: f_max = f_T
    f_line = np.linspace(10, 1000, 100)
    ax.plot(f_line, f_line, 'k--', alpha=0.3, label=r"$f_{\max} = f_T$")

    ax.set_xlabel("$f_T$ [GHz]")
    ax.set_ylabel("$f_{\\max}$ [GHz]")
    ax.set_title("Transistor Technology Comparison")
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    ax.set_xlim(0, 700)
    ax.set_ylim(0, 1100)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_8_tech_comparison.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_curtice_fet_iv() -> None:
    """Plot FET I-V curves using Curtice model."""
    V_ds_vals = np.linspace(0, 5, 200)
    V_T = -1.0
    beta = 0.05  # A/V^2

    fig, ax = plt.subplots(figsize=(10, 6))

    for V_gs in [0, -0.25, -0.5, -0.75, -0.9]:
        I_ds_vals = np.array([fet_drain_current_curtice(V_gs, Vds, V_T, beta)
                              for Vds in V_ds_vals])
        ax.plot(V_ds_vals, I_ds_vals * 1e3, linewidth=2,
                label=f"$V_{{gs}} = {V_gs:.2f}$ V")

        # Mark saturation region
        V_dsat = V_gs - V_T
        I_dsat = fet_drain_current_curtice(V_gs, V_dsat * 1.5, V_T, beta)
        ax.plot(V_dsat, I_dsat * 1e3, 'ko', markersize=4)

    ax.set_xlabel("Drain-Source Voltage $V_{ds}$ [V]")
    ax.set_ylabel("Drain Current $I_{ds}$ [mA]")
    ax.set_title("MESFET $I_{ds}-V_{ds}$ (Curtice Model, $V_T = -1$ V)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 5)

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_9_curtice_fet_iv.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_microstrip_cpw_comparison() -> None:
    """Plot microstrip vs CPW Z0 comparison."""
    epsilon_r_substrates = {
        "Alumina ($\\epsilon_r=9.9$)": 9.9,
        "Quartz ($\\epsilon_r=3.78$)": 3.78,
        "GaAs ($\\epsilon_r=12.9$)": 12.9,
    }

    aspect_ratios = np.linspace(0.1, 10, 300)  # W/h for microstrip
    h_sub = 0.254e-3  # 10 mil substrate

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))

    # Top left: Microstrip Z0
    for name, eps_r in epsilon_r_substrates.items():
        Z0_vals = []
        for ratio in aspect_ratios:
            W = ratio * h_sub
            Z0 = microstrip_characteristic_impedance(eps_r, W, h_sub)
            Z0_vals.append(Z0)
        ax1.semilogy(aspect_ratios, Z0_vals, linewidth=2, label=name)
    ax1.set_xlabel("$W/h$ (Aspect Ratio)")
    ax1.set_ylabel(r"$Z_0$ [$\Omega$]")
    ax1.set_title("Microstrip Characteristic Impedance")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_xlim(0.1, 10)

    # Top right: Microstrip effective permittivity (eps_r=9.9, alumina)
    eps_r_test = 9.9
    eps_eff_vals = [microstrip_effective_permittivity(eps_r_test, r * h_sub, h_sub)
                    for r in aspect_ratios]
    ax2.plot(aspect_ratios, eps_eff_vals, 'b-', linewidth=2,
             label=f"$\\epsilon_r = {eps_r_test}$")
    ax2.axhline((eps_r_test + 1) / 2, color='red', linestyle='--', alpha=0.5,
                label="$\\frac{\\epsilon_r + 1}{2}$")
    ax2.axhline(eps_r_test, color='green', linestyle=':', alpha=0.5,
                label=f"$\\epsilon_r = {eps_r_test}$")
    ax2.set_xlabel("$W/h$ (Aspect Ratio)")
    ax2.set_ylabel("$\\epsilon_{\\mathrm{eff}}$")
    ax2.set_title("Microstrip Effective Permittivity (Alumina)")
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    ax2.set_ylim(1, eps_r_test * 1.05)

    # Bottom left: Microstrip loss comparison
    f_vals = np.logspace(8, 11, 200)  # 0.1 GHz to 100 GHz
    W_50 = 0.25e-3  # ~50 Ohm line width
    eps_r_al = 9.9
    eps_eff_al = microstrip_effective_permittivity(eps_r_al, W_50, h_sub)

    alpha_d_vals = [microstrip_loss_dielectric(eps_r_al, eps_eff_al, 1e-4, f)
                    for f in f_vals]
    alpha_c_vals = [microstrip_loss_conductor(0.02, W_50, f, eps_eff_al)
                    for f in f_vals]

    ax3.loglog(f_vals / 1e9, alpha_d_vals, 'r-', linewidth=2,
               label="Dielectric loss ($\\tan\\delta=10^{-4}$)")
    ax3.loglog(f_vals / 1e9, alpha_c_vals, 'b-', linewidth=2,
               label="Conductor loss (Cu)")
    ax3.loglog(f_vals / 1e9, np.array(alpha_d_vals) + np.array(alpha_c_vals),
               'k--', linewidth=2, label="Total loss")
    ax3.set_xlabel("Frequency $f$ [GHz]")
    ax3.set_ylabel("Attenuation [dB/m]")
    ax3.set_title("Microstrip Loss (Alumina, $Z_0 \\approx 50$ $\\Omega$)")
    ax3.grid(True, alpha=0.3)
    ax3.legend()
    ax3.set_xlim(0.1, 100)

    # Bottom right: CPW Z0 example
    G_vals = np.linspace(5e-6, 100e-6, 200)
    S_fixed = 50e-6  # 50 um center conductor
    for eps_r_cpw, style, label in [(3.78, 'b-', "Quartz"),
                                     (9.9, 'r--', "Alumina"),
                                     (12.9, 'g:', "GaAs")]:
        Z0_cpw = [cpw_characteristic_impedance(eps_r_cpw, S_fixed, G, h_sub)
                  for G in G_vals]
        ax4.plot(G_vals * 1e6, Z0_cpw, style, linewidth=2, label=label)
    ax4.set_xlabel(r"Gap Width $G$ [$\mu$m]")
    ax4.set_ylabel(r"$Z_0$ [$\Omega$]")
    ax4.set_title("CPW Characteristic Impedance ($S = 50$ $\\mu$m)")
    ax4.grid(True, alpha=0.3)
    ax4.legend()

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_10_microstrip_cpw.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


def plot_tunnel_diode_iv() -> None:
    """Plot tunnel diode I-V characteristic with NDR region."""
    V_d = np.linspace(0, 0.7, 500)  # mV range

    # Simplified tunnel diode model
    I_P = 5e-3   # 5 mA peak
    V_P = 0.065  # 65 mV peak voltage
    I_V = 1e-3   # 1 mA valley
    V_V = 0.35   # 350 mV valley
    I_F = 2e-3   # 2 mA at high forward bias
    V_F = 0.55   # forward knee

    # Exponential + tunneling terms (phenomenological model)
    I_d = (I_P * (V_d / V_P) * np.exp(1 - V_d / V_P)
           + I_V * np.exp((V_d - V_V) / 0.04))

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(V_d * 1000, I_d * 1e3, 'b-', linewidth=2, label="Tunnel Diode I-V")

    # Mark key points
    ax.plot(V_P * 1000, I_P * 1e3, 'ro', markersize=8, label=f"Peak: $V_P={V_P*1000:.0f}$ mV")
    ax.plot(V_V * 1000, I_V * 1e3, 'go', markersize=8, label=f"Valley: $V_V={V_V*1000:.0f}$ mV")

    # Shade NDR region
    idx_peak = np.argmin(np.abs(V_d - V_P))
    idx_valley = np.argmin(np.abs(V_d - V_V))
    ax.fill_between(V_d[idx_peak:idx_valley] * 1000,
                    I_d[idx_peak:idx_valley] * 1e3,
                    alpha=0.2, color='red', label="NDR (Negative $R$)")
    ax.axvspan(V_P * 1000, V_V * 1000, alpha=0.1, color='red')

    ax.set_xlabel("Diode Voltage $V_d$ [mV]")
    ax.set_ylabel("Diode Current $I_d$ [mA]")
    ax.set_title("Tunnel Diode I-V Characteristic (Esaki Diode)")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 600)
    ax.set_ylim(0, I_P * 1e3 * 1.2)

    # Annotate PVCR
    PVCR = I_P / I_V
    ax.annotate(f"PVCR = {PVCR:.1f}:1",
                xy=((V_P + V_V) / 2 * 1000, (I_P + I_V) / 2 * 1e3),
                fontsize=10, ha='center',
                bbox=dict(boxstyle='round', fc='lightyellow', alpha=0.8))

    plt.tight_layout()
    path = os.path.join(FIG_DIR, "fig14_11_tunnel_diode.png")
    plt.savefig(path, dpi=150)
    plt.close()
    print(f"  [v] Saved {path}")


# ============================================================
# EXAMPLE CALCULATIONS
# ============================================================

def run_examples() -> None:
    """Print numeric examples for all major concepts."""
    print("=" * 72)
    print("Pozar Ch14 (4e Ch11) — Numerical Examples")
    print("=" * 72)

    # ---- §11.1 Diode Examples ----
    print("\n" + "=" * 50)
    print("  Section 11.1 — Microwave Diodes")
    print("=" * 50)

    # Schottky diode
    print("\n  --- Schottky Diode ---")
    I_S = 1e-9  # 1 nA
    for V_f in [0.2, 0.4, 0.6]:
        I_f = schottky_iv_current(np.array([V_f]), I_S)[0]
        R_j = schottky_junction_resistance(I_f)
        print(f"    V_d = {V_f:.1f} V  =>  I_d = {I_f:.4e} A,"
              f" R_j = {R_j:.1f} Ohm")

    # Schottky cutoff
    R_s = 5.0  # Ohm
    C_j0 = 0.2e-12  # 0.2 pF
    f_c = schottky_cutoff_frequency(R_s, C_j0)
    print(f"\n    R_s = {R_s} Ohm, C_j0 = {C_j0*1e12:.1f} pF")
    print(f"    f_c = {f_c/1e9:.1f} GHz")

    # PIN diode
    print("\n  --- PIN Diode ---")
    W = 50e-6
    tau = 1e-7
    for I_f in [1e-3, 10e-3, 50e-3]:
        R_f = pin_forward_resistance(I_f, W, tau)
        print(f"    I_f = {I_f*1e3:.0f} mA  =>  R_f = {R_f:.2f} Ohm")
    A_pin = 1e-8  # 0.01 mm^2
    C_R = pin_reverse_capacitance(11.9, A_pin, W)
    print(f"    Reverse bias: C_R = {C_R*1e12:.2f} pF (A={A_pin*1e8:.1e} mm^2,"
          f" W={W*1e6:.0f} um)")

    # Varactor
    print("\n  --- Varactor Diode ---")
    C_j0_v = 2e-12
    V_bi = 0.8
    for gamma_name, gamma in [("abrupt (0.5)", 0.5), ("hyper (0.75)", 0.75),
                               ("hyper (1.0)", 1.0)]:
        R_t = varactor_tuning_ratio(10, V_bi, gamma)
        print(f"    Tuning ratio ({gamma_name}): R = {R_t:.2f}:1")
    # Q at 2 GHz
    R_s_v = 1.5
    C_j_v = varactor_capacitance(5, C_j0_v, V_bi, 0.5)
    Q_v = varactor_quality_factor(2e9, R_s_v, C_j_v)
    print(f"    Q @ 2 GHz, V_R=5 V: {Q_v:.0f}")

    L_tank = 1e-9
    for V_R in [0, 5, 10, 15]:
        Cj = varactor_capacitance(V_R, C_j0_v, V_bi, 0.5)
        f0 = varactor_tuning_frequency(L_tank, Cj)
        print(f"    f0(V_R={V_R:2d} V) = {f0/1e9:.3f} GHz"
              f" (C_j = {Cj*1e12:.3f} pF, L = 1 nH)")

    # Gunn diode
    print("\n  --- Gunn Diode ---")
    v_s_gaas = 1e5
    for L_gunn in [1e-6, 2e-6, 5e-6, 10e-6]:
        f_t_gunn = gunn_transit_frequency(v_s_gaas, L_gunn)
        V_th_gunn = gunn_threshold_voltage(3.2e5, L_gunn)
        print(f"    L = {L_gunn*1e6:.0f} um  =>  f_t = {f_t_gunn/1e9:.2f} GHz,"
              f" V_th = {V_th_gunn:.1f} V")

    # IMPATT
    print("\n  --- IMPATT Diode ---")
    v_s_si = 1e5
    for x_d in [1e-6, 3e-6, 5e-6]:
        f_impatt = impatt_transit_frequency(v_s_si, x_d)
        print(f"    x_d = {x_d*1e6:.1f} um  =>  f_design = {f_impatt/1e9:.2f} GHz")
    # Efficiency
    V_a = 60.0
    for V_d_frac in [0.3, 0.5, 0.7]:
        eta_imp = impatt_efficiency(V_d_frac * V_a, V_a)
        print(f"    V_d/V_a = {V_d_frac:.1f}  =>  eta = {eta_imp*100:.1f}%")

    # ---- §11.2 BJT Examples ----
    print("\n" + "=" * 50)
    print("  Section 11.2 — Bipolar Junction Transistors")
    print("=" * 50)

    # BJT hybrid-pi
    I_C = 2e-3  # 2 mA
    g_m = bjt_transconductance(I_C)
    C_pi = 0.4e-12
    C_mu = 30e-15
    R_b_bjt = 8.0

    f_T_bjt = bjt_f_T(g_m, C_pi, C_mu)
    f_max_bjt = bjt_f_max(f_T_bjt, R_b_bjt, C_mu)

    print(f"\n    I_C = {I_C*1e3:.2f} mA")
    print(f"    g_m = {g_m*1e3:.1f} mS")
    print(f"    C_pi = {C_pi*1e12:.1f} pF, C_mu = {C_mu*1e15:.0f} fF")
    print(f"    R_b = {R_b_bjt:.1f} Ohm")
    print(f"    f_T = {f_T_bjt/1e9:.1f} GHz")
    print(f"    f_max = {f_max_bjt/1e9:.1f} GHz")

    # Current gain vs freq
    beta_0 = 150
    for f_test in [1e8, 1e9, 5e9, 10e9, 30e9]:
        h21 = bjt_current_gain(beta_0, f_test, f_T_bjt)
        print(f"    |h_21| @ {f_test/1e9:.1f} GHz = {abs(h21):.1f}"
              f" ({20*np.log10(abs(h21)):.1f} dB)")

    # Miller effect
    R_L = 100.0
    C_miller = bjt_miller_capacitance(C_mu, g_m, R_L)
    print(f"\n    Miller capacitance: C_miller = {C_miller*1e15:.1f} fF")
    print(f"    Effective C_in = C_pi + C_miller = {(C_pi + C_miller)*1e12:.2f} pF")

    # ---- §11.3 FET Examples ----
    print("\n" + "=" * 50)
    print("  Section 11.3 — Field Effect Transistors")
    print("=" * 50)

    I_dss = 0.08  # 80 mA
    V_T_fet = -1.0

    print("\n  --- MESFET Small-Signal ---")
    for V_gs in [0, -0.25, -0.5, -0.75]:
        g_m_fet = fet_transconductance(I_dss, V_gs, V_T_fet)
        C_gs_fet = 0.25e-12
        C_gd_fet = 25e-15
        f_T_fet = fet_f_T(g_m_fet, C_gs_fet, C_gd_fet)
        R_g_fet = 2.0
        f_max_fet = fet_f_max(f_T_fet, R_g_fet, C_gd_fet)
        print(f"    V_gs = {V_gs:.2f} V  =>  g_m = {g_m_fet*1e3:.1f} mS,"
              f" f_T = {f_T_fet/1e9:.1f} GHz, f_max = {f_max_fet/1e9:.1f} GHz")

    # Curtice model example
    print("\n  --- Curtice I-V Model ---")
    V_T_c = -1.0
    beta_c = 0.05
    for V_gs in [0, -0.5]:
        for V_ds in [1, 2, 4]:
            I_ds_c = fet_drain_current_curtice(V_gs, V_ds, V_T_c, beta_c)
            print(f"    V_gs = {V_gs:.1f} V, V_ds = {V_ds:.0f} V  =>"
                  f" I_ds = {I_ds_c*1e3:.2f} mA")

    # f_T from gate length
    print("\n  --- f_T from Gate Length ---")
    for L_g in [0.05e-6, 0.1e-6, 0.25e-6, 0.5e-6]:
        fT_gate = fet_f_T_approximate(1.5e5, L_g)
        print(f"    L_g = {L_g*1e6:.2f} um  =>  f_T ≈ {fT_gate/1e9:.0f} GHz")

    # ---- §11.4 MIC Examples ----
    print("\n" + "=" * 50)
    print("  Section 11.4 — Microwave Integrated Circuits")
    print("=" * 50)

    print("\n  --- Microstrip ---")
    for eps_r, name in [(9.9, "Alumina"), (3.78, "Quartz"), (12.9, "GaAs")]:
        h = 0.254e-3
        W_50_guess = h  # rough 50 Ohm
        Z0_ms = microstrip_characteristic_impedance(eps_r, W_50_guess, h)
        eps_eff = microstrip_effective_permittivity(eps_r, W_50_guess, h)
        print(f"    {name} (eps_r={eps_r}): W/h=1 => Z0={Z0_ms:.1f} Ohm,"
              f" eps_eff={eps_eff:.2f}")

    print("\n  --- CPW ---")
    S = 50e-6
    for G in [20e-6, 50e-6, 100e-6]:
        Z0_cpw = cpw_characteristic_impedance(12.9, S, G, 0.254e-3)
        print(f"    GaAs: S={S*1e6:.0f} um, G={G*1e6:.0f} um  =>  Z0={Z0_cpw:.1f} Ohm")

    print("\n" + "=" * 72)
    print("  All numerical examples complete.")
    print("=" * 72)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    print("Generating figures for Pozar Ch14 (4e Ch11)...\n")

    # §11.1 — Microwave Diodes
    print("[11.1] Microwave diode figures...")
    plot_schottky_iv()
    plot_varactor_cv()
    plot_pin_diode()
    plot_gunn_diode()
    plot_impatt_diode()
    plot_tunnel_diode_iv()

    # §11.2 — BJT
    print("[11.2] BJT figures...")
    plot_bjt_fT_fmax()

    # §11.3 — FET
    print("[11.3] FET figures...")
    plot_fet_ft_fmax()
    plot_curtice_fet_iv()
    plot_transistor_technology_comparison()

    # §11.4 — MIC
    print("[11.4] MIC figures...")
    plot_microstrip_cpw_comparison()

    # Numerical examples
    run_examples()

    print("\n" + "=" * 72)
    print("All outputs complete.")
    print(f"Figures saved to: {FIG_DIR}/")
    print("=" * 72)

#!/usr/bin/env python3
"""
Collins Ch9 — Solid-State Amplifiers & Oscillators — Example Code

Implements key computations from Collin's 'Foundations for Microwave Engineering'
2nd ed., Chapters 10 (Solid-State Amplifiers), 11 (Parametric Amplifiers),
and 12 (Oscillators and Mixers).

Functions
---------
stability_k_delta(s_params)
    Rollett stability factor K and Delta check (p. 735)
bilateral_conjugate_match(s_params)
    Simultaneous conjugate match for unconditionally stable devices (p. 743)
unilateral_gain_bounds(s_params)
    Unilateral transducer gain and error bound via U (p. 746–747)
constant_gain_circles(s21, s22, g_dB, npoints=361)
    Center and radius of constant operating-power-gain circles (p. 752)
noise_circles(fmin, gamma_opt, rn, nf_dB_list, npoints=361)
    Constant noise figure circles (p. 772)
oscillator_negative_resistance(z_in)
    Oscillation condition: Z_in + Z_L = 0 (p. 855)
varactor_multiplier_efficiency(n, cjo, vj, m, rs, fp)
    Varactor frequency multiplier efficiency (p. 800–825)
verify_collins_ch09()
    Run all examples with test cases and print results.

All functions accept/return NumPy arrays for compatibility with microwave
toolkits like scikit-rf if desired.
"""

import numpy as np
from numpy import abs, conj, sqrt, exp, angle, pi, real, imag

# ─────────────────────────────────────────────────────────────────────
#  9.1  Stability — K-Delta Test  (Collin §10.6, pp. 735–744)
# ─────────────────────────────────────────────────────────────────────

def stability_k_delta(s_params):
    """
    Rollett stability factor K and auxiliary Delta check.

    Parameters
    ----------
    s_params : complex 2×2 array
        S-parameter matrix [[S11, S12], [S21, S22]]

    Returns
    -------
    K : float
        Rollett stability factor (>1 for unconditional stability)
    Delta : complex
        Determinant S11*S22 - S12*S21
    is_unconditionally_stable : bool
        True if K > 1 and |Delta| < 1

    Notes
    -----
    Collin Eq. (10.36), p. 735.
    Both K > 1 AND |Delta| < 1 must hold for unconditional stability.
    """
    s11, s12 = s_params[0, 0], s_params[0, 1]
    s21, s22 = s_params[1, 0], s_params[1, 1]

    Delta = s11 * s22 - s12 * s21

    denom = 2.0 * abs(s12 * s21)
    if denom == 0:
        K = np.inf
    else:
        K = (1.0 - abs(s11)**2 - abs(s22)**2 + abs(Delta)**2) / denom

    is_stable = (K > 1.0 + 1e-12) and (abs(Delta) < 1.0 - 1e-12)
    return K, Delta, is_stable


# ─────────────────────────────────────────────────────────────────────
#  9.1  Bilateral Conjugate Match  (Collin §10.4–10.5, pp. 726–743)
# ─────────────────────────────────────────────────────────────────────

def bilateral_conjugate_match(s_params):
    """
    Simultaneous conjugate-match source/load terminations for
    unconditionally stable two-ports.  (Collin Eq. 10.48, p. 743)

    Parameters
    ----------
    s_params : complex 2×2 array
        S-parameter matrix

    Returns
    -------
    Gamma_MS : complex
        Source reflection coefficient for conjugate match
    Gamma_ML : complex
        Load reflection coefficient for conjugate match
    G_Tmax_dB : float
        Maximum transducer gain in dB
    K : float
        Stability factor (validates unconditional stability)

    Raises
    ------
    ValueError
        If the device is not unconditionally stable.

    Notes
    -----
    Uses the formulas:
      Gamma_MS = (B1 ± sqrt(B1^2 - 4|C1|^2)) / (2 C1)
      Gamma_ML = (B2 ± sqrt(B2^2 - 4|C2|^2)) / (2 C2)
    where the minus sign is taken for |B1/2C1| > 1 when |C1|,|C2| != 0.
    """
    s11, s12 = s_params[0, 0], s_params[0, 1]
    s21, s22 = s_params[1, 0], s_params[1, 1]

    K, Delta, stable = stability_k_delta(s_params)
    if not stable:
        raise ValueError(
            f"Device not unconditionally stable: K={K:.4f}, |D|={abs(Delta):.4f}"
        )

    C1 = s11 - Delta * conj(s22)
    C2 = s22 - Delta * conj(s11)
    B1 = 1.0 + abs(s11)**2 - abs(s22)**2 - abs(Delta)**2
    B2 = 1.0 + abs(s22)**2 - abs(s11)**2 - abs(Delta)**2

    # Chose sign so that |Gamma_MS| < 1
    Gam_MS = (B1 - sqrt(B1**2 - 4.0 * abs(C1)**2)) / (2.0 * C1 + 1e-30)
    if abs(Gam_MS) >= 1.0:
        Gam_MS = (B1 + sqrt(B1**2 - 4.0 * abs(C1)**2)) / (2.0 * C1 + 1e-30)

    Gam_ML = (B2 - sqrt(B2**2 - 4.0 * abs(C2)**2)) / (2.0 * C2 + 1e-30)
    if abs(Gam_ML) >= 1.0:
        Gam_ML = (B2 + sqrt(B2**2 - 4.0 * abs(C2)**2)) / (2.0 * C2 + 1e-30)

    # Maximum Available Gain (Collin Eq. 10.44, p. 743)
    G_Tmax = abs(s21 / s12) * (K - sqrt(K**2 - 1.0))
    G_Tmax_dB = 10.0 * np.log10(G_Tmax)

    return Gam_MS, Gam_ML, G_Tmax_dB, K


# ─────────────────────────────────────────────────────────────────────
#  9.2  Unilateral Gain & Error Bound  (Collin §10.7, pp. 746–748)
# ─────────────────────────────────────────────────────────────────────

def unilateral_gain_bounds(s_params):
    """
    Unilateral transducer gain and error bound.

    Parameters
    ----------
    s_params : complex 2×2 array
        S-parameter matrix

    Returns
    -------
    result : dict with keys:
        G_TU_max_dB   — maximum unilateral gain (S12=0 assumed)
        G_S_max_dB    — input mismatch gain
        G_0_dB        — |S21|^2 in dB
        G_L_max_dB    — output mismatch gain
        U             — unilateral figure of merit
        error_low_dB  — lower error bound (dB)
        error_high_dB — upper error bound (dB)

    Notes
    -----
    Collin Eq. (10.52)–(10.55), pp. 746–747.
    """
    s11, s12 = s_params[0, 0], s_params[0, 1]
    s21, s22 = s_params[1, 0], s_params[1, 1]

    G_0 = abs(s21)**2
    G_S_max = 1.0 / (1.0 - abs(s11)**2)
    G_L_max = 1.0 / (1.0 - abs(s22)**2)

    G_TU_max = G_0 * G_S_max * G_L_max

    # Unilateral figure of merit  (Eq. 10.54)
    U = (abs(s12) * abs(s21) * abs(s11) * abs(s22)
         / ((1.0 - abs(s11)**2) * (1.0 - abs(s22)**2)))

    # Error bound  (Eq. 10.55)
    error_low = 1.0 / (1.0 + U)**2
    error_high = 1.0 / (1.0 - U)**2

    return {
        "G_TU_max_dB": 10.0 * np.log10(G_TU_max),
        "G_S_max_dB": 10.0 * np.log10(G_S_max),
        "G_0_dB": 10.0 * np.log10(G_0),
        "G_L_max_dB": 10.0 * np.log10(G_L_max),
        "U": U,
        "error_low_dB": 10.0 * np.log10(error_low),
        "error_high_dB": 10.0 * np.log10(error_high),
    }


# ─────────────────────────────────────────────────────────────────────
#  9.2  Constant Gain Circles  (Collin §10.7, pp. 752–753)
# ─────────────────────────────────────────────────────────────────────

def constant_gain_circles(s21, s22, g_dB, npoints=361):
    """
    Compute constant operating-power-gain circle in Gamma_L plane.

    Parameters
    ----------
    s21 : complex
        Forward transmission S-parameter
    s22 : complex
        Output reflection S-parameter
    g_dB : float
        Desired operating power gain in dB
    npoints : int
        Number of points on the circle (default 361)

    Returns
    -------
    Gamma_L_pts : (npoints,) complex array
        Points on the constant gain circle in Gamma_L plane
    center : complex
        Center of the gain circle
    radius : float
        Radius of the gain circle

    Notes
    -----
    Collin Eq. (10.63)–(10.65), p. 752.
    Normalized gain: g = G_P / |S21|^2.
    """
    G_P = 10.0 ** (g_dB / 10.0)
    g = G_P / abs(s21)**2

    denom = 1.0 + g * (abs(s22)**2 - 1.0)
    if abs(denom) < 1e-15:
        raise ValueError("Denominator zero (circle at infinity)")

    center = g * conj(s22) / denom

    radicand = 1.0 - g * (1.0 - abs(s22)**2)
    if radicand < 0:
        raise ValueError(
            f"G_P = {g_dB} dB not achievable (radicand={radicand:.4f} < 0)"
        )
    radius = sqrt(radicand) / abs(denom)

    theta = np.linspace(0, 2 * pi, npoints)
    Gamma_L_pts = center + radius * exp(1j * theta)
    return Gamma_L_pts, center, radius


def unilateral_gain_circles(s11, g_s_dB, npoints=361):
    """
    Compute constant G_S circle in Gamma_S plane (unilateral approx).

    Parameters
    ----------
    s11 : complex
        Input reflection S-parameter
    g_s_dB : float
        Desired G_S value in dB (G_S = (1-|Gamma_S|^2) / |1-s11*Gamma_S|^2)
    npoints : int
        Number of points on the circle (default 361)

    Returns
    -------
    Gamma_S_pts : (npoints,) complex array
        Points on the circle
    center : complex
        Center of the circle
    radius : float

    Notes
    -----
    Normalized gain: g_s = G_S / (1 / (1-|S11|^2))
    """
    G_S_max = 1.0 / (1.0 - abs(s11)**2)
    G_S = 10.0 ** (g_s_dB / 10.0)
    g_s = G_S / G_S_max  # normalized

    denom = 1.0 + g_s * (abs(s11)**2 - 1.0)
    center = g_s * conj(s11) / denom
    radicand = 1.0 - g_s * (1.0 - abs(s11)**2)
    if radicand < 0:
        raise ValueError(
            f"G_S = {g_s_dB} dB not achievable (radicand={radicand:.4f} < 0)"
        )
    radius = sqrt(radicand) / abs(denom)

    theta = np.linspace(0, 2 * pi, npoints)
    Gamma_S_pts = center + radius * exp(1j * theta)
    return Gamma_S_pts, center, radius


# ─────────────────────────────────────────────────────────────────────
#  9.3  Noise Circles  (Collin §10.9, pp. 770–774)
# ─────────────────────────────────────────────────────────────────────

def noise_circles(fmin, gamma_opt, rn, nf_dB_list, npoints=361):
    """
    Compute constant noise-figure circles in Gamma_S plane.

    Parameters
    ----------
    fmin : float
        Minimum noise figure F_min (linear, NOT in dB)
    gamma_opt : complex
        Optimal source reflection coefficient for F_min
    rn : float
        Equivalent noise resistance R_n (in ohms)
    nf_dB_list : list of float
        Desired noise figure values in dB

    Returns
    -------
    circles : list of dict
        Each dict has keys: 'nf_dB', 'center' (complex), 'radius' (float),
        'points' (complex array of circle points, or None if radius > 1)

    Notes
    -----
    Collin Eq. (10.97)–(10.99), p. 772.
    Uses Smith chart normalization: R_n / Z_0.
    The points array is None if the circle extends beyond |Gamma| <= 1
    for the entire locus (radius > 1 and not contained).
    """
    Z0 = 50.0  # standard reference
    circles = []

    for nf_dB in nf_dB_list:
        F_k = 10.0 ** (nf_dB / 10.0)  # convert dB to linear
        N = (F_k - fmin) / (4.0 * rn / Z0) * abs(1.0 + gamma_opt)**2

        center = gamma_opt / (1.0 + N)
        radicand = N * (N + 1.0 - abs(gamma_opt)**2)
        radius = sqrt(max(0.0, radicand)) / (1.0 + N)

        if radius > 1.0 and abs(center) + radius > 1.0:
            # Circle extends beyond unit circle — may be partially valid
            pts = None
        else:
            theta = np.linspace(0, 2 * pi, npoints)
            pts = center + radius * exp(1j * theta)

        circles.append({
            "nf_dB": nf_dB,
            "center": center,
            "radius": radius,
            "points": pts,
        })

    return circles


# ─────────────────────────────────────────────────────────────────────
#  9.4  Oscillator Negative-Resistance Design  (Collin §12, pp. 854–856)
# ─────────────────────────────────────────────────────────────────────

def oscillator_negative_resistance(z_in, Z0=50.0):
    """
    Design a load impedance for oscillation from a one-port negative
    resistance device.

    Parameters
    ----------
    z_in : complex
        Input impedance of the active device (Z_in = R_in + jX_in, R_in < 0)
    Z0 : float
        Reference impedance (default 50 ohms)

    Returns
    -------
    result : dict
        Gamma_load   — load reflection coefficient
        Gamma_in     — device reflection coefficient
        Z_load       — required load impedance (series resonance)
        Gamma_in_mag — |Gamma_in| (must be > 1 for oscillation)
        margin       — fractional margin above 1 (typically 10-20%)
        start_up_ok  — True if |Gamma_in| > 1 (start-up condition satisfied)

    Notes
    -----
    Oscillation condition: Z_in + Z_load = 0  (Collin Eq. 12.39, p. 855).
    For start-up, we need |Gamma_in| > 1 so the overall circuit has
    negative resistance. The load is chosen as R_L = -R_in/3 for
    maximum power transfer.
    """
    R_in = real(z_in)
    X_in = imag(z_in)

    if R_in >= 0:
        raise ValueError(f"Device resistance must be negative. Got R_in={R_in:.3f}")

    # Optimal load for maximum power: R_L = -R_in / 3, X_L = -X_in
    R_L = -R_in / 3.0
    X_L = -X_in
    Z_load = R_L + 1j * X_L

    # Reflection coefficients
    Gamma_load = (Z_load - Z0) / (Z_load + Z0)
    Gamma_in = (z_in - Z0) / (z_in + Z0)

    gamma_mag = abs(Gamma_in)
    margin = gamma_mag - 1.0
    start_up_ok = gamma_mag > 1.0

    return {
        "Gamma_load": Gamma_load,
        "Gamma_in": Gamma_in,
        "Z_load": Z_load,
        "Gamma_in_mag": gamma_mag,
        "margin": margin,
        "start_up_ok": start_up_ok,
    }


# ─────────────────────────────────────────────────────────────────────
#  9.5  Varactor Multiplier / Parametric Amplifier  (Collin §11, pp. 799–830)
# ─────────────────────────────────────────────────────────────────────

def varactor_junction_cap(v_bias, cjo=1e-12, vj=0.7, m=0.5):
    """
    Varactor junction capacitance (Collin Eq. 11.1, p. 800).

    Parameters
    ----------
    v_bias : float
        Reverse bias voltage (positive)
    cjo : float
        Zero-bias capacitance (F), default 1 pF
    vj : float
        Built-in potential (V), default 0.7 V
    m : float
        Grading coefficient: 0.5 (abrupt), 1/3 (graded)

    Returns
    -------
    Cj : float
        Junction capacitance (F)
    """
    return cjo / (1.0 + v_bias / vj) ** m


def varactor_cutoff_frequency(cjo, rs, f_max=1e12):
    """
    Varactor cutoff frequency (p. 801).

    fc = 1 / (2 * pi * Rs * Cj0)

    Parameters
    ----------
    cjo : float
        Zero-bias junction capacitance (F)
    rs : float
        Series resistance (ohms)
    f_max : float
        Upper bound to avoid division by zero

    Returns
    -------
    fc : float
        Cutoff frequency (Hz)
    """
    if cjo <= 0 or rs <= 0:
        return f_max
    return 1.0 / (2.0 * pi * rs * cjo)


def varactor_multiplier_efficiency(n, fp, cjo, rs=2.0, vj=0.7, m=0.5,
                                    v_bias=5.0, f_max=1e12):
    """
    Estimate varactor frequency multiplier efficiency.

    Parameters
    ----------
    n : int
        Multiplication factor (e.g., 2 for doubler, 3 for tripler)
    fp : float
        Pump (input) frequency (Hz)
    cjo : float
        Zero-bias capacitance (F)
    rs : float
        Series resistance (ohms), default 2.0
    vj : float
        Built-in potential (V), default 0.7 V
    m : float
        Grading coefficient, default 0.5
    v_bias : float
        Reverse bias voltage (V), default 5.0
    f_max : float
        Upper bound for cutoff if cjo*rs = 0

    Returns
    -------
    result : dict
        fc           — cutoff frequency (Hz)
        Cj           — bias-dependent junction capacitance (F)
        Q            — quality factor at pump frequency
        eta_max      — maximum theoretical efficiency (ideal)
        eta_practical — practical efficiency (estimated)

    Notes
    -----
    For an abrupt-junction varactor (m=0.5), the maximum efficiency
    of an nth-order multiplier is approximately:
      eta_n ≈ 1/n^2  (ideal lossless case)

    In practice, efficiency is limited by:
      - Series resistance (Q factor)
      - Junction losses
      - Circuit losses

    Ref: Collin §11; also Penfield & Rafuse, Varactor Applications, MIT Press 1962.
    """
    Cj = varactor_junction_cap(v_bias, cjo, vj, m)
    fc = varactor_cutoff_frequency(cjo, rs, f_max)

    Q = fc / fp

    # Ideal efficiency bound for abrupt-junction
    eta_ideal = 1.0 / (n ** 2)

    # Practical efficiency accounting for resistive losses
    # Higher-order multipliers are more sensitive to Q
    Q_factor = (1.0 - np.exp(-2.0 * pi * Q / n)) if Q > 0 else 0.0
    eta_practical = eta_ideal * min(1.0, Q_factor)

    return {
        "fc_Hz": fc,
        "Cj_F": Cj,
        "Q": Q,
        "eta_max": eta_ideal,
        "eta_practical": eta_practical,
    }


# ─────────────────────────────────────────────────────────────────────
#  9.5  Parametric Amplifier — Gain (Collin §11.5, pp. 821–829)
# ─────────────────────────────────────────────────────────────────────

def parametric_amplifier_gain(f_signal, f_pump, c_ratio, rs, r_idler,
                               r_load=50.0):
    """
    Signal gain of a negative-resistance parametric amplifier
    (simplified model).

    Parameters
    ----------
    f_signal : float
        Signal frequency (Hz)
    f_pump : float
        Pump frequency (Hz)
    c_ratio : float
        Capacitance modulation ratio C1/C0 (typical 0.1–0.3)
    rs : float
        Varactor series resistance (ohms)
    r_idler : float
        Idler circuit loss resistance (ohms)
    r_load : float
        Load resistance (ohms), default 50

    Returns
    -------
    result : dict
        f_idler     — idler frequency f_i = f_p - f_s (Hz)
        M           — modulation index = C1 / (2*C0)
        R_neg       — negative resistance (ohms)
        G_S         — signal power gain (linear)
        G_S_dB      — signal power gain (dB)

    Notes
    -----
    Simplified model based on Collin's treatment of the negative-resistance
    parametric amplifier (Eq. 11.54, p. 821).
    The idler frequency is: f_i = f_p - f_s.
    Negative resistance: R_neg = -M^2 / (omega_s * omega_i * r_idler * C_j^2)
    """
    f_idler = f_pump - f_signal
    if f_idler <= 0:
        raise ValueError("Idler frequency must be positive. "
                         f"Got f_p={f_pump}, f_s={f_signal}")

    omega_s = 2.0 * pi * f_signal
    omega_i = 2.0 * pi * f_idler
    M = c_ratio / 2.0  # modulation index

    # Negative resistance (simplified expression)
    # Negative resistance for varactor paramp (F_{neg} = -M^2 / ω_s ω_i C_j^2 R_{idler})
    Cj_typical = 0.5e-12
    R_neg = -M**2 / (omega_s * omega_i * r_idler * Cj_typical**2)

    if R_neg >= 0:
        return {
            "f_idler": f_idler,
            "M": M,
            "R_neg": R_neg,
            "G_S": 0.0,
            "G_S_dB": -np.inf,
        }

    # Signal gain (from reflection-type paramp)
    # G_S = ((R_L - |R_neg|) / (R_L + R_s - |R_neg|))^2
    # For a simplified model, assume total circuit loss ~ Rs
    R_neg_abs = abs(R_neg)
    if r_load + rs <= R_neg_abs:
        G_S = np.inf  # oscillation
    else:
        G_S = ((r_load - R_neg_abs) / (r_load + rs - R_neg_abs))**2

    G_S_dB = 10.0 * np.log10(G_S) if G_S > 0 else -np.inf

    return {
        "f_idler": f_idler,
        "M": M,
        "R_neg": R_neg,
        "G_S": G_S,
        "G_S_dB": G_S_dB,
    }


# ─────────────────────────────────────────────────────────────────────
#  9.5  Manley-Rowe Relations  (Collin §11.2, pp. 807–809)
# ─────────────────────────────────────────────────────────────────────

def manley_rowe_upconverter(f_signal, f_pump, P_pump, P_signal_in=1e-3):
    """
    Compute power flows for an ideal parametric up-converter using
    Manley-Rowe relations.

    The up-converter produces output at f_o = f_p + f_s.
    An idler at f_i = f_p - f_s circulates in a resonant circuit.

    Sign convention: power flowing INTO the nonlinear reactance is +.
    Pump power is supplied (+), signal is supplied (+),
    output power flows out (-), idler may flow either way.

    Parameters
    ----------
    f_signal : float
        Signal frequency (Hz)
    f_pump : float
        Pump frequency (Hz)
    P_pump : float
        Pump power delivered to the varactor (W)
    P_signal_in : float
        Input signal power (W), default 1 mW

    Returns
    -------
    result : dict
        f_idler    — idler frequency (Hz)
        f_out      — output frequency (Hz)
        P_idler    — power at idler (W, + into varactor)
        P_signal   — net signal power (W, + into varactor)
        P_out      — output power (W, |value| delivered to load)
        gain_dB    — power gain in dB (P_out / P_signal_in)

    Notes
    -----
    Manley-Rowe relations (Collin Eq. 11.21, p. 807):
      Σ m·P_mn / (m·f_p + n·f_s) = 0
      Σ n·P_mn / (m·f_p + n·f_s) = 0

    For (1,0) pump, (0,1) signal, (1,1) output, (-1,1) idler:
      P_p/f_p + P_o/f_o - P_i/f_i = 0          ...(A)
      P_s/f_s + P_o/f_o + P_i/f_i = 0          ...(B)

    The idler power P_i is determined by circuit reactance—assume
    it takes half the available energy as a heuristic here.
    """
    import warnings

    f_idler = f_pump - f_signal
    f_out = f_pump + f_signal

    if f_idler <= 0:
        raise ValueError(f"Idler freq {f_idler/1e9:.2f} GHz <= 0 — degenerate case")

    # Solve Manley-Rowe: from (A) and (B):
    #   P_i = (P_p/f_p - P_s/f_s) / (2/f_i)  → P_i = (f_i/2)(P_p/f_p - P_s/f_s)
    #   P_o = -f_o(P_s/f_s + P_i/f_i)
    P_s = P_signal_in  # positive: signal power into varactor
    P_i = (f_idler / 2.0) * (P_pump / f_pump - P_s / f_signal)
    P_o = -f_out * (P_s / f_signal + P_i / f_idler)

    gain = abs(P_o) / P_signal_in if P_signal_in > 0 else 0.0
    gain_dB = 10.0 * np.log10(gain) if gain > 0 else -np.inf

    return {
        "f_idler": f_idler,
        "f_out": f_out,
        "P_idler": P_i,
        "P_signal": P_s,
        "P_out": abs(P_o),
        "gain_dB": gain_dB,
    }


# ─────────────────────────────────────────────────────────────────────
#  9.6  Balanced Amplifier  (Collin §10.11, pp. 778–780)
# ─────────────────────────────────────────────────────────────────────

def balanced_amplifier_gain(G_amp_dB, hybrid_loss_dB=0.3):
    """
    Overall gain of a balanced amplifier using two quadrature hybrids.

    Parameters
    ----------
    G_amp_dB : float
        Gain of each single amplifier (dB)
    hybrid_loss_dB : float
        Insertion loss of each hybrid (dB), default 0.3

    Returns
    -------
    G_total_dB : float
        Overall gain (dB)
    """
    return G_amp_dB - 2 * hybrid_loss_dB


def balanced_amplifier_vswr(gamma_1, gamma_2):
    """
    Input return loss improvement in a balanced amplifier.

    For identical amplifiers with identical reflection coefficients,
    the reflections cancel at the input port due to the hybrid.

    Parameters
    ----------
    gamma_1 : complex
        Input reflection coefficient of amplifier 1
    gamma_2 : complex
        Input reflection coefficient of amplifier 2

    Returns
    -------
    Gamma_total : complex
        Overall input reflection coefficient
    VSWR : float
        Overall VSWR
    """
    Gamma_total = 0.5 * (gamma_1 - gamma_2)
    VSWR = (1.0 + abs(Gamma_total)) / (1.0 - abs(Gamma_total))
    return Gamma_total, VSWR


# ─────────────────────────────────────────────────────────────────────
#  9.6  Distributed Amplifier  (Collin §10.11, pp. 780–785)
# ─────────────────────────────────────────────────────────────────────

def distributed_amplifier_gain(n_stages, gm, Z0g, Z0d):
    """
    Forward gain of an ideal distributed amplifier.

    Parameters
    ----------
    n_stages : int
        Number of transistors
    gm : float
        Transconductance (S)
    Z0g : float
        Characteristic impedance of gate line (ohms)
    Z0d : float
        Characteristic impedance of drain line (ohms)

    Returns
    -------
    G_linear : float
        Voltage gain (linear)
    G_dB : float
        Power gain (dB)
    """
    G_linear = 0.5 * n_stages * gm * sqrt(Z0g * Z0d)
    G_dB = 20.0 * np.log10(G_linear)
    return G_linear, G_dB


def distributed_amplifier_cutoff(cgs, L_section):
    """
    Cutoff frequency of the gate artificial transmission line.

    Parameters
    ----------
    cgs : float
        Gate-source capacitance (F)
    L_section : float
        Inductance per section (H)

    Returns
    -------
    fc : float
        Cutoff frequency (Hz)
    """
    return 1.0 / (pi * sqrt(L_section * cgs))


# ─────────────────────────────────────────────────────────────────────
#  Verification Suite
# ─────────────────────────────────────────────────────────────────────

def verify_collins_ch09():
    """
    Run all examples with test data and print results.

    Test transistor (NE71000 like, at 4 GHz):
      S11 = 0.75 ∠ -120°,  S12 = 0.10 ∠ 40°
      S21 = 3.50 ∠ 70°,    S22 = 0.45 ∠ -30°
    """
    print("=" * 70)
    print("Collins Ch9 — Solid-State Amplifiers & Oscillators — Verification")
    print("=" * 70)

    # ── Test S-parameters (NE71000 at 4 GHz, illustrative) ──
    s11 = 0.75 * exp(1j * np.radians(-120))
    s12 = 0.10 * exp(1j * np.radians(40))
    s21 = 3.50 * exp(1j * np.radians(70))
    s22 = 0.45 * exp(1j * np.radians(-30))

    s_params = np.array([[s11, s12], [s21, s22]], dtype=complex)

    print(f"\nTest S-parameters (4 GHz illustrative):")
    print(f"  S11 = {s11:.4f}")
    print(f"  S12 = {s12:.4f}")
    print(f"  S21 = {s21:.4f}  |S21|² = {abs(s21)**2:.2f} ({10*np.log10(abs(s21)**2):.2f} dB)")
    print(f"  S22 = {s22:.4f}")

    # ── 9.1 Stability ──
    print("\n" + "-" * 70)
    print("9.1: Stability K-Delta Test  [p. 735]")
    K, Delta, stable = stability_k_delta(s_params)
    print(f"  K     = {K:.4f}")
    print(f"  |Δ|   = {abs(Delta):.4f}")
    print(f"  Unconditionally stable: {stable}")
    if not stable:
        print("  → Device is conditionally stable; stability circles needed.")

    # ── 9.1 Bilateral conjugate match ──
    print("\n" + "-" * 70)
    print("9.1: Bilateral Conjugate Match  [p. 743]")
    if stable:
        Gam_MS, Gam_ML, G_Tmax_dB, _ = bilateral_conjugate_match(s_params)
        print(f"  Γ_MS   = {Gam_MS:.4f}")
        print(f"  Γ_ML   = {Gam_ML:.4f}")
        print(f"  G_Tmax = {G_Tmax_dB:.2f} dB")
    else:
        print("  (Skip — device not unconditionally stable)")

    # ── 9.2 Unilateral gain bounds ──
    print("\n" + "-" * 70)
    print("9.2: Unilateral Gain & Error Bound  [pp. 746–747]")
    ub = unilateral_gain_bounds(s_params)
    print(f"  G₀     = {ub['G_0_dB']:.2f} dB")
    print(f"  G_Smax = {ub['G_S_max_dB']:.2f} dB")
    print(f"  G_Lmax = {ub['G_L_max_dB']:.2f} dB")
    print(f"  G_TUmax = {ub['G_TU_max_dB']:.2f} dB")
    print(f"  U (figure of merit) = {ub['U']:.4f}")
    if ub['U'] < 0.1:
        print(f"  → Unilateral approx valid (U << 1)")
    else:
        print(f"  → Bilateral design required (U not negligible)")
    print(f"  Error bound: [{ub['error_low_dB']:.2f}, {ub['error_high_dB']:.2f}] dB")

    # ── 9.2 Constant gain circles ──
    print("\n" + "-" * 70)
    print("9.2: Constant Gain Circles  [p. 752]")
    for g_target in [10.0, 12.0, 14.0]:
        try:
            pts, center, radius = constant_gain_circles(s21, s22, g_target)
            print(f"  G_P = {g_target} dB: center={center:.4f}, "
                  f"radius={radius:.4f}")
        except ValueError as e:
            print(f"  G_P = {g_target} dB: {e}")
    # Unilateral circles
    for g_target in [0.5, 1.0, 1.5]:
        ub_gs = unilateral_gain_bounds(s_params)
        gs_target = ub_gs["G_S_max_dB"] - g_target
        try:
            pts, center, radius = unilateral_gain_circles(s11, gs_target)
            print(f"  Unilateral G_S = {gs_target:.1f} dB: "
                  f"center={center:.4f}, radius={radius:.4f}")
        except Exception as e:
            print(f"  Unilateral G_S = {gs_target:.1f} dB: {e}")

    # ── 9.3 Noise circles ──
    print("\n" + "-" * 70)
    print("9.3: Noise Circles & NF Optimization  [pp. 770–774]")
    F_min_lin = 1.5    # F_min = 1.5  (linear, ≈ 1.76 dB)
    Gamma_opt = 0.5 * exp(1j * np.radians(90))  # optimal Γ
    R_n = 10.0          # ohms
    nf_targets = [1.76, 2.0, 2.5, 3.0, 4.0]
    circles = noise_circles(F_min_lin, Gamma_opt, R_n, nf_targets)
    print(f"  F_min = {10*np.log10(F_min_lin):.2f} dB, "
          f"Γ_opt = {Gamma_opt:.4f}, R_n = {R_n} Ω")
    for c in circles:
        nf_text = f"{c['nf_dB']:.2f} dB"
        status = "valid" if c["points"] is not None else "extends beyond Γ≤1"
        print(f"  NF={nf_text}: center={c['center']:.4f}, "
              f"radius={c['radius']:.4f} [{status}]")

    # ── 9.4 Oscillator ──
    print("\n" + "-" * 70)
    print("9.4: Oscillator Negative-Resistance Design  [p. 855]")
    # Example: device with negative input impedance
    Z_in_neg = -30.0 + 1j * 20.0  # ohms (R_in < 0)
    print(f"  Device Z_in = {Z_in_neg:.1f} Ω")
    osc = oscillator_negative_resistance(Z_in_neg)
    print(f"  Required Z_L = {osc['Z_load']:.1f} Ω")
    print(f"  Γ_in        = {osc['Gamma_in']:.4f}")
    print(f"  |Γ_in|      = {osc['Gamma_in_mag']:.4f} (>1 → start-up OK)")
    print(f"  Γ_load      = {osc['Gamma_load']:.4f}")
    print(f"  Start-up condition met: {osc['start_up_ok']}")

    # ── 9.5 Varactor multiplier ──
    print("\n" + "-" * 70)
    print("9.5: Varactor Frequency Multiplier  [pp. 800–825]")
    vm = varactor_multiplier_efficiency(n=2, fp=4e9, cjo=1e-12, rs=2.0)
    print(f"  Doubler (n=2):")
    print(f"    fc = {vm['fc_Hz']/1e9:.2f} GHz,  Cj = {vm['Cj_F']*1e12:.2f} pF")
    print(f"    Q  = {vm['Q']:.1f}")
    print(f"    η_max       = {vm['eta_max']*100:.1f}%")
    print(f"    η_practical = {vm['eta_practical']*100:.1f}%")
    vm3 = varactor_multiplier_efficiency(n=3, fp=4e9, cjo=1e-12, rs=2.0)
    print(f"  Tripler (n=3):")
    print(f"    η_max       = {vm3['eta_max']*100:.1f}%")
    print(f"    η_practical = {vm3['eta_practical']*100:.1f}%")

    # ── 9.5 Parametric amplifier ──
    print("\n" + "-" * 70)
    print("9.5: Parametric Amplifier (Negative-Resistance)  [pp. 821–829]")
    # Tuned modulation index for positive gain without oscillation
    paramp = parametric_amplifier_gain(
        f_signal=4e9, f_pump=10e9,
        c_ratio=0.25, rs=2.0, r_idler=5.0, r_load=50.0
    )
    print(f"  f_idler  = {paramp['f_idler']/1e9:.2f} GHz")
    print(f"  M        = {paramp['M']:.3f}")
    print(f"  R_neg    = {paramp['R_neg']:.1f} Ω")
    if np.isfinite(paramp['G_S_dB']):
        print(f"  G_S      = {paramp['G_S_dB']:.1f} dB")
    else:
        print(f"  G_S      = oscillating (|R_neg| <= r_load + rs)")

    # ── 9.5 Manley-Rowe ──
    print("\n" + "-" * 70)
    print("9.5: Manley-Rowe Up-Converter  [pp. 807–809]")
    mr = manley_rowe_upconverter(f_signal=4e9, f_pump=10e9, P_pump=0.01, P_signal_in=1e-3)
    print(f"  f_idler  = {mr['f_idler']/1e9:.1f} GHz")
    print(f"  f_out    = {mr['f_out']/1e9:.1f} GHz")
    print(f"  P_pump   = 10.0 mW")
    print(f"  P_signal = {mr['P_signal']*1000:.2f} mW (input)")
    print(f"  P_idler  = {mr['P_idler']*1000:.2f} mW")
    print(f"  P_out    = {mr['P_out']*1000:.2f} mW")
    print(f"  Gain     = {mr['gain_dB']:.1f} dB")

    # ── 9.6 Balanced amplifier ──
    print("\n" + "-" * 70)
    print("9.6: Balanced Amplifier  [p. 778]")
    G_total = balanced_amplifier_gain(12.0, 0.3)
    print(f"  Single amp gain  = 12.0 dB")
    print(f"  Hybrid loss (×2) = 0.6 dB")
    print(f"  Total gain       = {G_total:.2f} dB")
    # VSWR improvement
    Gamma_t, vswr = balanced_amplifier_vswr(0.3 * exp(1j*0.5), 0.28 * exp(1j*0.6))
    print(f"  With slightly mismatched amplifiers:")
    print(f"    Γ_total = {Gamma_t:.4f}, VSWR = {vswr:.3f}")

    # ── 9.6 Distributed amplifier ──
    print("\n" + "-" * 70)
    print("9.6: Distributed Amplifier  [pp. 780–785]")
    G_lin, G_db = distributed_amplifier_gain(4, 50e-3, 50, 50)
    print(f"  4 stages, gm = 50 mS, Z0g = Z0d = 50 Ω")
    print(f"  Gain (linear) = {G_lin:.2f}")
    print(f"  Gain (dB)     = {G_db:.2f} dB")
    fc = distributed_amplifier_cutoff(0.5e-12, 0.5e-9)
    print(f"  Gate line fc  = {fc/1e9:.2f} GHz (Cgs=0.5pF, L=0.5nH)")

    # ── Summary ──
    print("\n" + "=" * 70)
    print("Verification complete. All 7+ functions executed.")
    print("=" * 70)
    return True


# ─────────────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    verify_collins_ch09()

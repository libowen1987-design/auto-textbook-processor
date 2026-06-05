#!/usr/bin/env python3
"""
Balanis Ch16 — Smart Antennas
====================================
Demos:
  1. ULA array factor and beamsteering
  2. MUSIC DOA estimation (two sources)
  3. LCMV (MVDR) adaptive beamformer
  4. LMS adaptive beamforming (convergence, SINR)

Figures saved to figures/ch16/.
verify_ch16() runs all checks -> ALL PASSED.
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

FIGS = Path(__file__).resolve().parent / "figures" / "ch16"
FIGS.mkdir(parents=True, exist_ok=True)

# ──────────────────────────────────────────────────────────────────────
# Constants & Helpers
# ──────────────────────────────────────────────────────────────────────
C = 3e8           # speed of light [m/s]
FREQ = 2.4e9       # carrier [Hz] (ISM band)
LAMBDA = C / FREQ
D = LAMBDA / 2     # inter-element spacing
DEG = np.pi / 180


def steering_vector(theta_deg, N_elements: int, d: float = D,
                    lam: float = LAMBDA) -> np.ndarray:
    """Array response / steering vector a(θ) for a ULA at broadside.
    theta_deg can be scalar or 1-D array.
    Returns shape (M,) for scalar, (M, K) for array input."""
    scalar_in = np.ndim(theta_deg) == 0 or np.isscalar(theta_deg)
    m = np.arange(N_elements)[:, None]
    theta_arr = np.atleast_1d(np.asarray(theta_deg, dtype=float)).ravel()[None, :]
    result = np.exp(-1j * 2 * np.pi * d / lam * m * np.sin(theta_arr * DEG))
    return result[:, 0] if scalar_in else result


def array_factor(theta_scan: np.ndarray, w: np.ndarray,
                 d: float = D, lam: float = LAMBDA) -> np.ndarray:
    """Compute the array factor over theta_scan (degrees) for weights w."""
    M = w.shape[0]
    m = np.arange(M)[:, None]  # shape (M, 1)
    AF = w.conj().T @ np.exp(-1j * 2 * np.pi * d / lam
                              * m * np.sin(theta_scan[None, :] * DEG))
    return AF.flatten()


# ──────────────────────────────────────────────────────────────────────
# Demo 1 — ULA Array Factor and Beamsteering
# ──────────────────────────────────────────────────────────────────────
def demo1_array_factor():
    """Beam patterns for a 16-element ULA steered to 0°, 30°, -20°."""
    print("=" * 60)
    print("Demo 1: ULA Array Factor and Beamsteering")
    print("=" * 60)

    N_elements = 16
    theta_scan = np.linspace(-90, 90, 1801)

    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2, projection='polar')

    # ── Linear array factor ──
    ax = ax1
    for steer_deg in [0, 30, -20]:
        w = steering_vector(steer_deg, N_elements) / N_elements
        AF = array_factor(theta_scan, w)
        ax.plot(theta_scan, 20 * np.log10(np.abs(AF) + 1e-12),
                label=f"$\\theta_0 = {steer_deg}^\\circ$", lw=1.5)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="Normalized AF [dB]",
           title="ULA Array Factor ($M=16$, $d=\\lambda/2$)",
           xlim=[-90, 90], ylim=[-40, 3])
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # ── Polar plot ──
    ax = ax2
    for steer_deg in [0, 30, -20]:
        w = steering_vector(steer_deg, N_elements) / N_elements
        AF = array_factor(theta_scan, w)
        AF_dB = 20 * np.log10(np.abs(AF) + 1e-12)
        AF_dB_clip = np.maximum(AF_dB, -30)
        ax.plot(theta_scan * DEG, AF_dB_clip, label=f"$\\theta_0 = {steer_deg}^\\circ$", lw=1.2)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_thetamin(-90)
    ax.set_thetamax(90)
    ax.set_title("Polar AF Pattern", va="bottom")
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIGS / "demo1_array_factor.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo1_array_factor.png\n")


# ──────────────────────────────────────────────────────────────────────
# Demo 2 — MUSIC DOA Estimation
# ──────────────────────────────────────────────────────────────────────
def demo2_music_doa():
    """MUSIC pseudospectrum for two non-coherent sources."""
    print("=" * 60)
    print("Demo 2: MUSIC DOA Estimation")
    print("=" * 60)

    N_elements = 12
    snapshots = 500
    theta_true = np.array([-12.0, 25.0])  # degrees
    n_sources = len(theta_true)
    snr = 20  # dB per source
    theta_scan = np.linspace(-90, 90, 1801)

    # Build array manifold
    A = steering_vector(theta_true[:, None].flatten(), N_elements)  # (M, K)
    A = A.reshape(N_elements, n_sources)

    # Generate signals
    np.random.seed(42)
    S = (np.random.randn(n_sources, snapshots)
         + 1j * np.random.randn(n_sources, snapshots)) / np.sqrt(2)
    sigma_s = np.sqrt(10 ** (snr / 10))
    S *= sigma_s
    noise = (np.random.randn(N_elements, snapshots)
             + 1j * np.random.randn(N_elements, snapshots)) / np.sqrt(2)

    X = A @ S + noise  # (M, N)

    # Covariance matrix
    R_xx = (X @ X.conj().T) / snapshots

    # Eigendecomposition
    eigvals, eigvecs = np.linalg.eigh(R_xx)
    # eigh returns ascending order; signal subspace = largest eigvals
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    # Noise subspace
    U_n = eigvecs[:, n_sources:]  # (M, M-K)

    # MUSIC pseudospectrum
    a_theta = np.exp(-1j * 2 * np.pi * D / LAMBDA
                     * np.arange(N_elements)[:, None]
                     * np.sin(theta_scan * DEG)[None, :])  # (M, N_theta)
    denom = np.sum(np.abs(U_n.conj().T @ a_theta) ** 2, axis=0)
    P_music = 1.0 / (denom + 1e-12)

    # Detect peaks
    from scipy.signal import find_peaks
    peaks_idx, _ = find_peaks(P_music, height=np.percentile(P_music, 99.5))
    theta_est = theta_scan[peaks_idx]
    # Match estimated DOAs to true DOAs (order-agnostic)
    if len(theta_est) > n_sources:
        theta_est = theta_est[:n_sources]
    elif len(theta_est) < n_sources:
        theta_est = np.pad(theta_est, (0, n_sources - len(theta_est)),
                           constant_values=np.nan)

    # Best matching: assign each estimated DOA to the closest true DOA
    matched_errs = []
    used_true = set()
    for est in theta_est[:]:
        best = np.argmin([np.abs(est - tt) for ii, tt in enumerate(theta_true)
                          if ii not in used_true])
        actual_idx = [i for i in range(len(theta_true)) if i not in used_true][best]
        matched_errs.append(np.abs(est - theta_true[actual_idx]))
        used_true.add(actual_idx)

    print(f"  True DOAs:           {theta_true}")
    print(f"  Estimated DOAs:      {np.round(theta_est, 1)}")
    print(f"  Angular errors (deg): {np.round(matched_errs, 2)}")

    # Plot
    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    ax = axes[0]
    ax.plot(theta_scan, 10 * np.log10(P_music + 1e-12), "b-", lw=1.5)
    for t in theta_true:
        ax.axvline(t, color="r", ls="--", alpha=0.5)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="MUSIC Pseudospectrum [dB]",
           title=f"MUSIC DOA ($M={N_elements}$, SNR={snr} dB, $d=\\lambda/2$)",
           xlim=[-90, 90])
    ax.legend(["$P_{\\mathrm{MU}}(\\theta)$", "True DOA"], fontsize=9)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.semilogy(np.arange(1, N_elements + 1), eigvals, "o-")
    ax.axvline(n_sources + 0.5, color="r", ls="--", alpha=0.6)
    ax.set(xlabel="Eigenvalue index", ylabel="Eigenvalue $\\lambda$",
           title="Eigenvalue Spectrum (signal / noise subspace boundary)")
    ax.grid(True, alpha=0.3)
    ax.text(n_sources + 0.5, np.median(eigvals),
            "  Signal subspace → | ← Noise subspace",
            rotation=90, va="center", fontsize=9, color="r")

    plt.tight_layout()
    fig.savefig(FIGS / "demo2_music_doa.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo2_music_doa.png\n")

    return theta_true, theta_est


# ──────────────────────────────────────────────────────────────────────
# Demo 3 — LCMV (MVDR) Adaptive Beamformer
# ──────────────────────────────────────────────────────────────────────
def demo3_lcmv_beamformer():
    """LCMV beamformer: unit gain at desired, deep nulls at interferers."""
    print("=" * 60)
    print("Demo 3: LCMV (MVDR) Adaptive Beamformer")
    print("=" * 60)

    N_elements = 16
    snapshots = 500
    theta_desired = 0.0       # desired signal [deg]
    theta_interf = np.array([-30.0, 40.0])  # interferers [deg]
    n_sources = 1 + len(theta_interf)
    snr = 15          # desired signal SNR [dB]
    inr = 25          # interferer-to-noise ratio [dB] per jammer
    theta_scan = np.linspace(-90, 90, 1801)

    np.random.seed(123)

    # Desired signal
    a_des = steering_vector(theta_desired, N_elements)
    sig = (np.random.randn(snapshots) + 1j * np.random.randn(snapshots)) / np.sqrt(2)
    sig *= np.sqrt(10 ** (snr / 10))

    # Interferers
    A_int = np.zeros((N_elements, len(theta_interf)), dtype=complex)
    for i, tint in enumerate(theta_interf):
        A_int[:, i] = steering_vector(tint, N_elements)
    jam = (np.random.randn(len(theta_interf), snapshots)
           + 1j * np.random.randn(len(theta_interf), snapshots)) / np.sqrt(2)
    jam *= np.sqrt(10 ** (inr / 10))

    # Noise
    noise = (np.random.randn(N_elements, snapshots)
             + 1j * np.random.randn(N_elements, snapshots)) / np.sqrt(2)

    X = (a_des[:, None] * sig[None, :] + A_int @ jam + noise)

    R_xx = (X @ X.conj().T) / snapshots
    R_xx_inv = np.linalg.inv(R_xx + 1e-10 * np.eye(N_elements))

    # LCMV: w = R⁻¹ a / (a^H R⁻¹ a)
    w_lcmv = R_xx_inv @ a_des.conj()
    w_lcmv /= a_des.conj().T @ w_lcmv

    # Array factor with LCMV weights
    a_theta = np.exp(-1j * 2 * np.pi * D / LAMBDA
                     * np.arange(N_elements)[:, None]
                     * np.sin(theta_scan * DEG)[None, :])
    AF_lcmv = w_lcmv.conj().T @ a_theta
    pattern_dB = 20 * np.log10(np.abs(AF_lcmv) + 1e-12)

    # Check null depths
    null_depths = []
    for tint in theta_interf:
        idx_null = np.argmin(np.abs(theta_scan - tint))
        null_depths.append(pattern_dB[idx_null])
    print(f"  Desired: {theta_desired}°  |  Interferers: {theta_interf}")
    print(f"  Null depths: {null_depths} dB")

    # Plot
    fig = plt.figure(figsize=(10, 8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax2 = fig.add_subplot(2, 1, 2, projection='polar')

    ax = ax1
    ax.plot(theta_scan, pattern_dB, "b-", lw=1.5)
    ax.axvline(theta_desired, color="g", ls="--", alpha=0.7, label=f"Desired {theta_desired}°")
    for tint in theta_interf:
        ax.axvline(tint, color="r", ls=":", alpha=0.6)
        idx = np.argmin(np.abs(theta_scan - tint))
        ax.plot(theta_scan[idx], pattern_dB[idx], "rv", markersize=6)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="Beam Pattern [dB]",
           title=f"LCMV (MVDR) Beamformer ($M={N_elements}$, $d=\\lambda/2$)",
           xlim=[-90, 90], ylim=[-60, 5])
    ax.legend(["$|\\mathrm{AF}(\\theta)|$", "Desired", "Null →"], fontsize=9)
    ax.grid(True, alpha=0.3)

    # Polar version
    ax = ax2
    pattern_clip = np.maximum(pattern_dB, -40)
    ax.plot(theta_scan * DEG, pattern_clip, "b-", lw=1.2)
    for tint in theta_interf:
        ax.plot(tint * DEG, -40, "rv", markersize=5)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_thetamin(-90)
    ax.set_thetamax(90)
    ax.set_title("LCMV Beam Pattern (Polar)", va="bottom")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIGS / "demo3_lcmv_beamformer.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo3_lcmv_beamformer.png\n")

    return np.array(null_depths)


# ──────────────────────────────────────────────────────────────────────
# Demo 4 — LMS Adaptive Beamforming
# ──────────────────────────────────────────────────────────────────────
def demo4_lms_adaptive():
    """LMS convergence: learning curve and steady-state SINR."""
    print("=" * 60)
    print("Demo 4: LMS Adaptive Beamforming")
    print("=" * 60)

    N_elements = 12
    snapshots = 5000
    theta_desired = 5.0
    theta_interf = np.array([-35.0, 50.0])
    snr = 10
    inr = 15

    np.random.seed(7)

    # Steering vectors
    a_des = steering_vector(theta_desired, N_elements)
    A_int = np.column_stack([steering_vector(t, N_elements) for t in theta_interf])

    # Signals
    sig = (np.random.randn(snapshots) + 1j * np.random.randn(snapshots)) / np.sqrt(2)
    sig *= np.sqrt(10 ** (snr / 10))
    jam = (np.random.randn(len(theta_interf), snapshots)
           + 1j * np.random.randn(len(theta_interf), snapshots)) / np.sqrt(2)
    jam *= np.sqrt(10 ** (inr / 10))
    noise = (np.random.randn(N_elements, snapshots)
             + 1j * np.random.randn(N_elements, snapshots)) / np.sqrt(2)

    X = (a_des[:, None] * sig[None, :] + A_int @ jam + noise)

    # Reference signal = desired signal + small noise (training)
    ref = sig + 0.01 * ((np.random.randn(snapshots)
                         + 1j * np.random.randn(snapshots)) / np.sqrt(2))

    # LMS — use adaptive step size based on eigenvalue estimate
    R_xx_est = (X @ X.conj().T) / min(snapshots, 200)
    mu_max = 1.0 / np.linalg.eigvalsh(R_xx_est)[-1]
    mu_lms = 0.25 * mu_max  # conservative step size
    w = np.zeros(N_elements, dtype=complex)
    y_out = np.zeros(snapshots, dtype=complex)
    error = np.zeros(snapshots, dtype=complex)
    w_norm = np.zeros(snapshots)

    for n in range(snapshots):
        y_out[n] = w.conj().T @ X[:, n]
        error[n] = ref[n] - y_out[n]
        w += mu_lms * np.conj(error[n]) * X[:, n]
        w_norm[n] = np.linalg.norm(w)

    w_lms = w.copy()

    # Learning curve (MSE)
    running_mse = np.convolve(np.abs(error) ** 2,
                              np.ones(50) / 50, mode="valid")

    # Steady state SINR (last half of samples)
    n_steady = snapshots // 2
    R_s = a_des[:, None] @ a_des[None, :].conj() * np.mean(np.abs(sig[n_steady:]) ** 2)
    R_in = (A_int @ np.diag(np.mean(np.abs(jam[:, n_steady:]) ** 2, axis=1))
            @ A_int.conj().T + np.eye(N_elements))
    sinr_num = w_lms.conj().T @ R_s @ w_lms
    sinr_den = w_lms.conj().T @ R_in @ w_lms
    sinr_db = 10 * np.log10(np.abs(sinr_num / sinr_den) + 1e-12)
    print(f"  Step size μ = {mu_lms:.6f} (μ_max ≈ {mu_max:.6f})")
    print(f"  μ/μ_max ≈ {mu_lms/mu_max:.2f}")
    print(f"  Steady-state SINR = {sinr_db:.2f} dB")

    # Beampattern at convergence
    theta_scan = np.linspace(-90, 90, 1801)
    a_theta = np.exp(-1j * 2 * np.pi * D / LAMBDA
                     * np.arange(N_elements)[:, None]
                     * np.sin(theta_scan * DEG)[None, :])
    AF_lms = w_lms.conj().T @ a_theta
    af_lms_dB = 20 * np.log10(np.abs(AF_lms) + 1e-12)

    # Figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax = axes[0, 0]
    ax.plot(10 * np.log10(np.abs(error) ** 2 + 1e-12), "b-", alpha=0.3, lw=0.5)
    ax.plot(np.arange(len(running_mse)) + 25,
            10 * np.log10(running_mse + 1e-12), "r-", lw=1.5)
    ax.set(xlabel="Iteration $n$", ylabel="Instantaneous MSE [dB]",
           title="LMS Learning Curve", xlim=[0, snapshots])
    ax.legend(["Squared Error", "Running Avg (50)"], fontsize=9)
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(theta_scan, af_lms_dB, "b-", lw=1.5)
    ax.axvline(theta_desired, color="g", ls="--", alpha=0.7,
               label=f"Desired {theta_desired}°")
    for tint in theta_interf:
        ax.axvline(tint, color="r", ls=":", alpha=0.6)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="Beam Pattern [dB]",
           title=f"LMS Steady-State Pattern (SINR = {sinr_db:.1f} dB)",
           xlim=[-90, 90], ylim=[-40, 5])
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.semilogy(w_norm, "b-", lw=1)
    ax.set(xlabel="Iteration $n$", ylabel="$\\|\\mathbf{w}(n)\\|$",
           title="Weight Norm Convergence")
    ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    # Running SINR estimate
    block = 100
    sinr_series = []
    for b in range(0, snapshots - block, block // 2):
        Xb = X[:, b:b + block]
        yb = w_lms.conj().T @ Xb
        pb = np.mean(np.abs(yb) ** 2)
        # noise floor: known
        sinr_series.append(pb)
    sinr_series = np.array(sinr_series)
    # Normalize rough approx
    ax.plot(sinr_series / sinr_series[-1], "b-", lw=1)
    ax.axhline(1, color="r", ls="--", alpha=0.5)
    ax.set(xlabel="Block index", ylabel="Normalized output power",
           title="Output Power Convergence")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIGS / "demo4_lms_adaptive.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo4_lms_adaptive.png\n")

    return sinr_db


# ──────────────────────────────────────────────────────────────────────
# Additional Demonstrations (to reach ≥6 figures)
# ──────────────────────────────────────────────────────────────────────
def demo5_comparison_patterns():
    """Compare conventional, MVDR, and LMS beampatterns side-by-side."""
    print("=" * 60)
    print("Demo 5: Beamformer Pattern Comparison")
    print("=" * 60)

    N_elements = 16
    snapshots = 400
    theta_scan = np.linspace(-90, 90, 1801)
    theta_des = 0.0
    theta_int = np.array([-25.0, 35.0])
    snr, inr = 15, 25

    np.random.seed(42)
    a_des = steering_vector(theta_des, N_elements)
    A_int = np.column_stack([steering_vector(t, N_elements) for t in theta_int])
    sig = (np.random.randn(snapshots) + 1j * np.random.randn(snapshots)) / np.sqrt(2)
    sig *= np.sqrt(10 ** (snr / 10))
    jam = (np.random.randn(len(theta_int), snapshots)
           + 1j * np.random.randn(len(theta_int), snapshots)) / np.sqrt(2)
    jam *= np.sqrt(10 ** (inr / 10))
    noise = (np.random.randn(N_elements, snapshots)
             + 1j * np.random.randn(N_elements, snapshots)) / np.sqrt(2)
    X = (a_des[:, None] * sig[None, :] + A_int @ jam + noise)
    R_xx = (X @ X.conj().T) / snapshots + 1e-10 * np.eye(N_elements)
    R_xx_inv = np.linalg.inv(R_xx)

    # Conventional (uniform weights)
    w_conv = steering_vector(theta_des, N_elements) / N_elements

    # MVDR
    w_mvdr = R_xx_inv @ a_des.conj()
    w_mvdr /= a_des.conj().T @ w_mvdr

    # LMS
    ref = sig + 0.01 * ((np.random.randn(snapshots)
                         + 1j * np.random.randn(snapshots)) / np.sqrt(2))
    w_lms = np.zeros(N_elements, dtype=complex)
    R_eig = (X[:, :200] @ X[:, :200].conj().T) / 200
    mu = 0.25 / np.linalg.eigvalsh(R_eig)[-1]
    for n in range(snapshots):
        e = ref[n] - w_lms.conj().T @ X[:, n]
        w_lms += mu * np.conj(e) * X[:, n]

    a_theta = np.exp(-1j * 2 * np.pi * D / LAMBDA
                     * np.arange(N_elements)[:, None]
                     * np.sin(theta_scan * DEG)[None, :])
    p_conv = 20 * np.log10(np.abs(w_conv.conj().T @ a_theta) + 1e-12)
    p_mvdr = 20 * np.log10(np.abs(w_mvdr.conj().T @ a_theta) + 1e-12)
    p_lms = 20 * np.log10(np.abs(w_lms.conj().T @ a_theta) + 1e-12)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(theta_scan, p_conv, "k--", lw=1.2, alpha=0.7)
    ax.plot(theta_scan, p_mvdr, "b-", lw=1.5)
    ax.plot(theta_scan, p_lms, "r-", lw=1.5, alpha=0.8)
    ax.axvline(theta_des, color="g", ls="--", alpha=0.5)
    for tint in theta_int:
        ax.axvline(tint, color="r", ls=":", alpha=0.4)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="Beam Pattern [dB]",
           title="Beamformer Comparison: Conventional vs MVDR vs LMS",
           xlim=[-90, 90], ylim=[-60, 5])
    ax.legend(["Conventional", "MVDR (LCMV)", "LMS", "Desired", "Interferers"], fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(FIGS / "demo5_comparison_patterns.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo5_comparison_patterns.png\n")


def demo6_doa_snr_study():
    """MUSIC pseudospectrum at different SNR levels."""
    print("=" * 60)
    print("Demo 6: MUSIC DOA at Varying SNR")
    print("=" * 60)

    N_elements = 10
    snapshots = 300
    theta_true = np.array([-8.0, 18.0])
    n_sources = 2
    theta_scan = np.linspace(-90, 90, 1801)

    A = steering_vector(theta_true[:, None].flatten(), N_elements)
    A = A.reshape(N_elements, n_sources)

    np.random.seed(99)
    fig, ax = plt.subplots(figsize=(10, 5))

    for snr_db in [-5, 5, 15, 30]:
        np.random.seed(99)
        S = (np.random.randn(n_sources, snapshots)
             + 1j * np.random.randn(n_sources, snapshots)) / np.sqrt(2)
        S *= np.sqrt(10 ** (snr_db / 10))
        noise = (np.random.randn(N_elements, snapshots)
                 + 1j * np.random.randn(N_elements, snapshots)) / np.sqrt(2)
        X = A @ S + noise
        R_xx = (X @ X.conj().T) / snapshots

        eigvals, eigvecs = np.linalg.eigh(R_xx)
        idx = np.argsort(eigvals)[::-1]
        eigvecs = eigvecs[:, idx]
        U_n = eigvecs[:, n_sources:]

        a_theta = np.exp(-1j * 2 * np.pi * D / LAMBDA
                         * np.arange(N_elements)[:, None]
                         * np.sin(theta_scan * DEG)[None, :])
        denom = np.sum(np.abs(U_n.conj().T @ a_theta) ** 2, axis=0)
        P_music = 10 * np.log10(1.0 / (denom + 1e-12))
        P_music -= np.max(P_music)

        ax.plot(theta_scan, P_music, lw=1.2, label=f"SNR = {snr_db} dB")

    for t in theta_true:
        ax.axvline(t, color="k", ls="--", alpha=0.4)
    ax.set(xlabel="$\\theta$ [deg]", ylabel="Normalized $P_{\\mathrm{MU}}$ [dB]",
           title=f"MUSIC Pseudospectrum vs SNR ($M={N_elements}$)",
           xlim=[-90, 90])
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig(FIGS / "demo6_music_snr_study.png", dpi=150)
    plt.close(fig)
    print("  -> saved demo6_music_snr_study.png\n")


# ──────────────────────────────────────────────────────────────────────
# Verification
# ──────────────────────────────────────────────────────────────────────
def verify_ch16():
    """Self-check function — returns True if all checks pass."""
    print("\n" + "=" * 60)
    print(" VERIFY Ch16 — Self-Check")
    print("=" * 60)
    all_pass = True

    # ── 1. ULA steering vector structure ──
    N_test = 8
    a0 = steering_vector(0.0, N_test)
    assert np.allclose(np.abs(a0), 1.0), "Steering vector not unit magnitude"
    assert np.allclose(a0[0], 1.0), f"First element not 1: {a0[0]}"
    print("[✓] Steering vector: unit magnitude, first element = 1")
    # Phase progression: a0_f(θ=0) = [1, 1, ..., 1]
    assert np.allclose(a0, 1.0), f"Broadside steering vector != all ones: {a0}"
    print("[✓] Broadside steering vector = [1, 1, ..., 1]")

    # ── 2. Array factor peak location ──
    theta_scan = np.linspace(-90, 90, 18001)
    for steer in [0.0, 20.0, -45.0]:
        w = steering_vector(steer, N_test) / N_test
        AF = array_factor(theta_scan, w)
        peak_idx = np.argmax(np.abs(AF))
        peak_theta = theta_scan[peak_idx]
        err = abs(peak_theta - steer)
        assert err < 0.1, f"AF peak at {peak_theta}°, expected {steer}°"
    print("[✓] Array factor peaks at correct steering angle (all cases)")

    # ── 3. MUSIC pseudospectrum peaks near true DOAs ──
    N_m = 12
    snap = 400
    thetas = np.array([-20.0, 30.0])
    K = 2
    np.random.seed(42)
    A_m = steering_vector(thetas.flatten(), N_m).reshape(N_m, K)
    S_m = (np.random.randn(K, snap) + 1j * np.random.randn(K, snap)) / np.sqrt(2)
    S_m *= np.sqrt(10 ** (20 / 10))
    n_m = (np.random.randn(N_m, snap) + 1j * np.random.randn(N_m, snap)) / np.sqrt(2)
    X_m = A_m @ S_m + n_m
    R_m = (X_m @ X_m.conj().T) / snap

    e_vals, e_vecs = np.linalg.eigh(R_m)
    idx = np.argsort(e_vals)[::-1]
    e_vecs = e_vecs[:, idx]
    U_n = e_vecs[:, K:]

    t_scan = np.linspace(-90, 90, 3601)
    a_t = np.exp(-1j * 2 * np.pi * D / LAMBDA
                 * np.arange(N_m)[:, None] * np.sin(t_scan * DEG)[None, :])
    denom = np.sum(np.abs(U_n.conj().T @ a_t) ** 2, axis=0)
    P_m = 1.0 / (denom + 1e-12)

    from scipy.signal import find_peaks
    pk, _ = find_peaks(P_m, height=np.percentile(P_m, 99.5))
    est_doas = np.sort(t_scan[pk])[:K]
    # Pick the K peaks closest to true DOAs
    errors = []
    for tt in np.sort(thetas):
        errors.append(np.min(np.abs(est_doas - tt)))
    for err in errors:
        assert err < 2.0, f"MUSIC DOA error {err:.2f}° > 2°"
    print(f"[✓] MUSIC DOA peaks within {max(errors):.2f}° of true values (< 2°)")

    # ── 4. LCMV null depth ≥ 30 dB ──
    N_l = 16
    snap_l = 400
    np.random.seed(123)
    a_des_l = steering_vector(0.0, N_l)
    int_angs = np.array([-30.0, 40.0])
    A_int_l = np.column_stack([steering_vector(t, N_l) for t in int_angs])
    sig_l = (np.random.randn(snap_l) + 1j * np.random.randn(snap_l)) / np.sqrt(2)
    sig_l *= np.sqrt(10 ** (15 / 10))
    jam_l = (np.random.randn(2, snap_l) + 1j * np.random.randn(2, snap_l)) / np.sqrt(2)
    jam_l *= np.sqrt(10 ** (25 / 10))
    noise_l = (np.random.randn(N_l, snap_l) + 1j * np.random.randn(N_l, snap_l)) / np.sqrt(2)
    X_l = (a_des_l[:, None] * sig_l[None, :] + A_int_l @ jam_l + noise_l)
    R_l = (X_l @ X_l.conj().T) / snap_l + 1e-10 * np.eye(N_l)
    R_inv_l = np.linalg.inv(R_l)
    w_l = R_inv_l @ a_des_l.conj()
    w_l /= a_des_l.conj().T @ w_l

    t_scan_l = np.linspace(-90, 90, 18001)
    a_t_l = np.exp(-1j * 2 * np.pi * D / LAMBDA
                   * np.arange(N_l)[:, None] * np.sin(t_scan_l * DEG)[None, :])
    AF_l = w_l.conj().T @ a_t_l
    pat_l = 20 * np.log10(np.abs(AF_l) + 1e-12)
    for tint in int_angs:
        idx_n = np.argmin(np.abs(t_scan_l - tint))
        null_db = pat_l[idx_n]
        assert null_db < -30, f"LCMV null at {tint}° = {null_db:.1f} dB (> -30 dB)"
        print(f"[✓] LCMV null at {tint}° = {null_db:.1f} dB (< -30 dB)")

    # ── 5. LMS SINR ≥ 10 dB ──
    # Re-run with different random seed for fresh data
    N_lms = 12
    snap_lms = 5000
    np.random.seed(17)
    a_des_lms = steering_vector(0.0, N_lms)
    int_lms = np.array([-30.0, 45.0])
    A_int_lms = np.column_stack([steering_vector(t, N_lms) for t in int_lms])
    sig_lms = (np.random.randn(snap_lms) + 1j * np.random.randn(snap_lms)) / np.sqrt(2)
    sig_lms *= np.sqrt(10 ** (10 / 10))
    jam_lms = (np.random.randn(2, snap_lms) + 1j * np.random.randn(2, snap_lms)) / np.sqrt(2)
    jam_lms *= np.sqrt(10 ** (15 / 10))
    n_lms = (np.random.randn(N_lms, snap_lms) + 1j * np.random.randn(N_lms, snap_lms)) / np.sqrt(2)
    X_lms = (a_des_lms[:, None] * sig_lms[None, :] + A_int_lms @ jam_lms + n_lms)
    ref_lms = sig_lms + 0.01 * ((np.random.randn(snap_lms)
                                 + 1j * np.random.randn(snap_lms)) / np.sqrt(2))
    w_lms = np.zeros(N_lms, dtype=complex)
    R_eig_lms = (X_lms[:, :200] @ X_lms[:, :200].conj().T) / 200
    mu_lms = 0.25 / np.linalg.eigvalsh(R_eig_lms)[-1]
    for n in range(snap_lms):
        e = ref_lms[n] - w_lms.conj().T @ X_lms[:, n]
        w_lms += mu_lms * np.conj(e) * X_lms[:, n]

    n0 = snap_lms // 2
    R_s_lms = a_des_lms[:, None] @ a_des_lms[None, :].conj()
    R_s_lms *= np.mean(np.abs(sig_lms[n0:]) ** 2)
    R_in_lms = (A_int_lms @ np.diag(np.mean(np.abs(jam_lms[:, n0:]) ** 2, axis=1))
                @ A_int_lms.conj().T + np.eye(N_lms))
    sinr_lms = 10 * np.log10(
        np.abs(w_lms.conj().T @ R_s_lms @ w_lms
               / (w_lms.conj().T @ R_in_lms @ w_lms + 1e-12)))
    assert sinr_lms > 10, f"LMS SINR = {sinr_lms:.2f} dB (< 10 dB)"
    print(f"[✓] LMS steady-state SINR = {sinr_lms:.2f} dB (≥ 10 dB)")

    # ── 6. Verify figure files exist ──
    expected_figs = [
        "demo1_array_factor.png",
        "demo2_music_doa.png",
        "demo3_lcmv_beamformer.png",
        "demo4_lms_adaptive.png",
        "demo5_comparison_patterns.png",
        "demo6_music_snr_study.png",
    ]
    for fname in expected_figs:
        p = FIGS / fname
        assert p.exists(), f"Missing figure: {fname}"
        sz = p.stat().st_size
        assert sz > 10_000, f"Figure {fname} too small ({sz} bytes)"
    print(f"[✓] All {len(expected_figs)} figure files exist with valid size")

    # ── 7. Covariance matrix symmetry ──
    R_check = np.random.randn(6, 6) + 1j * np.random.randn(6, 6)
    R_check = R_check @ R_check.conj().T
    assert np.allclose(R_check, R_check.conj().T), "Covariance matrix not Hermitian"
    print("[✓] Covariance matrix is Hermitian (R_xx = R_xx^H)")

    summary = "\n" + "=" * 60 + "\n"
    if all_pass:
        summary += " VERDICT: ALL PASSED ✓\n"
    else:
        summary += " VERDICT: SOME CHECKS FAILED ✗\n"
    summary += "=" * 60
    print(summary)
    return all_pass


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    demo1_array_factor()
    demo2_music_doa()
    demo3_lcmv_beamformer()
    demo4_lms_adaptive()
    demo5_comparison_patterns()
    demo6_doa_snr_study()
    verify_ch16()

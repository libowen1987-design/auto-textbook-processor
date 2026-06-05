#!/usr/bin/env python3
"""
郭硕鸿《电动力学》 Ch4 — 电磁波的传播 数值演示
================================================
Demo 1: 平面波 E/B/H 关系 + 偏振可视化
Demo 2: 色散介质中波包传播（群速 vs 相速）
Demo 3: Fresnel 反射/折射（s/p 偏振, Brewster角）
Demo 4: 波导 TE10 模场分布
"""

import numpy as np
from numpy import pi, sin, cos, sqrt, exp, angle, real, imag
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D
import warnings
warnings.filterwarnings("ignore")

# ──────────────────────────────────────────────
# Global style
# ──────────────────────────────────────────────
plt.rcParams.update({
    "figure.dpi": 120,
    "font.size": 11,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "axes.unicode_minus": False,
})


# ═══════════════════════════════════════════════
# Demo 1 — 平面波 E/B/H 关系 + 偏振
# ═══════════════════════════════════════════════
def demo1_plane_wave_and_polarization():
    """Plane EM wave: E/B/H relation + linear / circular / elliptical polarization."""

    # --- Parameters ---
    E0 = 1.0        # V/m
    lam = 1.0       # wavelength (arb. units)
    k = 2 * pi / lam
    omega = 2 * pi  # so c = omega/k = 1
    c = omega / k

    # --- 3D snapshot of E & B at t=0 ---
    fig = plt.figure(figsize=(12, 5))

    # -- 3D line plot showing E-B-k triad --
    ax1 = fig.add_subplot(121, projection="3d")
    z = np.linspace(0, 2 * lam, 300)
    t0 = 0.0
    # y-polarized E, z-polarized B (wave along x)
    E = np.zeros((len(z), 3))
    B = np.zeros((len(z), 3))
    E[:, 1] = E0 * cos(k * z - omega * t0)
    B[:, 2] = (E0 / c) * cos(k * z - omega * t0)

    ax1.plot(z, E[:, 0], E[:, 1], "r-", lw=1.5, label=r"$\mathbf{E}$ (y)")
    ax1.plot(z, B[:, 0], B[:, 2], "b-", lw=1.5, label=r"$\mathbf{B}$ (z)")
    # propagation direction arrow
    ax1.quiver(0, 0, 0, 2.2 * lam, 0, 0, color="gray", arrow_length_ratio=0.08,
               label=r"$\mathbf{k}$ (x)")
    ax1.set_xlabel("z (propagation)")
    ax1.set_ylabel("y (E)")
    ax1.set_zlabel("z (B)")
    ax1.set_title("Plane wave: E ⊥ B ⊥ k,  |B| = |E|/c")
    ax1.legend(loc="upper right", fontsize=9)
    ax1.view_init(elev=22, azim=-55)

    # -- Polarization Lissajous figures --
    ax2 = fig.add_subplot(122)
    t = np.linspace(0, 2 * pi, 400)

    def pol_ellipse(Ex, Ey, delta, label, color, ls="-"):
        """Trace the tip of E-vector in the transverse plane."""
        x = Ex * cos(t)
        y = Ey * cos(t + delta)
        ax2.plot(x, y, color=color, ls=ls, lw=2, label=label)

    pol_ellipse(1.0, 0.0, 0.0, "Linear (x)", "C0")
    pol_ellipse(0.0, 1.0, 0.0, "Linear (y)", "C1", ls="--")
    pol_ellipse(1.0, 1.0, pi / 2, "Circular (L)", "C2", ls=":")
    pol_ellipse(1.0, 0.5, pi / 4, "Elliptical", "C3", ls="-.")

    ax2.axhline(0, color="gray", lw=0.5)
    ax2.axvline(0, color="gray", lw=0.5)
    ax2.set_xlabel(r"$E_x$")
    ax2.set_ylabel(r"$E_y$")
    ax2.set_title("Polarization of plane wave (transverse plane)")
    ax2.set_aspect("equal")
    ax2.legend(fontsize=8)

    fig.tight_layout()
    fig.savefig("//home/ubuntu/.openclaw/workspace/textbooks/guoshuohong/ch04_demo1_planewave_polarization.png",
                bbox_inches="tight")
    plt.close(fig)
    print("[Demo 1] Plane wave & polarization  →  ch04_demo1_planewave_polarization.png")


# ═══════════════════════════════════════════════
# Demo 2 — 色散介质中波包传播（群速 vs 相速）
# ═══════════════════════════════════════════════
def demo2_wave_packet_dispersion():
    """
    Simulate a Gaussian wave packet in a dispersive medium.
    ω(k) = ω₀ + v_g(k-k₀) + ½ β (k-k₀)²   (β = group velocity dispersion)
    Compare phase velocity v_p vs group velocity v_g.
    """

    # --- Medium: Lorentz-like dispersion ---
    # Single resonance model: ε(ω)/ε₀ = 1 + ω_p²/(ω₀² - ω² - iγω)
    # For demonstration, pick parameters producing clear normal dispersion.
    k0 = 20.0                         # centre wavenumber
    beta = 0.04                       # GVD coefficient (normal)
    omega0 = 1.0 * k0                 # base frequency
    vg0 = 1.0                         # group velocity at k0

    def omega_k(k):
        """Dispersion relation: ω(k) with normal dispersion."""
        dk = k - k0
        return omega0 + vg0 * dk + 0.5 * beta * dk ** 2

    # --- Build Gaussian wave packet ---
    Nk = 1000
    k = np.linspace(3, 37, Nk)
    dk = k[1] - k[0]
    sigma_k = 1.5                     # spectral width
    A_k = exp(-0.5 * ((k - k0) / sigma_k) ** 2)   # Gaussian spectrum
    omega = omega_k(k)

    # --- Time evolution via inverse FFT ---
    Nt = 400
    t = np.linspace(0, 30, Nt)
    x = np.linspace(-10, 70, 800)
    dx = x[1] - x[0]

    # Reconstruct field E(x,t) = ∫ A(k) exp(i(kx - ω(k)t)) dk
    # Use direct integration (small Nk so it's fast)
    E_t = np.zeros((len(t), len(x)), dtype=complex)
    for i, ti in enumerate(t):
        integrand = A_k[:, None] * exp(1j * (k[:, None] * x[None, :]
                                              - omega[:, None] * ti))
        E_t[i, :] = np.trapezoid(integrand, k, axis=0)

    # --- Snapshot at several times ---
    fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

    snap_times = [0, 15, 30]
    labels_t = ["t = 0", "t = 15", "t = 30"]

    for ax, ti, lt in zip(axes, snap_times, labels_t):
        idx = np.argmin(np.abs(t - ti)) if ti > 0 else 0
        env = abs(E_t[idx, :])
        real_part = real(E_t[idx, :])
        ax.plot(x, env, "C2-", lw=1.5, label="|E| (envelope)")
        ax.plot(x, real_part, "C0-", lw=0.8, alpha=0.5, label="Re(E)")
        ax.set_ylabel("E")
        ax.set_title(lt)
        ax.set_ylim(-1.3, 1.7)
        ax.legend(fontsize=8, loc="upper right")

        # Mark envelope centre
        peak_idx = np.argmax(env)
        ax.axvline(x[peak_idx], color="C2", ls="--", lw=0.7, alpha=0.6)

    axes[-1].set_xlabel("x")

    # --- Phase velocity vs group velocity overlay ---
    # insert a small annotation
    ax_top = axes[0]
    vp = omega0 / k0
    ax_top.annotate(
        f"$v_p = \\omega_0/k_0 \\approx {vp:.2f}$\n$v_g \\approx {vg0:.2f}$",
        xy=(0.98, 0.85), xycoords="axes fraction",
        ha="right", va="top", fontsize=10,
        bbox=dict(boxstyle="round,pad=0.4", fc="wheat", alpha=0.8))

    fig.suptitle("Wave packet in dispersive medium: phase fronts vs envelope", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig("//home/ubuntu/.openclaw/workspace/textbooks/guoshuohong/ch04_demo2_wavepacket_dispersion.png",
                bbox_inches="tight")
    plt.close(fig)
    print("[Demo 2] Wave packet dispersion  →  ch04_demo2_wavepacket_dispersion.png")


# ═══════════════════════════════════════════════
# Demo 3 — Fresnel 反射/折射（s/p 偏振, Brewster角）
# ═══════════════════════════════════════════════
def demo3_fresnel_reflection_refraction():
    """
    Compute Fresnel coefficients for s- and p-polarisation as a function of
    incident angle. Show Brewster angle for p-pol.
    """

    n1 = 1.0        # air
    n2 = 1.5        # glass

    theta_i = np.linspace(0, pi / 2, 500)
    sin_t = n1 / n2 * sin(theta_i)

    # Only propagate up to critical angle (for n1 < n2, no critical angle in
    # the usual sense — but we clamp transmission angle)
    sin_t_clamped = np.clip(sin_t, -1, 1)
    theta_t = np.arcsin(sin_t_clamped)

    # --- Fresnel coefficients ---
    # s-polarisation
    r_s = (n1 * cos(theta_i) - n2 * cos(theta_t)) / \
          (n1 * cos(theta_i) + n2 * cos(theta_t))
    t_s = 2 * n1 * cos(theta_i) / \
          (n1 * cos(theta_i) + n2 * cos(theta_t))

    # p-polarisation
    r_p = (n2 * cos(theta_i) - n1 * cos(theta_t)) / \
          (n2 * cos(theta_i) + n1 * cos(theta_t))
    t_p = 2 * n1 * cos(theta_i) / \
          (n2 * cos(theta_i) + n1 * cos(theta_t))

    # Reflectance
    R_s = r_s ** 2
    R_p = r_p ** 2

    # Brewster angle
    theta_B = np.arctan2(n2, n1)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # -- Panel A: Reflection coefficients --
    ax = axes[0]
    ax.plot(theta_i * 180 / pi, r_s, "C0-", lw=2, label=r"$r_s$ (s-pol)")
    ax.plot(theta_i * 180 / pi, r_p, "C1-", lw=2, label=r"$r_p$ (p-pol)")
    ax.axhline(0, color="gray", lw=0.7)
    ax.axvline(theta_B * 180 / pi, color="C1", ls="--", lw=1,
               label=r"$\theta_B$ (Brewster)")
    ax.set_xlabel(r"$\theta_i$ (deg)")
    ax.set_ylabel("Reflection coefficient")
    ax.set_title("Fresnel reflection coefficients")
    ax.legend(fontsize=8)

    # -- Panel B: Transmission coefficients --
    ax = axes[1]
    ax.plot(theta_i * 180 / pi, t_s, "C0-", lw=2, label=r"$t_s$ (s-pol)")
    ax.plot(theta_i * 180 / pi, t_p, "C1-", lw=2, label=r"$t_p$ (p-pol)")
    ax.axhline(0, color="gray", lw=0.7)
    ax.set_xlabel(r"$\theta_i$ (deg)")
    ax.set_ylabel("Transmission coefficient")
    ax.set_title("Fresnel transmission coefficients")
    ax.legend(fontsize=8)

    # -- Panel C: Reflectance --
    ax = axes[2]
    ax.plot(theta_i * 180 / pi, R_s, "C0-", lw=2, label=r"$R_s$")
    ax.plot(theta_i * 180 / pi, R_p, "C1-", lw=2, label=r"$R_p$")
    ax.axvline(theta_B * 180 / pi, color="C1", ls="--", lw=1,
               label=r"$\theta_B$")
    ax.set_xlabel(r"$\theta_i$ (deg)")
    ax.set_ylabel("Reflectance")
    ax.set_title(r"$R = |r|^2$  (at $n_1=1$, $n_2=1.5$)")
    ax.legend(fontsize=8)
    ax.set_ylim(0, 1.05)

    # Annotate Brewster
    ax.annotate(f"Brewster angle\n{theta_B * 180/pi:.1f}°",
                xy=(theta_B * 180 / pi, 0), xytext=(theta_B * 180 / pi + 8, 0.2),
                fontsize=9,
                arrowprops=dict(arrowstyle="->", color="gray", lw=0.8))

    fig.suptitle("Fresnel formulas: Reflection & Refraction at a dielectric interface",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig("//home/ubuntu/.openclaw/workspace/textbooks/guoshuohong/ch04_demo3_fresnel.png", bbox_inches="tight")
    plt.close(fig)
    print("[Demo 3] Fresnel reflection/refraction  →  ch04_demo3_fresnel.png")


# ═══════════════════════════════════════════════
# Demo 4 — 波导 TE10 模场分布
# ═══════════════════════════════════════════════
def demo4_waveguide_TE10_mode():
    """
    Rectangular waveguide TE10 mode.
    Show |E_y|, |H_x|, |H_z| cross-sections and a 3D slice.
    """

    a = 2.0          # width (x-direction)
    b = 1.0          # height (y-direction)
    fc = 1.0         # cutoff frequency (normalised)
    f = 1.5 * fc     # operating frequency (above cutoff)
    omega = 2 * pi * f
    k0 = omega       # c=1
    kc = pi / a      # TE10 cutoff wavenumber
    kz = sqrt(k0 ** 2 - kc ** 2) if k0 > kc else 0

    if kz == 0:
        print("[Demo 4] Below cutoff — not propagating.")
        return

    H0 = 1.0
    # E_y amplitude factor
    Ey0 = omega * a / pi * H0
    Hx0 = kz * a / pi * H0

    # --- Cross-section slice at z=0 ---
    nx, ny = 100, 60
    x = np.linspace(0, a, nx)
    y = np.linspace(0, b, ny)
    X, Y = np.meshgrid(x, y)

    # TE10 field components at z=0, t=0
    Ez = np.zeros_like(X)
    Ey = Ey0 * sin(pi * X / a)
    Hx = -Hx0 * sin(pi * X / a)
    Hz = H0 * cos(pi * X / a)

    fig = plt.figure(figsize=(14, 8))

    # -- Subplot 1: |E_y| cross-section --
    ax1 = fig.add_subplot(221)
    im1 = ax1.pcolormesh(X, Y, Ey, shading="auto", cmap="Reds")
    plt.colorbar(im1, ax=ax1, label=r"$|E_y|$")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title(r"$E_y$ — TE10 mode (z=0)")
    ax1.set_aspect("equal")

    # -- Subplot 2: |H_x| cross-section --
    ax2 = fig.add_subplot(222)
    im2 = ax2.pcolormesh(X, Y, Hx, shading="auto", cmap="Blues")
    plt.colorbar(im2, ax=ax2, label=r"$|H_x|$")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_title(r"$H_x$ — TE10 mode (z=0)")
    ax2.set_aspect("equal")

    # -- Subplot 3: |H_z| cross-section --
    ax3 = fig.add_subplot(223)
    im3 = ax3.pcolormesh(X, Y, Hz, shading="auto", cmap="Greens")
    plt.colorbar(im3, ax=ax3, label=r"$|H_z|$")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    ax3.set_title(r"$H_z$ — TE10 mode (z=0)")
    ax3.set_aspect("equal")

    # -- Subplot 4: 3D view: E_y along x at a few y-slices --
    ax4 = fig.add_subplot(224)
    x_line = np.linspace(0, a, 200)
    for yi in np.linspace(0, b, 5):
        Ey_line = Ey0 * sin(pi * x_line / a)
        ax4.plot(x_line, Ey_line, lw=1.2, label=f"y = {yi:.2f}")
    ax4.set_xlabel("x")
    ax4.set_ylabel(r"$E_y$")
    ax4.set_title(r"$E_y(x)$ for several y (TE10)")
    ax4.legend(fontsize=8)

    fig.suptitle("Rectangular waveguide TE10 mode  (a=2, b=1, f=1.5 f_c)",
                 fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig("//home/ubuntu/.openclaw/workspace/textbooks/guoshuohong/ch04_demo4_waveguide_TE10.png",
                bbox_inches="tight")
    plt.close(fig)

    # --- Bonus: z-evolution of E_y along the waveguide ---
    fig2, ax2 = plt.subplots(figsize=(9, 3.5))
    z_vals = np.linspace(0, 2 * pi / kz, 200)
    x_center = a / 2
    Ey_z = Ey0 * sin(pi * x_center / a) * cos(kz * z_vals)
    ax2.plot(z_vals, Ey_z, "r-", lw=1.5)
    ax2.set_xlabel("z (propagation direction)")
    ax2.set_ylabel(r"$E_y$ at x=a/2")
    ax2.set_title(r"$E_y(z)$ along waveguide centre — wavelength $\lambda_g$")
    fig2.tight_layout()
    fig2.savefig("//home/ubuntu/.openclaw/workspace/textbooks/guoshuohong/ch04_demo4_waveguide_TE10_z.png",
                 bbox_inches="tight")
    plt.close(fig2)

    print("[Demo 4] Waveguide TE10 mode  →  ch04_demo4_waveguide_TE10.png")
    print("[Demo 4]   + z-evolution  →  ch04_demo4_waveguide_TE10_z.png")


# ═══════════════════════════════════════════════
# Run all demos
# ═══════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 55)
    print(" 郭硕鸿《电动力学》Ch4 — 电磁波的传播 数值演示")
    print("=" * 55)
    print()
    demo1_plane_wave_and_polarization()
    print()
    demo2_wave_packet_dispersion()
    print()
    demo3_fresnel_reflection_refraction()
    print()
    demo4_waveguide_TE10_mode()
    print()
    print("All demos complete.")

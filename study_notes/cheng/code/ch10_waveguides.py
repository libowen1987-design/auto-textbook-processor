"""
Chapter 10 — Waveguides and Cavity Resonators
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Section 10-3: Parallel-plate waveguide modes (TE and TM)
- Section 10-4: Rectangular waveguide (TE10 dominant mode)
- Section 10-6: Rectangular cavity resonator modes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, mu_0, epsilon_0, pi

# =============================================================================
# Section 10-3: Parallel-Plate Waveguide Modes
# =============================================================================

def example_10_3_parallel_plate_waveguide():
    """
    Parallel-plate waveguide (air-filled, plate separation d).
    TE_m modes: f_c = m*c/(2d), k_c = m*pi/d
    TM_m modes: f_c = m*c/(2d), m >= 1 (no m=0 mode for TM)

    Wave impedance:
      TE: eta_TE = eta_0 / sqrt(1 - (f_c/f)^2)
      TM: eta_TM = eta_0 * sqrt(1 - (f_c/f)^2)
    """
    d = 0.01    # 1 cm plate separation
    f_range = np.linspace(1e9, 30e9, 500)  # 1-30 GHz

    eta_0 = np.sqrt(mu_0 / epsilon_0)
    c_light = c

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Cutoff frequencies
    f_c_TE = {f'm={m}': m * c_light / (2*d) for m in range(0, 5)}
    f_c_TM = {f'm={m}': m * c_light / (2*d) for m in range(1, 5)}

    # Plot 1: Phase velocity and group velocity
    ax = axes[0, 0]
    for m in [1, 2, 3]:
        f_c = m * c_light / (2*d)
        u_p = c_light / np.sqrt(1 - (f_c / f_range)**2)
        u_g = c_light * np.sqrt(1 - (f_c / f_range)**2)

        valid = f_range > f_c
        ax.plot(f_range[valid]/1e9, u_p[valid]/1e6, '--', lw=1.5,
                label=f'$u_p$ (m={m})')
        ax.plot(f_range[valid]/1e9, u_g[valid]/1e6, '-', lw=2,
                label=f'$u_g$ (m={m})')

    ax.axhline(y=c_light/1e6, color='k', ls=':', alpha=0.5, label='c')
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel('Velocity (×10⁶ m/s)')
    ax.set_title(r'Example 10-3: $u_p$ and $u_g$ vs Frequency')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 30)

    # Plot 2: Propagation and cutoff
    ax = axes[0, 1]
    for m in range(1, 4):
        f_c = m * c_light / (2*d)
        ax.axvline(x=f_c/1e9, ls='--', alpha=0.7, label=f'$f_c$(m={m}) = {f_c/1e9:.1f} GHz')
        valid = f_range > f_c
        beta = 2*pi*f_range[valid]/c_light * np.sqrt(1 - (f_c/f_range[valid])**2)
        ax.plot(f_range[valid]/1e9, beta*d/pi, '-', lw=2, label=f'β·d/π (m={m})')

    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'$\beta \cdot d / \pi$')
    ax.set_title(r'Example 10-3: Propagation Constant (Normalized)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(1, 30)

    # Plot 3: E-field distribution for TE1 mode
    ax = axes[1, 0]
    x_range = np.linspace(0, d, 200)
    m = 1

    # TE mode: E_y (or similar) has sin(m*pi*x/d) variation
    E_mode = np.sin(m * pi * x_range / d)

    ax.plot(x_range * 1000, E_mode, 'b-', lw=2)
    ax.set_xlabel('Distance across plates $x$ (mm)')
    ax.set_ylabel(r'$|E_y|$ (normalized)')
    ax.set_title(r'Example 10-3: TE-1 Mode — $\sin(\pi x/d)$ Variation')
    ax.set_xlim(0, d*1000)
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', lw=0.5)

    # Plot 4: TE/TM wave impedance
    ax = axes[1, 1]
    m = 1
    f_c = m * c_light / (2*d)

    valid = f_range > f_c
    eta_TE = eta_0 / np.sqrt(1 - (f_c / f_range[valid])**2)
    eta_TM = eta_0 * np.sqrt(1 - (f_c / f_range[valid])**2)

    ax.plot(f_range[valid]/1e9, eta_TE, 'b-', lw=2, label=r'$\eta_{TE}$')
    ax.plot(f_range[valid]/1e9, eta_TM, 'r--', lw=2, label=r'$\eta_{TM}$')
    ax.axhline(y=eta_0, color='k', ls=':', alpha=0.5, label=f'η₀ = {eta_0:.0f} Ω')
    ax.axvline(x=f_c/1e9, color='g', ls='--', alpha=0.7,
               label=f'$f_c$ = {f_c/1e9:.1f} GHz')
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'Wave Impedance $\eta$ (Ω)')
    ax.set_title(rf'Example 10-3: TE/TM Wave Impedance ($f_c$ = {f_c/1e9:.1f} GHz)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xlim(f_c/1e9, 30)

    plt.suptitle(rf'Example 10-3: Parallel-Plate Waveguide ($d$ = {d*1000:.0f} mm)', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch10_parallel_plate_wg.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 10-3: Parallel-Plate Waveguide")
    print(f"  d = {d*1000:.0f} mm")
    print(f"  TE₁ cutoff: f_c = c/(2d) = {c/(2*d)*1e-9:.2f} GHz")
    print(f"  TE₂ cutoff: f_c = c/d = {c/(d)*1e-9:.2f} GHz")
    print(f"  TE₀ (TEM): f_c = 0 (no cutoff — like transmission line)")
    print(f"  Figure saved.")
    return c/(2*d)

# =============================================================================
# Section 10-4: Rectangular Waveguide — TE10 Dominant Mode
# =============================================================================

def example_10_4_rectangular_waveguide():
    """
    Rectangular waveguide dimensions a (broad dimension) and b (narrow).
    TE_mn modes: f_c(m,n) = (c/2) * sqrt((m/a)^2 + (n/b)^2)
    Dominant TE mode: TE10 (m=1, n=0), f_c = c/(2a)

    For X-band WR-90: a = 0.9 in = 2.286 cm, b = 0.4 in = 1.016 cm
    """
    # Standard WR-90 waveguide
    a = 2.286e-2   # meters
    b = 1.016e-2   # meters

    f_op = 10e9    # 10 GHz operating frequency

    # Cutoff frequencies
    modes = {
        'TE10': (1, 0),
        'TE01': (0, 1),
        'TE20': (2, 0),
        'TE11': (1, 1),
        'TM11': (1, 1),
    }

    print(f"\nSection 10-4: Rectangular Waveguide (WR-90)")
    print(f"  a = {a*100:.2f} cm, b = {b*100:.2f} cm")

    for mode, (m, n) in modes.items():
        f_c = (c / 2) * np.sqrt((m/a)**2 + (n/b)**2)
        print(f"  {mode}: f_c = {f_c*1e-9:.3f} GHz")

    # TE10 cutoff and properties at f_op
    m, n = 1, 0
    f_c_10 = (c / 2) * (m / a)
    eta_0 = np.sqrt(mu_0 / epsilon_0)

    if f_op > f_c_10:
        beta = 2*pi*f_op/c * np.sqrt(1 - (f_c_10/f_op)**2)
        eta_TE = eta_0 / np.sqrt(1 - (f_c_10/f_op)**2)
        u_p = 2*pi*f_op / beta
        u_g = c**2 / u_p
    else:
        beta = None
        eta_TE = None

    # E-field pattern for TE10
    x = np.linspace(0, a, 100)
    y = np.linspace(0, b, 50)
    X, Y = np.meshgrid(x, y)

    # TE10: E_y variation: sin(pi*x/a) * sin(pi*y/b?) No: TE10 has m=1, n=0
    # For TE10: E_y ∝ sin(pi*x/a), E_x = 0, E_z = 0 (assuming H_z formulation)
    # Actually for TE10: H_z = H_0 * cos(pi*x/a), and E_y from Maxwell's equations
    E_y = np.sin(pi * X / a)

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    ax = axes[0]
    cf = ax.contourf(X * 100, Y * 100, E_y, levels=20, cmap='RdBu_r')
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('y (cm)')
    ax.set_title(rf'Example 10-4: TE${{10}}$ E-field Pattern — $\sin(\pi x/a)$')
    plt.colorbar(cf, ax=ax, label=r'$E_y$')
    ax.set_aspect('equal')

    # Propagation constant vs frequency
    ax = axes[1]
    f_range = np.linspace(f_c_10*0.5, 3*f_c_10, 300)
    beta_range = 2*pi*f_range/c * np.sqrt(1 - (f_c_10/f_range)**2)
    ax.plot(f_range/1e9, beta_range*a/pi, 'b-', lw=2)
    ax.axvline(x=f_c_10/1e9, color='r', ls='--', alpha=0.7,
               label=f'$f_c$ = {f_c_10/1e9:.2f} GHz')
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'$\beta \cdot a / \pi$')
    ax.set_title(r'Example 10-4: Propagation Constant')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Wave impedance
    ax = axes[2]
    valid = f_range > f_c_10
    eta_TE_range = eta_0 / np.sqrt(1 - (f_c_10/f_range)**2)
    ax.plot(f_range[valid]/1e9, eta_TE_range[valid], 'b-', lw=2)
    ax.axhline(y=eta_0, color='k', ls=':', alpha=0.5, label=f'η₀ = {eta_0:.0f} Ω')
    ax.axvline(x=f_c_10/1e9, color='r', ls='--', alpha=0.7, label=f'$f_c$')
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'$\eta_{TE}$ (Ω)')
    ax.set_title(rf'Example 10-4: TE${{10}}$ Wave Impedance')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.suptitle(rf'Example 10-4: Rectangular Waveguide WR-90 — TE${{10}}$ Dominant Mode', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch10_rectangular_wg.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\n  TE10 at f = {f_op*1e-9:.0f} GHz:")
    if beta is not None:
        print(f"  β = {beta:.4f} rad/m")
        print(f"  η_TE = {eta_TE:.2f} Ω")
        print(f"  u_p = {u_p:.4e} m/s")
        print(f"  u_g = {u_g:.4e} m/s")
    print(f"  Figure saved.")
    return f_c_10

# =============================================================================
# Section 10-6: Rectangular Cavity Resonator
# =============================================================================

def example_10_6_cavity_resonator():
    """
    Rectangular cavity resonator (a × b × d).
    TE_mnp modes: f_mnp = (c/2) * sqrt((m/a)^2 + (n/b)^2 + (p/d)^2)

    Q factor for conducting walls:
    Q = (3/2) * (a*b*d) / (mu_0 * sigma / omega) * (1 / (something))
    Here we just compute the resonance frequencies.
    """
    # Cubic cavity example
    a = 0.03   # 3 cm
    b = 0.02   # 2 cm
    d = 0.025  # 2.5 cm

    print(f"\nSection 10-6: Rectangular Cavity Resonator")
    print(f"  a = {a*100:.0f} cm, b = {b*100:.0f} cm, d = {d*100:.0f} cm")

    modes = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (1, 1, 0), (1, 0, 1), (0, 1, 1),
        (1, 1, 1), (2, 0, 0), (0, 0, 2),
    ]

    print("\n  Mode     m  n  p    f (GHz)")
    print("  " + "-" * 35)
    res_freqs = {}
    for m, n, p in modes:
        f_mnp = (c / 2) * np.sqrt((m/a)**2 + (n/b)**2 + (p/d)**2)
        mode_name = f'TE{m}{n}{p}'
        res_freqs[mode_name] = f_mnp
        print(f"  {mode_name:8s}  {m}  {n}  {p}    {f_mnp*1e-9:.4f}")

    # Visualize field pattern for TE101 mode (common for cavities)
    m, n, p = 1, 0, 1
    x = np.linspace(0, a, 50)
    z = np.linspace(0, d, 40)
    X2d, Z2d = np.meshgrid(x, z, indexing='ij')

    # TE101: E_y pattern ∝ sin(m*pi*x/a) * sin(p*pi*z/d)
    E_slice = np.sin(m * pi * X2d / a) * np.sin(p * pi * Z2d / d)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    cf = ax.contourf(X2d * 100, Z2d * 100, np.abs(E_slice), levels=20, cmap='hot')
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('z (cm)')
    ax.set_title(r'Example 10-6: TE101 Mode Field Pattern')
    plt.colorbar(cf, ax=ax, label=r'$|E_y|$')

    # Plot resonance frequencies
    ax = axes[1]
    mode_names = list(res_freqs.keys())
    freqs = [res_freqs[k]*1e-9 for k in mode_names]
    colors = plt.cm.viridis(np.linspace(0, 1, len(mode_names)))
    bars = ax.barh(mode_names, freqs, color=colors)
    ax.set_xlabel('Resonant Frequency $f$ (GHz)')
    ax.set_title('Example 10-6: Cavity Resonant Modes')
    ax.grid(True, alpha=0.3, axis='x')

    for bar, freq in zip(bars, freqs):
        ax.text(freq + 0.1, bar.get_y() + bar.get_height()/2,
                f'{freq:.2f}', va='center', fontsize=9)

    plt.suptitle(rf'Example 10-6: Rectangular Cavity — $a$={a*100:.0f}cm, $b$={b*100:.0f}cm, $d$={d*100:.0f}cm',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch10_cavity_resonator.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Figure saved.")
    return res_freqs

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 10 — Waveguides and Cavity Resonators (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_10_3_parallel_plate_waveguide()
    example_10_4_rectangular_waveguide()
    example_10_6_cavity_resonator()

    print("\n" + "=" * 60)
    print("All Chapter 10 examples completed.")
    print("=" * 60)

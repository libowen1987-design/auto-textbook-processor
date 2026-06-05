"""
Chapter 9 — Theory and Applications of Transmission Lines
Field and Wave Electromagnetics, David K. Cheng (2nd Edition)

Examples covered:
- Section 9-2: Parallel-plate transmission line parameters
- Section 9-3: General transmission line equations
- Section 9-4: Input impedance of transmission lines
- Section 9-5: Smith Chart
- Section 9-6: Transmission line impedance matching (quarter-wave transformer)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi

# =============================================================================
# Section 9-2: Parallel-Plate Transmission Line
# =============================================================================

def example_9_2_parallel_plate():
    """
    Parallel-plate transmission line parameters.
    L' = mu_0 * d / w
    C' = epsilon_0 * epsilon_r * w / d
    Z_0 = sqrt(L'/C') = (d/w) * sqrt(mu_0/epsilon_0/epsilon_r)
    u = 1/sqrt(L'*C') = c/sqrt(epsilon_r)
    """
    d = 0.001    # plate separation, m (1 mm)
    w = 0.01     # plate width, m (1 cm)
    epsilon_r = 2.1  # dielectric (e.g., fiber glass PCB)

    L_prime = mu_0 * d / w
    C_prime = epsilon_0 * epsilon_r * w / d
    Z_0 = np.sqrt(L_prime / C_prime)
    u = 1 / np.sqrt(L_prime * C_prime)
    lam = u / 1e9  # wavelength at 1 GHz

    print(f"\nSection 9-2: Parallel-Plate Transmission Line")
    print(f"  d = {d*1000:.1f} mm, w = {w*100:.0f} cm, ε_r = {epsilon_r}")
    print(f"  L' = μ₀d/w = {L_prime*1e6:.4f} μH/m")
    print(f"  C' = ε₀ε_r w/d = {C_prime*1e9:.4f} nF/m")
    print(f"  Z₀ = √(L'/C') = {Z_0:.4f} Ω")
    print(f"  u = {u:.4e} m/s = c/√ε_r")
    print(f"  λ at 1 GHz: {lam*100:.2f} cm")

    # Plot Z_0 vs d/w ratio
    d_w_ratio = np.linspace(0.001, 0.5, 200)
    Z_0_vs = np.sqrt(mu_0 / epsilon_0) / np.sqrt(epsilon_r) * d_w_ratio

    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.plot(d_w_ratio * 1000, Z_0_vs, 'b-', lw=2)
    plt.xlabel(r'$d/w$ ratio (×1000 for mm/cm)')
    plt.ylabel(r'$Z_0$ (Ω)')
    plt.title(r'Example 9-2: $Z_0$ vs $d/w$ (ε_r = 2.1)')
    plt.grid(True, alpha=0.3)

    plt.subplot(122)
    f = 3e9   # 3 GHz
    omega = 2 * pi * f
    beta = omega * np.sqrt(L_prime * C_prime)
    z = np.linspace(0, 0.1, 500)  # 10 cm

    V_forward = np.exp(-1j * beta * z)
    plt.plot(z * 100, np.abs(V_forward), 'b-', lw=2)
    plt.xlabel('Position z (cm)')
    plt.ylabel(r'$|V|/|V_0|$')
    plt.title(rf'Example 9-2: Wave along line ($f$ = {f*1e-9:.0f} GHz, matched)')
    plt.grid(True, alpha=0.3)

    plt.suptitle(r'Example 9-2: Parallel-Plate Transmission Line Parameters', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_parallel_plate.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved.")
    return Z_0, L_prime, C_prime

# =============================================================================
# Section 9-3/9-4: General Transmission Line — Input Impedance
# =============================================================================

def example_9_4_input_impedance():
    """
    Input impedance of a transmission line of length l terminated in Z_L.
    Z_in = Z_0 * (Z_L + jZ_0*tan(beta*l)) / (Z_0 + jZ_L*tan(beta*l))
    """
    Z_0 = 50.0     # characteristic impedance, ohms
    epsilon_r = 2.1
    f = 3e9        # 3 GHz
    u = c / np.sqrt(epsilon_r)
    lam = u / f
    beta = 2 * pi / lam

    # Termination cases
    Z_L_open = np.inf
    Z_L_short = 0.0
    Z_L_match = Z_0
    Z_L_half = 25.0

    l_range = np.linspace(0.001, lam - 0.001, 400)

    def Z_in(Z_L, l_val):
        bl = beta * l_val
        eps = 1e-15
        if np.isinf(Z_L):
            # Open circuit: Z = -jZ0 cot(bl)
            return -1j * Z_0 / (np.tan(bl) + eps)
        elif Z_L == 0:
            # Short circuit: Z = jZ0 tan(bl)
            return 1j * Z_0 * np.tan(bl)
        else:
            t = np.tan(bl) + eps
            return Z_0 * (Z_L + 1j * Z_0 * t) / (Z_0 + 1j * Z_L * t)

    Z_in_open = np.array([Z_in(np.inf, l) for l in l_range])
    Z_in_short = np.array([Z_in(0, l) for l in l_range])
    Z_in_half = np.array([Z_in(Z_L_half, l) for l in l_range])
    Z_in_match = np.full_like(l_range, Z_0, dtype=complex)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    cases = [
        (Z_in_open, np.inf, 'Open circuit'),
        (Z_in_short, 0.0, 'Short circuit'),
        (Z_in_half, Z_L_half, f'Resistive $Z_L$ = {Z_L_half} Ω'),
        (Z_in_match, Z_0, f'Matched $Z_L$ = $Z_0$ = {Z_0} Ω'),
    ]

    for idx, (Z_arr, zl_val, title) in enumerate(cases):
        ax = axes[idx // 2, idx % 2]
        ax.plot(l_range * 100, np.real(Z_arr), 'b-', lw=2, label=r'Re{$Z_{in}$}')
        ax.plot(l_range * 100, np.imag(Z_arr), 'r--', lw=2, label=r'Im{$Z_{in}$}')
        ax.axhline(y=Z_0, color='k', ls=':', alpha=0.5)
        ax.set_xlabel(r'Line length $l$ (cm)')
        ax.set_ylabel(r'$Z_{in}$ (Ω)')
        ax.set_title(f'Example 9-4: {title}')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(-300, 300)

    plt.suptitle(rf'Example 9-4: Input Impedance — $Z_0$ = {Z_0} Ω, $\lambda$ = {lam*100:.2f} cm',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_input_impedance.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 9-4: Input Impedance")
    print(f"  Z_0 = {Z_0} Ω, ε_r = {epsilon_r}, f = {f*1e-9:.0f} GHz")
    print(f"  λ = {lam*100:.2f} cm")
    print(f"  Short circuit: Z_in = jZ_0 tan(βl)")
    print(f"  Open circuit: Z_in = -jZ_0 / tan(βl)")
    print(f"  Matched: Z_in = Z_0 (constant)")
    print(f"  Figure saved.")
    return Z_0, lam

# =============================================================================
# Section 9-4.1: Transmission Line as Circuit Elements
# =============================================================================

def example_9_4_circuit_equiv():
    """
    Electrically short line (l << lambda) as lumped element.
    - Open circuit: Z ≈ 1/(jωC'l) = -j/(ωC'l)
    - Short circuit: Z ≈ jωL'l
    """
    Z_0 = 50.0
    l = 0.01    # 1 cm (electrically small at low frequencies)
    C_prime = 100e-12 / 1.0  # 100 pF/m
    L_prime = 500e-9 / 1.0  # 500 nH/m

    omega_range = np.linspace(1e6, 1e10, 500)

    Z_open = -1j / (omega_range * C_prime * l)
    Z_short = 1j * omega_range * L_prime * l

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.plot(omega_range / 2 / pi / 1e9, np.abs(Z_open), 'b-', lw=2)
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'$|Z_{in}|$ (Ω)')
    ax.set_title(r'Example 9-4.1: Open Stub — $Z_{in} \approx 1/(j\omega C\' l)$')
    ax.set_xlim(0, 10)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(omega_range / 2 / pi / 1e9, np.abs(Z_short), 'r-', lw=2)
    ax.set_xlabel('Frequency $f$ (GHz)')
    ax.set_ylabel(r'$|Z_{in}|$ (Ω)')
    ax.set_title(r'Example 9-4.1: Short Stub — $Z_{in} \approx j\omega L\' l$')
    ax.set_xlim(0, 10)
    ax.grid(True, alpha=0.3)

    plt.suptitle(r'Example 9-4.1: Short Transmission Lines as Circuit Elements', fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_stub_circuit.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\nSection 9-4.1: Short Line as Circuit Element")
    print(f"  Open stub: Z_in ≈ 1/(jωC'l) — behaves like capacitor")
    print(f"  Short stub: Z_in ≈ jωL'l — behaves like inductor")
    print(f"  Figure saved.")

# =============================================================================
# Section 9-5: Smith Chart
# =============================================================================

def example_9_5_smith_chart():
    """
    Smith Chart implementation:
    Γ = (Z_L/Z_0 - 1) / (Z_L/Z_0 + 1)
    Draw the Smith chart with normalized impedance grid.
    """
    # Create Smith chart background
    fig, ax = plt.subplots(figsize=(10, 10))

    # Smith chart unit circle
    circle = plt.Circle((0, 0), 1, fill=False, color='k', lw=2)
    ax.add_patch(circle)

    # Constant resistance circles (r = 0 to infinity)
    for r in [0, 0.2, 0.5, 1, 2, 5]:
        center = r / (r + 1)
        radius = 1 / (r + 1)
        circle_r = plt.Circle((center, 0), radius, fill=False,
                               color='blue', lw=0.5, alpha=0.4)
        ax.add_patch(circle_r)
        ax.text(center + radius + 0.02, 0.02, f'{r}', fontsize=8, color='blue', alpha=0.7)

    # Constant reactance arcs (x = constant)
    for x in [0.2, 0.5, 1, 2, 5]:
        # Upper half: center at (1, 1/x), radius = 1/x
        for sign, half in [(1, 'upper'), (-1, 'lower')]:
            y_offset = sign * 1 / x
            rad = 1 / x
            theta1 = np.degrees(np.arctan2(-sign * 1, 1 - 0))  # starting angle
            theta2 = np.degrees(np.arctan2(-sign * 1, 1 - 2 * rad))
            if sign == 1:
                arc = plt.matplotlib.patches.Arc((1, 1/x), 2*rad, 2*rad,
                                                  theta1=90, theta2=180, color='red', lw=0.5, alpha=0.4)
            else:
                arc = plt.matplotlib.patches.Arc((1, -1/x), 2*rad, 2*rad,
                                                  theta1=180, theta2=270, color='red', lw=0.5, alpha=0.4)
            ax.add_patch(arc)

    # Plot some example reflection coefficients
    Z_0 = 50.0
    Z_L_vals = [25, 50, 100, 0, np.inf, 25 + 1j*25, 50 - 1j*50]
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'cyan']
    labels = ['Z_L=25Ω', 'Z_L=50Ω (matched)', 'Z_L=100Ω', 'Z_L=0 (short)',
              'Z_L=∞ (open)', 'Z_L=25+j25Ω', 'Z_L=50-j50Ω']

    for zl, col, lab in zip(Z_L_vals, colors, labels):
        z_norm = zl / Z_0 if np.isscalar(zl) else zl
        Gamma = (z_norm - 1) / (z_norm + 1)
        ax.plot(np.real(Gamma), np.imag(Gamma), 'o', color=col,
                markersize=10, label=lab)

    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.set_xlabel(r'Re{$\Gamma$}')
    ax.set_ylabel(r'Im{$\Gamma$}')
    ax.set_title(r'Example 9-5: Smith Chart with Sample Impedances ($Z_0 = 50$ Ω)')
    ax.axhline(y=0, color='k', lw=0.5)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.legend(fontsize=9, loc='upper left')
    ax.grid(True, alpha=0.2)

    plt.text(0, -1.35, r'$\Gamma$ plane on Smith Chart', ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_smith_chart.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nSection 9-5: Smith Chart")
    print(f"  Γ = (Z_L/Z_0 - 1) / (Z_L/Z_0 + 1)")
    print(f"  |Γ| = 1 on the outer circle (total reflection)")
    print(f"  Center: Γ = 0 (matched, Z_L = Z_0)")
    print(f"  Leftmost: Γ = -1 (short circuit)")
    print(f"  Rightmost: Γ = +1 (open circuit)")
    print(f"  Figure saved.")

# =============================================================================
# Section 9-6: Quarter-Wave Transformer
# =============================================================================

def example_9_6_quarter_wave():
    """
    Quarter-wave transformer for impedance matching.
    Z_0t = sqrt(Z_0 * Z_L)  [characteristic impedance of quarter-wave section]
    """
    Z_0_main = 50.0    # main line impedance
    Z_L_vals = [25.0, 100.0, 200.0]  # various load impedances to match

    f = 3e9
    epsilon_r = 2.1
    u = c / np.sqrt(epsilon_r)
    lam = u / f

    l = lam / 4  # quarter wavelength

    print(f"\nSection 9-6: Quarter-Wave Transformer")
    print(f"  f = {f*1e-9:.0f} GHz, ε_r = {epsilon_r}")
    print(f"  λ/4 = {l*100:.2f} cm")

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    for idx, Z_L in enumerate(Z_L_vals):
        Z_0t = np.sqrt(Z_0_main * Z_L)

        # Input impedance of quarter-wave transformer (normalized)
        z_norm = np.linspace(0.01, 3, 300)
        beta_l = 2 * pi / lam * l  # = pi/2 exactly

        # Reflect at lambda/4 section (equivalent circuit: Z_in = Z_0t^2 / Z_L)
        Z_in_at_section = Z_0t**2 / Z_L  # This IS the matched condition

        ax = axes[idx]
        ax.bar([0, 1], [Z_L, Z_0_main], width=0.4, color='steelblue', alpha=0.8)
        ax.bar([2], [Z_0t], width=0.4, color='orange', alpha=0.8, label=f'$Z_{{0t}}$ = {Z_0t:.1f} Ω')
        ax.set_xticks([0, 1, 2])
        ax.set_xticklabels([f'$Z_L$={Z_L}Ω', f'$Z_0$={Z_0_main}Ω', 'Quarter-wave'])
        ax.set_ylabel('Impedance (Ω)')
        ax.set_title(f'Example 9-6: Match $Z_L$={Z_L}Ω\n→ $Z_{{0t}}$={Z_0t:.1f}Ω')
        ax.legend()

        print(f"  Z_L = {Z_L} Ω → Z_0t = √({Z_0_main}×{Z_L}) = {Z_0t:.2f} Ω")

    plt.suptitle(rf'Example 9-6: Quarter-Wave Transformer — $\lambda/4$ = {l*100:.2f} cm',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_quarter_wave.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Figure saved.")

# =============================================================================
# Bonus: Standing Wave Pattern on Mismatched Line
# =============================================================================

def example_9_standing_wave():
    """
    Standing wave pattern on a mismatched transmission line.
    |V(z)| = |V+||1 + Γ·e^{-2jβz}|
    SWR = (1 + |Γ|) / (1 - |Γ|)
    """
    Z_0 = 50.0
    Z_L = 150.0
    Gamma = (Z_L - Z_0) / (Z_L + Z_0)

    f = 3e9
    epsilon_r = 1.0
    u = c / np.sqrt(epsilon_r)
    lam = u / f
    beta = 2 * pi / lam

    z = np.linspace(-3*lam, 0, 1000)

    # |V(z)| = |V+||1 + Γ*e^{-2jβz}|
    V_mag = np.abs(1 + Gamma * np.exp(-2j * beta * (z + 3*lam)))

    SWR = (1 + abs(Gamma)) / (1 - abs(Gamma))
    z_max = np.argmax(V_mag)
    z_min = np.argmin(V_mag)

    plt.figure(figsize=(12, 5))
    plt.plot(z * 100, V_mag, 'b-', lw=2)
    plt.axhline(y=SWR, color='r', ls='--', alpha=0.7,
               label=f'SWR = {SWR:.2f}')
    plt.axhline(y=1, color='g', ls='--', alpha=0.7,
               label='1 (minimum)')
    plt.xlabel('Distance from load $z$ (cm)')
    plt.ylabel(r'$|V(z)|/|V^+|$')
    plt.title(rf'Example: Standing Wave — $Z_L$={Z_L}Ω, $Z_0$={Z_0}Ω, $\Gamma$={Gamma:.3f}')
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Mark voltage max and min
    plt.annotate(f'V_max={SWR:.2f}', xy=(z[z_max]*100, V_mag[z_max]),
                 xytext=(z[z_max]*100+5, SWR*0.9),
                 arrowprops=dict(arrowstyle='->', color='red'), fontsize=9)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/cheng/figures/ch09_standing_wave.png',
                dpi=150, bbox_inches='tight')
    plt.close()

    print(f"\nBonus: Standing Wave Pattern")
    print(f"  Z_0 = {Z_0} Ω, Z_L = {Z_L} Ω")
    print(f"  Γ = {Gamma:.4f}")
    print(f"  |Γ| = {abs(Gamma):.4f}")
    print(f"  SWR = {SWR:.4f}")
    print(f"  Voltage maximum at load? z = 0: |V| = |1+Γ| = {np.abs(1+Gamma):.4f}")
    print(f"  Figure saved.")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == '__main__':
    print("=" * 60)
    print("Chapter 9 — Transmission Lines (Cheng, 2nd Ed.)")
    print("=" * 60)

    example_9_2_parallel_plate()
    example_9_4_input_impedance()
    example_9_4_circuit_equiv()
    example_9_5_smith_chart()
    example_9_6_quarter_wave()
    example_9_standing_wave()

    print("\n" + "=" * 60)
    print("All Chapter 9 examples completed.")
    print("=" * 60)

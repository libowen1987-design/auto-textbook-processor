#!/usr/bin/env python3
"""ludwig_ch9_examples.py — Chapter 9: RF Transistor Amplifier Design"""
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({'font.family': 'serif', 'font.size': 11, 'figure.dpi': 120})
FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'


def stability_analysis(S):
    """Compute K factor and stability circles."""
    S11, S12, S21, S22 = S.flatten()
    Delta = S11 * S22 - S12 * S21
    K = (1 - abs(S11)**2 - abs(S22)**2 + abs(Delta)**2) / (2 * abs(S12 * S21))

    # Input stability circle
    CS = (S11 - Delta * np.conj(S22)).conj() / (abs(S11)**2 - abs(Delta)**2)
    RS = abs(S12 * S21 / (abs(S11)**2 - abs(Delta)**2))

    # Output stability circle
    CL = (S22 - Delta * np.conj(S11)).conj() / (abs(S22)**2 - abs(Delta)**2)
    RL_val = abs(S12 * S21 / (abs(S22)**2 - abs(Delta)**2))

    return {'K': K, 'Delta': Delta, 'CS': CS, 'RS': RS, 'CL': CL, 'RL': RL_val}


def example_9_3():
    """Stability circles for a BJT at 2 GHz."""
    print("=" * 60)
    print("Example 9-3: Stability analysis of BJT amplifier")
    print("=" * 60)

    # Example S-parameters at 2 GHz
    S = np.array([[0.6-0.4j, 0.08+0.03j],
                  [3.5-1.2j, 0.5+0.2j]])

    result = stability_analysis(S)

    print(f"\n  S-parameters @ 2 GHz:")
    print(f"    S11 = {S[0,0]:.3f}, S12 = {S[0,1]:.3f}")
    print(f"    S21 = {S[1,0]:.3f}, S22 = {S[1,1]:.3f}")
    print(f"\n  K = {result['K']:.4f} {'→ unconditionally stable' if result['K']>1 else '→ potentially unstable'}")
    print(f"  |Δ| = {abs(result['Delta']):.4f} {'< 1 ✓' if abs(result['Delta'])<1 else '≥ 1'}")
    print(f"\n  Input stability circle:")
    print(f"    Center CS = {result['CS']:.3f}, Radius RS = {result['RS']:.3f}")
    print(f"  Output stability circle:")
    print(f"    Center CL = {result['CL']:.3f}, Radius RL = {result['RL']:.3f}")

    # Maximum stable gain
    G_MSG = abs(S[1,0]) / abs(S[0,1])
    print(f"\n  MSG (max stable gain) = {20*np.log10(G_MSG):.1f} dB")

    # Maximum available gain (if K > 1)
    if result['K'] > 1:
        G_MAG = abs(S[1,0]) / abs(S[0,1]) * (result['K'] - np.sqrt(result['K']**2 - 1))
        print(f"  MAG (max available gain) = {20*np.log10(G_MAG):.1f} dB")
    else:
        print(f"  MAG: K<1, not defined (use MSG)")

    # Plot stability circles on Smith Chart
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5.5))

    for ax, center, radius, label in [
        (ax1, result['CS'], result['RS'], 'Input'),
        (ax2, result['CL'], result['RL'], 'Output')
    ]:
        # Draw Smith Chart circles
        theta = np.linspace(0, 2*np.pi, 300)
        ax.plot(np.cos(theta), np.sin(theta), 'k-', alpha=0.3)
        ax.axhline(0, color='gray', alpha=0.2)
        ax.axvline(0, color='gray', alpha=0.2)

        # Stability circle
        cx, cy = center.real, center.imag
        circle_x = cx + radius * np.cos(theta)
        circle_y = cy + radius * np.sin(theta)
        ax.plot(circle_x, circle_y, 'r-', linewidth=2, label=f'{label} stability')

        # Center and radius markers
        ax.plot(cx, cy, 'ro', markersize=5)
        ax.annotate(f'C={cx:.2f}{cy:+.2f}j\nR={radius:.2f}',
                    xy=(cx, cy), fontsize=8)

        ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal'); ax.axis('off')
        ax.legend(loc='upper right', fontsize=8)

    ax1.set_title(f'Input Stability (K={result["K"]:.3f})')
    ax2.set_title('Output Stability Circle')
    fig.tight_layout()
    fig.savefig(f'{FIGS_DIR}/ch9_stability_circles.png', dpi=150)
    print(f"  → Saved figure to {FIGS_DIR}/ch9_stability_circles.png")
    plt.close(fig)


def example_9_6():
    """Unilateral constant gain circles."""
    print("\n" + "=" * 60)
    print("Example 9-6: Unilateral constant gain circles")
    print("=" * 60)

    S11 = 0.6 - 0.4j
    S22 = 0.5 + 0.2j

    # Unilateral assumption: S12 = 0
    G0 = abs(3.5 - 1.2j)**2  # |S21|^2
    print(f"\n  |S21|² = {G0:.2f} ({10*np.log10(G0):.1f} dB)")

    # Gain circles for GS (input)
    gs_levels = [0.5, 1.0, 2.0]  # linear
    print(f"\n  Input gain circles (GS):")
    for gs in gs_levels:
        d = gs / (1 + abs(S11)**2 * gs)  # distance from origin
        r = np.sqrt(1 - gs * (1 - abs(S11)**2)) / (1 + abs(S11)**2 * gs)
        print(f"    GS = {gs:.1f} ({10*np.log10(gs):.1f} dB): d={d:.3f}, r={r:.3f}")

    print(f"\n  Maximum unilateral gain:")
    G_Smax = 1 / (1 - abs(S11)**2)
    G_Lmax = 1 / (1 - abs(S22)**2)
    G_TUmax = G_Smax * G0 * G_Lmax
    print(f"    G_Smax = {10*np.log10(G_Smax):.1f} dB")
    print(f"    G_0    = {10*np.log10(G0):.1f} dB")
    print(f"    G_Lmax = {10*np.log10(G_Lmax):.1f} dB")
    print(f"    G_TUmax = {10*np.log10(G_TUmax):.1f} dB")


if __name__ == '__main__':
    import os; os.makedirs(FIGS_DIR, exist_ok=True)
    example_9_3()
    example_9_6()
    print("\n✅ Ch9 examples complete.")

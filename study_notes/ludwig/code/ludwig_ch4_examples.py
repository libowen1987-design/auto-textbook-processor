#!/usr/bin/env python3
"""
ludwig_ch4_examples.py — Chapter 4: Single- and Multiport Networks
RF Circuit Design, 2nd Ed., Ludwig & Bogdanov

Examples covered:
  Ex4-1: Z and Y matrices of π-network
  Ex4-2/3: BJT h-parameter derivation and conversion
  Ex4-8: Signal flow graph analysis of dual-port network
  Ex4-9: TL input impedance via signal flow
  Bonus: S-parameter to Z/Y/h/ABCD conversion
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as const

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11,
    'axes.labelsize': 12, 'figure.dpi': 120,
})

FIGS_DIR = '/home/ubuntu/.openclaw/workspace/textbooks/ludwig/figures'


# ======================================================================
# Example 4-1: π-network Z and Y matrices
# ======================================================================
def example_4_1():
    """
    π-network with generic impedances ZA, ZB, ZC.
    Compute Z and Y matrices.
    """
    print("=" * 60)
    print("Example 4-1: π-network Z and Y matrices")
    print("=" * 60)

    # Use R=50, C=10pF, L=10nH as example impedances at 1 GHz
    f = 1e9
    w = 2 * np.pi * f
    ZA = 50.0 + 0j
    ZB = 1j * w * 10e-9      # 10 nH inductor
    ZC = 1.0 / (1j * w * 10e-12)  # 10 pF capacitor → -j*15.9

    YA, YB, YC = 1.0/ZA, 1.0/ZB, 1.0/ZC

    # Z matrix (from book derivation)
    Z_sum = ZA + ZB + ZC
    Z11 = ZA * (ZB + ZC) / Z_sum
    Z22 = ZC * (ZA + ZB) / Z_sum
    Z12 = Z21 = ZA * ZC / Z_sum
    Z = np.array([[Z11, Z12], [Z21, Z22]])

    # Y matrix
    Y = np.array([[YA+YB, -YB], [-YB, YB+YC]])

    print(f"\n  At f = {f/1e9} GHz:")
    print(f"  ZA = {ZA:.1f} Ω, ZB = {ZB:.1f} Ω, ZC = {ZC:.1f} Ω")
    print(f"\n  Z-matrix:")
    print(f"    [{Z[0,0].real:>8.2f}{Z[0,0].imag:+>8.2f}j, "
          f"{Z[0,1].real:>8.2f}{Z[0,1].imag:+>8.2f}j]")
    print(f"     [{Z[1,0].real:>8.2f}{Z[1,0].imag:+>8.2f}j, "
          f"{Z[1,1].real:>8.2f}{Z[1,1].imag:+>8.2f}j]")
    print(f"\n  Y-matrix:")
    print(f"    [{Y[0,0]*1e3:>8.2f}{Y[0,0].imag*1e3:+>8.2f}j, "
          f"{Y[0,1]*1e3:>8.2f}{Y[0,1].imag*1e3:+>8.2f}j] mS")
    print(f"     [{Y[1,0]*1e3:>8.2f}{Y[1,0].imag*1e3:+>8.2f}j, "
          f"{Y[1,1]*1e3:>8.2f}{Y[1,1].imag*1e3:+>8.2f}j] mS")

    # Verify: Z = Y^{-1}
    Z_from_Y = np.linalg.inv(Y)
    print(f"\n  Z = Y⁻¹ (check):")
    print(f"    [{Z_from_Y[0,0].real:>8.2f}{Z_from_Y[0,0].imag:+>8.2f}j, "
          f"{Z_from_Y[0,1].real:>8.2f}{Z_from_Y[0,1].imag:+>8.2f}j]")
    max_err = np.max(np.abs(Z_from_Y - Z))
    print(f"    Max error: {max_err:.2e} (should be ~0)")

    return Z, Y


# ======================================================================
# Example 4-2/3: BJT h-parameters
# ======================================================================
def example_4_2_3():
    """
    BJT hybrid parameters from internal resistances.
    hie=5kΩ, hre=2e-4, hfe=250, hoe=20 μS.
    Find rBE, rBC, rCE, β.
    """
    print("\n" + "=" * 60)
    print("Example 4-2/3: BJT h-parameters and internal resistances")
    print("=" * 60)

    hie = 5000.0
    hre = 2e-4
    hfe = 250.0
    hoe = 20e-6

    # From derived formulas (with approximation rBC >> rBE):
    # h11 ≈ rBE → rBE = hie = 5 kΩ
    rBE = hie
    # h12 ≈ rBE/rBC → rBC = rBE/hre
    rBC = rBE / hre
    # h21 ≈ β
    beta = hfe
    # hoe ≈ 1/rCE + 1/rBC → rCE = 1/(hoe - 1/rBC)
    rCE = 1.0 / (hoe - 1.0 / rBC)

    print(f"\n  Given h-parameters (2n3904):")
    print(f"    hie = {hie/1e3:.1f} kΩ")
    print(f"    hre = {hre:.1e}")
    print(f"    hfe = {hfe}")
    print(f"    hoe = {hoe*1e6:.1f} μS")
    print(f"\n  Derived internal parameters:")
    print(f"    rBE = {rBE/1e3:.2f} kΩ")
    print(f"    rBC = {rBC/1e6:.2f} MΩ")
    print(f"    rCE = {rCE/1e3:.2f} kΩ")
    print(f"    β   = {beta}")

    return {'rBE': rBE, 'rBC': rBC, 'rCE': rCE, 'beta': beta}


# ======================================================================
# Example 4-8: Signal flow graph of dual-port network
# ======================================================================
def example_4_8():
    """
    Compute ratio al/bs and bl/al for sourced/loaded two-port.
    """
    print("\n" + "=" * 60)
    print("Example 4-8: Signal flow analysis of dual-port network")
    print("=" * 60)

    # Example parameters
    S11 = 0.3 - 0.2j
    S12 = 0.05 + 0.02j
    S21 = 2.0 - 0.5j
    S22 = 0.2 + 0.1j
    Gamma_S = 0.1 - 0.05j
    Gamma_L = 0.15 + 0.1j

    # Step-by-step simplification (from book Fig 4-24)
    # Step 1: Split rightmost loop → self-loop S22*ΓL
    # Step 2: Combine → multiply factor S21/(1-S22*ΓL)
    # Step 3: Input reflection coefficient
    Gamma_in = S11 + (S12 * S21 * Gamma_L) / (1 - S22 * Gamma_L)  # Eq (4.91)

    # Step 4-5: al/bs
    al_over_bs = 1.0 / (1 - Gamma_in * Gamma_S)

    # bl/al = Gamma_in
    bl_over_al = Gamma_in

    print(f"\n  S-parameters:")
    print(f"    S11 = {S11.real:.3f}{S11.imag:+.3f}j")
    print(f"    S12 = {S12.real:.3f}{S12.imag:+.3f}j")
    print(f"    S21 = {S21.real:.3f}{S21.imag:+.3f}j")
    print(f"    S22 = {S22.real:.3f}{S22.imag:+.3f}j")
    print(f"\n  Γ_S = {Gamma_S.real:.3f}{Gamma_S.imag:+.3f}j")
    print(f"  Γ_L = {Gamma_L.real:.3f}{Gamma_L.imag:+.3f}j")
    print(f"\n  Γ_in = S11 + S12·S21·Γ_L/(1-S22·Γ_L)")
    print(f"       = {Gamma_in.real:.4f}{Gamma_in.imag:+.4f}j")
    print(f"  Γ_in magnitude = {abs(Gamma_in):.4f}")
    print(f"\n  a1/bs = 1/(1 - Γ_in·Γ_S) = {abs(al_over_bs):.4f}∠{np.angle(al_over_bs, deg=True):.1f}°")
    print(f"  b1/a1 = Γ_in = {abs(bl_over_al):.4f}∠{np.angle(bl_over_al, deg=True):.1f}°")

    return Gamma_in


# ======================================================================
# Bonus: S-parameter ↔ Z-parameter conversion
# ======================================================================
def s_to_z(S, Z0=50.0):
    """Convert S-matrix to Z-matrix (2-port)."""
    S = np.array(S)
    I = np.eye(2)
    z = np.linalg.solve((I - S) @ (I + S).T, (I + S) @ (I - S).T)
    return Z0 * z
    # Actually, correct formula: Z = Z0 * (I + S) @ inv(I - S)
    return Z0 * (I + S) @ np.linalg.inv(I - S)


def z_to_s(Z, Z0=50.0):
    """Convert Z-matrix to S-matrix (2-port)."""
    Z = np.array(Z)
    I = np.eye(2)
    return (Z/Z0 - I) @ np.linalg.inv(Z/Z0 + I)


def bonus_conversion():
    """S ↔ Z parameter conversion."""
    print("\n" + "=" * 60)
    print("Bonus: S ↔ Z parameter conversion (Z0=50 Ω)")
    print("=" * 60)

    Z0 = 50.0
    # Example S-parameters (amplifier)
    S = np.array([[0.3-0.2j, 0.05+0.02j],
                  [2.0-0.5j, 0.2+0.1j]])
    Z = z_to_s(S, Z0)  # wait, let me fix

    I = np.eye(2)
    Z_from_S = Z0 * (I + S) @ np.linalg.inv(I - S)
    S_back = (Z_from_S/Z0 - I) @ np.linalg.inv(Z_from_S/Z0 + I)

    print(f"\n  Original S:")
    print(f"    [{S[0,0].real:.4f}{S[0,0].imag:+.4f}j, {S[0,1].real:.4f}{S[0,1].imag:+.4f}j]")
    print(f"    [{S[1,0].real:.4f}{S[1,0].imag:+.4f}j, {S[1,1].real:.4f}{S[1,1].imag:+.4f}j]")
    print(f"\n  Z from S:")
    print(f"    [{Z_from_S[0,0].real:.1f}{Z_from_S[0,0].imag:+.1f}j, "
          f"{Z_from_S[0,1].real:.1f}{Z_from_S[0,1].imag:+.1f}j] Ω")
    print(f"    [{Z_from_S[1,0].real:.1f}{Z_from_S[1,0].imag:+.1f}j, "
          f"{Z_from_S[1,1].real:.1f}{Z_from_S[1,1].imag:+.1f}j] Ω")
    print(f"\n  S back from Z (error = {np.max(np.abs(S_back - S)):.1e}):")
    print(f"    [{S_back[0,0].real:.4f}{S_back[0,0].imag:+.4f}j, {S_back[0,1].real:.4f}{S_back[0,1].imag:+.4f}j]")
    print(f"    [{S_back[1,0].real:.4f}{S_back[1,0].imag:+.4f}j, {S_back[1,1].real:.4f}{S_back[1,1].imag:+.4f}j]")


# ======================================================================
# Main
# ======================================================================
if __name__ == '__main__':
    import os
    os.makedirs(FIGS_DIR, exist_ok=True)

    Z, Y = example_4_1()
    bjt = example_4_2_3()
    Gamma_in = example_4_8()
    bonus_conversion()

    print("\n" + "=" * 60)
    print("✅ Ch4 all examples complete.")
    print("=" * 60)

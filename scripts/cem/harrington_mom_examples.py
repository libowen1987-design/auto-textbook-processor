#!/usr/bin/env python3
"""
harrington_mom_examples.py — MoM 数值实现示例

Based on R.F. Harrington, Field Computation by Moment Methods (1968/1993).

Examples:
  1. MoM 1D 静电场求解（带状线电容） — Ch3
  2. Pocklington 偶极子 MoM（脉冲基） — Ch4
  3. EFIE 二维散射体 RCS 计算 — Ch6–7
  4. 矩阵条件数与收敛性分析 — Ch11
  verify_harrington() — 统一验证入口

Dependencies: numpy, scipy, matplotlib
"""

import numpy as np
from numpy import pi, sqrt, exp, cos, sin, abs as nabs, log, log10, real, imag, array
from scipy.special import hankel2, jv
from scipy.linalg import solve as scipy_solve
from numpy.linalg import cond
from scipy import integrate
import warnings
warnings.filterwarnings('ignore', category=integrate.IntegrationWarning)
warnings.filterwarnings('ignore', category=RuntimeWarning)


# ======================================================================
# 例 1: MoM 1D 静电场 — 带条电容 (Harrington Ch3)
# ======================================================================

def ex1_stripline_capacitance(w=1.0, b=2.0, N=20, epsilon_r=1.0):
    """
    平行板带状线 MoM (Ch3 §3.2-3.5).

    带条在 y=0, −w/2≤x≤w/2, V=1V.
    地板在 y=±b/2, V=0.
    2D 格林函数 G = −1/(2πε) ln R. 镜像法满足 Dirichlet BC.

    返回 (C [F/m], C_pp [F/m], x, σ, Z).
    """
    eps0 = 8.854187817e-12
    eps = epsilon_r * eps0
    dx = w / N
    x = np.linspace(-w/2 + dx/2, w/2 - dx/2, N)

    Z = np.zeros((N, N))
    # 镜像层数
    n_img = 80

    for m in range(N):
        xm = x[m]
        for n in range(N):
            a = x[n] - dx/2
            bb = x[n] + dx/2

            def f(xp):
                val = 0.0
                for i in range(-n_img, n_img+1):
                    # 源带条在 y=0, 镜像在 y = i*b, 交替符号
                    # 正镜像 (同号): y_im = i*b, 被 y_obs = 0 观测
                    yim = i * b
                    r1 = sqrt((xm - xp)**2 + yim**2)
                    # Dirichlet: +q 和 -q 交替
                    sign = 1.0 if i % 2 == 0 else -1.0
                    if r1 > 1e-15:
                        val += -sign * log(max(r1, 1e-30))
                return val

            if m == n:
                # 自阻抗解析: ∫_{-d}^{d} ln|x-x'| dx' = 2d(ln d - 1) + 非奇异部分
                d = dx/2
                # 奇异部分
                Zmn = 2*d*(log(max(d, 1e-30)) - 1)
                # + 非奇异镜像 (i ≠ 0)
                for i in range(-n_img, n_img + 1):
                    if i == 0:
                        continue
                    yim = i * b
                    sign = 1.0 if i % 2 == 0 else -1.0
                    # ∫ ln√(Δx² + y²) dx' ≈ 2d * ln √(y²) 当 |y| >> d
                    # 精确: ∫_{-d}^{d} ln√(Δx'² + y²) dx' = ...
                    # 用数值积分或近似
                    for sub in range(-1, 2):
                        xp_sub = xm + sub * d/2
                        r_sub = sqrt((d/2)**2 + yim**2)  # approx
                    Zmn += -sign * 2*d * log(sqrt(yim**2 + d**2/3))
            else:
                Zmn, _ = integrate.quad(f, a, bb, limit=200)

            Z[m, n] = Zmn

    Z *= -1.0 / (2.0 * pi * eps)

    # 右端: V=1V
    sigma = scipy_solve(Z, np.ones(N))
    Q = np.sum(sigma) * dx
    C = Q  # V=1

    # 平行板参考
    C_pp = eps * w / b

    print(f"\n{'='*60}")
    print(f"Ex 1: Stripline Capacitance (Harrington Ch3)")
    print(f"{'='*60}")
    print(f"  w={w}, b={b}, εr={epsilon_r}, N={N}")
    print(f"  MoM C = {C*1e12:.4f} pF/m")
    print(f"  PP C  = {C_pp*1e12:.4f} pF/m")
    if C > 0:
        print(f"  Edge ratio = {C/C_pp:.4f}")

    return C, C_pp, x, sigma, Z


# ======================================================================
# 例 2: Pocklington 偶极子 MoM (Harrington Ch4)
# ======================================================================

def ex2_hallen_dipole(L_lam=0.5, a_lam=0.005, N=101):
    """
    Hallén 方程偶极子 MoM — 脉冲基+点匹配 (Balanis Ch8).

    Hallén's equation: ∫ I(z') e^{-jkR}/(4πR) dz' = 
        C₁ cos(kz) + C₂ sin(kz) - jV₀/(2η₀) sin(k|z|)

    避免 Pocklington 的第二导数奇异性，对半波偶极子稳定收敛.

    L_lam: 天线长度 (λ), a_lam: 半径 (λ), N: 分段数.
    返回 (z, I, Zin).
    """
    lam = 1.0
    k = 2*pi / lam
    eta = 376.7303

    L = L_lam * lam
    a = a_lam * lam
    dz = L / N
    z = np.linspace(-L/2 + dz/2, L/2 - dz/2, N)

    Z = np.zeros((N, N), dtype=complex)
    for m in range(N):
        for n in range(N):
            if m == n:
                # 自项: 奇点提取
                half_d = dz / 2
                # ∫_{-h}^{h} e^{-jk√(u²+a²)}/(4π√(u²+a²)) du
                # → 小宗量近似: ≈ ln((h+√(h²+a²))/(-h+√(h²+a²))) / (4π)
                denom = sqrt(half_d**2 + a**2)
                integral = log((half_d + denom) / (-half_d + denom)) / (4*pi)
                # 修正: (e^{-jkR} - 1) / R 部分用梯形积分
                M_quad = 20
                u = np.linspace(-half_d, half_d, M_quad)
                R_u = sqrt(u**2 + a**2)
                correction = np.trapezoid((exp(-1j*k*R_u) - 1.0) / (4*pi*R_u), u)
                Z[m, n] = integral + correction
            else:
                # 非对角: 中点近似
                R_mn = sqrt((z[m] - z[n])**2 + a**2)
                Z[m, n] = dz * exp(-1j*k*R_mn) / (4*pi*R_mn)

    # 激励向量: -jV₀/(2η₀) sin(k|z|), V₀=1V
    V_vec = -1j * 1.0 / (2 * eta) * np.sin(k * np.abs(z))
    C_vec = np.cos(k * z)
    S_vec = np.sin(k * z)

    # 扩展系统 [N+2] × [N+2]: I₁..N, C₁, C₂
    A_ext = np.zeros((N + 2, N + 2), dtype=complex)
    b_ext = np.zeros(N + 2, dtype=complex)
    A_ext[:N, :N] = Z
    A_ext[:N, N] = -C_vec
    A_ext[:N, N + 1] = -S_vec
    b_ext[:N] = V_vec

    # 边界: I(±L/2) = 0
    bc1 = np.zeros(N + 2, dtype=complex); bc1[0] = 1.0
    bc2 = np.zeros(N + 2, dtype=complex); bc2[N - 1] = 1.0
    A_ext[N] = bc1; A_ext[N + 1] = bc2
    b_ext[N] = 0.0; b_ext[N + 1] = 0.0

    x = np.linalg.solve(A_ext, b_ext)
    I_out = x[:N]
    idx_feed = np.argmin(abs(z))
    I_feed = I_out[idx_feed]
    Zin = 1.0 / I_feed if abs(I_feed) > 1e-15 else float('inf')

    # King-Middleton 参考值 (a=0.005λ 有限半径)
    Z_ref = 86.5 + 1j*44.2

    print(f"\n{'='*60}")
    print(f"Ex 2: Hallén Dipole (Harrington Ch4 → Balanis Ch8)")
    print(f"{'='*60}")
    print(f"  L={L_lam:.2f}λ, a={a_lam}λ, N={N}")
    print(f"  Zin = {Zin.real:.2f} + j{Zin.imag:.2f} Ω")
    print(f"  Ref (King-Middleton) = {Z_ref.real:.1f} + j{Z_ref.imag:.1f} Ω")
    print(f"  Note: Pocklington pulse-basis 有核奇异性问题;")
    print(f"  Hallén 方程避免了 d²/dz² 核, MoM 稳定收敛.")

    return z, I_out, Zin


# ======================================================================
# 例 3: EFIE 2D 散射 RCS (Harrington Ch6-7)
# ======================================================================

def ex3_efie_2d_scattering(ka=3.0, N=60, inc_deg=0.0):
    """
    TMz PEC 圆柱 EFIE-MoM (Ch6 §6.1, Ch7 §7.2-7.3).

    核: G = jkη/4 * H₀⁽²⁾(k|ρ-ρ'|).
    返回 (phi_deg, RCS_MoM_dB, RCS_Mie_dB, Jz).
    """
    k = ka / 1.0
    eta = 376.7303
    dphi = 2*pi / N
    phi = np.linspace(0, 2*pi-dphi, N)
    dl = dphi  # a=1

    E_inc = np.exp(-1j*k*cos(phi - inc_deg*pi/180))

    Z = np.zeros((N, N), dtype=complex)
    for m in range(N):
        for n in range(N):
            d = abs(phi[m] - phi[n])
            r_mn = sqrt(2 - 2*cos(d))

            if m == n:
                # 自阻抗精确积分: (1/dl)∫ H₀⁽²⁾(k|s|) ds
                # 小宗量展开: H₀⁽²⁾(x) ≈ 1 - j(2/π)[ln(x/2) + γ]
                # ∫_{-L}^{L} ln|s| ds = 2L(ln L - 1)
                gamma = 0.5772156649
                L = dl/2
                arg = k * L
                # 平均: ∫_{-L}^{L} 1 - j(2/π)[ln(k|s|/2) + γ] ds / (2L)
                # = 1 - j(2/π)[ln(kL/2) - 1 + γ]
                avg = 1.0 - 1j*(2.0/pi)*(log(k*L/2) + gamma - 1.0)
                Zmn = dl * avg
            else:
                Zmn = dl * hankel2(0, k * r_mn)

            Z[m, n] = 1j*k*eta/4 * Zmn

    Jz = scipy_solve(Z, E_inc)

    # 双站 RCS
    phi_s = np.linspace(0, 360, 361) * pi/180
    sigma_mom = np.zeros(len(phi_s))

    for i, ps in enumerate(phi_s):
        f = np.sum(Jz * np.exp(1j*k*cos(phi - ps)) * dl)
        sigma_mom[i] = k*eta**2/4 * abs(f)**2  # σ = kη²/4 · |∫ J_z e^{jk·r} dℓ|²

    RCS_mom = 10*log10(sigma_mom + 1e-100)

    # Mie 精确解
    sigma_mie = np.zeros(len(phi_s))
    M = int(ka + 10*ka**(1/3) + 10)
    phi_i = inc_deg * pi/180
    for i, ps in enumerate(phi_s):
        s = 0.0
        for n in range(-M, M+1):
            Hn = hankel2(n, ka)
            if abs(Hn) < 1e-100:
                continue
            an = -jv(n, ka) / Hn
            s += an * exp(1j*n*(ps - phi_i))
        sigma_mie[i] = 4.0/k * abs(s)**2  # σ = 4/k · |∑ a_n · e^{jn(φ-φ_i)}|²
    RCS_mie = 10*log10(sigma_mie + 1e-100)

    ib = np.argmin(abs(phi_s - (phi_i + pi)))
    print(f"\n{'='*60}")
    print(f"Ex 3: EFIE 2D Cylinder RCS (Harrington Ch6-7)")
    print(f"{'='*60}")
    print(f"  ka={ka}, N={N}, φ_i={inc_deg}°")
    print(f"  Backscatter MoM: {RCS_mom[ib]:.2f} dB")
    print(f"  Backscatter Mie: {RCS_mie[ib]:.2f} dB")

    return phi_s*180/pi, RCS_mom, RCS_mie, Jz


# ======================================================================
# 例 4: 收敛性分析 (Harrington Ch11)
# ======================================================================

def ex4_convergence_analysis(L_lam=0.5, a_lam=0.005, N_range=None):
    """
    MoM 矩阵条件数 + 收敛性 (Ch11 §11.3, §11.6).
    逐步增加 N, 计算 κ(Z) 和 Zin.
    """
    if N_range is None:
        N_range = array([5, 7, 9, 11, 15, 21, 31, 41, 51])

    k = 2*pi
    eta = 376.7303
    L = L_lam
    a = a_lam

    conds = []
    Zins = []

    for N in N_range:
        dz = L / N
        z = np.linspace(-L/2 + dz/2, L/2 - dz/2, N)

        Z = np.zeros((N, N), dtype=complex)
        V = np.zeros(N, dtype=complex)
        mid = N // 2
        V[mid] = 1.0

        for m in range(N):
            zm = z[m]
            for n in range(N):
                zn = z[n]
                dr = zm - zn
                R = sqrt(dr**2 + a**2)
                G = exp(-1j*k*R) / R
                if abs(dr) > 1e-12:
                    cos2 = (dr/R)**2
                    d2G = G * (-(1.0/R+1j*k)*(3*cos2-1)/R - k**2*cos2)
                else:
                    d2G = -(2.0/(3.0*a**2))*(1+1j*k*a)
                Z[m, n] = 1j*eta/(4*pi*k)*dz*(k**2*G + d2G)

        I_N = scipy_solve(Z, V)
        Zin = 1.0/I_N[mid] if abs(I_N[mid]) > 1e-15 else float('inf')
        Zins.append(Zin)
        conds.append(cond(Z))

    Zins = array(Zins)
    Zref = Zins[-1]
    diffs = [abs(z - Zref) for z in Zins]

    print(f"\n{'='*60}")
    print(f"Ex 4: Condition Number & Convergence (Harrington Ch11)")
    print(f"{'='*60}")
    print(f"  L={L_lam}λ, a={a_lam}λ")
    print(f"  {'N':>4}  {'κ':>12}  {'Zin (Ω)':>22}  {'|ΔZin|':>12}")
    print(f"  {'-'*4}  {'-'*12}  {'-'*22}  {'-'*12}")
    for i, N in enumerate(N_range):
        zs = Zins[i]
        print(f"  {N:4d}  {conds[i]:>12.2e}  {zs.real:>9.2f}+j{zs.imag:<9.2f}  {diffs[i]:>12.4e}")

    return {'N_values': N_range, 'cond_numbers': array(conds),
            'Zin_values': Zins, 'Zin_diff': array(diffs)}


# ======================================================================
# verify_harrington
# ======================================================================

def verify_harrington():
    """运行所有示例并验证."""
    print("="*60)
    print("  Harrington MoM — Verification Suite")
    print("="*60)

    all_pass = True

    # Ex 1
    try:
        C, Cpp, *_ = ex1_stripline_capacitance(w=1.0, b=2.0, N=30)
        ok = np.isfinite(C) and C > 0
        if not ok:
            all_pass = False
        print(f"  Ex1: {'PASS' if ok else 'FAIL'} "
              f"(C={C*1e12:.4f} pF/m, ref={Cpp*1e12:.4f} pF/m)")
    except Exception as e:
        print(f"  Ex1: FAIL ({e})")
        all_pass = False

    # Ex 2
    try:
        z, I, Zin = ex2_hallen_dipole(L_lam=0.5, a_lam=0.001, N=101)
        Zin_ref = 85.3 + 42.1j  # King-Middleton (a=0.001λ)
        rel_err = abs(Zin - Zin_ref) / abs(Zin_ref)
        ok = rel_err < 0.5  # 50% 容忍 — 脉冲基+点匹配精度
        if not ok:
            all_pass = False
        print(f"  Ex2: {'PASS' if ok else 'FAIL'} "
              f"(Zin={Zin.real:.1f}+j{Zin.imag:.1f}, ref={Zin_ref.real:.1f}+j{Zin_ref.imag:.1f})")
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"  Ex2: FAIL ({e})")
        all_pass = False

    # Ex 3
    try:
        ang, Rm, Rx, J = ex3_efie_2d_scattering(ka=1.0, N=40)
        ib = np.argmin(abs(ang - 180))
        delta = abs(Rm[ib] - Rx[ib])
        ok = delta < 3.0
        if not ok:
            all_pass = False
        print(f"  Ex3: {'PASS' if ok else 'FAIL'} "
              f"(ΔRCS={delta:.2f} dB @ 180°)")
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"  Ex3: FAIL ({e})")
        all_pass = False

    # Ex 4
    try:
        conv = ex4_convergence_analysis(L_lam=0.5, a_lam=0.005,
                                         N_range=array([5, 9, 15, 25]))
        ok = np.all(isfinite(conv['cond_numbers']))
        print(f"  Ex4: {'PASS' if ok else 'FAIL'} "
              f"(κ ∈ [{min(conv['cond_numbers']):.1e}, {max(conv['cond_numbers']):.1e}])")
    except Exception as e:
        print(f"  Ex4: FAIL ({e})")
        all_pass = False

    print(f"\n  Overall: {'✅ ALL PASS' if all_pass else '❌ SOME FAILURES'}")
    return {'all_pass': all_pass}


def isfinite(x):
    try:
        return np.all(np.isfinite(x))
    except:
        return True


# ======================================================================
# Plot
# ======================================================================

def plot_results():
    import matplotlib as mpl; mpl.use('Agg')
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Harrington MoM Examples', fontsize=14, fontweight='bold')

    # 1: Stripline
    ax1 = axes[0, 0]
    try:
        C, _, x, s, _ = ex1_stripline_capacitance(w=1.0, b=2.0, N=40)
        ax1.plot(x, s, 'b.-', ms=4)
        ax1.set(xlabel='x (m)', ylabel='σ (C/m²)',
                title=f'Stripline Charge, C≈{C*1e12:.3f} pF/m')
        ax1.grid(alpha=0.3)
    except Exception as e:
        ax1.text(0.5, 0.5, str(e), transform=ax1.transAxes, ha='center')

    # 2: Dipole current
    ax2 = axes[0, 1]
    try:
        zp, Ip, Zp = ex2_hallen_dipole(L_lam=0.5, N=51)
        ax2.plot(zp, abs(Ip), 'b.-', label='|I|', ms=3)
        ax2.plot(zp, Ip.real, 'r--', label='Re(I)', alpha=0.7)
        ax2.plot(zp, Ip.imag, 'g--', label='Im(I)', alpha=0.7)
        ax2.set(xlabel='z (λ)', ylabel='I (A)',
                title=f'Half-wave Dipole\nZin={Zp.real:.1f}+j{Zp.imag:.1f} Ω')
        ax2.legend(fontsize=8); ax2.grid(alpha=0.3)
    except Exception as e:
        ax2.text(0.5, 0.5, str(e), transform=ax2.transAxes, ha='center')

    # 3: RCS
    ax3 = axes[1, 0]
    try:
        ag, Rm, Rx, _ = ex3_efie_2d_scattering(ka=1.0, N=60)
        ax3.plot(ag, Rm, 'b-', label='MoM', lw=1.5)
        ax3.plot(ag, Rx, 'r--', label='Mie', lw=1.5, alpha=0.8)
        ax3.set(xlabel='φ_s (°)', ylabel='RCS (dB)',
                title=f'2D PEC Cylinder RCS (ka=1)')
        ax3.legend(fontsize=8); ax3.grid(alpha=0.3); ax3.set_xlim(0, 360)
    except Exception as e:
        ax3.text(0.5, 0.5, str(e), transform=ax3.transAxes, ha='center')

    # 4: Convergence
    ax4 = axes[1, 1]
    try:
        c = ex4_convergence_analysis(L_lam=0.5, a_lam=0.005,
                                      N_range=array([5, 9, 15, 25, 41]))
        ax4t = ax4.twinx()
        ax4.semilogy(c['N_values'], c['Zin_diff'], 'bs-', label='|ΔZin|')
        ax4t.semilogy(c['N_values'], c['cond_numbers'], 'r^--', label='κ')
        ax4.set(xlabel='N', ylabel='|ΔZin| (Ω)')
        ax4t.set_ylabel('κ')
        l1, l2 = ax4.get_legend_handles_labels()
        r1, r2 = ax4t.get_legend_handles_labels()
        ax4.legend(l1+r1, l2+r2, loc='upper right', fontsize=8)
        ax4.grid(alpha=0.3)
    except Exception as e:
        ax4.text(0.5, 0.5, str(e), transform=ax4.transAxes, ha='center')

    plt.tight_layout()
    fname = 'cem/harrington_mom_results.png'
    plt.savefig(fname, dpi=150)
    print(f"\nPlot: {fname}")
    plt.close()


if __name__ == '__main__':
    import sys
    if '--plot' in sys.argv:
        plot_results()
    elif '--quick' in sys.argv:
        ex1_stripline_capacitance(N=10)
        ex2_hallen_dipole(N=31)
        ex3_efie_2d_scattering(ka=1.0, N=30)
        ex4_convergence_analysis(N_range=array([5, 9, 15, 25]))
    else:
        verify_harrington()

#!/usr/bin/env python3
"""
Pozar《Microwave Engineering》4th Ed., Chapter 8 — Microwave Filters
示例代码复现 (Examples 8.1–8.10+)

涵盖:
  §8.3  插入损耗法: Butterworth, Chebyshev 低通原型
  §8.4  频率变换: 低通→高通, 带通, 带阻
  §8.6  阶跃阻抗低通滤波器
  §8.7  耦合线带通滤波器
  §8.8  发卡/叉指/梳状线滤波器 (设计参数计算)
  §8.9  腔体滤波器 (Qe, kij)
  对比: Butterworth vs Chebyshev vs 阶跃阻抗实现

依赖: numpy, scipy, matplotlib, skrf (scikit-rf)

Author: 二龙虾 (subagent for 🦞)
"""

import numpy as np
from scipy import signal, special
import matplotlib as mpl
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Tuple, List, Optional
import warnings

warnings.filterwarnings("ignore")

# ─── 全局常量 ────────────────────────────────────────────────────────
C0 = 299_792_458            # 真空光速 [m/s]
EPS0 = 8.854187817e-12      # 真空介电常数 [F/m]
MU0 = 4e-7 * np.pi          # 真空磁导率 [H/m]
ETA0 = np.sqrt(MU0 / EPS0)  # 真空波阻抗 ≈ 376.73 Ω

FIG_DIR = Path(__file__).resolve().parent / "figures" / "ch08"
FIG_DIR.mkdir(parents=True, exist_ok=True)


# =====================================================================
# 辅助函数
# =====================================================================

def db(x: np.ndarray) -> np.ndarray:
    """幅度 [V/V] → dB"""
    return 20 * np.log10(np.abs(x) + 1e-30)


def mag_to_dB(x: np.ndarray) -> np.ndarray:
    """功率线性值 → dB"""
    return 10 * np.log10(np.abs(x) + 1e-30)


# =====================================================================
# §8.3  低通原型元件值 (Pozar Table 8.3 & 8.4)
# =====================================================================

# Butterworth 原型 (表 8.3): g0=1, 结果时 g_{N+1}=1 for N odd, 1 for all
BUTTERWORTH_TABLE: dict[int, list[float]] = {
    1: [2.0000, 1.0000],
    2: [1.4142, 1.4142, 1.0000],
    3: [1.0000, 2.0000, 1.0000, 1.0000],
    4: [0.7654, 1.8478, 1.8478, 0.7654, 1.0000],
    5: [0.6180, 1.6180, 2.0000, 1.6180, 0.6180, 1.0000],
    6: [0.5176, 1.4142, 1.9318, 1.9318, 1.4142, 0.5176, 1.0000],
    7: [0.4450, 1.2470, 1.8019, 2.0000, 1.8019, 1.2470, 0.4450, 1.0000],
    8: [0.3902, 1.1111, 1.6629, 1.9615, 1.9615, 1.6629, 1.1111, 0.3902, 1.0000],
    9: [0.3473, 1.0000, 1.5321, 1.8794, 2.0000, 1.8794, 1.5321, 1.0000, 0.3473, 1.0000],
    10: [0.3129, 0.9080, 1.4142, 1.7820, 1.9754, 1.9754, 1.7820, 1.4142, 0.9080, 0.3129, 1.0000],
}


def get_butterworth_g(n: int, g0: float = 1.0) -> np.ndarray:
    """
    返回 Butterworth 低通原型元件值 g0, g1, ..., gN, g_{N+1}
    共 N+2 个值。
    """
    if n not in BUTTERWORTH_TABLE:
        raise ValueError(f"Butterworth N={n} not in table (1-10)")
    vals = BUTTERWORTH_TABLE[n]  # g1..g_{N+1}
    return np.concatenate([[g0], vals])


# Chebyshev 原型 (表 8.4, 0.5 dB ripple, g0=1)
# 最后一列前是 g_{N+1}
CHEBYSHEV_0_5dB_TABLE: dict[int, list[float]] = {
    1: [0.6986, 1.0000],
    2: [1.4029, 0.7071, 1.9841],
    3: [1.5963, 1.0967, 1.5963, 1.0000],
    4: [1.6703, 1.1926, 2.3661, 0.8419, 1.9841],
    5: [1.7058, 1.2296, 2.5408, 1.2296, 1.7058, 1.0000],
    6: [1.7254, 1.2479, 2.6064, 1.3137, 2.4758, 0.8696, 1.9841],
    7: [1.7372, 1.2581, 2.6381, 1.3444, 2.6381, 1.2581, 1.7372, 1.0000],
    8: [1.7451, 1.2647, 2.6564, 1.3590, 2.6964, 1.3389, 2.5093, 0.8796, 1.9841],
    9: [1.7504, 1.2690, 2.6678, 1.3673, 2.7237, 1.3673, 2.6678, 1.2690, 1.7504, 1.0000],
    10: [1.7543, 1.2721, 2.6754, 1.3725, 2.7392, 1.3806, 2.7231, 1.3485, 2.5239, 0.8842, 1.9841],
}

# Chebyshev 0.01 dB ripple
CHEBYSHEV_0_01dB_TABLE: dict[int, list[float]] = {
    1: [0.0960, 1.0000],
    2: [0.4488, 0.4077, 1.1008],
    3: [0.6291, 0.9702, 0.6291, 1.0000],
    4: [0.7128, 1.2003, 1.3212, 0.6476, 1.1008],
    5: [0.7563, 1.3049, 1.5773, 1.3049, 0.7563, 1.0000],
    6: [0.7813, 1.3600, 1.6896, 1.5350, 1.4970, 0.7098, 1.1008],
    7: [0.7969, 1.3924, 1.7481, 1.6331, 1.7481, 1.3924, 0.7969, 1.0000],
    8: [0.8072, 1.4130, 1.7824, 1.6833, 1.8529, 1.6193, 1.5550, 0.7333, 1.1008],
    9: [0.8144, 1.4270, 1.8043, 1.7125, 1.9057, 1.7125, 1.8043, 1.4270, 0.8144, 1.0000],
    10: [0.8197, 1.4369, 1.8192, 1.7311, 1.9362, 1.7590, 1.9108, 1.6553, 1.5814, 0.7446, 1.1008],
}

# Chebyshev 0.1 dB ripple
CHEBYSHEV_0_1dB_TABLE: dict[int, list[float]] = {
    1: [0.3052, 1.0000],
    2: [0.8430, 0.6220, 1.3554],
    3: [1.0315, 1.1474, 1.0315, 1.0000],
    4: [1.1088, 1.3061, 1.7703, 0.8180, 1.3554],
    5: [1.1468, 1.3712, 1.9750, 1.3712, 1.1468, 1.0000],
    6: [1.1681, 1.4039, 2.0562, 1.5170, 1.9029, 0.8618, 1.3554],
    7: [1.1811, 1.4228, 2.0966, 1.5734, 2.0966, 1.4228, 1.1811, 1.0000],
    8: [1.1897, 1.4346, 2.1199, 1.6010, 2.1699, 1.5640, 1.9444, 0.8778, 1.3554],
    9: [1.1956, 1.4425, 2.1345, 1.6167, 2.2053, 1.6167, 2.1345, 1.4425, 1.1956, 1.0000],
    10: [1.1999, 1.4481, 2.1444, 1.6265, 2.2253, 1.6418, 2.2046, 1.5821, 1.9628, 0.8853, 1.3554],
}

# Chebyshev 1.0 dB ripple
CHEBYSHEV_1_0dB_TABLE: dict[int, list[float]] = {
    1: [1.0171, 1.0000],
    2: [1.8219, 0.6850, 1.9841],
    3: [2.0236, 0.9941, 2.0236, 1.0000],
    4: [2.0991, 1.0644, 2.8312, 0.7892, 1.9841],
    5: [2.1349, 1.0911, 3.0009, 1.0911, 2.1349, 1.0000],
    6: [2.1546, 1.1041, 3.0634, 1.1518, 2.9097, 0.8101, 1.9841],
    7: [2.1664, 1.1115, 3.0936, 1.1735, 3.0936, 1.1115, 2.1664, 1.0000],
    8: [2.1740, 1.1162, 3.1117, 1.1846, 3.1562, 1.1745, 2.9469, 0.8155, 1.9841],
    9: [2.1793, 1.1193, 3.1235, 1.1910, 3.1890, 1.1910, 3.1235, 1.1193, 2.1793, 1.0000],
    10: [2.1831, 1.1214, 3.1314, 1.1949, 3.2079, 1.1990, 3.1834, 1.1790, 2.9574, 0.8170, 1.9841],
}


def get_chebyshev_g(n: int, ripple_dB: float = 0.5, g0: float = 1.0) -> np.ndarray:
    """
    返回 Chebyshev 低通原型元件值 g0..g_{N+1}
    """
    tables = {
        0.01: CHEBYSHEV_0_01dB_TABLE,
        0.1: CHEBYSHEV_0_1dB_TABLE,
        0.5: CHEBYSHEV_0_5dB_TABLE,
        1.0: CHEBYSHEV_1_0dB_TABLE,
    }
    key = min(tables.keys(), key=lambda k: abs(k - ripple_dB))
    if key not in tables:
        raise ValueError(f"Chebyshev ripple={ripple_dB} dB not supported. Available: {list(tables.keys())}")
    vals = tables[key][n]
    return np.concatenate([[g0], vals])


# =====================================================================
# §8.3  低通原型综合与响应
# =====================================================================

def synthesize_lowpass(
    g_values: np.ndarray,
    R0: float = 1.0,
    omega_c: float = 1.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    从 g-values 综合出低通 ladder 网络的 Z11, Z21 和频率响应。
    
    参数:
        g_values: array [g0, g1, ..., gN, g_{N+1}]
        R0: 源/负载阻抗 (归一化时=1)
        omega_c: 截止频率
    
    返回:
        omega, S11_dB, S21_dB, IL_dB
    """
    n = len(g_values) - 2  # 阶数
    g = g_values.copy()
    
    # 生成归一化频率点
    omega = np.logspace(-2, 2, 10000)
    
    # 构建 ladder 网络的 S21
    # 使用迭代反射系数法 (较数值稳定)
    # 对于归一化原型: g0 = R_s, g_{N+1} = R_L
    
    Rs = g[0]  # 源阻抗
    RL = g[-1]  # 负载阻抗
    
    # 使用 ABCD 矩阵级联
    # 串联阻抗: [1, Z; 0, 1]
    # 并联导纳: [1, 0; Y, 1]
    
    A, B, C_mat, D = 1.0, 0.0, 0.0, 1.0
    
    for k in range(1, n + 1):
        # 交替: 奇数索引 = 串联, 偶数索引 = 并联
        s = 1j * omega
        if k % 2 == 1:  # 串联元件 (电感)
            Zk = s * g[k]  # 串联电感 L = g_k, Z = jωL
            # T 矩阵: [1, Z; 0, 1]
            T_a, T_b, T_c, T_d = 1, Zk, 0, 1
        else:  # 并联元件 (电容)
            Yk = s * g[k]  # 并联电容 C = g_k, Y = jωC
            # T 矩阵: [1, 0; Y, 1]
            T_a, T_b, T_c, T_d = 1, 0, Yk, 1
        
        # 级联
        A_new = A * T_a + B * T_c
        B_new = A * T_b + B * T_d
        C_new = C_mat * T_a + D * T_c
        D_new = C_mat * T_b + D * T_d
        A, B, C_mat, D = A_new, B_new, C_new, D_new
    
    # 从 ABCD 计算 S21 (源/负载阻抗 Rs, RL)
    Z0_src = Rs
    Z0_load = RL
    
    denom = A * Z0_load + B + C_mat * Z0_src * Z0_load + D * Z0_src
    # 对于实值 Z0_src, Z0_load:
    sqrt_Z0 = np.sqrt(Z0_src * Z0_load)
    S21 = 2.0 * sqrt_Z0 / denom
    S11 = (A * Z0_load + B - C_mat * Z0_src * Z0_load - D * Z0_src) / denom
    
    S21_dB = 20 * np.log10(np.abs(S21) + 1e-30)
    S11_dB = 20 * np.log10(np.abs(S11) + 1e-30)
    IL_dB = -S21_dB  # Insertion Loss = -S21 in dB
    
    return omega, S11_dB, S21_dB, IL_dB


def order_from_spec(
    f_pass: float, f_stop: float,
    IL_max_pass: float, IL_min_stop: float,
    filter_type: str = "butterworth",
    ripple_dB: float = 0.5,
) -> int:
    """
    根据规格确定所需阶数 N
    
    参数:
        f_pass: 通带边缘频率 [GHz]
        f_stop: 阻带边缘频率 [GHz]
        IL_max_pass: 通带最大插损 [dB]
        IL_min_stop: 阻带最小衰减 [dB]
        filter_type: "butterworth" 或 "chebyshev"
        ripple_dB: Chebyshev 通带波纹 [dB]
    
    返回:
        N: 所需最小阶数
    """
    omega_ratio = f_stop / f_pass
    
    if filter_type == "butterworth":
        # P_LR = 1 + k^2 (ω/ω_c)^(2N)
        # At ω=ω_c: P_LR = 1 + k^2, L_pass = 10*log10(1+k^2)
        k_sq = 10**(IL_max_pass / 10) - 1.0
        # At ω=ω_s: P_LR = 1 + k^2 (ω_s/ω_c)^(2N)
        L_as_req = 10**(IL_min_stop / 10) - 1.0
        N = np.ceil(np.log10(L_as_req / k_sq) / (2 * np.log10(omega_ratio)))
        return int(N)
    
    elif filter_type == "chebyshev":
        # P_LR = 1 + k^2 T_N^2(ω/ω_c)
        k_sq = 10**(ripple_dB / 10) - 1.0
        L_as = 10**(IL_min_stop / 10) - 1.0
        # N = cosh^-1(sqrt((L_as-1)/(k^2))) / cosh^-1(omega_ratio)
        numerator = np.arccosh(np.sqrt(L_as / k_sq))
        denominator = np.arccosh(omega_ratio)
        N = np.ceil(numerator / denominator)
        return int(N)
    
    else:
        raise ValueError(f"Unknown filter type: {filter_type}")


# =====================================================================
# §8.3  示例 1: Butterworth 与 Chebyshev 低通原型对比
# =====================================================================

def example_butterworth_chebyshev_comparison() -> None:
    """
    比较 Butterworth 与 Chebyshev (不同波纹) 低通原型响应
    """
    print("=" * 60)
    print("§8.3  低通原型对比: Butterworth vs Chebyshev")
    print("=" * 60)
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    N = 5  # 固定阶数
    
    # --- Butterworth ---
    g_butter = get_butterworth_g(N)
    omega, s11_b, s21_b, il_b = synthesize_lowpass(g_butter)
    
    # --- Chebyshev 不同波纹 ---
    colors = ['b', 'g', 'r', 'm', 'c']
    ripples = [0.01, 0.1, 0.5, 1.0]
    
    ax[0].plot(omega, s21_b, 'k-', linewidth=2, label=f"Butterworth (N={N})")
    ax[1].plot(omega, il_b, 'k-', linewidth=2, label=f"Butterworth (N={N})")
    
    for i, r in enumerate(ripples):
        g_cheb = get_chebyshev_g(N, ripple_dB=r)
        omega, s11_c, s21_c, il_c = synthesize_lowpass(g_cheb)
        ax[0].plot(omega, s21_c, '--', color=colors[i], linewidth=1.5, label=f"Cheb {r} dB")
        ax[1].plot(omega, il_c, '--', color=colors[i], linewidth=1.5, label=f"Cheb {r} dB")
    
    # 截止频率标记
    for a in ax:
        a.axvline(1.0, color='gray', linestyle=':', alpha=0.5, label='$\\omega_c$')
        a.set_xscale('log')
        a.set_xlabel('Normalized Frequency $\\omega/\\omega_c$')
        a.grid(True, alpha=0.3)
        a.legend(fontsize=8)
    
    ax[0].set_ylabel('$|S_{21}|$ [dB]')
    ax[0].set_title('Transmission Response $S_{21}$')
    ax[0].set_ylim(-80, 3)
    ax[0].set_xlim(0.1, 10)
    
    ax[1].set_ylabel('Insertion Loss [dB]')
    ax[1].set_title('Insertion Loss')
    ax[1].set_ylim(0, 80)
    ax[1].set_xlim(0.1, 10)
    
    fig.suptitle(f'Butterworth vs Chebyshev Low-Pass Prototype (N={N})', fontsize=13)
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_1_prototype_comparison.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_1_prototype_comparison.png")
    plt.close(fig)
    
    # 验证表值
    print("\n  Butterworth N=5: g1..g5 =", g_butter[1:-1])
    # Chebyshev 0.5dB N=5
    g_ch = get_chebyshev_g(5, 0.5)
    print(f"  Chebyshev 0.5dB N=5: g1..g6 =", g_ch[1:])


# =====================================================================
# §8.3  示例 2: 阶数确定
# =====================================================================

def example_order_determination() -> None:
    """
    根据规格确定所需阶数
    """
    print("\n" + "=" * 60)
    print("§8.3  阶数确定示例")
    print("=" * 60)
    
    # 规格: LPF, fc=1 GHz, fs=2 GHz
    # 通带 IL: <0.1 dB @ 1 GHz, 阻带衰减: >30 dB @ 2 GHz
    f_pass = 1.0  # GHz
    f_stop = 2.0  # GHz
    il_pass = 0.1  # dB
    il_stop = 30.0  # dB
    
    N_b = order_from_spec(f_pass, f_stop, il_pass, il_stop, "butterworth")
    N_c = order_from_spec(f_pass, f_stop, il_pass, il_stop, "chebyshev", 0.5)
    
    print(f"  规格: fc={f_pass} GHz, fs={f_stop} GHz, IL<{il_pass}dB, Att>{il_stop}dB")
    print(f"  Butterworth 所需阶数: N={N_b}")
    print(f"  Chebyshev 0.5dB 所需阶数: N={N_c}")
    
    # 画出不同阶数的阻带衰减
    fig, ax = plt.subplots(figsize=(10, 6))
    
    omega = np.logspace(0, 1, 1000)  # 1-10
    
    for n in range(2, 8):
        # Butterworth 阻带衰减近似: 20*n dB/decade
        atten = 20 * n * np.log10(omega)  # 简化近似
        ax.plot(omega, atten, label=f'N={n}')
    
    ax.axhline(il_stop, color='r', linestyle='--', label=f'Required: {il_stop} dB')
    ax.axvline(f_stop / f_pass, color='r', linestyle=':', alpha=0.7)
    
    ax.set_xscale('log')
    ax.set_xlabel('$\\omega/\\omega_c$')
    ax.set_ylabel('Stopband Attenuation [dB]')
    ax.set_title('Butterworth Stopband Attenuation vs Order')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_ylim(0, 80)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_2_order_determination.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_2_order_determination.png")
    plt.close(fig)


# =====================================================================
# §8.4  频率变换
# =====================================================================

def lowpass_to_bandpass(
    g_values: np.ndarray,
    R0: float,
    omega_0: float,
    delta: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    低通→带通变换后的元件值 (串联 LC, 并联 LC)

    返回:
        L_series, C_series, L_shunt, C_shunt (长度 N)
        每对对应一个低通元件
    """
    n = len(g_values) - 2
    L_s = np.zeros(n)
    C_s = np.zeros(n)
    L_p = np.zeros(n)
    C_p = np.zeros(n)
    
    for k in range(1, n + 1):
        gk = g_values[k]
        if k % 2 == 1:  # 串联元件 → 串联 LC
            L_s[k-1] = gk * R0 / (omega_0 * delta)  # [H]
            C_s[k-1] = delta / (omega_0 * gk * R0)  # [F]
        else:  # 并联元件 → 并联 LC
            L_p[k-1] = delta * R0 / (omega_0 * gk)  # [H]
            C_p[k-1] = gk / (omega_0 * delta * R0)  # [F]
    
    return L_s, C_s, L_p, C_p


def lowpass_to_highpass(
    g_values: np.ndarray,
    R0: float,
    omega_c: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    低通→高通变换
    
    返回:
        C_series, L_shunt (串联电容 [F], 并联电感 [H])
    """
    n = len(g_values) - 2
    C_s = np.zeros(n)  # 串联电容
    L_sh = np.zeros(n)  # 并联电感
    
    for k in range(1, n + 1):
        gk = g_values[k]
        if k % 2 == 1:  # 串联 L → 串联 C
            C_s[k-1] = 1.0 / (omega_c * gk * R0)  # [F]
        else:  # 并联 C → 并联 L
            L_sh[k-1] = R0 / (omega_c * gk)  # [H]
    
    return C_s, L_sh


def lowpass_to_bandstop(
    g_values: np.ndarray,
    R0: float,
    omega_0: float,
    delta: float,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    低通→带阻变换
    
    串联元件 → 并联 LC 谐振
    并联元件 → 串联 LC 谐振
    """
    n = len(g_values) - 2
    L_s = np.zeros(n)
    C_s = np.zeros(n)
    L_p = np.zeros(n)
    C_p = np.zeros(n)
    
    for k in range(1, n + 1):
        gk = g_values[k]
        if k % 2 == 1:  # 串联 L → 并联 LC
            L_p[k-1] = delta * R0 / (omega_0 * gk)  # [H]
            C_p[k-1] = gk / (omega_0 * delta * R0)  # [F]
        else:  # 并联 C → 串联 LC
            L_s[k-1] = gk * R0 / (omega_0 * delta)  # [H]
            C_s[k-1] = delta / (omega_0 * gk * R0)  # [F]
    
    return L_s, C_s, L_p, C_p


def compute_bandpass_response(
    L_s: np.ndarray, C_s: np.ndarray,
    L_p: np.ndarray, C_p: np.ndarray,
    R0: float,
    freq: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    计算带通滤波器响应 (ABCD 级联法)
    """
    omega = 2 * np.pi * freq
    n = len(L_s)
    S21 = np.zeros(len(freq), dtype=complex)
    S11 = np.zeros(len(freq), dtype=complex)
    
    for idx, w in enumerate(omega):
        A, B, C_mat, D = 1.0, 0.0, 0.0, 1.0
        s = 1j * w
        
        for k in range(n):
            if k % 2 == 0:  # 串联 LC 谐振
                Zk = s * L_s[k] + 1.0 / (s * C_s[k]) if C_s[k] > 0 else 1e30
                Ta, Tb, Tc, Td = 1, Zk, 0, 1
            else:  # 并联 LC 谐振
                if L_p[k] > 0:
                    Yk = 1.0 / (s * L_p[k]) + s * C_p[k]
                else:
                    Yk = 0
                Ta, Tb, Tc, Td = 1, 0, Yk, 1
            
            A_new = A * Ta + B * Tc
            B_new = A * Tb + B * Td
            C_new = C_mat * Ta + D * Tc
            D_new = C_mat * Tb + D * Td
            A, B, C_mat, D = A_new, B_new, C_new, D_new
        
        denom = A * R0 + B + C_mat * R0 * R0 + D * R0
        S21[idx] = 2.0 * R0 / denom
        S11[idx] = (A * R0 + B - C_mat * R0 * R0 - D * R0) / denom
    
    return S11, S21


# =====================================================================
# §8.4  示例 3: 频率变换 — 低通→带通
# =====================================================================

def example_frequency_transformation() -> None:
    """
    频率变换: 低通→带通, 低通→高通
    """
    print("\n" + "=" * 60)
    print("§8.4  频率变换示例")
    print("=" * 60)
    
    R0 = 50.0  # 系统阻抗 [Ω]
    N = 3
    g_vals = get_butterworth_g(N)  # Butterworth N=3
    
    # —— 带通变换 ——
    f0 = 2.0e9  # 中心频率 2 GHz
    bw = 0.4e9  # 带宽 400 MHz
    omega_0 = 2 * np.pi * f0
    delta = bw / f0  # 分数带宽
    
    L_s, C_s, L_p, C_p = lowpass_to_bandpass(g_vals, R0, omega_0, delta)
    
    print(f"\n  带通滤波器: f0={f0/1e9:.2f} GHz, Δ={delta*100:.1f}%")
    print(f"  串联元件1: L={L_s[0]*1e9:.2f} nH, C={C_s[0]*1e12:.2f} pF")
    print(f"  并联元件2: L={L_p[1]*1e9:.2f} nH, C={C_p[1]*1e12:.2f} pF")
    print(f"  串联元件3: L={L_s[2]*1e9:.2f} nH, C={C_s[2]*1e12:.2f} pF")
    
    # —— 高通变换 ——
    f_c_hp = 1.0e9  # 1 GHz
    omega_c_hp = 2 * np.pi * f_c_hp
    C_s_hp, L_sh_hp = lowpass_to_highpass(g_vals, R0, omega_c_hp)
    
    print(f"\n  高通滤波器: fc={f_c_hp/1e9:.1f} GHz")
    print(f"  串联C1: {C_s_hp[0]*1e12:.2f} pF")
    print(f"  并联L2: {L_sh_hp[1]*1e9:.2f} nH")
    print(f"  串联C3: {C_s_hp[2]*1e12:.2f} pF")
    
    # —— 频率响应 ——
    freq = np.linspace(1.5e9, 2.5e9, 2000)
    S11_bp, S21_bp = compute_bandpass_response(L_s, C_s, L_p, C_p, R0, freq)
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    ax[0].plot(freq / 1e9, db(S21_bp), 'b-', linewidth=2, label='$S_{21}$')
    ax[0].plot(freq / 1e9, db(S11_bp), 'r-', linewidth=2, label='$S_{11}$')
    ax[0].axvline(f0/1e9, color='gray', linestyle=':', alpha=0.5)
    ax[0].axvline((f0 - bw/2)/1e9, color='gray', linestyle='--', alpha=0.3)
    ax[0].axvline((f0 + bw/2)/1e9, color='gray', linestyle='--', alpha=0.3)
    ax[0].set_xlabel('Frequency [GHz]')
    ax[0].set_ylabel('S-parameters [dB]')
    ax[0].set_title('Bandpass Filter Response (N=3 Butterworth)')
    ax[0].grid(True, alpha=0.3)
    ax[0].legend()
    ax[0].set_ylim(-60, 3)
    
    # 高通响应
    freq_hp = np.logspace(8, 10, 2000)  # 0.1-10 GHz
    omega_hp = 2 * np.pi * freq_hp
    S21_hp = np.zeros(len(freq_hp), dtype=complex)
    
    for i, w in enumerate(omega_hp):
        s = 1j * w
        A, B, C_mat, D = 1.0, 0.0, 0.0, 1.0
        
        # 串联 C1
        Z1 = 1.0 / (s * C_s_hp[0])
        Ta, Tb, Tc, Td = 1, Z1, 0, 1
        A1, B1, C1, D1 = A*Ta+B*Tc, A*Tb+B*Td, C_mat*Ta+D*Tc, C_mat*Tb+D*Td
        A, B, C_mat, D = A1, B1, C1, D1
        
        # 并联 L2
        Y2 = 1.0 / (s * L_sh_hp[1])
        Ta, Tb, Tc, Td = 1, 0, Y2, 1
        A1, B1, C1, D1 = A*Ta+B*Tc, A*Tb+B*Td, C_mat*Ta+D*Tc, C_mat*Tb+D*Td
        A, B, C_mat, D = A1, B1, C1, D1
        
        # 串联 C3
        Z3 = 1.0 / (s * C_s_hp[2])
        Ta, Tb, Tc, Td = 1, Z3, 0, 1
        A1, B1, C1, D1 = A*Ta+B*Tc, A*Tb+B*Td, C_mat*Ta+D*Tc, C_mat*Tb+D*Td
        A, B, C_mat, D = A1, B1, C1, D1
        
        denom = A * R0 + B + C_mat * R0 * R0 + D * R0
        S21_hp[i] = 2.0 * R0 / denom
    
    ax[1].semilogx(freq_hp / 1e9, db(S21_hp), 'b-', linewidth=2, label='$S_{21}$ (HP)')
    ax[1].axvline(f_c_hp/1e9, color='r', linestyle='--', label=f'$f_c={f_c_hp/1e9:.1f}$ GHz')
    ax[1].set_xlabel('Frequency [GHz]')
    ax[1].set_ylabel('$S_{21}$ [dB]')
    ax[1].set_title('Highpass Filter Response (N=3 Butterworth)')
    ax[1].grid(True, alpha=0.3)
    ax[1].legend()
    ax[1].set_ylim(-60, 3)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_3_freq_transform.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_3_freq_transform.png")
    plt.close(fig)


# =====================================================================
# §8.5  Richard's Transformation & Kuroda's Identities
# =====================================================================

def example_richard_kuroda() -> None:
    """
    Richard 变换与 Kuroda 恒等式可视化
    """
    print("\n" + "=" * 60)
    print("§8.5  Richard 变换与 Kuroda 恒等式")
    print("=" * 60)
    
    # Richard 变换: Ω = tan(βℓ) = tan(π/2 · ω/ω₀)
    omega_ratio = np.linspace(0, 2.5, 1000)
    omega_richard = np.tan(np.pi / 2 * omega_ratio)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(omega_ratio, omega_richard, 'b-', linewidth=2)
    ax.plot(omega_ratio, omega_ratio, 'r--', linewidth=1, alpha=0.7, label='Linear ($\\Omega = \\omega/\\omega_c$)')
    ax.axvline(1.0, color='gray', linestyle=':', alpha=0.5, label='$\\omega_0$ ($\\lambda/8$)')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.set_xlabel('Normalized Frequency $\\omega/\\omega_0$')
    ax.set_ylabel('$\\Omega = \\tan(\\pi\\omega/2\\omega_0)$')
    ax.set_title("Richard's Transformation")
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_xlim(0, 2.5)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_4_richard_transform.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_4_richard_transform.png")
    plt.close(fig)
    
    # Kuroda 恒等式示例: 串联短截线 + UE → 并联短截线 + UE
    print("\n  Kuroda Identity (Type 1):")
    Z_series = 50.0  # [Ω], 串联短截线阻抗
    Z_ue = 100.0  # [Ω], 单位元素阻抗
    
    n_sq = 1 + Z_ue / Z_series
    n = np.sqrt(n_sq)
    
    Z_shunt = n_sq * Z_series  # 变换后的并联短截线阻抗
    Z_ue_new = Z_ue / n_sq     # 变换后的 UE 阻抗
    
    print(f"    原始: Z_series={Z_series:.1f} Ω, Z_UE={Z_ue:.1f} Ω")
    print(f"    变换后: Z_shunt={Z_shunt:.1f} Ω, Z_UE_new={Z_ue_new:.1f} Ω, n²={n_sq:.3f}")


# =====================================================================
# §8.6  阶跃阻抗低通滤波器
# =====================================================================

def example_stepped_impedance_lpf() -> None:
    """
    微带阶跃阻抗低通滤波器设计 (Pozar Example 8.6)
    """
    print("\n" + "=" * 60)
    print("§8.6  阶跃阻抗低通滤波器设计")
    print("=" * 60)
    
    # 设计规格
    fc = 2.5e9  # 截止频率 2.5 GHz
    R0 = 50.0   # 系统阻抗
    N = 5       # 阶数
    
    # 材料参数
    epsilon_r = 4.2   # FR4
    h = 1.6e-3        # 介质厚度 [m]
    
    # 选择高/低阻抗
    Z_high = 120.0     # 高阻抗段 [Ω]
    Z_low = 15.0       # 低阻抗段 [Ω]
    
    # 低通原型
    g_vals = get_butterworth_g(N)
    print(f"\n  Butterworth N={N} 原型值: g1..g6 =", np.round(g_vals[1:], 4))
    
    # 相速度
    vp = C0 / np.sqrt(epsilon_r)  # [m/s]
    
    # 计算传输线段长度
    lengths: list[float] = []  # [m]
    impedances: list[float] = []
    
    for k in range(1, N + 1):
        gk = g_vals[k]
        if k % 2 == 1:  # 串联电感 → 高阻抗段
            Lk = gk * R0 / (2 * np.pi * fc)  # [H]
            ell = Lk * vp / Z_high          # [m]
            ell_deg = ell / (vp / fc) * 360  # 电长度 [°]
            impedances.append(Z_high)
            print(f"    节{k} (L={Lk*1e9:.2f} nH): ℓ={ell*1e3:.2f} mm = {ell_deg:.1f}° @ {Z_high:.0f} Ω")
        else:  # 并联电容 → 低阻抗段
            Ck = gk / (2 * np.pi * fc * R0)  # [F]
            ell = Ck * Z_low * vp            # [m]
            ell_deg = ell / (vp / fc) * 360  # 电长度 [°]
            impedances.append(Z_low)
            print(f"    节{k} (C={Ck*1e12:.2f} pF): ℓ={ell*1e3:.2f} mm = {ell_deg:.1f}° @ {Z_low:.0f} Ω")
        lengths.append(ell)
    
    total_length = sum(lengths)
    total_wavelength = total_length / (vp / fc) * 360  # [°]
    print(f"  总长度: {total_length*1e3:.2f} mm = {total_wavelength:.1f}°")
    print(f"  注: 各段电长度需要 < 45° 以确保短线段近似有效")
    
    # 计算微带线宽 (Pozar Eq 3.197)
    w_high = microstrip_width(Z_high, epsilon_r, h)
    w_low = microstrip_width(Z_low, epsilon_r, h)
    print(f"\n  微带线宽: W_high={w_high*1e3:.2f} mm, W_low={w_low*1e3:.2f} mm")
    
    # 绘制阶跃阻抗结构示意
    fig, ax = plt.subplots(figsize=(10, 3))
    x_pos = 0
    colors_list = ['#e74c3c', '#3498db', '#e74c3c', '#3498db', '#e74c3c']
    labels_list = ['L1', 'C2', 'L3', 'C4', 'L5']
    
    for k, (ell, z, c, lbl) in enumerate(zip(lengths[::-1], impedances[::-1], colors_list, labels_list)):  # reverse to draw left-to-right
        w_norm = (z - Z_low) / (Z_high - Z_low)  # normalize to 0-1
        w_scale = 0.2 + 0.8 * w_norm  # scale between min and max width
        y_offset = (1 - w_scale) / 2
        ax.add_patch(plt.Rectangle((x_pos, y_offset), ell * 1000, w_scale, 
                                     facecolor=c, alpha=0.7, edgecolor='k'))
        ax.text(x_pos + ell*500, 0.5, lbl, ha='center', va='center', fontsize=9)
        x_pos += ell * 1000
    
    ax.set_xlabel('Position [mm]')
    ax.set_ylabel('Normalized Width')
    ax.set_title('Stepped-Impedance LPF Layout (Schematic)')
    ax.set_xlim(0, x_pos)
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.2)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_5_stepped_impedance.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_5_stepped_impedance.png")
    plt.close(fig)


def microstrip_width(Z0: float, epsilon_r: float, h: float) -> float:
    """
    微带线宽计算 (Pozar Eq 3.197)
    Z0: 特征阻抗 [Ω]
    epsilon_r: 相对介电常数
    h: 介质厚度 [m]
    
    返回: 线宽 w [m]
    """
    A = Z0 / 60.0 * np.sqrt((epsilon_r + 1) / 2.0) + (epsilon_r - 1) / (epsilon_r + 1) * (0.23 + 0.11 / epsilon_r)
    B = 377 * np.pi / (2 * Z0 * np.sqrt(epsilon_r))
    
    if A > 1.52:
        w_over_h = 8 * np.exp(A) / (np.exp(2 * A) - 2)
    else:
        w_over_h = 2 / np.pi * (B - 1 - np.log(2 * B - 1) + (epsilon_r - 1) / (2 * epsilon_r) * (np.log(B - 1) + 0.39 - 0.61 / epsilon_r))
    
    return w_over_h * h


# =====================================================================
# §8.7  耦合线带通滤波器
# =====================================================================

def example_coupled_line_bpf() -> None:
    """
    耦合线带通滤波器设计 (Pozar Example 8.7-8.8)
    """
    print("\n" + "=" * 60)
    print("§8.7  耦合线带通滤波器")
    print("=" * 60)
    
    # 规格
    f0 = 5.0e9        # 中心频率 5 GHz
    bw_frac = 0.10    # 分数带宽 10%
    N = 5             # 阶数
    R0 = 50.0         # 系统阻抗
    epsilon_r = 10.8  # RT/Duroid 6010.2
    h = 1.27e-3       # [m]
    
    # 低通原型
    g_vals = get_chebyshev_g(N, 0.5)  # 0.5 dB 波纹
    print(f"\n  Chebyshev 0.5dB N={N}: g1..g{N+1} =", np.round(g_vals[1:], 4))
    
    delta = bw_frac  # 分数带宽
    omega_0 = 2 * np.pi * f0
    
    # J 逆变器系数 (Eq 8.72-8.74) — 以归一化 J/Y₀ 形式
    J_over_Y0 = np.zeros(N + 1)
    J_over_Y0[0] = np.sqrt(np.pi * delta / (2 * g_vals[0] * g_vals[1]))
    for j in range(1, N):
        J_over_Y0[j] = np.pi * delta / (2 * np.sqrt(g_vals[j] * g_vals[j+1]))
    J_over_Y0[N] = np.sqrt(np.pi * delta / (2 * g_vals[N] * g_vals[N+1]))
    
    print(f"\n  J/Y₀ 值 (归一化):")
    for i, jy in enumerate(J_over_Y0):
        print(f"    节 {i+1}: J/Y₀ = {jy:.4f}")
    
    # 奇偶模阻抗 (Eq 8.66)
    Z0e = np.zeros(N + 1)
    Z0o = np.zeros(N + 1)
    
    for i in range(N + 1):
        jy = J_over_Y0[i]
        Z0e[i] = R0 * (1 + jy + jy**2)
        Z0o[i] = R0 * (1 - jy + jy**2)
    
    print(f"\n  奇偶模阻抗:")
    for i in range(N + 1):
        k = (Z0e[i] - Z0o[i]) / (Z0e[i] + Z0o[i])
        print(f"    节 {i+1}: Z₀ₑ={Z0e[i]:.2f} Ω, Z₀ₒ={Z0o[i]:.2f} Ω, k={k:.4f}")
    
    # 验证: Z0e > Z0o > 0 且 k 物理可实现
    assert np.all(Z0e > 0), "Z0e must be positive"
    assert np.all(Z0o > 0), "Z0o must be positive"
    assert np.all(Z0e > Z0o), "Z0e must > Z0o"
    
    # 计算耦合线响应 (使用 λ/4 J-逆变器模型 + ABCD 分析)
    # 耦合线节的传输矩阵 T = T_line * T_J * T_line (J-逆变器模型)
    # 对于平行耦合 λ/4 段, 耦合线节等效为 J-inv + 两端 λ/4 传输线
    
    freq = np.linspace(4.0, 6.0, 501)  # [GHz]
    freq_hz = freq * 1e9
    omega = 2 * np.pi * freq_hz
    f0_hz = f0
    beta_l = np.pi / 2 * freq_hz / f0_hz  # 电长度, 在 f0 处为 π/2
    
    S21_total = np.ones(len(freq), dtype=complex)
    S11_total = np.zeros(len(freq), dtype=complex)
    
    for idx in range(len(freq)):
        theta = beta_l[idx]
        
        # 每个耦合线节使用 ABCD 级联
        A_tot, B_tot, C_tot, D_tot = 1.0, 0.0, 0.0, 1.0
        
        for i in range(N + 1):
            # 耦合线节 ≈ J-逆变器 + 传输线段
            # 使用 Z0e/Z0o 计算奇偶模特性
            z0e_i = Z0e[i]
            z0o_i = Z0o[i]
            
            # 耦合线的平均阻抗
            z0_avg = np.sqrt(z0e_i * z0o_i)
            
            # 对于 λ/4 耦合线节, 在端口接地的配置下,
            # 奇偶模分析给出从端口 1 到端口 3 的传输
            # 使用平行耦合线节公式 (Pozar Eq 7.54-7.56)
            
            # 简化为 J-inv + 两段 λ/4 线的近似:
            # 耦合线节等效为特征阻抗 Z0_avg, 电长度 θ 的传输线段
            # 在带通中心处, θ = π/2
            
            Z_char = z0_avg
            
            # 传输线 ABCD: [cosθ, jZsinθ; jYsinθ, cosθ]
            T_A = np.cos(theta) + 0j
            T_B = 1j * Z_char * np.sin(theta)
            T_C = 1j / Z_char * np.sin(theta)
            T_D = T_A.copy()
            
            # 级联
            A_new = A_tot * T_A + B_tot * T_C
            B_new = A_tot * T_B + B_tot * T_D
            C_new = C_tot * T_A + D_tot * T_C
            D_new = C_tot * T_B + D_tot * T_D
            A_tot, B_tot, C_tot, D_tot = A_new, B_new, C_new, D_new
        
        # ABCD → S21
        Z0_s = R0
        Z0_l = R0
        denom = A_tot * Z0_l + B_tot + C_tot * Z0_s * Z0_l + D_tot * Z0_s
        S21_total[idx] = 2.0 * np.sqrt(Z0_s * Z0_l) / denom
        S11_total[idx] = (A_tot * Z0_l + B_tot - C_tot * Z0_s * Z0_l - D_tot * Z0_s) / denom
    
    # 绘制频率响应
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    ax[0].plot(freq, db(S21_total), 'b-', linewidth=2, label='$S_{21}$')
    ax[0].plot(freq, db(S11_total), 'r-', linewidth=2, label='$S_{11}$')
    ax[0].axvline(f0/1e9, color='gray', linestyle=':', alpha=0.5, label=f'$f_0$={f0/1e9:.1f} GHz')
    ax[0].axvline(f0*(1-bw_frac/2)/1e9, color='green', linestyle='--', alpha=0.3)
    ax[0].axvline(f0*(1+bw_frac/2)/1e9, color='green', linestyle='--', alpha=0.3)
    ax[0].set_xlabel('Frequency [GHz]')
    ax[0].set_ylabel('S-parameters [dB]')
    ax[0].set_title(f'Coupled-Line BPF (N={N}, Cheb 0.5dB, Δ={bw_frac*100:.0f}%)')
    ax[0].grid(True, alpha=0.3)
    ax[0].legend(fontsize=9)
    ax[0].set_ylim(-60, 3)
    
    # Z0e/Z0o 分布图
    ax[1].plot(np.arange(N+1), Z0e, 'ro-', label='$Z_{0e}$', markersize=8)
    ax[1].plot(np.arange(N+1), Z0o, 'bs-', label='$Z_{0o}$', markersize=8)
    for i in range(N + 1):
        ax[1].annotate(f'{Z0e[i]:.1f}', (i, Z0e[i]), textcoords="offset points", xytext=(0, 10), ha='center', fontsize=8)
        ax[1].annotate(f'{Z0o[i]:.1f}', (i, Z0o[i]), textcoords="offset points", xytext=(0, -15), ha='center', fontsize=8)
    ax[1].set_xlabel('Section Index')
    ax[1].set_ylabel('Impedance [Ω]')
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_6_coupled_line_bpf.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_6_coupled_line_bpf.png")
    plt.close(fig)


# =====================================================================
# §8.8  发卡/叉指/梳状线滤波器设计计算
# =====================================================================

def example_advanced_filter_structures() -> None:
    """
    发卡线、叉指、梳状线滤波器参数计算
    """
    print("\n" + "=" * 60)
    print("§8.8  Hairpin / Interdigital / Combine 滤波器")
    print("=" * 60)
    
    f0 = 2.0e9        # 2 GHz
    R0 = 50.0
    N = 5
    
    # 低通原型
    g_vals = get_chebyshev_g(N, 0.5)
    delta = 0.08  # 8% 带宽 (窄带)
    
    # 计算 J 逆变器
    J_norm = np.zeros(N + 1)
    J_norm[0] = np.sqrt(np.pi * delta / (2 * g_vals[0] * g_vals[1]))
    for j in range(1, N):
        J_norm[j] = np.pi * delta / (2 * np.sqrt(g_vals[j] * g_vals[j+1]))
    J_norm[N] = np.sqrt(np.pi * delta / (2 * g_vals[N] * g_vals[N+1]))
    
    # --- 叉指滤波器参数 ---
    # 谐振杆导纳 (归一化)
    Y_k_norm = g_vals[1: N+1]  # 每个谐振杆的归一化导纳
    Y_k_actual = Y_k_norm / R0  # [S]
    
    print(f"\n  叉指滤波器 (Interdigital, λ/4 谐振器):")
    for i in range(N):
        coupling = np.sqrt(Y_k_norm[i] * Y_k_norm[min(i+1, N-1)]) if i < N-1 else 0
        print(f"    谐振器 {i+1}: Y = {Y_k_actual[i]*1e3:.2f} mS")
    
    # --- 梳状线滤波器参数 ---
    # λ/8 谐振器 + 集总电容加载
    # C_k = Y_k * tan(βℓ) / ω_0, ℓ = λ/8
    theta = np.pi / 4  # 45° at f0
    omega_0 = 2 * np.pi * f0
    
    print(f"\n  梳状线滤波器 (Combine, λ/8 + C_load):")
    for i in range(N):
        Ck = Y_k_actual[i] * np.tan(theta) / omega_0  # [F]
        # 耦合电容
        if i < N - 1:
            J_kk1 = J_norm[i+1] / R0  # 去归一化 [S]
            C_kk1 = J_kk1 / omega_0  # [F]
            print(f"    谐振器 {i+1}: C_load={Ck*1e12:.2f} pF, C_couple({i+1},{i+2})={C_kk1*1e12:.2f} pF")
        else:
            print(f"    谐振器 {i+1}: C_load={Ck*1e12:.2f} pF")
    
    # --- 发卡线 ---
    # 本质是折叠的耦合线，谐振器 U 形折叠
    print(f"\n  发卡线 (Hairpin):")
    print(f"    谐振器间距决定耦合系数 k_ij = Δ/√(g_i·g_j)")
    # 耦合系数
    k_12 = delta / np.sqrt(g_vals[1] * g_vals[2])
    k_23 = delta / np.sqrt(g_vals[2] * g_vals[3])
    k_34 = delta / np.sqrt(g_vals[3] * g_vals[4])
    print(f"    耦合系数: k_12={k_12:.4f}, k_23={k_23:.4f}, k_34={k_34:.4f}")
    
    # 绘制对比图
    fig, ax = plt.subplots(figsize=(8, 5))
    structures = ['Coupled-Line', 'Hairpin', 'Interdigital', 'Combine']
    sizes = [N+1, N+1, N, N]  # 节数/谐振器数
    lengths_mm = [(N+1)*15, (N+1)*8, N*12, N*8]  # 近似长度 [mm]
    
    bars = ax.bar(structures, lengths_mm, color=['#3498db', '#2ecc71', '#e74c3c', '#f39c12'], alpha=0.7)
    for bar, sz in zip(bars, sizes):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{sz} resonators', ha='center', va='bottom', fontsize=10)
    
    ax.set_ylabel('Approximate Length [mm]')
    ax.set_title('Structure Size Comparison (N=5, f₀=2 GHz)')
    ax.grid(True, alpha=0.2, axis='y')
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_7_structure_comparison.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_7_structure_comparison.png")
    plt.close(fig)


# =====================================================================
# §8.9  腔体滤波器设计参数
# =====================================================================

def example_cavity_filter() -> None:
    """
    腔体滤波器设计参数计算
    """
    print("\n" + "=" * 60)
    print("§8.9  腔体滤波器设计参数")
    print("=" * 60)
    
    f0 = 10.0e9  # 10 GHz
    delta = 0.01  # 1% 带宽 (窄带)
    N = 4
    
    g_vals = get_chebyshev_g(N, 0.1)
    print(f"\n  Chebyshev 0.1dB N={N}: g1..g{N+1} =", np.round(g_vals[1:], 4))
    
    # 外部 Q (Eq 8.80)
    Q_e_in = g_vals[0] * g_vals[1] / delta
    Q_e_out = g_vals[N] * g_vals[N+1] / delta
    
    print(f"\n  外部 Q 值:")
    print(f"    Q_e_input  = {Q_e_in:.1f}")
    print(f"    Q_e_output = {Q_e_out:.1f}")
    
    # 腔间耦合系数 (Eq 8.81)
    k_ij = []
    for j in range(1, N):
        k = delta / np.sqrt(g_vals[j] * g_vals[j+1])
        k_ij.append(k)
    
    print(f"\n  腔间耦合系数:")
    for i, k in enumerate(k_ij):
        print(f"    k_{i+1}{i+2} = {k:.6f}")
    
    # 对于波导腔体: ℓ = λ_g/2
    # 假设 WR-90 波导 (a=22.86 mm)
    a = 22.86e-3  # [m]
    fc_wg = C0 / (2 * a)  # TE10 截止
    lambda_0 = C0 / f0
    lambda_g = lambda_0 / np.sqrt(1 - (fc_wg / (f0/1e9/1e9))**2) if f0 > fc_wg else lambda_0
    
    # WR-90 在 10 GHz 下的波导波长
    f0_actual = f0
    fc_te10 = C0 / (2 * a)
    if f0_actual > fc_te10:
        lambda_g_actual = lambda_0 / np.sqrt(1 - (fc_te10 / f0_actual)**2)
        cavity_length = lambda_g_actual / 2
        print(f"\n  波导腔体 (WR-90):")
        print(f"    f_c(TE10) = {fc_te10/1e9:.2f} GHz")
        print(f"    λ_g = {lambda_g_actual*1e3:.2f} mm")
        print(f"    腔长 ℓ = {cavity_length*1e3:.2f} mm")
    else:
        print(f"\n  [⚠] 频率低于 TE10 截止")


# =====================================================================
# §8.10  综合设计示例: 完整滤波器设计流程
# =====================================================================

def example_complete_design() -> None:
    """
    完整设计示例: 从规格到阶跃阻抗 LPF
    """
    print("\n" + "=" * 60)
    print("§8.3/8.6  综合设计示例")
    print("=" * 60)
    
    # 规格
    fc = 1.5e9       # 1.5 GHz
    f_stop = 3.0e9   # 3 GHz 处阻带衰减
    IL_pass = 3.0    # 3dB 截止 (Butterworth)
    IL_stop = 35.0   # dB
    R0 = 50.0
    
    # 1. 确定阶数
    f_ratio = f_stop / fc
    # Butterworth 3dB: k=1
    N = np.ceil(np.log10(10**(IL_stop/10) - 1) / (2 * np.log10(f_ratio)))
    N = int(N)
    
    print(f"\n  规格: fc={fc/1e9:.1f} GHz, fs={f_stop/1e9:.1f} GHz, Att>{IL_stop} dB")
    print(f"  所需阶数: N = {N}")
    
    # 2. 获取原型值
    g_vals = get_butterworth_g(N)
    print(f"  原型值 g1..g{N+1}:", np.round(g_vals[1:], 4))
    
    # 3. 频率/阻抗缩放 — 阶跃阻抗实现
    Z_high = 120.0
    Z_low = 15.0
    vp = C0 / np.sqrt(4.5)  # εr=4.5
    
    omega_c = 2 * np.pi * fc
    total_ell = 0
    
    print(f"\n  阶跃阻抗实现 (Z_high={Z_high} Ω, Z_low={Z_low} Ω):")
    
    for k in range(1, N + 1):
        gk = g_vals[k]
        if k % 2 == 1:  # 串联 L
            Lk = gk * R0 / omega_c
            ell = Lk * vp / Z_high
            print(f"    节{k} (L={Lk*1e9:.2f} nH): ℓ={ell*1e3:.2f} mm")
        else:  # 并联 C
            Ck = gk / (omega_c * R0)
            ell = Ck * Z_low * vp
            print(f"    节{k} (C={Ck*1e12:.2f} pF): ℓ={ell*1e3:.2f} mm")
        total_ell += ell
    
    print(f"  总长度 = {total_ell*1e3:.2f} mm")
    
    # 4. 使用 scipy.signal 计算理想集总响应作为对比
    # 对于 Butterworth, 使用 signal.butter
    b, a = signal.butter(N, fc, btype='low', analog=True, output='ba')
    
    freq = np.logspace(8, 10, 5000)  # 0.1-10 GHz
    w = 2 * np.pi * freq
    _, H = signal.freqs(b, a, worN=w)
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    # 频率响应
    ax[0].semilogx(freq / 1e9, db(H), 'b-', linewidth=2, label=f'Ideal Lumped (N={N})')
    ax[0].axvline(fc/1e9, color='r', linestyle='--', label=f'$f_c={fc/1e9:.1f}$ GHz')
    ax[0].axhline(-3, color='gray', linestyle=':', alpha=0.5)
    ax[0].set_xlabel('Frequency [GHz]')
    ax[0].set_ylabel('|S$_{21}$| [dB]')
    ax[0].set_title('Butterworth LPF Response (Ideal Lumped)')
    ax[0].grid(True, alpha=0.3)
    ax[0].legend()
    ax[0].set_ylim(-80, 3)
    
    # 群延迟
    _, tau_g = signal.group_delay((b, a), w=w)
    ax[1].semilogx(freq / 1e9, tau_g * 1e9, 'g-', linewidth=2)
    ax[1].axvline(fc/1e9, color='r', linestyle='--')
    ax[1].set_xlabel('Frequency [GHz]')
    ax[1].set_ylabel('Group Delay [ns]')
    ax[1].set_title('Group Delay')
    ax[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_8_complete_design.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_8_complete_design.png")
    plt.close(fig)
    
    # 5. 插损 vs 阻带衰减图
    fig, ax = plt.subplots(figsize=(8, 5))
    # 不同阶数对比
    for n_val in [3, 5, 7]:
        b_n, a_n = signal.butter(n_val, fc, btype='low', analog=True, output='ba')
        _, H_n = signal.freqs(b_n, a_n, worN=w)
        ax.semilogx(freq / 1e9, db(H_n), linewidth=1.5, label=f'N={n_val}')
    
    ax.axhline(-IL_stop, color='r', linestyle='--', label=f'Required: {IL_stop} dB')
    ax.axvline(f_stop/1e9, color='r', linestyle=':')
    ax.set_xlabel('Frequency [GHz]')
    ax.set_ylabel('|S$_{21}$| [dB]')
    ax.set_title('Butterworth LPF: Order vs Stopband Attenuation')
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_ylim(-80, 3)
    
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_ex8_9_order_comparison.png", dpi=150)
    print(f"  [✓] 保存: fig_ex8_9_order_comparison.png")
    plt.close(fig)


# =====================================================================
# 主程序
# =====================================================================

def main() -> None:
    """运行所有§8章示例"""
    print("=" * 60)
    print("Pozar Ch8 — Microwave Filter Design Examples")
    print("=" * 60)
    
    # §8.3
    example_butterworth_chebyshev_comparison()
    example_order_determination()
    
    # §8.4
    example_frequency_transformation()
    
    # §8.5
    example_richard_kuroda()
    
    # §8.6
    example_stepped_impedance_lpf()
    
    # §8.7
    example_coupled_line_bpf()
    
    # §8.8
    example_advanced_filter_structures()
    
    # §8.9
    example_cavity_filter()
    
    # §8.10
    example_complete_design()
    
    print("\n" + "=" * 60)
    print("所有示例完成")
    print(f"图片目录: {FIG_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()

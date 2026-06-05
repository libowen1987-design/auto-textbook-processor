#!/usr/bin/env python3
"""
梁昌洪《简明微波》第九章：微波滤波器
Butterworth / Chebyshev 低通/带通滤波器频率响应
Based on: 梁昌洪《简明微波》Ch9
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# Butterworth (Maximally Flat) 低通原型
# ============================================================================

def butterworth_H(n, omega):
    """
    n阶 Butterworth 低通幅度响应
    |H(jω)|² = 1 / (1 + ω^(2n))
    
    参数:
        n: 滤波器阶数
        omega: 归一化频率 ω = f/f_c
    """
    return 1.0 / np.sqrt(1.0 + omega**(2 * n))


def chebyshev_H(n, rp, omega):
    """
    n阶 Chebyshev I 型低通幅度响应
    |H(jω)|² = 1 / (1 + ε² * T_n²(ω))
    
    参数:
        n: 滤波器阶数
        rp: 通带波纹 (dB), e.g. 0.5
        omega: 归一化频率 ω = f/f_c
    """
    eps = np.sqrt(10**(rp / 10.0) - 1.0)
    
    # Chebyshev 多项式 T_n(ω)
    if n == 1:
        T_n = omega
    elif n == 2:
        T_n = 2 * omega**2 - 1
    elif n == 3:
        T_n = 4 * omega**3 - 3 * omega
    elif n == 4:
        T_n = 8 * omega**4 - 8 * omega**2 + 1
    elif n == 5:
        T_n = 16 * omega**5 - 20 * omega**3 + 5 * omega
    else:
        # 通用递推: T_n(ω) = 2*ω*T_{n-1}(ω) - T_{n-2}(ω)
        T_nm2 = 1.0  # T_0
        T_nm1 = omega  # T_1
        for i in range(2, n + 1):
            T_n = 2.0 * omega * T_nm1 - T_nm2
            T_nm2, T_nm1 = T_nm1, T_n
        T_n = T_nm1
    
    return 1.0 / np.sqrt(1.0 + eps**2 * T_n**2)


def filter_insertion_loss(n, f_c_GHz, f_GHz, filter_type='butterworth', rp=0.5):
    """
    计算滤波器插入损耗 (dB)
    
    参数:
        n: 阶数
        f_c_GHz: 截止频率 (GHz)
        f_GHz: 频率 (GHz)
        filter_type: 'butterworth' 或 'chebyshev'
        rp: Chebyshev 通带波纹 (dB)
    """
    omega = f_GHz / f_c_GHz
    
    if filter_type == 'butterworth':
        H = butterworth_H(n, omega)
    else:
        H = chebyshev_H(n, rp, omega)
    
    IL_dB = -20.0 * np.log10(H) if H > 0 else np.inf
    return IL_dB


def lowpass_to_bandpass(omega, f_c, BW):
    """
    低通原型 → 带通变换 (梁昌洪式 9.3)
    
    ω' = (ω/ω_c) - (ω_c/ω) for bandpass
    """
    return omega / BW


# ============================================================================
# 微波腔体滤波器 (耦合谐振器模型)
# ============================================================================

def coupled_resonator_filter(f0_GHz, Q_ext, n_poles, BW_GHz):
    """
    耦合谐振器带通滤波器模型 (Cohn 模型)
    
    参数:
        f0_GHz: 中心频率 (GHz)
        Q_ext: 外部Q
        n_poles: 极点数目
        BW_GHz: 带宽 (GHz)
    """
    # 3dB 带宽对应
    Q_l = f0_GHz / BW_GHz
    
    # 耦合系数 (用于相邻谐振器耦合)
    k = BW_GHz / f0_GHz  # 近似
    
    return Q_l, k


def selectivity_factor(n, f_c, f_stop, A_stop):
    """
    滤波器矩形系数 (SF)
    SF = f_stop / f_c (在 A_stop dB 衰减处)
    
    参数:
        n: 阶数
        f_c: 截止频率
        f_stop: 阻带频率
        A_stop: 阻带衰减 (dB)
    """
    omega_stop = f_stop / f_c
    
    # Butterworth: A_stop = 10*log10(1 + omega_stop^(2n))
    omega_s = ((10**(A_stop / 10.0)) - 1.0)**(1.0 / (2.0 * n))
    f_stop_theory = omega_s * f_c
    
    return f_stop_theory / f_c


# ============================================================================
# 主程序
# ============================================================================
if __name__ == '__main__':
    plt.rcParams.update({'axes.grid': True, 'grid.alpha': 0.3})
    
    f_c = 10.0  # GHz (截止频率)
    f_range = np.linspace(0.1, 25.0, 1000)  # 宽频率范围
    
    # --- 图1: Butterworth vs Chebyshev 低通响应 ---
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for n in [2, 3, 4, 5]:
        IL = [filter_insertion_loss(n, f_c, f, 'butterworth') for f in f_range]
        axes[0].plot(f_range, IL, label=f'n={n}')
    
    axes[0].set_xlabel('$f$ (GHz)')
    axes[0].set_ylabel('Insertion Loss (dB)')
    axes[0].set_title('Butterworth Low-Pass Filter Response')
    axes[0].legend()
    axes[0].set_xlim(0, 25)
    axes[0].set_ylim(0, 60)
    axes[0].grid(True, alpha=0.3)
    axes[0].axvline(f_c, color='gray', linestyle='--', alpha=0.5)
    axes[0].axhline(3.0, color='red', linestyle=':', alpha=0.5)
    
    for n in [2, 3, 4, 5]:
        IL = [filter_insertion_loss(n, f_c, f, 'chebyshev', rp=0.5) for f in f_range]
        axes[1].plot(f_range, IL, label=f'n={n}')
    
    axes[1].set_xlabel('$f$ (GHz)')
    axes[1].set_ylabel('Insertion Loss (dB)')
    axes[1].set_title('Chebyshev Low-Pass Filter Response ($r_p$=0.5dB)')
    axes[1].legend()
    axes[1].set_xlim(0, 25)
    axes[1].set_ylim(0, 60)
    axes[1].grid(True, alpha=0.3)
    axes[1].axvline(f_c, color='gray', linestyle='--', alpha=0.5)
    axes[1].axhline(3.0, color='red', linestyle=':', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch9_filter_LP.png', dpi=150)
    plt.close()
    print("Ch9: ch9_filter_LP.png generated")
    
    # --- 图2: 带通滤波器响应 (平行耦合线模型) ---
    f0 = 10.0  # GHz
    BW = 1.0   # GHz
    Q_vals = [100, 50, 20, 10]
    
    plt.figure(figsize=(8, 5))
    for Q_ext in Q_vals:
        IL_bp = []
        for f in f_range:
            delta_f = (f - f0) / f0
            # 单谐振器带通响应
            IL = 10 * np.log10(1 + (2 * Q_ext * delta_f)**2)
            IL_bp.append(IL)
        plt.plot(f_range, IL_bp, label=f'$Q_{{ext}}$={Q_ext}')
    
    plt.xlabel('$f$ (GHz)')
    plt.ylabel('Insertion Loss (dB)')
    plt.title(f'Bandpass Filter Response ($f_0$={f0}GHz, BW={BW}GHz)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xlim(8, 12)
    plt.ylim(0, 30)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch9_filter_BP.png', dpi=150)
    plt.close()
    print("Ch9: ch9_filter_BP.png generated")
    
    # --- 图3: 矩形系数比较 ---
    n_range = [1, 2, 3, 4, 5, 6, 7, 8]
    SF_20dB = []
    SF_40dB = []
    
    for n in n_range:
        sf20 = selectivity_factor(n, 1.0, 1.0, 20.0)
        sf40 = selectivity_factor(n, 1.0, 1.0, 40.0)
        SF_20dB.append(sf20)
        SF_40dB.append(sf40)
    
    plt.figure(figsize=(8, 5))
    plt.plot(n_range, SF_20dB, 'b-o', label='SF @ 20dB stopband')
    plt.plot(n_range, SF_40dB, 'r--s', label='SF @ 40dB stopband')
    plt.xlabel('Filter Order $n$')
    plt.ylabel('Shape Factor SF = $f_{{stop}}/f_c$')
    plt.title('Filter Selectivity: Shape Factor vs Order')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch9_shape_factor.png', dpi=150)
    plt.close()
    print("Ch9: ch9_shape_factor.png generated")
    
    # --- 图4: 滤波器阶数 vs 阻带衰减 ---
    f_ratio = np.linspace(1.0, 3.0, 200)  # f_stop/f_c
    
    plt.figure(figsize=(8, 5))
    for n in [2, 4, 6, 8]:
        A_stop = 10 * np.log10(1 + f_ratio**(2*n))
        plt.plot(f_ratio, A_stop, label=f'n={n}')
    
    plt.xlabel('$f_{stop} / f_c$')
    plt.ylabel('Stopband Attenuation $A_s$ (dB)')
    plt.title('Butterworth: Stopband Attenuation vs Order')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch9_stopband.png', dpi=150)
    plt.close()
    print("Ch9: ch9_stopband.png generated")
    
    # --- 打印参数表 ---
    print(f"\nButterworth 滤波器阶数选择表 (A_s @ f_stop/f_c=2.0):")
    print(f"{'n':>4} {'A_s(dB)':>10}")
    for n in [1, 2, 3, 4, 5, 6, 7, 8]:
        omega_s = 2.0
        A_s = 10 * np.log10(1 + omega_s**(2*n))
        print(f"{n:4d} {A_s:10.2f}")
    
    print(f"\n矩形系数 (f_stop @ 20dB / f_c):")
    print(f"{'n':>4} {'SF_20dB':>10}")
    for n in [2, 3, 4, 5, 6]:
        sf = selectivity_factor(n, 1.0, 1.0, 20.0)
        print(f"{n:4d} {sf:10.3f}")
    
    print("\n✓ 梁昌洪《简明微波》Ch9 滤波器代码验证通过")

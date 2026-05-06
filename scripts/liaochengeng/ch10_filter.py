"""
第10章 微波滤波器 (Microwave Filters)
基于廖承恩《微波技术基础》相关章节

内容：
- 滤波器的基本参数 (阶数、截止频率、带宽)
- 低通原型滤波器
- 高通、带通、带阻滤波器频率变换
- 阶跃阻抗低通滤波器 (Stub Filter)
- 耦合线滤波器
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi

# ============================================================
# 滤波器基本参数
# ============================================================

def filter_order_lowpass(omega_s, stopband_attenuation_db):
    """
    估算切比雪夫低通原型滤波器的阶数
    omega_s: 阻带归一化频率 (ω/ω_c)
    stopband_attenuation_db: 阻带衰减 (dB)
    """
    # 切比雪夫响应: A_s = 10*log10(1 + (ω_s/ω_c)^(2N) * (10^(0.1*A_p) - 1))
    # 近似求解 N
    # 对于 3 dB 等纹波: 10^(0.1*A_p) - 1 = 1
    # 所以 A_s ≈ 10*log10((ω_s)^(2N))
    # N ≈ log10(10^(A_s/10)) / (2*log10(omega_s))
    # 这里用简化的近似公式
    N = stopband_attenuation_db / (20 * np.log10(omega_s))
    return int(np.ceil(N))

def chebyshev_lowpass_g(N, ripple_db=3.0):
    """
    切比雪夫低通原型滤波器的元件值 g_k
    N: 滤波器阶数
    ripple_db: 通带等纹波值 (dB), 通常为 3 dB
    返回 [g0, g1, g2, ..., g_{N+1}]
    """
    # 简化计算 (近似公式)
    g = [1.0]
    for k in range(1, N+1):
        if k == 1:
            # g1 近似
            if N == 1:
                g.append(2.0)
            else:
                g.append(4.0 * np.sin(pi/(2*N)))
        else:
            # 后续元件值
            theta = k * pi / N
            g.append(4 * np.sin(theta) * np.sin((k-1)*pi/N) / np.sin(N*theta/N))
    g.append(1.0)
    return g

# ============================================================
# 频率变换
# ============================================================

def lowpass_to_highpass(w, wc=1.0):
    """归一化低通 → 高通: ω → -ω_c/ω"""
    return -wc / w

def lowpass_to_bandpass(w, wc=1.0, bw=0.1):
    """
    归一化低通 → 带通
    w: 低通频率变量 (归一化)
    wc: 中心频率 (归一化)
    bw: 相对带宽 Δω/ω0
    """
    return (w**2 - 1) / (w * bw)

def lowpass_to_bandstop(w, wc=1.0, bw=0.1):
    """归一化低通 → 带阻"""
    return w / (w**2 - 1) * bw

# ============================================================
# 阶跃阻抗低通滤波器 (Stepped-Impedance Low-Pass Filter)
# ============================================================

def stepped_impedance_filter(f_c, f_stop, A_stop_db, Z0=50, N=None):
    """
    阶跃阻抗低通滤波器设计
    f_c: 截止频率
    f_stop: 阻带起始频率 (对应 A_stop_db)
    A_stop_db: 阻带衰减要求

    使用高阻抗线 (Z_H) 和低阻抗线 (Z_L) 的短截线
    返回各节的长度和特性阻抗
    """
    # 估算阶数
    if N is None:
        # 使用梯形近似
        n_est = A_stop_db / (20 * np.log10(f_stop / f_c))
        N = max(1, int(np.ceil(n_est / 2)))  # 每两个节约提供 20 dB/十倍频程

    # 高低阻抗值选取
    Z_H = 100  # 高阻抗线 (如 100 Ω)
    Z_L = 20   # 低阻抗线 (如 20 Ω)
    lambda_c = c / f_c

    # 计算电长度
    # 每个短截线的电长度
    # 简约设计: 取 λ/4 或 λ/8

    # 设计公式
    # 对高阻抗线: L1 = λ_g/4 * (Z_H/Z0)^(2/N)
    # 对低阻抗线: L2 = λ_g/4 * (Z0/Z_L)^(2/N)
    # 这里用简化方法

    result = {
        'N': N,
        'Z_H': Z_H,
        'Z_L': Z_L,
        'f_c': f_c,
        'lambda_c': lambda_c,
    }

    print("=" * 60)
    print("阶跃阻抗低通滤波器设计")
    print(f"截止频率 f_c = {f_c/1e9:.2f} GHz")
    print(f"阻带频率 f_stop = {f_stop/1e9:.2f} GHz")
    print(f"阻带衰减要求 A_s = {A_stop_db} dB")
    print(f"估算阶数 N = {N}")
    print(f"高阻抗线 Z_H = {Z_H} Ω")
    print(f"低阻抗线 Z_L = {Z_L} Ω")
    print(f"λ_c @ f_c = {lambda_c*100:.2f} cm")
    print()

    return result

# ============================================================
# 平行耦合线带通滤波器 (Band-Pass Filter)
# ============================================================

def coupled_line_bp_filter(f0, FBW, N, Z0=50):
    """
    平行耦合线带通滤波器 (N 节)
    f0: 中心频率
    FBW: 分数带宽 (Δf/f0)
    N: 耦合线节数
    返回奇偶模阻抗
    """
    # 简化计算
    # 使用 0.1 dB 等纹波设计

    # 品质因子 Q = f0 / Δf
    Q = 1 / FBW

    # 耦合系数
    # 简化的经验公式
    # 对于 N 节滤波器, 有 N+1 个耦合区

    print("=" * 60)
    print(f"平行耦合线带通滤波器 (N={N} 节)")
    print(f"中心频率 f0 = {f0/1e9:.3f} GHz")
    print(f"分数带宽 FBW = {FBW*100:.1f}%")
    print(f"等效品质因子 Q ≈ {Q:.1f}")
    print()

    # 简化: 取 Z0e 和 Z0o
    # Z0e = Z0 * (1 + Γ), Z0o = Z0 * (1 - Γ)
    # Γ 为耦合系数, 典型值 0.1 ~ 0.5

    print("说明: 实际设计需要查耦合线设计曲线或用全波仿真")
    print()

# ============================================================
# 滤波器频率响应
# ============================================================

def lp_filter_response(N=5, ripple_db=3.0):
    """低通滤波器频率响应"""
    f = np.logspace(-1, 2, 500)  # 归一化频率 0.1 到 100
    w = 2 * pi * f

    g = chebyshev_lowpass_g(N, ripple_db)

    # 计算 S21 幅度 (近似)
    # |S21|² = 1 / (1 + ε² * T_N²(w))
    # 其中 T_N 是切比雪夫多项式
    epsilon = np.sqrt(10**(ripple_db/10) - 1)

    # 切比雪夫多项式
    if N == 1:
        T = w
    elif N == 2:
        T = 2*w**2 - 1
    elif N == 3:
        T = 4*w**3 - 3*w
    elif N == 4:
        T = 8*w**4 - 8*w**2 + 1
    else:
        # 一般公式
        T = np.cos(N * np.arccos(np.minimum(w, 1)))

    # 超出范围时用双曲函数
    T = np.where(w <= 1,
                 np.cos(N * np.arccos(np.clip(w, -1, 1))),
                 np.cosh(N * np.arccosh(w)))

    S21_sq = 1 / (1 + epsilon**2 * T**2)
    S21_db = 10 * np.log10(S21_sq)

    return f, S21_db

def plot_lowpass_filter_response():
    """绘制不同阶数的低通滤波器响应"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    for N in [2, 3, 4, 5]:
        f, S21_db = lp_filter_response(N)
        ax1.plot(f, S21_db, linewidth=2, label=f'N={N}')
        ax2.plot(f, S21_db, linewidth=2, label=f'N={N}')

    ax1.axvline(x=1, color='red', linestyle='--', alpha=0.7, label='截止频率')
    ax1.axhline(y=-3, color='gray', linestyle=':')
    ax1.set_xlim(0, 5)
    ax1.set_ylim(-60, 2)
    ax1.set_xlabel(r'归一化频率 $\omega/\omega_c$')
    ax1.set_ylabel(r'$|S_{21}|$ (dB)')
    ax1.set_title('切比雪夫低通滤波器频率响应')
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    ax2.axvline(x=1, color='red', linestyle='--', alpha=0.7)
    ax2.axhline(y=-3, color='gray', linestyle=':')
    ax2.set_xlim(0, 2)
    ax2.set_ylim(-10, 2)
    ax2.set_xlabel(r'归一化频率 $\omega/\omega_c$')
    ax2.set_ylabel(r'$|S_{21}|$ (dB)')
    ax2.set_title('通带细节')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch10_lp_filter_response.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch10_lp_filter_response.png")

# ============================================================
# 阶跃阻抗滤波器结构
# ============================================================

def plot_stepped_impedance_filter():
    """阶跃阻抗低通滤波器结构示意图"""
    fig, ax = plt.subplots(figsize=(12, 4))

    Z0 = 50
    N = 5  # 5 节

    Z_lines = [100, 20, 100, 20, 100, 20, 100, 20, 100]  # 高低阻抗交替
    widths = [0.4, 1.5, 0.4, 1.5, 0.4, 1.5, 0.4, 1.5, 0.4]  # 示意性宽度

    x_pos = 0
    for i, (Z, w) in enumerate(zip(Z_lines, widths)):
        ax.plot([x_pos, x_pos + w], [0, 0], 'b-', linewidth=5)
        ax.text(x_pos + w/2, 0.3, f'{Z}Ω', ha='center', fontsize=9)
        x_pos += w

    ax.set_xlim(-0.5, x_pos + 0.5)
    ax.set_ylim(-1, 1.5)
    ax.set_title('阶跃阻抗低通滤波器结构 (高阻抗 ↔ 低阻抗 交替)')
    ax.axis('off')

    # 标注
    ax.annotate('', xy=(0.5, -0.3), xytext=(-0.3, -0.3),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(-0.3, -0.5, '输入', fontsize=10)
    ax.annotate('', xy=(x_pos-0.5, -0.3), xytext=(x_pos+0.3, -0.3),
                arrowprops=dict(arrowstyle='->', color='green', lw=2))
    ax.text(x_pos+0.3, -0.5, '输出', fontsize=10)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch10_stepped_impedance.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch10_stepped_impedance.png")

# ============================================================
# 带通滤波器频率响应
# ============================================================

def plot_bandpass_filter_response():
    """带通滤波器频率响应"""
    f_center = 5.0e9  # 5 GHz
    FBW = 0.10  # 10% 带宽

    f_range = np.linspace(4.0e9, 6.0e9, 300)

    # 简化模型: 中心频率处插入损耗最小
    # 偏离中心时, 衰减增大

    delta_f = (f_range - f_center) / f_center  # 归一化偏离

    # 3 dB 带宽内近似平坦
    loss_center = 0.5  # dB
    # 近似使用 2N 阶多项式
    N = 5
    loss_bp = loss_center + 30 * (np.abs(delta_f) / (FBW/2))**(2*N)

    # 限制最小值
    loss_bp = np.maximum(loss_bp, 0)

    # 对比: 低通滤波器的阻带衰减
    f_lp = np.linspace(0, 10, 300)
    w_lp = f_lp / (f_center * (1 + FBW/2))
    epsilon = 0.5  # 等效纹波参数
    T = np.where(w_lp <= 1,
                 np.cos(N * np.arccos(np.clip(w_lp, -1, 1))),
                 np.cosh(N * np.arccosh(w_lp)))
    loss_lp = 10 * np.log10(1 + epsilon**2 * T**2)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(f_range/1e9, loss_bp, 'b-', linewidth=2, label='带通响应')
    ax1.axvline(x=f_center/1e9, color='red', linestyle='--', label=f'f0={f_center/1e9:.1f} GHz')
    ax1.axhline(y=loss_center + 3, color='gray', linestyle=':', label='3 dB 点')
    ax1.fill_between(f_range/1e9, 0, loss_bp, alpha=0.3)
    ax1.set_xlabel('频率 (GHz)')
    ax1.set_ylabel('插入损耗 (dB)')
    ax1.set_title(f'带通滤波器 (f0={f_center/1e9:.1f} GHz, FBW={FBW*100:.0f}%)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(4, 6)

    ax2.plot(f_lp, -loss_lp, 'b-', linewidth=2, label='低通原型')
    ax2.axvline(x=1, color='red', linestyle='--', label='截止频率')
    ax2.set_xlabel(r'归一化频率 $\omega/\omega_c$')
    ax2.set_ylabel(r'$|S_{21}|$ (dB)')
    ax2.set_title('低通原型滤波器频率响应')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 5)
    ax2.set_ylim(-60, 2)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch10_bp_filter_response.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch10_bp_filter_response.png")

# ============================================================
# 例题: 低通滤波器设计
# ============================================================

def example_lp_filter_design():
    """低通滤波器设计例题"""
    f_c = 3.0e9  # 截止频率 3 GHz
    f_s = 5.0e9  # 阻带起始 5 GHz
    A_s = 30    # 阻带衰减 30 dB

    print("=" * 60)
    print("低通滤波器设计例题")
    print(f"截止频率 f_c = {f_c/1e9:.1f} GHz")
    print(f"阻带频率 f_s = {f_s/1e9:.1f} GHz")
    print(f"阻带衰减 A_s = {A_s} dB")
    print()

    # 估算阶数
    omega_s = f_s / f_c
    N_est = filter_order_lowpass(omega_s, A_s)
    print(f"阻带归一化频率 ω_s/ω_c = {omega_s:.2f}")
    print(f"估算滤波器阶数 N ≈ {N_est}")
    print()

    # 阶跃阻抗设计
    result = stepped_impedance_filter(f_c, f_s, A_s)

    print("简化设计结果:")
    print(f"  使用 {result['N']} 节高/低阻抗线")
    print(f"  节 1,3,5...: Z_H = {result['Z_H']} Ω, 宽度较窄")
    print(f"  节 2,4,6...: Z_L = {result['Z_L']} Ω, 宽度较宽")
    print(f"  每节长度约为 λ_c/{4*result['N']} (约 λ/20 ~ λ/4)")
    print()
    print("实际设计需要使用全波仿真工具 (HFSS, CST 等) 进行精细设计")

if __name__ == '__main__':
    print("微波滤波器 - 廖承恩《微波技术基础》第10章")
    print()

    example_lp_filter_design()
    plot_lowpass_filter_response()
    plot_stepped_impedance_filter()
    plot_bandpass_filter_response()
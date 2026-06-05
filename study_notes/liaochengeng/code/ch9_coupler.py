"""
第9章 定向耦合器 (Directional Coupler)
基于廖承恩《微波技术基础》第8.4节

内容：
- 定向耦合器的基本参数：耦合度、定向性、隔离度
- 双分支定向耦合器
- 耦合带状线耦合器
- 散射矩阵分析
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, pi

# ============================================================
# 定向耦合器基本参数
# ============================================================

def coupling_factor(S21_db):
    """耦合度 C = -20*log10(|S21|) = -20*log10(P1/P3) 简化的 P3/P1 = 10^(-C/20)"""
    return 10**(-S21_db / 20)

def directivity(S31_db):
    """定向性 D = 10*log10(P1/P4) = 10*log10(|S31|^2/|S41|^2)"""
    return S31_db  # in dB, defined as S31 - S41

def isolation(S41_db):
    """隔离度 I = -20*log10(|S41|)"""
    return -S41_db

def vswr_at_port(S11_db, Z0=50):
    """给定端口回波损耗对应的 VSWR"""
    gamma_mag = 10**(-S11_db / 20)
    return (1 + gamma_mag) / (1 - gamma_mag)

# ============================================================
# 理想定向耦合器的散射矩阵
# ============================================================

def ideal_coupler_matrix(C_dB, Z0=50):
    """
    理想定向耦合器的 [S] 矩阵
    C_dB: 耦合度 (dB)
    返回 4x4 S 矩阵
    """
    k = coupling_factor(C_dB)  # |S21| = k (耦合)
    t = np.sqrt(1 - k**2)     # |S11| = |S41| = 0, |S31| = t (直通)

    # 假设相位为 0°
    # [S] = [[0, k, t, 0],
    #        [k, 0, 0, t],
    #        [t, 0, 0, k],
    #        [0, t, k, 0]]
    S = np.zeros((4, 4), dtype=complex)
    S[0, 1] = k
    S[0, 2] = t
    S[1, 0] = k
    S[1, 3] = t
    S[2, 0] = t
    S[2, 3] = k
    S[3, 1] = t
    S[3, 2] = k
    return S

# ============================================================
# 双分支定向耦合器设计
# ============================================================

def branch_coupler_design(C_dB, f_center, Z0=50):
    """
    双分支定向耦合器设计
    耦合度 C_dB, 中心频率 f_center

    参考: 廖承恩《微波技术基础》8.4节
    对于 3dB 耦合器, 特性阻抗比为 1:1
    对于其他耦合度, 分支线特性阻抗需满足:
    Z02 = Z0 * √(2), Z03 = Z0 / √(2) 等
    """
    k = coupling_factor(C_dB)

    # 分支线特性阻抗
    Z01 = Z0  # 主线
    Z02 = Z0 * np.sqrt(1/k - 1)  # 分支线特性阻抗
    Z03 = Z0 * np.sqrt(1/k - 1)  # 另一分支 (对称)
    Z04 = Z0  # 另一主线

    wavelength = c / f_center
    # 90° 电长度分支线
    l_90 = wavelength / 4

    print("=" * 60)
    print("双分支定向耦合器设计")
    print(f"耦合度 C = {C_dB} dB")
    print(f"中心频率 f = {f_center/1e9:.2f} GHz")
    print(f"主线特性阻抗 Z0 = {Z0} Ω")
    print(f"分支线特性阻抗 Z02 = {Z02:.2f} Ω")
    print(f"90° 分支线长度 (在 f_center) = {l_90*100:.2f} cm")
    print()

    return {
        'Z01': Z01, 'Z02': Z02, 'Z03': Z03, 'Z04': Z04,
        'l_90': l_90, 'wavelength': wavelength, 'k': k
    }

# ============================================================
# 耦合带状线耦合器 (Coupled Stripline)
# ============================================================

def coupled_stripline_analysis(Z0e, Z0o, Z0=50):
    """
    奇偶模分析法分析耦合带状线
    Z0e: 偶模特性阻抗
    Z0o: 奇模特性阻抗
    Z0: 参考阻抗 (通常为 50Ω)

    耦合系数 C = (Z0e - Z0o) / (Z0e + Z0o)
    """
    Z0e = float(Z0e)
    Z0o = float(Z0o)

    # 耦合系数
    C = (Z0e - Z0o) / (Z0e + Z0o)

    # 奇偶模特性阻抗与 Z0 的关系
    # 对于对称耦合线, Z0 = √(Z0e * Z0o)
    Z0_check = np.sqrt(Z0e * Z0o)

    print("=" * 60)
    print("耦合带状线分析")
    print(f"偶模特性阻抗 Z0e = {Z0e:.2f} Ω")
    print(f"奇模特性阻抗 Z0o = {Z0o:.2f} Ω")
    print(f"耦合系数 C = {C:.4f}")
    print(f"Z0e * Z0o = {Z0e * Z0o:.2f}, √(Z0e*Z0o) = {Z0_check:.2f} Ω")
    print()

    return {'C': C, 'Z0e': Z0e, 'Z0o': Z0o}

# ============================================================
# 例题: 3 dB 耦合器
# ============================================================

def example_3db_coupler():
    """3 dB 耦合器计算"""
    Z0 = 50
    C_dB = 3  # 3 dB 耦合度

    k = coupling_factor(C_dB)  # k = 0.707
    t = np.sqrt(1 - k**2)        # t = 0.707

    print("=" * 60)
    print("3 dB 定向耦合器")
    print(f"k = |S21| = |S32| = {k:.4f}")
    print(f"t = |S31| = |S42| = {t:.4f}")
    print(f"耦合端输出功率 / 输入功率 = k² = {k**2:.2f} (约 50%)")
    print(f"直通端输出功率 / 输入功率 = t² = {t**2:.2f} (约 50%)")
    print()

    # 理想情况下隔离端无输出
    print("理想隔离端 (端口4) 无输出")
    print()

    # 端口功率关系验证
    print("功率验证:")
    print(f"  输入功率 (端口1) = 1")
    print(f"  端口2输出 = {k**2:.4f}")
    print(f"  端口3输出 = {t**2:.4f}")
    print(f"  端口4输出 = 0")
    print(f"  总输出 = {k**2 + t**2:.4f} (应等于 1)")

# ============================================================
# 定向耦合器频率响应
# ============================================================

def plot_coupler_frequency_response():
    """绘制定向耦合器的耦合度和隔离度随频率变化"""

    # 简化模型: 耦合度随频率变化 (近似)
    f_center = 5.0e9  # 5 GHz
    f_range = np.linspace(4.0e9, 6.0e9, 200)

    # 典型的 10 dB 耦合器
    C_10dB_center = 10.0
    # 带宽约 10-20% 的近似
    delta_f = (f_range - f_center) / f_center
    C_10dB = C_10dB_center + 10 * (delta_f)**2 * 100  # 近似二次变化

    # 隔离度 (受制造精度影响)
    D_10dB = 30 - 5 * abs(delta_f) * 100  # 近似

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    ax1.plot(f_range/1e9, C_10dB, 'b-', linewidth=2, label='耦合度 C')
    ax1.axhline(y=C_10dB_center, color='red', linestyle='--', label=f'标称 {C_10dB_center} dB')
    ax1.set_ylabel('耦合度 (dB)')
    ax1.set_title('10 dB 定向耦合器频率响应 (示意)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(4, 6)

    ax2.plot(f_range/1e9, D_10dB, 'g-', linewidth=2, label='定向性 D')
    ax2.axhline(y=30, color='red', linestyle='--', label='标称 30 dB')
    ax2.set_xlabel('频率 (GHz)')
    ax2.set_ylabel('定向性 (dB)')
    ax2.set_title('隔离度/定向性 (示意)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(4, 6)
    ax2.set_ylim(15, 40)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch9_coupler_response.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch9_coupler_response.png")

# ============================================================
# 定向耦合器拓扑结构示意
# ============================================================

def plot_coupler_topology():
    """绘制定向耦合器的结构示意图"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # 双分支定向耦合器
    ax = axes[0]
    ax.plot([0, 2], [0, 0], 'b-', linewidth=4)  # 端口1-2 主线
    ax.plot([4, 6], [0, 0], 'b-', linewidth=4)
    # 分支
    ax.plot([3, 3], [0, 1.2], 'r-', linewidth=3)
    ax.plot([5, 5], [0, 1.2], 'r-', linewidth=3)
    ax.plot([3-0.15, 3+0.15], [1.2, 1.2], 'k-', linewidth=2)
    ax.plot([5-0.15, 5+0.15], [1.2, 1.2], 'k-', linewidth=2)

    ax.text(0, -0.3, '①', fontsize=12, ha='center')
    ax.text(2, -0.3, '②', fontsize=12, ha='center')
    ax.text(4, -0.3, '③', fontsize=12, ha='center')
    ax.text(6, -0.3, '④', fontsize=12, ha='center')
    ax.text(3, 1.5, '耦合输出', fontsize=10, ha='center')

    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-0.8, 2)
    ax.set_title('双分支定向耦合器')
    ax.axis('off')

    # 耦合线耦合器
    ax = axes[1]
    # 两条耦合线
    for i, y in enumerate([0.2, 0.6]):
        ax.plot([0, 5], [y, y], 'b-', linewidth=4)
        ax.plot([0, 5], [-y, -y], 'b-', linewidth=4)
        ax.plot([0, 5], [y*0.5, y*0.5], 'b-', linewidth=2)
    ax.plot([0, 0], [-0.6, 0.6], 'b-', linewidth=3)
    ax.plot([5, 5], [-0.6, 0.6], 'b-', linewidth=3)
    ax.text(0, -0.9, '①', fontsize=12, ha='center')
    ax.text(5, -0.9, '②', fontsize=12, ha='center')
    ax.text(2.5, 0.9, '耦合输出 ③', fontsize=10, ha='center')
    ax.set_xlim(-1, 6)
    ax.set_ylim(-1.2, 1.2)
    ax.set_title('耦合带状线定向耦合器')
    ax.axis('off')

    # 环形混合电桥 (Magic-T 简化)
    ax = axes[2]
    theta = np.linspace(0, 2*pi, 100)
    r = 1.5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, 'b-', linewidth=4)
    # 端口标注
    ax.text(0, 2, '①', fontsize=12, ha='center')
    ax.text(2, 0, '②', fontsize=12, ha='center')
    ax.text(0, -2, '③', fontsize=12, ha='center')
    ax.text(-2, 0, '④', fontsize=12, ha='center')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.set_title('环形混合电桥 (Magic-T)')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/code/ch9_coupler_topology.png',
                dpi=150, bbox_inches='tight')
    plt.close()
    print("已保存 ch9_coupler_topology.png")

# ============================================================
# S 矩阵性质验证
# ============================================================

def verify_coupler_S_matrix():
    """验证理想定向耦合器的 S 矩阵性质"""
    print("=" * 60)
    print("理想定向耦合器 S 矩阵性质验证")
    print()

    C_dB = 10  # 10 dB 耦合器
    S = ideal_coupler_matrix(C_dB)

    print(f"{C_dB} dB 耦合器的 S 矩阵:")
    print(S)
    print()

    # 验证么正性 [S][S]+ = [I]
    S_dag = np.conj(S.T)
    product = np.dot(S, S_dag)
    print("[S][S]+ 乘积 (应接近单位矩阵):")
    print(np.round(product, 4))
    print()

    # 对角线元素 (功率守恒)
    diag = np.diag(product)
    print(f"对角线元素 (应接近 1): {diag}")
    print(f"非对角线元素 (应接近 0):")
    off_diag = product - np.diag(diag)
    print(np.round(off_diag, 4))

if __name__ == '__main__':
    print("定向耦合器 - 廖承恩《微波技术基础》第8.4节")
    print()

    example_3db_coupler()
    branch_coupler_design(3, 5e9)
    coupled_stripline_analysis(80, 50)
    verify_coupler_S_matrix()
    plot_coupler_frequency_response()
    plot_coupler_topology()
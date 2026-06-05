"""
第6章 微波网络基础 - S 参数分析
廖承恩《微波技术基础》

散射矩阵、ABCD矩阵、网络级联
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 6.2 / 6.4 散射矩阵
# ============================================================================

class TwoPortNetwork:
    """二端口微波网络"""

    def __init__(self, S=None, A=None, B=None, C=None, D=None, Z0=50.0):
        """
        初始化: 传入 S 参数或 ABCD 参数
        """
        self.Z0 = Z0
        if S is not None:
            self.S = np.array(S, dtype=complex)
        else:
            self.S = None

        if A is not None:
            self.A, self.B, self.C, self.D = A, B, C, D
            self._compute_S_from_ABCD()
        else:
            self.A = self.B = self.C = self.D = None

    def _compute_S_from_ABCD(self):
        """由 ABCD 计算 S 参数 (Z0 参考阻抗)"""
        A, B, C, D = self.A, self.B, self.C, self.D
        denom = A + B/self.Z0 + C*self.Z0 + D
        S11 = (A + B/self.Z0 - C*self.Z0 - D) / denom
        S12 = 2 * (A*D - B*C)**0.5 / denom  # 互易网络
        S21 = 2 * (A*D - B*C)**0.5 / denom
        S22 = (-A + B/self.Z0 - C*self.Z0 + D) / denom
        self.S = np.array([[S11, S12], [S21, S22]], dtype=complex)

    def _compute_ABCD_from_S(self):
        """由 S 参数计算 ABCD"""
        S = self.S
        denom = 2 * S[0,1] * self.Z0 - S[1,1] * S[0,0] + 1
        A = (S[0,0] * S[1,1] - S[0,1] * S[1,0] + 1) / (2 * S[0,1] * self.Z0**0.5)
        B = self.Z0 * (S[0,0] + 1) / (2 * S[0,1] * self.Z0**0.5)
        C = (1 - S[0,0]) / (2 * S[0,1] * self.Z0**0.5)
        D = (S[1,1] + 1) / (2 * S[0,1] * self.Z0**0.5)
        self.A, self.B, self.C, self.D = A, B, C, D

    def get_S(self):
        """返回 S 参数"""
        return self.S

    def get_ABCD(self):
        """返回 ABCD 参数"""
        if self.A is None:
            self._compute_ABCD_from_S()
        return self.A, self.B, self.C, self.D

    def S11(self):
        """输入反射系数"""
        return self.S[0,0] if self.S is not None else None

    def S21(self):
        """前向传输系数"""
        return self.S[1,0] if self.S is not None else None

    def S12(self):
        """反向传输系数"""
        return self.S[0,1] if self.S is not None else None

    def S22(self):
        """输出反射系数"""
        return self.S[1,1] if self.S is not None else None

    def VSWR_port1(self):
        """端口1 VSWR"""
        S11 = self.S11()
        if S11 is None:
            return None
        gamma_abs = np.abs(S11)
        if gamma_abs == 1.0:
            return np.inf
        return (1 + gamma_abs) / (1 - gamma_abs)

    def VSWR_port2(self):
        """端口2 VSWR"""
        S22 = self.S22()
        if S22 is None:
            return None
        gamma_abs = np.abs(S22)
        if gamma_abs == 1.0:
            return np.inf
        return (1 + gamma_abs) / (1 - gamma_abs)

    def insert_loss_dB(self):
        """插入损耗 (dB)"""
        S21 = self.S21()
        if S21 is None:
            return None
        return -20 * np.log10(np.abs(S21))

    def return_loss_dB_port1(self):
        """端口1 回波损耗 (dB)"""
        S11 = self.S11()
        if S11 is None:
            return None
        return -20 * np.log10(np.abs(S11))

    def return_loss_dB_port2(self):
        """端口2 回波损耗 (dB)"""
        S22 = self.S22()
        if S22 is None:
            return None
        return -20 * np.log10(np.abs(S22))

    def is_reciprocal(self):
        """检验互易性: S12 == S21"""
        if self.S is None:
            return None
        return np.abs(self.S[0,1] - self.S[1,0]) < 1e-12

    def is_lossless(self):
        """检验无耗: [S]+[S] = [I]"""
        if self.S is None:
            return False
        S = self.S
        S_dagger = S.conj().T
        product = np.dot(S_dagger, S)
        I = np.eye(2)
        return np.allclose(product, I, atol=1e-8)


# ============================================================================
# 基本元件的 ABCD 参数
# ============================================================================

def ABCD_series_Z(Z):
    """
    串联阻抗 Z 的 ABCD 矩阵
    [A,B;C,D] = [1, Z; 0, 1]
    """
    return 1.0, Z, 0.0, 1.0

def ABCD_shunt_Y(Y):
    """
    并联导纳 Y 的 ABCD 矩阵
    [A,B;C,D] = [1, 0; Y, 1]
    """
    return 1.0, 0.0, Y, 1.0

def ABCD_transmission_line(Z0, theta):
    """
    特性阻抗 Z0、电长度 theta 的传输线段
    [A,B;C,D] = [cos(theta), j*Z0*sin(theta); j*(1/Z0)*sin(theta), cos(theta)]
    """
    A = np.cos(theta)
    B = 1j * Z0 * np.sin(theta)
    C = 1j * (1/Z0) * np.sin(theta)
    D = np.cos(theta)
    return A, B, C, D

def ABCD_transformer(n):
    """
    阻抗变换比为 n 的理想变压器
    V1 = n*V2, I1 = I2/n
    [A,B;C,D] = [n, 0; 0, 1/n]
    """
    return n, 0.0, 0.0, 1.0/n

def ABCD_connect(nw1, nw2):
    """
    两个二端口网络的级联
    [ABCD]_total = [ABCD]_1 * [ABCD]_2
    """
    A1, B1, C1, D1 = nw1.get_ABCD()
    A2, B2, C2, D2 = nw2.get_ABCD()

    A = A1*A2 + B1*C2
    B = A1*B2 + B1*D2
    C = C1*A2 + D1*C2
    D = C1*B2 + D1*D2
    return A, B, C, D

# ============================================================================
# S 参数运算
# ============================================================================

def S_to_reflection(Z_L, Z0=50.0):
    """负载阻抗 -> 反射系数"""
    return (Z_L - Z0) / (Z_L + Z0)

def reflection_to_Z(Gamma, Z0=50.0):
    """反射系数 -> 阻抗"""
    return Z0 * (1 + Gamma) / (1 - Gamma)

def S_series_Z(Z, Z0=50.0):
    """
    串联阻抗 Z 的二端口 S 参数
    """
    # ABCD
    A, B, C, D = ABCD_series_Z(Z)
    denom = 2 * Z0**0.5
    S11 = B / denom
    S21 = (A + B/Z0 - C*Z0 - D) / (A + B/Z0 + C*Z0 + D)  # 简化
    S12 = 2 * Z0**0.5 / (A + B/Z0 + C*Z0 + D) * (A*D - B*C)**0.5
    S22 = (C*Z0 + D - A) / (A + B/Z0 + C*Z0 + D)
    return np.array([[S11, S12], [S21, S22]], dtype=complex)

def S_shunt_Y(Y, Z0=50.0):
    """
    并联导纳 Y 的二端口 S 参数
    """
    A, B, C, D = ABCD_shunt_Y(Y)
    denom = (A + B/Z0 + C*Z0 + D)
    S11 = (A + B/Z0 - C*Z0 - D) / denom
    S21 = 2 * (A*D - B*C)**0.5 / denom
    S12 = S21
    S22 = (-A + B/Z0 - C*Z0 + D) / denom
    return np.array([[S11, S12], [S21, S22]], dtype=complex)

def S_network_cascade(S1, S2, Z0=50.0):
    """
    两个二端口网络级联的 S 参数 (简化计算)
    精确计算需要先把 S 参数转换为 ABCD, 级联后再转回 S
    """
    # 先转为 ABCD
    nw1 = TwoPortNetwork(S=S1, Z0=Z0)
    nw2 = TwoPortNetwork(S=S2, Z0=Z0)
    A1, B1, C1, D1 = nw1.get_ABCD()
    A2, B2, C2, D2 = nw2.get_ABCD()

    # 级联 ABCD
    A = A1*A2 + B1*C2
    B = A1*B2 + B1*D2
    C = C1*A2 + D1*C2
    D = C1*B2 + D1*D2

    # 重新计算 S
    denom = A + B/Z0 + C*Z0 + D
    S11_new = (A + B/Z0 - C*Z0 - D) / denom
    S12_new = 2 * (A*D - B*C)**0.5 / denom
    S21_new = 2 * (A*D - B*C)**0.5 / denom
    S22_new = (-A + B/Z0 - C*Z0 + D) / denom
    return np.array([[S11_new, S12_new], [S21_new, S22_new]], dtype=complex)

# ============================================================================
# 绘图
# ============================================================================

if __name__ == "__main__":
    # 示例: 理想传输线段的 S 参数
    Z0 = 50.0
    f = 3.0e9
    v_p = 2.0e8  # 假设相速度
    l = 0.025   # 25 mm
    beta = 2 * np.pi * f / v_p
    theta = beta * l

    S_line = np.array([[0, np.exp(-1j*theta)], [np.exp(-1j*theta), 0]], dtype=complex)
    print(f"理想传输线 (theta={theta:.2f} rad):")
    print(f"S11 = {S_line[0,0]:.4f}")
    print(f"S21 = {S_line[1,0]:.4f}")

    # 示例: 串联电阻
    R = 10.0
    S_R = S_series_Z(R, Z0)
    print(f"\n串联电阻 R={R} Ohm:")
    print(f"S11 = {S_R[0,0]:.4f} (输入匹配)")
    print(f"S21 = {S_R[1,0]:.4f} (传输系数)")
    print(f"插入损耗 = {-20*np.log10(np.abs(S_R[1,0])):.2f} dB")

    # 绘图: S11 vs theta (传输线)
    theta_range = np.linspace(0, 2*np.pi, 500)
    S11_range = [np.exp(-1j*t) for t in theta_range]

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.polar(theta_range, [np.abs(s) for s in S11_range], 'b-')
    plt.title('传输线 S11 幅度 (极坐标)')
    plt.subplot(1, 2, 2)
    plt.plot(theta_range, [np.angle(s) for s in S11_range], 'r-')
    plt.title('传输线 S11 相位')
    plt.xlabel('theta (rad)')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liaochengeng/figures/ch6_S_parameter.png', dpi=150)
    plt.close()
    print("\nS参数图已保存")

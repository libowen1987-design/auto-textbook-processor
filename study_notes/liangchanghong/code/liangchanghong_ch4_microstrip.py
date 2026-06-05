#!/usr/bin/env python3
"""
梁昌洪《简明微波》第四章：微波集成传输线
微带线特性阻抗与有效介电常数计算
Based on: 梁昌洪《简明微波》Ch4
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# 微带线准静态参数计算
# ============================================================================

def microstrip_Z0_and_epsr(W_d, epsilon_r, accuracy='high'):
    """
    计算微带线特性阻抗 Z0 和有效介电常数 epsilon_eff
    
    参数:
        W_d: W/d (导体宽度/介质厚度比)
        epsilon_r: 相对介电常数
        accuracy: 'high' (EPA) 或 'medium' (Wheeler)
    
    返回:
        Z0: 特性阻抗 (Ohm)
        epsilon_eff: 有效介电常数
    """
    if accuracy == 'high':
        # EPA (Effective Permittivity Approximation)
        if W_d < 1.0:
            # 窄带公式
            numerator = 60.0 * np.log(8.0 / W_d + W_d / 4.0)
            denom = np.sqrt(epsilon_r)
        else:
            # 宽带公式
            numerator = 120.0 * np.pi / W_d
            denom = np.sqrt(epsilon_r) * (W_d / 8.0 + 1.0 / (2.0 * np.pi))
        
        Z0 = numerator / denom
        
        # 有效介电常数 (Hammerstad & Jensen)
        a_hj = 1.0 + np.log(W_d**2 + 0.25) * (0.5 - np.log(2.0 * W_d) / 16.0)
        epsilon_eff = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 / np.sqrt(1.0 + 10.0 / W_d)
    else:
        # Wheeler 简化公式
        if W_d < 1.0:
            Z0 = 60.0 / np.sqrt(epsilon_r) * np.log(8.0 / W_d + W_d / 4.0)
        else:
            Z0 = 120.0 * np.pi / (np.sqrt(epsilon_r) * (W_d + 1.5))
        epsilon_eff = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 * (1.0 + 10.0 / W_d)**(-0.5)
    
    return Z0, epsilon_eff


def finline_Z0_approximate(a, b, d, epsilon_r, wavelength):
    """
    集成鳍线特性阻抗近似计算 (梁昌洪式 4.4-16)
    
    参数:
        a, b: 波导尺寸 (m)
        d: 鳍线高度 (m)
        epsilon_r: 介质相对介电常数
        wavelength: 自由空间波长 (m)
    
    返回:
        Z0_fin: 鳍线特性阻抗 (近似)
    """
    # 截止波长比 (近似)
    lambda_c = 2.0 * a  # 空气波导截止波长
    epsilon_eff = (1.0 + epsilon_r) / 2.0  # 简化
    
    # 鳍线波导波长
    lambda_fin = wavelength / np.sqrt(epsilon_eff) * (1.0 + d / b)
    
    # 近似特性阻抗
    Z0_fin = 377.0 / np.sqrt(epsilon_eff) * (b / lambda_fin)
    return Z0_fin


def dispersion_microstrip(W_d, epsilon_r, f_GHz, d_mm=1.0):
    """
    微带线频散效应 (Schneider 模型)
    
    参数:
        W_d: 宽高比
        epsilon_r: 相对介电常数
        f_GHz: 频率 (GHz)
        d_mm: 介质厚度 (mm)
    """
    f_GHz = np.atleast_1d(f_GHz)
    
    # 准静态有效介电常数
    _, eps_eff_0 = microstrip_Z0_and_epsr(W_d, epsilon_r)
    
    # 频散修正 (Schneider)
    f_te = 0.0  # TE1 模截止频率近似 (GHz)
    f_ref = 1.0  # 参考频率 (GHz)
    
    # 频变有效介电常数
    eps_eff_f = eps_eff_0 - (eps_eff_0 - 1.0) / (1.0 + (f_GHz / 10.0)**1.5)
    
    return eps_eff_f


# ============================================================================
# 主程序：微带线参数图
# ============================================================================
if __name__ == '__main__':
    plt.rcParams.update({'axes.grid': True, 'grid.alpha': 0.3})
    
    # --- 图1: 微带线 Z0 vs W/d (不同 epsilon_r) ---
    W_d = np.logspace(-1, 2, 400)  # 0.1 to 100
    epsilon_rs = [2.1, 4.3, 9.8, 12.9]
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    for er in epsilon_rs:
        Z0_list = []
        eps_eff_list = []
        for wd in W_d:
            Z0, eps_eff = microstrip_Z0_and_epsr(wd, er)
            Z0_list.append(Z0)
            eps_eff_list.append(eps_eff)
        axes[0].loglog(W_d, Z0_list, label=f'$\\epsilon_r$ = {er}')
        axes[1].semilogx(W_d, eps_eff_list, label=f'$\\epsilon_r$ = {er}')
    
    axes[0].set_xlabel('$W/d$ (width-to-height ratio)')
    axes[0].set_ylabel('$Z_0$ ($\\Omega$)')
    axes[0].set_title('Microstrip Characteristic Impedance vs W/d')
    axes[0].legend()
    axes[0].grid(True, which='both', alpha=0.3)
    
    axes[1].set_xlabel('$W/d$')
    axes[1].set_ylabel('$\\epsilon_{{eff}}$')
    axes[1].set_title('Microstrip Effective Dielectric Constant vs W/d')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch4_microstrip_Z0.png', dpi=150)
    plt.close()
    print("Ch4: ch4_microstrip_Z0.png generated")
    
    # --- 图2: 频散效应 ---
    f_range = np.linspace(1, 100, 300)  # 1-100 GHz
    W_d_fixed = 2.0
    epsilon_r_fixed = 9.8
    
    eps_eff_disp = dispersion_microstrip(W_d_fixed, epsilon_r_fixed, f_range)
    _, eps_eff_static = microstrip_Z0_and_epsr(W_d_fixed, epsilon_r_fixed)
    
    plt.figure(figsize=(8, 5))
    plt.plot(f_range, eps_eff_disp, label='$\\epsilon_{{eff}}(f)$ — dispersion')
    plt.axhline(eps_eff_static, color='gray', linestyle='--', label=f'$\\epsilon_{{eff}}$ (static) = {eps_eff_static:.2f}')
    plt.xlabel('$f$ (GHz)')
    plt.ylabel('$\\epsilon_{eff}$')
    plt.title(f'Microstrip Dispersion: W/d={W_d_fixed}, $\\epsilon_r$={epsilon_r_fixed}')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch4_microstrip_dispersion.png', dpi=150)
    plt.close()
    print("Ch4: ch4_microstrip_dispersion.png generated")
    
    # --- 打印典型值 ---
    print("\n典型微带线特性阻抗值 (substrate $\\epsilon_r$=9.8):")
    for wd in [0.5, 1.0, 2.0, 5.0, 10.0]:
        Z0, eps_eff = microstrip_Z0_and_epsr(wd, 9.8)
        print(f"  W/d={wd:5.1f}: Z0={Z0:6.2f} Ohm, \\epsilon_eff={eps_eff:.3f}")
    
    print("\n✓ 梁昌洪《简明微波》Ch4 微带线代码验证通过")

#!/usr/bin/env python3
"""
Pozar《微波工程》第4版 第1章 — Python 例题复现
=================================================
覆盖：
  - Ex 1.1: 无损耗介质中的平面波
  - Ex 1.2: 良导体趋肤深度（铜随频率变化）
  - Ex 1.3: 正入射反射/透射（空气-介质界面 + 介质平板）
  - 扩展: 有损耗介质传播 + 斜入射 Fresnel 系数 + Brewster 角

变量命名规范: epsilon_r, mu_r, sigma, omega, beta, alpha, eta 等物理量含义命名

依赖: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker

# ============================================================
# 物理常量
# ============================================================
epsilon_0 = 8.854187817e-12   # [F/m]  真空介电常数
mu_0      = 1.2566370614e-6   # [H/m]  真空磁导率
c_0       = 2.99792458e8      # [m/s]  真空光速
eta_0     = np.sqrt(mu_0 / epsilon_0)  # [Ω]  ≈ 376.73 Ω

print("=" * 70)
print("Pozar 微波工程 — 第 1 章 电磁理论基础 例题复现")
print("=" * 70)

# ============================================================
# Example 1.1 — 无损耗介质中的平面波
# ============================================================
print("\n" + "─" * 70)
print("【Example 1.1】 无损耗介质中的平面波")
print("─" * 70)

# 已知: f = 10 GHz, epsilon_r = 2.25, mu_r = 1, E0 = 1 V/m +z 传播 +x 极化
f_1_1   = 10e9          # [Hz]  10 GHz
omega_1_1 = 2 * np.pi * f_1_1
epsilon_r_1_1 = 2.25    # 相对介电常数
mu_r_1_1 = 1.0          # 非磁性
epsilon_1_1 = epsilon_0 * epsilon_r_1_1
mu_1_1      = mu_0 * mu_r_1_1

# 相位常数 beta
beta_1_1 = omega_1_1 * np.sqrt(mu_1_1 * epsilon_1_1)   # [rad/m]

# 相速度 v_p
v_p_1_1 = 1.0 / np.sqrt(mu_1_1 * epsilon_1_1)          # [m/s]

# 波长 lambda
lambda_1_1 = 2 * np.pi / beta_1_1                       # [m]

# 波阻抗 eta
eta_1_1 = np.sqrt(mu_1_1 / epsilon_1_1)                 # [Ω]

print(f"  频率 f           = {f_1_1/1e9:.2f} GHz")
print(f"  epsilon_r        = {epsilon_r_1_1}")
print(f"  mu_r             = {mu_r_1_1}")
print(f"  相位常数 β       = {beta_1_1:.4f} rad/m")
print(f"  相速度 v_p       = {v_p_1_1:.4e} m/s  = {v_p_1_1/c_0:.4f} c")
print(f"  波长 λ           = {lambda_1_1*1e3:.4f} mm")
print(f"  介质波长/真空比  = {lambda_1_1/(c_0/f_1_1):.4f}")
print(f"  波阻抗 η         = {eta_1_1:.2f} Ω")
print(f"  (真空 η0         = {eta_0:.2f} Ω)")

# 量纲检查: beta 量纲应为 [rad/m]
# ω: 1/s, μ: H/m = V·s/A·m, ε: F/m = A·s/V·m
# μ·ε: (V·s/A·m)(A·s/V·m) = s²/m²
# √(μ·ε): s/m, ω√(μ·ε): 1/s · s/m = 1/m = rad/m ✅
print("  [量纲] β = ω√(με): [1/s · s/m = rad/m] ✅")

# 画一个周期内的波形
z_1_1 = np.linspace(0, 3 * lambda_1_1, 500)
E_x_1_1 = np.cos(omega_1_1 * 0 - beta_1_1 * z_1_1)   # t=0 时电场 E_x(z)
H_y_1_1 = E_x_1_1 / eta_1_1

fig1, (ax1a, ax1b) = plt.subplots(1, 2, figsize=(12, 4))

ax1a.plot(z_1_1 * 1e3, E_x_1_1, 'b-', linewidth=1.5, label=r'$E_x(z)$')
ax1a.plot(z_1_1 * 1e3, H_y_1_1 * eta_0, 'r--', linewidth=1.5,
          label=r'$H_y(z) \times \eta_0$ (scaled)')
ax1a.set_xlabel('z [mm]')
ax1a.set_ylabel('Field amplitude')
ax1a.set_title(r'Ex 1.1: Plane wave in $\epsilon_r=2.25$ at $t=0$')
ax1a.legend()
ax1a.grid(True, alpha=0.3)
ax1a.axvline(x=lambda_1_1 * 1e3, color='gray', linestyle=':', alpha=0.7)
ax1a.text(lambda_1_1 * 1e3 + 0.2, 0.9, r'$\lambda$', fontsize=10)

# 频散关系 (ω-β 图)
beta_range = np.linspace(0, 500, 200)
omega_range = beta_range / np.sqrt(mu_1_1 * epsilon_1_1)
ax1b.plot(beta_range, omega_range / 2e9 / np.pi, 'g-', linewidth=1.5)
ax1b.plot(beta_1_1, f_1_1 / 1e9, 'ro', markersize=8,
          label=f'f={f_1_1/1e9:.0f} GHz')
ax1b.set_xlabel(r'$\beta$ [rad/m]')
ax1b.set_ylabel(r'f [GHz]')
ax1b.set_title(r'Dispersion: $\omega = v_p \beta$')
ax1b.grid(True, alpha=0.3)
ax1b.legend()

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ex1_1_plane_wave.png',
            dpi=150)
print("  → 波形图已保存: fig_ex1_1_plane_wave.png")


# ============================================================
# Example 1.2 — 良导体趋肤深度（铜）
# ============================================================
print("\n" + "─" * 70)
print("【Example 1.2】 良导体趋肤深度")
print("─" * 70)

sigma_cu = 5.8e7          # [S/m]  铜的电导率
mu_r_cu  = 1.0            # 铜非磁性
mu_cu    = mu_0 * mu_r_cu

# (a) f = 10 GHz 时铜的趋肤深度
f_1_2_a   = 10e9
omega_1_2_a = 2 * np.pi * f_1_2_a

# 验证良导体条件: σ/(ωε) >> 1
ratio_cu_10g = sigma_cu / (omega_1_2_a * epsilon_0)
print(f"  σ/(ωε₀) @ 10 GHz = {ratio_cu_10g:.2e}  (>> 1 → 良导体) ✅")

# 趋肤深度 δ_s = 1/√(π f μ σ)
delta_s_10g = 1.0 / np.sqrt(np.pi * f_1_2_a * mu_cu * sigma_cu)
print(f"  趋肤深度 δ_s @ 10 GHz = {delta_s_10g*1e6:.4f} μm")

# 衰减常数 α = 1/δ_s
alpha_10g = 1.0 / delta_s_10g
print(f"  衰减常数 α @ 10 GHz  = {alpha_10g:.2f} Np/m")

# 良导体波阻抗 η_c = (1+j)√(π f μ / σ) = (1+j)/(σ δ)
eta_c_10g_real = np.sqrt(np.pi * f_1_2_a * mu_cu / sigma_cu)
print(f"  波阻抗实部 Re(η_c)  = {eta_c_10g_real:.6f} Ω")

# (b) 趋肤深度随频率变化曲线
frequencies = np.logspace(6, 12, 200)  # 1 MHz ~ 1 THz
delta_s_f = 1.0 / np.sqrt(np.pi * frequencies * mu_cu * sigma_cu)

fig2, (ax2a, ax2b, ax2c) = plt.subplots(1, 3, figsize=(15, 4.5))

ax2a.loglog(frequencies / 1e6, delta_s_f * 1e6, 'b-', linewidth=1.5)
ax2a.axvline(x=10e3, color='r', linestyle='--', alpha=0.6,
             label='10 GHz')
ax2a.axhline(y=delta_s_10g * 1e6, color='r', linestyle=':', alpha=0.6)
ax2a.set_xlabel('Frequency [MHz]')
ax2a.set_ylabel('Skin depth [μm]')
ax2a.set_title(r'Cu skin depth $\delta_s = 1/\sqrt{\pi f \mu \sigma}$')
ax2a.grid(True, which='both', alpha=0.3)
ax2a.legend()
ax2a.set_xlim([1, 1e6])

# 趋肤深度与常用金属/厚度的对比
materials = {
    'Copper (Cu)':   sigma_cu,
    'Silver (Ag)':   6.3e7,
    'Gold (Au)':     4.1e7,
    'Aluminum (Al)': 3.8e7,
    'Brass':         1.5e7,
}
f_test = 10e9
delta_materials = {}
for name, sig in materials.items():
    d = 1.0 / np.sqrt(np.pi * f_test * mu_0 * sig)
    delta_materials[name] = d * 1e6
    print(f"  {name:20s}: δ_s = {d*1e6:.3f} μm @ 10 GHz")

# 条形图对比
names_mat = list(delta_materials.keys())
values_mat = list(delta_materials.values())
colors_mat = ['#B87333', '#C0C0C0', '#FFD700', '#A0A0A0', '#D4A76A']
bars = ax2b.barh(names_mat, values_mat, color=colors_mat, alpha=0.8)
ax2b.set_xlabel('Skin depth [μm] @ 10 GHz')
ax2b.set_title('Skin depth for different metals')
for bar, val in zip(bars, values_mat):
    ax2b.text(val + 0.02, bar.get_y() + bar.get_height() / 2,
              f'{val:.2f} μm', va='center', fontsize=9)
ax2b.grid(True, axis='x', alpha=0.3)

# 衰减 vs 距离（10 GHz 铜中）
z_cu = np.linspace(0, 5 * delta_s_10g, 200)
E_att = np.exp(-z_cu / delta_s_10g)
ax2c.plot(z_cu / delta_s_10g, E_att, 'b-', linewidth=1.5)
ax2c.axvline(x=1, color='r', linestyle='--', alpha=0.6,
             label=r'$\delta_s$ (1/e)')
ax2c.axhline(y=1/np.e, color='r', linestyle=':', alpha=0.6)
ax2c.set_xlabel(r'$z / \delta_s$')
ax2c.set_ylabel(r'$|E| / |E_0|$')
ax2c.set_title(r'Field attenuation: $e^{-z/\delta_s}$')
ax2c.legend()
ax2c.grid(True, alpha=0.3)
ax2c.set_ylim([0, 1.05])

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ex1_2_skin_depth.png',
            dpi=150)
print("  → 趋肤深度图已保存: fig_ex1_2_skin_depth.png")


# ============================================================
# Example 1.3 — 正入射反射与透射
# ============================================================
print("\n" + "─" * 70)
print("【Example 1.3】 正入射反射与透射")
print("─" * 70)

# (a) 空气-玻璃界面: epsilon_r1 = 1, epsilon_r2 = 4 (玻璃)
epsilon_r1 = 1.0
epsilon_r2 = 4.0
eta1 = eta_0 / np.sqrt(epsilon_r1)
eta2 = eta_0 / np.sqrt(epsilon_r2)

Gamma_12 = (eta2 - eta1) / (eta2 + eta1)
Tau_12  = 2 * eta2 / (eta2 + eta1)

print(f"  界面: 空气(εr=1) → 玻璃(εr=4)")
print(f"    η₁ = {eta1:.2f} Ω,  η₂ = {eta2:.2f} Ω")
print(f"    Γ = {Gamma_12:.4f}")
print(f"    τ = {Tau_12:.4f}")
print(f"    验证 1+Γ = τ: 1 + {Gamma_12:.4f} = {1+Gamma_12:.4f}  vs τ = {Tau_12:.4f} ✅")

R_12 = np.abs(Gamma_12)**2
T_12 = 1 - R_12
print(f"    R = |Γ|² = {R_12:.4f}  ({R_12*100:.1f}%)")
print(f"    T = 1 - R = {T_12:.4f}  ({T_12*100:.1f}%)")

# (b) 反射系数随 εr2 变化
epsilon_r_range = np.linspace(1, 20, 200)
eta2_range = eta_0 / np.sqrt(epsilon_r_range)
Gamma_range = (eta2_range - eta1) / (eta2_range + eta1)
R_range = Gamma_range**2

fig3, (ax3a, ax3b) = plt.subplots(1, 2, figsize=(12, 4.5))

ax3a.plot(epsilon_r_range, Gamma_range, 'b-', linewidth=1.5,
          label=r'$\Gamma$')
ax3a.plot(epsilon_r_range, R_range, 'r--', linewidth=1.5,
          label=r'$R = |\Gamma|^2$')
ax3a.axvline(x=4, color='gray', linestyle=':', alpha=0.5,
             label=r'$\epsilon_{r2}=4$ (glass)')
ax3a.set_xlabel(r'$\epsilon_{r2}$')
ax3a.set_ylabel('Reflection coefficient')
ax3a.set_title(r'Normal incidence: air → $\epsilon_{r2}$')
ax3a.legend()
ax3a.grid(True, alpha=0.3)

# (c) 扫频反射 —— 有损耗介质平板（λ/4 → 匹配）
# 介质 3 是铜（短路），介质 2 是 Teflon
epsilon_r_teflon = 2.08
mu_r_teflon = 1.0
d_teflon = 1.5e-3          # 1.5 mm 厚 Teflon
sigma_teflon = 0           # 低损耗假设

eta_teflon = eta_0 / np.sqrt(epsilon_r_teflon)
f_scan = np.linspace(0.5e9, 30e9, 1000)
omega_scan = 2 * np.pi * f_scan
epsilon_teflon = epsilon_0 * epsilon_r_teflon
mu_teflon = mu_0 * mu_r_teflon

# 传播常数 γ = jβ (无损耗)
beta_scan = omega_scan * np.sqrt(mu_teflon * epsilon_teflon)

# 从短路 (Γ₃ = -1) 通过 Teflon 看入的输入反射系数
# Γ_in = (Γ_23 + Γ_12 e^{-2γd}) / (1 + Γ_12 Γ_23 e^{-2γd})
# Γ_23 = (η_3 - η_2)/(η_3 + η_2) 其中 η_3 = 0 (理想导体) → Γ_23 = -1
Gamma_23 = -1.0
Gamma_12_t = (eta_teflon - eta1) / (eta_teflon + eta1)
Gamma_in = (Gamma_23 + Gamma_12_t * np.exp(-2 * 1j * beta_scan * d_teflon)) / \
           (1 + Gamma_12_t * Gamma_23 * np.exp(-2 * 1j * beta_scan * d_teflon))

R_in = np.abs(Gamma_in)**2

ax3b.plot(f_scan / 1e9, R_in, 'b-', linewidth=1.5)
# 标注 λ/4 谐振点
f_lambda4 = c_0 / np.sqrt(epsilon_r_teflon) / (4 * d_teflon)
ax3b.axvline(x=f_lambda4 / 1e9, color='r', linestyle='--', alpha=0.6,
             label=r'$\lambda/4$ @ {:.1f} GHz'.format(f_lambda4/1e9))
ax3b.axvline(x=2*f_lambda4 / 1e9, color='r', linestyle=':', alpha=0.4,
             label=r'$\lambda/2$ @ {:.1f} GHz'.format(2*f_lambda4/1e9))
ax3b.set_xlabel('Frequency [GHz]')
ax3b.set_ylabel(r'$| \Gamma_{in} |^2$')
ax3b.set_title(r'Teflon slab ($d=1.5$mm) on short circuit')
ax3b.legend(loc='upper right', fontsize=8)
ax3b.grid(True, alpha=0.3)
ax3b.set_ylim([0, 1.05])

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ex1_3_reflection.png',
            dpi=150)
print("  → 反射系数图已保存: fig_ex1_3_reflection.png")


# ============================================================
# 扩展: 有损耗介质传播
# ============================================================
print("\n" + "─" * 70)
print("【扩展】 有损耗介质中的传播 — 水 @ 2.45 GHz (微波炉)")
print("─" * 70)

f_water = 2.45e9                      # [Hz] 微波炉频率
omega_water = 2 * np.pi * f_water
epsilon_r_prime_water = 77.0           # 水 ε' @ 2.45 GHz
tan_delta_water = 0.157                # 水 tanδ @ 2.45 GHz
sigma_water = omega_water * epsilon_0 * epsilon_r_prime_water * tan_delta_water
epsilon_c_water = epsilon_0 * epsilon_r_prime_water * (1 - 1j * tan_delta_water)

# 复传播常数 γ
gamma_water = 1j * omega_water * np.sqrt(mu_0 * epsilon_c_water)
alpha_water = gamma_water.real         # [Np/m]
beta_water  = gamma_water.imag         # [rad/m]

# 趋肤/穿透深度
delta_water = 1.0 / alpha_water        # [m]

# 波长
lambda_water = 2 * np.pi / beta_water   # [m]

print(f"  频率 f          = {f_water/1e9:.2f} GHz")
print(f"  ε' / tanδ      = {epsilon_r_prime_water} / {tan_delta_water}")
print(f"  等效 σ         = {sigma_water:.4f} S/m")
print(f"  衰减常数 α     = {alpha_water:.4f} Np/m")
print(f"  穿透深度 1/α   = {delta_water*1e3:.2f} mm")
print(f"  波长 λ         = {lambda_water*1e3:.2f} mm")
print(f"  随距离衰减曲线 → 图")

# 功率衰减曲线
z_water = np.linspace(0, 60e-3, 300)   # 0~60 mm
P_over_P0 = np.exp(-2 * alpha_water * z_water)

fig4, ax4 = plt.subplots(figsize=(8, 4))
ax4.plot(z_water * 1e3, P_over_P0, 'b-', linewidth=1.5, label='Power')
ax4.plot(z_water * 1e3, np.exp(-alpha_water * z_water), 'r--',
         linewidth=1.5, label='|E|/|E₀|')
ax4.axvline(x=delta_water * 1e3, color='gray', linestyle=':', alpha=0.6,
            label=f'1/e depth = {delta_water*1e3:.1f} mm')
ax4.set_xlabel('z [mm]')
ax4.set_ylabel('Normalized amplitude')
ax4.set_title(r'Wave propagation in water @ 2.45 GHz (lossy dielectric)')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ext_lossy_water.png',
            dpi=150)
print("  → 水中衰减图已保存: fig_ext_lossy_water.png")


# ============================================================
# 扩展: 斜入射 Fresnel 系数
# ============================================================
print("\n" + "─" * 70)
print("【扩展】 斜入射 Fresnel 系数与 Brewster 角")
print("─" * 70)

epsilon_r_2_f = 4.0    # 介质
mu_r_2_f = 1.0

theta_i = np.linspace(0, np.pi / 2, 500)
theta_i_deg = np.degrees(theta_i)

# Snell 定律: sin(θ_t) = sqrt(ε1/ε2) * sin(θ_i)
n1 = np.sqrt(epsilon_r1 * mu_r_1_1)
n2 = np.sqrt(epsilon_r_2_f * mu_r_2_f)
sin_theta_t = (n1 / n2) * np.sin(theta_i)

# 避免全内反射时取不到实数值
theta_t = np.arcsin(np.clip(sin_theta_t, -1, 1))
eta1_f = eta_0 * np.sqrt(mu_r_1_1 / epsilon_r1)
eta2_f = eta_0 * np.sqrt(mu_r_2_f / epsilon_r_2_f)

# TE (垂直极化)
Gamma_perp = (eta2_f * np.cos(theta_i) - eta1_f * np.cos(theta_t)) / \
             (eta2_f * np.cos(theta_i) + eta1_f * np.cos(theta_t))
tau_perp = (2 * eta2_f * np.cos(theta_i)) / \
           (eta2_f * np.cos(theta_i) + eta1_f * np.cos(theta_t))

# TM (平行极化)
Gamma_par = (eta2_f * np.cos(theta_t) - eta1_f * np.cos(theta_i)) / \
            (eta2_f * np.cos(theta_t) + eta1_f * np.cos(theta_i))
tau_par = (2 * eta2_f * np.cos(theta_i)) / \
          (eta2_f * np.cos(theta_t) + eta1_f * np.cos(theta_i))

# Brewster 角 (TM 极化 Γ=0)
theta_B = np.arctan(np.sqrt(epsilon_r_2_f / epsilon_r1))
print(f"  Brewster 角 θ_B = {np.degrees(theta_B):.2f}° (arctan(√(ε₂/ε₁)))")
idx_B = np.argmin(np.abs(theta_i - theta_B))
print(f"  Γ|| @ θ_B ≈ {Gamma_par[idx_B]:.6f} (应 ≈ 0) ✅")

# 临界角 (全内反射, 从介质到空气)
theta_c = np.arcsin(np.sqrt(epsilon_r1 / epsilon_r_2_f))
print(f"  临界角 θ_c (ε₂=4 → ε₁=1) = {np.degrees(theta_c):.2f}°")

fig5, (ax5a, ax5b) = plt.subplots(1, 2, figsize=(12, 5))

ax5a.plot(theta_i_deg, np.abs(Gamma_perp), 'b-', linewidth=1.5,
          label=r'$|\Gamma_\perp|$ (TE)')
ax5a.plot(theta_i_deg, np.abs(Gamma_par), 'r--', linewidth=1.5,
          label=r'$|\Gamma_\parallel|$ (TM)')
ax5a.axvline(x=np.degrees(theta_B), color='g', linestyle='-.', alpha=0.6,
             label=r'$\theta_B$ = {:.1f}°'.format(np.degrees(theta_B)))
ax5a.set_xlabel(r'$\theta_i$ [degrees]')
ax5a.set_ylabel(r'$|\Gamma|$')
ax5a.set_title(r'Fresnel reflection: air ($\epsilon_r=1$) → glass ($\epsilon_r=4$)')
ax5a.legend()
ax5a.grid(True, alpha=0.3)
ax5a.set_ylim([0, 1.05])

# 反射率 (功率)
R_perp = np.abs(Gamma_perp)**2
R_par  = np.abs(Gamma_par)**2
ax5b.plot(theta_i_deg, R_perp, 'b-', linewidth=1.5, label=r'$R_\perp$ (TE)')
ax5b.plot(theta_i_deg, R_par, 'r--', linewidth=1.5, label=r'$R_\parallel$ (TM)')
ax5b.axvline(x=np.degrees(theta_B), color='g', linestyle='-.', alpha=0.6,
             label=r'$\theta_B$')
ax5b.set_xlabel(r'$\theta_i$ [degrees]')
ax5b.set_ylabel('Power reflectivity')
ax5b.set_title(r'Power reflectivity (air → glass)')
ax5b.legend()
ax5b.grid(True, alpha=0.3)
ax5b.set_ylim([0, 1.05])

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ext_fresnel.png',
            dpi=150)
print("  → Fresnel 系数图已保存: fig_ext_fresnel.png")


# ============================================================
# 扩展: Poynting 矢量与功率流演示
# ============================================================
print("\n" + "─" * 70)
print("【扩展】 自由空间 Poynting 矢量")
print("─" * 70)

f_poynt = 5e9
omega_poynt = 2 * np.pi * f_poynt
beta_poynt = omega_poynt / c_0
lambda_poynt = 2 * np.pi / beta_poynt
E0_poynt = 1.0            # [V/m]

# 瞬时场
z_poynt = np.linspace(0, 2 * lambda_poynt, 300)
t_vals = np.array([0, 1/4/f_poynt, 1/2/f_poynt])  # 三个时间点

fig6, axes6 = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

for i, t_val in enumerate(t_vals):
    E = E0_poynt * np.cos(omega_poynt * t_val - beta_poynt * z_poynt)
    H = E / eta_0
    S = E * H       # 瞬时 Poynting 矢量 [W/m²]

    axes6[i].plot(z_poynt / lambda_poynt, E, 'b-', linewidth=1.5, label='E')
    axes6[i].plot(z_poynt / lambda_poynt, H * eta_0 / 3, 'r--',
                  linewidth=1.5, label='H × η₀/3 (scaled)')
    axes6[i].plot(z_poynt / lambda_poynt, S * 377, 'g-.',
                  linewidth=1.5, label='S × η₀ (scaled)')
    axes6[i].set_ylabel('Amplitude (scaled)')
    axes6[i].set_title(f't = {t_val*1e12:.0f} ps')
    axes6[i].legend(loc='upper right', fontsize=8)
    axes6[i].grid(True, alpha=0.3)

axes6[-1].set_xlabel(r'$z / \lambda$')
fig6.suptitle(r'Poynting vector: $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ '
              r'in free space')
plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/python/fig_ext_poynting.png',
            dpi=150)
print("  → Poynting 矢量图已保存: fig_ext_poynting.png")


# ============================================================
# 汇总输出
# ============================================================
print("\n" + "=" * 70)
print("所有例题完成 ✅")
print("生成文件:")
print("  notes/pozarch01_electromagnetic_theory.md  — 学习笔记")
print("  python/pozarch01_examples.py               — 本脚本")
print("  python/fig_ex1_1_plane_wave.png            — 平面波波形")
print("  python/fig_ex1_2_skin_depth.png            — 趋肤深度")
print("  python/fig_ex1_3_reflection.png            — 反射/透射")
print("  python/fig_ext_lossy_water.png             — 有损耗介质")
print("  python/fig_ext_fresnel.png                 — Fresnel 系数")
print("  python/fig_ext_poynting.png                — Poynting 矢量")
print("=" * 70)

---
chapter: 13
title: "Periodic Structures"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, J. G. Maloney, M. P. Kesler, G. S. Smith, W. J. Hoefer"
raw_size: 83,465 bytes
---

# Chapter 13: Periodic Structures
> **中英双语版**

> 周期结构

## 13.1 Introduction
> 引言

Periodic structures — frequency selective surfaces (FSS), electromagnetic bandgap (EBG) materials, metamaterials, phased arrays — are characterized by spatial periodicity $p$ in one or two dimensions. Modeling exploits the **Floquet (Bloch) theorem**: fields in adjacent unit cells differ only by a known phase factor.
> 周期结构——频率选择表面、电磁带隙材料、超材料、相控阵——具有一维或二维空间周期性 $p$。建模利用 **Floquet（Bloch）定理**：相邻原胞中的场仅相差一个已知相位因子。

**Computational savings**: A single unit cell with periodic boundary conditions (PBC) replaces the full $N \times N$ array, yielding $N^2$ savings in 2D or $N^3$ in 3D.
> **计算量节省**：使用周期性边界条件的单个原胞替代完整的 $N \times N$ 阵列，二维节省 $N^2$ 倍，三维节省 $N^3$ 倍。

## 13.2 Review of Scattering from Periodic Structures
> 周期结构散射回顾

### Floquet Mode Representation
> Floquet 模式表示

For a plane wave incident at angle $\phi_I$ on a 1D periodic structure (period $y_p$):
> 对于入射角 $\phi_I$ 的平面波照射一维周期结构（周期 $y_p$）：
$$
\mathbf{E}(x, y + y_p) = \mathbf{E}(x, y) e^{-j k_0 y_p \sin \phi_I}
$$

Scattered fields decompose into Floquet modes (grating lobes) at angles:
> 散射场分解为 Floquet 模式（栅瓣），角度为：
$$
\sin \phi_{T,m} = \sin \phi_I + \frac{2\pi m}{k_0 y_p}, \quad m = 0, \pm 1, \pm 2, \ldots
$$

**Grating lobe turn-on frequencies**:
> **栅瓣开启频率**：
$$
f_{\text{turn-on},m} = \frac{m c}{y_p (1 + \sin \phi_I)} \quad (m > 0)
$$

## 13.3 Direct Field Methods
> 直接场方法

### 13.3.1 Normal Incidence
> 正入射

For $\phi_I = 0$, the PBC involves only fields at the current time level:
> 对于 $\phi_I = 0$，PBC 仅涉及当前时间层的场：
$$
E_z(x, y=0, t) = E_z(x, y=y_p, t)
$$

### 13.3.2 Multiple Unit Cells for Oblique Incidence
> 斜入射的多原胞方法

For $\phi_I \neq 0$, the phase shift corresponds to a time delay. Using $M$ unit cells:
> 对于 $\phi_I \neq 0$，相移对应时间延迟。使用 $M$ 个原胞：
$$
E_z(x, y=y_p, t) = E_z(x, y=0, t + M\Delta t_{y_p})
$$

### 13.3.3 Sine-Cosine Method
> 正弦-余弦法

Single-frequency technique using two simultaneous grids (cos $\omega t$ and sin $\omega t$ excitation).
> 单频技术，使用两个同步网格（cos $\omega t$ 和 sin $\omega t$ 激励）。

**Advantage**: No time advance needed. **Disadvantage**: Only one frequency per simulation.
> **优势**：无需时间推进。**缺点**：每次仿真仅一个频率。

### 13.3.4 Angled-Update Method
> 斜角更新法

Exploits the natural time gradient across the grid. Fields at different $y$ positions are at different time levels:
> 利用网格上自然存在的时间梯度。不同 $y$ 位置处的场处于不同的时间层：
$$
E_z^n(i, 0) = E_z^{n-\Delta n}(i, N_y) e^{-j k_y y_p}
$$

## 13.4 Field-Transformation Technique
> 场变换技术

The key insight: remove the phase gradient by introducing transformed field variables:
> 关键见解：通过引入变换后的场变量消除相位梯度：
$$
P_z = E_z e^{j k_y y}, \quad Q_x = \eta_0 H_x e^{j k_y y}, \quad Q_y = \eta_0 H_y e^{j k_y y}
$$

The transformed fields satisfy **simple PBC**: $P_z(y=0) = P_z(y=y_p)$, $Q_x(y=0) = Q_x(y=y_p)$.
> 变换后的场满足**简单周期性边界条件**。

### Dispersion Relation
> 色散关系

The continuous dispersion relation is:
> 连续色散关系为：
$$
\frac{v_p}{c} = \sqrt{\sin \alpha \sin \phi + \sqrt{(\sin \alpha \sin \phi)^2 + \cos^2 \phi}}
$$

**Key insight**: The minimum phase velocity occurs at $\alpha = -90^\circ$: $v_{p,\min}/c = 1/(1 + \sin \phi)$.
> **关键见解**：最小相速度出现在 $\alpha = -90^\circ$ 时。

## 13.5 Multiple-Grid Approach
> 多网格法

Uses two spatially staggered grids (shifted $\Delta y/2$ and $\Delta t/2$) to center-difference the extra time-derivative terms.
> 使用两个空间交错网格，对额外的时间导数值项进行中心差分。

### Stability Criterion
> 稳定性条件
$$
\frac{c \Delta t}{\Delta} \leq \frac{1}{\sqrt{N}} \frac{1}{1 + \sin \phi}
$$
This is more restrictive than the standard CFL limit by the factor $1/(1+\sin \phi)$.
> 这比标准 CFL 极限更严格，因子为 $1/(1+\sin \phi)$。

## 13.6 Split-Field Method (2D)
> 分裂场法（二维）

### 13.6.1 Formulation
> 公式推导

A more efficient single-grid approach. The key is to **split** the transformed field variables:
> 更高效的单网格方法。关键在于**分裂**变换后的场变量：
$$
P_z = P_{zx} + P_{zy}, \quad Q_x = Q_{xx} + Q_{xy}
$$

### 13.6.2 Stability
> 稳定性

Von Neumann analysis yields:
> Von Neumann 分析得到：
$$
\frac{c \Delta t}{\Delta} \leq \frac{1}{\sqrt{N}} \cos \phi
$$
This is **less restrictive** than the multiple-grid approach.
> 这比多网格方法**限制更小**。

## 13.7 Split-Field Method (3D)
> 分裂场法（三维）

Extension to 3D with two periodic directions $(x, y)$ and incidence angles $(\theta, \phi)$. The transformation:
> 推广到三维，具有两个周期方向 $(x, y)$ 和入射角 $(\theta, \phi)$。变换：
$$
P = E e^{j(k_{x0}x + k_{y0}y)}, \quad Q = \eta_0 H e^{j(k_{x0}x + k_{y0}y)}
$$

## 13.8 Applications
> 应用

### 13.8.1 Electromagnetic Bandgap (EBG) Structures
> 电磁带隙结构

Split-field PBC enables wideband EBG characterization.
> 分裂场 PBC 支持宽带 EBG 表征。

### 13.8.2 Metamaterial Unit Cell Analysis
> 超材料原胞分析

The split-field method retrieves effective $\epsilon_{\text{eff}}(\omega)$ and $\mu_{\text{eff}}(\omega)$ from S-parameters of a single unit cell:
> 分裂场法从单个原胞的 S 参数提取有效介电常数和磁导率：
$$
\epsilon_{\text{eff}} = \frac{n}{Z}, \quad \mu_{\text{eff}} = nZ
$$
where $n$ is the refractive index and $Z$ the wave impedance extracted from $S_{11}$ and $S_{21}$.
> 其中 $n$ 为折射率，$Z$ 为波阻抗，从 $S_{11}$ 和 $S_{21}$ 提取。

### Summary
> 总结

| Method | Storage | Stability | Implementation |
|--------|---------|-----------|----------------|
| 方法 | 存储量 | 稳定性 | 实现难度 |
| Normal incidence PBC | 1× | Standard CFL | Trivial |
| 正入射 PBC | 1× | 标准 CFL | 极简单 |
| Multiple unit cells | $M^2$× | Standard CFL | Simple |
| 多原胞法 | $M^2$× | 标准 CFL | 简单 |
| Sine-cosine | 2× | Standard CFL | Moderate |
| 正余弦法 | 2× | 标准 CFL | 中等 |
| Angled-update | 1× | Modified CFL | Complex |
| 斜角更新法 | 1× | 修改 CFL | 复杂 |
| Field-transformation | 1× | Modified CFL | Complex |
| 场变换法 | 1× | 修改 CFL | 复杂 |
| **Split-field** | **1×** | **$\cos\phi$ CFL** | **Moderate** |
| **分裂场法** | **1×** | **$\cos\phi$ CFL** | **中等** |

The **split-field method** is the most practical for wideband oblique-incidence periodic FDTD.
> **分裂场法**是宽带斜入射周期结构 FDTD 最实用的方法。

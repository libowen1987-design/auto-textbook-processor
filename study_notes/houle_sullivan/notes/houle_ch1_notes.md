# Chapter 1 — One-Dimensional Simulation with the FDTD Method

> **中英双语版**
> **Source:** Houle & Sullivan, *Electromagnetic Simulation Using the FDTD Method with Python*, 3rd ed. (IEEE Press, 2020), Ch. 1

---

## 1.1 One-Dimensional Free-Space Simulation | 一维自由空间仿真

### Maxwell's Equations in 1D Free Space | 一维自由空间中的麦克斯韦方程组

For a plane wave propagating in the $z$-direction with $\mathbf{E}$ in $x$ and $\mathbf{H}$ in $y$:
对于沿 $z$ 方向传播的平面波，$\mathbf{E}$ 在 $x$ 方向，$\mathbf{H}$ 在 $y$ 方向：

$$
\frac{\partial E_x}{\partial t} = -\frac{1}{\varepsilon_0} \frac{\partial H_y}{\partial z} \tag{1.2a}
$$
$$
\frac{\partial H_y}{\partial t} = -\frac{1}{\mu_0} \frac{\partial E_x}{\partial z} \tag{1.2b}
$$

### Central Difference Discretization (Yee Grid) | 中心差分离散化（Yee 网格）

Using central differences in both time and space:
在时间和空间上都使用中心差分：

$$
E_x^{n+\frac{1}{2}}[k] = E_x^{n-\frac{1}{2}}[k] - \frac{\Delta t}{\varepsilon_0 \Delta x}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.4a}
$$
$$
H_y^{n+1}[k+\tfrac{1}{2}] = H_y^n[k+\tfrac{1}{2}] - \frac{\Delta t}{\mu_0 \Delta x}\left(E_x^{n+\frac{1}{2}}[k+1] - E_x^{n+\frac{1}{2}}[k]\right) \tag{1.4b}
$$

### Normalized Field Variables | 归一化场变量

Define: $\quad \tilde{E}_x = \sqrt{\varepsilon_0/\mu_0}\;E_x$
定义归一化电场，使得 $\tilde{E}_x$ 和 $H_y$ 具有相同的量级（对 PML 公式有重要优势）。

This gives $\tilde{E}_x$ and $H_y$ the same order of magnitude (key advantage for PML formulation):

$$
\tilde{E}_x^{n+\frac{1}{2}}[k] = \tilde{E}_x^{n-\frac{1}{2}}[k] - \frac{1}{2}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.6a}
$$
$$
H_y^{n+1}[k+\tfrac{1}{2}] = H_y^n[k+\tfrac{1}{2}] - \frac{1}{2}\left(\tilde{E}_x^{n+\frac{1}{2}}[k+1] - \tilde{E}_x^{n+\frac{1}{2}}[k]\right) \tag{1.6b}
$$

The factor $\frac{\Delta t}{\varepsilon_0\mu_0\Delta x} = \frac{1}{2}$ follows from choosing $\Delta t = \Delta x/(2c_0)$.
系数 $\frac{1}{2}$ 来自选择 $\Delta t = \Delta x/(2c_0)$ 的 CFL 条件。

### Python Implementation (1D FDTD core loop) | Python 实现（1D FDTD 核心循环）

```python
# ex[k] = ex[k] + 0.5 * (hy[k-1] - hy[k])   # Update E field | 更新电场
# hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])   # Update H field | 更新磁场
```

Key points | 关键要点：
- E and H updates use **separate loops** (interleaved in space and time)
  电、磁场更新使用**不同的循环**（空间和时间上交错）
- **Hard source**: override `ex[kc] = pulse` after E-update（**硬源**：在 E 更新后强制赋值）
- $E_x$ is positive in both propagation directions; $H_y$ changes sign with direction
- Without absorbing boundaries, the pulse reflects at grid edges
  无吸收边界时，脉冲会在网格边缘反射

---

## 1.2 Stability and the FDTD Method | 稳定性与 FDTD 方法

### Courant–Friedrichs–Lewy (CFL) Stability Condition | CFL 稳定条件

An EM wave in free space cannot travel faster than $c_0$. To propagate one cell requires $\Delta t \geq \Delta x / c_0$.
自由空间中电磁波速度不能超过 $c_0$，传播一个网格单元需要 $\Delta t \geq \Delta x / c_0$。

General dimension-`n` CFL condition | n 维 CFL 条件：

$$
\Delta t = \frac{\Delta x}{n \, c_0} \tag{1.10}
$$

For 1D: $\Delta t = \Delta x / c_0$; the book uses $\Delta t = \Delta x/(2c_0)$ to avoid square roots.
书中使用 $\Delta t = \Delta x/(2c_0)$ 以简化计算。

**If coefficient 0.5 is changed to 1.0 → instability (field grows without bound).**
**如果将系数 0.5 改为 1.0 → 不稳定（场无界增长）。**
**If changed to 0.25 → stable but overly dissipative.**
**如果改为 0.25 → 稳定但耗散过大。**

---

## 1.3 The Absorbing Boundary Condition (ABC) in One Dimension | 一维吸收边界条件

### Concept | 概念

At the grid edge, FDTD needs $H$ values on one side that don't exist. Absorbing boundary conditions prevent outgoing waves from reflecting back into the problem space.
在网格边缘，FDTD 需要的 $H$ 值不存在。吸收边界条件防止出射波反射回问题空间。

### First-Order ABC (Mur, 1981) | 一阶吸收边界条件

For a forward-traveling wave: $\quad \frac{\partial E}{\partial t} + c_0 \frac{\partial E}{\partial z} = 0$
前行波满足上述单向波动方程。

In normalized units ($c_0=1$, $\Delta x = \Delta t = 1$): $E[0]^{n+1} = E[1]^n$ (left boundary).
归一化单位下，$E[0]^{n+1} = E[1]^n$ 实现了左边界吸收。

```python
# Left boundary (k=0)
ex[0] = ex_prev_left   # stored from previous step
ex_prev_left = ex[1]   # update stored value

# Right boundary (k=ke-1)
ex[ke-1] = ex_prev_right
ex_prev_right = ex[ke-2]
```

---

## 1.4 Propagation in a Dielectric Medium | 在介质中的传播

### Formulation with Permittivity $\varepsilon_r$ | 考虑介电常数 $\varepsilon_r$ 的公式

When $\varepsilon = \varepsilon_r \varepsilon_0$:
当 $\varepsilon = \varepsilon_r \varepsilon_0$：

$$
E_x^{n+\frac{1}{2}}[k] = E_x^{n-\frac{1}{2}}[k] - \frac{1}{2\varepsilon_r}\left(H_y^n[k+\tfrac{1}{2}] - H_y^n[k-\tfrac{1}{2}]\right) \tag{1.17}
$$

Python: `ex[k] = ex[k] + (1/eps_r) * (hy[k-1] - hy[k])`

### Physical Consequences | 物理结果

| Property | Value |
|---|---|
| Wave speed in dielectric | $c = c_0 / \sqrt{\varepsilon_r}$ |
| Wavelength in dielectric | $\lambda = \lambda_0 / \sqrt{\varepsilon_r}$ |
| Intrinsic impedance | $\eta = \eta_0 / \sqrt{\varepsilon_r}$ |

介质中波速减慢、波长缩短、本征阻抗降低。

---

## 1.5 Simulating Different Sources | 模拟不同激励源

### Hard Source (Explicit Field Value) | 硬源（直接赋值）

```python
ex[kc] = pulse  # overrides computed value | 覆盖计算值
```
Disadvantage: introduces spurious reflections if not smoothly ramped.
缺点：如果阶跃不平滑会引入虚假反射。

### Soft Source (Additive) | 软源（叠加）

```python
ex[kc] += pulse  # adds to existing field | 叠加到现有场
```
Less reflection, more physical. 反射更小，更符合物理。

### Magnetic Source (Hy injection) | 磁源（H 场注入）

```python
hy[kc-1] = -hy[kc]   # dipole-like magnetic source | 类似偶极磁源
```

---

## 1.6 Determining Cell Size | 确定网格尺寸

### Resolution Requirement | 分辨率要求

To accurately model a wave, $\Delta x$ must be small enough to resolve the shortest wavelength:
为精确模拟波，空间步长 $\Delta x$ 必须足够小以分辨最短波长：

$$
\Delta x \leq \frac{\lambda_{\min}}{10} \quad \text{(rule of thumb | 经验法则)}
$$

### Time Step Selection | 时间步长选择

$$
\Delta t = \frac{\Delta x}{2c_0}
$$

### Normalized Units Summary | 归一化单位总结

| Quantity | Normalized Value |
|---|---|
| $c_0$ | 1 |
| $\varepsilon_0$ | 1 |
| $\mu_0$ | 1 |
| $\Delta x$ | 1 |
| $\Delta t$ | 1 |

归一化后所有物理常数均为 1，简化计算。

---

## 1.7 Propagation in a Lossy Dielectric Medium | 在有耗介质中的传播

### Maxwell's Equations with Conductivity | 含电导率的麦克斯韦方程

$$
\frac{\partial E_x}{\partial t} = \frac{1}{\varepsilon} \frac{\partial H_y}{\partial z} - \frac{\sigma}{\varepsilon} E_x \tag{1.18}
$$

The conductivity term causes **exponential attenuation**.
电导率项导致**指数衰减**。

### FDTD Update Coefficients | FDTD 更新系数

`eaf = dt * sigma / (2 * eps_r * eps0)`

$$
\text{ca}[k] = \frac{1 - \text{eaf}}{1 + \text{eaf}} \tag{1.23b}
$$
$$
\text{cb}[k] = \frac{0.5}{\varepsilon_r \cdot (1 + \text{eaf})} \tag{1.23c}
$$

Update: `ex[k] = ca[k] * ex[k] + cb[k] * (hy[k-1] - hy[k])`

### Physical Interpretation | 物理解释

| Parameter | Meaning | 含义 |
|---|---|---|
| $\sigma$ | Conductivity (S/m) | 电导率 |
| Loss tangent | $\tan\delta = \sigma / (\omega \varepsilon)$ | 损耗角正切 |
| Penetration depth | $\delta_p = \sqrt{2 / (\omega \mu \sigma)}$ | 穿透深度 |

### PEC (Perfect Electric Conductor) Approximation | PEC 近似

For metal: set $\sigma = 10^6$ (very large). This makes `ca ≈ -1`, essentially zeroing the E field inside the conductor.
金属中设置 $\sigma = 10^6$，使 `ca ≈ -1`，电场在导体内近乎为零。

---

## 1.A Appendix — Reflection and Transmission at Dielectric Interfaces | 附录：介质界面反射与传输

### Reflection and Transmission Coefficients | 反射系数与传输系数

For a plane wave incident from medium 1 onto medium 2:
平面波从介质 1 入射到介质 2：

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1} = \frac{\varepsilon_1^* - \varepsilon_2^*}{\varepsilon_1^* + \varepsilon_2^*} \tag{1.A.4}
$$
$$
\tau = \frac{2\eta_2}{\eta_2 + \eta_1} = \frac{2\varepsilon_1^*}{\varepsilon_1^* + \varepsilon_2^*} \tag{1.A.5}
$$

### Complex Permittivity | 复介电常数

$$
\varepsilon_r^* = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0}
$$

### Wave Propagation in Lossy Medium | 有耗介质中的波传播

$$
E_x(z) = E_0 e^{-\alpha z} e^{-j\beta z}
$$

where $k = \omega\sqrt{\mu\varepsilon} = \alpha + j\beta$ and:

$$
\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} - 1\right]^{1/2}
$$
$$
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1 + \left(\frac{\sigma}{\omega\varepsilon}\right)^2} + 1\right]^{1/2}
$$

$\alpha$ 为衰减常数，$\beta$ 为相位常数。

---

## Python Programs Summary | Python 程序总结

| Program | Description | Key Technique | 关键技术 |
|---|---|---|---|
| `fd1d_1_1.py` | Free-space 1D FDTD, Gaussian pulse | Basic E/H interleaved updates | 基本 E/H 交错更新 |
| `fd1d_1_2.py` | Free-space with first-order ABC | Mur ABC at both boundaries | Mur 吸收边界 |
| `fd1d_1_3.py` | Dielectric medium ($\varepsilon_r$) | Scaled E-update coefficient | 缩放 E 更新系数 |
| `fd1d_1_4.py` | Hard source sinusoidal in lossy medium | ca/cb loss coefficients | ca/cb 损耗系数 |
| `fd1d_1_5.py` | Sinusoid hitting lossy dielectric slab | Domain-specific loss parameters | 区域损耗参数 |

## Key Equations Master Index | 关键方程索引

| Eq. | Description | 说明 |
|---|---|---|
| (1.2a,b) | 1D Maxwell for $E_x$, $H_y$ in $z$ | 一维麦克斯韦方程 |
| (1.4a,b) | FDTD discretized (pre-normalization) | FDTD 离散化方程 |
| (1.5) | Normalization: $\tilde{E} = \sqrt{\varepsilon_0/\mu_0}\;E$ | 归一化 |
| (1.6a,b) | Normalized FDTD update | 归一化 FDTD 更新 |
| (1.10) | CFL: $\Delta t = \Delta x/(n c_0)$ | CFL 稳定条件 |
| (1.17) | Dielectric E-field update | 介质电场更新 |
| (1.18) | Maxwell with conductivity $\sigma$ | 含电导率的麦克斯韦方程 |
| (1.23a–c) | Loss coefficients ca, cb | 损耗系数 ca, cb |
| (1.A.4–5) | Reflection/transmission at interface | 界面反射/传输系数 |

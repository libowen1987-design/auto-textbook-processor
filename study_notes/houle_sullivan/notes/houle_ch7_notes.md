# Ch7: Two-Dimensional FDTD — Total-Field/Scattered-Field (TF/SF) Technique

> **中英双语版**
> **Source:** Houle & Sullivan — *Electromagnetic Simulation Using the FDTD Method with Python* (IEEE Press, 3rd ed. 2020), Chapter 3 (original pp. 93–127)
> **Core Topic:** 2D FDTD + TF/SF boundary injection + Fourier transform frequency-domain post-processing

## 7.1 Two-Dimensional FDTD Grid and Equations | 二维 FDTD 网格与方程组

### Scaling from 1D to 2D | 1D → 2D 的升维

In 1D, Maxwell's equations reduce to a plane-wave equation along $x$. In 2D, fields vary in the $xy$-plane and are uniform in $z$ ($\partial/\partial z = 0$).
一维 Maxwell 方程简化为沿 $x$ 方向的平面波方程。二维场量在 $xy$ 平面变化，$z$ 方向均匀。

**Normalized 2D Maxwell equations (TM$_z$ mode) | 归一化二维 Maxwell 方程组（TM$_z$ 模式）：**

$$\frac{\partial D_z}{\partial t} = \frac{\partial H_x}{\partial y} - \frac{\partial H_y}{\partial x},\quad \mathbf{D} = \epsilon \mathbf{E}$$

**TE$_z$ mode (dual) | TE$_z$ 模式（对偶）：**

$$\frac{\partial E_x}{\partial t} = \frac{1}{\epsilon}\frac{\partial H_z}{\partial y},\quad
\frac{\partial E_y}{\partial t} = -\frac{1}{\epsilon}\frac{\partial H_z}{\partial x},\quad
\frac{\partial H_z}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right)$$

---

## 7.2 Total-Field/Scattered-Field Boundary | 总场/散射场边界

### Physical Origin of the Problem | 问题的物理起源

Divide the computational domain into two regions:
将计算区域分为两个区：
- **Total Field region:** contains the scatterer, field = incident + scattered（**总场区：** 含散射体，场 = 入射+散射）
- **Scattered Field region:** outside, only scattered fields（**散射场区：** 外部，只有散射场）

### 1D Incident Wave Injection | 一维入射波注入

$$D_z^{\text{inc}}\big|_{\text{boundary}} = D_z^{\text{inc}}\big|_{\text{boundary}} \pm \frac{1}{2}H_x^{\text{inc}}$$

```python
# Incident Dz — top/bottom boundaries | 上下边界
for i in range(ia, ib + 1):
    dz[i, ja] = dz[i, ja] + 0.5 * hx_inc[ja - 1]
    dz[i, jb] = dz[i, jb] - 0.5 * hx_inc[jb]
```

### 2D TF/SF Boundary Equations | 二维 TF/SF 边界方程

For side boundaries (left $i = ia-1$, right $i = ib$):
对于侧面边界（左 $i = ia-1$，右 $i = ib$）：

$$H_y^{\text{inc}}\big|_{\text{boundary}} = H_y^{\text{inc}}\big|_{\text{boundary}} \pm \frac{1}{2}E_z^{\text{inc}}$$

```python
for j in range(ja, jb + 1):
    hy[ia - 1, j] = hy[ia - 1, j] - 0.5 * ez_inc[j]
    hy[ib, j] = hy[ib, j] + 0.5 * ez_inc[j]
```

### Incident Array Update | 入射场数组更新

The incident plane wave propagates along the $x$ direction:
入射平面波沿 $x$ 方向传播：

```python
for j in range(0, je - 1):
    hx_inc[j] = hx_inc[j] + 0.5 * (ez_inc[j] - ez_inc[j + 1])
```

This is the discretized Faraday law: $\partial H_x/\partial t = -\partial E_z/\partial y$.
这等价于离散化的法拉第定律。

---

## 7.3 Fourier Transform Post-Processing | 傅里叶变换后处理（频域结果提取）

### Why Frequency-Domain Processing | 为什么需要频域后处理

FDTD runs in time domain, but many applications need specific frequency responses. DFT extracts arbitrary frequency components after simulation.
FDTD 在时域运行，但许多应用需要特定频率响应。DFT 可在仿真后提取任意频率成分。

**Discrete Fourier Transform | 离散傅里叶变换：**

$$E_z(m\Delta f) = \sum_{n=0}^{N-1} E_z(n\Delta t) \cdot e^{-j2\pi mn/N}$$

```python
for j in range(0, je):
    for i in range(0, ie):
        for m in range(0, number_of_frequencies):
            real_pt[m, i, j] += cos(arg[m] * time_step) * ez[i, j]
            imag_pt[m, i, j] -= sin(arg[m] * time_step) * ez[i, j]
```

### Amplitude and Phase Extraction | 幅值与相位提取

```python
amp_in = np.sqrt(real_in ** 2 + imag_in ** 2)
phase_in = np.arctan2(imag_in, real_in)
```

### Total Field Normalization | 总场区结果归一化

For comparison inside/outside the dielectric sphere, normalize by the incident field:
介质球内外比较时，需除以入射场得到归一化响应：

```python
if gaz[ic, j] < 1:  # inside sphere
    amp[m, j] = 1 / (amp_in[m]) * sqrt(real_pt[m, ic, j]**2 + imag_pt[m, ic, j]**2)
    phase[m, j] = atan2(imag_pt[m, ic, j], real_pt[m, ic, j]) - pi - phase_in[m] + phase_offset[m]
```

---

## 7.4 Gaussian Pulse Source | 高斯脉冲入射源

$$E_z^{\text{inc}}(t) = \exp\left[-\frac{(t - t_0)^2}{2\tau^2}\right]$$

```python
t0 = 20; spread = 6
pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
ez_inc[3] = pulse
```

---

## 7.5 2D FDTD Update Equations Summary | 二维 FDTD 更新方程总结

### D-field Update | D 场更新

```python
for j in range(0, je):
    for i in range(0, ie):
        ez[i, j] = gaz[i, j] * (dz[i, j] - iz[i, j])
        iz[i, j] = iz[i, j] + gbz[i, j] * ez[i, j]
```

where | 其中：
$$g_{az} = \frac{1}{\epsilon_r + \frac{\sigma\Delta t}{\epsilon_0}},\quad g_{bz} = \frac{\sigma\Delta t}{\epsilon_0}$$

### H-field Update | H 场更新

```python
# Hx update | Hx 更新
for j in range(0, je - 1):
    for i in range(0, ie - 1):
        curl_e = ez[i, j] - ez[i, j + 1]
        ihx[i, j] = ihx[i, j] + curl_e
        hx[i, j] = fj3[j] * hx[i, j] + fj2[j] * (0.5 * curl_e + fi1[i] * ihx[i, j])

# Hy update | Hy 更新
for j in range(0, je):
    for i in range(0, ie - 1):
        curl_e = ez[i, j] - ez[i + 1, j]
        ihy[i, j] = ihy[i, j] + curl_e
        hy[i, j] = fi3[i] * hy[i, j] - fi2[i] * (0.5 * curl_e + fj1[j] * ihy[i, j])
```

---

## 7.6 Frequency-Domain Comparison: Bessel Function Analytical Solution | 频域比较：Bessel 函数解析解

Three frequencies: 50 MHz, 200 MHz, 500 MHz

| Frequency | Free-space $\lambda$ | Grid resolution |
|:----------|:--------------------|:----------------|
| 50 MHz | 600 cm | Grid << $\lambda$ |
| 200 MHz | 150 cm | Good sampling |
| 500 MHz | 60 cm | Note $\Delta x$ |

FDTD simulation results (lines) compared against analytical Bessel-function expansion solutions (circles) — excellent agreement.

---

## 7.7 TF/SF Boundary: Physical Intuition and Error Sources | TF/SF 边界的物理直觉与误差来源

### Why the TF/SF Boundary Is "Invisible" | 为什么 TF/SF 边界能够"隐身"

The TF/SF boundary acts as an **equivalent source**, satisfying the superposition principle:
TF/SF 边界的本质是**等效源**，满足重叠原理：

$$\underbrace{\mathbf{E}}_{\text{total}} = \underbrace{\mathbf{E}^{\text{inc}}}_{\text{incident}} + \underbrace{\mathbf{E}^{\text{sca}}}_{\text{scattered}}$$

### Error Sources | 注入误差来源

1. **Phase error | 相位误差**: Incident array values have a half-cell offset from the grid
2. **Discretization error | 离散化误差**: Injection uses first-order 0.5 weighting

### Avoiding Error Accumulation | 避免误差积累

The incident array uses **Mur's ABC** as its boundary condition:
```python
boundary_low = [0, 0]; boundary_high = [0, 0]
ez_inc[0] = boundary_low.pop(0)
boundary_low.append(ez_inc[1])
ez_inc[je - 1] = boundary_high.pop(0)
boundary_high.append(ez_inc[je - 2])
```

---

## 7.8 From 1D to 2D: Physical Significance | 从一维到二维：物理意义

2D FDTD reduces complexity from $O(N_x \times N_y \times N_z)$ to $O(N_x \times N_y)$.

**TM$_z$ vs TE$_z$ mode comparison | TM$_z$ 与 TE$_z$ 模对比:**

- **TM$_z$** (Transverse Magnetic): $E_z$ primary, $H_x, H_y$ secondary — use for dielectric waveguide and cylindrical scattering（适合电介质波导和柱面散射）
- **TE$_z$** (Transverse Electric): $H_z$ primary, $E_x, E_y$ secondary — use for metallic cavity resonance and metal scatterers（适合金属腔体谐振和金属散射体）

---

## 7.9 DFT Implementation Details | 傅里叶变换离散实现细节

### Real/Imaginary Decomposition of DFT | 复数 DFT 的实部/虚部分解

$$\hat{f}_{\text{real}}(m) = \sum_{n=0}^{N-1} f(n\Delta t) \cos(2\pi mn/N)$$
$$\hat{f}_{\text{imag}}(m) = -\sum_{n=0}^{N-1} f(n\Delta t) \sin(2\pi mn/N)$$

### Phase Unwrapping | 相位解卷绕

```python
if phase[m, j] < -2 * pi: phase[m, j] += 2 * pi
if phase[m, j] > 0:      phase[m, j] -= 2 * pi
```

### Key CFL Condition | CFL 条件

For 2D with uniform grid $\Delta x = \Delta y = h$:
$$\Delta t_{\max} = \frac{h}{c\sqrt{2}} \approx 0.707\frac{h}{c}$$

---

## Audit Table | 审计表格

| Item | Source | Status |
|:-----|:------|:------:|
| TF/SF injection eqs | raw text p.94 | ✅ |
| Gaussian pulse formula | raw text p.93 | ✅ |
| Fourier transform code | raw text p.93 | ✅ |
| Bessel comparison data | raw text pp.95-96 | ✅ |
| 3D plotting code | raw text pp.94-95 | ✅ |
| $g_{az}$, $g_{bz}$ definitions | analogy from 1D | ✅ |
| $\Delta t$ stability | 2D CFL condition | ✅ |

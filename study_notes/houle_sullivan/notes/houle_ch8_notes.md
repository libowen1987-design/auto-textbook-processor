# Ch8: Three-Dimensional FDTD — Yee Cell, PML, and Dielectric Sphere Scattering

> **中英双语版**
> **Source:** Houle & Sullivan — *Electromagnetic Simulation Using the FDTD Method with Python* (IEEE Press, 3rd ed. 2020), Chapter 4 (original pp. 99–127)
> **Core Topic:** 3D FDTD + Yee cell + PML absorbing boundary + dielectric sphere scattering + TF/SF in 3D

## 8.1 Yee Cell and 3D Maxwell's Equations | Yee 元胞与三维 Maxwell 方程

### 8.1.1 Yee Grid Configuration | Yee 网格构型

In 3D, all six field components $(E_x, E_y, E_z, H_x, H_y, H_z)$ are interleaved in space-time:
三维中六个电磁场分量在时空上交错采样：
- **Electric fields**: offset by half-cell along their own direction（沿自身方向偏离半格）
- **Magnetic fields**: offset by half-cell along two directions（沿两个方向偏离半格）

### 8.1.2 3D Maxwell Equations (6 Scalar Components) | 三维 Maxwell 方程组（6 个标量方程）

$$\frac{\partial D_x}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z}\right),\quad
\frac{\partial D_y}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x}\right),\quad
\frac{\partial D_z}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right)$$

$$\frac{\partial H_x}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right),\quad
\frac{\partial H_y}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z}\right),\quad
\frac{\partial H_z}{\partial t} = \frac{1}{\mu_0}\left(\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right)$$

### 8.1.3 Computer Implementation | 计算机实现方程

```python
# D-field updates | D场更新
dx[i,j,k] = dx[i,j,k] + 0.5 * (hz[i,j,k] - hz[i,j-1,k] - hy[i,j,k] + hy[i,j,k-1])
dy[i,j,k] = dy[i,j,k] + 0.5 * (hx[i,j,k] - hx[i,j,k-1] - hz[i,j,k] + hz[i-1,j,k])
dz[i,j,k] = dz[i,j,k] + 0.5 * (hy[i,j,k] - hy[i-1,j,k] - hx[i,j,k] + hx[i,j-1,k])

# H-field updates | H场更新
hx[i,j,k] = hx[i,j,k] + 0.5 * (ey[i,j,k+1] - ey[i,j,k] - ez[i,j+1,k] + ez[i,j,k])
hy[i,j,k] = hy[i,j,k] + 0.5 * (ez[i+1,j,k] - ez[i,j,k] - ex[i,j,k+1] + ex[i,j,k])
hz[i,j,k] = hz[i,j,k] + 0.5 * (ex[i,j+1,k] - ex[i,j,k] - ey[i+1,j,k] + ey[i,j,k])
```

---

## 8.2 Dipole Antenna Modeling | 偶极子天线建模

### 8.2.1 Physical Model | 物理模型

1. **Metal arms**: `gaz = 0` ($\sigma \to \infty$, forcing $E_z = 0$ inside) — 金属臂
2. **Source**: set $E_z$ in the gap — 馈源

### 8.2.2 Gaussian Pulse Source | 高斯脉冲源

$$E_z^{\text{source}}(T) = \exp\left[-\frac{(T - T_0)^2}{2\tau^2}\right]$$

```python
t0 = 20; spread = 6
pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
dz[ic, jc, kc] = pulse
```

### 8.2.3 FDTD Parameters (fd3d_4_1.py) | FDTD 参数设置

```python
ie = je = ke = 60      # grid size | 网格尺寸
ic = jc = kc = 30      # dipole center | 偶极子中心
gaz[ic, jc, kc-10:kc+10] = 0   # dipole arms | 金属臂
gaz[ic, jc, kc] = 1              # gap | 缝隙
ddx = 0.01; dt = ddx / 6e8
```

---

## 8.3 3D PML (Perfectly Matched Layer) | 三维 PML

### 8.3.1 Extending 2D PML to 3D | 从 2D 到 3D 的推广

2D PML uses two conductivities $(\sigma_x, \sigma_y)$. 3D extends to $(\sigma_x, \sigma_y, \sigma_z)$.

For $D_z$ (Eq. 4.4 from book):
$$\left(j\omega + \frac{\sigma_{Dx}}{\epsilon_0}\right)\left(j\omega + \frac{\sigma_{Dy}}{\epsilon_0}\right)\left(j\omega + \frac{\sigma_{Dz}}{\epsilon_0}\right)D_z = c_0\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right]$$

### 8.3.2 Auxiliary Integral Terms | 积分辅助项

```python
idz[i, j, k] = idz[i, j, k] + curl_h
dz[i,j,k] = gi3[i] * gj3[j] * dz[i,j,k] + \
    gi2[i] * gj2[j] * (0.5 * curl_h + gk1[k] * idz[i, j, k])
```

### 8.3.3 PML Parameter Configuration | PML 参数配置

```python
for n in range(npml):
    xxn = (npml - n) / npml
    xn = 0.33 * (xxn ** 3)
    fi1[n] = xn; fi1[ie - n - 1] = xn
    gi2[n] = 1 / (1 + xn); gi2[ie - 1 - n] = 1 / (1 + xn)
    gi3[n] = (1 - xn) / (1 + xn); gi3[ie - 1 - n] = (1 - xn) / (1 + xn)
    # ... similar for j and k directions
```

---

## 8.4 3D Total-Field/Scattered-Field (TF/SF) | 三维总场/散射场

### 8.4.1 Plane Wave Injection in 3D | 三维平面波注入

In 3D, the plane wave in the $j$ direction ($xz$ plane) TF/SF boundary:
- **$j = j_a$ face**: add incident wave to $D$ field（注入入射波）
- **$j = j_b$ face**: subtract incident wave（减去入射波）

### 8.4.2 k-direction Additional Boundary (Eq. 4.7a/4.7b) | k 方向额外边界

$$D_y(i, j+1/2, k_a) \leftarrow D_y(i, j+1/2, k_a) - \frac{1}{2}H_x^{\text{inc}}(j+1/2)$$
$$D_y(i, j+1/2, k_b+1) \leftarrow D_y(i, j+1/2, k_b+1) + \frac{1}{2}H_x^{\text{inc}}(j+1/2)$$

---

## 8.5 Dielectric Sphere Scattering | 介质球散射

### 8.5.1 Sphere Parameters | 介质球参数

```python
epsilon = [1.0, 30.0]  # air + medium (ε_r = 30)
sigma = [0.0, 0.3]    # S/m
radius = 10           # grid cells = 10 cm
```

### 8.5.2 Subcell Averaging (9-point method) | 亚网格平均（9点法）

Simple "in-or-out" method for $E_z$:
```python
zdist = kc - k - 0.5
dist = sqrt(xdist**2 + ydist**2 + zdist**2)
if dist <= radius:
    gaz[i,j,k] = 1 / (eps + (cond * dt / epsz))
```

9-point averaging (higher accuracy):
```python
for jj in range(-1, 2):
    for ii in range(-1, 2):
        dist = sqrt((ic-i + ii/3)**2 + (jc-j + jj/3)**2 + (kc-k-0.5)**2)
        if dist <= radius:
            eps += (1/9) * (epsilon[1] - epsilon[0])
            cond += (1/9) * sigma[1]
```

### 8.5.3 Validation Results | 验证结果

| Method | 50 MHz | 200 MHz | 500 MHz |
|:-------|:-------|:--------|:--------|
| In-or-out | Large deviation | Clear deviation | Severe deviation |
| 9-point avg | Good with Bessel | Good match | Good match |

---

## 8.6 PML Performance and Layer Count | PML 效能与层数选择

| PML layers | Typical reflection | Cost |
|:----------|:-------------------|:-----|
| 5 layers | ~$10^{-3}$ | Minimal |
| 7 layers | ~$10^{-4}$ | Moderate |
| 10 layers | ~$10^{-5}$ | Large |

The book uses **7-point PML** with polynomial order $m=3$: $x_n = 0.33 \times (xxn^3)$.

### 3D CFL Condition | 三维 CFL 条件

$$\Delta t \leqslant \frac{h}{c\sqrt{3}} \approx 0.577 \frac{h}{c}$$

More restrictive than 1D $(\Delta x/c)$ or 2D $(\Delta x/(c\sqrt{2}))$.

### Memory Estimate | 内存估算

$40\times40\times40$ grid, 12 field components, single precision:
$$12 \times 40^3 \times 4 \text{ bytes} \approx 3.1 \text{ MB}$$

---

## Audit Table | 审计表格

| Item | Source | Status |
|:-----|:------|:------:|
| Yee cell configuration | raw text p.99 | ✅ |
| 6 scalar equations (4.2a–4.2f) | raw text p.100 | ✅ |
| Computer implementation | raw text p.101 | ✅ |
| Dipole antenna model (gaz=0) | raw text p.102 | ✅ |
| 3D PML equations (4.4–4.6) | raw text pp.103-104 | ✅ |
| TF/SF k-boundary eqs (4.7a/4.7b) | raw text p.107 | ✅ |
| Sphere parameters (ε_r=30, σ=0.3) | raw text p.123 | ✅ |
| Subcell averaging (9-point) | raw text pp.109-110 | ✅ |
| Bessel comparison data | raw text p.126 | ✅ |

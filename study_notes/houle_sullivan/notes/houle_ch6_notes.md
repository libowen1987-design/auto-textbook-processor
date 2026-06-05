---
title: "Three-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 6
---

# Chapter 6 — Three-Dimensional Simulation

> **中英双语版**

## 6.1 Free-Space Simulation: The Yee Cell in 3D | 自由空间仿真：三维 Yee 网格

### The Yee Lattice | Yee 网格结构

The 3D Yee cell interleaves E and H components around a cubic cell:
三维 Yee 单元在立方体周围交错排列 E 和 H 分量：
- $E_x$ at $(i+1/2, j, k)$, $E_y$ at $(i, j+1/2, k)$, $E_z$ at $(i, j, k+1/2)$
- $H_x$ at $(i, j+1/2, k+1/2)$, $H_y$ at $(i+1/2, j, k+1/2)$, $H_z$ at $(i+1/2, j+1/2, k)$

### Full Maxwell's Equations (6 Scalar Components) | 完整麦克斯韦方程（6 个标量分量）

Starting from the normalized curl equations:
从归一化旋度方程出发：

$$
\frac{\partial D_x}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z}\right) \tag{6.1a}
$$
$$
\frac{\partial D_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_x}{\partial z} - \frac{\partial H_z}{\partial x}\right) \tag{6.1b}
$$
$$
\frac{\partial D_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{6.1c}
$$
$$
\frac{\partial H_x}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right) \tag{6.1d}
$$
$$
\frac{\partial H_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_z}{\partial x} - \frac{\partial E_x}{\partial z}\right) \tag{6.1e}
$$
$$
\frac{\partial H_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial E_x}{\partial y} - \frac{\partial E_y}{\partial x}\right) \tag{6.1f}
$$

### FDTD Update Equations (3D) | 三维 FDTD 更新方程

Using $\Delta t = \Delta x / (2c_0)$ and $\Delta x = \Delta y = \Delta z$:

```python
# D-field updates (6.2a-c) | D场更新
dx[i,j,k] = dx[i,j,k] + 0.5 * (
    hz[i,j,k] - hz[i,j-1,k] - hy[i,j,k] + hy[i,j,k-1])
dy[i,j,k] = dy[i,j,k] + 0.5 * (
    hx[i,j,k] - hx[i,j,k-1] - hz[i,j,k] + hz[i-1,j,k])
dz[i,j,k] = dz[i,j,k] + 0.5 * (
    hy[i,j,k] - hy[i-1,j,k] - hx[i,j,k] + hx[i,j-1,k])

# E-field from D (simple dielectric) | E场从D得到
ex[i,j,k] = gax[i,j,k] * dx[i,j,k]
ey[i,j,k] = gay[i,j,k] * dy[i,j,k]
ez[i,j,k] = gaz[i,j,k] * dz[i,j,k]

# H-field updates (6.2d-f) | H场更新
hx[i,j,k] = hx[i,j,k] + 0.5 * (
    ey[i,j,k+1] - ey[i,j,k] - ez[i,j+1,k] + ez[i,j,k])
hy[i,j,k] = hy[i,j,k] + 0.5 * (
    ez[i+1,j,k] - ez[i,j,k] - ex[i,j,k+1] + ex[i,j,k])
hz[i,j,k] = hz[i,j,k] + 0.5 * (
    ex[i,j+1,k] - ex[i,j,k] - ey[i+1,j,k] + ey[i,j,k])
```

> **Indexing pattern:** Each component uses neighbors offset by 1 in its own direction (positive derivative) and by 1 in the two perpendicular directions (negative derivatives). This mirrors the curl operator structure.
> **索引模式：** 每个分量用自身方向偏移 +1（正导数）和两个垂直方向偏移 +1（负导数）的邻居值，体现了旋度算符结构。

### Dipole Antenna Source | 偶极天线源

In 3D free-space with a point source, $E$ attenuates as $1/r$, making it hard to visualize. Instead, a **dipole antenna** is used:
三维自由空间中点源的 $E$ 按 $1/r$ 衰减，难以可视化。改用**偶极天线**：

1. Metal arms: set `gaz=0` in cells corresponding to metal → $E_z = 0$（金属臂：设置 `gaz=0`）
2. Gap: specify $E_z$ in the gap cell directly (Gaussian pulse)（间隙：直接设置 $E_z$ 为高斯脉冲）

> **Why dipole?** A dipole approximates the far-field radiation pattern of real antennas.
> **为什么用偶极子？** 偶极子近似真实天线的远场辐射方向图。

---

## 6.2 The PML in Three Dimensions | 三维 PML

### Extending 2D PML to 3D | 将二维 PML 扩展到三维

The 3D PML adds the z-direction to the anisotropic conductivity profile:
三维 PML 将 z 方向加入各向异性电导率分布：

$$
j\omega\left(1 + \frac{\sigma_{D,x}}{j\omega\varepsilon_0}\right)\left(1 + \frac{\sigma_{D,y}}{j\omega\varepsilon_0}\right)\left(1 + \frac{\sigma_{D,z}}{j\omega\varepsilon_0}\right)^{-1}D_z = c_0\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{6.3}
$$

### D-Field Update with 3D PML | 三维 PML D 场更新

```python
curl_h = (hy[i,j,k] - hy[i-1,j,k] - hx[i,j,k] + hx[i,j-1,k])
idz[i,j,k] = idz[i,j,k] + curl_h
dz[i,j,k] = (gi3[i] * gj3[j] * dz[i,j,k] 
           + gi2[i] * gj2[j] * (0.5 * curl_h + gk1[k] * idz[i,j,k]))
```

Where `idz` accumulates the "history integral" in the z-direction.
其中 `idz` 在 z 方向累积"历史积分"。

### Physical Interpretation | 物理解释

The 3D PML has three sets of g-parameters (x, y, z) and three auxiliary integration fields: `idx`, `idy`, `idz`. Each direction attenuates waves exiting through that face.
三维 PML 有三组 g 参数和三个辅助积分场。每个方向衰减从该面出射的波。

> **Memory consideration:** In 3D, idx, idy, idz are **3D arrays** — significant additional memory for large problems.
> **内存考虑：** 三维中 idx、idy、idz 是**三维数组**——大问题中内存开销显著。

---

## 6.3 Total-Field/Scattered-Field Formulation in 3D | 三维总场/散射场公式

### Plane Wave Generation in 3D | 三维平面波生成

Similar to 2D, but now the TF/SF boundary is a rectangular box in the XZ plane at $j = j_a$ and $j = j_b$.
与二维类似，但 TF/SF 边界是 XZ 平面中的矩形框。

The plane wave propagates in the y-direction — only $E_z$ and $H_x$ are nonzero (in free space). The incident buffer is 1D: `ez_inc[j]`, `hx_inc[j]`.
平面波沿 y 方向传播，只有 $E_z$ 和 $H_x$ 非零（自由空间中）。入射缓冲是一维数组。

### TF/SF Boundary Corrections (3D) | 三维 TF/SF 边界修正

At the boundary, corrections to D and H fields are applied using the incident buffer values. The corrections for $D_y$ and $H_x$ at the y-boundaries ensure the incident wave is properly added to the total field region.
在边界处，使用入射缓冲值对 D 和 H 场进行修正。y 边界上 $D_y$ 和 $H_x$ 的修正确保入射波正确添加到总场区。

> **Key insight:** Only the scattered fields leave through the PML — the incident wave stays inside the TF region.
> **关键洞察：** 只有散射场通过 PML 离开——入射波保持在总场区内。

---

## Code Reference | 代码参考

### Basic 3D FDTD (`fd3d_4_1.py`)

```python
import numpy as np
from numba import jit

ie = 40; je = 40; ke = 40
dx = np.zeros((ie, je, ke))
dy = np.zeros((ie, je, ke))
dz = np.zeros((ie, je, ke))
ex = np.zeros((ie, je, ke))
ey = np.zeros((ie, je, ke))
ez = np.zeros((ie, je, ke))
hx = np.zeros((ie, je, ke))
hy = np.zeros((ie, je, ke))
hz = np.zeros((ie, je, ke))
gax = np.ones((ie, je, ke))
gay = np.ones((ie, je, ke))
gaz = np.ones((ie, je, ke))

# Dipole: metal arms in z-direction at center
gaz[ic, jc, kc-2:kc+3] = 0   # gap is at kc

nsteps = 100
for time_step in range(1, nsteps + 1):
    # D-field updates (triple nested loop)
    for k in range(1, ke):
        for j in range(1, je):
            for i in range(1, ie):
                dx[i,j,k] += 0.5 * (hz[i,j,k] - hz[i,j-1,k] 
                                    - hy[i,j,k] + hy[i,j,k-1])
                dy[i,j,k] += 0.5 * (hx[i,j,k] - hx[i,j,k-1] 
                                    - hz[i,j,k] + hz[i-1,j,k])
                dz[i,j,k] += 0.5 * (hy[i,j,k] - hy[i-1,j,k] 
                                    - hx[i,j,k] + hx[i,j-1,k])
    
    ex = gax * dx; ey = gay * dy; ez = gaz * dz
    
    # Inject Gaussian pulse in dipole gap
    pulse = np.exp(-0.5 * ((t0 - time_step) / spread)**2)
    ez[ic, jc, kc] = pulse
    
    # H-field updates
    for k in range(1, ke-1):
        for j in range(1, je-1):
            for i in range(1, ie-1):
                hx[i,j,k] += 0.5 * (ey[i,j,k+1] - ey[i,j,k] 
                                    - ez[i,j+1,k] + ez[i,j,k])
                hy[i,j,k] += 0.5 * (ez[i+1,j,k] - ez[i,j,k] 
                                    - ex[i,j,k+1] + ex[i,j,k])
                hz[i,j,k] += 0.5 * (ex[i,j+1,k] - ex[i,j,k] 
                                    - ey[i+1,j,k] + ey[i,j,k])
```

> **Numba optimization:** `@numba.jit(nopython=True)` compiles the loop to near-C performance, making 3D FDTD practical in Python.
> **Numba 优化：** `@jit` 将循环编译为近 C 性能，使 Python 实现的三维 FDTD 可行。

### 3D PML Code | 三维 PML 代码

```python
npml = 8
gi1, gi2, gi3, fi1, fi2, fi3, \
gj1, gj2, gj3, fj1, fj2, fj3, \
gk1, gk2, gk3, fk1, fk2, fk3 = calculate_pml_parameters(npml, ie, je, ke)

idz = np.zeros((ie, je, ke))   # auxiliary for z-PML

# In main loop:
for k in range(1, ke):
    for j in range(1, je):
        for i in range(1, ie):
            curl_h = (hy[i,j,k] - hy[i-1,j,k] - hx[i,j,k] + hx[i,j-1,k])
            idz[i,j,k] += curl_h
            dz[i,j,k] = (gi3[i]*gj3[j]*dz[i,j,k] 
                        + gi2[i]*gj2[j]*(0.5*curl_h + gk1[k]*idz[i,j,k]))
```

---

## Key Equations Summary | 关键方程总结

| Equation | Name | Physical Meaning | 物理含义 |
|---|---|---|---|
| (6.1a-f) | 3D Maxwell curl eqs | Six scalar for all components | 6 个标量方程 |
| (6.3) | 3D PML field eq | Anisotropic lossy medium | 各向异性有耗介质 |
| D-update + idz | 3D PML D-field | Requires auxiliary idz | 需要辅助 idz |
| TF/SF corrections | 3D wave injection | Add/subtract at y-boundary | 在 y 边界加减 |

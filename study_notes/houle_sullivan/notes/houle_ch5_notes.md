---
title: "Two-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 5
---

# Chapter 5 — Two-Dimensional Simulation

> **中英双语版**

## 5.1 FDTD in Two Dimensions: TM Mode | 二维 FDTD：TM 模式

### Reducing Maxwell's Equations to TM Mode | 简化麦克斯韦方程到 TM 模式

For 2D simulation, we choose between two modes:
二维仿真有两种模式：
- **TM mode:** $E_z, H_x, H_y$ (transverse magnetic — E has no transverse component)（横磁模式 — E 没有横向分量）
- **TE mode:** $H_z, E_x, E_y$ (transverse electric — H has no transverse component)（横电模式 — H 没有横向分量）

Using the normalized Maxwell's equations:
使用归一化麦克斯韦方程组：

$$
\frac{\partial D_z}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\left(\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right) \tag{5.1a}
$$
$$
\frac{\partial H_x}{\partial t} = -\frac{1}{\varepsilon_0\mu_0}\frac{\partial E_z}{\partial y} \tag{5.1c}
$$
$$
\frac{\partial H_y}{\partial t} = \frac{1}{\varepsilon_0\mu_0}\frac{\partial E_z}{\partial x} \tag{5.1d}
$$

### Yee Grid in 2D | 二维 Yee 网格

The TM-mode Yee grid staggers $D_z$, $E_z$ on main grid points, with $H_x$ at $(i, j+1/2)$ and $H_y$ at $(i+1/2, j)$.
TM 模式 Yee 网格将 $D_z$、$E_z$ 放置在整数网格点，$H_x$ 在 $(i, j+1/2)$，$H_y$ 在 $(i+1/2, j)$。

### FDTD Update Equations (2D TM, Free Space) | 二维 TM 模式 FDTD 更新方程

```python
# D-field (flux density) update | D场更新
dz[i, j] = dz[i, j] + 0.5 * (hy[i, j] - hy[i-1, j] - hx[i, j] + hx[i, j-1])

# E-field update (simple lossy dielectric) | E场更新
ez[i, j] = gaz[i, j] * dz[i, j]

# Hx update | Hx更新
hx[i, j] = hx[i, j] + 0.5 * (ez[i, j] - ez[i, j+1])

# Hy update | Hy更新
hy[i, j] = hy[i, j] + 0.5 * (ez[i+1, j] - ez[i, j])
```

> **Physical intuition:** $H_x$ depends on the **y-derivative** of $E_z$, $H_y$ depends on the **x-derivative**.
> **物理直觉：** $H_x$ 依赖于 $E_z$ 对 $y$ 的导数，$H_y$ 依赖于 $E_z$ 对 $x$ 的导数。

---

## 5.2 The Perfectly Matched Layer (PML) | 完美匹配层

### The ABC Problem | 吸收边界问题

Without special treatment, waves reflect from boundaries. **Absorbing boundary conditions (ABCs)** minimize this.
没有特殊处理时，波会在边界反射。**吸收边界条件** 最小化这种反射。

### Reflection Coefficient Between Media | 介质间反射系数

If $\mu$ changes with $\varepsilon$ such that $\eta$ stays constant, $\Gamma = 0$ — **no reflection**.
如果 $\mu$ 随 $\varepsilon$ 变化使得 $\eta$ 保持恒定，则 $\Gamma = 0$ ——**无反射**。还需要**损耗**使波在到达边界前衰减。

### Berenger's PML Solution | Berenger 的 PML 方案

Idea: Use **fictitious anisotropic media** with complex permittivity and permeability.
思想：使用具有复介电常数和复磁导率的**假想各向异性介质**。

**Condition 1 — Impedance matching | 条件 1 — 阻抗匹配：**
$$
\eta_0 = \eta_m = 1 \quad \text{(normalized units)}
$$

**Condition 2 — Anisotropic indexing | 条件 2 — 各向异性索引：**
$$
\varepsilon_{Fx}^* = \frac{1}{\varepsilon_{Fy}^*},\quad \mu_{Fx}^* = \frac{1}{\mu_{Fy}^*}
$$

Choosing $\varepsilon_{Fm} = \mu_{Fm} = 1$ and $\sigma_m/\varepsilon_0 = \sigma_m/\mu_0 = \sigma_D$, then $\eta_m = 1$ everywhere — **perfectly matched**.
选择 $\varepsilon_{Fm} = \mu_{Fm} = 1$，$\sigma_m/\varepsilon_0 = \sigma_m/\mu_0 = \sigma_D$，则处处 $\eta_m = 1$ ——**完美匹配**。

### D-Field Update with PML | 含 PML 的 D 场更新

$$
D_z^{n+1/2}[i,j] = \texttt{gi3}[i]\,D_z^{n-1/2}[i,j] + \texttt{gi2}[i]\cdot 0.5\bigl(H_y^{n}[i+1/2,j] - H_y^{n}[i-1/2,j] - H_x^{n}[i,j+1/2] + H_x^{n}[i,j-1/2]\bigr) \tag{5.8}
$$

where | 其中：

$$
\texttt{gi2}[i] = \frac{1}{1 + xn[i]},\quad \texttt{gi3}[i] = \frac{1 - xn[i]}{1 + xn[i]},\quad xn[i] = \frac{\sigma_D[i]\Delta t}{2\varepsilon_0}
$$

### H-Field Updates with PML | 含 PML 的 H 场更新

**Hy update** (similar to D):
```python
Hy[i+1/2,j] = fi3[i+1/2] * Hy[i+1/2,j] + fi2[i+1/2] * 0.5 * (Ez[i+1,j] - Ez[i,j])
```

**Hx update** (uses auxiliary current $I_{Hx}$):
```python
curl_e = Ez[i,j] - Ez[i,j+1]
IHx[i,j+1/2] = IHx[i,j+1/2] + curl_e
Hx[i,j+1/2] = Hx[i,j+1/2] + 0.5 * curl_e + fi1[i] * IHx[i,j+1/2]
```

### Full 2D PML (X and Y directions) | 完整二维 PML（X 和 Y 方向）

When PML is applied on all four sides:
当 PML 应用在所有四个边界时：

$$
D_z^{n+1/2}[i,j] = \texttt{gi3}[i]\,\texttt{gj3}[j]\,D_z^{n-1/2}[i,j] + \texttt{gi2}[i]\,\texttt{gj2}[j]\cdot 0.5\bigl(H_y^{n}[i+1/2,j] - H_y^{n}[i-1/2,j] - H_x^{n}[i,j+1/2] + H_x^{n}[i,j-1/2]\bigr) \tag{5.12}
$$

### PML Profile and Parameters | PML 分布与参数

The conductivity $\sigma_D$ grows quadratically from the boundary inward:
电导率 $\sigma_D$ 从边界向内以指数增长：

```python
for i in range(1, length_pml+1):
    xn[i] = 0.333 * (i / length_pml) ** 3

gi2[i] = 1 / (1 + xn[i])
gi3[i] = (1 - xn[i]) / (1 + xn[i])
fi1[i] = xn[i]
```

> **Empirical insight:** The factor 0.333 and cubic profile were found empirically to provide the best absorption without numerical instability.
> **经验结论：** 因子 0.333 和三次方分布是经验上最佳吸收且能保持数值稳定的参数。

### Physical Interpretation | 物理解释

The PML is a **graded anisotropic absorber**. Impedance is matched at every point so waves enter without reflection. At depth 8 cells inside the PML, the wave has essentially decayed to near zero.
PML 是一个**渐变各向异性吸收体**。每点阻抗匹配使波无反射进入，8 个网格深度内波已衰减到近零。

---

## 5.3 Total-Field/Scattered-Field (TF/SF) Formulation | 总场/散射场公式

### Why TF/SF? | 为什么需要 TF/SF？

Divide the problem space into two regions:
将问题空间分为两个区域：
- **Total field region:** contains incident + scattered waves（**总场区：** 包含入射+散射波）
- **Scattered field region:** contains only scattered waves（**散射场区：** 只包含散射波）

### TF/SF Boundary Corrections | TF/SF 边界修正

**1. Dz at bottom (j=ja) and top (j=jb):**
```python
dz[i, ja] += 0.5 * Hx_inc[ja-1]
dz[i, jb] -= 0.5 * Hx_inc[jb+1]
```

**2. Hx just outside at j=ja and j=jb:**
```python
Hx[i, ja-1/2] += 0.5 * Ez_inc[ja]
Hx[i, jb+1/2] -= 0.5 * Ez_inc[jb]
```

**3. Hy just outside at i=ia and i=ib:**
```python
Hy[ia-1/2, j] -= 0.5 * Ez_inc[j]
Hy[ib+1/2, j] += 0.5 * Ez_inc[j]
```

### Plane Wave Pulse Generation | 平面波脉冲生成

```python
pulse = exp(-0.5 * ((t0 - time_step) / spread)**2)
ez_inc[ja] = pulse + ez_inc[ja]   # inject at boundary | 在边界注入
```

The same pulse is simultaneously subtracted at `jb`, ensuring no net energy accumulates.
同一脉冲同时在 `jb` 处减去，确保无净能量积累。

---

## 5.3.1 Plane Wave Impinging on a Dielectric Cylinder | 平面波入射介质圆柱

### Object Specification | 目标设定

```python
for j in range(ja, jb):
    for i in range(ia, ib):
        dist = sqrt((ic-i)**2 + (jc-j)**2)
        if dist <= radius:
            gaz[i,j] = 1/(epsr + sigma*dt/epsz)
            gbz[i,j] = sigma*dt/epsz
```

> **Limitation:** "In-or-out" specification causes **staircasing** — the fundamental accuracy limitation of FDTD on curved geometries.
> **局限性：** "进出式"指定导致**阶梯化**——FDTD 在弯曲几何上的基本精度限制。

### Subcell Averaging | 亚网格平均

A 3×3 subcell averaging technique reduces staircasing:
3×3 亚网格平均技术减少阶梯效应：

```python
for j in range(ja, jb):
    for i in range(ia, ib):
        eps = 1.0; cond = 0.0
        for jj in range(-1, 2):
            for ii in range(-1, 2):
                xdist = (ic-i) + (1/3)*ii
                ydist = (jc-j) + (1/3)*jj
                if sqrt(xdist**2 + ydist**2) <= radius:
                    eps += (1/9)*(epsr-1)
                    cond += (1/9)*sigma
        gaz[i,j] = 1.0/(eps + cond*dt/epsz)
```

### Validation | 验证

FDTD shows excellent agreement with analytical Bessel function solutions along the center axis (Fig. 5.10). This confirms the TF/SF + DFT methodology.
FDTD 与解析贝塞尔函数解沿中心轴高度吻合，验证了 TF/SF + DFT 方法的正确性。

---

## Key Equations Summary | 关键方程总结

| Equation | Name | Physical Meaning | 物理含义 |
|---|---|---|---|
| (5.1a-d) | 2D TM Maxwell | Only $E_z, H_x, H_y$ | 仅三个场分量 |
| (5.2a-d) | 2D TM FDTD updates | Yee grid on a plane | 平面上 Yee 网格 |
| (5.4) | PML impedance match | $\eta=1$ at every point | 各点阻抗匹配 |
| (5.8) | D-field with PML | Attenuated by gi3 | gi3 系数控制衰减 |
| (5.11a-c) | Hx with PML | IHx auxiliary for inverse $\mu$ | IHx 辅助处理逆磁导率 |
| (5.13a-b) | TF/SF Dz correction | Add incident Hx at boundary | 边界添加入射 Hx |

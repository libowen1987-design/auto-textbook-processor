---
title: "More on One-Dimensional Simulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 3
---

# Chapter 3 — More on One-Dimensional Simulation

> **中英双语版**

## 3.1 Reformulation Using the Flux Density | 使用电通量密度重新表述

A more general form uses the electric flux density **D**:
更通用的形式使用电通量密度 **D**：

$$
\frac{\partial \mathbf{D}}{\partial t} = \nabla \times \mathbf{H} \tag{3.1a}
$$
$$
\mathbf{D}(\omega) = \varepsilon_0 \varepsilon_r^*(\omega) \mathbf{E}(\omega) \tag{3.1b}
$$
$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu_0} \nabla \times \mathbf{E} \tag{3.1c}
$$

### Normalization | 归一化

$$
\tilde{\mathbf{E}} = \sqrt{\frac{\varepsilon_0}{\mu_0}} \mathbf{E},\quad
\tilde{\mathbf{D}} = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} \mathbf{D}
$$

### From Frequency Domain to Time Domain: Lossy Dielectric | 从频域到时域：有耗介质

For a lossy dielectric medium:
对于有耗介质：

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega \varepsilon_0} \tag{3.4}
$$

The second term $1/(j\omega)$ corresponds to **integration in time**:
第二项 $1/(j\omega)$ 对应**时间积分**：

$$
D(t) = \varepsilon_r E(t) + \frac{\sigma}{\varepsilon_0} \int_0^t E(t')\, dt' \tag{3.6}
$$

### Decoupling the Current $E^n$ Term | 解耦当前 $E^n$ 项

Solving for $E^n$ with auxiliary parameter $I^n$:
用辅助参数 $I^n$ 解出 $E^n$：

$$
E^n = \frac{D^n - I^{n-1}}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0}} \tag{3.8a}
$$
$$
I^n = I^{n-1} + \frac{\sigma \Delta t}{\varepsilon_0} E^n \tag{3.9}
$$

### Final FDTD Formulation (1D) | 最终一维 FDTD 公式

$$
D_x^{n+1}[k] = D_x^n[k] + 0.5 \cdot (H_y^n[k-1] - H_y^n[k]) \tag{3.10a}
$$
$$
E_x^{n+1}[k] = \texttt{gax}[k] \cdot D_x^{n+1}[k] - \texttt{ix}[k] \tag{3.10b}
$$
$$
I_x^{n+1}[k] = I_x^n[k] + \texttt{gbx}[k] \cdot E_x^{n+1}[k] \tag{3.10c}
$$
$$
H_y^{n+1}[k] = H_y^n[k] + 0.5 \cdot (E_x^{n+1}[k] - E_x^{n+1}[k+1]) \tag{3.10d}
$$

where the **media coefficients** | 其中介质系数：

$$
\texttt{gax}[k] = \frac{1}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0}},\quad
\texttt{gbx}[k] = \frac{\sigma \Delta t}{\varepsilon_0} \tag{3.11a,b}
$$

> **Key insight:** All media information is in Eqs. (3.10b) and (3.10c). Eqs. (3.10a) and (3.10d) remain **unchanged** regardless of the medium.
> **关键洞察：** 所有介质信息都在式 (3.10b) 和 (3.10c) 中。式 (3.10a) 和 (3.10d) 对任意介质**不变**。

For **free space**: `gax = 1`, `gbx = 0`.
For **lossy material**: calculate using Eq. (3.11).

---

## 3.2 Calculating the Frequency Domain Output | 计算频域输出

### The Impulse Response Approach | 冲激响应方法

Better approach: Use an **impulse** (narrow Gaussian pulse). Iterate until pulse dies out, take Fourier transform. Yields response at **all frequencies simultaneously**.
更好方法：使用**冲激**（窄高斯脉冲）。迭代到脉冲消失，取傅里叶变换。**同时**得到所有频率的响应。

### The Discrete Fourier Transform (DFT) in FDTD | FDTD 中的 DFT

$$
E(f_1) = \sum_{n=0}^{T} E^n \Delta t \, e^{-j 2\pi f_1 n \Delta t}
$$

### Implementation: Running Sums | 实现：运行累加

```python
real_pt[m,k] += cos(2*pi*f_m*dt*time_step) * E_x[k]
imag_pt[m,k] -= sin(2*pi*f_m*dt*time_step) * E_x[k]
```

> **Computational elegance:** Only two values per frequency per cell — no need to store the entire time-series!
> **计算优势：** 每个频率每单元仅两个值——无需存储整个时间序列！

### Amplitude and Phase Extraction | 幅度和相位提取

$$
\text{Amplitude}[m,k] = \sqrt{\texttt{real\_pt}[m,k]^2 + \texttt{imag\_pt}[m,k]^2}
$$
$$
\text{Phase}[m,k] = \text{atan2}(\texttt{imag\_pt}[m,k], \texttt{real\_pt}[m,k])
$$

---

## 3.3 Frequency-Dependent Media: The Debye Formulation | 频变介质：德拜公式

### The Problem | 问题

Most real media have $\varepsilon_r$ and $\sigma$ that **vary with frequency**.
大多数真实介质的 $\varepsilon_r$ 和 $\sigma$ 随频率变化。

### Debye Model for Dispersive Media | 色散介质的德拜模型

A single-pole Debye medium:
单极点德拜介质：

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega \varepsilon_0} + \frac{\chi_1}{1 + j\omega \tau} \tag{3.18}
$$

Parameters: $\varepsilon_r$ - static constant; $\sigma$ - conductivity; $\chi_1$ - frequency-dependent susceptibility; $\tau$ - relaxation time.
参数：$\varepsilon_r$ 静态介电常数；$\sigma$ 电导率；$\chi_1$ 频变极化率；$\tau$ 弛豫时间。

### From Frequency Domain to Time Domain | 从频域到时域

Define Debye term $S(\omega) = \frac{\chi_1}{1 + j\omega\tau} E(\omega)$.
定义德拜项 $S(\omega)$。

Inverse Fourier transform: $\frac{\chi_1}{\tau} e^{-t/\tau} u(t)$
逆傅里叶变换给出时间域卷积。

Sampled time domain recurrence:
采样时域递推：

$$
S^n = e^{-\Delta t/\tau} S^{n-1} + \frac{\chi_1 \Delta t}{\tau} E^n \tag{3.22}
$$

### Complete Update Equations for Debye Medium | 德拜介质的完整更新方程

$$
E^n = \frac{D^n - I^{n-1} - e^{-\Delta t/\tau} S^{n-1}}{\varepsilon_r + \frac{\sigma \Delta t}{\varepsilon_0} + \frac{\chi_1 \Delta t}{\tau}} \tag{3.24a}
$$
$$
I^n = I^{n-1} + \frac{\sigma \Delta t}{\varepsilon_0} E^n \tag{3.24b}
$$
$$
S^n = e^{-\Delta t/\tau} S^{n-1} + \frac{\chi_1 \Delta t}{\tau} E^n \tag{3.24c}
$$

### FDTD Code Implementation (1D Debye Medium) | 一维德拜介质 FDTD 代码实现

```python
dx[k] = dx[k] + 0.5 * (hy[k-1] - hy[k])          # D-field
ex[k] = gax[k] * dx[k] - ix[k] - del_exp * sx[k]  # E-field
ix[k] = ix[k] + gbx[k] * ex[k]                    # I update (conductive)
sx[k] = del_exp * sx[k] + gcx[k] * ex[k]           # S update (Debye)
hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])            # H-field
```

where:

```python
gax[k] = 1.0 / (epsr + sigma*dt/epsz + chi*dt/tau)
gbx[k] = sigma * dt / epsz
gcx[k] = chi * dt / tau
del_exp = exp(-dt / tau)
```

> **Physical intuition:** Higher $\sigma$ → more conductive loss. Higher $\chi_1$ → stronger Debye polarization. Smaller $\tau$ → faster relaxation.
> **物理直觉：** $\sigma$ 越大 → 电导损耗越大。$\chi_1$ 越大 → 德拜极化越强。$\tau$ 越小 → 弛豫越快。

---

## 3.3.1 Auxiliary Differential Equation (ADE) Method | 辅助微分方程法

Starting from Eq. (3.19): $(1 + j\omega\tau) S(\omega) = \chi_1 E(\omega)$:
从式 (3.19) 出发：

$$
S(t) + \tau \frac{dS(t)}{dt} = \chi_1 E(t) \tag{3.28}
$$

In discrete time domain, this becomes a simple algebraic update for $S^n$.
离散时域中，这变成 $S^n$ 的简单代数更新。

---

## Code Reference | 代码参考

### Figure 3.1 Simulation Code (`fd3d_1_1.py`)

```python
import numpy as np
from math import exp

ke = 200; ex = np.zeros(ke); hy = np.zeros(ke)
kc = int(ke/2); t0 = 40; spread = 12; nsteps = 100

for time_step in range(1, nsteps + 1):
    for k in range(1, ke):       # E-field
        ex[k] = ex[k] + 0.5 * (hy[k-1] - hy[k])
    pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
    ex[kc] = pulse               # Hard source
    for k in range(ke - 1):      # H-field
        hy[k] = hy[k] + 0.5 * (ex[k] - ex[k+1])
```

### Absorbing Boundary Condition Code (`fd3d_1_2.py`)

```python
ex[0] = boundary_low.pop(0)               # Left ABC
boundary_low.append(ex[1])
ex[ke-1] = boundary_high.pop(0)           # Right ABC
boundary_high.append(ex[ke-2])
```

### Lossy Dielectric Code (`fd3d_1_5.py`)

```python
epsilon = 4; sigma = 0.04
eaf = dt * sigma / (2 * epsz * epsilon)
ca[cb_start:] = (1 - eaf) / (1 + eaf)
cb[cb_start:] = 0.5 / (epsilon * (1 + eaf))
# In main loop: ex[k] = ca[k]*ex[k] + cb[k]*(hy[k-1] - hy[k])
```

---

## Key Equations Summary | 关键方程总结

| Equation | Name | Physical Meaning | 物理含义 |
|---|---|---|---|
| (3.1b) | D-E constitutive | Links D to E via $\varepsilon_r^*$ | D-E 本构关系 |
| (3.8a-b) | Flux density reform. | $I^n$ tracks conductive loss history | 辅助电流 $I^n$ 追踪电导损耗 |
| (3.10a-d) | 1D FDTD with flux | Media info in E-step only | 介质信息仅在 E 步 |
| (3.11a-b) | gax/gbx coefficients | Encodes $\varepsilon_r$ and $\sigma$ | 编码 $\varepsilon_r$ 和 $\sigma$ |
| (3.15a-b) | Running DFT | No need to store time-series | 无需存储时间序列 |
| (3.18) | Debye model | Single-pole dispersive permittivity | 单极点色散介电常数 |
| (3.24a-c) | Debye update | $E$, $I$ (loss), $S$ (polarization) | 三个辅助变量 |

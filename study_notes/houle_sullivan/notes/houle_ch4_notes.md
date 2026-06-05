---
title: "More on One-Dimensional Simulation — Z Transform Formulation"
author: "Jennifer E. Houle and Dennis M. Sullivan"
book: "Electromagnetic Simulation Using the FDTD Method with Python, Third Edition"
chapter: 4
---

# Chapter 4 — More on One-Dimensional Simulation: Z Transform Formulation

> **中英双语版**

## 4.1 Z Transform Formulation for Frequency-Dependent Media | 频变介质的 Z 变换公式

### The Z Transform Advantage | Z 变换的优势

Chapter 3 showed how to handle frequency-dependent media via a convolution approach. The **Z transform** method provides an equivalent but more elegant formulation — particularly valuable as media become more complex.
第 3 章通过卷积方法处理频变介质。**Z 变换**方法提供了等价但更优雅的公式——尤其在介质变得更复杂时更有价值。

Starting from the frequency-domain permittivity of a Debye medium:
从德拜介质的频域介电常数出发：

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0} + \frac{\chi_1}{1 + j\omega\tau} \tag{4.1}
$$

Going to the **Z domain** directly:
直接转换到 **Z 域**：

$$
D(z) = \varepsilon_r E(z) + \frac{\sigma\Delta t}{\varepsilon_0}\frac{1 - z^{-1}}{1} E(z) + \frac{\chi_1\Delta t}{\tau}\frac{1 - e^{-\Delta t/\tau}z^{-1}}{1} E(z) \tag{4.2}
$$

### Defining Auxiliary Parameters in Z Domain | Z 域中定义辅助参数

Define two auxiliary Z-domain variables:
定义两个 Z 域辅助变量：

$$
I(z) = \frac{\sigma\Delta t}{\varepsilon_0}(1 - z^{-1})E(z) = z^{-1}I(z) + \frac{\sigma\Delta t}{\varepsilon_0}E(z) \tag{4.3a}
$$

$$
S(z) = \frac{\chi_1\Delta t}{\tau}(1 - e^{-\Delta t/\tau}z^{-1})E(z) = e^{-\Delta t/\tau}z^{-1}S(z) + \frac{\chi_1\Delta t}{\tau}E(z) \tag{4.3b}
$$

Solving for $E(z)$ | 解出 $E(z)$：

$$
E(z) = \frac{D(z) - z^{-1}I(z) - e^{-\Delta t/\tau}z^{-1}S(z)}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0} + \frac{\chi_1\Delta t}{\tau}} \tag{4.5}
$$

### Direct Sampled-Time Translation | 直接采样时间翻译

**Key advantage of Z transforms:** replace $E(z) \rightarrow E^n$, $z^{-1}E(z) \rightarrow E^{n-1}$, etc.
**Z 变换的关键优势：** 直接替换为时域采样值即可。

$$
E^n = \frac{D^n - I^{n-1} - e^{-\Delta t/\tau}S^{n-1}}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0} + \frac{\chi_1\Delta t}{\tau}} \tag{4.6a}
$$
$$
I^n = I^{n-1} + \frac{\sigma\Delta t}{\varepsilon_0}E^n \tag{4.6b}
$$
$$
S^n = e^{-\Delta t/\tau}S^{n-1} + \frac{\chi_1\Delta t}{\tau}E^n \tag{4.6c}
$$

> **Why Z transforms?** We avoided dealing with convolution integrals and their approximations. As we move to more complicated multi-pole models (Lorentz), the Z transform formulation scales elegantly.
> **为什么用 Z 变换？** 我们避免了卷积积分及其近似。当转到更复杂的多极点模型（洛伦兹）时，Z 变换公式可以优雅地扩展。

---

## 4.2 Simulation of an Unmagnetized Plasma | 非磁化等离子体仿真

### Plasma Permittivity | 等离子体介电常数

$$
\varepsilon^*(\omega) = 1 + \frac{\omega_p^2}{\nu_c + j\omega} \tag{4.7}
$$

where: $\omega_p = 2\pi f_p$ — **plasma frequency**; $\nu_c$ — electron collision frequency.
其中 $\omega_p$ 为**等离子体频率**，$\nu_c$ 为电子碰撞频率。

> **Physical intuition:** Below $\omega_p$, plasma behaves like a metal (reflects waves). Above $\omega_p$, it becomes transparent.
> **物理直觉：** 低于 $\omega_p$ 时等离子体像金属（反射波）；高于 $\omega_p$ 时变成透明。

### Partial Fraction Expansion | 部分分式展开

$$
\varepsilon^*(\omega) = 1 + \frac{\omega_p^2}{\nu_c}\frac{1}{j\omega} - \frac{\omega_p^2}{\nu_c}\frac{1}{\nu_c + j\omega} \tag{4.8}
$$

### Z Domain Formulation | Z 域公式

Taking the Z transform | 取 Z 变换：

$$
\varepsilon^*(z) = 1 + \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - z^{-1}}{1} - \frac{\omega_p^2\Delta t}{\nu_c}\frac{1 - e^{-\nu_c\Delta t}z^{-1}}{1} \tag{4.9}
$$

### FDTD Implementation (1D Plasma) | 一维等离子体 FDTD 实现

```python
ex[k] = dx[k] - sx[k]

sxm1 = sxm2
sxm2 = sxm1_new
sx = (1 + np.exp(-vc*dt)) * sxm1 - np.exp(-vc*dt) * sxm2 \
     + (omega**2 * dt / vc) * (1 - np.exp(-vc*dt)) * ex[k]
```

### Physical Example: Silver Plasma | 银等离子体示例

Silver: $\omega_p = 2\pi \times 2000$ THz, $\nu_c = 57$ THz
- At **500 THz** (below $\omega_p$): wave is almost completely **reflected**（几乎完全反射）
- At **4000 THz** (above $\omega_p$): wave **passes through**（穿透通过）

---

## 4.3 Formulating a Lorentz Medium | 构建洛伦兹介质模型

### The Lorentz Model (Two-Pole) | 洛伦兹模型（双极点）

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\varepsilon_1}{1 + j2\delta_0\frac{\omega}{\omega_0} - \left(\frac{\omega}{\omega_0}\right)^2} \tag{4.13}
$$

Parameters: $\varepsilon_r$ - static constant; $\varepsilon_1$ - resonance strength; $\omega_0$ - resonant freq; $\delta_0$ - damping factor.
参数：$\varepsilon_r$ 静态介电常数；$\varepsilon_1$ 谐振强度；$\omega_0$ 谐振频率；$\delta_0$ 阻尼因子。

### ADE Method for Lorentz | 洛伦兹模型 ADE 方法

Starting from | 从方程开始：

$$
(\omega_0^2 + j2\delta_0\omega_0\omega - \omega^2)S(\omega) = \omega_0^2\varepsilon_1 E(\omega) \tag{4.15}
$$

Going to continuous time domain (second-order ODE):
转到连续时域（二阶 ODE）：

$$
\omega_0^2 S(t) + 2\delta_0\omega_0\frac{dS(t)}{dt} + \frac{d^2S(t)}{dt^2} = \omega_0^2\varepsilon_1 E(t) \tag{4.16}
$$

### Alternative Z Transform Method | 替代 Z 变换方法

$$
S^n = 2e^{-\alpha\Delta t}\cos(\beta\Delta t)S^{n-1} - e^{-2\alpha\Delta t}S^{n-2} + e^{-\alpha\Delta t}\sin(\beta\Delta t)\Delta t\gamma\varepsilon_1 E^{n-1} \tag{4.21}
$$

where $\alpha = \delta_0\omega_0$, $\beta = \omega_0\sqrt{1-\delta_0^2}$, $\gamma = \omega_0/\sqrt{1-\delta_0^2}$.

---

## 4.3.1 Simulation of Human Muscle Tissue | 人体肌肉组织仿真

### Cole-Cole Model for Biological Tissue | 生物组织的 Cole-Cole 模型

$$
\varepsilon_r^*(\omega) = \varepsilon_r + \frac{\sigma}{j\omega\varepsilon_0} + \varepsilon_1\frac{\omega_0}{\omega_0^2 + \alpha^2 + j\omega 2\alpha - \omega^2} \tag{4.22}
$$

### Muscle Tissue Properties | 肌肉组织特性

| Frequency (MHz) | $\varepsilon_r'$ | $\sigma$ (S/m) |
|---|---|---|
| 10   | 160   | 0.625 |
| 40   | 97    | 0.693 |
| 100  | 72    | 0.89  |
| 433  | 53    | 1.43  |
| 915  | 51    | 1.60  |

> **Physical intuition:** Muscle is lossy and water-rich. At low MHz, high $\varepsilon_r$ (~160) reflects bound water response. As frequency increases, $\varepsilon_r$ drops and $\sigma$ increases.
> **物理直觉：** 肌肉有耗且富含水分。低频时高介电常数反映结合水响应；随频率升高，$\varepsilon_r$ 下降、$\sigma$ 增大。

### FDTD Update Equations for Muscle Tissue | 肌肉组织 FDTD 更新方程

$$
E(z) = \frac{D(z) - z^{-1}I(z) - z^{-1}S(z)}{\varepsilon_r + \frac{\sigma\Delta t}{\varepsilon_0}} \tag{4.26a}
$$
$$
I(z) = z^{-1}I(z) + \frac{\sigma\Delta t}{\varepsilon_0}E(z) \tag{4.26b}
$$
$$
S(z) = 2e^{-\alpha\Delta t}\cos(\omega_0\Delta t)z^{-1}S(z) - e^{-2\alpha\Delta t}z^{-2}S(z) + \varepsilon_1 e^{-\alpha\Delta t}\sin(\omega_0\Delta t)\Delta t\, E(z) \tag{4.26c}
$$

> **Note:** Eq. (4.26c) requires storing **two previous values** of $S$ ($S^{n-1}$ and $S^{n-2}$).
> **注意：** 式 (4.26c) 需要存储 $S$ 的**两个前值**。

---

## Key Equations Summary | 关键方程总结

| Equation | Name | Physical Meaning | 物理含义 |
|---|---|---|---|
| (4.7) | Plasma permittivity | $\omega_p$ determines metal vs. dielectric | 等离子体频率决定金属/介质行为 |
| (4.10) | Z-domain plasma | Two-pole form similar to Debye | 双极点形式类似德拜 |
| (4.13) | Lorentz model | Resonance with damping | 含阻尼的谐振模型 |
| (4.19) | ADE Lorentz update | $S^n$ uses $S^{n-1}, S^{n-2}, E^{n-1}$ | 二阶差分更新 |
| (4.22) | Cole-Cole (muscle) | Lossy dispersive biological tissue | 有耗色散生物组织 |
| (4.26a-c) | Muscle FDTD update | Three auxiliary: $E$, $I$, $S$ | 三个辅助变量 |

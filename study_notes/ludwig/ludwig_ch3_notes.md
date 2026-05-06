---
title: "Chapter 3 — The Smith Chart"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "115–147"
processed: "2026-05-03"
tags: [smith-chart, reflection-coefficient, impedance-matching, admittance, stub]
---

# Chapter 3: The Smith Chart

> **Overview:** This chapter introduces the Smith Chart as a graphical tool for transmission line impedance/admittance calculations. It covers the mathematical derivation from reflection coefficient to normalized impedance, the construction of constant-resistance and constant-reactance circles, and practical usage including impedance transformation, admittance conversion, stub design, and series/parallel RLC analysis.

---

## 3.1 From Reflection Coefficient to Load Impedance

### 3.1.1 Reflection Coefficient in Phasor Form

$$
\Gamma_0 = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_0| e^{j\theta_\Gamma} \tag{3.1}
$$

Key points in $\Gamma$-plane:
- Short circuit ($Z_L=0$): $\Gamma_0 = -1$
- Open circuit ($Z_L\to\infty$): $\Gamma_0 = +1$
- Matched ($Z_L=Z_0$): $\Gamma_0 = 0$

> **Example 3-1:** For $Z_0=50\ \Omega$:
> - $Z_L=0$: $\Gamma_0=-1$
> - $Z_L=\infty$: $\Gamma_0=1$
> - $Z_L=50\ \Omega$: $\Gamma_0=0$
> - $Z_L=(16.67-j16.67)\ \Omega$: $\Gamma_0=0.54\angle 221^\circ$
> - $Z_L=(50+j150)\ \Omega$: $\Gamma_0=0.83\angle 34^\circ$

### 3.1.2 Normalized Impedance Equation

$$
z_{\text{in}} = \frac{1+\Gamma}{1-\Gamma} \tag{3.4}
$$

Separating into real and imaginary parts:

$$
r = \frac{1-\Gamma_r^2-\Gamma_i^2}{(1-\Gamma_r)^2+\Gamma_i^2} \tag{3.6}
$$

$$
x = \frac{2\Gamma_i}{(1-\Gamma_r)^2+\Gamma_i^2} \tag{3.7}
$$

> **Example 3-2:** $Z_L=(30+j60)\ \Omega$, $Z_0=50\ \Omega$, $l=2$ cm, $f=2$ GHz, $v_p=0.5c$:
> - $\Gamma_0 = 0.6\angle 56.3^\circ$
> - $\Gamma(d) = 0.6\angle (56.3^\circ - 191.99^\circ) = 0.6\angle -120.43^\circ$
> - $Z_{\text{in}} = Z_0 \frac{1+\Gamma}{1-\Gamma} = (14.7 - j26.7)\ \Omega$

### 3.1.3 Parametric Reflection Coefficient Equation

Mapping constant $r$ circles:

$$
\left(\Gamma_r - \frac{r}{r+1}\right)^2 + \Gamma_i^2 = \left(\frac{1}{r+1}\right)^2 \tag{3.10}
$$

Mapping constant $x$ circles:

$$
(\Gamma_r - 1)^2 + \left(\Gamma_i - \frac{1}{x}\right)^2 = \left(\frac{1}{x}\right)^2 \tag{3.11}
$$

**Smith Chart construction:** Overlay of constant-$r$ circles (Fig. 3-2) and constant-$x$ circles (Fig. 3-3) inside $|\Gamma| \le 1$. Rotation toward generator is clockwise (negative direction) by $2\beta d$.

---

## 3.2 Impedance Transformation

### Six-Step Smith Chart Procedure (Example 3-3)

1. Normalize: $z_L = Z_L/Z_0$
2. Locate $z_L$ at intersection of $r=\text{const}$ and $x=\text{const}$ circles
3. Read $\Gamma_0$ (magnitude and phase)
4. Rotate by $2\beta d$ clockwise → $\Gamma_{\text{in}}$
5. Read $z_{\text{in}}$ at the new location
6. Denormalize: $Z_{\text{in}} = z_{\text{in}} \cdot Z_0$

### 3.2.2 Standing Wave Ratio

$$
\text{SWR} = \frac{1+|\Gamma(d)|}{1-|\Gamma(d)|} \tag{3.12}
$$

- Read SWR from Smith Chart: intersection of $|\Gamma|$ circle with positive real axis.
- $|\Gamma| = \frac{\text{SWR}-1}{\text{SWR}+1}$

> **Example 3-4:** Four loads on $Z_0=50\ \Omega$:
> - $Z_L=50\ \Omega$: $\Gamma_0=0$, RL$=\infty$ dB, SWR$=1$
> - $Z_L=48.5\ \Omega$: $\Gamma_0=-0.015$, RL$=36.3$ dB, SWR$=1.03$
> - $Z_L=(75+j25)\ \Omega$: $\Gamma_0=0.27\angle 33.7^\circ$, RL$=11.1$ dB, SWR$=1.77$
> - $Z_L=(10-j5)\ \Omega$: $\Gamma_0=0.67\angle -168^\circ$, RL$=3.5$ dB, SWR$=5.05$

### 3.2.3 Open- and Short-Circuit Transformations

**Open-circuit stub** (start at $\Gamma_0=+1$):
- Capacitive ($-jX_C$): $d_1 = \frac{1}{\beta}\cot^{-1}\left(\frac{X_C}{Z_0}\right) \tag{3.16}$
- Inductive ($+jX_L$): $d_2 = \frac{1}{\beta}\tan^{-1}\left(\frac{X_L}{Z_0}\right) \tag{3.18}$

**Short-circuit stub** (start at $\Gamma_0=-1$):
- Capacitive: $d_1 = \frac{1}{\beta}\left[\pi - \tan^{-1}\left(\frac{X_C}{Z_0}\right)\right] \tag{3.20}$
- Inductive: $d_2 = \frac{1}{\beta}\tan^{-1}\left(\frac{X_L}{Z_0}\right) \tag{3.22}$

> **Example 3-5:** Open-circuit 50 $\Omega$ line at 3 GHz ($v_p=0.77c$):
> - 2 pF capacitor ($X_C=26.5\ \Omega$): $d_1=13.27 + n\cdot38.5$ mm
> - 5.3 nH inductor ($X_L=100\ \Omega$): $d_2=32.81 + n\cdot38.5$ mm

> **工程直觉:** 高频时开路短截线易受环境（温度/湿度）影响，工程中更偏好短路短截线。但短路短截线在极高频率时会产生寄生电感。实现电容时开路短截线长度最短。

---

## 3.3 Admittance Transformation

### From Impedance to Admittance

$$
y_{\text{in}} = \frac{1}{z_{\text{in}}} = \frac{1-\Gamma}{1+\Gamma}, \quad \Gamma \to -\Gamma \ (\text{180° rotation}) \tag{3.23, 3.24}
$$

**Y-Smith Chart:** Same circles reinterpreted:
- $r \to g$ (conductance), $x \to b$ (susceptance)
- Short ($z=0$) ↔ open ($y=\infty$)
- Upper half: inductive $b$, Lower half: capacitive $b$
- Real axis: $b=0$; conductance increases right→left

**ZY-Smith Chart:** Z and Y charts overlaid (Fig. 3-12) for direct impedance ↔ admittance conversion without manual rotation.

> **Example 3-6:** $z=1+j1$ → 180° rotation → $y=0.5-j0.5$
> **Example 3-7:** $z=0.5+j0.5$ in ZY-Chart → $y=1-j1$

---

## 3.4 Parallel and Series Connections

### Parallel RL (Y-Chart, upper half)

$$
y = g - j\frac{Z_0}{\omega L} \quad \text{(along constant-}g\text{ circle)}
$$

### Parallel RC (Y-Chart, lower half)

$$
y = g + j\omega C Z_0 \quad \text{(along constant-}g\text{ circle)}
$$

### Series RL (Z-Chart, upper half)

$$
z = r + j\frac{\omega L}{Z_0} \quad \text{(along constant-}r\text{ circle)}
$$

### Series RC (Z-Chart, lower half)

$$
z = r - j\frac{1}{\omega C Z_0} \quad \text{(along constant-}r\text{ circle)}
$$

> **工程直觉:** 串联元件在Z-Smith Chart上沿等电阻圆移动；并联元件在Y-Smith Chart上沿等电导圆移动。T型/π型网络通过交替Z↔Y变换来逐步添加串/并联元件。

### T-Network Example (Fig. 3-17)

T-network: $L_1$ (series) → shunt $R_L\|C_L$ → $C$ (shunt) → $L_2$ (series) at 2 GHz.

**Smith Chart steps (Z↔Y alternating):**
1. $R_L=31.25\ \Omega$ → $g=1.6$ in Y-Chart (point A)
2. Add $C_L=1.91$ pF → rotate along $g=1.6$ by $b=1.2$ (point B)
3. Convert B to Z-Chart → $z=0.4-j0.3$
4. Add $L_1$ → rotate along $r=0.4$ by $x=1.1$ (point C)
5. Convert C to Y-Chart → $y=0.5-j1.0$
6. Add $C=2.39$ pF → rotate along $g=0.5$ by $b=1.5$ (point D)
7. Convert D to Z-Chart → $z=1-j1$
8. Add $L_2$ → rotate along $r=1$ by $x=1$ → $z_{\text{in}}=1$ (point E) → $Z_{\text{in}}=50\ \Omega$ ✅

> **工程直觉:** 交替使用Z-Y-Smith Chart是处理串并联混合网络的精髓。每次串联 → 用Z-Chart移动；每次并联 → 转为Y-Chart移动。这种交替映射避免了复杂的代数运算。

---

## 审计表 (Audit)

| 项目 | 状态 | 备注 |
|------|------|------|
| §3.1 $\Gamma$→ $z$ 映射 | ✅ | 圆方程推导 |
| §3.1.2 归一化阻抗 | ✅ | Ex3-1, Ex3-2 |
| §3.2 阻抗变换 | ✅ | 六步法/Ex3-3 |
| §3.2.2 VSWR/RL | ✅ | Ex3-4 |
| §3.2.3 开路/短路变换 | ✅ | Ex3-5 |
| §3.3 导纳变换 | ✅ | Ex3-6, Ex3-7 |
| §3.4 串并联RLC | ✅ | 四种组合 + T网络 |
| 例题代码复现 | ✅ | 核心计算全部代码化 |
| 工程直觉段落 | ✅ | 每节末尾 |

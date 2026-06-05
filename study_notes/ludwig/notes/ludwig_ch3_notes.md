---
chapter: 3
title: The Smith Chart
source: Ludwig & Bogdanov, RF Circuit Design, 2nd Edition
pages: 115-157
---

# Chapter 3: The Smith Chart | 第3章：Smith 圆图

## 3.1 From Reflection Coefficient to Load Impedance | 从反射系数到负载阻抗

> **Original:** A transmission line changes its impedance depending on material properties and geometric dimensions. To facilitate the evaluation of the reflection coefficient, P. H. Smith developed a graphical procedure based on conformal mapping principles. This approach permits an easy and intuitive display of the reflection coefficient as well as the line impedance in one single graph.

**【中文注释】** 史密斯圆图（Smith Chart）是由P. H. Smith在1930年代发明的图形工具，用于直观地表示反射系数和传输线阻抗。它将复数阻抗平面通过共形映射变换到一个单位圆内，使得复杂的阻抗计算可以通过简单的旋转和读数完成。尽管现代计算机软件可以精确计算阻抗，但史密斯圆图仍然是射频工程师最直观的工具。

---

### 3.1.1 Reflection Coefficient in Phasor Form | 反射系数的相量形式

The **load reflection coefficient** $\Gamma_0$ at the load ($d = 0$):

$$\boxed{\Gamma_0 = \frac{Z_L - Z_0}{Z_L + Z_0} = |\Gamma_0| e^{j\theta_\Gamma}} \tag{3.1}$$

At a distance $d$ from the load (moving toward the source):

$$\boxed{\Gamma(d) = \Gamma_0 e^{-j2\beta d}} \tag{3.2}$$

**Special cases:**
- **Short circuit** ($Z_L = 0$): $\Gamma_0 = -1$ (point $-1 + j0$ on real axis)
- **Open circuit** ($Z_L \to \infty$): $\Gamma_0 = +1$ (point $+1 + j0$ on real axis)
- **Matched load** ($Z_L = Z_0$): $\Gamma_0 = 0$ (center of the chart)

**【中文注释】** 反射系数是一个复数量，其模表示反射波与入射波的幅度比，相角表示相位差。$\Gamma(d) = \Gamma_0 e^{-j2\beta d}$ 表明当波从负载向源端传播时，相角减少（顺时针旋转）——这是因为波需要"往返"两倍的距离才能从负载反射回观察点。

---

### Example 3-1: Reflection Coefficient Calculations | 例3-1：反射系数计算

For $Z_0 = 50\,\Omega$:

| Load $Z_L$ | $\Gamma_0$ | Location on $\Gamma$-plane |
|------------|-----------|---------------------------|
| $0$ (short) | $-1$ | Point $(-1, 0)$ |
| $\infty$ (open) | $+1$ | Point $(+1, 0)$ |
| $50\,\Omega$ (matched) | $0$ | Origin $(0, 0)$ |
| $16.67 - j16.67\,\Omega$ | $0.54\angle 221^\circ$ | Fourth quadrant |
| $50 + j150\,\Omega$ | $0.83\angle 34^\circ$ | First quadrant |

**【中文注释】** 从这个例子可以看出，反射系数的幅值$|\Gamma|$越大（越接近1），负载偏离匹配越远。复数负载的反射系数相位反映了负载阻抗的电抗性质——电感性负载（$+jX$）通常产生正相角（第一、四象限），而电容性负载（$-jX$）通常产生负相角（第二、三象限）。

---

### 3.1.2 Normalized Impedance Equation | 归一化阻抗方程

From (2.69), the input impedance at distance $d$:

$$Z_{\text{in}}(d) = Z_0 \frac{1 + \Gamma(d)}{1 - \Gamma(d)}$$

Normalizing with respect to $Z_0$: $z_{\text{in}} = Z_{\text{in}}/Z_0$, $z_L = Z_L/Z_0$:

$$\boxed{z_{\text{in}} = \frac{1 + \Gamma}{1 - \Gamma}} \tag{3.4}$$

**Inverse transformation:**

$$z_{\text{in}} = \frac{1 + \Gamma_r + j\Gamma_i}{1 - \Gamma_r - j\Gamma_i} = r + jx$$

Real and imaginary parts can be separated:

$$\boxed{r = \frac{1 - \Gamma_r^2 - \Gamma_i^2}{(1-\Gamma_r)^2 + \Gamma_i^2}} \tag{3.6}$$

$$\boxed{x = \frac{2\Gamma_i}{(1-\Gamma_r)^2 + \Gamma_i^2}} \tag{3.7}$$

**【中文注释】** 归一化阻抗 $z = Z/Z_0$ 是史密斯圆图的标准表示方式——实部$r$（归一化电阻）和虚部$x$（归一化电抗）都无量纲。这种归一化使得不同特性阻抗的系统可以在同一张图上进行分析。例如，50 Ω系统的$Z = 100 + j50$ 对应$r = 2$（即$2 \times 50 = 100$ Ω）。

---

### Parametric Circle Equations | 参数化圆方程

Inverting (3.6) and (3.7) yields circles in the $\Gamma$-plane:

**Constant normalized resistance $r$:**

$$\boxed{(\Gamma_r - \frac{r}{1+r})^2 + \Gamma_i^2 = \left(\frac{1}{1+r}\right)^2} \tag{3.10}$$

- Center: $(\frac{r}{1+r}, 0)$
- Radius: $\frac{1}{1+r}$

**Constant normalized reactance $x$:**

$$\boxed{(\Gamma_r - 1)^2 + (\Gamma_i - \frac{1}{x})^2 = \frac{1}{x^2}} \tag{3.11}$$

- Center: $(1, \frac{1}{x})$
- Radius: $|\frac{1}{x}|$

**【中文注释】** 公式(3.10)描述了归一化电阻$r$在反射系数复平面上的轨迹——是一族圆，圆心在实轴上（$\frac{r}{1+r}$, 0），半径为$\frac{1}{1+r}$。当$r = 0$时，圆心在原点、半径为1（即单位圆）；当$r = 1$时，圆心在(0.5, 0)、半径为0.5。公式(3.11)描述了归一化电抗$x$的轨迹——是一族圆，圆心在$(1, \frac{1}{x})$。

---

### 3.1.4 Graphical Representation | 图形表示

The **Smith Chart** is constructed by combining:
1. **Constant resistance circles** $r = \text{const}$ (from eq. 3.10)
2. **Constant reactance circles** $x = \text{const}$ (from eq. 3.11)
3. **Unit circle** $|\Gamma| = 1$ (boundary of passive region)

**Key properties:**
- **$r$ circles** are all tangent to the point $\Gamma = +1$ on the right of the real axis
- **$x$ circles** are all tangent to the point $\Gamma = +1$ as well, but are centered along a line perpendicular to the real axis
- **Normalized resistance** ranges: $0 \leq r < \infty$
- **Normalized reactance** ranges: $-\infty < x < +\infty$
- **Upper half** ($\Gamma_i > 0$): inductive reactances ($+jx$)
- **Lower half** ($\Gamma_i < 0$): capacitive reactances ($-jx$)
- **Right half** ($\Gamma_r > 0$): resistive parts $r > 1$
- **Left half** ($\Gamma_r < 0$): resistive parts $r < 1$

**Note on negative resistance:** $|\Gamma| > 1$ maps outside the unit circle (compressed Smith Chart). This occurs in oscillators where the device exhibits negative resistance. Not covered in this text.

**【中文注释】** 史密斯圆图是射频工程师最重要的图形工具。它将复杂的阻抗计算转化为简单的几何操作：
- 读取负载阻抗：找到$r$圆和$x$圆的交点
- 求反射系数：读出从原点到该点的矢量（长度= $|\Gamma|$，角度= $\theta_\Gamma$）
- 沿传输线移动：绕着单位圆顺时针旋转（因为$e^{-j2\beta d}$是负角度）
- 读取输入阻抗：旋转后的点对应新的$r$和$x$值

---

### Rotation on the Smith Chart | 史密斯圆图上的旋转

The rotation by $2\beta d = 2 \times (2\pi/\lambda) \times d = 4\pi d/\lambda$ is measured in the **clockwise direction** (negative mathematical angle) from the load toward the generator.

**Key relationship:** A complete revolution ($360^\circ$) corresponds to $d = \lambda/2$ (half-wavelength), because:

$$2\beta d = 2 \times \frac{2\pi}{\lambda} \times d = 4\pi \frac{d}{\lambda}$$

For $d = \lambda/2$: $4\pi \times (1/2) = 2\pi = 360^\circ$ → one full circle.

**Electrical length** $\theta = \beta d$ is often marked on the outer scale of the Smith Chart.

**【中文注释】** 在史密斯圆图上，每顺时针旋转半波长（$\lambda/2$）就会回到同一点——这是传输线阻抗周期性的体现。因此在史密斯圆图上，$\lambda/4$对应180°旋转，$\lambda/2$对应360°（完整一圈）。

---

## 3.2 Impedance Transformation | 阻抗变换

### 6-Step Smith Chart Procedure | 六步操作流程

To find the input impedance of a transmission line terminated with load $Z_L$:

| Step | Action |
|------|--------|
| 1 | Normalize: $z_L = Z_L/Z_0$ |
| 2 | Locate $z_L$ on Smith Chart (intersection of $r$ and $x$ circles) |
| 3 | Read $\Gamma_0 = |\Gamma|e^{j\theta}$ from the radial scale |
| 4 | Rotate $\Gamma_0$ by $2\beta d$ clockwise toward generator |
| 5 | Read normalized $z_{\text{in}}$ at the rotated point |
| 6 | Denormalize: $Z_{\text{in}} = z_{\text{in}} \times Z_0$ |

**【中文注释】** 这个六步流程是使用史密斯圆图的基本方法。在实际工程中，通常使用矢量网络分析仪（VNA）直接测量$S_{11}$并显示在史密斯圆图上，但理解手动旋转的过程对于掌握传输线理论至关重要。

---

### Example 3-3: Using the Smith Chart | 例3-3：使用史密斯圆图

**Problem:** Find input impedance of $Z_L = (30 + j60)\,\Omega$ on a $50\,\Omega$ line, $d = 2$ cm, $f = 2$ GHz, $v_p = 0.5c$.

**Solution:**

1. $z_L = 30/50 + j60/50 = 0.6 + j1.2$
2. Locate intersection of $r = 0.6$ circle and $x = 1.2$ circle (Fig 3-5)
3. Read $\Gamma_0 \approx 0.72\angle 115^\circ$
4. Compute $\beta = \omega\sqrt{\mu\varepsilon} = \omega\sqrt{\varepsilon_r}/c$; $v_p = 0.5c \Rightarrow \lambda = c/(0.5f) = 7.5$ cm; $\beta d = (2\pi/\lambda) \times 2 = 96^\circ$; $2\beta d = 192^\circ$ clockwise
5. Rotate $192^\circ$ clockwise from $\Gamma_0$ → find $z_{\text{in}} \approx 0.3 - j0.53$
6. $Z_{\text{in}} \approx (15 - j26.5)\,\Omega$

**Exact solution from formula:** $Z_{\text{in}} = (14.7 - j26.7)\,\Omega$. Small difference due to graphical approximation.

**【中文注释】** 这个例子展示了使用史密斯圆图进行阻抗计算的全过程。注意在计算电长度$\beta d$时，需要考虑相速度$v_p$——如果$v_p \neq c$，则波长$\lambda = v_p/f$会相应缩短。在实际微带线中，$v_p$通常介于$c$和$c/\sqrt{\varepsilon_r}$之间，取决于微带线的有效介电常数。

---

## 3.2.2 Standing Wave Ratio | 驻波比

From Section 2.8.3, the VSWR at distance $d$:

$$\boxed{\text{VSWR} = \frac{1 + |\Gamma(d)|}{1 - |\Gamma(d)|}} \tag{3.12}$$

On the Smith Chart, **VSWR circles** are circles centered at the origin with radius $|\Gamma|$. The VSWR value is read at the intersection of the $|\Gamma|$ circle with the positive real axis (where $\Gamma_i = 0$, $\Gamma_r = |\Gamma|$).

**Special cases:**
- VSWR = 1: $|\Gamma| = 0$ → matched condition (origin)
- VSWR → $\infty$: $|\Gamma| \to 1$ → short or open circuit (point at $\Gamma = \pm 1$)

**【中文注释】** VSWR圆是以原点为圆心的同心圆——所有与原点距离相同的点具有相同的VSWR。例如，VSWR = 2 对应 $|\Gamma| = 1/3 \approx 0.333$的圆。在工程中，通常要求VSWR ≤ 2（对应回波损耗≥ 9.5 dB），更好的系统要求VSWR ≤ 1.5（RL ≥ 13.5 dB）。

---

### Example 3-4: VSWR and Return Loss | 例3-4：驻波比与回波损耗

For $Z_0 = 50\,\Omega$, given four loads:

| Load $Z_L$ | $\Gamma_0$ | VSWR | Return Loss |
|------------|-----------|------|-------------|
| (a) $50\,\Omega$ | $0$ | $1$ | $\infty$ dB |
| (b) $48.5\,\Omega$ | $-0.015$ | $1.03$ | $36.5$ dB |
| (c) $75 + j25\,\Omega$ | $0.33\angle 30^\circ$ | $2.0$ | $9.5$ dB |
| (d) $20 - j60\,\Omega$ | $0.74\angle -50^\circ$ | $6.7$ | $2.6$ dB |

**Interpretation:** Load (a) is perfectly matched. Load (b) is nearly matched (36.5 dB RL excellent for most applications). Load (c) has moderate mismatch (9.5 dB RL, VSWR = 2.0). Load (d) is severely mismatched (2.6 dB RL, VSWR = 6.7 — only 54% of power is delivered to the load).

**【中文注释】** 回波损耗（Return Loss）和VSWR是衡量匹配质量的两个互补指标。当负载完全不匹配（开路或短路）时，VSWR → ∞，RL = 0 dB；当完全匹配时，VSWR = 1，RL → ∞。工程中常见的规格：VSWR ≤ 2（RL ≥ 9.5 dB）是一般要求；VSWR ≤ 1.2（RL ≥ 20.8 dB）用于精密测量系统。

---

## Advanced Smith Chart Operations | 史密斯圆图进阶操作

### Series and Parallel Elements | 串联和并联元件

**Adding a series element:** On the Smith Chart, adding a series $Z = R + jX$ corresponds to adding $X$ to the normalized reactance $x$ while keeping $r$ constant. This means **moving vertically** (along the constant-$r$ circle).

**Adding a parallel element:** Normalize the load admittance $Y_L = 1/Z_L$. On the admittance Smith Chart (rotated 180° from impedance), adding a shunt admittance corresponds to **moving horizontally** (along constant-$g$ circle).

**【中文注释】** 在史密斯圆图上，串联元件导致沿着等电阻圆移动（$r$不变，$x$变化）；并联元件导致沿着等电导圆移动（$g$不变，$b$变化）。因此，在设计匹配网络时，经常需要在阻抗图和导纳图之间切换（旋转180°）来简化某些操作。

---

### Stub Tuning | 短截线调谐

Stub tuning uses **shunt (or series) shorted or open transmission line segments** to provide reactive tuning elements.

**Single-stub tuner:** A shunt stub placed at a specific position along the main line. Two unknowns (stub position $d_1$, stub length $d_2$) can be solved to match any load.

**Double-stub tuner:** Two stubs at fixed positions provide more flexible matching, less sensitive to frequency.

**Smith Chart procedure for single-stub:**
1. Normalize $z_L$ → locate on chart
2. Rotate to a point where the admittance $y = 1/z$ has $g = 1$ (real part = 1)
3. Read required $b$ (imaginary part) → determines stub length
4. The rotation angle gives the stub position

**【中文注释】** 短截线调谐是射频匹配中最经典的技术之一。通过在主线上的适当位置并联一个短路或开路短截线，可以将任意负载阻抗变换到主线需要的输入阻抗。短路短截线的长度为$\lambda/8$到$\lambda/4$时提供感性电抗，开路短截线提供容性电抗。这种技术无需集总元件，特别适合微带电路。

---

### Quality Factor Q Circles | 品质因数圆

The **unloaded Q** of a resonant circuit can be represented as circles of constant Q on the Smith Chart:

$$Q = \frac{|x|}{r} = \frac{|\Gamma_i|}{|\Gamma_r - \frac{r}{1+r}|}$$

Constant-$Q$ circles are centered along the real axis, passing through the origin. **High-Q** resonances cluster near the real axis extremes (short or open); **low-Q** resonances are near the center (matched condition).

**【中文注释】** Q圆在滤波器设计中非常重要。高Q值（$Q > 10$）的谐振电路在史密斯圆图上表现为靠近实轴（纯电阻）末端的点——这意味着该电路选择性很强但带宽很窄。低Q值（$Q < 3$）的电路带宽更宽但选择性更差。在设计窄带滤波器时，需要使用高Q值的谐振器。

---

## Summary | 本章小结

### Key Concepts | 核心概念

1. **Reflection coefficient** $\Gamma = (Z_L - Z_0)/(Z_L + Z_0)$ is the fundamental parameter for analyzing mismatched lines
2. **Smith Chart** is a conformal map of the normalized impedance plane onto the unit circle in the complex $\Gamma$-plane
3. **Constant-$r$ circles** and **constant-$x$ circles** form the grid of the Smith Chart
4. **Rotation on the chart** by $2\beta d$ clockwise corresponds to moving toward the generator by distance $d$
5. **VSWR circles** are concentric circles centered at the origin; VSWR is read at the intersection with the positive real axis
6. **Stub tuning** uses shorted or open transmission line segments as reactive elements for impedance matching
7. **Normalized quantities** ($z = Z/Z_0$, $y = Y/Z_0$) make the Smith Chart independent of specific $Z_0$ values

### Key Equations | 核心公式

$$\boxed{\Gamma_0 = \frac{Z_L - Z_0}{Z_L + Z_0}}$$

$$\boxed{\Gamma(d) = \Gamma_0 e^{-j2\beta d}}$$

$$\boxed{z_{\text{in}} = \frac{1 + \Gamma}{1 - \Gamma}}$$

$$\boxed{r = \frac{1 - \Gamma_r^2 - \Gamma_i^2}{(1-\Gamma_r)^2 + \Gamma_i^2}}$$

$$\boxed{x = \frac{2\Gamma_i}{(1-\Gamma_r)^2 + \Gamma_i^2}}$$

$$\boxed{\text{VSWR} = \frac{1 + |\Gamma|}{1 - |\Gamma|}}$$

$$\boxed{\text{RL} = -20\log_{10}|\Gamma| \text{ [dB]}}$$

**【中文注释】** 史密斯圆图将复杂的复数阻抗计算转化为几何操作：找到点、旋转、读数。这种图形化方法不仅让计算更直观，也帮助工程师建立对射频行为的物理直觉——为什么阻抗随频率变化？为何某些位置阻抗特别高或低？史密斯圆图给出了清晰的视觉答案。
---
chapter: 5
title: Cylindrical Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 199-290
---

# Chapter 5: Cylindrical Wave Functions / 柱面波函数

## Section 5-1: The Wave Functions / 波动函数

**English:**

In **cylindrical coordinates** $(\rho, \phi, z)$, the scalar Helmholtz equation is:

$$\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho\frac{\partial\psi}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2} + \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{5-1}$$

Using **separation of variables** $\psi(\rho, \phi, z) = R(\rho)\Phi(\phi)Z(z)$:

$$\frac{1}{R}\frac{d}{d\rho}\left(\rho\frac{dR}{d\rho}\right) + \frac{1}{\rho^2\Phi}\frac{d^2\Phi}{d\phi^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} + k^2 = 0$$

This yields three equations:
1. **Z-equation:** $\frac{d^2Z}{dz^2} + k_z^2 Z = 0$ → $Z = e^{\pm jk_z z}$
2. **$\Phi$-equation:** $\frac{d^2\Phi}{d\phi^2} + n^2\Phi = 0$ → $\Phi = e^{jn\phi}$ ($n$ integer for single-valuedness)
3. **R-equation:** $\frac{d^2R}{d\rho^2} + \frac{1}{\rho}\frac{dR}{d\rho} + (k_\rho^2 - \frac{n^2}{\rho^2})R = 0$ → **Bessel's equation**

**Bessel's equation** of order $n$:
$$\rho^2\frac{d^2R}{d\rho^2} + \rho\frac{dR}{d\rho} + (k_\rho^2\rho^2 - n^2)R = 0 \tag{5-5}$$

**Solutions to Bessel's equation:**
$$R = B_1 J_n(k_\rho\rho) + B_2 N_n(k_\rho\rho) \quad \text{(bounded at origin)}$$
$$R = B_3 H_n^{(1)}(k_\rho\rho) + B_4 H_n^{(2)}(k_\rho\rho) \quad \text{(radiation condition)}$$

where:
- $J_n$ = **Bessel function of first kind** (finite at $\rho = 0$)
- $N_n$ = **Bessel function of second kind** (singular at $\rho = 0$)
- $H_n^{(1)}$ = **Hankel function of first kind** (outgoing waves as $\rho \to \infty$)
- $H_n^{(2)}$ = **Hankel function of second kind** (incoming waves as $\rho \to \infty$)

**Separation constant relation:**
$$k_\rho^2 + k_z^2 = k^2 \tag{5-6}$$

**Elementary wave functions:**
$$\psi_{nmp}(\rho, \phi, z) = B_n(k_\rho\rho)e^{jn\phi}h_p(k_z z) \tag{5-9}$$

**Modified Bessel functions** for evanescent ($\gamma$) waves:
$$I_n(x) = j^{-n} J_n(jx) \quad K_n(x) = \text{modified } N_n(x)$$

**Asymptotic behavior:**

For large $x$:
$$J_n(x) \approx \sqrt{\frac{2}{\pi x}}\cos\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right)$$
$$H_n^{(2)}(x) \approx \sqrt{\frac{2}{\pi x}}e^{-j\left(x - \frac{n\pi}{2} - \frac{\pi}{4}\right)}$$

**Bessel function identities:**
$$J_{-n}(x) = (-1)^n J_n(x)$$
$$H_{-n}^{(2)}(x) = (-1)^n H_n^{(2)}(x)$$

**中文：**

在**圆柱坐标系** $(\rho, \phi, z)$ 中，标量亥姆霍兹方程为：
$$\frac{1}{\rho}\frac{\partial}{\partial\rho}\left(\rho\frac{\partial\psi}{\partial\rho}\right) + \frac{1}{\rho^2}\frac{\partial^2\psi}{\partial\phi^2} + \frac{\partial^2\psi}{\partial z^2} + k^2\psi = 0 \tag{5-1}$$

分离变量 $\psi(\rho, \phi, z) = R(\rho)\Phi(\phi)Z(z)$ 得到三个方程，其中 $R$-方程为**贝塞尔方程**：
$$\rho^2\frac{d^2R}{d\rho^2} + \rho\frac{dR}{d\rho} + (k_\rho^2\rho^2 - n^2)R = 0 \tag{5-5}$$

**贝塞尔方程的解：**
$$R = B_1 J_n(k_\rho\rho) + B_2 N_n(k_\rho\rho) \quad \text{（有界于原点）}$$

其中：
- $J_n$ = **第一类贝塞尔函数**（在 $\rho = 0$ 处有限）
- $N_n$ = **第二类贝塞尔函数**（在 $\rho = 0$ 处奇异）
- $H_n^{(1)}$ = **第一类汉克尔函数**（外向波）
- $H_n^{(2)}$ = **第二类汉克尔函数**（内向波）

---

## Section 5-2: Circular Waveguides (Cylindrical) / 圆形波导（柱面）

**English:**

**Circular cylindrical waveguide** of radius $a$ supports TE and TM modes.

**TE modes** ($E_z = 0$, $H_z \neq 0$):
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n'(x) = 0$.

**TM modes** ($H_z = 0$, $E_z \neq 0$):
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n(x) = 0$.

**Characteristic roots:**

| Mode | Root equation | $p_{nm}$ example |
|------|-------------|-----------------|
| TE$_{nm}$ | $J_n'(p_{nm}) = 0$ | $p_{01} = 3.832$ |
| TM$_{nm}$ | $J_n(p_{nm}) = 0$ | $p_{01} = 2.405$ |

**Dominant circular waveguide mode:** TE11 ($p_{11} = 1.841$)

**Cutoff frequency:**
$$f_c = \frac{p_{nm}}{2\pi a\sqrt{\mu\epsilon}}$$

**Attenuation constants:**
$$\alpha_c \approx \frac{R_s}{a\eta}\left(1 + \frac{n^2}{p_{nm}^2 - n^2}\right) \quad \text{(TE)}$$
$$\alpha_c \approx \frac{R_s}{a\eta} \quad \text{(TM)}$$

**Polarization degeneracy:** For circular waveguide with $n \neq 0$, modes have two orthogonal polarizations ($\cos n\phi$ and $\sin n\phi$) with same cutoff.

**中文：**

半径为 $a$ 的**圆形柱面波导**支持 TE 和 TM 模式。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

其中 $p_{nm}$ 是 $J_n'(x) = 0$ 的第 $m$ 个根。

**主圆形波导模式：** TE11 ($p_{11} = 1.841$)

**极化简并：** 对于 $n \neq 0$，模式具有两个正交极化（$\cos n\phi$ 和 $\sin n\phi$），截止频率相同。

---

## Section 5-3: Circular Cavity Resonators / 圆形腔体谐振器

**English:**

A **circular cylindrical cavity** of radius $a$ and height $d$ has resonant modes.

**Resonant frequencies:**
$$f_{nmp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{p_{nm}}{a}\right)^2 + \left(\frac{q\pi}{d}\right)^2}$$

where $p_{nm}$ is the root of Bessel function (TM or TE), and $q$ is the axial mode number.

**TM modes in circular cavity:**
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)\cos\left(\frac{q\pi z}{d}\right)e^{jn\phi}$$

**TE modes in circular cavity:**
$$H_z = H_0 J_n\left(\frac{p_{nm}'\rho}{a}\right)\sin\left(\frac{q\pi z}{d}\right)e^{jn\phi}$$

where $p_{nm}'$ is the root of $J_n'(x) = 0$.

**Quality factor Q:**

For conducting walls with conductivity $\sigma$:
$$Q = \frac{\omega W}{P_\text{loss}}$$

where $W$ is stored energy and $P_\text{loss}$ is power dissipated in walls.

For circular cavity TM modes:
$$Q_{nmq} \approx \frac{(p_{nm})^2 a}{2R_s\delta_s\left(p_{nm}^2 + \left(\frac{n\pi a}{d}\right)^2\right)}$$

where $R_s = \sqrt{\omega\mu/(2\sigma)}$ is the surface resistance and $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ is the skin depth.

**Dominant mode of circular cavity:** TM010 ($f \approx 1.203c/(2a)$, $Q \approx 2.05a/\delta_s$)

**TM011:** Useful for dielectric resonator measurements (high Q, electric field concentrated in dielectric sample).

**中文：**

半径 $a$ 和高度 $d$ 的**圆形柱面腔体**具有谐振模式。

**谐振频率：**
$$f_{nmp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{p_{nm}}{a}\right)^2 + \left(\frac{q\pi}{d}\right)^2}$$

**品质因数 Q：**

对于导电壁：
$$Q = \frac{\omega W}{P_\text{loss}}$$

**圆形腔的主模式：** TM010 ($f \approx 1.203c/(2a)$)

---

## Section 5-4: Aperture Coupling and Slot Antennas / 孔耦合与缝隙天线

**English:**

**Aperture coupling** through a small hole in a conducting wall can be analyzed using **equivalence principle**.

**Babinet principle:** The fields from a complementary screen (aperture replaced by obstacle and vice versa) are related.

For a slot of length $L$ in a conducting plane, the complementary structure is a thin dipole of length $L$.

**Radiation from narrow slot:**
For a narrow slot of width $w \ll L$ and length $L \approx \lambda/2$:
$$E_z \approx \frac{V}{w} \sin\left(\frac{\pi z}{L}\right) \quad (|z| < L/2)$$

The magnetic current on the slot is:
$$M_s = -2\hat{n} \times E_\text{slot}$$

**Half-wave slot antenna:** $L = \lambda/2$, radiation pattern similar to dipole but with orthogonal polarization.

**Resonant slot:** At resonance, input conductance $G \approx 0.32$ S for narrow transverse slots in X-band waveguide.

**Radiating waveguide slots:** Slots cut in waveguide walls to couple power. Condition for radiation: slot must cut current path on waveguide surface.

**Longitudinal shunt slot:** Equivalent to series R-L branch.
**Transverse shunt slot:** Equivalent to shunt R-L branch.

**中文：**

**孔耦合**通过导电壁上的小孔，可以使用**等效原理**分析。

**巴比涅原理：** 互补屏幕（孔与障碍物互换）的场相互关联。

对于长度为 $L$ 的缝隙，互补结构是长度为 $L$ 的细偶极子。

**窄缝辐射：**
$$E_z \approx \frac{V}{w} \sin\left(\frac{\pi z}{L}\right) \quad (|z| < L/2)$$

---


---

## Section 5-5: Dielectric Rod Waveguide / 介质杆波导

**English:**

A **dielectric rod** can guide waves using total internal reflection, similar to optical fibers.

**Step-index circular rod:** Core of radius $a$, index $n_1$, surrounded by cladding $n_2 < n_1$.

**Guided modes:** For weak guidance ($n_1 \\approx n_2$), HE modes with approximate field distributions.

**Scalar wave equation** for the rod:
$$\\frac{d^2\\psi}{dr^2} + \\frac{1}{r}\\frac{d\\psi}{dr} + (k_0^2 n^2(r) - \\beta^2 - \\frac{n^2}{r^2})\\psi = 0$$

**V-number** for step-index fiber:
$$V = k_0 a \\sqrt{n_1^2 - n_2^2} = \\frac{2\\pi a}{\\lambda_0}\\sqrt{n_1^2 - n_2^2}$$

**Number of guided modes:**
- Single-mode condition: $V < 2.405$
- Multi-mode: approximately $M \\approx V^2/2$ for large $V$

**Hybrid modes in circular fiber:**
- **HE$_{nm}$**: Predominantly electric field axial component
- **EH$_{nm}$**: Predominantly magnetic field axial component
- **TE$_{0m}$**, **TM$_{0m}$**: Circularly symmetric modes

**Bessel function solutions:** Inside the rod, $J_n(u\\rho/a)$ is used. Outside, modified Bessel $K_n(w\\rho/a)$ for evanescent decay.

**Characteristic equation** for HE modes:
$$\\frac{uJ_{n-1}(u)}{J_n(u)} = \\frac{w K_{n-1}(w)}{K_n(w)}$$

where:
$$u^2 = a^2(k_0^2 n_1^2 - \\beta^2)$$
$$w^2 = a^2(\\beta^2 - k_0^2 n_2^2)$$

**Attenuation in dielectric waveguides:** Due to dielectric loss ($\\tan\\delta$):

$$\\alpha_d = \\frac{k_0 n_1 \\sin^2\\theta_m}{2\\beta}\\tan\\delta$$

where $\\theta_m$ is the mode angle with respect to the axis.

**中文：**

**介质杆**可以使用全内反射导波，类似于光纤。

**阶跃折射率圆杆：** 半径 $a$，折射率 $n_1$，被 $n_2 < n_1$ 的包层包围。

**导模：** 对于弱导 ($n_1 \\approx n_2$)，使用 HE 模式。

**V数**（阶跃光纤）：
$$V = k_0 a \\sqrt{n_1^2 - n_2^2} = \\frac{2\\pi a}{\\lambda_0}\\sqrt{n_1^2 - n_2^2}$$

**导模数量：**
- 单模条件：$V < 2.405$
- 多模：大约 $M \\approx V^2/2$

**特征方程（HE模式）：**
$$\\frac{uJ_{n-1}(u)}{J_n(u)} = \\frac{w K_{n-1}(w)}{K_n(w)}$$

---

## Section 5-6: Cylindrical Waveguide Coupling / 柱面波导耦合

**English:**

**Mode coupling** in cylindrical waveguides occurs at discontinuities and bends.

**Coupled-mode theory:** For two weakly coupled waveguides:

$$\\frac{da_1}{dz} = -j\\beta_1 a_1 + jC_{12} a_2$$
$$\\frac{da_2}{dz} = -j\\beta_2 a_2 + jC_{21} a_1$$

where $C_{ij}$ is the coupling coefficient.

**Synchronous coupling:** When $\\beta_1 = \\beta_2$, maximum power exchange occurs over the **coupling length**:
$$L_c = \\frac{\\pi}{2|C|}$$

**Directional coupler:** Two parallel waveguides coupled over a length $L$. Power transfer:

$$P_2(L) = P_1(0)\\sin^2(|C|L)$$

**Straight directional coupler:** For weak coupling, $P_2/P_1 = (\\pi/2)(L/L_c)^2$ when $L \\ll L_c$.

**Overcoupled regime:** Maximum coupling occurs at $L = L_c/2$, where complete power transfer is possible.

**Bend coupling:** In curved waveguides, mode conversion occurs due to curvature. Power radiates at a rate:

$$\\alpha_\\text{bend} \\approx \\frac{1}{2R}\\left(\\frac{\\lambda}{a}\\right)^2$$

for $a \\gg \\lambda$ and radius $R$.

**Transition radiation:** Due to gradual or sudden changes in waveguide dimensions.

**中文：**

**模式耦合**发生在不连续性和弯头处。

**耦合模理论：** 对于两个弱耦合波导：

$$\\frac{da_1}{dz} = -j\\beta_1 a_1 + jC_{12} a_2$$
$$\\frac{da_2}{dz} = -j\\beta_2 a_2 + jC_{21} a_1$$

**同步耦合：** 当 $\\beta_1 = \\beta_2$ 时，最大功率交换发生在**耦合长度**：
$$L_c = \\frac{\\pi}{2|C|}$$

**定向耦合器：** 两个平行波导在长度 $L$ 上耦合。

---

## Section 5-7: Cylindrical Cavity Filters / 柱面腔体滤波器

**English:**

**Cylindrical cavity filters** use resonant modes in cylindrical cavities to create band-pass or band-stop filters.

**TM010 mode** in circular waveguide (closed at both ends):
$$f_c = \\frac{1.203c}{2\\pi a} = \\frac{1.203}{2\\pi a\\sqrt{\\mu\\epsilon}}$$

**Iris-coupled cylindrical cavities:** Coupling iris between cavities controls coupling coefficient.

**Coupling coefficient for iris:**
$$k = \\frac{\\omega L}{2} \\quad \\text{(for inductive iris)}$$

where $L$ is the normalized iris reactance.

**Filter synthesis using cylindrical cavities:**

1. **Chebyshev filter:** Equal ripple passband, specified return loss
2. **Cavity Q:** $Q_c = \\omega W/P_\\text{loss}$ (conductor dominated)
3. **External Q:** $Q_e = g_0 g_1/FBW$ for input/output coupling

**Dual-mode cylindrical cavities:** Each cavity supports two orthogonal modes that can be coupled to form a 4-pole filter without extra cavities.

**Tuning:** Cylindrical cavities have screw tuners for fine adjustment of resonant frequency.

**Temperature stability:** Cavity filters have excellent temperature stability when made of low-expansion materials (Invar, superinvar).

**中文：**

**柱面腔体滤波器**使用柱面腔中的谐振模式来创建带通或带阻滤波器。

**TM010模式**在圆波导中（两端封闭）：
$$f_c = \\frac{1.203c}{2\\pi a}$$

**iris耦合柱面腔体：** 腔体之间的耦合iris控制耦合系数。

**滤波器综合：** 
1. **切比雪夫滤波器：** 等纹波通带，指定回波损耗
2. **腔体Q：** $Q_c = \\omega W/P_\\text{loss}$（由导体损耗主导）
3. **外部Q：** $Q_e = g_0 g_1/FBW$ 用于输入/输出耦合

---


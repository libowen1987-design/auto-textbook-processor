---
chapter: 6
title: Spherical Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 299-380
---

# Chapter 6: Spherical Wave Functions / 球面波函数

## Section 6-1: The Wave Functions / 波动函数

**English:**

In **spherical coordinates** $(r, \theta, \phi)$, the scalar Helmholtz equation is:

$$\frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\frac{\partial\psi}{\partial r}\right) + \frac{1}{r^2\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial\psi}{\partial\theta}\right) + \frac{1}{r^2\sin^2\theta}\frac{\partial^2\psi}{\partial\phi^2} + k^2\psi = 0$$

Using **separation of variables** $\psi(r, \theta, \phi) = R(r)\Theta(\theta)\Phi(\phi)$:

**Spherical Bessel equation** for $R(r)$:
$$r^2\frac{d^2R}{dr^2} + 2r\frac{dR}{dr} + [k^2r^2 - n(n+1)]R = 0$$

**Solutions — Spherical Bessel functions:**
$$j_n(kr) = \sqrt{\frac{\pi}{2kr}} J_{n+1/2}(kr) \quad \text{(spherical Bessel of 1st kind)}$$
$$n_n(kr) = \sqrt{\frac{\pi}{2kr}} N_{n+1/2}(kr) \quad \text{(spherical Bessel of 2nd kind)}$$
$$h_n^{(1)}(kr) = j_n(kr) + jn_n(kr) \quad \text{(spherical Hankel of 1st kind)}$$
$$h_n^{(2)}(kr) = j_n(kr) - jn_n(kr) \quad \text{(spherical Hankel of 2nd kind)}$$

**Associated Legendre equation** for $\Theta(\theta)$:
$$\frac{1}{\sin\theta}\frac{d}{d\theta}\left(\sin\theta\frac{d\Theta}{d\theta}\right) + \left[n(n+1) - \frac{m^2}{\sin^2\theta}\right]\Theta = 0$$

**Solutions — Associated Legendre functions:**
$$\Theta = P_n^m(\cos\theta), \quad \Phi = e^{jm\phi}$$

where $P_n^m$ is the **associated Legendre function** of degree $n$ and order $m$.

**Elementary spherical wave functions:**
$$\psi_{emn}(r, \theta, \phi) = h_n^{(1)}(kr)Y_n^m(\theta, \phi) \quad \text{(outgoing spherical wave)}$$
$$\psi_{smn}(r, \theta, \phi) = j_n(kr)Y_n^m(\theta, \phi) \quad \text{(standing spherical wave)}$$

where $Y_n^m(\theta, \phi) = P_n^m(\cos\theta)e^{jm\phi}$ is the **spherical harmonic**.

**Spherical wave expansion of plane wave:**
$$e^{-jkz} = \sum_{n=0}^{\infty} (-1)^n (2n+1) j_n(kr) P_n(\cos\theta)$$

**中文：**

在**球坐标系** $(r, \theta, \phi)$ 中，标量亥姆霍兹方程分离变量得到：

**球贝塞尔方程**：
$$r^2\frac{d^2R}{dr^2} + 2r\frac{dR}{dr} + [k^2r^2 - n(n+1)]R = 0$$

**解 — 球贝塞尔函数：**
$$j_n(kr) = \sqrt{\frac{\pi}{2kr}} J_{n+1/2}(kr) \quad \text{（第一类球贝塞尔）}$$
$$n_n(kr) = \sqrt{\frac{\pi}{2kr}} N_{n+1/2}(kr) \quad \text{（第二类球贝塞尔）}$$
$$h_n^{(1)}(kr) = j_n(kr) + jn_n(kr) \quad \text{（第一类球汉克尔）}$$

**球谐函数**：
$$Y_n^m(\theta, \phi) = P_n^m(\cos\theta)e^{jm\phi}$$

---

## Section 6-2: Spherical Waveguide / 球面波导

**English:**

**Spherical waveguides** have boundaries at $r = a$ (concentric spherical shells).

**Field representations:**

For TM modes ($E_r \neq 0$, $H_r = 0$):
$$E_r = \frac{1}{r^2}\frac{d}{dr}[rh_n^{(1)}(kr)]\Theta(\theta)\Phi(\phi)$$

For TE modes ($H_r \neq 0$, $E_r = 0$):
$$H_r = \frac{n(n+1)}{r^2} h_n^{(1)}(kr) P_n^m(\cos\theta)e^{jm\phi}$$

**Boundary condition** at perfectly conducting spherical shell $r = a$:
- TE modes: $\frac{\partial}{\partial r}[rh_n^{(1)}(kr)] = 0$ at $r = a$
- TM modes: $h_n^{(1)}(ka) = 0$ at $r = a$

**Spherical cavity resonator:** Conducting spherical shell at $r = a$.

TM mode resonances:
$$j_n(k_{nm}a) = 0 \Rightarrow k_{nm}a = p_{nm} \quad (p_{nm} = \text{zero of } J_{n+1/2})$$

TE mode resonances:
$$\frac{d}{dr}[rh_n^{(1)}(kr)] = 0 \text{ at } r = a$$

**Quality factor of spherical cavity:**
$$Q_{nmp} \approx \frac{\delta_s}{a} \frac{n(n+1)}{2n+1}$$

**Dominant mode (TE101-like spherical):** Lowest Q mode.

**TE modes** have no field singularities at $r = 0$ (finite for all $n \geq 1$).
**TM modes** have $E_r \to \infty$ at $r = 0$ for $n \geq 1$ (except $n=0$).

**中文：**

**球面波导**在 $r = a$ 处有边界（同心球壳）。

**球形腔体谐振器：** 导电球壳在 $r = a$ 处。

TM模式谐振：
$$j_n(k_{nm}a) = 0 \Rightarrow k_{nm}a = p_{nm}$$

---

## Section 6-3: Spherical Cavities and Mie Scattering / 球形腔体与米氏散射

**English:**

**Mie scattering** is the exact solution for scattering by a homogeneous sphere of radius $a$.

**Total field decomposition:**

**Incident field** (plane wave along $z$-axis):
$$\mathbf{E}^i = \hat{x}E_0 e^{-jkr\cos\theta} = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[j_n(kr)\hat{\theta} \cdot \mathbf{M}_{o1n} - \frac{1}{k}\frac{d}{dr}(kr j_n(kr))\hat{\phi} \cdot \mathbf{N}_{e1n}]$$

**Scattered field** (outgoing spherical waves):
$$\mathbf{E}^s = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[a_n j_n(kr) + b_n h_n^{(1)}(kr)]\mathbf{M}_{o1n} + [b_n j_n(kr) + a_n h_n^{(1)}(kr)]\mathbf{N}_{e1n}$$

**Internal field** (inside sphere):
$$\mathbf{E}^\text{int} = E_0 \sum_{n=1}^{\infty} c_n j_n(k_1 r)\mathbf{M}_{o1n} + d_n j_n(k_1 r)\mathbf{N}_{e1n}$$

where $k_1 = \omega\sqrt{\mu_1\epsilon_1}$.

**Scattering coefficients $a_n, b_n$:**

For a sphere with refractive index $m = n_1/n_2$:
$$a_n = \frac{jn_n(x) - mx h_n^{(2)}(mx)}{jn_n(x) - mx h_n^{(2)}(mx)} \quad \text{(TM modes)}$$
$$b_n = \frac{[mx j_n(mx)]' - nj_n(x)}{[mx h_n^{(2)}(mx)]' - nh_n^{(2)}(x)} \quad \text{(TE modes)}$$

where $x = ka$ is the **size parameter**.

**Optical efficiency factors:**

**Extinction efficiency:**
$$Q_\text{ext} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)\text{Re}\{a_n + b_n\}$$

**Scattering efficiency:**
$$Q_\text{sca} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)(|a_n|^2 + |b_n|^2)$$

**Absorption efficiency:**
$$Q_\text{abs} = Q_\text{ext} - Q_\text{sca}$$

**Asymptotic limits:**

- **Rayleigh scattering** ($x \ll 1$): $Q_\text{sca} \propto x^4$, $\sigma \propto 1/\lambda^4$
- **Mie regime** ($x \sim 1$): Complex resonance structure
- **Geometric optics** ($x \gg 1$): $Q_\text{sca} \to 2$ (extinction = 2 × geometric cross-section due to shadow)

**Forward scattering (Mie):** Sharp forward peak at large $x$.

**Rainbow angle:** For water droplets ($n \approx 1.333$), rainbow occurs at $\theta \approx 138°$.

**Resonant modes (Mie resonances):** Sphere acts as a dielectric resonator, supporting resonances at specific $x$ values.

**中文：**

**米氏散射**是球形均匀散射体的精确解。

**总场分解：**

**入射场**（沿 $z$ 轴的平面波）：
$$\mathbf{E}^i = E_0 e^{-jkz}\hat{x}$$

**散射场**（外向球面波）：
$$\mathbf{E}^s = E_0 \sum_{n=1}^{\infty} \frac{2n+1}{n(n+1)}[a_n \mathbf{M}_{o1n} + b_n \mathbf{N}_{e1n}]h_n^{(1)}(kr)$$

**散射系数 $a_n, b_n$：**

对于折射率 $m = n_1/n_2$ 的球体：
$$a_n = \frac{jn_n(x) - mx h_n^{(2)}(mx)}{...} \quad \text{（TM模式）}$$

其中 $x = ka$ 是**尺寸参数**。

**光学效率因子：**

**消光效率：**
$$Q_\text{ext} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)\text{Re}\{a_n + b_n\}$$

**散射效率：**
$$Q_\text{sca} = \frac{2}{x^2}\sum_{n=1}^{\infty}(2n+1)(|a_n|^2 + |b_n|^2)$$

**极限情况：**

- **瑞利散射** ($x \ll 1$): $Q_\text{sca} \propto x^4$
- **米氏区** ($x \sim 1$): 复杂共振结构
- **几何光学** ($x \gg 1$): $Q_\text{sca} \to 2$

---


---

## Section 6-4: Spherical Antenna Theory / 球面天线理论

**English:**

**Spherical waves** are the natural solution for radiation and scattering problems involving spherical geometry.

**Expansion of plane wave in spherical waves:**
$$e^{-jk\\hat{r}\\cdot\\mathbf{r}_0} = \\sum_{n=0}^{\\infty} (2n+1)(-j)^n j_n(kr_0) P_n(\\cos\\theta)$$

where $r_0$ is the distance from origin to source point.

**Dipole radiation patterns:**
For a small dipole (Hertzian dipole) of length $l$ and current $I_0$:

$$\\mathbf{E}_\\theta = \\frac{j\\omega\\mu_0 I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$
$$\\mathbf{H}_\\phi = \\frac{j k I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$

**Total radiated power:**
$$P_\\text{rad} = \\frac{\\eta_0 k^2 |I_0 l|^2}{12\\pi} = \\frac{\\pi}{3}\\left(\\frac{l}{\\lambda}\\right)^2 |I_0|^2 R_\\text{rad}$$

**Radiation resistance:**
$$R_\\text{rad} = 20\\pi^2 \\left(\\frac{l}{\\lambda}\\right)^2 \\quad \\Omega$$

**Multipole expansion:** Any radiation pattern can be expanded in spherical wave functions:
$$\\mathbf{E} = \\sum_{n=1}^{\\infty} \\sum_{m=-n}^{n} \\left[ a_{mn} \\mathbf{M}_{mn} + b_{mn} \\mathbf{N}_{mn} \\right]$$

where $\\mathbf{M}_{mn}$ and $\\mathbf{N}_{mn}$ are vector spherical wave functions.

**Spherical mode amplitudes** determine directivity pattern.

**Antenna Q factor** for small spherical antenna:
$$Q = \\frac{1}{k a}^3 \\quad (\\text{for } ka \\ll 1)$$

where $a$ is the antenna radius.

**Active sourcing:** For active antenna analysis, add source term $\\mathbf{J}_\\text{source}$.

**Chinese:**

**球面波**是涉及球面几何的辐射和散射问题的自然解。

**平面波的球面波展开：**
$$e^{-jk\\hat{r}\\cdot\\mathbf{r}_0} = \\sum_{n=0}^{\\infty} (2n+1)(-j)^n j_n(kr_0) P_n(\\cos\\theta)$$

**偶极子辐射方向图：**
对于长度为 $l$、电流为 $I_0$ 的小偶极子：

$$\\mathbf{E}_\\theta = \\frac{j\\omega\\mu_0 I_0 l}{4\\pi r}\\sin\\theta\\, e^{-jkr}$$

**辐射电阻：**
$$R_\\text{rad} = 20\\pi^2 \\left(\\frac{l}{\\lambda}\\right)^2 \\quad \\Omega$$

---

## Section 6-5: Spherical Scatterers and Radar Cross Section / 球面散射体与雷达截面

**English:**

**Radar cross section (RCS)** of a sphere is the canonical scattering problem.

**Mie scattering solution:**
$$\\sigma_\\text{back} = \\frac{\\lambda^2}{\\pi}\\left| \\sum_{n=1}^{\\infty} (-1)^n (2n+1)(a_n - b_n) \\right|^2$$

**Backscatter RCS:**
$$\\sigma = \\pi a^2 |\\Gamma|^2$$

where $\\Gamma$ is the reflection coefficient.

**Forward scatter:** $\\sigma_\\text{forward} = 4\\pi a^2$ at large $ka$.

**Optical theorem:** Relates extinction cross section to forward scattering amplitude:
$$\\sigma_\\text{ext} = \\frac{4\\pi}{k} \\text{Im}\\{f(0)\\}$$

**Low-frequency limit (Rayleigh scattering):** For $ka \\ll 1$:
$$\\sigma = \\frac{9\\pi a^2}{(ka)^4}|\\epsilon_r - 1|^2$$

**Resonant region:** $ka \\sim 1$, complex modal interaction.

**Physical optics approximation:** For large spheres ($ka \\gg 1$):
$$\\sigma \\approx \\pi a^2$$

**Shadow sector:** The forward scatter exceeds geometric cross section by factor of 4 (optical cross section = 4 times geometric).

**Bistatic radar:** RCS at angles other than backscatter.

**Chinese:**

**雷达截面（RCS）**的球体是典型的散射问题。

**米氏散射解：**
$$\\sigma_\\text{back} = \\frac{\\lambda^2}{\\pi}\\left| \\sum_{n=1}^{\\infty} (-1)^n (2n+1)(a_n - b_n) \\right|^2$$

**后向散射RCS：**
$$\\sigma = \\pi a^2 |\\Gamma|^2$$

**光学定理：** 消光截面与前向散射振幅相关：
$$\\sigma_\\text{ext} = \\frac{4\\pi}{k} \\text{Im}\\{f(0)\\}$$

**低频极限（瑞利散射）：** 对于 $ka \\ll 1$：
$$\\sigma = \\frac{9\\pi a^2}{(ka)^4}|\\epsilon_r - 1|^2$$

---

## Section 6-6: Spherical Cavity Resonators / 球面腔体谐振器

**English:**

**Spherical cavity** with conducting walls at radius $a$.

**Resonant modes:**

**TM modes** ($H_r = 0$): $j_n(k_{nm}a) = 0$ → $k_{nm}a = p_{nm}$
**TE modes** ($E_r = 0$): $[kj_n(k a)]' = 0$ → $k_{nm}a = p'_{nm}$

**TM$_{nmp}$ modes:**
$$f_{nmp} = \\frac{c}{2\\pi a}\\sqrt{p_{nm}^2 + \\left(\\frac{p\\pi a}{d}\\right)^2}$$

**TE$_{nmp}$ modes:**
$$f_{nmp} = \\frac{c}{2\\pi a}\\sqrt{p'_{nm}^2 + \\left(\\frac{p\\pi a}{d}\\right)^2}$$

where $p$ is the radial mode number.

**Quality factor** for spherical cavity:
$$Q_{nmp} = \\frac{\\omega_{nmp} W}{P_\\text{loss}} \\approx \\frac{\\eta_0}{R_s}(ka)$$

for the dominant TE mode with $ka \\gg 1$.

**Spherical reflector antennas:** Use spherical wave expansion to analyze feed radiation and reflector interaction.

**Spherical harmonic functions** are also used in global wave propagation, ionospheric modeling, and seismic wave analysis.

**Chinese:**

**球形腔体**在半径 $a$ 处有导电壁。

**谐振模式：**

**TM模式** ($H_r = 0$): $j_n(k_{nm}a) = 0$ → $k_{nm}a = p_{nm}$
**TE模式** ($E_r = 0$): $[kj_n(k a)]' = 0$ → $k_{nm}a = p'_{nm}$

**球形反射器天线：** 使用球面波展开来分析馈源辐射和反射器相互作用。

---


---
chapter: 4
title: Plane Wave Functions
source: Roger F. Harrington, Time-Harmonic Electromagnetic Fields, IEEE Press
pages: 144-230
---

# Chapter 4: Plane Wave Functions / 平面波函数

## Section 4-1: The Wave Functions / 波动函数

**English:**

**Separation of variables** is a technique to solve the scalar Helmholtz equation $\nabla^2\psi + k^2\psi = 0$ in various coordinate systems.

In **rectangular coordinates** $(x, y, z)$, we seek solutions of the form:
$$\psi(x,y,z) = X(x)Y(y)Z(z)$$

Substituting into the Helmholtz equation and dividing by $\psi$:
$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} = -k^2$$

Since each term depends on only one coordinate, they must each equal a constant. Let:
$$\frac{d^2X}{dx^2} + k_x^2 X = 0 \quad \Rightarrow \quad X = A_+ e^{-jk_x x} + A_- e^{jk_x x}$$
$$\frac{d^2Y}{dy^2} + k_y^2 Y = 0 \quad \Rightarrow \quad Y = B_+ e^{-jk_y y} + B_- e^{jk_y y}$$
$$\frac{d^2Z}{dz^2} + k_z^2 Z = 0 \quad \Rightarrow \quad Z = C_+ e^{-jk_z z} + C_- e^{jk_z z}$$

The **separation equation** relates the separation constants:
$$k_x^2 + k_y^2 + k_z^2 = k^2 \tag{4-5}$$

The elementary wave functions are:
$$\psi_{mnp} = h_m(k_x x)h_n(k_y y)h_p(k_z z) \tag{4-7}$$

where $h$ denotes harmonic functions (sine, cosine, exponential).

**Linear combinations** of elementary wave functions form general solutions:
$$\psi = \sum_{k_x, k_y} B_{k_x k_y} h(k_x x)h(k_y y)h(k_z z) \tag{4-8}$$

**Eigenvalues** $k_x, k_y, k_z$ are determined by boundary conditions.
**Eigenfunctions** are the elementary wave functions corresponding to specific eigenvalues.

**中文：**

**分离变量法**是求解标量亥姆霍兹方程 $\nabla^2\psi + k^2\psi = 0$ 在各种坐标系中的技术。

在**直角坐标系** $(x, y, z)$ 中，我们寻求如下形式解：
$$\psi(x,y,z) = X(x)Y(y)Z(z)$$

代入亥姆霍兹方程并除以 $\psi$：
$$\frac{1}{X}\frac{d^2X}{dx^2} + \frac{1}{Y}\frac{d^2Y}{dy^2} + \frac{1}{Z}\frac{d^2Z}{dz^2} = -k^2$$

由于每一项仅依赖于一个坐标，它们必须各等于一个常数。令：
$$\frac{d^2X}{dx^2} + k_x^2 X = 0 \quad \Rightarrow \quad X = A_+ e^{-jk_x x} + A_- e^{jk_x x}$$

**分离方程**将分离常数联系起来：
$$k_x^2 + k_y^2 + k_z^2 = k^2 \tag{4-5}$$

---

## Section 4-2: Rectangular Waveguides / 矩形波导

**English:**

A **rectangular waveguide** has conducting walls at $x = 0, a$ and $y = 0, b$ with $a > b$.

**TE modes** ($E_z = 0$, $H_z \neq 0$):

$$H_z = H_0 \cos\left(\frac{m\pi x}{a}\right)\cos\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**TM modes** ($H_z = 0$, $E_z \neq 0$):

$$E_z = E_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**Cutoff wavenumbers:**
$$k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

**Propagation constant:**
$$\gamma = \sqrt{k_c^2 - k^2} = \alpha + j\beta$$

- If $k > k_c$: $\gamma = j\beta$ (propagating)
- If $k < k_c$: $\gamma = \alpha$ (evanescent, no propagation)

**Cutoff frequency:**
$$f_c = \frac{v}{2}\sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}$$

**Dominant mode (TE10):** $m=1, n=0$, $f_c = c/(2a)$.

**Phase velocity:** $v_p = \omega/\beta > c$
**Group velocity:** $v_g = d\omega/d\beta = c^2/v_p < c$

**Wave impedances:**
$$\eta_{TE} = \frac{\eta}{\sqrt{1 - (f_c/f)^2}} = \eta / \cos\theta_g$$
$$\eta_{TM} = \eta \sqrt{1 - (f_c/f)^2} = \eta \cos\theta_g$$

where $\sin\theta_g = f_c/f$.

**Attenuation in rectangular waveguides:**

Due to conductor losses ($\alpha_c$):
$$\alpha_c \approx \frac{R_s}{b\eta}\frac{1 + \frac{2b}{a}(f_c/f)^2}{\sqrt{1-(f_c/f)^2}}$$

Due to dielectric losses ($\alpha_d$):
$$\alpha_d = \frac{k\tan\delta}{2\sqrt{1-(f_c/f)^2}}$$

**中文：**

**矩形波导**在 $x = 0, a$ 和 $y = 0, b$ 处有导电壁，其中 $a > b$。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：

$$H_z = H_0 \cos\left(\frac{m\pi x}{a}\right)\cos\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**TM模式** ($H_z = 0$, $E_z \neq 0$)：

$$E_z = E_0 \sin\left(\frac{m\pi x}{a}\right)\sin\left(\frac{n\pi y}{b}\right)e^{-\gamma z}$$

**截止波数：**
$$k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$$

**主模（TE10）：** $m=1, n=0$, $f_c = c/(2a)$。

---

## Section 4-3: Circular Waveguides / 圆形波导

**English:**

A **circular waveguide** has radius $a$ in cylindrical coordinates $(\rho, \phi, z)$.

**TE modes** ($E_z = 0$, $H_z \neq 0$):
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n'(x) = 0$ (derivative of Bessel function) for TE modes.

**TM modes** ($H_z = 0$, $E_z \neq 0$):
$$E_z = E_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

where $p_{nm}$ is the $m$-th root of $J_n(x) = 0$ for TM modes.

**Cutoff frequencies for circular waveguide:**

$$f_c = \frac{p_{nm}}{2\pi a\sqrt{\mu\epsilon}}$$

**Dominant TE mode (TE11):** $p_{11} \approx 1.841$ (lowest cutoff for TE modes).

**Attenuation in circular waveguides:**

For TE modes:
$$\alpha_c \approx \frac{R_s}{a\eta}\left(1 + \frac{n^2}{p_{nm}^2 - n^2}\right)$$

For TM modes:
$$\alpha_c \approx \frac{R_s}{a\eta}$$

**Polarization:** Circular waveguide can support two orthogonal polarizations ($e^{j\phi}$ and $e^{-j\phi}$) for the same mode.

**中文：**

**圆形波导**在圆柱坐标系 $(\rho, \phi, z)$ 中半径为 $a$。

**TE模式** ($E_z = 0$, $H_z \neq 0$)：
$$H_z = H_0 J_n\left(\frac{p_{nm}\rho}{a}\right)e^{jn\phi}e^{-\gamma z}$$

其中 $p_{nm}$ 是 $J_n'(x) = 0$ 的第 $m$ 个根（TE模式）。

**主TE模式（TE11）：** $p_{11} \approx 1.841$。

---

## Section 4-4: Waveguide Discontinuities / 波导不连续性

**English:**

Waveguide **discontinuities** occur at junctions, bends, posts, irises, etc. They create reflected and transmitted waves.

**E-plane T-junction:** Series junction where branch couples in E-plane.

**H-plane T-junction:** Shunt junction where branch couples in H-plane.

**E面T形结：** 串联结，分支在E面耦合。
**H面T形结：** 并联结，分支在H面耦合。

**Waveguide irises:** Thin obstacles perpendicular to propagation direction.

**Reactive irises:** Inductive or capacitive posts that create frequency-selective behavior.

**Mode matching:** Discontinuity excites higher-order modes near junction. Far from junction, only propagating modes matter.

**S-matrix formulation:** For a junction between waveguides:
$$[b] = [S][a]$$

where $a$ are incident waves, $b$ are reflected/transmitted waves.

For lossless junction: $[S]$ is unitary ($[S][S]^\dagger = [I]$).

**Step discontinuity:** Junction between waveguides of different cross-sections. Handled by expanding fields in both waveguides in terms of modes and matching boundary conditions.

**中文：**

波导**不连续性**出现在接头、弯头、柱、虹膜等处。它们产生反射和透射波。

**膜片：** 垂直于传播方向的薄障碍物。
**电抗性膜片：** 产生频率选择行为的感性或容性柱。

**模式匹配：** 不连续性在接头附近激发高阶模式。

**S矩阵公式：** 对于波导接头：
$$[b] = [S][a]$$

对于无损耗接头：$[S]$ 是酉矩阵（$[S][S]^\dagger = [I]$）。

---

## Section 4-5: Dielectric Waveguides / 介质波导

**English:**

**Dielectric waveguides** guide waves using total internal reflection at dielectric boundaries, without conducting walls.

**Planar dielectric slab waveguide:** Core of thickness $2d$ with permittivity $\epsilon_1$, surrounded by cladding with $\epsilon_2 < \epsilon_1$.

**Symmetric slab:** Same cladding on both sides.

**Mode condition for symmetric slab (TE modes):**

$$\tan(2k_x d) = \frac{2k_x \alpha}{k_x^2 - \alpha^2}$$

where:
- $k_x = \sqrt{k_1^2 - \beta^2}$ (propagating in core)
- $\alpha = \sqrt{\beta^2 - k_2^2}$ (evanescent in cladding)

**Guided modes exist** when $\beta$ satisfies $k_2 < \beta < k_1$.

**Number of guided modes:**
$$N \approx \left\lfloor \frac{4d}{\lambda_1}\sqrt{n_1^2 - n_2^2} \right\rfloor$$

**Metal-insulator-semiconductor (MIS) waveguides:** Used in integrated optics.

**Optical fibers:** Cylindrical dielectric waveguides for optical communication.

**Step-index fiber:** Core $n_1$, cladding $n_2 < n_1$.

**V-number (归一化频率):**
$$V = k_0 a \sqrt{n_1^2 - n_2^2}$$

**Single-mode condition:** $V < 2.405$ (like step-index fiber with NA and core radius $a$).

**Modal dispersion:** Different modes travel at different velocities.

**中文：**

**介质波导**使用全内反射来导波，无需导电壁。

**平面介质 slab 波导：** 厚度 $2d$ 的芯，介电常数 $\epsilon_1$，被 $\epsilon_2 < \epsilon_1$ 的包层包围。

**对称 slab：** 两面包层相同。

**模式条件（TE模式）：**

$$\tan(2k_x d) = \frac{2k_x \alpha}{k_x^2 - \alpha^2}$$

**导模存在条件：** $\beta$ 满足 $k_2 < \beta < k_1$。

**导模数量：**
$$N \approx \left\lfloor \frac{4d}{\lambda_1}\sqrt{n_1^2 - n_2^2} \right\rfloor$$

---


---

## Section 4-6: Mode Orthogonality / 模式正交性

**English:**

Waveguide modes satisfy **orthogonality** relations that are essential for mode matching and power calculations.

**Orthogonality of TE/TM modes in rectangular waveguide:**

$$\int_0^a \\int_0^b \\mathbf{E}_m \\cdot \\mathbf{E}_n^* \\, dx\\, dy = 0 \\quad \\text{for } m \\neq n$$

$$\int_0^a \\int_0^b \\mathbf{H}_m \\cdot \\mathbf{H}_n^* \\, dx\\, dy = 0 \\quad \\text{for } m \\neq n$$

**Normalization:** Each mode is normalized so that the time-average power crossing any cross-section is unity:

$$\\int_S \\mathbf{S}_m \\cdot \\hat{\\mathbf{z}}\\, dS = 1 \\text{ W}$$

For the **TE$_{mn}$** mode in rectangular waveguide:
$$P_{mn} = \\frac{\\beta_{mn}}{2\\omega\\mu}\\left(\\frac{k_c^2}{k_c^2}\\|\\right) H_0^2 \\cdot \\frac{ab}{4}$$

where $k_c^2 = (m\\pi/a)^2 + (n\\pi/b)^2$.

**Orthogonality integral for modes:**

$$\\int_S (\\mathbf{E}_m \\times \\mathbf{H}_n^*) \\cdot \\hat{\\mathbf{z}}\\, dS = \\delta_{mn}$$

This is critical for the **modal expansion theorem** — any field in a waveguide can be expressed as a sum of orthogonal waveguide modes:

$$\\mathbf{E}_t(x,y,z) = \\sum_n V_n(z)\\mathbf{e}_n(x,y)$$

$$\\mathbf{H}_t(x,y,z) = \\sum_n I_n(z)\\mathbf{h}_n(x,y)$$

where $\\mathbf{e}_n, \\mathbf{h}_n$ are the transverse modal distributions.

**Power orthogonality:** Modes carrying power in different directions are orthogonal with a minus sign:

$$\\int_S (\\mathbf{E}_m \\times \\mathbf{H}_n^*) \\cdot \\hat{\\mathbf{z}}\\, dS = \\begin{cases} +1 & m = n \\text{ (forward)} \\\\ -1 & m = n \\text{ (backward)} \\\\ 0 & m \\neq n \\end{cases}$$

**中文：**

波导模式满足**正交性**关系，这对模式匹配和功率计算至关重要。

**矩形波导中TE/TM模式的正交性：**

$$\\int_0^a \\int_0^b \\mathbf{E}_m \\cdot \\mathbf{E}_n^* \\, dx\\, dy = 0 \\quad (m \\neq n)$$

$$\\int_0^a \\int_0^b \\mathbf{H}_m \\cdot \\mathbf{H}_n^* \\, dx\\, dy = 0 \\quad (m \\neq n)$$

**归一化：** 每个模式归一化，使穿过任何横截面的时间平均功率为1：

$$\\int_S \\mathbf{S}_m \\cdot \\hat{\\mathbf{z}}\\, dS = 1 \\text{ W}$$

这对于**模展开定理**至关重要——波导中的任何场都可以表示为正交波导模式的和：

$$\\mathbf{E}_t(x,y,z) = \\sum_n V_n(z)\\mathbf{e}_n(x,y)$$

---

## Section 4-7: Waveguide Excitation and Coupling / 波导激励与耦合

**English:**

**Waveguide excitation** occurs when a source or discontinuity creates fields in the waveguide.

**Probe excitation:** A coaxial probe extends into the waveguide, exciting primarily the dominant TE10 mode.

**Loop excitation:** A small loop in the waveguide wall couples to the magnetic field.

**Aperture coupling:** A small hole in the waveguide wall couples to another waveguide or cavity.

**Waveguide-to-coaxial transition:** Often implemented as a probe or loop coupler.

**Coupling coefficient for aperture:** For a small circular aperture of radius $r_0$ in a thin conducting wall:

$$C = \\frac{j\\omega\\mu r_0^2}{2}\\left[\\frac{\\partial H_z}{\\partial x} - \\frac{\\partial H_x}{\\partial z}\\right]$$

**E-plane tee junction:** Series junction where signal splits in the E-plane. S-matrix is approximately:

$$[S] = \\begin{pmatrix} 0 & \\frac{1}{\\sqrt{2}} & \\frac{1}{\\sqrt{2}} \\\\ \\frac{1}{\\sqrt{2}} & -\\frac{1}{2} & \\frac{1}{2} \\\\ \\frac{1}{\\sqrt{2}} & \\frac{1}{2} & -\\frac{1}{2} \\end{pmatrix}$$

**H-plane tee junction:** Shunt junction where signal splits in the H-plane. S-matrix is approximately:

$$[S] = \\begin{pmatrix} -\\frac{1}{2} & \\frac{1}{\\sqrt{2}} & \\frac{1}{\\sqrt{2}} \\\\ \\frac{1}{\\sqrt{2}} & 0 & 0 \\\\ \\frac{1}{\\sqrt{2}} & 0 & 0 \\end{pmatrix}$$

**Magic-T (E-H tee):** A 4-port hybrid with complete isolation between E-arm and H-arm. Used in monopulse radar, balanced mixers, and power dividers.

**Cross-guide junction:** 4-port where two waveguides cross at 90°. Mode conversion occurs at the junction.

**Matched load:** Distributed resistive material or vane absorber that absorbs power with low VSWR.

**Short circuit:** Conducting plate. Reflection coefficient $\\Gamma = -1$.

**Rotary joint:** Allows mechanical rotation while maintaining electrical continuity through the waveguide run.

**中文：**

**波导激励**发生在源或不连续性在波导中产生场时。

**探针激励：** 同轴探针伸入波导，主要激励主模TE10。

**环激励：** 波导壁上的小环与磁场耦合。

**孔耦合：** 波导壁上的小孔耦合到另一个波导或腔体。

**E面T形结：** 串联结，信号在E面分开。

**H面T形结：** 并联结，信号在H面分开。

**魔T（E-H T形结）：** 具有E臂和H臂之间完全隔离的4端口混合接头。

---

## Section 4-8: Stripline and Microstrip / 带状线与微带线

**English:**

**Stripline** is a planar transmission line where a conductor is embedded between two ground planes, separated by dielectric.

**Characteristic impedance** of symmetric stripline:

$$Z_0 = \\frac{30\\pi}{\\sqrt{\\epsilon_r}}\\frac{b}{w + 0.441b}$$

where $w$ is the strip width and $b$ is the spacing between ground planes.

For $w/b > 0.35$:
$$Z_0 \\approx \\frac{30\\pi}{\\sqrt{\\epsilon_r}(w/b + 1.441)}$$

**Effective dielectric constant:**
$$\\epsilon_\\text{eff} = \\frac{\\epsilon_r + 1}{2} + \\frac{\\epsilon_r - 1}{2}\\frac{1}{\\sqrt{1 + 12b/w}}$$

**Velocity of propagation:**
$$v = \\frac{c}{\\sqrt{\\epsilon_\\text{eff}}}$$

**Dispersion:** Stripline is relatively dispersion-free for moderate frequencies.

**Microstrip** is a planar line with a conductor on top of a dielectric substrate over a ground plane.

**Characteristic impedance** (quasi-static approximation):
$$Z_0 = \\frac{60}{\\sqrt{\\epsilon_\\text{eff}}}\\ln\\left(\\frac{8h}{w} + \\frac{w}{4h}\\right) \\quad (w/h \\leq 1)$$
$$Z_0 = \\frac{120\\pi}{\\sqrt{\\epsilon_\\text{eff}}}\\frac{1}{w/h + 1.88} \\quad (w/h \\geq 1)$$

**Effective permittivity** (frequency-dependent for microstrip):
$$\\epsilon_\\text{eff}(f) = \\epsilon_r - \\frac{\\epsilon_r - \\epsilon_\\text{eff}(0)}{1 + G(f/f_n)^2}$$

where $f_n = c/(2h\\sqrt{\\epsilon_r - 1})$.

**Microstrip discontinuity effects:**
- Open end: Fringing field equivalent to capacitive load
- Step in width: Equivalent to series capacitance
- Gap: Equivalent to parallel capacitance (coupling)
- Bend: Radiation and current crowding

**Quarter-wave transformer:** Used for matching microstrip to other impedances. Length $\\lambda/4$, characteristic impedance $Z_t = \\sqrt{Z_0 Z_L}$.

**Via holes:** Connect microstrip conductor to ground plane. Equivalent to inductance at high frequencies.

**中文：**

**带状线**是一种平面传输线，导体嵌入两个接地平面之间，被电介质隔开。

**特性阻抗**（对称带状线）：

$$Z_0 = \\frac{30\\pi}{\\sqrt{\\epsilon_r}}\\frac{b}{w + 0.441b}$$

**有效介电常数：**
$$\\epsilon_\\text{eff} = \\frac{\\epsilon_r + 1}{2} + \\frac{\\epsilon_r - 1}{2}\\frac{1}{\\sqrt{1 + 12b/w}}$$

**微带线**是导体在电介质基板上、基板在接地平面上的平面线。

**特性阻抗（准静态近似）：**
$$Z_0 = \\frac{60}{\\sqrt{\\epsilon_\\text{eff}}}\\ln\\left(\\frac{8h}{w} + \\frac{w}{4h}\\right) \\quad (w/h \\leq 1)$$

**微带不连续性效应：**
- 开路端：等效于电容负载的边缘场
- 宽度阶梯：等效于串联电容
- 间隙：等效于并联电容（耦合）

---


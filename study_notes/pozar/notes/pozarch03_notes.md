# Pozar Chapter 3 — Transmission Lines and Waveguides
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 116–185.
> These notes derive all waveguiding structures from Maxwell's equations.

---

## 3.1 General Solutions for TEM, TE, and TM Waves
> TEM、TE 和 TM 波的一般解

### 3.1.1 Starting from Maxwell's Equations | 从 Maxwell 方程组出发

For time-harmonic fields ($e^{j\omega t}$) in a source-free, homogeneous, isotropic region:
> 对于无源、均匀、各向同性区域中的时谐场：

$$\nabla \times \mathbf{E} = -j\omega\mu \mathbf{H}, \quad \nabla \times \mathbf{H} = j\omega\epsilon \mathbf{E}, \quad \nabla \cdot \mathbf{E} = 0, \quad \nabla \cdot \mathbf{H} = 0.$$

### 3.1.2 Wave Equation | 波动方程

Taking the curl of Faraday's law and substituting Ampère's law yields the vector Helmholtz equation:
> 对法拉第定律取旋度并代入安培定律，得到矢量亥姆霍兹方程：

$$\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0, \quad \nabla^2 \mathbf{H} + k^2 \mathbf{H} = 0,$$

where $k = \omega\sqrt{\mu\epsilon} = 2\pi/\lambda$ is the wavenumber.
> 其中 $k = \omega\sqrt{\mu\epsilon} = 2\pi/\lambda$ 为波数。

### 3.1.3 Longitudinal-Transverse Decomposition | 纵向-横向分解

Assume propagation in $+z$: $\mathbf{E}(x,y,z) = [\mathbf{e}(x,y) + \hat{z} e_z(x,y)] e^{-j\beta z}$.
> 假设沿 $+z$ 方向传播。

The Laplacian separates: $\nabla^2 = \nabla_t^2 + \partial^2/\partial z^2$, giving:
> 拉普拉斯算子分离：

$$\nabla_t^2 \mathbf{e} + (k^2 - \beta^2)\mathbf{e} = 0, \quad \nabla_t^2 e_z + (k^2 - \beta^2) e_z = 0.$$

Define the **cutoff wavenumber**: $k_c^2 = k^2 - \beta^2$. Then:
> 定义**截止波数** $k_c^2 = k^2 - \beta^2$：

$$\boxed{\nabla_t^2 e_z + k_c^2 e_z = 0}, \quad \boxed{\nabla_t^2 h_z + k_c^2 h_z = 0}.$$

### 3.1.4 Transverse Fields from Longitudinal Components | 由纵向分量求横向场

From Maxwell's curl equations, transverse fields can be expressed entirely in terms of $E_z$ and $H_z$:
> 由 Maxwell 旋度方程，横向场可完全用 $E_z$ 和 $H_z$ 表示：

**TE modes** ($E_z = 0$):
$$\mathbf{E}_t = -\frac{j\omega\mu}{k_c^2} \hat{z} \times \nabla_t H_z, \quad \mathbf{H}_t = -\frac{j\beta}{k_c^2} \nabla_t H_z.$$

**TM modes** ($H_z = 0$):
$$\mathbf{E}_t = -\frac{j\beta}{k_c^2} \nabla_t E_z, \quad \mathbf{H}_t = -\frac{j\omega\epsilon}{k_c^2} \hat{z} \times \nabla_t E_z.$$

**TEM modes** ($E_z = H_z = 0$): Requires $k_c^2 = 0$, so $\beta = k$. Fields satisfy the 2D electrostatic problem $\nabla_t^2 \phi = 0$.
> TEM 模式需要 $k_c^2 = 0$，因此 $\beta = k$。

### 3.1.5 Propagation Constant and Wave Impedance | 传播常数和波阻抗

| Mode | Propagation | Wave Impedance |
|------|-------------|----------------|
| TEM | $\beta = k$ | $Z_{\text{TEM}} = \eta = \sqrt{\mu/\epsilon}$ |
| TE | $\beta = \sqrt{k^2 - k_c^2}$ ($f > f_c$) | $Z_{\text{TE}} = \eta / \sqrt{1-(f_c/f)^2}$ |
| TM | $\beta = \sqrt{k^2 - k_c^2}$ ($f > f_c$) | $Z_{\text{TM}} = \eta \sqrt{1-(f_c/f)^2}$ |
| Below cutoff | $\beta = -j\alpha$, $\alpha = \sqrt{k_c^2 - k^2}$ | Reactive (evanescent) |

Cutoff frequency: $f_c = k_c/(2\pi\sqrt{\mu\epsilon})$.
> 截止频率：$f_c = k_c/(2\pi\sqrt{\mu\epsilon})$。

---

## 3.2 Parallel Plate Waveguide | 平行板波导

Two conducting plates at $x=0$ and $x=a$, width $b$ in $y$, filled with $\epsilon,\mu$. Fields uniform in $y$.
> 两块导体板位于 $x=0$ 和 $x=a$，$y$ 方向宽度为 $b$。

**TEM mode** ($f_c = 0$): $\mathbf{E} = \hat{x} E_0 e^{-jkz}$, $\mathbf{H} = \hat{y} (E_0/\eta) e^{-jkz}$, $Z_0 = \eta b/a$.

**TM$_n$ modes**: $e_z = A_n \sin(n\pi x/a)$, $k_c = n\pi/a$, $f_{c,n} = n/(2a\sqrt{\mu\epsilon})$.

**TE$_n$ modes**: $h_z = B_n \cos(n\pi x/a)$, $k_c = n\pi/a$, $f_{c,n} = n/(2a\sqrt{\mu\epsilon})$.

---

## 3.3 Rectangular Waveguide | 矩形波导

Standard geometry: width $a$ in $x$, height $b$ in $y$, $a > b$.
> 标准几何：$x$ 方向宽度 $a$，$y$ 方向高度 $b$，$a > b$。

### 3.3.1 TE$_{mn}$ Modes

$$h_z = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

$$k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad f_{c,mn} = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$

**Dominant mode**: TE$_{10}$ ($m=1,n=0$), $f_{c,10} = 1/(2a\sqrt{\mu\epsilon})$.
> **主模**：TE$_{10}$。

### 3.3.2 TM$_{mn}$ Modes

$$e_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{-j\beta z}$$

$$k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}, \quad f_{c,mn} = \frac{1}{2\pi\sqrt{\mu\epsilon}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}$$

Lowest TM mode: TM$_{11}$.
> 最低 TM 模式为 TM$_{11}$。

### 3.3.3 Waveguide Parameters | 波导参数

**Guide wavelength**: $\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1-(f_c/f)^2}}$.
> **波导波长**：$\lambda_g = 2\pi/\beta$。

**Phase velocity**: $v_p = \frac{\omega}{\beta} = \frac{c}{\sqrt{1-(f_c/f)^2}} > c$.
> **相速度**：$v_p = \omega/\beta > c$。

**Group velocity**: $v_g = \frac{d\omega}{d\beta} = c\sqrt{1-(f_c/f)^2} < c$.
> **群速度**：$v_g = d\omega/d\beta < c$。

---

## 3.4 Circular Waveguide | 圆波导

Use cylindrical coordinates $(\rho, \phi, z)$. Fields expressed using Bessel functions.
> 使用柱坐标，场用贝塞尔函数表示。

**TE$_{nm}$ modes**: $k_c = p'_{nm}/a$ where $J'_n(p'_{nm}) = 0$. Dominant: TE$_{11}$.
> TE$_{nm}$ 模式的 $k_c = p'_{nm}/a$。

**TM$_{nm}$ modes**: $k_c = p_{nm}/a$ where $J_n(p_{nm}) = 0$. Dominant: TM$_{01}$.
> TM$_{nm}$ 模式的 $k_c = p_{nm}/a$。

---

## 3.5 Coaxial Line | 同轴线

TEM mode only (for ideal geometry). Fields:
> 仅有 TEM 模式（理想几何下）：

$$\mathbf{E} = \hat{\rho} \frac{V_0}{\rho \ln(b/a)} e^{-jkz}, \quad \mathbf{H} = \hat{\phi} \frac{V_0}{\eta \rho \ln(b/a)} e^{-jkz}.$$

Characteristic impedance: $Z_0 = \frac{\eta}{2\pi} \ln(b/a) = \frac{60}{\sqrt{\epsilon_r}} \ln(b/a)$ [$\Omega$].
> 特征阻抗：$Z_0 = \frac{\eta}{2\pi} \ln(b/a)$。

**Cutoff of higher-order modes / 高阶模式截止：**
- TE$_{11}$ (dominant higher mode): $f_c \approx \frac{c}{\pi\sqrt{\epsilon_r}(a+b)}$
- To avoid higher modes: $(a+b) < \lambda/\pi$
> 为避免高阶模式，需要 $(a+b) < \lambda/\pi$。

---

## 3.6 Surface Waves on Grounded Dielectric Slab | 接地介质板上的表面波

For a dielectric slab of thickness $d$ on a ground plane:
> 对于接地平面上的厚度为 $d$ 的介质板：

**TM$_0$ mode**: No cutoff ($f_c = 0$). Surface wave.
> TM$_0$ 模式无截止频率，为表面波。

**TE$_1$ mode**: Has a cutoff.
> TE$_1$ 模式有截止频率。

Fields decay exponentially in the air region above the slab.
> 场在介质板上方空气中指数衰减。

---

## 3.7 Stripline and Microstrip | 带状线和微带线

**Stripline / 带状线：**
- TEM mode, enclosed by ground planes / TEM 模式，由接地平面包围
- $Z_0 \approx \frac{30\pi}{\sqrt{\epsilon_r}} \frac{b}{W_e + 0.441b}$ (approximate formula for $W/b > 0.35$)
> 近似公式计算特征阻抗

**Microstrip / 微带线：**
- Quasi-TEM mode (not pure TEM due to inhomogeneous dielectric)
> 准 TEM 模式（由于介质不均匀，非纯 TEM）
- Effective permittivity: $\epsilon_e = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \frac{1}{\sqrt{1 + 12h/W}}$
> 有效介电常数
- $Z_0 = \frac{60}{\sqrt{\epsilon_e}} \ln\left( \frac{8h}{W} + \frac{W}{4h} \right)$ for $W/h \leq 1$
- $Z_0 = \frac{120\pi}{\sqrt{\epsilon_e} [W/h + 1.393 + 0.667 \ln(W/h + 1.444)]}$ for $W/h \geq 1$
> 特征阻抗计算公式

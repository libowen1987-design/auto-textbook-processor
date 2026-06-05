# Pozar Chapter 3 — Transmission Lines and Waveguides (Detailed / 详细版)
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 116–185.
> This detailed version includes full derivations and physical explanations.

---

## 3.1 General Solutions for TEM, TE, and TM Waves | TEM、TE 和 TM 波通解

### 3.1.1 Starting from Maxwell's Equations | 从 Maxwell 方程组出发

For time-harmonic fields ($e^{j\omega t}$) in a source-free, homogeneous, isotropic region:
> 对于无源、均匀、各向同性区域中的时谐场 ($e^{j\omega t}$)，Maxwell 方程组为：

$$\nabla \times \mathbf{E} = -j\omega\mu \mathbf{H}, \quad \nabla \times \mathbf{H} = j\omega\epsilon \mathbf{E}, \quad \nabla \cdot \mathbf{E} = 0, \quad \nabla \cdot \mathbf{H} = 0.$$

Taking the curl of Faraday's law:
> 对法拉第定律取旋度：

$$\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E} = -j\omega\mu \nabla\times\mathbf{H}.$$

Substituting $\nabla\times\mathbf{H} = j\omega\epsilon\mathbf{E}$ and $\nabla\cdot\mathbf{E} = 0$:
> 代入 $\nabla\times\mathbf{H} = j\omega\epsilon\mathbf{E}$ 和 $\nabla\cdot\mathbf{E} = 0$：

$$\nabla^2 \mathbf{E} + \omega^2\mu\epsilon \mathbf{E} = 0.$$

With $k = \omega\sqrt{\mu\epsilon} = 2\pi/\lambda$, we obtain the vector Helmholtz equation:
> 其中 $k$ 为波数，得到矢量亥姆霍兹方程：

$$\boxed{\nabla^2 \mathbf{E} + k^2 \mathbf{E} = 0}, \quad \boxed{\nabla^2 \mathbf{H} + k^2 \mathbf{H} = 0}.$$

### 3.1.2 Longitudinal-Transverse Decomposition | 纵向-横向分解

Assume propagation in the $+z$ direction. The fields can be separated into transverse ($t$) and longitudinal ($z$) components:
> 假设沿 $+z$ 方向传播，场可分离为横向和纵向分量：

$$\mathbf{E}(x,y,z) = [\mathbf{e}(x,y) + \hat{z} e_z(x,y)] e^{-j\beta z}, \quad \mathbf{H}(x,y,z) = [\mathbf{h}(x,y) + \hat{z} h_z(x,y)] e^{-j\beta z}.$$

The Laplacian separates as $\nabla^2 = \nabla_t^2 + \partial^2/\partial z^2 = \nabla_t^2 - \beta^2$.
> 拉普拉斯算子分离为横向和纵向部分。

Wave equations for transverse and longitudinal components:
> 横向和纵向分量的波动方程：

$$\nabla_t^2 \mathbf{e} + (k^2 - \beta^2)\mathbf{e} = 0, \quad \nabla_t^2 e_z + (k^2 - \beta^2) e_z = 0.$$

Define the cutoff wavenumber $k_c^2 = k^2 - \beta^2$. Then:
> 定义截止波数 $k_c^2 = k^2 - \beta^2$：

$$\boxed{\nabla_t^2 e_z + k_c^2 e_z = 0}, \quad \boxed{\nabla_t^2 h_z + k_c^2 h_z = 0}.$$

These are 2D scalar Helmholtz equations for the longitudinal components.
> 这些是纵向分量的二维标量亥姆霍兹方程。

### 3.1.3 Transverse Fields from Longitudinal Components | 纵向分量求横向场

The transverse fields can be expressed solely in terms of $E_z$ and $H_z$:
> 横向场可仅用 $E_z$ 和 $H_z$ 表示：

**For TE modes** ($E_z = 0$, $H_z \neq 0$):
$$\mathbf{E}_t = -\frac{j\omega\mu}{k_c^2} \hat{z} \times \nabla_t H_z, \quad \mathbf{H}_t = -\frac{j\beta}{k_c^2} \nabla_t H_z.$$

**For TM modes** ($H_z = 0$, $E_z \neq 0$):
$$\mathbf{E}_t = -\frac{j\beta}{k_c^2} \nabla_t E_z, \quad \mathbf{H}_t = -\frac{j\omega\epsilon}{k_c^2} \hat{z} \times \nabla_t E_z.$$

**For TEM modes** ($E_z = H_z = 0$):
The transverse fields satisfy $\nabla_t^2 \phi = 0$, a 2D electrostatic problem. TEM requires $k_c = 0$, $\beta = k$.
> TEM 模式需要 $k_c = 0$, $\beta = k$。

### 3.1.4 Propagation and Wave Impedance | 传播和波阻抗

- **TEM**: $\beta = k$, $Z_w = \eta = \sqrt{\mu/\epsilon}$, $f_c = 0$
- **TE**: $\beta = \sqrt{k^2 - k_c^2}$ ($f > f_c$), $Z_{\text{TE}} = k\eta/\beta = \eta/\sqrt{1-(f_c/f)^2}$
- **TM**: $\beta = \sqrt{k^2 - k_c^2}$ ($f > f_c$), $Z_{\text{TM}} = \beta\eta/k = \eta\sqrt{1-(f_c/f)^2}$
- **Below cutoff** ($f < f_c$): $\beta = -j\alpha$ where $\alpha = \sqrt{k_c^2 - k^2}$ (evanescent, reactive)

Cutoff frequency: $f_c = k_c/(2\pi\sqrt{\mu\epsilon})$.
> 截止频率：$f_c = k_c/(2\pi\sqrt{\mu\epsilon})$。

---

## 3.2-3.7 Waveguiding Structures | 波导结构总结

### Parallel Plate Waveguide | 平行板波导
Two plates at $x=0$, $x=a$, width $b$. TEM mode exhibits no cutoff.
> 平行板波导的 TEM 模式无截止频率。
- TEM: $Z_0 = \eta b/a$
- TM$_n$: $f_{c,n} = n/(2a\sqrt{\mu\epsilon})$
- TE$_n$: $f_{c,n} = n/(2a\sqrt{\mu\epsilon})$

### Rectangular Waveguide | 矩形波导
Standard: $a > b$ (width × height).
> 标准矩形波导：$a$（宽）× $b$（高），且 $a > b$。
- TE$_{mn}$: $k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$
- TM$_{mn}$: $k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$
- Dominant mode: TE$_{10}$, $f_c = 1/(2a\sqrt{\mu\epsilon})$, $\lambda_c = 2a$
> 主模为 TE$_{10}$，截止波长 $\lambda_c = 2a$。
- $\lambda_g = \lambda/\sqrt{1-(f_c/f)^2}$, $v_p = \omega/\beta > c$, $v_g = d\omega/d\beta < c$

### Circular Waveguide | 圆波导
- TE$_{nm}$: $k_c = p'_{nm}/a$ ($J'_n(p'_{nm})=0$), dominant TE$_{11}$
- TM$_{nm}$: $k_c = p_{nm}/a$ ($J_n(p_{nm})=0$), dominant TM$_{01}$

### Coaxial Line | 同轴线
TEM dominant. $Z_0 = (\eta/2\pi)\ln(b/a)$.
> 同轴线以 TEM 为主模。
- TE$_{11}$ cutoff: $f_c \approx c/(\pi\sqrt{\epsilon_r}(a+b))$
> 为避免高阶模传播，需满足 $(a+b) < \lambda/\pi$。

### Stripline and Microstrip | 带状线和微带线
- **Stripline**: TEM, enclosed. Width $W$, ground separation $b$.
  > 带状线为 TEM 模式，被接地平面包围。
- **Microstrip**: Quasi-TEM. Effective permittivity $\epsilon_e$ accounts for mixed dielectric.
  > 微带线为准 TEM 模式，有效介电常数 $\epsilon_e$ 考虑混合介质效应。

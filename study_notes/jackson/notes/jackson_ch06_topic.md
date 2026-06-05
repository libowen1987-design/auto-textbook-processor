# Jackson Ch6: Maxwell Equations, Macroscopic Electromagnetism / 麦克斯韦方程组与宏观电磁学

> **中英双语版**

**Unit system / 单位制：** Gaussian throughout / 全文使用高斯单位制。

---

## Maxwell's Equations / 麦克斯韦方程组

### Microscopic Maxwell Equations (Gaussian) / 微观麦克斯韦方程组（高斯单位制）

$$
\nabla \cdot \mathbf{E} = 4\pi\rho
$$

$$
\nabla \cdot \mathbf{B} = 0
$$

$$
\nabla \times \mathbf{E} + \frac{1}{c}\frac{\partial \mathbf{B}}{\partial t} = 0
$$

$$
\nabla \times \mathbf{B} - \frac{1}{c}\frac{\partial \mathbf{E}}{\partial t} = \frac{4\pi}{c} \mathbf{J}
$$

### Integral Form / 积分形式

| Equation / 方程 | Integral Form / 积分形式 |
|----------|--------------|
| Gauss E / 高斯电场 | $\oint \mathbf{E} \cdot d\mathbf{a} = 4\pi Q_{\text{enc}}$ |
| Gauss B / 高斯磁场 | $\oint \mathbf{B} \cdot d\mathbf{a} = 0$ |
| Faraday / 法拉第 | $\oint \mathbf{E} \cdot d\mathbf{l} = -\frac{1}{c} \frac{d\Phi_B}{dt}$ |
| Ampère-Maxwell / 安培-麦克斯韦 | $\oint \mathbf{B} \cdot d\mathbf{l} = \frac{4\pi}{c} I_{\text{enc}} + \frac{1}{c}\frac{d\Phi_E}{dt}$ |

### SI Version for Reference / 国际单位制参考

$$
\nabla \cdot \mathbf{E} = \rho/\varepsilon_0
$$

$$
\nabla \cdot \mathbf{B} = 0
$$

$$
\nabla \times \mathbf{E} + \frac{\partial \mathbf{B}}{\partial t} = 0
$$

$$
\nabla \times \mathbf{B} - \mu_0\varepsilon_0 \frac{\partial \mathbf{E}}{\partial t} = \mu_0\mathbf{J}
$$

where $c = 1/\sqrt{\mu_0\varepsilon_0}$.
其中 $c = 1/\sqrt{\mu_0\varepsilon_0}$。

---

## Conservation Laws / 守恒定律

### Poynting's Theorem (Energy Conservation) / 坡印廷定理（能量守恒）

$$
\frac{\partial u}{\partial t} + \nabla \cdot \mathbf{S} = -\mathbf{J} \cdot \mathbf{E}
$$

- **Energy density / 能量密度：** $u = \frac{1}{8\pi}(E^2 + B^2)$
- **Poynting vector / 坡印廷矢量：** $\mathbf{S} = \frac{c}{4\pi} \mathbf{E} \times \mathbf{B}$

**SI / 国际单位制：** $u = \frac{1}{2}\varepsilon_0 E^2 + \frac{1}{2\mu_0}B^2$, $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$

### Momentum Conservation / 动量守恒

$$
\mathbf{g} = \frac{1}{4\pi c} \mathbf{E} \times \mathbf{B} = \frac{1}{c^2} \mathbf{S}
$$

- **Maxwell stress tensor / 麦克斯韦应力张量** $T_{ij}$：

$$
T_{ij} = \frac{1}{4\pi}\left[ E_i E_j + B_i B_j - \frac{1}{2}\delta_{ij}(E^2 + B^2) \right]
$$

**Force / 力：** $F_i = \oint_S T_{ij} n_j \, da$

---

## Macroscopic Equations / 宏观方程

### Macroscopic Maxwell Equations / 宏观麦克斯韦方程组

$$
\nabla \cdot \mathbf{D} = 4\pi\rho_f
$$

$$
\nabla \cdot \mathbf{B} = 0
$$

$$
\nabla \times \mathbf{E} + \frac{1}{c}\frac{\partial \mathbf{B}}{\partial t} = 0
$$

$$
\nabla \times \mathbf{H} - \frac{1}{c}\frac{\partial \mathbf{D}}{\partial t} = \frac{4\pi}{c} \mathbf{J}_f
$$

### Constitutive Relations / 本构关系

Linear isotropic media / 线性各向同性介质：

$$
\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}, \quad \mathbf{J}_f = \sigma \mathbf{E}
$$

In vacuum / 真空中：$\varepsilon = 1$, $\mu = 1$.

### Dielectric Boundary Conditions / 介质边界条件

$$
(D_2 - D_1)\cdot \hat{\mathbf{n}} = 4\pi\sigma_f
$$

$$
\hat{\mathbf{n}} \times (\mathbf{E}_2 - \mathbf{E}_1) = 0
$$

$$
(B_2 - B_1)\cdot \hat{\mathbf{n}} = 0
$$

$$
\hat{\mathbf{n}} \times (\mathbf{H}_2 - \mathbf{H}_1) = \frac{4\pi}{c} \mathbf{K}_f
$$

---

## Frequency-Dependent Properties / 频相关特性

### Complex Dielectric Constant / 复介电常数

$$
\tilde{\varepsilon}(\omega) = \varepsilon'(\omega) + i\varepsilon''(\omega)
$$

### Complex Conductivity / 复电导率

$$
\tilde{\sigma}(\omega) = \sigma'(\omega) + i\sigma''(\omega)
$$

Relation / 关系式：$\tilde{\varepsilon}(\omega) = 1 + \frac{4\pi i}{\omega} \tilde{\sigma}(\omega)$ (Gaussian / 高斯单位制).

### Dispersion Relations (Kramers–Kronig) / 色散关系（克拉默斯–克勒尼希）

$$
\varepsilon'(\omega) - 1 = \frac{2}{\pi} P \int_0^\infty \frac{\omega' \varepsilon''(\omega')}{\omega'^2 - \omega^2} d\omega'
$$

$$
\varepsilon''(\omega) = -\frac{2\omega}{\pi} P \int_0^\infty \frac{\varepsilon'(\omega') - 1}{\omega'^2 - \omega^2} d\omega'
$$

These follow from causality (analyticity of $\varepsilon(\omega)$ in upper half-plane).
这些关系由因果性导出（$\varepsilon(\omega)$ 在上半平面解析）。

---

## Applications / 应用

### Simple Polarizable Media / 简单可极化介质

- **Lorentz oscillator model / 洛伦兹振子模型：**

$$
m\ddot{\mathbf{x}} + m\gamma \dot{\mathbf{x}} + m\omega_0^2 \mathbf{x} = -e\mathbf{E}(t)
$$

- **Resulting polarization / 产生的极化：**

$$
\mathbf{P} = N e \mathbf{x}, \quad \varepsilon(\omega) = 1 + \frac{\omega_p^2}{\omega_0^2 - \omega^2 - i\gamma\omega}
$$

where $\omega_p = \sqrt{4\pi N e^2/m}$ is the plasma frequency.
其中 $\omega_p = \sqrt{4\pi N e^2/m}$ 为等离子体频率。

### Plasma Frequency / 等离子体频率

$$
\omega_p = \sqrt{\frac{4\pi N e^2}{m}} \quad \text{(Gaussian / 高斯)} \quad \text{vs} \quad
\omega_p = \sqrt{\frac{N e^2}{\varepsilon_0 m}} \quad \text{(SI / 国际单位制)}
$$

### Pulsed Plane Wave Reflection / 脉冲平面波反射

- Reflection from conducting surface: boundary condition $\mathbf{E}_{\parallel} = 0$ / 导体面反射：边界条件 $\mathbf{E}_{\parallel} = 0$
- Retarded potentials used for time-dependent sources / 对时变源使用推迟势

### Retarded Potentials / 推迟势

$$
\Phi(\mathbf{x}, t) = \int \frac{[\rho(\mathbf{x}', t')]}{|\mathbf{x} - \mathbf{x}'|} d^3x'
$$

$$
\mathbf{A}(\mathbf{x}, t) = \frac{1}{c} \int \frac{[\mathbf{J}(\mathbf{x}', t')]}{|\mathbf{x} - \mathbf{x}'|} d^3x'
$$

where $t' = t - |\mathbf{x} - \mathbf{x}'|/c$ is the retarded time.
其中 $t' = t - |\mathbf{x} - \mathbf{x}'|/c$ 为推迟时间。

### Inhomogeneous Wave Equation / 非齐次波动方程

$$
\Box^2 \Phi = -4\pi\rho, \quad \Box^2 \mathbf{A} = -\frac{4\pi}{c} \mathbf{J}
$$

where $\Box^2 \equiv \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$ is the d'Alembertian operator.
其中 $\Box^2 \equiv \nabla^2 - \frac{1}{c^2}\frac{\partial^2}{\partial t^2}$ 为达朗贝尔算子。

---

### Key Formulas Summary / 重要公式汇总

| Quantity / 物理量 | Gaussian / 高斯制 | SI / 国际单位制 |
|----------|----------|-----|
| $\nabla \cdot \mathbf{E}$ | $4\pi\rho$ | $\rho/\varepsilon_0$ |
| $\nabla \times \mathbf{B} - \frac{1}{c}\frac{\partial \mathbf{E}}{\partial t}$ | $\frac{4\pi}{c}\mathbf{J}$ | $\mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}$ |
| $\frac{\partial u}{\partial t} + \nabla \cdot \mathbf{S}$ | $-\mathbf{J} \cdot \mathbf{E}$ | $-\mathbf{J} \cdot \mathbf{E}$ |
| $u$ | $(E^2+B^2)/8\pi$ | $\frac{1}{2}\varepsilon_0 E^2 + B^2/(2\mu_0)$ |
| $\mathbf{S}$ | $(c/4\pi)\mathbf{E} \times \mathbf{B}$ | $(1/\mu_0)\mathbf{E} \times \mathbf{B}$ |
| $\omega_p^2$ | $4\pi N e^2/m$ | $N e^2/(\varepsilon_0 m)$ |

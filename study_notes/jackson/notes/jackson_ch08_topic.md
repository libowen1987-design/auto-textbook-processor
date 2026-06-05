# Jackson Ch8: Waveguides, Resonant Cavities, Optical Fibers / 波导、谐振腔与光纤

> **中英双语版**

**Unit system / 单位制：** Gaussian throughout / 全文使用高斯单位制。

---

## Fields in Waveguides / 波导中的场

### Assumptions / 基本假设

- Perfectly conducting walls / 理想导体壁
- Fields have time dependence $e^{-i\omega t}$ / 场具有时谐依赖 $e^{-i\omega t}$
- Propagation along z: fields $\propto e^{i(kz - \omega t)}$ / 沿z方向传播：场 $\propto e^{i(kz - \omega t)}$
- Uniform cross-section in xy-plane / xy平面截面均匀

### Wave Equation for z-components / z分量波动方程

$$
\left[\nabla_t^2 + \left(\frac{\omega^2}{c^2} - k^2\right)\right] \begin{Bmatrix} E_z \\ B_z \end{Bmatrix} = 0
$$

where $\nabla_t^2 = \partial_x^2 + \partial_y^2$.
其中 $\nabla_t^2 = \partial_x^2 + \partial_y^2$。

### Cutoff Wave Number / 截止波数

$$
\gamma^2 = k^2 - \frac{\omega^2}{c^2} = -\kappa^2, \quad
\kappa^2 = \frac{\omega^2}{c^2} - k^2
$$

Propagation when $\omega > \omega_c$ where $\omega_c = c\kappa$ is the cutoff frequency.
当 $\omega > \omega_c$ 时传播，其中 $\omega_c = c\kappa$ 为截止频率。

---

## TE and TM Modes / TE模与TM模

### TE Modes ($E_z = 0$) / TE模（$E_z = 0$）

- Boundary condition / 边界条件：$\frac{\partial B_z}{\partial n} = 0$ on walls / 在壁上
- Transverse fields expressed via $B_z$ / 横向场用 $B_z$ 表示：

$$
\mathbf{E}_t = \frac{i\omega/c}{\kappa^2} \, \hat{\mathbf{z}} \times \nabla_t B_z
$$

$$
\mathbf{B}_t = \frac{ik}{\kappa^2} \, \nabla_t B_z
$$

### TM Modes ($B_z = 0$) / TM模（$B_z = 0$）

- Boundary condition / 边界条件：$E_z = 0$ on walls / 在壁上
- Transverse fields via $E_z$ / 横向场用 $E_z$ 表示：

$$
\mathbf{E}_t = \frac{ik}{\kappa^2} \, \nabla_t E_z
$$

$$
\mathbf{B}_t = -\frac{i\omega/c}{\kappa^2} \, \hat{\mathbf{z}} \times \nabla_t E_z
$$

---

## Rectangular Waveguide / 矩形波导

### Dimensions / 尺寸：$0 \le x \le a$, $0 \le y \le b$

### TM Modes / TM模

$$
E_z = E_0 \sin\left(\frac{m\pi x}{a}\right) \sin\left(\frac{n\pi y}{b}\right) e^{i(kz - \omega t)}
$$

### TE Modes / TE模

$$
B_z = B_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{i(kz - \omega t)}
$$

### Cutoff Frequency / 截止频率

$$
\omega_{mn} = c\pi \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2}
$$

### Dispersion Relation / 色散关系

$$
k_{mn} = \sqrt{\frac{\omega^2}{c^2} - \pi^2\left(\frac{m^2}{a^2} + \frac{n^2}{b^2}\right)}
$$

### Dominant Mode (TE₁₀) / 主模（TE₁₀）

- Lowest cutoff for $a > b$ / $a > b$ 时最低截止频率：$\omega_{10} = \pi c / a$
- Wavelength / 波长：$\lambda_c = 2a$
- Used in most practical rectangular waveguides / 大多数矩形波导使用此模式

### Group and Phase Velocity / 群速与相速

$$
v_p = \frac{\omega}{k} = \frac{c}{\sqrt{1 - (\omega_c/\omega)^2}}, \quad
v_g = c\sqrt{1 - (\omega_c/\omega)^2}
$$

Note / 注意：$v_p v_g = c^2$.

---

## Circular Waveguide / 圆波导

### TE Modes (Bessel functions) / TE模（贝塞尔函数）

$$
B_z = B_0 J_m(\kappa_{mn} \rho) \cos(m\phi) e^{i(kz - \omega t)}
$$

Boundary condition / 边界条件：$J_m'(\kappa_{mn} a) = 0$

### TM Modes / TM模

$$
E_z = E_0 J_m(\kappa_{mn} \rho) \cos(m\phi) e^{i(kz - \omega t)}
$$

Boundary condition / 边界条件：$J_m(\kappa_{mn} a) = 0$

### Cutoff Frequencies / 截止频率

- TE₁₁: $\kappa_{11} a = 1.841$ (dominant mode / 主模)
- TE₀₁: $\kappa_{01} a = 3.832$
- TM₀₁: $\kappa_{01} a = 2.405$

---

## Energy Flow and Attenuation / 能量流与衰减

### Power Flow / 功率流

$$
P = \frac{c}{8\pi} \operatorname{Re} \int_S (\mathbf{E} \times \mathbf{B}^*) \cdot \hat{\mathbf{z}} \, da
$$

### Attenuation Constant / 衰减常数

$$
\alpha = \frac{P_\text{loss}}{2P}
$$

For imperfect conductors: loss in walls due to finite conductivity.
对于非理想导体：有限电导率导致的壁损耗。

### Dielectric Loss / 介质损耗

If waveguide is filled with dielectric $\varepsilon = \varepsilon' + i\varepsilon''$ / 若波导填充介质 $\varepsilon = \varepsilon' + i\varepsilon''$：

$$
\alpha_d = \frac{\omega}{c} \frac{\varepsilon''}{2\sqrt{\varepsilon'}}
$$

---

## Resonant Cavities / 谐振腔

### Rectangular Cavity / 矩形谐振腔

Dimensions / 尺寸：$0 \le x \le a$, $0 \le y \le b$, $0 \le z \le d$

Standing wave along z / 沿z方向的驻波：$k = p\pi/d$

### Resonant Frequency / 谐振频率

$$
\omega_{mnp} = c\pi \sqrt{\frac{m^2}{a^2} + \frac{n^2}{b^2} + \frac{p^2}{d^2}}
$$

### Quality Factor (Q) / 品质因数（Q值）

$$
Q = \omega_0 \frac{U}{P_\text{loss}} = \frac{2}{\delta} \frac{V}{S} \quad (\text{for good conductors / 良导体})
$$

where $\delta$ is skin depth, V is cavity volume, S is surface area.
其中 $\delta$ 为趋肤深度，V 为腔体体积，S 为表面积。

### TE₁₀₁ Mode Example / TE₁₀₁模示例

Fields / 场分布：

$$
E_y = E_0 \sin\left(\frac{\pi x}{a}\right) \sin\left(\frac{\pi z}{d}\right)
$$

$$
B_x = -\frac{i ck_z}{\omega} E_0 \sin\left(\frac{\pi x}{a}\right) \cos\left(\frac{\pi z}{d}\right)
$$

$$
B_z = -\frac{i \pi c}{\omega a} E_0 \cos\left(\frac{\pi x}{a}\right) \sin\left(\frac{\pi z}{d}\right)
$$

---

## Cylindrical Cavity / 圆柱谐振腔

### TE Modes / TE模

- Resonant frequency / 谐振频率：$\omega_{mnp} = c\sqrt{(\kappa_{mn}/R)^2 + (p\pi/d)^2}$
- $\kappa_{mn} a = $ roots of $J_m'(x) = 0$ / $J_m'(x) = 0$ 的根

### TM Modes / TM模

- $\omega_{mnp} = c\sqrt{(\kappa_{mn}/R)^2 + (p\pi/d)^2}$
- $\kappa_{mn} a = $ roots of $J_m(x) = 0$ / $J_m(x) = 0$ 的根

---

## Dielectric Waveguides (Optical Fibers) / 介质波导（光纤）

### Step-Index Fiber / 阶跃折射率光纤

- Core / 纤芯：$n_1$, radius / 半径 $a$
- Cladding / 包层：$n_2 < n_1$

### V Parameter (Normalized Frequency) / V参数（归一化频率）

$$
V = \frac{2\pi a}{\lambda} \sqrt{n_1^2 - n_2^2} = \frac{\omega a}{c} \sqrt{n_1^2 - n_2^2}
$$

### Single-Mode Condition / 单模条件

$$
V < 2.405
$$

### HE₁₁ Mode / HE₁₁模：fundamental mode of optical fiber / 光纤基模

- Always propagates (no cutoff) / 始终传播（无截止）
- Hybrid mode (both Ez and Bz nonzero) / 混合模（Ez和Bz均不为零）

### Mode Classification / 模式分类

- **TE₀ₘ, TM₀ₘ:** axially symmetric modes / 轴对称模式
- **HEₘₙ, EHₘₙ:** hybrid modes / 混合模式, $m \neq 0$

---

## Attenuation in Optical Fibers / 光纤中的衰减

### Loss Mechanisms / 损耗机制

- **Rayleigh scattering / 瑞利散射：** $\propto 1/\lambda^4$ (dominates at short wavelengths / 在短波长占主导)
- **Absorption / 吸收：** OH⁻ impurities, electronic transitions / OH⁻杂质、电子跃迁
- **Bending loss / 弯曲损耗：** radiative loss at bends / 弯曲处的辐射损耗
- **Connector/splice loss / 连接/熔接损耗：** misalignment / 对准偏差

### Minimum Loss / 最小损耗

- Practical silica fiber / 实用石英光纤：~0.2 dB/km at 1.55 $\mu$m
- Window wavelengths / 窗口波长：1.3 $\mu$m, 1.55 $\mu$m

---

### Key Formulas Summary / 重要公式汇总

| Quantity / 物理量 | Expression / 表达式 |
|----------|-----------|
| Cutoff freq (rect.) / 矩形波导截止频率 | $\omega_{mn} = c\pi\sqrt{(m/a)^2 + (n/b)^2}$ |
| Rectangular cavity frequency / 矩形腔谐振频率 | $\omega_{mnp} = c\pi\sqrt{(m/a)^2 + (n/b)^2 + (p/d)^2}$ |
| $v_p v_g$ | $v_p v_g = c^2$ |
| V parameter / V参数 | $V = (2\pi a/\lambda)\sqrt{n_1^2 - n_2^2}$ |
| Single-mode fiber / 单模光纤 | $V < 2.405$ |
| Q factor / Q值 | $Q = \omega_0 U / P_\text{loss}$ |

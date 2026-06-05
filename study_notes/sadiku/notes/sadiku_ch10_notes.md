# Sadiku《Elements of Electromagnetics》Chapter 10: Waveguides
> **中英双语版**

## 10.1 General Wave Behaviors / 波的一般行为
$$\gamma = \sqrt{k_c^2 - k^2}, \quad \beta = \sqrt{k^2 - k_c^2} \; (f > f_c), \quad f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}$$
Cutoff: below $f_c$, waves are evanescent / 低于截止频率时，波为消逝波。

## 10.2 Rectangular Waveguide / 矩形波导
**TE$_{mn}$ modes**: $H_z = H_0 \cos(m\pi x/a) \cos(n\pi y/b) e^{-j\beta z}$
$$k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}, \quad \text{dominant TE}_{10}$$

**TM$_{mn}$ modes**: $E_z = E_0 \sin(m\pi x/a) \sin(n\pi y/b) e^{-j\beta z}$

**Cutoff wavelengths / 截止波长：**
$$\lambda_c = \frac{2}{\sqrt{(m/a)^2 + (n/b)^2}}$$

## 10.3 Waveguide Parameters / 波导参数
- Guide wavelength / 波导波长: $\lambda_g = \lambda/\sqrt{1-(f_c/f)^2}$
- Phase velocity / 相速度: $v_p = c/\sqrt{1-(f_c/f)^2} > c$
- Group velocity / 群速度: $v_g = c\sqrt{1-(f_c/f)^2} < c$
- Wave impedance / 波阻抗: $Z_{\text{TE}} = \eta/\sqrt{1-(f_c/f)^2}$, $Z_{\text{TM}} = \eta\sqrt{1-(f_c/f)^2}$

## 10.4 Power Transmission / 功率传输
$$P = \frac{1}{2}\text{Re}\int_S (\mathbf{E} \times \mathbf{H}^*) \cdot d\mathbf{S}$$

## 10.5 Dielectric Waveguide / 介质波导
Surface waves on dielectric slab; optical fibers (step-index, graded-index).
> 介质板上的表面波；光纤（阶跃折射率、渐变折射率）。

## 10.6 Circular Waveguide / 圆波导
Bessel function solutions. Dominant TE$_{11}$ mode.

# Sadiku《Elements of Electromagnetics》Chapter 8: Electromagnetic Wave Propagation
> **中英双语版**

## 8.1 Wave Equation / 波动方程
$$\nabla^2 \mathbf{E} = \mu\epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2}, \quad \nabla^2 \mathbf{H} = \mu\epsilon \frac{\partial^2 \mathbf{H}}{\partial t^2}$$

## 8.2 Plane Waves in Free Space / 自由空间平面波
$$\mathbf{E} = \mathbf{E}_0 e^{j(\omega t - kz)}, \quad \mathbf{H} = \frac{k}{\omega\mu} \hat{z} \times \mathbf{E}$$
$k = \omega\sqrt{\mu_0\epsilon_0} = \omega/c$, $\eta_0 = \sqrt{\mu_0/\epsilon_0} \approx 377\;\Omega$.

## 8.3 Wave Polarization / 波的极化
- **Linear / 线极化**: $\delta = \delta_y - \delta_x = 0$ or $\pi$
- **Circular / 圆极化**: $E_{x0} = E_{y0}$, $\delta = \pm \pi/2$
- **Elliptical / 椭圆极化**: General case

## 8.4 Plane Waves in Dielectrics / 介质中的平面波
Propagation constant $\gamma = \alpha + j\beta = \sqrt{j\omega\mu(\sigma + j\omega\epsilon)}$.
- Low-loss dielectrics / 低损耗介质: $\alpha \approx \sigma/2\sqrt{\mu/\epsilon}$, $\beta \approx \omega\sqrt{\mu\epsilon}$
- Good conductors / 良导体: $\alpha = \beta = \sqrt{\pi f\mu\sigma}$, skin depth $\delta_s = 1/\alpha = 1/\sqrt{\pi f\mu\sigma}$

## 8.5 Poynting Vector for Plane Waves / 平面波的坡印廷矢量
$$\mathbf{P}_{\text{av}} = \frac{1}{2}\text{Re}(\mathbf{E} \times \mathbf{H}^*) = \hat{k}\frac{|E_0|^2}{2\eta}$$

## 8.6 Reflection of Plane Waves / 平面波的反射
**Normal incidence / 正入射：**
$$\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}, \quad T = 1 + \Gamma$$
SWR = standing wave ratio: $S = \frac{1+|\Gamma|}{1-|\Gamma|}$ / 驻波比

**Oblique incidence / 斜入射：**
- Snell's law / 斯涅耳定律: $\sqrt{\mu_1\epsilon_1}\sin\theta_i = \sqrt{\mu_2\epsilon_2}\sin\theta_t$
- Fresnel equations for parallel/perpendicular polarization
  > 平行/垂直极化的菲涅耳公式
- Critical angle / 临界角: $\theta_c = \sin^{-1}(\sqrt{\epsilon_2/\epsilon_1})$
- Brewster angle / 布儒斯特角: $\theta_B = \tan^{-1}(\sqrt{\epsilon_2/\epsilon_1})$

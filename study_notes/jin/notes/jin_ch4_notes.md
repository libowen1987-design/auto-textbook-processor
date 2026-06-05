---
title: "Chapter 4 — Transmission Lines and Plane Waves"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Transmission line theory (RLCG parameters, Telegrapher's equations)
  - Uniform plane waves in unbounded media
  - Reflection and transmission at planar interfaces
  - Polarization (linear, circular, elliptical)
  - Dispersive media, group velocity, attenuation
  - Waves in anisotropic (uniaxial, gyrotropic) and bi-isotropic (chiral) media
---

# Chapter 4: Transmission Lines and Plane Waves | 第四章：传输线与平面波

> **中英双语版**

## 4.1 Transmission Line Theory | 传输线理论

**Telegrapher's equations / 电报方程:**

$$
\frac{dV}{dz} + (j\omega L + R)I = 0, \quad \frac{dI}{dz} + (j\omega C + G)V = 0
\tag{4.1.1, 4.1.2}
$$

Wave equation / 波动方程：

$$
\frac{d^2 V}{dz^2} - \gamma^2 V = 0, \quad \gamma = \sqrt{(j\omega L + R)(j\omega C + G)}
\tag{4.1.3}
$$

**Characteristic impedance / 特性阻抗:**

$$
Z_0 = \sqrt{\frac{j\omega L + R}{j\omega C + G}}
$$

For lossless line / 无耗线：$Z_0 = \sqrt{L/C}$, $\beta = \omega\sqrt{LC}$, $v_p = 1/\sqrt{LC}$。

**Reflection coefficient / 反射系数:**

$$
\Gamma(z) = \frac{V^-(z)}{V^+(z)} = \Gamma_L e^{2\gamma(z - L)}, \quad
\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}
$$

**Input impedance / 输入阻抗:**

$$
Z_{\text{in}}(z) = Z_0 \frac{Z_L + Z_0 \tanh(\gamma l)}{Z_0 + Z_L \tanh(\gamma l)}
$$

**Smith chart / 史密斯圆图** — 阻抗/反射系数可视化的图形工具。

---

## 4.2 Uniform Plane Waves | 均匀平面波

For a plane wave propagating in $+\hat{z}$ direction, fields are transverse ($E_z = H_z = 0$) / 沿 $+\hat{z}$ 方向传播的平面波，场为横向：

$$
\mathbf{E}(z) = \hat{x} E_0 e^{-jkz}, \quad \mathbf{H}(z) = \hat{y} \frac{E_0}{\eta} e^{-jkz}
$$

**Intrinsic impedance / 本征阻抗:** $\eta = \sqrt{j\omega\mu / (\sigma + j\omega\epsilon)}$。

For lossless media / 无耗媒质：$\eta = \sqrt{\mu/\epsilon}$。

**Phase velocity / 相速度:** $v_p = \omega/k = 1/\sqrt{\mu\epsilon}$。

**Attenuation in lossy media / 有损耗媒质中的衰减:** $\gamma = \alpha + j\beta$，$\alpha$ 为衰减常数。

---

## 4.3 Reflection and Transmission at Planar Interfaces | 平面界面的反射与传输

**Normal incidence / 正入射:**

$$
\Gamma = \frac{\eta_2 - \eta_1}{\eta_2 + \eta_1}, \quad
T = \frac{2\eta_2}{\eta_2 + \eta_1}
$$

**Oblique incidence / 斜入射** — Snell's law / 斯涅尔定律:

$$
k_1 \sin\theta_i = k_1 \sin\theta_r = k_2 \sin\theta_t
$$

**Fresnel coefficients (TE/S polarization) / 菲涅耳系数（TE/S极化）:**

$$
R_\perp = \frac{\eta_2 \cos\theta_i - \eta_1 \cos\theta_t}{\eta_2 \cos\theta_i + \eta_1 \cos\theta_t}
$$

**Fresnel coefficients (TM/P polarization) / 菲涅耳系数（TM/P极化）:**

$$
R_\parallel = \frac{\eta_2 \cos\theta_t - \eta_1 \cos\theta_i}{\eta_2 \cos\theta_t + \eta_1 \cos\theta_i}
$$

**Brewster angle / 布儒斯特角** (zero reflection for TM / TM零反射): $\tan\theta_B = \sqrt{\epsilon_2/\epsilon_1}$。

**Total internal reflection / 全内反射** when $\theta_i > \theta_c = \sin^{-1}(\sqrt{\epsilon_2/\epsilon_1})$。

---

## 4.4 Polarization | 极化

**Linear / 线极化:** $E_x$ 和 $E_y$ 同相。

**Circular / 圆极化:** $|E_x| = |E_y|$，相位差 $\pm 90^\circ$。

**Elliptical / 椭圆极化:** 一般情况。

---

## 4.5 Dispersion | 色散

**Group velocity / 群速度:** $v_g = d\omega/dk$。

In a dispersive medium, signal pulse broadens / 色散媒质中信号脉冲会展宽。关系: $v_g v_p = c^2/n_g$。

---

## 4.6 Anisotropic & Bi-isotropic Media | 各向异性和双各向同性媒质

**Uniaxial medium / 单轴媒质:** $\overline{\epsilon} = \text{diag}(\epsilon_t, \epsilon_t, \epsilon_z)$。寻常波 ($k_o = \omega\sqrt{\mu\epsilon_t}$) 和非常波。

**Gyrotropic medium (magnetized plasma) / 回旋媒质（磁化等离子体）:** $\overline{\epsilon}$ 有非对角元 → 法拉第旋转。

**Chiral medium / 手性媒质:** $D = \epsilon E + \xi H$, $B = \mu H + \zeta E$ → 依赖于手性的传播。

---

## Key Physical Intuition | 关键物理直觉

1. **传输线类比** 将分布式电路概念（$V$, $I$, $Z_0$）与波传播（$E$, $H$, $\eta$）联系。
2. **平面波是最简单的波解** — 任意波前可在局部近似为平面。
3. **极化** 对天线设计、雷达极化和光通信至关重要。
4. **色散** 会使脉冲失真——对高速数字和宽带系统至关重要。

---

## Audit / 审计

| Section / 节 | Content Coverage / 内容覆盖 |
|---------|-----------------|
| 4.1 | 传输线理论 |
| 4.2 | 均匀平面波 |
| 4.3 | 反射与传输 |
| 4.4 | 极化 |
| 4.5 | 色散 |
| 4.6 | 各向异性媒质 |

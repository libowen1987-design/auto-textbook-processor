# Jackson Ch13: Collisions, Energy Loss, and Scattering / 碰撞、能量损失与散射

> **中英双语版**

## Overview / 概述
Energy loss of charged particles passing through matter; scattering collisions; stopping power; range.
带电粒子穿过物质时的能量损失、散射碰撞、阻止本领与射程。

---

## Scattering Cross Section and Energy Loss / 散射截面与能量损失

### Kinematics of Elastic Scattering / 弹性散射运动学

**Lab frame / 实验室系**：projectile (mass $m$, charge $z e$) hits stationary target ($M$, $Ze$).
入射粒子（质量 $m$，电荷 $z e$）撞击静止靶核（$M$, $Ze$）。

**Energy transfer in a single collision / 单次碰撞中的能量转移**：

$$
\Delta E = \frac{2 m M}{(m+M)^2} \, p^2 (1 - \cos\Theta_{cm})
$$

where $\Theta_{cm}$ is the scattering angle in the center-of-mass frame.
其中 $\Theta_{cm}$ 为质心系中的散射角。

For $m \ll M$ (electron on heavy nucleus) / 当 $m \ll M$（电子撞击重核）：

$$
\Delta E \approx \frac{p^2}{M} (1 - \cos\Theta_{cm}) \quad \text{or} \quad \Delta E_{\text{max}} = \frac{2p^2}{M}
$$

### Differential Cross Section for Scattering / 散射微分截面

Rutherford scattering (Coulomb potential) / 卢瑟福散射（库仑势）：

$$
\frac{d\sigma}{d\Omega} = \left( \frac{z Z e^2}{4p v} \right)^2 \frac{1}{\sin^4(\Theta/2)}
$$

Energy-loss differential cross section / 能量损失微分截面：

$$
\frac{d\sigma}{d\Delta E} = \frac{2\pi z^2 Z^2 e^4}{m v^2} \frac{1}{(\Delta E)^2} \quad \text{(non-relativistic / 非相对论)}
$$

---

## Energy Loss for Moderately Heavy Charged Particles — Stopping Power / 中等质量带电粒子的能量损失——阻止本领

### Bethe-Bloch Formula (non-relativistic, heavy incident particle) / Bethe-Bloch公式（非相对论，重入射粒子）

Stopping power (energy loss per unit path length) / 阻止本领（单位路径长度能量损失）：

$$
-\frac{dE}{dx} = \frac{4\pi N_a z^2 e^4}{m_e v^2} Z \rho \frac{1}{A} \left[ \ln\frac{2 m_e v^2}{I} + \text{corrections} \right]
$$

where / 其中：
- $N_a$ = Avogadro's number / 阿伏伽德罗常数
- $m_e$ = electron mass / 电子质量
- $z e$ = projectile charge / 入射粒子电荷, $v$ = projectile speed / 速度
- $Z$ = atomic number of medium / 介质原子序数, $A$ = atomic weight / 原子量
- $\rho$ = density / 密度, $I$ = mean excitation potential / 平均激发能 ($I \approx 10Z$ eV for $Z \lesssim 30$)
- $\rho$ in g/cm³ → $dE/dx$ in MeV/cm / $\rho$ 单位 g/cm³ → $dE/dx$ 单位 MeV/cm

### Bethe-Bloch (relativistic) / 相对论Bethe-Bloch公式

$$
-\frac{dE}{dx} = \frac{4\pi N_a r_e^2 m_e c^2 z^2}{\beta^2} \frac{Z\rho}{A} \left[ \frac12 \ln\frac{2 m_e c^2 \beta^2 \gamma^2 T_{\text{max}}}{I^2} - \beta^2 - \frac{\delta}{2} \right]
$$

where / 其中：
- $r_e = e^2/m_e c^2$ = classical electron radius / 经典电子半径
- $T_{\text{max}} = \frac{2 m_e c^2 \beta^2 \gamma^2}{1 + 2\gamma m_e/M + (m_e/M)^2}$ = max kinetic energy transfer / 最大动能传递
- $\delta$ = density effect correction (Fermi plateau) / 密度效应修正（费米平台）
- Validity / 适用范围：$0.1 \lesssim \beta\gamma \lesssim 1000$ for heavy charged particles / 重带电粒子

### Key Features / 关键特征

1. **$1/\beta^2$ dependence** at low energies → Bragg peak near end of range / 低能时具有 $1/\beta^2$ 依赖 → 射程末端出现布拉格峰
2. **Relativistic rise** (ln $\gamma$) → "Fermi plateau" after density correction / 相对论上升 (ln $\gamma$) → 密度修正后的"费米平台"
3. **Minimum ionizing particles** (MIP) at $\beta\gamma \approx 3$–4 / 最小电离粒子在 $\beta\gamma \approx 3$–4
4. **Barkas effect / 巴卡斯效应**：$z^3$ correction for very slow particles / 极慢粒子的 $z^3$ 修正

---

## Range and Straggling / 射程与离散

### Range / 射程

Continuous Slowing Down Approximation (CSDA) range / 连续慢化近似射程：

$$
R(T) = \int_0^T \frac{dE}{(-dE/dx)}
$$

**Empirical range relation** (non-relativistic) / 经验射程关系（非相对论）：$R \propto M v^{3.2}$ for same $z$ at same $v$（相同电荷和速度下）

### Straggling / 离散

Energy-loss fluctuations due to the stochastic nature of collisions / 由碰撞随机性导致的能量损失涨落：
- **Vavilov distribution / 瓦维洛夫分布**：general case (Landau for thin absorbers, Gaussian for thick) / 一般情况（薄吸收体用朗道分布，厚吸收体用高斯分布）
- **Energy straggling / 能量离散** $\propto \sqrt{x}$ for thick absorbers / 厚吸收体
- **Range straggling / 射程离散** $\Delta R/R \propto 1/\sqrt{N}$ where $N$ = number of collisions / $N$ 为碰撞次数

---

## Energy Loss for Electrons and Positrons / 电子与正电子的能量损失

### Electrons are different from heavy particles / 电子与重粒子的不同之处：
1. Mass = target mass → large energy transfer in single collision / 质量与靶粒子相同 → 单次碰撞能量传递大
2. **Bremsstrahlung** significant at high energy (radiative vs. collision loss) / 高能时韧致辐射显著（辐射损失vs碰撞损失）

**Collision loss / 碰撞损失** (Bhabha for $e^+$, Møller for $e^-$) / （正电子用Bhabha散射，电子用Møller散射）：

$$
-\left(\frac{dE}{dx}\right)_{\text{coll}} = \frac{4\pi N_a r_e^2 m_e c^2}{\beta^2} \frac{Z\rho}{A} \times \text{logarithmic term / 对数项}
$$

**Critical energy** $E_c$ where collision loss = radiative loss / 临界能量 $E_c$，碰撞损失 = 辐射损失：
- For most materials / 对大多数材料：$E_c \approx 800\,\text{MeV}/(Z+1.2)$
- Above $E_c$ / $E_c$ 以上：radiation dominates / 辐射主导

**Radiation length** $X_0$ (mean distance for $1/e$ energy loss via bremsstrahlung) / 辐射长度 $X_0$（通过韧致辐射能量降至 $1/e$ 的平均距离）：

$$
X_0 \approx \frac{716.4\,\text{g/cm}^2 \cdot A}{Z(Z+1)\ln(287/\sqrt{Z})}
$$

---

## Energy Loss for Light Ions / 轻离子的能量损失

Extension of Bethe-Bloch to light ions ($p$, $d$, $\alpha$) / Bethe-Bloch公式向轻离子（质子、氘核、$\alpha$粒子）的推广：

$$
-\frac{dE}{dx} = z^2 f(\beta)
$$

where $f(\beta)$ depends on the medium but not on projectile charge or mass (at same velocity).
其中 $f(\beta)$ 取决于介质，但在相同速度下与入射粒子电荷或质量无关。

**Rigidity / 刚性**：$p/Z$ (momentum per unit charge / 单位电荷动量) determines trajectory in magnetic fields / 决定磁场中的轨迹。

---

## Multiple Scattering / 多次散射

### Molière Theory / 莫里哀理论

Angular distribution from many small-angle Coulomb scatterings / 多次小角度库仑散射的角度分布：
- **Gaussian core / 高斯核**：$\theta \propto \sqrt{x} / (p v)$ for small angles / 小角度
- **Power-law tails / 幂律尾部** from single large-angle events / 来自单次大角度事件

**RMS scattering angle / 均方根散射角**：

$$
\theta_{\text{rms}} = \frac{13.6\,\text{MeV}}{\beta c p} \sqrt{\frac{x}{X_0}} \left[1 + 0.038 \ln\left(\frac{x}{X_0}\right) \right]
$$

**Planar projection / 平面投影**：$\theta_{\text{plane, rms}} = \theta_{\text{space, rms}} / \sqrt{3}$

---

## Cherenkov Radiation / 切伦科夫辐射

### Threshold / 阈条件
Particle velocity $v > c/n$ (exceeds phase velocity of light in medium) / 粒子速度 $v > c/n$（超过介质中的光速）
Threshold / 阈条件：$\beta > 1/n$

### Angle / 辐射角

$$
\cos\theta_c = \frac{1}{\beta n}
$$

Energy radiated per unit path length / 单位路径长度的辐射能量：

$$
\frac{dE}{dx} = \frac{e^2}{c^2} \int_{\beta n > 1} \omega \left(1 - \frac{1}{\beta^2 n^2(\omega)}\right) d\omega
$$

### Applications / 应用
- Cherenkov counters for particle identification / 切伦科夫计数器用于粒子识别
- Ring Imaging Cherenkov (RICH) detectors / 环形成像切伦科夫探测器

---

## Key Formulas Summary / 重要公式汇总

| Concept / 概念 | Formula / 公式 |
|---------|---------|
| Bethe-Bloch (relativistic) / 相对论Bethe-Bloch | $-\frac{dE}{dx} = K \frac{z^2}{\beta^2} \frac{Z}{A} \left[ \frac12 \ln \frac{2m_e c^2 \beta^2 \gamma^2 T_{\text{max}}}{I^2} - \beta^2 - \frac{\delta}{2} \right]$ |
| Rutherford cross section / 卢瑟福截面 | $\frac{d\sigma}{d\Omega} = \left( \frac{zZe^2}{4pv} \right)^2 \csc^4\frac{\Theta}{2}$ |
| Multiple scattering RMS / 多次散射均方根 | $\theta_{\text{rms}} = \frac{13.6\,\text{MeV}}{\beta c p} \sqrt{x/X_0} \left[1 + 0.038 \ln(x/X_0)\right]$ |
| Cherenkov angle / 切伦科夫角 | $\cos\theta_c = 1/(\beta n)$ |
| Critical energy / 临界能量 | $E_c \approx 800/(Z+1.2)$ MeV |

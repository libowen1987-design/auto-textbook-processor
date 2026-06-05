# Jackson Ch15: Bremsstrahlung, Radiative Beta Decay / 韧致辐射与辐射β衰变

> **中英双语版**

## Overview / 概述
Radiation emitted when charged particles are accelerated in Coulomb fields of nuclei. The Weizsacker-Williams method of virtual quanta.
带电粒子在原子核库仑场中加速时产生的辐射。虚拟量子方法（魏茨泽克-威廉姆斯方法）。

---

## Bremsstrahlung in a Coulomb Field / 库仑场中的韧致辐射

### Classical Bremsstrahlung / 经典韧致辐射

A charged particle with charge $ze$ colliding with a nucleus of charge $Ze$.
电荷为 $ze$ 的带电粒子与电荷为 $Ze$ 的原子核碰撞。

**Radiation energy per unit frequency** (classical, non-relativistic) / **单位频率的辐射能量**（经典、非相对论）：

$$
\frac{dI}{d\omega} = \frac{8}{3\pi} \frac{z^2 Z^2 e^6}{(4\pi\epsilon_0)^3} \frac{1}{m^2 v_1^2 c^3} \ln\left( \frac{v_1 + v_2}{v_1 - v_2} \right)
$$

where $v_1$ is initial velocity, $v_2$ is final velocity.
其中 $v_1$ 为初速度，$v_2$ 为末速度。

### Low-frequency limit / 低频极限

For $\omega \ll v/b_{\text{min}}$ / 当 $\omega \ll v/b_{\text{min}}$：

$$
\frac{dI}{d\omega} \approx \frac{16}{3} \frac{z^2 Z^2 e^6}{(4\pi\epsilon_0)^3} \frac{1}{m^2 c^3 v_1^2}
$$

Independent of $\omega$ → flat spectrum at low frequencies (infrared divergence).
与 $\omega$ 无关 → 低频平坦谱（红外发散）。

### High-frequency cutoff / 高频截断

At $\omega \gg m v_1^2/\hbar$ (quantum regime) / 当 $\omega \gg m v_1^2/\hbar$（量子区域）：spectrum drops rapidly (quantum cutoff at $E_e = \hbar\omega_{\text{max}}$) / 频谱快速下降（量子截断在 $E_e = \hbar\omega_{\text{max}}$）

---

## Semiclassical and Quantum Treatment / 半经典与量子处理

### Born Approximation Cross Section / 玻恩近似截面

Differential cross section for bremsstrahlung / 韧致辐射微分截面：

$$
d\sigma = \alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \frac{p_2}{p_1} \left[ \text{angular and spin factors / 角度与自旋因子} \right]
$$

where $\alpha_f = e^2/(4\pi\epsilon_0 \hbar c) \approx 1/137$ is the fine-structure constant.
其中 $\alpha_f = e^2/(4\pi\epsilon_0 \hbar c) \approx 1/137$ 为精细结构常数。

### Bethe-Heitler Formula (extreme relativistic limit) / 贝特-海特勒公式（极端相对论极限）

For $E_1, E_2 \gg m_e c^2$ / 当 $E_1, E_2 \gg m_e c^2$ 时：

$$
d\sigma = 4 \alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \left[ \left( 1 + \left(\frac{E_2}{E_1}\right)^2 - \frac{2}{3} \frac{E_2}{E_1} \right) \left( \ln\frac{2E_1 E_2}{m_e c^2 \hbar\omega} - \frac12 \right) \right]
$$

### Screening / 屏蔽

**Complete screening** (Thomas-Fermi atom) / 完全屏蔽（托马斯-费米原子）：multiply by $F_{\text{sc}}$ (screening function) / 乘以 $F_{\text{sc}}$（屏蔽函数）：

$$
d\sigma_{\text{sc}} = d\sigma_{\text{BH}} \cdot F_{\text{sc}}(\xi)
$$

where $\xi = 100 m_e c^2 \hbar\omega / (E_1 E_2 Z^{1/3})$.
其中 $\xi = 100 m_e c^2 \hbar\omega / (E_1 E_2 Z^{1/3})$。

**No screening / 无屏蔽** ($\xi \gg 1$)：use unscreened Bethe-Heitler / 使用无屏蔽贝特-海特勒公式。

**Complete screening** ($\xi \ll 1$)：

$$
d\sigma = 4\alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \left( 1 + \left(\frac{E_2}{E_1}\right)^2 - \frac{2}{3}\frac{E_2}{E_1} \right) \left( \ln\frac{183}{Z^{1/3}} - f(Z) \right)
$$

---

## Energy Loss from Bremsstrahlung / 韧致辐射的能量损失

### Radiative Stopping Power / 辐射阻止本领

Energy-loss rate from bremsstrahlung for electrons / 电子韧致辐射的能量损失率：

$$
-\left(\frac{dE}{dx}\right)_{\text{rad}} = N \int_0^{E_1} \hbar\omega \, d\sigma
$$

Leading to / 得到：

$$
-\left(\frac{dE}{dx}\right)_{\text{rad}} = \frac{E}{X_0}
$$

where $X_0$ is the radiation length.
其中 $X_0$ 为辐射长度。

### Total Energy Loss (electrons/positrons) / 总能量损失（电子/正电子）

$$
-\frac{dE}{dx} = -\left(\frac{dE}{dx}\right)_{\text{coll}} - \left(\frac{dE}{dx}\right)_{\text{rad}}
$$

**Critical energy** $E_c$ / 临界能量 $E_c$：where $(-dE/dx)_{\text{coll}} = (-dE/dx)_{\text{rad}}$ / 碰撞损失 = 辐射损失

### Radiation Length / 辐射长度

$$
X_0 = \frac{716.4\,\text{g/cm}^2 \cdot A}{Z(Z+1)\ln(287/\sqrt{Z})}
$$

For a high-energy electron traversing $t$ radiation lengths / 对于穿过 $t$ 个辐射长度的高能电子：

$$
E(t) = E_0 e^{-t}
$$

---

## Weizsacker-Williams Method of Virtual Quanta / 魏茨泽克-威廉姆斯虚拟量子方法

### Key Idea / 核心思想
The electromagnetic field of a fast charged particle can be represented as a spectrum of virtual photons. When these virtual quanta interact with a target, the cross section = $\sigma_{\text{real-photon}} \times \text{photon spectrum}$.
快带电粒子的电磁场可以表示为一组虚拟光子的频谱。当这些虚拟量子与靶相互作用时，截面 = 真实光子截面 $\times$ 光子谱。

### Virtual Photon Spectrum / 虚拟光子谱

Number of virtual photons per unit frequency / 单位频率的虚拟光子数：

$$
I(\omega, b) = \frac{2}{\pi} \frac{z^2 \alpha_f c}{v^2} \frac{1}{\omega} \left[ K_0^2\left(\frac{\omega b}{\gamma v}\right) + \frac{v^2}{\gamma^2 c^2} K_1^2\left(\frac{\omega b}{\gamma v}\right) \right]
$$

where $K_0$, $K_1$ are modified Bessel functions, $b$ = impact parameter.
其中 $K_0$, $K_1$ 为修正贝塞尔函数，$b$ 为碰撞参数。

### Integrated Spectrum / 积分谱

Summed over all impact parameters > some minimum $b_{\min}$ / 对所有大于最小碰撞参数 $b_{\min}$ 的碰撞参数求和：

$$
N(\omega) \approx \frac{2}{\pi} \frac{z^2 \alpha_f}{c} \frac{1}{\omega} \ln\left( \frac{\gamma v}{\omega b_{\min}} \right) \quad \text{for / 条件 } \omega \ll \gamma v/b_{\min}
$$

### Applications / 应用

1. **Bremsstrahlung cross section / 韧致辐射截面**：$\sigma_{\text{brem}} = \int N(\omega) \sigma_{\gamma}(\omega) d\omega$
2. **Electro-disintegration / 电致蜕变** of nuclei: virtual photon excitation / 原子核的虚拟光子激发
3. **Pair production / 对产生** by virtual photons / 通过虚拟光子
4. **Ionization energy loss / 电离能量损失**：virtual photon absorption by atomic electrons / 原子电子对虚拟光子的吸收

---

## Connection of Virtual Quanta Method with Energy Loss / 虚拟量子方法与能量损失的联系

### Bethe-Bloch from Virtual Quanta / 从虚拟量子推导Bethe-Bloch公式

Energy loss = energy absorbed from virtual photon field / 能量损失 = 从虚拟光子场吸收的能量：

$$
-\frac{dE}{dx} = \int_0^{\infty} \hbar\omega \, n \cdot \sigma_{\gamma}^{\text{abs}}(\omega) \, N(\omega) \, d\omega
$$

Recovers the Bethe-Bloch formula / 恢复得到Bethe-Bloch公式：

$$
-\frac{dE}{dx} = \frac{4\pi z^2 e^4}{m_e v^2} N Z \ln\left( \frac{2m_e v^2}{I} \right) \quad \text{(non-relativistic / 非相对论)}
$$

### Key Insight / 关键见解
The W-W method is very general: any process that can occur with real photons also occurs with virtual photons, with cross section = $\sigma_{\text{real}} \times \text{flux of virtual quanta}$.
WW方法非常通用：任何可由真实光子发生的过程也可以通过虚拟光子发生，截面 = 真实光子截面 $\times$ 虚拟量子通量。

### Limitations / 局限性
- Valid when $\gamma \gg 1$ (ultrarelativistic) / 适用于 $\gamma \gg 1$（极端相对论）
- Assumes straight-line trajectory (small deflection) / 假设直线轨迹（小偏转）
- Impact parameter cutoff needed / 需要碰撞参数截断：$b_{\min} \sim \max(\hbar/(mc), \hbar/\gamma mc)$

---

## Key Formulas Summary / 重要公式汇总

| Concept / 概念 | Formula / 公式 |
|---------|---------|
| Classical bremsstrahlung spectrum / 经典韧致辐射谱 | $\frac{dI}{d\omega} = \frac{8}{3\pi} \frac{z^2 Z^2 e^6}{m^2 c^3 v_1^2} \frac{1}{(4\pi\epsilon_0)^3}$ |
| Bethe-Heitler cross section (relativistic) / 贝特-海特勒截面（相对论） | $d\sigma = 4\alpha_f Z^2 r_e^2 \frac{d\omega}{\omega} \ldots$ with screening / 含屏蔽 |
| Radiative energy loss / 辐射能量损失 | $-\frac{dE}{dx} = \frac{E}{X_0}$ |
| Radiation length / 辐射长度 | $X_0 \approx \frac{716.4 A}{Z(Z+1)\ln(287/\sqrt{Z})}$ g/cm² |
| Virtual photon spectrum / 虚拟光子谱 | $N(\omega) \approx \frac{2}{\pi} \frac{z^2 \alpha_f}{c} \frac{1}{\omega} \ln(\gamma v/\omega b_{\min})$ |
| Fine-structure constant / 精细结构常数 | $\alpha_f = e^2/(4\pi\epsilon_0\hbar c) \approx 1/137$ |

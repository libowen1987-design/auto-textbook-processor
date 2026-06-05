# Sadiku《Elements of Electromagnetics》Chapter 5: Electric Fields in Material Space
> **中英双语版**

Properties of conductors, polarization in dielectrics, continuity equation, and boundary conditions.

## 5.1 Current and Current Density | 电流和电流密度
$$I = \int_S \mathbf{J} \cdot d\mathbf{S}, \quad \mathbf{J} = \sigma \mathbf{E}$$
$\sigma$: conductivity (S/m), $\sigma = n e^2 \tau / m$.

## 5.2 Continuity Equation | 连续性方程
$$\nabla \cdot \mathbf{J} = -\frac{\partial \rho_v}{\partial t}$$
Consequence of charge conservation / 电荷守恒的推论。

## 5.3 Polarization in Dielectrics | 电介质中的极化
$$\mathbf{P} = \lim_{\Delta V \to 0} \frac{\sum \mathbf{p}}{\Delta V}, \quad \mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P}$$
For linear dielectrics: $\mathbf{P} = \epsilon_0 \chi_e \mathbf{E}$, $\epsilon_r = 1 + \chi_e$.

## 5.4 Boundary Conditions | 边界条件
$$E_{1t} = E_{2t}, \quad D_{1n} - D_{2n} = \rho_s$$
$$\frac{\tan\theta_1}{\tan\theta_2} = \frac{\epsilon_1}{\epsilon_2} \quad (\text{boundary refraction / 边界折射})$$

## 5.5 Capacitance | 电容
$$C = \frac{Q}{V} = \frac{\oint \mathbf{D} \cdot d\mathbf{S}}{-\int \mathbf{E} \cdot d\mathbf{l}}$$

**Parallel plate / 平行板:** $C = \epsilon S/d$
**Coaxial / 同轴:** $C = 2\pi\epsilon L / \ln(b/a)$
**Sphere / 球:** $C = 4\pi\epsilon ab/(b-a)$

---
> **本章小结：** 导体的电流密度与电场成正比（欧姆定律），电介质中的极化矢量描述了束缚电荷的分布，边界条件则是场在不同介质界面上的连续性要求。

# Sadiku《Elements of Electromagnetics》Chapter 4: Electrostatic Fields
> **中英双语版**

Coulomb's law, electric field intensity, electric flux density, Gauss's law, electric potential, energy, and conductors/dielectrics.

## 4.1 Coulomb's Law | 库仑定律
$$F = \frac{Q_1 Q_2}{4\pi\epsilon_0 R^2} \mathbf{a}_R$$
Force between two point charges / 两点电荷之间的力。

## 4.2 Electric Field Intensity | 电场强度
$$\mathbf{E} = \frac{Q}{4\pi\epsilon_0 R^2} \mathbf{a}_R \quad (\text{point charge})$$
$$\mathbf{E} = \frac{1}{4\pi\epsilon_0} \int_{L'} \frac{\rho_l d\mathbf{l}'}{R^2} \mathbf{a}_R \quad (\text{line charge})$$
$$\mathbf{E} = \frac{1}{4\pi\epsilon_0} \int_{S'} \frac{\rho_s dS'}{R^2} \mathbf{a}_R \quad (\text{surface charge})$$

## 4.3 Electric Flux Density | 电通量密度
$$\mathbf{D} = \epsilon_0 \mathbf{E}$$

## 4.4 Gauss's Law | 高斯定律
$$\oint_S \mathbf{D} \cdot d\mathbf{S} = Q_{\text{enc}}$$
Total electric flux through a closed surface equals the enclosed charge / 闭合面电通量等于面内总电荷。

## 4.5 Electric Potential | 电位
$$V(\mathbf{r}) = -\int_{\infty}^{\mathbf{r}} \mathbf{E} \cdot d\mathbf{l}, \quad \mathbf{E} = -\nabla V$$

## 4.6 Energy Density / 能量密度
$$W_e = \frac{1}{2}\epsilon E^2, \quad W = \frac{1}{2}\int_V \epsilon |E|^2 dV$$

## 4.7 Conductors | 导体
Inside a conductor: $\mathbf{E} = 0$. Surface: $\mathbf{D}_n = \rho_s$, $\mathbf{E}_t = 0$.

## 4.8 Dielectrics | 电介质
Polarization $\mathbf{P}$, relative permittivity $\epsilon_r$: $\mathbf{D} = \epsilon_0 \epsilon_r \mathbf{E}$.
Boundary conditions / 边界条件: $D_{1n} - D_{2n} = \rho_s$, $E_{1t} = E_{2t}$.

## 4.9 Poisson's and Laplace's Equations | 泊松方程和拉普拉斯方程
$$\nabla^2 V = -\frac{\rho_v}{\epsilon} \quad (\text{Poisson}), \quad \nabla^2 V = 0 \quad (\text{Laplace})$$

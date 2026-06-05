# Sadiku《Elements of Electromagnetics》Chapter 7: Time-Varying Fields and Maxwell's Equations
> **中英双语版**

## 7.1 Faraday's Law | 法拉第定律
$$\oint \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi}{dt} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S}$$
Changing magnetic flux induces EMF / 变化的磁通产生电动势。

## 7.2 Displacement Current | 位移电流
$$\mathbf{J}_d = \frac{\partial \mathbf{D}}{\partial t}$$
Maxwell's addition: changing electric flux acts as a current source for magnetic fields.
> Maxwell 的补充：变化的电通量充当磁场的电流源。

## 7.3 Maxwell's Equations in Integral Form | Maxwell 方程组的积分形式
$$\oint \mathbf{E} \cdot d\mathbf{l} = -\int_S \frac{\partial \mathbf{B}}{\partial t} \cdot d\mathbf{S} \quad \text{(Faraday)}$$
$$\oint \mathbf{H} \cdot d\mathbf{l} = \int_S (\mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}) \cdot d\mathbf{S} \quad \text{(Ampère-Maxwell)}$$
$$\oint \mathbf{D} \cdot d\mathbf{S} = \int_V \rho_v dV \quad \text{(Gauss)}$$
$$\oint \mathbf{B} \cdot d\mathbf{S} = 0 \quad \text{(Gauss for magnetism)}$$

## 7.4 Maxwell's Equations in Differential Form | Maxwell 方程组的微分形式
$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad \nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$
$$\nabla \cdot \mathbf{D} = \rho_v, \quad \nabla \cdot \mathbf{B} = 0$$

## 7.5 Time-Harmonic Fields / 时谐场
For $e^{j\omega t}$ dependence: $\partial/\partial t \to j\omega$:
$$\nabla \times \mathbf{E} = -j\omega\mathbf{B}, \quad \nabla \times \mathbf{H} = \mathbf{J} + j\omega\mathbf{D}$$

## 7.6 Poynting Theorem | 坡印廷定理
$$\nabla \cdot (\mathbf{E} \times \mathbf{H}) = -\mathbf{E} \cdot \mathbf{J} - \frac{\partial}{\partial t}\left(\frac{1}{2}\epsilon E^2 + \frac{1}{2}\mu H^2\right)$$
Power flow density: $\mathbf{P} = \mathbf{E} \times \mathbf{H}$ (Poynting vector / 坡印廷矢量, W/m²).

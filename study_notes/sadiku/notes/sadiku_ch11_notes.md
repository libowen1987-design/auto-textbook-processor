# Sadiku《Elements of Electromagnetics》Chapter 11: Antennas and Radiation
> **中英双语版**

## 11.1 Radiation Mechanism / 辐射机制
Accelerated charges or time-varying currents radiate electromagnetic waves.
> 加速电荷或时变电流辐射电磁波。

## 11.2 Hertzian Dipole / 赫兹偶极子
$$d\mathbf{E} = \frac{I_0 dl \sin\theta}{4\pi} \left( \frac{j\eta_0 k}{r} + \frac{\eta_0}{r^2} - \frac{j}{\omega\epsilon_0 r^3} \right) e^{-jkr} \mathbf{a}_\theta$$
$$d\mathbf{H} = \frac{I_0 dl \sin\theta}{4\pi} \left( \frac{jk}{r} + \frac{1}{r^2} \right) e^{-jkr} \mathbf{a}_\phi$$

**Far-field / 远场 ($kr \gg 1$):**
$$E_\theta = \frac{j\eta_0 k I_0 dl \sin\theta}{4\pi r} e^{-jkr}, \quad H_\phi = \frac{E_\theta}{\eta_0}$$

## 11.3 Antenna Parameters / 天线参数
- **Radiation intensity / 辐射强度**: $U = r^2 S_{\text{av}}$
- **Directivity / 指向性**: $D = 4\pi U_{\text{max}}/P_{\text{rad}}$
- **Gain / 增益**: $G = \eta_{\text{ant}} D$
- **Effective aperture / 有效孔径**: $A_e = \lambda^2 G/(4\pi)$
- **Input impedance / 输入阻抗**: $Z_{\text{in}} = R_{\text{rad}} + jX_{\text{in}}$

## 11.4 Half-Wave Dipole / 半波偶极子
$$E_\theta = \frac{j\eta_0 I_0 e^{-jkr}}{2\pi r} \frac{\cos(\pi/2 \cos\theta)}{\sin\theta}, \quad D = 1.64 = 2.15\;\text{dBi}$$

## 11.5 Antenna Arrays / 天线阵列
**Array factor / 阵因子 (uniform linear array / 均匀直线阵):**
$$\text{AF} = \frac{\sin(N\psi/2)}{\sin(\psi/2)}, \quad \psi = kd\cos\theta + \beta$$
Beam steering: $\beta = -kd\cos\theta_0$ / 波束指向。
Broadside: $\beta = 0$, End-fire: $\beta = \mp kd$.

## 11.6 Other Antenna Types / 其他天线类型
- Loop antenna / 环形天线
- Microstrip (patch) antenna / 微带（贴片）天线
- Horn antenna / 喇叭天线
- Reflector antenna / 反射面天线

# Sadiku《Elements of Electromagnetics》Chapter 9: Transmission Lines
> **中英双语版**

## 9.1 Transmission Line Parameters / 传输线参数
Distributed parameters: $R$ (series resistance / 串联电阻), $L$ (series inductance / 串联电感), $G$ (shunt conductance / 并联电导), $C$ (shunt capacitance / 并联电容).

## 9.2 Transmission Line Equations / 传输线方程
$$-\frac{\partial V}{\partial z} = RI + L\frac{\partial I}{\partial t}, \quad -\frac{\partial I}{\partial z} = GV + C\frac{\partial V}{\partial t}$$

**Time-harmonic / 时谐：**
$$\frac{d^2V}{dz^2} = \gamma^2 V, \quad \gamma = \sqrt{(R+j\omega L)(G+j\omega C)} = \alpha + j\beta$$

## 9.3 Characteristic Impedance / 特征阻抗
$$Z_0 = \sqrt{\frac{R+j\omega L}{G+j\omega C}} \quad \xrightarrow{\text{lossless}} \quad Z_0 = \sqrt{\frac{L}{C}}$$

## 9.4 Standing Waves and SWR / 驻波与驻波比
$$V(z) = V_0^+(e^{-j\beta z} + \Gamma e^{j\beta z}), \quad \Gamma = \frac{Z_L - Z_0}{Z_L + Z_0}$$
$$S = \frac{1+|\Gamma|}{1-|\Gamma|}, \quad \text{VSWR}$$

## 9.5 Smith Chart / 史密斯圆图
Normalized impedance: $z = Z/Z_0 = r + jx$.
Constant $r$ and $x$ circles form impedance chart / 等 $r$ 和等 $x$ 圆构成阻抗圆图。

## 9.6 Input Impedance / 输入阻抗
$$Z_{\text{in}} = Z_0 \frac{Z_L + jZ_0\tan\beta\ell}{Z_0 + jZ_L\tan\beta\ell}$$
Special cases: Open ($Z_{\text{in}} = -jZ_0\cot\beta\ell$), Short ($Z_{\text{in}} = jZ_0\tan\beta\ell$), $\lambda/4$ ($Z_{\text{in}} = Z_0^2/Z_L$).

## 9.7 Transients on Lines / 传输线瞬态
Reflection diagrams (bounce diagrams) for pulse propagation / 脉冲传播的反射图。

## 9.8 Impedance Matching / 阻抗匹配
Using quarter-wave transformer, single-stub, double-stub, or tapered lines.

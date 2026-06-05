# 廖承恩《微波技术基础》 第2章：传输线理论

> **来源：** 谢处方等，《电磁场与电磁波》，第2章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 2.1 传输线理论 | Transmission Line Theory

# 廖承恩《微波技术基础》第2章
 本笔记基于  文本清洗整理100% 来源于原书内容
## 第2章 传输线理论
### 2.1 传输线方程
**传输线 ( )**以  导模方式传送电磁波能量或信号的导行系统横向尺寸远小于工作波长
**分布参数**：$R'$（单位长度分布电阻）、$L'$（分布电感）、$C'$（分布电容）、$G'$（分布电导）
**均匀传输线**：$R', L', C', G'$ 沿线均匀分布，与距离无关。
#### 传输线方程（电报方程）
一般传输线方程（偏微分方程组）：
$$\frac{\partial v(z,t)}{\partial z} = -R' i(z,t) - L' \frac{\partial i(z,t)}{\partial t}$$
$$\frac{\partial i(z,t)}{\partial z} = -G' v(z,t) - C' \frac{\partial v(z,t)}{\partial t}$$
#### 时谐传输线方程
设电压、电流为时谐场，$v(z,t) = \mathrm{Re}\{V(z)e^{j\omega t}\}$，$i(z,t) = \mathrm{Re}\{I(z)e^{j\omega t}\}$：
$$\frac{$dV$(z)}{dz} = -(R' + j\omega L') I(z) = -\gamma Z_0 I(z)$$
$$\frac{dI(z)}{dz} = -(G' + j\omega C') V(z) = -\gamma Y_0 V(z)$$
其中传播常数 $\gamma = \alpha + j\beta = \sqrt{(R'+j\omega L')(G'+j\omega C')}$
#### 传输线特性参数
**特性阻抗**：
$$Z_0 = \sqrt{\frac{R' + j\omega L'}{G' + j\omega C'}}$$
**无耗线** ($R'=G'=0$)：
$$Z_0 = \sqrt{\frac{L'}{C'}} \quad \text{（纯电阻）}$$
**平行双导线特性阻抗**：
$$Z_0 = 120\pi \cdot \frac{1}{\varepsilon_r^{1/2}} \ln\left(\frac{2D}{d}\right) \quad [$\mathbf{D}$ \gg d]$$
**同轴线特性阻抗**：
$$Z_0 = \frac{60}{\sqrt{\varepsilon_r}} \ln\left(\frac{D}{d}\right) = \frac{138}{\sqrt{\varepsilon_r}} \log_{10}\left(\frac{D}{d}\right)$$
**平行板传输线特性阻抗**：
$$Z_0 = \frac{\eta}{\sqrt{\varepsilon_r}} \frac{h}{w} = \sqrt{\frac{L'}{C'}}$$
**传播常数**：
$$\gamma = \alpha + j\beta = \sqrt{(R'+j\omega L')(G'+j\omega C')}$$
无耗线$\ = 0$$\ = $\$\{}$
**相速度**波
$$v_p = \frac{\omega}{\beta} = \frac{1}{\sqrt{LC}} = \frac{c}{\sqrt{\varepsilon_r}}$$
**波长**：
$$\lambda = \frac{2\pi}{\beta} = \frac{v_p}{f}$$
---
### 2.2 分布参数阻抗
#### 输入阻抗
无耗线上距离负载 $d$ 处的输入阻抗：
$$Z_{in}(d) = Z_0 \frac{Z_L + jZ_0 \tan(\beta d)}{Z_0 + jZ_L \tan(\beta d)}$$
#### 反射系数
终端反射系数：
$$\Gamma_L = \frac{Z_L - Z_0}{Z_L + Z_0}$$
线上 $d$ 处反射系数（无耗线，$\beta d$ 从负载向源方向）：
$$\Gamma(d) = \Gamma_L e^{-j2\beta d}$$
#### 驻波比
$$\mathrm{VSWR} = \rho = \frac{1+|\Gamma_L|}{1-|\Gamma_L|}$$
行波系数：
$$K = \frac{1}{\mathrm{VSWR}} = \frac{1-|\Gamma_L|}{1+|\Gamma_L|}$$
#### 电压驻波最大/最小点位置
$$\beta d_{\max} = \phi_{\Gamma_L} + 2n\pi \quad \Rightarrow \quad d_{\max} = \frac{\phi_{\Gamma_L}}{2\beta} + \frac{n\lambda}{2}$$
$$\beta d_{\min} = \phi_{\Gamma_L} + (2n+1)\pi \quad \Rightarrow \quad d_{\min} = \frac{\phi_{\Gamma_L}+\pi}{2\beta} + \frac{n\lambda}{2}$$
#### 阻抗与驻波关系
在电压波腹点：$R_{\max} = \rho Z_0$
在电压波谷点：$R_{\min} = Z_0 / \rho$
---
### 2.3 无耗线工作状态分析
#### 1. 行波状态（无反射）
条件$ = 0$$\ = 0$$\{} = 1$
- 沿线电压电流振幅不变
- 沿线各点阻抗均等于 $Z_0$
#### 2. 驻波状态（全反射）
条件：$Z_L = 0$（短路）、$Z_L = \infty$（开路）、$Z_L = jX_L$（纯电抗）
**终端短路线**：
$$Z_{in}(d) = jZ_0 \tan(\beta d)$$
- $d=0$：$Z_{in}=0$（电压波节、电流波腹）
- $d=$\lambda$/4$：$Z_{in}=\infty$（并联谐振）
**终端开路线**：
$$Z_{in}(d) = -jZ_0 \cot(\beta d)$$
- $d=0$：$Z_{in}=\infty$（电压波腹、电流波节）
- $d=$\lambda$/4$：$Z_{in}=0$（串联谐振）
#### 3. 行驻波状态（部分反射）
条件：$Z_L$ 为一般复阻抗，$0<|\Gamma_L|<1$
沿线电压振幅范围：$[V_{\min}, V_{\max}]$
---
### 2.4 有耗线特性与计算
#### 损耗对传输线特性的影响
- 导体衰减常数 $\alpha_c = \frac{R'}{2Z_0}$（N p/m）
- 介质衰减常数 $\alpha_d = \frac{G'}{2Y_0}$（N p/m）
总衰减：$\alpha = \alpha_c + \alpha_d$（dB/m）
#### 入力功率与效率
$$$\mathbf{P}$_{in} = \frac{|V_0|^2}{2Z_0} \frac{1 - e^{-2\alpha l}}{1 - |\Gamma|^2 e^{-2\alpha l}}$$
$$\eta = \frac{$\mathbf{P}$_{in} - $\mathbf{P}$_{out}}{$\mathbf{P}$_{in}} = \frac{\text{损耗功率}}{输入功率}$$
---
### 2.5 史密斯圆图 (Smith Chart)
复平面上 $|\Gamma| = 1$ 的单位圆。
- 归一化阻抗 $\tilde{Z} = Z/Z_0$ 的正实部半圆 $\rightarrow$ 等电阻圆（单位圆内）
- 归一化阻抗 $\tilde{Z}$ 的正虚部半圆 $\rightarrow$ 等电抗圆（单位圆内）
**史密斯圆图用途**：
1. 已知 $\$读出 $\$$\(\)$
2. 已知 $Z_L$，求 $Z_{in}(d)$（沿等 $|\Gamma|$ 圆旋转）
3. 阻抗匹配（单枝节、双枝节、$$\lambda$/4$ 变换器）
 $\$ 与  的读法
- $|\Gamma|$：径向线上读数，$|\Gamma| = \frac{\rho - 1}{\rho + 1}$
- 等反射系数圆与正实轴交点${\}/0$
#### 阻抗匹配基本原理
通过添加一段特性阻抗为 $Z_0$ 的无耗线，使负载与馈线特性阻抗匹配。
---
### 2.6 阻抗匹配
#### 单枝节匹配
短路或开路单枝节，并联于主传输线。调节枝节长度 $l_s$ 和位置 $d_s$ 实现匹配。
匹配条件：$Y_{in} = Y_0 + jB_s + Y_s = Y_0$
#### 双枝节匹配
两段平行枝节，调节两段长度实现任意负载匹配。
#### $$\lambda$/4$ 阻抗变换器
长度为 $$\lambda$/4$，特性阻抗为 $Z_{opt} = \sqrt{Z_0 Z_L}$ 的均匀无耗线段。
---
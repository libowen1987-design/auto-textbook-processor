# 廖承恩《微波技术基础》 第?章：未知

> **来源：** 谢处方等，《电磁场与电磁波》，第?章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## ?.1 未知 | Unknown

# 廖承恩《微波技术基础》笔记
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
## 第3章 规则金属波导
### 3.1 矩形波导
矩形波导截面尺寸 $ \ $$  $传输  或  模不能传输  模
#### 波动方程（Helmholtz）
$$\nabla^2 $\mathbf{E}$ + $\mathbf{k}$^2 $\mathbf{E}$ = 0, \quad $\mathbf{k}$ = \frac{2\pi}{\lambda} = $\omega$\sqrt{$\mu$\varepsilon}$$
矩形波导中 $(x,y)$ 方向的边界条件为Dirichlet（理想导体边界）。
  模$ = 0$$ \ 0$
$$$\mathbf{H}$_z(x,y,z) = $\mathbf{H}$_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}$$
截止波数：$$\mathbf{k}$_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$
#### 截止波长
$$\lambda_c = \frac{2}{\sqrt{(m/a)^2 + (n/b)^2}}$$
主模 ${10}$$\ = 2$$ = /\tag{2}$
#### 传播常数
$$\gamma = \alpha + j\beta = \sqrt{$\mathbf{k}$_c^2 - $\mathbf{k}$^2}$$
- $$\mathbf{k}$ > $\mathbf{k}$_c$（$f > f_c$）：$\alpha = 0$，$\beta = \sqrt{$\mathbf{k}$^2 - $\mathbf{k}$_c^2}$，**传播**
- $$\mathbf{k}$ < $\mathbf{k}$_c$（$f < f_c$）：$\alpha > 0$，$\beta = 0$，**截止**
#### 相速度和群速度
$$v_p = \frac{\omega}{\beta} = \frac{v}{\sqrt{1 - ($\lambda$/\lambda_c)^2}} > v$$
$$v_g = \frac{d\omega}{d\beta} = v\sqrt{1 - ($\lambda$/\lambda_c)^2} < v$$
$$v_p \cdot v_g = v^2$$
#### 波导波长
$$\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1 - ($\lambda$/\lambda_c)^2}}$$
 传输功率${}$ 模
$$$\mathbf{P}$ = \frac{1}{2} \int_0^a \int_0^b \mathrm{Re}($\mathbf{E}$_x $\mathbf{H}$_y^* - $\mathbf{E}$_y $\mathbf{H}$_x^*) dx\,dy = \frac{a b}{4Z_{TE}} |$\mathbf{H}$_0|^2 (1+\delta_{m0})(1+\delta_{n0})$$
其中 ${} = $\$/\{1-($\$/\)^2}$ 为  模的波阻抗
---
### 3.2 圆波导
圆形波导截面半径为 $$传输  和  模用柱坐标系 $(\)$ 分析
#### 模式方程
${}$$( ) = 0$$ = \{}/$$\{}$ 为 $$ 阶贝塞尔函数导数的第 $$ 个根
${}$$( ) = 0$$ = \{}/$$\{}$ 为 $$ 阶贝塞尔函数的第 $$ 个根
#### 常用模式
- ${11}$主模$\ = 1.706$
- ${01}$对称模式$\ = 2.613$
- ${01}$低损耗模式圆波导通信
---
### 3.3 微带传输线
**微带线 ( )**介质基片上印刷导体带的传输线工作于准  模
#### 特性参数计算
有效介电常数：
$$\varepsilon_e = \frac{1+\varepsilon_r}{2} \cdot \frac{1+\tanh(1.45h/w)}{1+1.45h/w}$$
特性阻抗（窄带，$w/h > 1$）：
$$Z_0 = \frac{60}{\sqrt{\varepsilon_e}} \ln\left(\frac{8h}{w} + \frac{w}{4h}\right)$$
宽导体带（$w/h > 2$）：
$$Z_0 = \frac{\pi}{2\sqrt{2\varepsilon_r}} \cdot \frac{h}{w}$$
#### 波长和相速度
$$\lambda = \frac{\lambda_0}{\sqrt{\varepsilon_e}}, \quad v_p = \frac{c}{\sqrt{\varepsilon_e}}$$
---
## 第6章 微波网络基础
### 6.1 微波网络概述
微波电路可等效为微波网络，用网络参数描述。
#### 网络端口
$n$ 端口网络：有 $n$ 个微波端口（或参考面）。
### 6.2 一端口网络的阻抗特性
- **谐振频率**：$X($\omega$) = 0$（电抗为零）
- **品质因数 $$**$ = \{\0}{2} \\{}{\}\{\0} = \{\0 }{} = \{1}{\0 }$串联谐振
### 6.3 阻抗矩阵和导纳矩阵
**阻抗矩阵 $[Z]$**：$V_i = \sum_j Z_{ij} I_j$
**导纳矩阵 $[Y]$**：$I_i = \sum_j Y_{ij} V_j$
对于互易网络（无各向异性媒质）：$Z_{ij} = Z_{ji}$，$Y_{ij} = Y_{ji}$，矩阵为对称矩阵。
对于对称网络：$[Z]$ 或 $[Y]$ 有对称性特征值。
### 6.4 散射矩阵 $[$\mathbf{S}$]$
**散射矩阵**描述端口归一化入射波与归一化反射波的关系：
$$b = [$\mathbf{S}$] a$$
$$$\mathbf{S}$_{ij} = \frac{b_i}{a_j}\bigg|_{a_$\mathbf{k}$=0($\mathbf{k}$\neq j)}$$
物理含义：端口 $j$ 入射，端口 $i$ 反射。
**性质**：
- 互易网络：$[$\mathbf{S}$]^T = [$\mathbf{S}$]$（对称）
- 无耗网络：$[$\mathbf{S}$]^{+}[$\mathbf{S}$] = [I]$（么正性，$$\mathbf{S}$^\dagger $\mathbf{S}$ = I$）
- 对称端口网络：$[$\mathbf{S}$]$ 的本征值为 $\pm 1$
**$S$ 参数物理意义**：
- $$\mathbf{S}$_{11}$：端口 1 的反射系数（输入匹配）
- $$\mathbf{S}$_{21}$：端口 1 到端口 2 的传输系数（前向增益）
- $$\mathbf{S}$_{12}$：端口 2 到端口 1 的传输系数（反向增益）
- $$\mathbf{S}$_{22}$：端口 2 的反射系数（输出匹配）
 6.5  矩阵传输矩阵
$[]$ 矩阵描述两端口网络的链式连接
$$\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} $\mathbf{A}$ & $\mathbf{B}$ \\ C & $\mathbf{D}$ \end{bmatrix} \begin{bmatrix} V_2 \\ -I_2 \end{bmatrix}$$
**级联**：
$[ABCD]_{total} = [ABCD]_1 \cdot [ABCD]_2$
**常用元件的 $[]$**
- 串联阻抗 $Z$：$[$\mathbf{A}$,$\mathbf{B}$;C,$\mathbf{D}$] = [1,Z;0,1]$
- 并联导纳 $Y$：$[$\mathbf{A}$,$\mathbf{B}$;C,$\mathbf{D}$] = [1,0;Y,1]$
- 特性阻抗 $Z_0$、电长度 $\theta$ 的传输线段：$[$\mathbf{A}$,$\mathbf{B}$;C,$\mathbf{D}$] = [\cos$\theta$, jZ_0\sin$\theta$; j\frac{1}{Z_0}\sin$\theta$, \cos$\theta$]$
---
## 第7章 微波谐振器
### 7.1 谐振器的基本特性与参数
**谐振频率 $\omega_0$**：电纳 $$\mathbf{B}$($\omega$) = 0$ 的频率（或电抗 $X($\omega$) = 0$）
**品质因数 $Q$**：
$$Q = \frac{\omega_0 W}{$\mathbf{P}$_L} = \frac{\text{谐振器存储的能量}}{\text{每周期损耗的能量}} \times 2\pi$$
其中 $W$ 为存储能量，$$\mathbf{P}$_L$ 为损耗功率。
**带宽 $$**
$$BW = \frac{f_0}{Q}$$
**有载 $Q_L$**：
$$\frac{1}{Q_L} = \frac{1}{Q_U} + \frac{1}{Q_e}$$
$Q_U$ 为无载 $Q$（固有品质因数），$Q_e$ 为外部品质因数（耦合品质因数）。
### 7.2 串联和并联谐振电路
**串联谐振**：
- 谐振时 $Z \approx R$，$X=0$
- $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR}$
- 阻抗频率响应：$|Z| \approx R\sqrt{1 + Q^2(2$\Delta$$\omega$/\omega_0)^2}$
**并联谐振**：
- 谐振时 $Y \approx G$，$$\mathbf{B}$=0$
- $Q = \frac{\omega_0 C}{G} = \frac{R}{\omega_0 L}$
- 阻抗频率响应：$|Z| \approx R\sqrt{1 + Q_L^2(2$\Delta$$\omega$/\omega_0)^2}$
### 7.3 金属波导谐振腔
**矩形谐振腔**：由电壁围成的金属腔体，尺寸 $a \times b \times d$，内部填充均匀介质。
**模式 $\{}{}$$\{}{}$**
$$f_{mnp} = \frac{c}{2\sqrt{\varepsilon_r}} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2 + \left(\frac{p}{d}\right)^2}$$
**品质因数 $Q$**（导体损耗）：
$$Q \approx \frac{1}{\alpha_c} \left(\frac{2\pi}{\lambda_g}\right) \propto \frac{1}{\delta_s}$$
其中 $\delta_s$ 为趋肤深度，$\alpha_c$ 为导体衰减常数。
### 7.4 介质谐振器
使用高介电常数 ($\varepsilon_r \approx 30-100$) 低损耗介质材料制成，尺寸远小于工作波长。
**$\{}{01\}$ 模式**主模$$ 高可达 $10^4$ 量级
---
## 第8章 常用微波元件
### 8.1 一端口元件
**短路活塞**、**抗流结构 (Choke)**、**匹配负载 (Matched Load)**
### 8.3 二端口元件
**衰减器 (Attenuator)**：用吸收材料（如吸收片）或非互易特性（如铁氧体）实现。
**移相器 (Phase Shifter)**：改变信号相位，常用介质片或铁氧体。
### 8.4 四端口元件
**定向耦合器 (Directional Coupler)**：方向性将主波导功率耦合到副波导。
**环形器 (Circulator)**：三端口或四端口非互易元件，基于铁氧体制成。
---
## 附录：常用物理常数
| 常数 | 符号 | 值 |
|------|------|-----|
| 真空光速 | $c$ | $2.998 \times 10^8$ m/s |
| 真空阻抗 | $\eta_0$ | $376.73\ \Omega \approx 377\ \Omega$ |
| 真空介电常数 | $\varepsilon_0$ | $8.854 \times 10^{-12}$ $\mathbf{F}$/m |
| 真空磁导率 | $\mu_0$ | $4\pi \times 10^{-7}$ $\mathbf{H}$/m |
| 电子电荷 | $e$ | $1.602 \times 10^{-19}$ C |
---
## 第4章 圆波导 (Circular Waveguide)
圆波导是内壁为圆柱形的金属波导，因其轴对称性而具有独特的传输特性。
### 4.1 圆波导的导模
圆波导中传输  和  模两类导模不能传输  模因为需要双导体
**${\{}}$ 模**横电模$ \ 0  = 0$
截止波长：
$$\lambda_c = \frac{2\pi a}{\chi'_{mn}}$$
其中 $\chi'_{mn}$ 是 $m$ 阶贝塞尔函数导数 $$\mathbf{J}$'_m(x) = 0$ 的第 $n$ 个根。
**${\{}}$ 模**横磁模$ \ 0  = 0$
截止波长：
$$\lambda_c = \frac{2\pi a}{\chi_{mn}}$$
其中 $\chi_{mn}$ 是 $m$ 阶贝塞尔函数 $$\mathbf{J}$_m(x) = 0$ 的第 $n$ 个根。
### 4.2 重要模式
| 模式 | $\chi'_{mn}$ 或 $\chi_{mn}$ | $\lambda_c / a$ | 特点 |
|------|---------------------------|-----------------|------|
 ${11}$  1.8412  3.412  **主模**$\$ 最大 
 ${01}$  2.405  2.613  圆对称无极化简并 
 ${01}$  3.832  1.640  低损耗模适合远距离传输 
**主模 ${11}$ 的截止波长** $\ \ 3.41$是最长截止波长的模式
### 4.3 圆波导的传输特性
**传输条件**：$\lambda < \lambda_c$（工作波长小于截止波长）或 $f > f_c$。
**极化简并**${\{}}$ 模含 ${11}$ 主模存在极化简并沿圆周方向有两种场分布 $\(\)$ 和 $\(\)$截止波长相同但极化方向正交
这使得圆波导一般不宜用作传输系统（多用矩形波导），但可利用极化简并构成双极化元件。
**${01}$ 模**无极化简并$=0$场分布具有轴对称性特别适合用作天线扫描装置的旋转关节
**${01}$ 模**是低损耗模管壁电流只有 $\$ 分量趋肤效应导致的导体损耗随频率升高而减小毫米波远距离传输的优选模式
 4.4 ${\{}}$ 模的传播常数与波阻抗
$$\beta = \sqrt{$\mathbf{k}$^2 - $\mathbf{k}$_c^2}, \quad $\mathbf{k}$ = \frac{2\pi}{\lambda}$$
波阻抗：
$$Z_{\mathrm{TE}} = \frac{\eta}{\sqrt{1 - ($\lambda$/\lambda_c)^2}}, \quad \eta \approx 377\ \Omega$$
### 4.5 例题（例3.2-1）
半径 $a = 0.5$ cm，填充 $\varepsilon_r = 2.25$ 的圆波导，前两个传输模的截止频率：
- TE$_{11}$: $\chi'_{11} = 1.8412$, $f_c = \frac{c}{2\pi a/\chi'_{11}} \approx 17.6$ GHz
- TM$_{01}$: $\chi_{01} = 2.405$, $f_c \approx 22.9$ GHz
工作频率 $ = 13$  时两模均已截止单模传输的条件要求 $    {{01}}$
---
## 第8章 阻抗匹配 (Impedance Matching)
阻抗匹配是使微波电路或系统无反射、尽量接近行波状态的技术措施，是微波电路设计的关键问题。
### 8.1 阻抗匹配的重要性
1. **功率传输最大**：匹配时传输给负载的功率最大，馈线损耗最小
2. **避免击穿**：阻抗失配时传输大功率易导致击穿
3. **信号源稳定**：反射波对信号源产生频率牵引，可能使信号源工作不稳定
### 8.2 阻抗匹配问题
两类基本匹配问题：
1. **负载与传输线匹配**：使 $Z_L = Z_0$，消除负载端反射
2. **信号源与传输线匹配**：使 $Z_{in} = Z_0^*$（共轭匹配），使信号源输出功率最大
### 8.3 $\lambda$/4 阻抗变换器
对于纯电阻负载 $R_L$，在负载与传输线之间接入一段长度为 $$\lambda$/4$、特性阻抗为 $Z_{01}$ 的传输线：
$$Z_{01} = \sqrt{R_L \cdot Z_0}$$
此时从变换器输入端看进去的输入阻抗正好等于 $Z_0$，实现匹配。
**带宽特性**：$\lambda$/4 变换器的匹配是窄带的，工作频率偏离中心时反射增大。
### 8.4 双支节调配器
在主线中加入两个并联短路支节，通过调节两支节的长度 $l_1$、$l_2$ 使负载得到匹配。
- 两支节间距通常取 $$\lambda$/8$、$$\lambda$/4$、$3$\lambda$/8$ 等
- 调节自由度：两个变量（两支节长度）解决两个条件（实部=1，虚部=0）
### 8.5 渐变线匹配
用一段长度较长（如 $10\lambda$ 以上）的渐变线实现宽频带匹配。渐变线特性阻抗从 $Z_0$ 渐变到 $Z_L$，使反射逐渐产生并累加抵消。
常用形式：指数线、克洛普芬斯坦线、直线式、三角式、切比雪夫式。
---
## 第9章 定向耦合器 (Directional Coupler)
定向耦合器是具有方向性的四端口元件，可将主线中的功率按一定比例耦合到副线。
### 9.1 基本参数
**耦合度 $C$**（Coupling）：
$$C = 10\log_{10}\frac{$\mathbf{P}$_1}{$\mathbf{P}$_3}\ (\mathrm{dB})$$
**定向性 $D$**（Directivity）：
$$$\mathbf{D}$ = 10\log_{10}\frac{$\mathbf{P}$_3}{$\mathbf{P}$_4} = C_{dB} - I_{dB}\ (\mathrm{dB})$$
**隔离度 $I$**（Isolation）：
$$I = 10\log_{10}\frac{$\mathbf{P}$_1}{$\mathbf{P}$_4}\ (\mathrm{dB})$$
**回波损耗**：端口输入端的反射损耗。
### 9.2 无耗互易四端口网络的基本性质
无耗互易四端口网络的散射矩阵具有么正性 $[$\mathbf{S}$][$\mathbf{S}$]^+ = [I]$，由此推导出重要性质：
1. **完全匹配的无耗互易四端口 = 理想定向耦合器**
2. **理想定向性不一定需要四个端口均匹配**（匹配是充分条件，非必要）
3. **两个端口匹配且相互隔离 \rightarrow 另两个端口也匹配隔离**
### 9.3 理想定向耦合器的 $[$\mathbf{S}$]$ 矩阵
理想定向耦合器的 $S$ 矩阵只有三种形式，对应三种类型：
$$[$\mathbf{S}$_1] = \begin{bmatrix} 0 & $\mathbf{k}$ & t & 0 \\ $\mathbf{k}$ & 0 & 0 & t \\ t & 0 & 0 & $\mathbf{k}$ \\ 0 & t & $\mathbf{k}$ & 0 \end{bmatrix}$$
其中 $$\mathbf{k}$^2 + t^2 = 1$，$k$ 为耦合系数，$t$ 为直通系数。
**自由度**：除相位参考面外，理想定向耦合器仅有一个自由度（决定 $k$ 或 $t$）。
### 9.4 双分支定向耦合器
基于耦合微带线或波导分支线实现。3 dB 耦合器的分支线特性阻抗：
$$Z_{02} = Z_0\sqrt{2} \approx 70.7\ \Omega$$
### 9.5 耦合带状线耦合器
使用奇偶模分析法。耦合系数：
$$C = \frac{Z_{0e} - Z_{0o}}{Z_{0e} + Z_{0o}}$$
设计时需根据耦合度确定奇偶模特性阻抗，然后查表或计算介质厚度和耦合间距。
---
## 第10章 微波滤波器 (Microwave Filters)
滤波器是微波系统中用于选择频率成分的无源网络。
### 10.1 滤波器的基本参数
**通带纹波**：切比雪夫滤波器的通带等纹波值（通常 0.1 dB ~ 3 dB）。
**阻带衰减**：阻带最小衰减量（如 30 dB、40 dB）。
**截止频率 $f_c$**：通带与阻带的边界频率。
**带宽 $$**3  带宽1  带宽等
### 10.2 低通原型滤波器
通过频率变换可从低通原型获得高通、带通、带阻滤波器。
切比雪夫低通原型的元件值 $g_0, g_1, \ldots, g_{N+1}$ 可由滤波器设计表查得。
**阶数估算**：对于阻带衰减要求 $$\mathbf{A}$_s$ dB，归一化阻带频率 $\omega_s$：
$$N \approx \frac{$\mathbf{A}$_s}{20\log_{10}(\omega_s)}$$
### 10.3 频率变换
- **低通 \rightarrow 高通**：$\omega \to -\omega_c/\omega$
- **低通 \rightarrow 带通**：$\omega \to ($\omega$^2 - \omega_0^2)/(\omega \cdot $\Delta$$\omega$)$
- **低通 \rightarrow 带阻**：$\omega \to $\omega$\cdot$\Delta$$\omega$/(\omega_0^2 - $\omega$^2)$
### 10.4 阶跃阻抗低通滤波器
使用高阻抗线（$Z_H$）和低阻抗线（$Z_L$）交替构成，每节长度约为 $$\lambda$/8 \sim $\lambda$/4$。
- 高阻抗线：窄导体带，$Z_$\mathbf{H}$ = 80 \sim 120\ \Omega$
- 低阻抗线：宽导体带，$Z_L = 20 \sim 50\ \Omega$
每两节约提供 20 dB/十倍频程的阻带衰减。
### 10.5 平行耦合线带通滤波器
多节耦合线级联构成，每节提供一定的耦合量。$N$ 节滤波器可获得 $N+1$ 个谐振器对应的带宽响应。
设计需要查耦合线设计曲线或使用全波仿真 等精确计算
### 10.6 滤波器设计流程
1. 确定规格$0$$$通带纹波阻带衰减
2. 选择滤波器类型（切比雪夫、巴特沃斯、椭圆等）
3. 计算阶数 $N$
4. 查表或计算低通原型元件值
5. 进行频率变换得到实际元件参数
6. 使用全波仿真验证和优化
# Collins Chapter 6 — Passive Microwave Devices (无源微波器件)

> 来源：Collin, *Foundations for Microwave Engineering*, 2nd Ed., Ch.6, pp. 371–490

---

## §6.1 波导接头与变换器 (Waveguide Joints and Transitions)

### §6.1.1 E 面弯头和 H 面弯头 (E-Plane and H-Plane Bends)

- **E 面弯头 (E-plane bend)**：在电场平面（窄边方向）弯曲，改变波导高度方向传播
- **H 面弯头 (H-plane bend)**：在磁场平面（宽边方向）弯曲，改变宽边方向传播
- 弯头等效为一段传输线，附带不连续电抗
- 曲率半径 $R$ 需足够大（通常 $R \ge 1.5\lambda_g$）以减小反射
- 突变弯头（mitered bend）用切角补偿，切角深度 ≈ $0.5a$（宽边尺寸）可获得最佳匹配

### §6.1.2 扭波导 (Waveguide Twist)

- 将波导截面旋转 90° 改变极化方向
- 渐变扭波导长度通常取 $L \ge 2\lambda_g$ 以保持低驻波
- 等效为极化旋转器，理想情况下无附加反射

### §6.1.3 渐变段 (Tapered Transitions)

- 波导尺寸渐变或从波导到同轴线的过渡
- **指数渐变 (Exponential taper)**：特征阻抗 $Z(z) = Z_0 e^{\alpha z}$，反射系数：
  \[
  \Gamma \approx \frac{1}{2} \int_0^L \frac{d}{dz}[\ln Z(z)] e^{-j2\beta z} dz
  \]
- **Klopfenstein 渐变**：切比雪夫等波纹响应，在给定长度下获得最小带内反射
- **余弦平方渐变 (cosine-squared taper)**：导纳 $Y(z) = Y_0 + (Y_L - Y_0)\sin^2(\pi z/2L)$，旁瓣抑制优良

### §6.1.4 同轴-波导转接 (Coax-to-Waveguide Transition)

- 探针型：同轴内导体伸入波导充当辐射探针
- 探针深度 $d$ 及到短路板距离 $l$ 需优化
- 一般 $l \approx \lambda_g/4$，探针与波导宽边中心线平行
- 带宽可达 40%，VSWR < 1.25

---

## §6.2 波导分支与合成 (Waveguide Branching and Combining)

### §6.2.1 E 面 T 形分支 (E-Plane T-Junction)

- 分支在波导窄边方向引出，电场在分支面内
- 等效电路：串联分支
- 输入匹配度差，通常需加调谐元件

### §6.2.2 H 面 T 形分支 (H-Plane T-Junction)

- 分支在波导宽边方向引出，磁场在分支面内
- 等效电路：并联分支
- 类似 E 面分支，需匹配网络

### §6.2.3 Magic-T (魔 T)

- 由 E 面和 H 面 T 形分支组合而成
- S 参数矩阵（理想情况）：
  \[
  [S] = \frac{1}{\sqrt{2}}
  \begin{bmatrix}
  0 & 0 & 1 & 1 \\
  0 & 0 & 1 & -1 \\
  1 & 1 & 0 & 0 \\
  1 & -1 & 0 & 0
  \end{bmatrix}
  \]
  端口定义：1=H臂(Σ), 2=E臂(Δ), 3/4=共线臂
- 特性：
  - 端口 1(H) 输入 → 端口 3 和 4 等幅同相
  - 端口 2(E) 输入 → 端口 3 和 4 等幅反相
  - 端口 1 与 2 隔离（$S_{12}=0$）
  - 端口 3 与 4 隔离（$S_{34}=0$）
- 应用：平衡混频器、单脉冲雷达和差器、功率合成/分配

### §6.2.4 混合环 (Hybrid Ring / Rat-Race Coupler)

- 环形波导结构，周长 $3\lambda_g/2$
- 端口间隔：
  \[
  \begin{aligned}
  &\text{相邻端口间距} = \lambda_g/4 \\
  &\text{和/差端口间距} = 3\lambda_g/4
  \end{aligned}
  \]
- S 参数矩阵：
  \[
  [S] = -\frac{j}{\sqrt{2}}
  \begin{bmatrix}
  0 & 0 & 1 & 1 \\
  0 & 0 & -1 & 1 \\
  1 & -1 & 0 & 0 \\
  1 & 1 & 0 & 0
  \end{bmatrix}
  \]
- 带宽约 20%，低于 Magic-T 但结构更紧凑

---

## §6.3 阻抗变换器与匹配元件 (Impedance Transformers and Matching Elements)

### §6.3.1 波导螺钉 (Waveguide Screws / Tuning Screws)

- 从波导宽边中心线伸入的金属螺钉
- 等效为并联电纳 $jB$
- 螺钉深度 $h$ 与归一化电纳关系：
  \[
  \frac{B}{Y_0} = \frac{4b}{\lambda_g} \ln\left(\csc\frac{\pi h}{2b}\right)
  \]
  其中 $b$ 为波导窄边高度
- 螺钉穿出深度的变化可等效为从电容性到电感性

### §6.3.2 膜片 (Irises / Diaphragms)

- **容性膜片 (Capacitive iris)**：在宽边插入，窄孔：
  \[
  \frac{B}{Y_0} \approx \frac{4b}{\lambda_g} \ln\left(\csc\frac{\pi d}{2b}\right)
  \]
  其中 $d$ 为膜片开口高度
- **感性膜片 (Inductive iris)**：在窄边插入，窄缝：
  \[
  \frac{X}{Z_0} \approx \frac{a}{\lambda_g} \tan^2\frac{\pi w}{2a}
  \]
  其中 $w$ 为膜片开口宽度，$a$ 为宽边尺寸
- **谐振窗 (Resonant window)**：同时具容性和感性，在某频率下谐振

### §6.3.3 窗孔 (Windows)

- 用于波导间能量耦合（参见 §6.4 定向耦合器）
- 小圆孔耦合系数：
  \[
  C = -20\log_{10}|S_{13}| \quad\text{(dB)}
  \]
- 磁极化率 $\alpha_m$ 和电极化率 $\alpha_e$ 决定耦合度

### §6.3.4 渐变器 (Tapers)

- 参见 §6.1.3
- **同轴渐变线**：特征阻抗沿长度缓慢变化
  \[
  Z(z) = \sqrt{Z_{in} Z_L} \quad\text{(指数渐变)}
  \]
- **Chebyshev 渐变**：控制最大反射系数 $\Gamma_m$ 与过渡长度 $L$ 的关系：
  \[
  \Gamma(\theta) = \Gamma_m e^{-j\beta L} \frac{T_{N}(\sec\theta_m \cos\theta)}{T_N(\sec\theta_m)}
  \]
  其中 $\theta = \beta L$，$\theta_m$ 为通带边界

---

## §6.4 定向耦合器 (Directional Couplers)

### §6.4.1 基本参数

- 耦合度 $C$ (Coupling)：$C = -20\log_{10}|S_{13}|$ (dB)
- 方向性 $D$ (Directivity)：$D = -20\log_{10}\frac{|S_{14}|}{|S_{13}|}$ (dB)
- 隔离度 $I$ (Isolation)：$I = -20\log_{10}|S_{14}|$ (dB)
- 三者关系：$I = C + D$

### §6.4.2 Bethe 小孔理论 (Bethe's Small-Hole Theory)

- 波导公共壁上的小圆孔，等效为电极化偶极子和磁极化偶极子
- 电极化率 $\alpha_e$ 和磁极化率 $\alpha_m$：
  \[
  \alpha_e = \frac{2}{3} r^3, \quad \alpha_m = \frac{4}{3} r^3
  \]
  其中 $r$ 为圆孔半径
- 耦合电压幅值与孔位置的关系：
  \[
  \frac{V_3}{V_1} \propto j\omega (\alpha_e \mathbf{E}_1 \cdot \mathbf{E}_2 + \mu_0 \alpha_m \mathbf{H}_1 \cdot \mathbf{H}_2)
  \]
- **单孔定向耦合器**：在波导宽边中心线（$x=a/2$）开孔，因电场平行、磁场反平行，可实现定向耦合
- 孔偏移 $x_0$ 对耦合度的影响：
  \[
  C \approx -20\log_{10}\left[ j\omega \frac{4r^3}{3} \mu_0 H_0^2 \sin\frac{\pi x_0}{a} \right]
  \]

### §6.4.3 多孔定向耦合器 (Multi-Hole Directional Coupler)

- 利用多孔阵列增强方向性
- N 个等间距孔，间距 $d = \lambda_g/4$：
  \[
  \frac{S_{13}(\theta)}{S_{13}(0)} = \frac{\sin(N\theta)}{N\sin\theta}
  \]
  其中 $\theta = \pi(\lambda_{g0}/\lambda_g - 1)/2$，$\lambda_{g0}$ 为中心频率导波波长
- 方向性：
  \[
  D = 20\log_{10}\left|\frac{S_{13}}{S_{14}}\right|
  \]
- **Chebyshev 方向性**：利用切比雪夫多项式在通带内等波纹优化
- **Binomially weighted array**：二项式加权获得最大平坦方向性
- 3 孔、5 孔、7 孔常见，孔越多带宽越宽

### §6.4.4 分支线耦合器 (Branch-Line Coupler)

- 微带/带状线结构，四端口
- 分支线特性阻抗 $Z_0/\sqrt{2}$，主线 $Z_0$
- 3 dB 分支线耦合器 S 参数：
  \[
  [S] = -\frac{1}{\sqrt{2}}
  \begin{bmatrix}
  0 & j & 1 & 0 \\
  j & 0 & 0 & 1 \\
  1 & 0 & 0 & j \\
  0 & 1 & j & 0
  \end{bmatrix}
  \]
- 端口 1 输入 → 端口 2 和 3 各得一半功率，相位差 90°
- 带宽约 10–20%，$Z_0/\sqrt{2}$ 分支 → 3 dB

### §6.4.5 Lange 耦合器 (Lange Coupler)

- 四指交错微带耦合器
- 多段 $\lambda/4$ 耦合线段交错连接，实现紧耦合（3 dB）
- 带宽可达一个倍频程以上（1–2 倍频）
- 制造精度要求高，需精确控制线宽 $w$ 和间距 $s$
- 偶模特性阻抗 $Z_{0e}$ 和奇模特性阻抗 $Z_{0o}$：
  \[
  Z_0 = \sqrt{Z_{0e} Z_{0o}}
  \]
- 耦合度：$C = 20\log_{10}\frac{Z_{0e} - Z_{0o}}{Z_{0e} + Z_{0o}}$ (dB)

---

## §6.5 铁氧体器件 (Ferrite Devices)

### §6.5.1 铁氧体材料特性

- 铁氧体在直流偏置磁场下呈现旋磁各向异性
- **Polder 张量磁导率 (Polder permeability tensor)**：
  \[
  \overline{\overline{\mu}} = \mu_0
  \begin{bmatrix}
  \mu & -j\kappa & 0 \\
  j\kappa & \mu & 0 \\
  0 & 0 & \mu_z
  \end{bmatrix}
  \]
  其中：
  \[
  \mu = 1 + \frac{\omega_0 \omega_m}{\omega_0^2 - \omega^2},\quad
  \kappa = \frac{\omega \omega_m}{\omega_0^2 - \omega^2},\quad
  \mu_z = 1
  \]
- $\omega_0 = \gamma \mu_0 H_0$ 为拉莫尔进动频率
- $\omega_m = \gamma \mu_0 M_s$，$M_s$ 为饱和磁化强度
- $\gamma = 1.759 \times 10^{11}$ rad/(s·T) 为旋磁比
- 或写为 $\gamma = 2.21 \times 10^5$ rad/(s·A/m) 配合 cgs 单位
- 等效标量磁导率：
  \[
  \mu_{\text{eff}} = \frac{\mu^2 - \kappa^2}{\mu}
  \]

### §6.5.2 法拉第旋转 (Faraday Rotation)

- 线极化波沿偏置磁场方向传播时，极化面旋转
- 法拉第旋转角：
  \[
  \theta_f = \frac{\omega}{2c} (\sqrt{\mu_+ \epsilon} - \sqrt{\mu_- \epsilon}) l
  \]
  其中 $\mu_\pm = \mu \pm \kappa$ 为右/左旋圆极化波磁导率
- 对于 $\omega \gg \omega_0$ 近似：
  \[
  \theta_f \approx \frac{\omega_m}{2c} \sqrt{\mu_0 \epsilon} l = \frac{\gamma \mu_0 M_s}{2c} \sqrt{\mu_0 \epsilon} l
  \]
- 旋转方向取决于偏置磁场方向，与传播方向无关（非互易性）

### §6.5.3 法拉第旋转隔离器 (Faraday Rotation Isolator)

- 结构：输入极化器 → 45° 法拉第旋转器 → 电阻片 → 输出极化器
- 正向：极化旋转 45° 后通过电阻片
- 反向：极化错误，能量被电阻片吸收
- 隔离度 > 20 dB，插入损耗 < 1 dB
- 非互易特性：
  \[
  [S]_{\text{isolator}} =
  \begin{bmatrix}
  0 & 0 \\
  1 & 0
  \end{bmatrix}
  \]
  正向全通，反向全吸收

### §6.5.4 法拉第旋转环行器 (Faraday Rotation Circulator)

- 三端口环行器
- 信号按 1→2→3→1 顺序循环
- S 参数矩阵（理想 3 端口环行器）：
  \[
  [S] =
  \begin{bmatrix}
  0 & 0 & 1 \\
  1 & 0 & 0 \\
  0 & 1 & 0
  \end{bmatrix}
  \quad\text{或}\quad
  [S] =
  \begin{bmatrix}
  0 & 1 & 0 \\
  0 & 0 & 1 \\
  1 & 0 & 0
  \end{bmatrix}
  \]
- 端口匹配、相邻传输、隔离端口彻底隔离

### §6.5.5 结环行器 (Junction Circulator)

- 三端口 Y 形结环行器，含铁氧体圆柱
- 基于铁氧体结中谐振模式的非互易耦合
- 工作条件（Bosma 理论）：
  \[
  \frac{\kappa}{\mu} = \sqrt{3} \quad\text{(最佳环行条件)}
  \]
- 归一化铁氧体半径 $kR$ 满足：
  \[
  J_1(kR) = 0 \quad\text{或}\quad kR \approx 1.84
  \]
  对于 TE$_{01\delta}$ 谐振模式，其中 $k = \omega\sqrt{\mu_0 \epsilon_0 \epsilon_f \mu_{\text{eff}}}$
- S 参数（理想）：
  \[
  [S] =
  \begin{bmatrix}
  0 & S_{12} & 0 \\
  0 & 0 & S_{23} \\
  S_{31} & 0 & 0
  \end{bmatrix}
  \]
  其中 $|S_{12}| = |S_{23}| = |S_{31}| = 1$
- 典型性能：隔离 > 20 dB，插损 < 0.5 dB，带宽 10–40%
- 可微型化用于平面电路（微带结环行器）

### §6.5.6 YIG 调谐振荡器 (YIG Tuned Oscillator)

- YIG（Yttrium Iron Garnet，钇铁石榴石）小球
- 谐振频率与偏置磁场成正比：
  \[
  f_0 = \frac{\gamma}{2\pi} \mu_0 H_0 = 2.8 \mu_0 H_0
  \]
  其中 $\mu_0 H_0$ 单位为高斯 (G)，$f_0$ 单位为 MHz
  更准确：$f_0 \text{ (MHz)} = 2.8 \times H_0 \text{ (Oe)}$
- 典型调谐范围：2–18 GHz，甚至更宽（多倍频程）
- YIG 小球直径 0.3–1.0 mm
- 3-dB 线宽 $\Delta H$ 决定 Q 值：
  \[
  Q_u = \frac{f_0}{\gamma \Delta H/(2\pi)} \approx \frac{f_0}{2.8 \Delta H}
  \]
- 无载 Q 值可达 $10^3$–$10^4$
- 调谐线性度优于 0.1%
- 应用：频谱分析仪、扫频源、宽带接收机本振

---

## §6.6 微波滤波器简介 (Introduction to Microwave Filters)

### §6.6.1 滤波器基本概念

- 插入损耗法设计：由低通原型通过频率变换和 K/J 变换器得到带通、高通、带阻
- 低通原型元件值 $g_0, g_1, \dots, g_{n+1}$ 由 Butterworth、Chebyshev 或椭圆函数确定
- **Butterworth（最大平坦）**：
  \[
  |S_{21}(j\Omega)|^2 = \frac{1}{1 + \Omega^{2n}}
  \]
- **Chebyshev（等波纹）**：
  \[
  |S_{21}(j\Omega)|^2 = \frac{1}{1 + \epsilon^2 T_n^2(\Omega)}
  \]
  其中 $T_n(\Omega) = \cos(n\cos^{-1}\Omega)$

### §6.6.2 波导滤波器实现

- λ/4 短路短截线、耦合谐振腔
- **直接耦合腔滤波器**：相邻谐振腔通过膜片/窗孔耦合
- 耦合系数：
  \[
  k_{i,i+1} = \frac{\text{FBW}}{\sqrt{g_i g_{i+1}}}
  \]
  其中 FBW 为相对带宽
- **波导 E 面膜片滤波器**：周期性容性膜片形成慢波结构

### §6.6.3 微带滤波器

- 开路短截线滤波器、发夹线滤波器、交指滤波器
- 平行耦合线带通滤波器：$\lambda_0/4$ 耦合线段
- 设计公式（偶/奇模特性阻抗）：
  \[
  Z_{0e} = Z_0 \left[1 + \frac{J}{Y_0} + \left(\frac{J}{Y_0}\right)^2\right],\quad
  Z_{0o} = Z_0 \left[1 - \frac{J}{Y_0} + \left(\frac{J}{Y_0}\right)^2\right]
  \]
  其中 $J$ 为导纳变换器参数

### §6.6.4 其他滤波器形式

- **波导 E 面插入金属膜片滤波器**：带通，结构简单
- **介质谐振滤波器**：高介电常数材料（如 BaTi$_4$O$_9$，$\epsilon_r \approx 37$）
- **SAW/BAW 滤波器**：声表面波/体声波，用于射频前端

---

## 公式汇总

### Polder 张量（§6.5.1）
\[
\overline{\overline{\mu}} = \mu_0
\begin{bmatrix}
\mu & -j\kappa & 0 \\
j\kappa & \mu & 0 \\
0 & 0 & 1
\end{bmatrix},
\quad
\mu = 1 + \frac{\omega_0 \omega_m}{\omega_0^2 - \omega^2},
\quad
\kappa = \frac{\omega \omega_m}{\omega_0^2 - \omega^2}
\]

### 法拉第旋转角（§6.5.2）
\[
\theta_f = \frac{\omega l}{2c} (\sqrt{\mu_+ \epsilon_r} - \sqrt{\mu_- \epsilon_r})
\]

### YIG 调谐（§6.5.6）
\[
f_0 \text{ (MHz)} = 2.8 \times H_0 \text{ (Oe)}
\]

### Magic-T S 矩阵（§6.2.3）
\[
[S] = \frac{1}{\sqrt{2}}
\begin{bmatrix}
0 & 0 & 1 & 1 \\
0 & 0 & 1 & -1 \\
1 & 1 & 0 & 0 \\
1 & -1 & 0 & 0
\end{bmatrix}
\]

### Bethe 小孔极化率（§6.4.2）
\[
\alpha_e = \frac{2}{3}r^3,\quad \alpha_m = \frac{4}{3}r^3
\]

---

*Generated from Collins, 2nd Ed., Ch.6, pp. 371–490*

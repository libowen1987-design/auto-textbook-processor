# Johnson《Antenna Engineering Handbook》3rd Ed. 学习笔记

> Richard C. Johnson (Ed.), McGraw-Hill, 1993, ISBN 0-07-032381-X

---

## 目录

1. [书籍总览](#1-书籍总览)
2. [Part 1: Fundamentals (Ch1-5)](#2-part-1-fundamentals-ch1-5)
3. [Part 2: Wire Antennas (Ch6-10)](#3-part-2-wire-antennas-ch6-10)
4. [Part 3: Aperture Antennas (Ch11-16)](#4-part-3-aperture-antennas-ch11-16)
5. [Part 4: Arrays (Ch17-22)](#5-part-4-arrays-ch17-22)
6. [Part 5: Special Antennas (Ch23-35)](#6-part-5-special-antennas-ch23-35)
7. [Part 6: Structures & Materials (Ch36-45)](#7-part-6-structures--materials-ch36-45)
8. [Part 7: Design Data (Ch46-53)](#8-part-7-design-data-ch46-53)
9. [工程设计数据速查表](#9-工程设计数据速查表)
10. [交叉引用索引](#10-交叉引用索引)

---

## 1. 书籍总览

### 1.1 与 Balanis 教材定位差异

| 维度 | Johnson (工程手册) | Balanis (教材) |
|------|-------------------|----------------|
| **定位** | 工程参考手册，分章节专家撰稿 | 研究生/高年级教材 |
| **理论深度** | 偏工程公式和设计曲线 | 推导更完整，数学更系统 |
| **覆盖范围** | 50+ 章，涵盖工程各专业方向 | 17章，核心理论+主流天线 |
| **实践导向** | 大量实测数据、材料数据、结构指南 | 理论分析为主、仿真为辅 |
| **适用场景** | 设计师桌面参考 | 课堂学习和理论基础 |

### 1.2 核心特点
- **多作者协作**：每章由对应领域专家独立撰写
- **设计导向**：提供大量图表、设计曲线、经验公式
- **实测数据丰富**：包含大量实测天线方向图和阻抗数据
- **Part 6-7 独有**：天线结构、材料、测试等工程实用内容在其他书中少见

---

## 2. Part 1: Fundamentals (Ch1-5)

### Ch 1: 天线基础 (Antenna Fundamentals)

#### 核心内容
- 天线定义与功能：导行波→自由空间波的转换
- 近场与远场分区：反应近场、辐射近场(Fresnel)、远场(Fraunhofer)
- 远场条件: $R \ge 2D^2/\lambda$

#### 关键参数定义
| 参数 | 符号 | 定义 |
|------|------|------|
| 方向性系数 | $D$ | $4\pi U_{max}/P_{rad}$ |
| 增益 | $G$ | $\eta D$ |
| 辐射效率 | $\eta$ | $P_{rad}/P_{in}$ |
| 有效口径 | $A_e$ | $\frac{\lambda^2}{4\pi}G$ |
| 输入阻抗 | $Z_{in}$ | $R_{in}+jX_{in}$ |
| 波束宽度 | $\Theta_{HP}$ | 半功率点间角度 |
| 前后比 | F/B | 主瓣最大值/后瓣最大值 |

#### 与 Balanis 对应
- **Balanis Ch1** — 天线基础（Johnson 更简洁，直接给设计公式）

#### 天线基本方程
Friis 传输方程：
$$P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2$$

### Ch 2: 方向图与方向性 (Radiation Patterns & Directivity)

#### 核心内容
- 方向图类型：功率方向图、场方向图、增益方向图
- 主瓣、副瓣、后瓣、零点
- 方向性计算公式汇总

#### 各种天线方向性近似公式
| 天线类型 | 方向性近似公式 |
|---------|--------------|
| 短偶极子 ($l \ll \lambda$) | $D=1.5$ (1.76 dB) |
| 半波偶极子 | $D=1.64$ (2.15 dB) |
| 均匀线源 | $D = \frac{2L}{\lambda}$ (长阵) |
| 均匀面源 | $D = \frac{4\pi A}{\lambda^2}$ |
| 余弦分布口径 | $D = \frac{4\pi A}{\lambda^2} \cdot 0.81$ |
| 圆锥喇叭 | $D_{H} \approx 0.8 \frac{4\pi A}{\lambda^2}$ |

#### Kraus 公式（经验）
$$D \approx \frac{4\pi}{\Theta_1 \Theta_2}$$
其中 $\Theta_1, \Theta_2$ 为两个主平面半功率波束宽度（弧度）

#### 与 Balanis 对应
- **Balanis Ch2** — 方向图参数、方向性定义
- **Balanis Ch3** — 方向性计算方法（Johnson 更侧重工程近似）

### Ch 3: 阻抗与带宽 (Impedance & Bandwidth)

#### 核心内容
- 天线阻抗的频率特性
- 带宽定义：阻抗带宽、方向图带宽、极化带宽
- 品质因数 $Q$ 与带宽关系
- Chu-Harrington 极限（电小天线理论极限）

#### 基本关系
$$Q = \frac{2\omega W_e}{P_{rad}} \quad \text{(存储能量/辐射功率)}$$

电小天线最小 $Q$:
$$Q_{min} \approx \frac{1}{(ka)^3} + \frac{1}{ka}$$
其中 $a$ 为包围天线的最小球半径，$k=2\pi/\lambda$

工程带宽：$\text{BW} \approx \frac{1}{Q}$（小 $Q$ 时）

#### 与 Balanis 对应
- **Balanis Ch14** — 阻抗匹配理论
- **Balanis §4.6** — 偶极子阻抗
- Johnson 有更完整的工程阻抗数据

### Ch 4: 极化 (Polarization)

#### 核心内容
- 极化椭圆参数：轴比(AR)、倾角、旋向
- 线极化、圆极化、椭圆极化的数学描述
- 极化失配因子(PLF)：$\text{PLF} = |\hat{\rho}_w \cdot \hat{\rho}_a|^2$

#### 关键定义
$$AR = \frac{E_{max}}{E_{min}} = \frac{1+\epsilon}{1-\epsilon} \quad (\text{线性坐标下})$$

圆极化品质：
- 轴比≤3 dB 算良好圆极化
- 完美圆极化 AR=0 dB，$\epsilon=0$（无交叉极化分量）

#### 极化效率（任意两极化波之间）
$$\eta_p = \frac{(1+\epsilon_1^2)(1+\epsilon_2^2) + 4\epsilon_1\epsilon_2\cos 2\Delta\phi + (1-\epsilon_1^2)(1-\epsilon_2^2)\cos 2\Delta\tau}{2(1+\epsilon_1^2)(1+\epsilon_2^2)}$$

#### 与 Balanis 对应
- **Balanis §2.7** — 极化基础
- **Balanis §4.1.2** — 偶极子极化
- Johnson 有更多工程极化测试方法

### Ch 5: 天线测量 (Antenna Measurement)

#### 核心内容
- 室内测量（微波暗室、紧缩场）
- 室外测量（远场测试场）
- 近场扫描测量
- 阻抗测量（网络分析仪、史密斯圆图）

#### 测量方法对比
| 方法 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| 远场法 | 直接、直观 | 需要大场地 | 大型天线验证 |
| 紧缩场 | 室内完成、全天候 | 反射面边缘绕射 | 研发测试 |
| 近场扫描 | 高精度、全天候 | 计算量大 | 卫星天线、相控阵 |
| 球面近场 | 全方向图 | 复杂 | 完整3D方向图 |

#### 关键测量参数
- 增益测量：比较法（3dB法）、绝对法（双天线法）
- 方向图测量：转台+探头
- 极化测量：线极化/圆极化探头法
- 相位测量：干涉法、矢量网络分析仪

#### 与 Balanis 对应
- **Balanis Ch17** — 测量方法（Johnson 有更多工程细节）
- Johnson 包含更多实际测量设备和程序指导

---

## 3. Part 2: Wire Antennas (Ch6-10)

### Ch 6: 偶极子天线 (Dipole Antennas)

#### 核心理论和公式

**半波偶极子 ($l=\lambda/2$)**
- 输入阻抗：$Z_{in} \approx 73 + j42.5\ \Omega$
- 谐振时（缩短约5%）：$Z_{in} \approx 73\ \Omega$
- 方向性：$D = 1.64$ (2.15 dB)
- 辐射电阻：$R_r \approx 73\ \Omega$
- 半功率波束宽度：$\Theta_{HP} \approx 78^\circ$

**短偶极子 ($l \ll \lambda$)**
- 辐射电阻：$R_r = 20\pi^2 (l/\lambda)^2$
- 方向性：$D = 1.5$ (1.76 dB)
- 输入电抗：$X_{in} \approx -\frac{120}{\pi l/\lambda} [\ln(l/a)-1]$

**折合偶极子**
- 阻抗：$Z_{folded} \approx 4 \times Z_{dipole} \approx 292\ \Omega$
- 带宽比普通偶极子宽

**套筒偶极子 (Sleeve Dipole)**
- 用于宽带应用
- 阻抗变化平缓

#### 工程设计要点
- 谐振长度约为 $0.95 \times \lambda/2$（含末端效应）
- 铜管直径增大→带宽增加→谐振长度缩短
- 巴伦(Balun)设计关键参数

#### 与 Balanis 对应
- **Balanis §4.2** — 偶极子基础分析
- **Balanis §4.3** — 半波偶极子
- **Balanis §4.4** — 折合偶极子
- Johnson：实测数据更丰富，含各种变体设计

### Ch 7: 环形天线 (Loop Antennas)

#### 核心理论和公式

**电小环 ($C \ll \lambda$)**
- 辐射电阻：$R_r = 20\pi^2 \left(\frac{C}{\lambda}\right)^4$ (单匝圆形)
- 辐射电阻：$R_r = 320\pi^4 \left(\frac{A}{\lambda^2}\right)^2$ (一般形式)
- 方向图：$\sin\theta$（与短偶极子互补）
- 方向性：$D = 1.5$ (1.76 dB)

**大环 ($C \approx \lambda$)**
- 最大辐射在环面方向（区别于电小环的法线方向）
- 谐振环：$C = \lambda$ 时 $R_r$ 大
- 方向图随电尺寸变化显著

**多匝环**
- 辐射电阻增加 $N^2$ 倍
- 感应磁场接收器（铁氧体环）

#### 工程应用
- AM/FM 接收
- RFID 天线
- 定向探针
- 近场通信

#### 与 Balanis 对应
- **Balanis §5.2** — 电小环
- **Balanis §5.3** — 大环
- Johnson 更多接收环设计数据

### Ch 8: 螺旋天线 (Helical Antennas)

#### 核心理论和公式

**轴向模螺旋 (Axial Mode)**
- 工作条件：$C_\lambda \approx 1$（周长约一个波长）
- 圆极化辐射（沿轴向）
- 方向性近似（经验）：$D \approx 15 \cdot N \cdot \frac{C_\lambda^2 \cdot S_\lambda}{\lambda}$
- 半功率波束宽度：$\Theta_{HP} \approx \frac{52^\circ}{C_\lambda \sqrt{N S_\lambda}}$
- 轴比：$AR \approx \frac{2N+1}{2N}$

**法向模螺旋 (Normal Mode)**
- 线极化（或椭圆极化）
- 电长度短时类似于电短偶极子
- 多用于手持设备

#### 关键设计参数
| 参数 | 符号 | 典型值 |
|------|------|--------|
| 螺旋周长 | $C$ | $0.75\lambda \sim 1.33\lambda$ |
| 螺距角 | $\alpha$ | $12^\circ \sim 15^\circ$ |
| 匝数 | $N$ | 5 $\sim$ 15 |
| 间距 | $S$ | $0.2\lambda \sim 0.3\lambda$ |
| 增益 | $G$ | 10 $\sim$ 18 dBi |
| 带宽 | BW | 约 1.7:1 (VSWR<2) |

#### 与 Balanis 对应
- **Balanis §5.4** — 螺旋天线
- Johnson 提供更详细的设计曲线和实际案例

### Ch 9: 行波天线 / 表面波天线 (Traveling-Wave & Surface-Wave Antennas)

#### 行波天线 (Traveling-Wave Antennas)

**菱形天线 (Rhombic Antenna)**
- 行波结构，终端接匹配负载
- 宽带（可达 3:1 或更宽）
- 增益取决于臂长：$G \propto (L/\lambda)^2$

**贝弗里奇天线 (Beverage Antenna)**
- 长线行波天线
- 用于低频接收（LF/MF/HF）
- 方向性与长度成正比

#### 漏波天线 (Leaky-Wave Antennas)
- 波导/传输线开槽
- 波束扫描随频率变化（频率扫描）
- $k_z = \beta - j\alpha$ （传播常数，$\alpha$ 为泄露率）

#### 表面波天线
- 介质波导上周期性结构
- 丫基-乌达天线（Yagi-Uda）作为行波阵

#### 与 Balanis 对应
- **Balanis §10.2-10.5** — 行波天线
- **Balanis §10.6** — 漏波天线
- Johnson 包含更多实用设计图表

### Ch 10: 对数周期天线 (Log-Periodic Antennas)

#### 核心理论和公式

**对数周期偶极子阵 (LPDA)**
- 比例因子：$\tau = \frac{R_{n+1}}{R_n} = \frac{l_{n+1}}{l_n} < 1$
- 间距因子：$\sigma = \frac{d_n}{2l_n}$
- 工作带宽：$B_s = B \cdot \frac{1}{1-\tau} \cdot \frac{1}{\tan\alpha}$

**设计经验公式**
- 增益主要取决于 $\tau$ 和 $\sigma$ 的组合
- 典型 $\tau$: 0.8～0.95
- 典型 $\sigma$: 0.03～0.2
- 顶点半角：$\alpha = \arctan\left(\frac{1-\tau}{4\sigma}\right)$

**Carrel 设计法（经典）**
1. 选定增益 → 查表得 $\tau$ 和 $\sigma$
2. 计算顶点角 $\alpha$
3. 确定最大/最小单元长度
4. 逐单元计算位置和长度
5. 计算有源区单元数

#### 性能特点
| 特性 | 范围 |
|------|------|
| 频带比 | $2:1 \sim 10:1$ (或更宽) |
| 增益 | 6 $\sim$ 12 dBi |
| F/B 比 | 10 $\sim$ 25 dB |
| VSWR | 1.5 $\sim$ 2.0 |
| 阻抗 | 平衡约 200 $\sim$ 300 $\Omega$ |

#### 与 Balanis 对应
- **Balanis §11.2** — LPDA 分析和设计
- **Balanis §11.4** — 对数周期结构一般理论
- Johnson 的 Carrel 设计法更详细，包含设计表

---

## 4. Part 3: Aperture Antennas (Ch11-16)

### Ch 11: 喇叭天线 (Horn Antennas)

#### 核心理论和公式

**E面扇形喇叭**
- 口径场：TE₁₀模在E面呈余弦分布（近似均匀）
- 方向性：$D_E = \frac{64a}{\pi\lambda} \cdot \frac{A}{\lambda} \cdot F_E(t)$
- 最优喇叭：$L_h = h^2/3\lambda$（h为口径高度）

**H面扇形喇叭**
- 口径场：余弦锥削分布（H面）
- 最优喇叭：$L_h = A^2/3\lambda$（A为口径宽度）

**角锥喇叭 (Pyramidal Horn)**
- 综合 E 面和 H 面最优条件
- 方向性：$D = \frac{4\pi A B}{\lambda^2} \cdot \eta_{ap}$
- 口径效率：$\eta_{ap} \approx 0.51$（最优锥削喇叭）

**圆锥喇叭 (Conical Horn)**
- 常用于圆波导馈电
- 介质加载喇叭（介质锥加载）

#### 最优喇叭设计公式
| 喇叭类型 | 最优条件 | 口径效率 |
|---------|---------|---------|
| E面扇形 | $L_E = 2A^2/\lambda$ (近似) | ~0.64 |
| H面扇形 | $L_H = 3B^2/\lambda$ (近似) | ~0.64 |
| 角锥 | 同时满足E和H | ~0.51 |
| 圆锥(最优) | 基本同角锥 | ~0.5-0.52 |

#### 工程曲线
- 方向性 vs. 口径尺寸图（设计用）
- VSWR vs. 频率曲线
- 相位中心位置（重要用于反射面馈源）

#### 与 Balanis 对应
- **Balanis §13.2-13.5** — 喇叭天线
- Johnson 包含更多实际设计图和相位中心数据

### Ch 12: 反射面天线 (Reflector Antennas)

#### 核心理论和公式

**抛物面反射器**
- 几何关系：$r = \frac{2F}{1+\cos\theta}$
- 表面方程：$z = \frac{x^2+y^2}{4F}$
- 焦距直径比：$F/D = 0.3 \sim 1.0$

**方向性（理想抛物面）**
$$D = \left(\frac{\pi D}{\lambda}\right)^2 \cdot \eta_{ap}$$

典型口径效率 $\eta_{ap}$ 范围：
- 主馈抛物面：0.55～0.65
- 卡塞格伦：0.6～0.7
- 偏馈抛物面：0.65～0.8

**初级馈源要求**
- 锥削（edge taper）：约 -10 ～ -12 dB（减小副瓣）
- 相位中心稳定
- 低驻波
- 最小遮挡

**卡塞格伦天线**
- 双反射面：主抛物面 + 双曲面副反射面
- 等效焦距加长 → 馈电方便
- 放大倍数：$M = \frac{F_e}{F} = \frac{\tan(\theta_b/2)}{\tan(\theta_s/2)}$

**其他类型**
- 球面反射器（Arecibo型）
- 偏馈反射面（消除遮挡）
- 赋形反射面（优化效率/副瓣）

#### 工程设计要点
- 表面公差：$\sigma \leq \lambda/50$（Ruzé公式）
- 效率损失 = 4πσ/λ 的随机误差
- 副瓣控制：-25 dB 需要 0.3° rms 表面精度（C波段）

#### 与 Balanis 对应
- **Balanis §15.2-15.7** — 反射面天线
- **Balanis §15.8** — 馈源设计
- Johnson 包含更多反射面制造和测试内容

### Ch 13: 透镜天线 (Lens Antennas)

#### 核心理论和公式

**介质透镜**
- 延迟透镜（Luneburg透镜、半球透镜）
- 折射率取决于结构
- 等效口径效率高

**金属透镜**
- 加速透镜（平行板型含金属片阵列）
- 通过导波路径缩短实现聚焦

**Luneburg 透镜**
- 渐变折射率：$n(r) = \sqrt{2 - (r/R)^2}$
- 从表面馈送可在对面形成平行波束
- 多波束能力（多馈源）

#### 透镜设计参数
| 参数 | 介质透镜 | 金属透镜 |
|------|---------|---------|
| 折射率 | $n>1$ | $n<1$ |
| 重量 | 重（高介电常数材料） | 轻 |
| 带宽 | 宽（非色散材料） | 较窄 |
| 制造 | 模压/机械加工 | 组装 |
| 典型效率 | 0.5-0.7 | 0.4-0.6 |

#### 与 Balanis 对比
- 注意：**Balanis 不直接包含透镜天线章节**
- Johnson 是少见的有透镜天线详细工程的参考书

### Ch 14: 微带天线 (Microstrip Antennas)

#### 核心理论和公式

**矩形贴片**
- 谐振长度近似：$\Delta L = 0.412h \frac{\epsilon_{eff} + 0.3}{\epsilon_{eff} - 0.258} \cdot \frac{W/h + 0.264}{W/h + 0.8}$
- 有效介电常数：$\epsilon_{eff} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2}\left[1 + 12\frac{h}{W}\right]^{-1/2}$
- 谐振频率：$f_r = \frac{c}{2(L + 2\Delta L)\sqrt{\epsilon_{eff}}}$
- 输入阻抗（边缘馈电）：$Z_{in} \approx 90 \frac{\epsilon_r^2}{\epsilon_r - 1} \left(\frac{L}{W}\right)^2$
- 带宽（VSWR<2）：$\text{BW} \approx 3.77 \frac{(\epsilon_r - 1)}{\epsilon_r^2} \frac{h}{\lambda_0} \frac{W}{L}$

**圆形贴片**
- 谐振：$f_r = \frac{1.841c}{2\pi a_e \sqrt{\epsilon_r}}$（TM₁₁模）
- 等效半径含边缘场修正

**馈电方式**
- 探针馈电（同轴）
- 微带线馈电
- 电磁耦合馈电
- 口径耦合馈电（最宽带宽）

#### 性能典型值
| 参数 | 典型范围 |
|------|---------|
| 带宽 (VSWR<2) | 1～5%（标准）；可达 20-30%（宽频技术） |
| 增益 | 4～8 dBi（单个贴片） |
| 方向性 | 5～7 dB |
| 交叉极化 | -15 ～ -25 dB |
| 辐射效率 | 70～95% |

#### 与 Balanis 对应
- **Balanis Ch14** — 微带天线（最详细的章节之一）
- **区别**：Balanis 分析理论更完整（腔模法、全波法）
- Johnson 提供更多实际设计尺寸和馈电结构

### Ch 15: 缝隙天线 (Slot Antennas)

#### 核心理论和公式

**波导缝隙**
- Babinet原理：缝隙与互补偶极子
- 谐振缝隙（$\lambda/2$ 缝隙）：$R_{slot} \approx 363\ \Omega$
- 波导宽壁纵向缝隙：等效并联导纳
- 波导窄壁倾斜缝隙：等效串联阻抗

**缝隙阵**
- 谐振阵（驻波馈电）vs. 非谐振阵（行波馈电）
- 泰勒/切比雪夫加权 → 降低副瓣
- 波束指向：扫描角由缝隙间距和馈电相位决定

#### 设计公式
纵向缝隙归一化导纳：
$$g = g_1 \sin^2\left(\frac{\pi x}{a}\right)$$
其中 $x$ 为缝隙距波导中心线的偏移量，$g_1$ 为最大电导

缝隙导纳与偏移量的关系（Stevenson公式）：
$$G = \frac{2.09a\lambda_g}{b\lambda} \cos^2\left(\frac{\lambda\pi}{2\lambda_g}\right) \sin^2\left(\frac{\pi x}{a}\right)$$

#### 与 Balanis 对应
- **Balanis §4.5** — 缝隙天线基础
- **Balanis §12.5** — 波导缝隙阵
- Johnson 包含更多波导缝隙阵工程设计图表

### Ch 16: 喇叭与反射面阵列馈源 (Horn & Reflector Array Feeds)

#### 核心内容
- 多喇叭馈源（跟踪馈源）
- 单脉冲馈源系统（Σ/Δ 和差网络）
- 波束波导馈电
- 馈源阵列（多波束反射面）

#### 与 Balanis 对应
- **Balanis §15.8** — 馈源部分
- Johnson 更加工程化

---

## 5. Part 4: Arrays (Ch17-22)

### Ch 17: 线阵 (Linear Arrays)

#### 核心理论和公式

**阵因子 (AF)**
$$AF(\psi) = \sum_{n=1}^{N} I_n e^{j(n-1)\psi}$$
其中 $\psi = kd\cos\theta + \beta$，$\beta$ 为相邻单元相移

**均匀线阵 (ULA)**
$$AF = \frac{\sin(N\psi/2)}{\sin(\psi/2)}$$

**关键参数**
| 参数 | 公式 |
|------|------|
| 主瓣位置 | $\psi = 0 \rightarrow \cos\theta_0 = -\beta/kd$ |
| 第一零点间距 | $\Theta_{BWFN} \approx 2\lambda/(Nd)$ |
| 半功率波束宽度 | $\Theta_{HP} \approx 0.886\lambda/(Nd)$ (等幅同相) |
| 方向性(均匀阵) | $D \approx 2Nd/\lambda$ (长阵) |

**副瓣控制**
- **二项式分布**：无副瓣，但波束宽
- **切比雪夫阵**：等副瓣最优（Dolph-Chebyshev）
- **泰勒分布**：近端等副瓣、远端衰减（实用）
- **Bayliss分布**：差方向图低副瓣

**切比雪夫阵设计**
- 给定副瓣电平 $SLL$ (dB) → 计算 $R_0$
- 归一化阵因子：$AF_{norm} = T_{N-1}(R_0\cos\frac{\psi}{2})$
- $T_m$ 为第一类m次切比雪夫多项式
- 电流分布通过反变换得到

#### 与 Balanis 对应
- **Balanis Ch6** — 线阵理论
- **Balanis §7.3** — 切比雪夫阵
- Johnson 包含更多设计表格

### Ch 18: 面阵 (Planar Arrays)

#### 核心理论和公式

**矩形栅格面阵**
$$AF(\theta,\phi) = \sum_m\sum_n I_{mn} e^{j(m\psi_x + n\psi_y)}$$
其中 $\psi_x = kd_x\sin\theta\cos\phi + \beta_x$，$\psi_y = kd_y\sin\theta\sin\phi + \beta_y$

**方向性（均匀矩形阵）**
$$D = \pi D_x D_y \cos\theta_0$$

**方向性（均匀圆阵）**
$$D = \frac{4\pi A}{\lambda^2} \eta_{ap}$$

**锥削效率**
$$\eta_{taper} = \frac{|\sum\sum I_{mn}|^2}{N_{total}\sum\sum |I_{mn}|^2}$$

#### 面阵分类
| 类型 | 特点 | 应用 |
|------|------|------|
| 矩形栅格 | 结构简单 | 通用 |
| 三角栅格 | 更少单元数 | 空间有限 |
| 六边形阵 | 圆形覆盖 | 雷达 |
| 同心圆环阵 | 宽带扫描 | 天线测试 |
| 共形阵 | 贴附曲面 | 飞行器 |

#### 与 Balanis 对应
- **Balanis §6.3** — 面阵
- **Balanis §7.4** — 矩形面阵设计

### Ch 19: 相控阵 (Phased Arrays)

#### 核心理论和公式

**波束扫描**
$$\beta = -kd \sin\theta_0$$
- 电扫描：$\theta_0 = \arcsin(-\beta/kd)$
- 相移量：$\Delta\phi = \frac{2\pi d}{\lambda}\sin\theta_0$

**栅瓣条件**
避免栅瓣：$\frac{d}{\lambda} < \frac{1}{1+|\sin\theta_{max}|}$

| 最大扫描角 | 最大单元间距 |
|-----------|------------|
| $\pm 0^\circ$ | $d < 1.0\lambda$ |
| $\pm 30^\circ$ | $d < 0.67\lambda$ |
| $\pm 45^\circ$ | $d < 0.59\lambda$ |
| $\pm 60^\circ$ | $d < 0.54\lambda$ |

**移相器类型**
| 类型 | 位元 | 损耗 | 切换速度 | 成本 |
|------|------|------|---------|------|
| PIN二极管 | 4-6 | 中等 | ns | 低 |
| 铁氧体 | 6-8 | 低 | μs | 高 |
| MMIC(GaAs) | 4-6 | 中等 | ns | 中 |
| MEMS | 4-6 | 低 | μs | 中 |

**波束宽度随扫描变化**
$$\Theta_{HP}(\theta) = \frac{\Theta_{HP}(0)}{\cos\theta} \quad \text{(主平面扫描)}$$

#### 与 Balanis 对应
- **Balanis §7.5** — 相控阵概念
- **Balanis §7.6** — 扫描性能
- Johnson 详细讨论阵列架构和移相器

### Ch 20: 自适应阵 (Adaptive Arrays)

#### 核心内容
- 自适应波束形成（ABF）
- 数字波束形成（DBF）
- 自适应算法：LMS, RLS, CMA
- 干扰置零（Null Steering）
- 智能天线

#### 自适应性能指标
- SINR (Signal to Interference + Noise Ratio)
- 收敛速度
- 计算复杂度
- 伪相/信源分离（MUSIC, ESPRIT）

#### 与 Balanis 对应
- **Balanis §7.7** — 自适应阵（简要）
- Johnson 更深入覆盖算法和系统实现
- 注意：这部分在1993年仍属较新领域

### Ch 21: 随机阵与统计阵 (Random & Statistical Arrays)

#### 核心内容
- 稀布阵（Thinned Arrays）
- 稀疏阵（Sparse Arrays）
- 随机误差对阵列性能的影响（振幅/相位误差）
- 幅度量化副瓣（Amplitude Quantization Sidelobes）
- 失效阵元的统计处理

#### 误差模型
- 振幅误差：$\sigma_A \rightarrow$ 副瓣恶化
- 相位误差：$\sigma_\phi \rightarrow$ 副瓣恶化
- 单元失效：二进制有/无
- 平均副瓣电平提升：$\overline{SLL} \propto \sigma_A^2 + \sigma_\phi^2$

#### 与 Balanis 对应
- **Balanis §7.8** — 阵列误差分析（简要）
- Johnson 更系统覆盖稀有阵和误差统计

### Ch 22: 阵列馈电网络 (Array Feed Networks)

#### 核心内容
- 波束形成网络（BFN）
  - Butler 矩阵
  - Blass 矩阵
  - Rotman 透镜
  - 功分器/合成器
- 馈电架构：串联馈电、并联馈电、空间馈电
- 幅相控制：衰减器+移相器

#### 常见 BFN 对比
| 类型 | 波束数 | 损耗 | 带宽 | 复杂度 |
|------|--------|------|------|--------|
| Butler 矩阵 | N | 低 | 中等 | 中等 |
| Blass 矩阵 | M×N | 较高 | 宽 | 高 |
| Rotman 透镜 | 任意 | 中 | 宽 | 中 |
| 数字波束形成 | 任意 | 无(RF) | 由ADC决定 | 高 |

#### 与 Balanis 对应
- Balanis 无独立馈电网络章
- Johnson 独有内容，工程实用价值高

---

## 6. Part 5: Special Antennas (Ch23-35)

### Ch 23: 雷达散射截面 (Radar Cross Section / RCS)

#### 核心理论和公式

**RCS 定义**
$$\sigma = \lim_{R\to\infty} 4\pi R^2 \frac{|\mathbf{E}_{scat}|^2}{|\mathbf{E}_{inc}|^2}$$

**天线的 RCS**
- 结构模式（结构本身散射）
- 天线模式（负载匹配状态相关）
- 天线模式 RCS：$\sigma_{ant} = \frac{\lambda^2 G^2}{4\pi} |\Gamma|^2$
  - $\Gamma$ 为馈电反射系数
  - 匹配时 ($\Gamma=0$)：天线模式 RCS 为零（只剩结构RCS）
  - 开路时 ($\Gamma=1$)：最大天线模式 RCS

**RCS 减缩技术**
- 雷达吸波材料 (RAM)
- 外形隐身（Salisbury屏、Dallenbach层）
- 阻抗加载

#### 与 Balanis 对应
- **Balanis Ch16** — RCS 基础
- Johnson 从天线工程角度出发，更偏实际操作

### Ch 24: 地面通信天线 (Earth Station Antennas)

#### 核心内容
- 大孔径地面站天线
- 卫星通信频段：C(4/6)、Ku(12/14)、Ka(20/30)
- 天线性能指标：G/T(dBi/K)、EIRP
- 干扰协调与旁瓣包络要求

#### 与 Balanis 对应
- 卫星通信应用相关（Bal 部分涉及）

### Ch 25: 航天器天线 (Spacecraft Antennas)

#### 核心内容
- 卫星天线类型和设计约束
- 发射时的折叠/展开机构
- 热真空环境
- 低增益/中增益/高增益天线
- 反射面天线在卫星上的应用

#### 与 Balanis 对应
- 应用相关章节，Balanis 中没有单独展开

### Ch 26: 手机与移动通信天线 (Land-Mobile Antennas)

#### 核心内容
- 手机的倒F/单极/螺旋天线
- 车载天线：车顶安装、玻璃嵌入
- 分集天线
- 比吸收率(SAR)

#### 技术要点
- 手机天线的重要设计约束：小型化、多频、低SAR
- 典型结构：PIFA (Planar Inverted-F Antenna)
- 车载天线常用：四分之一波长单极、螺旋

#### 与 Balanis 对应
- 注意：**Balanis 教材出版早于手机普及期（第一版1982）**
- Johnson 1993 版已有初步手机天线内容

### Ch 27: 通信与广播发射天线 (Communication & Broadcast Transmitting Antennas)

#### 核心内容
- AM 广播（中波）：塔式天线
- FM 广播（VHF）：蝙蝠翼天线
- TV 广播：多频道组合天线
- 短波通信：对数周期/菱形天线

#### 与 Balanis 对应
- 实践导向，Balanis 不单独成章

### Ch 28: 雷达天线 (Radar Antennas)

#### 核心内容
- 搜索雷达天线（扇形波束）
- 跟踪雷达天线（笔形波束）
- 合成孔径雷达(SAR)
- 单脉冲天线（和/差波束）
- 相控阵雷达

**雷达方程（天线参数部分）**
$$R_{max} = \left[ \frac{P_t G_t A_{er} \sigma}{(4\pi)^2 S_{min}} \right]^{1/4}$$

**单脉冲跟踪**
- 和通道：$\Sigma = A + B + C + D$
- 方位差：$\Delta_{az} = (A + B) - (C + D)$
- 俯仰差：$\Delta_{el} = (A + C) - (B + D)$

#### 与 Balanis 对应
- 雷达相关应用，Balanis §1.8 有简要介绍

### Ch 29: 电子战与对抗天线 (Electromagnetic Warfare Antennas)

#### 核心内容
- 电子支援(ES)用宽带天线
- 电子攻击(EA)用高功率天线
- 电子防护(EP)相关
- 电子情报(ELINT)天线

#### 与 Balanis 对应
- 独特内容，大多书中不完整覆盖

### Ch 30: 探地雷达与穿墙雷达 (GPR & Through-Wall)

#### 核心内容
- 探地雷达(GPR)天线：Vivaldi、蝶形偶极子
- 穿墙雷达天线
- 超宽带脉冲辐射

#### 与 Balanis 对应
- Johnson 独有，Balanis 基本不涉及

### Ch 31: 超宽带天线 (Ultra-Wideband Antennas)

#### 核心内容
- 分类与定义（相对带宽>25% 或 绝对带宽>500MHz）
- TEM 喇叭
- Vivaldi 天线 / 指数渐变缝隙天线 (TSA)
- 蝶形偶极子 (Bow-tie)
- 自互补结构

**Vivaldi 设计**
- 指数渐变曲线：$y = C_1 e^{Rx} + C_2$
- 线极化的端射天线
- 带宽可达 10:1
- 增益中等（5-10 dBi）

**TEM 喇叭**
- 平衡传输线渐变到喇叭口
- 宽带阻抗匹配
- 时域脉冲保形

#### 与 Balanis 对应
- 注意：**Balanis 教材中 UWB 不是重点**
- Johnson 1993 版包含早期 UWB 内容

### Ch 32-35: 其他特殊天线

#### Ch 32: 等离子体天线
- 等离子体柱取代金属导体
- 可开关 / 可重构
- 低可观测性

#### Ch 33: 馈源喇叭的设计与应用
- 波纹喇叭（Corrugated Horn）
- 介质加载喇叭
- 双模喇叭（Potter 喇叭）

**波纹喇叭设计要点**
- 波纹深度 ≈ $\lambda/4$
- 提供对称的 E/H 面方向图
- 低交叉极化（< -30 dB）
- 广泛用于反射面馈源

#### Ch 34: 毫米波与亚毫米波天线
- 石英/硅透镜天线
- 波导型馈源
- 集成天线
- 片上天线

#### Ch 35: 小天线（电小天线）
- $ka < 0.5$ 的天线
- 阻抗特性：高 Q，窄带宽
- Chu-Harrington 极限的工程应用
- 匹配网络设计：L型网络、T型网络

---

## 7. Part 6: Structures & Materials (Ch36-45)

### Ch 36-37: 天线罩 (Radomes)

#### 核心内容
- 半波长透波壁：$t = \lambda_0/(2\sqrt{\epsilon_r})$
- A型夹层：内外皮+泡沫芯
- B型夹层：多层复合
- 材料：玻璃纤维、石英纤维、PTFE

**传递效率**
- 单层：
$$T = \frac{1}{1+R^2-2R\cos(2\beta t)}$$

#### 与 Balanis 对应
- Balanis 无天线罩章节
- Johnson 独有工程内容

### Ch 38: 塔架与支撑结构 (Towers & Supports)

#### 内容
- 格构塔架设计
- 拉线塔
- 抗风设计
- 基础设计

### Ch 39: 天线安装 (Antenna Installation)

#### 内容
- 地网系统
- 接地与防雷
- 结构对准
- 环境防护

### Ch 40-45: 材料与结构工程

| 章节 | 内容 |
|------|------|
| Ch 40-41 | 金属材料：铝/铜合金特性，耐腐蚀处理 |
| Ch 42-43 | 介质材料：介电常数/损耗角正切，高功率应用 |
| Ch 44 | 焊接、钎焊与连接技术 |
| Ch 45 | 天线结构公差与力学性能 |

#### 与 Balanis 对应
- **全书无对应** — Johnson 独有工程内容

---

## 8. Part 7: Design Data (Ch46-53)

### Ch 46: 波导数据 (Waveguide Data)

#### 标准波导数据

| 波导标号 | 频率范围 (GHz) | 内尺寸 (mm) | 截止频率 (GHz) |
|---------|---------------|------------|---------------|
| WR-90 (X) | 8.2-12.4 | 22.86 × 10.16 | 6.56 |
| WR-62 (Ku) | 12.4-18.0 | 15.8 × 7.9 | 9.49 |
| WR-42 (K) | 18.0-26.5 | 10.67 × 4.32 | 14.05 |
| WR-28 (Ka) | 26.5-40.0 | 7.11 × 3.56 | 21.08 |
| WR-15 (V) | 50-75 | 3.76 × 1.88 | 39.9 |
| WR-10 (W) | 75-110 | 2.54 × 1.27 | 59.0 |

**关键参数关系**
- 波导波长：$\lambda_g = \frac{\lambda}{\sqrt{1-(\lambda/\lambda_c)^2}}$
- 截止频率：$f_c = \frac{c}{2a}$ (矩形, TE₁₀)
- 特征阻抗：$Z_0 \approx \frac{b}{a} \cdot \frac{\eta}{\sqrt{1-(f_c/f)^2}}$

#### 与 Balanis 对应
- **Balanis §3.3-3.4** — 波导基础
- Johnson 提供完整截面尺寸表

### Ch 47: 传输线与馈电 (Transmission Lines & Feed Systems)

#### 常用传输线对比

| 类型 | 特性阻抗 $Z_0$ | 损耗 | 功率容量 | 带宽 |
|------|--------------|------|---------|------|
| 同轴电缆 | 50/75 $\Omega$ | 中等 | 中等 | 宽 |
| 波导 | 取决于尺寸 | 低 | 高 | 窄 |
| 微带线 | 20-120 $\Omega$ | 较高 | 低 | 中等 |
| 共面波导(CPW) | 50-100 $\Omega$ | 中等 | 低 | 宽 |
| 带状线 | 50-100 $\Omega$ | 中等 | 中等 | 中等 |

#### 馈电网络设计要点
- 阻抗变换：四分之一波长变换器、多节变压器
- 功分器：威尔金森、T型结、混合环
- 巴伦：Marchand巴伦、套筒巴伦、微带-缝隙过渡

#### 与 Balanis 对应
- **Balanis §1.5, §8.2** — 传输线和馈电
- Johnson 包含完整设计表格

### Ch 48: 阻抗匹配网络 (Impedance Matching Networks)

#### 常见匹配网络

**L型网络**
- 设计公式（源阻抗 $R_s$，负载 $R_L$）：
  - 若 $R_L > R_s$：串联L, 并联C
  - 若 $R_L < R_s$：并联L, 串联C
- Q值：$Q = \sqrt{R_{high}/R_{low} - 1}$

**T型与$\pi$型网络**
- 更高自由度
- 可挑选 Q 值
- 适用于宽带匹配

**四分之一波长变换器**
$$Z_1 = \sqrt{Z_{in}Z_L}$$
多节变换器提供更大带宽

#### 与 Balanis 对应
- **Balanis §1.5, §4.6** — 匹配网络
- Johnson 提供更多网络设计和元件值表格

### Ch 49: 史密斯圆图 (Smith Chart)

#### 核心用法
- 归一化阻抗/导纳
- 阻抗→导纳转换（绕图旋转180°）
- VSWR 圆
- 传输线长度变换
- 单/双/三 stub 匹配

#### 与 Balanis 对应
- **Balanis §1.5** — 史密斯圆图
- Johnson 在多个章节使用 Smith Chart

### Ch 50: 天线开关与旋转关节 (Switches & Rotary Joints)

#### 内容
- 同轴旋转关节
- 波导旋转关节
- RF 开关（机械/固态）
- 多路复用器

### Ch 51: 平衡-不平衡转换器 (Baluns)

#### 常见 Balun 类型
| 类型 | 频率范围 | 带宽 | 功率容量 |
|------|---------|------|---------|
| 对称套筒 | HF/VHF | 窄 | 高 |
| 同轴倍线 | VHF/UHF | 宽 | 中等 |
| 传输线变压器 | HF/UHF | 非常宽 | 中等 |
| Marchand | UHF/微波 | 宽 | 低 |
| 微带 | 微波 | 中等 | 低 |

#### 与 Balanis 对应
- Balanis 无独立 Balun 章
- Johnson 提供设计方法和数据

### Ch 52: 天线测试设施 (Antenna Test Facilities)

#### 内容
- 微波暗室设计（吸波材料选择、静区定义）
- 紧缩场（Compact Range）：反射面+馈源，形成准平面波
- 近场探头补偿
- 测试误差源分析

#### 测试参数与方法
| 参数 | 测试方法 |
|------|---------|
| 增益 | 比较法、三天线法 |
| 方向图 | 转台法 |
| 极化 | 旋转线极化法、圆极化法 |
| 相位 | 参考信号比较 |
| 阻抗 | 网络分析仪 |

#### 与 Balanis 对应
- **Balanis Ch17** — 测量基础
- Johnson 更详细覆盖设备和误差分析

### Ch 53: 展望与其他 (Miscellaneous / Emerging Topics)

#### 内容
- 超导天线
- 光控天线（Photonic antennas）
- 分形天线
- 可重构天线
- 计算电磁学在天线设计中的应用
- 神经网络在天线优化中的应用

---

## 9. 工程设计数据速查表

### 9.1 常见天线类型性能对比

| 天线类型 | 增益 (dBi) | 带宽 | 极化 | 复杂度 | 典型应用 |
|---------|-----------|------|------|-------|---------|
| 半波偶极子 | 2.15 | 5-10% | 线 | 低 | 通用、阵列单元 |
| 折合偶极子 | 2.15 | 10-15% | 线 | 低 | FM广播、TV |
| 四分之一波单极 | ~2-3 | 5-10% | 线(垂直) | 很低 | 车载、手机 |
| 螺旋(轴向) | 10-18 | 1.7:1 | 圆 | 中 | 卫星通信、跟踪 |
| 螺旋(法向) | <2 | 5-10% | 线 | 低 | 手持设备 |
| 对数周期(LPDA) | 6-12 | >3:1 | 线 | 中 | EMC测试、宽带 |
| Yagi-Uda | 6-17 | 2-5% | 线 | 中 | TV接收 |
| 角锥喇叭 | 10-25 | 10-20% | 线 | 低 | 测量、馈源 |
| 波纹喇叭 | 15-25 | 5-15% | 线(低交叉) | 高 | 卫星馈源 |
| 抛物面 | 20-50+ | 5-15% | 取决于馈源 | 高 | 卫星地面、雷达 |
| 微带贴片 | 4-8 | 2-5% | 线/圆 | 低 | 阵列、手机 |
| Vivaldi | 5-10 | >3:1 | 线 | 中 | UWB、相控阵 |
| 缝隙(波导) | 3-7 | 3-5% | 线 | 高 | 雷达、导航 |
| 相控阵(面) | 20-50+ | 受单元限制 | 可变 | 很高 | 雷达 |

### 9.2 常用频段与天线形式

| 频段 | 频率范围 | 典型天线 |
|------|---------|---------|
| LF | 30-300 kHz | 塔式、地网、环 |
| MF | 300-3000 kHz | 铁塔、单极 |
| HF | 3-30 MHz | 偶极子、菱形、LPDA |
| VHF | 30-300 MHz | Yagi、偶极子、蝙蝠翼 |
| UHF | 300-3000 MHz | Yagi、LPDA、微带、贴片 |
| L | 1-2 GHz | 微带、螺旋、喇叭 |
| S | 2-4 GHz | 喇叭、抛物面、阵列 |
| C | 4-8 GHz | 抛物面、喇叭、微带阵 |
| X | 8-12 GHz | 抛物面、喇叭、缝隙阵 |
| Ku | 12-18 GHz | 抛物面、喇叭、阵列 |
| K | 18-27 GHz | 喇叭、透镜、反射面 |
| Ka | 27-40 GHz | 喇叭、透镜、微带 |
| mmW | 40-300 GHz | 透镜、喇叭、片上天线 |

### 9.3 材料与介电常数速查

| 材料 | $\epsilon_r$ | $\tan\delta$ | 典型用途 |
|------|-----------|------------|---------|
| 空气 | 1.0 | 0 | 自然介质 |
| 聚四氟乙烯(PTFE) | 2.1 | 0.0002 | 微波基板 |
| 聚乙烯(PE) | 2.25 | 0.0003 | 同轴线绝缘 |
| Rogers 5880 | 2.2 | 0.0009 | 高频率微带 |
| Rogers 4003C | 3.38 | 0.0021 | 微波板 |
| FR-4 | 4.4 | 0.02-0.03 | 低频(不推荐高频) |
| 氧化铝(Al₂O₃) | 9.8 | 0.0002 | 厚膜电路 |
| 石英 | 3.78 | 0.0001 | 毫米波 |
| 硅 | 11.9 | 0.005 | 集成电路 |

### 9.4 巴伦设计速查

| 类型 | 变换比 | 频率范围 | 阻抗变换 |
|------|--------|---------|---------|
| 套筒巴伦 | 1:1 | 窄带 | 平衡→不平衡 |
| 折合四分之一波 | 4:1 | 窄带 | 300→75 |
| 传输线变压器 | 1:1或4:1 | 宽带 | 可变 |
| Marchand | 1:1 | 宽带 | 平衡→不平衡 |
| 倍线 | 1:1 | 宽带 | 平衡→不平衡 |

### 9.5 经验缩略与规则

| 规则 | 内容 |
|------|------|
| 谐振偶极子长度 | $l \approx 0.95(\lambda/2)$ |
| 地平面尺寸 | $\ge \lambda/2$ (典型$\lambda$) |
| 贴片天线厚度 | $0.003\lambda_0 \le h \le 0.05\lambda_0$ |
| 反射面公差 | $\text{rms} \le \lambda/50$ |
| 喇叭最优长度 | $L_{opt} \approx A^2/3\lambda$ |
| 阵列栅瓣条件 | $d/\lambda < 1/(1+\sin\theta_{max})$ |
| 主瓣-副瓣关系 | $-SLL(dB) \approx 13 + 20\log(\text{taper factor})$ |

---

## 10. 交叉引用索引

### Johnson vs. Balanis 章节对应表

| Johnson 章节 | 内容 | Balanis 对应章节 | Balanis 覆盖程度 |
|-------------|------|-----------------|----------------|
| **Part 1: Fundamentals** |
| Ch 1 | 天线基础 | Ch 1 | 全面 |
| Ch 2 | 方向图/方向性 | Ch 2, Ch 3 | 全面 |
| Ch 3 | 阻抗/带宽 | §4.6, Ch 14 | 理论为主 |
| Ch 4 | 极化 | §2.7 | 全面 |
| Ch 5 | 天线测量 | Ch 17 | 全面 |
| **Part 2: Wire Antennas** |
| Ch 6 | 偶极子 | §4.1-4.4 | 全面 |
| Ch 7 | 环形 | Ch 5 | 全面 |
| Ch 8 | 螺旋 | §5.4 | 全面 |
| Ch 9 | 行波/表面波 | Ch 10 | 全面 |
| Ch 10 | 对数周期 | §11.2 | 全面 |
| **Part 3: Aperture Antennas** |
| Ch 11 | 喇叭 | §13.2-13.5 | 全面 |
| Ch 12 | 反射面 | Ch 15 | 全面 |
| Ch 13 | 透镜 | 无 | **Johnson 独有** |
| Ch 14 | 微带 | Ch 14 | 全面 |
| Ch 15 | 缝隙 | §4.5, §12.5 | 中等 |
| Ch 16 | 阵列馈源 | §15.8 | 简要 |
| **Part 4: Arrays** |
| Ch 17 | 线阵 | Ch 6 | 全面 |
| Ch 18 | 面阵 | §6.3 | 全面 |
| Ch 19 | 相控阵 | §7.5-7.6 | 中等 |
| Ch 20 | 自适应阵 | §7.7 | 简要 |
| Ch 21 | 随机/统计阵 | §7.8 | 简要 |
| Ch 22 | 馈电网络 | 无 | **Johnson 独有** |
| **Part 5: Special Antennas** |
| Ch 23 | RCS | Ch 16 | 全面 |
| Ch 24-25 | 卫星/航天器 | 部分涉及 | 简要 |
| Ch 26 | 手机/移动 | 无 | **Johnson 独有** |
| Ch 27 | 广播发射 | 无 | **Johnson 独有** |
| Ch 28 | 雷达 | §1.8 | 简要 |
| Ch 29 | 电子战 | 无 | **Johnson 独有** |
| Ch 30 | GPR/穿墙 | 无 | **Johnson 独有** |
| Ch 31 | 超宽带 | 无 | **Johnson 独有** |
| Ch 32-35 | 特殊 | 无 | 多数独有 |
| **Part 6: Structures & Materials** |
| Ch 36-45 | 结构/材料 | 无 | **全部 Johnson 独有** |
| **Part 7: Design Data** |
| Ch 46-53 | 设计数据 | 散见各章 | 简要提及 |

### 一句话总结交叉价值

- **Balanis 无对应**：Ch 13(透镜), Ch 22(馈电网络), Ch 26-35(特殊天线), Part 6(结构), Ch 47-53(设计数据)
- **Balanis 理论更强**：Ch 14(微带天线), Ch 6(阵列), Ch 16(RCS)
- **Johnson 工程更强**：Ch 19(相控阵), Ch 10(LPDA设计), Ch 5(测量), 所有设计表格和材料数据

---

## 附录：推荐阅读路径

### 初学者路径（与Balanis配合）
```
Balanis Ch1-5 (理论) → Johnson Ch1-5 (设计补充)
Balanis Ch4 (线天线) → Johnson Ch6-10 (线天线设计)
Balanis Ch12-14 (口径天线) → Johnson Ch11-16 (口径天线设计)
Balanis Ch6-7 (阵列) → Johnson Ch17-22 (阵列设计/馈电)
```

### 工程师桌面路径
```
Johnson Ch11-12 (喇叭/反射面) → 设计曲线查阅
Johnson Ch46-49 (波导/传输线/阻抗匹配) → 快速查询
Johnson Ch36-39 (结构/安装) → 施工参考
Johnson Ch52 (测试) → 测试方案设计
```

---

*笔记完成日期：2026-05-01*
*交叉引用基于：Balanis "Antenna Theory: Analysis and Design" 4th Ed. (Balanis 教材笔记在 `balanis_notes.md`)*

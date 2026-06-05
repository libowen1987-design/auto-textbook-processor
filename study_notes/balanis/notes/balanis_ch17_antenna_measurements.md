
---

## §17.1 Introduction

天线测量验证理论与仿真，确保天线满足设计规范。核心挑战：
- **测试环境**：消除/量化环境反射
- **远场条件**：$$R \ge \frac{2D^2}{\lambda}$$（Fraunhofer 距离）
- **阻抗匹配**：测量端面校准

### 关键术语

| 术语 | 符号 | 定义 |
|------|------|------|
| 远场距离 | $$R_{ff}$$ | $$2D^2/\lambda$$，$$D$$ 为最大口径尺寸 |
| 辐射方向图 | $$F(\theta,\phi)$$ | 归一化辐射强度空间分布 |
| 增益 | $$G$$ | $$4\pi U(\theta,\phi)/P_{in}$$ |
| 方向性 | $$D$$ | $$4\pi U(\max)/P_{rad}$$ |
| 效率 | $$\eta$$ | $$P_{rad}/P_{in} = G/D$$ |
| 极化 | — | 电场矢量的时间变化轨迹 |

### 测量不确定性源

- 有限距离误差（非平面波前）
- 多次反射（环境/支撑结构）
- 探头耦合与互耦
- 阻抗失配（$$|\Gamma|^2$$ 损耗）
- 接收机非线性与动态范围
- 电缆相位漂移与温度效应

---


### 17.2.1 反射测试场 (Reflection Range)

地面反射场利用地面作为反射面，通过镜像原理形成等效阵列。

**设计约束**：
- 天线高度 $$h_t$$ 与 $$h_r$$ 满足：$$\frac{2h_t h_r}{\lambda R} \approx n/2, \; n=1,3,5,\ldots$$
- 反射区需平滑（Rayleigh 粗糙度：$$\Delta h < \lambda/(16\sin\theta_i)$$）
- 极化选择：水平极化通常反射更强

**场强**：
$$E_{total} = E_{direct} + E_{reflected} = E_0 \frac{e^{-jkR_1}}{R_1} + E_0 \Gamma \frac{e^{-jkR_2}}{R_2}$$

其中 $$\Gamma$$ 为反射系数，$$R_1$$ 为直射路径，$$R_2$$ 为反射路径。

### 17.2.2 紧凑测试场 (Compact Range)

使用反射面在近距离内产生准平面波。

**关键技术参数**：
- 反射面尺寸：$$W \ge 3D_{quiet} + 2F\tan(\alpha_r)$$
- 静区 (Quiet Zone) 尺寸：最大待测天线口径
- 幅锥度 (Amplitude Taper)：< 0.5 dB
- 相位波纹 (Phase Ripple)：< 10°

**静区场**：
$$E_{qz}(x,y) = E_0 e^{-jkz} \cdot \left[1 + \sum_{m} A_m e^{-j(\beta_m x + \phi_m)}\right]$$

其中 $$A_m$$ 为波纹幅度，$$\beta_m$$ 为空间频率，$$\phi_m$$ 为相位。

### 17.2.3 近场测试场 (Near-Field Range)

近场扫描 → 近远场变换 (NFFF)。

**扫描类型**：
- **平面扫描** (Plane Rectilinear)：适合高增益定向天线
- **柱面扫描** (Cylindrical)：适合扇区波束天线
- **球面扫描** (Spherical)：适合全向天线

**平面近场变换公式**：
$$\mathbf{F}(\theta,\phi) = \cos\theta \iint_S \mathbf{E}_{meas}(x',y') e^{jk(x'\sin\theta\cos\phi + y'\sin\theta\sin\phi)} \,dx'\,dy'$$

对 $$z = z_0$$ 平面的切向场作二维傅里叶变换。

**采样准则 (Nyquist)**：
$$\Delta x \le \frac{\lambda}{2(1+\cos\theta_{max})}, \quad \Delta y \le \frac{\lambda}{2(1+\cos\theta_{max})}$$

简化为：$$\Delta x \le \frac{\lambda}{2}$$（当 $$\theta_{max} = 90^\circ$$）

**误差预算**：
- 探头位置误差：$$\Delta p < \lambda/100$$（典型）
- 多次反射：< -60 dB
- 截断效应（扫描面有限）：影响低角度精度

### 17.2.4 其他测试场

| 类型 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| 微波暗室 | 通用 | 全天候，低反射 | 低频受限 |
| 室外场 | 大型天线 | 真实环境 | 天气影响 |
| 升空测试场 (Rise/Range) | 低副瓣 | 地面反射低 | 机械复杂 |

---


### 方向图分类

1. **主平面方向图**：E面 ($$\phi = 0$$) 与 H面 ($$\phi = 90^\circ$$)
2. **圆锥切面**：$$\theta = const$$ 切割
3. **等值线图**：完整3D方向图

### 测量原理（远场）

$$\text{AUT} \xrightarrow{P_t,G_t} \xrightarrow{\text{空间路径}} \xrightarrow{\text{AUT作为接收}} P_r(\theta,\phi)$$

**接收功率（Fries 传输公式）**：
$$P_r(\theta,\phi) = P_t G_t(\theta_t,\phi_t) G_r(\theta_r,\phi_r) \left(\frac{\lambda}{4\pi R}\right)^2 (1 - |\Gamma_t|^2)(1 - |\Gamma_r|^2)$$

### 测量配置

- **固定天线法**：AUT 旋转，参考天线固定
- **旋转天线法**：AUT 固定，探头绕 AUT 旋转
- **俯仰－滚转 (Elevation-over-Azimuth)**:
  - $$\theta$$ → 俯仰轴 (elevation)
  - $$\phi$$ → 滚转轴 (azimuth)
  - 极化泄露：$$\Delta G_{pol} \approx 20\log_{10}(\cos\epsilon)$$, $$\epsilon$$ 为对齐误差

### 方向图参数提取

- **HPBW**: 半功率波束宽度
- **FNBW**: 第一零点波束宽度
- **SLL**: 副瓣电平 (dB)
- **前后比 (F/B Ratio)**：$$10\log_{10}(G_{max}/G_{back})$$

### 采样准则

- 主瓣：$$\Delta \theta \le 0.1 \cdot HPBW$$（1°～5° 典型）
- 副瓣区：$$\Delta \theta \le 1^\circ$$
- 零点附近更密

### 误差分析

| 误差源 | 典型值 | 影响 |
|-------|--------|------|
| 对准误差 | $$0.1^\circ$$ | 增益偏差 $$< 0.1$$ dB |
| 电缆相位漂移 | $$0.5^\circ \sim 2^\circ$$ | 方向图畸变 |
| 多次反射 | $$< -40$$ dBc | 纹波 $$< \pm 0.5$$ dB |
| 有限距离 | $$R = 2D^2/\lambda$$ | 相位误差 $$22.5^\circ$$ |

---


### 17.4.1 比较法 (Comparison Method / Gain-Transfer)

用已知增益的标准天线标定 AUT。

**步骤**：
1. 将标准增益天线（标准喇叭）置于远场
2. 测量接收功率 $$P_s$$
3. 替换为 AUT，测量 $$P_{AUT}$$
4. 计算增益：
   $$G_{AUT}(dB) = G_s(dB) + 10\log_{10}\left(\frac{P_{AUT}}{P_s}\right) - 10\log_{10}\left(\frac{1-|\Gamma_s|^2}{1-|\Gamma_{AUT}|^2}\right)$$

**注意**：阻抗失配修正项通常 $$< 0.5$$ dB，大 VSWR 时不可忽略。

### 17.4.2 绝对增益法 (Absolute Gain / Two-Antenna Method)

适用于已知增益标准不可得时。

**Friis 传输公式**：
$$P_r = P_t G_t G_r \left(\frac{\lambda}{4\pi R}\right)^2$$

对两个相同的天线：
$$G = \frac{4\pi R}{\lambda} \sqrt{\frac{P_r}{P_t}}$$
$$G(dB) = \frac{1}{2}\left[10\log_{10}\left(\frac{P_r}{P_t}\right) + 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)\right]$$

### 17.4.3 三天线法 (Three-Antenna Method)

最精准的绝对增益法，无需假设天线相同。

**测量配置**：任选三副天线 A, B, C，测量三组传输损耗

$$P_{AB} = P_t G_A G_B \left(\frac{\lambda}{4\pi R_{AB}}\right)^2 = P_t \left(\frac{\lambda}{4\pi}\right)^2 \frac{G_A G_B}{R_{AB}^2}$$

同理：
$$P_{AC} = P_t \left(\frac{\lambda}{4\pi}\right)^2 \frac{G_A G_C}{R_{AC}^2}$$
$$P_{BC} = P_t \left(\frac{\lambda}{4\pi}\right)^2 \frac{G_B G_C}{R_{BC}^2}$$

假设 $$R_{AB} = R_{AC} = R_{BC} = R$$，解方程：

$$G_A = \frac{4\pi R}{\lambda} \sqrt{\frac{P_{AB} P_{AC}}{P_t P_{BC}}}$$
$$G_B = \frac{4\pi R}{\lambda} \sqrt{\frac{P_{AB} P_{BC}}{P_t P_{AC}}}$$
$$G_C = \frac{4\pi R}{\lambda} \sqrt{\frac{P_{AC} P_{BC}}{P_t P_{AB}}}$$

**对数形式**：
$$G_A(dB) = \frac{1}{2}\left[10\log_{10}\left(\frac{P_{AB} P_{AC}}{P_t P_{BC}}\right) + 20\log_{10}\left(\frac{4\pi R}{\lambda}\right)\right]$$

### 增益测量误差

| 误差源 | 不确定性 | 说明 |
|-------|---------|------|
| 距离误差 | $$\propto 2\Delta R/R$$ | 1% 距离误差 → 0.09 dB |
| 失配误差 | $$\propto 10\log_{10}(1-|\Gamma|^2)$$ | VSWR=2 → 0.5 dB |
| 极化失配 | $$20\log_{10}(\cos\theta_{pol})$$ | $$5^\circ$$ → 0.03 dB |
| 标准增益不确定度 | $$0.2 \sim 0.5$$ dB | 传递到 AUT |
| 多次反射 | $$< \pm 0.3$$ dB | 使用时间门控 |

---


### 方向性定义
$$D = \frac{U_{max}}{U_0} = \frac{4\pi U_{max}}{P_{rad}}$$

其中 $$U_0 = P_{rad}/(4\pi)$$ 为各向同性辐射强度。

### 数值积分法

通过方向图积分计算总辐射功率：

$$P_{rad} = \int_0^{2\pi} \int_0^\pi U(\theta,\phi) \sin\theta \,d\theta\,d\phi$$

方向性：
$$D = \frac{4\pi U_{max}}{\int_0^{2\pi} \int_0^\pi U(\theta,\phi) \sin\theta \,d\theta\,d\phi}$$

### 数值积分方法

**梯形法则**：
$$P_{rad} \approx \Delta\theta \Delta\phi \sum_{m=1}^{M} \sum_{n=1}^{N} U(\theta_m,\phi_n) \sin\theta_m$$

**Simpson 法则**（精度更高）：
$$P_{rad} \approx \frac{\Delta\theta \Delta\phi}{9} \sum_{m} \sum_{n} w_{mn} U(\theta_m,\phi_n) \sin\theta_m$$

### Kraus 近似公式（用于粗略估算）

对于主瓣窄的天线：
$$D \approx \frac{4\pi}{\Theta_{1r} \Theta_{2r}}$$

其中 $$\Theta_{1r}$$、$$\Theta_{2r}$$ 为两个主平面的 HPBW（弧度）。

更精确的公式（Tai & Pereira）：
$$D \approx \frac{4\pi}{\Theta_{1r}^2 + \Theta_{2r}^2} \quad \text{(适用于高方向性天线)}$$

### 误差分析

- 测量方向图采样密度不足 → 积分误差
- 后瓣与副瓣测量不准 → 对低方向性影响大
- 极化测量不完整 → $$P_{rad}$$ 低估
- 典型方向性误差：±0.5 dB (高增益), ±1.0 dB (低增益)

---


### 极化定义

极化 = 传播方向上电场矢量尖端的时间变化轨迹。

极化椭圆参数：

$$E(z,t) = E_{x0}\cos(\omega t - kz + \phi_x)\hat{x} + E_{y0}\cos(\omega t - kz + \phi_y)\hat{y}$$

### 极化参数

| 参数 | 符号 | 定义 |
|------|------|------|
| 轴比 (AR) | $$AR$$ | $$E_{max}/E_{min} = \sqrt{1 + \tan^2(2\tau)} / \tan(\tau)$$ |
| 倾角 | $$\tau$$ | $$0.5 \arctan(2E_{x0}E_{y0}\cos\delta / (E_{x0}^2 - E_{y0}^2))$$ |
| 旋向 | — | 右旋 (RH) 或左旋 (LH) |
| 极化效率 | $$PLF$$ | $$|\hat{\rho}_w^* \cdot \hat{\rho}_a|^2$$ |

其中 $$\delta = \phi_y - \phi_x$$，$$\tau$$ 为倾角。

轴比计算公式：
$$AR = \sqrt{\frac{E_{x0}^2 + E_{y0}^2 + \sqrt{(E_{x0}^2 - E_{y0}^2)^2 + (2E_{x0}E_{y0}\cos\delta)^2}}{E_{x0}^2 + E_{y0}^2 - \sqrt{(E_{x0}^2 - E_{y0}^2)^2 + (2E_{x0}E_{y0}\cos\delta)^2}}}$$

### 极化测量方法

**1. 旋转线性探头法** (Rotating Linear Probe)

$$V(\phi) = V_{max} \cos^2(\phi - \phi_0) + V_{min} \sin^2(\phi - \phi_0)$$
$$AR = \sqrt{\frac{V_{max}}{V_{min}}}$$

测量步骤：
1. 绕传播轴旋转线性极化探头
2. 记录最大与最小电压
3. 计算轴比

**2. 三线极化法 (Three-Component Method)**

测量三个固定线性极化的幅度与相位：
$$E_1 = E_{x0}e^{j\phi_x}$$
$$E_2 = E_{120^\circ}$$
$$E_3 = E_{240^\circ}$$

重构完整极化椭圆。

**3. 圆形极化分量法**

使用线极化 + 圆极化探头，或双圆极化探头测量：

$$\text{CRR (Cross-pol Ratio)} = \frac{|E_{RH}|}{|E_{LH}|}$$
$$AR = \frac{|E_{RH}|+|E_{LH}|}{|E_{RH}|-|E_{LH}|}$$

### 极化测量误差

- 探头极化纯度（有限隔离度）
- 多径反射改变极化状态
- 探头对准误差（倾角偏差）
- 电缆去极化（弯曲/应力）

---


### 测量原理

天线输入阻抗：
$$Z_{in} = R_{in} + jX_{in}$$

### 常用仪器

1. **网络分析仪 (VNA)**：最常用，全频段扫频
   - S11 (反射系数 → 阻抗)
   - 时域门控 (TDG) 去除环境反射

2. **阻抗桥**：低频段
3. **电桥法**：平衡-不平衡转换

### 测量方程

$$\Gamma = \frac{Z_{in} - Z_0}{Z_{in} + Z_0} = S_{11}$$
$$Z_{in} = Z_0 \frac{1 + \Gamma}{1 - \Gamma}$$

### VSWR
$$VSWR = \frac{1 + |\Gamma|}{1 - |\Gamma|}$$

### 校准

| 校准类型 | 参考标准 | 精度 |
|---------|---------|------|
| SOLT (Short-Open-Load-Through) | 已知标准 | 中等 |
| TRL (Through-Reflect-Line) | 传输线标准 | 高 |
| 电子校准 (ECal) | 内置阻抗状态 | 便捷 |

### 馈点校准

测量平面必须校准到天线馈点（去嵌入 De-embedding）：
$$Z_{AUT} = Z_0 \frac{1 + \Gamma_{meas} e^{+2j\beta L}}{1 - \Gamma_{meas} e^{+2j\beta L}}$$

其中 $$L$$ 为校准面到馈点的电缆长度，$$\beta = 2\pi/\lambda_g$$ 为波导波长。

### 误差

- 连接器重复性：$$< \pm 0.05$$ dB (S11)
- 电缆相位稳定性：温度漂移
- 环境耦合：天线附近物体改变阻抗
- 低频：接地回路效应

---


### 效率定义

$$\eta = \frac{P_{rad}}{P_{in}} = \frac{G}{D}$$

### 17.8.1 方向性-增益法 (Directivity-Gain Method)

分别测量 $$G$$ 和 $$D$$：
$$\eta = \frac{G}{D}$$

难点：$$D$$ 需完整三维方向图积分，精度受采样影响。

### 17.8.2 Wheeler Cap 法

最常用的天线效率测量方法，适用于小型谐振天线。

**原理**：用导电帽 (Wheeler Cap) 包围天线，在谐振频率附近：

- 当帽尺寸 $$\ll \lambda$$：辐射电阻被短路，输入阻抗只反映损耗电阻
- 无帽时：$$Z_{in,open} = R_{rad} + R_{loss} + jX_{in}$$
- 有帽时：$$Z_{in,cap} = R_{loss} + jX_{in}'$$

**效率公式**（在谐振频率）：

$$\eta = \frac{R_{rad}}{R_{rad} + R_{loss}} = \frac{R_{in,open} - R_{in,cap}}{R_{in,open}}$$

或用电抗微调至谐振：

$$\eta = \frac{P_{rad}}{P_{in}} = 1 - \frac{P_{loss}}{P_{in}} = \frac{\Re(Z_{open}) - \Re(Z_{cap})}{\Re(Z_{open})}$$

**Wheeler Cap 尺寸要求**：
$$a < \lambda/(2\pi) \approx \lambda/6.28$$

确保帽子不产生谐振模式，天线辐射场被完全屏蔽。

### 17.8.3 随机场法 (Reverberation Chamber)

天线置于混响室中，通过模式搅拌器创建统计均匀场。

**效率计算**：
$$\eta = \frac{\langle P_{received} \rangle}{\langle P_{transmitted} \rangle}$$

统计平均消除了位置和取向依赖性。

### 17.8.4 辐射测量法

在暗室中测量完整方向图积分得到 $$P_{rad}$$：
$$\eta = \frac{\iint U(\theta,\phi) \,d\Omega}{P_{in}}$$

### 效率测量误差

| 方法 | 典型精度 | 适用 |
|-----|---------|------|
| Wheeler Cap | $$\pm 3\% \sim \pm 10\%$$ | 小型谐振天线 |
| 方向性-增益 | $$\pm 5\% \sim \pm 15\%$$ | 所有天线 |
| 混响室 | $$\pm 3\% \sim \pm 8\%$$ | 小/中型天线 |
| 辐射积分 | $$\pm 5\% \sim \pm 12\%$$ | 所有天线（耗时） |

---


### 互耦机理

阵列中天线间的互耦通过：
1. 空间辐射耦合（直接路径）
2. 表面波耦合（介质基板）
3. 馈电网络耦合（共享馈线）

### S参数测量

对于 $$N$$ 元阵列，互耦用 S 参数矩阵描述：

$$S_{ij} = \frac{V_i^-}{V_j^+} \bigg|_{V_k^+ = 0, k \neq j}$$

其中 $$V_i^-$$ 为端口 $$i$$ 的反射波，$$V_j^+$$ 为端口 $$j$$ 的入射波。

**测量步骤**：
1. 校准 VNA 到各端口参考面
2. 依次激励每个端口，测量所有端口的耦合
3. 扫描频率获得宽频数据

### 互阻抗

$$Z_{ij} = \frac{V_i}{I_j} \bigg|_{I_k = 0, k \neq j}$$

从 S 参数转换为 Z 参数：
$$[Z] = Z_0 ([I] + [S]) ([I] - [S])^{-1}$$

### 隔离度

$$I_{ij}(dB) = -20\log_{10}|S_{ij}|$$

典型要求：相邻单元 $$I > 15$$~20 dB

### 误差

- 未激励端口必须接匹配负载（$$Z_0$$）
- 外部散射环境改变耦合
- 多端口校准复杂性（$$N^2$$ 测量）
- 互耦的温度与频率依赖性

---


### 缩放原理

若所有尺寸按因子 $$s = L_{model}/L_{full}$$ 缩放，则：

$$\lambda_{model} = s \cdot \lambda_{full}$$
$$\Rightarrow f_{model} = \frac{f_{full}}{s}$$

### 缩比关系

| 参数 | 缩放关系 | 说明 |
|------|---------|------|
| 频率 | $$f_m = f_f/s$$ | 频率反比于尺寸 |
| 电导率 | $$\sigma_m = \sigma_f/s$$（严格） | 可用相同材料近似 |
| 增益 | $$G_m = G_f$$ | 无量纲，保持不变 |
| 方向图 | $$F_m(\theta,\phi) = F_f(\theta,\phi)$$ | 形状不变 |
| 阻抗 | $$Z_{in,m} = Z_{in,f}$$ | 归一化阻抗不变 |
| 损耗 | $$\tan\delta_m = \tan\delta_f \cdot s$$（严格） | 低损耗近似 |

### 实际约束

- **材料频率特性**：介质 $$\epsilon_r$$ 和 $$\mu_r$$ 需频变补偿
- **金属损耗**：趋肤深度 $$\delta_s \propto 1/\sqrt{f}$$，严格缩比需调整电导率
- **机械公差**：缩比后制造公差也需按比例缩小

### 缩比模型的应用

1. **大型天线验证**（如反射面天线）
2. **飞机／舰船平台兼容性测试**
3. **新型天线概念验证**
4. **耦合与 EMC 分析**

### 不确定度

- 材料参数缩比误差：±1%～±5%
- 制造公差累积：影响谐振频率 ±2%～±5%
- 尺寸测量误差：缩比后误差放大因子 $$1/s$$

---


| 节号 | 内容 | 核心公式 |
|------|------|---------|
| 17.2 | 测试场 | $$R \ge 2D^2/\lambda$$, NFFF: $$\mathbf{F} \propto \mathcal{F}\{\mathbf{E}_{meas}\}$$ |
| 17.3 | 方向图 | $$P_r = P_t G_t G_r (\lambda/(4\pi R))^2$$ |
| 17.4 | 增益 | 三天线法：$$G_A = \frac{4\pi R}{\lambda}\sqrt{\frac{P_{AB}P_{AC}}{P_t P_{BC}}}$$ |
| 17.5 | 方向性 | $$D = 4\pi U_{max} / \iint U(\theta,\phi)\,d\Omega$$ |
| 17.6 | 极化 | $$AR = \sqrt{V_{max}/V_{min}}$$，$$PLF = \|\hat{\rho}_w^*\cdot\hat{\rho}_a\|^2$$ |
| 17.7 | 阻抗 | $$Z_{in} = Z_0(1+\Gamma)/(1-\Gamma)$$，$$\Gamma = S_{11}$$ |
| 17.8 | 效率 | Wheeler Cap: $$\eta = (R_{open} - R_{cap})/R_{open}$$ |
| 17.9 | 互耦 | $$S_{ij} = V_i^-/V_j^+$$，$$I_{ij} = -20\log_{10}\|S_{ij}\|$$ |
| 17.10 | 缩比模型 | $$f_m = f_f/s$$, $$G_m = G_f$$, $$Z_{in,m} = Z_{in,f}$$ |

---


- Balanis, C.A., "Advanced Engineering Electromagnetics", 2nd Ed.
- IEEE Std 149-2021: Antenna Measurement Standard
- IEEE Std 1720-2012: Near-Field Antenna Measurement
- Wheeler, H.A., "The Radiansphere Around a Small Antenna", Proc. IRE, 1959

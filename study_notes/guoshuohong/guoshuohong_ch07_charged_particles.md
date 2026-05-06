# 郭硕鸿《电动力学》第七章 — 带电粒子和电磁场的相互作用

> **范围**:
> §7.1 运动带电粒子的电磁场 — Liénard-Wiechert 势
> §7.2 辐射阻尼 — 辐射反作用力, 谱线宽度
> §7.3 电磁波的散射与吸收 — 自由电子散射 (Thomson), 共振吸收
> §7.4 带电粒子在电磁场中的运动

---

**全书收官章** 🎯 从 Maxwell 方程组出发，历经静电场、静磁场、电磁波传播、辐射、相对论，终于回到 **带电粒子本身与场的相互作用**——自洽的完整的电动力学闭环。

---

## §7.1 运动带电粒子的电磁场

### 从推迟势到 Liénard-Wiechert 势

回忆第五章的推迟势（在 Lorenz 规范下）：

$$
\varphi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf{r}', t_r)}{|\mathbf{r}-\mathbf{r}'|}\, d^3\mathbf{r}'
$$

$$
\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi}\int \frac{\mathbf{J}(\mathbf{r}', t_r)}{|\mathbf{r}-\mathbf{r}'|}\, d^3\mathbf{r}'
$$

其中 **推迟时间** $t_r = t - |\mathbf{r} - \mathbf{r}'|/c$。

对于 **单个点电荷** $q$ 沿轨迹 $\mathbf{r}_0(t)$ 运动：

- 电荷密度：$\rho(\mathbf{r}', t') = q\,\delta^{(3)}(\mathbf{r}' - \mathbf{r}_0(t'))$
- 电流密度：$\mathbf{J}(\mathbf{r}', t') = q\mathbf{v}(t')\,\delta^{(3)}(\mathbf{r}' - \mathbf{r}_0(t'))$，$\mathbf{v} = \dot{\mathbf{r}}_0$

积分时注意 $\delta$ 函数的自变量是时空耦合的（$\mathbf{r}'$ 出现在 $\rho$ 和 $t_r$ 中）。利用 $\delta$ 函数的变换性质：

$$
\delta\big(f(t')\big) = \sum_i \frac{\delta(t' - t_i)}{|f'(t_i)|}
$$

经过推导得到 **Liénard-Wiechert 势**：

$$
\boxed{\varphi(\mathbf{r}, t) = \frac{1}{4\pi\varepsilon_0} \left.\frac{q}{(R - \mathbf{R}\cdot\boldsymbol{\beta})}\right|_{t_r}}
$$

$$
\boxed{\mathbf{A}(\mathbf{r}, t) = \frac{\mu_0}{4\pi} \left.\frac{q\,c\,\boldsymbol{\beta}}{(R - \mathbf{R}\cdot\boldsymbol{\beta})}\right|_{t_r} = \frac{\boldsymbol{\beta}}{c}\,\varphi(\mathbf{r}, t)}
$$

其中各量均在 **推迟时间** $t_r$ 取值：

| 符号 | 定义 |
|---|---|
| $\mathbf{R} = \mathbf{r} - \mathbf{r}_0(t_r)$ | 从粒子的推迟位置到场点的 **相对矢径** |
| $R = |\mathbf{R}|$ | 相对距离 |
| $\boldsymbol{\beta} = \mathbf{v}(t_r)/c$ | 推迟时刻的归一化速度 |
| $\boldsymbol{n} = \mathbf{R}/R$ | 从粒子指向场点的单位矢量 |

### 运动点电荷的电磁场

对 Liénard-Wiechert 势求梯度/旋度得到场。这是**全书最复杂的推导之一**，涉及对 $t_r$ 的隐函数求导。结果为 **Heaviside-Feynman 公式**：

$$
\boxed{\mathbf{E}(\mathbf{r}, t) = \frac{q}{4\pi\varepsilon_0} \left[
\frac{\boldsymbol{n} - \boldsymbol{\beta}}{\gamma^2 (1 - \boldsymbol{n}\cdot\boldsymbol{\beta})^3 R^2}
+ \frac{\boldsymbol{n}\times\big[(\boldsymbol{n} - \boldsymbol{\beta})\times\dot{\boldsymbol{\beta}}\big]}{c\,(1 - \boldsymbol{n}\cdot\boldsymbol{\beta})^3 R}
\right]_{t_r}}
$$

$$
\boxed{\mathbf{B}(\mathbf{r}, t) = \frac{1}{c}\; \boldsymbol{n} \times \mathbf{E}(\mathbf{r}, t)}
$$

#### 两项的物理意义

1. **第一项（速度场 / 自场）** $\propto 1/R^2$：
   - 不依赖于加速度 $\dot{\boldsymbol{\beta}}$
   - 与静电场 $\propto 1/R^2$ 类似，但被 $\gamma$ 和运动方向修正（**收缩效应**）
   - 随粒子运动而"拖拽"，始终以速度 $c$ 传播
   - **不辐射能量**

2. **第二项（加速度场 / 辐射场）** $\propto 1/R$：
   - 正比于加速度 $\dot{\boldsymbol{\beta}}$
   - $\propto 1/R$ —— **远区主导项**
   - 电场方向与 $\boldsymbol{n}$ 和 $\dot{\boldsymbol{\beta}}$ 有关，是 **横波**（$\mathbf{E} \perp \boldsymbol{n}$）
   - **辐射能量**

### 特殊情况：低速运动的辐射场

当 $v \ll c$（即 $\beta \ll 1, \gamma \approx 1$），忽略 $\beta$ 的高阶项：

$$
\mathbf{E}_{\text{rad}} \approx \frac{q}{4\pi\varepsilon_0 c^2} \frac{\boldsymbol{n}\times(\boldsymbol{n}\times\dot{\mathbf{v}})}{R} \quad (v \ll c)
$$

利用矢量恒等式 $\boldsymbol{n}\times(\boldsymbol{n}\times\dot{\mathbf{v}}) = (\boldsymbol{n}\cdot\dot{\mathbf{v}})\boldsymbol{n} - \dot{\mathbf{v}}$，其垂直于 $\boldsymbol{n}$ 的分量即为辐射场。

**玻印亭矢量（远区）：**

$$
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B} = \frac{1}{\mu_0 c} |\mathbf{E}|^2 \boldsymbol{n}
$$

**辐射功率角分布（低速）：**

$$
\frac{dP}{d\Omega} = \frac{q^2}{16\pi^2\varepsilon_0 c^3}\, |\boldsymbol{n}\times(\boldsymbol{n}\times\dot{\mathbf{v}})|^2
= \frac{q^2\dot{v}^2}{16\pi^2\varepsilon_0 c^3} \sin^2\theta
$$

其中 $\theta$ 是 $\dot{\mathbf{v}}$ 与 $\boldsymbol{n}$ 的夹角。这是 **偶极辐射** 方向图。

积分得 **Larmor 公式**：

$$
\boxed{P = \frac{q^2 \dot{v}^2}{6\pi\varepsilon_0 c^3}}
$$

### 特殊情况：高速运动的辐射场

高速时需保留完整的 $\beta$ 和 $\gamma$ 因子。对 **瞬时共动惯性系（momentarily comoving frame）**，Larmor 公式仍然成立（在该系下粒子瞬时静止）。通过 Lorentz 变换回到实验室系：

$$
P' = \frac{q^2}{6\pi\varepsilon_0 c^3}\, \gamma^6\big[\dot{\mathbf{v}}_\parallel^2 + \gamma^2 \dot{\mathbf{v}}_\perp^2\big] \quad (\text{相对论推广})
$$

其中 $\dot{\mathbf{v}}_\parallel$ 和 $\dot{\mathbf{v}}_\perp$ 分别是加速度平行和垂直于速度方向的分量。

**重点结论**：
- $\dot{\mathbf{v}}_\parallel$ 项的辐射功率 $\propto \gamma^6$ — **直线加速器辐射**
- $\dot{\mathbf{v}}_\perp$ 项的辐射功率 $\propto \gamma^8$ — **回旋/同步辐射**（更剧烈！）

---

## §7.2 辐射阻尼

### 辐射的反作用

加速电荷辐射能量，因此辐射场对电荷有一个 **反作用力** $\mathbf{F}_s$（自作用力）。辐射的能量和动量来自带电粒子自身，所以粒子的运动方程需包含反作用项：

$$
m\ddot{\mathbf{r}} = \mathbf{F}_{\text{ext}} + \mathbf{F}_s
$$

### Abraham-Lorentz 力（非相对论）

考虑有限大小带电球模型（取极限）可推导出辐射反作用力的近似表达式：

$$
\boxed{\mathbf{F}_s = \frac{q^2}{6\pi\varepsilon_0 c^3}\,\dot{\mathbf{v}} = m\,\tau_0\,\dot{\mathbf{v}}}
$$

其中：

$$
\tau_0 = \frac{q^2}{6\pi\varepsilon_0 m c^3} \quad \text{（特征时间尺度）}
$$

对于电子：

$$
\tau_0 \approx \frac{e^2}{6\pi\varepsilon_0 m_e c^3} \approx 6.27 \times 10^{-24}\,\text{s}
$$

**Abraham-Lorentz 方程：**

$$
\boxed{m(\ddot{\mathbf{r}} - \tau_0 \dddot{\mathbf{r}}) = \mathbf{F}_{\text{ext}}}
$$

这一方程是三阶的，存在 **非物理解**（预加速解 runaway solutions），需小心处理。

### 谱线宽度

考虑一个受阻尼的谐振子：$m\ddot{x} + m\omega_0^2 x = F_s = m\tau_0 \dddot{x}$。

在小阻尼近似下，解为：

$$
x(t) \approx x_0 e^{-\Gamma t/2} \cos(\omega_0 t)
$$

其中阻尼系数：

$$
\Gamma = \omega_0^2 \tau_0
$$

辐射功率正比于 $|x|^2$，因此衰变寿命：

$$
\tau = \frac{1}{\Gamma} = \frac{1}{\omega_0^2 \tau_0}
$$

**自然线宽（自然展宽）**：辐射谱的能量分布为 **Lorentz 线型**：

$$
I(\omega) = I_0\, \frac{\Gamma/2\pi}{(\omega - \omega_0)^2 + (\Gamma/2)^2}
$$

线宽（FWHM）：$\Delta\omega = \Gamma = \omega_0^2 \tau_0$

对于原子光谱中的电偶极跃迁，$\Gamma \sim 10^8\,\text{s}^{-1}$，对应的 $\Delta\lambda \sim 10^{-4}\,\text{nm}$。

### 辐射阻尼的特征时间

电子辐射阻尼特征时间 $\tau_0 \sim 10^{-24}\,\text{s}$，意味着**在几乎所有经典场景中辐射反作用都可忽略**，只在极高加速度（如高能粒子在强磁场中回旋）时才显著。

---

## §7.3 电磁波的散射与吸收

### 自由电子的散射 — Thomson 散射

考虑自由电子受平面电磁波驱动：

$$
m\ddot{\mathbf{r}} = -e\mathbf{E}_0 e^{-i\omega t}
$$

电子做简谐振荡：$\mathbf{r} = \frac{e}{m\omega^2}\,\mathbf{E}_0 e^{-i\omega t}$

振荡电子辐射电磁波，即 **散射波**。由 Larmor 公式：

**散射总功率：**

$$
P = \frac{e^2}{6\pi\varepsilon_0 c^3}\,\dot{v}^2
= \frac{e^4 E_0^2}{6\pi\varepsilon_0 m^2 c^3}
$$

入射波能流密度（平均）：$\bar{S} = \frac{1}{2}\varepsilon_0 c E_0^2$

**Thomson 散射截面：**

$$
\boxed{\sigma_T = \frac{P}{\bar{S}} = \frac{8\pi}{3}\left(\frac{e^2}{4\pi\varepsilon_0 m c^2}\right)^2 = \frac{8\pi}{3} r_e^2}
$$

其中 **经典电子半径**：

$$
\boxed{r_e = \frac{e^2}{4\pi\varepsilon_0 m_e c^2} \approx 2.818 \times 10^{-15}\,\text{m}}
$$

**数值：** $\sigma_T \approx 6.65 \times 10^{-29}\,\text{m}^2$（约 $0.67\,\text{barn}$）

**Thomson 散射的特点：**
- 与频率无关（$\omega \ll mc^2/\hbar$ 时成立）
- 散射截面与电子半径平方同数量级
- 角分布：$\frac{d\sigma}{d\Omega} = r_e^2 \sin^2\Theta$（$\Theta$ 为入射-散射方向夹角，对偏振光还需附加因子）

### 带电谐振子的散射与吸收

真实原子中的束缚电子更接近谐振子模型，有固有频率 $\omega_0$ 和阻尼 $\Gamma$：

$$
m\ddot{x} + m\Gamma \dot{x} + m\omega_0^2 x = -eE_0 e^{-i\omega t}
$$

稳态解：

$$
x(t) = \frac{-eE_0}{m} \frac{e^{-i\omega t}}{\omega_0^2 - \omega^2 - i\omega\Gamma}
$$

#### 散射截面

对于束缚电子，**散射截面**（reradiate 的部分）：

$$
\boxed{\sigma_s(\omega) = \sigma_T\;\frac{\omega^4}{(\omega_0^2 - \omega^2)^2 + \omega^2\Gamma^2}}
$$

- $\omega \ll \omega_0$ 时：$\sigma_s \propto \omega^4$ — **Rayleigh 散射**（天空呈蓝色）
- $\omega \gg \omega_0$ 时：$\sigma_s \to \sigma_T$ — 趋近 Thomson 散射（自由电子）
- $\omega \approx \omega_0$ 时：$\sigma_s$ 有尖锐 **共振峰**，峰值 $\sigma_{\max} = \sigma_T (\omega_0/\Gamma)^2$

#### 吸收截面

**吸收截面**（耗散的部分，对应阻尼 $\Gamma \dot{x}$）：

$$
\boxed{\sigma_a(\omega) = \sigma_T\;\frac{\Gamma \omega_0^2}{(\omega_0^2 - \omega^2)^2 + \omega^2\Gamma^2} \cdot \frac{3c^2 \Gamma}{2\omega_0^2 r_e}}
$$

更常用的统一表达式——**共振吸收截面（Lorentz 线型）**：

$$
\sigma_{\text{abs}}(\omega) = \frac{\pi e^2}{2m\varepsilon_0 c}\,\frac{(\Gamma/2)}{(\omega - \omega_0)^2 + (\Gamma/2)^2}
$$

在共振点 $\omega = \omega_0$ 处：

$$
\sigma_{\text{abs}}(\omega_0) = \frac{2\pi e^2}{m\varepsilon_0 c\Gamma} = \frac{3\lambda_0^2}{2\pi}
$$

$\lambda_0 = 2\pi c/\omega_0$ 为共振波长。注意：共振吸收截面与 $\lambda_0^2$ 成正比，**与原子大小的具体细节无关**。

### 色散关系与 Kramers-Kronig 关系

介质的折射率和吸收系数通过 **Kramers-Kronig 关系** 相联系——由于因果律，$\varepsilon(\omega)$ 的实部和虚部不是独立的：

$$
\text{Re}\,\varepsilon(\omega) = 1 + \frac{2}{\pi}\mathcal{P}\int_0^\infty \frac{\omega'\,\text{Im}\,\varepsilon(\omega')}{\omega'^2 - \omega^2}\,d\omega'
$$

$$
\text{Im}\,\varepsilon(\omega) = -\frac{2\omega}{\pi}\mathcal{P}\int_0^\infty \frac{\text{Re}\,\varepsilon(\omega') - 1}{\omega'^2 - \omega^2}\,d\omega'
$$

其中 $\mathcal{P}$ 表示 Cauchy 主值积分。

---

## §7.4 带电粒子在电磁场中的运动

### Lorentz 力方程

带电粒子 $q$ 在外电磁场中的运动由 Lorentz 力决定：

$$
\boxed{\frac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})}
$$

其中 $\mathbf{p} = \gamma m\mathbf{v}$ 是相对论动量。

#### 静止均匀磁场中的回旋运动

若 $\mathbf{B} = B\hat{z}$，$\mathbf{E} = 0$：

- 垂直方向：**回旋运动**（匀速圆周）
- 平行方向：**匀速直线运动**
- 合运动：**螺旋线**

**回旋频率（非相对论）：** $\omega_c = \frac{qB}{m}$

**相对论回旋频率：** $\omega_c = \frac{qB}{\gamma m}$ — 质量增加使频率降低

**回旋半径（Larmor 半径）：**

$$
r_L = \frac{m v_\perp}{|q|B} = \frac{p_\perp}{|q|B} \quad (\text{非相对论})
$$

$$
r_L = \frac{\gamma m v_\perp}{|q|B} \quad (\text{相对论})
$$

### 均匀恒定电磁场中的漂移

当 $\mathbf{E}$ 和 $\mathbf{B}$ 同时存在：

#### $\mathbf{E} \perp \mathbf{B}$ 时的 $\mathbf{E}\times\mathbf{B}$ 漂移

运动方程解中出现垂直于两者的**漂移速度**：

$$
\boxed{\mathbf{v}_d = \frac{\mathbf{E} \times \mathbf{B}}{B^2}}
$$

特点：
- 与电荷 **符号无关**（正负电荷向同一方向漂移）
- 与非相对论或相对论无关
- 物理图像：电场加速，磁场偏转，合成漂移

#### 其他漂移

| 漂移类型 | 原因 | 漂移速度 |
|---|---|---|
| $\mathbf{E}\times\mathbf{B}$ 漂移 | 恒定电场 | $\mathbf{E}\times\mathbf{B}/B^2$ |
| 梯度漂移 | 磁场空间非均匀 | $\frac{mv_\perp^2}{2qB^3}(\mathbf{B}\times\nabla B)$ |
| 曲率漂移 | 磁力线弯曲 | $\frac{mv_\parallel^2}{qB^2R_c^2}\,\mathbf{R}_c\times\mathbf{B}$ |
| 极化漂移 | 电场变化 | $\frac{m}{qB^2}\frac{d\mathbf{E}_\perp}{dt}$ |

### 非均匀磁场中的运动 — 绝热不变量

在缓慢变化的磁场中（$\nabla B / B \ll \omega_c/v$），粒子的某些量近似守恒：

1. **磁矩绝热不变量：**

$$
\boxed{\mu = \frac{m v_\perp^2}{2B} \approx \text{const}}
$$

2. **纵向绝热不变量：**

$$
J = \oint p_\parallel \, dl \approx \text{const}
$$

3. **磁通绝热不变量：** 粒子回旋轨道所包围的磁通量 $\Phi \approx \text{const}$

#### 磁镜效应

由于 $\mu$ 守恒，当粒子从弱磁场区移入强磁场区时：

$$
v_\perp \propto \sqrt{B}
$$

由能量守恒 $v_\parallel^2 + v_\perp^2 = \text{const}$，$v_\parallel$ 减小。当 $B$ 足够大时 $v_\parallel \to 0$，粒子**反射**。

**磁镜比：**

$$
R_m = \frac{B_{\max}}{B_{\min}}
$$

**损失锥：** 只有 $v_\perp/v_\parallel$ 大于某个阈值的粒子才被约束。

**应用：** 托卡马克、磁约束核聚变、地球范艾伦辐射带。

### 相对论带电粒子运动

Lorentz 力方程的四维协变形式：

$$
\frac{dp^\mu}{d\tau} = q\,F^{\mu\nu} u_\nu
$$

其中 $p^\mu = m u^\mu$ 是四维动量，$F^{\mu\nu}$ 是电磁场张量。

**应用：**
- 粒子加速器（回旋加速器、同步加速器）设计
- 同步辐射计算（SSRF、HEPS 等光源）
- 宇宙线传播与太阳物理
- 等离子体约束

---

## 全书总结 🎉

| 章 | 主题 | 核心内容 |
|---|---|---|
| Ch1 | 电磁现象基本规律 | Maxwell 方程组, 边界条件, 能量动量 |
| Ch2 | 静电场 | 分离变量, 镜像法, 多极展开 |
| Ch3 | 静磁场 | 矢势, 磁标势, 磁多极 |
| Ch4 | 电磁波传播 | 波动方程, 偏振, 波导,  Fresnel 公式 |
| Ch5 | 辐射 | 推迟势, 电偶极辐射, 天线 |
| Ch6 | 狭义相对论 | Lorentz 变换, 四维势, 场张量, 质能方程 |
| **Ch7** | **带电粒子与场** | **Liénard-Wiechert, 辐射阻尼, Thomson散射, Lorentz力** |

**全书收官！** 🎯 从 Maxwell 方程出发，经历了从静到动、从低速到高速、从无源到有源的完整旅程，最终回到带电粒子本身与电磁场的相互作用。这不仅是电动力学的自然终点，也是通向量子电动力学（QED）的桥梁。

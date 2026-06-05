# 廖承恩《微波技术基础》第7章

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## 第7章 微波谐振器

### 7.1 谐振器的基本特性与参数

**谐振频率 $\omega_0$**：电纳 $B(\omega) = 0$ 的频率（或电抗 $X(\omega) = 0$）

**品质因数 $Q$**：

$$Q = \frac{\omega_0 W}{P_L} = \frac{\text{谐振器存储的能量}}{\text{每周期损耗的能量}} \times 2\pi$$

其中 $W$ 为存储能量，$P_L$ 为损耗功率。

**带宽 $BW$**：

$$BW = \frac{f_0}{Q}$$

**有载 $Q_L$**：

$$\frac{1}{Q_L} = \frac{1}{Q_U} + \frac{1}{Q_e}$$

$Q_U$ 为无载 $Q$（固有品质因数），$Q_e$ 为外部品质因数（耦合品质因数）。

### 7.2 串联和并联谐振电路

**串联谐振**：
- 谐振时 $Z \approx R$，$X=0$
- $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 CR}$
- 阻抗频率响应：$|Z| \approx R\sqrt{1 + Q^2(2\Delta\omega/\omega_0)^2}$

**并联谐振**：
- 谐振时 $Y \approx G$，$B=0$
- $Q = \frac{\omega_0 C}{G} = \frac{R}{\omega_0 L}$
- 阻抗频率响应：$|Z| \approx R\sqrt{1 + Q_L^2(2\Delta\omega/\omega_0)^2}$

### 7.3 金属波导谐振腔

**矩形谐振腔**：由电壁围成的金属腔体，尺寸 $a \times b \times d$，内部填充均匀介质。

**模式 $\mathrm{TE}_{mnp}$、$\mathrm{TM}_{mnp}$**：

$$f_{mnp} = \frac{c}{2\sqrt{\varepsilon_r}} \sqrt{\left(\frac{m}{a}\right)^2 + \left(\frac{n}{b}\right)^2 + \left(\frac{p}{d}\right)^2}$$

**品质因数 $Q$**（导体损耗）：

$$Q \approx \frac{1}{\alpha_c} \left(\frac{2\pi}{\lambda_g}\right) \propto \frac{1}{\delta_s}$$

其中 $\delta_s$ 为趋肤深度，$\alpha_c$ 为导体衰减常数。

### 7.4 介质谐振器

使用高介电常数 ($\varepsilon_r \approx 30-100$) 低损耗介质材料制成，尺寸远小于工作波长。

**$\mathrm{TE}_{01\delta}$ 模式**：主模，$Q_U$ 高（可达 $10^4$ 量级）。

---


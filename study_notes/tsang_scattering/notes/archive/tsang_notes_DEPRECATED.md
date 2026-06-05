# Tsang《Scattering of Electromagnetic Waves: Numerical Simulations》
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao
Wiley, 2001 — 3 Volumes

> 基于 OCR 文本洗稿，100% 源自原书

---

## 目录结构

- **Volume I: Numerical Simulations** — 主要数值方法
- **Volume II: Advanced Topics** — 增强绕射公式、波传播
- **Volume III: Microwave Interaction** — 亮温与被动遥感

---

## 第 1 章：Monte Carlo Methods for Layered Media

### 1.1 蒙特卡洛方法概述

Monte Carlo 方法通过随机抽样模拟波与随机介质的相互作用。基本思想：

1. 生成随机入射角和极化
2. 计算反射/透射系数
3. 跟踪多次散射事件
4. 统计平均得到总体散射特性

### 1.2 分层介质模型（Layered Media Model）

介质参数：
- $\varepsilon_r$：相对介电常数（复数形式 $\varepsilon_r = \varepsilon_r' - j\varepsilon_r''$）
- $\sigma$：电导率（S/m）
- $\mu_r$：相对磁导率

传播常数：$\gamma = \alpha + j\beta = j\omega\sqrt{\mu\varepsilon}$

### 1.3 多次散射（Multiple Scattering）

能量传递系数（塘合系数）：
$$T = e^{-\gamma \cdot d}$$

散射系数取决于表面粗糙度和介电常数对比。

---

## 第 2 章：Integral Equations and Moment Methods

### 2.1 积分方程形式

表面电流 $J$ 满足：
$$\oint_S G(\mathbf{r}, \mathbf{r}') J(\mathbf{r}') ds' = E_{\text{inc}}(\mathbf{r})$$

其中 $G$ 为格林函数（Green's function）。

### 2.2 矩量法（Method of Moments / MoM）

将连续方程离散化：
1. 基函数展开：$J = \sum_n a_n f_n$
2. 配置点法（Point Matching）或 Galerkin 法
3. 形成矩阵方程 $Z \cdot I = V$
4. 求解 $I = Z^{-1} V$

计算复杂度：$O(N^2)$（$N$ 为未知量个数）

### 2.3 快速方法

- **SMCG**（Sparse-Matrix Canonical Grid）：稀疏矩阵 + 规则网格
- **FMM**（Fast Multipole Method）：$O(N \log N)$ 复杂度
- **MLFMA**：多层快速多极子

---

## 第 4 章：Rough Surface Simulation

### 4.1 表面粗糙度参数

- 均方根高度（RMS height）：$\sigma_h$
- 相关长度（Correlation length）：$l_c$
- 高度分布概率密度函数（PDF）

高斯相关函数：
$$R(\rho) = \sigma_h^2 \exp\left(-\frac{\rho^2}{l_c^2}\right)$$

### 4.2 Small Perturbation Method (SPM)

适用于 $\sigma_h < \lambda/10$ 的弱粗糙表面：
$$\sigma_{\text{spm}} \propto \sigma_h^2 \cdot k^4$$

### 4.3 Numerical Methods for Rough Surfaces

- **有限差分时域法（FDTD）**
- **矩量法（MoM）**
- **边界积分方程法（BIE）**

---

## 第 5 章：Brightness Temperature and Passive Sensing

### 5.1 亮温定义

$$T_B = \varepsilon \cdot T_{\text{physical}}$$

其中 $\varepsilon$ 为发射率，$T_{\text{physical}}$ 为物理温度（K）。

### 5.2 辐射传输方程（Radiative Transfer）

$$\frac{dT_B}{ds} = -T_B + \varepsilon \cdot T$$

在热力学平衡下：
$$\int_0^\infty \varepsilon(\nu) \cdot T \cdot d\nu = \frac{h\nu}{e^{h\nu/kT} - 1}$$

### 5.3 土壤湿度遥感

L波段（1.4 GHz）和 C 波段（6.9 GHz）对土壤水分敏感。
干燥土壤：$\varepsilon_r' \approx 3$，湿润土壤：$\varepsilon_r' \approx 20$+

---

## 附录：物理常数

| 常数 | 符号 | 值 |
|------|------|-----|
| 光速 | $c$ | $2.998 \times 10^8$ m/s |
| 自由空间阻抗 | $\eta_0$ | $376.73\ \Omega$ |
| 玻尔兹曼常数 | $k_B$ | $1.38 \times 10^{-23}$ J/K |
| 普朗克常数 | $h$ | $6.626 \times 10^{-34}$ J·s |

---
chapter: 12
title: Concluding Remarks on Computational Electromagnetics
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 675–704
sections: 3
examples: 0
---

# Chapter 12: Concluding Remarks on Computational Electromagnetics | 第十二章：计算电磁学总结

> **中英双语版**

## 12.1 Overview of Computational Electromagnetics | 计算电磁学概述 (pp. 651–678)

CEM methods divide into **time-domain** and **frequency-domain**, related by Fourier transform / 计算电磁学方法分为**时域**和**频域**，通过傅里叶变换联系。

### 12.1.1 Frequency- vs. Time-Domain Analysis | 频域与时域分析对比

| Feature / 特性 | Frequency Domain / 频域 | Time Domain / 时域 |
|---------|:----------------:|:-----------:|
| 维度 | 3D + 1参数 ($\omega$) | 4D (空间 + 时间) |
| 矩阵求解 | 每频率一次 | 时间步进 |
| 多激励 | 高效（矩阵可复用） | 需重复 |
| 宽带 | 需要多频率 | 单次运行足够 |
| 色散媒质 | 自然 | 更复杂 |
| 非线性媒质 | 困难 | 自然 |

### 12.1.2 High-Frequency Asymptotic Techniques | 高频渐近技术 (pp. 652–654)

基于当物体 $\gg \lambda$ 时的射线光学：

- **GO** (Geometrical Optics / 几何光学): 斯涅尔定律射线追踪；阴影区场为零。
- **GTD** (Geometrical Theory of Diffraction / 几何绕射理论): 添加来自棱边的绕射场。
- **UTD** (Uniform Theory of Diffraction / 一致性绕射理论): 阴影边界处的过渡函数。
- **PO** (Physical Optics / 物理光学): 照亮侧 $\mathbf{J}_s \approx 2\hat{n}\times\mathbf{H}^{\text{inc}}$，阴影侧为0。
- **PTD** (Physical Theory of Diffraction / 物理绕射理论): 添加边缘效应的边缘电流。
- **SBR** (Shooting and Bouncing Rays / 弹跳射线法): 射线网格通过GO追踪，每次弹跳进行PO积分。

渐近方法快但近似；数值方法精确但昂贵。

### 12.1.3 First-Principle Numerical Methods | 第一性原理数值方法 (pp. 654–656)

**PDE methods / 偏微分方程方法** (FDM, FEM):
- 静态：椭圆型PDE → 正定矩阵
- 时谐：双曲型PDE → 不定矩阵 → 迭代收敛慢
- 色散误差：相误差 $\propto O[(h/\lambda)^2]$（线性基），累积性
- 高阶基指数级降低相误差

**Integral equation methods / 积分方程方法** (MoM):
- SIE（表面积分）：对不可穿透/均匀区域
- VIE（体积分）：对非均匀区域
- EFIE：第一类弗雷德霍姆方程 → 精确但收敛慢
- MFIE：第二类弗雷德霍姆方程 → 收敛快但精度低
- CFIE：对封闭体的组合 → 消除内部谐振
- 预条件：Calderón恒等式、块对角、近邻

**PEEC** (Partial Element Equivalent Circuit / 部分元等效电路): 将EFIE转化为电路模型，用于EMI/EMC。

### 12.1.4 Time-Domain Methods | 时域方法 (pp. 656–658)

| Method / 方法 | Key Feature / 关键特性 |
|--------|:-----------:|
| **FDTD** (Yee, 1966) | 显式蛙跳，每步 $O(N)$ |
| **FETD** | 非结构网格，隐式/显式 |
| **TLM** | 传输线矩阵，惠更斯原理 |
| **FIT** (Weiland) | 对偶网格上的有限积分 |
| **FVTD** | 守恒型有限体积，激波捕捉 |
| **PSTD** | 傅里叶伪谱，粗网格 |
| **MRTD** | 小波基，多分辨率 |
| **DGTD** | 间断伽辽金，单元局部，并行 |

### 12.1.5 Surface Integral Equations | 表面积分方程 (pp. 658–660)

For PEC bodies / 对PEC体：
- EFIE: $\hat{n}\times(\mathcal{L}\mathbf{J}) = -\hat{n}\times\mathbf{E}^{\text{inc}}$
- MFIE: $\frac{1}{2}\mathbf{J} - \hat{n}\times(\mathcal{K}\mathbf{J}) = -\hat{n}\times\mathbf{H}^{\text{inc}}$
- CFIE: $\alpha\text{EFIE} + (1-\alpha)\eta\text{MFIE}$

For dielectric bodies / 对介质体：PMCHWT公式，同时使用EFIE和MFIE。

### 12.1.6 Volume Integral Equations | 体积分方程 (pp. 660–662)

For inhomogeneous dielectrics / 对非均匀介质：

$$
\mathbf{E}(\mathbf{r}) = \mathbf{E}^{\text{inc}}(\mathbf{r}) + k_0^2\iiint_V (\epsilon_r(\mathbf{r}') - 1)\mathbf{E}(\mathbf{r}')G_0(\mathbf{r},\mathbf{r}')\,dV' + \nabla\iiint_V \frac{(\epsilon_r(\mathbf{r}') - 1)\nabla'\cdot\mathbf{E}(\mathbf{r}')}{k_0^2} G_0(\mathbf{r},\mathbf{r}')\,dV'
$$

VIE yields $3N$ unknowns for $N$ volume cells (vs $2N$ for SIE on surface) / VIE对 $N$ 个体单元产生 $3N$ 个未知量（而SIE在表面上为 $2N$）。

## 12.2 Practical Applications | 实际应用 (pp. 678–690)

### 12.2.1 Antenna Analysis and Design | 天线分析与设计
- Wire antennas / 线天线 (MoM-Wu-King, Hallén, Pocklington)
- Microstrip antennas / 微带天线 (FEM, MoM with layered Green's function / 使用分层格林函数的矩量法)
- Reflector antennas / 反射面天线 (PO/PTD + FMM)
- Antenna arrays / 天线阵列 (FEM for finite arrays / 有限阵列的FEM, periodic BC for infinite / 无限的周期边界条件)

### 12.2.2 Microwave Circuits | 微波电路
- Waveguide components / 波导元件 (FEM, Mode matching / 模式匹配)
- Filters / 滤波器 (FEM with adaptive mesh refinement / 自适应网格细化的FEM)
- Power dividers, couplers / 功分器、耦合器
- RFIC/MMIC (PEEC, FEM)

### 12.2.3 Scattering and RCS | 散射与RCS
- Monostatic RCS / 单站RCS (FMM/MLFMA with iterative solves for each angle / 对各角度进行迭代求解)
- Bistatic RCS / 双站RCS
- Radar signature / 雷达特征 (SBR for complex targets / 复杂目标的弹跳射线法)

### 12.2.4 EMC/EMI | 电磁兼容/电磁干扰
- Cable coupling / 电缆耦合 (TL theory + MoM / 传输线理论+矩量法)
- Shielding effectiveness / 屏蔽效能 (FEM)
- System-level EMC / 系统级电磁兼容 (hybrid methods / 混合方法)

### 12.2.5 Biomedical Applications | 生物医学应用
- SAR calculation / SAR计算 (FDTD, FEM)
- Hyperthermia treatment planning / 热疗治疗计划
- Medical imaging / 医学成像 (microwave tomography / 微波层析成像)
- Wireless body area networks / 无线体域网

### 12.2.6 Photonics and Optics | 光子学与光学
- Optical waveguides / 光波导 (FEM with PML)
- Photonic crystals / 光子晶体 (FDTD, FEM)
- Plasmonic structures / 等离激元结构
- Nonlinear optics / 非线性光学 (FDTD with nonlinear materials / 带非线性材料的FDTD)

## 12.3 Challenges and Future Trends | 挑战与未来趋势 (pp. 690–704)

### 12.3.1 Computational Challenges | 计算挑战
- **Multi-scale problems / 多尺度问题**: 电大结构中的精细特征
- **Multi-physics / 多物理**: 电磁 + 热 + 力耦合
- **Uncertainty quantification / 不确定性量化**: 随机几何/材料
- **Real-time simulation / 实时仿真**: 数字孪生

### 12.3.2 Algorithmic Development | 算法发展
- 间断伽辽金方法 (DGTD, DGFEM)
- 等几何分析 (IGA) — 高阶光滑基
- 模型降阶 (MOR) — 缩减基、POD
- 区域分解方法 (DDM) — 加性Schwarz、FETI

### 12.3.3 Hardware Acceleration | 硬件加速
- GPU加速：$10\times$–$100\times$ 对FDTD、FEM、MoM加速
- 众核CPU (Xeon Phi)
- 基于FPGA的电磁求解器
- 用于基于ML方法的张量处理单元 (TPU)

### 12.3.4 Machine Learning in CEM | 计算电磁学中的机器学习
- 电磁分析的代理模型
- 基于神经网络的求解器 (PINN)
- 用于网格生成和优化的ML
- ML加速的迭代求解器
- 使用深度学习的逆向设计

### 12.3.5 High-Performance Computing | 高性能计算
- 使用区域分解+MPI的并行FDTD
- 使用混合MPI/OpenMP的分布式MLFMA
- 基于云的电磁仿真
- 百亿亿次计算：$10^{18}$ FLOPs

### 12.3.6 CEM at Extremes | 极端条件下的计算电磁学
- **低频**: DC到日光——需要特殊公式保持稳定收敛
- **超高频**: 太赫兹、光子学
- **电大**: $>10^6\lambda$（渐近+数值混合）
- **电小**: 量子电磁效应

## 12.4 Summary: Choosing the Right Method | 总结：选择正确的方法

| Problem Type / 问题类型 | Recommended Method / 推荐方法 | Why / 原因 |
|:-------------|:------------------:|:----|
| Large, smooth scatterer ($\gg\lambda$) / 大而光滑的散射体 | PO/PTD, UTD, SBR | 渐近法，非常快 |
| Small-to-medium, complex geometry / 中小规模复杂几何 | FEM | 几何灵活性，稀疏矩阵 |
| Open region, homogeneous objects / 开放区域，均匀物体 | MoM + MLFMA | 精确辐射条件，$O(N\log N)$ |
| Broadband, nonlinear / 宽带，非线性 | FDTD, FETD, DGTD | 单次运行，宽带 |
| Inhomogeneous + complex / 非均匀+复杂 | FE-BI, hybrid FEM/MoM | 两全其美 |
| Circuit/package EMC / 电路/封装电磁兼容 | PEEC, FEM | 电路理论友好 |
| Biophotonics/nanophotonics / 生物光子学/纳米光子学 | FDTD, FEM | 处理色散、非线性 |

## **Physical Intuition / 物理直觉**
- 不存在单一的"最佳"计算电磁学方法——选择取决于问题几何、频率范围、材料属性和所需精度。
- 精度、速度和通用性之间的权衡是根本性的：渐近方法快但近似，数值方法精确但昂贵。
- 混合方法试图兼得——对每个子区域使用正确的工具。

## **Numerical Intuition / 数值直觉**
- $N \sim \lambda/h$：对 $\lambda/10$ 网格，$10\lambda\times10\lambda\times10\lambda$ 体积有 $10^6$ 个单元 → VIE需要300万未知量，但SIE仅需约6万。
- MLFMA使 $N\sim 10^7$ 当前可行——$100\lambda$ 球体需要约 $10^7$ 未知量，占用约 100 GB内存。
- GPU上的FDTD每秒可处理10亿单元——$1000^3$ 网格以约 15 时间步/秒运行。
- ML加速求解器对参数扫描可提供 $10\times$–$100\times$ 加速。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Content / 关键内容 | Verified / 验证 |
|---------|-------|:-----------:|:--------:|
| 12.1 | 651–662 | CEM概述，方法分类 | ✓ |
| 12.2 | 678–690 | 应用 | ✓ |
| 12.3 | 690–704 | 挑战，未来趋势 | ✓ |

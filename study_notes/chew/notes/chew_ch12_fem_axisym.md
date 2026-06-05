# Chapter 12: Finite Element Analysis of Complex Axisymmetric Problems
# 第十二章：复杂轴对称问题的有限元分析

**Author 作者**: Andrew D. Greenwood and Jian-Ming Jin

## 12.1 引言 | Introduction

**轴对称物体（Body of Revolution, BOR）** 同时是重要的雷达目标和天线辐射结构。由于旋转对称性，3D问题可以降维为2D计算，显著降低计算复杂度。

**传统方法及其局限**：
- **MOM（矩量法）**：基于积分方程，对 PEC 或均匀材料表现良好；但涉及非均匀材料时计算复杂度急剧上升（需要体 formulation 且产生稠密矩阵）
- **FDM（有限差分法）**：产生稀疏矩阵，计算高效；但依赖矩形、圆柱或球形网格，难以建模任意形状几何

**FEM（有限元法）的优势**：
1. 对导体、均匀和非均匀几何**使用统一 formulation**
2. 产生**稀疏矩阵**，内存和 CPU 时间远低于稠密 MOM 矩阵
3. 用三角形网格方便精确地建模任意形状
4. 对任意非均匀轴对称物体具有显著计算优势

**本章结构**：
- §12.2：混合边-节点 formulation（含PML吸收边界）
- §12.3：圆柱形 PML 网格截断
- §12.4：数值验证
- §12.5：带小附属物的 BOR 近似处理方法
- §12.6：结论

---

## 12.2 公式化 | Formulation

### 12.2.1 历史方法回顾

过去的 FEM 公式化方法：

1. **CAP（Coupled Azimuth Potential） formulation**：以角向电场 $E_\phi$ 和角向磁场 $H_\phi$ 为未知量，其他分量由其导数得到。优点是未知量减少约1/3，且无伪模（spurious modes）；缺点是横场分量计算存在不完美抵消问题导致精度下降。

2. **三分量节点 formulation**：以完整电场或磁场为未知量，每个分量用节点标量基函数展开。优点是所有场分量直接得到，避免了 CAP 的不完美抵消问题；缺点是在材料间断面和导体尖角处难以施加正确边界条件，且需 penalty 因子来消除伪模。

**本章方法：混合边-节点 formulation**：
- 横向场分量（$\rho$、$z$ 方向）：使用 **2D边缘（矢量）基函数**
- 角向分量（$\phi$ 方向）：使用 **2D节点（标量）基函数**

该方案自动满足材料间断面的物理边界条件（切向场连续，法向场自然），且无需 penalty 因子即可消除伪模。

### 12.2.2 问题定义

典型问题的计算域如图12.1所示。外部边界布置圆柱形 PML（完全匹配层）。

在 PML 区域，介电参数和磁导率表现为**各向异性张量**：

$$\overline{\bar{\varepsilon}} = \varepsilon_0 \overline{\bar{\Lambda}} \quad \overline{\bar{\mu}} = \mu_0 \overline{\bar{\Lambda}} \tag{12.1}$$

其中 $\overline{\bar{\Lambda}} = \text{diag}(\Lambda_\rho, \Lambda_z, \Lambda_\phi)$，在 PML 之外 $\overline{\bar{\Lambda}} = \overline{\bar{I}}$。

### 12.2.3 变分公式化 | Variational Formulation

从本构参数出发，矢量波动方程为：

$$\nabla \times \left( \overline{\bar{\mu}}^{-1} \nabla \times \mathbf{E} \right) - k^2 \overline{\bar{\varepsilon}} \cdot \mathbf{E} = -j\omega \mathbf{J}_{ext} \tag{12.3}$$

边界条件包括 PEC ($\hat{n} \times \mathbf{E} = 0$)、PMC ($\hat{n} \times \nabla \times \mathbf{E} = 0$) 和阻抗边界条件。

**变分原理**：定义泛函 $\mathcal{F}(\mathbf{E})$，使 $\delta\mathcal{F} = 0$ 等价于求解原边界值问题。

散射问题中，$\mathbf{E} = \mathbf{E}^{inc} + \mathbf{E}^{scat}$，激励为入射平面波。

**利用旋转对称性**：将场展开为 Fourier 模式：

$$E_\rho(\rho,\phi,z) = \sum_{n=-\infty}^{\infty} E_\rho^n(\rho,z) e^{jn\phi} \tag{12.9}$$

对于给定模式编号 $n$，2D切片问题独立求解。

**轴线条件**：沿 $\rho = 0$ 轴，所有场值必须连续。需要特别设计基函数以满足轴线条件（避免 $\rho = 0$ 处的奇异性）：

$$E_\rho^n(\rho=0,z) = \text{finite}, \quad E_z^n(\rho=0,z) = \text{finite} \tag{12.15}$$

### 12.2.4 方程求解 | Solution of the Equations

FEM 方程形式为：

$$[K]\{x\} = \{b\} \tag{12.22}$$

**关键特性**：
- 矩阵是**稀疏**且**对称**的
- **与激励无关**：矩阵分解只需一次，可用于多个激励（如多个入射角、极化方式）
- 使用 **RCM（Reverse Cuthill-McKee）排序**可获得高度带状（banded）矩阵
- **复杂度**：分解 $O(N_b^3)$，求解（前后代）$O(N_b^2)$，其中 $N_b$ 是半带宽

### 12.2.5 远场计算 | Far-Field Calculations

通过**互易定理**从近场值计算远区 RCS：

$$\mathbf{E}^{scat}(\mathbf{r}) = \frac{jk}{4\pi r} e^{-jkr} \hat{r} \times \int_V \mathbf{J}(\mathbf{r}') \times e^{jk\hat{r} \cdot \mathbf{r}'} \, dV' \tag{12.26}$$

对于散射问题，RCS 定义为：

$$\sigma = \lim_{r \to \infty} 4\pi r^2 \frac{|\mathbf{E}^{scat}|^2}{|\mathbf{E}^{inc}|^2} \tag{12.29}$$

---

## 12.3 圆柱形 PML | Cylindrical PML

### 12.3.1 为什么需要 PML

传统 FEM 网格截断方法：
- **Unimoment方法**：使用球谐展开截断，需球形边界，不够灵活
- **近似 ABC**：精度有限，需将边界放得较远，且某些 ABC 需要增大 FEM 矩阵带宽

**PML 的优势**：
1. 任意形状的网格边界（对轴对称问题使用圆柱形）
2. 理论上无反射（$R = 0$ 对所有入射角和频率）
3. 可放置在散射体非常近的位置
4. 通过增加 PML 厚度可**系统性降低反射误差**

### 12.3.2 参数定义 | Parameter Definitions

PML 张量元素为：

$$\Lambda_\rho = \frac{\rho}{\rho + d_\rho}, \quad \Lambda_z = \frac{z_{PML}}{z_{PML} + d_z}, \quad \Lambda_\phi = \frac{\rho + d_\rho}{\rho} \cdot \frac{z_{PML} + d_z}{z_{PML}} \tag{12.30}$$

其中 $d_\rho, d_z, d_\phi$ 是 PML 层厚度，参数 $\beta$ 控制 PML 损耗：

- 较小的 $\beta$：降低空气-PML 界面对比度，减少离散化伪反射
- 较大的 $\beta$：增加 PML 内的波衰减

最优值经验为 $\beta \approx 0.1$（在典型网格设置下）。

### 12.3.3 系统性误差控制

通过固定 PML 厚度，寻找使反射误差最小的 $\beta$ 值。如果精度仍不够，增加 PML 厚度并重复。

验证方法：
- 自由空间 FEM 网格中电流环激励的近场误差
- 导体球后向 RCS 与 Mie 级数解的对比

---

## 12.4 数值结果 | Numerical Results

### 12.4.1 散射问题

**EMCC 基准目标**验证：

1. **金属橄榄体（Ogive）**：长轴长度、锥角等参数定义，与测量值高度吻合
2. **双橄榄体**：两个不同半橄榄体对接形成，与测量值在动态范围底部外均吻合良好
3. **锥-球体（Conesphere）**：球形头部 + 锥形天线阵，含间隙结构，展示处理不连续几何的能力
4. **Luneburg 透镜**：渐变折射率介质球（$\varepsilon_r = 2 - (r/a)^2$），验证 FEM 对非均匀材料的处理能力

**计算资源**：内存和 CPU 时间随目标复杂度增加近似线性增长，表明方法具有良好的可扩展性。

### 12.4.2 辐射问题

**沟槽形喇叭天线（Corrugated Horn Antenna）**：
- 由交替厚度金属垫圈构建的周期结构
- 在 5.3 GHz 至 9.3 GHz 范围内与测量值**极好吻合**
- E面和H面图案的轻微不对称性（天线设计用来产生圆极化）

**Luneburg 透镜作为方向性辐射器**：
- 透镜越大，辐射方向性越强
- 旁瓣电平始终保持在 -20 dB 以下
- 展示场分布如何从点源产生的球面波转换为局部平面波前

---

## 12.5 带附属物的 BOR | BOR with Appendages

### 问题背景

当 BOR 上附加小附属物（如小翼、缝隙、腔体）时，旋转对称性被打破，需要3D方法。

**纯3D方法**：计算成本高（$O(N^2)$ 或 $O(N^{1.5})$ for MLFMA）。

### 混合方法

核心思想：附属物的散射近似叠加到大型 BOR 的散射上：

$$\mathbf{E}^{scat} = \mathbf{E}^{scat}_{BOR} + \mathbf{E}^{scat}_{App} \tag{12.35}$$

**公式**：
1. 使用 FEM 计算附属物在 BOR 存在时的入射场 $\mathbf{E}^{inc}_{App}$
2. 在附属物表面离散积分方程（仅对附属物表面，而非整个目标）
3. 使用几何光学（GO）近似 BOR 的 dyadic Green 函数

**验证**：金属圆柱 + 4个小翼的算例，与 FISC（MOM/MLFMA 商业代码）结果吻合良好。

---

## 12.6 结论 | Conclusion

本章发展的 FEM 方法特点：

1. **混合边-节点 formulation**：
   - 横向分量用边缘矢量基函数（自动满足切向连续性）
   - 角向分量用节点标量基函数
   - 无需 penalty 因子即可消除伪模
   - 便于处理材料间断面和导体尖角边界条件

2. **圆柱形 PML 网格截断**：
   - 允许任意形状（圆柱形）对几乎任何问题几何
   - 可紧靠目标放置（无需远距离截断）
   - 反射误差可通过厚度和 $\beta$ 参数系统性控制

3. **计算效率**：
   - 矩阵稀疏且对称，可使用高效带状求解器
   - 与激励无关的矩阵分解（一次分解，多激励复用）
   - 内存和 CPU 需求近似线性增长

4. **与测量值的高度吻合**：EMCC 基准目标的验证算例展示了方法对电大尺寸雷达目标的实际工程应用能力

5. **可与 MOM 混合**：处理带小附属物的 BOR 问题，兼具效率和精度

# Sadiku《Elements of Electromagnetics》第1章：矢量代数
> **来源：** Matthew N.O. Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **章节来源：** Chapter 1: Vector Algebra, pp.30-57  
> **提取方式：** ✅ 清晰文本PDF直接提取

---

## 1.1 引言 | Introduction

电磁学（EM）是研究静止和运动电荷之间相互作用的学科。它涵盖电场的分析、综合、物理解释和应用。

电磁学是物理学或电气工程的一个分支，研究电现象和磁现象。

**电磁学的应用领域：** 微波、天线、电机、卫星通信、生物电磁学、等离子体、核研究、光纤、电磁干扰与兼容性、机电能量转换、雷达气象学、遥感等。

> **物理医学应用：** 电磁能量（短波或微波）用于加热深层组织、刺激特定生理反应。
> **感应加热：** 熔炼、锻造、退火、表面硬化、焊接。
> **介质加热：** 用于塑料薄膜的焊接与密封。

**常见电磁器件：** 变压器、继电器、收音机/电视、电话、电机、传输线、波导、天线、光纤、雷达、激光器。

---

## 1.2 Maxwell 方程组预览 | Maxwell's Equations Preview

本书所研究的电磁现象可以用 **Maxwell 方程组** 概括：

$$\nabla \cdot \mathbf{D} = \rho_v \quad \text{(1.1) 高斯定律}$$

$$\nabla \cdot \mathbf{B} = 0 \quad \text{(1.2) 磁通连续性方程}$$

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \quad \text{(1.3) Faraday电磁感应定律}$$

$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t} \quad \text{(1.4) Ampère-麦克斯韦定律}$$

其中：
- $\nabla$：向量微分算子（nabla 算子）
- $\mathbf{D}$：电通量密度（electric flux density），单位 $\mathrm{C/m^2}$
- $\mathbf{B}$：磁通量密度（magnetic flux density），单位 $\mathrm{T}$（特斯拉）
- $\mathbf{E}$：电场强度（electric field intensity），单位 $\mathrm{V/m}$
- $\mathbf{H}$：磁场强度（magnetic field intensity），单位 $\mathrm{A/m}$
- $\rho_v$：体电荷密度（volume charge density），单位 $\mathrm{C/m^3}$
- $\mathbf{J}$：电流密度（current density），单位 $\mathrm{A/m^2}$

---

## 1.3 标量与矢量 | Scalars and Vectors

**标量（Scalar）：** 仅由大小完全确定的物理量。例：时间、质量、距离、温度、熵、电势。

**矢量（Vector）：** 既有大小的物理量。例：速度、力、动量、加速度、位移、电场强度。

> **物理意义：** 电磁学中，$\mathbf{E}$、$\mathbf{H}$、$\mathbf{B}$、$\mathbf{D}$、$\mathbf{J}$ 都是矢量，准确把握方向是理解电磁场的第一步。

**场（Field）：** 在某区域内指定每点物理量的函数。

$$\text{标量场：} T(x,y,z) \quad \text{例：温度分布、电势}$$

$$\text{矢量场：} \mathbf{E}(x,y,z) \quad \text{例：电场、磁场、风速场}$$

---

## 1.4 单位矢量 | Unit Vector

矢量 $\mathbf{A}$ 的大小写作 $|\mathbf{A}|$ 或 $A$，其单位矢量 $\hat{\mathbf{a}}_A$ 定义为：

$$\hat{\mathbf{a}}_A = \frac{\mathbf{A}}{|\mathbf{A}|}$$

直角坐标系中的三个单位矢量：

$$\hat{\mathbf{x}} \quad \hat{\mathbf{y}} \quad \hat{\mathbf{z}}$$

---

## 1.5 矢量代数 | Vector Algebra

### 矢量加法与减法 | Addition and Subtraction

$$\mathbf{A} \pm \mathbf{B} = (A_x \pm B_x)\hat{\mathbf{x}} + (A_y \pm B_y)\hat{\mathbf{y}} + (A_z \pm B_z)\hat{\mathbf{z}}$$

### 标量乘法 | Scalar Multiplication

$$k\mathbf{A} = (kA_x)\hat{\mathbf{x}} + (kA_y)\hat{\mathbf{y}} + (kA_z)\hat{\mathbf{z}}$$

---

## 1.6 位置矢量与距离矢量 | Position and Distance Vectors

**位置矢量（Position vector）** $\mathbf{r}_P$：从原点指向点 $P$ 的矢量：

$$\mathbf{r}_P = x_P\hat{\mathbf{x}} + y_P\hat{\mathbf{y}} + z_P\hat{\mathbf{z}}$$

**距离矢量（Distance/Separation vector）** $\mathbf{r}_{PQ}$：从点 $P$ 指向点 $Q$ 的位移：

$$\mathbf{r}_{PQ} = \mathbf{r}_Q - \mathbf{r}_P = (x_Q - x_P)\hat{\mathbf{x}} + (y_Q - y_P)\hat{\mathbf{y}} + (z_Q - z_P)\hat{\mathbf{z}}$$

**两点间距离：**

$$d = |\mathbf{r}_{PQ}| = \sqrt{(x_Q - x_P)^2 + (y_Q - y_P)^2 + (z_Q - z_P)^2}$$

---

## 1.7 矢量乘法 | Vector Multiplication

### A. 点积（标量积）| Dot Product (Scalar Product)

$$\mathbf{A} \cdot \mathbf{B} = |\mathbf{A}||\mathbf{B}|\cos\theta_{AB}$$

几何意义：$\mathbf{A}$ 在 $\mathbf{B}$ 方向上的投影乘以 $|\mathbf{B}|$。

**物理应用：**
- 功：$W = \mathbf{F} \cdot \mathbf{d}$
- 电通量：$\Psi = \mathbf{D} \cdot \mathbf{S}$
- 功率密度：$P = \mathbf{E} \cdot \mathbf{J}$

### B. 叉积（矢量积）| Cross Product (Vector Product)

$$\mathbf{A} \times \mathbf{B} = |\mathbf{A}||\mathbf{B}|\sin\theta_{AB}\,\hat{\mathbf{n}}$$

其中 $\hat{\mathbf{n}}$ 由右手定则确定。

**物理应用：**
- 洛伦兹力：$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})$
- 力矩：$\boldsymbol{\tau} = \mathbf{r} \times \mathbf{F}$
- 角动量：$\mathbf{L} = \mathbf{r} \times \mathbf{p}$

### C. 标量三重积 | Scalar Triple Product

$$\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = \begin{vmatrix} A_x & A_y & A_z \\ B_x & B_y & B_z \\ C_x & C_y & C_z \end{vmatrix}$$

几何意义：三个矢量构成的平行六面体的**体积**。

### D. 矢量三重积 | Vector Triple Product

$$\mathbf{A} \times (\mathbf{B} \times \mathbf{C}) = \mathbf{B}(\mathbf{A} \cdot \mathbf{C}) - \mathbf{C}(\mathbf{A} \cdot \mathbf{B})$$

> **记忆法：** "BAC - CAB"

---

## 1.8 矢量分量 | Components of a Vector

**标量分量（Scalar projection）：**

$$A_B = A\cos\theta_{AB} = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{B}|}$$

**矢量分量（Vector projection）：**

$$\mathbf{A}_B = A_B \hat{\mathbf{B}} = \frac{\mathbf{A} \cdot \mathbf{B}}{|\mathbf{B}|^2}\mathbf{B}$$

---

## 本章要点总结 | Key Takeaways

1. **Maxwell 方程组**是电磁学的核心，四个方程分别对应：电荷产生散度、不存在磁单极子、Faraday感应、Ampère-麦克斯韦位移电流。

2. **矢量运算**（点积、叉积、三重积）是描述场的叠加、能量流、力矩的核心工具。

3. **右手坐标系**（$\hat{\mathbf{x}} \times \hat{\mathbf{y}} = \hat{\mathbf{z}}$）是本书统一采用的约定。

4. **坐标系选择**：球坐标系天然适合处理球面波辐射问题，柱坐标系适合柱状结构。

---

## 习题精选 | Selected Problems

> **注：** 以下为例题精要，完整习题见原书 pp.24-57。

**例题 1.1：** 已知 $\mathbf{A} = 10\hat{\mathbf{x}} - 4\hat{\mathbf{y}} + 6\hat{\mathbf{z}}$，$\mathbf{B} = 2\hat{\mathbf{x}} + \hat{\mathbf{y}}$，求 $3\mathbf{A} - 2\mathbf{B}$。

**解：**
$$3\mathbf{A} - 2\mathbf{B} = [30-4]\hat{\mathbf{x}} + [-12-2]\hat{\mathbf{y}} + [18-0]\hat{\mathbf{z}} = 28\hat{\mathbf{x}} - 14\hat{\mathbf{y}} + 18\hat{\mathbf{z}}$$

$$|3\mathbf{A} - 2\mathbf{B}| = \sqrt{28^2 + (-14)^2 + 18^2} = \sqrt{784 + 196 + 324} = \sqrt{1304} = 36.1$$

**例题 1.6（点积与叉积）：** 验证 $\mathbf{A} = 3\hat{\mathbf{x}} + 4\hat{\mathbf{y}} + \hat{\mathbf{z}}$ 与 $\mathbf{B} = 2\hat{\mathbf{y}} - 5\hat{\mathbf{z}}$ 的夹角。

**解：**
$$\mathbf{A} \cdot \mathbf{B} = 0 + 8 - 5 = 3$$

$$|\mathbf{A}| = \sqrt{9+16+1} = \sqrt{26}, \quad |\mathbf{B}| = \sqrt{0+4+25} = \sqrt{29}$$

$$\cos\theta_{AB} = \frac{3}{\sqrt{26}\sqrt{29}} = 0.1092 \Rightarrow \theta_{AB} = 83.7°$$
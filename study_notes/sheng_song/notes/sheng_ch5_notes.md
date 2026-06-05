---
title: "Ch5: Hybrid Methods"
book: "Sheng & Song, Essentials of Computational Electromagnetics (2012)"
chapter: 5
pages: "248-285"
weight: 5
topics:
  - PO-FEM hybrid
  - PO-MoM hybrid
  - FE-BI-MLFMA
  - CFIE formulations (TENH, NETH, TETH, NENH)
  - Mode-matching hybrid
  - SBR (Shooting-Bouncing Ray)
notes_version: "1.1"
---

# Chapter 5: Hybrid Methods | 混合方法

> **中英双语版**

Numerical methods for EM computation are roughly categorized into:
电磁计算方法大致分为：

1. **High-frequency asymptotic methods | 高频渐进方法**: PO, GO, GTD, PTD, SBR
2. **Full-wave numerical methods | 全波数值方法**: MoM, FEM, FDTD

Each method has distinct advantages and disadvantages. Hybrid methods combine different methods for accurate and efficient results.
每种方法各有优缺点。混合方法结合不同方法以求精确高效的结果。

Two types of hybridization | 两类混合：
1. **Domain decomposition (equivalence principle)**: Partition domain, apply different methods to each subregion. Example: **FE-BI**.
   **域分解**：划分域，对各子区域应用不同方法。示例：FE-BI。
2. **Dimension separation (mode theory)**: Different methods for different dimensions. Example: **Mode-matching**.
   **维度分离**：对不同维度应用不同方法。示例：模式匹配。

---

## 5.1 Hybrid High-Frequency Asymptotic + Full-Wave Methods | 高频渐进 + 全波混合方法

### 5.1.1 Hybrid PO-FEM Method (Cavity Problem) | PO-FEM 混合法（腔体问题）

**Problem | 问题**: Electrically large PEC scatterer with a dielectric-filled cavity. PEC body size: tens to hundreds of wavelengths; cavity: a few wavelengths.
电大尺寸 PEC 散射体含介质填充腔体。PEC 体尺寸几十到几百波长；腔体仅几个波长。

#### 5.1.1.1 Idea | 思路

Partition using the **equivalence principle**:
使用**等效原理**划分：

1. **Exterior region**: Replace cavity with PEC. Apply **PO method** (high-frequency asymptotic).
   **外部区域**：用 PEC 替代腔体。应用 **PO 方法**（高频渐进）。
2. **Interior region (cavity)**: Apply **FEM** for accurate solution.
   **内部区域（腔体）**：应用 **FEM** 求精确解。

#### 5.1.1.2 PO Solution in Exterior Region | 外部区域的 PO 解

The total scattering field outside the cavity:
腔体外总散射场：

$$
\mathbf{H} = \mathbf{H}_{po} + \mathbf{H}_m \tag{5.6}
$$

**PO magnetic field**: $\mathbf{H}_{po} = -\int_S \mathbf{J}_{po} \times \nabla G_0 \, dS'$, where
$$
\mathbf{J}_{po} = \begin{cases} 2\hat{n} \times \mathbf{H}^i(\mathbf{r}) & \mathbf{r} \in S_{\text{slit}} \\ 0 & \mathbf{r} \in S_{\text{dark}} \end{cases} \tag{5.2}
$$

**Scattering from equivalent magnetic current** $\mathbf{M}$ uses the half-space dyadic Green's function (5.4).
等效磁流的散射使用半空间并矢格林函数。

#### 5.1.1.3 FEM Solution Inside the Cavity | 腔体内 FEM 解

The variational problem inside the cavity (5.7) is discretized with tetrahedral edge elements. The exterior field (5.6) is substituted in, yielding the sparse linear system (5.10) with matrix elements (5.11) and RHS (5.12).
腔体内变分问题用四面体边元离散。代入外部场得到稀疏线性系统。

#### 5.1.1.4 Far-Field Calculation via Reciprocity | 通过互易原理计算远场

Since the exact dyadic Green's function for the PEC body with cavity is unavailable, the **reciprocity principle** is used to compute far-zone scattering:
由于无法获得含腔体 PEC 体的精确并矢格林函数，使用**互易原理**计算远区散射：

$$
\mathbf{E}_{sc}^{y,f} = \frac{jk_0 Z_0 e^{-jk_0 r}}{4\pi r} \int_{S_a} \mathbf{M} \cdot \mathbf{H}_{po}^{v,h} \, dS \tag{5.15}
$$

### 5.1.2 Hybrid PO-MoM Method (Protrusion Problem) | PO-MoM 混合法（凸起问题）

**Problem**: Electrically large PEC object with a small protrusion (compared to the body).
电大尺寸 PEC 目标上有一个小的凸起。

The smooth body has known PO solution. The protrusion introduces an **equivalent electric current** $\mathbf{J}$ solved by MoM.
光滑体有已知 PO 解。凸起引入**等效电流** $\mathbf{J}$，用 MoM 求解。

$$
\mathbf{E}_s - jk_0 \int_{S_p} \overline{\overline{G}} \cdot \mathbf{J} \, dS' \Big|_{\text{tangential}} = 0 \tag{5.16}
$$

Far-zone scattering via reciprocity: $\mathbf{E}_{sc}^{y,f} = -\frac{jk_0 e^{-jk_0 r}}{4\pi r} \int_{S_p} \mathbf{J} \cdot \mathbf{E}_{po}^{v,h} \, dS$ (5.17).
远区散射通过互易原理计算。

---

## 5.2 Hybrid Full-Wave Numerical Methods | 全波数值混合方法

### 5.2.1 Hybrid FE-BI-MLFMA | 有限元-边界积分-MLFMA 混合

**Problem**: Scattering by a coated metallic object (stealth aircraft design).
涂覆金属目标的散射（隐身飞机设计）。

#### 5.2.1.1 Idea | 思路

Partition using the **equivalence principle**:
使用等效原理划分：

1. **Interior** (between metallic surface $S_i$ and coating surface $S_e$): **FEM** (tetrahedral mesh, edge elements)
   **内部**（金属面 $S_i$ 和涂层外表面 $S_e$ 之间）：**FEM**
2. **Exterior** (free space outside $S_e$): **MoM** (boundary integral on $S_e$)
   **外部**（$S_e$ 外自由空间）：**MoM**
3. **Connection**: Huygens' equivalence principle links FEM and MoM via surface unknowns on $S_e$
   **连接**：惠更斯等效原理通过 $S_e$ 上的面未知量连接 FEM 和 MoM

Called **FE-BI (Finite Element–Boundary Integral)**.
称为 **FE-BI（有限元-边界积分）**。

#### 5.2.1.2 Formulation | 公式

FEM functional (interior region $V$):
FEM 泛函（内部区域 $V$）：

$$
F(\mathbf{E}) = \frac{1}{2} \int_V \left[ \frac{1}{\mu_r} (\nabla \times \mathbf{E}) \cdot (\nabla \times \mathbf{E}^*) - k_0^2 \epsilon_r \mathbf{E} \cdot \mathbf{E}^* \right] dV + jk_0 \int_{S_0} \mathbf{E} \times (\overline{\overline{I}} - \hat{n}\hat{n}) \cdot \mathbf{H}^* \, dS \tag{5.18}
$$

Discretization yields the combined system:
离散化得到组合系统：

$$
\begin{pmatrix} \mathbf{K}_{II} & \mathbf{K}_{IS} & 0 \\ \mathbf{K}_{SI} & \mathbf{K}_{SS} & \mathbf{B} \\ 0 & \mathbf{P} & \mathbf{Q} \end{pmatrix} \begin{pmatrix} \mathbf{E}_I \\ \mathbf{E}_S \\ -\mathbf{H}_S \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ \mathbf{b} \end{pmatrix} \tag{5.29}
$$

where $\mathbf{P}\mathbf{E}_S + \mathbf{Q}(-\mathbf{H}_S) = \mathbf{b}$ is the **Combined Field Integral Equation (CFIE)**.
其中 $\mathbf{P}\mathbf{E}_S + \mathbf{Q}(-\mathbf{H}_S) = \mathbf{b}$ 是**组合场积分方程**。

#### CFIE Formulation Comparison | CFIE 公式对比

| Scheme | Testing | Interior Resonance |
|--------|---------|-------------------|
| TETH | EFIE: RWG, MFIE: RWG | Suffers |
| **TENH** | EFIE: RWG, MFIE: $\hat{n} \times$ RWG | **Free** |
| NETH | EFIE: $\hat{n} \times$ RWG, MFIE: RWG | Poor convergence |
| NENH | EFIE: $\hat{n} \times$ RWG, MFIE: $\hat{n} \times$ RWG | Suffers |

The **TENH** scheme has the best condition number and is recommended for FE-BI-MLFMA.
**TENH** 方案条件数最佳，推荐用于 FE-BI-MLFMA。

#### 5.2.1.3 Solution and Complexity | 求解与复杂度

Using **CG iteration** with **MLFMA** acceleration:
使用 **CG 迭代** + **MLFMA** 加速：

- **Memory**: $O(N_v + N_s \lg N_s)$
- **Per iteration cost**: $O(N_v + N_s \lg N_s)$
- **Preconditioning**: LU decomposition of FEM coefficient matrix $\mathbf{K} = \mathbf{L} \mathbf{U}$ (5.35) to accelerate convergence.
  预处理：FEM 系数矩阵的 LU 分解以加速收敛。

#### 5.2.1.4 Numerical Results | 数值结果

Examples include coated spheres verified against Mie series — excellent agreement with high efficiency.
涂覆球体示例经 Mie 级数验证——高度吻合，效率高。

---

## 5.3 Straight-Line Method (Mode Matching) | 直线法（模式匹配）

For waveguide discontinuities and cascading problems. Separates dimensions:
用于波导不连续和级联问题。维度分离：

- **Transverse direction**: Galerkin method (MoM or FEM) — solves for modal field patterns
  **横向**：Galerkin 方法——求解模式场分布
- **Propagation direction**: Analytical propagation of modal amplitudes using transmission-line theory
  **传播方向**：用传输线理论解析传播模态幅度

This hybrids **mode-matching** (analytical in propagation) and **numerical** (Galerkin in transverse).
混合了**模式匹配**（传播方向解析）和**数值法**（横向 Galerkin）。

---

## Key Equations Summary | 关键方程总结

| Equation | Description | 说明 |
|----------|-------------|------|
| (5.1) | PO magnetic field | PO 磁场 |
| (5.2) | PO surface current | PO 面电流 |
| (5.6) | Total exterior field | 外部总场 |
| (5.7) | FEM functional (cavity) | 腔体 FEM 泛函 |
| (5.10) | FEM linear system | FEM 线性系统 |
| (5.16) | IE for protrusion current | 凸起电流积分方程 |
| (5.18) | FE-BI functional | FE-BI 泛函 |
| (5.29) | Combined FE-BI-CFIE matrix | FE-BI-CFIE 组合矩阵 |
| (5.35) | LU preconditioning | LU 预处理 |

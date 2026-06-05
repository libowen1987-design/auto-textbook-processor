# Chew, Jin, Michielssen, Song — Fast and Efficient Algorithms in CEM (2001)

Artech House, ISBN 1-58053-152-0

> MLFMA 标准教材。结合 Harrington《Field Computation by Moment Methods》循序渐进。

---

## Part I: 积分方程方法 (Integral Equation Methods)

### 1.1 基本框架

- 时谐场 (time-harmonic, $e^{j\omega t}$) → Helmholtz 方程
- 表面积分方程 (SIE) 求解散射/辐射问题
- 核心: **等效原理** — 表面未知电流/磁流替代物体, 通过边界条件建立积分方程

### 1.2 EFIE (电场积分方程)

$$
\hat{n} \times \left[ E^{\text{inc}}(\mathbf{r}) + E^{\text{scat}}(\mathbf{r}) \right] = 0 \quad \mathbf{r} \in S
$$

其中散射场由表面电流 $\mathbf{J}$ 产生:

$$
\mathbf{E}^{\text{scat}}(\mathbf{r}) = -j\omega\mu \iint_S \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS' + \frac{1}{j\omega\epsilon} \nabla \iint_S \nabla' \cdot \mathbf{J}(\mathbf{r}') G(\mathbf{r}, \mathbf{r}') \, dS'
$$

- 适用于开/闭表面, 薄导线
- 对闭合导体有内谐振问题 (RWG 基函数仍需关注)
- 弱化形式: Galerkin 测试 → 对称系统

### 1.3 MFIE (磁流积分方程)

$$
\frac{1}{2} \hat{n} \times \mathbf{J}(\mathbf{r}) - \hat{n} \times \left[ \hat{n} \times \text{PV} \iint_S \mathbf{J}(\mathbf{r}') \times \nabla' G(\mathbf{r}, \mathbf{r}') \, dS' \right] = \hat{n} \times \mathbf{H}^{\text{inc}}(\mathbf{r})
$$

- 仅适用于闭合导体 (PEC)
- 第二类 Fredholm 方程 → 条件数低于 EFIE
- 需主值积分 (PV) 处理奇异性

### 1.4 CFIE (组合场积分方程)

$$
\text{CFIE} = \alpha \cdot \text{EFIE} + (1-\alpha) \cdot \eta \cdot \text{MFIE}
$$

- $\alpha \in [0, 1]$, 通常取 $\alpha = 0.5$
- 消除内谐振 → 唯一解
- 条件数优于 EFIE, 适合迭代求解

### 1.5 矩量法 (MoM)

RWG 基函数 (三角形剖分):

$$
\mathbf{f}_n(\mathbf{r}) = \begin{cases}
\frac{l_n}{2A_n^+} (\mathbf{r} - \mathbf{r}_n^+), & \mathbf{r} \in T_n^+ \\
\frac{l_n}{2A_n^-} (\mathbf{r}_n^- - \mathbf{r}), & \mathbf{r} \in T_n^-
\end{cases}
$$

阻抗矩阵:

$$
Z_{mn} = j\omega\mu \iint_{S_m} \iint_{S_n} \mathbf{f}_m(\mathbf{r}) \cdot \mathbf{f}_n(\mathbf{r}') G(\mathbf{r},\mathbf{r}') \, dS' \, dS \\
- \frac{1}{j\omega\epsilon} \iint_{S_m} \iint_{S_n} \nabla\cdot\mathbf{f}_m(\mathbf{r}) \nabla'\cdot\mathbf{f}_n(\mathbf{r}') G(\mathbf{r},\mathbf{r}') \, dS' \, dS
$$

**复杂度**: $O(N^2)$ 填充 + $O(N^3)$ 直接求解 — 大问题不可行。

---

## Part II: 快速多极子方法 (FMM)

### 2.1 核心思想

将 MoM 矩阵-向量乘分解为:
- **近场部分**: 直接计算 (小矩阵, 稀疏)
- **远场部分**: 通过多极展开聚合 → 转移 → 配置

### 2.2 加法定理 (Addition Theorem)

球谐函数展开自由空间格林函数:

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jk|\mathbf{r} - \mathbf{r}'|}}{4\pi|\mathbf{r} - \mathbf{r}'|}
= -jk \sum_{l=0}^{\infty} \sum_{m=-l}^{l} h_l^{(2)}(kr) j_l(kr') Y_{lm}(\hat{\mathbf{r}}) Y_{lm}^*(\hat{\mathbf{r}}')
$$

其中 $h_l^{(2)}$ 为第二类球汉克尔函数, $j_l$ 为球贝塞尔函数。

### 2.3 多极展开

当 $|\mathbf{d}| < |\mathbf{r}_m - \mathbf{r}_{k'}|$ 时:

$$
G(\mathbf{r}_{kj}, \mathbf{r}_{k'j'}) \approx \frac{-jk}{4\pi} \iint e^{-j\mathbf{k} \cdot (\mathbf{r}_{kj} - \mathbf{X}_{k'})} T_L(\mathbf{k} \cdot \hat{\mathbf{r}}_{kk'}) e^{j\mathbf{k} \cdot (\mathbf{r}_{k'j'} - \mathbf{X}_{k'})} d^2\hat{\mathbf{k}}
$$

其中 **平移算子**:

$$
T_L(\mathbf{k} \cdot \hat{\mathbf{r}}_{kk'}) = \sum_{l=0}^{L} (-j)^l (2l+1) h_l^{(2)}(k r_{kk'}) P_l(\hat{\mathbf{k}} \cdot \hat{\mathbf{r}}_{kk'})
$$

### 2.4 三阶段流程 (FMM 矩阵-向量乘)

对于基函数分组后的相互作用:

1. **聚合 (Aggregation)**:
   $$
   V_{k'}(\hat{\mathbf{k}}_p) = \sum_{j'} w_j' e^{j\mathbf{k}_p \cdot (\mathbf{r}_{j'} - \mathbf{X}_{k'})}
   $$
   将组内源点贡献 → 组中心的多极表示

2. **转移 (Transfer)**:
   $$
   V_k(\hat{\mathbf{k}}_p) = \sum_{k'} T_L(\mathbf{k}_p \cdot \hat{\mathbf{r}}_{kk'}) V_{k'}(\hat{\mathbf{k}}_p)
   $$
   远场组之间的平移

3. **配置 (Configuration/Disaggregation)**:
   $$
   V_i^{\text{field}} \approx \sum_{p} w_i e^{-j\mathbf{k}_p \cdot (\mathbf{r}_i - \mathbf{X}_k)} V_k(\hat{\mathbf{k}}_p)
   $$
   从接收组中心 → 各测试点

### 2.5 FMM 复杂度

- 分组数: $M \propto \sqrt{N}$
- 多极模式数: $L \propto \sqrt{N}$
- 总复杂度: $O(N^{1.5})$

---

## Part III: 多层快速多极子法 (MLFMA)

### 3.1 树形结构

- **八叉树 (Octree)**: 3D 空间递归二分
- 根节点: 包围盒 (bounding box) 包含整个物体
- 叶节点: 边长 ~0.25λ, 每组约 10-100 个未知数
- 层数: $O(\log N)$

### 3.2 多层级策略

```
Level (fine)   l = L   叶节点, 小分组, 少数基函数
   ↑
   | 向上遍历: 子节点聚合 → 父节点 (upsampling + interpolation)
   |
Level (coarse) l = 0   根节点, 全物体包围盒
```

**近场**: 最细层相邻组直接计算 (稀疏矩阵)
**远场**: 从粗到细的树状遍历

### 3.3 插值和反插值 (Interpolation & Anterpolation)

层间操作:
- **向上 (聚合方向)**: 细层模式数多 → 粗层模式数少
  - 使用插值 (interpolation): $L_{l-1} < L_l$, 插值核由球谐展开的截断决定
- **向下 (配置方向)**: 粗层 → 细层
  - 使用反插值/滤波 (anterpolation/filtering)
- 模式数 (每层): $L_l \propto k D_l$, $D_l$ 为层 $l$ 的分组尺寸

### 3.4 平移算子的分层计算

- 同一父节点下的兄弟组 → 用该层的平移算子
- 不同父节点 → 向上聚合到公共父层再平移
- 避免重复计算: 平移矩阵仅在不同层有不同截断阶数

### 3.5 复杂度: $O(N \log N)$

| 步骤 | 复杂度 |
|------|--------|
| 近场填充 | $O(N)$ |
| 聚合 (每层) | $O(N_l)$ |
| 转移 (每层) | $O(L_l M_l^2) = O(N_l)$ |
| 配置 (每层) | $O(N_l)$ |
| 总迭代每步 | $O(N \log N)$ |

---

## Part IV: 预条件与迭代求解

### 4.1 迭代求解器

**CG (共轭梯度法)**:
- 仅适用于对称正定矩阵
- EFIE 非正定 → 不适用
- CFIE 对称但非正定

**GMRES (广义最小残差法)**:
- 通用 Krylov 子空间方法
- 适用于非对称、非正定系统
- 每次迭代存储 $m$ 个 Arnoldi 向量
- 重启机制 (restart): GMRES(m)

**BiCGSTAB**:
- 稳定双共轭梯度法, 存储需求小
- 收敛特性不如 GMRES 稳定

### 4.2 收敛性

- EFIE: 条件数 $\kappa \propto O(\sqrt{N})$, 迭代次数随 $N$ 增长
- MFIE: $\kappa$ 较小, 收敛快
- CFIE: 介于两者之间, 无内谐振

### 4.3 预条件技术

**近场预条件 (Near-field preconditioner)**:
- 仅使用近场矩阵 $Z_{\text{near}}$ 构造预条件子
- ILU(0)/ILUT 分解
- SPAI (Sparse Approximate Inverse)

**块对角预条件**:
- 每块 = 一个叶节点组的近场自作用
- 并行友好

**多层预条件**:
- 利用 MLFMA 的层级结构
- 从粗网格到细网格校正

### 4.4 预条件效果

| 问题 | 无预条件 | ILU(0) | 块对角 |
|------|---------|--------|--------|
| 简单形状 | 上百次迭代 | 数十次 | 数十次 |
| 细长/复杂 | 不收敛 | 可收敛 | 有限改善 |

---

## Part V: 大规模应用

### 5.1 雷达散射截面 (RCS)

- 典型流程: SIE → MoM/MLEMA → RCS 计算
- 双站 RCS: $\sigma(\theta, \phi) = \lim_{r\to\infty} 4\pi r^2 \frac{|E^{\text{scat}}|^2}{|E^{\text{inc}}|^2}$
- 单站 RCS (单基地): 多个入射角, 需多次求解

### 5.2 天线阵列

- 阵列因子 × 单元方向图 (耦合存在时需全波分析)
- MLFMA 加速阵列分析: 每个阵元 → 一个分组
- 自适应 vs 预计算阵列格林函数

### 5.3 典型性能

| 问题规模 | MoM (直接) | MLFMA (迭代, 200 iter) |
|----------|-----------|----------------------|
| N=10⁴ | ~100 GB, 数小时 | ~0.5 GB, 数分钟 |
| N=10⁵ | 不可行 | ~5 GB, ~1h |
| N=10⁶ | 不可行 | ~50 GB, ~10h |

### 5.4 工程注意事项

- 截断阶数 $L$: $L = kd + \beta (kd)^{1/3}$, $\beta \approx 2 \sim 10$
- 角向采样: $K = 2(L+1)^2$ (3D)
- 近场半径: 叶节点相邻组直接计算
- 精度控制: $\varepsilon \sim 10^{-3}$ 对大多数工程问题足够

---

## 总结: 从 MoM 到 MLFMA 的演进

```
MoM (O(N³))              直接填充 Z, LU 分解         ← 小规模
  ↓
FMM (O(N¹·⁵))            分组 + 多极展开加速 MV       ← 中等规模
  ↓
MLFMA (O(N log N))       树形 + 插值多层级            ← 大规模
  ↓
MLFMA + 预条件           加速迭代收敛                 ← 极端规模
```

---

## 参考文献

- Chew et al., *Fast and Efficient Algorithms in CEM*, Artech House, 2001
- Harrington, *Field Computation by Moment Methods*, IEEE Press, 1993
- Song, Lu, Chew, "Multilevel Fast Multipole Algorithm for Electromagnetic Scattering by Large Complex Objects," *IEEE Trans. Antennas Propagat.*, 1997
- Greengard & Rokhlin, "A Fast Algorithm for Particle Simulations," *J. Comput. Phys.*, 1987
- Saad, *Iterative Methods for Sparse Linear Systems*, SIAM, 2003

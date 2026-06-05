---
title: "Chapter 3 — Electromagnetic Theorems and Principles"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Uniqueness theorem
  - Image theory (PEC/PMC ground planes)
  - Surface equivalence principle
  - Induction theorem
  - Reciprocity theorem
  - Duality principle
  - Aperture radiation & Babinet's principle
---

# Chapter 3: Electromagnetic Theorems and Principles | 第三章：电磁定理与原理

> **中英双语版**

## 3.1 Uniqueness Theorem | 唯一性定理

The field in a volume $V$ with given sources is **unique** if either the tangential $\mathbf{E}$ or tangential $\mathbf{H}$ (or a mix) is specified on the bounding surface $S$ / 体积 $V$ 中具有给定源的场在以下条件下**唯一**：在边界 $S$ 上指定了切向 $\mathbf{E}$ 或切向 $\mathbf{H}$（或两者的组合）。

**Proof (time-harmonic, lossy medium) / 证明（时谐、有损耗媒质）:** 假设两个解，相减，在 $V$ 上积分 $\nabla \cdot (\delta\mathbf{E} \times \delta\mathbf{H}^*)$：

$$
\oiint_S (\delta\mathbf{E} \times \delta\mathbf{H}^*) \cdot d\mathbf{S} = \iiint_V [ -j\omega\mu|\delta\mathbf{H}|^2 + (j\omega\epsilon^* - \sigma)|\delta\mathbf{E}|^2 ] dV
$$

当 $\hat{n} \times \mathbf{E}$ 或 $\hat{n} \times \mathbf{H}$ 被指定时面积分为零 → 对于有损耗媒质 $\delta\mathbf{E} = \delta\mathbf{H} = 0$。

**Three sufficient conditions / 三个充分条件:**
1. $\hat{n} \times \mathbf{E}$ 在 $S$ 上处处指定
2. $\hat{n} \times \mathbf{H}$ 在 $S$ 上处处指定
3. $\hat{n} \times \mathbf{E}$ 在一部分，$\hat{n} \times \mathbf{H}$ 在其余部分

---

## 3.2 Image Theory | 镜像原理

Replace a PEC/PMC ground plane with equivalent image sources in free space / 用自由空间中的等效镜像源替换PEC/PMC接地平面。

| Dipole Type / 偶极子类型 | Above PEC / PEC上方 | Above PMC / PMC上方 |
|:-----------|:----------|:----------|
| 垂直电偶极子 $\hat{z}Il$ | 同向 $\hat{z}Il$ | 反向 $-\hat{z}Il$ |
| 水平电偶极子 $\hat{x}Il$ | 反向 $-\hat{x}Il$ | 同向 $\hat{x}Il$ |
| 垂直磁偶极子 $\hat{z}K$ | 反向 $-\hat{z}K$ | 同向 $\hat{z}K$ |
| 水平磁偶极子 $\hat{x}K$ | 同向 $\hat{x}K$ | 反向 $-\hat{x}K$ |

For an arbitrary current above PEC ground plane / 对于PEC接地平面上方的任意电流：

$$
\mathbf{J}_{\text{im}}(\mathbf{r}) = 2\hat{z}\hat{z}\cdot\mathbf{J}(\mathbf{r}_i) - \mathbf{J}(\mathbf{r}_i), \quad \mathbf{r}_i = x\hat{x} + y\hat{y} - z\hat{z}
$$

---

## 3.3 Surface Equivalence Principle | 表面等效原理

Replace actual sources on a closed surface $S$ with **equivalent surface currents** / 用**等效面电流**替换封闭曲面 $S$ 上的实际源：

$$
\mathbf{J}_s = \hat{n} \times \mathbf{H}, \quad \mathbf{M}_s = -\hat{n} \times \mathbf{E}
$$

These produce the same fields outside $S$ (zero fields inside — Love's equivalence) / 这些在 $S$ 外部产生相同场（内部为零场——乐甫等效）。

**核心作用**：所有积分方程方法（矩量法、有限元–边界元法）的基础。

---

## 3.4 Induction Theorem | 感应定理

Special case of equivalence: a PEC scatterer is replaced by induced surface currents equal to $2\hat{n} \times \mathbf{H}^{\text{inc}}$ in the illuminated region (physical optics approximation) / 等效原理的特例：PEC散射体被照亮区域的感应面电流等于 $2\hat{n} \times \mathbf{H}^{\text{inc}}$（物理光学近似）。

---

## 3.5 Reciprocity Theorem | 互易定理

For two sets of sources $(\mathbf{J}_1, \mathbf{M}_1)$ and $(\mathbf{J}_2, \mathbf{M}_2)$ producing $(\mathbf{E}_1, \mathbf{H}_1)$ and $(\mathbf{E}_2, \mathbf{H}_2)$ in the same medium / 两组源 $(\mathbf{J}_1, \mathbf{M}_1)$ 和 $(\mathbf{J}_2, \mathbf{M}_2)$ 在同一媒质中产生 $(\mathbf{E}_1, \mathbf{H}_1)$ 和 $(\mathbf{E}_2, \mathbf{H}_2)$：

$$
\iiint_V (\mathbf{E}_1 \cdot \mathbf{J}_2 - \mathbf{H}_1 \cdot \mathbf{M}_2) dV = \iiint_V (\mathbf{E}_2 \cdot \mathbf{J}_1 - \mathbf{H}_2 \cdot \mathbf{M}_1) dV
$$

For isotropic media / 各向同性媒质：天线的接收和发射方向图相同。

**Example 3.3 / 例3.3:** 垂直接收天线拾取的信号与发射垂直天线相同。

**Example 3.4 / 例3.4:** 波导内的小回路——回路信号 $\propto$ 回路所在位置的磁场。

---

## 3.6 Duality Principle | 对偶原理

Maxwell's equations are symmetric under the exchange / 麦克斯韦方程组在以下交换下对称：

$$
\mathbf{E} \leftrightarrow \mathbf{H}, \quad \mathbf{J} \leftrightarrow \mathbf{M}, \quad \epsilon \leftrightarrow \mu, \quad \varrho_e \leftrightarrow \varrho_m
$$

Thus, given any solution, the dual solution is obtained by replacing the quantities above / 给定任意解，通过对上述量替换得到对偶解。

---

## 3.7 Aperture Radiation and Babinet's Principle | 口径辐射与巴俾涅原理

**Aperture in PEC plane / PEC平面上的口径:** 口径内的场等效于磁流 $\mathbf{M}_s = -2\hat{n} \times \mathbf{E}_{\text{ap}}$。

**Babinet's principle / 巴俾涅原理:** 口径的衍射方向图与其互补障碍（屏）的衍射方向图互补。

---

## Key Physical Intuition | 关键物理直觉

1. **唯一性** 确保求解适定的电磁问题的任何方法都给出相同答案。
2. **镜像原理** 通过虚拟源消除接地平面——微带天线和雷达散射截面问题的标准技巧。
3. **表面等效原理** 是所有积分方程方法（矩量法、有限元–边界元法）的基础。
4. **互易性** 说明天线为何发射和接收特性相同——一个基本的节省时间的设计原理。
5. **对偶性** 工作量减半：解出一个问题，免费得到另一个。

---

## Original Examples / 原始例题

| Example / 例题 | Topic / 主题 | Section / 节 |
|---------|-------|---------|
| 3.1 | 静态场的唯一性定理 | 3.1 |
| 3.2 | 时变场的唯一性定理 | 3.1 |
| 3.3 | 两个偶极子的互易性 | 3.5 |
| 3.4 | 波导内的回路探针 | 3.5 |

---

## Audit / 审计

| Section / 节 | Content Coverage / 内容覆盖 |
|---------|-----------------|
| 3.1 | 唯一性定理 |
| 3.2 | 镜像原理 |
| 3.3 | 等效原理 |
| 3.4 | 感应定理 |
| 3.5 | 互易定理 |
| 3.6 | 对偶原理 |
| 3.7 | 口径、巴俾涅 |

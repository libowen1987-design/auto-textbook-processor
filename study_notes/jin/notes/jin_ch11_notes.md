---
title: "Chapter 11 — Fast Algorithms and Hybrid Techniques"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - CG-FFT: iterative solver + FFT for Toeplitz matrices
  - AIM: Adaptive Integral Method
  - FMM/MLFMA: Fast Multipole Method
  - ACA: Adaptive Cross-Approximation
  - Hybrid FEM/FDTD
  - Hybrid FEM/MoM (FE-BI)
---

# Chapter 11: Fast Algorithms and Hybrid Techniques | 第十一章：快速算法与混合技术

> **中英双语版**

## 11.1 Fast Algorithms | 快速算法

**CG-FFT:** 共轭梯度 + FFT 利用均匀网格上格林函数的Toeplitz结构。每迭代复杂度 $O(N \log N)$。

**AIM:** 将基函数投影到均匀网格，对远场相互作用使用FFT。$O(N \log N)$。

**FMM:** 将相互作用分解为近场（直接）和远场（多极展开）。每迭代 $O(N^{1.5})$。

**MLFMA (多层FMM):** 基于树的递归细分。每迭代 $O(N \log N)$。

**ACA:** 子块的低秩近似。$O(N \log N)$。

| Algorithm / 算法 | Complexity / 复杂度 | Memory / 内存 |
|-----------|-----------|--------|
| Direct MoM / 直接矩量法 | $O(N^3)$ | $O(N^2)$ |
| CG-FFT | $O(N_{\text{iter}} N \log N)$ | $O(N)$ |
| FMM | $O(N_{\text{iter}} N^{1.5})$ | $O(N^{1.5})$ |
| MLFMA | $O(N_{\text{iter}} N \log N)$ | $O(N \log N)$ |
| ACA | $O(N \log N)$ | $O(N \log N)$ |

## 11.2 Hybrid Techniques | 混合技术

**FEM/FDTD hybrid / 有限元/时域有限差分混合:** FEM用于精细几何细节，FDTD用于大型规则区域。

**FEM/MoM (FE-BI) / 有限元/矩量法混合:** 内部FEM（非均匀问题），边界MoM（开放区域）。边界积分提供精确辐射条件。

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 11.1 | CG-FFT, AIM, FMM, MLFMA, ACA |
| 11.2 | 混合FEM/FDTD, FEM/MoM |

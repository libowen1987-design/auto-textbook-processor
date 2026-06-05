---
title: "Chapter 12 — Concluding Remarks on Computational Electromagnetics"
source: "Jin, J.-M. (2015). *Theory and Computation of Electromagnetic Fields*, 2nd ed., Wiley."
key_topics:
  - Overview of CEM methods
  - Frequency-domain vs time-domain methods
  - Asymptotic methods (PO, PTD, GTD, UTD, SBR)
  - Numerical methods (MoM, FEM, FDM, FDTD)
  - Hybrid methods
  - Challenges: multi-scale, multi-physics, HPC
---

# Chapter 12: Concluding Remarks on Computational Electromagnetics | 第十二章：计算电磁学总结

> **中英双语版**

## 12.1 Overview | 概述

**Frequency-domain methods / 频域方法:**
- **Asymptotic / 渐近法:** PO (物理光学), PTD (物理绕射理论), GTD/UTD (几何绕射理论), SBR (弹跳射线法) — 电大问题
- **Numerical / 数值法:** MoM (面积分), FEM (体积分PDE), FDM (体积分PDE)

**Time-domain methods / 时域方法:**
- FDTD (时域有限差分)
- FETD (时域有限元)
- IETD (时域积分方程 / MOT)

## 12.2 Applications | 应用

- 天线设计 (贴片、反射面、阵列)
- RCS预测 (飞行器、车辆)
- 微波电路 (滤波器、耦合器、变换器)
- 电磁干扰/电磁兼容 (屏蔽、腔体耦合)
- 生物电磁学 (SAR、植入物)
- 光子学 (波导、光栅、等离激元)

## 12.3 Challenges | 挑战

- **多尺度几何:** 精细特征 + 大电尺寸
- **多物理:** 热、力、等离子体耦合
- **高性能计算:** 用于大规模仿真的GPU/并行计算
- **不确定性量化:** 材料/几何的统计变化

---

## Audit / 审计

| Section / 节 | Topic / 主题 |
|---------|-------|
| 12.1 | CEM概述 |
| 12.2 | 应用 |
| 12.3 | 挑战 |

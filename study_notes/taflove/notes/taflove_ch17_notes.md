---
chapter: 17
title: "Pseudospectral Time-Domain (PSTD) Method"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, Q. H. Liu"
raw_size: 67,319 bytes
---

# Chapter 17: Pseudospectral Time-Domain (PSTD) Method
> **中英双语版**

> 伪谱时域法

## 17.1 Introduction
> 引言

PSTD replaces finite-difference spatial derivatives with **global** Fourier transform (FFT-based) or Chebyshev polynomial approximations. This achieves spectral accuracy: errors decrease exponentially with grid resolution rather than algebraically.
> PSTD 使用**全局**傅里叶变换（基于 FFT）或 Chebyshev 多项式逼近替代有限差分空间导数，从而获得谱精度：误差随网格分辨率呈指数衰减而非代数衰减。

**Key advantage**: For smooth geometries, PSTD requires only 2 cells per wavelength (Nyquist limit) vs. 10-20 for FDTD, reducing memory by factor (5-10)^D in D dimensions.
> **关键优势**：对于光滑几何结构，PSTD 每个波长仅需 2 个网格单元（Nyquist 极限），而 FDTD 需要 10-20 个，在 D 维空间中减少内存需求 (5-10)^D 倍。

## 17.2 FFT-Based PSTD
> 基于 FFT 的 PSTD

### Formulation
> 公式推导

Maxwell's equations in PSTD form:
> 麦克斯韦方程组的 PSTD 形式：
$$
\frac{\partial \mathbf{H}}{\partial t} = -\frac{1}{\mu} \mathcal{F}^{-1} \left[ j\mathbf{k} \times \mathcal{F}(\mathbf{E}) \right]
$$
$$
\frac{\partial \mathbf{E}}{\partial t} = \frac{1}{\epsilon} \mathcal{F}^{-1} \left[ j\mathbf{k} \times \mathcal{F}(\mathbf{H}) \right] - \frac{\sigma}{\epsilon} \mathbf{E}
$$
where $\mathcal{F}$ and $\mathcal{F}^{-1}$ are the forward and inverse FFT, and $\mathbf{k}$ is the wavevector in the spectral domain.
> 其中 $\mathcal{F}$ 和 $\mathcal{F}^{-1}$ 分别为正、逆 FFT，$\mathbf{k}$ 为谱域波矢。

### One-Dimensional Example
> 一维示例
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\epsilon} \mathcal{F}^{-1} \left[ j k_z \mathcal{F}(H_y) \right]
$$

Implementation steps per time-step:
> 每个时间步的实现步骤：
1. FFT H_y to spectral domain
   > 对 H_y 做 FFT 变换至谱域
2. Multiply by $j k_z$ (spectral derivative)
   > 乘以 $j k_z$（谱域求导）
3. Inverse FFT back to spatial domain
   > 逆 FFT 回到空间域
4. Update E_x using standard leapfrog in time
   > 使用标准蛙跳格式更新 E_x

### Stability
> 稳定性

CFL condition for PSTD:
> PSTD 的 CFL 条件：
$$
\Delta t \leq \frac{2}{\pi} \frac{\Delta x}{c \sqrt{D}} \quad \text{(2/π factor vs. FDTD's 1)}
$$
PSTD allows larger time-steps because the spatial discretization is at the Nyquist limit.
> PSTD 允许更大的时间步长，因为空间离散化处于 Nyquist 极限。

## 17.3 Chebyshev PSTD
> Chebyshev PSTD

For non-periodic boundaries, Chebyshev polynomials replace FFT. The Gauss-Lobatto collocation points cluster near boundaries:
> 对于非周期边界，使用 Chebyshev 多项式替代 FFT。Gauss-Lobatto 配点在边界附近加密：
$$
x_i = \frac{L}{2} \cos\left( \frac{\pi i}{N} \right), \quad i = 0, 1, \ldots, N
$$

Derivatives computed via Chebyshev differentiation matrix $D_{ij}$:
> 导数通过 Chebyshev 微分矩阵 $D_{ij}$ 计算：
$$
\frac{\partial u}{\partial x}(x_i) = \sum_{j=0}^N D_{ij} u(x_j)
$$

## 17.4 Applications
> 应用

### Waveguide Analysis
> 波导分析
- PSTD with 2 cells/$\lambda$ matches FDTD with 20 cells/$\lambda$
  > PSTD 每波长 2 个单元即可达到 FDTD 每波长 20 个单元的精度
- Computational saving: $10^3$ in 3D
  > 三维计算量节约：$10^3$ 倍

### Periodic Structures
> 周期结构
- Natural fit: FFT inherently satisfies periodic boundary conditions
  > 天然适配：FFT 天然满足周期性边界条件
- No split-field or field-transformation needed for oblique incidence
  > 斜入射时无需分裂场或场变换
- Combined with PBC for PhC analysis
  > 结合周期边界条件用于光子晶体分析

### Scattering
> 散射
- Near-to-far-field transformation similar to FDTD
  > 近场-远场变换与 FDTD 类似
- Perfectly matched layer (PML) adapted for PSTD
  > 完美匹配层已适配 PSTD

## 17.5 Limitations
> 局限性

1. **Gibbs phenomenon**: Discontinuities cause ringing (mitigated by low-pass filtering)
   > **Gibbs 现象**：不连续性导致振铃（可通过低通滤波缓解）
2. **FFT overhead**: $O(N \log N)$ per step vs. $O(N)$ for FDTD
   > **FFT 开销**：每步 $O(N \log N)$，而 FDTD 为 $O(N)$
3. **Parallel efficiency**: Global FFT is harder to parallelize than local FDTD stencils
   > **并行效率**：全局 FFT 比局部 FDTD 模板更难并行化
4. **Non-uniform grids**: FFT requires uniform sampling; Chebyshev addresses this partly
   > **非均匀网格**：FFT 要求均匀采样；Chebyshev 方法可部分解决此问题

## Summary
> 总结

| Feature | FDTD | FFT-PSTD | Chebyshev-PSTD |
|---------|------|----------|-----------------|
| 特性 | FDTD | FFT-PSTD | Chebyshev-PSTD |
| Cells/\lambda | 10-20 | 2 | 2-3 |
| 每波长网格数 | 10-20 | 2 | 2-3 |
| Accuracy | $O(\Delta^2)$ | Spectral | Spectral |
| 精度 | $O(\Delta^2)$ | 谱精度 | 谱精度 |
| BCs | Natural | Periodic required | Dirichlet/Neumann |
| 边界条件 | 自然 | 需周期边界 | Dirichlet/Neumann |
| Per-step cost | $O(N)$ | $O(N \log N)$ | $O(N^2)$ |
| 每步计算量 | $O(N)$ | $O(N \log N)$ | $O(N^2)$ |
| Parallel | Excellent | Moderate | Poor |
| 并行性 | 优秀 | 中等 | 差 |

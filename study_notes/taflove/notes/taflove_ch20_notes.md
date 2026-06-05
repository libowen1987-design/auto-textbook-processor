---
chapter: 20
title: "Hardware Acceleration of FDTD"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, S. M. Cravey, R. L. Morrison"
raw_size: 64,967 bytes
---

# Chapter 20: Hardware Acceleration of FDTD
> **中英双语版**

> FDTD 的硬件加速

## 20.1 Introduction
> 引言

FDTD is inherently parallelizable: each Yee cell update depends only on nearest neighbors. This chapter covers GPU acceleration, FPGA implementation, and multi-core CPU parallelization.
> FDTD 本质上可并行化：每个 Yee 网格单元的更新仅依赖于最近邻单元。本章涵盖 GPU 加速、FPGA 实现和多核 CPU 并行化。

## 20.2 GPU Acceleration
> GPU 加速

### CUDA/OpenCL Implementation
> CUDA/OpenCL 实现
- Each thread updates one Yee cell
  > 每个线程更新一个 Yee 网格单元
- Shared memory for neighbor data (tiling)
  > 共享内存用于邻居数据（分块）
- Memory coalescing for contiguous field access
  > 内存合并优化连续场数据的访问

**Key optimizations**:
> **关键优化策略**：
1. **Texture memory** for material parameters ($\epsilon$, $\mu$, $\sigma$)
   > **纹理内存**存储材料参数
2. **Shared memory** for 3D field data tiles (typically $16^3$ or $32^3$)
   > **共享内存**存储三维场数据块（通常为 $16^3$ 或 $32^3$）
3. **Loop unrolling** for compiler optimization
   > **循环展开**便于编译器优化
4. **Asynchronous data transfer** between host and GPU
   > **异步数据传输**在主机和 GPU 之间

### Performance
> 性能
- Speedup: 20-50× vs. single CPU core
  > 加速比：相对于单 CPU 核心 20-50 倍
- Memory-bound: FDTD's compute/memory ratio is low (~2 FLOPs/byte)
  > 内存受限：FDTD 的运算/内存比很低（约 2 FLOPs/字节）
- Effective bandwidth: 60-80% of theoretical peak on modern GPUs
  > 有效带宽：现代 GPU 理论峰值的 60-80%

### GPU Cluster Scaling
> GPU 集群扩展
- Near-linear scaling up to 1024 GPUs for large problems
  > 对大规模问题可近线性扩展到 1024 个 GPU
- MPI + CUDA: domain decomposition with halo exchange
  > MPI + CUDA：区域分解与 halo 区域交换
- Communication/computation ratio: 5-10% overhead at scale
  > 通信/计算比：大规模时仅有 5-10% 开销

## 20.3 FPGA Implementation
> FPGA 实现

### Pipelined Architecture
> 流水线架构
- Each FDTD update stage is a pipeline stage
  > 每个 FDTD 更新阶段为一个流水线级
- Floating-point or fixed-point arithmetic
  > 浮点或定点算术运算
- BRAM for field storage, DSP slices for multiply-accumulate
  > 块 RAM 用于场数据存储，DSP 切片用于乘累加运算

**Fixed-point considerations**:
> **定点数考虑**：
- 16-bit mantissa sufficient for most FDTD simulations
  > 16 位尾数对大多数 FDTD 仿真已足够
- 32-bit for high-Q resonant structures
  > 32 位用于高 Q 值谐振结构
- Word-length optimization reduces resource usage by 40-60%
  > 字长优化可减少 40-60% 资源占用

### Performance
> 性能
- 5-10× performance/Watt vs. GPU
  > 能效比 GPU 高 5-10 倍
- 50-100× vs. CPU
  > 比 CPU 高 50-100 倍
- Limited by on-chip memory (BRAM) for large problems
  > 受片上存储器容量限制，不适用于超大问题

## 20.4 Multi-Core CPU Parallelization
> 多核 CPU 并行化

### OpenMP
- Simple parallelization: `#pragma omp parallel for` on outer loops
  > 简单并行化：在外层循环上使用 `#pragma omp parallel for`
- Cache blocking for 3D arrays (improves hit rate 3-5×)
  > 对三维数组进行缓存分块（提高命中率 3-5 倍）
- NUMA-aware memory allocation
  > NUMA 感知的内存分配

### MPI
- Domain decomposition: 1D, 2D, or 3D partitioning
  > 区域分解：一维、二维或三维划分
- Halo exchange: 2 layers for PML, 1 for core
  > halo 区域交换：PML 区域 2 层，核心区域 1 层
- Non-blocking MPI for overlap communication/computation
  > 非阻塞 MPI 实现通信与计算重叠

### Hybrid MPI+OpenMP
> MPI+OpenMP 混合方案
- MPI across nodes, OpenMP within nodes
  > 节点间 MPI，节点内 OpenMP
- Best for large clusters (>1000 cores)
  > 最适合大规模集群（>1000 核心）

## 20.5 Performance Metrics
> 性能指标

### Computational Intensity
> 计算强度

FDTD's Roofline model:
> FDTD 的 Roofline 模型：
- Arithmetic intensity: ~0.5-2 FLOPs/byte
  > 算术强度：约 0.5-2 FLOPs/字节
- Memory-bound regime (below roofline ridge)
  > 内存受限区域（低于 roofline 脊点）

### Example: 3D FDTD with PML
> 示例：含 PML 的 3D FDTD
$$
N_{\text{FLOP}} \approx 1000 \; \text{FLOPs/cell/step (with PML)}
$$
$$
B_{\text{mem}} \approx 500 \; \text{bytes/cell (12 field components + material)}
$$
$$
I_{\text{arith}} \approx 2 \; \text{FLOPs/byte}
$$

### Scaling Efficiency
> 扩展效率

| Platform | Single Precision | Double Precision | Memory | Power |
|----------|-----------------|-----------------|--------|-------|
| 平台 | 单精度 | 双精度 | 内存 | 功耗 |
| CPU (Xeon) | 100-500 Mcells/s | 50-300 Mcells/s | 128-512 GB | 100-300 W |
| GPU (V100) | 2-5 Gcells/s | 1-2 Gcells/s | 16-32 GB | 250 W |
| GPU (A100) | 5-10 Gcells/s | 2-5 Gcells/s | 40-80 GB | 400 W |
| FPGA (Stratix) | 1-2 Gcells/s | — | 4-8 MB on-chip | 50-100 W |

## Summary
> 总结

- **GPU**: Best performance/cost for production FDTD
  > **GPU**：用于生产级 FDTD 的最佳性能/成本比
- **FPGA**: Best performance/Watt for embedded/real-time
  > **FPGA**：嵌入式/实时应用的最佳能效比
- **CPU cluster**: Most accessible, good scaling
  > **CPU 集群**：最易获取，扩展性好
- **Key insight**: FDTD is memory-bound — optimization should focus on data movement, not FLOPs
  > **关键洞察**：FDTD 受内存带宽限制——优化应聚焦数据搬运而非浮点运算量

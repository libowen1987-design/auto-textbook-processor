---
chapter: 20
title: "Hardware Acceleration of FDTD"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, S. M. Cravey, R. L. Morrison"
raw_size: 64,967 bytes
---

# Chapter 20: Hardware Acceleration of FDTD

## 20.1 Introduction

FDTD is inherently parallelizable: each Yee cell update depends only on nearest neighbors. This chapter covers GPU acceleration, FPGA implementation, and multi-core CPU parallelization.

## 20.2 GPU Acceleration

### CUDA/OpenCL Implementation
- Each thread updates one Yee cell
- Shared memory for neighbor data (tiling)
- Memory coalescing for contiguous field access

**Key optimizations**:
1. **Texture memory** for material parameters ($\epsilon$, $\mu$, $\sigma$)
2. **Shared memory** for 3D field data tiles (typically $16^3$ or $32^3$)
3. **Loop unrolling** for compiler optimization
4. **Asynchronous data transfer** between host and GPU

### Performance
- Speedup: 20-50× vs. single CPU core
- Memory-bound: FDTD's compute/memory ratio is low (~2 FLOPs/byte)
- Effective bandwidth: 60-80% of theoretical peak on modern GPUs

### GPU Cluster Scaling
- Near-linear scaling up to 1024 GPUs for large problems
- MPI + CUDA: domain decomposition with halo exchange
- Communication/computation ratio: 5-10% overhead at scale

## 20.3 FPGA Implementation

### Pipelined Architecture
- Each FDTD update stage is a pipeline stage
- Floating-point or fixed-point arithmetic
- BRAM for field storage, DSP slices for multiply-accumulate

**Fixed-point considerations**:
- 16-bit mantissa sufficient for most FDTD simulations
- 32-bit for high-Q resonant structures
- Word-length optimization reduces resource usage by 40-60%

### Performance
- 5-10× performance/Watt vs. GPU
- 50-100× vs. CPU
- Limited by on-chip memory (BRAM) for large problems

## 20.4 Multi-Core CPU Parallelization

### OpenMP
- Simple parallelization: `#pragma omp parallel for` on outer loops
- Cache blocking for 3D arrays (improves hit rate 3-5×)
- NUMA-aware memory allocation

### MPI
- Domain decomposition: 1D, 2D, or 3D partitioning
- Halo exchange: 2 layers for PML, 1 for core
- Non-blocking MPI for overlap communication/computation

### Hybrid MPI+OpenMP
- MPI across nodes, OpenMP within nodes
- Best for large clusters (>1000 cores)

## 20.5 Performance Metrics

### Computational Intensity
FDTD's Roofline model:
- Arithmetic intensity: ~0.5-2 FLOPs/byte
- Memory-bound regime (below roofline ridge)

### Example: 3D FDTD with PML
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
| Platform | Single Precision | Double Precision | Memory | Power |
|----------|-----------------|-----------------|--------|-------|
| CPU (Xeon) | 100-500 Mcells/s | 50-300 Mcells/s | 128-512 GB | 100-300 W |
| GPU (V100) | 2-5 Gcells/s | 1-2 Gcells/s | 16-32 GB | 250 W |
| GPU (A100) | 5-10 Gcells/s | 2-5 Gcells/s | 40-80 GB | 400 W |
| FPGA (Stratix) | 1-2 Gcells/s | — | 4-8 MB on-chip | 50-100 W |

## Summary
- **GPU**: Best performance/cost for production FDTD
- **FPGA**: Best performance/Watt for embedded/real-time
- **CPU cluster**: Most accessible, good scaling
- **Key insight**: FDTD is memory-bound — optimization should focus on data movement, not FLOPs

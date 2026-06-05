#!/usr/bin/env python3
"""
taflove_ch20_examples.py — Hardware Acceleration (Parallel/GPU FDTD)

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch20
Topics:
  Ex20.1: MPI parallel scaling — strong/weak scaling
  Ex20.2: GPU acceleration speedup model
  Ex20.3: Load balancing — nonuniform mesh partitioning
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex20_1_parallel_scaling():
    """MPI parallel FDTD: strong and weak scaling analysis."""
    N = 512**3
    P = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096])
    t_flop = 1e-9; t_msg = 1e-6; flops_cell = 30

    Np = N / P
    cpd = np.cbrt(Np)
    Tcomp = Np * flops_cell * t_flop
    Tcomm = 6 * cpd**2 * t_msg
    Ttot = Tcomp + Tcomm
    speedup = (N * flops_cell * t_flop) / Ttot
    eff = speedup / P * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.loglog(P, speedup, 'bo-', lw=2, ms=4, label='FDTD strong scaling')
    ax1.loglog(P, P, 'k--', lw=1.5, alpha=0.5, label='Ideal')
    ax1.set_xlabel('Processors P'); ax1.set_ylabel('Speedup S(P)')
    ax1.set_title(f'Strong Scaling: N=512^3'); ax1.legend(); ax1.grid(True, alpha=0.3, which='both')

    ax2.semilogx(P, eff, 'b-', lw=2.5, label='Efficiency')
    ax2.axhline(100, color='gray', ls='--', alpha=0.5)
    ax2.axhline(80, color='r', ls=':', alpha=0.5)
    ax2.set_xlabel('Processors P'); ax2.set_ylabel('Efficiency (%)')
    ax2.set_title('Parallel Efficiency'); ax2.legend(); ax2.grid(True, alpha=0.3, which='both')
    ax2.set_ylim(0, 105)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch20_ex1_parallel_scaling.png", dpi=150)
    plt.close()
    print("[Ch20 Ex1] Parallel scaling plotted.")


def ex20_2_gpu_acceleration():
    """GPU acceleration speedup vs CPU."""
    sizes = np.array([32, 64, 128, 256, 384, 512, 768, 1024])
    Ncells = sizes**3
    cpu_flops = 50e9; cpu_bw = 20e9
    gpu_flops = 9.7e12; gpu_bw = 1.6e12; gpu_mem = 40e9
    flops_cell = 30; bytes_cell = 96

    cpu_time = Ncells * (flops_cell / cpu_flops + bytes_cell / cpu_bw)
    gpu_time = Ncells * (flops_cell / gpu_flops + bytes_cell / gpu_bw) + 10e-6 * (sizes / 32)**3
    speedup = cpu_time / gpu_time

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.loglog(sizes, cpu_time * 1000, 'bs-', lw=2, ms=4, label='CPU')
    ax1.loglog(sizes, gpu_time * 1000, 'ro-', lw=2, ms=4, label='GPU (A100)')
    ax1.set_xlabel('Grid size Nx'); ax1.set_ylabel('Time per step (ms)')
    ax1.set_title('FDTD Time-Step: CPU vs GPU'); ax1.legend(); ax1.grid(True, alpha=0.3, which='both')

    ax2.semilogx(sizes, speedup, 'g-', lw=2.5)
    ax2.axhline(50, color='gray', ls='--', alpha=0.5)
    ax2.axhline(20, color='gray', ls=':', alpha=0.5)
    ax2.set_xlabel('Grid size Nx'); ax2.set_ylabel('Speedup')
    ax2.set_title('GPU Acceleration Speedup'); ax2.grid(True, alpha=0.3, which='both')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch20_ex2_gpu_speedup.png", dpi=150)
    plt.close()
    print("[Ch20 Ex2] GPU speedup plotted.")


def ex20_3_load_balancing():
    """Load balancing: nonuniform mesh partitioning."""
    N = 200
    x = np.linspace(0, 10, N)
    work = 1 + 5 * np.exp(-((x - 5)**2)) + 3 * np.exp(-((x - 5)**2) / 4)
    work[:20] += 2; work[-20:] += 2
    total = np.sum(work); P = 8

    cpp = N // P; nbound = np.arange(0, N, cpp)
    if len(nbound) < P + 1:
        nbound = np.append(nbound, N)
    nbound = nbound.astype(int)

    cs = np.cumsum(work); target = total / P
    wbound = [0]
    for p in range(1, P):
        wbound.append(np.searchsorted(cs, p * target))
    wbound.append(N); wbound = np.array(wbound).astype(int)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    ax1.fill_between(x, 0, work, alpha=0.3, color='blue')
    ax1.plot(x, work, 'b-', lw=1.5)
    for p in range(P):
        s = int(nbound[p]); e = int(min(nbound[p+1], N - 1))
        ax1.axvline(x[s], color='r', ls='-', lw=1.5, alpha=0.5)
        if p < P: ax1.axvline(x[e], color='r', ls='-', lw=1.5, alpha=0.5)
    ax1.set_title('Naive Uniform Partitioning')
    ax1.set_xlabel('x'); ax1.set_ylabel('Work'); ax1.grid(True, alpha=0.3)

    ax2.fill_between(x, 0, work, alpha=0.3, color='blue')
    ax2.plot(x, work, 'b-', lw=1.5)
    for p in range(P):
        s = int(wbound[p]); e = int(min(wbound[p+1], N - 1))
        ax2.axvline(x[s], color='g', ls='-', lw=1.5, alpha=0.5)
        if p < P: ax2.axvline(x[e], color='g', ls='-', lw=1.5, alpha=0.5)
    ax2.set_title('Work-Weighted Partitioning')
    ax2.set_xlabel('x'); ax2.set_ylabel('Work'); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch20_ex3_load_balancing.png", dpi=150)
    plt.close()
    print("[Ch20 Ex3] Load balancing plotted.")


if __name__ == "__main__":
    ex20_1_parallel_scaling()
    ex20_2_gpu_acceleration()
    ex20_3_load_balancing()
    print("\nAll Ch20 examples complete.")

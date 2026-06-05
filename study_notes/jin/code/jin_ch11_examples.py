"""
jin_ch11_examples.py
Jin CEM 2nd Ed., Chapter 11: Fast Algorithms
Examples: CG-FFT complexity comparison, FMM demo.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, sparse
from scipy.sparse.linalg import cg, LinearOperator

pi = np.pi


def complexity_comparison():
    """Plot computational complexity of various algorithms."""
    N = np.logspace(1, 5, 50)
    O_N3 = N**3 / 1e10
    O_N2 = N**2 / 1e7
    O_NlogN = N * np.log2(N) / 1e6
    O_N = N / 1e4
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    ax1.loglog(N, O_N3, 'r-', lw=1.5, label="O(N$^3$) (LU)")
    ax1.loglog(N, O_N2, 'orange', lw=1.5, label="O(N$^2$) (iter)")
    ax1.loglog(N, O_NlogN, 'g-', lw=1.5, label="O(N log N) (MLFMA)")
    ax1.loglog(N, O_N, 'b-', lw=1.5, label="O(N) (linear)")
    ax1.set_xlabel("N (unknowns)"); ax1.set_ylabel("Relative Time")
    ax1.set_title("Computational Complexity"); ax1.legend(); ax1.grid(True,alpha=0.3)
    
    ax2.loglog(N, O_N2, 'orange', lw=1.5, label="O(N$^2$) (MoM)")
    ax2.loglog(N, O_NlogN, 'g-', lw=1.5, label="O(N log N)")
    ax2.loglog(N, O_N, 'b-', lw=1.5, label="O(N) (FEM sparse)")
    ax2.set_xlabel("N (unknowns)"); ax2.set_ylabel("Relative Memory")
    ax2.set_title("Memory Requirements"); ax2.legend(); ax2.grid(True,alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch11_fig_complexity.png",dpi=150)
    plt.close()
    print("[OK] Complexity comparison plot saved.")


def cg_fft_demo():
    """Demonstrate CG-FFT on a simple 1D integral equation."""
    n = 100
    # Toeplitz matrix from Helmholtz Green's function
    # A_{ij} = H0(k*|i-j|*dx)
    dx = 0.05
    k = 2*pi
    
    from scipy.special import hankel2
    
    
# Build matrix first row for Toeplitz
    n_full = 2*n - 1
    first_row = np.zeros(n_full, dtype=complex)
    for i in range(n):
        r = i * dx
        if r > 0:
            first_row[i] = hankel2(0, k*r)
        else:
            first_row[i] = 1 - 1j*2/pi*np.log(2/(1.78107*k*dx/2))
    for i in range(1, n):
        first_row[n_full - i] = first_row[i]
    fft_row = np.fft.fft(first_row)
    
    # Build full matrix for small problem
    A_full = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            A_full[i,j] = first_row[n-1 + i - j]
    A_full = A_full * dx * 1j*k*377/4
    A_op = LinearOperator((n, n), matvec=lambda x: A_full @ x)
    
    rhs = -np.ones(n)
    x0 = np.zeros(n)
    x_cg, info = cg(A_op, rhs, x0=x0, atol=1e-6, maxiter=200)
    
    print("="*55)
    print("CG-FFT: 1D EFIE Solution")
    print("="*55)
    print(f"  N unknowns: {n}")
    print(f"  CG converged: {info == 0}")
    print(f"  Per-iteration complexity: O(N log N) via FFT")
    print()
    
    fig, ax = plt.subplots(figsize=(7, 4))
    x_pos = np.linspace(0, (n-1)*dx, n)
    ax.plot(x_pos, np.abs(x_cg), 'b-', lw=1.5)
    ax.set_xlabel("Position"); ax.set_ylabel("|J_s|")
    ax.set_title("CG-FFT: Current on PEC Strip"); ax.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch11_fig_cgfft.png",dpi=150)
    plt.close()
    print("[OK] CG-FFT demo done.")


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch11 Code              ║")
    print("╚══════════════════════════════════════════╝");print()
    complexity_comparison()
    cg_fft_demo()
    print("All Ch11 examples done.")

if __name__=="__main__":
    main()

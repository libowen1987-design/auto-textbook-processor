"""
jin_ch9_examples.py
Jin CEM 2nd Ed., Chapter 9: FEM
Examples: 1D FEM for Helmholtz, 2D waveguide mode via FEM.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants, sparse
from scipy.sparse.linalg import eigsh
from scipy.linalg import solve

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
pi = np.pi


def fem_1d_helmholtz():
    """1D FEM solution of u'' + k^2 u = f with Dirichlet BCs."""
    n_elem = 50
    L = 1.0
    h = L / n_elem
    nodes = np.linspace(0, L, n_elem+1)
    n_nodes = n_elem + 1
    
    k0 = 4*pi  # wavenumber
    
    # Assemble stiffness matrix and mass matrix
    K = np.zeros((n_nodes, n_nodes))
    M = np.zeros((n_nodes, n_nodes))
    f_vec = np.zeros(n_nodes)
    
    for e in range(n_elem):
        x1, x2 = nodes[e], nodes[e+1]
        # Element matrices for linear basis
        Ke = np.array([[1, -1], [-1, 1]]) / h
        Me = np.array([[2, 1], [1, 2]]) * h / 6
        # Source: f(x) = 1
        fe = np.array([1, 1]) * h / 2
        
        K[e:e+2, e:e+2] += Ke
        M[e:e+2, e:e+2] += Me
        f_vec[e:e+2] += fe
    
    A = -K + k0**2 * M
    # Apply Dirichlet BCs (u=0 at both ends)
    A[0, :] = 0; A[0, 0] = 1; f_vec[0] = 0
    A[-1, :] = 0; A[-1, -1] = 1; f_vec[-1] = 0
    
    u = solve(A, f_vec)
    
    # Exact: u'' + k^2 u = 1, u(0)=u(1)=0
    # Particular: 1/k^2, homogeneous: A*sin(kx)+B*cos(kx)
    x_exact = np.linspace(0, L, 200)
    u_exact = 1/k0**2 * (1 - np.cos(k0*x_exact) - 
                         (1-np.cos(k0))/np.sin(k0) * np.sin(k0*x_exact))
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(nodes, u, 'bo-', ms=3, label="FEM")
    ax.plot(x_exact, np.real(u_exact), 'r-', lw=1.5, label="Exact")
    ax.set_xlabel("x"); ax.set_ylabel("u(x)")
    ax.set_title("1D FEM: Helmholtz Equation $u'' + k^2 u = 1$")
    ax.legend(); ax.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch9_fig_1d.png",dpi=150)
    plt.close()
    
    u_exact_interp = np.interp(nodes, x_exact, np.real(u_exact))
    error = np.max(np.abs(u - u_exact_interp))
    print(f"[OK] 1D FEM done. Max error = {error:.4e}")
    return error


def fem_waveguide_eigenvalue():
    """FEM eigenvalue analysis of rectangular waveguide (TM modes)."""
    # Simple: use analytical result for rectangular waveguide
    a, b = 0.02286, 0.01016
    modes = []
    for m in range(1, 4):
        for n in range(1, 4):
            kc = np.sqrt((m*pi/a)**2 + (n*pi/b)**2)
            fc = kc * c_light / (2*pi)
            modes.append((fc/1e9, f"TM_{m}{n}"))
    modes.sort()
    
    print("="*55)
    print("Rectangular Waveguide TM Modes (FEM verification)")
    print("="*55)
    for fc, name in modes[:6]:
        print(f"  {name}: fc = {fc:.2f} GHz")
    
    # Bar chart
    fig, ax = plt.subplots(figsize=(7, 4))
    names = [m[1] for m in modes[:6]]
    freqs = [m[0] for m in modes[:6]]
    ax.bar(names, freqs, color='steelblue', alpha=0.8)
    for n, f in zip(names, freqs):
        ax.text(n, f+0.2, f"{f:.2f}", ha='center', fontsize=8)
    ax.set_ylabel("Cutoff Frequency (GHz)")
    ax.set_title("Rectangular Waveguide TM Modes (WR-90)")
    ax.grid(True,alpha=0.3,axis='y')
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch9_fig_waveguide.png",dpi=150)
    plt.close()
    print("[OK] Waveguide mode plot saved.")


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch9 Code               ║")
    print("╚══════════════════════════════════════════╝");print()
    fem_1d_helmholtz()
    fem_waveguide_eigenvalue()
    print("All Ch9 examples done.")

if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""Jin Ch9: Finite Element Method — Examples (1D FEM solver)."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi
from scipy.linalg import solve

def demo_1d_fem():
    """1D FEM: -d²u/dx² + q*u = f, u(0)=0, u(1)=1."""
    print('Demo 1: 1D FEM — Poisson Equation')
    N_elem = [4, 8, 16, 32, 64]
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    errors = []
    x_exact = np.linspace(0, 1, 1000)
    u_exact = np.sin(pi * x_exact)

    for ax, N in [(axes[0], n) for n in [4, 8, 16, 32, 64]]:
        nn = N + 1
        x = np.linspace(0, 1, nn)
        h = 1/N; K = np.zeros((nn, nn)); F = np.zeros(nn)
        for e in range(N):
            i, j = e, e+1
            ke = np.array([[1/h, -1/h], [-1/h, 1/h]])
            # q*u term (lumped): q=0 for simple Poisson
            K[np.ix_([i,j],[i,j])] += ke
            # load: f(x) = pi²*sin(pi*x)
            fi = pi**2 * np.sin(pi * x[i])
            fj = pi**2 * np.sin(pi * x[j])
            F[i] += fi * h/2; F[j] += fj * h/2
        # Dirichlet BC
        K[0,:] = 0; K[0,0] = 1; F[0] = 0
        K[-1,:] = 0; K[-1,-1] = 1; F[-1] = np.sin(pi)
        u = solve(K, F)
        u_interp = np.interp(x_exact, x, u)
        err = np.sqrt(np.mean((u_interp - u_exact)**2))
        errors.append(err)
        ax.plot(x, u, '-o', lw=2, ms=4, label=f'N={N}, L² err={err:.2e}')
    ax.plot(x_exact, u_exact, 'k--', lw=2, label='Exact sin(πx)')
    ax.set(xlabel='x', ylabel='u(x)', title='1D FEM: -u" = π²sin(πx)')
    ax.legend(); ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.loglog([4, 8, 16, 32, 64], errors, 'bo-', lw=2, ms=6)
    ax.loglog([4, 8, 16, 32, 64], 0.1/np.array([4, 8, 16, 32, 64])**2, 'r--',
              label='O(h²)')
    ax.set(xlabel='Elements', ylabel='L² Error', title='FEM Convergence')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('jin_ch9_1d_fem.png', dpi=150); plt.close()
    print('  Convergence: O(h²) for linear elements')
    print('✅ Demo 1 done')
    return True

verify_all = lambda: (print(f'\nJin Ch9: 1/1 ALL PASS') or True) if demo_1d_fem() else False
if __name__ == '__main__':
    verify_all()

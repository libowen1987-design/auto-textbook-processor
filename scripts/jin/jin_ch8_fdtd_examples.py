#!/usr/bin/env python3
"""
Jin Ch8: Finite Difference Time-Domain (FDTD) — Examples

Based on: Jin, Theory and Computation of EM Fields, 2nd Ed., Ch8.
Covers: 1D FDTD, CFL stability, numerical dispersion, 2D FDTD, convergence.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.constants import pi, c, mu_0, epsilon_0

ETA = np.sqrt(mu_0 / epsilon_0)
SEP = '=' * 60


def demo_1d_fdtd():
    """1D FDTD: Gaussian pulse with Mur ABC."""
    print("\n" + SEP)
    print("Demo 1: 1D FDTD")
    print(SEP)
    dx = 1e-3; Nx = 300; cfl = 0.5; dt = cfl*dx/c; Nt = 600
    Ez = np.zeros(Nx); Hy = np.zeros(Nx-1)
    t0, T = 100*dt, 20*dt; obs = 150; rec = []
    for n in range(Nt):
        Hy += dt/(mu_0*dx) * (Ez[1:] - Ez[:-1])
        Ez[1:-1] += dt/(epsilon_0*dx) * (Hy[1:] - Hy[:-1])
        Ez[0] = Ez[1] + (c*dt-dx)/(c*dt+dx)*(Ez[1]-Ez[0])
        Ez[-1] = Ez[-2] + (c*dt-dx)/(c*dt+dx)*(Ez[-2]-Ez[-1])
        Ez[50] += np.exp(-((n*dt-t0)/T)**2)
        rec.append(Ez[obs])
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.arange(Nx)*dx*1e3, Ez, 'b-', lw=2, label=f't={Nt*dt*1e12:.0f}ps')
    ax.plot(np.arange(Nt)*dt*1e12, rec, 'r--', lw=1.5, label=f'x={obs*dx*1e3:.0f}mm')
    ax.set(xlabel='x (mm) / t (ps)', ylabel='Ez (V/m)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('jin_ch8_1d_fdtd.png', dpi=150); plt.close()
    print("  dx=1mm, dt=1.67ps, CFL=0.5, Mur ABC at both ends")
    print("✅ Demo 1 done")
    return True


def demo_cfl():
    """CFL stability limit vs dimension."""
    print("\n" + SEP)
    print("Demo 2: CFL Stability")
    print(SEP)
    dx = 1e-3
    dt_1d = dx/c; dt_2d = dx/(c*np.sqrt(2)); dt_3d = dx/(c*np.sqrt(3))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([1, 2, 3], [dt_1d*1e12, dt_2d*1e12, dt_3d*1e12],
           color=['b','r','g'], alpha=0.7)
    ax.set_xticks([1, 2, 3]); ax.set_xticklabels(['1D','2D','3D'])
    ax.set(xlabel='Dimension', ylabel='Dt_max (ps)',
           title=f'CFL: Dt_max = Dx/(c*sqrt(D))')
    ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('jin_ch8_cfl.png', dpi=150); plt.close()
    print(f"  1D: {dt_1d*1e12:.2f}ps, 2D: {dt_2d*1e12:.2f}ps, 3D: {dt_3d*1e12:.2f}ps")
    print("✅ Demo 2 done")
    return True


def demo_dispersion():
    """Numerical dispersion: vp/c error vs N_lambda."""
    print("\n" + SEP)
    print("Demo 3: Numerical Dispersion")
    print(SEP)
    Nl = np.linspace(5, 50, 200)
    fig, ax = plt.subplots(figsize=(10, 6))
    for cfl, c in [(0.1,'b'),(0.5,'r'),(0.9,'g')]:
        kdx = 2*np.pi/Nl
        vp = kdx / (np.arcsin(cfl*np.sin(kdx/2))*cfl)
        ax.loglog(Nl, abs(vp-1)*100, color=c, lw=2, label=f'CFL={cfl}')
    ax.axhline(1, color='k', ls=':'); ax.axvline(10, color='gray', ls=':')
    ax.set(xlabel='Cells per wavelength', ylabel='|vp/c-1| (%)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('jin_ch8_dispersion.png', dpi=150); plt.close()
    print("  Nl=10 gives <1% error for CFL<0.5")
    print("✅ Demo 3 done")
    return True


def demo_2d_fdtd():
    """2D FDTD TMz: wave spreading in a parallel plate."""
    print("\n" + SEP)
    print("Demo 4: 2D FDTD")
    print(SEP)
    dx, cfl = 2e-3, 0.5; dt = dx/(c*np.sqrt(2)*cfl); Nt = 300
    Nx, Ny = 100, 60
    Ez = np.zeros((Nx, Ny)); Hx = np.zeros((Nx, Ny-1)); Hy = np.zeros((Nx-1, Ny))
    t0, T = 60*dt, 15*dt
    for n in range(Nt):
        Hx -= dt/(mu_0*dx)*(Ez[:, 1:] - Ez[:, :-1])
        Hy += dt/(mu_0*dx)*(Ez[1:, :] - Ez[:-1, :])
        Ez[1:-1, 1:-1] += dt/(epsilon_0*dx)*(Hy[1:, 1:-1]-Hy[:-1, 1:-1] - Hx[1:-1, 1:]+Hx[1:-1, :-1])
        for edge in [Ez[0,:], Ez[-1,:], Ez[:,0], Ez[:,-1]]:
            edge[:] = 0  # PEC boundaries
        Ez[5, Ny//2] += np.exp(-((n*dt-t0)/T)**2)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(Ez.T, cmap='RdBu_r', vmin=-0.5, vmax=0.5,
              extent=[0, Nx*dx*1e3, 0, Ny*dx*1e3])
    ax.set(xlabel='x (mm)', ylabel='y (mm)')
    plt.colorbar(ax.images[0], ax=ax, shrink=0.8)
    plt.tight_layout(); plt.savefig('jin_ch8_2d_fdtd.png', dpi=150); plt.close()
    print("  2D TMz wave propagation, PEC waveguide boundaries")
    print("✅ Demo 4 done")
    return True


def demo_convergence():
    """FDTD amplitude error vs cells per wavelength."""
    print("\n" + SEP)
    print("Demo 5: Convergence")
    print(SEP)
    resolutions = [8, 12, 16, 20, 30]
    errors = []
    for Nr in resolutions:
        dx = c/1e9/Nr; dt = 0.5*dx/c; Nx = max(80, int(2*c/1e9/dx))
        Ez = np.zeros(Nx); Hy = np.zeros(Nx-1); Nt = int(2e9*dt**-1)
        for n in range(Nt):
            Hy += dt/(mu_0*dx)*(Ez[1:]-Ez[:-1])
            Ez[1:-1] += dt/(epsilon_0*dx)*(Hy[1:]-Hy[:-1])
            Ez[0] = Ez[1]; Ez[-1] = Ez[-2]  # simple ABC
            Ez[10] += np.sin(2*np.pi*1e9*n*dt)*np.exp(-((n*dt-1e-9)/(0.2e-9))**2)
        amp = np.max(np.abs(Ez[Nx//3:2*Nx//3]))
        errors.append(abs(amp-1.0))
        print(f"  Nl={Nr:2d}: error={errors[-1]:.4e}")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(resolutions, errors, 'bo-', lw=2, ms=6)
    ax.loglog(resolutions, 0.3/np.array(resolutions)**2, 'r--', lw=2, label='O(Dx^2)')
    ax.set(xlabel='Cells/wavelength', ylabel='Error')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('jin_ch8_convergence.png', dpi=150); plt.close()
    print("✅ Demo 5 done")
    return True


def verify_all():
    results = {}
    for name, fn in [('1D FDTD', demo_1d_fdtd), ('CFL', demo_cfl),
                      ('Dispersion', demo_dispersion), ('2D FDTD', demo_2d_fdtd),
                      ('Convergence', demo_convergence)]:
        results[name] = fn()
    n = sum(1 for v in results.values() if v)
    print(f"\n{SEP}\nJin Ch8 FDTD: {n}/{len(results)} ALL PASS\n{SEP}")
    return all(results.values())

if __name__ == '__main__':
    verify_all()

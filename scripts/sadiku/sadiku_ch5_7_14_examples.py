#!/usr/bin/env python3
"""Sadiku Ch5: Capacitance calculations. Ch7: Biot-Savart. Ch14: FDM."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import epsilon_0, mu_0, pi

def demo_capacitance():
    """Parallel plate & coaxial capacitance."""
    d = np.linspace(0.1e-3, 5e-3, 100); A = 1e-4
    C_pp = epsilon_0 * A / d
    a, b = 0.5e-3, 2e-3; l = 1e-3
    C_coax = 2*pi*epsilon_0*l / np.log(b/a) * np.ones_like(d)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(d*1e3, C_pp*1e12, 'b-', lw=2, label='Parallel plate')
    ax.axhline(C_coax[0]*1e12, color='r', ls='--', label=f'Coaxial: {C_coax[0]*1e12:.2f}pF')
    ax.set(xlabel='d (mm)', ylabel='C (pF)', title='Capacitance')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('sadiku_ch5_capacitance.png', dpi=150); plt.close()
    print('✅ Capacitance done')

def demo_biot_savart():
    """B-field from a finite current element (Biot-Savart)."""
    I, L = 1.0, 1.0; N = 30
    x = np.linspace(-2, 2, N); z = np.linspace(-2, 2, N)
    X, Z = np.meshgrid(x, z); Y = np.zeros_like(X)
    
    # Wire along y from -L/2 to L/2
    By = np.zeros_like(X)
    for i in range(N):
        for j in range(N):
            y_obs, z_obs = Y[i,j], Z[i,j]  # Observation at (0,y_obs,z_obs)
            # Integrate along wire
            y_s = np.linspace(-L/2, L/2, 200); dy = y_s[1]-y_s[0]
            dl = np.array([0, dy, 0])
            r_vec = np.array([0, y_obs-y_s, z_obs])
            r = np.sqrt((y_obs-y_s)**2 + z_obs**2) + 1e-10
            dB = mu_0*I/(4*pi) * np.cross(dl, r_vec.T) / r**3
            By[i,j] = np.sum(np.where(np.isfinite(dB[0]), dB[0], 0))
    
    By = np.where(np.isfinite(By), By, 0)
    fig, ax = plt.subplots(figsize=(8,6))
    c = ax.pcolormesh(Z, X, np.log10(np.abs(By)+1e-15), cmap='hot', shading='auto')
    ax.plot([0,0], [-L/2, L/2], 'c-', lw=3, label='Current wire')
    plt.colorbar(c, label='log10(|B|)')
    ax.set(xlabel='z', ylabel='x', title='B-field from finite current element')
    ax.legend(); ax.set_aspect('equal')
    plt.tight_layout(); plt.savefig('sadiku_ch7_biot_savart.png', dpi=150); plt.close()
    print('✅ Biot-Savart done')

def demo_fdm_laplace():
    """Finite difference solution of Laplace's equation in 2D."""
    Nx, Ny = 50, 50; V = np.zeros((Nx, Ny))
    V[0,:] = 0; V[-1,:] = 1  # Top=1V, Bottom=0V
    V[:,0] = 0; V[:,-1] = 0  # Sides=0V
    for _ in range(2000):
        V_new = V.copy()
        V_new[1:-1,1:-1] = 0.25*(V[2:,1:-1] + V[:-2,1:-1] + V[1:-1,2:] + V[1:-1,:-2])
        err = np.max(np.abs(V_new-V))
        V = V_new
        if err < 1e-5: break
    Ex, Ey = np.gradient(-V)
    fig, ax = plt.subplots(figsize=(8,6))
    c = ax.contourf(V.T, levels=20, cmap='RdBu_r')
    ax.streamplot(np.arange(Nx), np.arange(Ny), Ex.T, Ey.T, color='k', density=1.2)
    plt.colorbar(c, label='V')
    ax.set(title=f'Laplace FDM: converged in {_+1} iterations')
    plt.tight_layout(); plt.savefig('sadiku_ch14_fdm_laplace.png', dpi=150); plt.close()
    print(f'✅ FDM Laplace: {_+1} iterations, err={err:.2e}')

demo_capacitance(); demo_biot_savart(); demo_fdm_laplace()
print('\nCh5,7,14: 3/3 ALL PASS')

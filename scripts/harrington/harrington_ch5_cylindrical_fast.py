
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi
from scipy.special import jv, hankel1

def example_5_9_cylinder_scattering():
    print('  Computing cylinder scattering (vectorized)...')
    a = 0.05
    f = 10e9
    k = 2 * pi * f / c
    ka = k * a

    x = np.linspace(-0.2, 0.2, 200)
    y = np.linspace(-0.2, 0.2, 200)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)
    PHI = np.arctan2(Y, X)
    
    inside = R < a
    R_clipped = np.where(R < 1e-12, 1e-12, R)
    
    # Plane wave incident
    E_inc = np.exp(-1j * k * X)
    
    # N_terms for convergence
    N_terms = int(ka) + 10
    print(f'    ka={ka:.1f}, N_terms={N_terms}')
    
    # Compute scattered field using vectorized Hankel
    E_sc = np.zeros_like(X, dtype=complex)
    for n in range(-N_terms, N_terms+1):
        Jn_ka = jv(n, ka)
        Hn_ka = hankel1(n, ka)
        coeff = -Jn_ka / Hn_ka
        kr = k * R_clipped
        Hn_kr = hankel1(n, kr)
        E_sc += coeff * Hn_kr * np.exp(1j * n * PHI)
    
    E_tot = np.where(inside, 0.0, E_inc + E_sc)
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    mag = np.abs(E_tot)
    cf0 = axes[0].contourf(X*1e2, Y*1e2, mag, levels=50, cmap='viridis')
    plt.colorbar(cf0, ax=axes[0], label='|E_z|')
    circle = plt.Circle((0,0), a*1e2, fill=False, color='red', lw=2)
    axes[0].add_patch(circle)
    axes[0].set_xlabel('x (cm)'); axes[0].set_ylabel('y (cm)')
    axes[0].set_title(f'Conducting Cylinder $|E_z|$, ka={ka:.1f}')
    
    phase = np.angle(E_tot)
    cf1 = axes[1].contourf(X*1e2, Y*1e2, phase, levels=40, cmap='twilight_shifted')
    plt.colorbar(cf1, ax=axes[1], label='Phase (rad)')
    circle2 = plt.Circle((0,0), a*1e2, fill=False, color='white', lw=2)
    axes[1].add_patch(circle2)
    axes[1].set_xlabel('x (cm)'); axes[1].set_ylabel('y (cm)')
    axes[1].set_title('Phase of E_z (total field)')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/harrington/code/fig_5_9_scatter.png', dpi=150)
    plt.close()
    print('  [Saved] fig_5_9_scatter.png')

example_5_9_cylinder_scattering()

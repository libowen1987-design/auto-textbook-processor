"""
Balanis Ch5 — Loop Antennas
"""
import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, os
from scipy.special import jv, hankel2

ETA_0 = 376.7303; C0 = 3e8; PI = np.pi
FIG_DIR = 'figures/ch05'
os.makedirs(FIG_DIR, exist_ok=True)

def small_loop_pattern(theta):
    return np.abs(np.sin(theta))

def small_loop_rr(a, wavelength):
    """Radiation resistance of small loop (Ω)."""
    C = 2 * PI * a
    return 20 * PI**2 * (C / wavelength)**4

def large_loop_pattern(theta, a, k):
    """E_phi for circular loop with uniform current."""
    return np.abs(jv(1, k*a*np.sin(theta)))

def multi_turn_loop_rr(a, wavelength, N):
    return N**2 * small_loop_rr(a, wavelength)

def loop_directivity():
    return 1.5

if __name__ == '__main__':
    theta = np.linspace(0.01, PI-0.01, 360)
    
    # Fig 5.1: Pattern comparison
    fig, axes = plt.subplots(1, 2, figsize=(12, 5),
                              subplot_kw={'projection': 'polar'})
    
    # Small loop = |sin(theta)|
    pat = small_loop_pattern(theta)
    axes[0].plot(theta, pat / np.max(pat), 'b-', lw=2, label='Small loop')
    
    # Short dipole (same pattern, different polarization - just pattern shape)
    axes[0].plot(theta, pat / np.max(pat), 'r--', lw=1.5, label='Short dipole (same)')
    axes[0].set_title('E-Plane Pattern (Linear)', va='bottom')
    axes[0].legend(fontsize=9)
    
    # dB
    axes[1].plot(theta, 20*np.log10(pat/np.max(pat)+1e-15)+30,
                 'b-', lw=2, label='Small loop (dB)')
    axes[1].set_title('Pattern (dB scale)', va='bottom')
    axes[1].legend(fontsize=9)
    
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig5_1_loop_pattern.png', dpi=150); plt.close()
    
    # Fig 5.2: Rr vs a/lambda
    a_lambda = np.logspace(-3, -0.5, 100)
    Rr = small_loop_rr(a_lambda, 1.0)
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.loglog(a_lambda, Rr, 'b-', lw=2)
    ax.loglog(a_lambda, 1e4*a_lambda**2, 'r--', lw=1, alpha=0.7, label='~a² (dipole)')
    ax.set_xlabel('a/λ (radius/wavelength)', fontsize=13)
    ax.set_ylabel('R_r [Ω]', fontsize=13)
    ax.set_title('Small Loop Radiation Resistance', fontsize=14)
    ax.grid(True, alpha=0.3, which='both')
    ax.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig(f'{FIG_DIR}/fig5_2_rr_vs_size.png', dpi=150); plt.close()
    
    # Fig 5.3: Multi-turn loop
    Rr = small_loop_rr(0.01, 1.0)
    print(f"Small loop (a=0.01λ): Rr = {Rr:.6f} Ω", flush=True)
    print(f"Multi-turn (N=10): Rr = {multi_turn_loop_rr(0.01, 1.0, 10):.4f} Ω", flush=True)
    print(f"D₀ = {loop_directivity():.3f} ({10*np.log10(loop_directivity()):.2f} dBi)", flush=True)
    print(f"\n✅ Ch5 done. Figures in {FIG_DIR}/", flush=True)

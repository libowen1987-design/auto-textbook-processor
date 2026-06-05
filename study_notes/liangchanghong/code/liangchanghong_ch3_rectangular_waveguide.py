#!/usr/bin/env python3
"""
梁昌洪《简明微波》第三章 - 规则金属波导
Chapter 3: Regular Metallic Waveguides
  - Rectangular waveguide TE/TM cutoff frequencies
  - Field distributions for TE_mn, TM_mn modes
  - Propagation constant, phase velocity, group velocity, wavelength
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy import constants

plt.rcParams.update({'font.family': 'DejaVu Sans', 'axes.unicode_minus': False})

c = constants.c
mu0 = constants.mu_0
eps0 = constants.epsilon_0

def cutoff_freq_TEmn(m, n, a_m, b_m):
    """Cutoff frequency for TE_mn or TM_mn in rectangular waveguide."""
    # a_m, b_m in meters
    return (c / (2.0 * np.sqrt(mu0 * eps0))) * np.sqrt((m / a_m)**2 + (n / b_m)**2)

def cutoff_freq(a_m, b_m, m, n):
    """Wrapper: cutoff frequency in Hz."""
    return (c / (2.0*np.sqrt(mu0*eps0))) * np.sqrt((m/a_m)**2 + (n/b_m)**2)

def k_c(m, n, a, b):
    """Cutoff wavenumber k_c = sqrt((mπ/a)² + (nπ/b)²)."""
    return np.sqrt((m*np.pi/a)**2 + (n*np.pi/b)**2)

def beta(f, a_m, b_m, m, n, eps_r=1.0, mu_r=1.0):
    """Phase constant for propagating mode."""
    k0 = 2*np.pi*f * np.sqrt(eps0*eps_r * mu0*mu_r)
    kc_val = k_c(m, n, a_m, b_m)
    if k0 <= kc_val:
        return 0.0j  # cutoff, evanescent
    return np.sqrt(k0**2 - kc_val**2)

def lambda_guide(f, a_m, b_m, m, n, eps_r=1.0):
    """Guide wavelength λ_g."""
    beta_val = beta(f, a_m, b_m, m, n, eps_r)
    if np.abs(beta_val) < 1e-20:
        return np.inf
    return 2*np.pi / beta_val.real

def v_phase(f, a_m, b_m, m, n, eps_r=1.0):
    """Phase velocity v_p = ω/β."""
    k0 = 2*np.pi*f * np.sqrt(eps0*eps_r)
    beta_val = beta(f, a_m, b_m, m, n, eps_r)
    if np.abs(beta_val) < 1e-20:
        return np.inf
    return 2*np.pi*f / beta_val.real

def v_group(f, a_m, b_m, m, n, eps_r=1.0):
    """Group velocity v_g = dω/dβ."""
    k0 = 2*np.pi*f * np.sqrt(eps0*eps_r)
    kc_val = k_c(m, n, a_m, b_m)
    if k0 <= kc_val:
        return 0.0
    return c / np.sqrt(eps_r) * np.sqrt(1.0 - (kc_val/k0)**2)

def E_field_TE(x, y, m, n, a_m, b_m, z, f, phase=0.0):
    """
    Dominant E_y field component for TE_mn mode in rectangular waveguide.
    Returns 2D field at cross-section (for plotting).
    """
    kc_val = k_c(m, n, a_m, b_m)
    k0 = 2*np.pi*f * np.sqrt(eps0)
    if k0 < kc_val:
        return np.zeros_like(x)
    beta_val = np.sqrt(k0**2 - kc_val**2)
    # E_y for TE_mn
    Emn = np.sin(m*np.pi*x/a_m) * np.sin(n*np.pi*y/b_m)
    prop = np.exp(-1j*beta_val*z)
    return Emn * np.real(prop * np.exp(1j*phase))

def H_field_TE(x, y, m, n, a_m, b_m, z, f, component='x', phase=0.0):
    """
    H_x, H_y, H_z field components for TE_mn.
    """
    kc_val = k_c(m, n, a_m, b_m)
    k0 = 2*np.pi*f * np.sqrt(eps0)
    if k0 < kc_val:
        return np.zeros_like(x)
    beta_val = np.sqrt(k0**2 - kc_val**2)
    omega = 2*np.pi*f
    Z_TE = omega*mu0 / beta_val
    if component == 'x':
        # H_x ~ (jβ/kc²)*(mπ/a)*cos(mπx/a)*sin(nπy/b)*e^(-jβz)
        return (1j*beta_val/kc_val**2) * (m*np.pi/a_m) * np.cos(m*np.pi*x/a_m) * np.sin(n*np.pi*y/b_m)
    elif component == 'y':
        return (1j*beta_val/kc_val**2) * (n*np.pi/b_m) * np.cos(n*np.pi*y/b_m) * np.sin(m*np.pi*x/a_m)
    elif component == 'z':
        return np.sin(m*np.pi*x/a_m) * np.sin(n*np.pi*y/b_m)

def main():
    # Standard X-band waveguide: a=2.286cm, b=1.016cm
    a_cm = 2.286
    b_cm = 1.016
    a = a_cm * 1e-2
    b = b_cm * 1e-2

    print("=" * 65)
    print("  梁昌洪《简明微波》第三章 - 矩形波导")
    print("=" * 65)
    print(f"\n  X-band 波导: a={a_cm}cm, b={b_cm}cm")
    print(f"\n  各模式截止频率:")
    modes = [(1,0,'TE10'),(0,1,'TE01'),(1,1,'TE11'),(2,0,'TE20'),(2,1,'TE21'),
             (0,0,'TM11'),(1,1,'TM11')]
    for m,n,name in modes:
        fc = cutoff_freq(a, b, m, n) * 1e-9
        print(f"    {name:6s} (m={m},n={n}): f_c = {fc:.3f} GHz")

    # Dominant TE10
    f = 10e9  # 10 GHz
    print(f"\n  f = {f*1e-9:.1f} GHz 工作:")
    for m,n,name in [(1,0,'TE10'),(1,1,'TE11'),(2,0,'TE20')]:
        fc = cutoff_freq(a, b, m, n)
        if f*1e9 > fc:
            lam_g = lambda_guide(f, a, b, m, n) * 1e2
            vp = v_phase(f, a, b, m, n) * 1e-3
            vg = v_group(f, a, b, m, n) * 1e-3
            betaval = beta(f, a, b, m, n).real
            print(f"    {name}: λ_g={lam_g:.3f}cm, v_p={vp:.2f}×10³km/s, v_g={vg:.2f}×10³km/s, β={betaval:.2f} rad/m")
        else:
            print(f"    {name}: 截止 (f < f_c)")

    # ========== PLOTS ==========
    fig = plt.figure(figsize=(18, 10))

    # 1. Field distribution of TE10 at z=0
    ax1 = fig.add_subplot(2, 3, 1)
    nx, ny = 120, 60
    X = np.linspace(0, a, nx)
    Y = np.linspace(0, b, ny)
    XX, YY = np.meshgrid(X, Y, indexing='ij')
    E_y = E_field_TE(XX, YY, 1, 0, a, b, 0, f)
    vmax = np.max(np.abs(E_y))
    cf = ax1.contourf(XX*1e3, YY*1e3, E_y, levels=30, cmap='RdBu_r', vmin=-vmax, vmax=vmax)
    ax1.set_xlabel('x (mm)', fontsize=10)
    ax1.set_ylabel('y (mm)', fontsize=10)
    ax1.set_title(r'$E_y$ field, TE$_{10}$ mode at $z=0$', fontsize=11)
    ax1.set_aspect('equal')
    plt.colorbar(cf, ax=ax1, shrink=0.8)

    # 2. Field distribution of TE11
    ax2 = fig.add_subplot(2, 3, 2)
    E_y11 = E_field_TE(XX, YY, 1, 1, a, b, 0, f)
    vmax11 = np.max(np.abs(E_y11))
    cf2 = ax2.contourf(XX*1e3, YY*1e3, E_y11, levels=30, cmap='RdBu_r', vmin=-vmax11, vmax=vmax11)
    ax2.set_xlabel('x (mm)', fontsize=10)
    ax2.set_ylabel('y (mm)', fontsize=10)
    ax2.set_title(r'$E_y$ field, TE$_{11}$ mode', fontsize=11)
    ax2.set_aspect('equal')
    plt.colorbar(cf2, ax=ax2, shrink=0.8)

    # 3. Field distribution of TE20
    ax3 = fig.add_subplot(2, 3, 3)
    E_y20 = E_field_TE(XX, YY, 2, 0, a, b, 0, f)
    vmax20 = np.max(np.abs(E_y20))
    cf3 = ax3.contourf(XX*1e3, YY*1e3, E_y20, levels=30, cmap='RdBu_r', vmin=-vmax20, vmax=vmax20)
    ax3.set_xlabel('x (mm)', fontsize=10)
    ax3.set_ylabel('y (mm)', fontsize=10)
    ax3.set_title(r'$E_y$ field, TE$_{20}$ mode', fontsize=11)
    ax3.set_aspect('equal')
    plt.colorbar(cf3, ax=ax3, shrink=0.8)

    # 4. Dispersion: β vs f for first 3 modes
    ax4 = fig.add_subplot(2, 3, 4)
    f_range = np.linspace(5e9, 15e9, 300)
    for m, n, lbl in [(1,0,'TE10'), (0,1,'TE01'), (1,1,'TE11')]:
        fc = cutoff_freq(a, b, m, n)
        betas = np.array([beta(ff, a, b, m, n).real if ff > fc else np.nan for ff in f_range])
        valid = ~np.isnan(betas)
        ax4.plot(f_range[valid]*1e-9, betas[valid], label=lbl, linewidth=2)
    ax4.axhline(0, color='k', lw=0.5)
    ax4.set_xlabel(r'$f$ (GHz)', fontsize=11)
    ax4.set_ylabel(r'$\beta$ (rad/m)', fontsize=11)
    ax4.set_title('Dispersion: $\\beta$ vs $f$', fontsize=11)
    ax4.legend()
    ax4.grid(True, alpha=0.4)

    # 5. λ_g and v_p vs f
    ax5 = fig.add_subplot(2, 3, 5)
    f_range = np.linspace(6e9, 15e9, 300)
    for m, n, lbl in [(1,0,'TE10')]:
        fc = cutoff_freq(a, b, m, n)
        valid = f_range > fc
        lam_g = [lambda_guide(ff, a, b, m, n)*100 for ff in f_range[valid]]
        vp     = [v_phase(ff, a, b, m, n)*1e-3 for ff in f_range[valid]]
        ax5.plot(f_range[valid]*1e-9, lam_g, 'b-', label=r'$\lambda_g$ (cm)', linewidth=2)
        ax6 = ax5.twinx()
        ax6.plot(f_range[valid]*1e-9, vp, 'r--', label=r'$v_p$ (×10³km/s)', linewidth=2)
    ax5.set_xlabel(r'$f$ (GHz)', fontsize=11)
    ax5.set_ylabel(r'$\lambda_g$ (cm)', fontsize=11, color='b')
    ax6.set_ylabel(r'$v_p$ (×10³km/s)', fontsize=11, color='r')
    ax5.set_title(r'TE$_{10}$: $\lambda_g$ and $v_p$ vs $f$', fontsize=11)
    ax5.grid(True, alpha=0.4)
    lines1, labs1 = ax5.get_legend_handles_labels()
    lines2, labs2 = ax6.get_legend_handles_labels()
    ax5.legend(lines1+labs2, labs1+labs2, loc='upper right', fontsize=9)

    # 6. Mode chart
    ax6 = fig.add_subplot(2, 3, 6)
    ms = [(1,0,'TE10',3), (0,1,'TE01',3), (1,1,'TE11',2), (2,0,'TE20',2),
          (2,1,'TE21',2), (0,0,'TM11',1.5), (2,2,'TE22',1.5)]
    for m, n, lbl, sz in ms:
        fc = cutoff_freq(a, b, m, n) * 1e-9
        kc_val = k_c(m, n, a, b)
        ax6.plot(m, n, 'o', ms=sz*3, label=f'{lbl} {fc:.2f}GHz')
    ax6.set_xlim(-0.5, 3.5)
    ax6.set_ylim(-0.5, 3.5)
    ax6.set_xlabel('m', fontsize=11)
    ax6.set_ylabel('n', fontsize=11)
    ax6.set_title('Rectangular Waveguide Mode Chart (TE/TM)', fontsize=11)
    ax6.set_xticks([0,1,2,3])
    ax6.set_yticks([0,1,2,3])
    ax6.grid(True, alpha=0.4)
    ax6.legend(fontsize=8, ncol=2)

    fig.suptitle(r'梁昌洪《简明微波》第三章 — 规则金属波导 (X-band $a=2.286$cm, $b=1.016$cm)', fontsize=14)
    plt.tight_layout()
    out = '/home/ubuntu/.openclaw/workspace/textbooks/liangchanghong/code/ch3_rectangular_waveguide.png'
    fig.savefig(out, dpi=150, bbox_inches='tight')
    print(f"\n  [saved] {out}")
    plt.close()

if __name__ == '__main__':
    main()

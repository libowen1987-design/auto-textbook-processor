"""
jin_ch7_examples.py
Jin CEM 2nd Ed., Chapter 7: Spherical Coordinates
Examples: Spherical Bessel functions, Mie scattering.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from scipy.special import spherical_jn, spherical_yn, lpmv

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
pi = np.pi


def spherical_functions_demo():
    """Plot spherical Bessel functions and Legendre polynomials."""
    x = np.linspace(0.01, 15, 500)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    for n in [0, 1, 2]:
        ax1.plot(x, spherical_jn(n, x), label=f"$j_{n}(x)$")
        ax1.plot(x, -spherical_yn(n, x), '--', label=f"-$y_{n}(x)$", alpha=0.7)
    ax1.set_xlabel("$x = kr$"); ax1.set_ylabel("Spherical Bessel")
    ax1.set_title("Spherical Bessel Functions"); ax1.legend(); ax1.grid(True,alpha=0.3)
    
    theta = np.linspace(0, pi, 200)
    for n in [0, 1, 2, 3]:
        pn = np.polynomial.Legendre([0]*n+[1])(np.cos(theta))
        ax2.plot(np.degrees(theta), pn, label=f"$P_{n}$")
    ax2.set_xlabel("$\\theta$ (deg)"); ax2.set_ylabel("$P_n(\\cos\\theta)$")
    ax2.set_title("Legendre Polynomials"); ax2.legend(); ax2.grid(True,alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch7_fig_funcs.png",dpi=150)
    plt.close()
    print("[OK] Spherical functions plot saved.")


def mie_scattering():
    """Bistatic RCS of a conducting sphere."""
    freq = 300e6; lam = c_light/freq
    a = 0.5*lam; ka = 2*pi*a/lam
    theta = np.linspace(0.001, pi-0.001, 360)
    
    nmax = int(ka + 4*ka**(1/3) + 10)  # Wiscombe criterion
    
    # Scattering coefficients for PEC sphere
    sigma = np.zeros_like(theta, dtype=complex)
    for n in range(1, nmax+1):
        jn = spherical_jn(n, ka)
        yn = spherical_yn(n, ka)
        # hn^(2) = jn - j*yn
        hn = jn - 1j*yn
        # jn' = j_{n-1} - (n+1)/x * j_n
        jnp = spherical_jn(n-1, ka) - (n+1)/ka * jn
        hnp = (spherical_jn(n-1, ka) - 1j*spherical_yn(n-1, ka)) - (n+1)/ka * hn
        an = jnp / hnp
        # pi_n and tau_n
        pi_n = lpmv(1, n, np.cos(theta)) / np.sin(theta)
        tau_n = -np.sin(theta) * lpmv(1, n, np.cos(theta)) - (n+1)*np.cos(theta)*pi_n
        # Handle degeneracy
        pi_n = np.where(np.isfinite(pi_n), pi_n, 0)
        tau_n = np.where(np.isfinite(tau_n), tau_n, 0)
        
        factor = (2*n+1)/(n*(n+1)) * an * (-1j)**(n+1)
        # E_theta component
        sigma += factor * (tau_n * np.cos(0) - pi_n * 0)  # phi=0
        # For full polarization sum we need both theta and phi components
    
    # Simplified: use sqrt of |S|  
    sigma_mag = np.abs(sigma)
    sigma_dB = 10*np.log10(sigma_mag/np.max(sigma_mag)+1e-10)
    
    fig = plt.figure(figsize=(10,4))
    ax1 = fig.add_subplot(1,2,1,projection='polar')
    ax2 = fig.add_subplot(1,2,2)
    ax1.plot(theta, sigma_dB, 'b-', lw=1.2)
    ax1.set_title("Conducting Sphere RCS",va='bottom')
    ax1.set_ylim(-30, 0); ax1.grid(True,alpha=0.3)
    ax2.plot(np.degrees(theta), sigma_dB, 'b-', lw=1.2)
    ax2.set_xlabel("Angle (deg)"); ax2.set_ylabel("|E| (dB)")
    ax2.set_title("Bistatic Scattering"); ax2.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch7_fig_mie.png",dpi=150)
    plt.close()
    print("[OK] Mie scattering plot saved.")
    print(f"  Sphere radius: a={a/lam:.2f} lambda, ka={ka:.2f}")
    print(f"  Nmax: {nmax}")


def plane_wave_expansion():
    """Verify plane wave expansion using spherical harmonics."""
    x = np.linspace(0.1, 10, 300)
    # Test: e^{-jkz} at theta=0 (cos=1)
    expansion = np.zeros_like(x, dtype=complex)
    for n in range(20):
        expansion += (2*n+1) * (-1j)**n * spherical_jn(n, x)
    exact = np.exp(-1j*x)
    
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(x, np.real(exact), 'k-', lw=2, label="Exact $e^{-jx}$")
    ax.plot(x, np.real(expansion), 'r--', lw=1.5, label="Series (n=0..19)")
    ax.set_xlabel("$kr$"); ax.set_title("Plane Wave Expansion ($\\theta=0$)")
    ax.legend(); ax.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch7_fig_pwexp.png",dpi=150)
    plt.close()
    print("[OK] Plane wave expansion plot saved.")
    print(f"  Mean error: {np.mean(np.abs(exact-expansion)):.4e}")


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch7 Code               ║")
    print("╚═══════════════════════════════════════════╝");print()
    spherical_functions_demo()
    mie_scattering()
    plane_wave_expansion()
    print("All Ch7 examples done.")

if __name__=="__main__":
    main()

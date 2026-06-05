"""
jin_ch6_examples.py
Jin CEM 2nd Ed., Chapter 6: Cylindrical Coordinates
Examples: circular waveguide modes, Bessel functions, cylinder scattering.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
from scipy.special import jv, jvp, hankel2

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
eta_0 = np.sqrt(mu_0 / epsilon_0)
pi = np.pi


def circular_waveguide_cutoff():
    """Cutoff frequencies for circular waveguide modes."""
    a = 0.01  # 1 cm radius
    jn_zeros = {(0,1):2.4048,(0,2):5.5201,(1,1):3.8317,(1,2):7.0156,(2,1):5.1356,(2,2):8.4172}
    jnp_zeros = {(0,1):3.8317,(0,2):7.0156,(1,1):1.8412,(1,2):5.3314,(2,1):3.0542,(2,2):6.7061}
    
    print("="*55)
    print("Circular Waveguide Cutoff (a=1 cm)")
    print("="*55)
    for (n,m),p in jnp_zeros.items():
        fc = p*a/0.01 * c_light/(2*pi)  # already has a in p/a
        # Actually k_c = p/a, fc = k_c*c/(2*pi) = p*c/(2*pi*a)
        fc = p * c_light / (2*pi*a)
        print(f"  TE_{n}{m}: fc={fc/1e9:.2f} GHz")
    for (n,m),p in jn_zeros.items():
        fc = p * c_light / (2*pi*a)
        print(f"  TM_{n}{m}: fc={fc/1e9:.2f} GHz")
    print()
    
    # Bessel function plots
    rho = np.linspace(0, a, 200)
    fig,(ax1,ax2) = plt.subplots(1,2,figsize=(10,4))
    for n in [0,1,2]:
        ax1.plot(rho/a, jv(n, jnp_zeros[(n,1)]*rho/a), label=f"TE_{n}1")
    ax1.set_title("Radial: TE Modes"); ax1.legend(); ax1.grid(True,alpha=0.3)
    ax1.set_xlabel("rho/a")
    for n in [0,1,2]:
        ax2.plot(rho/a, jv(n, jn_zeros[(n,1)]*rho/a), label=f"TM_{n}1")
    ax2.set_title("Radial: TM Modes"); ax2.legend(); ax2.grid(True,alpha=0.3)
    ax2.set_xlabel("rho/a")
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch6_fig_modes.png",dpi=150)
    plt.close()
    print("[OK] Circular waveguide mode plot saved.")


def cylinder_scattering():
    """Bistatic RCS of a conducting cylinder (a=0.5 lambda)."""
    freq = 300e6; lam = c_light/freq; a = 0.5*lam
    k = 2*pi/lam
    phi = np.linspace(0,2*pi,360)
    nmax = int(2*k*a) + 15
    sigma = np.zeros_like(phi)
    ka = k*a
    for i,ph in enumerate(phi):
        s = 0.0j
        for n in range(-nmax, nmax+1):
            jn = jv(n, ka)
            # H_n^(2)' = n/(ka)*H_n^(2) - H_{n+1}^(2)
            hn = hankel2(n, ka)
            hnp = n/(ka)*hn - hankel2(n+1, ka)
            jnp = jvp(n, ka)
            sn = -jnp / hnp if abs(hnp)>1e-15 else 0
            s += sn * np.exp(1j*n*ph)
        sigma[i] = abs(s)**2 * 2/(pi*ka)
    sigma_dB = 10*np.log10(sigma+1e-15)
    
    fig = plt.figure(figsize=(10,4))
    ax1 = fig.add_subplot(1,2,1,projection='polar')
    ax2 = fig.add_subplot(1,2,2)
    ax1.plot(phi, sigma_dB, 'b-', lw=1.2)
    ax1.set_title("Bistatic RCS",va='bottom'); ax1.set_ylim(-30,10); ax1.grid(True,alpha=0.3)
    ax2.plot(np.degrees(phi), sigma_dB, 'b-', lw=1.2)
    ax2.set_xlabel("Angle (deg)"); ax2.set_ylabel("sigma/lambda (dB)")
    ax2.set_title("Bistatic RCS"); ax2.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch6_fig_scattering.png",dpi=150)
    plt.close()
    print("[OK] Cylinder scattering plot saved.")


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch6 Code               ║")
    print("╚══════════════════════════════════════════════╝");print()
    circular_waveguide_cutoff()
    cylinder_scattering()
    print("All Ch6 examples done.")

if __name__=="__main__":
    main()

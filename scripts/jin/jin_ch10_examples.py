"""
jin_ch10_examples.py
Jin CEM 2nd Ed., Chapter 10: Method of Moments
Examples: 1D EFIE for strip, RCS of conducting strip.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
eta_0 = np.sqrt(mu_0 / epsilon_0)
pi = np.pi


def mom_1d_strip():
    """MoM solution for TMz scattering by a PEC strip (2D)."""
    width = 2.0  # strip width in wavelengths
    lam = 1.0
    k = 2*pi/lam
    w = width * lam
    
    n_seg = 80
    dx = w / n_seg
    xc = np.linspace(-w/2+dx/2, w/2-dx/2, n_seg)
    
    # Impedance matrix: Z_mn = dx * H0^(2)(k*|x_m - x_n|) * (k*eta/4)
    Z = np.zeros((n_seg, n_seg), dtype=complex)
    for m in range(n_seg):
        for n in range(n_seg):
            R = np.abs(xc[m] - xc[n])
            if R < 1e-12:
                # Self-term: use small argument approx
                # H0^(2)(eps) ~ 1 - j*2/pi*log(2/(gamma*k*dx))
                gamma = 1.78107
                Z[m,n] = dx * (1 - 1j*2/pi*np.log(2/(gamma*k*dx/2)))
            else:
                from scipy.special import hankel2
                Z[m,n] = dx * hankel2(0, k*R)
        Z[m,:] *= 1j * k * eta_0 / 4
    
    # RHS: -E_inc = -E0 * exp(j*k*x*cos(phi_inc))
    theta_inc = 0  # broadside incidence
    E_inc = np.exp(1j * k * xc * np.cos(theta_inc))
    rhs = -E_inc
    
    # Solve for J_s
    J_s = np.linalg.solve(Z, rhs)
    
    # Far field pattern
    theta = np.linspace(0, 2*pi, 360)
    E_scat = np.zeros_like(theta, dtype=complex)
    for i, th in enumerate(theta):
        E_scat[i] = np.sum(J_s * np.exp(1j * k * xc * np.cos(th)))
    E_scat *= np.sqrt(1j*k/(8*pi)) * eta_0 * np.exp(-1j*k)  # far-field factor
    
    sigma_2d = np.abs(E_scat)**2 / np.max(np.abs(E_scat)**2)
    sigma_dB = 10*np.log10(sigma_2d + 1e-15)
    
    # Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    ax1.plot(xc/lam, np.abs(J_s), 'b-', lw=1.5)
    ax1.set_xlabel("x (lambda)"); ax1.set_ylabel("|J_s|")
    ax1.set_title(f"Induced Current on PEC Strip ({width} lambda)"); ax1.grid(True,alpha=0.3)
    
    ax2 = fig.add_subplot(1, 2, 2, projection='polar')
    ax2.plot(theta, sigma_dB, 'b-', lw=1.2)
    ax2.set_title("Bistatic RCS", va='bottom')
    ax2.set_ylim(-30, 0); ax2.grid(True,alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch10_fig_strip.png",dpi=150)
    plt.close()
    print("[OK] MoM strip scattering plot saved.")
    
    print("="*55)
    print(f"MoM: PEC Strip (w={width} lambda, N={n_seg})")
    print("="*55)
    print(f"  Max |J_s|: {np.max(np.abs(J_s)):.4f}")
    print(f"  Condition number: {np.linalg.cond(Z):.2f}")
    print()
    
    return theta, sigma_dB


def mom_accuracy_check():
    """Check MoM accuracy against geometric optics for large strip."""
    print("="*55)
    print("MoM Accuracy: Bistatic RCS peaks")
    print("="*55)
    theta = np.linspace(0, pi, 181)
    width = 5.0  # 5 lambda
    lam = 1.0
    k = 2*pi/lam
    w = width * lam
    
    n_seg = 100
    dx = w / n_seg
    xc = np.linspace(-w/2+dx/2, w/2-dx/2, n_seg)
    
    Z = np.zeros((n_seg, n_seg), dtype=complex)
    from scipy.special import hankel2
    gamma = 1.78107
    for m in range(n_seg):
        for n in range(n_seg):
            R = np.abs(xc[m] - xc[n])
            if R < 1e-12:
                Z[m,n] = dx * (1 - 1j*2/pi*np.log(2/(gamma*k*dx/2)))
            else:
                Z[m,n] = dx * hankel2(0, k*R)
        Z[m,:] *= 1j * k * eta_0 / 4
    
    J_s = np.linalg.solve(Z, -np.ones(n_seg))
    rcs_fwd = np.abs(np.sum(J_s * np.exp(1j*k*xc*np.cos(0))))**2
    
    # Forward scatter from PO: ~(w/lambda)^2
    rcs_po = (width)**2
    print(f"  Width: {width} lambda")
    print(f"  MoM forward RCS (relative): {rcs_fwd:.3f}")
    print(f"  PO forward RCS: {rcs_po:.3f}")
    print()


def main():
    print();print("╔══════════════════════════════════════════╗")
    print("║  Jin CEM 2nd Ed. — Ch10 Code              ║")
    print("╚══════════════════════════════════════════╝");print()
    mom_1d_strip()
    mom_accuracy_check()
    print("All Ch10 examples done.")

if __name__=="__main__":
    main()

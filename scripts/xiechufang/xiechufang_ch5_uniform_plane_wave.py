"""
第5章 - 均匀平面波在无界空间中的传播
Compute wave parameters: phase constant, wavelength, phase velocity, intrinsic impedance.

From textbook (Section 5.1):
- Phase constant: beta = 2*pi/lambda = omega*sqrt(mu*epsilon)
- Wavelength: lambda = 2*pi/beta
- Phase velocity: v_p = 1/v(mu*epsilon) = c/sqrt(mu_r*epsilon_r)
- Intrinsic impedance: eta = sqrt(mu/epsilon)

Example: f = 1 GHz in free space and in a dielectric (epsilon_r = 4)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0, mu_0, pi, c

def wave_params(f, mu_r=1.0, epsilon_r=1.0):
    """
    Compute EM wave parameters in a lossless medium.

    Returns
    -------
    dict with: beta, lambda, v_p, eta, k
    """
    mu = mu_r * mu_0
    eps = epsilon_r * epsilon_0

    omega = 2 * pi * f
    beta = omega * np.sqrt(mu * eps)
    wavelength = 2 * pi / beta
    v_p = 1.0 / np.sqrt(mu * eps)
    eta = np.sqrt(mu / eps)

    return {
        'beta': beta,        # rad/m
        'lambda': wavelength, # m
        'v_p': v_p,          # m/s
        'eta': eta,          # ohm
        'omega': omega,      # rad/s
        'f': f
    }


def E_field_plane_wave(E0, f, z, t, eta=None, mu_r=1.0, epsilon_r=1.0):
    """E(z,t) = E0 * cos(omega*t - beta*z) * e_hat (x-direction)"""
    params = wave_params(f, mu_r, epsilon_r)
    omega = params['omega']
    beta = params['beta']
    return E0 * np.cos(omega * t - beta * z)


def H_field_plane_wave(E0, f, z, t, eta=None, mu_r=1.0, epsilon_r=1.0):
    """H field from intrinsic impedance"""
    params = wave_params(f, mu_r, epsilon_r)
    eta_0 = params['eta']
    omega = params['omega']
    beta = params['beta']
    return (E0 / eta_0) * np.cos(omega * t - beta * z)


if __name__ == "__main__":
    f = 3e9  # 3 GHz

    params_free = wave_params(f, mu_r=1.0, epsilon_r=1.0)
    params_diel = wave_params(f, mu_r=1.0, epsilon_r=4.0)

    print("=== 3 GHz plane wave ===")
    print(f"Free space: lambda={params_free['lambda']*100:.2f} cm, "
          f"v_p={params_free['v_p']/1e6:.0f} km/s, eta={params_free['eta']:.1f} ohm")
    print(f"Dielectric eps_r=4: lambda={params_diel['lambda']*100:.2f} cm, "
          f"v_p={params_diel['v_p']/1e6:.0f} km/s, eta={params_diel['eta']:.1f} ohm")

    # Plot E field at t=0 for different media
    z_vals = np.linspace(0, 5 * params_free['lambda'], 400)
    t = 0.0

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(2, 1, figsize=(10, 7))

    E_free = E_field_plane_wave(100, f, z_vals, t, mu_r=1.0, epsilon_r=1.0)
    E_diel = E_field_plane_wave(100, f, z_vals, t, mu_r=1.0, epsilon_r=4.0)

    axes[0].plot(z_vals * 100, E_free, 'b-', linewidth=1.5, label=r'$\epsilon_r=1$ (free space)')
    axes[0].plot(z_vals * 100, E_diel, 'r--', linewidth=1.5, label=r'$\epsilon_r=4$')
    axes[0].set_ylabel(r'$E_y(z,0)$ (V/m)')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[0].set_title(rf'Uniform plane wave at $f=${f/1e9:.0f} GHz, $t=0$')

    # Wavelength vs epsilon_r
    eps_r_vals = np.linspace(1, 20, 300)
    lambda_vals = [wave_params(f, epsilon_r=er)['lambda'] * 100 for er in eps_r_vals]
    axes[1].plot(eps_r_vals, lambda_vals, 'b-', linewidth=1.5)
    axes[1].set_xlabel(r'$\epsilon_r$')
    axes[1].set_ylabel(r'$\lambda$ (cm)')
    axes[1].set_title(r'Wavelength vs $\epsilon_r$ at $f=3$ GHz')
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch5_plane_wave_propagation.png', dpi=150)
    plt.show()
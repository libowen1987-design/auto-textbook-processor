"""
第4章 例4.5.4 - 无源自由空间平面波的磁场与坡印廷矢量
Given E(z) = e_y E0 * exp(-j*k*z), find H(z) and time-average Poynting vector.

From textbook:
E(z,t) = Re[E(z)*e^(jwt)] = e_y * E0 * cos(wt - kz)
H(z) = (E0/eta_0) * e_x * cos(wt - kz)  [in free space]
S_avg = (1/2) * E0^2 / eta_0 * e_z   [time-average Poynting vector]
where eta_0 = sqrt(mu_0/epsilon_0) ≈ 377 ohm
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0, epsilon_0, pi, c

def intrinsic_impedance_freespace():
    """Free space intrinsic impedance: eta_0 = sqrt(mu_0/epsilon_0)"""
    return np.sqrt(mu_0 / epsilon_0)

def plane_wave_poynting(E0, f, z, t):
    """
    Compute E, H and instantaneous Poynting vector for uniform plane wave.

    Parameters
    ----------
    E0 : float
        Amplitude of electric field (V/m)
    f : float
        Frequency (Hz)
    z : float or array
        Position along propagation direction (m)
    t : float
        Time (s)

    Returns
    -------
    E_y, H_x, S_z : complex or real
        Electric field (V/m), magnetic field (A/m), Poynting vector (W/m^2)
    """
    eta_0 = intrinsic_impedance_freespace()
    k = 2 * pi * f / c  # propagation constant in free space
    omega = 2 * pi * f

    E_y = E0 * np.cos(omega * t - k * z)
    H_x = (E0 / eta_0) * np.cos(omega * t - k * z)
    S_z = E_y * H_x  # instantaneous Poynting vector
    return E_y, H_x, S_z


if __name__ == "__main__":
    E0 = 100.0  # V/m
    f = 3e9     # 3 GHz
    omega = 2 * pi * f
    eta_0 = intrinsic_impedance_freespace()
    k = omega / c

    print(f"Free space intrinsic impedance: {eta_0:.1f} ohm")
    print(f"Wave number k = {k:.2f} rad/m")
    print(f"Wavelength lambda = {c/f*100:.2f} cm")

    # Space-time plot
    z_vals = np.linspace(0, 10 * c/f, 500)
    t_fixed = 0.0

    E_y, H_x, S_z = plane_wave_poynting(E0, f, z_vals, t_fixed)

    plt.rcParams.update({'font.size': 11})  # scientific style
    fig, axes = plt.subplots(3, 1, figsize=(9, 8))

    axes[0].plot(z_vals * 100, E_y, 'b-', linewidth=1.5, label=r'$E_y$')
    axes[0].set_ylabel(r'$E_y$ (V/m)')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    axes[1].plot(z_vals * 100, H_x * 1e3, 'r-', linewidth=1.5, label=r'$H_x$ (mA/m)')
    axes[1].set_ylabel(r'$H_x$ (mA/m)')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    axes[2].plot(z_vals * 100, S_z / 1e3, 'g-', linewidth=1.5, label=r'$S_z$ (kW/m$^2$)')
    axes[2].set_xlabel(r'$z$ (cm)')
    axes[2].set_ylabel(r'$S_z$ (kW/m$^2$)')
    axes[2].legend(); axes[2].grid(True, alpha=0.3)

    axes[0].set_title(f'Uniform plane wave in free space: f={f/1e9:.0f} GHz, '
                      r'$E_0=$' + f'{E0:.0f} V/m')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/xiechufang/code/ch4_plane_wave_poynting.png', dpi=150)
    plt.show()

    # Time-average Poynting vector
    S_avg = (E0**2 / (2 * eta_0))
    print(f"Time-average Poynting vector: {S_avg:.3f} W/m^2")
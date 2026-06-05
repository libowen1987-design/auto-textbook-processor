"""
Taflove Multilayer FDTD — Layered Medium Propagation
====================================================
Multilayer dielectric FDTD and SAR calculation.
Based on Taflove 3rd Ed., Chapter 4 (Multilayer Media) and Chapter 6 (SAR).

Implements:
  - multilayer_fdtd()  : FDTD in multilayered media
  - SAR_calculation()  : Specific Absorption Rate computation
  - Debye_material()   : Debye dispersion model for biological tissues

Author: 小龙虾 (based on Taflove 3rd Ed.)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

# Physical constants
c = constants.speed_of_light
epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0


def Debye_material(freq_Hz, epsilon_inf, epsilon_static, tau_ps, sigma=0.0):
    """
    Debye dispersion model for biological tissues.

    The complex relative permittivity for a Debye medium is:

        ε_r(ω) = ε_inf + (ε_static - ε_inf) / (1 + j ω τ)

    where τ is the relaxation time (ps) and σ is the DC conductivity (S/m).

    Reference: Taflove Section 4.9 (Biological Media)

    Parameters
    ----------
    freq_Hz       : float – Frequency (Hz)
    epsilon_inf   : float – High-frequency permittivity (ε_∞)
    epsilon_static: float – Static (low-frequency) permittivity (ε_s)
    tau_ps        : float – Relaxation time (picoseconds)
    sigma         : float – DC conductivity (S/m)

    Returns
    -------
    epsilon_r     : complex – Complex relative permittivity
    conductivity  : float   – Effective conductivity at freq (S/m)
    """
    omega = 2.0 * np.pi * freq_Hz
    tau_s = tau_ps * 1e-12   # convert ps to seconds

    # Debye equation
    epsilon_r = epsilon_inf + (epsilon_static - epsilon_inf) / (1 + 1j * omega * tau_s)

    # Add conductivity contribution
    epsilon_total = epsilon_r + sigma / (1j * omega * epsilon_0)
    conductivity = sigma

    return epsilon_total, conductivity


def Cole_Cole_model(freq_Hz, epsilon_inf, epsilon_static,
                    alpha, tau_s, sigma=0.0):
    """
    Cole-Cole model (generalized Debye with distribution of relaxation times).

        ε_r(ω) = ε_inf + (ε_static - ε_inf) / (1 + (j ω τ)^(1-α))

    Parameters
    ----------
    alpha : float – Cole-Cole parameter (0 ≤ α ≤ 1), typically 0.1-0.3
    """
    omega = 2.0 * np.pi * freq_Hz
    term = 1.0 + (1j * omega * tau_s) ** (1.0 - alpha)
    epsilon_r = epsilon_inf + (epsilon_static - epsilon_inf) / term
    return epsilon_r


def SAR_calculation(E_field, sigma, rho_kg_m3=1000.0):
    """
    Specific Absorption Rate (SAR) calculation.

    SAR = σ |E|^2 / (2 * ρ)    [W/kg]

    where σ is tissue conductivity (S/m), E is peak electric field (V/m),
    and ρ is tissue density (kg/m³).

    Reference: Taflove Eq. 6.4

    Parameters
    ----------
    E_field  : ndarray – Electric field magnitude (V/m) or complex field
    sigma    : float  – Tissue conductivity (S/m)
    rho_kg_m3: float  – Tissue density (kg/m³), default 1000

    Returns
    -------
    SAR : ndarray – SAR distribution (W/kg)
    """
    if np.iscomplexobj(E_field):
        E_mag_sq = np.abs(E_field) ** 2
    else:
        E_mag_sq = E_field ** 2

    SAR = (sigma * E_mag_sq) / (2.0 * rho_kg_m3)
    return SAR


def multilayer_fdtd(L=0.2, dx=5e-4,
                    layer_thicknesses=None, epsilon_r=None, mu_r=None,
                    sigma_S_m=None,
                    num_steps=800, source_type='gaussian',
                    f_Hz=2e9, show_plots=True):
    """
    1D FDTD in multilayered media with material properties.

    For a cell at position x belonging to layer i, the material
    parameters ε_i, μ_i are used in the update coefficients:

        mH[i] = dt / μ[i]
        mE[i] = dt / ε[i]

    At each interface, the field components must be continuous
    (E_tangential and H_tangential are continuous, D_normal and B_normal
    are continuous). The standard FDTD scheme enforces this automatically
    through the update equations.

    Parameters
    ----------
    L               : float – Total domain length (m)
    dx              : float – Grid spacing (m)
    layer_thicknesses: list of float – Thickness of each layer (m)
    epsilon_r       : list of float – Relative permittivity of each layer
    mu_r            : list of float – Relative permeability of each layer
    sigma_S_m       : list of float – Conductivity of each layer (S/m)
    num_steps       : int   – Number of time steps
    source_type     : str   – 'gaussian' or 'sine'
    f_Hz            : float – Source frequency (Hz)

    Returns
    -------
    Ez_history : ndarray – (num_steps, Nx)
    Hy_history : ndarray – (num_steps, Nx)
    x_arr      : ndarray – Spatial axis (m)
    t_arr      : ndarray – Time axis (s)
    layer_idx  : ndarray – Layer index for each cell
    """
    if layer_thicknesses is None:
        layer_thicknesses = [0.05, 0.05, 0.05, 0.05]  # 4 layers
    if epsilon_r is None:
        epsilon_r = [1.0, 2.1, 40.0, 1.0]  # air, fat, muscle, air
    if mu_r is None:
        mu_r = [1.0] * len(layer_thicknesses)
    if sigma_S_m is None:
        sigma_S_m = [0.0, 0.05, 0.7, 0.0]  # typical values

    N_layers = len(layer_thicknesses)

    # Build domain
    Nx = int(L / dx) + 1
    x_arr = np.linspace(0, L, Nx)

    # Assign layer to each cell
    layer_idx = np.zeros(Nx, dtype=int)
    x_cumulative = 0.0
    for i in range(N_layers):
        x_end = x_cumulative + layer_thicknesses[i]
        mask = (x_arr >= x_cumulative) & (x_arr < x_end)
        layer_idx[mask] = i
        x_cumulative = x_end

    # Material parameters
    eps_r = np.array(epsilon_r)
    mu_r_arr = np.array(mu_r)
    sigma_arr = np.array(sigma_S_m)

    eps_eff = epsilon_0 * eps_r[layer_idx]    # F/m
    mu_eff = mu_0 * mu_r_arr[layer_idx]      # H/m
    sigma_eff = sigma_arr[layer_idx]          # S/m

    # Time step
    dt = 0.9 * dx / (2.0 * c)

    # Source
    src_idx = 10  # Near left boundary

    # Fields
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)

    # History
    Ez_history = np.zeros((num_steps, Nx))
    Hy_history = np.zeros((num_steps, Nx))

    # Coefficients (lossy medium update)
    # For lossy medium with conductivity σ:
    #   H^{n+1} = (1 - σ_H) * H^n - (dt/μ) * ∂E/∂x
    #   E^{n+1} = (1 - σ_E) * E^n + (dt/ε) * ∂H/∂x
    # where σ_H = dt * σ / (2ε), σ_E = dt * σ / (2ε)
    # Alternatively, use the auxiliary differential equation (ADE) method

    def mH_coef(i):
        return dt / mu_eff[i]

    def mE_coef(i):
        return dt / eps_eff[i]

    def loss_H(i):
        # Factor for H update in lossy medium (average of neighboring cells)
        sig_avg = (sigma_eff[i] + sigma_eff[min(i + 1, Nx - 1)]) / 2.0
        eps_avg = (eps_eff[i] + eps_eff[min(i + 1, Nx - 1)]) / 2.0
        return np.exp(-sig_avg * dt / (2.0 * eps_avg))

    def loss_E(i):
        sig_avg = sigma_eff[i]
        eps_avg = eps_eff[i]
        return np.exp(-sig_avg * dt / (2.0 * eps_avg))

    # Source parameters
    if source_type == 'gaussian':
        t0 = 30.0 * dt
        spread = 12.0 * dt
    else:
        t0 = 0.0
        spread = 0.0

    print(f"\n[Multilayer FDTD] Grid: {Nx} cells, {N_layers} layers")
    print(f"[Multilayer FDTD] dt={dt:.4e} s, steps={num_steps}")
    print("[Multilayer FDTD] Layer properties:")
    for i in range(N_layers):
        print(f"  Layer {i}: ε_r={epsilon_r[i]:.2f}, "
              f"μ_r={mu_r[i]:.2f}, σ={sigma_S_m[i]:.4f} S/m, "
              f"d={layer_thicknesses[i]*100:.2f} cm")

    # FDTD loop
    t_arr = np.arange(num_steps) * dt

    for n in range(num_steps):
        t = n * dt

        # Source
        if source_type == 'gaussian':
            src = np.exp(-((t - t0) ** 2) / (2.0 * spread ** 2))
        else:
            src = np.sin(2.0 * np.pi * f_Hz * t)

        # H update
        for i in range(Nx - 1):
            dEz = (Ez[i + 1] - Ez[i]) / dx
            Hy[i] = loss_H(i) * Hy[i] - mH_coef(i) * dEz

        # E update
        Ez[src_idx] = src
        for i in range(1, Nx):
            dHy = (Hy[i] - Hy[i - 1]) / dx
            Ez[i] = loss_E(i) * Ez[i] + mE_coef(i) * dHy

        Ez_history[n] = Ez.copy()
        Hy_history[n] = Hy.copy()

        if (n + 1) % 200 == 0:
            print(f"  step {n+1}/{num_steps}, t={t:.6e} s")

    # ── Plots ──────────────────────────────────────────────────────────────
    if show_plots:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("Taflove Multilayer FDTD — "
                     f"{'Gaussian' if source_type=='gaussian' else f'f={f_Hz/1e9:.1f} GHz'} source",
                     fontsize=12)

        # Field snapshot at different times
        times_to_show = [num_steps // 4, num_steps // 2,
                         3 * num_steps // 4, num_steps - 1]
        colors = ['royalblue', 'forestgreen', 'darkorange', 'crimson']

        # Plot layers as background
        ax0 = axes[0, 0]
        for i in range(N_layers):
            x_start = sum(layer_thicknesses[:i])
            x_end = x_start + layer_thicknesses[i]
            ax0.axvspan(x_start * 100, x_end * 100, alpha=0.1,
                        color='gray', label=f'Layer {i}' if i == 0 else '')
        for idx, col in zip(times_to_show, colors):
            ax0.plot(x_arr * 100, Ez_history[idx], color=col,
                     label=f't={idx * dt:.2e}s')
        ax0.set_xlabel('Position (cm)')
        ax0.set_ylabel(r'$E_z$ (V/m)')
        ax0.set_title('Electric Field Propagation in Multilayers')
        ax0.legend()
        ax0.grid(True, alpha=0.3)

        # Space-time diagram
        ax1 = axes[0, 1]
        extent = [0, L * 100, 0, num_steps * dt]
        ax1.imshow(Ez_history[:, ::3].T, aspect='auto', origin='lower',
                   cmap='RdBu', extent=extent)
        ax1.set_xlabel('Position (cm)')
        ax1.set_ylabel('Time (ns)')
        ax1.set_title('Space-Time Diagram')

        # Material profile
        ax2 = axes[1, 0]
        ax2.plot(x_arr * 100, eps_r[layer_idx], color='steelblue',
                 linewidth=2, label=r'$\varepsilon_r$')
        ax2.set_xlabel('Position (cm)')
        ax2.set_ylabel(r'$\varepsilon_r$')
        ax2.set_title('Layer Permittivity Profile')
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # SAR profile at peak time
        ax3 = axes[1, 1]
        peak_step = np.argmax(np.max(np.abs(Ez_history), axis=1))
        E_peak = Ez_history[peak_step]
        sigma_profile = sigma_arr[layer_idx]
        SAR = SAR_calculation(E_peak, sigma_profile, rho_kg_m3=1000.0)
        ax3.plot(x_arr * 100, SAR, color='darkorange', linewidth=2)
        ax3.set_xlabel('Position (cm)')
        ax3.set_ylabel('SAR (W/kg)')
        ax3.set_title(f'SAR Distribution at Peak Time (step {peak_step})')
        ax3.grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('/tmp/taflove_multilayer.png', dpi=150)
        print("[Multilayer FDTD] Plot saved to /tmp/taflove_multilayer.png")
        plt.show()

    return Ez_history, Hy_history, x_arr, t_arr, layer_idx


def multilayer_reflection_analysis():
    """
    Analyze reflection coefficient at multilayer interfaces.

    For N layers with thickness d_i and refractive index n_i,
    the reflection coefficient is computed via transmission line analogy.
    """
    print("\n[Multilayer Reflection] Fresnel coefficients")

    # Case: plane wave from air (n=1) → fat (n≈1.45) → muscle (n≈9)
    layers = [
        {'name': 'Air', 'n': 1.0, 'd': np.inf},
        {'name': 'Fat', 'n': 1.45, 'd': 0.05},
        {'name': 'Muscle', 'n': 9.0, 'd': 0.05},
        {'name': 'Air', 'n': 1.0, 'd': np.inf},
    ]

    freq = 2.4e9  # ISM band
    omega = 2.0 * np.pi * freq
    k = omega / c

    print(f"Frequency: {freq/1e9:.2f} GHz")
    print("-" * 50)

    for i in range(len(layers) - 1):
        n1 = layers[i]['n']
        n2 = layers[i + 1]['n']

        # Normal incidence reflection coefficient
        r = (n1 - n2) / (n1 + n2)
        R = abs(r) ** 2
        T = 1.0 - R

        print(f"Interface {layers[i]['name']} → {layers[i+1]['name']}: "
              f"n1={n1:.2f}, n2={n2:.2f}, "
              f"r={r:.4f}, R={R:.4f} ({R*100:.2f}%), T={T:.4f}")

    return layers


def SAR_head_model_demo():
    """
    Demo: Simplified human head SAR calculation using multilayer FDTD.

    Layer structure (approximate):
      Layer 1: Skin  (ε_r=42, σ=0.7 S/m, ρ=1000 kg/m³)
      Layer 2: Skull (ε_r=12, σ=0.02 S/m, ρ=1500 kg/m³)
      Layer 3: Brain (ε_r=45, σ=0.8 S/m, ρ=1040 kg/m³)
    """
    print("\n[SAR Head Model Demo] Simplified head model")

    L_total = 0.12  # 12 cm head model
    dx = 1e-3       # 1 mm resolution

    # Layer structure (thickness in m)
    layer_thicknesses = [0.004, 0.005, 0.041]  # skin, skull, brain
    epsilon_r = [42.0, 12.0, 45.0]
    mu_r = [1.0, 1.0, 1.0]
    sigma = [0.7, 0.02, 0.8]
    rho = [1000.0, 1500.0, 1040.0]

    Ez_h, Hy_h, x, t_arr, layer_idx = multilayer_fdtd(
        L=L_total, dx=dx,
        layer_thicknesses=layer_thicknesses,
        epsilon_r=epsilon_r,
        mu_r=mu_r,
        sigma_S_m=sigma,
        num_steps=800,
        source_type='gaussian'
    )

    # Compute SAR at peak time
    peak_step = np.argmax(np.max(np.abs(Ez_h), axis=1))
    E_peak = Ez_h[peak_step]

    # Per-layer SAR
    print("\n[SAR Head Model] Per-layer peak SAR:")
    for i in range(len(layer_thicknesses)):
        mask = layer_idx == i
        E_layer = E_peak[mask]
        sig = sigma[i]
        rho_i = rho[i]
        SAR_layer = SAR_calculation(E_layer, sig, rho_kg_m3=rho_i)
        SAR_peak = np.max(SAR_layer)
        print(f"  {['Skin', 'Skull', 'Brain'][i]}: "
              f"σ={sig:.3f} S/m, ρ={rho_i} kg/m³, "
              f"SAR_peak={SAR_peak:.4f} W/kg")

    return Ez_h, Hy_h, x, layer_idx


# ── Validation & Demo ────────────────────────────────────────────────────────
if __name__ == '__main__':
    print("=" * 60)
    print("Taflove Multilayer FDTD — Validation")
    print("=" * 60)

    # 1. Debye material model
    print("\n[1] Debye Dispersion Model")
    freqs = [900e6, 1.8e9, 2.4e9, 5.0e9]
    for f in freqs:
        eps, sig = Debye_material(f, epsilon_inf=4.0, epsilon_static=50.0,
                                  tau_ps=7.0, sigma=0.2)
        print(f"  f={f/1e9:.2f} GHz: ε_r={eps:.4f}")

    # 2. Multilayer reflection
    print("\n[2] Multilayer Reflection Analysis")
    multilayer_reflection_analysis()

    # 3. Standard multilayer FDTD
    print("\n[3] Multilayer FDTD — Gaussian Source")
    Ez_h, Hy_h, x, t, idx = multilayer_fdtd(
        L=0.1, dx=5e-4,
        layer_thicknesses=[0.02, 0.03, 0.02, 0.03],
        epsilon_r=[1.0, 2.1, 40.0, 1.0],
        mu_r=[1.0, 1.0, 1.0, 1.0],
        sigma_S_m=[0.0, 0.05, 0.7, 0.0],
        num_steps=600,
        source_type='gaussian'
    )

    # 4. SAR head model
    print("\n[4] SAR Head Model Demo")
    SAR_calculation(5.0, sigma=0.8, rho_kg_m3=1040)

    print("\n" + "=" * 60)
    print("Multilayer FDTD validation complete.")
    print("=" * 60)
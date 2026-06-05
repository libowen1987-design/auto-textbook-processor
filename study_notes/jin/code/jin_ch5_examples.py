"""
jin_ch5_examples.py
Jin CEM 2nd Ed., Chapter 5: Fields and Waves in Rectangular Coordinates
Examples: waveguide modes, cutoff frequency, cavity resonance, field plots.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

epsilon_0 = constants.epsilon_0
mu_0 = constants.mu_0
c_light = constants.c
eta_0 = np.sqrt(mu_0 / epsilon_0)
pi = np.pi


def rectangular_waveguide_cutoff():
    """Plot cutoff frequencies for TE/TM modes in rectangular waveguide."""
    a = 0.02286  # m — WR-90 waveguide (X-band)
    b = 0.01016  # m
    
    mode_count = 6
    modes = []
    for m in range(4):
        for n in range(4):
            if m == 0 and n == 0:
                continue
            k_c = np.sqrt((m * pi / a)**2 + (n * pi / b)**2)
            f_c = k_c * c_light / (2 * pi)
            modes.append((m, n, f_c, 'TE' if m > 0 or n > 0 else 'TEM'))
    
    modes.sort(key=lambda x: x[2])
    modes = modes[:mode_count]
    
    names = [f"{t}$_{{{m}{n}}}$" for m, n, f, t in modes]
    freqs = [f / 1e9 for _, _, f, _ in modes]
    
    fig, ax = plt.subplots(figsize=(8, 4))
    colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(modes)))
    bars = ax.barh(names, freqs, color=colors, alpha=0.8)
    
    for bar, fc in zip(bars, freqs):
        ax.text(fc + 0.1, bar.get_y() + bar.get_height()/2,
                f"{fc:.2f} GHz", va='center', fontsize=9)
    
    ax.set_xlabel("Cutoff Frequency (GHz)", fontsize=11)
    ax.set_title(f"Rectangular Waveguide Cutoff Frequencies "
                 f"(WR-90: {a*1e3:.2f}$\\times${b*1e3:.2f} mm)", fontsize=12)
    ax.set_xlim(0, max(freqs) + 2)
    ax.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch5_fig_cutoff.png",
                dpi=150)
    plt.close()
    print("[OK] Waveguide cutoff plot saved.")
    
    print("=" * 55)
    print("Rectangular Waveguide Cutoff Frequencies (WR-90)")
    print("=" * 55)
    for name, fc in zip(names, freqs):
        print(f"  {name:8s}: {fc:.2f} GHz")
    print(f"  Dominant mode: {names[0]} at {freqs[0]:.2f} GHz")
    print()


def te10_field_plot():
    """Plot TE10 mode fields in a rectangular waveguide cross-section."""
    a = 0.02286
    b = 0.01016
    freq = 10e9
    k = 2 * pi * freq / c_light
    k_c = pi / a
    k_z = np.sqrt(k**2 - k_c**2 + 0j)
    
    nx, ny = 40, 20
    x = np.linspace(0, a, nx)
    y = np.linspace(0, b, ny)
    X, Y = np.meshgrid(x, y)
    
    H_z = np.cos(pi * X / a)  # TE10 Hz
    
    # Transverse fields: E_y = j*omega*mu/k_c^2 * dHz/dx
    E_y = np.zeros_like(H_z)
    E_y[:, 1:-1] = np.real((1j * k * eta_0 * pi / (k_c**2 * a)) * (-np.sin(pi * X[:, 1:-1] / a)))
    
    H_x = np.zeros_like(H_z)
    H_x[:, 1:-1] = np.real((1j * k_z * pi / (k_c**2 * a)) * (np.sin(pi * X[:, 1:-1] / a)))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    
    # Contour of H_z
    c1 = ax1.contourf(X*1e3, Y*1e3, np.real(H_z), levels=20, cmap='RdBu')
    ax1.set_title("TE$_{10}$: $H_z$ (contour)", fontsize=11)
    ax1.set_xlabel("x (mm)", fontsize=10)
    ax1.set_ylabel("y (mm)", fontsize=10)
    ax1.set_aspect('equal')
    plt.colorbar(c1, ax=ax1, shrink=0.8)
    
    # Quiver of transverse fields
    skip = 3
    ax2.quiver(X[::skip, ::skip]*1e3, Y[::skip, ::skip]*1e3,
               np.real(H_x[::skip, ::skip]), np.real(E_y[::skip, ::skip]),
               alpha=0.7)
    ax2.set_title("TE$_{10}$: $\\mathbf{E}_t$ and $\\mathbf{H}_t$", fontsize=11)
    ax2.set_xlabel("x (mm)", fontsize=10)
    ax2.set_ylabel("y (mm)", fontsize=10)
    ax2.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch5_fig_TE10.png",
                dpi=150)
    plt.close()
    print("[OK] TE10 field plot saved.")


def cavity_resonance():
    """Rectangular cavity resonant frequencies."""
    a = 0.02286  # m
    b = 0.01016  # m
    d = 0.02     # m cavity length
    
    modes = []
    for m in range(3):
        for n in range(3):
            for p in range(3):
                if m == 0 and n == 0:
                    continue
                if p == 0:
                    continue
                k_mnp = np.sqrt((m*pi/a)**2 + (n*pi/b)**2 + (p*pi/d)**2)
                f = c_light * k_mnp / (2 * pi)
                modes.append((m, n, p, 'TE' if m > 0 or n > 0 else 'TM', f/1e9))
    
    modes.sort(key=lambda x: x[4])
    
    print("=" * 55)
    print("Rectangular Cavity Resonant Frequencies")
    print("=" * 55)
    print(f"  Dimensions: a={a*1e3:.2f}, b={b*1e3:.2f}, d={d*1e3:.2f} mm")
    for m, n, p, t, f in modes[:8]:
        print(f"  {t}$_{{{m}{n}{p}}}$: {f:.2f} GHz")
    print()
    
    # Plot first few modes
    names = [f"{t}$_{{{m}{n}{p}}}$" for m, n, p, t, _ in modes[:8]]
    freqs = [f for _, _, _, _, f in modes[:8]]
    
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.bar(names, freqs, color='steelblue', alpha=0.8)
    for name, fc in zip(names, freqs):
        ax.text(name, fc + 0.2, f"{fc:.2f}", ha='center', fontsize=8)
    ax.set_ylabel("Frequency (GHz)", fontsize=11)
    ax.set_title("Rectangular Cavity Resonant Frequencies", fontsize=12)
    ax.set_ylim(0, max(freqs) + 2)
    ax.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch5_fig_cavity.png",
                dpi=150)
    plt.close()
    print("[OK] Cavity resonance plot saved.")


def waveguide_dispersion():
    """Dispersion diagram for rectangular waveguide modes."""
    a = 0.02286
    b = 0.01016
    
    f = np.linspace(6e9, 18e9, 500)
    
    fig, ax = plt.subplots(figsize=(7, 4.5))
    
    colors = plt.cm.tab10(np.linspace(0, 1, 6))
    
    for idx, (m, n) in enumerate([(1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (3, 0)]):
        k_c = np.sqrt((m * pi / a)**2 + (n * pi / b)**2)
        f_c = k_c * c_light / (2 * pi)
        
        beta = np.zeros_like(f)
        mask = f > f_c
        beta[mask] = np.sqrt((2 * pi * f[mask] / c_light)**2 - k_c**2)
        
        v_p = 2 * pi * f / beta
        v_p[~mask] = np.nan
        v_g = np.gradient(2 * pi * f, beta)
        
        label = f"TE$_{{{m}{n}}}$ ($f_c={f_c/1e9:.2f}$ GHz)"
        ax.plot(f/1e9, beta, color=colors[idx], linewidth=1.2, label=label)
        
        # Light line
        ax.plot(f/1e9, 2*pi*f/c_light, 'k--', linewidth=0.8, alpha=0.4)
    
    ax.set_xlabel("Frequency (GHz)", fontsize=11)
    ax.set_ylabel("$\\beta$ (rad/m)", fontsize=11)
    ax.set_title("Waveguide Dispersion Diagram", fontsize=12)
    ax.legend(fontsize=8, ncol=2)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig("/home/ubuntu/.openclaw/workspace/textbooks/jin/figures/jin_ch5_fig_dispersion.png",
                dpi=150)
    plt.close()
    print("[OK] Dispersion diagram saved.")


def main():
    print()
    print("╔══════════════════════════════════════════════════════╗")
    print("║   Jin CEM 2nd Ed. — Ch5 Example Code               ║")
    print("║   Fields and Waves in Rectangular Coordinates      ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()
    
    rectangular_waveguide_cutoff()
    te10_field_plot()
    cavity_resonance()
    waveguide_dispersion()
    
    print("All Ch5 examples completed successfully.")

if __name__ == "__main__":
    main()

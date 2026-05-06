"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter IV: Static Magnetic Field

Key equations (Landau §27-§33):
1. B = H + 4πM  (magnetic induction relation)
2. B = μH = (1 + 4πχ)H  (linear isotropic medium)
3. div B = 0,  curl H = (4π/c)j  (field equations)
4. Magnetic scalar potential: H = -grad ψ (when j=0)
5. Magnetostatic energy: U = (1/8π) ∫ H·B dV
6. Self-inductance: U = (1/2c²) L I²

Landau §27: Constant magnetic field in matter
Landau §29: Magnetic field of a constant current
Landau §32: Energy of a system of currents
Landau §33: Self-inductance of linear conductors
"""

import numpy as np
import matplotlib.pyplot as plt


def solenoid_magnetic_field():
    """
    Compute B and H inside a long solenoid (Landau §29).
    
    For a solenoid with n turns per unit length, carrying current I:
    H_z = (4π/c) n I   (inside, along axis)
    B_z = μ H_z = μ_r μ0 H_z
    
    Outside the solenoid, the field is approximately zero for an ideal infinite solenoid.
    For a finite-length solenoid, use the exact formula.
    
    This example compares:
    - Ideal infinite solenoid (analytical)
    - Finite solenoid with end effects (numerical integration)
    """
    mu0 = 4 * np.pi * 1e-7  # H/m
    c = 3e10  # cm/s (Gaussian units conversion factor)

    # Solenoid parameters
    n_turns_per_m = 5000  # turns per meter
    radius = 2.0  # cm
    length = 20.0  # cm
    current = 1.0  # A

    # --- Ideal infinite solenoid ---
    # In Gaussian units: H = (4π/c) n I  (Oe)
    # SI: H = n I  (A/m)
    n_SI = n_turns_per_m  # turns/m
    H_infinite_SI = n_SI * current  # A/m
    B_infinite = mu0 * H_infinite_SI  # Tesla

    # --- Field along axis of finite solenoid (Biot-Savart numerical) ---
    n_turns = int(n_turns_per_m * length / 100)  # total turns
    z_axis = np.linspace(-0.5 * length, 0.5 * length, 500)  # cm

    def Bz_on_axis(z, R, n_tot, L):
        """B_z at position z along axis of solenoid with R radius, L length."""
        # Divide solenoid into n_tot filamentary rings
        dz = L / n_tot
        B_total = 0.0
        for i in range(n_tot):
            z_i = -L/2 + (i + 0.5) * dz  # position of i-th ring (cm)
            # Field from ring at axial position z:
            # dB_z = (2πR² I dz/L) / (c * (R² + (z-z_i)²)^(3/2))  [Gaussian]
            # In SI: dB_z = (mu0/2) * R² I dz / ((R²+(z-z_i)²)^(3/2))
            r_sq = R**2 + (z - z_i)**2
            dB = (mu0 / 2) * (R**2 * current * dz / 100) / (r_sq ** 1.5)
            B_total += dB * 100**3  # convert m->cm
        return B_total  # Tesla

    # Gaussian units: B(Oe) -> convert to SI
    B_axis_finite = np.array([Bz_on_axis(z, radius, 100, length) for z in z_axis])

    # Convert Gaussian H (Oe) to SI A/m: 1 Oe = 1000/(4π) A/m ≈ 79.577 A/m
    H_axis_finite_Oe = np.array([(4*np.pi / c) * n_turns_per_m * current * 100 *
                                  (1.0 if -length/2 <= z <= length/2 else 0.0)
                                  for z in z_axis])
    H_axis_finite_SI = H_axis_finite_Oe * (1000 / (4 * np.pi))

    fig, axes = plt.subplots(2, 1, figsize=(12, 9))

    ax = axes[0]
    ax.plot(z_axis, B_axis_finite * 1e3, 'b-', lw=2, label='Finite solenoid (numerical)')
    ax.axhline(B_infinite * 1e3, color='r', ls='--', lw=2, label=f'Ideal infinite: B={B_infinite*1e3:.2f} mT')
    ax.axvline(-length/2, color='gray', ls=':', lw=1)
    ax.axvline(length/2, color='gray', ls=':', lw=1, label=f'Solenoid ends at ±{length/2} cm')
    ax.set_xlabel('z (cm)')
    ax.set_ylabel(r'$B_z$ (mT)')
    ax.set_title(fr'Solenoid: $n$={n_turns_per_m}/m, $R$={radius}cm, $I$={current}A')
    ax.legend()
    ax.grid(True, alpha=0.3)

    ax2 = axes[1]
    ax2.plot(z_axis, H_axis_finite_SI, 'g-', lw=2, label=r'$H_z$ (finite, SI A/m)')
    ax2.axhline(H_infinite_SI, color='orange', ls='--', lw=2, label=f'$H$ ideal = {H_infinite_SI:.0f} A/m')
    ax2.axvline(-length/2, color='gray', ls=':', lw=1)
    ax2.axvline(length/2, color='gray', ls=':', lw=1)
    ax2.set_xlabel('z (cm)')
    ax2.set_ylabel(r'$H_z$ (A/m)')
    ax2.set_title(r'Magnetic field $H_z$ along axis')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch4_solenoid.png'
    fig.savefig(fname, dpi=150)
    plt.close()

    print(f"[landau_ch4] Ideal infinite solenoid: H={H_infinite_SI:.0f} A/m, B={B_infinite*1e3:.2f} mT")
    print(f"[landau_ch4] Field at center (finite): B={B_axis_finite[len(z_axis)//2]*1e3:.2f} mT")
    print(f"[landau_ch4] Plot saved.")


def demagnetization_factor_ellipsoid():
    """
    Compute the demagnetizing factor N for ellipsoids of revolution
    and verify that N_x + N_y + N_z = 4π (Gaussian) / 1 (SI).
    
    Landau §27-§28: The demagnetizing field H_d = -N M for a uniformly
    magnetized ellipsoid. The effective field inside is H_eff = H_ext - N M.
    
    For a sphere: N_x = N_y = N_z = 4π/3  (Gaussian) / 1/3 (SI)
    For a needle (prolate spheroid, c>>a): N_z → 0, N_x = N_y → 2π
    For a disk (oblate spheroid, c<<a): N_z → 4π, N_x = N_y → 0
    """
    pass  # demagnetizing factor formulas are direct

    def demagnetizing_prolate(eccentricity):
        """
        Demagnetizing factors for prolate spheroid (a=a=b < c).
        e = sqrt(1 - a²/c²) is the eccentricity.
        
        N_c = (1 - e²)/(2*e³) * (ln((1+e)/(1-e)) - 2*e)
        N_a = (1 - N_c) / 2
        """
        if eccentricity < 1e-10:
            return 2/3, 2/3, 2/3  # sphere limit

        e = eccentricity
        N_c = (1 - e**2) / (2 * e**3) * (np.log((1 + e) / (1 - e)) - 2 * e)
        N_a = (1 - N_c) / 2.0
        return N_a, N_a, N_c  # N_x, N_y, N_z

    # Test cases
    print("[landau_ch4] Demagnetizing factors (Gaussian units):")
    print(f"[landau_ch4] Sphere (e=0): N_x=N_y=N_z = 4π/3 = {4*np.pi/3:.4f}")
    N_a, N_b, N_c = demagnetizing_prolate(0.0)
    print(f"[landau_ch4]   → computed: {N_a:.4f}, {N_b:.4f}, {N_c:.4f}")

    # Prolate spheroid: needle with c/a = ratio
    ratios = [1.0, 2.0, 5.0, 10.0, 50.0]
    print(f"\n[landau_ch4] Prolate spheroid (c/a ratio → needle):")
    for ratio in ratios:
        e = np.sqrt(1 - 1/ratio**2)
        N_a, N_b, N_c = demagnetizing_prolate(e)
        print(f"[landau_ch4]   c/a={ratio}: e={e:.4f}, N_a={N_a:.4f}, N_c={N_c:.4f}, sum={N_a+N_b+N_c:.4f} (expect 4π={4*np.pi:.4f})")

    # Oblate spheroid
    def demagnetizing_oblate(eccentricity):
        """
        Demagnetizing factors for oblate spheroid (a=b > c).
        e = sqrt(1 - c²/a²)
        N_c = (1/(2*e³)) * (2*e*(1+e²) - ln((1+e)/(1-e)))
        N_a = (1 - N_c)/2
        """
        if eccentricity < 1e-10:
            return 2/3, 2/3, 2/3
        e = eccentricity
        N_c = (1/(2*e**3)) * (2*e*(1+e**2) - np.log((1+e)/(1-e)))
        N_a = (1 - N_c) / 2.0
        return N_a, N_a, N_c

    print(f"\n[landau_ch4] Oblate spheroid (a/c ratio → disk):")
    for ratio in [1.0, 2.0, 5.0, 10.0, 50.0]:
        e = np.sqrt(1 - 1/ratio**2)
        N_a, N_b, N_c = demagnetizing_oblate(e)
        print(f"[landau_ch4]   a/c={ratio}: e={e:.4f}, N_a={N_a:.4f}, N_c={N_c:.4f}, sum={N_a+N_b+N_c:.4f}")

    # Plot N vs c/a ratio
    ratios = np.logspace(-1, 2, 200)  # 0.1 to 100
    N_z_prolate = []
    N_x_prolate = []
    for ratio in ratios:
        e = np.sqrt(1 - 1/ratio**2) if ratio > 1 else 0.0
        if ratio == 1.0:
            e = 0.0
        if e < 1e-10:
            N_a = N_b = N_c = 2*np.pi/3 * 2  # In Gaussian: 4π/3 for sphere
        else:
            e_val = np.sqrt(1 - 1/ratio**2) if ratio > 1 else 0.0
            e_val = max(0.0, min(e_val, 1.0 - 1e-10))
            N_c = (1 - e_val**2)/(2*e_val**3)*(np.log((1+e_val)/(1-e_val)) - 2*e_val) if e_val > 1e-10 else 2*np.pi/3*2
            N_a = (1 - N_c)/2 if e_val > 1e-10 else 2*np.pi/3*2
        N_z_prolate.append(N_c if ratio > 1 else 2*np.pi/3*2)
        N_x_prolate.append(N_a if ratio > 1 else 2*np.pi/3*2)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    ax.semilogx(ratios, N_z_prolate, 'b-', lw=2, label=r'$N_z$ (along c-axis)')
    ax.semilogx(ratios, N_x_prolate, 'r--', lw=2, label=r'$N_x=N_y$ (equatorial)')
    ax.axhline(4*np.pi/3, color='k', ls=':', lw=1, label=r'$4\pi/3$ (sphere)')
    ax.axvline(1.0, color='gray', ls=':', lw=1, label='Sphere (c/a=1)')
    ax.set_xlabel(r'Sem-axis ratio $c/a$ (prolate, $c>a$)')
    ax.set_ylabel(r'Demagnetizing factor $N$ (Gaussian)')
    ax.set_title(r'Landau §27: Demagnetizing factors for prolate spheroid')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Effective permeability with demagnetization
    mu0 = 4*np.pi*1e-7
    mu_r_values = [10, 100, 1000]  # relative permeability
    H_ext = 1e4  # A/m applied field
    M_s_values = [1e4, 1e5, 1e6]  # A/m saturation magnetization

    ax2 = axes[1]
    for mu_r in mu_r_values:
        # Effective B: B = μ0 μ_r H_eff where H_eff = H_ext - N M
        # For linear: M = χ H_eff = (μ_r - 1)/4π * H_eff (Gaussian)
        # In SI: M = (μ_r - 1)/μ0 * H_eff
        chi = mu_r - 1
        # SI formula: M = χ / (1 + Nχ) * H_ext
        N_sphere = 1/3
        M_eff = chi / (1 + N_sphere * chi) * H_ext
        B_eff = mu0 * (H_ext + M_eff)
        label = rf'$\mu_r$={mu_r}'
        ax2.semilogx(ratios, B_eff * 1e3 * np.ones_like(ratios), label=label)

    ax2.set_xlabel(r'Sem-axis ratio $c/a$')
    ax2.set_ylabel(r'$B$ (mT) - effective field')
    ax2.set_title(r'$B$-field in ellipsoid vs shape (constant $H_{ext}$)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch4_demagnetization.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch4] Plot saved.")


def magnetic_energy_and_inductance():
    """
    Compute magnetic energy and self-inductance of a solenoid (Landau §32-§33).
    
    Energy: U = (1/2c²) L I²  (Gaussian)
            U = (1/2) L I²   (SI)
    
    Self-inductance of solenoid:
    L = (4π μ N² A) / l  (Gaussian)
    L = μ0 μ_r N² A / l  (SI)
    where A = cross-sectional area, l = length, N = total turns
    """
    mu0 = 4*np.pi*1e-7

    # Solenoid: N turns, length l, area A
    N = 1000
    l = 0.1  # m
    A = np.pi * (0.02)**2  # m², radius 2 cm
    mu_r = 1.0  # air core

    # SI self-inductance
    L_SI = mu0 * mu_r * N**2 * A / l  # Henry
    I = 1.0  # A
    U_SI = 0.5 * L_SI * I**2  # Joules

    print(f"[landau_ch4] Solenoid: N={N}, l={l*100:.0f}cm, R=2cm")
    print(f"[landau_ch4] Self-inductance L = {L_SI*1e6:.2f} μH")
    print(f"[landau_ch4] Magnetic energy at I=1A: U = {U_SI*1e3:.3f} mJ")

    # Compare with field energy: U = (1/2μ0) ∫ B² dV
    B = mu0 * mu_r * N/l * I
    V = A * l
    U_field = B**2 / (2 * mu0) * V  # SI: B²/2μ0 per m³
    print(f"[landau_ch4] Field energy: U = {U_field*1e3:.3f} mJ  (B={B*1e3:.1f} mT)")
    print(f"[landau_ch4] Match: {abs(U_SI - U_field)/U_field*100:.1f}% difference")

    # Plot energy vs current
    currents = np.linspace(0, 5, 200)
    energies = 0.5 * L_SI * currents**2 * 1e3  # mJ

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.plot(currents, energies, 'b-', lw=2)
    ax.set_xlabel(r'Current $I$ (A)')
    ax.set_ylabel(r'Magnetic energy $U$ (mJ)')
    ax.set_title(fr'Landau §32: Magnetic energy $U=\frac{{1}}{{2}}LI^2$, L={L_SI*1e6:.1f} μH')
    ax.grid(True, alpha=0.3)

    # Field energy density map inside solenoid
    ax2 = axes[1]
    r = np.linspace(0, 0.02, 100)
    z = np.linspace(-0.05, 0.05, 100)
    R, Z = np.meshgrid(r, z)
    B_rz = mu0 * mu_r * N/l * I * np.ones_like(R)  # uniform inside
    u = B_rz**2 / (2 * mu0) * 1e3  # mJ/m³
    im = ax2.pcolormesh(r*100, z*100, np.ones_like(Z) * u, cmap='hot', shading='auto')
    ax2.set_xlabel('r (cm)')
    ax2.set_ylabel('z (cm)')
    ax2.set_title(r'Energy density $u = B^2/2\mu_0$ inside solenoid (mJ/m³)')
    plt.colorbar(im, ax=ax2, label='mJ/m³')

    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch4_inductance.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch4] Plot saved.")


if __name__ == '__main__':
    solenoid_magnetic_field()
    demagnetization_factor_ellipsoid()
    magnetic_energy_and_inductance()

"""
harrington_waveguide.py
=======================
Waveguide mode analysis and cavity resonance.
Based on Harrington, "Time-Harmonic Electromagnetic Fields", Ch. 5-7.

Topics:
    - rectangular_waveguide_modes()  : Rectangular waveguide TE/TM modes
    - circular_waveguide_modes()     : Circular waveguide modes
    - waveguide_dispersion()         : Plot dispersion curves ω vs β
    - cavity_modes()                 : Cavity resonator resonant frequencies

Author: Computational Electromagnetics Group
"""

import numpy as np
from scipy.constants import mu_0, epsilon_0, pi, c, inch
from scipy.linalg import solve
from scipy.optimize import brentq, newton
import matplotlib.pyplot as plt

# Waveguide module-wide defaults
f_0 = 3e9          # 3 GHz
omega_0 = 2 * np.pi * f_0
k_0 = omega_0 * np.sqrt(mu_0 * epsilon_0)


# -----------------------------------------------------------------
# Rectangular Waveguide
# -----------------------------------------------------------------

def rectangular_waveguide_modes(a: float, b: float,
                                f_range: tuple = (1e9, 20e9),
                                num_modes: int = 5,
                                verbose: bool = True):
    """
    Compute TE and TM modes for rectangular waveguide (Harrington Ch. 5).

    For a waveguide of width a (x-direction) and height b (y-direction):

    TE_mn / TM_mn cutoff wavenumbers:
        k_c = (mπ/a)² + (nπ/b)²

    Cutoff frequency:
        f_c = (c/2) * sqrt( (m/a)² + (n/b)² )

    For TE: m,n not both zero
    For TM: m,n not both zero (but m=0,n=0 gives no mode for TE)

    Propagation constant:
        β = sqrt(k² - k_c²)   for f > f_c (propagating)
        β = j * sqrt(k_c² - k²)  for f < f_c (evanescent)

    Parameters
    ----------
    a : float
        Waveguide width in x-direction (m).
    b : float
        Waveguide height in y-direction (m).
    f_range : tuple
        (f_min, f_max) frequency range to analyze.
    num_modes : int
        Number of lowest-order modes to return.
    verbose : bool

    Returns
    -------
    modes : list of dict
        Each dict: {'type': 'TE'/'TM', 'm': int, 'n': int,
                    'f_c': float, 'name': str}
    """
    c_val = c
    modes = []

    for m in range(num_modes + 2):
        for n in range(num_modes + 2):
            if m == 0 and n == 0:
                continue
            # TE modes: m,n not both zero
            k_c_sq = (m * pi / a)**2 + (n * pi / b)**2
            f_c = c_val / 2 * np.sqrt((m / a)**2 + (n / b)**2)
            modes.append({
                'type': 'TE',
                'm': m,
                'n': n,
                'k_c': np.sqrt(k_c_sq),
                'f_c': f_c,
                'name': f'TE_{m}{n}'
            })
            if m > 0 and n > 0:
                # TM modes (m,n > 0)
                modes.append({
                    'type': 'TM',
                    'm': m,
                    'n': n,
                    'k_c': np.sqrt(k_c_sq),
                    'f_c': f_c,
                    'name': f'TM_{m}{n}'
                })

    # Sort by cutoff frequency
    modes = sorted(modes, key=lambda x: x['f_c'])

    if verbose:
        print(f"\n[Rectangular WG] a = {a*100:.2f} cm, b = {b*100:.2f} cm")
        print(f"  Dominant mode (lowest f_c):")
        dom = modes[0]
        print(f"    {dom['name']} @ f_c = {dom['f_c']/1e9:.4f} GHz")
        print(f"  First {min(num_modes, len(modes))} modes:")
        for m in modes[:num_modes]:
            print(f"    {m['name']:6s}  f_c = {m['f_c']/1e9:.4f} GHz")

    return modes


def rectangular_wg_field_dist(a: float, b: float,
                              m: int, n: int,
                              mode_type: str = 'TE',
                              f: float = 3e9,
                              num_pts: int = 51,
                              verbose: bool = True):
    """
    Compute E or H field distribution for a rectangular WG mode.

    For TE_mn (Harrington Eq. 5-37):
        H_z = H_0 * cos(mπx/a) * cos(nπy/b) * e^(-jβz)
    Electric field components derived from Maxwell's equations.

    Parameters
    ----------
    a, b : float
        Waveguide dimensions (m).
    m, n : int
        Mode indices.
    mode_type : str
        'TE' or 'TM'.
    f : float
        Operating frequency.
    num_pts : int
        Grid resolution.
    verbose : bool

    Returns
    -------
    X, Y : np.ndarray
        Grid coordinates.
    E_components : dict
        Field component values.
    """
    omega = 2 * np.pi * f
    k = omega * np.sqrt(mu_0 * epsilon_0)

    # Cutoff wavenumber
    k_c = np.sqrt((m * pi / a)**2 + (n * pi / b)**2)

    if k <= k_c:
        if verbose:
            print(f"  [WARNING] f = {f/1e9:.2f} GHz < f_c = {k_c*c/(2*pi)/1e9:.2f} GHz (evanescent)")
        return None, None, None

    beta = np.sqrt(k**2 - k_c**2)

    # Cross-section grid
    x = np.linspace(0, a, num_pts)
    y = np.linspace(0, b, num_pts)
    X, Y = np.meshgrid(x, y)

    if mode_type == 'TE':
        # TE mode: H_z is primary
        H0 = 1.0  # amplitude
        kx = m * pi / a
        ky = n * pi / b

        # E_x, E_y from Maxwell (for z=0 cross-section)
        # At z=0 plane: E_x = -j ω μ₀ / k_c² * (nπ/b) * H_0 * cos(kx*x)*sin(ky*y)
        # E_y = +j ω μ₀ / k_c² * (mπ/a) * H_0 * sin(kx*x)*cos(ky*y)
        denom = k_c**2 + 1e-12
        E_x = -1j * omega * mu_0 / denom * (n * pi / b) * H0 * np.cos(kx * X) * np.sin(ky * Y)
        E_y = 1j * omega * mu_0 / denom * (m * pi / a) * H0 * np.sin(kx * X) * np.cos(ky * Y)
        E_z = np.zeros_like(X)  # TE modes have no E_z

        H_z = H0 * np.cos(kx * X) * np.cos(ky * Y)

        E_components = {
            'E_x': E_x,
            'E_y': E_y,
            'E_z': E_z,
            'H_z': H_z
        }
    else:  # TM
        # TM mode: E_z is primary
        E0 = 1.0
        kx = m * pi / a
        ky = n * pi / b

        E_z = E0 * np.sin(kx * X) * np.sin(ky * Y)
        E_x = -1j * beta / (k_c**2 + 1e-12) * kx * E0 * np.cos(kx * X) * np.sin(ky * Y)
        E_y = -1j * beta / (k_c**2 + 1e-12) * ky * E0 * np.sin(kx * X) * np.cos(ky * Y)

        E_components = {
            'E_x': E_x,
            'E_y': E_y,
            'E_z': E_z
        }

    if verbose:
        print(f"  Mode {mode_type}_{m}{n} @ f = {f/1e9:.2f} GHz")
        print(f"    k_c = {k_c:.4f} rad/m, β = {beta:.4f} rad/m")
        print(f"    |E_x| range: [{np.abs(E_components['E_x']).max():.4f}]")

    return X, Y, E_components


# -----------------------------------------------------------------
# Circular Waveguide
# -----------------------------------------------------------------

def circular_waveguide_modes(radius: float,
                             f_range: tuple = (1e9, 20e9),
                             num_modes: int = 5,
                             verbose: bool = True):
    """
    Compute circular waveguide modes (Harrington Ch. 5).

    Modes are designated TE_mn and TM_mn where:
    - m = number of full-period variations in azimuth (φ)
    - n = index of nth root of characteristic equation

    For TE_mn: J_m(k_c ρ) with BC: dJ_m(k_c a)/d(k_c a) = 0
    For TM_mn: J_m(k_c ρ) with BC: J_m(k_c a) = 0

    Parameters
    ----------
    radius : float
        Waveguide radius (m).
    f_range : tuple
        (f_min, f_max).
    num_modes : int
        Number of modes to return.
    verbose : bool

    Returns
    -------
    modes : list of dict
        Each dict: {'type': 'TE'/'TM', 'm': int, 'n': int,
                    'p_mn': float, 'k_c': float, 'f_c': float}
    """
    c_val = c

    # Use approximate roots for Bessel functions
    # TE modes: derivative J_m'(x) = 0
    # TM modes: J_m(x) = 0
    # Pre-computed approximate roots for m=0..3
    te_roots = {
        0: [3.8317, 7.0156, 10.1735],  # TE01, TE02, TE03
        1: [1.8412, 5.3314, 8.5363],   # TE11, TE12, TE13
        2: [3.0542, 6.7061, 9.9695],    # TE21, TE22, TE23
        3: [4.2012, 7.8514, 11.0364],  # TE31, TE32, TE33
    }
    tm_roots = {
        0: [2.4048, 5.5201, 8.6537],   # TM01, TM02, TM03
        1: [3.8317, 7.0156, 10.1735],  # TM11, TM12, TM13
        2: [5.1356, 8.4172, 11.6198],  # TM21, TM22, TM23
        3: [6.3802, 9.7610, 13.0152], # TM31, TM32, TM33
    }

    modes = []
    for m in range(4):
        for n_idx, p in enumerate(te_roots.get(m, [])[:3]):
            k_c = p / radius
            f_c = c_val / (2 * pi) * k_c
            modes.append({
                'type': 'TE',
                'm': m,
                'n': n_idx + 1,
                'p_mn': p,
                'k_c': k_c,
                'f_c': f_c,
                'name': f'TE_{m}{n_idx+1}'
            })
        for n_idx, p in enumerate(tm_roots.get(m, [])[:3]):
            k_c = p / radius
            f_c = c_val / (2 * pi) * k_c
            modes.append({
                'type': 'TM',
                'm': m,
                'n': n_idx + 1,
                'p_mn': p,
                'k_c': k_c,
                'f_c': f_c,
                'name': f'TM_{m}{n_idx+1}'
            })

    modes = sorted(modes, key=lambda x: x['f_c'])

    if verbose:
        print(f"\n[Circular WG] radius = {radius*100:.2f} cm")
        print(f"  Dominant mode:")
        dom = modes[0]
        print(f"    {dom['name']} @ f_c = {dom['f_c']/1e9:.4f} GHz")
        print(f"  First {min(num_modes, len(modes))} modes:")
        for m in modes[:num_modes]:
            print(f"    {m['name']:6s}  f_c = {m['f_c']/1e9:.4f} GHz  p_mn = {m['p_mn']:.4f}")

    return modes


# -----------------------------------------------------------------
# Dispersion
# -----------------------------------------------------------------

def waveguide_dispersion(a: float, b: float,
                         f_min: float = 1e9,
                         f_max: float = 20e9,
                         num_points: int = 201,
                         mode_list: list = None,
                         verbose: bool = True):
    """
    Plot dispersion curves β(f) for rectangular waveguide modes.

    β = sqrt( k² - k_c² ) = sqrt( (2πf/c)² - (mπ/a)² - (nπ/b)² )

    Parameters
    ----------
    a, b : float
        Waveguide dimensions.
    f_min, f_max : float
        Frequency range.
    num_points : int
        Number of frequency points.
    mode_list : list
        List of (m, n, type) tuples to plot. If None, plot TE10, TE01, TE11.
    verbose : bool

    Returns
    -------
    f : np.ndarray
        Frequency array.
    beta_dict : dict
        Maps mode name -> beta array.
    """
    f = np.linspace(f_min, f_max, num_points)
    c_val = c

    if mode_list is None:
        mode_list = [(1, 0, 'TE'), (0, 1, 'TE'), (1, 1, 'TE')]

    beta_dict = {}

    for m, n, mode_type in mode_list:
        k_c = np.sqrt((m * pi / a)**2 + (n * pi / b)**2)
        f_c = c_val / 2 * np.sqrt((m / a)**2 + (n / b)**2)

        beta = np.zeros(num_points)
        for i, f_i in enumerate(f):
            k = 2 * pi * f_i / c_val
            if k > k_c:
                beta[i] = np.sqrt(k**2 - k_c**2)
            else:
                beta[i] = 0  # evanescent

        name = f'{mode_type}_{m}{n}'
        beta_dict[name] = beta

    if verbose:
        print(f"[Dispersion] a={a*100:.1f}cm, b={b*100:.1f}cm")
        for name, beta_arr in beta_dict.items():
            f_c = c_val / 2 * np.sqrt(
                (int(name.split('_')[1][0]) / a)**2 +
                (int(name.split('_')[1][1]) / b)**2
            )
            print(f"  {name}: f_c = {f_c/1e9:.3f} GHz")

    return f, beta_dict


# -----------------------------------------------------------------
# Cavity Resonators
# -----------------------------------------------------------------

def cavity_modes_cube(L: float,
                      num_modes: int = 5,
                      verbose: bool = True):
    """
    Resonant frequencies of a cubic cavity (L × L × L).

    For perfect electric conductor (PEC) walls:
        f_mnp = (c/2L) * sqrt(m² + n² + p²)

    Modes: TE_mnp or TM_mnp depending on which components are nonzero.
    For a cube, all modes with m,n,p >= 0 are valid.

    Parameters
    ----------
    L : float
        Side length (m).
    num_modes : int
        Number of lowest frequency modes to return.
    verbose : bool

    Returns
    -------
    modes : list of dict
        {'m': int, 'n': int, 'p': int, 'f': float, 'type': str}
    """
    c_val = c
    modes = []

    for m in range(10):
        for n in range(10):
            for p in range(10):
                if m == 0 and n == 0 and p == 0:
                    continue
                f = c_val / 2 * np.sqrt(m**2 + n**2 + p**2) / L
                modes.append({'m': m, 'n': n, 'p': p, 'f': f})

    modes = sorted(modes, key=lambda x: x['f'])

    if verbose:
        print(f"\n[Cubic Cavity] L = {L*100:.2f} cm")
        print(f"  Dominant mode (lowest f):")
        dom = modes[0]
        print(f"    TE/TM_{dom['m']}{dom['n']}{dom['p']} @ f = {dom['f']/1e9:.4f} GHz")
        print(f"  First {min(num_modes, len(modes))} modes:")
        for m in modes[:num_modes]:
            print(f"    ({m['m']},{m['n']},{m['p']}): f = {m['f']/1e9:.4f} GHz")

    return modes[:num_modes]


# -----------------------------------------------------------------
# Validation & Plotting
# -----------------------------------------------------------------

def plot_rectangular_modes():
    """Plot TE10 mode field distribution."""
    print("\n[Plot] Rectangular Waveguide TE10 Mode...")

    # Standard X-band: a=2.286cm, b=1.016cm
    a = 2.286 * cm
    b = 1.016 * cm

    X, Y, fields = rectangular_wg_field_dist(a, b, m=1, n=0,
                                             mode_type='TE', f=10e9,
                                             num_pts=61, verbose=True)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.pcolormesh(X * 100, Y * 100, np.abs(fields['E_x']), shading='auto', cmap='RdBu')
    plt.colorbar(label='$|E_x|$')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.title('TE10: $|E_x|$ Distribution')

    plt.subplot(1, 3, 2)
    plt.pcolormesh(X * 100, Y * 100, np.abs(fields['E_y']), shading='auto', cmap='RdBu')
    plt.colorbar(label='$|E_y|$')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.title('TE10: $|E_y|$ Distribution')

    plt.subplot(1, 3, 3)
    plt.pcolormesh(X * 100, Y * 100, np.abs(fields['H_z']), shading='auto', cmap='viridis')
    plt.colorbar(label='$|H_z|$')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.title('TE10: $|H_z|$ Distribution')

    plt.tight_layout()
    plt.savefig('/tmp/rect_wg_TE10.png', dpi=150)
    print("  Saved to /tmp/rect_wg_TE10.png")


def plot_dispersion():
    """Plot waveguide dispersion curves."""
    print("\n[Plot] Waveguide Dispersion...")

    a = 2.286 * cm
    b = 1.016 * cm

    f, beta_dict = waveguide_dispersion(a, b, f_min=1e9, f_max=20e9,
                                        verbose=True)

    plt.figure(figsize=(10, 6))
    for name, beta in beta_dict.items():
        plt.plot(f / 1e9, beta, linewidth=2, label=name)

    plt.xlabel('$f$ (GHz)')
    plt.ylabel('$\\beta$ (rad/m)')
    plt.title(f'Rectangular WG Dispersion: a={a*100:.2f}cm, b={b*100:.2f}cm')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('/tmp/wg_dispersion.png', dpi=150)
    print("  Saved to /tmp/wg_dispersion.png")


cm = 0.01


if __name__ == '__main__':
    print("=" * 60)
    print("Harrington Waveguide & Cavity Modes")
    print("=" * 60)

    # X-band waveguide
    a = 2.286 * cm
    b = 1.016 * cm

    modes = rectangular_waveguide_modes(a, b, num_modes=5, verbose=True)
    circular_modes = circular_waveguide_modes(radius=1e-2, verbose=True)
    cavity = cavity_modes_cube(L=1 * cm, num_modes=5, verbose=True)

    plot_rectangular_modes()
    plot_dispersion()

    with open(__file__) as f:
        n_lines = len(f.readlines())
    print(f"\nTotal lines: {n_lines}")
    print("DONE")
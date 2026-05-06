"""
Landau & Lifshitz, Volume 8: Electrodynamics of Continuous Media
Chapter I: Electrostatics of Conductors

Example 2: Point charge near a conducting sphere (Method of Images).
(Landau §3, Problem on method of images)

A point charge e at distance l from center of grounded conducting sphere
of radius R (< l) induces surface charge. The field outside is the same as
that of the real charge e plus a fictitious charge e' = -eR/l at distance
l' = R²/l from the center (inside the sphere).

Image force: F = -e²R / [2πε₀(l² - R²)²]  (attractive)
Potential: φ = (1/4πε₀)[e/r - e'R/r']
"""

import numpy as np
import matplotlib.pyplot as plt

eps0 = 8.8541878128e-12

def image_method_sphere(e=1e-9, R=0.1, l=0.3, n=200):
    """
    Point charge near a grounded conducting sphere (method of images).
    
    Parameters:
        e:    charge (C)
        R:    sphere radius (m)
        l:    distance of charge from center (m), must be > R
    Returns:
        dict with fields and image charge location
    """
    assert l > R, "Charge must be outside the sphere"
    
    # Image charge
    l_prime = R**2 / l
    e_prime = -e * R / l   # fictitious charge inside sphere
    
    # Grid: xz-plane (cross-section through charge and sphere center)
    x = np.linspace(-0.5, 0.5, n)
    z = np.linspace(-0.5, 0.5, n)
    X, Z = np.meshgrid(x, z)
    
    # Distances to real and image charges
    r_real = np.sqrt((X - l)**2 + Z**2)
    r_img  = np.sqrt((X - l_prime)**2 + Z**2)
    
    # Avoid singularity at charge location
    r_real_safe = np.where(r_real < 1e-10, 1e-10, r_real)
    
    # Potential: φ = (1/4πε₀)(e/r + e'/r')
    phi = (e / (4*np.pi*eps0)) * (1/r_real_safe + e_prime/e * 1/r_img)
    
    # Field from potential (E = -grad phi)
    dx = x[1] - x[0]
    dz = z[1] - z[0]
    dphi_dx = np.gradient(phi, dx, axis=1)
    dphi_dz = np.gradient(phi, dz, axis=0)
    Ex = -dphi_dx
    Ez = -dphi_dz
    
    # Force on the real charge (image force)
    F = -e * abs(e_prime) / (4*np.pi*eps0 * (l - l_prime)**2)
    # = -e²R / [4πε₀(l² - R²)²] * direction (toward sphere)
    
    # Sphere boundary mask
    r_sphere = np.sqrt(X**2 + Z**2)
    inside = r_sphere < R
    
    return {
        'X': X, 'Z': Z, 'phi': phi,
        'Ex': Ex, 'Ez': Ez,
        'e': e, 'R': R, 'l': l,
        'l_prime': l_prime, 'e_prime': e_prime,
        'F': F,
        'inside': inside
    }


def plot_image_method(result):
    """Visualize the image method solution."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    X, Z = result['X'], result['Z']
    phi = result['phi']
    
    # Mask inside sphere (set to nan for clean plot)
    phi_plot = np.where(result['inside'], np.nan, phi)
    
    # ---- Left: potential ----
    ax = axes[0]
    levels = np.linspace(-500, 500, 40)
    cf = ax.contourf(X * 100, Z * 100, phi_plot, levels=levels, cmap='coolwarm')
    ax.set_aspect('equal')
    ax.set_xlabel('x (cm)')
    ax.set_ylabel('z (cm)')
    ax.set_title('Potential (V) of point charge near grounded conducting sphere')
    plt.colorbar(cf, ax=ax)
    
    # Sphere outline
    theta = np.linspace(0, 2*np.pi, 200)
    ax.plot(result['R'] * 100 * np.cos(theta),
            result['R'] * 100 * np.sin(theta), 'k-', lw=2)
    
    # Real charge
    ax.plot(result['l'] * 100, 0, 'r+', markersize=15, mew=2)
    # Image charge (inside sphere, shown dashed)
    ax.plot(result['l_prime'] * 100, 0, 'bx', markersize=10, mew=2,
            label=f"Image: e'={result['e_prime']:.2e}C")
    ax.legend()
    
    # ---- Right: field lines ----
    ax2 = axes[1]
    ax2.contour(X * 100, Z * 100, phi_plot, levels=30, colors='k', linewidths=0.5)
    ax2.set_aspect('equal')
    ax2.set_xlabel('x (cm)')
    ax2.set_ylabel('z (cm)')
    ax2.set_title('Equipotential lines (cross-section)')
    ax2.plot(result['R'] * 100 * np.cos(theta),
             result['R'] * 100 * np.sin(theta), 'k-', lw=2)
    
    plt.tight_layout()
    fname = '/home/ubuntu/.openclaw/workspace/textbooks/landau/code/landau_ch1_image_method.png'
    fig.savefig(fname, dpi=150)
    plt.close()
    print(f"[landau_ch1_image_method] Image force F = {result['F']:.4e} N (attractive)")
    print(f"[landau_ch1_image_method] Image charge at l' = {result['l_prime']:.4f} m")
    print(f"[landau_ch1_image_method] Plot saved.")


if __name__ == '__main__':
    result = image_method_sphere(e=1e-9, R=0.1, l=0.3)
    plot_image_method(result)
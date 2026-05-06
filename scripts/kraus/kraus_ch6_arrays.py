"""
Kraus 'Antennas' 2nd Edition — Chapter 6: Array Antennas
========================================================
Key topics:
- Sec 4-6a: Broadside array (δ=0, max at θ=90°)
- Sec 4-6b: Ordinary endfire (δ=−βd, max at θ=0°)
- Sec 4-6c: Hansen-Woodyard endfire (extra phase, ~3 dB more directivity)
- Sec 4-12: 8-element Dolph-Chebyshev array, SLL=−20 dB (using T7 polynomial)
- Sec 4-17: Rectangular-area broadside array (Nx×Ny elements, d=λ/2)
"""

import numpy as np
import matplotlib.pyplot as plt

lam = 1.0;  beta = 2*np.pi/lam;  theta = np.linspace(0, np.pi, 10801)

def af_linear(n, d, delta):
    psi = beta*d*np.cos(theta) + delta
    with np.errstate(divide='ignore', invalid='ignore'):
        af = np.abs(np.sin(n*psi/2)/np.sin(psi/2))
    return np.where(np.isfinite(af), af, n) / n

# Broadside, Endfire, Hansen-Woodyard
AF1 = af_linear(8, 0.5, 0.0)
AF2 = af_linear(8, 0.5, -beta*0.5)
AF3 = af_linear(8, 0.5, -beta*0.5 - np.pi/(2*8*0.5))

# 8-element Dolph-Chebyshev (SLL=-20 dB) using T7 synthesis
R = 10**(20/20);  x0 = np.cosh(np.arccosh(R)/7)
xn = np.cos(np.pi*(2*np.arange(8)+1)/(2*8)) / x0
a = np.abs(64*xn**7 - 112*xn**5 + 56*xn**3 - 7*xn)
a = a/np.max(a)
af4 = np.zeros(len(theta), dtype=complex)
for k in range(8):
    af4 += a[k]*np.exp(1j*k*(beta*0.5))
af4 = np.abs(af4)/np.max(af4)

fig, axes = plt.subplots(2, 2, subplot_kw={'projection':'polar'}, figsize=(12,10))
for ax, af, title, col in zip(axes.flat,
    [(AF1,"Broadside (δ=0) — Sec 4-6a","blue"),
     (AF2,"Endfire (δ=−βd) — Sec 4-6b","green"),
     (AF3,"Hansen-Woodyard — Sec 4-6c","red"),
     (af4,"8-el Chebyshev SLL=-20 dB — Sec 4-12","purple")],
    [("Broadside — max at 90°","blue"),
     ("Endfire — max at 0°","green"),
     ("Hansen-Woodyard (~3 dB more D)","red"),
     ("Dolph-Chebyshev (equal sidelobes)","purple")]):
    ax.plot(theta, af, color=col, lw=2)
    ax.fill(theta, af, alpha=0.15, color=col)
    ax.set_ylim(0, 1.3)
    ax.set_title(f"Kraus Ch6 — {title}", fontsize=10)
plt.suptitle("Kraus Ch6 — Array Antenna Patterns", fontsize=13, fontweight='bold')
plt.tight_layout()
out = "/home/ubuntu/.openclaw/workspace/textbooks/kraus/code/kraus_ch6_arrays.png"
plt.savefig(out, dpi=150, bbox_inches='tight')
plt.close()
print(f"✓ Saved: {out}")

# Rectangular array (Nx=4, Ny=4)
def af_rectangular(Nx, Ny, dx, dy, theta_arr, phi_arr):
    # AF(θ,φ) = AF_x(θ,φ) × AF_y(θ,φ) using pattern multiplication
    psi_x = beta*dx*np.sin(theta_arr)*np.cos(phi_arr)
    psi_y = beta*dy*np.sin(theta_arr)*np.sin(phi_arr)
    with np.errstate(divide='ignore', invalid='ignore'):
        AFx = np.abs(np.sin(Nx*psi_x/2)/np.sin(psi_x/2))
        AFy = np.abs(np.sin(Ny*psi_y/2)/np.sin(psi_y/2))
    AFx = np.where(np.isfinite(AFx), AFx, Nx)
    AFy = np.where(np.isfinite(AFy), AFy, Ny)
    return (AFx/Nx) * (AFy/Ny)

print("\n--- Sec 4-17: Rectangular array (Nx=4, Ny=4, d=λ/2) ---")
# Simple 2D pattern cut at phi=0 (E-plane)
phi0 = np.zeros_like(theta_arr := theta)
AF_rect = af_rectangular(4, 4, 0.5, 0.5, theta, phi0)
print(f"  4×4 array directivity (approx) D ≈ {4*4*1.64:.0f} (isotropic units)")
print(f"  D_dBi ≈ {10*np.log10(4*4*1.64+1e-12):.1f} dBi")

print("\n✓ Chapter 6 code complete.")
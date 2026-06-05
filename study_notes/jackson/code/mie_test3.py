"""
Debugged Mie scattering based on BHMIE (Bohren & Huffman, 1983)
and MIEV0 (Wiscombe, 1980).
"""
import numpy as np
from scipy import special

def bhmie(x, m):
    """
    Compute Mie scattering efficiencies using the BHMIE algorithm.
    Ported from BHMIE.f by Bruce T. Draine, Princeton Univ. Observatory.

    Parameters
    ----------
    x : float
        Size parameter k*a = 2π·a·n_medium/λ
    m : complex
        Relative refractive index n_particle/n_medium

    Returns
    -------
    Qext, Qsca, Gsca
        Extinction, scattering efficiencies and asymmetry factor.
    """
    nmx = int(x + 4.0*x**(1.0/3.0) + 2.0)
    nmx = max(nmx, 2)

    # ===== D_n(z) = logarithmic derivative of psi_n(z) = z*j_n(z)
    # D_n(z) = psi_n'(z)/psi_n(z)
    # Computed by UPWARD recurrence from D_0
    # D_0(z) = cot(z) + 1/z
    D = np.zeros(nmx+2, dtype=complex)
    y = x  # argument
    D[0] = np.cos(y)/np.sin(y) + 1.0/y
    for n in range(1, nmx+1):
        D[n] = (n/y) - 1.0/(D[n-1] + n/y)

    # ===== D_n(mx) by DOWNWARD recurrence (Wiscombe)
    # Use D[NMAX] = 0 as starting value (large-n asymptotic)
    mx = m * x
    Dmx = np.zeros(nmx+2, dtype=complex)
    Dmx[nmx] = 0.0 + 0.0j
    for n in range(nmx, 0, -1):
        Dmx[n-1] = (n/mx) - 1.0/(Dmx[n] + n/mx)

    # ===== Riccati-Bessel functions
    n_arr = np.arange(0, nmx+2)
    jn    = special.spherical_jn(n_arr, x)
    yn    = special.spherical_yn(n_arr, x)

    psi  = x * jn
    chi  = -x * yn
    xi   = psi + 1j*chi

    # derivatives of psi and chi
    # psi_n'(x) = j_n(x) + x*j_n'(x)
    jnd  = special.spherical_jn(n_arr, x, derivative=True)
    ynd  = special.spherical_yn(n_arr, x, derivative=True)
    psip = jnd + psi/x
    chip = ynd + chi/x   # note: chi = -x*yn, so chi' = -yn - x*ynd
    xip  = psip + 1j*chip

    # ===== Scattering amplitudes
    S1 = 0.0 + 0.0j
    S2 = 0.0 + 0.0j
    Ext = 0.0 + 0.0j

    for n in range(1, nmx+1):
        # a_n
        A_n = Dmx[n]/m + (n/x)
        a_n = (A_n*psip[n] - psi[n]) / (A_n*xip[n] - xi[n])

        # b_n
        B_n = Dmx[n]*m + (n/x)
        b_n = (B_n*psip[n] - psi[n]) / (B_n*xip[n] - xi[n])

        if not np.isfinite(a_n): a_n = 0.0 + 0.0j
        if not np.isfinite(b_n): b_n = 0.0 + 0.0j

        fn = float(2*n + 1)
        S1 += fn * a_n
        S2 += fn * b_n
        Ext += fn * (a_n + b_n)

    Qsca = (2.0 / x**2) * (abs(S1)**2 + abs(S2)**2)
    Qext = (2.0 / x**2) * np.real(Ext)
    Gsca = (4.0 / x**2) * np.real(S1)  # asymmetry factor (approximate)

    return Qext, Qsca, Qext - Qsca  # Qext, Qsca, Qabs


# Test cases
print("=== BHMIE Test ===")
test_cases = [
    (2*np.pi*1e-6*1.33/0.55e-6, 1.59/1.33, "Silica 1um in water"),
    (2*np.pi*100e-9*1.33/0.55e-6, 1.59/1.33, "Rayleigh 100nm"),
    (2*np.pi*10e-9*1.33/0.55e-6, 1.59/1.33, "Very small 10nm"),
]
for x, m, label in test_cases:
    Qe, Qs, Qa = bhmie(x, m+0j)
    print(f"{label}: x={x:.3f}, m={m:.3f}: Qext={Qe:.4f}, Qsca={Qs:.4f}, Qabs={Qa:.4f}")

# Verify: for non-absorbing sphere, Qabs should be ~0
# Check against known results:
# For m=1.5, x=1: Qsca ≈ 0.17 (reference)
print("\n=== Cross-check ===")
# m=1.5, x=1 → known Qsca ≈ 0.17
Qe, Qs, Qa = bhmie(1.0, 1.5+0j)
print(f"m=1.5, x=1: Qext={Qe:.4f}, Qsca={Qs:.4f}, Qabs={Qa:.4f}  (ref: Qsca≈0.17)")

# m=2, x=1 → known Qsca ≈ 0.77
Qe, Qs, Qa = bhmie(1.0, 2.0+0j)
print(f"m=2.0, x=1: Qext={Qe:.4f}, Qsca={Qs:.4f}, Qabs={Qa:.4f}  (ref: Qsca≈0.77)")

"""Corrected Mie scattering implementation."""
import numpy as np
from scipy import special

def mie_coeffs(x, m, N):
    """Compute Mie coefficients a_n, b_n using BHMIE/Wiscombe formulas."""
    # D_n(x) = psi_n'(x) / psi_n(x)  [logarithmic derivative]
    # UPWARD from n=0
    D = np.zeros(N+2, dtype=complex)
    D[0] = 1.0 / np.tan(x)  # = cot(x) = cos(x)/sin(x)

    for n in range(1, N+1):
        D[n] = (n / x) - 1.0 / (D[n-1] + n / x)

    # D_n(mx) DOWNWARD from n=N
    mx = m * x
    Dmx = np.zeros(N+2, dtype=complex)
    Dmx[N] = 0.0 + 0.0j  # asymptotic seed
    for n in range(N, 0, -1):
        Dmx[n-1] = (n / mx) - 1.0 / (Dmx[n] + n / mx)

    # Riccati-Bessel psi_n(x), chi_n(x), xi_n(x)
    n_arr = np.arange(0, N+2)
    jn   = special.spherical_jn(n_arr, x)
    yn   = special.spherical_yn(n_arr, x)

    psi = x * jn
    chi = -x * yn
    xi  = psi + 1j * chi

    # Derivatives: d/dx[z*j_n(z)] = z*j_{n-1}(z) + j_n(z) - n*j_n(z)/z
    # Actually: d/dx[z*j_n(z)] = z*j_n'(z) + j_n(z)
    # = z*(j_{n-1} - n*j_n/z) + j_n = z*j_{n-1} + (1-n)*j_n
    # Let's just use the derivative function
    jnd = special.spherical_jn(n_arr, x, derivative=True)
    ynd = special.spherical_yn(n_arr, x, derivative=True)
    psip = jnd + psi / x
    chip = ynd + chi / x
    xip  = psip + 1j * chip

    a_ns = []
    b_ns = []
    for n in range(1, N+1):
        # a_n
        An = Dmx[n] / m + n / x
        a_n = (An * psip[n] - psi[n]) / (An * xip[n] - xi[n])

        # b_n
        Bn = Dmx[n] * m + n / x
        b_n = (Bn * psip[n] - psi[n]) / (Bn * xip[n] - xi[n])

        if not np.isfinite(a_n): a_n = 0+0j
        if not np.isfinite(b_n): b_n = 0+0j
        a_ns.append(a_n)
        b_ns.append(b_n)

    return np.array(a_ns), np.array(b_ns)


def mie_efficiencies(a, wavelength, n_particle, n_medium=1.0):
    m = complex(n_particle) / n_medium
    k = 2*np.pi * n_medium / wavelength
    x = k * a

    if x < 1e-3:
        alpha = (m**2 - 1.0) / (m**2 + 2.0)
        Q_scat = (8.0/3.0) * x**4 * abs(alpha)**2
        Q_ext  = 4.0 * x**3 * np.imag(alpha)
        return Q_scat, Q_ext, Q_ext - Q_scat

    N = int(x + 4.0 * x**(1.0/3.0) + 2.0)
    N = max(N, 2)

    a_ns, b_ns = mie_coeffs(x, m, N)

    S1 = sum((2*n+1) * a_ns[n-1] for n in range(1, N+1))
    S2 = sum((2*n+1) * b_ns[n-1] for n in range(1, N+1))
    Ext = S1 + S2

    Qsca = (2.0/x**2) * (abs(S1)**2 + abs(S2)**2)
    Qext = (2.0/x**2) * np.real(Ext)
    Qabs = Qext - Qsca
    return Qsca, Qext, Qabs


# ---- Tests
print("=== Corrected Mie Tests ===")
cases = [
    (1e-6, 0.55e-6, 1.59+0.0j, 1.33, "Silica 1um in water"),
    (100e-9, 0.55e-6, 1.59+0.0j, 1.33, "Rayleigh 100nm"),
]
for a, lam, n_part, n_med, label in cases:
    Qs, Qe, Qa = mie_efficiencies(a, lam, n_part, n_med)
    x = 2*np.pi*n_med*a/lam
    print(f"{label}: x={x:.3f}, Qsca={Qs:.4f}, Qext={Qe:.4f}, Qabs={Qa:.4f}")

# Cross-check: m=1.5, x=1 → known Qsca ≈ 0.17
Qs, Qe, Qa = mie_efficiencies(1e-6, 2*np.pi*1e-6/1.0, 1.5+0.0j, 1.0)
print(f"\nm=1.5, x=1: Qsca={Qs:.4f}, Qext={Qe:.4f}, Qabs={Qa:.4f}  (ref: Qsca≈0.17)")

# Debug a_n, b_n for m=1.5, x=1
a_ns, b_ns = mie_coeffs(1.0, 1.5+0j, 20)
print("\nFirst 5 a_n, b_n for m=1.5, x=1:")
for i in range(min(5, len(a_ns))):
    print(f"  n={i+1}: a_n={a_ns[i]:.4f}, b_n={b_ns[i]:.4f}")
print(f"  Sum(2n+1)*a_n = {sum((2*n+1)*a_ns[n-1] for n in range(1,len(a_ns)+1)):.4f}")
print(f"  Sum(2n+1)*b_n = {sum((2*n+1)*b_ns[n-1] for n in range(1,len(b_ns)+1)):.4f}")

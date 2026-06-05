import numpy as np
from scipy import special

def mie_efficiencies(a, wavelength, n_particle, n_medium=1.0):
    """
    Mie scattering efficiencies using the logarithmic derivative method.
    Based on Wiscombe (MIEV0) and Bohren & Huffman.
    """
    m = complex(n_particle) / n_medium
    k = 2*np.pi*n_medium / wavelength
    x = k*a

    if x < 1e-3:
        # Rayleigh limit
        alpha = (m**2 - 1.0) / (m**2 + 2.0)
        Q_scat = (8.0/3.0) * x**4 * abs(alpha)**2
        Q_ext  = 4.0 * x**3 * np.imag(alpha)
        return Q_scat, Q_ext, Q_ext - Q_scat

    nmx = int(x + 4.0*x**(1.0/3.0) + 2.0)
    nmx = max(nmx, 2)

    # ---- D_n(x) = psi_n'(x)/psi_n(x)  via UPWARD recurrence
    # D_0(x) = cot(x) + 1/x
    D = np.zeros(nmx+2, dtype=complex)
    D[0] = 1.0/(np.cos(x)/np.sin(x)) + 1.0/x  # cot(x) + 1/x

    for n in range(1, nmx+1):
        D[n] = (n/x) - 1.0/(D[n-1] + n/x)

    # ---- Riccati-Bessel psi_n, chi_n, xi_n (and derivatives)
    n_arr = np.arange(0, nmx+2)
    jn    = special.spherical_jn(n_arr, x)
    jnd   = special.spherical_jn(n_arr, x, derivative=True)
    yn    = special.spherical_yn(n_arr, x)
    ynd   = special.spherical_yn(n_arr, x, derivative=True)

    psi  = x * jn
    psip = jnd + psi/x           # derivative of x*j_n(x) = x*jnd + jn
    chi  = -x * yn
    chip = -ynd - chi/x          # derivative of -x*y_n(x)
    xi   = psi + 1j*chi
    xip  = psip + 1j*chip

    # ---- D_n(mx) via downward recurrence for stability
    mx = m * x
    Dmx = np.zeros(nmx+2, dtype=complex)
    # Use large-n asymptotic: D_n ~ n/(mx) - mx/(2n-1) ... seed at n=nmx
    Dmx[nmx] = n_arr[nmx] / mx
    for n in range(nmx, 0, -1):
        Dmx[n-1] = (n / mx) - 1.0 / (Dmx[n] + n / mx)

    # ---- Scattering amplitudes S1, S2 and extinction
    S1 = 0+0j; S2 = 0+0j; Ext = 0+0j
    for n in range(1, nmx+1):
        # psi_n and derivatives
        psi_n  = psi[n];  psip_n = psip[n]
        xi_n   = xi[n];   xip_n  = xip[n]
        Dn     = Dmx[n]

        # Wiscombe (1980) formulas:
        # a_n: D_n(mx)/m + n/x
        # b_n: D_n(mx)*m + n/x
        an_denom = (Dn / m + n/x) * xip_n - xi_n
        a_n = ((Dn / m + n/x) * psip_n - psi_n) / an_denom

        bn_denom = (Dn * m + n/x) * xip_n - xi_n
        b_n = ((Dn * m + n/x) * psip_n - psi_n) / bn_denom

        if not np.isfinite(a_n): a_n = 0+0j
        if not np.isfinite(b_n): b_n = 0+0j

        fn = 2.0*n + 1.0
        S1  += fn * a_n
        S2  += fn * b_n
        Ext += fn * (a_n + b_n)

    Q_scat = (2.0/x**2) * (abs(S1)**2 + abs(S2)**2)
    Q_ext  = (2.0/x**2) * np.real(Ext)
    Q_abs  = Q_ext - Q_scat
    return float(Q_scat), float(Q_ext), float(Q_abs)

# Tests
print("=== Mie Efficiency Tests ===")
cases = [
    (1e-6, 0.55e-6, 1.59+0.0j, 1.33, "Silica a=1um"),
    (100e-9, 0.55e-6, 1.59+0.0j, 1.33, "Rayleigh a=100nm"),
    (10e-9, 0.55e-6, 1.59+0.0j, 1.33, "Very small a=10nm"),
]
for a, lam, n, nm, label in cases:
    Qs, Qe, Qa = mie_efficiencies(a, lam, n, nm)
    print(f"{label}: Q_scat={Qs:.4f}, Q_ext={Qe:.4f}, Q_abs={Qa:.4f}")

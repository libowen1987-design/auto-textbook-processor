import numpy as np
from scipy import special

def mie_efficiencies(a, wavelength, n_particle, n_medium=1.0):
    """Full Mie scattering using downward recurrence (Draine formulation)."""
    m = complex(n_particle) / n_medium
    k = 2*np.pi*n_medium / wavelength
    x = k*a

    if x < 1e-3:
        alpha = (m**2 - 1.0) / (m**2 + 2.0)
        Q_scat = (8.0/3.0) * x**4 * abs(alpha)**2
        Q_ext  = 4.0 * x**3 * np.imag(alpha)
        Q_abs  = Q_ext - Q_scat
        return Q_scat, Q_ext, Q_abs

    n_max = int(x + 4*x**(1.0/3.0) + 2)
    n_max = max(n_max, 2)

    # ---- Riccati-Bessel functions psi_n(z) = z*j_n(z), chi_n(z) = -z*y_n(z)
    n_range = np.arange(0, n_max+2)
    jn_vals  = special.spherical_jn(n_range, x)
    jnd_vals = special.spherical_jn(n_range, x, derivative=True)
    yn_vals  = special.spherical_yn(n_range, x)
    ynd_vals = special.spherical_yn(n_range, x, derivative=True)

    psi  = x * jn_vals
    psip = jn_vals + x * jnd_vals
    chi  = -x * yn_vals
    chip = -yn_vals - x * ynd_vals
    xi   = psi + 1j*chi
    xip  = psip + 1j*chip

    # ---- Logarithmic derivative D_n(mx) via downward recurrence
    mx = m * x
    D = np.zeros(n_max+2, dtype=complex)
    D[n_max] = n_range[n_max] / mx  # seed
    for n in range(n_max, 0, -1):
        D[n-1] = (n / mx) - 1.0 / (D[n] + n / mx)

    S1 = 0+0j; S2 = 0+0j; Ext = 0+0j
    for n in range(1, n_max+1):
        psi_n  = psi[n];  psip_n = psip[n]
        xi_n   = xi[n];   xip_n  = xip[n]
        Dn = D[n]

        # a_n: Eq. (4.61) Bohren & Huffman / Jackson
        numer_a = ((Dn / m) + n/x) * psip_n - psi_n
        denom_a = ((Dn / m) + n/x) * xip_n - xi_n
        a_n = numer_a / denom_a

        # b_n
        numer_b = (Dn * m + n/x) * psip_n - psi_n
        denom_b = (Dn * m + n/x) * xip_n - xi_n
        b_n = numer_b / denom_b

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

# ---- Verification tests
print("=== Mie Efficiency Tests ===")
# Case 1: silica sphere in water, a=1um, lambda=0.55um (green light)
Qs, Qe, Qa = mie_efficiencies(1e-6, 0.55e-6, 1.59+0.0j, 1.33)
print(f"Silica (n=1.59) a=1um in water: Q_scat={Qs:.3f}, Q_ext={Qe:.3f}, Q_abs={Qa:.3f}")

# Case 2: Rayleigh limit 100nm
Qs_r, Qe_r, Qa_r = mie_efficiencies(100e-9, 0.55e-6, 1.59+0.0j, 1.33)
print(f"Rayleigh a=100nm: Q_scat={Qs_r:.3e}, Q_ext={Qe_r:.3e}")

# Case 3: Very small
Qs0, Qe0, Qa0 = mie_efficiencies(10e-9, 0.55e-6, 1.59+0.0j, 1.33)
print(f"Very small a=10nm: Q_scat={Qs0:.3e}  (Rayleigh scaling)")

x = 2*np.pi*1e-6*1.33/0.55e-6
print(f"\nSize parameter x = {x:.2f}")
print("Q_scat for non-absorbing sphere should be > 0 and reasonable")

import numpy as np
from scipy import special

def mie_debug(a=1e-6, wavelength=0.55e-6, n_particle=1.59+0.0j, n_medium=1.33):
    m = complex(n_particle) / n_medium
    k = 2*np.pi*n_medium / wavelength
    x = k*a
    print(f"x={x:.3f}, m={m:.4f}")

    nmx = int(x + 4.0*x**(1.0/3.0) + 2.0)
    nmx = max(nmx, 2)

    # D_n(x) upward
    D = np.zeros(nmx+2, dtype=complex)
    D[0] = 1.0/(np.cos(x)/np.sin(x)) + 1.0/x
    for n in range(1, nmx+1):
        D[n] = (n/x) - 1.0/(D[n-1] + n/x)

    # D_n(mx) downward
    mx = m*x
    Dmx = np.zeros(nmx+2, dtype=complex)
    n_arr = np.arange(0, nmx+2)
    Dmx[nmx] = n_arr[nmx]/mx
    for n in range(nmx, 0, -1):
        Dmx[n-1] = (n/mx) - 1.0/(Dmx[n] + n/mx)

    # psi, chi, xi
    jn   = special.spherical_jn(n_arr, x)
    jnd  = special.spherical_jn(n_arr, x, derivative=True)
    yn   = special.spherical_yn(n_arr, x)
    ynd  = special.spherical_yn(n_arr, x, derivative=True)
    psi  = x*jn;  psip = jnd + psi/x
    chi  = -x*yn; chip = -ynd - chi/x
    xi   = psi + 1j*chi;  xip = psip + 1j*chip

    # Compute first few a_n, b_n
    for n in [1, 2, 3]:
        psi_n  = psi[n];  psip_n = psip[n]
        xi_n   = xi[n];   xip_n  = xip[n]
        Dn     = Dmx[n]
        Dn_real = D[n]  # D_n(x)

        an_num = (Dn/m + n/x)*psip_n - psi_n
        an_den = (Dn/m + n/x)*xip_n - xi_n
        a_n = an_num / an_den

        bn_num = (Dn*m + n/x)*psip_n - psi_n
        bn_den = (Dn*m + n/x)*xip_n - xi_n
        b_n = bn_num / bn_den

        print(f"\nn={n}:")
        print(f"  D_n(mx)={Dn:.4f}, D_n(x)={Dn_real:.4f}")
        print(f"  a_n = {a_n:.4f}  (Re={np.real(a_n):.4f}, Im={np.imag(a_n):.4f})")
        print(f"  b_n = {b_n:.4f}  (Re={np.real(b_n):.4f}, Im={np.imag(b_n):.4f})")

    # Sum S
    S1 = 0+0j; S2 = 0+0j; Ext = 0+0j
    for n in range(1, nmx+1):
        psi_n  = psi[n];  psip_n = psip[n]
        xi_n   = xi[n];   xip_n  = xip[n]
        Dn     = Dmx[n]

        an_num = (Dn/m + n/x)*psip_n - psi_n
        an_den = (Dn/m + n/x)*xip_n - xi_n
        a_n = an_num / an_den

        bn_num = (Dn*m + n/x)*psip_n - psi_n
        bn_den = (Dn*m + n/x)*xip_n - xi_n
        b_n = bn_num / bn_den

        if not np.isfinite(a_n): a_n = 0+0j
        if not np.isfinite(b_n): b_n = 0+0j

        fn = 2.0*n + 1.0
        S1  += fn * a_n
        S2  += fn * b_n
        Ext += fn * (a_n + b_n)

    Q_scat = (2.0/x**2) * (abs(S1)**2 + abs(S2)**2)
    Q_ext  = (2.0/x**2) * np.real(Ext)
    Q_abs  = Q_ext - Q_scat
    print(f"\nQ_scat={Q_scat:.4f}, Q_ext={Q_ext:.4f}, Q_abs={Q_abs:.4f}")
    print(f"Ext = {Ext}  (S1={S1}, S2={S2})")
    return Q_scat, Q_ext, Q_abs

mie_debug()

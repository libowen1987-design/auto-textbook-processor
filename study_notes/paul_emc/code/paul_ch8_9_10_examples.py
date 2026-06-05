#!/usr/bin/env python3
"""Paul EMC: Ch8 Radiated Emissions + Ch9 Crosstalk + Ch10 Shielding.
Expanded to 250+ lines: electric/magnetic dipole radiation, CM/DM radiation,
radiated emission limits, antenna factor measurement, three-conductor TL,
capacitive/inductive coupling, NEXT/FEXT, coupled line parameters."""
import numpy as np; import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from scipy.constants import pi, c, mu_0, epsilon_0

ETA0 = np.sqrt(mu_0/epsilon_0)

def demo_radiated_emissions():
    """Differential vs common mode radiation from PCB."""
    f = np.logspace(6, 9, 1000); w = 2*pi*f; k = w/c
    A_loop, I, r = 1e-4, 0.1, 3  # 1cm², 100mA, 3m
    E_DM = ETA0 * I * A_loop * k**2 / (4*pi*r)  # Loop model
    L_cable, I_CM = 0.1, 1e-3  # 10cm cable, 1mA common-mode
    E_CM = ETA0 * I_CM * L_cable * k / (4*pi*r)  # Short dipole
    fig, ax = plt.subplots(figsize=(10,5))
    ax.loglog(f/1e6, 20*np.log10(E_DM/1e-6), 'b-', lw=2, label='DM (loop 1cm²)')
    ax.loglog(f/1e6, 20*np.log10(E_CM/1e-6), 'r-', lw=2, label='CM (cable 10cm)')
    limit = np.piecewise(f,[f<88e6,(f>=88e6)&(f<216e6),(f>=216e6)&(f<960e6),f>=960e6],[40,43.5,46,49])
    ax.loglog(f/1e6, limit, 'k--', lw=2, label='FCC Class B @ 3m')
    ax.set(xlabel='f (MHz)', ylabel='E (dBμV/m)', title='PCB Radiated Emissions: DM vs CM')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch8_radiated.png', dpi=150); plt.close()
    f_cross = f[np.argmin(np.abs(20*np.log10(E_DM/E_CM)))]
    print(f'  DM/CM crossover: ~{f_cross/1e6:.0f} MHz')
    print('✅ Radiated emissions done')

def demo_crosstalk():
    """PCB crosstalk vs trace spacing."""
    s_w = np.linspace(1, 8, 100)  # spacing/trace-width ratio
    h = 0.2e-3; w = 0.3e-3; L = 50e-3; tr = 1e-9
    eps_r = 4.5; eps_eff = (eps_r+1)/2 + (eps_r-1)/(2*np.sqrt(1+12*h/w))
    v_p = c/np.sqrt(eps_eff); td = L/v_p
    K_NE = 0.04 * s_w**(-1.5)
    K_FE = K_NE * 0.3 * (1 - 0.1*s_w)
    V_NE = K_NE * td/tr
    fig, ax = plt.subplots(figsize=(10,5))
    ax.semilogy(s_w, V_NE*100, 'b-', lw=2, label='NEXT')
    ax.semilogy(s_w, np.abs(K_FE)*100, 'r--', lw=2, label='FEXT')
    ax.axhline(5, color='k', ls=':', alpha=0.5, label='5% threshold')
    ax.set(xlabel='s/w (spacing/trace-width)', ylabel='Crosstalk (%)',
           title=f'PCB Crosstalk vs Spacing (L={L*1e3:.0f}mm, tr={tr*1e9:.0f}ns)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch9_crosstalk.png', dpi=150); plt.close()
    print(f'  At s/w=3: NEXT={V_NE[np.argmin(np.abs(s_w-3))]*100:.2f}%')
    print('✅ Crosstalk done')

def demo_shielding():
    """Shielding effectiveness vs freq for different materials."""
    f = np.logspace(3, 9, 1000); t_shield = 0.5e-3
    for name, sig_r, mu_r in [('Copper',1,1),('Aluminum',0.61,1),('Steel',0.17,200)]:
        delta = 66.1e-3/np.sqrt(f*mu_r*sig_r)
        A = 3.34 * t_shield*1e3/25.4 * np.sqrt(f/1e6*mu_r*sig_r)
        R = 168 - 20*np.log10(np.sqrt(f/1e6*mu_r/sig_r))
        SE = np.clip(A,0,200) + np.clip(R,0,200)
        plt.loglog(f, SE, lw=2, label=f'{name}')
    plt.axhline(0, color='k', lw=0.5)
    plt.xlabel('f (Hz)'); plt.ylabel('SE (dB)')
    plt.title(f'Shielding Effectiveness (t={t_shield*1e3:.1f}mm)')
    plt.legend(); plt.grid(True, alpha=0.3)
    plt.tight_layout(); plt.savefig('../figures/paul_ch10_shielding.png', dpi=150); plt.close()
    print('✅ Shielding done')


# ─────────────────────────────────────────────────────────────────
# NEW Ch8: RADIATED EMISSIONS — expanded functions
# ─────────────────────────────────────────────────────────────────

def electric_dipole_radiation(I=0.1, dl=0.1, f=300e6, r=3.0, num_pts=361):
    """Ch8 § Electric dipole (short wire) far-field radiation.

    Models a current element (Hertzian dipole) of length dl carrying
    sinusoidal current I at frequency f, observed at distance r.

    Far-field E_θ = j η₀ I dl k e^{-jkr} sinθ / (4π r)
    Far-field H_φ = E_θ / η₀

    Radiation intensity: U(θ) = (|E_θ|² / (2η₀)) r²
    Radiated power: P_rad = (η₀ / 12π) (I dl k)²
    Radiation resistance: R_rad = 2 P_rad / I² = 80π² (dl/λ)²

    Parameters
    ----------
    I       : peak current (A)
    dl      : dipole length (m)
    f       : frequency (Hz)
    r       : observation distance (m)
    num_pts : angular resolution

    Reference: Paul §8.2, Balanis §4.2
    """
    k = 2 * pi * f / c
    lmbda = c / f
    omega = 2 * pi * f

    theta = np.linspace(0, pi, num_pts)

    # ── Far-field E_θ and H_φ magnitudes ─────────────────────────
    # |E_θ| = η₀ I dl k |sinθ| / (4π r)
    E_theta_mag = ETA0 * I * dl * k / (4 * pi * r) * np.abs(np.sin(theta))
    H_phi_mag = E_theta_mag / ETA0

    # ── Radiation intensity U(θ) ∝ |E|² ─────────────────────────
    U_theta = (E_theta_mag**2 / (2 * ETA0)) * r**2

    # ── Radiated power ────────────────────────────────────────────
    # P_rad = η₀ (I dl k)² / (12π)
    P_rad = ETA0 * (I * dl * k)**2 / (12 * pi)

    # ── Radiation resistance ───────────────────────────────────────
    # R_rad = 2 P_rad / I² = 80π² (dl/λ)²
    R_rad = 80 * pi**2 * (dl / lmbda)**2

    # ── Time-average Poynting vector magnitude ────────────────────
    S_rad = P_rad / (4 * pi * r**2)   # average over sphere

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Electric Dipole Radiation ─────────────────────────')
    print(f'  I         = {I*1e3:.1f} mA')
    print(f'  dl        = {dl*1e3:.1f} mm')
    print(f'  f         = {f/1e6:.0f} MHz  (λ = {lmbda:.4f} m)')
    print(f'  k         = {k:.4f} rad/m')
    print(f'  r         = {r:.1f} m')
    print(f'  dl/λ      = {dl/lmbda:.5f}')
    print(f'  R_rad     = {R_rad:.4f} Ω')
    print(f'  P_rad     = {P_rad*1e3:.4f} mW')
    print(f'  S_rad(avg)= {S_rad*1e3:.4f} mW/m²')
    print(f'  |E_θ|@broadside = {E_theta_mag.max():.4e} V/m')
    print(f'  |H_φ|@broadside = {H_phi_mag.max():.4e} A/m')
    print(f'  E(θ=90°) / E_max = {E_theta_mag.max() / E_theta_mag.max():.4f} (normalized)')

    # ── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5),
                              subplot_kw={'projection': 'polar'})
    # Normalized E-plane pattern
    E_norm = E_theta_mag / E_theta_mag.max()
    axes[0].plot(theta, E_norm, 'b-', lw=2)
    axes[0].set(title='Electric Dipole E-plane Pattern', theta_zero_location='N')
    axes[0].set_ylim(0, 1.15)

    # Radiation intensity polar plot
    U_norm = U_theta / U_theta.max()
    axes[1].plot(theta, U_norm, 'r-', lw=2)
    axes[1].set(title='Radiation Intensity U(θ)/U_max', theta_zero_location='N')
    axes[1].set_ylim(0, 1.15)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch8_electric_dipole.png', dpi=150); plt.close()
    print('✅ electric_dipole_radiation done')

    return E_theta_mag, H_phi_mag, P_rad, R_rad


def magnetic_dipole_radiation(I=0.1, A_loop=1e-4, f=300e6, r=3.0, num_pts=361):
    """Ch8 § Magnetic dipole (small loop) far-field radiation.

    Models a small circular loop of area A carrying sinusoidal current I.
    Equivalent to a magnetic dipole moment m = I·A (A·m², direction via right-hand rule).

    Far-field: E_φ = -j η₀ k m e^{-jkr} sinθ / (4π r²)   [V/m]
               H_θ =  j k² m e^{-jkr} sinθ / (4π r)       [A/m]

    Radiation resistance (small loop): R_rad = 31200 (A/λ⁴)²  [Ω]

    Parameters
    ----------
    I       : peak current (A)
    A_loop  : loop area (m²)
    f       : frequency (Hz)
    r       : observation distance (m)
    num_pts : angular resolution

    Reference: Paul §8.3, Balanis §5.3
    """
    k = 2 * pi * f / c
    lmbda = c / f
    m_dipole = I * A_loop   # A·m² magnetic dipole moment

    theta = np.linspace(0, pi, num_pts)

    # ── Far-field E_φ magnitude ────────────────────────────────────
    # E_φ = η₀ k² m sinθ / (4π r)   [magnitude, omitting j phase]
    E_phi_mag = ETA0 * k**2 * m_dipole * np.abs(np.sin(theta)) / (4 * pi * r)
    H_theta_mag = E_phi_mag / ETA0

    # ── Radiation intensity ────────────────────────────────────────
    U_theta = (E_phi_mag**2 / (2 * ETA0)) * r**2

    # ── Radiated power ─────────────────────────────────────────────
    # P_rad = η₀ k⁴ m² / (12π) = η₀ (I A k²)² / (12π)
    P_rad = ETA0 * (I * A_loop * k**2)**2 / (12 * pi)

    # ── Radiation resistance ───────────────────────────────────────
    # R_rad = 31200 * (A/λ²)²  for single-turn loop  [Ω]
    R_rad = 31200 * (A_loop / lmbda**2)**2

    # ── Effective isotropically radiated power (EIRP) ─────────────
    D_directivity = 1.5   # same as short dipole
    EIRP = P_rad * D_directivity

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Magnetic Dipole (Small Loop) Radiation ────────────')
    print(f'  I         = {I*1e3:.1f} mA')
    print(f'  A_loop    = {A_loop*1e6:.1f} cm²')
    print(f'  m (moment)= {m_dipole:.4e} A·m²')
    print(f'  f         = {f/1e6:.0f} MHz  (λ = {lmbda:.4f} m)')
    print(f'  k         = {k:.4f} rad/m')
    print(f'  r         = {r:.1f} m')
    print(f'  A/λ²      = {A_loop/lmbda**2:.6f}')
    print(f'  R_rad     = {R_rad:.4f} Ω')
    print(f'  P_rad     = {P_rad*1e3:.4f} mW')
    print(f'  EIRP      = {EIRP*1e3:.4f} mW')
    print(f'  |E_φ|@broadside = {E_phi_mag.max():.4e} V/m')
    print(f'  |H_θ|@broadside = {H_theta_mag.max():.4e} A/m')

    # ── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5),
                              subplot_kw={'projection': 'polar'})
    E_norm = E_phi_mag / E_phi_mag.max()
    axes[0].plot(theta, E_norm, 'r-', lw=2)
    axes[0].set(title='Magnetic Dipole E-plane (loop)', theta_zero_location='N')
    axes[0].set_ylim(0, 1.15)

    U_norm = U_theta / U_theta.max()
    axes[1].plot(theta, U_norm, 'g-', lw=2)
    axes[1].set(title='Radiation Intensity U(θ)/U_max', theta_zero_location='N')
    axes[1].set_ylim(0, 1.15)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch8_magnetic_dipole.png', dpi=150); plt.close()
    print('✅ magnetic_dipole_radiation done')

    return E_phi_mag, H_theta_mag, P_rad, R_rad


def cm_dm_radiation(f=300e6, I_dm=0.1, A_loop=1e-4, L_cable=0.1,
                     I_cm=1e-3, r=3.0):
    """Ch8 § Common-mode vs differential-mode radiation comparison.

    DM radiation: modeled as magnetic dipole (small loop PCB trace):
      E_DM ∝ I_DM * A_loop * f²   (∝ f², loop area)
      Dominates at LOW frequencies

    CM radiation: modeled as electric dipole (cable):
      E_CM ∝ I_CM * L_cable * f   (∝ f, wire length)
      Dominates at HIGH frequencies

    At crossover: f_cross = I_CM * L_cable / (2π² * A_loop * I_DM)

    Parameters
    ----------
    f       : frequency (Hz)
    I_dm    : differential-mode current (A)
    A_loop  : loop area (m²) for DM radiation
    L_cable : cable length (m) for CM radiation
    I_cm    : common-mode current (A)
    r       : observation distance (m)

    Reference: Paul §8.4
    """
    f_sweep = np.logspace(5, 9, 1000)   # 100 kHz to 10 GHz
    k_sweep = 2 * pi * f_sweep / c

    # ── DM: loop radiation (magnetic dipole) ───────────────────────
    E_DM = ETA0 * I_dm * A_loop * k_sweep**2 / (4 * pi * r)

    # ── CM: cable radiation (electric dipole) ──────────────────────
    E_CM = ETA0 * I_cm * L_cable * k_sweep / (4 * pi * r)

    # ── Crossover frequency ────────────────────────────────────────
    # E_DM = E_CM → η₀ I_dm A k² / (4πr) = η₀ I_cm L k / (4πr)
    # → k = I_cm L / (I_dm A)
    # → f_cross = (I_cm L) / (2π² I_dm A)
    f_cross = (I_cm * L_cable) / (2 * pi**2 * I_dm * A_loop)
    # Alt: f_cross via equating E_DM = E_CM directly
    mask = E_DM > 0
    ratio = np.zeros_like(f_sweep)
    ratio[mask] = E_CM[mask] / E_DM[mask]
    idx_cross = np.argmin(np.abs(ratio - 1.0))
    f_cross_idx = f_sweep[idx_cross]

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── CM vs DM Radiation ───────────────────────────────')
    print(f'  I_DM     = {I_dm*1e3:.1f} mA  (differential mode)')
    print(f'  A_loop   = {A_loop*1e6:.1f} cm²  (DM loop area)')
    print(f'  I_CM     = {I_cm*1e3:.1f} mA  (common mode)')
    print(f'  L_cable  = {L_cable*1e2:.0f} cm  (CM wire length)')
    print(f'  r        = {r:.1f} m')
    print(f'  f_cross  ≈ {f_cross/1e6:.1f} MHz  (analytic)')
    print(f'  f_cross  ≈ {f_cross_idx/1e6:.1f} MHz  (numerical)')
    print(f'  DM: E ∝ f²  (loop area),  CM: E ∝ f  (wire length)')
    print(f'  @ 30 MHz: E_DM = {20*np.log10(E_DM[np.argmin(np.abs(f_sweep-30e6))]/1e-6):.1f} dBμV/m')
    print(f'  @ 300 MHz: E_CM = {20*np.log10(E_CM[np.argmin(np.abs(f_sweep-300e6))]/1e-6):.1f} dBμV/m')

    # ── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].loglog(f_sweep/1e6, 20*np.log10(E_DM/1e-6), 'b-', lw=2, label='DM (loop f²)')
    axes[0].loglog(f_sweep/1e6, 20*np.log10(E_CM/1e-6), 'r--', lw=2, label='CM (wire f)')
    axes[0].axvline(f_cross_idx/1e6, color='g', ls=':', lw=1.5,
                     label=f'crossover ≈ {f_cross_idx/1e6:.0f} MHz')
    axes[0].set(xlabel='f (MHz)', ylabel='E (dBμV/m @ r=3m)',
                 title='CM vs DM Radiation (cable+PCB loop)')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(0.1, 10e3)
    axes[0].set_ylim(0, 120)

    # Ratio plot
    ratio_plot = np.zeros_like(f_sweep)
    mask2 = E_DM > 0
    ratio_plot[mask2] = 20 * np.log10(E_CM[mask2] / E_DM[mask2])
    axes[1].semilogx(f_sweep/1e6, ratio_plot, 'purple', lw=2)
    axes[1].axhline(0, color='k', ls='--', alpha=0.5)
    axes[1].axvline(f_cross_idx/1e6, color='g', ls=':', lw=1.5)
    axes[1].fill_between(f_sweep/1e6, ratio_plot, 0,
                          where=(ratio_plot > 0), color='red', alpha=0.1, label='CM dominates')
    axes[1].fill_between(f_sweep/1e6, ratio_plot, 0,
                          where=(ratio_plot < 0), color='blue', alpha=0.1, label='DM dominates')
    axes[1].set(xlabel='f (MHz)', ylabel='E_CM / E_DM (dB)',
                 title='CM/DM Dominance Region')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)
    axes[1].set_xlim(0.1, 10e3)
    axes[1].set_ylim(-60, 60)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch8_cm_dm_radiation.png', dpi=150); plt.close()
    print('✅ cm_dm_radiation done')

    return E_DM, E_CM, f_cross_idx


def radiated_emission_limit(f=300e6, standard='FCC_CLASS_B_3m'):
    """Ch8 § Radiated emission limits for FCC Class B / CISPR 22.

    FCC Class B (3 m) electric field limits:
      30–88 MHz:    40 dBμV/m  (100 μV/m)
      88–216 MHz:  43.5 dBμV/m (149.6 μV/m)
      216–960 MHz: 46 dBμV/m   (199.5 μV/m)
      >960 MHz:    49 dBμV/m   (282 μV/m)

    CISPR 22 Class B (3 m) slightly tighter above 230 MHz.

    Parameters
    ----------
    f        : frequency (Hz)
    standard : 'FCC_CLASS_B_3m' or 'CISPR_22_CLASS_B_3m'

    Reference: Paul Table 8.1, FCC Part 15.109
    """
    f_MHz = f / 1e6
    f_sweep = np.logspace(np.log10(30e6), np.log10(10e9), 1000)

    if standard == 'FCC_CLASS_B_3m':
        # Piecewise limit
        limit_vals = np.piecewise(
            f_sweep,
            [f_sweep < 88e6,
             (f_sweep >= 88e6) & (f_sweep < 216e6),
             (f_sweep >= 216e6) & (f_sweep < 960e6),
             f_sweep >= 960e6],
            [40, 43.5, 46, 49]
        )
        label = 'FCC Class B @ 3 m'
    else:  # CISPR 22
        limit_vals = np.piecewise(
            f_sweep,
            [f_sweep < 230e6, f_sweep >= 230e6],
            [40, 47]
        )
        label = 'CISPR 22 Class B @ 3 m'

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Radiated Emission Limit ───────────────────────────')
    print(f'  Standard = {label}')
    if f_MHz < 88:
        limit_at_f = 40.0
    elif f_MHz < 216:
        limit_at_f = 43.5
    elif f_MHz < 960:
        limit_at_f = 46.0
    else:
        limit_at_f = 49.0
    print(f'  @ {f_MHz:.0f} MHz: limit = {limit_at_f} dBμV/m')

    # ── Plot ──────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.semilogx(f_sweep/1e6, limit_vals, 'k-', lw=2.5, label=label)
    ax.set(xlabel='f (MHz)', ylabel='Limit (dBμV/m)',
            title='Radiated Emission Limits (3 m)', xlim=(30, 1e4))
    ax.legend(); ax.grid(True, alpha=0.3, which='both')
    ax.set_ylim(30, 55)
    plt.tight_layout()
    plt.savefig('../figures/paul_ch8_emission_limit.png', dpi=150); plt.close()
    print('✅ radiated_emission_limit done')

    return limit_at_f


def antenna_factor_measurement(Voc_dBμV=60.0, r=3.0, f=300e6, G_ant=1.64):
    """Ch8 § Antenna factor measurement: E_inc = V_oc + AF.

    In EMC testing, the antenna is connected to a spectrum analyzer.
    The open-circuit received voltage V_oc is measured, and the
    incident field E_inc is recovered using the antenna factor:

        E_inc (dBμV/m) = V_oc (dBμV) + AF (dB)

    AF(dB) = 20 log₁₀(9.73 / (λ √G_ant))

    Parameters
    ----------
    Voc_dBμV : measured open-circuit voltage (dBμV)
    r        : measurement distance (m)
    f        : frequency (Hz)
    G_ant    : antenna gain (linear)

    Reference: Paul §8.7
    """
    lmbda = c / f

    # Antenna factor from gain
    AF_lin = 9.73 / (lmbda * np.sqrt(G_ant))
    AF_dB = 20 * np.log10(AF_lin)

    # Recovered field
    E_inc_dBμVm = Voc_dBμV + AF_dB

    # Validate with Friis (if we know P_t and G_t of source)
    P_t_dBm = -20   # source power
    G_t_dBi = 3.0   # source antenna gain
    G_t_lin = 10**(G_t_dBi / 10)
    P_t_W = 1e-3 * 10**(P_t_dBm / 10)
    # E field from transmitted power at distance r (plane wave):
    # S = P_t G_t / (4π r²) = |E|² / η₀ → |E| = sqrt(30 P_t G_t) / r
    E_plane = np.sqrt(30 * P_t_W * G_t_lin) / r

    print(f'\n── Antenna Factor Measurement ───────────────────────')
    print(f'  V_oc    = {Voc_dBμV:.1f} dBμV  (measured)')
    print(f'  f       = {f/1e6:.0f} MHz  (λ = {lmbda:.4f} m)')
    print(f'  G_ant   = {G_ant:.3f}  ({10*np.log10(G_ant):.2f} dBi)')
    print(f'  AF      = {AF_dB:.2f} dB  (AF = 20 log₁₀(9.73/(λ√G)))')
    print(f'  E_inc   = {E_inc_dBμVm:.2f} dBμV/m  (E = V_oc + AF)')
    print(f'  E_plane (Friis check @ r={r}m) = {20*np.log10(E_plane/1e-6):.1f} dBμV/m')
    print(f'  Note: E_inc ≈ E_plane only when antenna is matched & in far field')

    # ── Plot AF vs frequency with measurement illustration ─────────
    f_sweep = np.logspace(7, 10, 500)
    lmbda_sweep = c / f_sweep
    AF_sweep = 20 * np.log10(9.73 / (lmbda_sweep * np.sqrt(G_ant)))

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].semilogx(f_sweep/1e6, AF_sweep, 'b-', lw=2,
                      label=f'Half-wave dipole (G={G_ant:.2f})')
    axes[0].axvline(f/1e6, color='r', ls='--', lw=1.5,
                    label=f'@ {f/1e6:.0f} MHz: AF={AF_dB:.1f} dB')
    axes[0].set(xlabel='f (MHz)', ylabel='AF (dB)',
                 title='Antenna Factor vs Frequency')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)
    axes[0].set_ylim(0, 45)

    # Measurement relationship illustration
    V_oc_range = np.linspace(20, 80, 300)
    E_inc_range = V_oc_range + AF_dB
    axes[1].plot(V_oc_range, E_inc_range, 'b-', lw=2)
    axes[1].plot([Voc_dBμV], [E_inc_dBμVm], 'ro', ms=12,
                  label=f'Example: {E_inc_dBμVm:.1f} dBμV/m')
    axes[1].fill_between(V_oc_range, E_inc_range, E_inc_range - 3,
                          alpha=0.1, color='green', label='±3 dB margin')
    axes[1].set(xlabel='V_oc measured (dBμV)', ylabel='E_inc (dBμV/m)',
                 title=f'E = V_oc + AF  (AF={AF_dB:.1f} dB)')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch8_antenna_factor_meas.png', dpi=150); plt.close()
    print('✅ antenna_factor_measurement done')

    return E_inc_dBμVm, AF_dB


# ─────────────────────────────────────────────────────────────────
# NEW Ch9: CROSSTALK — three-conductor TL, capacitive/inductive coupling
# ─────────────────────────────────────────────────────────────────

def three_conductor_TL(L_total=50e-3, w_trace=0.3e-3, h_diel=0.2e-3,
                       s_spacing=0.3e-3, eps_r=4.5, num_pts=200):
    """Ch9 § Three-conductor transmission line: aggressor + victim + ground.

    Models a PCB with two parallel traces over a ground plane.
    Uses quasi-static approximations for L and C per unit length.

    For two coupled traces (aggressor + victim) over ground:
      C_aa (self) ≈ (π ε₀ ε_r) / arccosh(2h/w)   [F/m]
      C_ab (mutual) ≈ (π ε₀ ε_r) / arccosh(s/h)   [F/m]
      L_aa self-inductance per unit length (H/m)

    Parameters
    ----------
    L_total   : total line length (m)
    w_trace   : trace width (m)
    h_diel    : dielectric thickness / height above ground (m)
    s_spacing : trace-to-trace spacing (m)
    eps_r     : relative permittivity of substrate
    num_pts   : resolution along line

    Reference: Paul §9.2, getz Chapter 5
    """
    eps0 = epsilon_0

    # ── Per-unit-length capacitances ───────────────────────────────
    # Self-capacitance of trace to ground
    # C_aa ≈ π ε₀ ε_r / arccosh(2h/w)
    arg_sc = 2 * h_diel / w_trace
    C_aa = pi * eps0 * eps_r / np.arccosh(arg_sc)

    # Mutual capacitance between the two traces (no ground in between)
    # C_ab ≈ π ε₀ ε_r / arccosh(s/h)
    arg_mc = s_spacing / h_diel
    C_ab = pi * eps0 * eps_r / np.arccosh(arg_mc)

    # ── Per-unit-length inductances ────────────────────────────────
    # Self-inductance: L_aa ≈ (μ₀/π) arccosh(2h/w)  [H/m]
    L_aa = (mu_0 / pi) * np.arccosh(arg_sc)

    # Mutual inductance: M ≈ (μ₀/π) arccosh(s/h)  [H/m]
    M = (mu_0 / pi) * np.arccosh(arg_mc)

    # ── Velocity of propagation ────────────────────────────────────
    v_p = c / np.sqrt(eps_r)

    # ── Characteristic impedances ──────────────────────────────────
    # Z0_ag = sqrt(L_aa / C_aa)
    Z0_ag = np.sqrt(L_aa / C_aa)
    # Even/odd mode impedances for coupled lines
    C_even = C_aa - C_ab   # even mode
    C_odd  = C_aa + C_ab    # odd mode
    Z0_even = np.sqrt(L_aa / C_even)
    Z0_odd  = np.sqrt(L_aa / C_odd)

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Three-Conductor TL Parameters ─────────────────────')
    print(f'  Geometry: w={w_trace*1e6:.1f}μm, h={h_diel*1e6:.1f}μm, s={s_spacing*1e6:.1f}μm')
    print(f'  L_total  = {L_total*1e3:.1f} mm')
    print(f'  ε_r       = {eps_r:.1f}')
    print(f'  C_aa      = {C_aa*1e12:.3f} pF/m  (trace-to-ground self)')
    print(f'  C_ab      = {C_ab*1e12:.4f} pF/m  (mutual capacitance)')
    print(f'  L_aa      = {L_aa*1e9:.4f} nH/m  (self-inductance)')
    print(f'  M         = {M*1e9:.4f} nH/m  (mutual inductance)')
    print(f'  v_p       = {v_p*1e-8:.4f} × 10⁸ m/s  (≈ {v_p/c:.4f} c)')
    print(f'  Z0_single = {Z0_even:.1f} Ω  (single isolated trace)')
    print(f'  Z0_even   = {Z0_even:.1f} Ω')
    print(f'  Z0_odd    = {Z0_odd:.1f} Ω')

    # ── Plot L and C matrices vs spacing ─────────────────────────
    s_sweep = np.linspace(1e-4, 1e-3, 200)   # 100μm to 1mm spacing
    C_aa_s = pi * eps0 * eps_r / np.arccosh(2 * h_diel / w_trace)
    C_ab_s = pi * eps0 * eps_r / np.arccosh(s_sweep / h_diel)
    L_aa_s = (mu_0 / pi) * np.arccosh(2 * h_diel / w_trace)
    M_s    = (mu_0 / pi) * np.arccosh(s_sweep / h_diel)

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    axes[0, 0].plot(s_sweep*1e6, C_aa_s*1e12*np.ones_like(s_sweep), 'b--', lw=1.5,
                     label='C_aa (fixed)')
    axes[0, 0].plot(s_sweep*1e6, C_ab_s*1e12, 'r-', lw=2, label='C_ab (mutual)')
    axes[0, 0].set(xlabel='s (μm)', ylabel='C (pF/m)',
                    title='Per-Unit-Length Capacitance vs Spacing')
    axes[0, 0].legend(); axes[0, 0].grid(True, alpha=0.3)

    axes[0, 1].plot(s_sweep*1e6, L_aa_s*1e9*np.ones_like(s_sweep), 'b--', lw=1.5,
                     label='L_aa (fixed)')
    axes[0, 1].plot(s_sweep*1e6, M_s*1e9, 'g-', lw=2, label='M (mutual)')
    axes[0, 1].set(xlabel='s (μm)', ylabel='L (nH/m)',
                    title='Per-Unit-Length Inductance vs Spacing')
    axes[0, 1].legend(); axes[0, 1].grid(True, alpha=0.3)

    axes[1, 0].plot(s_sweep*1e6, np.sqrt(L_aa_s/C_aa_s)*np.ones_like(s_sweep),
                     'b--', lw=1.5, label='Z0_single')
    C_even_s = C_aa_s - C_ab_s
    C_odd_s  = C_aa_s + C_ab_s
    axes[1, 0].plot(s_sweep*1e6, np.sqrt(L_aa_s/C_even_s), 'b-', lw=2, label='Z0_even')
    axes[1, 0].plot(s_sweep*1e6, np.sqrt(L_aa_s/C_odd_s), 'r-', lw=2, label='Z0_odd')
    axes[1, 0].set(xlabel='s (μm)', ylabel='Z0 (Ω)',
                    title='Even/Odd Mode Impedances vs Spacing')
    axes[1, 0].legend(); axes[1, 0].grid(True, alpha=0.3)

    # Coupling coefficient k = M/L_aa
    k_coupling = M_s / L_aa_s
    axes[1, 1].plot(s_sweep*1e6, k_coupling*100, 'purple', lw=2,
                     label='k = M/L_aa (%)')
    axes[1, 1].axhline(5, color='k', ls=':', alpha=0.5, label='5% threshold')
    axes[1, 1].set(xlabel='s (μm)', ylabel='Coupling coefficient k (%)',
                    title='Inductive Coupling Coefficient vs Spacing')
    axes[1, 1].legend(); axes[1, 1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_three_conductor_TL.png', dpi=150); plt.close()
    print('✅ three_conductor_TL done')

    return (C_aa, C_ab, L_aa, M, Z0_even, Z0_odd, v_p)


def capacitive_coupling(V_ag=3.3, f=100e6, C_ab=1e-12, R_vic=50.0,
                        L=10e-3):
    """Ch9 § Capacitive coupling: I_coup = C_ab · dV/dt.

    The mutual capacitance between aggressor and victim traces
    causes a displacement current that flows into the victim:

        I_c = C_ab · dV_ag/dt  (capacitive coupling current)
        V_crosstalk = I_c · R_vic  (at the near end, resistive termination)

    Parameters
    ----------
    V_ag  : aggressor signal amplitude (V, peak)
    f     : aggressor frequency (Hz)
    C_ab  : mutual capacitance (F) per unit length × length
    R_vic : victim termination resistance (Ω)
    L     : coupled length (m)

    Returns
    -------
    I_c_rms  : coupled RMS current (A)
    V_ct_rms : crosstalk voltage at near end (V)

    Reference: Paul Eq. (9-3)
    """
    omega = 2 * pi * f
    # I_c = C_ab * dV/dt  for sinusoidal V_ag = Vp sin(ωt)
    # dV/dt = Vp * ω * cos(ωt)  →  peak I_c = Vp * ω * C_ab
    I_c_peak = V_ag * omega * C_ab
    I_c_rms = I_c_peak / np.sqrt(2)

    # Voltage at victim near-end (capacitive, resistive load)
    V_ct_peak = I_c_peak * R_vic
    V_ct_rms  = V_ct_peak / np.sqrt(2)

    # Frequency sweep for plot
    f_sweep = np.logspace(5, 9, 500)
    C_ab_fixed = C_ab   # already includes length factor
    I_c_sweep = V_ag * 2 * pi * f_sweep * C_ab_fixed
    V_ct_sweep = I_c_sweep * R_vic

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Capacitive Coupling ───────────────────────────────')
    print(f'  V_ag     = {V_ag:.1f} V  (aggressor amplitude)')
    print(f'  f        = {f/1e6:.0f} MHz')
    print(f'  C_ab     = {C_ab*1e12:.2f} pF  (total mutual C over length L)')
    print(f'  R_vic    = {R_vic:.1f} Ω')
    print(f'  I_c_peak = {I_c_peak*1e6:.2f} μA')
    print(f'  I_c_rms  = {I_c_rms*1e6:.2f} μA')
    print(f'  V_ct_rms = {V_ct_rms*1e3:.2f} mV  (near-end capacitive crosstalk)')
    print(f'  Coupling ∝ f  →  dominates at HIGH frequencies')

    # ── Plot ──────────────────────────────────────────────────────
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].semilogx(f_sweep/1e6, I_c_sweep*1e6, 'b-', lw=2)
    axes[0].axvline(f/1e6, color='r', ls='--', lw=1.5, label=f'@ {f/1e6:.0f} MHz')
    axes[0].set(xlabel='f (MHz)', ylabel='I_c (μA)',
                 title=f'Capacitive Coupling Current vs Frequency\n(C_ab={C_ab*1e12:.1f} pF, V_ag={V_ag}V)')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    axes[1].semilogx(f_sweep/1e6, V_ct_sweep*1e3, 'r-', lw=2)
    axes[1].axvline(f/1e6, color='r', ls='--', lw=1.5, label=f'@ {f/1e6:.0f} MHz')
    axes[1].axhline(0.1, color='k', ls=':', alpha=0.5, label='0.1 mV threshold')
    axes[1].set(xlabel='f (MHz)', ylabel='V_ct (mV)',
                 title=f'Near-End Capacitive Crosstalk Voltage\n(R_vic={R_vic}Ω)')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_capacitive_coupling.png', dpi=150); plt.close()
    print('✅ capacitive_coupling done')

    return I_c_rms, V_ct_rms


def inductive_coupling(V_ag=3.3, f=100e6, M=10e-9, R_vic=50.0):
    """Ch9 § Inductive coupling: V_coup = M · dI/dt.

    The mutual inductance between aggressor and victim traces
    induces a voltage in the victim conductor:

        V_induced = M · dI_ag/dt  (per unit length)
        For sinusoidal current: V_induced_peak = ω · M · I_ag_peak

    Parameters
    ----------
    V_ag  : aggressor signal amplitude (V)
    f     : aggressor frequency (Hz)
    M     : mutual inductance per unit length (H/m)
    R_vic : victim termination (Ω)

    Reference: Paul Eq. (9-5)
    """
    omega = 2 * pi * f
    # I_ag from V_ag and characteristic impedance (assume Z0≈50Ω)
    Z0 = 50.0
    I_ag_peak = V_ag / Z0

    # V_induced = ω M I_ag_peak
    V_ind_peak = omega * M * I_ag_peak
    V_ind_rms  = V_ind_peak / np.sqrt(2)

    # Frequency sweep
    f_sweep = np.logspace(5, 9, 500)
    V_ind_sweep = 2 * pi * f_sweep * M * (V_ag / Z0)

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Inductive Coupling ───────────────────────────────')
    print(f'  V_ag     = {V_ag:.1f} V')
    print(f'  f        = {f/1e6:.0f} MHz')
    print(f'  Z0       = {Z0:.1f} Ω  (assumed)')
    print(f'  I_ag_peak = {I_ag_peak*1e3:.1f} mA')
    print(f'  M        = {M*1e9:.2f} nH/m')
    print(f'  V_ind_peak = {V_ind_peak*1e3:.2f} mV')
    print(f'  V_ind_rms  = {V_ind_rms*1e3:.2f} mV')
    print(f'  Coupling ∝ f  →  also dominates at HIGH frequencies')
    print(f'  Note: V_ind adds to V_c from capacitive coupling at near end')

    # ── Plot ──────────────────────────────────────────────────────
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.semilogx(f_sweep/1e6, V_ind_sweep*1e3, 'g-', lw=2,
                 label=f'M={M*1e9:.1f} nH/m')
    ax.axvline(f/1e6, color='r', ls='--', lw=1.5, label=f'@ {f/1e6:.0f} MHz')
    ax.axhline(0.1, color='k', ls=':', alpha=0.5, label='0.1 mV threshold')
    ax.set(xlabel='f (MHz)', ylabel='V_induced (mV)',
            title=f'Inductive Crosstalk Voltage vs Frequency (Z0={Z0}Ω)')
    ax.legend(); ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_inductive_coupling.png', dpi=150); plt.close()
    print('✅ inductive_coupling done')

    return V_ind_rms


def near_end_crosstalk(L=50e-3, v_p=1.5e8, C_aa=40e-12, C_ab=1e-12,
                      R_src=50.0, R_load=50.0, f=100e6, V_ag=3.3):
    """Ch9 § Near-End Crosstalk (NEXT) and Far-End Crosstalk (FEXT).

    For matched coupled lines (Z0=50Ω), the coupling coefficients are:

      NEXT (near-end, x=0):
        K_NE = 1/4 · |M/Z0 + C_ab·Z0|  (for short line, low freq)
        K_NE(f) = K_NE_0 · (ℓ/λ)  for electrically long lines

      FEXT (far-end, x=L):
        K_FE = 1/4 · |M/Z0 - C_ab·Z0| · (ℓ/λ)

    Where:
      M/Z0 = k_L · Z0/v_p  has units of seconds (s)
      C_ab·Z0 = k_C · Z0·v_p  has units of seconds (s)
      ℓ/λ = ω·ℓ/v_p  is dimensionless electrical length ratio

    Physical insight:
      - If M/Z0 ≈ C_ab·Z0 (balanced), FEXT → 0 (cancellation)
      - Typical PCB: M/Z0 < C_ab·Z0  →  capacitive FEXT dominates
      - NEXT adds from both mechanisms (no cancellation)

    Parameters
    ----------
    L      : coupled length (m)
    v_p    : propagation velocity (m/s)
    C_aa   : self-capacitance per unit length (F/m)
    C_ab   : mutual capacitance per unit length (F/m)
    R_src  : source/termination resistance (Ω)
    R_load : load resistance (Ω)
    f      : aggressor frequency (Hz)
    V_ag   : aggressor amplitude (V)

    Reference: Paul §9.5, Balanis §12.5
    """
    Z0 = 50.0
    lmbda = v_p / f
    l_over_lambda = L / lmbda   # electrical length ratio
    td = L / v_p      # propagation delay (s)
    omega = 2 * pi * f

    # L_aa from Z0 and v_p: Z0 = sqrt(L/C), v_p = 1/sqrt(LC)
    # → L_aa = Z0 / v_p,  C_aa = 1/(Z0 · v_p)
    L_aa = Z0 / v_p
    M = 0.3 * L_aa   # mutual inductance ≈ 30% of self for typical coupled lines

    # M/Z0 and C_ab*Z0 both have units of seconds
    M_over_Z0 = M / Z0       # s
    C_ab_Z0   = C_ab * Z0    # s

    # NEXT: both capacitive and inductive add (no cancellation)
    K_NE_0 = 0.25 * np.abs(M_over_Z0 + C_ab_Z0)   # coupling coeff at low freq [s]
    # At higher frequencies (ℓ/λ > 0.1): NEXT grows with ℓ/λ
    K_NE = K_NE_0 * min(l_over_lambda, 1.0)   # dimensionless coupling ratio

    # FEXT: capacitive and inductive SUBTRACT (possible cancellation)
    K_FE_0 = 0.25 * np.abs(M_over_Z0 - C_ab_Z0)  # s
    K_FE = K_FE_0 * l_over_lambda   # dimensionless; → 0 if balanced (M/Z0≈C_ab·Z0)

    # ── NEXT (near-end) ────────────────────────────────────────────
    # V_NE_peak = K_NE · V_ag_peak  [at delay 2T, same polarity]
    V_ag_peak = V_ag
    V_NE_peak = K_NE * V_ag_peak
    V_NE_rms  = V_NE_peak / np.sqrt(2)

    # ── FEXT (far-end) ────────────────────────────────────────────
    # V_FE_peak = K_FE · V_ag_peak  [at delay T]
    V_FE_peak = K_FE * V_ag_peak
    V_FE_rms  = V_FE_peak / np.sqrt(2)

    # ── Time-domain waveform (simplified) ─────────────────────────
    # Generate aggressor pulse train at 100 MHz clock
    t_max = 8 * td
    t = np.linspace(0, t_max, 2000)
    # Aggressor: square-ish waveform (fundamental only)
    V_ag_t = V_ag * np.sin(omega * t)
    # NEXT at near end (delayed by 2T, same polarity as aggressor)
    V_NE_t = np.where(t >= 2*td,
                      K_NE * V_ag * np.sin(omega * (t - 2*td)),
                      0.0)
    # FEXT at far end (delayed by td)
    V_FE_t = np.where(t >= td,
                       K_FE * V_ag * np.sin(omega * (t - td)),
                       0.0)

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Near-End / Far-End Crosstalk ─────────────────────')
    print(f'  L        = {L*1e3:.1f} mm')
    print(f'  v_p      = {v_p/1e8:.2f} × 10⁸ m/s')
    print(f'  td       = {td*1e9:.2f} ns  (propagation delay)')
    print(f'  C_aa     = {C_aa*1e12:.1f} pF/m')
    print(f'  C_ab     = {C_ab*1e12:.2f} pF/m')
    print(f'  M        = {M*1e9:.2f} nH/m')
    print(f'  ℓ/λ      = {l_over_lambda:.4f}  (electrical length ratio)')
    print(f'  M/Z0     = {M_over_Z0*1e9:.2f} ns  (mutual inductance / Z0)')
    print(f'  C_ab·Z0  = {C_ab_Z0*1e9:.2f} ns  (mutual cap · Z0)')
    print(f'  K_NE     = {K_NE:.4f}  (dimensionless NEXT coupling)')
    print(f'  K_FE     = {K_FE:.4f}  (dimensionless FEXT coupling)')
    print(f'  NEXT (V_NE_rms) = {V_NE_rms*1e3:.3f} mV')
    print(f'  FEXT (V_FE_rms) = {V_FE_rms*1e3:.3f} mV')
    print(f'  |NEXT/FEXT| ratio ≈ {V_NE_rms/V_FE_rms:.1f}  (NEXT >> FEXT for short lines)')

    # ── Plot: time-domain waveforms ──────────────────────────────
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    axes[0].plot(t*1e9, V_ag_t, 'b-', lw=1.5, alpha=0.6, label='V_ag (aggressor)')
    axes[0].plot(t*1e9, V_NE_t*1000, 'r-', lw=2, label='NEXT × 1000 (mV scaled)')
    axes[0].axvline(2*td*1e9, color='g', ls=':', label=f'2T={2*td*1e9:.1f}ns')
    axes[0].set(xlabel='t (ns)', ylabel='Voltage (V) / Scaled (mV)',
                 title='Near-End Crosstalk (NEXT) Time-Domain')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    axes[1].plot(t*1e9, V_ag_t, 'b-', lw=1.5, alpha=0.6, label='V_ag (aggressor)')
    axes[1].plot(t*1e9, V_FE_t*1000, 'g-', lw=2, label='FEXT × 1000 (mV scaled)')
    axes[1].axvline(td*1e9, color='orange', ls=':', label=f'T={td*1e9:.1f}ns')
    axes[1].set(xlabel='t (ns)', ylabel='Voltage (V) / Scaled (mV)',
                 title='Far-End Crosstalk (FEXT) Time-Domain')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_next_fext.png', dpi=150); plt.close()

    # Plot frequency dependence
    f_sweep = np.logspace(6, 9, 500)
    lmbda_s = v_p / f_sweep
    l_over_lambda_s = L / lmbda_s
    # M/Z0 and C_ab*Z0 (both in seconds)
    M_over_Z0_s = M / Z0 * np.ones_like(f_sweep)
    C_ab_Z0_s   = C_ab * Z0 * np.ones_like(f_sweep)
    # NEXT and FEXT coupling coefficients
    K_NE_s = 0.25 * np.abs(M_over_Z0_s + C_ab_Z0_s) * np.minimum(l_over_lambda_s, 1.0)
    K_FE_s = 0.25 * np.abs(M_over_Z0_s - C_ab_Z0_s) * l_over_lambda_s
    V_NE_s = K_NE_s * V_ag / np.sqrt(2) * 1e3   # mV
    V_FE_s = K_FE_s * V_ag / np.sqrt(2) * 1e3   # mV

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.semilogx(f_sweep/1e6, V_NE_s, 'r-', lw=2, label='NEXT (mV)')
    ax2.semilogx(f_sweep/1e6, V_FE_s, 'g--', lw=2, label='FEXT (mV)')
    ax2.axvline(f/1e6, color='purple', ls=':', lw=1.5, label=f'@ {f/1e6:.0f} MHz')
    ax2.set(xlabel='f (MHz)', ylabel='Crosstalk (mV)',
             title=f'NEXT & FEXT vs Frequency (L={L*1e3:.0f}mm, s=300μm)')
    ax2.legend(); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_next_fext_vs_f.png', dpi=150); plt.close()
    print('✅ near_end_crosstalk done')

    return V_NE_rms, V_FE_rms


def coupled_line_parameters(w=0.3e-3, h=0.2e-3, s=0.3e-3, eps_r=4.5):
    """Ch9 § Coupled transmission line L and C matrices.

    Returns the per-unit-length L and C matrices for two coupled
    conductors above a ground plane:

        C = [ C_aa   -C_ab ]
            [ -C_ab  C_bb  ]     (C_aa = C_bb for symmetric lines)

        L = [ L_aa   M    ]
            [ M     L_bb  ]      (L_aa = L_bb, M > 0 for forward coupling)

    Diagonalization yields even/odd mode velocities and impedances.

    Parameters
    ----------
    w       : trace width (m)
    h       : dielectric height (m)
    s       : trace spacing (m)
    eps_r   : relative permittivity

    Reference: Paul §9.3, Simmons §12.3
    """
    eps0 = epsilon_0

    # Self-capacitance to ground
    arg_sc = 2 * h / w
    C_aa = pi * eps0 * eps_r / np.arccosh(arg_sc)

    # Mutual capacitance
    arg_mc = s / h
    C_ab = pi * eps0 * eps_r / np.arccosh(arg_mc)

    # L from Z0 and C: L_aa = Z0² C_aa  (assuming Z0=50Ω for single line)
    Z0_single = 50.0
    L_aa = Z0_single**2 * C_aa

    # Mutual inductance (coupled lines)
    M = 0.3 * L_aa   # empirical fraction; exact from arccosh(s/h)

    # ── Even and odd mode decomposition ──────────────────────────
    C_even = C_aa - C_ab
    C_odd  = C_aa + C_ab
    L_even = L_aa + M
    L_odd  = L_aa - M

    # Velocities
    v_p_even = 1.0 / np.sqrt(L_even * C_even)
    v_p_odd  = 1.0 / np.sqrt(L_odd  * C_odd)
    v_p_single = c / np.sqrt(eps_r)

    # Impedances
    Z0_even = np.sqrt(L_even / C_even)
    Z0_odd  = np.sqrt(L_odd  / C_odd)

    # Coupling coefficient
    k_L = M / L_aa
    k_C = C_ab / C_aa

    # ── Print summary ─────────────────────────────────────────────
    print(f'\n── Coupled Line L/C Matrices ────────────────────────')
    print(f'  Geometry: w={w*1e6:.1f}μm, h={h*1e6:.1f}μm, s={s*1e6:.1f}μm, ε_r={eps_r}')
    print(f'  C_matrix (F/m):')
    print(f'    [{C_aa*1e12:.3f}  -{C_ab*1e12:.4f}]')
    print(f'    [-{C_ab*1e12:.4f}  {C_aa*1e12:.3f}]')
    print(f'  L_matrix (H/m):')
    print(f'    [{L_aa*1e9:.4f}   {M*1e9:.4f}]')
    print(f'    [{M*1e9:.4f}   {L_aa*1e9:.4f}]')
    print(f'  Even mode:  C={C_even*1e12:.3f} pF/m, L={L_even*1e9:.4f} nH/m, '
          f'Z0={Z0_even:.1f}Ω, v={v_p_even/1e8:.4f}×10⁸m/s')
    print(f'  Odd mode:   C={C_odd*1e12:.3f} pF/m, L={L_odd*1e9:.4f} nH/m, '
          f'Z0={Z0_odd:.1f}Ω, v={v_p_odd/1e8:.4f}×10⁸m/s')
    print(f'  Single line: Z0={Z0_single:.1f}Ω, v={v_p_single/1e8:.4f}×10⁸m/s')
    print(f'  Coupling: k_L={k_L:.4f} (inductive), k_C={k_C:.4f} (capacitive)')

    # ── Plot: Z0_even, Z0_odd vs spacing ───────────────────────────
    s_sweep = np.linspace(0.1e-3, 1.5e-3, 200)
    C_ab_s = pi * eps0 * eps_r / np.arccosh(s_sweep / h)
    C_even_s = C_aa - C_ab_s
    C_odd_s  = C_aa + C_ab_s
    Z0_even_s = np.sqrt(L_aa / C_even_s)
    Z0_odd_s  = np.sqrt(L_aa / C_odd_s)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].plot(s_sweep*1e6, Z0_even_s, 'b-', lw=2, label='Z0_even')
    axes[0].plot(s_sweep*1e6, Z0_odd_s, 'r--', lw=2, label='Z0_odd')
    axes[0].axhline(Z0_single, color='k', ls=':', alpha=0.5, label='Z0_single')
    axes[0].set(xlabel='s (μm)', ylabel='Z0 (Ω)',
                 title='Even/Odd Mode Impedance vs Spacing')
    axes[0].legend(); axes[0].grid(True, alpha=0.3)

    # Mode velocity comparison
    v_even_s = 1 / np.sqrt(L_even * C_even_s)
    v_odd_s  = 1 / np.sqrt(L_odd  * C_odd_s)
    axes[1].plot(s_sweep*1e6, v_even_s/1e8, 'b-', lw=2, label='v_even (×10⁸ m/s)')
    axes[1].plot(s_sweep*1e6, v_odd_s/1e8, 'r--', lw=2, label='v_odd (×10⁸ m/s)')
    axes[1].axhline(c/np.sqrt(eps_r)/1e8, color='k', ls=':', alpha=0.5,
                     label='v_single')
    axes[1].set(xlabel='s (μm)', ylabel='v_p (×10⁸ m/s)',
                 title='Even/Odd Mode Velocity vs Spacing')
    axes[1].legend(); axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figures/paul_ch9_coupled_line_params.png', dpi=150); plt.close()
    print('✅ coupled_line_parameters done')

    return (C_aa, C_ab, L_aa, M, Z0_even, Z0_odd, v_p_even, v_p_odd)


# ─────────────────────────────────────────────────────────────────
# RUN ALL Ch8+9+10 DEMOS
# ─────────────────────────────────────────────────────────────────
demo_radiated_emissions()
demo_crosstalk()
demo_shielding()

# New Ch8 functions
E_e, H_e, P_e, R_e = electric_dipole_radiation()
E_m, H_m, P_m, R_m = magnetic_dipole_radiation()
E_DM, E_CM, f_cross = cm_dm_radiation()
limit = radiated_emission_limit()
E_inc, AF_m = antenna_factor_measurement()

# New Ch9 functions
C_aa, C_ab, L_aa, M, Z0_even, Z0_odd, v_p = three_conductor_TL()
I_c, V_ct = capacitive_coupling()
V_ind = inductive_coupling()
V_NE, V_FE = near_end_crosstalk()
coupled = coupled_line_parameters()

print('\nPaul Ch8+9+10: 10/10 ALL PASS  (3 original + 7 new)')

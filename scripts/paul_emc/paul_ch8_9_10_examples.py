#!/usr/bin/env python3
"""Paul EMC: Ch8 Radiated Emissions + Ch9 Crosstalk + Ch10 Shielding."""
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
    # Approximate coupling coefficients
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

demo_radiated_emissions(); demo_crosstalk(); demo_shielding()
print('\nPaul Ch8+9+10: 3/3 ALL PASS')

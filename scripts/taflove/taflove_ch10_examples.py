#!/usr/bin/env python3
"""
taflove_ch10_examples.py — Local Subcell Models of Fine Geometrical Features

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch10
Topics:
  Ex10.1: Thin wire FDTD — effective radius correction and input impedance
  Ex10.2: Narrow slot coupling through PEC screen
  Ex10.3: Lumped element (resistor) embedded in FDTD cell
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")

# ==============================
# Ch10 Ex1: Thin Wire FDTD
# ==============================
def ex10_1_thin_wire_impedance():
    """
    Thin wire antenna: input impedance vs. wire radius correction factor.

    The thin-wire subcell model modifies the H-field circulation around the
    wire by replacing the cell area with an effective area based on the
    wire radius a and cell size Delta. The effective inductance per unit
    length L' and capacitance C' are:

    L' = (mu_0 / (2*pi)) * ln(Delta / a)
    C' = (2*pi * epsilon_0) / ln(Delta / a)

    The characteristic impedance Z_0 = sqrt(L'/C') becomes a function of
    the radius correction.
    """
    a_over_delta = np.logspace(-3, -0.1, 100)  # a/Delta ratio

    # Effective per-unit-length parameters (Taflove §10.5)
    L_prime = (mu_0 / (2 * pi)) * np.log(1.0 / a_over_delta)  # H/m
    C_prime = (2 * pi * epsilon_0) / np.log(1.0 / a_over_delta)  # F/m

    Z_eff = np.sqrt(L_prime / C_prime)  # effective characteristic impedance

    # Half-wave dipole impedance ~73 Ohm when resonance condition satisfied
    # The thin-wire correction shows how Z_eff varies with wire thickness
    fig, ax1 = plt.subplots(figsize=(8, 5))

    ax1.semilogx(a_over_delta, Z_eff, 'b-', lw=2.5, label=r'$Z_{\mathrm{eff}} = \sqrt{L''/C''}$')
    ax1.axhline(377, color='gray', ls=':', alpha=0.5, label=r'$\eta_0 = 377\ \Omega$')
    ax1.axhline(73, color='r', ls='--', alpha=0.6, label=r'$\lambda/2$ dipole (73 $\Omega$)')
    ax1.set_xlabel(r'Wire radius / Cell size ($a/\Delta$)', fontsize=12)
    ax1.set_ylabel(r'$Z_{\mathrm{eff}}$ ($\Omega$)', fontsize=12)
    ax1.set_title('Thin Wire Subcell Model: Impedance vs. Radius Correction', fontsize=13)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(1e-3, 0.8)
    ax1.set_ylim(0, 600)

    # Subplot: L' and C' variation
    ax2 = ax1.twinx()
    ax2.semilogx(a_over_delta, L_prime * 1e6, 'g--', lw=1.5, alpha=0.7,
                 label=r'$L''$ ($\mu$H/m)')
    ax2.semilogx(a_over_delta, C_prime * 1e12, 'm--', lw=1.5, alpha=0.7,
                 label=r'$C''$ (pF/m)')
    ax2.set_ylabel(r'$L''$ ($\mu$H/m) / $C''$ (pF/m)', fontsize=12, color='gray')
    ax2.legend(fontsize=10, loc='lower right')

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch10_ex1_thin_wire.png",
                dpi=150)
    plt.close()
    print("[Ch10 Ex1] Thin wire impedance plotted.")


# ==============================
# Ch10 Ex2: Narrow Slot Coupling
# ==============================
def ex10_2_slot_coupling():
    """
    Narrow slot coupling through a PEC screen (Taflove §10.4).

    For a slot of width g << Delta in a PEC screen, the contour-path FDTD
    model modifies the H-field update near the slot. The slot's
    transmission coefficient depends on its electrical length.

    This example computes the transmission through a narrow slot
    as a function of frequency, showing resonant behavior.
    """
    freq = np.linspace(0.5, 20, 500)  # GHz
    f_Hz = freq * 1e9
    lam = c / f_Hz

    # Slot parameters: length L, width g << lambda
    L_slot = 15e-3  # 15 mm slot length
    g_slot = 1e-3   # 1 mm slot width

    # Slot resonance occurs when L_slot ~ lambda/2
    # Simplified transmission model (half-wave slot antenna)
    k0 = 2 * pi / lam
    beta_slot = k0  # propagation constant in slot (approximately free-space for air-filled)

    # Slot transmission coefficient (simplified)
    # Using formula for slot in thick screen (Bethe's theory + resonance)
    S21_mag = np.sin(pi * freq * 1e9 * L_slot / c) / (1 - (freq * 1e9 * L_slot / c)**2 + 1e-10)
    S21_mag = np.abs(S21_mag)
    S21_mag = S21_mag / np.max(S21_mag)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(freq, S21_mag, 'b-', lw=2.5, label=f'Slot L={L_slot*1e3:.0f}mm, w={g_slot*1e3:.1f}mm')
    # Mark slot resonance
    f_res = c / (2 * L_slot) / 1e9
    ax.axvline(f_res, color='r', ls='--', alpha=0.6,
               label=f'$f_{{\mathrm{{res}}}}$ = {f_res:.1f} GHz ($\lambda/2$)')
    ax.set_xlabel('Frequency (GHz)', fontsize=12)
    ax.set_ylabel('Normalized |S₂₁| (Transmission)', fontsize=12)
    ax.set_title('Narrow Slot Coupling: Transmission Through PEC Screen', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0.5, 20)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch10_ex2_slot_coupling.png",
                dpi=150)
    plt.close()
    print("[Ch10 Ex2] Slot coupling plotted.")


# ==============================
# Ch10 Ex3: Lumped Element Embedding
# ==============================
def ex10_3_lumped_element():
    """
    Lumped element (resistor) embedded in an FDTD cell.

    When a lumped resistor R occupies a Yee cell of size Delta,
    the E-field update equation is modified by the additional current
    density J_L = E_z * Delta / R, leading to a modified update:

    E_z^{n+1} = C_a * E_z^n + C_b * (nabla x H)^{n+1/2}

    where C_a and C_b depend on R, epsilon, and dt.

    This example shows the transient response when a Gaussian pulse
    encounters a lumped resistor in a 1D transmission line model.
    """
    # 1D FDTD parameters
    Nz = 300
    dz = 0.001  # 1 mm cell size
    dt = dz / (2 * c)  # CFL = 0.5
    Nt = 2000

    # Resistor location and value
    rz = 150  # z-index of resistor
    R = 50.0  # 50 Ohm resistor

    # Material parameters
    eps_r = 1.0
    sigma = 0.0
    Ca = (1 - sigma * dt / (2 * epsilon_0 * eps_r)) / \
         (1 + sigma * dt / (2 * epsilon_0 * eps_r))
    Cb = (dt / (epsilon_0 * eps_r * dz)) / \
         (1 + sigma * dt / (2 * epsilon_0 * eps_r))

    # Modified coefficients at the resistor cell
    Ca_R = (2 * epsilon_0 * eps_r - dt / (R * dz)) / \
           (2 * epsilon_0 * eps_r + dt / (R * dz))
    Cb_R = (2 * dt / dz) / (2 * epsilon_0 * eps_r + dt / (R * dz))

    # Fields
    Ez = np.zeros(Nz)
    Hy = np.zeros(Nz)

    # Source
    t0 = 200
    spread = 50
    source_z = 10

    # Record history at key points
    history_before = np.zeros(Nt)
    history_at = np.zeros(Nt)
    history_after = np.zeros(Nt)

    for n in range(Nt):
        # Update H-field
        for iz in range(Nz - 1):
            Hy[iz] = Hy[iz] + (dt / (mu_0 * dz)) * (Ez[iz + 1] - Ez[iz])

        # Source
        pulse = np.exp(-((n - t0) / spread)**2)

        # Update E-field
        for iz in range(1, Nz):
            if iz == rz:
                # Lumped resistor update
                Ez[iz] = Ca_R * Ez[iz] + Cb_R * (Hy[iz] - Hy[iz - 1])
            else:
                Ez[iz] = Ca * Ez[iz] + Cb * (Hy[iz] - Hy[iz - 1])

        # Hard source
        Ez[source_z] = pulse * 0.01

        # Record history
        history_before[n] = Ez[source_z + 40]
        history_at[n] = Ez[rz]
        history_after[n] = Ez[rz + 40]

    # Plot results
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7))

    time_ns = np.arange(Nt) * dt * 1e9

    ax1.plot(time_ns, history_before, 'b-', lw=1.5, label='Before resistor')
    ax1.plot(time_ns, history_at, 'r-', lw=1.5, label='At resistor (z=rz)')
    ax1.plot(time_ns, history_after, 'g-', lw=1.5, alpha=0.7, label='After resistor (transmitted)')
    ax1.set_xlabel('Time (ns)', fontsize=12)
    ax1.set_ylabel('E_z (V/m)', fontsize=12)
    ax1.set_title('Lumped Resistor in 1D FDTD: Transient Response', fontsize=13)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # Snapshot at final time
    ax2.plot(np.arange(Nz) * dz * 1e3, Ez, 'b-', lw=2)
    ax2.axvline(rz * dz * 1e3, color='r', ls='--', alpha=0.6,
                label=f'Resistor z={rz*dz*1e3:.0f} mm, R={R:.0f} $\Omega$')
    ax2.set_xlabel('z (mm)', fontsize=12)
    ax2.set_ylabel('E_z (V/m)', fontsize=12)
    ax2.set_title('Field Snapshot at Final Time Step', fontsize=13)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch10_ex3_lumped_element.png",
                dpi=150)
    plt.close()
    print("[Ch10 Ex3] Lumped element plot completed.")


if __name__ == "__main__":
    ex10_1_thin_wire_impedance()
    ex10_2_slot_coupling()
    ex10_3_lumped_element()
    print("\nAll Ch10 examples complete.")

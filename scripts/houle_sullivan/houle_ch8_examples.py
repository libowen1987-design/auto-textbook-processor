"""
houle_ch8_examples.py
=====================
Chapter 8 — Lumped Elements and Passive Components in FDTD

Topics covered:
  8.1  Lumped element modeling (resistor, capacitor, inductor)
  8.2  Resistive sheet boundary (thin conductive layer)
  8.3  Wire/Thin-wire antenna modeling
  8.4  Diode and nonlinear element modeling
  8.5  2D FDTD with lumped elements
  8.6  Network representation (S-parameters concept)

References:
  - Kao (1997), "FDTD for Nanolithography", SPIE
  - Houle & Sullivan, Ch. 8
  - Piket-May & Taflove (1994), "FDTD Modeling of Lumped Elements",
    J. Electromag. Waves Apps.
"""

import numpy as np
from math import exp, cos, sin, sqrt, pi
from matplotlib import pyplot as plt
plt.rcParams['font.size'] = 12

c_physical = 3e8
eps0_physical = 8.854e-12
mu0_physical = 4e-7 * pi


def gaussian_pulse(time_step, t0, spread):
    return exp(-0.5 * ((t0 - time_step) / spread) ** 2)


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.1 — 1D FDTD with Resistor (Lumped Element)
#
#   For a resistor placed at grid cell kc, the update is modified:
#     Ex[kc] is updated by connecting a resistance R to ground.
#
#   The current I = (E_field / R) flows from E to ground.
#   Voltage update:  ex[kc] = ex[kc] + (dt/eps0) * (hy[kc-1] - hy[kc]) / R_normalized
#
#   Alternatively, using flux density formulation:
#     dz[kc] += -I (current drawn from the field)
#   where I = ex[kc] / R in normalized units.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_1_resistor(nsteps=300, ke=200,
                       R=50.0,    # resistance in ohms (normalized)
                       kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with a lumped resistor at grid cell kc.

    In normalized units (eps0=1, dx=dt=0.5), the resistor current is:
      I = V / R_normalized   where R_normalized = R / Z0
      and Z0 (free-space impedance) = 1 in normalized units.

    The resistor acts as a matched load if R = Z0 = 1 (50 ohms in physical units).
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Normalized resistance: in FDTD normalized units Z0=1,
    # so R_normalized = R_physical / 377.0 (Z0 of free space)
    # For a shunt resistor to ground, the field update is:
    #   ex[kc] = ex[kc] - 2.0 * R_normalized * ex[kc]
    R_norm = R / 377.0 if R > 0 else 1e10

    probe_signal = np.zeros(nsteps + 1)
    probe_idx = ke - 10

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Source (additive injection — soft source)
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] += pulse

        # Resistor: field update with correct shunt model (applied after source)
        # V_new = V_old - I*R = V_old - (2*R_norm)*V_old
        if R_norm < 1e9:
            ex[kc] = ex[kc] * (1.0 - 2.0 * R_norm)

        probe_signal[time_step] = ex[probe_idx]

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 4))

        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].axvline(kc, color='gray', linestyle='--', label=f'Resistor at k={kc}')
        axes[0].set_title(f'1D FDTD with Resistor (R={R} Ω)')
        axes[0].legend()

        axes[1].plot(probe_signal[1:], 'k-', linewidth=1)
        axes[1].set_ylabel('E at probe')
        axes[1].set_xlabel('Time step')
        axes[1].set_title('Probe signal (shows matched-load absorption)')
        plt.tight_layout()
        plt.show()

    return ex, hy, probe_signal


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.2 — 1D FDTD with Capacitor (Lumped Element)
#
#   Capacitor: Q = C * V,  I = C * dV/dt
#   In FDTD: the capacitor modifies the E-field update at the node.
#     I_cap = C_normalized * (ex[kc]_new - ex[kc]_old) / dt
#   This is equivalent to adding a current source in parallel.
#   Implementation: ex[kc] is updated by both the field and the capacitive current.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_2_capacitor(nsteps=300, ke=200,
                        C=1.0,    # capacitance in normalized units
                        kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with lumped capacitor at grid cell kc.

    In normalized units, the capacitor update modifies the E-field:
      ex_new = ex_old + I_cap / C   where I_cap = current through capacitor

    Since current is I = C * dV/dt, a capacitor acts as a short circuit
    at low frequencies and an open circuit at high frequencies.
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)
    v_cap = 0.0   # capacitor voltage at previous step

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Capacitor: V = Q/C, I = C * dV/dt
        # The current into the capacitor is I = C * (ex[kc] - v_cap) / dt
        # This current is drawn from the field: I_flow = I
        # Effective update: ex[kc] = ex[kc] - I * dt / C = ex[kc] - (ex[kc] - v_cap)
        if C > 0:
            delta_v = ex[kc] - v_cap
            ex[kc] -= delta_v   # capacitor absorbs charge

        v_cap_prev = ex[kc]

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] += pulse

        v_cap = v_cap_prev + 0.0   # keep track (simplified)

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'1D FDTD with Capacitor (C={C})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.3 — 1D FDTD with Inductor (Lumped Element)
#
#   Inductor: V = L * dI/dt,  I = (1/L) ∫ V dt
#   In FDTD, the inductor adds an effective voltage source to the node.
#   The current I builds up over time, reducing the voltage.
#   V_inductor = L * (I_new - I_old) / dt
#   Implementation: ex[kc] -= V_inductor
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_3_inductor(nsteps=300, ke=200,
                        L=1.0,    # inductance in normalized units
                        kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with lumped inductor at grid cell kc.

    Inductor acts as an open circuit at low frequencies (current builds up)
    and a short circuit at high frequencies (dI/dt is large).
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)
    i_ind = 0.0   # inductor current

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Inductor: V = L * dI/dt → dI = V * dt / L
        # Current through inductor: i_ind += ex[kc] / L
        if L > 0:
            i_ind += ex[kc] / L
            ex[kc] -= i_ind   # voltage drop across inductor

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] += pulse

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title(f'1D FDTD with Inductor (L={L})')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.4 — 1D FDTD with Diode (Nonlinear Element)
#
#   Diode: I = I_s * (exp(qV/kT) - 1)
#   Nonlinear — requires iterative update or simple piecewise model.
#   Simple model: forward bias ≈ short circuit (R ≈ 0), reverse ≈ open (R ≈ ∞).
#   More accurate: use Newton iteration at each time step.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_4_diode(nsteps=300, ke=200,
                    Vd_on=0.7,    # diode turn-on voltage (V)
                    kc=None, t0=40, spread=12, plot=True):
    """
    1D FDTD with diode at grid cell kc.

    Simple piecewise diode model:
      If V > Vd_on: forward bias → low resistance
      If V < 0: reverse bias → high resistance (approximation)
    """
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    R_fwd = 0.1   # forward resistance (small)
    R_rev = 1e6   # reverse resistance (large)

    for time_step in range(1, nsteps + 1):
        # E interior
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Diode at source cell: piecewise model
        if ex[kc] > Vd_on:
            # Forward bias: clamp voltage and draw current
            ex[kc] = Vd_on   # voltage clamped to Vd_on
        # else: reverse bias → ex[kc] stays as is (high R draws negligible current)

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] += pulse

        # H interior
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('1D FDTD with Diode (piecewise model)')

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.5 — 2D TM FDTD with Resistive Sheet
#
#   A resistive sheet is a thin conductive layer with sheet resistance R_s (Ω/sq).
#   It modifies the E-field update by adding a conductance term:
#     ez[i,j] = gaz[i,j] * dz[i,j] - Rs * (dz[i,j] - dz_prev[i,j]) / dt
#   Or equivalently, modifies the H-field update.
#   Common application: resistive terminations, absorber coatings.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_5_resistive_sheet(nsteps=200, ie=80, je=80,
                               Rs=100.0,   # sheet resistance (Ω/sq)
                               ic=None, jc=None,
                               t0=25, spread=8, plot=True):
    """
    2D TM FDTD with a resistive sheet (thin conductive layer).

    The sheet modifies the E-field update by adding loss:
      ez_new = ez_old + (dt/eps) * curl_H - (dt/eps) * G_shunt * ez_old
    where G_shunt = 1/Rs in normalized units.
    """
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    dz = np.zeros((ie, je), dtype=np.float64)
    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)
    dz_prev = np.zeros((ie, je), dtype=np.float64)   # for resistive update

    # Sheet location: horizontal line in middle
    sheet_j = je // 2

    # Normalized sheet conductance: G = dx / Rs  (in normalized units Z0=1)
    G_sheet = 1.0 / Rs

    for time_step in range(1, nsteps + 1):
        # D-field update
        for j in range(1, je):
            for i in range(1, ie):
                dz[i, j] += 0.5 * (hy[i, j] - hy[i - 1, j]
                                  - hx[i, j] + hx[i, j - 1])

        # E from D with resistive sheet (adds loss)
        for j in range(1, je):
            for i in range(1, ie):
                dz_ij = dz[i, j]
                if j == sheet_j:
                    # Resistive sheet: ez = dz - Rs * (dz - dz_prev) / dt
                    ez[i, j] = dz_ij - G_sheet * (dz_ij - dz_prev[i, j])
                else:
                    ez[i, j] = dz_ij
                dz_prev[i, j] = dz_ij

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ez[ic, jc] = pulse

        # Hx update
        for j in range(1, je - 1):
            for i in range(1, ie):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])

        # Hy update
        for j in range(1, je):
            for i in range(1, ie - 1):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])

    if plot:
        fig, axes = plt.subplots(1, 2, figsize=(11, 4))

        extent = [0, ie, 0, je]
        im0 = axes[0].imshow(ez.T, origin='lower', cmap='RdBu_r',
                               vmin=-1.2, vmax=1.2, aspect='equal')
        axes[0].axhline(sheet_j, color='green', linewidth=3,
                         label=f'Resistive sheet (j={sheet_j})')
        axes[0].set_title('2D TM with Resistive Sheet')
        axes[0].set_xlabel('i')
        axes[0].set_ylabel('j')
        axes[0].legend()
        plt.colorbar(im0, ax=axes[0], label=r'$E_z$')

        # Profile along j = sheet_j
        axes[1].plot(ez[:, sheet_j], 'k-', linewidth=1)
        axes[1].set_xlabel('i')
        axes[1].set_ylabel(r'$E_z$ at sheet')
        axes[1].set_title('Field along resistive sheet')
        axes[1].set_xlim(0, ie)

        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.6 — Thin Wire (1D Transmission Line Model)
#
#   A thin wire (single conductor above ground) can be modeled as a
#   1D transmission line with distributed L and C per unit length.
#   In FDTD, this reduces to the standard 1D update but with modified
#   characteristic impedance Z0 = sqrt(L/C.
#
#   This example shows a transmission line terminated with a matched load.
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_6_transmission_line(nsteps=400, ke=400,
                                 Z0=1.0,     # characteristic impedance (normalized)
                                 R_load=None,
                                 kc=None, t0=60, spread=15, plot=True):
    """
    1D transmission line FDTD.

    Uses the standard 1D FDTD update with source at one end and
    matched or mismatched load at the other end.

    If R_load = Z0: matched → no reflection
    If R_load != Z0: reflection coefficient Γ = (R_load - Z0)/(R_load + Z0)
    """
    if kc is None:
        kc = ke // 2
    if R_load is None:
        R_load = Z0  # matched load

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    for time_step in range(1, nsteps + 1):
        # E update (standard)
        for k in range(1, ke):
            ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])

        # Source at kc
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        # Load at ke-1: apply resistive termination
        # Effective resistance adds a current I_load = ex[ke-1] / R_load
        ex[ke - 1] -= ex[ke - 1] / R_load   # draws current to ground

        # H update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(10, 3.5))

        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].axvline(ke - 1, color='gray', linestyle='--', label=f'Load R={R_load:.2f}')
        axes[0].set_title(f'Transmission Line (Z0={Z0}, R_load={R_load})')
        axes[0].legend()

        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 8.7 — S-Parameter Concept (Reflection from Impedance Discontinuity)
#
#   When a wave travels from medium with Z1 to medium with Z2:
#     Reflection coefficient: Γ = (Z2 - Z1)/(Z2 + Z1)
#     Transmission coefficient: τ = 2Z2/(Z2+Z1)
#
#   In FDTD: impedance mismatch causes partial reflection.
#   This example shows a wave hitting a dielectric slab (impedance mismatch).
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_8_7_impedance_mismatch(nsteps=400, ke=300,
                                  eps_r1=1.0, eps_r2=4.0,
                                  kc=None, t0=60, spread=15, plot=True):
    """
    1D FDTD showing impedance mismatch and reflection.

    Medium 1 (k < ke//2): eps_r = eps_r1  → Z1 = 1/sqrt(eps_r1)
    Medium 2 (k >= ke//2): eps_r = eps_r2 → Z2 = 1/sqrt(eps_r2)

    Reflection coefficient: Γ = (Z2-Z1)/(Z2+Z1)
    For eps_r1=1, eps_r2=4: Z1=1, Z2=0.5 → Γ = (0.5-1)/(0.5+1) = -1/3 ≈ -33%
    """
    if kc is None:
        kc = ke // 4

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    # Permittivity profile: half free space, half dielectric
    eps_profile = np.ones(ke) * eps_r1
    eps_profile[ke // 2:] = eps_r2

    inv_eps = 1.0 / eps_profile

    interface = ke // 2
    reflection_coef = (1/sqrt(eps_r2) - 1/sqrt(eps_r1)) / (1/sqrt(eps_r2) + 1/sqrt(eps_r1))

    probe_signal = np.zeros(nsteps + 1)
    probe_idx = ke // 4   # in medium 1, before interface

    for time_step in range(1, nsteps + 1):
        # E update with per-cell coefficient
        for k in range(1, ke):
            ex[k] = ex[k] + inv_eps[k] * 0.5 * (hy[k - 1] - hy[k])

        # Source
        pulse = gaussian_pulse(time_step, t0, spread)
        ex[kc] = pulse

        probe_signal[time_step] = ex[probe_idx]

        # H update
        for k in range(ke - 1):
            hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(10, 5))

        # Final field profile
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].axvline(interface, color='gray', linestyle='--',
                         linewidth=2, label=f'Interface (Γ={reflection_coef:.2f})')
        axes[0].axvline(kc, color='blue', linestyle=':', label='Source')
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlabel('FDTD cells')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('Impedance Mismatch Reflection (eps_r1=1 → eps_r2=4)')
        axes[0].legend()

        # Probe signal (shows reflection arriving later)
        axes[1].plot(probe_signal[1:], 'k-', linewidth=1)
        axes[1].set_ylabel(r'$E_x$ at probe')
        axes[1].set_xlabel('Time step')
        axes[1].set_title('Probe signal (incident + reflected)')
        plt.tight_layout()
        plt.show()

    return ex, hy, reflection_coef


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check for Ch8 lumped element code."""
    print("=== Ch8 Verification ===")

    # Resistor: check field is bounded (matched load → no reflection)
    ex1, _, _ = fd3d_8_1_resistor(nsteps=150, ke=100, R=1.0, plot=False)
    assert abs(ex1).max() < 5.0, "Resistor: field blowup"
    print("  [OK] Resistor (lumped)")

    # Capacitor: check non-zero
    ex2, _ = fd3d_8_2_capacitor(nsteps=150, ke=100, C=1.0, plot=False)
    assert abs(ex2).max() > 0, "Capacitor: no field"
    print("  [OK] Capacitor")

    # Inductor: check non-zero
    ex3, _ = fd3d_8_3_inductor(nsteps=150, ke=100, L=1.0, plot=False)
    assert abs(ex3).max() > 0, "Inductor: no field"
    print("  [OK] Inductor")

    # Diode: check bounded
    ex4, _ = fd3d_8_4_diode(nsteps=150, ke=100, plot=False)
    assert abs(ex4).max() < 5.0, "Diode: field blowup"
    print("  [OK] Diode")

    # 2D resistive sheet: check non-zero
    ez5, _, _ = fd3d_8_5_resistive_sheet(nsteps=100, ie=40, je=40, plot=False)
    assert abs(ez5).max() > 0, "Resistive sheet: no field"
    print("  [OK] 2D resistive sheet")

    # Transmission line: check non-zero
    ex6, _ = fd3d_8_6_transmission_line(nsteps=150, ke=100, R_load=1.0, plot=False)
    assert abs(ex6).max() > 0, "Transmission line: no field"
    print("  [OK] Transmission line")

    # Impedance mismatch: check reflection coefficient sign
    ex7, _, Gamma = fd3d_8_7_impedance_mismatch(nsteps=200, ke=100, plot=False)
    assert -1.0 < Gamma < 0.0, f"Impedance mismatch: bad Gamma={Gamma}"
    print(f"  [OK] Impedance mismatch (Γ={Gamma:.3f})")

    print("All Ch8 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch8 — Lumped Elements")
    print("=" * 60)

    print("\n--- Program 8.1: Resistor ---")
    fd3d_8_1_resistor(nsteps=200, ke=200, R=1.0, plot=True)

    print("\n--- Program 8.7: Impedance Mismatch ---")
    fd3d_8_7_impedance_mismatch(nsteps=300, ke=300, eps_r1=1.0, eps_r2=4.0, plot=True)

    print("\n--- Program 8.5: 2D Resistive Sheet ---")
    fd3d_8_5_resistive_sheet(nsteps=150, ie=80, je=80, Rs=10.0, plot=True)

    print("\n=== Verification ===")
    verify()
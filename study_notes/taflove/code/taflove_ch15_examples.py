#!/usr/bin/env python3
"""
taflove_ch15_examples.py — High-Speed Circuits with Active/Nonlinear Components

Reference: Taflove, "Computational Electrodynamics", 3rd Ed., Ch15
Topics:
  Ex15.1: Diode detector — nonlinear I-V rectification
  Ex15.2: SPICE-like RLC lumped element FDTD embedding
  Ex15.3: Microstrip transmission line S-parameter extraction
"""
import numpy as np
from scipy.constants import c, epsilon_0, mu_0, pi, k, e
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-darkgrid")


def ex15_1_diode_detector():
    """Diode detector: nonlinear I-V response to modulated RF pulse."""
    I_S = 2.2e-8; n = 1.08; V_T = n * k * 300 / e
    R_load = 1000; C_load = 10e-12
    t = np.linspace(0, 50e-9, 5000); dt = t[1] - t[0]
    V_in = 0.5 * np.sin(2 * pi * 2e9 * t) * np.exp(-((t - 15e-9) / (8e-9))**2)
    V_out = np.zeros(len(t))

    for i in range(1, len(t)):
        V_D_i = V_in[i] - V_out[i-1]
        I_D_i = I_S * (np.exp(V_D_i / V_T) - 1) if V_D_i > -5 * V_T else -I_S
        V_out[i] = V_out[i-1] + dt * (I_D_i - V_out[i-1] / R_load) / C_load
        V_out[i] = max(V_out[i], 0)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
    ax1.plot(t * 1e9, V_in, 'b-', lw=1.5)
    ax1.set_ylabel('V_in (V)'); ax1.set_title('Diode Detector: RF Input')
    ax1.grid(True, alpha=0.3); ax1.set_xlim(0, 50)

    ax2.plot(t * 1e9, V_out, 'r-', lw=2)
    ax2.set_xlabel('Time (ns)'); ax2.set_ylabel('V_out (V)')
    ax2.set_title(f'Detected Envelope (RC={R_load*C_load*1e9:.1f} ns)')
    ax2.grid(True, alpha=0.3); ax2.set_xlim(0, 50)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch15_ex1_diode_detector.png", dpi=150)
    plt.close()
    print("[Ch15 Ex1] Diode detector plotted.")


def ex15_2_rlc_circuit():
    """Series RLC lumped circuit in FDTD cell."""
    R = 50.0; L = 10e-9; C = 1e-12
    f_res = 1 / (2 * pi * np.sqrt(L * C))
    dz = 0.001; dt = dz / (2 * c); Nz = 300; Nt = 5000
    Ez = np.zeros(Nz); Hy = np.zeros(Nz)
    rlc_z = 150; V_cap = 0.0; I_L = 0.0
    V_gap_hist = []; I_L_hist = []

    for n in range(Nt):
        for iz in range(Nz - 1):
            Hy[iz] = Hy[iz] + (dt / (mu_0 * dz)) * (Ez[iz + 1] - Ez[iz])
        pulse = np.exp(-((n - 200) / 50)**2)
        for iz in range(1, Nz):
            curl_H = (Hy[iz] - Hy[iz-1]) / dz
            if iz == rlc_z:
                V_gap = Ez[iz] * dz
                I_L = I_L + (dt / L) * V_gap
                V_cap = V_cap + (dt / C) * I_L
                Ez[iz] = Ez[iz] + (dt / epsilon_0) * (curl_H - I_L / dz**2)
            else:
                Ez[iz] = Ez[iz] + (dt / epsilon_0) * curl_H
        Ez[20] = pulse * 0.1
        if n % 5 == 0:
            V_gap_hist.append(Ez[rlc_z] * dz)
            I_L_hist.append(I_L)

    time = np.arange(len(V_gap_hist)) * 5 * dt * 1e9
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6))
    ax1.plot(time, V_gap_hist, 'b-', lw=1.5)
    ax1.set_ylabel('V_gap (V)'); ax1.set_title(f'RLC (f0={f_res/1e9:.2f} GHz)')
    ax1.grid(True, alpha=0.3)
    ax2.plot(time, np.array(I_L_hist) * 1e3, 'r-', lw=1.5)
    ax2.set_xlabel('Time (ns)'); ax2.set_ylabel('I_L (mA)'); ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch15_ex2_rlc_circuit.png", dpi=150)
    plt.close()
    print("[Ch15 Ex2] RLC circuit plotted.")


def ex15_3_microstrip_S_params():
    """Microstrip line: S-parameters with impedance mismatch."""
    freq = np.linspace(0.1, 20, 500) * 1e9
    Z0 = 50.0; Z_load = 75.0; v_p = c / np.sqrt(4.2)
    L_line = 30e-3; Gamma_L = (Z_load - Z0) / (Z_load + Z0)
    beta = 2 * pi * freq / v_p
    S11 = Gamma_L * np.exp(-2j * beta * L_line)
    S21 = np.exp(-1j * beta * L_line)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 7))
    ax1.plot(freq / 1e9, 20 * np.log10(np.abs(S11) + 1e-10), 'b-', lw=2, label='S11')
    ax1.plot(freq / 1e9, 20 * np.log10(np.abs(S21) + 1e-10), 'r-', lw=2, label='S21')
    ax1.set_xlabel('Freq (GHz)'); ax1.set_ylabel('|S| (dB)')
    ax1.set_title(f'Microstrip: Z0={Z0} Ohm, ZL={Z_load} Ohm')
    ax1.legend(); ax1.grid(True, alpha=0.3); ax1.set_ylim(-40, 3)

    ax2.plot(freq / 1e9, np.angle(S11, deg=True), 'b-', lw=2, label='angle S11')
    ax2.plot(freq / 1e9, np.unwrap(np.angle(S21)) * 180 / pi, 'r-', lw=2, label='angle S21')
    ax2.set_xlabel('Freq (GHz)'); ax2.set_ylabel('Phase (deg)')
    ax2.legend(); ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig("/home/ubuntu/.openclaw/workspace/textbooks/taflove/figures/ch15_ex3_microstrip_S_params.png", dpi=150)
    plt.close()
    print("[Ch15 Ex3] Microstrip S-params plotted.")


if __name__ == "__main__":
    ex15_1_diode_detector()
    ex15_2_rlc_circuit()
    ex15_3_microstrip_S_params()
    print("\nAll Ch15 examples complete.")

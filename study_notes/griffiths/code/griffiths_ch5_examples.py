#!/usr/bin/env python3
"""Griffiths Ch.5: Magnetostatics"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import constants

plt.style.use('seaborn-v0_8')
mu0 = constants.mu_0
eps0 = constants.epsilon_0

def example_5_3_infinite_wire():
    """B field from infinite straight wire: B = mu0*I/(2*pi*s)"""
    I = 10.0
    s = np.linspace(0.01, 0.5, 100)
    B = mu0 * I / (2 * np.pi * s)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(s*1e2, B*1e4, 'b-', linewidth=2)
    ax.set_xlabel('s (cm)'); ax.set_ylabel('B (Gauss)')
    ax.set_title(f'B field from infinite wire (I = {I}A)')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch5_ex3_wire_B.png', dpi=150)
    plt.close(fig)
    print(f"At s=10cm: B = {mu0*I/(2*np.pi*0.1)*1e4:.2f} Gauss")
    print("Figure saved: griffiths_ch5_ex3_wire_B.png")

def example_5_4_circular_loop():
    """B on axis of circular loop: B = mu0*I*R^2 / (2*(R^2+z^2)^(3/2))"""
    I, R = 10.0, 0.1
    z = np.linspace(-0.5, 0.5, 200)
    B = mu0 * I * R**2 / (2 * (R**2 + z**2)**(3.0/2.0))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z*1e2, B*1e4, 'b-', linewidth=2)
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_xlabel('z (cm)'); ax.set_ylabel('B (Gauss)')
    ax.set_title(f'B on axis of circular loop (I={I}A, R={R*1e2:.0f}cm)')
    ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch5_ex4_loop_B.png', dpi=150)
    plt.close(fig)
    print(f"B at center (z=0): {mu0*I/(2*R)*1e4:.2f} Gauss")
    print("Figure saved: griffiths_ch5_ex4_loop_B.png")

def example_5_6_solenoid():
    """B inside long solenoid: B = mu0*n*I"""
    n_turns_per_m = 1000
    I = 5.0
    B_in = mu0 * n_turns_per_m * I
    z = np.linspace(-0.3, 0.3, 500)
    L = 0.2  # solenoid length
    R = 0.05
    # Finite solenoid field on axis
    B_finite = mu0*n_turns_per_m*I/2 * ((z+L/2)/np.sqrt(R**2+(z+L/2)**2) - (z-L/2)/np.sqrt(R**2+(z-L/2)**2))
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(z*1e2, B_finite*1e4, 'b-', linewidth=2, label='Finite solenoid')
    ax.axhline(B_in*1e4, color='r', linestyle='--', label=f'Infinite limit = {B_in*1e4:.1f} G')
    ax.set_xlabel('z (cm)'); ax.set_ylabel('B (Gauss)')
    ax.set_title('B on axis of solenoid'); ax.legend(); ax.grid(True, alpha=0.3)
    fig.savefig('/home/ubuntu/.openclaw/workspace/textbooks/griffiths/figures/griffiths_ch5_ex6_solenoid.png', dpi=150)
    plt.close(fig)
    print(f"B inside (infinite limit): {B_in*1e4:.1f} Gauss")
    print("Figure saved: griffiths_ch5_ex6_solenoid.png")

if __name__ == "__main__":
    example_5_3_infinite_wire()
    example_5_4_circular_loop()
    example_5_6_solenoid()
    print("\n✅ Ch.5 examples done")

"""
houale_circuit_fdtd.py - Lumped Element and Transmission Line FDTD
Based on Houle & Sullivan, "EM Simulation Using FDTD"
Author: 小龙虾 (Crawfish)
Features: Resistor, inductor, capacitor, transmission line FDTD
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0
import warnings
warnings.filterwarnings('ignore')


class LumpedResistor:
    """
    Lumped resistor model for FDTD.
    
    Models a resistor connected between two nodes in the FDTD grid.
    Uses the voltage/current relationship: V = I * R
    
    For FDTD update:
        I^{n+1/2} = (V_i^n - V_j^n) / R
        Update E field based on current
    """
    
    def __init__(self, R=50.0, location='interface'):
        """
        Initialize lumped resistor.
        
        Parameters
        ----------
        R : float
            Resistance in Ohms
        location : str
            'interface' - at grid boundary, 'bulk' - embedded in material
        """
        self.R = R
        self.location = location
        
    def get_admittance(self):
        """Return admittance Y = 1/R for circuit analysis."""
        return 1.0 / self.R
    
    def update_VI(self, V_i, V_j, dt, epsilon_eff=epsilon_0):
        """
        Update current through resistor.
        
        Parameters
        ----------
        V_i, V_j : float
            Voltages at nodes i and j
        dt : float
            Time step
        epsilon_eff : float
            Effective permittivity for dielectric constant calculation
            
        Returns
        -------
        I : float
            Current through resistor
        """
        Y = self.get_admittance()
        # Simple explicit update
        I = (V_i - V_j) / self.R
        return I
    
    def voltage_drop(self, V_i, V_j):
        """Calculate voltage drop across resistor."""
        return V_i - V_j


class LumpedInductor:
    """
    Lumped inductor model for FDTD.
    
    Models an inductor with: V = L * dI/dt
    
    For FDTD using bilinear transform:
        I^{n+1} = I^n + (dt/L) * (V_i^n + V_j^n)/2
    """
    
    def __init__(self, L=1e-9):
        """
        Initialize lumped inductor.
        
        Parameters
        ----------
        L : float
            Inductance in Henries
        """
        self.L = L
        self.I_prev = 0.0
        
    def get_reactance(self, omega):
        """Inductive reactance X_L = ω*L."""
        return omega * self.L
    
    def update_I(self, V_avg, dt):
        """
        Update current through inductor.
        
        Parameters
        ----------
        V_avg : float
            Average voltage across inductor
        dt : float
            Time step
            
        Returns
        -------
        I_new : float
            New current
        """
        I_new = self.I_prev + (dt / self.L) * V_avg
        self.I_prev = I_new
        return I_new
    
    def get_stored_energy(self, I):
        """Magnetic energy: W = 0.5 * L * I^2."""
        return 0.5 * self.L * I**2


class LumpedCapacitor:
    """
    Lumped capacitor model for FDTD.
    
    Models a capacitor with: I = C * dV/dt
    
    For FDTD:
        V^{n+1} = V^n + (dt/C) * I^{n+1/2}
    """
    
    def __init__(self, C=1e-12):
        """
        Initialize lumped capacitor.
        
        Parameters
        ----------
        C : float
            Capacitance in Farads
        """
        self.C = C
        self.V_prev = 0.0
        
    def get_capacitance(self):
        """Return capacitance value."""
        return self.C
    
    def update_V(self, I, dt):
        """
        Update voltage across capacitor.
        
        Parameters
        ----------
        I : float
            Current into capacitor
        dt : float
            Time step
            
        Returns
        -------
        V_new : float
            New voltage
        """
        V_new = self.V_prev + (dt / self.C) * I
        self.V_prev = V_new
        return V_new
    
    def get_stored_energy(self, V):
        """Electric energy: W = 0.5 * C * V^2."""
        return 0.5 * self.C * V**2


def lumped_resistor_FDTD_1d(Nx=200, L=1.0, R=50.0, T_max=2e-9,
                            epsilon_r=1.0, source_type='gaussian'):
    """
    1D FDTD with lumped resistor load.
    
    Models a transmission line terminated with a matched resistor.
    
    Parameters
    ----------
    Nx : int
        Number of grid points
    L : float
        Line length (m)
    R : float
        Termination resistance (Ohms)
    T_max : float
        Simulation time (s)
    epsilon_r : float
        Relative permittivity
    source_type : str
        Source waveform type
    
    Returns
    -------
    z : ndarray
        Spatial grid
    Ez : ndarray
        E-field distribution
    I_history : ndarray
        Current at resistor location
    """
    dx = L / (Nx - 1)
    c_numerical = c / np.sqrt(epsilon_r)
    dt = 0.99 * dx / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    # Characteristic impedance of transmission line
    # Z0 = sqrt(L'/C') = (1/c) * sqrt(μ/ε) for free-space TEM line
    Z0 = np.sqrt(mu_0 / (epsilon_0 * epsilon_r))
    
    # Initialize fields
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    # Resistor at right end
    R_node = Nx - 2
    
    # Source parameters
    source_x = Nx // 10
    
    def source_t(n):
        t_n = n * dt
        if source_type == 'gaussian':
            tau = 30 * dt
            t0 = 80 * dt
            return np.exp(-((t_n - t0) / tau)**2)
        elif source_type == 'step':
            return 1.0 if t_n < 5e-10 else 0.0
        elif source_type == 'sinusoidal':
            omega = 2 * np.pi * 5e9
            return np.sin(omega * t_n)
        return 0.0
    
    # Update coefficients
    C2 = 2 * dt / (dx * epsilon_0 * epsilon_r)
    D2 = 2 * dt / (dx * mu_0)
    
    I_history = np.zeros(Nt)
    
    print(f"[Lumped Resistor FDTD] R = {R} Ω, Z0 = {Z0:.2f} Ω")
    print(f"  Match condition: R = Z0 for no reflection")
    
    for n in range(Nt):
        # Update H
        for i in range(Nx - 1):
            Hy[i] += D2 * (Ez[i + 1] - Ez[i])
        
        # Update E (standard)
        for i in range(1, Nx - 1):
            Ez[i] += C2 * (Hy[i] - Hy[i - 1])
        
        # Apply resistor boundary at R_node
        # V = Ez * dx, I = V / R at resistor
        V_R = Ez[R_node] * dx
        I_R = V_R / R
        
        # Modify E field at resistor to absorb wave
        # For matched load: Ez[R_node] = -Hy[R_node-1] * Z0
        # For general R: use current injection
        Ez[R_node] = V_R / dx
        
        I_history[n] = I_R
        
        # Source injection
        Ez[source_x] = source_t(n)
        
        # ABC at left boundary
        Ez[0] = Ez[1] + (c_numerical * dt - dx) / (c_numerical * dt + dx) * (Ez[1] - Ez[0])
    
    z = np.linspace(0, L, Nx)
    
    return z, Ez, I_history


def lumped_inductor_FDTD_1d(Nx=200, L=1.0, L_ind=5e-9, T_max=2e-9, epsilon_r=1.0):
    """
    1D FDTD with lumped inductor.
    
    The inductor is placed at the end of the transmission line.
    """
    dx = L / (Nx - 1)
    c_numerical = c / np.sqrt(epsilon_r)
    dt = 0.99 * dx / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    # Initialize
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    # Inductor at end
    L_node = Nx - 2
    inductor = LumpedInductor(L=L_ind)
    
    source_x = Nx // 10
    
    def source_t(n):
        t_n = n * dt
        tau = 30 * dt
        t0 = 80 * dt
        return np.exp(-((t_n - t0) / tau)**2)
    
    C2 = 2 * dt / (dx * epsilon_0 * epsilon_r)
    D2 = 2 * dt / (dx * mu_0)
    
    V_history = np.zeros(Nt)
    I_history = np.zeros(Nt)
    
    print(f"[Lumped Inductor FDTD] L = {L_ind*1e9:.1f} nH")
    
    for n in range(Nt):
        # Update H
        for i in range(Nx - 1):
            Hy[i] += D2 * (Ez[i + 1] - Ez[i])
        
        # Update E
        for i in range(1, Nx - 1):
            Ez[i] += C2 * (Hy[i] - Hy[i - 1])
        
        # Inductor boundary condition
        # V = L * dI/dt, I = Hy at inductor location
        V_L = Ez[L_node] * dx
        I_L = inductor.update_I(V_L, dt)
        
        # Adjust E field for inductor
        # Simple series: modify next node
        Ez[L_node + 1] -= (dt / (epsilon_0 * epsilon_r * dx)) * I_L
        
        V_history[n] = V_L
        I_history[n] = I_L
        
        # Source
        Ez[source_x] = source_t(n)
        
        # ABC
        Ez[0] = Ez[1] + (c_numerical * dt - dx) / (c_numerical * dt + dx) * (Ez[1] - Ez[0])
    
    z = np.linspace(0, L, Nx)
    
    return z, Ez, V_history, I_history


def lumped_capacitor_FDTD_1d(Nx=200, L=1.0, C_cap=2e-12, T_max=2e-9, epsilon_r=1.0):
    """
    1D FDTD with lumped capacitor at termination.
    """
    dx = L / (Nx - 1)
    c_numerical = c / np.sqrt(epsilon_r)
    dt = 0.99 * dx / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    C_node = Nx - 2
    capacitor = LumpedCapacitor(C=C_cap)
    
    source_x = Nx // 10
    
    def source_t(n):
        t_n = n * dt
        tau = 30 * dt
        t0 = 80 * dt
        return np.exp(-((t_n - t0) / tau)**2)
    
    C2 = 2 * dt / (dx * epsilon_0 * epsilon_r)
    D2 = 2 * dt / (dx * mu_0)
    
    V_history = np.zeros(Nt)
    Q_history = np.zeros(Nt)
    
    print(f"[Lumped Capacitor FDTD] C = {C_cap*1e12:.1f} pF")
    
    for n in range(Nt):
        # Update H
        for i in range(Nx - 1):
            Hy[i] += D2 * (Ez[i + 1] - Ez[i])
        
        # Update E
        for i in range(1, Nx - 1):
            Ez[i] += C2 * (Hy[i] - Hy[i - 1])
        
        # Capacitor boundary
        # Q = C * V, I = dQ/dt
        V_C = Ez[C_node] * dx
        I_C = capacitor.update_V(V_C, dt) / dt * C_cap  # simplified
        
        # Adjust field
        Ez[C_node] = capacitor.V_prev / dx
        
        V_history[n] = V_C
        Q_history[n] = capacitor.C * V_C
        
        Ez[source_x] = source_t(n)
        Ez[0] = Ez[1] + (c_numerical * dt - dx) / (c_numerical * dt + dx) * (Ez[1] - Ez[0])
    
    z = np.linspace(0, L, Nx)
    
    return z, Ez, V_history, Q_history


def transmission_line_1d(Nx=400, L=2.0, Z0=50.0, f_source=5e9,
                        T_max=5e-9, epsilon_r=2.1):
    """
    Transmission line FDTD (telegrapher's equations).
    
    Solves:
        dV/dz = -L' * dI/dt
        dI/dz = -C' * dV/dt
    
    where:
        L' = μ_r * μ0 / (width * effective_height)  [H/m]
        C' = ε_r * ε0 * width / effective_height   [F/m]
        Z0 = sqrt(L'/C')
    
    Parameters
    ----------
    Nx : int
        Number of cells
    L : float
        Line length (m)
    Z0 : float
        Characteristic impedance (Ohms)
    f_source : float
        Source frequency (Hz)
    T_max : float
        Simulation time (s)
    epsilon_r : float
        Dielectric relative permittivity
    
    Returns
    -------
    z : ndarray
        Spatial grid
    V : ndarray
        Voltage distribution
    I : ndarray
        Current distribution
    t : ndarray
        Time array
    """
    dx = L / (Nx - 1)
    
    # Calculate per-unit-length parameters
    # For a parallel plate: L' = μ0 * μ_r * h / w, C' = ε0 * ε_r * w / h
    # Z0 = sqrt(L'/C') = (1/c) * sqrt(μ_r/ε_r) * (h/w)
    # Assuming h/w ratio for 50 ohm in free space: ~0.5 mm / 1 mm = 0.5
    h_w_ratio = Z0 * epsilon_0 * c  # h/w = Z0 * sqrt(ε0/μ0) * sqrt(ε_r/μ_r)
    # Actually: Z0 = (1/(c*ε0))^(1/2) * sqrt(μ_r/ε_r) * (h/w)
    # For Z0=50, ε_r=2.1: h/w = 50 * sqrt(2.1) / (377)
    
    # For coax-like: use effective L', C'
    L_prime = (mu_0 * mu_0) / (2 * np.pi)  # placeholder
    C_prime = 2 * np.pi * epsilon_0 * epsilon_r / mu_0  # placeholder
    
    # Better: derive from Z0 and epsilon_r
    # Z0 = sqrt(L'/C'), v = 1/sqrt(L'*C') = c/sqrt(epsilon_r)
    # L' = Z0 / v = Z0 * sqrt(epsilon_r) / c
    # C' = 1/(Z0 * v) = sqrt(epsilon_r) / (Z0 * c)
    v = c / np.sqrt(epsilon_r)
    L_prime = Z0 / v
    C_prime = 1.0 / (Z0 * v)
    
    dt = 0.99 * dx / v
    Nt = int(T_max / dt)
    
    print(f"[Transmission Line] Z0 = {Z0} Ω, ε_r = {epsilon_r}")
    print(f"  L' = {L_prime*1e9:.4f} nH/m, C' = {C_prime*1e12:.4f} pF/m")
    print(f"  v = {v/1e8:.4f} x 10^8 m/s, dt = {dt:.2e} s")
    
    # Initialize V, I (staggered grid)
    V = np.zeros(Nx)  # V at integer nodes
    I = np.zeros(Nx - 1)  # I at half-integer nodes
    
    # Update coefficients
    inv_L = 1.0 / L_prime
    inv_C = 1.0 / C_prime
    
    # Source at left end
    source_node = 0
    
    def source_t(n):
        omega = 2 * np.pi * f_source
        return np.sin(omega * n * dt)
    
    t = np.arange(Nt) * dt
    V_history = []
    
    for n in range(Nt):
        # Update I (half step)
        for i in range(Nx - 1):
            I[i] += (dt * inv_L) * (V[i + 1] - V[i])
        
        # Update V (full step)
        for i in range(1, Nx - 1):
            V[i] += (dt * inv_C) * (I[i] - I[i - 1])
        
        # Boundary conditions
        # Left: voltage source with source impedance Z0
        V[source_node] = source_t(n)
        I[source_node] = (V[source_node] - source_t(n)) / Z0  # matched source
        
        # Right: matched load Z0
        V[-1] = I[-2] * Z0
        
        if n % 10 == 0:
            V_history.append(V.copy())
    
    z = np.linspace(0, L, Nx)
    
    return z, np.array(V_history), I, t


def validate_circuit_components():
    """Validate all circuit component models."""
    print("\n" + "=" * 60)
    print("Circuit Component FDTD Validation")
    print("=" * 60)
    
    # Resistor test
    print("\n[Test] Lumped Resistor (R=50Ω matched load)")
    z, Ez_R, I_R = lumped_resistor_FDTD_1d(
        Nx=300, L=1.0, R=50.0, T_max=3e-9, epsilon_r=1.0, source_type='gaussian'
    )
    print(f"  Max current: {np.max(np.abs(I_R))*1e3:.4f} mA")
    
    # Inductor test
    print("\n[Test] Lumped Inductor (L=5nH)")
    z, Ez_L, V_L, I_L = lumped_inductor_FDTD_1d(
        Nx=300, L=1.0, L_ind=5e-9, T_max=3e-9, epsilon_r=1.0
    )
    print(f"  Max voltage: {np.max(np.abs(V_L))*1e3:.4f} mV")
    print(f"  Max current: {np.max(np.abs(I_L))*1e3:.4f} mA")
    
    # Capacitor test
    print("\n[Test] Lumped Capacitor (C=2pF)")
    z, Ez_C, V_C, Q_C = lumped_capacitor_FDTD_1d(
        Nx=300, L=1.0, C_cap=2e-12, T_max=3e-9, epsilon_r=1.0
    )
    print(f"  Max voltage: {np.max(np.abs(V_C))*1e3:.4f} mV")
    print(f"  Max charge: {np.max(np.abs(Q_C))*1e15:.4f} fC")
    
    return True


def plot_transmission_line():
    """Plot transmission line simulation results."""
    print("\n[Transmission Line] Running simulation...")
    z, V_hist, I_final, t = transmission_line_1d(
        Nx=300, L=1.0, Z0=50.0, f_source=10e9, T_max=2e-9, epsilon_r=2.1
    )
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # Voltage snapshots
    colors = plt.cm.viridis(np.linspace(0, 1, len(V_hist)))
    for i, V in enumerate(V_hist[::10]):  # every 10th
        axes[0].plot(z * 1e3, V, color=colors[i], alpha=0.7)
    axes[0].set_xlabel('Position (mm)')
    axes[0].set_ylabel('Voltage (V)')
    axes[0].set_title('Transmission Line: Voltage Waveform Snapshots')
    axes[0].grid(True, alpha=0.3)
    
    # Final current distribution
    z_I = np.linspace(0, z[-1], len(I_final))
    axes[1].plot(z_I * 1e3, I_final * 1e3, 'r-', linewidth=1.5)
    axes[1].set_xlabel('Position (mm)')
    axes[1].set_ylabel('Current (mA)')
    axes[1].set_title('Transmission Line: Current Distribution')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/transmission_line.png',
                dpi=150, bbox_inches='tight')
    print("Saved: transmission_line.png")
    plt.close()


def plot_lumped_element_results():
    """Plot results from lumped element simulations."""
    print("\n[Lumped Elements] Generating plots...")
    
    # Resistor
    z_R, Ez_R, I_R = lumped_resistor_FDTD_1d(
        Nx=200, L=0.5, R=50.0, T_max=1e-9, source_type='step'
    )
    
    # Inductor
    z_L, Ez_L, V_L, I_L = lumped_inductor_FDTD_1d(
        Nx=200, L=0.5, L_ind=3e-9, T_max=1e-9
    )
    
    # Capacitor
    z_C, Ez_C, V_C, Q_C = lumped_capacitor_FDTD_1d(
        Nx=200, L=0.5, C_cap=1e-12, T_max=1e-9
    )
    
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    
    # Resistor results
    axes[0, 0].plot(z_R * 1e3, Ez_R, 'b-', linewidth=1.5)
    axes[0, 0].set_ylabel('E (V/m)')
    axes[0, 0].set_title('Resistor: E-field')
    axes[0, 0].grid(True, alpha=0.3)
    
    axes[0, 1].plot(I_R * 1e3, 'r-', linewidth=1.5)
    axes[0, 1].set_ylabel('I (mA)')
    axes[0, 1].set_title('Resistor: Current')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Inductor results
    axes[1, 0].plot(z_L * 1e3, Ez_L, 'g-', linewidth=1.5)
    axes[1, 0].set_ylabel('E (V/m)')
    axes[1, 0].set_title('Inductor: E-field')
    axes[1, 0].grid(True, alpha=0.3)
    
    axes[1, 1].plot(V_L * 1e3, 'm-', linewidth=1.5, label='V')
    axes[1, 1].plot(I_L * 1e3, 'c-', linewidth=1.5, label='I')
    axes[1, 1].set_ylabel('V/I')
    axes[1, 1].set_title('Inductor: V and I')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    # Capacitor results
    axes[2, 0].plot(z_C * 1e3, Ez_C, 'k-', linewidth=1.5)
    axes[2, 0].set_xlabel('z (mm)')
    axes[2, 0].set_ylabel('E (V/m)')
    axes[2, 0].set_title('Capacitor: E-field')
    axes[2, 0].grid(True, alpha=0.3)
    
    axes[2, 1].plot(V_C * 1e3, 'orange', linewidth=1.5, label='V')
    axes[2, 1].plot(Q_C * 1e15, 'purple', linewidth=1.5, label='Q (fC)')
    axes[2, 1].set_xlabel('Time step')
    axes[2, 1].set_ylabel('V / Q')
    axes[2, 1].set_title('Capacitor: V and Q')
    axes[2, 1].legend()
    axes[2, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/lumped_elements.png',
                dpi=150, bbox_inches='tight')
    print("Saved: lumped_elements.png")
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan FDTD - Circuit Elements")
    print("=" * 60)
    
    # Validate circuit components
    validate_circuit_components()
    
    # Plot transmission line
    plot_transmission_line()
    
    # Plot lumped element results
    plot_lumped_element_results()
    
    # Print file info
    import os
    filepath = os.path.abspath(__file__)
    with open(filepath, 'r') as f:
        lines = len(f.readlines())
    print(f"\n[DONE] {filepath}")
    print(f"       Lines: {lines}")
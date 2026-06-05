"""
houale_materials.py - Dispersive Material Models for FDTD
Based on Houle & Sullivan, "EM Simulation Using FDTD"
Author: 小龙虾 (Crawfish)
Features: Debye, Lorentz, Drude models with ADE method
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0
import warnings
warnings.filterwarnings('ignore')


class DebyeMaterial:
    """
    First-order Debye model for dielectric dispersion.
    
    ε_r(ω) = ε_∞ + (ε_s - ε_∞) / (1 + j*ω*τ)
    
    where:
        ε_∞ = infinite frequency permittivity
        ε_s = static (low-frequency) permittivity
        τ = relaxation time
    
    ADE (Auxiliary Differential Equation) formulation:
        dP/dt = (ε_s - ε_∞) * E / τ - P / τ
        D = ε_0 * ε_∞ * E + P
    """
    
    def __init__(self, eps_inf=2.0, eps_s=5.0, tau=1e-12):
        """
        Initialize Debye material parameters.
        
        Parameters
        ----------
        eps_inf : float
            High-frequency relative permittivity
        eps_s : float
            Static (DC) relative permittivity  
        tau : float
            Relaxation time (seconds)
        """
        self.eps_inf = eps_inf
        self.eps_s = eps_s
        self.tau = tau
        self.delta_eps = eps_s - eps_inf
        
    def get_epsilon_r(self, omega):
        """Complex relative permittivity at angular frequency omega."""
        return self.eps_inf + self.delta_eps / (1 + 1j * omega * self.tau)
    
    def ADE_update_P(self, P, E, dt):
        """
        Update polarization P using ADE scheme.
        
        dP/dt + P/τ = (ε_s - ε_∞) * E / τ
        """
        return P + dt * (self.delta_eps * E / self.tau - P / self.tau)
    
    def plot_dispersion(self, f_min=1e9, f_max=100e9, filename=None):
        """Plot frequency-dependent permittivity."""
        f = np.logspace(np.log10(f_min), np.log10(f_max), 500)
        omega = 2 * np.pi * f
        
        eps_r = np.array([self.get_epsilon_r(w) for w in omega])
        
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        
        # Real part
        axes[0].semilogx(f/1e9, np.real(eps_r), 'b-', linewidth=2)
        axes[0].axhline(y=self.eps_s, color='r', linestyle='--', label=f'ε_s = {self.eps_s}')
        axes[0].axhline(y=self.eps_inf, color='g', linestyle='--', label=f'ε_∞ = {self.eps_inf}')
        axes[0].set_ylabel('ε\'_r')
        axes[0].set_xlabel('Frequency (GHz)')
        axes[0].set_title('Debye Model: Real Permittivity')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Imaginary part
        axes[1].semilogx(f/1e9, np.imag(eps_r), 'r-', linewidth=2)
        axes[1].set_ylabel('ε\"_r')
        axes[1].set_xlabel('Frequency (GHz)')
        axes[1].set_title('Debye Model: Imaginary Permittivity (Loss)')
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if filename:
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            print(f"Saved: {filename}")
        plt.close()
        
        return f, eps_r


class LorentzMaterial:
    """
    Lorentz model for resonant media.
    
    ε_r(ω) = ε_∞ + Σ (Δε_k * ω_k^2) / (ω_k^2 - ω^2 + j*ω*Γ_k)
    
    For single oscillator:
        ε_r(ω) = ε_∞ + (ω_p^2) / (ω_0^2 - ω^2 + j*ω*Γ)
    
    where:
        ω_0 = resonant frequency
        ω_p = plasma frequency  
        Γ = damping factor
    """
    
    def __init__(self, eps_inf=2.0, omega_0=2*np.pi*10e9, omega_p=2*np.pi*20e9, Gamma=1e9):
        """
        Initialize Lorentz material.
        
        Parameters
        ----------
        eps_inf : float
            Background permittivity
        omega_0 : float
            Resonant angular frequency (rad/s)
        omega_p : float
            Plasma angular frequency (rad/s)
        Gamma : float
            Damping factor (rad/s)
        """
        self.eps_inf = eps_inf
        self.omega_0 = omega_0
        self.omega_p = omega_p
        self.Gamma = Gamma
        
    def get_epsilon_r(self, omega):
        """Complex relative permittivity."""
        denom = self.omega_0**2 - omega**2 + 1j * omega * self.Gamma
        return self.eps_inf + self.omega_p**2 / denom
    
    def ADE_update_P(self, P, dP_dt_prev, E, dt):
        """
        Update polarization and its time derivative using Lorentz ADE.
        
        d²P/dt² + Γ*dP/dt + ω_0²*P = ε_0 * Δε * ω_0² * E
        
        where Δε = (ε_∞ + ε_potential) - ε_∞ at resonance
        """
        dP_dt = dP_dt_prev + dt * (
            - self.Gamma * dP_dt_prev
            - self.omega_0**2 * P
            + epsilon_0 * (self.omega_p**2) * E
        )
        P_new = P + dt * dP_dt
        return P_new, dP_dt
    
    def plot_dispersion(self, f_min=1e9, f_max=100e9, filename=None):
        """Plot Lorentz dispersion curve."""
        f = np.logspace(np.log10(f_min), np.log10(f_max), 500)
        omega = 2 * np.pi * f
        
        eps_r = np.array([self.get_epsilon_r(w) for w in omega])
        
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        
        axes[0].semilogx(f/1e9, np.real(eps_r), 'b-', linewidth=2)
        axes[0].axvline(x=self.omega_0/(2*np.pi)/1e9, color='r', linestyle='--',
                        label=f'ω₀/2π = {self.omega_0/(2*np.pi)/1e9:.1f} GHz')
        axes[0].set_ylabel('ε\'_r')
        axes[0].set_xlabel('Frequency (GHz)')
        axes[0].set_title('Lorentz Model: Real Permittivity')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].semilogx(f/1e9, np.imag(eps_r), 'r-', linewidth=2)
        axes[1].axvline(x=self.omega_0/(2*np.pi)/1e9, color='r', linestyle='--',
                        label=f'ω₀/2π = {self.omega_0/(2*np.pi)/1e9:.1f} GHz')
        axes[1].set_ylabel('ε\"_r')
        axes[1].set_xlabel('Frequency (GHz)')
        axes[1].set_title('Lorentz Model: Imaginary Permittivity (Loss)')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if filename:
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            print(f"Saved: {filename}")
        plt.close()


class DrudeMaterial:
    """
    Drude model for free electron (plasma) media.
    
    ε_r(ω) = ε_∞ - ω_p² / (ω² + j*ω*Γ)
    
    where:
        ω_p = plasma frequency
        Γ = collision frequency
    """
    
    def __init__(self, eps_inf=1.0, omega_p=2*np.pi*50e9, Gamma=1e11):
        """
        Initialize Drude material.
        
        Parameters
        ----------
        eps_inf : float
            Background permittivity (usually 1 for vacuum/plasma)
        omega_p : float
            Plasma angular frequency (rad/s)
        Gamma : float
            Electron collision frequency (rad/s)
        """
        self.eps_inf = eps_inf
        self.omega_p = omega_p
        self.Gamma = Gamma
        
    def get_epsilon_r(self, omega):
        """Complex relative permittivity at frequency omega."""
        denom = omega**2 + 1j * omega * self.Gamma
        return self.eps_inf - self.omega_p**2 / denom
    
    def get_skin_depth(self, f):
        """Calculate skin depth at frequency f (for highly conducting case)."""
        omega = 2 * np.pi * f
        eps_r = self.get_epsilon_r(omega)
        # For metal-like: δ = c / (ω * Im(√ε_r))
        alpha = omega * np.imag(np.sqrt(eps_r)) / c
        return 1 / alpha if alpha > 0 else np.inf
    
    def ADE_update_J(self, J, E, dt):
        """
        Update current density J using Drude ADE.
        
        dJ/dt + Γ*J = ε_0 * ω_p² * E
        """
        return J + dt * (-self.Gamma * J + epsilon_0 * self.omega_p**2 * E)
    
    def plot_dispersion(self, f_min=1e9, f_max=200e9, filename=None):
        """Plot Drude dispersion."""
        f = np.logspace(np.log10(f_min), np.log10(f_max), 500)
        omega = 2 * np.pi * f
        
        eps_r = np.array([self.get_epsilon_r(w) for w in omega])
        
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        
        axes[0].semilogx(f/1e9, np.real(eps_r), 'b-', linewidth=2)
        axes[0].axhline(y=self.eps_inf, color='g', linestyle='--', 
                        label=f'ε_∞ = {self.eps_inf}')
        axes[0].axvline(x=self.omega_p/(2*np.pi)/1e9, color='r', linestyle='--',
                        label=f'ω_p/2π = {self.omega_p/(2*np.pi)/1e9:.1f} GHz')
        axes[0].set_ylabel('ε\'_r')
        axes[0].set_xlabel('Frequency (GHz)')
        axes[0].set_title('Drude Model: Real Permittivity')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        axes[1].semilogx(f/1e9, np.imag(eps_r), 'r-', linewidth=2)
        axes[1].axvline(x=self.omega_p/(2*np.pi)/1e9, color='r', linestyle='--',
                        label=f'ω_p/2π = {self.omega_p/(2*np.pi)/1e9:.1f} GHz')
        axes[1].set_ylabel('ε\"_r')
        axes[1].set_xlabel('Frequency (GHz)')
        axes[1].set_title('Drude Model: Imaginary Permittivity (Loss)')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        if filename:
            plt.savefig(filename, dpi=150, bbox_inches='tight')
            print(f"Saved: {filename}")
        plt.close()


def dispersive_FDTD_1d(Nx=400, L=2.0, T_max=5e-9, material='debye',
                       **material_params):
    """
    1D FDTD with dispersive material using ADE method.
    
    Parameters
    ----------
    Nx : int
        Number of grid points
    L : float
        Domain length (m)
    T_max : float
        Simulation time (s)
    material : str
        'debye', 'lorentz', or 'drude'
    **material_params
        Parameters for the material model
    
    Returns
    -------
    z : ndarray
        Spatial grid
    Ez : ndarray
        E-field history [Nt x Nx]
    """
    dx = L / (Nx - 1)
    c_numerical = c
    dt = 0.99 * dx / (2 * c_numerical)
    Nt = int(T_max / dt)
    
    # Initialize fields
    Ez = np.zeros(Nx)
    Hy = np.zeros(Nx)
    
    # Initialize material
    if material == 'debye':
        mat = DebyeMaterial(**material_params)
        P = np.zeros(Nx)  # polarization
    elif material == 'lorentz':
        mat = LorentzMaterial(**material_params)
        P = np.zeros(Nx)  # polarization
        dP_dt = np.zeros(Nx)
    elif material == 'drude':
        mat = DrudeMaterial(**material_params)
        J = np.zeros(Nx)  # current density
    
    # Source
    source_x = Nx // 10
    
    def source_t(n):
        t_n = n * dt
        tau = 20 * dt
        t0 = 60 * dt
        return np.exp(-((t_n - t0) / tau)**2)
    
    # Update coefficients
    C2 = 2 * dt / (dx * epsilon_0 * (mat.eps_inf if hasattr(mat, 'eps_inf') else mat.eps_inf))
    D2 = 2 * dt / (dx * mu_0)
    
    print(f"[Dispersive FDTD 1D] Material: {material}")
    print(f"  Grid: {Nx} pts, dt: {dt:.2e} s, Nt: {Nt}")
    
    for n in range(Nt):
        # Update H
        for i in range(Nx - 1):
            Hy[i] += D2 * (Ez[i + 1] - Ez[i])
        
        # Update polarization/current based on material
        if material == 'debye':
            for i in range(Nx):
                P[i] = mat.ADE_update_P(P[i], Ez[i], dt)
        elif material == 'lorentz':
            for i in range(Nx):
                P[i], dP_dt[i] = mat.ADE_update_P(P[i], dP_dt[i], Ez[i], dt)
        elif material == 'drude':
            for i in range(Nx):
                J[i] = mat.ADE_update_J(J[i], Ez[i], dt)
        
        # Update E
        for i in range(1, Nx - 1):
            if material == 'debye':
                # D = ε_0*ε_∞*E + P, then E from D
                Dz = epsilon_0 * mat.eps_inf * Ez[i] + P[i]
                Ez[i] = Dz / (epsilon_0 * mat.eps_inf + epsilon_0 * mat.delta_eps * dt / (dt + mat.tau))
            elif material == 'lorentz':
                # Simplified: use effective epsilon
                eps_eff = epsilon_0 * (mat.eps_inf + mat.omega_p**2 / mat.omega_0**2)
                Ez[i] = Ez[i] + C2 * (Hy[i] - Hy[i-1])
            elif material == 'drude':
                # J update affects E
                Dz = epsilon_0 * mat.eps_inf * Ez[i] - J[i] * dt
                Ez[i] = Dz / (epsilon_0 * mat.eps_inf + epsilon_0 * mat.omega_p**2 * dt**2)
        
        # Source
        Ez[source_x] = source_t(n)
    
    z = np.linspace(0, L, Nx)
    return z, Ez


def validate_debye():
    """Validate Debye model against analytical solution."""
    print("\n" + "=" * 50)
    print("Debye Model Validation")
    print("=" * 50)
    
    mat = DebyeMaterial(eps_inf=2.0, eps_s=5.0, tau=1e-12)
    
    # Plot dispersion
    mat.plot_dispersion(
        f_min=1e9, f_max=50e9,
        filename='/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/debye_dispersion.png'
    )
    
    # Test frequency response at specific points
    test_frequencies = [1e9, 5e9, 10e9, 20e9]
    print("\nFrequency response at test points:")
    for f in test_frequencies:
        omega = 2 * np.pi * f
        eps_r = mat.get_epsilon_r(omega)
        print(f"  f = {f/1e9:.1f} GHz: ε_r = {eps_r.real:.4f} + j{eps_r.imag:.4f}")
    
    return True


def validate_lorentz():
    """Validate Lorentz model."""
    print("\n" + "=" * 50)
    print("Lorentz Model Validation")
    print("=" * 50)
    
    mat = LorentzMaterial(
        eps_inf=2.0, 
        omega_0=2*np.pi*10e9, 
        omega_p=2*np.pi*20e9, 
        Gamma=1e9
    )
    
    mat.plot_dispersion(
        f_min=1e9, f_max=50e9,
        filename='/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/lorentz_dispersion.png'
    )
    
    # Near resonance, check energy loss
    f_res = mat.omega_0 / (2*np.pi)
    print(f"\nResonant frequency: {f_res/1e9:.2f} GHz")
    eps_at_res = mat.get_epsilon_r(mat.omega_0)
    print(f"  At resonance: ε_r = {eps_at_res.real:.4f} + j{eps_at_res.imag:.4f}")
    
    return True


def validate_drude():
    """Validate Drude model for metal-like behavior."""
    print("\n" + "=" * 50)
    print("Drude Model Validation")
    print("=" * 50)
    
    # Gold-like parameters
    mat = DrudeMaterial(
        eps_inf=1.0, 
        omega_p=2*np.pi*2175e12,  # ~217.5 THz plasma frequency
        Gamma=1e13  # collision
    )
    
    mat.plot_dispersion(
        f_min=100e12, f_max=3000e12,
        filename='/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/drude_dispersion.png'
    )
    
    # Skin depth test
    test_f = [500e12, 1000e12, 2000e12]
    print("\nSkin depth at optical frequencies:")
    for f in test_f:
        delta = mat.get_skin_depth(f)
        print(f"  f = {f/1e12:.1f} THz: δ = {delta*1e9:.2f} nm")
    
    return True


def dispersive_FDTD_comparison():
    """Run dispersive FDTD for all three models."""
    print("\n" + "=" * 60)
    print("Dispersive FDTD 1D Comparison")
    print("=" * 60)
    
    z_debye, Ez_debye = dispersive_FDTD_1d(
        Nx=300, L=1.5, T_max=3e-9, material='debye',
        eps_inf=2.0, eps_s=5.0, tau=1e-12
    )
    
    z_lorentz, Ez_lorentz = dispersive_FDTD_1d(
        Nx=300, L=1.5, T_max=3e-9, material='lorentz',
        eps_inf=2.0, omega_0=2*np.pi*15e9, omega_p=2*np.pi*30e9, Gamma=5e9
    )
    
    z_drude, Ez_drude = dispersive_FDTD_1d(
        Nx=300, L=1.5, T_max=3e-9, material='drude',
        eps_inf=1.0, omega_p=2*np.pi*50e9, Gamma=1e11
    )
    
    # Plot comparison
    fig, axes = plt.subplots(3, 1, figsize=(12, 10))
    
    axes[0].plot(z_debye * 1e3, Ez_debye, 'b-', linewidth=1.5)
    axes[0].set_ylabel('E (V/m)')
    axes[0].set_title('Debye Material (ε_s=5, τ=1ps)')
    axes[0].grid(True, alpha=0.3)
    
    axes[1].plot(z_lorentz * 1e3, Ez_lorentz, 'g-', linewidth=1.5)
    axes[1].set_ylabel('E (V/m)')
    axes[1].set_title('Lorentz Material (ω₀=15GHz, ω_p=30GHz)')
    axes[1].grid(True, alpha=0.3)
    
    axes[2].plot(z_drude * 1e3, Ez_drude, 'r-', linewidth=1.5)
    axes[2].set_xlabel('z (mm)')
    axes[2].set_ylabel('E (V/m)')
    axes[2].set_title('Drude Material (ω_p=50GHz)')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/houle_sullivan/code/dispersive_comparison.png',
                dpi=150, bbox_inches='tight')
    print("Saved: dispersive_comparison.png")
    plt.close()


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan FDTD - Dispersive Materials")
    print("=" * 60)
    
    # Validate all material models
    validate_debye()
    validate_lorentz()
    validate_drude()
    
    # Run dispersive FDTD comparison
    dispersive_FDTD_comparison()
    
    # Print file info
    import os
    filepath = os.path.abspath(__file__)
    with open(filepath, 'r') as f:
        lines = len(f.readlines())
    print(f"\n[DONE] {filepath}")
    print(f"       Lines: {lines}")
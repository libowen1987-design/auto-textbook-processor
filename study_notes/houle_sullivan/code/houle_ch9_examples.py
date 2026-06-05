"""
houle_ch9_examples.py
=====================
Chapter 9 — Advanced Python Features for FDTD

Topics covered:
  9.1  Numba @njit JIT compilation for 10-100x speedup
  9.2  namedtuple for constants and PML parameter encapsulation
  9.3  class-based FDTD grid management
  9.4  Vectorized operations with NumPy broadcasting
  9.5  Memory layout optimization (row-major vs. column-major)
  9.6  Profiling and performance analysis

References:
  - Lam et al. (2015), "Numba: a LLVM-based Python JIT compiler",
    Proc. LLVM Workshop
  - Houle & Sullivan, Ch. 9
"""

import numpy as np
from math import exp, sqrt, cos, sin, pi
from matplotlib import pyplot as plt
from collections import namedtuple
from time import time as timer
plt.rcParams['font.size'] = 12

# ─────────────────────────────────────────────────────────────────────────────
# DATA STRUCTURES
# ─────────────────────────────────────────────────────────────────────────────

# Namedtuple for simulation constants
Constants = namedtuple('Constants', [
    'ddx',       # Δx (grid spacing, meters)
    'dt',        # Δt (time step, seconds)
    'eps0',      # ε₀ (vacuum permittivity)
    'mu0',       # μ₀ (vacuum permeability)
    't0',        # Gaussian pulse center time
    'spread',    # Gaussian pulse spread
    'npml',      # PML layer thickness
])

# Namedtuple for PML parameters (3 directions × 3 parameters each)
PMLCoefficients = namedtuple('PMLCoefficients', [
    'gi1', 'gi2', 'gi3',
    'fi1', 'fi2', 'fi3',
    'gj1', 'gj2', 'gj3',
    'fj1', 'fj2', 'fj3',
    'gk1', 'gk2', 'gk3',
    'fk1', 'fk2', 'fk3',
])

# Grid dimensions
Dimensions = namedtuple('Dimensions', [
    'nx', 'ny', 'nz',
    'nxa', 'nya', 'nza',
])


def make_constants(ddx=0.5, npml=8):
    """Create normalized simulation constants."""
    return Constants(
        ddx=ddx,
        dt=ddx / 2.0,
        eps0=1.0,
        mu0=1.0,
        t0=40,
        spread=12,
        npml=npml,
    )


def calculate_pml_coefficients(nx, ny, nz, npml=8, sigma_max=0.333):
    """Calculate Berenger PML coefficients for 3D FDTD."""
    gi1 = np.zeros(nx); gi2 = np.ones(nx); gi3 = np.ones(nx)
    fi1 = np.zeros(nx); fi2 = np.ones(nx); fi3 = np.ones(nx)
    gj1 = np.zeros(ny); gj2 = np.ones(ny); gj3 = np.ones(ny)
    fj1 = np.zeros(ny); fj2 = np.ones(ny); fj3 = np.ones(ny)
    gk1 = np.zeros(nz); gk2 = np.ones(nz); gk3 = np.ones(nz)
    fk1 = np.zeros(nz); fk2 = np.ones(nz); fk3 = np.ones(nz)

    for i in range(1, npml + 1):
        ratio = (npml - i + 1) / npml
        xn = sigma_max * (1 - ratio) ** 3
        gi2[i] = 1.0 / (1.0 + xn)
        gi3[i] = (1.0 - xn) / (1.0 + xn)
        fi1[i] = xn
        fi2[i] = 1.0 / (1.0 + xn * 0.5)
        fi3[i] = (1.0 - xn * 0.5) / (1.0 + xn * 0.5)
        gi2[nx - 1 - i + 1] = gi2[i]
        gi3[nx - 1 - i + 1] = gi3[i]
        fi1[nx - 1 - i + 1] = fi1[i]

    for j in range(1, npml + 1):
        ratio = (npml - j + 1) / npml
        yn = sigma_max * (1 - ratio) ** 3
        gj2[j] = 1.0 / (1.0 + yn)
        gj3[j] = (1.0 - yn) / (1.0 + yn)
        fj1[j] = yn
        fj2[j] = 1.0 / (1.0 + yn * 0.5)
        fj3[j] = (1.0 - yn * 0.5) / (1.0 + yn * 0.5)
        gj2[ny - 1 - j + 1] = gj2[j]
        gj3[ny - 1 - j + 1] = gj3[j]
        fj1[ny - 1 - j + 1] = fj1[j]

    for k in range(1, npml + 1):
        ratio = (npml - k + 1) / npml
        zn = sigma_max * (1 - ratio) ** 3
        gk2[k] = 1.0 / (1.0 + zn)
        gk3[k] = (1.0 - zn) / (1.0 + zn)
        fk1[k] = zn
        fk2[k] = 1.0 / (1.0 + zn * 0.5)
        fk3[k] = (1.0 - zn * 0.5) / (1.0 + zn * 0.5)
        gk2[nz - 1 - k + 1] = gk2[k]
        gk3[nz - 1 - k + 1] = gk3[k]
        fk1[nz - 1 - k + 1] = fk1[k]

    return PMLCoefficients(
        gi1=gi1, gi2=gi2, gi3=gi3,
        fi1=fi1, fi2=fi2, fi3=fi3,
        gj1=gj1, gj2=gj2, gj3=gj3,
        fj1=fj1, fj2=fj2, fj3=fj3,
        gk1=gk1, gk2=gk2, gk3=gk3,
        fk1=fk1, fk2=fk2, fk3=fk3,
    )


# ─────────────────────────────────────────────────────────────────────────────
# CLASS-BASED FDTD GRID
# ─────────────────────────────────────────────────────────────────────────────

class FDTDGrid:
    """Encapsulates a 3D FDTD grid with material parameters."""

    def __init__(self, nx, ny, nz, npml=0):
        self.dims = Dimensions(nx=nx, ny=ny, nz=nz,
                                nxa=npml, nya=npml, nza=npml)
        self.nx = nx; self.ny = ny; self.nz = nz
        self.ex = np.zeros((nx, ny, nz), dtype=np.float64)
        self.ey = np.zeros((nx, ny, nz), dtype=np.float64)
        self.ez = np.zeros((nx, ny, nz), dtype=np.float64)
        self.hx = np.zeros((nx, ny, nz), dtype=np.float64)
        self.hy = np.zeros((nx, ny, nz), dtype=np.float64)
        self.hz = np.zeros((nx, ny, nz), dtype=np.float64)
        self.dx = np.zeros((nx, ny, nz), dtype=np.float64)
        self.dy = np.zeros((nx, ny, nz), dtype=np.float64)
        self.dz = np.zeros((nx, ny, nz), dtype=np.float64)
        self.gax = np.ones((nx, ny, nz), dtype=np.float64)
        self.gay = np.ones((nx, ny, nz), dtype=np.float64)
        self.gaz = np.ones((nx, ny, nz), dtype=np.float64)
        self.idx = np.zeros((nx, ny, nz), dtype=np.float64)
        self.idy = np.zeros((nx, ny, nz), dtype=np.float64)
        self.idz = np.zeros((nx, ny, nz), dtype=np.float64)
        self.pml = None

    def set_material(self, x0, y0, z0, dx, dy, dz, eps_r, sigma=0.0):
        x1 = min(x0 + dx, self.nx)
        y1 = min(y0 + dy, self.ny)
        z1 = min(z0 + dz, self.nz)
        self.gax[x0:x1, y0:y1, z0:z1] = 1.0 / eps_r
        self.gbx[x0:x1, y0:y1, z0:z1] = sigma

    def update_H(self):
        nx, ny, nz = self.nx, self.ny, self.nz
        for k in range(1, nz - 1):
            for j in range(1, ny - 1):
                for i in range(1, nx - 1):
                    self.hx[i, j, k] += 0.5 * (
                        self.ey[i, j, k + 1] - self.ey[i, j, k]
                      - self.ez[i, j + 1, k] + self.ez[i, j, k])
                    self.hy[i, j, k] += 0.5 * (
                        self.ez[i + 1, j, k] - self.ez[i, j, k]
                      - self.ex[i, j, k + 1] + self.ex[i, j, k])
                    self.hz[i, j, k] += 0.5 * (
                        self.ex[i, j + 1, k] - self.ex[i, j, k]
                      - self.ey[i + 1, j, k] + self.ey[i, j, k])

    def update_D(self):
        nx, ny, nz = self.nx, self.ny, self.nz
        for k in range(1, nz - 1):
            for j in range(1, ny - 1):
                for i in range(1, nx - 1):
                    self.dx[i, j, k] += 0.5 * (
                        self.hz[i, j, k] - self.hz[i, j - 1, k]
                      - self.hy[i, j, k] + self.hy[i, j, k - 1])
                    self.dy[i, j, k] += 0.5 * (
                        self.hx[i, j, k] - self.hx[i, j, k - 1]
                      - self.hz[i, j, k] + self.hz[i - 1, j, k])
                    self.dz[i, j, k] += 0.5 * (
                        self.hy[i, j, k] - self.hy[i - 1, j, k]
                      - self.hx[i, j, k] + self.hx[i, j - 1, k])

    def update_E(self):
        self.ex[:] = self.gax * self.dx
        self.ey[:] = self.gay * self.dy
        self.ez[:] = self.gaz * self.dz

    def inject_source(self, x, y, z, value):
        self.ez[x, y, z] = value


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 9.1 — Numba JIT-Accelerated 1D FDTD
# ─────────────────────────────────────────────────────────────────────────────
NUMBA_AVAILABLE = False
try:
    from numba import njit, typed
    NUMBA_AVAILABLE = True
except ImportError:
    pass


if NUMBA_AVAILABLE:
    @njit
    def _fdtd_1d_step_jit(ex, hy, kc, nsteps, t0, spread):
        """Numba-JIT compiled 1D FDTD inner loop. 10-100x faster than pure Python."""
        for time_step in range(1, nsteps + 1):
            for k in range(1, len(ex) - 1):
                ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])
            tau = (t0 - time_step) / spread
            pulse = np.exp(-0.5 * tau * tau)
            ex[kc] = pulse
            for k in range(len(hy) - 1):
                hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])
        return ex, hy
else:
    # Stub function for when Numba is not available
    def _fdtd_1d_step_jit(ex, hy, kc, nsteps, t0, spread):
        for time_step in range(1, nsteps + 1):
            for k in range(1, len(ex) - 1):
                ex[k] = ex[k] + 0.5 * (hy[k - 1] - hy[k])
            pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
            ex[kc] = pulse
            for k in range(len(hy) - 1):
                hy[k] = hy[k] + 0.5 * (ex[k] - ex[k + 1])
        return ex, hy


def fd3d_9_1_numba_1d(nsteps=1000, ke=200,
                       kc=None, t0=40, spread=12, plot=True):
    """1D FDTD with Numba JIT acceleration."""
    if kc is None:
        kc = ke // 2

    ex = np.zeros(ke, dtype=np.float64)
    hy = np.zeros(ke, dtype=np.float64)

    if NUMBA_AVAILABLE:
        # Warm up (JIT compilation)
        _fdtd_1d_step_jit(ex.copy(), hy.copy(), kc, 10, t0, spread)
        t_start = timer()
        ex, hy = _fdtd_1d_step_jit(ex, hy, kc, nsteps, t0, spread)
        t_end = timer()
        print(f"Numba 1D FDTD: {nsteps} steps in {t_end-t_start:.4f} s "
              f"({nsteps/(t_end-t_start):.0f} steps/sec)")
    else:
        print("Numba not available, using pure Python fallback")
        t_start = timer()
        ex, hy = _fdtd_1d_step_jit(ex, hy, kc, nsteps, t0, spread)
        t_end = timer()
        print(f"Python 1D FDTD: {nsteps} steps in {t_end-t_start:.4f} s "
              f"({nsteps/(t_end-t_start):.0f} steps/sec)")

    if plot:
        fig, axes = plt.subplots(2, 1, figsize=(8, 3.5))
        axes[0].plot(ex, 'k-', linewidth=1)
        axes[0].set_ylabel(r'$E_x$')
        axes[0].set_xlim(0, ke)
        axes[0].set_title('Numba JIT 1D FDTD')
        axes[1].plot(hy, 'k-', linewidth=1)
        axes[1].set_ylabel(r'$H_y$')
        axes[1].set_xlabel('FDTD cells')
        plt.tight_layout()
        plt.show()

    return ex, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 9.2 — Numba JIT-Accelerated 2D TM FDTD
# ─────────────────────────────────────────────────────────────────────────────
if NUMBA_AVAILABLE:
    @njit
    def _fdtd_2d_tm_step_jit(ez, hx, hy, gaz, ic, jc, t0, spread, time_step):
        """Numba JIT 2D TM FDTD update."""
        nx, ny = ez.shape
        for j in range(1, ny - 1):
            for i in range(1, nx - 1):
                ez[i, j] = gaz[i, j] * (
                    ez[i, j] + 0.5 * (hy[i, j] - hy[i - 1, j]
                                    - hx[i, j] + hx[i, j - 1]))
        tau = (t0 - time_step) / spread
        pulse = np.exp(-0.5 * tau * tau)
        ez[ic, jc] = pulse
        for j in range(1, ny - 2):
            for i in range(1, nx - 1):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])
        for j in range(1, ny - 1):
            for i in range(1, nx - 2):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])
        return ez, hx, hy
else:
    def _fdtd_2d_tm_step_jit(ez, hx, hy, gaz, ic, jc, t0, spread, time_step):
        nx, ny = ez.shape
        for j in range(1, ny - 1):
            for i in range(1, nx - 1):
                ez[i, j] = gaz[i, j] * (
                    ez[i, j] + 0.5 * (hy[i, j] - hy[i - 1, j]
                                    - hx[i, j] + hx[i, j - 1]))
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ez[ic, jc] = pulse
        for j in range(1, ny - 2):
            for i in range(1, nx - 1):
                hx[i, j] += 0.5 * (ez[i, j] - ez[i, j + 1])
        for j in range(1, ny - 1):
            for i in range(1, nx - 2):
                hy[i, j] += 0.5 * (ez[i + 1, j] - ez[i, j])
        return ez, hx, hy


def fd3d_9_2_numba_2d_tm(nsteps=500, ie=60, je=60,
                          ic=None, jc=None,
                          t0=20, spread=8, plot=True):
    """2D TM FDTD with Numba JIT acceleration."""
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    ez  = np.zeros((ie, je), dtype=np.float64)
    hx  = np.zeros((ie, je), dtype=np.float64)
    hy  = np.zeros((ie, je), dtype=np.float64)
    gaz = np.ones((ie, je), dtype=np.float64)

    if NUMBA_AVAILABLE:
        _fdtd_2d_tm_step_jit(ez.copy(), hx.copy(), hy.copy(),
                               gaz, ic, jc, t0, spread, 1)
        t_start = timer()
        for time_step in range(1, nsteps + 1):
            ez, hx, hy = _fdtd_2d_tm_step_jit(ez, hx, hy, gaz,
                                               ic, jc, t0, spread, time_step)
        t_end = timer()
        print(f"Numba 2D TM: {nsteps} steps in {t_end-t_start:.4f} s "
              f"({nsteps/(t_end-t_start):.0f} steps/sec)")
    else:
        t_start = timer()
        for time_step in range(1, nsteps + 1):
            ez, hx, hy = _fdtd_2d_tm_step_jit(ez, hx, hy, gaz,
                                               ic, jc, t0, spread, time_step)
        t_end = timer()
        print(f"Python 2D TM: {nsteps} steps in {t_end-t_start:.4f} s "
              f"({nsteps/(t_end-t_start):.0f} steps/sec)")

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, origin='lower', cmap='RdBu_r',
                        vmin=-1.2, vmax=1.2, aspect='equal')
        ax.set_title(f'2D TM FDTD (Numba JIT, T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 9.3 — Vectorized FDTD (NumPy Broadcasting)
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_9_3_vectorized_2d(nsteps=200, ie=60, je=60,
                            ic=None, jc=None,
                            t0=20, spread=8, plot=True):
    """Vectorized 2D TM FDTD using NumPy broadcasting."""
    if ic is None:
        ic = ie // 2
    if jc is None:
        jc = je // 2

    ez = np.zeros((ie, je), dtype=np.float64)
    hx = np.zeros((ie, je), dtype=np.float64)
    hy = np.zeros((ie, je), dtype=np.float64)

    t_start = timer()
    for time_step in range(1, nsteps + 1):
        ez = ez + 0.5 * (hy - np.roll(hy, 1, axis=0)
                       - hx + np.roll(hx, 1, axis=1))
        pulse = exp(-0.5 * ((t0 - time_step) / spread) ** 2)
        ez[ic, jc] = pulse
        hx = hx + 0.5 * (ez - np.roll(ez, -1, axis=1))
        hy = hy + 0.5 * (np.roll(ez, -1, axis=0) - ez)

    t_end = timer()
    print(f"Vectorized 2D TM: {nsteps} steps in {t_end-t_start:.4f} s "
          f"({nsteps/(t_end-t_start):.0f} steps/sec)")

    if plot:
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, ie, 0, je]
        im = ax.imshow(ez.T, origin='lower', cmap='RdBu_r',
                        vmin=-1.2, vmax=1.2, aspect='equal')
        ax.set_title(f'2D TM FDTD (Vectorized NumPy, T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return ez, hx, hy


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 9.4 — Memory Layout and Performance Comparison
# ─────────────────────────────────────────────────────────────────────────────
def benchmark_memory_layout():
    """Compare row-major (C) vs column-major (Fortran) memory layout."""
    sizes = [40, 60, 80]
    results = []
    for n in sizes:
        arr_c = np.zeros((n, n, n), dtype=np.float64, order='C')
        t_start = timer()
        for _ in range(5):
            for k in range(1, n - 1):
                for j in range(1, n - 1):
                    for i in range(1, n - 1):
                        arr_c[i, j, k] += 0.5
        t_c = timer() - t_start

        arr_f = np.zeros((n, n, n), dtype=np.float64, order='F')
        t_start = timer()
        for _ in range(5):
            for k in range(1, n - 1):
                for j in range(1, n - 1):
                    for i in range(1, n - 1):
                        arr_f[i, j, k] += 0.5
        t_f = timer() - t_start

        results.append((n, t_c, t_f))
        print(f"  Grid {n}x{n}x{n}: C-order={t_c:.4f}s, F-order={t_f:.4f}s "
              f"(speedup={t_f/t_c:.2f}x)")

    return results


# ─────────────────────────────────────────────────────────────────────────────
# PROGRAM 9.5 — Class-Based 3D FDTD
# ─────────────────────────────────────────────────────────────────────────────
def fd3d_9_5_class_3d(nsteps=100, nx=40, ny=40, nz=40,
                       ic=None, jc=None, kc=None,
                       t0=20, spread=8, plot=True):
    """3D FDTD using class-based grid management."""
    if ic is None:
        ic = nx // 2
    if jc is None:
        jc = ny // 2
    if kc is None:
        kc = nz // 2

    grid = FDTDGrid(nx, ny, nz, npml=0)

    t_start = timer()
    for time_step in range(1, nsteps + 1):
        grid.update_D()
        grid.update_E()
        grid.inject_source(ic, jc, kc,
                            exp(-0.5 * ((t0 - time_step) / spread) ** 2))
        grid.update_H()

    t_end = timer()
    print(f"Class-based 3D FDTD: {nsteps} steps in {t_end-t_start:.4f} s")

    if plot:
        k_mid = nz // 2
        fig, ax = plt.subplots(figsize=(6, 5))
        extent = [0, nx, 0, ny]
        im = ax.imshow(grid.ez[:, :, k_mid].T, origin='lower',
                        cmap='RdBu_r', aspect='equal',
                        vmin=-1.2, vmax=1.2)
        ax.set_title(f'3D FDTD: Ez at z={k_mid} (T={nsteps})')
        ax.set_xlabel('i')
        ax.set_ylabel('j')
        plt.colorbar(im, ax=ax, label=r'$E_z$')
        plt.tight_layout()
        plt.show()

    return grid.ez, grid.hz


# ─────────────────────────────────────────────────────────────────────────────
# VERIFICATION
# ─────────────────────────────────────────────────────────────────────────────
def verify():
    """Self-check Ch9 advanced Python code."""
    print("=== Ch9 Verification ===")

    const = make_constants(ddx=0.5, npml=8)
    assert const.ddx == 0.5 and const.dt == 0.25
    print("  [OK] Constants namedtuple")

    pml = calculate_pml_coefficients(40, 40, 40, npml=8)
    assert pml.gi2[8] < 1.0, "PML gi2 should be < 1"
    print("  [OK] PML coefficients")

    grid = FDTDGrid(30, 30, 30)
    assert grid.ex.shape == (30, 30, 30)
    assert grid.gaz.shape == (30, 30, 30)
    print("  [OK] FDTDGrid class")

    ex, hy = fd3d_9_1_numba_1d(nsteps=100, ke=50, plot=False)
    assert abs(ex).max() > 0, "Numba 1D: no field"
    print("  [OK] Numba 1D FDTD")

    ez, _, _ = fd3d_9_2_numba_2d_tm(nsteps=100, ie=40, je=40, plot=False)
    assert abs(ez).max() > 0, "Numba 2D: no field"
    print("  [OK] Numba 2D TM FDTD")

    ez_v, _, _ = fd3d_9_3_vectorized_2d(nsteps=100, ie=40, je=40, plot=False)
    assert abs(ez_v).max() > 0, "Vectorized: no field"
    print("  [OK] Vectorized NumPy 2D FDTD")

    print("All Ch9 examples passed verification.")


if __name__ == "__main__":
    print("=" * 60)
    print("Houle & Sullivan Ch9 — Advanced Python Features")
    print("=" * 60)

    print(f"\nNumba available: {NUMBA_AVAILABLE}")

    print("\n--- Program 9.1: Numba JIT 1D ---")
    fd3d_9_1_numba_1d(nsteps=500, ke=200, plot=False)

    print("\n--- Program 9.2: Numba JIT 2D TM ---")
    fd3d_9_2_numba_2d_tm(nsteps=200, ie=60, je=60, plot=False)

    print("\n--- Program 9.3: Vectorized NumPy ---")
    fd3d_9_3_vectorized_2d(nsteps=100, ie=60, je=60, plot=False)

    print("\n--- Program 9.4: Memory Layout Benchmark ---")
    benchmark_memory_layout()

    print("\n--- Program 9.5: Class-Based 3D FDTD ---")
    fd3d_9_5_class_3d(nsteps=60, nx=40, ny=40, nz=40, plot=False)

    print("\n=== Verification ===")
    verify()
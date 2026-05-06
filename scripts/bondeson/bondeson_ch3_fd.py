#!/usr/bin/env python3
"""
Bondeson Computational Electromagnetics - Chapter 3: Finite Differences
FDTD discretization, numerical error, convergence analysis
"""
import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch3.1 - Laplace equation finite difference grid
ax = axes[0, 0]
nx, ny = 20, 15
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

# Solve Laplace equation with Dirichlet BCs: V=1 at left, V=0 at right
V = np.zeros((ny, nx))
V[:, 0] = 1.0   # left boundary
V[:, -1] = 0.0  # right boundary

# Gauss-Seidel iteration
for _ in range(500):
    V_new = V.copy()
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            V_new[i, j] = 0.25 * (V[i+1, j] + V[i-1, j] + V[i, j+1] + V[i, j-1])
    V = V_new

im = ax.imshow(V, extent=[0, 1, 0, 1], origin='lower', cmap='RdBu', aspect='auto')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Laplace Equation: V(x,y) via Finite Differences')
plt.colorbar(im, ax=ax, label='Potential V')

# Ch3.2 - Convergence of Gauss-Seidel
ax = axes[0, 1]
grid_sizes = [10, 20, 40, 80]
errors = []
for n in grid_sizes:
    V_n = np.zeros((n, n))
    V_n[:, 0] = 1.0
    V_n[:, -1] = 0.0
    for _ in range(1000):
        V_old = V_n.copy()
        for i in range(1, n-1):
            for j in range(1, n-1):
                V_n[i, j] = 0.25 * (V_n[i+1, j] + V_n[i-1, j] + V_n[i, j+1] + V_n[i, j-1])
        if np.max(np.abs(V_n - V_old)) < 1e-10:
            break
    errors.append(np.max(np.abs(V_n - V_old)))

ax.loglog(grid_sizes, errors, 'bo-', lw=2, markersize=8)
ax.set_xlabel('Grid Size N')
ax.set_ylabel('Max Residual Error')
ax.set_title('Gauss-Seidel Convergence vs Grid Size')
ax.grid(True, alpha=0.3)

# Ch3.3 - Central difference approximation error
ax = axes[1, 0]
h = np.logspace(-4, -1, 50)
f = np.sin
x0 = 1.0
df_analytical = np.cos(x0)

# Central difference: (f(x+h) - f(x-h)) / (2h)
df_numerical = (np.sin(x0 + h) - np.sin(x0 - h)) / (2 * h)
error = np.abs(df_numerical - df_analytical)

ax.loglog(h, error, 'b-', lw=2, label='Numerical error')
ax.loglog(h, h**2 * 0.1, 'r--', lw=2, label=r'$O(h^2)$ reference')
ax.set_xlabel('Step size h')
ax.set_ylabel('|Error|')
ax.set_title('Central Difference: Second Derivative Error vs Step Size')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch3.4 - FDTD Yee cell visualization
ax = axes[1, 1]
# Draw a simple Yee cell grid
for i in range(5):
    for j in range(5):
        x, y = i * 0.3, j * 0.3
        # E nodes (cross)
        ax.plot([x - 0.1, x + 0.1], [y, y], 'r-', lw=2, alpha=0.7)  # Ex
        ax.plot([x, x], [y - 0.1, y + 0.1], 'b-', lw=2, alpha=0.7)  # Ey
        # H nodes (diamond, offset)
        ax.scatter([x + 0.15], [y + 0.15], color='green', s=30, zorder=5)

ax.plot([], [], 'r-', lw=2, label='E-field components')
ax.plot([], [], 'b-', lw=2, label='E-field components')
ax.scatter([], [], color='green', s=30, label='H-field nodes')
ax.set_xlim(-0.2, 1.7)
ax.set_ylim(-0.2, 1.7)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Yee Cell: FDTD Staggered Grid')
ax.legend(fontsize=8)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch3_fd.png', dpi=150)
plt.close()
print("bondeson_ch3_fd.png saved")

# Ch3.5 - Capacitance calculation via FD
fig, ax = plt.subplots()
nx, ny = 50, 30
V = np.zeros((ny, nx))
# Parallel plate: V=0 at top and bottom, V=1 at left/right
V[0, :] = 0
V[-1, :] = 0
V[:, 0] = 1
V[:, -1] = 1
# Init interior
for _ in range(2000):
    V_old = V.copy()
    for i in range(1, ny-1):
        for j in range(1, nx-1):
            V[i, j] = 0.25 * (V[i+1,j] + V[i-1,j] + V[i,j+1] + V[i,j-1])

ax.imshow(V, aspect='auto', cmap='coolwarm')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('2D Electrostatic Potential: Parallel Plate Capacitor')
plt.colorbar(ax.images[0], label='V')
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch3_capacitor.png', dpi=150)
plt.close()
print("bondeson_ch3_capacitor.png saved")

# Ch3.6 - FEM mesh quality
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Poor mesh
ax = axes[0]
np.random.seed(42)
n_pts = 50
x_poor = np.random.rand(n_pts) + np.random.randn(n_pts) * 0.1
y_poor = np.random.rand(n_pts) + np.random.randn(n_pts) * 0.1
from scipy.spatial import Delaunay
tri_poor = Delaunay(np.column_stack([x_poor, y_poor]))
ax.triplot(x_poor, y_poor, tri_poor.simplices, 'b-', lw=0.5)
ax.scatter(x_poor, y_poor, c='red', s=10)
ax.set_title('Poor Quality Mesh (random points)')
ax.set_aspect('equal')

# Good mesh
ax = axes[1]
x_good = np.linspace(0, 1, 15)
y_good = np.linspace(0, 1, 15)
X_g, Y_g = np.meshgrid(x_good, y_good)
points = np.column_stack([X_g.ravel(), Y_g.ravel()])
tri_good = Delaunay(points)
ax.triplot(points[:, 0], points[:, 1], tri_good.simplices, 'g-', lw=0.5)
ax.scatter(points[:, 0], points[:, 1], c='blue', s=10)
ax.set_title('Good Quality Mesh (structured points)')
ax.set_aspect('equal')

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch3_mesh_quality.png', dpi=150)
plt.close()
print("bondeson_ch3_mesh_quality.png saved")
print("bondeson ch3 code complete!")
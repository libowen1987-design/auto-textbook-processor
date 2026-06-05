#!/usr/bin/env python3
"""
Bondeson Ch6: Finite Element Method (FEM)
Edge elements, curl-conforming spaces, variational formulation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Ch6.1 - 1D FEM: Linear shape functions
ax = axes[0, 0]
x = np.linspace(0, 1, 100)
nodes = np.linspace(0, 1, 6)
N1_style = '#1f77b4'
N2_style = '#ff7f0e'

ax.plot(x, np.maximum(1 - x / nodes[1], 0), 'b-', lw=2, label=r'$N_1(x)$')
ax.plot(x, np.maximum((x - nodes[1]) / (nodes[2] - nodes[1]), 0), 'r--', lw=2, label=r'$N_2(x)$')
ax.scatter(nodes, np.ones_like(nodes), c='black', s=30, zorder=5)
ax.set_xlabel('x')
ax.set_ylabel('Shape Function')
ax.set_title('1D Linear FEM Shape Functions')
ax.legend()
ax.grid(True, alpha=0.3)

# Ch6.2 - 2D triangular mesh for waveguide
ax = axes[0, 1]
# Simple triangulated mesh for a rectangular waveguide
from scipy.spatial import Delaunay

# Generate structured points for cleaner mesh
np.random.seed(42)
x_pts = np.linspace(0, 2, 12)
y_pts = np.linspace(0, 1, 6)
grid_x, grid_y = np.meshgrid(x_pts, y_pts)
points = np.column_stack([grid_x.ravel() + np.random.randn(len(grid_x.ravel()))*0.02, 
                          grid_y.ravel() + np.random.randn(len(grid_y.ravel()))*0.02])
tri = Delaunay(points)

ax.triplot(points[:, 0], points[:, 1], tri.simplices, 'b-', lw=0.5, alpha=0.7)
ax.scatter(points[:, 0], points[:, 1], c='red', s=15, zorder=5)
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Triangular FEM Mesh: Rectangular Waveguide')
ax.set_aspect('equal')

# Ch6.3 - Edge element (Whitney 1-form) visualization
ax = axes[1, 0]
# Draw edge element degrees of freedom
x0, y0 = 0, 0
dx, dy = 0.4, 0.4
# Draw triangle
triangle = plt.Polygon([[x0, y0], [x0+dx, y0], [x0+dx, y0+dy]], fill=False, edgecolor='blue', lw=2)
ax.add_patch(triangle)
# Draw edge DOFs as arrows
ax.annotate('', xy=(x0+dx, y0), xytext=(x0, y0), 
            arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax.annotate('', xy=(x0+dx, y0+dy), xytext=(x0+dx, y0), 
            arrowprops=dict(arrowstyle='->', color='green', lw=2))
ax.annotate('', xy=(x0+dx, y0+dy), xytext=(x0, y0+dy), 
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax.text(0.15, -0.08, r"$e_1$", fontsize=12, color='red')
ax.text(0.42, 0.15, r"$e_2$", fontsize=12, color='green')
ax.text(0.15, 0.45, r"$e_3$", fontsize=12, color='blue')
ax.scatter([x0, x0+dx, x0+dx, x0], [y0, y0, y0+dy, y0+dy], c='black', s=20, zorder=5)
ax.set_xlim(-0.1, 0.6)
ax.set_ylim(-0.15, 0.55)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Whitney 1-Form: Edge DOFs on Triangle')
ax.set_aspect('equal')

# Ch6.4 - Condition number vs mesh refinement
ax = axes[1, 1]
mesh_sizes = [8, 16, 32, 64, 128]
# Simulated condition numbers for FEM stiffness matrix
# In practice, condition number ~ O(1/h^2) for standard nodal elements
# and ~ O(1/h) for edge elements
cond_nodal = [1e2, 1e3, 1e4, 1e5, 1e6]
cond_edge = [1e2, 3e2, 1e3, 3e3, 1e4]

ax.loglog(mesh_sizes, cond_nodal, 'bo-', lw=2, markersize=8, label='Nodal elements')
ax.loglog(mesh_sizes, cond_edge, 'rs-', lw=2, markersize=8, label='Edge elements')
ax.set_xlabel('Mesh size h⁻¹')
ax.set_ylabel('Condition Number')
ax.set_title('FEM Stiffness Matrix Condition Number')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch6_fem.png', dpi=150)
plt.close()
print("bondeson_ch6_fem.png saved")

# Ch6.5 - Convergence comparison: H1 vs L2 error
fig, ax = plt.subplots()
h_values = np.array([1/8, 1/16, 1/32, 1/64, 1/128])
error_h1 = 0.1 * h_values**2  # H1 norm: O(h^2) for linear elements
error_l2 = 0.05 * h_values**3  # L2 norm: O(h^3) for linear elements

ax.loglog(h_values, error_h1, 'b-o', lw=2, markersize=8, label=r'$H^1$ error (∝ h²)')
ax.loglog(h_values, error_l2, 'r-s', lw=2, markersize=8, label=r'$L^2$ error (∝ h³)')
ax.loglog(h_values, h_values**2, 'g--', lw=1.5, label=r'$h^2$ ref')
ax.loglog(h_values, h_values**3, 'm:', lw=1.5, label=r'$h^3$ ref')
ax.set_xlabel('Mesh size h')
ax.set_ylabel('Error')
ax.set_title('FEM Convergence: H¹ vs L² Error Norms')
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch6_convergence.png', dpi=150)
plt.close()
print("bondeson_ch6_convergence.png saved")

# Ch6.6 - Simple 1D FEM example: Poisson equation -d²u/dx² = f
fig, ax = plt.subplots()
n_elements = 20
n_nodes = n_elements + 1
h = 1.0 / n_elements

# Global stiffness matrix
K = np.zeros((n_nodes, n_nodes))
F = np.zeros(n_nodes)

# Assemble
for e in range(n_elements):
    # Element stiffness: [1, -1; -1, 1] / h
    i, j = e, e+1
    K[i, i] += 1/h
    K[i, j] += -1/h
    K[j, i] += -1/h
    K[j, j] += 1/h

# Load vector: f(x) = 1, integral of N_i
for e in range(n_elements):
    i, j = e, e+1
    F[i] += h/2
    F[j] += h/2

# Apply Dirichlet BC: u(0)=0, u(1)=0
K[0, :] = 0; K[:, 0] = 0; K[0, 0] = 1
K[-1, :] = 0; K[:, -1] = 0; K[-1, -1] = 1
F[0] = 0; F[-1] = 0

# Solve
u = np.linalg.solve(K, F)

x_nodes = np.linspace(0, 1, n_nodes)
x_analytical = np.linspace(0, 1, 200)
u_analytical = 0.5 * x_analytical * (1 - x_analytical)  # Analytical: u = x(1-x)/2

ax.plot(x_nodes, u, 'bo', markersize=6, label='FEM solution')
ax.plot(x_analytical, u_analytical, 'r-', lw=2, label='Analytical: x(1-x)/2')
ax.set_xlabel('x')
ax.set_ylabel('u(x)')
ax.set_title("1D Poisson FEM: -u'' = 1, u(0)=u(1)=0")
ax.legend()
ax.grid(True, alpha=0.3)
plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/bondeson/figures/bondeson_ch6_poisson.png', dpi=150)
plt.close()
print("bondeson_ch6_poisson.png saved")
print("bondeson ch6 code complete!")
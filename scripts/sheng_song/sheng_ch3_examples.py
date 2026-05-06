"""
Sheng & Song, Chapter 3: Finite-Element Method
Code examples: waveguide eigenvalue, edge element assembly, 2D scattering (FEM)
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh
from scipy.sparse import coo_matrix, lil_matrix
from scipy.sparse.linalg import eigsh


# =============================================================================
# Example 1: Eigenmodes of a dielectric-loaded waveguide
# (Simplified 2D model using nodal FEM, not edge elements)
# =============================================================================

def waveguide_eigenmode(a=1.0, b=1.0, epsilon_r=2.1, mu_r=1.0, n_elements=20):
    """
    Solve for propagation constants of dielectric-loaded rectangular waveguide.
    
    The waveguide (a x b cross-section) has one region with permittivity epsilon_r
    and the rest is air (epsilon_r=1).
    
    Simplified model: 2D scalar Helmholtz equation for TE modes.
    d^2 phi/dx^2 + d^2 phi/dy^2 + k_t^2 phi = 0
    where k_t^2 = k0^2*epsilon_r - beta^2
    
    This uses nodal linear triangles (not edge elements) for demonstration.
    
    Parameters
    ----------
    a, b     : waveguide dimensions [m]
    epsilon_r: relative permittivity of loading
    mu_r     : relative permeability
    n_elements: mesh density per dimension
    
    Returns
    -------
    beta     : propagation constants [rad/m] for k0=1 rad/m
    """
    # Physical constants
    c = 3e8  # speed of light [m/s]
    k0 = 2 * np.pi  # free-space wavenumber at 1 GHz
    
    # --- Build mesh ---
    nx = n_elements
    ny = n_elements
    hx = a / nx
    hy = b / ny
    
    # Node grid
    nnode_x = nx + 1
    nnode_y = ny + 1
    n_nodes = nnode_x * nnode_y
    
    x = np.linspace(0, a, nnode_x)
    y = np.linspace(0, b, nnode_y)
    xx, yy = np.meshgrid(x, y)
    node_x = xx.flatten()
    node_y = yy.flatten()
    
    # Element connectivity (triangular mesh)
    elements = []
    for j in range(ny):
        for i in range(nx):
            n00 = j * nnode_x + i
            n10 = n00 + 1
            n01 = n00 + nnode_x
            n11 = n01 + 1
            # Two triangles per rectangle
            elements.append([n00, n10, n01])
            elements.append([n10, n11, n01])
    
    n_elements = len(elements)
    elements = np.array(elements, dtype=int)
    
    # --- Identify interior and boundary nodes ---
    # PEC on all walls: phi = 0 on boundaries
    is_bdy = np.zeros(n_nodes, dtype=bool)
    for n in range(n_nodes):
        xi = node_x[n]
        yj = node_y[n]
        if abs(xi) < 1e-10 or abs(xi - a) < 1e-10 or abs(yj) < 1e-10 or abs(yj - b) < 1e-10:
            is_bdy[n] = True
    
    # --- Assemble stiffness and mass matrices ---
    n_free = n_nodes - is_bdy.sum()
    free_idx = np.where(~is_bdy)[0]
    
    # Map global free node index to matrix index
    free_map = np.full(n_nodes, -1)
    free_map[free_idx] = np.arange(n_free)
    
    # Element matrices (linear triangles)
    K = lil_matrix((n_free, n_free))
    M = lil_matrix((n_free, n_free))
    
    for elem in elements:
        # Get node coordinates
        x1, y1 = node_x[elem[0]], node_y[elem[0]]
        x2, y2 = node_x[elem[1]], node_y[elem[1]]
        x3, y3 = node_x[elem[2]], node_y[elem[2]]
        
        # Jacobian
        b1 = y2 - y3
        b2 = y3 - y1
        b3 = y1 - y2
        c1 = x3 - x2
        c2 = x1 - x3
        c3 = x2 - x1
        J = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
        Area = abs(J) / 2.0
        
        # For dielectric loading: center of element determines epsilon_r
        xm = (x1 + x2 + x3) / 3.0
        ym = (y1 + y2 + y3) / 3.0
        # Central loading region (half-width strip)
        er = epsilon_r if (0.3*a <= xm <= 0.7*a) else 1.0
        mr = mu_r
        
        # Local stiffness matrix (grad N_i · grad N_j)
        for i_local, i_global in enumerate(elem):
            if is_bdy[i_global]:
                continue
            mi = free_map[i_global]
            for j_local, j_global in enumerate(elem):
                if is_bdy[j_global]:
                    continue
                mj = free_map[j_global]
                
                # Coefficient: (1/mu_r) * (b_i * b_j + c_i * c_j) / (4*Area)
                coef = (b1 if i_local == 0 else b2 if i_local == 1 else b3) * \
                       (b1 if j_local == 0 else b2 if j_local == 1 else b3) + \
                       (c1 if i_local == 0 else c2 if i_local == 1 else c3) * \
                       (c1 if j_local == 0 else c2 if j_local == 1 else c3)
                coef = coef / (4.0 * Area * mr)
                K[mi, mj] += coef
                
                # Mass matrix: N_i * N_j
                # Integral of N_i * N_j over triangle = Area / 6 for i==j, Area/12 for i!=j
                if i_local == j_local:
                    mass_coef = Area / 3.0
                else:
                    mass_coef = Area / 6.0
                M[mi, mj] += k0**2 * er * mass_coef
    
    K = K.tocoo()
    M = M.tocoo()
    
    # --- Solve generalized eigenvalue: K * u = lambda * M * u ---
    # lambda = k_t^2 = k0^2*epsilon_r - beta^2
    def matvec(v):
        return K @ v - (k0**2) * (M @ v)  # Wrong: we want K u = lambda M u
    
    # Actually solve K u = omega^2 M u (standard)
    # For waveguide, k0 is fixed, we solve for beta
    # From functional: K(beta) = 0, with k0 fixed and beta unknown
    # Simplified: we solve for k_t^2 = k0^2 - beta^2 (assuming er=1 regions)
    # Here we just do a standard eigenvalue problem A x = lambda x for demonstration
    
    # Use dense for small example
    K_d = K.toarray()
    M_d = M.toarray()
    
    # Solve K * phi = lambda * M * phi  => lambda = k_t^2
    try:
        eigenvalues, eigenvectors = eigh(K_d, M_d)
        # Filter positive eigenvalues and sort
        pos_mask = (eigenvalues > 0) & ~np.isnan(eigenvalues) & ~np.isinf(eigenvalues)
        k_t_sq = eigenvalues[pos_mask]
        k_t_sq = np.sort(k_t_sq)
        betas = np.sqrt(k0**2 - k_t_sq)
        
        print(f"Found {len(betas)} propagating modes (beta > 0)")
        print(f"First 5 propagation constants (beta):")
        for i, beta in enumerate(betas[:5]):
            print(f"  Mode {i+1}: beta = {beta:.4f} rad/m  (k0 = {k0:.4f})")
        return betas
    except Exception as e:
        print(f"Eigenvalue solve failed: {e}")
        return np.array([])


# =============================================================================
# Example 2: Edge element basis functions on a triangle
# =============================================================================

def edge_element_on_triangle():
    """
    Compute edge element (Whitney) basis functions N_i on a reference triangle.
    
    For a triangle with nodes (x1,y1), (x2,y2), (x3,y3) labeled anticlockwise,
    the area coordinates L_i and edge element basis functions are:
    
    L_i = area_i / total_area
    N_i = (L_j * grad(L_k) - L_k * grad(L_j)) * l_i
    
    where (i,j,k) is a cyclic permutation of (1,2,3).
    """
    # Triangle vertices (example)
    nodes = np.array([[0.0, 0.0],
                       [1.0, 0.0],
                       [0.5, 0.866025]])  # equilateral triangle, side=1
    
    x1, y1 = nodes[0]
    x2, y2 = nodes[1]
    x3, y3 = nodes[2]
    
    # Area
    J = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
    A = abs(J) / 2.0
    print(f"Triangle area: {A:.6f}")
    
    # Edge vectors
    r21 = nodes[1] - nodes[0]
    r32 = nodes[2] - nodes[1]
    r13 = nodes[0] - nodes[2]
    
    # Edge lengths
    l1 = np.linalg.norm(r32)  # edge opposite node 1
    l2 = np.linalg.norm(r13)  # edge opposite node 2
    l3 = np.linalg.norm(r21)  # edge opposite node 3
    
    print(f"Edge lengths: l1={l1:.6f}, l2={l2:.6f}, l3={l3:.6f}")
    
    # Edge unit vectors (pointing from start to end in local numbering)
    # edge 1: from node 2 to node 3 (opposite node 1)
    e1 = r32 / l1
    # edge 2: from node 3 to node 1 (opposite node 2)
    e2 = r13 / l2
    # edge 3: from node 1 to node 2 (opposite node 3)
    e3 = r21 / l3
    
    print(f"Edge unit vectors:\n  e1={e1}, e2={e2}, e3={e3}")
    
    # Compute grad(L_i) using formula: grad(L_i) = (1/(2A)) * (b_i, c_i)
    # where for node i with coordinates (x_i, y_i):
    # b_i = y_j - y_k, c_i = x_k - x_j (cyclic i,j,k)
    
    def grad_L(i):
        j = (i) % 3 + 1 - 1
        k = (i + 1) % 3 + 1 - 1
        b_i = nodes[j][1] - nodes[k][1]
        c_i = nodes[k][0] - nodes[j][0]
        return np.array([b_i, c_i]) / (2 * A)
    
    # Compute basis functions N_i at triangle centroid
    L1_cent = 1.0 / 3.0
    L2_cent = 1.0 / 3.0
    L3_cent = 1.0 / 3.0
    
    grad_L1 = grad_L(0)
    grad_L2 = grad_L(1)
    grad_L3 = grad_L(2)
    
    # N1 = (L2*grad(L3) - L3*grad(L2)) * l1
    N1 = (L2_cent * grad_L3 - L3_cent * grad_L2) * l1
    N2 = (L3_cent * grad_L1 - L1_cent * grad_L3) * l2
    N3 = (L1_cent * grad_L2 - L2_cent * grad_L1) * l3
    
    print("\nEdge element basis functions at centroid:")
    print(f"  N1 = {N1}")
    print(f"  N2 = {N2}")
    print(f"  N3 = {N3}")
    
    # Verify the tangential property: e_i · N_i = 1, e_j · N_i = 0 for j != i
    print("\nVerification of tangential property:")
    print(f"  e1 · N1 = {np.dot(e1, N1):.6f} (should be 1)")
    print(f"  e2 · N1 = {np.dot(e2, N1):.6f} (should be 0)")
    print(f"  e3 · N1 = {np.dot(e3, N1):.6f} (should be 0)")
    print(f"  e2 · N2 = {np.dot(e2, N2):.6f} (should be 1)")
    print(f"  e3 · N2 = {np.dot(e3, N2):.6f} (should be 0)")
    
    return N1, N2, N3


# =============================================================================
# Example 3: 2D FEM scattering with PML truncation
# =============================================================================

def fem_2d_scattering_plane_wave(L=2.0, n_cell=40, k0=20.0):
    """
    2D FEM scattering by a dielectric cylinder using triangular mesh.
    
    Solve: ∇×(1/μ_r ∇×E_z) - k0^2 ε_r E_z = -j k0 Z0 J_z
    
    PEC cylinder: E_z = 0 on cylinder surface
    PML: uniaxial PML with conductivity profile
    
    Parameters
    ----------
    L      : domain half-size [wavelengths] (domain is [-L, L] x [-L, L])
    n_cell : number of cells per dimension
    k0     : wavenumber (free-space)
    
    Returns
    -------
    E_z    : 2D field map (complex)
    """
    # --- Mesh ---
    n_nodes = (n_cell + 1) ** 2
    h = 2 * L / n_cell
    
    x = np.linspace(-L, L, n_cell + 1)
    y = np.linspace(-L, L, n_cell + 1)
    xx, yy = np.meshgrid(x, y)
    node_x = xx.flatten()
    node_y = yy.flatten()
    
    # Element connectivity
    elements = []
    for j in range(n_cell):
        for i in range(n_cell):
            n00 = j * (n_cell + 1) + i
            n10 = n00 + 1
            n01 = n00 + (n_cell + 1)
            n11 = n01 + 1
            elements.append([n00, n10, n01])
            elements.append([n10, n11, n01])
    elements = np.array(elements, dtype=int)
    n_elem = len(elements)
    
    # --- PEC cylinder in center (r < 0.3) ---
    r_cylinder = 0.3  # in wavelengths (L is in wavelengths)
    is_pec = np.array([np.sqrt(node_x[i]**2 + node_y[i]**2) < r_cylinder 
                       for i in range(n_nodes)])
    
    # --- PML layers (outer 5 cells) ---
    pml_thickness = 5
    pml_width = pml_thickness * h
    pml_sigma0 = 2.0  # maximum conductivity
    
    def pml_conductivity(xi, yj):
        dist = max(abs(xi) - (L - pml_width), abs(yj) - (L - pml_width), 0.0)
        if dist <= 0:
            return 0.0
        sigma = pml_sigma0 * (dist / pml_width) ** 2
        return sigma
    
    # --- Plane wave (x-polarized, propagating in +z direction, TE case: Ez only) ---
    # E_i = e^{-j k0 x} (for plane wave along y-direction)
    # Incident field on each node
    E_inc = np.exp(1j * k0 * node_x)
    
    # --- Assemble sparse FEM matrices ---
    from scipy.sparse import lil_matrix
    from scipy.sparse.linalg import spsolve
    
    n_unknowns = n_nodes
    K = lil_matrix((n_unknowns, n_unknowns), dtype=complex)
    RHS = np.zeros(n_unknowns, dtype=complex)
    
    # Build element loop
    for elem_idx, elem in enumerate(elements):
        # Node coordinates
        x1, y1 = node_x[elem[0]], node_y[elem[0]]
        x2, y2 = node_x[elem[1]], node_y[elem[1]]
        x3, y3 = node_x[elem[2]], node_y[elem[2]]
        
        # Area
        J = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
        Area = abs(J) / 2.0
        
        # Centroid
        xm = (x1 + x2 + x3) / 3.0
        ym = (y1 + y2 + y3) / 3.0
        
        # Material properties
        r_meas = np.sqrt(xm**2 + ym**2)
        if r_meas < r_cylinder:
            # PEC: handled by boundary condition, skip this element
            er = 1.0
            mr = 1.0
            is_pec_elem = True
        else:
            er = 2.0  # dielectric cylinder
            mr = 1.0
            is_pec_elem = False
        
        # PML: modify material for absorbing boundary
        sigma = pml_conductivity(xm, ym)
        if sigma > 0:
            # Uniaxial PML: effective ε_r and μ_r are modified
            # For simplicity, use reduced permittivity in PML region
            # (Proper PML needs coordinate stretching in matrix assembly)
            pml_factor = 1.0 + 1j * sigma / k0
            er_pml = er * pml_factor
            mr_pml = mr * pml_factor
        else:
            er_pml = er
            mr_pml = mr
        
        # b and c coefficients for gradient
        b1 = y2 - y3
        b2 = y3 - y1
        b3 = y1 - y2
        c1 = x3 - x2
        c2 = x1 - x3
        c3 = x2 - x1
        
        # Element matrix (E_z scalar case, simplified)
        for a_local, a_global in enumerate(elem):
            if is_pec[a_global]:
                continue
            for b_local, b_global in enumerate(elem):
                if is_pec[b_global]:
                    continue
                
                # (1/mu_r) * grad(N_a) · grad(N_b) - k0^2 * eps_r * N_a * N_b
                grad_a = np.array([b1, c1]) / (2 * Area)
                grad_b = np.array([b2, c2]) / (2 * Area)
                if a_local == 1:
                    grad_a = np.array([b2, c2]) / (2 * Area)
                if a_local == 2:
                    grad_a = np.array([b3, c3]) / (2 * Area)
                if b_local == 1:
                    grad_b = np.array([b2, c2]) / (2 * Area)
                if b_local == 2:
                    grad_b = np.array([b3, c3]) / (2 * Area)
                
                stiff = (1.0 / mr_pml) * np.dot(grad_a, grad_b) * Area
                mass = k0**2 * er_pml * Area / 6.0  # approximate
                K[a_global, b_global] += stiff - mass
    
    # --- Impose boundary conditions (PEC: E_z = 0 on cylinder) ---
    # For interior PEC: set row/col to identity and RHS to 0
    for n in range(n_nodes):
        if is_pec[n]:
            K[n, :] = 0
            K[:, n] = 0
            K[n, n] = 1.0
            RHS[n] = 0.0
    
    # --- Solve ---
    K_csr = K.tocsr()
    try:
        E_z = spsolve(K_csr, RHS)
    except Exception as e:
        print(f"Solve failed: {e}")
        E_z = np.zeros(n_nodes)
    
    # --- Reshape and plot ---
    E_z_map = E_z.reshape(n_cell + 1, n_cell + 1)
    
    plt.figure(figsize=(8, 6))
    plt.imshow(np.abs(E_z_map), extent=[-L, L, -L, L], origin='lower', cmap='RdBu')
    plt.colorbar(label='|E_z|')
    plt.xlabel('x (wavelengths)')
    plt.ylabel('y (wavelengths)')
    plt.title('2D FEM Scattering: |E_z|')
    plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch3_fem_2d_scattering.png', dpi=150)
    plt.close()
    print("Saved figure: sheng_ch3_fem_2d_scattering.png")
    
    return E_z_map


# =============================================================================
# Example 4: Convergence study for waveguide eigenvalue
# =============================================================================

def waveguide_convergence():
    """
    Study convergence of numerical eigenvalue vs mesh density.
    """
    betas = []
    for n in [10, 15, 20, 30]:
        beta = waveguide_eigenmode(n_elements=n)
        if len(beta) > 0:
            betas.append(beta[0])
    
    if len(betas) >= 2:
        plt.figure(figsize=(8, 4))
        n_elements = [10, 15, 20, 30]
        plt.plot(n_elements, betas, 'o-', color='steelblue', linewidth=2)
        plt.xlabel('Mesh density (elements per dimension)')
        plt.ylabel('Propagation constant beta [rad/m]')
        plt.title('Convergence of First Mode: Dielectric-Loaded Waveguide')
        plt.grid(True, alpha=0.4)
        plt.savefig('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures/sheng_ch3_convergence.png', dpi=150)
        plt.close()
        print("Saved figure: sheng_ch3_convergence.png")
    
    return betas


if __name__ == '__main__':
    print("=" * 60)
    print("Sheng Ch3: Finite-Element Method - Code Examples")
    print("=" * 60)
    
    import os
    os.makedirs('/home/ubuntu/.openclaw/workspace/textbooks/sheng_song/figures', exist_ok=True)
    
    print("\n--- Example 1: Waveguide Eigenmode ---")
    waveguide_eigenmode()
    
    print("\n--- Example 2: Edge Element Basis Functions ---")
    edge_element_on_triangle()
    
    print("\n--- Example 3: 2D FEM Scattering (PML truncated) ---")
    fem_2d_scattering_plane_wave()
    
    print("\n--- Example 4: Convergence Study ---")
    waveguide_convergence()
    
    print("\n" + "=" * 60)
    print("All examples completed.")
    print("=" * 60)
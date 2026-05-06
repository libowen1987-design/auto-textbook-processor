# Chapter 8: The Finite Difference Method (FDM/FDTD)

**Source:** Jin, *Theory and Computation of Electromagnetic Fields*, 2nd Ed., Chapter 8 (pp. 409–456)

---

## 8.1 Basic Finite Differencing

### 8.1.1 Finite Difference Approximations

Central difference for first derivative:
$$
\frac{df}{dx}\bigg|_i \approx \frac{f_{i+1} - f_{i-1}}{2\Delta x} + O(\Delta x^2)
\tag{8.1.5}
$$

Second derivative:
$$
\frac{d^2f}{dx^2}\bigg|_i \approx \frac{f_{i+1} - 2f_i + f_{i-1}}{\Delta x^2} + O(\Delta x^2)
\tag{8.1.7}
$$

### 8.1.2 FD for 1D Wave Equation

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

Discretized:
$$
\frac{u_i^{n+1} - 2u_i^n + u_i^{n-1}}{\Delta t^2} = c^2 \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2}
\tag{8.1.12}
$$

Explicit update:
$$
u_i^{n+1} = 2(1 - r^2)u_i^n + r^2(u_{i+1}^n + u_{i-1}^n) - u_i^{n-1}
\tag{8.1.13}
$$

where $r = c\Delta t / \Delta x$ is the Courant number.

**CFL stability condition:** $r \leq 1$

### 8.1.3 FD for 1D Diffusion Equation

$$
\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}
$$

Explicit (forward-time, central-space):
$$
u_i^{n+1} = u_i^n + \frac{\alpha \Delta t}{\Delta x^2}(u_{i+1}^n - 2u_i^n + u_{i-1}^n)
\tag{8.1.17}
$$

Stability: $\frac{\alpha \Delta t}{\Delta x^2} \leq \frac{1}{2}$

---

## 8.2 Finite Difference Time-Domain (FDTD) Method

### 8.2.1 Yee's Algorithm (1966)

Maxwell's curl equations in 3D:

$$
\frac{\partial H_x}{\partial t} = \frac{1}{\mu}\left(\frac{\partial E_y}{\partial z} - \frac{\partial E_z}{\partial y}\right)
$$
$$
\frac{\partial E_x}{\partial t} = \frac{1}{\epsilon}\left(\frac{\partial H_z}{\partial y} - \frac{\partial H_y}{\partial z} - \sigma E_x\right)
$$

Yee's leapfrog scheme positions E and H staggered in both space and time:

- **Electric field** E at integer time steps ($n$) on cell edges
- **Magnetic field** H at half-integer time steps ($n+1/2$) on cell faces

### 8.2.2 1D FDTD Update Equations

For a 1D TM wave ($E_z, H_y$ propagation along $x$):

$$
E_z^{n+1}(k) = E_z^n(k) + \frac{\Delta t}{\epsilon \Delta x}\left[H_y^{n+1/2}(k+1/2) - H_y^{n+1/2}(k-1/2)\right]
\tag{8.2.6}
$$

$$
H_y^{n+1/2}(k+1/2) = H_y^{n-1/2}(k+1/2) + \frac{\Delta t}{\mu \Delta x}\left[E_z^n(k+1) - E_z^n(k)\right]
\tag{8.2.7}
$$

### 8.2.3 2D FDTD: TM$_z$ Mode

$$
E_z^{n+1}(i,j) = E_z^n(i,j) + \frac{\Delta t}{\epsilon \Delta}\left[H_y^{n+1/2}(i+1/2,j) - H_y^{n+1/2}(i-1/2,j)\right.$$
$$\left. - H_x^{n+1/2}(i,j+1/2) + H_x^{n+1/2}(i,j-1/2)\right]
\tag{8.2.11}
$$

### 8.2.4 3D FDTD

$$
E_x^{n+1}(i,j,k) = E_x^n(i,j,k) + \frac{\Delta t}{\epsilon \Delta}\left[H_z^{n+1/2}(i,j+1/2,k) - H_z^{n+1/2}(i,j-1/2,k)\right.$$
$$\left. - H_y^{n+1/2}(i,j,k+1/2) + H_y^{n+1/2}(i,j,k-1/2)\right]
\tag{8.2.12}
$$

---

## 8.3 Numerical Dispersion and Stability

### 8.3.1 CFL Condition

For 3D FDTD with uniform cell size $\Delta$:

$$
\Delta t \leq \frac{\Delta}{c\sqrt{3}}
\tag{8.3.1}
$$

For 1D:
$$
\Delta t \leq \frac{\Delta x}{c}
\tag{8.3.2}
$$

### 8.3.2 Numerical Dispersion Relation

For 1D FDTD:
$$
\sin^2\left(\frac{\omega \Delta t}{2}\right) = r^2 \sin^2\left(\frac{k \Delta x}{2}\right)
\tag{8.3.3}
$$

Phase velocity error:
$$
\frac{v_p}{c} = \frac{\omega/k}{c} = \frac{\pi}{N_\lambda r} \cdot \frac{1}{\arcsin\left[r\sin(\pi/N_\lambda)\right]}
$$

For $N_\lambda \geq 10$ (cells per wavelength), error < 1% with $r = 0.5$.

---

## 8.4 Absorbing Boundary Conditions (ABCs)

### 8.4.1 Mur's First-Order ABC

For a wave propagating along $+x$:

$$
\left(\frac{\partial}{\partial x} + \frac{1}{c}\frac{\partial}{\partial t}\right)E_z^{\text{out}} = 0
\tag{8.4.1}
$$

Discretized at the right boundary $x = N_x \Delta x$:

$$
E_z^{n+1}(N_x) = E_z^n(N_x-1) + \frac{c\Delta t - \Delta x}{c\Delta t + \Delta x}\left[E_z^{n+1}(N_x-1) - E_z^n(N_x)\right]
\tag{8.4.5}
$$

### 8.4.2 PML (Perfectly Matched Layer)

Berenger's PML introduces a lossy anisotropic layer surrounding the computational domain where the wave is absorbed without reflection.

---

## 8.5 Source Excitation

### 8.5.1 Hard Source

$$
E_z^n(k_s) = f(n\Delta t)
$$

Simple but causes reflections from the source point.

### 8.5.2 Soft Source (Total-Field/Scattered-Field)

$$
E_z^{n+1}(k_s) = E_z^{n+1}(k_s)\big|_{\text{FDTD}} + E_z^{\text{inc}}(k_s)
$$

Allows incident wave injection without spurious reflections.

---

## 8.6 Example: 1D FDTD Simulation

**Problem:** Simulate a Gaussian pulse propagating in free space using 1D FDTD.

**Parameters:** 
- Domain: 200 cells, $\Delta x = 1$ mm
- Time step: $\Delta t = \Delta x / (2c)$ (CFL = 0.5)
- Gaussian source: $E_z(t) = \exp\left[-(t - t_0)^2 / T^2\right]$
- Mur ABC at boundaries

**Update loop (per time step):**
1. Update $H_y$ at $n+1/2$ using $E_z$ at $n$
2. Update $E_z$ at $n+1$ using $H_y$ at $n+1/2$
3. Apply ABCs at boundaries
4. Inject source
5. Record field at observation point

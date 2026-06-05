---
chapter: 15
title: "Modeling of High-Speed Digital and Analog Circuits"
book: "Computational Electrodynamics: The Finite-Difference Time-Domain Method, 3rd Ed."
authors: "A. Taflove, M. Piket-May, S. Gedney, S. O. Nelson"
raw_size: 143,812 bytes
---

# Chapter 15: Modeling of High-Speed Digital and Analog Circuits

## 15.1 Introduction

FDTD is widely used for analyzing high-speed circuits: microstrip interconnects, vias, discontinuities, and their signal integrity effects. Key capabilities: (1) broadband S-parameter extraction, (2) lumped element models, (3) nonlinear device embedding, (4) SPICE coupling.

## 15.2 Microstrip Discontinuity Modeling

### Effective Dielectric Constant
For a microstrip line width $w$, substrate thickness $h$, $\epsilon_r$:

$$
\epsilon_{\text{eff}} = \frac{\epsilon_r + 1}{2} + \frac{\epsilon_r - 1}{2} \left( 1 + \frac{12h}{w} \right)^{-1/2}
$$

Characteristic impedance:

$$
Z_0 = \frac{60}{\sqrt{\epsilon_{\text{eff}}}} \ln\left( \frac{8h}{w} + \frac{w}{4h} \right), \quad w/h \leq 1
$$

### S-Parameter Extraction
Using time-domain fields on two reference planes $z_1$, $z_2$:

$$
S_{11} = \frac{V_1^{-}(\omega)}{V_1^{+}(\omega)}, \quad S_{21} = \frac{V_2^{-}(\omega)}{V_1^{+}(\omega)}
$$

Voltage is computed as line integral of E-field from strip to ground. Current via Ampère's law around the strip.

## 15.3 Lumped Inductance and Capacitance

### Inductance from Magnetic Flux
$$
L = \frac{\Phi}{I} = \frac{\iint_S \mu \mathbf{H} \cdot d\mathbf{S}}{I}
$$

where $S$ is the surface bounded by the signal and return paths.

### Capacitance from Electric Flux
$$
C = \frac{Q}{V} = \frac{\iint_S \epsilon \mathbf{E} \cdot d\mathbf{S}}{V}
$$

### Equivalent Circuit Fitting
Fit $Z(\omega)$ or $S(\omega)$ to an equivalent circuit (RLC):

$$
Z(\omega) = R + j\omega L + \frac{1}{j\omega C}
$$

## 15.4 Discontinuity Characterization

### Microstrip Gap
Equivalent $\pi$-network: $C_{\text{series}}$, $C_{\text{shunt}}$ from FDTD field data. Gap coupling increases with decreasing gap width.

### Microstrip Bend
Mitred bend optimization: FDTD determines optimal 45° chamfer for minimum reflection ($|S_{11}| < -25$ dB).

### Microstrip Via
via inductance: $L_{\text{via}} \approx \frac{\mu_0 h}{2\pi} \ln\left( \frac{2h}{r} \right)$ for via radius $r$ through substrate thickness $h$.

## 15.5 Parallel Coplanar Microstrips

### Coupled Line Parameters
Even- and odd-mode impedances $Z_{0e}$, $Z_{0o}$ from FDTD:

$$
Z_{0e} = \sqrt{\frac{L_{11} + L_{12}}{C_{11} - C_{12}}}, \quad
Z_{0o} = \sqrt{\frac{L_{11} - L_{12}}{C_{11} + C_{12}}}
$$

### Directional Coupler
4-port S-parameters for a quarter-wave coupled section. FDTD predicts coupling level within 0.5 dB of measurements.

## 15.6 Multilayered Interconnect Modeling

For complex PCB/package structures with multiple layers:
- FDTD naturally handles layer transitions
- Signal vias, ground vias, power planes modeled directly
- Simultaneous switching noise (SSN) analysis
- Results: $S_{21}$ within 1 dB of measurements to 20 GHz

## 15.7 S-Parameter Extraction

General procedure for $N$-port waveguide structures:

1. Excite port $p$ with broadband pulse
2. Record incident/reflected waves at all ports
3. Compute $S_{qp}(\omega) = V_q^-(\omega)/V_p^+(\omega)$

For non-TEM waveguides (rectangular, circular), mode decomposition is required using field orthogonality:

$$
a_p(\omega) = \iint \mathbf{E}_{\text{total}} \times \mathbf{h}_p^* \cdot d\mathbf{S}
$$

where $\mathbf{h}_p$ is the normalized magnetic field of mode $p$.

## 15.8 Digital Signal Processing

### Prony's Method
Extract resonant frequencies and Q-factors from time-domain data:

$$
x[n] = \sum_{k=1}^K A_k e^{(\alpha_k + j\omega_k) n\Delta t}
$$

### Pencil Method (MPM)
More robust than Prony for noisy data. Constructs a matrix pencil from the time series and solves a generalized eigenvalue problem.

### Pade Approximation
Extrapolates frequency response beyond the FDTD bandwidth:

$$
S(\omega) \approx \frac{\sum_{p=0}^P a_p (j\omega)^p}{1 + \sum_{q=1}^Q b_q (j\omega)^q}
$$

## 15.9 Modeling of Lumped Circuit Elements

### 15.9.1 Extended FDTD Formulation

Lumped elements modify the Ampère law update at specific cells:

$$
\nabla \times \mathbf{H} = \epsilon \frac{\partial \mathbf{E}}{\partial t} + \sigma \mathbf{E} + \mathbf{J}_{\text{lumped}}
$$

### 15.9.2 Resistor

For a resistor $R$ at cell $(i,j,k)$:

$$
J_{\text{lumped}} = \frac{E_z}{R \cdot \Delta z}
$$

The update becomes:

$$
E_z^{n+1} = \frac{2\epsilon - \Delta t(\sigma + 1/(R\Delta z))}{2\epsilon + \Delta t(\sigma + 1/(R\Delta z))} E_z^n + \frac{2\Delta t}{2\epsilon + \Delta t(\sigma + 1/(R\Delta z))} (\nabla \times \mathbf{H})^{n+1/2}
$$

### 15.9.3 Capacitor

For a capacitor $C$:

$$
I_C = C \frac{dV}{dt} = C\Delta z \frac{dE_z}{dt}
$$

Update (using trapezoidal integration):

$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon + C\Delta z/\Delta t} (\nabla \times \mathbf{H})^{n+1/2} - \frac{C\Delta z}{\epsilon\Delta t + C\Delta z} (E_z^n - E_z^{n-1})
$$

### 15.9.4 Inductor

For inductor $L$, using the current-voltage relation $V = L dI/dt$:

$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon} (\nabla \times \mathbf{H})^{n+1/2} - \frac{\Delta t \cdot I_L}{\epsilon \Delta x \Delta y}
$$

where $I_L^{n+1/2} = I_L^{n-1/2} + \Delta t \cdot E_z^n / (L/\Delta z)$.

### 15.9.5 Diode

For a PN junction diode, the nonlinear current:

$$
I_D = I_s \left[ \exp\left( \frac{qV}{nkT} \right) - 1 \right], \quad V = E_z \cdot \Delta z
$$

Newton-Raphson iteration solves the nonlinear update at each time-step:

$$
E_z^{n+1} = E_z^n + \frac{\Delta t}{\epsilon} (\nabla \times \mathbf{H})^{n+1/2} - \frac{\Delta t}{\epsilon \Delta x \Delta y} \cdot I_D(E_z^{n+1})
$$

## 15.10 SPICE-FDTD Hybrid

For complex nonlinear circuits, the FDTD field solver is coupled to a SPICE circuit solver:

$$
I_{\text{port}}(t) = \text{SPICE}_{\text{solve}}(V_{\text{port}}(t))
$$

The SPICE model provides current as a function of voltage, while FDTD provides voltage from the field solution. Coupling at each time-step:

1. FDTD provides $V_{\text{port}}^n$
2. SPICE computes $I_{\text{port}}^{n+1/2}$
3. FDTD updates $E$-field with $J_{\text{lumped}} = I_{\text{port}} / (\Delta x \Delta y)$

## Summary

| Element | FDTD Implementation | Nonlinear | Stability Impact |
|---------|-------------------|-----------|-----------------|
| Resistor | Additive conductivity | No | Negligible |
| Capacitor | Modified permittivity | No | CFL reduced |
| Inductor | Recursive current integral | No | CFL reduced |
| Diode | Newton-Raphson | Yes | Time-step limited |
| BJT/FET | SPICE coupling | Yes | SPICE-dependent |
| Transmission line | 1D FDTD | No | CFL of 1D line |

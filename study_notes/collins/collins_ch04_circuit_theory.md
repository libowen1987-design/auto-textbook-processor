# Collins Ch4 — Circuit Theory for Waveguiding Systems

> **Source:** R. E. Collin, *Field Theory of Guided Waves*, 2nd Ed., Ch. 4, pp. 220–300.
> **Time convention:** $e^{j\omega t}$ (Collin standard)
> **Compiled from:** Collin §§4.1–4.12

---

## §4.1 Equivalent Voltages and Currents

### Motivation

For waveguides, a distributed circuit description replaces the full field solution. Equivalent voltages and currents are defined so that:

- Power flow = $\frac{1}{2} \operatorname{Re}(V I^*)$
- Transverse electric field is proportional to a **mode voltage** $V(z)$
- Transverse magnetic field is proportional to a **mode current** $I(z)$

### Definition

For a waveguide mode $n$ propagating in the $+z$ direction, write:

$$
\mathbf{E}_t(x,y,z) = V_n(z)\, \mathbf{e}_n(x,y)
$$
$$
\mathbf{H}_t(x,y,z) = I_n(z)\, \mathbf{h}_n(x,y)
$$

where $\mathbf{e}_n, \mathbf{h}_n$ are transverse vector mode functions satisfying orthonormality:

$$
\iint_S (\mathbf{e}_n \times \mathbf{h}_m^*) \cdot \hat{z}\, dS = \delta_{nm}
$$

### Complex Power

The total complex power carried by mode $n$:

$$
P = \frac{1}{2} \iint_S (\mathbf{E} \times \mathbf{H}^*) \cdot \hat{z}\, dS
  = \frac{1}{2} V_n I_n^*
$$

provided the mode functions are normalized such that:

$$
\iint_S (\mathbf{e}_n \times \mathbf{h}_n^*) \cdot \hat{z}\, dS = 1
$$

### Normalization

Following Collin's normalization convention:

- **Wave impedance:** For TE modes $Z_{\text{TE}} = \dfrac{\omega\mu}{\beta} = \dfrac{\eta}{\sqrt{1-(f_c/f)^2}}$
  For TM modes $Z_{\text{TM}} = \dfrac{\beta}{\omega\varepsilon} = \eta\sqrt{1-(f_c/f)^2}$
- **Normalized voltage/current:** $V_n = \dfrac{V}{\sqrt{Z_0}},\quad I_n = I\sqrt{Z_0}$
- This ensures that for a matched line, $V_n = I_n$ in normalized units.

### Mode Voltage and Mode Current

For each mode, the voltage and current satisfy the **telegrapher's equations**:

$$
\frac{dV(z)}{dz} = -j\beta Z_0 I(z)
$$
$$
\frac{dI(z)}{dz} = -j\frac{\beta}{Z_0} V(z)
$$

where $Z_0$ is the mode characteristic impedance and $\beta$ is the propagation constant.

For the dominant TE₁₀ mode in rectangular waveguide ($a \times b$):

$$
\lambda_c = 2a, \quad \beta = \sqrt{k^2 - (\pi/a)^2}
$$
$$
Z_{\text{TE}_{10}} = \frac{120\pi}{\sqrt{1-(\lambda/2a)^2}} \quad [\Omega]
$$

---

## §4.2 Impedance Description of Waveguide Elements

### One-Port (Single-Port) Circuits

An arbitrary waveguide discontinuity can be represented at a reference plane $T$ by an equivalent impedance $Z_{\text{in}}$:

$$
Z_{\text{in}} = \frac{V}{I} = R + jX
$$

For a lossless one-port, $R = 0$ and $Z_{\text{in}} = jX$ (pure reactance).

### Lossless One-Port Termination

A short-circuited lossless transmission line of length $l$ has:

$$
Z_{\text{in}} = j Z_0 \tan(\beta l)
$$

An open-circuited line:

$$
Z_{\text{in}} = -j Z_0 \cot(\beta l)
$$

---

## §4.3 Foster's Reactance Theorem

For a **lossless** one-port network, the reactance $X(\omega)$ satisfies:

$$
\frac{\partial X(\omega)}{\partial\omega} > 0
$$

i.e., the reactance is a monotonically increasing function of frequency.

**Consequences:**
- Poles and zeros of $X(\omega)$ interlace on the real frequency axis
- $X(\omega)$ can be synthesized as:

$$
X(\omega) = \frac{H(\omega^2 - \omega_1^2)(\omega^2 - \omega_3^2)\cdots}{(\omega^2 - \omega_2^2)(\omega^2 - \omega_4^2)\cdots}
$$

where $\omega_1 < \omega_2 < \omega_3 < \cdots$ are the resonant and anti-resonant frequencies.

Collin gives the canonical Foster form for a lossless one-port impedance:

$$
Z(s) = \frac{1}{sC_0} + sL_\infty + \sum_{k=1}^N \frac{2s/R_k}{s^2 + \omega_k^2}
$$

where $s = j\omega$, $C_0$ is the low-frequency capacitance, $L_\infty$ the high-frequency inductance, and the sum represents parallel resonant contributions.

---

## §4.4 Even and Odd Properties of $Z_{\text{in}}$

For a **real impedance function** $Z_m(s)$ (where $s = \sigma + j\omega$):

- **$Z_m(s)$ is a positive real function**
- On the imaginary axis: $Z_m(j\omega) = R(\omega) + jX(\omega)$
- $R(\omega)$ is even: $R(-\omega) = R(\omega)$
- $X(\omega)$ is odd: $X(-\omega) = -X(\omega)$
- $Z_m(s^*) = Z_m^*(s)$ (realness property)

For lossless networks:
- $Z_m(j\omega) = jX(\omega)$, purely imaginary
- $X(\omega)$ is an odd function of $\omega$

---

## §4.5 N-Port Circuits

### Impedance Matrix

An $N$-port waveguide junction is described by:

$$
\begin{bmatrix}
V_1 \\ V_2 \\ \vdots \\ V_N
\end{bmatrix}
=
\begin{bmatrix}
Z_{11} & Z_{12} & \cdots & Z_{1N} \\
Z_{21} & Z_{22} & \cdots & Z_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
Z_{N1} & Z_{N2} & \cdots & Z_{NN}
\end{bmatrix}
\begin{bmatrix}
I_1 \\ I_2 \\ \vdots \\ I_N
\end{bmatrix}
$$

or compactly $\mathbf{V} = \mathbf{Z} \mathbf{I}$.

### Symmetry

If the network is **reciprocal** (containing only linear, isotropic, passive materials):

$$
Z_{mn} = Z_{nm} \quad \text{(symmetric Z matrix)}
$$

This follows from the Lorentz reciprocity theorem applied to waveguide junctions (Collin §4.5).

### Lossless Junctions

For a **lossless** junction, the net real power entering is zero:

$$
\operatorname{Re}\!\left( \frac{1}{2} \mathbf{I}^\dagger \mathbf{Z} \mathbf{I} \right) = 0
$$

This implies that $\mathbf{Z}$ is **purely imaginary** and anti-Hermitian:

$$
\mathbf{Z} = j\mathbf{X}, \quad \mathbf{X}^T = \mathbf{X} \quad (\text{real symmetric})
$$

Equivalently: $\mathbf{Z} + \mathbf{Z}^\dagger = 0$ (anti-Hermitian).

For normalized impedance $\mathbf{z} = \mathbf{Z}/Z_0$, similar properties hold.

### Normalized Impedance/Admittance Matrices

Define normalized voltages and currents:

$$
V_n = \frac{V}{\sqrt{Z_{0n}}}, \quad I_n = I\sqrt{Z_{0n}}
$$

The normalized impedance matrix $\mathbf{z}$ relates normalized quantities:

$$
\mathbf{v} = \mathbf{z}\, \mathbf{i}
$$

where $z_{mn} = Z_{mn}\sqrt{\frac{Z_{0n}}{Z_{0m}}}$ for different reference impedances.

The normalized admittance matrix $\mathbf{y} = \mathbf{z}^{-1}$.

---

## §4.6 Two-Port Junctions

### Equivalent Two-Port Circuit

Any reciprocal two-port waveguide junction can be represented by an equivalent T- or $\pi$-network.

### T-Equivalent Circuit

For a T-network:

$$
\begin{bmatrix}
V_1 \\ V_2
\end{bmatrix}
=
\begin{bmatrix}
Z_{11} & Z_{12} \\
Z_{21} & Z_{22}
\end{bmatrix}
\begin{bmatrix}
I_1 \\ I_2
\end{bmatrix}
$$

T-network elements (Collin Fig. 4.6-1):
$$
Z_a = Z_{11} - Z_{12}, \quad Z_b = Z_{22} - Z_{12}, \quad Z_c = Z_{12}
$$

### $\pi$-Equivalent Circuit

Using admittance parameters:

$$
\begin{bmatrix}
I_1 \\ I_2
\end{bmatrix}
=
\begin{bmatrix}
Y_{11} & Y_{12} \\
Y_{21} & Y_{22}
\end{bmatrix}
\begin{bmatrix}
V_1 \\ V_2
\end{bmatrix}
$$

$\pi$-network elements:
$$
Y_a = Y_{11} + Y_{12}, \quad Y_b = Y_{22} + Y_{12}, \quad Y_c = -Y_{12}
$$

For reciprocal junctions: $Z_{12} = Z_{21}$ and $Y_{12} = Y_{21}$.

---

## §4.7 Scattering Matrix Formulation

### Definition

The scattering matrix relates **incident** and **reflected** wave amplitudes at the ports:

$$
\mathbf{b} = \mathbf{S} \, \mathbf{a}
$$

where:
- $a_n$ = incident wave amplitude at port $n$
- $b_n$ = reflected wave amplitude at port $n$

Relationships to voltage:

$$
V_n = \sqrt{Z_{0n}} (a_n + b_n)
$$
$$
I_n = \frac{1}{\sqrt{Z_{0n}}} (a_n - b_n)
$$

### S-Parameter Definition

The scattering parameter $S_{mn}$ is:

$$
S_{mn} = \left. \frac{b_m}{a_n} \right|_{a_k = 0 \text{ for } k \ne n}
$$

i.e., $S_{mn}$ = output at port $m$ when port $n$ is excited and all other ports are matched.

### Symmetry

For reciprocal networks:

$$
S_{mn} = S_{nm} \quad \text{(symmetric S matrix)}
$$

### Lossless Junctions

For a lossless junction, the S matrix is **unitary**:

$$
\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}
$$

This means:
- $\sum_{k=1}^N |S_{kn}|^2 = 1$ (power conservation for excitation at port $n$)
- $\sum_{k=1}^N S_{km}^* S_{kn} = \delta_{mn}$ (orthogonality of columns)

### Two-Port S-Matrix

For a two-port reciprocal network:

$$
\mathbf{S} = \begin{bmatrix}
S_{11} & S_{12} \\
S_{12} & S_{22}
\end{bmatrix}
$$

For a lossless two-port:

$$
|S_{11}|^2 + |S_{12}|^2 = 1
$$
$$
|S_{22}|^2 + |S_{12}|^2 = 1
$$
$$
S_{11}^* S_{12} + S_{12}^* S_{22} = 0
$$

---

## §4.8 Scattering Matrix for a Two-Port Junction (pp. 254–257)

### Basic Relations (Fig. 4.16)

$$
V_1^- = S_{11} V_1^+ + S_{12} V_2^+
$$
$$
V_2^- = S_{21} V_1^+ + S_{22} V_2^+
\tag{4.64}
$$

- $S_{11}$: input reflection coefficient (port 2 matched, $V_2^+ = 0$)
- $S_{21}$: forward transmission coefficient
- $S_{22}$: output reflection coefficient (port 1 matched)
- $S_{12}$: reverse transmission coefficient

### Effect of Output Load Mismatch

If port 2 has load reflection $\Gamma_L = (Z_L-1)/(Z_L+1)$, the effective input reflection:

$$
S_{11}' = S_{11} + \frac{S_{12} S_{21} \Gamma_L}{1 - S_{22} \Gamma_L}
\tag{4.66}
$$

### Lossless Reciprocal Two-Port

From the unitary condition:

1. **Equal reflection magnitudes**: $|S_{11}| = |S_{22}|$ \hfill (4.68)
2. **Power conservation**: $|S_{12}| = \sqrt{1 - |S_{11}|^2}$ \hfill (4.69)
3. **Phase condition** ($S_{11} = |S_{11}|e^{-j\theta_1}$, $S_{22} = |S_{11}|e^{j\theta_2}$, $S_{12} = |S_{12}|e^{j\theta_0}$):
   $$
   \theta_1 + \theta_2 = 2\theta_0 - \pi \pm 2n\pi
   \tag{4.70}
   $$

Thus a lossless reciprocal two-port is fully described by **three parameters** ($|S_{11}|$, $\theta_1$, $\theta_2$).

### Example: Shunt Susceptance (Fig. 4.17a)

A shunt $jB$ across a line with characteristic admittance $Y_c$:

$$
S_{11} = S_{22} = \frac{-jB}{2Y_c + jB}, \quad
S_{21} = S_{12} = \frac{2Y_c}{2Y_c + jB}
\tag{4.71}
$$

### Example: Series Reactance (Fig. 4.17b)

A series $jX$ between lines with $Z_1$, $Z_2$:

$$
S_{11} = \frac{Z_2 - Z_1 - jX}{Z_1 + Z_2 + jX}, \quad
S_{22} = \frac{Z_1 - Z_2 - jX}{Z_1 + Z_2 + jX}
\tag{4.72a}
$$
$$
S_{21} = S_{12} = \frac{2\sqrt{Z_1 Z_2}}{Z_1 + Z_2 + jX}
\tag{4.72b}
$$

### Key Points

- $S$-parameters are the most practical directly measurable quantities at microwave frequencies
- A lossless reciprocal two-port needs only one reflection and one transmission measurement
- $|S_{21}|^2$ is the power transmission coefficient; $|S_{11}|^2$ is the power reflection
- Unitary property $\Rightarrow$ sum of reflected and transmitted powers equals incident power

---

## §4.9 Transmission-Matrix Representation

### Voltage-Current Transmission Matrix (ABCD)

For a two-port, the ABCD matrix relates input to output:

$$
\begin{bmatrix}
V_1 \\ I_1
\end{bmatrix}
=
\begin{bmatrix}
A & B \\
C & D
\end{bmatrix}
\begin{bmatrix}
V_2 \\ -I_2
\end{bmatrix}
$$

Note: $I_2$ direction is defined **out** of the second port.

Properties:
- For reciprocal networks: $AD - BC = 1$
- For symmetric networks: $A = D$
- For lossless networks: $A$ and $D$ are real, $B$ and $C$ are imaginary

**Cascade connection:** If network A ($\mathbf{T}_A$) is followed by network B ($\mathbf{T}_B$), the overall ABCD matrix is:

$$
\mathbf{T} = \mathbf{T}_A \cdot \mathbf{T}_B
$$

### Wave Amplitude Transmission Matrix ($T$-Matrix)

The $T$-matrix relates incident and reflected waves at port 1 to those at port 2:

$$
\begin{bmatrix}
b_1 \\ a_1
\end{bmatrix}
=
\begin{bmatrix}
T_{11} & T_{12} \\
T_{21} & T_{22}
\end{bmatrix}
\begin{bmatrix}
a_2 \\ b_2
\end{bmatrix}
$$

For cascade of networks: $\mathbf{T}_{\text{total}} = \mathbf{T}_A \cdot \mathbf{T}_B$

The $T$-matrix is especially useful for cascaded waveguide junctions (Collin §4.8).

### Conversion Between S and T

From Collin:

$$
\begin{aligned}
T_{11} &= 1/S_{21} \\
T_{12} &= -S_{22}/S_{21} \\
T_{21} &= S_{11}/S_{21} \\
T_{22} &= (S_{12}S_{21} - S_{11}S_{22})/S_{21}
\end{aligned}
$$

---

## §4.10 Signal Flow Graphs (Mason's Gain Formula)

### Motivation

Signal flow graphs (SFG) provide a graphical method for analyzing microwave networks, particularly useful for cascaded and feedback configurations.

### Mason's Rule

The transfer function $T$ from a source node to a sink node:

$$
T = \frac{\sum_k P_k \Delta_k}{\Delta}
$$

where:
- $\Delta = 1 - \sum L_1 + \sum L_2 - \sum L_3 + \cdots$
- $L_1$ = sum of all first-order loop gains
- $L_2$ = sum of products of two non-touching loop gains
- $L_3$ = sum of products of three non-touching loop gains
- $P_k$ = gain of the $k$-th forward path
- $\Delta_k$ = value of $\Delta$ with loops touching path $k$ removed

### Rules for SFG Construction

1. Nodes represent variables ($a_n$, $b_n$, $V_n$, $I_n$)
2. Branches represent S-parameters or transmission coefficients
3. Signal flows in direction of arrow
4. Node value = sum of signals entering it

### Two-Port Example

For a two-port with generator $a_1$ and load $\Gamma_L$:

Forward paths:
- $P_1 = S_{21}$ (direct: a₁ → b₂)

Loops:
- $L_1 = S_{11}\Gamma_S$ (source mismatch)
- $L_2 = S_{22}\Gamma_L$ (load mismatch)
- $L_3 = S_{12}S_{21}\Gamma_S\Gamma_L$ (through loop)

Using Mason's rule:

$$
\frac{b_2}{a_1} = \frac{S_{21}}{1 - S_{11}\Gamma_S - S_{22}\Gamma_L + S_{11}S_{22}\Gamma_S\Gamma_L - S_{12}S_{21}\Gamma_S\Gamma_L}
$$

---

## §4.11 Generalized Scattering Matrix for Power Waves

### Power Waves

For transmission lines with different real characteristic impedances, the conventional S-matrix definition using voltage waves is inconvenient. Collin introduces **power waves**.

For a port with impedance $Z_0$ (real):

$$
a = \frac{V + Z_0 I}{2\sqrt{Z_0}}, \quad
b = \frac{V - Z_0 I}{2\sqrt{Z_0}}
$$

These are normalized so that $|a|^2$ = incident power and $|b|^2$ = reflected power.

### Generalized S-Matrix

The generalized S-matrix is defined as:

$$
\mathbf{b} = \mathbf{S}_g \, \mathbf{a}
$$

where power waves are used instead of voltage waves. This formulation:

1. Allows ports with different reference impedances
2. Preserves unitary property for lossless junctions
3. $S_{g,mn} = \frac{b_m}{a_n}\Big|_{a_k=0, k\neq n}$

### Properties

- For lossless: $\mathbf{S}_g^\dagger \mathbf{S}_g = \mathbf{I}$ (unitary)
- For reciprocal: $\mathbf{S}_g^T = \mathbf{S}_g$ (symmetric)
- Related to conventional S via transformer relations

### Conversion from Conventional to Power-Wave S

If port reference impedances change from $Z_{0n}$ to $Z'_{0n}$, the generalized S-matrix transforms. For a single port with impedance change from $Z_0$ to $Z_0'$:

$$
\Gamma' = \frac{\Gamma - \Gamma_0}{1 - \Gamma\Gamma_0^*}
$$

where $\Gamma_0 = (Z_0' - Z_0)/(Z_0' + Z_0)$ (Collin §4.10, Eq. 4.116).

---

## §4.12 Excitation of Waveguides

### Probe Coupling (Rectangular Waveguide)

A small probe (monopole antenna) inserted into a rectangular waveguide excites the dominant TE₁₀ mode. The equivalent circuit is a voltage generator in series with the probe impedance.

**Probe impedance** (Collin, Fig. 4.11-1):

$$
Z_p = R_p + jX_p
$$

where radiation resistance $R_p$ depends on probe position and length.

For a probe at $(x_0, y_0)$ in a rectangular waveguide ($a \times b$):

$$
R_p \propto \sin^2\!\left(\frac{\pi x_0}{a}\right) \cdot (\text{probe length factor})
$$

### Radiation from a Current Element (Electric Dipole)

A short electric dipole (current element) inside a waveguide excites multiple modes. The amplitude of the $n$th mode is proportional to the projection of the dipole moment onto the modal field.

For a current element $\mathbf{J} = \hat{x} I_0 l \, \delta(x-x_0)\delta(y-y_0)\delta(z)$ in a rectangular waveguide, the TE₁₀ mode amplitude is (Collin §4.11):

$$
a_{10} \propto I_0 l \, \sin\!\left(\frac{\pi x_0}{a}\right)
$$

### Radiation from a Current Loop (Magnetic Dipole)

A small current loop (magnetic dipole) inside a waveguide couples primarily to the magnetic field of the mode. A loop in the $x$-$y$ plane (area $A$, current $I$) excites:

Mode amplitude proportional to loop's magnetic moment $\mathbf{m} = I A \, \hat{n}$.

For a loop in the transverse plane ($xy$-plane), coupling is proportional to the modal $H_z$ component (for TE modes). A loop oriented to couple to $H_y$ of the TE₁₀ mode (loop in $xz$-plane):

$$
a_{10} \propto I A \, \sin\!\left(\frac{\pi x_0}{a}\right)
$$

---

## §4.13 Waveguide Coupling by Apertures

### Transverse Wall Aperture (Iris in Transverse Plane)

A small aperture in a transverse wall (iris) between two waveguide sections acts as a shunt reactance.

For a **capacitive iris** (narrow slot parallel to E-field in rectangular waveguide, $a \times b$ at TE₁₀):

$$
\frac{B}{Y_0} = -\frac{4b}{\lambda_g} \ln\!\left[ \csc\!\left(\frac{\pi w}{2b}\right) \right]
$$

where $w$ is the gap width and $\lambda_g$ is the guide wavelength (Collin, Eq. 4.169).

For an **inductive iris** (narrow slot transverse to E-field):

$$
\frac{X}{Z_0} = \frac{a}{\lambda_g} \tan^2\!\left(\frac{\pi d}{2a}\right) \left[ 1 + \frac{1}{2}\left(\frac{\lambda_g}{a}\right)^2 \sin^2\!\left(\frac{\pi d}{2a}\right) \ln\!\csc\!\left(\frac{\pi d}{2a}\right) \right]^{-1}
$$

where $d$ is the aperture width (Collin, Eq. 4.177).

### Broad Wall Aperture

A small hole in the broad wall of a rectangular waveguide radiates into free space or couples to an adjacent waveguide.

**Bethe's Small-Hole Theory** (Collin §4.12): A small aperture can be represented by equivalent electric and magnetic dipole moments:

$$
\mathbf{p} = \varepsilon_0 \alpha_e \hat{n}(\hat{n} \cdot \mathbf{E})
$$
$$
\mathbf{m} = -\alpha_m \mathbf{H}_t + \alpha_{m,n} (\hat{n} \cdot \mathbf{H}) \hat{n}
$$

where $\alpha_e$, $\alpha_m$ are the electric and magnetic polarizabilities of the aperture.

For a **circular aperture** of radius $r_0$:

$$
\alpha_e = \frac{2r_0^3}{3}, \quad \alpha_m = \frac{4r_0^3}{3}
$$

For a **rectangular slot** of length $l$ and width $w$ ($l \gg w$):

$$
\alpha_e = \frac{\pi w^2 l}{16}, \quad \alpha_m = \frac{\pi l^3}{24\ln(2l/w) - \cdots}
$$

### Coupling Coefficient

The coupling between waveguides through an aperture is proportional to (Collin Eq. 4.192):

$$
C \propto \left| \alpha_e (\hat{n} \cdot \mathbf{E}_1)(\hat{n} \cdot \mathbf{E}_2) - \mu_0 \alpha_m (\mathbf{H}_{t1} \cdot \mathbf{H}_{t2}) - \mu_0 \alpha_{m,n} H_{n1} H_{n2} \right|^2
$$

where subscripts 1 and 2 refer to fields on either side of the aperture.

---

## Key Equations Summary

| Quantity | Formula | Section |
|----------|---------|---------|
| TE wave impedance | $Z_{\text{TE}} = \eta/\sqrt{1-(f_c/f)^2}$ | §4.1 |
| TM wave impedance | $Z_{\text{TM}} = \eta\sqrt{1-(f_c/f)^2}$ | §4.1 |
| Foster's theorem | $\partial X/\partial\omega > 0$ | §4.3 |
| Lossless Z matrix | $\mathbf{Z} + \mathbf{Z}^\dagger = 0$ | §4.5 |
| Unitary S matrix | $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ | §4.7 |
| Reciprocity | $S_{mn} = S_{nm}$ | §4.7 |
| ABCD determinant | $AD - BC = 1$ (reciprocal) | §4.8 |
| Mason's rule | $T = \sum P_k \Delta_k / \Delta$ | §4.9 |
| Power wave | $a = (V + Z_0 I)/(2\sqrt{Z_0})$ | §4.10 |
| Aperture polarizability | $\alpha_e = 2r_0^3/3$ (circular) | §4.12 |

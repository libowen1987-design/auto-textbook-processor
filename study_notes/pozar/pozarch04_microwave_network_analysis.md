# Pozar Chapter 4 — Microwave Network Analysis

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 186–249.
> Covers impedance/admittance matrices, scattering parameters, ABCD matrix, signal flow graphs, T-parameters, and generalized scattering parameters. All derivations start from the fundamental definitions and build to engineering design applications.

---

## 4.1 Impedance and Admittance Matrices

### 4.1.1 Network Port Representation

A microwave network is characterized by its **ports** — points where energy enters or leaves the network. Each port is associated with a terminal pair carrying a total voltage $V_n$ and total current $I_n$.

For an $N$-port network, the **impedance matrix** $\mathbf{Z}$ relates the port voltages to the port currents:

$$
\boxed{\mathbf{V} = \mathbf{Z} \mathbf{I}}
$$

$$
\begin{bmatrix} V_1 \\ V_2 \\ \vdots \\ V_N \end{bmatrix} =
\begin{bmatrix}
Z_{11} & Z_{12} & \cdots & Z_{1N} \\
Z_{21} & Z_{22} & \cdots & Z_{2N} \\
\vdots & \vdots & \ddots & \vdots \\
Z_{N1} & Z_{N2} & \cdots & Z_{NN}
\end{bmatrix}
\begin{bmatrix} I_1 \\ I_2 \\ \vdots \\ I_N \end{bmatrix}
$$

**Physical interpretation**:

$$
Z_{ij} = \frac{V_i}{I_j} \Big|_{I_k = 0 \text{ for } k \neq j}
$$

$Z_{ii}$ is the **input impedance** at port $i$ when all other ports are open-circuited. $Z_{ij}$ ($i \neq j$) is the **transfer impedance** — voltage at port $i$ due to current at port $j$.

### 4.1.2 Admittance Matrix

The **admittance matrix** $\mathbf{Y}$ is the inverse of $\mathbf{Z}$:

$$
\boxed{\mathbf{I} = \mathbf{Y} \mathbf{V}}
$$

$$
Y_{ij} = \frac{I_i}{V_j} \Big|_{V_k = 0 \text{ for } k \neq j}
$$

$Y_{ii}$ is the **input admittance** at port $i$ with all other ports short-circuited. $Y_{ij}$ is the **transfer admittance**.

Since $\mathbf{Y} = \mathbf{Z}^{-1}$, for a lossless network the admittance matrix is purely imaginary (same as $\mathbf{Z}$).

### 4.1.3 Properties of Z and Y Matrices

| Property | Condition | Mathematical Statement |
|----------|-----------|----------------------|
| **Reciprocal** (passive, no anisotropic media) | $\mathbf{Z} = \mathbf{Z}^T$, $\mathbf{Y} = \mathbf{Y}^T$ | $Z_{ij} = Z_{ji}$ |
| **Lossless** | $\text{Re}(Z_{ij}) = 0 \ \forall i,j$ | All $Z_{ij}$ purely imaginary |
| **Lossless, reciprocal** | $Z_{ij}$ imaginary, $Z_{ij} = Z_{ji}$ | $\mathbf{Z} = j\mathbf{X}$ with $\mathbf{X} = \mathbf{X}^T$ |

For a lossless network, the net real power entering the network must be zero:

$$
P = \frac{1}{2} \text{Re}(\mathbf{V}^\dagger \mathbf{I}) = \frac{1}{2} \text{Re}(\mathbf{I}^\dagger \mathbf{Z}^\dagger \mathbf{I}) = 0
$$

This requires $\mathbf{Z}^\dagger = -\mathbf{Z}$ (skew-Hermitian), which for reciprocal networks reduces to $\text{Re}(Z_{ij}) = 0$.

### 4.1.4 Example: Two-Port Z and Y Parameters

For a two-port network:

$$
V_1 = Z_{11} I_1 + Z_{12} I_2
$$
$$
V_2 = Z_{21} I_1 + Z_{22} I_2
$$

$$
I_1 = Y_{11} V_1 + Y_{12} V_2
$$
$$
I_2 = Y_{21} V_1 + Y_{22} V_2
$$

For reciprocal networks: $Z_{12} = Z_{21}$, $Y_{12} = Y_{21}$.

From the definition of the Z matrix elements:

- $Z_{11} = V_1 / I_1$ with $I_2 = 0$ (open-circuited port 2)
- $Z_{21} = V_2 / I_1$ with $I_2 = 0$
- $Z_{22} = V_2 / I_2$ with $I_1 = 0$
- $Z_{12} = V_1 / I_2$ with $I_1 = 0$

---

## 4.2 The Scattering Matrix (S-Parameters)

### 4.2.1 Why S-Parameters?

At microwave frequencies, $\mathbf{Z}$ and $\mathbf{Y}$ matrices are impractical because:
- Open and short circuits are difficult to realize over a broad bandwidth due to parasitic effects
- Active circuits may oscillate under open/short conditions
- S-parameters are measured directly with a Vector Network Analyzer (VNA)

**S-parameters** relate the **incident** and **reflected** voltage waves at each port:

$$
\boxed{\mathbf{V}^- = \mathbf{S} \mathbf{V}^+}
$$

where $V_n^+$ is the incident voltage wave at port $n$, and $V_n^-$ is the reflected voltage wave at port $n$.

### 4.2.2 Definition of S-Parameters

For an $N$-port network, with each port having a characteristic impedance $Z_{0n}$:

$$
V_n^- = \sum_{j=1}^N S_{nj} V_j^+
$$

$$
S_{ij} = \frac{V_i^-}{V_j^+} \Big|_{V_k^+ = 0 \text{ for } k \neq j}
$$

**Physical interpretation**:

- $S_{ii}$: **Input reflection coefficient** at port $i$ when all other ports are matched (terminated in $Z_0$)
- $S_{ij}$ ($i \neq j$): **Transmission coefficient** from port $j$ to port $i$

For the common **two-port network**:

$$
\begin{bmatrix} V_1^- \\ V_2^- \end{bmatrix} =
\begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix}
\begin{bmatrix} V_1^+ \\ V_2^+ \end{bmatrix}
$$

- $S_{11}$: Input return loss / reflection coefficient at port 1 (port 2 matched)
- $S_{21}$: Forward gain/transmission (port 2 matched)
- $S_{12}$: Reverse isolation (port 1 matched)
- $S_{22}$: Output return loss / reflection coefficient at port 2 (port 1 matched)

### 4.2.3 Relating S-Parameters to Voltages and Currents

The total voltage and current at port $n$ are:

$$
V_n = V_n^+ + V_n^-
$$
$$
I_n = \frac{V_n^+ - V_n^-}{Z_{0n}}
$$

For a uniform convention with reference impedance $Z_0$ at all ports:

$$
V_1 = V_1^+ + V_1^-, \quad I_1 = \frac{V_1^+ - V_1^-}{Z_0}
$$

From these relationships, the reflection coefficient looking into port $n$ with all other ports matched:

$$
\Gamma_n = \frac{V_n^-}{V_n^+} = S_{nn}
$$

And the input impedance at port $n$:

$$
Z_{\text{in},n} = Z_{0n} \frac{1 + \Gamma_n}{1 - \Gamma_n} = Z_{0n} \frac{1 + S_{nn}}{1 - S_{nn}}
$$

### 4.2.4 Power Waves

The **incident power** at port $n$ is:

$$
P_n^+ = \frac{1}{2} |V_n^+|^2 / Z_{0n}
$$

The **reflected power**:

$$
P_n^- = \frac{1}{2} |V_n^-|^2 / Z_{0n}
$$

The **net power** delivered to the network:

$$
P_n = P_n^+ - P_n^- = \frac{1}{2Z_{0n}} \left( |V_n^+|^2 - |V_n^-|^2 \right)
$$

Total net power entering an $N$-port network:

$$
P_{\text{net}} = \frac{1}{2} \sum_{n=1}^N \frac{|V_n^+|^2 - |V_n^-|^2}{Z_{0n}}
$$

### 4.2.5 Properties of S-Parameters

#### Reciprocal Networks

For a reciprocal network (passive, containing only isotropic materials):

$$
\boxed{S_{ij} = S_{ji}} \quad \text{or} \quad \mathbf{S} = \mathbf{S}^T
$$

Proof follows from the Lorentz reciprocity theorem.

#### Lossless Networks

For a lossless network, the total incident power equals the total reflected power:

$$
\sum_{n=1}^N |V_n^+|^2 = \sum_{n=1}^N |V_n^-|^2
$$

In matrix form, this requires the scattering matrix to be **unitary**:

$$
\boxed{\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}}
$$

where $\mathbf{S}^\dagger = (\mathbf{S}^*)^T$ is the conjugate transpose.

**Implications of unitarity**:
- For any column $j$: $\displaystyle \sum_{i=1}^N |S_{ij}|^2 = 1$ (power conservation — all incident power at port $j$ is either reflected or transmitted to other ports)
- For $i \neq j$: $\displaystyle \sum_{k=1}^N S_{ki}^* S_{kj} = 0$ (orthogonality of columns)

#### Symmetrical Networks

Symmetry imposes additional constraints. For a two-port network with **mirror symmetry**:

- If the network is symmetric about a plane: $S_{11} = S_{22}$ (same input and output match)
- For a physically symmetric reciprocal network: $S_{11} = S_{22}$, $S_{12} = S_{21}$

### 4.2.6 Summary: Reciprocal, Lossless Two-Port Network Constraints

For a reciprocal, lossless two-port network:

1. Reciprocity: $S_{12} = S_{21}$
2. Unitarity:
   - $|S_{11}|^2 + |S_{12}|^2 = 1$
   - $|S_{12}|^2 + |S_{22}|^2 = 1$
   - $S_{11}^* S_{12} + S_{12}^* S_{22} = 0$

From these constraints, we deduce:
- $|S_{11}| = |S_{22}|$ (equal input/output return loss magnitudes)
- $S_{12} = S_{21} = \sqrt{1 - |S_{11}|^2} \, e^{j\theta}$

The phase relationship imposes:

$$
S_{11} = -\frac{S_{12}}{S_{12}^*} S_{22}^*
$$

For a reciprocal, lossless two-port, the S-parameters have only **three degrees of freedom**: magnitudes $|S_{11}|$ (or $|S_{12}|$), and two phases.

### 4.2.7 Example: Transmission Line Section

Consider a transmission line of length $l$ and characteristic impedance $Z_0$, terminated in $Z_0$ at both ports (the ports are the two ends of the line). 

For a matched line:

$$
S_{11} = 0, \quad S_{22} = 0
$$
$$
S_{12} = S_{21} = e^{-j\beta l}
$$

The phase shift is simply the electrical length of the transmission line.

If the line has characteristic impedance $Z_{01} \neq Z_0$ (the reference impedance), then there will be reflections at the junctions:

$$
S_{11} = \frac{Z_{01} - Z_0}{Z_{01} + Z_0} = \Gamma
$$
$$
S_{22} = \frac{Z_{01} - Z_0}{Z_{01} + Z_0} = \Gamma \quad \text{(symmetry)}
$$
$$
S_{12} = S_{21} = \frac{(1 - \Gamma^2) e^{-j\beta l}}{1 - \Gamma^2 e^{-j2\beta l}}
$$

---

## 4.3 ABCD Matrix (Transmission Matrix)

### 4.3.1 Definition

The ABCD matrix (also called the **chain matrix** or **transmission matrix**) relates the voltage and current at port 1 to those at port 2:

$$
\boxed{\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix}}
$$

**Sign convention**: $I_2$ flows **out of** port 2 (into the load). This convention allows cascading.

### 4.3.2 Physical Interpretation

- $A = \dfrac{V_1}{V_2} \Big|_{I_2 = 0}$: Reciprocal of voltage gain with output open-circuited (dimensionless)
- $B = \dfrac{V_1}{I_2} \Big|_{V_2 = 0}$: Transfer impedance with output short-circuited ($\Omega$)
- $C = \dfrac{I_1}{V_2} \Big|_{I_2 = 0}$: Transfer admittance with output open-circuited (S)
- $D = \dfrac{I_1}{I_2} \Big|_{V_2 = 0}$: Reciprocal of current gain with output short-circuited (dimensionless)

### 4.3.3 ABCD Matrices of Common Networks

| Network | ABCD Matrix | Notes |
|---------|-------------|-------|
| Series impedance $Z$ | $\begin{bmatrix} 1 & Z \\ 0 & 1 \end{bmatrix}$ | |
| Shunt admittance $Y$ | $\begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}$ | |
| Transmission line (length $l$, char. imp. $Z_0$, prop. const. $\beta$) | $\begin{bmatrix} \cos(\beta l) & jZ_0 \sin(\beta l) \\ jY_0 \sin(\beta l) & \cos(\beta l) \end{bmatrix}$ | Lossless |
| Transmission line (lossy) | $\begin{bmatrix} \cosh(\gamma l) & Z_0 \sinh(\gamma l) \\ Y_0 \sinh(\gamma l) & \cosh(\gamma l) \end{bmatrix}$ | $\gamma = \alpha + j\beta$ |
| Ideal transformer (ratio $n:1$) | $\begin{bmatrix} n & 0 \\ 0 & 1/n \end{bmatrix}$ | |
| Open circuit | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ | No transmission |
| $\pi$-network (series $Z$, shunt $Y_1, Y_2$) | $\begin{bmatrix} 1+Z Y_2 & Z \\ Y_1+Y_2+Z Y_1 Y_2 & 1+Z Y_1 \end{bmatrix}$ | |
| T-network ($Z_1, Z_2, Z_3$) | $\begin{bmatrix} 1+Z_1/Z_3 & Z_1+Z_2+Z_1 Z_2/Z_3 \\ 1/Z_3 & 1+Z_2/Z_3 \end{bmatrix}$ | $Z_3$ is the shunt arm |

### 4.3.4 Properties of ABCD Matrices

- **Reciprocal network**: $\boxed{AD - BC = 1}$ (determinant = 1)
- **Symmetric network**: $A = D$
- **Lossless network**: $A$ and $D$ are real, $B$ and $C$ are imaginary
- **Cascade connection**: For two networks in cascade:
  $$
  \boxed{\mathbf{ABCD}_{\text{total}} = \mathbf{ABCD}_1 \cdot \mathbf{ABCD}_2}
  $$

The cascade property is the key advantage of the ABCD representation — it avoids the matrix conversions needed when cascading S-parameter subnetworks.

### 4.3.5 Example: Cascade of Two Transmission Lines

Two lines of lengths $l_1, l_2$, both with $Z_0, \beta$:

$$
\mathbf{ABCD} = \mathbf{ABCD}_1 \cdot \mathbf{ABCD}_2
$$

$$
= \begin{bmatrix} \cos(\beta l_1) & jZ_0 \sin(\beta l_1) \\ jY_0 \sin(\beta l_1) & \cos(\beta l_1) \end{bmatrix}
\begin{bmatrix} \cos(\beta l_2) & jZ_0 \sin(\beta l_2) \\ jY_0 \sin(\beta l_2) & \cos(\beta l_2) \end{bmatrix}
$$

Result:

$$
A = \cos(\beta l_1)\cos(\beta l_2) - \sin(\beta l_1)\sin(\beta l_2) = \cos(\beta[l_1+l_2])
$$
$$
B = jZ_0[\cos(\beta l_1)\sin(\beta l_2) + \sin(\beta l_1)\cos(\beta l_2)] = jZ_0\sin(\beta[l_1+l_2])
$$
$$
C = jY_0\sin(\beta[l_1+l_2])
$$
$$
D = \cos(\beta[l_1+l_2])
$$

This confirms that the cascade of two matched lines acts as a single longer line.

---

## 4.4 Signal Flow Graphs and Mason's Gain Formula

### 4.4.1 Introduction

Signal flow graphs provide a graphical method for analyzing microwave networks by representing S-parameter relationships as directed paths. They are especially useful for:
- Analyzing complex networks with multiple reflections
- Computing transfer functions and reflection coefficients
- Understanding feedback in active microwave circuits

### 4.4.2 Graph Elements

- **Nodes**: Represent variables ($V_n^+$, $V_n^-$, sources)
- **Branches**: Directed edges with gain $S_{ij}$, representing the wave amplitude transfer

**Rules**:
1. A node equals the sum of all incoming signals multiplied by their branch gains
2. A node value is transmitted along all outgoing branches

### 4.4.3 Basic Two-Port Signal Flow Graph

```
     ┌─────────────────────────────────┐
     │            S21                  │
     │   ┌───────────────────────┐     │
     │   │                       ▼     │
     V1⁺ ● ──►● V1⁻     V2⁺ ● ──►● V2⁻
     │         ▲               │       │
     │         │ S11           │ S22   │
     │         └───────── ─────┘       │
     └─◄─────── ─── ───────────────────┘
                  S12
```

### 4.4.4 Mason's Gain Formula

The **transfer function** between any two nodes in a signal flow graph is:

$$
\boxed{T = \frac{\sum_k T_k \Delta_k}{\Delta}}
$$

where:
- $T_k$: Gain of the $k$-th forward path
- $\Delta = 1 - \sum L_1 + \sum L_2 - \sum L_3 + \cdots$: Determinant of the graph
- $L_1$: Sum of all first-order loop gains (single closed loops)
- $L_2$: Sum of products of gains of two non-touching loops
- $L_3$: Sum of products of gains of three non-touching loops
- $\Delta_k$: $\Delta$ evaluated with loops touching the $k$-th forward path removed

**Definitions**:
- **Loop**: A closed path that starts and ends at the same node, with no node visited more than once
- **Non-touching loops**: Loops that share no common nodes
- **Forward path**: A path from the source node to the sink node, traversing branches in the direction of the arrows, with no node visited more than once

### 4.4.5 Example: Two-Port with Mismatched Source and Load

Consider a two-port network described by S-parameters $S_{11}, S_{12}, S_{21}, S_{22}$, connected to a source with reflection coefficient $\Gamma_S$ and a load with $\Gamma_L$.

**Loops in the signal flow graph**:

1. $L_1 = S_{11} \Gamma_S$
2. $L_2 = S_{22} \Gamma_L$
3. $L_3 = S_{21} \Gamma_L S_{12} \Gamma_S$ (through the network and back)

$L_1$ and $L_2$ are non-touching (they involve different nodes), so:

$$
\sum L_1 = S_{11} \Gamma_S + S_{22} \Gamma_L + S_{21} S_{12} \Gamma_L \Gamma_S
$$
$$
\sum L_2 = S_{11} \Gamma_S \cdot S_{22} \Gamma_L
$$

Thus:

$$
\Delta = 1 - (S_{11} \Gamma_S + S_{22} \Gamma_L + S_{21} S_{12} \Gamma_L \Gamma_S) + S_{11} S_{22} \Gamma_S \Gamma_L
$$

**Forward path from source to output**:

$T_1 = S_{21}$ (direct path), $\Delta_1 = 1 - S_{22} \Gamma_L$ (remove loops touching this path: $L_2$ touches, remove it; $L_1$ and $L_3$ don't touch the path)

Wait — let's be more careful. The forward path from the source to the output goes through:
$V_S \to a_1 \to b_2 \to V_{\text{out}}$

Actually, the structure is:
1. Source node $V_S$ connects to $a_1 = V_1^+$ through a branch.
2. $a_1$ goes to $b_1 = V_1^-$ via $S_{11}$ and to $b_2 = V_2^-$ via $S_{21}$.
3. $b_1$ sees $\Gamma_S$ (reflected back to $a_1$).
4. $b_2$ sees $\Gamma_L$ (reflected back to $a_2 = V_2^+$).
5. $a_2$ goes to $b_1$ via $S_{12}$ and to $b_2$ via $S_{22}$.

(This is the standard "feedback loop" structure through the two-port.)

**Forward path from $V_S$ to $b_2$**: $T_1 = 1 \cdot S_{21}$ (assuming $V_S$ normalized to $a_1$)

Loops:
- $L_a = S_{11} \Gamma_S$
- $L_b = S_{22} \Gamma_L$
- $L_c = S_{21} \Gamma_L S_{12} \Gamma_S$

$\Delta = 1 - (L_a + L_b + L_c) + L_a L_b$ (since $L_a$ and $L_b$ are non-touching)

$\Delta_1$: Remove loops touching forward path — $L_a$ and $L_c$ touch (involve $a_1$), $L_b$ also touches (involves $b_2$). So $\Delta_1 = 1$.

Wait — let me reconsider which nodes the forward path visits. The forward path from $V_S$ to $b_2$ goes through:
$V_S \to a_1 \to b_2$

This path touches nodes $V_S, a_1, b_2$.

Loop $L_a = S_{11} \Gamma_S$ goes through $a_1 \to b_1 \to a_1$. It touches $a_1$. So it touches the forward path.
Loop $L_b = S_{22} \Gamma_L$ goes through $b_2 \to a_2 \to b_2$. It touches $b_2$. So it touches the forward path.
Loop $L_c = S_{21} \Gamma_L S_{12} \Gamma_S$ goes through $a_1 \to b_2 \to a_2 \to b_1 \to a_1$. It touches both $a_1$ and $b_2$. So it also touches.

Therefore $\Delta_1 = 1$.

The overall gain from source to $b_2$:

$$
\frac{b_2}{V_S} = \frac{S_{21}}{1 - (S_{11}\Gamma_S + S_{22}\Gamma_L + S_{21}S_{12}\Gamma_L\Gamma_S) + S_{11}S_{22}\Gamma_S\Gamma_L}
$$

This can be rewritten as:

$$
\frac{b_2}{V_S} = \frac{S_{21}}{(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L) - S_{21}S_{12}\Gamma_L\Gamma_S}
$$

### 4.4.6 Common Transfer Functions via Signal Flow

**Input reflection coefficient** ($\Gamma_{\text{in}}$):

$$
\boxed{\Gamma_{\text{in}} = \frac{b_1}{a_1} = S_{11} + \frac{S_{12} S_{21} \Gamma_L}{1 - S_{22} \Gamma_L}}
$$

**Output reflection coefficient** ($\Gamma_{\text{out}}$):

$$
\boxed{\Gamma_{\text{out}} = \frac{b_2}{a_2} = S_{22} + \frac{S_{12} S_{21} \Gamma_S}{1 - S_{11} \Gamma_S}}
$$

**Transducer power gain** ($G_T$):

$$
\boxed{G_T = \frac{|S_{21}|^2 (1 - |\Gamma_S|^2)(1 - |\Gamma_L|^2)}{|(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L) - S_{12}S_{21}\Gamma_S\Gamma_L|^2}}
$$

**Voltages** for the forward path where we track $V_2^-$ (the wave emerging from the two-port toward the load):

$$
\frac{V_2^-}{V_S} = \frac{S_{21}(1 + \Gamma_L)}{(1 - S_{11}\Gamma_S)(1 - S_{22}\Gamma_L) - S_{12}S_{21}\Gamma_S\Gamma_L}
$$

---

## 4.5 T-Parameters (Scattering Transfer Parameters)

### 4.5.1 Definition

The **T-matrix** (or **scattering transfer matrix**) relates the incident and reflected waves at port 1 to those at port 2, making it convenient for cascading networks (similar to how ABCD matrices are used for voltage/current).

$$
\boxed{\begin{bmatrix} V_1^+ \\ V_1^- \end{bmatrix} = \begin{bmatrix} T_{11} & T_{12} \\ T_{21} & T_{22} \end{bmatrix} \begin{bmatrix} V_2^+ \\ V_2^- \end{bmatrix}}
$$

**Sign convention**: The waves at port 2 are ordered so that the cascade property is simple.

### 4.5.2 Relation Between S and T Parameters

For a two-port network, the conversion from S to T:

$$
\boxed{T_{11} = \frac{1}{S_{21}}, \quad T_{12} = -\frac{S_{22}}{S_{21}}}
$$
$$
\boxed{T_{21} = \frac{S_{11}}{S_{21}}, \quad T_{22} = \frac{S_{12} S_{21} - S_{11} S_{22}}{S_{21}}}
$$

The inverse conversion (T to S):

$$
\boxed{S_{11} = \frac{T_{21}}{T_{11}}, \quad S_{12} = \frac{T_{11} T_{22} - T_{12} T_{21}}{T_{11}}}
$$
$$
\boxed{S_{21} = \frac{1}{T_{11}}, \quad S_{22} = -\frac{T_{12}}{T_{11}}}
$$

### 4.5.3 Cascade Property

For two networks in cascade:

$$
\boxed{\mathbf{T}_{\text{total}} = \mathbf{T}_1 \cdot \mathbf{T}_2}
$$

This is the primary advantage of T-parameters — they avoid the tedious S-parameter re-normalization required when directly cascading S-parameter blocks.

### 4.5.4 Example: Transmission Line T-Parameters

For a lossless transmission line section of length $l$:

$$
\mathbf{T} = \begin{bmatrix} e^{j\beta l} & 0 \\ 0 & e^{-j\beta l} \end{bmatrix}
$$

This is especially simple because there are no reflections ($S_{11} = S_{22} = 0$, $S_{12} = S_{21} = e^{-j\beta l}$).

---

## 4.6 Generalized Scattering Parameters

### 4.6.1 Why Generalized S-Parameters?

In many practical situations, the reference impedances at different ports are not equal. The **generalized scattering matrix** accounts for this by normalizing the wave amplitudes appropriately.

### 4.6.2 Power-Wave Definition

Define normalized **power waves** $a_n$ and $b_n$ for each port:

$$
a_n = \frac{V_n^+}{\sqrt{Z_{0n}}} \quad \text{(incident power wave)}
$$
$$
b_n = \frac{V_n^-}{\sqrt{Z_{0n}}} \quad \text{(reflected power wave)}
$$

Then $|a_n|^2$ is the incident power at port $n$, and $|b_n|^2$ is the reflected power at port $n$.

The generalized S-matrix $\mathbf{S}^{(g)}$ is defined by:

$$
\boxed{\mathbf{b} = \mathbf{S}^{(g)} \mathbf{a}}
$$

### 4.6.3 Conversion to Z/Y Matrices

For an $N$-port network with reference impedance $Z_{0n}$ at port $n$:

Define diagonal matrix $\mathbf{Z}_0 = \text{diag}(Z_{01}, Z_{02}, \dots, Z_{0N})$.

The generalized S-parameters relate to the impedance matrix by:

$$
\boxed{\mathbf{S}^{(g)} = \mathbf{Z}_0^{-1/2} (\mathbf{Z} - \mathbf{Z}_0^*)(\mathbf{Z} + \mathbf{Z}_0)^{-1} \mathbf{Z}_0^{1/2}}
$$

For the common case where all reference impedances equal $Z_0$:

$$
\boxed{\mathbf{S} = (\mathbf{Z} - Z_0 \mathbf{I})(\mathbf{Z} + Z_0 \mathbf{I})^{-1}}
$$

### 4.6.4 Properties of the Generalized S-Matrix

- **Reciprocal**: $\mathbf{S}^{(g)} = [\mathbf{S}^{(g)}]^T$ (same as standard S-parameters)
- **Lossless**: $[\mathbf{S}^{(g)}]^\dagger \mathbf{S}^{(g)} = \mathbf{I}$ (unitary, same as standard)
- **Shift of reference plane**: Shifting port $n$ reference plane by $l_n$ multiplies the $n$-th column and $n$-th row by $e^{\pm j\beta_n l_n}$

### 4.6.5 Reference Plane Transformation

Moving the reference plane at port $i$ outward by distance $l_i$ multiplies the incident wave by $e^{j\beta_i l_i}$ and the reflected wave by $e^{-j\beta_i l_i}$. The S-matrix transforms as:

$$
S_{ij}' = S_{ij} e^{-j(\beta_i l_i + \beta_j l_j)}
$$

Or in matrix form:

$$
\mathbf{S}' = \mathbf{P} \mathbf{S} \mathbf{P}
$$

where $\mathbf{P} = \text{diag}(e^{-j\beta_1 l_1}, e^{-j\beta_2 l_2}, \dots, e^{-j\beta_N l_N})$.

This is critical for VNA calibration — the reference planes must be de-embedded to the device under test (DUT).

---

## 4.7 Conversion Between Matrix Representations

### 4.7.1 S ↔ Z Conversion

Given $\mathbf{Z}$ (with all ports referenced to $Z_0$):

$$
\boxed{\mathbf{S} = (\mathbf{Z} - Z_0\mathbf{I})(\mathbf{Z} + Z_0\mathbf{I})^{-1}}
$$
$$
\boxed{\mathbf{Z} = Z_0(\mathbf{I} + \mathbf{S})(\mathbf{I} - \mathbf{S})^{-1}}
$$

For a two-port network explicitly:

$$
S_{11} = \frac{(Z_{11} - Z_0)(Z_{22} + Z_0) - Z_{12}Z_{21}}{\Delta_Z}
$$
$$
S_{12} = \frac{2Z_{12}Z_0}{\Delta_Z}
$$
$$
S_{21} = \frac{2Z_{21}Z_0}{\Delta_Z}
$$
$$
S_{22} = \frac{(Z_{11} + Z_0)(Z_{22} - Z_0) - Z_{12}Z_{21}}{\Delta_Z}
$$

where $\Delta_Z = (Z_{11} + Z_0)(Z_{22} + Z_0) - Z_{12}Z_{21}$.

Likewise, Z from S:

$$
Z_{11} = Z_0 \frac{(1 + S_{11})(1 - S_{22}) + S_{12}S_{21}}{\Delta_S}
$$
$$
Z_{12} = Z_0 \frac{2S_{12}}{\Delta_S}
$$
$$
Z_{21} = Z_0 \frac{2S_{21}}{\Delta_S}
$$
$$
Z_{22} = Z_0 \frac{(1 - S_{11})(1 + S_{22}) + S_{12}S_{21}}{\Delta_S}
$$

where $\Delta_S = (1 - S_{11})(1 - S_{22}) - S_{12}S_{21}$.

### 4.7.2 S ↔ ABCD Conversion

For the common case of equal reference impedance $Z_0$ at both ports:

**ABCD → S**:

$$
S_{11} = \frac{A + B/Z_0 - C Z_0 - D}{A + B/Z_0 + C Z_0 + D}
$$
$$
S_{12} = \frac{2(AD - BC)}{A + B/Z_0 + C Z_0 + D}
$$
$$
S_{21} = \frac{2}{A + B/Z_0 + C Z_0 + D}
$$
$$
S_{22} = \frac{-A + B/Z_0 - C Z_0 + D}{A + B/Z_0 + C Z_0 + D}
$$

**S → ABCD**:

$$
A = \frac{(1 + S_{11})(1 - S_{22}) + S_{12}S_{21}}{2S_{21}}
$$
$$
B = Z_0 \frac{(1 + S_{11})(1 + S_{22}) - S_{12}S_{21}}{2S_{21}}
$$
$$
C = \frac{1}{Z_0} \frac{(1 - S_{11})(1 - S_{22}) - S_{12}S_{21}}{2S_{21}}
$$
$$
D = \frac{(1 - S_{11})(1 + S_{22}) + S_{12}S_{21}}{2S_{21}}
$$

### 4.7.3 Consistency Checks

When converting between representations, always verify:

1. **Reciprocity**: $Z_{12} = Z_{21}$, $Y_{12} = Y_{21}$, $S_{12} = S_{21}$, $AD - BC = 1$
2. **Determinant check**: For a reciprocal network, $\det(\mathbf{ABCD}) = 1$
3. **Losslessness**: For lossless networks, $|S_{11}|^2 + |S_{21}|^2 = 1$ (for a reciprocal two-port)
4. **Relativity**: S-parameter magnitudes must be $\le 1$ for passive networks

### 4.7.4 Conversion Table Summary

| Convert | To Z | To Y | To S | To ABCD | To T |
|---------|------|------|------|---------|------|
| **From Z** | — | $\mathbf{Z}^{-1}$ | $(Z - Z_0 I)(Z + Z_0 I)^{-1}$ | See Pozar Table 4.1 | — |
| **From Y** | $\mathbf{Y}^{-1}$ | — | $(I - Z_0 Y)(I + Z_0 Y)^{-1}$ | See Pozar Table 4.1 | — |
| **From S** | $Z_0(I+S)(I-S)^{-1}$ | $Z_0^{-1}(I-S)(I+S)^{-1}$ | — | See §4.7.2 | See §4.5.2 |
| **From ABCD** | See Pozar Table 4.1 | See Pozar Table 4.1 | See §4.7.2 | — | — |

---

## 4.8 Practical S-Parameter Measurements

### 4.8.1 Vector Network Analyzer (VNA)

The VNA measures S-parameters by:
1. Generating a swept-frequency test signal
2. Separating incident and reflected waves at each port using directional couplers
3. Down-converting the RF signals to an IF for detection
4. Computing complex ratios $b_i / a_j$

### 4.8.2 Calibration

VNA calibration removes systematic errors (directivity, source match, load match, isolation, frequency response):

| Calibration Type | Standards Required | Accuracy |
|-----------------|-------------------|----------|
| SOLT (Short-Open-Load-Thru) | 4 known standards | Good |
| TRL (Thru-Reflect-Line) | Transmission line standards | Excellent |
| SOLR (Short-Open-Load-Reciprocal) | Similar to SOLT, unknown thru | Good |

### 4.8.3 De-embedding

De-embedding removes the effects of fixtures, cables, and probes from measured S-parameters. The DUT's S-parameters are extracted from the cascade:

$$
\mathbf{S}_{\text{measured}} = \mathbf{S}_{\text{fixture1}} \star \mathbf{S}_{\text{DUT}} \star \mathbf{S}_{\text{fixture2}}
$$

Using T-parameters or ABCD matrices for the cascade, the DUT parameters can be extracted by pre-multiplying and post-multiplying by the inverses of the fixture parameters.

---

## 4.9 Detailed Examples

### 4.9.1 Example 4.1: S-Parameters of a Series Impedance

Find the S-parameters of a series impedance $Z$ inserted between two transmission lines of characteristic impedance $Z_0$.

**Solution using the Z-matrix approach:**

For a series impedance, the two-port Z-matrix is:

$$
Z_{11} = \frac{V_1}{I_1}\Big|_{I_2=0}, \quad Z_{12} = \frac{V_1}{I_2}\Big|_{I_1=0}
$$

With $I_2 = 0$ (port 2 open): $V_1 = Z I_1$, so $Z_{11} = Z$.
With $I_1 = 0$ (port 1 open): $V_1 = Z I_2$, so $Z_{12} = Z$.

By symmetry: $Z_{21} = Z$, $Z_{22} = Z$.

Thus:

$$
\mathbf{Z} = \begin{bmatrix} Z & Z \\ Z & Z \end{bmatrix}
$$

Converting to S-parameters:

$$
S_{11} = \frac{(Z - Z_0)(Z + Z_0) - Z^2}{(Z + Z_0)^2 - Z^2} = \frac{Z}{2Z_0 + Z}
$$

Wait, let's recalculate carefully.

$\Delta_Z = (Z_{11} + Z_0)(Z_{22} + Z_0) - Z_{12}Z_{21} = (Z + Z_0)^2 - Z^2 = Z^2 + 2ZZ_0 + Z_0^2 - Z^2 = 2ZZ_0 + Z_0^2$

$S_{11} = \frac{(Z - Z_0)(Z + Z_0) - Z^2}{\Delta_Z} = \frac{Z^2 - Z_0^2 - Z^2}{\Delta_Z} = \frac{-Z_0^2}{2ZZ_0 + Z_0^2} = \frac{-Z_0}{2Z + Z_0} = \frac{Z}{2Z + Z_0}?$ 

Hmm, let me recheck:

$S_{11} = \frac{(Z_{11} - Z_0)(Z_{22} + Z_0) - Z_{12}Z_{21}}{(Z_{11} + Z_0)(Z_{22} + Z_0) - Z_{12}Z_{21}} = \frac{(Z - Z_0)(Z + Z_0) - Z \cdot Z}{(Z + Z_0)(Z + Z_0) - Z \cdot Z}$

$(Z - Z_0)(Z + Z_0) = Z^2 - Z_0^2$
$(Z + Z_0)^2 - Z^2 = Z^2 + 2ZZ_0 + Z_0^2 - Z^2 = 2ZZ_0 + Z_0^2$

$S_{11} = \frac{Z^2 - Z_0^2 - Z^2}{2ZZ_0 + Z_0^2} = \frac{-Z_0^2}{2ZZ_0 + Z_0^2} = \frac{-Z_0}{2Z + Z_0}$

For a purely real impedance $Z = R$: $S_{11} = -\frac{Z_0}{2R + Z_0}$

$S_{21} = \frac{2Z_{21} Z_0}{\Delta_Z} = \frac{2ZZ_0}{2ZZ_0 + Z_0^2} = \frac{2Z}{2Z + Z_0}$

By symmetry of the series impedance network: $S_{11} = S_{22}$ and $S_{12} = S_{21}$.

For a **resistor** $R = Z_0$, we get $S_{11} = -1/3$, $S_{21} = 2/3$. Check: $|S_{11}|^2 + |S_{21}|^2 = 1/9 + 4/9 = 5/9 < 1$ (not lossless — power is dissipated in the resistor).

### 4.9.2 Example 4.2: S-Parameters of a Shunt Admittance

Find the S-parameters of a shunt admittance $Y$ across the transmission line, using $Z_0$ as reference.

**Z-matrix approach:**

For a shunt element, think of it as a T-network with the shunt element in the middle and the transmission line on both sides (the shunt element connects port 1 and port 2).

Better approach: From ABCD matrix.

For a shunt admittance $Y$:

$$
\mathbf{ABCD} = \begin{bmatrix} 1 & 0 \\ Y & 1 \end{bmatrix}
$$

Converting to S-parameters:

$$
S_{11} = \frac{A + B/Z_0 - C Z_0 - D}{A + B/Z_0 + C Z_0 + D} = \frac{1 + 0 - Y Z_0 - 1}{1 + 0 + Y Z_0 + 1} = \frac{-Y Z_0}{2 + Y Z_0} = -\frac{Y Z_0}{2 + Y Z_0}
$$

$$
S_{21} = \frac{2}{A + B/Z_0 + C Z_0 + D} = \frac{2}{2 + Y Z_0}
$$

For a **capacitor** $Y = j\omega C$ at high frequencies: $S_{11} \to -1$, $S_{21} \to 0$ (shorted at high frequency).

For an **open circuit**: $Y = 0$, $S_{11} = 0$, $S_{21} = 1$ (no effect).

For a **short circuit**: $Y \to \infty$, $S_{11} \to -1$, $S_{21} \to 0$ (total reflection, no transmission).

### 4.9.3 Example 4.3: S-Parameters of a Transmission Line Section

A lossless transmission line of characteristic impedance $Z_0$ and length $l$ is connected between two ports with reference impedance $Z_0$.

**Direct from physics**: The wave on a matched line suffers only a phase shift:

$$
V_1^- = V_2^+ e^{-j\beta l}, \quad V_2^- = V_1^+ e^{-j\beta l}
$$

Wait — this is actually a cascade relationship. Let me re-derive properly.

For a transmission line of length $l$ with characteristic impedance $Z_0$ (same as reference impedance), when port 2 is matched:

- No reflection at the load: $V_2^+ = 0$ (terminated in $Z_0$)
- $V_1^- = V_2^- e^{-j\beta l} = 0$ (no reflected wave from matched load)
- $S_{11} = V_1^- / V_1^+ = 0$

When port 1 is matched ($V_1^+ = 0$):
- $S_{22} = V_2^- / V_2^+ = 0$

Transmission:
- $S_{21} = V_2^- / V_1^+ = e^{-j\beta l}$ (the wave propagates from port 1 to port 2)
- $S_{12} = V_1^- / V_2^+ = e^{-j\beta l}$ (the wave propagates from port 2 to port 1)

Thus:

$$
\boxed{\mathbf{S} = \begin{bmatrix} 0 & e^{-j\beta l} \\ e^{-j\beta l} & 0 \end{bmatrix}}
$$

This is a **reciprocal** ($S_{12} = S_{21}$) and **lossless** ($|S_{11}|^2 + |S_{21}|^2 = 0 + 1 = 1$) network.

### 4.9.4 Example 4.4: Reflection Coefficient of a Load Through a Line

A load impedance $Z_L$ is connected to port 2 of a transmission line of length $l$ and $Z_0$. Find the input reflection coefficient at port 1.

Using the signal flow graph approach:

The load has reflection coefficient $\Gamma_L = (Z_L - Z_0)/(Z_L + Z_0)$.

The line has S-matrix: $\mathbf{S} = \begin{bmatrix} 0 & e^{-j\beta l} \\ e^{-j\beta l} & 0 \end{bmatrix}$

From the input reflection coefficient formula:

$$
\Gamma_{\text{in}} = S_{11} + \frac{S_{12} S_{21} \Gamma_L}{1 - S_{22} \Gamma_L} = 0 + \frac{e^{-j\beta l} \cdot e^{-j\beta l} \cdot \Gamma_L}{1 - 0} = \Gamma_L e^{-j2\beta l}
$$

Thus:

$$
\boxed{\Gamma_{\text{in}} = \Gamma_L e^{-j2\beta l}}
$$

This is the classic transmission line impedance transformation — the reflection coefficient at the input is the load reflection coefficient rotated by $2\beta l$ on the Smith chart.

Check: For $l = \lambda/4$ ($\beta l = \pi/2$):

$$
\Gamma_{\text{in}} = \Gamma_L e^{-j\pi} = -\Gamma_L
$$

which corresponds to $Z_{\text{in}} = Z_0^2 / Z_L$ — the quarter-wave transformer.

### 4.9.5 Example 4.5: Two-Port Amplifier

An amplifier has S-parameters (measured in 50 $\Omega$ system at 2 GHz):

$$
S_{11} = 0.3 \angle -60^\circ, \quad S_{21} = 5.0 \angle 90^\circ
$$
$$
S_{12} = 0.1 \angle 30^\circ, \quad S_{22} = 0.2 \angle -30^\circ
$$

**(a) Is the amplifier stable?** Compute $\Gamma_{\text{in}}$ and $\Gamma_{\text{out}}$ for $Z_S = Z_L = 50\ \Omega$.

Since $\Gamma_S = 0$ and $\Gamma_L = 0$ (source and load matched to 50 $\Omega$):

$$
\Gamma_{\text{in}} = S_{11} = 0.3 \angle -60^\circ \quad (|\Gamma_{\text{in}}| = 0.3 < 1, \text{ stable})
$$
$$
\Gamma_{\text{out}} = S_{22} = 0.2 \angle -30^\circ \quad (|\Gamma_{\text{out}}| = 0.2 < 1, \text{ stable})
$$

**(b) Maximum transducer gain:**

For a unilateral amplifier ($S_{12} \approx 0$):

$$
G_{TU} = \frac{|S_{21}|^2 (1 - |\Gamma_S|^2)(1 - |\Gamma_L|^2)}{|1 - S_{11}\Gamma_S|^2 |1 - S_{22}\Gamma_L|^2}
$$

For matched source and load: $G_T = |S_{21}|^2 = 25$ (about 14 dB).

For the unilateral case with conjugate matching:

$$
\Gamma_S = S_{11}^* = 0.3 \angle 60^\circ, \quad \Gamma_L = S_{22}^* = 0.2 \angle 30^\circ
$$

$$
G_{TU,\max} = |S_{21}|^2 \cdot \frac{1}{1 - |S_{11}|^2} \cdot \frac{1}{1 - |S_{22}|^2} = 25 \cdot \frac{1}{1 - 0.09} \cdot \frac{1}{1 - 0.04}
$$
$$
= 25 \cdot 1.099 \cdot 1.042 = 28.63 \quad (\text{about } 14.6 \text{ dB})
$$

The unilateral figure (14 dB) is close to the matched case (14 dB) because $S_{12}$ is small and the input/output match is reasonable.

### 4.9.6 Example 4.6: ABCD Matrix of a Cascade

Find the ABCD matrix of a cascade: series resistor $R \to$ transmission line (length $l$, $Z_0$) $\to$ shunt capacitor $C$.

$$
\mathbf{ABCD}_{\text{total}} = 
\begin{bmatrix} 1 & R \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} \cos(\beta l) & jZ_0 \sin(\beta l) \\ jY_0 \sin(\beta l) & \cos(\beta l) \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ j\omega C & 1 \end{bmatrix}
$$

Let's compute step by step.

First, series R + line:

$$
\begin{bmatrix} 1 & R \\ 0 & 1 \end{bmatrix}
\begin{bmatrix} \cos\theta & jZ_0 \sin\theta \\ jY_0 \sin\theta & \cos\theta \end{bmatrix}
= \begin{bmatrix} \cos\theta + jRY_0\sin\theta & jZ_0\sin\theta + R\cos\theta \\ jY_0\sin\theta & \cos\theta \end{bmatrix}
$$

where $\theta = \beta l$.

Then cascade with shunt C:

$$
\begin{bmatrix} \cos\theta + jRY_0\sin\theta & jZ_0\sin\theta + R\cos\theta \\ jY_0\sin\theta & \cos\theta \end{bmatrix}
\begin{bmatrix} 1 & 0 \\ j\omega C & 1 \end{bmatrix}
$$

$$
A_{\text{total}} = (\cos\theta + jRY_0\sin\theta) \cdot 1 + (jZ_0\sin\theta + R\cos\theta) \cdot j\omega C
$$
$$
= \cos\theta + jRY_0\sin\theta + j\omega C (jZ_0\sin\theta + R\cos\theta)
$$
$$
= \cos\theta + jRY_0\sin\theta - \omega C Z_0 \sin\theta + j\omega C R \cos\theta
$$
$$
= (\cos\theta - \omega C Z_0 \sin\theta) + j(RY_0\sin\theta + \omega C R \cos\theta)
$$

$$
B_{\text{total}} = (\cos\theta + jRY_0\sin\theta) \cdot 0 + (jZ_0\sin\theta + R\cos\theta) \cdot 1
$$
$$
= jZ_0\sin\theta + R\cos\theta
$$

$$
C_{\text{total}} = (jY_0\sin\theta) \cdot 1 + (\cos\theta) \cdot j\omega C
$$
$$
= jY_0\sin\theta + j\omega C \cos\theta
$$

$$
D_{\text{total}} = (jY_0\sin\theta) \cdot 0 + (\cos\theta) \cdot 1 = \cos\theta
$$

This ABCD matrix can then be converted to S-parameters for insertion into a 50 $\Omega$ system.

---

## 4.10 Extended Numerical Experiment: S-Parameter Validation

### 4.10.1 Self-Consistency Checks for S-Parameters

Any physically realizable S-parameter matrix must satisfy:

1. **Passive network**: $\mathbf{I} - \mathbf{S}^\dagger \mathbf{S}$ is positive semidefinite (the eigenvalues of $\mathbf{S}^\dagger \mathbf{S}$ are $\le 1$)
2. **Lossless network**: $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ (all singular values = 1)
3. **Reciprocal network**: $S_{ij} = S_{ji}$
4. **Causality**: Kramers-Kronig relations between real and imaginary parts

### 4.10.2 Numerical Self-Consistency Test

For a random reciprocal, lossless two-port, verify:

- $|S_{11}|^2 + |S_{21}|^2 = 1$
- $S_{11}^* S_{21} + S_{21}^* S_{22} = 0$ (column orthogonality)

Parameterize using one real parameter $0 \le \rho \le 1$ and phases $\phi, \theta$:

$$
S_{11} = \rho e^{j\phi}
$$
$$
S_{22} = -\rho e^{j(2\theta - \phi)} \quad \text{(from orthogonality condition)}
$$
$$
S_{12} = S_{21} = \sqrt{1 - \rho^2} \, e^{j\theta}
$$

This 3-parameter form fully describes any reciprocal, lossless two-port.

### 4.10.3 Conversion Accuracy

A complete round-trip conversion test:
1. Start with S-parameters
2. Convert to ABCD
3. Convert back to S
4. Verify maximum fractional error $< 10^{-12}$ (machine precision)

---

## 4.11 Engineering Applications

### 4.11.1 Matching Network Design

S-parameters guide matching network design:
- $S_{11}$ and $S_{22}$ show how well ports are matched to the reference impedance
- Matching networks are designed to minimize $S_{11}$ and $S_{22}$ over a bandwidth
- The reflection coefficient is directly $S_{11}$ when all source/load ports are terminated

### 4.11.2 Amplifier Design

- **Gain**: Maximizing $|S_{21}|$ within stability constraints
- **Stability**: Ensuring $|\Gamma_{\text{in}}| < 1$ and $|\Gamma_{\text{out}}| < 1$ for all passive source/load impedances
- **Noise figure**: Optimizing source reflection coefficient for minimum noise
- **Bandwidth**: Trade-off between gain flatness and matching

### 4.11.3 Filter Design

- S-parameters define passband ($|S_{21}| \approx 1$) and stopband ($|S_{21}| \ll 1$)
- Insertion loss: $IL = -20\log_{10}|S_{21}|$ (dB)
- Return loss: $RL = -20\log_{10}|S_{11}|$ (dB)
- ABCD matrices cascade filter sections efficiently

### 4.11.4 Power Dividers and Couplers

- **Ideal 3-dB hybrid**: $|S_{21}| = |S_{31}| = 1/\sqrt{2}$, $S_{11} = S_{41} = 0$
- **Wilkinson power divider**: All ports matched, high isolation between output ports
- **Directional coupler**: $S_{31} \approx 0$ (isolation port), $S_{21}$ (through), $S_{41}$ (coupled)

---

## 4.12 Key Formulas Cheat Sheet

### S-Parameter Fundamentals

| Quantity | Formula |
|----------|---------|
| Definition | $\mathbf{V}^- = \mathbf{S} \mathbf{V}^+$ |
| Reflection coefficient at port $n$ | $\Gamma_n = S_{nn}$ (others matched) |
| Input impedance | $Z_{\text{in},n} = Z_{0n} \frac{1 + S_{nn}}{1 - S_{nn}}$ |
| Reciprocal | $\mathbf{S} = \mathbf{S}^T$ |
| Lossless | $\mathbf{S}^\dagger \mathbf{S} = \mathbf{I}$ |

### Two-Port Network Conversions

| From S to Z | From S to ABCD |
|-------------|----------------|
| $Z_{11} = Z_0 \frac{(1+S_{11})(1-S_{22}) + S_{12}S_{21}}{\Delta_S}$ | $A = \frac{(1+S_{11})(1-S_{22}) + S_{12}S_{21}}{2S_{21}}$ |
| $Z_{12} = Z_0 \frac{2S_{12}}{\Delta_S}$ | $B = Z_0 \frac{(1+S_{11})(1+S_{22}) - S_{12}S_{21}}{2S_{21}}$ |
| $Z_{21} = Z_0 \frac{2S_{21}}{\Delta_S}$ | $C = \frac{1}{Z_0} \frac{(1-S_{11})(1-S_{22}) - S_{12}S_{21}}{2S_{21}}$ |
| $Z_{22} = Z_0 \frac{(1-S_{11})(1+S_{22}) + S_{12}S_{21}}{\Delta_S}$ | $D = \frac{(1-S_{11})(1+S_{22}) + S_{12}S_{21}}{2S_{21}}$ |

where $\Delta_S = (1 - S_{11})(1 - S_{22}) - S_{12}S_{21}$.

### Input/Output Reflection

| Quantity | Formula |
|----------|---------|
| Input $\Gamma$ | $\Gamma_{\text{in}} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L}$ |
| Output $\Gamma$ | $\Gamma_{\text{out}} = S_{22} + \frac{S_{12}S_{21}\Gamma_S}{1 - S_{11}\Gamma_S}$ |
| Transducer gain | $G_T = \frac{|S_{21}|^2 (1-|\Gamma_S|^2)(1-|\Gamma_L|^2)}{|(1-S_{11}\Gamma_S)(1-S_{22}\Gamma_L) - S_{12}S_{21}\Gamma_S\Gamma_L|^2}$ |

### Scattering Transfer Matrix

| T from S | S from T |
|----------|----------|
| $T_{11} = 1/S_{21}$ | $S_{11} = T_{21}/T_{11}$ |
| $T_{12} = -S_{22}/S_{21}$ | $S_{12} = (T_{11}T_{22} - T_{12}T_{21})/T_{11}$ |
| $T_{21} = S_{11}/S_{21}$ | $S_{21} = 1/T_{11}$ |
| $T_{22} = (S_{12}S_{21} - S_{11}S_{22})/S_{21}$ | $S_{22} = -T_{12}/T_{11}$ |

### ABCD Matrix Properties

| Property | Condition |
|----------|-----------|
| Cascade | $\mathbf{ABCD}_{\text{tot}} = \mathbf{ABCD}_1 \mathbf{ABCD}_2$ |
| Reciprocal | $AD - BC = 1$ |
| Symmetric | $A = D$ |
| Lossless | $A, D$ real; $B, C$ imaginary |

---

## 4.13 Summary Checklist

| ✅ | Topic | Key Takeaway |
|----|-------|-------------|
| ✓ | Z/Y matrices | Total voltage/current representation; reciprocal $\Rightarrow$ symmetric |
| ✓ | S-parameters | Wave representation; directly measurable; unitary for lossless |
| ✓ | ABCD matrices | Cascade-friendly; $AD - BC = 1$ for reciprocal |
| ✓ | Signal flow graphs | Graphical network analysis; Mason's gain formula |
| ✓ | T-parameters | Cascade-friendly wave representation |
| ✓ | Generalized S-params | Different reference impedances per port |
| ✓ | Matrix conversions | S ↔ Z, S ↔ ABCD, S ↔ T all well-defined |
| ✓ | Reciprocal constraints | $S_{ij} = S_{ji}$, $AD - BC = 1$ |
| ✓ | Lossless constraints | $S^\dagger S = I$, $|S_{11}|^2 + |S_{21}|^2 = 1$ |
| ✓ | De-embedding | Fixture removal using cascade matrix inversion |

---

## References

1. D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley, 2012, Chapter 4.
2. K. Kurokawa, "Power Waves and the Scattering Matrix," *IEEE Trans. Microwave Theory Tech.*, vol. MTT-13, no. 2, pp. 194–202, Mar. 1965.
3. S. J. Mason, "Feedback Theory — Some Properties of Signal Flow Graphs," *Proc. IRE*, vol. 41, no. 9, pp. 1144–1156, Sept. 1953.
4. P. H. Smith, "Transmission Line Calculator," *Electronics*, vol. 12, no. 1, pp. 29–31, Jan. 1939.
5. R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., Wiley-IEEE Press, 2001, Ch. 4.

<!-- 完成于 2026-04-29 09:56 CST -->

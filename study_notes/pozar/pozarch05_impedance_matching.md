# Pozar Chapter 5 — Impedance Matching and Tuning

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 250–320.
> Covers lumped L-section matching, single/double-stub tuning, quarter-wave transformers, and tapered-line matching.

---

## 5.1 L-Section Matching Networks (LC Lumped Elements)

### 5.1.1 Problem Statement

Given a load impedance $Z_L = R_L + jX_L$ and a real source/line impedance $Z_0$, design a **2-element LC network** (L-section) that transforms $Z_L$ to $Z_0$ at a single design frequency $f_0$.

**Key constraint**: The L-section introduces zero DC path between input and output (for the series-capacitor / shunt-inductor topology). The 8 possible topologies arise from:
- Shunt-first vs. series-first ordering
- Capacitor vs. inductor in each arm
- Which side the shunt element is on (load side vs. source side)

**Selection rule** — use normalized LOAD CONDUCTANCE $g_L = G_L / Y_0$ (correct for both real and complex loads):

$$
\begin{cases}
g_L < 1 \; \text{(load admittance inside $g=1$ circle)} &\Rightarrow \text{shunt-first topology} \\
g_L \ge 1 \; \text{(load admittance outside/on $g=1$ circle)} &\Rightarrow \text{series-first topology}
\end{cases}
$$

> ⚠️ **Caution**: The simplified rule $R_L < Z_0 \to$ shunt-first is **only valid for purely real loads**. For complex $Z_L$, the criterion must use $g_L = \text{Re}(1/Z_L) \, / \, Y_0$. Example: $Z_L = 200 - j100\,\Omega$ with $Z_0 = 100\,\Omega$ has $R_L = 200 > Z_0$, but $g_L = 0.4 < 1$, so the correct topology is **shunt-first**, not series-first.

### 5.1.2 Analytical Solution — Shunt-First ($g_L < 1$)

Topology: load $\to$ shunt $jB$ $\to$ series $jX$ $\to$ source

**Step 1 — Shunt susceptance $B$**:

$$
\boxed{B = -B_L \pm \frac{\sqrt{G_L/Z_0 - G_L^2}}{G_L / Z_0}}
$$

where $Y_L = 1/Z_L = G_L + jB_L$.

Equivalently, written with circuit parameters:

$$
\boxed{B = -B_L \pm \frac{\sqrt{G_L(1/Z_0 - G_L)}}{G_L / Z_0} = \frac{-B_L \pm \sqrt{G_L Z_0 - G_L^2 Z_0^2}}{G_L Z_0 / Z_0?}}
$$

More cleanly:

$$
B_{\pm} = -B_L \pm \frac{\sqrt{G_L/Y_0 - G_L^2}}{G_L/Y_0} \quad\text{where } Y_0 = 1/Z_0
$$

Two solutions exist since $G_L < Y_0$.

**Step 2 — Series reactance $X$**:

After shunt $B$, the transformed admittance is $Y' = G_L + j(B_L + B)$.
The impedance looking into the series element toward the load is:

$$
Z' = \frac{1}{Y'} = \frac{G_L}{G_L^2 + (B_L + B)^2} - j\frac{B_L + B}{G_L^2 + (B_L + B)^2}
$$

Since real($Z'$) must equal $Z_0$:

$$
\frac{G_L}{G_L^2 + (B_L + B)^2} = Z_0 \quad \Rightarrow \quad G_L^2 + (B_L + B)^2 = \frac{G_L}{Z_0}
$$

The series reactance cancels the remaining imaginary part:

$$
\boxed{X = \frac{B_L + B}{G_L^2 + (B_L + B)^2} = Z_0 \frac{B_L + B}{G_L}}
$$

**Complete solution (shunt-first)**:

$$
\boxed{
\begin{aligned}
B &= -B_L \pm \frac{\sqrt{G_L/Y_0 - G_L^2}}{G_L / Y_0} \\[4pt]
X &= Z_0 \frac{B_L + B}{G_L}
\end{aligned}}
$$

The $\pm$ gives two solutions (different element values, bandwidths).

### 5.1.3 Complete Analytical L-Section Formulas (Pozar Eqs. 5.6–5.11)

Given load $Z_L = R_L + jX_L$ and system impedance $Z_0$, define the discriminant:

$$
\Delta = R_L^2 + X_L^2 - Z_0 R_L
$$

> $\Delta \ge 0$ is required for a physically realizable L-section. This defines the **matchable region** of load impedances.

**Shunt-first** (load inside $g=1$ circle, $g_L < 1$):

$$
\boxed{B_s = \frac{X_L \pm \sqrt{R_L/Z_0} \sqrt{\Delta}}{R_L^2 + X_L^2},\qquad
X_s = \frac{1}{B_s} + \frac{X_L Z_0}{R_L} - \frac{Z_0}{B_s R_L}}
$$

**Series-first** (load outside $g=1$ circle, $g_L \ge 1$):

$$
\boxed{X_s = \frac{-X_L \pm \dfrac{\sqrt{\Delta}}{\sqrt{R_L/Z_0}}}{R_L/Z_0 - 1},\qquad
B_s = -\operatorname{Im}\left(\frac{1}{Z_L + jX_s}\right)}
$$

Each gives two solutions ($\pm$), yielding different LC component values and bandwidths.

### 5.1.4 Example 5.1 — L-Section Matching (Pozar 4th ed.)

> Design an L-section matching network to match $Z_L = 200 - j100\;\Omega$ to a $Z_0 = 100\;\Omega$ line at $f_0 = 500\;\text{MHz}$.

$Z_L = 200 - j100\,\Omega$, $Z_0 = 100\,\Omega$.
$g_L = G_L/Y_0 = \text{Re}(1/Z_L) \cdot Z_0 = 0.4 < 1$ → **shunt-first** topology.

Using Pozar Eq. 5.6–5.7:
- Solution 1: $B = 0.002899\,\text{S}$, $X = 122.47\,\Omega$
- Solution 2: $B = -0.006899\,\text{S}$, $X = -122.47\,\Omega$

> ⚠️ The naive rule $R_L > Z_0 \to$ series-first would give the WRONG topology here. Always check $g_L$, not $R_L/Z_0$, for complex loads.

### 5.1.6 Bandwidth of L-Section Networks

The L-section is inherently **narrowband**. At frequencies away from $f_0$:

$$
|\Gamma|^2 = \frac{(X/X_0 - B/B_0)^2}{4 + (X/X_0 - B/B_0)^2}
$$

The fractional bandwidth for a given $|\Gamma_m|$ is approximately:

$$
\frac{\Delta f}{f_0} \approx \frac{2}{Q_L} \cdot \frac{|\Gamma_m|}{\sqrt{1 - |\Gamma_m|^2}}
$$

where $Q_L$ is the loaded Q of the matching network. Between the two solutions, the one with lower Q gives wider bandwidth.

---

## 5.2 Single-Stub Tuning

### 5.2.1 Concept

A **stub** is a short length of transmission line (open-circuited or short-circuited) connected in shunt or in series with the main line. The input impedance of a stub is purely reactive (imaginary for lossless lines), making it equivalent to a lumped $L$ or $C$ at a single frequency.

**Four configurations**:
1. Shunt stub (short-circuited)
2. Shunt stub (open-circuited)
3. Series stub (short-circuited)
4. Series stub (open-circuited)

### 5.2.2 Shunt Stub Tuning

Topology: load → transmission line (length $d$) → shunt stub (length $l$) → source

**Design procedure**:

**Step 1** — Find $d$ such that the admittance $Y(d)$ looking toward the load at distance $d$ from the load has real part $= Y_0 = 1/Z_0$.

$$Y(d) = Y_0 \frac{Y_L + jY_0 \tan(\beta d)}{Y_0 + jY_L \tan(\beta d)} = G(d) + jB(d)$$

Find $d$ such that $G(d) = Y_0$.

Two mathematical solutions:

$$
\tan(\beta d) = \frac{B_L \pm \sqrt{G_L[(Y_0 - G_L)^2 + B_L^2]/Y_0 - (Y_0 - G_L)B_L}}{G_L - Y_0}
$$

More commonly, solve via Smith chart:
1. Plot $y_L = Y_L/Y_0$ on Smith chart
2. Rotate toward generator to intersect the $g=1$ circle
3. Read $d$ (in wavelengths) and $b$ (normalized susceptance at intersection)

**Step 2** — Choose stub length $l$ to produce susceptance $B_s = -B(d)$.

For a **short-circuited** shunt stub:

$$
B_s = -Y_0 \cot(\beta l) \quad\Rightarrow\quad \frac{l}{\lambda} = \frac{1}{2\pi} \arctan\left(\frac{Y_0}{B_s}\right)
$$

For an **open-circuited** shunt stub:

$$
B_s = Y_0 \tan(\beta l) \quad\Rightarrow\quad \frac{l}{\lambda} = \frac{1}{2\pi} \arctan\left(\frac{B_s}{Y_0}\right)
$$

### 5.2.3 Series Stub Tuning

Topology: load → transmission line (length $d$) → series stub (length $l$) → source

**Step 1** — Find $d$ such that the impedance $Z(d)$ has real part $= Z_0$.

$$Z(d) = Z_0 \frac{Z_L + jZ_0 \tan(\beta d)}{Z_0 + jZ_L \tan(\beta d)} = R(d) + jX(d)$$

Find $d$ such that $R(d) = Z_0$.

**Step 2** — Choose stub length $l$ to produce reactance $X_s = -X(d)$.

For **short-circuited** series stub:

$$
X_s = Z_0 \tan(\beta l) \quad\Rightarrow\quad \frac{l}{\lambda} = \frac{1}{2\pi} \arctan\left(\frac{X_s}{Z_0}\right)
$$

For **open-circuited** series stub:

$$
X_s = -Z_0 \cot(\beta l) \quad\Rightarrow\quad \frac{l}{\lambda} = \frac{1}{2\pi} \arctan\left(\frac{Z_0}{X_s}\right)
$$

### 5.2.4 Example 5.2 — Shunt Stub Matching

> Match $Z_L = 100 + j80\;\Omega$ to a $75\;\Omega$ line using a single shunt stub (short-circuited).

$Z_0 = 75\;\Omega$, $Z_L = 100 + j80\;\Omega$.

$y_L = \frac{Z_0}{Z_L} = \frac{75}{100 + j80} = 0.457 - j0.366$ (normalized).

On the Smith chart, rotate toward generator to the $g=1$ circle. Two intersections give:

- Solution 1: $d_1 = 0.103\lambda$, $b_1 = 0.84$ → $l_1 = 0.099\lambda$
- Solution 2: $d_2 = 0.352\lambda$, $b_2 = -0.84$ → $l_2 = 0.401\lambda$ (since $\cot(\beta l) = -0.84$)

### 5.2.5 Analytical Solution for Shunt Stub $d$

Given $Y_L = G_L + jB_L$, the admittance at distance $d$ from the load is:

$$
Y(d) = Y_0 \frac{G_L + j(B_L + Y_0 t)}{Y_0 + j G_L t - B_L t} \quad\text{where } t = \tan(\beta d)
$$

Setting $G(d) = Y_0$ gives a quadratic in $t$:

$$
t^2 = \frac{(Y_0 - G_L)^2 + B_L^2}{G_L Y_0 - Y_0^2} \cdot \frac{Y_0}{G_L}? 
$$

More precisely (from Pozar Eq. 5.18):

$$
t = \frac{B_L \pm \sqrt{G_L[(Y_0 - G_L)^2 + B_L^2]/Y_0}}{G_L - Y_0}
$$

where $t = \tan(\beta d)$.

From $t$, we find $d$:

$$
\frac{d}{\lambda} = 
\begin{cases}
\frac{1}{2\pi} \arctan(t) & t \ge 0 \\
\frac{1}{2\pi} [\pi + \arctan(t)] & t < 0
\end{cases}
$$

The normalized susceptance at this point is:

$$
b(d) = \frac{B(d)}{Y_0} = \frac{B_L + Y_0 t - (G_L t - B_L)t / (1 + t^2)}{G_L t + Y_0(1 + t^2/t)...}
$$

This is messy. The Smith chart approach is more intuitive.

---

## 5.3 Double-Stub Tuning

### 5.3.1 Motivation

Single-stub tuning requires a variable $d$ (distance from load to stub), which is impractical in fixed printed circuits. **Double-stub tuning** uses two stubs at **fixed spacing** (typically $\lambda/8$ or $3\lambda/8$), with only the stub lengths being adjustable.

### 5.3.2 Configuration

```
Load --- TL length d --- Stub 1 --- TL length s --- Stub 2 --- Source
```

where $s$ is fixed (e.g., $3\lambda/8$) and $d$ is also known. Only $l_1$ and $l_2$ (stub lengths) are variable.

### 5.3.3 Design Procedure (Shunt Stubs)

Given load $Y_L$, fixed $d$ and $s$:

**Step 1** — Transform $Y_L$ through $d$ to get $Y_1$ at stub 1 location.

**Step 2** — Add stub 1 susceptance $B_1$: $Y_1' = Y_1 + jB_1$.

**Step 3** — Transform $Y_1'$ through $s$ to get $Y_2$ at stub 2 location.

**Step 4** — Add stub 2 susceptance: $Y_{\text{in}} = Y_2 + jB_2 = Y_0$.

### 5.3.4 Forbidden Region (Blind Spot)

Double-stub tuners have a **forbidden region** of load admittances that cannot be matched for a given stub spacing $s$.

The condition for matchability is:
$$
G_L > \frac{Y_0}{\sin^2(\beta s)} \cdot \frac{1}{1 + \cot^2(\beta s)}? 
$$

More precisely, the admittance $Y_1$ (after distance $d$ from load) must fall **outside** a certain "forbidden circle" on the Smith chart. The forbidden region expands as $s$ approaches 0 or $\lambda/2$.

For $s = \lambda/8$ ($45^\circ$), the forbidden region is $g_L > 2$.
For $s = 3\lambda/8$ ($135^\circ$), the forbidden region is $g_L > 2$ (same).
For $s = \lambda/4$ ($90^\circ$), all loads with $g_L \le 1$ are matchable, but $g_L > 1$ loads may be problematic.

The **forbidden circle** on the admittance Smith chart has:

$$
\text{Center: } \left(\frac{1}{2\sin^2(\beta s)}, 0\right), \quad \text{Radius: } \frac{1}{2|\sin(\beta s)|}
$$

Any normalized load conductance $g_L$ must satisfy:
$$
g_L \le \frac{1}{\sin^2(\beta s)}
$$

For $s = \lambda/8$: $\beta s = \pi/4$, $\sin(\pi/4) = 1/\sqrt{2}$, so $g_L \le 2$.
For $s = 3\lambda/8$: $\beta s = 3\pi/4$, $\sin(3\pi/4) = 1/\sqrt{2}$, so $g_L \le 2$ (same).

### 5.3.5 Extending Range

To match loads in the forbidden region:
- Change the stub spacing $s$
- Add a section of transmission line between the load and the first stub
- Use a triple-stub tuner (no forbidden region, all loads matchable)

---

## 5.4 Quarter-Wave Transformer

### 5.4.1 Single-Section Transformer

A transmission line of length $\lambda/4$ and characteristic impedance $Z_1$ can transform a real load $Z_L$ to a real input impedance $Z_{\text{in}}$:

$$
\boxed{Z_{\text{in}} = \frac{Z_1^2}{Z_L}}
$$

To match a real load $R_L$ to a line $Z_0$:

$$
\boxed{Z_1 = \sqrt{Z_0 R_L}}
$$

**Bandwidth**: The reflection coefficient magnitude varies with frequency as:

$$
|\Gamma| = \frac{|R_L - Z_0|}{\sqrt{(R_L + Z_0)^2 + 4\sqrt{Z_0 R_L} \tan^2(\theta)}}
$$

where $\theta = \beta l = \frac{\pi}{2} \frac{f}{f_0}$.

At the center frequency $f_0$ ($\theta = \pi/2$), $|\Gamma| = 0$. At $f$ where $\theta \ne \pi/2$:

$$
\Gamma = \frac{R_L - Z_0}{R_L + Z_0 + j2\sqrt{Z_0 R_L} \tan \theta}
$$

$$
|\Gamma| = \frac{|R_L - Z_0|}{\sqrt{(R_L + Z_0)^2 + 4 Z_0 R_L \tan^2\theta}}
$$

**Fractional bandwidth** for a maximum acceptable $|\Gamma_m|$:

$$
\boxed{\frac{\Delta f}{f_0} = 2 - \frac{4}{\pi} \arccos\left[ \frac{|\Gamma_m|}{\sqrt{1 - |\Gamma_m|^2}} \cdot \frac{2\sqrt{Z_0 R_L}}{|R_L - Z_0|} \right]}
$$

For small mismatch:

$$
\frac{\Delta f}{f_0} \approx 2 - \frac{4}{\pi} \arccos\left( \frac{2\Gamma_m Z_1}{|R_L - Z_0|} \right)
$$

### 5.4.2 Multi-Section Quarter-Wave Transformer

To increase bandwidth, use **N cascaded $\lambda/4$ sections** at $f_0$, each with impedance $Z_n$.

**Design approaches**:
1. **Binomial (maximally flat)** — reflection coefficient has $N$ zero derivatives at $f_0$
2. **Chebyshev (equal-ripple)** — reflection coefficient has equal ripple in the passband

### 5.4.3 Binomial Transformer (Maximally Flat)

The reflection coefficient is designed to have the form:

$$
\Gamma(\theta) = A (1 + e^{-j2\theta})^N = A \cdot 2^N \cos^N(\theta) \cdot e^{-jN\theta}
$$

where $A$ is determined by the impedance ratio.

The impedance of section $n$ is:

$$
\ln\left(\frac{Z_{n+1}}{Z_n}\right) \approx 2^{-N} C_n^N \ln\left(\frac{R_L}{Z_0}\right)
$$

where $C_n^N$ are binomial coefficients.

For $N = 2$:

$$
\ln\left(\frac{Z_1}{Z_0}\right) = \frac{1}{4} \ln\left(\frac{R_L}{Z_0}\right), \quad
\ln\left(\frac{Z_2}{Z_1}\right) = \frac{1}{4} \ln\left(\frac{R_L}{Z_0}\right)
$$

So $Z_1 = Z_0^{3/4} R_L^{1/4}$, $Z_2 = Z_0^{1/4} R_L^{3/4}$.

Bandwidth:

$$
\frac{\Delta f}{f_0} = 2 - \frac{4}{\pi} \arccos\left[ \frac{1}{2} \left(\frac{2\Gamma_m}{A}\right)^{1/N} \right]
$$

where $A \approx \frac{1}{2^N} \ln\left(\frac{R_L}{Z_0}\right)$.

### 5.4.4 Chebyshev Transformer (Equal Ripple)

The reflection coefficient follows a Chebyshev polynomial:

$$
\Gamma(\theta) = A e^{-jN\theta} \frac{T_N(\sec\theta_m \cos\theta)}{T_N(\sec\theta_m)}
$$

where $T_N(x) = \cos(N \arccos x)$ is the Chebyshev polynomial.

The passband is $\theta_m \le \theta \le \pi - \theta_m$ (where $|\Gamma| \le \Gamma_m$) and:

$$
\theta_m = \arccos\left(\frac{1}{\sec\theta_m}\right) \quad\text{(chebyshev: fixed ripple)}
$$

Fractional bandwidth:

$$
\frac{\Delta f}{f_0} = 2 - \frac{4\theta_m}{\pi}
$$

### 5.4.5 Practical Comparison

| Transformer | Bandwidth | Complexity | Passband ripple |
|-------------|-----------|------------|-----------------|
| Single-section $\lambda/4$ | Narrow | 1 section | None at $f_0$ |
| Binomial (N-section) | Wider as $N\uparrow$ | N sections | Zero at $f_0$, smooth |
| Chebyshev (N-section) | Widest for given $N$ | N sections | Equal ripple |

For a given number of sections $N$, the **Chebyshev** design gives the widest bandwidth, while the **binomial** gives the flattest response.

---

## 5.5 Tapered Transmission Lines

### 5.5.1 Concept

A **tapered line** (also called a **graded transition**) has a continuously varying characteristic impedance $Z(z)$ along its length, providing broadband matching between two real impedances $Z_0$ and $Z_L$.

### 5.5.2 Small-Reflection Theory

For a tapered line with impedance $Z(z)$ varying slowly along length $L$, the total reflection coefficient is approximately:

$$
\Gamma(\theta) \approx \frac{1}{2} \int_0^L e^{-j2\beta z} \frac{d}{dz} [\ln Z(z)] \, dz
$$

where $\theta = \beta L$ and $Z(z)$ varies from $Z(0) = Z_0$ to $Z(L) = Z_L$.

The design problem is to choose $Z(z)$ such that $|\Gamma(\theta)|$ is acceptably small over a desired bandwidth.

### 5.5.3 Exponential Taper

Impedance varies exponentially:

$$
Z(z) = Z_0 e^{az}, \quad a = \frac{1}{L} \ln\left(\frac{Z_L}{Z_0}\right)
$$

Reflection coefficient:

$$
\Gamma(\theta) = \frac{\ln(Z_L/Z_0)}{2} \cdot e^{-j\beta L} \frac{\sin(\beta L)}{\beta L}
$$

Magnitude:

$$
|\Gamma| = \frac{1}{2} \left|\ln\frac{Z_L}{Z_0}\right| \cdot \left|\frac{\sin(\beta L)}{\beta L}\right|
$$

For $\beta L > \pi$, the sinc envelope ensures $|\Gamma|$ decreases as $1/(\beta L)$.

**Bandwidth** for a given $|\Gamma_m|$:

$$
\frac{\Delta f}{f_0} \approx 2 - \frac{4}{\pi} \arcsin\left(\frac{2|\Gamma_m|}{|\ln(Z_L/Z_0)|}\right)
$$

### 5.5.4 Triangular Taper

Impedance derivative follows a triangular function:

$$
\frac{d}{dz}[\ln Z(z)] = 
\begin{cases}
\frac{4}{L^2} \ln\left(\frac{Z_L}{Z_0}\right) \cdot z, & 0 < z < L/2 \\
\frac{4}{L^2} \ln\left(\frac{Z_L}{Z_0}\right) \cdot (L - z), & L/2 < z < L
\end{cases}
$$

Reflection coefficient magnitude:

$$
|\Gamma| = \frac{1}{2} \left|\ln\frac{Z_L}{Z_0}\right| \cdot \left|\frac{\sin(\beta L/2)}{\beta L/2}\right|^2
$$

The decay is $1/(\beta L)^2$ — faster than the exponential taper but with higher sidelobes.

### 5.5.5 Klopfenstein Taper (Optimal)

The **Klopfenstein taper** is the optimal impedance taper in the sense that for a given taper length $L$, it achieves the lowest maximum reflection coefficient in the passband, or equivalently, the shortest length for a given maximum $|\Gamma|$.

It is derived from the Chebyshev transformer in the limit $N \to \infty$ while keeping $\Gamma_m$ constant.

The impedance function:

$$
\ln Z(z) = \frac{1}{2} \ln(Z_0 Z_L) + \frac{\Gamma_0}{\cosh A} A^2 \phi\left(\frac{2z}{L} - 1, A\right)
$$

where $\Gamma_0 = \frac{1}{2} \ln(Z_L/Z_0)$ is the reference mismatch, $A$ is a design parameter related to the maximum passband ripple $\Gamma_m$:

$$
\Gamma_m = \frac{\Gamma_0}{\cosh A}
$$

And $\phi(x, A)$ is defined by:

$$
\phi(x, A) = 
\begin{cases}
\frac{I_0(A\sqrt{1-x^2})}{I_0(A)} \cdot \frac{x}{|x|}, & |x| \le 1 \\
0, & |x| > 1
\end{cases}
$$

where $I_0$ is the modified Bessel function of the first kind.

The **taper length** required for a given $\Gamma_m$:

$$
L = \frac{\lambda_0}{2\pi} \sqrt{A^2 + (\ln(Z_L/Z_0)/2)^2}
$$

**Key properties**:
- Provides **equal ripple** in the passband
- Gives the **shortest taper** for a given maximum reflection coefficient
- Superior to exponential and triangular tapers for a given length

### 5.5.6 Taper Comparison

| Taper | $|\Gamma|$ envelope | Relative length for $\Gamma_m$ |
|-------|-------------------|-------------------------------|
| Exponential | sinc: $1/(\beta L)$ | Longest |
| Triangular | $\text{sinc}^2$: $1/(\beta L)^2$ | Moderate |
| Klopfenstein | Chebyshev-type, equal ripple | Shortest (optimal) |

---

## 5.6 Smith Chart Graphical Design

### 5.6.1 L-Section on Smith Chart

1. Plot normalized load $z_L = Z_L/Z_0$ (or $y_L$)
2. If $z_L$ inside $r=1$ circle: **shunt-first** → add shunt susceptance to rotate on constant-$g$ circle to $g=1$ circle → add series reactance on constant-$r$ circle to center
3. If $z_L$ outside $r=1$ circle: **series-first** → add series reactance to rotate on constant-$r$ circle to $r=1$ circle → add shunt susceptance to center

### 5.6.2 Single Stub on Smith Chart

1. Plot $y_L$ on admittance Smith chart
2. Rotate toward generator on constant-$|\Gamma|$ circle to intersect $g=1$ circle
3. Read $d$ (distance in $\lambda$) and $b(d)$ (normalized susceptance at that point)
4. For the stub: find $l$ such that $b_{\text{stub}} = -b(d)$

### 5.6.3 Double Stub on Smith Chart

1. Load $y_L$ is rotated by distance $d$ to get $y_1$
2. Move on constant-$g$ circle by adding $jb_1$ (stub 1) to reach the rotated $g=1$ circle
3. Rotate by $s$ (fixed stub spacing) to get $y_2$
4. Add $jb_2 = -j \cdot \text{Im}(y_2)$ with stub 2 to reach center

---

## 5.7 Key Formulas Cheat Sheet

| Matching Type | Key Parameters | Formula |
|--------------|----------------|---------|
| L-section (shunt-first, $g_L<1$) | $B, X$ | $B_s = \frac{X_L \pm \sqrt{R_L/Z_0}\sqrt{\Delta}}{R_L^2+X_L^2}$, $X_s = \frac{1}{B_s} + \frac{X_L Z_0}{R_L} - \frac{Z_0}{B_s R_L}$ where $\Delta = R_L^2+X_L^2-Z_0R_L$ |
| L-section (series-first, $g_L\ge1$) | $X, B$ | $X_s = \frac{-X_L \pm \sqrt{\Delta}/\sqrt{R_L/Z_0}}{R_L/Z_0-1}$, $B_s = -\operatorname{Im}[1/(Z_L+jX_s)]$ |
| Single shunt stub | $d, l$ | $\tan(\beta d) = \frac{B_L \pm \sqrt{G_L[(Y_0-G_L)^2+B_L^2]/Y_0}}{G_L - Y_0}$, $l = \frac{\lambda}{2\pi}\arctan(Y_0/B_s)$ |
| Single series stub | $d, l$ | $R(d) = Z_0$ → find $d$, then $l$ from $X_s = -X(d)$ |
| $\lambda/4$ transformer | $Z_1$ | $Z_1 = \sqrt{Z_0 R_L}$ |
| Binomial ($N$ section) | $Z_n$ | $\ln(Z_{n+1}/Z_n) = 2^{-N} C_n^N \ln(R_L/Z_0)$ |
| Exponential taper | $Z(z)$ | $Z(z) = Z_0 e^{az}$, $|\Gamma| = \frac{1}{2}|\ln(R_L/Z_0)| \cdot |\sin(\beta L)/(\beta L)|$ |
| Klopfenstein taper | $Z(z)$ | $\ln Z(z)$ involves $I_0(A\sqrt{1-x^2})$, $\Gamma_m = \Gamma_0/\cosh A$ |

---

## 5.8 Chapter Summary Checklist

| ✅ | Topic | Key Takeaway |
|----|-------|-------------|
| ✓ | L-section LC matching | 2-element network, 8 topologies, narrowband, analytic solution with $\pm$ two options |
| ✓ | Single-stub tuning | Stub length $l$ and position $d$; 4 configurations (shunt/series × short/open) |
| ✓ | Double-stub tuning | Fixed stub spacing, only stub lengths variable, has forbidden region |
| ✓ | $\lambda/4$ transformer | $Z_1 = \sqrt{Z_0 R_L}$, bandwidth limited, N-section for wider BW |
| ✓ | Exponential taper | $Z(z) = Z_0 e^{az}$, $|\Gamma| \propto \text{sinc}(\beta L)$ |
| ✓ | Klopfenstein taper | Optimal taper: shortest length for given $\Gamma_m$, equal-ripple response |
| ✓ | Smith chart design | Graphical approach for all matching types; constant-$r$, constant-$g$ circles |

---

## References

1. D. M. Pozar, *Microwave Engineering*, 4th ed., Wiley, 2012, Chapter 5.
2. P. H. Smith, "Transmission Line Calculator," *Electronics*, vol. 12, no. 1, pp. 29–31, Jan. 1939.
3. R. W. Klopfenstein, "A Transmission Line Taper of Improved Design," *Proc. IRE*, vol. 44, pp. 31–35, Jan. 1956.
4. R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., Wiley-IEEE Press, 2001, Ch. 5.
5. R. Levy, "Tables of Element Values for the Distributed Low-Pass Prototype Filter," *IEEE Trans. Microwave Theory Tech.*, vol. MTT-13, pp. 514–536, Sept. 1965.
6. G. L. Matthaei, L. Young, E. M. T. Jones, *Microwave Filters, Impedance Matching Networks, and Coupling Structures*, Artech House, 1980.

---

## Appendix: Selected Derivations

### A.1 Bandwidth of L-Section

For the L-section (shunt $B_0$, series $X_0$ at $f_0$), off-resonance:

$$
\Gamma = \frac{Z_{\text{in}} - Z_0}{Z_{\text{in}} + Z_0}
$$

where $Z_{\text{in}} = jX + \frac{1}{jB + Y_L}$. At $f_0$: $\Gamma = 0$ (perfect match).

For small frequency deviations $\Delta f$:

$$
|\Gamma| \approx \frac{\sqrt{(X_0 \Delta\omega)^2 - (B_0 Z_0 \Delta\omega)^2}}{2Z_0 + \dots}
$$

Bandwidth (VSWR-based): $\Delta f / f_0 \approx 2/Q_L$.

### A.2 Single-Stub Analytical Solution

Derivation of $\tan(\beta d)$:

At distance $d$ from load:
$$Y(d) = Y_0 \frac{Y_L + jY_0 t}{Y_0 + jY_L t}, \quad t = \tan(\beta d)$$

$$G(d) = Y_0 \frac{G_L(1 + t^2)}{(Y_0 - B_L t)^2 + (G_L t)^2}$$

Set $G(d) = Y_0$:

$$G_L(1 + t^2) = (Y_0 - B_L t)^2 + G_L^2 t^2$$

$$G_L + G_L t^2 = Y_0^2 - 2Y_0 B_L t + B_L^2 t^2 + G_L^2 t^2$$

$$(G_L - B_L^2 - G_L^2)t^2 + 2Y_0 B_L t + (G_L - Y_0^2) = 0$$

This gives a quadratic in $t$ with two solutions (two intersection points with $g=1$ circle).

### A.3 Double-Stub Forbidden Region Derivation

The admittance at stub 2, after rotating $y_1 + jb_1$ by $\theta = \beta s$:

$$y_2 = \frac{(y_1 + jb_1) + j\tan\theta}{1 + j(y_1 + jb_1)\tan\theta}$$

For matchability, we need $y_2$ to reach center after adding $jb_2$. This requires $\text{Re}(y_2) = 1$, which leads to the condition $g_1 \le 1/\sin^2\theta$.

<!-- 完成于 2026-04-29 11:56 CST -->

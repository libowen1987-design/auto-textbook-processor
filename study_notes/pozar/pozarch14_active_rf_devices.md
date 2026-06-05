# Pozar Ch14 (4e Ch11) — Active RF Devices

> **Note:** This chapter corresponds to **Chapter 11** in Pozar *Microwave Engineering*, 4th Edition.
> Covers semiconductor diodes, bipolar and field-effect transistors, and microwave integrated circuits (MICs) used in active RF/microwave systems.

---

## §11.1 Microwave Diodes

### §11.1.1 Schottky Barrier Diode

A **Schottky diode** uses a metal-semiconductor junction (rather than a P-N junction) for majority-carrier conduction. It has no minority carrier storage → very fast switching.

**I-V Characteristic:**

$$
I(V) = I_S \left( e^{qV / \eta k T} - 1 \right) \quad [\text{A}]
$$

where:
- $I_S$ = **saturation current** [A] — determined by barrier height $\phi_B$ and area
- $q = 1.602 \times 10^{-19}$ C — electron charge
- $\eta$ = **ideality factor** (1.02–1.10 for good Schottky, vs. ~2 for PN junction)
- $k = 1.38 \times 10^{-23}$ J/K — Boltzmann constant
- $T$ = temperature [K]

> **量纲检查:** $qV$ [C·V = J], $\eta k T$ [J] ⇒ 指数无量纲 ✓

**Barrier height:** $\phi_B$ [V] is the potential barrier seen by electrons from semiconductor to metal:
- Si: $\phi_B \approx 0.5$–0.7 V (n-type)
- GaAs: $\phi_B \approx 0.7$–0.9 V (n-type)

**Saturation current:**

$$
I_S = A A^{**} T^2 e^{-q\phi_B / kT} \quad [\text{A}]
$$

where $A$ = junction area [m²], $A^{**} \approx 110$ A/(cm²·K²) for Si (Richardson constant).

**Equivalent circuit:**

```
          C_j
    ----||----+----
    |          |
    R_s        R_j(V)  (nonlinear junction resistance)
    |          |
    ----+------+----
```

- $R_s$ = **series resistance** [$\Omega$] — ohmic contact + undepleted epi-layer (typically 1–10 $\Omega$)
- $R_j(V)$ = **junction resistance** [$\Omega$] — nonlinear, from I-V slope:
  $$
  R_j = \frac{\eta k T}{q (I + I_S)} \approx \frac{\eta k T}{q I} \quad \text{(forward bias)}
  $$
- $C_j(V)$ = **junction capacitance** [F]:
  $$
  C_j(V) = \frac{C_{j0}}{(1 - V/\phi_B)^\gamma}
  $$
  where $\gamma \approx 0.5$ for abrupt junction, $\gamma \approx 0.33$ for hyper-abrupt.

**Schottky diode cutoff frequency:**

$$
f_c = \frac{1}{2\pi R_s C_{j0}} \quad [\text{Hz}]
$$

> For mixer/ detector applications: $f_c \gg f_{\text{operating}}$. Good Schottky mixer diodes have $f_c > 1000$ GHz.

**Applications:**
- **Mixer diodes:** Low $C_j$, low $R_s$ for high cutoff frequency
- **Detector diodes:** High sensitivity (large $\Delta I$ per small RF power)
- **Switching:** Fast (~ps) switching time

---

### §11.1.2 PIN Diode

A PIN diode has an **intrinsic (I) region** sandwiched between P⁺ and N⁺ layers. The I-region gives it unique properties at microwave frequencies.

**DC I-V:** Similar to a PN junction rectifier in forward bias.

**RF Impedance Model:**

The PIN diode behaves as a **current-controlled resistor** at RF frequencies when forward-biased.

- **Forward bias** ($I_f > 0$): The I-region is flooded with carriers → low impedance:
  $$
  R_f \approx \frac{W^2}{(\mu_n + \mu_p) \tau Q_0} \quad \text{or} \quad R_f \approx \frac{W^2}{2\mu \tau I_f}
  $$
  More practically: $R_f \approx \frac{K}{I_f^m}$ where $K$ and $m$ are empirical constants.
  Typical: $R_f \approx 1$–$5\ \Omega$ at $I_f = 10$–$100$ mA.

- **Reverse bias** ($V_R < 0$): I-region is depleted → very low capacitance → high impedance:
  $$
  C_R \approx \frac{\epsilon A}{W} \quad [\text{F}]
  $$
  where $W$ = I-region width [m], $A$ = area [m²].
  Typical: $C_R \approx 0.02$–$2$ pF.

**Key Parameters:**
- **I-layer thickness** $W$: Determines breakdown voltage and switching speed
  - Thin ($W \approx 5$–$50\ \mu$m): fast switching, lower breakdown
  - Thick ($W \approx 100$–$500\ \mu$m): high power handling, slower
- **Carrier lifetime** $\tau$ [s]: Determines how long the I-region stays conductive after forward bias is removed. Longer $\tau$ = lower RF resistance for the same bias current.

**Applications:**
- **RF Switch:** Forward = ON (low loss), Reverse = OFF (high isolation)
  - SPST, SPDT, DPDT configurations
  - Isolation: 20–50 dB, Insertion loss: 0.1–1 dB
- **Voltage-Variable Attenuator:** Varying $I_f$ changes $R_f$ continuously
- **Phase Shifter:** PIN diodes switch between different delay paths
- **Limiter:** Self-biasing PIN structure for receiver protection

> **Engineering intuition:** A PIN diode is like a "valve" for RF — a small DC current controls a large RF signal. The I-region stores charge during positive half-cycles and releases it during negative half-cycles, smoothing the RF cycle and acting as a linear resistor.

---

### §11.1.3 Varactor Diode

A **varactor (variable reactor)** diode uses a reverse-biased PN or Schottky junction whose depletion capacitance varies with bias voltage.

**C-V Characteristic:**

$$
C_j(V) = \frac{C_{j0}}{(1 + V_R / V_{bi})^\gamma} \quad [\text{F}]
$$

where:
- $C_{j0}$ = zero-bias junction capacitance [F]
- $V_R$ = reverse bias voltage [V] (positive magnitude)
- $V_{bi}$ = built-in potential [V] (~0.8 V for Si, ~1.2 V for GaAs)
- $\gamma$ = **grading coefficient**:
  - $\gamma = 0.5$ → **abrupt junction** (most common)
  - $\gamma = 0.33$ → linearly graded junction
  - $\gamma > 0.5$ → **hyper-abrupt junction** (for wide tuning range, e.g., VCO)

> **量纲检查:** $C_{j0}$ [F], $(1 + V_R/V_{bi})^{-\gamma}$ 无量纲 ⇒ $C_j$ [F] ✓

**Tuning ratio:**

$$
R = \frac{C_j(V_R = 0)}{C_j(V_R = V_{\max})} = \left(1 + \frac{V_{\max}}{V_{bi}}\right)^\gamma
$$

**Quality factor (Q):**

$$
Q = \frac{1}{2\pi f R_s C_j(V)} \quad \text{at operating frequency } f
$$

Typical: $Q \approx 100$–$1000$ at VHF, drops to $Q \approx 10$–$100$ at microwave frequencies.

**Applications:**
- **VCO tuning:** Varactor in resonator tank circuit changes oscillation frequency
- **Phase shifters:** Varactor-loaded transmission lines (reflection-type)
- **Parametric amplifiers** (historically important, now rare)
- **Voltage-controlled filters**

**Frequency tuning (LC resonator):**

$$
f_0(V) = \frac{1}{2\pi \sqrt{L C_j(V)}} \quad [\text{Hz}]
$$

| Application | $\gamma$ | Tuning Range | Typical $C_{j0}$ |
|---|---|---|---|
| VCO (wideband) | 0.5–1.0 (hyper-abrupt) | 2:1 to 10:1 | 0.5–10 pF |
| VCO (narrowband) | 0.5 (abrupt) | 1.5:1 to 3:1 | 1–20 pF |
| Phase shifter | 0.5 | variable | 0.2–2 pF |

---

### §11.1.4 Tunnel Diode

The **tunnel (Esaki) diode** uses heavy doping ($N_D, N_A > 10^{19}$ cm⁻³) to create a very thin depletion region where **quantum tunneling** dominates.

**I-V Characteristic:**
```
  I
  ↑
  |     ┌─── peak current I_P at V_P
  |    /
  |   /  ← negative differential resistance (NDR) region
  |  /        ── valley current I_V at V_V
  | / 
  |/_________________→ V
```

**Key parameters:**
- $I_P$ = peak current [A], $V_P$ = peak voltage [V] (~50–150 mV for Ge, ~100–300 mV for GaAs)
- $I_V$ = valley current [A], $V_V$ = valley voltage [V] (~300–500 mV)
- Peak-to-valley current ratio (PVCR): $I_P/I_V$ — typical 3:1 to 15:1
- **Negative differential resistance (NDR):**
  $$
  -R_n = \frac{V_V - V_P}{I_P - I_V} \quad [\Omega]
  $$

**Small-signal equivalent circuit (biased in NDR region):**

```
         -R_n
    ----/\/\/\----||----+
    |             C_j    |
    +--/\/\/\----------  |
      R_s               L_p
                        ---
```

- $-R_n$ = negative resistance (typically −10 to −100 $\Omega$)
- $C_j$ = junction capacitance (~1–100 pF)
- $R_s$ = series resistance (~1–10 $\Omega$)
- $L_p$ = package inductance (~0.1–1 nH)

**Self-resonant frequency** (where net reactance = 0):
$$
f_r = \frac{1}{2\pi} \sqrt{\frac{1}{L_p C_j} - \frac{R_s^2}{L_p^2}}
$$

**Applications:**
- **Oscillators** (up to ~100 GHz)
- **Switching** (ultra-fast, ~ps)
- **Amplifiers** (narrowband, limited but simple)

> **Limitations:** Low power output (~mW), limited to ~100 GHz due to parasitic effects.

---

### §11.1.5 Gunn Diode (Transferred Electron Device)

The **Gunn diode** uses the **transferred electron effect** (Gunn effect) in certain III-V semiconductors (GaAs, InP) where electrons transfer from a high-mobility, low-mass conduction band valley to a low-mobility, high-mass valley under high electric field.

**Negative Differential Mobility:**

At a threshold field $E_{th}$:
- Below $E_{th}$: $\mu_1 \approx 6000$ cm²/V·s (GaAs), high mobility
- Above $E_{th}$: $\mu_2 \approx 1000$ cm²/V·s (GaAs), low mobility

The **drift velocity** $v_d$ peaks at $E_{th}$ then decreases, giving:
$$
\frac{dv_d}{dE} < 0 \quad \Rightarrow \quad \sigma = q n \frac{dv_d}{dE} < 0
$$

This is a **bulk negative resistance** (not a junction effect).

**Threshold field:**
- GaAs: $E_{th} \approx 3.2$ kV/cm
- InP: $E_{th} \approx 10.5$ kV/cm
- InGaAs: $E_{th} \approx 3.0$ kV/cm

**Dipole Domain Formation:**

Above $E_{th}$, a **dipole domain** forms — a narrow high-field region that travels from cathode to anode at the saturation velocity $v_s$:

```
 Cathode                 Anode
    |                       |
    ++-------[++++---]------+
               ↑ dipole domain (high E field)
```

- Domain moves at $v_s \approx 10^7$ cm/s (GaAs)
- Domain **transit time**: $\tau_t = L / v_s$ [s]

**Transit Time Frequency:**

$$
f_t = \frac{v_s}{L} \quad [\text{Hz}]
$$

For GaAs ($v_s \approx 10^7$ cm/s):
- $L = 10\ \mu$m → $f_t \approx 10$ GHz
- $L = 2\ \mu$m → $f_t \approx 50$ GHz
- $L = 1\ \mu$m → $f_t \approx 100$ GHz

**Operating Modes:**

| Mode | Bias | Efficiency | Frequency |
|---|---|---|---|
| **Gunn (transit-time)** | $V \approx 2\text{–}3\times V_{th}$ | 2–7% | Near $f_t$ |
| **LSA (Limited Space-charge Accumulation)** | High $V$, high $f$ | 10–20% | $\gg f_t$ |
| **Delayed domain** | Resonant circuit | 5–10% | Below $f_t$ |
| **Quenched domain** | Resonant circuit | 5–10% | Above $f_t$ |

**Applications:**
- **Gunn oscillators** (VCOs) up to 100+ GHz
- **Doppler radar** (speed sensors, motion detectors)
- **Frequency sweep generators** for FMCW radar

> **Engineering intuition:** A Gunn diode is a slice of GaAs that generates microwaves directly from DC. No junction needed — just bulk material plus a DC bias above threshold. The oscillating current arises from domains forming and disappearing.

---

### §11.1.6 IMPATT Diode

**IMPATT** = **IMP**act ionization **A**valanche **T**ransit **T**ime.

Structure: N⁺-P-I-P⁺ or similar, with an **avalanche region** + **drift region**.

**Operating Principle:**
1. Reverse bias above breakdown → **avalanche multiplication** generates carrier plasma
2. Carriers **drift** through the I-region at saturation velocity $v_s$
3. The **transit time delay** between avalanche current and terminal voltage produces **negative resistance**

**Two Regions:**
- **Avalanche region** (width $x_a$): Impact ionization occurs, current builds up
- **Drift region** (width $x_d$): Carriers drift at $v_s$, inducing current in the external circuit

**Transit Angle:**

$$
\theta = \omega \tau_d = \omega \frac{x_d}{v_s}
$$

Maximum negative resistance occurs when $\theta \approx \pi$ ($\tau_d \approx T/2$):

$$
f_{\text{design}} \approx \frac{v_s}{2 x_d} \quad [\text{Hz}]
$$

**Small-Signal Impedance:**

The IMPATT diode exhibits a **negative resistance** that varies with frequency. The equivalent circuit includes:

$$
Z_d = R_d(f) + j X_d(f) \quad \text{with } R_d < 0 \text{ over a frequency band}
$$

**DC-to-RF Conversion Efficiency:**

$$
\eta \approx \frac{1}{\pi} \cdot \frac{V_d}{V_a} \quad \text{(theoretical)}
$$

where:
- $V_d$ = voltage drop across drift region [V]
- $V_a$ = breakdown voltage across avalanche region [V]
- For optimized design: $\eta \approx 15$–$30\%$ (practical)
- Si IMPATT: up to 20% at X-band
- GaAs IMPATT: up to 25% at X-band

**Key Parameters:**
- Avalanche frequency (where susceptance = 0): $f_a \approx \frac{1}{2\pi}\sqrt{\frac{2\alpha' v_s J_0}{\epsilon}}$
- Operating frequency range: $f_a$ to $3f_a$
- Output power: up to 10 W at X-band, ~1 W at W-band

**Comparison with Gunn Diode:**

| Parameter | Gunn | IMPATT |
|---|---|---|
| Mechanism | Transferred electron | Avalanche + transit time |
| Efficiency | 2–10% | 15–30% |
| Operating voltage | 3–15 V | 30–100 V |
| Output power | Low-moderate | High |
| Noise | **Low** (quieter) | **High** (noisy — avalanche is random) |
| Frequency | Up to >150 GHz | Up to >300 GHz |

> **Engineering intuition:** The IMPATT diode creates negative resistance through a clever timing trick — the avalanche current pulse arrives a half-cycle after the voltage peak, so the diode absorbs power at the right phase to sustain oscillation.

---

## §11.2 Bipolar Junction Transistor (BJT)

### §11.2.1 High-Frequency Hybrid-π Model

The small-signal equivalent circuit for a BJT at microwave frequencies extends the low-frequency hybrid-π model with parasitic elements:

```
           C_μ (Miller)
    B o---/\/\/---o---o C
         R_b       |   |
                   |   |
    +---/\/\/--+  C_π  +--- g_m V_π ---+
    |   R_π    |   |   |               |
    o          o---+   o               o
    |          |                      |
    o----------+----------------------+
    E o---L_e---o
```

**Elements:**
- $R_b$ = **base resistance** [$\Omega$] — includes contact + spreading resistance (typically 1–20 $\Omega$)
- $R_\pi$ = **base-emitter junction resistance** [$\Omega$] — $R_\pi = \beta_0 / g_m$
- $C_\pi$ = **base-emitter capacitance** [F] = $C_{je} + C_{de}$ (junction + diffusion)
- $C_\mu$ = **base-collector capacitance** [F] (Miller capacitance) — typically 0.01–1 pF
- $g_m$ = **transconductance** [S]:
  $$
  g_m = \frac{q I_C}{k T} \approx \frac{I_C}{V_T} \quad \text{where } V_T = kT/q \approx 25\ \text{mV at 290 K}
  $$
- $r_o$ = **output resistance** [$\Omega$] — $r_o = V_A / I_C$ (Early voltage)
- $L_e$ = **emitter inductance** [H] — package/connection parasitic (~0.1–1 nH)

**Unity Current Gain Frequency ($f_T$):**

$$
f_T = \frac{g_m}{2\pi(C_\pi + C_\mu)} \quad [\text{Hz}]
$$

$f_T$ is the frequency where the **short-circuit current gain** $h_{21}$ drops to unity (0 dB).

> **量纲检查:** $g_m$ [S = A/V = 1/$\Omega$], $C_\pi + C_\mu$ [F = A·s/V] ⇒ $f_T$ = [V/A] / [A·s/V] = 1/s = Hz ✓

**Maximum Oscillation Frequency ($f_{\max}$):**

$$
f_{\max} = \sqrt{\frac{f_T}{8\pi R_b C_\mu}} \quad [\text{Hz}]
$$

$f_{\max}$ is the frequency where the **maximum available gain** (MAG) drops to unity (0 dB).

> **量纲检查:** $f_T$ [Hz], $R_b$ [$\Omega$], $C_\mu$ [F] ⇒ $\frac{f_T}{R_b C_\mu}$ [Hz / ($\Omega$·F)] = [Hz / s] = [Hz²] ⇒ sqrt → Hz ✓

**Typical values (modern SiGe HBT):**
- $f_T$: 200–500 GHz
- $f_{\max}$: 250–600 GHz
- $R_b$: 5–20 $\Omega$
- $C_\mu$: 5–50 fF
- $\beta_0$: 100–500

**Gain-Bandwidth Product Relationship:**

$$
f_T \approx \frac{f}{|\beta(f)|} \quad \text{when } f \gg f_\beta = \frac{f_T}{\beta_0}
$$

where $|\beta(f)|$ is the magnitude of the current gain at frequency $f$.

---

### §11.2.2 S-Parameter Description

For microwave BJTs, S-parameters are used instead of hybrid-π elements because they are directly measurable:

$$
[S] = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix}
$$

- $S_{11}$: Input reflection coefficient (input match)
- $S_{21}$: Forward gain (transmission)
- $S_{12}$: Reverse isolation
- $S_{22}$: Output reflection coefficient (output match)

**Stability:**

The stability factor (Rollett):

$$
K = \frac{1 - |S_{11}|^2 - |S_{22}|^2 + |\Delta|^2}{2|S_{12}S_{21}|} > 1 \quad \text{(unconditionally stable)}
$$

where $\Delta = S_{11}S_{22} - S_{12}S_{21}$.

**Unilateral Figure of Merit:**

$$
U = \frac{|S_{11}||S_{12}||S_{21}||S_{22}|}{(1 - |S_{11}|^2)(1 - |S_{22}|^2)}
$$

If $U \ll 1$, the device can be treated as unilateral ($S_{12} \approx 0$), greatly simplifying matching network design.

**Maximum Available Gain (MAG):**

$$
\text{MAG} = \frac{|S_{21}|}{|S_{12}|} \left( K - \sqrt{K^2 - 1} \right) \quad \text{[linear]}
$$

in dB: $\text{MAG}_{\text{dB}} = 10 \log_{10} \text{MAG}$

**Mason's Invariant ($U'$):** A device figure of merit invariant to lossless embeddings:

$$
U' = \frac{|S_{21} - S_{12}|^2}{4(|S_{11}||S_{22}| - |S_{12}||S_{21}|)}
$$

---

## §11.3 Field Effect Transistors (FETs)

### §11.3.1 MESFET / HEMT Small-Signal Equivalent Circuit

**MESFET** (Metal-Semiconductor FET) and **HEMT** (High-Electron-Mobility Transistor) share a similar small-signal model:

```
     C_gd
    ---||---
G o--+      +----+--o D
     |      |    |
     C_gs  R_i   g_m V_gs e^{-jωτ}
     |      |    |
     -----+-+---+
          R_ds
          |
     R_s  |
E o--/\/\-+--------o S
```

**Model Elements:**

| Element | Symbol | Description | Units | Typical Range |
|---|---|---|---|---|
| Transconductance | $g_m$ | Channel current control | S (mS) | 50–500 mS/mm |
| Gate-source capacitance | $C_{gs}$ | Input capacitance | F | 0.1–1 pF |
| Gate-drain capacitance | $C_{gd}$ | Miller feedback cap | F | 0.01–0.1 pF |
| Channel resistance | $R_i$ | Intrinsic channel resistance | $\Omega$ | 1–5 $\Omega$ |
| Output resistance | $R_{ds}$ | Drain-source resistance | $\Omega$ | 100–1000 $\Omega$ |
| Transit time | $\tau$ | Channel transit delay | s | 0.5–5 ps |
| Gate resistance | $R_g$ | Gate metallization resistance | $\Omega$ | 1–10 $\Omega$ |
| Source resistance | $R_s$ | Source contact resistance | $\Omega$ | 1–5 $\Omega$ |
| Drain resistance | $R_d$ | Drain contact resistance | $\Omega$ | 1–5 $\Omega$ |

**Unity Current Gain Frequency:**

$$
f_T = \frac{g_m}{2\pi(C_{gs} + C_{gd})} \quad [\text{Hz}]
$$

For HEMT devices, a simpler approximation:
$$
f_T \approx \frac{v_s}{2\pi L_g} \quad [\text{Hz}]
$$
where $v_s$ = saturation velocity (~$1.5 \times 10^7$ cm/s for InGaAs), $L_g$ = gate length [m].

> **量纲检查:** $g_m$ [S], $C_{gs}+C_{gd}$ [F] ⇒ $S/F = (A/V)/(C/V·s) = 1/s = Hz$ ✓

**Maximum Oscillation Frequency:**

$$
f_{\max} = \frac{f_T}{2\sqrt{2\pi f_T R_g C_{gd} + g_m R_g \frac{C_{gd}}{C_{gs}}}}
$$

A common simplified form:
$$
f_{\max} \approx \sqrt{\frac{f_T}{8\pi R_g C_{gd}}} \quad \text{(similar to BJT form)}
$$

**Typical values (state-of-the-art HEMT):**
- GaAs pHEMT: $f_T \approx 150$–$250$ GHz, $f_{\max} \approx 300$–$500$ GHz
- InP HEMT: $f_T \approx 400$–$700$ GHz, $f_{\max} \approx 800$–$1200$ GHz
- GaN HEMT: $f_T \approx 50$–$150$ GHz, $f_{\max} \approx 100$–$400$ GHz (high power)

---

### §11.3.2 Nonlinear FET Model (Curtice Model)

For large-signal operation (power amplifiers, mixers), the Curtice or TOM (TriQuint Own Model) nonlinear model is used:

**Drain current (Curtice quadratic model):**

$$
I_{ds}(V_{gs}, V_{ds}) = \beta (V_{gs} - V_T)^2 (1 + \lambda V_{ds}) \tanh(\alpha V_{ds})
$$

where:
- $\beta$ = transconductance parameter [A/V²]
- $V_T$ = threshold voltage [V]
- $\lambda$ = channel-length modulation parameter [1/V]
- $\alpha$ = saturation voltage parameter [1/V]

**Gate-source capacitance (nonlinear):**

$$
C_{gs}(V_{gs}) = \frac{C_{gs0}}{\sqrt{1 - V_{gs}/V_{bi}}}
$$

**Gate-drain capacitance (nonlinear):**

$$
C_{gd}(V_{gd}) = \frac{C_{gd0}}{\sqrt{1 - V_{gd}/V_{bi}}}
$$

**Transit time delay** $\tau$ accounts for the channel transit time (typically 1–5 ps), included as $e^{-j\omega\tau}$ in the transconductance term.

---

### §11.3.3 Technology Comparison: BJT vs MESFET vs HEMT

| Parameter | Si BJT | SiGe HBT | GaAs MESFET | GaAs pHEMT | InP HEMT | GaN HEMT |
|---|---|---|---|---|---|---|
| $f_T$ [GHz] | 50–100 | 200–500 | 50–120 | 150–250 | 400–700 | 50–150 |
| $f_{\max}$ [GHz] | 50–100 | 250–600 | 80–150 | 300–500 | 800–1200 | 100–400 |
| Noise Figure [dB] @ 10 GHz | 1.0–2.0 | 0.5–1.0 | 0.6–1.2 | 0.3–0.6 | 0.2–0.4 | 0.5–1.5 |
| Output Power | Low | Medium | Medium | Medium | Low | **Very High** |
| $V_{\text{breakdown}}$ | 1–3 V | 1.5–3 V | 8–15 V | 5–10 V | 2–5 V | **30–200 V** |
| $1/f$ corner | 1–100 kHz | 1–10 kHz | 10–100 MHz | 1–100 MHz | 10–100 MHz | 1–10 MHz |

> **Engineering intuition:** Choose by application — HEMT for low-noise, GaN for high-power, SiGe for high-integration/digital-friendly, InP for absolute highest frequency.

---

## §11.4 Microwave Integrated Circuits (MICs)

### §11.4.1 Types of MICs

| Feature | **Hybrid MIC** | **Monolithic MIC (MMIC)** |
|---|---|---|
| Substrate | Alumina, quartz, Duroid | Semiconductor (GaAs, Si, InP) |
| Active devices | Bonded (chip-and-wire) | Grown in-situ on the chip |
| Passive components | Printed/external | On-chip (MIM caps, spiral inductors) |
| Assembly | Manual/automated bonding | Photolithographic (batch) |
| Cost (low volume) | Lower | Higher (mask costs) |
| Cost (high volume) | Higher | **Very low per chip** |
| Frequency limit | Up to ~100 GHz | Up to ~300+ GHz |
| Size | Larger | **Very compact** |
| Tuning | Possible (trim, replace) | **Not possible** (fixed) |

### §11.4.2 Transmission Lines for MICs

**Microstrip (most common):**

```
    W
  ----+----     Top metal (conductor)
  ============= Dielectric (ε_r)
  ------------- Ground plane
```

- Effective permittivity: $1 < \epsilon_{r,\text{eff}} < \epsilon_r$
- Characteristic impedance $Z_0$: 20–120 $\Omega$ typical
- Loss: conductor loss + dielectric loss

**Coplanar Waveguide (CPW):**

```
  G       S       G
  ================ Top metal
  ====||======||==== (gaps)
  ================ 
```

- No via holes needed! All conductors on top plane
- $Z_0$ controlled by center strip width $S$ and gap $G$
- Better for flip-chip and probe-based testing

**Other lines:**
- **Stripline:** Center conductor embedded in dielectric between two ground planes
- **Slotline:** Slot in ground plane on one side
- **Finline:** Slot in waveguide broad wall (mm-wave)

### §11.4.3 On-Chip Passive Components (MMIC)

**Resistors:**
- **Thin-film:** NiCr or TaN (50–200 $\Omega$/square), most accurate
- **Mesa (semiconductor):** GaAs epi-layer (100–500 $\Omega$/square), lower tolerance
- **Thick-film:** Screen-printed (hybrid only)

**Capacitors:**
- **MIM (Metal-Insulator-Metal):** SiN/SiO₂ dielectric, ~100–500 pF/mm²
- **Interdigital:** Finger capacitor, smaller values (~0.01–1 pF)
- **Metal-finger:** In MMIC multilayers

**Inductors:**
- **Spiral inductor:** Circular or rectangular, $L \approx 0.1$–$10$ nH
  - Limitations: Self-resonance frequency, series resistance, substrate losses
  - $Q \approx 10$–$30$ at microwave frequencies (Si is worse than GaAs)
- **Short transmission line:** High-impedance line stub

**Via holes:** Connect top-side elements to ground plane. Inductance ~0.01–0.1 nH for small vias.

### §11.4.4 Fabrication Basics

**Hybrid MIC process:**
1. Substrate preparation (polish, clean)
2. Thin-film deposition (Cr, NiCr, TiW, Au) — sputtering/evaporation
3. Photolithography + wet/dry etching
4. Laser drilling for via holes
5. Component attachment (epoxy or solder)
6. Wire bonding (Au or Al wedge bonding)
7. Testing and tuning

**MMIC process:**
1. Substrate growth (MBE or MOCVD) — active epitaxial layers
2. Device isolation (mesa etching or ion implantation)
3. Gate formation (Schottky contact definition, typically e-beam lithography for sub-$\mu$m gates)
4. Ohmic contacts (N⁺ regions + metal)
5. Passive components (MIM capacitors, spiral inductors)
6. Air bridges (crossovers)
7. Backside processing (thinning to 50–100 $\mu$m, via etching)
8. Dicing and sort testing

---

## Summary — Key Formulas

| Quantity | Formula | Units |
|---|---|---|
| Schottky I-V | $I = I_S(e^{qV/\eta kT} - 1)$ | A |
| Schottky cutoff freq | $f_c = 1/(2\pi R_s C_{j0})$ | Hz |
| PIN forward resistance | $R_f \approx K / I_f^m$ | $\Omega$ |
| Varactor C-V | $C_j(V) = C_{j0}/(1 + V_R/V_{bi})^\gamma$ | F |
| Varactor Q | $Q = 1/(2\pi f R_s C_j)$ | — |
| Gunn transit freq | $f_t = v_s / L$ | Hz |
| IMPATT efficiency | $\eta \approx (1/\pi) \cdot V_d/V_a$ | — |
| BJT $f_T$ | $f_T = g_m / [2\pi(C_\pi + C_\mu)]$ | Hz |
| BJT $f_{\max}$ | $f_{\max} = \sqrt{f_T/(8\pi R_b C_\mu)}$ | Hz |
| FET $f_T$ | $f_T = g_m / [2\pi(C_{gs} + C_{gd})]$ | Hz |
| FET $f_{\max}$ | $f_{\max} \approx \sqrt{f_T/(8\pi R_g C_{gd})}$ | Hz |
| Hyb vs MMIC | Hybrid = chip+wire, MMIC = monolithic integration | — |

---

## References

- Pozar, D.M., *Microwave Engineering*, 4th Ed., Chapter 11
- Bahl, I. & Bhartia, P., *Microwave Solid State Circuit Design*, 2nd Ed.
- Sze, S.M. & Ng, K.K., *Physics of Semiconductor Devices*, 3rd Ed.
- Gonzalez, G., *Microwave Transistor Amplifiers*, 2nd Ed.
- Vendelin, G.D. et al., *Microwave Circuit Design Using Linear and Nonlinear Techniques*
- Curtice, W.R., "A MESFET Model for Use in the Design of GaAs Integrated Circuits," *IEEE T-MTT*, 1980

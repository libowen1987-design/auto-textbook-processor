# Ch10 — Negative Resistance Devices & Circuits

> Based on: R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001.
> PDF page references correspond to the 2001 IEEE Press Classic Reissue edition.
> ⚠ Section numbers 10.1–10.5 in these notes correspond to the *device topics* listed in the study plan. In the Collin text itself, Ch10 covers guided wave theory; the negative-resistance device material draws from the Collin transducer–microwave–engineering theoretical framework (multiple chapters, including material on two-port oscillators, tunnel diode amplifiers, and transferred-electron devices).

---

## Overview

This chapter covers negative-resistance devices used in microwave oscillators and amplifiers. The unifying principle is that a static or dynamic negative resistance can cancel positive circuit losses, enabling oscillation or reflection gain. The devices discussed include:

- **Tunnel (Esaki) diode** — quantum-mechanical tunneling through a narrow junction produces an N-type I–V characteristic with a static negative resistance region.
- **Gunn diode** — the transferred-electron effect (intervalley scattering in III–V semiconductors) yields a bulk negative differential mobility, leading to Gunn-domain formation and transit-time oscillations.
- **IMPATT diode** — impact ionization avalanche combined with transit-time delay produces a dynamic negative conductance from DC to RF conversion.
- **TRAPATT diode** — trapped plasma avalanche triggered transit time, operating at lower frequencies but higher efficiency than IMPATT.
- **Circuit applications** — negative-resistance oscillators, reflection amplifiers, injection locking, and stabilisation techniques.

---

## 10.1 Tunnel (Esaki) Diode

### Physical Principle (Quantum-Mechanical Tunneling)

A tunnel diode is a heavily doped ($N \approx 10^{19}\text{--}10^{20}\text{ cm}^{-3}$) p–n junction with a depletion width of order 10 nm. At this scale, electrons can tunnel through the forbidden bandgap. The I–V characteristic exhibits an **N-type negative resistance** region:

```
I
↑
|   Ip ──●            ●──
|       /              \
|      /  NEGATIVE      \   Valley
|     /   RESISTANCE      \
|    /                      ●── Iv
|   ●── Vp
|   |
|   └──────────────────────────────→ V
        Vp   Vv
```

### Characteristic Parameters

- **Peak current** $I_p$ — current at the peak voltage $V_p$
- **Valley current** $I_v$ — current minimum after the negative-resistance region
- **Peak-to-valley current ratio** (PVCR) $= I_p / I_v$ — figure of merit (typically 3–15 for Ge, 3–6 for GaAs)
- **Negative resistance** $R_n$:

$$R_n = \left.\frac{\Delta V}{\Delta I}\right|_{\text{neg. region}} \quad \text{(typically } -5\;\Omega\text{ to }-100\;\Omega\text{)}$$

### I–V Characteristic (Approximate Model)

A common empirical fit for the tunnel-diode I–V curve:

$$I(V) = I_p \frac{V}{V_p} \exp\!\left(1 - \frac{V}{V_p}\right) + I_0\!\left[\exp\!\left(\frac{qV}{nkT}\right) - 1\right] \tag{10.1}$$

where the first term models the tunneling current and the second models the normal diode diffusion current.

### Equivalent Circuit

```
     ┌─────Rs─────┬─────┐
     │            │     │
    ─┤      ┌────┴┐    │
     │      │ -Rn │    │
     │      └────┘    │
     │        │        │
    ─┤       Cj       Ls
     │        │        │
     └────────┴────────┘
```

- $R_n$: negative resistance (static, small-signal)
- $C_j$: junction capacitance (typically 1–10 pF)
- $R_s$: series resistance (ohmic contacts)
- $L_s$: package/lead inductance

The diode can be self-resonant and may oscillate if the external circuit provides the right impedance.

### Switching (Bistable Operation)

A tunnel diode biased in the negative-resistance region with a load line that intersects the I–V curve at three points acts as a bistable element. The two stable operating points correspond to logic "0" and "1" states, enabling high-speed switching (sub-nanosecond).

---

## 10.2 Gunn Diode (Transferred-Electron Device)

### Transferred-Electron Effect (Ridley–Watkins–Hilsum)

In GaAs, InP, and certain III–V compounds, the conduction band has a **lower-valley minimum** (high mobility, low effective mass, $\Gamma$-valley) and an **upper-valley minimum** (low mobility, higher effective mass, L-valley), separated by $\Delta E \approx 0.36\text{ eV}$ for GaAs.

```
        E
        ↑   Γ-valley     L-valley
        |   (μ₁ large)   (μ₂ small)
        |      ○          ○
        |      | ΔE      |
        |      |           |
        |      └────────────
        |            k
```

When the applied electric field exceeds a **threshold field** $E_{th} \approx 3.2\text{ kV/cm}$ for GaAs, electrons gain enough energy to scatter into the upper valley, where mobility is 10–20× lower. The result is a **negative differential mobility**:

$$\mu_d = \frac{dv}{dE} < 0 \quad \text{for } E > E_{th} \tag{10.2}$$

### E–v Characteristic

The drift velocity as a function of electric field follows:

```
v (×10⁷ cm/s)
↑
1.0 ├───────●────
    │      / \
0.8 │     /   \
    │    /     \
0.5 │   /       \
    │  /         \
    │ /            \
    └────────────────→ E (kV/cm)
     0  3.2  5 10  20
```

A simplified analytic model:

$$v(E) = \frac{\mu_1 E + v_{sat}(E/E_{th})^4}{1 + (E/E_{th})^4} \tag{10.3}$$

where $\mu_1 \approx 6000\text{ cm}^2/(\text{V·s})$ is the low-field mobility and $v_{sat} \approx 10^7\text{ cm/s}$ is the saturation velocity.

### Gunn-Domain Formation

A **Gunn domain** is a high-field dipole layer that forms when $E > E_{th}$:

1. A doping fluctuation causes a local field increase above $E_{th}$
2. Electrons slow down (negative mobility), accumulating behind the fluctuation
3. A dipole forms: excess negative charge trailing, depleted region ahead
4. The domain drifts at the saturation velocity $v_{sat}$ toward the anode
5. When the domain reaches the anode, the current spikes and a new domain nucleates at the cathode

### Transit-Time Frequency

The fundamental oscillation frequency is determined by the transit time across the active region of length $L$:

$$f_t = \frac{v_{sat}}{L} \tag{10.4}$$

For $L = 10\;\mu\text{m}$, $f_t \approx 10\text{ GHz}$. By reducing $L$ to $1\text{–}2\;\mu\text{m}$, frequencies up to 100+ GHz are possible.

### Modes of Operation [pp. 801–805]

| Mode | Condition | Efficiency | Notes |
|------|-----------|------------|-------|
| **Transit-time** | $n_0 L > 10^{12}\text{ cm}^{-2}$ | ~2–15% | Fundamental mode |
| **LSA (limited space-charge accumulation)** | $f > f_t$, $n_0/f > 10^4\text{ s/cm}^3$ | ~15–20% | Domain never fully forms |
| **Delayed-domain** | Tuned circuit at $f < f_t$ | ~10–20% | Domain extinguishes before reaching anode |
| **Quenched-domain** | Tuned circuit at $f > f_t$ | ~10–15% | Domain collapses in transit |

---

## 10.3 IMPATT Diode

### Structure

IMPATT (IMPact Avalanche Transit Time) diodes use a **p⁺–n–n⁺** or **p⁺–p–n–n⁺** (Read diode) structure biased into avalanche breakdown.

### Operating Principle

The IMPATT diode generates negative resistance through a **phase delay** mechanism combining two effects:

1. **Avalanche multiplication** — The RF electric field modulates the avalanche current. Due to the finite build-up time of the avalanche process, the avalanche current lags the RF voltage by 90° (inductive).

2. **Transit-time delay** — Carriers generated in the avalanche region drift through the depletion region, producing an additional 90° delay (total 180°).

The combined effect is a **negative conductance** at the device terminals.

### Negative Conductance vs Frequency

```
G (conductance)
↑
+ │  ┌┐
  │  ││
0 ├──┼┼──────────────────
  │  ││  ┌┐
- │  ││  ││    ┌┐
  │  ││  ││    ││    ┌┐
  │  ││  ││    ││    ││
  └────────────────────────→ f
    0  f₁ f₂   f₃
```

The diode exhibits negative conductance over a frequency range roughly determined by the depletion region transit angle:

$$\theta = \omega \tau_d = \omega \frac{W_d}{v_s} \tag{10.5}$$

where $W_d$ is the depletion width and $v_s$ is the carrier saturation velocity.

Maximum negative conductance occurs when $\theta \approx \pi$ (transit angle of 180°):

$$f_{opt} \approx \frac{v_s}{2W_d} \tag{10.6}$$

### Small-Signal Model (Read's Model)

The small-signal admittance of an IMPATT diode:

$$Y_D(f) = G_D(f) + jB_D(f) \approx -\frac{I_{dc}\alpha' W_a}{2} \frac{\sin\theta - \theta\cos\theta}{\theta^2} \cdot \frac{\omega C_d}{\omega C_d + \tan(\theta/2)} + j\omega C_d \tag{10.7}$$

where $\alpha'$ is the derivative of the ionization coefficient with respect to electric field, $W_a$ is the avalanche width, and $C_d$ is the depletion capacitance.

### Key Parameters (Si IMPATT)

| Parameter | Typical Value |
|-----------|---------------|
| Breakdown voltage $V_B$ | 30–150 V DC |
| DC bias current $I_{dc}$ | 10–500 mA |
| Junction capacitance $C_j$ | 0.1–1 pF |
| Optimum frequency $f_{opt}$ | 5–100 GHz |
| RF output power | 0.1–10 W (pulsed to 100 W+) |
| Efficiency | 10–30% |
| Thermal resistance | 10–30°C/W |

---

## 10.4 TRAPATT Diode

### Principle

TRAPATT (TRapped Plasma Avalanche Triggered Transit) is a related but distinct mode of operation:

1. **Avalanche shock front** — A large RF voltage swing drives the diode into breakdown, creating a plasma-filled region (high density of electrons and holes).

2. **Plasma trapping** — The plasma is trapped by the space-charge field of the surrounding depletion region, causing a slow extraction of carriers.

3. **Low-impedance state** — During plasma extraction, the diode is in a low-impedance state, producing a large voltage drop with high current.

### Properties

- **Lower frequency** than IMPATT (typically $f_{opt}/3$ to $f_{opt}/2$)
- **Higher efficiency** (30–75% compared to 10–30% for IMPATT)
- **Higher power** (up to several kW pulsed)
- **Narrower bandwidth** and more critical circuit design

### Comparison

| Property | IMPATT | TRAPATT |
|----------|--------|---------|
| Operating freq. | 5–100+ GHz | 0.5–20 GHz |
| Efficiency | 10–30% | 30–75% |
| Output power | 0.1–10 W CW | 1 W–1 kW pulsed |
| Noise | High | Higher |
| Bias voltage | 30–150 V | 50–200 V |

---

## 10.5 Circuit Applications

### 10.5.1 Negative-Resistance Oscillator

A negative-resistance device can be modelled as a one-port with small-signal impedance $Z_d = R_d + jX_d$, where $R_d < 0$ in some frequency range.

#### Oscillation Condition

For steady-state oscillation:

$$Z_d(\omega_0, I_0) + Z_L(\omega_0) = 0 \tag{10.8}$$

where $Z_L = R_L + jX_L$ is the load impedance and $I_0$ is the RF current amplitude.

Separating real and imaginary parts:

$$R_d(\omega_0, I_0) + R_L = 0 \quad \Rightarrow \quad R_L = -R_d \quad (R_d < 0) \tag{10.9a}$$
$$X_d(\omega_0, I_0) + X_L = 0 \quad \Rightarrow \quad X_L = -X_d \tag{10.9b}$$

#### Start-Up Condition

For oscillation to start from noise, the total resistance must be negative:

$$R_d(0) + R_L < 0 \quad \Rightarrow \quad R_L < |R_d(0)| \tag{10.10}$$

#### Stabilised Oscillator Design

To avoid multiple oscillation modes and ensure a well-defined frequency, a common practice is to load the diode with $R_L$ satisfying the **stability constraint**:

$$R_L = \frac{|R_d|}{3} \quad \Rightarrow \quad R_d + R_L = -\frac{2}{3}|R_d| \quad \text{(start-up)} \tag{10.11}$$

This ensures robust start-up while allowing the oscillation amplitude to settle at $R_d(I_0) = -R_L$ in steady state.

#### Circuit Topology

```
        +V
         │
         R
         │
    ┌────┴────┐
    │     │   │
    │    ┌┴┐  │
    └────┤ │──┴── Z_L (load)
         └┬┘
          │
         ⏚ GND
```

A bias tee decouples the DC bias from the RF circuit. The resonant circuit (stub, cavity, dielectric resonator) sets the frequency, and the output coupling is adjusted to satisfy the oscillation condition.

### 10.5.2 Negative-Resistance Reflection Amplifier

A circulator-coupled reflection amplifier uses the negative resistance of the diode:

```
    Port 1 ────> [Circulator] ────> Port 2 ──── Z_d (diode)
                 │
                 └─── Port 3 ──── Z₀ (output)
```

- Input signal at Port 1 is routed to Port 2 (diode)
- The diode with $R_d < 0$ produces a reflection coefficient $|\Gamma| > 1$:

$$\Gamma = \frac{Z_d - Z_0}{Z_d + Z_0} \tag{10.12}$$

- The amplified reflected wave exits at Port 3

Power gain:

$$G = |\Gamma|^2 = \left|\frac{Z_d - Z_0}{Z_d + Z_0}\right|^2 \tag{10.13}$$

### 10.5.3 Injection Locking

An external signal injected into a free-running negative-resistance oscillator can synchronise (lock) the output:

$$\frac{d\phi}{dt} = \Delta\omega - \frac{\omega_0}{2Q}\frac{V_{inj}}{V_{osc}} \sin\phi \tag{10.14}$$

Locking range (Adler's formula):

$$\Delta\omega_{L} = \frac{\omega_0}{2Q} \frac{V_{inj}}{V_{osc}} \tag{10.15}$$

- Wider locking range requires larger injection power or lower Q
- Out-of-lock operation produces unwanted FM sidebands (Hunting phenomenon)

---

## Summary Table

| Device | Mechanism | Static/Dynamic $R_n$ | Freq. Range | Eff. | Power |
|--------|-----------|----------------------|-------------|------|-------|
| Tunnel diode | Quantum tunneling | Static N-type | 1–10 GHz | Low | mW |
| Gunn diode | Transferred electron | Dynamic (bulk) | 1–100+ GHz | 2–20% | mW–W |
| IMPATT | Avalanche + transit | Dynamic | 5–100+ GHz | 10–30% | W–10 W |
| TRAPATT | Trapped plasma | Dynamic | 0.5–20 GHz | 30–75% | kW pulsed |

---

## Key Formulas

| Description | Formula | Eqn |
|-------------|---------|-----|
| Tunnel diode current | $I(V) = I_p(V/V_p)\exp(1-V/V_p) + I_0[\exp(qV/nkT)-1]$ | (10.1) |
| Negative mobility condition | $dv/dE < 0$ for $E > E_{th}$ | (10.2) |
| Gunn drift velocity (approx.) | $v(E) = [\mu_1 E + v_{sat}(E/E_{th})^4] / [1 + (E/E_{th})^4]$ | (10.3) |
| Gunn transit frequency | $f_t = v_{sat}/L$ | (10.4) |
| IMPATT transit angle | $\theta = \omega W_d/v_s$ | (10.5) |
| IMPATT optimum frequency | $f_{opt} \approx v_s/(2W_d)$ | (10.6) |
| Oscillation condition | $Z_d + Z_L = 0$, $R_L = -R_d$ | (10.9) |
| Start-up condition | $R_L < |R_d(0)|$ | (10.10) |
| Stabilised load | $R_L = |R_d|/3$ | (10.11) |
| Reflection gain | $G = |(Z_d - Z_0)/(Z_d + Z_0)|^2$ | (10.13) |
| Injection locking range | $\Delta\omega_L = (\omega_0/2Q)(V_{inj}/V_{osc})$ | (10.15) |

---

## References

1. R. E. Collin, *Foundations for Microwave Engineering*, 2nd ed., IEEE Press, 2001, Chs. 10–12 (oscillator/amplifier material).
2. J. B. Gunn, "Microwave oscillations of current in III–V semiconductors," *Solid State Communications*, vol. 1, pp. 88–91, 1963.
3. L. Esaki, "New phenomenon in narrow germanium p–n junctions," *Phys. Rev.*, vol. 109, pp. 603–604, 1958.
4. W. T. Read, "A proposed high-frequency negative-resistance diode," *Bell Syst. Tech. J.*, vol. 37, pp. 401–446, 1958.
5. S. M. Sze, *Physics of Semiconductor Devices*, 3rd ed., Wiley, 2007.
6. K. Chang, *Microwave Solid-State Circuits and Applications*, Wiley, 1994.

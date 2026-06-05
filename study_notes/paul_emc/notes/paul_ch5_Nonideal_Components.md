# Chapter 5 — Nonideal Behavior of Components

> **Source:** Clayton R. Paul, *Introduction to Electromagnetic Compatibility*, 2nd Ed., Wiley, 2006. Chapter 5, pp. 299–last.
> **Status:** 🟡 Raw text → LaTeX洗稿中

---

## 5.1 Wires

### 5.1.1 Resistance and Internal Inductance

The dc resistance of a round wire of radius $r_w$, conductivity $\sigma$, and total length $L$ is

$$
R_{\mathrm{dc}} = \frac{L}{\sigma \pi r_w^2} \quad \text{[}\Omega\text{]}
\tag{5.1}
$$

#### Skin Depth

As frequency rises, current crowds toward the outer surface due to **skin effect**. The current concentrates in an annulus of thickness equal to the skin depth:

$$
\delta = \frac{1}{\sqrt{\pi f \mu_0 \sigma}}
      = 6.6\times10^{-2}\,\sqrt{\frac{\text{m}}{\text{Hz}}}\;\sqrt{\frac{1}{f}}
      = 2.6\times10^{3}\,\sqrt{\frac{\text{mils}}{\text{Hz}}}\;\sqrt{\frac{1}{f}}
\tag{5.2}
$$

For copper ($\sigma_{\mathrm{Cu}} = 5.8\times10^7\ \mathrm{S/m}$, $\mu_r = 1$, $\varepsilon_r = 1$):

| $f$       | $\delta$ (copper)      |
|----------|------------------------|
| 60 Hz    | 8.5 mm                 |
| 1 kHz    | 2.09 mm                |
| 100 kHz  | 0.21 mm                |
| 1 MHz    | 2.6 mils               |
| 10 MHz   | 0.82 mils              |
| 100 MHz  | 0.26 mils              |
| 1 GHz    | 0.0823 mils            |

> **工程直觉:** 在辐射发射频段（30 MHz–40 GHz），趋肤深度急剧减小——100 MHz时仅0.26 mils（≈6.6 μm）。高频电流只利用了导体截面的极小一部分。

#### High-Frequency Resistance

The per-unit-length resistance transitions from dc to a high-frequency asymptote when $\delta < r_w$:

$$
r_{\mathrm{lf}} = r_{\mathrm{dc}} = \frac{1}{\sigma\pi r_w^2} \quad \text{when } r_w \ll \delta
$$

$$
r_{\mathrm{hf}} = \frac{1}{\sigma\cdot 2\pi r_w \delta}
                = \frac{r_w}{2\delta}\,r_{\mathrm{dc}}
                = \frac{1}{2r_w}\sqrt{\frac{\mu_0 f}{\pi\sigma}} \quad \text{when } r_w \gg \delta
\tag{5.3b}
$$

> **工程直觉:** 高频电阻以 **+10 dB/decade** 的速率随频率增长（因为 $\delta \propto f^{-1/2}$，而 $r_{\mathrm{hf}} \propto 1/\delta$）。转折点发生在 $r_w = 2\delta$ 处。

#### Internal Inductance

The **internal inductance** $L_i$ arises from magnetic flux internal to the wire itself.

DC internal inductance per unit length:

$$
\ell_{i,\mathrm{dc}} = \frac{\mu_0}{8\pi}
                   = 0.5\times10^{-7}\ \mathrm{H/m}
                   = 50\ \mathrm{nH/m}
                   = 1.27\ \mathrm{nH/in.}
\tag{5.4a}
$$

High-frequency internal inductance (when $r_w \gg \delta$):

$$
\ell_{i,\mathrm{hf}} = \frac{2\delta}{r_w}\,\ell_{i,\mathrm{dc}}
                     = \frac{1}{4\pi r_w}\sqrt{\frac{\mu_0 f}{\pi\sigma}}
\tag{5.4b}
$$

> **工程直觉:** 高频内感以 **−10 dB/decade** 速率下降（因为 $\delta \propto f^{-1/2}$）。在高频下，电流趋于表面，内感随之减小。

**Example 5.1 — 20 AWG copper wire at 200 MHz:**

- $r_w = 16\ \text{mils} = 16\times2.54\times10^{-5}\ \text{m} = 0.4064\ \text{mm}$
- Skin depth: $\delta \approx 0.184\ \text{mils}$ → skin-effect regime ($r_w \gg \delta$)
- $r_{\mathrm{hf}} = 1.44\ \Omega/\text{m} = 36.7\ \text{m}\Omega/\text{in.}$
- Total resistance of 2 in.: $R \approx 73.4\ \text{m}\Omega$
- $\ell_{i,\mathrm{hf}} = 1.15\ \text{nH/m} = 29.2\ \text{pH/in.}$
- Total internal inductance for 2 in.: $L_i \approx 58.4\ \text{pH}$

---

### 5.1.2 External Inductance and Capacitance of Parallel Wires

For a pair of parallel round wires, radius $r_w$, length $L$, center-to-center separation $s$ (with $s/r_w > 5$, so proximity effect is negligible):

**Per-unit-length external inductance** (loop inductance, flux between the two wires):

$$
\ell_e = \frac{\mu_0}{\pi}\ln\!\left(\frac{s}{r_w}\right)
       = 0.4\ \ln\!\left(\frac{s}{r_w}\right)\ \mathrm{\mu H/m}
       = 10.16\ \ln\!\left(\frac{s}{r_w}\right)\ \mathrm{nH/in.}
\tag{5.5}
$$

Total loop inductance: $L_{\text{loop}} = 2\ell_i L + \ell_e L$.

**Per-unit-length capacitance** between the two wires:

$$
c = \frac{\pi\varepsilon_0}{\ln(s/r_w)}
  = \frac{27.78}{\ln(s/r_w)}\ \mathrm{pF/m}
  = \frac{0.706}{\ln(s/r_w)}\ \mathrm{pF/in.}
\tag{5.6}
$$

**Characteristic impedance** of the parallel-wire transmission line:

$$
Z_C = \sqrt{\frac{\ell_e}{c}}
     = 120\,\ln\!\left(\frac{s}{r_w}\right)\ \Omega
\tag{5.7}
$$

> **工程直觉:** 对于典型间距（如扁平电缆中相邻导线间距50 mils），外感 $\ell_e \approx 11.6\ \text{nH/in.}$，大约是内感的 **10倍**！因此在高频下，外感是主导因素，内感可忽略。

**Review Exercise 5.1 (solution hint):** For 20 AWG solid wires, $r_w = 16$ mils, $s = 250$ mils (¼ in.):
$\ell_e \approx 10.16\ln(250/16) \approx 27.9\ \text{nH/in.}$, $c \approx 0.257\ \text{pF/in.}$

---

### 5.1.3 Lumped Equivalent Circuits of Parallel Wires

If the line is **electrically short** ($L \ll \lambda$), the distributed parameters can be lumped. Four lumped-circuit topologies exist (all equivalent for short lines):

| Model | Structure |
|-------|-----------|
| Lumped-backward Γ | Series $R$, series $L$ (internal + external), shunt $C$ |
| Lumped-Π | Shunt $C$ at both ends, series $R$+$L$ in middle |
| Lumped-T | Series $R$+$L$ at both ends, shunt $C$ in middle |
| Lumped-G | Full tee/pi hybrid |

**Selection criterion:**
- **Low-$Z_L$ load** → prefer **lumped-G** or **lumped-T** (the rightmost shunt $C$ of Γ or Π models is bypassed by the low load, rendering it ineffective)
- **High-$Z_L$ load** → prefer **lumped-Γ** or **lumped-Π** (the rightmost series $R$+$L$ of G or T models is in series with the high load, rendering it ineffective)

> **工程直觉:** 永远根据负载阻抗高低选择最合适的等效电路拓扑；选错会导致模型在较低频率就失效。

**Review Exercise 5.2 (answer hint):** For 28-gauge solid wires, $L = 5$ in., $s = 50$ mils at $f = 10$ MHz:
$R \approx 0.209\ \Omega$, $L_{\text{internal}} \approx 3.32\ \text{nH}$, $L_{\text{external}} \approx 105\ \text{nH}$, $C \approx 1.7\ \text{pF}$.

---

## 5.2 Printed Circuit Board (PCB) Lands

### Resistance

PCB lands have **rectangular** cross sections (width $w$, thickness $t$, $t \ll w$). The current distribution behaves analogously to round wires.

DC/low-frequency resistance per unit length:

$$
r_{\mathrm{lf}} = r_{\mathrm{dc}} = \frac{1}{\sigma\, w\, t} \quad \Omega/\text{m}
\tag{5.8a}
$$

High-frequency resistance (current crowds to outer edges, assuming uniform distribution over skin depth $\delta$):

$$
r_{\mathrm{hf}} = \frac{1}{\sigma\,(2\delta w + 2\delta t)}
              = \frac{1}{2\sigma\delta\,(w + t)} \quad \Omega/\text{m}
\tag{5.8b}
$$

The two asymptotes join at the frequency where $\delta = \dfrac{1}{2}\dfrac{wt}{w+t} \approx \dfrac{t}{2}$ (since typically $t \ll w$).

> **工程直觉:** PCB覆铜厚度1 oz ≈ 1.38 mils；高频时电流只在顶底两个表面流动，等效导电宽度变为 $2(w+t)$。

### External Inductance and Capacitance

The external (loop) inductance and capacitance of PCB lands are computed from the characteristic impedance and velocity of propagation:

$$
Z_C = \sqrt{\frac{\ell_e}{c}}\quad \Omega
\tag{5.9a}
$$

$$
v = \frac{1}{\sqrt{\ell_e c}}
  = \frac{c_0}{\sqrt{\varepsilon_r^{\text{eff}}}}
  = 3\times10^8\sqrt{\frac{1}{\varepsilon_r^{\text{eff}}}}\ \mathrm{m/s}
  = 11.8\sqrt{\frac{1}{\varepsilon_r^{\text{eff}}}}\ \mathrm{in./ns}
\tag{5.9b}
$$

Then:

$$
\ell_e = \frac{Z_C}{v},\qquad
c = \frac{1}{v Z_C}
\tag{5.10}
$$

> **工程直觉:** 有效介电常数 $\varepsilon_r^{\text{eff}}$ 解释了电场同时存在于PCB板料（$\varepsilon_r\approx4.7$）和空气中的事实。微带线的 $v$ 比自由空间光速慢，$\varepsilon_r^{\text{eff}}$ 通常在 $2\sim4$ 之间。

**Review Exercise 5.3 (answer hint):** For PCB I configuration, $L = 5$ in., $s = w = 15$ mils, $h = 62$ mils, $t = 1.38$ mils, $\varepsilon_r = 4.7$ at $f = 100$ MHz:
$R \approx 796\ \text{m}\Omega$, $L_e \approx 102\ \text{nH}$, $C \approx 4.89\ \text{pF}$.

---

## 5.3 Effect of Component Leads

### Lead Inductance

Component leads form a loop. Treating them as a pair of parallel round wires (20 AWG, $r_w = 16$ mils), for lead length $0.5$ in. and separation $0.25$ in.:

$$
L_{\text{lead}} = \ell_e \times (\text{lead length})
                \approx 14\ \text{nH}
\tag{derived from (5.5)}
$$

### Lead Capacitance

For the same geometry, using (5.6):

$$
C_{\text{lead}} = c \times (\text{lead length}) \approx 0.128\ \text{pF}
$$

> **工程直觉:** 引线电感（14 nH）通常远大于引线电容（0.128 pF）的容抗在高频下。但漏电阻和封装电容可达 $1\!-\!2$ pF，成为与电感共振的主角。

### Lumped Lead Model

For electrically short leads, the four lumped topologies of Fig. 5.8 apply (identical in structure to the wire pair models). The choice of topology follows the same load-impedance criterion as Section 5.1.3.

---

## 5.4 Resistors

### Types and Construction

| Type | Key Property | Inductance | Notes |
|------|-------------|------------|-------|
| Carbon composition | Most common | Low | 5–10% tolerance; good for high-$di/dt$ |
| Wire wound | Tight tolerance | **High** (due to coil) | Avoid for sense resistors in switchers |
| Thin film | Precise value | Lower than wire-wound | Deposited metallic film |

### Nonideal Frequency Behavior

The leads contribute $L_{\text{lead}} \approx 14\ \text{nH}$ and parasitic capacitance $C_{\text{par}} \approx C_{\text{lead}} + C_{\text{leakage}} \approx 1$–$2\ \text{pF}$. Replacing leads with a lumped-backward Γ gives the **complete resistor model** (Fig. 5.10b).

The impedance transfer function ($p = j\omega$):

$$
\hat{Z}(p) = \frac{L_{\text{lead}}\,p^2 + \dfrac{p}{R C_{\text{par}}} + \dfrac{1}{L_{\text{lead}}C_{\text{par}}}}
                {p + \dfrac{1}{R C_{\text{par}}}}
\tag{5.12}
$$

Or substituting $p = j\omega$:

$$
\hat{Z}(j\omega) = \frac{L_{\text{lead}}\!\left(\frac{1}{L_{\text{lead}}C_{\text{par}}} - \omega^2\right)
                   + j\frac{\omega}{R C_{\text{par}}}}
                  {j\omega + \dfrac{1}{R C_{\text{par}}}}
\tag{5.13}
$$

### Bode Plot Interpretation (Fig. 5.10c)

| Frequency | Behavior | Phase |
|-----------|----------|-------|
| DC ($f = 0$) | $\hat{Z} = R$ (ideal resistor) | $0^\circ$ |
| $f_1 = \dfrac{1}{2\pi R C_{\text{par}}}$ | $C_{\text{par}}$ shorting $R$; magnitude drops at $-20$ dB/dec | approaches $-90^\circ$ |
| $f_0 = \dfrac{1}{2\pi\sqrt{L_{\text{lead}}C_{\text{par}}}}$ | **Resonance** — magnitude minimum (≈ $R$ if $R$ is small, or $\to\infty$ for large $R$) | $\to 0^\circ$ |
| $f \gg f_0$ | $L_{\text{lead}}$ dominates; magnitude rises at $+20$ dB/dec | approaches $+90^\circ$ |
| $f \to \infty$ | Open circuit (inductor blocks, capacitor shorts) | $+90^\circ$ |

> **工程直觉:** 对于高阻值电阻（如1 kΩ），$f_1 \approx 1/(2\pi \cdot 10^3 \cdot 1.2\times10^{-12}) \approx 133$ MHz，电容主导的$-90^\circ$区域更早出现。对于低阻值电阻，自谐振频率 $f_0$ 更低。

**典型测量数据 (Fig. 5.12):** 1 kΩ碳合成电阻，½ in.引线，lead separation 0.25 in.：
$f_1 \approx 120$ MHz, $f_0$ 接近但高于500 MHz上限。拟合模型: $R = 1.05$ kΩ, $C_{\text{par}} = 1.2$ pF, $L_{\text{lead}} = 14$ nH。

---

## 5.5 Capacitors

### Ideal Capacitor Frequency Response

$$
\hat{Z}(j\omega) = \frac{1}{j\omega C}
                 = \frac{1}{\omega C}\,\angle -90^\circ
\tag{5.16}
$$

- Magnitude: $-20$ dB/decade (decreases linearly with $f$)
- Phase: constant $-90^\circ$

### Types and Characteristics

| Type | Capacitance Range | Typical Use | Behavior Above SRF |
|------|-----------------|-------------|-------------------|
| Ceramic | 1 mF down to 5 pF | Radiated emission suppression (high freq) | Excellent up to SRF |
| Tantalum electrolytic | 1–1000 μF | Conducted emission suppression + bulk charge | Higher ESR; degrades faster |

### Physical Model (Fig. 5.16)

The capacitor is modeled as a pair of parallel plates with dielectric loss ($R_{\text{diel}}$) and plate resistance ($R_{\text{plate}}$). Leads contribute $L_{\text{lead}}$ and $C_{\text{lead}}$. Neglecting $R_{\text{diel}}$ (large) and $C_{\text{lead}} \ll C$, we obtain the **simplified series model** (Fig. 5.17):

$$
\hat{Z}(p) = \frac{L_{\text{lead}}\,p^2 + \dfrac{R_s}{L_{\text{lead}}}\,p + \dfrac{1}{L_{\text{lead}}C}}
                {p}
\tag{5.17}
$$

Substituting $p = j\omega$:

$$
\hat{Z}(j\omega) = \frac{L_{\text{lead}}\!\left(\frac{1}{L_{\text{lead}}C} - \omega^2\right)
                   + j\omega\,\frac{R_s}{L_{\text{lead}}}}
                  {j\omega}
\tag{5.18}
$$

### Key Parameters

- **Self-Resonant Frequency (SRF):**
  $$
  f_0 = \frac{1}{2\pi\sqrt{L_{\text{lead}}C}}
  \tag{derived from (5.18)}
  $$
  For $L_{\text{lead}} \approx 14$ nH (0.5 in. leads, 0.25 in. separation):
  - 470 pF → $f_0 \approx 62$ MHz
  - 0.1 μF → $f_0 \approx 4.25$ MHz

- **ESR (Equivalent Series Resistance):** $R_s$, typically several Ω for electrolytic, negligible for ceramic.

### Frequency Behavior (Fig. 5.17)

| Frequency | Dominant Element | Magnitude Slope | Phase |
|-----------|-----------------|-----------------|-------|
| DC | Open circuit | — | $-90^\circ$ |
| $f < f_0$ | Capacitor $C$ | $-20$ dB/dec | $-90^\circ$ |
| $f = f_0$ | $C$ and $L$ cancel → net impedance = $R_s$ | Minimum | $\to 0^\circ$ |
| $f > f_0$ | Inductor $L_{\text{lead}}$ | $+20$ dB/dec | $\to +90^\circ$ |

> **工程直觉 #1:** 盲目增大电容值来降低阻抗是常见错误。大电容的SRF更低，在高频下反而呈现感性，阻抗反而增大！测量数据证实：100 pF陶瓷电容在100 MHz时阻抗8 Ω；10,000 pF同条件反而是12 Ω（感性）。

> **工程直觉 #2:** 并联电容只有在 **高阻抗电路** 中才有效（电流分流原理：若 $Z_{\text{LOAD}} \gg Z_{\text{CAP}}$，大部分噪声电流被分流）。低阻抗电路中，并联电容无效。

### Current Division (Fig. 5.22)

When a capacitor is placed in parallel to divert noise current $\hat{I}_{\text{NOISE}}$ away from a load:

$$
\hat{I}_C = \frac{\hat{Z}_{\text{LOAD}}}{\hat{Z}_{\text{CAP}} + \hat{Z}_{\text{LOAD}}}\,\hat{I}_{\text{NOISE}}
\tag{5.19}
$$

若 $\hat{Z}_{\text{LOAD}} \gg \hat{Z}_{\text{CAP}}$ → $\hat{I}_C \approx \hat{I}_{\text{NOISE}}$ （有效分流）。
若 $\hat{Z}_{\text{LOAD}} \ll \hat{Z}_{\text{CAP}}$ → $\hat{I}_C \approx 0$ （电容无效！）。

**Review Exercise 5.6 (solution):** $Z_{\text{LOAD}} = 1000$ Ω, want 90% current through capacitor at 100 MHz:
$0.9 = Z_{\text{LOAD}}/(Z_{\text{CAP}}+Z_{\text{LOAD}}) \Rightarrow Z_{\text{CAP}} = 111$ Ω.
At 100 MHz: $C = 1/(2\pi\cdot100\times10^6\cdot111) \approx 14.3$ pF (or more precisely solving the quadratic gives $C \approx 3.3$ pF when using exact current division with $\hat{Z}_{\text{CAP}} = 1/(j\omega C)$).

---

## 5.6 Inductors

### Ideal Inductor

$$
\hat{Z}_L(j\omega) = j\omega L
                   = \omega L\angle +90^\circ
\tag{5.20}
$$

- Magnitude: $+20$ dB/decade (increases with $f$)
- Phase: constant $+90^\circ$

### Nonideal Model (Fig. 5.24)

Winding turns of wire introduce:

- **$R_{\text{par}}$:** Wire resistance plus core loss
- **$C_{\text{par}}$:** Parasitic capacitance between adjacent turns (increases significantly with layered winding)
- **$L_{\text{lead}}$:** Lead inductance (usually negligible compared to intended $L$)

The model: $R_{\text par}$ in **series** with $L$, the whole series combination **in parallel** with $C_{\text{par}}$.

Impedance transfer function:

$$
\hat{Z}_L(p) = R_{\text{par}}\,
               \frac{1 + \dfrac{pL}{R_{\text{par}}}}
                    {p^2 L C_{\text{par}} + p\,R_{\text{par}}C_{\text{par}} + 1}
\tag{5.21}
$$

Substituting $p = j\omega$:

$$
\hat{Z}_L(j\omega) = R_{\text{par}}\,
                     \frac{1 + j\omega\,\dfrac{L}{R_{\text{par}}}}
                          {1 - \omega^2 L C_{\text{par}} + j\omega\,R_{\text{par}}C_{\text{par}}}
\tag{5.22}
$$

### Frequency Behavior

| Frequency | Dominant Element | Magnitude | Phase |
|-----------|-----------------|-----------|-------|
| Low $f$ | $R_{\text{par}}$ | Constant (≈ $R_{\text{par}}$) | $\to 0^\circ$ |
| Midrange: $\omega = R_{\text{par}}/L$ | $L$ dominates | Rises at $+20$ dB/dec | $\to +90^\circ$ |
| $f_0 = \dfrac{1}{2\pi\sqrt{LC_{\text{par}}}}$ | $L$ and $C_{\text{par}}$ resonate | **Peak** (limited by $R_{\text{par}}$) | $\to 0^\circ$ |
| $f \gg f_0$ | $C_{\text{par}}$ short-circuits $L$ | Drops | $\to -90^\circ$ |

> **工程直觉:** 和电容一样，**增大电感值会降低SRF**（$f_0 \propto 1/\sqrt{L}$）！10 mH电感（而非1.2 mH）的SRF约40 MHz，在高频下可能呈现电容性。

**测量数据 (Fig. 5.25):** 1.2 mH inductor, SRF ≈ 110 MHz → $C_{\text{par}} \approx 1.7$ pF。

### Series Inductors vs. Parallel Capacitors

| Device | Purpose | Best Environment |
|--------|---------|-----------------|
| Series inductor | Block noise current (series element → increase net series impedance) | **Low-impedance** circuits ($Z_{\text{LOAD}}$ low → large $\Delta Z$ from added $j\omega L$) |
| Parallel capacitor | Divert noise current (shunt element → provide low-$Z$ alternative path) | **High-impedance** circuits ($Z_{\text{LOAD}} \gg Z_{\text{CAP}}$ → effective diversion) |

---

## 5.7 Ferromagnetic Materials — Saturation and Frequency Response

### Three Critical Properties

1. **Saturation** — permeability $\mu$ decreases with increasing current
2. **Frequency response** — $\mu$ deteriorates with frequency
3. **Flux concentration** — magnetic fields concentrate in high-$\mu$ materials

### Saturation (Fig. 5.27)

For a toroidal inductor with $N$ turns on a ferromagnetic core (cross-section $A$, mean path length $\ell$):

$$
L = \frac{\mu_r \mu_0 N^2 A}{\ell}
$$

The $B$–$H$ curve of a ferromagnetic material is **nonlinear**. At low currents, slope (permeability) is high. As current increases, the operating point moves up the curve, the slope decreases, and **permeability drops**. Since $L \propto \mu$, inductance decreases with increasing current.

> **工程直觉:** 铁磁芯电感在高电流下会"软化"——电感值下降，使得高频噪声抑制性能在高电流条件下退化。

### Magnetic Circuit Analogy

| Electrical | Magnetic |
|------------|----------|
| Voltage $V$ | Magnetomotive force $\mathcal{F} = NI$ (ampere-turns) |
| Current $I$ | Magnetic flux $\Phi$ (webers) |
| Resistance $R = V/I$ | Reluctance $\mathcal{R} = \mathcal{F}/\Phi = \ell/(\mu A)$ |

The equivalent magnetic circuit (Fig. 5.27b) divides flux into **core flux** $\Phi_{\text{core}}$ and **leakage flux** $\Phi_{\text{air}}$:

$$
\Phi_{\text{core}} = \frac{\mathcal{R}_{\text{air}}}{\mathcal{R}_{\text{air}} + \mathcal{R}_{\text{core}}}\,\Phi
\tag{5.26}
$$

For high-$\mu$ cores ($\mathcal{R}_{\text{core}} \ll \mathcal{R}_{\text{air}}$), most flux is confined to the core.

### Frequency Response of Permeability (Fig. 5.28)

| Material | Typical $\mu_r$ at 1 kHz | Frequency Behavior |
|----------|------------------------|-------------------|
| MnZn (manganese zinc) ferrite | High (2000–3000) | $\mu$ drops rapidly; poor above ~10 MHz |
| NiZn (nickel zinc) ferrite | Lower (500–800) | $\mu$ stays higher into 100s of MHz |

> **工程直觉:** 抑制传导发射（150 kHz–30 MHz）→ **MnZn**（初始$\mu$高）。抑制辐射发射（30 MHz–1 GHz）→ **NiZn**（高频$\mu$保持更好）。混用会导致选错磁芯，使抑制效果严重退化。

**实测数据 (Fig. 5.29):** 5 turns on MnZn → $Z \approx 500\ \Omega$ @ 1 MHz but only $380\ \Omega$ @ 60 MHz. NiZn → $80\ \Omega$ @ 1 MHz but **1200 Ω** @ 60 MHz！NiZn在高频完胜。

---

## 5.8 Ferrite Beads

### Construction and Principle

Ferrite beads are **nonconductive ceramic** materials (low eddy-current losses up to 100s of MHz). The ferrite is formed around a conductor, resembling a resistor (black bead without bands). They provide **frequency-selective attenuation** without affecting low-frequency functional signals.

### Complex Permeability

The ferrite is characterized by a **complex relative permeability**:

$$
\mu_r(f) = \mu_r'(f) - j\,\mu_r''(f)
\tag{5.27}
$$

- $\mu_r'$: Real part → **stored magnetic energy** (inductive reactance)
- $\mu_r''$: Imaginary part → **losses** (effective resistance)

The bead impedance:

$$
j\omega L_{\text{bead}} = j\omega\mu_0\mu_r K
                      = j\omega\mu_0(\mu_r' - j\mu_r'')K
                      = \underbrace{\omega\mu_0\mu_r''K}_{\text{Effective }R(f)}
                        + j\,\underbrace{\omega\mu_0\mu_r'K}_{\text{Effective }L(f)}
\tag{5.28}
$$

> **工程直觉:** 铁氧体磁珠的等效电路是**频率相关的串联R+L**：$R$和$L$都随频率变化。在某一频段，$R$（损耗）占主导，提供耗散性抑制。

- Typical bead impedance: $\sim 100\ \Omega$ above ~100 MHz
- Multi-hole beads (Fig. 5.32): increase impedance by increasing effective turns
- ½-turn vs. 2½-turn: impedance roughly triples with extra turns (from ~200 Ω to ~600 Ω @ 100 MHz, Fig. 5.33)

> **工程直觉:** 磁珠阻抗上限约几百欧姆，适合**低阻抗电路**（如电源线）中的损耗性滤波，而非高阻抗电路。也易在60 Hz大电流下饱和。

---

## 5.9 Common-Mode Chokes

### Common-Mode vs. Differential-Mode Currents

For a two-conductor pair carrying $\hat{I}_1$ and $\hat{I}_2$:

$$
\hat{I}_D = \frac{1}{2}(\hat{I}_1 - \hat{I}_2) \quad \text{(differential mode — functional signal)}
$$
$$
\hat{I}_C = \frac{1}{2}(\hat{I}_1 + \hat{I}_2) \quad \text{(common mode — unintended, antenna-mode)}
\tag{5.30}
$$

**辐射潜力:** 同一导体上的差模电流方向相反，产生的辐射电场倾向于相互抵消；而共模电流方向相同，辐射电场**叠加**。**微安级的共模电流产生的辐射与数十毫安的差模电流相当！**

### Common-Mode Choke Structure (Fig. 5.36)

Two windings on a **high-μ ferrite core**, with directions such that:
- **Differential-mode flux** (opposite currents) **cancels** in the core → $L - M \approx 0$, ideally no effect on functional signal
- **Common-mode flux** (same direction currents) **adds** in the core → $L + M$, providing high impedance to block these currents

For symmetric windings ($L_1 = L_2 = L$, $M$):

$$
\hat{Z}_{\text{CM}} = j\omega(L + M) \quad \text{(common-mode)}
\tag{5.32}
$$
$$
\hat{Z}_{\text{DM}} = j\omega(L - M) \quad \text{(differential-mode)}
\tag{5.33}
$$

If $L = M$ (ideal tight coupling), $\hat{Z}_{\text{DM}} = 0$ — **no effect on differential-mode (functional) currents**.

In addition to the inductive reactance, ferrite cores add **frequency-dependent loss resistance** $R(f)$ in series with the common-mode path, dissipating energy.

> **工程直觉:** 共模扼流圈的核心优势：**差模磁通在铁芯中抵消**，所以高电平功能电流（通常较大）不会使铁芯饱和，同时铁芯的高$\mu$又对共模电流（通常较小）提供高阻抗。这是几乎唯一不影响功能信号同时抑制共模辐射的器件。

### Winding Check (Fig. 5.37)

Use the **right-hand rule**: thumb = current direction, fingers = flux direction. Ensure input and output leads are separated on the core to minimize **parasitic capacitance** that bypasses the core at high frequencies.

---

## 5.10 Electromechanical Devices

### 5.10.1 DC Motors

**主要EMC问题：**
1. **电刷换向拉弧** → 产生宽频谱高频辐射（200 MHz–1 GHz）
2. **驱动电路引入共模电流** → 通过电机外壳与产品金属机架之间的寄生电容$C_{\text{par}}$形成通路

**抑制措施 (Fig. 5.38c):**
- 在换向器段之间跨接**电阻或电容**（弧抑制）
- 驱动引线中串入**共模扼流圈**（阻止共模电流）

**H桥驱动电路 (Fig. 5.39):** 电机外壳接地作为散热器 → 产生较大$C_{\text{par}}$ → 共模噪声电流通过驱动线–电机外壳–产品框架形成大环路（高频辐射增强）。

### 5.10.2 Stepper Motors

- 无换向器拉弧，但驱动电路的**高频开关噪声**通过寄生电容耦合到电机外壳
- 与DC电机相同的共模问题
- 典型寄生阻抗：@ 70 MHz处有约3 Ω的阻抗零点

### 5.10.3 AC Motors

- 无电刷，但定子/转子间距小 → 寄生电容较大
- 若外壳接地，高频共模电流可能耦合到电源线或产品框架
- **Chopper drivers** 产生高频开关谱，需要共模扼流圈

### 5.10.4 Solenoids

- 通断电感能量 → 高频瞬态噪声
- 绕组与金属外壳之间寄生电容 → 共模通路
- 小型电磁阀典型：@ 150 MHz处有约8 Ω的共模阻抗零点

> **工程直觉:** 任何带金属外壳并通过引线连接到PCB的机电部件，都可能通过寄生电容在产品框架上注入高频共模电流。排查辐射问题时，电机类负载是不可忽视的潜在源头。

---

## 5.11 Digital Circuit Devices

### Spectral Content of Digital Signals

The **transition time** ($t_r$, $t_f$) of digital pulses — as short as ~1 ns in modern devices — determines the **high-frequency spectral content** (Chapter 3). The spectral amplitude at frequency $f$ is approximately constant up to $f \approx 1/(\pi t_r)$ and rolls off as $1/f$ beyond that.

### Architectural EMC Concerns

| Component | EMC Consideration |
|-----------|-------------------|
| Microprocessor / clock | Fastest transitions, highest spectral content |
| Buffers/drivers | "Square up" slowed signals, add current drive → increase spectral content |
| Rare-event lines (reset, control) | May carry inadvertently coupled high-frequency noise |
| ROM/RAM | Less directly problematic, but data line switching adds to total noise |

### Parasitic Capacitances in Semiconductor Junctions

Each semiconductor junction (diode, BJT, FET) forms a **parasitic capacitance** at the p-n junction. At high frequencies, these capacitances provide direct coupling from input to output, effectively "shorting" the device.

> **工程直觉:** 永远不要假设某根信号线"不承载高频"——实测几乎所有数字信号线在1 ns级的探头下都能看到百MHz级谱。在PCB上用频谱仪探测每个可疑节点是定位辐射源的最直接方法。

---

## 5.12 Effect of Component Variability

### The Compliance Reproducibility Problem

A prototype "fine-tuned" to pass EMC limits does **not** guarantee all production units will pass. Sources of variability:

| Source | Effect |
|--------|--------|
| Parts vendor changes | Different semiconductor $t_r$, different parasitic capacitances |
| Component tolerance stackup | Digital IC max/$t_r$ variation (functional spec) vs. min/$t_r$ (EMC spec) |
| Ferrite core batch variation | $\pm 20\%$ permeability variation → SRF shift |

> **工程直觉:** 功能性能目标与EMC性能目标经常**冲突**。例如功能设计师要求最坏情况下的最大$t_r$（以保证功能正常），但EMC工程师关心的是最小$t_r$（越短则高频谱越大）。器件厂商保证的是功能规格，不保证EMC兼容性。

**案例 (Paul, 2006):** 同一型号RS-232线路驱动器的−12 V供电引线，不同厂商甚至同厂商不同批次的芯片在10–210 MHz频段内的传导发射谱差异可达 **20 dB以上**！所有器件均通过功能测试。

> **工程直觉:** 在产品生命周期的任何时间点更换元器件供应商，都必须重新进行EMC验证，而不仅仅是功能性验证。

---

## 5.13 Mechanical Switches

*（本节原文约631行，内容从机械开关的抖动（contact bounce）产生的瞬态、开关触点间的寄生电容、以及开关闭合时的瞬态电流对辐射的影响等方面展开。）*

机械开关的触点在闭合时会产生**抖动（bounce）**，每次抖动都产生快速瞬态电流，其频谱含量可延伸至数百MHz。此外，开关两触点之间存在**寄生电容**（pF级），在高频下提供耦合路径。开关触点材料（贵金属vs.普通金属）影响接触电阻的稳定性。

> **工程直觉:** 机械开关的EMC问题往往被低估。在产品使用期间反复操作的开关（如电源开关、模式切换开关）是潜在的辐射源。抑制措施包括在触点间并联 **RC缓冲网络**（吸收瞬态能量）或 **TVS二极管**。

---

## Summary: Nonideal Component Behavior at High Frequency

| Component | Nonideal Effect | Dominant Parasitic | Key Failure Mode |
|-----------|----------------|-------------------|-----------------|
| Wire | Skin effect | $R_{\text{hf}} \propto \sqrt{f}$ | Resistance not "flat"; internal $L$ decreases |
| Wire pair | Loop inductance | External $L_e \gg$ internal $L_i$ | Transmission-line behavior if $L > \lambda/10$ |
| PCB land | Edge crowding | $r_{\text{hf}} \propto 1/(w+t)$ | Same as wire |
| Resistor | Lead $L$+$C$ resonance | $L_{\text{lead}}$, $C_{\text{par}}$ | Self-resonance; above SRF → inductive |
| Capacitor | Lead $L$ resonance | $L_{\text{lead}}$, $R_s$ (ESR) | SRF; above SRF → inductive; larger $C$ → lower SRF |
| Inductor | Turn-to-turn $C$ resonance | $C_{\text{par}}$ | SRF; larger $L$ → lower SRF; wire-$R$ + core loss = ESR |
| Ferrite bead | Complex $\mu_r(f)$ | $R(f)$+$L(f)$ both $\propto f$ | Effective only above ~100 MHz; saturates at high $I$ |
| Common-mode choke | Coupling asymmetry | Leakage $L$, parasitic $C$ | Poor coupling → DM signal affected |

### Golden Rules for Component Selection in EMC

1. **永远检查SRF：** 任何用于EMI抑制的电容或电感，其目标噪声频率必须**低于**器件的自谐振频率。
2. **加大容值要谨慎：** 增大电容值→降低SRF，可能使原本在容性频段的电容在目标频率变成感性。
3. **引线越短越好：** $L_{\text{lead}} \propto$ lead length; SMT器件天然优于通孔器件。
4. **高阻抗并联/低阻抗串联：** 电容靠分流抑制高阻抗节点的噪声；电感靠串联增加低阻抗支路对噪声的阻塞。
5. **共模扼流圈是全能选手：** 理想情况下不影响差模（功能）信号，同时对共模辐射提供高阻抗+损耗。
6. **选对铁氧体材料：** 传导（≤30 MHz）用MnZn；辐射（≥30 MHz）用NiZn。

---

*DONE — Character count: see `wc -c`*
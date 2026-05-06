---
chapter: 2
title: Basic Concepts in RF Design
source: Razavi, "RF Microelectronics", 2nd Ed.
pages: p33-116 (book pp.7-86)
---

# Ch2: Basic Concepts in RF Design

## 2.1 General Considerations (p7-14)

### 2.1.1 Units in RF Design (p7-9)

**Decibel (dB):**
- Voltage gain: $A_V|_{\text{dB}} = 20 \log(V_{\text{out}}/V_{\text{in}})$
- Power gain: $A_P|_{\text{dB}} = 10 \log(P_{\text{out}}/P_{\text{in}})$

These are only equal when input and output impedances match.

**dBm:** Power relative to 1 mW.
$$P_{\text{sig}}|_{\text{dBm}} = 10 \log\left(\frac{P_{\text{sig}}}{1\,\text{mW}}\right)$$

**Key result:** 0 dBm into $50\,\Omega \implies V_{pp} = 632\,\text{mV}$ (derived from $V_{pp}^2/(8R_L) = 1\,\text{mW}$).

**Example 2.1 (p8):** 0 dBm into $50\,\Omega$ → $V_{pp} = 632\,\text{mV}$.

**Example 2.2 (p8-9):** GSM receiver at -100 dBm → $6.32\,\mu\text{V}_{pp}$ input. After 15 dB gain ($\times 5.62$) → $35.5\,\mu\text{V}_{pp}$ output.

### 2.1.2 Time Variance (p9-12)

- **Linear system:** superposition holds: $a y_1(t) + b y_2(t) = f[a x_1(t) + b x_2(t)]$
- **Time-invariant:** $y(t-\tau) = f[x(t-\tau)]$
- Switching circuit example (Fig. 2.2): with $v_{\text{in}2}$ as input, the system is **linear but time-variant**.
- $v_{\text{out}}(t) = v_{\text{in}2}(t) \cdot S(t)$ where $S(t)$ is a square wave.
- Output spectrum: $V_{\text{out}}(f) = V_{\text{in}2}(f) * \sum_{n=-\infty}^\infty \frac{\sin(n\pi/2)}{n\pi} \delta(f - n/T_1)$

**Example 2.3 (p10-11):** Switch driven by $\cos\omega_1t$, input $\cos(1.25\omega_1t)$. Output = product with square wave → convolution in freq domain.

**Key insight:** A linear time-variant system CAN generate new frequencies (not just nonlinear systems).

### 2.1.3 Nonlinearity (p12-14)

Memoryless nonlinear systems approximated by polynomial:
$$y(t) = \alpha_0 + \alpha_1 x(t) + \alpha_2 x^2(t) + \alpha_3 x^3(t) + \cdots$$

**Odd symmetry** (balanced/differential): $\alpha_j = 0$ for even $j$.

**Differential pair** (Eq. 2.19, 2.22):
$$V_{\text{out}} = \sqrt{\mu_n C_{ox}\frac{W}{L}I_{SS}} \left(1 - \frac{\mu_n C_{ox}W/L}{8 I_{SS}} V_{\text{in}}^2\right) R_D \, V_{\text{in}}$$

**Example 2.4 (p13):** Square-law MOS differential pair → linear term ($\sqrt{\mu_n C_{ox} W/L \cdot I_{SS}}\, R_D\, V_{\text{in}}$) + third-order term. Even-order terms vanish due to symmetry.

---

## 2.2 Effects of Nonlinearity (p14-35)

### 2.2.1 Harmonic Distortion (p14-16)

For $x(t) = A \cos \omega t$:
$$y(t) = \frac{\alpha_2 A^2}{2} + \left(\alpha_1 A + \frac{3\alpha_3 A^3}{4}\right)\cos\omega t + \frac{\alpha_2 A^2}{2}\cos 2\omega t + \frac{\alpha_3 A^3}{4}\cos 3\omega t$$

- Even-order → DC offset, $2^{nd}$ harmonic
- Odd-order → gain compression, $3^{rd}$ harmonic
- $n^{th}$ harmonic ∝ $A^n$

**Example 2.5 (p15-16):** Mixer with 3rd-order nonlinearity on one port → unwanted spurs at $\omega_1 \pm 3\omega_2$.

**Example 2.6 (p16):** GSM 900 MHz TX → 2nd harmonic falls in GSM-1800 band; 6th harmonic in 5 GHz WLAN band.

### 2.2.2 Gain Compression (p16-20)

For $\alpha_1 \alpha_3 < 0$ (compressive), gain = $\alpha_1 + \frac{3\alpha_3}{4}A^2$.

**1-dB compression point:**
$$20\log\left|\alpha_1 + \frac{3}{4}\alpha_3 A_{\text{in,1dB}}^2\right| = 20\log|\alpha_1| - 1\,\text{dB}$$
$$A_{\text{in,1dB}} = \sqrt{0.145 \left|\frac{\alpha_1}{\alpha_3}\right|}$$

**Desensitization:** For signal $A_1\cos\omega_1t$ + blocker $A_2\cos\omega_2t$ with $A_1 \ll A_2$:
$$y(t) = \left(\alpha_1 + \frac{3}{2}\alpha_3 A_2^2\right) A_1 \cos\omega_1 t + \cdots$$

**Example 2.7 (p19-20):** GSM TX (1W at 900 MHz) → 2nd harmonic must be >45 dB below fundamental to avoid desensitizing a 1.8 GHz RX ($P_{\text{1dB}}=-25$ dBm) at 1m distance with 10 dB attenuation.

### 2.2.3 Cross Modulation (p20-21)

AM interferer $A_2(1+m\cos\omega_m t)\cos\omega_2t$ transfers modulation to desired signal:
$$y(t) = \left[\alpha_1 + \frac{3}{2}\alpha_3 A_2^2\left(1+\frac{m^2}{2}+\frac{m^2}{2}\cos 2\omega_m t + 2m\cos\omega_m t\right)\right] A_1 \cos\omega_1 t + \cdots$$

**Example 2.8 (p21):** Phase-modulated interferers → NO cross modulation in memoryless systems. Dynamic nonlinear systems may differ.

### 2.2.4 Intermodulation (p21-33)

Two-tone test $x(t) = A_1\cos\omega_1t + A_2\cos\omega_2t$:

**Third-order IM products:**
$$2\omega_1 \pm \omega_2\!:\ \frac{3\alpha_3 A_1^2 A_2}{4}\cos(2\omega_1 \pm \omega_2)t$$
$$2\omega_2 \pm \omega_1\!:\ \frac{3\alpha_3 A_1 A_2^2}{4}\cos(2\omega_2 \pm \omega_1)t$$

**Critical:** $2\omega_1 - \omega_2$ and $2\omega_2 - \omega_1$ fall near $\omega_1,\omega_2$ if tones are close.

**Example 2.9 (p22-23):** Bluetooth: Users at 2.410, 2.420, 2.430 GHz → IM at 2.410 GHz corrupts User 4.

**Example 2.10 (p24):** LNA gain=10, $P_{\text{1dB}}=-30$ dBm. Interferers at -40 dBm → IM3 product = -59.3 dBm, same level as desired signal at -60 dBm, even though no compression occurs!

**Third Intercept Point (IP3):**
$$A_{\text{IIP3}} = \sqrt{\frac{4}{3}\left|\frac{\alpha_1}{\alpha_3}\right|}$$
$$\frac{A_{\text{IIP3}}}{A_{\text{1dB}}} = \sqrt{\frac{4}{0.435}} \approx 9.6\,\text{dB}$$

**Shortcut method (Eq. 2.56):** $P_{\text{IIP3}} = \frac{\Delta P}{2} + P_{\text{in}}$ where $\Delta P$ = difference between fundamental and IM3 at output.

**Example 2.11 (p27):** LNA: signal -80 dBm, interferers -20 dBm → need IIP3 = +15.2 dBm (extremely difficult) for IM to be 20 dB below signal.

### 2.2.5 Cascaded Nonlinear Stages (p29-33)

Cascade of two stages ($\alpha_1,\alpha_2,\alpha_3$ and $\beta_1,\beta_2,\beta_3$):
$$\frac{1}{A_{\text{IP3}}^2} \approx \frac{1}{A_{\text{IP3,1}}^2} + \frac{\alpha_1^2}{A_{\text{IP3,2}}^2}$$

For narrowband (IM products within band), the $\alpha_2\beta_2$ cross-term is heavily filtered.

**Key insight:** The IP3 of each later stage is divided by the total preceding voltage gain. The latter stages are MORE critical for linearity.

**Example 2.12 (p29-30):** Two differential stages → can't get infinite IP3 even with cancellation because both are compressive.

**Example 2.13 (p32):** LNA (IIP3=-10 dBm, gain=20 dB) + mixer (IIP3=+4 dBm). Scaled IIP3 of mixer = -16 dBm, which is WORSE than LNA → mixer limits IP3 more.

### 2.2.6 AM/PM Conversion (p33-35)

APC arises from dynamic nonlinearity:
- A nonlinear capacitor with even-order voltage dependence changes its average capacitance with amplitude
- This produces amplitude-dependent phase shift

**Example 2.14 (p35):** $C_1 = C_0(1+\alpha_1 V_{\text{out}} + \alpha_2 V_{\text{out}}^2)$ → phase shift contains $-\frac{\alpha_2}{2}R_1 C_0 \omega_1 V_1^2/2$. Odd-symmetric dependence causes no APC.

---

## 2.3 Noise (p35-58)

### 2.3.1-2 Noise as Random Process & Spectrum (p36-38)

- Noise power: $P_n = \lim_{T\to\infty} \frac{1}{T} \int_0^T n^2(t) dt$
- PSD: $S_x(f)$ = average power in 1 Hz bandwidth
- Total power: $\int_0^\infty S_x(f) df = \overline{x^2(t)}$

### 2.3.3 Effect of Transfer Function (p39-40)

For LTI system $H(s)$: $S_y(f) = S_x(f) |H(f)|^2$

### 2.3.4 Device Noise (p40-46)

**Resistor thermal noise:**
- Thevenin: $\overline{V_n^2} = 4kTR$ (V$^2$/Hz)
- Norton: $\overline{I_n^2} = 4kT/R$ (A$^2$/Hz)
- Available noise power: $kT = -173.8$ dBm/Hz at 300K
- Passivity theorem: noise of any passive network = $4kT\,\text{Re}\{Z_{\text{out}}\}$

**Example 2.15 (p38-39):** 50 $\Omega$ resistor → $\overline{V_n^2} = 8.28\times 10^{-19}$ V$^2$/Hz → $\sqrt{\overline{V_n^2}} = 0.91$ nV/$\sqrt{\text{Hz}}$.

**Example 2.16 (p40-41):** RLC tank noise peaks at resonance: $\overline{V_n^2} = 4kTR_1$ at $f_0$.

**MOSFET noise:**
- Channel thermal: $\overline{I_n^2} = 4kT\gamma g_m$ ($\gamma=2/3$ long-channel, $\gamma\rightarrow 2$ short-channel)
- Gate resistance: $R_G = (W/L)R_\square$, effective $\overline{V_n^2} = 4kT(R_G/3)$
- Flicker ($1/f$): $\overline{V_n^2} = \frac{K}{WLC_{ox}}\frac{1}{f}$
- $1/f$ corner: $f_c = \frac{K}{WLC_{ox}}\frac{g_m}{4kT\gamma}$

**Bipolar noise:**
- Base shot: $\overline{I_{n,b}^2} = 2qI_B = 2q I_C/\beta$
- Collector shot: $\overline{I_{n,c}^2} = 2qI_C = 4kT \cdot g_m/2$

### 2.3.5 Noise in Circuits (p46-58)

**Input-referred noise:** Model noisy circuit as noiseless with series $V_n^2$ + parallel $I_n^2$ at input.

**Example 2.18 (p47-48):** CG stage input-referred noise voltage $\approx 4kT\gamma/g_m$, current $= 4kT\gamma/(g_m R_1^2)$.

**Noise Figure (NF):**
$$\text{NF} = \frac{\text{SNR}_{\text{in}}}{\text{SNR}_{\text{out}}} = 1 + \frac{V_n^2}{|\alpha|^2 A_v^2} \cdot \frac{1}{4kTR_S}$$

Where $\alpha = Z_{\text{in}}/(Z_{\text{in}}+R_S)$.

**Calculation method:** $\text{NF} = \frac{\overline{V_{n,\text{out}}^2}}{A_0^2} \cdot \frac{1}{4kTR_S}$, where $A_0 = V_{\text{out}}/V_{\text{in}}$.

**Example 2.20 (p51):** Shunt resistor $R_P$ with source $R_S$ → $\text{NF} = 1 + R_S/R_P$. If $R_P = R_S$ (matching), NF = 3 dB minimum.

**Example 2.21 (p52):** CS stage → $\text{NF} = 1 + \gamma/(g_m R_S)$.

**Friis' Equation (cascaded NF):**
$$\text{NF}_{\text{tot}} = \text{NF}_1 + \frac{\text{NF}_2 - 1}{A_{P1}} + \frac{\text{NF}_3 - 1}{A_{P1}A_{P2}} + \cdots$$

Where $A_{P1}$ is the **available power gain** of stage 1.

**Example 2.22 (p55):** Cascade of two CS stages (both with infinite $R_{\text{in}}$):
$$\text{NF} = 1 + \frac{\gamma}{g_{m1}R_S} + \frac{\gamma}{g_{m1}^2 r_{O1}^2 g_{m2} R_S}$$

**Example 2.23 (p56):** CS + CG cascade → direct NF calculation required since Friis' is cumbersome with non-50$\Omega$ interfaces.

**NF of lossy passive circuits:** $\text{NF} = L$ (power loss of the network).

**Example 2.24 (p58):** BPF ($L=1.5$ dB) + LNA ($\text{NF}=2$ dB) → $\text{NF}_{\text{tot}} = L \cdot \text{NF}_{\text{LNA}} = 3.5$ dB.

---

## 2.4 Sensitivity and Dynamic Range (p58-62)

### 2.4.1 Sensitivity (p59-60)

$$P_{\text{sen}}|_{\text{dBm}} = -174\,\text{dBm/Hz} + \text{NF}|_{\text{dB}} + 10\log B + \text{SNR}_{\text{min}}|_{\text{dB}}$$

Where $-174$ dBm/Hz = $kT$ at 300K, $B$ = bandwidth.

**Example 2.25 (p60):** GSM (BW=200 kHz, SNR=12 dB) → $P_{\text{sen}}=-102$ dBm. WLAN (BW=20 MHz, SNR=23 dB) → $P_{\text{sen}}=-71$ dBm. WLAN appears worse but carries 200× data rate.

### 2.4.2 Dynamic Range (p60-62)

**Spurious-Free Dynamic Range (SFDR):**
$$P_{\text{in,max}} = \frac{2P_{\text{IIP3}} + (-174\,\text{dBm} + \text{NF} + 10\log B)}{3}$$
$$\text{SFDR} = \frac{2(P_{\text{IIP3}} - (-174\,\text{dBm}) - \text{NF} - 10\log B)}{3} - \text{SNR}_{\text{min}}$$

**Example 2.26 (p62):** $P_{\text{1dB}} > P_{\text{in,max}}$ typically → two-tone IM is more restrictive than single-tone compression.

---

## 2.5 Passive Impedance Transformation (p62-71)

### 2.5.1 Quality Factor (p63)
- Series RC: $Q_S = 1/(C\omega R_S)$
- Parallel RC: $Q_P = R_P/(1/(C\omega))$
- Series RL: $Q_S = L\omega/R_S$
- Parallel RL: $Q_P = R_P/(L\omega)$

### 2.5.2 Series-to-Parallel Conversion (p63-65)

For $Q^2 \gg 1$:
$$R_P \approx Q_S^2 R_S, \quad C_P \approx C_S$$

### 2.5.3 Basic Matching Networks (p65-69)

Four L-section topologies (Fig 2.62):
1. Series C & shunt L → transforms $R_L$ **down** (lower input impedance)
2. Series L & shunt C → transforms $R_L$ **down**
3. Shunt C & series L → transforms $R_L$ **up**
4. Shunt L & series C → transforms $R_L$ **up**

**Voltage/current transformation** in lossless network: $V_{\text{out}}/V_{\text{in}} = \sqrt{R_L/\text{Re}\{Z_{\text{in}}\}}$

**Example 2.27 (p66):** Match $50\;\Omega\rightarrow 25\;\Omega$ at 5 GHz. Exact: $C_1=0.637$ pF, $L_1=0.796$ nH (not $Q\gg 1$, so exact equations needed).

**Example 2.28 (p67):** Shunt L with series RL → parallel conversion gives $R_P = L_1^2\omega^2/R_L$, cancelled by shunt C.

**Example 2.29 (p68-69):** Swapping input/output inverts transformation ratio.

**Transformer:** $1:n$ turns ratio → $R_{\text{in}} = R_L/n^2$, $V_{\text{out}} = n V_{\text{in}}$.

### 2.5.4 Loss in Matching Networks (p69-71)

**Series loss model** (Fig 2.65): Loss $= 1 + R_S/R_{\text{in}1}$.

**Parallel loss model** (Fig 2.66): Loss $= 1 + R_L/R_P$.

---

## 2.6 Scattering Parameters (p71-75)

**S-parameter equations:**
$$V_1^- = S_{11} V_1^+ + S_{12} V_2^+$$
$$V_2^- = S_{21} V_1^+ + S_{22} V_2^+$$

- $S_{11}$ = input reflection coefficient ($V_1^-/V_1^+|_{V_2^+=0}$) — input matching
- $S_{12}$ = reverse isolation — coupling from output to input
- $S_{22}$ = output reflection coefficient — output matching
- $S_{21}$ = forward gain

**Input reflection coefficient:**
$$\Gamma_{\text{in}} = \frac{Z_{\text{in}} - R_S}{Z_{\text{in}} + R_S}$$

In dB: $S_{mn}|_{\text{dB}} = 20\log|S_{mn}|$

**Example 2.30 (p74-75):** CG stage S-parameters. $S_{11} = (1-g_m R_S - C_X s)/(1+g_m R_S + C_X s)$, $S_{12}=0$, $S_{22}$ from $Z_{\text{out}} = R_D || (C_Y s)^{-1}$, $S_{21}$ from gain expression.

---

## 2.7-2.8 Nonlinear Dynamic Systems & Volterra Series (p75-85)

### Dynamic Nonlinearity

Static nonlinearity $y(t)=\alpha_1 x+\alpha_2 x^2+\alpha_3 x^3$ is insufficient when reactive elements cause frequency-dependent nonlinear effects.

**Harmonic balance** approach: assume output form $y(t) = \sum a_n \cos(n\omega_1 t+\theta_n) + \sum \sum c_{m,n}\cos(\ldots)$, substitute into differential equation, solve.

### Volterra Series (p77-85)

General output for $N$ input exponentials:
$$V_{\text{out}}(t) = \sum_{k=1}^N H_1(\omega_k)V_0 e^{j\omega_k t} + \sum\sum H_2(\omega_m,\pm\omega_k)V_0^2 e^{j(\omega_m\pm\omega_k)t} + \cdots$$

Where $H_n$ are Volterra kernels computed recursively.

**Example 2.31 (p78):** $H_2$ for RC with $C_1 = C_0(1+\alpha V_{\text{out}})$:
$$H_2(\omega_1,\omega_2) = -\alpha R_1 C_0 j(\omega_1+\omega_2) H_1(\omega_1) H_1(\omega_2) H_1(\omega_1+\omega_2)$$

**Example 2.32 (p79):** 2nd harmonic amplitude for same circuit = $\frac{2|\alpha|R_1 C_0 \omega_1 V_0^2}{(R_1^2 C_0^2 \omega_1^2+1)\sqrt{4R_1^2 C_0^2 \omega_1^2+1}}$.

**Example 2.33 (p79):** Ratio of $A_{\omega_1+\omega_2}/A_{\omega_1-\omega_2}$ determined by $H_1$ frequency dependence.

**Example 2.34 (p80):** $H_3(\omega_1,\omega_2,\omega_3)$ for the same RC circuit — involves cross-products of $H_1$ and $H_2$ terms.

**Method of Nonlinear Currents (p81-85):**
1. Find linear response $H_1$
2. Compute voltage across nonlinear device
3. Calculate nonlinear current source
4. Compute circuit response to this current source (with input = 0)

**Example 2.35 (p82-83):** Using nonlinear current method to find $H_2$ and $H_3$.

**Example 2.36 (p83-85):** CS LNA with source degeneration $L_1$. Even though the transistor has only $2^{nd}$-order nonlinearity ($I_D \propto V_{\text{GS}}^2$), source degeneration feedback produces $3^{rd}$-order terms. Third-order nonlinear current:
$$I_{D,\text{non}} = 2\alpha[H_1(\omega_1)H_2(\omega_2,\omega_3) + H_1(\omega_2)H_2(\omega_1,\omega_3) + H_1(\omega_3)H_2(\omega_1,\omega_2)] V_0^3 e^{j(\omega_1+\omega_2+\omega_3)t}$$

---

## Physical/Engineering Intuition

1. **Desensitization vs IM:** A single large blocker desensitizes (reduces gain); two large blockers create IM products that can fall directly on the desired channel. The latter is usually more restrictive.

2. **P1dB vs IIP3:** IIP3 is ~9.6 dB above P1dB in a pure $3^{rd}$-order system. This ratio is a useful sanity check.

3. **Cascaded IP3:** Later stages dominate because their IP3 is "divided" by the preceding gain. The mixer after an LNA often limits receiver linearity.

4. **Friis vs Direct NF:** Friis' equation requires available power gains and is cumbersome for modern CMOS stages with non-50$\Omega$ interfaces. Direct calculation (divide total output noise by total voltage gain) is often simpler.

5. **NF of lossy front-end:** Passive filter loss adds directly to NF. A 3-dB loss = 3-dB NF degradation.

6. **S-parameters** are measurement-friendly but less natural for CMOS cascade analysis where stages don't provide internal matching.

7. **Memoryless vs dynamic nonlinearity:** Many RF effects (AM/PM, frequency-dependent IM) require dynamic nonlinear analysis. Volterra series is the rigorous tool.

# Chapter 9: Radiating Systems, Multipole Fields and Radiation

> Jackson *Classical Electrodynamics*, 3rd Ed, §9.1–9.14

---

## 1. Overview — Why Multipoles Matter

When a localized charge/current distribution oscillates in time, it radiates electromagnetic waves. The multipole expansion lets us decompose the radiation field into contributions of increasing angular complexity:
- **Electric dipole** (dominant for most antennas)
- **Magnetic dipole** (loops, small coils)
- **Electric quadrupole** (symmetric arrangements, next order)

**Key insight**: For a source region small compared to wavelength ($d \ll \lambda$), higher multipoles are suppressed by powers of $(d/\lambda)$, so the lowest non-vanishing multipole dominates.

---

## 2. 时谐场中的矢势 (Vector Potential for Time-Harmonic Fields)

Assume $e^{-i\omega t}$ time dependence. For a current density $\mathbf{J}(\mathbf{x}')$ localized in a volume $V$:

$$
\mathbf{A}(\mathbf{x}) = \frac{\mu_0}{4\pi} \int_V \mathbf{J}(\mathbf{x}') \frac{e^{ik|\mathbf{x} - \mathbf{x}'|}}{|\mathbf{x} - \mathbf{x}'|} d^3x'
$$

where $k = \omega/c = 2\pi/\lambda$.

**Regions of interest**:
- **Near zone** ($kr \ll 1$): quasistatic fields
- **Intermediate zone** ($kr \sim 1$): transition
- **Far zone / Radiation zone** ($kr \gg 1$): $1/r$ fields dominate, outward energy flow

---

## 3. 远场近似 (Far-Field Approximation)

In the far zone ($r \gg r'$, $kr \gg 1$):

$$
|\mathbf{x} - \mathbf{x}'| \approx r - \mathbf{n} \cdot \mathbf{x}'
$$

$$
\frac{e^{ik|\mathbf{x} - \mathbf{x}'|}}{|\mathbf{x} - \mathbf{x}'|} \approx \frac{e^{ikr}}{r} e^{-ik\mathbf{n} \cdot \mathbf{x}'}
$$

Hence:

$$
\mathbf{A}(\mathbf{x}) \approx \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} \int_V \mathbf{J}(\mathbf{x}') e^{-ik\mathbf{n} \cdot \mathbf{x}'} d^3x'
$$

This is the **fundamental formula** for all antenna and multipole calculations.

---

## 4. 多极展开 (Multipole Expansion)

Expand the plane-wave factor:

$$
e^{-ik\mathbf{n} \cdot \mathbf{x}'} = 1 - ik(\mathbf{n} \cdot \mathbf{x}') - \frac{1}{2} k^2 (\mathbf{n} \cdot \mathbf{x}')^2 + \cdots
$$

### 4.1 Electric Dipole Term (Leading Order)

$$
\mathbf{A}(\mathbf{x}) \approx \frac{\mu_0}{4\pi} \frac{e^{ikr}}{r} \int_V \mathbf{J}(\mathbf{x}') d^3x'
$$

Using the identity $\int \mathbf{J} d^3x = -i\omega \mathbf{p}$ where $\mathbf{p}$ is the electric dipole moment:

$$
\mathbf{A}_{\text{ED}}(\mathbf{x}) = -\frac{i\mu_0 \omega}{4\pi} \frac{e^{ikr}}{r} \mathbf{p}
$$

**Radiation fields**:

$$
\mathbf{B} = ik(\mathbf{n} \times \mathbf{A}), \quad \mathbf{E} = c(\mathbf{B} \times \mathbf{n})
$$

$$
\mathbf{B}_{\text{ED}} = -\frac{\mu_0 \omega^2}{4\pi c} \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{p})
$$

$$
\mathbf{E}_{\text{ED}} = \frac{1}{4\pi \epsilon_0} k^2 \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{p}) \times \mathbf{n}
$$

**Angular distribution**:

$$
\frac{dP}{d\Omega} = \frac{c^2 Z_0}{32\pi^2} k^4 |\mathbf{n} \times \mathbf{p}|^2 = \frac{Z_0}{32\pi^2} \omega^4 |\mathbf{p}|^2 \sin^2\theta
$$

**Total power** (Larmor formula generalization):

$$
P = \frac{Z_0 \omega^4 |\mathbf{p}|^2}{12\pi c^2} = \frac{\mu_0 \omega^4 |\mathbf{p}|^2}{12\pi c}
$$

### 4.2 Magnetic Dipole Term

From the $ik(\mathbf{n} \cdot \mathbf{x}')$ term, there is both an electric quadrupole and a magnetic dipole contribution.

**Magnetic dipole moment**:

$$
\mathbf{m} = \frac{1}{2} \int \mathbf{x}' \times \mathbf{J}(\mathbf{x}') d^3x'
$$

$$
\mathbf{A}_{\text{MD}}(\mathbf{x}) = \frac{i\mu_0 k}{4\pi} \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{m})
$$

**Radiation fields**:

$$
\mathbf{B}_{\text{MD}} = -\frac{\mu_0 \omega^2}{4\pi c^2} \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{m}) \times \mathbf{n}
$$

$$
\mathbf{E}_{\text{MD}} = -\frac{Z_0 \mu_0 \omega^2}{4\pi c} \frac{e^{ikr}}{r} (\mathbf{n} \times \mathbf{m})
$$

**Total power**:

$$
P_{\text{MD}} = \frac{Z_0 \omega^4 |\mathbf{m}|^2}{12\pi c^4}
$$

**Comparison**: $\displaystyle \frac{P_{\text{MD}}}{P_{\text{ED}}} \sim \left(\frac{|\mathbf{m}|}{c|\mathbf{p}|}\right)^2 \sim \left(\frac{\text{source size}}{\lambda}\right)^2 \ll 1$ for small sources.

### 4.3 Electric Quadrupole Term

**Electric quadrupole moment tensor**:

$$
Q_{\alpha\beta} = \int (3x'_\alpha x'_\beta - r'^2 \delta_{\alpha\beta}) \rho(\mathbf{x}') d^3x'
$$

**Radiation fields**:

$$
\mathbf{B}_{\text{EQ}} = -\frac{i\mu_0 \omega^3}{24\pi c^2} \frac{e^{ikr}}{r} \mathbf{n} \times \mathbf{Q}(\mathbf{n})
$$

where $\mathbf{Q}(\mathbf{n})$ is the vector $\mathbf{Q}_\alpha = \sum_\beta Q_{\alpha\beta} n_\beta$.

**Angular distribution**:

$$
\frac{dP}{d\Omega} = \frac{Z_0 \omega^6}{288\pi^2 c^4} |\mathbf{n} \times \mathbf{Q}(\mathbf{n})|^2
$$

**Total power**:

$$
P_{\text{EQ}} = \frac{Z_0 \omega^6}{1440\pi c^4} \sum_{\alpha\beta} |Q_{\alpha\beta}|^2
$$

---

## 5. 天线的辐射 (Radiation from Antennas)

### 5.1 短天线 / 赫兹偶极子 (Short Dipole / Hertzian Dipole)

A short wire of length $l \ll \lambda$ carrying uniform current $I_0 e^{-i\omega t}$:

$$
\mathbf{p} = \frac{i I_0 l}{\omega} \hat{\mathbf{z}}
$$

**Radiation resistance**:

$$
R_{\text{rad}} = \frac{2P}{I_0^2} = \frac{Z_0}{6\pi} \left(\frac{l}{\lambda}\right)^2 \approx 80\pi^2 \left(\frac{l}{\lambda}\right)^2
$$

### 5.2 半波偶极子 (Half-Wave Dipole $l = \lambda/2$)

Current distribution: $I(z) = I_0 \cos(kz)$ for $|z| \leq \lambda/4$

**Far-field**:

$$
\mathbf{E}_\theta = \frac{i Z_0 I_0 e^{ikr}}{2\pi r} \frac{\cos(\frac{\pi}{2}\cos\theta)}{\sin\theta}
$$

**Radiation resistance**: $R_{\text{rad}} \approx 73 \, \Omega$

**Directivity**: $D = 1.64$ (2.15 dB)

### 5.3 天线阵列 (Antenna Arrays)

Array factor for $N$ identical elements at positions $\mathbf{x}_j$:

$$
F(\mathbf{n}) = \sum_{j=1}^N a_j e^{-ik\mathbf{n} \cdot \mathbf{x}_j}
$$

**Linear array** (spacing $d$, phase shift $\delta$):

$$
F(\theta) = \sum_{j=0}^{N-1} e^{-ij(kd\cos\theta + \delta)} = \frac{\sin\left[\frac{N}{2}(kd\cos\theta + \delta)\right]}{\sin\left[\frac{1}{2}(kd\cos\theta + \delta)\right]}
$$

- **Broadside** ($\delta=0$): main lobe perpendicular to array
- **End-fire** ($\delta = -kd$): main lobe along array axis

### 5.4 相位阵列 / 波束成形 (Phased Arrays / Beamforming)

By electronically adjusting $\delta$, the beam direction can be steered without mechanical movement. Used in radar, 5G, satellite communications.

---

## 6. 球谐展开 (Spherical Harmonic Expansion)

For a completely general source, expand the vector potential in vector spherical harmonics:

$$
\mathbf{A}(\mathbf{x}) = \frac{\mu_0}{4\pi} \sum_{lm} \left[ a_E(l,m) \mathbf{X}_{lm}(\theta,\phi) + a_M(l,m) \mathbf{Y}_{lm}(\theta,\phi) \right] h_l^{(1)}(kr)
$$

- $l=1$ → dipole terms
- $l=2$ → quadrupole terms
- **Transverse electric (TE)** modes: multipole index $a_E(l,m)$
- **Transverse magnetic (TM)** modes: $a_M(l,m)$

**Total radiated power**:

$$
P = \frac{Z_0}{2k^2} \sum_{lm} \left[ |a_E(l,m)|^2 + |a_M(l,m)|^2 \right]
$$

---

## 7. 重要公式速查 (Key Formulas Cheat Sheet)

| Quantity | Electric Dipole | Magnetic Dipole | Electric Quadrupole |
|---|---|---|---|
| Source moment | $\mathbf{p} = \int \mathbf{x}' \rho d^3x'$ | $\mathbf{m} = \frac12 \int \mathbf{x}' \times \mathbf{J} d^3x'$ | $Q_{\alpha\beta} = \int (3x'_\alpha x'_\beta - r'^2\delta_{\alpha\beta})\rho d^3x'$ |
| $\mathbf{A}$ in far zone | $-\frac{i\mu_0\omega}{4\pi}\frac{e^{ikr}}{r}\mathbf{p}$ | $\frac{i\mu_0 k}{4\pi}\frac{e^{ikr}}{r}(\mathbf{n}\times\mathbf{m})$ | $-\frac{\mu_0 \omega k}{24\pi}\frac{e^{ikr}}{r}\mathbf{Q}(\mathbf{n})$ |
| $P_{\text{total}}$ | $\frac{Z_0\omega^4|\mathbf{p}|^2}{12\pi c}$ | $\frac{Z_0\omega^4|\mathbf{m}|^2}{12\pi c^4}$ | $\frac{Z_0\omega^6}{1440\pi c^4}\sum_{\alpha\beta}|Q_{\alpha\beta}|^2$ |
| Angular dep. | $\sin^2\theta$ | $\sin^2\theta$ (about $\mathbf{m}$ axis) | More complex |
| Scaling | $\propto (l/\lambda)^2$ | $\propto (l/\lambda)^2 \cdot (l/\lambda)^2$ | $\propto (l/\lambda)^4$ |

---

## 8. 物理直觉 (Physical Intuition)

1. **A static charge doesn't radiate** — acceleration is needed ($\ddot{\mathbf{p}} \neq 0$)
2. **Electric dipole dominates** because it's the lowest order; magnetic dipole and electric quadrupole are down by $(d/\lambda)^2$
3. **Symmetry matters**: a symmetric charge distribution ($\mathbf{p}=0$) radiates via higher multipoles
4. **Antenna as impedance transformer**: matches waveguide impedance to free-space impedance ($Z_0 \approx 377\,\Omega$)
5. **Reciprocity**: an antenna's receiving pattern = its transmitting pattern

---

## 9. Application Notes

- **Wireless power transfer**: near-field ($kr \ll 1$), primarily magnetic induction
- **Radio/TV broadcast**: half-wave dipoles and arrays for directional coverage
- **MRI systems**: magnetic dipole radiation from precessing nuclear spins
- **Gravitational wave detection**: electric quadrupole radiation (mass quadrupole)
- **Nano-antennas**: plasmonic structures, enhanced dipole moments at resonance

---

## References

- Jackson §9.1–§9.14 (full derivations)
- Balanis, *Antenna Theory* (engineering perspective)
- Kraus & Marhefka, *Antennas* (practical design)

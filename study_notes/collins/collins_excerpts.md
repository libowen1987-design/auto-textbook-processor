> **备注：** 此文件为原文摘录/旧版备份，非正式笔记。中英双语笔记请查看 notes/ 目录下的对应章节文件。

# Collins PDF 原文摘录 (Foundations for Microwave Engineering, 2nd Ed.)

---

## Ch1 (§1.1, pp. 1–2) — 频率定义与频段表

> "The descriptive term microwaves is used to describe electromagnetic waves with wavelengths ranging from 1 cm to 1 m. The corresponding frequency range is 300 MHz up to 30 GHz for 1-cm-wavelength waves. Electromagnetic waves with wavelengths ranging from 1 to 10 mm are called millimeter waves." (§1.1, p. 1)

> "Thus by the term microwave engineering we shall mean generally the engineering and design of information-handling systems in the frequency range from 1 to 100 GHz corresponding to wavelengths as long as 30 cm and as short as 3 mm." (§1.1, p. 3)

**Table 1.1** — Frequency Band Designation (VLF through EHF with services)
**Table 1.2** — Microwave Frequency Band Designation (Old: VHF,L,S,C,X,Ku,K,Ka vs New: C,D,E,F,G,H,I,J,K)

---

## Ch1 (§1.2, pp. 5–6) — 工业加热/ISM 频段

> "The domestic microwave oven operates at 2,450 MHz and uses a magnetron tube with a power output of 500 to 1000 W. For industrial heating applications, such as drying grain, manufacturing wood and paper products, and material curing, the frequencies of 915 and 2,450 MHz have been assigned." (§1.2, p. 6)

> ⚠️ Collin 原文未使用 "ISM" 缩写。此处"have been assigned"指工业加热用途。

---

## Ch2 (§2.1, pp. 17–23) — Maxwell's Equations

**Time-domain (script letters) Eqs. (2.13a–d), p. 21:**
> ∇ × ℰ = −∂ℬ/∂t (2.13a)
> ∇ × ℋ = ∂𝒟/∂t + 𝒥 (2.13b)
> ∇ · 𝒟 = ρ (2.13c)
> ∇ · ℬ = 0 (2.13d)

**Continuity Eq. (2.12), p. 20:**
> ∇ · 𝒥 + ∂ρ/∂t = 0 (2.12)

**Phasor-form Eqs. (2.18a–d), p. 23:**
> ∇ × E = −jωB (2.18a)
> ∇ × H = jωD + J (2.18b)
> ∇ · D = ρ (2.18c)
> ∇ · B = 0 (2.18d)

**Wave equation (2.44), p. 32: ∇²ℰ − μϵ ∂²ℰ/∂t² = 0**
**Helmholtz equation (2.45), p. 33: ∇²E + k²E = 0**
**Wave number (2.46): k = ω√(μϵ) = ω/v = 2π/λ**

---

## Ch3 (§3.1, pp. 72–76) — Transmission Line Equations

**Telegrapher's equations (3.1a–b), p. 72:**
> −∂V/∂z = R I + L ∂I/∂t
> −∂I/∂z = G V + C ∂V/∂t

**Wave equation (3.2a): ∂²V/∂z² = LC ∂²V/∂t² + (RC+GL)∂V/∂t + RG V**

**Propagation constant (3.22): γ = √[(R + jωL)(G + jωC)]**
**Characteristic impedance: Z₀ = √[(R + jωL)/(G + jωC)]**

---

## Ch4 (§4.3, pp. 230–232) — Foster's Reactance Theorem

> "the slope of the reactance is always positive; that is, dX/dω > 0. This positive-slope condition means that the poles and zeros of X must alternate as ω is increased from zero to infinity. We shall show below that this is a general property of any reactive one-port circuit, a result known as Foster's reactance theorem." (§4.3, p. 230)

**Eq. (4.20):** Z_sc = jZ₀ tan(k₀l)  (short-circuited coaxial line)
**Eq. (4.21):** Infinite product and partial fraction expansion of tan(k₀l)

---

## Ch4 (§4.7, pp. 248–254) — S-parameter Definition

> Scattering matrix relates incident and reflected wave amplitudes: **b = S a**
> where: aₙ = incident wave amplitude at port n, bₙ = reflected wave

> **Sₘₙ = bₘ/aₙ|_{aₖ=0 for k≠n}** — output at port m when port n is excited and all other ports are matched.

> **Unitary property for lossless:** S†S = I
> **Reciprocal:** Sₘₙ = Sₙₘ

> **Relationship to voltage/current:**
> Vₙ = √Z₀ₙ (aₙ + bₙ)
> Iₙ = (1/√Z₀ₙ)(aₙ − bₙ)

---

## Ch4 (§4.9, pp. 257–260) — ABCD Matrix

> [V₁; I₁] = [A B; C D] [V₂; −I₂]

> **Properties:** AD − BC = 1 (reciprocal), A = D (symmetric), A,D real and B,C imaginary (lossless)
> **Cascade:** T_total = T₁ · T₂

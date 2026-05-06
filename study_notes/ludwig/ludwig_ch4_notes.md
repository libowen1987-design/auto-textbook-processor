---
title: "Chapter 4 — Single- and Multiport Networks"
book: "RF Circuit Design — 2nd Ed."
author: "Reinhold Ludwig, Gene Bogdanov"
pages: "157–208"
processed: "2026-05-03"
tags: [S-parameters, ABCD-matrix, Z-parameters, Y-parameters, signal-flow-graph, TRL]
---

# Chapter 4: Single- and Multiport Networks

> **Overview:** This chapter covers network parameter representations essential for RF circuit analysis: impedance (Z), admittance (Y), hybrid (h), chain (ABCD), and scattering (S) parameters. It also introduces signal flow graphs and the TRL calibration technique.

---

## 4.1 Basic Definitions

### Impedance (Z) Parameters

$$
\begin{bmatrix} V_1 \\ V_2 \end{bmatrix} = \begin{bmatrix} Z_{11} & Z_{12} \\ Z_{21} & Z_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \end{bmatrix} \tag{4.2}
$$

$$
Z_{nm} = \frac{V_n}{I_m}\Big|_{I_k = 0,\ k\neq m} \tag{4.4}
$$

### Admittance (Y) Parameters

$$
\begin{bmatrix} I_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} Y_{11} & Y_{12} \\ Y_{21} & Y_{22} \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \end{bmatrix} \tag{4.5}
$$

$$
Y_{nm} = \frac{I_n}{V_m}\Big|_{V_k = 0,\ k\neq m} \tag{4.7}
$$

$[Z] = [Y]^{-1}$ for reciprocal networks. Passive linear networks are symmetric: $Z_{12} = Z_{21}$, $Y_{12} = Y_{21}$.

> **Example 4-1:** $\pi$-network with $Z_A, Z_B, Z_C$:
> $$
> Z_{11} = \frac{Z_A(Z_B+Z_C)}{Z_A+Z_B+Z_C},\quad Z_{22} = \frac{Z_C(Z_A+Z_B)}{Z_A+Z_B+Z_C}
> $$
> $$
> Z_{12} = Z_{21} = \frac{Z_A Z_C}{Z_A+Z_B+Z_C}
> $$
> $$
> Y = \begin{bmatrix} Y_A+Y_B & -Y_B \\ -Y_B & Y_B+Y_C \end{bmatrix}
> $$

### ABCD (Chain) Parameters

$$
\begin{bmatrix} V_1 \\ I_1 \end{bmatrix} = \begin{bmatrix} A & B \\ C & D \end{bmatrix} \begin{bmatrix} V_2 \\ I_2 \end{bmatrix} \tag{4.10}
$$

For reciprocal networks: $AD - BC = 1$.

### Hybrid (h) Parameters

$$
\begin{bmatrix} V_1 \\ I_2 \end{bmatrix} = \begin{bmatrix} h_{11} & h_{12} \\ h_{21} & h_{22} \end{bmatrix} \begin{bmatrix} I_1 \\ V_2 \end{bmatrix} \tag{4.11}
$$

Common in BJT datasheets: $h_{ie}, h_{re}, h_{fe}, h_{oe}$.

> **Examples 4-2/4-3:** BJT hybrid parameters:
> $$
> h_{11} \approx r_{BE},\quad h_{12} \approx \frac{r_{BE}}{r_{BC}},\quad h_{21} \approx \beta,\quad h_{22} \approx \frac{1}{r_{CE}} + \frac{1}{r_{BC}}
> $$

---

## 4.2 Interconnecting Networks

- **Series** → add Z matrices
- **Parallel** → add Y matrices
- **Cascade** → multiply ABCD matrices: $[ABCD]_{\text{total}} = [ABCD]_1 \cdot [ABCD]_2$

---

## 4.4 Scattering (S) Parameters

### Definition

Normalized incident and reflected power waves:

$$
a_n = \frac{V_n + Z_0 I_n}{2\sqrt{Z_0}},\quad b_n = \frac{V_n - Z_0 I_n}{2\sqrt{Z_0}} \tag{4.36}
$$

Inversion: $V_n = \sqrt{Z_0}(a_n + b_n)$, $I_n = (a_n - b_n)/\sqrt{Z_0}$.

### S-Matrix

$$
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix} = \begin{bmatrix} S_{11} & S_{12} \\ S_{21} & S_{22} \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} \tag{4.41}
$$

- $S_{11}$: input reflection coefficient ($a_2=0$)
- $S_{21}$: forward transmission gain
- $S_{22}$: output reflection coefficient ($a_1=0$)
- $S_{12}$: reverse transmission gain

### Key Relations

Return Loss: $\text{RL} = -20\log|S_{11}|$ dB

VSWR: $\text{VSWR} = \frac{1+|S_{11}|}{1-|S_{11}|}$

Forward power gain: $G_T = |S_{21}|^2$

### Signal Flow Graphs

**Building blocks** (Table 4-3): nodes, branches, series/parallel connections, self-loops.

**Mason's rule simplification** (Example 4-8):
Input reflection coefficient with mismatched load:

$$
\Gamma_{\text{in}} = S_{11} + \frac{S_{12}S_{21}\Gamma_L}{1 - S_{22}\Gamma_L} \tag{4.91}
$$

> **Example 4-9:** TL input impedance via signal flow:
> $\Gamma_{\text{in}} = \Gamma_L e^{-j2\beta l}$, $Z_{\text{in}} = Z_0 \frac{1+\Gamma_{\text{in}}}{1-\Gamma_{\text{in}}}$

### TRL Calibration

Three standards: Through ($S_{11}=S_{22}=0$, $S_{12}=S_{21}=1$), Reflect ($\Gamma$), Line ($e^{-\gamma l}$). Solves for 6 error coefficients (Fig. 4-30).

---

## 审计表 (Audit)

| 项目 | 状态 | 备注 |
|------|------|------|
| §4.1 Z/Y/h/ABCD 参数 | ✅ | Ex4-1 π网络 |
| §4.1 BJT h参数 | ✅ | Ex4-2, Ex4-3 |
| §4.2 网络互连 | ✅ | 级联/串/并联 |
| §4.4 S参数 | ✅ | 定义/测量/SFG |
| §4.4 信号流图 | ✅ | Ex4-8, Ex4-9 |
| §4.4 TRL校准 | ✅ | 误差盒方法 |
| 例题代码复现 | ✅ | S参数计算+SFG |

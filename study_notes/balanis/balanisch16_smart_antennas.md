# Chapter 16: Smart Antennas — Balanis Antenna Theory (4th Ed.)

> **Tutorial chapter**: Covers smart antenna system architectures, DOA estimation, and adaptive beamforming algorithms.

---

## §16.1 Introduction

Smart antennas combine an array of antenna elements with real-time signal processing to:

- **Enhance desired signals** via adaptive beamforming
- **Suppress interference** by steering nulls toward interferers
- **Track mobile users** in dynamic environments
- **Increase system capacity** (SDMA — Space Division Multiple Access)

Key applications: cellular base stations (4G/5G), radar, sonar, GPS anti-jam, cognitive radio.

---

## §16.2 Smart Antenna System Architecture

### Switched Beam vs. Adaptive Array

| Feature | Switched Beam | Adaptive Array |
|---------|---------------|----------------|
| Beam pattern | Predefined, fixed beams | Dynamically computed |
| Interference rejection | Limited (off-boresight) | ✓ **Nulls placed on interferers** |
| Computational cost | Low | High |
| Tracking | Beam-switching only | Continuous adaptation |
| Channel capacity | Limited | Maximum (optimal SINR) |
| Typical N beams | N = number of elements | N/A |

**Switched beam**: A Butler matrix or similar feed selects among K pre-computed beams. When the user moves between sectors, the base station switches beams. Simple but suboptimal in interference-rich environments.

**Adaptive array**: Weights $w_i$ are computed in real-time using DSP to maximize SINR. The pattern adapts continuously — peaks toward desired signals, nulls toward interferers.

### Digital Beamforming Architecture

```
Antenna elements → LNA → Downconverter → ADC → Digital Processor → w^H x(t)
  [0] ───── RF chain 0 ────▶ ADC ──▶ x₀[n]
  [1] ───── RF chain 1 ────▶ ADC ──▶ x₁[n]    ─▶ w₀* x₀ + w₁* x₁ + ...
  [2] ───── RF chain 2 ────▶ ADC ──▶ x₂[n]
  ...
  [M-1] ── RF chain M-1 ── ADC ──▶ x_{M-1}[n]
```

The baseband processor forms the array output as a linear combination of element signals:

$$y(t) = \mathbf{w}^H \mathbf{x}(t)$$

where $\mathbf{w} = [w_0, w_1, \ldots, w_{M-1}]^T$ is the complex weight vector.

---

## §16.3 Array Fundamentals

### Uniform Linear Array (ULA)

For an $M$-element ULA with inter-element spacing $d = \lambda/2$:

**Array response (steering) vector**:

$$\mathbf{a}(\theta) = \left[1,\; e^{-j\frac{2\pi}{\lambda} d \sin\theta},\; e^{-j\frac{2\pi}{\lambda} 2d \sin\theta},\; \ldots,\; e^{-j\frac{2\pi}{\lambda} (M-1)d \sin\theta}\right]^T$$

With $d = \lambda/2$, this simplifies to:

$$\mathbf{a}(\theta) = \left[1,\; e^{-j\pi \sin\theta},\; e^{-j2\pi \sin\theta},\; \ldots,\; e^{-j(M-1)\pi \sin\theta}\right]^T$$

The **array factor** (AF) for weights $\mathbf{w}$ is:

$$\text{AF}(\theta) = \sum_{m=0}^{M-1} w_m e^{-j m \pi \sin\theta} = \mathbf{w}^H \mathbf{a}(\theta)$$

**Conventional beamformer** (uniform weights, steered to $\theta_0$):

$$\mathbf{w} = \frac{1}{M} \mathbf{a}(\theta_0) \quad \Rightarrow \quad \text{AF}(\theta) = \frac{1}{M} \sum_{m=0}^{M-1} e^{-j m \pi (\sin\theta - \sin\theta_0)}$$

Beamwidth (HW) ≈ $\frac{0.886 \lambda}{M d \cos\theta_0}$ rad (for $d = \lambda/2$ and broadside).

### Signal Model

The received signal vector at time $t$:

$$\mathbf{x}(t) = \sum_{k=1}^{K} \mathbf{a}(\theta_k) s_k(t) + \mathbf{n}(t)$$

where:
- $K$ = number of sources (signals + interferers)
- $s_k(t)$ = complex baseband signal from source $k$
- $\mathbf{n}(t)$ = AWGN noise vector, $\mathcal{CN}(0, \sigma_n^2 \mathbf{I})$

### Array Covariance Matrix

For $N$ snapshots (sampling at $t = 1, 2, \ldots, N$):

$$\mathbf{R}_{xx} = \frac{1}{N} \sum_{t=1}^{N} \mathbf{x}(t) \mathbf{x}^H(t)$$

In the limit of infinite samples:

$$\mathbf{R}_{xx} = \mathbb{E}[\mathbf{x} \mathbf{x}^H] = \mathbf{A} \mathbf{R}_{ss} \mathbf{A}^H + \sigma_n^2 \mathbf{I}$$

where $\mathbf{A} = [\mathbf{a}(\theta_1), \ldots, \mathbf{a}(\theta_K)]$ is the $M \times K$ array manifold matrix, and $\mathbf{R}_{ss} = \mathbb{E}[\mathbf{s} \mathbf{s}^H]$ is the $K \times K$ source covariance.

---

## §16.4 Direction-of-Arrival (DOA) Estimation

### 16.4.1 Conventional Beamforming (Bartlett)

Spatial spectrum (analogous to periodogram in spectral analysis):

$$P_{\text{Bartlett}}(\theta) = \frac{\mathbf{a}^H(\theta) \mathbf{R}_{xx} \mathbf{a}(\theta)}{M^2}$$

Peaks occur at source DOAs. Resolution is limited by the Rayleigh (Fourier) limit — cannot resolve sources closer than approximately the beamwidth $\approx \lambda/(M d)$.

**Strength**: Simple, robust.
**Weakness**: Poor resolution, high sidelobes.

### 16.4.2 Capon's Method (MVDR)

Minimum Variance Distortionless Response (MVDR), also called **Minimum Variance** beamformer:

$$P_{\text{Capon}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta)}$$

**Idea**: A spatial filter that passes the direction $\theta$ with unit gain while minimizing total output power from all other directions.

**Resolution**: Better than Bartlett. Can resolve sources closer than the beamwidth, limited by array geometry and SNR.

### 16.4.3 MUSIC (MUltiple SIgnal Classification) — §16.4.3

**Key insight**: The signal vectors $\mathbf{x}(t)$ lie in a $K$-dimensional subspace (signal subspace) of the $M$-dimensional observation space. The noise occupies the orthogonal $(M-K)$-dimensional subspace.

**Algorithm**:

1. **EVD of $\mathbf{R}_{xx}$**:
   $$\mathbf{R}_{xx} = \mathbf{U}_s \mathbf{\Lambda}_s \mathbf{U}_s^H + \mathbf{U}_n \mathbf{\Lambda}_n \mathbf{U}_n^H$$

   where:
   - $\mathbf{U}_s$ = $M \times K$ matrix of signal eigenvectors (largest $K$ eigenvalues)
   - $\mathbf{U}_n$ = $M \times (M-K)$ matrix of noise eigenvectors (smallest $M-K$ eigenvalues)
   - $\mathbf{\Lambda}_s = \text{diag}(\lambda_1, \ldots, \lambda_K)$ with $\lambda_k > \sigma_n^2$
   - $\mathbf{\Lambda}_n = \sigma_n^2 \mathbf{I}_{M-K}$

2. **MUSIC Pseudospectrum**:
   $$P_{\text{MU}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{U}_n \mathbf{U}_n^H \mathbf{a}(\theta)}$$

**Why MUSIC achieves super-resolution**:

The steering vectors $\{\mathbf{a}(\theta_1), \ldots, \mathbf{a}(\theta_K)\}$ span the same subspace as $\mathbf{U}_s$. Therefore they are orthogonal to $\mathbf{U}_n$:

$$\mathbf{a}^H(\theta_k) \mathbf{U}_n = \mathbf{0}^T \quad \text{for } k = 1, \ldots, K$$

At true DOAs, the denominator $\mathbf{a}^H(\theta) \mathbf{U}_n \mathbf{U}_n^H \mathbf{a}(\theta) \to 0$, so $P_{\text{MU}}(\theta) \to \infty$ (in practice, sharp peaks). This **subspace orthogonality** decouples resolution from the beamwidth — limited only by the number of snapshots and SNR.

**Resolution threshold**: MUSIC can resolve sources at arbitrarily close angles given sufficient SNR and snapshots. The threshold SNR for resolution scales as $1/M^3$ for large arrays.

**Limitations**:
- Requires $K < M$ (more elements than sources)
- Fails for **coherent** signals (multipath) without spatial smoothing
- Sensitive to array calibration errors
- Computational cost: $O(M^2 N + M^3)$

### 16.4.4 ESPRIT (Estimation of Signal Parameters via Rotational Invariance Techniques)

**Key idea**: Exploit the **translational invariance** of two identical subarrays. No search over $\theta$ needed.

For a ULA with subarrays spaced by $\Delta$, the steering vectors satisfy:

$$\mathbf{a}_2(\theta_k) = \mathbf{a}_1(\theta_k) \, e^{-j\frac{2\pi}{\lambda} \Delta \sin\theta_k}$$

The signal subspace eigenvectors also satisfy a shift-invariance equation. DOAs are extracted from the eigenvalues of:

$$\mathbf{\Phi} = \mathbf{U}_{s1}^\dagger \mathbf{U}_{s2}$$

where $\mathbf{U}_{s1}$, $\mathbf{U}_{s2}$ are the signal subspaces of the two subarrays, and $(\cdot)^\dagger$ denotes pseudoinverse. Then:

$$\theta_k = \arcsin\left(\frac{\lambda}{2\pi \Delta} \arg(\phi_k)\right)$$

**Advantages**:
- No grid search — computationally efficient
- No need to know array manifold precisely (only shift invariance needed)
- Real-time capable

### DOA Algorithm Comparison

| Algorithm | Resolution | Complexity | Grid Search | Coherent Sources | Calibration |
|-----------|-----------|------------|-------------|------------------|-------------|
| Bartlett | Poor | $O(M^2 N)$ | Yes | Robust | Low |
| Capon (MVDR) | Medium | $O(M^2 N + M^3)$ | Yes | Robust | Medium |
| MUSIC | High | $O(M^2 N + M^3)$ | Yes | ✗ (needs smoothing) | High |
| ESPRIT | High | $O(M^2 N + M^3)$ | **No** | ✗ (needs smoothing) | Medium |

---

## §16.5 Adaptive Beamforming

### 16.5.1 Optimal Beamforming

**Goal**: Find weight vector $\mathbf{w}$ that minimizes output power while satisfying constraints on desired signal.

**General optimization**:

$$\min_{\mathbf{w}} \mathbf{w}^H \mathbf{R}_{xx} \mathbf{w} \quad \text{s.t.} \quad \mathbf{C}^H \mathbf{w} = \mathbf{f}$$

where $\mathbf{C}$ is the $M \times L$ constraint matrix and $\mathbf{f}$ is the $L \times 1$ response vector.

### LCMV (Linearly Constrained Minimum Variance) Beamformer

For a single desired signal at $\theta_0$ (unit gain constraint):

$$\min_{\mathbf{w}} \mathbf{w}^H \mathbf{R}_{xx} \mathbf{w} \quad \text{s.t.} \quad \mathbf{a}^H(\theta_0) \mathbf{w} = 1$$

**Solution**:

$$\mathbf{w}_{\text{LCMV}} = \frac{\mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}{\mathbf{a}^H(\theta_0) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}$$

This is the **MVDR beamformer**. Key properties:
- Unit gain in desired direction
- Minimum total output power → automatically places nulls at interference directions
- Output SINR = $(\text{SNR}_{\text{in}})(M)$ in interference-free case (array gain = $M$)

### 16.5.2 Adaptive Algorithms

#### LMS (Least Mean Squares)

**Iterative update** (minimizes MSE between $y(n)$ and reference $d(n)$):

$$\mathbf{w}(n+1) = \mathbf{w}(n) + \mu \, e^*(n) \, \mathbf{x}(n)$$

where:
- $e(n) = d(n) - y(n) = d(n) - \mathbf{w}^H(n) \mathbf{x}(n)$ = error signal
- $\mu$ = step size (convergence parameter)

**Convergence condition**: $0 < \mu < 1/\lambda_{\text{max}}$ where $\lambda_{\text{max}}$ is the largest eigenvalue of $\mathbf{R}_{xx}$.

**Convergence speed**: Proportional to the eigenvalue spread $\lambda_{\text{max}}/\lambda_{\text{min}}$ of $\mathbf{R}_{xx}$. Wide spread → slow convergence.

**Steady-state excess MSE**: $J_{\text{ex}} \approx \mu \, J_{\text{min}} \, \text{tr}(\mathbf{R}_{xx})$, where $J_{\text{min}}$ is the Wiener MSE.

**Complexity**: $O(M)$ per iteration — very low.

#### RLS (Recursive Least Squares)

**Exponentially weighted least squares**:

$$\mathbf{w}(n) = \min_{\mathbf{w}} \sum_{i=1}^{n} \beta^{n-i} |e(i)|^2$$

where $\beta < 1$ is the forgetting factor.

**Update**:
$$\mathbf{k}(n) = \frac{\beta^{-1} \mathbf{P}(n-1) \mathbf{x}(n)}{1 + \beta^{-1} \mathbf{x}^H(n) \mathbf{P}(n-1) \mathbf{x}(n)}$$
$$\mathbf{w}(n) = \mathbf{w}(n-1) + \mathbf{k}(n) e^*(n)$$
$$\mathbf{P}(n) = \beta^{-1} \mathbf{P}(n-1) - \beta^{-1} \mathbf{k}(n) \mathbf{x}^H(n) \mathbf{P}(n-1)$$

**Convergence**: Much faster than LMS (independent of eigenvalue spread).
**Complexity**: $O(M^2)$ per iteration.

#### CMA (Constant Modulus Algorithm)

For **blind equalization** — no training sequence needed. Exploits constant envelope property of signals like FM, PSK, QAM.

**Cost function**:
$$J(n) = \mathbb{E}\left[ (|y(n)|^p - \gamma_p)^2 \right]$$

where $\gamma_p$ is the constant modulus (for PSK, $\gamma_2 = 1$).

**Stochastic gradient update** ($p=2$):
$$\mathbf{w}(n+1) = \mathbf{w}(n) + \mu \, y^*(n) \, (1 - |y(n)|^2) \, \mathbf{x}(n)$$

### Algorithm Comparison

| Algorithm | Complexity | Convergence Speed | Training Needed | Tracking | Robustness |
|-----------|-----------|-------------------|-----------------|----------|------------|
| **LCMV** (batch) | $O(M^3)$ | Instant (batch) | No (uses constraints) | Static env | High |
| **LMS** | $O(M)$ | Slow (depends on $\mu$, eig. spread) | Yes (reference) | Good | Medium |
| **NLMS** | $O(M)$ | Faster than LMS | Yes (reference) | Good | High |
| **RLS** | $O(M^2)$ | Fast ($\approx 2M$ iter.) | Yes (reference) | Best | Medium |
| **CMA** | $O(M)$ | Moderate | **No** (blind) | Good | Moderate |

---

## §16.6 Performance Metrics

### SINR (Signal-to-Interference-plus-Noise Ratio)

$$\text{SINR} = \frac{\mathbf{w}^H \mathbf{R}_{ss} \mathbf{w}}{\mathbf{w}^H \mathbf{R}_{in} \mathbf{w}} = \frac{\sigma_s^2 |\mathbf{w}^H \mathbf{a}(\theta_0)|^2}{\mathbf{w}^H \mathbf{R}_{in} \mathbf{w}}$$

where $\mathbf{R}_{in} = \sum_{k=2}^{K} \sigma_k^2 \mathbf{a}(\theta_k) \mathbf{a}^H(\theta_k) + \sigma_n^2 \mathbf{I}$.

**SINR improvement** (array gain) = $\text{SINR}_{\text{out}} / \text{SINR}_{\text{in}} \leq M$.

### Beam Pattern and Null Depth

- **Mainlobe width** ≈ $\frac{0.886 \lambda}{M d \cos\theta_0}$ (radians, 3 dB beamwidth)
- **Sidelobe level** ≈ $-13.5$ dB for uniform weighting
- **Null depth**: Typically 30–60 dB for adaptive arrays

### Convergence Metrics

- **Misadjustment**: $\mathcal{M} = \frac{J_{\text{ex}}}{J_{\text{min}}}$ (steady-state excess MSE / Wiener MSE)
- For LMS: $\mathcal{M} \approx \mu \, \text{tr}(\mathbf{R}_{xx})$
- **Time constant**: $\tau_{\text{LMS}} \approx \frac{1}{\mu \lambda_k}$ for mode $k$

---

## §16.7 Practical Considerations

### Source Coherence

When signals are coherent (e.g., multipath), $\mathbf{R}_{ss}$ becomes singular and $\text{rank}(\mathbf{R}_{xx}) < K$. Subspace methods (MUSIC, ESPRIT) fail.

**Solution**: Spatial smoothing — partition the array into $L$ overlapping subarrays, average their covariance matrices. This restores rank to $\mathbf{R}_{ss}$.

### Finite Sample Effects

With limited snapshots $N$, $\hat{\mathbf{R}}_{xx}$ is a poor estimate of $\mathbf{R}_{xx}$. The signal and noise subspaces become mixed. Rule of thumb: $N > 10M$ for reliable DOA estimation.

### Array Calibration

MUSIC and ESPRIT assume perfectly known array manifold. Gain/phase errors between channels cause:
- Biased DOA estimates
- Reduced null depth
- False peaks in pseudospectrum

**Mitigation**: Auto-calibration (e.g., using known sources), mutual coupling compensation.

---

## Summary

Smart antennas bridge antenna theory and signal processing:

1. **Architecture**: Switched beam (low cost) vs. adaptive array (high performance)
2. **DOA estimation**: Progresses from Bartlett → Capon → MUSIC → ESPRIT, each improving resolution
3. **Beamforming**: From conventional (fixed weights) to optimal (MVDR/LCMV) to adaptive (LMS/RLS/CMA)
4. **Subspace separation** is the core insight behind super-resolution: signal and noise subspaces are orthogonal, and the sharpness of MUSIC peaks comes from this orthogonality, not from the array beamwidth
5. **Adaptation** enables tracking in dynamic environments, at the cost of convergence time and computational complexity

---

*References: Balanis, Antenna Theory 4th Ed., Chapter 16. H.L. Van Trees, Optimum Array Processing. Stoica & Moses, Spectral Analysis of Signals.*

# Chapter 16: Smart Antennas — Balanis Antenna Theory (4th Ed.) / 第16章：智能天线

> **中英双语版**

> **Tutorial chapter**: Covers smart antenna system architectures, DOA estimation, and adaptive beamforming algorithms.
> **教程章节**：涵盖智能天线系统架构、DOA估计和自适应波束赋形算法。

---

## §16.1 Introduction / 引言

Smart antennas combine an array of antenna elements with real-time signal processing to / 智能天线将天线阵元阵列与实时信号处理相结合，以实现：

- **Enhance desired signals / 增强期望信号** via adaptive beamforming / 通过自适应波束赋形
- **Suppress interference / 抑制干扰** by steering nulls toward interferers / 将零点指向干扰源
- **Track mobile users / 跟踪移动用户** in dynamic environments / 在动态环境中
- **Increase system capacity / 提高系统容量** (SDMA — Space Division Multiple Access / 空分多址)

Key applications / 关键应用：cellular base stations (4G/5G), radar, sonar, GPS anti-jam, cognitive radio / 蜂窝基站、雷达、声纳、GPS抗干扰、认知无线电。

---

## §16.2 Smart Antenna System Architecture / 智能天线系统架构

### Switched Beam vs. Adaptive Array / 切换波束 vs 自适应阵列

| Feature / 特性 | Switched Beam / 切换波束 | Adaptive Array / 自适应阵列 |
|---------|---------------|----------------|
| Beam pattern / 波束方向图 | Predefined, fixed beams / 预定义固定波束 | Dynamically computed / 动态计算 |
| Interference rejection / 干扰抑制 | Limited (off-boresight) / 有限（偏离轴向） | ✓ **Nulls placed on interferers / 对干扰源置零** |
| Computational cost / 计算成本 | Low / 低 | High / 高 |
| Tracking / 跟踪 | Beam-switching only / 仅波束切换 | Continuous adaptation / 连续自适应 |
| Channel capacity / 信道容量 | Limited / 有限 | Maximum (optimal SINR) / 最大（最优信干噪比） |

**Digital Beamforming Architecture / 数字波束赋形架构**：

The baseband processor forms the array output as a linear combination of element signals / 基带处理器将阵列输出表示为阵元信号的线性组合：

$$y(t) = \mathbf{w}^H \mathbf{x}(t)$$

where $\mathbf{w} = [w_0, w_1, \ldots, w_{M-1}]^T$ is the complex weight vector / 其中 $\mathbf{w} = [w_0, w_1, \ldots, w_{M-1}]^T$ 为复权矢量。

---

## §16.3 Array Fundamentals / 阵列基础

### Uniform Linear Array (ULA) / 均匀直线阵

For an $M$-element ULA with inter-element spacing $d = \lambda/2$ / 对于 $M$ 元ULA，阵元间距 $d = \lambda/2$：

**Array response (steering) vector / 阵列响应（导向）矢量**：

$$\mathbf{a}(\theta) = \left[1,\; e^{-j\frac{2\pi}{\lambda} d \sin\theta},\; e^{-j\frac{2\pi}{\lambda} 2d \sin\theta},\; \ldots,\; e^{-j\frac{2\pi}{\lambda} (M-1)d \sin\theta}\right]^T$$

With $d = \lambda/2$ / 当 $d = \lambda/2$：

$$\mathbf{a}(\theta) = \left[1,\; e^{-j\pi \sin\theta},\; e^{-j2\pi \sin\theta},\; \ldots,\; e^{-j(M-1)\pi \sin\theta}\right]^T$$

**Signal Model / 信号模型**：

The received signal vector at time $t$ / $t$ 时刻的接收信号矢量：

$$\mathbf{x}(t) = \sum_{k=1}^{K} \mathbf{a}(\theta_k) s_k(t) + \mathbf{n}(t)$$

where / 其中：
- $K$ = number of sources (signals + interferers) / 源数目（信号+干扰）
- $s_k(t)$ = complex baseband signal from source $k$ / 来自源 $k$ 的复基带信号
- $\mathbf{n}(t)$ = AWGN noise vector / 加性高斯白噪声矢量, $\mathcal{CN}(0, \sigma_n^2 \mathbf{I})$

---

## §16.4 Direction-of-Arrival (DOA) Estimation / 波达方向估计

### 16.4.1 Conventional Beamforming (Bartlett) / 常规波束赋形

Spatial spectrum / 空间谱：

$$P_{\text{Bartlett}}(\theta) = \frac{\mathbf{a}^H(\theta) \mathbf{R}_{xx} \mathbf{a}(\theta)}{M^2}$$

Peaks occur at source DOAs. Resolution is limited by the Rayleigh limit / 峰值出现在源DOA处。分辨率受瑞利极限限制。

### 16.4.2 Capon's Method (MVDR) / 卡彭法

Minimum Variance Distortionless Response / 最小方差无失真响应：

$$P_{\text{Capon}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta)}$$

**Idea / 思想**：A spatial filter that passes direction $\theta$ with unit gain while minimizing total output power / 对方向 $\theta$ 以单位增益通过，同时最小化总输出功率的空间滤波器。

### 16.4.3 MUSIC / 多信号分类法

**Key insight / 关键洞见**：The signal vectors lie in a $K$-dimensional subspace, noise in the orthogonal $(M-K)$-dimensional subspace / 信号矢量位于 $K$ 维子空间，噪声位于正交的 $(M-K)$ 维子空间。

**MUSIC Pseudospectrum / MUSIC伪谱**：

$$P_{\text{MU}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{U}_n \mathbf{U}_n^H \mathbf{a}(\theta)}$$

**Why MUSIC achieves super-resolution / 为什么MUSIC实现超分辨**：

The steering vectors $\{\mathbf{a}(\theta_1), \ldots, \mathbf{a}(\theta_K)\}$ span the same subspace as $\mathbf{U}_s$. They are orthogonal to $\mathbf{U}_n$ / 导向矢量与信号子空间 $\mathbf{U}_s$ 张成同一空间，与噪声子空间 $\mathbf{U}_n$ 正交：

$$\mathbf{a}^H(\theta_k) \mathbf{U}_n = \mathbf{0}^T \quad \text{for } k = 1, \ldots, K$$

### 16.4.4 ESPRIT / 旋转不变技术

**Key idea / 关键思想**：Exploit the **translational invariance** of two identical subarrays. No search over $\theta$ needed / 利用两个相同子阵的**平移不变性**，无需搜索 $\theta$。

**DOAs extracted from / DOA从下式提取**：

$$\theta_k = \arcsin\left(\frac{\lambda}{2\pi \Delta} \arg(\phi_k)\right)$$

### DOA Algorithm Comparison / DOA算法对比

| Algorithm / 算法 | Resolution / 分辨率 | Complexity / 复杂度 | Grid Search / 网格搜索 | Coherent Sources / 相干源 | Calibration / 校准 |
|-----------|-----------|------------|-------------|------------------|-------------|
| Bartlett | Poor / 差 | $O(M^2 N)$ | Yes | Robust | Low / 低 |
| Capon (MVDR) | Medium / 中 | $O(M^2 N + M^3)$ | Yes | Robust | Medium / 中 |
| MUSIC | High / 高 | $O(M^2 N + M^3)$ | Yes | ✗ (needs smoothing / 需平滑) | High / 高 |
| ESPRIT | High / 高 | $O(M^2 N + M^3)$ | **No / 否** | ✗ (needs smoothing / 需平滑) | Medium / 中 |

---

## §16.5 Adaptive Beamforming / 自适应波束赋形

### 16.5.1 Optimal Beamforming / 最优波束赋形

**Goal / 目标**：Find weight vector $\mathbf{w}$ that minimizes output power while satisfying constraints / 求满足约束的同时最小化输出功率的权矢量 $\mathbf{w}$。

### LCMV (Linearly Constrained Minimum Variance) / 线性约束最小方差

For a single desired signal at $\theta_0$ (unit gain constraint) / 对于 $\theta_0$ 处的单个期望信号（单位增益约束）：

$$\mathbf{w}_{\text{LCMV}} = \frac{\mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}{\mathbf{a}^H(\theta_0) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}$$

### 16.5.2 Adaptive Algorithms / 自适应算法

**LMS (Least Mean Squares) / 最小均方**：

$$\mathbf{w}(n+1) = \mathbf{w}(n) + \mu \, e^*(n) \, \mathbf{x}(n)$$

Convergence condition / 收敛条件：$0 < \mu < 1/\lambda_{\text{max}}$

Complexity / 复杂度：$O(M)$ per iteration / 每次迭代

**RLS (Recursive Least Squares) / 递归最小二乘**：

Complexity / 复杂度：$O(M^2)$ per iteration / 每次迭代

Convergence / 收敛速度：Much faster than LMS, independent of eigenvalue spread / 远快于LMS，与特征值散布无关

**CMA (Constant Modulus Algorithm) / 恒模算法**：

For **blind equalization** — no training sequence needed / 用于**盲均衡**——无需训练序列。

Cost function / 代价函数：

$$J(n) = \mathbb{E}\left[ (|y(n)|^p - \gamma_p)^2 \right]$$

### Algorithm Comparison / 算法对比

| Algorithm / 算法 | Complexity / 复杂度 | Convergence Speed / 收敛速度 | Training Needed / 需训练 | Tracking / 跟踪 | Robustness / 鲁棒性 |
|-----------|-----------|-------------------|-----------------|----------|------------|
| **LCMV** (batch) | $O(M^3)$ | Instant (batch) / 瞬时（批量） | No (uses constraints / 使用约束) | Static env / 静态环境 | High / 高 |
| **LMS** | $O(M)$ | Slow / 慢 | Yes / 是 | Good / 好 | Medium / 中 |
| **RLS** | $O(M^2)$ | Fast / 快 | Yes / 是 | Best / 最好 | Medium / 中 |
| **CMA** | $O(M)$ | Moderate / 中等 | **No** (blind / 盲) | Good / 好 | Moderate / 中 |

---

## §16.6 Performance Metrics / 性能指标

### SINR (Signal-to-Interference-plus-Noise Ratio) / 信干噪比

$$\text{SINR} = \frac{\mathbf{w}^H \mathbf{R}_{ss} \mathbf{w}}{\mathbf{w}^H \mathbf{R}_{in} \mathbf{w}}$$

**SINR improvement / SINR提升** (array gain / 阵列增益) = $\text{SINR}_{\text{out}} / \text{SINR}_{\text{in}} \leq M$.

### Beam Pattern and Null Depth / 波束方向图与零点深度

- **Mainlobe width / 主瓣宽度** ≈ $\frac{0.886 \lambda}{M d \cos\theta_0}$ (radians, 3 dB beamwidth / 弧度，3 dB波束宽度)
- **Sidelobe level / 旁瓣电平** ≈ $-13.5$ dB for uniform weighting / 均匀加权
- **Null depth / 零点深度**：Typically 30–60 dB for adaptive arrays / 自适应阵列典型值

---

## §16.7 Practical Considerations / 实际考量

### Source Coherence / 源相干性

When signals are coherent (e.g., multipath), $\mathbf{R}_{ss}$ becomes singular. Subspace methods fail / 当信号相干时（如多径），子空间方法失效。

**Solution / 解决方案**：Spatial smoothing / 空间平滑 — partition array into overlapping subarrays / 将阵列分割为重叠子阵。

### Finite Sample Effects / 有限样本效应

Rule of thumb / 经验法则：$N > 10M$ for reliable DOA estimation / 为获得可靠的DOA估计。

### Array Calibration / 阵列校准

Gain/phase errors cause / 增益/相位误差会导致：
- Biased DOA estimates / DOA估计偏差
- Reduced null depth / 零点深度降低
- False peaks in pseudospectrum / 伪谱中的虚假峰值

---

## Summary / 总结

Smart antennas bridge antenna theory and signal processing / 智能天线连接了天线理论与信号处理：

1. **Architecture / 架构**：Switched beam (low cost / 低成本) vs. adaptive array (high performance / 高性能)
2. **DOA estimation / DOA估计**：Progresses from Bartlett → Capon → MUSIC → ESPRIT / 从Bartlett到ESPRIT逐步提高分辨率
3. **Beamforming / 波束赋形**：From conventional to optimal (MVDR/LCMV) to adaptive (LMS/RLS/CMA) / 从常规到最优到自适应
4. **Subspace separation / 子空间分离** is the core insight behind super-resolution / 是超分辨的核心洞见
5. **Adaptation / 自适应** enables tracking in dynamic environments / 实现在动态环境中的跟踪

---

*References / 参考文献：Balanis, Antenna Theory 4th Ed., Chapter 16. H.L. Van Trees, Optimum Array Processing. Stoica & Moses, Spectral Analysis of Signals.*

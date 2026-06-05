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

The baseband processor forms the array output as a linear combination / 基带处理器将阵列输出表示为线性组合：

$$y(t) = \mathbf{w}^H \mathbf{x}(t)$$

where $\mathbf{w} = [w_0, w_1, \ldots, w_{M-1}]^T$ is the complex weight vector / 其中 $\mathbf{w} = [w_0, w_1, \ldots, w_{M-1}]^T$ 为复权矢量。

---

## §16.3 Array Fundamentals / 阵列基础

### Uniform Linear Array (ULA) / 均匀直线阵

For an $M$-element ULA with inter-element spacing $d = \lambda/2$ / 对于 $M$ 元ULA，阵元间距 $d = \lambda/2$：

**Array response (steering) vector / 阵列响应（导向）矢量**：

$$\mathbf{a}(\theta) = \left[1,\; e^{-j\frac{2\pi}{\lambda} d \sin\theta},\; e^{-j\frac{2\pi}{\lambda} 2d \sin\theta},\; \ldots,\; e^{-j\frac{2\pi}{\lambda} (M-1)d \sin\theta}\right]^T$$

**Signal Model / 信号模型**：

$$\mathbf{x}(t) = \sum_{k=1}^{K} \mathbf{a}(\theta_k) s_k(t) + \mathbf{n}(t)$$

---

## §16.4 Direction-of-Arrival (DOA) Estimation / 波达方向估计

### 16.4.1 Conventional Beamforming (Bartlett) / 常规波束赋形

$$P_{\text{Bartlett}}(\theta) = \frac{\mathbf{a}^H(\theta) \mathbf{R}_{xx} \mathbf{a}(\theta)}{M^2}$$

### 16.4.2 Capon's Method (MVDR) / 卡彭法

$$P_{\text{Capon}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta)}$$

### 16.4.3 MUSIC / 多信号分类法

**Key insight / 关键洞见**：Signal and noise subspaces are orthogonal / 信号子空间与噪声子空间正交。

$$P_{\text{MU}}(\theta) = \frac{1}{\mathbf{a}^H(\theta) \mathbf{U}_n \mathbf{U}_n^H \mathbf{a}(\theta)}$$

### 16.4.4 ESPRIT / 旋转不变技术

**Key idea / 关键思想**：Exploit translational invariance of two subarrays. No grid search / 利用两个子阵的平移不变性，无需网格搜索。

$$\theta_k = \arcsin\left(\frac{\lambda}{2\pi \Delta} \arg(\phi_k)\right)$$

### DOA Algorithm Comparison / DOA算法对比

| Algorithm / 算法 | Resolution / 分辨率 | Complexity / 复杂度 | Grid Search / 网格搜索 | Coherent Sources / 相干源 |
|-----------|-----------|------------|-------------|------------------|
| Bartlett | Poor / 差 | $O(M^2 N)$ | Yes | Robust |
| Capon (MVDR) | Medium / 中 | $O(M^2 N + M^3)$ | Yes | Robust |
| MUSIC | High / 高 | $O(M^2 N + M^3)$ | Yes | ✗ |
| ESPRIT | High / 高 | $O(M^2 N + M^3)$ | **No / 否** | ✗ |

---

## §16.5 Adaptive Beamforming / 自适应波束赋形

### 16.5.1 Optimal Beamforming / 最优波束赋形

$$\mathbf{w}_{\text{LCMV}} = \frac{\mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}{\mathbf{a}^H(\theta_0) \mathbf{R}_{xx}^{-1} \mathbf{a}(\theta_0)}$$

### 16.5.2 Adaptive Algorithms / 自适应算法

**LMS**: $\mathbf{w}(n+1) = \mathbf{w}(n) + \mu \, e^*(n) \, \mathbf{x}(n)$ — $O(M)$ per iter / 每次迭代

**RLS**: — $O(M^2)$ per iter / 每次迭代, faster convergence / 更快收敛

**CMA**: $\mathbf{w}(n+1) = \mathbf{w}(n) + \mu \, y^*(n) \, (1 - |y(n)|^2) \, \mathbf{x}(n)$ — blind / 盲

---

## §16.6 Performance Metrics / 性能指标

### SINR (Signal-to-Interference-plus-Noise Ratio) / 信干噪比

$$\text{SINR} = \frac{\mathbf{w}^H \mathbf{R}_{ss} \mathbf{w}}{\mathbf{w}^H \mathbf{R}_{in} \mathbf{w}}$$

---

## Summary / 总结

Smart antennas bridge antenna theory and signal processing / 智能天线连接了天线理论与信号处理。

1. **Architecture / 架构**：Switched beam (low cost / 低成本) vs. adaptive array (high performance / 高性能)
2. **DOA estimation / DOA估计**：Bartlett → Capon → MUSIC → ESPRIT
3. **Beamforming / 波束赋形**：Conventional → Optimal → Adaptive
4. **Subspace separation / 子空间分离** is the core insight behind super-resolution / 是超分辨的核心洞见

---

*References / 参考文献：Balanis, Antenna Theory 4th Ed., Chapter 16. H.L. Van Trees, Optimum Array Processing.*

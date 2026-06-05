# Pozar Chapter 5 — Impedance Matching and Tuning
> **中英双语版**

> Comprehensive notes on Pozar *Microwave Engineering*, 4th Edition, pp. 250–320.
> Covers lumped L-section matching, single/double-stub tuning, quarter-wave transformers, and tapered-line matching.

---

## 5.1 L-Section Matching Networks | L 型匹配网络

Given a load impedance $Z_L = R_L + jX_L$ and a real source/line impedance $Z_0$, design a 2-element LC network that transforms $Z_L$ to $Z_0$ at a single design frequency $f_0$.
> 给定负载阻抗 $Z_L$ 和实值源/传输线阻抗 $Z_0$，设计一个双元件 LC 网络，在单一设计频率 $f_0$ 处将 $Z_L$ 变换为 $Z_0$。

**8 possible topologies** arise from series/shunt ordering and which element is capacitor/inductor.
> **8 种可能的拓扑**来源于串联/并联顺序以及哪个元件是电容/电感。

### 5.1.1 Analytic Solution | 解析解

For $Z_L = R_L + jX_L$ with $R_L > Z_0$:
> 对于 $R_L > Z_0$ 的情况：

$$Q = \sqrt{\frac{R_L}{Z_0} - 1}, \quad X = \frac{R_L}{Q}, \quad B = \frac{Q}{R_L}$$

> 其中 $X$ 为串联电抗，$B$ 为并联电纳。

For $R_L < Z_0$:
> 对于 $R_L < Z_0$ 的情况：

$$Q = \sqrt{\frac{Z_0}{R_L} - 1}, \quad X = Q Z_0, \quad B = \frac{Q}{Z_0}$$

### 5.1.2 Smith Chart Solution | 史密斯圆图解法

1. Plot the normalized load $z_L = Z_L/Z_0$ on the Smith chart
2. Move along constant $R$ or $G$ circle to intersect the $r=1$ or $g=1$ circle
3. Read the required reactance/susceptance from the chart
4. Implement using lumped elements (capacitor or inductor)

> 史密斯圆图解法：在 Smith 圆图上标记归一化负载 $z_L$，沿等 $R$ 或等 $G$ 圆移动至与 $r=1$ 或 $g=1$ 圆相交，读取需要的电抗/电纳值。

---

## 5.2 Single-Stub Tuning | 单枝节调谐

A shunt (or series) open/short-circuited stub is placed at a distance $d$ from the load.
> 在距离负载 $d$ 处放置一个并联（或串联）的开路/短路枝节。

**Procedure / 步骤：**
1. Find distance $d$ from the load where $Y = Y_0 + jB$ (real part = $Y_0$)
   > 找到负载到 $Y = Y_0 + jB$ 点的距离 $d$
2. Choose stub length $\ell$ to provide susceptance $-jB$
   > 选择枝节长度 $\ell$ 以提供电纳 $-jB$

**Stub input susceptance / 枝节输入电纳：**
- Short-circuited: $B_{\text{sc}} = -jY_0 \cot(\beta\ell)$
- Open-circuited: $B_{\text{oc}} = jY_0 \tan(\beta\ell)$

Multiple solutions exist; typically choose the shorter line lengths.
> 存在多组解；通常选择较短的传输线长度。

---

## 5.3 Double-Stub Tuning | 双枝节调谐

Two stubs are placed at fixed distances (typically $\lambda/8$ or $\lambda/4$ apart).
> 两个枝节以固定间距（通常为 $\lambda/8$ 或 $\lambda/4$）放置。

**Advantage / 优势：** Adjustable without changing stub position (only stub lengths).
> 可在不改变枝节位置的情况下调节（仅改变枝节长度）。

**Limitation / 局限性：** Some load impedances cannot be matched (forbidden region on Smith chart).
> 某些负载阻抗无法匹配（Smith 圆图上的禁区）。

The forbidden region can be reduced by choosing a larger stub spacing.
> 可通过选择更大的枝节间距来缩小禁区。

---

## 5.4 Quarter-Wave Transformer | 四分之一波长变换器

For matching a real load $R_L$ to a real line impedance $Z_0$:
> 用于匹配实值负载 $R_L$ 到实值线阻抗 $Z_0$：

$$Z_1 = \sqrt{Z_0 R_L}$$

where $Z_1$ is the characteristic impedance of a $\lambda/4$ line section inserted between $Z_0$ and $R_L$.
> 其中 $Z_1$ 是插入在 $Z_0$ 和 $R_L$ 之间的 $\lambda/4$ 线段的特征阻抗。

**Bandwidth / 带宽：** The bandwidth increases as the impedance ratio $R_L/Z_0$ approaches 1.
> 带宽随阻抗比 $R_L/Z_0$ 趋近于 1 而增加。

**Multi-section / 多节：** Using cascaded $\lambda/4$ sections (binomial, Chebyshev) improves bandwidth.
> 使用多节级联 $\lambda/4$ 线段可提高带宽。

---

## 5.5 Tapered Lines | 渐变线

A smooth transition from $Z_0$ to $R_L$ using a gradually tapered transmission line.
> 使用逐渐渐变的传输线从 $Z_0$ 平滑过渡到 $R_L$。

**Types / 类型：**
- **Exponential taper**: $Z(z) = Z_0 e^{az}$, $0<z<L$
- **Triangular taper**: Optimized for given $L$
- **Klopfenstein taper**: Optimal (provides the shortest taper for a given reflection coefficient)
  > Klopfenstein 渐变线：给定反射系数下的最优渐变线（最短长度）

**Reflection coefficient for taper / 渐变线的反射系数：**

$$\Gamma(f) \approx \frac{1}{2} \int_0^L \frac{d}{dz}[\ln Z(z)] e^{-j2\beta z} dz$$

> 设计目标是使 $\Gamma(f)$ 在所需频带内足够小。

---

## 5.6 Summary / 总结

| Method | Bandwidth | Complexity | Best For |
|--------|-----------|------------|----------|
| L-section | Narrow | Low | Single-frequency lumped matching |
| Single stub | Moderate | Low | Coaxial/waveguide matching |
| Double stub | Moderate | Medium | Adjustable tuning |
| $\lambda/4$ transformer | Narrow | Low | Real impedances |
| Multi-section | Broad | Medium | Broadband matching |
| Tapered line | Very broad | High | Ultra-wideband applications |

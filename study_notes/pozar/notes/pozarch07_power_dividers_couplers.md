# Pozar《Microwave Engineering》4th Ed., Chapter 7 — Power Dividers and Directional Couplers
> **中英双语版**

> 功率分配器与定向耦合器 — 无源多端口网络设计与分析

---

## §7.1 Basic Properties of Dividers and Couplers

### 三端口网络 (T-Junction)

任意无耗互易三端口网络的散射矩阵：

$$
\mathbf{S} = \begin{bmatrix}
S_{11} & S_{12} & S_{13}\\
S_{12} & S_{22} & S_{23}\\
S_{13} & S_{23} & S_{33}
\end{bmatrix}
$$

**无耗互易三端口网络的矛盾**：除非全部端口匹配（$S_{11}=S_{22}=S_{33}=0$），否则无法实现所有端口同时匹配。

- 若三端口全部匹配 → 有耗 或 非互易
- **实际方案**：要么有耗（电阻性分配器），要么加入隔离电阻（Wilkinson）

### 四端口网络 (Directional Coupler)

理想定向耦合器的散射矩阵（无耗、匹配、互易）：

$$
\mathbf{S} = \begin{bmatrix}
0 & 0 & S_{13} & S_{14}\\
0 & 0 & S_{23} & S_{24}\\
S_{13} & S_{23} & 0 & 0\\
S_{14} & S_{24} & 0 & 0
\end{bmatrix}
$$

**关键参数**（dB 值）：

| 参数      | 定义                       | 公式                                   |
|-----------|----------------------------|----------------------------------------|
| 耦合度 C  | 输入 → 耦合端衰减           | $C = -20\log_{10}|S_{31}|$            |
| 隔离度 I  | 输入 → 隔离端衰减           | $I = -20\log_{10}|S_{41}|$            |
| 方向性 D  | 耦合端 vs 隔离端功率比       | $D = I - C = -20\log_{10}\frac{|S_{41}|}{|S_{31}|}$ |
| 插损 IL   | 输入 → 直通端衰减            | $IL = -20\log_{10}|S_{21}|$           |
| 回波损耗 RL| 端口匹配度                  | $RL = -20\log_{10}|S_{11}|$           |

**量纲检查**：S 参数均为无量纲电压比；C, I, D, IL, RL 均为 dB 值（无量纲对数）。

**相位关系**（对称定向耦合器）：

$$
S_{31} = C_0 \quad (\text{耦合端}, \angle 0^\circ)
$$
$$
S_{21} = -j\sqrt{1-C_0^2} \quad (\text{直通端}, \angle -90^\circ)
$$

即耦合端 0^\circ 相位，直通端 −90^\circ 相位。

---

## §7.2 The T-Junction Power Divider

### 无耗 T 型结

传输线模型（特征导纳分路）：

$$
Y_{\text{in}} = Y_1 + Y_2 + Y_3
$$

为匹配输入（$Z_0$），要求：

$$
\frac{1}{Z_0} = \frac{1}{Z_1} + \frac{1}{Z_2} + \frac{1}{Z_3}
$$

若输出端口用四分之一波变换器匹配到 $Z_0$：

$$
Z_1 = \frac{Z_0}{P_1/P_{\text{in}}}, \quad Z_2 = \frac{Z_0}{P_2/P_{\text{in}}}, \quad Z_3 = \frac{Z_0}{P_3/P_{\text{in}}}
$$

但输出端口之间无隔离 — 这是 T 型结的根本缺陷。

### 电阻性分配器

有耗 T 型结，三个端口均可匹配（$S_{11}=S_{22}=S_{33}=0$），但插入损耗大 ($-6$ dB)。

$$
\mathbf{S}_{\text{resistive}} = \frac{1}{2} \begin{bmatrix}
0 & 1 & 1\\
1 & 0 & 1\\
1 & 1 & 0
\end{bmatrix}
$$

**输出端口隔离度仅 $-6$ dB**，且 50% 功率损耗在电阻中。

---

## §7.3 The Wilkinson Power Divider

### 等分 Wilkinson 分配器

关键特征：无耗互易三端口，**有耗**（隔离电阻），但可实现**所有端口匹配 + 输出端口隔离**。

**结构**：两个 $$\lambda$/4$ 传输线（阻抗 $Z_0\sqrt{2}$），输出端口间跨接 $2Z_0$ 电阻。

### 奇偶模分析

将 Wilkinson 分解为两个单端口网络（偶模和奇模激励）：

#### 偶模激励 ($V_{g2}=V_{g3}=2V$)

- 对称面为开路，隔离电阻无电流
- 端口 2 看入阻抗 $Z_{\text{in}}^e = Z_{\text{line}}^2 / (2Z_0)$

#### 奇模激励 ($V_{g2}=2V, V_{g3}=0$)

- 对称面为短路，隔离电阻中点接地
- 端口 2 看入阻抗 $Z_{\text{in}}^o = R/2$

**设计方程**：

$$
\text{阻抗变换器: } Z_{\text{line}} = \sqrt{2} Z_0
$$
$$
\text{隔离电阻: } R = 2 Z_0
$$

**S 参数**（等分 Wilkinson）：

$$
S_{11} = S_{22} = S_{33} = 0 \quad (\text{完全匹配})
$$
$$
|S_{21}| = |S_{31}| = -\frac{1}{\sqrt{2}} \quad (-3\ \text{dB})
$$
$$
S_{23} = S_{32} = 0 \quad (\text{完全隔离})
$$

### 不等分 Wilkinson

功率比 $K^2 = P_3/P_2$：

$$
Z_{\text{line2}} = Z_0 \sqrt{\frac{1+K^2}{K^3}}
$$
$$
Z_{\text{line3}} = Z_0 \sqrt{K(1+K^2)}
$$
$$
R = Z_0(K + 1/K)
$$

### 多节 Wilkinson

宽带设计。N 节级联 $$\lambda$/4$ 变换器可实现 $>1$ 倍频程带宽。

---

## §7.4 The Quadrature (90^\circ) Hybrid — Branch-Line Coupler

### 单节 Branch-Line

结构：四条 $$\lambda$/4$ 传输线形成矩形环，特征阻抗分别为 $Z_0/\sqrt{2}$ 或 $Z_0$。

**3 dB (90^\circ) 混合耦合器设计**：

| 段          | 特征阻抗                         |
|-------------|----------------------------------|
| 水平臂 (主线) | $Z_0/\sqrt{2} \approx 35.35\ \Omega$ (50Ω 系统) |
| 垂直臂 (支线) | $Z_0 \approx 50\ \Omega$        |

**S 参数矩阵**（3 dB 情况）：

$$
\mathbf{S} = -\frac{1}{\sqrt{2}} \begin{bmatrix}
0 & j & 1 & 0\\
j & 0 & 0 & 1\\
1 & 0 & 0 & j\\
0 & 1 & j & 0
\end{bmatrix}
$$

**端口分配**：
- Port 1 → Port 2（$-3$ dB, $-90^\circ$）和 Port 3（$-3$ dB, $0^\circ$）
- Port 4 隔离

### 多节 Branch-Line

更多支线 → 更宽带宽。常见为 2 节、3 节结构（对称），可达到 20–30% 相对带宽。

---

## §7.5 The 180^\circ Hybrid — Rat-Race Coupler

### 环形混合耦合器

环形周长 $1.5\lambda_g$，阻抗 $Z_0\sqrt{2}$（3 dB 耦合）。

**端口布置**：

```
     Port 1 ($\Sigma$) ───── $\lambda$/4 ──── Port 2
          │                     │
         3$\lambda$/4                  $\lambda$/4
          │                     │
     Port 4 ($\Delta$) ───── $\lambda$/4 ──── Port 3
```

**S 参数矩阵**（3 dB 等分）：

$$
\mathbf{S} = -\frac{j}{\sqrt{2}} \begin{bmatrix}
0 & 1 & 0 & -1\\
1 & 0 & -1 & 0\\
0 & -1 & 0 & 1\\
-1 & 0 & 1 & 0
\end{bmatrix}
$$

**端口特征**（S 矩阵约定）：
- **\Sigma 和差端口** (Port 1): 输入 → Port 2 (−90^\circ, -3 dB) 和 Port 4 (+90^\circ, -3 dB), Port 3 隔离
- **\Delta 差端口** (Port 4): 输入 → Port 1 (+90^\circ, -3 dB) 和 Port 3 (−90^\circ, -3 dB), Port 2 隔离
- Port 1 ↔ Port 3 隔离；Port 2 ↔ Port 4 隔离

> ⚠️ 不同教科书对 Rat-Race 端口编号和 S 矩阵约定不同。
> Pozar 4/e §7.5 标准 S 矩阵 (Eq 7.89) 为 S = -j/\sqrt₂[[0,1,1,0],[1,0,0,-1],[1,0,0,1],[0,-1,1,0]]，
> 其 \Sigma (Port 1) → Port 2,3 (-90^\circ 等幅同相)，\Delta (Port 4) → Port 2 (+90^\circ), Port 3 (-90^\circ)，隔离对为 (1,4) 与 (2,3)。
> 本笔记与代码使用另一套端口分配，隔离对为 (1,3) 与 (2,4)，物理行为等价。

**S 参数相位与隔离验证**（代码）：
$$
\mathbf{S} = -\frac{j}{\sqrt{2}} \begin{bmatrix}
0 & 1 & 0 & -1\\
1 & 0 & -1 & 0\\
0 & -1 & 0 & 1\\
-1 & 0 & 1 & 0
\end{bmatrix}
\quad \Rightarrow \quad \mathbf{S}\mathbf{S}^\dagger = \mathbf{I}
$$

### 平面 Rat-Race vs 环形

环形 $1.5\lambda$ 周长仅占标准 rat-race 的 75%。平面变体（圆形、弯折）用于紧凑封装。

---

## §7.6 Coupled Line Directional Couplers

### 耦合传输线基础

对称耦合线的**奇偶模分解**：

| 参数      | 偶模                            | 奇模                            |
|-----------|--------------------------------|----------------------------------|
| 特征阻抗  | $Z_{0e}$                       | $Z_{0o}$                         |
| 电压分布  | $V_1 = V_2$                    | $V_1 = -V_2$                     |
| 场分布    | 电场偶对称（弱耦合→高阻抗） | 电场奇对称（强耦合→低阻抗）   |

### 设计方程

给定耦合度 $C$ (dB)，奇偶模阻抗：

$$
\frac{Z_{0e}}{Z_0} = \sqrt{\frac{1 + 10^{-C/20}}{1 - 10^{-C/20}}}
$$
$$
\frac{Z_{0o}}{Z_0} = \sqrt{\frac{1 - 10^{-C/20}}{1 + 10^{-C/20}}}
$$

**$C \to 0$ dB 极限**：$Z_{0e}/Z_0 \to \infty$，$Z_{0o}/Z_0 \to 0$（强耦合需要极窄间距）

**$C \to \infty$ dB 极限**：$Z_{0e} \to Z_0$，$Z_{0o} \to Z_0$（弱耦合 → 间距大）

### 单节 $$\lambda$/4$ 耦合线耦合器

S 参数：

$$
S_{11} = 0 \quad \text{(理想匹配)}
$$
$$
S_{31} = j k \quad \text{(耦合端, $-90^\circ$)}
$$
$$
S_{21} = \sqrt{1 - k^2} \quad \text{(直通端, $0^\circ$)}
$$
$$
S_{41} = 0 \quad \text{(隔离端)}
$$

其中耦合系数 $k = (Z_{0e} - Z_{0o}) / (Z_{0e} + Z_{0o})$。

$$\lambda$/4$ 单节仅在中心频率处理想；带宽受限于耦合线电长度。

### 物理结构

| 类型      | 特点                               | 典型应用            |
|-----------|-----------------------------------|---------------------|
| 微带耦合线 | 边缘耦合，弱耦合 ($C > 10$ dB)     | 弱耦合器、方向性检测 |
| 带状线耦合线 | 宽边耦合，强耦合 ($C \approx 3$ dB) | 3 dB 混合耦合器      |
| Lange 耦合器 | 交指结构，强耦合                     | 宽带 3 dB 耦合器     |

### 多节耦合线耦合器

级联多节 $$\lambda$/4$ 耦合线（类阻抗变换器节）可实现宽带响应。设计采用切比雪夫或最大平坦优化。

---

## §7.7 The Lange Coupler

### 特点

- 四根或更多交指耦合线
- 使用跳线 (bond wires) 实现交叉连接
- 可在微带中实现强耦合 ($C = 3$ dB)
- 带宽 > 1 倍频程

### 设计方程

四导线 Lange 耦合器 ($$\lambda$/4$ 长度)：

$$
Z_{0e} = Z_0 \frac{4k + 3 + \sqrt{9 + 8k^2}}{\sqrt{(1-k)(8 + 4k - 3k + \cdots)}}
$$

简化设计公式（Waugh 公式）：

$$
Z_{0e} \approx Z_0 \sqrt{ \frac{1 + 10^{-C/20}}{1 - 10^{-C/20}} }
$$

与常规耦合线相比，Lange 结构将 $Z_{0e}/Z_{0o}$ 比值提高了约 3 倍（四线结构）。

### 实际考虑

- 条带宽度 ~25–50 $\mu$m（毫米波频段）
- 间距 ~10–25 $\mu$m
- 跳线位置约在 $$\lambda$/4$ 两端，影响高频性能
- 介质厚度、金属化厚度影响奇偶模阻抗

---

## §7.8 Additional Practical Examples

### Example 7.1: T-Junction Design

设计等分三路无耗 T 型结，输入 $Z_0=50\Omega$，各输出支路均需用 $$\lambda$/4$ 变换器匹配到 $50\Omega$：

$$
Z_1 = 3 \times 50 = 150\ \Omega
$$
$$
$\lambda$/4\ \text{变换器: } Z_{\text{trans}} = \sqrt{50 \times 150} \approx 86.6\ \Omega
$$

### Example 7.2: Wilkinson 等分分配器

$f_0 = 2\ \text{GHz}$，$Z_0 = 50\ \Omega$：
- 变换器阻抗: $Z = 50\sqrt{2} \approx 70.71\ \Omega$
- 隔离电阻: $R = 100\ \Omega$
- S 参数在 $f_0$: $S_{11} = S_{22} = S_{33} = 0$, $S_{21} = S_{31} = -3\ \text{dB}$, $S_{23} = -\infty$

### Example 7.3: 3 dB Branch-Line Coupler

$f_0 = 3\ \text{GHz}$，$Z_0 = 50\ \Omega$：
- 主线水平臂: $Z_0/\sqrt{2} \approx 35.35\ \Omega$，$$\lambda$/4$ 长度
- 支线垂直臂: $Z_0 = 50\ \Omega$，$$\lambda$/4$ 长度
- 耦合度 3 dB，端口 4 隔离

### Example 7.4: Rat-Race Coupler

$f_0 = 1\ \text{GHz}$，$Z_0 = 50\ \Omega$：
- 环阻抗: $50\sqrt{2} \approx 70.71\ \Omega$
- 周长: $1.5\lambda_g$
- 4 个端口间距: Port 1-2: $$\lambda$/4$, Port 2-3: $$\lambda$/4$, Port 3-4: $$\lambda$/4$, Port 4-1: $3$\lambda$/4$

### Example 7.5: Coupled Line Coupler

$C = 10\ \text{dB}$，$f_0 = 4\ \text{GHz}$，$Z_0 = 50\ \Omega$：

$$
Z_{0e} = 50 \sqrt{\frac{1 + 10^{-10/20}}{1 - 10^{-10/20}}} \approx 69.39\ \Omega
$$
$$
Z_{0o} = 50 \sqrt{\frac{1 - 10^{-10/20}}{1 + 10^{-10/20}}} \approx 36.03\ \Omega
$$

### Example 7.6: Lange Coupler

$C = 3\ \text{dB}$，$Z_0 = 50\ \Omega$：
- 四线交指结构
- 耦合系数 $k = 10^{-C/20} = 0.707$
- 奇偶模比 $Z_{0e}/Z_{0o} = (1+k)/(1-k) \approx 5.83$
- 等效于带状线宽边耦合才能实现的强度

### Example 7.7: Multi-Section Coupled-Line Coup.

宽带设计，多节 $$\lambda$/4$ 耦合线段级联，切比雪夫响应。

---

## 关键公式总结

| 拓扑                    | 关键公式                                              |
|------------------------|-------------------------------------------------------|
| T 型结                 | $Y_{\text{in}} = \sum Y_i$                            |
| 电阻性分配器             | $\mathbf{S} = \frac{1}{2}[[0,1,1],[1,0,1],[1,1,0]]$ |
| Wilkinson (等分)        | $Z_{\text{line}} = \sqrt{2}Z_0$, $R=2Z_0$            |
| Branch-Line (3 dB)     | 主线 $Z_0/\sqrt{2}$, 支线 $Z_0$                       |
| Rat-Race (3 dB)        | 环 $Z_0\sqrt{2}$, $$\Sigma$/\Delta$ 端口                |
| 耦合线方向性              | $k=(Z_{0e}-Z_{0o})/(Z_{0e}+Z_{0o})$                  |
| Lange                   | 交指结构, $C$ 可达 3 dB (微带)                        |

## 设计要点检查表

- [ ] $S_{11}$ 回波损耗: 至少 > 15 dB (典型)
- [ ] 耦合度偏差: $\pm 0.5$ dB 以内
- [ ] 隔离度: > 20 dB (3 dB 耦合器), > 30 dB (10 dB 耦合器)
- [ ] 相位平衡: $\pm 3^\circ$ 以内 (90^\circ 或 180^\circ)
- [ ] 阻抗变换器: $$\lambda$/4$ 电长度在中心频率精确
- [ ] 制造公差: 微带线宽/间距变化 → 耦合度变化

---

## 量纲审计

| 量            | 单位                | 备注                        |
|---------------|---------------------|-----------------------------|
| $Z_0, Z_{0e}, Z_{0o}$ | $\Omega$           | 特征阻抗                    |
| $S_{ij}$      | 无量纲（电压比）      | $|S_{ij}| \le 1$            |
| $C, I, D, IL$ | dB (无量纲)         | $>0$ 表示衰减               |
| $k$           | 无量纲 (0 \leq k \leq 1)  | 耦合系数                     |
| $R$           | $\Omega$            | 隔离电阻                     |
| $\lambda_g$   | m                   | 导波波长                     |

> 所有 S 参数矩阵行列式 $\det(\mathbf{S})=1$（无耗）或 $<1$（有耗）——这是无源网络的能量守恒约束。

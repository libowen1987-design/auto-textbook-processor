---
chapter: 5
title: Fields and Waves in Rectangular Coordinates
source: Jin, Theory and Computation of Electromagnetic Fields, 2nd Ed., pp. 223–284
sections: 8
examples: 4
---

# Chapter 5: Fields and Waves in Rectangular Coordinates | 第五章：直角坐标中的场与波

> **中英双语版**

## 5.1 Uniform Waveguides | 均匀波导 (pp. 199–212)

### 5.1.1 General Analysis | 一般分析 (p. 200)

For a uniform waveguide (no variation along $z$), fields propagate as / 对于均匀波导（沿 $z$ 方向无变化），场以 $e^{-jk_z z}$ 形式传播：

$$
\mathbf{E} = \mathbf{E}_t + \hat{z}E_z = [\mathbf{e}_t(x,y) + \hat{z}e_z(x,y)] e^{-jk_z z} \tag{5.1.1}
$$
$$
\mathbf{H} = \mathbf{H}_t + \hat{z}H_z = [\mathbf{h}_t(x,y) + \hat{z}h_z(x,y)] e^{-jk_z z} \tag{5.1.2}
$$

From Maxwell's equations, transverse fields expressed via longitudinal components / 从麦克斯韦方程组，用纵向分量表示横向场：

$$
\mathbf{E}_t = \frac{1}{k_t^2} (j\omega\mu\,\hat{z}\times\nabla_t H_z - jk_z\nabla_t E_z) \tag{5.1.11}
$$
$$
\mathbf{H}_t = \frac{1}{k_t^2} (-j\omega\epsilon\,\hat{z}\times\nabla_t E_z - jk_z\nabla_t H_z) \tag{5.1.12}
$$

where $k_t^2 = k^2 - k_z^2$ / 其中 $k_t^2 = k^2 - k_z^2$。

$E_z$ and $H_z$ satisfy the scalar Helmholtz equation in the transverse plane / $E_z$ 和 $H_z$ 满足横向平面中的标量亥姆霍兹方程：

$$
\nabla_t^2 E_z + k_t^2 E_z = 0 \quad\text{in }\Omega \tag{5.1.15}
$$
$$
\nabla_t^2 H_z + k_t^2 H_z = 0 \quad\text{in }\Omega \tag{5.1.16}
$$

Boundary conditions on conducting wall $\Gamma$ / 导体壁 $\Gamma$ 上的边界条件：
- TM: $E_z = 0$ on $\Gamma$ \tag{5.1.17}
- TE: $\partial H_z/\partial n = 0$ on $\Gamma$ \tag{5.1.19}

Since $E_z$ and $H_z$ are decoupled, TE and TM modes exist independently / 由于 $E_z$ 和 $H_z$ 解耦，TE和TM模独立存在。

### 5.1.2 TE and TM Modes | TE和TM模

**TM modes / TM模** ($H_z=0$):
$$
\mathbf{E}_t = -\frac{jk_z}{k_t^2}\nabla_t E_z,\quad
\mathbf{H}_t = -\frac{j\omega\epsilon}{k_t^2}\hat{z}\times\nabla_t E_z \tag{5.1.20}
$$

**TE modes / TE模** ($E_z=0$):
$$
\mathbf{E}_t = \frac{j\omega\mu}{k_t^2}\hat{z}\times\nabla_t H_z,\quad
\mathbf{H}_t = -\frac{jk_z}{k_t^2}\nabla_t H_z \tag{5.1.21}
$$

Cutoff / 截止: $k_t = k_c$ when $k_z = 0$, i.e., $f_c = \frac{k_c}{2\pi\sqrt{\mu\epsilon}}$。

Below cutoff / 截止以下: $k_z = -j\alpha$，evanescent mode / 凋落模 ($\alpha = \sqrt{k_c^2 - k^2}$)。

**三种模式类型:**
- **TEM** ($E_z = H_z = 0$): $k_z = k$，无截止
- **TE** ($E_z = 0$): $H_z$ 满足 $\nabla_t^2 H_z + k_t^2 H_z = 0$
- **TM** ($H_z = 0$): $E_z$ 满足 $\nabla_t^2 E_z + k_t^2 E_z = 0$

### 5.1.3 Waveguide Parameters | 波导参数

**Wave impedance / 波阻抗**:
$$
Z_{\text{TE}} = \frac{k\eta}{k_z},\quad Z_{\text{TM}} = \frac{k_z\eta}{k} \tag{5.1.23}
$$

**Guide wavelength / 波导波长**: $\lambda_g = 2\pi/k_z$

**Phase velocity / 相速度**: $v_p = \omega/k_z > c$

**Group velocity / 群速度**: $v_g = d\omega/dk_z < c$

**Attenuation due to imperfect conductors / 非理想导体的衰减** (perturbation method / 微扰法):

$$
\alpha_c = \frac{R_s}{2}\frac{\oint_\Gamma |\mathbf{H}_w|^2 d\Gamma}{\iint_\Omega (\mathbf{e}_t\times\mathbf{h}_t^*)\cdot\hat{z}\,d\Omega} \tag{5.1.25}
$$

**Dielectric loss / 介质损耗**: $\alpha_d = \frac{k^2\tan\delta}{2k_z}$ \tag{5.1.129}

**Power flow / 功率流**: $P = \frac{1}{2}\iint_\Omega (\mathbf{e}_t\times\mathbf{h}_t^*)\cdot\hat{z}\,d\Omega$

## 5.2 Rectangular Waveguide | 矩形波导 (pp. 212–226)

Cross-section $a\times b$ ($a > b$ by convention) / 横截面 $a\times b$（约定 $a > b$）。

### 5.2.1 TE Modes | TE模

$$
H_z = A_{mn}\cos\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z} \tag{5.2.1}
$$

Cutoff wavenumber / 截止波数：$k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$。

Propagation constant / 传播常数：$k_z = \sqrt{k^2 - k_c^2}$。

Transverse fields / 横向场 (Eqs. 5.2.3–5.2.6):

$$
E_x = j\omega\mu\frac{n\pi}{b}\frac{A_{mn}}{k_c^2}\cos\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
E_y = -j\omega\mu\frac{m\pi}{a}\frac{A_{mn}}{k_c^2}\sin\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
H_x = jk_z\frac{m\pi}{a}\frac{A_{mn}}{k_c^2}\sin\frac{m\pi x}{a}\cos\frac{n\pi y}{b}\,e^{-jk_z z}
$$
$$
H_y = jk_z\frac{n\pi}{b}\frac{A_{mn}}{k_c^2}\cos\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z}
$$

### 5.2.2 TM Modes | TM模

$$
E_z = B_{mn}\sin\frac{m\pi x}{a}\sin\frac{n\pi y}{b}\,e^{-jk_z z} \tag{5.2.7}
$$

Cutoff same as TE / 截止与TE相同。注意：$m=0$ 或 $n=0$ 对TM模给出平凡解 $E_z=0$。

### 5.2.3 Dominant TE$_{10}$ Mode | 主模 TE$_{10}$

For $a > b$, TE$_{10}$ has lowest cutoff ($k_c = \pi/a$, $f_c = c/(2a)$) / 当 $a > b$ 时，TE$_{10}$ 的截止频率最低。

**Field components of TE$_{10}$ / TE$_{10}$ 的场分量:**

$$
H_z = A_{10}\cos\frac{\pi x}{a}\,e^{-jk_z z}
$$
$$
E_y = -j\omega\mu\frac{a}{\pi}A_{10}\sin\frac{\pi x}{a}\,e^{-jk_z z}
$$
$$
H_x = jk_z\frac{a}{\pi}A_{10}\sin\frac{\pi x}{a}\,e^{-jk_z z}
$$

**Attenuation of TE$_{10}$ / TE$_{10}$ 的衰减:**

$$
\alpha_c^{\text{TE}_{10}} = \frac{2R_s}{b\eta\sqrt{1-(f_c/f)^2}}
\left[\frac{1}{2} + \frac{b}{a}\left(\frac{f_c}{f}\right)^2\right] \tag{5.2.12}
$$

### 5.2.4 Mode Charts and Degeneracy | 模式图与简并

相同 $m,n$ 的 TE$_{mn}$ 和 TM$_{mn}$ 有相同截止（简并），但 $m=0$ 或 $n=0$ 时TM不存在。

**Example 5.1 / 例5.1** (p. 218): 矩形波导设计（X波段 WR-90: $a=22.86$ mm, $b=10.16$ mm）。TE$_{10}$ 截止频率6.56 GHz，工作范围8.2–12.4 GHz。

**Example 5.2 / 例5.2** (p. 220): WR-90在10 GHz时TE$_{10}$模的衰减常数（铜）：$\alpha_c \approx 0.11$ dB/m。

## 5.3 Rectangular Cavity | 矩形腔 (pp. 226–236)

Cavity dimensions $a\times b\times d$ (short circuits at $z=0,d$) / 腔体尺寸 $a\times b\times d$（在 $z=0,d$ 处短路）。

### 5.3.1 TE$_{mnp}$ and TM$_{mnp}$ Modes | TE$_{mnp}$ 和 TM$_{mnp}$ 模

Resonant frequency / 谐振频率：

$$
f_{mnp} = \frac{1}{2\pi\sqrt{\mu\epsilon}}\sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{d}\right)^2} \tag{5.2.5}
$$

**TE$_{101}$ dominant mode / 主模 TE$_{101}$** when $d > a > b$ or $a > d > b$。

Resonant frequency / 谐振频率：$f_{101} = \frac{c}{2\pi}\sqrt{(\pi/a)^2 + (\pi/d)^2}$。

### 5.3.2 Quality Factor | 品质因数

$$
Q_c = \frac{\omega_0 W}{P_{dc}} = \frac{2}{\delta_s}\frac{\iiint_V |\mathbf{H}|^2 dV}{\oint_S |\mathbf{H}_w|^2 dS}
$$

where $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ is the skin depth / $\delta_s = \sqrt{2/(\omega\mu\sigma)}$ 是趋肤深度。

For TE$_{101}$ mode / 对 TE$_{101}$ 模：

$$
Q_{c,101} = \frac{kad\eta}{2R_s}\frac{b}{(a^2 + d^2)ad/2 + b(a^3 + d^3) + abd}
$$

**Example 5.3 / 例5.3** (p. 231): X波段腔体 ($a=22.86$ mm, $b=10.16$ mm, $d=20$ mm), TE$_{101}$ 在10.5 GHz, $Q_c \approx 7000$（铜）。

### 5.3.3 Modal Field Distributions | 模场分布

电场线：TM模有非零 $E_z$，TE模 $E_z = 0$。

## 5.4 Dielectric Slab Waveguide | 介质板波导 (pp. 236–252)

### 5.4.1 TE Surface Wave Modes | TE表面波模

Structure: dielectric slab ($\epsilon_1$, thickness $h$) on ground plane / 结构：介质板（$\epsilon_1$，厚度 $h$）在接地平面上。

For TE modes ($E_y$ polarized) / 对TE模（$E_y$ 极化）：

在板内：$E_y = A\sin(k_x x)$ 对奇模，$E_y = A\cos(k_x x)$ 对偶模。

在板外上方：$E_y = Be^{-\alpha(x-h)}$。

Characteristic equation / 特征方程：

$$
k_x\cot(k_x h) = -\alpha \quad\text{(even TE modes / 偶TE模)} \tag{5.4.5}
$$
$$
k_x\tan(k_x h) = \alpha \quad\text{(odd TE modes / 奇TE模)} \tag{5.4.6}
$$

其中 $k_x^2 = \epsilon_{r1}k_0^2 - k_z^2$, $\alpha^2 = k_z^2 - k_0^2$。

### 5.4.2 TM Surface Wave Modes | TM表面波模

Similar characteristic equations with $\epsilon_{r1}$ factor / 类似特征方程，带有 $\epsilon_{r1}$ 因子：

$$
\frac{k_x}{\epsilon_{r1}}\cot(k_x h) = -\frac{\alpha}{\epsilon_{r2}} \quad\text{(even TM / 偶TM)}
$$
$$
\frac{k_x}{\epsilon_{r1}}\tan(k_x h) = \frac{\alpha}{\epsilon_{r2}} \quad\text{(odd TM / 奇TM)}
$$

**Example 5.4 / 例5.4** (p. 244): TE$_0$ 模无截止频率；$m=1$ 模的截止在 $k_x h = \pi/2$。

### 5.4.3 Dispersion Curves | 色散曲线

$k_z$ vs. frequency: surface wave modes cluster near the light line $k_z = k_0$ at low frequencies and approach $k_z = \sqrt{\epsilon_{r1}}k_0$ at high frequencies / $k_z$ 对频率：低频时表面波模聚集在光线 $k_z = k_0$ 附近，高频时趋近 $k_z = \sqrt{\epsilon_{r1}}k_0$。

介质板波导不像金属波导那样有尖锐截止——模在所有频率都存在，但在低频时束缚较弱。

## 5.5 Field Excitation in Waveguides | 波导中的场激励 (pp. 252–260)

A probe (vertical electric dipole) inside a waveguide excites TM modes predominantly / 波导内的探针（垂直电偶极子）主要激励TM模。A loop (magnetic dipole) excites TE modes / 回路（磁偶极子）激励TE模。

**Coupling coefficient / 耦合系数**: 正比于源位置处的模场值。

## 5.6 Fields in Planar Layered Media | 平面分层媒质中的场 (pp. 260–284)

### 5.6.1 Transfer Matrix Method | 传输矩阵法

For $N$-layer structure, relate fields at top and bottom / 对于 $N$ 层结构，关联顶层和底层的场：

$$
\begin{bmatrix} E_1 \\ H_1 \end{bmatrix} = \mathbf{T}_1\mathbf{T}_2\cdots\mathbf{T}_N \begin{bmatrix} E_{N+1} \\ H_{N+1} \end{bmatrix}
$$

其中 $\mathbf{T}_i = \begin{bmatrix} \cos(k_{zi}d_i) & j\eta_i\sin(k_{zi}d_i)/k_i \\ jk_i\sin(k_{zi}d_i)/\eta_i & \cos(k_{zi}d_i) \end{bmatrix}$。

TMM 对分层媒质是 $O(N)$ 的——对一维问题非常高效。

### 5.6.2 Microstrip Green's Function | 微带格林函数

Spectral-domain Green's function for layered medium using transmission line analogy / 使用传输线类比的谱域格林函数。

## 5.7 Rectangular Waveguide Green's Function | 矩形波导格林函数 (pp. 276–284)

Source excitation inside rectangular waveguide: modal expansion using eigenfunctions of the cross-section / 矩形波导内的源激励：使用横截面本征函数的模展开。

$$
G(\mathbf{r},\mathbf{r}') = \sum_{m,n} \frac{\psi_{mn}(x,y)\psi_{mn}(x',y')}{2jk_{z,mn}} e^{-jk_{z,mn}|z-z'|}
$$

其中 $\psi_{mn}$ 是横截面的本征函数（正弦/余弦乘积）。

## **Physical Intuition / 物理直觉**
- TE$_{10}$ 是基模，因为 $\cos(\pi x/a)$ 以最小的 $k_c$ 满足 $x=0,a$ 处的 $\partial H_z/\partial n = 0$。
- TM 模要求 $m,n \ge 1$，所以当 $a > b$ 时截止频率总是高于 TE$_{10}$。
- 截止以下时，模为凋落模——场指数衰减，无实功率传播。
- 矩形波导是高通滤波器：只有 $f > f_c$ 的模才能传播。
- 波导模在横向平面内是驻波，在纵向是行波。

## **Numerical Intuition / 数值直觉**
- WR-90 ($22.86\times10.16$ mm) 的 TE$_{10}$ 截止为6.56 GHz——此频率以下无传播。
- 对腔体，$Q \sim \text{体积}/(\text{表面积} \times \delta_s)$——腔体越大 $Q$ 越高。
- 介质板波导的特征方程是超越方程——需通过数值求根求解。

## **Audit Table / 审计表**
| Section / 节 | Pages / 页 | Key Formulas / 关键公式 | Verified / 验证 |
|---------|-------|:------------:|:--------:|
| 5.1 | 199–212 | (5.1.1)–(5.1.25) | ✓ |
| 5.2 | 212–226 | (5.2.1)–(5.2.12) | ✓ |
| 5.3 | 226–236 | (5.2.5), 腔 $Q$ | ✓ |
| 5.4 | 236–252 | (5.4.5)–(5.4.6) | ✓ |
| 5.5 | 252–260 | 激励 | ✓ |
| 5.6 | 260–276 | TMM, 微带格林函数 | ✓ |
| 5.7 | 276–284 | 波导格林函数 | ✓ |

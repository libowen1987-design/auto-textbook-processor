# 廖承恩《微波技术基础》第3章

> 本笔记基于 OCR 文本清洗整理，100% 来源于原书内容。

## 第3章 规则金属波导

### 3.1 矩形波导

矩形波导截面尺寸 $a \times b$（$a > b$），传输 TE 或 TM 模，不能传输 TEM 模。

#### 波动方程（Helmholtz）

$$\nabla^2 E + k^2 E = 0, \quad k = \frac{2\pi}{\lambda} = \omega\sqrt{\mu\varepsilon}$$

矩形波导中 $(x,y)$ 方向的边界条件为Dirichlet（理想导体边界）。

#### TE 模（$E_z = 0$，$H_z \neq 0$）

$$H_z(x,y,z) = H_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}$$

截止波数：$k_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$

#### 截止波长

$$\lambda_c = \frac{2}{\sqrt{(m/a)^2 + (n/b)^2}}$$

主模 TE$_{10}$：$\lambda_c = 2a$，$f_c = c/(2a)$

#### 传播常数

$$\gamma = \alpha + j\beta = \sqrt{k_c^2 - k^2}$$

- $k > k_c$（$f > f_c$）：$\alpha = 0$，$\beta = \sqrt{k^2 - k_c^2}$，**传播**
- $k < k_c$（$f < f_c$）：$\alpha > 0$，$\beta = 0$，**截止**

#### 相速度和群速度

$$v_p = \frac{\omega}{\beta} = \frac{v}{\sqrt{1 - (\lambda/\lambda_c)^2}} > v$$

$$v_g = \frac{d\omega}{d\beta} = v\sqrt{1 - (\lambda/\lambda_c)^2} < v$$

$$v_p \cdot v_g = v^2$$

#### 波导波长

$$\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1 - (\lambda/\lambda_c)^2}}$$

#### 传输功率（TE$_{mn}$ 模）

$$P = \frac{1}{2} \int_0^a \int_0^b \mathrm{Re}(E_x H_y^* - E_y H_x^*) dx\,dy = \frac{a b}{4Z_{TE}} |H_0|^2 (1+\delta_{m0})(1+\delta_{n0})$$

其中 $Z_{TE} = \eta/\sqrt{1-(\lambda/\lambda_c)^2}$ 为 TE 模的波阻抗。

---

### 3.2 圆波导

圆形波导截面半径为 $a$，传输 TE 和 TM 模。用柱坐标系 $(r,\phi,z)$ 分析。

#### 模式方程

TE$_{mn}$：$J_m'(k_c r) = 0$（$k_c = \chi'_{mn}/a$，$\chi'_{mn}$ 为 $m$ 阶贝塞尔函数导数的第 $n$ 个根）

TM$_{mn}$：$J_m(k_c r) = 0$（$k_c = \chi_{mn}/a$，$\chi_{mn}$ 为 $m$ 阶贝塞尔函数的第 $n$ 个根）

#### 常用模式

- TE$_{11}$：主模，$\lambda_c = 1.706a$
- TM$_{01}$：对称模式，$\lambda_c = 2.613a$
- TE$_{01}$：低损耗模式（圆波导通信）

---

### 3.3 微带传输线

**微带线 (Microstrip Line)**：介质基片上印刷导体带的传输线，工作于准 TEM 模。

#### 特性参数计算

有效介电常数：

$$\varepsilon_e = \frac{1+\varepsilon_r}{2} \cdot \frac{1+\tanh(1.45h/w)}{1+1.45h/w}$$

特性阻抗（窄带，$w/h > 1$）：

$$Z_0 = \frac{60}{\sqrt{\varepsilon_e}} \ln\left(\frac{8h}{w} + \frac{w}{4h}\right)$$

宽导体带（$w/h > 2$）：

$$Z_0 = \frac{\pi}{2\sqrt{2\varepsilon_r}} \cdot \frac{h}{w}$$

#### 波长和相速度

$$\lambda = \frac{\lambda_0}{\sqrt{\varepsilon_e}}, \quad v_p = \frac{c}{\sqrt{\varepsilon_e}}$$

---


# 第四章 电磁波的传播

> 郭硕鸿《电动力学》笔记

---

## §4.1 平面电磁波

### 波动方程

真空中的麦克斯韦方程组：

$$
\nabla \cdot \mathbf{E} = 0, \quad \nabla \cdot \mathbf{B} = 0
$$
$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \quad 
\nabla \times \mathbf{B} = \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}
$$

对 $\nabla \times \mathbf{E}$ 两边取旋度，利用矢量恒等式 $\nabla \times (\nabla \times \mathbf{E}) = \nabla(\nabla\cdot\mathbf{E}) - \nabla^2\mathbf{E}$：

$$
\nabla^2\mathbf{E} - \mu_0\varepsilon_0 \frac{\partial^2\mathbf{E}}{\partial t^2} = 0
$$

同理可得 $\mathbf{B}$ 的波动方程。定义 $c = 1/\sqrt{\mu_0\varepsilon_0}$（光速）。

### 平面波解

单色平面波形式：

$$
\mathbf{E}(\mathbf{x}, t) = \mathbf{E}_0 e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
$$
$$
\mathbf{B}(\mathbf{x}, t) = \mathbf{B}_0 e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)}
$$

其中波矢 $\mathbf{k}$ 满足色散关系：$|\mathbf{k}| = \omega/c$。

### E 与 B 的关系

由 $\nabla \times \mathbf{E} = -\partial \mathbf{B}/\partial t$ 可得：

$$
\mathbf{k} \times \mathbf{E} = \omega \mathbf{B} \quad \Rightarrow \quad 
\mathbf{B} = \frac{1}{\omega} \mathbf{k} \times \mathbf{E}
$$

重要性质：
1. **横波性**：$\mathbf{k} \cdot \mathbf{E} = 0$, $\mathbf{k} \cdot \mathbf{B} = 0$（由 $\nabla \cdot \mathbf{E} = 0$ 和 $\nabla \cdot \mathbf{B} = 0$）
2. **相互垂直**：$\mathbf{E} \perp \mathbf{B} \perp \mathbf{k}$，三者构成右手系（$\mathbf{E} \times \mathbf{B}$ 沿 $\mathbf{k}$ 方向）
3. **振幅关系**：$|\mathbf{B}| = |\mathbf{k}||\mathbf{E}|/\omega = |\mathbf{E}|/c$

### 坡印廷矢量与能流密度

$$
\mathbf{S} = \frac{1}{\mu_0} \mathbf{E} \times \mathbf{B} = \frac{|\mathbf{E}_0|^2}{\mu_0 c} \cos^2(\mathbf{k}\cdot\mathbf{x} - \omega t) \,\hat{\mathbf{k}}
$$

时间平均能流密度：

$$
\langle\mathbf{S}\rangle = \frac{1}{2} \varepsilon_0 c |\mathbf{E}_0|^2 \,\hat{\mathbf{k}}
$$

### 电磁波的偏振

平面电磁波是横波，电场矢量在垂直于传播方向的平面内振动。

| 偏振类型 | 电场端点轨迹 | 描述 |
|---|---|---|
| **线偏振** | 直线 | 两个正交分量同相或反相 |
| **圆偏振** | 圆 | 两个正交分量振幅相等，相位差 $\pm\pi/2$ |
| **椭圆偏振** | 椭圆 | 一般情况 |

**数学描述**（波沿 $z$ 方向传播）：

$$
\mathbf{E}(z,t) = (E_x \hat{\mathbf{x}} + E_y \hat{\mathbf{y}}) e^{i(kz - \omega t)}
$$

令 $\delta = \delta_y - \delta_x$：

- $\delta = 0$ 或 $\pi$：线偏振
- $\delta = \pm\pi/2$ 且 $E_x = E_y$：圆偏振（$+$：左旋，$-$：右旋）
- 其他：椭圆偏振

---

## §4.2 电磁波在各向同性介质中的传播

### 介质的电磁性质

线性各向同性介质中：

$$
\mathbf{D} = \varepsilon \mathbf{E}, \quad \mathbf{B} = \mu \mathbf{H}
$$

$\varepsilon = \varepsilon_0\varepsilon_r$，$\mu = \mu_0\mu_r$。

### 波动方程与折射率

介质中的波动方程：

$$
\nabla^2\mathbf{E} - \mu\varepsilon \frac{\partial^2\mathbf{E}}{\partial t^2} = 0
$$

相速度 $v = 1/\sqrt{\mu\varepsilon} = c/n$，其中折射率 $n = \sqrt{\mu_r\varepsilon_r}$。

对非磁性介质（$\mu_r \approx 1$）：$n = \sqrt{\varepsilon_r}$。

### 能量关系

$$
\langle\mathbf{S}\rangle = \frac{1}{2} \sqrt{\frac{\varepsilon}{\mu}} |\mathbf{E}_0|^2 \,\hat{\mathbf{k}} = \frac{1}{2} n \varepsilon_0 c |\mathbf{E}_0|^2 \,\hat{\mathbf{k}}
$$

能量密度：

$$
\langle w\rangle = \frac{1}{2} \varepsilon |\mathbf{E}_0|^2 = \frac{1}{2} n^2 \varepsilon_0 |\mathbf{E}_0|^2
$$

### 色散

**正常色散**：$dn/d\omega > 0$（大部分透明介质）
**反常色散**：$dn/d\omega < 0$（发生在吸收带附近）

#### 洛伦兹色散模型

将电子视为束缚谐振子，运动方程：

$$
m\ddot{\mathbf{x}} + m\gamma\dot{\mathbf{x}} + m\omega_0^2\mathbf{x} = -e\mathbf{E}
$$

解得复介电常数：

$$
\varepsilon(\omega) = \varepsilon_0\left(1 + \frac{Ne^2}{\varepsilon_0 m}\frac{1}{\omega_0^2 - \omega^2 - i\gamma\omega}\right)
$$

#### 相速与群速

相速：$v_p = \omega/k = c/n$

群速（波包传播速度）：$v_g = \dfrac{d\omega}{dk}$

二者关系：

$$
v_g = \frac{d\omega}{dk} = \frac{v_p}{1 - \frac{\omega}{v_p}\frac{dv_p}{d\omega}} = v_p - \lambda\frac{dv_p}{d\lambda}
$$

- 正常色散区：$v_g < v_p$
- 反常色散区：$v_g > v_p$（但仍有因果性）

---

## §4.3 电磁波在导体中的传播

### 导体的麦克斯韦方程组

导体中有自由电荷和传导电流。欧姆定律 $\mathbf{J} = \sigma\mathbf{E}$。

考虑时谐场 $e^{-i\omega t}$：

$$
\nabla \times \mathbf{H} = \mathbf{J} - i\omega \mathbf{D} = \sigma\mathbf{E} - i\omega\varepsilon\mathbf{E} = -i\omega\left(\varepsilon + i\frac{\sigma}{\omega}\right)\mathbf{E}
$$

定义**复介电常数**：

$$
\tilde{\varepsilon} = \varepsilon + i\frac{\sigma}{\omega}
$$

### 波动方程与复波矢

导体中的波动方程形式上与介质中相同，但使用 $\tilde{\varepsilon}$。

设波沿 $z$ 方向传播，波矢为复数：$\tilde{k} = k + i\kappa$

$$
\mathbf{E}(z,t) = \mathbf{E}_0 e^{-\kappa z} e^{i(kz - \omega t)}
$$

### 趋肤效应

电场在导体中指数衰减。定义**趋肤深度**：

$$
\delta = \frac{1}{\kappa}
$$

对良导体（$\sigma \gg \omega\varepsilon$）：

$$
k \approx \kappa \approx \sqrt{\frac{\omega\mu\sigma}{2}}
$$
$$
\delta = \sqrt{\frac{2}{\omega\mu\sigma}}
$$

**关键结论**：
- 高频电磁波只能穿透导体表面很薄的一层
- 频率越高，趋肤深度越小（$\delta \propto 1/\sqrt{\omega}$）
- 导电性越好，趋肤深度越小（$\delta \propto 1/\sqrt{\sigma}$）

---

### 复折射率与波阻抗

复折射率：$\tilde{n} = n + i\kappa' = c\sqrt{\mu\tilde{\varepsilon}}$

良导体中的波阻抗：

$$
Z = \sqrt{\frac{\mu}{\tilde{\varepsilon}}} \approx (1+i)\sqrt{\frac{\omega\mu}{2\sigma}}
$$

---

## §4.4 电磁波在界面上的反射和折射

### 反射定律与折射定律

入射波、反射波、折射波在同一平面内（入射面）。

**反射定律**：$\theta_r = \theta_i$

**折射定律**（Snell 定律）：

$$
n_1 \sin\theta_i = n_2 \sin\theta_t
$$

### Fresnel 公式

将电场分解为两个偏振分量：
- **s 偏振**（TE波）：电场垂直于入射面
- **p 偏振**（TM波）：电场平行于入射面

#### s 偏振（电场垂直于入射面）

由边界条件 $E_{\parallel}$ 和 $H_{\parallel}$ 连续：

反射系数：
$$
r_s = \frac{E_{0r}}{E_{0i}} = \frac{n_1\cos\theta_i - n_2\cos\theta_t}{n_1\cos\theta_i + n_2\cos\theta_t}
$$

透射系数：
$$
t_s = \frac{E_{0t}}{E_{0i}} = \frac{2n_1\cos\theta_i}{n_1\cos\theta_i + n_2\cos\theta_t}
$$

#### p 偏振（电场平行于入射面）

反射系数：
$$
r_p = \frac{E_{0r}}{E_{0i}} = \frac{n_2\cos\theta_i - n_1\cos\theta_t}{n_2\cos\theta_i + n_1\cos\theta_t}
$$

透射系数：
$$
t_p = \frac{E_{0t}}{E_{0i}} = \frac{2n_1\cos\theta_i}{n_2\cos\theta_i + n_1\cos\theta_t}
$$

#### 反射率与透射率

$$
R = |r|^2, \quad T = 1 - R
$$

能量守恒：$R + T = 1$

### Brewster 角

当 $r_p = 0$ 时，反射光中无 p 偏振分量，反射光为完全 s 偏振。

$$
\tan\theta_B = \frac{n_2}{n_1}
$$

此时 $\theta_i + \theta_t = \pi/2$。

### 全反射

当光从光密介质进入光疏介质（$n_1 > n_2$），且 $\theta_i > \theta_c$ 时发生全反射。

**临界角**：
$$
\sin\theta_c = \frac{n_2}{n_1}
$$

全反射时，透射波沿界面传播，在第二介质中指数衰减：

$$
\mathbf{E}_t = \mathbf{E}_{0t} e^{-\kappa z} e^{i(k_x x - \omega t)}
$$

衰减系数 $\kappa = k_0\sqrt{n_1^2\sin^2\theta_i - n_2^2}$。

#### 全反射的相位变化

全反射时反射系数为复数，产生相位跃变：

s 偏振：
$$
\tan\frac{\delta_s}{2} = \frac{\sqrt{\sin^2\theta_i - (n_2/n_1)^2}}{\cos\theta_i}
$$

p 偏振：
$$
\tan\frac{\delta_p}{2} = \frac{\sqrt{\sin^2\theta_i - (n_2/n_1)^2}}{(n_2/n_1)^2\cos\theta_i}
$$

两者相位差可用于产生圆偏振光（Fresnel rhomb）。

---

## §4.5 波导

### 理想波导中的场方程

考虑无限长理想导体矩形波导，沿 $z$ 方向传播，横截面 $a \times b$（$a > b$）。

时谐场（$e^{i(k_z z - \omega t)}$），纵向场分量满足 Helmholtz 方程：

$$
(\nabla_t^2 + k_c^2) \begin{Bmatrix}E_z \\ H_z\end{Bmatrix} = 0
$$

其中 $k_c^2 = \omega^2\mu\varepsilon - k_z^2$ 为截止波数。

### TE 模（横电模）

$E_z = 0$，$H_z \neq 0$。边界条件：在波导壁上 $E_{\parallel} = 0$，即：

$$
\frac{\partial H_z}{\partial n}\bigg|_{\text{壁}} = 0
$$

解得：

$$
H_z = H_0 \cos\frac{m\pi x}{a} \cos\frac{n\pi y}{b} e^{i(k_z z - \omega t)}
$$

其中 $m, n = 0, 1, 2, \ldots$，但 $m = n = 0$ 无意义（平凡解）。

**截止波数**：
$$
k_c = \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}
$$

**截止频率**：
$$
\omega_c = \frac{k_c}{\sqrt{\mu\varepsilon}}, \quad f_c = \frac{\omega_c}{2\pi}
$$

### TM 模（横磁模）

$H_z = 0$，$E_z \neq 0$。边界条件 $E_z|_{\text{壁}} = 0$：

$$
E_z = E_0 \sin\frac{m\pi x}{a} \sin\frac{n\pi y}{b} e^{i(k_z z - \omega t)}
$$

其中 $m, n = 1, 2, 3, \ldots$（$m$ 或 $n$ 为零导致 $E_z = 0$，即 TEM 模）。

### TE10 模（主模）

$m = 1$, $n = 0$ 的 TE 模，是最低阶传播模式（设 $a > b$）。

截止波数：$k_c = \pi/a$

截止频率：$f_c = \frac{1}{2a\sqrt{\mu\varepsilon}}$

场分量：

$$
H_z = H_0 \cos\frac{\pi x}{a} e^{i(k_z z - \omega t)}
$$
$$
E_y = \frac{i\omega\mu a}{\pi} H_0 \sin\frac{\pi x}{a} e^{i(k_z z - \omega t)}
$$
$$
H_x = -\frac{ik_z a}{\pi} H_0 \sin\frac{\pi x}{a} e^{i(k_z z - \omega t)}
$$

传播常数 $k_z = \sqrt{k_0^2 - (\pi/a)^2}$。

### 传输特性

**波导波长**：
$$
\lambda_g = \frac{2\pi}{k_z} = \frac{\lambda}{\sqrt{1 - (f_c/f)^2}}
$$

**相速**：
$$
v_p = \frac{\omega}{k_z} = \frac{c}{\sqrt{1 - (f_c/f)^2}} > c
$$
（相速可以大于光速，不代表信号传输速度）

**群速**：
$$
v_g = \frac{d\omega}{dk_z} = c\sqrt{1 - (f_c/f)^2} < c
$$
（信号速度由群速决定）

### 阻抗与功率传输

TE10 模的波阻抗：

$$
Z_{\text{TE}} = \frac{k_0}{k_z}\eta = \frac{\eta}{\sqrt{1 - (f_c/f)^2}}
$$

其中 $\eta = \sqrt{\mu/\varepsilon}$ 为介质本征阻抗。

传输功率：

$$
P = \frac{ab}{4Z_{\text{TE}}} |E_0|^2
$$

---

## 关键公式速查

| 物理量 | 公式 |
|---|---|
| 波动方程 | $\nabla^2\mathbf{E} - \mu\varepsilon\partial^2\mathbf{E}/\partial t^2 = 0$ |
| 真空光速 | $c = 1/\sqrt{\mu_0\varepsilon_0}$ |
| 折射率 | $n = \sqrt{\mu_r\varepsilon_r}$ |
| 相速 | $v_p = \omega/k = c/n$ |
| 群速 | $v_g = d\omega/dk = v_p/(1 - (\omega/v_p)(dv_p/d\omega))$ |
| E-B 关系 | $\mathbf{B} = (\mathbf{k}\times\mathbf{E})/\omega$ |
| 能流密度 | $\langle\mathbf{S}\rangle = \frac12\sqrt{\varepsilon/\mu}\,|E_0|^2\;\hat{\mathbf{k}}$ |
| 趋肤深度 | $\delta = \sqrt{2/(\omega\mu\sigma)}$ |
| Snell 定律 | $n_1\sin\theta_i = n_2\sin\theta_t$ |
| Brewster 角 | $\tan\theta_B = n_2/n_1$ |
| 全反射临界角 | $\sin\theta_c = n_2/n_1$ |
| 波导截止波数 | $k_c = \sqrt{(m\pi/a)^2 + (n\pi/b)^2}$ |
| 波导波长 | $\lambda_g = \lambda/\sqrt{1 - (f_c/f)^2}$ |

# Ch8: Dielectric Body Scattering and RCS

## 元信息
- **教材**: Houle & Sullivan — Electromagnetic Simulation Using the FDTD Method with Python (IEEE Press 2019)
- **章节**: Ch8 Three-Dimensional Simulation with Dielectric Bodies
- **对应原文**: `/tmp/houle_ch8_raw.txt`

---

## 8.1 介质体散射问题

三维 FDTD 可用于计算雷达散射截面（RCS）。考虑一个介电球：

$$\epsilon_r = 30, \quad \sigma = 0.3\,\text{S/m}$$

**参数设置**：

```python
epsilon = [1.0, 30.0]  # 空气 + 介质球
sigma = [0.0, 0.3]     # S/m
radius = 10  # 网格单元
```

**更新系数**：

$$g_{ax} = \frac{1}{\epsilon_r + \frac{\sigma\Delta t}{\epsilon_0}}$$
$$g_{bx} = \frac{\sigma\Delta t}{\epsilon_0}$$

---

## 8.2 雷达散射截面（RCS）

RCS 定义为：

$$\sigma = \lim_{r\to\infty} 4\pi r^2 \frac{|E_s|^2}{|E_i|^2}$$

**双站 RCS**：入射波与散射波方向不同。

**Python 实现**：

```python
def calculate_rcs(ez_scattered, hx_scattered, hy_scattered,
                  frequency, dx, dy, dz, dt):
    """计算给定频率的雷达散射截面"""
    omega = 2 * np.pi * frequency
    # 远场变换：积分得到散射场
    # ...
    return rcs  # m²
```

---

## 8.3 数值直觉

> **介电常数跳变**：$\epsilon_r = 30$ 意味着光速在介质中降低为 $c/\sqrt{30} \approx 0.183c$。相应地，波长也缩短 $\sqrt{30}$ 倍，网格尺寸必须相对于介质中波长而非自由空间波长进行采样。

> **计算时间**：$40\times40\times40$ 网格，$\Delta t \approx 5.5\,$ps，每步约需 0.1ms（Numba 加速）。若仿真 10000 步，总时间约 1 秒。RCS 计算的远场积分需额外 10-30% 时间。

---

## 审计表格

| 公式 | 含义 | 验证 |
|:-----|:-----|:----:|
| $g_{ax}$ 更新系数 | $1/(\epsilon_r + \sigma\Delta t/\epsilon_0)$ | ✅ |
| RCS 公式 | $4\pi r^2 |E_s|^2/|E_i|^2$ | ✅ |
| 介质波长 | $\lambda_m = \lambda_0/\sqrt{\epsilon_r}$ | ✅ |
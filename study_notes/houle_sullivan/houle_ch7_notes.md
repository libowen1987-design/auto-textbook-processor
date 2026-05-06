# Ch7: Three-Dimensional FDTD and PML

## 元信息
- **教材**: Houle & Sullivan — Electromagnetic Simulation Using the FDTD Method with Python (IEEE Press 2019)
- **章节**: Ch7 Three-Dimensional Simulation & PML
- **对应原文**: `/tmp/houle_ch7_raw.txt`

---

## 7.1 三维 FDTD 仿真

三维 FDTD 将完整的 Maxwell 旋度方程离散化，使用 Yee 元胞在三个空间维度上交替采样电场和磁场分量：

$$E_x^{n+1}(i+1/2,j,k) = E_x^n(i+1/2,j,k) + \frac{\Delta t}{\epsilon\Delta x}[H_z^n(i+1/2,j+1/2,k) - H_z^n(i+1/2,j-1/2,k)]$$

**3D  CFL 稳定性条件**：

$$\Delta t \leqslant \frac{1}{c\sqrt{\frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2}}}$$

均匀立方体网格（$\Delta x = \Delta y = \Delta z = h$）：

$$\Delta t_{\max} = \frac{h}{c\sqrt{3}} \approx 0.577\frac{h}{c}$$

---

## 7.2 偶极子天线建模

简单偶极子天线由两根金属臂构成。FDTD 中的处理方式：

1. **金属设置**：$g_{az} = 0$（电导率无穷大），使金属内部 $E_z = 0$
2. **馈源设置**：在缝隙处设定 $E_z$ 值（高斯脉冲或正弦波）

$$E_z^{\text{source}}(t) = E_0 \cdot \exp\left[-\frac{(t-t_0)^2}{2\tau^2}\right]$$

**关键洞察**：馈源处的 $E_z$ 场等于由电流产生的真实场，这比通过 $H$ 场设定电流更简单。

---

## 7.3 PML 在三维中的应用

二维 PML 推广到三维需要处理 $D_x, D_y, D_z$ 三个分量。以 $D_z$ 为例：

$$\left(j\omega + \frac{\sigma_{D_x}}{\epsilon_0}\right)\left(j\omega + \frac{\sigma_{D_y}}{\epsilon_0}\right)D_z = c_0\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right]$$

定义积分辅助量：

$$\text{ID}_z = \frac{1}{j\omega}\left[\frac{\partial H_y}{\partial x} - \frac{\partial H_x}{\partial y}\right]$$

PML 层的电导率沿法向方向线性增加：

$$\sigma_D(x) = \sigma_{\max}\left(\frac{x}{d}\right)^m, \quad m=2\text{～}4$$

---

## 7.4 Numba 加速

三维 FDTD 需要大量内存（$N_x \times N_y \times N_z$ 个网格点）。纯 Python 循环速度极慢。Numba 库通过 JIT 编译将 Python 函数转换为机器码：

```python
from numba import njit

@njit
def update_H(Hx, Hy, Hz, Ex, Ey, Ez, dx, dy, dz, dt, mu):
    # Numba-compiled FDTD update loop
    # 性能接近 C 语言
    pass
```

典型加速比：10-100 倍。

---

## 7.5 数值直觉

> **内存估算**：$100\times100\times100$ 网格，单精度浮点（4 bytes）需要：
> $$N_{\text{fields}} \times N_x \times N_y \times N_z \times 4\text{ bytes} = 6 \times 10^6 \times 4 \approx 24\text{ MB}$$
> 三维仿真的内存随网格体积的三次方增长。

> **时间步长**：3D FDTD 的 $\Delta t$ 比 1D 的 $\Delta t = \Delta x/c$ 小 $\sqrt{3}$ 倍。对于均匀网格，$\Delta t = 0.577 \cdot \Delta x/c$，而 1D 中 $\Delta t = \Delta x/c$。

---

## 审计表格

| 公式 | 含义 | 验证 |
|:-----|:-----|:----:|
| 3D CFL | $\Delta t \leqslant h/(c\sqrt{3})$ | ✅ |
| 偶极子 $g_{az}=0$ | 金属 PEC 条件 | ✅ |
| PML 电导率 | $\sigma(x) = \sigma_{\max}(x/d)^m$ | ✅ |
| Numba @njit | JIT 编译加速 | ✅ |
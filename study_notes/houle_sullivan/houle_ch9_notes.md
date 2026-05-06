# Ch9: Advanced Python Features for FDTD

## 元信息
- **教材**: Houle & Sullivan — Electromagnetic Simulation Using the FDTD Method with Python (IEEE Press 2019)
- **章节**: Ch9 Advanced Python Features, pp.143-180
- **对应原文**: `/tmp/houle_ch9_raw.txt`

---

## 9.1 Numba JIT 加速

Numba 通过 `@njit`（no Python 对象模式）将 FDTD 循环编译为机器码：

```python
from numba import njit

@njit
def update_ez(ez, hy, dx, dt, epsz):
    # 编译后的 FDTD 更新
    for j in range(1, je-1):
        for k in range(1, ke-1):
            ez[ie, j, k] = gax[ie,j,k] * ez[ie,j,k] + ...
```

**关键性能指标**：
- 标准 Python 循环：$O(10^4)$ 倍慢于 C
- Numba @njit：接近 C 的性能，加速比 10-100 倍

---

## 9.2 namedtuple 与类封装

Houle 代码使用 namedtuple 封装常量和数据结构：

```python
from collections import namedtuple

# 常量封装
Constants = namedtuple('Constants', [
    'ddx', 'dt', 'arg', 't0', 'spread'
])

# PML 参数封装
PML = namedtuple('PerfectlyMatchedLayer', [
    'fi1','fi2','fi3','fj1','fj2','fj3','fk1','fk2','fk3',
    'gi1','gi2','gi3','gj1','gj2','gj3','gk1','gk2','gk3',
])
```

优点：Immutable、字典式访问、代码可读性高。

---

## 9.3 网格维度类

```python
class Dimensions:
    def __init__(self, x, y, z, xa, ya, za):
        self.x = x          # 网格单元数
        self.y = y
        self.z = z
        self.xa = xa        # PML 厚度
        self.ya = ya
        self.za = za
        self.xb = x - xa - 1  # 上边界
```

---

## 9.4 FDTD 类结构

完整 FDTD 程序架构：

```python
class FDTD3D:
    def __init__(self, nx, ny, nz, pml_thickness):
        self.dims = Dimensions(nx, ny, nz, pml_thickness)
        self.fields = FieldArrays(...)  # E/H/D/B 数组
        self.pml = PML(...)             # PML 系数
        
    def step(self):
        """一个时间步"""
        self.update_H()
        self.update_D()
        self.update_E()
        
    def run(self, n_steps):
        for _ in range(n_steps):
            self.step()
```

---

## 9.5 数值直觉

> **Numba vs C++**：对于 FDTD 更新循环，Numba 的性能约为手写 C 的 80-90%，但编程效率远高。
>
> **内存布局**：Numba 使用行优先（Row-major）存储，与 C 一致。访问模式 `ez[i,j,k]` 比 `ez[k,j,i]` 快得多。
>
> **PML 厚度**：通常 8-10 个网格单元。$\sigma_{\max}$ 取值需满足 $(σΔt)/(ε_0) \approx 0.2$，以避免低频反射。

---

## 审计表格

| 特性 | 作用 | 验证 |
|:-----|:-----|:----:|
| @njit | JIT 编译加速 | ✅ |
| namedtuple | 常量封装 | ✅ |
| class Dimensions | 网格参数管理 | ✅ |
| PML namedtuple | 吸收边界参数 | ✅ |
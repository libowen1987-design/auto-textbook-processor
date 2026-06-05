# Ch9: Object-Oriented Python for FDTD — Classes, Program Structure, and Interactive Widgets

> **中英双语版**
> **Source:** Houle & Sullivan — *Electromagnetic Simulation Using the FDTD Method with Python* (IEEE Press, 3rd ed. 2020), Chapter 5 (original pp. 129–158)
> **Core Topic:** Python OOP (classes) + namedtuple + PML refactoring + program modularization + Matplotlib interactive widgets

## 9.1 From Procedural to Object-Oriented | 从过程式到面向对象

### 9.1.1 Why Classes? | 为什么需要类？

In `fd3d_4_3.py`, there are 24 lines of separate field array initialization:
在 `fd3d_4_3.py` 中有 24 行独立的场数组初始化代码，可用一个 `Field` 类替代。

### 9.1.2 Field Class Definition | Field 类定义

```python
class Field(object):
    """Field in three directions: x, y, z."""
    def __init__(self, x_cells, y_cells, z_cells, initial_value):
        self.x = np.ones((x_cells, y_cells, z_cells)) * initial_value
        self.y = np.ones((x_cells, y_cells, z_cells)) * initial_value
        self.z = np.ones((x_cells, y_cells, z_cells)) * initial_value
```

Usage | 使用方式：
```python
e = Field(IE, JE, KE, 0)   # Electric field, 3 components, all zero | 电场，三分量，零初始
h = Field(IE, JE, KE, 0)   # Magnetic field | 磁场
d = Field(IE, JE, KE, 0)   # Flux density | 电通量
```

### 9.1.3 Class Methods | 类的方法

```python
def vector_magnitude(self):
    return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1 / 2)
```

### 9.1.4 Numba Compatibility | Numba 与自定义类的兼容

> Numba does not directly recognize custom classes. Use `@numba.jitclass` with explicit type declarations.
> Numba 不直接识别自定义类。需使用 `@numba.jitclass` 显式声明字段类型。

```python
@numba.jitclass([
    ('x', numba.float32[:, :, :]),
    ('y', numba.float32[:, :, :]),
    ('z', numba.float32[:, :, :])
])
class Field:
    def __init__(self, x_cells, y_cells, z_cells, initial_value):
        self.x = np.ones((x_cells, y_cells, z_cells), dtype=np.float32) * initial_value
        self.y = np.ones((x_cells, y_cells, z_cells), dtype=np.float32) * initial_value
        self.z = np.ones((x_cells, y_cells, z_cells), dtype=np.float32) * initial_value
```

---

## 9.2 Using namedtuple | namedtuple 的使用

### 9.2.1 What is namedtuple? | 什么是 namedtuple？

A lightweight immutable class factory from Python's `collections` module. Supports attribute access with dot notation.
来自 `collections` 模块的轻量级不可变类工厂，支持点号属性访问。

### 9.2.2 PML namedtuple Definition | PML namedtuple 定义

```python
from collections import namedtuple
PerfectlyMatchedLayer = namedtuple('PerfectlyMatchedLayer', (
    'fi1', 'fi2', 'fi3', 'fj1', 'fj2', 'fj3',
    'fk1', 'fk2', 'fk3', 'gi1', 'gi2', 'gi3',
    'gj1', 'gj2', 'gj3', 'gk1', 'gk2', 'gk3',
))
```

### 9.2.3 Simplified Function Signature | 函数签名简化

```python
# Before namedtuple: 18 separate array parameters
# After namedtuple: single pml object
@numba.jit(nopython=True)
def calculate_dx_field(IE, JE, KE, dx, idx, hy, hz, pml):
    curl_h = (hz[i,j,k] - hz[i,j-1,k] - hy[i,j,k] + hy[i,j,k-1])
    idx[i,j,k] = idx[i,j,k] + curl_h
    dx[i,j,k] = pml.gj3[j] * pml.gk3[k] * dx[i,j,k] + \
                pml.gj2[j] * pml.gk2[k] * (0.5 * curl_h + pml.gi1[i] * idx[i,j,k])
    return dx, idx
```

---

## 9.3 PML Parameter Slice Refactoring | PML 参数片重构

### 9.3.1 The DRY Problem | 代码重复问题

Original code repeated the same PML computation pattern 6 times (for i, j, k directions, offset 0 and 0.5).
原始代码将相同的 PML 计算模式重复了 6 次。

### 9.3.2 calculate_pml_slice Function | 抽象函数

```python
def calculate_pml_slice(size, offset, pml_cells):
    """Calculate a slice of PML params along one direction.
    fx1, gx2, gx3: offset = 0; gx1, fx2, fx3: offset = 0.5"""
    distance = np.arange(pml_cells, 0, -1)
    xxn = (distance - offset) / pml_cells
    xn = 0.33 * (xxn ** 3)
    p1 = np.zeros(size); p2 = np.ones(size); p3 = np.ones(size)
    p1[:pml_cells] = xn; p1[size-pml_cells:size] = np.flip(xn, 0)
    p2[:pml_cells] = 1/(1+xn); p2[size-pml_cells:size] = 1/(1+np.flip(xn,0))
    p3[:pml_cells] = (1-xn)/(1+xn); p3[size-pml_cells:size] = (1-np.flip(xn,0))/(1+np.flip(xn,0))
    return p1, p2, p3
```

### 9.3.3 Complete PML Generation (6 lines) | 完整 PML 生成

```python
fi1, gi2, gi3 = calculate_pml_slice(x_cells, 0, npml)
fj1, gj2, gj3 = calculate_pml_slice(y_cells, 0, npml)
fk1, gk2, gk3 = calculate_pml_slice(z_cells, 0, npml)
gi1, fi2, fi3 = calculate_pml_slice(x_cells, 0.5, npml)
gj1, fj2, fj3 = calculate_pml_slice(y_cells, 0.5, npml)
gk1, fk2, fk3 = calculate_pml_slice(z_cells, 0.5, npml)
```

**Before:** 62 lines of PML code; **After:** 6 calls + 25-line function = 60% reduction.

---

## 9.4 Program Structure | 程序整体结构

### 9.4.1 Refactoring Principles | 重构原则

1. **Single Responsibility | 单一职责**: each function does one thing
2. **Black-box design | 黑盒化**: clear input/output interfaces
3. **Testability | 可测试性**: independent unit testing
4. **No global variables | 避免全局变量**

### 9.4.2 Main Function Flow (fd3d_5_1.py) | main 函数高层流程

```
set_constants → generate_initial_arrays → calculate_pml_parameters → create_sphere → main_fdtd_loop:
  ├── calculate_incident_buffer
  ├── fourier_transform_inc_field
  ├── absorbing_bound_cond
  ├── calculate_dx/dy/dz_field (+ PML)
  ├── add_source_in_gap
  ├── calculate_inc_dy/dz_field (TF/SF)
  ├── calculate_e_fields
  ├── calculate_fourier_transform_ex
  └── calculate_hx/hy/hz_field
```

### 9.4.3 `__main__` Idiom

```python
if __name__ == '__main__':
    dims = Dimensions(x=40, y=40, z=40, xa=7, ya=7, za=7)
    main(nsteps=500, num_freq=3, freq=np.array((50e6, 200e6, 500e6)), dims=dims)
```

Ensures `main()` only runs when the script is executed directly, not when imported.
确保脚本直接运行时才执行 `main()`，而非被 import 时自动执行。

---

## 9.5 Dimensions Class | Dimensions 类

```python
@numba.jitclass([('x', numba.int16), ('y', numba.int16), ('z', numba.int16),
    ('x_center', numba.int16), ('y_center', numba.int16), ('z_center', numba.int16),
    ('xa', numba.int16), ('ya', numba.int16), ('za', numba.int16),
    ('xb', numba.int16), ('yb', numba.int16), ('zb', numba.int16)])
class Dimensions:
    def __init__(self, x, y, z, xa, ya, za):
        self.x = x; self.y = y; self.z = z
        self.x_center = int(x/2); self.y_center = int(y/2); self.z_center = int(z/2)
        self.xa = xa; self.ya = ya; self.za = za
        self.xb = x - xa - 1; self.yb = y - ya - 1; self.zb = z - za - 1
```

---

## 9.6 Matplotlib Interactive Widgets | Matplotlib 交互控件

### 9.6.1 Controller Class | Controller 类

```python
class Controller:
    def __init__(self, figure, current_ax, plot_parameters, fdtd_plot, bessel_plot):
        self.figure = figure; self.current_ax = current_ax
        self.plot_parameters = plot_parameters
        self.fdtd_plot = fdtd_plot; self.bessel_plot = bessel_plot
        self.selected_freq_label = plot_parameters[0].frequency_label
        radio_axes = plt.axes([0.03, 0.55, 0.15, 0.20])
        self.radio = RadioButtons(ax=radio_axes,
            labels=[o.frequency_label for o in plot_parameters])
        self.radio.on_clicked(self.on_radio_select)
```

### 9.6.2 Redraw Method | 核心方法——动态重绘

```python
def redraw(self):
    for plot_parameter in self.plot_parameters:
        if self.selected_freq_label == plot_parameter.frequency_label:
            self.fdtd_plot.set_data(plot_parameter.fdtd_location, plot_parameter.fdtd_amplitude)
            self.bessel_plot.set_data(plot_parameter.bessel_location, plot_parameter.bessel_amplitude)
            self.current_ax.relim()
            self.current_ax.autoscale_view(True, True, True)
            plt.draw()
```

### 9.6.3 PlotParameters namedtuple | 数据容器

```python
PlotParameters = namedtuple('PlotParameters',
    ['frequency', 'frequency_label', 'fdtd_location', 'fdtd_amplitude',
     'bessel_location', 'bessel_amplitude'])
```

---

## 9.7 Data Persistence with save_outputs | 数据持久化

```python
def save_outputs(freq, amp, compare_amp, x_array, compare_array):
    np.save('fdtd_amp', amp); np.save('bessel_amp', compare_amp)
    np.save('fdtd_x_axis', x_array); np.save('bessel_x_axis', compare_array)
    np.save('frequencies', freq)
```

---

## Audit Table | 审计表格

| Item | Source | Status |
|:-----|:------|:------:|
| Field class definition | raw text p.130 | ✅ |
| Field @numba.jitclass | raw text p.142 | ✅ |
| Dimensions class | raw text p.142 | ✅ |
| Constants namedtuple | raw text p.143 | ✅ |
| PML namedtuple | raw text p.132 | ✅ |
| calculate_pml_slice | raw text p.134 | ✅ |
| fd3d_5_1.py main loop | raw text p.147 | ✅ |
| Controller + RadioButtons | raw text p.138 | ✅ |
| save_outputs | raw text p.155 | ✅ |

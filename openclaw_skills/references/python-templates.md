# Python Templates Reference

## 标准文件头模板

```python
#!/usr/bin/env python3
"""
{书名} 第{n}章: {主题}
例题 {X.Y} / Figure {X.Y}
参考: {原书页码范围}
物理常数来源: scipy.constants
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import c, epsilon_0, mu_0, pi, kilo, mega, giga

# ============ 配置 ============
OUTPUT_DIR = 'figures/'
plt.style.use('science')
plt.rcParams.update({
    'font.size': 12,
    'axes.labelsize': 14,
    'axes.titlesize': 14,
    'legend.fontsize': 10,
    'figure.figsize': (10, 6),
    'savefig.dpi': 150,
    'savefig.bbox': 'tight',
})
```

## 物理常数使用规范

```python
# ✅ 正确：使用 scipy.constants
from scipy.constants import c, epsilon_0, mu_0, pi, nano, micro, milli
Z_0 = np.sqrt(mu_0 / epsilon_0)  # 真空阻抗 ~377Ω

# ✅ 正确：派生常数
f = 3e9  # Hz
lambda_ = c / f  # 波长

# ❌ 禁止：硬编码物理常数
Z_0 = 377  # 永远不要这样做
c = 3e8    # 永远不要这样做
```

## 变量命名规范（电磁学）

| 物理量 | 变量名 | 说明 |
|--------|--------|------|
| 真空阻抗 | `Z_0` | 约377Ω |
| 相对介电常数 | `epsilon_r` | 无量纲 |
| 复介电常数 | `epsilon_c = epsilon_r - j*sigma/omega/epsilon_0` | |
| 传播常数 | `gamma = alpha + j*beta` | |
| 衰减常数 | `alpha` | Np/m |
| 相位常数 | `beta` | rad/m |
| 特性阻抗 | `Z_0` | Ω |
| 电压驻波比 | `VSWR` | |
| 反射系数 | `Gamma`, `S11` | 复数 |
| 传输系数 | `T`, `S21` | 复数 |
| 散射矩阵 | `S` | 2×2或4×4复矩阵 |
| 磁导率 | `mu`, `mu_r` | H/m |
| 电导率 | `sigma` | S/m |
| 损耗角正切 | `tan_delta` | |
| 群延迟 | `tau_g` | s |
| 方向性 | `D` | dBi |
| 效率 | `eta` | 0~1 |

## 微波工程模板（skrf）

```python
import skrf as rf
import numpy as np

# 创建简单传输线模型
freq = rf.Frequency(1, 10, 101, unit='GHz')
Z_0 = 50  # 系统阻抗
d = 10e-3  # 线长 10mm
epsilon_r = 4.5  # Rogers RT/duroid 5880

# 计算介电填充的微带线参数
# 使用近似公式
beta = 2 * np.pi * freq.f / (c / np.sqrt(epsilon_r))
Z0_microstrip = 50 * (1 / np.sqrt(epsilon_r))  # 简化估算

# S参数计算
S11 = np.zeros_like(freq.f, dtype=complex)
S21 = np.exp(-1j * beta * d)
rf.Network(s=np.array([[S11, S21], [S21, S11]])), frequency=freq)
```

## 频域图表模板

```python
def plot_frequency_response(freq_ghz, S11_dB, S21_dB, title, filename):
    """绘制频率响应曲线（阻抗匹配分析用）"""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    # S11 (输入反射)
    ax1.plot(freq_ghz, S11_dB, 'b-', lw=2, label=r'$S_{11}$')
    ax1.axhline(y=-10, color='r', ls='--', alpha=0.7, label='-10 dB threshold')
    ax1.set_ylabel('|S₁₁| (dB)')
    ax1.set_title(title)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_ylim([-30, 0])
    
    # S21 (插入损耗)
    ax2.plot(freq_ghz, S21_dB, 'g-', lw=2, label=r'$S_{21}$')
    ax2.set_xlabel('Frequency (GHz)')
    ax2.set_ylabel('|S₂₁| (dB)')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved: {filename}")
```

## 史密斯圆图模板

```python
import skrf as rf
import numpy as np

def draw_smith_chart_with_traces(gamma, filename):
    """在史密斯圆图上绘制阻抗轨迹"""
    fig, ax = plt.subplots(figsize=8, 8))
    
    # 创建史密斯圆图网格
    # 使用 skrf 内置绘图
    freq = rf.Frequency(1, 10, 101, unit='GHz')
    network = rf.Network(s=gamma, frequency=freq)
    
    # 绘制S11轨迹
    ax = network.plot_s_smith(ax=ax, color='blue', lw=2)
    
    # 标记点
    ax.plot(np.real(gamma[0]), np.imag(gamma[0]), 'ro', markersize=10, label='Start')
    ax.plot(np.real(gamma[-1]), np.imag(gamma[-1]), 'go', markersize=10, label='End')
    
    ax.legend()
    ax.set_title('Impedance Trajectory on Smith Chart')
    plt.savefig(filename, dpi=150)
    plt.close()
```

## 双坐标系模板（时域+频域）

```python
def plot_time_and_freq(t_ns, signal, freq_ghz, spectrum_dB, title, filename):
    """双Y轴：时域波形 + 频谱"""
    fig, ax1 = plt.subplots(figsize=(12, 5))
    
    # 时域
    color1 = 'tab:blue'
    ax1.set_xlabel('Time (ns)')
    ax1.set_ylabel('Amplitude (V)', color=color1)
    ax1.plot(t_ns, signal, color=color1, lw=1.5)
    ax1.tick_params(axis='y', labelcolor=color1)
    
    # 频域（共享X轴）
    ax2 = ax1.twiny()
    color2 = 'tab:red'
    ax2.set_xlabel('Frequency (GHz)', color=color2)
    ax2.plot(freq_ghz, spectrum_dB, color=color2, lw=1.5)
    ax2.tick_params(axis='x', labelcolor=color2)
    
    plt.title(title)
    fig.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
```

## 场分布可视化模板（2D截面）

```python
def plot_field_2d(X, Y, Ez, Hx, Hy, title, filename):
    """绘制2D电磁场分布（FDTD结果可视化）"""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Ez场
    vmax = np.max(np.abs(Ez))
    im1 = axes[0].pcolormesh(X*100, Y*100, Ez, cmap='RdBu', vmax=vmax, vmin=-vmax, shading='gouraud')
    axes[0].set_xlabel('x (cm)')
    axes[0].set_ylabel('y (cm)')
    axes[0].set_title(r'$E_z$ field')
    plt.colorbar(im1, ax=axes[0])
    
    # Hx场
    vmax = np.max(np.abs(Hx))
    im2 = axes[1].pcolormesh(X*100, Y*100, Hx, cmap='RdBu', vmax=vmax, vmin=-vmax, shading='gouraud')
    axes[1].set_xlabel('x (cm)')
    axes[1].set_title(r'$H_x$ field')
    plt.colorbar(im2, ax=axes[1])
    
    # 坡印廷矢量 S = E × H*
    S_z = np.real(0.5 * Ez * np.conj(Hx))
    vmax = np.max(np.abs(S_z))
    im3 = axes[2].pcolormesh(X*100, Y*100, S_z, cmap='hot', vmax=vmax, vmin=0, shading='gouraud')
    axes[2].set_xlabel('x (cm)')
    axes[2].set_title(r'Power density $S_z$ (W/m²)')
    plt.colorbar(im3, ax=axes[2])
    
    plt.suptitle(title)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
```

## 批量生成子图模板

```python
def plot_parametric_study(param_values, results_dict, xlabel, title, filename):
    """参数化研究结果（单图多曲线）"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(param_values)))
    for param, color in zip(param_values, colors):
        ax.plot(results_dict[param]['x'], results_dict[param]['y'], 
                color=color, lw=2, label=f'{param}')
    
    ax.set_xlabel(xlabel)
    ax.set_ylabel('Response')
    ax.set_title(title)
    ax.legend(title='Parameter')
    ax.grid(True, alpha=0.3)
    
    plt.savefig(filename, dpi=150)
    plt.close()
```

## 错误处理规范

```python
def calculate_microstrip_Z0(epsilon_r, w_d, h):
    """
    计算微带线特性阻抗
    epsilon_r: 相对介电常数
    w_d: 线宽/介质厚度比 (w/h)
    h: 介质厚度 (m)
    """
    if epsilon_r < 1 or w_d <= 0:
        raise ValueError(f"Invalid params: epsilon_r={epsilon_r}, w_d={w_d}")
    
    # Quasi-static formula (Hammerstad-Jensen)
    if w_d < 1:
        # 窄微带
        Z0 = 60 / np.sqrt(epsilon_r) * np.log(8/w_d + w_d/4)
    else:
        # 宽微带
        Z0 = 120 * np.pi / (np.sqrt(epsilon_r) * (w_d + 1.393 + 0.667*np.log(w_d+1.444)))
    
    if not (1 < Z0 < 200):
        print(f"Warning: Z0={Z0:.1f}Ω outside typical range, check input params")
    
    return Z0
```

## 测试与验证模板

```python
def test_skin_depth():
    """测试：铜在1MHz下的皮肤深度 ≈ 0.066 mm"""
    from scipy.constants import mu_0, pi
    sigma_cu = 5.8e7  # S/m (铜电导率)
    f = 1e6  # 1 MHz
    
    delta = np.sqrt(2 / (2 * pi * f * mu_0 * sigma_cu))
    
    expected = 66e-6  # 66 µm
    assert abs(delta - expected) / expected < 0.05, f"skin depth error: {delta:.2e} vs {expected:.2e}"
    print(f"✓ skin depth test passed: {delta*1e6:.1f} µm")

def test_vacuum_impedance():
    """测试：真空阻抗 Z0 ≈ 376.73 Ω"""
    from scipy.constants import epsilon_0, mu_0
    Z0 = np.sqrt(mu_0 / epsilon_0)
    expected = 376.73
    assert abs(Z0 - expected) / expected < 0.001, f"Z0 error: {Z0:.2f} vs {expected:.2f}"
    print(f"✓ vacuum impedance test passed: {Z0:.2f} Ω")

if __name__ == '__main__':
    test_skin_depth()
    test_vacuum_impedance()
```
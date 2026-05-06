# Ch10: Treatment Planning and SAR

## 元信息
- **教材**: Houle & Sullivan — Electromagnetic Simulation Using the FDTD Method with Python (IEEE Press 2019)
- **章节**: Ch10 Deep Regional Hyperthermia Treatment Planning, pp.143-180
- **对应原文**: `/tmp/houle_ch10_raw.txt`

---

## 10.1 治疗计划系统

FDTD 用于深部热疗（Deep Regional Hyperthermia），通过局部加热杀死癌细胞。系统输入：

1. **CT 扫描图像** → 组织电导率 $\sigma$ 和介电常数 $\epsilon_r$
2. **相控阵天线（A1-A4）** → 四个馈源的幅度和相位
3. **目标点** → 期望最大场强位置

**工作流程**：

```
CT scan → super_apa.py → fd3d_apa.py → SAR distribution
         (分割组织)    (FDTD仿真)    (比吸收率)
```

---

## 10.2 SAR（比吸收率）

SAR 定义单位质量组织吸收的电磁功率：

$$\text{SAR} = \frac{\sigma |E|^2}{\rho}$$

其中 $\sigma$ 为电导率（S/m），$\rho$ 为组织密度（kg/m³）。

**临床阈值**：全身 SAR < 1 W/kg（IEEE C95.1-2019）。

---

## 10.3 相控阵天线相位控制

四个天线单元（A1-A4）的相位调节：

```python
def estimate_phases(ipos, jpos, field_pattern):
    """
    估计四个象限的相位，使得目标点场强最大。
    
    距离: dist_i = |r_target - r_antenna_i|
    相位补偿: φ_i = -k * dist_i
    """
    dist = [dist1, dist2, dist3, dist4]
    phases = [-k * d for d in dist]
    return phases
```

**场强叠加**：

$$E_{\text{total}} = \sum_{i=1}^{4} E_i \cdot e^{j\phi_i}$$

---

## 10.4 数值直觉

> **SAR 计算**：在 $50\times50\times50$ 网格中，计算每个网格点的 $\sigma|E|^2/\rho$。对于典型人体组织密度 $\rho \approx 1000\,$kg/m³，在 $E = 1000\,$V/m、$\sigma = 0.5\,$S/m 时：
> $$\text{SAR} = \frac{0.5 \times 10^6}{1000} = 500\,\text{W/kg}$$
> 这超过临床安全阈值，必须优化相位分布以降低峰值。

> **计算时间**：治疗计划 FDTD 仿真通常需要数千到数万时间步，相位优化需多次迭代，因此总时间可达数小时。

---

## 审计表格

| 公式 | 含义 | 验证 |
|:-----|:-----|:----:|
| SAR | $\sigma|E|^2/\rho$ | ✅ |
| 相位补偿 | $\phi_i = -k \cdot d_i$ | ✅ |
| 场叠加 | $E = \sum E_i e^{j\phi_i}$ | ✅ |
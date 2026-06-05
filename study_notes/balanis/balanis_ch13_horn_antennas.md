# Balanis Ch13 — Horn Antennas 学习笔记

> **来源:** Antenna Theory: Analysis and Design, 4th Ed., C. A. Balanis
> **范围:** §13.1–§13.6 | 量化验证级笔记

---

## §13.1 Introduction

**核心思想:** 喇叭天线通过将波导的口径逐渐张开（flare），将导行波平滑过渡到自由空间波。这样做有三个好处：

1. **阻抗匹配** — 波导特性阻抗 → 自由空间波阻抗 (377 Ω)
2. **增加方向性** — 口径面积 $A_p = A \times B$ 增大
3. **控制方向图** — 通过调节 flare 角平衡增益与相位误差

**分类:**

```
                   ┌─ E-plane sectoral (E面扇形)
  Rectangular Horn ── H-plane sectoral (H面扇形)
                   └─ Pyramidal (角锥喇叭)
  
  Circular Horn ─── Conical (圆锥喇叭)
  
  Corrugated Horn ── 波纹喇叭 (混合模 HE₁₁)
```

**关键物理量:**

| 符号 | 含义 | 量纲 |
|------|------|------|
| $a$ | 波导宽边 (x方向) | [L] |
| $b$ | 波导窄边 (y方向) | [L] |
| $A$ | 喇叭口径宽 (x方向) | [L] |
| $B$ | 喇叭口径高 (y方向) | [L] |
| $\rho_e$ | E面斜长 (apex to aperture in E-plane) | [L] |
| $\rho_h$ | H面斜长 (apex to aperture in H-plane) | [L] |
| $R_0$ | 喇叭轴向长度 | [L] |
| $\delta_e$ | E面口径最大相位差 $= B^2/(8\lambda\rho_e)$ | [1] |
| $\delta_h$ | H面口径最大相位差 $= A^2/(8\lambda\rho_h)$ | [1] |

---

## §13.2 Rectangular Horns

### 共同假设

- 馈电波导工作在 $\text{TE}_{10}$ 主模
- 口径场近似为波导 $\text{TE}_{10}$ 场分布乘以二次相位因子
- 喇叭壁为理想导体，壁厚忽略
- 使用口径场法（aperture-field method）计算远场

### 13.2.1 E-plane Sectoral Horn

**几何:** 波导在 E 面（y方向）张开，H 面保持波导尺寸 $a$。

**口径场:**

$$E_a = E_0 \cos\left(\frac{\pi x'}{a}\right) e^{-j k y'^2 / (2 \rho_e)} \quad \hat{\mathbf{y}}$$

其中二次相位来自球面波前在口径面的投影：
$$e^{-j k \Delta(y')} \approx e^{-j k y'^2/(2\rho_e)}$$

**辐射场 (E-plane, $\phi = \pi/2$):**

$$E_\theta(\theta) \propto \int_{-a/2}^{a/2} \cos\left(\frac{\pi x'}{a}\right) dx' \int_{-B/2}^{B/2} e^{-j k y'^2/(2\rho_e)} e^{j k y' \sin\theta} dy'$$

第一项积分给出 $\text{sinc}$ 函数；第二项为 Fresnel 积分。

**H-plane 方向图 ($\phi = 0$):** 与均匀照明矩形口径相同。
$$E_\theta(\theta) \propto \frac{\cos\left(\frac{k a}{2}\sin\theta\right)}{\left(\frac{\pi}{a}\right)^2 - (k\sin\theta)^2}
\times \int_{-B/2}^{B/2} e^{-j k y'^2/(2\rho_e)} dy'$$

**最大方向性:**

$$D_E = \frac{64 a \rho_e}{\pi \lambda b} \left[ C^2(u) + S^2(u) \right] \quad \text{[Balanis Eq. (13-30)]}$$

其中:
$$u = \frac{B}{\sqrt{2 \lambda \rho_e}}$$

$C(u)$ 和 $S(u)$ 为 Fresnel 积分:
$$C(u) = \int_0^u \cos\left(\frac{\pi t^2}{2}\right) dt, \quad
S(u) = \int_0^u \sin\left(\frac{\pi t^2}{2}\right) dt$$

**最佳设计 (Optimum):** $u \approx 1$ → $B \approx \sqrt{2 \lambda \rho_e}$

此时 $\delta_e = B^2/(8\lambda\rho_e) = \frac{1}{4}\lambda$ （即 90° 相位差）

**HPBW 近似 (E-plane):**

$$\text{HPBW}_E \approx 2 \arcsin\left(\frac{0.94\lambda}{B}\right) \text{[rad]}$$

### 13.2.2 H-plane Sectoral Horn

**几何:** 波导在 H 面（x方向）张开，E 面保持波导尺寸 $b$。

**口径场:**

$$E_a = E_0 \cos\left(\frac{\pi x'}{A}\right) e^{-j k x'^2 / (2 \rho_h)} \quad \hat{\mathbf{y}}$$

**辐射场 (H-plane, $\phi = 0$):**

$$E_\phi(\theta) \propto \int_{-A/2}^{A/2} \cos\left(\frac{\pi x'}{A}\right) e^{-j k x'^2/(2\rho_h)} e^{j k x' \sin\theta} dx' \times \int_{-b/2}^{b/2} dy'$$

**最大方向性:**

$$D_H = \frac{4\pi b \rho_h}{\lambda a} \, \varepsilon_t \, \varepsilon_{ph}
\quad \text{where } \varepsilon_t = \frac{8}{\pi^2}, \;
\varepsilon_{ph} = \frac{\pi^2}{64 t} \left\{ [C(p_1) - C(p_2)]^2 + [S(p_1) - S(p_2)]^2 \right\}$$

参数:
$$t = \frac{1}{8} \left( \frac{A}{\sqrt{\lambda \rho_h}} \right)^2 =
\frac{A^2}{8\lambda \rho_h} = \frac{\delta_h}{\lambda}$$

$$p_1 = \frac{1}{\sqrt{2}} \left( \frac{\sqrt{\lambda \rho_h}}{A} + \frac{A}{\sqrt{\lambda \rho_h}} \right) =
\sqrt{2} \left( \frac{1}{4\sqrt{t}} + \sqrt{t} \right)$$

$$p_2 = \frac{1}{\sqrt{2}} \left( \frac{\sqrt{\lambda \rho_h}}{A} - \frac{A}{\sqrt{\lambda \rho_h}} \right) =
\sqrt{2} \left( \frac{1}{4\sqrt{t}} - \sqrt{t} \right)$$

也可写作简化形式:

$$D_H = \frac{4\pi b}{\lambda a} \rho_h \varepsilon_{ap}$$

其中 $\varepsilon_{ap} = \varepsilon_t \varepsilon_{ph}$ 为口径效率。

**最佳设计:** $\delta_h \approx 0.375\lambda$ → $t \approx 0.375$ 或 $A \approx \sqrt{3\lambda \rho_h}$

**HPBW 近似 (H-plane):**

$$\text{HPBW}_H \approx 2 \arcsin\left(\frac{0.68\lambda}{A}\right) \text{[rad]}$$

### 13.2.3 Pyramidal Horn (角锥喇叭)

**核心思想:** E 面和 H 面同时张开。设计的关键约束为 **几何一致性**:

$$\frac{\rho_e}{B} = \frac{\rho_h}{A} \quad \text{(两斜面交于同一点)}$$

或者更精确地:
$$\frac{\rho_e}{B-b} = \frac{\rho_h}{A-a} = \frac{R_0}{2}$$

其中 $R_0$ 为喇叭轴向长度。

**方向性:**

$$D_P = \frac{8\pi}{\lambda^2} \frac{A B}{64} \, \varepsilon_t \, \varepsilon_{ph,E} \, \varepsilon_{ph,H}$$

更常用的形式 (Balanis Eq. 13-48):

$$D_P = \frac{4\pi}{\lambda^2} (A B) \, \varepsilon_{ap}$$

其中 $\varepsilon_{ap} = \varepsilon_t \varepsilon_{ph,E} \varepsilon_{ph,H}$。

**Schelkunoff 增益公式 (经验设计):**

$$G(\text{dBi}) = 10 \log_{10} \left( \frac{4\pi}{\lambda^2} A B \right) - L_E(s) - L_H(t)$$

其中 $L_E(s)$ 和 $L_H(t)$ 为增益缩减因子 (dB)，与相位误差参数 $s$ 和 $t$ 有关:

$$s = \frac{B^2}{8\lambda \rho_e} \quad (\text{E-plane phase error in wavelengths})$$
$$t = \frac{A^2}{8\lambda \rho_h} \quad (\text{H-plane phase error in wavelengths})$$

**最优设计:** 同时达到 $\delta_e = 0.25\lambda$ (E-plane) 和 $\delta_h = 0.375\lambda$ (H-plane)。

**HPBW:**

$$\text{HPBW}_E \approx 2 \arcsin\left(\frac{0.94\lambda}{B}\right)$$
$$\text{HPBW}_H \approx 2 \arcsin\left(\frac{0.68\lambda}{A}\right)$$

**第一次旁瓣电平 (SLL):**

- E-plane: $\approx -13$ dB (余弦分布)
- H-plane: $\approx -13$ dB 但受相位误差影响退化至 $-11$ dB

---

## §13.3 Circular Horns (Conical Horn)

**几何:** 圆波导馈电，锥形张开的圆形口径。

**口径场 (TE₁₁ 主模):**

$$E_a = E_0 J_1(\chi'_{11} \rho'/a) e^{-j k \rho'^2/(2\rho_0)} \cdot \hat{\boldsymbol{\rho}}' \text{ 分量}$$

其中 $\chi'_{11} \approx 1.841$ 为一阶贝塞尔函数导数的第一个零点，$a$ 为圆波导半径。

**最大方向性 (近似):**

$$D_0 \approx \frac{4\pi}{\lambda^2} (\pi a_m^2) \, \varepsilon_{ap}$$

其中 $a_m$ 为喇叭口径半径，$\varepsilon_{ap} \approx 0.5\text{–}0.6$。

**最佳设计:** 口径最大相位差 $\delta = \frac{a_m^2}{2\lambda\rho_0} \approx 0.25\lambda$ (即 90°)。

---

## §13.4 Corrugated Horns

**关键创新:** 在喇叭内壁刻 λ/4 深槽，改变边界条件:

- E 面: 槽等效为短路 → $E_\phi = 0$
- 效果: 口径场对称分布 → E/H 面方向图完全一致

**混合模 HE₁₁:**

$$E_a \propto \begin{cases}
J_0(\chi_{01} \rho'/a_m) & \text{轴对称分量} \\
J_2(\chi_{21} \rho'/a_m) \cos 2\phi' & \text{四极分量}
\end{cases}$$

**优点:**
- 交叉极化电平极低 ($< -30$ dB)
- 旁瓣电平低 ($< -30$ dB)
- 方向图旋转对称 → 理想馈源
- 可使用高斯束模型近似

**高斯耦合效率:**
$$\eta_g = \frac{|\iint E_a \cdot \psi_g \, dS|^2}{\iint |E_a|^2 dS \iint |\psi_g|^2 dS} \approx 0.98$$

其中 $\psi_g$ 为基模高斯束。

---

## §13.5 Aperture Matching

**问题:** 口径不连续 → 反射 → VSWR 升高。

**方法:**

1. **λ/4 匹配段:** 在喇叭喉部插入渐变节
2. **阶梯匹配:** 多节 λ/4 变换器
3. **脊波导:** 在波导宽边加脊降低阻抗比

**反射系数近似 (小喇叭):**

$$|\Gamma| \approx \frac{(a-A)(b-B)}{(a+A)(b+B)}$$

**工程要点:** 标准增益喇叭通常 VSWR < 1.1 (回波损耗 > 26 dB)。

---

## §13.6 Horn Design Considerations

### 标准增益喇叭设计流程 (以 Pyramidal 为例)

**已知:** 工作频率 $f$ (波长 $\lambda$)，目标增益 $G_0$ (dBi)

**步骤:**

1. **选择波导尺寸:** $a$ 和 $b$ (确保单模传输: $a < \lambda < 2a$, $b < \lambda/2$)

2. **确定口径尺寸:**
   近似解: $A \approx \sqrt{\frac{G_0 \lambda^2}{4\pi \varepsilon_{ap}}}$, $B \approx \frac{A}{1.3\text{–}1.5}$ (保持合理 flare 角)

3. **确定斜长:**
   $$\rho_e = \frac{B^2}{8\lambda \delta_e}, \quad \delta_e \approx 0.25$$
   $$\rho_h = \frac{A^2}{8\lambda \delta_h}, \quad \delta_h \approx 0.375$$

4. **轴向长度:**
   $$R_0 = \frac{\rho_e B}{B-b} = \frac{\rho_h A}{A-a}$$

5. **验证增益:** 使用 Schelkunoff 公式迭代微调。

---

## 关键设计公式汇总表

| 参数 | E-plane Sectoral | H-plane Sectoral | Pyramidal |
|------|-----------------|------------------|-----------|
| 口径宽 $A$ | $a$ (波导宽) | $A$ (张开) | $A$ |
| 口径高 $B$ | $B$ (张开) | $b$ (波导窄) | $B$ |
| 最佳相位差 $\delta$ | $0.25\lambda$ | $0.375\lambda$ | 0.25 (E) / 0.375 (H) |
| 最佳口径尺寸 | $B \approx \sqrt{2\lambda\rho_e}$ | $A \approx \sqrt{3\lambda\rho_h}$ | 联合求解 |
| HPBW (度) | $2\arcsin(0.94\lambda/B)$ | $2\arcsin(0.68\lambda/A)$ | 组合 |
| SLL (dBi) | $\approx -13$ | $\approx -13$ | $-13$ / $-11$ |
| 方向性公式 | $D_E = \frac{64a\rho_e}{\pi\lambda b}[C^2+S^2]$ | $D_H = \frac{4\pi b\rho_h}{\lambda a}\varepsilon_t\varepsilon_{ph}$ | $D_P = \frac{4\pi}{\lambda^2}AB\varepsilon_{ap}$ |

---

## 量纲一致性标注

- 所有长度量 $[L]$: $a, b, A, B, \rho_e, \rho_h, \lambda, R_0$
- Fresnel 参数 $u, p_1, p_2, t, s$: 无量纲 $[1]$
- $C(u), S(u)$: 无量纲 $[1]$
- 增益/方向性 $D$: 无量纲 (功率比)
- 相位差 $\delta$: 量纲 $[L]$, 以 $\lambda$ 倍数给出

---

## 物理直觉

1. **相位误差是双刃剑:** 增大口径 → 增益↑ 但相位误差↑ → 效率↓。最优解是平衡点。
2. **E 面和 H 面不对称:** TE10 模在 E 面是均匀分布（余弦项在 x），H 面有余弦幅度锥削。因此 H 面 HPBW 更窄。
3. **波纹喇叭为何好:** 改变边界条件使 E 面电流为零 → 口径场对称 → 完美馈源。
4. **角锥喇叭是最实用选择:** 增益 10–25 dBi，带宽 > 40%，制造简单。

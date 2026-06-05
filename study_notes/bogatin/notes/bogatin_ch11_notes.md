---
title: "Chapter 11 — Differential Pairs"
book: "Signal Integrity and Power Integrity (2nd Ed.)"
author: "Eric Bogatin"
chapter: 11
pages: "504–582"
---

# Ch11: Differential Pairs

> **中英双语版**

## 11.1 Differential vs. Common Signals | 差模与共模信号

**Differential signal:** $V_{\text{diff}} = V_1 - V_2$ (signal swings opposite on each line)
**差模信号：** 两根线上信号反向摆动，差值为有效信号。

**Common signal:** $V_{\text{comm}} = (V_1 + V_2)/2$ (both lines swing together)
**共模信号：** 两根线同向摆动，取平均值为共模分量。

## 11.2 Odd Mode and Even Mode | 奇模与偶模

**Odd mode:** Lines driven with opposite polarity ($+V, -V$)
**奇模：** 两条线以相反极性驱动。

**Even mode:** Lines driven with same polarity ($+V, +V$)
**偶模：** 两条线以相同极性驱动。

**Impedances | 阻抗：**
- $Z_{\text{odd}}$: impedance of one line in odd mode（奇模下单线阻抗）
- $Z_{\text{even}}$: impedance of one line in even mode（偶模下单线阻抗）
- $Z_{\text{diff}} = 2 \times Z_{\text{odd}}$: impedance seen by differential signal（差模信号看到的阻抗）
- $Z_{\text{comm}} = Z_{\text{even}} / 2$: impedance seen by common signal（共模信号看到的阻抗）

## 11.3 Effect of Coupling | 耦合效应

For coupled lines with mutual inductance $L_m$ and mutual capacitance $C_m$:
对于具有互感 $L_m$ 和互容 $C_m$ 的耦合线：

$$
Z_{\text{odd}} = \sqrt{\frac{L_L - L_m}{C_L + C_m}} = Z_0 \sqrt{\frac{1 - k_L}{1 + k_C}}
$$

$$
Z_{\text{even}} = \sqrt{\frac{L_L + L_m}{C_L - C_m}} = Z_0 \sqrt{\frac{1 + k_L}{1 - k_C}}
$$

where $k_L = L_m/L_L$, $k_C = C_m/C_L$
其中 $k_L$ 和 $k_C$ 分别为电感耦合系数和电容耦合系数。

**Key results | 关键结论：**
- **Tighter coupling** → lower $Z_{\text{diff}}$（耦合越紧 → 差模阻抗越低）
- **Tighter coupling** → higher $Z_{\text{common}}$（耦合越紧 → 共模阻抗越高）
- **Tighter coupling** → lower differential-to-common conversion（耦合越紧 → 差模-共模转换越小）

## 11.4 Advantages of Differential Signaling | 差分信号的优势

1. **Less EMI** → fields cancel for differential signals（场相互抵消，EMI 更小）
2. **Better noise immunity** → external noise couples as common mode, rejected by receiver（外部噪声耦合为共模，被接收机抑制）
3. **Less rail collapse** → current is constant (one line goes up, other goes down)（电流近似恒定，电源轨塌陷小）
4. **Higher signal swing** for same supply voltage（同等供电电压下信号摆幅更大）
5. **Less sensitivity to ground bounce**（对地弹不敏感）

## 11.5 Common Terms | 常用术语

| Term | Meaning | 中文含义 |
|:--|:--|:--|
| $Z_{\text{diff}}$ | Impedance between the two lines (differential) | 差模阻抗（两线之间） |
| $Z_{\text{odd}}$ | Impedance of one line, odd-mode drive | 奇模阻抗（单线） |
| $Z_{\text{even}}$ | Impedance of one line, even-mode drive | 偶模阻抗（单线） |
| $S_{\text{dd21}}$ | Differential transmission S-parameter | 差模传输 S 参数 |
| $S_{\text{cc21}}$ | Common-mode transmission S-parameter | 共模传输 S 参数 |
| $S_{\text{cd21}}$ | Mode conversion (diff→common) | 模式转换（差模→共模） |

> **Engineering Intuition:** In a differential pair, "coupling" between lines REDUCES differential impedance. Tight coupling means the two lines are close together, so each line "sees" the other as part of its return path.
> **工程直觉：** 在差分对中，线间耦合**降低**差模阻抗。紧耦合意味着两根线靠得很近，每条线都将另一条线视为其返回路径的一部分。

## 11.6 Key Formulas | 关键公式

| Formula | Description | 中文说明 |
|:--|:--|:--|
| $V_{\text{diff}} = V_1 - V_2$ | Differential signal | 差模信号 |
| $V_{\text{comm}} = (V_1 + V_2)/2$ | Common signal | 共模信号 |
| $Z_{\text{diff}} = 2 \cdot Z_{\text{odd}}$ | Differential impedance | 差模阻抗 |
| $Z_{\text{comm}} = Z_{\text{even}}/2$ | Common impedance | 共模阻抗 |
| $Z_{\text{odd}} = \sqrt{(L_L - L_m)/(C_L + C_m)}$ | Odd-mode impedance | 奇模阻抗 |
| $Z_{\text{even}} = \sqrt{(L_L + L_m)/(C_L - C_m)}$ | Even-mode impedance | 偶模阻抗 |

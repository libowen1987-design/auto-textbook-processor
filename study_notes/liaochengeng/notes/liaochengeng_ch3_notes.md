# 廖承恩《微波技术基础》 第3章：波导理论

> **来源：** 谢处方等，《电磁场与电磁波》，第3章
> **提取方式：** 📷 扫描PDF → OCR → 人工清洗

---

## 3.1 波导理论 | Waveguide Theory

# 廖承恩《微波技术基础》第3章
 本笔记基于  文本清洗整理100% 来源于原书内容
## 第3章 规则金属波导
### 3.1 矩形波导
矩形波导截面尺寸 $ \ $$  $传输  或  模不能传输  模
#### 波动方程（Helmholtz）
$$\nabla^2 $\mathbf{E}$ + $\mathbf{k}$^2 $\mathbf{E}$ = 0, \quad $\mathbf{k}$ = \frac{2\pi}{\lambda} = $\omega$\sqrt{$\mu$\varepsilon}$$
矩形波导中 $(x,y)$ 方向的边界条件为Dirichlet（理想导体边界）。
  模$ = 0$$ \ 0$
$$$\mathbf{H}$_z(x,y,z) = $\mathbf{H}$_0 \cos\left(\frac{m\pi x}{a}\right) \cos\left(\frac{n\pi y}{b}\right) e^{-\gamma z}$$
截止波数：$$\mathbf{k}$_c^2 = \left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2$
#### 截止波长
$$\lambda_c = \frac{2}{\sqrt{(m/a)^2 + (n/b)^2}}$$
主模 ${10}$$\ = 2$$ = /\tag{2}$
#### 传播常数
$$\gamma = \alpha + j\beta = \sqrt{$\mathbf{k}$_c^2 - $\mathbf{k}$^2}$$
- $$\mathbf{k}$ > $\mathbf{k}$_c$（$f > f_c$）：$\alpha = 0$，$\beta = \sqrt{$\mathbf{k}$^2 - $\mathbf{k}$_c^2}$，**传播**
- $$\mathbf{k}$ < $\mathbf{k}$_c$（$f < f_c$）：$\alpha > 0$，$\beta = 0$，**截止**
#### 相速度和群速度
$$v_p = \frac{\omega}{\beta} = \frac{v}{\sqrt{1 - ($\lambda$/\lambda_c)^2}} > v$$
$$v_g = \frac{d\omega}{d\beta} = v\sqrt{1 - ($\lambda$/\lambda_c)^2} < v$$
$$v_p \cdot v_g = v^2$$
#### 波导波长
$$\lambda_g = \frac{2\pi}{\beta} = \frac{\lambda}{\sqrt{1 - ($\lambda$/\lambda_c)^2}}$$
 传输功率${}$ 模
$$$\mathbf{P}$ = \frac{1}{2} \int_0^a \int_0^b \mathrm{Re}($\mathbf{E}$_x $\mathbf{H}$_y^* - $\mathbf{E}$_y $\mathbf{H}$_x^*) dx\,dy = \frac{a b}{4Z_{TE}} |$\mathbf{H}$_0|^2 (1+\delta_{m0})(1+\delta_{n0})$$
其中 ${} = $\$/\{1-($\$/\)^2}$ 为  模的波阻抗
---
### 3.2 圆波导
圆形波导截面半径为 $$传输  和  模用柱坐标系 $(\)$ 分析
#### 模式方程
${}$$( ) = 0$$ = \{}/$$\{}$ 为 $$ 阶贝塞尔函数导数的第 $$ 个根
${}$$( ) = 0$$ = \{}/$$\{}$ 为 $$ 阶贝塞尔函数的第 $$ 个根
#### 常用模式
- ${11}$主模$\ = 1.706$
- ${01}$对称模式$\ = 2.613$
- ${01}$低损耗模式圆波导通信
---
### 3.3 微带传输线
**微带线 ( )**介质基片上印刷导体带的传输线工作于准  模
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
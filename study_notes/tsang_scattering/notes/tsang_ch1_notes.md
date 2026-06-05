# Tsang《Scattering of EM Waves》Chapter 1

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

> **第一章：矢量柱面波与圆柱散射理论导引**。本章涵盖第一卷第1章的基础理论，包括Bessel/Hankel函数的矢量柱面波表示、平移加法定理、圆柱散射体的T矩阵方法，以及多根圆柱的多次散射方程推导。以下内容包含来自第12章（边界存在下的圆柱多次散射）的公式推导引用。

**Chapter 1 overview:** Chapter 1 of Volume I covers the fundamental theory of vector cylindrical wave expansions, the translation addition theorem for cylindrical waves, and the T-matrix approach for scattering by dielectric cylinders. Below are additional derivations related to multiple scattering by cylinders in the presence of reflective boundaries (Chapter 12).

> **第1章概览**：第一卷第1章涵盖矢量柱面波展开、柱面波平移加法定理、电介质圆柱的T矩阵方法等基础理论。以下公式来自第12章边界存在下圆柱的多次散射推导。

**Multiple scattering derivation references / 多次散射推导引用:**

Chapter 1 of Volume I, with Hankel functions replaced by Bessel functions.
The integral in the first term of (12.2.48) is over dk, with kop = {k? — Ke)?
while the second term is over dky with ko, = (k? — k3)'/?. This gives

> 第一卷第1章，将Hankel函数替换为Bessel函数。(12.2.48)第一项对dk积分(kop=(k²−k_x²)^(1/2))，第二项对dk_y积分(kop=(k²−k₀²)^(1/2))。

Step iii: We next use the translation addition theorem to express vector
cylindrical waves centered at F; in terms of vector cylindrical waves centered
at F,. We can then derive the expression of an exciting field at cylinder J due
to a scattered field from cylinder j.

> **步骤(iii)**：使用平移加法定理将中心在r_j的矢量柱面波用中心在r_l的矢量柱面波表示，从而得到圆柱l处由圆柱j散射场产生的激发场表达式。

--- (formulas 12.2.49, 12.2.50, 12.2.51) ---

> **关键概念总结**：
> 1. **矢量柱面波（Vector Cylindrical Waves）**：M_n和N_n波函数是Maxwell方程在柱坐标系中的基本解，分别对应TE_z和TM_z模式。
> 2. **平移加法定理（Translation Addition Theorem）**：将柱面波在不同坐标系中心之间变换的数学工具，是多圆柱散射的核心。
> 3. **Green函数展开**：自由空间G₀和反射G_ref的并矢格林函数用柱面波展开，用于描述散射场传播。
> 4. **Zenneck表面波**：介质分界面的表面波模式，在复k_z平面分析中可能出现极点贡献。
> 5. **锥形图样（Conical Pattern）**：有限长圆柱的散射图样由sinc函数描述，在垂直方向形成锥形分布。
> 6. **Foldy-Lax方程**：通过自洽激发场方法建立多圆柱间的耦合多次散射方程。

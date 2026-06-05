# Introduction to Electromagnetic Analysis and Computational Electromagnetics / 电磁分析与计算电磁学导论

> **中英双语版**

**Source:** Chew, *Fast and Efficient Algorithms in Computational Electromagnetics*, Chapter 1
**来源：** Chew《计算电磁学中的快速高效算法》第1章

---

## 1.1 Introduction / 引言

Electromagnetic analysis, a discipline whereby one solves Maxwell's equations to obtain a better understanding of a complex system, is becoming increasingly important in electrical engineering. One reason is that Maxwell's theory is essential for the manipulation of electricity and hence is indispensable. Another reason is that Maxwell's theory has proven to have strong predictive power. This strong predictive power, together with the advent of computer technology, has changed the practice of electrical engineering in recent years. A complete solution to Maxwell's equations can expedite many electrical engineering design processes.
电磁分析是一门通过求解麦克斯韦方程组来更好地理解复杂系统的学科，在电气工程中日益重要。原因之一是麦克斯韦理论是驾驭电力的基础，不可或缺。另一个原因是麦克斯韦理论已被证明具有强大的预测能力。这种强大的预测能力，加上计算机技术的出现，近年来改变了电气工程的实践。完整求解麦克斯韦方程组可以加速许多电气工程设计过程。

A notable example is the integrated circuits industry where computer-aided design predictive tools, using circuit theory that is partly based on low-frequency Maxwell's theory, have completely changed how electrical engineering design processes are performed.
一个显著的例子是集成电路行业，其中基于部分低频麦克斯韦理论的电路理论CAD预测工具，彻底改变了电气工程设计流程的实施方式。

In the beginning, electromagnetic analyses were performed with pencil and paper, solving for closed form and approximate solutions. However, this has changed with the advent of numerical methods and computers, which have spurred the field of "computational electromagnetics."
最初，电磁分析是用纸笔完成的，求解闭合形式和近似解。然而，随着数值方法和计算机的出现，这一情况发生了改变，催生了"计算电磁学"领域。

Traditional numerical methods are inefficient, but fast algorithms in computational electromagnetics will alter the use of many of these electromagnetic analysis methods in the future. For a problem with N degrees of freedom, or N unknowns, many of these fast algorithms use O(N log N) memory, and close to O(N log N) time, as opposed to the traditional methods requiring O(N²) memory and O(N²) time.
传统的数值方法效率低下，但计算电磁学中的快速算法将改变许多电磁分析方法的使用方式。对于具有N个自由度（或N个未知数）的问题，许多快速算法仅需O(N log N)内存和接近O(N log N)时间，而传统方法需要O(N²)内存和O(N²)时间。

Despite its arcane sounding name, "computational electromagnetics" is actually highly interdisciplinary, drawing knowledge from physics, mathematics, and computer science.
尽管名字听起来深奥，"计算电磁学"实际上高度跨学科，从物理学、数学和计算机科学中汲取知识。

---

## 1.2 A Bit of History / 历史的吉光片羽

Maxwell's theory was completed over a century ago in 1864 [1]. At the time of its completion, it was regarded as a triumph by mathematicians and physicists alike. Maxwell's theory unifies both the theory of light and the theory of electromagnetism, which were thought to be two different theories. The motivation to add displacement current to Ampere's Law to complete Maxwell's equations was both a mathematical and a physical one.
麦克斯韦理论在一个多世纪前的1864年完成[1]。在其完成之时，被数学家和物理学家视为一项胜利。麦克斯韦理论统一了光的理论和电磁理论，此前这被认为是两种不同的理论。在安培定律中加入位移电流以完善麦克斯韦方程组的动机既是数学的也是物理的。

The existence of electromagnetic fields as waves was finally confirmed by Heinrich Hertz in 1888, and later the propagation of radio wave across the Atlantic Ocean was demonstrated by Guglielmo Marconi in 1901.
电磁场以波的形式存在的实验最终由海因里希·赫兹于1888年证实，随后古列尔莫·马可尼于1901年演示了无线电波跨大西洋传播。

Maxwell's equations are given by / 麦克斯韦方程组如下：

$$
\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} \tag{1.1}
$$

$$
\nabla \times \mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J} \tag{1.2}
$$

$$
\nabla \cdot \mathbf{D} = \rho \tag{1.3}
$$

$$
\nabla \cdot \mathbf{B} = 0 \tag{1.4}
$$

Shortly after the advent of Maxwell's theory, closed form solutions to Maxwell's equations were sought by the separation of variables. For instance, the Mie scattering solution for a sphere was found around the end of the 19th century [3,4]. The guided wave solution in a hollow waveguide was given by Rayleigh in 1897 [5]. The famous Sommerfeld half-plane solution for diffraction of waves by a semi-infinite half plane was presented by Sommerfeld in 1896 [6].
麦克斯韦理论出现后不久，人们就开始通过分离变量法寻找麦克斯韦方程组的闭合形式解。例如，19世纪末发现了球的Mie散射解[3,4]。瑞利于1897年给出了空心波导中的导波解[5]。著名的Sommerfeld半平面临界衍射解由Sommerfeld于1896年提出[6]。

### A Brief History of Numerical Methods / 数值方法简史

Numerical methods for differential equations were concurrently developed. The finite-difference technique for solving partial differential equations was developed by Courant, Friedrichs, and Lewy in 1928 [17]. The finite element method was developed in the 1950s—its efficiency has been documented by Zienkiewicz [18].
微分方程的数值方法也在同步发展。求解偏微分方程的有限差分技术由Courant、Friedrichs和Lewy于1928年提出[17]。有限元方法于20世纪50年代发展起来，Zienkiewicz[18]记录了其效率。

The numerical solution of integral equations was pioneered by Harrington in the 1960s when the method of moments was introduced to solve electromagnetic problems [24,25]. Rokhlin founded the fast multipole method (FMM) for the Laplace equation in 1985 which became the cornerstone for the multilevel fast multipole algorithm (MLFMA) for the Helmholtz equation [105–107].
积分方程的数值求解由Harrington在20世纪60年代开创，当时他将矩量法引入电磁问题求解[24,25]。Rokhlin于1985年为拉普拉斯方程创立了快速多极子方法(FMM)，这成为亥姆霍兹方程多层快速多极子算法(MLFMA)的基石[105–107]。

---

## 1.3 More on Differential Equation Solvers / 微分方程求解器详解

There is a distinct difference between differential equation solvers and integral equation solvers. In differential equation solvers, one solves for the field that permeates all of space. In contrast, integral equation solvers solve for the sources. For surface scattering phenomena, the equivalent currents reside on the surface or at the interface between regions, reducing the dimensionality of the problem.
微分方程求解器与积分方程求解器之间存在显著差异。在微分方程求解器中，求解的是充满整个空间的场。相比之下，积分方程求解器求解的是源。对于表面散射现象，等效电流位于表面或区域间的界面上，从而降低了问题的维度。

Since the computer has only a finite amount of memory, to mimic an infinite space, differential equation solvers require the use of the absorbing boundary condition to emulate the radiation condition at infinity [18,57]. In contrast, an integral equation can be derived with Green's functions satisfying the radiation condition, and hence providing solutions that satisfy the radiation condition.
由于计算机只有有限的内存，为了模拟无限空间，微分方程求解器需要使用吸收边界条件来模拟无穷远处的辐射条件[18,57]。相比之下，积分方程可以用满足辐射条件的格林函数推导，因此提供满足辐射条件的解。

In solving differential equations, one constructs a numerical grid on which a field is propagated—hence, a field propagates from point A to point B via a numerical grid. A small amount of error is often committed in this mode of field propagation, giving rise to a phase error in the field. This phase error is cumulative and becomes larger with larger simulation size.
在求解微分方程时，需要构建一个数值网格，场在网格上传播——因此，场从点A传播到点B是通过数值网格完成的。在这种场的传播模式中，常常会产生少量误差，导致场的相位误差。这种相位误差是累积的，随仿真规模增大而增大。

### 1.3.1 Convergence Rate of Iterative Differential Equation Solvers / 迭代微分方程求解器的收敛速率

Since differential equation solvers are associated with sparse matrices with O(N) elements, a matrix-vector product is achieved in O(N) operations. When the matrix system is solved iteratively, the only remaining avenue for accelerating differential equation solvers is to reduce the number of iterations needed or the number of time steps needed in time-stepping methods.
由于微分方程求解器与具有O(N)元素的稀疏矩阵相关，矩阵-矢量乘积可在O(N)操作内完成。当迭代求解矩阵系统时，加速微分方程求解器的唯一途径是减少所需的迭代次数或时步法所需的时间步数。

The convergence rate in a matrix equation is determined by the condition number of the matrix, which is the ratio of its largest eigenvalue to its smallest eigenvalue.
矩阵方程中的收敛速率由矩阵的条件数决定，即最大特征值与最小特征值之比。

### 1.3.2 Fast Solvers for Differential Equations / 微分方程的快速求解器

Fast direct solvers also exist for solving the matrix system resulting from differential equations. The nested dissection ordering method [82] permits the direct solution of the matrix system in O(N^1.5) operations in 2D and O(N^1.33) operations in 3D [83].
快速直接求解器也可用于求解微分方程产生的矩阵系统。嵌套分割排序法[82]允许在2D中以O(N^1.5)操作、在3D中以O(N^1.33)操作直接求解矩阵系统[83]。

### 1.3.3 Time Domain Differential Equation Solvers / 时域微分方程求解器

In the time domain, finite-difference time-domain (FDTD) method pioneered by Yee [54] discretizes Maxwell's equations directly in space and time. The FDTD method is simple, robust, and handles nonlinear materials naturally.
在时域中，Yee[54]开创的时域有限差分法(FDTD)直接在空间和时间上离散麦克斯韦方程组。FDTD方法简单、鲁棒，且自然处理非线性材料。

---

## 1.4 Integral Equation Solvers / 积分方程求解器

The integral equation of scattering can be derived using the Green's function. For electromagnetics, the integral equation is called the Stratton-Chu integral equation [92].
散射的积分方程可以利用格林函数推导。对于电磁学，该积分方程称为Stratton-Chu积分方程[92]。

### 1.4.1 Surface Integral Equations / 表面积分方程

Given two equations / 给定两个方程：

$$
(\nabla^2 + k^2) \phi_1(r) = Q(r) \tag{1.13}
$$

$$
(\nabla^2 + k^2) g_1(r, r') = -\delta(r - r') \tag{1.14}
$$

Using Green's theorem, the surface integral equation is obtained / 利用格林定理，得到表面积分方程：

$$
\phi_1(r) = \phi_{\text{inc}}(r) - \int dS' [g_1(r, r') \partial_{n'} \phi_1(r') - \phi_1(r') \partial_{n'} g_1(r, r')], \quad r \in V_1 \tag{1.18}
$$

### 1.4.2 Magnetic Field Integral Equation (MFIE) / 磁场积分方程

For impenetrable scatterers with PEC boundary condition, the electric field integral equation (EFIE) and the magnetic field integral equation (MFIE) can be derived. The combined field integral equation (CFIE) is often used to avoid internal resonances.
对于具有PEC边界条件的不可穿透散射体，可以推导出电场积分方程(EFIE)和磁场积分方程(MFIE)。通常使用组合场积分方程(CFIE)来避免内部谐振。

### 1.4.3 Numerical Solution of Integral Equations / 积分方程的数值求解

The method of moments (MoM) converts the integral equation into a dense matrix equation of the form $\mathbf{Z} \cdot \mathbf{J} = \mathbf{V}$, where $\mathbf{Z}$ is the impedance matrix, $\mathbf{J}$ is the unknown current vector, and $\mathbf{V}$ is the excitation vector. Traditional MoM requires O(N²) memory and O(N²) or O(N³) time to solve.
矩量法(MoM)将积分方程转换为稠密矩阵方程，形式为 $\mathbf{Z} \cdot \mathbf{J} = \mathbf{V}$，其中 $\mathbf{Z}$ 为阻抗矩阵，$\mathbf{J}$ 为未知电流矢量，$\mathbf{V}$ 为激励矢量。传统MoM需要O(N²)内存和O(N²)或O(N³)时间来求解。

### 1.4.4 Fast Solvers for Integral Equations / 积分方程的快速求解器

Fast solvers reduce the complexity of the matrix-vector product to O(N log N) or O(N). These include:
快速求解器将矩阵-矢量乘积的复杂度降低到O(N log N)或O(N)。这些包括：

- Fast multipole method (FMM) / 快速多极子方法
- Multilevel fast multipole algorithm (MLFMA) / 多层快速多极子算法
- Adaptive integral method (AIM) / 自适应积分方法
- Precorrected-FFT (pFFT) / 预校正FFT
- FFT-based methods for Toeplitz-like matrices / 基于FFT的Toeplitz类矩阵方法

---

## 1.5 A Simplified View of the Multilevel Fast Multipole Algorithm / 多层快速多极子算法的简化视图

When solving an integral equation of scattering, the pertinent equation is / 求解散射积分方程时，相关方程为：

$$
\phi_{\text{inc}}(r) = \int dS' g(r, r') j(r') \tag{1.52}
$$

The Green's function is not a local function, but a function that connects two points irrespective of their separation. Therefore, all the current sources on the scatterer cooperate with each other to produce a field that cancels the incident field inside the scatterer.
格林函数不是局部函数，而是连接两点的函数，无论它们的距离如何。因此，散射体上的所有电流源相互协作产生一个场，以抵消散射体内的入射场。

In a numerical discretization, the current is described by discrete elements on the surface of the scatterer. The cooperative behavior of the current elements can be likened to a telephone network consisting of N telephones where each telephone is connected to every other telephone by direct wire connections. This requires O(N²) telephone lines.
在数值离散中，电流由散射体表面上的离散元描述。电流元的协作行为可以类比为N部电话组成的电话网络，每部电话通过直接线路连接至其他每部电话。这需要O(N²)条电话线。

However, the telephone company knows better. The number of telephone lines needed to connect N telephones can be greatly reduced using the hub system. Telephones are first divided into groups according to their proximity, and those within the same group are connected to a single hub. Then, wires are used to connect the hubs together.
然而，电话公司更明智。连接N部电话所需的电话线数量可通过枢纽系统大大减少。电话首先按其邻近度分组，同组电话连接至一个枢纽，然后使用线路将各枢纽连接起来。

In terms of matrix elements, factorizing the Green's function yields / 就矩阵元素而言，因式分解格林函数得到：

$$
A_{ij} = \mathbf{V}_{il}^t \cdot \mathbf{T}_{ll'} \cdot \mathbf{V}_{l'j} \tag{1.53}
$$

where $\mathbf{V}_{l'j}$ aggregates radiation from sources in group $l'$ to the hub, $\mathbf{T}_{ll'}$ translates between hubs, and $\mathbf{V}_{il}^t$ disaggregates to the observer.
其中 $\mathbf{V}_{l'j}$ 将组 $l'$ 中源的辐射聚合到枢纽，$\mathbf{T}_{ll'}$ 在枢纽之间传输，$\mathbf{V}_{il}^t$ 将信息分发到观察点。

A matrix-vector product is replaced by / 矩阵-矢量乘积被替换为：

$$
\sum_j A_{ij} x_j = \mathbf{V}_{il}^t \cdot \sum_{l'} \mathbf{T}_{ll'} \cdot \sum_{j \in G_{l'}} \mathbf{V}_{l'j} x_j \tag{1.54}
$$

If $\mathbf{T}_{ll'}$ is made diagonal, the information transmission between groups becomes efficient. The diagonal factorization of the Green's function for the Helmholtz problem was first achieved by Rokhlin in 1990 [107].
如果 $\mathbf{T}_{ll'}$ 是对角化的，组间的信息传输就变得高效。亥姆霍兹问题格林函数的对角因子分解由Rokhlin于1990年首次实现[107]。

This idea can be extended to multilevel / 这个想法可以扩展到多层：

$$
A_{ij} = \mathbf{V}_{il_1}^t \cdot \beta_{l_1 l_2} \cdots \beta_{l_{L-1} l_L} \cdot \mathbf{T}_{l_L, l_L'} \cdot \beta_{l_{L-1}'} \cdots \beta_{l_1'} \cdot \mathbf{V}_{l_1' j} \tag{1.55}
$$

Interpolation and anterpolation operators have to be added between levels to arrive at an O(N log N) fast matrix-vector product [111,112].
在层之间需要添加插值和反插值算子，以实现O(N log N)的快速矩阵-矢量乘积[111,112]。

---

## 1.6 Conclusion / 结论

This book documents recent advances in fast and efficient methods in computational electromagnetics. There are methods for both differential equation solvers as well as integral equation solvers. Methods for both frequency and time domain will be presented. Hybridization methods will be discussed, as well as methods to solve Maxwell's equations stably from static to microwave frequencies.
本书记录了计算电磁学中快速高效方法的最新进展。涵盖了微分方程求解器和积分方程求解器的方法，将介绍频域和时域两种方法，讨论混合方法以及从静态到微波频率稳定求解麦克斯韦方程组的方法。

Despite the voluminous amount of work presented here, we believe that much work still needs to be done in computational electromagnetics so that some day, it will provide the same confidence level in electromagnetic simulation as circuit theory has provided in the microchip industry.
尽管本书呈现了大量工作，但我们相信计算电磁学仍有大量工作要做，以期有朝一日它能为电磁仿真提供如电路理论在微芯片行业中所提供的同等信任水平。

---

## References / 参考文献

[1] P. M. Harman (ed.), *The Scientific Letters and Papers of James Clerk Maxwell*, Vol. II, 1862-1873, Cambridge, U.K.: Cambridge University Press, 1995.
[3] G. Mie, "Beiträge zur optik trüber medien speziel kolloidaler metallösungen," *Ann. Phys.*, vol. 25, pp. 377–445, 1908.
[5] Lord Rayleigh, "On the passage of electric waves through tubes, or the vibrations of dielectric cylinders," *Phil. Mag.*, vol. 43, pp. 125–132, 1897.
[6] A. Sommerfeld, "Mathematische theorie der diffraction," *Math. Ann.*, vol. 47, pp. 317–374, 1896.
[7] A. Sommerfeld, "Über die ausbreitung der wellen in der drahtlosen telegraphie," *Ann. Phys.*, vol. 28, pp. 665–737, 1909.
[24] R. F. Harrington, *Field Computation by Moment Methods*, Macmillan, 1968.
[105] V. Rokhlin, "Rapid solution of integral equations of classical potential theory," *J. Comput. Phys.*, vol. 60, pp. 187–207, 1985.
[107] V. Rokhlin, "Rapid solution of integral equations of scattering theory in two dimensions," *J. Comput. Phys.*, vol. 86, pp. 414–439, 1990.
[146] J. J. H. Wang, *Generalized Moment Methods in Electromagnetics*, Wiley, 1991.
[147] E. K. Miller, L. Medgyesi-Mitschang, and E. H. Newman (eds.), *Computational Electromagnetics: Frequency-Domain Method of Moments*, IEEE Press, 1992.
[148] J. L. Volakis, A. Chatterjee, and L. C. Kempel, *Finite Element Method for Electromagnetics*, IEEE Press, 1998.
[149] T. Itoh (ed.), *Numerical Techniques for Microwave and Millimeter-Wave Passive Structures*, Wiley, 1989.
[150] M. N. O. Sadiku, *Numerical Techniques in Electromagnetics*, CRC Press, 1992.
[151] A. F. Peterson, S. L. Ray, and R. Mittra, *Computational Methods for Electromagnetics*, IEEE Press, 1998.

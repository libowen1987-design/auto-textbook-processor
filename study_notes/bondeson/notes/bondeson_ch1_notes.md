# Bondeson《Computational Electromagnetics》第1章
> **中英双语版**

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 20-28 of 231 (231 total)

---

## Introduction | 引言

### 1 Introduction

Computational electromagnetics (CEM) deals with numerical tools developed for electromagnetics problems.
> 计算电磁学（CEM）研究用于电磁问题的数值工具。

CEM allows for a faster and cheaper design process, where the use of expensive and time-consuming prototypes is minimized.
> CEM 能够实现更快、更廉价的设计流程，最大限度地减少昂贵且耗时的原型制作。

These tools can also provide crucial information and understanding of a device's electromagnetic operation, which may be difficult or even impossible to achieve by means of experiments or analytical calculations.
> 这些工具还能提供有关设备电磁工作的关键信息和理解，而这些信息可能难以甚至无法通过实验或解析计算获得。

Automation of computations allows for extensive parametric studies.
> 计算的自动化允许进行广泛的参数化研究。

It is only relatively recently that optimization by computation has been used for electromagnetic design problems.
> 直到最近，计算优化才开始应用于电磁设计问题。

In times of a rapid pace of development, analysis and optimization of electromagnetic devices by CEM tools may be crucial for maintaining competitiveness.
> 在快速发展的时代，通过 CEM 工具对电磁设备进行分析和优化对于保持竞争力至关重要。

Today, there is a broad selection of commercially available computer programs that provide implementations of popular and powerful CEM algorithms.
> 如今，市场上有大量商业计算机程序提供流行且强大的 CEM 算法实现。

These programs can handle many engineering and research problems.
> 这些程序可以处理许多工程和研究问题。

However, a well-informed choice and correct use of software for reliable results and conclusions require good knowledge of CEM.
> 然而，要做出明智的选择并正确使用软件以获得可靠的结果和结论，需要扎实的 CEM 知识。

Furthermore, problems that extend beyond the applicability of commercially available software packages demand modifications or additions that again rely on a good command of CEM.
> 此外，超出商业软件包适用范围的问题需要修改或补充，这同样依赖对 CEM 的熟练掌握。

---

#### 1.1 Computational Electromagnetics | 计算电磁学

CEM is a young discipline.
> CEM 是一门年轻的学科。

It is still growing, in response to the steadily increasing demand for software for the design and analysis of electrical devices.
> 它仍在发展，以响应电气设备设计和分析软件需求的稳步增长。

Ten years ago, most electrical devices were designed by building and testing prototypes, a process that is both costly and slow.
> 十年前，大多数电气设备是通过制作和测试原型来设计的，这一过程既昂贵又缓慢。

Today the design can be made faster and cheaper by means of numerical computation.
> 如今，通过数值计算，设计可以变得更快、更便宜。

CEM has become a main design tool in both industrial and academic research.
> CEM 已成为工业界和学术界的主要设计工具。

There are numerous application areas for CEM, and here we mention a few.
> CEM 的应用领域众多，以下列举几个。

In electric power engineering, computation is well established for the analysis and design of electrical machines, generators, transformers, and shields.
> 在电力工程领域，计算已广泛应用于电机、发电机、变压器和屏蔽体的分析与设计。

In applications to microwaves, CEM is a more recent tool, but it is now used for designing microwave networks and antennas, and even microwave ovens.
> 在微波应用中，CEM 是一种较新的工具，但现在已用于设计微波网络、天线甚至微波炉。

The analysis and optimization of radar cross sections (RCS) for stealth devices has been the driving force for the development of many new techniques in CEM.
> 隐身设备雷达散射截面（RCS）的分析与优化一直是 CEM 许多新技术发展的驱动力。

The clock frequencies of modern microprocessors are approaching the region where circuits occupy a large fraction of a wavelength.
> 现代微处理器的时钟频率已接近电路占据波长的很大一部分的区域。

Then ordinary circuit theory no longer applies and it may be necessary to solve Maxwell's equations to design smaller and faster processors.
> 此时普通电路理论不再适用，可能需要求解 Maxwell 方程组来设计更小、更快的处理器。

The increased demand for electromagnetic compatibility (EMC) also poses new computational problems.
> 对电磁兼容性（EMC）日益增长的需求也带来了新的计算问题。

The performance of CEM tools is increasing rapidly.
> CEM 工具的性能正在快速提升。

One reason for this is the steady growth of computer capacity over half a century.
> 原因之一是半个多世纪以来计算机容量的稳步增长。

Another equally important reason is improvements in algorithms.
> 另一个同等重要的原因是算法的改进。

The purpose of this book is to give an introduction to the most frequently used algorithms in CEM.
> 本书的目的是介绍 CEM 中最常用的算法。

The most common approaches in CEM are finite differences (FD) (usually in the time domain), the finite element method (FEM), and the boundary element method (BEM), which is usually referred to, for historical reasons, as the method of moments (MoM).
> CEM 中最常见的方法是有限差分法（FD，通常在时域）、有限元法（FEM）和边界元法（BEM），后者出于历史原因通常称为矩量法（MoM）。

Finite difference methods are more or less straightforward discretizations of Maxwell's equations in differential form, using the field components, or the potentials, on a structured grid of points as unknowns.
> 有限差分法是对微分形式 Maxwell 方程组的直接离散化，使用结构化网格点上的场分量或势作为未知量。

Finite differences in general, and the finite-difference time-domain (FDTD) method in particular, are very efficient and require few operations per grid point.
> 有限差分法总体上，特别是时域有限差分法（FDTD），效率非常高，每个网格点的运算量很少。

The FDTD is one of the most widespread methods in CEM, and it can be applied to a large variety of microwave problems.
> FDTD 是 CEM 中最广泛使用的方法之一，可应用于各种微波问题。

One drawback of finite difference methods is that they work well only on uniform Cartesian (structured) grids, and typically use the so-called staircase approximation of boundaries not aligned with the grid.
> 有限差分法的一个缺点是它们只能在均匀的笛卡尔（结构化）网格上表现良好，并且通常对未与网格对齐的边界采用所谓的阶梯近似。

Finite element methods in which the computational region is divided into unstructured grids (typically triangles in two dimensions and tetrahedra in three dimensions) can approximate complex boundaries much better, but are considerably slower in time-domain calculations.
> 有限元法将计算区域划分为非结构化网格（二维通常为三角形，三维通常为四面体），可以更好地逼近复杂边界，但在时域计算中速度慢得多。

The FEM is mainly used for time-harmonic problems, and it is the standard method for eddy current calculations.
> FEM 主要用于时谐问题，是涡流计算的标准方法。

The MoM discretizes Maxwell's equations in integral form, and the unknowns are sources such as currents or charges on the surfaces of conductors and dielectrics.
> MoM 对积分形式的 Maxwell 方程组进行离散化，未知量是导体和介质表面的电流或电荷等源量。

This method is advantageous for problems involving open regions, and when the current-carrying surfaces are small.
> 该方法适用于涉及开放区域的问题，以及载流表面较小的情况。

The MoM is often applied to scattering problems.
> MoM 通常应用于散射问题。

We will discuss how the three types of methods, FD, FEM, and MoM, can be applied to different electromagnetics problems, in both the time domain and the frequency domain (time-harmonic fields and currents).
> 我们将讨论 FD、FEM 和 MoM 这三种方法如何应用于不同的电磁问题，包括时域和频域（时谐场和电流）。

Some other methods will be mentioned in Chapter 8.
> 其他一些方法将在第 8 章中提及。

---

#### 1.2 Maxwell's Equations | Maxwell 方程组

Before discussing how to solve electromagnetics problems, we will first write down Maxwell's equations in the form in which they can be found in most textbooks on electromagnetics, see e.g. [18, 30, 4].
> 在讨论如何求解电磁问题之前，我们首先写出大多数电磁学教科书中出现的 Maxwell 方程组形式。

They are usually stated as:

**Ampère's law | 安培定律**

$$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}, \tag{1.1}$$

**Faraday's law | 法拉第定律**

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}, \tag{1.2}$$

**Poisson's equation | 泊松方程**

$$\nabla \cdot \mathbf{D} = \rho, \tag{1.3}$$

**and the condition of solenoidal magnetic flux density | 磁通密度无散条件**

$$\nabla \cdot \mathbf{B} = 0. \tag{1.4}$$

Here $\mathbf{H}$ is the magnetic field, $\mathbf{J}$ is the current density, $\mathbf{D}$ is the electric displacement, $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic flux density, $\rho$ is the electric charge density, and $t$ denotes the time variable.
> 其中 $\mathbf{H}$ 为磁场强度，$\mathbf{J}$ 为电流密度，$\mathbf{D}$ 为电位移矢量，$\mathbf{E}$ 为电场强度，$\mathbf{B}$ 为磁通密度，$\rho$ 为电荷密度，$t$ 为时间变量。

Moreover, we have

$$\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M}), \qquad \mathbf{D} = \epsilon_0 \mathbf{E} + \mathbf{P},$$

where $\mu_0 = 4\pi \cdot 10^{-7}$ Vs/Am is the free-space magnetic permeability, $\epsilon_0 = 1/(c_0^2 \mu_0) \approx 8.854 \cdot 10^{-12}$ As/Vm is the free-space electric permittivity, $\mathbf{M}$ is the magnetization and $\mathbf{P}$ is the polarization.
> 其中 $\mu_0 = 4\pi \cdot 10^{-7}$ Vs/Am 为真空磁导率，$\epsilon_0 = 1/(c_0^2 \mu_0) \approx 8.854 \cdot 10^{-12}$ As/Vm 为真空介电常数，$\mathbf{M}$ 为磁化强度，$\mathbf{P}$ 为极化强度。

In vacuum, the speed of light is $c_0 = 299\,792\,458$ m/s.
> 真空中光速为 $c_0 = 299\,792\,458$ m/s。

In this book, we will restrict attention to linear, isotropic and nondispersive materials for which the constitutive relations

$$\mathbf{B} = \mu \mathbf{H}, \qquad \mathbf{D} = \epsilon \mathbf{E}$$

hold with frequency-independent electric permittivity $\epsilon$ and magnetic permeability $\mu$.
> 本书将局限于线性、各向同性和非色散材料，其本构关系中的介电常数 $\epsilon$ 和磁导率 $\mu$ 与频率无关。

The permittivity is often written as $\epsilon = \epsilon_0 \epsilon_r$, where $\epsilon_r$ is called the relative permittivity.
> 介电常数通常写为 $\epsilon = \epsilon_0 \epsilon_r$，其中 $\epsilon_r$ 称为相对介电常数。

Similarly, the permeability is often written $\mu = \mu_0 \mu_r$ where $\mu_r$ is called the relative permeability.
> 类似地，磁导率写为 $\mu = \mu_0 \mu_r$，其中 $\mu_r$ 称为相对磁导率。

For electrically conductive materials, an electric field causes a current density

$$\mathbf{J} = \sigma \mathbf{E}$$

where $\sigma$ is the electric conductivity.
> 对于导电材料，电场引起电流密度 $\mathbf{J} = \sigma \mathbf{E}$，其中 $\sigma$ 为电导率。

---

##### 1.2.1 Boundary Conditions | 边界条件

Consider the situation in which one medium, characterized by $\epsilon_1$ and $\mu_1$, shares an interface with another medium, characterized by $\epsilon_2$ and $\mu_2$.
> 考虑一个以 $\epsilon_1$ 和 $\mu_1$ 表征的介质与另一个以 $\epsilon_2$ 和 $\mu_2$ 表征的介质共享界面的情形。

We use the subindices 1 and 2 to denote quantities that are associated with media 1 and 2, respectively.
> 我们使用下标 1 和 2 分别表示与介质 1 和介质 2 相关的量。

At the interface, the tangential and normal fields must satisfy so-called boundary conditions, which are consequences of Maxwell's equations.
> 在界面处，切向和法向场必须满足所谓的边界条件，这些条件是 Maxwell 方程组的推论。

For example, (1.4) states the condition of solenoidal magnetic flux density, and Gauss's theorem

$$\int_V \nabla \cdot \mathbf{B} \, dV = \oint_{\partial V} \mathbf{B} \cdot \hat{n} \, dS, \tag{1.5}$$

where $\partial V$ is the surface enclosing the volume $V$, applied to this conservation law yields the boundary condition

$$\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0,$$

where $\hat{n}$ is a unit normal to the interface that points into medium 2.
> 其中 $\partial V$ 为包围体积 $V$ 的曲面，将此守恒律应用于高斯定理得到边界条件 $\hat{n} \cdot (\mathbf{B}_2 - \mathbf{B}_1) = 0$，其中 $\hat{n}$ 为指向介质 2 的界面单位法向量。

Similarly, Poisson's equation (1.3) gives

$$\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s,$$

where $\rho_s$ is the surface charge density on the interface.
> 类似地，泊松方程 (1.3) 给出 $\hat{n} \cdot (\mathbf{D}_2 - \mathbf{D}_1) = \rho_s$，其中 $\rho_s$ 为界面上的面电荷密度。

Stokes's theorem

$$\int_S (\nabla \times \mathbf{E}) \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{E} \cdot d\mathbf{l}, \tag{1.6}$$

where $\partial S$ is the curve enclosing the surface $S$, applied to Faraday's law (1.2) yields

$$\hat{n} \times (\mathbf{E}_2 - \mathbf{E}_1) = 0$$

and, analogously, Ampère's law (1.1) gives

$$\hat{n} \times (\mathbf{H}_2 - \mathbf{H}_1) = \mathbf{J}_s,$$

where $\mathbf{J}_s$ is the surface current on the interface between the two media.
> 其中 $\mathbf{J}_s$ 为两种介质界面上的面电流。

The electric field inside a perfect electric conductor (PEC) is zero and, consequently, also the electric displacement.
> 理想电导体（PEC）内部的电场为零，电位移矢量也为零。

We get the boundary conditions $\hat{n} \cdot \mathbf{D}_2 = \rho_s$ and $\hat{n} \times \mathbf{E}_2 = 0$ when medium 1 is a PEC.
> 当介质 1 为 PEC 时，得到边界条件 $\hat{n} \cdot \mathbf{D}_2 = \rho_s$ 和 $\hat{n} \times \mathbf{E}_2 = 0$。

At finite frequencies, Faraday's law yields that the magnetic flux density is zero inside a PEC (which also applies to the magnetic field) and we get the boundary conditions $\hat{n} \cdot \mathbf{B}_2 = 0$ and $\hat{n} \times \mathbf{H}_2 = \mathbf{J}_s$ when medium 1 is a PEC.
> 在有限频率下，法拉第定律推出 PEC 内部磁通密度为零（磁场也如此），当介质 1 为 PEC 时得到边界条件 $\hat{n} \cdot \mathbf{B}_2 = 0$ 和 $\hat{n} \times \mathbf{H}_2 = \mathbf{J}_s$。

Another kind of boundary conditions, which do not correspond to any physical boundary, are absorbing boundary conditions (ABC).
> 另一类不对应任何物理边界的边界条件是吸收边界条件（ABC）。

These are used to truncate the computational domain in case of open region problems and can be implemented using a variety of techniques.
> 它们用于在开放区域问题中截断计算域，可以通过多种技术实现。

The most popular ABC is the perfectly matched layer (PML), which will be described in Section 5.3.1.
> 最流行的 ABC 是完全匹配层（PML），将在第 5.3.1 节中描述。

For a more detailed discussion on boundary conditions, the reader is referred to a textbook on electromagnetics; see, e.g., [18, 30, 4].
> 关于边界条件的更详细讨论，请读者参考电磁学教科书，例如 [18, 30, 4]。

---

##### 1.2.2 Energy Relations | 能量关系

For Maxwell's equations, it is useful (and in some cases essential) to regard the energy as being stored in the fields.
> 对于 Maxwell 方程组，将能量视为存储在场中是有用的（在某些情况下是必要的）。

For electrostatics, we have the energy density $w_e = \epsilon |\mathbf{E}|^2 / 2$ and the work to assemble a static charge distribution is

$$W = \frac{1}{2} \int_V \epsilon |\mathbf{E}|^2 \, dV. \tag{1.7}$$

> 对于静电场，能量密度为 $w_e = \epsilon |\mathbf{E}|^2 / 2$，组装静态电荷分布所做的功为 (1.7)。

There are alternative expressions for the evaluation of $W$ in terms of the charge distribution and the electrostatic potential.
> 还有用电荷分布和静电势表示 $W$ 的替代表达式。

In magnetostatics, the corresponding energy density is $w_m = |\mathbf{B}|^2 / (2\mu)$.
> 在静磁场中，相应的能量密度为 $w_m = |\mathbf{B}|^2 / (2\mu)$。

For a time-varying electromagnetic field, we have the energy density $w_e + w_m$ and this quantity is often used to form energy conservation expressions that involve the electromagnetic phenomena.
> 对于时变电磁场，能量密度为 $w_e + w_m$，该量通常用于构建涉及电磁现象的能量守恒表达式。

---

##### 1.2.3 Time Evolution | 时间演化

Before discussing schemes for evolving Maxwell's equations (1.1)–(1.4) in time, we must note that they are not all independent.
> 在讨论 Maxwell 方程组 (1.1)–(1.4) 的时间演化方案之前，我们必须注意到它们并非都是独立的。

For example, Poisson's equation (1.3) is best viewed as an initial condition for the charge density.
> 例如，泊松方程 (1.3) 最好视为电荷密度的初始条件。

To see this, take the divergence of Ampère's law, which gives

$$\frac{\partial}{\partial t} \nabla \cdot \mathbf{D} + \nabla \cdot \mathbf{J} = 0. \tag{1.8}$$

> 为说明这一点，对安培定律取散度，得到 (1.8)。

Replacing $\nabla \cdot \mathbf{J}$ from the equation of continuity for electric charge

$$\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0,$$

we see that the divergence of Ampère's law (1.8) is the time derivative of Poisson's equation $\nabla \cdot \mathbf{D} = \rho$.
> 用电荷连续性方程替换 $\nabla \cdot \mathbf{J}$，可见安培定律的散度 (1.8) 正是泊松方程 $\nabla \cdot \mathbf{D} = \rho$ 的时间导数。

Therefore, if the initial fields satisfy Poisson's equation, time advancement of Ampère's law together with the conservation of charge will ensure that Poisson's equation holds at later times.
> 因此，如果初始场满足泊松方程，安培定律的时间推进与电荷守恒将确保泊松方程在以后的时间成立。

Similarly, the divergence of Faraday's law shows that the time derivative of $\nabla \cdot \mathbf{B}$ vanishes, so $\nabla \cdot \mathbf{B} = 0$ need only be given as an initial condition.
> 类似地，法拉第定律的散度表明 $\nabla \cdot \mathbf{B}$ 的时间导数为零，因此 $\nabla \cdot \mathbf{B} = 0$ 只需作为初始条件给出。

Thus, $\nabla \cdot \mathbf{B} = 0$ can be seen as a restriction on valid initial conditions for Faraday's law.
> 因此，$\nabla \cdot \mathbf{B} = 0$ 可视为法拉第定律有效初始条件的限制。

We conclude that the time evolution of the fields is completely specified by

$$\epsilon \frac{\partial \mathbf{E}}{\partial t} = \nabla \times \mathbf{H} - \mathbf{J}, \tag{1.9}$$

$$\mu \frac{\partial \mathbf{H}}{\partial t} = -\nabla \times \mathbf{E}. \tag{1.10}$$

> 我们得出结论：场的完整时间演化由 (1.9) 和 (1.10) 完全确定。

This form is used in the FDTD method to advance $\mathbf{E}$ and $\mathbf{H}$ in time, as will be described in Chapter 5.
> 这种形式用于 FDTD 方法中随时间推进 $\mathbf{E}$ 和 $\mathbf{H}$，将在第 5 章中描述。

The initial conditions for this set of equations are the electric and magnetic fields $\mathbf{E}$ and $\mathbf{H}$, and they must satisfy (1.3) and (1.4).
> 这组方程的初始条件是电场 $\mathbf{E}$ 和磁场 $\mathbf{H}$，它们必须满足 (1.3) 和 (1.4)。

The system of two first-order equations can be combined to a single second-order equation for $\mathbf{E}$:

$$\epsilon \frac{\partial^2 \mathbf{E}}{\partial t^2} + \nabla \times \frac{1}{\mu} \nabla \times \mathbf{E} = -\frac{\partial \mathbf{J}}{\partial t}, \tag{1.11}$$

> 两个一阶方程的系统可以合并为一个关于 $\mathbf{E}$ 的二阶方程 (1.11)。

which is often referred to as the curl-curl equation or the vector wave equation.
> 这通常称为旋度-旋度方程或矢量波动方程。

We will use Maxwell's equations in this form in Chapter 6 on the FEM.
> 我们将在第 6 章关于 FEM 的内容中使用这种形式的 Maxwell 方程组。

The initial conditions that need to be specified for (1.11) are the electric field and its time derivative.
> 需要为 (1.11) 指定的初始条件是电场及其时间导数。

In particular, FEM is generally used to solve the frequency domain form of the curl-curl equation, sometimes referred to as the vector Helmholtz equation, where $\exp(j\omega t)$ time dependence is assumed, so that the time derivative $\partial/\partial t$ is replaced by $j\omega$, where $j$ is the imaginary unit and $\omega$ is the angular frequency.
> 特别地，FEM 通常用于求解频域形式的旋度-旋度方程，有时称为矢量亥姆霍兹方程，其中假设 $\exp(j\omega t)$ 时间依赖关系，时间导数 $\partial/\partial t$ 替换为 $j\omega$，这里 $j$ 为虚数单位，$\omega$ 为角频率。

The full Maxwell equations (1.9)–(1.10) or (1.11) are commonly used for microwave problems, such as antennas and microwave circuits.
> 完整的 Maxwell 方程组 (1.9)–(1.10) 或 (1.11) 通常用于天线和微波电路等微波问题。

One of the difficulties one has to face in solving these equations is that the computational domain may extend over many wavelengths in all three coordinate directions, and that consequently the required number of unknowns needed for an accurate computation may be very large.
> 求解这些方程面临的一个困难是计算域可能在所有三个坐标方向上延伸多个波长，因此精确计算所需的未知量数量可能非常庞大。

To complicate matters, one may have to deal with complex three-dimensional (3D) geometry, including details, such as wires, that are much smaller than a wavelength.
> 更复杂的是，可能需要处理复杂的三维（3D）几何形状，包括比波长小得多的细节，如导线。

Moreover, microwave problems often involve open regions, and to model this, the computational domain has to be truncated by means of absorbing boundary conditions.
> 此外，微波问题通常涉及开放区域，为对其进行建模，必须通过吸收边界条件截断计算域。

---

##### 1.2.4 Dispersion Relation and Wave Velocities | 色散关系与波速

The propagation of electromagnetic waves is often characterized in terms of the dispersion relation, which relates spatial and temporal variation of a monochromatic solution by means of its wavevector $\mathbf{k}$ and frequency $\omega$, respectively.
> 电磁波的传播通常以色散关系来表征，该关系通过波矢 $\mathbf{k}$ 和频率 $\omega$ 将单色解的空间和时间变化联系起来。

Often, we deal with nondispersive situations where the frequency is directly proportional to the wavenumber $k$.
> 通常，我们处理的是非色散情况，其中频率与波数 $k$ 成正比。

When the frequency is not proportional to the wavenumber, we have dispersion and this occurs physically for wave propagation in some media and waveguides.
> 当频率与波数不成正比时，就产生了色散，这在某些介质和波导中的波传播中物理存在。

However, the discretization process may also cause dispersion, which is often referred to as numerical dispersion.
> 然而，离散化过程也可能引起色散，这通常称为数值色散。

In general, dispersion implies that a wave packet containing several different spatial frequencies will change shape as it propagates.
> 一般来说，色散意味着包含多个不同空间频率的波包在传播过程中会改变形状。

Naturally, it is important that the numerical dispersion is small in comparison to the physical dispersion of interest.
> 自然地，数值色散相比所关注的物理色散应该很小。

To provide a brief introduction to dispersion and related issues, we use (1.11) to deduce the corresponding 1D wave equation:

$$\frac{\partial^2}{\partial t^2} E(z, t) = c^2 \frac{\partial^2}{\partial z^2} E(z, t), \tag{1.12}$$

> 为了简要介绍色散及其相关问题，我们使用 (1.11) 推导相应的一维波动方程 (1.12)。

where the transverse electric field is denoted $E(z, t)$.
> 其中横向电场记为 $E(z, t)$。

Here, the speed of light $c$ in the medium is constant.
> 这里介质中的光速 $c$ 为常数。

The exact solutions of (1.12) on an infinite interval have the form

$$E(z, t) = E_+(z - c t) + E_-(z + c t), \tag{1.13}$$

> (1.12) 在无限区间上的精确解的形式为 (1.13)。

where $E_+$ and $E_-$ represent waves traveling in the positive and negative $z$-directions, respectively.
> 其中 $E_+$ 和 $E_-$ 分别表示沿 $z$ 正方向和负方向传播的波。

This solution typically involves a range of frequencies and, next, we consider one of these, i.e. the monochromatic case.
> 该解通常涉及一个频率范围，接下来我们考虑其中之一，即单色情况。

To obtain the dispersion relation for the 1D wave equation, we substitute $E = \exp(j\omega t - jkz)$ in (1.12), and then divide both sides by $\exp(j\omega t - jkz)$, which gives $\omega^2 = c^2 k^2$.
> 为得到一维波动方程的色散关系，将 $E = \exp(j\omega t - jkz)$ 代入 (1.12)，然后两边同除以 $\exp(j\omega t - jkz)$，得到 $\omega^2 = c^2 k^2$。

Consequently, the dispersion relation for the 1D wave equation is

$$\omega = c k. \tag{1.14}$$

> 因此，一维波动方程的色散关系为 $\omega = c k$。

The angular frequency $\omega$ is a linear function of the wavenumber $k$ and this implies that all frequency components of a transient wave propagate with the same velocity.
> 角频率 $\omega$ 是波数 $k$ 的线性函数，这意味着瞬态波的所有频率分量以相同的速度传播。

The phase velocity $v_p$, defined as the velocity of a constant phase surface, satisfies $(d/dt)(\omega t - k z) = \omega - k v_p = 0$, which gives

$$v_p = \frac{\omega}{k}. \tag{1.15}$$

> 相速度 $v_p$ 定义为恒定相位面的速度，满足上述关系，得到 $v_p = \omega/k$。

Next, we consider the superposition of the two signals $E_A = \exp[j(\omega - \Delta\omega)t - j(k - \Delta k)z]$ and $E_B = \exp[j(\omega + \Delta\omega)t - j(k + \Delta k)z]$.
> 接下来，我们考虑两个信号 $E_A$ 和 $E_B$ 的叠加。

The sum wave $E_A + E_B$ can be written as a carrier wave $\exp(j\omega t - jkz)$ times a slowly varying envelope which is $2\cos(t \Delta\omega - z \Delta k)$.
> 合成波 $E_A + E_B$ 可以写为载波 $\exp(j\omega t - jkz)$ 乘以慢变包络 $2\cos(t \Delta\omega - z \Delta k)$。

We see that the propagation speed of the envelope is $\Delta\omega/\Delta k$ and, in the limit where $\Delta\omega$ and $\Delta k$ become small, this is called the group velocity

$$v_g = \frac{\partial \omega}{\partial k}. \tag{1.16}$$

> 我们看到包络的传播速度为 $\Delta\omega/\Delta k$，在 $\Delta\omega$ 和 $\Delta k$ 趋于零的极限下，这就是群速度 $v_g = \partial \omega/\partial k$。

The envelope can be identified with a wave-packet and, if an energy density is associated with the magnitude of the wave, the transportation of energy occurs with the group velocity.
> 包络可视为波包，如果将能量密度与波的幅度关联起来，则能量的传输以群速度进行。

For the wave equation (1.12), both the phase and group velocities are constant and equal to the speed of light $v_p = v_g = c$.
> 对于波动方程 (1.12)，相速度和群速度都是常数，且等于光速 $v_p = v_g = c$。

This is also evident from the explicit solution (1.13).
> 这从显式解 (1.13) 中也很明显。

Given this analytical treatment, all waves propagate with the same speed, independent of their wavenumber $k$.
> 根据这一解析处理，所有波以相同速度传播，与波数 $k$ 无关。

Therefore we say that there is no dispersion.
> 因此我们说没有色散。

However, a numerical treatment of (1.12) will, in almost all cases, suffer from numerical dispersion and this is discussed in Chapters 3, 4, and 5.
> 然而，(1.12) 的数值处理在几乎所有情况下都会遭受数值色散的影响，这将在第 3、4 和 5 章中讨论。

---

##### 1.2.5 Low-Frequency Approximation | 低频近似

A special case of (1.11) is the "low-frequency approximation," used for instance for electrical machines, generators, and transformers.
> (1.11) 的一个特殊情况是"低频近似"，用于电机、发电机和变压器等。

The low-frequency approximation consists in setting $\epsilon_0 = 0$, that is, one neglects the displacement current in (1.11):

$$\nabla \times \frac{1}{\mu} \nabla \times \mathbf{E} + \sigma \frac{\partial \mathbf{E}}{\partial t} = -\frac{\partial \mathbf{J}_{\text{external}}}{\partial t} \tag{1.17}$$

> 低频近似设 $\epsilon_0 = 0$，即忽略 (1.11) 中的位移电流，得到 (1.17)。

where the electrical current density was taken as $\mathbf{J} = \sigma \mathbf{E} + \mathbf{J}_{\text{external}}$, and $\sigma$ is the electrical conductivity.
> 其中电流密度取为 $\mathbf{J} = \sigma \mathbf{E} + \mathbf{J}_{\text{external}}$，$\sigma$ 为电导率。

The low-frequency approximation gets rid of the electromagnetic waves present in the full Maxwell equations (1.9)–(1.10) and makes it possible to take time steps on the much longer time scale associated with the penetration of eddy currents in conductors.
> 低频近似消除了完整 Maxwell 方程组 (1.9)–(1.10) 中的电磁波，使得可以采用与导体中涡流穿透相关的更长的时间尺度进行时间步进。

However, the low-frequency approximation is mathematically more complicated, because in regions where $\sigma = 0$, the time derivative of $\mathbf{E}$ drops out of (1.17).
> 然而，低频近似在数学上更复杂，因为在 $\sigma = 0$ 的区域，$\mathbf{E}$ 的时间导数从 (1.17) 中消失。

As a consequence, (1.17) gives no information about $\nabla \cdot \mathbf{E}$ in the nonconducting regions, so that $\mathbf{E}$ itself is not actually known.
> 因此，(1.17) 在非导电区域不提供关于 $\nabla \cdot \mathbf{E}$ 的信息，所以 $\mathbf{E}$ 本身实际上未知。

Since the low-frequency equations are important in the area of both electric power engineering and electromagnetic compatibility, we will discuss, briefly, some methods used to solve these equations in Section 6.6.
> 由于低频方程在电力工程和电磁兼容领域都很重要，我们将在第 6.6 节简要讨论求解这些方程的一些方法。

Some challenges that frequently occur in eddy current problems come from extremely complicated 3D geometry and thin layers of currents caused by the skin effect.
> 涡流问题中经常出现的一些挑战来自极其复杂的三维几何形状和由趋肤效应引起的薄电流层。

---

##### 1.2.6 Integral Formulation | 积分形式

A simple special case is electrostatics, where there is no time-dependence.
> 一个简单的特殊情况是静电场，其中没有时间依赖关系。

For static conditions, Faraday's law implies $\nabla \times \mathbf{E} = 0$, so that $\mathbf{E} = -\nabla \varphi$, where $\varphi$ is the electrostatic potential.
> 在静态条件下，法拉第定律推出 $\nabla \times \mathbf{E} = 0$，因此 $\mathbf{E} = -\nabla \varphi$，其中 $\varphi$ 为静电势。

Poisson's equation then becomes

$$\nabla \cdot (\epsilon \nabla \varphi) = -\rho. \tag{1.18}$$

> 泊松方程变为 (1.18)。

The formulations mentioned so far are all differential equations.
> 到目前为止提到的公式都是微分方程。

However, sometimes integral equations are useful.
> 然而，有时积分方程更有用。

In three dimensions, the "solution" to Poisson's equation in free space is

$$\varphi(\mathbf{r}) = \int_{V'} \frac{\rho(\mathbf{r}') \, dV'}{4\pi \epsilon_0 |\mathbf{r} - \mathbf{r}'|}. \tag{1.19}$$

> 在三维情况下，自由空间中泊松方程的"解"为 (1.19)。

This formulation is used in the MoM to solve for the charges on conductors needed to produce specified potential distributions, as discussed in Chapter 7.
> 该公式在 MoM 中用于求解导体上产生指定电位分布所需的电荷，如第 7 章所述。

Similar reformulations in terms of surface integrals exist also for the time-dependent Maxwell system.
> 对于时变 Maxwell 系统，也存在类似的表面积分公式。

The integral equations are called the electric field integral equation (EFIE), the magnetic field integral equation (MFIE), and the combined field integral equation (CFIE).
> 这些积分方程称为电场积分方程（EFIE）、磁场积分方程（MFIE）和组合场积分方程（CFIE）。

We will derive and employ the EFIE for a scattering problem in Chapter 7, which also contains discussions on the MFIE and CFIE.
> 我们将在第 7 章推导 EFIE 并用于散射问题，该章还包含对 MFIE 和 CFIE 的讨论。

---

### Convergence | 收敛性

When using numerical tools, one must keep in mind that they never give the exact answer.
> 使用数值工具时，必须记住它们永远不会给出精确答案。

The accuracy of the numerical result depends on the resolution.
> 数值结果的精度取决于分辨率。

Resolution may mean the number of grid points per wavelength in microwave problems, or how well the geometry of an electrical motor is represented by a finite element mesh.
> 在微波问题中，分辨率可能意味着每波长的网格点数，或者电机几何形状被有限元网格表示的精细程度。

If the method works correctly, the computed answer will converge to the exact result as the resolution increases.
> 如果方法正确工作，随着分辨率的提高，计算答案将收敛到精确结果。

However, with finite resolution, the error is nonzero, and one must estimate it to ensure that its magnitude is acceptable.
> 然而，在有限分辨率下，误差非零，必须对其进行估计以确保其大小可接受。

This is particularly true for large systems, where it may be hard to resolve details of the geometry or to afford a sufficient number of points per wavelength.
> 对于大型系统尤其如此，因为可能难以解析几何细节或无法承担每波长足够的点数。

Examples of this state of affairs are found in 3D-modeling of electrical motors and generators, large array antennas, and computation of the radar cross sections of aircrafts.
> 这种情况的例子见于电机和发电机的 3D 建模、大型阵列天线以及飞机雷达散射截面的计算。

Applied mathematicians have derived a posteriori error estimates, which can be evaluated after an approximate numerical solution has been computed.
> 应用数学家已经推导出后验误差估计，可以在计算出近似数值解后进行评估。

However, such error estimates are only beginning to be established for Maxwell's equations, and discussion of these would take us far beyond an introductory course.
> 然而，这类误差估计对 Maxwell 方程组才刚刚开始建立，讨论这些会远远超出入门课程的范围。

For further information on this topic, see, e.g., [66, 45].
> 关于该主题的更多信息，请参见 [66, 45]。

Nevertheless, error estimates are useful because they can be exploited for adaptive mesh refinement in regions that give large contributions to the error.
> 尽管如此，误差估计仍然有用，因为它们可用于在误差贡献大的区域进行自适应网格细化。

A simpler method to estimate the error of a given computation is to do a convergence test by increasing the resolution uniformly, finding out the order of convergence, and then extrapolating the computed results to infinite resolution.
> 一种更简单的估计给定计算误差的方法是进行收敛性测试：均匀增加分辨率，找出收敛阶，然后将计算结果外推到无限分辨率。

That is the approach we will follow.
> 这就是我们将采用的方法。

In general, one does not know the order of convergence of a computational method for a given problem a priori.
> 一般来说，预先不知道一种计算方法对于给定问题的收敛阶。

Even though standard centered finite differences or linear finite elements converge with an error of order $h^2$ (where $h$ is the grid spacing or the cell size) for regular problems, singular behavior of the solution decreases the order of convergence in most application problems.
> 尽管标准中心有限差分或线性有限元在常规问题中以 $h^2$ 阶误差收敛（其中 $h$ 为网格间距或单元尺寸），但在大多数应用问题中，解的奇异性会降低收敛阶。

Singularities are introduced by sharp edges and tips of objects such as metallic conductors, dielectrics, and magnetic materials.
> 奇异性由金属导体、介质和磁性材料等物体的尖锐边缘和尖端引入。

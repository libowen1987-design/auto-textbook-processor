# Tsang《Scattering of EM Waves》Chapter 7

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 7

> **第七章：体散射模拟**。本章研究体散射模拟方法，将体散射与辐射传输理论结合，通过Foldy-Lax自洽多次散射方程求解点散射体问题，分析均匀分布和簇状分布的散射特性，并通过蒙特卡洛模拟验证解析结果。**

VOLUME SCATTERING SIMULATIONS

> **第七章：体散射模拟**。本章研究体散射模拟方法，将问题分解为两步：第一步对包含多个散射体的测试体积计算消光系数和相位矩阵（包含相干多次散射效应），第二步将模拟值用于辐射传输方程计算双站和反散射系数。

1 Combining Simulations of Collective Volume Scattering

> **第1节：集体体散射效应模拟与辐射传输理论的结合**

Effects with Radiative Transfer Theory 373
2 Foldy-Lax Self-Consistent Multiple Scattering Equations 376

> **第2节：Foldy-Lax自洽多次散射方程**

2.1 Final Exciting Field and Multiple Scattering Equation 376

> **2.1 最终激发场与多次散射方程**

2.2. Foldy-Lax Equations for Point Scatterers 379

> **2.2 点散射体的Foldy-Lax方程**

2.3 The N-Particle Scattering Amplitude 382

> **2.3 N粒子散射振幅**

3 Analytical Solutions of Point Scatterers 382

> **第3节：点散射体的解析解**

3.1 Phase Function and Extinction Coefficient for Uniformly

> **3.1 均匀分布点散射体的相位函数与消光系数**

Distributed Point Scatterers 382
3.2 Scattering by Collection of Clusters 389

> **3.2 簇状分布散射体的散射**

4 Monte Carlo Simulation Results of Point Scatterers 392

> **第4节：点散射体的蒙特卡洛模拟结果**

References and Additional Readings 401

> **引言**：经典矢量辐射传输理论假设粒子独立散射，基于不同粒子散射的随机相位，当粒子相对位置的随机性大于或相当于波长时成立。但在微波频段，某些植被冠层中相对位置随机性小于波长（如雪中冰粒、植被枝干簇），此时散射体呈集体散射，需考虑这些效应。

In Chapters 4 to 6 we have studied extensively the simulation of rough
surface scattering. In those problems, we have simulated the final results of
bistatic scattering coefficients, backscattering coefficients, and emissivitics.
In this chapter we will perform volume scattering simulations. However,
for volume scattering simulations, there is one more dimension than rough
surface scattering, and it becomes difficult to simulate the final results of
bistatic and backscattering coefficients. Nevertheless, it is still possible to
simulate important features of volume scattering. We decompose the problem
into two steps. In step 1 we perform volume scattering simulation on a test
volume of many scatterers to calculate the extinction coefficients and the
phase matrix. In this step 1, the coherent multiple scattering effects among
the many scatterers that are within the test volume are included. In step
2 the simulated values of extinction coefficients and phase matrix elements
are used in radiative transfer equation to calculate the bistatic scattering
coefficients, backscattering coefficients, and emissivities.
> 第4-6章已详细研究粗糙面散射模拟。本章将进行体散射模拟。体散射多了一个维度，直接模拟双站/反散射系数困难，故分解为两步：第一步对包含许多散射体的测试体积计算消光系数和相位矩阵（包含相干多次散射效应），第二步将模拟值用于辐射传输方程。

> 第4-6章已详细研究粗糙面散射模拟。本章将进行体散射模拟。体散射多了一个维度，直接模拟双站/反散射系数困难，故分解为两步：第一步对包含许多散射体的测试体积计算消光系数和相位矩阵（包含相干多次散射效应），第二步将模拟值用于辐射传输方程。

Classical vector radiative transfer theory which is studied in Volume I
has been used extensively in studying the electromagnetic scattcring effects.
However, classical radiative transfer theory assumes that the particles scatter
independently. This assumption is based on the random phases of scattering
by different particles and is valid if the particle positions are independent
and the randomness of relative positions is comparable to or larger than a
wavelength. Such an assumption can be invalid at microwave frequencics.
For exainple, in dense media with particles closely packed together as in
grains in snow and ice, and for scatterers clustered together as in branches
and leaves in a vegetation canopy, the randomness in the relative positions of
scatterers can be less than a wavelength. In such a case the scatterers scatter
collectively, and the effects of scattering have to be taken into account.
> 经典矢量辐射传输理论（第一卷第4章）假设独立散射，当粒子相对位置随机性≥波长时有效。但在微波频段（如雪中冰粒密堆积、植被枝干簇状），相对位置随机性可能<波长，散射体呈集体散射。

> 本章通过研究点散射体的案例来测试集体散射概念。点散射体的优势在于基于Foldy-Lax自洽多次散射方程可轻松计算蒙特卡洛精确解。比较均匀分布和簇状分布两种情况，并描述求解多次散射方程的迭代方法。前向散射振幅结合Foldy近似用于计算消光率，但N粒子前向散射振幅需计算至二阶才适用。

In this chapter, we study the collective scattering effects of a conglom-
cration of particles. The radiative transfer theory is modified by defining the
phase matrix and extinction coefficient as, respectively, the bistatic cross
section per unit volume of space and the extinction cross section per unit
volume of space. The limit of the volume of space is taken to be larger or
much larger than a wavelength so that the collective and coherent scattering
effects of N particles within the test volume are taken into account. We test
the concept of collective scattering by studying the case of point scatterers.
The advantage of point scatterers is that the exact solutions of Monte Carlo
simulations can be readily computed based on the Foldy-Lax self-consistent
multiple scattering equations. We compare the case when the point scat-
terers are uniformly distributed and the case when the point scatterers are
--- PAGE 394 ---
§1 Combining Volume Scattering Simulations with Radiative Transfer 373
> 本章通过点散射体的蒙特卡洛模拟测试集体散射概念。相干波在大体积和大N极限下趋近于前向delta函数，相干场强度须从总散射强度中扣除，得到描述能量从前向散射到其他方向的相位矩阵和描述前向波衰减的消光系数。

> 相干波在大体积和大N极限下趋近于前向的delta函数。因此，相干场强度须从总散射强度中扣除，以给出：(a) 描述能量从前向散射到其他方向的相位矩阵；(b) 描述前向波衰减的消光系数。通过求解波动方程并对多次实现取平均进行蒙特卡洛模拟。

in clusters. We also describe the iterative approach for solving the multi-
ple scattering equations. Forward scattering amplitude in conjunction with
Foldy's approximation has been uscd to calculate the extinction rate. It is
shown that this is only applicable if the N-particle forward scattering am-
plitude is calculated to the second order. It is also shown that the coherent
wave approaches a delta function in the forward dircction in the limit of a
large volume and large number of scatterers (large N). Thus, the coherent
field intensity has to be subtracted from the total scattered intensity to give
(a) the phase matrix which describes the scattering of energy away from
the forward direction and (b) the extinction coefficient which describes the
wave decay in the forward direction. We perform Monte Carlo simulations
by solving the wave equations and averaging over many realizations.

1 Combining Simulations of Collective Volume Scattering

> **第1节：集体体散射效应模拟与辐射传输理论的结合**

Effects with Radiative Transfer Theory

> **第1节：集体体散射效应模拟与辐射传输理论的结合**。重新定义辐射传输理论的散射和消光参数以包含粒子的集体散射行为，区别于常规的平均单粒子散射定义。

In this section we redefine the scattering and extinction parameters of radia-
tive transfer theory to include the collective scattering bchavior of particles.
This distinguishes the definition from the conventional definition of averaged.
single-particle scattering behavior.
> 重新定义辐射传输理论的散射和消光参数以包含粒子的集体散射行为。体元V需满足条件：V>>λ³且包含大量粒子N，确保V中的相干多次散射包含随机相位涨落。

> 在辐射传输理论中，考虑特定强度入射到横截面积A、长度ds的体元V（图7.1.1）。体元V = Ads需满足以下条件：(i) V >> λ³ 或 V >> λ³；(ii) V中包含大量粒子N。条件(i)(ii)确保V中的相干多次散射包含随机相位涨落，使能量进出V可平均。

In radiative transfer theory we consider a specific intensity incident upon
an elemental volume with cross-sectional area A and length ds (Fig. 7-1-1).
The cross-sectional shape is arbitrary. It is an elemental test volume in the
development of the radiative transfer equation. It is not small in the sense
of the wave equation. The elemental volume V = Ads needs to obey the
--- PAGE 395 ---
374 7 VOLUME SCATTERING SIMULATIONS
following criteria:
(i) V > » or V2*. In other words, V = NyA°, where Ny is a number of
moderate size.
(ii) There is a large number of particles, N, contained in V. The particles
are randomly positioned.

> 设E_i为入射场，E_s为N粒子体积V的散射场。散射场可分解为相干场<E_s>和非相干场ε_s。

Let F; be the incident field in the direction k; = (6;,;), and let E, be
the scattered ficld from volume V of N particles.
Ey = exp(ikj - 7) (7.1.1)
The scattered ficld can be decomposed into coherent field (F;) and incoher-
ent field €,.
Es — (Es) + €s (7.1.2)

> N粒子总散射振幅F(k_s, k_i)可分解为相干分量<F>和非相干分量\~F。光学定理适用于N散射体（视为单个"N散射体"对象）。

From one clemental volume V to most other elemental volumes, the far
field of #, can be taken. We have
> » .exp(ikr
By = Fy, ky 22 (713)
where hy = (0,.s) is the scattered direction. In (7.1.3), F' (Rs, 0) represents
the N-particle collective scattering amplitude. It can be decomposed into
coherent component (F(ks,k;)) and incoherent component F(ks, ki).
F (ks, ki) = (F (ks, ki)) + F (Bs, ke) (7.1.4)

> 相位函数P(k_s, k_i)和散射系数κ_s重新定义为考虑N粒子集体散射行为的量（式7.1.6-7.1.7），取大体积极限下固定数密度n_0 = N/V。这些定义包含集体散射效应，且应与测试体积V的形状无关。

The phase function P(ks, k;) and the scattering coefficient «s are next defined
to take into account the collective scattering behavior of N particles.
a hg, ki) |?
Plis ki) = ti (Fs kd!) (7.1.6)
V—large Vv
--- PAGE 396 ---
§1 Combining Volume Scattering Simulations with Radiative Transfer 375
Ks = [e2P Gok (7.1.7)

> 相干N粒子散射振幅<F>依赖于体元形状，故相位函数仅包含非相干波。定义的相位函数和散射系数是单位体积的量。吸收系数κ_a = P_a/(V × 入射通量)，为极限下每单位体积的吸收截面。消光系数κ_e = κ_a + κ_s。

The limit in (7.1.6) is taken for fixed no, where ny = N/V is the number of
particles per unit volume. Thus the definition of (7.1.6) and (7.1.7) contains
collective scattering effects. The results of (7.1.6) and (7.1.7) should also be
independent of the shape of elemental test volume V. On the other hand,
the coherent N-particle scattering amplitude (#) as given by the coherent:
wave is dependent on the shape of the elemental volume V. Thus the phase
function in (7.1.6) only includes the incoherent wave. The phase function and
the scattering coefficient defined in (7.1.6) and (7.1.7) are per unit volume
quantities in the limit of large volume. Note that the limit with large N
and large V is taken for convergence. The coherent field is excluded from
the equations defining the extinction coefficient and the phase function. The
absorption coefficient is
Pa
= oT 7.1.8
"a V x (incident flux) (7.1.8)
where P, is the power absorbed by the N particles in volume V that includes
coherent wave interaction among the particles. Thus, the absorption coeffi-
cient is the absorption cross section per unit volume in the limit of large V.
The extinction coefficient is
Ke = Ka + Ks (7.1.9)

> 相位矩阵和消光系数计算后，辐射传输方程采用标准形式(7.1.10)。体元V的上限条件(iii)：V << (L_mfp)³，其中L_mfp = 1/κ_e。条件(i)(iii)可同时满足当L_mfp >> λ或k >> κ_e，这也是传输型方程有效的条件。当L_mfp ≈ λ时（Ioffe-Regel判据），可能出现强光子局域化。

Once the phase matrix and the extinction coefficient are calculated, the
radiative transfer equation assumes the following standard form
1
ales) = —K LF, 8) + [eorre.syie, 8) (7.1.10)
8 J

> 当条件(7.1.12)(7.1.13)满足但仍有后向散射增强（弱光子局域化）的情况。后向散射增强是循环散射图的结果，辐射传输方程仅含梯形图，不包含此效应，在第三卷讨论。对于N散射体独立散射的情况，(<|F|²>) = N<|f|²>，则P = n_0<|f|²>，退化为常规辐射传输理论结果。

To establish the upper limit of elemental volume V for the definition of
the phase function and the scattering coefficient, we note that if V is too
large, then the definition of (7.1.6) will include the radiative transfer theory
of (7.1.10) and is actually the bistatic cross section of the overall medium
(rather than the elemental test volume V as used) with multiple incoherent
scattering included. Thus, the upper limit of elemental volume V is that V
needs to be small cnough so that multiple scattering of incoherent waves can
be excluded. Multiple scattering of incoherent waves will take place in the
distance scale of the mean free path L»fp where
1
L =— TAAL
mfp Ke ( )
Thus the third criterion of V is an upper limit and is
--- PAGE 397 ---
376 7 VOLUME SCATTERING SIMULATIONS
3
(iii) Vi< (4)
The volume V can simultancously satisfy criteria (i) and (iii) if the mean
free path is much larger than the wavelength or the wavenumber is much
larger than the extinction coefficient.
Ingp > > (7.1.12)
k> he (7.1.13)
The conditions as exhibited in (7.1.12) and (7.1.13) are actually the condi-
tions for transport-type equations to be valid. When the condition is violated
so that Imsp & A (known as the Ioffe-Regel criterion) [Sheng, 1990], strong
photon localization may take place and radiative transfer-type equations
are inappropriate. For real-life applications, conditions (7.1.12) and (7.1.13)
are usually obeyed. However, even though (7.1.12) and (7.1.13) are obeyed,
there are still cases when backscattering enhancement (weak photon local-
ization) will take place. Backscattering enhancement is a result of cyclical
scattering diagrams and is not included in the radiative transfer equations
which only include ladder diagrams. We discuss backscattering enhancement
in Volume III. For the case of independent scattering of the N scatterers,
(\F (ks, ki)|?) = N (FI?) so that P(ks, ki) = no(|f|?), where ny = N/V is the
number of particles per unit volume and (| f|?) is the averaged single-particle
scattering cross section. Thus, (7.1.6) and (7.1.7) reduce to the result of con-
ventional radiative transfer theory. In the following sections we illustrate the
applications of these new definitions by using examples of two different types
of random distributions of point scatterers.

2 Foldy-Lax Self-Consistent Multiple Scattering Equations

> **第2节：Foldy-Lax自洽多次散射方程**

> **第2节：Foldy-Lax自洽多次散射方程**。

2.1 Final Exciting Field and Multiple Scattering Equation

> **2.1 最终激发场与多次散射方程**

> **2.1 最终激发场与多次散射方程**。考虑体积V中的N个粒子分布（图7.2.1）。每个粒子j有单粒子散射过渡算符T_j，当它单独存在时是对单粒子散射性质的精确描述，包含近场和远场效应。给定入射场Ψ_inc和入射到粒子j的场Ψ_j^E，粒子j的散射场为Ψ_j^S = G_0 T_j Ψ_j^E。

Consider a distribution of N particles in a volume V (Fig. 7.2.1). Let Uine be
the incident wave. The wave generally will be scattered by all the particles.
Each particle will have incidence upon it, the incident wave and the multiply
scattered wave from all other particles. How do we write an expression for
the field y that is the final answer after multiple scattering? A self-consistent
result can be constructed in a manner due to Foldy [1945] and Lax [1952].
Each particle j has a single-particle scattering transition operator T).
This is the response of the particle when it exists alone. In Volume J we
have calculated single-particle scattering propertics of scatterers with simple
shapes. The operator Tj is an exact transition operator for a single particle
--- PAGE 398 ---
§2.1 Final Exciting Field and Multiple Scattering Equation 377
> 考虑体积V中的N个粒子分布（图7.2.1）。每个粒子j有单粒子散射过渡算符T_j，包含近场和远场效应。Foldy-Lax自洽多次散射方程是Maxwell方程的精确描述，N个方程N个未知数。

> 两个粒子j和l的情况：总场包含直接散射、二阶散射（从j到l再从l散射，或从l到j再从j散射）等无穷级数。通过对无穷级数重排，定义Ψ_j^E为"最终"激发粒子j的场，Ψ_l^S为粒子l的"最终"散射场。

includes near-field and far-field effects.

'Thus given a single particle j and a field Y/ impinging upon a particle

j, the scattered field from particle j is

U5 = GoToF (7.2.1)
where the superscript £ denotes exciting field and Gp is the Green's function
(propagator).

Next consider two particles 7 and | with the incident field wine upon

them. The total field includes

® = Wine + Gol Wine + GoTjbine + °° (7.2.2)

> 重排无穷级数得到自洽方程(7.2.13)(7.2.14)：Ψ_j^E = Ψ_inc + G_0 T_l Ψ_l^S，Ψ_l^E = Ψ_inc + G_0 T_j Ψ_j^S。注意G_0 T_j Ψ_j^E不会出现在Ψ_j^E右侧，因为粒子的最终激发场不会激发自身。Foldy-Lax方程是精确的。

where GoTibine and GoTtine are the scattered fields from particle | and
particle j, respectively, that "directly" scatters inc.

However, there can be second-order scattering which are GoT}GoTjWine
and GoTjGoTiWinc. The second-order field GoT}GoTjyPinc scatters the inci-
dent field from j to | which further scatters the field.
Similarly, GoTjGoTiPine consists of scattering first from particle | and then
from particle j. Thus we have

WO = Wine+GoliVine+ GoT jPine+ GoTi Gol; Pine + GoTjGoTiPine+ > (7.2.3)
We can keep repeating for the third order, the fourth order and so on, up to
an infinite number of terms

= Vine + GoTrpine + Gol ;Vine + GoTtGoTj Vine + GoT;GoT Vine

+ GoTGoT; GoT Wine + GoT;GoTiGoTj Wine
+ GoT\GoTjGoTiGoTjhine + GoT;GoTiG@oTjGoTivine + +++ (7.2.4)

> 推广到N粒子：Ψ_j^E = Ψ_inc + Σ_{l≠j} G_0 T_l Ψ_l^E （j=1,...,N）。总散射场Ψ_s = Σ_j Ψ_j^S，Ψ_j^S = G_0 T_j Ψ_j^E。总场Ψ = Ψ_inc + Ψ_s。Foldy-Lax自洽多次散射方程(7.2.15)-(7.2.18)由Maxwell方程导出，是精确的，无近似[Peterson and Strom, 1973; Tsang et al, 1985]。一般包含N个方程、N个未知数Ψ_j^E，可数值求解。

'The infinite series in (7.2.4) can be rearranged as follows
v =Vine + Goli (vine + GoTjPine + GoT}GoTiWine
+ GoT}GoNGoLythine + ---) + GoT} (vine + GoTivine
+ GoLiGoT; Pine + GoTIGoLjGoTivine + +++) (7.2.5)

> 第一和经过粒子l为最后粒子，第二和经过粒子j为最后粒子。定义Ψ_l^E为第一个括号中的和，Ψ_j^E为第二个括号中的和。最终激发场Ψ_j^E表示经过粒子间的多次散射后最终激发粒子j的场。

The first sum in (7.2.5) went through particle I as the last particle, and the
second sum in (7.2.5) went through particle j as the last particle. We define
the exciting field %/ to be the sum in the first parentheses and define the
exciting field ue to be the sum in the second parenthesis. Thus
WF = Vine + GoliWine + FoTGoTjVine + GoNGoT)Golivine
+ GoTiGoTjGoTiGolWine + +++ (7.2.6)
dP =Vine + GoT Pine + GoTjGoTivine + GoTjGoTiGoT Wine
+ GoTjGoT:GoTjGoTiWine + +++ (7.2.7)

> 两个粒子的Foldy-Lax多次散射方程(7.2.13)(7.2.14)是精确的。T_j和T_l仅为单粒子散射过渡算符。

We also let
we = Golf (7.2.8a)
Ww} = GoTyb? (7.2.8b)
be the scattered fields from particles / and j, respectively. Then,
O= Pine + WE + YF (7.2.9)
We also have
Y= Pine + Ps (7.2.10)
bs =U + U5 (7.2.11)
Thus we of (7.2.6) represents the "final" exciting ficld that excites particle j.
Tt expresses the idea that after going through multiple scattering between the
two particles, this is the field that is finally exciting the particle j. Similarly
yf is the "final" scattered field from particle 1.
Next, the infinite series in (7.2.6) can be manipulated as follows:
UF = Vine + Gol Vine+ Gol} Vine +GoljGoT bine + Gol jGoNGoT hine+--*)
(7.2.12)
Comparing with (7.2.7), it is clear that the term in the parentheses in (7.2.12)
is yf. Thus
EB aj Tape 5
WF = Vine + GoTnhj (7.2.13)
Similarly from (7.2.7) we obtain
UP = Vine + oly} (7.2.14)

2.2 Foldy-Lax Equations for Point Scatterers

> **2.2 点散射体的Foldy-Lax方程**。点散射体的过渡算符T_j形式简单。点散射体的单粒子散射关系为Ψ_s = f e^{ikr}/r，其中f为标量。为满足光学定理，f必须为复数。散射截面σ_s = 4π|f|²。前向散射定理给出kσ_a/(4π) + k|f|²/π = Im(f)，其中σ_a为吸收截面。

For the cases of point scatterers, the transition operator Tj is simple so that
the Foldy-Lax multiple scattering equations assume a simple form. The point
scatterer has a simple single-particle scattering relation of
> 点散射体简化了Foldy-Lax方程，散射关系Ψ_s = f e^{ikr}/r。f为复数以满足光学定理，散射截面σ_s = 4π|f|²。T_j = -4πf δ(r-r_j)。

efkr

— 7.2.19

fc (7.2.19)

where f is an isotropic quantity. To obey the optical theorem, f must be
--- PAGE 401 ---
380 7 VOLUME SCATTERING SIMULATIONS
complex. The scattering cross section is
O.= fesse = 4n|f/? (7.2.20)
Hence, applying the forward scattering theorem, we have
; dr
oa +4n|fP2 = Fins (7.2.21)
where ¢q is the absorption cross section of the particle. Thus we assume that
f=fi+if" (7.2.22)
and |f"| < | f"| so that
ko,
ppt BOa 2.93
frakf?+ (7.2.23)

> T_j = -4πf δ(r - r_j)。N个点粒子中心在r_1,...,r_N时，Foldy-Lax方程简化形式如(7.2.26)-(7.2.30)。

Ifo, =0, then f" = kf". For a point scatterer,
T; = —4n fO(F — 7) (7.2.24)
so that
eiklFT]
GoT bP = fy ©) (7.2.25)
J

> 使用直接迭代法求解：一阶解Ψ_j^E(1) = Ψ_inc(r_j)，高阶解(n>1)如式(7.2.33)。Foldy-Lax方程可写成矩阵形式(7.2.38)-(7.2.41)，阻抗矩阵Z×列向量ψ = b。迭代法（Neumann级数或Born级数）中一阶项即Born近似。

For N point particles centered at 71,...,7N, the Foldy-Lax multiple scat-
tering equations assume the following form
b N iklF—Fil kb
BFF) = Vinel®) + >> fat (7.2.26)
w
N ikir-7i| rE
WF) = Vinel(®) + » le = wP (Fi) (7.2.27)
eikFFl
v3) = {oF ) (7.2.28)
FF

2.3 The N-Particle Scattering Amplitude

> **2.3 N粒子散射振幅**

> **2.3 N粒子散射振幅**。矩阵方程(7.2.40)可精确求解。远场中总散射场如式(7.2.42)，其中k_s = kk̂_s为散射方向。N粒子双站散射振幅F(k_s, k_i) = Σ_l f e^{-i k_s·r_l} Ψ_l^E，如式(7.2.44)。

The matrix cquation (7.2.40) can be solved exactly and the exciting fields
can be calculated. The final scattered field is, in the far field, from (7.2.29),
NU ikF—Fi| ike N :
.€ 7 e iB, F 1, By.
vs = Liferay = Y fe BEG) (7.2.42)
1=1 1=1
where ky = kk, and k, is the scattered direction. Thus if we regard the N
particles as a single scattering object, the N-particle, then
eke
tis = Flks. ki) (7.2.43)
where F'(k,, ki) is the N-particle bistatic scattering amplitude inchiding col-
lective scattering effects. Comparing (7.2.43) and (7.2.42) gives
N -
Pkg, fei) = SO feo" yi) (7.2.44)
=I

3 Analytical Solutions of Point Scatterers

> **第3节：点散射体的解析解**

> **第3节：点散射体的解析解**。考虑两种分布：均匀随机分布和簇状分布。即使每单位体积平均散射体数相同，散射性质也可能截然不同。

We shall consider two cases of point scatterers. In the first case, the point
scatterers are uniformly randomly distributed. In the second case, the point
scatterers form clusters. We study scattering by a collection of clusters. We
shall show that even though the two cases have the same average number of
scatterers per unit volume, their scattering propertics are quite different.
> 考虑两种分布：均匀随机分布和簇状分布。即使每单位体积平均散射体数相同，散射性质可能截然不同。

3.1 Phase Function and Extinction Coefficient for Uniformly Dis-

> **3.1 均匀分布点散射体的相位函数与消光系数**

tributed Point Scatterers

> **3.1 均匀分布点散射体的相位函数和消光系数**。使用第1节的定义(7.1.6)(7.1.7)，将Foldy-Lax自洽多次散射方程解至二阶。考虑非吸收性点散射体，均匀随机分布在体积V中。

Tn this section we illustrate the phase function and the extinction coefficient
for nonabsorptive point scatterers using the definition of (7.1.6) and (7.1.7).
The Foldy-Lax self-consistent multiple scattering equations will be solved to
second order.
--- PAGE 404 ---
§3.1 Uniformly Distributed Point Scatterers 383

> 入射平面波沿k_i方向入射到体积V上（图7.3.1），V包含N个非吸收性点散射体。粒子位置分布通过单粒子PDF和多粒子联合PDF描述。

Consider an incident plane wave Ling in the direction k; impinging upon
a volume V, the size of which obeys the three criteria of Section 1. The
volume V contains N number of nonabsorptive point scatterers located at
F\,72,...,7N (Fig. 7.3.1). The point scatterers are uniformly and randomly
distributed in volume V.

> **一阶解**：Ψ_j^E(1) = e^{i k_i·r_j}。一阶N粒子散射振幅F^(1)(k_s,k_i) = f Σ_j e^{i k_d·r_j}，k_d = k_i - k_s。系综平均得<F^(1)(k_s,k_i)> = n_0 f ∫_V dr e^{i k_d·r}，在前向尖锐峰。一阶解不满足光学定理，需将InF计算至二阶。

The multiple scattering cquations for the "final" exciting field EZ, are,
from (7.2.26),
BLP) = Be F x exp(ik|F; — Tu) pt = 731
ea(7 3) = Eine(Fj) + Ls 7 ex (Fl) (7.3.1)
ies
where j = 1,2,3,...,N. After the exciting fields F2,,j = 1,2,...,N, are
solved, then the total field is given by
_ a ae
B(F) = Bine(t) + 97S Beal) (7.3.2)
1=1
From (7.2.44), the scattering amplitude for N particles is
N
Flix, ky) = 0 exp(-i, PEL (A) (7.3.3)
1

> 计算<|F^(1)|²>分解为j=l和j≠l两项。第一项N|f|²对应常规辐射传输理论，第二项包含相关效应，最后一项对应前向相干强度。一阶N粒子前向散射振幅Im F^(1) = k|f|²N/π仅含第一项，不含配对分布函数和尖锐前向散射。

The conventional radiative transfer theory gives the phase function and scat-
tering coefficient as
P(hes, ki) = nol fl? (7.3.4)
ks = Arno fl? (7.3.5)

> 定义非相干散射振幅\~F = F - <F>，从<|F|²>中减去|<F>|²得<|\~F|²>，除以V得相位函数P = n_0|f|² + n_0²|f|² ∫ dr e^{i k_d·r}[g(r)-1]。常规辐射传输理论P = n_0|f|²，仅当g=1时一致。

--- PAGE 409 ---
388 7 VOLUME SCATTERING SIMULATIONS

> 相干波的相位矩阵在大V极限下为前向Dirac delta函数。其功率（式7.3.26）随V增大不收敛且依赖于V的形状。纯前向散射不影响辐射传输，进一步证明在相位矩阵中排除相干波的合理性。

As clear from (7.3.25), the phase matrix of the coherent wave is a Dirac delta
function in the forward direction in the limit of large V. Its power as given by
(7.3.26) is nonconvergent with large V and also depends on the shape of V.
Purely forward scattering does not affect radiative transfer, which describes
the redistribution of radiative energy in different directions. This further
justifies the exclusion of the coherent wave in the phase matrix.

> **二阶解**：加入二阶后，能量守恒（光学定理）得到满足。N粒子前向散射振幅计算至二阶的结果如式(7.3.32)，对其虚部求积分验证光学定理（式7.3.33-7.3.35）。

Second-Order Solution
Next, we show that energy conservation is obeyed if we include second-order
scattering amplitude in the forward direction. In the second-order solution,
the exciting field is
x exp(ik|Fj —Fi|)
= exp(iky -F CXPURITG STU orn ak, - F
BS = exp(iki 73) + xv f iF Fil exp(ik; - 71) (7.3.28)
tw
> 能量守恒（光学定理）需将N粒子前向散射振幅计算至二阶才满足。一阶解不满足光学定理，不包含配对分布函数。

3.2 Scattering by Collection of Clusters

> **3.2 簇状分布散射体的散射**

> **3.2 簇集合的散射**。每个簇标记为主散射体，簇内点散射体为次散射体。相位函数和消光系数依赖于簇内配对函数g_s和簇间配对函数g_p。

Consider a volume clement V as defined in Section 1. The volume con-
tains N, primary scatterers (clusters), cach of which consists of N, sec-
ondary point scatterers (Fig. 7.3.2). The Np clusters are centered at Fg, a =
1,2,..., Np, and within each cluster a the secondary scatterers are centered
at Taj with respect to the center of the ath cluster, 7 = 1,2,...,N,. Thus

N=N,Np (7.3.36)
is the total number of particles in volume V. Then
N ; 9
No= = Nenp (7.3.37)

> 一阶集体散射振幅F^(1) = f Σ_p e^{i k_d·R_p} f_α(k_s,k_i)，其中f_α为簇散射振幅。相位函数P = n_p <|f_α|²> + n_p² |<f_α>|² ∫ dr e^{i k_d·r} [g_p(r)-1]。当g_p=1, g_s=1，簇为立方体积l³时解析式如(7.3.46)。

--- PAGE 411 ---
390 7 VOLUME SCATTERING SIMULATIONS

> 式(7.3.46)显示簇状分布的结果与均匀分布（式7.3.22）显著不同，某些情况下大得多。这表明当小点散射体聚集形成"更大"粒子时，即使总小散射体数相同，散射可大大增强。

is the number of particles per unit volume and n, = N,/V is the number of
clusters per unit volume. Note that N and N, are large numbers in V while
IN, does not have to be large. Then, from (7.3.11), the first-order collective
scattering amplitude is
N Np Ny
FO (hei) = f So exp(ika-F)) = f 7 YW expibe: Fa +Faj)) (7.3.38)
jel a=1 j=l
where 7; = 7a +Foj. This can be expressed in terms of the scattering am-
plitude of the primary scatterers with
N.
L2 (kes, ki) = f YO exp(ika + Fas) (7.3.39a)
j=l
so that
--- PAGE 412 ---
§3.2 Scattering by Collection of Clusters 391
Np
FO) (Reg, Fe) = So exp (ig Fa) £0 (ee fe) (7.3.39)
a=l
The phase function is
a FO (by, bi) 2) — (PO (he, by) 2
P(kg ki) = SE eat ee (7.3.40a)

4 Monte Carlo Simulation Results of Point Scatterers

> **第4节：点散射体的蒙特卡洛模拟结果**

> **第4节：点散射体的蒙特卡洛模拟结果**。计算均匀随机分布和簇状随机分布两种情况的消光系数和相位函数。

In this section we illustrate Monte Carlo simulations of scattering by point
scatterers. We calculate the extinction coefficients and phase functions for
the cases of uniformly random distribution and the case of clustered random
distributions.
> 本节展示点散射体的蒙特卡洛模拟结果。λ=3cm，L=50λ，θ_i=10°，φ_i=10°。500散射体，100次实现。均匀分布与簇状分布显著不同。

> 入射波E_inc = e^{i k_i·r}，k_i如式(7.4.2)。N粒子放置在立方体积V = L³中。通过求解Foldy-Lax方程得到激发场，然后在远场计算散射场和N粒子散射振幅F。

Consider an incident wave impinging upon N scatterers
Eine(P) = ef * (7.4.1)
where
kj = k(sin 0; cos @i& + sin 0; sin d:f + cos 6,2) (7.4.2)

> 通过多次实现取系综平均。平均散射振幅<F>和非相干散射振幅\~F按式(7.4.7)(7.4.8)计算。相位函数按式(7.4.9)计算，消光系数按式(7.4.10)通过对所有散射角积分得到。

We start by putting N particles in a cubic box of size V = L*. The coor-
dinates 7; = (a;,4j,2j),9 = 1,2,...,N, are determined by choosing three
random numbers between 0 and 1 and then multiplying them by L. Once the
positions of the N particles are given, we can solve the Foldy-Lax multiple
scattering equations
: 5) eS pil =F) pa
BL, = Bine(Fj) +S) fF ELF) (7.4.3)
a lit
143
j =1,2,...,.N. After the exciting field Fi, (Fj) are calculated, the "final"
scattered field can be calculated in the far-field region. Let
ks = k(sin 9, cos ds% + sin 0, sin os + cos 052) (7.4.4)

> 模拟参数：L = 50λ，入射平面波θ_i = 10°, φ_i = 10°。散射振幅f = 0.008905 + i0.0005（典型小粒子值，满足光学定理）。500个散射体。均匀随机分布：N=500在立方体内。簇状分布：50个簇，每簇10个粒子。结果取100次实现平均。

be the observation direction of the scattered ficld. Hence,
ike
Es?) = —— Fr (hss hi) (7.4.5)
where
> = N =
Fy (ks, ki) = 30 f exp(—ikis 71) Eee() (7.4.6)
I=L

> **均匀随机分布**（图7.4.1）：N=63（L=25λ）和N=500（L=50λ）的收敛性测试。独立散射理论κ_ei = 4πn_0|f|² = 4.0×10⁻⁶ λ⁻¹，MC模拟结果κ_e = 3.958×10⁻⁶ λ⁻¹（100次实现）。

is the N-particle scattering amplitude. These can be calculated for many
realizations. We then calculate the realization averages. Let angular bracket
() denote realization average. The coherent scattering amplitude is
N,
a 1 & a8
(Fw (ks, ki) = WD Fwvlhs, hi) (7.4.7)
OT rl

> **簇状分布**（图7.4.2）：簇尺寸l_c从1.0λ减小到0.2λ。相对消光系数κ_re = κ_e/κ_ei。l_c=1.0λ时与均匀分布几乎无差异；l_c=0.2λ时κ_re显著增大。这表明随机介质问题中簇状几何的重要性。

where r is the realization index and N,, is the number of realizations. The
incoherent scattering amplitude for each realization is
F (kas ki) = Fes bi) — (Fv (hss bi) (748)

> **相位函数极坐标图**（图7.4.3-7.4.4）：均匀分布和簇状分布（l_c=0.2λ）。簇状分布的非相干贡献大于均匀分布，而相干部分相反。相干部分在前向（θ_s=170°, φ_s=10°）有尖锐大振幅峰值（比其它方向大几十dB）。随V→∞，相干波趋近Dirac delta函数，须从相位和消光系数计算中排除。

The phase function is calculated by
ZA N,
7.) — Finks MP?) 1 ge ge pyr
Pll, fi) == = 2 Fitba (7.4.9)
The extinction coefficient is calculated by
7 2a .
ke = [ dd, sind, [ 04? (ks, bi) (7.4.10)
0 JO
--- PAGE 415 ---
394 7 VOLUME SCATTERING SIMULATIONS

> **二阶近似与精确解的比较**（图7.4.5-7.4.6）：单次实现中二阶解与精确解差异显著，但100次平均后吻合良好。这表明单次实现中高阶散射效应重要，但平均后趋于抵消，二阶理论适用于平均结果。

We present the Monte Carlo simulation results of two types of config-
urations as shown in Figs. 7.3.1 and 7.3.2. In Fig. 7.3.1 the nonabsorptive
particles are uniformly and randomly distributed in a cubic box of size L3. In
Fig. 7.3.2 the same number of particles are distributed in clusters in the cu-
bic box of size L, The clusters contain N particles cach. In each cluster the
particles are randomly distributed in a cubic volume of size (3. All distance
dimensions are in wavelengths (\). In the Monte Carlo simulations, (7.4.3)
is solved exactly to find the incoherent phase function as defined by (7.4.8).
Then the scattcring coefficient defined by (7.4.10) is found by integrating
over all scattered angles. To make comparisons, we also find the scattering
coefficient and the phase function by approximating the multiple scattering
equation to the second order
> 均匀分布和簇状分布的MC结果比较。簇尺寸l_c=0.2λ时消光系数比l_c=1.0λ大得多，显示簇状几何的重要性。MC结果与集体散射理论一致，独立散射预测错误。

(Q)2 + N ~~. NWN oc _ eiklti-F

Fy (Fes, hi) = YO FERRI 4 SE pherthe™ et (7.4.11)
j=l j=l [=1 Ir; —¥el

> **解析集体散射理论与MC比较**（图7.4.7）：式(7.3.46)的解析集体散射理论、独立散射理论和MC模拟（1000次实现）的比较。MC结果与集体散射理论一致，独立散射预测错误。MC结果的凹陷是由于从总相位函数中减去了相干部分。

taj
The second-order iterative approach is then compared with the exact solu-
tion.

The cubic box is of volume V and the length of each side L is 50\. A
scalar plane wave is incident at 6; = 10° and ¢; = 10°. The incident and
scattering angles are defined as in Fig. 7.3.1 such that the backscattering di-
rection is #; = 6; and @s = m+ qj. For illustrations, let scattering amplitude
f = (0.008905 + 10.0005). The value of f is typical of a small particle. The
real and imaginary parts are chosen to obey the optical theorem of (7.2.23)
of a single non-absorptive particle. In different realizations, we only change
the positions of the particles. The positions of 500 scatterers are generated
randomly. For the uniform random case, N = 500 center positions are gener-
ated randomly within the cubic box (Fig. 7.3.1) of side length L. For the case
of clustered random distribution, N = 500 particle positions are generated in
two stages (Fig. 7.3.2). The 500 particles are of 50 clusters with each cluster
containing 10 particles. The cluster volume is a cube with length /.. Initially,
50 center positions are generated within the cube of length L and they are
randomly chosen with the constraint that there is no interpenetration of
the different cluster cubes. Then in the second stage, we randomly generate
10 particles inside each cluster of volume 13. We vary /, and investigate its
effects. The results are calculated for 100 realizations.

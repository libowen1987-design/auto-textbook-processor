# Tsang《Scattering of EM Waves》Chapter 8

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 8

> **第八章：大粒子稠密介质**。研究稠密介质中粒子尺寸较大的情况，涉及配对分布函数与结构因子、Percus-Yevick方程、硬球和粘性球的PY解、蒙特卡洛模拟粒子位置、粘性粒子模型、以及椭球体的粒子放置算法。**

PARTICLE POSITIONS FOR DENSE MEDIA
CHARACTERIZATIONS AND SIMULATIONS
1 Pair Distribution Functions and Structure Factors 404

> **第1节：配对分布函数与结构因子**（第404页）

1.1 Introduction 404

> **1.1 引言**

1.2 Pereus—Yevick Equation and Pair Distribution Function for

> **1.2 Percus-Yevick方程与硬球的配对分布函数**

Hard Spheres 406
1.3 Calculation of Structure Factor and Pair Distribution Function 409

> **1.3 结构因子和配对分布函数的计算**

2 Percus—Yevick Pair Distribution Functions for Multiple

> **第2节：多种尺寸的Percus-Yevick配对分布函数**

Sizes 411
3 Monte Carlo Simulations of Particle Positions 414

> **第3节：粒子位置的蒙特卡洛模拟**

3.1 Metropolis Monte Carlo Technique A15

> **3.1 Metropolis蒙特卡洛技术**

3.2 Sequential Addition Method 418

> **3.2 顺序添加法**

3.3. Numerical Results A18
4 Sticky Particles 424

> **第4节：粘性粒子**

4.1 Percus~Yevick Pair Distribution Function for Sticky Spheres 424

> **4.1 粘性球的Percus-Yevick配对分布函数**

4.2. Pair Distribution Function of Adhesive Sphere Mixture 429
4.3 Monte Carlo Simulation of Adhesive Spheres 434

> **4.3 粘附球的蒙特卡洛模拟**

5 Particle Placement Algorithm for Spheroids 444

> **第5节：椭球的粒子放置算法**

5.1 Contact Functions of Two Ellipsoids 445

> **5.1 两椭球的接触函数**

5.2 Illustrations of Contact Functions 446

> **5.2 接触函数的图示**

References and Additional Readings 450
= 403 —
--- PAGE 424 ---
404 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS

The scattering of electromagnetic waves by random media depends on.
the positions of the particles. A dense medium denotes a medium where
the particles are densely packed and occupy appreciable fractional volume.
In the random medium, the probability density function (pdf) of particle
positions p(7;) is uniformly random, However, because of the finiteness of
particle size, the joint probability density function of two particle positions
cannot be independent. If p(7i,7;) is the joint probability density function
of two particles centered at 7; and 7, then p(T;,7;) = 0 for |F; —T;| smaller
than the minimum separation which is the diameter if the two particles are
spheres of the same radius. The pair distribution function is proportional
to the joint probability density functions of two particles. The finiteness of
the particle sizes creates nontrivial pair distribution functions. The Fourier
transform of the pair distribution function is the structure factor. We have
discussed pair distribution function in Chapter 4, Section 5.2 of Volume I. In
this chapter, we consider two methods of studying random particle positions.
One method is based on analytic theory to derive analytic pair distribution
functions. The other method is to use Monte Carlo simulations to generate
particle positions. The Monte Carlo procedure of generating particle posi-
tions is also important as numerical solutions of the Maxwell equations can
be computed based on the generated realizations. On the other hand, an-
alytic pair distribution function is useful for analytic scattering theory of
dense media. Analytic scattering theory of dense media will be treated in
Volume IIL.

In Section 1, we describe the pair distribution function under the Percus-
Yevick approximation. In Section 2, we consider the case where the particles
in the same medium can have different sizes. In Section 3, we describe Monte
Carlo simulations of spherical particles. In Section 4, we consider the case
of sticky particles. This represents the case when particles have adhesive
force. The adhesive force means that the particles can form aggregates. We
consider the case of collections of aggregates. In Section 5, the Monte Carlo
technique is extended to particles of spheroidal shapes.

1 Pair Distribution Functions and Structure Factors

> **第1节：配对分布函数与结构因子**（第404页）

1.1 Introduction
Let N be the number of particles. They are centered at 71,72,...,7y. Let
the particles be put in a volume V. Then
1
wT) =F (8.1.1)
--- PAGE 425 ---
§1.1 Introduction 405
is the single-particle pdf, and from Volume I, Eqs. (4.5.21) (4.5.23),
g(Fistj) N
WF. F,) = Sats) (8.1.2)
is the joint pdf of two particles, and g is the pair distribution function. In
the limit of large N, p(7i,7j) © g(Fi,7;)/V?.

Analytic theory of volume scattering is discussed in Volume IIT, where
it is shown that in applying the quasi-crystalline approximation and the
quasi-crystalline approximation with coherent potential, the pair distribu-
tion function of particle positions must be specified. In the special case of
independent particle position, g(F) = 1. Another approximation to the pair
distribution function is the hole-correction (HC) approximation, given by
g(r) = 0 for r < b and g(r) = 1 for r > b, where b is the diameter of the
circumscribing sphere of the particle. For the case of spherical particles with
radius a, } is equal to 2a. The hole-correction approximation takes into ac-
count the fact that the particles cannot interpenetrate each other. Neither
the independent position approximation nor the hole-correction approxima-
tion is correct when the fractional volume of scatterers, f, is appreciable.
It is easier to visualize this for the case of one-dimensional scatterers. The
hole-correction approximation is illustrated in Fig. 8.1.1A. Next we imagine
that f is equal to unity so that the entire volume V is occupied by scat-
terers. In such a case, the centers of these one-dimensional particles will be
separated by integral multiples of 6 from each other. The pair distribution
function g(r) will be zero for r # mb where m is any nonzero integer. It
consists of delta functions at the position of r equal to an integral multiple
of b (Fig. 8.1.1B). Thus, the hole-correction approximation is poor in such a
limit. When f is not equal to 1 but appreciable, the pair distribution func-
tion will be of a form between A and B in Fig. 8.1.1. We also note that as the
two-particle separation r approaches infinity, the positions of the particles
should be independent of each other. Hence lim g(r) = 1 for f not equal to
maximum concentration. mes

The study of pair distribution functions is a subject of interest in statis-
tical mechanics [McQuarrie, 1976]. Based on the form of the pair distribu-
tion function, substances can be classified into three different types: (1) gas;
(2) liquid and amorphous solid; and (3) crystalline solid. The three forms of
the pair distribution function are illustrated in Fig. 8.1.2. The case of gas
with particles sparsely distributed is considered to be a system of extreme
disorder, so that the hole-correction approximation or the independent po-
sition approximation is a good description of the pair distribution function.
In the opposite extreme, the case of crystalline solid with relative positions
--- PAGE 426 ---
406 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
{| [| TUT
b
(1) Particles (W) Particles
alr) alr)
{o_ r TELL r
’ b 2b 3b Ab 5b Gb Tb Sb 9b 105
(11) Pair Function (U1) Pair Function
A. Small f Bf=l
Figure 8.1.1 Pair distribution function for one-dimensional particles: (A) Small f; particles
and pair function. (B) f = 1; particles and pair function.
of the particles fixed is a case of extreme order. The pair distribution func-
tion exhibits sharp peaks (Fig. 8.1.2c). The case of a liquid and amorphous
solid is a system of partial order and is an interpolation between the two ex-
treme cases of gas and crystalline solid (Fig. 8.1.2d), Extensive experimental
and theoretical investigations have been carried out for the pair distribution
function of liquid and amorphous solid [Waseda, 1980]. To the first-order
approximation, the bistatic scattering intensity is proportional to the struc-
ture factor which is related to the Fourier transform of the pair distribution
functions. The study of pair distribution functions is an important subject
in molecular theory of fluids as well as in random media [Wertheim, 1963,
1964; McQuarrie, 1976; Ziman, 1979; Perram et al. 1984; Perla et al. 1986;
Penders and Vrij, 1990; Shi et al. 1993; Zurk et al. 1997].
1.2 Percus—Yevick Equation and Pair Distribution Function for
Hard Spheres
A total influence A of a particle 1 on another particle 2 can be defined as
hFi2) = g(F2) — 1 (8.1.3)
The total influence is decomposed into a sum of direct and indirect corre-
lation functions. The direct correlation function or influence is denoted by
cP):
(Piz) = e(Fi2) + indirect (8.1.4)
The direct correlation function is defined such that it satisfies the following
--- PAGE 427 ---
§1.2 Percus-Yevick Equation and Pair Distribution Function 407
alr) alr)
1 |[— 1 ao -
r r
ob
a) Independent b) Gas (Hole correction)
g(r) ar)
fv
r r
0b
c) Crystalline solid d) Liquid or amorphous solid
Figure 8.1.2 Pair functions for (a) independent: particle position, (b) gas, (c) crystalline
solid, and (d) liquid and amorphous solid.
integral equation:
A(Fi2) = c(Fi2) +1 f dractris)M(o2) (8.1.5a)
From (8.1.3),

HF) =olPva) +10 f araclPrealFaa) ~ 3] (8.1.56)
which is known as the Ornstein-Zernike equation. The physical interpretation
of the second term of (8.1.5a). which is the indirect. correlation function, is
that the indirect influence of particle 1 on particle 2 is a result of particle
1 acting directly on a particle at 73, which in turn exerts total influence
on particle 2. The indirect. influence is averaged over particle positions 73
and weighted by the number of particles per unit volume n, as indicated in
(8.1.5a) and (8.1.58).

The Ornstein-Zernike equation consists of two unknowns c(F) and h(F)
in one equation. An approximation is to be made on the relation between c(7)
and h(r), reducing (8.1.5) to one equation and one unknown. The Percus—
Yevick approximation [Percus and Yevick, 1958] can be introduced in the
following heuristic manner.
The potential energy between two particles is governed by u(7) where r
is their separation, For the case of hard sphere potential, we have
= oo forr<b
u(7) = 8.1.6
) {3 forr >b ( )
Equation (8.1.6) says that in the absence of other particles, the potential
energy between the two particles is infinite when they overlap each other
--- PAGE 428 ---
408 8 PARTICLE POSITIONS FOR. DENSE MEDIA CHARACTERIZATIONS
(thus disallowing interpenetration) and is zero otherwise. For this case, we
define y(F) so that
7 0 for r <b
97) = (bo forr >b (8.1.7)
The function y(F) is defined for both r < b and r > b. Equation (8.1.7)
defines it for r > 6. Later we will define it for r < 6,
In (8.1.7), we let g(F) = y(F) for r > 6. Then, for hard-sphere potential
we have
a — _f-t forr <b
ne) = 90) -1= {F - for r > (8.1.8)
When y = 1, there is no indirect influence. Thus y — 1 is a measure of
indirect influence. Also h — ¢ is equal to to indirect influence. The Percus
Yevick approximation consists of equating h —c to y— 1 for all 7.
A(7) — cF) = y(7) - 1 (8.1.9)
This equation then extends the definition of y(F) to r < b.
From (8.1.8) to (8.1.9) and (8.1.3) we obtain
e(F) = h(F) +1 — y(F) = g(F) — ylF) (8.1.10a)
From (8.1.10@) and (8.1.7) we have
=) _ fe?) forr<b
y(F) = {oe for r>b (8.1.10)
Also from (8.1.10a) and (8.1.10b) we have
=) -y(F) forr<b .
e(F) = {3 for r>b (8.1.10c)
Let Fig =F) —Po =F, M3 =71 —73 =?" so that F499 =73-7o =F-F in
(8.1.58). Note that from (8.1.8) and (8.1.10c), we have both h and c expressed
in terms of y. Thus expressing (8.1.56) in terms of y, we have
ut) =1= nf drut) ole —7) ~ 1 (8.1.11)
<b
We further decompose the integral of (8.1.11) into two parts of |7 — 7'| < b
and |F —7'| > b. The integral equation becomes:
yr) =1 +n [ ey UF) no f vey FUP Vy) —Y] (8.1.12)
|r’ |<b |F-Fl>b
A closed-form solution can be obtained for c(7) via the integral equation
(8.1.12) (Wertheim, 1963, 1964]. The solution is given below. Let the distance
--- PAGE 429 ---
§1.3 Calculation of Structure Factor and Pair Distribution Function 409
be normalized by b:
r
f= > 8.1.13
; (8.1.13)
The solution for (7) is a cubic polynomial
—e(z) =a + Bx + bx* (8.1.14)
for x <1 and e(x) = 0 for « > 1. In (8.1.14) we have
(1+ 2f)?
a= 8.1.15
aA G11)
(+ £/2)?
B=-6f ——— (8.1.16)
a-f)
fU+2f)?
6= LL
a0 fF e117)
ab
f= aa (8.1.18)
For spheres, b = 2a and f given in (8.1.18) is the fractional volume of
spherical scatterers.
1.3 Calculation of Structure Factor and Pair Distribution Func-

> **1.3 结构因子和配对分布函数的计算**

tion
The Born approximation and the distorted Born approximation give a bi-
static scattering cross section that is proportional to the structure factor. The
structure factor is related to the Fourier transform of the total correlation
function.
Define the Fourier transform of the total correlation function as
1 or
3) = iz TPT A F 1.19
HO)= oi [ua eFF hip) (8.1.19)
and let C(p) denote the Fourier transform of the direct correlation function
(Fr).
1 eo oF
(5) = 2 iPT ye
CO = a [are (7) (8.1.20)
The integral in the Ornstein-Zernike equation of (8.1.5) is a convolution
integral. Thus, in the Fourier transform domain, the integral in the Ornstein-
Zernike equation is proportional to the product of C(p) and H(p). Solving
the equation gives
a CP)
HO) = THROW) ery
--- PAGE 430 ---
410 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
The structure factor $(p) is defined as
S(B) =1+n (273A) (8.1.22)
The Quantity H(p) for the Percus—Yevick Hard-Sphere Pair Function
The closed-form solution for the direct correlation function of Percus~Yevick
hard spheres is given in (8.1.14) through (8.1.18). The Fourier transform C(p)
can be calculated readily and is only a function of pb, b, and f :
C(p) = Cpy (pb, b, f) (8.1.23)
with
(27)?noCpy (pb, b, f)
= 24f {et cosu— (a+ 26+ 49) sin uw
U ue
2(8 + 66 28 246 246
- eee) cosu + 2e + e sinu+ op eos - o} (8.1.24)
where wu = pb and a, 3,6 are given in (8.1.15) through (8.1.17). The closed-
form solution of H(p = 0) is obtained by letting p = 0 in (8.1.21), (8.1.23),
and (8.1.24). We get
(27) (p = 0) ” anlar) —1J=-14 222 (g1.5)
no(2ar =0)=n 7F)~Y=-1+—— 7 1.25,
“oe "Sooo 9 (427

To numerically compute the pair distribution function, the following
steps are taken.

Step 1: Use (8.1.24) to compute C(p). Because of spherical symmetry,
it is a function of p = |p| only.

Step 2: Use (8.1.21) to compute H(p) = H(p).

Step 3: Take inverse Fourier transform of H(p) to calculate h(7F) in ac-
cordance with (8.1.19). Because of spherical symmetry, we only need to carry
out a one-dimensional integral:

oo 7 oc
A(R) = h(r) = | dpe®*H(p) = 2n | a, sin bp [ dppre'?™ 8 H(p)
—00 0 0
20 .
=f dp? (==) H(p) (8.1.26)
0 pr

Step 4: The pair function is g(r) = A(r) +1.

In Fig. 8.1.3 we plot the g(r) for hard spheres for f = 0.2 and f = 0.4.
We note that the pair distribution functions are equal to zero for r less
--- PAGE 431 ---
§2 Percus-Yevick Pair Distribution Functions for Multiple Sizes 411
v aA
[ 02)
asp | Al,
3
25| |
. ) [
15st \ 4
\ la
/™ ee
' YL
os
a eC
rio
Figure 8.1.3 The Percus Yevick pair distribution function g(r) for hard spheres with
distance normalized by the diameter of the spheres
than a diameter. They assume maximum values at r = 6. As r increases,
they fluctuate and asymptotically approach unity. The case with larger f
fluctuates more. If we treat g = 1 as the independent position result, we can
see that positions are less independent as f increases.
2  Percus—Yevick Pair Distribution Functions for Multiple
Sizes
Many media consist of particles with multiple sizes. For a system of spher-
ical particles of L different sizes with radii a,,a2,...,az respectively, the
pair distribution function gi;(r) for a pair of particles of sizes a; and a; is
proportional to the conditional probability of finding a particle of size aj
at a distance r from the origin given that there is a particle of size a; at
the origin. The pair distribution functions depend on the sizes a), @2,...,az
and on the number densities n,n2,...,nz of the L species of spheres. The
number density n; is the number of particles per unit volume of radius a.
The conditional probability is in the presence of other particles. Similar to
the case of single size, the total correlation function hij(r) between a pair of
particles is defined as [Baxter, 1970]
ha(r) = g(r) -1 (8.2.1)
--- PAGE 432 ---
412 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
The direct correlation function cj;{r) is related to hi;(r) by means of the
generalized Ornstein-Zernike relation:
L
hi(r) = ey(r) + Som | dF ca(r’)huy (IF — #1) (8.2.2)
1=1
which is an extension of (8.1.5). Under the Percus-Yevick approximation,
and applying to the special case of zero interparticle force except for non-
interpenetration, we have, as an extension of (8.1.10c) and (8.1.8),
um — J ~wil) for r < aj +a;
eiy(?) = {5 for r > aj + ay (8.2.3)
._f-l for r < aj +a;
hglh) = {in —1 for r > aj +a; (8.2.4)
When (8.2.3) and (8.2.4) are substituted into (8.2.2), (8.2.2) becomes a set of
nonlinear integral equations for y:;(7),i, 7 = 1,2,..., L. The total correlation
function h;;(7) describes the total influence of a particle of radius a; on
another particle of radius a; with respect to their spatial arrangements. From
(8.2.2) the total correlation is separated into two contributions. The first
contribution is the direct effect between two particles which is short ranged,
as indicated in (8.2.3), and is described by cj; (7). The second contribution is
an indirect, effect, in which a particle of size a; influences some other particles
of size a, at 7, which in turn affects the particle of size aj. The solution for
impenetrable spherical particles has been obtained by Baxter [1970] using a
factorization technique.
Let Hi;(p) and C;;(p) be proportional to the respective 3-D Fourier
transform of hij(F) and cij(F):
HB) = (nany)"? [are ha) (825)
CtD) = (rary)? fare ex) (826)
In matrix form, let H,j; and C;; denote the (7,7) element of matrices Hand
C, respectively. The Fourier transform of Ornstein-Zernike relation becomes
H(p) = C(p) + Clp)H(p) (8.2.7)
Because of the spherical particle assumption, the transform only depends on
p= |p|. Based on the generalized Wiener—-Hopf technique, matrix C(p) can
be factorized into
C(p) = 1 QT(-p)Q(v) (8.2.8)
--- PAGE 433 ---
§2 Percus-Yevick Pair Distribution Functions for Multiple Sizes 413
where T is a unit matrix, and the superscript T denotes the transpose of
matrix. The matrix Q which has components Qi; as
Ris -
Qu (0) = 85 — fo" dremauer (8.2.9)
So
where 6;; is the Kronecker delta, Si; = a; — aj, and Rij = a; + aj, with a;
and ay being the radii of particle species i and j, respectively. The function
Qi;(r) has been solved and is given by
Qij(r) = 2n(ninj)?aiy(r) (8.2.10)
The solution of qij(r) is, for Sij <r < Ri,
2
Tr
g(r) = Ay + Bir + Dij (8.2.11)
with
1 — & + 6ai£2
Ay = ——_ 8.2.12
‘ (1 - 3)? ¢ }
6a? £>
B= -— 8.2.13
"Tap G28)
R
Dij = -AS — BiRij (8.2.14)
oes
fa= 5 Denia) (8.2.15)
j=l
and a@ = 0,1, 2,3.
From (8.2.8) (8.2.15), the matrix elements C;;(p) can be obtained as
Ciy(P)
mT fTGNG { . 3é2RicosX; — 36,N; 9E3N; |
= —7 + 4 Mj |cos Xj + Xi sin. Xj + -——_—.__ + ~— + 2-5
61-& ? o_— . 1-& 1-&  (1-&)?
. 362R;cosX; | 36N; , 9E3Nj |
+ Mj; |cos Xj + Xj sin Xj + ~SS—— 4+ St SD
| eee 1-& 1-3 (1-3)?
& Pk ists 9&3 |
+ M.M, |? + P44 a 4
a i —€  4(1-g)  (1—&)? (1 &)8
962 NiN,
+ 3N;, Rj cos X; +3N;R, cos Xi + eM} (8.2.16)
—&
where
sinX; cos X,
M; = 3R3 [ xe - "| (8.2.17)
--- PAGE 434 ---
414 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
Ni= Rae (8.2.18)
X= ph (8.2.19)
and J; = 2a; is the diameter of a particle of size a;. Thus, the procedure for
calculating the pair distribution function is as follows. First Cij(p) is calcu-
lated from (8.2.16) (8.2.19). Next, H(p) is computed by solving the linear
matrix equation (8.2.7). Then hj;(r) is obtained by taking an inverse Fourier
transform of H(p) according to (8.2.5). Finally, the pair distribution function
gij(r) can be calculated using (8.2.1). Numerical results of the Percus-Yevick
pair distribution function of multiple sizes will be shown in Section 3.3.
3 Monte Carlo Simulations of Particle Positions

> **第3节：粒子位置的蒙特卡洛模拟**

Jn this section we describe Monte Carlo simulations of the pair distribution
function of dense discrete random media. with multiple sizes of particles. Two
Monte Carlo methods, namely, the Metropolis technique and the sequential
addition of particles, are commonly used. Particle positions are generated
randomly in a cubic box. The number of particles used is between 400 and
4000. In the Metropolis Monte Carlo technique the particles are next shuffled
to create different realizations. On the other hand, the sequential addition
method adds particles serially and randomly into the box. Thus, in the se-
quential addition method the particles are not shuffled. In positioning the
particles, we assume that there are no interparticle forces except. that inter-
penetration is not allowed. Many realizations are used. We have used up to
3000 realizations. The pair distribution functions are calculated by using the
definition of joint probability density functions and by counting the occur-
rence of pair separation of particles as a function of separation distance. The
counting is averaged over these realizations. The edge effects of the cubic
box are taken into account by adopting the periodic boundary conditions.
The Monte Carlo results for the pair distribution function are illustrated
and compared with the results of the Percus-Yevick approximation for the
single-size case and for the case of multiple sizes. They are found to be in
good agreement. The Monte Carlo simulations show that the Percus Yevick
approximations of single size and multiple sizes can be used for macroscopic
objects such as particles in geophysical terrain and composite materials.
The computer experiments are performed on a system with N number of
particles. These N spheres with different sizes are placed inside a cubic cell
of side length @. Let N; be the number of particles of radius a;. Then number
--- PAGE 435 ---
§3.1 Metropolis Monte Carlo Technique 415
density n; and fractional volume f; for particles of radius a; are given by
n= = (8.3.1)
fi=mica} (8.3.2)
3
L
N=yOM (8.3.3)
i=l
L
f=Doh (8.3.4)
i=l
where f is the total fractional volume occupied by the particles.

We note that the pair distribution function gj;(7) approaches unity as 7
becomes large, meaning that the particle positions are independent: if they
are far apart. For a fractional volume of less than 40%, the pair distribution
functions are practically equal to unity for pair separations larger than five
diameters. Thus taking N between 400 and 4000 is generally sufficient to
simulate the pair distribution function. In the simulations, periodic boundary
conditions are employed. The N particles of interest are placed inside the
central cell, and this cental cell is taken to be surrounded by the periodic
images of itself. Each image cell contains N particles with exactly the same
geometric arrangement as that in the central primary cell.

3.1 Metropolis Monte Carlo Technique

> **3.1 Metropolis蒙特卡洛技术**

We use the technique of Metropolis et al. [1953] for both the 3-D case and
2-D case. The 2-D case is described in Chapier 9, Section 2. For the 3-D case,
we consider a cubic box containing N particles. Initially, the N spheres are
placed randomly inside the primary cell with no overlap. To generate new
realizations, the particles are shuffled as follows. In each cycle every particle
js subject to be randomly displaced once. The acceptance of its new position
is according to whether it overlaps another sphere or not. The displacement
is random and is not governed by any interparticle force except that it cannot
penetrate other particles. We should note that the displacement of particles
introduced in the simulation is for the purpose of creating new configurations
and realizations. It does not mean that the particles move physically, The
steps are as follows.

Step 1: Set an initial configuration of the system. The initial configura-
tion may be produced by assigning the particle coordinates within the cell.
All the coordinates of spheres lie in the range (0, ¢]. The initial configuration
--- PAGE 436 ---
416 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
may be obtained by placing all the particles in a periodic spatial function in
the box.

Step 2: Change the system configuration by random displacement, of
particles. The particles are displaced sequentially in the simulation. The
displacement of a particle to a new trial position is determined according to
the following prescription:

2or+An yoytAnm  2-+2+Anm (8.3.5)
where x, y, and z are the particle coordinates and A is the maximum dis-
placement allowed in each movement. The 7;, i = 1,2,3, are independent
random numbers uniformly distributed in the range [—@, £]. Thus after a dis-
placement, the particle is equally likely to be anywhere in a little cube of side
2eA centered about its original position. The prescription for displacing a
particle given by (8.3.5) must satisfy the periodic boundary conditions; that
is, if a particle is displaced past the cell on one side during the simulation, it
actually reenters the cell from the opposite side. For example, if the center
of a sphere changes to a new position (2’,y’, 2’) in this step, and if a’ > £, or
zw’ <0, then its new x coordinate will be a’ - @, or x’ + é, respectively. The
same applies to the y— and z— coordinates. If A is too small, displacements
are usually accepted. If A is too large, most displacements will be rejected.
The rule of thumb is to choose A such that the acceptance rate A, is from
30% to 70%.

Step 3: Check whether the displacements are accepted. It is possible
that the new position of the displaced particle may overlap one of the other
particles in the system. If not, accept the displacement and update the co-
ordinates of the displaced particle. Otherwise, reject the displacement and
return the particle to its original position. The value of maximum displace-
ment A influences the acceptance percentage of new positions. Even though
checking the overlap of particles is straightforward, care must be taken in
cases where a pair of particles do not overlap in the central cell but where
the image of one of them in the next cell is within the forbidden region of
the other.

Step 4: Update the number of configurations generated. Add one to the
number of configurations counted. It should be emphasized that even if a
displacement of the particle in a particular stage of Step 2 is not allowed,
we still consider ourselves to be in a new configuration. A new configuration
means that every particle has to be subject to a single attempted displace-
ment even if some of the displacements are not, allowed. We shall distinguish
between configurations and realizations. Every N, configuration is called a
realization. Thus between two realizations, every particle has been displaced
--- PAGE 437 ---
§3.1 Metropolis Monte Carlo Technique 417
an average of N,A; times where A, is the acceptance rate.

Step 5: Count the frequency of occurrence of different pair separations.
For cach configuration so reached, we will count, Chir), the number of
particles of size aj having their centers located in a spherical shell with inner
radius r and outer radius r + dr, where r is measured from a tagged particle
J of size a; during the simulation cycle of realization t. The subscripts i and j
are indices of particle sizes, the superscript J is for labeling the particle, and
the superscript ¢ is the index of realization. These tabulations are carried
out for a number of divisions of r between Rj; and 5Rj;, where Rij = a; +a;-
The thickness of the spherical shell dr will then be the smallest length over
which the pair distribution functions are resolved.

The above process is repeated for a large number of times to gener-
ate many different realizations and to record the frequency of occurrence of
different pair separations. Thus, the average number of particles of size a;
contained within a spherical shell of thickness dr at a distance r from a par-
ticle of size a;, averaged over all particles of size a; and total T realizations,
can be expressed as

iid Nv.
(Cis) = aE YY citer) (8.3.6)
“ t=1 [=I
On the other hand, if the particles were totally uncorrelated, the average
number of particles of size aj in the spherical shell surrounding a particle of
size a; at a distance r away would be
(Cij(r))une = MONO) ra (8.3.7)
Nj
where une stands for uncorrelated, 4ar*dr is the volume of a spherical shell
of thickness dr, and 6; ij is the Kronecker delta function which corrects the
inability of the tagged particle to be in the spherical shell. The pair distribu-
tion functions gj;(r) are then calculated from (8.3.6) and (8.3.7) by means
of the relation
(Cy(r)) Ny Scl  (g3s

957) = CSc TNing (Ny 6) Gavdr) >> 3 (838)
Generally, a pair of particles is considered to be uncorrelated when their
separation is greater than 52j;, and the values of pair distribution functions
gij(r) are taken to be unity for r > 58j;. The pair distribution functions
vanish, gij(r) = 0 for r < Rij, due to the non-interpenetrable characteristic
of macroscopic spheres.
--- PAGE 438 ---
418 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
3.2 Sequential Addition Method

> **3.2 顺序添加法**

The simulation of random distribution of particles using sequential addition
method is different from the Metropolis technique in that the realizations of
discrete random media are constructed by depositing spheres one by one into
the box subject to the same condition of no overlap with all other particles.
Thus, in the sequential addition method the particles do not move, and there
is no shuffling of particles. The procedures adopted are as follows.

Step 1: Generate a random test site to accommodate a new particle. The
x,y, and z coordinates of this trial position within the cube are determined
by three independent random number generators as

T= y= 256 (8.3.9)
where ¢;, i = 1,2,3 are random numbers uniformly distributed in the range
(0, andO<a,y,2< 6

Step 2: Check the separation of trial site from those particles already
established in the primary cell. A new particle will be left on the test position
if it does not overlap with any other particles; otherwise it is rejected and
the procedure goes back to Step 1 to gencrate another test: site.

Step 3: Introduce the next particle and return to Step 1. The additional
sphere is joined one at a time to the group of particles until all N particles
are filled in the primary cell.

Step 4: Count the frequency of occurrence of different pair separations.
This step is the same as Step 5 of the Metropolis technique.

The above process is repeated to generate many different realizations.
The procedures for obtaining the pair distribution functions are as in equa-
tions (8.3.6)- (8.3.8) for the Metropolis method.

3.3 Numerical Results

The Monte Carlo techniques are used to generate the random distribution
of particles of multiple sizes and to obtain the pair distribution functions
gij(r) from the computer generated samples. The Monte Carlo simulation
results of pair distribution functions are compared with those under Percus
Yevick approximation. For the computer experimental results shown below,
a unit cell, £ = 1, containing spheres with different, sizes was chosen as our
model system. The numerical results of pair distribution functions using the
Metropolis technique are illustrated in Figs. 8.3.1-8.3.6, and the simulation
results using the sequential addition method are shown in Fig. 8.3.7. In all the
figures except Figs. 8.3.2 and 8.3.7, we have used T = 3000 configurations
--- PAGE 439 ---
§3.3 Numerical Results 419
28 : ms es
{ a = si |
1 ~~ f20.3(PY) |
H °  f=0.2(MC)
ar ¢ 5 #=0.3(MC)| ~
| 4
4 BT
s| ‘
a
Figure 8.3.1 Pair distribution functions g(r) for media with particles of single size as a
function of r normalized by 2a. The simulation parameters are (i) N = 400, f = 0.2, A=
0.06105 and (ii) N = 600, f = 0.3, A = 0.02757. ‘The data points are Metropolis Monte
Carlo simulation results, and the curves are obtained from Percus  Yevick calculations.
and, assuming N, = 1, also 3000 realizations. The choice of displacement
A is dictated by the following considerations. The choice of maximum dis-
placement A in the Metropolis technique for each movement will affect the
percentage of accepted displacements. If A is too big, almost all the dis-
placements will be rejected, so the ensemble of system realizations will be
composed of nearly the same configurations repeated many times and pro-
vides very little new information at each step. On the other hand, if A is too
small, the displacement of a particle is always accepted, but the configura-
tion changes very slowly and gives inefficient sampling in the configuration
space. The size of A has been adjusted by trials to give about 30% to 70%
acceptance of the new position.

In Fig. 8.3.1 the pair distribution functions are shown for systems with
particles of identical size for two cases: (i) f = 0.2, N = 400 and (ii) f =
0.3, N = 600. The pair distribution function g(r) is at its maximum at the
separation equal to one diameter of particle, which shows a strong likeli-
hood that the particles will clump together in a dense medium. The pair
distribution function behaves more oscillatory and has higher peaks for the
case of larger concentration of particles. The result also shows that the pair
--- PAGE 440 ---
420 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
25 _—
| —  PercusYevick |
© Monte Carlo
\ Loe!
2 7
|
_ 8
g | a
&
1 ail cea aaa
os-
o es . 1 en |
0 o5 4 15 2 26 3 98 4 45 6
tia)
Figure 8.3.2 Pair distribution function g(r) for media with particles of single size as a
function of r normalized by 2a. The simulation parameters are f = 0.25, N = 4000, Ne = 10
configurations per realization, and T = 30 realizations. ‘The simulated results are compared
with Percus-Yevick calculations. The acceptance rate Ay is 42.5%.
distribution function asymptotically approaches unity as the interparticle
distance increases. The PY results are in good agreement with Monte Carlo
simulations.

In Fig. 8.3.2 we consider a volume with f = 0.25 and N = 4000. We
take NV, = 10 configurations before we obtain a realization, but we take only
T = 30 realizations. The simulated pair distribution functions, as shown in
the figure, still compare very well with the Pereus- Yevick approximation.
This example shows that the number of required realizations can be small if
the number of particles is large.

In Figs. 8.3.3 and 8.3.4 we illustrate the results of pair distribution func-
tions for a medium with particles of two different: sizes. For Fig. 8.3.3 we
placed N = 558 spheres inside a unit cell in which N; = 486 of them are
smaller particles and N2 = 72 are larger in size with az = 1.5a,. The vol-
ume fractions for cach size are f; — 0.16 and f = 0.08, respectively. In
Fig. 8.3.4 we consider a system having a higher concentration of particles
with a larger size ratio, but with a smaller number of larger particles. The
model parameters are N = 816, Ny — 768, Nz = 48, az = 2a), fi = 0.2,
and f2 = 0.1. In Figs. 8.3.5 and 8.3.6 the pair distribution functions are for
--- PAGE 441 ---
§3.3 Numerical Results 421
28 pe
| — #2ey|
| = gt2(PY))
\ | ~~ + gii(PY)
2 bh © g22(MC)
the | = gt2(MC)
Rl 4 a gt1(Mc)
st eed
z AAA
B YAR AY
oN
rt |
> Os 1 cy 2 25 3 35 4 4s cy
12a)
Figure 8.3.3 Pair distribution functions gj;(r) for media with particles of two different
sizes as a function of r normalized by 2a). The simulation parameters are N = 558, Ny =
486, Ny = 72, a2 = 1.5a1, fi = 0.16, fo = 0.08, and A = 0.04498. The data points are
Metropolis Monte Carlo simulation results, and the curves are obtained from Pereus- Yevick
calculations.
35 a
—— gary) |
a - a1ayy| |
le= gt1(PY)
° Feri
fb > a g12(MC)
it = gittc)
2 you |
= RRA
BS A Fh
1s rh kia |
' ay
| y of.
v ' , ws Doe
ose f
ee
rr
(2a)
Figure 8.3.4 Pair distribution functions gij(r) for media with particles of two different
sizes as a function of r normalized by 2a). The simulation parameters are N = 816, Ny =
768, Nz = 48, a2 = 201, fi = 0.2, fo = 0.1, and A = 0.03169. The data points are
Metropolis Monte Carlo simulation results, and the curves are obtained from Pereus-Yevick
calculations.
--- PAGE 442 ---
422 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
3 ' —
—— g34PY)
a so g2a(PY)
== gt3(PY) :
g22(PY)
25 hk . g12(PY)
ath : - g11(PY)
recut © g33(me)
2 rath & + g23(MC)|
4 att ~ — gi3(Mc)
5 ahhh | g22(MC)
5 a 2% gta(Mc)
| 1 NB © git(Mc)
1 ONL S -
1 4
eS
o5| !
4
7 ! - a ___}
os SS
nat)
Figure 8.3.5 Pair distribution functions g,;(r) for media with particles of three different
sizes as a function of r normalized by 2a1. The simulation parameters are N = 481, Ny =
324, No = 125, Ngj = 32, ag = 1.5a1, a2 = 1.2a1, fr = 0.15, fo = 0.1, fg = 0.05, and
A = 0.03167. The data points are Metropolis Monte Carlo simulation results, and the curves
are obtained from Percus- Yevick calculations.
a mixture of three particle sizes with ag > a2 > a1. The particle sizes and
volume fractions are (i) ag = 1.5a,, a2 = 1.20, f; = 0.15, fo = 0.1, and
fs = 0.05 in Fig. 8.3.5 and (ii) @3 = 2a). ag = 1.24). fy = 0.12. fo = 0.09,
and fz = 0.05 in Fig. 8.3.6. We observe that it usually requires more par-
ticles in the simulation processes to obtain better results when the ratios
of particle size are increased. The maxima of pair distribution functions for
multiple size cases are at the separation equal to the sum of the radii of
two particles. Thus gij(r) is maximum at r = a; + aj. We note that gi;(r)
exhibits the most oscillation when both i and j are of the largest size, while
there is less oscillation in g;;(r) for smaller sizes. This shows that in a dense
medium with particles of different sizes. the larger particles show stronger
correlation and less freedom than smaller particles in positioning themselves
in the presence of all other particles. Generally, the features of the function
of giz are between gi and gj;. The results in Figs. 8.3.3-8.3.6 are in good
agreement with the Percus-Yevick approximation.

In Fig. 8.3.7, we use the sequential addition method to generate random
distributions of particles and re-examine the cases of the particles of same
size for (i) f = 0.2, N = 400, and (ii) f = 0.3, N = 600. The simulated pair
distribution functions obtained are averaged over J’ = 30 realizations. The
--- PAGE 443 ---
§3.3 Numerical Results 423
35 =a
; =
—  983(PY)
3 ~=  g2a(PY)
os g13(PY)
g22(PY)
ose if + gta(Py)
tok ~ = gtt(Py) |
sh © g33(c)|
_2 oe OR ' 923(MC)| -
= wee EE | x gt3(Mc)
5 a ve = gee(Mc)
13 yor Ye joa g12(MC)
cS, a ° 11(MC)
1 “ : i git y
' ' ag BOQ OS
mo OS °
os :
Latics
o 08 4 15 2 25 3 38 4 a5 5
(2a)
Figure 8.3.6 Pair distribution functions gj;(r) for media with particles of three different
sizes as a function of r normalized by 2a;. The simulation parameters are N = 1284, Ny =
864, No = 375, Nz = 45, ag = 2ai, ag = 1.20), fy = 0.12, fo = 0.09, fs = 0.05, and
A = 0.03213. The data points are Metropolis Monte Carlo simulation results, and the curves
are obtained from Percus-Yevick calculations.
7 — : os,
. — fo2apy) |
| i == #20.3(PY)
4 £=0.2(MC)
ab nh a $20.9(MC))
i
A |
mAh
Ba
» i |
= | &
5 % |
Yeo |
i
os} i |
fc
Ce ee Ya eC Cr
(2a)
Figure 8.3.7 Pair distribution functions g(r) for media with particles of single size as a
function of r normalized by 2a. The simulation parameters are (i) N = 400, f = 0.2 and
Gi) N = 600, f = 0.3, and 7’ = 30 realizations. The data points are Monte Carlo simulation
results using sequential addition method, and the curves are obtained from Percus- Yevick
calculations.
--- PAGE 444 ---
424 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
simulated pair distribution functions compare well with the Percus—Yevick
approximation. This example shows that both the numbers of required re-
alizations and the number of particles may be small if using the method of
sequential random addition.

Both Metropolis shuffling approach and sequential deposition method
have been used to create ensembles of randomly distributed spherical parti-
cles. Generally speaking, Metropolis method is a good candidate for creating
high volume fraction configurations. Because of the rising rate of overlapping,
the sequential deposition method will become difficult by depositing parti-
cles one by one into the test volume when the density of particles becomes
higher (> 30%).

4 Sticky Particles
Tn this section we consider particle with surface adhesion. This means that
when the particles are randomly packed together, they have a tendency to
form clusters and bonds with each other. This is an appropriate model for
certain types of geophysical media and composite materials. For example,
terrain snow consists of ice grains that form bridges as metamorphism occurs.
The clustering potential is modeled in the Percus—Yevick pair distribution
formulation with spheres displaying surface adhesion. The adhesive force is
parameterized using a variable 7 which governs the degree of clustering. The
structure factor has a closed form analytical solution.
4.1 Percus—Yevick Pair Distribution Function for Sticky Spheres
We shall consider a system consisting of non-penetrable, spherical particles
of diameter d with a non-zero surface adhesive force, i.e. sticky hard spheres
(SHS). In this model, the interaction between two particles is of very short
range, with the nature of surface adhesion, and it is strong enough to bind the
two particles when they contact each other. The SHS model is characterized
by an interparticle potential, u(r), given by:
co for0<r<s
12r(d-s
u(r) = 9 In ane) ) fors<r<d (8.4.1)
0 for r >d
A limit is taken in which the range of interaction becomes infinitesimal and,
simultaneously, its well depth infinite, in such a way that
d
lim(d ~ sje") = — < 8.4.2
lim(d ~ s)e 127 ~ (8.4.2)
--- PAGE 445 ---
§4.1 Percus-Yevick Pair Distribution Function for Sticky Spheres 425
with d and 7 being held fixed. The parameter 7 in (8.4.1) is dimensionless,
and its inverse is a measure of the attraction or stickiness between parti-
cles. The case of r~! = 0¢ corresponds to infinite stickiness and 7! = 0
corresponds to non-sticky particles.

The total correlation function h(r) between a pair of particle is as in
(8.1.3). The direct correlation function c(r) between a pair of particles, which
is short-ranged, is related to h(r) by means of the Ornstein-Zernike relation
as in (8.1.5a).

Under the Percus-Yevick (PY) approximation, when the potential u(r)
vanishes, so does c(r), thus:

e(r)=0 for r>d (8.4.3)
Also, since the particles are non-penetrable, the pair distribution function
g(r) is zero when r < s. Hence, h(r) = —1 as r < s, The behavior of function
A(r) is more complicated in the region s < r < d. It can be seen from (8.4.1)
that h(r) will have a delta-function singularity when s > d. In this limit, we
have
n(r) 1+ A445 d) for0<r<d (8.4.4)
ur) =— TOT 0) 4.
127 ns
td
g(r) =A(r) +1 = ahr -d) for0<r<d (8.4.5)
Qr
where / is a dimensionless parameter to be determined later. The parameter
{ tends to zero in the limit 7~! = 0. The PY approximation of the pair
distribution function for the sticky hard spherical particles can be solved
analytically using the factorization method of Baxter {1968a,b].

The Ornstein-Zernike relationship can be Fourier transformed to obtain
a convenient algebraic equation:

1—noC(p) = {1+ nH (p)}! (8.4.6)
where no is the number of particles per unit volume. H(p) and C(p) are
respectively the 3-D Fourier transforms of h(F) and c(7), i-e.,

H(p) = | dre? (7) = (20) H(p) (8.4.7)

(p) = / are? Te(F) = (2n)°C(p) (8.4.8)

According to the Wiener-Hopf technique due to Baxter, the left-hand side
of (8.4.6) can be factorized into the form

1 ~ nC(p) = Q(v)Q(—P) (8.4.9)
--- PAGE 446 ---
426 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
where Ql) is defined by
7 d
Q(p) =1- ane [ dre”™Q(r) (8.4.10)
0
Here Q(r) is a real function, and Q(r) = 0 for r > d. Explicit relations
between Q(r) and c(r) and h(r) can be obtained by substituting (8.4.7)-
(8.4.8) and (8.4.10) into (8.4.6) and (8.4.9), and taking the inverse Fourier
transforms. It is found that [Baxter, 1971]
Ad
re(r) = —Q'(r) + 2am i dxQ'(x)Q(x —r) (8.4.11)
for 0<r<d, and
d
rh(r) = -Q'(r) + aan, [ dx(r — x)h(\r — x|)Q(2) (8.4.12)
0
for r > 0, where Q'(r) is the derivative of Q(r).
For sticky particles, using (8.4.4), (8.4.5), and (8.4.12), in the range
0 <r <d, gives rise to the closed-form expression for Q(r).
re
Q(r) = AS + Br+D (8.4.13)
where
142f-—p
AS os 8.4.14
a7 Ga)
(-3f + wd
Bait 8.4.15
2-7? G41)
& td?
D=-AS - Ba+ = (8.4.16)
f= E not (8.4.17)
6
n=tf-f) (8.4.18)
The direct correlation function ¢(r) can be evaluated from (8.4.11) by using
(8.4.13). The explicit expression of 1 — ngC(p) in (8.4.9) is
ra f 3f ate
1 = noC(p) = T-f L-tf+ T-f @(X) + [8 — 41 ~ f)] YX)
2 2
+ cox} + {: fy [X&(X)] + cnx} (8.4.19)
--- PAGE 447 ---
§4.1 Porcus-Yevick Pair Distribution Function for Sticky Spheres 427
where X = pd/2 and
sin X
W(X) = xX (8.4.20)
sinX cosX
O(X)=3 ees - | (8.4.21)
For a given volume fraction f and stickiness parameter 7, the parameter t is
determined by solving the quadratic equation
fp f 1+f2
st -|r+— J) t+—-5 = 0 8.4.22
3 1-7) '* 0-7 eae)
When 7 is greater than a value
2-2
te = aoe (8.4.23)
there are two real solutions for ¢ throughout the permissible fractional volume
range 0 < f < 1. Below this value there exists an intermediate range of
volume fractions within which there are no real solutions for 1, Moreover, a
further condition to determine the solution of ¢ is that Q(0) must be positive,
or
w<l+2fF (8.4.24)

The procedure for calculating the pair function is as follows. Given the
particle diameter d, particle concentration f, and particle stickiness 7, the pa-
rameter ¢ is first determined from (8.4.22) (8.4.24). By using the parameter
t and Eqs. (8.4.19) (8.4.21), C(p) can be computed. Next, H(p) is computed
by solving (8.4.6). Then h(r) is obtained by taking an inverse Fourier trans-
form of /7(p) according to (8.4.7). Finally, the pair distribution function g(r)
can be calculated from h(r) + 1.

In Fig. 8.4.1, the pair distribution functions are shown for systems with
sticky particles of identical size, 7 = 0.2 and r = 0.5, and compared with the
non-sticky case for f = 0.3. In the figure, we do not include the Dirac delta
functions of (8.4.5). The major features for the pair distribution functions
of sticky particles are the occurrence of discontinuities when the particle
separation equals one and two diameters. The discontinuity at r = d arises
because the particles cannot penctrate each other. The height of the peak
at r = d grows rapidly with the increase of particle stickiness while the
width of this peak is reduced. This shows a stronger connectedness between
particles as particles become more sticky, and other particles are more likely
to be excluded from the region d < r < 2d. Therefore, in a dense medium
with sticky particles, the sticky particles tend to aggregate together. The
--- PAGE 448 ---
428 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
in oo]
2 thcos
23s, |
fo |
ws
1 Se ce
nee |
.{
do _|
ea eT re
1/(2a)
Figure 8.4.1 Percus- Yevick Pair distribution function for sticky spheres with 7 = 0.2 and
7 =0.5, and for non-sticky spheres, Fractional volune is f = 0.3.
gr
| Em ]
| == 1204 |
a | |
ia |
Sis
| ;
| Aa
a |
°% 5 1 1s 2 25 3 35 4 as 5
(2a)
Figure 8.4.2 Percus-Yevick Pair distribution function for sticky spheres with f = 0.2 and
f =0.4 and stickiness 7 = 0.2.
--- PAGE 449 ---
§4.2 Pair Distribution Functions of Adhesive Sphere Mixture 429
25 |
\ -- t=01) |
— 1=05|
a \ --- t35
\ —_ J
\
ih \
sy \
o \
oS { \
& o8- \
HOON |
-05+ NS me ae 4
see ge
° 1 2 3 4 5 6
pd
Figure 8.4.3 (27)3ngH(p) as a function of pd for tT = 0.1, 0.5 and 5.
discontinuity at r = 2d arises from the fact that for r > 2d, the integrand
in the integral of (8.4.12) does not include the contribution of the delta
function of (8.4.4) and (8.4.5), while for r < 2d, the delta function is included,
Physically, when the separation between the two particles is larger than twice
the diameter, the probability of these two particles being bound or connected
to a third particle drops to zero. In Fig. 8.4.2, the pair distribution functions
are plotted for f = 0.2 and f = 0.4, with stickiness r = 0.2. For higher
concentration of sticky particles, the pair distribution function displays more
fluctuations just as the case of non-sticky particles. In Fig. 8.4.3, we plot
no(2m)3H (p) as a function of pd for f = 0.3 and for 7 = 0.1, 0.5 and 5. We
note that for large pd, the values of the three curves are comparable. For
small pd, they are very different, with no(27)?H(p) positive for small 7 and
negative for large r.
4.2 Pair Distribution Functions of Adhesive Sphere Mixture
In this section, the model of spherical particles with identical size and inter-
action is extended to be polydisperse with respect to both sizes and inter-
actions. Consider an M-component mixture system of spherical particles of
diameter d;, i = 1,2,...,M!, with the interparticle adhesive potential ui; (r)
--- PAGE 450 ---
430 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
given by:

0° for0<r <a

12 -
uy(r) = lim 2 In 1rd =O) toe oy, <r < diy (8.4.25)
ists di;

0 for r > di;
where the limit is taken with dj; and 7j held fixed, and dij = (d;+d;)/2
is the cross-term hard sphere diameter. The parameter 7; in (8.4.25) is
dimensionless, and its inverse is a measure of the attraction or stickiness
between particles of species i and j. The case of Ti) = oc corresponds to
infinite stickiness and T;) = 0 corresponds to non-sticky particles.

Under the Percus -Yevick (PY) approximation, the direct correlation
function ¢;;(r) and the total correlation function /;;(r) are respectively ap-
proximated by

ey(r) =0 for r > di (8.4.26)
ti; di .
hg(r) = -14+ 2 b(r-dij) — forO<r<dy (8.4.27)
127;
The parameters ¢;; in (8.4.27) can be obtained by solving the following sys-
tem of M(M + 1)/2 coupled quadratic equations
M 2
Boo big d
tyty = At + G > Moy Hala) (8.4.28)
where nq is the number density of a species particles, si; = (dj—d;)/2, and
A , tyjd?,
a(t) = 5 (7? — dh) + bil ~ dy) + a (8.4.29)
1 - & + 3digo Xi
A= mba _ Ai 8.4.29b
‘ (1 ~ &3)? (1—&) ( )
3d7E2 a Xi
B=- he 4 St 8.4.29¢
* 2(1= 3)?" 21 = &) J
molt
q ,
X= FY natiadad (8.4.29d)
a=l
net
f= BD Malda)! (8.4.29¢)
o=t
with yz = 0,1, 2,3. Insertion of (8.4.29a) (8.4.29e) into (8.4.28) yields
--- PAGE 451 ---
§4.2 Pair Distribution Functions of Adhesive Sphere Mixture A431
1-&  3didj>
tyTig = —— a + BD
wy 1-8)? © (1 &)?
M
mdj(1— &3) 2
oo tye (dj + da)*d,
WC — &)2(d, +a) Natya (dj + da)"da
ad, af
2 ta (ds +d.)
oa yard) Natia (dj + do)"do
© M
y 2 2 AS
‘Hee » Natia tia (dj +da)*(di+da)? (8.4.30)
oF
which is useful in solving the parameters (;;.
The PY approximation of the pair distribution function gjj(r) = hij(r)+
1 for sticky spherical particles can be solved analytically using the factoriza-
tion method of Baxter [1968a,b]. The multi-species Ornstein-Zernike (OZ)
relation, as in (8.2.2), can be Fourier transformed to obtain a convenient
algebraic equation H(p) = C(p) + C(p) - H(p). The matrix elements Hj;(D)
and Cij(p) are
Hiy(B) = (riny)!”? / oF PFhi(P) (8.4.31)
(0) = (many) far ees) (8.4.32)
Because of the spherical particle assumption, the transform only depends on
p = |p|. The Wicner-Hopf technique can be used to factorize the transformed
OZ equation. The matrix elements Cij(p) are
w 2a: 3d? ji(xs)
—Ci;(p) = BVM; COS; [-sidta Joli) + G=&)n
4 3djd} jo(wi) _ 6Byd} Ae)
(1&3) djxj
T ; 343 ji(x;)
— igh; cos; |—tiyd?.d; jo(s ad
+ a TNF OSX; 1g jy dy do(z;) 4 a ~&)e)
3did? Jo(z;) 6 Bid? ii(a;)
pS ON ED
(1 — 3) dx;
+ a Rn; sine Bye u(x) Huai) + sins, Bdid u(y) a (3)
ov ee) OG)
--- PAGE 452 ---
432 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
‘ Gps Vai 9dpdd? jy (xs) 1 (a3)
= ny fiqng § ———
w/t “ (1 ~ &)
3d} j1(xi)
+ |-tidj.d; jo(xi) +
[-rit Jon) + FOE
4 3dd} Jo(wi) _ 6Byd} AG)
(1— 3) dyer;
P 3d} ji(x;)
+ |-tyd?d, jo(as) +
15414; Jo(x;) (1 -&)e;
3did} jo(xj) 6 Bid} jr(xy) oe
+ + (8.4.33)
(1-&) dy;
where
pd, ‘
nay (8.4.34)
. sin 2, .
jo(xi) = —— (8.4.35)
vy
. sing; cosa; .
x)= —- > 8.4.36
Ji) zB 7 (8.4.36)
‘The procedure of calculating the pair function is as described in Section 8.2.
First C,;(p) is calculated from (8.4.33). Next, H(p) is computed by solving
the linear matrix equation (8.2.7). Then hj;(r) is obtained by taking an
inverse Fourier transform of H(p) according to (8.4.31). Finally, the pair
distribution function g,;(r) can be calculated by using (8.2.1).

In Fig. 8.4.4, the pair distribution functions for a binary mixture of
adhesive spheres are illustrated with a2 = 0.6a,, f; = 0.1, fe = 0.15, and
Ti = Ti = To2 = 0.2. We note that, besides the discontinuities at the particle
separation equals to the sum of two particles’ radii, the discontinuities of
the pair distribution functions also occur at other particle separations which
depend on the various co-linear arrangements of three particles. For example,
the arrangement of a larger sphere between two small spheres gives the
discontinuity at r = 1.6d,, while the arrangement of a larger particle with
two consecutive small spheres gives the discontinuity at r = 1.4d,. Because
of the symmetry relation gi; = gji, only three pair distribution functions
are illustrated. The pair distribution functions for another case of binary
mixture of adhesive spheres are shown in Fig. 8.4.5 with ag = 0.4a1, f; = 0.2,
fo = 0.04, and 7 = 1, M2 = 0.2, and 722 = oo. For this case, since the
particle species 2 is non-adhesive, there is no discontinuity at r = 0.8d,.
--- PAGE 453 ---
§4.2 Pair Distribution Functions of Adhesive Sphere Mixture 433
6-4 - : —
it — git
“I it =~ gi2|
tot -- ge
1s ot
i) ‘
'
nal i) : }
it an] /|
uy ta ad |
S on ltd A
gy bo ‘
3 H 4
} ]
°° ' FM enaf a /
' n
« OY
ot
Mt
o7| '
' 1
\ oy i
ost rt 4
0 05 1 13 2 25 3
dt
Figure 8.4.4 Percus Yevick pair distribution function for a binary mixture of sticky spheres
with ag = 0.601, fr =0.1, fo = 0.15, and 711 = T19 = 722 = 0.2.
14
7
' —~ a
( ‘ : = gta)
13 | ' -+ + g22
‘
' I
12 t
; ‘
' ' |
Bat ‘ t 4
3" ‘
a
L 1 \a N Ane —
1 : eA / 2 i
: Se —
1 ' I
oa] : '
' '
{ \ \ [
98 oO 1s )”CO 25
tid1
Figure 8.4.5 Percus-Yevick pair distribution function for a binary mixture of sticky spheres
with ag = 04a, fr = 0.2, fo = 0.04, and 711 = 1, 712 = 0.2, and 122 = 00.
--- PAGE 454 ---
434 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
4.3 Monte Carlo Simulation of Adhesive Spheres

> **4.3 粘附球的蒙特卡洛模拟**

The Metropolis shuffling technique as described in Section 3.1 is usually
employed for particles without surface adhesion. This conventional method
generates new configurations by giving random displacements to particles
and then accepting or rejecting the configuration based on particle overlap.
However, this method cannot be directly applied to particles interacting via
the adhesive potential as given by (8.4.1). By taking the limit, s — d in the
exponential of (8.4.1), we have
Oe { tho(r—d) forr<d (8.4.37)
1 forr>d
here d is the particle diameter and 7 is the stickiness parameter related to
the adhesion strength. Thus, the adhesive potential (8.4.1) implies that there
exists a finite probability of contact, proportional to d/(12r), for adhesive
particle pairs. As 7 decreases, the adhesion strength increases, and favors
more the formation of clusters. This feature cannot be captured by using
the shuffling technique since it is very unlikely to sample any surfaces of
other particles while each particle is displaced in a three-dimensional space.
In order to explore the available contact states of adhesive particles,
Seaton and Glandt [1986, 1987] and Kranendonk and Frenkel [1988] have
developed alternative sampling procedures which allow a particle to break or
form bonds with other particles during its Monte Carlo displacement. They
have considered only transitions between four binding states a = 0,1,2,3,
corresponding to the unbounded, single-bond, double-bond, and triple-bond
configurations, respectively. The a-bond state indicates that a particle is in
contact with a number of other particles. The maximum number of bonds
is 12. The binding states a = 0,1,2,3 of a particle, represented by a filled
circle, are illustrated in Fig. 8.4.6. We will describe the Kranendonk-Frenkel
algorithm in this section for the three-dimensional simulations of adhesive
particles. The description of Seaton-Glandt algorithm will be given in Chap-
ter 9 for the two-dimensional simulations.
In the Kranendonk-Frenkel algorithm, a total effective volume vo is
assigned to the a-bond state of the test particle k as given by
(c ad \* 4
vo = 3 (i) | da: (8.4.38)
where dg; represents all degrecs of frecdom of the test particle k, remaining
after making the a bonds. The summation in (8.4.38) is over all possible
combinations of the test particle with all the other particles that can realize
the type of a-bond. Possible excluded volume effects are ignored in com-
--- PAGE 455 ---
§4.3 Monte Carlo Simulation of Adhesive Spheres 435
~~
‘ : )
au ED
(a) (b)
—~ ™
Og Ref
= \
tii
HED —
ney a,
(c) (dy
Figure 8.4.6 The particle binding states: (a) unbounded, (b) single-bond, (c) double-bond,
and (d) triple-bond.
puting the integral in (8.4.38). The effective volume yo represents a direct
measure of the probability of the a-bond configuration, with a contributing
factor (7).
The total effective volume associated with the unbounded state of a test
particle k is
VO =v (8.4.39)
which is simply the total volume available to the test particle, including
overlapping regions. Next we examine the single bond (Fig. 8.4.7a). Let r be
Qn pr
the distance between particle i and test particle k. Then | i] r? sin 6d0d@
o Jo
is the surface area that the center 7; of particle k can be located such that
particle & is attached to particle i. The total effective volume of the single-
bond state of a test particle k is
N Qn pr
(i) d 2.
A = 1 (5) | | r° sin dédd
wre 127) Jo Jo
Xai d
=> of = (1) (5) na?) (8.4.40)
" 127
itk
As shown in Fig. 8.4.7a, the test particle k can be placed anywhere on
the surface of another particle i. Thus, as indicated in (8.4.40), ot is the
effective volume associated with the single bond between particles k and i.
yoni (4 2 4
ut = (i And (8.4.41)
--- PAGE 456 ---
436 8 PARTICLE POSITIONS FOR. DENSE MEDIA CHARACTERIZATIONS
on am ? ~
Wouny Ace | AGB»
4 Cee
T= i + Ay Tig
(a) (b)
GED
i
ES ci)
La Cy)
(c)
Figure 8.4.7 The effective volumes of the binding states of a test particle k: (a) single-bond,
(b) double-bond, and (c) triple-bond.
The total effective volume of one bond is then cqual to the surface area of a
sphere with radius d times ie and (N — 1), excluding the displaced particle
itself.

Next, we consider VO for the double-bond state of a particle. From
Fig. 8.4.7b, r is the radius of the circle on which the center of the test
particle k can be placed. This circle is formed by all points that have a
distance d form both particles i and j. Thus the total effective volume of the
double-bond state associated with the test particle k is given by

N 2 p2
‘ d al
v2) = oa rd
ef > 127) Jo ?
i<j
ijg¢k
N 2 pe [TT
d rij \?
-y (4 | je- (2) ao
7 127 0 2
icy
ijek
N ( , d 2 N 7; 2
= ij _ ( © 2 (2 9
= Yoh = (i) So amd (@) (8.4.42)
i<j i<j
jek igAk
here 0? is the effective volume for the double-bond configuration of the
--- PAGE 457 ---
§4.3 Monte Carlo Simulation of Adhesive Spheres 437
particle k with particles 7 and i.
2

v2 = (Gs) Qn) a2 — (BY (8.4.43)
Note that Qt =0 when rj; > 2d. This is because particle k can not form
a double-bond with particles i and j simultaneously when their distance is
greater than two diameters. The effective volume for a triple-bond configu-
ration of particle k with particles i, j, and / is

aut _ (4) ! ad

= (i) tage Gra)
and the total effective volume of the triple-bond state of the test particle k
is given by

®) N a\3 1

3) _ of 5

Ver > (a) leix » (jx x @x)| (6445)
ijk

where jx, €jx, and €, are unit vectors along the directions joining the center
of particle k to the centers of particles i, j, and J, that form a triple-bond
with particle k. A necessary condition is that the diameter of the inscribed
circle within the triangle, whose vertices are the centers of particles i, 7,
and J, must be be less than the diameter of the test particle k, as shown in
Fig. 8.4.7c.

The calculations of the total effective volumes Vio, a=0,1,2.3 of the
test particle & do not depend on its current binding state. In the trial move
of sticky particles, the final move consists of changing the binding state. The
binding state may change from its present 6-bond configuration to a new
@'-bond configuration. Thus, each move will involve a transition among zero
bond, single bond, double bond, and triple bond states. We calculate vo
and v2) by doing the following. We first make a list. of all pairs of particles
with which the test particle k can form a double-bond. This double-bond
list. is then used to compute the total effective volume vy according to
(8.4.42). From the list of pairs we further select those triplets that can form
a triple-bond with the test particle, and these possible triplets are used to
calculate the total effective volume V2) using (8.4.45). In this algorithm,
we let the test particle free to move over the entire volume, every particle,
except itself, is possible to form a single-bond with the test particle. Thus
the total effective volumes yo) and vp are constants during the whole
simulation process. The new binding state {' for the test. particle is selected
--- PAGE 458 ---
438 8 PARTICLE POSITIONS FOR. DENSE MEDIA CHARACTERIZATIONS
with the probability of
(3°)
P(s') = ai (8.4.46)

va

a=0
It is noted that the magnitude of P(’) depends on the binding structure of
the system prior to the particle k being moved.

The three-dimensional Monte Carlo simulation of adhesive particles be-
gins with N unbounded spheres randomly or regularly placed inside a cubic
box with no overlap. In the first stage, the Monte Carlo steps are similar to
the ones described in Section 8.3.1 for non-sticky particles. The spheres are
shuffled to create an initial realization. In the second stage, however, instead
of moving the test particle randomly within a small cube of side A to deter-
mine its trial location, the test adhesive sphere is displaced according to the
breaking of its current binding state and the formation of new binding state
with other particles. Thus the second stage consists of transitions among
binding states. If the test particle is found to bind with four or more parti-
cles, it will not be moved. If not, the attempt of changing the test particle’s
number of bonds is described in the following.

Before changing the test particle k’s binding state, we have to establish
a catalog of the current system’s binding structure, that is, to build the lists
of pairs and triplets as described above, and to compute the probabilities
P(") for 3’=0, 1, 2,3. A random number generator, between 0 and 1, is then
used to generate a random number and compared with the obtained P({’)
of the current system to decide the new binding state of the test particle.
Obviously, the transition involves all four states. If 3’ = 0 is favored, the
new location of the test particle is determined from three random numbers,
for its x, y, and z coordinates. If 3’—1, an integer random number # with
equal probabilities, i=1,2....,.N, i#k, is generated to select the potential
single-bond candidate particle. Random polar and azimuthal angles are then
generated to determine the location of particle k’s center on a spherical sur-
face of radius d centered at particle i (Fig. 8.4.7a). If ’=2, another random
number, between 0 and 1, is generated to select a candidate pair of particles
(i,j) from the double-bond list according to the following probability to form
a double-bond with the test particle k.

. pi
pif) = ty (8.4.47)
Vor
Another random angle between 0 and 27 is then generated to sclect the
--- PAGE 459 ---
§4.3 Monte Carlo Simulation of Adhesive Spheres 439
location of particle k’s center on a circle centered at the midpoint of the
vector 7;; joining the centers of particles i and j (Fig. 8.4.7b). Similarly,
when §’ = 3, a random number, between 0 and 1, is generated to select a
candidate triple of particles (i, j,/) from the triple-bond list according to the
following probability to form a triple-bond with the test particle k.

(3)igt

pi, 5.0) = od (8.4.48)

Vott
For the triple-bond, there are only two choices for the positions of particle
k, either above or under the surface containing the triangle formed by the
line segments connecting the centers of particles i, 7, and |. It is possible
that the new position of the test particle may overlap with one of the other
particles in the system. If not, we will accept the displacement and update
the coordinates of the displaced particle. Otherwise, reject the displacement,
and return the test particle to its original position. The calculation of total
effective volumes requires the maintenance of an updated catalog of the
system's binding configuration, so that we need to rebuild the pair-list and
the triplet-list whenever a trial move of the test particle is successful.

‘The algorithm is applied to a system of 300 sticky spheres of identical
size and stickiness. The volume fraction is f=0.3. The Monte Carlo results
are obtained by averaging over 10, 000 passes. Fig. 8.4.8 illustrates the Monte
Carlo results of pair distribution functions for particles with stickiness 7 =
0.5. A Comparison with Percus-Yevick (PY) approximation calculations is
also made in Fig. 8.4.8, which shows good agreements between these two
approaches. In Fig. 8.4.9, the particle sticky strength is increased to 7 =0.2.
Compared with PY approximation, a slight dephasing appears in the interval
d<r< 1.5d between Monte Carlo data and PY results. Moreover, another
discontinuity of the pair distribution function near r = V3d is predicted in
this case as discussed in the work of Seaton and Glandt [1987].

The effective volumes described in the Kranendonk-Frenkel algorithm
can be easily gencralized to the case of multi-species of adhesive particles.
Consider a system that has M-species of spherical particles of diameter dj,
i4=1,2,...,M, with the interparticle adhesive potential u,j(r) as given in
(8.4.25). Similarly, the effective volume ul associated with the single-bond
between particle k and particle i becomes

yi — Ge) ian rin @ dod@

of Nt) Jo Jo
= (34) An di (8.4.49)
© Tari J" a
--- PAGE 460 ---
440 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
14—— - yon re
| — PY
c MC)
13]
4
12 4
1
et 4 fi
4 é
4 4 g ta ROTI a Gi alti
N J ac be aS Re
f i
oa} 4 |
|
$s 1 15 2 25 3 35 4
(2a)
Figure 8.4.8 Pair distribution functions obtained from Monte Carlo simulations and
Percus-Yevick approximation for a system of single size sticky spheres with 7 = 0.5 and
fy = 0.3, The symbols are Monte Carlo simulation results and the curve is for Pereus Yevick
calculations.
ue —o
| =a
+al | “a MC
HG |
| y
14 6 e | |
wt i
4
cat
o7| 4
gh»
ts ; 15 2 25 3 35 4
(2a)
Figure 8.4.9 Pair distribution functions obtained from Monte Carlo simulations and
Percus-Yevick approximation for a system of single size sticky spheres with 7 = 0.2 and
fy = 0.3. The symbols are Monte Carlo simulation results and the curve is for Pereus-Yevick
calculations.
--- PAGE 461 ---
§4.3 Monte Carlo Simulation of Adhesive Spheres 441
where d;j,=(d; + d,)/2 is the cross-term hard sphere diameter, and 7;, is a
measure of the attraction between particles i and k. For the mixture case,
a factor ($4) contributes to the bonding probability that depends on the
distance and adhesion strength between particles of species i and k. Thus,
ul) " is not a constant, it depends on the types of two particles that form a
bond. The effective volume vu of the test particle k having a double-bond
with particles i and j is
dix Qn
ed = ati) (dite r dob
127%) \127;%) Jo
dix dix | on =
=(——J( = dix sin(cos* (éjx - é, d
(soe) (spec) [f° le siloos Mew -25))] a
= (#) (it) 9, [dix sin(cos!(@ix-@ij))]} (8.4.50)
arin) \ 127; 7
where the unit vectors @;; and éj, are along the directions connecting the
centers of particles i and j and particles i and k, respectively. The effective
volume yt of the test particle k forming a triple-bond with particles i, j
and L is
Oat ( dit ) ( dix ) ( das ) a (8.4.51)
of Larix) \ 12734) Lr / eam (Bix x ern) |
here @j, and @, are unit vectors from the center of the test particle k to
the respective centers of particles j and 1. The total effective volumes vo),
a=0,1,2,3, are then given by
vO av (8.4.52)
N d
(1) ik 2 -
Vi = > (3) 4nd (8.4.53)
i#k
) N d, dix
(2) _ tk ik \ ¢ ‘ alia. 3 4
Vip = » G =) (34:) 2m [dj sin(cos” (2x + ij))] (8.4.54)
agek
» fa d d 1
(3) _ ($4) (#4) (#4) _
y@) = ——--—_— (8.4.55)
oe > L2rie J 127} J \L2T J Nein (im x etx) |
ipl Ak
The particle displacement algorithm for the mixture of adhesive particles
is the same as that of the single species case. However, it is noted that the
--- PAGE 462 ---
442 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
15 : ———
1a toy ;—— git(Pyy | |
to g12(PY)
an = ge2(PY)
13) ey 4 git(MC)| ~
my © gi2(Mc)
12| oo | a 922(MC)|
1b an) & fs
eo it fs | Bn ak jah ad
ZB. ' Us
3 ' aegis
i &. ~
o3| ' fs, fa s 4
» tf nel {
es,
oa| a oars |
lear |
07] : -
+ of ]
\
05, —--—
0 os 1 15 2 35 3
dt
Figure 8.4.10 Pair distribution functions obtained from Monte Carlo simulations and.
Percus Yevick approximation for a binary mixture of sticky spheres with a9 = 0.6a,, f) =
O.1, fo = 0.15, and 7144 = m12 = 722 = 0.2. The symbols are Monte Carlo simulation results
and the curves are for Percus~Yeviek calculations.
iad 7 —_—
1 '— atten)
| 1 g12(PY)
13 ' ~~ g22(PY)
' ‘ ay) 4 gtt(Mc)
' me 2 gi2(Mc)
12 q t Cw 2 g22(MC)
t H 4
es VE
Su ' :
1 7 OA / 5 ener ‘sienna
ag| \
\
'
0a:-—-—— ’
) 08 n 15 2 2s
Wat
Figure 8.4.11 Pair distribution functions obtained from Monte Carlo simulations and
Percus~Yevick approximation for a binary mixture of sticky spheres with a2 = 0.4a1, fi =
0.2, fo = 0.04, and 711 = 1, 12 = 0.2, and 722 = o0. The symbols are Monte Carlo simulation
results and the curves are for Percus: Yevick calculations.
--- PAGE 463 ---
§4.3 Monte Carlo Simulation of Adhesive Spheres 443
Figure 8.4.12 Three-dimensional sample of computed generated sticky spheres with f =
0.35 and rT = 0.2.
single-bond effective volume of is not a constant but depends on the types
of two particles i and k that form such a single-bond. Thus, an integer
random number with equal probability between 1 and N — 1 is required
to select the candidate particle i (which cannot be the test particle itself)
according to the probability
yd
pi) = (8.4.56)
yo
elf
where v{f" is given by (8.4.49). Thus for the mixture case, we have to store
three arrays of probabilities, (8.4.56), (8.4.47), and (8.4.48), to select a can-
didate particle i, pair (i,j), and triplet (i, j,1) to from single-, double-, and
triple-bond, respectively, with the test particle.

In Figs. 8.4.10 and 8.4.11, we illustrate the Monte Carlo results of pair
distribution functions for a medium with adhesive binary mixtures of parti-
cles. For Fig. 8.4.10 we placed N = 1144 spheres inside a unit cell in which
N2= 1000 of them are smaller particles and Nj = 144 are larger in size with
az =0.6a,. The volume fractions are f; =0.1 and f2=0.15. They have the
stickiness with 711 = T12 = 722 = 0.2. In Fig. 8.4.11 we consider the case of
--- PAGE 464 ---
444 8 PARTICLE POSITIONS FOR. DENSE MEDIA CHARACTERIZATIONS
particles having different adhesive forces. This system has a high concentra-
tion of larger particles and a much less volume fraction of smaller particles.
The parameters are N = 885, N, = 200, No = 685, ag = 0.4a), fy) = 0.2,
f2=0.04, and the stickiness parameters are 711 =1, T12=0.2, and 72 = 00.
The Monte Carlo results for both cases are obtained by averaging over 12, 000
passes. In general, the Monte Carlo results are in good agreement with the
Percus—Yevick approximation calculations. In Fig. 8.4.12, we show a typical
configuration for a 3-D sample of sticky spheres with r = 0.2 and volume
fraction f = 0.35 [Zurk, 1995]. The generated realizations of random media.
can be used for the numerical solutions of Maxwell's equations.

5 Particle Placement Algorithm for Spheroids

> **第5节：椭球的粒子放置算法**

In this section we apply Metropolis shuffling process to generate the positions
and orientations of a system of densely packed spheroids. For nonspherical
particles such as spheroids, rotations need to be performed in addition to
displacements.

To simplify the simulation process, we consider N spheroidal particles
of the same shape that are randomly placed in a simple cubic cell. Periodic
boundary conditions are employed to minimize the finite size effect. A cen-
tral primary cell with side length L is set up to contain the N spheroids, and
this central cell is surrounded by the periodic images of itself. The state of
each spheroid is specified by the location # = (2, y, z) of its center and the
orientation Q = (0, ¢) of its symmetry axis. Given the particle concentration,
size, and shape, the N spheroids are initially aligned along the 2-direction,
and are placed in close contact with each other but without overlapping. In
such an initial set-up, we are able to create configurations of higher frac-
tional volumes. The shuffling process consists of a succession of trial moves
in which we attempt to change the locations and orientations of particles by
the combination of random displacements and rotations. For the spheroid j,
the new location Fr, is determined from its present location Fj by

vy = aj + Ane (8.5.1)
yl = 9; + Any (8.5.2)
2 = ay + Anz (8.5.3)
where A is the maximum displacement allowed in each spatial movement,
and 1z, Ny, and 7, are random numbers uniformly distributed between —1
and 1. Each spheroid has an axis of symmetry. We also perform random
--- PAGE 465 ---
§5.1 Contact Functions of Two Ellipsoids 445
rotation. The new orientation a of the particle is determined by
o, = 710 (8.5.4)
5 = 2mng (8.5.5)
where mg and ny are random numbers with magnitudes between 0 and 1.
5.1 Contact Functions of Two Ellipsoids

> **5.1 两椭球的接触函数**

During the course of simulation, in order to select the allowed new locations
and orientations of particles, we have to examine whether the trial moves lead
to overlap of spheroids. The checking of the overlap of spheroids is facilitated
by the use of a contact function. The contact function F4g(Fa,Q4,7B,Qz)
is defined for a pair of particles A and B centered at 74 and Fp, and with
orientations 24 and Qp, respectively. For two ellipsoids A and B, Perram
and Wertheim [1985] define a parametric function of the two particles as
FF, A) = AFa(F —Fa, 2a) + (1 ~ A)Fa(F — FB, QB) (8.5.6)
where \ is a parameter and F;(? —7;,9i), i = A, B, refers to an ellipsoid i
centered at 7;
a
FAP —F;,%) = (F— rs)" G; (Ms) (F— 7) (85.7)
with T denoting the transpose, and G; being the matrix
G.(Q)) = aja? + vb;5; + eal (8.5.8)
In (8.5.8), @ is the column vector denoting the direction of the @ vector
with the given oricntation Q;. Similar definitions apply to 6; and @. For
example (04,¢4) = Qa, then oN = [sind4 cos $4, sin 4 sin ¢4,cos@,]. Also
a;, 6:, and cj are the length of the scmi-axis @, 6;, and €;, respectively.
The matrix G; depends on the shape and orientation of the ellipsoid. G;
=-1
and G, are symmetric and positive definite. The parameter ) is restricted
within the interval 0 < A < 1, so that F(7,) > 0. For fixed A, the function
F(F,A) has a unique minimum as a function of 7. The contact function
Fap(Fa,Qa,7g, Og) is thus constructed in terms of the object function $(A).
Fap(Fa.Qa,7B, QB) = Ss 8.5.9
‘'aB(FA,Q4,7 5, OB) oma, ()} (8.5.9)
where
S(A) = min[F(F, A)] (8.5.10)
F
--- PAGE 466 ---
446 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
The contact function takes the values
<1. if Aand B overlap
_ _ =1 if A and B are externally tangent
Fan(Fa,Qa,7B. Qn) just touching each other (8.5.11)
> 1. if A and B are not overlapping
The minimization in (8.5.10) can be easily solved, which will be illustrated
in the next section. The maximization in (8.5.9) is carried out numerically
using the Method of Brent [1973].

This process of randomly moving and rotation, and checking overlap
is repeated for each particle inside the test volume. A single attempt to
change the state of each particle is called a Monte Carlo step (MCS). The
configurations used for the simulation of scattering have been selected at
intervals of 10°N MCSs apart. This is in order to establish a Markov chain of
configurations, thereby eliminating correlations among configurations. The
adjustments of random displacements and rotations are such that 50% of
the attempted Monte Carlo moves are accepted.

5.2 Illustrations of Contact Functions

> **5.2 接触函数的图示**

The contact function described in (8.5.11) plays an important role in the
Monte Carlo simulation for checking the overlap of particles. The paramet-
ric function F(F,A), defined in (8.5.6) for two ellipsoids A and B, has the
minimum of F(F,A) = 0 at F = Fg for A = 0, and it is F(F,A) = 0 at
F =F, for \=1. For 0 < \ <1, the location of the minimum of F'(7, A) is
determined by
VF (FA) = 0 (8.5.12)
or
=1 =-1
MA -(F—F4)+(1-AB - (F—FR) =O (8.5.13)
=1 = =1 pet
where A = (F—F4)?-G4 (Q4)-(F—-F4) and Bo = (F¥-Fg)!-Gy (Qz)-
(F — 7g) as defined in (8.5.7). From (8.5.13), the location of the minimum
F(X) can be obtained as
F(A) —Fa = (1-A) A-C- Fea (8.5.14a)
F(A) Fg =—-AB-O-rpa (8.5.14b)
where 7g4 = 7g —7, and the matrix Cis given by
= = =)
C= [a — A+ Bi (8.5.15)
--- PAGE 467 ---
§5.2 Illustrations of Contact Functions 447
The matrix © is symmetric and its existence is guaranteed by the positive
definite property of matrices A and B. Insertion of (8.5.14a) and (8.5.14b)
in (8.5.6) yields an equation for the object function
S(A) = min FF, ) = AL — A) Foy CF aa (8.5.16)
F
which does not contain 7 explicitly.

Tn computer simulations, it is straightforward to perform the numerical
inversion of the 3x3 matrix on the right-hand side of (8.5.15) and to compute
the object function $(A) using (8.5.16). However, for some special cases
explicit expressions of $(\) may be obtained. If the two particles are spheres
of radii a and b, the respective matrices A and B are

A=al (8.5.17a)
B=vl (8.5.17)
where T is the identity matrix. Then the matrix Cis
= 1 =
C=-— I 8.5.18
(1 — A)a® + Ab? ( )
and the object function S() is
Ma — 2d) ,
S() = > ——— real’ 8.5.19
= Go yaeeam eal (85.19)
max S(A) occurs at A = Ayy = a/(a + 6) and yp = S(Aqt) = \Fpal?/(a+b)?
which clearly obeys (8.5.11).

Another useful case is for two spheroids of the same size, but have dif-
ferent orientations. Let aq = ay = ea, and b4 = ca = bp = cp =a with e
being the elongation of spheroidal particle. Then the respective matrices A
and B are given by

A= a2 T+ 0(e2—1) aa Gy (8.5.20)
Baa 1+ ae? —1) ay ap (8.5.21)
where @,4 and @p are unit vectors along their respective symmetry axcs. In
matrix notations, @4 and @p are column vectors containing the components
of @ and Gy along the #, j, and 2 directions. Then the matrix C is given as

= lp _ 4c

C= [T- way ax—v ay ap
a

- 3 [Peo ds dat 3 ap ay +7 (aa dv tan aa)] (8.5.22)
--- PAGE 468 ---
448 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
with
w=(1-)) (1-e) (8.5.23)
v=A(1-e’) (8.5.24)
u(1—v)
= TT FT 5.26
° (1—u)(1—v) — uv(@4+ Gp)? (8.5.25)
v(1 —u)
B= 5.2
(1—u)(1 —v) — w(G@4- Gp)? (8.5.26)
uu (Ga - ap)
= a) 8.5.27
> Tw =0) wlan aa? 6520)
Insertion of (8.5.22) into (8.5.16) yields the object function for the case of
two identical spheroids
. M1-A 3 . yg a
SQ) = a [irzal +a(Fpa- da)” + BFR ap)?
+29(FBA-Ga)(FBaA- ax)| (8.5.28)
The algorithm of spheroidal particle placement will be applied in the next
chapter of dense media models and simulations.

It is noted that S(A) is non-negative over the interval 0 < \ < 1, and
vanishes at both end poimts when \ = 0 and 1. As \ changes from 0 to 1,
the location 7(A) will trace a path starting at 7g and ending at 74. The
following three situations for two ellipsoids A and B can be distinguished:
(i) A and B non-overlapping: The path F(A) pass through the region outside
both particles, where both F4 and Fy are greater than 1, and F(¥,\) >1.
Thus, max S(,) attains values greater than 1.

O<A<1
(ii) A and B overlapping: The minimum value of $()) is less than 1 inside
the overlapped region of two particles, where both F'4 and F'g are less than 1.
This precludes the path 7(A) from entering the region outside both particles,
and hence max S(A) is less than 1.
OSA<1

(iii) A and B externally tangent: At the touching point F(7,\) is equal to
1, which implies $(A) <1 for all \. This means that the path F(A) cannot go
outside both particles, so that max $(A) is equal to 1.

O<A<1
Based on these observations, Perram and Wertheim [1985] proposed the con-
tact function as given in (8.5.11). They also proved that the object function
--- PAGE 469 ---
§5.2 Illustrations of Contact Functions 449
S(\) has a unique maximum in the interval 0< <1. Various optimization
methods can be applied to obtain the maximum value of S(A). For exam-
ple, Brent’s method [1973], due to the concavity property of S(A), converges
quickly to the maximum. The explicit expression of the derivative of the
object function S(A) is given as

SIO) =7h,-E- [a —)? a-» B| -C-Tna (8.5.29)
which might be used to speed up the optimization scheme applied.
--- PAGE 470 ---
450 8 PARTICLE POSITIONS FOR DENSE MEDIA CHARACTERIZATIONS
REFERENCES AND ADDITIONAL READINGS

Allen, M. P. and D. J. Tildesley (1989), Computer Simulation of Liquids, Oxford University
Press, New York.

Baxter, R. J. (1968a), Percus-Yevick equation for hard spheres with surface adhesion,
J. Chem. Phys., 49(6), 2770-2773.

Baxter, R. J. (1968b), Ornstein-Zernike relation for a disordered fluid, Aust. J. Phys., 21,
563-569.

Baxter, R. J. (1970), Ornstein-Zernike relation and Percus-Yevick approximation for fluid
mixtures, J. Chem, Phys., 52, 4559-4562.

Baxter, R. J. (1971), Distribution functions, in Physical Chemistry: An Advanced Treatise.
Vol. UIA. The Liquid State, edited by D. Henderson, Chapter 4, 267-334, Academic
Press, New York.

Brent, R. P. (1973), Algorithms for Minimization without Derivatives, Prentice-Hall, Engle-
wood Cliffs, NJ.

Ding, K. H., (1989), Electromagnetic wave propagation and scattering in dense media, Ph.D.
thesis, University of Washington, Seattle.

Ding, K. H., C. Mandt, L. Tsang, and J. A. Kong (1992), Monte Carlo simulations of pair
distribution functions with multiple sizes in dense discrete random media, J. Electromag.
Waves and Appl., 6(1), 1015-1029, 1992.

Ding, K. H. and L. Tsang (1988), Effective propagation constants of dense nontenuous media
with multi-species of particles, J. Electroma. Waves and Appl. 2(8), 757-777.

Ding, K. H. and L. Tsang (1989), Effective propagation constants in media with densely
distributed dielectric particles of multiple sizes and permittivities, in Progress in Elec-
tromagnetic Research, PIER. 1, (edited by J. A. Kong), Chapter 3, 241-295, Elsevier,
New York.

Ding, K. H., L. M, Zurk, and L, Tsang (1994), Pair distribution functions and attenuation
rates for sticky particles in dense media, 8(12), 1585-1604.

Frenkel, D. and B. Smit (1996), Understanding Molecular Simulations: From Algorithms to
Applications, Academic Press, San Diego.

Hansen, J. P. and I. R. MeDonald (1986), Theory of Simple Liquids, Academic Press, New
York.

Kranendonk, W. G. T. and D. Frenkel (1988), Simulation of the adhesive-hard-sphere model,
Molecular Phys., 64(3), 403-424.

McQuarrie, D. A. (1976), Statistical Mechanics, Harper and Row, New York.

Metropolis, N., A. W. Rosenbluth, N. Rosenbluth, A. H. Teller, and E. ‘Teller (1953), Equation
of state calculation by fast computing machines, J. Chem. Phys., 21(6), 1087-1092

Penders, M. H. G. M. and A. Vrij (1990), A turbidity study on colloidal silica particles in
concentrated suspensions sing the polydisperse adhesive hard sphere wodel, J. Chem.
Phys., 93(5), 8704-3711.

Percus, J. K. and G. J. Yevick (1958), Analysis of classical statistical mechanics by means of
collective coordinates, Phys. Rev., 110, 1-13.

Perla, R., J. Dozier, and R. E. Davis (1986), Preparation of serial subsections in dry snow
specimens, J. of Microscopy, 141, 111-114.

Perram, J, W. and M. 8. Wertheim (1985), Statistical mechanics of hard ellipsoids, I. overlap
algorithm and the contact function, J. of Comp. Phys., 58, 409-416.
--- PAGE 471 ---
REFERENCES 451

Perram. J, W.. M. S. Wertheim, J. L. Lebowitz, and G. O. Williams (1984). Monte Carlo
simulations of hard spheroids, Chem. Phys. Lett., 105, 277-280.

Seaton, N. A. and L5. D. Glandt (1986), Monte Carlo simulation of adhesive disks, J. Chem.
Phys., 84(8), 4595-1601.

Seaton, N. A. and E, D. Glandt (1987), Monte Carlo simulation of adhesive spheres, J. Chem.
Phys., 87(3), 1785 1790,

Shi, J., R. FE. Davis, and J, Dozier (1993), Stereological determination of dry-snow parameters
for discrete-scatterer microwave modeling, Annals of Glaciology, 17.

Waseda, Y. (1980), The Structure of Non-Crystalline Materials, Liquids and Amorphous
Solids, McGraw-Hill, New York.

Wertheim, M. S. (1963), Exact solution of the Percus-Yevick integral equation for hard
spheres, Phys. Rev, Lett., 20, 321-323.

Wertheim, M. S. (1964), Analytical solution of the Percus~Yevick equation, Equilibrium
Theory of Classical Fluids, H. L. Frisch and J. L. Lebowitz, Eds., W. A. Benjamin,
Inc., New York.

Ziman, J. M. (1979), Models of Disorder, Cambridge University Press, New York.

Zurk, L. M. (1995), Electromagnetic wave propagation and scattering in dense, discrete
random media with application to remote sensing of snow, University of Washington,
Seattle.

Zutk, L. M., L. Tsang, D. P. Winebrenner, J. Shi, and R. E. Davis (1997), Electromag-
netic scattering calculated from pair distribution functions retrieved from planar snow
sections, IFEE ‘Trans. Geosci. Remote Sens., 35(6), 1419-1428.
--- PAGE 472 ---
Scattering of Electromagnetic Waves: Numerical Simulations.

Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.

Copyright © 2001 John Wiley & Sons, Inc.

ISBNs; 0-471-38800-9 (Hardback); 0-47 1-22430-8 (Electronic)

# Tsang《Scattering of EM Waves》Chapter 8

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 9

> **第八章：大粒子稠密介质**。研究稠密介质中粒子尺寸较大的情况，涉及配对分布函数与结构因子、Percus-Yevick方程、硬球和粘性球的PY解、蒙特卡洛模拟粒子位置、粘性粒子模型、以及椭球体的粒子放置算法。**

SIMULATIONS OF TWO-DIMENSIONAL
DENSE MEDIA
1 Introduction 454
1.1 Extinction as a Function of Concentration 454
1.2 Extinction as a Function of Frequency 456
2 Random Positions of Cylinders 458
2.1 Monte Carlo Simulations of Positions of Hard Cylinders 458
2.2 Simulations of Pair Distribution Functions 460
2.3. Percus Yevick Approximation of Pair Distribution Functions 461
2.4 Results of Simulations 463
2.5 Monte Carlo Simulations of Sticky Disks 463
3 Monte Carlo Simulations of Scattering by Cylinders 469
3.1 Scattering by a Single Cylinder 469
3.2 Foldy-Lax Multiple Scattering Equations for Cylinders 476
3.3 Coherent Field, Incoherent Field, and Scattering Coefficient 480
3.4 Scattered Field and Internal Field Formulations 481
3.5 Low Frequency Formulas 482
3.6 Independent Scattering 484
3.7 Simulation Results for Sticky and Non-Sticky Cylinders A85
4 Sparse-Matrix Canonical-Grid Method for Scattering
by Many Cylinders 486
4.1 Introduction 486
4.2. The Two-Dimensional Scattering Problem of Many Dielectric
Cylinders 489
4.3 Numerical Results of Scattering and CPU Comparisons 490
References and Additional Readings 493
453 —
--- PAGE 473 ---
454 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
1 Introduction
In Chapter 7, we have discussed analytical theory and Monte Carlo simula-
tions of three-dimensional point scatterers. In Chapter 8, we have examined
the generation of dense media that consist of three-dimensional particles
densely packed together. We study both analytical theory and Monte Carlo
simulations of pair distribution functions and structure factors. In Chap-
ter 10, we will study 3-D simulations of scattering by dense media. Volume
scattering is a computationally intensive problem having one more dimen-
sion than surface integral equation used in rough surface scattering. Thus in
this chapter, we study extensively the simpler problem of the simulations of
2-D scattering problems that consist of infinitely long cylinders. We make
use of vector cylindrical wave functions described in Chapter 1 of Volume I.
In Section 2, we describe Monte Carlo generations of positions of hard
(non-sticky) cylinders and also sticky cylinders. We also study the Percus—
Yevick approximation of pair distribution functions for two-dimensional hard
disks.* In Section 3, we perform Monte Carlo simulations of scattering by
densely packed non-sticky cylinders and sticky cylinders. We study the fre-
quency dependence of scattering by dense media. In Section 4, we apply
the sparse-matrix canonical-grid (SMCG) method to fast computations of
scattering by cylinders.
1.1 Extinction as a Function of Concentration
In a dense medium, the particles are densely packed together occupying high
fractional volumes. In the three-dimensional case, for a medium consisting of
spheres with radius a, the volume of the sphere v, and the fractional volume
f occupied by the particles are respectively
4m 3
Y= ae (9.1.1)
fener? (9.1.2)
where no is the number of spheres per unit volume. Let the particles be of
permittivity €,, and they are embedded in a background of permittivity e. As
discussed in Chapter 8, in a dense medium, the pair distribution functions
differ significantly from that of particles with independent positions. This
will affect the scattering phase functions and the extinction coefficients as
well as the effective permittivity of the medium.
” As far as the generation of cylinder positions is concerned, disks and infinite circular
cylinders are equivalent. We shall use the terms disk and cylinder interchangeably.
--- PAGE 474 ---
§1.1 Extinction as a Function of Concentration 455
| indepedent scattering
{| unrealistic for appreciable f
'
{
tf 4
I | |
FN
if
i \
f \ a realistic solution |
i \ |
~
I ” ———.
{ en.
° 1
f
Figure 9.1.1 Scattering attenuation as a function of fractional volume of particles: Inde-
pendent scattering and a more realistic solution.

In Volume I, we have employed the radiative transfer theory to evalu-
ate the scattering of waves by discrete scatterers. The extinction rate and
phase matrix are constructed by assuming that the particles scatter inde-
pendently. Hence, the extinction rate will be linearly proportional to the
number of particles per unit volume and the fractional volume of particles
f = novo (Fig. 9.1.1). However, physical intuition indicates that the linear
relation cannot be correct for arbitrary f. For example, at f = 1, when
the entire volume is occupied by scatterers, the medium becomes a homo-
geneous medium. Hence, in the absence of absorption, scattering should be
equal to zero in the limit f = 1 (Fig. 9.1.1). Independent scattering is not
valid for materials with an appreciable fractional volume of scatterers. This
has been verified by controlled laboratory experiments [Ishimaru and Kuga,
1982: Mandt ct al. 1992: West et al. 1994).

When a coherent wave propagates through a scattering medium, it is at-
tenuated by both absorption and scattering. The coherent wave propagation
constant is denoted by A, where

K=K,+ik; (9.1.3)
The attenuation K; is a summation of the absorption K, and scattering Ks
Ki = Ka+ Kz (9.1.4)
The scattering part of the attenuation is dependent on the particle size.
--- PAGE 475 ---
456 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
Usually

Ky, > Kj (9.1.5)
The effective permittivity e.g is defined as

Ke .

eet = oy (9.1.6)

Equation (9.1.5) gives the approximate relation
K? = (K, + iKa)? + 21K.K, (9.1.7)

We use kg = 2Kq, Ks = 2K 5, Ke = Ka + Ks, where Kg, Ks, and Ke are
the absorption coefficient, scattering coefficient, and extinction coefficient,
respectively. The effective permittivity includes absorption and scattering.
The classical mixing formulas for effective permittivity applies when scat-
tering attenuation can be ignored [Bottcher, 1952; Maxwell-Garnett, 1904;
Polder and van Santern, 1946]. Scattering is generally size dependent. For
example, Rayleigh scattering gives a scattering cross section that is propor-
tional to k4a°. Hence, at very low frequencics, scattering attenuation can be
neglected. In such a limit, the effective permittivity will be the same as the
effective permittivity from classical mixture formula. Thus classical mixture
formula can be regarded as a very low frequency limiting case of the effective
permittivity and wavenumber of dense media.

Random discrete scatterers can be classified as in Table 9.1.1. Particles
are described as tenuous if their dielectric properties are only slightly differ-
ent from the background medium. The characteristics of wave propagation
in such media will be quite similar to those of continuous random media.
The properties of K, and Kj; for the four classes of particles are described
in Table 9.1.1, where k is used to denote the propagation constant of the
background medium. Of the four classes of random discrete particles, class
D is the subject. of dense media.

1.2 Extinction as a Function of Frequency

In experiments of scattering by random distribution of particles, the scat-
tering and extinction are usually measured as a function of frequency. For
example, in satellite passive microwave remote sensing, the brightness tem-
peratures are measured at 10 GHz, 19 GHz, 37 GHz, and 94 GHz. In satellite
active microwave remote sensing backscattering measurements, the frequen-
cies are 1.5 GHz, 5 GHz, and 10 GHz. The objectives of these sensors are
to extract the snow parameters from these multi-frequency measurements.
Thus it is important to study the frequency dependence of scattering and
--- PAGE 476 ---
§1.2 Extinction as a Function of Frequency 457
Dielectric
Class property Particle Particle Ky Relation of
fom | ee | ti | am | amc
[| wens | —souse [ete [=| te |
significantly
non-tenuous dense correlated different, nonlinear
Table 9.1.1 Classification of random discrete scatterers.
extinction by random distribution of particles. For a small particle of radius
a, it is well known that the dependence of scattering is k4a® for 3-D par-
ticles, and ka‘ for 2-D scattering. The dependence of frequency is strong.
When the frequency is doubled, scattering increases by 16 times and 8 times
respectively for 3-D and 2-D scattering. For particle sizes comprable to the
wavelength, then the freqeuncy dependence is weaker and becomes indepen-
dent of frequency at the geometric optics limit. For sparse concentration of
random distribution of particles, because independent scattering is valid, the
frequency dependence follows that of single particles. If the particles have a
size distribution with some particles smaller than the wavelength and others
comparable to the wavelength, then the medium can exhibit varied frequency
dependence of scattering. However, does the frequency dependence of scat-
tering change with the concentration of particles? In this section, we will
show that the frequency dependence of scattering of dense media is differ-
ent from that of sparse concentration of particles. When the particles are
densely packed together, they can adhere to form aggregates. In the sticky
particle dense media model, we study densely packed aggregates of parti-
cles. We shall show that for the case of densely packed small particles, the
sticky property makes them exhibit frequency dependence of scattering that
is much weaker than (frequency)* and (frequency)® respectively of the 3-
D case and the 2-D case. For passive microwave remote sensing of snow,
this is particularly important. The ice grain in snow is of the order of 0.04
cm in radius (0.8 mm in diameter). The wavelengths are 1.58 cm and 0.81
cm respectively at 19 GHz and 37 GHz. This means that ka = 0.16 and.
ka = 0.31 respectively at 19 GHz and 37 GHz. Although the ice grains are
small at these two frequencies, the extinction measurements in snow seldom
--- PAGE 477 ---
458 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
exhibit the 16 times difference between the two frequencies as predicted for
classical Rayleigh scattering of small particles [Hallikainen ct al. 1987}. In
Monte Carlo simulations presented in this chapter, we will use the sticky
particle model to position the particles. Then we calculate rigorously the so-
lutions of Maxwell’s equations at several frequencies to study the frequency
dependence of scattering.
2 Random Positions of Cylinders
2.1 Monte Carlo Simulations of Positions of Hard Cylinders
We describe the Monte Carlo procedure of shuffling the positions of ran-
domly positioned two-dimensional particles in a square area. Let there be NV
particles. For simplicity, let
N=N? (9.2.1)
where Nj is an integer. The particles are placed in a unit square of [0,1] x
0, 1). If np is the number of particles per unit area, then
Ng =N (9.2.2)
Let 6 be the diameter of the particle, with b = 2a, where a is the radius of
the particle. Let f be the fractional area occupied by the particles. In the
computer code, we specify N and f. Then the diameter 6 is
[af
b= 9.2.3
oN (9.2.3)
Inside the square, we first placed the particles periodically in both @ and %
directions with spacing s given by
1
= 9.2.4
= (9:24)
For example, the first row of N) particles can have coordinates
8 8 3s 8 5s s 1 8
palrlaralelooalecol (Ms )a5 9.2.5
(555) (5 5) € 5) (( ‘ 5) 3) (9.2.5)
the second row has coordinates
s 38 3s 3s 5s 3s 1 38
sallow )laow fel (4-5 Jas 9.2.6
(95)-Ga)-Gea)((-a)aa) 20
and so on.
To generate the Oth realization, we use shuffling. We perform Npass
passes. For cach pass, there is an attempt to move each particle once even
--- PAGE 478 ---
§2.1 Monte Carlo Simulations of Positions of Hard Cylinders 459
though the move may not be accepted. The move is as follows. Let
A= cab (9.2.7)
where cy; is an adjustable constant for the displacement. For a particle j with
coordinates («;,yj) we gencrate its possible new coordinates (2’,,y/) from
two random numbers r; and r2 that are randomly and uniformly distributed
between -1 and 1. In MATLAB, the function rand can be used to generate
r, and ro.
x; =ajt+ndA (9.2.8)
yy =u tr (9.2.9)
Next we need to check whether the new coordinates, (x), Yj). are acceptable
by making sure that they do not overlap with other particles. Note that
the periodic boundary conditions are used. Thus each particle has images
in other squares. To check for overlap with particle J, (J = 1,2,...,N and
1#j), we calculate
Ty = Xp — £4 (9.2.10)
However, if rz > 0.5, then the image of 2; is closer to 2. Thus we do the
following
ifr, > 0.5, replace ry by rz -- 1;
ifr, < —0.5, replace rz by rz +1
Do the same for ry = yr — yj. with the appropriate replacements.
Then we calculate the distance between particles j and 1
ra= rete (9.2.11)
If
rq > b for all l 4 j,
then the move is accepted for particle j
replace «x; by «jj:
replace yj by y}.
If
ra <b for any | F j,
then the move is rejected and the original coordinates (x;,y;) are kept.
If rq > 6 for all | 4 j, we take (x4,y}) and call it temporarily the new
coordinates (xj, y;). Before we finally accept the new (2j,y;), we need to
make sure that particle j is within the unit square. If it is outside, it has
--- PAGE 479 ---
460 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
become an image, and we need to translate it back into the unit square.
Thus for the new <7;

ifr; <0, replace x; by 73 +1;

ifaj >1, replace 2; by aj —1
Do the same for y;, with the appropriate replacements. Then we accept
(xj, ¥;) as the new position for particle j.

The process is applied to all the particles j = 1,2,3,...,N. When that is
done, one pass is completed. A new realization is generated after Npass passes
to make sure that the particles are sufficiently randomized. To get the Oth
realization from the initial periodic configuration, it is better to do several
times of Nyass passes. From the Oth realization, we generate new realizations
for a total N, realizations, with each one created after Npass passes. For each
accepted new position for a particle, we count it as an accepted move. Let
Nace be the total number of accepted moves after N, realizations. Then the
acceptance rate is

Nace
accept rate = —-———_ 9.2.12

NNyoseN (9.2.22)
If the dsipacement A is too small, then all the moves will be accepted, and
the realizations will be dependent on each other. On the other hand, if the
displacement A is too large, then the moves will not be accepted. A good
acceptance rate is between 30% and 70% by choosing an appropriate A
through adjusting c.; in (9.2.7).
2.2 Simulations of Pair Distribution Functions
We calculate the pair distribution function from the realizations generated.
Let the separation of the disks be counted in intervals of Ar. For the nth
interval, the center separations of the particles are bewteen rz, = b+ (n—
Ar and ry, = b+nAr-. Since a pair of disks is considered to be uncorrelated
when their separation is greater than 5b (ie., g(r) = 1 when r > 5b), and
they cannot interpenetrate, the interval Ar is determined by

4b

Ar=— 9.2.13

M ( )
where M is the total number of intervals and determines the resolution of the
Monte Carlo pair distribution function. For each relaization, we count the
N(N — 1) pairs of separation. In the counting process, for the jth particle,
j = 1,2,3,...,N, we calculate its separation with the /th particle (1 =
1,2,3,...,N and] 4 j).

Te Ut Ty = MH
--- PAGE 480 ---
§2.3 Percus~Yevick Approximation of Pair Distribution Functions 461
if rz > 0.5, replace ry by ry — 1;
if r; <—0.5, replace rz by rz + 1;
Do the same for ry, with the appropriate replacements. Then we compute
the separation ry
ra= rir?
and find out the interval where rg falls. That will increase by one the counting
of separations for that interval.
Let C, be the number of counts of pair separations that fall in the nth
interval. Then
Cn
WAT ay 9.2.14
N(N-1) ( )
is the probability of finding a particle at the nth interval of separation. Thus,
using the definition of the pair distribution function and the conditional
probability
won = [, arvtri (9.215)
N(N=1) Jatt
where p(7|0) is the conditional probability of finding a particle at 7 given a
particle at. the origin. Since
r
plo) = 2) (9.2.16)
A
we have
CG, me gr) _ 9%) 72 _ a 7
Noy = [ Param = 8 (ry — 18) (9.2.17)
where 7, is a weighted position in the nth interval. For example, 7, =
Mn+ 7) 72. Thus
- (Cn)
9Fn) = 7 5 (9.2.18)
MO no(N = Vat (Pin = Tn)
where angular bracket refers to average over realizations.
2.3. Percus—Yevick Approximation of Pair Distribution Functions
Tn Chapter 8, we have studied three-dimensional pair distribution functions
based on the Percus—Yevick approximation. These results are based on the
analytic closed form solution for the direct correlation function. However,
for the case of two-dimensional problems, there are no closed form analytic
solution for the direct correlation function. There are numerical slutions
--- PAGE 481 ---
462 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
of Percus-Yevick integral equation for the case of hard disks [Lado, 1968].
There are also approximate analytic expressions for the direct correlation
functions of hard disks. We summarize the results Ripoll and Tejero [1995]
on the approximate analytic expressions for the two-dimensional case.
Let
re ; (9.2.19)
where r is the radial distance between the two disks and 6 is the diameter
of the disk. Also, the two-dimensional fractional volume is
f =nora? (9.2.20)
where a = b/2 is the radius of the disk and no is the number of particles per
unit area. Then, under the Percus-Yevick approximation,
e(x)=0 forr>1 (9.2.21)
For x < 1, direct correlation c(x) assumes the form,
zr
e(x) = (0) [1 —4f +4 fue (5) + 59( fz] (9.2.22)
where
2 ——-
w(x) = : [cos r—2Vil— a] (9.2.23)
3f? [8-2 25 — 9p)pf — (7 — 3p)pf?
so(f) = SE [SG 2p) + C5 — Spf (T— SPPF 9.9 94)
8 1+ f +3pf? — pf
1+ f +3pf? — pf?
e(0) = -————_——_—— 9.2.25
(0) To (9.2.5)
4
p= ; 83 (9.2.26)
w
Given the direct correlation function, we can use the Ornstein-Zernike equa-
tion to calculate the pair distribution function g(r)

A(r) = g(r) -1 (9.2.27)
where f(r) is the total correlation which is related to c(r) by means of the
Ornstein-Zernike equation

ia) =e (M12) + ne f drac (Fis) (Fa) (9.2.28)
Define the two-dimensional Fourier transforms of h(r) and (7)
1 _
H)=— | dre" nw) (9.2.29)
An? Joo
1 ee aa
‘(p) = —> re Phe F 9.2.30
C(p) Re [we c(F) (! )
--- PAGE 482 ---
§2.4 Results of Simulations 463
‘Then from (9.2.28) (9.2.30), we have
H(p) = C(P) + nodx?C(p)H (p) (9.2.31)
C@)
Hp) = ——— 20
®) 1 — nodx?C(p) (9.2.82)
For the case of isotropic total and direct correlation functions, (9.2.29) and
(9.2.30) take the form of the Fouricr-Bessel transform
1 x
Hip) == | dr h(r)Jo(pr) (9.2.33)
2m Jo
1 f%
C(p) = x | dr c(r)Jo(pr) (9.2.34)
® IO
where Jo is the Bessel function of zeroth order. By changing the variable to
x =r/b, (9.2.34) becomes
Bee
C(p) = =| dx xc(bx) Jo(pbx) (9.2.35)
T™ Jo
After C(p) is obtained, H(p) can be computed from (9.2.32). The pair dis-
tribution function g(#) is given by
20
gF) =1+ / dp e'?" H(p) (9.2.36)
Jo
or
co
g(br) =1+ 2x [ dp pH (p)Jo(pbr) (9.2.37)
0
2.4 Results of Simulations
In Figs. 9.2.1, 9.2.2, and 9.2.3, we compare the results of the pair distribution
functions from the Monte Carlo simulations and the analytic Percus Yevick
approximation for fractional volumes of 10%, 30%, and 50%, respectively.
A total of 200 cylinders are used in the simulations. The number of passes
Npass; the displacement A, and the number of realizations used are given in
the figure captions. Monte Carlo simulations agree well with the approximate
PY pair distribution functions.
2.5 Monte Carlo Simulations of Sticky Disks
In order to capture the finite binding probabilities of adhesive disk pairs,
Seaton and Glandt [1986] have developed new methods which allow the
change of a sticky disk’s number of bonds with other disks during its Monte
--- PAGE 483 ---
464 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
a
PY
2 we |
25 |
2
Sis 4
PP eee ea sO Ian BPre ° ap
° 5 8 es ®
05
|
1 15 2 25 0 30 850 4 45
ry
Figure 9.2.1 Pair distribution function for cylinders with f = 0.1. Results from the
Monte Carlo (MC) simulations are obtained using 200 cylinders with A = 0.020 (6 = 0.025),
Npass = 2000, and N, = 50. Results of Percus-Yevick (PY) approximation are also shown.
3 —
— PY}
| © we]
25+
2
S15 , |
fo patente
|
0.5) |
a ee
1 15 2 25 3 35 4 45 5
hb
Figure 9.2.2 Pair distribution function for cylinders with f = 0.3. Results from the
Monte Carlo (MC) simulations are obtained using 200 cylinders with A = 0.015 (6 = 0.044),
Npass = 2000, and N;. = 50. Results of Percus~Yevick (PY) approximation are also shown.
--- PAGE 484 ---
§2.5 Monte Carlo Simulations of Sticky Disks 465
3 =
[ — PY
} o MC
2ale
ary
4
- x
Serb .
fos
1 f ~~
o%
"
% js 2 25 3 35 4 45 5
re
Figure 9.2.3 Pair distribution function for cylinders with f = 0.5. Results from the
Monte Carlo (MC) simulations are obtained using 200 cylinders with A = .023 (b = 0.056),
Npass = 1000, and N; = 10. Results of Percus-Yevick (PY) approximation are also shown.
Carlo displacement. They have taken into account transitions between three
binding states a=0,1, 2. The four binding states of a particle are illustrated
Fig. 9.2.4. They also call the number of bonds as “particle energy state”
(PES) to denote the number of potential wells in which the particle sits.
The maximum number of bonds with other particles is 6 for two-dimension.
In Fig. 9.2.4, we show 4 of the 7 binding states. In short, the 7 binding states
are the configurations where the number of particles that stick together is
0, 1, 2, ..., 6. In numerical simulations of this section, we use the first three
binding states only, corresponding to (a), (b), and (c) of Fig. 9.2.4.

Seaton and Glandt also derive the “unnormalized” total transition prob-
ability pa for changing the displaced particle k’s binding state to the a-bond
state. The calculation of the probability pg involves integrating over all pos-
sible contact sites available to this particular a-bond state, allowing particle
overlap to occur. Let 7, be the position vector of particle k and A be the
total arca of the system. The unnormalized total transition probability po
for the test disk k to form no bond with all other disks is

po -/ dr =A (9.2.38)
A
Let d be the diameter of the particle and 7 be the sticky paramter. The
--- PAGE 485 ---
466 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
(a) (b)
( a
oe
©) (d)
Figure 9.2.4 Four binding states of sticky disks: (a) unbounded, (b) single-bond, (c)
double-bond, and (d) triple-bond.
unnormalized total transition probability p; for the test particle k to be in
the single-bond state is given by
N
a= vp (9.2.39)
tk
where the summation is over all other disks and
i iid 5 d
= = ik — a) dry, = { — } 2nd 9.2.40
v= f (2) otra) arn = (2) 2n (9.2.40)
Thus
d
p= (=) (N —1)2nd (9.2.41)
which is equal to the total circular perimeter available to the test particle
k times a factor #. Note that the difference between the three-dimensional
and two-dimensional adhesive particles, the probability is proportional to a
factor (gye for an a-bond sticky disk instead of ()* for an a-bond sticky
sphere. This has been indicated by Stell [1991]. To calculate the double-bond
unnormalized total transition probability p2 for the test particle k, a double
summation with i < j 4 k, where i,j are particle indices, is required. The
probability po is given as
N
m= pe (9.2.42)
i<j
age
--- PAGE 486 ---
§2.5 Monte Carlo Simulations of Sticky Disks 467
where
ry d 2
= [(E) stra) dey —a) are
JA\AT
_{4 ° Xr, a) ir. d Vik dra, d
= +) Jf eou- ) b(rjn — d) rpsindys drix, Ur jx
2 9
-(4) (0248)
rig — (Gi)

where dr, =rizdrindOjx and re, = r2.+r}, —2rixrij C0845, have been used to
obtain the sccond equality in (9.2.43). rj; is the distance between particles 4
and j, and 6;, is the angle between the line segments 7;; and 74 connecting
particles i with particle j and with particle k, respectively. Note that p2=0
when rjj > 2d, since particle k cannot form a double-bond with praticles i
and j simultaneously when their distance is greater than two diameters. po
has an integrable singularity at rj =2d for any pair of disks i and j. Note
that the total “transition probability” defined by Seaton and Glandt has the
dimension of “volume” which is similar to the “effective volume” used by
Kranendonk and Frenkel [1988].

‘The definitions of unnormalized total transition probabilities do not de-
pend on the previous binding state of the displaced particle k. However,
during an actual Monte Carlo step the binding state of a displaced disk may
change from its present 3-bond configuration to a new {’-bond configuration.
Similarly, in order to calculate the unnormalized total transition probabili-
ties, a list of all pairs of particles with which the test particle k could form
a double-bond, has to be established. Then, the new binding state {’ for the
test disk k is selected according to the normalized probability

P(g) = Pe (9.2.44)

Soro

a=0
It is noted that the magnitude of P(3) depends on the binding structure of
the system prior to the disk k being moved. The transitions involve all three
binding states. In the following, we describe the Monte Carlo process.
Step 1. The Monte Carlo simulations for sticky disks also begin with N’
unbounded disks regularly placed within a unit square without overlapping.
To create the 0“ (initial) realization of random distribution, the periodic
particle positions are randomized by using the shuffling method described in
Section 2.1.
--- PAGE 487 ---
468 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
Step 2. To generate sticky disks, we do not shuffle the test disk within a small
square of [0, A] x {0, A]. Instead, the disk k makes a transition according to
the breaking of its current binding state and the formation of new binding
state with other disks. We evaluate the transition probability of particle
k. Before changing the test disk k’s binding state, we have to build a list
of all possible pairs with which the test disk k could form a double-bond.
We compute the normalized probabilities P({’) according to the respective
unnormalized total transition probability pg for 8’ =0,1,2. We also store
the array of probabilities for the pair of disks (4, j)
Gj) = By (9.2.45)
POG m 2.
Step 3. A random number generator, between 0 and 1, is used to gener-
ate a random number r and compared with the obtained P({’) of the cur-
rent system to decide the new binding state of the test disk. Three obvious
possibilities are: 3’ = 0,1,2 corresponding to unbounded, single-bond, and
double-bond state, respectively. If 0 < r < P(0), then 3’ = 0 is chosen. If
P(0) <r < P(0)+ P(1), then ’ = 1 is chosen. If P(0) + P(1) <r <1, then
6! = 2 is chosen.
Step 4. The possible new location of disk k, (x/,,y,) is then determined as
follows, depending on which {9’ is chosen is Step 3. If 9’=0, the coordinates
(24,,y;) of the test disk is determined using two random number generators,
each between 0 and 1, for its 2 and y coordinates. If 3’=1, an integer random
number i with equal probabilities, i=1,2,...,N, i#k, is generated to select
the potential single-bond candidate disk. A random angle generator, between
0 and 27, is employed to determine ¢. Then
ry, =a; +d cosd
Ye =ytdsingd
where (;, y;) are the coordinates of the candidate disk i and d is the diameter
of the disk. If 3’=2, a random number, between 0 and 1, is generated. This
is then used to select a candidate pair of disks (i,j) from the established
pair-list according to the stored array of probabilities p®(i,j) to form a
double-bond with the test disk k. For this double-bond state, there are only
two choices for the test disk k’s locations, either above or below the line
segment joining the centers of disks ¢ and j. hen we determine (z/,, yj.) as
follows. Let
gq = Xj — Xj
Yd = Y5— Mi
--- PAGE 488 ---
§3 Monte Carlo Simulations of Scattering by Cylinders 469
Calculate the polar coordinates (ra, y) from (Xa, ya) by
tq =Prgcosy
ya = rasiny
where rq = Ne + yz and y = tan7!(yg/aq). Then calculate a = cos~!2rg/d.
Generate a random number u between 0 and 1. If 0 <u<05,¢=y-a.
If 0.5 <u<1,¢=7+a. The coordinates (zj,,y,) are then
a, = 2 +dcosd
Ye = yi tdsingd
Step 5. It is possible that the new position of the displaced disk may overlap
with other disks in the system. We check overlap similar to what is done
in Section 2.1 for hard cylinders. If there is no overlap, we will accept the
move and update the coordinates of the displaced disk. Otherwise, reject the
displacement and return the test disk to its original position. As in the case
of sticky sphere, we have to maintain an updated catalog of the system’s
binding configuration, so that we need to rebuild the list of possible double-
bond candidates whenever a trial move of the test disk is successful.

In Figs. 9.2.5 and 9.2.6, we illustrate the Monte Carlo simulations of the
pair distribution functions for the two-dimensional sticky disks. The result
in Fig. 9.2.5 is for the case of 200 sticky disks and fractional volume of
20%. For Fig. 9.2.6. we use 300 sticky disks for the fractional volume of
30%. The Monte Carlo results are obtained by averaging over 12000 and
10000 passes, respectively. For both cases, the sticky paramter is 7 = 0.1.
Compared with the 3-D results shown in Chapter 8, the 2-D sticky disks
exhibit discontinuities in the pair distribution functions at pair separations
of r = 3d, V7d, and 3d in addition to r = d and 2d. These features have
also been shown in the study of Seaton and Glandt [1986] for adhesive disks.
3 Monte Carlo Simulations of Scattering by Cylinders
3.1 Scattering by a Single Cylinder
Consider a cylinder of permittivity €) and radius a centered at the origin
(Fig. 9.3.1). Let the incident wave have exp(iki,z) dependence. The incident
wave is given by

20
Bi= > [a RaM (hip, hiss?) + RGN alkip,Kiss7)] (9.3.1)
n=—00
--- PAGE 489 ---
470 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
38 a
2st ° |
2 4
| °
S15 . 4
tr & emgnsoss6 Fe sosebis ame esses SOmCNRES
Senses
| '
osl J
| 1 4 —_1___. J
% 16 2 25 3 35 4 445 5
id
Figure 9.2.5 Pair distribution function obtained from Monte Carlo simulations for a system
of single size sticky disks with r = 0.1 and f = 0.2. 200 disks are used in the simulations,
and the results are obtained by averaging over 12000 passes.
3)
°
25 :
2
s ° °
Sis
| § |
é 5 6
§ °. 26 fae
' e camps oO oases
os! {
\
A
1 169 2 25 3 35 4 45 5
rr)
Figure 9.2.6 Pair distribution function obtained from Monte Carlo simulations for a system
of single size sticky disks with + = 0.1 and f = 0.3. 300 disks are used in the simulations,
and the results are obtained by averaging over 10000 passes.
--- PAGE 490 ---
§3.1 Scattering by a Single Cylinder 471
z
a
8s og fi
y
Z| 7
€0
a
Figure 9.3.1 Scattering by a single cylinder with permittivity ep and radius a.
where al? and al) are the ‘TE and TM wave coefficients and the regular
vector cylindcrical waves RgM,, and RgN,, are defined in Chapter 1, Section
4.2 of Volume L. In (9.3.1),
hip = \/k? — 2 (9.3.2)
The scattered ficld is given by
— oS. — \ =>
Ex = S> [al Wa (hipsics7) + aN (hip, hies7)] (9.3.3)
n= 00
where als and als are the TE and TM scattered wave expansion coefli-
cients and the vector cylinderical waves M;, and NV, are defined in Chapter 1,
Section 4.2 of Volume I.
The internal field is given by
ES
Eine = S> [eBO RGM aking: hics7) + AM RGN n(Bippsiss7)] (9-3-4)
n=—90
where fit ) and bX) are the TE and TM internal ficld coefficients and
Kipp = 4/ k2 ~ ke, (9.3.5)
with k, = w,/jié. Because of phase matching, both the scattered field and
the internal field have the same exp(ikjzz) dependence.
--- PAGE 491 ---
472 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
From Chapter 1, Section 6.2 of Volume I, there are four equations re-
lating the scattered field coefficients als as and the internal field coef-
ficients fh), to the incident field coefficients al) a ) From equations
(1.6.58)-(1.6.61) of Volume I,
j j nk, ;
— kiya J (kiga) — kiya?’ HY" (kiya) — Fea Inlkipa)
nkiz (ys
— eal HD (hint)
, nkiz iw
=~ King? Ind Bipot) — Fre Sul io) (9.3.6)
Ki wy ,, Fe yay Uys — Fino (W) 7
Pn kipalan”) + 4 P Hn (Ripa)an’* = Fi, ln kip )en (9.3.7)
® Pp
[igo (big) — Ryall)
Diz (M0 7 (hy,a) — BE a? HO (by
~ ka In (Rip) — ka “” ne (kip@)
y nkiz p
=kp [typo - L(g) (9.3.8)
py
KE In Ripa all) + 2H) (hipa)a® = ny In (kip) (9.3.9)
Eliminating the scattered field coefficients gives the equations relating the
internal field coefficients to the incident field coefficients. From Volume I,
(1.6.62) to (1.2.67), we have
AMM (k,.)c00 4 AMIN (iz)eG™) = af (9.3.10)
ARM (ss)elOD + ANN (se) = af (9.3.11)
where
A ian
AMM.) = — SE [Fokipdn (Kppa) 2" (Isiga) — Kippk?, Ti (hppa) HL (Ripa) }
“ip
(9.3.12)
; jax [ n 244
AMN (hz) = oe [M(H - 1 Jalna) E(k) (9.3.13)
“ip LEP
k, :
AN (his) = GP An™ (hi) (9.3.14)
--- PAGE 492 ---
§3.1 Scattering by a Single Cylinder AT3
NN iar [kk; kip (yy Kpkippkt 1, (a)
An” (kiz) = Re In kp) An (kipa)— "Jn (Rpp) Hn (Ripa)
"ip 'p
(9.3.15)
After the internal field coefficients and scattered field coefficients are ob-
tained, we can write the relations between the internal field and the incident
field as
OD = BMMg™) 4. BMNG(N) (9.3.16)
SY) = BNMg™) 4 BNN QO) (9.3.17)
and the relations between the scattered field and incident field as
GDS = TMM gM) 4 PMN GW) (9.3.18)
als = TNM gM) 4 DNNG(N) (9.3.19)
Generally TE and TM waves are coupled for scattering by dielectric cylin-
ders. The TE and TM waves are decoupled and the equations simplify for
the following two cases:
(A) Scattering by dielectric cylinders with incidence in the r-y plane. For
this case, the TE and TM waves are decoupled.
kiz =0; kip =k, kpp = kp (9.3.20)
AMM(h..) = a [A2k.Jn (pa) HD" (ka) - kph? Jq (kya) HD (ka)| (9.3.21)
AMN(h.) = 0 (9.3.22)
AN (ki.) =0 (9.3.23)
y ian [2 2
ANN (kiz) = ap [}? kJ (kpa) Hi" (ka) — KB kJ (ya) HL (ka) (9.3.24)
Then from (9.3.16)-(9.3.19), we have
fh = Ba) (9.3.25)
&) = Ba) (9.3.26)
als = TOD gM) (9.3.27)
alN)8 = TM) gl) (9.3.28)
where
" at
BO) = BM = rakp (9.3.29)
ep” (ka) Jn (ipa) — KH (Kea) Jt (Hepa)
Bik
BO) = pl) =-—___h___ 3s)
" kp HD (ea) Tf, (kiya) — KH! (hea) Jn (hepa)
--- PAGE 493 ---
474 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
an nM)
TAM) = 7) = -—* __ (9.3.31)
ST ae
(N) (N) ry )
TON) = 7) = =n (9.3.32
rT
a)? = kyJn (ha) In (kya) ~ kJn (ha) Jp (kya) (9.3.33)
y) = kpY J (ka) Jn (kiya) — k¥n (ka) Ji, (kpa) (9.3.34)
a) = kyJn(ka) Jp, (hpa) — kJn (hea) In (Kya) (9.3.35)
u®) = kp¥n (ka) J}, (kya) — KY, (ka) Jn (Kp) (9.3.36)
For the case of small cylinders, we use small argument approximations of
Hankel and Bessel functions. We also keep the leading term of the real part
and the leading term of the imaginary part.
Analogous to the sphere case treated in Eqs. (2.8.54)-(2.8.59) from
# Tsang《Scattering of EM Waves》Chapter 8

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 2 of Volume I, since a) < y?, of) < y?, we have

> **第八章：大粒子稠密介质**。研究稠密介质中粒子尺寸较大的情况，涉及配对分布函数与结构因子、Percus-Yevick方程、硬球和粘性球的PY解、蒙特卡洛模拟粒子位置、粘性粒子模型、以及椭球体的粒子放置算法。**

TA) = 100 + ary? (9.3.37)
(M) oi)
Th) = ay (9.3.38)
Yn
M)\2
(AT) an? ‘9.3.39
Ty) =— | 5 (9.3.39)
Yn
TOY) = 7) 4 a7) (9.3.40)
wy _ of? 0
Tai = oxy (9.3.41)
Yn
a \?
N) me d
TN) = (Ss) (9.3.42)
Yn
Neglecting T-matrix coefficients that are less than O(k?a) , it can be shown
that for TM waves, only n = 0 term contributes while for TE waves, only
n = +1 contribute.
Making small argument approximations, we obtain for TM waves,
N a 112 2 9 44
ay”) =—$ (KH) (9.3.43)
y= (9.3.44)
a
--- PAGE 494 ---
§3.1 Scattering by a Single Cylinder 475
Thus
N) oN) Ny\?
TY) = ins — (18°) (9.3.45)
2
(N)_ Ta" 719 eae
Ty) =~ (hp — ke) (9.3.46)
For TE waves
M kya ka a
aM) kyo — eS (9.3.47)
2
iy 41 ey 9.3.48
ni amet) (9.3.48)
M M) _ sa(M (M)\? F
TY) = 78) = ant — (72) (9.3.49)
mazk2 (2 — 2
rit). RPK? (hp =) (9.3.50)
rtCeT
(B) Scattering by perfect electric conducting (PEC) cylinders. For this case,
the TE and TM waves are decoupled, and we have
cM) = A) = 0 (9.3.51)
aM) — 7(M) QM) (9.3.52)
al)s = TIM) Q) (9.3.53)
where
1h
7400 = 700 = —_Jalbio) (0.3.54)
Fn" (kipa)
y N) Ty (ky,
TO) = TY) = at Kip) (9.3.55)
Fy (kip)
For plane wave incidence in the z-y plane, the incident field is
Ey (7) = (Be, + hiBp,) (9.3.56)
with the incident direction vector
kj = k (&cos ¢; + Jsing;) (9.3.57)
Then the incident wave is, from Eq. (1.6.54) in Chapter 1 of Volume I and
setting kip = k and ky, = 0,
_ 2 me ings _ _
Ei) = >> —— [iE RgMn (k,0,7) — Ey. RgNp (k,0,7)] (9.3.58)
n=—20
--- PAGE 495 ---
476 9 SIMULATIONS OF ‘TWO-DIMENSIONAL DENSE MEDIA
Thus for this case, the incident field coefficients are
any _ attlemings
ay") = —{— Eh, (9.3.59)
. nen ings
al) = SB, (9.3.60)
3.2 Foldy-Lax Multiple Scattering Equations for Cylinders
The cylinders are centered at 71,72,.-.,7n. Let the incident direction be
in the 2-y plane so that 6; = 90°, kiz = 0,kip = k. We use the Foldy-Lax
multiple scattering equations which states that
N
BO B+ YE (9.3.61)
pal pea
The equation states that the final exciting field of particle q is equal to the
incident wave plus the scattered waves to particle g from all other particles p
except q itself. The incident wave can also be expressed in terms of cylindrical
waves centered at the cylinder q.
Ei(P) = (Be, + hikn,) oF = (iE, + iE) OB Pre)
ep, Co iteniné _
= hh 5” > (iE, RgMn (k,P — By)
n=—o0
—Ey,RgNn (k,P —Dy)| (9.3.62)
The exciting field of cylinder q is equal to
x
BAO = SY [wiOMy (8-7) WON n (—7a)| (9-363)
n=—00
where wo) and wi are the final exciting field coefficients. The excit-
ing field of cylinder p is
oo
zea a ava ee N’ ad es
EO . [w? Rg Mw (ky P — Dy) + wo 1?) RGN» (k,p- »)|
n’i=—oo
(9.3.64)
The scattered field from particle p is,
oo
ae (AM), (MY) zy =_- VY). (NYP) RF =
BY = > [7.! wD My (kB — Dy) + TM ON ye (kp 7»)
n'=—00
(9.3.65)
--- PAGE 496 ---
§3.2 Foldy-Lax Multiple Scattering Equations for Cylinders 477
y =
Ox D -B;
Pi PL
Om
Figure 9.3.2 Translational addition theorem in the cylindrical coordinate system.
where Tr) and 7) are the T-matrix coefficients.
To obtain equations for the exciting ficld coefficents from the Foldy-Lax
multiple scattering equations, we need the translational addition theorem of
HY (k|p—p) et" oor (9.3.66)
where p57 is the aziumthal angle that p — p’ makes with the x-axis (see
Fig. 9.3.2). Let
PP =D—Do- (P' ~ Po) (9.3.67)
|e’ — Pol = IP - Pol (9.3.68)
Then
HO (b[p—p) eer
0
= DS In(klp— Ml eH, (kp — pole" (9.3.69)
n=—00
For the vector cylindrical wave functions with
[Pp ~ Bgl = |p ~ Pal (9.3.70)
we have
My (k.P — Pp)
oo
= SD RGM n (BD -Bq) Foy (k [Bp — Bal) (9.3.71)
n=—00
--- PAGE 497 ---
478 9 SIMULATIONS OF ''WO-DIMENSIONAL DENSE MEDIA
Ny (kp — Bp)
o
= SO RIND (EP -Fq) HO (EIB, — Fal) CR (9.3.72)
n=—00
Putting the cylindrical wave translational formula into Foldy-Lax multiple
scattering equations, we have
ES
[wi 1D RgM,, (kB — J) + WY RgN np (kp — >a)
n=—90
ap, Ce ie ith: _ _
=P ST —S— [iE ROM n (k,P ~ Pq) — Ev RON n (h-P ~ Pa)
n=—00
SA OS M)) (M ava
OE DY [ral Rath (7 -7,)
Pt n'=—90 N=—O
oe
(N)(N 7 iha a
$72) yO RoW, (k,p— 7,)| x
1 Ly -afnen’
Fe (F [Bp ~ Bal) eA"
(9.3.73)
Balancing the coefficients for the TE waves gives
= _ ntle—ind,
WON — ikea, Me a En,
x ON -
+ DAD (ke [ip — al) oo RTO WLP (9.3.74)
n= -99 PHT
aq
and for TM waves
wl = em 7 E.,
~ ~ ) ome (N), (NYG
1 |) (nn! pN), (N’ 7
+ SD SAD lay — By) OT WL) (9.3.75)
nia—0o P=
péa
The above equations can be written in a matrix form. For example, for TE
case with Ninax = 1 and N = 2, we have
--- PAGE 498 ---
§3.2 Foldy-Lax Multiple Scattering Equations for Cylinders 479
1 0 0
0 1 0
(1) ? (ay 0 (1) b
—H§ (k |p, — Bol) — AS) (k IP — Pal) — Hg (ke |p ~ Pal):
ray eta TM) PomaT)
—H\ (Ip, — pal) — HQ? (|p — Dal) — HEY CIP ~ Pal)
ema TM) Th) cnn")
Dips 5 Dips _s at
HS? (hp, — pal) — HN? (Ip — pal) —H8? (Ip, ~ Pal)
ePemma tM) maT) 7)
Np. Wipe = Wypin a
=H) (k Ip — Pal) —HEY (ke ~ Pal) HS (IP = i):
pap elt TAM) ePemmT(\)
Dini. _s an Mins
= H8 (py al)» HE Py Pal) HSL Oe ~ PD
ean TM) TY) ela qT)
1 i = 1 = = (1 = =
HL (k |p — pri) — HN? (kip — pul) — HBS? (ke ~ Ail):
em TD eam 7) 7M)
1 0 0
0 1 0
0 0 1
AP) cae p,
wid oii : Ey,
; = _ j2pnids
whd® eked, = En,
x = a (9.3.76)
wie | | np,
a ik. 3%
we) iki PT En,
— 2b:
wine ihr = En,
After the exciting field coefficients are solved, the “final” scattered field
from cylinder q and the final internal field of the cylinder g can be obtained.
oo
BO- > [ato RoM, (kp — Pq) +a RgNy (kD ?.)|
n=—0o
(9.3.77)
--- PAGE 499 ---
480 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
aM) = TM yON@ (9.3.78a)
AlN) = TON yO (9.3.78b)
The total scattered field is
N
EB.=oE (9.3.79)
ql
For the final internal field of cylinder q
ox
EQ = D> [eM RIT (by, P Dy) + Ran (ps? — Pa)
n=—00
(9.3.80)
where
BO = BADD)
AMO = BN wo (9.3.81)
After the “final” exciting field coeffcients are obtained, we can calculate the
“final” scattered field in the direction k, = k(cos ¢,¢ + sin @,4). Using the
asymptotic form of Hankel functions and derivatives, we have, in the limit
of p> x,
Tn (iy hesB) = ~Biy] He eur -f) tins (9382)
= ~ 2Kp ilkpp-2)rinz [kz | hp.
Mn (KpskssP) = / Belo f)-5 (Fp 4 Ps) (9.3.88
Qk Nx
E, = [Bel > > [-di7 up + 27) 0]
™P q=1 n=—20
x €in(b-) nike By (9.3.84)
3.3 Coherent Field, Incoherent Field and Scattering Coefficient
Let A be the area in which the cylinders are placed. The fractional area
occupied by the cylinders is
Nraz
f= — (9.3.85)
The Monte Carlo simulations of scattering by the cylinders are performed for
N, realizations. Let F,, be the scattered field F’, for the rth realization. The
--- PAGE 500 ---
§3.4 Scattered Field and Internal Field Formulations 481
coherent scattered field (E') is obtained by averaging over N, realizations
_ 1X
(Bs) = 5 SOEs (9.3.86)
Ne
ral
The averaged intensity is given by
2 1S p
(Es|?) = Nw SE» (9.3.87)
OT ps
and the incoherent intensity is equal to
zB 2 FR 2 «
((E.|°) - |(Es)| (9.3.88)
The scattering rate is the scattering cross section per unit volume. To obtain
unit volume, we can consider a unit length in the 2-direction. Then the
scattering coefficient is
2m
2 TB \2
ff 40 ((\Bel?) ~ KBP)
he = 20 poe (9.3.89)
A (\Euil? + |Bwil?)
Only the incoherent intensity is used in calculating the scattering coefficient
for reasons as discussed in Chapter 7. If the cylinders are not absorptive,
then ke = Ks.
3.4 Scattered Field and Internal Field Formulations
Instead of using equations for the exciting field coefficients, the scattered
field coefficients can also be used in Foldy-Lax equations. For TE waves
= - gntle—inds
aQts(@) = eirB, 2 © TOME,
k
xo ON
FT OR ae (Py — Pal) RRA (9.3.90)
1 =—00 Pat
pea
and for TM waves
4 t  GMenings
alsa) = TN) @heFy “SE,
xo ON - y
+2) SO SHY, (he [Pp — Dal) PAN (9.3.91)
nis—o0 Pot
Pa
--- PAGE 501 ---
482 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
The internal field coefficients can also be used in Foldy-Lax equations leading
to the internal field formulation. For TE waves
= _ jntle~ingy
OOM = othe 7 BOR,
9° N
+ BED SO STH (fp — Pal) Fe SN LMOM —_(g.3.99)
nis—o0 P=
psa
where
M),
T, inak,
(M) fn P (M) .
Si Bo mR tn (9.3.93)
that relates the scattered field to the internal field. For TM waves
, <= itte-inds y
N)@) = ~eik 5 — By, BAN)
oo ON
WN 1 = _s “(nn ore g(N)_(N
+BY) ST SOHO, (|p —Dyl) oO r~SM AMO (9.3.94)
n'=—0G P=l
Pea
where
wy Th? imaky (xy
SM) = Sa = ee (9.3.95)
Br
3.5 Low Frequency Formulas
We next consider the low frequency limit of the formulas for the Foldy-Lax
multiple scattering equations.
TM case
For the low frequency limit, only m = 0 (monopole) contributes to TO),
Then
in i(k? — k?
7) = We), (9.3.96)
q k
BN) = * (9.3.97)
Kp
where ¢ = ra” is the cross section area of the cylinder. The exciting field
equations then become
--- PAGE 502 ---
§3.5 Low Frequency Formulas 483
WO = hr gikP, =
N i(k? — 2
Depls 5) Loo) ww :
+H? lop 7) Doug 03.98)
p=1
P#Fq
and the internal field equations become
N 5 (p2 2
(N Ep, Er i(ke —k Na
0) = —en Fa 4 H® (kD, —Pyl) ip) eS ) el) (9.3.99)
‘Po p=
PFd
Note that in the low frequency limit, only the z component of the electric
field exists, we also have for the internal field of cylinder q as
BRD) = hyd (9.3.100)
Thus the internal field equation can be put in the form
N.
EMO = CR PEy, + STH,” (Pp ~Pal) (hp — 2) 02 (9.3.101)
p=l
Fd
The above matrix equation is consistent with that of a volume integral
equation using pulse basis function for each cylinder by recognizing that the
2-D Green’s function is ty (k [Pp — Bal)-
TE case
Only n = +1 contribute. Thus we have
N
M kip, 1% D(pin = MM), (M)
wf 8m Sy SH (ap) 12 lh
=1
Pea
“ 1) brary M M
+ SO AY? (FB, = Bal) © PPP TM WAP (93.102)
= 1
beq
; N
M 7, 2 Dipis = M) (M
wh Na) = ¢i PE, + 1 Ht ) (k |p, — Bal) TE YpODo)
=1
pea
N 9
+ MS (be [py — Dal) HTP WOM) (9.3.103)
p=1
P#d
--- PAGE 503 ---
484 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
3.6 Independent Scattering
The results of independent scattering can be readily derived. From (9.3.75),
we approximate for TM waves,
yO) = ihn, HE
vO =~. B, (9.3.104)
Thea
ok N © _
EB, = =k > TON yl NVM) iO Hemera (93.105)
™? g=ln==00
Assuming independent scattering of the scatterers, |E5|? becomes
2k | *
Fone: v N),,(N) pin(oe =
|B. = 2 9° 14 Vapl™) eins i (9.3.106)
The the scattering coefficient is defined as
Qn
[t,o 1B?
is = 22 ____ 9.3.107)
TEP O10)
Using (9.3.104)-(9.3.106) in (9.3.107), we have
. 4no = (N) (2
Kea oe YS in! (9.3.108)
n=—00
Similarly, for TE waves,
Ang SS spun :
woe YD In| (9.3.109)
n=—00
At low frequency for TM waves, using (9.3.96), we have
2 22/2
Ano ke =e 204
is = — |— 9.3.1
hs | 1 ma ( 10)
This gives
‘ log 998 2
= = eK ana? |e = 1
7 2
= IE p2q2| Se - 1| (9.3.11)
4 €
Thus, from (9.3.110), Ks has a (frequency)* dependence.
--- PAGE 504 ---
§3.7 Simulation Results for Sticky and Non-Sticky Cylinders 485
3.7 Simulation Results for Sticky and Non-Sticky Cylinders

In the following, we present simulation results of TM waves. We find that for
the case of small cylinders, the condition number of the matrix equation with
internal field formulation is lower than that of the exciting field formulation.
Thus the results shown in this section are computed based on the internal
field formulation of Eq. (9.3.94). Matrix equation is solved by direct matrix
inversion. We illustrate results for ka = 0.2 to ka = 0.8. Multipoles are
truncated at Ninax = 3.

In Fig. 9.3.3, we plot the normalized extinction coefficient K./k for non-
sticky and sticky cylinders for ka = 0.2, 0.4, 0.8 and ¢, = 3.2¢,, € = €. The
results show convergence with respect to the number of realizations. We use
up to 50 realizations. The fractional volume is f = 0.2, and we use 200
cylinders in the simulations. For sticky cylinders, we use a sticky parameter
of r = 0.1. The independent scattering result is computed based on (9.3.108).
In Table 9.3.1, we tabulate the results for ks/k. The frequency dependence
of scattering can be derived from Table 9.3.1 as follows. We consider three
frequencies at w1, w2 = 2w,, and w4 = 4u,. Let k; = 1 be the wavenumber
of w). Then ky = 2 and k4 = 4 respectively of wo and w4. Let @ be such that
kia = 0.2. Then kya = 0.4 and kya = 0.8. For non-sticky particles, extinction
coefficient Ks, at w) has Ks1/k; = 0.0116 so that ks: = 0.0116. For we, kya =
0.4. From Table 9.3.1, the extinction coefficient Ks: has Ks2/k2 = 0.0335
so that Ks2 = 0.0670. At wy, kya = 0.8, then the extinction coefficient at
ws has Ks4/kq = 0.0281 so that Ks = 0.1124, The case of sticky particles
and the case of independent scattering are determined similarly. Table 9.3.2
gives the results of extinction. It is clear that sticky cylinders have a weaker
frequency dependence than non-sticky cylinders. Sticky cylinders also have
a weaker frequency dependence than independent scattering. For example,
K52/Ks1 = 5.78 for non-sticky cylinders, K2/Ks1 = 2.93 for sticky cylinders,
and Ks2/Ks = 9.2 for independent scattering.

0.0116 0.0327
0.0480 0.1633
[as [poate | 02706
Table 9.3.1 Extinction coefficients for non-sticky and sticky cylinders.
--- PAGE 505 ---
486 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
0.08 : ' ep
| < non-stickyka=0.2 |
+ non-sticky,ka=0.4
0.07 * non-sticky ka=0.8
iS  Sticky,ka=0.2,
© sticky,ka=0.4
4 © stickyka-o8 |
0.05)
\ aocoa, 998 coguensnocnsoranaagsarcagacoqnanaga
a2
S004- cc
0.03 Tyra ps maLeesaaZOhSARAEAREA LAR AAA GAARA ARAB SA
. ene
o. afhbtsesssesseneeresesscenennsnsessessssesys
0.02; * 8 +
A
0.011 Fees ge 208 2002020 O OGIO ROG OBO B OO UE
ol .
o 5 0 1 2 2 3 3 4 45 50
number of realizations
Figure 9.3.3 Extinction coefficients for non-sticky and sticky cylinders.
(ee me]
0.0670 | 0.1124
sticky 0.0327 | 0.0960 | 0.1072
| independent | 0.0355 |” 0.3266 | 1.0824
Table 9.3.2 Extinction coellicients based on Table 9.3.1 with a = 0.2, kya = 0.2, k2a = 0.4,
kga = 0.8.
4 Sparse-Matrix Canonical-Grid Method for Scattering by
Many Cylinders
4.1 Introduction
In Chapters 5 and 6, we applied the sparse-matrix canonical-grid (SMCG)
method to solve rough surface scattering problem. For the case of rough
surface scattering, equally spaced points on a flat surface was used on the
canonical grid. In this section, we illustrate how the method is applied to
volume scattering [Chan and Tsang, 1995; Chew et al. 1995]. In the SMCG
method, we carry out the decomposition of strong and weak interactions.
The weak interactions, which account for the majority of the required CPU
time and memory, are calculated using a canonical grid with a translational
--- PAGE 506 ---
§4.1 Introduction 487

DADCD | em

aya <a interaction
CYAN — weak
Aa
{
mo
IC)

Figure 9.4.1 Decomposition of strong and weak interactions.
addition theorem. ‘This facilitates the use of FFT and results in an N log N-
-type efficiency for CPU and O(N) for memory. We use the concept of the
sparse-matrix canonical grid method for scattering by many discrete scat-
terers. The near- and intermediate-range interactions are represented by the
strong interaction matrix. For the weak part of the interaction among many
discrete scatterers, we utilize a uniform grid as the canonical grid. By us-
ing a translational addition theorem, each scatterer is translated to a grid
point in the uniform grid. We are making use of the equivalence principle
to state that the field scattered by a scatterer is equivalent to the radiation
from a grid point in the uniform grid. We further illustrate the method by
considering scattering by Np dielectric cylinders (two-dimensional scattering
problem), the positions of cylinders are randomly placed in a square box
(Fig. 9.4.1). The square box is next discretized by a two-dimensional uni-
formly spaced grid with N, points. The grid size is chosen according to the
cylinder distributions. Each cylinder is associated with a grid point that: is
closest to the center of the cylinder. Several cylinders may be associated with
the same grid point.

The strong interactions between two cylinders in the vicinity of each
other are calculated directly and represent the strong-interaction matrix.
On the other hand, as depicted in Fig. 9.4.2, the weak interactions between.
two distant cylinders centered at p, and fg are calculated indirectly. We
first translate from P, to its associated grid point at 7... Then we calculate
radiation from the grid point p,, to the grid point f,4. The points p,, and
Pog are on the uniform grid. Finally we translate from p,3 to the center
of the cylinder at jg. All the operations can be performed by the use of
translational addition theorem. The indirect calculation is cast into a form
--- PAGE 507 ---
488 9 SIMULATIONS OF T'WO-DIMENSIONAL DENSE MEDIA
(aan
oO
Figure 9.4.2 Direct and indirect interactions from cylinder to cylinder a.
such that the weak interactions of all the cylinders, which account for the
majority of the CPU time, can be evaluated simultaneously using FFT, thus
achieving an N, log N,-type efficiency. Note that N, can be less than N,
when several scatterers associate with one grid point. This method only
requires translation of a short or moderate distance to the nearest grid point
so that the translational addition theorem only requires a low order. Using
the matrix notation of the impedance matrix, the strategy can be represented
as follows. By discretizing integral equations, a matrix equation
ZX=b (9.4.1)
can be obtained. In (9.4.1), Z is the impedance matrix, X is the unknown
column vector, and 6 is the known vector corresponding to the excitation.
Next the impedance matrix is decomposed into strong and weak interaction
matrices
> = sw
Z=Z4Z (9.4.2)
ss . . . sw.
In (9.4.2) Z represents strong neighborhood interaction and Z is the
s.sW
rest of Z. In Z , we use translational addition theorem to find equivalent
sources at the uniform grid points, which are further translated to the actual
observation points. In matrix notation
sW. =s5
ZX =T,Z,T.X (9.4.3)
where T, isa diagonal translation matrix for the scatterers, Z, is the matrix
representing the canonical uniform grid problem of radiating from grid points
to grid points, and T, is the diagonal translation matrix to the observation
points. Thus the product of T, and X requires O(N,) steps. Next, multipli-
cation by Z, can be performed by discrete convolution using 2-D FFTs, as
--- PAGE 508 ---
§4.2 Two-Dimensional Scattering Problem of Many Dielectric Cylinders 489
Z, is a translationally invariant matrix. This requires O(A.N, log 4N,) steps.
Further multiplication by T, requires O(N>) steps. In the memory, T,. and
Tg are of the order O(N,), because they are diagonal matrices. The Z, ma-
trix is translationally invariant and consists of points that are equally spaced
apart requires memory of the order of O(4N,). Iterative solutions such as the
conjugate gradient can be adopted for the iterative solution of the matrix
equation.
4.2 The Two-Dimensional Scattering Problem of Many Dielectric
Cylinders
Consider an incident wave with wave vector kj; scattered by a medium
consisting of N, circular dielectric cylinders centered at ~, where a =
1,2,..., Np. Each cylinder has a radius of a, permittivity «,. We consider
the algorithm for TE wave. The Foldy-Lax multiple scattering equations
are, from (9.3.74),
- Np
Wl) = Fag lem By; + Sw? (9.4.4)
aga
where we have defined wee as the exciting field of a due to the scattered
field from . It is given by
. a)
wit = SS Ow ANY, (klig — Pal) exp [-i(n — m)baqpz] (9.4.5)
m=—00
We have suppressed the (M) superscript in (9.4.5). Equation (9.4.5) is
termed a direct calculation. Let p,, and Pg be the grid points in the grid
associated with the cylinders at J, and fg, respectively. After the successive
use of the translational addition theorem to (9.4.5) to translate from fp, and
Dg to Pog and Pog, respectively, we have
oc
up? = So TR ul?
m=—00
oo oo
> YS Savin blBs — Boal) exp [-ien! — m) barn]
m/=—00 n’=—00
1 _ = . ,
x Hy? sy (EIB ~ Boal) &xP [—i(n! — mi) bgerpec]
x Inn (k\Poa ~ Bal) exp [-i(n —n')op-xp5] (9.4.6)
--- PAGE 509 ---
490 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
This procedure is termed indirect calculation. It is then clear that the excit-
ing field coefficients among all cylinders can be computed simultaneously,
First, let us define a pre-multiplication process as
oo
~ 8 I = . (3 8
ah, = S> Inr-mlblps ~ Posh) exp [-ilmn! — m)bprrx] Tu (9.4.7)
m=—ce
This step requires O(N,)} operations, where N, is the number of scatterers.
Next we sum over all scatterers to obtain
oo
za 1 al = A -3
HY = YO HO bIPoa — Boal) exp [inl — moran] v2, (9.48)
m'!=—00
Because the points p,,, and ~,g are equally spaced on the uniform grid, this
process can be performed simultaneously for all @ and 8 combinations via
the use of 2-D FFTs. This step requires O(4N, log N,) operations. Finally,
we perform post-multiplication to complete the indirect calculation so that
ES
we? = So Incn' (Boa — Bal) exp [-i(n— n!)og—pe] ty, (9.4.9)
nm =—9C
The final step requires O(N») operations. In this way, we obtain the N?
combinations of w%? simultancously. Note that if the scatterers are of small
to moderate size, only a few orders in the T-inatrix coefficients are needed. If
the center of the cylinder is not too far from the grid point, only a few terms
in the translational formula are needed in the above infinite series. The fact
that a majority of the interactions are weak and can be evaluated simultane-
ously using FFTs means that this algorithm is efficient when the number of
scatterers is large, for example, on the order of several thousand. We define
a neighborhood distance rg. For a distance between scatterers less than the
neighborhood distance, we exercise the direct calculation corresponding to
oS
the strong interaction matrix Z . For a distance between scatterers larger
than rg, we exercise the indirect calculation corresponding to the weak in-
sw
teraction Z utilizing FFTs.
4.3 Numerical Results of Scattering and CPU Comparisons
Figure 9.4.3 shows the distribution of N, = 4000 cylinders with a total area,
of 40% of a unit square box. This is generated by discretizing the region
with a 64 x 64 grid (N, = 4096) where a cylinder is assigned to each grid
point. We then randomly removed 96 cylinders from the region. The re-
maining 4000 cylinders are allowed to move away from the grid point with
--- PAGE 510 ---
§4.3 Numerical Results and CPU Comparisons 491
Ba Fessertersrotrsranaenienctierr nyt
Ea aaa
a
= 08 ea Seas nat
é ie Hane ee
SUR Earner aut
—o.
Bae ite Sunn
eee
2 ee
oo | HESS a Eas
00 os 10
Position
Figure 9.4.3 4000 cylinders randomly placed in a unit, square box.
a random displacement between 0 and 50% of the radius of the cylinder.
The average distance from the grid point for all the cylinders is 0.27% of
the radius. The cylinder has a complex dielectric constant of 20+i3 with
a radius of 1/20 of a free-space wavelength (A,). The total area occupied
by the square box is scaled to 78.54\?. The transverse electric (‘TE) case is
considered with the angle of incidence @ = 30°. Three cylindrical modes are
needed to represent the scattered field of each cylinder; that is, n = —1,0,
and 1 in (9.4.5). Therefore, we have a total of 12,000 unknowns. We vary the
summation indices (m) in (9.4.5) and (9.4.7) (9.4.9) until the solution con-
verges. We also vary the neighborhood distance rg to observe the changes in
the solution. In (9.4.4), @° is calculated for @ = 1,2, and 3 whose centers are
located at. (x,y) = (—0.0004, —0.0011), (0.2496, 0.2498), and (0.5161, 0.5164)
in Fig. 9.4.3, respectively. For the indirect summation of (9.4.7) using the
SMCG method, we need to identify the neighboring cylinders associated with
each cylinder, to compute the Bessel functions and Hankel functions, and to
perform the convolutions using FFTs. We compare both the accuracy and
the CPU time of the SMCG and those of direct. summation for one iteration.
For the direct summation, we extrapolate the CPU for the 4000 cylinders
from that of the first 40 multiplied by 100. Table 9.4.1 shows the accuracy
of the SMCG method versus direct summation, and Table 9.4.2 shows the
--- PAGE 511 ---
492 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA
Cylinder Sparse-Marix Canonical-Grid Method
a Direct Summation m= 3, ng = 1 m=2,ng=0 m=1,ng=0
I n= 1 ~307.618 + i309.548 —307.618 + 1309.550 —307.478 + 1209.747 —294.812 + 1310.465
O 442.489 + 111.032 442.489 + 111.032 442.497 + 111.013 443.113 + i111.381
1 127.204 — 452.282 -127.204 - 452.848 127.023 - 452.967 141.035 — 1459.339
2n=—1 - 181.995 + i295.316 -181.995 + 295.316 —181.997 + 295.355 —178.900 + i297.484
0 350.850 + 228.2337 350.850 = 128.2336 350.853 + 128.2186 351.379 + 728.3405
1 -146.117 — 822.364 —146.116 — 1322.363 146.148 — 1322.37 150.337 — 1321.097
Bn—-1 162.8564 1155.520 162.856 +£155.519 162.932 + 415.537 162.164 + 160.916
0 42.4817 — 219.952 42.4816 ~ 1219.951 42.4738 — #219.951 42.5461 — 220.327
1 =217.190 + i77.7958 —217.191 ~ i77.7962 —217.260 + 677.7984 —216.326 + 171.9728
Table 9.4.1 Accuracy of the Sparse-Matrix Canonical-Grid Method Versus Direct, Sum-
mation.
Sparse-Marix Canonical-Grid Method
m=3,ng=2 m=2,ng=1 m=1,ng=1 Direct Sum.
Neighborhood sorting time 23 0 0 0
Bessel function 3 2 2 0
Hankel function 31 2 u 0
Strong int. 46 0 0 28,700
Weak int. pre-multipl. 1 1 1 0
Weak int. convolution 58 30 i 0
Weak int, post-multipl. 1 1 1 0
Total CPU (second) 163 55. 26 28,700
Table 9.4.2 CPU time in seconds (based on a Sun SPARC 10) of the sparse-matrix
canonical-grid method ys. direct summation.
comparison of CPU time. It is observed that the SMCG can be faster by two
orders of magnitude for the example presented in this section. This method
can be extended to multiple scattering of many spheres.
--- PAGE 512 ---
REFERENCES 493
REFERENCES AND ADDITIONAL READINGS

Allen, M. P. and D. J. Tildesley (1989), Computer Simulation of Liquids, Oxford University
Press, New York.

Bottcher, C. J. F. (1952), Theory of Electric Polarization, Elsevier, Amsterdam.

Chan, C. H. and L, Tsang (1995), A sparse-matrix canonical-grid method for scattering by
many scatterers, Microwave Opt. Technol. Lett., 8(2), 114-118.

Chew, W. C. (1990), Waves and Fields in Inhomogeneous Media, Van Nostrand Reinhold,
New York.

Chew, W. C., J. H. Lin, and X. G. Yang (1995), An FFT T-matrix method for 3D microwave
scattering solution from random discrete scatterers, Microwave Opt. Technol. Lett., 9,
194-196.

Colbeck, S. C. (1982), An overview of snow metamorphism, Reviews of Phys. and Space
Phys., 20(1), 45 61.

Ding, K. IL, L. M. Zurk, and L. Tsang (1994), Pair distribution functions and attenuation
rates for sticky particles in dense media, 8(12), 1585-1604.

Frenkel, D. and B. Smit (1996), Understanding Molecular Simulation: From Algorithms to
Applications, Academic Press, San Diego.

Hansen, J. P. and I. R. McDonald (1986), Theory of Simple Liquids, Academic Press, New
York.

Hallikainen, M. T., F. T. Ulaby, and T. E. V. Deventer (1987), Extinction behavior of dry
snow in the 18- to 90-GHz range, JEEE Trans. Geosci. Remote Sens., 25(6), 737-750.

Ishimaru, A. and Y. Kuga (1982), Attenuation constant of a coherent field in a dense distri-
bution of particles, J. Opt. Soc. Am., 72, 1317-1320.

Jin, Y.-Q. (1994), Electromagnetic Scattering Modelling for Quantitative Remote Sensing,
World Scientific, London.

Koh, G. (1992), Experimental study of electromagnetic wave propagation in dense random
media, Waves in Random Media, 2, 39-48.

Kranendonk, W. G. T. and D. Frenkel (1988), Simulation of the adhesive-hard-sphere model,
Molecular Phys., 64(3), 403 424,

Kuga, Y., F. T. Ulaby, ‘I. F. Haddock, and R. D. DeRoo (1991), Millimeter-wave radar
scattering from snow: I. Radiative transfer model, Radio Sci., 26(2), 239-341.

Lado, F (1968), Equation of state of the hard-disk fluid from approximate integral equations,
J. Chem. Phys., 49(7), 3092-3096.

Lu, C. C., W. C, Chew, and L. Tsang (1995), The application of recursive aggregate T-matrix
algorithm in the Monte Carlo simulations of the extinction rate of random distribution
of particles, Radio Sci., 30(1), 25-28.

Mandt, C., Y. Kuga, L. Tsang, and A, Ishimaru (1992), Microwave propagation and scat-
tering in a dense distribution of spherical particles: experiment and theory, Waves in
Random Media, 2(3), 225-234.

Maxwell-Garnett, J. C. (1904), Colours in metal glasses and in metallic films, Trans. Roy.
Soc. London, 203, 385-420.

Metropolis, N., A. W. Rosenbluth, N. Rosenbluth, A. H. Teller, and E. Teller (1953), Equation
of state calculation by fast computing machines, J. Chem. Phys., 21(6). 1087-1092.

Polder, D. and J. H. van Santern (1946), The effective permeability of mixture of solids,
Physica, 12, 257-271
--- PAGE 513 ---
494 9 SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA

Ripoll, M. §. and C.F. Tejero (1995), Approximate analytical expression for the direct corre-
lation function of hard dises within the Percus- Yevick equation, Molecular Phys., 85(2),
423-428.

Rosenfeld, 8. and N. C. Grody (2000), Metamorphic signature of snow revealed in SSM/I
measurements, JEEE Trans, Geosci. Remote Sens., 38(1), 53-63.

Sarabandi, K. and P. Siqueira (1997), Numerical scattering analysis for two-dimensional
dense random media: Characterization of effective permittivity, IEEE Trans. Antennas
Propagat., 45(5), 858 867.

Seaton, N. A. and F. D. Glandt (1986), Monte Carlo simulation of adhesive disks, J. Chem.
Phys., 84(8), 4595-1601.

Seaton, N. A. and E. D. Glandt (1987), Monte Carlo simulation of adhesive spheres, J. Chem.
Phys., 87(3), 1785-1790.

Siqueira, P. and K. Sarabandi (1996), Method of moments evaluation of the two-dimensional
quasicrystalline approximation, IEEE Trans. Antennas Propagat., 44(8), 1067-1077.

Stell, G. (1991), Sticky spheres and related systems, J. Statistical Phys., 63, 1203-1221.

Tsang, L., C.-T. Chen, A. T. C. Chang, J. Guo, and K.-H. Ding (2000), Dense media radiative
transfer based on quasicrystalline approximation with applications to passive microwave
remote sensing of snow, Radio Sci., 35(3), 731-749.

Tsang, L. and J. A. Kong (1992), Scattering of electromagnetic waves from a dense medium
consisting of correlated Mie scatterers with size distributions and applications to dry
snow, J. Electromag. Waves and Appl., 6(3), 265-286.

Tsang, L., C. Mandt, and K. Il. Ding (1992), Monte Carlo simulations of the extinction
rate of dense media with randomly distributed dielectric spheres based on solution of
Maxwell’s equations, Optics Lett., 17(5), 314-316.

West, 1, D. Gibbs, L. ‘sang, and A. K. Fung (1994), Comparison of optical scattering
experiments and the quasicrystalline approximation for dense media, J. Opt. Soc. Am.
A, 11(6), 1854-1858.

Veysoglu, M. E. and J, A. Kong (1996), Multi-scale correlation function for random medium
models, Progress in Electromag. Res., PIER 14, 279-315

Zurk, L. M. (1995), Electromagnetic wave propagation and scattering in dense, discrete
random media with application to remote sensing of snow, University of Washington,
Seattle.
--- PAGE 514 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc.
ISBNs: 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)

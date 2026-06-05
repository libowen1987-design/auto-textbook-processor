# Tsang《Scattering of EM Waves》Chapter 6

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 6
THREE-DIMENSIONAL WAVE SCATTERING
FROM TWO-DIMENSIONAL ROUGH SURFACES
1 Scattering by Non-Penetrable Media 270
1.1 Scalar Wave Scattering 270
1.1.1 Formulation and Numerical Method 270
1.1.2 Results and Discussion 273
1.1.3 Convergence of SMFSIA 277
1.2 Electromagnetic Wave Scattering by Perfectly Conducting
Surfaces 278
1.2.1 Surface Integral Equation 278
1.2.2 Surface Integral Equation for Rough Surface Scattering 280
1.2.3 Computation Methods 281
1.2.4 Numerical Simulation Results 286
2 Integral Equations for Dielectric Surfaces 293
2.1 Electromagnetic Fields with Electric and Magnetic Sources 293
2.2 Physical Problem and Equivalent Exterior and Interior Problems 296
2.2.1 Equivalent Exterior Problem, Equivalent Currents and
Integral Equations 296
2.2.2 Equivalent Interior Problem, Equivalent Currents and
Integral Equations 298
2.3. Surface Integral Equations for Equivalent Surface Currents,
Tangential and Normal Components of Fields 300
3 Two-Dimensional Rough Dielectric Surfaces with Sparse
Matrix Canonical Grid Method 304
3.1 Integral Equation and SMCG Method 304
3.2. Numerical Results of Bistatic Scattering Coefficient 318
— 267 —
--- PAGE 290 ---
268 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
4 Scattering by Lossy Dielectric Surfaces with PBTG

Method 326
4.1 Introduction 326
4.2 Formulation and Single Grid Implementation 328
4.3. Physics-Based Two-Grid Method 329
44 Numerical Results and Comparison with Second Order

Perturbation Method 334
4.5 Numerical Simulations of Emissivity of Soils with Rough

Surfaces at Microwave Frequencies 343
5 Four Stokes Parameters Based on Tangential Surface

Fields 350
6 Parallel Implementation of SMCG on Low Cost Beowulf

System 354
6.1 Introduction 354
6.2 Low-Cost Beowulf Cluster 355
6.3 Parallel Implementation of the SMCG Method and the PBTG

Method 356
6.4 Numerical Results 360

References and Additional Readings 366
--- PAGE 291 ---
6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES 269

In Chapter 5, we have applied fast computation methods to two-
dimensional scattering with one-dimensional random rough surface. In this
chapter, we extend the algorithms to three-dimensional problems with two-
dimensional random rough surfaces. Study of three-dimensional scattering
problem is an active research area. For applications, three-dimensional sim-
ulations represent the physical reality and can be used for comparison with
real-life data. With the advent of modern computers, new results of large-
scale simulations are reported continually. We emphasize that the numer-
ical results presented in this chapter are limited to cases when they were
first reported in the literature using computer resources available at that
time. In Section 1, we apply the sparse-matrix flat-surface iterative approach
(SMFSIA) to solve the problem of scalar wave scattering from a 2-D random
rough surface and extend the method to study electromagnetic wave scat-
tering by a two-dimensional perfect electric conductor. Numerical results are
illustrated for incident angles of 10° and 20° and with areas between 256A?
to 1024)? and up to 1000 surface realizations. The cases of rms heights of
0.5A and 1\ are considered. Backscattering enhancement is exhibited for
both co-polarized and cross-polarized components. Comparisons are made
with controlled laboratory millimeter wave experimental data at 20° inci-
dent angle. The advantages of millimeter wave scattering experiments are
that the calibration allows the comparison of scattered power to incident
power [Kuga and Phu, 1996]. Thus, the absolute value of the bistatic scat-
tering coefficient as normalized by the incident power is measured. Thus,
we are able to compare the absolute values of the bistatic scattering coef-
ficient between Monte Carlo simulations and experiments. The comparison
is without adjustable parameters. it is shown that the co-polarized bistatic
coefficient is in good agreement and the cross-polarized bistatic coefficient
is in excellent agreement. Agreement is in terms of both absolute magni-
tude and angular dependence. In Section 2, we discuss integral equations
for dielectric surfaces. In Section 3, electromagnetic wave scattering by 2-D
dielectric surfaces are studied. In Section 4, we consider bistatic electromag-
netic wave scattering from a two-dimensional lossy dielectric random rough
surfaces (3-D scattering problem) with large permittivity. For media with
large permittivities, the fields can have large spatial variations on the sur-
face. Thus a dense discretization of the surface is required to implement.
the method of moments (MoM) for the surface integral equations. Such a
dense discretization is also required to ensure that the emissivity can be
calculated accurately for passive remote sensing applications. We used the
physics-based two-grid (PBTG) method that can give the accurate results of
--- PAGE 292 ---
270 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
the surface fields on the dense grid and also the emissivities. The numerical
results are calculated by using the PBTG in conjunction with the sparse-
matrix canonical grid method (SMCG). The numerical results are compared
with that of the second order small perturbation method (SPM) which is
described in Chapter 1 of Volume III. The comparisons show that a large
difference in brightness temperature exists between the SPM and numerical
simulation results for cases with moderate rms slope.

We also model real-life applications in microwave emission from soils.
The results are calculated at two frequencies, viz., L- and C-bands, using
the same physical roughness parameters for a variety of soil moisture con-
ditions. This has important application because in practice, the same soil
can be measured at different frequencies, different incident angles, and using
both active and passive sensors. The physical roughness parameters of the
medium are independent of these sensor characteristics and should be used
to characterize soils. In the last section, we describe the implementation of
the SMCG/PBTG method in a low cost parallel Beowulf system that was
completed at the City University of Hong Kong [Li et al. 1999, 2000b].

1 Scattering by Non-Penetrable Media

1.1 Scalar Wave Scattering

In this section, we give results of scattering of scalar waves by 2-D non-

penetrable surfaces (3-D scattering problem). The computation is based on

a numerical method called the sparse-matrix flat-surface iterative approach.

The approach decomposes the matrix of the integral equation as a sum of

a sparse matrix, a flat-surface block Toeplitz matrix, and a weak remainder

that is followed by an iterative solution until convergence is achieved.

1.1.1 Formulation and Numerical Method

Consider a tapered scalar plane wave tinc(x,y, 2) impinging upon a 2-D

random rough surface with Dirichlet boundary condition and with a random

height profile z = f(x,y). The incident direction is kj = sin 49 cos 9% +

sin 09 sin é94 — cos 2. It is tapered so that the illuminated rough surface

can be confined to the surface area L x L. The incident field is

Winel@,y, 2) = exp[—ik(cos 49z—z sin A cos Hp—y sin Mp sin d)(1+w)]exp(—t)
(6.1.1)
--- PAGE 293 ---
§1.1 Scalar Wave Scattering 271
where t= t, +ty, and
cos 99 Cos ox + Cos Og Sin doy + sin Bz)?
ty == (£0880 008 60 cos Oo sin doy 02) (6.1.2)
g? cos? Io
ty = (—sin doz + cos oy)? (6.1.3)
g
1 [(t,~1) . (2ty—1)
Y= | >t a 6.1.4
Oe [S cos? 9 * g ( )
and g is the parameter that controls the tapering of the incident wave. The
Dirichlet boundary condition is that the wave function y is equal to zero
on the random surface. A Fredholm integral equation of the first kind can
be formed. Let 7 = éa! + jy! + 2f(«',y') denote a field point and let 7 =
aa + jy + 22 denote a source point on the rough surface. Then the integral
equation is
0= vine) = ff dedyGte.y flew) al a fe WUC) (6:5)
Gklr — 7 ; .
where Go(7,7") = ae is the free-space Green’s function and the
unknown surface field U(a, y) is
2
aw (F) apy? (ary? |?
U(z,y) => |1 > z= 6.1.6
(y= —5, + ar) + lay (6.1.6)
To apply the numerical method, we decompose the integral of (6.1.5) into
three terms. We first, identify the strong interaction neighborhood of rg. Let
p=([(w@—-2')? + (y—y')*]? be the separation between the field point and the
source point on the horizontal plane. Let the flat-surface Green’s function
Gers be
+ , , ror exp(ikp)
Grs(x—2',y—y') =G(2,y,2 = O;0,y',2 = 0) = ip (6.1.7)
Then the integral equation (6.1.5) becomes
ll dadyGg{F.7 )U (x,y) + I dadyGrs(x— 2',y— y/)U(a,y)
pera pra
= viel) = ff dody [Galr.7!)~Geste—a'.y—y)]Uleu) (628)
para
The second term is a 2-D flat-surface convolution integral, whereas the last
integral is a weak interaction because G, and Gy are approximately equal
--- PAGE 294 ---
272 6 3-D WAVE SCATTERING FROM 2-D ROUGI SURFACES
when ry is large. In terms of matrix notation, we write (6.1.5) and (6.1.8),
respectively, as
ZX=5 (6.1.9)
= sb) SS Sw
FF Z (6.1.10)
where Z is the matrix of the original integral equation (6.1.5). In (6.1.10),
Zs
Z 9 is the strong interaction matrix corresponding to the first integral of
(6.1.8). It is a sparse matrix consisting of interactions within a neighborhood
; . «BFS. . A .
of rg. The flat-surface matrix of Gpg is Z » It is a block Toeplitz matrix
s(FS)
so that the product of Z ) with a column vector can be computed by a 2-D
fast-Fourier-transform algorithm. Ze is the weak matrix corresponding to
the last integral on the right-hand side of (6.1.8). The calculation procedure
is, for the first-order and higher-order solutions,
(9) S(FS)] .
[2 47 | XY) 5 (6.1.11)
=(s) =(FS)) Sone z{(n
[2° +2 | xe) pe) (6.1.12)
where
Br) 5 _ xm (6.1.13)
for n > 1. For each order the generic equation to be solved is
sls) S(FS)] x
z 147) | XM =5 (6.1.14)
where the superscript (w) stands for updated. Note that the flat surface
(FS! sls)
Z ) as well as the sparse matrix 7 is on the left-hand side of the general
equation.

The matrix equation (6.1.14) is solved by the conjugate gradient method
(CGM). For each order, we use CGM to solve (6.1.12). The error of the
original exact, matrix equation (6.1.9) is defined by the error norm

ss(n) 5,72
ZX
EO = 2x —5ll x 100% (6.1.15)
\l6l)
In the iteration procedure the iteration stops when a certain error criterion
is reached. We call the method SMFSIA (sparse matrix flat surface iterative
approach). In Section 1.1.3 we examine the convergence of this iterative
--- PAGE 295 ---
§1.1 Scalar Wave Scattering 273
= 0.80
fo ++ ++ 1-D (4000)
& 0.60 ir.
P 0.50 SS
3 4 “
g 0.40 c ws
8 030 Pa os
2 ” “.
8 0.20 a ma
Boi} x,
2 0.00
9 6 3 0 3 0
Scattering Angle (degrees)
Figure 6.1.1 © Comparison of normalized bistatic scattering coefficients of 2-D and 1-D
random rough surfaces (310 and 4000 realizations, respectively) for an rms height of 0.5
and correlation length of 0.707A with incident angle 9 = 20°.
approach. After the unknown U(x, y) is computed, the normalized bistatic
scattering coefficient o(k,) in the direction k, is calculated by a weighted
integration of the surface field. We have
: F (hes) |?
o(ks) = — eon th ol 3 3 (6.1.16)
8n%q2.cos 6 [1 — (1 + cos* 0 + 2 tan? 69)
mareost Bie g? cos? Oy
where
F(ks) = — I dadyU (x,y) exp{—ike sin 0, cos ds
— iky sin 6, sind, — ik f(x,y) cos 5] (6.1.17)
The normalized bistatic scattering coefficient is such that the integration
of it over the 27 solid angle of the upper half-space is equal to unity for
conservation of energy.
1.1.2 Results and Discussion
We use the method to compute the solution of a random rough surface with
a surface area of 80)? and 4096 surface unknowns. The area is L*, with
L = 8.94}. This represents a sampling of 51 points per \”, and a total of
310 realizations are used. The rough surface has an rms height of 0.5. and
a correlation length of 0.707A so that the rms slope is 1, The neighborhood
distance rg is chosen to be 3A.
Figure 6.1.1 shows a comparison of the normalized bistatic scattering
coefficient for the 2-D random rough surface and that of the 1-D random
--- PAGE 296 ---
274 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
}_—=380__{_aseaeaas ao fg | __paszangt |
0.4650497

84.0
04430476 |
0.4276016

78.0
5.8554430 x 107? 14.0

=72.0
7.907978 x 107?
9.0578713 x 107?
0.1029617 22.0 0.3450787
26.0 0.3070970
O.1842503
0.2098318 38.0

=48.0

=440 | 02689258
0.1472065

=36.0
O.1276718

=28.0 0.5533673 60.0.

26.0 9.926586 x 107?

24.0 9.1046810 x 10-?

= 22.0 0.5788418 66.0 8.2607575 x 107?
06030874 68.0 74216217 x 10-2
0.6167714 6.5988846 x 1072
72.0. 57991304 x 10"?
74.0

10.0 78.0

—6.0 0.5672148 2.5101034 x 10°?
2.0536819 x 107?

[8.9 Tt 9083 x 10"?
Table 6.1.1  Bistatic coefficients of the 2-D rough surface of Fig. 6.1.1
--- PAGE 297 ---
§1.1 Scalar Wave Scattering 275
rough surface with the angle of incidence of 6) = 20° and #) = 0°. The
results of bistatic scattering for 2-D random rough surface results are also
tabulated in Table 6.1.1.

For 3-D scattering, the bistatic scattering coefficients are shown in the
plane of incidence with ¢, = 0° or ¢s = 180°. This convention is also used
in Table 6.1.1. The scattering angle is labeled as positive for ¢; = 0° and
negative for @, = 180°. The tapering parameter g is equal to L/3. For the
1-D case the surface length is set at 40 and the results are averaged over
4000 realizations. Backscattering enhancements are observed for both 2-D
and 1-D surfaces, with a peak at @, = —20°. Note that because the surface
area is only (8.94A)?, the incident wave has a half beamwidth of 6°. Thus
there is associated broadening that is due to the beam pattern. From the
results it is also seen that there is no forward peak that is due to the forward
scattering. It should be noted that the integration of the normalized bistatic
scattering coefficient curve of the 1-D surface over 1-D angle 6, is equal
to unity, whereas the normalized bistatic scattering coefficient of the 2-D
surface is only plotted for observation on the x-z plane. The two curves
follow a similar trend, with the 2-D curve always below the 1-D curve. The
2D bistatic scattering coefficient is lower because scattering can occur for
directions off the plane of incidence.

Figure 6.1.2 shows the convergence of the bistatic scattering coefficients
for the 2-D surface versus the number of realizations. The coefficients con-
verge in approximately 310 realizations, which is evident from the fact that
the curves for 310 and 275 realizations overlie each other. The coefficient also
shows that the backscattering peak requires more realizations to converge
than other scattering directions. In Table 6.1.2, we list the error norm and
the number of iterations for each order. For each order of solution in (6.1.12),
a required number of iterations is used for the CGM. For each order of the
SMFSIA the solution is solved by the CGM. The convergence criteria for
both the SMFSIA and the CGM are set at 1%. The number of iterations
required for each order of the SMFSIA decreases with the increase of the
solution order, and at the sixth order the solution error is less than 0.1%.
In Table 6.1.1 we list the bistatic scattering coefficients for the results av-
eraged over 310 realizations to facilitate comparisons with other methods.
Figure 6.1.3 shows a comparison of the second-order Kirchhoff method with
the exact solution. The second order Kirchhoff method uses the Neumann
iteration method and iterate up to second order. The results clearly show
that the second-order Kirchhoff method fails for this case.
--- PAGE 298 ---
276 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
# 0.70
3 ‘Number of Realizations
0.60 LL
' 0 =
x ~
= 0.40 ~
2
£ 0.30
3 0.20
i 0.10
= 0,00
9 60 32 o 08 & 9
Scattering Angle (degrees)
Figure 6.1.2 Convergence of histatic scattering coefficient with the number of realizations
for a 2-D rough surface. Four cases are shown: 155, 225, 275, and 310 realizations, The cases
of 275 and 310 realizations overlap each other.
= 1.00
———this method (310)
0.
: 80 --2::Kirchhott (360)
¥F 060
3
3 040 .
i 0.20 b Renan See
Z 0.00
9 6 3 0 3 ©
Scattering Angle (degrees)
Figure 6.1.3 Comparison between the SMFSIA and the second-order Kirchhoff method.
The second-order Kirchhoff method result is based on 360 realizations.
Order Number of Exror
Number | CGM Iterations | Norm %
2
3 13,
7 1.04
0.12
Table 6.1.2 Convergence of the SMFSIA of 2-D surface of a single realization
--- PAGE 299 ---
81.1 Scalar Wave Scattering 277
For each order of solution the error norm £ can be easily computed
as follows. From (6.1.12) and (6.1.15) we obtain
a ~ ss) s(FS), 4 — Sw) 7 =
(ZX — Fy) = [ZO ZOYX — G-ZORM | = pH HO
(6.1.18)
Table 6.1.2 shows the convergence of the SMFSIA for a single realization.
1.1.3 Convergence of SMFSIA
In actual implementation of the SMFSIA the iteration stops when the error
norm of the original matrix equation has reached the established smallness
criterion. In this section we examine the convergence of the SMFSIA. We
note that the right-hand side 6 corresponds to the incident wave and is
of the order of O(1), where © stands for the order. The column vector
Sw), °
ZX corresponds to the last term of (6.1.8). It is the original impedance
matrix with the removal of the near field sparse matrix and the flat surface
impedance matrix.
—(w)__ , ila 24 42)5 ik
ox) ro) I dady explihs(ag + va + #a)#) _ explikp) U(x,y)
p>ra An(a + y3 + 23)2 4np
(6.1.19)
where ey =a —2!, ye=y— y's 24 = fle,y) ~ fle'sy’) and p= (03 + 99)2.
We note that U(r, y) is of the order kO(1) and has a phase that is randomly
fluctuating, whereas zq is of the order of rms height h. Thus in the limit of
large rg, with rg > h, the first term in the square brackets can be Taylor-
expanded. Therefore we have
Sw , xp(ikp) (ik
oO [2°] =0 (// dady SPEEA) (=) U(«, »|
p>ra 4np 2p
poo pQn i ike?
exp(ikp) (ikz7
=o] d, | dé———— | —* | U(a.y
| ee J, dnp 3p (x,y)
| exp(ik,
=0 | ip POD) in r2U(e, v| (6.1.20)
ra 4p
By performing integration by parts of (6.1.20), we get
(wv) 2
oO [Z| =0 (*) (6.1.21)
Td
which is much smaller than O(1) in the limit of large rq.
--- PAGE 300 ---
278 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
1.2 Electromagnetic Wave Scattering by Perfectly Conducting
Surfaces
1.2.1 Surface Integral Equation
Consider an electromagnetic wave impinging upon a rough surface that is
perfectly conducting. Then the integral equation for 7 above the rough sur-
face is
Aw = [ as’ [v x Ger. 7)-al x H@)] + Hinel?) (6.1.22)
s"
Letting 7 — 7, which is a point infinitesimally above the rough surface, we
have
AXH(F) =AxHino(F)+lim Ax [ as’ [v x Ger) a x H)| (6.1.23)
rary Igy
For a constant vector @
= = 1
Vx G77) a=Vx (7+ pv’) GFF) a
= Vo(F,F) xa (6.1.24)
Using (6.1.24) in (6.1.23), we have
Ax AP) = Ax Hinc(F)+ lim Rr xf ds! [Vg(r.7') x (a! x H(r’)] (6.1.25)
Pore Pa
The integral in (6.1.25) is singular at F = 7’. To handle this problem, we
perform similarly to the Neumann case of Chapter 4, Section 1.5. Let
F=pton (6.1.26)
where f is a point on the rough surface. If 6 > 0,7 =74, andifd <0,7=7..
Thus, 7; is infinitesimally above the surface while F_ is infinitesimally below
the surface. In (6.1.25) and (6.1.26) # is the normal to the surface at point
p. Then
ax H(p) =2x Hine() + lim fx I, ds! [(vatr, cp) a H®)|
(6.1.27)
The f,, integration is divided into a circular disk Sq of small radius a about
p and the rest which is known as the principal value integral
[ ds! = [ ds! +| ds! = i ds! + fas (6.1.28)
JS ISa S-S. So
where f represents principal value integral, which is the integration over S
with an infinitesimal circular disk of radius a, S,, removed from S.
--- PAGE 301 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 279
We next examine
T= imax I a8! (VolFF)) on, x! x HP)
= lim x I as'valr.7)) x (Ax 0) (6.1.29)
+ Se PoFa
where 6 > 0 for 7 = 7, and 6 < 0 for F = 7_. Let (p’,¢’) be the polar
coordinates of 7’ of circular disk of radius a centered about p
a Qn 1
zim f ds'Vg (7,7) = | dp’ pl | WV
a Qn 1
= | ape | dé! setae -7)|
[ A anr FP =
ra Qn “ lm + pl sin bla
5 — (p' cos d'& + p’ sin d’9)
=] dlp [ gl | (2d = (e' cos o' + p sin d'9)
[ PF I “ der (pl? + 52)872
The @ and # components integrate to zero because of the sin ¢/ and cos ¢!
dependence. Thus
[ dS'Vg (7,7) = ad f dp’ —
s. 2 Io PP PERF
1 5 ° a 6
= -nrs |-—,——.| =-5|-— 541
er
where the + sign is for 6 > 0 and — sign is for 6 < 0. Hence
, 2 for Py
| as'Vo(r7) = 4? (6.1.30)
Sa a for T
Thus
A _ ax HF
T=ax I(-3) x (Ax m0] = hx Ho)
with the + sign for F = 74 and — sign for F = F_. Equation (6.1.30) is a
useful integral identity. We have the integral equation known as MFIE:
ax H(F) = 2A x Hine(F) + 2A xf dS'Vg(F,7') x al x H(F) (6.1.31)
$
--- PAGE 302 ---
280 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
1.2.2 Surface Integral Equation for Rough Surface Scattering
The 2-D surface spectrum is given by
. Iplyh? Kee KR .
W(K,, Ky) = Pa exp (-4 - — (6.1.32)
where I, ly, are the correlation lengths in x and y directions respectively,
and kK, and Ky are the spatial frequency in « and y directions respectively.
The incident direction is kj = sin 0; cos 6;% + sin 0; sin dif — cos0;2 and has
a perpendicular polarization (TE incidence). The incident wave is tapered
so that the illuminated rough surface can be confined to the surface area
L, x Ly. The incident magnetic field is then
— 1 +90 +00 .
H,(x,y,2z) = al ak, dk, exp(iket +ikyy—ik.2) Err (Ke, ky)h(—kz)
—o0 -co
(6.1.33)
where
i(—ke) = *= (eh, + phy) + M22 (6.1.34)
OO Rey _
where kz = \/k? —k2—k? and kp = \/k2 + k2. In (6.1.33), Evn(ke, ky) is
the spectrum of the incident wave and we use the following spectrum.
1 90 +00
Epp(kz, ky) = ral dx [ dy exp(—ikea — ikyy)
An? Jin doo
-exp(i(hizw + Riyy)(1 + w)) exp(—t) (6.1.35)
where t = t; + ty = (a? + y*)/g? and
(cos 0; cos jx + cos 8; sin ey)?
_ = (cos cos dee + cos Oy sin day)” A.
te g? cos? 6; (6.1.36)
(—sin dia + cos diy)? :
ty= nr (6.1.37)
1 [(2t2-1) , (2ty-1)
we |S yo 6.1.38
w= E cos? 6; a g ( )
The w and ¢ terms are introduced to approximate the tapered wave solution
that was previously used for the scalar wave case. However, in (6.1.33), we
have a spectrum of electromagnetic plane waves so that the incident waves
obey the Maxwell equations exactly. Let 7 = éa! + gy! + 2f(a',y’) denote a
source point and F = éx + gy + 2f(x,y) denote a field point on the rough
surface. We have the magnetic field integral equation (MFIE) on the perfectly
--- PAGE 303 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 281
conducting rough surface is, as derived in Eq. (6.1.31). Note that
Vg = (F-F)G(R) (6.1.39)
_ GikR — 1) exp(ikR) ]
G(R) = ~~ as (6.1.40)
and R= J@=@ FW VP FU) —F@ a). The MPIE can be
reduced to two coupled scalar integral equations
FAO, ED faatay/G(R)|(a— 2))Fy() ~ (u~ W/)Fet)
F(a! yf
+ fatajerey{ [ce 2E + ee - sew))] Fer)
Fayy’) pm OFM) yy (o -
—(y— 7!) es HY EIN) ey ey
(z-2') ay F,(7') By Hi, (7) — Hay (7) (6.1.41)
and
FAD) OF EU) facta G(R) [C2 — 2 Fy) ~ (uv) Fal)
wal
= f acarour{v- y) LEY) rae)
Of (a'.y!
+ [0-7 E — Ha.) — Hev)] HO}
= PEED (6) + Hal?) (6.1.42)
where
- Of (uy) OFM)". Hey. 5
T)= 4/1 —_— SS a “f 1.42
F,(7) \ + ( oe HE ax A(F)-@ (6.1.43)
and
|, (fan) , (FD). am .4
7") = f\"is ) ry +g 1.44
Fy) 1+( a +(e axH)-g (6.1.44)
are proportional respectively to the « and y components of fi x FH on the
surface.
1.2.3 Computation Methods
(A) SMFSIA
In SMFSIA, we choose rg, the neighborhood distance. Let
pr= Va 2!) + (yy? (6.1.45)
--- PAGE 304 ---
282 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
be the horizontal separation between two points (x.y, f(x,y)) and (2’,y/,
f(a',y')). If the neighborhood distance rq is chosen to be much greater than
the rms height, then the Green’s function G(R) of (6.1.40) is asymptotically
equal to
ikpr — 1) exp(ikp
Grs(pa) = hee Vexwltkon) 7 expt pr) (6.1.46)
mp
Note that Gy»s(pp) is translationally invariant in the horizontal plane. Thus,
we write G(R) in the integrands of the integral equations of (6.1.41) and
(6.1.42) for pr > ra by
G(R) = Grs(or) + (G(R) — Grs(pr)) (6.1.47)
Then the integral equation (6.1.41)-(6.1.42) becomes
Fe) OFC f dala G(R ~2VF 7) YF)
2 Oy Soa<ra
wy!
+ / artay’c(ny{ [te - on ew) + (F(a.y) — fle’, v)| F,(7")
Spare
fy) pa
— (2) SP Ry)
Of (x, ° .
PAE) f aatay Ges(pnyile — 2 )Fy)—(y~ Fe)
Yo Spn2ra
r Of (aly!
+ | delay Grs(on){ [-« - of )Pflaty)
Jpn2ra Oe
7 fey) 5 yor
+ (eu) ~ feat] Fale) = (2 FSP Bey
— PF) be) — HaylF
= py el) — Hi, (7)
Of (a, oI a
- LED f gatay G(R) - Grsion)) le 2')FylP) ~ (w— wFal)
By Spu2re
af(a!,y’
= [deta cr) - Grston)){ [-« — Phew)
pr2ra Ox
, _ x,y!
+(e fe'a)| Be) ~ (e- 2)FEP ayo} 6.148)
and
--- PAGE 305 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 283
E(F) afte
Fo) ONY) fad G(R) [C0 — 2! Fy) ~ (y= v Fel")
2 Oa pr<ta ‘
OF) pg
-[ asl G(R){ (yu) LOY) pe)
pr<Ta
ata. .
+ [W225 — ay - sew] Bu)
Of (x,
LED fal aif Grs(on)lce —2')Fy(t) ~ (wv) Fel)
Gd pn2ra
Of (ey) nn
~ [ astaa’eeston)} (y—v) Oe)
pa2ra a
Of (aly! 7
+ [0-2 - Gen - Kew] Fe
OF OW y(n a
= FED (7) + Heal)
Of (ay 7
+ SEED [date G(R) —Ges(on) lla —2! Fy) ~ y—v Fel)
PR2Ta
¥ OF(e YW)
+f aay rr) - Geston)){y— yn 6)
Spn2ra Ou
Of (aly! oy
+ [rv AS — reea)— stew) ry} (6.1.48)
The last terms on the right-hand side of the integral equations of (6.1.48)—
(6.1.49) are small since rg > h. In terms of matrix notation the SMFSIA
procedure is as follows, The surface integral equations (6.1.41) and (6.1.42)
are cast into a matrix equation by the method of moments. This gives
ZE=5 (6.1.50)
Then, the original matrix is decomposed into the sum of a strong matrix, a
block Toeplitz flat-surface part, and a weak remainder as
Ss) s(FS)  =(w) - .
Cnn ae (6.1.51)
=
In (6.1.51), Z » is a matrix corresponding to the integrals of (6.1.48) and
(6.1.49) with pr < rq. The strong matrix is a sparse matrix. The flat sur-
face matrix corresponds to the second term with Gyg(r) in (6.1.48) and
(6.1.49) with py > ra. The flat surface matrix is a block Toeplitz matrix.
The weak remainder matrix elements consist of the differences of the Green’s
function G(R) - Grs(pr) connecting the two points whose horizontal dis-
tance is greater than rg and corresponds to the last terms on the right hand
--- PAGE 306 ---
284 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
sides of (6.1.48) and (6.1.49). The weak and the flat surface matrix elements
are nonzero only for those points whose horizontal interaction distances are
greater than rg. Next, the matrix equation is rearranged to take an itera-
tive form. The calculation procedure is, for the first-order and higher order
solutions
Ss) =FS -
B47) =5 (6.1.52)
= (FS s(n
ZZ) gory gn (6.1.53)
BD —5_ Zam (6.1.54)
; slFs)
The flat surface impedance matrix Z must be on the left-hand side of
(6.1.53) for the SMFSIA to work for 2-D surfaces. For each order of solution
2), the matrix equations (6.1.52) or (6.1.53) is solved by the conjugate
srs)
gradient method. Note that the product of Z > with X can be computed
by a 2-D fast Fourier transform (FFT) algorithm which makes conjugate
gradient iteration more efficient. The iteration of ZR through (6.1.53)
and (6.1.54) is carried out until the error norm
=n)
ZX’ -b
2 x =I (6.1.55)
Wel
falls below a threshold. In this section, an error norm of 1% is used for all
numerical simulations.
(B) SMFSIA/CAG
We can further improve the SMFSIA by using the flat surface as a canonical
grid (CAG). This method is called SMFSIA/CAG. For the weak remainder
matrix elements, Green’s function is approximately equal to the Green’s
function of the horizontal distance between the two points. Green’s function
can be expanded in a Taylor’s series about the horizontal distance between
the two points.
(ikR — 1)exp(ikR) — (ikpr — 1) exp(ikppr)
G(R) — Gres = Se OF
(R) ¥s(pR) An PR? anph
M ym
= ¥ an(px) (3) (6.1.56)
m=1 PR
where zq = f(x,y) — f(a’, y/). The larger the rq the less number of terms we
need in (6.1.56). In this section, we keep up to the sixth term in the Taylor
--- PAGE 307 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 285
series. In the following, the first 3 coefficients are listed for reference.
2exp(ikpr) . exp(ikpr) exp(ikpr)
= — hk _— 3ik—_,— _ + 3— > 1.5
a1(pr) kK tpn 3ik anf, +3 amp (6.1.57)
.3¢xp(ikpr) gexp(ikpr) _,.exp(ikpr)
r = — iS + OP + 15K
aa(pr) = — tho B2mpn Bap
— 15 2enlikpn) (6.1.58)
820 pp
exp(ikpr) | 15:,3e8P(iKeR) yop 2exP(tkpR)
3 = kapp——— + 10ik° —~—— — 42k* —
as(er) = karo + 10k 1927 pp
pexPliken) , ygexPlikpr) 5
— 96ik ‘ 6 6.1.5
26 o6ap, + i96ap%, (6.1.59)

The important property of above coefficients is that they are transla-
tionally invariant. In terms of the matrix equation, the iterative procedure
is then

= S(FS) +
ZO 4 ZO) gory — per (6.1.60)
6
a) 25- Zoran) (6.1.61)
m=1
where Ze ) is the expanded form of the weak matrix. The updated right-hand
side is calculated by the FFT.

Like the SMFSIA, SMFSIA/CAG has an adjustable parameter rq (the
neighborhood distance). Furthermore, in SMFSIA/CAG there is a second
adjustable parameter, which is the number of Taylor series coefficients of
(6.1.56). These two adjustable parameters of rg and the number of Taylor
series terms are interdependent. They are chosen to optimize the CPU.

The numerical simulation results are presented in terms of the normal-
ized bistatic scattering coefficient as normalized by the incident power

Ea?

Yan(Os. Os) = Ombre (6.1.62)
where a = h (horizontal polarization) and a = v (vertical polarization). The
incident power is

ine 2x? ake
Pre = — dkydky| Err (ka, Ry)|? = (6.1.63)
WD Sky<k k
and the co-polarized and cross-polarized components of €3 are respectively
& = = | dx'dy exp(—ik6") F(a’, y') sin 6, — Fy(a/,y!) cos 6s} (6.1.64)
47°
--- PAGE 308 ---
286 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
hh
ee
05 —— hh-(Mi)
z | y — vinta)
Boal ----+hh-(SMFSIA/CAG)
e* s--->_ vh-(SMFSIA/CAG)
a)
> 03;
£ |
gs |
B02 vh
§ /
8 /
= os 4
2
a
00
“80 60 “40 “20 0 20 40 60 80
Scattering Angle (Degrees)
Figure 6.1.4 Comparison between the SMFSIA/CAG and the full matrix inversion (MI)
result.
and
nik . Of (a! .
= . [aay exo(—ikat)f Fale, y) [ew sin 0, — cos 6, cos ds
An , ce
Of (a,
+ F,(',y') [Pei ina, — cos, sin 6, } (6.1.65)
y By
where §’ = a! sins cos ¢s+y/ sin 0s sin ds + f(x’, y’) cos 0s. The normalization
is such that energy conservation requires the integration of ¥,,, and > ,~ over
solid angles to give unity.
1.2.4 Numerical Simulation Results
We first describe the various numerical accuracy tests of the methods. In the
MoM implementation, we use the pulse basis function and point matching
technique.

To confirm the accuracy of the SMFSIA/CAG, comparison is made in
Fig. 6.1.4 between the normalized bistatic scattering coefficient obtained by
the exact matrix inversion (MI) with the solution obtained by the SMF-
SIA/CAG. The results are for a single surface realization. Surface lengths in
the x and y directions are Ly = Ly = 8.0. The rms height is h = 0.5, with
correlation lengths of l,, = ly = 1.0. The surface is sampled at 16 points per
? to give 2048 surface unknowns. The neighborhood distance rq is 3.52. It
can be observed from Fig. 6.1.4 that both co-polarized and cross-polarized
components of MI and SMFSIA/CAG curves completely overlap each other.
--- PAGE 309 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 287
CPU
— 42 hours
SMFSIA/CAG 8 hours
Table 6.1.3 CPU comparison (based on a SUN SPARC10).
Figure |ra(A) |g |Laz = Ly (A) |pts/d?
6.14 | 35 [L,/3 8.0 16 | 2048); 1
6.158 i [32768 [1
6.1.5b | 1.0 |£,/3! 16.0 0.6
—
bas [ae ey2[ 60 ofan reo fos [10
6.1.9 [26 [oo | 160 | 6a [s27e8 [495
|
Table 6.1.4 List of parameters for the simulations.

The SMFSIA/CAG represents an improvement over the SMFSIA in
terms of the matrix solving time. In Table 6.1.3, the matrix solving time
is given for the case of 32768 surface unknowns for a single surface realiza-
tion. The run times are for a SUN SPARC10 workstation. Surface lengths
are L, = Ly = 16A with an area of L? = 256\2. This represents 64 sam-
ple points per \?. The rms height is h = 0.2, with correlation lengths of
1, = ly = 0.6). For these surface parameters, rg is 1.0. From Table 6.1.3, it is
observed that SMFSIA/CAG is 5 times faster than the SMFSIA. The results
of Figs. 6.1.5a show that both methods give the same bistatic scattering coef-
ficient. It should be noted that when compared to the SMFSIA, the efficiency
of the SMFSIA/CAG will be improved even more for those cases involving
larger surface areas than the 256? given in this example. This is because for
given rough surface statistics, as the surface area increases CPU for the weak
matrix multiplication step becomes more dominant. SMFSIA/CAG speeds
up the computation of the product of the weak matrix and the column vec-
tor. In Fig. 6.1.5b, a Monte Carlo simulation result of Fig. 6.1.5a is presented
for an ensemble average of 280 realizations.

We will show convergence of bistatic scattering with respect to the num-
ber of surface realizations, surface size, surface sampling rate and tapering
parameter. In Table 6.1.4, all the numerical parameters used for the results
illustrated in various figures are tabulated.
--- PAGE 310 ---
288 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES

10 7

2 += hh{SMFSIA/CAG) =
3 07, | === vh{SMFSIA/CAG) Bos — th
sc 3
Boa! 3°
Boat Bw
a 3
Bo g” ueesee nee
a or ar a a a
‘Scattering Angle (Degrees) ‘Scattering Angle (Degrees)
fa) (b)
Figure 6.1.5 (a) Comparison between the original SMFSIA and SMFSIA/CAG for 1
realization. Rough surface parameters Ly = Ly = 16\, h = 0.2A, ly = ly = 0.6, and incident,
angle 6; = 10° and 4; = 0°. (b) A Monte Carlo simulation result with SMFSIA/CAG and
280 realizations.

The convergence of the solution of the matrix equation is defined with
respect to the error norm of the matrix equation (6.1.55). The error norm
criteria of < 1% is satisfied for each surface realization.

In Fig. 6.1.6, the averaged normalized bistatic scattering coefficients are
plotted for various numbers of realizations (272, 432, and 1000). Surface
lengths in the x and y directions are Ly = Ly = 32A\(Ly x Ly = 10242)
with a surface rms height hz = hy = 0.5\ and correlation lengths of ly =
ly = 1.0A. The surface is sampled at 16 points per \? to give 32768 sur-
face unknowns. The neighborhood distance rg is 2.6. The incident angle
is 6; = 10° and ¢; = 0°. The tapering parameter g is equal to Lz /2. The
computations were carried out using the IBM SP/2 at the Maui High Per-
formance Computing Center. On the average, for the case of 32768 surface
unknowns, it takes approximately 2.4 CPU minutes per realization. Figure
6.1.6 shows that after 272 realizations, for scattering angles away from the
backscattering angle of —10°, the result shows convergence. Note that the
backscattering enhancement peak converges last. It takes many more real-
izations, usually between 400 to 1000 realizations as shown in Fig. 6.1.6, for
the enhancement peak to be well defined.

Figure 6.1.7 shows a comparison between a smaller surface area of 256.7
(650 realizations) and 1024? case (1000 realizations). The result shows good
agreement including the backscattering direction. A convergence of scatter-
ing coefficient with respect to the surface area is a necessary condition in sim-
ulations. Other important convergence tests are with respect to the number
of sample points representing the rough surface (Fig. 6.1.8) and with respect
to the tapering parameter g (Fig. 6.1.9). In Fig. 6.1.8, the cases of 256A? area
--- PAGE 311 ---
§1.2 Electromagnetic Wave Scattering by Perfectly Conducting Surfaces 289
| hh (272)
5 , vh (272)
2 ----- hh (432)
= os 4 s---- vh (432)
8 hh — hh (1000)
2 — vh(1000)
£ A
§ 02 ‘
Ei
a a
Q os p <
S {
2
ao
00 &
a a a eT)
Scattering Angle (Degrees)
Figure 6.1.6 Backscattering enhancement of cases with h = 0.5 and ly = ly = 1,0.
Surface parameters are Ly = Ly = 32A (Ly x Ly = 1024?) and the surface is sampled at
16 points/A? (rg = 2.6, 6; = 10°, @; = 0° and g = L,./2). Convergence with respect to the
number of realizations is shown.
sampled at 64 points per \? and 256? area sampled at 16 points per \? are
given. Good agreement between the two cases establishes the sampling rate
needed in Monte Carlo simulations with the moderate incident angle and
moderate rms slope of this example. In Fig. 6.1.9, a tapered plane wave with
a tapering parameter g = L,/2 and a plane wave (g = oc) incident on a
rough surface with area of 256\” are compared. A plane wave incident case
has diffraction contributions from the boundary edges of the rough surface.
However, the result agrees with a tapered plane wave case in Fig. 6.1.9. This
illustrates that for these combinations of rms height and corrclation length,
the bistatic scattering is large for the scattering angles of interest and the
edge diffraction levels are negligible. Furthermore, it shows that the spot size
of the incident tapered wave is large enough for the two cases to agree.
For h = 0.5A and | = 1.0A cases of Table 6.1.4, we compare in Table
6.1.5 the average error defined by the equation
1 (8s) = woe
average error(%) = —— Sl | x 100 6.1.66
ge erxor(%) me 710.) 61.88)
for Figs. 6.1.7, 6.1.8, and 6.1.9. In the above equation, N, is the number of
realizations, (0;)i000 is the bistatic scattering coefficient of the 1000 realiza-
tion case of Fig. 6.1.6, y(,) is the bistatic scattering coefficient of Figs. 6.1.7,
6.1.8 or 6.1.9, and Ng is the number of scattering angles.
In Fig. 6.1.10, the normalized bistatic scattering coefficient in the plane
of incidence for the 1-D random rough surface, 2-D surface with scalar inci-
--- PAGE 312 ---
290 6 3-D WAVE SCATTERING FROM 2-l) ROUGH SURFACES
._* ----+ hh (256)
5 . -----vh (256)
2 al —— hh (1024)
5 09 —— vh (1024)
° hh J
o
2
z ...|
5 |
8
6 j x
2 oo)
s | .
B
3
0,9 bebe
cr a a a ae ee ee rT)
Scattering Angle (Degrees)
Figure 6.1.7 Convergence with respect to area (Liz = Liy = 16A, Liz x L1y = 256A?
and Lge = Loy = 32, Lax x Loy = 1024.7). Other parameters are those of Fig. 6.1.6. The
surfaces are sampled at 16 points/A?.
~~ -—- hhh (64)
5 4 s-->vh (64)
2 HAS — hh(16)
= os — vh(t6)
8 thf
2 ri ¥
3 02 i %
2 y
8
7)
2 ow
s
2
a
0.0 a
“60-60-40 -20=C« CSCO
Scattering Angle (Degrees)
Figure 6.1.8 Convergence with respect to the surface sampling rate of 64 points/? (Li, =
Liy = 16A, Lis x Liy = 25647) and 16 points/A? (Laz = Ley = 16A, Lae x Loy = 2562).
Other parameters are those of Fig. 6.1.6.
number of realizations | % error co-pol. | % error cross-pol.
as) 5.8
769 8.8 7.0
495 9.3 14.2
Table 6.1.5 Average error respect to 1000 realization case of Fig. 6.1.6.
--- PAGE 313 ---
§1.2 Blectromagnetic Wave Scattering by Perfectly Conducting Surfaces 291
o4
4 —— hh (Plane Wave)
3 — vh (Plane Wave)
= os ----= hh (g=L/2)
8 o--->vh (g=L/2)
8 hh
2
2
§ 02
F=4
S
8 | A
2 | iN
g on 4 OS .
3 y, Sey ;
0.0
80-60 «40-2020 2=« 0 SCSCO
Scattering Angle (Degrees)
Figure 6.1.9 Convergence with respect to the tapering parameter g for 64 points per
square wavelength sampling. For g = L;/2, the Lz = Ly = 16) result of Fig. 6.1.8 is used.
The g = oo case is for 495 realizations with L; = Ly = 164. Other parameters are those of
Fig. 6.1.6.
os
=
07
8 1D
= os ----- 2-D Scalar
8 os —— 2D Vector
© os os
£ va sn
5 4] f \
§ 03) a \
a a N
g 02 a oN
@ oF ee
a Sey
oo a
cr a eT)
Scattering Angle (Degrees)
Figure 6.1.10 Backscattering enhancement of three cases: 1-D, 2-D scalar wave incidence,
and 2-D electromagnetic wave incidence. Comparison of normalized bistatic scattering coef
ficients for rms height of 0.5A and correlation length of 1.0A with incident angle 6; = 10°
and 4; = 0°
dent wave, and the 2-D surface with electromagnetic incident wave are com-
pared. The incidence angle is 0; = 10° and @; = 0°. The tapering parameter
g = L/3 for the 2-D surface with scalar wave incidence, g = L/2 for the 2-D
surface with a electromagnetic wave incidence, and L/4 for the 1-D surface.
In the 1-D surface simulations, the surface length is set at 40 for an ensem-
ble average of 4000 realizations. For the scalar wave scattering from a 2-D
--- PAGE 314 ---
292 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
05,
g —— hh (SMFSIA)
Soa) —— vh(SMFSIA)
= ----- hh (Experiment)
8 -----_vh (Experiment)
D> 03 RN
£ aS
E ~
® 02 \
8 .
ao
g
mw «(Of | =
g .
a =
00 oe
‘2 60 «-40«-20=«CCSC«iSCéO
Scattering Angle (Degrees)
Figure 6.1.11 Monte Carlo simulation comparison of SMFSIA and experimental data of
backscattering enhancement. For SMFSIA an area of 1024 square wavelength with tapering
g = Lx/2. The surface has an rms height of 1\ and correlation length of 2
surface with area of 81\*, an ensemble average of 674 realizations is taken.
For the electromagnetic wave scattering case, the co-polarized component of
Fig. 6.1.6 is given as a comparison. Three curves follow a similar trend for
all scattering angles. Backscattering enhancement at —10° is observed for all
three cases. For the 2-D surface cases, the scattering coefficient is lower at
all angles than the 1-D case since the scattering can occur for directions off
the plane of incidence. The co-polarized scattering coefficient of the electro-
magnetic case is less than that of the scalar wave due to a significant amount
of energy converted into the cross-polarization component.

We next compare with a controlled millimeter wave laboratory exper-
iment (Kuga et. al. 1993; Kuga and Phu, 1996]. The rough surface is a
Gaussian random rough surface with a Gaussian correlation function. It has
arms height of 1\ and correlation of 2A. The incident angle is 20° from the
normal. In Fig. 6.1.11, the Monte Carijo simulation results of both experi-
mental and numerical results are given. The numerical simulation is carried
out with tapering g = L,/2, Lz = Ly = 32\(Ly x Ly = 10247), and 16
points per \* sampling (32768 surface unknowns). In the experiment, the
calibration is done by using a electric conductor so that the scattered power
can be compared with total power. Thus, the absolute order of the bistatic
scattering coefficient as defined by (6.1.62) is measured in the experiment.
Therefore, with this set-up, it is possible to compare the absolute order of
bistatic scattering coefficient between numerical simulation and experiment.
Both Monte Carlo simulation and experiment show backscattering enhance-
ment for both co-polarized and cross-polarized components. The co-polarized
--- PAGE 315 ---
§2 Integral Equations for Dielectric Surfaces 293
scattering is in good agreement. The cross-polarized scattering is in excellent
agreement. The comparison is excellent in view of the fact that the absolute
values are compared and there are no adjustable parameters. Backscatter-
ing enhancement is a result of the contributions of the cyclical scattering
processes (see Chapter 8 of Volume III) which begin at the second order.
For co-polarization, the second-order terms can be obscured by the presence
of first-order scattering. However, for cross-polarization, the first-order scat-
tering is zero. Thus, the second-order backscattering enhancement is more
clearly exhibited as seen in the simulations and the experimental data.
2 Integral Equations for Dielectric Surfaces
2.1 Electromagnetic Fields with Electric and Magnetic Sources
In formulating integral equations for electromagnetic wave scattering, a con-
venient method is through the use of equivalent electric and magnetic cur-
rents [Harrington, 1961; Wang, 1991]. _
For the Maxwell equations with electric sources of current density J,
volume charge density p,, and surface charge density ps
Vx E= twp (6.2.1)
Vx = -iweh + J (6.2.2)
VE = py (6.2.3)
V- pH =0 (6.2.4)
V-J—iwp, =0 (6.2.5)
Vs-ds—iwp; =0 (6.2.6)
where V,- J, is the surface divergence of J,. Vector potential A and scalar
potential ® can be employed.
a= _l =
H= ma xA (6.2.7)
E=iwA—-Vo (6.2.8)
Using the gauge condition
1=_.
a -A=iwed (6.2.9)
Then
(V? +k) A= pd (6.2.10)
3 3 Dy
(V2 +42) >= -% (6.2.11)
--- PAGE 316 ---
294 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Using the Green’s function
, iklF "|
9 (7,7) = FoF (6.2.12)
we have
Ar) =p | ar'g (7,7) 7 (P) (6.2.13)
1
OF) == [as 7’) po ®) (6.2.14)
The magnetic field is
H=vx [ earn) =- [evar x I) (6.2.15)
The electric field is
= = 1
E(F) = iwp [as (Pr) 7 (7) -V= [as (FP) po (®)
J €y
‘ = 1 =
= nop | rg (FF) IF) + BV | arg (RF) VT | (6.2.16)
The fields are expressed in terms of electric current or in terms of electric
current and electric charge.
__ For the case of equivalent magnetic sources of magnetic current density
M, volume charge density m, and surface charge density ms, the Maxwell
equations are
VxE=iwpH-M (6.2.17)
V x = -iwek (6.2.18)
V-cE=0 (6.2.19)
V- pH =m (6.2.20)
V-M—iwm=0 (6.2.21)
Vs: M, —iwms =0 (6.2.22)
Vector potential F and scalar potential ¢ can be employed. Derivation is
analogous to that of the electric source case
— 1 =
B=--VxF (6.2.23)
H = -iwF —Vu (6.2.24)
The gauge condition is
i
=<V-F = iwpr (6.2.25)
€
--- PAGE 317 ---
§2.1 Electromagnetic Fields with Electric and Magnetic Sources 295
Then
(V4k)F=-M (6.2.26)
(WR) e= - (6.2.27)
Fr) =« / dr'g (7,"°) M (F*) (6.2.28)
Fi
WF) = i [es (7,7) m (7) (6.2.29)
The electric field is
Er) = -V x [os (77) M (7) = ~ [avs (77) x M (7) (6.2.30)
and the magnetic field is
a . ty (eo) UE ry m(7)
H(r) = ive [ ora (77) M(r)-V [aoe
= iwe [eratrry Me) + By [ao er)v @)| (6.2.31)
The fields are expressed entirely in terms of magnetic current or in terms of
magnetic current and magnetic charge.
When both electric and magnetic sources are present, Eqs. (6.2.16)-
(6.2.15) and (6.2.30) (6.2.31) are combined to give
Ber) = - | ar'Vg (7,7) x 1 (F’)
a 1 _
+ twp || ens (FP) I(r) + av | (77) v'-7)|62.32)
_ — 1 =
A (7) = iwe [/ dr'g (7,7) M (F’) + py [es (7) VM @)|
+ [ava (rr) «I (”) (6.2.33)
The boundary conditions separating two media of 4, €, and pg, €2 with
surface electric and magnetic sources are
ax Ey ~-ix Ey =-M, (6.2.34)
ax A, -ax Hy = Js, (6.2.35)
fi €1B —fi- egB2 = ps (6.2.36)
fi Hy — ft: poH2 = ms (6.2.37)
--- PAGE 318 ---
296 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
. E, =E:+E.
incident wave
Hy -H; +H, | scattered wave
HNN 4 EH,
Region 1
€2, 2
Region 2 Ea, Aa
Figure 6.2.1 Scattering of waves by dielectric surface: Physical problem, no surface sources.
2.2 Physical Problem and Equivalent Exterior and Interior Prob-
lems
Consider an incident wave with electric field E; and magnetic field H;
(Fig. 6.2.1) on an dielectric surface. Let €1, j41 be the permittivity and per-
meability respectively above the surface and €2, j12 be the permittivity and
permeability respectively below the surface. This is the physical problem.
Tn region 1, the electromagnetic fields are
Fi =E;+ Fs (6.2.38)
H, =H;+H, (6.2.39)
In region 2, the electromagnetic fields are Ez and H. ‘The boundary condi-
tions are
Ax Fy —-ax B2=0 (6.2.40)
ax Hy) -nhx H2,=0 (6.2.41)
ft-€,E1 —t-€g2E. =0 (6.2.42)
fi Hy — f+ poH, =0 (6.2.43)
Because this is a dielectric surface, there are neither surface currents nor sur-
face charges at the boundary separating regions 1 and 2. Hence we have the
boundary condition of (6.2.40) (6.2.43). The physical problem can be rep-
resented by the exterior problem and the interior problem using equivalent
surface currents and charges.
2.2.1 Equivalent Exterior Problem, Equivalent Currents and Integral Equa-
tions
Consider the equivalent exterior problem A with the same incident electric
field E; and magnetic field H; and same electric field £) and magnetic field
Hy in region 1 as in the physical problem. In the equivalent problem A, let
--- PAGE 319 ---
§2.2 Physical Problem and Equivalent Exterior and Interior Problems 297
. E,=E,+5,
incident wave a
H, =H, +7, | scattered wave
Region 1
Surface sources
Mix A
Region 2 ms pt a0
a Bs Hi =0
Figure 6.2.2 Equivalent problem A, exterior problem with M4, 74, pA, ma.
there be equivalent sources on the boundary (Fig. 6.2.2)
-M4 =axE, (6.2.44)
Tisaxl (6.2.45)
pi=a- ek, (6.2.46)
ma =n: inf; (6.2.47)
Because of these equivalent sources, we have
ax EF, -ax Ey =-M4 (6.2.48)
ix Hy, -nax Hy =T4 (6.2.49)
fi-e:By heb = p4 (6.2.50)
fe wy Hy — ii: joHy =m (6.2.51)
Using (6.2.44) (6.2.47) in (6.2.48)-(6.2.51), we have E} = 0, and H? =0
at the boundary. By Huygen’s principle
ES =0 (6.2.52)
Hi =0 (6.2.53)
everywhere in region 2.
The scattered field generated by these equivalent sources are
E,(F) =- / dS'V 9; (7,7) x ME (7)
aA 1 a
+ fay [fea (7) TW) +pBV [asian (7) VoTs @)
‘1
(6.2.54)
--- PAGE 320 ---
298 63D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Wom) 5 yf oy GA 1 a =A
H(F) = iwe, [fsa (77) M, ()+ pV [asia (7,7) V's My @)
+ | dS'V 91 (7,7) x 2 (*’) (6.2.55)
where
- eikilFF)
7,7) = —— 6.2.56
nr) anlF —7| (6.2.56)
The equivalent sources radiative into all of space. As these equivalent sources
radiate into region 2, these fields will cancel the incident fields to give EY =0
and Hi = 0. Note that region 2 also has €; and j1; as region 1.
For 7 in region 2, we thus have the E equation from the extinction
theorem, £; + Fs = 0:
= [asta (7) x HES () +o [saer7@)
1 a sA Biz nop
+ BV | dS! (FP) V's Te ) =-E\(r) (6.2.57)
and for F in region 2 the H equation from the extinction theorem, H;+H, =
0:
— 1 a4
iwet [[os'n (7) Ms ()+ pv [asta @r) VM 2)
Tu
+ | dS'Vqn (77) x To (#!) = —Hdr) (6.2.58)
We can verify that these equations are identical to those based on vector
Green’s theorem and dyadic Green’s functions in previous chapters. Note
that the Green’s function g; is used in Eqs. (6.2.57) and (6.2.58) for 7 in
region 2. There are 6 scalar integral equations above. However, they are not
independent and just. by themselves cannot be used to calculate the unknown
surfaces fields. This is obvious because pa, €2, and go are not involved in the
equations. Thus we also need the interior equivalent problem.
2.2.2 Equivalent Interior Problem, Equivalent Currents and Integral Equa-
tions
Consider the equivalent problem B with the same electric field Hy and mag-
netic field H2 in region 2 as in the physical problem. At the boundary we
introduce equivalent sources (Fig. 6.2.3). With i; = —n
—M® =n; x Bo (6.2.59)
--- PAGE 321 ---
§2.2 Physical Problem and Equivalent Exterior and Interior Problems 299
zB
Ep=0
Region 1 5
‘egion #20
ae
in Surface sources
Mes. Eom
Region 2 mE pP >
Figure 6.2.3. Equivalent problem B, interior problem with M2, J... p2, m8.
—BOo. oe
Te = ny x Hy (6.2.60)
pe = iy Bs (6.2.61)
mB = Ay: oH (6.2.62)
Because of these equivalent sources, we have
Ey =0 (6.2.63)
H? =0 (6.2.64)
in region 1.
The field generated by these equivalent sources are
E'@ =- | dS'VonFF) x MP (F) + inns [ / a8'go(7,7°)I2 )
y4y ‘as’ a Py, gF (Fe 5;
B (FF YV'sF, (7) (6.2.65)
oan
— eee 1 —_
He! (7) = iweg [ | dS! (rTM (P) +59 / 45'9\(7,7)V', MEE @)|
2
+ | a8'Von(r.7) x To (7) (6.2.66)
where
__ eike|r—F"| ok
RFF) = Por] (6.2.67)
‘These equivalent sources radiative with the Green’s function gz into all of
space. As these equivalent sources radiate into region 1, these fields will give
EP =Oand A = 0. Note that we also have ¢2 and pg for region 1 as well.
Thus, for 7 in region 1, we have the E equation from ore =0
- / dS'Vgo(F,7") x MP (7)
tiene! [as'oa(e,7)7° (P)+AV [as'qolF, PV's Te (F)| <0 (6.2.68
wp! | dS"go(F,F) J, "+B dS PFTFV' s-JF, (FY) = 2.68)
--- PAGE 322 ---
300 6 3:.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
and for 7 in region 1 the H equation from ci =0
x7 1 ¥ =

iwen [ / dS'go(F,F Me (7) + BY / dS! g2(F, PV's Me |

+ | dS'Vgo(F,7") x TP (#) =0 (6.2.69)
There are six scalar integral equations above. Note that in (6.2.68) and
(6.2.69), the Green’s function go is used for F in region 1. However, they
are not independent and just by themselves cannot be used to calculate
the unknown surfaces fields. This is obvious because 4), €1, and g) are not
involved in the equations. Neither is the incident field involved in (6.2.68)
and (6.2.69). Thus we also need the exterior equivalent problem.

Because of the continuity of tangential E and H, and continuity of nor-
mal D and B for the physical problem, and fi; = —?, we have the following
relations between equivalent sources A and B.

M4 = -M? (6.2.70)
yi=-7? (6.2.71)
ps =—pe (6.2.72)
ma = —m8 (6.2.73)
for the equivalent sources between problems A and B.
2.3 Surface Integral Equations for Equivalent Surface Currents,
Tangential and Normal Components of Fields
Surface integral equations are obtained by taking various combinations of the
interior and exterior integral equations. As we discuss earlier, both integral
equations from the exterior problem and from the interior problem need to
be included. Let:
74 =a point on the surface but in region 1 (infinitesimally close) (6.2.74)
7_ =a point on the surface but in region 2 (infinitesimally close) (6.2.75)
Define
M, = M4 = -Mf =F xi =Boxi (6.2.76)
J, = Ts = 7? =x Hy =ax Ay (6.2.77)
Ps = Pe = — pe =A By =f eB (6.2.78)
m, = m4 = —m® = f- Ai = fi pHs (6.2.79)
Thus M, and J, represent tangential electric ficld and magnetic field for
the physical problem, where p; and m, represent normal components of D
--- PAGE 323 ---
§2.3 Surface Integral Equations 301
and B for the physical problem. Suppose we take the tangential E equation
for exterior problem equation (6.2.57) and the tangential H equation for the
interior problem equation (6.2.69),
[- [esa (F..7) x Ms | + iwpy [/ dS'g (F_.7)Js (F’)
tan
1 i > Rte
+ BY | Sarre T @)|, = [-Ei? Jian (6.2.80)
an
i: = 1 f —_
iw | dS'go(F4.,7)Ms (F) + BY | dS! 9(F4,F')V's-Ms |
J tan
- | [ast vantr7) x Js )| =0 (6.2.81)
tan
where subscript “tan” means the tangential vector components. From
(6.1.30), we know that for a small circular disk $, around the point 7 on the
surface, we have
| dS'Vo(rs,7') = 5 = — i as'Vo(F_.7") (6.2.82)
Sa IS.
Then
[-§ «Mi, «| + [- | aS'V9(F,7") x Me |
2 P tan
= i _
+ ional fas'o(r.7 97. (+ pv [as'alrr VT. @)|
i tan
=FR san (6.2.83)
“ive fas'on(r.7)M (7) +90 [as ont, PV's Ms @),
J ’ tan
- [/ dS'Vg0lF,F") x Ts | + 5 x 7, (7F) =0 (6.2.84)
P tan
where Jf, = principal value integral. Also
ax M,=E-f(h-E) = Ein (6.2.85)
axJ,=-H+n(i-H) = —Aian (6.2.86)
Thus the above contains 4 scalar equations for the four scalar unknowns of
the surface electric and surface magnetic currents. Standard MoM techniques
can then be applied. For example, using Galerkin’s method and the Rao-
Wilton-Glisson (RWG) basis functions [Rao et al. 1982], matrix equations
can be readily obtained.
--- PAGE 324 ---
302 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Surface integral equations can also be obtained for the 6 electromagnetic
field components which is also known as the Stratton-Chu formulation. We
take the the cross product of # and the H exterior equation (6.2.58), and
the cross product of 7 and the £ interior equation (6.2.68)
—_ 1 —
iwerix [ / as'o(r_,7)M. +9 | aS! (F,7)V'o Me 8)
1
+n x [esvar7) x Js (7) = —A x Hi (F) (6.2.87)
aX [es'vontrs.7) x M, (F’)
iwpigh aI [esa P)Ts ()+Y [aston TW T. (r)}-0 (6.2.88)
2
Note that
fix | dS'Vg(F4,F') x Q(F)
Se
=-ax G x a0) =-h «| dS'Vg(F_.F) x Q(") (6.2.89)
Sa
ax | aS'V9(Fs.F)P (F)
Sa
=-A «ff dS'Vg(F_,7)P (F’) =a x (-5) =0 (6.2.90)
Su
Thus
ax [ aS'VgiF_.7") x FP)
So
n f&os\)_i., 5 Te Axi -
=nx G x1.) = gh(ieJs)— Fy (6.2.91)
ax [ dS'V92(74,7") x M, (7) = —a x G x M.) = a4 (6.2.92)
IS.
Using the surface integral equations from (6.2.89) (6.2.92) in (6.2.87)-
(6.2.88),
iweyftx | [sur roM, (+g [ as'Valr V's Me @)
{JP
ix HF = =,
~ 8x20 tax [ dS! (VaulF_.7) x J, (F)] = ax Hi)
JP
(6.2.93)
--- PAGE 325 ---
§2.3 Surface Integral Equations 303
~RXEO vax [ dS! [VoalFy.”) x MF. (|
P
= 1 _
~ ipa fosars, PIs Pgs | dS'Von(Fs,7)V'o-Te a) =0
Q/P
(6.2.94)
We next introduce normal components of surface fields that correspond to
surface charges
V's My (7) = twm, (7) = iwh! + A, (7) = iwh!- 2H (7) (6.2.95)
V's-Js (7) = iwps (7) = wit’ Ey (7) = iwi! Ey (7) (6.2.96)
Remember that tangential electric fields are continuous and normal compo-
nents are discontinuous. Rearranging terms and also using Vg = —V‘g we
get from (6.2.93) and (6.2.94),
ax [ [es icra rylel<B @))- [asc ryn-Fy a)
P
ix HF = —
- mei) +x | aS! [Vi (F,7') x (i! x H(?))] =a x Hi)
P
(6.2.97)
=< - Lax [ dS! [V'g(F,7) x [al x EB (F’)]]
P
ax [ / AStisprga(@, 7) (A! <H (P)) + 2 | aS'V'go(7,F)A" By |
2JP
=0 (6.2.98)
To complete the picture, we need normal FE and LH equations. ‘To do that,
we take normal dot product with the E exterior equation (6.2.57), and the
normal dot product with the H interior equation (6.2.69)
he [svar x ME (r')
= 1 =
+ iwpyi- f [ aS! (7,7)! (F") + BY | aS'g\(F_.7)V', Te @)|
= -A-E; (7) (6.2.99)
— 1 —
iwenh- | dS'qo(F,7')Me (F’) +2V | dS'9(F,.F)V'p- Me @)
2
+h fesvar, P) xT? (F) =0 (6.2.100)
--- PAGE 326 ---
304 6 3:D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Using similar techniques to the tangential components case, and separating
out the principal values, (6.2.99) and (6.2.100) become
_ a By (F
A | as'V'gi(F,7") x [il x E(F)] + EE}
P
-A- [ asticungstt.r) [nl x A ()] +f as'v'q (779) [w-F @))]
y JP
=A- Ei (F) (6.2.101)
-a. | [isticcartt,7) [-al x Bp] + [as'v'eae.r) [w: oy, @)]]
P 2
_ 1 _
+i f as'V'oatr.7) x [it x) 3 [i “A, | =0 (6.2102)
P 2
Thus we have six scalar equations in (6.2.97) (6.2.98) and (6.2.101) -(6.2.102)
for the six field components of A x £), A x Hi, A+ Fy, and A- Ay.
3 Two-Dimensional Rough Dielectric Surfaces with Sparse
Matrix Canonical Grid Method
3.1 Integral Equation and SMCG Method
Consider an electromagnetic wave with fields E;(x,y, z) and Hij(x,y, 2) im-
pinging on a 2-D rough surface with a random height profile z = f(x,y).
Above the rough surface is a free space (region 1) while the subsurface is
characterized by permittivity €, and permeability jy (region 2). The height
function z = f(x,y) is a random process with zero mean. The incident direc-
tion is kj = sin 6; cos ¢;% + sin 6; sin df — cos 6,2. The incident field is given
as
_ p+o0 +00
E,(2,y,2) = | dky [ dky exp(iket + ikyy — ik.z) Err ke, ky)e(—kz)
J—co Jo
(6.3.1)
where
é(-kz) = A ek, — jkr) (6.3.2)
Ky
and incident magnetic field is given by (6.1.33). We use the same spectrum
Eru(kz, ky) as given by Eqs. (6.1.35) (6.1.38). Let 7 = #2’ + fy! +2f(2',y’/)
denote a source point and 7 = a + jy + 2f(x,y) denote a field point on the
rough surface. ‘Then the integral equations on the dielectric rough surface
using the 6 scalar components are, from Section 2 and repeated below for
--- PAGE 327 ---
§3.1 Integral Equation and SMCG Method 305
convenience,
0=- ine -ax (/ iw! x HP) waged!
+ f {i x E(?’)) x Vigo + (a: E@)2v'an)} ast] (6.3.3)
2
ax HF) = ana -ax / iwi! x EF )ergids!
+f {(’ x H(P’)) x Vin +A! A(PV'n} as] (6.3.4)
2 i EP —
A E™@ = aan) -A- [/ al x HP iwpigidS!
+f {(l x BF) x Vig + Vigil! -Be")} 4s (6.3.5)
a HF , _
0=- mee) - ite (/ a! x E(?)iweogodS!
+f {cw x HF) x V'go + Vigil - “ne} as'| (6.3.6)
pa
where E(7), H(7) represent surface fields when approaching the surface from
region 1. In (6.3.3) (6.3.6), g, and gg are the scalar Green’s function in region
1 (air) and region 2 (lossy diclectric medium), respectively
__ exp (iki 2R) ~
N2= — TR (6.3.7)
and
V'gi2 = (F —7)G12(R) (6.3.8)
where
(1 — thy oR) exp (iki, 2R)
Gi2(R) = —————_———+ 6.3.9)
1,2(R) tak8 (6.3.9)
and R= J/(2@—2')? +(y-y')? + F(a, y) — f(v.y)). The unit normal
vectors ft and 7’ refer respectively to unprimed and primed coordinates and
point away from the second medium. The vector integral equations are put
in the form of 6 coupled scalar integral equations. Let Fy and Fy represent
the 2 and y components of % x H and F), represent the normal component
of H. To be specific, let
--- PAGE 328 ---
306 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
par) = y/r4 (QED) , (LOWY 9 HE 2
e(F) = 4/1+ On + oy a (F)-&
= (Ge - a) A (6.3.10)
»_ |, (aw) , (ew). a.
Fy(7) = 1+( On +a, ax Ar) -§
_ (a, .\ a ;
= (Sfe+ *) A (6.3.11)
_ |, (few? , (flew. a
F, (7) =4/1+ (“en + dy a Ar)
_ (a, Fy saa
=( ant L543) a (6.3.12)
Similarly, for the x, y components of the tangential electric field and the
normal component of the electric field, they are represented by J;, Iy, and
I, as follows:
a) ty (HOD) , (OD) . aro
T,(7) = 1+( Ox + Oy ax Er) -&
_{_%Ff, \ 44
= (She - i) E (6.3.13)
|, , (fw? , (Ale), a.
1(F) = 1+ ( On + Oy ax Er) -y
_ (8. .\ a '
= (Se: + *) ‘B (6.3.14)
-_ |, (Sawn , (Few. po
T,(F) = \f1+ ( an +a, n- Er)
_ (af, af. .\ .,
= (ee - ay! +2) ‘EB (6.3.15)
Then the six scalar coupled integral equations are
0=- 2 + fdaly (1eP G8)
afew, oy, Welw), on 7,
[Py = vy 4 Ae — a) (2-21)
--- PAGE 329 ---
§3.1 Integral Equation and SMCG Method 307
+ Ly(F")G2(R) [-2Ae we -2/)+ De - |
+ I(r) 26(8) [POEM — 2) + —v)]}
+ | ata’ {damgake(e) LEB SD)
+ iki goFy(?’) [eer + il} (6.3.16)
p= 40) +f aetdy {T0712
: [Poy -y)- HED Yy - mn)
+ 14726) [—(e— 21) 4 LEM Gy — yy 4 LED eat]
+ TPIS GAR) [-2Aew) ~2/)-(e- a) }
+ facar{naatse) [2b 2)
+ iFy(F )kimge [-Aewere |} (6.3.17)
rps(7) = 2D + fas'ay'{cxcrytae)| PFE FE oy _ yy
+ Sea) ON Dew) (2-2) -w-v)}
+ 6,(Ryiy(7) [PEED [oe — 2 — EE Gy _ yy]
+ 64( 1) n(F) [AED ce — 2) + FEW ey y) (2-2) }
+ | data {shrma. Fl?) [Men - ee
+ikimgFy?) [42 - one) (6.3.18)
--- PAGE 330 ---
308 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Fi(7) = 20) + [ertty{ Pate [ener]
- Danley (eee + 1) + feta (aR)
[PE Davy + OE e — 2) -(2- 2]
4+ GRE) [-“Ae ee 9+ ae - a)
+Gi(R)F,("’) [Mere -2Z)+(y- v| } (6.3.19)
FMF) = Ff) + | delay {i gta) [= - ae ore)
+f dday {o(nyee) PERM Gy — y) - FED yy]
+ GAUR)FyP) [-« -2)4 HE Dy ~ 9) + AED 2)
+ Gi(R)Fi(F’) [-Aew. -2)-(¢- |} (6.3.20)
0=- Fal) + [tay {tem 2c) [ow ~ |
+ facta {cata ro | ALE HE oy _
+ Ea [21s - 2) ~ 2-2) -w-v)]
+ Go(R)F, (7) [eee —2/)+ CA ONC g —2')
= OE LED iy — yf) +(e = 2!)] + GARE)
: [Ae —a')+ FED Gy -y)-(2- 4] } (6.3.21)
--- PAGE 331 ---
§3.1 Integral Equation and SMCG Method 309
In terms of a matrix notation, the SMCG procedure is as follows. First,
the above 6 scalar surface integral equations are discretized into a matrix
equation by the moment method. Then, we choose the neighborhood distance
rq as the distance which defines the boundary between the weak and strong
element of the impedance matrix Z (for example, ry = 2A). Let
pr=V(@-2'? +(y—y')? (6.3.22)
represent the horizontal separation between two points on the rough surface
(x,y, f(x,y)) and (2', y', f(x’, y’)). The strong matrix is a sparse matrix. For
the weak matrix elements, we expand the Green’s function in a Taylor’s
series about the flat surface, f(x,y) = 0.
. . M m
_ (L— iki 2R) exp(iki2R) (12) 2
Gra(R) = = Yale on) (Ze) (6.828)
m=0
_exp(inR) _ & (1.2) 2i\" a6
92> — TR = SY of) (or) zB (6.3.24)
m=0 R
where zg = f(x,y) —f(2',y’). The above coefficients all?) (pr) and of) (pp)
are translationally invariant in the horizontal directions. In the numerical
results of this section, we keep the expansion terms at 6 (M = 5) in (6.3.23)
and (6.3.24). In the following the first 4 coefficients are listed for reference
12 . exp (ik1,2pR) _
al!) (pp) = (1— ih a0) (6.3.25)
. 2 .
(1.2) exp(iki2pr) J ig | 3iki2 3 s 9 on
a PR) = 459-7 +39 - a 6.3.26
vr) dn pr” Pe he 6828)
. ike 2 .
(42), ) _ exp(ikiger) J ia Ohig — Wikig | 15° 6.3.27
ay’ (pr) = ere cn ay a + ah (6.3.27)
abt?) (pq) — SP. (iki 2pR) _ Kiger _ 10ik? » 4 105Kj 2
3 VR dn 48 B Tipp
35ik12 35 ~
2_ 3) 6.3.28
+ 16p an} ( )
(1.2) exp (iki 2pR)
bi Sy 6.3.29
0 (eR) npn ( )
1)(9p) — exp (iki opp) {ee — 1 (6.3.30)
| ° 80 87pR
--- PAGE 332 ---
310 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
0h) (og) = exp (iki 2pR) Hapa Sika, —3_ (6.3.31)
27 MPR) XP ONL2PR)) “305 Bae BOR "
9 kiape ke opr
pt?) ~e ik: _ MLQPR  ®12PR
by ”'(pr) = exp (iki2PR) ) ~iGo97 + 357
13k 13
= - = 6.3.32
+ 92, 192zpR (6.3.32)
The impedance matrix is decomposed into the sum of a strong and a
weak matrix.
=s ss) Sw) .
Z=Z 42 (6.3.33)
=(s =(w)
where Z ©) represents near field strong interaction and Z {w represents non-
near field weak interaction. Next, the weak matrix elements are expanded in
a Taylor’s series about the horizontal distance between the two points
=v) Mw)
2 =S°Z,, (6.3.34)
m=0
The zeroth term in (6.3.34) is called the flat. surface contribution
SPS) s(w) .
Z =Zy (6.3.35)
The iterative matrix-solving procedure is, for the first-order and higher order
solutions
= =(FS) a:
Z 47°") gO =F (6.3.36)
= s(FS) x
ZZ") gory =p (6.3.37)
c(ntl) M —(w) (n)
BY = b- SZ, (6.3.38)
m=1
Equations (6.3.36) and (6.3.37) are solved using the conjugate gradient
(FS)
method (CGM). The flat surface matrix Z ‘ which represents the lowest
order Taylor expansion term is on the left-hand side of the matrix equation.
Without the flat-surface matrix on the left-hand side, we have observed
that the iteration does not converge for rough surfaces with moderate rms
heights. Thus, the terms strong and weak refer to the magnitude of the
matrix clements, instead of their total contributions to the iterative matrix
equation.
srs
The product of Z y with can be computed using a 2-D FFT algo-
rithm. Updating the right-hand side is also calculated using the FFT. An
--- PAGE 333 ---
§3.1 Integral Equation and SMCG Method 311
additional advantage of the SMCG is that only the Taylor expanded coeffi-
cients need to be stored.

With the number of Taylor series coefficient fixed at M = 5, for a given
rough surface the computational complexity will depend on the number of
CGM iterations (6.3.37), SMCG iterations (6.3.38) and the neighborhood
distance rg. The total number of operations (multiplications) is approxi-
mately

Noom [256r4? nN +2N log(N )mrrr| + Nemo (72N log(N) mrt]

(6.3.39)
where Noam and Ngycc are the number of iterations in CGM matrix solver
and the number of right-hand side updates, respectively, n is the number of
sample points per \?, and myyrr is the total number of FFT’s and inverse
FFT’s. Note that in the above equation, the total number of iterations re-
quired for convergence depends on ry. As an example, consider a simulation
with the following number of iterations Noam = 110 and Ngmcq = 4, with
sampling of n = 64, rg = 2.5A, N = 16384, and mppr = 120. The term
containing the rg dominates with 1.55 x 10" computational steps. Therefore,
SMCG is effective for a moderate rms height so that the number of Taylor
series expansion terms can be manageable and the neighborhood distance ry
can be much smaller than the surface length. In this section, an error norm
of 0.01 is used for all numerical simulations.

Integral Form of Matrix Equations
For completeness, we list the detailed integral form of the six matrix equa-
tions in the following
5 274m pe
7 za) [Of@y
=f eta {700m [4] PED, — yp
mal PR>Ta PR y
age), ay
+ ED wea!) (2-2)
9 ay" 1 af(a.y) Of (2',y')
(n) (ot), (2) 24 _ Wey Yee
+ 10) (7*)a2(oR) [=| [-2A to — a) 4 Ao)
2a\" [Af(x.y)
(n) (pty 1 g(2) (2a) JOM, on a yy!
+17 ySae (2) [ED +—W)
bp ; 2am af (x.y) OF (a’.y!
_ > | as! ay {ths 0 (0R) [=| 0 pt) 2) OF!)
mai! PR>ra PR oy de
--- PAGE 334 ---
312 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
2ym elo! yl
+ tkimb2 (pr) [#4] FOO) [ae i " ee 4 if}
ie Dat h Ped (ac
=-=5> +f. da! dy {i +) (F)G2(R)
Of(a, ny, OF (ay! ' 1
[Pe 1) + LE ea) ea]
m+) (Ny, ofa, nr OF (a, f
$1) G(R) [-“ete —a')+ HE De -a |
+12) @(R) PA. ~2)4+(y -¥)] }
@ Oy
aS satmeay on OF ly) OF(a!, 9!
Of (x,y) Of (z',y!
+ ihm mE) (P) (-Av 5 y) Oat y) = dy i }
+f aatay {12° e909 (0n)
PR>Ta
Bow on Aru’),
Po a + Ae ea) (e-2)]
7 Of(2'.y’
+ HMA pe) (SE a — a) SAE oa)
4. Of (x
+107) (on) AEM — 2) + yw}
+ [eater imo compte 0 Lewd le)
a 241 6 4 4 /
+ thy mb? (pr) ERDF) [Penney + 7 } (6.3.40)
: )(7\a2)(pp) (24)
- de'dy! 5 1) (Fa =
Po 1) ~ Fea vi] + nr era ion [4]
Of(z’, rn , OF (x, ,
Le 2) 4 FE yy) + LEW _ a0)
--- PAGE 335 ---
§3.1 Integral Equation and SMCG Method 313
$1) (PE aie (or) Fal . [-"Aere a Ce *))} \

=- no +f o data {12° G(R)
: eee -y')- HED fy - “|
sapere) [-(e~ 2) + yyy 4 EDs 2)
+ 1st enn | FED. 2 4 (ea)
+ | von aetay’{shymgak Se ) [-1 ~ ore oe)
+i OF) Ermge [-“4eeore | }
+ feta {1200 Com) PEE Gy — y) — LEG — yh]
+1 ea Con) [C2 = 2) + FE yy) 4 AED ea]
+1) ) Sah (pr) [-Aewe —2)+(2— | }
+ AEP kf (pn) [PA OLY (63.41)
+ Ew [PED (e - 2) -e-2)) -w-v)]
--- PAGE 336 ---
314 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
() 24)" pen [AF@M [, ny PFO WD
+ alton) [24] ayer) [AED [2 — 2) — FE yy]
AF (e,y) Of a", , ,
4 OD NE De —2) 4 e-2)]
( 2a] oy (OF) on, OFM ny
+ on)| 2] "racy | LEH ce — a) + LEW y — yy (2 - 2]}
_s ‘ay’ Likym bpp) (24) rye [OLE _ Of. ¥)
x [ te ay { ihm (or) al mG i & e
shen BL) 2d man [Of Gy) _ OF(ehy’) ine (=
+-akim(on) [24] nye) [PA — FINN eee
=P 4 factay' {cy nyse] PF Fa) oy yy
Of (x,y) [é vy!
+ Ee Le — 2) — (2 )-w-¥)]
+ 6H) g(r) LED [(2 — 2) - My _ |
4 ow) Hee -r4+(e- |
+64 da?) [LE Ge — 2) + FED yy) (2-2) }
+ [ delay {item Fae) [Ae D el
1 (Oflu) _ Ofla'.y’)
sons
rath) ay (_Of@. Af (ey),
+ ff aata'{ 8) (ony [OF Fy — yy
Afle.y) [Ow ay
+ Td Oe — 2) - (2-2) - wv)
+ (omy i(7) [22 [(e- 2) - AE Gy _y)
+ ane ¥) ane v) (x —2') + (x— |
+ 0§) (onynte) [PRED cw — 2) 4 FEW Gy yt) (2-2) }
--- PAGE 337 ---
83.1 Integral Equation aud SMCG Method 315
fo. arty {ayn (on) cr) [AGH — 2)
+ iki (on) Fir) [22GB _ FO) (6.3.42)
- > [aot (aon [Pee Pov)
+ BOD (a — 2! =(z- |
+-a6on) [34] rer) [PEE ea— 25 4 MEA a2
+af2(on) [4] ne [AGM -29 +0-vi] |
+f data {Gu REL)
JS prSra
[PAD yy) + HO a — 2!) — (2 - )
+ Gi (RELY) [ere —a')+ Mee - «|
sane [AED - 25 +4}
+f dala omer) [Mew |
--- PAGE 338 ---
316 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
+ | asta (a9) (on EM
PR>Te
af (a. Af (a',y!
. [ LED yy) + B22!) (2-2)
Of (x, 4 wy!
+ af payer ner) | PFE ce — at) 4 EI et]
+a$) (pp) Fe) (P) [eee -2/)+(y- V)| } (6.3.43)
ef Fi ya)
vine (=) dr'dy!§ ib) (p
eer) Lf tea {-i00\on)
[28)” pon fy few) _ afey)
[#] wre [a- ee -e
kiya) 2B ™ (n) (or OF (2',y') OF (x,y)
+2 NPlon) [A] pene ore
y tat) a) ale (1) (at
- LI tea {<i> [#] FG)
, [ey —y) _ “ey — y)| +a) (pp) [| FOV)
oa or oe
[e= 2) 4 Ey — yy FEM ee — 2h]
often) [3] nie”) [-2AEB 2-2) tra]
m dx
FER ff kt emstyycy afew) OFf(e.y)
=> + [oe dy’ {Pou YF) [-1 ~~ ag al
By many cn Olle!) Of (ery)
+ oh nly TDF) oy Ox
ofits (erry (e) [PRED y — yy — 20th yy)
+ GCE [e244 FO — yy 4 FE Ge 01)
+ Gi (RE (F') [- Ae ») (z-2')-(a- x)
--- PAGE 339 ---
§3.1 Integral Equation and SMCG Method 317
+ ma (on) yee ore |
+ acon”) [2 4 Fy — yy 4 MEM e 20)
+ af (pa)FEY [-“Aeee ~2/)-(4- | } (6.3.44)
- y | etd {shan 202 (pr) [z)" IM @) [a2 - oe)
_ y [aaa {o2on) [zy FOG) [Ae rey -y)
+ Sw) PA eat) —(2-2)| 1]
~ ee —y)+(e- *)} + al?) (pp) [4] m EOF)
; [Pe ce = 2) + FED yy) — (2 alt
+ 2a) [20 V) oy) —(2-24] -w-v)]
--- PAGE 340 ---
318 6 3:.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Of(z,y) Of (z',y') OF (ay)
G(R) FO) pF) | PAE (2 — 2) pg SEO IEEN SI gt
+ GA(R)E DR) ETB 2 — 2) 4 SMILED a — a)
Af(o',y!) OF (x,y
_ ral LD yy) +(e-2)]
+ aatayeiern ey [PAE — a) 4 PEt yy —(2-2)]}
“ay! ity 24 omy dined er) [LW _ OFCataw”)
* fo ay { ihm €1 by (pre) Ox Ox!
gle 2 [MAD (php) Of(z,y) — OF(2',y’)
-thim 1, b aoe _ ee
thm Ty (Fog (on) | oy Oy’
rah (2 (net) pry [_ OFC 9) OF@Y) | y
+f arta {o omer eey| 2 Fy — y)
Of (ay) [OF(@,y') a , '
+ EE OEY @-2')~(2-2)]-W-W)
(2) (nt) rae Of (ay) ~_ Of(a',y) OF (ay) _ ot
+ a (dE (7) PEED ce — 2) 4 SAE OFWs 2
Of (a',y') OF (a, 4 5
_ ney ) 1G Diy —y) + (2 2) al) (pp) RO (7)
Of (x,y) ny, OF(%,9) / q 345
[PA eee = a) + MED yy) (2-2! (63.45)
3.2 Numerical Results of Bistatic Scattering Coefficient
The numerical simulation results are presented in terms of the bistatic scat-
tering coefficient as normalized by the incident power. For an incident wave
with a horizontal polarization (TE) we have yan(4s,@s) and P;"¢ is given by
(6.1.62) and (6.1.63) respectively. In medium 1, the co-polarized and cross-
polarized scattered components of €§ for a = v (vertical polarization) and h
(horizontal polarization) expressed in terms of the surface field components,
Fy, Fy, Tz, Ty, are respectively
&{= x | dx’ dy! exp(—ik/’) [+ (x',y') cos 0, cos bs + Iy(x",y’) cos 0 sin ds
an ,
, f yf
—I,(2"', yew) sind, — 1y(e', yA sin 0}
— {Fr (2’,y') sin ds — F(x", y') cos #.)| (6.3.46)
--- PAGE 341 ---
§3.2 Numerical Results of Bistatic Scattering Coefficient 319
and
» _ ik . .
= | dx’ dy! exp(—ik@’) [tte y') sin ds — Ly(2',y’) cos ds}
Of (ay!
+ nf (2',y’) cos @, cos 65 + Fy cos 6, sing. — F(x", y') fe) sin Oy
Of(a',y')
(pl yl Wd).

— F,(2',y') ay sin ds (6.3.47)
where 3! = «' sin 6, cos bs +y’ sin @, sin d.+-f(2’, y’) cos @,. The expressions for
the transmitted waves are similar. The normalization is that the integration
of reflected and transmitted power over solid angles gives unity for a lossless
second medium.

The rough surface has a 2-D Gaussian power spectrum given by

Lglyh? Kee KP
W (Kz, Ky) = aa exp (-8 - — (6.3.48)

We describe various accuracy tests using a 2-D dielectric rough sur-
face. Then, we compute the solution of an electromagnetic wave scattering
problem with up to 98,304 surface unknowns and up to 300 realizations.
We first compare against matrix inversion (MI) for a small problem, In
Figs. 6.3.1 and 6.3.2 the normalized bistatic scattering coefficient obtained
by the MI is compared to the solutions obtained by the SMCG for co- and
cross-polarized components, respectively, using a single surface realization.
Surface lengths in the 2 and y directions are L, = Ly = 4.0\ which gives an
area of L? = 16”. The rms height is h = 0.2A, with a correlation length of
1, = ly = 1.0) and a relative permittivity of (3.0 + 70.2). The surface is sam-
pled at 16 points per A” to give 1536 surface unknowns. The neighborhood
distance rg = 2.0A. The incident angles for all illustrations in this paper are
6; = 10° and ¢; = 0°. It can be observed that both polarized components of
MI and SMCG curves almost completely overlap each other in Fig. 6.3.1.
(A) Accuracy Tests: Choice of rg and Taylor Series Terms
The convergence of the solution is defined with respect to the error norm of
the matrix equation. The error norm criteria is set at < 1% for all simulations
in this section. This is satisfied for all realizations.

Next, the minimum neighborhood distance is shown to be a function
of rough surface statistics. In Figs. 6.3.3 and 6.3.4, a convergence test is
performed with respect to the size of rg. Surface lengths are Lz = Ly = 16d,
which gives an area of L? = 256\?. The rms height is h = 0.2A, correlation
--- PAGE 342 ---
320 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
0.07
z _ _
cna — hh(SMcG)
= ----+ hh (Ml)
S005
3
2 ooa; A
g
= 00s
3
G 002
Boo
oO
0.00 ~~ _____ = =
0-60 40 20 0 2 40 60 80
Scattering Angle (Degrees)
Figure 6.3.1 Comparison between SMCG and full matrix inversion (MI): Co-polarized
result. The simulation parameters are Ly = Ly = 4.0A. bh = 0.2A, ly = ly = LOA, & =
(3.0 + 40.2), and rg = 2.0A. The incident angles are @; = 10° and 4; = 0°.
0.010
5 008
2 0.008
3 0.007 -
2 0.008 | —— vh(SMCG)
= ---- vh (Mt
Eons vi
B 0.004
8
® 0.003
°
% 0.002
8 0.001
0.000 —__ *, — ns
“80 60-40-20 0 20 40 60 80
Scattering Angle (Degrees)
Figure 6.3.2 Comparison between SMCG and full matrix inversion (MI): Cross-polarized
result, The simulation parameters are those of Fig. 6.3.1.
lengths are 1, = 1, = 0.6, and the surface is sampled at 64 points per
d to give 98,304 surface unknowns. The neighborhood distance rg varies
from 2.0 to 5.0 2. It can be seen that for an accurate simulation of the
co-polarized scattering, rq = 2.0\ can be used for this surface. Note that
Ta > 2.0\ appears sufficient for the cross-polarized scattering coefficient.
This demonstrates that the choice of neighborhood distance is a function
of rough surface statistics, and many different rg work for a given surface.
Therefore, the neighborhood distance rg can be chosen to optimize CPU.
--- PAGE 343 ---
§3.2 Numerical Results of Bistatic Scattering Coetlicient 321

<

2

3

= ot

a

8 102

2

£ 109)

£ 4

= tos ----+ r=2.0 wavelength

8 “om 1288 wavajength

Bros} r=3.5 wavelendgt!

° | —— 725:6 wavelength

BH 198

3 0 60-40 20 0 20 40 60 80

a Scattering Angle (Degrees)
Figure 6.3.3 Convergence with respect to the neighborhood distance rg for co-polarized
component. Simulation parameters are Ly = Ly = 16, h = 0.2d, le = ly = 0.6, er =
(6.5 + 41.0), and 6; = 10° and ¢; = 0°.

=

3

8

2

E 104

2 2.0 wavelength

= aa--= =D

8 103! settee 138 wavelength

5 r=3.5 wavelength 4

° —— 125 wavelength oY,

Be ¥

3 ‘30-80-4020 ~C« CSC

a Scattering Angle (Degrees)
Figure 6.3.4 Convergence with respect to the neighborhood distance rq for cross-polarized
component. The simulation parameters are those of Fig. 6.3.3.
(B) CPU Dependence on rq and €2
Next, the matrix solving time dependence on the neighborhood distance (r)
and dielectric constant of the second medium are illustrated. In Fig. 6.3.5,
total CPU time (in hours) is plotted as a function of neighborhood distance.
The CPU times are based on a DEC Alpha workstation. The simulation
parameters are those of Fig. 6.3.3. It can be seen that the CPU time has
an approximately rj? dependence. In Fig. 6.3.6, the CPU dependence with
respect to the relative permittivity is illustrated. For this figure, the simula-
tion parameters are as follows: Surface length in the @ and g directions are
Ly = Ly = 8A (Lz x Ly = 64*) with a surface rms height h = 0.5A and
correlation lengths of l,, = ly = 1.04. The surface is sampled at 64 points per
d? to give 24,576 surface unknowns. The neighborhood distance rg = 3.5.
The incident angle is 6; = 10° and ¢ = 0°. The tapering parameter g is
equal to L,./3. The CPU time increases approximately as ¢}°. Since in this
--- PAGE 344 ---
322 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
70
@
E 50
=
2
rat 40
g
3 30
2
20
10
20°28 30 35 40 45 50
Neighborhood Distance (Wavelength)
Figure 6.3.5 Dependence of CPU time on neighborhood distance rg. The simulation
parameters are those of Fig. 6.3.3.
“|
a 9
g |
<
z
3)
cc
o
F 10
a
3 4 5 6 7
Relative Permittivity
Figure 6.3.6 Dependence of CPU time on ep. Lz = Ly = 8.0A, h = 0.5A, ly = ly =
LOA, rg =3.5A, 8; = 10° and @; = 0°.
example the second medium relative permittivity varies, it is important to
check power conservation (Fig. 6.3.7) with respect to permittivity. A general
decrease in power conservation from 99.8 to 98.9 is seen as relative permit-
tivity increases from ¢€, = 3 to €, = 7. One reason for the increase of CPU
with ¢, is that as €, increases, the sampling density of 64 points per square
wavelength is not enough, and it takes more iterations to converge. Thus for
large permittivity, we need to sample more points per square wavelength on
the surface.
--- PAGE 345 ---
§3.2 Numerical Results of Bistatic Scattering Coefficient 323
1.000
0.998
0.996
0.994
o
S 0.992
&
2 990
s
S 098s
e
0.986
0.984
0.982
0.980
3 4 5 é 7
Relative Permittivity
Figure 6.3.7 Dependence of power conservation error on €. The simulation parameters
are those of Fig. 6.3.6.
Pao 50
S009 nN seseeee 150
= 008 -—7 200
8 007 —— 300
2 008 -
Boos Pe
§ y
GB 008 p \
3 I
@
ge 00
0.00 - — es
so 60 40 20 0 2 4 60 80
Scattering Angle (Degrees)
Figure 6.3.8 Bistatic co-polarized scattering coefficients for h = 0.2A, Ly = ly = 0.6, Le =
Ly = 16d, ¢ = (6.5-+41.0), rg =3.0d, 6; = 10° and 4; = 0°. Result illustrates convergence
with respect to the number of realizations.
(C) Monte Carlo Simulation Results
In Fig. 6.3.8, the average normalized bistatic scattering coefficients are plot-
ted for up to 300 realizations. Surface length in the x and y directions are
Ly = ly = 16d (Ly x Ly = 256\”) with a surface rms height h = 0.2
and correlation lengths of l, = l, = 0.6\. The surface is sampled at 64
points per A? to give 98,304 surface unknowns. The neighborhood distance
rq = 3.0X. The incident angle is 6; = 10° and ¢; = 0°. The tapering pa-
rameter g is equal to L,/3. Note that the sharp forward specular peak at
--- PAGE 346 ---
324 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
0.008

= 50

s a 150

2 0.004 Ni --- 200

3 > ¢ De — 900

> 0.008 j

2

3 a XX

% 0.002 , ..

S .

ra) Se

2 Xe

0.001 %

a fe

an

0.000 —  —_ - _—
80-60 «40-200 2s
Scattering Angle (Degrees)

Figure 6.3.9 Bistatic cross-polarized scattering coefficients with simulation parameters of
Fig. 6.3.8. Result illustrates convergence with respect to the number of realizations.
+10° is present in the co-polarized scattering component due to the coherent
wave. In Fig. 6.3.9, the cross-polarized components of Fig. 6.3.8 are plotted
for up to 300 realizations. Unlike the co-polarized component, a peak in the
backscattering direction can be secn. As in the perfect electric conductor
case, the second-order backscattering enhancement is more clearly exhibited
for the cross-polarized case.

The calculations needed for the Monte Carlo simulations were carried
out on a supercomputer located in Hawaii. The CPU time required on the
Maui supercomputer depended on the number of nodes. The supercomputer
is a parallel computer with 400 nodes. Compared to a serial processing, each
realization requires much less clock time when using parallel processing.
Thus, the required CPU time depends on the availability of nodes. However,
it is informative to note that on the average approximately 25 CPU hours are
required for one realization on DEC Alpha workstation. The average number
of iterations required for Fig. 6.3.8 are Negiz = 105 and Nsucc = 4. With
N = 16384 and mppr = 120, Eq. (6.3.39) gives approximately 2.5 x 101!
computational steps.

A Monte Carlo simulation of the backscattering enhancement is illus-
trated for both co- and cross-polarization in Fig. 6.3.10 for the case of
larger rms height. Surface lengths in the x and y directions are Ly = Ly =
8\ (Ly x Ly = 644”) with a surface rms height h = 0.5, and correlation
lengths of l, = ly = 1.0A. The surface is sampled at 64 points per A? to
give 24,576 surface unknowns. The neighborhood distance rg = 3.5. The
incident angle is @; = 10° and @; = 0°. The tapering parameter g is equal to
L,,/2. The surface parameters of h = 0.54 and / = 1.0A are moderately rough
--- PAGE 347 ---
§3.2 Numerical Results of Bistatic Scattering Coefficient 325
€
S 005
2
= onl
8
is}
D 0.08
£
5 oe
8
D oot
2
B 0.00 a _.
co “30 80-40-20
mo Scattering Angle (Degrees)
Figure 6.3.10 Bistatic scattering coefficients for co-polarization and cross polarization for
h=0.5A, le =ly = LOA, Lz = Ly = 16A, & = (6.54 41.0), rg = 3.5A, 0; = 10°, and o; =
0°.
Boon
@ o10 a —— 2-0 (200)
tos oN = FB {883}
a MN en
© oo7 yo nem
2 006 / ~~
S008 “ \
= 004 / S
5 003” \,
OD 002 ~N
g 001 E >
% ool —— a >
i 80 60 40 20 0 20 40 60 80
a Scattering Angle (Degrees)
Figure 6.3.11 Backscattcring enhancement of two cases: 1-D and 2-D electromagnetic wave
incidence on dielectric surface (€, = 6.5-+11.0). Comparison of normalized bistatic scattering
coefficients for h = 0.54, 1= 1.0A, @; = 10°, and @; = 0°.
with an incident angle of 10°. The peaks near —10° are clearly visible. In
the simulation, the co-polarized component requires many realizations for the
backscattering peak to converge. This is because in co-polarization, the first-
order scattering obscures the second-order scattering contribution, which.
is mostly responsible for the backscattering enhancement peak. The cross-
polarized component of the backscattering enhancement peak converges af-
ter 50 realization averages. This clearly demonstrates the dominance of the
second-order scattering contribution to the cross-polarized result. The aver-
age number of iterations for this example are Ncga = 220 and Nsuccg = 6.
With N = 4096 and mprr = 120, Eq. (6.3.39) gives approximately 1.8 x 10!
computational steps.
In Fig. 6.3.11, the normalized bistatic scattering coefficient in the plane
of incidence for the 1-D random rough surface and the 2-D dielectric sur-
face with electromagnetic incident wave are compared. The incidence angle
--- PAGE 348 ---
326 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
is 6; = 10° and ¢; = 0°. In the 1-D surface simulations, the tapering pa-
rameter is g = L/4, surface length is 30A, and an ensemble average of 500
realizations are used. For the 2-D dielectric rough surface simulation, the
co-polarized result of Fig. 6.3.10 is used. Two curves follow a similar trend
for all scattering angles. The backscattering enhancement at near —10° is
observed in both co-polarization and cross-polarization,

4 Scattering by Lossy Dielectric Surfaces with PBTG

Method
4.1 Introduction
In this section, we study the scattering of electromagnetic waves by lossy di-
electric surfaces with large permittivity. This has broad applications in nat-
ural media. For wet soil, the relative permittivity can be as high as 17+72.0
at 1.4 GHz. For ocean surfaces, the permittivity can be as high as 39.7+740.2
at 14GHz. For lossy dielectric rough surfaces with high permittivity, there
can be rapid spatial variations of the dielectric medium Green’s function and
surface fields. Also the wave can propagate from a point on the rough surface
to another point on the rough surface through the lossy medium. Based on
physical reasons, the surface fields can have large spatial variations within
short distances. These large spatial variations can also be attributed to fine
scale geometric irregularities on the surface or due to large permittivity of
the lower medium. From the point of view of spatial frequency, the high
spatial frequency components can interact with the low spatial frequency
components. Thus a dense grid is needed to discretize the surface fields.

In Chapter 5, we have developed the physics-based two-grid (PBTG)
method. In PBTG, two grids are used: a dense grid and a sparse grid. The
sparse grid is that of the usual 8 to 10 points per wavelength. The dense
grid ranges from 16 or higher number of points per wavelength depending
on the relative permittivity of the lossy dielectric medium. The surface fields
are calculated on the dense grid. In the formulation of the surface integral
equations, two Green’s functions are used. The free space Green’s function
and the Green’s function of the lossy dielectric medium. Although the sur-
face fields have large spatial variations, what need to be calculated are the
convolution of the surface fields with the two Green’s functions. The PBTG
is based on two observations: (1) the Green’s function of the lossy dielectric
is attenuative (spatial limited), and (2) the Green’s function of free-space
is slowly varying on the dense grid (spatial frequency limited). The first
observation results in a sparse matrix for the Green’s function of the lossy
--- PAGE 349 ---
84.1 Introduction 327
dielectric. When this Green’s function convolves with the surface fields on
the dense grid, it will be just the product of a sparse matrix and a column
vector. The second observation allows us, when using the free-space Grecn’s
function to convolve with the surface fields of dense grid, to first average the
values of surface unknowns on the dense grid and then place them on the
coarse grid.

In Chapter 5, the PBTG method was implemented for 1-D surface (2-D
scattering problem). In this section, we (i) extend the PBTG to.2-D rough
surface (3-D scattering problem), (ii) combine the PBTG method with the
sparse matrix canonical grid method (SMCG) for improving CPU and mem-
ory requirements, and (iii) study bistatic scattering coefficients and emissiv-
ity for wave scattering from 2-D dielectric rough surface with high permit-
tivity. The wave interaction in the rough surface is divided into: (1) very
near field, (2) near field, and (3) non-near field. (1) Very near field is of dis-
tance of separation less than half a wavelength. (2) Near field separation is
between half a wavelength and rg wavelengths. (3) Non-near field is beyond
rq wavelengths. For very near field interactions, we use the usual product
of sparse matrix and column vector. For near-field and non-near field inter-
actions, the free space Green’s function is slowly varying on the dense grid.
We first average the fields on the dense grid to get fields on the coarse grid.
For the non-near field interactions, we further expand free space Green’s
function on a canonical grid of a horizontal surface so that the fast Fourier
Transform (FFT) can be applied. In the lower medium, the non-near field
interactions are neglected because of lossy properties of the lower medium.
The approach is denoted as PBTG/SMCG. The computational complexity
and the memory requirements for the algorithm are O(Nyey log(.Nscy)) and
O(Necg), respectively, where Nycg is the number of grid points on the coarse
grid. The second-order small perturbation method (SPM) will be studied in
Volume II. Also, SPM agrees with the small slope approximation in emis-
sivity calculation for half-space case [Irisov, 1997]. Monte Carlo simulations
of emissivities are compared with those of the second-order SPM.

In Section 4.2, the formulation of the problem of wave impinging upon
a 2-D dielectric surface (3-D scattering problem) is described, and the sur-
face integral equations are converted into a matrix equation using a single
grid discretization. In Section 4.3, we describe the physics-based two-grid
algorithm and combine it with the sparse matrix canonical grid method.
The mathematical expressions of the bistatic scattering coefficients and the
emissivity are given. In Sections 4.4 and 4.5, numerical results are illustrated.
--- PAGE 350 ---
328 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
4.2 Formulation and Single Grid Implementation
Consider an electromagnetic wave, E;(F) and H;(7), impinging upon a 2-D
dielectric rough surface with a random height profile z = f(x,y). It is tapered
so that the illuminated rough surface can be confined to the surface area
Lyx Ly. The direction of incident wave is kj = sin 6; cos ¢;% +sin 6; sin d; —
cos 6,2.
The incident fields for TE wave incidence are given as
+00 +00
E,(r) = | adh / dk, expliket + thyy — ik.2)E (ke, ky)@(—ke)
o —00
(6.4.1)
_— 1 +00 +00 a
Har) =—4+ | dk | dy exp(iky + ikyy — tks2)E (Kes ky) —ke)
™ J—o0 00
(6.4.2)
where
1
&(—kz) =F (@ky — Gke) (6.4.3)
‘p
i, Rs on a Kp 3 4
i(-kz) = i (ke + Gky) + 2 (6.4.4)
and for TM wave incidence
_ +00 +00 .
E,(F) = | ak, [ dky exp(ikea + ikyy — ikz2)F (ke, ky)h(—kz)
—00 20
(6.4.5)
_ 1 pte +00
Hi(7) =— / ak, | dk, exp(ikzx + ikyy — ikzz)F (kz, ky)é(—kz)
™M J—oo 00
(6.4.6)
The spectrum of the incident wave, E(kz, ky), is given as
1 ose 00
Elke, ky) = al de | dy exp(—ikza — ikyy)
An? Joc Joe
- exp [i (Kina + kiyy) (1 + w)] exp(—t) (6.4.7)
where t = t, + ty = (x? +y")/9? and
(cos 6; cos 2 + cos 6; sin diy)? .
t, = 64.8
te Pore, (6.4.8)
ty = (-sin ee cos diy)? (6.4.9)
--- PAGE 351 ---
§4.3 Physics-Based ‘T'wo-Grid Method 329
1 (2%tp-1 . %ty-1
at (2a) ty t 6.4.10
° ki (a cos? 6; + a ( )
The six component surface integral equations are given by (6.3.3)-(6.3.6).
As in Section 3.1, we also take the « and y components of the tangential
field equations and the normal component of the field equation. The method
of moments (MoM) is used to discretize the integral equation. The resulting
matrix equations are
N
So [ZB + ZAI + 10 + Ze + 210 + 2,1] = 100°
n=1
(6.4.11)
for p = 1, 2,3 which correspond the surface integral equation when approach-
ing the surface from free space and for p = 4,5,6 when approaching the sur-
face from the lower medium. The quantities of {pine are zero for p = 4,5, 6.
Also
I) = F,(F) = Sey(Fn) [& x H(Fn)] -# (6.4.12)
TD) = Fy) = Sey(Fa) [x HG n)] G9 (6.4.13)
1?) = In(?) = Szy(Fn)ft- En) (6.4.14)
I) = In(F) = Sey (Fn) [A x EFn)] # (6.4.15)
IP) = 1,(7) = Sey(Fn) [a x BG ,)] 9 (6.4.16)
TD) = Fu) = Soya) Hn) (6.4.17)
ae. yd ato yq2) WV?
are surface unknowns and Syy = {i + [2a] + [242] } . The Zi,
are the impedance matrix elements and are determined by the free space
Green’s function and the dielectric medium Green’s function. The parameter
N is the number of points we use to discretize the rough surface.
4.3. Physics-Based Two-Grid Method
In this section, we describe the physics-based two-grid method. We assume
that the upper medium is the free space and the lower medium is lossy with
large permittivity.

2 = (1 +itand) (6.4.18)
where tan 6 stands for loss tangent. Let A, and Ag represent the wavelength
of the wave in the free space and the lower medium, respectively, and

ng = integer (ve) (6.4.19)
--- PAGE 352 ---
330 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Then, the relationship between A, and \2 can be expressed approximately
by

X

yee (6.4.20)

ng
The number of sampling points needed in the lower medium should be ng
times that of the free space.

In the physics-based two-grid method, we use two grids with samplings
per wavelength of nseg (coarse grid) and nedg (dense grid), respectively. Let
Neay and Nyeg be respectively the total number of points on the dense grid
and the coarse grid.

7. Ly Ly
Nodg = (nao) (nasa (6.4.21)
. Ls L .
Necg = (52) (m5) (6.4.22)
For example nseg = 8 and Nsdg = 8n2. We first re-write equation (20) using
the dense grid.
Neag
Do [ze + Ze 1) + 2819 + ZeL IY + ZFS 19) + Zp8, HO] —1Ipyine
nat
(6.4.23)
The Roman numeral subscripts m, n denote indexing with the dense grid.
In Fig. 6.4.1, we plot the real part of the products of distance and the two
Green’s functions. We make the following three observations:
(1) The Green’s function in the lower region is heavily attenuative. Let ky
be the imaginary part of ka. If k{r > C, where C is a constant, then the field
interaction between the mth and the nth point is vanishingly small. We can
define a distance limit as dictated by dissipative loss:
Cc
n= (6.4.24)
i
outside of which the lower medium Green’s function can be set equal to zero.
Based on comparisons with the results from SMCG, C is fixed at 1.5.
Based on this observation, we calculate the left-hand sides of (6.4.23)
for as follows by approximating
3 Zin Tan S71 .
po ~ gpq — J mn Tnn STI 5
Din © Zinn {3 ree >t (6.4.25)
where Tmn is the distance between the mth point and the nth point on the
dense grid. Thus Z5%, (p = 4,5,6) are sparse matrices and Eq. (6.4.23) for
--- PAGE 353 ---
§4.3 Physics-Based Two-Grid Method 331
1 a rs a ee
oak ots “ 4 " tt mo Y
cf
oat hr ee SE RY Peas
Hi ryt ' vor ra tt
Roaklhi ce pa eh py
SB WiliMar ss ee te al
FN 1 i111] Ae eae I
& q(iee: ee pe
on fyb a pa ba te
. i Phar tr ye hag hy te
Ot
Pep yet hr ot rs reg boty
a
Ce rT
yoo et \ Ho tnt)
1 a a
0 2 4 6 8 10
distance in free space wavelength
Figure 6.4.1 ‘The variation of rG of free space (dash line) and lossy medium (solid line)
with relative permittivity of 17 + 72.0 as a function of distance.
p = 4,5,6 becomes
Neag
Fpl zi Fp2 7(2 Gps 7(3 pa (4 Zpd 7(5 > 6)) _ ¢
De [Zeit + Bee Le + ZrO) + Zee th + Zee A + Zee, 10] =1pne
n=l
(6.4.26)
(2) For non-near field interaction, Green’s function for the upper medium is
slowly varying on the dense grid. Thus when performing matrix and column
vector multiplication on the dense grid as indicated in (6.4.23), the Green’s
function of the upper medium is essentially constant over an area of ny x ng
points on the dense grid. Thus we can write
n3 n3 1a
Pq (a) gpa (q) _ 277 — (q)
> Zins ynet) intl © Zinnptiny SOD = BLP ne a Ve,
=) 1=1 2121
(6.4.27)
where l/ = 1,2,.. 273 and the points with indexes mmp and mp are the
central point of the n3 dense grid points of m +1, m+2,..., m+n} and
n+1, n+2, ..., n+n3, respectively. What is performed in (6.4.27) is that
the surface fields on the dense grid are first averaged before multiplied by
the upper medium Green’s function.
(3) The slowly varying nature of Green’s function of the upper medium
--- PAGE 354 ---
332 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
only applies to non-near field interaction. For near field interaction, Green’s
functions G; and G2 have similar rate of variations. Thus we separate out a
distance, say 1A, outside of which G2 is much more rapidly varying spatially
than G,.
Based on the observations above, we decompose the upper medium
Green’s function into near field and non-near field interactions
Nodg Neag Neag
Ye zea = Y= 20810 + Ss zee (0.28
n=l n=l n=1
where Z21°) and ZX) are determined by
PY
pas) — J Zin Tmn Sp 45
Za {5 met (6.4.29)
pains) _ {0 Tmn STy ’
Br = { Be vmm 2 Py (6.4.30)
Thus r; is the distance outside which the Green’s function of the lower
medium is fast varying compared with that of free space Green’s function.
Let m and 7 denote the coarse grid indices. The coarse grid has surface
unknowns J; Ha) which are averages of the dense grid surface unknowns. Thus
if 7; is centered in the group of the n3 dense grid points of n +1, n+
2, ..., n+n?, we have
(4) (@) (a)
~ Ta tite to tle
+1 #2 n
7@ = 2h oe oe (6.4.31)
ni
The Green’s function of the upper medium on the coarse grid is represented
by 2%... Then Eq. (6.4.23) for p = 1,2,3 becomes
6 Neag 6 [Neco loss)
DD MOL + SEE OP | = pire (6.4.82)
q=l n=l q=l | A=1 intp
Note in Eq. (6.4.32) that whee ZEgs) 1 includes Nggy values of m =
1,2,..., Nedg on the dense grid, while view ZEA) T@ only has values of
m = 1,2,...,Nscy on the coarse grid. Thus we first compute shes Zpalns)
7. Then we use linear interpolation of Nee ZEA) 7 on the coarse grid
to find Nyag values on the dense grid. In Eq. (6.4.32), we use subscript ntp to
represent that interpolation. Thus the computational steps for matrix-vector
multiplication are associated with the number of surface unknowns on the
coarse grid. The algorithm is described pictorially in Fig. 6.4.2. The PBTG
--- PAGE 355 ---
§4.3 Physics-Based Two-Grid Method 333
Nag
¥ Gili AD egy. MAL 2 Ny
fa
Coarse se Gri
aa | | Dense Grid_|
Interpolate from | | average from dense grid 10
| coarse grid 10 coarse grid before
| dense grid after convolution
| convolution
L
Figure 6.4.2 Illustration of convolution of upper medium Green's function with surface
fields on dense grid.
is also used in conjunction with the SMCG. The computational complexity
of the combined algorithm of PBTG/SMCG is O( Neg log(Nseg))-

The numerical simulation results are presented in terms of the bistatic
scattering coefficients normalized by the incident power. For an incident wave
with a polarization 8, we have

Esl? :
Yas (9s. 0s; 9i, Pi) = Bn, PRE (6.4.33)
The incident power is
vine _ 277 2 ky
pyre t dkadky |E(ke by) (6.4.34)
ND Shyck
where kp = \/k2 + k2.

The horizontal and vertical polarized scattered components of Eg are,
respectively, given by (6.3.46) and (6.3.47). The emissivity of the rough sur-
face at incident angle (6;, ¢:) is

1 .
eats, 6) =1— ae ff Canal Oar si 800) + roe dui Bg) si dB
T
(6.4.35)
--- PAGE 356 ---
334 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
4.4 Numerical Results and Comparison with Second Order Per-
turbation Method

In this section, we illustrate the numerical simulation results of wave scat-
tering from 2-D lossy dielectric rough surface. Simulations are based on
Gaussian random rough surfaces with Gaussian correlation functions. All
the cases are computed with the relative dielectric constants of 17 + i2 and
4.06 + 70.3, surface area of 8 free space wavelengths by 8 free space wave-
lengths, rms height fromm 0.05 to 0.3 wavelengths, and correlation length of
1.0 wavelength.

The results of three methods will be shown: (i) single coarse grid of 8
points per free space wavelength with SMCG (SCG/SMCG), (ii) single dense
gird of 16 points per free space wavelength with SMCG (SDG/SMCG), and
(iii) PBTG/SMCG. Based on the experience of 1-D dielectric rough surfaces,
the sampling density of 16 points per wavelength for the permittivity of
17 ~ i2.0 gives convergent results. Thus we regard (ii) as accurate results.
We will show that (iii) is as accurate as (ii) and takes much less CPU time.
First, we compare the bistatic scattering coefficients for one realization based
on different methods. Next, the emissivities and CPU are compared. The
results show that the dense grid is required for the case with large dielectric
constant. Then the variation of brightness temperatures with observation
angles is illustrated and compared with the second order small perturbation
method, Finally, the brightness temperature as a function of rms height is
shown for different observation angles. We use T = 300K as the physical
temperature. All the numerical results were computed on a DEC Alpha
workstation.

(A) Comparisons of Bistatic Scattering Coefficients Computed by Vari-
ous Methods

In Figs. 6.4.3a and 6.4.3b, the comparisons of bistatic scattering coefficients
in the plane of incidence ¢; = 0°, ¢; = 0° and 180° of a single real-
ization of rough surface obtained by the SCG/SMCG, SDG/SMCG, and
PBTG/SMCG are shown. Figure 6.4.3a is for co-polarization and 6.4.3b for
cross-polarization. The incidence wave is TE wave with the incidence angle of
10 degrees, and the rms height is 0.3 free space wavelength. The relative per-
inittivity of lower medium is 17 +22. There are some small differences among
three results. That means it is not strictly necessary to use dense grid for
the calculation of the bistatic scattering coeflicients for this case of TI. inci-
dence. But the PBTG/SMCG can give better results than the SCG/SMCG.
In Figs. 6.4.4a and 6.4.4b, the results are shown for TM wave incidence. It
--- PAGE 357 ---
§4.4 Numerical Results and Comparison 335

0.35; - + -

—  spa/smea |
8 03 --  SCG/SMCG as
3 -- PBTG/SMCG Po
gp)
Zoost it
a it
: boa
3 02 | h ify
| as
3 (\ ! lef ( {
2 { i wil
Fors fof
4 ia | “ |
Eos Pit | |
il Ayo |
g . !
Hoos. yoo \ | yo
. y \ ot \ vat
a Nf \/
pet YN NN
o © 2% o| 2 «0 «0 €
‘scattering angle (degree)
(a)

a ae
gt ‘ = SDG/SMCG
gore n ~~ SCG/SMCG
g vi j---  PBTG/SMCG
H yh |
5 oc {4
B yy
H I
Foo 1} |
5 |
5 1
Foe } ot
: |
Zoopi. 19
Zo02 | \

: j
i | At)
YX G LN a |
2 iV VA oa
) VK PS,
l= a oo
#0 40 20 ee re er)
scattering ange (degr08)
(b)
Figure 6.4.3 Comparison of the bistatic scattering coefficients between the SDG/SMCG,
SCG/SMCG, and PBTG/SMCG for the TE wave incidence. ‘The case is with rms height of
0.3 wavelengths, correlation lengths of 1 wavelength, surface lengths of 8 by 8 wavelengths,
and relative permittivity of 17 + 2é at incidence angle of 10 degrees. a) co-polarization b)
cross-polarization.
--- PAGE 358 ---
336 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Incidence | CPU time Difference of | Difference of
| spasmca | te | 45.05 | ose | |
BA
TM
* The difference of emissivity means the emissivity minus the emissivity of
corresponding SDG/MCG,
Table 6.4.1 Comparison of emissivities and CPU based on different methods.
is seen that the coarse grid leads to a larger error for TM wave than for
TE wave. Comparing the results of Figs. 6.4.3 and 6.4.4 indicates that the
PBTG/SMCG can give better results than the SCG/SMCG particularly for
cross-polarization component.
(B) Comparisons of Emissivities and CPU Requirements from Various
Methods
In Table 6.4.1, the emissivities obtained by various methods are shown for
one realization. The input parameters of rough surface are the same as before.
The difference of emissivities between the SDG/SMCG and the SCG/SMCG
for TE wave incidence is 0.0447. It will lead to a difference of 13.41K in
brightness temperature and is unacceptable in passive remote sensing appli-
cations. The emissivities obtained by the PBTG/SMCG are also shown. The
difference between the SDG/SMCG and the PBTG/SMCG is only 0.003316.
That will give a small difference of 0.99K in brightness temperature. The
emissivities for TM wave incidence are also shown in Table 6.4.1. It is seen
that the PBTG/SMCG can give almost the same results as the SDG/SMCG
while the SCG/SMCG cannot. The CPU requirements for various methods
are also shown in Table 6.4.1. It is clear that the SDG/SMCG requires the
most CPU. On the other hand the PBTG/SMCG is five times faster than the
SDG/SMCG and takes even less CPU than the SCG/SMCG. The fact that
the PBTG/SMCG requires less CPU than SCG/SMCG is because the former
requires less number of conjugate gradient iterations. Thus PBTG/SMCG
can obtain the accurate results and require much Jess CPU than that of the
single dense grid.
--- PAGE 359 ---
§4.4 Numerical Results and Comparison 337
co ve
.|——  spq@smec | ae
g°3"| -_.  scqy/smcG Av \ 1
3 ---  PBTG/SMCG| Mt
2 } ‘y! i
= 03 :
g j \\
E as \
S '
i \
502 .
£ | \
a \ |
gous A Woy
4 iA val |
Boon _f \ 4 \
i rs
ya \/ NY \
ole Wa
rn rr) rr
‘scattering angle (degrees)
@
0.085 ye
5 — sp@/smca
g 004 A ---+  SCG/SMCG
3 \ =~ PBTGISMCG,
: aie
= vos 7
A f\s
i | | {\
E 0s , Wesks ;
z an i |
Joves | VAN ; i "
3 i rn |
#002 nr rr en
i PooL gp boy
Boots i H ny H \ of
ial POUL Ein
ee" a} VU BPG
Jas (\p TW YN
2 - ~f \ \ a \ I
“ 80 60 40 20 0 20 40 60 80
acting angi (derecs}
(b)
Figure 6.4.4 Same as Fig. 6.4.3 except for TM wave incidence.
ig is
--- PAGE 360 ---
338 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
200-- a
200- |
== meee © |
£0; — .
H aon
E ao oS
g a a
2 eo 6 -
pe a
@ |----2-2_-- 6
¥ 100 ==
z = Flat Surface(17+2i) \
B joo} ——__ SPM(17421) — i
© PBTG/SMCG(17+2i) ~
- Flat Surface(4.+0.3i) se
“ SPM(4.+0.3i) ~.
= PBTG/SMCG(4.040.3)) \
i
‘Observation angle (dagree)
fa)
Oe 5
280] aca 7 a
370) : oo 1
g |
'§ 240 a4
z we?
I ge
ma so 8 eee
Bole
§ 180, -—
5 Flat Surface(17+2i)
2 reo] | SPM(IZ42i)
60 ° PBTG/SMCG(17+2i)
7 > Flat Surface(4+0.3i) |
140) ‘SPM(4+0.3!)
PBTG/SMCG(4+0.3i) |
Sia ee ee ee ee
Observation angio (dogree)
©)
Figure 6.4.5 The brightness temperature of Monte Carlo simulation averaged over 5 real-
izations as a function of observation angles and comparisons with that from the second order
small perturbation method and flat surface. The case is with rms height of 0.3 wavelengths,
correlation lengths of 1.0 wavelength, relative permittivities of 17 + i2.0 and 4.06 + 10.3, and
physical temperature of 300K. (a) TE wave (b) TM wave.
--- PAGE 361 ---
§4.4 Numerical Results and Comparison 339
(C) Variation of Brightness Temperature with Observation Angles and
Comparison with Results from the Second Order Small Perturbation
Method

The brightness temperature results based on averaging over 5 realizations
are shown in Figs. 6.4.5a and 6.4.5b for horizontal and vertical polarization,
respectively. The rough surface is with rms height of 0.3 wavelengths and
correlation length of 1.0 wavelength. The observation angles are varied from
10 degrees to 50 degrees. The relative permittivities is 17.0 + 72.0. We note
that in the simulation of emissivity in passive remote sensing, only a small
number of realizations are required. This is because in passive remote sensing
an integration of scattered angles is used and that has built in smoothing.
For the case of permittivity of 17 +i2 at the observation angle of 10 degrees,
the horizontal emissivity averaged over 10 realizations is 0.699 and is 0.701
for averaging over 5 realizations. The difference between them is 0.002. That.
means that averaging over 5 realizations can give accurate results. Figure
6.4.5a is for TE wave and 6.4.5b for TM wave. The brightness tempera-
ture shown in solid line is from the second order small perturbation method
(SPM), in dash-dot line is from flat surface, and in circle is from numerical
simulation results. It is shown that surface roughness increases the bright-
ness temperature over flat surface for horizontal polarization. It can increase
or decrease the brightness temperature for vertical polarization depending
on observation angles. It is well-known that the SPM cannot give the cor-
rect results of emissivities for moderate to large rms slope. For TE wave,
the numerical results show that the brightness temperature decreases with
observation angles. On the other hand the SPM results show that: brightness
temperature increases with observation angles. The brightness temperature
for the permittivity of 4.06 + i0.3 is also plotted in the figures. Similar fea-
tures are exhibited in this case. It can be seen that surface roughness has
a larger influence in brightness temperature for large permittivity than for
the small permittivity. For horizontal polarization, more energy is reflected
with the increase of incident angles. Thus the brightness temperature de-
creases with the observation angles. For vertical polarization, more energy is
transmitted into lower medium with the increase of incident angles if angle
is less than the Brewster angle. Thus the brightness temperature increases
with the observation angles.
--- PAGE 362 ---
340 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
20). sp a
© NU:10 degrees
+ SPM:10 degrees|
Exp 8 NU:30 degrees
£ x SPM:30 degrees|
5 ° NU:50 degrees
gf ‘SPM:50 degrees| |
200} 4
poi ; & 4
i e 2 $ . 8
2 tao . ®
i 2 . °
2 °
3 +
reo 3
wo oo
° 005 Oa on 02 028 as
rms height (wavelength)
fa)
240 we - -
° 9
4
g200) ~ 9
4 ° NU:10 degrees + °
4 * SPM:10 degrees| + ?
3 a NU:30 degrees i
$220}, x SPM:30 degrees:
8 ° NU:50 degrees
Fl + ‘SPM:50 degrees|
£210 ‘
2 x a
3 g 8
fal 2
BI °
&
é 1 @ 3 8 ’ . |
s80l— _ - _ _
0 008 on 045 02 03 2a
‘ms height (wavelength)
)
Figure 6.4.6 The brightness temperature of Monte Carlo simulation averaged over 5 real-
izations as a function of rms heights and comparisons with that from the second order small
perturbation method. The rms height of zero means flat surface. The case is with correlation
lengths of 1.0 wavelength, relative permittivity of 17-+ 2i, and physical temperature of 300K
at observation angles of 10, 30, and 50 degrees. a) TE wave b) TM wave.
--- PAGE 363 ---
§4.4 Numerical Results and Comparison 341
(D) Variation of Brightness Temperatures with rms Height and Com-
parison with that from the Second Order Small Perturbation Method
The brightness temperatures as functions of rms height are plotted in
Fig. 6.4.6a for horizontal polarization and in Fig. 6.4.6b for vertical po-
larization for the observation angles of 10, 30, and 50 degrees, respectively.
The correlation length is 1 wavelength and the permittivity is 17 + 2i. We
also show the results from the second order SPM. The numerical results
are averaged over 5 realizations. For the small rms height, the results of
simulations and SPM are in good agreement. It also illustrates that the nu-
merical algorithm can give the correct emissivity calculations. For the case
of flat surface, one needs to use many angles in integrating near the specular
direction to give correct emissivity. With the increase of rms height, the dif-
ferences between them get large, especially for the observation angles of 10
aud 50 degrees. Because the numerical results and SPM results cross each
other around the observation angle of 30 degrees as shown in Fig. 6.4.5, the
differences between them is small. For the rms height of 0.3 wavelength, the
difference between SPM and numerical simulation in horizontal polarization
can be as large as 30K in the brightness temperatures at the observation
angle of 50 degrees. Another feature shown in the figures is that the surface
roughness increases the brightness temperature for all the cases except for
the vertical polarization at observation angle of 50 degrees. The reason is
that the observation angle of 50 degrees is close to the Brewster angle. At
the Brewster angle, the emissivity of flat surface is the maximum for vertical
polarization. Thus surface roughness will lead to a decrease in the emissivity
near the Brewster angle for vertical polarization.

(E) Comparisons with Empirical Formula

In passive remote sensing with soil, an empirical formula, which has been
used for many years, is as follows [Wang et al. 1983; Njoku and Li, 1999;
Jackson, 2001]

Taul(Or, ei) = {1 —[rva(is pi)(L— Q) + rno(Oi, piQLE HLT (6.4.36)
Ton(0:,¢2) = {1 [raol8i,~)(1— Q) + roi edQ]EN VT (6.4.87)
where 7’, and Tz, are brightness temperatures for vertical and horizontal
polarizations, respectively, 7’ is physical temperature of dielectric medium,
and Q and H are empirical constants that are used to fit the data. The
parameters 7,9 and rpg are the flat surface Fresnel reflectivity of vertical
--- PAGE 364 ---
342 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Observation Flat Surface SPM PBTG/SMCG H™ “|
ste | 7 |
| 1 | TE 186.2 1884 210A
10 | T™ 189.6 190.7 1.5997 | _ 0.1971

“TE 188.9 205.7
1943

“a0.

i023
0.2081
1055
TE 159.2 212.3 192.7

“TE | Mid |
* Parameters Q and H are computed from the brightness temperatures from the numerical
simulation results.

Table 6.4.2. ‘The brightness temperatures of Fig. 6.4.5

and horizontal polarized waves, respectively. The empirical parameter Q
represents coupling between polarizations. On the other hand, the factor
exp(—H cos* ;) represents depletion of reflectivity. Both Q and H are as-
sumed independent of observation angles and soil moisture.

In Table 6.4.2, we tabulate the brightness temperatures of Fig. 6.4.5
based on numerical simulations for the permittivity of 17 + 72.0 and also
use the simulated results to compute Q and H parameters from (6.4.36) and
(6.4.37). The table shows that Q and H are actually functions of observation
angles, In the original proposal [Wang et al. 1983], H is supposed to be 4k?h?
where / is the rms height. For this case, 4k?h? = 14.19. From Table 6.4.2,
H is much smaller than 14.19. The table shows that Q and H are empirical
parameters that do not have physical meaning.
--- PAGE 365 ---
§4.5 Numerical Simulations of Emissivity of Soils 343
4.5 Numerical Simulations of Emissivity of Soils with Rough Sur-
faces at Microwave Frequencies

Tn this section, we illustrate the numerical simulation results of emissivities
of wet soils with 2-D rough surface (3-D problem). A key result is that emis-
sivities are calculated for soils at two frequencies using the same values of
physical roughness parameters of rms height and correlation length in cen-
timeters. The simulations have important applications in microwave remote
sensing of soils. In practice, active and passive sensors are used at different
frequencies and incident angles. The same physical roughness parameters
are independent of sensor characteristics and should be used to characterize
the soil surface. Simulations in this section are based on Gaussian random
rough surfaces with Gaussian correlation functions. In the numerical results,
the surface area used is 64 square wavelengths. We use 64 points per square
wavelength as coarse grid and 256 points per square wavelength as dense
grid, which leads to a total of 98,304 surface unknowns. For the rough sur-
faces with rms height of 0.3 wavelength, correlation length of 1.0 wavelength,
and relative permittivity of 17 + 2i, the total CPUs for the single dense grid
with SMCG are about 45 hours for TE wave and 49 hours for TM wave, re-
spectively, on DEC 3000/700 workstation. By using the PBTG with SMCG,
the CPUs are about 8.5 hours for TE and 9.0 hours for TM, respectively, for
the same case. The permittivities of wet soil by weight of the soil moisture at
L-band (1.4 GHz) are listed in Table 6.4.3. The permittivities of soil by the
soil moisture in volumetric water contents (em*/cm*) for L- and C-bands
are given in Table 6.4.4. C-band is at 5 GHz. Permittivities are based on the
results of [Wang and Schmugge, 1980] and are also given in Eq. (5.4.1) of
Volume [. All the cases are computed at the observation angle of 50 degrees,
unless otherwise indicated. In Tables 6.4.5 to 6.4.9, emissivities are tabu-
lated for ease of comparisons by interested readers. We also illustrate the
brightness temperatures in Figs. 6.4.7 to 6.4.11. The physical temperature
is taken as 300 K for all cases.

(A) Variation of Brightness Temperatures at L-Band of Wet Soil with
the Soil Moisture and Correlation length at Fixed rms Height

In Figs. 6.4.7 and 6.4.8, we plot the brightness temperatures as a function
of soil moisture by weight at L-band for horizontal and vertical polariza-
tions, respectively. The corresponding permittivities are taken from Table
6.4.3. The rms height is fixed at 0.1 wavelength and the correlation lengths
are varied from 0.33 to 1.0 wavelengths. It is shown that brightness tem-
--- PAGE 366 ---
344 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Permittivity | 4.06-+ | 4.81+ | 5.564 | 7.354 | 10.8-+ | 14.254 [17.7+ [21.354 | 24.64
Table 6.4.3. Relative permittivities of soil moistures in weight at L-band.
Permittivity | 3.66+ | 466+ | 6.26+ [845+ [113+ | 15.24 [i924 [ 23.04
Permittivity [362+ | 452+ [5.944 | 7.904 | 1044+ [1394+ [ 1744 | 20.8+
Table 6.4.4 Relative permittivities of soil moistures in volumetric water content (cm /emn®*)

at L- and C-bands.
Mare
(%)
0.7286
roo
0.5990
0583
0.4366
Table 6.4.5 Computed soil emissivities at L-band. Horizontal polarization; rms height =
0.1 wavelength, observation angle = 50 degrees.
Nostare
%)
0.8084
Table 6.4.6 Computed soil emissivities at L-band. Vertical polarization; rms height =
0.1 wavelength, observation angle = 50 degrees.
--- PAGE 367 ---
§4.5 Numerical Simulations of Emissivity of Soils 345
Emissivity Soil Moisture in Weight (%)
h (case 2) | 0.8392 | 0.8053 0.7519 | 0.6868 | 0.6376
h (case 3) 0.7820 | 0.7686 | 0.7252 [0.6593
0.9437 | 0.9308 0.8568 0.7841 | 0.7535
0.9289 0.7698 [0.7385
0.9302 | 0.9154 | 0.9052 0.8266 | 0.7840
Case 1: rms height = 0.1 wavelength, correlation length = 0.333 wavelength,
observation angle = 50 degrees
Case 2: rms height = 0.3 wavelength, correlation length = 1.000 wavelength,
observation angle = 50 degrees
Case 3: rms height = 0.3 wavelength, correlation length = 1.000 wavelength,
observation angle = 55 degrees
Table 6.4.7 Computed soil emissivities for different soil moistures at L-band.
Emissivity Volumetric Water Content (cm* /cm’)
025
h (L-band) | 0.8434 | 0.8008 | 0.7490 | 0.6996 | 0.6446 0.5278
h (C-band) | 0.8626 | 0.8285 | 0.7900 | 0.7613 0.6658 | 0.6813 | 0.6032
v (L-band) | 0.9615 | 0.9444 [0.9181 0.8424 | 0.7995
v (C-band) 0.9178 | 0.8867 | 0.8441 0.7630 0.6989
rins height = 2.45 cm, correlation length = 8.0 cm, observation angle = 50 degrees;
L-band: f = 1.4 GHz; C-band: f = 5.0 GHz.
Table 6.4.8 Computed soil emissivities for different volumetric water contents.
Emissivity Volumetric Water Content, (em? /em*)
7 (band) 6198 | O.s807
h (C-band) | 0.8202 0.7290 | 0.6778 | 0.6234 | 0.5656
v (L-band) 0.9747 0.9132. | 0.8766 0.7633
(C-band) 0.9430 0.8820 0.7968
rms height = 0.73 cm, correlation length = 3.5 cm, observation angle = 50 degrees;
L-band: f = 1.4 GHz; C-band: f = 5.0 GHz.
Table 6.4.9 Computed soil emissivities for different volumetric water contents.
--- PAGE 368 ---
346 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
260; a
§ 240
2S
$220, SSSA. correlation length = 0.33
EB SQ
E aN
3 180- SSS
5 S&
3 SS
Brso} correlation engin = 10 Se
2 SEES
5140 ——
1205 10 5 2t”t*~SS
soil moisture in Weight (%)
Figure 6.4.7 The variation of brightness temperatures at L-band with the soil moistures
in weight. The rough surface is with rms height of 0.1 wavelength and correlation lengths
from 0.33 to 1.0 wavelength. ‘The observation angle is at 50 degrees. Horizontal polarization.
290- ——— — = — — — > -
ge |
S270 * l= 0.38, 0cl=1.0 -
3
&
> 260
3S ‘
g
3250: \. |
g \
2 <<
§e40- N
3 AN i
2230 iN 1
= A:
5220 NN
2105 10 15 pn)
soil moisture in weight (%)
Figure 6.4.8 The variation of brightness temperatures at L-band with the soil moistures
in weight. ‘The rough surface is with rms height of 0.1 wavelength and correlation lengths of
from 0.33 to 1.0 wavelength. The observation angle is at 50 degrees. Vertical polarization,
--- PAGE 369 ---
§4.5 Numerical Simulations of Emissivity of Soils 347
perature decreases with the increase of soil moistures for both horizontal
and vertical polarizations. For horizontal polarization, soils with largest cor-
relation length of 1.0 wavelength have the smallest brightness temperature
and vice versa. For vertical polarization, this feature is not. exhibited. The
surface roughness has a larger influence in brightness temperature for hori-
zontal polarization than the vertical. The brightness temperature in vertical
polarization is mainly determined by the rms height for this case. With the
increase of soil moisture, the differences in brightness temperatures between
different correlation lengths increase. For horizontal polarization, the biggest
difference in brightness temperature increases from 12.7 K degrees for 5% of
soil moisture to 18.6 K degrees for 25% of soil moisture. It increases from
1.86 K degrees to 6.72 K degrees for the corresponding vertical polarization.
This shows that the effects of surface roughness become larger for large soil
moisture than small one.

(B) Variation of Brightness Temperature at L-Band with the Soil Mois-
tures for the Rough Surfaces with the Fixed rms Slope and Different rms
Height

In Fig. 6.4.9, the brightness temperatures are plotted as a function of soil
moisture in both horizontal and vertical polarizations. Two sets of simulation
results are used. One is with rms height of 0.1 wavelength and correlation
length of 0.33 wavelength. The other is with rms height of 0.3 wavelength and
correlation length of 1.0 wavelength. The rms slopes for these two cases are
the same. It can be seen that the increase of rms height decreases the differ-
ence in brightness temperature between horizontal and vertical polarizations.
As scattering by rough surface increases, there is “mixing” of polarizations.
The roughness effect is more pronounced for horizontal polarization.

(C) Variation of Brightness Temperatures with the Soil Moistures at
Both L- and C-Bands Using the Same Physical Roughness Parameters
The brightness temperatures in passive microwave remote sensing are mea-
sured at L- and C-bands. So it is useful to compare the brightness tem-
peratures of soils at L- and C-bands using the same values in centimeters.
of physical roughness parameters of rms height and correlation length. We
also use the same physical values of moisture for the two frequencies. In
Fig. 6.4.10, we plot the brightness temperatures as a function of soil mois-
ture in volumetric water content at both L- and C-bands. The corresponding
permittivities are taken from Table 6.4.4. The physical parameters are that
--- PAGE 370 ---
348 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
9300 gp
280¢
3260 oN
2 i
s . ~
@240h—~_ ° ° ee
2220 — * waa
5 Ie .
8 200-
g °
& . °
ies ~~ °
—_ |
160 Lt
1405 10 15 20 25
‘soil moisture in weight (%)
Figure 6.4.9 The variation of brightness temperatures with the soil moistures in weight.
The rough surfaces are with rms height of 0.1 and 0.3 wavelength and correlation lengths
of 0.33 and 1.0 wavelength, respectively. The two surfaces have the same rms slope. The
observation angle is at 50 degrees. The Solid line and dash line is h- and v-polarization with
rms height of 0.1 wavelength, respectively. The circle and star is h- and v-polarization with
rms height of 0.3 wavelength, respectively.
:300.—<$___—_—_—_—____——.Y>} SH
£ . oo ~
3 , ms
£ 250P— o ~s
a ™ ~
~ aa
‘ Nt :
S ~ °
5 NN
— ~.
Bos 04015 02 025 03 008 04
volumetric water content (em°/cm*)
Figure 6.4.10 The variation of brightness temperatures with the soil moistures in volu-
metric water content at L- and C-bands using the permittivities in Table 6.4.4. The physical
rough surface parameters are rms height of 2.45 cm and correlation length of 8.0 cm. The
observation angle is at 50 degrees, The Solid line and dash line is h- and v-polarization at
L-band, respectively. The circle and star is h- and v-polarization at C-band, respectively.
--- PAGE 371 ---
§4.5 Numerical Simulations of Emissivity of Soils 349
300, —— —- eo
280 . . _ “os ~
$260 tO
2 . me
© 240} 7 + 7
So
5 220 Ne +
E 200 NN 8
2 ae
2 180) NN
5 ™ ©
5 160] — °
140 |
O05. 01 015 02 02 03 085 04
‘volumetric water content (omS/cm®)
Figure 6.4.11 The variation of brightness temperatures with the soil moistures in volu-
metric water content at L- and C-bands using the permittivities in Table 6.4.4. The physical
rough surface parameters are rms height of 0.73 cm and correlation length of 3.5 cm. The
observation angle is at 50 degrees. ‘I'he Solid line and dash line is h- and v-polarization at
L-band, respectively. The circle and star is h- and v-polarization at C-band, respectively.
the rms height is 2.45 cm and correlation length is 8.0 cm. We can see that the
brightness temperatures are higher at C-band than at L-band for horizontal
polarization and lower at C-band than at L-band for vertical polarization.
Since the permittivities between L- and C-bands are comparable, the results
indicate that roughness has a larger effect on C-band than at L-band. In
Fig. 6.4.11, the results are shown with different rough surface parameters.
The rms height is 0.73 cm and correlation length is 3.5 cm in this figure.
Comparing the results of Figs. 6.4.10 and 6.4.11 indicates that as roughness
decreases, the brightness temperatures of L- and C-bands are closer to each
other.
(D) Comparisons with Empirical Formula
In passive remote sensing with soil, a popular model for calculating the
brightness temperatures from soil is the Q and H empirical model given in
Eqs. (6.4.36) and (6.4.37). In Table 6.4.2 we have shown that Q and H are
dependent on observation angles.
In Tables 6.4.10 and 6.4.11, we tabulate the values of Q and H com-
--- PAGE 372 ---
350 6 3D WAVE SCATTERING FROM 2-D ROUGH SURFACES
QandH | Volumetric Water Content (cm /em’) :
oe | Oi [tus 0]
Q (L-band) | 0.1304 | 0.1242 | 0.1190 | 0.1292 | 0.1258 | 0.1144 | 0.1305 | 0.1407 |
H (L-band) | 0.4661 0.4337 | 0.4189 | 0.3718 | 0.3273 | 0.3289 | 0.3148
Q (Cand) | 0.2644 0.2793 | 0.3248 | 0.3255 | 0.3157 | 0.3173 | 0.3200
A (C-band) | 0.4013 | 0.3956 | 0.4246 | 0.4812 | 0.4520 | 0.4284 | 0.4233 | 0.4084
ms height = 2.45 cm, correlation length = 8.0 cm, observation angle = 50 degrees;
L-band: f = 1.4 GHz; C-band: f = 5.0 GHz.
Table 6.4.10 Parameters Q and H determined from the numerical simulation results of
Fig. 6.4.10.
Qand I Volumetric Water Content (cm? fem) |
10.05 | 0.10 | 0.15 | 0.20 | 0.25 | 0.30 0.40
Q (L-band) | -0.0344 -0.0356 | -0.0457 | -0.0866
Hf (L-band) | 0.0271 0.0538 0.1051 | 0.1547 | 0.1437 | 0.1297 | 0.1441 | 0.1436
Q (C-band) | 0.1111 [0.1106 | 0.1085 [0.1127 0.1074 | 0.1107 | 0.1169
H (C-band) | 0.1541 | 0.1769 | 0.2044 0.1919 | 0.1622 | 0.1573
rms height = 0.73 cm, correlation length — 3.5 cm, observation angle = 50 degrees;
L-band: f = 1.4 GHz; C-band: f = 5.0 GHz.
Table 6.4.11 Parameters Q and H determined from the numerical simulation results of
Fig. 6.4.11.
puted from (6.4.36) and (6.4.37) by using the brightness temperatures of
Figs. 6.4.10 and 6.4.11 based on numerical simulations. The tables show
that parameters of Q and H are dependent on soil moistures, frequencies,
and observation angles. The tables show that Q and H are empirical param-
eters that do not have physical meaning. On the other hand, the physical
roughness parameters are rms height and correlation length in absolute value
of centimeters. They are physical characteristics of the roughness and are in-
dependent of angles, frequencies and soi] moistures.
5 Four Stokes Parameters Based on Tangential Surface
Fields
The four Stokes parameters of passive remote sensing are described in Sec-
tion 5.4 of Chapter 3 in Volume [. In previous sections, we calculate the four
Stokes parameters by using one minus the integration of the bistatic scatter-
--- PAGE 373 ---
85 Four Stokes Parameters Based on ‘Tangential Surface Fields 351
incident wave
8 a put
Region 1 Ey = Ei tbs
. Ay=Hi+ds
ee
Hyg = tig

Region 2 Eo, He
Figure 6.5.1 Incident wave in direction $,, and brightness temperatures in direction
$0 = —Sob-
ing coefficients. On Monte Carlo simulations, the emissivity and absorptivity
can also be calculated directly from the surface fields.

Consider a dielectric medium with a surface S, normal 7, with a physical
temperature T, Consider an incident wave in direction 8,,, with incident
power P; (Fig. 6.5.1). Let a@g(8,) be the absorptivity when the incident
wave has polarization 3. The absorptivity is the fraction of the incident
power that is absorbed by the medium. Then from (3.5.75a—d) of Volume I,
the brightness temperatures of the four Stokes parameters in the observation
direction of §, = —S,, are

Tpv($0) = Tan (Soo) (6.5.1)
Tan (0) = Tan(Sov) (6.5.2)
Up (80) = Tpv(80) + Ten (So) — 2T ap (800) (6.5.3)
Va(80) = Tau(80) + Tan (So) — 2Tar(Sos) (6.5.4)
where subscript v means vertical polarized, h means horizontal polarized,
subscript P refers to linear polarization with incident polarization vector
~ Lr. a
Pas, [®ce) + iGon)| (6.5.5)
and subscript FR is right-hand circular polarized with incident polarization
vector
~ 4 .
R=— [@ Son) + tA(3ep | (6.5.6
3 (Bop) ) )
Let the incident wave of @ polarization with 6 = v, h, P, R has electric
field E; and magnetic field H; and the scattered wave has fields E, and H,.
Tn region 1,
FE, =F; +E (6.5.7)
--- PAGE 374 ---
352 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Hy =H, +H, (6.5.8)
and in region 2, the fields are £2 and Hy. The boundary conditions are
Ax By =ax By (6.5.9)
aX HL =Ax Ay (6.5.10)
Let Pj, Ps, and Py be respectively the incident power, scattered power, and
the absorption power. Then
Pa
a3 => 6.5.11
B= (6.5.11)
By conservation of energy
Po=Pa+Ps (6.5.12)
so that
P; .
=1-= 6.5.13.
ag P, ( )
The incident Poynting’s vector is
= 1 a
3, = 5Re (Ei x Hi) (6.5.14)
and the scattered and transmitted wave Poynting’s vector are respectively
= 1 — _
5, = 5Re (E. x F.) (6.5.15)
a
Bp = 5Re (B: x TT) (6.5.16)
Both S$; and S, are divergence free. In view of the divergence theorem, the
surface integral over Poynting’s vector to get power for $; and S, can be
taken over surfaces in region 1. In particular, we can use the the rough surface
(Fig. 6.5.1). Thus
= 1 —
P= -[ dS3;-a= ~ [as5Re (E x ,) A (6.5.17)
s s
= 1 => o>
P= [ass AS [assre (B. x 7.) a (6.5.18)
Thus the absorptivity is
1 ll (a=
=1-5 | ds5Re(E,x Hi) + 6.5.19
ag ah, S4Re(E, x H.) -a (6.5.19)
1 1 a a
=1- x [as5Re [Ei -E,) x (m-™)] fa (6.5.20)
PJs 2
In Monte Carlo simulations, we calculate the tangential surface fields ft x
‘E, and i x Hy. Absorptivity can be calculated by using (6.5.20). Another
--- PAGE 375 ---
§5 Four Stokes Parameters Based on Tangential Surface Fields 353,
formula can be derived as follows. The power absorbed is obtained from the
integration of dissipation over region 2
loos
Pa -[ ar swenE2 By (6.5.21)
Va
Using Maxwell’s equations, we have
v- [5Re (Ee x 7)| =V- = 5weSBa BR (6.5.22)
Thus
Pa -f dFV -S2= [4532-0 (6.5.23)
Va Js
7 1 ‘—
= | asi. [Re (Ba x 7)} (6.5.24)
s
However, since tangential electric and magnetic fields are continuous, we
have
Py= [ Si [3Re (i xT1)} (6.5.25)
Js
The absorptivity is
1 1 = a
= 5 | asa-|5Re(E, x 7) 6.5.2
a3 7 [ase [sre ( Lx i)| (6.5.26)
Using Monte Carlo simulations, the surface fields are calculated. Thus we
can use the two forroulas derived in this section to calculate the absorp-
tivity from the tangential surface fields. Once the absorptivity for the four
different polarization incidences, v, h, P, and R, are determined, the bright-
ness temperatures of the four Stokes parameters can be calculated. We can
also verify conservation of energy. Reflectivity rg is integration of scattered
power. Thus we can use the surface fields to get rg.
1 [aszre(E xH) a
ra=> 5 .
B Pilg s s
lf 1 = oR =p >* ~
= ral assRe|(E:— Bi) x (H,-H)|-2 (6.5.27)
PJs 2
Energy conservation can be verified by checking that
rg of (6.5.27) + ag of (6.5.26) = 1 (6.5.28)
--- PAGE 376 ---
354 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
6 Parallel Implementation of SMCG on Low Cost Beowulf

System
6.1 Introduction
The need for solving MoM for large-scale rough surface problems is appar-
ent. (1) For example, in low grazing problems, the surface area has to be
very large in order to include the multiple scattering and shadowing effects.
(2) For scattering and emission by soil surfaces or ice surfaces, it is impor-
tant to solve larger scale problem of several thousand square wavelengths
to better study the target response. (3) For the case of ocean surfaces, the
roughness is of many scales from several wavelengths to sub-wavelengths. In
order to simulate the overall response, a larger surface is needed. (4) Fine
discretization is needed for surfaces with lossy dielectric. All these prob-
lems require millions or tens of millions of surface unknowns in the MoM
implementation of surface integral equations. With the advent of fast com-
putation methods, new frontiers are opened for large-scale simulations. Fur-
thermore, the use of parallel computing will enhance the capabilities. In the
past, parallel computing is hampered by the cost of massively parallel pro-
cessors (MPP). High performance computing has been static because of the
high price/performance ratio. However, recently the parallel computing is
made more possible with low cost Beowulf system of PC clusters [Sterling
et al. 1999]. For a Beowulf cluster, a node is a personal computer from the
commercial mass market with LINUX as the operating system. Also critical
to the recent success of Beowulf was the development of low cost moderate
bandwidth local area network (LAN). The Beowulf project was started at
the Center of Excellence in Space data and Information Science (CESDIS),
NASA, Washington DC in 1994 to provide affordable parallel computing
capability. It received worldwide acceptance among academic and research
institutions.

In the previous sections, we have used the SMCG method for solving
large-scale problem. A salient feature of SMCG is that it is FFT based. Since
MPI (message-passing interface) of FFT is available [Frigo and Johnson,
1997], this facilitates the implementation of SMCG on low cost Beowulf
system. This has been accomplished at the City University of Hong Kong
{Li et. al. 1999, 2000b].

In this section, we present a cost-effective solution by implementing the
SMCG method on a Beowulf system that consists of PC’s (processors) con-
nected by 100 Base TX Ethernet switch. The workloads of computing the
sparse-matrix-vector multiplication corresponding to the near interactions
and the fast Fourier transform (FFT) operations corresponding to the far in-
--- PAGE 377 ---
86.2 Low-Cost Beowulf Cluster 355
teractions in the SMCG method can be easily distributed among all the pro-
cessors. Both perfectly conducting and lossy dielectric surfaces of Gaussian
spectrum are analyzed thereafter. When possible, speedup factors against a
single processor are given. It is shown that the SMCG method for a single
realization of rough surface scattering can be efficiently adapted for paral-
lel implementation. The largest number of surface unknowns solved in this
section is over 1.5 million. On the other hand, a problem of 131,072 surface
unknowns for a PEC random rough surface of 1024 square wavelengths only
requires a CPU time of less than 20 minutes.

6.2 Low-Cost Beowulf Cluster

We describe the Beowulf system that was used to perform the computations
presented in this section.

A. The Hardware

The Beowulf system at City University of Hong Kong that is used to com-
pute results in this section consists of 17 computing processors (nodes) which
are connected to two 3Com Superstack LinkSwitch 300 Fast Ethernet switch
with twelve 100 Base TX ports. A 24-port switch would provide faster net-
working speed. A 9-node system was first installed to try out the concept
using a 12-port switch. This system was later expanded to 17 nodes with an
addition of 12-port. switch. Each computing node has an Intel Pentium I 450
MHz Processor, 256 MByte SDRAM and a 3Com 3C905 Network Interface
for connection to the communication switch. One of the nodes is designated
as the server and it has 12 GBytes of hard disk. All the other nodes either
has 1 or 2 GBytes of hard disk so that they can be used individually. The
whole set up was under US $30,000 in 1998. Although the 1000 Base TX
Ethernet card and switch are now available, the price is still too expensive.
Optical fiber will be required for the connections between the PC’s and the
switch. It is estimated that an additional cost of approximately US $50,000
is needed in 1999 to upgrade the Beowulf to 1000 Base TX connection using
the existing 17 PC’s. It should be noted that the speed of the computer code
highly depends on the hardware. When PC’s were upgraded from 233 MHz
to 450 MHz while all other hardware remains unchanged, a speed up factor
of 1.6 was obtained. The communication time among processors for rough
surface simulations using integral equation approach is small compared to
that of the matrix-vector multiplication. It is more cost effective to upgrade
the system using faster processors than to upgrade the Ethernet cards and
communication switch.
--- PAGE 378 ---
356 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
B. The Software

The system software requires Redhat Linux Version 6.0 and the Message
Passing Interface (MPI) Version 1.1.2. Detailed system software set up can
be found in the CESDIS web page. The aim of MPI is to develop a widely
used standard for writing message-passing programs [Gropp et al. 1994]. The
message-passing model consists of a set of processes that have only local
memory but are able to communicate with other processes by sending and
receiving messages from one node to the other and vice versa. Data transfer
from the local memory of one process to the local memory of another requires
operations to be performed by both processes.

A key to the numerical efficiency and computer memory reduction of the
SMCG and PBTG methods is the use of FFT’s for performing the convolu-
tion of the weak part of the matrix-vector multiplication. The MPI version
of the fast Fourier transform code was adopted — the Fastest Fourier Trans-
form in the West (FFTW) developed by the Laboratory of Computer Sci-
ence, MIT [Frigo and Johnson, 1997] was used. This subroutine is written in
C. A Fortran wrapper was written so that this subroutine was incorporated
in the parallel Fortran codes. In addition, a real-time monitoring system was
also developed so that all the MPT commands can be monitored on the fly.
6.3 Parallel Implementation of the SMCG Method and the PBTG

Method
In applying the SMCG method, we rewrite the MoM matrix equation
[Z]{z} = {0} as
[2° (o} + 12" If2} = 0} (6.6.1)
where [Z*] and [Z“] correspond to the strong near-field interaction and the
weak far-field interaction, respectively. The distance chosen to distinguish
the near and far interactions is defined so that the Green’s functions can
converge rapidly within a few orders of Taylor series expansion about z = 0
when the separation between the source and field point is beyond rg. In this
section, we use 49 terms in the expansion, The convolution of [7*]{x} is
computed by direct multiplication. In contrast, for the far interactions [Z“],
because of the expansion of the Green’s function with the Taylor series,
[Z”]{x} can be computed using FFT’s as
[2°\{2} = VOTaJF" (GF - Lalo} (6.6.2)
i=0
where [Tj 49] is a block diagonal matrix, [Gj] is a block Toeplitz matrix, and
quantity with a tilde means that it is in the Fourier domain. The number of
--- PAGE 379 ---
§6.3 Parallel Implementation of the SMCG Method and the PBTG Method 357

terms in the summation depends on the order of the Taylor series expansion.

Substituting (6.6.2) into (6.6.1), the unknown vector {x} is solved iteratively

as

[Z"{a°} + [Too]F~! « [GolF - [Tor}{x°} = {6} (6.6.3)
[Z°]{a""} + [Tos] FO! - [Gol F - [Tox] {21}
= {6} — SMa]: [Gi] - (Tal{2"} = {0"} (6.6.4)
i=l

In all the examples shown, the maximum value of n is 4 while the typical
value is 2. The number of CG iteration steps reduces significantly when n in-
creases. Initially, the error norm of the CG method may be reduced rapidly.
This reduction may eventually be flattened out. Therefore, the maximum
number of CG iterative steps was set at 100 for each value of n. After mod-
ifying the right-hand side, the CG will converges rapidly again. All terms in
both (6.6.3) and (6.6.4) can be parallelized easily as will be discussed.

For a lossy dielectric rough surface with high permittivity, we use the
PBTG method. The Green’s function in the lower region is heavily attenu-
ative. Thus, matrix elements of the Green’s function for the lower medium
correspond to source and field point separation beyond a radial distance rg
can simply be set to zero.

(1) The matrix-vector multiplication corresponds to the Green’s function in
the lossy medium is a sparse-matrix-vector multiplication operation on
the dense grid.

(2) For the near interactions of the free-space Green’s function, the near-
interaction range rg defined in the SMCG method is further divided into
two regions. Within a radial distance r, (< rq) of the source point, we
have sparse-matrix-vector multiplication on the dense grid.

(3) For the interactions between r, and rq, we have averaging from the dense
grid to the coarse grid, sparse-matrix-vector multiplication on the coarse
grid and interpolation from the coarse grid to the dense grid.

(4) Beyond rq, the convolution between the far interactions [Z“’] corresponds
to the free-space Green’s function and the vector {x} will be computed
by averaging from the dense grid to the coarse grid, using FFT’s for
matrix vector multiplication on the coarse grid and interpolation from
the coarse grid to the dense grid.

In the lossy surface sinmlations, we select rg = 3A, and re = 0.5A,, which

make the Taylor expansion converges quickly and the Green’s function in the

lower medium sufficiently attenuated beyond . The procedure for averaging
and interpolation in the convolution of the free space Green’s function is
--- PAGE 380 ---
358 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
described by the equation

N

Ym = S_GolkolFm —Fr|)-ta, m=1,2,...,N (6.6.5)

n=l
where m and nm are indices in the coarse grid and 7 in the dense grid. A
coarse grid can be used for the non-near field convolution of the free space
Green’s function because the free space Green's function is spatial frequency
limited on the dense grid. The value of x at % is obtained from the average
of the values of x at the dense grid. After the convolution using the coarse
grid, the values of y at the dense grid will be interpolated from the coarse
grid. Tt is not difficult to see that the steps of averaging and interpolation
in the PBTG method would not cause significant additional computation to
the SMCG method when analyzing lossy dielectric rough surfaces.

Parallel implementation of the SMCG method has been reported (John-
son et al. 1996, 1999; Pak et al. 1997; Johnson and Chou, 1998] on the
multimillion-dollar IBM SP/2-based parallel computer at the Maui High
Performance Computing Center. However, the parallelization that is imple-
mented in this section is for a single realization of rough surface and for oue
incident angle with a large number of surface unknowns. Previous efforts are
for different realizations and/or different incident angles.

In this section, parallel versions of both the SMCG method and the
PBTG method are implemented on the low-cost Beowulf system. The sparse-
matrix-vector multiplications are implemented using parallelization so that
both the CPU time and memory storage are distributed among the proces-
sors. The use of the MPI version of FFTW, however, requires less computer
memory than that of distributing the multiple FFT calls among the proces-
sors. For an N x N FFT, the implementation only requires to store N/Np
rows of the N x N array where Np is the number of processors used. There
is no significant difference in the CPU time required in these implemen-
tations of the weak part of the matrix-vector multiplication. However, the
reduced memory requirement may be important in implementing the multi-
level SMCG method [Chan et al. 1998; Li et al. 2001]. In this multi-level
SM/CM scheme, the strong interaction range and hence the memory stor-
age of the sparse matrix can be reduced significantly. On the other hand,
3-D FFT’s will, be required and the memory reduction in the FFT’s become
important. Apparently, the use of the MPT version of FFTW can distribute
the computation evenly among the processors and can better synchronize
the parallel code as opposed to distributing the multiple FFT calls among
the processors.
--- PAGE 381 ---
§6.3 Parallel Implementation of the SMCG Method and the PBTG Method 359

In the following, we briefly describe the parallelization of the key steps
in the SMCG and PBTG methods.

A. Sparse-Matrix-Vector Multiplication

For a large rough surface, the number of the non-zero elements of the strong
matrix [Z*] may still be too large to store, so we recalculate them when
necessary. When the number of surface unknown is manageable, we only
compute the strong matrix once and store them in an array instead. The
strong matrix [Z*] is computed in parallel and distributively stored among
the processors. The unknown vector {x} is stored in all processors for the
convenience of performing the conjugate gradient procedure. Note that stor-
ing an array of a couple of million elements does not require much memory
storage but it can reduce some communication time among the processors.
Each processor performs a different part of the sparse-matrix-vector multi-
plication, then the results in each processor are combined and broadcasted
back to all processors.

B. Diagonal Matrix Pre-Multiplication, Fast Fourier Transform, and Di-
agonal Matrix Post-Multiplication

The convolution of the weak matrix with the vector is performed by FF T's.
Tn order to perform the convolution, the array should be zero padded before
applying the FFT’s, and the original array is only one quarter of the zero-
padded one. The zero-padded array is uniformly distributed among all 16
processors, while only half of the processors, in which one quarter of the zero-
padded array is stored, perform the pre-multiplication. Upon applying the
forward FFT, only 1/16 of the array F -[Tpi]{x} are stored in each processor.
Similarly, the corresponding 1/16 of the array [Go] are stored in the same
processor. ‘The products between the elements of these two arrays are carried
out in parallel. Upon taking the inverse FFT, only one quarter of the full
array residing in half of the processors require the post-multiplication.

Tn performing the FFT’s, we use the MPI_FFT transposed command
which is much faster than the normal FFT operation. We perform the trans-
posed FFT command twice, one for the forward FFT and one for the inverse
FFT as shown in (6.6.3) and (6.6.4). The result will be stored in the original
sequence as depicted in Fig. 6.6.1.
--- PAGE 382 ---
360 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
Forward FFT Tnverse FFT
Figure 6.6.1 Storage of the partitioned array in each step of the FFT’s.
6.4 Numerical Results
In this section, we present results for PEC and lossy dielectric surfaces with
Gaussian spectrum. For the PEC and lossy dielectric surfaces, we compare
the bistatic scattering coefficients obtained from a single processor and 16
processors to verify the parallel version codes. We only use 16 instead of 17
processors in our present parallel codes because of the radix-2 FFT require-
ment although we can slightly improve the computation by using 17 nodes
for all the operations other than the FF’I’s. We also give the comparison
between the results obtained with near-field integration and those obtained.
by the collocation method to demonstrate the accuracy improvement after
using the near-field integration. The brightness temperature is calculated by
multiplying the emissivity with the surface physical temperature, which is
chosen to be 283K in this paper. The emissivity is obtained by integrating
the scattering coefficients above the half space. For the simulations in this
section, we choose the radius of the incident tapered wave spot size to be
1/3 of the edge length to provide sufficient field attenuation at surface edges.
For PEC cases, we use the SMCG method, while the SMCG/PBTG method
is used for lossy dielectric surfaces. In the SMCG/PBTG method, we choose
Te = 0.50, ra = 3Aq and 64 points per square wavelength for the coarse
grid and 256 points per square wavelength for the dense grid. For lossy di-
electric surfaces, the permittivity ¢, = 45 + 130 is used. The CG iterations
are stopped when the error is at 1%.

For Gaussian surfaces of rms height, h, up to 0.3, and size up to 32 by
322 with a correlation length of 1A, we present the bistatic scattering cocf-
ficients and/or brightness temperatures. In Figs. 6.6.2 and 6.6.3, we give the
bistatic scattering coefficients of the PEC and the lossy dielectric surfaces.
‘The results using a single processor and those using 16 processors overlie each.
other. It is important to compare the CPU time between a single processor
and 16 processors. In ‘Tables 6.6.1 and 6.6.2, we show the comparison of CPU
time for calculating PEC and lossy dielectric surfaces, respectively. Speedup
factor is also tabulated. The tables indicate that the speedup factor increases
--- PAGE 383 ---
§6.4 Numerical Results 361
35
£30 co i
3 parallel | i
8 it
e 2s | i 7
3 Le singe i
20 | 7
Bol |
aa
3 |
21s | ha i
3 id
2 i
3 10 it
2s fy
jo
0
# 10 50-30-10 «10 30 50 700
scattering angle degree)
Figure 6.6.2 Comparison of the bistatic scattering coellicients for PEC rough surface
obtained by the single code and parallel code. 8 x 8\2, h = 0.1Ag incident angle = 40°
1.6
ia A
2 parallel it
B12 single | ‘|
g —_snee i
en i '
° ii |
A=] i
E 08 | it
a It
206 Ay
2 Phor 4
204 PAP |
2 pp 4
02 JEN
a! Ae
-90 60 -30 0 30 60 90
scattering angle (degree)
Figure 6.6.3 Comparison of the bistatic scattering coefficients for lossy dielectric rough
surface obtained by the single code and parallel code. 8 x 8\2, h = 0.2A incident angle =
30°, €p = 45 + 430.
--- PAGE 384 ---
362 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
~~ CPU time (Sec.)
Surface size (42) | Number of unknowns Parallel code
code factor
xs | 8,192 785 | __ 66
16x16 32,768 1373 | 220
| 32x32 131,072 rs ee ee
64x64 | 524,288 [ae 6045
{32x32 | (oneCGterm) | —_ 382.48 92
L_ 64x64 ‘one CGterm) | 4381.74 | 115.61 37.9
Table 6.6.1 Comparison of CPU time for PEC rough surface h = 0.19.
Surface size | Number of | ™S |. CPU time (Sec.) i
(2) | unknowns | height i) | Sequential Parallel code
___code factor
0.05 49,368 9.77 |
7,643 | 1LS7 6712
114,385 11.55 __ 9,906
8x8 98,340 0.20 161,313 11.79. 13,682
0.25 207,095 ‘41,92. 17,371
L030 275,485 _ 12.23, 22.517
303,216 0.05 270,204 | 13.20 20,477
0.10 469,831 13.43 | 34,981
a [ 133,798
ane es ee |
Table 6.6.2 Comparison of CPU time for lossy dielectric rough surface ¢, = 45 -+ 130.
when the number of unknowns increases. For the surfaces with the same size,
the CPU time increases with h because of the slow convergence of the CGM
for rougher surfaces. For example, it only needs 2 iterations (n = 1) with 40
CG terms in the first iteration and 1 CG term in the second iteration for the
8 x 8)? surface with h. = 0.05A,. In contrast, it needs 3 iterations (n = 2)
with 100 CG terms in the first iteration, 41 CG terms in the second iteration
and 4 CG terms in the last iteration when h increases to 0.3A,. The speedup
factors become large when the CPU time increases. It is shown that the
best speedup factor is around 13.7 for the PEC surface with 32,768 surface
unknowns and h = 0.1X,9, and 13.4 for the lossy dielectric surface with 0.4
million surface unknowns for the same h. For the PEC surfaces, CPU times
of the parallel code are obtained when the strong matrix is computed once
--- PAGE 385 ---
§6.4 Numerical Results 363
| Total time
___Commmmnicationtime | AB

Near interaction calculation time i 2918.6 s
____Far interaction calculation time | 289A 8
_____Emissivity calculationtime | 205.78
Table 6.6.3 CPU time distribution for the case of 8 x BA? surface with h = 0.05A,.

and stored. When the number of unknowns exceeds 131,000, we recalculate
the strong matrix in the sequential code when necessary. In the last two rows
of Table 6.6.1, we give the comparison of CPU time for one CG term when
the surface sizes are 32 x 32 and 64 x 642, respectively. The strong matrix is
recalculated in the sequential code. One can see that the speedup factor can
be up to 115.6 for 1 CG term. To complete the conjugate gradient solution
of sequential code will be prohibitive long. For diclectric surfaces, when the
number of unknowns exceeds 1.5 millions, the code on a single processor can-
not be run and therefore parallel computation is the only alternative. In the
1.5 million unknown example, the computer code requires about 78% of the
4.0 GBytes of RAM. We should emphasize that the CPU time comparisons
shown in Table 6.6.1 and 6.6.2 are based on the collocation method. For the
lossy dielectric surface, it is found that near-field integration is necessary.
Although this near-field integration requires additional CPU time, the re-
sulting matrix is better conditioned so that the number of CG terms may
be reduced. For examples, with near-field integration, the CPU time for the
8x8 and 16 x 162 surface with h = 0.05, reduces from 5,051 to 4,585 and
20,474 to 19,085 seconds, respectively. It is expected that similar speed-up
factors are obtained when replacing the collocation method with the near-
field integration. Table 6.6.3 shows the CPU time distribution for a 8 x 82
surface with near-field integration, where h = 0.05). The communication
time is only a small part of the total CPU time. Most of the CPU time is
spent on calculating the sparse matrix and sparse-matrix-vector multiplica-
tion. Communication time only attributes to 2.6% of the total CPU time
while that of the far interaction calculation based on FFT is 6.3%.

Table 6.6.4 shows the comparison of the computed brightness tempera-
ture versus surface size and rms height, and the comparison between the
results obtained with and without the near-field integration. The incident
angle for the 8 x 8A2 surfaces is 30° while that of the remaining ones is 50°.
The result of an infinite flat surface with the same permittivity is also given
for reference. It should be pointed out that the brightness temperatures of
the rough surfaces are obtained from one realization. Different realizations
--- PAGE 386 ---
364 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES
crinteneratey | (eit
108.45
109.92
8x8 112.64
(8, =30") 0.20 116.44 116.30
122.15 122.58
_— 129.64
0.10 86.51
(6,=50°) a
102.79 103.38
110.43
[om 3
exe 0.10 86.19
6,=30°, Temperature = 103.07 K; 6,= 0°, Temperature = 80.85 K
Table 6.6.4 Brightness temperatures of lossy dielectric rough surfaces. Incident angle is
30° for 8 x 8A2, 50° for 16 x 16 and 32 x 322 surface, ¢, = 45 + 130.
may give different results varying within about 4 K which is illustrated in
Table 6.6.5. From Table 6.6.4, it is observed that when h is small, the bright-
ness temperature resembles that of the flat surface provided that the surface
size is large enough, e.g., 16 x 16\?. The brightness temperature increases
with increasing h. The difference between the temperatures of the 16 x 16.3
and those of 32 x 32A? surfaces is less than 1 K for all the cases with dif-
ferent h considered. It implies that a surface with 16 x 16)? is sufficiently
large in numerical simulations at least in the cases considered. We also plot
the results in Fig. 6.6.4 to give a better illustration. From the comparison
between results obtained with and without the near-field integration, one
can see that the accuracy is improved after using the near-field integration.
The maximum improvement may be up to about 3 K. Table 6.6.5 shows the
ensemble average of the brightness temperature versus the number of real-
izations for surfaces of 16 x 1642. The difference among different realizations
is small, and the result converges within five realizations.
--- PAGE 387 ---
§6.4 Numerical Results 365
“Realization | Temperature of one realization (K) | _ Average temperature (K)
126.33 [ee
2 | 125.12 __ 125.725
123.49 124.980
124.86 124.950
123.04 124.568
Table 6.6.5 Ensemble average of brightness temperatures versus mmber of realizations.
Incident angle = 50°. The surface size is 16 x 16A2, h = 0.3Ao, €y = 45-+ 130.
gl” |
2 | © infiniteOd)
a
2 10- a
5 _—- wr —e3202
E 10 oe aa ae a 16x16
vs a
g >< infiniteGod)
2 | a m infiniteG0d) |
& x—-8x8
= a |
a
0 oa 02 03 o4
sms height (wavelengh)
Figure 6.6.4 Brightness temperatures of lossy dielectric rough surfaces with different rms
heights and sizes. Incident angle is 30° for 8 x 8A2 surface, 50° for 16 x 16 and 32 x 32X2
surface, ¢, = 45 + 130.
--- PAGE 388 ---
366 6 3.D WAVE SCATTERING FROM 2-D ROUGH SURFACES
REFERENCES AND ADDITIONAL READINGS

Adams, R. J. and G. S. Brown (1998), Use of fast multipole method with method of ordered
multipole interactions, Electronics Lett., 34(23), 2219 2220.

Arias-Gonzalez, J. R., M. Nieto-Vesperinas, and A. Madrazo (1999), Morphology-dependent
resonances in the scattering of electromagnetic waves from an object buried beneath a
plane or a random rough surface, J. Opi. Soc. Am. A, 16(12), 2928-2934.

Belszynski, E., M. Belszynski, and T. Jaroszewicz (1994), A fast integral-equation solver
for electromagnetic scattering problems, [MEE Ant. and Propagat. Soc. Int, Sym., 1,
416-419,

Brown, G. §.. Ed. (1998), Special issue on low grazing-angle backscattering from rough
surfaces, IEEE Trans. Antennas Propagat., 46.

Chan, C. H., L. Tsang, and Q. Li (1998), Monte-Carlo simulations of large-scale one-
dimensional random rough surface scattering at near grazing incidence: Penetrable case,
IEEE Trans. Antennas Propagat., 46(1), 142 149.

Chew, W. C. and Q. H. Lin, Eds. (2000). Special Issue on computational wave issues in
remote sensing, imaging and target identification, propagation and inverse scattering,
IEEE Trans. Geosci. Remote Sens., 38.

Chou, H. T. (2000), Extension of the forward-backward method using spectral acceleration for
the fast analysis of large array problems, [EE Proc. — Microw., Antennas, and Propag.,
147(3), 167-172.

Chou. H. ‘T. and J. 'T. Johnson (1998), A novel acceleration algorithm for the computation of
scattering from rough surfaces with the forward-backward method, Radio Sci., 33(5).
1277-1287.

Coifman, R., V. Rokhlin, and $. Wandzura (1993), The fast multipole method for the wave
equation: A pedestrian prescription, IEEE Ant. Propagat. Mag., 35(3), 7-12.

Frigo, M. and S. G, Johuson (1997), The Fastest Fourier Transform in the West, Cambridge,
MA. Available online at http: //www.fftw.org.

Greenbaum, A. (1997), Iterative Methods for Solving Linear Systems, SIAM Frontiers in
Applied Mathematics, vol. 17, SIAM, Philadephia.

Gropp, W., E. Lusk, and A. Skiellum (1994), Using MPI: Portable Parallel Programming
with the Message-Passing Interface, MIT Press. Cambridge, MA.

Harrington, R. F. (1961), Time-Harmonic Blectromagnetic Fields, McGraw-Uill, New York.

Harrington, R. F. (1968), Field Computation by Moment Mcthod, Macmillan, New York.

Holliday, D., L. L. DeRaad, Jr., and G. J. St-Cyr (1996), Forward-backward: A new method
for computing low-grazing angle scattering, IEEE Trans. Antennas Propagat., 44, 722-
729.

Holliday, D., L. L. DeRaad, Jr., and G. J. St-Cyr (1998), Forward-backward method for
scattering from imperfect conductors, IEEE Trans. Antennas Propagat., 46, 101-107.

Irisov, V. G. (1997), Small-slope expansion for thermal and reflected radiation from a rough
surface, Waves in Random Media, T(1), 1-10.

Jackson, T. J. (2001), Multiple resolution analysis of I-band brightness temperature for soil
moisture, IEEE Trans. Geosei. Remote Sens., 39(1), 151-164.

Janaswamy, R. (1994), A fast finite difference method for propagation predictions over irreg-
ular, inhomogeneous terrain, IEEE Trans. Antennas Propagat., AP-42, 1257--1267.
--- PAGE 389 ---
REFERENCES 367

Jandhyala, V., E. Michielssen, S. Balasubramaniam, and W, C, Chew (1998a), A combined
steepest descent-fast multipole algorithm for the fast analysis of three-dimensional scat-
tering by rough surfaces, IEEE Trans. Geosci. Remote Sens., 36(3), 738-748.

Jandhyala, V., B. Shanker, E. Michielssen, and W. C. Chew (1998b), A fast algorithm for
the analysis of scattering by dielectric rough surface, J. Opt. Soc. Am. A, 1877-1885.

Johnson, J. T. (1996), Applications of numerical models for rough surface scattering, Ph.D.
thesis, Massachusetts Institute of Technology.

Johnson, J. T. and H. T. Chou (1998), Numerical studies of low grazing angle backscatter
from 1-D and 2-D impedance surfaces, Proc. IGRASS 1998, Seattle WA, 2295-2297.

Johnson, J. T., R. T. Shin, J. C. Eidson, L. ‘Tsang, and J. A. Kong (1997), A method of
moments model for VIF propagation, IEEE Trans. Antennas Propagat., 45, 115-125.

Johnson, J. T., R. T. Shin, J. A. Kong, and L. Tsang (1999), A numerical study of ocean
polarimetric thermal emission, IEEE Trans. Geosci. Remote Sens., 37(1), 8-20.

Johnson, J. T., L. Tsang, R. Shin, K. Pak, C. H. Chan, A. Ishimarn, and Y. Kuga (1996),
Backscattering enhancement of electromagnetic waves from two-dimensional perfectly
conducting random rough surfaces: A comparison of Monte Carlo simulations with ex-
perimental data, IEEE Trans. Antennas Propagat., 44, 748-756.

Kapp, D. A. and G. S. Brown (1996), A new numerical method for rough surface scattering
calculations, IEEE Trans. Antennas Propagat., 44, 711-721.

Krause, K. C., S. H. Lou, L. Tsang, and ©. H. Chan (1991), Application of the finite clement
method to Monte Carlo simulations of random rough surface scattering with Neumann,
boundary conditions, Microwave Opt. Technol. Lett., 4(7), 255 258.

Kuga, Y., J. S. Colburn, and P. Phu (1993), Millimeter-wave scattering from one-dimensional
surface of different surface correlation functions, Waves in Random Media, 3, 101-110.

Kuga, Y. and P. Phu (1996), Experimental techniques in random media and rough surface,
Progress in Electromag. Res., PIER 14, Chapter 2, Elsevier Science Publishers, Cam-
bridge.

Li, Q. (2000), Numerical simulation of interactions of electromagnetic waves with lossy dielec-
tric surfaces using fast computational methods, Ph.D. thesis, University of Washington,
Seattle.

Li, Q., L. Tsang, K. §. Pak, and C. H, Chan (2000a), Bistatie scattering and emissivi-
ties of random rough diclectric lossy surfaces with the physics-based two-grid method
in conjunction with the sparse-matrix canonical grid method, IEEE Trans. Antennas
Propagat., 48(1), 1-11.

Li, S. Q., C. H. Chan, L. Tsang, and Q. Li (1999), Parallel implementation of the sparse-
matrix canonical grid method for two-dimensional lossy dielectric random rough surfaces
(3D scattering problems) on a Beowulf system, IEEE Ant. and Propagat. Soc. Int. Sym.,
1, 522-525.

Li, S. Q., C. H. Chan, L. Tsang, and Q. Li (2000b), Parallel implementation of the sparse-
matrix/canonical grid method for the analysis of two-dimensional random rough surfaces
(Three-dimensional scattering problem) on a Beowulf System, [EEE Trans. Geosci. Re-
mote Sens., 38, 1600-1608.

Li, 8. Q. C. H. Chan, and L. Tsang (2001), Multilevel expansion of the sparse-matrix canon-
ical grid method for two-dimensional random rough surfaces, IEEE Trans. Antennas
Propagat., in press.
--- PAGE 390 ---
368 6 3-D WAVE SCATTERING FROM 2-D ROUGH SURFACES

Lin, C.-M. and C. H. Chan (1998), Monte Carlo simulations for the electromagnetic scatter
ing of rough surfaces by the combined wavelet transform and banded-matrix iterative
approach/canonical grid method, Microwave Opt. Technol. Lett., 19(4), 274-279.

Liou, Y-A., K-S. Chen, K-S., and T.-D. Wu (2001), Reanalysis of L-band brightness pre-
dicted by the LSP/R model for prairie grassland: incorporation of rough surface scat-
tering, IEEE Trans. Geosci. Remote Sens., 39(1), 129-135.

Lou, S. H. (1991), Application of numerical methods to Monte Carlo simulations of scattering
of waves by random rough surfaces, Ph.D. thesis, University of Washington, Seattle.

Lou, 8. H., L. Tsang, C. H. Chan, and A, Ishimaru (1990), Monte Carlo simulations of
scattering waves by a random rough surfaces with the finite clement method and the
finite difference method, Microwave Opt. Technol. Lett., 3(5), 150-154.

Lon, S. H., L. Tsang, C. H. Chan, and A. Ishimaru (1991), Application of the finite element
method to Monte Carlo simulations of scattering of waves by random rough surface with
the periodic boundary conditions, J. Electromag. Waves and Appl., 5, 835-855.

Macaskill, C. and B. J. Kachoyan (1988), Numerical evaluation of the statistics of acoustic
scattering from a rough surface, J. Acous. Soc. Am. A, 84, 1825-1835.

Michielssen. E., A. Boag, and W. C. Chew (1996), Scattering from elongated objects: Di-
rect solution in O(N log2N) Operations, IEE Proc. Microwave Antennas Propagation,
143(4), 277-283.

Michielssen, E. and W. C. Chew (1996), Fast steepest descent path algorithm for analyzing
scattering from two-dimensional objects, Radio Sci., 31(5), 1215-1224.

Njoku, E. G. and L. Li (1999), Retrieval of land surface parameters using passive microwave
measurements at 6-18 GHz, IEEE Trans. Geosci. Remote Sens., 37(1), 79 93.

Ngo, H. D, and C. Rino (1994), Applications of beam simulation to scattering at low grazing
angles: Part 1. Methodology and validation, Radio Sci., 29(6), 1365-1379.

Pak, K. (1996), Studies of large-scale random rough surface scattering problems based on
Monte Carlo simulations with efficient computation integral equations methods, Ph.D.
thesis, University of Washington, Seattle.

Pak, K., L. ‘Tsang, and J. Johnson (1997), Numerical simulations and backscattering enhance-
ment of electromagnetic waves from two-dimensional dielectric random rough surfaces
with the sparse matrix canonical grid method, J. Opt. Soc. Am. A, 14(7), 1515 1529.

Peterson, A. F., S. L. Ray, and R. Mittra (1998), Computational Methods for Electromagnel-
ics, Oxford University Press, New York.

Rao, 8. M., D. R. Wilton, and A. W. Glisson (1982), Electromagnetic scattering by surfaces
of arbitrary shape, IEEE Trans. Antennas Propagat., 30(3), 409-418.

Rino, C. L. and H. D. Ngo (1994), Application of beam simulation to scattering at low grazing
angles. 2. Oceanlike surfaces, Radio Sci., 29(6), 1381-1391.

Rino, GC. L. and H. D. Ngo (1998), Numerical simulation of low-grazing angle ocean microwave
backscatter and its relation to sea spikes, IEEE Trans. Antennas Propagat., 46(1), 133-
M1.

Rokhlin, V. (1983), Rapid solution of integral equations of classic potential theory, J. of
Comp. Phys., 60, 187-207.

Rokhlin, V. (1990), Rapid solution of integral equations of scattering theory in two dimen-
sions, J. of Comp. Phys., 86, 414-439.

Sarabandi, K. and T. Chiu (1997), Electromagnetic scattering from slightly rough surfaces
with inhomogeneous dielectric profiles, IEEE Trans. Antennas Propagat., 45(9), 1419-
1430.
--- PAGE 391 ---
REFERENCES 369

Schneider, J. B. and S. L. Broschat (1995), The measured equation of invariance method
applied to randomly rough surfaces, Applied Computational Electromagnetics Society
Journal, 10(1), 19-30.

Sterling, T. L., J. Salmon, D. J. Becker, and D. F. Savarese (1999), How to Build a Be-
owulf, A Guide lo the Implementation and Application of PC Clusters, The MIT Press,
Cambridge, MA.

‘Torrungrueng. D., IL~T. Chou, J. T. Johnson (2000), A novel acceleration algorithm for the
computation of scattering from two-dimensional large-scale perfectly conducting random
rough surfaces with the forward-backward method, IEEE Trans. Geosci. Remote Sens.,
38(4), 1656-1668.

Tran, P. (1997), Calculation of the scattering of electromagnetic waves from a two-dimen-
sional perfectly conducting surface using the method of ordered multiple interaction,
Waves in Random Media, 7(3), 295-302.

Tran, P. and J. M. Elson (1998), Banded method of ordered waultiple interaction for the
scattering of electromagnetic waves from a rough surface, J. Opt. Soc. Am. A, 15(6),
1643-1646.

‘Tran, P. and A. A, Maradudin (1993), Scattering of a scalar beam from a two-dimensional
randomly rough hard wall: Dirichlet and Neumann boundary conditions, Appl. Optics,
32(15), 2848 2851.

Voronovich, A. G. (1994), Wave Scattering from Rough Surfaces, Springer-Verlag, Berlin.

Wagner, R. L., J. S. Song, and W. C. Chew (1997), Monte Carlo simulation of electromag-
netic scattering from two-dimeusional random rough surfaces, IEEE Trans. Antennas
Propagat., 45(2), 235-245.

Wang, J. J. HL. (1991), Generalized Moment Methods in Electromagnetics : Formulation and
Computer Solution of Integral Equations, Wiley-Interscience, New York, NY.

Wang, J. R., P. E. O'Neill, T. J. Jackson, and E. T. Engman (1983), Multi-frequency mea-
surements of the effects of soil moisture, soil texture and surface roughuess, [EEE Trans.
Geosci. Remote Sens., 21(1), 44-51.

Wang, J. R. and 'T. J. Schmugge (1980), An empirical model for the complex dielectric
permittivity of soils as a function of water content, IEEE Trans, Geosci. Remote Sens.,
18(4), 288 295.
--- PAGE 392 ---
Scattering of Electromagnetic Waves: Numerical Simulations,
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Hlectronic)

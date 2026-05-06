# Tsang《Scattering of EM Waves》Chapter 3

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 3
SCATTERING AND EMISSION
BY A PERIODIC ROUGH SURFACE
1 Dirichlet Boundary Conditions 62
1.1 Surface Integral Equation 62
1.2 Floquet’s Theorem and Bloch Condition 63
1.3 2-D Green’s Function in 1-D Lattice 64
14 _ Bistatic Scattering Coefficients 67
2 Dielectric Periodic Surface: T-Matrix Method 68
2.1 Formulation in Longitudinal Field Components 69
2.2 Surface Field Integral Equations and Coupled Matrix Equations 74
2.3 Emissivity and Comparison with Experiments 81
3 Scattering of Waves Obliquely Incident on Periodic
Rough Surfaces: Integral Equation Approach 85
3.1 Formulation 85
3.2 Polarimetric Brightness Temperatures 89
4 Ewald’s Method 93
4.1 Preliminaries 93
4.2 3-D Green’s Function in 3-D Lattices 98
4.3 3-D Green’s Function in 2-D Lattices 102
4.4 Numerical Results 105
References and Additional Readings 110
~61—
--- PAGE 85 ---
62 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The scattering of waves from a periodic surface has been studied exten-
sively. Two methods of solution wil! be used in this chapter: (1) the method
of moments based on periodic Green's function and (2) the T-matrix method.
In Section 1, the problem of a one-dimensional periodic rough surface with
Dirichlet boundary condition is illustrated. In Section 2, we consider the
case of vector electromagnetic wave obliquely incident on a one-dimensional
periodic rough surface. The incident direction is also at a nonzero azimuthal
angle with respect to the periodic direction. This problem has applications
in polarimetric passive remote sensing of rough surfaces because the third
and fourth Stokes parameters are nonzero. The components of the electric
and magnetic fields along the row direction are used as unknown scalar func-
tions to reduce the vector nature of the problem to a scalar one. Then, the
extended boundary condition (EBC) approach with Fourier series expansion
for the surface fields is used to obtain the matrix equations governing the
scattered field amplitudes. In Section 3, we study the vector electromagnetic
case using integral equation method. In Sections 1 and 3, the periodic surface
is one-dimensional, and the Green’s function is two-dimensional. A method
of speeding up the computation of 2-D Green’s function in 1-D lattice is pre-
sented. In Section 4, we describe Ewald’s method of computing 3-D Green’s
function in 3-D lattice and 2-D lattice. Besides rough surfaces, periodic
structure problems are studied extensively in frequency selective surfaces
[Chan, 1995; Munk, 2000] and photonic bandgap materials [Yablonovich,
1987; Joannopoulos et al. 1995).
1 Dirichlet Boundary Conditions
1.1 Surface Integral Equation
Consider a. plane wave incident upon a periodic surface with height function
z= f(x), such that f(e+P) = f(x). The period of the rough surface is P in
the &-direction. The incident direction is in the 2-2 plane. The electric field
of the incident wave is given by
EF, =5eh" (3.1.1)
where k; denotes the incident wave vector and is given by @kiz — 2kiz with
kig = ksin 6; and kj, = k cos@;. We have 7 = ¢x + 2z. The electric field Ey
satisfies the two-dimensional wave equation
2 2
Ga + =) Ey +B, =0 (3.1.2)
--- PAGE 86 ---
§1.2 Ploquet’s Theorem and Bloch Condition 63
The Green’s function is
er) —t HO alee) <2 [ ae, 2 exp like(2 — 2’) + ik
GFF) = gto (klF-F|) = rs [. dkz, mee [ihe (@ — a!) + ik, |z — 2'|]
(3.1.3)
where kz = (k? —k2)'/?, Making use of Green’s function of region 0, we have
20
Eq(F) — | do! [ORF )A- V' By) — Bylr)Aa- Var}
90
_JE,(F) z> fla) :
= {5 z<fz) 14)
and
aa ls FO) 5
da’ = : 8 da! (3.1.5)
For Dirichlet boundary conditions Ey = 0 on the surface, the integral
equation in (3.1.4) becomes
oo
Byi(a.2 = f(2)) = fda! G(x, f(a)sa!, f(a) VEY) ogee (81.5)
00
Let the unknown surface variable be denoted by u(x) so that
a)dx = (doh: VE,(F 3.1.
u(e)de = (don ¥ W)) (3.1.7)
Equation (3.1.6) becomes
20
etre ikis S(t) — | dr'G(a, f(x); 2", f(2’))u(2’) (3.1.8)
1.2 Floquet’s Theorem and Bloch Condition
‘The left-hand side of (3.1.8) has the following translational property
gibie(@=nP)~ikief(e+nP) _ gikienP pikize—iki. f(x) (3.1.9)
Letting a be replaced by x + nP in (3.1.8) and using (3.1.9), we have also
a! a! +nP.
20
cikianP gikset—ike. f(t) — | de! Ga + nP, f (x):2! + nP, f(a")u(a! + nP)
—00
= | de'G(a, f(x); 2’, f(x))u(e! + nP)
~ poo
= cikianP | dx'Gle, f(a);«!, f(a!)Ju(a’) (3.1.10)
J-s0
--- PAGE 87 ---
64 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The second equality in (3.1.10) is a result of translational invariant property
of G. Thus we have
u(a’ + nP) = e*"Pu(e’) (3.1.11)
Equation (3.1.11) is known as the Floquet’s theorem and is generally true
for periodic structures. Thus one write
u(x) = e*="w(x) (3.1.12)
where w(x) is a periodic function with period P. From (3.1.12), we have the
Bloch condition
u(x + P) = cP u(x) (3.1.13)
The surface integral in (3.1.8) is over infinite domain. However, it can
be condensed into a single period. Let the center period be from —P/2 to
P/2. Thus, using (3.1.8), for —P/2 <x < P/2 we have
cikver—iks. f(a)
20H P/2+mP
= 1 | dx'G(x, f(x); 2', f(x’))u(e’)
mors 1 ~P/2+mP.
P/2 oo 5
= [ dx! S> G(x. fa);2! + mP, fle’)? ule’) (3.1.14)
—P/2 m=—00
The second equality in (3.1.14) is a result of changing dummy variables of
integration from 2x’ to x’ + mP and using Floquet’s theorem for u(x).
1.3 2-D Green’s Function in 1-D Lattice
From (3.1.14), one can define the periodic Green’s function
0
G,(a, 42',2') = Ss Ge, 2;2' + mP, 2/)eibemP (3.1.15)
m=-00
Thus for —P/2 <a < P/2 the integral equation of (3.1.14) becomes
; Pp
eibect—ikecf (0) = / da! G(x, f(x):2!, f("))u(2") (3.1.16)
=P/2
Thus the advantage of (3.1.16) is that the integral equation is reduced to
matching the left- and right-hand sides over only one period of the periodic
medium instead of over an infinite domain. However, instead of the free space
Green’s function G, we have to compute the periodic Green’s function G,
which is an infinite series as represented by (3.1.15).
--- PAGE 88 ---
§1.3 2-D Green’s Function in 1-D Lattice 65
From (3.1.3) and (3.1.15) we obtain
- 2
Gpla, 232.2) = j So chem? HY (ke — a — mPP + (2 2)
m=—00
(3.1.17)
Equation (3.1.17) is the periodic Green’s function in spatial domain. As
m — oo, the terms inside the summation decay as 1/m. One can express the
result in the spectral domain by making use of the spectral representation
of the free space Green’s function
Gp(x, 232" nat > [tee iky(2—a!—mP)+ik: 1) oikismP
ip(a,25a',2!) = 2 pkey. exp(ik,(x—2'—mP)+ikz|2—2'|)e'
m=—00
(3.1.18)
We next make use of the property of Fourier series that
y> clamp FS ( a") 3.1.19)
e€ => a =>" wd.
en PE Le
where 6 is Dirac delta function. Equation (3.1.19) simply states that a pe-
riodic train of impulses with period 27/P can be represented by a Fourier
series with the Fourier coefficient equal to P/27. Substituting (3.1.19) in
(3.1.18) gives the periodic Green’s function in the spectral domain.
0
Gp(x, 2:2", 2/) = sp > i exp(ikem(x — 2’) + ikem|2 — 2'|) (3.1.20)
m=—o0
where kom = Kig + 2mm/P and kim = (k? — k2,,)'/?. For kum < k, we have
propagating Floquet modes. For kr, > k, kz becomes imaginary giving rise
to evanescent Floquet modes. The spectral form of (3.1.20) does converge
rapidly for large values of |z—2z’| due to exponential decay, but we often need
to evaluate this function for small or zero values of |z — z'| in which case the
summation is slowly convergent. Here, we present a general transformation to
speed up the convergence of summation that is due to Veysoglu et al. [1991].
We start from the expansion
x
7 = em Seite (3.1.21)
m=1
Multiply both sides by q(v) and integrate from 0 to oo. This gives
es mo q(v)
doe Q(m) = ef a (3.1.22)
mah ° ove
where
--- PAGE 89 ---
66 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
oo
Q(m) -[ dy qv) (3.1.23)
0
is the Laplace transform of q(v).
Next, we make use of the following Laplace transform integral using
Bessel function of order 1/2 [Oberhettinger and Badii, 1973}.
- ; i2 cos (a(y? — 2iy)!/?)
; Hf ( 2 2 ve) --2/ dy env t t 3.1.24
eae te) why “YS (y? — 2iy)V/? ( )
Let
s =—k(x — 2! —mP) (3.1.25)
a=k(z-2') (3.1.26)
in (3.1.24), This gives
oth? HD (kV /(e— a! —mP PP + (2 — 2)
m 0 (y? — 2iy)'/?
(3.1.27)
Changing dummy integration variable from y to v = kPy gives
eth? HOE (a — 2! —mP)? + (z— 2)?)
ogy \ V2
wD a ces weet ati 18)")
_ dven™ |— nike 2) g(e=2")o/ P
0 akP ( uy? = By?
PP? — kP
(3.1.28)
Comparing (3.1.28) with (3.1.23) shows that the left-hand side of (3.1.28)
is Q(m) while g(v) is the square bracket on the right-hand side of (3.1.28).
Use Q(m) and q(v) from (3.1.28) and substitute into (3.1.22). We also let
t= (Kir +h)P (3.1.29)
These give
co
So heh HY (ke = a — PP + 2)
m=1
2 »\ 1/2
oo % _, con (a (sips ~ 28) )
— git dv _ enik(a—2') (a—a')u/P
Jo ev—elt | ckP (gp - Biv y 1?
EP — RP
(3.1.30)
--- PAGE 90 ---
§14 Bistatic Scattering Coefficients 67
‘Transforming dummy variable from v to u? = v/(kP) gives
aa)
Gyla, 232',2!) = 5 SO clk? HY (ke = a! = mPP? + (2 —2/P)
m1
cil kio + k)P p—ik(2—2")
= x
w
oo LW kP+K a2? cog (k(x — 2Julu2 ~ 2%) 2
x L608 (2 = 2')ulu? = 26)77) (3.1.31)
0 1 — ce tkP a i(k FE) (u2 — 21/2
This integral is rapidly convergent due to exponential decay and can casily be
evaluated by using Romberg integration. Having the formula for the periodic
Green’s function, one can use the method of moments to solve (3.1.16) for
the unknown surface variable by matching over one period of rough surface
-P/2<a < P/2
1.4 Bistatic Scattering Coefficients
Once the surface field u(x) is calculated, the scattered field for z > f(x) is,
on using (3.1.4) and (3.1.6)-(3.1.8),
2°
EY) = -| da! G(x, 2:0", f(x’))u(e') (3.1.32)
—00
‘The integral in (3.1.32) can again be condensed into one period
P/2
E,(r) = -|[ dr! Gy(a, 2,2, f(x))u(a’) (3.1.33)
-P/2
We use (3.1.20) in (3.1.33) to get
oe
Bs7) = So theme? Bry (3.1.34)
m=—00
where
i PPP ig them fl2")y (ol
Bn = - ap | da! ee Bam FE ag! 3.1.35
=~ ape | on ) (3.1.35)
Note that only propagating Floquet modes carry time-averaged radiation
power. The incident power on the rough surface over a period P is Pw/2y,
where w is the width in the §-direction. The time-averaged power contained
in scattered wave is equal to —E}/(2iwj) (QEy" /Iz) Pw. Thus the fractional
power is
ake
Pn = |BmP (3.1.36)
--- PAGE 91 ---
68 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
for the mth propagating Floquet mode. Conservation of energy requires
> Pm =1 (3.1.37)
m=propagat.
modes
For the case of large P with P much bigger than wavelength, the propagating
Floquet modes can approximate a continuum of scattered angles. Let
2am :
Kam = hie + > = ksin 0, (3.1.38)
represent the transformation between k,,,, m, and scattered angle 6,. Thus
27am
Akom = —S— 1.39
m= (3.1.39)
Since Am = 1,
P P pre
So Am() = 5= | dhtem() = = dk cos 0, () (3.1.40)
Qn Qn Jon/2
m
where ( ) stands for a mathematical expression. Such transformation between
discrete and continuum as represented in (3.1.40) is customarily done in solid
state physics when a periodic boundary condition is applied to truncate the
domain to a finite size. Thus
P opr ok,
P= [ dB. 6089, |B (3.1.41)
rm Qn Jin k
If we let
om [2
Pa = | d0,0 (0s) (3.1.42)
m cam /2
where o(9,) is the bistatic scattering coellicient, we have
Pk
o(0s) = 5 cos” 43 |Byn|” (3.1.43)
TT
for the propagating mth Floquet mode (i.e., |kiz2m| < ). Equation (3.1.43)
expresses the bistatic scattering coefficient in terms of Floquet mode ampli-
tudes.
2 Dielectric Periodic Surface: T-Matrix Method
In this section the scattering of electromagnetic waves from dielectric peri-
odic rough surface is studied. We consider the case of oblique incidence and
also at an arbitrary azimuthal angle with respect to the row direction. In
the formulation, the components of the clectric and magnetic fields along the
--- PAGE 92 ---
§2.1 Formulation in Longitudinal Field Components 69
Region 0 1. €
NS 2
y
NS |
i P
Region 1 p, €

Figure 3.2.1 Geometrical configuration of the problem.
row direction are used as unknown scalar functions to reduce the vector na-
ture of the problem to a scalar one. The rough surface is invariant along the
row direction. Then, the extended boundary condition (EBC) approach with
Fourier series expansion for the surface fields is used to obtain the matrix
equations governing the scattered field amplitudes. In general, the E-waves,
which are characterized by the components of the electric fields along the row
direction, and the H-waves, which are characterized by the components of
the magnetic fields along the row direction, are coupled together. Results are
illustrated with sinusoidal profiles. The scattered power calculated is shown
to satisfy reciprocity and energy conservation. The emissivity of a periodic
rough surface is calculated from one minus the reflectivity. We also show
good comparison with experimental data.
2.1 Formulation in Longitudinal Field Components
Consider a plane wave incident upon a periodic surface described by f(x) =
f(a +P), with P denoting the period of the surface in the @-direction
(Fig. 3.2.1). The electric field of the incident wave is given by

E, = @Bne™* (3.2.1)
where k; denotes the incident wave vector and is equal to &kin + jkiy — 2kiz
and @; is the polarization of the electric field vector.

Since the structure is uniform in the g-direction, all the field components
in both region 0 and region 1 will have the same exp(ikiyy) dependence.
With this dependence, we can replace 0/Oy in Maxwell’s equation by ikiy.
It is possible to express all field components transverse to 7 in terms of
longitudinal field components in the #-direction. Unless otherwise specified,
we will suppress the exp(ikiyy) dependence.
--- PAGE 93 ---
70 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
In terms of the longitudinal components, the transverse components are
= i =
Bye) = te [keh lh) +en¥ «Hi 220)
jy
— i _ =
Hye(?) = gape [bv Voie P) — wesVs x Eyy(r)] (8.2.26)
jy
where j = 0,1 signify regions 0 and 1, respectively, Vs is the transverse
gradient operator that is transverse to j-direction
0 a)
Ve=25>+22- 3.2.
a= * 9, + #9, (3.2.3)
and Ej; and Hys denote the transverse components of the clectric and mag-
netic fields for region j. The subscript 7 = 0 is suppressed. The E-waves are
described by Hjy = 0 and H-waves are described by Ejy = 0. The longitudi-
nal components Ej, and Hj, satisfy the equations
(V2 + kj — kz) Ey =0 3.2.4)
STN Si) | Hy f (3.2.
We let
Dy = ba + 22 (3.2.5)
be the position vector that is transverse to the j-direction. Since Hj, and
Hj, satisfy a two-dimensional wave equation, we shall use a two-dimensional
Green’s function. The Green’s function is
— ta - 4 .
(4.0) = SH)” (kis |B. ~ P4)) (3.2.6)
where j = 0,1 and
12 <
keys = (Aj — kR,) (3.2.7)
Note that the Green’s function is similar to (3.1.3), except that k has been
replaced by kjs of (3.2.7). Integral equation can be formed by applying ex-
tinction theorem to Ey and Hy, separately. We also make use of Floquet’s
theorem to condense the integral equation for one period using a procedure
similar to that in Section 1. We have
E(B.) ~ | da’ {Gr(P Fe) A VyEy(B.) ~ EP.) VG PPP}
Jp
_ J Fy.) => Fle) (3.2.82)
0 2< fle) (3.2.8b)
--- PAGE 94 ---
§2.1 Formulation in Longitudinal Field Components 7
where the integration do’ is over one period P, and similarly
Hy(B.) ~ fda! {Gel VHP.) ~ Hy(P.)A- V.Ge(PusP.)}
_ fp.) 2> Fe) (3.2.94)
~ 10 z< f(x) (3.2.90)
where
 — ls, F@) :
do! = [: 8S | da! (3.2.10)
and
- vy ai yp tl oo) ah |e ol 2 4
Gp(D,, 7.) = WP > kan expliken(x — 2') + iken|z — 2'|] (3.2.11)
is the periodic Green’s function of region 0. In (3.2.11)
ken = hig + sa = han (3.2.12)
Keen = R23 — Kin = 9) B? — ky — by = BesiBn (3.2.13)
Making use of periodic Green's function of region 1, we have
[42 {Gir PsP) A: VB ag) ~ Big Fe) VCP Po}
_ fo 2> f(x) (3.2.14a)
= Biy(B) 2 < Fla) (3.2.14b)
[ to! {Grr(..06) AV. Hig Oe) — HiylD,) A VC ePP)
JP
_ fo z> f(x) (3.2.15a)
© | AiO) 2 < f(x) (3.2.15b)
where
ayo! 1 tka (a —a!) +i. 2 3 5
CrP PoP) = 5p u ba expliken(e — 2’) tikien|z—2'|] (3.2.16)
is the periodic Green’s function of medium 1, and
Bian = (KE — hy — REy)'? = (Rh, — Bin)'/? = kasi, (3.2.17a)
kan = hie + ma = hysal, (3.2.17)
--- PAGE 95 ---
72 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
k,
ky
= -\ ky
X((/ AS ‘
aa
—k
LAAN
Figure 3.2.2 Conical diffraction of the reflected wave in region 0.
We see that the waves are propagating in discrete Floquet modes forming
a cone shape when the observation point is either above the highest point
or below the lowest point of the surface (Fig. 3.2.2).
Let fmar and fmin be respectively the maximum and minimum values
of the surface profile f(x), Then
FB.
Ey, (ps) = EyilD, bn > . 3.2.18:
(Ps) = Byi(Bs) + s bn ae > Sma (3.2.18)
clk PB
0 = Eyi(p,) — i < n 3.2.186
vil.) Lm Ti Sani (3.2.188)
py cin Pe
Hy(P,) = Hyi(P,) + > oe fara 2>fmar  (3.2.19a)
" On,
(pe) ral etka
0 = Ay(p,) — So a ox < fm (3.2.19)
yt 7 n 5, hn min
where
Be = hep + Fk (3.2.20)
--- PAGE 96 ---
§2.1 Formulation in Longitudinal Field Components 73
denote the propagation vectors of Floquet modes. We recognize that b, and
of ) are scattered field amplitudes. The coefficients an, bn, al?) and a ) are
related to the surface fields by the following integrals,
+. c+
1 pferrPle) yay op OTe P(@)
n= sep [do {SE Al VB (Ay) — Eyl) A! Ve
(3.2.21)
and of is the same expression as b, with Ey replaced by Hy.
-1 fern PR@) cp op Othe BEY
On = TEP [ do Tk fl - VL Ey (,) — Ey(Bs) 2 Vee
(3.2.22)
and af?) is the same expression as a, with Ey replaced by Hy. In (3.2.21)
and (3.2.22)

D(x") = tu + 2f(e') (3.2.23)
is a point on the periodic surface. Similarly, making use of (3.2.14) and
(3.2.15), we obtain

etki Be .
0= LB ae 2> faz (3.2.24a)
7 Pa
y eikin Be (
E,y(.) = >) An—— 2 <i 3.2.24b)
y\Ps 2 Vi min
rt
h) Ekin Ba aor
o=->> Bi TE 2> fmax (3.2.25a)
7m
che? ,
Aiy(p,) = >- AY Te 7s imin (3.2.25)
7 Pr
where
1 en BAe)
Boe f dg (er Ov VE

"= Seep | { Ta Vain)

en BAe)
~ Eyl) V5 ————} (3.2.26)

Bi) is the same expression as B,, with Fj, replaced by Hi,
--- PAGE 97 ---
74 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
"Dik P Jp” VR es
Cin Ba’)
— Ey,(9,) a! - Vi, — (3.2.27)
Vio,
A is the same expression as A, with Ey, replaced by Hy,, and
zt +
kin = fkien + Zhen (3.2.28)
are the propagation vectors of the Floquet modes in region 1. By using
(3.2.18) and (3.2.19b), we can readily solve for a, and aS” in terms of
incident wave amplitudes.
an = dno VV 30 Eo (6: >) (3.2.29)
Hot on
a) = b9/3o on (ki x @:-9) (3.2.30)
Also, from (3.2.24) and (3.2.25) we obtain
B, = BY =0. for all n (3.2.31)
Given a, a, Br, and Bw in (3.2.29) (3.2.31), we next formulate matrix
equations to solve for the surface fields. After the surface fields are solved,
then the scattered ficld amplitudes b,,, bf, Ay, and AS” can be obtained
using (3.2.21) and (3.2.27).
2.2 Surface Field Integral Equations and Coupled Matrix Equa-
tions
The surface integral equations are, from (3.2.22), (3.2.29), (3.2.30), and
(3.2.26),
an = dno V/ GoBo(6: * G)
-] da! otk, BAe") al VIE (GL
= aap |, 7) RNs 'y(Ps)
B(p) i Vy 3.2.32
—E,(p,) 0 ° Tie (3.2.32a)
--- PAGE 98 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 75
. 1 nr
all) = bn0V/Bo— (Ie: x + 9)
wy
-1 a ff ik Ba) VHA
~ a Jot | yay
H, (pi) WV" one) 3.2.32b)
_ py) + —S—S—— ye da
y\Ps + Tha (
1 , enh B,(2’) a ,
By, =0= —— | d ———— _ i’ - VF, (Pp
eB)
1 (atv et ot
— Ey, (pi) a anya (3.2.32c)
Pr
1 sf niki, Bala’)
BY =0= —— | do! §-—__—_ a. Vi, (7h,
t 2ik.P Jp” va". 1y(Ps)
oF Ble’)
~ Hi, (7) a - Va (3.2.32d)
On
However, in the four equations of (3.2.32a)-(3.2.32d), there are eight un-
knowns Ey, Hy, 2-VsEy, %- VsHy, Ey, Hy, 2-VsE1y, and t-VsHiy. We
need to impose four boundary conditions to obtain a total of eight equations
for the eight unknowns.
Applying the boundary conditions for the tangential electromagnetic
fields on the periodic surface S, we have
Ey = Evy (3.2.32)
Hy = Hy (3.2.336)
AX Es =x Bs (3.2.33c)
Ax H,=AaAx hs (3.2.33d)
where E,, Hs, E,, and Hy, are related to By, Hy, Eiy, and Hyy by (3.2.2).
Equations (3.2.33a) and (3.2.33b) relate the four unknowns. Next we need
to put (3.2.33c) and (3.2.33d) as conditions on the eight unknowns,
From # x Bs = x F4,, (3.2.2) and (3.2.26),
Kiy . , WH. = kiy . win. za
ra x VsEy + ee x (Vs x Hy) = R" x VsBty + u" x (Vs x Aly)
(3.2.34)
--- PAGE 99 ---
76 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
Note that
x (V, x Ay) =: Va dy (3.2.35)
where Ay = 9A,(p,). Thus,
Kk
yx V7, Bye (iV Hy) = [higix Vo Bay weer j(A-VeHy)| (3.2.36)
is
From (3.2.33a) and (3.2.33) we have two relations
E,|v,z = f(«)| = Eyle,2 = f(2)] (3.2.37a)
Ay{x,2 = f(x)] = Aiy|x,2 = f(x)] (3.2.376)
Note that the surface fields (with z = f(x)) Ey, Hy, E1y, and Hyy are
functions of x only. If we take total derivative of (3.2.37a) with respect to x,
we have
dE, OE, , OE, df(z) _ OFty , OEtydf(x) _ dFy
de Oc * dz de Oc | dz dz de (3.2.38)
with 2 = f(x). Since
._[ df... df\?| *
s-[-de44 f(D
we get
2177 7, 0
axe, = li+ (4 Ofy , af OBy
" dx Ox dx Oz |, 42)
dg\?| * dEy
=|1 = —_ 3.2.39
+ (4) dx (3.2.39)
From (3.2.38) and (3.2.39), it follows that
ix VeBy =x VsEly (3.2.40a)
a GHy — diliy
Similarly, Tp da 8° that
AX VaHy = x Valy (3.2400)
Putting (3.2.40a) and (3.2.40) in (3.2.36), we have
U(@- VsHy) = —don x VsE1y + doi(ti- VsHiy) (3.2.41)
where
ke ky
do = [# _ 7 Kay (3.2.42a)
Ki, | wy
al ke .
= (3.2.42b)
--- PAGE 100 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 7
Equation (3.2.41) is a result of applying ? x E, =n x Ej,. If we apply the
same procedure to? x Hy =n X His, we get
H(i Vs Ey) = cof x Vs Hay + co9(- VE ty) (3.2.43)
where
ke k,
co = le - i oe (3.2.44a)
ek?
2 = 3.2.44b
a= E, (3. b)
Using (3.2.39) and the like in (3.2.41) and (3.2.43), we get respectively
do ue
ft: (V Hy) = Trap +do(i-VsAiy) — (3.2.45a)
1 a
+ (Z)
diy
os
fee (Vshy) = a + c(i: VsE ly) (3.2.45b)
i4(2
dx.
Equations (3.2.37a), (3.2.37b), (3.2.45a), and (3.2.45) provide the four re-
lations for the eight surface fields Ey, Hy, Evy, Hiy, 1» Vsby, V+ VsHy,
h-VsEiy, and ni» VsHiy. The integral equations (3.2.32a-d) provide the
additional four integral equations.
Surface Field Expansion
As indicated in Section 2.1, the surface fields obey Floquet’s theorem; that
is, (a) = exp(ikizr)w(x), where w(x) is a periodic function with period P.
Thus one can expand w(x) in a Fourier series. We use such expansion for
the surface field components as follows. With p,(%) = #x + 2f(z), let
. _ on , A
Ey |p,(e)| = Exylp,(x)] = > 2a% exp [hi + in'5] (3.2.46a)
2
doit VsEvy[P,(2)] = tkisde S~ 23% exp it + ine] (3.2.46b)
n
7 1 ; . 2 .
H,[p.(0)| = Haylpg()} = D> 298 exp [tie + in} (3.2.46¢)
”
--- PAGE 101 ---
78 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
n a . <8 . _ 20
dot VsHiylq(x)] = ikiede Y> 253 exp thine + in551| (3.2.46d)
n
From (3.2.45a), (3.2.45b), and (3.2.46a-d),
— 2
don: VsHy = dey [-ar2asi ( + ar) + dei.26
n
Qn
x exp [tae + in| (3.2.46e)
= 27 .
doit V.By = de > [oor (be + 7 + ail. 24)
7
. 2a 7 .
x exp [thier + inge (3.2.46f)
Thus all cight surface field components are now expressed in terms of four
sets of unknown coefficients af, 3%. 78, and 6%. Substitute the surface field
expressions of (3.2.46a d) in the two surface integral equations of (3.2.32c)
eto se
and (3.2.32d). Define Qp,, Qu, as the Dirichlet and Neumann matrices with
clements
ot
[2]
mn
-1 Fin Bala) : On
= _- [oe exp ikigt + ine
a | inexp | —i(m — n) a — ikig +6) f(a) (3.2.47)
=> | deexp|-i(m—-n)>2-i f x 3.2.4
PV, Pp xP P URLs m
sot
[2s]
mn
1 ien-V e-in Bal2) een int
= mp [or oe oP i int + ina]
-1+a',a), [ . Qn, _
= xp | —i(m — n)—x — ik 5 x 3.2.47b
La, VHP pdPep i(m — n) ptt isftG,)f(x)| 7b)
where the integrations are performed over one period. We obtain the two
matrix equations
st as =t =
—Qp, 8 -Qy, -@=B=0 (3.2.48a)
= is st —
Gp, 3° - Oy, 7 =B” =0 (3.2480)
In deriving the second equality in (3.2.47b), we have performed an inte-
--- PAGE 102 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 79
gration by parts. Here the vectors B, BY, a*, 3°, 7, and 6° contain the
elements B,,, Bo, as, 68, yn, 68, respectively. Similarly, substituting the
surface field expressions of (3.2.46a—d) in the surface integral equations of
(3.2.32a) and (3.2.326), we get the equations in the following matrix forms
= kiss- oe =
T= COQny V+ eZ Qn, ‘B+Qn,% (3.2.48¢)
= kigz- zs ee .
A) = ~doQiys O° + "0 ip, 8 +Qy, 7% (3.2-48d)
‘8
where @ and a") are the column vectors containing the known coefficients a,
and a!" respectively, while Qj, denotes the hybrid matrix which couples
a and 7 to @ and a"), and
[2 | = [ deexp |—i(m — n) ee ~ tke(£Gn)f(0)| (3.249)
=— -i(m—n)= 2-1 x 3.2.46
Ps) an Pf Be fp OPO? pe NSP
+t —l+aman - Qi .
(2x, mm TBnVinP [dro [itm - npr - ik) (2)
(3.2.49b)
ct a
[Qian] =-On, [2p,| (3.2.50)
mn mn
Equations (3.2.48a-d) can be put into the following matrix equation.
= kis=- = as _
Qn, FQ, COQny1 0 ° e
's
= = kys=- ci ath)
=doQhyi 0 Qn, a7-Qo, = (3.2.51)
=t+ = . As
Ons @p, 0 0 . 8
0 0 @y, Gp, LS 0
The unknown vectors @*, 8”, 7°, and d° for the surface ficld expansions are
obtained by solving the above matrix equation. After the coefficients @, 2,
7, and 5° are solved, the upward-going field amplitudes of (3.2.18a) and
(3.2.19a) by using (3.2.21) for b,, and the like for bi”
_ = _ hist as sete. .
B= COQ ny -T — a @n, ‘B-Qy,:-® — (3.2.52a)
<(h) StL, kisst x8 tO,
5” = MQiyi  B — oF On, “0 -Qy, 7" (3.2.52b)
‘8
and the dowuward-going field amplitudes of (3.2.24b) and (3.2.25) by using
--- PAGE 103 ---
80 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
(3.2.27) for A, and the like for A”) are
A=Op, +O, (3.2.53a)

sth) = we SL .

A” =p, 3° +n, 79 (3.2.53)
From the matrix equations we see that the E- and H-waves are generally
coupled. An incident wave of E-type (a) = 0) will be diffracted from the
dielectric periodic surface into waves that have both E-wave and H-wave
components. Both types of wave will coexist to satisfy the boundary con-
ditions. When the incident wave vector is in the z-z plane (kjy = 0), then
9 = dy = 0 and we can easily see that the scattered waves arising from E yi
are decoupled from those arising from Hy.

We next apply to the case when the surface is a sinusoidal function

Qe
F(x) = ~heos(=*) (3.2.54)
st
The Q matrices can be calculated by carrying out the integrations in
(3.2.47), (3.2.49), and (3.2.50), and expressed in terms of Bessel functions.
= -1
= (Ei) iin ny (eo 3.2.55
[2], = CED inn al Bn) (3.2.55a)
Fal 1+ Om). |m—n|
N =" (ti Iim—n| (ksh, 3.2.55b)
[Oe an = aa EO in tn) (82.558)
at re ot
[>]... = van "in nj (Rishi) (3.2.55¢)
+ 14 hn  . \im—
ye) = (£1) inn (sh, 3.2.55d
[Orbe = Ee ae HY manish) (8.2554)
at ay -\\m— A aor
[Gnu]... = eC ni BaP) (3.2.55e)
where Jjm—n| denotes the Bessel function of order |m —n|.

The T-matrix approach, which makes use of Green’s theorem to derive
the extended boundary conditions, is exact. However, the matrices used may
become ill-conditioned when the surface corrugation is deep or when the
corrugation depth divided by the period is large. This limits the applicable
regime of this method. The reason for ill-conditioning is that entire basis
functions rather than subscctional basis functions are used in surface field
expansions. In Section 3 we shall apply subsectional basis functions to this
problem which can handle surfaces with deeper corrugations.
--- PAGE 104 ---
§2.3 Emissivity and Comparison with Experiments 81
2.3. Emissivity and Comparison with Experiments
In this section a sinusoidal surface is used to model a row-structured plowed
field, and the theoretical results of emissivity are illustrated and compared
with the experimental data obtained from field measurements.
‘The reflected power P, for one period is
1 pe ae
P= nah Rel(E, x H*) - 3] de (3.2.56)
2P Jy
and incident power is
1 ofP oo _ .
Prne= 3p [ Rel(Eine<Fne)(~a] de (8.257)
2P Jo
For the reflected E-modes, by using (3.2.2) and (3.2.18a) for z > fmar. we
get.
—kiykon/ ke
_ bp cts iyRan/ ks
E, = >) etn 1 (3.2.58)
7 Vin —kiyken/ ke
ken /k2
_ wen gts ‘an/ ks
en (3.2.59)
mw VPn Keon /K2
By substituting (3.2.58) and (3.2.59) into (3.2.56) and integrating, the Flo-
quet modes are orthogonal and for the E-modes we have
P, => bent al” (3.2.60)
re eT mo
Similarly, the reflected power for the H-modes can be obtained. The total
reflected power is
. h)i2
1 when (lal? (be? } .
P= = Re—= [ e—— + pd) = Pr 3.2.61
’ 2 Te Tat TY Taal > " (8.261)
where Pf can be interpreted as the reflected power for the nth Floquet mode.
When the mode is evanescent, kz, is purely imaginary. The power Pl = 0
for the evanescent mode. The incident power is
lwe Lk th) yp °
Pine = 5 5 (Iaol? + Zia?) (3.2.62)
Thus, the reflectivity for a wave with horizontal or vertical polarization is
1 (Pol? + ba
Ta=>-) P= a (3.2.63)
“Pine x . » {aol + nal 2

=== RESTART FROM PAGE 104 ===
Progress: 120/723
Progress: 140/723
Progress: 160/723
--- PAGE 105 ---
82 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
where a = v, h incident polarization. The summation in (3.2.63) is over the
propagating modes and ap and al are obtained from (3.2.29) and (3.2.30),
by setting
a= 4; (3.2.64)
The transmitted power per period of the nth mode passing through the
surface defined by z = Zmin is
1 wk, |A,/? AM 2 1
Pta RO Men (Ane AY catia en temin 3.2.65
mR a a 289)
for all modes, where kyz,, = k)4{},, and Im[k1zn] > 0 should be used. When
medium 1 is lossless, we have (letting m = \/#1/€1)
we
Ph = SO (An? + lm A/?) (3.2.66)
2kis
for the nth propagating mode and P! = 0 for the evanescent mode. The
transmissivity is given by
er ky |Anl? + (mA?
=> Be Aal+ me P (a =v,h) (3.2.67)
nm © Sis jag|? + |g”?
For the lossless case, the power conservation relation is
ratty =1 (3.2.68)
For both lossless and lossy media, the emissivity is given by
€a=1-Ta (3.2.69)

The theoretical results are illustrated for a sinusoidal surface in Figs.
3.2.3, 3.2.4, and 3.2.5 at a frequency of 1.4 GHz. The effect of the row
structure on the microwave emission from a bare agricultural field has been
reported [Wang et al. 1980] together with the soil moisture contents for the
measured data. The periodic surface has a height h = 10 cm and a period
P = 95 cm and can be approximated by a sinusoidal function. For the upper
medium, we let € = €, and pt = ply.

In Fig. 3.2.3 we illustrate the comparison between the theoretical results
and the experimental data for both the vertical and horizontal polarizations
when the radiometer observation angle is along the row direction (¢ = 90°).
The reported soil moisture content varies from 26% by dry weight at top
0 to 1 cm to 21.4% at 9 to 15 cm. In the theoretical results, we take e, =
(5.5 + i1.2)e, which corresponds to a soil moisture content of approximately
18%. In the same figure, we also show the theoretical curves for the flat
surface case. It is seen that the brightness temperature for the periodic rough
--- PAGE 106 ---
§2.3 Emissivity and Comparison with Experiments 83
1.
290
,
a
zs “
aos
260 nd
ara
2a)
ee)
230 ~
rar suericeS,
. ‘.
. \
200 i \
setaa estan \
coven ace \
10S} 6e90r, Featon. nriGom \
79, ’
a a rr a
INCIDENT ANGLE
Figure 3.2.3 Brightness temperature as a function of viewing angle. Radiometer observation
plane is parallel to the row direction (@ = 90°). ¢ = (5.5 +1.2)e,
surfaces for the horizontal polarization is higher than that for the flat surface,
whereas for the vertical polarization the brightness temperature is lower. For
the flat surface, both polarizations have the same brightness temperature
value when viewed from nadir, whereas for the periodic surface, the values
for the horizontal polarization are higher than the vertical polarization at
near-nadir angles and become lower at larger angles of observation.

In Fig. 3.2.4, the radiometer observation angles are perpendicular to the
row direction (@ = 0°). The soil moisture content is 29% by dry weight at
the top 0 to 5 cm and becomes drier with depth. We use €; = (10 + i2)€p.
We see that at near-nadir angles, as compared with the flat surface cases,
the brightness temperatures for the horizontal polarization are lower and
for the vertical polarization are higher. The effect of the rough surface as
compared with the flat surface appears to bring both the horizontal and
vertical polarization results closer together at higher incident angles. The
case of observation plane at @ = 30° is illustrated in Fig. 3.2.5.

In Figs. 3.2.3, 3.2.4, and 3.2.5, we observe that the Tg curves for the
periodic rough surface are not smoothly varying. For instance, in Fig. 3.2.4,
there are kinks appearing at observation angles # near 6°, 19°, 34°, and 51°.
‘The corresponding change in Tg may be as high as 10 K. Such a phenomenon
can be explained by the appearance and disappearance of Floquet modes at
various threshold angles. The kinks are caused by the redistribution of the
--- PAGE 107 ---
84 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
20,"
7
235] /
Y
240 “
ww v
vo
225) 7
210: ">> >
4 >
ST
195) * aN
oN
180) \
me \
stig \
tes Pmowersiao .
$50 Potten, Revoem \
\
i) 10 20 30 40 50 60 °
INCIDENT ANGLE.
Figure 3.2.4 Brightness temperature as a function of viewing angle. Radiometer observation
plane is perpendicular to the row direction (@ = 0°). €1 = (10 + i2)eo.
%
27007 y
7
/
asrs /
Z
Z 7 v
2480) wo
uv
232s
Ron
2200 _
Na
. Ny
207s NY
. N
LN
1980 — \
se SMe \
tens Peau = 40h \
9230", Fe 95m, 82 1Gem \
\
i005 40 20 30 40 30 60 ‘
INCIDENT ANGLE
Figure 3.2.5 Brightness temperature as a function of viewing angle. Radiometer observation
plane is slanted with respect to the row direction (¢ = 30°). €1 = (8 + 71.9)eo.
--- PAGE 108 ---
§3 Integral Equation Approach 85
scattered power during the course of the disappearance and appearance of
the propagating Floquet modes. For real soil surfaces, such kinks will not
appear because real soil surfaces are not periodic. They have randommess
superimposed on the periodic structure.
3 Scattering of Waves Obliquely Incident on Periodic
Rough Surfaces: Integral Equation Approach
In this section, we use subsectional basis functions to solve the integral equa-
tions. The speed-up computation of the periodic Green’s functions as dis-
cussed in Section 1 will be used.
3.1 Formulation
We use the integral equations developed in Section 2.1. From (3.2.8),
(3.2.9), (3.2.14), and (3.2.15), we have
EAB.) ~ fda { CrP Fe) VE (A) ~ EulPE)H “VeGrlP.-)}
= J Ey(As) for Bs = PE 3.3
Hp(Pe)~ fel { rls.) 8 Voy) ~ Hy.) VeCo(Pes 7}
_ fHy@,) for p, = PF 7
= { for B= pe (3.3.2)
Jf do! {Gre (@e.04) Al VeBiy(P) ~ Bil AH ViGir(PasP)}
JP
0 for Pp, = Py age
=ft Ps = Ps 3.3.3
{Buin for D. = Bs (838)
Jf da! { Gre .H) Al Veta Ae) — Hay.) A VCP PsA)
P
0 for Pp, = DE
= = = = 3.3.4
{ro for Pp, = Py )
In (3.3.1) (3.3.4),
D, = 2'& + f(a')2 (3.3.5)
Bl = ct + ft(x)z (3.3.6a)
Py = wh + fo (x)d (3.3.66)
where f+(c) means infinitesimally larger than f(x) and f(x) means in-
--- PAGE 109 ---
86 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
finitesimally smaller than f(x). The discontinuity is due to the fact that
a-VGp and ft. VGip have a nonintegrable singularity when p, and 7,
coincide. In the spatial domain, the periodic Green’s functions are
.
Gyp(a,2:2',2) = ; Se them PH (hj VG — a — mPP + (2-2)
m=—co

(3.3.7)
where j = 0,1. Computation of the periodic Green’s function can be speeded
up by using transformation as described in Section 1. We have, fron (3.1.31),

©
; > etkomP 1 (5a — a! —mP)? + (z—2/)*)
m=1
cil kis thy.)P p—iky.(e—a")
=
7
°° po Whi P+ky(e 2M cos (kjg(z — 2!)u(u? — 2i)!/?
[ du—2 nn cos (Ria( = 2')ulu? — 21)"") 3 38)
i La en his P+i(hix thy )P (u2 — 2%)1/2
where j = 0,1.

Equations (3.3.1) (3.3.4) are four integral equations with eight
unknowns, namely, Ey, Hy, Eiy, Hiy, 2: VsEy, ts VeHy, 1+ VsEiy, and
n+» VsHiy. Thus as in Section 2, we have the four boundary conditions of
(3.2.37a), (3.2.37b), (3.2.45a), and (3.2.45) so that, when combined with
(3.3.1)-(3.3.4), we have cight equations for the eight unknowns.

Next we apply MoM with pulse basis functions and point matching at
the midpoint. The midpoint between #,_; and x, designated as p, is the
testing point of the point matching. For the nth internal between z,_) and
Ln

By = Evy =n (3.3.94)
A-VsEty = 5n (3.3.98)
Ay = Hy = Cn (3.3.9¢)
A-VsAty =n (3.3.9d)
Let us consider (3.3.3). The discontinuity is due to the singularity of A’ -
V.Gip for p, and 7, on the same patch (self patch). Thus (3.3.3) can be
written, assuming p, to be on the same patch so that p, = Py»,
Yon [do Gre (PsP) — Som [ dolit Gre BP.)
7 Eno ném Vent
x, ~
™ ~ at oy 0 for Ay, (9 9
—4, doi! -V'.Gip (pe, Bi) = Pm 3.3.10
Ym [. o sG@1P Pm: Ps) = 4 on, for Be (3.3.10)
--- PAGE 110 ---
§3.1 Formulation 87
Hence, if we take the difference between upper half and lower half of
(3.3.10), we have
Ym = Im [ do! - VGie (Pin, Be) + 77m [ do!i! -V.GipBm Ps)
Emaa Em—1
(3.3.11)
If the patch is approximated by a straight segment, then the two parts of
(3.3.11) should be equal to and opposite each other. Thus
Lm . Pam - a 1.
[ dof!» V.Gip (Bf, p,) = — [ do’?! - VG p(B, De) = 5 (3.3.12)
Lint Fem—r
Using (3.3.12), (3.3.10) can be written as
Yo onEmn + D2 YnDmn = 0 (3.3.13)
7” n
where
In
Enn =~ [ da! Gin. Ps) (3.3.14)
Ena
1 .
3 ifm=n
Dinn = § “pen (3.3.15)
[ do! -VeCrpPy. Bi) ifm xn
Ent
Equation (3.3.4) becomes, in a similar manner,
SY Emnén + D> DinnGn = 0 (3.3.16)
n n-
Next we consider (3.3.1). Note that at the boundary, Ey = E1y, Hy =
dE, dE, dH, dH P
Hy. == = and = a Consider the term [ do'Gp Bn B,)
fh’. VE, and use boundary condition (3.2.45b),
-P
[ A0!Go(Ppath)il Vey
Jo
= [do's 3) 42 +- all Vs By)
0 df(a’)\?|~
14(=4
da!
--- PAGE 111 ---
88 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
=) oy falta a a
=[Cr@n Peeoty(M)].,_, — | de’ | [Erm %)| colly 7)
2/=0 0 dx
Pp
+e [ do'G PP in, Bu) «Ve E ry (3.3.17)
JO
The second equality is a result of integration by parts. Since
[CrPmsP)]__p =e"? [GePns7)| (3.3.18)
=P a'=0
and
ot = cikieP “) 8816
[uP], =e? [Hu] (3.3.19)
the first term of (3.3.17) vanishes. Thus
P
| do!G P(BmsPo)it! Vy Ey = C0 D> CranGn +02 9 Brann (3.3.20)
J ” n
where
En,
Bun = [ do! GP(Pns P's) (3.3.21)
Tana
Cun = GP(P ns Pp) ~ GP (Brus Pn-t) (3.3.22)
with p, = (tn, f(ap)). Also let
4 ifm=n
An = tn 3.3.23
mm - [ do'il -V.Gp(Pm: Be) ifm #n ( )
nat
Integral equation (3.3.1) becomes, using (3.3.23) and (3.3.20),
Eyi(Pm) ~ C2 > Brandn + 6 > CmnGn = Y> Amn In (3.3.24)
” 7 7”
Similarly, from (3.3.2) we have, using boundary condition of (3.2.45a),
Ayi(B.) ~ €2 Y> Bnn&n = do 9 Cnn = > Amnbn (3.3.25)
n n 7
where cg, ¢2, do, and dy are given in (3.2.42a-b) and (3.2.44a b).
Equations (3.3.13), (3.3.16), and (3.3.24)-(3.3.25) are the equations gov-
erning the unknowns Yn, dn, Gr and €. In matrix notation, they can be put
in the form
A c@B -mC 0 ¥ Eyi
D E 0 0 6 0 .
\z. 0 A ‘| | = | ty: (3.3.26)
0 0 D E & 0
--- PAGE 112 ---
§3.2 Polarimetric Brightness Temperatures 89

é z

sr hh

1 y

' a

' 3 -

1 tj ut

H L-Se e

T = Ho;€o

1 ra

1 olen

L- a| INI\I\f«

—
Pp Ho,

Figure 3.3.1 Polarimetric emission from a sinusoidal surface at temperature To.
Solving (3.3.26) numerically gives the surface field unknowns.

After the surface fields are determined, the coefficients of the reflected
Floquet modes can be calculated. The reflected fields for z > f(x) can be
written as

rho
By = Yo dpethn Pe (3.3.27a)
n
its
Hy = So bebe Pe (3.3.276)
n
Using (3.2.21) for b, and the like for b%”, we have
1 7? femme ap op Ora
bn == | do! | —_—A' - VLE, (p,) — Ey (BA - Vs | (3.3.28
sip |, €0'| GW VB uB) ~ By(@H- Vi | (8.8280)
r+, cto
1 P en thn Be ent Be
= ae da! | i! - Vy (B,) — Hy (ph - V,—
0 = sep fo! | Goal Vit) — Mytadal VI
(3.3.28)
3.2 Polarimetric Brightness Temperatures
In this section, polarimetric brightness temperatures are illustrated for the
emission from a sinusoidal surface (Fig. 3.3.1). The frequency is fixed at
1 GHz and the period is fixed at 50 cm. The first region is free space and
the physical temperature of the lossy dielectric, Tj, is fixed at 300 K. The
expressions for emissivity of the four Stokes parameters can be found in
Chapter 3, Section 5.4 of Volume I.
--- PAGE 113 ---
90 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
00 300
200 * 200 +t
me, + mo ot ft . 4
mf os) ‘Oy m0 e © f *
i “os fal 9 2 +
Ee . .
I Ded fs
Bee . Bee
Foy "ae
ea 0
0 B10
iat rr ee a at rr re ee
us tn degrees A in degrees
a «
« «
2 2
» .°
: » ; 10
. °
fil fg + £.
wt Up tt os
-%0 rs a
~o ~o
a er ac er
Ps Ln dagrene PM tn degrees
Figure 3.3.2 Brightness temperature versus @. 4 : 1 = 6, °: €r1 =9, #: €p1 = 12.
Figure 3.3.2 plots the brightness temperatures versus the azimuth angle
@. For these plots, the height is 15 cm and the incident angle @ is 20°.
Calculations are made for three different values of €1 = €1/€o. It is seen
that Tj, and T, tend to be higher for smaller ¢-1, while |U| increases with
increasing €,1. No significant change is observed in V. With increasing ¢, Th
decreases and T, increases. The brightness temperature of U is zero when
@ = 0° or @ = 90° as expected. In between, it decreases to about —30 K.
Values of V are small for the whole range of ¢.
Figure 3.3.3 shows the variation with respect to 6 with @ fixed at 45° and
height kept at 15 cm. Again, the plots are given for three different values of
--- PAGE 114 ---
§3.2 Polarimetric Brightness Temperatures 91
0 300
0 200
+ +

ee +t wo se

mb io e mt © © © 4
z ° . °
a fob!
be» . Lee .
3 e+ i .
£20 20
“he . “ae

°

= =

0 . B10

200 00

o 1 mm «60 00 m0 60 o 10 26 3 <0 8060 000 wo

et tn degrees ‘eta tn degree

© «

« «

2% 3

» 20

ze $
i ° . : i ol w ag :
£78 +e go) 3 3
> + : = :
~~ + ° ~2
eo 8
os) a nd 30!
~0 ~0
0 +0
ow a wow 90 60 70 60 oo 010 2 30 «0 60 e070 ao 8D
‘theta in degrees Geta fo degrees
Figure 3.3.3 Brightness temperature versus @. +: ¢-1 = 6,0: 1 =9, #2 ép1 = 12.
€,, and we observe the same behavior. There is a more than 30 K difference
in Th, for different €,; values at 6 = 60°. We also observe a change in V with
increasing 6.

Dependence of brightness temperatures on the surface height is given in
Fig. 3.3.4. For this case, ¢-1 = 12, 8 = 20°, and @ = 30°. We see a general
tendency of increasing 7}, and T,. V does not change much, but U varies
significantly with height. We note that when the height is 10 cm, |U| is as
high as 48 K.

Finally, we analyze the effect of complex €,; on the brightness temper-
atures in Fig. 3.3.5, when @ is 20°, @ is 45°, and height is 15 cm. The real
--- PAGE 115 ---
92 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE

00

200

200 + 4 Ff

+ °

= * + + Gg ee °

:- °°
5 250

: +e?

"eo

= °

= 8

210

‘200

oz 4s 8 0 a2 te as 2 22 mm oe 30
Inelgbt 10 on
10
° o 6 8 8 F © ~ 2 6
10
> +
3 + *
> 30 +
+ + ¢
“0
+
“80 *
~e0
o 2 « © © 00 Ww wt 16 18 90 2 &% 6 25 30
eight te oxo
Figure 3.3.4 Brightness temperature vs. height. + : T,(U), 0: Ty(V).
part of €,; is fixed at 12 and the imaginary part is varied from 0 to 8. Real
€+1 is taken as a base and the difference in temperatures is plotted. It is seen
that variations in T;, and T, are almost identical while the decrease in U is
less. There is a slight increase in V.

Note also that the plots are not given as continuous curves. We merely
show the results of some calculations, and linear interpolation between these
may be misleading. This is due to the presence of kinks in actual continuous
curves as shown in Section 2.
--- PAGE 116 ---
§4 Ewald’s Method 93
2
0
-2
~4
®
3
3
-8
-6
-10
712
o 1 2 38 4 5&8 6 7 6 8 10
imag epsi
Figure 3.3.5 Brightness temperature vs. én). +: Th, 0: Ty: U,v: V
4 Ewald’s Method
A method that is used in computing periodic Green’s function is the Ewald’s
method, which we will discuss in this section.
4.1 Preliminaries
We first describe several properties that are used in the derivation of Ewald’s
method. The first is an integral identity of the Hankel function.
From Abramowitz and Stegun [1965], the integral representation of the
Hankel function of order v is
1 perm ink 7
HO(2) = 4 | dt =D with Jarg z| < 2 (34.1)
Ti Joc" 2
where the integral contour in the complex t plane is labeled by C’. Next we
make the transformation u = e'. Then sinht = } (u— +) ;dt = du/u. The
--- PAGE 117 ---
94 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
integral becomes
lf z 1
)(,) = a z 2 \ | ent ‘
AS” (z) = [. du exp F (u *)) u (3.4.2)
The contour C’ in the complex u plane is from 0 to —oo along some suitable
chosen path.
The spherical Hankel function of order 0 is, letting z = kyr,
ier 0) Ty
- =hy’ (Kor) = Ty (ki,
kor 0 (kor) kort 2 (kor)
a ol kor 1 3
=,/——— | d —-(u--)|w? 3.4.3
\ kor wi f. wu exp 2 (« ~)] we B43)
Next we make transformation of variable to s. Let u = shz.du = — sds,
duu? =-,/ ds. Then
1 i2 ke 25
1 (hor) = [ ds exp [i = 232 (3.4.4)
The contour C’ in the complex s plane is from oo to 0 (Watson, 1966]. We
define the contour C' to be the reverse of C’ so that C is from s = 0 to
sx.
2
Q) __2 Fo ao 34
hg (kor) = iVak [ ds exp [i —rs (3.4.5)
To choose the proper contour. Note that as s > oo, the convergence of the
integral is dictated by exp(—r?s?) and we require Re(s?) > 0. Thus
as 8 > oo, largs| < . (3.4.6)
On the other hand, as s — 0), the convergence of the integral is dictated by
exp (%) and we require Re (2) < 0 which means 5 < arg (k2) —Qargs <
ae, Thus
30 7 .
ass — 0, —7té<ages<—-7+8 (3.4.7)
where 3 = } arg (k2) = arg(ka).
The contour C’ is as shown in Fig. 3.4.1. For0 < 8 < 3 the intersection
of these two regions is [Jordan ct al. 1986]
us T
~~ <args<—-—4+39 3.4.8
q Sess —gti (3.4.8)
The second relation is the definition of the lattice vectors and reciprocal
lattice vectors. Consider a periodic lattice that is three-dimensional. Let
R= mG + no + nya3 (3.4.9)
--- PAGE 118 ---
§4.1 Preliminaries 95
Ims
7 Res
Sz-- xt +9
‘ ToS.
N. ant
N ~~
N
N
aN C
N.
S.
N
aN
Figure 3.4.1 Contour C with @ = argko
where @, @, and Gy are the basis lattice vectors and ni, nz, and ng are
integers.

By a periodic medium, we mean that the wave function ~ obeys a wave
equation with periodic potential V(F). The periodic potential obeys the con-
dition

V(iF+R) =VF) (3.4.10)
where R is as given in (3.4.9). Note that
oo 2° oo
y=-y od Gan)
Ro M=—0o mp=—00 n3=—00
The reciprocal space is defined by
K = [by + lobe + Igd3 (3.4.12)
and
Q = G - Ae x G3 (3.4.13)
is the cell volume. The vectors by, 62, and bg are the basis in the reciprocal
vector space
z 2a
b= Gm x Ty (3.4.14)
> 2 5
bo = Bas xa (3.4.15)
z 27
by = ay x a (3.4.16)
2
Thus
6; +d; = 26; (3.4.17)
--- PAGE 119 ---
96 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The sum 7x is used to denote summation over the reciprocal lattice space
oo wo
y-y yy” 418
RK  y=—00lp=—00ly=—00
Note that exp(iK - R) = 1.

The third relation is the Poisson’s summation which replaces summation
over lattice vectors by summation over reciprocal lattice vectors. Consider
any function f(#) and define g(¥) by

a) = Sle*Ps F-R) (3.4.19)
R
Consider
a7 +R) = e** se +R -R) (3.4.20)
R
Then
a+ R) = SoHE) pRB") = FF air) (3.4.21)
2
Thus q(¥) obeys Bloch’s condition. We then have
a?) =F w(7) = So e* RFF R) (3.4.22)
R
where w(F) is periodic in R. The periodic function w(7) can be represented
by a Fourier series in spectral domain
w(F) = So wae! F = oF RFR (3.4.23)
K R
The Fourier coefficient is given by
le a
wR=s [ drw(FeKF (3.4.24)
2Q Jog
where 2 is the area of the unit cell and Q is the domain of cell 0. Hence
1s Ke ike ch =
we=a |] dre hte *TY che FGF _R
kK Q I, > a )
R
1 (KiB)(7-E = J
=o f dre O-®) per _ BR) (3.4.25)
2 &— Joy
R
Let F(k) be the Fourier transform of f(F)
F(R) = / dre—** f (7) (3.4.26)
--- PAGE 120 ---
§4.1 Preliminaries 97
The integration is over all space. We can divide the infinite space into peri-
odic array of cells
F(R) =>, dre~*®* f (7) (3.4.27)
ROR
where Q_ is the cell with center at Rf. Let 7 = 7 — R. Then
PR => f are ®O My —® (3.4.28)
F 1
Using (3.4.25) and (3.4.28),
Toe a
wR = ght) (3.4.29)
Putting (3.4.29) in (3.4.22), we establish Poisson’s summation formula
Is 1_- = atoms
q(®) = x eh Rs (FR) = x grk+ Kei) (3.4.30)
R RK
In the above derivation, 7, R, K, and Rare 3-D vectors. For the case when
F =p+ 22 are 3-D while p, R, K, and k are 2-D vectors, the corresponding
results are as follows.
Let
R= na) + nd (3.4.31)
where m1 and nz are integers_ and @ and @2 are two-dimensional lattice
vectors in the z-y plane. Let K is the reciprocal lattice vector
K =lb; + lobe (3.4.32)
0; -G; = 276i; (3.4.33)
~~ ©
vs-E Dd (3.4.34)
K  =-col=—00
Also b, x bz and @ x @ are both in positive 2-direction, and exp(iK -R) = 1.
Let k be a 2-D vector and
af) = le* FFF —R) = Soe fG—R+ 23) (3.4.35)
R R
The Poisson’s summation formula is
a lo < ges
p) = ER (= R) —- Sri pes (B4R) 5 949
a?) = ue f(F@-R) = x ar &+ Ke é (3.4.36)
--- PAGE 121 ---
98 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
where F'(k) is the 2-D Fourier transform of f (7):
F(k) = fo e PF (5 + 22) (3.4.37)
=~ oy. _t i ik BE 24
f@+22) = aa | & F(R) (3.4.38)
4.2 3-D Green’s Function in 3-D Lattices
We first consider the case where 7 and FR are three-dimensional. A periodic
Green’s function involyes summation of radiation from sources at all the R
in the periodic lattice. Let
_ __. gikelF-R|
GZ(F,0) = )_ exp(ik -R)——— 3.4.39
s(7-0) = Yo explik -R) ae (3.4.39)
R
where ko = w,/fié is the wavenumber, k is a wavevector, and S7z is a three-
fold summation over the lattice. In solid state theory, k is a vector in the
first Brillouin zone. More geuerally, we need to evaluate
— 2 gether R
GFP) = exp(ik - 2) ————_—— 3.4.40
aT 7’) y pik By a (3.4.40)
where F and 7 are both in the unit cell centered at the origin. The unit cell
centered at the origin has R = 0. Direct summation of (3.4.40) converges
slowly because the decay for large indices is only 1/(distance).
Without loss of generality, let r > r’. Note that
VG(F,T) + RGF. 7’) = -(F - 7’) (3.4.41)
We use the addition theorem for r > r’,
etkelt—-F"| co Ol - ; y
mr-r| = > s ikohy(kor Yim (*)ju(Kor Yim (7) (3.4.42)
1=0 m=-i
Then we define Dj,,(7) such that
co
GFP) =O YP (i! Dim (Pju(hor Vin) (3.4.43)
120 m=-1
In (3.4.43),
= (6,0) (3.4.44)
is the direction vector with angular variables (6’,¢’). aud Yim(6’, @') are the
spherical harmonics. In this section, unlike in other chapters, we shall define
--- PAGE 122 ---
§4.2 3D Green’s Function in 3-D Lattices 99
them as
1
(21 +1) (l— m)!]? 6
y, 4) = 1 aoe Oy eit 3.4.45
in( 4) = | ED EO rin (cos te (3.445)
where P/"(cos @) is the associated Legendre polynomial as defined in (1.4.37)
of Volume I. The definition in (3.4.45) differs from (1.4.45) of Volume I by
a scale factor. The orthonormality relation for the spherical harmonic is
Qn oo
[46 fF at six 05(0, 89% (0.6) = 5S (3.4.46)
0 0
From (3.4.43) and (3.4.46)
Dim(F) = tke De® Phy (hole ~ R))i'¥im(F — R) (3.4.47)
R
where F — R refers to the unit vector point from R to F and is in the direction
of the spherical coordinate angles, © and ®. Note that G;(7.0) is a special
case of (3.4.47) with
1
GF, 0) = \ Gyo) (3.4.48)
From (3.4.47), we can interpret Dj,,(7) as multipole radiation from the lattice
points.
Next, use the integral identity
12 f° 22, Ke 244
holo) = Fee | ds exp [-" P+ is (3.4.49)
Cc
where C' is a contour (Fig. 3.4.1) that ensures the convergence of the integral.
For C, as indicated in (3.4.49), the arg s of C obeys the condition,
7 T
a <args<p- a (3.4.50)
where 3 = arg ko.
By using (3.4.49), no (kor) = ~A) (kor), the recurrence relation
21+1
hisi(kor) = @l+)) Tor ) hal kor) — hy (Kor) (3.4.51)
‘0
and mathematical induction, it can be shown that
Ca 2 2.2, Ke
or) == | ds s a2? 4 2% 4.52
hilkor) RAVE | ds s* exp |—r?s* + re (3.4.52)
c
--- PAGE 123 ---
100 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
Next, we split the integral of s into two parts from 0 to E and from E to
co, where F is known as the splitting parameter. Thus
Din (F) = DY (F) + DER) (3.4.53)
where
DO gp a2 eFRe_Bluly, wo).
in (TF) = HLS |F— RLV inl? “ON
2 2 Pi2.2 RR
ds s” exp |—|r — RI?s? + —> 4.54,
| ss exp [=F rps + *| (3.4.54a)
oi _ —~ 9
(2)—) _ 2 BR Bly. (oy _2
DPF) = mL FF RY FYin(F ~
0 > « ke
[ ds s” exp [- — Rs? + is] (3.4.54b)
E 4s
The quantity De (®) of (3.4.54b) can be calculated by direct numerical in-
tegration since an exponential decay is endowed in the integral, particularly
for large R. For | = 0, it can be evaluated exactly as will be shown in Section
4.3.
For the calculation of DOW), we let
f(F—R) =#YVin(F — RF — Ri! exp(—lF — Rl?s*) (3.4.55)
Sek R —R) = ul) (3.4.55b)
R
Then
gl 9 fb ,2
()in) _ 2 2 2t K = ;
Din (F) = Eve dh ds 8” exp 42 u(?) (3.4.56)
Using Poisson’s summation formula (3.4.30) from Section 4.1 and (3.4.55b),
1 Rene. o -
ur) = G Ve FE+K) (3.4.57)
R
where F'(k) is the Fourier transform of f (7). From (3.4.55a) and the property
of Fourier transform
‘co TH
F(k) = | OF #'Vim(*)r! exp(—r?s*)e (3.4.58)
—co
We use the spherical wave expansion of
= an 37 (—i) (kr) ¥ih PV) (3.4.59)
im
--- PAGE 124 ---
§4.2 3-D Green’s Function in 3-D Lattices 101
Then using the orthogonality relation of (3.4.46), we obtain
_ 00 5 ft Qn .
F(R) = [ dr r? [ dO sind | dgiV im (8, 37! exp(—r?s?)
Jo 0 0
«Ae S(~1y! julie) Vine Vim (B)
Um’
7. a, _ kt Ke
=n Sint exp (-#) (3.4.60)
Putting (3.4.60) and (3.4.57) in (3.4.56), we have
°E 2 —
ayy 1 2 RY 1 Ra Rye
Dry (F) “ave, ds exp a ave +K)F
=. FI! =. Pe
7 aa |k+ Ke k+k
: ary EVinK +K EAL exp [Par] (3.4.61)
The ds integration in (3.4.61) can be performed. We get
DO = 4 Vin (E+ RihR) lk+ |! E = Fer
r)= TWH L € Sa EXP | ee
tm Qe \k+ Rl? — 2 AE?
_ (3.4.62)
This converges rapidly in A because of the exponential decay in K. To
summarize, using (3.4.62), (3.4.53) and (3.4.54b), we have
DimlF) = Din) + Dim F)
riz?
1¢4 [k++ Ky'exp(# RE )
a a RK Bs
=o Vin(k + Kye 47 —____x
it Q oy m [r+ KY —
ki. = 3 2
+2 x ek Re _ Rilly. (F Ns
co _ Ke
. [ ds exp [- —RpPs + | } (3.4.63)
JE As’
In numerical implementation, the parameter E in (3.4.63) has to be chosen.
The optimum choice of the splitting parameter E is when DWF) and De (7)
do uot differ by more than several orders of magnitude. For the special case
of l=m=0,
--- PAGE 125 ---
102 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
2b Kl?
[1 1 f4nc ak on(® = )
Gz(F,0) = yf —Pool(F) = aK ellk+K)F __\
k dn An ad [E+ RP — 8
+ yet RS [vas exp|—|F — R)?s? + ua (3.4.64)
ee de s BR 3.4,
R
4.3 3-D Green’s Function in 2-D Lattices
We next consider 3-D Green’s function in 2-D lattices. In this case the space
is three-dimensional so that the field point 7 and source point 7’ are in
three-dimensional space. However, the periodic lattice is two-dimensional.
This problem has applications in scattering by frequency sclective surfaces,
periodic surfaces, and random rough surfaces with periodic boundary con-
ditions. Let k be a 2-D vector and the Green’s function be
— a. eikol?—R| ER ikoho(kolr - Rl)
GF) = ¥° exp(ik - R) ——— = So eth SOON (3.4.65
HF) =D expt ara Hh L dn (3.4.65)
R R
where Dy = VP oo Lasso: To put (3.4.65) in spectral domain, we let
k=kzd + ky and
eikor i _ ik p+ik, 2|
7) = —— =—, | dk 3.4.66
f(r) Anr 4p? | 2k, )
Then
_ jet BF le!
F(k) = ———== (3.4.67)
2k? — k?
Using (3.4.67) in the Poisson summation formulation, the reciprocal lattice
domain solution is
i eh emp
G(F) = = —— es hp 3.4.68
= 9a (3.4.68)
R
where
kz = \/k2 —|k+K\?, Imk, >0 (3.4.69)
We make use of the integral identity of (3.4.49) for ho(k(F—R]) and a splitting
parameter of B, Thus
G(F) = GilF) + Ga(F) (3.4.70)
where
--- PAGE 126 ---
§4.3 3D Green's Function in 2-D Lattices 103
i) = exp(ik- BZ f asexp |p RP? +] gar )
1) = Fe exp li Vid Is exp r 8 1 A.71a
R Cc
nme tpl Ree B
Ga(F) = ip Loh . my | ds exp [-r ~RyPs?+ 75] (84.710)
The integral of G2(F) in (3.4.71b) can be calculated as follows
Vite is EXP r s ra
tol oo _ ik _ 2
== ds \\F — R| - —% —|F- Rs? + —&
Var {[. ash R| ma eo | |r — Ri*s +a2
~ aslir Fy . tke = Fil2e2 4. Ke
+f ds [r-m + | exp [-r — Ris? + re
= _[explitir —B))
Vi iF RO
co miko a. ike \?
ff ds (i ~R1- 3) xn] - (i ~Rijs+ oe
= Ty fae lim FR 4. tke ike)?
+ exp(—iko|F — ny fF ds ('r —Ri+ a) exp |— (r —R\s— oe
(3.4.72)
The complementary error function is
2 oe 2
erfe(z) = — [ dwe™ (3.4.73)
Then
2 [° = F242. Ke
= |, ds exp (ir 8 +i
| _ fexplikgl — Rierte (jr — Rip + tke
= = 4e tolF — rF- RE +
air - RY OP oF
a a iko
+exp(—ike|F — R})erfe (\r -RiE- mE) } (3.4.74)
Putting in (3.4.71b) gives the expression of G2 that is written in (3.4.836).
For Gi(F), we note that since R is in the x-y plane and 7 = (x,y, 2),
exp(—|F — Rls?) = exp(—2?s”) exp(—|p — R[?s?) (3.4.75)
where p = 2% + yy is the two-dimensional position vector. Let
--- PAGE 127 ---
104 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
f(p- R) = exp(-|p - Ri’s) (3.4.76)
a(p) = >_exp(ik - R) Ff — PR) (3.4.76b)
R
From (3.4.36) of Section 4.1,
— _ an
B) = ¥- exp(ik - R) exp(—[p — Ri?s*) = S> = PR + Kye? (3.4.
4() = So exp(ik- R) exr(—[p — R’s*) = SOP E+ Ke (3.4.77)
R K
where F(k) is the 2-D Fourier transform of f()
~ oe En 20, 7 Ke
F(k) = I dp e~**? exp(—p?s*) = = exp (-) (3.4.78)
00 s 4s’
Thus we have
kp Kp. kt KP .
q(p) =e" > e "On exp [-Fext (3.4.79)
RK
Putting (3.4.79) into (3.4.71a) gives
12 /* KB .
Gir) = —— dsexp { —& 3) exp (— 22s
1) =z = sexp | ul) exp (—22s?)
12 i(k+K) po F ds Ik+ KP 2.2 ke
ray be af, P°P| ae 78 + aR
K c
(3.4.80)
Letting s + 1/s in (3.4.80), we have
n@=—! 1+R7 [~ dsexp|-(HARE _ ke) p_ 2
GF) = a a ener 7 1)% - 2
c
(3.4.81)
where C’ is a contour that ensures convergence at oo. Equation (3.4.81) is
now in similar now to (3.4.71) and can be manipulated in a similar manner
to be in the form of complementary error function.
To summarize, we have
G(F) = Gi(F) + Ga(F) (3.4.82)
where
7 i cilktK)p . ik,
GilF) = io x a {esp(ik.e)nt (-# - t.)
RK
. ike 2 4 92
+exp(—ik,z)erfc oF +E, (3.4.83a)
--- PAGE 128 ---
§4.4 Numerical Results 105
with kz = 4/k2 —|k+K|?, Imk, > 0, and
1 a 1 = = ik,
Ga(F) = 5 = exp(ik- Ra {exptilr — Ri) erfe G -RIE+ aa)
Lic.P = _ Fi ike
+ exp(—ikelr ~ Ri) erfe (|r — RIE — 58 (3.4.836)
The splitting parameter F’ is optimally chosen such that G)(F) and G(r)
do not differ by more than several orders of magnitude.
4.4 Numerical Results
We illustrate the results for the case of 3-D Greens function in a 2-D square
lattice. The case that the Ewald’s method gains is when the medium is
lossless and z = 0. Let the lattice be a = az%, G2 = ayy. Then b) =
25%, bo = 289. The lattice vectors and the reciprocal lattice vectors are
2 iy
respectively
R= maeé + n2ayi (3.4.84)
=> 2al 2ai:
Kap 4 eg (3.4.85)
Qy ay
Also Q = a;ay. We consider the case that k = kict + kiy. The spatial
domain solution is
Ng Ng in k yeitonins
Giz. y. = UKizMiGeThiyN2dy) ~ 3.4.86
wn SS cee oN
ny=—Ns na=—Ng
where
Rnyng = \f (t — maz)? + (y— ngay)? + 2? (3.4.87)
and we also truncate at N;.
The reciprocal lattice domain, or the spectral domain solution is
LON Ne i[ (hoot 22D) c+ (hin +222) uy] cider rple
i e ee ay JY] gikayigle
G(a,y,z) = => (3.4.88
e2=—5 oY = (9.4.8)
L=-N,b=—N,
where
: Qn \? 2nly\?
kents = 4{k2 — [(« + ait) + (ku a) (3.4.89)
az ay
and truncation is at N,. Also Im(kzj,1,) > 0.
--- PAGE 129 ---
106 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
On the other hand, in Ewald’s method,
G(x, y, 2) = Gi(a,y, z) + Gola, y, 2) (3.4.90)
where
5 MN il (bret 2) 2+ (hi +24) 9]
i é we oy
Gia, y, 2) = = —
MBI) = FG u uo Rett
h=-M b=-Ny ib
{eteoeterte (Se - Es) te Kutt erfe (Se + ks) }
(3.4.91)
and
No No cilkiamaethiynady) pikoRny na ik,
- 7 e yay) ane iky
Gateys)= Yo ye ee (Ram + 5)
m=—Nom=~No
No Nz pilkianiae-+hiynaey) tke Rn n ;
é re a ik,
ere | Rainn B- 58
+ 8tRnins er e( Many a)
n=—N2n2= No
(3.4.92)
where truncations of G; and G2 are done respectively at Ny and Np.
Asymptotically,
enw?
rfe(w)  —— 4,
erfe(w) Jaw (3.4.93)
Thus both series of Gi(x,y) and G2(x,y) have exponential decay:
2 2
Gi(x,y) (=) + (a) (3.4.94)
Fi(2,y) > exp | —~—4—_—*" *— 3.4.6
We,y, Pp 42
Golx,y) > exp [- (mae)? + (n20)”) B] (3.4.95)
-(2)? 2
For the 1-D case, the two series are respectively e (=) and e7[(mee)"1E*_
The two series have the same exponential decay rate if E = /7/az.
For the 2-D case, we choose splitting parameter £ such that
E=,f— (3.4.96)
Ay Ay
In the numerical simulations, we use the following parameters: A = 1, a, =
0.95A, ay = 0.95A, hic = Re(k,) sin 6; cos $j, kiy = Re(ko) sin 8; sin d;, Ni =
Ny =2, B= \/-™ = 1.86671.
ey
--- PAGE 130 ---
§4.4 Numerical Results 107
[Case TN, [Spatial [N- [Spectral 2G GT Ewald)
fe) [300 [0202+ a.517 /250 | 0.202 wo.a17 | 0856+ as |—O.15A— w.0170 | 0.2024 W517
(b) |1000 | -0.164 + 40.069 | 10 | —0.166 + 10.071 | -0.623 + 10,071 0.457 0.165 | 40.071
(ec) | 1000 | 0.0566 + 10.473 | 10 | 0.0163 + 10.457 | 0.162 + 10.468 | —0.146—w.010 | 0.0162 - 10.457
(a) {1000 | 0.0609 ~i0.465 | 300 | 0.0216 + 10.450 | u.175+%0.460 | —0.154 — i0.o106 cn
Table 3.4.1 Computation of the periodic Green’s function using Ewald’s method.

We use very few terms in the Ewald summation. The slight difference in
the results could be due to the accuracy in computing the complementary
error function of complex arguments.

The results for the four cases considered below are tabulated in Ta-
ble 3.4.1.

Case (a) Lossy medium: k, = 2r(1 + 10.01), @; = 45°, ¢; = 25°, z = 0,
x = 0.48, y = —0.91). In Fig. 3.4.2, we plot the convergence tests of the
spatial solution (dotted line) and the spectral solution (solid line) for the
real part of the Green’s function as a function of N, and N, respectively.
There are good convergence for both spatial and spectral solutions.

Case (b) Normal incidence: k, = n 6, = 0°, , @ = 25°, 2 =O01A, 2 =
0.48\, y = —0.91A. In Fig. 3.4.3, we plot the convergence tests of the spatial
solution (dotted line) and the spectral solution (solid line) for the real part of
the Green’s function as a function of N, and N, respectively. There is good
convergence for the spectral solution. Because z is not equal to zero, there
is good exponential decay for the evanescent Floquet modes in the spectral
solution. Ou the other hand, the spatial solution needs many more terms.
Case (c) Oblique incidence: z 4 0, ky = on 6; = 45°, @ = 25°, 2 = 0.1,
a = 048A, y = —0.91). In Fig. 3.4.4, we plot the convergence tests. There
is good convergence for the spectral solution. On the other hand, the spatial
solution does not converge even for N, = 1000.

Case (d) Oblique incidence: z = 0, ko = 3, 6; = 45°, $; = 25°, z = 0,
a =0.48A, y = —0.91A. In Fig. 3.4.5, we plot the convergence tests. Neither
spatial solution nor spectral solution converge well. However, the spectral
solution shows a better convergence.

It is important to emphasize that Ewald’s method requires very few
terms for all the four cases considered. As shown in Table 3.4.1, the results
of Ewald’s method are also accurate.
--- PAGE 131 ---
108 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
0.4, v v — =
Spatial solution
i — spectral solution |!
0.35 —
03) 7
oO 0.25
3
5 02
3
3
[0.45
o4 4
0.05)
% 40 20 30 40 50 60 70 8 90 100
Ns and Nr
Figure 3.4.2. Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (a) — Lossy medium: ky = 24 (1410.01), 0; = 45°, 6 = 25°, z = 0, c = 0.48,
y= 0.91).
$0.44] 4. re
spatial solution |
——=_Spectral solution
0.15
-0.16) : Lo
° coe
3 :
é 0.17] .
a
3
é :
0.18}: J
0.19)
0.2)
0 100 200 300 400 500 600 700 600 900 1000
Ns and Nr
Figure 3.4.3 Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (b) — Normal incidence: ky = 22, 6; = 0°, dj = 25°, = = 0.10, # = 048A,
y= 0.910.
--- PAGE 132 ---
§4.4 Numerical Results 109
05,
spatial solution
— spectral solution |
04
03- 4
o | .
3 02 4
=
5
«
Bot
@
ty)
0.1
02 1 1 a
0 10 20 30 40 50 60 70 80 90 100
Ns and Nr
Figure 3.4.4 Convergence of the spatial solution (dotted line) and spectral solution (solid
Tine) for case (c) ~ Oblique incidence: z # 0, ko = 32, 0) = 45°, ; = 25°, z = 0.12,
w= 0.482, y = —0.91A.
05 . Te eee
spatial solution
— spectral solution!
0.4- 4
0.3
oO
5 0.2
=
5
& .
Bor
& |
0} 4
04
0.2. 1 1 ‘ sat
0 10 2 30 40 50 60 70 8 9 100
Ns and Nr
Figure 3.4.5 Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (d) — Oblique incidence: z = 0, ko = 22, 0; = 45°, 4; = 25°, = = 0, x = 0.484,
y= 0.91).
--- PAGE 133 ---
110 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
REFERENCES AND ADDITIONAL READINGS
Abramowitz, M. and J. A. Stegun (1965), Handbook of Mathematical Functions, Dover Pub-

lications, New York.

Chan, C. IL. (1995), Analysis of frequency selective surfaces, in Frequency Selective Surface
and Grid Array, edited by 'T. K. Wu, Chapter 2, 27-85, Wiley-Interscience, New York.

Cohen, E. (1995), An Ewald transformation of frequency domain integral formulations, Hlec-
tromagnetics, 15, 427 439.

Ewald, P. P. (1921), Die berechnug optischer und elekrostatischen gitterpotential, Ann. Phys.,
64, 253-268.

Kipp, R. A. and C. H, Chan (1994), A numerically efficient technique for the method of mo-
ments solution to planar periodic structures in a layered media, IEEE Trans. Microwave
Theory Tech., 42(4), 635-643.

Joannopoulos, J. D., R. D. Meade, and J. M. Winn (1995), Photonic Crystals: Molding the
Flow of Light, Princeton University Press, Princeton.

Johnson, J.'T., J. A. Kong, R.'T. Shin, D. H. Staclin, K. O'Neill, and A. W. Lohanick (1993),
Third Stokes parameter emission from a periodic water surface, IEEE Trans. Geosci.
Remote Sens., 31(5). 1066-1080.

Jordan, K. E., G. R. Richter, and P. Sheng (1986), An efficient numerical evaluation of the
Green’s function for the Helmholtz operator on periodic structures, J. of Comp. Phys.,
63, 222-235.

Kittel, C. (1996), Introduction to Solid State Physics, 7th edition, Wiley, New York.

Mathis, A. W. and A. F, Peterson (1996), A comparison of acceleration procedures for the
two-dimensional periodic Green's function, IEEE Trans. Antennas Propagat., 44(1),
367-571.

Mathis, A. W. and A. F. Peterson (1998), Efficient electromagnetic analysis of a doubly
infinite array of rectangular apertures, IEEE Trans. Microwave Theory Tech., 46(1),
46-54.

Munk, B. A. (2000), Frequency Selective Surfaces: Theory and Design, Wiley-Interscience,
New York.

Nghiem, S. V..M. B. Veysoglu, J. A. Kong, R. T. Shin, K. O'Neill, and A. W. Lohanick (1991),
Polarimetric passive remote sensing of a periodic soil surface: Microwave measurements
and analysis, J. Blectromag. Waves and Appl., 5, 997-1005.

Oberhettinger, F. and 1.. Badii (1973), Tables of Laplace Transforms, Springer-Verlag, Berlin.

Radisic. V.. Y. Qian, and '. Itoh (1998), Broadband power amplifier using dielectric photonic
bandgap structures, IEBE Microwave Guided Wave Lell., 8, 13-14.

Veysoglu, M. E., S. H. Yueh, R. T. Shin, and J. A. Kong (1991), Polarimetric passive remote
sensing of periodic surfaces, J. Electromag. Waves and Appl., 5, 267 280.

Wang, J. R., R. W, Newton, and J. W. Rouse (1980), Passive microwave remote sensing of
soil moisture: The effect of tilled row structure, IEEE Trans. Geosci, Remote Sens., 18,
296-302.

Watson, G. N. (1966), A Treatise on the Theory of Bessel Functions, 2nd edition, Cambridge
University Press, Cambridge.

Yablonovitch, E. (1987), Inhibited spontaneous emission is solid state physics and electronics,
Phys. Rev. Lett., 58(20), 2059-2062.

Yu, Y. X. and C. H. Chan (1998), On the extension of Ewald’s method to periodic structures,
Microwave Opt. Technol. Lett., 19(2), 125-131
--- PAGE 134 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
Chapter 4
RANDOM ROUGH SURFACE SIMULATIONS
1 Perfect Electric Conductor (Non-Penetrable Surface) 114
1.1 Integral Equation 114
1.2 Matrix Equation: Dirichlet Boundary Condition
(EFIE for TE Case) 116
1.3. Tapering of Incident Waves and Calculation of Scattered
Waves 118
1.4 Random Rough Surface Generation 124
1.4.1 Gaussian Rough Surface 124
1.4.2 Fractal Rough Surface 132
1.5 Neumann Boundary Condition (MFIE for TM Case) 134
2 Two-Media Problem 137
2.1. TE and TM Waves 139
2.2 Absorptivity, Emissivity and Reflectivity 141
2.3 Impedance Matrix Elements: Numerical Integrations 143
24 Simulation Results 145
2.4.1 Gaussian Surface and Comparisons with Analytical
Methods 145
2.4.2 Dirichlet Case of Gaussian Surface with Ocean Spectrum
and Fractal Surface 150
2.4.3 Bistatic Scattering for Two Media Problem with Ocean
Spectrum 151
3 Topics of Numerical Simulations 154
3.1 Periodic Boundary Condition 154
3.2 MFIE for TE Case of PEC 158
3.3. Impedance Boundary Condition 161
4 Microwave Emission of Rough Ocean Surfaces 163
-1li-
--- PAGE 135 ---
112 4 RANDOM ROUGH SURFACE SIMULALIONS
5 Waves Scattering from Real-Life Rough Surface Profiles 166
5.1 Introduction 166
5.2 Rough Surface Generated by Three Methods 167
5.3 Numerical Results of the Three Methods 169

References and Additional Readings 175
--- PAGE 136 ---
4 RANDOM ROUGH SURFACE SIMULATIONS 113

In this chapter we study random rough surface simulations of one-
dimensional surface for two-dimensional scattering problem. The simulations
of rough surface scattering started in the late 1970’s and continue to the
present day [Axline and Fung, 1978; Thorsos, 1988; Thorsos and Jackson,
1991; Maystre et al. 1991; Devayya and Wingham, 1992; Thorsos and Jack-
son, 1989; Thorsos and Broschat, 1995; Maradudin et al. 1990; Michel and
O'Donnell, 1992; McGurn and Maradudin, 1993; Chan et al. 1991; Nieto-
Vesperinas and Soto-Crespo, 1987]. The main purposes of the early simula-
tions were to validate analytic scattering theory and to investigate backscat-
tering enhancement.

The numerical method in this chapter is based on the formulation of
integral equations and converting the integral equations into matrix equa-
tions using the method of moments. We discuss the Dirichlet problem and
Neumann problem and illustrate the results using Gaussian surfaces, sur-
faces with ocean spectrum, and fractal surfaces. Next, we discuss dielectric
surface and the calculation of emissivity for applications in passive remote
sensing. In particular, we address the accuracy issue in the calculation of
emissivity. The accurate calculation of emissivity distinguishes the emphasis
of rough surface simulations in this book. Most researchers on rough sur-
face simulations emphasize on bistatic scattering and backscattering, which
are usually measured and plotted in dB scale. For such simulations, an ac-
curacy of 25% or 1 dB is acceptable. However, for passive remote sensing
calculations, the physics is based on energy conservation, The key result in
passive remote sensing is the difference of emissivity between a rough sur-
face and a flat surface. The difference is small and can be a few percent to
Jess than 1%, For ocean remote sensing, that difference is particularly small,
e.g., 0.003 or 0.3%, This corresponds to a brightness temperature difference
of less than a Kelvin between a rough surface and a flat surface. The ability
to distinguish that small difference actually forms the basis of passive remote
sensing of ocean wind. This means that for passive remote sensing numerical
simulations, energy conservation has to be within 0.3%. Such a stringent
requirement is not necded in active remote sensing simulations, where an
energy conservation of 96% is deemed to be good. Thus numerical methods
of simulations for active remote sensing can be different from passive remote
sensing because of the large difference in accuracy requirements. Onc key im-
plication for calculations in passive remote sensing is that: the rough surface
needs to have a fine discretization. In this chapter, we will also introduce ex-
amples of real life surface profiles measured for rocky surfaces, soil surfaces,
and snow surfaces.
--- PAGE 137 ---
114 4 RANDOM ROUGH SURFACE SIMULATIONS
1 Perfect Electric Conductor (Non-Penetrable Surface)
1.1 Integral Equation
Consider an incident wave Winc(F) impinging upon a random surface
(Fig. 4.1.1) with height profile z = f(x). In two-dimensional scattcring prob-
lem F = wa: + 22, the wavefunction (7) is
UP) = Vine?) + Us(F) (4.1.1)
where w),(7) is the scattered wave. The wavefunction obeys the equation
(V7 4k?) vy =0 (4.1.2)
The two-dimensional Green’s function obeys the equation
(W? +) (7) = ~0(7 - 7") (4.1.3)
and
9(F,7') = SHS” (kr -7')) (4.1.4)
Let the spaces above and below the rough surface be denoted by region
0 (Vo) and region 1 (Vj). We use the Green’s theorem to get
[fe wovatr.r) - 97, 7V0@)
IVa
~~ I ds A: (WO)Va(r”) ~ afFF Var]
s
+ I ds i [WR)VoF) — (FF )VUR] (4.4.5)
Sx
where Sx is the surface at infinity. Using (4.1.2) and (4.1.3) in the left-hand
side of (4.1.5), we have
ih dF [b(F) (Pg FF) — 5(F -7)) +97. 7) PUR]
Yo
=- I dF 5(F =r’) HF) (4.1.6)
Jd Vo
To evaluate (4.1.6), one needs to define where 7 is. One can have F above
the rough surface or 7 below the rough surface. Note that 7” can be infinites-
imally close to the surface. If 7 is infinitesimally close but above the rough
surface, we denote it by 7,. If it is infinitesimally close but below the rough
surface, we denote it by 7_. Also
_ sim wl) ane) — J ~V7") if im region Vo
Ike OF or 7) Or) = {5 if F” in region Vi (41.7)
--- PAGE 138 ---
§1.1 Integral Equation 115
_ z
Ey
4
iat)
z= f(z)
ee ee ~ eas
€y
Figure 4.1.1 Wave impinging upon a dielectric surface,
The surface integral at infinity in (4.1.5) gives the incident wave. Thus
Vine) fds a- [wry Valr,*) ~ gtF.F)VUO)]
s
_ fur) Fev (4.1.80)
~ (0 rev (4.1.8)
The zero in (4.1.85) corresponds to the extinction theorem. Note that in
(4.1.82) and (4.1.85), 7 is on surface S while 7 is in region Vy or Vj. To
obtain integral equations, we consider the following two cases.
A. Dirichlet Boundary Condition
Dirichlet boundary condition represents the TE case of electromagnetic scat-
tering with & = 9£ and the surface is perfectly conducting.
The Dirichlet boundary condition is
w(F) =0 (4.1.9)
for F on S. Then
oh (\ aoe yoy JO) Mev (41-10a)
vine? fas or ra Wore) = {5 NET ra
If we let 7 approach the surface, we note that both (4.1.10a) and
(4.1.10) will approach zcro, Thus one does not have to distinguish between
7, and 7. For F on S, (4.1.10) takes the form of a surface integral equation
for the surface unknown 7’ - Vu)(7)
Winel?’) = [as GFF )a- Vv(r) (4.1.11)
s
Note that both 7 and 7 are on S in (4.1.11).
We also note that as F — 7”, g(7,7’) has an integrable singularity for
a one-dimensional integration. Equation (4.1.11) is also known as the EFIE
--- PAGE 139 ---
116 4 RANDOM ROUGH SURFACE SIMULATIONS
(clectric field integral equation) for TE case because ¢ represents the electric
field which points in the horizontal direction.
B. Neumann Boundary Condition
This represents a TM case when the magnetic field is 7 = 9H and the surface
is perfectly conducting. Let 7 represent H. Then the boundary condition is
a-Vo=0 (4.1.12)
From (4.1.8), we have
gl cap Cote) a UP) KEV (41.130)
vinel?)+ [ds veya Votrn7) = (9) TS ye erie
Next, we let 7 approach the surface. In this case, it makes a difference
whether one approaches the surface from above which gives (F",) or from
below which gives zero by (4.1.13b). Thus, we have
Wine(T) + [ ds i(r)r-VoF,F,) = 0) (4.1.14a)
Ss
Wine(F_) + [ ds w(F)i- Vg(F,F_) =0 (4.1.14b)
Js
In Section 1.5, we shall show that because of the singularity of Green’s
function, (4.1.14a) and (4.1.146) are consistent with each other. One can use
(4.1.14a) or (4.1.148) to solve for the surface unknown ¢(7). The discontinu-
ity of W(F_) and w(Fr"_) can be accounted for by the singularity of the normal
derivative of the Green’s function. As 7 — 7, n- Vg(7,7") is more singular
than (7,7).
1.2 Matrix Equation: Dirichlet Boundary Condition (EFIE for TE
Case)
Integral equations can be readily converted to matrix equations. The surface
integral equation for Dirichlet boundary condition is, for 7’ on S,
Vinel) = [ dsg(r,7')a- Vu(r) (4.1.15)
Ss
Note that both F and 7 are on S. On S, z = f(z) and 2! = f(x‘). Hence
(4.1.15) becomes
L | gy?
2 ; ante
vine $e) = [7 dey (Z) ale. feh2! 29) AVM) 15
. (4.1.16)
--- PAGE 140 ---
§1.2 Matrix Equation: Dirichlet Boundary Condition (EFIE for TE Case) 17
where we have limited the surface to between —L/2 to L/2. The quantity
Wine(2", f(x’) is only a function of x’. Let
b(2") = Wine(2’, F(2’)) (4.1.17)
Also let
df\? .
1+ x (A: VO) 22 p(0) = U(2) (4.1.18)
be the surface unknown. The kernel of the integral equation is
K(a',2) = g(a, f(x); 2", f(2’)) = g(a’, f(a"); 2, f(a)) (4.1.19)
Putting (4.1.17), (4.1.18), and (4.1.19) into (4.1.16), we have
L
[ da K(a',£)U (ax) = b(2’) (4.1.20)
-2
2
Next we convert (4.1.20) into a matrix equation using MoM. The domain
—L/2 < « < L/2 is divided into N intervals, cach of width A = L/N. The
intervals are centered at a,, m = 1,2,...,N. Thus U(x) = U, in the nth
interval and we point match the integral equation at 2! = 2).
First. we set ’ = 2 in (4.1.20) (point matching):
A
[ de K (itm,t)U (2) = (arm) (4.1.21)
-k
2
m=1,2,...,N. Next the integral (4.1.21) can be replaced by a summation,
assuming that U(x) is constant in each interval (pulse basis functions):
N
Ae K (emt) C0») + {ff de Kem 2)) Un) = bln) (1.22)
nem m
where m = 1,2,...,N and f,, implies integration over the mth interval. We
have to single out the mth interval because K(2,,) is singular at 7 = &m.
The second term in (4.1.22) is known as the sclf-patch contribution. For x
and 2,,, close to each other, the argument of the Green’s function is small.
For small argument w,
Ow) =142n(% 4.1.23
HOw) 1+icin (2%) (4.1.23)
where y = 1.78107. We further approximate
—f(@m) + £(@) = f'(@m)(@ — em) (4.1.24)
--- PAGE 141 ---
118 4 RANDOM ROUGH SURFACE SIMULATIONS
Thus
r Cm FAE
| dz K(xm,2) = 2/ dx K(2m,®)
m Em
ise 2. fy ;
x sf de +iZIn (Zeryi + (Fem)? )]
iAx 2 ak 2
= — {1+i-In|—Ary/1 7
{14 i2tn [ary + (rem) }
iAgr 2 ak
=— i— — 2
z {1+i2in (Zar) } (4.1.25)
where Al, = Ary/1 + (f"(2m))? is the length of the segment of the surface
that is centered at 2.
Let
U(2n) =Un (4.1.26)
b(@m) = bm (4.1.27)
Az K({tm,2n) formA~n
Amn = § idx 2 yk 4.1.28
mm — jl+i-ln Alm form =n ( )
4 7 de
Tn Section 2.3, we will describe numerical integration to obtain more accurate
matrix clements. Putting (4.1.26)-(4.1.28) into (4.1.22), we get the equation
N
SO AmnUn = bm (4.1.29)
n=1
In matrix notation, we have
AU=5 (4.1.30)
1.3 Tapering of Incident Waves and Calculation of Scattered
‘Waves
In numerical simulations, the rough surface is truncated at 2 = +L/2. This
means that the surface current is forced to be zero for |2| > L/2. If there is
an abrupt change of surface current from nonzero to zero, artificial reflection
from the two endpoints will occur. To avoid these problems, one way is to
taper the incident wave so that the incident wave decays to zero in a Gaussian
manner for large x.
--- PAGE 142 ---
§1.3 Tapering of Incident Waves and Calculation of Scattered Waves 119
A tapered incident wave is [Thorsos, 1988}
ae x + ztand;)?
Wine(F) = exp (ik(x sin 6; — z.cos 6;)(1 + w(F))) exp (Se)
(4.1.31)
where g is the tapering parameter, and the incident wave vector is
kj = k(& sin 8; — 200s 0) (4.1.32)
The choice of decay factor is dictated by the fact that the direction of con-
stant phase and the direction of constant amplitude are perpendicular. We
have
V(asin 6; — z cos 6;) - V ((x + ztand;)?) =0 (4.1.33)
Note also that at z = 0,
2
|Vine()|,-9 = xP (-3) (4.1.84)
so that it is Gaussian in the plane z = 0 and decays rapidly for |x| > g.
The additional factor in the phase, w(7) is inserted such that yinc obeys
the wave equation to a higher order. The choice of w(7) is
+ ztan 0;)2
[pict eeear _ 7
— g
wr) = — > 4.1.35
(7) (kg cos 0;)? ( )
By straightforward differentiation, it follows that
Pine, Pine . 12,
en tae t kWine
=P bind —w?- 16 sin 8; — z cos 6;)?(x + z tan 6)?
k4g8 cos® 0;
Aik(z sin 6; — zcos 6;) A(x + z tan 4;)?
{SS 1 - -—— > 4.1.36
+ k4g* cost 6; g ( 5)
The right-hand side of (4.1.36) is much smaller than |kVine|- The curly
bracket in (4.1.36) is of the order of Ogg) and is usually small for
large g and 6; not close to grazing. In numerical simulations, g is usually
chosen to be somewhere between £ to 4, depending on the incident angle.
The advantage of the analytical expression of (4.1.31) is that Wine can be
evaluated readily for any x and z. However, the right-hand side of (4.1.36)
can grow as aby as 6; > 90°. Thus Wine of (4.1.31) should not be used for
problems of low grazing angle (LGA) incidence where 0; — 90°. To calculate
--- PAGE 143 ---
120 4 RANDOM ROUGH SURFACE SIMULATIONS
the Poynting’s vector of the incident wave, note that
zs 1
3S —-——Im(V" 4.1.37
Onk mV") (4.1.37)
At z =0, by using (4.1.37) and (4.1.31), we have
(@-Bine)owo = — etn ( bing Wine (4.1.38)
‘ine)z=0 = onk Vine Oz 0 dee
2x?
LJ peoso, (t= G1 | aksin aj tan dir? | 22 (4.1.9)
=o —t | — Se Le
2nk ‘ (kg cos 6; )? k2g4 cos? 0;
The power received by the rough surface is obtained by integrating over x
from —oo to co
oe a
Pine = -/ de (5-2).-0 (4.1.40)
-0o
On integration,
cos 6; T 1+ 2tan? 6;
Pine = ——9\/541- =; Al.
me 2n oz{ 2k2g? cos? 0; (4.1.41)
A second way of tapering is to taper the incident wave in the spectral
domain. Let
2° — ke, — kin 2@2
Wine(2, 2) = iz / ~ ky chet thee exp[-Ge— Bal) (4.1.42)
The advantage of using (4.1.42) is that it obeys the wave equation exactly
since it is a spectrum of plane waves. Note that |x| can be very large while
|2| is moderate. The disadvantage of using (4.1.42) is that the vinc(x, f(x))
has to be numerically evaluated by performing the integration of (4.1.42).
The integrand in (4.1.42) can be highly oscillatory for large |2|. To avoid the
oscillatory integrand, one can carry out a numerical contour integration as
shown in Fig. 4.1.2. Let x > 0 and consider general z. Consider the domi-
ag
nant exponential factor exp(ik,x — Ee), Let ke = ki, + ik. The dominant
exponent term for large value of zx is,
en — Kix)2g?
exponent = ik, x — Gael
Mad J p )2 PP) q2
=i [ee - BL, - 7) - [xe + he = hoo) ~ Beet
Tf we let
2a
ky e
--- PAGE 144 ---
81.3 Tapering of Incident Waves and Calculation of Scattered Waves 121
ke
a
oe ‘s
-k ¢ h
| | ,
Figure 4.1.2 Contour in complex plane of ky.
then
2 , 292
a ki, — k,
exponent = ikjrr — [5 + Gate)
The exponential has constant phase and the real part decays rapidly from
Kh = kin.
The contour C consists of I), I2, and Iz in the complex ky-plane. Contour
J, is parallel to real kz-axis at a distance 22/g? above it, and Re(kz) runs
from ~oo to k. Contour Iz goes down on the left-hand side of the vertical
branch cut at k and goes up on the right-hand side of the branch cut. Contour
Jy is parallel to the Re(k,)-axis and at a distance of 2r/g? above it and runs
from k to oo.
rs
g 1 | -ikez
Dine(t, 2) = dk [e*|
incl 2) Ir la! ® ke =k 4i2e/g?
eo he biao? 2?
exp [tet a a
0
g J | tk.
tse |] ak [em]
Qn [i * hem +ida/g?
. (ki, = Kin)?g? a?
exp [ia ny e
di ka — kie)?g?
+ xf, lg of #72 prep |_ Hz = Fie)" (4.4 43)
27m Si) 4
In numerical integration, (4.1.43) converges much faster. Vor x < 0, similar
formula can be established. Note that Jy is a short contour as the “length”
--- PAGE 145 ---
122 4 RANDOM ROUGH SURFACE SIMULATIONS
of the contour normalized by k is 2{a|/(kg), which is much less than 1 even
when |z| = L.
To calculate the power impinging upon the surface, we have, from
(4.1.38) and (4.1.42)
= 1 2 poo , = fe. 2G
Sines 2= - Im al dk, eikia—i/F he xp _ (ke Kin)" g
2nk At fice 4
°° ikea-bike 2. ke — kix)?g?
. | dk, c~®®+18-*ike* exp [- (ease) (4.1.44)
50 4
On substituting (4.1.44) into (4.1.40) and integrating over dx, we get a Dirac
delta function so that ki, = k,. Because the imaginary part is taken in
(4.1.44), only propagating waves contribute to power. Thus
2 pk 22
g (ke = kix)"g
Pine = — te kz exp| ———_——+*— 4.14
ine = Ee ff the «| ; (4.1.45)
Scattered Wave
After the surface fields (7) and #-Vw(F) are calculated by numerical meth-
ods, the scattered wave can be calculated by using Huygen’s principle. We
describe general nonzero surface fields of (7) and i - Vy(F) so that the
results of the scattered wave are also applicable to the two media problem
to be treated in Section 2. From (4.1.8a), the scattered wave is
WF) = ~ [as [WFR Val(F.7) — oF.7F)A-Vd(F)] (4.1.46)
Ss
Given ¢(7) and n-V4y(¥) on the surface, 7,(7’) can be calculated by carrying
out the integration in (4.1.46).
To calculate bistatic scattering coefficients, we put 7’ in the far field. For
observation in the k, = sin#,# + cos 6,2 direction,
mot) 2] 2 it ike’ ,—ih(sin0,2-+008 0.2)
F)=-/—\ ei" @ * ° 14
GFP) WWame ‘ee (4.1.47)
Then
(n- Vo(F',7)) 1+ af i 2 ett ihr,
MO aha) dz) ~ 4V ake!
[42 assim 05)— ik cos 0, @~ih(sin Oce+-c0s 8. f(x) (4.1.48)
--- PAGE 146 ---
§1.3 Tapering of Incident Waves and Calculation of Scattered Waves 123
Putting (4.1.47) and (4.1.48) in (4.1.46), we have
bP) = i lee 5 a y)(6,) (4.1.49)
‘ AV wkr! vs . .
where
N °° df
WO) (05) = — [ daz 4 — U(x) +u(x)ik| = sin 0, — cos 0,
Joo dx
. eik(sin 0,2~f() 2086.) (4.1.50)
and u(x) = o(«,2 = f(x)) is the surface field, and U(x) = (fh Ve)z-5@@)
Vit (tp is proportional to the normal derivative of the surface field. The
Poynting’s vector in direction k, is
1 he ees
S37) = 5 (vs F VOT) (4.1.51)
Tn the far field, this becomes
s@-E (1, \wio)l" (4.1.52)
. 2n \8rkr’ } VSS _
The total power scattered is
— f aacrsar) =f ao, £() wore! ;
Pom [ dber'siet)= f° a ay (aan) ol 41.88)
The bistatic scattering coefficient o(6;) is defined so that
P, 2
a f dO, 0(8s) (4.1.54)
Pine x
giving
1 1 ° 2
i(N)
ay ankles (8s)
o(0,) = 21 ani | (4.158)
Pine
The definition of o(0.) is such that [20.016.) = 1 for non-penctrable
rough surface. For the spatial domain tapered incident wave, with Pine given
by (4.1.41), we have
Ny 2
, jw 1] as
(8s) = soky, Reosa, fy. be 2tan? A (4.1.56)
-q, |e cos _ :
BRIA] 9 CRM 2k2g? cos? 0;
--- PAGE 147 ---
124 4 RANDOM ROUGH SURFACE SIMULATIONS
For the spectral domain tapered incident. wave of (4.1.42) and (4.1.45) we
obtain
N) 2
o ws @)| as
o a, a aC Tre 15
. 2 x (ke ~ kin)?g?
Ang dkz kz exp |--————=——
-k 2

1.4 Random Rough Surface Generation
In this section, we describe how to generate realizations of random rough sur-
face. We generate Gaussian rough surfaces with Gaussian correlation func-
tion, Gaussian rough surface with band-limited ocean spectrum, and fractal
rough surface.
1.4.1 Gaussian Rough Surface
A process f(x) is Gaussian if the random variables f(x1), f(x2),.... f(@n)
are jointly Gaussian for any n, «1, £2, ..., 2n [Papoulis, 1984]. The Gaussian
process is completely characterized by the correlation function (f(x1)f(x2))
= h?C(a1, 72). If the rough surface f(x) is statistically translational invari-
ant, then C(a1,22) = C(a1 — x2). The Fourier transform of h?C(a) is the
spectral density W(k,).

To generate Gaussian random rough surfaces, we use the results from
Chapter 9, Section 2 of Volume I. We first note that from Eq. (9.2.10) of
Volume I,

(F(ke)F*(K,)) =0 (4.1.58)
for ky # ki. Thus
(F (ke) F* (kq)) = (F (kan) (F* (ke) = 0 (4.1.59)
for k, # K,. This means that F(k,) and F(k’,) are independent random
variables for ky 4 k,.
A surface of finite length L is to be generated. We make f(x) periodic
outside L, i.c., f(x) = f(x +L). A Fourier series is used to represent f(x)
li< enn
f@)=F Se tne= (4.1.60)
n=—00
where b, is a Gaussian random variable. From (4.1.60) we have
1 <2 oe gy Bante iemey
(f(a) f(w2)) = Bp ys > (bnby, ye & ee & (4.1.61)
n=—00 m=—00
--- PAGE 148 ---
§1.4 Random Rough Surface Generation 125
From (9.2.5) and (9.2.12) of Volume I,
(Ser) F(22)) = R°C(e1 ~ 22) = | * dkgei( WV (Ie.) (4.1.62)
00
Comparing (4.1.61) and (4.1.62),
(bnbd},,) = bamBn (4.1.63)
[. dhe") (fe, = z ys Bn exp (ee - »)) (4.1.64)
—00 nowoe
Let
Ak, = = (4.1.65)
Ky, = on = nAky (4.1.66)
we sample k, at K,. Then
Qn L< (a2
BES) el WK) = Ze SD Bnei) 4.1.67)
n=~00 n=—00
giving
By = 2n LW (Kn) (4.1.68)
From (4.1.63) and (4.1.68)
{| bp {?) = 29 LW (Kp) (4.1.69)
From (9.2.11) of Vohune I,
F(Ky) = F*(—Kn) (4.1.70)
Since b, is proportional to F(K,),
bp = be, (4.1.71)
Let m = —n in (4.1.63). Then
(bnb\,) = 0 (4.1.72)
and from (4.1.71) and (4.1.72)
(babn) = 0 (4.1.73)
Let
bn = Reby + ilmby (4.1.74)
Then (4.1.73) gives
((Reb,,)?) = ((Tmbn)*) (4.1.75)
(Rebp) (Imbp) = 0 (4.1.76)
--- PAGE 149 ---
126 4 RANDOM ROUGH SURFACE SIMULATIONS
Thus Reb, and Imb, are independent Gaussian random variables with vari-
ance equal to half of that of (|b,/?).
We further use a DFT (discretized Fourier transform) version of (4.1.60).
Let there be N points in both space and spectral domains
L
Ar= W (4.1.77)
and
Lm = MAX (4.1.78)
for
N N
m= — +4,..,0, 1,0. z
f(@m) = fm (4.1.79)
Then
x
1 = 2mm
fn= 5 L by exp (ea (4.1.80)
n=— $41
The inverse DFT is
x
=F > ime (4.1.81)
n= y me! > 4.1.81)
m=—S41
Equations (4.1.80) and (4.1.81) can readily be computed from FF'T. Both
Jim and by are periodic sequences with period N. That is,
nin = On (4.1.82)
Emin = Sm (4.1.83)
Hence
box = by (4.1.84)
z 2
However from (4.1.71)
bs =bx =bin (4.1.85)
2 2 zy
Then
bys is real (4.1.86)
Also from (4.1.71)
bo is real (4.1.87)
To summarize, we have by and byw, which account for two Gaussian
random numbers. Also b_» 41,b_ 2.49) +-5-2,b-1 are complex with real and
2 2
--- PAGE 150 ---
§1.4 Random Rough Surface Generation 127
imaginary parts and account for aX —1) = 2N —2 Gaussian random num-
bers. The rest of the b, can be computed as follows. The quantities b, for
n=1,2,..., x — 1 can be calculated by using the condition b, = b*,,. Other
values obey the periodic relation of (4.1.82). This is how the N independent
Gaussian random numbers are distributed to the b,’s. The algorithm is as
follows.

(i) With a given seed, get N Gaussian distributed random numbers that
have zero mean and unit variance. The IMSL subroutine is rnnor and
the MATLAB function is randn. Note that these N numbers are inde-
pendent and they need not be grouped or arranged in any order. Let the
numbers be labeled 71, 12,..., 7.

(ii) Calculate

bo = V 20 LW (Ora (4.1.88)
TN
_,fo {Pee
byx = 4/20 LW ( L \ra (4.1.89)
where a # 3 and a and # assume one of the values of 1, 2,..., N. These
use up two of the random numbers rj, r2, ---,7N+
(iii) Calculate
aaa Sl .
by = 20 L WR) {gle + iro} (4.1.90)
for n = x +1,...,-2,-1 where o,€ are distinct indices of 1,2,...,.N.
Thus (4.1.90) will use up the remaining N — 2 of the random numbers
Pe T2: ves TN:
(iv) Calculate
bn = bt, (4.1.91)
for n = 1,2,..., Xx —1 by using (4.1.90).
For gencral DFT relations
?
X(K)= Satie" (4.1.92)
ja~ $l
x
2
2(j) = x dX (he (4.1.93)
k=- X41

where X(k) and «(j) are periodic:

2(j +N) = 2(9) (4.1.94)
--- PAGE 151 ---
128 4 RANDOM ROUGH SURFACE SIMULATIONS
X(k+N) =X(k) (4.1.95)
An alternative way of writing (4.1.92)-(4.1.93)
N-1
X(k) = Yo alse (4.1.96)
=0
, Na ,
‘Va 28h jh 7
o() = 57 Do X (be (4.1.97)
k=0
Define
3G +1) = #(j) (4.1.98)
X(k +1) = X(k) (4.1.99)
Both (7) and X(k) are also periodic sequences. Then
N
X(k) = Dae EVD (4.1.10)
j=l
if a
sis) Xess k-1 4
=F 2 X(he G-Y&-1) (4.1.101)
Equations (4.1.96) and (4.1.97) and (4.1.100) and (4.1.101) are common
forms of DFT subroutines. [MATLAB utilizes (4.1.100) and (4.1.101).] We
have
X(k) = X*(-k) (4.1.102)
Then
X(k +1) = X*(-k +1) (4.1.103)
We first periodically extend b,
byw =x = Oe, (4.1.104)
for 1=1,2,..., 4-1. First let
X(n) = bp (41.105)
We can then obtain X(n) from X(n) by using (4.1.99). From X(n) we cal-
culate Z(n), n = 1,2,...,N by FFT of (4.1.101). Then we obtain z(n), n=
0,1,2,...,N — 1 from %(n) by (4.1.98). We next. periodically extend a(n).
Finally, we obtain the rough surface height profiles using
N
fn = a(n) (4.1.106)
--- PAGE 152 ---
§1.4 Random Rough Surface Generation 129
form=-4$41,...,4.
To evaluate the derivative and higher order derivatives of the rough
surface profile, one method is to evaluate by means of finite difference
A f(@m+1) ~ f(@m~1)
ny) 4.1.107
f'(m) tAn ( )
For the two endpoints m = -X +1 andm= x one can use the periodic
condition of DFT to get f(am) form = -% and m= x +1. Another method
of calculating derivatives is to differentiate (4.1.60) directly.
LS, inn 2
Ho) — Qans
f@=F bare (4.1.108)
n=—00
In terms of DFT, this becomes
x
Men) =4 > by (4.1.109)
a) =F 2 nT -L.
n=— E41
Also, the second derivative is
1 2 Qnn\? s2ennm
£"(@m) =F 2 " () et (4.1.10)
n=—S41
FET can be performed in ways similar to that of calculating fm.
Gaussian Spectrum
For Gaussian rough surface with Gaussian spectrum
(F(a) f(w2)) = WC (1 — 22) (4.111)
ey — 2g)?
= he (4.1.12)
The correlation length is related to the rms slope s by
h
l= Vo" (4.1.13)
8s
The radius of curvature is defined by (9.4.16) of Volume I. The radius of
curvature p can be estimated by calculating the fourth derivative of the
1 P
correlation function if we let is of p) & ——— aay = SE
correlation function if we let (rms of p) mus of [Pal > V3h
The Gaussian spectrum is
nL see
=e 4.1114
Wks) = 3 e ( )
--- PAGE 153 ---
130 4 RANDOM ROUGH SURFACE SIMULATIONS
op
‘| | | | |
1S iy t |
i if
mt i | I i, | |
Ba GE AA ta
Post fA uit il HE AR
4 Be eee Eda LEE EG
eo MAST a | | i
2 Wheat Eat yh ey ey
Qos UE an
£0 W | tay
ee ee |
| ee | en |
4 i
4 ‘| ! { ‘ |
325 02 015 01 005 0 005 01 015 02 02s
xin meters
Figure 4.1.3 Gaussian rough surface.
Note that the Gaussian spectrum is for 0 < jk,| < 00. In Fig. 4.1.3, we plot
the height profile with a Gaussian spectrum that has the same rms height
and rms slope of the band-limited ocean spectrum to be discussed below. For
this case h = 8.1202 x 1074 meters, s = 0.2252 and J = 5.0993 x 107* meter.
Bandlimited Ocean Spectrum
The ocean spectrum has been discussed in Chapter 4, Section 8 of Volume I.
Note that the ocean spectrum case is still a Gaussian process with the ocean
spectral density. For 2-D spectrum W (kins ky). we have
poo 20
WO(x,y) = | dhe [ dkyet®= yu Wo(ky, ky) (4.1.115)
Jox db -00
On oo oo
n= [ dxf dk pk pWo(kp) = a f dkpkpW(kp) (41.116)
0 0 0
On the other hand for 1-D spectrum,
oo
n2=2 | dk, W (Key) (41.117)
0
Also
1
/9(kp) = ——S(k, 4.1.118
Walk) = ap = SUhy) (41.118)
‘To set up a correspondence between 2-D spectrum Wo(k,) and 1-D spectrum
--- PAGE 154 ---
§1L4 Random Rough Surface Generation 131
W(k,), we compare (4.1.116) and (4.1.117). Then
W (kz) = W(|kzx|) = wkpWalkp) (4.1.119)
I(|Kpl
W (lel) = SMe) (4.1.120)
For ocean spectrum, letting W2(k,) = Wpy(k,) of (4.8.13) in Volume I (DV
stands for Durden-Vesecky) and ignoring anisotropy, S(k,) is found to be
kp
ag ( bkpu? alogia (x)
pl ky > ky
S{kp) = 4 "PX > (4.1.121)
bo ke
mee [-o (z) ky < ky
where
ge = 9 +7ke (4.1.122)
y= 7.25 x 1075 (4.1.123)
g=981 (4.1.124)
@ = 0.225 (4.1.125)
b= 1.25 (4.1.126)
ag = 0.008 (4.1.127)
kj =2m! (4.1.128)
g
ke = oo Al.
ke = Ege (41.129)
U(z)= Po in (2) (ocean wind speed at elevation z in meters)(4.1.130)
F 0
0.0000684
29 = ++ 0.00428u2 ~ 0.000443 (4.1.131)
Suppose the wind speed is 10m/s at elevation 5m, then
5
U(5) =10=“*In (<) (4.1.132)
0.4 20
We solve for uy by using (4.1.131) and (4.1.132). (Use fzero in MATLAB
to find u,.)

To perform numerical simulations, it is customary to bandlimit the ocean
spectrum. For ocean spectrum, let Wrwo(k,) be bandlimited between ky
and ky. Then

yy J Wp), ki < hp < kv os
Wawolkp) = {i otherwise (41.133)
--- PAGE 155 ---
132 4 RANDOM ROUGH SURFACE SIMULATIONS
x10"
[aT
i i} i
18} i i | \ |
i h
| | i \ oh t 1
\ {i | ii |
til) ya ia hi fl
P bh ya | I
ivi lh eh ii Nt aim
| | rep pape fly
eo ii PLL |
& la Tr ue depp ary
Bos My. fy a Wy 4
£05) Wy hl Awe ed
ee |
fa Wyoy Aly yoo i
a | i i i i |
I i
45 i | 1
2 mn
|
25
“025-02 018 O01 005 0 005 Of O15 02 025
xin meters
Figure 4.1.4 Surface profile with ocean spectrum.
For the bandlimited spectrum between ky, and ky, we can calculate the rms
height # and the rms slope s
, oo Ay
we=2 i dk,W (kr) = 2 | dk, Wrwolkz) (4.1.134)
0 fk,
Ay °
v= af dk, k2Wuwolkz) (4.1.135)
ky,
For example, for microwave scattering at 19 GHz, we can choose ky =
100m~! and ky = 4000m7!. Then for wind speed at 10 m/s, we have
h = 8.1202 x 1074 m and s = 0.2252.

In Fig. 4.1.4, we show a surface height profile created for a Gaussian
range surface with the bandlimited ocean spectrum (N = 256; Ax = X/10).
Note that Figs. 4.1.3 and 4.1.4 have the same rms height and rms slope. We
can see that the bandlimited ocean surface of Fig. 4.1.4 is more spiky than
the Gaussian spectrum surface of Fig. 4.1.3.

1.4.2 Fractal Rough Surface
For fractal surface, we can use the Weierstrass- Mandelbrot function [Berizzi
et al. 1999]. Unlike the previous two cases, the fractal surface is not a Guas-
--- PAGE 156 ---
§1.4 Random Rough Surface Generation 133
FS
2
| | | |
18 ! | | |
li | |
dd had uctalhy
pe AM AGT HH Mn |
Bo THT WE NAY
i Ln TE Ve!
Bost ania ed (yy
a Wy We yy ail |
ytd | | a
4s i \ j
Bes 02 016 01 008 0 008 01 018 02 025
xin meters
Figure 4.1.5 Surface profile for fractal surface.
sian process. The Weierstrass-Mandelbrot function is
Ny-l
(x) = hCw S> bO-2)" sin Kop" + Bp) (4.1.136)
n=0
where
h = rms height
Ny = # of tones (e.g., 100) (4.1.187)
s= fractal dimension (1 <s < 2)) (4.1.138)
2 (1 — bS-2) oo
Cy = \ 2 = normalization constant (4.1.139)
®, = phase and is a Gaussian random variable uniformly distributed
between 0 and 2m (in MATLAB use 27 *rand(Nj.1)) (4.1140)
We also bandlimit the fractal surface between ky, and ky. This means
Ky =k (4.1.141)
Kobi! sky (41.142)
so that
baer (#) we (4.1.143)
ky
--- PAGE 157 ---
134 4 RANDOM ROUGH SURFACE SIMULATIONS
In Fig. 4.1.5, we plot one height profile for ky, = 100 m7! and ky = 4000 m7!.
For this case rms height h = 8.1202 x 10~*m, and fractal dimension is
s = 1.5, We compare between Figs. 4.1.4 and 4.1.5. Both have the same rms
height h and the same ky and ky. We note that Fig. 4.1.5 of the fractal
surface is more spiky.
1.5 Neumann Boundary Condition (MFIE for TM Case)
From (4.1.13a) and (4.1.13), we have the integral equations for the Neumann
boundary condition. We let 7” approach the boundary S. If we zoom in at the
point 7’, we can have a small piece of surface of length 2a that is symmetrical
about the point 7”. This piece can be regarded as a straight line for the limit
of vanishing a (Fig. 4.1.6). Then
[ dsi(F)i- VgF,F) =f dsy(7)r- Vg (FF) + [ VAR VaR)
Ss s Jpiece
(4.1.144)
where f is the principal value integral with a vanishingly small piece sub-
tracted out from the domain of the integration. For the small piece, we
use the coordinate system X and Z that are tangential and normal to the
straight line respectively. Thus
ds=dX, i=Z, X’=0
Z=0, Z' = infinitesimal
For Z' positive, 7 is above the surface. For Z' negative, 7 is below the
surface.
[ e@a-vorr) ) [ax F )
u(r)r-Vo(F,F) = lim Jim vr) [ dX 9g (4.1.145
piece 40 |2"\=0 a OZ
Note that the order of the two limits cannot be interchanged. In the small
piece,
jF-F'] = VX? 4+ (Z- 2? (4.1.146)
ta yic w 1, (F-P|
9= GH (k|F ~ ¥"|) > 5 hn (4.1.147)
Og Z'
= = 41,148
(33). Qn(X? + (Z)?) ( )
Thus
! » [* Zz’
iF « 77) = be A AF 7
fen Vor) = tim lime 0) [OX sae + (2)
--- PAGE 158 ---
§1.5 Neumann Boundary Condition (MFJE for TM Case) 135
3 Ss
#
ee ee eee
‘a fF = (02)
j
mo X
a
Figure 4.1.6 Principal value integral obtained by subtracting a small piece around «’.
. 9 uF) _, x)" 4 (7) 1a
=lim lim YY? =| = BY tan! &
a0 |Z" [00 Qn [tan Zh ao T tan Z
1
50") for Z’>0
=o?) (4.1.149)
5h) for Z’ <0
The integral equation of (4.1.13) for * approaching the surface from region
0 then becomes
A ic\ a _ 1
Vine(®) + f dsi(F)a- Volt, 7) + 5007) =U) (4.1.150)
s
while the integral equation of (4.1.13) for * approaching the surface from
region 1 becomes
1
wine?) + f dsi(F)n- Vg (FF) — zor) =0 (4.1151)
Js
‘These two equations of (4.1.150) and (4.1.151) become identical, which mean
that Eqs. (4.1.13a) and (4.1.13b) are well explained by the singularity of the
normal derivative of the Green’s function. Equation (4.1.151) is known as
MPIE (magnetic field integral equation) because y represents the magnetic
field which is in the horizontal direction for the TM case.
Then if we let the kernel be
ay?
Ky (a!) = f 1+ (4) o-vair|
2=f(e), /=f(e')
} ay? a
~  plg
=4f/le{— “ROS 41.152
yt () ne Ron (41.152)
--- PAGE 159 ---
136 4 RANDOM ROUGH SURFACE SIMULATIONS
the surface integral equation is
io 1
Wine(x') +f dx h(a) Ky (2",2) = 5H) (4.1.153)
Joe
where Winc(2’) = Wine(2’, 2! = f(w')) and w(x) = y(2,2 = f(x)).

The integral equation is solved using the method of moment with pulse
basis functions and point matching. Let there be N intervals with length
Az for each interval. The simplest approximation of f dx is to exclude the
interval about «’. Then the diagonal matrix element is 1/2. Let

Pine(®m) = (tm) = bm (4.1.154)
b(@m) = Um (4.1.155)
—Azr Ky(%m.tn) for m#n
Brn = 4 1 (4.1.156)
5 for m=n
2
Then the matrix equation is
Y> Brnntin = Bm (4.1.157)
n
Equations (4.1.154)-(4.1.157) are of sufficient accuracy for many cases.
Note that
1 food) {Flot ~ Pla\\2
il (ky (=a) + (Fle) - J@)F)
Ky(2',2) = eee
Vee = 2)? + (fl) = FO)
»{f'(x)(@ — 2’) — (F(x) - f(x’) } (4.1.158)
To have a more accurate evaluation of the self patch of m = n, we need to
calculate
m+ SE
i= dx Ky(&m,2)
Bm — AE
2
( ey n)\2
ik f paz Hy” («V/ (em — 2)? + (f(am) — f(2)) )
= ey Sr
AS, 2 / 3 Ff \\2
Men 8 Vem — 2)? + (Fem) — Fa)?
df .
+4 Gg (@ — Bm) — (F(2) ~ F(®m)) (4.1159)
We next approximate f(x) and oe) by Taylor expansions about: 2,
,
f(a) = fam) + f'@m)(a — &m) + Lem) Gn) (x ~ xm)? (41.160)
--- PAGE 160 ---
§2 Two Media Problem 137
qj 7
GO) = Ham) + Heme en) (41.161)
Then
V (2m ~ 2) + (F@m) = F(@))? ey (em — 2)? + (Fm) (2m — 2)?
(4.1.162)
dj "(tm ‘
Fe — 2m) ~ (02) ~ Flam) =F") (am = 2) (41.163)
For small argument w
May) = 2
Hy"(w) =—-F (4.1.164)
Thus
pom + SE Lam) (a — ap 2
raf ae ea
We_— 2 (%#— Lm)? + (F'(Xm)(@m — 2))
yo ptmt "(ton
= xf dx —£n) (4.1.165)
Patan 8 OL + (F(tm))]
Since the integrand is now well-behaved, subtracting out an infinitesimally
small piece does not make any difference. Thus
A "(an
p= At_ fm) (4.1.16)
4m 1+ (f"(am))
Thus the matrix elements become, from (4.1.156) and (4.1.166),
| —Ag Ky(%m,tn) for m#n
Bun = 41 f"(@m) Ax _ (44.167)
2a TFG Gae
Tn Section 2.3, we will include numerical integration to further improve the
accuracy of the matrix elements.
2 Two-Media Problem
For the case of a two media problem where the lower medium has permit-
tivity e; (Fig. 4.1.1), we need dual integral equations. The first one is given
by (4.1.8). We also use the relation given in (4.1.149). Then we have, for 7
and 7 on S,
ined) = Gu") — fF dswlryn- Vor”) + f dsalr.r ya Vor) (42.1)
/ s
--- PAGE 161 ---
138 4 RANDOM ROUGH SURFACE SIMULATIONS
We next apply Green’s theorem to the lower medium.
(V? +k?)u1 =0 (4.2.2)
where ky = w,/ji. The Green’s function of the lower half-space gi (F,7") is
ae?) = GHD ks \F-?\) (4.2.3)
(VW? + ig (F.7') = —3(F 7’) (4.2.4)
Applying Green’s theorem,
Il & [PV GEF) — n(F.7 Van P)]
Jdy,
= [ dsti- [WiFVat?) — at )Var)
Sue
+ [asi La @ValtF) — FPF )Vor)] (4.2.5)
Ss
where fi. _, is the surface integral at infinity of the lower half-space and
contributes zero in this case.
We use (4.2.2) and (4.2.4) in the left-hand side of (4.2.5):
[fe tmv'ngr) - nerve)
vi
_ nim sie wy JO ifr €Vo
- - ff wil) 6(F- 7’) = {ou vey. (426)
Thus, we have
ms Ue ee oy oy yy _ f0 if” EVo
[es [a®a- Var) — nr )a:- Vii] = { —wi(F) ifr ev
(4.2.7)
We have a similar relation to (4.1.149). Let 5 be an infinitesimal positive
number,
[ [ devin (F)a-VaulF, "|
Js r'=(2',f(a’)£6)
1
= $5) + fas Volt?) (4.2.8)
Using this in (4.2.7) gives, for F and 7 on S,
1
SvlF) + fadsvstrya- Vane) - [ dsqi(F.F)A-Vin(F) =0 (4.29)
Equations (4.2.1) and (4.2.9) are the dual integral equations for the two-
media problem.
Progress: 180/723
Progress: 200/723
Progress: 220/723
Progress: 240/723
Progress: 260/723
Progress: 280/723
Progress: 300/723
Progress: 320/723
Progress: 340/723
Progress: 360/723
Progress: 380/723
Progress: 400/723
Progress: 420/723
Progress: 440/723
Progress: 460/723
Progress: 480/723
Progress: 500/723
Progress: 520/723
Progress: 540/723
Progress: 560/723
Progress: 580/723
Progress: 600/723
Progress: 620/723
Progress: 640/723
Progress: 660/723
Progress: 680/723
Progress: 700/723
Progress: 720/723
OCR Complete
--- PAGE 1 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
SCATTERING OF
ELECTROMAGNETIC
WAVES
--- PAGE 2 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
WILEY SERIES IN REMOTE SENSING
SS
Jin Au Kong, Editor
Asrar ¢ THEORY AND APPLICATIONS OF OPTICAL REMOTE SENSING
Crane ¢ ELECTROMAGNETIC WAVE PROPAGATION THROUGH RAIN
Curlander and McDonough * SYNTHETIC APERTURE RADAR: SYSTEMS
AND SIGNAL PROCESSING
Elachi ¢ INTRODUCTION TO THE PHYSICS AND TECHNIQUES OF
REMOTE SENSING
Haykin, Lewis, Raney, and Rossiter ¢ REMOTE SENSING OF SEA ICE
AND ICEBERGS
Haykin and Steinhardt ¢ ADAPTIVE RADAR DETECTION AND
ESTIMATION
Hord ¢ REMOTE SENSING: METHODS AND APPLICATIONS
Janssen ¢ ATMOSPHERIC REMOTE SENSING BY MICROWAVE
RADIOMETRY
Maffett © TOPICS FOR A STATISTICAL DESCRIPTION OF RADAR CROSS
SECTIONS
Steinberg and Subbaram * MICROWAVE IMAGING TECHNIQUES
Szekielda ¢ SATELLITE MONITORING OF THE EARTH
Tsang, Kong, and Shin * THEORY OF MICROWAVE REMOTE SENSING
Tsang, Kong, and Ding ¢ SCATTERING OF ELECTROMAGNETIC WAVES:
THEORIES AND APPLICATIONS
Tsang, Kong, Ding, and Ao * SCATTERING OF ELECTROMAGNETIC
WAVES: NUMERICAL SIMULATIONS
Tsang and Kong ¢ SCATTERING OF ELECTROMAGNETIC WAVES:
ADVANCED TOPICS
--- PAGE 3 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc.
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
bl
Numerical Simulations
Leung Tsang
Jin Au Kong
Kung-Hau Ding
Chi On Ao
A Wiley-interscience Publication
JOHN WILEY & SONS, INC.
New York « Chichester ¢ Weinheim © Brisbane « Singapore » Toronto
--- PAGE 4 ---
This text is printed on acid-free paper. @
Copyright © 2001 by John Wiley & Sons, Inc,
All rights reserved. Published simultaneously in Canada,
No part of this publication may be reproduced, stored in a retrieval system or transmitted in any
form or by any means, electronic, mechanical, photocopying, recording, scanning or otherwise,
except as permitted under Section 107 or 108 of the 1976 United States Copyright Act, without
cither the prior written permission of the Publisher, or authorization through payment of the
appropriate per-copy fee to the Copyright Clearance Center, 222 Rosewood Drive, Danvers, MA
01923, (978) 750-8400, fax (978) 750-4744, Requests to the Publisher for permission should be
addressed to the Permissions Department, John Wiley & Sons, Inc., 605 Third Avenue, New York,
NY 10158-0012, (212) 850-601 I, fax (212) 850-6008, E-Mail; PERMREQ @ WILEY.COM,
For ordering and customer service, call 1-800-CALL-WILEY.
Library of Congress Cataloging in Publication Data
‘Tsang, Leung.
Scattering of electromagnetic waves: Numerical simulations / L. Tsang . .. [et al.)
p. cm. — (Wiley series in remote sensing)
Includes index
ISBN 0-471-38800-9 (cloth: alk. paper)
1. Electromagnetic waves—Scattering—Mathematical models. 1. Tsang, Leung. 11.
Series.
QC665.83 S23 2000
621,36'78'015118—de21 00-040864
Printed in the United States of America,
10987654321
--- PAGE 5 ---
To my family, Hannah, Clarisse, and Kalcb for their love.
— L. Tsang
To our families.
— J. A. Kong, K. H. Ding, C. O. Ao
--- PAGE 6 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
CONTENTS
CHAPTER 1
MONTE CARLO SIMULATIONS OF LAYERED MEDIA .... 1
1 One-Dimensional Layered Media with Permittivity
Fluctuations 2
11 Continuous Random Medium 2
1.2 Generation of One-Dimensional Continuous Gaussian Random
Medium 4
1.3 Numerical Results and Applications to Antarctica 5
2 Random Discrete Layering and Applications 8
References and Additional Readings 12
CHAPTER 2
INTEGRAL EQUATION FORMULATIONS AND
BASIC NUMERICAL METHODS ........................... 18
1 Integral Equation Formulation for Scattering Problems 14
11 Surface Integral Equations 14
1.2. Volume Integral Equations 17
1.3. Dyadic Green’s Function Singularity and Electrostatics 19
2 Method of Moments 23
3 Discrete Dipole Approximation (DDA) 27
3.1 Small Cubes 28
3.2 Radiative Corrections 29
3.3 Other Shapes 31
4 Product of Toeplitz Matrix and Column Vector 37
4.1 Discrete Fourier Transform and Convolutions 38
4.2 FFT for Product of Toeplitz Matrix and Column Vector 42
= vii
--- PAGE 7 ---
viii CONTENTS
5 Conjugate Gradient Method 46
5.1 Steepest Descent Method 46
5.2 Real Symmetric Positive Definite Matrix 48
5.3. General Real Matrix and Complex Matrix 52

References and Additional Readings 57

CHAPTER 3

SCATTERING AND EMISSION BY A PERIODIC

ROUGH SURFACE ..... 2.26.26. ees G1
1 Dirichlet Boundary Conditions 62
Ll Surface Integral Equation 62
1.2. Floquet’s Theorem and Bloch Condition 63
1.3 2-D Green’s Function in 1-D Lattice 64
14 Bistatic Scattering Coefficients 67
2 Dielectric Periodic Surface: T-Matrix Method 68
2.1 Formulation in Longitudinal Field Components 69
2.2 Surface Field Integral Equations and Coupled Matrix

Equations 74
2.3. Emissivity and Comparison with Experiments 81
3 Scattering of Waves Obliquely Incident on Periodic

Rough Surfaces: Integral Equation Approach 85
3.1 Formulation 85
3.2. Polarimetric Brightness Temperatures 89
4 Ewald’s Method 93
41 Preliminaries 93
4.2. 3-D Green's Function in 3-D Lattices 98
43 3-D Green’s Function in 2-D Lattices 102
44 Numerical Results 105

References and Additional Readings 110
--- PAGE 8 ---
CONTENTS ix
CHAPTER 4
RANDOM ROUGH SURFACE SIMULATIONS............. 111
1 Perfect Electric Conductor (Non-Penetrable Surface) 114
1.1. Integral Equation 114
1.2 Matrix Equation: Dirichlet Boundary Condition
(EFIE for TE Case) 116
1.3. Tapering of Incident Waves and Calculation of Scattered
Waves 118
1.4 Random Rough Surface Generation 124
1.4.1 Gaussian Rough Surtace 124
1.4.2 Fractal Rough Surface 132
1.5 | Neumann Boundary Condition (MFIE for TM Case) 134
2 Two-Media Problem 137
2.1 TE and TM Waves 139
2.2 Absorptivity, Emissivity and Reflectivity 141
2.3. Impedance Matrix Elements: Numerical Integrations 143
2.4 Simulation Results 145
2.4.1 Gaussian Surface and Comparisons with Analytical
Methods 145
2.4.2 Dirichlet Case of Gaussian Surface with Ocean
Spectrum and Fractal Surface 150
2.4.3 Bistatic Scattering for Two Media Problem with Occan
Spectrum 151
3 Topics of Numerical Simulations 154
3.1 Periodic Boundary Condition 154
3.2. MEFIE for TE Case of PEC 158
3.3. Impedance Boundary Condition 161
4 Microwave Emission of Rough Ocean Surfaces 163
5 Waves Scattering from Real-Life Rough Surface
Profiles 166
5.1 Introduction 166
5.2 Rough Surface Generated by Three Methods 167
--- PAGE 9 ---
x CONTENTS
5.3 Numerical Results of the Three Methods 169
References and Additional Readings 175
CHAPTER 5
FAST COMPUTATIONAL METHODS FOR SOLVING
ROUGH SURFACE SCATTERING PROBLEMS............ 177
1 Banded Matrix Canonical Grid Method for
Two-Dimensional Scattering for PEC Case 179
1.1. Introduction 179
1.2 Formulation and Computational Procedure 180
1.3. Product of a Weak Matrix and a Surface Unknown Column
Vector 187
14 Convergence and Neighborhood Distance 188
1.5 Results of Composite Surfaces and Grazing Angle Problems 189
2 Physics-Based Two-Grid Method for Lossy Dielectric
Surfaces 196
2.1 Introduction 196
2.2 Formulation and Single-Grid Implementation 198
2.3. Physics-Based Two-Grid Method Combined with Banded
Matrix Iterative Approach/Canonical Grid Method 200
2.4 Bistatic Scattering Coefficient and Emissivity 203
3 Steepest Descent Fast Multipole Method 212
3.1 Steepest Descent Path for Green’s Function 213
3.2. Multi-Level Impedance Matrix Decomposition and Grouping 216
3.3. Multi-Level Discretization of Angles and Interpolation 222
3.4 Steepest Descent Expression of Multi-Level Impedance
Matrix Elements 226
3.5 SDFMM Algorithm 235
3.6 Numerical Results 242
4 Method of Ordered Multiple Interactions (MOMI) 242
4.1. Matrix Equations Based on MFIE for TE and TM Waves
for PEC 242
--- PAGE 10 ---
CONTENTS xi
42 Iterative Approach 245
4.3 Numerical Results 247
5 Physics-Based Two-Grid Method Combined with

the Multilevel Fast Multipole Method 249
5.1 Single Grid and PBTG 249
5.2 Computational Complexity of the Combined Algorithm of

the PBTG with the MLFMM 252
5.3. Gaussian Rough Surfaces and CPU Comparison 254
5.4 Non-Gaussian Surfaces 257

References and Additional Readings 263

CHAPTER 6

THREE-DIMENSIONAL WAVE SCATTERING

FROM TWO-DIMENSIONAL ROUGH SURFACES ........ 267
1 Scattering by Non-Penetrable Media 270
1.1 Scalar Wave Scattering 270

1.1.1 Formulation and Numerical Method 270
1.1.2 Results and Discussion 273
1.1.3 Convergence of SMFSIA 277
1.2. Electromagnetic Wave Scattering by Perfectly Conducting
Surfaces 278
1.2.1 Surface Integral Equation 278
1.2.2 Surface Integral Equation for Rough Surface Scattering 280
1.2.3 Computation Methods 281
1.2.4 Numerical Simulation Results 286
2 Integral Equations for Dielectric Surfaces 293
2.1 Electromagnetic Fields with Electric and Magnetic Sources 293
2.2 Physical Problem and Equivalent Exterior and Interior
Problems 296
2.2.1 Equivalent Exterior Problem, Equivalent Currents and
Integral Equations 296
--- PAGE 11 ---
xii CONTENTS
2.2.2 Equivalent Interior Problem, Equivalent Currents and
Integral Equations 298
2.3 Surface Integral Equations for Equivalent Surface Currents,

Tangential and Normal Components of Fields 300
3 Two-Dimensional Rough Dielectric Surfaces with

Sparse Matrix Canonical Grid Method 304
3.1 Integral Equation and SMCG Method 304
3.2 Numerical Results of Bistatic Scattering Coefficient 318
4 Scattering by Lossy Dielectric Surfaces with PBTG

Method 326
4.1 Introduction 326
4.2 Formulation and Single Grid Implementation 328
4.3 Physics-Based Two-Grid Method 329
4.4 Numerical Results and Comparison with Second Order

Perturbation Method 334
4.5 Numerical Simulations of Emissivity of Soils with Rough

Surfaces at. Microwave Frequencies 343
5 Four Stokes Parameters Based on Tangential Surface

Fields 350
6 Parallel Implementation of SMCG on Low Cost

Beowulf System 354
6.1 Introduction 354
6.2 Low-Cost Beowulf Cluster 355
6.3 Parallel Implementation of the SMCG Method and the PBTG

Method 356
6.4 Numerical Results 360

References and Additional Readings 366

CHAPTER 7
VOLUME SCATTERING SIMULATIONS .................. 371

1 Combining Simulations of Collective Volume

Scattering Effects with Radiative Transfer Theory 373
--- PAGE 12 ---
CONTENTS xiii
2 Foldy-Lax Self-Consistent Multiple Scattering
Equations 376
2.1. Final Exciting Field and Multiple Scattering Equation 376
2.2 Foldy-Lax Equations for Point Scatterers 379
2.3. The N-Particle Scattcring Amplitude 382
3 Analytical Solutions of Point Scatterers 382
3.1 Phase Function and Extinction Coefficient for Uniformly
Distributed Point Scatterers 382
3.2 Scattering by Collection of Clusters 389
4 Monte Carlo Simulation Results of Point Scatterers 392
References and Additional Readings 401
CHAPTER 8
PARTICLE POSITIONS FOR DENSE MEDIA
CHARACTERIZATIONS AND SIMULATIONS ............ 403
1 Pair Distribution Functions and Structure Factors 404
1.1 Introduction 404
1.2. Pereus—Yevick Equation and Pair Distribution Function for
Hard Spheres 406
1.3 Calculation of Structure Factor and Pair Distribution
Function 409
2 Percus—Yevick Pair Distribution Functions for
Multiple Sizes 411
3 Monte Carlo Simulations of Particle Positions 414
3.1. Metropolis Monte Carlo Technique 415
3.2 Sequential Addition Method 418
3.3 Numerical Results 418
4 Sticky Particles 424
41 Percus-Yevick Pair Distribution Function for Sticky Spheres 424
4.2 Pair Distribution Function of Adhesive Sphere Mixture 429
4.3. Monte Carlo Simulation of Adhesive Spheres 434
--- PAGE 13 ---
xiv CONTENTS
5 Particle Placement Algorithm for Spheroids 444
5.1 Contact Functions of Two Ellipsoids 445
5.2 Illustrations of Contact Functions 446

References and Additional Readings 450

CHAPTER 9

SIMULATIONS OF TWO-DIMENSIONAL DENSE MEDIA 453
1 Introduction 454
1.1 Extinction as a Function of Concentration 454
1.2 Extinction as a Function of Frequency 456
2 Random Positions of Cylinders 458
2.1. Monte Carlo Simulations of Positions of Hard Cylinders 458
2.2 Simulations of Pair Distribution Functions 460
2.3. Percus Yevick Approximation of Pair Distribution Functions 461
2.4 — Results of Simulations 463
2.5 Monte Carlo Simulations of Sticky Disks 463
3 Monte Carlo Simulations of Scattering by Cylinders 469
3.1 Scattering by a Single Cylinder 469
3.2. Foldy-Lax Multiple Scattering Equations for Cylinders AT6
3.3. Coherent Field, Incoherent Field, and Scattering Coefficient 480
3.4 Scattered Field and Internal Field Formulations 481
3.5. Low Frequency Formulas 482
3.6 Independent Scattering 484
3.7 Simulation Results for Sticky and Non-Sticky Cylinders 485
4 Sparse-Matrix Canonical-Grid Method for Scattering

by Many Cylinders 486
4.1 Introduction 486
4.2 The Two-Dimensional Scattering Problem of Many Dielectric

Cylinders 489
4.3 Numerical Results of Scattering and CPU Comparisons 490

References and Additional Readings 493
--- PAGE 14 ---
CONTENTS xv
CHAPTER 10
DENSE MEDIA MODELS AND THREE-DIMENSIONAL
SIMULATIONS .... 20... cence cnet een es 495
1 Introduction 496
2 Simple Analytical Models For Scattering From a
Dense Medium 496
2.1 Effective Permittivity 496
2.2 Scattering Attenuation and Coherent Propagation Constant 500
2.3. Coherent Reflection and Incoherent Scattering From a
Hal(-Space of Scatterers 505
2.4 A Simple Dense Media Radiative Transfer Theory 510
3 Simulations Using Volume Integral Equations 512
3.1 Volume Integral Equation 512
3.2. Simulation of Densely Packed Diclectric Spheres 514
3.3. Densely Packed Spheroids 518
4 Numerical Simulations Using T-Matrix Formalism 533
4.1 Multiple Scattering Equations 533
4.2 Computational Considerations 541
4.3 Results and Comparisons with Analytic Theory 545
4.4 Simulation of Absorption Coefficient 547
References and Additional Readings 548
CHAPTER 11
ANGULAR CORRELATION FUNCTION AND
DETECTION OF BURIED OBJECT........................ 551
1 Introduction 552
2 Two-Dimensional Simulations of Angular Memory
Effect and Detection of Buried Object 553
2.1 Introduction 553
2.2 Simple and General Derivation of Memory Effect 553
2.3. ACF of Random Rough Surfaces with Different Averaging
Methods 555
--- PAGE 15 ---
xvi CONTENTS
2.4 Scattering by a Buried Object Under a Rough Surface 557
3 Angular Correlation Function of Scattering by a
Buried Object Under a 2-D Random Rough Surface
(3-D Scattering) 564
3.1 Introduction 564
3.2 Formulation of Integral Equations 565
3.3 Statistics of Scattered Fields 570
3.4 Numerical Illustrations of ACF and PACF 571
4 Angular Correlation Function Applied to Correlation
Imaging in Target Detection 575
4.1 Introduction 575
4.2 Formulation of Imaging 578
4.3. Simulations of SAR Data and ACF Processing 580
References and Additional Readings 591
CHAPTER 12
MULTIPLE SCATTERING BY CYLINDERS IN THE
PRESENCE OF BOUNDARIES..................0.0.000-0.- 593
1 Introduction 594
2 Scattering by Dielectric Cylinders Above a Dielectric
Half-Space 594
2.1 Scattering from a Layer of Vertical Cylinders: First-Order
Solution 594
2.2 First- and Second-Order Solutions 603
2.3 Results of Monte Carlo Simulations 613
3 Scattering by Cylinders in the Presence of Two
Reflective Boundaries 622
3.1. Vector Cylindrical Wave Expansion of Dyadic Green’s
Function Between Two Perfect. Conductors 622
3.2 Dyadic Green’s Function of a Cylindrical Scatterer Between
Two PEC 629
3.3. Dyadic Green’s Function with Multiple Cylinders 631
3.4 Excitation of Magnetic Ring Currents 635
--- PAGE 16 ---
CONTENTS xvii
3.4.1 First Order Solution 637
3.4.2 Numerical Results 638
References and Additional Readings 640
CHAPTER 13
ELECTROMAGNETIC WAVES SCATTERING BY
VEGETATION ... 1.0.06. ep eee ees 641
1 Introduction 642
2 Plant Modeling by Using L-Systems 644
2.1 Lindenmayer Systems 644
2.2 Turtle Interpretation of L-Systems 646
2.3. Computer Simulations of Stochastic L-Systems and Input
Files 649
3 Scattering from Trees Generated by L-Systems
Based on Coherent Addition Approximation 654
3.1 Single Scattering by a Particle in the Presence of Reflective
Boundary 655
3.1.1 Electric Field and Dyadic Grecn’s Function 655
3.1.2 Scattering by a Single Particle 656
3.2 Scattering by Trees 659
4 Coherent Addition Approximation with Attenuation 667
5 Scattering from Plants Generated by L-Systems
Based on Discrete Dipole Approximation 669
5.1 Formulation of Discrete Dipole Approximation (DDA)
Method 670
5.2 Scattering by Simple Trees 672
5.3. Scattering by Honda Trees 677
6 Rice Canopy Scattering Model 685
6.1 Model Description 685
6.2. Model Simulation 689
References and Additional Readings 691
--- PAGE 17 ---
Scattering of Electromagnetic Waves

Volume I: Theories and Applications (Tsang, Kong, and Ding)
Volume II: Numerical Simulations (Tsang, Kong, Ding, and Ao)
Volume III: Advanced Topics (Tsang and Kong)
--- PAGE 18 ---
PREFACE

Electromagnetic wave scattering is an active, interdisciplinary arca of
research with myriad practical applications in fields ranging from atomic
physics to medical imaging to geoscience and remote sensing. In particular,
the subject of wave scattering by random discrete scatterers and rough sur-
faces presents great theoretical challenges due to the large degrees of freedom
in these systems and the need to include multiple scattering effects accu-
rately. In the past three decades, considerable theoretical progress has been
made in elucidating and understanding the scattering processes involved in
such problems. Diagrammatic techniques and effective medium theories re-
main essential for analytical studies; however, rapid advances in computer
technology have opened new doors for researchers with the full power of
Monte Carlo simulations in the numerical analysis of random media scatter-
ing. Numerical simulations allow us to solve the Maxwell equations exactly
without the limitations of analytical approximations, whose regimes of va-
lidity are often difficult to assess. Thus it is our aim to present in these three
volumes a balanced picture of both theoretical and numerical methods that
are commonly used for tackling electromagnetic wave scattering problems.
While our book places an emphasis on remote sensing applications, the ma-
terials covered here should be useful for students and researchers from a
variety of backgrounds as in, for example, composite materials, photonic de-
vices, optical thin films, lasers, optical tomography, and X-ray lithography.
Introductory chapters and sections are also added so that the materials can
be readily understood by graduate students. We hope that our book would
help stimulate new ideas and innovative approaches to electromagnetic wave
scattering in the years to come.

The increasingly important role of numerical simulations in solving elec-
tromagnetic wave scattering problems has motivated us to host a companion
web site that contains computer codes on topics relevant: to the book. These
computer codes are written in the MATLAB programming language and
are available for download from our web site at www.emwave.com. They are
provided to serve two main purposes. The first is to supply our readers a
hands-on laboratory for performing numerical experiments, through which
the concepts in the book can be more dynamically relayed. The second is
to give new researchers a set of basic tools with which they could quickly
build on projects of their own. The fluid nature of the web site would also
allow us to regularly update the contents and keep pace with new research
developments.

— xix —
--- PAGE 19 ---
xx PREFACE

The present volume covers numerical simulation techniques and results
for electromagnetic wave scattering in random media and rough surfaces.
Due to the large degree of freedom associated with these systems, especially
for 3-D scattering problems, fast computational methods are essential for
maximizing returns from limited computational resources. Indeed, the sub-
ject of numerical electromagnetics has scen explosive growth in recent years.
For lack of space, we choose to focus here on methods and techniques which
are more directly related to our own research.

We begin in Chapter 1 with Monte Carlo simulations of a simple one-
dimensional random medium — a layered medium characterized by permit-
tivity fluctuations. Simulation results are used to explain passive remote
sensing, measurements of the Antarctic firn. For two- and three-dimensional
scattering, it is advantageous to formulate the problem in terms of surface
integral equations where the unknowns are confined to a lower dimension-
ality. Numerical solutions of surface integral equations are often obtained
through the method of moments (MoM). We also discuss a useful technique
known as the discrete dipole approximnation (DDA) for solving volume inte-
gral equation. The DDA can be used to model inhomogeneous, irregularily
shaped object by discretizing it as a collection of point dipoles. In MoM and
DDA, numerical solutions are obtained by approximating the integral equa-
tions with a sct of linear equations. Thus matrix computation is an essential
aspect of numerical electromagnetics. When the size of the system becomes
very large, direct matrix inversion becomes inefficient, and iterative meth-
ods such as the conjugate gradient methods are often used instead. Iterative
methods usually require repeated computations of matrix-vector multiplica-
tion, and for problems with translational invariance, it is possible to utilize
fast Fourier transform (FFT) to speed up this operation. The use of FFT
in conjunction with iterative solvers is the cornerstone of fast computational
methods introduced later in this book. Therefore we discuss these topics at
some length in Chapter 2.

The remainder of the book is divided into two main parts. Chapters 3-6
deal with simulations of rough surface scattering, while volume scattering
simulations involving random discrete scatterers are studied in Chapters 7
13 (except Chapter 11 -— which contains aspects of both rough surface and
volume scattering). The topic of electromagnetic wave interactions with
rough surfaces has important applications in microwave remote sensing of
ocean surface, geophysical terrain, and agricultural fields as well as in the de-
sign and manufacturing of optical systems and X-ray lithography. In Chap-
ter 3, we discuss scattering and emission by periodic rough surfaces. Two
--- PAGE 20 ---
PREFACE xxi
solution methods are used to solve this problem. The first is the T-matrix
method, which makes use of Floquet mode expansions and the extended
boundary condition. The T-matrix formulation is exact, but the resulting
equations become ill-conditioned when the surface is very rough. The sec-
ond method uses a surface integral equation approach with MoM. Although
computationally more intensive than the T-matrix method, the surface inte-
gral cquation approach is applicable to surfaces with deep corrugation. We
also describe Ewald’s method for speeding up calculations of the Green’s
function in periodic medium. This has applications in active rescarch areas
such as frequency selective surfaces and photonic bandgap materials.

In Chapter 4, we discuss one-dimensional random rough surface scat-
tering. The core ideas behind rough surface scattering simulations are in-
troduced here. We describe in details the discretization procedure for the
surface integral equations in the Dirichlet, Neumann, and two-media prob-
lems. Numerical methods for generating Gaussian and fractal rough surface
profiles are described. The issue of truncating the rough surface and limiting
the computational domain is also an important one. We discuss two popular
approaches. The first approach uses a tapered incident wave that illumi-
nates only a part of the entire rough surface, while the second approach uses
a periodic boundary condition. As described in Volume I, random rough
surfaces are often characterized by their power spectra. This is convenient
for theoretical work, but how well does it model reality? We include discus-
sion of wave scattering from real-life rough surface profiles. In addition to
simulating bistatic scattering from rough surfaces, we also take an in-depth
look at emissivity calculations based on rough surface simulations, which
impose much more stringent energy conservation requirement.

Chapters 5 and 6 are devoted respectively to fast computational meth-
ods in 1-D and 2-D rough surface scattering simulations. The development
of fast computational methods is particularly important in scattering by
2-D rough surfaces (3-D scattering problem) where the number of unknowns
can quickly escalate as we increase the surface size. Since real-life surfaces
are 2-D, we emphasize in this book fast computational methods that can
be applied to scattering by both 1-D and 2-D rough surfaces. We introduce
the sparse matrix iterative approach with canonical grid (SMCG). In this
method, the impedance matrix is split into a strong part that consists of
near-neighbor interactions and a weak part that consists of all the rest. An
iterative scheme such as the conjugate gradient method is adopted to solve
the matrix equation. The strong matrix is sparse and can be easily handled.
However, the weak interactions require the multiplication of the dense weak
--- PAGE 21 ---
xxii PREFACE
matrix with successive iterates and could therefore present a major compu-
tational bottleneck. To speed up such calculations, the concept of canonical
grid (CG) is introduced. The essential nature of CG is that it is translation-
ally invariant. In rough surface scattering problems, the CG is usually taken
to be the mean flat surface. By translating the unknowns to the CG, the
weak interactions can be performed simultancously for all unknowns using
FFT. This reduces memory requirements from O(N?) to O(N) and opcra-
tion counts from O(N?) to O(N log N). We also introduce the physics-based
two-grid (PBTG) method for dealing with lossy dielectric surfaces. In this
method, a dense grid suitable for the lower half-space and a coarse grid
suitable for the upper half-space are chosen. By taking advantage of the
attenuative nature of the Green’s function in the lower half-space and the
slowly varying nature of the Green’s function in the upper half-space with
respect to the dense grid, one can achieve the accuracy of a single dense grid
with the computational efficiency of a single coarse grid. Other fast methods
discussed and illustrated in Chapter 5 include the steepest descent fast mul-
tipoles method (SDFMM) and the method of ordered multiple interactions
(MOMI).

Tn contrast to rough surface scattering, volume scattering involving
dense distributions of discrete scatterers is often a full-fledged 3-D scat-
tering problem. The additional degree of freedom makes direct simulations
of scattering coefficients rather difficult. Radiative transfer theory is com-
monly used for such problems, but the conventional approach fails to take
into account of coherent multiple interactions between the scatterers. A
better approach is to perform the scattering simulations on a test volume
that contains a large number of scatterers but forms only a small part of
the whole system. Coherent interactions are captured through the simu-
lated extinction coefficients and phase functions, which can then be used
in the dense medium radiative transfer equation (rigorously derived in Vol-
ume III) to solve the large-scale problem. These concepts are discussed in
Chapter 7, where idealized randomly distributed point scatterers are used to
illustrate the methods. The multiple scattering problem is formulated using
the Foldy-Lax self-consistent equations.

In a dense medium, the correlation of scatterer positions could signifi-
cantly affect the scattering results. The pair-distribution fimction quantifies
the two-particle correlation property of the scatterers. In Chapter 8, we
introduce the Percus Yevick equation for the pair-distribution function and
give closed-form solutions for hard and sticky spheres. For Monte Carlo sim-
ulations, statistical realizations of scatterer configurations are needed. Two
--- PAGE 22 ---
PREFACE xxiii
methods are commonly employed to generate the particle positions: sequen-
tial addition and Metropolis shuffling, the latter method being more efficient
when the particles are very closely packed. We show simulation results of the
pair distribution functions for hard spheres and spheroids as well as sticky
spheres. The simulated pair distribution functions are found to compare
well with the Percus: Yevick pair distribution functions. Before dealing with
3-D dense media scattering, it is instructional to first study. in Chapter 9,
the simpler problem of 2-D dense media scattering, where the volume scat-
terers are chosen to be infinitely long cylinders. We describe analytical pair
distribution function and Monte Carlo simulations of particle positions in
the 2-D case. The Foldy-Lax multiple scattering equations are then used to
simulate extinction coefficients for densely packed hard and sticky cylinders.
Finally, the SMCG method used in rough surface scattering is generalized
to the volume scattering simulations. In Chapter 10, we perform 3-D dense
media scattering calculations with diclectric spheres and spheroids. The
volume integral equation approach as well as the T-matrix approach based
on the Foldy-Lax equations are described in details. Simulation results for
the extinction coefficients and phase matrices are shown and compared with
analytical approximations.

In Chapter 11, we describe the novel correlation phenomenon in random
media scattering known as the memory effect, which manifests itself in wave
scattering through the angular correlation function (ACF). ACF has been
discussed in Chapter 6 of Volume I in the context of single scattering by
point scatterers. Here, we provide a general derivation of the memory effect
based on the statistical translational invariance of the random medium. The
special property of ACF for random medium makes it a good candidate for
the detection of a target embedded in random clutter. We explore such ideas
by studying targets buried under rough surface and volume scatterers.

The subject of multiple scattering by finite cylinders has important ap-
plications in the remote sensing of vegetation as well as signal coupling
among multiple vias in high frequency circuits. In Chapter 12, we con-
sider scattering by vertical cylinders in the presence of reflective boundaries,
which introduce additional complications. We discuss Monte Carlo simu-
lations of these systems as well as simple analytical results that take into
account of first and second order scattering. In Chapter 13, more realistic
modeling of vegetation structures through stochastic Lindenmayer systems
are presented. We compare scattcring results from such systems obtained
using the methods of DDA, the coherent addition approximation, and indc-
pendent scattering.
--- PAGE 23 ---
xxiv PREFACE
This book should provide a good mix of basic principles and current
research topics. An introductory course in Monte Carlo simulations can
cover most of Chapters 1, 2, 4, 5, 7, and 9.
Acknowledgments
We would like to acknowledge the collaboration with our colleagues and grad-
uate students. In particular, we wish to thank Professor Chi Chan of City
University of Hong Kong, Professor Joel T. Johnson of Ohio State University,
Dr. Robert T. Shin of MIT Lincoln Laboratory, and Dr. Dale Winebrenner
of University of Washington. The graduate students who completed their
Ph.D. theses from the University of Washington on random media scatter-
ing include Boheng Wen (1989), Kung-Hau Ding (1989), Shu-Hsiang Lou
(1991), Charles E. Mandt (1992), Richard D. West (1994), Zhengxiao Chen
(1994), Lisa M. Zurk (1995), Kyung Pak (1996), Guifu Zhang (1998), and
Qin Li (2000). Much of their dissertation works are included in this book.
Financial supports from the Air Force Office of Scientific Research, Army
Research Office, National Aeronautics and Space Administration, National
Science Foundation, Office of Naval Research, and Schlumberger-Doll Re-
search Center for research materials included in this book are gratefully
acknowledged. We also want to acknowledge the current UW graduate stu-
dents who have helped to develop the numerical codes used throughout this
book. These include Chi-Te Chen, Houfei Chen, Jianjun Guo, Chung-Chi
Huang, and Lin Zhou. Special thanks are also due to Tomasz Grzegorezyk
for proofreading on parts of the manuscript and Bac-Ian Wu for production
assistance.
Leung Tsang
Seattle, Washington
Jin Au Kong
Cambridge, Massachusetts
Kung-Hau Ding
Hanscom AFB, Massachusetts
Chi On Ao
Cambridge, Massachusetts
February 2001
--- PAGE 24 ---
SCATTERING OF
ELECTROMAGNETIC
WAVES
--- PAGE 25 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao
Copyright © 2001 John Wiley & Sons, Inc.
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
Chapter 1
MONTE CARLO SIMULATIONS OF LAYERED MEDIA
1 One-Dimensional Layered Media with Permittivity
Fluctuations 2
1.1 Continuous Random Medium 2
1.2. Generation of One-Dimensional Continuous Gaussian Random
Medium 4
1.3 Numerical Results and Applications to Antarctica 5
2 Random Discrete Layering and Applications 8
References and Additional Readings 12
--- PAGE 26 ---
2 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA
1 One-Dimensional Layered Media with Permittivity Fluc-
tuations
We study Monte Carlo simulations of solutions of the Maxwell equations in
Volume II. The simplest case of random medium is one where the permit-
tivity is a random function of positions in a one-dimeusional problem. In
Fig. 1.1.1, we show a stratified medium of many layers. The permittivity
fluctuates from layer to layer. The basic theory of waves in layered medium
was covered in Chapter 5 of Volume I. Nevertheless, even in this simple case,
there can be two distinct kinds of layering. The first kind is a continuous
random medium in which the random medium permittivity e(z) is a random
process that is a continuous function of z. The second kind is discrete layer-
ing in which there are abrupt changes of permittivity from layer to layer. To
further illustrate the difference, we apply both models to thermal emission of
a layered medium and make a comparison with observed brightness tempera-
tures of Antarctica. We found that in order to match the observed brightness
temperatures, the two models have to use drastically different physical pa-
rameters. The results illustrate the difference between a continuous random
medium and a discrete random medium.
| z
te
€3
°
°
° ——___
— €N-2
— -—__ N= 1
€N
Figure 1.1.1 Stratified medium with permittivity fluctuations from layer to layer.
1.1 Continuous Random Medium
A common approach is to assume a Gaussian random process of the permit-
tivity fluctuations. Figure 1.1.2 illustrates a realization of Gaussian random
process as a function of position. The density of snow is used for illustration.
--- PAGE 27 ---
$1.1 Continuous Random Medium 3
0.5
5
So.
2
>
a
a
g
9
a
0.3
9-2 50 100 150 200 250
Depth (cm)
Figure 1.1.2 A single realization of a continuous Gaussian random profile with a mean
density of 0.4 g/em®, a correlation length of 2 mm, and a standard deviation in density of
0.0156 g/cm’.
For layered random media, one can assume €(z) as a one-dimensional Gaus-
sian random process with mean ¢,, and variance o? = ée?,. The probability
density function is
L (€=¢m)?
P(e) = = exp — (1.1.1)
V2xo 20?
Let z1 and zg be two positions and let €; = €(z1) and eg = €(z2). Then
the joint probability density function is
1 1 2
(EL; €2) = > ONP sas (a —&m)
Qna® V1 =r? 207(1 — r?)
‘ 2 5
= 2r(€, ~ €m)(€2 — &m) + (2 — em) )| (1.1.2)
where r is the correlation coefficient that depends on |z; — 29]. If the corre-
lation coefficient is of exponential form, then
za — 22| :
r(z1 — z2) =exp (-B*) (1.1.3)
--- PAGE 28 ---
4 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA

where l, is the correlation length. Let €(z) = €(z) — ém be the fluctuating

part of the permittivity. Then the covariance function of the permittivity is
22!

(es(zJes(2’)) = be? exp (=) (1.1.4)
where angular bracket denotes average. Given a realization of permittivity
profile, we can discretize the medium into fine layers (say up to 30,000 layers).
We note that in Fig. 1.1.2 of the Gaussian random process, the perinittivity
is a continuous function of depth.

1.2 Generation of One-Dimensional Continuous Gaussian Ran-
dom Medium
If we assume that f(z) is a real Gaussian process with normalized correlation
function C(z). Then
(F(2)f(2)) = #C(z— 2!) (1.1.5)
Let W(K) be the spectral density
oo
o2C(2) = | ake W(K) (1.1.6)
Lope
W(K)= =| dzo?C(z)e (1.1.7)
2m Jocc
For the case that the correlation is exponential
C(z) = exp (-2) (1.1.8)
the spectral density is
oo ol
W(K) = ——a 1.1.9
(K) a 1+ kK? ( )
Let the sample be generated for 0 < z < L. Outside L, we can assume that
cs(2) is periodic. Then using a Fourier series,
12
inns
f= VE ne (1.1.10)
n=—06
The discretization is
AK =" (1.11)
2rn
Kn = at =nbK (1.1.12)
--- PAGE 29 ---
§1.3 Numerical Results and Applications to Antarctica 5
The 6,’s are complex and
co
(fate) =f" akeKo w(K)
J-co
1 jan en
=p SOY bnbs ee (1.1.13)
nom
=> PE eles) (Ky) (1.1.14)
n
Thus
(bnb%,) = bnm 2 LW (Kn) (1.1.15)
Since f is real,
bn = bh, (1.1.16)
(|Pnl?) = (Sal?) = eLW (Kn) (1.1.17)
where 6, = 6f, +76. The real and imaginary parts are independent Gaussian
random variables. Thus (b,5%,) = (bnbn) = 0. Let L be divided with N
intervals,
L
Az=—= Ll
oN (1.1.18)
and N be a power of 2.
N/2
1 ,2nnl
fed =F x b, exp (75") (1.1.19)
n=—N/241
Then bo and by» are real. We first obtain N independent Gaussian random
numbers with zero mean and unit variance. We next multiply the numbers
by a normalization factor to bo, by 2, 6}, and bf with n = 1,2,...,N/2-1,
such that (1.1.17) holds. We then use
bin = by (1.1.20)
to get b, with n = —1,—2,...,-N/2+ L. The permittivity is then calculated
by (1.1.19).
1.3 Numerical Results and Applications to Antarctica
In this section we illustrate the numerical results and application to the
Antarctic firn. The Antarctic firn has a layering structure. The permittivity
of snow is around 1.5¢,. Thus if a half-space medium is assumed, the reflec-
tivity at #, = 0 is 0.01 so that with T = 240 K, the brightness temperature
is 237.6 K. However, the measured brightness temperature is significantly
--- PAGE 30 ---
6 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA
less than that. The difference can be attributed to the reflections by the
layering structure. Snow is a mixture of ice and air, so that the density of
snow p indicates the fractional volume of ice in snow. Ice has a density of
0.91 g/cem®. The density of snow is
p=0.91 f (1.1.21)
where f is the fractional volume of ice in snow. We model p(z) as a random
process. First we assume that p(z) is a Gaussian random process with
(0) = pm (1.1.22)
p(Z) = Pm + pp (2) (1.1.23)
’ lar = zal ‘
(ps(a)py(z2)) = 0? exp(—E (1.1.24)
In Fig. 1.1.2 we show a simulated density profile of a single realization using
1, = 2 mm, o, = 0.0156 g/cm’, and p, = 0.4 g/om®. The continuous profile
of each realization is generated down to a depth of 21 m and is discretized
with 2!4 = 32, 768 layers. This gives a Az discretization thickness of 0.6 mm.
The permittivity of cach layer is calculated using the following empirical
mixing formula for dry snow
é 1.60p
—=1+—_ 11.25
0 1—0.35p ( )
ell F
— = + (0.52 p + 0.62 p?) (1.1.26)
fo 0
where ¢//,, is the imaginary part of the permittivity of pure ice and is tempera-
ture-dependent. If a) < pm. we can linearize (1.1.25) and (1.1.26), so that
é, and pm are related by the same relation as in (1.1.25) and ¢, and pm are
telated by the same relation as in (1.1.26).
en 1.60pm
t= 1+——_—_ 1.1.274.
£0 1— 0.35pm ¢ )
de 2
=H = (0.52pm + 0.62p?,) (1.1.27b)
60 €o
Let € =m +f. Then cs, the fluctuating part is
é 1.60
f :
+= —__—_, 1.1.28
co 00.85 pe (11.28)
elt
fx Mee (0,52 + 1.24 pn)oy (1.1.29)
fo £0
The permittivity fluctuation is also a Gaussian random process.
--- PAGE 31 ---
§1.3 Numerical Results and Applications to Antarctica 7
250

* eS

‘ou WERT Mr

: VITA

A Ve TAY out

i 7 i rn i |

Paso ue i! IN

: NAN,

H . “wl

3 —— 200 Realizations Vi i

gi00p --~— 1 Realization I \

‘ ------ 1 Realization ‘

50 10 20. 30 40 5060 70 80
view angle (deg)

Figure 1.1.3 Computed brightness temperatures using fluctuation dissipation theory and
a discretized continuous Gaussian random density profile with a mean density of 0.4 g/em®,
a correlation length of 2 mm, and a standard deviation in density of 0.0156 g/cm®. The tem-
perature profile is: T(z) = 222+34 exp(0.81 z) (2 is 0 at the top and negative in the medium).
Both profiles are carried down to a depth of 21 m. and are discretized into 32.768 layers,
giving @ layer thickness of 0.6 mm. Both vertically and horizontally polarized brightness
temperatures are shown, with Ty > Th.

The brightness temperature of such a profile is then calculated using
the layered medium model of Chapter 5 of Volume I. The layered medium
model also accounts for a temperature profile. The temperature profile is
assumed to have the form of T, + Tp exp(7z). This form of temperature pro-
file is characteristic of Antarctic firn in the summer. We use Eqs. (5.2.36a)
and (5.2.36b) of Volume I to compute the brightness temperature. Figure
1.1.3 shows the brightness temperatures of two different realizations which
have the same correlation length and variance as the realization shown in
Fig. 1.1.2. A single realization of permittivity profile means that a single
sample of random permittivity fluctuation is produced. The brightness tem-
peratures are then computed. Since the layered medium model is based on a
coherent approach, the results have to be averaged over many realizations. In
areal-life situation, there can be built-in incoherence. For example, the inter-
faces of the layered structure can be rough with rms height larger than 1/16
of a wavelength so that the reflection is rendered incoherent. In Fig. 1.1.3,
we also show the brightness temperature averaged over 200 realizations. The
--- PAGE 32 ---
8 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA
averaging shows that all the coherent oscillations have been smoothed out in
the average. However, in order to produce a significant amount of decrease in
brightness temperature due to reflection, a small correlation length of 2mm
is required as shown in Fig. 1.1.2. The reasons are that the permittivity in
a Gaussian random process is a continuous function of z. As we sec in some
of the examples in Chapter 5 of Volume I, a continuous profile usually does
not produce much reflection. In order to produce reflection, the continuous
profile must have a substantial change of permittivity over a short distance,
say 2 mm. Over a long distance of 2.5 m, this means more than 1200 re-
flections. Thus to match brightness temperature experimental data, a small
standard deviation of 0.0156 g/cm’ is used for the density fluctuations. This
will reduce the amount of power reflections for cach reflection. Hence, the
choice of parameters of 1, = 2 mm and \/(p;2) = 0.0156 g/cm? is dictated
by the underlying assumption of Gaussian random process.

By choosing the parameters of the Gaussian random process, we can
get reasonable brightness temperatures. However, the question is whether
these physical parameters are reasonable. In the next section we discuss the
discrete layering model.

2 Random Discrete Layering and Applications

The ground truth measurements of snow density profile have been taken
by Rott et al. [1993]. Figure 1.2.1 illustrates the results for the station at
Vestestraumen. The profiles indicate discrete layering with layer thickness of
the order of 5 cm. Abrupt changes of densities are associated with discrete
layering. The ground truth layering geometry docs not correspond to the
continuous Gaussian random process that is discussed in Section 1. Thus
a satisfactory theory needs to (1) give an accurate and correct solution of
Maxwell's equations; (2) match experimental measurements, and (3) use a
correct medium characterization with parameters that are verified by ground
truth measurements.

To incorporate ground truth data on the density profile, we apply a
centimeter discrete layering model instead of a millimeter correlation length
continuous random medium model. The measured profile in Fig. 1.2.1 shows
a background trend of the form 1 — exp(éz) (z < 0) which saturates below
about 1 m of depth. A theoretical profile similar to the measured profile
can be generated using two random variables and a background exponential
trend. The two random variables are the layer thickness and the density.
The layer thickness is assumed to be exponentially distributed. The layer-to-
--- PAGE 33 ---
§2 Random Discrete Layering and Applications 9
0.5
3
$ 0.4
p
0.3
0.2 30 Too 750 200 750
Depth (cm)
Figure 1.2.1 The snow density profile measured by H. Rott at Vestestraumen. The profile
was obtained by measuring the average density in consecutive 5-cm layers.
layer density variations are assumed to be normally distributed and are then
superimposed on top of the background exponential profile. The profile is
carried down to 10-m depth. Below this depth, layered scattering is expected
to drop off. The temperature profile is again assumed to have the form of
T.+T), exp(yz). Since the measurements were made in the Antarctic summer,
the temperature distribution decays from a high temperature at the surface
down to the mean annual temperature at depths greater than 10 m. Figure
1.2.2 shows two sample theoretical profiles generated. The layer thickness is
exponentially distributed with a mcan layer thickness of 4.1 em. The density
is
p(z) = 0.25 + 0.16 [1 — exp(0.05z)| + py(z) (1.2.1)
with z in centimeters. The fluctuating part ps(z) is normally distributed with
standard deviation of of 0.04 g/cm*. Both parameters of layer thickness and
density fluctuation are very different from that of the continuous random
medium model. The continuous random medium model used 1; = 2m and
density fluctuation of 0.0156 g/cm*. Figure 1.2.3 shows the corresponding
histogram of the densities in a theoretical profile along with the histogram
of the actual densities. The background exponential profile was set to pro-
vide the correct density level in the theoretical profile. Using the layered
medium model, the theoretical brightness temperatures for a range of ob-
--- PAGE 34 ---
10 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA
0.8
Bon | L
=
3
i
o3f
oe 30 Too 150 700380
Depth (cm)
Figure 1.2.2 Two sample realizations of a discrete random profile. The profiles are generated
with an exponential distribution of layer thickness and a mean thickness of 4.1 cm. The
density in each layer is the sum of a deterministic part given by 0.25 (g/em*) + 0.16(1 —
exp(z/(20 em)))(g/em*) and a normally distributed random variable with zero mean and a
standard deviation of 0.04 g/cm? (2 is 0 at the top and negative in the medium). For display
purposes, the resulting profile is then averaged over 5-cm intervals just as Rott’s measured
profile was (see Fig. 1.1.2). Calculation of brightness temperatures uses the original profile
without the 5-cm averaging.
servation angles are computed and averaged over many realizations. Figure
1.2.4 shows the results when 600 such realizations are averaged. The mea-
sured brightness temperatures are also shown in Fig. 1.2.4, along with the
results which would be expected from a uniform density profile and the same
temperature profile. The layered scattering model gives good agreement of
brightness temperature with the measured results out to an observation an-
gle of 50°. Note that the discrete layering used by the theory (Fig. 1.2.2) is
statistically similar to the observed profile (Fig. 1.2.1). No ad-hoc correction
factors are required. The half-space model of uniform density does not give
adequate results. The half-space model results show much less polarization
contrast. The half-space model of homogencous density gives much higher
brightness temperatures that does not agree with experimental observations.
These simulations show that layer scattering with centimeter layer thickness
is an important phenomenon at C-band passive remote sensing of Antarctica.
Extensions have been made to a Poisson process with a modified spectral
density. Good agreement with data have also been found for Vestestraumen,
Amundsen Ice and Base Camp stations [West, 1994].
--- PAGE 35 ---
§2 Random Discrete Layering and Applications 1
as
—— measured profile
0.4 ~w-— 1 Theoretical realization
>
i
i
$0.3
3
k
H
3 0.2
i dil
an 4
OAT WA
oo ta 0.4 0.5 0.6
Density (g/em*3)
Figure 1.2.3 A histogram of the measured density profile superimposed on a histogram of
one realization of a density profile using the discrete random profile described in Fig, 1.2.2.
250
4 200 ° 3
1 |
i °
3
§1so ———— Averaged discrete layering
8
3
q --- constant density profile
&
© © © bate
200 20 30 40 50 60 70 eo
View Augle (deg)
Figure 1.2.4 A comparison of the measured brightness temperatures with theoretical
results using the discrete random profile described in Fig. 1.2.2. Average layer thickness
is 4.1 em, standard deviation of density variation is 0.04 g/cm’, and a background trend is
given by 0.25 (g/em*) +0.16(1—exp(z/(20 cm)))(g/cem?). The temperature profile is: T(z) =
234 2+ 2dexp(0.81 z) (z is O at the top and negative in the medium). Both profiles are carried
down to a depth of 10 1n. Vertically and horizontally polarized brightness temperatures are
shown, with Ty > Tj at all viewing angles.
--- PAGE 36 ---
42 1 MONTE CARLO SIMULATIONS OF LAYERED MEDIA
REFERENCES AND ADDITIONAL READINGS

Fung, A. K. (1994), Microwave Scattering and Emission Models and Their Applications,
‘Artech House, Norwood, Massachusetts.

Gurvich, A. S., V. L. Kalinin, and D. T. Matveyer (1973), Influence of the internal structure
of glaciers on their thermal radio emission, Alm. Oceanic Phys. USSR, 9, 713-717.
Hall, D. K. and J. Martinec (1985), Remote Sensing of Snow and Ice, Chapman and Hall,

London.

Kong, J. A. (1990), Electromagnetic Wave Theory, 2nd edition, John Wiley & Sons, New
York,

Mitzler, C. (1987), Applications of the interaction of microwaves with the natural snow cover,
Remote Sens. Rev., 2(2), 259-387.

Rott, HL, K. Sturm, and H. Miller (1993), Active and passive microwave signatures of Antare-
tic firn by means of field measurements and satellite data, Annals of Glaciology, 17,
337-343,

Sheng, P., B. White, Z-Q. Zhang, and G. Papanicolaou (1990), Wave localization and mul-
tiple scattering in randomly-layered media, in Scattering and Localization of Classical
Waves in Random Media, edited by P. Sheng, 563 619, World Scientific, Singapore

Stogryn, A. (1970), The brightness temperature of a vertically structured layer, J. Geophys.
Res., 80, 4484-4496.

Tsang, L. and J. A. Kong (1975), The brightness temperature of a half-space random medium
with nonuniform temperature profile, Radio Sci. 10(12), 1025-1033.

Tsang, L., J. A. Kong, and R. T. Shin (1985), Theory of Microwave Remote Sensing, Wiley-
Interscience, New York.

Tsang L., E. Njoku, and J. A. Kong (1975), Microwave thermal emission from a stratified
medium with nonuniform temperature distribution, J. Appl. Phys., 46(12), 5127-5133.

Ulaby, F. T., R. K. Moore, and A. K. Fung (1981), Microwave Remote Sensing: Active and
Passive, 1 and 2, Addison-Wesley, Reading, MA.

West, R. (1994), Microwave emission of polar firn, Ph.D. thesis, University of Washington,
Seattle,

West, R., D. P. Winebrenner, L. Tsang, and H. Rott (1996), Microwave emission from density
stratified Antarctic firn at 6 cm wavelength, J. of Glaciology, 42(140). 63-76.
--- PAGE 37 ---
Scattering of Electromagnetic Waves: Numerical Simulations.

Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.

Copyright © 2001 John Wiley & Sons, Inc,

ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Hlectronic)

Chapter 2
INTEGRAL EQUATION FORMULATIONS
AND BASIC NUMERICAL METHODS
1 Integral Equation Formulation for Scattering Problems 14
1.1 Surface Integral Equations 14
1.2 Volume Integral Equations 17
1.3. Dyadic Green’s Function Singularity and Electrostatics 19
2 Method of Moments 23
3 Discrete Dipole Approximation (DDA) 27
3.1 Small Cubes 28
3.2 Radiative Corrections 29
3.3 Other Shapes 31
4 Product of Toeplitz Matrix and Column Vector 37
4.1 Discrete Fourier Transform and Convolutions 38
4.2 FFT for Product of Toeplitz Matrix and Column Vector 42
5 Conjugate Gradient Method 46
5.1 Steepest Descent Method 46
5.2 Real Symmetric Positive Definite Matrix 48
5.3 General Real Matrix and Complex Matrix 52
References and Additional Readings 57
~13-
--- PAGE 38 ---
14 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
In this chapter, we discuss integral equation formulation of boundary
value problems. We will give a brief overview with more detailed analysis
to be given in subsequent chapters where the numerical methods are ap-
plied to specific problems. We will also describe the basic numerical methods
that include the method of moments, discrete dipole approximation, product
of Toeplitz matrix and column vector using FFT, and conjugate gradient
method. These numerical methods will be used extensively in subsequent.
chapters.
1 Integral Equation Formulation for Scattering Problems
1.1 Surface Integral Equations
Tntegral equations can be derived by using Green’s functions. The advantage
of surface integral equation is that they reduce the dimension of the prob-
lem by one. In the following we first consider a two-dimensional scattering
problem so that the surface integral equation becomes one-dimensional.
Consider an incident wave impinging upon an object. Let the problem
be uniform in the #-direction so that there is no variation in the §-direction
ic., 2 =0 (Fig. 2.11).
We first consider the TE case with electric field in the j-direction
Eine = Wine(@,2) (2.1.1)
E = (2, z) (2.1.2)
The # field is
— .f Ow OY
H=i(-— = 2.1.3
jwp i( ae) +258 ( )
For the TM case, the H field will be in the g-direction so that
Hine = ines) (2.1.4)
A = inb(a, 2) (2.1.5)
Then the electric field is
~ a fOr OY .
~iweE = 9 (-52) +a (2.1.6)
If the scattering object is a perfect electric conductor, then the boundary
condition is
axE=0 (2.1.7)
--- PAGE 39 ---
§1.1 Surface Integral Equations 15
~~ i™
incident wave \
( \
% |
j
ne /
ee 4
\s
Figure 2.1.1 2-D scattering problem with 1-D boundary.
Let #2 = ng& + n_%. We note from (2.1.6) that
n Oy Oy . Oy Ow OY!
x (a 4) = ln an) = 2.1
” ( "O2t Op | nea, tM 5, Von (2.1.8)
where = =h- Vy.
n
Thus for two-dimensional problem, we can simply use y:. Then
Vth =0 (2.1.9)
(i) For TE problem of perfect electric conductor, the boundary condition is
y=0 at (2.1.10)
(ii) For TM problem of perfect electric conductor, the boundary condition
is
Oy
= =0 at S 2.1.11
dn a (2-111)
For two-dimensional problems, the Green’s function is
_ é a ¢ ¢
90.9.) = Hs” (lp — 7) (2.1.12)
where p = r& + 22 and HW is the zeroth order Hankel function of the first
kind.
The Green’s function obeys the equation
(V? +k) 99,2) = -6 (B—7') (2.1.13)
Applying the scalar Green’s theorem.
[o (di Vay = eV7 qn) = f dB + (i Vibe — Yo Ven) (2.1.14)
--- PAGE 40 ---
16 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
Let w=) and uy = g in (2.1.14). Then
[ore — ¥vV9)
= [ alo(-#v) - (-#o-4 7)
wip) itp inv Ow Og
= =— | dS (ga -y |) tine (W) (2.0.15
{ if p’ in Vp Tan an + Pine () ( )
where ” is the outward normal to surface S. In (2.1.14), the surface integral
at infinity gives the incident wave Winc(p). For TE case of PEC, we apply
(2.1.10) to get
up) ifp’inV | Ow ,
Y =~ [ asoG.) 2D + vine (F 2.1.16
(0) coin yy tof SAPTIGE + Hine (@) (226)
To obtain a surface integral equation, we Ict p’ approach surface S, then we
have
, oy OW
0= vine) ~ fag (7) 5° @) (2.1.17)
for pl € S.

Equation (2.1.17) is a surface integral equation because p and p’ both
belong to the same domain $. Equation (2.1.17) is Fredholm equation of the
first kind. The source domain 7 and the field domain 9’ belong to the same
domain. As p — 7’, 9(7,7’) is large which means the matrix equation will
have strong diagonal elements which makes (2.1.17) well conditioned usu-
ally. This is unlike Fredholm equation of the first kind in inverse scattering
problems. In such inverse scattering problems, the source domain and the
field domain are different. The matrix equation does not have large diagonal
elements and the equation is often ill-conditioned.

For TM problem of PEC, we apply boundary conditions (2.1.11). Then

vp) ifp inv 7 | a OG po

=u dsw(p) = (p, 2.1.18

{5 itp in vy ~ Pn) + J A800)5, (7!) (2.1.18)

To gct a surface integral equation, we let p’ approach surface S. However,
since ¥(f’) experiences a discontinuity of S from V to V, which is also

; 0. . . .

manifested in the fact that ae (p,p') has a non-integrable singularity at
p=P. care has to be exercised. We will address these problems later when
we implement these equations numerically in later chapters. At this point
--- PAGE 41 ---
81.2 Volume Integral Equations 17
V, («9 )
Figure 2.1.2. An incident wave impinges on a scatterer with permittivity ep(F) and volume
Vp.
we let p! — p!, when + stands for the fact that we approach $ from V. Then
—, . =) 99 ;_
0) = Wine (@) + im, f ase (7) 32 (9,0) (2.1.19)
Pe, ne
for p’ on S.
1.2 Volume Integral Equations
Consider an incident wave E'"“(F) impinging upon the scatterer with per-
mittivity €,(7) (Fig. 2.1.2). Maxwell’s equations are
Vx EB =+iwpH (2.1.20)
V x A = —iwe,(7)E (2.1.21)
where
_, _ felt) fTEV,
ép(F) = 2.1,22)
ofr) {% fF EV ¢
It follows that
Vx Vx E-RPE =k (e(7) -1E (2.1.23)
where €,(7) = €p(7)/e is the relative permittivity. Thus the scattered field is
Eu) = | aFGF") P(e") IE) (2.1.24)
Adding E,(7) to E'“(r) gives the total field B(7). Then
E@ =F" (7) +h | a'GF,7) - (e(F) — 1) EF’) (2.1.25)
We can also regard
P(F) = €(e-(F) — 1) EF) (2.1.26)
--- PAGE 42 ---
18 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
as the induced polarization density. When solving (2.1.25) numerically, we
have to take into account the singularity of the dyadic Green’s function.
A volume integral equation can also be obtained by using vector and
scalar potentials.
Vx E=+iwpH (2.1.27)
V x H = -iwe,(7)E
= —iweB — iwe(e,(F) — 1I)F (2.1.28)
V-H=0 (2.1.29)
V- (epFE) =0=V- [(e + (&-(F) — 1) E| (2.1.30)
Using equivalent current of
I(F) = —iwe (c-(F) — 1) EF) (2.1.31)
From (2.1.30), V+ (cB) = V- [eB — ¢-(F)cE}. Thus
1 = =
ps (7) = py Im) = -V- [(e-(7) — 1) E®)] (2.1.32)
We can make use of the scalar Green’s function
_ iklFF|
9") = Fae (2.1.83)
The solutions of scalar and vector potentials are
A(F) = [rawr wIe) (2.1.34)
=) — fartotre yO) 0.1.35
OF) = | drg(F.7)2— (2.1.35)
€
Since B, = iwA — V®, we have
Bia; Ioia al\ Tiel at pm on PL) 5128
E.(F) = iw | dr g(FF )ud(F) —V | dr 9 FP) (2.1.36)
Using (2.1.31) and (2.1.32) in (2.1.36), we get
Ber) =B™(r) + f deter’) (oP) ~ 1) BG)
+ vf aarryv- [(e(F) - 1) B®)| (2.1.37)
The volume integral over d7’ is carried over infinite space. Thus if €(7’)
is discontinuous, the divergence term inside the integrand of (2.1.37) can
give rise to surface charge density. This happens when there is a boundary
separating two media of different permittivities.
--- PAGE 43 ---
81.3 Dyadic Green's Function Singularity and Electrostatics 19
1.3. Dyadic Green’s Function Singularity and Electrostatics
From (2.1.25), the volume integral equation is in terms of the dyadic Green’s
function. Using

= = VV\ _ .

G7’) = (7 + *) GFF) (2.1.38)
we have

E@)=E™(@)+ 8 fare) —1E(’)
+ / aF"(VV9(F,F")) - ((F") ~ EC") (2.1.39)

To take into account of the singularity of the dyadic Green’s function, let

= = Tor - 7"

GFF") = PVG) - oe) (2.1.40)
where PV stands for principal value integral and 6(F — 7’) is the three-
dimensional Dirac delta function. The volume integration in PV is over the
volume with a volume V5 excluded from the observation point 7 (Fig. 2.1.3).
The volume V5 is infinitesimal. Nevertheless the shape of the exclusion vol-
ume has to be specified. The dyad Z depends on the shape of the exclusion
volume.

The volume integral equation becomes

E(r) =E'" (7) +[ aFGF, )(e(F) — Ik? BF’) + Eoots(F) (2.1.41)

V-Vs

where

Eva (F) = —(er(F) - 1) L- Bl) (2.1.42)
is the self field. The source is an infinitesimal volume Vj of relative permit-
tivity & = €p/e (i.e. relative to the background ¢), and with internal field
‘E(F) inside Vs. On the other hand, the first two terms on the right-hand
side of (2.1.41) is the contribution to E(F) from the incident field and its
surrounding medium. Since V3 — 0, the self field Esei¢(F) can be interpreted
in terms of electrostatic field created by free charge and polarization charge
densities and surface charge densities.

On the other hand, if the vector potential and scalar potential are used,
we have the volume integral equation of (2.1.37). The subject of singularity
of the dyadic Green’s function are discussed in [van Bladel, 1961; Livesay
and Chen, 1974; Yaghjian, 1980; Tsang et. al. 1985; Chew, 1990]. We note
that by comparing (2.1.37) and (2.1.39) that the term due to electric current
--- PAGE 44 ---
20 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
J is benign. The singularity comes from the electrostatic part. of electric field
due to charges that are in the third term of (2.1.37) and (2.1.39). Thus we
shall use electrostatics and examine how electric charges and polarization
charges produce electric field in the source region.
In the electrostatic limit
gF.F) = FoI (2.1.43)
The electrostatic equations are
V-D=p; (2.1.44)
VxE=0 (2.1.45)
The electrostatic potential is & such that
E=-Vo (2.1.46)
The boundary condition is
fa (Dont — Din) = Ps (2.1.47)
where “out” and “in” represent the outside and inside of the particle respec-
tively. If we use polarization density, with « being the background permit-
tivity,
D=cE+P (2.1.48)
P=(e,(7F)-e)E (2.1.49)
Then
V cE = py t pp (2.1.50)
where
Pp = -V-P=-V- [(e(7) - OF] (2.1.51)
is the polarization charge density. The surface polarization charge is
—f- (Pout — Pin) = op (2.1.52)
The electrostatic potential can be calculated from the superposition integral
of these charges
OF) = tf aro) [or @) + ppl®)]
+ tf astatr.r) {os(F’) + op(')] (2.1.53)
For the case of an infinitesimal volume Vj, we can assume that it is of ho-
mogeneous permittivity €p inside Vs (Fig. 2.1.4). The field inside is FE.
Pin =(€p-O)E (2.1.54)
Pou =0 (2.1.55)
--- PAGE 45 ---
§1.3 Dyadic Green’s Function Singularity and Electrostaties 21
We).
Ss
Figure 2.1.4 Field produced by E inside Vs on itself.
Note that Pin = constant inside Vs so that Pp=-V- Pin = 0. For dielectric
problem, py = 7; = 0. Thus we only have
Op = —ft+ (Pout — Pin) = fe (Er — IE (2.1.56)
Thus for 7 inside V5, from (2.1.53) and (2.1.56),
1
Path) = = f dS'alr Pop)
: 1 - _
= / 4s Ror” “(@ —- DEP) (2.1.57)
The electric field is Eee = —VOcir(F). Let R=(F-7)/R with R=|F-?’|
and R! = —R. Then —V(1/R) = R/R?. Also V5 is small so that E is constant
inside V5.
Buatr) = fase, EW") =—(¢ —DE-E (2.1.58)
self (7) = 6 Tar rp A(T) = —(€r E As
where
_ Ral
L= | ds'———, 2.1.59
[i dnlF— FP (2.1.59)
Note that 7 is at the center of Vj and F is a unit vector pointing from 7 to
FP.
Example 1: Without loss of generality, let 7 = 0. If Vs is a sphere of radius
6 and 5 > 0, then R! =n! = 7 = sin @cos d% + sin Asin df + cos 02. We have
= ayn 2
T= zf aosind do FF (2.1.60a)
An Jo 0
--- PAGE 46 ---
22 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
and
| dQ FF = [ axeind cost + sin @sin ¢y + cos 62)
: (sin 0 cos % + sin @ sin dy + cos 92)
An=
= oa T (2.1.60b)
We have used the result that on integration, the cross terms in (2.1.60)
vanish. Hence
= e+ 9y+2e _T .
L=— . =5 2.1.61
3 3 ( )
Example 2: Let Vs be a rectangular parallelepiped with sides equal to dz, dy
and 6., respectively. Also let 6, = ad, 6, = 66 and 6, = cd and 6 > 0. Thus
a, b and ¢ are finite numbers and the ratios among them are important
to determine LZ. In this case there are six faces for the surface integral of
(2.1.60). The sum of the contributions from the top and bottom faces to L
is
Lim [° ls i dy + ub + (62/22) ~ Hee + vi ~ (62/2)2)
Am o-0 J 5,/2 J-8,/2 (a? + y? + (62/2)?)3/
_, bbe pee 1
= 2z—— U3 $ aT OT
2m Jo (a? + (52/2)?)(a? + (8y/2)? + (6:/2)?)9/?
— 332 tant b2by 216
= 22 tan Ree og + HE (2.1.62)
The integration over dy and dz can be found in Gradshteyn and Ryzhik
{1965]. Note that in (2.1.62), the result only depends on the ratios of the
lengths of the three sides of the rectangular parallelepiped. Similar expres-
sions can be derived for the other four faces.
Et 2 2 tan7! be 499 tan ca
=f FF te ST n+ —
re eae ayia Ty a+ eR + aye
a5 = ab
+ 22 tan arta} (2.1.63)
For the special case of a cube, we set a = b = c in (2.1.63). That gives
= #+gg+s2 7
L = ———=5 2.1.64
3 3 (2.1.64)
Examples of other shapes can be found in Yaghjian [1980].
--- PAGE 47 ---
§2 Method of Moments 23

2 Method of Moments

The method of moments (MoM) is a numcrical technique that has been

used extensively in the solution of electromagnetic boundary value prob-

lems. Many excellent texts have been written on this subject. [Harrington,

1968]. The technique is used extensively in this book in Monte Carlo sim-

ulations. A characteristic of this technique is that it leads to a full matrix

equation which can be solved by matrix inversion. In later chapters, we will
describe techniques that can speed up the numerical solution of these matrix
equations.

With the use of Green’s function, integral equations can be derived.

Consider a one dimensional integral equation of the form

b
[ da'G(x, x") f(a") = e(x) (2.2.1)
a

where G(x, 2’) is the Green’s function, f(z) is the unknown for the domain

a <a <b, and c(x) is known for a < x < b. To solve (2.2.1), two sets of

functions are used in the MoM: basis functions and weighting functions.

(1) Basis functions. A set of N basis functions in the domain of a < x <b
is chosen. Let the basis functions be fi, f2,....fn. The unknown func-
tion f(x) is expanded in terms of a linear combination of these basis
functions.

N
Fle) = 7 bnfale) (2.2.2)
n=l
The linear combination of f,,(2) should well represent the unknown f(x)
in the domain. Substitute (2.2.2) into (2.2.1), we have
N »
Sibu ff det Gleya!) fale!) = ee) (2.2.3)
n=l @
The unknown coefficients 6), b2,...,by are to be determined.

(2) Next a set of N weighting functions (testing functions) w1(:), wo(x),
.+., wn (x) is chosen. Multiply (2.2.3) by wm(x) and integrate over the
domain

N “b “b b
Yin | dwn (x) | du'G(w, 2") fn(2’) = | drwm(x)e(e) (2.2.4)
fal a Ja a
--- PAGE 48 ---
24 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
This gives the matrix equation
N
S° Gnbn = em (2.2.5)
n=l
m=1,2,...,N, where
b
Cn = | dew, (x)c(x) = (wm, c) (2.2.6)
a
b b
Grn = | daw (2) [ da!G(2,2") fala’) = (ms Gfa) (2.2.7)
a a
where the inner product notation is used.
b
(a = [de Fa) a) (2.28)
‘a

Computational Considerations

Generally (2.2.5) is a full matrix equation. We note the following

(1) Matrix solution: To solve a full matrix equation of order N by full ma-
trix inversion (e.g., Gaussian elimination) requires O(N) number of
operations. This increases rapidly with N.

(2) Matrix filling: To calculate Ginn, m,n = 1,2,...,N can be computa-
tionally intensive because there are N? values of Gin. Also Gyn can
require the evaluation of a double integral as given in (2.2.7). The ma-
trix filling can be more computationally intensive than matrix solution
because G(x, x") can be of a complicated form. Also since there are N?
elements of Ginn, this can impose a large memory requirement.

(3) The study of fp, n = 1,2,...,N is also an important subject as the
choice of f;,, must well represent the correct solution. Often they have to
satisfy differentiation and continuity properties.

Basis Functions

Basis functions can use full domain functions such as sines, cosines, special

functions, polynomials, modal solutions, etc. A set that is useful for practical

problem is the subsectional basis function. This means that each f, is only

nonzero over a subsection of the domain of f.

A common choice is the pulse function (Fig. 2.2.1a)
1 ifan<a sh, :
ner) = {for Sa tm (229)
0 otherwise
--- PAGE 49 ---
§2 Method of Moments 25
In(z)
Fat) fnsi(a)
i4---
an bn Gy Qnty tt
@ o)
Figure 2.2.1 Common choices of basis functions: (a) pulse functions; (b) triangle functions.
where the interval a < « < 6 have been divided into N intervals with end-
points @, and bn, n = 1,2,...,.N.

Another choice is the triangle basis functions (Fig. 2.2.1b). In Fig. 2.2.1b
we show fp(«) and fn41(#). Note that f,(a) and fn4i(a) overlap.
Weighting Functions
Two common choices are
(1) Galerkin’s method. In this case the weighting functions, n = 1,2,...,

NN, are the same as the basis functions, i.e., wn(x) = fn(x).

(2) Point matching. One can pick a set of points ¢ = 24, 72,...,7n to
enforce (2.2.3). Then
N b
Sin [ da!G(am,#') fala’) = c(am) (2.2.10)
n=1 "@

where

Cm = 2m) (2.2.11)
b

Gn = [ da! Gam, 2") fn(2") (2.2.12)
@

This particular choice of testing procedure is called point matching. In

terms of weighting functions, this means that the weighting functions

are
Win (x) = O(a — tm) (2.2.13)
where m = 1,2,...,N and 6 is the Dirac delta function.

In Chapter 1 of Volume I, we have used an infinite cylinder approxima-
tion to calculate the scattering by a cylinder of finite length. The surface
--- PAGE 50 ---
26 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
2.0
20
o 15
i Lo”
% 10 (foo—o-o-0 oo Ne |
= / y= \ t
05 os 0
00 oS
0 5 10 15 20
Location t (cm)
Figure 2.2.2 Comparison of total surface fields for m = 0 harmonic computed based
on infinite cylinder approximation (IC) and MoM solution using the following parameters:
frequency = 1.225 GHz, permittivity of cylinder ey = (6.5 +42)eo, radius of cylinder = 2.5 em,
length of cytinder = 15 em.
fields are then used to calculate the scattering by integrating the surface
ficlds only over the finite length of the cylinder. Numerically, one can use
the method of moment body of revolution code [Glisson and Wilton, 1979}
to calculate scattering from a finite length cylinder by solving the surface
integral equations. The variations of the unknown electric and magnetic sur-
face fields are approximated by staggered pulse functions in the ¢-direction
and are expanded in Fourier series in the ¢-direction.

In Fig. 2.2.2 we make a comparison of total surface fields for m = 0 har-
monic, computed based on infinite cylinder (IC) approximation and MoM
solution. The incident wave is of unit amplitude in a direction perpendicular
to the axis of the cylinder with polarization parallel to the axis of the cylin-
der. Equivalent electric surface currents 7.J, and equivalent magnetic surface
current My are shown.

The t coordinate and the ¢ direction is as indicated in Fig. 2.2.2. The t
coordinate starts from center of bottom face, radially outward to the edge,
along the curved side and then ends at the center of the top face with range
2.50m +15cm +2.5cm = 20cm. Thus the infinite cylinder approximation
has uniform current densities on the curved surface of the cylinder while the
MoM code predicts a maximum at the midpoint.
--- PAGE 51 ---
§3 Discrete Dipole Approximation 27
3 Discrete Dipole Approximation
In this section we discuss how the volume integral equation of Sections 1.2
and 1.3 can be discretized and solved numerically based on the discrete
dipole approximation (DDA) [Purcell and Pennypacker, 1973; Goodman ct
al. 1991].
The volume integral equation is
E(7) =E™ (7) + [ aFGF) - (e(7) — NE)
JIV-V5
~ (e(7) - 1) L- Er) (2.3.1)
If we define polarization P by
(e,(F) — ¢) E(r) = P(r) (2.3.2)
Then
= =i ke = = ——
Fr) =E'"(r) + =[ a G(r) - P(r’) —((F) - I) E-E®) (2.3.3)
V-Vs
We discretize (2.3.3) into volumes AV; with centers at 7j, j = 1,2,...,N.
Inside AVj, there is uniform field Ej and polarization Pj. Then
ay _ ine RAMS = ==
EQ) =E™ (7) + — SO GF) PAV) — (GF) -YL-E, (2.3.4)
=1
i
Let R = unit vector from to7, R= |F-7"| and R=7-7"’. For F 47, by
straightforward differentiation,
G(r,7") = Gi(R)I + Go(R)RR (2.3.5)
where
; apo eth
Gi(R) = (-1+ikR+k°R FRB (2.3.6)
CG apo, eikR
'2(R) = (3 — 3ikR - *)-—___, 2.3.7
2(R) = (3 — 3ikR — k°R TRB (2.3.7)
We let
= Ps
A(F,?’) = Ger, F)
elk 25 pp, LotkR) oF ape
= RP (HRT (RT -3RR)} (2.3.8
cm { ( +RR)+ 772 (R°T—3RR)> (2.3.8)
--- PAGE 52 ---
28 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
3.1 Small Cubes
If the volumes AV; are cubes, then
Bj = (AV)P; (2.3.9)
where AV = V/N = d? and d is the length of each volume cube. Then the
discretized version of the volume integral equation is, with L = 1/3,
X= € E
Fine Fie. =.\.5 pi i
E, = E' ~ LAr) -B~ (= -1) 5 (2.3.10)
j=
jf
where Ej, EB’, Pj, €pi are the values in the ith elemental cube. Note that
the second term excludes j = i in accordance with principal value and the
last term is a result of the E factor associated with cubic volume. The dipole
moment for each cube is
p; = Pep — )E; (2.3.11)
Putting the last term in (2.3.10) on the left-hand-side and using (2.3.11)
gives the matrix equation for the dipole moment of each cube
N
Bi = WE; - 0% s Aig Pj (2.3.12)
j=l
dA
where Aj; = A(T;,7;),
n?—1 (2 ~ 1)
ay = af = 3ed® (3) = 3eAV 3 (2.3.13)
ne +2 (= + 2)
€
and n = \/ep/e is the complex relative refractive index. In (2.3.13) a€ is the
familiar Clausius-Mossoti polarizability. However a; in (2.3.13) does not obey
optical theorem and will subsequently be changed to include more correction
terms. _

We note that the matrix elements A is that of the dyadic Green’s func-
tion which is translational invariant. Thus the product of A and a column
vector can be computed by FFT. That is

N_
AaB
j=l
j#t
--- PAGE 53 ---
§3.2 Radiative Corrections 29
where the summation over all cubes except the ith one can be computed
by FFT. Thus solution of (2.3.12) using conjugate gradient method com-
bined with FFT makes the solution much faster than that of the Gaussian
elimination [Goodman ct al. 1991].

However, if €p; is the same as € in most of the the region, it may be more

efficient to use the electric field equation from (2.3.11) and (2.3.12)
N
Beg: — 6) _ ine = 3 =
EE = Ey So Ay Ble; — E; (2.3.14)
i jal
j#i
where N now only need to include those cubes that have €); 4 €. Note also
that (€pi — €)/a; is finite as can be seen from (2.3.13) even when €pj = €.

For the case of as single small cube, the scattering solution is calculated
by dropping the )> Aj; +p; term from (2.3.10). The equation can be solved
readily to give E; = F;"* [1+ } (& — 1)] 7‘. We note the similarity between
a small cube and a small sphere. The polarizability of a small sphere is
1s = 3uge(n® — 1)/(n? +2) where n = €p/e and vo = (4/3)a3 is the same as
(2.3.13) with d replaced by (47/3)a%. The internal field of a small sphere is
(3e/(€p + 2e))E""° which becomes the same as that of a small cube.

As we examine the optical theorem for a small sphere in Chapter 2, Sec-
tion 8.2 of Volume I, we have noted that the Clausius-Mossoti internal field
is not accurate enough because when one applies the optical theorem using
the result forward scattering amplitudes, it does not give the contribution
due to the scattering part. For the case of small cube, the same reasoning
applies. Thus to ensure that the final scattering obeys energy conservation,
one has to take into account radiative correction. In doing so, the expression
of a; in (2.3.14) is modified with the new expression given below.

3.2 Radiative Corrections

Tn numerical implementations, the cubes are not infinitesimal. One major
correction is to improve the self-term impedance matrix clement. This will
give correction to the Clausius-Mossoti polarizability.

From (2.3.1), the self field Ese¢ should be, for volume cube of finite size,

Boctt =» [ dFG(P)-(e ~ VE -(e -1)L-E (2.3.15)
Ve-Vs
where Vz is the self cube, Vs is the exclusion volume, and 7 is at the center
of the cube. Thus
Eset = FS - (6 — LE (2.3.16)
--- PAGE 54 ---
30 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
where _ _
= f Fi L € = LT
= 'GFF) —- = -S iy Ar, 7) — = 3.1
Ss [wee 7) RB el A(r,?') RB (2.3.17)
and
= k=
A=-—G (2.3.18)
Then the DDA equation becomes
a pine PNAS s = =
E; = Ey + = SO G,F))- P)AV) + PS (GF) -1)E; (2.3.19)
=1
iyi
Because of the similarity between a small cube and a small sphere, a small
equivalent spherical volume of radius a where (47/3)a3 = d* = vp will be
assumed. Then, using G; and G2 as given by (2.3.6) and (2.3.7)
s 7 . fe af = ate
S=-s5+ ti [ dr’! [ation + Go(r!iF]
Tt... fo n , Galt’)
= gp + jim in [ a'r [cuir +S) T (2.3.20)
The second equality in (2.3.20) is a result of (2.1.60). Since
Galr!) _ itr’
yy, Gar) _ 4
Gir’) + 3 Sar? (2.3.21)
we have
S=Is (2.3.22)
where
_ 1,2, ” aplpteikr’ — 1 2 ike, ik
3= gat jin [ dr'r'e =—3 + ga [ite ql ika)|
1 2 [ka ik§a3
~-s54+s5 | + 2.3.23
ota (ot | (2.3.28)
in the limit of small a. Putting (2.3.22) in (2.3.19)
N
a _ Fine | (€ oa =
BE, =B+ (2 —1) si? E,- y Aiy -By (2.3.24)
i=
aft
Thus
_ Rin 1 N_
BE, = — —  - ——— . Ay-3 (2.3.25)
1 (2-1? (Bye
€ € fia
--- PAGE 55 ---
83.3 Other Shapes 31
Multiply by AV (ep; — €:), and noting that.
D; = AV (Epi — 6) Ey (2.3.26)
we have
N=
B, = aiF, — 04S AyD; (2.3.27)
ji
SFt
with
AV (Gi -
oy = AV 6) _ (2.3.28)
1— (B= 1) sk?
€
Putting (2.3.23) in (2.3.28) gives
aeAV (1)
€
w= a2 3q3
pi (2 ) ka’ kPa
B49 -9(B 1) (22 4 j="
e 7 € 2 a 3
c
af
= oo 2.3.2!
1-2 al (ka? + ik3 a3 (2.3.29)
3e AV | 2 3
Using a = (3/4m)'/3d and AV = d? in (2.3.29) gives
c
a
og = ——_ (2.3.30)
: 1 08 [ (42) yap, IDK
dred? |\ 3 : 3
The term with imaginary part in the denominator of (2.3.30) is known as
radiative correction, which arises for the same reasoning as when scattering
by Rayleigh spheres was discussed in Chapter 2, Section 8.2 of Volume I.
3.3. Other Shapes
Let the medium be discretized into rectangular parallelepipeds V, of sizes
dy, x dy x dz. We let dy = ad, dy = bd, dz = cd where a, b and ¢ are dimen-
sionless quantities and their ratios denote the relative sizes of the three sides
of the rectangular parallelepiped. The exclusion volume Vj for the dyadic
Green’s function in this case will be an infinitesimal parallelepiped with di-
mensions J, = a0, dy = bd and 6, = cd and the Tis as given in (2.1.63). Note
that the ratios of the sides of the finite small rectangular parallelepiped V;
is the same as that of the infinitesimal rectangular parallelepiped V3. Then
--- PAGE 56 ---
32 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
it is useful to write a low frequency approximation of G(R). We note that
for R40
__ e=— eikR 2, pF pop, (— IRR), oF ope
G(R) = pA = -am{# (-R T+RR)+ py (RB 7-3)
_ (2.3.31)
When expanding G(R) of (2.3.31), it is important to see that there is a sin-
gular part of O(1/(k?R*)) that is non-integrable over the origin. We also
have to expand to the leading term in the imaginary part because that
accounts for radiative correction. The Green's function G(R), on expan-
sion will give O(1/(k?3)) + O(1/R) + iO(k). Thus in (2.3.31), we write
exp(ikR) ~ 1+ ikR — k?R?/2— ik?R3/6. We have to include —ik* R3/6 be-
cause this gives a term of order (O(k) when multiplicd with the second term
inside the curly bracket of (2.3.31). Thus for R 40 and kR <1
G(R 1 2 27 4RR i
G(R) ~ rat (—R?7 + RR)(1+ikR)
(L=ikR) = gan ( op RAR? ke RS
— ~3RR ~ oS i
+ S(T — BRR) (1 +ikR ~~ )
_ 1 os apm, Ll pt ap 4ikeL ys
= Tee I-3RR)+ xf a 7+RR)+ “7 (2.3.32)
Note that the imaginary part term of (2.3.32) is just the product of a constant
and a unit dyad. Following (2.3.17), let
— ¢ _ I
S=-3 dr A(r,?’) — > 3.33
el, F Ar?) BR (2.3.33)
We use (2.3.32) to write A as a sum of a regular part Ap that is integrable
over the origin and a singular part A, that is non-integrable over the origin.
Thus
A(R) ~ A(R) + A(R) (2.3.34)
where
A(R) a (R27+RR) ies (2.3.35a)
=- - -— 3.354
° 8reRS 67
Zr 2F . SRR ae
AFP) = pps (HT ~ BRR) (2.3.356)
Thus
3=-4 ] w Ar)-< Ayer) - © 2.3.36)
S=-p he ir lM) ~ F5 yy Ae) — (2.3.
--- PAGE 57 ---
§3.3 Other Shapes 33
Note that Ay is non-integrable over the origin. However, the origin is excluded
in the integration over V, — V5.

The second integral in (2.3.36) can be shown generally to be zero. Here
we perform it for the case of rectangular parallelepipeds of Vs and Vs. The
volume V,; — Vs can be formed from 8 octants. In integration, the cross terms
vanish. The volume integration can also be combined into that of one octant.
Thus

pf a Aaer)
Re Iy.-Vs
de by 4 bs ty as
2 2 3 r 3 7 -
=-—5 [ ar f ay f a+ [ ae f ay [ dz
me dy Sy 4 fi a" Jo
ta te de 1
2 2 2
dx d d —[94(—20? + y2 + 22
+f 2 | vf eb x aaa ttl a + yy" +2")
+ p(—2y? 42 422) 4 232 $y? -22%)| =0 (2.3.37)
The integral over Ay can be performed as follows. The dyad Sis diagonal
so that
S = Spt + Sy + S242 (2.3.38)
T= L,&é + Lyi + L222 (2.3.39)
and
5-52
S=D-Z (2.3.40)
D = D,* + Dy + Dk (2.3.41)
where
20 4 be “
Ly = = tan ete pAye (2.3.42)
2 = ca
L.=~t oe 2.3.43
y= ON at TAR (2.3.48)
2 4 ab
a2 a 2.3.44
bem tan (a? + 6? + c?)1/? ( )
--- PAGE 58 ---
34 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
1 [ae Peay tee) =)
D,=— al dy ln ——2—_. +
us 2 Jo 2 a.\2
VP (#)
de d.\ (dy .
+ [Pier _O8)_ + av 3s)
er (OnerOae
2 2
2 2
off pant O-®)
va) |o f, > —
7 0 yet (4)
we de) (4. ;
+ | * ay ayant C4) (8) + Pav (2.3.46)
‘ V(4) +#+(4)
NP yn?
fla pe byte 4)'+
De=— $f dey —— $$ —_
ene)
4 &) (de ik
+ [Oo aeretaart GO) + Rav (2.3.47)
Pern
Substituting (2.3.40) into (2.3.19), we get
= = = N =
Pp, Qi zine an nT Dj 24
zav =ay Ear d(eav )Aij - Ar (2.3.48)
i
where
Gi = OinE + oviy 9 + 04222 = (= 1), (2.3.49)
Bix 1 ;
Bix — 2.3.50
cAV 14 (@-1) (Le - Det) 8)
€
--- PAGE 59 ---
§3.3 Other Shapes 35
Siy 1
= (2.3.51)
cAV 14 (= 1) (Ly ~ Dyk?)
Biz 1
Se = (2.3.52)
cAV 14 (= 1) (L. = DK?)
€
and AV = d,dydz.
In the case of cells of circular cylindrical shape of radius a and length 1,
the corresponding results of Lz, Ly, Lz and D,, Dy and D, are
:
Ly = Ly = ar BR (2.3.53a)
L
L,=1-—>——3 2.3.53b
. (da? + [?)1/2 (2.353)
ike"l lp pg 5 2 (1+ VP + 4a?
Dz=Dy = +5 { VB +40? — 1} + © n(t) (2.3.53¢)
ika?l a?) (14+ VI? + 4a? es
Dz= 3. t Su(oe*) (2.3.53d)
Equation (2.3.48) is the DDA matrix equation and is to be solved nu-
merically. After the solution is obtained, we have the solution of the induced
dipole moment ; for every cell. The electric field at cell i is given by
= 1 PD; a
=a 3.54
BE; (ear (2.3.54a)
€
for €pi # € for cell i. For the case of €p; = €,
5 5 N =
= & sine 8 = p&p
= te i, FAV)A;; > 2. 2.3.54
Bim ay Bi cay ue As AV (2.3.546)
afi
For the case of rectangular parallelepipeds the matrix equation of
(2.3.48) is of dimension 3N x 3N where N is the number of rectangular
parallelepipes and the factor 3 arises from the 2, y and z components of the
polarization vector. In the standard form, the matrix equation is
Zz=b (2.3.55)
where Z is the impedance matrix and Z is the unknown column vector and 6
is the right-hand side. Let the rectangular parallelepipeds be equally spaced
in #, J and 2 directions. Then (2.3.48) can be solved by using conjugate
--- PAGE 60 ---
36 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
gradient method (CGM) combined with fast Fourier transform (FFT) that
will be discussed in Section 4. In applying CGM, we need to take the product
Zd and the product. Zc where + denotes adjoint, d is the direction vector
and F is the residual vector. For example, if there are two rectangular paral-
lelepipeds, N = 2, then the impedance matrix Z is of dimension 6 x 6 and
is
= ina =
_ I cay (AV) Az _
Z=| = (2.3.56)
2 = =
= (AV) Al: I
cay (AV )Aiz
Note that
Ay = Aji (2.3.57)
and
+ =
Ai; = Aij (2.3.58)
where ¢ denotes transpose of the dyad. Then the adjoint of the impedance
matrix is
= = a
st I (AV) Ayo SG
Z= = cAV (2.3.59)
ane Oo =
(eAV) Aj - av T
where * denotes complex conjugate.
After the matrix equation (2.3.48) is solved, the far field scattered field
in direction ky is
ee ce ip ik, 7, _Pi
F)= 7 (dg6. . yikes 9 9
E(r= tar® AV (885 + hshs) > e cAV (2.3.60)
i
The time-averaged power absorbed is equal to
1 =
(P,) = 59 nl BP AV (2.3.61)
i
where Si is the imaginary part of €,; for the ith cell. In terms of dipole
moment of each cell, we have
0 _f# e!,=0
1 1 a
=~-w P; . ‘
R= ca Rea ire z0 (2.3.62)
€
--- PAGE 61 ---
§4 Product of Toeplitz Matrix and Column Vector 37
Calculation of Matrix Elements by Numerical Integration
In the matrix equation of (2.3.48), the Ai elements are calculated by taking
the value of A(F,7") at the point 7; and Fj, for 7) AF;
Ajj = A(Fi,7)) (2.3.63)
These may not be accurate enough particularly for 7; and 7; in the neigh-
borhood of each other. Accuracy can be improved by numerical integration
over the cell V; centered at 7;. Thus we can define a neighborhood distance
Tq so that
1 | =
= =< | dF A(r;,7) for |F —7;| < Ta
Ay = AV Ny, BP) fori Fy (2.3.64)
A(Fi,7;) for (7; —7;| > 7a
The expression of A,; of (2.3.64) will still preserve the translational invariant
property so that the FFT can still be taken when the matrix equation is
solved by iterative method.
4 Product of Toeplitz Matrix and Column Vector
In matrix equation, the product of a matrix and a column vector is
y=9r (2.4.1)
where F and ¥ are column vectors of dimension N and g is a matrix of
dimension N x N. In matrix notation
N
y(n) = ys g{n, m)a(m) (2.4.2)
m=1
n = 1,2,...,N. The domain has N points. If the kernel g(n,m) is transla-
tional invariant, then
N
y(n) = > g(n — m)a(m) (2.4.3)
m=
If gum = Gn—m; the matrix 9 is known as a Toeplitz matrix.
Equation (2.4.3) looks like a discrete convolution. A fast way to do such
a computation is to use FFT. However, since 1 <n < Nandl<m<N,
the range of n — m is such that -(N — 1) <n—m < N—1s0 that the
argument of g has 2N —1 points. Thus Fourier transform of (2.4.3) should be
taken over at least 2N —1 points. In the following, we briefly review discrete
Fourier transform.
--- PAGE 62 ---
38 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
:¢6-<$ $$ $$
| |
| |
|
6
ee 1
% t
al i |
°% 1 2 3 cy 5 6 7 8 9
a
Figure 2.4.1 The x(n) sequence.
4.1 Discrete Fourier Transform and Convolutions
Consider a sequence 2(n) that has length N such that a(n) = 0 except in
the range 1 <n < N. A periodic sequence %(n) can be formed from x(n) by
repeating x(n) periodically outside the range 1 <n < N. Suppose N = 4
and we have a sequence x(n) as shown in Fig. 2.4.1. We can form a periodic
sequence with period N as shown in Fig. 2.4.2.
2°
i(n) = S> x(n + rN) (2.4.4)
r=—00
Let Uy(n) be a rectangular sequence of length N.
7 1 forl<n<N
Uy(n) = { srs
n(n) 0 otherwise
Then
x(n) = &(n)UN(n) (2.4.5)
To take discrete Fourier transform, we define the complex number
Qn
Wy =exp (=) (2.4.6a)
so that
Wh =1 (2.4.66)
N N-1 . . . .
ys whir-n) _ yx wrer-n) { N_ ifn—n' = integer multiples of NV
N = N = is
0 otherwise
k=L k=0
(2.4.6¢)
--- PAGE 63 ---
§4.1 Discrete Fourier Transform and Convolutions 39
TT : : 1
| |
e
a
°
Ss |
a ’ |
2 . |
44 | |
n
Figure 2.4.2. x(n) with period of N = 4.
Then the discrete Fourier transform is, for all k
N N
Xb) = a) WE POY = Vain Ve (2.4.7)
n=l n=l
From (2.4.7), X(k) is periodic with period N. It follows that for all n
LS (k-1)(n=1)
x fn) — Spy k-Vr- y
F(n) = vy XWMy (2.4.8)
The discrete Fourier transform pairs are defined as in (2.4.7) and (2.4.8).
Next define X(k) as one period of X(k).
X(k) = X(k)Uy(k) = {x k=1....,N (2.4.9)
0 otherwise
Thus from (2.4.7) and (2.4.9), fork =1,...,N
N
X(k) = a(n HOY (2.4.10)
n=]
From (2.4.8) and (2.4.10), forn =0,1,...,N—1
1s (e1)(n—1)
7 = LV kD 6
a(n) = WL XO (2.4.11)
Note that the right-hand sides of (2.4.10) and (2.4.11) are periodic while
left-hand sides are only nonzero over one period. The advantage of using fast
--- PAGE 64 ---
40 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
Fourier transform (FFT) is that both (2.4.7) and (2.4.8) can be computed
in N log, N steps rather than N? steps.
The periodic convolution is as follows. Let #;(n) and &2(n) be periodic
sequences of period N and X)(k) and X9(k) be their respective DFT. Let
X3(k) = X1(k)Xo(k) (2.4.12)
and %3(n) be the inverse discrete Fourier transform
1&
Te == Xalky Wee Dae-D
Eg(n) = W ys X3(k)Wy
k=l
tO
x = k-1(mtr—n-1
= WD s Lami Ymtron=1)
k=tm=lr=1
NON
_ Ss > &\(m)¥o(r) m+r—n-—1= integer multiples of N
m=1r=1
0 otherwise
N
= ¥ a(m)a(n+1-m) (2.4.13)
m=1
Equation (2.4.13) is known as periodic convolution. Note that %3(n) is also
a periodic sequence. However, (2.4.13) is not the usual (linear) convolution.
This is because the periodic sequence Z2(n + 1 — m), when it is “shifted”
outside the period N, re-enters on the other side because of the periodic
property. Thus
N
2 (n) = bs #(m)io(n — m+ | Uy(n) (2.4.14)
m=1
is known as circular convolution.
Circular convolution is not equal to linear convolution of
y
SE eu(n)aro(m —n+1) (2.4.15)
n=1
Steps of linear convolution is as shown in Fig. 2.4.3. To use circular convolu-
tion to get the result of linear convolution, we need zero padding (Fig. 2.4.4).
We also note from Fig. 2.4.3 that to obtain linear convolution from circular
convolution, zero padding such that the period becomes 2N is sufficient.
Let 24(n) and a(n) be of length N and zero outside 1 <n < N. The
--- PAGE 65 ---
§4.1 Discrete Fourier Transform and Convolutions 41
9@ rs
12
Es |
x .
: wrliltts
Ssa4ae21 012345678 9 01 12 13 14
n
16; rn
al
= °
el oT til
‘ . ? |
saver t o1e3 4567 8 9 1011 1210 14
E96) a
3
x = 12 +
ae Q oe
BB4 | ] eT ttt.
aa +P 44 t.
©6543 21 01 2 3 4 5 6 7 8 9 10 11 12 13 14
n
Figure 2.4.3 Steps of linear convolution (N = 10).
linear convolution is
N
ag(n) = So ay(m)aro(n —m +1) (2.4.16)
m=1
and a3(n) can be nonzero for 1 <n < 2N ~ 1. Thus there are 2N — 1 points
in a(n).
To use DFT to reform the convolution, we need to “pad” 2,(n) and
x(n) with zeroes to have sequences of length M > 2N —1
7 _ fan) l1<n<N Df
pln) = {5 N+l<en<M (2.4.17)
_ fain) l<n<N
2ap(n) = {i Nal<n<M (2.4.18)
Usually M is chosen as 2N. Then define #1)(m) and %2p(n) as periodic se-
quences with period M. That is, they are periodic replicas of 1,(n) and
X9p(n) respectively. Then from (2.4.16)-(2.4.18)
M
u3(n) = > Fip(n)z2p(n — m) (2.4.19)
m=1
--- PAGE 66 ---
42 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
; |
|
7
°
gs
. |
it | LC |
%—+ ea EE
n
Figure 2.4.4 Zero padding of x(n). (N = 4)
for n = 1,2,...,2N. ‘Thus the DFT pairs that give (2.4.16) are
M
Xip(k) = Sap(ywygrver? (2.4.20)
n=l
7 M
Xa(k) = So aap(aywy VOY (2.4.21)
n=1
Xap(k) = Xiph) Xap(k) (2.4.22)
M
1 ~ ~(n—1)(k—-
Bap(n) = 5 SP Xap PEP (2.4.23)
Oke}
The equation (2.4.23) gives the relation in which 23(m) as defined by (2.4.16)
is computed. Note that the relations (2.4.16) (2.4.23) are exact. F3p(n) is a
periodic sequence of period M and 2’3(n) = F3p(n) for n = 1,2,...,2N.
4.2 FFT for Product of Toeplitz Matrix and Column Vector
Next we address the equation (2.4.3) that describes the product of a matrix
and a column vector.
N
y(n) = S g(n — m)x(m) (2.4.24)
m=1
The equation of (2.4.24) has the following features:
(i) only N values of y(n) are needed. That is, we need to compute y(n),
n=1,2,...,N.
--- PAGE 67 ---
§4.2 FFT for Product of Toeplitz Matrix and Column Vector 43
¢—
A
7 +
°
3 . ]
foe |
%M 1294 8 8 FB ow 2 ww
n
Figure 2.4.5 Zero padding with period of 2N.
(ii) g(m) is needed for n = —N +1,-N+2,...,0,...,N—2,N —1, a total
of 2N — 1 distinct values.
(iii) a(n) is defined for n =1,...,.N.
For simplicity, we take M = 2N.
To illustrate for the case N = 4, we need
(i) a(n), n= 1,2,3,4
(ii) y(n), m= 1,2.3,4
(iii) g(n —m), n—m = —3,—2,-1.0,1.2,3
First we do zero padding of x(n) (Fig. 2.4.5) to get a(n). Let #,(n) be
the periodic version of #1(n) with period 2N.
. _ fa(n) forn=1,2,3,...,N 946
a(n) = {; forn=N+1,N+2,...,2N (2.4.25)
Then
2N
y(n) = S- g(n ~ m)z1(m) (2.4.26)
m=1
Note that the summation has been changed to 2N.
Define
g'(n) = g(n—1) (2.4.27)
See Fig. 2.4.6 for g’(n). Then
2N
y(n) = Ss g/(n —m + 1)%1(m) (2.4.28)
m=1
--- PAGE 68 ---
44 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
10 : sy
8
6
Ez
o 4
°
eld
S32 A o ot 2 3 4 5 6
n
10 1 -
8
26
£
m4
ate
l
Se 2 4 0 1 2 3 (4 5 6
n
Figure 2.4.6 g(n) and g(n — 1).
Define x(n) by
gi (n) forl<n<N
xo(n) = 4 0 forn=N+1 (2.4.29)
g(n-2N) forN+2<n<2N
for n = 1,2,...,2N. Let %2(n) be the periodic version of x(n) with period
2N. Then
Z2(n)=g'(n) for -N+2<n<N (2.4.30)
Note that
g(n—1) l<n<N
a(n) = ¢ 0 n=N+41 (2.4.31)
gm—-2N-1) N+2<n<2N
Hence
2N
y(n) = S> Fo(n — m+ 1)a(m) (2.4.32)
mat
--- PAGE 69 ---
§4.2 PFT for Product of Toeplitz Matrix and Column Vector 45
Define
Qn
U(n) = So F(n — m+ 1)H(n) (2.4.33)
m=1
for all n. The result of §(n) is periodic with period 2N. Also
y(n) = 9(n) for l<gn<N (2.4.34)
Now (2.4.33) satisfies the properties of periodic convolution.
We apply periodic convolution.
2N
X(k) = Wanye Ver?
n=l 9438
7 ON (2.4.35)
ate) = S-natoe
n=1
Then
Y(k) = Xo(k)X(k) (2.4.36)
2N
~ 1wes p—(k-1)(n-1 94997
a(n) = wer Wye VOY (2.4.37)
‘We can extend to the case of three-dimensional convolution with three indices
as needed for the discrete dipole approximation. Let N,, Ny and N, points,
respectively, in @, 7 and 2 directions with N,, N, and N, all cqual to powers
of 2. Let
Ne Ny Ne
y(n,m,l) = > > Lan —n'jm—ml—U)x(n',m'U) (2.4.38)
n=l m'=1=1
is to be computed. For the sake of simplicity, we illustrate the scalar case.
The vector case follows by a simple extension. Then we have 3-D periodic
sequences & and Z2 with period M, = 2N,, My, = 2N, and M, = 2N.,
respectively in @, § and 2 directions. For one period of Z(n,m, 1) it is
a(n,m,l) l<n<N,andl<m<N,and1<l<N,
#(n,m,l)= 40 when Nz +1 <n <2,
or Ny +1<m<2N, or N,+1<1<2N,
(2.4.39)
The #2 for nonzero values can be computed as in Table 2.4.1. ‘Then the 3-D
DFT and inverse DFT can be performed accordingly.
--- PAGE 70 ---
46 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
n m Te Fa(n,m,1)
i eC
[N; + 2,2N,] Ny} LM] g(n—2N, —1m-1.1~-1)
[Nz + 2,2Nz] | [Ny + 2,2Ny] (1,.N.] g(n ~ 2N, —1,m—2N, — 11-1)
aM) | LM N,+2,2N,] | g(n—1,m~—1,1—2N,-1)
[N, +2,2N, iN. +2,2N.] | g(n—2N, —1,m—1,l-2N. —1)
[Le] | IN, +22] g(n—1,m—2N,-10-2N,-1) |
Nz +2,2N,] j[Ny + 2,2N,] g(n—2N, —1,m—2N,—1,12N.—1) |
Table 2.4.1 Computations for the nonzero values of &2(n, m,!).
5 Conjugate Gradient Method
Consider a matrix equation of the form
A¥=b (2.5.1)
where A is a N x N nonsingular matrix, x is the unknown column vector
and 6 is the right hand side. Both ¥ and 6 are N x 1 column vectors.

In the following we briefly describe the conjugate gradient method. De-
tails can be found in textbooks on matrix computation [Hestenes and Stiefel,
1952; Golub and Van Loan, 1996].

5.1 Steepest Descent Method
Let A be a real symmetric matrix and positive definite and $(Z) be the
functional
14s -
eZ) = ri AT—b (2.5.2)
where ¢ denotes transpose so that 7! is a row vector of dimension 1 x N. In
index notation
1 4
oF) = 5 So ai Aigay — SO aibi (2.5.3)
aj i
Taking the derivatives
) 1 1
-3~ =7-5 Aijxy ~ 5) ej Aji + bi
--- PAGE 71 ---
§5.1 Steepest Descent Method AT
=) — SO Agr; (2.5.4)
J
The second equality is due to the fact that
Aig = Aji (2.5.5)
Thus the gradient is
-Vo=b-AE (2.5.6)
Optimizing @ with respect to F gives
0=-Vg=b-Az (2.5.7)
‘This means that optimizing ¢ is equivalent to solving the matrix equation
AT=b.
The residual is the “left over” or the “remainder”. Let Zj—1 be the
(i — 1)th iterative solution. The residual is
71 =b- AR (2.5.8)
The direction vector d; gives the next solution
EF = Fi + ad; (2.5.9)
Jn the method of steepest descent, the direction vector is chosen to be the
same as the residual vector.
di =Fin (2.5.10)
Then the ith solution is
Fi = Fir + arin (2.5.11)
Substituting in (2.5.2), we have
O(F) = 6% 1 + ad)
1) 5\t= (5 s i 5\tz
=3 (Zi-1 + aid;) A (Ei-1 + agd;) — (F—-1 + aid) 6
= 2.
4= t= ste
= OCF) + od AB + Gd AG, — add
= we, = <
= d(Fi-1) + air yAT-1 + a jAT-1 — uF b
a ot os Cran es x
= bi-1) — WF ATi + DFAT (2.5.12)
Optimizing 6(%;) by taking its derivative with respect to a; and setting it
to zero gives
Tait
en (2.5.13)
T_ATiv1
--- PAGE 72 ---
48 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
In the steepest descent method, the direction vector is in the residual direc-
tion. On the other hand, in the conjugate gradient , the direction vector is
more general.
5.2 Real Symmetric Positive Definite Matrix
We first. summarize the results for the conjugate gradient method for real
symmetric positive definite matrix. At the zeroth step, let the solution be
Fo =0 (2.5.14)
At the (i — 1) th step, let %;_; be the approximate solution. Then
Fi = 6 - AFi-n (2.5.15)
is the residual at the (i — 1) th step. In particular,
Fo =5 (2.5.16)
To get a new solution ¥,;, i= 1,2,..., let
Ty =F + and; (2.5.17)
where d; is the unknown direction vector and a; is the unknown scalar to
denote the movement in the d; direction. To determine a; and d;, we note
that
bie 5 be i ass sty .
(Fi-1 + ayd;) = O(Fi-1) + aid; ATi-1 + ahi Ad; — aid; b (2.5.18)
Next determine d; by setting the second term to zero
z_,Ad; =0 (2.5.19)
The previous solution Z;_) for i =_2,3,... is be a linear combination of
previous direction vectors d),d2,...,dj—1. That is #1 € span{d),..., di-1},
for i = 2,3,....
‘Thus we have i — 1 equations,
Ad; =0 (2.5.20)
@Ad; =0 (2.5.21)
@_,Ad; =0 (2.5.22)
This is called a conjugation of d; to d), de, ds, ..., di-1.
_ Let Da be the N x (i — 1) matrix containing the column vectors
dy, dg, dg, ..., dia.
=t a
D,_, Ad; =0 (2.5.23)
--- PAGE 73 ---
§5.2 Real Symmetric Positive Definite Matrix 49
Then ,
(Bit + o4d;) = O(F 1) + tan Fa, ~aidb (2.5.24)
Minimizing (2.5.24) with respect to a; gives
ay = <_m (2.5.25)
d, Ad;
Next we relate the residual vectors of the ith step and the (i—1)th step.
Let
di =6 (2.5.26)
B= d (2.5.27)
then
7, = linear combination of 6 and Ab
= span {8,45} (2.5.28)
The residual vector at the ith step is
F = b— Az, = b— A(F_1 + a4d;) (2.5.29)
Fe =i — Ad; (2.5.30)
Since d; is A-orthogonal to previous direction vectors,
db=a (6 -Ax.-1) =dr-1 (2.5.31)
Using (2.5.31) in (2.5.25),
a 2m - dra (2.5.32)
d; Add; Ad;
The following are three properties concerning the properties of residuals
[Golub and van Loan, 1996]:
Property (A):
Dr; =0 (2.5.33)
Property (B):
span {d),d2,...,d;} = span {F0,71,...,7i-1}
= span {.%0, as, see a ‘ih
= span {ro Aro a Avo} =K (70.4.4) (2.5.34)
--- PAGE 74 ---
50 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
where K (Fo, A, 2) is the Krylov subspace.
Property (C): all the residuals are mutually orthogonal
FFj1=0 (2.5.35)
for i=0,1,2,...,7-2.
It then follows that [Golub and van Loan, 1996]
dy € span{7,—1,d,—1} (2.5.36)
Let
d; =Fi1 + Bid 1 (2.5.37)
Then from (2.5.23) and (2.5.37)
a@_, Ad, =d_, AT. + Bid, , Adi. =0 (2.5.38)
giving
4 = Ate (2.5.39)
q_ Adi
Also from (2.5.32) and (2.5.37),
a= dics = [ia tada) re (2.5.40)
@Ad; aA d;
On the other hand
dj_; € span{7o,71,...,7i—2} (2.5.41)
so that
Gar =0 (2.5.42)
Let
|Z? = zz (2.5.43)
be the L? norm. From (2.5.40) and (2.5.42),
a= Wrecall? (2.5.44)
aA d;
From (2.5.30) and using (2.5.35),
Fill? = 77; =747;4 — aur Ad, = -ayrt Ad; (2.5.45)
Then
Wri al? = er?) Adi = -aj1d; .. AF (2.5.46)
--- PAGE 75 ---
§5.2 Real Symmetric Positive Definite Matrix 51
because A is symmetric. Since dj-1 is orthogonal to 7;_1, and using (2.5.37),
0= 6h = dF 2 — ad, Ad =F _gh2 — -1d,_, Adi 4

(2.5.47a)
Thus
Feil? = asd, Ades (2.5.47)
Using (2.5.46) in (2.5.39), we have
1 Iria?
a= |Pear (2.5.48a)
m1 |G, Ads
Further, use (2.5.47) in (2.5.48a) to give
3 _ tral?
3, = —— 2.5.485,
8 Teal? 2480)
To summarize, the conjugate gradient algorithm for symmetric positive def-
inite matrix is as follows:
Fo =0 (2.5.49)
To=5 (2.5.50)
a =5 (2.5.51)
Foll2
oy = loll” (2.5.52)
dj Ad,
Ti =Tot+aid (2.5.53)
Fi =7y -mAdy (2.5.54)
For i > 2,
a — Weal? « ns
A= eo (2.5.55
= rol J
Ti + ides (2.5.56)
F,_1|I2
o; = Ball (2.5.57)
d;Ad;
Fj = Tia + ad; (2.5.58)
7 =Fi-1 —aAd; (2.5.59)
The iteration is stopped when the residual becomes small.
--- PAGE 76 ---
52 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
5.3 General Real Matrix and Complex Matrix
The procedure can be extended to general nonsymmetric matrix A that is
real and nonsingular (conjugate gradient normal equation residual method).
One can solve
Az=b (2.5.60)
in the following manner.
Consider the matrix
= ==
B=AA (2.5.61)
= =+t= = =
Then B = A A= B, so that B is symmetric. Also,
= == = = = 2
i By =a A Ay = (Ay)'Ay) = |[aal| =o (2.5.62)
Hence B is also positive definite. Since B is symmetric and positive defi-
nite, we can apply the results of (2.5.49)-(2.5.59) to the matrix B. Multiply
=t
(2.5.60) by A , we have
Br=t (2.5.63)
where
= sta
v=Ab (2.5.64)
= ==
In the algorithm, do not calculate B = A A because matrix-matrix multi-
plication is an O(N) procedure for a full matrix. Let
P=) -BE (2.5.65)
F=b-AE (2.5.66)
be the residuals respectively of the Band A matrix equations. Then
os! = rg
F=ATr (2.5.67)
The steps in the conjugate gradient method will be (2.5.49) (2.5.59), with
= =i =t=
F, and A replaced by 7, = A 7; and A A, respectively.
_ Suppose that we are solving equation (2.5.63), then Z = 0, 7% = a,
ad, =7%
(all?
624 (2.5.68)
© UPI?
dj =F_, + Bidi-1 (2.5.69)
--- PAGE 77 ---
§5.3 General Real Matrix and Complex Matrix 53
tll? |e Fie
= Weel” =; Hea” = Weal (2.5.70)
GBA |i a zal aa
Fi = Fy-1 + aid (2.5.71)
=7_ — a, Bd; (2.5.72)
=t =t =t=_
A 7, =A 7-1-0; A Ad; (2.5.73)
7 =Fi1— aj; Ad; (2.5.74)
Then the algorithm is as follows for real non-symmetric matrix:
Fo =0 (2.5.75)
To =b (2.5.76)
= te
ad; =7)=Ab (2.5.77)
tay?
irae _ [el
a= 2 = (2.5.78)
aba [Adl
FE. =To+od) (2.5.79)
FL =Fo-MAdy (2.5.80)
For i > 2,
. st 2
[ial? _ [Ar
an a TT (2.5.81)
[reall tral
- a =t .
d; =, + Bidi-) = AFi_1 + Bidi-1 (2.5.82)
=e 2
tro _ Pl
GQ = SS- = (2.5.83)
aa” Fal
Fi = Ti-1 + ad) (2.5.84)
FHT — Ad; (2.5.85)
In the algorithm, there is no matrix and matrix products. There are only
products of matrix and column vector.
For a general nonsingular complex matrix A, we solve the equation
Ar=b (2.5.86)
--- PAGE 78 ---
54 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
Let superscript + denote adjoint. The L? norm is defined by ||z||? = z'z.
The algorithm of conjugate gradient method is similar to that of the general
real matrix before with transpose replaced by adjoint. One can consider the
matrix
= st=
B=AA (2.5.87)
st p=ty* . ee
where A = (A ) is the Hermitian adjoint matrix of A. Then the compu-
tational steps become, on replacing ¢ by +
To =0 (2.5.88a)
T= 6 (2.5.88)
5 =
dy = AT (2.5.89a)
=+_ ||?
F'n|
a= (2.5.89)
[aa]
Fy =2o+ ard (2.5.89¢)
Fy =T) —Ady (2.5.89d)
and for 7 = 2,3,...
=i P
[Fs]
Bi = jg (2.5.90a)
Fro]
— =t =
dj =A Fi + Gidi-1 (2.5.90b)
2
=t
[a>
a = + (2.5.90¢)
[al
F = Fi-1 + aid; (2.5.90d)
Fi =Ti-1 — ai Ad; (2.5.90e)
_ Let A be a real matrix, then there exist orthogonal matrices of © and
V and diagonal matrix © such that
= ==st
A=UEV (2.5.91)
--- PAGE 79 ---
§5.3 General Real Matrix and Complex Matrix 55.
where
Es diag(ai,02,...,0n) 1 >o2 >... > 0,20 (2.5.92)
This is known as singular value decomposition. Using the L? norm for vectors,
let the matrix norm be
|| = max |aa| (2.5.93)
zI|=1
The relations between matrix norm and singular values are
{Al =o (2.5.94)
Since
=1 ==-1=t
A =VEY U (2.5.95)
=1
the largest singular value of A is 1/op.
\7"| 1 (2.5.96)
7 ao 5.96
On
The condition number is
= =| )J=01
k (4) = || | = (2.5.97)
on
If the condition number is large, the matrix solution can be unstable. To
change the condition number, pre-conditioning can be done.
Let
AzF=6 (2.5.98)
The goal is to find a pre-conditioning matrix Cc
# -CE (2.5.99)
=
E=C ¥ (2.5.100)
Then
=—-1 -
AC P=5 (2.5.101)
=
Multiply by C
Sles-l, =-l _
C AC #=C 6 (2.5.102)
Let
S sl==-1
A=C AC (2.5.103)
+ ele
v=C 5 (2.5.104)
--- PAGE 80 ---
56 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS
Then

=I, oo

Az =0 (2.5.105)
A judicious choice of the pre-conditioning matrix can drastically change the

= = =-1

condition number. To make the computation of A efficient, C and C — must
be simple matrices.
--- PAGE 81 ---
REFERENCES 57
REFERENCES AND ADDITIONAL READINGS
Anderson, M. G. (1965), Scattering from bodies of revolution, EEE Trans, Antennas Prop-

agat., 13, 303-310.

Barrett, R., M. Berry, T. F. Chan, J, Dammel, J. Donato, J. Dongarra, V. Eijkhout, R.
Pozo, C. Romine, H. van der Vorst (1993), Templates for the Solution of Linear Systems:
Building Blocks for Iterative Methods, SIAM Publications, Philadelphia, PA.

Borup, D. T. and O. P. Gandhi (1985), Calculation of high resolution SAR distributions in
biological bodies using the FFT algorithm and conjugate gradient method, IEEE Trans.
Microwave Theory Tech., 33, 417 419.

Brigham, E. O. (1988), The Fast Fourier Transform and its Applications, Prientice-Hall,
Englewood Cliffs, NJ.

Catedra, M. F., E. Gago, and L. Nuno (1989), A numerical scheme to obtain the RCS of
three-dimensional bodies of resonant size using the conjugate gradient method and the
fast Fourier transform, JEEE Trans. Antennas Propagat., 37, 528-537.

Chan, C. H. and R. Mittra (1987), Some recent developments in iterative techniques for
solving electromagnetic boundary value problems, Radio Sei., 22(6), 929-934.

Chew, W. C. (1990), Waves and Fields in Inhomogeneous Media, Van Nostrand Reinhold,
New York.

Gan, H. and W. C. Chew (1995), A discrete BCG-FFT algorithm for solving 3D inhomoge-
neous scatterer problems, J. Electromag. Waves and Appl., 9, 1339-1357.

Glisson, A. W. and D. R. Wilton (1979), Simple and efficient numerical techniques for treat-
ing bodies of revolution, Technical Report 105, Engineering Experiment Station, The
University of Mississippi, University, Mississippi.

Glisson, A. W. and D, R. Wilton (1980), Simple and efficient mumerical methods for prob-
Jems of electromagnetic radiation and scattering from surfaces, [EEE Trans. Antennas
Propagat., 28, 593 603.

Goedecke, G. H, and 8. G. O’Brien (1988), Scattering by irregular inhomogeneous particles
via the digitized Green's function algorithm, Appl. Optics, 27, 2431- 2438.

Golub, G. H. and C. F, Van Loan (1996), Matrix Computations, 3rd edition, Johns Hopkins
University Press, Baltimore, MD.

Goodman, J. J., B. T. Drain, and P, J, Flatau (1991), Application of fast-Fourier-transform
techniques to the discrete-dipole approximation, Optics Lett., 16(15), 1198-1200.
Gradshteyn, I. S. and I. M. Ryzhik (1965), Table of Integrals, Series and Products, Academic

Press, New York

Harrington, R. F. (1968), Field Computation by Moment Method, Macmillan, New York.

Hestenes, M. R. and E. Stiefel (1952), Methods of conjugate gradients for solving linear
systems, J. Res. Nat. Bur. Standards, 49, 409-436.

Jackson, J. D. (1975), Classical Electrodynamics, John Wiley & Sons, New York.

Jin, J. M, and J. L, Volakis (1992), A biconjugate gradient FFT solution for scattering by
planar plates, Electromagnetics, 12, 105-109.

Joseph, J. (1990), Application of integral equation and finite difference method to electro-
magnetic scattering by two dimensional and boy of revolution geometries, Ph.D. thesis,
Department of Electrical Engineering and Computer Science, University of Urbana-
Champaign, Urbana, IL.

Kas, A. and E. L.. Yip (1987), Preconditioned conjugate gradient methods for solving elec-
tromaguetic problems, IEEE Trans. Antennes Propagat., 35, 147-152.
--- PAGE 82 ---
58 2 INTEGRAL EQUATION FORMULATIONS AND NUMERICAL METHODS

Lakhtakia, A. (1992), General theory of the Purcell-Pennypacker scattering approach and its
extension to bianisotropic scatterers, Astrophys. J., 394(2), 494-499.

Lee, $, W., J. Boersma, C. L. Law, and G. A. De Champs (1980), Singularity in Green's
function and its numerical evolution, IEEE Trans. Antennas Propagat., 28, 311-317.

Livesay, D. E. and K. M. Chen (1974), Electromagnetic fields induced inside arbitrarily
shaped biological bodies, IEEE Trans. Microwave Theory Tech., 22, 1273-1280.

Mantz, J. R. and R. F, Harrington (1969), Radiation and scattering from bodies of revolution,
Appl. Sci. Res., 20, 405-435.

Miller, E. K., L. Medgyesi-Mitschang, and E, H. Newman, Eds. (1992), Computational Elee-
tromagnetics: Frequency-Domain Method of Moments, IEEE Press, New York.

Oppenheim, A. V. and R. W. Schafer (1975), Digital Signal Processing, Prentice-Hall, En-
glewood Cliffs, NJ.

Peterson, A. F. and R. Mittra (1984), Method of conjugate gradient for the numerical solution
of large body electromagnetic scattering problems, J. Opt. Soc. Am., 2, 971-977.

Peterson, A. F. and R. Mittra (1985), The convergence of the conjugate gradient method when
applied to matrix equations representing electromagnetic scattering problems, IEEE
Trans. Antennas Propagat., 34, 1447-1454. J. Opt. Soc. Am., 2, 971-977.

Peterson, A. F., S. 1. Ray, C. H. Chan, and R, Mittra (1991), Numerical implementations of
the conjugate gradient method and the CG-FFT for electromagnetic scattering, PIER
5, T. K. Sarkar, ed., Elsevier, New York.

Peterson, A. F., 8. L. Ray, and R. Mittra (1997), Computational Methods for Blectromagnet-
ies, IEEE Press, New York.

Poggio, A. J. and E. K. Miller (1973), Integral equation solution of three-dimensional seat
tering problems, Computer Techniques for Electromagnetics, R. Mittra, ed., Pergamon,
New York.

Purcell, E. M. and C. R, Pennypacker (1973), Scattering and absorption of light by non-
spherical dielectric grains, Astrophys. J., 186, 705-714.

Rao, 8. M., D. R. Wilton, and A. W. Glisson (1982), Electromagnetic scattering by surfaces
of arbitrary shape, [EBE Trans. Antennas Propagat., 30(3), 409-418.

Sarkar, T. K. (1991), editor, Application of Conjugate Gradient Method to Electromagnetics
and Signal Analysis, PIER 5, Elsevier, New York.

Sarkar, T. K., E. Arvas, and S. M. Rao (1986), Application of the fast Fourier transform
and conjugate gradient method for efficient solution of electromagnetic scattering both
electrically large and small conducting bodies, IEEE Trans. Antennas Propagat., 34,
635-640.

Sarkar, T, K., X. Yang, and B. Arvas (1988), A limited survey of various conjugate gradient
methods for complex matrix equations answering in electromagnetic wave interactions,
Wave Motion, 10, 527-546.

Singham, S. B. and G. C, Salzam (1986), Evaluation of the scattering matrix of an arbitrary
particle using the coupled dipole approximation, J. Chem. Phys., 84, 2658-2667.

Stoer, J. and R. Bulirsch (1992), Introduction to Numerical Analysis, 2nd edition, Springer-
Verlag, New York.

Tsang, L., J. A. Kong, and R. T. Shin (1985), Theory of Microwave Remote Sensing, Wiley-
Interscience, New York.

Van Bladel, J. (1961), Some remarks on Green’s dyadic for infinite space, JRE Trans. Ant.
and Prop., 9, 563-566.
--- PAGE 83 ---
REFERENCES 59

Van Bladel, J. (1991), Singular Electromagnetic Fields and Sources, Oxford, Oxford Univer-
sity Press.

Wang, J. J. H. (1991), Generalized Moment Methods in Electromagnetics, John Wiley and
Sons, New York.

Yaghjian, A. D. (1980), Electric dyadic Green's functions in the source region, Proc. IBEE,
68, 248-263.

Zwamborn, P. and P, M, van den Berg (1992), The three-dimensional weak form of the
conjugate gradient FFT method for solving scattering problems, IEEE Trans. Microwave
Theory Tech., 40(9), 1757-1766.
--- PAGE 84 ---
Scattering of Electromagnetic Waves: Numerical Simulations.

Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.

Copyright © 2001 John Wiley & Sons, Inc.

ISBNs: 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)

Chapter 3
SCATTERING AND EMISSION
BY A PERIODIC ROUGH SURFACE
1 Dirichlet Boundary Conditions 62
1.1 Surface Integral Equation 62
1.2 Floquet’s Theorem and Bloch Condition 63
1.3 2-D Green’s Function in 1-D Lattice 64
14 _ Bistatic Scattering Coefficients 67
2 Dielectric Periodic Surface: T-Matrix Method 68
2.1 Formulation in Longitudinal Field Components 69
2.2 Surface Field Integral Equations and Coupled Matrix Equations 74
2.3 Emissivity and Comparison with Experiments 81
3 Scattering of Waves Obliquely Incident on Periodic
Rough Surfaces: Integral Equation Approach 85
3.1 Formulation 85
3.2 Polarimetric Brightness Temperatures 89
4 Ewald’s Method 93
4.1 Preliminaries 93
4.2 3-D Green’s Function in 3-D Lattices 98
4.3 3-D Green’s Function in 2-D Lattices 102
4.4 Numerical Results 105
References and Additional Readings 110
~61—
--- PAGE 85 ---
62 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The scattering of waves from a periodic surface has been studied exten-
sively. Two methods of solution wil! be used in this chapter: (1) the method
of moments based on periodic Green's function and (2) the T-matrix method.
In Section 1, the problem of a one-dimensional periodic rough surface with
Dirichlet boundary condition is illustrated. In Section 2, we consider the
case of vector electromagnetic wave obliquely incident on a one-dimensional
periodic rough surface. The incident direction is also at a nonzero azimuthal
angle with respect to the periodic direction. This problem has applications
in polarimetric passive remote sensing of rough surfaces because the third
and fourth Stokes parameters are nonzero. The components of the electric
and magnetic fields along the row direction are used as unknown scalar func-
tions to reduce the vector nature of the problem to a scalar one. Then, the
extended boundary condition (EBC) approach with Fourier series expansion
for the surface fields is used to obtain the matrix equations governing the
scattered field amplitudes. In Section 3, we study the vector electromagnetic
case using integral equation method. In Sections 1 and 3, the periodic surface
is one-dimensional, and the Green’s function is two-dimensional. A method
of speeding up the computation of 2-D Green’s function in 1-D lattice is pre-
sented. In Section 4, we describe Ewald’s method of computing 3-D Green’s
function in 3-D lattice and 2-D lattice. Besides rough surfaces, periodic
structure problems are studied extensively in frequency selective surfaces
[Chan, 1995; Munk, 2000] and photonic bandgap materials [Yablonovich,
1987; Joannopoulos et al. 1995).
1 Dirichlet Boundary Conditions
1.1 Surface Integral Equation
Consider a. plane wave incident upon a periodic surface with height function
z= f(x), such that f(e+P) = f(x). The period of the rough surface is P in
the &-direction. The incident direction is in the 2-2 plane. The electric field
of the incident wave is given by
EF, =5eh" (3.1.1)
where k; denotes the incident wave vector and is given by @kiz — 2kiz with
kig = ksin 6; and kj, = k cos@;. We have 7 = ¢x + 2z. The electric field Ey
satisfies the two-dimensional wave equation
2 2
Ga + =) Ey +B, =0 (3.1.2)
--- PAGE 86 ---
§1.2 Ploquet’s Theorem and Bloch Condition 63
The Green’s function is
er) —t HO alee) <2 [ ae, 2 exp like(2 — 2’) + ik
GFF) = gto (klF-F|) = rs [. dkz, mee [ihe (@ — a!) + ik, |z — 2'|]
(3.1.3)
where kz = (k? —k2)'/?, Making use of Green’s function of region 0, we have
20
Eq(F) — | do! [ORF )A- V' By) — Bylr)Aa- Var}
90
_JE,(F) z> fla) :
= {5 z<fz) 14)
and
aa ls FO) 5
da’ = : 8 da! (3.1.5)
For Dirichlet boundary conditions Ey = 0 on the surface, the integral
equation in (3.1.4) becomes
oo
Byi(a.2 = f(2)) = fda! G(x, f(a)sa!, f(a) VEY) ogee (81.5)
00
Let the unknown surface variable be denoted by u(x) so that
a)dx = (doh: VE,(F 3.1.
u(e)de = (don ¥ W)) (3.1.7)
Equation (3.1.6) becomes
20
etre ikis S(t) — | dr'G(a, f(x); 2", f(2’))u(2’) (3.1.8)
1.2 Floquet’s Theorem and Bloch Condition
‘The left-hand side of (3.1.8) has the following translational property
gibie(@=nP)~ikief(e+nP) _ gikienP pikize—iki. f(x) (3.1.9)
Letting a be replaced by x + nP in (3.1.8) and using (3.1.9), we have also
a! a! +nP.
20
cikianP gikset—ike. f(t) — | de! Ga + nP, f (x):2! + nP, f(a")u(a! + nP)
—00
= | de'G(a, f(x); 2’, f(x))u(e! + nP)
~ poo
= cikianP | dx'Gle, f(a);«!, f(a!)Ju(a’) (3.1.10)
J-s0
--- PAGE 87 ---
64 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The second equality in (3.1.10) is a result of translational invariant property
of G. Thus we have
u(a’ + nP) = e*"Pu(e’) (3.1.11)
Equation (3.1.11) is known as the Floquet’s theorem and is generally true
for periodic structures. Thus one write
u(x) = e*="w(x) (3.1.12)
where w(x) is a periodic function with period P. From (3.1.12), we have the
Bloch condition
u(x + P) = cP u(x) (3.1.13)
The surface integral in (3.1.8) is over infinite domain. However, it can
be condensed into a single period. Let the center period be from —P/2 to
P/2. Thus, using (3.1.8), for —P/2 <x < P/2 we have
cikver—iks. f(a)
20H P/2+mP
= 1 | dx'G(x, f(x); 2', f(x’))u(e’)
mors 1 ~P/2+mP.
P/2 oo 5
= [ dx! S> G(x. fa);2! + mP, fle’)? ule’) (3.1.14)
—P/2 m=—00
The second equality in (3.1.14) is a result of changing dummy variables of
integration from 2x’ to x’ + mP and using Floquet’s theorem for u(x).
1.3 2-D Green’s Function in 1-D Lattice
From (3.1.14), one can define the periodic Green’s function
0
G,(a, 42',2') = Ss Ge, 2;2' + mP, 2/)eibemP (3.1.15)
m=-00
Thus for —P/2 <a < P/2 the integral equation of (3.1.14) becomes
; Pp
eibect—ikecf (0) = / da! G(x, f(x):2!, f("))u(2") (3.1.16)
=P/2
Thus the advantage of (3.1.16) is that the integral equation is reduced to
matching the left- and right-hand sides over only one period of the periodic
medium instead of over an infinite domain. However, instead of the free space
Green’s function G, we have to compute the periodic Green’s function G,
which is an infinite series as represented by (3.1.15).
--- PAGE 88 ---
§1.3 2-D Green’s Function in 1-D Lattice 65
From (3.1.3) and (3.1.15) we obtain
- 2
Gpla, 232.2) = j So chem? HY (ke — a — mPP + (2 2)
m=—00
(3.1.17)
Equation (3.1.17) is the periodic Green’s function in spatial domain. As
m — oo, the terms inside the summation decay as 1/m. One can express the
result in the spectral domain by making use of the spectral representation
of the free space Green’s function
Gp(x, 232" nat > [tee iky(2—a!—mP)+ik: 1) oikismP
ip(a,25a',2!) = 2 pkey. exp(ik,(x—2'—mP)+ikz|2—2'|)e'
m=—00
(3.1.18)
We next make use of the property of Fourier series that
y> clamp FS ( a") 3.1.19)
e€ => a =>" wd.
en PE Le
where 6 is Dirac delta function. Equation (3.1.19) simply states that a pe-
riodic train of impulses with period 27/P can be represented by a Fourier
series with the Fourier coefficient equal to P/27. Substituting (3.1.19) in
(3.1.18) gives the periodic Green’s function in the spectral domain.
0
Gp(x, 2:2", 2/) = sp > i exp(ikem(x — 2’) + ikem|2 — 2'|) (3.1.20)
m=—o0
where kom = Kig + 2mm/P and kim = (k? — k2,,)'/?. For kum < k, we have
propagating Floquet modes. For kr, > k, kz becomes imaginary giving rise
to evanescent Floquet modes. The spectral form of (3.1.20) does converge
rapidly for large values of |z—2z’| due to exponential decay, but we often need
to evaluate this function for small or zero values of |z — z'| in which case the
summation is slowly convergent. Here, we present a general transformation to
speed up the convergence of summation that is due to Veysoglu et al. [1991].
We start from the expansion
x
7 = em Seite (3.1.21)
m=1
Multiply both sides by q(v) and integrate from 0 to oo. This gives
es mo q(v)
doe Q(m) = ef a (3.1.22)
mah ° ove
where
--- PAGE 89 ---
66 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
oo
Q(m) -[ dy qv) (3.1.23)
0
is the Laplace transform of q(v).
Next, we make use of the following Laplace transform integral using
Bessel function of order 1/2 [Oberhettinger and Badii, 1973}.
- ; i2 cos (a(y? — 2iy)!/?)
; Hf ( 2 2 ve) --2/ dy env t t 3.1.24
eae te) why “YS (y? — 2iy)V/? ( )
Let
s =—k(x — 2! —mP) (3.1.25)
a=k(z-2') (3.1.26)
in (3.1.24), This gives
oth? HD (kV /(e— a! —mP PP + (2 — 2)
m 0 (y? — 2iy)'/?
(3.1.27)
Changing dummy integration variable from y to v = kPy gives
eth? HOE (a — 2! —mP)? + (z— 2)?)
ogy \ V2
wD a ces weet ati 18)")
_ dven™ |— nike 2) g(e=2")o/ P
0 akP ( uy? = By?
PP? — kP
(3.1.28)
Comparing (3.1.28) with (3.1.23) shows that the left-hand side of (3.1.28)
is Q(m) while g(v) is the square bracket on the right-hand side of (3.1.28).
Use Q(m) and q(v) from (3.1.28) and substitute into (3.1.22). We also let
t= (Kir +h)P (3.1.29)
These give
co
So heh HY (ke = a — PP + 2)
m=1
2 »\ 1/2
oo % _, con (a (sips ~ 28) )
— git dv _ enik(a—2') (a—a')u/P
Jo ev—elt | ckP (gp - Biv y 1?
EP — RP
(3.1.30)
--- PAGE 90 ---
§14 Bistatic Scattering Coefficients 67
‘Transforming dummy variable from v to u? = v/(kP) gives
aa)
Gyla, 232',2!) = 5 SO clk? HY (ke = a! = mPP? + (2 —2/P)
m1
cil kio + k)P p—ik(2—2")
= x
w
oo LW kP+K a2? cog (k(x — 2Julu2 ~ 2%) 2
x L608 (2 = 2')ulu? = 26)77) (3.1.31)
0 1 — ce tkP a i(k FE) (u2 — 21/2
This integral is rapidly convergent due to exponential decay and can casily be
evaluated by using Romberg integration. Having the formula for the periodic
Green’s function, one can use the method of moments to solve (3.1.16) for
the unknown surface variable by matching over one period of rough surface
-P/2<a < P/2
1.4 Bistatic Scattering Coefficients
Once the surface field u(x) is calculated, the scattered field for z > f(x) is,
on using (3.1.4) and (3.1.6)-(3.1.8),
2°
EY) = -| da! G(x, 2:0", f(x’))u(e') (3.1.32)
—00
‘The integral in (3.1.32) can again be condensed into one period
P/2
E,(r) = -|[ dr! Gy(a, 2,2, f(x))u(a’) (3.1.33)
-P/2
We use (3.1.20) in (3.1.33) to get
oe
Bs7) = So theme? Bry (3.1.34)
m=—00
where
i PPP ig them fl2")y (ol
Bn = - ap | da! ee Bam FE ag! 3.1.35
=~ ape | on ) (3.1.35)
Note that only propagating Floquet modes carry time-averaged radiation
power. The incident power on the rough surface over a period P is Pw/2y,
where w is the width in the §-direction. The time-averaged power contained
in scattered wave is equal to —E}/(2iwj) (QEy" /Iz) Pw. Thus the fractional
power is
ake
Pn = |BmP (3.1.36)
--- PAGE 91 ---
68 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
for the mth propagating Floquet mode. Conservation of energy requires
> Pm =1 (3.1.37)
m=propagat.
modes
For the case of large P with P much bigger than wavelength, the propagating
Floquet modes can approximate a continuum of scattered angles. Let
2am :
Kam = hie + > = ksin 0, (3.1.38)
represent the transformation between k,,,, m, and scattered angle 6,. Thus
27am
Akom = —S— 1.39
m= (3.1.39)
Since Am = 1,
P P pre
So Am() = 5= | dhtem() = = dk cos 0, () (3.1.40)
Qn Qn Jon/2
m
where ( ) stands for a mathematical expression. Such transformation between
discrete and continuum as represented in (3.1.40) is customarily done in solid
state physics when a periodic boundary condition is applied to truncate the
domain to a finite size. Thus
P opr ok,
P= [ dB. 6089, |B (3.1.41)
rm Qn Jin k
If we let
om [2
Pa = | d0,0 (0s) (3.1.42)
m cam /2
where o(9,) is the bistatic scattering coellicient, we have
Pk
o(0s) = 5 cos” 43 |Byn|” (3.1.43)
TT
for the propagating mth Floquet mode (i.e., |kiz2m| < ). Equation (3.1.43)
expresses the bistatic scattering coefficient in terms of Floquet mode ampli-
tudes.
2 Dielectric Periodic Surface: T-Matrix Method
In this section the scattering of electromagnetic waves from dielectric peri-
odic rough surface is studied. We consider the case of oblique incidence and
also at an arbitrary azimuthal angle with respect to the row direction. In
the formulation, the components of the clectric and magnetic fields along the
--- PAGE 92 ---
§2.1 Formulation in Longitudinal Field Components 69
Region 0 1. €
NS 2
y
NS |
i P
Region 1 p, €

Figure 3.2.1 Geometrical configuration of the problem.
row direction are used as unknown scalar functions to reduce the vector na-
ture of the problem to a scalar one. The rough surface is invariant along the
row direction. Then, the extended boundary condition (EBC) approach with
Fourier series expansion for the surface fields is used to obtain the matrix
equations governing the scattered field amplitudes. In general, the E-waves,
which are characterized by the components of the electric fields along the row
direction, and the H-waves, which are characterized by the components of
the magnetic fields along the row direction, are coupled together. Results are
illustrated with sinusoidal profiles. The scattered power calculated is shown
to satisfy reciprocity and energy conservation. The emissivity of a periodic
rough surface is calculated from one minus the reflectivity. We also show
good comparison with experimental data.
2.1 Formulation in Longitudinal Field Components
Consider a plane wave incident upon a periodic surface described by f(x) =
f(a +P), with P denoting the period of the surface in the @-direction
(Fig. 3.2.1). The electric field of the incident wave is given by

E, = @Bne™* (3.2.1)
where k; denotes the incident wave vector and is equal to &kin + jkiy — 2kiz
and @; is the polarization of the electric field vector.

Since the structure is uniform in the g-direction, all the field components
in both region 0 and region 1 will have the same exp(ikiyy) dependence.
With this dependence, we can replace 0/Oy in Maxwell’s equation by ikiy.
It is possible to express all field components transverse to 7 in terms of
longitudinal field components in the #-direction. Unless otherwise specified,
we will suppress the exp(ikiyy) dependence.
--- PAGE 93 ---
70 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
In terms of the longitudinal components, the transverse components are
= i =
Bye) = te [keh lh) +en¥ «Hi 220)
jy
— i _ =
Hye(?) = gape [bv Voie P) — wesVs x Eyy(r)] (8.2.26)
jy
where j = 0,1 signify regions 0 and 1, respectively, Vs is the transverse
gradient operator that is transverse to j-direction
0 a)
Ve=25>+22- 3.2.
a= * 9, + #9, (3.2.3)
and Ej; and Hys denote the transverse components of the clectric and mag-
netic fields for region j. The subscript 7 = 0 is suppressed. The E-waves are
described by Hjy = 0 and H-waves are described by Ejy = 0. The longitudi-
nal components Ej, and Hj, satisfy the equations
(V2 + kj — kz) Ey =0 3.2.4)
STN Si) | Hy f (3.2.
We let
Dy = ba + 22 (3.2.5)
be the position vector that is transverse to the j-direction. Since Hj, and
Hj, satisfy a two-dimensional wave equation, we shall use a two-dimensional
Green’s function. The Green’s function is
— ta - 4 .
(4.0) = SH)” (kis |B. ~ P4)) (3.2.6)
where j = 0,1 and
12 <
keys = (Aj — kR,) (3.2.7)
Note that the Green’s function is similar to (3.1.3), except that k has been
replaced by kjs of (3.2.7). Integral equation can be formed by applying ex-
tinction theorem to Ey and Hy, separately. We also make use of Floquet’s
theorem to condense the integral equation for one period using a procedure
similar to that in Section 1. We have
E(B.) ~ | da’ {Gr(P Fe) A VyEy(B.) ~ EP.) VG PPP}
Jp
_ J Fy.) => Fle) (3.2.82)
0 2< fle) (3.2.8b)
--- PAGE 94 ---
§2.1 Formulation in Longitudinal Field Components 7
where the integration do’ is over one period P, and similarly
Hy(B.) ~ fda! {Gel VHP.) ~ Hy(P.)A- V.Ge(PusP.)}
_ fp.) 2> Fe) (3.2.94)
~ 10 z< f(x) (3.2.90)
where
 — ls, F@) :
do! = [: 8S | da! (3.2.10)
and
- vy ai yp tl oo) ah |e ol 2 4
Gp(D,, 7.) = WP > kan expliken(x — 2') + iken|z — 2'|] (3.2.11)
is the periodic Green’s function of region 0. In (3.2.11)
ken = hig + sa = han (3.2.12)
Keen = R23 — Kin = 9) B? — ky — by = BesiBn (3.2.13)
Making use of periodic Green's function of region 1, we have
[42 {Gir PsP) A: VB ag) ~ Big Fe) VCP Po}
_ fo 2> f(x) (3.2.14a)
= Biy(B) 2 < Fla) (3.2.14b)
[ to! {Grr(..06) AV. Hig Oe) — HiylD,) A VC ePP)
JP
_ fo z> f(x) (3.2.15a)
© | AiO) 2 < f(x) (3.2.15b)
where
ayo! 1 tka (a —a!) +i. 2 3 5
CrP PoP) = 5p u ba expliken(e — 2’) tikien|z—2'|] (3.2.16)
is the periodic Green’s function of medium 1, and
Bian = (KE — hy — REy)'? = (Rh, — Bin)'/? = kasi, (3.2.17a)
kan = hie + ma = hysal, (3.2.17)
--- PAGE 95 ---
72 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
k,
ky
= -\ ky
X((/ AS ‘
aa
—k
LAAN
Figure 3.2.2 Conical diffraction of the reflected wave in region 0.
We see that the waves are propagating in discrete Floquet modes forming
a cone shape when the observation point is either above the highest point
or below the lowest point of the surface (Fig. 3.2.2).
Let fmar and fmin be respectively the maximum and minimum values
of the surface profile f(x), Then
FB.
Ey, (ps) = EyilD, bn > . 3.2.18:
(Ps) = Byi(Bs) + s bn ae > Sma (3.2.18)
clk PB
0 = Eyi(p,) — i < n 3.2.186
vil.) Lm Ti Sani (3.2.188)
py cin Pe
Hy(P,) = Hyi(P,) + > oe fara 2>fmar  (3.2.19a)
" On,
(pe) ral etka
0 = Ay(p,) — So a ox < fm (3.2.19)
yt 7 n 5, hn min
where
Be = hep + Fk (3.2.20)
--- PAGE 96 ---
§2.1 Formulation in Longitudinal Field Components 73
denote the propagation vectors of Floquet modes. We recognize that b, and
of ) are scattered field amplitudes. The coefficients an, bn, al?) and a ) are
related to the surface fields by the following integrals,
+. c+
1 pferrPle) yay op OTe P(@)
n= sep [do {SE Al VB (Ay) — Eyl) A! Ve
(3.2.21)
and of is the same expression as b, with Ey replaced by Hy.
-1 fern PR@) cp op Othe BEY
On = TEP [ do Tk fl - VL Ey (,) — Ey(Bs) 2 Vee
(3.2.22)
and af?) is the same expression as a, with Ey replaced by Hy. In (3.2.21)
and (3.2.22)

D(x") = tu + 2f(e') (3.2.23)
is a point on the periodic surface. Similarly, making use of (3.2.14) and
(3.2.15), we obtain

etki Be .
0= LB ae 2> faz (3.2.24a)
7 Pa
y eikin Be (
E,y(.) = >) An—— 2 <i 3.2.24b)
y\Ps 2 Vi min
rt
h) Ekin Ba aor
o=->> Bi TE 2> fmax (3.2.25a)
7m
che? ,
Aiy(p,) = >- AY Te 7s imin (3.2.25)
7 Pr
where
1 en BAe)
Boe f dg (er Ov VE

"= Seep | { Ta Vain)

en BAe)
~ Eyl) V5 ————} (3.2.26)

Bi) is the same expression as B,, with Fj, replaced by Hi,
--- PAGE 97 ---
74 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
"Dik P Jp” VR es
Cin Ba’)
— Ey,(9,) a! - Vi, — (3.2.27)
Vio,
A is the same expression as A, with Ey, replaced by Hy,, and
zt +
kin = fkien + Zhen (3.2.28)
are the propagation vectors of the Floquet modes in region 1. By using
(3.2.18) and (3.2.19b), we can readily solve for a, and aS” in terms of
incident wave amplitudes.
an = dno VV 30 Eo (6: >) (3.2.29)
Hot on
a) = b9/3o on (ki x @:-9) (3.2.30)
Also, from (3.2.24) and (3.2.25) we obtain
B, = BY =0. for all n (3.2.31)
Given a, a, Br, and Bw in (3.2.29) (3.2.31), we next formulate matrix
equations to solve for the surface fields. After the surface fields are solved,
then the scattered ficld amplitudes b,,, bf, Ay, and AS” can be obtained
using (3.2.21) and (3.2.27).
2.2 Surface Field Integral Equations and Coupled Matrix Equa-
tions
The surface integral equations are, from (3.2.22), (3.2.29), (3.2.30), and
(3.2.26),
an = dno V/ GoBo(6: * G)
-] da! otk, BAe") al VIE (GL
= aap |, 7) RNs 'y(Ps)
B(p) i Vy 3.2.32
—E,(p,) 0 ° Tie (3.2.32a)
--- PAGE 98 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 75
. 1 nr
all) = bn0V/Bo— (Ie: x + 9)
wy
-1 a ff ik Ba) VHA
~ a Jot | yay
H, (pi) WV" one) 3.2.32b)
_ py) + —S—S—— ye da
y\Ps + Tha (
1 , enh B,(2’) a ,
By, =0= —— | d ———— _ i’ - VF, (Pp
eB)
1 (atv et ot
— Ey, (pi) a anya (3.2.32c)
Pr
1 sf niki, Bala’)
BY =0= —— | do! §-—__—_ a. Vi, (7h,
t 2ik.P Jp” va". 1y(Ps)
oF Ble’)
~ Hi, (7) a - Va (3.2.32d)
On
However, in the four equations of (3.2.32a)-(3.2.32d), there are eight un-
knowns Ey, Hy, 2-VsEy, %- VsHy, Ey, Hy, 2-VsE1y, and t-VsHiy. We
need to impose four boundary conditions to obtain a total of eight equations
for the eight unknowns.
Applying the boundary conditions for the tangential electromagnetic
fields on the periodic surface S, we have
Ey = Evy (3.2.32)
Hy = Hy (3.2.336)
AX Es =x Bs (3.2.33c)
Ax H,=AaAx hs (3.2.33d)
where E,, Hs, E,, and Hy, are related to By, Hy, Eiy, and Hyy by (3.2.2).
Equations (3.2.33a) and (3.2.33b) relate the four unknowns. Next we need
to put (3.2.33c) and (3.2.33d) as conditions on the eight unknowns,
From # x Bs = x F4,, (3.2.2) and (3.2.26),
Kiy . , WH. = kiy . win. za
ra x VsEy + ee x (Vs x Hy) = R" x VsBty + u" x (Vs x Aly)
(3.2.34)
--- PAGE 99 ---
76 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
Note that
x (V, x Ay) =: Va dy (3.2.35)
where Ay = 9A,(p,). Thus,
Kk
yx V7, Bye (iV Hy) = [higix Vo Bay weer j(A-VeHy)| (3.2.36)
is
From (3.2.33a) and (3.2.33) we have two relations
E,|v,z = f(«)| = Eyle,2 = f(2)] (3.2.37a)
Ay{x,2 = f(x)] = Aiy|x,2 = f(x)] (3.2.376)
Note that the surface fields (with z = f(x)) Ey, Hy, E1y, and Hyy are
functions of x only. If we take total derivative of (3.2.37a) with respect to x,
we have
dE, OE, , OE, df(z) _ OFty , OEtydf(x) _ dFy
de Oc * dz de Oc | dz dz de (3.2.38)
with 2 = f(x). Since
._[ df... df\?| *
s-[-de44 f(D
we get
2177 7, 0
axe, = li+ (4 Ofy , af OBy
" dx Ox dx Oz |, 42)
dg\?| * dEy
=|1 = —_ 3.2.39
+ (4) dx (3.2.39)
From (3.2.38) and (3.2.39), it follows that
ix VeBy =x VsEly (3.2.40a)
a GHy — diliy
Similarly, Tp da 8° that
AX VaHy = x Valy (3.2400)
Putting (3.2.40a) and (3.2.40) in (3.2.36), we have
U(@- VsHy) = —don x VsE1y + doi(ti- VsHiy) (3.2.41)
where
ke ky
do = [# _ 7 Kay (3.2.42a)
Ki, | wy
al ke .
= (3.2.42b)
--- PAGE 100 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 7
Equation (3.2.41) is a result of applying ? x E, =n x Ej,. If we apply the
same procedure to? x Hy =n X His, we get
H(i Vs Ey) = cof x Vs Hay + co9(- VE ty) (3.2.43)
where
ke k,
co = le - i oe (3.2.44a)
ek?
2 = 3.2.44b
a= E, (3. b)
Using (3.2.39) and the like in (3.2.41) and (3.2.43), we get respectively
do ue
ft: (V Hy) = Trap +do(i-VsAiy) — (3.2.45a)
1 a
+ (Z)
diy
os
fee (Vshy) = a + c(i: VsE ly) (3.2.45b)
i4(2
dx.
Equations (3.2.37a), (3.2.37b), (3.2.45a), and (3.2.45) provide the four re-
lations for the eight surface fields Ey, Hy, Evy, Hiy, 1» Vsby, V+ VsHy,
h-VsEiy, and ni» VsHiy. The integral equations (3.2.32a-d) provide the
additional four integral equations.
Surface Field Expansion
As indicated in Section 2.1, the surface fields obey Floquet’s theorem; that
is, (a) = exp(ikizr)w(x), where w(x) is a periodic function with period P.
Thus one can expand w(x) in a Fourier series. We use such expansion for
the surface field components as follows. With p,(%) = #x + 2f(z), let
. _ on , A
Ey |p,(e)| = Exylp,(x)] = > 2a% exp [hi + in'5] (3.2.46a)
2
doit VsEvy[P,(2)] = tkisde S~ 23% exp it + ine] (3.2.46b)
n
7 1 ; . 2 .
H,[p.(0)| = Haylpg()} = D> 298 exp [tie + in} (3.2.46¢)
”
--- PAGE 101 ---
78 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
n a . <8 . _ 20
dot VsHiylq(x)] = ikiede Y> 253 exp thine + in551| (3.2.46d)
n
From (3.2.45a), (3.2.45b), and (3.2.46a-d),
— 2
don: VsHy = dey [-ar2asi ( + ar) + dei.26
n
Qn
x exp [tae + in| (3.2.46e)
= 27 .
doit V.By = de > [oor (be + 7 + ail. 24)
7
. 2a 7 .
x exp [thier + inge (3.2.46f)
Thus all cight surface field components are now expressed in terms of four
sets of unknown coefficients af, 3%. 78, and 6%. Substitute the surface field
expressions of (3.2.46a d) in the two surface integral equations of (3.2.32c)
eto se
and (3.2.32d). Define Qp,, Qu, as the Dirichlet and Neumann matrices with
clements
ot
[2]
mn
-1 Fin Bala) : On
= _- [oe exp ikigt + ine
a | inexp | —i(m — n) a — ikig +6) f(a) (3.2.47)
=> | deexp|-i(m—-n)>2-i f x 3.2.4
PV, Pp xP P URLs m
sot
[2s]
mn
1 ien-V e-in Bal2) een int
= mp [or oe oP i int + ina]
-1+a',a), [ . Qn, _
= xp | —i(m — n)—x — ik 5 x 3.2.47b
La, VHP pdPep i(m — n) ptt isftG,)f(x)| 7b)
where the integrations are performed over one period. We obtain the two
matrix equations
st as =t =
—Qp, 8 -Qy, -@=B=0 (3.2.48a)
= is st —
Gp, 3° - Oy, 7 =B” =0 (3.2480)
In deriving the second equality in (3.2.47b), we have performed an inte-
--- PAGE 102 ---
§2.2 Surface Field Integral Equations and Coupled Matrix Equations 79
gration by parts. Here the vectors B, BY, a*, 3°, 7, and 6° contain the
elements B,,, Bo, as, 68, yn, 68, respectively. Similarly, substituting the
surface field expressions of (3.2.46a—d) in the surface integral equations of
(3.2.32a) and (3.2.326), we get the equations in the following matrix forms
= kiss- oe =
T= COQny V+ eZ Qn, ‘B+Qn,% (3.2.48¢)
= kigz- zs ee .
A) = ~doQiys O° + "0 ip, 8 +Qy, 7% (3.2-48d)
‘8
where @ and a") are the column vectors containing the known coefficients a,
and a!" respectively, while Qj, denotes the hybrid matrix which couples
a and 7 to @ and a"), and
[2 | = [ deexp |—i(m — n) ee ~ tke(£Gn)f(0)| (3.249)
=— -i(m—n)= 2-1 x 3.2.46
Ps) an Pf Be fp OPO? pe NSP
+t —l+aman - Qi .
(2x, mm TBnVinP [dro [itm - npr - ik) (2)
(3.2.49b)
ct a
[Qian] =-On, [2p,| (3.2.50)
mn mn
Equations (3.2.48a-d) can be put into the following matrix equation.
= kis=- = as _
Qn, FQ, COQny1 0 ° e
's
= = kys=- ci ath)
=doQhyi 0 Qn, a7-Qo, = (3.2.51)
=t+ = . As
Ons @p, 0 0 . 8
0 0 @y, Gp, LS 0
The unknown vectors @*, 8”, 7°, and d° for the surface ficld expansions are
obtained by solving the above matrix equation. After the coefficients @, 2,
7, and 5° are solved, the upward-going field amplitudes of (3.2.18a) and
(3.2.19a) by using (3.2.21) for b,, and the like for bi”
_ = _ hist as sete. .
B= COQ ny -T — a @n, ‘B-Qy,:-® — (3.2.52a)
<(h) StL, kisst x8 tO,
5” = MQiyi  B — oF On, “0 -Qy, 7" (3.2.52b)
‘8
and the dowuward-going field amplitudes of (3.2.24b) and (3.2.25) by using
--- PAGE 103 ---
80 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
(3.2.27) for A, and the like for A”) are
A=Op, +O, (3.2.53a)

sth) = we SL .

A” =p, 3° +n, 79 (3.2.53)
From the matrix equations we see that the E- and H-waves are generally
coupled. An incident wave of E-type (a) = 0) will be diffracted from the
dielectric periodic surface into waves that have both E-wave and H-wave
components. Both types of wave will coexist to satisfy the boundary con-
ditions. When the incident wave vector is in the z-z plane (kjy = 0), then
9 = dy = 0 and we can easily see that the scattered waves arising from E yi
are decoupled from those arising from Hy.

We next apply to the case when the surface is a sinusoidal function

Qe
F(x) = ~heos(=*) (3.2.54)
st
The Q matrices can be calculated by carrying out the integrations in
(3.2.47), (3.2.49), and (3.2.50), and expressed in terms of Bessel functions.
= -1
= (Ei) iin ny (eo 3.2.55
[2], = CED inn al Bn) (3.2.55a)
Fal 1+ Om). |m—n|
N =" (ti Iim—n| (ksh, 3.2.55b)
[Oe an = aa EO in tn) (82.558)
at re ot
[>]... = van "in nj (Rishi) (3.2.55¢)
+ 14 hn  . \im—
ye) = (£1) inn (sh, 3.2.55d
[Orbe = Ee ae HY manish) (8.2554)
at ay -\\m— A aor
[Gnu]... = eC ni BaP) (3.2.55e)
where Jjm—n| denotes the Bessel function of order |m —n|.

The T-matrix approach, which makes use of Green’s theorem to derive
the extended boundary conditions, is exact. However, the matrices used may
become ill-conditioned when the surface corrugation is deep or when the
corrugation depth divided by the period is large. This limits the applicable
regime of this method. The reason for ill-conditioning is that entire basis
functions rather than subscctional basis functions are used in surface field
expansions. In Section 3 we shall apply subsectional basis functions to this
problem which can handle surfaces with deeper corrugations.
--- PAGE 104 ---
§2.3 Emissivity and Comparison with Experiments 81
2.3. Emissivity and Comparison with Experiments
In this section a sinusoidal surface is used to model a row-structured plowed
field, and the theoretical results of emissivity are illustrated and compared
with the experimental data obtained from field measurements.
‘The reflected power P, for one period is
1 pe ae
P= nah Rel(E, x H*) - 3] de (3.2.56)
2P Jy
and incident power is
1 ofP oo _ .
Prne= 3p [ Rel(Eine<Fne)(~a] de (8.257)
2P Jo
For the reflected E-modes, by using (3.2.2) and (3.2.18a) for z > fmar. we
get.
—kiykon/ ke
_ bp cts iyRan/ ks
E, = >) etn 1 (3.2.58)
7 Vin —kiyken/ ke
ken /k2
_ wen gts ‘an/ ks
en (3.2.59)
mw VPn Keon /K2
By substituting (3.2.58) and (3.2.59) into (3.2.56) and integrating, the Flo-
quet modes are orthogonal and for the E-modes we have
P, => bent al” (3.2.60)
re eT mo
Similarly, the reflected power for the H-modes can be obtained. The total
reflected power is
. h)i2
1 when (lal? (be? } .
P= = Re—= [ e—— + pd) = Pr 3.2.61
’ 2 Te Tat TY Taal > " (8.261)
where Pf can be interpreted as the reflected power for the nth Floquet mode.
When the mode is evanescent, kz, is purely imaginary. The power Pl = 0
for the evanescent mode. The incident power is
lwe Lk th) yp °
Pine = 5 5 (Iaol? + Zia?) (3.2.62)
Thus, the reflectivity for a wave with horizontal or vertical polarization is
1 (Pol? + ba
Ta=>-) P= a (3.2.63)
“Pine x . » {aol + nal 2
--- PAGE 105 ---
82 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
where a = v, h incident polarization. The summation in (3.2.63) is over the
propagating modes and ap and al are obtained from (3.2.29) and (3.2.30),
by setting
a= 4; (3.2.64)
The transmitted power per period of the nth mode passing through the
surface defined by z = Zmin is
1 wk, |A,/? AM 2 1
Pta RO Men (Ane AY catia en temin 3.2.65
mR a a 289)
for all modes, where kyz,, = k)4{},, and Im[k1zn] > 0 should be used. When
medium 1 is lossless, we have (letting m = \/#1/€1)
we
Ph = SO (An? + lm A/?) (3.2.66)
2kis
for the nth propagating mode and P! = 0 for the evanescent mode. The
transmissivity is given by
er ky |Anl? + (mA?
=> Be Aal+ me P (a =v,h) (3.2.67)
nm © Sis jag|? + |g”?
For the lossless case, the power conservation relation is
ratty =1 (3.2.68)
For both lossless and lossy media, the emissivity is given by
€a=1-Ta (3.2.69)

The theoretical results are illustrated for a sinusoidal surface in Figs.
3.2.3, 3.2.4, and 3.2.5 at a frequency of 1.4 GHz. The effect of the row
structure on the microwave emission from a bare agricultural field has been
reported [Wang et al. 1980] together with the soil moisture contents for the
measured data. The periodic surface has a height h = 10 cm and a period
P = 95 cm and can be approximated by a sinusoidal function. For the upper
medium, we let € = €, and pt = ply.

In Fig. 3.2.3 we illustrate the comparison between the theoretical results
and the experimental data for both the vertical and horizontal polarizations
when the radiometer observation angle is along the row direction (¢ = 90°).
The reported soil moisture content varies from 26% by dry weight at top
0 to 1 cm to 21.4% at 9 to 15 cm. In the theoretical results, we take e, =
(5.5 + i1.2)e, which corresponds to a soil moisture content of approximately
18%. In the same figure, we also show the theoretical curves for the flat
surface case. It is seen that the brightness temperature for the periodic rough
--- PAGE 106 ---
§2.3 Emissivity and Comparison with Experiments 83
1.
290
,
a
zs “
aos
260 nd
ara
2a)
ee)
230 ~
rar suericeS,
. ‘.
. \
200 i \
setaa estan \
coven ace \
10S} 6e90r, Featon. nriGom \
79, ’
a a rr a
INCIDENT ANGLE
Figure 3.2.3 Brightness temperature as a function of viewing angle. Radiometer observation
plane is parallel to the row direction (@ = 90°). ¢ = (5.5 +1.2)e,
surfaces for the horizontal polarization is higher than that for the flat surface,
whereas for the vertical polarization the brightness temperature is lower. For
the flat surface, both polarizations have the same brightness temperature
value when viewed from nadir, whereas for the periodic surface, the values
for the horizontal polarization are higher than the vertical polarization at
near-nadir angles and become lower at larger angles of observation.

In Fig. 3.2.4, the radiometer observation angles are perpendicular to the
row direction (@ = 0°). The soil moisture content is 29% by dry weight at
the top 0 to 5 cm and becomes drier with depth. We use €; = (10 + i2)€p.
We see that at near-nadir angles, as compared with the flat surface cases,
the brightness temperatures for the horizontal polarization are lower and
for the vertical polarization are higher. The effect of the rough surface as
compared with the flat surface appears to bring both the horizontal and
vertical polarization results closer together at higher incident angles. The
case of observation plane at @ = 30° is illustrated in Fig. 3.2.5.

In Figs. 3.2.3, 3.2.4, and 3.2.5, we observe that the Tg curves for the
periodic rough surface are not smoothly varying. For instance, in Fig. 3.2.4,
there are kinks appearing at observation angles # near 6°, 19°, 34°, and 51°.
‘The corresponding change in Tg may be as high as 10 K. Such a phenomenon
can be explained by the appearance and disappearance of Floquet modes at
various threshold angles. The kinks are caused by the redistribution of the
--- PAGE 107 ---
84 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
20,"
7
235] /
Y
240 “
ww v
vo
225) 7
210: ">> >
4 >
ST
195) * aN
oN
180) \
me \
stig \
tes Pmowersiao .
$50 Potten, Revoem \
\
i) 10 20 30 40 50 60 °
INCIDENT ANGLE.
Figure 3.2.4 Brightness temperature as a function of viewing angle. Radiometer observation
plane is perpendicular to the row direction (@ = 0°). €1 = (10 + i2)eo.
%
27007 y
7
/
asrs /
Z
Z 7 v
2480) wo
uv
232s
Ron
2200 _
Na
. Ny
207s NY
. N
LN
1980 — \
se SMe \
tens Peau = 40h \
9230", Fe 95m, 82 1Gem \
\
i005 40 20 30 40 30 60 ‘
INCIDENT ANGLE
Figure 3.2.5 Brightness temperature as a function of viewing angle. Radiometer observation
plane is slanted with respect to the row direction (¢ = 30°). €1 = (8 + 71.9)eo.
--- PAGE 108 ---
§3 Integral Equation Approach 85
scattered power during the course of the disappearance and appearance of
the propagating Floquet modes. For real soil surfaces, such kinks will not
appear because real soil surfaces are not periodic. They have randommess
superimposed on the periodic structure.
3 Scattering of Waves Obliquely Incident on Periodic
Rough Surfaces: Integral Equation Approach
In this section, we use subsectional basis functions to solve the integral equa-
tions. The speed-up computation of the periodic Green’s functions as dis-
cussed in Section 1 will be used.
3.1 Formulation
We use the integral equations developed in Section 2.1. From (3.2.8),
(3.2.9), (3.2.14), and (3.2.15), we have
EAB.) ~ fda { CrP Fe) VE (A) ~ EulPE)H “VeGrlP.-)}
= J Ey(As) for Bs = PE 3.3
Hp(Pe)~ fel { rls.) 8 Voy) ~ Hy.) VeCo(Pes 7}
_ fHy@,) for p, = PF 7
= { for B= pe (3.3.2)
Jf do! {Gre (@e.04) Al VeBiy(P) ~ Bil AH ViGir(PasP)}
JP
0 for Pp, = Py age
=ft Ps = Ps 3.3.3
{Buin for D. = Bs (838)
Jf da! { Gre .H) Al Veta Ae) — Hay.) A VCP PsA)
P
0 for Pp, = DE
= = = = 3.3.4
{ro for Pp, = Py )
In (3.3.1) (3.3.4),
D, = 2'& + f(a')2 (3.3.5)
Bl = ct + ft(x)z (3.3.6a)
Py = wh + fo (x)d (3.3.66)
where f+(c) means infinitesimally larger than f(x) and f(x) means in-
--- PAGE 109 ---
86 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
finitesimally smaller than f(x). The discontinuity is due to the fact that
a-VGp and ft. VGip have a nonintegrable singularity when p, and 7,
coincide. In the spatial domain, the periodic Green’s functions are
.
Gyp(a,2:2',2) = ; Se them PH (hj VG — a — mPP + (2-2)
m=—co

(3.3.7)
where j = 0,1. Computation of the periodic Green’s function can be speeded
up by using transformation as described in Section 1. We have, fron (3.1.31),

©
; > etkomP 1 (5a — a! —mP)? + (z—2/)*)
m=1
cil kis thy.)P p—iky.(e—a")
=
7
°° po Whi P+ky(e 2M cos (kjg(z — 2!)u(u? — 2i)!/?
[ du—2 nn cos (Ria( = 2')ulu? — 21)"") 3 38)
i La en his P+i(hix thy )P (u2 — 2%)1/2
where j = 0,1.

Equations (3.3.1) (3.3.4) are four integral equations with eight
unknowns, namely, Ey, Hy, Eiy, Hiy, 2: VsEy, ts VeHy, 1+ VsEiy, and
n+» VsHiy. Thus as in Section 2, we have the four boundary conditions of
(3.2.37a), (3.2.37b), (3.2.45a), and (3.2.45) so that, when combined with
(3.3.1)-(3.3.4), we have cight equations for the eight unknowns.

Next we apply MoM with pulse basis functions and point matching at
the midpoint. The midpoint between #,_; and x, designated as p, is the
testing point of the point matching. For the nth internal between z,_) and
Ln

By = Evy =n (3.3.94)
A-VsEty = 5n (3.3.98)
Ay = Hy = Cn (3.3.9¢)
A-VsAty =n (3.3.9d)
Let us consider (3.3.3). The discontinuity is due to the singularity of A’ -
V.Gip for p, and 7, on the same patch (self patch). Thus (3.3.3) can be
written, assuming p, to be on the same patch so that p, = Py»,
Yon [do Gre (PsP) — Som [ dolit Gre BP.)
7 Eno ném Vent
x, ~
™ ~ at oy 0 for Ay, (9 9
—4, doi! -V'.Gip (pe, Bi) = Pm 3.3.10
Ym [. o sG@1P Pm: Ps) = 4 on, for Be (3.3.10)
--- PAGE 110 ---
§3.1 Formulation 87
Hence, if we take the difference between upper half and lower half of
(3.3.10), we have
Ym = Im [ do! - VGie (Pin, Be) + 77m [ do!i! -V.GipBm Ps)
Emaa Em—1
(3.3.11)
If the patch is approximated by a straight segment, then the two parts of
(3.3.11) should be equal to and opposite each other. Thus
Lm . Pam - a 1.
[ dof!» V.Gip (Bf, p,) = — [ do’?! - VG p(B, De) = 5 (3.3.12)
Lint Fem—r
Using (3.3.12), (3.3.10) can be written as
Yo onEmn + D2 YnDmn = 0 (3.3.13)
7” n
where
In
Enn =~ [ da! Gin. Ps) (3.3.14)
Ena
1 .
3 ifm=n
Dinn = § “pen (3.3.15)
[ do! -VeCrpPy. Bi) ifm xn
Ent
Equation (3.3.4) becomes, in a similar manner,
SY Emnén + D> DinnGn = 0 (3.3.16)
n n-
Next we consider (3.3.1). Note that at the boundary, Ey = E1y, Hy =
dE, dE, dH, dH P
Hy. == = and = a Consider the term [ do'Gp Bn B,)
fh’. VE, and use boundary condition (3.2.45b),
-P
[ A0!Go(Ppath)il Vey
Jo
= [do's 3) 42 +- all Vs By)
0 df(a’)\?|~
14(=4
da!
--- PAGE 111 ---
88 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
=) oy falta a a
=[Cr@n Peeoty(M)].,_, — | de’ | [Erm %)| colly 7)
2/=0 0 dx
Pp
+e [ do'G PP in, Bu) «Ve E ry (3.3.17)
JO
The second equality is a result of integration by parts. Since
[CrPmsP)]__p =e"? [GePns7)| (3.3.18)
=P a'=0
and
ot = cikieP “) 8816
[uP], =e? [Hu] (3.3.19)
the first term of (3.3.17) vanishes. Thus
P
| do!G P(BmsPo)it! Vy Ey = C0 D> CranGn +02 9 Brann (3.3.20)
J ” n
where
En,
Bun = [ do! GP(Pns P's) (3.3.21)
Tana
Cun = GP(P ns Pp) ~ GP (Brus Pn-t) (3.3.22)
with p, = (tn, f(ap)). Also let
4 ifm=n
An = tn 3.3.23
mm - [ do'il -V.Gp(Pm: Be) ifm #n ( )
nat
Integral equation (3.3.1) becomes, using (3.3.23) and (3.3.20),
Eyi(Pm) ~ C2 > Brandn + 6 > CmnGn = Y> Amn In (3.3.24)
” 7 7”
Similarly, from (3.3.2) we have, using boundary condition of (3.2.45a),
Ayi(B.) ~ €2 Y> Bnn&n = do 9 Cnn = > Amnbn (3.3.25)
n n 7
where cg, ¢2, do, and dy are given in (3.2.42a-b) and (3.2.44a b).
Equations (3.3.13), (3.3.16), and (3.3.24)-(3.3.25) are the equations gov-
erning the unknowns Yn, dn, Gr and €. In matrix notation, they can be put
in the form
A c@B -mC 0 ¥ Eyi
D E 0 0 6 0 .
\z. 0 A ‘| | = | ty: (3.3.26)
0 0 D E & 0
--- PAGE 112 ---
§3.2 Polarimetric Brightness Temperatures 89

é z

sr hh

1 y

' a

' 3 -

1 tj ut

H L-Se e

T = Ho;€o

1 ra

1 olen

L- a| INI\I\f«

—
Pp Ho,

Figure 3.3.1 Polarimetric emission from a sinusoidal surface at temperature To.
Solving (3.3.26) numerically gives the surface field unknowns.

After the surface fields are determined, the coefficients of the reflected
Floquet modes can be calculated. The reflected fields for z > f(x) can be
written as

rho
By = Yo dpethn Pe (3.3.27a)
n
its
Hy = So bebe Pe (3.3.276)
n
Using (3.2.21) for b, and the like for b%”, we have
1 7? femme ap op Ora
bn == | do! | —_—A' - VLE, (p,) — Ey (BA - Vs | (3.3.28
sip |, €0'| GW VB uB) ~ By(@H- Vi | (8.8280)
r+, cto
1 P en thn Be ent Be
= ae da! | i! - Vy (B,) — Hy (ph - V,—
0 = sep fo! | Goal Vit) — Mytadal VI
(3.3.28)
3.2 Polarimetric Brightness Temperatures
In this section, polarimetric brightness temperatures are illustrated for the
emission from a sinusoidal surface (Fig. 3.3.1). The frequency is fixed at
1 GHz and the period is fixed at 50 cm. The first region is free space and
the physical temperature of the lossy dielectric, Tj, is fixed at 300 K. The
expressions for emissivity of the four Stokes parameters can be found in
Chapter 3, Section 5.4 of Volume I.
--- PAGE 113 ---
90 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
00 300
200 * 200 +t
me, + mo ot ft . 4
mf os) ‘Oy m0 e © f *
i “os fal 9 2 +
Ee . .
I Ded fs
Bee . Bee
Foy "ae
ea 0
0 B10
iat rr ee a at rr re ee
us tn degrees A in degrees
a «
« «
2 2
» .°
: » ; 10
. °
fil fg + £.
wt Up tt os
-%0 rs a
~o ~o
a er ac er
Ps Ln dagrene PM tn degrees
Figure 3.3.2 Brightness temperature versus @. 4 : 1 = 6, °: €r1 =9, #: €p1 = 12.
Figure 3.3.2 plots the brightness temperatures versus the azimuth angle
@. For these plots, the height is 15 cm and the incident angle @ is 20°.
Calculations are made for three different values of €1 = €1/€o. It is seen
that Tj, and T, tend to be higher for smaller ¢-1, while |U| increases with
increasing €,1. No significant change is observed in V. With increasing ¢, Th
decreases and T, increases. The brightness temperature of U is zero when
@ = 0° or @ = 90° as expected. In between, it decreases to about —30 K.
Values of V are small for the whole range of ¢.
Figure 3.3.3 shows the variation with respect to 6 with @ fixed at 45° and
height kept at 15 cm. Again, the plots are given for three different values of
--- PAGE 114 ---
§3.2 Polarimetric Brightness Temperatures 91
0 300
0 200
+ +

ee +t wo se

mb io e mt © © © 4
z ° . °
a fob!
be» . Lee .
3 e+ i .
£20 20
“he . “ae

°

= =

0 . B10

200 00

o 1 mm «60 00 m0 60 o 10 26 3 <0 8060 000 wo

et tn degrees ‘eta tn degree

© «

« «

2% 3

» 20

ze $
i ° . : i ol w ag :
£78 +e go) 3 3
> + : = :
~~ + ° ~2
eo 8
os) a nd 30!
~0 ~0
0 +0
ow a wow 90 60 70 60 oo 010 2 30 «0 60 e070 ao 8D
‘theta in degrees Geta fo degrees
Figure 3.3.3 Brightness temperature versus @. +: ¢-1 = 6,0: 1 =9, #2 ép1 = 12.
€,, and we observe the same behavior. There is a more than 30 K difference
in Th, for different €,; values at 6 = 60°. We also observe a change in V with
increasing 6.

Dependence of brightness temperatures on the surface height is given in
Fig. 3.3.4. For this case, ¢-1 = 12, 8 = 20°, and @ = 30°. We see a general
tendency of increasing 7}, and T,. V does not change much, but U varies
significantly with height. We note that when the height is 10 cm, |U| is as
high as 48 K.

Finally, we analyze the effect of complex €,; on the brightness temper-
atures in Fig. 3.3.5, when @ is 20°, @ is 45°, and height is 15 cm. The real
--- PAGE 115 ---
92 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE

00

200

200 + 4 Ff

+ °

= * + + Gg ee °

:- °°
5 250

: +e?

"eo

= °

= 8

210

‘200

oz 4s 8 0 a2 te as 2 22 mm oe 30
Inelgbt 10 on
10
° o 6 8 8 F © ~ 2 6
10
> +
3 + *
> 30 +
+ + ¢
“0
+
“80 *
~e0
o 2 « © © 00 Ww wt 16 18 90 2 &% 6 25 30
eight te oxo
Figure 3.3.4 Brightness temperature vs. height. + : T,(U), 0: Ty(V).
part of €,; is fixed at 12 and the imaginary part is varied from 0 to 8. Real
€+1 is taken as a base and the difference in temperatures is plotted. It is seen
that variations in T;, and T, are almost identical while the decrease in U is
less. There is a slight increase in V.

Note also that the plots are not given as continuous curves. We merely
show the results of some calculations, and linear interpolation between these
may be misleading. This is due to the presence of kinks in actual continuous
curves as shown in Section 2.
--- PAGE 116 ---
§4 Ewald’s Method 93
2
0
-2
~4
®
3
3
-8
-6
-10
712
o 1 2 38 4 5&8 6 7 6 8 10
imag epsi
Figure 3.3.5 Brightness temperature vs. én). +: Th, 0: Ty: U,v: V
4 Ewald’s Method
A method that is used in computing periodic Green’s function is the Ewald’s
method, which we will discuss in this section.
4.1 Preliminaries
We first describe several properties that are used in the derivation of Ewald’s
method. The first is an integral identity of the Hankel function.
From Abramowitz and Stegun [1965], the integral representation of the
Hankel function of order v is
1 perm ink 7
HO(2) = 4 | dt =D with Jarg z| < 2 (34.1)
Ti Joc" 2
where the integral contour in the complex t plane is labeled by C’. Next we
make the transformation u = e'. Then sinht = } (u— +) ;dt = du/u. The
--- PAGE 117 ---
94 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
integral becomes
lf z 1
)(,) = a z 2 \ | ent ‘
AS” (z) = [. du exp F (u *)) u (3.4.2)
The contour C’ in the complex u plane is from 0 to —oo along some suitable
chosen path.
The spherical Hankel function of order 0 is, letting z = kyr,
ier 0) Ty
- =hy’ (Kor) = Ty (ki,
kor 0 (kor) kort 2 (kor)
a ol kor 1 3
=,/——— | d —-(u--)|w? 3.4.3
\ kor wi f. wu exp 2 (« ~)] we B43)
Next we make transformation of variable to s. Let u = shz.du = — sds,
duu? =-,/ ds. Then
1 i2 ke 25
1 (hor) = [ ds exp [i = 232 (3.4.4)
The contour C’ in the complex s plane is from oo to 0 (Watson, 1966]. We
define the contour C' to be the reverse of C’ so that C is from s = 0 to
sx.
2
Q) __2 Fo ao 34
hg (kor) = iVak [ ds exp [i —rs (3.4.5)
To choose the proper contour. Note that as s > oo, the convergence of the
integral is dictated by exp(—r?s?) and we require Re(s?) > 0. Thus
as 8 > oo, largs| < . (3.4.6)
On the other hand, as s — 0), the convergence of the integral is dictated by
exp (%) and we require Re (2) < 0 which means 5 < arg (k2) —Qargs <
ae, Thus
30 7 .
ass — 0, —7té<ages<—-7+8 (3.4.7)
where 3 = } arg (k2) = arg(ka).
The contour C’ is as shown in Fig. 3.4.1. For0 < 8 < 3 the intersection
of these two regions is [Jordan ct al. 1986]
us T
~~ <args<—-—4+39 3.4.8
q Sess —gti (3.4.8)
The second relation is the definition of the lattice vectors and reciprocal
lattice vectors. Consider a periodic lattice that is three-dimensional. Let
R= mG + no + nya3 (3.4.9)
--- PAGE 118 ---
§4.1 Preliminaries 95
Ims
7 Res
Sz-- xt +9
‘ ToS.
N. ant
N ~~
N
N
aN C
N.
S.
N
aN
Figure 3.4.1 Contour C with @ = argko
where @, @, and Gy are the basis lattice vectors and ni, nz, and ng are
integers.

By a periodic medium, we mean that the wave function ~ obeys a wave
equation with periodic potential V(F). The periodic potential obeys the con-
dition

V(iF+R) =VF) (3.4.10)
where R is as given in (3.4.9). Note that
oo 2° oo
y=-y od Gan)
Ro M=—0o mp=—00 n3=—00
The reciprocal space is defined by
K = [by + lobe + Igd3 (3.4.12)
and
Q = G - Ae x G3 (3.4.13)
is the cell volume. The vectors by, 62, and bg are the basis in the reciprocal
vector space
z 2a
b= Gm x Ty (3.4.14)
> 2 5
bo = Bas xa (3.4.15)
z 27
by = ay x a (3.4.16)
2
Thus
6; +d; = 26; (3.4.17)
--- PAGE 119 ---
96 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
The sum 7x is used to denote summation over the reciprocal lattice space
oo wo
y-y yy” 418
RK  y=—00lp=—00ly=—00
Note that exp(iK - R) = 1.

The third relation is the Poisson’s summation which replaces summation
over lattice vectors by summation over reciprocal lattice vectors. Consider
any function f(#) and define g(¥) by

a) = Sle*Ps F-R) (3.4.19)
R
Consider
a7 +R) = e** se +R -R) (3.4.20)
R
Then
a+ R) = SoHE) pRB") = FF air) (3.4.21)
2
Thus q(¥) obeys Bloch’s condition. We then have
a?) =F w(7) = So e* RFF R) (3.4.22)
R
where w(F) is periodic in R. The periodic function w(7) can be represented
by a Fourier series in spectral domain
w(F) = So wae! F = oF RFR (3.4.23)
K R
The Fourier coefficient is given by
le a
wR=s [ drw(FeKF (3.4.24)
2Q Jog
where 2 is the area of the unit cell and Q is the domain of cell 0. Hence
1s Ke ike ch =
we=a |] dre hte *TY che FGF _R
kK Q I, > a )
R
1 (KiB)(7-E = J
=o f dre O-®) per _ BR) (3.4.25)
2 &— Joy
R
Let F(k) be the Fourier transform of f(F)
F(R) = / dre—** f (7) (3.4.26)
--- PAGE 120 ---
§4.1 Preliminaries 97
The integration is over all space. We can divide the infinite space into peri-
odic array of cells
F(R) =>, dre~*®* f (7) (3.4.27)
ROR
where Q_ is the cell with center at Rf. Let 7 = 7 — R. Then
PR => f are ®O My —® (3.4.28)
F 1
Using (3.4.25) and (3.4.28),
Toe a
wR = ght) (3.4.29)
Putting (3.4.29) in (3.4.22), we establish Poisson’s summation formula
Is 1_- = atoms
q(®) = x eh Rs (FR) = x grk+ Kei) (3.4.30)
R RK
In the above derivation, 7, R, K, and Rare 3-D vectors. For the case when
F =p+ 22 are 3-D while p, R, K, and k are 2-D vectors, the corresponding
results are as follows.
Let
R= na) + nd (3.4.31)
where m1 and nz are integers_ and @ and @2 are two-dimensional lattice
vectors in the z-y plane. Let K is the reciprocal lattice vector
K =lb; + lobe (3.4.32)
0; -G; = 276i; (3.4.33)
~~ ©
vs-E Dd (3.4.34)
K  =-col=—00
Also b, x bz and @ x @ are both in positive 2-direction, and exp(iK -R) = 1.
Let k be a 2-D vector and
af) = le* FFF —R) = Soe fG—R+ 23) (3.4.35)
R R
The Poisson’s summation formula is
a lo < ges
p) = ER (= R) —- Sri pes (B4R) 5 949
a?) = ue f(F@-R) = x ar &+ Ke é (3.4.36)
--- PAGE 121 ---
98 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
where F'(k) is the 2-D Fourier transform of f (7):
F(k) = fo e PF (5 + 22) (3.4.37)
=~ oy. _t i ik BE 24
f@+22) = aa | & F(R) (3.4.38)
4.2 3-D Green’s Function in 3-D Lattices
We first consider the case where 7 and FR are three-dimensional. A periodic
Green’s function involyes summation of radiation from sources at all the R
in the periodic lattice. Let
_ __. gikelF-R|
GZ(F,0) = )_ exp(ik -R)——— 3.4.39
s(7-0) = Yo explik -R) ae (3.4.39)
R
where ko = w,/fié is the wavenumber, k is a wavevector, and S7z is a three-
fold summation over the lattice. In solid state theory, k is a vector in the
first Brillouin zone. More geuerally, we need to evaluate
— 2 gether R
GFP) = exp(ik - 2) ————_—— 3.4.40
aT 7’) y pik By a (3.4.40)
where F and 7 are both in the unit cell centered at the origin. The unit cell
centered at the origin has R = 0. Direct summation of (3.4.40) converges
slowly because the decay for large indices is only 1/(distance).
Without loss of generality, let r > r’. Note that
VG(F,T) + RGF. 7’) = -(F - 7’) (3.4.41)
We use the addition theorem for r > r’,
etkelt—-F"| co Ol - ; y
mr-r| = > s ikohy(kor Yim (*)ju(Kor Yim (7) (3.4.42)
1=0 m=-i
Then we define Dj,,(7) such that
co
GFP) =O YP (i! Dim (Pju(hor Vin) (3.4.43)
120 m=-1
In (3.4.43),
= (6,0) (3.4.44)
is the direction vector with angular variables (6’,¢’). aud Yim(6’, @') are the
spherical harmonics. In this section, unlike in other chapters, we shall define
--- PAGE 122 ---
§4.2 3D Green’s Function in 3-D Lattices 99
them as
1
(21 +1) (l— m)!]? 6
y, 4) = 1 aoe Oy eit 3.4.45
in( 4) = | ED EO rin (cos te (3.445)
where P/"(cos @) is the associated Legendre polynomial as defined in (1.4.37)
of Volume I. The definition in (3.4.45) differs from (1.4.45) of Volume I by
a scale factor. The orthonormality relation for the spherical harmonic is
Qn oo
[46 fF at six 05(0, 89% (0.6) = 5S (3.4.46)
0 0
From (3.4.43) and (3.4.46)
Dim(F) = tke De® Phy (hole ~ R))i'¥im(F — R) (3.4.47)
R
where F — R refers to the unit vector point from R to F and is in the direction
of the spherical coordinate angles, © and ®. Note that G;(7.0) is a special
case of (3.4.47) with
1
GF, 0) = \ Gyo) (3.4.48)
From (3.4.47), we can interpret Dj,,(7) as multipole radiation from the lattice
points.
Next, use the integral identity
12 f° 22, Ke 244
holo) = Fee | ds exp [-" P+ is (3.4.49)
Cc
where C' is a contour (Fig. 3.4.1) that ensures the convergence of the integral.
For C, as indicated in (3.4.49), the arg s of C obeys the condition,
7 T
a <args<p- a (3.4.50)
where 3 = arg ko.
By using (3.4.49), no (kor) = ~A) (kor), the recurrence relation
21+1
hisi(kor) = @l+)) Tor ) hal kor) — hy (Kor) (3.4.51)
‘0
and mathematical induction, it can be shown that
Ca 2 2.2, Ke
or) == | ds s a2? 4 2% 4.52
hilkor) RAVE | ds s* exp |—r?s* + re (3.4.52)
c
--- PAGE 123 ---
100 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
Next, we split the integral of s into two parts from 0 to E and from E to
co, where F is known as the splitting parameter. Thus
Din (F) = DY (F) + DER) (3.4.53)
where
DO gp a2 eFRe_Bluly, wo).
in (TF) = HLS |F— RLV inl? “ON
2 2 Pi2.2 RR
ds s” exp |—|r — RI?s? + —> 4.54,
| ss exp [=F rps + *| (3.4.54a)
oi _ —~ 9
(2)—) _ 2 BR Bly. (oy _2
DPF) = mL FF RY FYin(F ~
0 > « ke
[ ds s” exp [- — Rs? + is] (3.4.54b)
E 4s
The quantity De (®) of (3.4.54b) can be calculated by direct numerical in-
tegration since an exponential decay is endowed in the integral, particularly
for large R. For | = 0, it can be evaluated exactly as will be shown in Section
4.3.
For the calculation of DOW), we let
f(F—R) =#YVin(F — RF — Ri! exp(—lF — Rl?s*) (3.4.55)
Sek R —R) = ul) (3.4.55b)
R
Then
gl 9 fb ,2
()in) _ 2 2 2t K = ;
Din (F) = Eve dh ds 8” exp 42 u(?) (3.4.56)
Using Poisson’s summation formula (3.4.30) from Section 4.1 and (3.4.55b),
1 Rene. o -
ur) = G Ve FE+K) (3.4.57)
R
where F'(k) is the Fourier transform of f (7). From (3.4.55a) and the property
of Fourier transform
‘co TH
F(k) = | OF #'Vim(*)r! exp(—r?s*)e (3.4.58)
—co
We use the spherical wave expansion of
= an 37 (—i) (kr) ¥ih PV) (3.4.59)
im
--- PAGE 124 ---
§4.2 3-D Green’s Function in 3-D Lattices 101
Then using the orthogonality relation of (3.4.46), we obtain
_ 00 5 ft Qn .
F(R) = [ dr r? [ dO sind | dgiV im (8, 37! exp(—r?s?)
Jo 0 0
«Ae S(~1y! julie) Vine Vim (B)
Um’
7. a, _ kt Ke
=n Sint exp (-#) (3.4.60)
Putting (3.4.60) and (3.4.57) in (3.4.56), we have
°E 2 —
ayy 1 2 RY 1 Ra Rye
Dry (F) “ave, ds exp a ave +K)F
=. FI! =. Pe
7 aa |k+ Ke k+k
: ary EVinK +K EAL exp [Par] (3.4.61)
The ds integration in (3.4.61) can be performed. We get
DO = 4 Vin (E+ RihR) lk+ |! E = Fer
r)= TWH L € Sa EXP | ee
tm Qe \k+ Rl? — 2 AE?
_ (3.4.62)
This converges rapidly in A because of the exponential decay in K. To
summarize, using (3.4.62), (3.4.53) and (3.4.54b), we have
DimlF) = Din) + Dim F)
riz?
1¢4 [k++ Ky'exp(# RE )
a a RK Bs
=o Vin(k + Kye 47 —____x
it Q oy m [r+ KY —
ki. = 3 2
+2 x ek Re _ Rilly. (F Ns
co _ Ke
. [ ds exp [- —RpPs + | } (3.4.63)
JE As’
In numerical implementation, the parameter E in (3.4.63) has to be chosen.
The optimum choice of the splitting parameter E is when DWF) and De (7)
do uot differ by more than several orders of magnitude. For the special case
of l=m=0,
--- PAGE 125 ---
102 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
2b Kl?
[1 1 f4nc ak on(® = )
Gz(F,0) = yf —Pool(F) = aK ellk+K)F __\
k dn An ad [E+ RP — 8
+ yet RS [vas exp|—|F — R)?s? + ua (3.4.64)
ee de s BR 3.4,
R
4.3 3-D Green’s Function in 2-D Lattices
We next consider 3-D Green’s function in 2-D lattices. In this case the space
is three-dimensional so that the field point 7 and source point 7’ are in
three-dimensional space. However, the periodic lattice is two-dimensional.
This problem has applications in scattering by frequency sclective surfaces,
periodic surfaces, and random rough surfaces with periodic boundary con-
ditions. Let k be a 2-D vector and the Green’s function be
— a. eikol?—R| ER ikoho(kolr - Rl)
GF) = ¥° exp(ik - R) ——— = So eth SOON (3.4.65
HF) =D expt ara Hh L dn (3.4.65)
R R
where Dy = VP oo Lasso: To put (3.4.65) in spectral domain, we let
k=kzd + ky and
eikor i _ ik p+ik, 2|
7) = —— =—, | dk 3.4.66
f(r) Anr 4p? | 2k, )
Then
_ jet BF le!
F(k) = ———== (3.4.67)
2k? — k?
Using (3.4.67) in the Poisson summation formulation, the reciprocal lattice
domain solution is
i eh emp
G(F) = = —— es hp 3.4.68
= 9a (3.4.68)
R
where
kz = \/k2 —|k+K\?, Imk, >0 (3.4.69)
We make use of the integral identity of (3.4.49) for ho(k(F—R]) and a splitting
parameter of B, Thus
G(F) = GilF) + Ga(F) (3.4.70)
where
--- PAGE 126 ---
§4.3 3D Green's Function in 2-D Lattices 103
i) = exp(ik- BZ f asexp |p RP? +] gar )
1) = Fe exp li Vid Is exp r 8 1 A.71a
R Cc
nme tpl Ree B
Ga(F) = ip Loh . my | ds exp [-r ~RyPs?+ 75] (84.710)
The integral of G2(F) in (3.4.71b) can be calculated as follows
Vite is EXP r s ra
tol oo _ ik _ 2
== ds \\F — R| - —% —|F- Rs? + —&
Var {[. ash R| ma eo | |r — Ri*s +a2
~ aslir Fy . tke = Fil2e2 4. Ke
+f ds [r-m + | exp [-r — Ris? + re
= _[explitir —B))
Vi iF RO
co miko a. ike \?
ff ds (i ~R1- 3) xn] - (i ~Rijs+ oe
= Ty fae lim FR 4. tke ike)?
+ exp(—iko|F — ny fF ds ('r —Ri+ a) exp |— (r —R\s— oe
(3.4.72)
The complementary error function is
2 oe 2
erfe(z) = — [ dwe™ (3.4.73)
Then
2 [° = F242. Ke
= |, ds exp (ir 8 +i
| _ fexplikgl — Rierte (jr — Rip + tke
= = 4e tolF — rF- RE +
air - RY OP oF
a a iko
+exp(—ike|F — R})erfe (\r -RiE- mE) } (3.4.74)
Putting in (3.4.71b) gives the expression of G2 that is written in (3.4.836).
For Gi(F), we note that since R is in the x-y plane and 7 = (x,y, 2),
exp(—|F — Rls?) = exp(—2?s”) exp(—|p — R[?s?) (3.4.75)
where p = 2% + yy is the two-dimensional position vector. Let
--- PAGE 127 ---
104 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
f(p- R) = exp(-|p - Ri’s) (3.4.76)
a(p) = >_exp(ik - R) Ff — PR) (3.4.76b)
R
From (3.4.36) of Section 4.1,
— _ an
B) = ¥- exp(ik - R) exp(—[p — Ri?s*) = S> = PR + Kye? (3.4.
4() = So exp(ik- R) exr(—[p — R’s*) = SOP E+ Ke (3.4.77)
R K
where F(k) is the 2-D Fourier transform of f()
~ oe En 20, 7 Ke
F(k) = I dp e~**? exp(—p?s*) = = exp (-) (3.4.78)
00 s 4s’
Thus we have
kp Kp. kt KP .
q(p) =e" > e "On exp [-Fext (3.4.79)
RK
Putting (3.4.79) into (3.4.71a) gives
12 /* KB .
Gir) = —— dsexp { —& 3) exp (— 22s
1) =z = sexp | ul) exp (—22s?)
12 i(k+K) po F ds Ik+ KP 2.2 ke
ray be af, P°P| ae 78 + aR
K c
(3.4.80)
Letting s + 1/s in (3.4.80), we have
n@=—! 1+R7 [~ dsexp|-(HARE _ ke) p_ 2
GF) = a a ener 7 1)% - 2
c
(3.4.81)
where C’ is a contour that ensures convergence at oo. Equation (3.4.81) is
now in similar now to (3.4.71) and can be manipulated in a similar manner
to be in the form of complementary error function.
To summarize, we have
G(F) = Gi(F) + Ga(F) (3.4.82)
where
7 i cilktK)p . ik,
GilF) = io x a {esp(ik.e)nt (-# - t.)
RK
. ike 2 4 92
+exp(—ik,z)erfc oF +E, (3.4.83a)
--- PAGE 128 ---
§4.4 Numerical Results 105
with kz = 4/k2 —|k+K|?, Imk, > 0, and
1 a 1 = = ik,
Ga(F) = 5 = exp(ik- Ra {exptilr — Ri) erfe G -RIE+ aa)
Lic.P = _ Fi ike
+ exp(—ikelr ~ Ri) erfe (|r — RIE — 58 (3.4.836)
The splitting parameter F’ is optimally chosen such that G)(F) and G(r)
do not differ by more than several orders of magnitude.
4.4 Numerical Results
We illustrate the results for the case of 3-D Greens function in a 2-D square
lattice. The case that the Ewald’s method gains is when the medium is
lossless and z = 0. Let the lattice be a = az%, G2 = ayy. Then b) =
25%, bo = 289. The lattice vectors and the reciprocal lattice vectors are
2 iy
respectively
R= maeé + n2ayi (3.4.84)
=> 2al 2ai:
Kap 4 eg (3.4.85)
Qy ay
Also Q = a;ay. We consider the case that k = kict + kiy. The spatial
domain solution is
Ng Ng in k yeitonins
Giz. y. = UKizMiGeThiyN2dy) ~ 3.4.86
wn SS cee oN
ny=—Ns na=—Ng
where
Rnyng = \f (t — maz)? + (y— ngay)? + 2? (3.4.87)
and we also truncate at N;.
The reciprocal lattice domain, or the spectral domain solution is
LON Ne i[ (hoot 22D) c+ (hin +222) uy] cider rple
i e ee ay JY] gikayigle
G(a,y,z) = => (3.4.88
e2=—5 oY = (9.4.8)
L=-N,b=—N,
where
: Qn \? 2nly\?
kents = 4{k2 — [(« + ait) + (ku a) (3.4.89)
az ay
and truncation is at N,. Also Im(kzj,1,) > 0.
--- PAGE 129 ---
106 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
On the other hand, in Ewald’s method,
G(x, y, 2) = Gi(a,y, z) + Gola, y, 2) (3.4.90)
where
5 MN il (bret 2) 2+ (hi +24) 9]
i é we oy
Gia, y, 2) = = —
MBI) = FG u uo Rett
h=-M b=-Ny ib
{eteoeterte (Se - Es) te Kutt erfe (Se + ks) }
(3.4.91)
and
No No cilkiamaethiynady) pikoRny na ik,
- 7 e yay) ane iky
Gateys)= Yo ye ee (Ram + 5)
m=—Nom=~No
No Nz pilkianiae-+hiynaey) tke Rn n ;
é re a ik,
ere | Rainn B- 58
+ 8tRnins er e( Many a)
n=—N2n2= No
(3.4.92)
where truncations of G; and G2 are done respectively at Ny and Np.
Asymptotically,
enw?
rfe(w)  —— 4,
erfe(w) Jaw (3.4.93)
Thus both series of Gi(x,y) and G2(x,y) have exponential decay:
2 2
Gi(x,y) (=) + (a) (3.4.94)
Fi(2,y) > exp | —~—4—_—*" *— 3.4.6
We,y, Pp 42
Golx,y) > exp [- (mae)? + (n20)”) B] (3.4.95)
-(2)? 2
For the 1-D case, the two series are respectively e (=) and e7[(mee)"1E*_
The two series have the same exponential decay rate if E = /7/az.
For the 2-D case, we choose splitting parameter £ such that
E=,f— (3.4.96)
Ay Ay
In the numerical simulations, we use the following parameters: A = 1, a, =
0.95A, ay = 0.95A, hic = Re(k,) sin 6; cos $j, kiy = Re(ko) sin 8; sin d;, Ni =
Ny =2, B= \/-™ = 1.86671.
ey
--- PAGE 130 ---
§4.4 Numerical Results 107
[Case TN, [Spatial [N- [Spectral 2G GT Ewald)
fe) [300 [0202+ a.517 /250 | 0.202 wo.a17 | 0856+ as |—O.15A— w.0170 | 0.2024 W517
(b) |1000 | -0.164 + 40.069 | 10 | —0.166 + 10.071 | -0.623 + 10,071 0.457 0.165 | 40.071
(ec) | 1000 | 0.0566 + 10.473 | 10 | 0.0163 + 10.457 | 0.162 + 10.468 | —0.146—w.010 | 0.0162 - 10.457
(a) {1000 | 0.0609 ~i0.465 | 300 | 0.0216 + 10.450 | u.175+%0.460 | —0.154 — i0.o106 cn
Table 3.4.1 Computation of the periodic Green’s function using Ewald’s method.

We use very few terms in the Ewald summation. The slight difference in
the results could be due to the accuracy in computing the complementary
error function of complex arguments.

The results for the four cases considered below are tabulated in Ta-
ble 3.4.1.

Case (a) Lossy medium: k, = 2r(1 + 10.01), @; = 45°, ¢; = 25°, z = 0,
x = 0.48, y = —0.91). In Fig. 3.4.2, we plot the convergence tests of the
spatial solution (dotted line) and the spectral solution (solid line) for the
real part of the Green’s function as a function of N, and N, respectively.
There are good convergence for both spatial and spectral solutions.

Case (b) Normal incidence: k, = n 6, = 0°, , @ = 25°, 2 =O01A, 2 =
0.48\, y = —0.91A. In Fig. 3.4.3, we plot the convergence tests of the spatial
solution (dotted line) and the spectral solution (solid line) for the real part of
the Green’s function as a function of N, and N, respectively. There is good
convergence for the spectral solution. Because z is not equal to zero, there
is good exponential decay for the evanescent Floquet modes in the spectral
solution. Ou the other hand, the spatial solution needs many more terms.
Case (c) Oblique incidence: z 4 0, ky = on 6; = 45°, @ = 25°, 2 = 0.1,
a = 048A, y = —0.91). In Fig. 3.4.4, we plot the convergence tests. There
is good convergence for the spectral solution. On the other hand, the spatial
solution does not converge even for N, = 1000.

Case (d) Oblique incidence: z = 0, ko = 3, 6; = 45°, $; = 25°, z = 0,
a =0.48A, y = —0.91A. In Fig. 3.4.5, we plot the convergence tests. Neither
spatial solution nor spectral solution converge well. However, the spectral
solution shows a better convergence.

It is important to emphasize that Ewald’s method requires very few
terms for all the four cases considered. As shown in Table 3.4.1, the results
of Ewald’s method are also accurate.
--- PAGE 131 ---
108 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
0.4, v v — =
Spatial solution
i — spectral solution |!
0.35 —
03) 7
oO 0.25
3
5 02
3
3
[0.45
o4 4
0.05)
% 40 20 30 40 50 60 70 8 90 100
Ns and Nr
Figure 3.4.2. Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (a) — Lossy medium: ky = 24 (1410.01), 0; = 45°, 6 = 25°, z = 0, c = 0.48,
y= 0.91).
$0.44] 4. re
spatial solution |
——=_Spectral solution
0.15
-0.16) : Lo
° coe
3 :
é 0.17] .
a
3
é :
0.18}: J
0.19)
0.2)
0 100 200 300 400 500 600 700 600 900 1000
Ns and Nr
Figure 3.4.3 Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (b) — Normal incidence: ky = 22, 6; = 0°, dj = 25°, = = 0.10, # = 048A,
y= 0.910.
--- PAGE 132 ---
§4.4 Numerical Results 109
05,
spatial solution
— spectral solution |
04
03- 4
o | .
3 02 4
=
5
«
Bot
@
ty)
0.1
02 1 1 a
0 10 20 30 40 50 60 70 80 90 100
Ns and Nr
Figure 3.4.4 Convergence of the spatial solution (dotted line) and spectral solution (solid
Tine) for case (c) ~ Oblique incidence: z # 0, ko = 32, 0) = 45°, ; = 25°, z = 0.12,
w= 0.482, y = —0.91A.
05 . Te eee
spatial solution
— spectral solution!
0.4- 4
0.3
oO
5 0.2
=
5
& .
Bor
& |
0} 4
04
0.2. 1 1 ‘ sat
0 10 2 30 40 50 60 70 8 9 100
Ns and Nr
Figure 3.4.5 Convergence of the spatial solution (dotted line) and spectral solution (solid
line) for case (d) — Oblique incidence: z = 0, ko = 22, 0; = 45°, 4; = 25°, = = 0, x = 0.484,
y= 0.91).
--- PAGE 133 ---
110 3 SCATTERING AND EMISSION BY A PERIODIC ROUGH SURFACE
REFERENCES AND ADDITIONAL READINGS
Abramowitz, M. and J. A. Stegun (1965), Handbook of Mathematical Functions, Dover Pub-

lications, New York.

Chan, C. IL. (1995), Analysis of frequency selective surfaces, in Frequency Selective Surface
and Grid Array, edited by 'T. K. Wu, Chapter 2, 27-85, Wiley-Interscience, New York.

Cohen, E. (1995), An Ewald transformation of frequency domain integral formulations, Hlec-
tromagnetics, 15, 427 439.

Ewald, P. P. (1921), Die berechnug optischer und elekrostatischen gitterpotential, Ann. Phys.,
64, 253-268.

Kipp, R. A. and C. H, Chan (1994), A numerically efficient technique for the method of mo-
ments solution to planar periodic structures in a layered media, IEEE Trans. Microwave
Theory Tech., 42(4), 635-643.

Joannopoulos, J. D., R. D. Meade, and J. M. Winn (1995), Photonic Crystals: Molding the
Flow of Light, Princeton University Press, Princeton.

Johnson, J.'T., J. A. Kong, R.'T. Shin, D. H. Staclin, K. O'Neill, and A. W. Lohanick (1993),
Third Stokes parameter emission from a periodic water surface, IEEE Trans. Geosci.
Remote Sens., 31(5). 1066-1080.

Jordan, K. E., G. R. Richter, and P. Sheng (1986), An efficient numerical evaluation of the
Green’s function for the Helmholtz operator on periodic structures, J. of Comp. Phys.,
63, 222-235.

Kittel, C. (1996), Introduction to Solid State Physics, 7th edition, Wiley, New York.

Mathis, A. W. and A. F, Peterson (1996), A comparison of acceleration procedures for the
two-dimensional periodic Green's function, IEEE Trans. Antennas Propagat., 44(1),
367-571.

Mathis, A. W. and A. F. Peterson (1998), Efficient electromagnetic analysis of a doubly
infinite array of rectangular apertures, IEEE Trans. Microwave Theory Tech., 46(1),
46-54.

Munk, B. A. (2000), Frequency Selective Surfaces: Theory and Design, Wiley-Interscience,
New York.

Nghiem, S. V..M. B. Veysoglu, J. A. Kong, R. T. Shin, K. O'Neill, and A. W. Lohanick (1991),
Polarimetric passive remote sensing of a periodic soil surface: Microwave measurements
and analysis, J. Blectromag. Waves and Appl., 5, 997-1005.

Oberhettinger, F. and 1.. Badii (1973), Tables of Laplace Transforms, Springer-Verlag, Berlin.

Radisic. V.. Y. Qian, and '. Itoh (1998), Broadband power amplifier using dielectric photonic
bandgap structures, IEBE Microwave Guided Wave Lell., 8, 13-14.

Veysoglu, M. E., S. H. Yueh, R. T. Shin, and J. A. Kong (1991), Polarimetric passive remote
sensing of periodic surfaces, J. Electromag. Waves and Appl., 5, 267 280.

Wang, J. R., R. W, Newton, and J. W. Rouse (1980), Passive microwave remote sensing of
soil moisture: The effect of tilled row structure, IEEE Trans. Geosci, Remote Sens., 18,
296-302.

Watson, G. N. (1966), A Treatise on the Theory of Bessel Functions, 2nd edition, Cambridge
University Press, Cambridge.

Yablonovitch, E. (1987), Inhibited spontaneous emission is solid state physics and electronics,
Phys. Rev. Lett., 58(20), 2059-2062.

Yu, Y. X. and C. H. Chan (1998), On the extension of Ewald’s method to periodic structures,
Microwave Opt. Technol. Lett., 19(2), 125-131
--- PAGE 134 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)
Chapter 4
RANDOM ROUGH SURFACE SIMULATIONS
1 Perfect Electric Conductor (Non-Penetrable Surface) 114
1.1 Integral Equation 114
1.2 Matrix Equation: Dirichlet Boundary Condition
(EFIE for TE Case) 116
1.3. Tapering of Incident Waves and Calculation of Scattered
Waves 118
1.4 Random Rough Surface Generation 124
1.4.1 Gaussian Rough Surface 124
1.4.2 Fractal Rough Surface 132
1.5 Neumann Boundary Condition (MFIE for TM Case) 134
2 Two-Media Problem 137
2.1. TE and TM Waves 139
2.2 Absorptivity, Emissivity and Reflectivity 141
2.3 Impedance Matrix Elements: Numerical Integrations 143
24 Simulation Results 145
2.4.1 Gaussian Surface and Comparisons with Analytical
Methods 145
2.4.2 Dirichlet Case of Gaussian Surface with Ocean Spectrum
and Fractal Surface 150
2.4.3 Bistatic Scattering for Two Media Problem with Ocean
Spectrum 151
3 Topics of Numerical Simulations 154
3.1 Periodic Boundary Condition 154
3.2 MFIE for TE Case of PEC 158
3.3. Impedance Boundary Condition 161
4 Microwave Emission of Rough Ocean Surfaces 163
-1li-
--- PAGE 135 ---
112 4 RANDOM ROUGH SURFACE SIMULALIONS
5 Waves Scattering from Real-Life Rough Surface Profiles 166
5.1 Introduction 166
5.2 Rough Surface Generated by Three Methods 167
5.3 Numerical Results of the Three Methods 169

References and Additional Readings 175
--- PAGE 136 ---
4 RANDOM ROUGH SURFACE SIMULATIONS 113

In this chapter we study random rough surface simulations of one-
dimensional surface for two-dimensional scattering problem. The simulations
of rough surface scattering started in the late 1970’s and continue to the
present day [Axline and Fung, 1978; Thorsos, 1988; Thorsos and Jackson,
1991; Maystre et al. 1991; Devayya and Wingham, 1992; Thorsos and Jack-
son, 1989; Thorsos and Broschat, 1995; Maradudin et al. 1990; Michel and
O'Donnell, 1992; McGurn and Maradudin, 1993; Chan et al. 1991; Nieto-
Vesperinas and Soto-Crespo, 1987]. The main purposes of the early simula-
tions were to validate analytic scattering theory and to investigate backscat-
tering enhancement.

The numerical method in this chapter is based on the formulation of
integral equations and converting the integral equations into matrix equa-
tions using the method of moments. We discuss the Dirichlet problem and
Neumann problem and illustrate the results using Gaussian surfaces, sur-
faces with ocean spectrum, and fractal surfaces. Next, we discuss dielectric
surface and the calculation of emissivity for applications in passive remote
sensing. In particular, we address the accuracy issue in the calculation of
emissivity. The accurate calculation of emissivity distinguishes the emphasis
of rough surface simulations in this book. Most researchers on rough sur-
face simulations emphasize on bistatic scattering and backscattering, which
are usually measured and plotted in dB scale. For such simulations, an ac-
curacy of 25% or 1 dB is acceptable. However, for passive remote sensing
calculations, the physics is based on energy conservation, The key result in
passive remote sensing is the difference of emissivity between a rough sur-
face and a flat surface. The difference is small and can be a few percent to
Jess than 1%, For ocean remote sensing, that difference is particularly small,
e.g., 0.003 or 0.3%, This corresponds to a brightness temperature difference
of less than a Kelvin between a rough surface and a flat surface. The ability
to distinguish that small difference actually forms the basis of passive remote
sensing of ocean wind. This means that for passive remote sensing numerical
simulations, energy conservation has to be within 0.3%. Such a stringent
requirement is not necded in active remote sensing simulations, where an
energy conservation of 96% is deemed to be good. Thus numerical methods
of simulations for active remote sensing can be different from passive remote
sensing because of the large difference in accuracy requirements. Onc key im-
plication for calculations in passive remote sensing is that: the rough surface
needs to have a fine discretization. In this chapter, we will also introduce ex-
amples of real life surface profiles measured for rocky surfaces, soil surfaces,
and snow surfaces.
--- PAGE 137 ---
114 4 RANDOM ROUGH SURFACE SIMULATIONS
1 Perfect Electric Conductor (Non-Penetrable Surface)
1.1 Integral Equation
Consider an incident wave Winc(F) impinging upon a random surface
(Fig. 4.1.1) with height profile z = f(x). In two-dimensional scattcring prob-
lem F = wa: + 22, the wavefunction (7) is
UP) = Vine?) + Us(F) (4.1.1)
where w),(7) is the scattered wave. The wavefunction obeys the equation
(V7 4k?) vy =0 (4.1.2)
The two-dimensional Green’s function obeys the equation
(W? +) (7) = ~0(7 - 7") (4.1.3)
and
9(F,7') = SHS” (kr -7')) (4.1.4)
Let the spaces above and below the rough surface be denoted by region
0 (Vo) and region 1 (Vj). We use the Green’s theorem to get
[fe wovatr.r) - 97, 7V0@)
IVa
~~ I ds A: (WO)Va(r”) ~ afFF Var]
s
+ I ds i [WR)VoF) — (FF )VUR] (4.4.5)
Sx
where Sx is the surface at infinity. Using (4.1.2) and (4.1.3) in the left-hand
side of (4.1.5), we have
ih dF [b(F) (Pg FF) — 5(F -7)) +97. 7) PUR]
Yo
=- I dF 5(F =r’) HF) (4.1.6)
Jd Vo
To evaluate (4.1.6), one needs to define where 7 is. One can have F above
the rough surface or 7 below the rough surface. Note that 7” can be infinites-
imally close to the surface. If 7 is infinitesimally close but above the rough
surface, we denote it by 7,. If it is infinitesimally close but below the rough
surface, we denote it by 7_. Also
_ sim wl) ane) — J ~V7") if im region Vo
Ike OF or 7) Or) = {5 if F” in region Vi (41.7)
--- PAGE 138 ---
§1.1 Integral Equation 115
_ z
Ey
4
iat)
z= f(z)
ee ee ~ eas
€y
Figure 4.1.1 Wave impinging upon a dielectric surface,
The surface integral at infinity in (4.1.5) gives the incident wave. Thus
Vine) fds a- [wry Valr,*) ~ gtF.F)VUO)]
s
_ fur) Fev (4.1.80)
~ (0 rev (4.1.8)
The zero in (4.1.85) corresponds to the extinction theorem. Note that in
(4.1.82) and (4.1.85), 7 is on surface S while 7 is in region Vy or Vj. To
obtain integral equations, we consider the following two cases.
A. Dirichlet Boundary Condition
Dirichlet boundary condition represents the TE case of electromagnetic scat-
tering with & = 9£ and the surface is perfectly conducting.
The Dirichlet boundary condition is
w(F) =0 (4.1.9)
for F on S. Then
oh (\ aoe yoy JO) Mev (41-10a)
vine? fas or ra Wore) = {5 NET ra
If we let 7 approach the surface, we note that both (4.1.10a) and
(4.1.10) will approach zcro, Thus one does not have to distinguish between
7, and 7. For F on S, (4.1.10) takes the form of a surface integral equation
for the surface unknown 7’ - Vu)(7)
Winel?’) = [as GFF )a- Vv(r) (4.1.11)
s
Note that both 7 and 7 are on S in (4.1.11).
We also note that as F — 7”, g(7,7’) has an integrable singularity for
a one-dimensional integration. Equation (4.1.11) is also known as the EFIE
--- PAGE 139 ---
116 4 RANDOM ROUGH SURFACE SIMULATIONS
(clectric field integral equation) for TE case because ¢ represents the electric
field which points in the horizontal direction.
B. Neumann Boundary Condition
This represents a TM case when the magnetic field is 7 = 9H and the surface
is perfectly conducting. Let 7 represent H. Then the boundary condition is
a-Vo=0 (4.1.12)
From (4.1.8), we have
gl cap Cote) a UP) KEV (41.130)
vinel?)+ [ds veya Votrn7) = (9) TS ye erie
Next, we let 7 approach the surface. In this case, it makes a difference
whether one approaches the surface from above which gives (F",) or from
below which gives zero by (4.1.13b). Thus, we have
Wine(T) + [ ds i(r)r-VoF,F,) = 0) (4.1.14a)
Ss
Wine(F_) + [ ds w(F)i- Vg(F,F_) =0 (4.1.14b)
Js
In Section 1.5, we shall show that because of the singularity of Green’s
function, (4.1.14a) and (4.1.146) are consistent with each other. One can use
(4.1.14a) or (4.1.148) to solve for the surface unknown ¢(7). The discontinu-
ity of W(F_) and w(Fr"_) can be accounted for by the singularity of the normal
derivative of the Green’s function. As 7 — 7, n- Vg(7,7") is more singular
than (7,7).
1.2 Matrix Equation: Dirichlet Boundary Condition (EFIE for TE
Case)
Integral equations can be readily converted to matrix equations. The surface
integral equation for Dirichlet boundary condition is, for 7’ on S,
Vinel) = [ dsg(r,7')a- Vu(r) (4.1.15)
Ss
Note that both F and 7 are on S. On S, z = f(z) and 2! = f(x‘). Hence
(4.1.15) becomes
L | gy?
2 ; ante
vine $e) = [7 dey (Z) ale. feh2! 29) AVM) 15
. (4.1.16)
--- PAGE 140 ---
§1.2 Matrix Equation: Dirichlet Boundary Condition (EFIE for TE Case) 17
where we have limited the surface to between —L/2 to L/2. The quantity
Wine(2", f(x’) is only a function of x’. Let
b(2") = Wine(2’, F(2’)) (4.1.17)
Also let
df\? .
1+ x (A: VO) 22 p(0) = U(2) (4.1.18)
be the surface unknown. The kernel of the integral equation is
K(a',2) = g(a, f(x); 2", f(2’)) = g(a’, f(a"); 2, f(a)) (4.1.19)
Putting (4.1.17), (4.1.18), and (4.1.19) into (4.1.16), we have
L
[ da K(a',£)U (ax) = b(2’) (4.1.20)
-2
2
Next we convert (4.1.20) into a matrix equation using MoM. The domain
—L/2 < « < L/2 is divided into N intervals, cach of width A = L/N. The
intervals are centered at a,, m = 1,2,...,N. Thus U(x) = U, in the nth
interval and we point match the integral equation at 2! = 2).
First. we set ’ = 2 in (4.1.20) (point matching):
A
[ de K (itm,t)U (2) = (arm) (4.1.21)
-k
2
m=1,2,...,N. Next the integral (4.1.21) can be replaced by a summation,
assuming that U(x) is constant in each interval (pulse basis functions):
N
Ae K (emt) C0») + {ff de Kem 2)) Un) = bln) (1.22)
nem m
where m = 1,2,...,N and f,, implies integration over the mth interval. We
have to single out the mth interval because K(2,,) is singular at 7 = &m.
The second term in (4.1.22) is known as the sclf-patch contribution. For x
and 2,,, close to each other, the argument of the Green’s function is small.
For small argument w,
Ow) =142n(% 4.1.23
HOw) 1+icin (2%) (4.1.23)
where y = 1.78107. We further approximate
—f(@m) + £(@) = f'(@m)(@ — em) (4.1.24)
--- PAGE 141 ---
118 4 RANDOM ROUGH SURFACE SIMULATIONS
Thus
r Cm FAE
| dz K(xm,2) = 2/ dx K(2m,®)
m Em
ise 2. fy ;
x sf de +iZIn (Zeryi + (Fem)? )]
iAx 2 ak 2
= — {1+i-In|—Ary/1 7
{14 i2tn [ary + (rem) }
iAgr 2 ak
=— i— — 2
z {1+i2in (Zar) } (4.1.25)
where Al, = Ary/1 + (f"(2m))? is the length of the segment of the surface
that is centered at 2.
Let
U(2n) =Un (4.1.26)
b(@m) = bm (4.1.27)
Az K({tm,2n) formA~n
Amn = § idx 2 yk 4.1.28
mm — jl+i-ln Alm form =n ( )
4 7 de
Tn Section 2.3, we will describe numerical integration to obtain more accurate
matrix clements. Putting (4.1.26)-(4.1.28) into (4.1.22), we get the equation
N
SO AmnUn = bm (4.1.29)
n=1
In matrix notation, we have
AU=5 (4.1.30)
1.3 Tapering of Incident Waves and Calculation of Scattered
‘Waves
In numerical simulations, the rough surface is truncated at 2 = +L/2. This
means that the surface current is forced to be zero for |2| > L/2. If there is
an abrupt change of surface current from nonzero to zero, artificial reflection
from the two endpoints will occur. To avoid these problems, one way is to
taper the incident wave so that the incident wave decays to zero in a Gaussian
manner for large x.
--- PAGE 142 ---
§1.3 Tapering of Incident Waves and Calculation of Scattered Waves 119
A tapered incident wave is [Thorsos, 1988}
ae x + ztand;)?
Wine(F) = exp (ik(x sin 6; — z.cos 6;)(1 + w(F))) exp (Se)
(4.1.31)
where g is the tapering parameter, and the incident wave vector is
kj = k(& sin 8; — 200s 0) (4.1.32)
The choice of decay factor is dictated by the fact that the direction of con-
stant phase and the direction of constant amplitude are perpendicular. We
have
V(asin 6; — z cos 6;) - V ((x + ztand;)?) =0 (4.1.33)
Note also that at z = 0,
2
|Vine()|,-9 = xP (-3) (4.1.84)
so that it is Gaussian in the plane z = 0 and decays rapidly for |x| > g.
The additional factor in the phase, w(7) is inserted such that yinc obeys
the wave equation to a higher order. The choice of w(7) is
+ ztan 0;)2
[pict eeear _ 7
— g
wr) = — > 4.1.35
(7) (kg cos 0;)? ( )
By straightforward differentiation, it follows that
Pine, Pine . 12,
en tae t kWine
=P bind —w?- 16 sin 8; — z cos 6;)?(x + z tan 6)?
k4g8 cos® 0;
Aik(z sin 6; — zcos 6;) A(x + z tan 4;)?
{SS 1 - -—— > 4.1.36
+ k4g* cost 6; g ( 5)
The right-hand side of (4.1.36) is much smaller than |kVine|- The curly
bracket in (4.1.36) is of the order of Ogg) and is usually small for
large g and 6; not close to grazing. In numerical simulations, g is usually
chosen to be somewhere between £ to 4, depending on the incident angle.
The advantage of the analytical expression of (4.1.31) is that Wine can be
evaluated readily for any x and z. However, the right-hand side of (4.1.36)
can grow as aby as 6; > 90°. Thus Wine of (4.1.31) should not be used for
problems of low grazing angle (LGA) incidence where 0; — 90°. To calculate
--- PAGE 143 ---
120 4 RANDOM ROUGH SURFACE SIMULATIONS
the Poynting’s vector of the incident wave, note that
zs 1
3S —-——Im(V" 4.1.37
Onk mV") (4.1.37)
At z =0, by using (4.1.37) and (4.1.31), we have
(@-Bine)owo = — etn ( bing Wine (4.1.38)
‘ine)z=0 = onk Vine Oz 0 dee
2x?
LJ peoso, (t= G1 | aksin aj tan dir? | 22 (4.1.9)
=o —t | — Se Le
2nk ‘ (kg cos 6; )? k2g4 cos? 0;
The power received by the rough surface is obtained by integrating over x
from —oo to co
oe a
Pine = -/ de (5-2).-0 (4.1.40)
-0o
On integration,
cos 6; T 1+ 2tan? 6;
Pine = ——9\/541- =; Al.
me 2n oz{ 2k2g? cos? 0; (4.1.41)
A second way of tapering is to taper the incident wave in the spectral
domain. Let
2° — ke, — kin 2@2
Wine(2, 2) = iz / ~ ky chet thee exp[-Ge— Bal) (4.1.42)
The advantage of using (4.1.42) is that it obeys the wave equation exactly
since it is a spectrum of plane waves. Note that |x| can be very large while
|2| is moderate. The disadvantage of using (4.1.42) is that the vinc(x, f(x))
has to be numerically evaluated by performing the integration of (4.1.42).
The integrand in (4.1.42) can be highly oscillatory for large |2|. To avoid the
oscillatory integrand, one can carry out a numerical contour integration as
shown in Fig. 4.1.2. Let x > 0 and consider general z. Consider the domi-
ag
nant exponential factor exp(ik,x — Ee), Let ke = ki, + ik. The dominant
exponent term for large value of zx is,
en — Kix)2g?
exponent = ik, x — Gael
Mad J p )2 PP) q2
=i [ee - BL, - 7) - [xe + he = hoo) ~ Beet
Tf we let
2a
ky e
--- PAGE 144 ---
81.3 Tapering of Incident Waves and Calculation of Scattered Waves 121
ke
a
oe ‘s
-k ¢ h
| | ,
Figure 4.1.2 Contour in complex plane of ky.
then
2 , 292
a ki, — k,
exponent = ikjrr — [5 + Gate)
The exponential has constant phase and the real part decays rapidly from
Kh = kin.
The contour C consists of I), I2, and Iz in the complex ky-plane. Contour
J, is parallel to real kz-axis at a distance 22/g? above it, and Re(kz) runs
from ~oo to k. Contour Iz goes down on the left-hand side of the vertical
branch cut at k and goes up on the right-hand side of the branch cut. Contour
Jy is parallel to the Re(k,)-axis and at a distance of 2r/g? above it and runs
from k to oo.
rs
g 1 | -ikez
Dine(t, 2) = dk [e*|
incl 2) Ir la! ® ke =k 4i2e/g?
eo he biao? 2?
exp [tet a a
0
g J | tk.
tse |] ak [em]
Qn [i * hem +ida/g?
. (ki, = Kin)?g? a?
exp [ia ny e
di ka — kie)?g?
+ xf, lg of #72 prep |_ Hz = Fie)" (4.4 43)
27m Si) 4
In numerical integration, (4.1.43) converges much faster. Vor x < 0, similar
formula can be established. Note that Jy is a short contour as the “length”
--- PAGE 145 ---
122 4 RANDOM ROUGH SURFACE SIMULATIONS
of the contour normalized by k is 2{a|/(kg), which is much less than 1 even
when |z| = L.
To calculate the power impinging upon the surface, we have, from
(4.1.38) and (4.1.42)
= 1 2 poo , = fe. 2G
Sines 2= - Im al dk, eikia—i/F he xp _ (ke Kin)" g
2nk At fice 4
°° ikea-bike 2. ke — kix)?g?
. | dk, c~®®+18-*ike* exp [- (ease) (4.1.44)
50 4
On substituting (4.1.44) into (4.1.40) and integrating over dx, we get a Dirac
delta function so that ki, = k,. Because the imaginary part is taken in
(4.1.44), only propagating waves contribute to power. Thus
2 pk 22
g (ke = kix)"g
Pine = — te kz exp| ———_——+*— 4.14
ine = Ee ff the «| ; (4.1.45)
Scattered Wave
After the surface fields (7) and #-Vw(F) are calculated by numerical meth-
ods, the scattered wave can be calculated by using Huygen’s principle. We
describe general nonzero surface fields of (7) and i - Vy(F) so that the
results of the scattered wave are also applicable to the two media problem
to be treated in Section 2. From (4.1.8a), the scattered wave is
WF) = ~ [as [WFR Val(F.7) — oF.7F)A-Vd(F)] (4.1.46)
Ss
Given ¢(7) and n-V4y(¥) on the surface, 7,(7’) can be calculated by carrying
out the integration in (4.1.46).
To calculate bistatic scattering coefficients, we put 7’ in the far field. For
observation in the k, = sin#,# + cos 6,2 direction,
mot) 2] 2 it ike’ ,—ih(sin0,2-+008 0.2)
F)=-/—\ ei" @ * ° 14
GFP) WWame ‘ee (4.1.47)
Then
(n- Vo(F',7)) 1+ af i 2 ett ihr,
MO aha) dz) ~ 4V ake!
[42 assim 05)— ik cos 0, @~ih(sin Oce+-c0s 8. f(x) (4.1.48)
--- PAGE 146 ---
§1.3 Tapering of Incident Waves and Calculation of Scattered Waves 123
Putting (4.1.47) and (4.1.48) in (4.1.46), we have
bP) = i lee 5 a y)(6,) (4.1.49)
‘ AV wkr! vs . .
where
N °° df
WO) (05) = — [ daz 4 — U(x) +u(x)ik| = sin 0, — cos 0,
Joo dx
. eik(sin 0,2~f() 2086.) (4.1.50)
and u(x) = o(«,2 = f(x)) is the surface field, and U(x) = (fh Ve)z-5@@)
Vit (tp is proportional to the normal derivative of the surface field. The
Poynting’s vector in direction k, is
1 he ees
S37) = 5 (vs F VOT) (4.1.51)
Tn the far field, this becomes
s@-E (1, \wio)l" (4.1.52)
. 2n \8rkr’ } VSS _
The total power scattered is
— f aacrsar) =f ao, £() wore! ;
Pom [ dber'siet)= f° a ay (aan) ol 41.88)
The bistatic scattering coefficient o(6;) is defined so that
P, 2
a f dO, 0(8s) (4.1.54)
Pine x
giving
1 1 ° 2
i(N)
ay ankles (8s)
o(0,) = 21 ani | (4.158)
Pine
The definition of o(0.) is such that [20.016.) = 1 for non-penctrable
rough surface. For the spatial domain tapered incident wave, with Pine given
by (4.1.41), we have
Ny 2
, jw 1] as
(8s) = soky, Reosa, fy. be 2tan? A (4.1.56)
-q, |e cos _ :
BRIA] 9 CRM 2k2g? cos? 0;
--- PAGE 147 ---
124 4 RANDOM ROUGH SURFACE SIMULATIONS
For the spectral domain tapered incident. wave of (4.1.42) and (4.1.45) we
obtain
N) 2
o ws @)| as
o a, a aC Tre 15
. 2 x (ke ~ kin)?g?
Ang dkz kz exp |--————=——
-k 2

1.4 Random Rough Surface Generation
In this section, we describe how to generate realizations of random rough sur-
face. We generate Gaussian rough surfaces with Gaussian correlation func-
tion, Gaussian rough surface with band-limited ocean spectrum, and fractal
rough surface.
1.4.1 Gaussian Rough Surface
A process f(x) is Gaussian if the random variables f(x1), f(x2),.... f(@n)
are jointly Gaussian for any n, «1, £2, ..., 2n [Papoulis, 1984]. The Gaussian
process is completely characterized by the correlation function (f(x1)f(x2))
= h?C(a1, 72). If the rough surface f(x) is statistically translational invari-
ant, then C(a1,22) = C(a1 — x2). The Fourier transform of h?C(a) is the
spectral density W(k,).

To generate Gaussian random rough surfaces, we use the results from

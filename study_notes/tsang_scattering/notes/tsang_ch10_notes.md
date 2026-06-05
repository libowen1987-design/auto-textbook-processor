# Tsang《Scattering of EM Waves》Chapter 10

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 10

> **第十章：稠密介质辐射传输**。研究稠密随机介质的辐射传输理论，包括有效介电常数模型、散射衰减和相干传播常数、相干反射与非相干散射、简单DMRT理论、体积分方程模拟、以及基于T矩阵形式化的数值模拟。**

DENSE MEDIA MODELS AND
THREE-DIMENSIONAL SIMULATIONS
1 Introduction 496

> **第1节：引言**（第496页）

2 Simple Analytical Models For Scattering From a Dense

> **第2节：稠密介质散射的简单解析模型**

Medium 496
2.1 Effective Permittivity 496

> **2.1 有效介电常数**

2.2 Scattering Attenuation and Coherent Propagation Constant 500

> **2.2 散射衰减与相干传播常数**

2.3 Coherent Reflection and Incoherent Scattering From a

> **2.3 分层介质的相干反射与非相干散射**

Half-Space of Scatterers 505
2.4 A Simple Dense Media Radiative Transfer Theory 510

> **2.4 简单稠密介质辐射传输理论**

3 Simulations Using Volume Integral Equations 512

> **第3节：使用体积分方程的模拟**

3.1 Volume Integral Equation 512

> **3.1 体积分方程**

3.2 Simulation of Densely Packed Dielectric Spheres 514

> **3.2 密堆积电介质球的模拟**

3.3. Densely Packed Spheroids 518
4 Numerical Simulations Using T-Matrix Formalism 533

> **第4节：使用T矩阵形式化的数值模拟**

4.1 Multiple Scattering Equations 533

> **4.1 多次散射方程**

4.2 Computational Considerations 541

> **4.2 计算考量**

4.3 Results and Comparisons with Analytic Theory 545

> **4.3 结果与解析理论比较**

4.4 Simulation of Absorption Coefficient 547

> **4.4 吸收系数的模拟**

References and Additional Readings 548
- 495 —
--- PAGE 515 ---
496 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
1 Introduction

In scattering of waves by densely packed media, the particles do not scatter
independently. The correlated scattering between particles has to be taken
into account. This was verified by controlled experiments [Ishimaru and
Kuga, 1982; Mandt et al. 1992; West et al. 1994]. In Volume II], we study
extensively the analytic theory of dense media scattering. These include the
Feynman diagrammatic methods leading to the Dyson equation and the
Bethe-Salpeter equation. Yo make analytic theory numerically tractable,
approximations have to be made on the mass and intensity operators. In
Volume IIT, we study the quasi-crystalline approximation (QCA), the quasi-
crystalline approximation with coherent potential (QCA-CP), the corre-
lated ladder approximation and the dense media radiative transfer theory
(DMRT). These approaches take into account the pair-distribution func-
tions of particle positions for which we have used the Percus- Yevick pair-
distribution functions as illustrated in Chapter 8. Near-field coherent wave
interactions are also included. In this chapter, we study Monte Carlo simu-
lations of three-dimensional dense media. In Section 2, we first formulate a
simple analytic model for scattering by dense media. In Section 3, we use a
volume integral equation approach for Monte Carlo simulations of spheres
and spheroids. In Section 4, we use the T-matrix approach. Scattering sim-
ulations include up to 5000 particles. We simulate the extinction rates and
the phase matrices. The scattering results compare well with dense media
analytic theory for the case of spheres. However, for complicated cases of
densely packed media such as densely packed nonspherical particles, numer-
ical simulations of Maxwell’s equations become more attractive.

2 Simple Analytical Models For Scattering From a Dense

> **第2节：稠密介质散射的简单解析模型**

Medium
2.1 Effective Permittivity

> **2.1 有效介电常数**

Consider a distribution of spheres with permittivity ¢; embedded in a back-
ground medium of permittivity ¢. Let the medium have polarization P
(Fig. 10.2.1).

We first determine the field created by polarization P inside a sphere
on itself. Consider a single sphere with polarization P = 2P and let the per-
mittivity outside the sphere be ¢ (Fig. 10.2.2).We next calculate the electric
field due to the polarization P. Let ©, and ©, be the scalar potentials
--- PAGE 516 ---
§2.1 Bitective Permittivity 497
" C1)
Figure 10.2.1 Collection of dielectric spheres.
outside and inside the sphere, respectively. Solving Laplace’s equation.
A
Bout = 2 cos @ (10.2.1)
®;,, = Broosé (10.2.2)
The boundary conditions at r =a are
Dour = Pin
eh Vou = eh VPin +A P (10.2.3)
‘Yhus with i =? and 2 = cos? — sind@
A
+= = Ba 10.2.4
@ = Ba ( )
2A
cz = -cB+P (10.2.5)
a
Solving (10.2.4) and (10.2.5) gives
P
B= 10.2.
% (10.2.6)
The electric field inside the sphere FE, due to this P is
= . P
Ey = —V%%, = —Bz = -% (10.2.7)
Note that E,, is not the total field of the problem. It is only the field due
to polarization P (Fig. 10.2.2). Next we consider the collection of induced
dipoles shown in Fig. 10.2.1. Let the electric field inside the medium be E.
Consider the electric field E* exciting a particle. It is equal to the electric
field E minus the electric field created by P. Thus
--- PAGE 517 ---
498 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Figure 10.2.2 Polarization in a dielectric sphere.
ae =,P
EB =E+ 10.2.8
3e ( )
Under the exciting clectric field E*, the dipole moment induced inside the
sphere is p, with
p=aE (10.2.9)
where a is the polarizability of the sphere. The polarization P is the dipole
moment per unit volume. Thus
P=n.p (10.2.10)
where mo is the number of spheres per unit volume. Putting (10.2.8),
(10.2.9), and (10.2.10) together gives
> ae _ P
P=naE = na (F+ x) (10.2.11)
€
Solving (10.2.11) gives
P=" FE (10.2.12)
1 3e
The electric flux density D is
D=E+P (10.2.13)
Putting (10.2.12) in (10.2.13) gives
Qnoa
B 1455
=~ = nae 3 a 5
Da B+ Toa = ar EB (10.2.14)
3e 3e
The effective permittivity is co such that
D = eg E (10.2.15)
--- PAGE 518 ---
§2.1 Effective Permittivity 499
Comparing (10.2.14) and (10.2.15) gives
14+ noc
fe = € | (10.2.16)
ye
3
Next we determine the polarizability a of a sphere of radius a and permittiv-
ity ¢», consider E* = E°2 to be the exciting field upon the sphere. Let ®oyy
and ®;, be the scalar potentials outside and inside the sphere, respectively.
Solving Laplace’s equation by letting
Bou = —E*r cos + A cos 6 (10.2.17)
r
®;, = Brcosd (10.2.18)
The boundary conditions are the continuity of the potential and the conti-
nuity of the normal component of the displacement. At r = a
Bout = Pin (10.2.19)
OBout _ — IPin
Gp =P Op (10.2.20)
Using (10.2.17)-(10.2.18) in (10.2.19) (10.2.20) gives
tat A
—EB*at+ Qo Ba (10.2.21)
2A
Et — aCe 6B (10.2.22)
Solving (10.2.21) and (10.2.22) gives
3eKe
B= 3 (10.2.23)
@ + 2€
Thus the induced electric field inside the particle is
_ 3B"
Ein = —V8in = <4 (10.2.24)
The induced dipole moment inside the particle will be
P= voPin (10.2.25)
where Pj, is the induced polarization inside the particle. Thus
Pin = (@ — OE in (10.2.26)
Using (10.2.24) -(10.2.26)
_ _ Uo(Ep — €)3€ Re
=“ SE 10.2.27
P €p + 2€ ( )
--- PAGE 519 ---
500 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Comparing (10.2.27) and (10.2.9) gives the polarizability
(-9)
= 3eu, 10.2.28
a = 3ev ep oe ( )
Putting a from (10.2.28) in (10.2.16) gives the effective permittivity of a
medium consisting of particles of permittivity ¢, embedded in a background
medium of permittivity ¢.
1+2fy
cot = € | ——— 10.2.29
oe (TF (0228)
where
f= novo (10.2.30)
is the fractional volume occupied by the particles and
& —€
=“ 10.2.31
9 & + 2€ ( )
Equation (10.2.16) is known as the Clausius-Mossoti formula or the Lorentz-
Lorenz formula. On the other hand, (10.2.29) is known as the Maxwell-
Garnett mixing formula. The Maxwell-Garnett mixing formula can be put
in the following symmetric form
Cott ~ € & —€
— = f-— 10.2.32
€egt + 2€ foam ( )
which is also known as the Rayleigh mixing formula. Given the effective
permittivity, we can also calculate the effective propagation constant K with
K =w\/jita (10.2.33)
so that
2 gl +2ft
Kea eittly (10.2.34)
1—fy
However the imaginary part of the effective propagation constant K in
(10.2.33) only accounts for absorption. To include the attenuation due to
scattering, we have to take into account incoherent scattering which we will
study in the next section.
2.2 Scattering Attenuation and Coherent Propagation Constant

> **2.2 散射衰减与相干传播常数**

In this section, the coherent propagation constant is calculated by including
the attenuation due to scattering. The scattered intensity can be attributed
to the radiation of the induced dipole that is induced by the exciting field.
--- PAGE 520 ---
§2.2 Scattering Attenuation 501
From (10.2.8) and (10.2.12)
xe E E
EF =—, = —— (10.2.35
T= 38 hu
From (10.2.9) and (10.2.35), we have
aE 3eugyE
pee 10.2.36
l-fy 1-fy ( )
Since the electric field E is in the medium that has effective wavenumber K.
Let A, = Re(K). Thus we can write
E = yee (10.2.37)
where é is the polarization of the electric field and K, is the wavevector with
|K,| = K,. At the position 7; of the ith particle, we have induced dipole
moment
= — 3vocy K.F.3
B= Tf E&KeTe (10.2.38)
The radiation field of the ith particle is

_ w2yethhe .

Eg(t) = am x pi) x Rj (10.2.39)
and R; = 7 —7; is the vector pointing from the ith dipole to the observation
point. . _ .

In the far field direction ks, we have |F;| = r—ks-7; and using (10.2.38)
and (10.2.39)
By(?) = Ad; (10.2.40)
where
Jj = exp(ia - Fi) (10.2.41)
a=K,—ks (10.2.42)
and
__B2gBeikr .
A="** (ki, x @) x k——F, (10.2.43)
r 1—fy
is a vector independent of i. The total scattered field is the sum of the
radiation fields of all the dipoles. Hence,
N
E,= Au (10.2.4)
1
--- PAGE 521 ---
502 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
The radiation intensity I, is
= sje | 4 NON
_ |Es? _ [AP 2 *
1 oy = ay Va + di
i=l i= it
ime
‘ae NN
=a Nt Sy nF (10.2.45)
i=1 i=
iat
We decompose J, into coherent and incoherent intensity,
Bs)P _ (Bs?) _ Es)?
Zs) = (Is) — Som = 10.2.4
(.) = (ly) = GE = St (10.2.46)
[AP ‘
= — {N iJ* 2.
(h)= 5 + J) (10.2.47)
arn
Calculating the configuration average of the second term in (10.2.47) gives
Al? r mF, —F.

UIs) = oC {+x - 1) far: f arspatrrine uc) (10.2.48)
where po(7i,7;) is the joint probability density function of particles located
at 7; and 7;. On the other hand, the coherent field is, from (10.2.44)

(B,) = NA [ arplrje™™ (10.2.49)
Letting
1
wr) = 5 (10.2.50)
a py MFT, ‘
pa(FiF;) = aT) i) (10.251)
where g(7) is the pair distribution function, we have
(Es) = nod f are (10.2.52)
[AP 2 = AlF. — F.\ ei (Fi-Fy) 9
(Ix) = op N+ng | dr; | drj9(7i—7;)e (10.2.53)
Coherent scattered intensity is, from (10.2.52)
(E)P _ ndlAP fo. ia(r.—F, 2.54
om =o dr jee) (10.2.54)
--- PAGE 522 ---
§2.2 Scattering Attenuation 503
By taking the difference of (10.2.53) and (10.2.54), we have the incoherent
intensity as
IAP f, m7) (on,
Le) = yp [Nm fare f arje™O™ (90% -7))—1)
Al? -_ ar
= a {x + ¥ng [ are™* (ar) - i)
Al? ar l=
= no eV {1 +n / dre® *(9@) - 1) } (10.2.55)
We further assume spherical symmetry of pair distribution functions.
GF) = g(r) (10.2.56)
Also
g(r) =0 for r <b = 2a
As r — 00
g(r) =1 (10.2.57)
As shown in Chapter 8, g(r) is practically equal to unity for r larger than a
few diameters. We assume that ka < 1. However, if, say ka = 0.2, 3kb = 1.2
is not much less than unity. Thus, we may need to keep the e’*? term in
(10.2.55) Let
y= gop [ar a (10.258)
H@) =e / F(g(F) — Ie"? 10.2.58
(2) Joe
be the structure factor. Then
2
(Z,) = nol y {1 + (20) nol (ks — Ky)} (10.2.59a)
7
Let é be in g direction and K, be in 2 direction, and
ky = sin @, cos d,# + sin 8, sin ds + cos O52
Then
i. 4 Pat 2 2 2
|(k x é)x i.| = (sin* 4; cos” ds + cos” 45)
The total incoherent scattered power is obtained by integration of the inco-
herent intensity over 47 solid angles.
P= f ara.)
Jan
og Qn 2 pe
4 E.
= ‘ sektae|—¥__| Bo
| ds sind f dosk*a T— ful 2
noV {1 + (2)*nol (ks — Ky2)} (sin? 4, cos” 6s + cos” O,) (10.2.59b)
--- PAGE 523 ---
504 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Since by spherical symmetry
H (ks — K,2) =H (ks ~ K,3|) =H ( /k? sin? 0, + (cos Os — ,?)
(10.2.60)
is independent of ¢,. Then
" sin? 6 3 y PE
P. =2n f dO, sin 8. (S% + costa ) k4a8 al 2
. oN . 1—fy| 29
meV {1+ (20) rofl ([Rs — K,2\)} (10.2.61a)
Suppose we have a cylindrical volume of area A and length / containing 7%
particles per unit volume. The input power due to the wave in (10.2.37) is
1
i, eet \?
Pin = 5 ERA (= 10.2.6
in = 3H ( it ( 1b)
The number of particles in the cylindrical volume is N = n Al. Let Ks
denote the scattering rate and Kg denote the absorption rate. The scattering
attenuation rate denoted by ks is given by
P, P,
ks = > = ——+_, (10.2.61e)
[Pin 1 rey ( &# 2
2° b
Putting (10.2.614) into (10.2.61¢) gives and using ,/ 25 = Bs f = 4nnga*/3
3k5a8 ar sin? 4 :
Ks ates | dO, sin, ae + cos? t)
{1 + 20) nol (Rs — K,al)} (10.2.62)
For the special case that the correlation is short ranged so that:
_ . 1 +00
H (\ks — K,2|) & H(0) = of. dF (g(r) — 1)
1 dn 3
= ag + ArbF Hop (10.2.63
ar { g + And'Ho ¢ (10.2.65a)
where
oo
Hy = [ doo” (g(ab) — 1) (10.2.63b)
1
For the short ranged case, putting (10.2.63a) in (10.2.62), we can integrate
over 9, to get
2k? a3 y -
ts = —— fi——| 01-8 24f A 10.2.64)
n= PEE || (18g +24) (10.2.640)
--- PAGE 524 ---
§2.3 Coherent Reflection aud Incoherent Scattering 505
The scattering attenuation can be added to the effective propagation con-
stant of (10.2.34) as follows
K? ~ K?+iK,(2K;) = K2 +ik,(a + ks) = K?2 +iK pa +iK; hs
= (K* absorption only + 1K rks (10.2.64b)
Using (10.2.62), (10.2.64a), and (10.2.34)
: 14+2fy) 355; Pot
Kael tty). Bpoqs5 res | x | d0,sin 8,
1— fy 2 1- fy 0
nd : ; _
: ( + cos? ) {1 + (20)8noH (|ks - K,a\)} (10.2.652)
Equation (10.2.65a) is the general result for small particle but longer ranged
pair distribution function. If the pair distribution function is short ranged,
we have
o(1+2f1 : 2
Ke = EASY 50 64503 al (1—8f-+24fHo) — (10.2.656)
1-fy 1—fy
2.3 Coherent Reflection and Incoherent Scattering From a Half-

> **2.3 分层介质的相干反射与非相干散射**

Space of Scatterers
Consider a plane wave incident on a half-space of dielectric scatterers
(Fig. 10.2.3). We shall first consider vertically polarized incidence. The case
of horizontally polarized incidence can be treated in a similar manner. The
incident wave is in the direction (6;,¢;)and the incident field is Eine =
GigE, exp(ikia 7) with kiq = sin 0; cos j% + sin 6; sin dj — cos 6:2, bia =
~ sin @% + cos dif, and Gig = dia X kia forming the orthonormal triad. The
subscript d is to denote the fact that the wave is propagating downward. In
the lower region, the coherent effective propagation constant is A. The trans-
mitted macroscopic field is Ey with propagation direction following Snell’s
Jaw is:

E,= BT oF 7 (10.2.66)
with K given by (10.2.65), Kg = ksin0jcos¢i% + ksin@sindgy —
VK? — k? sin? 6,2 = K,t+Kyy—-K,2, 81a = — cos O cos :%—Ccos 0, sin o;9—
sin #2 and @; is the transmitted angle obeying Snell’s law

sin = # sin 6; (10.2.67)
K,
The Fresnel transmission coefficient for TM waves is TEM for the magnetic
--- PAGE 525 ---
506 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
z
scattered
incident wave
wave
~ Os ke
Kia\ 9.
Figure 10.2.3. Plane wave incident on a half-space of dielectric scatterers. Induced dipoles.
field with
: 2K7k;
Th = > 10.2.68
0 Rk: + KS ( )
where ki, = kcos 6; and K, = VK? — k? sin? 6;.
Dipoles are induced in the dielectric spheres and the dipole moment jp;
of the jth particle, centered at F; is, using (10.2.38),
= 4  30Y apm FOR
= O0%4—— Toy" se'"**" 10.2.69.
P; aT Py a Re (10.2.69)
The total radiation field of the dipoles is then
N
EF) = OW; (10.2.70)
j=l
where J; = exp [i(Ka —ks)- Fj] :
—unetkh 2k 5 Busey para &
w-% He ke fp PRY pam *
Tp tks * Ota) * Bs Ty
kadeikr , Yoru k
= lbs x a) eT (10.2.71)
k, = sin 0, cos ost + sin Os sin OY + COS O52 = ksr¥ + ksyif + ksz2 is the prop-
agation direction of the scattered wave with ky = kks.
--- PAGE 526 ---
§2.3 Coherent Reflection and Incoherent Scattering 507
Coherent Reflected Field
To calculate the coherent scattered field, the configuration average of
(10.2.71) is taken
= N —
(E<(F)) =W (Jj) =WN{J;) (10.2.72)
j=l
Since p(7;) = %, we have, on evaluating (J;) by integrating over the lower
half-space,
1 oe 20 0 ee
Gyas dx; dy; dajel Rake)
Vv 09 0° 00
giving rise to 6(Kz — ksx) 5(Ky — ksy) indicating that the coherent scattered
field is in the specular direction.
- ee a
E,) =n,.W——— o(k sin 8. bs — ksin 8; cos @
(E,) =n (K, + hn) (k sin 6, cos bs sin 8; cos di)
- d(ksin 0, sin ds — ksin 6; sin d;) (10.2.73)
For ky in specular reflected direction
(ks x Oa) x ky = — c08(6; + 6:)6; (10.2.74a)
We make use of the relation of (10.2.34) so that
a _ elk a - am & ‘
noW = — (—cos(6, + 6)br) (5? — RTM (10.2.74b)
Also K? — k? = (Kz + kiz)(Ke — hiz), 8o that
4r?ingW  wiet*r aya ru k °
Koaike r (- c0s(0; + #4)6t) (Ke—kis)T Ge (10.2.74e)
We make use of the relation
kis K? + kK,
(K, + iz) cos(0; — )) = “=X +E Se (10.2.74¢)
kK
so that
om & kj,
Th = = ——_=_—_-~ 10.2.75
OL KR (K+ iz) 0030; — 0) (10.2.75a)
Also we have
K.—kiz\ cos(@i+%) — K*kiz — kK, cM
a ) ae ER 10.2.75b.
(z + kiz ) cos(0; 0) Kk, +h? K, ( 5b)
--- PAGE 527 ---
508 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Putting (10.2.75) into (10.2.74¢) and (10.2.73), we get
_ . eikr
(E,) = — 620k. RA lk sin @, cos @, — k sin 6; cos ¢;)
- d(ksin 6, sin gs — ksin 6; sin dj) (10.2.76)
Thus the coherent reflected wave is in the specular direction, containing no
depolarization and obeying the Fresnel reflection formula for TM waves.
The case of horizontally polarized incident: waves is treated in a similar
manner. For an incident field of Bing = 6; Ey exp(ikja- 7). The result for the
coherent reflected field is
. aon elk
(EF) = — 6; i2ki: REP — 5(ksin 8, cos d, — ksin 6; cos 6;)
r
- 6(k sin 6, sin ¢, — ksin 6; sin ¢;) (10.2.77)
where
kiz — K;
ROY = == 10.2.78
01 Kiz +K, ( )
is the Fresnel reflection coefficient for TE waves.
Incoherent Scattered Field
The incoherent scattered field €, is €5(7) = E,(7) — (Es(F)). Hence, the
incoherent intensity is
N NON
= _ a9 ‘ 2
(E.(7) -EZ(7)) = wrt Sua) $V ilf) | uni} (10.2.79)
isl i=1 y
Following a similar procedure as in Section 2.2, we have
(&-E,) =|"? ees tnt far [ toe -F;))-1]
sows WMm(K,) ef Tf IES
» Ka. iK iF ¢ Bevan (10.2.80)
where Ag is the area of the target area. The integral in (10.2.80) can be
carried out readily. Hence,
7) EF a72__Ro‘so zl o(F ReK «—k.)-F
E509 Es) = WP spre {1 + no f a lor) — 1] ee vt
(10.2.81)
--- PAGE 528 ---
§2.3 Coherent Reflection and Incoherent Scattering 509
where for vertically polarized incidence, W is given by (10.2.71) and for
horizontally polarized incidence
a wpe” 4 — BUoey
V = ——__(k, x 6; te (1 + REP
W dar (hs x Gi) x Be S (1 + Ron )
Kaveh . Y Qkiz
= —— (kg x gi) x kk —- >——_ 10.2.82a
7S 0) BTR hin ( )
so that
a. elk, * 2k,
w =o ((k . . 2 po iz 2.85
ng = T— ( (hes bs) > hy) (A? ~ B) ney (10-2828)
In backscattering direction,
kis x (hs * oi) = os.
Thus
a Kz —kiz)kiz\?  noAg 1
Es a) | 2 = ( cd iz Miz '0- a
(les@P) | No 2hn(Kz)r? 4a?
ia zk)
: { + no [ dF(g(F) — 1)et(ReK eke) “} (10.2.83)
-00
The backscattering coefficient is
4nr? (\E5(F) |?
ona) = AEE
Ag
so that
(Kz —kiz)kiz |? no me ReRa-ky)¥
we [MA Meee) ite) Fi =) — ])ei(ReKa-k.)F
ohh | he Saint Ut J F(g(F) — le
(10.2.84)
For the case of vertical polarized incidence, we can perform similar calcula-
tions. In the backscattering direction, 6, = 0; and ¢, = 7+i, ks x (ks Ota) =
—cos(#; — 6;)@s;. Hence, the backscattering coefficients are the same for oy,
and o7,,. We have
_ _ |(Ke=hiz)hiz|? Mo
ovvlOi) = onn(Os) = | No 2nIm(K,)
oc sot).
x {i +10 / dF (g(F) — eeeReRory (10.2.85)
J—00
The results of coherent reflection in this section agree with the QCA results
in the low frequency approximation. The bistatic intensity agrees with QCA
combined with distorted Born approximation. The QCA approximation will
be treated in Volume III.
--- PAGE 529 ---
510 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
2.4 A Simple Dense Media Radiative Transfer Theory

> **2.4 简单稠密介质辐射传输理论**

A simple dense media radiative transfer theory can be developed based on
the derivations of Sections 2.1 and 2.2. The model is based on the assumption
that the particles are small so that ka < 1. However because the particle
positions can have long-range correlation (e.g., sticky particles), the correla-
tion distance can be comparable to or larger than a wavelength. Specifically,
say ka = 0.2 and the correlation distance is up to 5kb, where b = 2a is the
diameter. Then 5kb = 10ka = 2 is larger than unity.
First we calculate the effective propagation constant which is determined
by (10.2.65a)
2 ,20+2fy) 3,5 4 y [Tp , (sino :
K? = 72+ 2s) +i5k*a3 f |—_ d6 sin 8 | ——— + cos? 0
l-fy 2 1—fyl Jo 2
{1 + (2m)*noH(\/k2 sin? 6 + (k cos 0 — x} (10.2.86)
The effective propagation constant is
K=K,+ik; (10.2.87)
The extinction rate is
ke = 2K; (10.2.88)
The structure factor is
1 iad red
A(p) => dr(g(F) — le?" 10,2.89
©) = as [-artatr) - 1} (10.2.89)
Because of spherical symmetry, this can be expressed as a sine transform.
- 1 8 sin pr
H(”) =H) = 55 | der (g(r) — ye (10.2.90)
In practice, it is often easier to calculate the structure factor than calculating
the pair distribution function. The scattering rate is
3 ka? am in? 9 :
Ks = lal [ désiné > + cos? @
{i + (20) bnoH (ve sin? @ + (k cos 0 — K)) } (10.2.91)
To calculate the phase function, we first consider scattering using the
1-2 system. Consider propagation in the 7 direction and incident polarization
in the 1, or 3; as done in Chapter 1, Section 1.2 of Volume I. The scattered
direction is § = ks which makes an angle © with the incident direction. The
polarizations of the scattered wave are in the 1, and 2, directions. Then,
--- PAGE 530 ---
§2.4 Dense Media Radiative Transfer Theory 511
we can apply the analysis as in Section 2.2. The polarization dependence of
(ky x €) x ky of the scattered wave is that of Rayleigh polarization dependence
(ful?) = lfol?V [1 +@ny'not (ve sin? © + (kcos © — KP)| (10.2.92)
where V is the volume containing the scatterers and the number of particles
in V is noV. In (10.2.92)
5q6 2
lol? = ste [al (10.2.93)
Following similar analysis
(fiz?) =0 (10.2.94)
(\far2) =0 (10.2.95)
(| foal?) = Lfol?V F + (20)?noll (ve sin? © + (kcos@ — K)] (10.2.96)
For the phase matrix in the 6, h system, results are similar to that of Rayleigh
phase matrix except with the inclusion of the 1+ (Q27)8noH factor. Thus, in
the vertical and horizontal polarization system, for incident direction (6’, ¢')
and scattered direction (@,) as done in Chapter 7, Section 2.1 of Volume I,
we have the phase matrix
Pn Pe Ps 0
D a! 1 Po Pos 0
P(O,6;0',6') = [i Py Pay 0 (10.2.97)
0 0 O Pra
where
Py =w [sin? Asin? ’ + 2sind sin @’ cosd cos cos(¢ — ¢')
+ cos? @ cos’ 6’ cos”(@ — 4')] (10.2.98)
Piz =weos? @sin?(¢ — ¢’) (10.2.99)
Pig =w [cos 4 sin 4 sin 6 sin(d — ¢') cos? 6
- cos #’ sin(d — ¢') cos(¢ — ¢’)| (10.2.100)
Px, =wcos? 6' sin?(é — ¢') (10.2.101)
Po, = wcos?(¢ — o') (10.2.102)
Po3 = — woos 6’ sin(¢ ~ ¢') cos(¢ — ¢’) (10.2.103)
Ps =w [—2sin 4 sin 6’ cos 6’ sin(¢ — 6)
~ 2cos 4 cos? 6! cos( — ¢') sin(d — ¢’)] (10.2.104)
P32 = 2w cos @ sin(d — 6’) cos(¢ — ¢’) (10.2.105)
--- PAGE 531 ---
512 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
P33 =w (sin @sin 6 cos(¢ — ¢’) + cos cos 6’ (cos"(6 — ¢’)
— sin’(@ ~ ¢'))] (10.2.106)
P44 =wsin @ sin &’ cos(¢ — ') + cos 6 cos 6] (10.2.107)
where
w= |fol? [ + (22)°noH (Vv k? sin? © + (kcosQ — K?)| (10.2.108)
cos @ = cos 8 cos 6 + sin @ sin 4 cos(é — ¢') (10.2.109)
3 Simulations Using Volume Integral Equations

> **第3节：使用体积分方程的模拟**

Simulations of particle positions by packing several thousands of particles
randomly in a box was done in Chapter 8. In this section, we solve Max-
well’s equations for scattering by these realizations of particle positions. The
simulations are performed over many samples (realizations) and the scatter-
ing results are averaged over these realizations. The results give information
about the collective scattering effects of many particles packed together.

In this section, we use volume integral equation to simulate the scattering
by densely packed spheres. We still restrict our attention to the case of small
particles. In Section 4, we shall use multipole expansions to study scattering
by spheres.

3.1 Volume Integral Equation

> **3.1 体积分方程**

Consider waves in an inhomogeneous medium with permittivity ¢,(7). For
the case of N discrete scatterers with permittivity «, occupying regions
Vi, V2,..., Viv, we have discontinuous permittivity ¢,(7) with
for? € Vj, j =1,2,...,N
(7) = {° orre i I=) (10.3.1)
e otherwise
Let the inhomogeneous electric susceptibility be
T
x(F) = of) -1=6(F)-1 (10.3.2)
where ¢,(7) is the relative permittivity. The electric field is, from (2.1.37) of
# Tsang《Scattering of EM Waves》Chapter 10

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 2,

> **第十章：稠密介质辐射传输**。研究稠密随机介质的辐射传输理论，包括有效介电常数模型、散射衰减和相干传播常数、相干反射与非相干散射、简单DMRT理论、体积分方程模拟、以及基于T矩阵形式化的数值模拟。**

EG) Binet) +R? fa gtr.r)x( VEC")
all space
+V [ ag FF)V' : (xP JER)) (10.3.3)
Jall space
--- PAGE 532 ---
§3.1 Volume Integral Equation 513
Note that the integration space of (10.3.3) is over all space. The first in-
tegral is over regions where (7) is nonzero, that is, where ¢,(7) 4 «. The
second integral is over space where V -(x{7)£(7)) is nonzero. For the case of
discontinuous permittivity like discrete scatterers, the jump of permittivity
across the scatterer boundary can have nonzero divergence at the boundary
and give rise to a surface integral. Thus V - (x(F)E(#)) in (10.3.3) can be
both zero outside and inside the scatterer and yet have a surface integral
contribution.
We can also use polarization density P(F). Let
P(F) = ex(F)E(F) (10.3.4)
Then (10.3.3) becomes
_ _ . Br
E(F) =Bine(P) + #? [ ager) ©)
all space €
Pr
+ vf dr'g(F.7)V' (2) (10.3.5)
all space €
We can recast the last term of (10.3.5) by using the divergence theorem
Pr
| dr’ g(7,7P)V' + (on )
‘all space €
Dis Dir
= [ ary - (ary) - [ ar (Vig(r,7))- PO)
Jall space € all space €
pL Py Pr
= f ds (orn) - | ae (Wor) PO (10.3.6)
Soo € all space €
The first term in (10.3.6) vanishes because of radiation condition at infinity.
Putting (10.3.6) in (10.3.5) gives
By
Bi) =Einti) +0 [arg
Jall space €
Pir
- vf dr’ (V'g(F,F)) - Pr) (10.3.7)
all space €
Equation (10.3.7) has an advantage in that one only needs to integrate over
regions where P(7) is nonzero (i.e., x(7) nonzero) and does not have surface
integral contributions as in (10.3.3).
--- PAGE 533 ---
514 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
3.2 Simulation of Densely Packed Dielectric Spheres

> **3.2 密堆积电介质球的模拟**

Let an incident electric field Eine(F) be impinging upon N number of ran-
domly positioned dielectric spheres. Sphere j is centered at 7; and has per-
mittivity ¢;,j = 1,2,3,...,N. The discrete scatterers are embedded in a
background with permittivity «. Particle j occupies region Vj. Let ¢,(7) be
the permittivity as a function of 7. Thus
—)_ fej forrin Vj
ep?) = {: for F in background (10.3.8)
The induced polarization P(F)is nonzero over the particles only. Let P;(7) be
the polarization density inside particle 7. Then the volume integral equation
gives
BW <5 25 f argtr.e im) _¥ regtotg gly PAP)
Er) = Binc(?) +k >| ar'g(#,7') 1) -yv/ aF'V'g(F7")-
ly, € a Ny €
(10.3.9)
To solve (10.3.9) by the method of moments, we assume that the dielectric
spheres of radii aj, j = 1,2,...,N, are small so that only dipoles are induced
inside the spheres. Let
E(7) = Ej(F) for F € Vj (10.3.10)
We expand the internal field E;(7) into electrostatic dipole functions
3
Ej) = >> ejaF jal?) (10.3.11)
a=l
where
Fz 1
f@) =2#— (10.3.12)
; Vi
=. .1 ae
Fil?) = IG (10.3.13)
z= my _3_! 3
figF) = 5 (10.3.14)
where vj = pur is the volume of the jth sphere. The normalization factor
is put in (10.3.12)-(10.3.14) so that
fDi Tya = 600 (10.3.15)
--- PAGE 534 ---
§3.2 Simulation of Dielectric Spheres 515

Substituting (10.3.11) into (10.3.9) results in

N 3
E@) = Eine) + 92S cjaFjal7) (10.3.16)
j=lo=t
where
Tal) =P ff arate PF ley —D-V f de'V' 907) Talons =)
v, Vv
; (10.3.17)
and €,; = © is the relative permittivity of the jth particle.

Of particular importance is the expression for 7;,,(7) when 7 is in V; (the
self term). The first term in (10.3.17) is a wave field while the second term
in (10.3.17) is dominated by the electrostatic field for 7 in Vj, assuming a
small particle. Thus for 7 in Vj

Gal?) ~ -v oF T'9 FP) Fjo(erj — V) (10.3.18)
v,
However, the right hand side of (10.3.18) is the electrostatic field produced
inside Vj by polarization Pj = F jq€(érj — 1) which by (10.2.7) is —S2 =
—4a2 (ej — 1). Thus for F in Vj,
o£ .
Tal?) & —22 (5-1) (10.3.19)
To solve (10.3.16), we apply testing functions of fia?) and dot product it
with (10.3.16) and integrate it over region Vj.
N 3
| F) Be) = ff arFig() Enel) +2 60 f drFig()-THalP
vi vi jaa Mi
(10.3.20)

Using (10.3.10) (10.3.11) indicates that the left hand side of (10.3.20) is
equal to cjg. The second term in (10.3.20) on the right hand side is decom-
posed into j #/ and j =/ terms. We thus have

, N 3 3 ,
as = far Fig Eine) +S) Yea fa Fig Tal + Dem fdr FigMal
vi i a= Vi ont vi
vat
(10.3.21)
Using (10.3.19) in the last term of (10.3.21) gives
N 3
=z ot pe a 1
cg = I a Fig» Bine(P) + >> Ca I GF fig Gal?) + op (- 3) (¢=1)
ae
--- PAGE 535 ---
516 10 DENSE MEDIA MODELS AND T'HREE-DIMENSIONAL SIMULATIONS
so that
3 _ N 3
n= ec) | ha Bonlt)+ Yim fai Tol) f (103.22)
2t+en| iy 7 a=l vi
pat
with 1 = 1,2,...,N, and 8 = 1,2,3. Equation (10.3.22) provides the matrix
equations of 3N equations for the 3N unknowns ¢g, | = 1,2,...,N and
8 =1,2,3.
By using the small particle assumption, the matrix elements ini (10.3.22)
can be simplified.
[ OF fig Eine(®) = w1S ig * Eine(T) (10.3.23)
Vi
For 7 #1
fF Fsl0) Tio)
a
-[ ar Fig {ef dg (FP )F jal€rj -1)
Vi Vv,
HV fava) Thales - o}
Jv,
© k(eng — Yury Fig GO-7)) - Fi (10.3.24)
where the dyadic Green’s function is
eo = VV\
GP) = (7 + v) g(F,7') (10.3.25)
Explicit expressions of Gr,7’) are given in (2.3.5)-(2.3.7) of Chapter 2.
Substituting (10.3.23) and (10.3.24) into (10.3.22), we have
3 _ N 3 _ _
a an {its Emer) + > Y> ejack™ (ery = ory fig CFF) Jnl
‘ jet
(10.3.26)
Equation (10.3.26) is the Foldy-Lax multiple scattering equations based on
volume integral equation. After the matrix equations are solved, the final
scattered field is
N _ seo
E,(7) -ey | dr'G(F,7') + Pil) (10.3.27)
; €
jae
--- PAGE 536 ---
§3.2 Simulation of Dielectric Spheres 517
We calculate the final scattered field 7 in the far field in the direction k=
(95,05). Let d, and h, be the vertical and horizontal polarization vectors
respectively. The polarization in particle 7 is
3
PsP) = Yo (ej — YegaFial™ (10.3.28)
asl
We have, putting (10.3.28) in (10.3.27) and taking the result in the far-field,
_ K2eikr a. KS Le _
Es(F) = (Oss + hshs) D> nye (65 — Veja ja — (10.3.29)
jela=
This can be written in terms of the horizontal and vertical polarized com-
ponents
_ . elke
EB, = (Eystis + Ejshs)—— (10.3.30)
with
eye a
Ewer SOY vje-®™ (Gj — Vejalts Fa) (10.3.312)
j=la=l
eee = .
Ens = 3 SOE je (Gry = Nejallts: Fig) (10-3.318)
j=la=l
The scattered power is
Qn aa Eye? + |Ensl2
P,= | dé, [ di, sin 9, esl + 1Pnsl*) (10.3.32)
0 Jo 27
To get the incoherent power, we have to subtract out the coherent intensity.
Thus,
Qn x 1 ,
pyncoherent — | do [ dB, sit B65 { (En ~ (Bos))?) + (|Bina ~ (Hns)I?)}
0 0
(10.3.33)
Equation (10.3.26) can also be put in the more familiar form of exciting
fields. From (10.3.26), we can also have
a 3 (_ N _ BL
SS eishig = 54 FinelF) + D2 P(Ej = DST) So Cio F ju
g=1 2+ er rm a=l
pat
(10.3.34)
The dipole moment is
3 =
Dj (F) = vjel€ry ~ IE; = vj¢(6rj — 1) YO ja F ja (10.3.35)
al
--- PAGE 537 ---
518 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Dipole moment is also equal to
= re rj — [ae
= aj EF, = 3evj; 4 F 10.3.

By = jk; WG e 2) (10.3.36)
where Ey is exciting field of particle j. Thus we have from (10.3.36) and
(10.3.35)

€ 1 3
a, ri — be F
Benj ae = vye(€rj — 1) Li tiedn
so that
3
pe Sg $2 = 2 97
Ej= a YS Gia F a (10.3.37)
a=l
Multiplying by (€,, + 2)/3 im (10.3.34) gives
N 3 =
E; = Eine(7i) + 0 (erg — Yuya): E; (10.3.38)
= rj

on

We recognize the scattering transition matrix clement of
2 &j—-1
tj = 3k? yj; 10.3.39
i ej +2 ( )
This puts the matrix equation in the form of the multiple scattering equation
of Foldy-Lax form based on exciting fields
N
Ey = Einc(Pi) + 9° G77) « t3E5 (10.3.40)
j=
ial
3.3 Densely Packed Spheroids
In this section, we perform Monte Carlo simulations of non-spherical parti-
cles that are non-sticky. We describe the formulation of scattering by many
spheroids in terms of volume integral equation. The method of moments
is used with choices of basis functions that are appropriate for spheroids.
The shuffling process to generate the positions of densely packed spheroids
was described in Chapter 8. Both cases of aligned orientation and random
orientation are considered. We illustrate the numerical results using several
thousands of spheroids. Salient features of numerical results indicate that
(1) the extinction rates of densely packed small spheroids are smaller than
those of independent scattering; (2) for aligned spheroids, the extinction
--- PAGE 538 ---
§3.3 Densely Packed Spheroids 519
Figure 10.3.1 An electric ficld Bj,.(7) incidents upon N non-overlap, small spheroids that
are randomly positioned and oriented in a volume V.

rates are polarization dependent, while for completely random orientation,
the extinction rates are polarization independent; (3) the co-polarized part
of the phase matrix is smaller than that of independent scattering, while the
depolarized part is larger than that of independent scattering. This means
that the ratio of cross-polarization to co-polarization is significantly higher
than that of independent scattering.

Let an incident electric field Eine(F) be impinging upon N number of
randomly positioned small spheroids (Fig. 10.3.1). Spheroid j is centered
at Fj and has permittivity ¢j, j= 1,2,3,...,N. The discrete scatterers are
embedded in a background with permittivity ¢. Particle j occupies region
V;. Let €p(7) be the permittivity as a function of F,

—_ fe for? in Vj 4
(7) = {s for F in the background (10.3.41)
Then the volume integral equation is. from (10.3.9)
N = of N tole 7
Br — Fak IFPI V9FP) 55 po
BE) = Ener) 4 9 [ar EO peo far’ PEP) pe
fo fi. c V, €
j=’ j=l
— (10.3.42)
where P;(7) = ex;(7)E;(7). To solve (10.3.42) by the method of moments,
we expand the electric field £';(7) inside the jth spheroid in a set of Ny, basis
--- PAGE 539 ---
520 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
functions
Ne
EjF) = Yo ajaF ja(F) (10.3.43)
a=l
Here the spheroid is assumed to be small, we choose the basis functions in
(10.3.43) to be the electrostatic solution of that of a spheroid.
Let the jth spheroid be centered at 7j with
Fj = 2jl + yi + 22 (10.3.44)
and the symmetry axes of the spheroid be #j, yj, and 24; with respective
semi-axes lengths be aj, aj, and c;. The orientation of the symmetry axis
2yy is
4y3 = sin J; cos aj% + sin G; sin ajy + cos 952 (10.3.45)
The first eight normalized basis functions for the electric fields are
= 1
Fi =%j— 10.3.46
jl ae ( )
> 1
5 = %;— 23.4
Fja = Fj Wa (10.3.47)
> 1
3 = ij— 10.3.4:
Jia = O05 Jour (10.3.48)
= 1 . . .
Jin = He (wojeoj + Yost; — 2205%s) (10.3.49)
/ Aaj
= 1 . . >
Fis = = (ej Fn) + 20%) (10.3.50)
VV A5j
_ 1 . . .
Fig = z= ojiinj + yoi2es) (10.3.51)
/ As;
s 1 » o q
Fiz = = (vjtr; — vests) (10.3.52)
V Ar
= 1 . .
Sig= Vin (ynj@vj + oj 90;) (10.3.53)
Ary
where Aq, a = 4,5,...,8, are normalization factors such that
[Fa Ts= ba (40.3.54)
v
In (10.3.54), a, 6 = 1,2,...,8, and V is the volume domain of the spheroid.
‘There are three basis functions for electric dipole and five basis functions for
electric quadrupoles.
--- PAGE 540 ---
§3.3 Densely Packed Spheroids 521
Next we describe the derivation of the quadrupole basis functions. Con-
sider a single small prolate spheroid of semi-axis a in # and ¥ directions
and semi-axis ¢ in 2 direction. The volume of the small prolate spheroid is
Vo = 4ra*c/3 and let the permittivity of the spheroid be €.
For prolate spheroids with ¢ > a, let
fo= Vea (10.3.55)
be the semifocal length. The prolate spheroidal coordinates, £, 7, , are
related to the Cartesian coordinates by
w= foy/(E? —1)(1 — n*) cos (10.3.56)
y= foV(2— IU — 9) sing (10.3.57)
z= fo&n (10.3.58)
Then the five quadrupole solutions to Laplace’s equation are
P2(§)P3(n) exp(2id) = 9(€ — 1)(1 ~ n?) exp(2é6)
9.
= pe —y? + i2ry) (10.3.59)
0
P3(E)P3(n) exp(id) = —9n VE — 1) (1 — 9?) exp(id)
9z
=~ (a + iy) (10.3.60)
fe
PEM@Ps Mn) exp(—id) = ~Fala — w) (10.3.61)
°
Py *(E)P)*(0 216) = g(a? =P = Dien 10.3.62
2 (§)P2 (0) exp(—2i¢) = ap” —y" — xy) (10.3.62)
lowe 9 9
PHEOPE() = 70980? — 31? — 32 + 1)
Barty? 32% 1
=—7 ep TTD 10.3.63
a ta 2 — OOSS)
where Pi" is the associated Legendre polynomial. We can obtain the five
quadrupole basis functions for the potential functions by linear combinations
of &4, bs, Bg, b;, and &g. Let
2
O,= =a? +yjt2- £ (10.3.64)
O5 = —28 (10.3.65)
De = —2y (10.3.66)
1
o;= =3 —y?) (10.3.67)
®g = xy (10.3.68)
--- PAGE 541 ---
522 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
The five electric field quadrupole basis functions are calculated by taking
the negative gradient of the above and then normalizing the basis functions.
We obtain (10.3.49) (10.3.53) in this manner.
The polarization is
Pa =(@- Sa (10.3.69)
for a = 1,2,3,...,8. The polarization P, will induce an internal field
E®),, a =1,2,...,Ny inside the spheroid. They are as follows
Bw = Coa (10.3.70)
a=1,2,...,8, where
( = ©) [& & +1 2 4
4 = SP! inf 2) -1 -1 10.3.71
a © [2 "\e-1 ( - 1) (10.3.7)
—~c,— 1 (#25 G1 fot] 4
Cy = C3 = 3 ( z Je [é 7 In é-1 (10.3.72)
3g & —£\ fl par & +1 :
C= > (@ -1) (#=*) {5 (365 — yn (2t — 3& ¢ (10.3.73)
(GS-1) (a= 2
1s = Cg =~ 2 -1
C5 = Ce 7 — } (2& ~1)
365-2 BE) (Eo41
{e= "3 In é 1 (10.83.74)
24 -
Cr =Cg = - (=>) (@=) &
4 €
3 (ea fot1)\ 36) —5& 7
(ie yin(2*5) - on (10.3.75)
with
1
——— (10.3.76)
We shall illustrate the derivation of Cz and Cs. The rest can be derived in a
similar fashion.
Let the electric field inside the spheroid be
7s |
E= fy=%— = 10.3.77)
fo Via (
The polarization inside the spheroid is
5 &
= (6 — €) = 10.3.78
P=(e-€6) Via (10.3.78)
--- PAGE 542 ---
§3.3 Densely Packed Spheroids 523
To determine the electrostatic solution as a result of polarization of (10.3.78),
we construct solutions based on Legendre functions of the first and sec-
ond kind and spheroidal coordinates €, 7, and @. Let ®j, and ®y,4 be the
scalar potentials inside and outside the spheroid. Both ©;,, and ©,,,; satisfy
Laplace equation. They obey the boundary condition that at the surface of
the spheroid € = &,
Pout = Vin (10.3.79)
2 + ; P
~E* Vout + & + VP in = €- z (10.3.80)
To solve ®;, and ®oue, let
Pin = AV (E2 — 1)(1 = 177) cos (10.3.81)
out = BQNE)P}(n) cos @ (10.3.82)
where P?™(n) is the associated Legendre polynomial and Q’() is the Leg-
endre function of second kind. In (10.3.82)
Pi(n) = V1 — 9 (10.3.83)
Le) = fey |_$&—— 1, (E+! F
Qi) = Ve=1 lz S = 5In ( s (10.3.84)
Applying boundary conditions (10.3.79) and (10.3.82) gives
1 (@—e) fo&[, &-1) (S41
A=z{P— |} 22 |e, — 2 — mn (| 10.3.85
(2) le (ES (10389)
where f, = Vc?—a?. ‘The internal induced electric field is Bing = —Vin.
This gives
<2 =
Byay = Col, (10.3.86)
with C2 and fz as given in (10.3.72) and (10.3.47), respectively.
For the case of f, let the electric field inside the spheroid be
F=f, (10.3.87)
Then
p_ (@-9,,. 5 4
P= SPL” (23 4 23) (10.3.8)
VAs
The potentials ©;, and ®,., are proportional to P3(€)P}(n) cos
and Qh(€)P} (7) cos d respectively, where P7"(€) is Legendre function of the
first kind. Let
Bin = —APPEn(E — DA — 7) cose (10.3.89)
@-2 1
ot =BYe=1 = - Ein (3) 3nV1—7ecosd  (10.3.90)
--- PAGE 543 ---
524 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Applying boundary conditions of (10.3.79) and (10.3.80) gives
1 (€2 —1) (ep—-€ 362-2 36 fo +1
A= def PF (ng? — 1) | Se * — 8 iy f
Fe ES? (4) ty [SP Bene (4
(10.3.91)
Using (16.3.89), we get EO), = —-V;, = Csf, where Cs and f,, are as given
in (10.3.74) and (10.3.50), respectively.

If the particles are closely packed, the near field interactions have large
spatial variations over the size of a spheroid that may induce quadrupole
fields inside the spheroid. However, the non-near field interactions have small
spatial variations over the size of a spheroid and only induce dipole fields
inside the spheroid.

Substituting (10.3.43) into (10.3.42), we get

N N
E(F) = Bine(?) + > Yo ajaitja(F) (10.3.92)
j=la=l
where
Bol) =H? fa oFF Fal) (6r5 ~1)
f
<9 ff ae Val7.7) Fl) (er) 1) (10.898)
IV,
is the electric field induced by the polarization P,(F) of the spheroid j. Of
particular importance is the internal field created by Pj(7) on itself. For this
self term contribution, the second term in (10.3.93) dominates. Because of
the smallness of the spheroid, an electrostatic solution can be sought for the
second term in (10.3.93). We have from (10.3.70), for F in Vj, the self term
becomes
Tal?) © ChoT jal?) (10.3.94)
where j is the particle index, a is the basis function index, and Cjq’s are given
by (10.3.71)-(10.3.75) for cach particle j. In the expressions of (16.3.70)—
(10.3.75), we nced to replace ¢, and & by the value for each particle. An
approximation sign is used in (10.3.94) to indicate the low frequency approx-
imation.
--- PAGE 544 ---
§3.3 Densely Packed Spheroids 525
Next; we apply Galerkin’s method by testing (10.3.92) with fig(¥),
_ _ Ns
a3 = I dF fig(F)- BF) = I dF fig): af ia(F)
4 Me a=
_ NN, _
= | OF Fig(F)- Binelt) + SY aa I oF Fis?) Gol?)
G ah asl ‘
Ny
+ Loan far Fig) trl)
o=l vi
_ _ NON, _
= [© Tis) Biel) +O Y tie fa Fal) Gal)
M 71 a=1 vi
jet
+ agCig (10.3.95)
This gives
1 _ _ NM, _
a9 = ayy | A Fig) Enel) +2 Soe [ Fs) Gal)
(L— Cis) Jy = vi
oat
(10.3.96)
Because of the small spheroid assumption, only the dipole term contributes
to the first term in (10.3.96) which is the polarization induced by the incident
field. Thus
Fm) Bp) = § atig: Eine(F) for 8 =1,2,3 397
I, dF Fig(F) « Bine(F) = { woh ine(Fi) es (10.3.97)
After the coefficients ajg, 1 = 1,2,...,N, and @ = 1,2,..., Ny are solved,
the far field scattered field in the direction (03, @,) is expressed as
_ ye _ N pga
Rp) = pee ah tk PF (a
E.(7) =k (50 + hshs) “L Lee ls -) [ PF)
j=la= a
(10.3.98)
where €,; = ¢j/c. Under the small spheroid assumption, only the dipole fields
will contribute to the far field radiation in (10.3.98). Thus, we have
a elim NON, ae
E,(F) ~ ee (bts + fash) >> > Aja (€rj — 1) voy Fyne? (10.3.99)
j=la=
We next illustrate the results of the numerical simulations by using
N = 2000 spheroids and up to f = 30% by volume fraction. The rela-
tive permittivity used for the spheroids is 3.2 and the size parameter of the
--- PAGE 545 ---
526 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
spheroids used is such that ka = 0.2. At this volume fraction, permittivity,
and size, we did not include the quadrupole effects in the simulations. For
dipole interactions, we replace the integral in the last term of (10.3.93) as
follows.
[2 Fal) Tal) = (ery ~ 1) v0je0k* Fis BHF)“ Fyq (108.100)
Vi
In the simulations, all the spheroids are prolate and are identical in size
with ¢ = ea, where e is the elongation ratio of the prolate spheroid. ‘The size
of the box in which the spheroids are placed is
Nv
V=— (10.3.101)
f
where f is the fractional volume, and v = 47a?c/3 is the volume of one
spheroid.
An incident electric field of
Eiine(®) = ge** (10.3.102)
is launched outo the box containing the N spheroids. The matrix equation
of (10.3.96) is solved by iteration. After the matrix equation is solved, the
scattered field is calculated by (10.3.99). The scattered field is decomposed
into vertical and horizontal polarization
E, = Evats ~ Enchs (10.3.103)
We performed N, = 50 realizations in the numerical illustrations. Let
a be the realization index. Decomposition of the field into coherent and
incoherent scattered fields is also made as in Section 3.2. The incoherent
scattered field is decomposed into vertical and horizontal polarization
Ef = El, + Efnis (10.3.104)
The averaged N-particle bistatic scattering cross sections are
1&
v,N (Os, 8s) = HY EC” (10.3.105)
OT g=1
1s
: -= 7 2 q
on. (Os-0s) = N Do lehol (10.3.106)
For the simulations, the particles are not absorptive. ‘Thus the extinction
rate is the same as the scattering rate. The extinction rate is
1 oft Qn
Ks =Ke= if do, sind, [ dos (ay,.N ~ ohn) (10.3.107)
0 0
--- PAGE 546 ---
§3.3 Densely Packed Spheroids 527
oxo" . — pe
}
st - ° 5 |
al ° |
: ° 4
j i
3 . x
5 Tr 2
3 x
x
1
gh ; |
° 0.08 oa 0.18 02 028 03
fractional volume
Figure 10.3.2 Extinction rate as a function of fractional volume of particles. Relative per-
mittivity of particles ¢, > 3.2. For spheroids ka = 0.2 and ¢ = 1.8. for spheres ka = 0.2. The
dotted curve is for the medium with spheres, the symbol “+” is for the medium with randomly
oriented spheroids. The symbols “o” and “x” are for the medium with aligned spheroids but
with incident: wave being vertically polarized and horizontally polarized, respectively.

In Fig. 10.3.2, we illustrate the extinction coefficients normalized by
the wavenumber k as a function of fractional volume. We consider the case
consisting of aligned prolate spheroids with ka = 0.2 and e = 1.8. In such
a medium, a vertically polarized incident wave with the incident polariza-
tion aligned with the symmetry axis of the prolate spheroids has a higher
extinction rate than that of the horizontally polarized incident wave. ‘The ex-
tinction rate is polarization dependent. In the same figure, we also show the
extinction rate for the case when the spheroids are randomly oriented. For
random orientation, the probability density function of orientation p(3, a) is

sin 3
(3,a) = —— 10.3.108
»(3,a) = ( )
for0<8<7,and0<a< 2z,

The result of the attenuation for the randomly oriented case is between
those of vertically and horizontally polarized incidence of the aligned case.
The extinction rates are also compared with those of a medium with spher-
ical particles of ka = 0.2 and e = 1. The spherical case predicts a smaller
attenuation than the spheroidal case, even though the medium has the same
fractional volume. Figure 10.3.3 shows the extinction rates as a function
--- PAGE 547 ---
528 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
ox . fo
pos °
|
5 °
5 °
8 4]
3
35) © j
i
3: °
25}
! Jo
or a CT!
elongation (c/a)
Figure 10.3.3 Extinction rate as a function of elongation ratio of spheroids. The spheroids
are randomly oriented. For spheroids ka = 0.2 and fractional volume f = 20%
of particle elongation for a medium with randomly oriented spheroids, The
size parameter is ka = 0.2 and fractional volume f = 20%. It shows that
the spheroid with longer elongation ratio predicts a larger attenuation due
to its larger particle volume.

Next we illustrate the scattering phase matrices. The phase matrices
are bistatic scattering cross sections per unit volume of a conglomeration
of particles. We consider the incident wave and polarization as given by
(10.3.102). The spheroids are randomly oriented in the following illustrations.
We also compare with the results of independent scattering. ‘he independent
scattering results are obtained by including only the first term inside the
curly bracket of (10.3.96). That is

1 = =
ag =—— |] FF fig(?)- Binc(® 10.3.109
19 = Gaey I, Fo) Boel) (10.8.109)

We represent the phase matrix by using the (k, 1, 2) orthogonal system
for polarization as treated in Section 1.2 of Chapter 1 of Volume I. We
consider the incident wave as given by (10.3.102) with k; = 2 and incident
polarization é; = 9.

Case (a): ds = 0° and ds = 180° For ¢, = 0°,
hk, =sin 0,4 +.c0s0.3; 9, = cos0,@—sind,3; he =%
Then
1, = t= (he x ki)/|he x iJ = = hy 2, = hy x1, = 0,
--- PAGE 548 ---
§3.3 Densely Packed Spheroids 529
Thus the incident wave with @; = g is of polarization 1;. Similar polarization
vector formulas can be obtained for ¢, = 180°. Hence we define the phase
matrix elements as

Pii(6s) = AX (10.3.110)

Onn

PaO) = (10.3.111)
The quantities Pj,(@,) and Px(6s) correspond to co-polarization and cross-
polarization, respectively. In Figs. 10.3.4a and 10.3.4, we plot Py; and Por,
respectively, as a function of scattering angle for scattering angle between
O° and 360°. We give the results of ¢, = 0° and @, = 180° in the same
figure. The following definition is used. For ¢, = 0°, we have scattering
angle between 0° and 180° and the scattering angle is equal to 0, with
0 < 4, < 180°. For 4, = 180°, the scattering angle is equal to 360°—6, with
0 < @, < 180°, covering the range of scattering angles between 180° and
360°.
Case (b): @s = 90° and ¢, = 270°. For ¢. = 90°,

ky = sin Os + c08952; i, = cos0, —sin0.2; hy = —&
Then
iy = is = (hy x bi)/|he X bi] = 8 = he
Rak xt=h %=kxi= a
‘Thus the incident wave with @; = @ is of polarization 2;. Similar polarization
vector formulas can be obtained for 6, = 270°. Hence we define the phase
matrix elements as
The N

P20.) = (10.3.112)

Pan(0,) = TX (10.3.113)
The quantities P22(,) and Pj2(8,) correspond to co-polarization and cross-
polarization, respectively. In Figs. 10.3.4c and 10.3.4d, we plot Piz and P2,»,
respectively, as a function of scattering angle. The scattering angle is between
0° and 360°. The following definition is used. For ¢, = 90°, we have the
scattering angle between 0° and 180°. The scattering angle is equal to 5.
For ¢s = 270°, the scattering angle is equal to 360°—@, with 0 < 4, < 180°,
covering the range of scattering angles between 180° and 360°.

In Fig. 10.3.4, we show the results of Pi1, Poi, Piz, and P22 for the

fractional volume of 10%. The results of independent scattering are also
shown for comparison. The unit is such that wavelength is equal to unity.
--- PAGE 549 ---
530 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
x10*
5 —-_—_—
°
°
= 2, g008829°8 on
EL © Poooe 042922, 400,
it o °
°
0 50 100 150 200 250 300 350
‘scattering angle (degree)
fa)
5x08
45) 0°0 °
°
‘ ° °o ° ° ° °
Bes ° ego 0 9°
3 2% ° ° Po
° 6 ° °
2st o °
2
a a a a
scattering angie (deere)
(b)
Pes 10"
45 °°
4 00°” o ° 2500
. of 6 °
2555 9 50° 508 8 ° °
ato °o oo °
2s °
2
rr
scattering ange (door)
()
aud
x x * x x
wt x x 0% * x
& x xo x x
2 ° °
00% Xo o.*% Xoo
1 ox xo Pox Ko
° x °
° 25 nd Suond?
rr a)
scattering ange (Sesree)
(d)
Figure 10.3.4 Phase matrix as a function of scattering angle for ka = 0.2, fractional volume
f = 10%, clongation ratio e — 1.8, relative permittivity of particles ¢ = 3.2. The spheroids
are randomly oriented. In the simulations, N = 2000 particles are used and the results are
averaged over N, = 50 realizations. (a) P11, (b) Por. (c) Piz, and (d) P22. The syinbol
“o” represents the dense medium results, and the symbol “x” represents the independent
scattering results.
--- PAGE 550 ---
§3.3 Densely Packed Spheroids 531
x10"
15
9000200290000 0000000020 2003 2 20
1
=
os|
° 00900°°0 ° °
902000000 0 00°09509°00006
gbooe Load
0 50 i ae i nS)
scattering angle (degree)
@
25e 10 —— TO
0°
2 0°"
000 ooo
00° ° ° 4°
Fisk?ooo ° ° o0°
a 00 250° oo
1 °°
9000000020200 OO I I
oO 50 100 150 200 250 300 ~ 350
scattering angle (degree)
)
10°
5X0 ——
eo
2 ° ° °
°
0 0°0 0%, of oe °
Sist °° ° ° ° ° ° °
= °
= 0 265° oa
1
2000 OOO LI IKK I IK OE
° 50 100 150 200 250 300 350
scattering angie (degree)
)
ist ‘0
x x « x
atx x x x
aw x x x x
EY x x x x |
as x x x x
x x x x
0009°%%
90 000% ¥o00° Sox Xg0000
0 30 "00 ~«ts0~=~=~«wSCHSSCOSCSC«C
scattering angle (degree)
@
Figure 10.3.5 Phase matrix as a function of scattering angle for ka — 0.2, fractional volume
f = 30%, clongation ratio e — 1.8, relative permittivity of particles ¢- = 3.2. The spheroids
are randomly oriented. In the simulations, N = 2000 particles are used and the results are
averaged over N, = 50 realizations. (a) Pi1, (b) Pei, (c) Pia, and (d) P22. The symbol
“o" represents the dense medium results, and the symbol “x” represents the independent
scattering results.
--- PAGE 551 ---
532 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
Piy(dense) | P21(dense) | Py1(indep) | Poi (indep)
f Pix{indep) | Pii(dense) | Pi1{indep)
Pii(dense) | Poi(dense) | P2\(indep)
3.67 15.80 178.08

Table 10.3.1 Values of phase matrix for various fractional volumes. The elements depend.
on scattering angles. The maximum values are tabulated.
‘The dimension of phase matrix is inverse of distance. We note that the co-
polarization, Pj; and P22, are smaller than those of independent scattering,
while the cross-polarization, P2; and Pj, are higher than those of indepen-
dent scattering. We also note that the simulation results fluctuate because
of random phase situation while that of independent scattering are smooth
curves. We also note that P22 has angular dependence that is the character-
istic of Rayleigh scattering.

In Fig. 10.3.5, we show the corresponding results for a higher fractional
volume of 30%. In this case, the co-polarization of Pj; and P22 become much
lower than those of independent scattering, while cross-polarization Pz; and
Pig ave uch higher than those of independent scattering. To compare the
result quantitatively, we tabulate the values of P,; and P2; in Table 10.3.1.
The values are dependent on scattering angles. We tabulate the maximum
values only. We also list the results for those of fractional volume of 20%.
We note that the ratio of co-polarization of independent scattering to that
of dense media scattering increases from 1.25 to 3.67 from fractional vol-
ume of 10% to 30%. This means that independent scattering significantly
overestimates the total amount of scattering at high fractional volume for
non-sticky particles. The cross-polarization is a small fraction of the total
scattering. However, it has the opposite trend. The ratio of cross-polarization.
to co-polarization stays around 178 for independent scattering. However, the
ratio decreases from 68.5 to 15.8 when fractional volume increases from 10%
to 30%. Compared with 178, the ratio of 15.8 is ten times less, meaning that
the ratio of cross-polarization to co-polarization for dense media can be ten
times different from that of independent scattering.
--- PAGE 552 ---
§4 Numerical Simulations Using T-Matrix Formalism 533
4 Numerical Simulations Using T-Matrix Formalism

> **第4节：使用T矩阵形式化的数值模拟**

4.1 Multiple Scattering Equations

> **4.1 多次散射方程**

In this section, we use the multiple scattering equations based on the T-
inatrix formalism. Consider N spherical scatterers bounded by surfaces $1,
S,..., Sy (Fig. 10.4.1) occupying regions Vj, V2,...,Viv. The scatterers are
centered at 7,72,...,7N and have radii a), a2, ..., ay, respectively. Let
the background region be denoted by V,. The ith scatterer has permittivity
equal to ¢;, wavenumber k;, and permeability 4. Consider an incident field
expressed in terms of vector spherical wave functions

BF) = YD [alt Ronn kr, 8,6) + 088) RgNmn(kr56,8)| (104.1)

myn
The Foldy-Lax equations are of the following form
N
per pine | B jer 7
Ey =E™ +G, 9 TE; (10.4.2)
yt

The interpretation is that the field exciting particle | is the sum of the
incident ficld and scattered field from all particles j except particle 1. The
term GoT'jE;" is the field exciting particle j that is scattered by particle j
and then propagates to particle J.

Let 7 be in the vicinity of particle J. ‘The exciting field of particle J is

EL) = So [wQQO Renn kT) + whBP Ryn (KFA) (10.4.3)

mn
where widO and wr) © are unknown exciting field coefficients to be de-
termined.
&) CG)
G) .
&) C)

Figure 10.4.1 Particles 1,2,...,.N occupying regions Vj, V2,..., Viv and bounded by sur-
faces S1,S2,...,Sy, respectively.
--- PAGE 553 ---
534 10 DENSE MEDIA MODELS AND ‘THREE-DIMENSIONAL SIMULATIONS
For F in the vicinity of particle j, the exciting field of particle j is
B=) [w{80 RoMran( 775) + WhO RGN mn KF) | (10.4.4)

mn

The particle j will scatter EY and give rise to outgoing vector spherical

waves. The scattered wave by particle j is
ESF) = [ww QPOTE NT an (WTF) + WY OTL OW pan KF]

mn
(10.4.5)

where ris) and Th) are T-matrix elements of spheres as given in (2.8.46)-

(2.8.47) of Chapter 2, Volume I. Putting (10.4.5) and (10.4.1) in (10.4.2), we

have for |F —F|2a,,

Slt Ra aa AFM) + LN RON nn
mn
= So [alt RoW, (kr) + a RoN w(K]
7
N
+ OY [uronrom, 6G) + OOM (krFH)] 10.46)
j=l pv
jAl
Tn order to balance coefficients in (10.4.6), we make the transformation of
the vector spherical waves so that the spherical waves are all centered at 7).
The translational addition theorem for vector spherical waves can be
expressed as follows. Consider the triangle with vectors Fo, 7, and 7 forming
the three sides. The vector spherical wave centered at O can be expressed
in terms of linear combinations of vector spherical waves at O! (Fig. 10.4.2).
Note that in Fig. 10.4.2,
FaToth (10.4.7)
Then the translation addition theorem is [Cruzan, 1961, 1962]
Rg Mn (BP) = {RGA pan KF) ROM py (KF")
vi
+ RgByumn (Fo) RGN ARF) } (10.4.8)
RgN mn (iP) = So {Ro Burin Fo) ROM (KP)
up
+ Ro Apa KFo) RGN w(K") } (10.4.9)
--- PAGE 554 ---
§4.1 Multiple Scattering Equations 535
= Pr
7
on
To
10)
Figure 10.4.2 Translational addition theorem for vector spherical waves. Three vectors
F, 7, and 7, form a triangle.
and for rp > r"
Mann RP) = SD {Apunen Fo) ROM a (BT) + Byrn Ko) RON uo KP) }
up
(10.4.10)
Naan(bt) = Y7 { Burman io) RGM BH KE) + Aporn(RFe) RGN pe RF}
vy
(10.4.11)
where
Ajwmnn(kFo)
— Tmn(_jye f bp yim
= Tm (Ay Talons] — p,ip)aln, x, p)hig( bro) ¥e"" (Boro)
Yuu >
(10.4.12)
Bywran(kFo)
= TAS afm. nl — pe ulp.p ~ 1)0(02, 7p) kr o)¥p" "(Bos bo)
Yaw 7
(10.4.13)
and mn is defined in Eq. (1.4.59) of Chapter 1, Volume I. The expressions
RgAjwmalkFo) and RgByynn(kFo) are respectively those in (10.4.12) and.
(10.4.13) with h,(kFo) replaced by jp(kF). In (10.4.12) and (10.4.13)
/2
+m)\(v + p)\(p —m — p)!]"
,v|p) = (-1)™# (2p +1 (n+ mv + w)Mp — m — pw)!
am, nly vip) = (Tp + Ag Sn) — wpm + po)!
(nv P nov p ;
( E “tnew) ( 0 5) (104.14)
--- PAGE 555 ---
536 10 DENSE MEDIA MODELS AND ‘THREE-DIMENSIONAL SIMULATIONS
aden, nyeulp. 9g) = (<1)™%(ap-4 1) [EMILY + Hem — wt”
Ma Ms VIP, a) = P (n—m)\(v — pp +m +p)
[mv p nov gq
(r ” ons) ( 0 ’) (10.4.15)
quontp
ans?) = Sap [anv +1)(Qv +1) + (v +1)(n+v~p)
‘(n+p—vtl)—v(nt+vtpt2avtp—nt | “(10.4.16)
2 1
b(n,v, p) = oer [(n +u+p+li(v+p—n)
1/2
(n+p-v(ntyv—p+)) (10.4.17)
and
ho je Js
( mz —(m, oo) (10.4.18)
are the Wigner 3 symbols [Edmonds, 1957]. We note the following:

(1) The m index consists of m = 0,+1,+2,...,+n and p index consists of
p= 0,41,+2,..., 4».

(2) Ayn, Buvmn may not be of the same dimension as Minn and Nin:
For example, we may truncate Mjan and Ny, at a multipole order of
n= Ny. However, for Ajymn and Byymn, the summations of (10.4.8)—
(10.4.11), we may need to sum over v = 1, 2,..., to beyond Ny; to have
sufficient accuracy. This means Ayymn and Byuymn can be non-square
matrices.

(3) For the Wigner 3j symbols in (10.4.18),

m =0,+1,...,+)1
mg =0,4+1,...,+J2
Also j3 is bounded by
li — del Sis SA + je (10.4.19)
The symmetry relations for Wigner 37 symbols are, for even permuta-
tions,
hook B\)VL(k b A\N_(b A kh
my, M2 M3 m2 m3 m4 m3 mm, mg
(10.4.20a)
--- PAGE 556 ---
§4.1 Multiple Scattering Equations 537
and for odd permutations
koh B\V_(h b BR) (hb hk oh
m2 my m3 my m3 me m3 m2 my,
a(-1ytirn (Bs (10.4.206)
my, m2 m3
(4) In view of (10.4.20a) and (10.4.208),
nov Pp nov p
m p —(m+p) 000
is only nonzero for
p= |n-vl,|n—v|+2,|n—vj/+4,....n+v (10.4.21a)
and
nov Pp nv p-l
m po —(m+ ys) 00 0
is only nonzero for
p=|n-v|+1,|Jn—v|+3,....nt+yv-1 (10.4.216)
Equations (10.4.21a) and (10.4.21b) can be applied to the summations
in (10.4.19) and (10.4.20), respectively.
Next we apply the translation theorem to (10.4.6). Note that
el ee ee ee te ee ee (10.4.22)
and
pri < br (10.4.23)
Also ¥ = 77} +7). We have on using translation addition theorem in (10.4.6),
YF [e82© Ra an kIT) + WNP RaW omn (KFD)] =
mn
Dy {aap [RoArnnyu( Ta) Ronn (kF7]) + R9Brnnpu( KF) RGN nn (r7)|
pv mn
+ of [Rg bronge (7) Ron (RFF) + Ro Army BF) RON u(r] }
--- PAGE 557 ---
538 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
N :
+eEey {wjanerngsne) [Anns ( FTG) ROM (RT)
j=l av mn
SAL
+ Brung RVRGN ran (kITD)] + {OTN
- [Brno RTIG) Rg Mran RPT) + Amnyar RTGS) RGN ran (KFT) | } (10.4.24)
Balancing the coefficients of RgMmn(k77) and RgNmn(kT77), we obtain
WO = J [RoAmmulRFall? + RoBrnuu( bras) |
jw
N
$Y [Anne CarIAG) TYING wh)
jl ww
A
+ Brine RAAT wi] (10.4.25a)
WMO = ST [RoBrnywAKR)GLLY + RAAT) AY |
we
N
+ OY [Branue WFAGTEMP WAP
j=l w
jAl
+ Annu kD wa] (10.4.258)
Equations (10.4.25a) (10.4.25b) can be conveniently put in matrix form.
Let A and B represent respectively Amnw aud Brnyy, and the matrices
are of dimension Lmax X Lax, using the notation from Table 2.7.1 in Chap-
ter 2 of Volume I. Also let TQ) represent TP Note that T™ is of
dimension Lmax * Lmax- Also let column vectors @#) and a) represent
who and af) etc, These column vectors are of dimension Lmax X 1. Then
we have
DONO = RgA(kr)a™) + RoB(Rr a)
N
+> [Ager TEP WAn” + BOTTOM] (10.4.262)
jal
jAl
--- PAGE 558 ---
§4.1 Multiple Scattering Equations 539
WMO = RgB(kra™) + RgA(kr)a®)
N
4 1 [Barm)TEdD MEA + AGATA TOO DMA) (10.4.26b)
=1
jv
Let
_ a)
Fine = | ZN) (10.4.27)
be of dimension 22inax x 1,
_ A(kr) Blkr
3 (kr) = [30° a) (10.4.28)
B(kF) A(kF)
be of dimension 2L£max X 2Lmax, and

a_[T’ _o A

T= 0 TT!) (10.4.29)
be of dimension 2Lmax X 2Lmax- Then, the multiple scattering equations of
(10.4.26a) and (10.4.26b) can be expressed in compact matrix form.

N
BO = SP Fer TATOO + KgF(kF Jane (10.4.30)
=1
Hl
for 1=1,2,...,.N.
After the coefficients 77'9)’s are solved, then the scattered wave is given
by
N
Br) => > {E aS OM man (KIT) + cE hr} (10.4.31)
j=l Umn
Let 9) be a 2Linax X 1 column matrix defined by

3; aS(M)(A)

750) = [Fore (10.4.32)
and a0) and GG) are Emax X 1 matrices representing ai”) and
a) Prom (10.4.5), the scattered field coefficients 7°) satisfy the rela-
tion

a) = TOG” (10.4.33)
Hence, once the exciting field coefficients @) are solved from (10.4.30),
the coefficients of the scattered field are calculated by (10.4.33). The final
scattered field is then calculated via (10.4.31).
--- PAGE 559 ---
540 10 DENSE MEDIA MODELS AND ‘THREE-DIMENSIONAL SIMULATIONS
For the case of plane wave incidence, we can further simplify (10.4.30).
Consider an incident wave with k; = sin 6; cos 6;% + sin 6; sin d;4 + cos 4,2.
Let.
Ep) = Heike?
= [a8 RoMnlkr) + aSPRGNan(kr)] (10.4.8)
nn
Given polarization vector A, af) and al) can be calculated readily. We
note that E’“(F) can be written in the following alternate form
E™(@) = etki MA eike (FH)
= ETS [aD Rg Mmm RTT) +a RGN an(kTA)] (104.35)
nm
Hence e* Fg) and ef Fa) are the contributions of the incident wave
to the exciting field coefficients whdO and why) respectively of particle l.
Thus
RgG(kT1)Bine = CT Fine (10.4.36)
and we have the following simplified form of the multiple scattering equations
for plane wave incidence
N
BO = SOF kr)TOD + eine (10.4.37)
mi
for 1 = 1,2,...,N. After the exciting field coefficients are calculated. The
scattered field is calculated by (10.431). Let @) be a 2Lmax x 1 column
matrix defined by
BMA)
as a 4
as) = [Fswnc | (10.4.38)
and @()0) and @)G) are Imax X 1 matrices representing a) and
al )0)_ The scattered field coefficients 75) satisfy the relation
WO) =F GO (10.4.39)
The final scattered field in the far field is
as _ elke MA oon s(N)B —
BS = Yan [aC nO)" + 087 B (8.00)
mn
(10.4.40)
in the observation direction of k, = sin 4, cos d.% + sin 6, sin def + cos O52.
--- PAGE 560 ---
§4.2 Computational Considerations 541
4,2 Computational Considerations
In implementing the numerical simulation of scattering, several items have
to be computed. We consider their computations in the following.
Wigner 3j Symbols
The Wigner 3j symbols are related to the Clebsch-Gordan coefficients by
A ja 9 ~jo-mso; hy. at
(i me i) = (125 + 1) 8 Gajamame | jrj2j(—m))
(10.4.41)
where (jijgmime | jij2j,(—m)) are the Clebsch-Gordan coefficients [Ed-
monds, 1957; Abramowitz and Stegun, 1964]. It is given by the following
formula,
(tijemame | jrjed,(—m))
4h -p)iGtioplG+ pop )MQ LI
= 5(mymy + mq) | BABIN + j= NMG + jo = HMI + VY
G+51+J2+1)!
: ye (-LE Gi + mi)! — mi)!G2 + ma)!G2 — ma)IG +m)! — m)!
E Rj + jo — 5 — k)M(G1 — mi — k) (Jo + m2 — k)!
1 ) (10.4.42)
(j = ja + my + k)N(G — jx — mp +k)! _
with 5(i,k) = 6 being the Kronecker delta. Thus
( a J ) =0 (10.4.4)
my mo m
if m # —(m) + mz). The values of j are within the range
ln —je) SI SHA+32 (0.4.44)
Also
m = 0,41, 42,...,441 (10.4.45a)
mg = 0,+1,4£2,...,4J2 (10.4.45b)
In the summation over k in (10.4.42), the summation is over integers of k such.
that none of the factorial is negative. Note 1! = 1, 0! = 1, (—1)! = undefined.
Thus summation over k in (10.4.42) is k = 0,1,... such that none of the
factorial is negative. This means for a given ji, j2, ™1, m2, j, m, there are
only a finite number of terms in the summation.
--- PAGE 561 ---
542 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
To prevent the factorial to acquire too large an integer value, it is com-
putationally advantageous to work with the logarithm of factorial. Thus let
Aa, | Gt d= ING +A = JaG + Je = IAI FV
G+tAtie2+!
x V (jr + mai)'(ji ~ m1)!
x VGa+ maya = mag +myG =m)! (10.4.46)
A, = log A
= 5 [los (Gin + ia = 3)! +108 (Gj +1 — a)!) +J08 (Gi + Ja — ))
+ log(27 + 1) + log (ji + mi)!) + log (Gi — m1)!) + log ((j2 + m2)!)
+ log ((j2 — ma)!) + log (Gj + m)!) + log (7 — m)!)
~ log (+ Ji + do + Y))] (10.4.47)
po
EG + jo —7 — Bi — m — kya + ma — fi)!
1
TT 10.4.48
(j — jo + my + k)!(j ~ ji ~ me + ky! ( )
By =logB
=~ [log (it!) + log ((jr + ja - 9 - BY
+ log ((j1 — m1 — k)!) + log ((j2 + ma — k)!)
+ log ((j — jo + ma + k)!) + log ((j — jf — ma + *))] (10.4.49)
Thus we calculate A; and B, instead of A and B.
The Clebsch-Gordan coefficient is
(infamy | jijajm) = dmmtme™ Y(-1ke™ (10.4.50)
k
Computation of T-Matrix Coefficients
We need to compute jn(«) and yn(«). The recurrence relations are, for in-
creasing orders
. 2n+1). .
Inga(x) = Gat) (2) = jn—1(2) (10.4.51)
2n+1
vnsa(a) = PPFD (2) — yyi(a) (10.4.52)
--- PAGE 562 ---
§4.2 Computational Considerations 543
The lowest two orders are
jola) = = (10.4.53)
. sing cosa
Ale) = - (10.4.54)
yo(r) = — = (10.4.55)
cosx sing
yi(z) = ——- - — 10.4.56
n(z) = -S2 - (10.4.56)
Using initial values of (10.4.53)-(10.4.56), the values of higher order spheri-
cal Bessel and Neumann functions can be calculated by (10.4.51)-(10.4.52).
However, for small argument «, the recurrence relation of (10.4.51) for spher-
ical bessel functions may not provide numerically accurate values as higher
order spherical Bessel functions have smaller and smaller values. For this case
we can use the backward recurrence formula for spherical Bessel functions.
. 2n+1). .
jn(a) = PP*D 52) — jn ale) (104.57)
For smaller argument and a higher order n,
gn
ji a 10.4.58)
In) = TSS One) (10.4.58)
Thus one start with high order values of bessel function and use (10.4.57) to
work backward to j;() and jo(x).
Computation of Vector Spherical Harmonics and Vector Spherical Wave
Functions
We need to compute associated Legendre polynomials defined by sin @ and
derivatives of associated Legendre polynomials. We define #7" and s7* func-
tions
Pi" (cos@
(cos 9) = V/2an(n+ Trina eles) (10.4.59)
sin
- dP™(cos 8
s™ (cos) = Bankr + Lynn (cos ) (10.4.60)
To compute {7 and s{" for n > 1, we use the following recurrence relations
. m+. 2m +3\V? .
#eti(cos@) = —sind (=) (3) U™ (cos) (10.4.61)
#" (cos) = /2m + 3 cosGt" (cos 4) (10.4.62)
--- PAGE 563 ---
544 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
, In+1 (n=1)2 —m2\'?
(0) = \a-m [v2n —Irt™ (x) — aS te a(2)]
(10.4.63)
for n > m+ 2. The recurrence relation can be initialized by
t}(cos 0) = —V3/2 (10.4.64)
and compute #3, #3, ... by using (10.4.61). Then we compute th, #3, ... by
using (10.4.62). Also
t°(cos@) =0 (10.4.65)
We then use (10.4.63) to compute #7” for increasing n.
The computation of the s7'(cos@) function can be carried out by using
the following relations.
(i) For m > 0:
sm (cos 4) = cos 647" (cos @) (10.4.66)
5 2 2) 1/2
ms"(cos 0) = n.cos 6t(cos 4) — t% ;(cos8) (eee =) .
(n>m+1) (10.4.67)
(ii) For m = 0:
cos 6 p n Qn + 1\'/?
8° (cos) = qo ~1)'/7s°_)(cos@) — noi (F445) s9_4(cos @)
(10.4.68)
The computation is initialized by the relations
sh(cos 4) =0 (10.4.69)
s{(cos 0) = —\/3/2sind (0.4.70)
To calculate f° and sf" for negative m, we can use the relations
t,(cos 0) = (—1)™*!#" (cos) (10.4.71)
8;,""(cos 0) = (—1)™s?"(cos 0) (10.4.72)
Thus, to set up a computer code, we first decide on a maximum value of
n equal to Nyax and initialize the values by using (10.4.64) and (10.4.65).
Next the values of ¢7) and t7,, for m = 1,2,...,Nmax are calculated by
(10.4.61) and (10.4.62). The values for negative degrees m are obtained by
using (10.4.71). The values of the functions s7" for m > 0 are obtained from
the #7" values by (10.4.66) and (10.4.67). The function s° is computed by
using the recurrence relation of (10.4.68) which is initialized by (10.4.69) and
(10.4.70). Negative degrees of s7" are calculated by using (10.4.72).
--- PAGE 564 ---
§4.3 Results and Comparisons 545
— (0.45
S 0.40
$ —
& 035
= 030
0.25
2 020 —— __2000,4th
= ———— -2000,6th
Fd
ets seamen 4000,4th
zoo soosereseer  4000,6th
E 0.05
& 0.00
0 2 4 6 8 10 12 14 16 18 20
number of realizations
Figure 10.4.3 Convergence of extinction rate versus number of realizations and number
of iterations for fractional volume f = 15% and N = 2000 and 4000. The extinction rate is
normalized to the independent scattering case. Other parameters are ¢y = 3.2€9 and ka = 0.2.
= (0.25
e lessees pesconamersvnresstg’ |
sg Festa ae oer
0.20 i
£ a
Sosy ff
¢ if —— _ 2000,6tn
£ o104 | ——— 2000,9th
g j seseemeeneee — 4000,61h
= 0054 | sreemeeeees  4000,9th
£
S 0.00
0 2 4 6 & 10 12 14 16 18 20
number of realizations
Figure 10.4.4 Convergence of extinction rate versus number of realizations and number:
of iterations for fractional volume f = 25% and N = 2000 and 4000. The extinction rate is
normalized to the independent scattering case. Other parameters are ¢, = 3.2¢> and ka = 0.2.
4.3 Results and Comparisons with Analytic Theory

> **4.3 结果与解析理论比较**

We solve (1.4.37) by iterations. In this section we present results for diclec-
tric spheres of permittivity €, = 3.2e,. In Fig. 10.4.3 we show the results
Of Ke/(te)ind at a fractional volume of 15% as a function of realization by
using 4 and 6 iterations. We note that for 2000 spheres there is practically
no difference between 4 and 6 iterations. For 4000 spheres, the results of 4
and 6 iterations are practically identical. This demonstrates numerically the
convergence with iterations for the simulated extinction rate. The results in
--- PAGE 565 ---
546 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
8,000-4 =
7.00e-4 a
6.000-4 independent ————_y,
= Monte Caro a Lo Sal
= 5.00e-4 “
3 wie Foldy
% 4.000-4 ee
z 3.000-4 Le QcA-cP-PY
* 2.006-4 4
ower ~ ecapy-——™ —
0.00840
0 5 10 16 20 26 30
fractional volume (in %)
Figure 10.4.5 Extinction rate normalized to the free-space wave number as a function
of the fractional volume of scatterers. The plots show calculations based on independent,
scattering, Foldy’s formula, QCA-PY, QCA-CP-PY, and Monte Carlo simulations. Other
parameters are ¢y = 3.2€, and ka = 0.2.
I Method 15% 25%
Monte Carlo o74s | 038! | 0.224
4000 spheres (4th)* (6th) (9th)
Monte Carlo 0.732 | 0.398 0.2138 |
2000 spheres (4th) (6th) (9th)
Independent scattering | 1 | 1 | 1 |
Foldy 0.969 0.915 0.870
QCA PY 0.674 0.318 0.150 |
QCA CP PY 0.732 0.402} 0.215
Table 10.4.1 Numerical values of the ratio ke/(#e ina. ("Phe numbers in parentheses below
the Monte Carlo values denote the numbers of iterations used.)
Fig. 10.4.3 also demonstrate convergence with the number of realizations.
However, there is a small difference between the results with 2000 and 4000
spheres. The small difference can be attributed to the difference in the num-
ber of spheres that lie close to the edge of the cubic box in the cases of 2000
and 4000 spheres. The case of 25% is shown in Fig. 10.4.4 with 6 and 9
iterations, In Fig. 10.4.5 we compare the simulated results of 5% (30 realiza-
tions), 15% (20 realizations), and 25% (20 realizations) with analytic approx-
imatious of independent scattering, Foldy’s approximation, QCA-PY, and
QCA-CP-PY. We plot K-/k as a function of fractional volume f. We note
that independent scattering predicts a linear increase with fractional volume,
while Foldy’s approximation predicts a monotonic increase with fractional
--- PAGE 566 ---
§4.4 Simulation of Absorption Coefficient 547
volume at a slower rate than that of independent scattering. The QCA~-PY
and the QCA CP--PY predict saturation and a decrease with further in-
crease of fractional voluine and are in good agreement with the simulations.
Note that these simulations are for hard spheres without interparticle force.
The results are tabulated in Table 10.4.1.
4.4 Simulation of Absorption Coefficient

> **4.4 吸收系数的模拟**

For particles with absorption, the absorption coefficient can also be simu-
lated. Upon solving the Foldy-Lax multiple scattering equations of (10.4.37),
we obtain the coefficients w4 and wi) which gives the final exciting
ficld of particle 1. The power absorbed by particle / is then, from (2.8.84) in
# Tsang《Scattering of EM Waves》Chapter 10

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 2 of Volume I,

> **第十章：稠密介质辐射传输**。研究稠密随机介质的辐射传输理论，包括有效介电常数模型、散射衰减和相干传播常数、相干反射与非相干散射、简单DMRT理论、体积分方程模拟、以及基于T矩阵形式化的数值模拟。**

1 9
r(l A M op
wi = — 1 {uit eererstn 4+ ryan)
We tam
+ wMOP REVO + PMO Py} (10.4.73)
‘The power absorbed by N particles is
N
Wan = Sow? (10.4.74)
1=1
The absorption coefficient is equal to the absorption cross section per unit
volume of space. Let S; be the incident wave Poynting vector. Then
1 =
Ka = Sv Wan (10.4.75)
is the absorption cross section per unit volume of space. In (10.4.75), V is
the total volume in which the sample of spheres is placed. For plane wave
with unit magnitude of electric field, $; = 1/(27). Then we have
N
i A pM) 1 2
re = — pes OT Lola Pner 0 + (re)
1=1 mn
+ WO PRETLMO + EMOPy} (10.4.76)
Simulations by particles continue to be an important problem [Tsang et
al. 1992; Zurk et al. 1995; Siqueira and Sarabandi, 2000]. Other computa-
tion methods used included the recursive T-matrix method {Lu et al. 1995;
Chew et al. 1990], the discrete dipole approximation (DDA) [Purcell and
Pennypacker, 1973; Draine and Flatau, 1994] discussed in Chapter 2, and
the finite-difference time-domain (FDTD) method [Karkkainen et al. 2000].
--- PAGE 567 ---
548 10 DENSE MEDIA MODELS AND THREE-DIMENSIONAL SIMULATIONS
REFERENCES AND ADDITIONAL READINGS
Abramowitz, M. and J. A. Stegun (1964), Handbook of Mathematical Functions, Dover Pub-

lications, New York.

Chew, W. C. (1990), Waves and Fields in Inhomogeneous Media, Van Nostrand Reinhold,
New York.

Chew, W. C., J. A. Friedrich, and R. Geiger (1990), A multiple scattering solution for the
effective permittivity of a sphere mixture, IEEE Trans. Geosci. Remote Sens., 28(2),
207-214.

Cruzan, O. R. (1961), Translational addition theorems for spherical vector wave functions,
TR-906, Diamond Ordinance Fuse Laboratories, Department of the Army, Washington
be.

Cruzan, O. R. (1962), ‘lranslational addition theorems for spherical vector wave functions,
Quart. J. Appl. Math., 20, 33-40.

Draine, B. T. and P. J. Flatau (1994), Discrete-dipole approximation for scattering caloula-
tions, J. Opt. Soc. Am. A, 11, 1491-1499.

Edmonds, A. R. (1957), Angular Momentum in Quantum Mechanics, Princeton University,
Princeton, NJ.

Ishimaru, A. and Y. Kuga (1982), Attenuation constant of a coherent field in a dense distri-
bution of particles, J. Opt. Soc. Am., 72, 1317-1320.

Karkkainen, K. K., A. H. Sihvola, and K. L Nikoskinen (2000), Effective permittivity of
mixtures: numerical validation by the FDTD method, IEEH Trans. Geosci. Remote
Sens., 38(3), 1303-1308

Lu, C. C., W. C. Chew, and L. Tsang (1995), The application of reewrsive aggregate T-mmatrix
algorithm in the Monte Carlo simulations of the extinction rate of random distribution
of particles, Radio Sci., 30(1), 25-28.

Mandt, C. (1992), Multiple scattering in random meda: Backscattering enhancement in a
sparse distribution of large scatterers and Monte Carlo simulations of the extinction
rate in dense media, University of Washington, Seattle.

Mandt, C., Y. Kuga, L. ‘Tsang, and A. Ishimaru (1992), Microwave propagation and seat-
tering in a dense distribution of spherical particles: experiment and theory, Waves in
Random Media, 2(3), 225-234.

Metropolis, N., A. W. Rosenbluth, N. Rosenbluth, A. H. ‘Teller, and E. ‘Teller (1953), Equation
of state calculation by fast computing machines, J. Chem. Phys., 21(6), 1087-1092.

Peterson, B. and S. Strom (1973), T matrix for electromagnetic scattering from an arbitrary
number of scatterers and representation of E(3), Phys. Rev. D, 8, 3661-3678.

Purcell, E. M. and C. R. Pennypacker (1973), Scattering and absorption of light by non-
spherical dielectric grains, Astrophys. J., 186, 705-714.

Siqueira, P. and K. Sarabandi (1996), Method of moments evaluation of the two-dimensional
quasicrystalline approximation, IEEE Trans. Antennas Propagat., 44(8), 1067-1077.

Siqueira, P. R. and K. Sarabandi (2000), T-matrix determination of effective permittivity
for three-dimensional dense random media, IEEE Trans. Antennas Propagat., 48(2),
317-327.

Tsang, L., K. H. Ding, S. B. Sbih, and J. A. Kong (1998), Scattering of electromagnetic
waves from dense distributions of spherical particles based on Monte Carlo simulations,
J. Opt. Soc. Am. A, 15(12), 2660-2670.
--- PAGE 568 ---
REFERENCES 549

Tsang, L., J. A. Kong, and R. T. Shin (1985), Theory of Microwave Remote Sensing, Wiley-
Interscience, New York.

Tsang, L., C. Mandt, and K. H. Ding (1992), Monte Carlo simulations of the extinction
rate of dense media with randomly distributed dielectric spheres based on solution of
Maxwell's equations, Optics Lett., 17(5), 314-316.

West, R., D. Gibbs, L. Tsang, and A. K. Fimg (1994), Comparison of optical scattering
experiments and the quasicrystalline approximation for dense media, J. Opt. Soc. Am.
A, 11(6), 1854-1858.

Zurk, L. M., L. Tsang, K. H. Ding, and D. P. Winebrenner (1995), Monte Carlo simula-
tions of the extinction rate of densely packed spheres with clustered and‘non-clustered
geometries, J. Opt. Soc. Am. A, 12(8), 1772-1781.
--- PAGE 569 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Hlectronic)

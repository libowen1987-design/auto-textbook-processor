# Tsang《Scattering of EM Waves》Chapter 7

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 7
VOLUME SCATTERING SIMULATIONS
1 Combining Simulations of Collective Volume Scattering
Effects with Radiative Transfer Theory 373
2 Foldy-Lax Self-Consistent Multiple Scattering Equations 376
2.1 Final Exciting Field and Multiple Scattering Equation 376
2.2. Foldy-Lax Equations for Point Scatterers 379
2.3 The N-Particle Scattering Amplitude 382
3 Analytical Solutions of Point Scatterers 382
3.1 Phase Function and Extinction Coefficient for Uniformly
Distributed Point Scatterers 382
3.2 Scattering by Collection of Clusters 389
4 Monte Carlo Simulation Results of Point Scatterers 392
References and Additional Readings 401
371 -
--- PAGE 393 ---
372 7 VOLUME SCATTERING SIMULATIONS

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
ds
——
e°- 7
T(0,4) eo %:e
x
oo 1 @ | -*.7(0,0)
e@ e e° +P(O, 6,0,,4)1(0. 6%)
= N particles
T(0;, bi)

Figure 7.1.1 An clemental volume clement V with arbitrary cross section area A and
length ds for a random medium containing discrete scatterers. The elemental volume clement,
contains many particles.
in clusters. We also describe the iterative approach for solving the multi-
ple scattering equations. Forward scattering amplitude in conjunction with
Foldy’s approximation has been uscd to calculate the extinction rate. It is
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

Effects with Radiative Transfer Theory
In this section we redefine the scattering and extinction parameters of radia-
tive transfer theory to include the collective scattering bchavior of particles.
This distinguishes the definition from the conventional definition of averaged.
single-particle scattering behavior.

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
Criteria (i) and (ii) are necessary to ensure that the coherent multiple scat-
tering in volume V will include random phase fluctuations so that the energy
transfer in and out of volume V can be averaged. Furthermore, if the parti-
cles are of different sizes, shapes, and permittivities in volume V, averaging
of particle scattering behavior will also be included in the radiative energy
transfer within elemental test volume V. Criteria (i) and (ii) establish a lower
limit of volume V. .
Let F; be the incident field in the direction k; = (6;,;), and let E, be
the scattered ficld from volume V of N particles.
Ey = exp(ikj - 7) (7.1.1)
The scattered ficld can be decomposed into coherent field (F;) and incoher-
ent field €,.
Es — (Es) + €s (7.1.2)
The scattered field F, is a statistical field that contains the coherent multiple
scattering within volume V.
From one clemental volume V to most other elemental volumes, the far
field of #, can be taken. We have
> » .exp(ikr
By = Fy, ky 22 (713)
where hy = (0,.s) is the scattered direction. In (7.1.3), F' (Rs, 0) represents
the N-particle collective scattering amplitude. It can be decomposed into
coherent component (F(ks,k;)) and incoherent component F(ks, ki).
F (ks, ki) = (F (ks, ki)) + F (Bs, ke) (7.1.4)
The optical theorem can be applied to N scatterers, which can be viewed
as a single object called N-scatterer. Thus, for the case of nonabsorptive
scatterers we have
An a eo
Fim {tka kd} = ff an.lr Ob)? (7.1.5)
7 4x
The phase function P(ks, k;) and the scattering coefficient «s are next defined
to take into account the collective scattering behavior of N particles.
a hg, ki) |?
Plis ki) = ti (Fs kd!) (7.1.6)
V—large Vv
--- PAGE 396 ---
§1 Combining Volume Scattering Simulations with Radiative Transfer 375
Ks = [e2P Gok (7.1.7)
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
Once the phase matrix and the extinction coefficient are calculated, the
radiative transfer equation assumes the following standard form
1
ales) = —K LF, 8) + [eorre.syie, 8) (7.1.10)
8 J
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
2.1 Final Exciting Field and Multiple Scattering Equation
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
‘, ew
ia ebony My H
ee
Yine 5 ge te fF
—- | ce 8
pe Mega
feve e % S
Figure 7.2.1 An incident ficld inc(F) impinges on a collection of N particles in yolume
Vv.
and includes near-field and far-field effects.

‘Thus given a single particle j and a field Y/ impinging upon a particle

j, the scattered field from particle j is

U5 = GoToF (7.2.1)
where the superscript £ denotes exciting field and Gp is the Green’s function
(propagator).

Next consider two particles 7 and | with the incident field wine upon

them. The total field includes

® = Wine + Gol Wine + GoTjbine + °° (7.2.2)
where GoTibine and GoTtine are the scattered fields from particle | and
particle j, respectively, that “directly” scatters inc.

However, there can be second-order scattering which are GoT}GoTjWine
and GoTjGoTiWinc. The second-order field GoT}GoTjyPinc scatters the inci-
dent field from j to | which further scatters the field. Similarly,
GoTjGoTiPine consists of scattering first from particle | and then from par-
ticle j. Thus we have

WO = Wine+GoliVine+ GoT jPine+ GoTi Gol; Pine + GoTjGoTiPine+ > (7.2.3)
We can keep repeating for the third order, the fourth order and so on, up to
an infinite number of terms

= Vine + GoTrpine + Gol ;Vine + GoTtGoTj Vine + GoT;GoT Vine

+ GoTGoT; GoT Wine + GoT;GoTiGoTj Wine
+ GoT\GoTjGoTiGoTjhine + GoT;GoTiG@oTjGoTivine + +++ (7.2.4)
--- PAGE 399 ---
378 7 VOLUME SCATTERING SIMULATIONS
‘The infinite series in (7.2.4) can be rearranged as follows
v =Vine + Goli (vine + GoTjPine + GoT}GoTiWine
+ GoLjGoNGoLythine + ---) + GoT} (vine + GoTivine
+ GoLiGoT; Pine + GoTIGoLjGoTivine + +++) (7.2.5)
The first sum in (7.2.5) went through particle I as the last particle, and the
second sum in (7.2.5) went through particle j as the last particle. We define
the exciting field %/ to be the sum in the first parentheses and define the
exciting field ue to be the sum in the second parenthesis. Thus
WF = Vine + GoliWine + FoTGoTjVine + GoNGoT)Golivine
+ GoTiGoTjGoTiGolWine + +++ (7.2.6)
dP =Vine + GoT Pine + GoTjGoTivine + GoTjGoTiGoT Wine
+ GoTjGoT:GoTjGoTiWine + +++ (7.2.7)
We also let
we = Golf (7.2.8a)
Ww} = GoTyb? (7.2.8b)
be the scattered fields from particles / and j, respectively. Then,
O= Pine + WE + YF (7.2.9)
We also have
Y= Pine + Ps (7.2.10)
bs =U + U5 (7.2.11)
Thus we of (7.2.6) represents the “final” exciting ficld that excites particle j.
Tt expresses the idea that after going through multiple scattering between the
two particles, this is the field that is finally exciting the particle j. Similarly
yf is the “final” scattered field from particle 1.
Next, the infinite series in (7.2.6) can be manipulated as follows:
UF = Vine + Gol Vine+ Gol} Vine +GoljGoT bine + Gol jGoNGoT hine+--*)
(7.2.12)
Comparing with (7.2.7), it is clear that the term in the parentheses in (7.2.12)
is yf. Thus
EB aj Tape 5
WF = Vine + GoTnhj (7.2.13)
Similarly from (7.2.7) we obtain
UP = Vine + oly} (7.2.14)
--- PAGE 400 ---
§2.2 Foldy-Lax Equations for Point Scatterers 379
As derived above, the concepts of final exciting field and final scattered field
are rigorous.

Note that GoT}~/? does not appear on the right-hand side of (7.2.13)
because the final exciting field of particle 7 docs not excite itself. Equations
(7.2.18) and (7.2.14) are the self-consistent multiple scattering equations
for the exciting fields of two particles. After the exciting fields are solved,
(7.2.8) and (7.2.11) are used to calculate the total scattered field. Note that
the Foldy-Lax multiple scattering equations for the two particles as given by
(7.2.18) and (7.2.14) are exact. It is also important to recognize that 7; and
T; are only the single-particle scattering transition operator.

‘The equations of two-particle scattering can be readily gencralized to N
particles. For N particles

N
OF = Vine + Gotinl (7.215)
ee
where j = 1,...,N. The total scattered field is
N
b= uy (7.2.16)
j=l
W) = GoTiye (7.2.17)
The total field is
= Vine + Us (7.2.18)

Equations (7.2.15)-(7.2.18) are the Foldy-Lax self-consistent multiple
scattering equations. They are derivable from Maxwell's equations and are
exact relations without approximations [Peterson and Strom, 1973; Tsang ct
al, 1985]. Generally, (7.2.15) consists of N equations with N unknowns 2,
j =1,...,.N. In principle they can be solved numerically to yield the exact
result of the multiple scattering equations.

2.2 Foldy-Lax Equations for Point Scatterers
For the cases of point scatterers, the transition operator Tj is simple so that
the Foldy-Lax multiple scattering equations assume a simple form. The point
scatterer has a simple single-particle scattering relation of

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
Ifo, =0, then f” = kf”. For a point scatterer,
T; = —4n fO(F — 7) (7.2.24)
so that
eiklFT]
GoT bP = fy ©) (7.2.25)
J
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
The total scattered field and the total field are, respectively,
N gikit-7il b
vel®) = > fw (m) (7.2.29)
in FF
VF) = Bine(F) + v4(7) (7.2.30)
If an iterative approach is used to solve (7.2.26), then the first-order solution
is
WO) = VinelT) (7.2.31)
--- PAGE 402 ---
§2.2 Foldy-Lax Equations for Point Scatterers 381
for the exciting field. For the first-order scattered field we have
1 N giklr—7i|
wM=Le Forint) (7.2.32)
=
N
WA = VT y@ (7.2.32)
I=1
where
,ik|F—Fi|
say — pe CF > 29
wy) =f Fm ine(Fi) (7.2.32c)
The higher-order solutions are, for n > 1,
E(nt)) = Cu Oye 4
FR) = dinel®) +0 F om"! (m) (7.2.33)
iv
j N iklF-Fil E(n+1)
wtD@) = Vira aq (7.2.34)
1
The Foldy-Lax multiple scattcring equation (7.2.26) can be cast in a matrix
form. Let
by = VER) (7.2.35)
eiklti—F 5)
Ay = f—— 7.2.36,
ot (7.2.96)
b; = Wine(*,) (7.2.37)
Then (7.2.26) becomes
N
by = by + Agr (7.2.38)
va
If we further let
1 ifi=j
Zi = se 2 7.2.39
0 {has iA] (7.2.39)
then we have the following matrix equation:
N
Se Sj = by (7.2.40)
I=]
In matrix notation
Z-pad (7.2.41)
--- PAGE 403 ---
382 7 VOLUME SCATTERING SIMULATIONS
where Z is the impedance matrix, # is the unknown column vector of the
exciting fields of the particles, and b is the right-hand side. The iterative
approach that is used in (7.2.31)-(7.2.34) is called the direct iteration, and
the Neumann series or the Born series. The first-order term is known as the
Born approximation.
2.3 The N-Particle Scattering Amplitude
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
We shall consider two cases of point scatterers. In the first case, the point
scatterers are uniformly randomly distributed. In the second case, the point
scatterers form clusters. We study scattering by a collection of clusters. We
shall show that even though the two cases have the same average number of
scatterers per unit volume, their scattering propertics are quite different.
3.1 Phase Function and Extinction Coefficient for Uniformly Dis-
tributed Point Scatterers
Tn this section we illustrate the phase function and the extinction coefficient
for nonabsorptive point scatterers using the definition of (7.1.6) and (7.1.7).
The Foldy-Lax self-consistent multiple scattering equations will be solved to
second order.
--- PAGE 404 ---
§3.1 Uniformly Distributed Point Scatterers 383
Z
ks
ky MOO
vie oo
feie fe:
‘ te H H
IRS oi ee:
PANS OE
H eee
te oy tes” Yy
fe @ege 'e-
i @ oor
xX
Figure 7.3.1 Monte Carlo simulation geometry. Many point particles are randomly and
uniformly distributed in a cubic box with volume V.
Consider an incident plane wave Ling in the direction k; impinging upon
a volume V, the size of which obeys the three criteria of Section 1. The
volume V contains N number of nonabsorptive point scatterers located at
F\,72,...,7N (Fig. 7.3.1). The point scatterers are uniformly and randomly
distributed in volume V.
The multiple scattering cquations for the “final” exciting field EZ, are,
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
The conventional radiative transfer theory gives the phase function and scat-
tering coefficient as
P(hes, ki) = nol fl? (7.3.4)
ks = Arno fl? (7.3.5)
--- PAGE 405 ---
384 7 VOLUME SCATTERING SIMULATIONS
The particle positions are discussed in Chapter 4, Section 5 of Volume I.
From (4.5.18) of Volume I
(n()) = Np) = no (7.3.6)
so that
M=7 (73.7)
DY) = V “3.
is the single-particle probability density function. From (4.5.21) and (4.5.22)
of Volume T
(n® (7) = N(N — 1)pa(F,7’) (7.3.8a)
where po(¥,7") is the joint probability density function. Furthermore,
(OE, F)) = (MOP) (MOF) oF) (7.3.8)
where g is the pair distribution function. Hence
2 ;
= uA FF N ap :
=P) =F =o 3.8
PAPE) = IME) = GE yaa”) (7.3.80)
As the particle separation becomes large, their joint probability density func-
tion should be independent. Thus
jim 9() =l1 (7.3.9)
If we view the N particles as a single object, the N-particle, the forward
scattering theorem should also be applicable to the N-particle scattering
amplitude. Thus
An oe 8 a eye
a mF (hs, ki) = | dQ.|F (ks, ki)| (7.3.94)
First-Order Solution
For the first-order solution we have
E}, (3) = exp(iki -¥;) (7.3.10)
Then, the first-order N-particle scattcring amplitude is
N
FO (ks, hi) = f° exp(ika 7) (7.3.11)
jal
where ky = k;—K. From (7.3.11), we sce that the random positions of 7; will
give random phase fluctuations except in the forward direction of ky = 0.
--- PAGE 406 ---
§3.1 Uniformly Distributed Point Scatterers 385
Taking the configurational average of (7.3.11) gives
3 N’ f&
(F% (ley, es) = £37 i] dF; exp(ika -7;)p(Fj) = 7 i dF; oxp(ika +75)
jae jae
(7.3.12)
Note that before averaging, cach 7; is distinct as given by (7.3.11). However,
7; becomes a duinmy integration variable on averaging. The summation over
j can now be replaced by N. We thus have
(F (kes. ki) = nol f dr; exp(ika + Fj) (7.3.13)
Vv
Since the volume V is much larger than a wavelength, the coherent field as
given by (7.3.13) is sharply peaked in the forward direction of ks = kj. This
concept of strong forward scattering of a coherent wave is evident in wave
theory.
Jim (FO (hey, ki)) = nof (27)35(Ka) (7.3.14)
90
The absolute value of the amplitude squared is
NON
[FO (hs, Ri)? = S00 FP exp(ika « (Fj — 70) (7.3.15)
j=1l=1
The double summation is next separated into j = 1 and j ¥ I, that is
scattering from the same particle and scattering from two different particles.
NON
[POO (Fey, bi)? = NU FP + 3° 0 [FP explika - (F) — 7) (7.3.16)
a
Next the average of (7.3.16) is taken with the second term averaged over the
two-particle joint probability density function of (7.3.8c)
NN. -
(FO (be kiP) = NIP + 00 / arf dr] f Pe Mpo(F 5,71)
By
NON _ N
NIFI2 . 2 etka (Fy—Fi)___ ae.
= nif *LE fof eur Fee alts 7)
tay
(7.3.17)
Note that on integration both 7; and 7; become dummy variables. Then
a a . N? " a-(Fi—F1) p(x. _ =.
(FO (kak) = UIP + Pals f arsf are a07; — TH)
--- PAGE 407 ---
386 7 VOLUME SCATTERING SIMULATIONS
= nif NP ae an, | amee Fs) toe, 7) —1
HANIFP + Delf f ari] are lori 7%) ~ 1]
N?. 4 f fz,
+ Tait far f are -7) (7.3.18)
The first term in (7.3.18) represents that of conventional radiative transfer
theory and the second term represents correlation effects. The last term in
(7.3.18) corresponds to the coherent intensity that is in the forward direction.
However, from (7.3.11) we have
1 ayy
it PO (hs hi) = {Inf = Nf? (7.3.19)
Thus, (7.3.19) only contains the first term of (7.3.18) and does not con-
tain the pair distribution function as in (7.3.18), nor docs it contain the
sharply peaked forward scattering. Thus, the first-order solution alone does
not, obey the optical theorem of (7.1.5). For the optical scattering theorem to
be obeyed, it shall be shown that the InF has to be carried out to the second
order in scattering. Coherent forward scattcring does not contribute to the
phase function nor to the scattering coefficient. Next we calculate the inco-
herent bistatic scattering intensity. Define incoherent scattering amplitude
by
F (kis, bs) = F (key, Bi) — (F (kes, ki) (7.3.20a)
and
(WF (ks, ki) ?) = (UF (hes, Ri) PP) — (Ps, Be)? (7.3.20b)
Note that from (7.3.13) we ave
a N2 P _
( \ - . a a
EO (kak) = Fish fay [ arvesplika-(—F)) (78.206)
Note that (7.3.20c) is identical to the last term of (7.3.18). To first order we
have
FO) (hey, by) = FO (hey, be) — (FO (kes, ks)) (7.3.20d)
Thus, if we take the average of the absolute value squared of F“) by sub-
tracting (7.3.20c) from (7.3.18), we obtain
(FO (Fes, b)/?) = (PO (hes fs))?) — (FO (Bs, Bi) P
N? Z,.(7, -m))olF,
= NUP + Tals? fay f arvexpliRe- (rj ~ root) -70) ~ 1
pra Np EP e(F 735
=ais2+ Cure f arexpliba-Pl9) - 1 (7.3.21)
--- PAGE 408 ---
§3.1 Uniformly Distributed Point Scatterers 387
We further divide (7.3.21) by V to calculate the phase function:
a py — ea ke?)
Plks, ki) = v
=nilfP + nals? f drexp(iEa- ral) 1] (7.3.22)
In the conventional radiative transfer theory, P(k,, ki) = no|f|?. Thus, the
phase function of collective scattering is not the same as conventional theory
except when the particle positions are independent, that is, g = 1.
We next carry out an angular integration over the scattered directions
in (7.3.22). We make use of the integral identity
z sin(ki
| dO, oxp(—iky-7) = 4n Be) (7.3.23)
An kr
Integrating over the scattered angles, we obtain
Par An sin(k _
[ Plbsinyan, =dnng|f 2 +n? [ese(om -1) SSO) c(i 7)
(7.3.24)
We next examine the consequence if the coherent intensity is included in the
phase matrix. Let the phase matrix of coherent wave be P, :
ra 1 eg n2\f\? = a z
Paks) = FIP Go ky) = "SF" ff arsexp(iba-13) [ arvexp(—ia-7)
v Vv
= nats? f arexplika-7) (7.3.25)
Integration of (7.3.25) over scattered directions gives
as r — sin(k
| d0,P. (kg, bi) = r2|f2 | dr expliKj yan)
v .
oyna — _.,_sin(kr)
= nis? f drcos(R;-F4aa——— (7.3.26)
Vy
The integration of P, over directions gives the power contained in the coher-
ent wave. Summation of the integration of P and P, then gives, from (7.3.26)
and (7.3.24)
/ d024(P(ks, hi) + Pes, i)
2,2 2. op aloe sin(kr)
=4nrn,|f/P +5 J dri fl? cos(ki -F) (97) - 14
Vv kr
2 f omer xy sin(kr)
+ ni ff GF | fP cos(Ry Par (7.3.27)
Vv
--- PAGE 409 ---
388 7 VOLUME SCATTERING SIMULATIONS
As clear from (7.3.25), the phase matrix of the coherent wave is a Dirac delta
function in the forward direction in the limit of large V. Its power as given by
(7.3.26) is nonconvergent with large V and also depends on the shape of V.
Purely forward scattering does not affect radiative transfer, which describes
the redistribution of radiative energy in different directions. This further
justifies the exclusion of the coherent wave in the phase matrix.
Second-Order Solution
Next, we show that energy conservation is obeyed if we include second-order
scattering amplitude in the forward direction. In the second-order solution,
the exciting field is
x exp(ik|Fj —Fi|)
= exp(iky -F CXPURITG STU orn ak, - F
BS = exp(iki 73) + xv f iF Fil exp(ik; - 71) (7.3.28)
tw
Putting (7.3.28) into (7.3.3) gives the N-particle scattering amplitude as
N
F (ks, ki) = SOF exp ks -71) exp(—iks 7)
=1
N - .exp(ik{Fj; — Ti) Loz
+32 f exp(-ik, -7) LIA exp(iki +7) (7.3.29)
1 on
The forward scattering amplitude to second order is
MX pcexp(iklr; — Fil)
FO (Fisk) = NF + YY POSIT exp(—iki(P1 — 75) (7-830)
rp TL
Bie ;
where F) is the sum of the first-order term and the second-order term.
Taking the average using p2(7;,77) as given by (7.3.8¢)
(ip. pee 2 f exp(ik|Fy — Til)
(FO (hi, ki)) = NF + OCF | ar; oa
I=1 al J
Tomo N —
-exp(iki- (Fi — Mayers)
N? exp(ik|Fj — 7|)
=Nftalh | a; |
re qah far fem iF) — 7
- exp(iki - (Fi — F5))g(7i — 75) (7.3.31)
--- PAGE 410 ---
§3.2 Scattering by Collection of Clusters 389
Using the property that g(¥) = g(-7) gives
(FO (ky, fi))
N? r exp(ik|Fy — 7) =
HN p+ el? fates far E TD cost (r-rs)itr 75)
N? ik 7
=NtTP | ap SUH) cos(k; -F)g(F) (7.3.32)
To verify optical theorem, we take the imaginary part of (7.3.32)
4 Tn (F) (hi, i)
k Vv
4n 4rsin(kr >
= nolm{f} + n2/? [ aptesinkr) cos(ki -F)[9(F) — 1]
k Jy kr
Ag sin(k _
nef? [ apt Snlle) cos(hy-¥) (7.3.33)
Vv wr
Comparing the right-hand sides of (7.3.33) and (7.3.27) shows that they
agree with each other. Thus
/ ds (Plies, fa) + Pe(kis, i)
_ de Im{ (FO) (he, i))}
ok Vv
r (D (fe fee) |2 FO (fee. ee) |2
= | ds [Fs ki)? + MEO Cs, ki)? (7.3.34)
V Vv
Thus, to apply the optical theorem, the N-particle forward scattering am-
plitude has to be calculated to the second order so that
. [FO (hy, bs)?
= 1,
mem la | aE
. 4nln{ (FO) (kj, h))} 1 (ip fry? :
= lm (reat fou (be.f))|2| (7.3.35)
3.2 Scattering by Collection of Clusters
We next consider scattering by collection of clusters. Let each cluster be la-
beled as a primary scatterer, and let the point scatterers within each cluster
be labeled as secondary scattercrs. Then the phase function and extinction
coefficients depend on gs, which is the pair distribution function among sec-
ondary scatterers within a primary scatterer as well as the pair function
between clusters gp.
--- PAGE 411 ---
390 7 VOLUME SCATTERING SIMULATIONS
Zz
k,
iy ee
“ot e ot
i ad care
MR / eee:
: tee y
ie ee 3
fe ee 8
x
Figure 7.3.2 Clustered point particles are randomly distributed in a cubic box of size L
with volume V. The clusters are randomly distributed, and within each cluster of size |. the
particles are randomly distributed.

Consider a volume clement V as defined in Section 1. The volume con-
tains N, primary scatterers (clusters), cach of which consists of N, sec-
ondary point scatterers (Fig. 7.3.2). The Np clusters are centered at Fg, a =
1,2,..., Np, and within each cluster a the secondary scatterers are centered
at Taj with respect to the center of the ath cluster, 7 = 1,2,...,N,. Thus

N=N,Np (7.3.36)
is the total number of particles in volume V. Then
N ; 9
No= = Nenp (7.3.37)
is the number of particles per unit volume and n, = N,/V is the number of
clusters per unit volume. Note that N and N, are large numbers in V while
IN, does not have to be large. Then, from (7.3.11), the first-order collective
scattering amplitude is
N Np Ny
FO (hei) = f So exp(ika-F)) = f 7 YW explibe: Fa +Faj)) (7.3.38)
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
From (7.3.395) we obtain
FO (be RP) LIRR pee
= FUE
o=1
Ny Np
+ SOY expla: (Fo Fad (bE hah "ask
a=19=1
Ba
i (er ree
= 7 Noliee Gack
N?2 = ran ar
+ | dF exp(ika TF) (hts. hi) SZ tha konte)} (7.3406)
On the other hand,
(FO (hashs)) =p f drexp(iRa -7)( 2 (hss) (7.3.40¢)
In (7.3.40b) we have made use of the joint probability density function of
primary scatterers, that is analogous to (7.3.8¢),
= ay { (FarFs) Np q
Pp(Fa,Fa) = ( va N,-1 (7.3.41)
and gp is the pair distribution function of primary scatterers. Note that
from this point of view, the primary scatterer is a “unit” scatterer. Putting
(7.3.40b) and (7.3.40e) into (7.3.40a) gives
Plies, ki) = Mp (Ja (ks, hi) |?)
+ mig fa (bs bi) ) (69 (hss fi) | drexp(ika -F) (9p(F)—1) (7.3.42)
Let the primary scatterer size be confined to vp. Then the first moment of
primary scatterer scattering amplitude is from (7.3.39a)
(18 ek) — 2 [ arexpiika 7) (7.3.43)
p Jo,
--- PAGE 413 ---
392 7 VOLUME SCATTERING SIMULATIONS
From (7.3.39a) we obtain
Proj. p\i2
{fo (Rs, Ki)|")
Ne Ne
=IFPNs +f? 30 > (exp(iha- Foy — For))) (7.3.44)
j=l =i
Aj
2, N? 2 -
= nals Se f area f area expliRa- (Pag ~Fot))QelFop Fot) (7.3.44)
“Pp JUp Up
where the joint probability density function of secondary scatterers is, anal-
ogous to (7.3.8¢),
—— Gs(Faj,Fat)\ Ns 4
Ps(Faj;Fot) = (eSegta N-1 (7.3.45)
with g, being the pair distribution function of secondary scatterers. To illus-
trate, we consider a special case with gp = 1,gs = 1, and let vp, be a cubic
volume of /3. Then the integrals in (7.3.43) and (7.3.44) can be carried out
readily. Putting the results into (7.3.42) gives
2 2 2
as ° . sin (Kae sin (kay sin (ka. ‘¢
Phy, bi) =nol FP + roNol Ff? sin (kee) sin (Kay'g) sin (kes'§)
kacS Kay kazS
(7.3.46)
where kg, kay, and kg, are respectively the -, y-, and z-components of
kq. Note that the result in (7.3.46) is substantially different from that of
(7.3.22), where the particles are not in clusters. In some cases, the result
of (7.3.46) can be much larger than that of (7.3.22). This shows that when
small point scatterers cluster to form “larger” particles, the scattering can
be much larger even when the total number of small point scatterers remain
the same.
4 Monte Carlo Simulation Results of Point Scatterers
In this section we illustrate Monte Carlo simulations of scattering by point
scatterers. We calculate the extinction coefficients and phase functions for
the cases of uniformly random distribution and the case of clustered random
distributions.
Consider an incident wave impinging upon N scatterers
Eine(P) = ef * (7.4.1)
--- PAGE 414 ---
§4 Monte Carlo Simulation Results of Point Scatterers 393
where
kj = k(sin 0; cos @i& + sin 0; sin d:f + cos 6,2) (7.4.2)
We start by putting N particles in a cubic box of size V = L*. The coor-
dinates 7; = (a;,4j,2j),9 = 1,2,...,N, are determined by choosing three
random numbers between 0 and 1 and then multiplying them by L. Once the
positions of the N particles are given, we can solve the Foldy-Lax multiple
scattering equations
: 5) eS pil =F) pa
BL, = Bine(Fj) +S) fF ELF) (7.4.3)
a lit
143
j =1,2,...,.N. After the exciting field Fi, (Fj) are calculated, the “final”
scattered field can be calculated in the far-field region. Let
ks = k(sin 9, cos ds% + sin 0, sin os + cos 052) (7.4.4)
be the observation direction of the scattered ficld. Hence,
ike
Es?) = —— Fr (hss hi) (7.4.5)
where
> = N =
Fy (ks, ki) = 30 f exp(—ikis 71) Eee() (7.4.6)
I=L
is the N-particle scattering amplitude. These can be calculated for many
realizations. We then calculate the realization averages. Let angular bracket
() denote realization average. The coherent scattering amplitude is
N,
a 1 & a8
(Fw (ks, ki) = WD Fwvlhs, hi) (7.4.7)
OT rl
where r is the realization index and N,, is the number of realizations. The
incoherent scattering amplitude for each realization is
F (kas ki) = Fes bi) — (Fv (hss bi) (748)
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

(Q)2 + N ~~. NWN oc _ eiklti-F

Fy (Fes, hi) = YO FERRI 4 SE pherthe™ et (7.4.11)
j=l j=l [=1 Ir; —¥el
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

Tn Monte Carlo simulations, it is important to demonstrate convergence
with respect to the number of particles N in the cubic box and the number
of realizations N, for a fixed particle number density ny. We first present the
convergence of extinction coefficients as we increase the number of realiza-
--- PAGE 416 ---
§4 Monte Carlo Simulation Results of Point Scatterers 395
P50
4.0 =
5 3.0 { in LEGEND
2°) Sahara
5B 2.0
1.0
0.0
° 20 40 «460 «80 =§=60
number of realizations
Figure 7.4.1 Convergence test for the Monte Carlo simulations with respect to realizations
and the number of particles for N = 63 (ZL = 25A) and N = 500 (Z = 502) point particles
uniformly and randomly distributed as in Fig. 7.3.1. ‘They are compared with the independent
scattering result,
tions and the number of particles in Fig. 7.4.1. The results in Fig. 7.4.1 are
for the uniform random case. Initially, we put N = 63 particles in a cubic
box of size L = 25A, so that the particle density is n, = 0.004A~9. This
is to be compared with the independent scattering theory, Kes = 47no|f|?,
where the subscript i stands for independent scattering. The independent.
scattering as defined by (7.3.5) predicts Ke; = 4.0 x 10-°\~!, while in the
Monte Carlo simulations we get Ke = 3.958 x 106A"! after 100 realizations.
To demonstrate convergence with respect to the number of particles, we in-
crease the number of particles to N = 500 while ny remains at 0.004A~3,
This is done by increasing the number of particles to 500 and increasing
the volume to V = L? = (50A)%. This result is also given in Fig. 7.4.1,
where Ke = 3.944 x 10-°A~! after 100 realizations. Figure 7.4.1 indicates
convergence of the results with respect to the number of realizations and.
the number of particles. All the Monte Carlo results to be presented from
this point on are given for N = 500 particles with L = 50A, 6; = 10°, and
oj = 10°.

Next, we consider the case of clustered random distribution with 10
particles in each cluster. Figure 7.4.2 shows the convergence of the extinction
coefficients versus realizations. The relative extinction coefficient (#,<) is the
collective extinction coefficient divided by that of independent scattering
--- PAGE 417 ---
396 7 VOLUME SCATTERING SIMULATIONS
“ =
_—_—
<= 21) LEGEND
= |/ 1
3 10 | 05...
3 = -
at —*-
¥ | -—-— - —-
ae
a4
24°
°
0 2 40 60 8 WO
number of realizations
Figure 7.4.2 Monte Carlo simulations for the clustered scatterers of Fig. 7.3.2. I, is de-
creased from 1.0 to 0.24. There are 50 clusters containing 10 scatterers each (N = 500, L =
5OA).
(kre = #* with Ke; = 4.0 x 10-A~1). There are 50 clusters, cach containing
10 particles in all plots given. The cluster cube size |, is varied from 1.0
to 0.2. For the cubic box size of 1.0A there is very little difference between
the uniform and clustered distribution as can be seen from the solid curve in
Fig. 7.4.2. However, as the cluster volume is made smaller than a wavelength,
Kre can become large. We see from Fig. 7.4.2 that the result of tp. for the case
of /, = 0.2A is much larger than «,, for the case of |, = 1\. This shows that
when considering random media problems, the significance of the clustered
geometry must be considered. In Figs. 7.4.3 and 7.4.4, the phase functions
of the Monte Carlo results of Fig. 7.4.1 (uniform random N = 500) and the
1. = 0.2X of Fig. 7.4.2 are presented, respectively. Both the incoherent phase
function Pinc(dotted line) and the combined phase function Pine + Peoherent
(solid line) are given. The results are averaged over 100 realizations. In the
polar plots, the top half-plane gives @, = 10° and @, ranges from 0 — 180°
going clockwise. In the bottom halfplane @, = 190° and @, ranges from 0 >
180° going counterclockwise. Comparing Figs. 7.4.3 and 7.4.4, we sec that
the clustered scattering case gives a larger incoherent contribution than does
the uniform case, while the opposite is true for the coherent contribution. In
both figures, the cohcrent part has a sharp peak of large amplitude (many
decibels larger) in the forward direction (0. = 170°, és = 10°). Note that the
polar plot is in the decibel scale, so that the coherent forward peak has much
larger amplitude than that of the other directions. As V approaches infinity,
--- PAGE 418 ---
§4 Monte Carlo Simulation Results of Point Scatterers 397
polar plot (dB)
-20
-60
20-60 -80 -o— -80 -60 -20

-80

60

-20
Figure 7.4.3. Polar plot (dB) of the phase function of Fig. 7.4.1 of the uniform random
case for N = 500 and E = 50) with the geometry given as in Fig. 7.3.1. Upper half-plane
shows @5 = 10° and @, is 0° + 180° going clockwise. Lower half-plane shows 65 = 190° and
Gs is 0° + 180° going counterclockwise. Incident angles are 6; = 10° and ; = 10°.

polar plot (dB)
-20
(>,
20 -d -80 -f10 80 0-20

“80

60

-20
Figure 7.4.4 Polar plot (dB) of the phase function of Fig. 7.4.2 of the clustered random
case for N = 500, f. = 0.2A, and L = 50) with incident angles at 6; = 10° and o; = 10°
Upper half-plane shows @, = 10° and 4 is 0° — 180° going clockwise. Lower half-plane
shows 0, = 190° and 4, is 0° + 180° going counterclockwise.
--- PAGE 419 ---
398 7 VOLUME SCATTERING SIMULATIONS
2 60
If
§ 40 : = -4NG_OFGEF.
2 H :
S 304 |i h i
g ik ;
—& 20 i
10 i
0.0
0 20 40 60 80 100 120 140 160 180
scattering angle (degree)
Figure 7.4.5 Comparison test between the second-order approach and the exact solution
Phase function of Fig. 7.4.2 with [, = 0.354, NV = 500 and L = 502 for 1 realization (6; =
10°, 0; = 10°, 6s = 20° and @, ranges from 0° to 180°).
the coherent wave will approach a Dirac delta function. Thus, the coherent
peak has to be excluded from the phase matrix and extinction coefficient
calculations.

All the Monte Carlo results given so far are obtained by solving the mul-
tiple scattcring equation (7.4.3) exactly. To compare the iterative method
solution and the exact solution, we compare the incoherent phase functions
for a single realization using the second-order approximation and the ex-
act. method. The comparison is shown in Fig. 7.4.5. In the figure, I, =
0.35A, N = 500, @, = 20°, and @, is varied from 0° to 180°. For one realiza-
tion, the second-order solution shows significant differences from the exact
solution for most scattering angles. However, when 100 realizations are ay-
eraged, the second-order solution agrees with the exact method (Fig. 7.4.6).
This shows that for a single realization, higher-order scattering effects are
important. However, these higher-order scattering effects tend to cancel out
on averaging over realizations, and the second-order theory gives a quite
accurate average. The iteration approach can be very attractive for more
complicated problems of vector electromagnetic scattcring by a large num-
ber of dielectric scatterers of arbitrary size. In Fig. 7.4.7 the comparison
between the analytic collective scattering theory of (7.3.46), the indepen-
dent scattering of (7.3.4), and the Monte Carlo simulation of Fig. 7.4.6 with
--- PAGE 420 ---
§4 Monte Carlo Simulation Results of Point Scatterers 399
%
P 60
50 LEGEND
c ind oder..
3 40
2 30
$ S
g 20
10
0.0
© 20 40 60 80 100 120 140 160 180
scattering angle (degree)
Figure 7.4.6 Comparison test between the second-order approach and the exact solution
of Fig. 7.4.5. Results are averaged over 100 realizations (6; = 10°, ; = 10°, @5 = 20°, and
Os ranges from 0° to 180°).
2 eo
LEGEND
6.0 OR esaes—
-- VQ averages...
c —inder.
2 40
é
2 30s,
2 : .
8 fA
2 204i: .
a ~
104 ¢ =
0.0 >
© 20 40 60 8D 100 120 140 160 180
scattering angle (degree)
Figure 7.4.7 Comparison test between the analytical result from (7.3.46), the independent
scattering, and the Monte Carlo simulation of Fig.7.4.6 (1000 realizations). The parameters
are: lg = 0.35A, Ns = 10, Np = 50, N = 500, no = 0.004A~ and L = 50A (4; = 10°, 0; =
10°, 5 = 20°, and 4, ranges from 0° and 180°).
--- PAGE 421 ---
400 7 VOLUME SCATTERING SIMULATIONS
1000 realizations is given. While the Monte Carlo result and the collective
scattering theory agrees, the independent scattering predicts the wrong re-
sult. The dip in the Monte Carlo result is due to the subtraction of the
coherent part from the total phase function.
--- PAGE 422 ---
REFERENCES 401
REFERENCES AND ADDITIONAL READINGS

Au, W. C., J. A. Kong, and L. Tsang (1994), Absorption enhancement of scattering of
electromagnetic waves by diclectric cylinder clusters, Microwave Opt. Technol. Lett.,
7(10), 454-457.

Au, W. C., L. Tsang, R. T. Shin, and J. A. Kong (1996), Collective scattering and absorption
in microwave interaction with vegetation canopies, Progress in Electromag. Res., 14,
182-231, EMW Publishers, Cambridge, Massachusetts.

Chuah, H, T. and H. S. Tan (1992), A microwave emission model for vegetation medium
using the Monte Carlo method, Part I and Part LI, J. Electromag. Waves and Appl., 6,
799-852

de Vries, P., D. V. van Coevorden, and A. Lagendijk (1998), Point scatterers for classical
waves, Rev. Modern Phys., 70, 447-466.

Fikioris, J. G. and P. GC. Waterman (1964), Multiple scattering of waves, IT. Hole corrections
in the scalar case, J. Math. Phys., 5, 1413-1420.

Foldy, L. L. (1945), The multiple scattering of waves, Phys. Rev., 67, 107-119.

Lax, M. (1951), Multiple scattering of waves, Rev. Modern Phys., 23, 287-310.

Lax, M. (1952), Multiple scattering of waves IL. The effective field in dense systems, Phys.
Rev., 85, 261-269.

Manchuck, G. I, G. A. Mikhailou, M. A, Nagaralieu, R. A. Darbinjn, B. A. Kargin, and
B. §. Flepou (1980), The Monte Carlo Methods in Atmosphere Optics, Springer-Verlag,
New York.

Peterson, B. and S. Strom (1973), 'T matrix for electromagnetic scattering from an arbitrary
number of scatterers and representation of E(3), Phys. Rev. D, 8, 3661-3678.

Sheng, P., Ed. (1990), Scattering and Localization of Classical Waves in Random Media,
World Scientific, Singapore.

Tsang, L., J. A. Kong, Z. Chen, K. Pak, and C. Hsu (1995), ‘Theory of microwave scattering
from vegetation based on the collective scattering effects of discrete scatterers, Passive
Microwave Remote Sensing of Land-Atmosphere Interaction, B. J. Choudhury, Y. H.
Kerr, E. G. Njoku, and P. Pampaloni, Nds., 117-154,

Tsang, L., J. A. Kong, and R. 'T. Shin (1985), Theory of Microwave Remote Sensing, Wiley-
Interscience, New York.

Tsang, L., C. Mandt, and K. H. Ding (1992), Monte Carlo simulations of the extinction
rate of dense media with randomly distributed dielectric spheres based on solution of
Maxwell’s equations, Optics Lett., 17(5), 314-316.

Yueh, 8. H., J. A. Kong, J. K. Jao, R. T. Shin, and T. Le Toan (1992), Branching model for
vegetation, IEEE Trans. Geosci. Remote Sens., 30, 390-402.
--- PAGE 423 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc.
ISBNs: 0-471-38800-9 (Hardback); 0-471-22430-8 (Electronic)

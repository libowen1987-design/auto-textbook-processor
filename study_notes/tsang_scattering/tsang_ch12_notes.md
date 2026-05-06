# Tsang《Scattering of EM Waves》Chapter 12

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 12
MULTIPLE SCATTERING BY CYLINDERS
IN THE PRESENCE OF BOUNDARIES
1 Introduction 594
2 Scattering by Dielectric Cylinders Above a Dielectric
Half-Space 594
2.1 Scattering from a Layer of Vertical Cylinders: First-Order
Solution 594
2.2 First- and Second-Order Solutions 603
2.3 Results of Monte Carlo Simulations 613
3 Scattering by Cylinders in the Presence of Two
Reflective Boundaries 622
3.1 Vector Cylindrical Wave Expansion of Dyadic Green’s Function
Between Two Perfect Conductors 622
3.2. Dyadic Green’s Function of a Cylindrical Scatterer Between
Two PEC 629
3.3. Dyadic Green’s Function with Multiple Cylinders 631
3.4 Excitation of Magnetic Ring Currents 635
3.4.1 First Order Solution 637
3.4.2 Numerical Results 638
References and Additional Readings 640
— 593 -
--- PAGE 612 ---
594 12 MULTIPLE SCATTERING BY CYLINDERS
1 Introduction
In Chapters 7 to 11, we have studied the multiple scattering problems with
particles in an infinite medium. In this chapter, we study the case when the
cylinders are placed on top of reflective boundaries. In Section 2, we study
scattering by dielectric cylinders lying above a diclectric half-space. Applica-
tions to scattering by vegetation and forests are illustrated. We discuss the
uniform randomly distributed cylinders and also cylinders in clusters. The
two cases have very different scattering properties. The study of backscat-
tering enhancement for the case of cylinders in the presence of reflective
boundary is also illustrated. This is a case of backscattering enhancement
that is exhibited in volume scattering in the presence of reflective boundary.
The subject of backscattering enhancement will be treated in more details
in Chpater 8 of Volume IIT. In Section 3, we study the problem of metallic
cylinders placed between two perfect conductors. For this case, the parallel
waveguide geometry facilitates the use of waveguide modes for propagation
and scattering among cylinders.
2 Scattering by Dielectric Cylinders Above a Dielectric
Half-Space
Scattering of waves from a layer of vertical dielectric cylinders overlying
a homogeneous half-space is an important remote sensing problem in mi-
crowave propagation, scattering, and cmission of vegetation. For example,
in forests and corn canopy, the scattering can be dominated by the trunks
and corn stalks. In this section we illustrate analytically the first-order scat-
tering solution and the concepts of gs (pair distribution functions among
scatterers in a cluster) and gp (pair distribution function between clusters)
in the two-dimensional random positioning of the vertical cylinders. Analyt-
ical solution is derived for single scattering. We shaJl present the forms of
the analytical expressions for the first-order solutions in Section 2.1, Both
first- and second-order solutions will then be rigorously derived in Section
2.2.
2.1 Scattering from a Layer of Vertical Cylinders: First-Order
Solution
Consider a plane clectromagnetic wave incident upon a layer of vertical di-
electric cylinders overlying a homogeneous dielectric half-space (Fig. 12.2.1).
The boundary of the dielectric half-space is at. z = —d. There are N cylin-
--- PAGE 613 ---
§2.1 Scattering from Vertical Cylinders: First-Order Solution 595
4,
KZ
Ly
ee
Figure 12.2.1 Scattering by vertical cylinders of length L and permittivity ¢ overlying a
dielectric half-space of permittivity €1.
ders in the canopy planted in an area A. The centers of the cylinders are
located at 71,72,...,7y. The ath cylinder is of length La and radius ag
with a = 1,2,...,N, where N is a large number. The permittivities of the
cylinders and the homogencous half-space are €, and €1, respectively. The
incident wave is in direction (x — 6;, @;) with incident electric field as
EB = (Byiiy + Epihi) et thoym thee (12.2.1)
where kir = ksin 0; cos $j, kiy = ksin0;sind;, kiz = kcos0;, 0) = On -
0;,0;), and hy = 6(x — 0;,0;). We consider observation direction k, with
hey = Ks + boyd + aed (12.2.2)
where ksz = ksin®scosds. ksy = ksinOssings, and ks, = kcos0;. The
single scattering solution will have four contributions. By single scattering
we mean single volume scattering that can also include bouncing from the
boundary of the homogeneous half-space at z = ~d. Let 7) = PD; + 252
be the position of the jth cylinder. The four contributions are as follows
(Fig. 12.2.2):
(a) Direct volume scattering by cylinder j that has a dependence of
Kab L, Lj
elkar’ By @thr22s —thes2s “J sing k, Res Ai
sasine | (kis + hss)
where
By = BF + yy
Bea = (Ri — hs) (12.2.3)
--- PAGE 614 ---
596 12 MULTIPLE SCATTERING BY CYLINDERS
(a) } - (b) ) -
(c) | (a)
Figure 12.2.2 Four scattering contributions for single scattering of the cylinder in the
presence of a reflective boundary.
Rap = Rip — Fsp = (Kix — Kor) + (kiy — Key) (12.2.4)
is a vector in the z-y-plane and
Bap Dy = huey + hayth (12.2.5)
The phase dependence can be directly traced from the figure. The phase
dependence e~*+#)—«=% jg due to the vertical z; position of the cylin-
der. The phase dependence of e*#’?s is due to the horizontal position
p; of the cylinder j, where kup is the wave vector difference between the
incident and scattered wave vectors in the horizontal direction. The am-
plitude dependence is as illustrated by the conical pattern of the cylinder
that was discussed in Chapter 1, Section 6.2 of Volume 1.
(b) Reflection by boundary followed by volume scattering by cylinder j,
which has a dependence of
ciao Dy gtkia(es+2d)~ihset, Pi ging [ (his — Reedy
Qa 2
The phase factor exp(ikiz2d) is a result of the incident wave traveling
through the canopy.
--- PAGE 615 ---
82.1 Scattering from Vertical Cylinders: First-Order Solution 597
(c) Volume scattering followed by reflection that has a dependence of
cite Bs pthinzs gtikes ey +2d) Li os, | (Rie = he)Ly
20 2
(d) Reflection volume reflection scattering. Reflection followed by volume
scattering that is further followed by reflection. The dependence is
ethan Dy gikial2r42d) ihealzs+2e) Li 55, | (Riz + Ks) Ly
Qn 2

In this case both incident waves and scattered waves traveled through

the canopy. Thus
FOO @)
ike N

eikr L; &, 5.) Lyla yp py Ha ik.

=— ye fn [ie +h] folks, kie Renty @— thes

j=l
ji Li) F (pp) pibiszy—ikeet)+2ikyed
+ sine | (ki: — ks) fplks, hile" a .
. Lis op py thea; —ikieay 2ikea (2) +d)
+ sine | (his — fse)GE Fry fs hae ets bes
. Li\s 7p 3 . 9 '

+ sine [is + we) F ror (ks, ki)etes* eth 6H hex nosh (12.2.6)
where fi, furs fro: and f,,, are field vectors that depend on cylinder ra-
dius a; and is polarization dependent on the scattering characteristics of
the cylinders and the reflection by the half-space boundary. They will be
derived rigorously in Section 2.2. The subscripts v and r denote volume and
reflection, respectively.

In the following, we shall assume that (1) the position of z; is z; =
L;/2—d (that is, the cylinder is attached to the boundary of the dielectric
half-space) and (2) the length of the cylinder is Gaussian distribution with
mean Ly and standard deviation o7,. The probability density function (pdf)
is

1 (L—L,)?
p(L) = —— exp [-“ ; (12.2.7)
V2roL 207,
The probability distribution of length will smooth out side lobes that may
exist in the conical scattering pattern. The radius of the cylinder is equal to
constant a for all the cylinders. The pdf and joint pdf of horizontal positions
are independent of lengths of cylinders. Thus, letting z; = L;/2—d in (12.2.6)
--- PAGE 616 ---
598 12 MULTIPLE SCATTERING BY CYLINDERS
gives
a(t elk
BOG = —F ) (12.2.8a)
where
1 N
FY = eh F(15) (12.2.85)
jal
is the first-order scattering amplitude of the canopy, and
+ L; 4 Lj|= 9
F(Lj) = Betton [se +4 kn) | Fye thes thes) es/2
a
. Li) ilkse-kes)L,/2
+ sine | (iz — kas) Ff ype eRe
ine | (k LG) ilkoe -hiz)bs/2
sinc | (hie — Kes) S| Fryer Bo
Ljjs 4 2
+ sinc [«. + tn) 2 Frvreilhs meonel (12.2.9)
The pdf and joint pdf of horizontal positions of cylinders are as follows. Let
the cylinders be in clusters with N, cylinders per cluster. Hence the number
of clusters is VN, with
N
Ne == 12.2.1¢
= (12.2.1
Note that N and N; are large numbers while Vv, may not be a large number.
Let the cluster center be at (to. Ya) with a = 1,...,N,. Each cluster lies
within a radius R,. Thus the pdf and joint pdf of clusters are
1
P(Ges Ya) = A (12.2.11)
where A = L,Ly is the area under observation and Ly >> A, Ly > r. The
joint pdf of clusters is
_ 2) _ Ir(PasBp)
b2(PosBp) = a (12.2.12)
A
where g, is the pair distribution function. We also disallow interpenetration
of clusters so that
IParPg)=0 for |Py Pal < de (12.2.13)
where d, is the minimum separation of the centers of two clusters. Within
each cluster a, the positions of the secondary scatterers are at Dy + Pojs
--- PAGE 617 ---
§2.1 Scattering from Vertical Cylinders: First-Order Solution 599
jal. No.
i 9
(a3, Yaj) = (12.2.14)
lc
where A, = 7R? is the area occupied by a cluster.
= = )_ 9s(PajrPat) 5
P2(Boj:Pat) = 45 (12.2.15)
Ale
Note that for the random media problem, NV, N., and A — oo while Ns and
A, may not be large number.
The pair functions are normalized quantities so that the magnitudes are
Ne Ne
of the order of unity. The summation of (12.2.8) is then replaced by > > :
a= j=l
1 Ne Ne
FO ashi) = YO he PoP F Las) (12.2.16)
o=1 j=1
We first evaluate the coherent field by taking the average of (12.2.16)
(F (ks, fi) = NeNo(etBtr'@ Por) F(Leaj)) (12.2.17)
where
(ciel tBas)) = i [o. ciFto Da z/ Tig, eter Pas (12.2.18)
Aj °* Ac Ja, 9
Assuming a rectangular area A = L,Ly, we have
Kay(B +2. Kerk kay. ~
(clue Pa “Pos)) = sine [s= =| sine = | X (Rap) (12.2.19)
where
— 1 eg,
X (Fay) = 3 I, ; Api etBee Pos (12.2.20)
Depending on clustering size Ay, the integral of the exponential term in
(12.2.20) may not undergo large phase fluctuation over the cluster area.
From (12.2.20), X(0) = 1. For Lz and Ly — oo, the sine terms in (12.2.19)
are sharply peaked at kay = kay = 0 so that we can replace kp by 0 in
X(kap) in (12.2.19). Thus
ae . L
(efFao(Ba+Pa3)) — sine [| sine (‘| (12.2.21)
--- PAGE 618 ---
600 12 MULTIPLE SCATTERING BY CYLINDERS
Hence
ml) p 5 Kae Ly kayLy| >
(F (ke, ki) = Nsine [*s*] sine [| (F(L)) (12.2.22)
Using (12.2.7) and (12.2.9), we have
=z 1 = =
(FL) = 5 {W(—(hes + Bis) Fo + W (hie ~ es) For
+ W(lioe — is)Foy + Whos + his) Fro hel) (1.2.23)
7 1 ~ P . al ;
W(a) = ia {cite op /2 1} = (LsineS ela /2) (12.2.24)
‘The bistatic scattering coefficient is
a ey _ am(lFP)
he, hj) = SMELT
Wks ki) Acos 0;
The contribution of the bistatic coefficient is the sum of the coherent field
© contribution and the incoherent field contribution, 7 :
yarry (12.2.25)
For coherent field contribution,
we _ 4a\(F)P
' Acos 6;
Ani L, kay =
= cosh, Nsinc? (i *) sine? (a 2) \(F(Z)yP (12.2.26)
where n4 = N/A is the number of cylinders per unit area. Thus the coherent
intensity is sharply peaked in the specular direction and depends on the total
number of scatterers N, the size of the area L, and L,, and the shape of the
area under observation. The incoherent field is
F =F -(F) (12.2.27)
The incoherent ficld can contain partial coherent effects. The bistatic scat-
tering coefficient of the incoherent field is y’ with
«gy _ atlF lbs ks)
(ks, ki) = ees 12.2.28
bank) = See (22.2.28)
The incoherent bistatic scattering coefficient, on the other hand, as shown
by following calculation, depends only on the intrinsic properties of the ran-
dom media (e.g., m4) and does not depend on parameters such as N, Lz,
and L,. Thus the 7’ obtained with Monte Carlo simulations is a physically
meaningful quantity that can be used for practical applications.
--- PAGE 619 ---
§2.1 Scattering from Vertical Cylinders: First-Order Solution 601
Next we form [FOC k,)|?, which gives a fourfold summation of
La Xj Ug X- This can be separated into three terms: (i) a = 8, j = 1,
scattered field and field conjugate from the same cylinder, (ii) a = 8, j £1,
scattered field and field conjugate from the same cluster but from different,
cylinders in the cluster, (iii) a # 3, scattered field and ficld conjugate from
cylinders of two different clusters. Thus,
A)
(F Ghashs)?)
Ne Ne Ne Ne Ne
= VF Les?) + OY (op (tap Bas ~ Bar)) FE)?
a=1 j=l a=1 j=) [=1
j#t
Ne No Ne Ne
+ LLY Vee (tap (Ba + Pay) — Bs + Bar))))  MFL))P
a=] p=1 j=l I=1
aZ8
(12.2.29)
Using the definitions of pair distribution functions of cluster-cluster gp) and
cylinder-cylinder in the same cluster g,, we have
(lye vy
(PO (hy, f)) =
IF a 9s (Daj: Bat)
NAEP) + NeNa(Me 1) fO dhag fd =P
Ac Ac c
exp (tap * (aj — Pat) F(Z)?
+ NNe~ IN? fp [apy 2 Pex2o?
A A A _
“exp (Hap Ba — Ba) |X Bap)? CFE) (12.2.30)
The pair functions over clusters gp(P., fg) are to be integrated over a large
arca A as indicated in (12.2.30). Besides the nonpenetrating condition of
(12.2.13), the function must asymptotically approach unity because the clus-
ter positions must be independent if they are far apart. Thus,
lim 9p(PasPp) = 1 (12.2.1)
Pa-Bs!r00 .
Furthermore, we assume that it is translational invariant. 9p(Po: Pa) =
9p(Pa — Pg). On the other hand, gs, the pair function within a cluster, ex-
tends over a smaller area A, and does not share the same properties as gp.
We write gy = (gp — 1) +1 in (12.2.30) and let N. and N — oo. We also
make use of the translational invariant property of gp :
--- PAGE 620 ---
602 12 MULTIPLE SCATTERING BY CYLINDERS
PO py) = ay
(|B (ks, ki) ?) = N(\f(L))?)
UN _ f 9s(PajsPat) iReg(3..—B..) 1 ‘
NON =1) f aay fags A PEgePat er tPos-Pad CFL)
JA. ‘Ac ¢
Nef Z E35 Z, \2F 2
bp J PGP) — V exp(ikdp -P)|X Rap) \CF(E))|
A Sa
s _ exp (ikdp + (Ba — Bg) ey
ent fap, [ap Ee PoP) xe, \ Gu 12.28)
The last term in (12.2.32) is the coherent intensity. Subtracting it from
(12,2.32) gives the incoherent intensity, which, however, can contain partial
coherent effects. Thus the bistatic intensity of the incoherent field, under the
first-order approximation, is
a 4n sri
1 Osh) = Sa {na(lF@e
, ’  9sPaj>Pat) Zo ity)
nate 1) f aay f dps 229P2 exp (iEdp (Pus ~ Pai) (FOL)!
e
snk foto) — eX ap PIAL)? Y (12.238)
A
As is clear from (12.2.33), the bistatic intensity of the incoherent field only
depends on intrinsic properties of the random media such as quantities like
na, L, gs, and gp. The value of 7’ obtained by Monte Carlo simulations can
be used for practical applications. The integral of g, is only over the cluster
size and can be performed numerically. The integral of gp is only over the
region of A that gp is not equal to 1. That is an area much smaller than A,
and the integral of gp — 1 can be performed mumerically.

We note that the first term in (12.2.33) is the independent scattering
result. The second term is the correlation due to clustering effects for a single
cluster. The last term is due to correlation between clusters. We note that for
N, > 2 the second term due to gs gives a positive contribution, giving rise to
enhancement of scattering due to clustering. The larger the N,, the stronger
the effect. Physically, this can easily be interpreted by the fact that when
scatterers form a cluster, they form a larger particle and can give rise to a
larger cross section. The last term in (12.2.33) is due to correlation effects
between clusters. It is usually negative (e.g., gp — 1 = —1 for |p| < dinin).
giving rise to less incoherent scattering. We illustrate the results with the
following simple example. Let gs = 1, and A, is a circular area with radius
--- PAGE 621 ---
§2.2 First- and Second-Order Solutions 603
Re.
_, _f0 if fp] <2R,
woo) ={ 9 Plone (12.2.38)
Equation (12.2.34) is known as the hole correction and is valid when the
density of clusters is not too large. Using the integral identity
[eee Jo(a) = vJy (x) (12.2.35)
we then have
> 2
X (Kap) = Il kap Re 12.2.8
Bin) = GI hip) (12.236)
Hence
a 4n spy 2 srry
Vi hey. ey) = ——d na (iF(D)2) + |. :
1 (abs) = SG, MAF?) + |p Fa bap RFD)
9 ATR (hap2R,
. [naire -1)- ng | (12.2.37)
kap
where the 2, argument in the last term of (12.2.37) arises from the fact
that the hole correction has radius of 2R, for the hole. It will be shown in the
next section that the analytical result of (12.2.37) agrees well with Monte
Carlo simulations.
2.2 First- and Second-Order Solutions
Tu this section we formulate the Foldy-Lax multiple scattering equations of
the problem. A half-space Green’s function is used that is also expressed
in vector cylindrical waves. We also derive the first-order solution and give
expressions of f,, for: fpy: aud fy, that were needed in Section 2.1. The
incident field is given by (12.2.1). The sum of the incident field and reflected
field is
Eine + Eves
= (Euiti + Enilas)
+ (Soi (hiz) Bu:0(0;,6,) + Ro(hi)En0(0,64)) Ade? (12.2.38)
where
Ki = kick + kiyi) — bizd (12.2.39)
Ki = Bint + kiy + hick (12.2.40)
--- PAGE 622 ---
604 12 MULTIPLE SCATTERING BY CYLINDERS
Both the incident fields and the reflected fields are expressed plane waves in
(12.2.38).

Consider cylinder | centered at 7). The field exciting cylinder I is the
sum of incident field, reflected field, and scattered wave from other cylinders
j with j #1. First we express the incident field and scattered field in terms
of vector cylindrical waves centered at 7).

Eine + Ere f
iK 7, 1 - _ —
= eer [Bag SO(-Hre ie"? Rg Nn (hips —hizsF — 7)
it
1 A —
+ Bris Do(—1yre ine"? Rg Ma kip, kes? — n|
thip
oo E, _
— GikeFr 2ikied [soz So(-1)"e Mi")? Rg Ny (Rip, hie. F — Fi)
kip &
+ Rois So(-1)tei2 i")? Rg Mn (Kip kiss? —Fi))— (12.2.41)
ikip 7

To determine the exciting field of cylinder J and to find the scattered field
from cylinder j to cylinder 1, we use a procedure that includes the following
steps:

{i) Write down the expression of internal field for cylinder j in terms of
vector cylindrical waves with unknown coefficients.

(it) Use Green’s function to find the scattered field from cylinder j. The
Green’s function is the half-space Green's function. The half-space
Green’s function includes the direct scattered ficld and the scattered
field that is reflected by the half-space boundary at z = —d. The scat-
tered field is expressed in terms of vector cylindrical waves centered at
Fj.

(iii) Use translation addition theorem to express the vector cylindrical waves
from cylinder j in terms of vector cylindrical waves centered at cylinder
1.

(iv) Equate exciting field coefficients of cylinder J to an incoming wave on
cylinder | that includes incident, reflected, and scattered field from all
cylinders j, j = 1,2,...,N, except j = /. Then obtain self-consistent
multiple scattering equations.
--- PAGE 623 ---
§2.2 First- and Second-Order Solutions 605
Step i: The internal field inside cylinder j is assumed to have the following
form:
Fp) + a M aya
mo [ a, [689 (KL) Ro Mw (Koy BF —75)
ni=—co
+ QO (KL) Rg Nv (Kye KeoF = 75)] (122.42)
xo OS
iwpH?? = y i» | dk’, [cP (yng Nn (ky kes? 75)
n'=—00 ed
N WZ —— ;
+ LO (iL) Rg My (kiyys Res F — 7)|(02.2.43)
where Ae. ) and 0) are unknown internal field coefficients to be deter-
mined self-consistently. In (12.2.42) and (12.2.43), kf, = \/k2 — k?.
Step ii: The scattered field from cylinder j is
BE) (?)
—L5/2+25 Qn =) _ =
- | dz [ 1 99,05} 2HPpp, x HOF) - (GolF¥”) + Gres P72)
<14/2+2, JO
+ Pop, x BOF) -V x (Goer, P) + Grey (F, 7)) \ (12.2.44)
where Ppp, and dp,, are polar coordinates with center at p; (Fig. 12.2.3).
In (12.2.44), Go + Greg is the half-space Green’s function which contains
the reflected part that denotes a scattered field that is further reflected by
boundary at z = —d. From Chapter 5, Section 2.2 of Volume I, we have the
reflected part of the Dyadic Green’s function in plane wave representation
7m ee i ~ | . EF. ike
Greg (F.7") = gia [ELAM EK.)e Ke
+ RMR Je®Fh( hee" } (12.2.45)
where
RTP (kz) = Ror(kz)e7"4 (12.2.46a)
REM (k,) = Soi(ke)e™=4 (12.2.468)
for the half-space case with boundary at z = —d. Using the transformation.
between vector plane waves and vector cylindrical waves as given by (2.1.26)
--- PAGE 624 ---
606 12 MULTIPLE SCATTERING BY CYLINDERS
and (2.1.25), we have
Gres FF)
_ if dh,k,— ihort g2ikoed S (a)
am Jo kockp? 7
. [Ror (koz)Rg Mn (Kp: Koes F — Fp) Mn (kip, hoz,” —F))
+ Sou(kox)Rg N -nlkps kozsF —F;)Rg Nn(kps kos?” -7))| (12.2.47)
For the free-space Green’s function. G, we have
Golr,7')
i poo 1
-2y ay f thes [By Mn (hop, Bes 7) Mn (Kop: —hiesT! — Fy)
n=—o0 hed “op
+ RyNol(Kop, ke. F —F))N—n (Kop; —kesP —F; )} (12.2.47b)
Integration in G, is over [25 dhs because the direct scattered wave from
cylinder j to cylinder / includes both upward and downward going waves.
However, integration in (12.2.47a) for Greg is over fy° dkpky because the
reflected wave only has upward going waves. Substitute (12.2.42), (12.2.43),
(12.2.47a), and (12.2.47b) in (12.2.4). Integration over ddpp, gives n’ = n.
Also since F is on the surface of the cylinder, we have |p — p,| = a. We then
have
Bp P=
od OO oO
> (-2) | dk, / dkzsinc (« - we)
note \ 2A) Jaco S00 2
{Myo (kops bss P 75) [00 (RL) Rg AN (op, Bes Bpps es Qj)
4h OL) Rg AM (Kops Res Reps hes; )
+ Ni Cops bes = 19) [el (RL) Rg ARM (Kops es Bpps Bes 43)
+ LORY Rg ANN (kop, Kes Ryys hes ) }
eS L;\ [* ky ai kon +k,
+ 2) / an, [ dky 2 Po +4 sine ((“3*) ts)
>a ( BI) bce "Io Pho 2 ;
. {Rg Muy (Kp, ozs — F)Roi (Koz) [PO (KL Rg AMM
--- PAGE 625 ---
§2.2 First- and Second-Order Solutions 607
«(Rips Rios fps hes a3) + OY (Rg AM (ky, Rios. Rp, ks a;)|
> ow a\e M NM
+ Ra Nw(kpskoes? ~74)S01 (ox) [e609 (HL) Rg AN™ (kp, Foss Ry es 43)
N NN
= LD (RL) Rg AB (op, hos, Rhys es a3)| } (12.2.48)
where the coupling coefficients Rg A,y are as given in (1.6.64)-(1.6.67) from

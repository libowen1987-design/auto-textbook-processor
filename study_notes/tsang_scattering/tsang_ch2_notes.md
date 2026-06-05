# Tsang《Scattering of EM Waves》Chapter 2

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 2. The advantage of this approach is that the mutual interactions
between the branches are included. The scattering from a layer of trees
overlaying ground is calculated by assuming each tree scatters independently.
As shown in Section 3, this assumption has compared well with the coherent
addition approximation through the C-band, the L-band, and the P-band.
--- PAGE 688 ---
670 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
5.1 Formulation of Discrete Dipole Approximation (DDA)
Method
Using the DDA equations from (2.3.48) of Chapter 2, we have
- = = N -
Pi Oj Fine na Dy .
Pi Re AV)Ayy » 3.5.1
cAV AV“? CAV ele Min AV (13.5.1)
where € is the permittivity of the background medium, and
Bs = ott + any + 01232 = (= - 1) 5, (13.5.2)
Bix 1
a 13.5.3
AV 14(2-1 (Lz, _D,k) (185.3)
Biy 1
— a 13.5.4
AV 14 (@—1) (Ly — DF) (18.5.4)
Biz 1
Pe 13.5.5
AV 14 (@-1(L.-D.P) (1885)
and AV = d,dyd:.
Tn the case of cells of circular cylindrical shape of radius a and length l,
the corresponding results of L,, Ly, Lz and D,, Dy and D, are
U .
Lz =Ly= ae (13.5.6a)
L =
L,=1- Gap (13.5.6b)
ikal 2 (t+ VP + 4a?
D, = Dy = "4 = {ve +42 -1h 4 © inf YET") 135.60)
° 6 8 4 2a
ikal a? (1+ VP + 402 —
Di = 4 5 ne (13.5.6d)
and AV = za?l. _
The equation for A(7,7’) is given in (2.3.8) of Chapter 2. The value of
A(?,?"), for F =7; and F = 7;, (Fi #7;) is expressed as
Ai = A(Fi, 7) (13.5.7)
However, these may not be accurate enough when 7; and 7; are in the neigh-
borhood of each other. Accuracy can be improved by numerical integration
over the cell Vj centered at 7;. Thus we can define a neighborhood distance
--- PAGE 689 ---
§5.1 Discrete Dipole Approximation (DDA) Method 671
rq so that
1 [ Riz. -! =
= = | GA(F,.7") for 7; —F;| < 1a
Ay = {= Iv, ‘ vous (13.5.8)
A(Fi,F;) for |Fi -—73| > ra
The expression of Ay; in (13.5.8) will still preserve the translational invariant
property so that the FFT can still be taken when the matrix equation is
solved by iterative method.
After the solution is obtained, we have the solution of the reduced dipole
moment ); for every cell. The electric field at every cell F; is given by
a 1 D,
EE; = = 13.5.9
1 (@ = 1) AY ( )
Note that we only have to include those cells which have €p; 4 €. The matrix
equation (13.5.1) is of dimension 3N x 3N, where N is the number of small
cylindrical subcells. The cylindrical subcells may have different lengths and
radii in tree scattering. The factor 3 arises from the x, y, and z components
of the polarization vector.
After the matrix equation (13.5.1) is solved, the far-field, scattered field
in the direction kg is
ikr N ZB.
Rix € 2 (5 « ij ike F, Pi tA
B= (i065 + heh, ‘Le cay, 4M (13.5.10)
Based on (13.5.10), the far-field scattering amplitude matrix can be com-
puted readily.
The time-averaged power absorbed is equal to
1 &
BZA y, P
(Pa) = 52 lel AV, (13.5.11)
i=l
where Shi is the imaginary part of cp; for the ith cell. In terms of dipole
moment of each cell. we have
1 1 p, P
ip.) — +. WAY. i P
(Pa) 2° 2A F ze | (13.5.12)
€
‘We have verified the validity of the discrete dipole approximation method by
calculating the backscattering coefficients from a vertical cylinder of length
1 = 1), radius a = 0.05, and permittivity «, = (3 + i0.5)e [Chen, 1994].
--- PAGE 690 ---
672 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
The method is further validated by comparing its results with those
of another method of moment code for a body of revolution based on the
surface integral formulation. The results agree well with each other. Energy
conservation is checked by comparing the extinction coefficient obtained by
the optical theorem and that by the sum of the total scattering coefficient
and the absorption coefficient. The details of the validity of our numerical
code can be found in (Chen, 1994].
5.2 Scattering by Simple Trees
In the following study, the trees to be used as our scattering objects are
grown by using the stochastic L-systems discussed in Section 2. The input
file to the L-systems is the input file B given in Section 2.3. Figure 13.2.3
shows one of the generated trees. Here, we assume that the unit used in the
above process is one wavelength.

Three hundred trees are generated. The maximum height of these trees
is 2.47. The shadow of each tree can be put in a circle of minimum diameter
0.632. We define a shadow cylinder for each tree as one which has a height of
the maximum height of the tree and minimum diameter to cover the shadow
of the tree. We define the local fractional volume as the total volume of all
the branches of one tree divided by the volume of its shadow cylinder. The
averaged local fractional volume for these 300 trees is f,y = 2.89%.

In each realization of our calculation, ten of these trees are put into a
pixel of the size of 3A x 3\. The positions of the trees are random, but the
shadow cylinders of the trees won’t overlap each other. The fractional area
fa, defined as the sum of the shadow areas of all these ten shadow cylinders
divided by the area of the pixel, is 0.346. Thus the fractional volume occupied
by the branches in the forest is f = fur fa = 1.0%.

Each pixel is assumed to have a reflective boundary of permittivity
(16+ i4)eo. The following three scattering mechanisms are considered in the
presence of the reflective boundary (Fig. 13.3.1a-c). The first term represents
the scattering from the incident direction by a scatterer into the scattered
direction. The second term represents the scattering of the reflected wave
by a scatterer into the scattered direction. The third term represents the
scattering from the incident direction by a scatterer, and the wave is then
reflected by the boundary before going into the scattered direction.

The backscattering coefficients calculated using the discrete dipole ap-
proximation ol) can be expressed as follows:
--- PAGE 691 ---
§5.2 Scattering by Simple Trees 673
(D) Am PN 1 ere
Fra ( — Gist + 5B Bi) = DT (sa? Oi + O37 — Os, 61)
ttree=1
+ £8) (0;, 7 + $15 0:,6:) Ra (Oi)
+ Rg(4i) fee ~Gi,7 + dis m — 8:, G3) ?) (13.5.13)
Here A is the area of the pixel where the N; trees are located. The scattering
amplitude is feo for the ith tree, Ry is the reflection coefficient for the
incident polarization, and Rg is the reflection coefficient for the scattered
polarization. Note that in the second scattering mechanism, the wave re-
flects at the boundary first, then scatters at the object. Thus, the reflection
coefficient is Ry. In the third scattering mechanism, the wave scatters at the
object first, then reflects at the boundary. Thus, the reflection coefficient is
Rg.

In the coherent addition approximation (CAA), as given in (13.3.30),
each branch is treated as a scatterer and the scattering amplitude is cal-
culated. The total scattered field is obtained by adding the scattered fields
from the branches coherently. In the independent scattering approximation,
each branch is treated as an individual scatterer and the scattering ampli-
tude is calculated. The scattered intensity for the independent scattering is
assumed to be the sum of the scattered wave intensities from each scatterer.
The expression of scattering coefficient is the same as that given in (13.3.31).

We use a relative permittivity of 11+74 for the branches in the following
numerical simulations. Figures 13.5.1, 13.5.2, and 13.5.3 show the backscat-
tering coefficients ayy, Tn, and opp, respectively, which are calculated by
discrete dipole approximation and are compared with those of coherent ad-
dition approximation and independent scattering approximation. It is ob-
served that the coherent addition approximation gives good estimates of the
copolarized backscattering coefficients (both vv and hh). The differences be-
come larger and can be 17 dB for the case of cross-polarized backscattering
coefficients. This is because the interactions between branches and the main
stem give rise to cross-polarized backscattering coefficients which cannot be
captured in the CAA. In the CAA, the internal fields are assumed to be the
same as that of a single scatterer. The polarization current induced will be
dictated by the incident field direction. When the polarization current ra-
diates in the scattering direction, depolarization is usually small. However,
in the volume integral equation with discrete dipole approximation, mutual
coherent interaction, especially in the near field, can significantly change the
direction of the internal field and the polarization current. This creates a
much larger depolarized scattering cross section.
--- PAGE 692 ---
674 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
sl _ discrete dipole
=: indopendent scattering
10
saranaseoherent aditon
Bp —————
5 > a
Bre fo
bo ONY
Sos: 4
3 | |
8 -20|
{
28 1
30} |
aa) 70 eo 20 40 50 4,
angle of incidence (deg)
Figure 13.5.1 Comparison of backscattering coefficients oy» for a two-layer medium by
discrete dipole approximation, coherent addition approximation, and independent scattering
approximation, Fractional yolume f — fyfa = 1.0%, €s = (11 + é)co. The scattering
layer has a thickness of 2.47A and the underlying half-space is Hat and has a permittivity
soit = (16 + 4)eo. The number of branches for each simple tree is 11.
ee oo
‘8 _____s iscroe dipole
a =~ indopandent sattarng
sess seoherent ation
g4
5 4
2 J
B |
2-10 |
Bas J
Boo ae
al ae
ee Tee
35
0 10 2 30 30 30 cd
angle of incidence (deo)
Figure 13.5.2 Comparison of backscattering coefficients op for a two-layer medium by
discrete dipole approximation, coherent addition approximation, and independent scattering
approximation. Fractional volume f = fyrfa = 1.0%, €5 = (11+ i4)ey. The scattering
layer has # thickness of 2.47A and the underlying half-space is flat and has a permittivity
€soit = (1G + i4)eg. The number of branches for cach simple tree is 11.
--- PAGE 693 ---
§5.2 Scattering by Simple Trees 675
ast discrete dipole i
sss independent scatering
10-
sesso !eoherent addon
a5
Boh
§ _-
2 sp--- >> eee
8
2-10
§45)
%
$20
25+ 4
20 |
4g-——- 1» - ____]
7 70 20 30 40 Ey 80
angle of incidence (deg)
Figure 13.5.3 Comparison of backscattering coefficients op), for a two-layer medium by
discrete dipole approximation, coherent addition approximation, and independent scattering
approximation. Fractional volume f = frfa = 1.0%, €5 = (11 + id)eo. The scattering
layer has a thickness of 2.47A and the underlying half-space is flat and has a permittivity
€s0i1 ~ (16 + i4)e. The number of branches for each simple tree is 11
Figures 13.5.4, 13.5.5, and 13.5.6 show the bistatic scattering coefficients
vv, Th, ANd Opp, for an incident angle of 45°. Again, the results are in good
agreement for co-polarizations (vv and hh) between discrete dipole approxi-
mation and coherent addition approximation. There are large differences for
the cross-polarization (vh). It is also noted that there is a maximum at the
backscattering direction for the bistatic scattering coefficient of vv but not
for that of hh and vh. That is because the contribution of the central cylin-
der to the vv-polarized scattering wave is dominant and has a maximum at
the conical direction which is reflected to the backscattering direction. How-
ever, for the hh-polarized wave, the contribution comes from the all branches
which are randomly distributed along the 2-direction. The scattering pat-
tern depends on the structure and does not necessarily have a maximum
at the conical direction. The scattered wave of cross-polarization is due to
the inclination of branches and mutual interaction and has a more complex
scattering pattern.
--- PAGE 694 ---
676 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
ce
a
5 i ee / \
/ _ “4 i
= f \ cone CAA | in
g : Ay.
gy i \ fois
z i \ \
Ele AL AS cio
ploAl ME in,
cara . fy ON:
Be Na oy
sf | ‘ fi | i
roa | ye en eh
8 \! aA fy 4 \ ¥
g Yoo PING
hs IP
Hy [ho :
N
20) of H
a a rT
is ee ‘00
‘Scattering Angle (degree)
Figure 13.5.4 Comparison of bistatic scattering coefficients op» for a two-layer medium by
discrete dipole approximation, coherent addition approximation, and independent scattering
approximation. Incident angle is 45°. Fractional volume f = fur fa = 1.0%, ce = (114 iA)eo.
‘The scattering layer has a thickness of 2.47) and the underlying half-space is fat and has a
permittivity €4o;2 = (16 + i4)¢o. The number of branches for cach simple tree is 11.
98)
/\
\ aN |
20) i\ i o4
a f\ f \ 1] |
e] hoy yf 7 a Se
= seh Vo
‘S -25) fom “ “7 Vv
3 poo ee
3 Py sy a
2 fo\d : |
4 {oye i |
fo of VO Trae
8 nA we
yo :
g iv _DpA nl
35> aan
ind :
: seen CAM . |
7 re na |
a a a a ee ee
catering Angie (gree
Figure 13.5.5 Comparison of bistatic scattering coefficients oy, for a two-layer medium by
discrete dipole approximation, coherent addition approximation, and independent scattering
approximation. Incident angle is 45°. Fractional volume f = fyi fa = 1.0%, €s = (11+ é)eo.
‘The scattering layer has a thickness of 2.47 and the underlying half-space is flat and has a
permittivity esi = (16 + ideo. The number of branches for each simple tree is 11.
--- PAGE 695 ---
85.3 Scattering by Honda Trees 677
Np ee
DOA f\
: A uw ff \
e [\ fo \ |
s ; \ sees CAA i \
f \ j
2 4 { \ H Ww |
5 i; 4 i \
3 { o- fo- \
hn pen
:* { \ v ‘ Lo ‘
= i ! i .
e \ | NN al 1 \ ‘
: aes tA
3" Vi horas ut
3 aff Apes
a | ve ‘ce
a5 g “ 4
a a a a a a a 4
Scaltering Anglo (degree)
Figure 13.5.6 Comparison of bistatic scattering coefficients opp, for a two-layer medium by
diserete dipole approximation, coherent addition approximation, and independent scattering
approximation. Incident angle is 45°. Fractional volume f = fy fa = 1.0%, ¢s = (11 + i4)eo.
The scattering layer has a thickness of 2.474 and the underlying half-space is flat and has a
permittivity ¢soi1 = (16 + i4)éo. The number of branches for each simple tree is 11.
5.3 Scattering by Honda Trees
Next we use DDA to calculate scattering by Honda trees. The Honda trees
are generated based on L-systems. Figure 13.5.7 shows the growth process of
a Honda tree up to the 5th generation. First, we have a cylinder. Then two
shrunk cylinders are generated from the top. One is in the same direction as
the mother branch. Another one has a branch angle of 45°. This process is
repeated to each end branch, and the next generation of the tree is obtained.
Stochastic process can be introduced in the L-systems. For a Honda tree,
the structure is controlled by the parameters such as contraction rate, branch
angle, divergence angle, and width decrease rate. We use random number
generators to randomize the parameters and achieve the randomization of
the tree. Four Honda trees of the 6th generation are shown in Fig. 13.5.8.
Each tree has 63 branches. The trees are different from each other while
maintaining the same characteristics. _
The scattered field in the direction k, can be written as
zs et 8 ine
E(7)= Toph (hss hi) - Ey (13.35.14)
dar
where E,,”* is the incident field in the local coordinate systems and F is the
--- PAGE 696 ---
678 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
Figure 13.5.7 Growth process of a Honda tree.
Figure 13.5.8 Different trces but the same characteristics, each tree with 63 branches.
scattering amplitude matrix for the tree given by
_ Ree anon AD
F (ks, bi) = 2 Se li ‘Piv s ee] (13.5.15)
6 FF hs Diy Ns Din
where p;,, and p,, are the dipole moments induced by a unit vertically po-
larized incident wave and by a unit horizontally polarized incident wave,
respectively. N is the total number of discretized cylindrical cells of the tree.
The effects of ground surface are taken into account by introducing
boundary reflections. The four scattering mechanisms are as follows: (a) the
scattering from the incident direction by a scatterer into the scattered direc-
tion, (b) the reflected wave that is subsequently scattered by a scatterer into
the scattered direction, (c) the scattered wave of a scatterer, which is subse-
quently reflected by the boundary into the scattered direction, and (d) the
scattering of the reflected wave by a scatterer that is followed by a second
boundary reflection (Fig. 13.3.1).
The bistatic scattcring cross sections gag of a single tree are calculated
--- PAGE 697 ---
§5.3 Scattering by Honda ‘Tres 679
by three approaches:
Coherent Interaction Model (CIM): Each tree that consists of many
branches is treated as a single scatterer. Maxwell's equations are solved using
DDA for the entire tree.
CIM , ,
OY 8. 5: i, 1) = (Fira Oss G53 — 915 01) + Fe-(sy $5391. :) Ra(Oi)

+ Rg (Gs) Faa(™ — Os, $s) 0 — 6; i)

+ Ral.) Fal — 9, 6636, 61) Ra(6:)2) (13.516)
where the phase shifts due to reflections associated with the four scattering
processes are included in the definition of Fa.

Coherent Addition Approximation (CAA): Each branch is treated as
an individual scatterer. The total scattered field is obtained by the sum-
mation of the scattered fields from each scatterer. Relative phase shifts are
included. Mutual interaction is excluded.
Ny
CAA Salis zo
On (5, 638i, 01) = Y(LS2 Os. G05 7 — 8: di) exp(Ran -Ti,)
i=l
+ P52 (06.0658: Gi) Ro (Bi) exp(iRaa -Fs,)
+ Ra(Os) f90(7 — Os, 665 — Oi. 6) exp(ihag -Fi,)
+ Ras) Fyn (# — 9x Osi 0%, 4) Ro(Os) exp(iRas “F%,)P) (13.5.17)
where expressions for kg), kag. kag, and Rag are given in (13.3.16) (13.3.19).
Independent Scattering Approximation (IND): Each branch is treated
as an independent scatterer. The total scattered intensity is the sum of the
scattered intensities from each scatterer.
Ne
a _—
OY (Bs. 0538: 01) = SUF Oa. bait — Bi. a)?
i=l
(in) 2
+ fsa (Os, $s; 9i, i) Ra(6i)|
+ |Rg(0.) £52 (oe — 5, 637 — 8.64)?
+ |Ra(Bs) fy.) (w — G5, 06; Bi. 4) Re (Or)/") (13.5.18)
Tn (13.5.16), Fzq is the scattering amplitude of the whole tree, while in
(13.5.17)-(13.5.18), the scattering amplitude of the ,th branch of the trec is
{$0 Bis the reftection coefficient, and Nj is the total number of branches.
Equation (13.5.16) is the exact solution of wave scattering by a tree. Both
--- PAGE 698 ---
680 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
(13.5.17) and (13.5.18) are approximate methods. CAA gives a better ap-
proximation than independent scattering since it includes the relative phase
shifts among branches.

Our scattering objects are the Honda trees (as shown in Fig. 13.5.8) with
63 branches generated by using stochastic L-systems. The central branch
consists of six branches of decreasing sizes. Thirty trees are generated in this
manner. The input file for the L-systems is given as follows:

#define maxgen 6

#define r; 0.85+0.1*rand(1) /* contraction ratio for trunk * /

#define r2 0.55+0.1¥rand(1)  /* contraction ratio for branches + /

#define ay 44 + rand(2) /* branching angle from the trunk «/

#define ay 44+ rand(2) /* branching angle for lateral axes «/

#define d 127.5 +rand(180) —/* divergence angle */

#define w, 0.85+4+0.1*rand(1) /* width decrease rate x /

START : A(1,10)

pr: A(l,w) : « — > I(w)F())[& (a9) B(L «re, w * w,)]/(d)A(L «ry, « wy)

po: B(l,w) :* — > "(w)F(D[-(a2)8C(L # ro, w * w,)|C(L r1,w * we)

pa C(l,w) 2 * — > Vw) F() [+ (a) $B(L * rp, w * wp) |B(L« ry, w *w,)
The maximum height of these trees is 5.18\. The bistatic scattering cross
sections for both co-polarization and cross-polarization are calculated by
using (13.5.16)--(13.5.18) and are averaged over 30 realizations of trees. We
plot the normalized cross section ¢/A? in the dB scale.

Figures 13.5.9 and 13.5.10 show the bistatic scattering cross sections for
co-polarizations oy, and o},, for an incident angle of 45°. The results for CIM
and CAA have a distinct scattering pattern. The result for IND, however, is a
smooth curve. The results are in good agreement for both vv and hh between
the coherent interaction model and coherent addition approximation. As
noted for the case of simple trees in Section 5.2, there is a maximum at
the backscattering direction for the bistatic scattering coefficient of vv, but
not for that of hh. There is no maximum at the backscattering direction of
vv for IND, because we treat all 63 branches as independent scatterers. For
example, the central branch consists of six independent scattering branches
of shrinking radius that is a result of L-systems structure.

Next, we compare the results by redefining the branches that continue
in the same direction as one branch. ‘To account for the decreasing radii, the
length of the modified branch is the sum of the lengths of the branches. The
--- PAGE 699 ---
§5.3 Scattering by Honda Trees 681
10¢
d om
é sonnet OAM
zo tna
&
i 5
$0 . Av
3 - A j' ‘ .
al CEE ae \
“Soo 2060 0-200 a0
Scattering Angle (degree)
Figure 13.5.9 Comparison of bistatic scattering cross sections o,/A* for a Honda tree by
coherent interaction model, coherent addition approximation, and independent seattering ap-
proximation. Incident angle is 45°. The tree is 5.18A in height at maximum with 63 branches.
¢p = (11+ i4)eo. The underlying half-space is flat and has a permittivity esoit = (16+ id)eo.
They are averaged over 30 realizations.
16,
ri om
g enon OMA /
2 Ind
5
j 5
Bed f\
g r|
fo io “ "i
ai ’ \
7
a a a a a a a a
‘Scattering Angle (degree)
Figure 138.5.10 Comparison of bistatic scattcring cross sections op,/” for a Honda tree by
coherent interaction model, coherent addition approximation, and independent scattering ap-
proximation, Incident angle is 45°. ‘The tree is 5.18, in height at maximum with 63 branches.
€p = (11+ i4)eo. The underlying half-space is flat and has a permittivity ¢soit = (16 + i4)eo.
‘They are averaged over 30 realizations.
--- PAGE 700 ---
682 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
radius of the modified branch is calculated by

N, Ny

aj = (s: a) / (=: :) (13.5.19)

i=l i=l
where Nj is the number of branches that continue in the same direction. The
radius and length of the original ith branch are a; and J;, respectively. Thus,
the modified central branch replaces the original six branches of different
radius. Equation (13.5.19) keeps the volume of the modified branch to be
the sum of individual branches. We rearrange the output data from the L-
systems. The 63-branch tree then becomes a 32-branch tree-like structure.
The results of wave scattering from the 32-branch tree-like structures are
given below.

Figures 13.5.11 and 13.5.12 show the bistatic scattering cross sections for
co-polarization o,, and opp for an incident angle of 45°. The results of CIM
and CAA in Figs. 13.5.11 and 13.5.12 are comparable to those in Figs. 13.5.9
and 13.5.10. This shows that since the wave approaches take into account the
phase differences among branches, the results are not critically dependent
on how the branches are labeled as independent scatterers. However, we can
see large differences of the results of independent scattering when compar-
ing Figs. 13.5.9-13.5.12. The results of independent scattering depend on
how branches are labeled as independent scatterers. We also see large radar
cross section in the backscattering direction for the independent scattering
approximation, which does not appear in Figs. 13.5.9 and 13.5.10. This is
due to the contribution of the modified central cylinder which has become
much larger and contributes dominant scattering at the conical direction.

Figures 13.5.13 and 13.5.14 show the bistatic scattering cross sections
for cross-polarization o,), and a). The results in Figs. 13.5.13 and 13.5.14
have the same parameters as Figs. 13.5.11 and 13.5.12. We can see differ-
ences between the results of the coherent interaction model and the coherent
addition approximation. It is shown that the results of cross-polarization of
CAA and CIM can be smaller than those of independent scattering. ‘The
cross-polarized component of the scattered wave is a result of the inclination
angles of branches and the coherent wave interaction among the induced
polarization within the branches. This field interaction depends strongly on
how the branches are placed and oriented with respect to each other. It also
creates a more complicated scattering pattern. The results of Fig. 13.5.14,
show that the interactions between branches and the main stem give rise
to cross-polarized backscattering coefficients which are different from those
calculated by the CAA. In the CAA, the internal fields are assumed to be
--- PAGE 701 ---
§5.3 Scattering by Honda Trees 683
10,
| CM
8 sei CAR
3 at
5
i 4 N -
fd eh ry
i” hs
25] aa
“foo a0 80S 00
‘Scatenng Angle (dogres}
Figure 13.5.11 Comparison of bistatic scattering cross sections oy,/d? for a modified
Honda tree by coherent interaction model, coherent addition approximation, and independent
scattering approximation. Incident angle is 45°, The tree is 5.18\ in height at maximum
with 32 branches. ¢, = (11 + #4). The underlying half-space is flat and has a permittivity
€soit = (16 + id)eg. They are averaged over 30 realizations.
10, $$
5 CM
a nooo CAA
zo ost
3 . y
) a”
H N\ |
Bad Pavan - J Me
6 ia b-5 64 4
hs W/ ! Kh:
i?
as
“Noo 80 02000
‘Scatiering Angle (degree)
Figure 13.5.12 Comparison of bistatic scattering cross sections o,,/A for a modified
Honda tree by coherent interaction model, coherent addition approximation, and independent
scattering approximation. Incident angle is 45°, ‘The tree is 5.18 in height at maximum
with 32 branches. cy = (11 + i4)e,. The underlying half-space is flat and has a permittivity
€soit — (16 + é4)e. They are averaged over 30 realizations.
--- PAGE 702 ---
684 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
4
cm
a) aoancedl
g A
€ | mo Ind ry
er on. _ h
p~ fd'- Voy ay hare
oo Noy Woo yy yo
g5 oS \, aan
i | N
asi “
i
7)
i a a eT)
‘Scattering Angle (degree)
Figure 13.5.13 Comparison of bistatic scattering cross sections o,,/X? for a modified
Honda tree by coherent interaction model, coherent addition approximation, and independent,
scattering approximation. Incident angle is 45°, The tree is 5.184 in height at maximum
with 32 branches. €p = (11 + i4)eg. The underlying half-space is flat and has a permittivity
€soit = (16 + i4)éo. They are averaged over 30 realizations.
4
—— CIM
=-t0} cece GAN
g nd
z
i M woe canes
e om , ‘
ic
® 30)
ar a re TD
Scattering Angle (degree)
Figure 13.5.14 Comparison of bistatic scattering cross sections ap,/A? for a modified
Honda tree by coherent interaction model, coherent addition approximation, and independent
scattering approximation. Incident angle is 45°. The tree is 5.18A in height at maximum
with 32 branches. e, = (11 + i4)ey. The underlying half-space is flat and has a permittivity
€s0it = (16 + i4)eo. They are averaged over 30 realizations.
--- PAGE 703 ---
§6 Rice Canopy Scattering Model 685
the same as if each branch exists by itself. That internal field is dictated
entirely by the polarization and the direction of the incident wave. However,
the mutual coherent interaction, especially in the near field, can significantly
change the direction of the internal field and the polarization current. This
creates a larger difference of wave scattering for cross-polarization.

6 Rice Canopy Scattering Model

The application of space-borne sensors on monitoring rice crop growth is
important to study the usage of earth lands. The possibility of using SAR
measurements for the remote sensing of rice crop is based on a. particular
characteristic of the rice field that has a flooded ground surface during a
large portion of its growing period, and a nearly vertical rice plant struc-
ture which is somewhat different from other types of vegetation. Satellite
SAR data of rice field have shown strong temporal responses, At C-band,
the ERS-1 backscatter data of rice fields increase significantly with the rice
plant height and biomass until its fully-grown stage. The increase is also
enhanced by the highly reflective underlying flooded surface through the
volume-surface interaction. In this section, we describe a scattering model
for microwave remote sensing of rice field. The model is developed based
on the coherent addition approximation and Monte Carlo approach. Sim-
ulated backscattering coefficients employing ground truth characterization
agree well with the temporal variations of SAR backscatter data from test.
rice field sites.

6.1 Model Description

The Monte Carlo configurations of rice fields used in the simulations are
created on the basis of ground truth characteristics, such as volume fractions,
sizes and shapes of rice plants. The locations, orientations, and distributions
of rice plant components are generated using random number gencrators.
Figure 13.6.1 shows a schematic diagram of the simulated rice field where
rice branches are planted with nearly constant spacing over a square area
A, but a small random variation in the spacing between rice branches are
allowed. The lower half space is water with complex dielectric constant €.
Each rice plant contains a bunch of N, dielectric cylindrical stems with height
A, radius a, and complex dielectric constant €,. Each rice stem has attached
N¢ leaves of elliptical disc shape with length @, width w, thickness d, and
complex diclectric constant €g. Within a rice bunch, the stems are uniformly
randomly placed inside a circle of radius ap. There is a total number of Ne
--- PAGE 704 ---
686 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
I Wo
Hog tt tatty /. /
eb GS //
PCH | CRY ID / A
/
ID AEH ath GED /
/
CD dd ab ab aby /
=
a
Figure 13.6.1 Rice model configuration. Rice bunches are planted over a square area A
with spacing @ in the « direction and spacing 6 in the y direction
bunches inside the simulated rice field such that the total number of stems
is Nox N, and N,x Ns x N¢ for leaves. The rice stem height may assume a
Gaussian distribution with the mean height given by the ground truth. The
orientation of leaves can be described by Euler angles. The rice stems and
leaves may tilt from the vertical direction to the maximum tilt angle 95 for
stems and 6,,,¢ for leaves. ;

Consider an incident wave E', in the direction (9;,;), impinging on a
rice canopy of layer thickness h. As shown in Fig. 13.6.2, the first-order far-
field solution of the backscattered field from a rice canopy can be expressed
as the summation of four major scattering mechanisms,

eikr

F4(r) = —[ 81 + S2 + Sa + Sa JE} (13.6.1)
where p and q denote the polarization of the incident and scattered waves, re-
spectively. The first term S} describes the direct scattering from a scatterer,

Fig. 13.6.2a,

Ne _ ~.
S1= YO AG: + 61:0;.6,) OREO. +617 (13.6.2)
(Sem jad

oF lea!
where t denotes the scatterer type: stem or leaf, and N;=N,x N; for stems
and N; = N,x Ny x Ne for leaves. fy is the scattering amplitude matrix
element for an incident wave with polarization p and a scattered wave with
polarization q. k is the incident wave propagation vector and Ky is for the
scattered field. 75 = da$+iy{—22% is the location of the rice canopy element j
of type t. The second term Sy describes the single scattering from a scatterer
--- PAGE 705 ---
§6.1 Model Description 687
(a) (b)
\ \
~---%\)_- HN, —p—:=0
ava
----e zach
(©) @)
» *
So \aayae oo A are
\ \
\ \\ 7
vA --- He E za-h
La _- .
Figure 13.6.2 Four major backscattering mechanisms in a rice canopy: (a) direct scattering
from the scatterer; (b) single scattering from the scatter followed by reflection off the ground
surface; (c) ground surface reflection followed by single scattering from the scatterer; (d)
reflection by ground surface followed by single scattering from the scatterer and further
reflection off the ground surface.
followed by a reflection off the ground surface, Fig. 13.6.2b,
NM _, .,
S2= S> SP Ra(G;) feist + 1:64, 04) eRe O)-K C67; (13.6.3)
omen =]
or Wat
The third term $3 is the reverse of the second scattering mechanism,
Fig. 13.6.2c,
Me -, ze =
$3 = DYE F614 bis 785, 84) Ry (Os) elo P 9) Rls Or
testo jal
(13.6.4)
where Rp(9;) and R,(9;) in (13.6.3) and (13.6.4) are the Fresnel reflection
coefficients of the p and q-polarizations, respectively. The fourth term S4
describes a reflection by the ground surface followed by the backscattering
from the scatterer and further reflection off the ground surface, Fig. 13.6.2d,
M _, -.
Sy = yy 3 Ry(8i) fog Bis 7+ 945 1 —B;, 5) Ry (Bi et BHO) (0.8400) FF
or tear 272
(13.6.5)
--- PAGE 706 ---
688 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
‘To calculate the scattering amplitude matrix elements of rice plants,
the infinite cylinder approximation can be applied for rice stems, and the
infinite disk approximation can be employed for rice leaves. These two ana-
lytical approximations have been described in details in Chapter 1, Section 6
of Volume I. The effects of attenuation on the coherent wave is taken into
account by using Foldy’s approximation. The extinction matrix is obtained
by averaging the forward scattering amplitude matrix over rice canopy scat-
tering components. The rice plants are then assumed to be excited by this
coherent wave. The two characteristic waves propagate along the direction
(8, @) inside the canopy with the propagation constants
ky = ko — iMan (13.6.6)
ky = ko — {My (13.6.7)
for horizontally and vertically polarized components, respectively. In (13.6.6)
and (13.6.7),
i2n NeNs f , sete , .
May =F ye [ (ft0™(0,6;0,0)) + Ne( fleet(0, 6:6.6)) | (13.6.8)
where the angular brackets denote configurational average, h is the layer
depth of rice canopy, and k, is the wavenumber of free space. The real parts
of Mpp and Mgq give the extinction. Since the calculated k, and ky are quite
close to ky, the effects of reflection and refraction at the top boundary of
tice canopy layer are neglected. Based on equations (13.6.6) and (13.6.7),
equation (13.6.1) can be expressed as
eikr Ne
E@=— Vy
some Ga]
or teat
at at
—Myq—- =} Di(kt gt +h yt ki zt
[ate i) a a aR
Myg eee —Myp it “bevy!
+ Ro(8:) ft (0i, 7 + 0:3 0;, Oiler corm oo Mov mea, Bilas +h ys +kEh)
+ fap (t — Gi, + bis 7 — 81, 01) Rp (Bi)
x eo Mea sitar ¢Mro saat p2i(he thy! +i)
+ Ra (6i) fin (9i.% + O45 7 — 9;, :) Rp (9i)
M, that M. ahte5 Kent kt yt ke (2h ‘
x ean ceaat @ Moe caxay p2ilkias +hyyS+h: (2h+25)] Ei (13.6.9)
where ki, = ko sin 8; cos @;, hi, = ko sin 6; sin ¢;, and ki =ko cos 6}.
--- PAGE 707 ---
§6.2 Model Simulation 689

In each realization of the simulated rice field, the center positions of
N, tice clusters are first created and then the positions of the N, stems
within every bunch are generated, both steps use random number generators
with uniform distribution. The positions of rice stems are checked so that
there is no overlapping between stems. The positions and orientations of
the attached leaves on each stem are also generated using random number
generators. The tilt angles of stems or leaves are similarly generated. The
scattered electric field £, from each realization is calculated according to
(13.6.9). The backscattering coefficient is computed from

dar? (Es?) ag
Ow = TE (13.6.10)

where A is the simulated rice field area. The results are obtained by av-
eraging over an ensemble of realizations. The angular brackets denote the
configurational average.
6.2 Model Simulation
‘The rice canopy scattering model described in the previous section is applied
to simulate the backscattering signatures at different rice growth stages and
compared with ERS-1 data. The frequency is 5.3 GHz, the incidence angle is
23°, and the polarization is VV. The parameters used in the simulation are
summarized in Table 13.6.1. The dielectric constants of rice plant at various
growth stages are calculated from the gravimetric water content using an
empirical formula given by Ulaby and El-Rays [1987]. Since the bottom part
of the rice plants is in the water, the dielectric constant of the ground surface
is that: of water at the frequency of 5.3 GHz at 20°C, which is ¢) =(74+721)e,.
In the simulation, the average spacing between two rice bunches is about
22 cm. We also assume that the height of stem has a normal distribution
with the standard deviation of | cm. The backscattering coefficients are
obtained by averaging over 50 realizations. The parameters and data used
in this comparison are obtained from the reference [Le Toan et al. 1997].

In Fig. 13.6.3, the model backscattering results of VV polarization at
different growth stages are compared with the ERS-1 data. ‘The compari-
son shows good agreement between model and measurements. The increas-
ing trend of the temporal radar response is well captured by the Monte
Carlo modeling. Since the bottom of rice plants are immersed in water, the
backscattering returns are dominated by the volume-surface interactions.
--- PAGE 708 ---
690 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION
a (ax) a
stent height H (cm) 20.0 | 35.0 684 76.7
a1 | 0.2 0.16 O18
# of stems per bunch Ny to | Ww | 10 10
# of bunches per m™ (No/A) 20 20 | 20 20
_ gravimetric water content 0.74 | 0.71 O71
|" dielectric constant ¢,, « 27.6418. [25.7 418.0] 25.7418.
f leaf width w (cm) _ OAT 0.74 is [7 12a]
jaf ength € (em); Tae [2472 “0 |
__leaf thickness d (em) 0.02 0.02 | 002 | 0.02 0.02 |
# leaves per stem Ne 5 a re
volume fraction (%) | 0.06 0.09, 0.123 | 016i | 0.204
bunch radius a, (cin) 18 + 2.1 230 [23
max stem tilt angle On. (deg)| 0 0 0 3 | 10
max leaf tilt angle 0,, (deg) 20 30 40
Table 13.6.1 Input parameters for model simulation.
9
i scons Model
L4 Data | |
7 |
4, A
q a oa)
& Age eee te
g aA’ Ay
g10 een a A
5 a A A
Gob oa a 4
F , A
z | “
4
wi 4
| '
|
0 10 20 30 40 50 60 70 80 90 100
‘Age (days)
Figure 13.6.3 Comparison of measured and model backscattering coefficients at C-band
versus rice age.
--- PAGE 709 ---
REFERENCES 691
REFERENCES AND ADDITIONAL READINGS

Abelson, H. and A. A. diSessa (1982), Turtle Geometry, MIT Press, Cambridge, MA.

Au, W. C.. J. A. Kong, and L. Tsang (1994), Absorption enhancement of scattering of
electromagnetic waves by dielectric cylinder clusters, Microwave Opt. Technol. Lett.,
7(10), 454-457.

Au, W. C., L. Tsang. R. T. Shin, and J. A. Kong (1996). Collective scattering and absorption
in microwave interaction with vegetation canopies, Progress in Electromag. Res., 14,
182-231, FMW Publishers, Cambridge, Massachusetts.

Chen, Z. (1994), Microwave remote sensing of vegetation: Stochastic Lindenmayer systems,
collective scattering effects, and neural network inversions, Ph.D. thesis, University of
Washington, Seattle.

Chen, Z., L. Tsang, and G. Zhang (1995), Scattering of electromagnetic waves by vegetation
based on the wave approach and the stochastic Lindenmayer system, Microwave Opt.
Technol. Lett., 8(1), 30-33.

Chen, Z., L. Tsang, and G. Zhang (1996), Application of stochastic Lindenmayer systems
to study collective and cluster scattering in microwave remote sensing of vegetation,
Progress in Electromag. Res., 14, 233-277, EMW Publishers, Cambridge, Massachusetts.

Fung, A. K. (1994), Microwave Scattering and Emission Models and Their Applications,
Artech House, Norwood, Massachusetts.

Goel, N. S., L Rozehual, and R. 1. Thompson (1991), A computer graphics based model for
scattering from objects of arbitrary shapes in the optical region, Remote Sens. Environ.,
36, 73-104.

Herman, G., A. Lindenmayer, and G, Rozenberg (1975), Description of developmental lan-
guages using recurrence systems, Mathematical Systems Theory, 8, 316-341.

Le Toan, ‘f., F. Ribbes, L. F. Wang, N. Floury, K. H. Ding J. A. Kong, M. Fujita, and T.
Kurosa (1997), Rice crop mapping and monitoring using ERS-1 data based on experi-
ment and modeling results, EEE Trans. Geosci. Remote Sens.. 35, 41-56.

Lin, Y. C. and K. Sarabandi (1999a), A Monte Carlo coherent scattering model for forest
canopies using fractal-generated trees, IEEE Trans. Geosci. Remote Sens., 87, 440 451.

Lin, Y. C. and K, Sarabandi (1999b), Retrieval of forest parameters using a fractal-based
coherent scattering model and a genetic algorithm, [EEE Trans, Geosci. Remote Sens.,
37, 1415 1424.

Lindenmayer, A. (1968), Mathematical models for cellular interaction in development, Parts
Land II, Journal of Theoretical Biology, 18, 280-315

Lindenmayer, A. (1974), Adding continuous components to L-systems, L Systems,, Lecture
Notes in computer Science, 15, 53-68, Springer-Verlag, Berlin.

Mandelbrot, B. B. (1983). The Fractal Geometry of Nature, W. H. Freeman & Co., New
York

Prusinkiewicz, P. and J. Hanan (1989), Lindenmayer Systems, Fractals, and Plants, Vol. 79
of Lecture Notes in Biomathematics, Springer-Verlag, Berlin

Prusinkiewicz, P. and A. Lindenmayer (1990), The Algorithmic Beauty of Plants, Springer-
Verlag, New York

Stiles, J. M. and K, Sarabandi (2000), Electromagnetic scattering from grassland. I. A fully
phase-coherent, scattering model, IEEE Trans. Geosci. Remote Sens., 38(1), 339-348,
--- PAGE 710 ---
692 13 ELECTROMAGNETIC WAVES SCATTERING BY VEGETATION

Stiles, J. M:, K. Sarabandi, and F. T. Ulaby (2000), Electromagnetic scattering from grass-
land. 11, Measurement and model results, IEEE Trans, Geosci. Remote Sens., 38(1),
349-356.

Tsang, L., K. H, Ding, G. Zhang, C. C. isu, and J. A, Kong (1995), Backscattering en-
hancement and clustering effects of randomly distributed dielectric cylinders overlying
a diclectric half space based on Monte-Carlo simulations, IEEE Trans. Antennas Prop-
agat., 43(5), 488-499.

Ulaby, F. T. and C. Elachi, Eds. (1990), Radar Polarimetry for Geoscience Applications,
Artech House, Norwood.

Ulaby, F. T. and M. A. El-Rays, (1987), Microwave dielectric spectrum of vegetation — Part
TI: dual-dispersion model, IEEE Trans. Geosci. Remote Sens., 25, 550-557.

Yueh, $. H., J. A. Kong, J. K. Jao, R. T. Shin, and T, Le Toan (1992), Branching model for
vegetation, IEEE Trans, Geosci. Remote Sens., 30, 390 402.

Zhang, G., L. Tsang, and Z, Chen (1996), Collective scattering effects of trees generated by
Stochastic Lindenmayer Systems, Microwave Opt, Technol. Lett., 11(2), 107-111.
--- PAGE 711 ---
Scattering of Electromagnetic Waves: Numerical Simulations.

Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.

Copyright © 2001 John Wiley & Sons, Inc.

ISBNs; 0-471-38800-9 (Hardback); 0-47 1-22430-8 (Electronic)
INDEX

Absorption, 455, 500. Associated Legendre polynomial, 99, 521,

coefficient, 375, 456, 507, 547, 614, 620, 523, 543.
621, 672. Attenuation, 455, 688.
cross section, 375, 380, 547. rate, 504.
enhancement, 643. Averaging
for independent scattering, 620. angular, 556, 561.
rate, see Absorption coefficient. azimuthal, 565, 571, 572.
Absorptivity, 141, 142, 351, 353. configuration, 385, 502.
Angular correlation function (ACF), 553, frequency, 556, 557, 559.
556, 559, 560, 564, 565, 572, 573, 577, realization, 7, 393, 555-557, 580.
580. Axiom, 645, 646.
focusing, 583. Avimuthal averaging, 565, 571, 572.
imaging, 582, 583, 586, 587.
see also Frequency angular correlation Backscattering coefficient, 372.
function (FACF). from half-space of scatterers, 509.
see also Polarization angular correlation from rice canopy, 689.
function (PACF). from rough surfaces 151, 154, 210, 212.

Active remote sensing, 179, 456. from trees 643, 660, 662 668, 671-675,

Adaptive integral method, 180. 682,

Addition theorem, 98, 487-489. Backscattering enhancement, 376.
for vector cylindrical waves, 477, 478, comparison with experiments, 292, 293.

604, 607, 632, 636. for I-D random rough surface, 113, 260,
for vector spherical waves, 534, 535, 537. 269, 275, 288, 289, 291-293.

Adhesive for 2-D random rough surface, 324-326.
disk, 463. for volume scattering with reflective
particle, 434, 438. boundary, 594, 614-616, 618.
potential, 434, 439. Backsubstitution, 186, 245.
see also Sticky. Banded matrix, 179, 181, 183, 186, 201,

Adjoint, 36. 252.

Aggregation, 235, 238. Banded matrix iterative approach (BMIA),

Aligned spheroids, 518, 527. 179.

Alphabet, 644. with canonical grid (BMIA/CAG), 180,

Angular averaging, 556, 561. 185, 187, 190, 194, 203.
azimuthal, 565, 571, 572. Bandwidth, 187, 215.

Angular width, 616. Basis function, 23, 24

Anisotropy, 131. dipole, 514

Antarctic firn, 5, 7. entire domain, 24, 80.

Antarctica, 2, 5, 10. pulse, 24, 86.

Anterpolation, 240, 241, 253. quadrupole, 521, 522

693 —
--- PAGE 712 ---
694 INDEX
Rao-Wilton-Glisson, 301. Block Toeplitz matrix, 272, 283.
subsectional, 24, 80, 85. Bonds, 465.
triangle, 25. Born approximation, 382, 409, 656, 658.

Basis lattice vectors, 95. distorted, 409, 509.

Beowulf system, 270, 354, 355. Born series, 382.

Bessel function, 66, 80, 463, 491, 543, 607, Born term, 246.

626 Boundary condition
recurrence relation for, 542. Dirichlet, 15, 62, 63, 113, 115, 116, 180,
small argument, 474. 212, 270, 271

Bethe-Salpeter equation, 496 extended (EBC), 62, 69, 80.

Binary branching, 652. for tangential fields, 75.

Binding states, 465. impedance, 154, 161, 162, 196.

Biomass, 685. Neumann, 113, 116, 134, 158, 159.

Bistatic intensity, 602. periodic, see Periodic boundary condi-

Bistatic scattering amplitude, 658. tion.

Bistatic scattering coefficient, 372. with surface charge, 20.
from 1-D random rough surface, 113, Branching

123, 141, 146-153, 160, 190, 194, 203, angles, 651
204, 207, 210, 211, 254, 258. binary, 652.
from 2-D random rough surface, 269, ternary, 651
273 276, 285-292, 318, 323, 325, 333, Brent's method, 449.
334, 360. Brewster angle, 339, 341.
from azimuthally averaged, 570, 571. Brightness temperature, 456.
from band-limited surfaces, 151. from Antarctic firn, 2, 5, 7-11.
from periodic surface, 68, 158. from soil, 260, 341, 343, 347, 349.
from real-life rough surfaces, 167. from layered medium, 7-11.
from trees, 675. from periodic surface, 82, 83, 89-91.
from vertical cylinders, 600, 614. from 1-D random rough surface, 113,
using BMIA/CAG, 190, 194. 141, 165, 260.
using Kirchhoff approximation, 145, 146, from 2-D random rough surface, 270,
275. 334, 336, 339, 341, 343, 349, 360, 363,
using PBTG-BMIA/CAG, 203, 204, 207. 364.
210, 211, 254, 258. polarimetric, 89.
using PBTG/SMCG, 333, 334, 360. of the four Stokes parameters, 351, 353.
using small perturbation method, 145, see also Emissivities.
using SMCG, 285-287, 318, 323, 325. Brillouin zone, 98.
using SMFSIA, 273-276. Buried object, 553, 557, 564.

Bistatic scattering cross section
from rough surface, 172. Canonical grid
from trees, 678, 680, 682. for surface scattering, 180, 183, 198
in relation to structure factor, 409. for volume scattering, 486, 487.
in relation to phase matrix, 528. Cell volume, 95.

Bistatic scattering intensity, 406. Circular SAR, 578.

Bloch condition, 63, 64, 96, 155. Imaging, 581
--- PAGE 713 ---
INDEX 695
Classical mixture formula, 456. in volume scattering problem, 489.
Clausius-Mossoti with FFT, 29, 36,
formula, 500. Conservation of energy, see Energy conser-
internal field, 29. vation.
polarizability, 28, 29. Contact function, 445, 446, 448.
Clebsch-Gordan coefficient, 541, 542. Continuous random medium, 2.
Cluster Convergence, 188, 194, 288, 319, 394.
of cylinders, 598, 599, 601, 602, 617, 620. of bistatic scattering coefficients, 275,
of point. seatterers, 389, 392. 287.
of spheres, 424. of SMFSIA, 277,
Clutter suppression, 576. Convolution, 41, 326, 333, 491, 492.
Coarse grid, 197, 200, 202, 254, 330, 332. circular, 40.
Coherent discrete, 37, 488.
component, 374. integral, 271, 409.
field, 375, 502, 600. linear, 40, 41.
forward scattering, 386. periodic, 40, 45.
intensity, 377 386, 387, 502, 517, 602, Corn canopy, 594
616. Correlated ladder approximation, 496,
inltiple scattering, 372, 374. Correlated scattering, 496.
propagation constant, 500. Correlation
reflection, 509. between clusters, 602.
scattered field, 481, 507. coefficient, 3.
scattered intensity, 502. distance, 510.
specular peak, 150. function, see Correlation function.
wave. 194, 373, 375, 387, 388. imaging, 576, 577, 579, 580.
Coherent addition approximation (CAA), length, 4, 8, 129, 150, 167, 169, 179, 257.

642, 643, 660, 665, 667, 673, 675, 679, Correlation function, 4, 124, 129.

682. direct, see Direct correlation function.
Coherent interaction model (CIM), 679. exponential, 4, 166, 257.
Complementary error function, 103. Gaussian, 145, 166, 204, 257, 292, 334,
Composite surface, 194. 343, 556.

Computational complexity, 186, 327. indirect, 406,
of PBTG-MLSDFMM, 254. mutual, 577,
of PBTG/SMCG, 333. total, see Total correlation function.
Condition number, 55, 56. Covariance function, 4.
Configuration average, 385, 502. Cubes, 28.
Conical scattering, 597. Curvature, 129, 150.
Conjugate gradient method (CGM), 46. Cyclical scattering, 293, 376.
for complex matrix, 54,
for real nonsymmetric matrix, 52. Dense grid, 197, 200, 202, 254, 326,
for real symmetric positive definite ma- 330-332.
trix, 48, 51. Dense media, 372, 454, 456, 496.
in surface scattering problem, 183, 186, Dense media radiative transfer (DMRT)
272, 284, 310, 336, 570. theory, 496, 510.
--- PAGE 714 ---
696 INDEX
Densely packed propagation constant, 500, 505, 510, 669.
spheres, 512, 514. volume, see Effective volume.
spheroids, 518. wavenumber, 501.
Depolarization, 519, 673. Effective volume, 434, 435, 441, 467.
Dipole moment, 28, 35, 36, 498, 506, 517, with single bond, 435, 436.
518, 678. with triple bond, 437.
Direct correlation function, 406, 412, 425, with unbounded state, 435,
426, 430, 461. Electric
of hard disks, 462. dipole, 520. see also Dipole moment.
of hard spheres, 410. flux density, 498.
Direction vector, 36, 47-49. quadrupole, 520.
Dirichlet Electric field integral equation (EFIE), 115,
matrix, 78. 116, 158.
boundary condition, 62, 63, 113, 115, Electrostaties, 20, 514.
116, 180, 212, 270, 271 Elemental volume, 373.
Disaggregation, 235, 238, 241, 253. Ellipsoid, 445.
Diserete dipole approximation (DDA), 27, Elongation, 447, 526.
30, 35, 547. Emissivities, 372.
applied to trees, 669, 670, 672, 673, 675. from 1-D random rough surface, 113,
with FFT, 45, 141, 142, 162, 165, 196, 205, 207, 260.
Discrete Fourier transform (DFT), 37-40, from 2-D random rough surface, 270,
126, 127-129. 327, 333, 334, 336, 351, 360.
&D, 45. from periodic surface, 69, 81, 82, 89.
inverse, 40, 45. from soil, 260, 343.
Discrete layering model, 2, 8, 10. of four Stokes parameters, 89.
Discrete random medium, 2. see also Brightness temperature.
Displacement, 416, 444, 459 Energy conservation
choice of, 419. comparison between EFIE and MFTE,
Dissipative loss, 330. 161.
Distorted Born approximation, 409, 509. in scattering by periodic surface, 68, 69.
Divergence angles, 651. in scattering by random rough surface,
DOL-system, 645. 113, 159, 161, 163, 254, 256, 273, 286,
Double bond, 434, 466-468. 352.
Downward-going, 79, 611, 612. in volume scattering 672
Dual integral equations, 137, 138, 140, 162. Entire basis functions, 80.
Durden-Vesecky spectrum, 131. Equivalent
Dyadic Green's function, 19, 28, 31, 516, charges, 296.
622, 655. currents, 18, 293, 296.
low frequency approximation, 32. exterior problem, 296, 300.
Dyson equation, 496. interior problem, 298.
sources, 297, 298, 300.
E-waves, 69, 70, 80. Error function, 103, 104.
Effective ERS-1, 685, 689.
permnittivity, 454, 456, 496, 498, 500. Euler angles, 686.
--- PAGE 715 ---
INDEX 697
Ewald's method, 62, 93, 105-107. Foldy’s approximation, 373, 546, 643, 667,
Exclusion volume, 29, 31. 669, 688.
Extended boundary condition (EBC), 62, Foldy-Lax multiple scattering equations
69, 80. hased on volume integral equation, 516,
Extinction, 456. 518.
as function of concentration, 454. first order solution, 381, 384, 603, 611,
as function of frequency, 456. 620, 637.
coefficient, sce Extinction coefficient. for cylinders, 476-478, 481, 482, 489.
matrix, 688. for cylinders with reflective boundary,
measurements in snow, 457. 603, 608, 611, 622, 631-633.
rate, see Extinction coefficient. for point scatterers, 372, 379-382, 393.
theorem, 70, 115, 298. for spheres, 516, 533, 547.
Extinction coefficient, 372, 373, 375, 376, higher-order solutions, 381.
454-456, 510, 672. iterative solution, 373, 382, 611.
for cylinders, 485. in waveguide, 622, 631.633.
for point scatterers, 382, 389, 392 395, internal field formulation, 482.
398. low frequency formulas for, 482.
for spheres, 545, 546. scattered field formulation, 481.
for spheroids, 518, 519, 526, 527. second order solution, 388, 394, 617, 620.
‘T-matrix formulation, 533, 539, 547.
Factorization method, 412, 425, 431. Forest, 594.
Fast multipole method (FMM), 179, 212, Forward scattering amplitude, 373.
216. matrix, 688.
multilevel, 218. to second order, 388.
steepest descent, see Steepest descent Forward scattering theorem, 380, 384.
fast multipole method. see also Optical theorem.
FETW, 356. Forward specular peak, 275, 323.
Field imaging, 576, 579, 582, 583, 587. Fourth Stokes parameters, 62.
Filter function, 579. Fourier-Bessel transform, 463.
Finite-difference time-domain (FDTD) Fractal, 644
method, 179, 547. dimension, 133, 150.
Finite element method (FEM), 179. rough surface, 113, 124, 132, 133, 150,
Flat-surface block Toeplitz matrix, 270. 163.
Flat-surface Green's function, 271, 282. Fractional
Floquet mode, 68, 72-74, 81, 83, 89, 155, area, 458.
156, 191, 192. volume, 415, 454, 455, 500, 526, 613, 617,
amplitudes, 68. 638, 661, 672.
evanescent, 65, 107, 156. Fredholm integral equation of the first
propagating, 65, 67, 68, 85, 156. kind, 16, 180, 271.
propagation vectors, 74. Frequency angular correlation function
reflected power for, 81. (FACF), 577, 579, 580, 586.
Floquet’s theorem, 63, 64, 70, 77, 552. imaging, 578, 580, 587.
Focusing, 576, 578. Frequency averaging, 556, 557, 559.
--- PAGE 716 ---
698 INDEX
Frequency correlation function (FCF). 552, periodic, sec Periodic Green's function.
577, 580. reflected, 608.
imaging, 586, 587. response, 623, 624, 629, 630.

Frequency selective surfaces, 62, 102. singularity in, 20, 86, 115, 116,

Fresnel translational invariance of, 554,
reflection coefficient, 162, 508, 656, 687. Taylor expansion of, 180, 181.
reflectivity, 341. Green’s theorem, 15, 80, 114, 138.
transmission coefficient, 505.

H-waves, 69, 70, 80.

Galerkin’s method, 25, 301, 525. Half-space Green’s function, 603-605.

Gauge condition, 293, 294. Hankel function, 15, 491, 607, 626.

Ganssian asymptotic, 189, 480.
correlation function, 145, 166, 204, 257, integral identity, 93, 99.

292, 334, 343, 556. integral representation, 93.
distribution, 597, 613. recurrence relation for, 99.
height distribution, 556. small argument, 474.
random numbers, 126, 127. spherical, 94.
random process, 2-4, 6, 8, 124, 130, 132. Heaviside step function, 181, 188, 610.
rough surface, 113, 145, 204, 292, 334, Hole-correction (HC) approximation, 405,
343. 603.
~ with Gaussian spectrum, 124, 129, 130, Honda trees, 677, 680.
132, 150, 257, 280, 319, 571. Huygen’s principle, 122, 297.
~ with ocean spectrum, 113, 124, 150, Hybrid matrix, 79.
163.
random variable, 5, 124. Ice, 6, 10, 372.
Generalized surfaces, 354.
Ornstein-Zernike equation, 412. Ml-conditioned matrix, 16, 80, 157.
phase matching, 553. Impedance boundary condition, 154, 161,
Wiener-Hopf technique, 412. 162, 196.

Geometric optics, 457. Impedance matrix, 35, 159, 180, 216, 252,

Green's function, 14, 18, 63, 271, 37. 310, 329, 382, 488, 568.
2D, 15, 23, 70, 114, 138, 189, 213. decomposition, 245.
asymptotic approximation, 189. multilevel, see Multilevel impedance ma-
cylindrical wave representation, 606. trix,
decomposition of, 188, 250, 332. with numerical integration, 37, 143, 160.
dyadic, see Dyadic Green’s function. Incoherent
flat-surface, 271, 282. bistatic scattering coefficient, 613, 614.
electrostatic, 20. bistatic scattering intensity, 386.
half-space, 603-605. component, 374.
in lossy dielectric, 197, 200, 201, 250, field, 600.

326, 330. intensity, 481, 502, 503, 508, 602.
in spatial domain, 65. phase function, 396.
in spectral domain, 65, 213. power, 517.
primary, 622, 624, 629, 633. scattered field, 508.
--- PAGE 717 ---
INDEX 699
scattered power, 503. Ladder diagrams, 376.
scattering amplitude, 386, 393. Laplace equation, 497, 499, 521, 523.
wave, 375. Laplace transform, 66.
Independent random variables, 124 Large-scale rough surface, 179.
Independent scattering Lattice
for cylinders, 484, 485, 602, 616. 1-D, 64,
for point scatterers, 376. 2D, 102, 105.
for spheres, 546. 3-D, 98.
for spheroids, 519, 532. Lattice vector, 94-97, 105.
for trees, 643, 661, 665, 667, 673, 679, reciprocal, 94, 96, 105.
682. Layered medium, 2, 7.
Induced continuous, 2.
dipole, 497, 499. discrete, 2.
polarization, 499. eanission from, 2.
Infinite cylinder approximation, 25, 26, 688. — Legendre function
Infinite disk approximation, 688. of second kind, 523.
Inner product, 24. of the first kind, 523.
Integral equation, 14 Lindenmayer system (L-system), 642, 644,
electric field, see Electric field integral 677.
equation (EFIE). DOL-systems, 645.
formulation, 14, OL-system, 645.
magnetic field, see Magnetic field integral parametric, 645, 648.
equation (MFTE). stochastic, 642, 643, 646, 649, 669, 680.
surface, sce Surface integral equation. Linear
volume, sce Volume integral equation. convolution, 40,
Internal field formulation, 482, 485. interpolation, 226,
Interpolation SAR, 578, 585, 586.
function, 225, 236, 240. Localization
operator, 251. strong, 376.
Inverse scattering, 16. weak, 376.
loffe-Regel criterion, 376. LOGO, 647.
Longitudinal components. 70.
Joint probability density function, 3, 384, Lorentz-Lorenz, formula, 500.
404, 405. Loss tangent, 200, 329.
of primary scatterers, 391. Low grazing angle (LGA) incidence, 119,
of secondary scatterers, 392. 179, 210, 354.
Isys, 649.
Kernel, 37, 135, 159. LU decomposition, 186.
singular, 32, 117, 278.
Kirchhoff approximation (KA), 145, 275. Magnetic field integral equation (MFTE),
Kramer-Kronig relation, 197. 135, 280, 281, 567.
Kranendonk-Frenkel algorithm, 434, 439. for TE case, 158, 242, 243.
Krylov subspace, 50. for TM case, 158, 242, 244.
Magnetic ring current. 635, 638.
--- PAGE 718 ---
700 INDEX
Markov chain, 446, see also Kranendonk-Frenkel algorithm,
Massively parallel processors (MPP), 354. Seaton-Glandt algorithm.
Matched filtering, 576. Microwave remote sensing
Matrix equation, 23, 24, 37, 113. active, see Active remote sensing.

for 2-D dielectric rough surface, 329. passive, see Passive remote sensing.

for DDA, 28, 35. Mic scattering, 572, 573, 583, 587.

for EFTE, 117. Mixing formula

for MFIE 136, 159. classical, 456.

for periodic surface, 74, 79, 156. for dry snow, 6.

for two-media problem, 140, 143. ve ee 500.

with BMTA, 179. Modal solution, 625, 630.

with conjugate gradient method, 46, 186, Mode expansion, 156.

with PBTG, 252. Mode function, 632.

with single grid, 199, Modified power-law spectrum, 258.

with SMCG, 285, 309. Moisture, 82, 83, 260, 342, 562.
Matrix filling, 24. Monestatic radar, 582, 585,
Maxwell equations, 2, 17, 353, 496. Monte Carlo step (MCS), 446.
Maxwell-Gamett mixing formula, 500. Multigrid method, 197,

Multilevel FMM, 218.
Mean free path, 375. “evel *) -
Memory dot, 583, discretization of angles in, 222.
Memory effect, 553, 555, 577, 580, 586. with steepest descent (SDFMM), 253.
oy ees eee Multilevel impedance matrix, 218 221, 229.

derivation, 553.
Memory line, 552, 553, 557, 562. lower, 231, 252.

FUME, BOM 8, OT OO upper, 221, 229, 230, 231, 235.
Message-passing interface (MPI), $54. Muitiple incoherent scattering, 375.
Metamorphisin, 424, Multiple scattering equations,

Method of moments (MoM), 23. see Foldy-Lax multiple scattering
basis function for, see Basis function. cantations.
body of revolution code, 26. Multiple species
on surface integral equation, 86, 113, 117, of adhesive particles, 439.
136, 159, 179, 269, 286, 329. Ornstein-Zernike equation, 431.
on volume integral equation, 514, 518, Multipole, 485
519. expansion, 512.
Method of ordered multiple interactions radiation from lattice, 99.
(MOM), 179, 242, 245. Mutual correlation function, 577.
new Born term in, 246.
recurrence relation, 246. N-particle scattering amplitude, 374, 375,
tenth-order, 247. 382, 384, 388, 393.
zeroth-order, 247. first-order, 384, 390.
Method of steepest descent, 47. Near-field
Metropolis shutting, 414, 415, 418, 424. integration, 363.
for cylinders, 458, 638. interaction, 202, 253, 254, 310, 332.
for spheroids, 444, 518. region, 203.
for sticky particles, 434, 467. see also Strong interaction.
--- PAGE 719 ---
INDEX 701
Neighborhood distance, 37, 181, 188, 273, Pair function, see Pair distribution func-

281, 282, 285, 309, 320. tion,

Neumann Parallel computing, 354, 356, 358, 359.
boundary condition, 113, 116, 134, 158, Parallel plate waveguide, 622, 638.

159. Parametric
function, 543. L-system, 645, 648.

recurrence relation for, 542. OL-system, 645.
iteration method, 275. Parallelepiped, 22, 31, 35.
matrix, 78. Particle energy state (PES), 465.
series, 382. Passive remote sensing, 113, 336, 339, 456.

Non-near field, 251, 327. of Antarctica, 10.
interaction, 202, 235, 253, 310, 331, 332. of ocean surfaces, 163.
region, 203. of rongh surfaces, 62.
see also Weak interaction. of soil, 341, 349.
Percus-Yevick (PY) approximation, 407,
Object function, 445, 448, 449. 408, 414.
Ocean, 257. for hard disks, 461.
pemnittivity, 163. for sticky particles, 425, 430, 439.
spectrum, 130, 131. Pereus-Yevick (PY) integral equation, 462.
surface, 132, 196, 326, 354. Percus-Yevick (PY) pair distribution fune-
OL-system, 645. tion, 496, 505.
Optical theorem, 28, 29, 374, 379, 386, 389, for hard disks, 463.

394, 672. for hard spheres, 409-411, 414, 418.
sce also Forward scattering theorem. for multiple sizes, 411, 414.

Optical thickness, 617. for sticky spheres, 424, 425, 428, 431,
Ornstein-Zernike equation, 407, 409, 412, 432.

425, 462. Periodic boundary condition, 68, 102.
Generalized, 412. in particle position generation, 416, 459.
multiple species, 431. in random rough surface simulation, 154,

Overlap of spheroids, 445. 157, 190.
Periodic convolution, 40, 45.
Pair distribution function, 384, 404-407, Periodic Green’s function, 62, 64, 65, 67,

502. 71, 85, 86, 93, 98, 107, 155.

Monte Carlo simulations of, 414, 415, 2D, 64.

417, 418. 3D in 2D lattice, 102.
~ for hard disks, 460. 3-D in 3-D lattice, 98.
~ for hard spheres, 419-424. in spatial domain, 65.
~ for sticky disks, 469. in spectral domain, 65, 105.

— for sticky spheres, 427, 429, 439, 443. Periodic potential, 95.
of primary scatterers, 391, 594, 598, 601. Periodic rough surface, 62.
of secondary scatterers, 389, 392, 594, Permittivity

599, 601 fiuctuation, 2, 6, 7.
Percus-Yevick, see Percus-Yevick (PY) of ocean, 151.

pair distribution function. of soil, 343.
--- PAGE 720 ---
702 INDEX
Phase function Primary Green's function, 622, 624, 629,
defintion, 374, 375. 633.
for point scatterers, 382, 383, 386, 387, Primary scatterer, 389.
391-393, Principal value integral, 19, 134, 159, 567.
in dense media, 454, 510 Probability density function, 3, 166, 404,
see also Phase matrix. 502, 597,
Phase matching, 552, 553. single-particle, 405, 384.
Phase matrix, 372, 373, 455. Productions, 644 646,
for point scatterers, 387, 388. Prolate spheroid, 521, 526. :
for spheres, 496, Propagation constant, 455.
for spheroids, 519, 528, 532 effective, 500, 505, 510, 669.
see also Phase function. Propagator, 377.
Photonie bandgap, 62. Pulse basis function, 24, 26, 86, 117, 136,
Physics-based two-grid (PBTG) method, 143, 286, 242.
179, 196, 197, 200, 326, $27, 329, 330. . .
parallel implementation, 356, 358, 359 Quadrupole basis functions, 521, 522,
with BMTA/CAG, 198, 204, 207, 210, Quasi-crystalline approximation (QCA).
O11. 405, 496, 509, 546.
with SDFMM. 249, 252. 254, Quasi-crystalline approximation with co-
with SMCG, 270, 897, 394. herent potential (QCA- CP), 405, 496,
Point matching, 25, 86, 117, 136, 143, 242, 546.
non 3 3 Radiation condition, 513.
Point scatterer, 372, 379, 380, 382. Radiative correction, 29, 31, 32.
Poisson process, 10. Radiative transfer
Poisson's summation formula, 96, 97, 100, in dense modia, 496, 510.
we equation, 372, 375, 376.
Polarimetric brightness temperatures, 89. theory, 373, 383.
Polarizability, 498-500. Radius of curvature, 129, 150.
of a small sphere, 29. Random medium
Polarization, 27, 496, 498, 514, 517, 522. continuous, 2.
charge density, 20. discrete, 2.
density, 18, 20, 513. Random process, 2, 166.
vector, 35. Random rough surface generation, 124.
Polarization angular correlation function Rao-Wilton-Glisson basis function, 301.
(PACP), 565, 571, 575. Rayleigh
Post-multiplication, 186, 187, 490. mixing formula, 500.
Power conservation, 82, 172. phase matrix, 511.
Power spectrum, 166, 169, 170, 171, 173, polarization dependence, 511.
74. seattering, 458.
modified, 258. Realization averaging, 7, 393, 555-557, 580.
Pre-conditioning, 55, 56, Reciprocal lattice, 96, 102, 105.
Pre-corrected FFT method, 180. basis, 95.
Presmultiplication, 186, 187, 490. space, 95, 96.
--- PAGE 721 ---
INDEX 703
vectors, 94, 96, 105. Scattering coefficient, 374, 375, 456, 481,
Reciprocity, 69, 615. 672.
Rectangular parallelepiped, 22, 31, 35. back-, see Backscattering coefficient.
Recurrence relation bistatic, see Bistatic scattering coeffi-
for Bessel fimetion, 542 cient.
for Hankel function, 99. for cylinders, 481, 484.
for MOMT, 216. for point scatterers, 383, 386, 394.
for Neumann funetion, 542. for spheres, 504, 510
for vector spherical harmonies, 543, 544. for spheroids, 526.
Recursive T-matrix method, 179, 547. Scattering cross section, 380.
Reflected Scattering phase function, sce Phase func-
E-modes, 81. tion
field, 89. Scattering rate, see Scattering coefficient.
Floquet modes, 89. Seaton-Glandt algorithm, 434,
Green's function, 608. Second moment, 554,
HLmedes, 81. Second-order
power, 8 Kirchhoff method, 275.
Reflectivity, 69, 81, 141, 142. SPM, 327.
Refractive index, 28. Secondary scatterers, 389.
Residual, 47-52, 186. ser a 19
en “ ol patch, 86, 117, 136, 144, 158, 159.
Residues, 627. teem, 29
re Self-similarity, 644.
Respouse Green's function, 623, 624, 629, cs wential addition method, 414, 418, 424.
630. Shadow cylinder, 661, 672.
Revwriting Shadowing, 146, 150, 354.
Process, 644. Shuffiing, see Metropolis shuffling
rules, 644, 646. Single coarse grid (SCG), 196, 198, 199,
Rice crop, 643, 685. 204, 334.
dielectric constant for, 689. Single dense grid (SDG), 196, 199, 204,
rms height, 132, 133, 150, 170, 257. 307, 210, 334.
rms slope, 129, 132, 150, 270. Single scattering, 595, 655.
Rock surfaces, 113, 167, 169, 171, 173. Single bond, 434, 466, 468.
Row direction, 62, 69, 82. Singular value, 55.
Singular value decomposition, 55.
Scalar potential, 19, 293, 294, 496. Singularity
Scattered field formulation, 481. in dyadic Green’s function, 18, 19.
Scattered power, 142. in integral equation, 32, 117, 278.
Scattering amplitude, 659. Sinusoidal surface, 80, 81.
amplitude matrix, 688, Small perturbation method (SPM), 173,
N-particle, 374, 375, 382, 384, 388, 393. 145, 270, 327, 334, 339
Scattering attenuation, 500, Small slope approximation, 327.
--- PAGE 722 ---
704 INDEX
Snell’s law, 505, 552. Sticky
Snow, 2, 5, 6, 8, 9, 167-174, 372, 424. cylinders, 454,
surfaces, 113, 167, 169, 173. disk, 463, 466, 467, 469.
density profile, 8. hard spheres (SHS), 424
dry, 6. parameter, 425, 427, 434, 465.
Soil, 257, 258, 326. particle, 40, 424-429, 457, 510.
microwave emission from, 82, 270. spheres, 444, 466.
moisture, 82, 83, 260, 342, 562. see also Adhesive.
permittivity, 260. Stochastic
surfaces, 113, 167, 169, 171, 173, 196, L-system, 642, 643, 649, 669, 680.
354. OL-system, 646.
Sommerfeld integral, 626. Stokes parameters, 62, 89, 350.
Sommerfeld integration path (SIP), 213, Stratton-Chu
626, 627. fornmlation, 302.
Sparse matrix canonical grid (SMCG) surface integral equations, 565, 566.
method, 179, 304, 309, 319, 354, 360, Strong
570, 572. interaction, 179, 181, 188, 189, 310, 486,
direct calculation in, 187, 188, 489. 488.
for scattering by cylinders, 486, 487, 491. localization, 376.
indirect calculation in, 187, 188, 490. matrix, 187, 272, 283, 359.
on Beowulf system, 354. Structure factor, 404, 406, 409, 410, 424,
parallel implementation, 356, 358, 359. 454, 503, 510.
with PBTG, 270, 360. Subsectional basis function, 24, 80, 85, 156.
Sparse matrix flat surface iterative ap- Surface adhesion, 424,
proach (SMESIA), 272, 269, 270, 281. Surface electric current, 139.
with canonical grid (SMFSIA/CAG), Surface integral equation, 14, 16, 74, 115,
284, 286. 136, 139, 161, 162, 179, 300, 301.
Sparse media, 667. for 2-D rough surface, 269, 282, 293.
Specific intensity, 373. for periodic surface, 62, 85.
Spectral density, 4, 124, 168. Stratton-Chu, 565, 566.
Spherical harmonics, 99. TE case of PEC, 16.
Spherical wave expansion, 100. TM case of PEC, 16.
Spheroid, 444. see also Electric field integral equation
Splitting parameter, 100-102, 105, 106. (EFIE), Magnetic field integral equa-
Statistical tion (MEIB).
moments, 552. Surface magnetic current, 139, 161.
phase-matching condition, 554 Surface polarization charge, 20.
translational invariance, 124, 552-555. Synthetic aperture radar (SAR), 685.
Steepest decent fast multipole method imaging, 553, 575, 576, 582.
(SDEMM), 179, 212, 235, 249. Synthetic Surfaces, 168.
Steepest descent method, 46-48.
Steepest descent path, 214, 225. T-matrix, 62, 80
representation of matrix elements, 226, approach, 62, 80, 155, 496, 533.
representation of Green’s function, 231 coefficients, 474, 477, 490, 534.
--- PAGE 723 ---
INDEX 705
for dielectric periodic surfaces, 68. Vector
low frequency limit, 482. cylindrical waves, 471, 477, 604, 622, 623.
recursive, 179, 547. Green’s theorem, 298.
Tapered wave, 119, 142, 154, 180, 198, 254, potential, 18, 19, 293, 294.
270. spherical harmonics, 543.
in spatial domain, 123, 146. spherical waves, 533, 534, 543.
in spectral domain, 120, 124, Vegetation, 594, 642, 667.
Tapering parameter, 119, 179, 204, 323, canopy, 644.
556. Very near field, 203, 327.
TEM mode, 626, Visibility, 587.
Ternary branching, 651. Volume
Testing, function, 23, 515. effective, see Effective volume.
see also Weighting function. elemental, 373.
Third Stokes parameter, 62. exclusion, 29, 31.
Timeaveraged power, 67. scattering, 372, 454.
absorbed, 36, 671. Volume integral equation, 17-19, 27, 483,
‘Toeplitz matrix, 14, 37, 39, 42. 496, 512, 516, 518, 519.
Tones, 150. discretized, 27, 28.
Total correlation function, 409, 411, 425,
430. Wave equation, 62, 70, 95, 119, 120, 373.
‘fransition operator, 376, 379. Waveguide, 594.
‘Transition probability, 465-467. modes, 622, 633.
‘Lranslation addition theorem, see Addition Wavelet method, 179.
theorem. Weak
‘Translation matrix, 488. interaction, 179, 181, 188, 189, 271, 310,
‘Translational invariance, 28, 37, 64, 182, 486.
185, 187, 282, 285, 489. localization, 376.
statistical, 124, 552-555. matrix, 187, 272, 285, 308, 359.
Transmissivity, 82. Weierstrass-Mandelbrot function, 132, 133.
Transmitted power, 82. Weighting function, 23, 25.
Transverse components, 70. point matching, 25.
‘Tree-independent scattering approximation, see also Testing function.
643, 660, 665, 667 Wiener-Hopf technique, 425, 431.
‘Triangle basis functions, 25. Wigner 3j symbols, 536, 541.
Triple bond, 434. Wind speed, 131, 150.
Turtle, 646. Wronskian, 630.
Two media problem, 137.
Zenneck surface wave, 608.
Upward-going, 79, 611, 612. Zero padding, 40, 43.

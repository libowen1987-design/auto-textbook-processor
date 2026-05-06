# Tsang《Scattering of EM Waves》Chapter 4

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 4. The integral equation is next discretized using an evenly spaced
single grid. The surface is discretized into a single grid of N points for z
between —L/2 and L/2, and the «m points are at tm, = (m—0.5)Ar—#, m=
1,2,...,.N. The discretized equations become
N N
SY amnte(tn) + $2 bmn t(@n) = Yine(m) (5.2.4)
n=1 n=1
N N
Ye af), pulzen) + > BY wh(an) = 0 (5.2.5)
n=1 n=l
where u(x) = \/1+[f(x)j20w/On, p = ju/p, and €;/e for TE and TM
polarization, respectively. The matrix elements @inn, bmn; al),, and a),
are, to a first order approximation,
Ay” (krinn) men
Omn = i) (5.2.6)
Aci Hh {kArym/(2e)| m=n
ik f' &n — 2m) — |f (tn) —
Arlt enon =) — flee) — 10) (hyn) mn
= ‘mn
Pn = 9 4 fem) Ae
-_- m=n
20 4n 92,
(5.2.7)
Ar-H (kyrmn) men
Q) 4 5.2.8
Ginn = i) (5.2.8)
~Ari Hy ‘kj Ary /(2e}] m=n
Agi f'(@n)(@n — tm) — [f (en) — FC) 7) (Ferny) men
a) = 4 Tmn
mn 1 fam) Ax _
a+ a 2 m=n
(5.2.9)
where tmn = V/(@n ~ tm)? + [f(@n) = F(am)]? and ym = V1 + [fm ?-
The matrix equation in (5.2.4) and (5.2.5) is in the form of a single grid.
Let n = N/L be the number of points per wavelength. Usually a sample
frequency of n = 10 is taken, meaning that we have 10 points per wavelength.
We shall call such a sampling a single coarse grid (SCG). If the sampling
frequency is two or more times denser than the coarse grid, we shall call it
a single dense grid (SDG). The dense grid that we use ranges from n = 20
to n = 30 in this section.
--- PAGE 223 ---
200 5 FAST METHODS FOR ROUGH SURFACE SCATTERING

2.3 Physics-Based Two-Grid Method Combined with Banded
Matrix Iterative Approach/Canonical Grid Method

Assume that the upper medium is the free space and that the lower medium

is lossy with the following relative permittivity:

e: = e\(1+itand) (5.2.10)
where tan 6 stands for loss tangent. Let \ and A; represent the wavelength
of the wave in the free space and the lower medium, respectively, with
A = A/Rey/e}. The number of sampling points needed in the lower medium
should be Re,/e{ times more than that in the free space.

In the physics-based two-grid method, we use two grids with samplings
per wavelength of neg (coarse grid) and nag (dense grid), respectively. Let
Nag and N be, respectively, the total number of points on the dense grid
and the coarse grid.

r L
Nag = Nagy (5.2.11)
L
N= Neg y (5.2.12)
Let ndg/Neg = m1. For the sake of convenience, we choose nj to be an integer.
We first rewrite (5.2.4) and (5.2.5) using the dense grid.
Nag Nag
DY anntt(en) + YO Pmnt?(@n) = Vine(em) (5.2.13)
nel n=1
Nag Nag
Se al) pun) + 2b d(an) = 0 (5.2.14)
n=1 n=1
The subscripts m,n denote indexing with the dense grid. In the method
of PBTG, the surface fields on the dense grid are calculated. The matrix
elements @m, and bmn represent Green’s function of the upper medium,
while af), and of, represent Green’s function of the lower medium of the
lossy dielectric. We make the following three observations:
(1) The Green’s function in the lower region can have moderate to large at-
tenuation. A medium with a large real part of dielectric constant is normally
associated with a large imaginary part. Let k/ be the imaginary part of ky.
Let rmy be the distance between the mth and the nth parts. If k{rmn > C,
where C is a constant, the field interaction between the mth and the nth
point is vanishingly small. We can define a distance limit as dictated by
--- PAGE 224 ---
§2.3 Physics-Based Two-Grid Method with BMIA/CAG 201
attenuative loss:
Cc =
r= w (5.2.15)
outside of which the lower medium Green’s function’can be set equal to zero.
In the simulation of this section, we let C' be fixed at 1.5.
Based on this observation, we calculate the left-hand sides of (5.2.14) as
follows. We approximate
()
a) x a) = {em Tmn STI (5.2.16)
0 Tmn 271
~ 1
OW), wb), = {tm Tmn ST (5.2.17)
0 Tmn 271
Thus a), and en are banded matrices and (5.2.14) becomes
Nag Nag
Ye al) oulen) + 2 OY, v(en) = 0 (5.2.18)
n=1 n=l
(2) For non-near-field interaction, the free space Green’s function is slowly
varying (spatial frequency limited) on the dense grid. Thus when performing
matrix and column vector multiplication on the dense grid as indicated in
(5.2.13), the Green’s function of the upper medium is essentially constant
over an interval of n; points on the dense grid. Thus we can write
ma ma 1
Va(mtnyins\tinet & mggtny 2 Unt = MAmnpring (T= >, Url
T=1 1 es
(5.2.19)
where l/ = 1,2,...,m1 and the points with indexes Mmp and Nmp are the
middle points between the (m+ lth point and the (m+ ,)th point and
between the (n + 1)th point and the (n + n,)th point, respectively. What is
done in (5.2.19) is that the surface fields on the dense grid are first averaged
before multiplied by the upper medium Green’s function.
(3) The slowly varying uature of Green’s function of the upper medium
only applies to non-near-field interaction. For near-field interaction, Green's
functions G and G; have roughly the same spatial rate of variation. Thus we
need to separate out a distance, say 1A, outside of which G; is much more
rapidly varying than G. Within near field interaction for the upper medium
Green’s function, direct matrix and vector multiplication is performed.
Based on the observations above, we decompose the upper medium
--- PAGE 225 ---
202 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Green’s function into near-field and non-near-field interactions
Nas Nay Nag
YS amnte(tn) = So ahintin + D> aiintin (5.2.20)
n=l n=1 n=1
Nag Nay Nag
LP in) =D Uiantin + Yo Paintin (5.2.21)
n1 n=l n=l
where the superscript s represents near field interactions and superscript ns
represents non-near field interactions. The matrices a},,; Dian: @mn: and bi,
are determined by
se _ famn Tm STF q
dm = {mr mS (5.2.22)
b, Tan <r
s _ J bmn Tn S1F 4
Bian = {? rmn > Tf (5.2.23)
0 Tmn ST.
ns mn STF
On = {on tmn 2 Tf (5.2.24)
0 Tmn STs 5
prs 5.2.5
mn bmn Tmn 2 UF (5.2.25)
Thus ry is the distance outside which the Green’s function of the lower
medium is fast varying compared with that of free space Green’s function.
We use the Greek indices to represent coarse grid and Roman indices
for dense grid. The coarse grid has surface unknowns % and 4, which are
averages of the dense grid surface unknowns. Thus if 7g is centered in the
middle of the n; dense grid points of n + 1,n+2,...,n +1, we have
jig = Unti + Unde +0 + Unt (5.2.26)
nm
be = Unrit Une +17 + Unter (5.2.27)
ny
We calculate Green’s function of the upper medium on the coarse grid. These
are represented by Gag and bag.
- AGH) (bras) Tas >
Gag = gee Wap) Nae > Nf (5.2.28)
0 Tad STF
_ik f'(eg)(@g —%a) — [fF (xp) — f(x
. _agik ft a)(wa a) ~ [fF (wa) = F¢ 1 (era) Tag > TF
bog = 4 Tas ;
0 Tag SUF
(5.2.29)
--- PAGE 226 ---
82.4 Bistatic Scaticring Coellicient and Emissivity 203
where AZ is the coarse grid sampling, Az = n; Ax, and Az is the dense grid
sampling. Thus we use this averaging for the second terms of both (5.2.20)
and (5.2.21). Equation (5.2.13) becomes
Nag Neg N N
DY aiunulen) +2 bntblan)} + | Yo aagi(wa) + D> by0(es)
n=l n=1 6=1 B=1
intp
= Vine(tm) (5.2.30)
In (5.2.30) we use subscript “intp” to represent linear interpolation. Note
in (5.2.30) that re @%,,U(tn) has Nag values of m = 1,2,...,Nag, while
Ngat G4git(w) only has N values ofa = 1,2,...,N. Thus we first compute
N
YS a8, sta) = d(wa) (5.2.30a)
g=1
for a = 1,2,...,N on the coarse grid. To find d(z,,) on the dense grid of
@m, m= 1,2,...,.Nag, we use linear interpolation of d(q)Js to get d(rm)s.
We further use BMIA/CAG to solve matrix equation. We divide non-
near-field intcractions into two regions which are separated by rg. We now
have three distance ranges for the upper medium Green’s function, 0 <r <
rp.rf <7 Sra, and r > rq with different operations. For 0 <r < rf known
as very near-ficld region, we use direct matrix and column vector product.
on the dense grid. For ry <r < rq known as near-field region, we use direct
matrix and column yector product on the coarse grid and interpolation as
in (5.2.30). For r > rg known as non-near-field region, we expand G@gg and
bag in Taylor series as in the BMLA/CAG so that the FFTs can be used
to compute this part of the matrix-vector multiplication. The Taylor series
expansion is as in Section 1
oo za)?"
H (ky/a3 +23) = va) {= 5.2.31
(y/28-+ 22) = > am(na) (24 (62.31)
m=0
Here H represents both HY and HY.
2.4 Bistatic Scattering Coefficient and Emissivity
After the matrix equation is solved, the surface field can be calculated. The
bistatic scattering coefficient o(0,,9;) for the spectral domain tapered wave
is given in (4.1.57).
We next illustrate the numerical simulation results of wave scattering
from a rough lossy dielectric surface for both TE and TM waves [Tsang and
--- PAGE 227 ---
204 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
ee eee
f ahi

ro {- yay .

Bod A Muh Taha

i | ‘ po ie vei

ete il gl mf “i

i Ht \ Hl | i ie ih | an

oa. Wh. i) ae. f mht

An nis it ty iN a . vi .. ON
eC 8 Swegaroe ingen) “SS oo ey
fa) (b)

Figure 5.2.1 Comparison of the bistatic scattering coefficients between the single dense
grid of 30 points per wavelength and the single coarse grid of 10 points per wavelength. TE
wave, rms h = 0.5, correlation length of ! = 0.6A, dielectric constant of ¢, = 25 + i, surface
length of L = 100A, and tapering parameter of g = L/4 at incidence angle of 6;. (a) One
realization, (b) 20 realizations.
Li, 1997; Li et al. 1999]. Simulations are based on Gaussian random rough
surfaces with Gaussian correlation functions. First, we show the comparisons
of bistatic scattering coefficients and surface fields based on a single dense
grid (SDG) and a single coarse grid (SCG) with a complex dielectric constant
of 25+, surface length of 100 wavelengths, and at an incidence angle of 30°.
The results show that the dense grid is required for the case with large
dielectric constant. We shall regard the SDG results to be correct. Next, we
compare the results based on PBTG-BMIA/CAG with that of SDG. Then
we use the PBTG-BMIA/CAG method to calculate the cases with large
surface length and compare with SDG.

The tapering parameter was taken to be L/4 for the case of surface
length of 100 wavelengths and L/8 for the case of surface length of 500
wavelengths at near-grazing incidence. The critical distance ry that defines
the very near field is fixed at 1 wavelength. The cases with a surface length of
100 wavelengths were run on a SPARC 20 workstation, and the cases with
a surface length of 500 wavelengths were run on a Pentium-Pro Personal
Computer with a clock rate of 200 MHz.

a) Comparison Between a Single Dense Grid and a Single Coarse Grid

In Figs. 5.2.1a and 5.2.1b, we compare respectively the results of the bistatic
scattering coefficients of a single realization of rough surface and averaged
over 20 realizations for a TE wave, at incident angle 0; = 30°, and surface
--- PAGE 228 ---
§2.4 Bistatic Scattering Coefficient and Emissivity 205
7 2 | a) a
fH ke oh oS
i| ae eer
i | dal Wl Hh ree |
ya! ' t ' ry | eat wy Mat hh
i red | re kt ere
. | a sol | et
me hth ioe i PTW
TONING lady a S
ir ang eee) iin a oe)
(a) ()
Figure 5.2.2 Comparison of the bistatic scattering coefficients between the single dense
grid of 30 points per wavelength and the single coarse grid of 10 points per wavelength. TM
wave, rms A = 0.5A, correlation length of / = 0.6A, dielectric constant of €, = 25 + 7, surface
length of L = 100A, and tapering parameter of g = 1/4 at incidence angle of 6; = 30°.
(a) One realization, (b) 20 realizations.
length L = 100A, where A is the wavelength. The rms height and correlation
length are 0.5 and 0.6 wavelength, respectively. We compare the cases of
SCG of meg = 10 and SDG of ngg = 30 points per wavelength. We note
that the results of SCG and SDG are quite different both for one realization
and for averages over 20 realizations. The results based on SCG are not
accurate. The comparisons were also made in Figs. 5.2.2a and 5.2.2b for a
TM wave with the same parameters. It is noted that the performance of
SCG is poorer for the TM case. This is because more energy is transmitted
into the lower medium for the TM case than for the TE case, and the lower
medium dielectric requires a dense discretization. In Figs. 5.2.3a and 5.2.3b,
we compare the surface electric fields between SDG and SCG for TE and TM
waves, respectively. In Table 5.2.1, we compare the emissivities calculated for
using one realization and 20 realizations for SCG and SDG for both TE and
TM waves. We found that for SCG the emissivity is 0.614097, while for SDG
the emissivity is 0.592344 for one realization of a TE wave. The difference of
emissivities of 0.021753 can give a difference of 300 K x 0.021753 = 6.53 K
in brightness temperature. Even after averaging over 20 realizations, the
emissivity for SCG still has a —0.013456 difference from that of SDG. For
a TM wave, the difference of emissivity is much larger. It is —0.061699 for
one realization and —0,092587 for 20 realizations. This gives differences of
18.5 K and 27.78 K in brightness temperatures, respectively. Thus SCG is
not accurate for problems of large dielectric constant and cannot be used
to calculate the emissivitics. In Table 5.2.2, we compare the CPU. We note
that although SDG is accurate, it requires much more CPU than SCG.
--- PAGE 229 ---
206 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Method Tad Polar | Number of | Emissivity | Difference of
zation | Realizations Emissivity***
Ese 0.021753
SbG** TE i osoasss | 0 |
soa} 0
a
PBTG-BMIA/CAG | 10 and 30 0.768926 | 0.003697
cheat mena
$cG TE 20 0.592318 = 0.013456
ee 7
SDG 30 T™ 20 | O7o4i53 0
PBIG-BMIA/CAG | 10 and 30 20 0.797086 0.002933
*SCG = single coarse grid *“SDG = single dense grid
“The difference of emissivity means the emissivity minus the emissivity of SDG.
Table 5.2.1 Comparison of emissivities based on PBT'G-BMIA/CAG and single grid method
(L = 100 wavelength).
, = bo rote-— eee
cof remmencomcy |. Bs | = ag
oe t ~ 7 T 1
\ \ ' 1k
al i } | phy thee i
= ad 4 gali Wcy fi » iy /
Pel bg Ph A AN ake | A nan het kag
Cobh ae WU Ys hh ie ti ti} it llth
SW ine CUAL A filth Pal PA PU ee
pel Pi WA) Uh Abi H bMS Vee ini Whe
rt oth a Mia Be yy Vy oy PW UNG at
it ef yt 1 ey H (a my
ol 4 fo a 1 | } :
i 4 i my | ' | ' 4
or u Ww |
(a) 0)
Figure 5.2.3 Comparison of the surface fields between the single dense grid of 30 points per
wavelength and the single coarse grid of 10 points per wavelength. rms h = 0.5. correlation
length of I = 0.6,, diclectric constant of ¢, = 25+, surface length of L = 100), and tapering
parameter of g = L/4 at incidence angle of 0; = 30°. (a) TE wave (b) I'M wave.
--- PAGE 230 ---
§2.4 Bistatic Scattering Coefficient and Emissivity 207
=
unknowns | zation | per iteration | iterations | time (s)
conn
SDG 30 6000 TM. 77.0 108 8333.2
Table 5.2.2 Comparison of CPU based on PBTG-BMIA/CAG and single grid method
(1 realization and L = 100 wavelength)
b) Comparison Between a PBTG Combined with BMIA/CAG and a
Single Dense Grid
In Figs. 5.2.4a and 5.2.4b, we compare the results of the bistatic scattering
coefficients respectively obtained from a single realization of rough surface
and averaged over 20 realizations of rough surfaces using SDG and PBTG-
BMIA/CAG for a TE wave. For PBTG-BMIA/CAG, the two grids are used
with reg = 10 and ngg = 30. The results obtained by PBTG-BMIA/CAG
are almost identical to the SDG results. In Figs. 5.2.5a and 5.2.5b, the com-
parisons are made for a TM wave which also show that PBTG-BMIA/CAG
can give almost the same results as SDG. The comparisons of the surface
fields between SDG and PBTG-BMIA/CAG for TE and TM cases are shown
in Figs. 5.2.6a and 5.2.6b, respectively. The agreements are good. The emis-
sivities calculated by SDG and PBTG-BMIA/CAG are compared in Table
5.2.1. The emissivities calculated by PBTG-BMIA/CAG are very close to
those of SDG for TE and TM waves. The difference of emissivities averaged
over 20 realizations between SDG and PBTG-BMIA/CAG is —0.007889 for
a TE wave and —0.002933 for a TM wave. This leads to maximum differ-
ences of 2.3667 K and 0.8799 K in brightness temperatures, respectively. We
also compare the CPU between PBTG-BMIA/CAG, SDG, and SCG. In Ta-
ble 5.2.2, we give the comparisons of the total CPU and CPU per iteration
based on PBTG-BMIA/CAG and single grid methods for one realization.
The total CPU of PBTG-BMIA/CAG is slightly larger that of SCG. But
the CPU of PBTG-BMIA/CAG is still several times smaller than that of
SDG.
--- PAGE 231 ---
208 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Esme | : | | ir =o a |
[ePrice [=rremetoe |
1 | o26| \
| {h
fea | Lo bad rr ih
ho | a A
foo ily pe fle a
Ht I | |, Ploy y MPM
HWW |
; ;
09 4
ul fii \ \ cot | Ww
AN I \
. pi RAEI ye Uo NN
a ls sas
Fw eacnmce
(a) (b)
Figure 5.2.4 Comparison of the bistatic scattering coefficients between the single dense
grid of 30 points per wavelength and the PBTG-BMIA/CAG with rp = 1. TE wave, rms
h = 0.5A, correlation length of | = 0.64, dielectric constant of 6 = 25 + i, surface length
of L = 100d, and tapering parameter of g = L/4 at incidence angle of 8; = 30°. (a) One
realization, (b) 20 realizations.
= iio [Swett |
fad :
i Ln
r f «ah
fe
i ba allan ltl tual ny | |
few i] al Hh Vath Ald |
| \ | Wl 4 yt
Tr ali sok “| ey,
LAA NN alt ta w oS
a i
(a) (b)
Figure 5.2.5 Comparison of the bistatic scattering coefficients between the single dense
grid of 30 points per wavelength and the PBTG-BMIA/CAG with rp = 1\. TM wave, rms.
Ah = 0.5A, correlation length of | = 0.6A, dielectric constant of ¢- = 25 + i, surface length
of L = 100A, and tapering parameter of g — L/4 at incidence angle of 6; = 30°. (a) One
realization, (b) 20 realizations.
--- PAGE 232 ---
§2.4 Bistatic Scattering Coefficient and Emissivity 209
‘ ee " TWWAVE MOIDENCE
sal rewavenoncxe (= BE ead| , \ == RBEReaa| |
af ‘ |
ood Ar , ||
i . Py A t
Cha wad cate a TNA fy DA RR
iil ww AY Aad i Ht 8 HET It
bul HRW ie i | Tia ha MULT |
2 Ai la! Uo) alba H WM VARY | i
pry VET ATU SNe ITT
Bal yoy Bey \ | | MN \
“f i [ i | |
fe
a Pt
(a) (b)
Figure 5.2.6 Comparison of the surface fields between the single dense grid of 30 points
per wavelength and the PBTG-BMIA/CAG with rz = 1A. rms h = 0.5, correlation length.
of 1 = 0.6A, diclectric constant of ¢, = 25+ %, surface length of L = 100A, and tapering
parameter of g = L/4 at incidence angle of 0; = 30°. (a) ‘TE wave, (b) TM wave.
rT eee a
Peeks || | TE |
| |
fos fod
{ ey
bus fos! |
i | ; | |
je | j je | |
a iA Mh iy |’ “i HN!
\ ! \
iL Gd
ca) o 40 20 oO 2 oO cy 80 “0 20 0 20 o 8 CJ
amacontadee Boones
(a) (b)
Figure 5.2.7 Comparison of the bistatic scattering coefficients between the single dense grid
of 20 points per wavelength and the PBT'G-BMIA/CAG with rz = 1) for one realization.
rms h = 0.3A, correlation length of | = 0.54, dielectric constant of c, = 17+ 7, surface length
of L = 500A, and tapering parameter of g = L/8 at incidence angle of 8; = 30°. (a) TE wave,
(b) TM wave.
--- PAGE 233 ---
210 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Me | ts i ceU Ea
Method surface angle |zation |Emissivity |time (s) per | itera- time
unknowns } iterations tions (mins)
IPBTG-BMIA/CAG | 20,000 [30 | TE 984 | 1579
PBTG-BMIA/CAG | 20,000 30 | TM
spG 20,000 0.140012 [40.72
PBTG-BMIA/CAG | 30,000 | 85 202 | 68
Table 5.2.3 Comparison of emissivity and CPU based on PBTG-BMIA/CAG and SDG
method (1 realization and L = 500 wavelength).
c) Comparison Between a PBTG-BMIA/CAG and a SDG for the Large
Surface Length Case
In Figs. 5.2.7a and 5.2.7b, the bistatic scattering coefficients obtained by
PBTG-BMIA/CAG and SDG, respectively, are compared for the case of a
large surface length of 500A, an rms height of 0.3A, a correlation length of
0.5A, and a dielectric constant of 17 +i at incidence angle of 30° for one
realization for both TE and TM waves. In this case, SDG has 20 points
per wavelength. PBTG-BMIA/CAG is with neg = 10 and ngg = 20. The
agreements are good. The comparisons of emissivities and CPU are shown
in Table 5.2.3. The uses of PBTG-BMIA/CAG with Neg = 10 and Ndg = 40
are shown shown.
d) Backscattering Coefficients from a Rough Surface with a Large Di-
electric Constant at Near-Grazing Incidence Angle
We also compare the bistatic scattering coefficients between a PBTG-BMIA/
CAG and an SDG at an incidence angle of 85° in Figs. 5.2.8a and 5.2.8b.
In this case, other parameters used are the same as the Figs. 5.2.7a and
5.2.7b. The agreements are good except for a small difference in the forward
scattering directions. It is important to note that PBTG-BMIA/CAG gives
accurate results in backscattering direction.
In Fig. 5.2.9a, we show the bistatic scattering coefficients of TE wave
at 85° incidence angle averaged over various number of realizations. In
--- PAGE 234 ---
§24 Bistatic Scattering Coefficient and Emissivity 211
yo —
—- | aw h
10} |= pareemacas A [_ Peronoaa i
heel ig (
Ey ‘isang iAAbilttha/ Be :
£2) yh NO HAINTT | Fa MMMM
a) agli f eae Nt) thy
300 ah it eral IN! y i! nl i
al iat rey
ie j |
| : |
“| | !
ee a
Smaate tts Brora ct
(a) )
Figure 5.2.8 Comparison of the bistatic scattering coefficients between the single dense grid
of 20 points per wavelength and the PBTG-BMIA/CAG with rf = 1A for one realization.
rms h = 0.32, correlation length of / = 0.5, dielectric constant of ¢, = 17 +4, surface length
of L = 500), and tapering parameter of g = L/8 at incidence angle of 6; = 85°. (a) TE wave,
(b) TM wave.
Ey =
oes i (vere 20
~sdenenen | ‘sean
| —
a. it og
7 marr) H _-
rl : a
ry of LP a
| / | de |
gy | | 8 ed \
| ’
Ce a a a
tao eons ree aren
(a) )
Figure 5.2.9 Comparison of the bistatic scattering coefficients averaged over various number
of realizations calculated by PBTG-BMIA/CAG with rf = 1) and using the dense grid of 30
points per wavelength and coarse grid of 10 points per wavelength, TE wave, rms h = 0.5,
correlation length of [ = 0.6, dielectric constant of ¢. = 25 +i, surface length of L = 500A,
and tapering parameter of g = 1/8 at incidence angle of 8; = 85°. (a) Entire range of
scattering angles, (b) vicinity of backscattering direction,
--- PAGE 235 ---
212 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
ofr tomas | A ea |
acces i 1 | tran 00 a

§ nd € a
1 jh —
a wo be a
ry f j { Lo
pr / poy
ol | ° |
a a io = 2 a7 % = 8 we we H w
sotern wg ere) scaeng age es)
(a) (b)

Figure 5.2.10 Comparison of the bistatie scattering coefficients averaged over various

number of realizations calculated by PBTG-BMIA/CAG with rz = 1A and using the dense

grid of 30 points per wavelength and coarse grid of 10 points per wavelength. TM wave, rms

h = 0.5A, correlation length of | = 0.6A, dielectric constant of ¢, = 25 + i, surface length

of L = 500A, and tapering parameter of g = L/8 at incidence angle of 6; = 85°. (a) Entire

range of scattering angles, (b) vicinity of backscattering direction.

Fig. 5.2.9b, we zoom in and show the bistatic scattering coefficients in the

vicinity of backscattering direction. In Figs. 5.2.10a and 5.2.10b, we show

the corresponding results for a TM wave. We take the surface length of 500

wavelengths, an rms height of 0.5,, a correlation length of 0.6, and a dielec-

tric constant of 25 + i. In PBTG-BMIA/CAG, we use two grids of neg = 10

points per wavelength and ngg = 30 points per wavelength. We found that

50 realizations are required for convergence of backscattering coefficients for

TE waves and 70 realizations are required for TM waves.

3  Steepest Descent Fast Multipole Method

The fast multipole method (FMM) was invented by Rohklin [Rohklin, 1990;

Coifman et al. 1993]. Michielssen and Chew [1996] used the steepest descent

method to express the product of impedance matrix and column vector.

Jandhyala et al. {1998a,b] applied the steepest decent fast multipole method

(SDF MM) to 3-D rough surface scattering problem. Recently, FMM has been

applied extensively to large scale electromagnetic boundary value problems.

SDFMM has also been combined with the PBTG method [Li, 2000]. In the

following, we apply the method for one-dimensional rough surface for the

Dirichlet problem, In Sections 3.1-3.4, the theoretical analysis is presented.

In Section 3.5, the computational algorithm and the computational com-

plexity of the approach are given.
--- PAGE 236 ---
§3.1 Steepest Descent Path for Green's Function 213
3.1 Steepest Descent Path for Green’s Function
The Green’s function is
i
9 (7,7) = 5H (|r 7") (5.3.1)
with plane wave representation
g (2,2) = if” dkzclteltgthe: L 66.3.2)
, ao ke ~
Later on zg > 2-2’, z 4 2-2',
The integration contour is on the real k, axis. Next we make transfor-
mation to complex angle.
k, = kcosa = kcos(a! + ia”) = ki, + ik! (5.3.3)
ke = ksina (5.3.4)
Balancing real and imaginary parts
ki, = kcosa’ cosh a” (5.3.5)
ki! = —ksina’ sinha” (5.3.6)
Similarly for ky
Ki, + ikf = ksina’ cosh a” + ikcosa’ sinh a” (5.3.7)
We also have dk, = —ksina da.
The original contour integral is now in the complex a plane and is de-
noted the Sommerfeld integration path (SIP)
yt kl2| sin a-Like cosa 5
g(x, 2) = =[ da e* (5.3.8)
4n Jsip
The Sommerfeld integration path extends from a = 0 + ico to a = 0 along
the imaginary axis. It then goes from a = 0 to a = 7 along the real a axis.
Finally it goes from a = 7 to a@ = m — ioe (Fig. 5.3.1). Since |x| > |z|, the
dominant exponential term is
eikle|sin a _ pi(ksina’ cosh a’’+ik|a| cos a’ sinh a”)
= cikle|-Kizl cosa’ sinha” (5.3.9)
The steepest descent path T is defined by
Re(sina) = 1 (5.3.10)
so that
sina’ cosh (a) = | (5.3.11)
--- PAGE 237 ---
214 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
a!
ky = oo fiat
tea
Agi
An.
FE : x
oF 2 ol
k=k net
7
os
ay
cc
a
Figure 5.3.1 Stecpest descent path and Sommerfeld integration path (SIP).
The saddle point is at a = 7/2. The steepest descent path P is a contour of
constant phase for the dominant exponential term, the amplitude of which
decreases rapidly away from the saddle point.
In the vicinity of (a’,a") = (3.0), by letting a’ = 5 + 3, we have
sin(Z + 8) cosha” = 1 or cos Bcosha” = 1. For small @ and a”, the equa-
q mya
tion becomes (1 ~ £) ( + co) = 1, giving a’ = —8. Thus the steepest
descent path T has slope = —1 in the vicinity of (a’,a") = (§,0) as shown
in Fig. 5.3.1.
Since the major contribution comes from the vicinity of a’ = 5, the
integration can be discretized as follows:
i ik|x| sin a-biks cosa
x,z)=— | dae’
g(w.2) = 7 f
i Q
_ 2 ikl] sin ag +ikz COs Oey A, 5.3.12
= e a, 5.3.
dn > 4 ( )
q=l
If we use the transformation Ane, = 7 — a@ and then let Qnew — a, we have
tf 7 .i&|2| sin a—ike cosa
g(x.z) = — | dae"
oed=z ff
iS um
_ ik|a| sin ag—ikz cos a, 5.3.13
=—) e * “Aa, 5.3.13.
4n » 1 ( )
--- PAGE 238 ---
§3.1 Steepest Descent Path for Green’s Function 215
where Q is the number of angles. This means that the sign of the cosine term
in the exponent in (5.3.12) can be switched. Let BW be the bandwidth on
either side of a’ = §, We sample evenly on the a’ axis with interval Aa’.
Let the number of angles Q be an odd integer.
2(BW
Aad! = uM (sample evenly on real a’-axis) (5.3.14)
ig = af, + tay (5.3.15)
an R<
a= a7 (BW) + (q— Aa!’ (5.3.16)
1 1
osha!’ = _ 5.3.1
cea Sina, cosB (6.3.17)
Note that a7 is an odd function of 3, ay > 0 for a < 5 and af < 0 for
al, > 5. The selection of BW must be large enough to ensure that integrand
becomes small enough. Note that BW depends on ||. When |z| is small the
contribution is from larger range of a. The worst case and the largest BW
corresponds to |z| = 2min, Where Zin is the minimum separation in a. It is
required that
kemin( BW)? > 1 (5.3.18)
Let
BW= a (C; = large constant) (5.3.19)
Vkemin
On the other hand, the selection of sampling Aa’ must be small enough to
ensure enough sampling of the integrand. The worst case and the smallest
Aa! corresponds to || = &max, Where max is the maximum separation in
a. It is required that
ktmax(Aa')? <1 (5.3.20)
Let
kamax(Aa’)? = C, (C, = small constant) (5.3.21)
Cs 4
Ad’ = —— (5.3.22)
Thus the number of sampling points is on the order of
BW Cy [&max )
=O a) =O (Gr oe 5.3.23
Q ee CSV tmin 6 )
Note that Q can be a fixed constant if
mex — constant (5.3.24)
Emin
--- PAGE 239 ---
216 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
In the multilevel grouping, the division of groups is such that %max/min is
the same for each level.
3.2 Multi-Level Impedance Matrix Decomposition and Grouping
In the fast multipole method, the impedance matrix elements are decom-
posed into various levels based on multilevel grouping. To illustrate, let the
number of elements in the {st level group be M and the number of groups
of the Ist level be Z. Then the total number of elements is N = LM (c.g.,
M = 20, L = 64, then N = 1280 — We use this case as an illustration in
this section. Generalization can readily be made to other values of M and
L). Let L = 2+1, where p corresponds to the level of decomposition of the
impedance matrix. The first level groups have M elements each. Beyond the
first level, the number of clements increase by a factor of 2 for each higher
level. Level 1 group has M elements, level 2 group has 2M clements, level 3
group has 27M elements, and so on. For L = 64, p=5
level of group # of elements # of groups
1 M 64
2 2M 32
3 4M 16 (5.3.25)
4 8M 8
5 16M 4
6 32M 2
The grouping as shown in Fig. 5.3.2. Group m at level n is denoted as mp.
The impedance matrix is decomposed as (p = 5 for this case)
= 50 sQv sev sQU sav sau
Z=Z 042420 47°42" 42°
SWL =2)L sQL s@L s)L
+Z 0 +2 0° +2 0 °4+2 0°42 (5.3.26)
where the number in the parenthesis stands for the level of the group, super-
script U and L denote the upper matrix and lower matrix respectively. The
upper matrix has column index larger than row index for nonzero elements.
It is the reverse for the lower matrix.
sl
Let Z,,n, denote the interaction of elements between group m,; and
group n; in level i. They are all full matrices.
s(t
Zz, = dimension M x M (5.3.27)
P=
Zz. = dimension 2M x 2M (5.3.28)
- 0) . . 0) 5. .
Note that Z,,,,,, are defined differently from Z". For example, Z is of di-
--- PAGE 240 ---
§3.2 Multi-Level Impedance Matrix Decomposition and Grouping 217
; —_—
UN. 2d
J /\ KY JW
AAAAAAAA
IN 2 8 4) By BT) 8 WO Ay 12) Uh My TS) 16,
12345...M
Figure 5.3.2 Multilevel fast multipoles structure.
ear are BA) . . . ae
mension N x N while Z,,,,,, is of dimension 2M x2M. The various definitions
of impedance matrix elements should be distinguished.
=(1
a > = zero matrix of dimension M x M (5.3.29)
=(2
3°” = zero matrix of dimension 2M x 2M (5.3.30)
=i) . . : . .
0. = zero matrix of dimension (iM) x (iM) (5.3.31)
Suppose we use M = 20. Then examples are
=) Zao. ***  Za1,180
Z3.9, = : a : = 20 x 20 (5.3.32)
20,161 «++ 260,180
(2) gy Z
Zs,9, = [23° | = 40 x 40 (5.3.33)
2637, 2618
sHY 52) = eae .
Thus Zyrrnys Zrasna? Zang: tC. keep track of all the individual impedance
matrix elements.
. FO . .
The (th level impedance matrix Z represent interaction at level 1
--- PAGE 241 ---
218 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
between itself and its neighbors on the two sides.
BM 5) =(1) =(1)
ane Zany on) 0 che
sQ) sQ) sa =(1)
=) | 421 ane 22,3, ° us
Zo =} eH Sh 5 3) =NxN 5.3.34
0 23,2, 43,3, 434, °° ( )
=(L =(L
a? a” a ee eee
0) . .

For Z, the impedance matrix clements can be calculated accurately by

using near field integrations.

In the multilevel fast multipole method, the impedance matrix of each
level is generated by following rules:

(i) In each level, the impedance matrices only interact with itself or its
nearest neighbors. _

(ii) Each impedance matrix element in Z can occur only once in the matrix
decomposition. If a pair had interacted previously in lower level groups,
it cannot interact again in the current level. That entry has to be set to
zero at. the current level.

sl
To generate the next level, i.c., 1st level impedance matrix Z ( a we first
apply rule (i) to get the NV x N matrix

=sQ2) sQ =(2) =(2)

sQ@) <Q) s@ =(2)

Zo1y 423, 22. ¥ =

=2) =) =2) =(2) 5.3.35,
0 23.2, 230%, 23nd. °° ¢ )
=(2 =(2)
5” 5” wee see eee

However, according to rule (ii), the diagonal matrix elements should be set

=

to zero because they have already interacted in Z' ) Setting them to zero

then gives

=2) 52) =) =(2)

a ) Z\», a ) rh .

=(2) =Q2) =(2) =(2)

Zoi, 9 2234 ¥ aa

=(2) =) <Q) (2) 5.3.36
) 23,2, 9 23x42 °° ‘ )
=(2 =(2

a z fit ) _ cee nee
--- PAGE 242 ---
§3.2 Multi-Level Impedance Matrix Decomposition and Grouping 219
However, in
sl) =s0)
32) Z: Zi .
Zi,2, = [Fi a (5.3.37)
223, Sad
5 . BO) a.
Zo,3, has already been included in Z . Thus, we set that entry to zero also
and define, with a prime superscript,
su st)
02" Z Z
Zi, = [7 nis Z | = dimension 2M x 2M (5.3.38)
0 22.4,
Similarly, we define
=) =(1)
sy Z, 0 ae
Zo, = [2 =) | (5.3.39)
441, 242
Thus, the first level impedance matrix assumes the final form:
se) =(I)U s)L
2-72 (5.3.40)
=) =Q2) =2 =(2
5? Zo q? 7 ...
(2) =(2) S02)’ =(2)
a Oe
FT? 0 0 A
=2)  =(2
a? 5 see ee aes
=) =) = SM =f)
Oo” 0 213, 414, 0 _ _ ws
=(1) =) =(1 (1 =(1 =(1
TO WP
=) =) sM s@ =H
ale. = 06 0 23,5) 20 i) vee nee
=(1 =) s(t =(1 =(1
ern er Za, 0 a ee
=) sl) 1) S01)
rs | 0 25.7, 25,6, vee
=(1 =) =
cee nee see vee vee a? ih 2, see
(5.3.41)
--- PAGE 243 ---
220 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
=(2 =(2) =(2) =(2
oe De v5 De ~
(UL Zon, 0 o 0) _
FZ - | =(2 sy’ =2) =(2
Ze =10? 2, 0? 9?
= =(2
WGP
=(1
0 cay ts
Jy My ae
Zsa 0 0 see res
st) sa =(1 =(1 eae
= Zi», ZB, a ) a ne (5.3.42)
=(1 =(1 =(L =(1 =(1
a? iii Zs, GF? FP.
=) =) =) x(l)
see 0 26.3, 26.4, 0 bee nee
For the 2nd level impedance matrix, we have
SQ) sQU sb
Z° =F" £7 (5.3.43)
Note that:
so (70, 72
Zi,2, = Ey 7 (5.3.44)
22.3. 42.4
=
But. Ze, has already been included in previous level impedance matrices
sO sOv sa . . .
Z orZ +24 ~ . Thus, we set that part to zero and define, with a prime
superscript,
gy 72, #
Zi,9, = oy 2 | = dimension 22M x 22M
0 2,4,
so sO sQ SM)
pik Be Si Se
= =(1 =(1 =
al ae (5.8.45)
0 0 Zs, " 28,
= = sd) =
0 0 4a, Zaza,
Similarly, let
3?) = +2)
sy _ |Z, 0 53.46
2x1, = [7a S02) | (5.3.46)
Ziyi, 24,2.
--- PAGE 244 ---
§3.2 Multi-Level Impedance Matrix Decomposition and Grouping 221
. Be,
Thus the 2nd level upper matrix 7 is
=3) =@Y =) =
2 Fo.
=3) <3) =) =)
Zr 1) =) “ase wy
~ 10 0 o Zig _
=) =(3
Fike 5° cee bee eae
=2) =2) S02) s(2) =(2)
0 0 Zia, Zax a beeen eee
=2) =2) =2) <= =(2 =(2
52 72 5 Zz, GF
=2) =2) =@) =@ =(2
= =(2 =@) = =(2) =(2
ce BO ZB GO A
=(2) =(2) (2) -=(2)
sep tte see ee 0) 25074 2558, us
=2) =) =@
see nee nee see |) 0 Zoosk, °°
=Q) =) =) =) sQ SM Ss) 3s) =(1)
a) 2 » x = aie a ah 74 =) -
=) =) =) <0) Ss) SQ) sa) s =(1
0’ 0° 0 OY Zs, Za, Zan Za. 0 a
=) =) =(1 =(1 = = =(1
wre a” a” 5” 0 23.7, 23,8, a a
=) = =i) =) sa =(1
ee
=(1 =(1 =(1 =) =(
ce ee ee GD FD FO FO Zs,9, °°
=(I =(1 =) =)
ve ee ee ee FD FO FO Zoo, 0
=U) -=(l
bee ee ee nee tee tee tes 5” x” see
(5.3.47)
SDL
A similar expression can be found for Z
a oe . . 3)
Similar derivation can be applied to higher levels. For level 3, Z- =
SOU sG)L
Zz » 4% » , with
--- PAGE 245 ---
222 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
=(4) =(4)’ =(4 =(4
a Fy
=(4) =(4) =)’ =(4)
i OT a Oe
oO Za
=(4) (4)
rie 5” _ eee
=(3) =(3) <3) =s@ =(3
0 FZ We
=(3) =) =3) (3) =(3) =(3
i” i” i” Zs, 5° i a oe
=(3) =(3 =3 =(3 a(S)
settee a a” Z., 2, a” see tee
= (3) (3) 3) (8) 13)
ee nee nee 0 0 Ze 0 0 _
=(3) =3) = st
vee nee nas v0 ) 25515 2o98, uo
=(3 =3) =
pee eee nee _ wee ” 0” Zoxas 00
(5.3.48)
=(3)b
A similar expression can be found for Z
Continuing in this manner, the original impedance matrix is decomposed
=6) =6U S(O)L
up toZ” =7” +7 :
3.3 Multi-Level Discretization of Angles and Interpolation
Because of the manner the impedance matrix elements are grouped at various
levels, a constant 2max/Xmin ratio in different levels of Zz” is maintained.
( E00)
Figure 5.3.3 illustrates the ratio w/a), for level 1 group in Z. Note
that. ro). and 2) are as shown because we have deleted those elements that
sO
belong to Zz! ».
0)
In Z
wQ) 2 4M Ar (5.3.49)
aw) ~ MAx (5.3.50)
(1)
Snax _ 4 (5.3.51)
py
min
--- PAGE 246 ---
§3.3 Multi-Level Discretization of Angles and Interpolation 223
ly Qo
i : MN vIN
12345- j i of
i eo i
Po gl Me Ar po
i Le SE *g
po 3M. Ax {
es
‘ a) =4M - Ac
Figure 5.3.3 The 2max/2min ratio for level 1 group. 2max/stmin = 4
Is 23
hh 24 31 44 By 61 ven 8
12345. Pg it
i i 3M. Az i ci
i 7M: Ax ‘ot
o2=8M-Ar
Figure 5.3.4 The 2max/tmin ratio for level 2 group.

. aa: 2 (2) 7 (2) ‘ . B)
Figure 5.3.4 illustrates the ratio 2max/2,5;, for level 2 group in Z . Note
that 2). and 2?) are as shown because we have deleted those elements

(0) =) =)
that belong to Z| and Z. In Z

a2) ~ 4(2M)Ar (5.3.52)
2®) ~2MAx (5.3.53)

2?)

aS =4 (5.3.54)
(2)

Thin
--- PAGE 247 ---
224 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Similarly, / 2 = 4 for gencral level i. Because of the ratio of 2, | 2)
is equal to 4 for all levels, the nu-nber of angles Q in each level is kept constant
by (5.3.23).
Thus from (5.3.22), the sampling interval of angles in level i is,
Aati) = Os (5.3.55)
vag |x|
acy | febe| 2c, 4c;
we Oe | PT Gt ig Bt 535
Qe C, Fg I~ G 2 C. (5.3.56)
‘min
Thus if we choose C; ~ 3, Cs = 5 then Q can be rounded to 37. Let
Q=37 (5.3.57)
2, = 2'"(4MAz) (5.3.58)
From (5.3.22),
rT
Aa) = —3__ (5.3.59)
yk |xlch
BW! = (>) Aa = 18A0' (5.3.60)
For example, let M = 20, Ax = #,, then for i=1
Qo = 4(20)5 =8\ (5.3.61)
1
3 1
Aal) = —3__ = —__ = 0,047 rad (5.3.62
ae. 37.08) (5.5.62)
Vo
BW) = 0.846 rad (5.3.63)
For i= 2
rh) = 16. (5.3.64)
Aa) = 0.033 rad (5.3.65)
BW®) =0.6 rad (5.3.66)
We tabulate af), a), and af) in Table 5.3.1. Note that the sct of angles
--- PAGE 248 ---
§3.3 Multi-Level Discretization of Angles and Interpolation 225
0.7245 +0.9703i | 0.9724 40.6371 | 1.1477 + 0.43641
0.7715 +.0.90114 | 0056 + 0.5979% L712 + 0.41074
0.8185 + 0.8353¢__| 1.0389 + 0.5589% | 1.1947 + 0.3853%
0.8656 + 0.77221 | 1.0721 + 0.52071 | 1.2182 + 0.36028
1.1054 + 0.48324 [1.2417 + 0.3352
0.9596 + 0.6533) | 1.1386 +0.4a6ai | 1.2652 +0.31052
1.0066 + 0.5967% | 1.1719+0.4100i | 1.2887 + 0.2859%
1.0536 +0.5419% | 1.2051 +0.37414 | 1.3122 + 0.26154
9 11006 + 0.48851 [1.2383 +0.3388% [1.3357 + 0.237%
10 [| L147? + 0.43647 [1.2716 +0.30381 | 1.3592 + 0.21321
1.1947 +.0.3853i | 1.3048 + 0.26921] 1.3827 + 0.18927
1.2417 + 0.33521 | 1.3381 + 0.2348i_ | 1.4062 + 0.16532
1.2887 +. 0.28591 | 1.3713 + 0.208%
1.3357 +0.23781 [1.4046 +0.1670i | 1.4533 + 0.11785
1.3827 + 0.18924 | 1.4378 +0.13341 [1.4768 + 0.09422
16 | 1.4207+0.14151 | 14711 +0.09991 | 1.5003 + 0.07067
1.4768 + 0.09421 | 1.5043 + 0.0665¢ [| 1.5238 + 0.04701
1.5238 + 0.04701 [1.5376 + 0.03331 [1.5473 + 0.02351
TTS
Table 5.3.1 The ag angles for the first three levels. Parameters used: M = 20, Ax =
A. Q=37.
for g > sot = 19 is symmetrically placed on the lower half of the complex
@ plane.

Interpolation rules have to be established for interpolation functions of
one level of angles to another level of angles. The set of angles for lower level is
of larger range than the set of higher level angles. Clearly BW) > BWe+),
Thus a function of f (adit) can be obtained from interpolation of the set

(@)

Fag").
Let Inf? (of), a) be the interpolation functions. Then
. (i) (i)
+1) _ i41 i é 2
FAD) = SF MO (al, a) Fal?) (5.3.67)
q=1

A simple way is to choose a two point lincar interpolation. For example,
from Table 5.3.1, the of) falls between og? and ol) in the steepest descent
path.
--- PAGE 249 ---
226 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Thus the linear interpolation is
Dy(g@ _ My (,2) — y®
b(a?) = F(aio ag” = a9") + Flag )(ag" = a0) (5.3.68)
a) 4 @ (@) Gd
40 — %% ag" — 9
The linear interpolation function is
2) 1
ofa
=
(1) _ a
Wag) ot
Iny (ag Oy’) = a) _ af) a (5.3.69)
aa 7 = 10
10 — &%
0 all other q' values
Other J: ni? (a?.a?) can be obtained similarly.
3.4 Steepest Descent Expression of Multi-Level Impedance Ma-
trix Elements
‘The location of group centers of each level can be defined. For example in
the first level
Xi, = atest tie (5.3.70)
M
Xp, = EM4i+@2My2+F%my3t+'*+2oM (5.3.71)
M
For higher levels, we can define, for example
xX x:
X= a (5.3.72)
X3 x:
X2, = ma tee (5.3.73)
X3, + X4
Xo, = Megat (5.3.74)
In general, for a level higher than the first level,
Xm, = Feats + Fam es (5.3.75)
Note that the centers do not have z coordinates. Next, steepest descent: path
=S(Iu
representation of matrix elements are derived. For example, 2,41 is in Z )
s(1
because it is in Z; 0.
i 5 , aoe
Zia = ACHP kV en — a1)? + (a — 21)2) (5.3.76)
--- PAGE 250 ---
§3.4 Steepest Descent Expression of Multi-Level Impedance Matrix Elements 227
. «0 .
Elements not in Z ~ are not in the near field, thus we do not need near field
integration for matrix elements.
=U
Using steepest descent and level 1 angles and noting that for Z ©) matrix
clements, xj > xj,
i 2 1) tksin al (ea, 21) 4ik cosa!) (241-2
“a= Avr) Aah )piksinal? (eas -24)-+ikcosal)(eu1—21)_
=
ie (1) piksinal (X,, -21)-ik cosa? (21)
= ArT S Aafiesinan Os
qul
«elk sinay? (Xa, —%i,) , giksin al (aay -Xa,) rik cos af (241)
Q
(yu pu >()U =
SO (a 2 oP WAT (0?) (5.3.77)
ql
where
V0" (ag) = piksinag(X1, 21) ik cosa (zi)
(the ith element relative to the center of the Ith group of level 1) (5.3.78)
TAYE (a) = Dag Aa reih a Rann)
interaction between the {th group and the Jth group of level 1) (5.3.79)
g
Wie (ag) =: eT thsin ag (Xn, ~a,) ik cos ag (~ 2)
(the jth element relative to the center of the Jth group of level 1) (5.3.80)
Note that the above definitions of V4 (a,) and WY" (aq) are for general
q q &
angle directions ag of any level.
_ s(yu .
Then the Ist level upper matrix Z y can be written as
suv Saw ay ROY ay BO ay -.
Zo = SOV (a) T (a?) W (al?) (5.3.81)
=
where
--- PAGE 251 ---
228 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
va" 0 0
Van 0 :
Var, 0 :
(ou :
=(DU 0 Varia, .
VoM)=] ; : : =NxL (5.3.82)
: (yu :
: Voura, ;
: 0 a 0
: : (U0
: : Vare-a)44,t
P : (je
9 0 Vithts
00 TRY TPP 0 OE
00 0 Bo oF
=U 4 oo : . a
T (af ) =10 : : 0 Tye he :
Lo . deo:
Oo: : : 0 Te :
=LxL (5.3.83)
WI Wi WO 0
=(U (yu
Wa) =] 0 Oe 0 Wh
0 0 wee wee see
_ ow OL ce we 0
s+ Woou 9 _ _ _
- - au" ~ du
ces 0 Wrewa-pn 7 Wieue
=LxN (5.3.84)
--- PAGE 252 ---
§3.4 Stcepest Descent Expression of Multi-Level Impedance Matrix Elements 229
In (5.3.84), the second half is connected to the first half to make it a L x N
matrix. The awkward arrangement is a result of the lack of space.

Note that although the matrix notation is used for “matrix products”
in (5.3.81), it is actually an element by an clement product. Also note that
(0 | =(U
W resembles the matrix transpose of Vo.

. . eo (2U a DU

Similarly the clement 21,117 is contained in Z because it is in 21.6;

Su .
and in Z. Or Thus, we have the following example of level 2 clerhent.
Z. yt <. Aa) ik sin. af (2117-«1)+ik cosa? (2117-21)
unr = Ar SO aye ‘a
q=l
i 2 2) iksina® (X,, —m,) ikea? ina’?
_ Are J Aaleitsinay (Xi, -) ik cos a?) (21)-+ik sina? (X1,—Xi,)
el
_ eiktsin ag? (Xs, —Xig) , piksinay? (Xo, ~Xaq) tik sin al (w117—Xe, )+ik cos a? (2117)
Q
yu QU (2) ypl2U (2) py (ZU HU (2
= MOP WEL OP IT OPW (OPW tara) (6.3.85)
ql
Note that VOY and W(" in (5.3.85) are as defined earlier in (5.3.78) and
(5.3.80) for general ay’s. In (5.3.85),
V2" (ag) = iksinag(X1—X:,)
(the ith element relative to the center of the [th group of level 2) (5.3.86)
2U (2 2) Apt piksin a (Xs, -X1,
TE (a®) = dak Aa Tella Xn)
(interaction between the th group and the Jth group of level 2) (5.3.87)
WY (aq) = ev iksinay(Xy—X5,)
(the jth clement relative to the center of the Jth group of level 2) (5.3.88)
Note also that V@Y and W@", like VOY and WY, are defined for general
Og.
_ QU .
Hence, the 2nd level upper matrix Z can be written as
; Q : : +
=U SOW gy SQWU oy SQW’ g) SOW wy SOU ¢
Zo = VV AQ) VO (a) F(a) We (a) W (a)
q=l
(5.3.89)
--- PAGE 253 ---
230 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
where
20
vor 0 0
2U Lo
oe 0 Ve
iva 2)) 2U : 5 4
VP) =] 0 ve 0 : (5.3.90)
: Quo:
nn
: a Ae
00 TOY Tee o 0:
00 0 TYR 0 0:
ZU oy : : ;
= : : (2)U QU : 53¢
To O@P)=]o 2: 0 Ts Tie | (5.3.91)
of: : 0 Tee:
7(2)U 2)U
wee WEE 9 0 bee ee
7(2)U 7(2)U
Fa 0 0 Wee wR o wee
Fe) = : :
q 0 ves ve 0 «WEE WwRe ..
(5.3.92)
‘The matrices have the same pattern for higher levels. To generalize, the mth
level upper matrices (I < J) can be written as follows
(mu 2 =(1)U, SQU ny s(m)U, (muy
Zo = SOV al) Vi (ah) WO (al) F(a)
q=l
=(m)U, =(2)U, =U.
nm (al) Wa) 7 ) (a)
where
--- PAGE 254 ---
§3.4 Steepest Descent Expression of Multi-Level Impedance Matrix Elements 231
Hohn 8 9 0
Mig 8 PE
ee
simu ; .
Vo @™)=) 0 YyrPe 0:
: u :
0 Ve |
: $ (m0 3
: ne
for m = 2,3,4,5,... (5.3.93)
pin (mu :
00 Ty TO 0 :
(m)U :
00 0 Tm 0 0 :
ROW my ™ 7
= : : yu uo:
To@M)=)o 3 0 TEE eee:
: : : yu:
of: : 0 Te:
for m = 2,3,4,5,... (5.3.94)
SS(mU,
Wo (al) =
a
plmyU Amu
0 0 Wea Wana Oo vs
(mv (m0
0 ” 0 Wi WB
for m = 2,3,4,5,... (5.3.95)
The matrix elements are as follows
VE (ug) = REMAX “Kim a) for m = 2,3, 4)... (5.3.96)
Tea) _ Adal Art ebsnal” (Sm Xie) (5.3.97)
WIE (agg) = etm Nima) for m = 2,3,4,-.. (5.3.98)
The reason for separating the lower L and upper U matrices is because
in the steepest descent representation of Green’s function, the definition in
eksinalz| ave absolute value of z.
--- PAGE 255 ---
232 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
For lower matrix, note that
i i 7 i si ik z
g(t,2) = i [daettsmtntsitcoes _ ay [daettsini ikcos(a)2
(5.3.99)
That is, the sign of cos(a)z factor can be changed. Note that for lower
sb
impedance matrix Z , 2; > 2;. For example, analogous to (5.3.77),
. Q
i sina (rq, 21) 4ik cosa?” (2a5—
Zug = Art) Aaldeisnes (a1 —a1) tik cos af) (241-21).
=
id (2) piksin al? (arg —Xs,) +k cosa 2a,
= Are x Aalde 9 1 a
_ eiksinay? (Xs, —Xi,) , giksinal? (Xi, ~21)~ikcosay) ze,
Q
DL DL (LE
= Va APTS CaP WY (al?) (6.3.10)
=
The mth level lower matrices can be written (I > J)
Q
=(m)I. =(I)L =(2)L =(m)L, =(m)L,
Br Habe) FOG oh)) 10 Halen) Fah)
=
(mL, S2)L SL
Weal) 0 Wal) Wah) (5.3.101)
where the v, T, and W matrices are given as follows
DL
ia 0 0
vr 0 :
ML 4 :
Virus 0 :
(YE :
SL 9 Vieri21 .
Va) = |: : : =NxL (53.102)
: (LE :
‘ Vons.2, .
: 0 0
: : yor
: : M(L~-1)+1Ly
0 0 Ville
--- PAGE 256 ---
§3.4 Steepest Descent Expression of Multi-Level Impedance Matrix Elements 233
0 : : : : 0
0 0 : : pot
AL : : pot
TE 0 : Poot:
=(L pL  p(Db : Dot
To) = [0K Tx 0 of flanxb (63.103)
0 le oe
: : AL DL :
: : TC os Tet oO:
0 : : : : 0
yQ)E (LE (AVE
Wi Wy Wo
SL yb
w ) (aq) = 0 0 tee 0 Weis
0 Oe ae wee
es ve vee 0
see Woy oa 0 see vee wee
see me we” tee aa
ue ue 0 Whe M(L-1)41 ve Wr
=LxN (5.3.104)
For m = 2,3,4,..., we have
yer 0 0 0
Yen, 0 PoE
(m)L : :
0 V5, 12m : :
(mL (mE . ;
Vo(@=| 0 Yrs 0 : (5.3.105)
: (m)L :
On ee
: L (m)E :
rn ae
--- PAGE 257 ---
234 5 FAS'T METHODS FOR ROUGH SURFACE SCATTERING
0 : : : 2:0
0 0 i : poiot
Teg : re!
Tal = | TE 0 Poob ad (5.3.106)
0 0 To
. L L Ls
: 0 TPN Ty OEE
SS(m)L,
W (aq) =
(mL iL
a
0 0 Week WE 0 vee aes
0 - os OW WS oe
(5.3.107)
The matrix elements are
Vag) = pliksina,(2;—X1,)+ik cosag(z:))
= WM (a9) (5.3.108)
VA) = eiksinay (Xin —Xtm)
= Wi (ag) for m = 2,3,4,... (5.3.109)
Ly a iksin a" (X7,,—X.
Ty aq) = Bal Aa Tel nag”) (Xt — Xm)
for m = 1,2.3,4,... (5.3.110)
w4(e,) = ef viksin a4 (0; —X.7, )—ik cos a7 (25)
Ay
= VP") form =1 (5.3.111)
wit (0) =e -ik sin ay(X5,,_)—Xsm)
mdm 1
= Vj") (a9) for m = 2,3,4,... (5.3.112)
--- PAGE 258 ---
§3.5 SDFMM Algorithm 235
3.5 SDFMM Algorithm
Tn the following we describe the SDFMM algorithm and the computational
steps. Each computational step ends with //. In an iterative solution to
matrix equation, the important step is to compute the product of impedance
matrix Z and a column vector 6 from surface field. Continuing the same
example where M = 20, L = 64 and N = 1280, we have
s- [60 s@ s@ s® s@ sO)]-
Zb= [2° +2 PP FZ 2p
sO) sQVU s@L sQu sy
= [Zz 42 +Z 4 4F
SBU SQL =4U SOL s=6)U sO)L]~
a ew )P (5.3.13)
- BO, . rr
(1) Computational step: Compute Z 6 by direct multiplication //,
The number of computational steps for near field interactions Nyear is
Nnear = 3M?L — 2M? =3MN —2M?
= M(3N —2M) (5.3.114)
For non-near field interactions, the two processes are aggregation and
dis-aggregation. Define the upper matrix
, SQV. SQW. =3UL Ss4UL SOUL
a a ee ee
Q . . ;
=()U (IU =()U .
=v (a) F(a) We (al)
q=l
O =(1u (2) GO (ay BOW, (ay, OW. (0) SEU, gy.
FV (ePD) Ve) T™ (a) Wo) We" (a) b+ +
q=l
© DY 5) SOU, 6) BOY (6) OU. os BOW 5,
+ OVP) Vo @P)T (ol) Wo (af). Wi (al?) 6
q=l
(5.3.115)
For general aq, not restricted to angular direction of a particular level,
let
<u =U le
Bag) = Wag) b= L x1 (5.3.116)
--- PAGE 259 ---
236 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
<(2)U, SOU 5 s(QU Ue
BO cag) = WO (exg) Berg) = Wag) Pg) b
L
=5x1 (5.3.117)
<(3)U =(3)U ¢ sQU QU SU. .-
5 (64g) = WO cag) Berg) = WO cag) Ferg) Wing) B
L
=5xl (5.3.18)
<(5)U Ug =(5)U SOU
BOM (ag) = WO (04) Bag) = We (aug) «Wo eng)
L 4
= 57x l=4x1 (5.3.119)
=S(U 20
(2) Computational step: Compute and_ store vw” (af), we (a),
=3)U =U (5
wv ) (a), ves Ww » (ai). Note that there is no need to compute
SU. SU 4 SU, yg
Ww (a), Ww ) (a), Ww , (a4), etc. Also compute and store the
interpolation functions Tn (of, a”) //
Then we have
Q >
_ SW ay =U ay ca
B= SPO) Fa) Bal)
ql
2 au SOU , a(QU (2)
VV eV (a2) TP (a) Bal)
q=1
oyu SQV. pg =U, pg, SOU, 0g). 13), (9
Ea) FP al) HO a) Fa) 5a)
q=1
2 (yu SU) SOU (5) 2(5), (5
Fe tO (a) VO (AP) T (al?) 5 (af?) (.8.120)
=
7 (DU >
(3) Computational step: Compute Bal) = iv’ » (a) b //
The number of computational steps for calculating Bef) is
Qn
(4) Computational step: Compute Ba?) ) from Wa) by interpolation
Q
Ba) =P InY(a?,o Ma) // (5.3.121)
gal
--- PAGE 260 ---
§3.5 SDFMM Algorithm 237
The number of computational steps for interpolation is
L
2
Q 2(2--2)
(5) Computational step: Compute Ba?) by
~ 4 =5(2)U =
B02) = Wa Ba?) (5.3.12)
The number of computational steps for the above operation is
L
Q 202-2)
Compute also 6a") from Bai”) by interpolation
Q
BP(a®) = S> InP) (a, a) (a) (5.3.123)
q=1
The number of computational steps for the above interpolation is
L
2
@ 23-2)
Then compute
=(3 =(3)U =(2), (9 .
5 (a®) = WP” (a) Ba) // (5.3.124)
The number of computational steps for the above operation is
L
ereasy
In this manner, we move up the levels. For each level there is one product
and one interpolation.
(6) Computational step: The computational steps for the mth level:
1. Interpolation
Q
B™ Nal) = SP aD (al™ al" DT" MQM") (5.3.15)
q’=l
The number of computational steps for the above operation is
L
2
Om
2. Multiplication
—(m)U +(m-
B%al™) _ rm” (a) a” Yak) (5.3.126)
--- PAGE 261 ---
238 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
The number of computational steps for the above operation is
L
Q 20n—2)
Steps repeat up to Ag (af) //
When 5” (a!) is completed, the process of aggregation is computed.
The total number of steps in aggregation is
N L
1, = ON 2
Na=QN+ Se + Vm
m=2
P41 oQ2 N 8 19"
= QN + 2(Q° + Vr (5.3.127)
(7) Computational step: multiplication of T matrices
7 =(1)U x
AMG) = Fa) Fa) (5.3.128)
9 ; =QU iy (2) ¢
Ma) = F(a 5a) (5.3.129)
(5 - SU os), 3(5), (5
2 (a) = F(a) Ba) // (5.3.130)
The number of computational steps for the product of T matrices with
column vectors is Nr:
; al , tL PL
Np = 31Q + 385Q ++ +355 GQ = Lye?
N
= 6LQ = 6057 (5.3.131)
Next, we start the process of dis-aggregation.
| Au 2 ROW, gy SQW py
p= vv (ai) 2 (af?) + “iv (eV (a?) 2) (a?)
q=l q=l
2 =U 4), SOU, 3 FOU. (3) 2(8)/ (8
EV ay Fa) F(a) 2 (a)
g=l
SOY 0) FM 0) HOM eld) Halt 29 (al
FV a) VAT (af) V (af?) 2 (a4)
=
--- PAGE 262 ---
§3.5 SDFMM Algorithm 239
FY 15) OY 10) FO tO) FO) Fa) (al
EV P/V PV PV (AP)V (a) 2a”)
q=l
(5.3.132)
For general ag, not restricted to angle direction of any particular level,
let
=(4)U =U .=QU) .SQUu sau
FO ag) = ag) Fag) V ag) Vay) (5.8138)
Then the sum of last two terms in p” in (5.3.132) is
Q_, ;
sou, sv SAW, (yy, SOU 7
Tus = SLV (of) Ve (a) VO (a) Vo (ap) 2 (a)
q=l
2 KOU) SQW, SOU SU, ey =U. G5), 7
EP EP) MV P)V (AP) ¥ (al) 2 (a?))
ql
Q Q 5
=(4U “)/f =(4)U, SOUS) (5) (8)
HVT aM) OM + OT OPV (a) 2 (al?)
qu q=l
(5.3.134)
=U (5 =U
Note that 7 , (a) is related to 7 > (a) by interpolation
, Q caytr
=(4)U = oe =(4U
FY (a) = S> In (aa?) F(ab?) (6.3.135)
=i
Substitute (5.3.135) in the expression for Is in (5.3.134)
50H 2) lO (ald
Ts = 27 (al) (af?)
gq=1
ent (4) JOY By) FOXY) (a
+0 Nom Ya® a) T (a) V (al 2) (a) (5.3.136)
q=lq=1
In (5.3.136), interchanging dummy variable q' = q in the last term and
then combining with the first term, we have
Q
=(4)U
ts= S07” |x
q=l
2 8) (9) FOXY, (5)\ (5)/,6)
SY MO (al? ol) Vo (ay ye)(al?)) (5.3.137)
q=l
--- PAGE 263 ---
240 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
(8) Computational step:
5 SOU 05), 45 5
Fo) = Fal) a) // (5.3.38)
The number of computational steps for the above operation is
L
Qa
(9) Computational step:
Q
al4 ~ 5 a
B (ald) = S> In{9 (a af) 74a) (5.3.139)
q=1
This step is known as anterpolation because summation is on the first
argument of the interpolation fumction instead of the second argument
in usual interpolation. Use the stored interpolation functions to perform
this step //
The number of computational steps for the above operation is
L
2
Q 2(p-2)
2 cau H(4)
Ts = 07 (al) (eal) +B (a{)] (5.3.140)
q=l
Thus for each level, we need to multiply, anterpolate, and add. Also note
that we do not calculate J45 in (5.3.140) but continue on to consider I345,
Tozq5, Tioga, etc., where I345 means the summation of the third, fourth,
and fifth terms. Now
oe GO ayy aye) 4 SOY, (2) SOM, 029) 202)/ 2
P= VAM) M OMY) + SOV PIV (a?) 2 (a?)
q=l q=l
SOY (0) FM 00) Fa 2a
FV OPV PIV Pp) 2a?)
ql
SG oy. FOF [O(ald) + Fal 5.
4 Va) F(a) ic (al) +B (al )| (5.3.141)
q=l
(10) Computational step: Addition and multiplication
7 =u, 7 a4 .
Fal) =V"(al?) [e¢a) +3 fai)] (5.3.142)
--- PAGE 264 ---
§3.5 SDFMM Algorithm 241
The number of computational steps for the above operation is
L
WH
Anterpolation
Q
(3), = me
B (a) = D> In (a, a!) Fal) // (53.143)
q=l
The number of computational steps for the above operation is
L
2
Q Q(e-3)
Then
PFO AD (alt) 4 OPO Fal 2 al2
B= SOV (al) A (a9) + SOV (a) (a) 2) (a?)
q=l q=l
2 au SQW (3), =O og , (3),
tV PP (a) 7 (a) [e® (o) +3 (a)|
q=l
(5.3.14)
(11) Computational step: we move down the level in this manner. Addition,
multiplication and anterpolation.
ss(m)U ~
"Dlal™)) =V ‘m) (a) [em (a™) + Bae )| (5.3.145)
Q
BO Ma) = > InP-Y (aL), al“) "NEM 7 (5.3.146)
el
The number of computational steps for calculating mV (qh) and
Beau") is respectively,
L > L
Orman OD
The same procedure goes on until we reach the first level, which does
not need anterpolation. The first level needs QN steps. Thus the total
number of steps for dis-aggregation is
Le L
Np =QN+ O(Q?+ Vm
m=2
; 2 N z
ZQN + 2Q + O)5 (5.3.147)
--- PAGE 265 ---
242 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
(12) Computational step: Repeat im the same manner for 5”.//
The total number of steps is, including p” and p”,
Metal = Nnear + 2(Na + Ny + Np)
N N
= M(3N —2M)+2 [ew +2(Q? + QVayzt «qe
ON +21Q +Q)
“ne M
2
= M(3N -2M)+4N le + S|
Since Q and M are fixed, the CPU requirement is O(N).
3.6 Numerical Results
In Fig. 5.3.5, we illustrate the numerical reslts of the SDFMM method.
We consider a single realization of random rough surface with h = 0.3
and 1 = 4, 0; = 50°. The frequency is 19 GHz so that A = 0.0158 m.
We use Ax = 4/10, g = L/4, L = NAx. In SDFMM, we use N = 320
and M = 10. In 5.3.5, we compare the results of direct multiplication and
multilevel SDFMM. The two results are indistinguishable.
4 Method of Ordered Multiple Interactions (MOMI)
In previous sections, we have used the banded matrix iterative approach and
the conjugate gradient approach for treating matrix equations. The method
was also enhanced by using canonical grid together with FFT (BMIA/CAG).
In this section, a different iterative approach known as method of ordered
multiple interactions (MOMI) is discussed. The method was first proposed
in connection with using the parabolic equation method for rough surface
scattering [Spivak, 1990; Holliday et al. 1996]. and was later extended to
treat higher order scattering in random rough surface [Kapp and Brown,
1996].
4.1 Matrix Equations Based on MFIE for TE and TM Waves for
PEC
The method used MFIE for both TE and TM waves for perfect electric
conductor. As discussed in Chapter 4, using MFIE for TM waves has been
standard treatment. For TE waves, usually, EFIE is utilized. In Chapter 4,
Section 3.2, we also derived the MFIE for TE case. We use pulse basis
--- PAGE 266 ---
§4.1 Matrix Equations Based on MFIB for TE and TM Waves for PEC 243
x10°
a SS
, Ka AA haa
BS ft fh i
é AAA ATTEN ATTIUILITUTALA AAA AA
e VMI
4 PUES Cs
2 ‘ ryt +
3m a2 a1 01000 0080S 02s
xin meter
x10"
3
I
2 Tad
=! aha RAM {
g, UA UA TUTTTHEA AAA
? VARVARA AAA
Fate Ry Marge
ye yyy!
at |
2502-01501 ~008~=~C~S~« HSCS SSCS
xin meter
Figure 5.3.5 Comparison of SDFMM and direct multiplication.
functions and point matching.
(A) For TE case, the integral equation is given by Eq. (4.3.32) with w
representing the electric field. In matrix form,
N
SL Zintn =O, M=1,2...,N (5.4.1)
n=l
where
On = [ft VP Jpmaeg =f len) (5.4.2)
Bin = 2 [ft Verine(T)) |= itm,2=F (em) (5.4.3)
nin | SE
Zin =2 | *daKO (am,2) — (m #n) (5.4.4a)
Bao S
om bE M)
Zh = 142 f aK 2 (arm, 2) (5.4.40)
amy 9E
where f is the principal value integral. Note that we have multiplied
--- PAGE 267 ---
244 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Eq. (4.3.32) by 2. Thus the right hand side has a factor of 2 and the
impedance matrix elements also have a factor of 2. The quantity K; MY) (at, x)
is given in (4.3.33). We have seen that for energy conservation, it is necessary
to perform numerical integration of near-field impedance matrix elements in-
cluding the self-patch. As a result of the numerical integration, the diagonal
element of the impedance matrix element is not equal to unity, as shown in
(5.4.46). To apply MOMI, we divide (5.4.1) by Z/,,,,, so that
N
Se Zann = bm (5.4.5)
n=1
where
by
Om = Zee (5.4.6)
mm Zin
gy
Zinn = (5.4.7)
un Eine
Thus the diagonal elements Z,, are now equal to unity.
After the matrix equation is solved, the scattered wave can be computed
by
N
W)(0,) = SO Ae V1+ (Fen) Pre HOM ern FlF) 20880) (5.4.8)
n=1
(B) For TM case, the integral equation is given by Eq. (4.1.151) with w
representing the magnetic field. In matrix form,
N
So Zante (a9
n=1
Wn = [Pron 2=Flen) (5.4.10)
Bh, = 2lWine( Maney -flen) (5.4.11)
tat
Zan = -2[ dxKy (amt)  (m#n) (5.4.12a)
ta
Bn + SE
Zon =1—2 f dizKy(&m,2) (5.4.126)
Fry 92
where Ky(z',x) is given in (4.1.158). To make diagonal elements equal to
unity, we again divide (5.4.9) by Z/,,,, to get
N
Ye Boantin = in (5.4.13)
n=l
--- PAGE 268 ---
§4.2 Iterative Approach 245
where
by
bn = 5.4.14
"Zim Gans)
7
Znn = 5.4.15
mn = 7 (5.4.15)
After the matrix equation is solved, the far field scattered field is computed
from
N Py
YWY(8.) = > Acik[f! (wn) sin 8, cos AsJyine MO Meee =Fl%m) 20865) (5.4.16)
n=1
4.2 Iterative Approach
To apply the method of ordered multiple interactions (MOM1), the following
iterative approach is used. The impedance matrix is decomposed into
Z=I-L-U (5.4.17)
where
-Z, form >n
Ln = {57 5.4.1
mm 0 otherwise ( 8)
Los -Zmn form<n 5.41
Umn { otherwise (5.4.19)
Note that E and U are lower and upper triangular matrix, respectively. The
diagonal elements are also zero. Note that for both TE and TM waves, the
diagonal elements of the impedance matrix Zam = 1, with m= 1,2,...,.N.
We treat the case of TE waves (the TM waves can be treated in a similar
manner). The matrix equation is
Zo=5 (5.4.20)
It is rewritten as
ABU =b+LU5 (5.4.21)
where
A=I-L (5.4.22)
B=1-U (5.4.23)
Note that A and B are triangular matrices so that the product of the inverse
and a column vector can be solved by back-substitution and not by inver-
9 . Si
sion. The back-substitutions require O(N?) operations. For example, B 0
--- PAGE 269 ---
246 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
is solved by back-substitution. Let,
Bu=7 (5.4.24)
Then
Aq=3+L0B 9 (5.4.25)
Thus we use (5.4.25) to solve for 7, and then we use (5.4.24) to solve for T.
The zeroth order solution is
Aq =5 (5.4.26)
BO =9 (5.4.27)
The zeroth order solution, 5), is solved by using (5.4.26) and (5.4.27), The
zeroth order solution is also known as the “new” Born term.
For higher order solutions, they obey the equation,
Aq” =b4EUB ge (5.4.28)
7) =O 44 ETB ge) (5.4.29)
Bom) = (5.4.30)
Then, using the recurrence relation,
a”) =9 40 TOR ye (5.4.31)
Ww) B® (5.4.32)
‘This means
W) = 4B ATT (5.4.33)
32 = 4 BF TH
=0 45 7 TI +B A TB A Taw (5.4.34)
Tn general
” faos-1s=}4
BM =F 4° iB ATL 0] GO (5.4.35)
g=1
Note that
UB’ =(i-B)B'=B'-i (5.4.36)
a ‘2-4-7 (5.4.37)
--- PAGE 270 ---
§4.3 Numerical Results 247
In the numerical algorithin [Kapp and Brown, 1996}, the procedure is as
follows. From (5.4.36)-(5.4.37) and (5.4.29), the updating algorithm is,
=-1 =\/s-1 =
ge = G+ (a - 7) (B - 7) ge?) (5.4.38)
When all the orders are completed, we get the final gf“), Thus, the final
solution is obtained by solving
slop,
B=B qin (5.4.39)
=1 =
Note that we calculate #"—) = (3 - T) gt) by
inl) Bye) yer) (5.4.40)
This is done by back-substitution and a subtraction of a column vector.
<(n- =I =
Similarly, compute d”-) = (a - 7) 2-1) by
a) =F Ae) — er) (5.4.41)
4.3 Numerical Results
In Figs. 5.4.1 and 5.4.2, we plot the surface currents for a single realization
of random rough surface. The real part of the surface current v,, for the case
of TE wave incidence with 6; = 30°, h = 0.4A, 1 = 0.2A using 80 points
per wavelength. Comparisons are made between matrix inversion, zeroth-
order MOMI and tenth-order MOMI. The tenth order solution is in good
agreement with matrix inversion. In Table 5.4.1, we test energy conservation
using
P= | * d0,0(0s)
z
which should be equal to unity. As noted in Section 3.2 of Chapter 4, MFJE
of TE case has inadequate energy conservation test.
No. of points/\ | Matrix inversion [Oth-order MOMI
40 0.9158 0.8262 0.9126
072 0.9536
Table 5.4.1 Comparison of the energy conservation for TE case using MVIE at @; = 30°
with h = 0.44, 1= 0.22, and L = 25.64.
--- PAGE 271 ---
248 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
* " al
= Zoroth ordor MOM!
TY
i | |
3 po [, i | H
I eli AT
3 |i qi MI) en
: | Mu hal i, Mea dll AY |
8 { ay | q \! a | W
eee Ge neE P|
i meni if
B10 Wo Wy
E
asl |
ars 10 18 20
‘Surface position (wavelength)
Figure 5.4.1 Comparison of the surface currents by matrix inversion and zeroth-order
MOMI for TE case at 6; = 30° with h = 0.4A and / = 0.2A, 80 points/A diseretization and
near-field integration are used in the simulation. L = 25.6).
re | oy
‘ep |
2 l
b. —
3 | Hote Mal |.
i i Lit i [| | Hy it
BL ad hE OY
i oe a
ee ee
3 ee ie
8 i Wyle qh
$0 i H | iif
E
4s : ; |
| \
75 10 15 20
Surface position (wavelength)
Figure 5.4.2 Comparison of the surface currents by matrix inversion and tenth-order MOML
for TE ease at #; = 30° with h = 0.4) and I = 0.2A, 80 points/, discretization and near-field
integration are used in the simulation. L = 25.6A.
--- PAGE 272 ---
§5 PBTG Combined with the Multilevel Fast Multipole Method 249
5 Physics-Based Two-Grid Method Combined with

the Multilevel Fast Multipole Method
For scattering by lossy dielectric rough surfaces with large permittivities, we
have introduced the PBTG method in Section 2. The PBTG method was
further combined with BMIA/CAG in Section 2. In this section, the PBTG
is used in conjunction with the steepest descent multilevel fast multipole
method (SDFMM) to solve wave scattering from one-dimensional random
lossy dielectric rough surfaces. The proposed algorithm has the computa-
tional complexities of O( Nag) for near-field interactions and O( Neg) for non-
near field interactions, where Nqg and Neg are the number of sampling points
on the dense and coarse grid, respectively. Using the proposed algorithm,
wave scattering from Gaussian and non-Gaussian rough surfaces is investi-
gated and illustrated. Special emphasis is put on checking the accuracy of
the algorithm and energy conservation.

We illustrate the single grid method and the PBTG in Section 5.1.
We discuss the computational complexity of the combined algorithm of the
PBTG with the SDFMM in Section 5.2. In Section 5.3, we apply the algo-
rithm to Gaussian rough surfaces and discuss the accuracy of the algorithm.
In Section 5.4, we apply the method to study scattering by the modified
power-law spectrum.

5.1 Single Grid and PBTG
Consider a tapered plane wave Winc(?) incident on a random dielectric rough
surface defined by z = f(x). The surface fields satisfy the dual surface inte-
gral equations. let G(F,7’) and G1(7,7") be the 2-dimensional Green’s func-
tions of free space and the medium, respectively. Let p be equal to p/p and
€1/¢ for TE and TM polarization, respectively. Using the method of moments
(MoM), the integral equations are cast into the matrix equations:
N N
YS aiju(as) + Yo bigs) = Vino(wi) (5.5.1)
j=1 j=)
N N
Ya? putes) + ov Pv(es) =0 (5.5.2)
j=l j=l
= Jaw”. Expressions ai;, b:;, a), and 6 are as i
where u(x) = V/1 + [f/(z)] on Expressions aj, bij, aj;', and 6;;’ are as in
(5.2.6) (5.2.9).
--- PAGE 273 ---
250 5 FAST METHODS FOR ROUGH SURFACE SCATTERING

The quantity N is the number of sampling points on the surfaces. The
matrix elements ajj, bij, a), and wi? are determined by the Green’s func-
tions. :

We let, Roman numeral subscripts i, j denote indexing with the dense
grid and i, j with the coarse grid. Assume that the upper medium is free
space and the lower medium is lossy with a relative complex permittivity €.
We can define a distance limit r, as determined by the complex permittivity
of the lower medium. Outside this limit the field interaction between the
ith and the jth point is vanishingly small, and the lower medium Green’s
function can be set equal to zero. Therefore we can approximate

(1)
al) wal) = {es ng Sr (5.5.3)
0 rg =r
aw 70 [0 ry <1
by aw by = 4 0G TST (5.5.4)
a a 0 ry =r
where rij is the distance between the éth point and the jth point on the dense
grid. Thus ay ) and ey are banded matrices and Equation (5.5.2) becomes
N N
~(1 zQ). rf x
Saf} pule;) + 5) Wiles) =0 (5.5.5)
j=l j=l

Based on the observation that the upper medium Green’s function is
slowly varying on the dense grid, we decompose the upper medium Green’s
function into near field and non-near field interactions

N N N
> aiju(xj) = Y aiyu; + > aus (5.5.6)
j=l j=l j=l
N N N
SP digh(ars) = D7 bj + Yo oP (5.5.7)
j=l j=l jal
where aj;, bj, aj, and 62% are determined by
s fj TH STS 5
ai = {5 ry > ry (5.5.8)
by TH ST.
so i THOTT 5.5
w= {0 BST 659
0 Tig ST
ane = {i ri ST (5.5.10)
ij TOTS
o Tyg <r
ons = aalf 5.5.11
ij by Ty > Ty (5.5.11)
--- PAGE 274 ---
§5.1 Single Grid and PBTG 251
Thus r; is the distance separating near field and non-near field. For non-near-
field interactions, the Green’s function of free space is slowly varying on the
dense grid. We can use the coarse grid to sample it. Assume the number of
sampling points on the coarse grid is smaller than that on the dense grid
by a factor of ni, where n; = integer(Re(/c1)). Thus the ith point on the
coarse grid corresponds to n1 points it, %9,---;%n, on the dense grid. The i
with no subscript, it refers to the same coarse point i. For tp, p = 1,2,...,m1,
it refers to the m; dense grid points associated with the coarse grid point i.
The ipth (p = 1,2,...,7™) point is the ith dense grid point where i is given
by ¢ = (i — 1)n1 + p. When we calculate the convolution of aj? and surface
fields of uj on the dense grid, the following approximation can be made.
N Nim ni Nim om
Leaputes) = S> Srars wlw;,) » SF aks Yo ule;,) (5.5.12)
jel jai at jai ql
In getting (5.5.12), we need the property that the Green’s function of free
space is essentially constant over an interval of ni points. Furthermore, the
elements as of p = 1,2,...,m1 can be found by interpolating from the
.
coarse grid to the dense grid,
7
ns a ns Rey
as > In{ip,i + 7)a} 23 (5.5.13)
r=-T
where J nip, i+7) is the interpolation operator and T is the number of points
of the coarse grid we use to interpolate. Then
N N/m 7 nm T
So ahvu(e;) = S> Yo Inliy, i+r)ae 93 Do ule;,) =F Inlip.i +7) G25
j=l jai t=—T q=l r=—T
(5.5.14)
where
Ning m
Siar = Do Ej YU.) (5.5.15)
j=l ql
What is done is that the surface fields on the dense grid are first averaged
before being convolved with the free space Green’s function on the coarse
grid. Then we use interpolation to find N values on the dense grid. Similarly,
we can obtain:
N r
So oyu(ay) = SO InG,,i+ rh, (5.5.16)
j=l t=-T
--- PAGE 275 ---
252 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
where
Nim nm
Wi = Dy DV O;,) (5.5.17)
j= gal
Thus, Eq. (5.5.1) can be rewritten as
N N T
SY ajjues) + Yo ofo(es)| + YO InG,,i+7)932,
j=l j=l =
T a
+ YE Inlip,i + 7) hi, = Vine(wi) (5.5.18)
1=-T
‘We can write Eqs. (5.5.5) and (5.5.18) as the following matrix equations.
sl) xu _ _
Z Aisdg Usdg + ZB sig * Usdg = Isdg (5.5.19)
ZA.sdg + Usdg + ZB,sdg - Dsag + ZA.seg . fig + Za,s09 Brea, = Winesdg
$ intp imp
(5.5.20)
Note that the elements of a), a, a};, and 63; consist only of banded
matrices. The main CPU requirements are to calculate the values of g; and
hy with i from 1 to N/n,. For direct matrix and column vector multiplication,
it takes approximately (N/n1)? operations. Note that N/n, is the number
of unknowns on the coarse grid. The computational steps can be further
reduced using the BMIA or the FMM. In Section 2, we have illustrated the
PBTG-BMIA. In the following section, we will illustrate how to combine the
PBTG with the multilevel steepest descent path FMM.
5.2 Computational Complexity of the Combined Algorithm of the
PBTG with the MLFMM
For the multilevel FMM, multi-sized groups are formed. At the lowest level,
the N elements are decomposed into L groups. Each group includes M ele-
ments where N = ML. Then each two subgroups at the level form an upper
level group (large group) until the highest level. The interactions of groups
at each level are calculated only for the non-near groups at this level inside
the neighboring groups of an upper level. Thus, the impedance matrix can
be written as the sum of the following matrices.
= sO st = sé
Fa 2 2g ZO 4 (5.5.21)
--- PAGE 276 ---
§5.2 Computational Complexity of PBTG with MLFMM 253
_ lm).

where the matrix Z — includes only the elements that would be computed

at the nth level.

As illustrated in Section 3.2, the procedure of the multilevel SDFMM is
composed of three steps. First, the surface fields at each element are trans-
lated to the group centers at each level. When transferring the field from
the lower level group center to the upper level group center, an interpola-
tion is required to find the values of the fields from the coarser angles to the
finer angles. Second, the interactions of group centers at each level are calcu-
lated. Only those of the non-near groups inside the neighboring groups of the
upper level are calculated at each level. Lastly, the receiving fields at each
group center are distributed to its subgroup centers/elements. The last step
is performed from the highest level to the lowest level with anterpolation.

The number of computational steps for the first step is

P P ,
1 , L L yr N
Ni =2 [er + 30x] + 2 001TH = 2QN +4Q(Qi + IG
n=2 n=2
(5.5.22)
where the first term comes from aggregating the surface fields to group cen-
ters, and the second one comes from interpolating the fields from the coarse
angles to the dense angles for all the levels. The integer Q, is the number of
operations used to interpolate for a single angle.
The number of computational steps for the second step is
PB
L Q
1p = \>3-— -Q ON, 5.5.24
No Ligne 657, (5.5.23)
n=
and the number of computational steps for the last one is
N3 = N ; b >y Dw 2QN +4 yr
N3 = 2|Q) + Oa + 015m * QN + 4Q(Qi + 1) 55-
n= n=
(5.5.24)
The first term is for disaggregating and the second is for anterpolating.
Thus, the total number of computational steps for the matrix-vector
tnultiplication is
4 7
Neotaa = M(3N — 2M) +2Q [2 + oF | N, (5.5.25)
where the first term is from near field interactions and last one is from non-
near field interactions. As long as Q is constant, the computation steps will
increase only with linear N.
--- PAGE 277 ---
254 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
To coinbine the PBTG with the multilevel SDFMM, the near field in-
teractions have to be calculated directly on the dense grid, and the non-near
field interactions are calculated on the coarse grid through the MLFMM.
sl

In Eq. (5.5.19), the number of computational steps for ZO sag *Usdg and
stl —

ZS sty *Wedg is 2MiNgdg, where M, is determined by the permittivity of
the lossy medium and the number of sampling points per wavelength on
the dense grid and is a constant for a given case because no non-near field
interactions are calculated through it. In Eq. (5.5.20), the MLSDFMM is

= s =(0

used. We treat the matrices Z4,sdg and Zpisdg a8 Z ) in Eq. (5.5.21) and
= = =( = slp

ZaAjseq ad ZB, seg a Zz ) +A+ zZ” +A4 Zz”. Thus the number of com-
putational steps for this part is 2Msag(3Nedg — 2Msag) + 4Q[2 + 4@="| Nocg
plus the number of operations used to interpolate from the coarse grid to the
dense grid, which is proportional to Nggg. The total number of operations
for the PBTG-MLSDFMM is 2M, Nag + 2Mydg(3Nedg — 2Moag) + 4Q[2 +
S97) Nocg + QoNeag. Thus the computational complexity of the PBTG-
MLSDFMM is O(Nedg + Nseg)-

Numerical simulation results will be presented in terms of the normalized
bistatic scattering coefficients and emissivities or brightness temperatures.
The bistatic scattering coefficients are defined as, using a tapered plane wave
in the spectral domains,

Trey (OE . °
da |iky(x) | sin 6, — cos @, ) — u(x) | exp(—ika(@,, x))
—00 dx
(05, 0;) = i
ang [ dkgk, exp [—(Ky — ksin 6;)?9?/2]
—k
(5.5.26)
In (5.5.26), a(05,2) = sin O.x + cos Os f(x), and k, = \/k? — k2.
5.3 Gaussian Rough Surfaces and CPU Comparison
In this section, we illustrate the accuracy of the algorithm for the energy
conservation, and compare the results and CPU requirements between the
PBTG-MLSDFMM and the BMIJA with the single dense grid. We use 10
points per wavelength as the coarse grid and 30 points per wavelength as
the dense grid. We also plot the results from the PBTG-BMIA. All the
results are run on a Pentium IL with 450 MHz and 256 Mbytes.

In Fig. 5.5.1, the bistatic scattering coefficients computed from the

BMIA, PBTG-FMM, and PBTG-BMIA are shown for one realization. The
--- PAGE 278 ---
§5.3 Gaussian Rough Surfaces and CPU Comparison 255
4.8 po a
| [== Bom
| io7 PBTG-FMM
5 |
2
2% '
2 | |
: Lid |
gos \ | | { i
rr ant
\ | i \
ART BHT
ACL Hae
oat | Ae YM Vn
80-60 -40 -20 0 20 40 60 80
scattering angle (degrees)
(a)
0.5. $$$
0.45} i POTG-AMIA
me PBTG-FMM
5 0.4} n TO
Sos} | | | |
5 asl | t |
3 0.3" | | |
poz) | | | j
5
i Hh a
3 |
IANA Ly |
Fo Ul i MA 4
Fy OP iii i
oat all t\ i i AY URAL
Atv yh EW
-80 -60 -40 -20 oO 20 40 60 80
scattering angle (degrees)
(b)
Figure 5.5.1 Comparison of the bistatic scattering coefficients computed by the PBTG-
FMM, PBTG-BMIA, and BMIA. The rms height is 0.3 wavelength, correlation length is 0.5
wavelength, angle of incidence is 30 degrees, permittivity is 25+ 22, and surface length is 128
wavelengths. (a) TE wave incidence; (b) TM wave incidence.
--- PAGE 279 ---
256 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
1
0.9) ee |
© horizontal pol
gos 17 veneatpol |
§07- i
S06 4
2 |
805) * {
50 . ,
£7 .
50.3 7
5 0.2? ° ° ° |
0.4)
0 a
5 10 15 20 25 30
soil moisture in weight percent (%)
Figure 5.5.2 Error of the energy conservation check as a function of soil moisture.
relative permittivity of the lower medium is 25 + 2i, and the rms height
and correlation length are 0.3 and 0.5 wavelengths. We use 30 points per
wavelength as the dense grid and the surface length is 128 wavelengths with
7,680 surface unknowns. The angle of incidence is 30 degrees. Figure 5.5.la
is for TE wave incidence and 5.5.1b is for TM wave incidence. We regard the
results from the BMIA with 30 points per wavelength as the accurate one.
‘The three results are in good agreement. The CPU required for the BMIA,
PBTG-FMM, and PBTG-BMIA are 372, 163, and 157 seconds for the TE
wave and 123, 49, and 48 seconds for the TM wave, respectively. Thus both
the PBTG-FMM and PBTG-BMIA methods can save CPU compared with
the single dense grid.

In Fig. 5.5.2, the relative error of energy conservation check is plotted
as a function of the relative permittivity of the lower medium. The results
are from the PBTG-MLSDFMM. The relative permittivities of the lower
medium are changed according to the soil moistures from 5 to 30 percent, in
weight. The correlation length is 1.0 wavelength in this case and the other
parameters are same as in Fig. 5.5.1. The energy conservation is less than
0.6% for all the cases.

In Fig. 5.5.3, the CPU per iteration in the conjugate gradient method
is plotted against the number of surface unknowns for the three methods.
--- PAGE 280 ---
§5.4 Non-Ganssian Surfaces 257
18 ' 7 SS]
;— sma |
16) - PBTG-BMIA -
| == + PBTG-FMM | |
a4 a
12;
8 y
510 Lo
8
£8 5
a /
6. /
a /
4 “
a peer eee |
2 eee
a
ol 5-5 -
0 1 2 3 4 5 6 7
number of surface unknowns x10!
Figure 5.5.3 Comparisons of CPU time per iteration in the conjugate gradient method
required by the PBTG-MM, PBTG-BMIA, and BMIA. N is the number of surface un-
knowns.
The dense grid is fixed at 30 points per wavelength and we change the
surface length. It is shown that the PBTG-BMIA and PBTG-MLSDFMM
have similar performance for the cases we compute. The first algorithm is
an O(N log N) algorithm and the latter is a linear algorithm with N. Both
of them take less CPU than the BMIA with the dense grid.
5.4 Non-Gaussian Surfaces
There are two types of correlation functions often used [Chen and Ishimaru,
1990], Gaussian and exponential correlation functions. The spectral densities
of the Gaussian and exponential are given, respectively, by
, RL ee
W(k) = —= exp {| -—— (5.5.27)
Van 4
rll
W(k) = ——35 5.5.28
() mw 1+ ki? ( )
where h is rms height, J is correlation length, and k is surface wavenumber.
It has been found that the surfaces with Gaussian spectral density are far
away from real natural rough surfaces such as soil and ocean whereas the
surfaces with exponential correlation function are without rms slope, which
is required for numerical simulations of wave scattering from random rough
--- PAGE 281 ---
258 5 FAST METHODS FOR ROUGII SURFACE SCATTERING
surfaces. The third type of surface roughness spectrum, power-law spectral
density, is proposed as the following [Chen and Ishimaru, 1990; Kuga et al.
1993].
ayy. Wl n= ayy? Rey” _
Wk) = Te fits esd a (5.5.29)
where (2n — 2)!! = 2x 4x---x (2n—2), (2n—3)!!=1x3x--- x (2n—-3),
and (—1)!! = 1. The above spectrum becomes a Gaussian spectrum when the
power index of n goes to infinity and is very similar to the spectrum with an
exponential correlation function when n is one. The parameters h and | are
supposed to be the rms height and correlation length in the above spectrum,
respectively. But if we compare the power-law spectrum with a power index
of one with the spectrum of the exponential correlation function, we find
that the real correlation length of power-law spectrum is actually \/7l/2 .
This can be seen by rewriting the power-law spectrum with the power of 1
as:
2
wry =m) (5.5.30)
wT 1 +h? (/7nl/2)
Thus, a coefficient varying with the power index is needed and introduced to
overcome this problem. The modified power-law spectrum is the following:
nL ay\? 22] .

W(k) = Vinh, l + (2) 7 (5.5.31)
where a, = I'(p — 0.5)/T'(p) and I is the Gamma function and b; = /7/2,
by = 0.95, b3 = 0.97, by = 0.98,..., and bo, = 1.0 are determined numerically,
and h is the rms height and / is the correlation length. The modified power-
Jaw spectrum becomes a Gaussian spectrum when the power index n goes
to infinity, and is the spectrum of an exponential correlation function when
n is one, The important feature of the proposed spectrum is that it gives
various spectra but with fixed rms height and correlation length, which are
physical parameters usually used to describe the rough surfaces.

We next show some numerical results of the bistatic scattering coeffi-
cients and the brightness temperatures from wet soil with the power law spec-
trum. The rms height and correlation length are fixed at 0.3 and 1.0 wave-
length, respectively. The surface length is 64 wavelengths and the dense grid
is 30 points per wavelength. The simulation was performed by the PBTG-
MLSDFMM.

In Fig. 5.5.4, the comparisons of the bistatic scattering coefficients be-
tween surfaces with a power law spectrum with different power indices are
--- PAGE 282 ---
§5.4 Non-Gaussian Surfaces 259
5 [ — se ae
AMP Aon
ae Tan
gn x |
“10 + fh Y J
a | af ‘ |
= Vf \
318 a Va V4
Ss, af \
Q f 1
8 vf
3 af \
Bo; / \ |
3 "| \
8 if s————————+
st if -——  Gaussian(n=infinity)| \!
jaf [=== powerlaw(n=3) 1
“y ==> power-law(n=2)
ob
80-60 -40 -20 0 20 40 60 8
scattering angle (degrees)
(a)
5 re
( |
appre, |
“10 gh aN
= Le soe
@] =
= . =~
B45; / \ 1
5 af f A
8 aw “
2.20! / 4
Be i
ast} | —  Gaussian(n=infinity) 4]
if | === power-law(n=3) ]
{| == power-taw(n-2) |
pole
60 60 -40 -20 O 20 40 60 68
scattering angle (degrees)
(b)
Figure 5.5.4 Comparisons of the bistatic scattering coefficients from various spectra but
with fixed rms height of 0.3 wavelength and correlation length of 1.0 wavelength at a angle
of incidence of 30 degrees. The relative permittivity is 17.7 + 72.26. (a) TE wave; (b) TM
wave.
--- PAGE 283 ---
260 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
shown. The relative permittivity of the lower medium is 17.7 + 12.26 and
the angle of incidence is 30 degrees. Figure 5.5.4(a) is for TE wave incidence
and 5.5.4(b) is for TM wave incidence. For scattering angles smaller than 0
degrees, the surface with the power index of 2 has the strongest scattering
and the Gaussian surface has the weakest. For scattering angle larger than
0 degree, the situation is the opposite. The reason is that the surface with
smaller power index has a larger rms slope, which is an important factor
for increasing scattering in the back directions. Unlike the results presented
by Maradudin et al. (Maradudin et al. 1990; Maradudin and Mendez, 1996},
there is no obvious backscattering enhancement that is shown in these cases.
A possible reason is that rough surface used here is smoother than theirs.

In Fig. 5.5.5, we plot the brightness temperature as a function of the ob-
servation angle. The physical temperature is 300K and the other parameters
are the same as in Fig. 5.5.4. The emissivity is calculated as one minus the
reflectivity. Figure 5.5.5(a) is for horizontal polarization and 5.5.5(b) is for
vertical polarization. For the same roughness parameters of rms height and
correlation length, the differences in brightness temperature for the various
spectra can be as large as 15 K. For the horizontal polarization, this differ-
ence is almost the same for observation angles between 10 and 50 degrees.
For the vertical polarization, the difference has the largest value at the ob-
servation angle of 10 degrees and the smallest value at the observation angle
of 50 degrees. In general, the surfaces with the smaller power index have the
larger brightness temperature.

In Fig. 5.5.6, the brightness temperature is presented as a function of the
soil moistures. The relationship between soil moisture and relative permit-
tivity is from Tsang and Newton [1982] which assumes the following mixing
formula at a wavelength of \ = 21 cm:

é 2.56 +0.308m for $n < 11.5 .

a {2300 $1.B8S pq fOr Sy > 115 (6.5.32a)

ef 0.068, for 8m < 11.5

a {0 +0.1858m for Sy > 11.5 (5.5.52)
where e’ and e” are respectively the real and imaginary parts of the soil
permittivity and s,, is the percent of soil moisture by weight.

The observation angle is fixed at 30 degrees and the other parameters are
the same as in the preceding figure. Again, for the horizontal polarization,
the differences of the hrightness temperatures among the different spectra
are essentially the same for soil moistures between 5 and 30 percent. For the
vertical polarization, this difference increases with increasing soil moisture.
--- PAGE 284 ---
§5.4 Non-Gaussian Surfaces 261
990)
a 4

e180 Ps .
® 2
°
2175 .
é
5170 °
B
£165
& | eee |
5 160) © Gaussian i
| * Power law (n=3)) ¢
[2 Power law (n=2}
155~ ~~
tol
10 15 20 2 30 3 40 45 50
‘observation angle (degree)
(a)
240) $$$ poe
| aussan |
235-  * — Power law (n=3)
| |e Power law (n=2)
230
2 a 4
5
2 o
5 8
8 4 .
8720 3
g .
£215 .
z
2 °
5210)
2057
L os es)
200s =O OCGCSCSCSCSC*«SO
observation angle (degree)
{b)

Figure 5.5.5 Brightness temperature of a rough surface as a function of observation an-

gles and comparisons between various spectra. The rms height is 0.3 wavelength and the

correlation length is 1.0 wavelength. The relative permittivity is 17.7 + £2.26.
--- PAGE 285 ---
262 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
280, = a
© Gaussian
. Power Law (n=3) |
26 Power Law (n=2)
Seao- 5 |
2
eo |
3220
2 P |
s 3
200
=
S o
2180 5 |
1 ; |
8
4496-1.
5 10 15 20 25 30
soil moisture in weight percent (%)
(a)
300-—~ == ———<—<<
[ el
. Power Law (n=3)
2803 |e Power Law (n=2) _
i . \
° 3
2 al
@
S
a
3 p40- :
g ro
2
z
220} : |
a : 1
1005 10 1820 25 30
soil moisture in weight percent (%)
(b)
Figure 5.5.6 Brightness temperature of a rough surface as a function of soil moisture
and comparisons between various spectra. The rms height is 0.3 wavelength and correlation
length is 1.0 wavelength. The observation angle is 30 degrees.
--- PAGE 286 ---
REFERENCES 263
REFERENCES AND ADDITIONAL READINGS
Anastassin, H. T., M. Smelyanskiy, $. Bindiganavale, and J. L. Volakis (1998), Scattering

from relatively flat surfaces using the adaptive integral method, Radio Sci., 33(1), 7-16.

Axline, R. M. and A. K. Fung (1978), Numerical computation of scattering from a perfectly
conducting random surface, IEEE Trans. Antennas Propagat., 26(3), 482-488.

Belszynski, E., M. Belszynski, and T. Jaroszewicz (1994), A fast integral-equation solver
for electromagnetic scattering problems, IEEE Ant. end Propagat. Soc. Int. Sym., 1,
416-419.

Briggs, W. L. (1987), A Multigrid Tutorial, SIAM, Philadelphia.

Chan, C. H., §. H. Lou, L. Tsang, and J. A. Kong (1991), Electromagnetic scattering of
waves by random rough surface: A finite-difference time-domain approach, Microwave
Opt. Technol. Lett., 4(9), 355-359.

Chan, C. IL, L. Tsang, and Q. Li (1998), Monte-Carlo simulations of large-scale one-
dimensional random rough surface scattering at, near grazing incidence: Penetrable case,
IEEE Trans. Antennas Propagation, 46(1), 142-149.

Chen, J. S. and A. Ishimaru (1990), Numerical simulation of the second order Kirchhoff
approximation from very rough surfaces and study of backscattering enhancement, J.
Acous. Soc. Am., 88, 1846-1850.

Chou, H. T. (2000), Extension of the forward-backward method using spectral acceleration for
the fast analysis of large array problems, IEE Proc. — Microw., Antennas, and Propag.,
147(3), 167-172.

Chou, H. T. and J. T. Johnson (1998), A novel acceleration algorithm for the computation of
scattering from rough surfaces with the forward-backward method, Radio Sci, 33(5),
1277-1287.

Coifinan, R., V. Rohklin, and S. Wandzura (1993), The fast multipole method for the wave
equation: A pedestrian prescription, IEEE Antennas Propag. Mag., 85(3), 7-12.

Devayya, R. and D. J. Wingham (1992), The numerical calculation of rough surface scattering
by the conjugate gradient method, IEEE Trans. Geosci. Remote Sens., 80(3), 645-648.

Donohue, D. J., H. C. Ku, and D. R. Thompson (1998), Application of iterative moment
method solutions to ocean surface radar scattering, IEEE Trans. Antennas Propagat.,
46, 121-132

Fung, A. K., Z. Li, and K. S. Chen (1992), Backscattering from a randomly rough dielectric
surface, IEEE Trans. Geosci. Remote Sens., 30(2), 356-369.

Holliday, D., L. L. DeRaad, Jr., and G. J. St-Cyr (1996), Forward-backward: A new method
for computing low-grazing angle scattering, IEEE ‘rans. Antennas Propagat., 44, 722-
729.

Jandhyala, V., FE. Michielssen, $. Balasubramaniam, and W. C. Chew (1998a), A combined
steepest descent-fast multipole algorithm for the fast analysis of three-dimensional scat-
tering by rough surfaces, IEEE Trans. Geosci. Remote Sens., 36(3), 738-748.

Jandhyala, V., B. Shanker, E. Michielssen, and W. C. Chew (1998b), A fast algorithm for
the analysis of scattering by dielectric rough surface, J. Opt. Soc. Am. A, 1877-1885.

Johnson, J. T. (1996), Applications of numerical models for rough surface scattering, Ph.D.
thesis. Massachusetts Institute of ‘Technology.

Kapp, D. A. and G. S. Brown (1996), A new numerical method for rough surface scattering
calculations, IEEE Trans. Antennas Propagat., 44, 711-721.
--- PAGE 287 ---
264 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Kuga, Y., J-S. Colburn, and P, Phu (1993), Millimeter-wave scattering from one-dimensional
surfaces of different surface correlation functions, Waves in Random Media, 3, 101-110.

Li, Q. (2000), Numerical simulation of interactions of electromagnetic waves with lossy dielec-
tric surfaces using fast computational methods, Ph.D. thesis, University of Washington,
Seattle.

Li, Q., C. H. Chan, and L. Tsang (1999), Monte-Carlo simulations of wave scattering from
lossy dielectric random rough surfaces using the physics-based two-grid method and
canonical grid method, IEEE Trans. Antennas Propagat., 47(4), 752-763.

Li, Q. and L. Tsang (2001), Wave scattering from lossy dielectric random rough surfaces
using the physics-based two grid method in conjunction with the mutilevel fast umltipole
method, Radio Sci.. in press.

Li, Q., L. Tsang, K. S. Pak, and C. H. Chan (2000). Bistatic scattering and emissivities of ran-
dom rough dielectric lossy surfaces with the physics-based two-grid method in conjunc-
tion with the sparse-matrix canonical grid method, IEEE Trans. Antennas Propagat.,
48(1), 1-11.

Li, S., C. H. Chan, L. ‘Tsang, Q. Li, and L. Zhou (2000), Parallel implementation of the
sparse-matrix/cauonical grid method for the analysis of two-dimensional random rough
surfaces (‘hree-dimensional scattering problem) on a Beowulf System, IEEE ‘Trans.
Geosci. Remote Sens., 38, 1600-1608.

Lin, C. M., C. H. Chan, and L. Tsang (1999), Conical diffraction of electromagnetic waves
from one-dimensional lossy dielectric rough surfaces by combined wavelet transform and
banded-matrix iterative approach/canonical grid methods, IEEE Trans. Geosci. Remote
Sens., 37(5), 2295-2304.

Liu, C. C. and W.C. Chew (1994), A multilevel algorithm for solving a boundary integral
equation of wave scattering, Microwave Opt. Technol. Lett., 7, 466 470.

Lou, S. H., L. Tsang, and C. H. Chan (1991), Application of finite element method to Monte
Carlo simulations of scattering of waves by random rough surfaces: penetrable case,
Waves in Random Media, 1(4), 287-307.

Maradudin, A. A. and I. R. Mendez (1996), The utility of an impedance boundary condition
in the scattering of light from one-dimensional randomly rough dielectric surfaces, Optics
and Spectroscopy, 80, 109-420.

Maradudin, A. A., 'T. Michel, A. R. McGurn, and E. R. Mendez (1990), Enhanced backscat-
tering of light from a random grating, Ann. Phys., 203(2), 255-307.

Michelssen, E., A. Boag, and W. C. Chew (1996), Scattering from elongated objects, IEE’
Proceedings Microwave Ant. and Propag., 143, 277 283.

Michielssen, E. and W. C. Chew (1996), The fast steepest descent path algorithm for ana-
lyzing scattering from two-dimensional objects, Radio Sci., 31(5), 1215-1224.

Pak, K. (1996). Studies of large-scale random rough surface scattering problems based on
Monte Carlo simulations with eflicient computation integral equations methods, Ph.D.
thesis, University of Washington, Seattle.

Pak, K., L. Tsang, C. H. Chan, and J. Johnson (1995), Backscattering enhancement of vector
electromagnetic waves from two-dimensional perfectly conducting random rough surfaces
based on Monte Carlo simulations, J. Opt. Soc. Am. A, 12(11). 2491-2499.
--- PAGE 288 ---
REFERENCES 265
Pak, K.,L. Tsang, and J. Johnson (1997), Numerical simulations and backscattering enhance-
ment of electromagnetic waves from two-dimensional dielectric random rough surfaces
with the sparse matrix canonical grid method, J. Opt. Soc. Am. A, 14(7), 1515-1529.

Phillips, J. R. and J. K. White (1997), A precorrected-FFT method for electrostatic anal-
ysis of complicated 3-D structures, IEBE Transactions on Computer-Aided Design of
Integrated Circuits and Systems, 16(10), 1059 1072.

Rohklin, V. (1990), Rapid solution of integral equations of scattering theory in two dimen-
sions, J. of Comp. Phys., 36, 414-439,

Spivak, M. (1990), A numerical approach to rough surface scattering by the parabolic method,
J, Acous. Soc. Am., 87(5), 1999-2004.

Thorsos, E. 1. (1988), The validity of the Kirchhoff approximation for rough surface scattering
using a Gaussian roughness spectrum, J. Acous. Soc. Am., 83(1), 78-92.

Tsang, L., C. H. Chan, K. Pak, and H. Sangani (1994), A BMIA/FFT algorithm for the
Monte Carlo simulations of large scale random rough surface scattering, IEEE Ant. and
Propagat. Soc. Int. Sym., 8, 2028-2031.

‘Tsang, L., C. H. Chan, K. Pak, and H. Sangani (1995), Monte Carlo simulations of large-scale
problems of random rough surface scattering and applications to grazing incidence with
the BMIA/canonical grid method, IEEE Trans. Antennas Propagat., 43(8), 851-859.

Tsang, L., C. H. Chan, and H, Sangani (1993), A banded matrix iterative approach to Monte
Carlo simulations of scattering of waves by large-scale random rough surface problems:
TM case, Blectronics Lett., 29(2), 166-168.

Tsang, L., C. H. Chan, and HH. Sangani (1993b), Application of a banded matrix iterative
approach to Monte Carlo simulations of scattering of waves by a random rough surface:
TM Case, Microwave Opt. Technol. Lett., 6(2), 148-151.

Tsang, L., C. H. Chan, H. Sangani, A. Ishimaru, and P. Phu (1993c), A banded matrix itera-
tive approach to Monte-Carlo simulations of large-scale random rough surface scattering:
TE case, J. Blectromag. Waves and Appl.. 7(9), 1185-1200.

‘Tsang, L. and Q. Li (1997), Numerical solution of scattering of waves by lossy dielectric
surfaces using a physics-based two-grid method, Microwave Opt. Technol. Lett., 16(6),
356-364.

‘Tsang, L. and R. W. Newton (1982), Microwave emissions from soils with rough surfaces, J.
Geophys. Res., 87(11), 9017-9024.

West, J. C. and J. M. Sturm (1999), On iterative approaches for electromagnetic rough-
surface scattering problems, IEEE Trans. Antennas Propagat., 47(8), 1281-1288.
--- PAGE 289 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs: 0-471-38800-9 (Hardback); 0-471-22430-8 (Hlectronic)

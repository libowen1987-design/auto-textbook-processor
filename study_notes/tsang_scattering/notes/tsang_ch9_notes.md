# Tsang《Scattering of EM Waves》Chapter 9

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 9, Section 2 of Volume I. We first note that from Eq. (9.2.10) of

> **第九章：随机粗糙面模拟**。研究随机粗糙面的数值模拟方法，包括粗糙面的统计表征、高斯和非高斯粗糙面的生成算法、自相关函数的控制、以及粗糙面电磁散射的数值模拟技术。**

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
--- PAGE 162 ---
§2.1 VE and 1M Waves 139
2.1 TE and TM Waves
Surface integral equations are also conveniently expressed in terms of surface
electric current J, and surface magnetic current M,. For fT on S,
J,=axH (4.2.10)
M,=Exh (4.2.11)
(A) TE case: 1: represents the electric field
E=jyp (4.2.12)
> 1
H=-——yx Vy 4.2.13)
io * ( )
axH=-“(a-vy) (4.2.14)
twp
Similar relations apply to £1, H), and yj. Thus for = on S, the boundary
conditions of continuity of the tangential electric and magnetic fields become
respectively,
WF) = vi(F) (4.2.15)
A-Vyplr) =A- Vun(F) (4.2.16)
(B) TM case: 7) represents the magnetic field
If = ip (4.2.17)
= 1
B= —yx Vi (4.2.18)
WWE
Byun De wy
Exni=-—(f- Vy) (4.2.19)
_ iwe
Ay =H (4.2.20)
Ey xa=—-“L(a- vin) (4.2.21)
iwe,
For F on S, the boundary conditions of continuity of tangential clectric and
magnetic field become respectively,
a Vul®) = ~A- Ven F) (4.2.22)
€l
wT) = w(7) (4.2.23)
The TE and TM cases when put into (4.2.9) become
50) + feaswiryi VoilF.?) -| dsgi(F,7)ph- VF) =0 (4.2.24)
s
--- PAGE 163 ---
140 4 RANDOM ROUGH SURFACE SIMULATIONS:
where p = 1 for TE wave and p = €1/¢ for TM wave.
Let
LLY woo ;
u(x) = \) +(e (A ViF)) f(a) (4.2.25)
Then the dual integral equations of (4.2.1) and (4.2.24) become
, “ 1
Wine(2’) +/[ dx (w(x) Kv (2", 2) - K(a',x)u(x)] = ge’) (4.2.26)
1 -° ,
5ue’) + f de [(a) Kay (2",2) — Ky(a',2)pu(e)] =0 (4.2.27)
~co
In (4.2.27), the kernels Kyy(2’,2) and Ky(u',x) are that of using
Green’s function g; of the lower medium that has wavenumber ky
Ky (2',2) =q(a', f(x’); 2, f(«))
i 7 +}
= 5H) (nV @ =a FF) F@)P) (4.2.28)
ip, Ht (nye 2 +7) — 1009")
Kyy(a',2) — > nee
Veer =a + (fa) = Fa)?
- {f'(a)(@ — 2") — (F(x) — f(2"))} (4.2.29)
We obtain the matrix equation from (4.2.26)
N N
So Amntin + S2 Brann = brn (4.2.30)
n=l n=l
where Amn is given by (4.1.28) of the Dirichlet case and Bmn is given by
(4,1.156) or (4.1.167) of the Neumann case.
For the surface integral equation of (4.2.27)
N N
SO AD, p tn + YF BO tin = 0 (4.2.31)
nt n=l
where
Az Ki(tm,%n) form #n.
4) —) iA i :
Ainn = 5 (A® 1 + 2 (EL atn) form=n (4.2.32)
4 ‘® de
—Az Kin (@m,2n;0) form #n
B= > 1 fam) de (4.2.33)
Hs - SS —_—_.. form=n
2 an 1+ (f"(am))?
--- PAGE 164 ---
§2.2 Absorptivity, Emissivity and Reflectivity 141
Note that there is a sign difference in the 3 term between Bm, and BY),
Equations (4.2.30) and (4.2.31) are for m = 1,2,...,N. They provide 2N
equations for the 2N unknowns of tn, Un, m = 1,2,...,N. In Section 2.3,
we discuss numerical integration to obtain more accurate matrix elements.
2.2 Absorptivity, Emissivity and Reflectivity
Consider the incident wave impinging on the dielectric medium at an incident
angle of @;. We can calculate o (0,,0;), the bistatic scattering coefficient
from incident, direction 6; into scattered direction #,. The reflectivity is the
integration of the bistatic scattering coefficient
(0) = | * dso (0s) (4.2.34)
“2
This is a way of calculating reflectivity. For perfect conductor the reflectivity
should be equal to unity. This provides a useful check on the numerical
accuracy of the bistatic scattering coefficient. For penetrable medium, the
absorptivity is
a (0;)) =1—r (4) (4.2.35)
The emissivity is equal to the absorptivity
e(8;) = a(@;) = 1— r(0;) (4.2.36)
and the brightness temperature is equal to
Tp (0) = € (6) T (4.2.37)
where T is the physical temperature. We can use (4.2.34) and (4.2.36) to
calculate emissivity.

In Monte Carlo simulations, we can calculate the surface fields for each
realization of the rough surface. We can also use the surface fields to calculate
reflectivity and absorptivity. The power absorbed in medium 1 is

lf _
P, = 3/ oF welE,)? (4.2.38)
vi
Using Maxwell’s equations, it follows that
1 ee
Py= ~5Re [ drv-(E. x Hi)
a hy
Using the divergence theorem and the continuity of tangential fields,
1 ~ (F >
P= — pre [asi (Ex mf)
--- PAGE 165 ---
142 4 RANDOM ROUGH SURFACE SIMULATIONS
lL, fs. (=o
=-5Re | asa (ExT)
2 Ss
=- | dst -3 (4.2.39)
Is
In terms of the wavefunction, we then have
1 “ ‘
Py= re )
2
=m far + (2) awe)
Ink : dx ”
1 ;
=a" / dv} (a) u* (@) (4.2.40)
ay” (5
where u(x) = 4/1+ (4) (i- Vib) 2=F(0):
The absorptivity, which is equal to emissivity, is
P,
a(;) = e(0;) =s* (4.2.41)
Pine
For the case of tapered incident wave,
im f dew(a)ur(e)
| = = 4.2.42
a(8:) (61) k 6 ca 1 1+ 2tan? 0; ( )
6 COS Oj 7 D122 Dd
CSMIND 2k? 9? cos? 0;
This formula allows the calculation of absorptivity and emissivity in terms
of surface fields. The reflectivity can also be calculated using surface fields.
The scattered power is
1 ~ fe oad . (aoa
P, = 5Re [. dsh- (B. x H.) = pre [as Ae (Es x i) (4.2.43)
‘Thus the reflectivity is
7 (6) = 2 (4.2.44)
Pine
and for the case of tapered wave, we have
im [ae ws (x) us (x)
" ToT VV 4.2.45
” (6) beost.g, (Ef, — 1+ 2tan™O, (4.2.45)
CS MIND LO Bheg? cos? 8;
--- PAGE 166 ---
§2.3 Impedance Matrix Elements: Numerical Integrations 143
where the surface scattered fields are
ts (e) = 0 (a) ~ Vine(w) (4.2.46)
Us (£) = u(2) — Uine(®) (4.2.47)
On the rough surface, we have, for the case of a tapered incident wave,
Wine (©) = Vine (2 = f(x) (4.2.48)
ha (4y weve
Uine (x) = \ 1+ (¢ Gn Vine] za f(2)
vf. df.
= Wine (x) 4 ik (1+ w) -b sin; — cos 9;
x tan 0, q
4 dik (wsind; — zcoso;) 2214) (tan 6; - #)
9? (kg cos 8;) dx
a+ ztan8, d
+ g(t + ztan 6) (¢ ~tane,) } (4.2.49)
£ da 2=H(0)
2.3. Impedance Matrix Elements: Numerical Integrations
The rough surface can have fine scale structures. By fine scale structures, we
mean irregularities that are smaller than a wavelength and yet have large
slopes. They can also have radius of curvature smaller or much smaller than
a wavelength. It can become necessary to perform numerical integrations to
calculate the impedance matrix elements accurately. The matrix equations
are
N N
bm = Y> Amnttn ~ Y> Bran'in = 0 (4.2.50)
n=h n=l
N N
So AD un +2 BO an = 0 (4.2.51)
n=l n=1
using the pulse basis functions and point matching.
For non-self patches, we can perform integration on the integrals as
follows. For m 4 n,
Ey SE
Ayn = [ 2K (2m, 2) (4.2.52)
tn, BE
Py tAe
AQ = [OF dean.) (4.2.53)
BaP
--- PAGE 167 ---
144 4 RANDOM ROUGH SURFACE SIMULATIONS
Ln SE
Brn = [ 4, (eK (ems) (4.2.54)
pity + AE
BUY) = - | dak iw m2) (4.2.55)
For self patches, the formulas for numerical integrations are
Brun = Bran +5 (4.2.56)
Bi, = BY, 5 (4.2.57)
where
5 pe ; | ik? (kV Gm — 2 + F@m) — FOE)
ram = I
Fi 82 4 Vm — 2 + (F@m) — F(@))?
dj
[ete — an) — Vee) ~ flem)| } (4.258)
50) fo and (hv Gn 24 TG) — FOP)
Sieg 4 V(tim — 2)? + (Fm) — F(a)?
df (a 5
[Fe ~ =m) ~ 1) ~ sem) \ (1.2.59)
= iAx 2) (yk Loe
Arn = Arnon + I +=In ( An) (4.2.60)
~ mt SE i
nm = f _ ao{ Lng? (§V@— en) + Fe) Fen?)
-5 [ +i2n (TeV@= an) FU) — FenP)| \ (4.261)
a ga 4 At], 2), (ae
Aram = Amin + FZ [: ton [Alm (4.2.62)
gm. fr Sign 2 2
Ag), = [OF deg tH (nye = aml? + FO) ~ Flem))
i 2 y a Vary a) PS
-4 [ +i=n (Zh Veo, P+ F@) “Tea)]} (4.2.63)
--- PAGE 168 ---
§2.4 Simulation Results 145
where
Alm = Avv1+ (f(@m))? (4.2.64)
and f denotes principal value, i.c., with a section of very small radius a
subtracted from the interval of integration. Numerical integrations are per-
formed over the integrals in (4.2.52)-(4.2.55) and (4.2.58)-(4.2.63) to im-
prove the accuracy of the impedance matrix elements.
2.4 Simulation Results
The MATLAB programs used to generate the simulation results in this sec-
tion can be found on the World Wide Web at http: //www.emwave.com.
2.4.1 Gaussian Surface and Comparisons with Analytical Methods
Tn this section, we simulate scattering from Gaussian random rough surface
profiles with rms height h for the Dirichlet problem. The correlation function
is also Gaussian with
a
C(a) = exp (-#) (4.2.65)
In the simulation, N = 256 points are used. All distance units are in terms
of free space wavelength.
For Gaussian random rough surface and Gaussian correlation function,
the power spectrum is, from (9.2.14) of Volume I,
Wl RP
W (ke) = 572 exp(-“=-) 4.2.66
(ke) = 5 wa (4.2.66)
The bistatic scattering coefficient for the incoherent wave from the small
perturbation method (SPM) is, from (9.3.40) of Volume I,
al (sin 9, — sin 6;)?k? 1?
85) = 4k° cos? 0, cos 8; ——= exp | ——— 4.2.67
a(9s) cos” Ms cos 4 aR xp m1 ( )
For the Kirchhoff approximation (KA), we first calculate, from (9.4.45) of
Volume I,
1 fe , nem Be
WM (ke) = — f dae 7h?" C™ (aw) = —— exp |-=—] (4.2.68
(ke) 2m Juco (2) 2/mr F 4m ( )
Then the bistatic scattcring coefficient for the incoherent wave from the
Kirchhoff approximation follows from (9.4.47) of Volume I,
--- PAGE 169 ---
146 4 RANDOM ROUGH SURFACE SIMULATIONS
>» kK 279 9
o(85) = |1 + cos(®j + 9.)P exp [-#A? (cos 0; + cos 6.)"|
208
S. (k(cos 6; +608 85))2"—D R24 Re ae ;
x re a exp [i sn, sin 6) (4.2.69)

In Fig. 4.2.1, we show a single realization of rough surface profile with
h = 0.05, | = 0.35, L = 25.6, and Ax = 0.1. Since 1 < L, we see many
peaks and valleys in the realization. Note that the vertical and horizontal
scales are different so that the slopes are exaggerated in the figure. Although
the rms height is h = 0.05, the maximum and minimum f(x) can go up to
0.1 and ~0.1 respectively. Thus the maximum peak to valley separation can
be as large as 0.2 for an rms height of 0.05.

We usc the spatial tapered wave of (4.1.31). We use an incident angle
of 0; = 30°, and g = £ We calculate (0s) for each realization, The average
bistatic scattering coefficient (a(0,)) is o(0;) averaged over 100 realizations.

Four cases are considered: (a) h = 0.005, | = 0.35; (b) h = 0.005, | =
0.20; (c) h = 0.2, 1 = 1.5; (d) h = 0.2, 1 = 0.6.

In Fig. 4.2.2, a single realization of o(0,) for case (a) is shown. Because
of the small rms height, we see a distinct coherent. wave peak in the specular
direction of 0, = 6;. Since the result is only for one realization, there are
angular fluctuations as a result of constructive and destructive interferences
as a function of 45.

In Figs. 4.2.3-4.2.6, we show the results of (o(@,)) for cases (a), (b), (c),
and (d), respectively, averaged over 100 realizations. The results of (o(@s))
for the incoherent wave based on the small perturbation method and the
Kirchhoff approximation are also shown for comparison. We see that after
averaging, the plot of (o(@s)) is much smoother than that: of (4) of one
realization.

In Fig. 4.2.3, the parameters are h = 0.05 and | = 0.35. Because of
the small height, we see a distinct angular peak in the specular direction of
0, = 9; = 30°. Because of the small slope, (7(4;)) decreases rapidly away
from the specular direction. In Fig. 4.2.4, the results are for the same h and
a smaller J of 0.2. We see that (a(0,)) decreases less rapidly with @, when
compared with Fig. 4.2.3. Note that the results of ((#,)) for SPM and
KA are for the incoherent wave only. The results of SPM are in excellent:
agreement with numerical simulations. However, the results of KA only agree
in the vicinity of the specular direction. The results of KA are poor for large
@, because shadowing effects have been neglected.
--- PAGE 170 ---
§2.4 Simulation Results 147
Se . —
o2-
ors
‘ . , , ,

f Aonh Hl j\ i
0s, ho ANA fh hf /l iia
we IAM IK Fat EA EEE yg iii
Bah VV Tle Waeb a mM Aate
= yo Vat \ ia Hy I
Pour AM OW WEAVE Why
po tt Oy yey ES Ps ;
yoy voy y
01 it
V
01s J
“|
0255 3 ° 3 v0
x
Figure 4.2.1 A single realization of a Gaussian rough surface profile with h = 0.05,
1=0.35, L = 25.6, N = 256.
a
fl
tI
im
5 {|
) | |
= it
s It
; 4
* Af |
Aid
2 Derrat trick A
ite { aaa)
§0 Nt LAE Tea
£ haere te ap LE bn Be
i bare VE AR LT OLE TS
3 a rr Lp. Sta,
oe Pear ee a ec
3 eA GY \ Vinee:
ee a ee
© -20 4 ia i Yow As
cd a | vat
aN . if \s
as ‘| We \A
i voy
we yl
ar a a 0° 2% 4 6 ©
Scattering angle (deg)

Figure 4.2.2 N = 256, Av = 0.1, L = 25.6, 0; = 30°, h — 0.05, 1 = 0.35, g = &, and

one realization. Solid curve: MoM; dashed curve: SPM; +: KA.
--- PAGE 171 ---
148 4 RANDOM ROUGH SURFACE SIMULATIONS
10 nay aa
f
i | |
i}
s i |
hy
o | \
Ss | | \
oe i
5 wets |
9 OTL | i
Pool pee ca J
5 od
2 ies Nee i
5 as| wee the
g we Nye
ele te
3 aol / Yo
f \
A \|
fo iv
» ee a
rr ee er ee er a)
Scattering angle (deg)
Figure 4.2.3 N = 256, Ar =0.1, L = 25.6, 4; = 30°, h = 0.05, 1= 0.35, g = &, and
100 realizations. Solid curve: MoM; dashed curve: SPM; +: KA.
ee a
| /\ |
i
5 ia |
Hy 1
| t
a 4 i | j
g i |
‘ 1
5 s | \ 4
2 | \ |
Pal [pI SON |
2 | eet Pe Py |
Bobet y
o8 y SH.
hal / -
/ \ 7
asl. / \
| VO
| \
Pe ee
a rr a a a oe ee |
Scattering angle (deg)
Figure 4.2.4 N = 256, Ar = 0.1, L = 25.6, 6; = 30°, h = 0.05, 1=0.2, g= 4, and 100
realizations. Solid curve: MoM; dashed curve: SPM; +: KA.
--- PAGE 172 ---
§2.4 Simulation Results 149
, ‘,
3 we! —
8 10> yr i AN
2. Yo! Na
3 Vani Ve
a J SV
ey ; ‘|
7, ' :
“40 w/ ; 4
+/ !
7, }
nee eee ee
a a a a a a |
Scattering angle (deg)
Figure 4.2.5 N = 256, b= 25.6, 6 = 30°, h=0.2, 1= 1.5, g = , and 100 realizations.
Solid curve: MoM; dashed curve: SPM; +: KA.
10% |
g° a a
g omen —
= EORTC RTS.
3 aye cen
Seo pat ra Nw
QD +H ‘ \\
gue va , \ i
5 / ,
Bao / / \
s | / / \
s |/ /

/ i
wh ]
ce ane

Scattering angle (deg)
Figure 4.2.6 N = 256, L = 25.6, 0; = 30°, h = 0.2, 1= 0.6, g = %, and 100 realizations.
Solid curve: MoM; dashed curve: SPM; +: KA.
--- PAGE 173 ---
150 4 RANDOM ROUGH SURFACE SIMULATIONS

In Figs. 4.2.5 and 4.2.6, we show the results of a larger rms height of h =
0.2. The coherent specular peak disappears in the numerical simulation. For
Fig. 4.2.5, with a large correlation length of | = 1.5, there is good agreement,
between KA and numerical simulations. The agreement is particularly good
in the vicinity of the specular direction. This case has a large radius of
curvature that accounts for the agreement. However, for this case the fact
that kh = 1.26 is larger than unity accounts for the poor agreement of SPM
with numerical simulations. For Fig. 4.2.6, we use a smaller correlation length
of | = 0.6. Because of the larger slope, we have larger bistatic scattering
return. SPM results are incorrect. KA also gives poor results for larger 0,
because of the neglect of multiple scattering and shadowing.
2.4.2 Dirichlet Case of Gaussian Surface with Ocean Spectrum and Fractal

Surface

We next illustrate rough surface scattering from Gaussian surfaces with
ocean spectrum and from fractal surfaces. To compare scattering from dif-
ferent surfaces, the equivalent rms height and correlation length are first
calculated from the ocean spectrum.

Assuming the wind speed at z = 5 is 10 m/s. We can first: solve for uy
(ux = 0.437198), The lower and upper limits of the ocean spectrum chosen
are ky = 100m™~! and ky = 4000m~!. We then calculate the equivalent
rms height as h = 8.1202 x 10-‘m from (4.1.134). Then the rms slope s
can be calculated from (4.1.135). The equivalent correlation length is | =
V2h/s. For this case, the equivalent correlation length is calculated to be
1 = 5.0993 x 1073 m. Frequency is 19 GHz. The surface length is L = 25.6
and 10 points per wavelength are taken on the rough surface (N = 256). For
fractal surface, the number of tones (Ny) is 100 and the fractal dimension
sis 1.5. Numerical integration is not performed to calculate the impedance
matrix elements. The formulas of (4.1.27) and (4.1.28) are used.

For the incident field, we use tapered plane wave at 6; = 50° with
g = L/A. The bistatic scattering coefficients averaged over 100 realizations
are plotted as a function of observation angle. In Fig. 4.2.7, we show, for refer-
ence, the results for Gaussian surfaces with Gaussian spectrum. Figures. 4.2.8
and 4.2.9 show the cases of Gaussian surfaces with ocean spectrum and of
fractal surfaces, respectively. Note that a forward scattering peak appears
at @, = 50° (the specular direction). In comparison with Gaussian surfaces
with Gaussian correlation function, the bistatic scattering coefficients for
the ocean surfaces of Vig. 4.2.8 and the fractal surfaces of Fig. 4.2.9 both
show a “dip” near the specular direction. This is because for both cases, the
--- PAGE 174 ---
§2.4 Simulation Results 151
10
5
a
3
s |
25 |
s
2
@ -10-
8
2
45-
5 5 -21.573
§ -20 |
2
#25
a
ao
-30- |
“35
80 60 -40 -20 oO 2 40 60 80
Scattering angle in degrees
Figure 4.2.7 Bistatic scattering coeflicient for Gaussian surfaces with Gaussian spectrum,
rough surface spectrum is bandlimited. The bandlimited spectrum means
that there is no spectral component less than kz, to contribute to scattering
near the specular direction. The backscattering coefficients for random rough
surfaces are at 0, = —50°. We found that fractal surfaces have the largest.
backscattering.
2.4.3 Bistatic Scattering for Two Media Problem with Ocean Spectrum
Tn the two media problem, we use a relative permittivity of ocean ¢, of
28.9541 + 136.8430 for 19 GHz and 13.2444 + 124.5221 for 37 GHz for the
lower medium. After solving u, and wn, the bistatic scattering coefficient can
be calculated by integrating the fields over the rough surface using (4.1.50).
Parameters for the incident field and for ocean spectrum are the same as Sec-
tion 2.4.2. The surface length is L = 20). Results are shown for impedance
matrix elements with and without numerical integrations for TE and TM.
The numerical integration is done for both self-patch term and near field
terms ((m —n) Ax < A). For bistatic scattering coefficients, numerical inte-
grations do not seem to result in significant differences.
For the simulations, a discretization of 40 points per wavelength is used
for this simulation. The bistatic scattering coefficients averaged over 50 real-
--- PAGE 175 ---
152 4 RANDOM ROUGH SURFACE SIMULATIONS
10 ++
8
a 0 1
2 |
s |
€ 5
Ss
2
@ +10
8
38
2s: |
s | |
% ool 24.324 |
§ -20 ‘
2 { i
# 25
2
o
“30
ee
80 60 -40 -20 0 2 40 6 80
Scattering angle in degrees
Figure 4.2.8 Bistatic scattering coefficient for Gaussian surfaces with ocean spectrum.
10. >_>.
:
m@ OF
ie]
&
= 5
5 |
S| !
5 10 4
8 |
8
D
£15 20,968
5 |
§ -20r
2
# 25: |
3 i
o
-30 1
wag a
-80 60 40 +20 0 20 40 60 80
Scaitering angle in degrees
Figure 4.2.9 Bistatic scattering coefficient for fractal surfaces.
--- PAGE 176 ---
§2.4 Simulation Results 153
OO aU Aa |
g °
£
3
é -10)
8!
27 |
g } {
5
@ -30| 7
8
=
2
® -a0|
50
-100 80 60 ~40 +20 oO 20 40 60 80 100
Scattering angle in degrees
Figure 4.2.10 Bistatic scattering coefficient from ocean surface. TE polarization. Without
numerical integration of impedance matrix elements: ¢(—50°) = —26.316d4B and o(50°) =
7.028 dB. With integration: ¢(—50°) = —26,283 dB and o(—50°) = 7.043 dB.
oo
ol
a
g
fa | )
e
2
3
= -10]
8
8 i
aa 1
$ |
§ 2)
5
2
& -25
2
ao
-30|
a
-100  -80 60 40 -20 oO 20 40 60 80 100
Scattering angle in degrees
Figure 4.2.11 Bistatic scattering coefficient, from ocean surface. TM polarization. Without
numerical integration of impedance matrix elements: ¢(—50°) — —17.697dB and o(50°) =
4.378 dB. With integration: o(—50°) = —17.693dB and o(—50°) = 4.349 dB.
--- PAGE 177 ---
154 4 RANDOM ROUGH SURFACE SIMULATIONS
izations are plotted as a function of observation angle. Results with and
without numerical integrations to obtain matrix elements are plotted in
Figs. 4.2.10 and 4.2.11 respectively for TE and TM waves. There is no
appreciable difference between the results with and without numerical in-
tegrations. Results of backscattering coefficients can have 1.3dB difference
between using 30 or 40 points per wavelength.
3 Topics of Numerical Simulations
In this section, we discuss several aspects in the numerical simulations of
rough surface scattering. The topics include periodic boundary condition,
MFIE for TE case, and the impedance boundary condition.
3.1 Periodic Boundary Condition
To prevent current discontinuity at « = +L/2, a tapered incident wave
was introduced either in the spatial domain or in the spectral domain. An
alternative method is to use the periodic boundary condition. In this case,
an incident plane wave is used:
Vine(F) = ele -thuee (4.3.1)
‘To prevent current discontinuity, the surface is assumed to be infinite, that is,
@ is from ~oo to oo. Obviously, in numerical methods, we cannot deal with
a rough surface of infinite length. To circumvent this problem, a periodic
surface with period P is assumed. Thus
f(@+P) = f(x) (4.3.2)
for the height profile. However, the period P is quite large, P > /, where
lis the correlation length, so that there are many peaks and valleys of the
height profile within the period P.
The integral equation is given by (4.1.15) for the Dirichlet. boundary
condition:
vine?) = fds o(rr ya VC) (433)
Ss
for F and 7” on S. This means that
rod
Viola’) = eRe =P de gah fle))ule) (43.4)
~oo
where
= 14 (£) @-voe (435)
u(r) = \ +( a) @ WF) 2=F(2) 3.5
--- PAGE 178 ---
§3.1 Periodic Boundary Condition 155
is the surface unknown.
To solve (4.3.4), we use the Bloch condition as in Chapter 3. Let
u(a) = eT w(x) (4.3.6)
and w(2) is a periodic function obeying
w(e2+ P) = w(2) (4.3.7)
We next convert the integral equation to be with one period from —P/2
to P/2. We follow Section 1 of Chapter 3. Let the periodic Green’s function
be defined by
oo
gp(@', 2/3252) = D> g(a’, z/;a + mL, zee (4.3.8)
m=—00
Then the integral equation (4.3.4) becomes
2
efhist’— thie! — [ dx gpa’, z'; 2, f(x))c**w(a) (4.3.9)
2
The integral equation in (4.3.9) needs to be solved only over one period.
Solution methods were discussed in Chapter 3. The periodic Green’s func-
tion can be presented in the spectral domain as in Section 1 of Chapter 3.
Equation (4.3.9) can be solved using the T-matrix method as in Section 2
of Chapter 3.
Let
2am
Kem = hie + (4.3.10)
Kiem = Vk* — ken (4.3.11)
be the wave vector components of the mth Floquet mode.
The integral equation becomes
i fz ca ikemetikem f(2)
bmo = Sp / ‘ da EH) (4.3.12)
where u(2) is as given by (4.3.6). To solve (4.3.12), a Fourier series expansion
of w(a) can be made
eS
ann
w(x) = > wre Pr * (4.3.13)
n=~00
Let.
i oft en tksmt+ikem f(t) +ikent
= ——— ee 4.3.
Amn op I. dx Tom (4.3.14)
--- PAGE 179 ---
156 4 RANDOM ROUGH SURFACE SIMULATIONS
to denote the coupling between the mth and nth Floquet modes, then the
matrix equation is

oo

SS Anntwn = dno (4.3.15)

n==00

Tn actual numerical implementation, the number of modes are truncated by
keeping all the propagating modes |kym| < & and a reasonable number of
evanescent: modes. Suppose we keep modes from —N to M so that we have
a total of N + M +1 modes, we then have the standard matrix equation of
dimension M@ +N +1.

M

YE Ann = bmo (4.3.16)

n=—N
m=-N,-N+1,...,-1,0,1,...,M.
Suppose P = 25.6 wavelengths. Then
Qn Qari
P  (25.6)A — (25.6)\ 25.6

Thus

ham = bie +
To illustrate, let kjz = 0 (normal incidence). Then

mk
kom = D6

The propagating modes are m = —25,—-24,...,1,0,1,...,25, a total of 51
propagating modes. Suppose we put 5 evanescent: modes on both sides giving
us 61 modes. Thus we have p,, m = —30,-29, —28, -27,...,-1,0,1,...,30.
The larger the value of P, the smaller is the mode spacing, and the more
modes we have. For example, for P = 25.6, we have 60/25.6 = 2.3 modes
per wayelength. This method of mode expansion has the advantage over
the method of subsectional basis function, which needs 10 points (i.e., 10
subsectional basis functions) per wavelength. The method of subsectional
basis function needs 256 unknowns for the case P = 25.6\. On the other
hand, the periodic boundary condition method uses 51 modes. However, the
disadvantage of the mode expansion method is that the diagonal elements of
the matrix equation may not be dominant. As can be scen from (4.3.14), Amn
depends on f(x). If f(a) is small, then Ay», has large diagonal elements. For
the special case when f(a) = 0, we have Amn = 54mm and all off-diagonal
elements are zero. However, for large values of f(x), the diagonal elements
--- PAGE 180 ---
§3.1 Periodic Boundary Condition 157
may not be large compared with the off-diagonal elements. Also for kzm
imaginary, depending on how large is f(x), the integrand in (4.3.14) can be
exponentially large or exponentially small. Thus some off-diagonal elements
can be exponentially large or exponential small, giving an ill-conditioned
matrix. Nevertheless, the periodic boundary condition method is quite useful
in the small height limit.
After the w,,’s are solved, we can calculate the scattered field as follows:
oo
s(2’, 2") = > Bypeibeme’ +ikeme! (4.3.17)
m=—00
where
20
bm = SS Brun (4.3.18)
n=—90
Pp .
i fF, em iRemamikemf(@)
Brn = op [. dx ae (4.3.19)
The incident power per unit area is
=. 1
Sine 2 = 3 4; (4.3.20)
The power per unit area outflowing from the surface is
rl i OWS
‘Ss + 2) = Re{ ——y,—* 4.3.21
6-2) (Gv) (4.3.21)
If we integrate over a period, then
z ~
i 2 Ka 2 Kem akem
i a (Sy +3) = Pm | = Sem
p fae 82) re( Pl 5 Sb Se
2 m=—s0 im. propagating
‘modes only
(4.3.22)
We only have propagating modes in (4.3.22) because kz,, of evanescent
modes are imaginary. Next we need to convert the result to bistatic scattering
coefficients as a function of scattered angle. Let
kom = ksin 0, (4.3.23)
For each discrete m, there corresponds a scattered angle @,. ‘Thus we have
discrete scattered angles. The spacing of kzm is 27/P, so that in the limit
of large P the discrete angles almost form a continuum. To convert the
summation to integration, we note that since the kym’s are spaced 27/P
apart we have
Qn
Akem = - (4.3.24)
--- PAGE 181 ---
158 4 RANDOM ROUGH SURFACE SIMULATIONS
Thus
P P f* P fz
== Akem = - rm = >~ A A 4.3.25
D =D Ahm = [a = [ a0, tecost, (43.25)
Propagat Propagat 2
From (4.3.22) and (4.3.25) and using kzm = kcos@, we obtain
Left og . Pl fF :
3 I. de B,-2) = 5 [. 8, 008? Bslb mal? (4.3.26)
Since the incident power per unit area is an the bistatic scattering coef-
ficient is
Pk 2 2 95
o(8.) = wand A. |Drn|* (4.3.27)
In Chapter 5, we shall compare the numerical results of using periodic bound-
ary condition with that of using a large surface length L of many wavelengths.
3.2 MFIE for TE Case of PEC
For scattering by PEC, we have used EFIE as given by (4.1.11) for TE case
and MFIE as given by (4.1.151) for TM case. For EFIE of the TE case, the
self patch is of order O(Aa In Ax) as given by (4.1.28) and the non-self patch
is of order O{Azx). On the other hand, for MFIE of the TM case, the self
patch is equal to 1/2 as represented by (4.1.156). Non-self patch is of order
O(Az). Thus MFIE gives larger diagonal elements for the impedance matrix
and that gives a better condition number. In this section, the MFIE for the
TE case is derived which results in larger diagonal elements than the EFIE
for TE case.
We use (4.1.10) and take normal derivative with respect to 7 and let 7”
approach the surface
. . on oo al Vuh) FeV
A! VinelF)— [ as|i’ V'g(F,®)) fh - VHP) = { ave) Fe Vo
(4.3.28)
The self patch analysis can be performed as in Section 1.5 for the Neumann
case. The integral equation becomes, for F and 7’ on surface S,
1
WV Vine ®) = 3 Vur) +f ds{h! - V'g(F,7' Ila Vo)
s
lar one) efaclat p22] w-cumy U3:
=5% Var) fas [a R OR [A-VuF)} (4.3.29)
--- PAGE 182 ---
§3.2 MFIE for TE Case of PEC 159
where f ds is the principal value integral which is integration by subtracting
s
out a very small section of radius a about (a’, f(x’). Let the surface unknown
be
V(2) = [i VOM]. 72) (4.3.30)
and
Vine(t) = [ft > Vebine()]2=p(2) (4.3.31)
Note that the self patch is of order unity. The kernel is also different from the
Neumann case because the surface normal #’ is at the field point * rather
than at the source point 7. The integral equation is
1 M
Vine(x") = 5V@) + f dxK™) (z’,2)V (2) (4.3.32)
where
M) oot TNS gt. py O!
KEY (ala) = 1+ Fen: woe
_ kA kV @ =P) — FO)
TV Fe) Fey?
LHF)? 6 py near /
a (O(a @)— f(x 43.33
(ra erenp POM —0) + (400) ~ Ha))] (43:38)
To compute numerical results, we use MoM with pulse basis functions
and point matching. To obtain accurate results, particularly for energy con-
servation, we use numerical integration to calculate near-field impedance
matrix clements including the self patch.
The matrix equation is
N
So AGO Va = Om (4.3.34)
n=1
where
bin = Vine(&m) (4.3.35)
Va = V(tn) (4.3.36)
Without numerical integration, the matrix clements are
1 for m
= r =n
AM = 2 2 (4.3.37)
KG (Gm itn )Ar formAn
--- PAGE 183 ---
160 4 RANDOM ROUGH SURFACE SIMULATIONS
Bp rr 1
| — WIE |
| 7 a2 ERIE ||
o f\ ("\ \ A |
| / AV Naat
a | Nat v AMAA
8 os. ii fh | fy | VAG A |
2 iif hf WAVE a {\
5 i iy VALU at 4 \
3 i if Heliyir yg (ofA
5-10 i il cl Ho ALY |
8 | i Yl | i | MAA g
2 | | I} ti wy |
£ rst | \ |
a \ lt .
2 | ie
do} a) Hoo
V } y
25 ‘ i \
v Wo
\ |
a
“100-8602 0 2 «40~C«sSCti«iSC«
Scattering angle (degrees)
Figure 4.3.1 Comparison of the bistatic scattering coefficient of 1 realization for TE case
using MFIE and EFIE at 6; = 30° with h = 0.4A, 1 = 0.2A, and L = 25.64. 80 points/A
discretization and near-field integration are used in the simulation.
With numerical integration, the matrix elements are
1 mb ;
3 +f “de KE? en, 2) form=n
M) _ Lm — AE
ACY ate (4.3.37)
i dx KO9 Gn, 2) form An
Jay 92
where f denotes principal value integration. In Fig. 4.3.1, we compare the
bistatic scattering coefficients for one realization using MFIE and EFIE for
TE wave with 6; = 30°, h = 0.4A, | = 0.2A, and L = 25.64. Because the
correlation length is small, we use 80 points per wavelength. The results
for bistatic scattering coefficients are almost indistinguishable in dB scale.
Nevertheless there are major differences in energy conservation. The test is
to compute
--- PAGE 184 ---
§3.3 Impedance Boundary Condition 161
—
No of points/A ; No. num. int. | With num. int. | No. num. int. With num. int.

. 40 i 0.83603 ____ 0.9158 1.0021 1.0023
80 0.9036 0.9530 H 0.99955 0.9996
Table 4.3.1 Comparison of the energy conservation for TE case using MEIE at @; = 30°
with h = 04,1 = 0.2, and L = 25.6..
P= dO, (5)
-3

which should be equal to unity. The results are tabulated in Table 4.3.1

for 40 points per wavelength and 80 points per wavelength. We note that

energy conservation for MFIE is inadequate while EFIE has good energy
conservation. EFIE also obeys energy conservation even for 40 points per
wavelength.

3.3 Impedance Boundary Condition

The impedance boundary condition is a common approximation to the two

media problem when the lower medium is lossy. Its approximation is similar

to that of the transmission line concept when the voltage is equal to the

product of the impedance and the current. In terms of wave reflection by a

lossy medium, the impedance boundary condition is

Etan = nds = mn x H (4.3.38)
where Eton is the tangential electric field and J, is the surface electric cur-
rent, and 7 = \/j1/e1 is the wave impedance of the lower medium.
The surface integral equation is, from (4.2.1)
1 * a4
Pinel?) = 30) -f dsu(t)a: VoF.F) + [ dsatrr)a- Woe) (4.3.39)
s Ss

The impedance boundary condition can be used to establish a relation be-

tween y and 2+ Vu.

For TM case, taking the cross product of both sides of (4.3.38) with the
surface normal gives

Ax Etan = My =—mnx Js (4.3.40)

where M, is the surface magnetic current. Using (4.2.19) in (4.3.40), we have

he Ve) = —mi x (Ax Hb) = mod (4.3.41)
--- PAGE 185 ---
162 4 RANDOM ROUGH SURFACE SIMULATIONS
Hence
ke
a- Vol?) = “tv (4.3.42)
cL
Then the surface integral equation (4.3.39) becomes
1 Rk
Pinel?) = =o(F) — f dsu(P)i- VglF,F) — i f dsg FF )b(F) (4.3.43)
2 Is kids
For TE case, from (4.2.12), (4.2.13), and (4.3.38),
~ 9. '
=m |—(n- Ve 4.3.44
ww =m [Ha-ve)] (43.49)
Thus the impedance boundary condition becomes
1
—h- Vil?) = —v(F) (4.3.45)
iky
which results in the integral equation
1, 7 1 in im ANITA a
Vine) = ———[h’ - VO(F’))] + —F dsla- VolFF)[A- Vd(7)]
Qiky ikiJs
+ [ dsg(F,7')[A- Val) (4.3.46)
s
When applying MoM to solve these integral equations, matrix elements in-
chiding numerical integrations can be derived using procedures described in
previous sections.
For the case of flat surface, the Fresnel reflection coefficients for TE and
TM waves for impedance boundary conditions are respectively
veg Riz — i
RBS oe 4.3.47
kis + hy ( )
Ke
Kis — A
R™ _ —? (4.3.48)
kiz +
iz + hi
The emissivities are
ere = 1— {RTP (4.3.49)
em =1-|RIMP (4.3.50)
In Section 4, we compare emissivities of rough surface computed using the
impedance boundary condition with the dual integral equation method.
--- PAGE 186 ---
84 Microwave Emission of Rough Ocean Surfaces 163
4 Microwave Emission of Rough Ocean Surfaces

Numerical simulation of passive microwave remote sensing of ocean surfaces
has a strict accuracy requirement. This is because the key output of the
simulations is the difference of brightness temperature between a rough sur-
face and a flat surface. Since the difference can be as small as 0.5 K, it
is important to be able to simulate the scattering and emission accurately.
Tn this section, we perform accurate simulations of TE and TM waves for
ocean surfaces with relative permittivity 28.9541 + 136.8430 at 19 GHz. Be-
cause the ocean permittivity is large, we use up to 80 points per free space
wavelength. To ensure accuracy, matrix equation is solved by direct inver-
sion. Conservation of energy is within 0.001 in the simulations. Numerical
results are illustrated for rough surfaces with Gaussian spectrum, bandlim-
ited ocean spectrum, and bandlimited fractal surfaces. We show convergence
with respect to the density of sampling points and to the upper limit of the
bandlimited ocean spectrum, Comparisons are also made with the results
of impedance boundary condition. Numerical results indicate that fine dis-
cretization is required for ocean surfaces with fine scale roughness.

The rough surfaces are generated as described in Section 1.4. The ocean
surfaces are generated using 240 points per wavelength. In the numerical
results, an incident angle of 50° is used, and the physical temperature is
283 K. Energy conservation check is done by using e(4;) + r(8;), where e(6;)
and r(6;) are given by (4.2.42) and (4.2.45), respectively. Table 4.4.1 presents
the emissivity for both TE and TM waves with various surface lengths. Based
on energy conservation check, a surface length of 8A is not large enough
to give the correct results. Hence, a surface length of 20A is used in all
subsequent simulations.

To demonstrate the significance of the numerical integrations taken be-
tween near field interaction, we show in Table 4.4.2 the significant improve-
ment for TM waves after near field integration was performed for the matrix
elements.

In Table 4.4.3, the simulations are performed for one realization of the
same profile with a sampling density that various from 10 to 80 points per
wavelength. It is shown that the results converge and accuracy requirement
is satisfied with 40 points per wavelength discretization for TE polarization
and 80 points per wavelength discretization for TM polarization.

In Table 4.4.4, ky is chosen to be 400, 1000, 4000, and 6000 rads/m, while
ky, is fixed at 100 rads/m. The rms heights for these four cases correspond
to kh = 0.31130, 0.32257, 0.32404, 0.32406, respectively. As kyr increases,
there are more fine scale structures on the ocean spectrum. Results show
--- PAGE 187 ---
164 4 RANDOM ROUGH SURFACE SIMULATIONS
| Polar} Surface | Emission | Energy cons. | Emissivity of | Tg(K}| ATp(rough
| length() check flat surface — flat surface)
TE 0.28914 | 0.99384 0.28728 | 81.83
_TE 0.29738 0.99974 a6 | 2.86
(Te [20 0.29695" | LobuT6 8404 za
T™ 8 0.57340 1.0006 400 |
T™ 16 0.56778 1.00084 0.55927 | 160.68 2.41
ae Loatos 0.85927
‘Table 4.4.1 Comparison of emissivities with various surface length for TE and 'TM polar-
izations. ky, = 100rads/m, kyr = 4000 rads/m, and 60points/A discretization. (~ represents
the correct result.)
| Codes with | Polar | Emissiity | Energy cons. | Emissivity of | Tg(K)| ATg(rough
| near field int. check flat surface —flat surface)
|___YES TE | 0.29695" | 1.00016 0.28728 | 84.04 2.74"
NO [TE [0.29696 [0.9997 0.28728" | 84.04, 274 |
YES TM [ 0.56823" | 1.00096 0.55927 | 160.81 2.50"
dupa | d9968 sas 056
Table 4.4.2 Comparison of emissivities with and without near field integration for TE and
TM waves. hy, = 100rads/m, kyy ~ 4000 rads/m, and 60 points/ discretization. (* represents
the correct result.)
No. of | Polar | Emissiity | Energy cons. | Emissivity of | 73(K) | ATp(rough
points/\ | check flat surface — flat surface)
10 TE | 0.30400 | 10189 | 0.28728 | 86.03 | 4.73
40 TE | 0.29710 | 1.00050 0.28728" | 84.08 2.78
0.29695 | 1.00016 0.28728 | 84.04 2.74
80 TE | 0.29686 | 0.999968 0.28728 271 |
0.56097 | 0.99511 | 0.55927, 0.48
TM | 0.56894 1.00155 1 0.55927 | 161.01 | 2.74
TM | 0.56849 1.00121 | 0.55927 | 160.88 261
0.56823 | 1.00096 0.55927 | 160.81
Table 4.4.3 Emissivity with various sampling density (# of pts/wavelength) number of
points/A. ky = LO0rads/m, and ky = 4000 rads/m.
--- PAGE 188 ---
§4 Microwave Emission of Rough Ocean Surfaces 165
Polar | ky (rads/m) | Emission | Energy cons. | Emissivity of | p(X) | AT'p (rough
pve Peg ine |
Te | 400
i006 [0.28728
Linn | 0.2872
reo | | ssm—ra| ras |
T™ | 4000 1.00096 0.55927 | 160.81 254 |
ts
Table 4.4.4 Emissivity and brightness temperature with various value of ky. ky =
100rads/m.
Polar | kr (tads/m) | Emission | Energy cons. | Emissivity of | Tg(K) | ATp (ough
Poe rein Pee Pere [ime || tm
1000 0.29403 1.0001 2.03
rE
| TE 1.0002 | __(0.28684 | 83.16 | 1.99
(TM 400 0.56286 1.0001 0.55984 0.85,
™ 1000 0.56557 1,0004 0.55984 1.62
T™ 6000 0.56935 1.0018 0.55984 | 161.13 2.69
Table 4.4.5 Emissivity and brightness temperature with various value of kz using impedance
boundary conditions. The paraineters used are the same as in Table 4.4.4.
the importance of fine scale structures on the observed brightness temper-
atures and emissivities. We also list results calculated using the impedance
boundary condition in Table 4.4.5. Comparing the results in Table 4.4.5
and Table 4.4.4, we find that good agreement between the results using the
impedance boundary condition and the dual integral equations when ky is
small, However, as ky increases, the differences between the two methods
become larger. Since a larger ky represents a finer scale structure, this in-
dicates that the impedance boundary condition is applicable only when the
radius of curvature is not much less than a wavelength.
Tables 4.4.6 and 4.4.7 show the emissivities and brightness temperatures
for different kinds of rough surfaces, using both the dual integral equations
and the impedance boundary condition. In Table 4.4.6, a Gaussian spectrum
--- PAGE 189 ---
166 4 RANDOM ROUGH SURFACE SIMULATIONS
| Method | Polur ; Emission | Energy cons. | Emissivity of | Tp() | AT p (rough
i | check | flat surface flat surface)
Dual 0.42639 | 1.00067 0.28728
_ 0.63463 1.0084 0.55927 179.60
Impedance 0.40160 1.0007 | _0.28684
| Tmpedance 0.63428 Lon | 0.5584 [70.50 [21.07 |
Table 4.4.6 Emissivity and brightness temperature for Gaussian rough surface with rms
height h = 0.2. and correlation length | = 0.2 A.
| Method | Polar | Emission | Energy cons. | Emissivity of | Tp() | ATp (rough
| check flat surface ~ flat surface)
_Dual_| Te | 0.32536 | o.s9074 [0.28728 | 9208 | 10.78 |
Dual TM | 0.60870 1.0147 0.55927 172.26 13.99
0.29923 1.0010 0.28684 3.51
0.60536 1.0149 0.55984 | 171.32 12.88
Table 4.4.7 Emissivity and brightness temperature for fractal surface. Ko = ky, = 100,
and KgbN/-1 = ky = 4000.
with rms height h = 0.24 and correlation length | = 0.2, is used the simula-
tions. In Table 4.4.7, bandlimited fractal surfaces are used with the number
of tones Ny = 100 and fractal dimension s = 1.5. The equivalent rms height,
h = 0.051572A is the same as chosen in the ocean spectrum with bandlimits
ky = 100 rads/m and ky = 4000 rads/m.
5 Waves Scattering from Real-Life Rough Surface Profiles
5.1 Introduction
In modeling random rough surface scattering, the rough surface is usually
modeled as a random process f(z). It is characterized by a height probability
density function (PDF) and its surface power spectral density. In real life,
one is often faced with a problem of estimating the average surface spectrum
and PDF from a limited amount of surface profile data. A common proce-
dure is to use a surface spectrum with a power law or a correlation function
with an exponential function or a Gaussian correlation function. Thus, a
best-fit spectrum has been used in scattering models. However, scattering
solutions based on an average or a best-fit surface spectrum has not been
rigorously verified. Also, in fitting a correlation function or a spectrum, it
--- PAGE 190 ---
§5.2 Rough Surface Generated by ‘Three Methods 167
is unclear which portion of the correlation function or spectrum in the spa-
tial and spectral domain, respectively, should be fitted to produce the best
wave scattering results. Thus, depending on how the correlation function is
fitted, several correlation lengths can be obtained. This complicates the mat-
ter because scattering results are strongly dependent on correlation lengths.
Furthermore, a particular fit may produce a good scattering agreement at
one frequency and incident angle, but not at other frequencies and incident
angles.

Tn this section, we illustrate rough surface simulations on real life mea-
sured profiles. Three methods are used. In the first method, we use a set of
field-measured profiles of a natural surface to calculate the scattering directly
for each profile. This will be called the correct result. In the second method,
an average surface spectrum is found from the same ficld-measured profiles
of the first method. Because of the limited number of real-life profiles that
are measured, the average spectrum still oscillates. Based on this average
spectrum that still contains oscillations, a large number of realizations of
synthetic surfaces are numerically generated by the spectral method. Scat-
tering is calculated for these synthetic profiles. Then, an average scattering
cross section of the generated profiles is found. In the third method, which is
a commonly adopted procedure, the average surface spectrum found in the
second method is fitted with a power-law function. From the best-fit spec-
trum, many independent realizations of surfaces are numerically generated.
Then, the average scattering cross section is calculated for these realizations.
The third method is the most common because an analytic expression is ob-
tained for the power spectrum. Based on this analytic expression, analytical
scattering results and numerical simulated scattering results can be caleu-
lated. However, we shall show in this section that this method can give poor
results.

5.2 Rough Surface Generated by Three Methods

The surfaces generated by methods 1-3 shall be labeled S$), $2, and §3,
respectively. The profiles S| are the actual measured profiles.

Method 1

In Method 1 we use a set of measured profiles of soil, snow, and rock sur-
faces. The measured profiles are called S. Based on the measured profile
z= fi(a,), where t denotes true profiles, we compute the average bistatic
scattering coefficient. From Table 4.5.1 the number of profiles used for rock,
snow, and soil are 20, 35, and 14. respectively. We denote the number of
--- PAGE 191 ---
168 4 RANDOM ROUGH SURFACE SIMULATIONS
f Rock | Suow | Soil
Number of samples (Vz) | 20 35 14
Surface length (A) 125 | 3413 | 96
Number of points N 300 512 96
rms height(A) 04 0.156 0.1
Table 4.5.1 Real-life surface profile data.
measured samples by N;. Note that because the profiles are actually mea-
sured in the field, there can only be a moderate number of profilés for cach
case. Surface length, rms height, and total number of points are also listed
in Table 4.5.1. The sampling rate is at least 10 points per wavelength.
Methods 2 and 3 of the scattering study use numerically generated sur-
face profiles based on the calculated average spectrum.
Synthetic Surfaces
In Methods 2 and 3, realizations of height profiles are generated from spectral
density W(K,) with K, = 27n/L. Methods 2 and 3 use different W(K;).
Using W(K,), we generate a realization of F(K,) by the method described
in Section 1.4,
loi. . N
—([N(0,1)+iN(0,1)] 1 40,—
F(K,) = V2nLW(K,) 4 V2 Ry 5.4)
N(0,1) n=05
where N(0, 1) is a sequence of normally distributed random numbers in [0, 1}
with zero mean and unity standard deviation and N is the total number of
sampling points.. From F(K;,), the rough surface profile is given by
1 Xe
f@= 7 Yo F(Ka)expiKnn) (45.2)
n=—N/2
Method 2: $2 Surfaces
We compute the spectral density from the true measured profiles f;(a,) by
taking averages of the N; profiles as follows:
2
N-1 |
Sp L 1
W(Kn) = 555 (hs SY fulen)g(an) exp(—j2an/L)
x a)
pt wel, Xe e
=—— = Q —j2: l, 4.5.3
WOM 2 li Dy fezndalan) exp(—J2nn/T | (4.5.3)
--- PAGE 192 ---
§5.3 Numerical Results of the Three Methods 169
where g({z,) is a space-domain window function, the angular brackets de-
note the ensemble average, and U is a normalization constant. We then set
W(K,,) = W(K,) in Method 2. Because of the limited number of samples
in the true profiles, there are still oscillations in W(K). We then use this
oscillatory W(A) = W(K) to generate many profiles to compute the scat-
tering results. However, in spite of the presence of oscillations in W(i,)
we find that the scattering results computed with this method are in good
agreement with Mcthod 1.
Method 3: 53 Surfaces
This is a common procedure. The averaged power spectrum W(K) found in
(4.5.3) is fitted with a function W,(A), A power-law spectrum is frequently
used. This can be a controversial procedure. For example, different corre-
Jation lengths can be obtained, depending on the fitting procedure. In the
following we use a weighted least-squares method to fit a calculated spectrum
of (4.5.3) with a power-law spectrum
W,(K) = C|K|-* (4.5.4)

where C and a are parameters to be determined. They are tabulated in
Table 4.5.2. When the power-law spectrum is plotted on a log-log scale, we
have a linear function given by

log(W(K)) = —alog(|K'|) + log(C) (4.5.5)
Then we let W(4) = W,(K) in (4.5.3) to gencrate independent realizations
of synthetic surfaces in Method 3.
5.3 Numerical Results of the Three Methods
In Fig. 4.5.1 a real-life rock surface profile ($1), a synthetically generated
rock surface profile based on the calculated average spectrum (S2), and a
surface based on the best-fit spectrum ($3) are illustrated. In Figs. 4.5.2 and
4.5.3, we illustrate Sj, So, and S3 for the cases of snow and soil surfaces,
respectively. The profiles are shifted vertically for comparison. It can be
observed that none of the S3 surfaces have the appearance of the measured
profile. In fact, the $3 surface of snow has a closer resemblance to a measured
soil profile than to the snow profile. The S2 surfaces of snow and soil have the
best. resemblance to the real-life profiles. For all three surfaces, $2 surfaces
resemble the real-life surface profiles better than the $3 surface profiles. Thus,
one can foresee (and it will be demonstrated) that the scattering from the
S» surfaces will have better agreement. with the correct scattering results of
--- PAGE 193 ---
170 4 RANDOM ROUGH SURFACE SIMULATIONS
ar|
measured
2] eee
08
5
Su
5 os
g 06
= 07
= a9
a
z
2 “4
S12
& sa .
60 58D 45° 40S
Horizontal Position-X (wavelength)
Figure 4.5.1 Comparison of three profiles of rock surfaces: real-life $1 (top), synthetic
surface based on the calculated average spectrum S$» (center), synthetic surface based on the
power-law spectrum $3 (bottom).
os;
| measured
oa LINN
= oh
Bol
Ed
$ 00
za
2
3
2 os
2
gt
Sd
"4g 198 438 Soa 92 190 408 428 424 TAR ABO
Horizontal Position-X (wavelength)
Figure 4.5.2 Comparison of three profiles of snow surfaces: real-life $1 (top), $2 (center),
S3 (bottom),
S; surfaces. In Table 4.5.2, the rms heights of three type of surfaces $1, So,
and $3 for rock, snow, and soil are compared.

In Pig. 4.5.4 the power spectra of Sy and $3 surfaces for rock, soil, and
snow are illustrated on a log-log plot. Note that the power spectra of S$;
and $2 are the same. We use a weighted least-squares best fit to find the
parameters C’ and a in (4.5.5). It should be noted that in fitting the calcu-
--- PAGE 194 ---
§5.3 Numerical Results of the Three Methods 171
o7
os measured
£
S
& oa
$
§
=o
z
Eo
2
2 03
eo
05 \ — a -
2 4 r) 7 2 3
Horizontal Position-x (wavelength)
Figure 4.5.3 Comparison of three profiles of soil surfaces: real-life $1 (top), Sz (center).
53 (bottom).
Rocks (20) | Snow (35) | Soil (14)
Si(mms) | 0.4 0.156 0.10
Setrms) | 0.3 | 0.143 0.106
S3(rms) | 0.55 0.145 | 9.102
; & 2.25 18 | 25 j
c | lo-4 197288 wis |
Table 4.5.2 Comparisons of rms heights.
lated power spectrum with a power law, we have disregarded regions that do
not have a linear behavior on a log-log plot. In Table 4.5.2, we list the pa-
rameters C and « of the power law. Because the power-law function blows
up for K = 0, we have assigned W(0) = 0 in the surface generation. An
alternative approach is to taper the power-law spectrum by an exponential
function for small values of K,. However, we find that the alternative ap-
proach of an exponential tapering did not produce a noticeable difference in
the surface profile or the scattering result. It can be seen from Fig. 4.5.4 that
the power law gives a good fit for the cases of rock and soil surface spectra.
For a rock surface, a power-law fit overestimates the calculated spectrum for
spatial frequencies lower than 3/A. Therefore, a rock surface generated with
the fitted spectrum of Fig. 4.5.4a generates surfaces with larger rms surface
heights. From Table 4.5.2, we see that the rms height difference between the
real-life surfaces and those generated with a power-law spectrum is 38%. For
a soil-surface spectrum, the agrecinent between the calculated spectrum and
the best-fit spectrum is good over a wider range than the rock-surface case.
--- PAGE 195 ---
172 4 RANDOM ROUGH SURFACE SIMULATIONS
— — coatetated | “t — ccaeuates
orn TZ Benen a . ==~ BestFit
= 8s, zw = -
Br 5 i
Ete =. ss,
10 a
a, A Sa rc |
(1/wavelength) (1/wavelengtn)
(a) b)
02 . --
=~ — calculated
> noo BestFit |
zoo
Hi >
ae van
En >»
Foti S
pig Pee iG 5
(wavelength)
(©)
Figure 4.5.4 Comparison of calculated average spectrum and a best-fit spectrum for (a) rock
(a = 25, C = 1074), (b) snow (a = 1.8, C = 107785), and (c) soil (a = 2.25, C =
10 74),
[| Rocks (dB) | Snow (dB) | Soil (dB)
S, | -9.6 16.0 13.1
$2) -91 -14.9 -14.8
$3 | -4.0 ~19.8 | -19.4
Table 4.5.3 Backscattering level comparison —45°.
This is further evident in the rms height comparison, where the agreement
is within 1%.

Next, bistatic scattering cross sections from the surfaces of Figs. 4.5.1
4.5.3 are presented in Figs. 4.5.5a~4.5.5c, respectively. The incident angle
is 45° for all simulations. Since the study is a profile testing, all scattering
simulations are based on perfect electric conductors. In Table 4.5.3, we list
the backscattering (9, = —0;) levels in decibel scale; the number of surface
realizations is found in Table 4.5.2. All simulations satisfy the power con-
--- PAGE 196 ---
§5.3 Numerical Results of the Three Methods 173
ge. Bw»
}: eye i. N
4 2
i \ ds
2 —— Reattite i i
ie et Loe et
i « :
we Boatiorng Angie (degree) so $8 oattering Angie depres
@

g

a

£0 :

8

[- =—

a

oan pel

Figure 4.5.5 Comparison of bistatic scattering coefficient from three types of surfaces:
(a) rock surfaces of Fig. 4.5.1, (b) snow surfaces of Fig. 4.5.2, and (c) soil surfaces of Fig. 4.5.3.
servation check to less than 1%. From Figs. 4.5.5a 4.5.5¢ and Table 4.5.3, it
is seen that the backscattering from the calculated spectra (S2 surfaces) are
within 1.1 dB of real-life surfaces (9; ) for all cases. Note that because of the
limited number of real-life profiles, the calculated power spectrum W(K;)
from S| still oscillates (Fig. 4.5.4). This W(K;,) is also used to generate Sz
profiles. Nevertheless, the backscattering from $2 surfaces all converge to
within 1.1 dB of the correct results.

From Table 4.5.3, we can sce that the backscattering level of the power-
law spectrum that are used to fit the measured spectrum and the real-life
surfaces are not in good agreement. For rocks (Fig. 4.5.5a) the best-fit spec-
trum model scattering result is 5.6 dB above that of the real-life surface. For
snow surfaces, the scattering solutions between the real-life and best-fit spec-
tra have a 4 dB difference. The power-law spectrum of soil provides a better
fit of the spectrum than snow or rocks over a wider range of spatial frequen-
cies. Based on this observation, it would seem that the soil-surface case will
likely give the best scattering agreement. However, it gave a 4.3-dB differ-
ence in backscattering. If we take the point of view of the first-order small
perturbation model, the average backscattering is proportional to the spatial
frequency component 2ksin@m. of the spectral density, ie., W(2k sin Oinc).
Thus SPM says that only the spectral component 2k sin in. in the spectrum
matters in backscattering. Mor the cases considered, 2k sin @jy< is approxi-
--- PAGE 197 ---
174 4 RANDOM ROUGH SURFACE SIMULATIONS
mately equal to 9/X for the calculation. In fitting the spectrum, we paid
particular attention to matching up the spectrum at 2k sin @;,-. At this spa-
tial frequency the calculated power spectrum and the power-law best-fit spec-
trum are within 1 dB for rocks (Fig. 4.5.4a) and soil surfaces (Fig. 4.5.4c).
However, although the spectral are matched at 2k sin @ine, the differences in
the backscattering levels were 5.6 and 4.3 dB, respectively. For a snow surface
the calculated power spectrum and the power-law best-fit spectrum have a.
6-dB difference (Fig. 4.5.4), but they have a 4.0-dB difference in backscat-
tering. These observations suggest that even though the power spectrum can
be fitted to have good agreement at W(2ksin Ojnc), the backscattering levels
can be significantly different. It is also interesting that $; and S2 backscat-
tering are larger than $3 backscattering for snow and soil while the opposite
is true for rock surfaces.

Tn the past, Methods 1 and 2 are not adopted because (i) there are only
a limited number of surface profiles and (ii) the calculated average surface
spectrum based on the limited number of samples still have oscillations.
However, we show that even with this limited number of profiles, Methods 1
and 2 give results that are within 1.1 dB of each other. On the other hand,
the commonly adopted method of fitting a power spectrum is a controversial
procedure because it is unclear which part of the spectrum is to be fitted.
Furthermore, the generated surface profiles $3 produce backscattering results
of up to a 6-dB difference from Method 1. Results from this section indicate
that further studies of surface profiles and rough surface characterization are
needed.
--- PAGE 198 ---
REFERENCES 175
REFERENCES AND ADDITIONAL READINGS

Agnon, Y. and M. Stiassnie (1991), Remote sensing of the roughness of a fractal sea surface,
J. Geophys. Res., 96(C7), 12773-12779.

Austin, T. R., A. W. England, and G. H. Wakefield (1994), Special problems in the estimation
of power-law spectra as applied to topographical modeling, IEEE Trans. Geosci. Remote
Sens., 32, 928 939.

Axline, R. M. and A. K. Fung (1978), Numerical computation of scattering from a perfectly
conducting random surface, IEEE Trans. Antennas Propagat., 26(3). 482 488.

Berizzi, F., E. D, Dalle Mese, and G, Pinelli (1999). One dimensional fractal model of the
sea surface, JEE Proc. -Redar, Sonar, and Navig., 146, 55-64.

Brown, $. R. and C. H. Scholz (1985), Broad bandwidth study of the topography of natural
rock surfaces, J. Geophys. Res., 90(B14), 12575-12582.

Chan, C. H., 8. H. Lou, L. Tsang, and J. A. Kong (1991), Electromagnetic scattering of
waves by random rough surface: a finite-difference time-domain approach, Microwave
Opt. Technol. Letl., 4, 355-359.

Chen, J., T. K. L. Lo, H. Leung. and J. Litva (1996), The use of fractals for modeling
EM waves scattering from rough sea surface, IEEE Trans. Geosci. Remote Sens., 34,
966-972.

Chen, M. F. and A. K. Fung (1988), A numerical study of the regions of validity of the
Kirchhoff and small-perturbation rough surface scattering models, Radio Sci., 23, 163
170.

Devayya, R. and D. J. Wingham (1992), The numerical calculation of rough surface scattering
by the conjugate graclient method, JEEE Trans. Geosci. Remote Sens., 30(3), 645. 648.

Franceschetti, G., A. Iodice, M. Migliaccio, and D, Riccio (1999), Scattering from natural
rough surfaces modeled by fractional browning motion two-dimensional process, IEEE
Trans. Antennas Propagat., 47(9), 1405 1415,

Franceschetti, G., A. Iodice, and D, Riccio (2000), Scattering from diclectric random fractal
surfaces via method of moments, IEEE Trans. Geosci. Remote Sens., 38(4), 1644 1655.

Fung, A. K. and M. F. Chen (1985), Numerical simulation of scattering from simple and
composite random surfaces, J. Opt. Soc. Am. A, 2, 2274-2284.

Garcia, N. and 1. Stoll (1984), Monte Carlo calculation for electromagnetic-wave scattering
from random rough surfaces, Phys. Rev. Lett., 52, 1798-1801.

Irisov, V. G. (2000). Azimuthal variations of the microwave radiation from a slightly non-
Gaussian sea surface. Radio Sci., 35(1), 65-82.

Ishimaru, A. (1978), Wave Propagation and Scattering in Random Media, 1 and 2, Academic
Press, New York.

Jaggard, D. L. (1990), On fractal electromagnetics, Recent Advances in Blectromagnetic The-
ory, H. N. Kritios and D. L. Jaggard, Eds., Springer-Verlag, Berlin, Germany, 183-223.

Jaggard, D. L. and X. Sum (1990), Scattering from fractally corrugated surfaces, J. Opt. Soc.
Am. A, 7, 1131-1139.

Johnson, J. 'T., R. ‘I. Shin, J. A. Kong, and L. Tsang (1999), A numerical study of ocean
polarimetric thermal emission, JEEE Trans. Geosci. Remote Sens., 37(1), 8-20.

Lou, $. H. (1991), Application of numerical methods to Monte Carlo simulations of scattering
of waves by random rough surfaces. University of Washington, Seattle.
--- PAGE 199 ---
176 4 RANDOM ROUGH SURFACE SIMULATIONS

Lou, $. H., L. Tsang, and C. H. Chan (1991), Application of the finite element method to
Monte Carlo sitmulations of scattering of waves by random rough surface: penetrable
case, Waves in Random Media, 1, 287-307.

Lou, $. H., L. Tsang, C. H. Chan, and A. Ishimaru (1991), Application of the finite element
method to Monte Carlo simulations of scattering of waves by random rough surface with
the periodic boundary conditions, J. Electromag. Waves and Appl., 5, 835-855.

Mandelbrot, B. B. (1983), The Fractal Geometry of Nature, W. H. Freeman & Co., New
York.

Maradudin, A. A., E. R. Mendez, and T. Michel (1990), Backscattering effects in the elastic
scatteting of p-polarization light from a large amplitude random grating, Scattering in
Volumes and Surfaces, M. Nieto-Vesperians and J. C. Dainty, Eds., Elsevier Science
Publishers, North-Holland.

Maradudin, A. A., T. Michel, A. R. McGum, and E. R. Mendez (1990), Enhanced backscat-
tering of light from a random grating, Ann, Phys., 203(2), 255-307.

Maystre, D., M. Saillard, and J. Ingers (1991), Scattering by one- or two-dimensional ran-
domly rough surfaces, Waves in Random Media, 1, 143-155.

McGurn, A. R. and A. A, Maradudin (1993), Weak transverse Jocalization of the light scat-
tered incoherently from a one-dimensional random metal surfaces, J. Optical Soc. Am.
B, 10(3), 539-545.

Michel, T. R. and K. A. O’Donnell (1992), Angular correlation functions of amplitudes scat
tered from a one-dimensional, perfectly conducting rough surface, J. Opt. Soc. Am. A,
9(8), 1374-1384.

Nieto-Vesperinas, M. and J. M. Soto-Crespo (1987), Monte-Carlo simulations for scattering
of electromagnetic waves from perfectly conducting random rough surfaces, Optics Lett.,
12, 979-981.

Papoulis, A. (1984), Probability, Random Variables, and Stochastic Processes, McGraw Hill,
New York.

Rino, C. L., T. L. Crystal, A. K. Koide, H. D. Ngo, and H. Guthart (1991), Numerical
simulations of backscatterer from linear and nonlinear ocean surface realizations, Radio
Sci., 26, 51-71.

Thorsos, E. I. (1988), The validity of the Kirchhoff approximation for rough surface scattering
using @ Ganssian roughness spectrum, J. Acous. Soc. Am., 83(1), 78-92.

Thorsos, E. I. and S. L. Broschat (1995), An investigation of the small slope approximation
for scattering from rough surfaces. Part I. Theory, J. Acous. Soc. Am., 97 (4). 2082-2093.

‘Thorsos, E. I. and D. R. Jackson (1989), The validity of the perturbation approximation
for rough surface scattering using a Gaussian roughness spectrum, J. Acous. Soc. Am.,
86(1), 261-272.

‘Thorsos, E. I. and D. R. Jackson (1991), Studies of scattering theory using numerical meth-
ods, Waves in Random Media, 1(3), $165-S190.

Toporkov, J. V., R. S. Awadallah, and G. S. Brown (1999), Issues related to the use of a
Gaussian-like incident field for low-grazing-angle scattering, J. Opt. Soc. Am. A, 16,
176-187.

West, J. C. (2000), Integral equation formulation for iterative calculation of scattering from
lossy rough surfaces, IEEE Trans. Geosci, Remote Sens., 38(4), 1609-1615.

Yueh, §. H. (1997), Modeling of wind direction signal in polarimetric sea surface brightness
temperatnres, IBEE Trans, Geosci. Remote Sens., 35(6), 1400-1418.
--- PAGE 200 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc.
ISBNs; 0-471-38800-9 (Hardback); 0-47 1-22430-8 (Electronic)

> 本章研究随机粗糙面的数值模拟。粗糙面的统计特性由高度PDF和ACF描述。

> 通过FFT高效生成大尺寸粗糙面样本，表面长度应足够大以包含多个相关长度。

> 本节描述具有指定功率谱或ACF的随机粗糙面生成方法。

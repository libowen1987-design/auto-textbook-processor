# Tsang《Scattering of EM Waves》Chapter 5

> 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 5
FAST COMPUTATIONAL METHODS FOR SOLVING
ROUGH SURFACE SCATTERING PROBLEMS
1 Banded Matrix Canonical Grid Method for
Two-Dimensional Scattering for PEC Case 179
1.1 Introduction 179
1.2 Formulation and Computational Procedure 180
1.3 Product of a Weak Matrix and a Surface Unknown Column
Vector 187
1.4 Convergence and Neighborhood Distance 188
1.5 Results of Composite Surfaces and Grazing Angle Problems 189
2 Physics-Based Two-Grid Method for Lossy Dielectric
Surfaces 196
2.1 Introduction 196
2.2 Formulation and Single-Grid Implementation 198
2.3. Physics-Based Two-Grid Method Combined with Banded
Matrix Iterative Approach/Canonical Grid Method 200
24 Bistatic Scattering Coefficient and Emissivity 203
3 Steepest Descent Fast Multipole Method. 212
3.1 Steepest Descent Path for Green’s Function 213
3.2 Multi-Level Impedance Matrix Decomposition and Grouping 216
3.3. Multi-Level Discretization of Angles and Interpolation 222
3.4. Steepest Descent Expression of Multi-Level Impedance Matrix
Elements 226
3.5 SDFMM Algorithm 235
3.6 Numerical Results 242
177 -
--- PAGE 201 ---
178 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
4 Method of Ordered Multiple Interactions (MOMI) 242
4.1 Matrix Equations Based on MFIE for TE and TM Waves

for PEC 242
4.2 Iterative Approach 245
4.3 Numerical Results 247
5 Physics-Based Two-Grid Method Combined with

the Multilevel Fast Multipole Method 249
5.1 Single Grid and PBTG 249
5.2 Computational Complexity of the Combined Algorithm of the

PBTG with the MLFMM 252
5.3. Gaussian Rough Surfaces and CPU Comparison 254
5.4 Non-Gaussian Surfaces 257

References and Additional Readings 263
--- PAGE 202 ---
§1 Banded Matrix Canonical Grid Method for 2-D Scattering 179
In this chapter we study the fast computational methods that can be
used to numerically simulate random rough surface scattering. Many meth-
ods have been used for rough surface simulations. These include the finite
difference time domain (FDTD) [Chan ct al. 1991] method, finite element
method (FEM) [Lou et al. 1991], wavelet. method [Lin et al. 1999], multi-
grid method [Donohue et al. 1998], method of multiple interactions (MOM1)
[Kapp and Brown, 1996], recursive T-matrix [Michclssen et al. 1996], and
the fast multipole method (FMM) [Jandhyala et al. 1998a,b]. In this book,
we choose to illustrate the sparse matrix canonical grid (SMCG) and the
physics-based two-grid (PBTG) method in details. These two methods have
been applied extensively to 3-D simulations for dielectric surfaces and lossy
dielectric surfaces which are practical problems in active and passive mi-
crowaye remote sensing. In this chapter, we illustrate the SMCG and PBTG
for 2-D problems. The 3-D cases will be discussed in Chapter 6. We also
discuss the steepest descent fast multipole method (SDFMM), MOMI, and
the combination of PBTG and SDFMM. Numcrical results presented in this
chapter are limited to cases when the results were first published using com-
puter resources available at the time.
1 Banded Matrix Canonical Grid Method for

Two-Dimensional Scattering for PEC Case
1.1 Introduction
We have illustrated the surface integral equation method. The integral equa-
tion is converted to a matrix equation by the method of moments, and the
resulting equation is solved with a full matrix inversion. Surface lengths of
the order of 40 to 100 wavelengths have been used in Chapter 4. Many prac-
tical problems such as near-grazing incidence or rough surfaces with large
correlation lengths are considered large-scale rough surface problems. For
such large-scale rough surface problems, a much larger surface length is re-
quired and a more efficient method is needed.

A banded matrix iterative approach (BMIA) has been applied to rough
surface scattering. In the BMIA, the original full matrix equation is decom-
posed into (a) a banded matrix which represents strong interaction and (b)
the remainder of the full matrix which represents the weak interaction part.
An iterative approach is then adopted. The size of the neighborhood varies
depending on the rough surface statistics and the incident angle. It is always
much less than the required surface length and is also much less than the
tapering parameter g.
--- PAGE 203 ---
180 5 FAST METHODS FOR ROUGH SURFACE SCATTERING

Improvements to the BMIA method are further made by using the flat
surface as a canonical grid (CAG or CG). We call the method BMIA/CAG.
For two points outside the neighborhood, the Green’s function connecting
the two points on the rough surface is close to that of a flat surface. Thus in
this case, the flat surface provides the CAG for distances larger than neigh-
borhood distance. A Taylor expansion is carried out for the Green's function
outside the neighborhood distance. The impedance matrix from the Green's
function is decomposed into a sum of the banded matrix and the Taylor
expanded flat surface impedance matrix that replaces the weak matrix from
the BMIA method. The advantage of the canonical grid (flat surface in this
case) is that the product of the ‘Taylor expanded flat surface matrix and the
surface current column vector can be computed by the fast Fourier trans-
form (FFT). The BMIA/CAG is much faster than the customary full matrix
inversion. When the method was first. used in 1994 (Tsang et. al. 1994, 1995],
we studied rough surfaces with lengths up to 2500 wavelengths with 25,000
surface unknowns. The method was also applied to the case of near grazing
incidence. We also make comparisons between using a large surface length
and the method of using a periodic boundary condition which emulates a
large surface length.

Other methods known as the adaptive integral method [Belszynski et
al. 1994; Anastassiu et al. 1998] and the pre-corrected FFT method [Phillips
and White, 1997] are similar in concept to the BMIA/CAG.

1.2. Formulation and Computational Procedure
Consider a tapered plane wave Winc(x, 2) impinging upon a one-dimensional
(1-D) rough surface with a random height profile z = f(x).

Wine(F) = elk FL+w(F)] -—(@t2 tan Bone)? /g? (5.1.1)
where w and g are as given in Chapter 4. Applying the boundary condition
that (7) = 0 on the rough surface, the Fredholm integral equation of the
first kind can be formed. For a point 7 = 2% + f(x) on the rough surface,
the integral equation for the Dirichlet boundary condition is

oc
0= ine(?) — | de! G(F, Fula’) (5.1.2)
00
where
On”
ula!) = J+ (ae) awe 2ee)
1
is the surface unknown to be calculated. Let xy = |x — 2’| be the separation
distance between the field point and the source point on the rough surface.
--- PAGE 204 ---
§1.2 Formulation and Computational Procedure 181
We select a neighborhood distance within which there is a strong interaction.
In numerical simulations, rg is an adjustable parameter and rg > h. Then,
(5.1.2) can be put into the form
Fe dy 2 yy Flae’))2) ula .
[ae (b+ 019?) wey (r4~ 20)
=00
¥o te pl) 2 ry\2 Yur
+ [dat HS? (bye FO) = 1) we 0 (ea ra
= Vine(@, [(x)) = b(x) (5.1.3)
with U as the Heaviside step function. Thus the first term in (5.1.3) repre-
sents strong interaction, and the second term represents weak interaction.
The strong interaction term corresponds to a banded matrix (a sparse matrix
for the 3-D scattering case), and the weak interaction term is a dense matrix.
The weak interaction matrix is the computationally intensive part because
of the large number of pairs of points that are not within the neighborhood
of cach other. We then rewrite the weak interaction matrix by using Taylor
series expansion to translate it to a flat surface which acts as the canonical
grid. Since in the weak interaction term, we have zg > rq > h, we ob-
tain xq > |f(z) — f(2’)|. Thus a Taylor expansion can be made on Green’s
function. Let zg = |f(x) — f(2’)|-
From Chapter 4, the impedance matrix is Zn = Amn, Where
wet ky ()
Amn = [ as da’ qtlo (kV Gn = 2!)? + (f (am) — F@)?) (5.1.4)
Sty SE
N ;
Ye Zrnnttn = Om (5.1.5)
n=l
Decompose into strong part and weak part.
N N
Ye Zan tO Zn = bn (5.1.6)
n=l nek
where
Amn for |m—n| < by
Zieh ~ {3 for i - A > by (5.1.7)
. 0 for |m—n| < bw
Zin = {Shon for hn - " 5 Bo (5.18)
where by = ra/Aa. Without loss of generality, we can make by, an integer,
eg., if rg = 2A, Ar = X/10, then by = 20. Since 2) is in the non-near
--- PAGE 205 ---
182 5 PAST METHODS FOR ROUGH SURFACE SCATTERING
field, we can calculate the matrix elements without numerical integration.
0 for im —n| < by
Zhe) = 5 4 pa) ( 3 B) Ag f
SHS? (kV Gin = @n)? FFG m) — Fl@n))P) Ae for [ma — n| > bu
(5.1.9)
Let
Zhe) = Zhi + (Zhe) ~ Zh) (5.1.10)
0 for |m —n| < by
(w)(0) 2G 5
Br =) AH) («/3) Ar for|m—nj>by bt)
where
gq = \n—nldr (5.1.12)
Note that ZV) is translational invariant.
The matrix equation is
Zu =5 (5.1.13)
so that
[Z° +2) u=b (5.1.14)
We rewrite (5.1.14) as
(5s)  =(w)(0 — (se) swy(o
[2° +z" ‘ w=b- (2 3" ’) a (5.1.15)
Note that the sparse matrix and the flat surface impedance matrix are kept
on the left-hand side of (5.1.15). We discuss three ways of iteration listed
below as (A), (B), and (C).
(A) Iteration Based on Strong Matrix and Zeroth Order Weak Matrix
The zeroth order solution @ obeys the equation
= =(w)(0) -
[2° 47" }e =5 (5.1.16)
sO -
ZG =5 (5.1.17)
(0) .
where the zeroth order impedance matrix Z — is defined as
sO =) swe
2° =79 ZO 6.1.18)
--- PAGE 206 ---
§1.2 Formulation and Computational Procedure 183
. . 5) rN,
We can apply the conjugate gradient method to solve Z 7) = b, Note that
ls) . . .
Z isa banded matrix. It only has values near the diagonal. The product of
=
matrix and column vector Z°'77 requires O(Nb,) iterations, The product of
Zlwroy" . .
matrix and column vector 2 requires O(N logs N) iterations. Thus
in implementing conjugate gradient method, the number of operations is
O(Nbw) + O(N logy N) per iteration. Using (5.1.15), higher order solutions
can be obtained.
The nth order solution 7) is given by
a)
ZO (5.1.19)
where the updating of the right hand side is
a =5- (2° 7 7) 7) (6.1.20)
Tn (5.1.19) and (5.1.20), n > 1. We then rewrite the weak interaction matrix
by using Taylor scrics expansion to translate to a flat surface which acts
as the canonical grid. Let. Ny be the number of terms in the Taylor series
expansion. Let zy = |f(x) — f(2")|. Define
sw) S(w)(0}
Um = {(2 Ze jal (5.1.21)
m
Then
Mi i
a) 5 a
Yn = > F Hj” (4 [a2 + 4) ~ 545 ra) Un
N Nr 22)!
= SY alee) (4) Un (5.1.22)
n=l [=I va
where a;(x,4) represents the [th order term in Taylor series expansion and
tq = |m—nlAr (5.1.23)
24 = f (4m) — f(@n) (5.1.24)
Then
j Nr 2y!
1 z;
oH ) (yi + 4) = YS ai(ea) (3) (5.1.25)
n=l “d
For the first three terms,
. ke,
ay (ta) = GHP (ea (5.1.26)
--- PAGE 207 ---
184 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
eee i ke
aya) = ~ ft HS? (bora) + St (kena) (5.1.27)
ikak ay, ira ay i kia (1)
x(a) =~ gpg Ho (era) + G—Gge Ma (hea) — GGA (hr)
(5.1.28)
If we retain three terms in the Taylor expansion (Nr = 3),
N
un = S> (280) — 26) un
=
N 2 N oA N of
= > a1 (t4)=$ tin +) a2(@4) btn + YS a3(a) Sun (5.1.29)
n=l 4 n=l wa n=1 Tq
_ aes alae) : X ai(va) .
= (f(am)) > Bin 2f(%m) ys aT (2n)un
n=)“ d n=1 d
X ai(ea)
+ (Fen))Ptn
n= d
ae alee) ’ Ws a2(ta) 4g
+ Fem) tin = Fem) GE Hen )ten
n=1 “da n=l “a
. 2d a2(za) 2 N a2(2a) 3
+ (Fm)? YP ABE Sn)? ttn = AL me) Yo Fen) Pein
n=1 d n=1 d
Nay (ca)
+30 SS" (fen) yun
n=l Td
6 Os 43(4) 5 o> a3(t4)
+ (F(@m))° YO ae un ~ 6(L(2m)) > aE LEn)un
n=1 “da n=] d
Na: (xa)
+ 15(S (em) SEE (f(en))?tn
n=1 a
S a3(4)
~ 20(F(2m))? YEAS @n)) tn
n=1 a
2 “ a3 (xa) 4, . x a3 (aa) 5
+ 15(S (0m) Yo SE (F(tn)) hn = 6m) Yo FEEL On)?
n=1 a n=1 d
--- PAGE 208 ---
§1.2 Formulation and Computational Procedure 185
Ss as(aa)
+ SEU en))Puin (5.1.30)
r
n=l “d
We make use of FFT in the calculation of ym in (5.1.30). For example, for
the second term in (5.1.30), —2(f(am)) DX, 2F2 f(ep)un, we calculate in
a
the following manner:
(1) preanultiply w, by flan) to get f(en)un = wn
N :
(2) calculate 3° BF) ang by FET
nat “a
(3) post-multiply by —2f (an)
In the BMIA/CAG method, the Z” is decomposed into a sum repre-
sented by the Taylor series expansion. Thus
M
=(w =(w}
2 27 (5.1.31)
m=0
The m = 0 term corresponds to that of a flat surface. The form of ra is
such that it consists of terms that are products of a diagonal matrix Ty, a
translationally invariant matrix Zy, and a diagonal matrix T.:

T,ZaTs (5.1.32)
where T, is a function of the coordinates 2’ of the scattering source, while
T, is a function of the coordinates x of the field.

(B) Iteration Based on Updating the Right-Hand Side
Let X° ana Xx” represent the zeroth-order solution and the nth-order
solution, respectively. They obey the equations
so) =
ZX -G (5.1.33)
ZK OM (5.1.34)
where o represents the updated right-hand side with
Go =G
=) oA tu)
O” =O-B"X" =6- OZ x” (5.1.35)
m=0
--- PAGE 209 ---
186 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
- « . . 5). - .
Note that for this case of iteration, only Z ~ is kept in the left-hand side of
(5.1.34).
A residual RB” can be defined as follows such that its norm provides
the stopping criterion for the iterative procedure:
_ =_ _ =) sw) _
BR” =-7X 46 =- FZ? 42X46 (5.1.36)
. . . =)
where the normalized L-2 norm is defined as VIR /[IC]] x 100%. From
(5.1.33) (5.1.36), it follows that
M
5 Boy oe A coe Su)
RO = FRO _ZMXO Ga _ZMXO = s a xo (5.1.37)
m=0
and
> s(s5)~ a = aI
ROY = AZOKOHY _ZOKOM LS LSMY _ EG 5.1.38)
Thus the residual vector can be computed readily from the updated right-
hand sides. In the numerical results illustrated in this section, the stopping
criterion of the iterative solution is sct at 0.1%.
Computational Complexity
For the TE case the matrix is symmetric. The bandwidth b is usually much
smaller than the order of the matrix N. To take full advantage of the banded
matrix 2, a direct banded matrix solver is used to solve (5.1.33) and
(5.1.34), The LU decomposition requires O(b?N/2) operations, while the
sS(w)
backsubstitution only requires O(2bN) operations. The Z ( X product is
computed by the FFT. Therefore, we can evaluate ZX in rN (log N) +sN
operations (where r accounts for the number of FFTs and s accounts for the
number of pre- and post-multiplications before the FFT). The computational
complexity up to the nth-order solutions are O(nb?N)+O(nrN log N+nsN).
(C) Solution Based on Complete Impedance Matrix and Conjugate Gra-
dient Method (CGM)
Another iteration approach is to keep the entire impedance matrix on the
left-hand side. Then we apply a conjugate gradient method (CGM) to the
matrix equation with the matrix decomposition.
M
=(s) — — =
G >> 2) ¥=C (5.1.39)
m=0
--- PAGE 210 ---
§1.3 Weak Matrix and Unknown Column Vector 187
For the CGM version, an initial guess of X) = 0 is chosen. Let Nz be
: . eo = sw)

the number of CGM iterations. By decomposing into Z » and Z. and the
use of FFT in conjunction with CGM, the approach requires O(N.(bN +
rN log N +sN)).

Memory Requirements

_ 6). .

‘The memory requirement of the strong matrix Z is O(bN). The coefficients
(xq) in the Taylor expansions are translationally invariant. The storage

‘ Zw) ‘ Noy
requirement for Z,. , m=0,1,2,...,M,is O((M+1)N). The total memory
requirement for the algorithm is O(bN + (M+ 1)N).

In the simulations, the bandwidth 6 is an adjustable parameter. In the
updated right-hand-side approach there is a minimum bandwidth bin for
which the iteration process works. It requires many more iteration steps to
converge at b = bmin than at a larger bandwidth. Therefore, in the simula-
tions, b is chosen to be greater than the bin so as to reduce the number
of iteration steps. For the CGM iterative approach discussed above, the
bandwidth can be smaller than the one used in the updated right-hand-side
approach. This is because the bandwidth in this case depends on the accu-
racy of the Taylor series expansion. As a result, this approach requires less
computer memory, and therefore it is ideal for very large surface lengths.
However, it usually takes more iteration steps to converge. In Section 1.5,
only the 2500 wavelength surface examples are performed by applying the
CGM iterative approach.

1.3 Product of a Weak Matrix and a Surface Unknown Column
Vector
From (5.1.32), the product of a matrix term in the Taylor expanded impe-
dance matrix with column vector can be expressed in the form
v=T,Za0.X (5.1.40)
‘The calculation procedure of equation (5.1.40) is as follows. First, the prod-
uct T,X is performed (premultiplication). Next, the product Zq and T,X
is done by the FFT. Then the product of T, and ZT, X is performed
(postimultiplication).

In Fig. 5.1.1, we illustrate the physical interpretation of the two ways of
calculating radiation from N source points to N field points on the rough
surface. Direct calculation is from source $ to field point R. Indirect calcu-
lation consists of first translation from source point to a point Sy on the flat
--- PAGE 211 ---
188 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
Rs Field Point
Source Point
—_ .
s
Z,
[ « ; *
Flat Surface
Reference Plane
Figure 5.1.1 Direct (dotted line) and indirect (solid line) calculation of radiation from a
source point § to a field point I. Points Sz and Ry are projections respectively of points
and R on flat surface. Indirect calculation procedure: (1) Translate from a source point to
a point Si on the flat surface via T, (2) translate from Sy to Ry on flat flat surface using
Zq, and (3) translate from Ry to R via Ty.
surface via T,. Next, we calculate radiation from $7 to Ry on flat surface
using Zq. Finally, we calculate translation from R y to R via T,. For a single
source point S$ to a single field point R, direct calculation is faster. However,
for calculations of N source points to N field points, indirect calculation
is faster. Direct calculation requires N? operations. Indirect calculation re-
quires N operations for T,, times a column vector, N log N for Zq times a
column vector, and N for T, times a column vector. Indirect calculation is
faster because of the use of FFT.
1.4 Convergence and Neighborhood Distance
In actual numerical computation, the method works for a neighborhood dis-
tance rg which is much less than the surface length Z. The kernel Green’s
function can be decomposed into two parts representing strong and weak
interactions as limited by the neighborhood distance rg.

GU, 7') = GU, PU ra — |e = 2!) + GPU —2!|— ra) (6.1.41)
where U is a Heaviside step function. Then the integral equation of (5.1.2)
can be put into the following form:

prtra df(a)]? 5; aul?
| da! s+ [42 | arr)
pra da’ On
2
af a’) ?Y* u(r’)
= bine?) — dz’ 414] Grr) (5.1.42
incl) [ cena V+ [Ss ry 6.142)
--- PAGE 212 ---
§1.5 Results of Composite Surfaces and Grazing Angle Problems 189
The left-hand side represents the strong interaction ZR, and the second
term on the right-hand side represents the weak interaction ZR, the mag-
nitude of which is estimated as follows.

Because rq is chosen to be at least several wavelengths, an asymptotic
approximation can be made on the two-dimensional Green's function of the
Hankel function. Thus

1
=u). df(x’)]2)? explikit —7)) Ow’
o@X)=0 [ de! 14 eee 4 exp(ikfr = 7) Ou(r)
J\e-2'|>ra dx’ (klF —7/|)2 On
(5.1.43)
where O(-) represents the order of magnitude. We note that wine is of order
O(1) and that 9 is of order kO(1), assuming that the order of magnitude
of the normal derivative of the wavefunction is about the same as that of
the incident wave. Thus, if rg > h, where h is the rms height, then
oo n72)2 ha! (rt
sw), a oxplik(a’ — x)] Oy
oF) _ [ ae 14 [| exp[ik(a’ *)) au(r")
Jataa+ra de’ (h(a! —a)]? On
a
wa df(x')]2) ? explik(« — x')] Ou(?’
+f da! 414 [| explik(e = 2°)] vt") (5.1.44)
—00 dx (k(a’ —a)]? On!
An asymptotic evaluation of (5.1.44) can be performed by integration by
parts. This gives
oF ®) o( 1 ) (5.1.45)
= a, 5.1
Vvkra
Thus the weak part ZR is of order O(1/Vkra) and is smaller than Wine.
Sw) ss)
Hence ZX is smaller than Zz" X. The left-hand side of (5.1.42) balances
most of wince. However, for the case of 2-D surface (3-D scattering problem),
su) .
the result for the estimate of O(Z xX ) is different from that of the 1-D
surface (2-D case), as shown Chapter 6. For iteration approach (A) with
=(w)(0) Ze) . 0)
Z as well as Zon the left-hand side of (5.1.15), the product (Z © —
Sw)(0) : Bw
Zz a a will be smaller. This indicates that the order of magnitude of Z xX
is dimension-dependent.
1.5 Results of Composite Surfaces and Grazing Angle Problems
In this section, we present the results that were generated when the approach
was initially proposed [Tsang et al. 1994, 1995]. All the computations were
--- PAGE 213 ---
190 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
"Method Speed
| BMIA/CAG 0.20 MB
Table 5.1.1 £ = 40A, N = 400, Iteration for BMIA/CAG is based on Method B.
Method Speed Memory
Gaussian elimination days 512 MB
“BMTA/CAG | 20 minutes
Table 5.1.2 £ = 800A, N = 8000. Iteration for BMLA/CAG is based on Method B.
done on a SUN SPARC10 which has a speed of 60 MHz. We use 10 unknowns
per wavelength. In the figures, the bistatic scattering coefficient o(0,) as
defined by (4.1.56) is plotted.
Example 1. Comparison of CPU and memory requirements
In Tables 5.1.1 and 5.1.2, we compare the CPU and memory requirements
for L = 40. (400 unknowns) and L = 800A (8000 unknowns) for h = 0.52,
correlation length J = 1.0, and incident angle of 10°. The BMIA/CAG is 60
times faster than the Gaussian elimination. ‘The results of all these methods
completely overlie each other. For the case of L = 800A (8000 unknowns), the
BMIA/CAG requires only 20 minutes CPU for one realization and a memory
of 26 MBytes. The CPU time for the method of Gaussian elimination consists
of projected values only.
Example 2. Comparison of results for different surface lengths for one
realization and for averages over realizations
In Fig. 5.1.2, we compare the results of surface length of (a) L = 40A, (b)
L = 200, and (c) L = 800) for one realization. The rms height is h = 0.5A,
correlation length 1 = 1.0A, and incident angle 6; = 10° with g = L/4. We
note that the results of the three cases have different features. The largest
surface length case of L = 800X has very rapid angular fluctuations of inten-
sity, a feature that is very different from L = 40A, which has much slower
angular fluctuations of intensity. Instead of using a tapered wave, another
method is the periodic boundary condition method (PBC). This mwnethod
uses a plane wave and assumes that the random rough surface lengths re-
--- PAGE 214 ---
§.5 Results of Composite Surfaces and Grazing Angle Problems 191
20- 2
By g uf
2 sol 2 is
go 2 |
ois -
Boal Bos
B oe: B oe
go goon
2 o- ge
Oe mo em 8 me an 0 8
Scattering Angie (agrees) ‘Scattering Angle (Degrees)
(a) (b)
20 20
Eu zou '
a st Lind
z z bt
B = 1 fetes
zo zo hgh
B os Bo hetgmitrl $k g
2 2 ah nH Ayn ast
gM = x! OE aes |i
ge go JMS $f ty legit a
i i } a a a a
Scattering Angle (Degrees) Scattering Angle (Degrees)
co) @)
Figure 5.1.2 Comparison of various surface lengths of one realization with h = 0.5, |=
1.0\. and @; = 10°. The number of surface unknowns are varied from (a) V = 400 with
b = 40(4d), (b) N = 2000 with 6 = 200(20A), (c) N = 8000 with 6 = 400(40d), and (d)
periodic boundary condition (PBC) with N = 400.
peats itself for a given period P. Usually the period used is not very large.
The PBC method was described in Chapter 4. The CPU associated with
computing the periodic Green’s function can be intensive. In Fig. 5.1.2d, we
show the result of a periodic boundary condition with period = 404. Because
of the periodic boundary condition, the scattered angles As, are governed
by the Floquet modes ksin Os, = ksin 0; + aan m = 0,4+1,+£2,..., which
results in a finite number of angles. We note that the features of the peri-
odic boundary condition are also different. Because of the finite number of
discrete scattered angles, it does not have the rapid angular variations as
in the 800 surface length case. Its features are more like that of a surface
length of 40, of Fig. 5.1.2a. ‘The imposition of the PBC does not imply that
the rough surface is random from —oco to +00.
In Fig. 5.1.3, we compare the results when averaged over realizations.
--- PAGE 215 ---
192 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
os oa
Eo fe
j os 7
os o os
Fas Eve
Boo Eos
go Boo
Oo a mw fo ea wo om
‘Scattering Angle (Degrees) ‘Scattering Angle (Degrees)
(a) {b)
a oy
3 o7 é or
5 oe 3 oe
Boos Bo
gc go
oy 2 4 a 0 a w= a  )
Scattering Angle (Degrees) Scattering Angle (Degrees)
() (dy
Figure 5.1.3 Comparison of Monte-Carlo simulations of small and large surface lengths
with (a) L = 40A with 4000 realizations, (b) L = 200. with 800 realizations, (c) L = 800A
with 200 realizations, and (d) periodic boundary condition method with L = 40A with 100
realizations. The parameters are h = 0.54, 1 = 1.0, and 0; = 10°.
The numbers of realizations are 4000 for L = 40A, 800 for L = 200A, 200
for L = 800A, and 100 for the periodic case with P = 40\. The results of
all four cases are similar upon averaging over realizations. It is to be noted
that in Fig. 5.1.3d of PBC, the data points for angles beyond —78° are not
available since the number of angular data points are limited by the Floquet
modes.
Example 3. Close to grazing and moderate RMS height and correlation
length
In Fig. 5.1.4a, we illustrate the results for an incidence angle = 85°, rms
height A = 0.5\ and / = 1.0\ and averaged over 50 realizations. We com-
pare three cases of (L = 200A, g = L/4), (L = 800A, g = L/4), and
(LZ = 800\, g = L/8). The results for the cases agree except for the for-
ward specular direction (Fig. 5.1.4b) and the vicinity of the backscattering
direction (Fig. 5.1.4c). The difference in the forward direction is due to the
--- PAGE 216 ---
§1.5 Results of Composite Surfaces and Grazing Angle Problems 193
Ew A
2 we i
3 Ibe
8 108] " ne
P io \
g .
B10 oo ,
B —— L200 wavelength, 9=0.25L
10 = + L=800 wavelengths, g=0.25L
Bios ~----_L=B00 wavelengths, g=0125L
2 a ——re-erv—ore
rook. —
80-60 402000
‘Scattering Angle (Degrees)
(a)
Eo so
5 tf SM
6 vy ,
Boag) cet sO
g 107] | — L=200 wavelength, g=0.25L. ‘
© |_| - - - L+800 wavetengths, g=0.25L on
B gg, | bA800 wavelengths, 90.1281. | .
% 7 7 88ST
Scattering Angle (Degrees)
(b)
103 _
3 a = ~
8 tos — +200 wavelength, g=0.25L
Bo | 77 > L=B00 wavelengths, g=0.25L
Sot ~-+-+ L=800 wavelengths, 9=0.1 251.
= | — Flat Surtace :
8 10 — -
2 4
S toe /
@ Flat Surtace /
a
"og ass 87 G68 wae G0
‘Scattering Angle (Degrees)
(c)
Figure 5.1.4 (a) Comparison of bistatic scattering coefficients for various surface lengths
and g for 50 realizations with h = 0.5A, 1 = 1.0, and 0; = 85°. For L = 200A the bandwidth
is b = 200(20A), and for 1 = 8002 it is 6 = 400(40A). (b) Comparison of bistatic scattering
coefficients of (a) near-specular direction. (c) Comparison of bistatic scattering coellicients
of (a) near backscattering direction. The flat surface result is for L = 800A and g = 0.25L.
--- PAGE 217 ---
194 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
fact that the forward scattering peak of the coherent wave depends strongly
on the surface lengths. The bistatic scattering coefficient from the largest
surface length and the smallest tapering gives the smallest scattering level
for angles beyond —85°. In Fig. 5.1.4c, an additional simulation is performed
with a flat surface to illustrate the edge diffraction contribution to backscat-
tering. Note that the backscattering level is at least two orders of magni-
tude larger than the edge diffraction. For this particular example, we have
achieved convergence up to —87°.

Example 4. Close to grazing angle and composite surface

Next we examine the case of scattering from a composite random rough
surface at a near-grazing incidence angle of 0; = 85°. The composite surface
has a small-scale roughness (hy = 0.1A and 1; = 0.3A) superimposed on
a larger scale roughness (hy = 0.5A and ly = 5A). Figure 5.1.5a shows the
bistatic scattering coefficient for one realization for the surface length of 2500
wavelengths with 25,000 surface unknowns. From Table 5.1.3 we can see
that in order to perform Monte Carlo simulations with the 25,000 unknowns
case, other methods which require the storage of a full matrix would be
impossible on a workstation. However, using the BMIA/CAG, we were able
to compute the solution. For a problem of this size, it requires 6 CPU hours
on a SPARC10 workstation with 75 Mbytes of memory. In Fig. 5.1.5b, the
bistatic scattering coefficient for 50 realizations is shown.

In Fig. 5.1.5c, we compare the four cases of L = 200A, L = 400\, L =
800A, and L = 2500X near the backscattering angle. Clearly, the L = 200
surface is not large enough for the parameters used for this example. On the
other hand, the results for L = 400A, L = 800A, and L = 2500A agree near
the backscattering angle of —85° and up to —88°. This shows convergence of
the bistatic coefficient with respect to the surface length for the scattering
angles up to —88°. Next in Fig. 5.1.5d, the bistatic scattering coefficient from
the 2500 wavelengths composite surface is compared with the result from
the PBC with P = 40X. Since the periodic surface has the periodicity of 40
wavelengths, the angular resolution is only 6° near the backscattering angle
of —85°. This is illustrated in Fig. 5.1.6 for one realization with P = 40A.
In fact, for the 40 surface, the maximum backscattering angle for PBC is
—78°. If we use a period of 200A for PBC, The matrix building time for this
corresponding 2000 « 2000 matrix can be large.
--- PAGE 218 ---
§1.5 Results of Composite Surfaces and Grazing Angle Problems 195
Method Memory
Gaussian elimination 5000 MB
BMIA/CAG 75 MB
Table 5.1.3 L = 2500, N = 25000. Iteration for BMIA/CAG is based on conjugate
gradient and matrix decomposition (Method ©).
| _ wh
8 wos! ca
2 oe, e
3 BW
po Boe
8 ee a
an ee
a Bo
fot ee - a
a a oe a
Scattering Angle (Degrees) ‘Scattering Angle (Degrees)
(a) (b)
E10 weer TAY ‘4 Mere
8 ios ee &
2 = L=200 wavelengths 2 — +2500 wavelengths (50)
5 oaoo wavelengths 5 Ton oso wavelangtle Gu)
ey, | === £2600 wavelongths Bags —
a | i UieeSaveenge |g
we rr
ee 6 cD a
‘Scattering Angie (Degrees) ‘Scattering Angie (Degrees)
(c) (d)
Figure 5.1.5 (a) Close to grazing angle and composite surface. Incident angle 0; = 85°, g =
0.125, 6 = 400. hy ~ 0.1, and ly = 0.3A, hg = 0.5A, and ly — 5A for one realization,
(b) Close to grazing angle and composite surface. Averaged over 50 realizations, (c) Com
parison near-backscaticring angle for various surface lengths. Parameters are those of (a).
For 2500 wavelengths surface 50 realizations of Fig. 5.1.5b is used and others are averaged
over 10 realizations, ‘The bandwidths of = 200A and L = 800. are the same as Fig. 5.1.4a,
for L = 400A, 6 = 300(30A). (d) Comparison near-backscattering angle with the periodic
boundary condition method (PBC). For BMIA/CAG the result of (b) is used. The PBC is
for the surface length of 40 wavelengths and averaged over 30 realizations. Parameters are
those of (a).
--- PAGE 219 ---
196 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
0.50

E

g

5 090

°

a 0.20

009 00 200 300 “400
Surface points
Figure 5.1.6 Magnitude of the surface current for one realization for the PBC method
with P = 40 wavelengths. Parameters are those of Fig, 5.1.5a.
2 Physics-Based Two-Grid Method for Lossy Dielectric
Surfaces

2.1 Introduction
In the application of the method of moments to the rough surface scatter-
ing problem, a common implementation is to use a grid of 10 points per
free-space wavelength to discretize the surface. We shall call such a grid-
ding a single coarse grid (SCG). However, in lossy diclectric surfaces, the
wavelength in the dielectric medium is much shorter. ‘Thus in scattering by
lossy diclectric rough surfaces with high permittivity, there can be rapid spa-
tial variation of surface ficlds. For microwave remote sensing applications,
both wet soil surfaces and ocean surfaces can have large permittivity. Two
alternatives were used. The first alternative is to use impedance boundary
condition as shown in Chapter 4. The disadvantage of this alternative is
that an approximation is used in the problem. The second alternative is to
use a dense grid with a large number of points (say more than 30 points)
per free-space wavelength. We shall call such a gridding a single dense grid
(SDG). We have shown in Chapter 4 that dense sampling of points is a re-
quirement for energy conservation and an accurate calculation of emissivity,
The disadvantage of this second alternative is that there is a large increase
in CPU and required memory. The physics-based two-grid (PBTG) method
to be discussed in this section is an improvement over these two alternatives
in that it has the same accuracy as the single dense grid and yet has a CPU
comparable with that of the single coarse grid. To demonstrate the accuracy
of the PBTG method, we use it to calculate the emissivity of a random rough
surface. In PBTG, two grids were used: a dense grid and a sparse grid. The
--- PAGE 220 ---
§2.1 Introduction 197
sparse grid is that of the usual 10 points per wavelength. The dense grid
ranges from 20 to higher number points per wavelength, depending on the
relative permittivity of the lossy dielectric medium. The method of PBTG
is based on the following two observations: (1) Green’s function of the lossy
dielectric is attenuative, and (2) Green’s function of free space is slowly
varying on the dense grid. Because of the Kramer-Kronig relation, a large
real part of dielectric constant is associated with a large imaginary part.
The first property of the lossy diclectric gives a banded submatrix for the
Green's function of the lossy dielectric. When the Green’s functions act on
the surface field on the dense grid, it corresponds to the product of a sparse
matrix with that of a column vector. ‘Thus the convolution of the lossy di-
electric Green’s function with surface fields is a spatial limited operation.
The second property means that the convolution of the free space Green’s
functions with surface fields on the dense grid is a spatial frequency limited
operation. This allows us, when using the free space Green’s function to act
on the surface fields of the dense grid, to first average the values of surface
unknowns on the dense grid and then place them on the coarse grid. PBTG
calculates surface ficld solutions on the dense grid. It needs to be mentioned
that PBTG is different from multigrid method [Donohue et al. 1998, Briggs.
1987]. The multigrid method tries to facilitate the convergence of iterations
in iterative techniques. It entails discretization of the structure into various
grid sizes. The coarse grid corresponds to the low-frequency portion of the
solution, while the fine grid corresponds to that of the high-frequency solu-
tion. An iterative solution is obtained for cach level of discretization, and the
solutions are interpolated from the coarse grid to the fine grid. The solution.
is first obtained in the coarse grid, and then one moves to the next level of
fine grid. Once the iterative solution is obtained in the fine grid, one has
to go back to the coarse grid to refine the solution. The present method of
PBTG, on the other hand, is based on scattering physics. The purpose of
PBTG is to speed up the matrix-vector product of two Green’s functions
convolving with the surface fields on the dense grid.

We use two grids in PBTG: a dense grid and a coarse grid. The inter-
action is divided into (1) a very near field of less than 1 wavelength, (2)
a near field of between 1 wavelength and rg wavelengths, and (3) a non-
near-field beyond rg wavelengths. In the numerical simulations performed in
this section, rg is fixed at 10 wavelengths. For very near-ficld interactions,
we use a dense grid which is represented by four banded submatrices. For
near-field and non-near-field interactions, the free-space Green’s function is
slowly varying on the dense grid. We average the fields on the dense grid to
--- PAGE 221 ---
198 5 FAST METHODS FOR ROUGH SURFACE SCATTERING
get fields on the sparse grid. For the non-near-field interactions, we further
expand on a canonical grid of a horizontal surface so that the fast Fourier
transform (FFT) can be applied. In the lower medium, non-near-field inter-
actions were neglected because of lossy properties of the lower medium. The
approach is denoted as PBTG-BMIA/CAG. The computational complexity
and the memory requirements for the present algorithm are O(N log(N))
and O(N), respectively, where N is the number of surface unknowns on the
coarse grid. Using this approach, we illustrate numerical results of TE and

TM wave scattering up to surface length of 500 wavelengths and 30,000 sur-

face unknowns. The salient features of the numerical results are as follows:

(1) A single coarse grid (SCG) has poorer accuracy for TM case than for
‘TE case.

(2) PBTG-BMIA/CAG speeds up CPU and preserves the accuracy. It has
accuracy comparable to that of a single dense grid and yct has a CPU
comparable to that of a single coarse grid. It also gives surface fields on
the dense grid and can give accurate results of the surface fields even
when the surface fields have large spatial variations.

(3) PBTG-BMIA/CAG gives accurate results for emissivity calculations.

2.2 Formulation and Single-Grid Implementation

Consider a tapered plane wave, ¥inc(x, z), impinging upon a 1-D rough sur-

face with a random height profile z = f(x). It is tapered in the spectral

domain so that the illuminated rough surface can be confined to surface
length L. The incident wave is tapered in the spectral domain as given in

(4.1.42),

poo . 7) _ (ke hag)9%
Vinel, f(a) = ce sal? 52.)

Let x and 71 denote, respectively, the wave functions for the upper medium

and lower medium. From Chapter 4, Section 2, they satisfy the following

surface integral equations
I _ OG(F,7" = Or 7”
gum) -f po) — Gr, ry ds = WineT) (5.2.2)
1 ’ IG(F,r Ge
se) +f [nme ~ alr, pyre) ds =0 (5.2.3)
where f denotes a Cauchy principal value integral and G and G; are the
s

2-D Green’s function of the upper and lower medium. The wave functions y

and 7 are related through the boundary conditions on the surface Sas in
--- PAGE 222 ---
§2.2 Formulation and Single-Grid Implementation 199

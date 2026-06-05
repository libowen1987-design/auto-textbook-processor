# Tsang《Scattering of EM Waves》Chapter 11

> **中英双语版** | 本笔记基于 OCR 文本整理，OCR 识别率约 85-90%。

Chapter 11

> **第十一章：角相关函数**。研究随机介质的角相关函数（ACF）及其在成像中的应用，包括记忆效应的2D模拟、掩埋目标散射的角相关函数、ACF在相关成像中的应用、SAR数据模拟及ACF处理。**

ANGULAR CORRELATION FUNCTION
AND DETECTION OF BURIED OBJECT
1 Introduction 552

> **第1节：引言**（第552页）

2 Two-Dimensional Simulations of Angular Memory

> **第2节：角记忆效应的2D模拟**

Effect and Detection of Buried Object 553
2.1 Introduction 553

> **2.1 引言**

2.2 Simple and General Derivation of Memory Effect 553

> **2.2 记忆效应的简单与一般推导**

2.3 ACF of Random Rough Surfaces with Different Averaging

> **2.3 不同平均方式的随机粗糙面ACF**

Methods 555
2.4 Scattering by a Buried Object Under a Rough Surface 557

> **2.4 粗糙面下掩埋目标的散射**

3 Angular Correlation Function of Scattering by a Buried

> **第3节：掩埋目标散射的角相关函数**

Object Under a 2-D Random Rough Surface
(3-D Scattering) 564
3.1. Introduction 564
3.2. Formulation of Integral Equations 565
3.3. Statistics of Scattered Fields 570
3.4 Numerical Illustrations of ACF and PACF 571

> **3.4 ACF与PACF的数值示例**

4 Angular Correlation Function Applied to Correlation

> **第4节：角相关函数在相关成像中的应用**

Imaging in Target Detection 575
4.1 Introduction 575

> **4.1 引言**

4.2 Formulation of Imaging 578

> **4.2 成像公式化**

4.3 Simulations of SAR Data and ACF Processing 580

> **4.3 SAR数据模拟与ACF处理**

References and Additional Readings 591
— 551 -
--- PAGE 570 ---
552 11 ACF AND DETECTION OF BURIED OBJECT
1 Introduction

Besides using radar cross section, it is important to study statistical
> 除雷达截面外，研究场的统计矩也很重要。角相关函数（ACF）已被用于检测随机介质中的掩埋目标。研究表明随机粗糙面的ACF在记忆线（memory line）以外通常很小。 mo-
iments of the field. It is also useful to study object buried in random media.
In remote sensing applications, investigators have used angular correlation
functions [Chan et al. 1999] and frequency correlation functions (Sarabandi
and Nashashibi, 1999]. Angular correlation function has also been used in
detection of object that is buried in random media [Tsang ct al. 1996; Zhang
and Tsang, 1997, 1998; Zhang et al. 1998a,b]. Experiments have also been
performed [Chan et al. 1999].

Studies show that the angular correlation function of scattering by ran-
dom rough surface is generally small away from the memory line. The angular
correlation function is the correlation function of two scattered fields in di-
rections 952 and 4,; corresponding to two incident waves in the 6j2 and 6)1
directions, respectively (Fig. 11.1.1). The correlation function is obtained by
taking an average over realizations (samples) of rough surfaces. The mem-
ory line obeys the angular relation of sin 4,2 — sin @,) = sin6j2 — sin 6:1. The
memory line is a result of statistical translational invariance of the random
rough surface. This is analogous to phase matching. For a planar boundary
separating two homogeneous media, the problem is horizontal translational
invariant. The horizontal translational invariance gives rise to Snell’s law as
a result of phase matching. For periodic structures, the translational invari-
ance of the structure holds when the translation is equal to a period. In this
case, phase matching gives Floquet’s theorem. For random medium, assum-
ing statistical translational invariance of the medium, the memory effect is
a consequence of the phase matching of the statistical moments of the fields.

5, /
wy On f
so) 9.2!
Y yf Ost
Figure 11.1.1 Configuration of angular correlation of wave scattering by a buried object
under a rough surface. Scales are in wavelengths.
--- PAGE 571 ---
§2 2D Simulations of Angular Memory Effect and Detection of Buried Object 553

In this chapter, we study the angular correlation function, the memory
> 本章研究角相关函数、记忆效应以及随机介质中掩埋目标的检测。第2节研究2D模拟，比较ACF和雷达截面。第3节进行3D模拟。第4节研究SAR成像，利用ACF改善圆形SAR中掩埋目标的成像质量。
effect [Feng ct al. 1988] and the detection of object buried in random media.
In Section 2, we study two-dimensional simulations and compare the angu-
lar correlation function and radar cross section. In Section 3, we perform
three-dimensional simulations. Both angular and polarization correlations
are utilized. In Section 4, we study SAR imaging. Angular correlation func-
tion and angular-frequency correlation function are used. It is shown that
using angular correlation function in circular SAR improves the imaging of
the buried object in random media.
2 Two-Dimensional Simulations of Angular Memory Effect

> **第2节：角记忆效应的2D模拟**

and Detection of Buried Object
2.1 Introduction
In Section 2.2, we first give a simple derivation of the memory effect. In
Section 2.3, we study the detection of buried object. In the real-life problem
of buried object detection, the buried object is under a single random rough
surface. [f the wave is incident on another part of the random rough sur-
face (another sample of rough surface), the buried object may no longer be
within the incident beam. Thus, averaging over realizations of random rough
surface is not applicable. In this section we study the electromagnetic wave
scattering of a tapered incident wave by a buried object under a single ran-
dom rough surface. The angular correlation function is calculated by taking
the average over frequencies instead of taking the average over realizations of
random rough surfaces. It is shown that for a sufficiently long random rough
surface, the memory line still exists on averaging over frequencies. We also
show that away from the memory line, the contribution of random rough
surface scattering to the angular correlation function is small. This means
that scattering by the buried object becomes more conspicuous.
2.2 Simple and General Derivation of Memory Effect

> **2.2 记忆效应的简单与一般推导**

The memory effect is a condition of generalized phase matching due to statis-
tical translational invariance of clutter (volume scattering and rough surface
scattering). This is the only condition that is needed to derive the memory
effect condition for the angular correlation function. The memory effect was
first described by Feng ct al. [1988].

The angular correlation function is the correlation function of two scat-
tered fields in directions 9,2 and 51 corresponding to two incident waves
--- PAGE 572 ---
554 11 ACF AND DETECTION OF BURIED OBJECT
in the 62 and 9; direction, respectively (Fig. 11.1.1). The correlation func-
tion is obtained by taking an average over realizations (samples) of rough
surfaces.

If the clutter is statistically translationally invariant in a horizontal
direction, the statistical phase-matching condition for the two-dimensional
scattering problem is

Ksxi — Bsa2 = Kina — kina (11.2.1)
or
sin 4.1 — sin Ao = sin 91 — sin 62 (11.2.2)

The relations of (11.2.1)-(11.2.2) are proved as follows: Let Ji1 and Jig be
the two antenna sources that launch the incident waves in direction kj; and
kia, respectively. The wavevector components in « direction are respectively
kig, and kjg2. Note that the antenna currents Jj; and Jj2 that launch the
incident waves are not random. Let G(p,p’) be the exact Green's function
for the boundary value problem that includes volume scattering and rough
surface scattering effects. Assume statistical translational invariance in the
horizontal «-direction and let Ax = ¢Az. Then the following statistical
properties hold for the exact Green’s function

(G(p + Be, p' + Ke) = (G(p,7')) (11.2.3)

(Gp + Ax, p" + Axy@"(p' + Ax,p" + Ax) = (G(p,p")G" (p',p")) (11.2.4)

where the angular brackets denote the ensemble average. Note that the hor-

izontal translational invariance holds when averages are taken. It does not
hold for each realization.

Let the scattered field be ¢,; and 52 for the two antenna currents Jj,
and Jj2, respectively. Then

1 = [ COP @) (11.2.5)
82 Lia
Because the incident wave is a plane wave with e“- dependence, the au-
tenna that launches the incident plane wave obeys the condition
Triay (p+ Kx) = exp 4 ikpiety At} Jpn (7) (11.2.6)
[3] [iz] [3]

The second moment, as given by the average of the product of two

scattered fields, is
(eatPria’(@)) = f an" [ ap"G@.pNG@.7")Ia@" 40")
, (11.2.7)
--- PAGE 573 ---
§2.3 ACF of Random Rough Surfaces with Different Averaging Methods 555
‘The two incident field directions are kj, and ki. Displacement of p and 7!
by Ax gives
(ysi(p + Bx)wyo(p! + Be)
= fo [amrco+ Bs, BG Gp + Az,p")) Ja") Fo(0")
= [ar | dp" (G(p + Az, p" + Ax)G" (a! + Ax. p” + Az))
-Aa(p" + Aa) Ji(o" + Ax)
= | oe" fo CO.r ye @'.7") alo" + Br\ylp" +e) (11.2.0
The second equality is a result of transformation of dummy variables. The
third equality is a result of using the statistical translational invariance prop-
erty of (11.2.4), Next we make use of the translational property (11.2.6) of
the antenna current in (11.2.7). Then
(Us (B+ Ae)wro(p' + Az))
_ cthentag heeds fag! [ap cp,pIyG(WP")In (p)Ia(p")
= ethene thaad2 (a But) (11.2.8)
In the scattered directions kg; and ksz2 respectively of 4.1 and y.2, we have
(wiai(9 + Be)sa(@ + Be) = Me (pwe(P)) (11.2.9)
Substituting (11.2.9) into (11.2.8) gives
ellker Khor (uy. (Dur (p!)) = ellie “Bie 0 (ys 5 B)ut(p’)) (1.2.10)
Thus balancing the two sides of (11.2.10) gives either (151 (A)W%2(7’)) = 0 or
the memory effect condition
Kivi ~ hiea = Rea — ksx2 (1.2.11)
In terms of angles,
sin), ~ sin @j2 = sing. — sin Oe (11.212)
2.3 ACF of Random Rough Surfaces with Different Averaging

> **2.3 不同平均方式的随机粗糙面ACF**

Methods
Tn the simulation of wave scattering from rough surfaces, it is customary as
shown in Chapters 4 to 6 to use the realization average to calculate the scat-
tering cross section. However. when the object is buried under a single rough
surface, realization averaging is not applicable, and other means of taking
--- PAGE 574 ---
556 11 ACF AND DETECTION OF BURIED OBJECT
coherent averages must be investigated. We examine the ACF based on three
methods of averaging: realization, frequency, and angular. The normalized
scattered field is defined by
ir
8 (F ,
WR= Fs (ks, ky) (1.2.13)

Realization averaging: The ensemble average is obtained by taking aver-

aging over different samples (rough surfaces) with the same statistics.
N,
loon :
T (951, 9113 92, 9:2) = N WN (Os1, O11, nN” (O50, Oia, 2)/ VPP
NT nel

(11.2.14)
where n denotes the realization index, and N, is the number of realizations.
P, and P2 are total power flux of the two incident waves, respectively. In
general, many independent realizations must be generated to get smooth
averages.

Frequency averaging. Frequency averaging takes an ensemble average
over a frequency bandwidth 2Af centered f,. This can be done if scattering
data are available over a wide frequency band. The excitation frequency
varies between —Af + fp to Af + fo

Ng
5 1 a "
Ty (Os1, 0:13 952, 8:2) = Ny WY (sr. 011s fn) uN * (O52. 0:25 fn) / V PLP2
‘ n=!

(1.2.15)
where N, is the number of frequencies over the frequency range fo — Af <
In < fo+ Af, and n is the frequency index for fy.

Angular averaging: The angular averaging is defined by the small changes
of incident and scattering angles around the fixed angles.

Ta (9s1, 6:1; 952, Fi2)
N,
low - \ N. .
= eh er + dns Or + Sn) Baa + bn, Oia + Jn)/V PVPs (11.2.16)
e nsl
where Ne is the number of the angles, and 5, is the small angular difference
for index n.

Figure 11.2.1 shows the ACF magnitude with the three different en-
semble averaging methods. The random rough surface is generated by using
the spectrum method with a Gaussian height distribution and a Gaussian
correlation function. The tapering parameter g chosen to be L/4. We plot
the ACF as a function of sin 9,2 and sin@,9 with fixed angles @;; = 20° and
45, = —20°. Figure 11.2.1a is the result for one rough surface without any
--- PAGE 575 ---
§2.4 Scattering by a Buried Object Under a Rough Surface 557
averaging. Figure 11.2.1b is that of realization averaging taken over 100 real-
izations. It is clear that the existence of the memory line becomes apparent
if a sufficient number of independent samples are included. Figure 11.2.1¢
shows the ACF magnitude of a single rough surface based on the frequency
averaging method. ‘The single rough surface profile is as shown in Fig. 11.1.1.
There are 50 equally spaced frequency samples over the frequency bandwidth
of 0.5f. to 1.5f. Although the ACF magnitude by frequency averaging is
noisier than that of realization averaging, a distinct. memory linc is clearly
visible. To suppress fluctuation in Fig. 11.2.1c, more independent samples
must be included in the averaging process. It was estimated that only about
10 independent samples can be obtained with the bandwidth of 0.5f, to
1.5fo. For the frequency averaging to be effective, a wide bandwidth may be
required. Figure 11.2.ld shows the ACF magnitude by the angular averag-
ing method given in (11.2.16). The results are smoother than those without
averaging (Fig. 11.2.1a), but the memory line is not as clearly visible as that
of frequency averaging.

2.4 Scattering by a Buried Object Under a Rough Surface

> **2.4 粗糙面下掩埋目标的散射**

In this section we study the scattered field from an object placed below
a rough surface. ‘he incident wave is a horizontally polarized (TE) wave,
and we assume that the buried object is a perfect conductor as shown in
Fig. 11.1.1.

Let yo and %; be the fields in regions 0 and 1, respectively, and let the
boundary conditions be zo = v1, dee = Ea at the rough surface and 4; = 0
on the surface of the object. We make use of the surface integral equations
from Chapter 4. In region 0 we have the integral equation given by, for 7 on
Sry

loo life . nv OGlF,7) _ _,Ov(7)] 4

gio) =r) +f [ve - Goh.) ds’ (1.2.17)
where ¢'(F) is the incident wave field, G,(7,7") is the Green’s function for
region 0, and f denotes the principal value integral over the rough surface.

In region 1 we have the integral equation given by

1 ~ 1 OG (F,7") _ _, Ovi 7")
pul) = yf(F) -f [« aa ~ GRP) ds’ (11.2.18)
where 1(7) is the scattered field from the buried object and is given by
: ‘ Ou (T"
us(F) = -| ag 2a@) ds! (11.2.19)
8 On
--- PAGE 576 ---
558 11 ACF AND DETECTION OF BURIED OBJECT.
oe 4 PARRA AI |
hit dl ony
" WW es
om i iil idgaf “| eh
pig ie ea ca idl
AM ve a ae hos f é d
(a) )
AB he of ie
ow 461 Milian el
02. 5 A, on rt ar ree ee we |
| a ye aoe | Als fed Bae a
OE Pe ee hk
I a oe
sete s2) 8S atta 2) sine $2) 85 ten)
©) @
Figure 11.2.1  Three-dimensional plots of ACF magnitude by different averaging methods.
Reference angles are (@j1 = 20°, @41 = 20°). Dielectric constant of region 1 is ey =
B.7 + 10.13. h = 0.35Ay, [- 1.0), L = 40A9, g = L/4. (a) One realization. (b) Realization
averaging over 100 rough surfaces. (c) Frequency averaging over a frequency band of 0.5f,
to 1.5fo. (d) Angular averaging over an angular range of @ — 10° to 6 + 10°.
and s, is the surface of the buried object.
For 7 on the surface of the buried object, we have
, f Oy (7
wm — | Ga, pO) ds' =0 (11.2.20)
Se On
where 7)*(7) is the scattered field from the rough surface, given by
OG 7,7") Ow (F)
48 (7 ol > sin ol !
OF) = wn (F) = - Gir.) | ds 11.2.21
v2) = [ [eo — ae ry ai2.21)
--- PAGE 577 ---
§2.4 Scattering by a Buried Object Under a Rough Surface 559
Thus Egg. (11.2.18) and (11.2.20) become, respectively,
lio Pe Olt) 4,
=a (F WF ds
3 (7) + [ curr) ann 8
gn OGlh?) OF) ,
+f [v Oar - ART ds’ =0 (1.2.22)
for F on sy.
On)
GFF )——— ds’
[oun gr as
ny OGA(F, 7") dyn (7)
(PED _ ay py | as! = 9
-f [oe Oni Gi(F,7') Bal ds' =0 (11.2.23)
for F on sy.

Equations (11.2.17), (11.2.22), and (11.2.23) are three coupled surface
integral equations and can be put into a matrix form with discretization.
The surface unknowns are (%)s,, (3) , and (3%) , which denote the

3, 4
values of ¢), its normal derivative on the rough surface s,, and the values of
the normal derivative of x; on an object surface sy, respectively.
ABO @).,
Ow Wi
CDE (x ), =|0 (1.2.24)
On 0
FG #H oa
On),
The quantities A through H are impedance matrices.
After the matrix {11.2.24) is solved, the scattered field in region 0 is
calculated by
f OG(F,?’) — Owl?)
»(F) = BF — GF, 7’) ———] ds’ 11.2.25
w= f oy? SEP — ary SO as (1.2.25)
The normalized scattered field is defined im (11.2.13), and the ACF based
on frequency averaging can be obtained using (11.2.15). When 61 = 42 and
Os, = 952, the ACF becomes the scattered intensity. The average scattered
intensity can be defined based on the frequency averaging method similar to
that of ACP.
1 &
= NV : 2
I; (93,04) = Ny ls (05,043 fa)?/P (11.2.26)
We conducted simulations using a circular cylinder as the buried object.
Frequency averaging is used. The cylinder is placed at a depth d = 2A, and
--- PAGE 578 ---
560 11 ACF AND DETECTION OF BURIED OBJECT
a surface length of L = 40A, is used (Fig. 11.1.1). Unless specified otherwise,
all distance units are based on wavelength A, of the center frequency.

In Fig. 11.2.2a and 11.2.2b, both ACF magnitude and scattered intensity
with and without the buried object are shown as a function of the incident
angle 6;2. The reference angles are 4;; = 30° 6.; = —50°, and the variable
angles are sct to 0,9 = —6j2. This configuration provides the backscatter-
ing cross section (RCS) for intensity, but the ACF magnitude intercepts
the memory line only at 2 = 39° at which a peak can be observed in
Fig. 11.2.2a, since 2sin 39° = sin 30° + sin 50°. In general, the RCS varies
slowly as a function of angle, whereas the ACF becomes small away from
the memory line due to the destructive phase interference in the coherent
averaging process. We note that ACF in Fig. 11.2.2 is small because the
memory line is avoided.

The ACF in Fig. 11.2.2b is much bigger than Fig. 11.2.2a because ACF
of buried object is much bigger than ACF of rough surface away from the
memory line. We calculated the ratios of ACF with and without the buried
object. A similar definition is used for the intensity. The definition of the
respective ratios are

- _ _|ACP| with buried object:
ratio of |ACE| = |ACF] without buried object
_ Pse(Oe1, Bir; sz, Giz)) (1.2.27)
\T'.(Os1, 9:1; 952, 9:2)|
cae _ _ I with buried object Ise(@s, 41)
ratio of T= I without buried object 1,(4,, 6) (1.2.28)

The comparisons of these two ratios are shown in Fig. 11.2.2c. Although
the ratio of ACF contains a large amount of fluctuation due to a limited
number of independent samples, the presence of the buried object is clearly
identifiable in the ACF data because the ACT ratio is considerably higher
than that of the ratio of intensity. For example, for —40° < 62 < 40°, the
ratio of intensity is about 1 dB while the ratio of ACF is up to 15 dB. In
Fig. 11.2.2a-c, the intensity and its ratio are that for (45,4;) = (@s2, 6:2) at
back directions (8, = —6;).

The large difference between the ratio of ACF and that of RCS in
Fig. 11.2.2c is partially due to the small scattering from the rough sur-
face at the reference angles (4;; = 30°, 41 = —50°). For a fair comparison,
two ratios of intensities are shown in Fig. 11.2.2d. One is for the reference
angles with (@,,4;) = (@s1,4i1) = (—50°, 30°) used in (11.2.28), and one is
for the observation angles (95, 4;) = (92, 4:2) = (—@i2, Ai2) in (1.2.28). It is
to be noted that the results shown in Fig. 11.2.2d are obtained by an addi-
--- PAGE 579 ---
§2.4 Scattering by a Buried Object Under a Rough Surface 561
8-10 B-10
2-15 3
5 -20 2 20K,
z 25 z 25
730 rad
9-35 9 -25 —--— Intensity
s A = 40 : ACF
“40 -50 0 50 50 oO 50
Theta_i2 (dearee) Theta_i2 (degree)
@ )
25 2
1 ACE V] —— AGE
=— === Inter for reference
20 heey 20 —_—: nen it observation
15 wis
8 8
210 210)
é @
& 5 5
0 0 ey prt
5
6 -50 oO 50 -50 oO 50
Theta_i2 (degree) Theta_i2 (degree)
© ®
Figure 11.2.2 Comparisons of ACF magnitude (solid line) and intensity (dashed line).
Averaging band is (0.5f, tol.5fo). Reference angles are 6; = 30° and @5) = ~50°. e- =
3.7+i0.13. L = 40\o, g = L/4. (a) Without the object. (b) With the object (a= 1.549, tp =
0, d = 2Ao). (c) Ratios of results in (a) and those in (b). In (a), (b), and (c), the intensity
is the backscattered intensity for the observation angles (#49 = —0;2) and a rough surface
with h = 0.1849, and 1 = 1.0. is used. (d) Ratios for a rougher surface case of h = 0.55
and 1 = 0.59. Two ratios of intensities are shown, One is for the reference angles with
(05, :) = (s1,8:1) = (—50°,30°), and one is for the observation angles with (@5,0;) =
(852, 9:2) = (—Ai2, 012).
tional averaging. We further take the angular averaging over the frequency
averaged results as given by
Na
l ; 4
Tya(Bat, Bari Biz, 8:2) = = DOL (Oar. Oia Oi ~ bn, 0:2 + Sn) (1.2.29)
OF n=l
The angular averaging is taken over a 20° angular range. We can see that
both the ratio of the intensity at reference angles and that at observation
--- PAGE 580 ---
562 11 ACF AND DETECTION OF BURIED OBJECT

| ia Tocl/IPs| Teo/Ts

{a= 0a) [OIE Cae

=80°| 2.76

[08

2785 | 0.503)

Table 11.2.1 Ratios of ACF magnitudes and intensities in decibel scale.
angles are small. However, the ratio of ACF can be 10 dB. Parameters for
Fig. 11.2.2d are the same as those used in Fig. 11.2.2c except that changes are
made for the parameters of the rough surface with h = 0.5A, and | = 0.5A9
instead of h = 0.18A, and / = 1.0A,. A rougher surface produces large clutter
scattering at large angles. In this case, the ratio of intensity at both reference
angles and observation angles are small, but the ratio of ACF can be larger
by 10 dB.

In Table 11.2.1, the ratios obtained with (11.2.27) and (11.2.28) are listed
for the reference angles (;1,4s1) of (20°, —40°), and (30°, —30°), (30°, —40°),
and (30°,—50°). In most cases, the ratio of ACF is higher than that of the
intensity.

Figure 11.2.3 shows the ACF magnitude for various rms heights and
soil moisture conditions. Results are shown for the reference angles in the
backscattering direction as a function of incident angles 6,2, Ty (9x1 = —20°,
Gi, = 20°; ~0j2, 0:2). In Fig. 11.2.3a, the ACF magnitudes for two surface
mms heights (h = 0.35A, and h = 0.18A,) are obtained with and without an
object. The memory line is at #2 = 20° where the values are at maximum.
For rough surface scattering only, the ACF magnitude of h = 0.35A, is
substantially different from that of h = 0.18A, because the rough surface
scattering depends on the surface characteristics. However, results with the
buried object for the two different rms heights are similar because, at these
angles, the ACF is dominated by the scattering from the buried object and
the contribution from the rough surface is small. Figure 11.2.3b shows results
of two soil moisture conditions. Moisture contents of 5% and 30% in soil
corresponds to the dielectric constants of ¢, = (3.7+70.13) and €, = (16.16+
41.15), respectively, We note that for the large moisture case (30%). the effect
of the buried object becomes less because of the heavy attenuation in the
soil.

Figure 11.2.4a shows the ACF magnitude for three different depths of
the object. Although the ACF magnitude decreases with increasing depth,
--- PAGE 581 ---
§2.4 Scattering by a Buried Object Under a Rough Surface 563
(a) Dependence on the surface roughness
= 10 canna
Si (1): h= 0.35, 1= 1.0
@ 15 iN ~ (2): h= 0.18, 1= 1.0 foy-
Bao Qe oR
3 25 Wey. hers wd : Surface and object
3 MN ‘ :
3-20 Ye voy ----: Surface only
S Yoo.
SZ yg) <Q)
20 30 40 50 60
Theta_i2 (degree)
(b) Dependence on the soil moisture
B10 ote |
S — \,__ (1): 8% moisture)
215K \ (2): 30% moisture ]
8 PAA AP
BON
2 af :
3 25 Wot A ____: Surface and object
8 30 hy ak -=+--+! Surface only
pt Veo,
J YS @
Z yg lh —— a
20 30 «40 50s«O
Theta_i2 (degree)
Figure 11.2.3 ACF magnitude for various surface properties. Averaging band is (0.5fo to
1.5 fo). Reference angles are (i = 20°, @51 = —20°), a = 1.5Ao, L = 40Ag, g = L/4. (a)
Dependence on the roughness, ¢, = 3.7 + 0.13% for two cases (1) h = 0.35A,, | = 1.0, and
(2) h = 0.18Ay, £ = 1.09. (b) Dependence on the moisture, h = 0.18\9. 1 = LOAy, € =
3.7 + 0.13% for 5% moisture, ¢, = 16.67 + 1.15i for 30% moisture.
it is still much higher than that of rough surface scattering if the angles are
chosen carefully. Figure 11.2.4b shows the dependence of ACF magnitude
on the horizontal position of the object. When ay is less than 2A, (curves
1 and 2 in Fig. 11.2.4b), the object is still within the incident beam and
the scattered wave contains both rough surface and object. contributions.
This accounts for the much larger value of the ACF magnitude for curves
1 and 2, For ap = 4A, and 6X, (curves 3 and 4), the object is on the edge
of the incident beam, so that the ACF magnitude with and without the
buried object are comparable. Figure 11.2.4¢ shows the ACF magnitude for
three different object sizes: a@ = 1.59, Ly, and 0.5A,. As expected, the
ACF magnitude decreases as the size of the object decreases. However, if
the incident angle 6;2 is far away from the memory line of the rough surface,
a significant difference in the ACF magnitude is apparent even with the
smallest size (a = 0.5A,).
--- PAGE 582 ---
564 11 ACF AND DETECTION OF BURIED OBJECT
(a) Dependence on the position d (b) Dependence on the position X

BO “Gyae2 gt Tpx=0
8 | ars Ssh aix=2 |
£ pA (hde4 ae s& Wix6
gop B20
3S. Ye 3. vis oS
2 Yy Seal 25 VN / 2)
8-20 Wa 1 830, | Ks
3 } 3 V "
Zs} \ 35 v . BI,
gg 2 yg. VV |

20 30 40 80 60 2 30 40 «50 60

Theta_i2 (degree) Theta_i2 (degree)
(0) Dependence onthe size

go ——wWasts OT
245 7 a=10 |
g Gra=05 ay
20 _ 2)
3 - pe) ___: Surface and object
ad bef
S f
8.30 v\ YD — BL s-seee! Surface only
a We
35° \/ \
Syg .

20 30 40 50 60

Theta_i2 (degree)

Figure 11.2.4 ACK magnitude of different object positions and sizes. Averaging band

is 0.5fo to L5fo. Reference angles are 0; = 20° and 0.1 = —20°. ¢ = 3.7 + 0.134. h =

0.18X5, | = LOAg, L = 409, g = L/4. (a) Various depth dependence d (xp = 0, a =
1.5Ao). (b) Various horizontal position dependence xp (d = 2A, @ = 1.59). (c) Various size
dependence a (xp =0, d= 2A).

3 Angular Correlation Function of Scattering by a Buried

> **第3节：掩埋目标散射的角相关函数**

Object Under a 2-D Random Rough Surface (3-D Scat-
tering)

3.1 Introduction

Since the practical problems involve a 3-D object buried under a 2-D rough

surface, a solution of electromagnetic wave scattering from a 2-D random

rough surface with a 3-D buried object is needed. To speed up the solution
of surface integral equations for rough surface with MoM, fast computational
methods of Chapters 5 and 6 are used.

Angular correlation functions are obtained by taking averages over a
product of two signals. Thus, a key step of calculating the ACF is taking
averages. For random media scattering, the average is usually taken over
realizations of random media or rough surfaces, which is not applicable for
--- PAGE 583 ---
§3.2 Formulation of Integral Equations 565
the detection of the object buried under a rough surface. For 2-D scatter-
ing problems of a target embedded in clutter in Section 2, we have used
frequency averaging and zenith angular averaging to obtain the ACF in Sec-
tion 2. Numerical results have shown that detection of targets by the ACF
with frequency and angular averaging has advantages over the radar cross
section (RCS). Since the scattering characteristics of the object is frequency
dependent, the frequency averaging may smear the result. In this section, we
study 3-D scattering. In 3-D scattering, there is an additional degree of free-
dom, that of varying the azimuthal angle. Therefore, we will use azimuthal
angular averaging instead.

We study electromagnetic wave scattering by a 3-D buried object un-
der a 2-D random rough surface. We formulate the problem based on the
Stratton-Chu surface integral equations for the rough surface and the surface
of the object. Next the scattered wave fields from the object onto the rough
surface are treated as additional incident fields on the rough surface. Then,
the SMCG method is used for the solution of the matrix equation. Numerical
results are calculated for a perfectly conducting sphere under the rough sur-
face. Both the ACF and scattering coefficient are calculated. To take averages
of the statistical results, we use azimuthal averaging. It is found that ACF is
more effective in suppressing the effects of the rough surface scattering. Also,
for 3-D scattering, we have cross-polarization. We utilize angular correlation
and polarization correlation together giving the PACF (Polarization-angular
correlation function). It is shown that the cross-polarization components of
ACF can be more useful than co-polarization components for the detection
of the buried object.

3.2. Formulation of Integral Equations
Consider an electromagnetic wave with fields E'(a,y,z) and H(a,y, 2) im-
pinging on a 2-D rough surface with a random height profile z = f(x,y).
Above the rough surface is a free space (region 0} while the subsurface is
characterized by permittivity ¢; and permeability jx (region 1). The incident
direction is &; = sin 0; cos ¢i# + sin 6; sin dif — cos 6;3. The incident electric
and magnetic fields are given as

00 Foc

E (a,y,2) = / dky [ dky exp(ikyx + ikyy — ikzz)Ej(kx, ky)
—0o Joe
- [aT Pe(—k,) + a7 h(—ks)] (11.3.1)
--- PAGE 584 ---
566 11 ACF AND DETECTION OF BURIED OBJECT
_ 1 ste 00
F'(a,y,2) = ‘| dkiz [ dky exp(ikea + ikyy — ikez) i(k, ky)
1 J—co Joo
-[-a™ i(k.) +a™e(—k.)] (11.3.2)
where (a?” = 1,a!™ = 0) indicates incident TE (horizontal) polarization
while (a7 = 0,a!™ = 1) indicates TM (vertical polarization). The polar-
ization unit vectors é(—kz) and (—k-) are as defined in (2.1.18) of Volume 1.
In (11.3.1) and (11.3.2), Ej(k2, ky) is the spectrum of the incident wave.
We use the following spectrum
1 +00 +00
Ei(kes ky) => | de | dyexp(—ikea — ikyy)
An? Jie —0o
x exp(i(Kiew + kiyy)(L + w)) exp(—t) (11.3.3)
where t = ty + ty = (a? + y*)/g? and
(cos 6; cos da + cos 6; sin diy)?
t; = orev 3.4
m a oos? 8, (11.3.4)
ty= (- antes cos Py)” (11.3.5)
pa 2 [Cte , Cty-D F
w=p [S ata, te (11.3.6)
The parameter g controls the tapering of the incident wave. The tapering is
done in the spectral domain.

We apply Stratton-Chu surface integral equations on the rough surface
and the surface of the buried object. The boundary conditions for the di-
electric rough surface are

Ax Ey =AXE, AxH=axH
sone an — (11.3.7)
eon: Eg=ein- Fy, pon-Ho = n+ Ay
By using fo = p41, we use Stratton-Chu equations approaching from both
sides of the rough surface and the boundary conditions. Let BE; and Hy
denote the scattered fields from the buried target. The integral equations on
the rough surface are, with 7 on the rough surface
aE a
aE = nee) -a. / al x H@)iwpogodS!
+ f {(a! x BG) x V'go + V gon’ - F@)}as' (11.3.8)
IS,
--- PAGE 585 ---
§3.2 Formulation of Integral Equations 567
_ Ax H(F —
ax (r= An tO) ax i/ —iwi! x E()eogodS!
+f {i x H(r’)) x Vigo +i! - APY was (11.3.9)
Se
ax Er) = x0 -Aax [/ iwn x HP) ugids!
+ f {(al x Br) x V gi + (a! EP)AV a)\as)
S, ‘0
(1.3.10)
_ A. HF f —
-a- He = ie) -A- i/ -Al x E(P)iwergids!
+f {(a! x H(r)) x Vg t Vig’: Heys (11.3.11)
S,
where the integral f represents the principal-value integral, S, is the rough
surface, and go and gy are the scalar Green’s function in region 0 (air) and
region 1, respectively
exp (ikoR) exp (ik R)
= al = 11.3.
90 TR and gy ick (1.3.12)
The distance between a field point 7 and a source point 7 is R =
V@~2' P+ (y-v')? + (Fey) ~ fa WP.

In Eqs. (11.3.10) and (11.3.11), EZ} and Hj, are scattered fields from the
buried object onto the rough surface. They are calculated as follows.

We assume that the buried object is a perfectly conducting sphere. It is
convenient to use the magnetic field integral equation (MFIE) to solve the
surface current on the object. For an exciting ficld of 17; incoming on the
buried object, the MFIE for the surface current J, = i x H), on the buried
object is

fy x HF) = 2) — thy x [ Tir’) x V' gids! (11.3.13)
2 Js,
where the unit normal vector of the surface of the buried object is A», and
Sy is the surface of the buried object. In (11.3.13), the exciting field of Hj,
for the buried object is the scattered field from the rough surface, ic.
fy x Hi(P) = — fin x | [-a" x B@)iwerg + (a! x HP) x Vin
S,
$V nai: T@)| ds! (1.3.14)
--- PAGE 586 ---
568 11 ACF AND DETECTION OF BURIED OBJECT
The right hand sides of (11.3.13) and (11.3.14) are to be equated with F on
Sy. Then, the scattered fields from the buried object are expressed in terms
of the surface current as

Hy?) = [ Ty(r) x V' gids! (11.3.15)

Sy
Fir) = —v x [ Th(r") x V' gids! (11.3.16)
Wey Js,

The expressions of (1.3.15) and (11.3.16) are substituted in (1.3.10)
and (11.3.11) for * on §S,. Equations (11.3.8)-(11.3.11) combined with
(11.3.13)-(11.3.16) constitute the coupled integral equations between the
rough surface and the buried object. There are six equations in (11.3.8)-
(11.3.11), two equations in (11.3.13)-(11.3.14). Equations (11.3.15) and
(11.3.16) are to be substituted into the left hand sides of (11.3.10) and
(11.3.11). The unknowns are the six field components on the rough surface
and the components of the surface current on the object.

To solve the coupled integral equations, we discretize the rough surface
and the surface of the object into small patches. For a patch at the rough
surface, we use 6 knowns for the surface fields as follows:

JF) =7x E,(F) + (11.3.17)

J(F) =7 x E.(F) (11.3.18)

Jg(F) =7- E,.(7) (113.19)

IF) =x H,(F)-& (1.3.20)

IsF) = Tx Hy) -G (1.3.21)

Je(F) = 7- H,.(7) (11.38.22)
where 7 is on S,.

Using the above definitions for unknowns and the MoM, Eggs. (11.3.8)—

(11.3.11) become a matrix equation as

ZI =bi+b, (1.3.23)
where the impedance matrix of rough surface is Z, }; represents incident
fields, and by represents scattered fields from the buried object.

Let Z, be the impedance matrix for the buried object, Z,» be impedance
matrix that characterize scattering from the buried object to the rough sur-
face, and Z,, be the impedance matrix that characterize scattering from the
rough surface to the buried object. Let the surface currents on the buried
object be

Ju(F) = fig x Hy (7) (11.3.24)
--- PAGE 587 ---
§3.2 Formulation of Integral Equations 569
Ion (F) = ty x HF) (11.3.25)
Jog (F) = thy x Hy (7) 2 (11.3.26)
where F is on S}. From Eqs. (11.3.15)-(11.3.16) , we have
by = Zod (1.3.27)
From (11.3.13), we have
T, =2ZsTs (1.3.28)
where 7; is the column vector that represents the values of iy x HF) on
8p, and from (1.3.14)
Ty = Zod (11.3.29)
Thus
, S232 63 Ss S's -
bp = Zr» Jy = 25 Zy Jy = 2 rp Zy Zor J (11.3.30)
We assume that the number of buried object surface unknowns is far less
than that of the rough surface so that calculating the inverse of Z, does not
present large CPU requirement. Substituting Eq. (11.3.30) into (11.3.23), we
get
see's u :
(Z-Zyy Z, Zor) J = bj (11.3.31)
To speed up the solution of Eq. (11.3.31), we decompose the impedance
matrix for the rough surface Z into three parts: a’block Toeplitz flat-surface
sFs =s =W
part Z_, strong interaction part Z , and the weak remainder Z_ . Thus
Ss = sFs sw
Z=Z 47°42 (11.3.32)
With the weak remainder part moved to the right-hand side, we have
sFS s8 = = 15 = + sw
(Z +2 -ZyZ, Zt =b:-Z I (1.3.33)
For a small object, the solution of Eq. (11.3.33) can be further speeded
up by moving the buried object term to the right-hand side,
sFS =sS_ _ Ss S15 — SW
(Z 42 )J=b+ ZZ, ZyJI-Z I (1.3.34)
The matrix equation is then iteratively
sFS <8 _ -
(Z +7 )I =i (11.3.35)
si r s Sls - sw
BY) <5 4 ZyZ, Lyd -Z I” (11.3.36)
sFs sS =|
(Zora Z yy) — perv (11.3.37)
--- PAGE 588 ---
570 11 ACF AND DETECTION OF BURIED OBJECT
for n = 0,1,2,.... Equations (11.3.35) and (11.3.37) are solved by conju-
gate gradient method (CGM). We also use the sparse matrix canonical grid
=W_ s(FS) =
method to calculate Z J”. The product of Z”” with J can be com-
puted using a 2-D fast FFT algorithm as described in Chapter 6. Updating
the right-hand side is also quickly calculated. In the numerical calculations
shown in Section 3.4, the iteration is terminated when the error norm crite-
rion is less than 0.2%.
3.3 Statistics of Scattered Fields
After the surface currents are solved, the scattered fields in medium 0 can be
calculated. The scattering amplitudes for both the co-polarized and cross-
polarized polarizations F3, are respectively
ik
Fhoa = eel da'dy! exp(—iky’ Iv xx’, y’) cos A, COS bs
ho = TP ds, iy exp(-iky') |) Ji(a’,y') cos 8s cos s
Of(2!.y!
+ Ja(a',y’) cos, sin 8, — Hat. AS w) sin 8,
Ox
Of(x'.y! .
— da’, yytew sin as} —n{ Ja(a’,y') sin ds — J5(x",y’) cos 6]
y
(1.3.38)
and
ik
Fug = == | dz'dy' ex ~iky)[ J) 2’, y') sin bg ~ Joa", y') cos ¢.
va ane lh, y' exp(—iky’)| {Ji(2’,y’) 2(2',y') cos ds}
Of(a'.y!
+n{Ja(a’, y’) cos 05 cos bs + Js cos 0, sin, — Ja(a’, jen sind,
of (a',y’)
= Jo(x! yA sino.) 11.38.39
(a's yl) 5 Ge sin Bs} (11.3.39)
where 7/ = w'sin®,cos¢; + y’ sin 8s sings + f(2',y') cos Os. The scattering
amplitudes in (11.3.39) are normalized by the square root of the incident
power 27Piq where
a ad , k, 44
Pia 7 | Ap dkey| Bio (Ke, By)? 7 (11.3.40)
ky<k
As discussed in Section 2, since the buried object is under a single ran-
dom rough surface, the realization averaging that is usually done in random
rough surface scattering simulations is not applicable. In the numerical re-
sults, both the bistatic scattering coefficient (normalized RCS) and ACF are
--- PAGE 589 ---
§3.4 Numerical Ilustrations of ACF and PACF 571
calculated based on azimuthal averaging. Let Ng be the number of azimuthal
angles. The bistatic scattering coefficient is
No
1 : :
O50 (8s,9:) = <= D_|Faa (Bs; bsni Gi, in)! (11.3.41)
Now
and
No
1 7 *
Per(8s25 6125 As1, 8:1) = 5 YS. Fea (O02, 6:20; 0:2; bia) Figa(Ie1 Pains Air, Gi1m)
Ve nel
(1.3.42)
where ¢in and gp are incident and scattering azimuthal angles. In the scat-
tering plane, they are related to each other by the relations of (i) dsn = din
for 6, having the same sign as 6;, (ii) den = ¢in + 180° for 6, having an
opposite sign of 6;.

For 6, having the same sign as 6;, the scattering is in the forward di-
rection, and we have set ¢sn = din. We also let the two incident @’s to be
the same, @ian = din. The azimuthal averaging over @’s means that we keep
the source and receiving directions on opposite sides of the scattering plane
and rotating both by the same amount in the azimuthal direction. For 6,
having the opposite sign as 6;, the scattering is in the backward direction.
We set den = din + 180°, meaning that the source and the observation are in
the same side of the scattering plane. Azimuthal averaging means rotating
source and observation by the same amount in the azimuthal direction.

Equation (11.3.42) can be extended to calculate the polarization-
angular correlation function (PACF) as follows

T'3,021 8202 (951, G11; O52, 4:2)
1
“Ne SP Fra.ay (851, Pstni 9:1 Gin) Fhe (8521 @s2n} 912, Gian) (11.3.43)
P n=l
Equation (11.3.43) inchaides effects of both angular correlations and polar-
ization correlations.
3.4 Numerical Illustrations of ACF and PACF

> **3.4 ACF与PACF的数值示例**

The numerical simulation is conducted for a perfectly electrical conductor
(PEC) sphere buried under a 2-D Gaussian random rough surface. The rough
surface is generated by using the spectrum method with an assumption of a
Gaussian spectrum. The sizes of the rough surface in the # and y directions
are Ly = Ly = 8.0). The surface rms heights are hy = hy = 0.02A, and
the correlation lengths are 1, = ly = 0.5. The relative dielectric constant of
--- PAGE 590 ---
572 11 ACF AND DETECTION OF BURIED OBJECT
ae
FAN
AEE ZA
‘\ : ‘ ays VANe
Xi ><] <M
VAAN NN
TOONS)
NO SX)
VAAL UZ™ YO AAI
Vi NA 7 If \]
a an 4 DW
Q Ss ANA
NAB G
Figure 11.3.1  Discretization of a sphere into 80 triangle patches.
the lower medium is ¢, = (2.0 + 10.2). The surface is sampled at 64 points
per 2 giving 4096 points on the rough surface and 24576 surface unknowns.
The neighborhood distance in the implementation of SMCG is rg = 3.5).
The sphere of radius of a = 0.3A is buried under the rough surface at a
depth of d = 0.6. The sphere surface is discretized into 80 triangle patches
as shown in Fig. 11.3.1 for which the surface currents are represented by
240 unknowns. The impedance matrix of the sphere Z, is calculated and
tested by calculating the scattering cross section of a sphere in free space.
The numerical results agree with that obtained by Mie scattering as shown
in Fig. 11.3.2.

We solve the matrix equations with the buried object contribution on
the left-hand side (11.3.33) and that on the right side (11.3.34). Both give
the same result. The scattering coefficients are shown in Fig. 11.3.3. The
CPU with the target term on the right-hand side is five times faster than
the CPU with the target term on the left-hand side.

We calculate the scattering amplitudes for 10 azimuthal angles at 0°,
36°,..., and 324°, respectively. There is only one realization of the random
rough surface. The RCS and ACF are calculated by using azimuthal angular
averaging as given in Eq. (11.3.41) and (11.3.42). We plot the results as
functions of the scattering angle 6.9. Parameters for other angles are 6;, =
20°, 05, = —40°, and @j2 = 20°. The memory line is at 6.2 = —40° which
shows a moderate peak for the ACF without the target. Figure 11.3.4 shows
the results for hh polarization component. Both the results with and without
--- PAGE 591 ---
§3.4 Numerical Ilustrations of ACF and PACF 573
wo Bistatic Scattering by a PEC Sphere (a0.96)
ae
SS oN ee
NE |
5 Nw _
5 ~ ae
3 Nf
\
NU
a Mie
___: MoM -
i
10590 ao 6080009216) F80
scattering angle (degree)
Figure 11.3.2 Comparison of MoM and Mie scattering for the radar cross section of a
PEC sphere.
the target sphere are shown for comparison. Figure 11.3.4b is for RCS. As
expected, there is a peak in the specular direction, which is due to the slightly
rough surface. The difference of RCS with and that without the target is large
only for large scattering angles, since the rough surface scattering is small
in these cases. As shown in Fig. 11.3.4a, however, the difference of ACF can
be 7dB, even for angles closed to the nadir direction. This is because the
memory effect is avoided and rough surface scattering is minimized in the
ACF.

The fully polarimetric results of RCS and ACF are calculated and shown
in Figs. 11.3.5 and 11.3.6. Figure 11.3.5 shows the results of RCS. We see
that the differences of RCS between with and without the target for co-
polarizations are larger than those for cross-polarizations. This is because
the cross-polarization components are mainly due to the rough surface scat-
tering. Because the target is a sphere, it has only a small cross-polarization
contribution in RCS. It is also found that there are larger differences for the
vv component than for the hk component, since the vertical polarization
wave has better penetration through the rough surface. Figure 11.3.5 shows
the results of ACF. We can sec the large difference of ACF between with and
without a target in both the co-polarization and cross-polarization result.
--- PAGE 592 ---
574 il ACF AND DETECTION OF BURIED OBJECT
10° sn a
an |
_: Lett side f \ |
t = Right side | \ q
wos fo 1
2 H \
Ed ' \
i
10° /™ i NX
LYNN ~\
\ \
y, V\ \
10% \
10° . — re
100-80 «60-40-20 sCiSC‘i SCC
Scattering angle (degree)
Figure 11.3.3 Comparison between the solution of the matrix equation for the target
object term on left-hand side and that on right-hand side.
5 ACF (20-40)
10) a '
tot so
10°} eT tea = 22S with Target ~
weet” =: Without Target a
ww «0 4 2 o ™ 4 6 0
scattering angle (degree)
5 Res
10
[ ( .
2 f \
10 A \
2 A Nn
@ ee Se
os eas With Target —
ae no Target |
ws 60 4 2 0 2 4 6 60
‘catering angle (degree)
Figure 11.3.4 ACF and RCS of EM wave scattering by a PEC sphere buried under a
2D rough surface for hh polarization component. Parameters are: @ = 0.3A, d = 0.6;
Lz = Ly = 80d, h = 0.02A, le = ly = 0.5, rq = 3.5A, 641 = 20°, 851 = —40°, and
4; = 20°. Solid line with target; dashed line without target
--- PAGE 593 ---
§4 ACF Correlation Imaging 575
hh pol w pol
10° — 10° T
j \ ji 4
w) oe we
for? \ a NN
ety oy \ « fy v\
tor) 1} {
si! on :
a) 0 50 eo S0 0 50
scattering angle (degree) scattering angle (degree)
4 vh pol 4 by pol.
2 a |
"| fe Sy 10° fe SS i
/; \ A \
Bie 4’ \ Bigs) /o! \
gL \ gir / }
/ Vy
10" 10"
i’ i
10°! ne 10°
-50 0 50 50 0 50
‘scattering angle (degree) scattering angle (degree)
Figure 11.3.5 RCS of EM wave scattering by a PEC sphere buried under a 2-D rough
surface for co-pol. and cross-pol. components. Parameters are: a = 0.3A, d = 0.64; Le =
Ly = 8.0d, h = 0.02A, le = ly = 0.5A, rg = 3.5A, Oj = 20°, 851 = —40°, and Aj2 = 20°.
Solid line with target; dashed line without target.
This is because of the random phase of rough surface scattering that causes
cancellation in the ACF calculation. The results of polarization-angular cor-
relation function (PACF) are also calculated and shown in Fig. 11.3.7. Fig-
ure 11.3.7a is the PACF between hh components and vk components. Figure
11.3.7b is the PACF between vv components and hv components. We can
see an even larger difference up to 10 to 20dB. This is due to the fact that
the PACF of rough surface scattering has little polarization correlation.
4 Angular Correlation Function Applied to Correlation

> **第4节：角相关函数在相关成像中的应用**

Imaging in Target Detection
4.1 Introduction
SAR imaging is an important topic in remote sensing [Soumekh, 1996; Ax-
elsson, 1995]. Resolution and signal-to-noise ratio are two important criteria.
in image processing. A radar system of fine resolution usually requires high
operating frequency. At high frequencies, however, waves are also scattered
by clutter such as rough surface and random media, causing low signal-noise
--- PAGE 594 ---
576 11 ACF AND DETECTION OF BURIED OBJECT
2 hh pol. 2 w pol.
10° 10? —
| feor\ | fer
ji *
orp | —/) \\
r \ 14
S10 vo . Sit, vs - .
, wed / 4
10°} U7 . | 10°} sy
Fe wet!
-50 0 50 -50 0 50
scattering angle (degree) scattering angle (degree)
vh pol. hy pol.
10° ——_—__ 10° eee
5 | 5
107+ 10
| Na fT A a
aoe, OY OS goal “0 ONS
(en v NS .
Q10 J ~ s Q10 / .
boos i! el
107; 7 ¥ 107 ¢
tl ee
-50 0 50 -50 0 50
scattering angle (degree) scattering angle (degree)
Figure 11.3.6 ACF of EM wave scattering by a PEC sphere buried under a 2-D rough
surface for co-pol. and cross-pol. components. Parameters are: @ = 0.3\, d = 0.6\; Ly =
Ly =8.0A, h = 0.02, Le = Ty = 0.52, rg = B.5A, 01 = 20°, Og, = —40°, and Ajo = 20°
ratio. Therefore, developing data processing methods that would give fine
resolution and effective clutter suppression is an important goal.

Imaging is to obtain the detailed information from a wide-band and a
large range of angular measurements. The conventional SAR imaging method
can be called field imaging, in which the target function is obtained from the
measured fields by inverse Fourier transform {Soumekh, 1996] or by focusing
[Axelsson, 1995; Moore, 1996]. The focusing method is also called correlation
imaging since the field is correlated with a reference signal. The focusing
method was described in Chapter 6, Section 2 of Volume I for linear and
circular SAR. The field focusing method can be improved by introducing
filter function such as matched filtering if the scattering property of the
target is known [Moore, 1996]. However, if the target scattering function is
not known, the matched filtering method cannot be applied. In this section,
--- PAGE 595 ---
§4.1 Introduction 577
5 PACF (hhvh)
10” - Ln 7
a / \
to" _ _ / wa 1
pee i ee
x10 petty lett e! _
10° _ a _-_! With Target Verte
~ —--+! Without Target
10” —
80-60-4020 ty 2 440 «660 =~ 80
scattering angle (degree)
PACF (why)
10° — 2
4 ’ , j
"0 —— —-_—_"
woof / sl
210° . woe 5, —
= UN a? .
10° 7 “V : With Target ae
; ae =: Without Target
40 i a rr
80 60-40-20 0 20 «402~=COOs«O
scattering angle (degree)
Figure 11.3.7 PACF of EM wave scattering by a PEC sphere buried under a 2-D rough
surface between co-pol. and cross-pol. components. Parameters are: a = 0.3A, d = 0.6);
Lz = Ly = 80d, h = 0.02A, le = ly = 0.5A, rq = 3.5d, O11 = 20°, Oy. = —40°, and
6:2 = 20°. (a): hhvh, (b) vwhv.
we study the ACF imaging method that is based on the calculation of mutual
correlation function of two received signals at two different angles.

Correlation imaging is to calculate the correlation function with focusing
on every position in a region and then a image is obtained for the entire
yegion. The memory effect of the mutual correlation function for random
scattering is avoided. The correlation imaging uses the phase difference (or
sum) of two wave propagation paths, while the field imaging is to use the
phase of one path. Therefore, correlation imaging uses a larger spectrum
domain information which gives a finer resolution and can suppress clutter.
The correlation imaging can be realized by calculating angular correlation
function (ACF), frequency correlation function (FCF), and the combination
of both frequency angular correlation function (FACF).

In this section, we perform numerical simulations of SAR imaging. In
Section 4.2, we discuss the fundamentals of correlation imaging. The sim-
ilarities and differences between field imaging and correlation imaging are
compared. Then, in Section 4.3, the angular correlation imaging method is
--- PAGE 596 ---
578 11 ACF AND DETECTION OF BURIED OBJECT
illustrated by using Monte Carlo simulations for circular SAR and linear
SAR. Circular SAR gives finer resolution and better signal-clutter ratio of
100%. For linear SAR, it is found that the frequency angular correlation
imaging gives better performance.
4.2 Formulation of Imaging

> **4.2 成像公式化**

Imaging is to obtain the detailed information of a region by measuring the
scattered field from many view angles and frequencies. Under the far-ficld
approximation, the received signal is a set of data E(k) which can be written
as
E(k) = [ -ReFar (11.4.1)
where k = kj — ky is the difference between the incident wave vector kj
and the scattered wave vector ky. Thus, k is a function of frequency and
view angle. The target function f(r,k) is generally frequency and angular
dependent. _ _
In the ideal case, f(7,k) is not dependent on k. Thus
FB © fal?) (114.14)
Then in this ideal case, the target function is the inverse Fourier transform
of received signals.
=). 1 h) ik? ap
fal?) = Go [BW dk (1.4.2)
A second way to obtain the target function is by focusing. The received
signal £(k) is correlated with a reference response E, focused on Fy. From
Eq. (6.2.25) of Chapter 6, Volume 1,
1 es ra
Cr(Fo) = ay | PERE (11.4.3)
ns
Putting (11.4.1) in (11.4.3) and using E, = 1, we have
1 _ ar a
Cr(Fo) = om | “ / Arf) Bye" = fialFo) (11-4)
We will use the notation that
= 1 ot \
(w(k)) p= an | w(k) (11.4.5a)
where (---)z denotes an averaging over k space. For functions that are de-
pendent on two E vectors
—— 1 - — es
(w(ba Fading, = eye f tbr f tha wh Fo) (11.458)
--- PAGE 597 ---
§4.2 Formulation of Imaging 579

This operation can be interpreted as spectrum averaging, with Ey named
the filter function.

Both methods (inverse Fourier transform and focusing) of finding target
function in (11.4.2) and (11.4.3) are based on the received field, which we
shall call field imaging.

In correlation imaging, we calculate the correlation function of two re-
ceived signals. We further perform focusing by spectrum averaging as

Co(Fo) = (ER ew 7+ B* Rael ye 5,

1 - 1 — co —~. pa
_ dik = enti Fo EX (fey) etka Fo A
Qn [e Gas | Fopeve (ka)e (11.4.6)
Putting (11.4.1) in (11.4.6), we have, for the ideal case
Cr(Fo)

1 - 1 ik Fo ike ¥. _ \ ik F, pe fe Teo F
"as | hs af thre tks To gtk */ a fiaFie™ of arate tha Ta
= far f arasatra sal2)5(%s —7.)8(r2 Fo) = |falFo) (ALA)
Thus ideally, Cr(¥,) gives | fia(Fo)|?- The correlation imaging can be related
to frequency angular correlation function of scattering.

We shall show that correlation imaging also has better performance for
the nonideal case when f(7,k) is dependent on k.

First, we let k =k, and kg = ko — ky. Then

1 — on / er a
Cr(Fo) = Oa [ca [ ckEG Ee + Raethere (11.4.8)
The frequency angular correlation function is
< eee 1 me
Va(ka) = (E(R)E*(k + ka) )g = oF / dkE(k)E*(k + ka) (11.4.9)
Using (11.4.9) in (11.4.8), we have
OF E\eikeFoy — 1 ET (E,\oikeFo
Cr(Fo) = (Valkalen )g, = oa dkaV (kale (11.4.10)
Tu (ka) is known as the frequency angular correlation function (FACF) of
scattering. Note that in (11.4.9), we have taken the averaging over hk to
obtain T'g(ka)-

For random media scattering, very often, averaging is taken over real-

izations
Par(Fa) = (E(E)E* (K + ka))reatization (114.11)
--- PAGE 598 ---
580 11 ACF AND DETECTION OF BURIED OBJECT.
For the case of realization averaging, the angular correlation function (ACF)
of scattering by random media (clutter) has been studied. It has been shown
in Section 2 that the scattering by random media does not contribute to
AGF except along the memory directions of kg = 0. That is, the ACF of
random scattering is small except for ky = 0.

For imaging purpose, random scattering can be minimized by avoid-
ing the memory effect by choosing kg # 0. We next define a more general
expression for correlation imaging function by generalizing (11.4.6)

w(F,) = z, f Teo ET Jo 72k RU) 7

Cr(Fo) = One [% [tee Gve (e)—Fo
+ E* (ka )ehel Ra) Fol Wy (Ry: Ba) (1.4.12)
where R(k) and R(k2) are distances between the focusing position and
the receiver positions. In Eq. (11.4.12), W(k1;k2) is a weighting function,
which can be chosen to further suppress clutter effect if the clutter scattering
characteristics are known. We shall assume that it is equal to unity for

simplicity. We will use (11.4.8) to process (simulated) SAR data.

The correlation imaging may be done by calculating angular correlation
function (ACF), frequency correlation function (FCF) and frequency angular
correlation function (FACF). The central idea. of correlation imaging is to
use a large phase difference for focusing and to avoid the memory effect. so
that clutter is suppressed. The large phase difference, however, may not be
obtained using ACF imaging in some practical problems, like linear SAR.
Tn this case, frequency angular correlation imaging (FACF imaging) gives
better performance. In practice, the integration in (11.4.12) is discretized
and approximated by finite sums.

4.3 Simulations of SAR Data and ACF Processing

> **4.3 SAR数据模拟与ACF处理**

Tn this section, we use the Monte Carlo simulations of wave scattering to
simulate SAR data. Then we use ACF to process the simulated SAR data.

Consider an incident wave impinging upon the targets that are embed-
ded in random medium (Fig. 11.4.1). Let the incident wave be given by

E,(ki,F) = ef 7 (1.4.13)
where 7; is antenna position, 7 is field position.

In the numerical simulation, the random medium is modeled by a collec-
tion of randomly distributed small scatterers. Let the scattering amplitude
of the targets be denoted by Fin(ks,ki), n = 1,2,...,N, where N, is the
number of targets. Let fn(kis, ki) be the scattering amplitude of the small
--- PAGE 599 ---
§4.3 Simulations of SAR Data and ACF Processing 581
H
H ]
ES AT OVER
REESE asc | fro h cB i
Pig i ay fomrnmrn Noes (aoa Vesa
[Me MEY (xs BEY
fa) (b)
Figure 11.4.1 Confignrations of SAR. imaging for targets embedded in small scatterers.
(a) Circular SAR, (b) linear SAR.
random scatterers with n = 1,2,...,N, where N, is the number of small
scatterers.
Assuming single scattering, the scattered field at the receiver is given by
Noo _.
E(B, B) = > REI Fie RE D-Fale, (hey,fe)
n=1
Np | _.
+ Soe RE Dt) FR) Fol 6. (yey) (14.1)
n=1
where the received field is expressed in terms of the scattering amplitude
of the targets Fj,(k) and the scattering amplitudes of randomly distributed
particles f,,(k)

In this manner, we generate the simulated data of the scattered field for
many combinations of incident and scattered field directions and frequencies.
Next we describe how correlation imaging is used to process the simulated
circular SAR and the linear SAR data.

Circular SAR Imaging

Let a mono-static radar be moving along a circular path of radius of R, and
at height H above the target region (Figure 11.4.1a). The radar position is
a function of the azimuthal angle ¢ as R(¢) = R, cos d% + Ry sin dy + Hz.
--- PAGE 600 ---
582 11 ACF AND DETECTION OF BURIED OBJECT
We write the total scattered field at the radar
Ni 8 Ny
E(k, 6) = So PRO —Pol Fy (ke) + > eM NRO—Tel fh) (1.4.15)
n=1 n=1
where the received signal is expressed in terms of the scattering amplitude
of targets F),(k) and the scattering amplitudes of randomly distributed par-
ticles fr(k) (n = 1,2,---,Np). The factor of 2 in the phase accounts for the
round trip phase shift for a monostatic radar.

The conventional SAR imaging, which we call field imaging, can be
realized by correlating the received signal with a reference signal E, and
then summing over frequency and angle. From (11.4.3),

Ne Ne oo
Ce (Fo) = YY. Blin, bn) je Pn lRO)-Fa (114.16)
matn=1
‘The reference signal FE, is chosen to be a constant. As shown in (11.4.3)-
(11.4.4), (11.4.16) las well defined peaks when F, approaches the location
of the scatterers. To have a fair comparison with ACF imaging which is
proportional to the square of the signal, we also take the absolute valued
square of (11.4.16). That is
Cor(Fo) = |Cr(Fo)|? (1.4.17)
The result of (11.4.16)-(11.4.17) is known as field imaging. Next we caleu-
late ACF imaging. The ACF imaging is to correlate two signals received at
different, angles and to sum over frequency and angles. From (11.4.12),
Ne No Ne _
Coo) = YF dF LE Elina bn, Je Mel Mod Toh
m=1ny=1 ng=1noeni
.E* (Kins Gang) ez RlOna2) Fol (1.4.18)
Note that the integrand in (11.4.10) is the angular correlation function. The
memory effect of random scattering is avoided by ng # m1. In practical
simulations, we let [ny —n| > N, instead of just no # nq in (1.4.18) so that
the angular difference ¢¢ = |@n, — én.| is larger than the correlation angle of
the angular correlation function. The choice of N, depends on the correlation
angle of random scattering. The correlation angle of random scattering is
usually small, which is in the order of A/Z where L is the size of the medium.
By having |nz—,| > No, only a small portion of information is removed for
the target. Therefore, target information is essentially preserved in (11.4.18)
while the clutter due to random scattering is significantly suppressed.
--- PAGE 601 ---
§4.3 Simulations of SAR Data and ACF Processing 583

In the numerical simulations, 80,000 small particles with radius of a =
0.044, are used to mode} clutter. They are randomly distributed in a layer
region of 40\, x 40A, x 0.5A,. Four target spheres with radius of a =
0.3A, are placed at positions of (10,14,0)A,, (10,28,0)\., (30,10,0),, and
(30,32,0)A,. The dielectric constant of both the targets and the small par-
ticles are (3.23+i0.36). All distances are in terms of the wavelength A,
of the center frequency. The circular path of the receiver has a radius of
R, = 1732A, at height of H = 1000A,. The backscattering amplitudes for
targets and particles are calculated based on Mie scattering. The received
signal is calculated by Eq. (11.4.14). The frequency band is from 0.5f, to
1.5f. with an increment of 0.01 f,. Thus N; = 100, ky = 0.5f,, ko = 0.51fo,
..+, etc. The azimuth angle is from 0° to 360° at an interval of 3.6 degrees.
Thus Ng = 100, 41 = 0°, ¢2 = 3.6°, @3 = 7.2°, ete.

The simulated data is processed by field imaging and ACF imaging.
The results are normalized by the maximum of the target. The normalized
results are shown in Fig, 11.4.2 and 11.4.3. Figure 11.4.2 shows the results
of the square of (11.4.16), i.c., the results of (11.4.17) of field imaging. The
4 targets are spread out to a two wavclength size and are obscured by the
background clutter. Figure 11.4.3 shows the results of ACF imaging. We sce
that the spot size of targets is smaller, which is a result of finer resolution.
The background clutter is significantly suppressed. We use the condition of
in] — ng| > 5, ie., No = 5, to ensure that the angular pairs 6,, and @p,
are away from the memory dot. The better performance of ACF imaging is
due to (1) the clutter effect is minimized by avoiding the memory effect of
random scattering and (2) the spreading due to the frequency dependence of
scattering is compensated by the cross-range resolution in ACF imaging. The
angular correlation function with focusing (ACF focusing) is also shown in
Fig, 11.4.4. The ACF focusing Cr(Fo, 0a) is obtained by using Eq. (11.4.18)
with the summation over vee , replaced by nz = 1 + na, as given by

NM Ne _

Cr(Fo,ba) = Y> YO Elkins one eo) Fel

m=ln=l

+ B* (Rims Oneng eRe Hn vad Fel (11.4.19)
Therefore, ACF imaging is the summation over many images of ACF fo-
cusing. Because ACI focusing is a random function of correlation angle ¢q
when 7, is not at a target. Comparing (11.4.18) and (11.4.19), we note that
the clutter is further suppressed by having one more averaging in (11.4.18)
than in (11.4.19).
--- PAGE 602 ---
584 11 ACF AND DETECTION OF BURIED OBJECT
fats maging
bed os
_— 06
oa
Figure 11.4.2 Simulated image of targets embedded in clutter by field imaging for circular
SAR
ACF imaging
b os
Zz |
) o4
Figure 11.4.3 Simulated image of targets embedded in clutter by ACF imaging for circular
SAR
--- PAGE 603 ---
§4.3 Simulations of SAR Data and ACF Processing 585
ACF focusing
'
} 4 os
|
4
os
o4
02
0
Figure 11.4.4 Simulated image of targets embedded in clutter by ACF focusing for circular
SAR.
Linear SAR Imaging
For linear SAR as shown in Fig. 11.4.1, a monostatic radar moves along
a linear path at height H above the target region. The radar position is
function of the antenna position x as R(x) = «x — dj + Hz. Therefore, the
received signals can be written as
Nt Ne Np a
E(k, x) = > eH R)-Fal Fen (k) + D> eR) —Fol p(k) (1.4.20)
n=l n=l
where the received signal is a function of wave number k (frequency) and
antenna position x.
The field imaging is to correlate the received signal with a reference
signal E, and then sum over frequency k,, and azimuthal position 2,,.
MN. Ne -
Cr(Fo) = >> > Elk; tn) Eo(km)°e~ 2! Me=)-Fel_ (1.4.21)
m=1n=1
and
Cor (Fo) = |Cr(Fo)|? (11.4.216)
In the numerical simulations, the reference signal E, is chosen to be unity
--- PAGE 604 ---
586 11 ACF AND DETECTION OF BURIED OBJECT
for simplicity. The correlation defined above has well defined peaks when 7,
approaches the locations of the scatterers.

It was shown that in circular SAR, the angular correlation imaging can
give clear images. On the other hand, in linear SAR, spatial correlation
imaging gives fine cross-range resolution and frequency correlation imaging
gives fine range resolution. In general, frequency spatial correlation will give
better performance in correlation imaging for linear SAR. The frequency
angular correlation function (FACF) imaging is defined by

Ne Ne Ne Ne _
Cro) = LLL DBs hra Bn) Pl
mi=1m=lme=l n=l ba> Kk
E* (Ray Png) eral Rena) Fol (11.4.22)
The memory effect is avoided in the summation by choosing kg > K. The
magnitude of the difference of the two wave vectors kg is given by
hea = (km, C08 $1 Sin Oy ~ kms COS G2 Sin A)”
+ (km, sin @1 sin #1 — km, sin d2 sin 2)
1/2
+ (Ky, 0801 — km, €08 82)”] (114.23)
where the angular pairs (61,01) and (02,2) are the orientation angles for
vectors Rap, )--F, and R(an,)—Fo, respectively. In the numerical simulations
of correlation focusing, kg is chosen to be larger than k,/16, ie., kg > K =
4s where ko is the conter wave number. Equation (11.4.22) reduces to FCF
imaging with ng = m, and to ACF imaging by letting mz = m,. The FCF
imaging is then given by
‘ Ne Ne Ne _
WFCF) 2th. ‘n)—Fo
CEO) = S22 YS Bb tne Billed
n=tmy=l mo=lka>K
+ E* (keg, tn )e*Rm al Rn) Fol (1.4.24)
and ACF imaging is written as
Ne Ns Ne _
Ce(Fo) = > > > E (Kins tn, Joven R@n) Fel
m=1n=1 n2=1,ka>K
+ B* (km, tn, etm Ren, )—Fol (1.4.25)

For the numerical simulations of linear SAR imaging, 80,000 small par-
ticles are used to model clutter. They are randomly distributed in a layer re-
gion of 40A, x40A, x0.5A,. Four targets are placed at positions of (10,14,0)A.,
--- PAGE 605 ---
§4.3 Simulations of SAR Data and ACF Processing 587
(10,28.0)A;, (30,10,0)A,, and (30,32,0)A,. The dielectric constant of the tar-
gets and the scatterers are equal to (3.23 + 70.36). The back-scattering am-
plitudes for the targets and the particles are calculated based on Mie scat-
tering. The receiver moves from 7, = —d/2 to xs = d/2 with an increment
of d/100. The horizontal position is ys = d with d = 1732A, and the height
is z; = H = 1000A,. The received signal is calculated over a frequency band
0.5f, to 1.5 fo with an increment of 0.01f, and 100 azimuthal positions with
equal space.

The simulated data is processed by the methods of field imaging and
FACF imaging. The normalized results are shown in Fig. 11.4.5, and 11.4.6.
Figure 11.4.5 shows field imaging of Cyp({F,) = |Cy(F,)|?. The 4 targets are
obscured by the background clutter. Figure 11.4.6 shows the results of FACF
imaging with the memory effect avoided, which has lower clutter level than
that in Fig. 11.4.5. The results of FCF imaging and ACF imaging are also
shown in Fig. 11.4.7 and 11.4.8. We sce that ACF imaging loses range reso-
lution and FCF does not have good cross-range resolution. Therefore, FACF
imaging gives better performance than ACF imaging and FCF imaging for
linear SAR.

To compare results quantitatively, we define the visibility of targets in
clutter as a ratio of target signal and the average signal strength for the
entire image covering the region. The visibility is calculated by

v= —Max(Go))) (11.4.26)
/ rel.) / / iF,
In Eq. (11.4.26). the numerator corresponds to the J of the targets, and the
denominator is the mean value of background clutter.

The visibility of targets in clutter for images shown in Figs. 11.4.2, 11.4.3,
11.4.5 and 11.4.6 are calculated. We find that correlation imaging gives bet-
ter visibility than the conventional field imaging. The image in Fig. 11.4.3
obtained for the ACF imaging has a visibility of 2 times that of field imaging
shown in Fig. 11.4.2. The visibility of the image in Fig. 11.4.6 of FACF is
1.3 times that in Fig. 11.4.5. The results are summarized in Table 11.4.1

Tain
192
Table 11.4.1 Comparison of visibility of target in clutter.
--- PAGE 606 ---
588 11 ACF AND DETECTION OF BURIED OBJECT
fats maging
06
Cs ' :
Figure 11.4.5 Simulated image of targets embedded in clutter by field imaging for linear
SAR
FACE maging
r os
Ee ' :
02
Figure 11.4.6 Simulated image of targets embedded in clutter by FACF imaging for linear
SAR
--- PAGE 607 ---
§4.3 Simulations of SAR Data and ACF Processing 589
FCF enagng
'
be os
{
WG
:
12
‘
Figure 11.4.7 Simulated image of targets embedded in clutter by FCF imaging for linear
SAR
ACK wnageg
} 5
Oe os
i ,
2
Figure 11.4.8 Simulated image of targets embedded in clutter by ACF imaging for linear
SAR
--- PAGE 608 ---
590 11 ACF AND DETECTION OF BURIED OBJECT

From the formulation and numerical results, we found that correlation
imaging gives better results for the detection of targets embedded in clut-
ter than field imaging when the size of random particles is smaller than a
wavelength. For the same received signals, the image obtained by correlation
imaging has a finer resolution and a larger signal-clutter ratio than that by
ficld imaging. This is because the clutter effect is minimized in correlation
imaging by avoiding the memory effect of random scattcring. It is shown that
the clutter effect can be substantially reduced for both circular and lincar
configurations. In a similar manner, a 3-D image can be obtained with fo-
cusing on different layers. The frequency dependence can be compensated by
using a weighting function. The image processing algorithm can be speeded
up by using FFT with the far-field approximation for the phase.
--- PAGE 609 ---
REFERENCES 591
REFERENCES AND ADDITIONAL READINGS

Axelsson, S. (1995), Frequency and azimuth variation and their influence upon low-frequency
SAR imaging, JEEE Trans. Geosci. Remote Sens., 83, 1258-1265.

Rerkovits, R., M. Kaveh, and S. Feng (1989), Memory effect: of waves in disordered systems:
a real-space approach, Phys. Rev. B, 40, 737-740.

Berkovits, R. and §. Feng (1994), Correlations in coherent multiple scattering, Phy. Rep.,
238, 135-172.

Chan, 'T-K., Y. Kuga, and A. Ishimaru (1999), Experimental studies on circular SAR imaging
in clutter using angular correlation function technique, IEEE Trans. Geosci. Remote
Sens., 37(5), 2192-2197.

Chan, T-K., Y. Kuga, and A. Ishimaru (1997), Subsurface detection of a buried object using
angular correlation function measurement, Waves in Random Media, 7(3), 457-465.

Chan, T-K., Y. Kuga, and A, Ishimaru (1996), Angular memory effect of millimeter-wave
scattering from two-dimensional conducting random tough surfaces, Radio Sci., 31,
1067-1076.

Feng, S., C. Kane, P, A. Lee, and A. D, Stone (1988), Correlations and fluctuations of coherent
wave transmission through disordered media, Phys. Rev. Lett., 61, 834-837.

Freund, [. (1990), Correlation imaging through multiply scattering media, Phys. Lett. A,
147(8/9), 502-506.

Freund, L., M. Rosenbluh, and S. Feng (1988), Memory effects in propagation of optical waves
throngh disordered media, Phys. Rev. Lett., 61, 2328-2331.

Kawanishi, T., Z. L. Wang, M. Izutsu, H. Ogura (1999), Conjugate memory effect of random
scattered waves, J. Opt. Soc. Am. A, 16, 1342-1349.

Knotts, M. E., T. R. Michel, and K. A. O'Donnel) (1992), Angular correlation functions of
polarized intensities scattered from a one-dimensionally rough surface, J. Opt. Soc. Am.
A, 9, 1882-1831.

Kuga, Y.,C. 1. C. Le, A. Ishimaru, and L, Ailes-Sengers (1996), Analytical experimental, and
mumerical studies of angular memory signatures of waves scattered from one-dimensional
rongh surfaces, IEEE Trans. Geosci. Remote Sens., 34, 1300-1307.

Le, C. T. G., ¥. Kuga, and A. Ishimarn (1996), Angular correlation function based on the
second-order Kichhoff approximation and comparison with experiments, J. Opt. Soc.
Am. A, 13, 1057-1067.

Lu, J. Q. and Z. H. Gu (1997), Angular correlation function of speckle patterns scattered
from a one-dimensional rough dielectric film on a glass substrate, Appl. Optics, 36,
4562-4570.

Michel, ‘T. R. and K. A. O'Donnell (1992), Angular correlation functions of amplitudes seat-
tered from a one-dimensional, perfectly conducting rongh surface, J. Opt. Soc, Am. A,
9(8), 1374-1384,

Moore (1996), A new algorithm for the formation of ISAR images, [EEE Trans. Aerosp.
Electron. Syst., 32(2), 714-721.

Nieto-Vesperinas, M. and J. M. Soto-Crespo (1987), Monte-Carlo simulations for scattering
of electromagnetic waves from perfectly conducting random rough surfaces, Optics Lett.,
12, 979-981

ONeill, K. (2000), Broadband bistatic coherent and incoherent detection of buried objects
beneath randomly rough surfaces, IEEE Trans. Geosci. Remote Sens., 38(2), 891-898.
--- PAGE 610 ---
592 11 ACF AND DETECTION OF BURIED OBJECT

Sarahandi, K. and A. Nashashibi (1999), Analysis and applications of backscattered frequency
correlation function, INE Trans. Geosci. Remote Sens., 37, 1895-1906.

Tsang, L., G. Zhang, and K. Pak (1996), Detection of a buried object under a single random
rough surface with angular correlation function in EM wave scattering, Microwave Opt.
Technol. Lett., 11(6), 300-304. Corrections to “Detection of a buried object under a
single random rough surface with angular correlation function in EM wave scattering” ,
Microwave Opt. Technol. Lett., 12, 375.

Soumekh, M. (1996), Reconnaissance with slant plant circular SAR imaging, JEEE Trans.
Image Processing, 35, 45-51.

Soumekh, M. (1999), Synthetic Aperture Radar Signal Processing with MATLAB Algorithms,
Wiley-Interscience, New York.

Zhang, G. and L,, ‘Tsang (1997), Angular correlation function of wave scattering by a random
rough surface and discrete scatterers and its application in the detection of a buried
object, Waves in Random Media, 7(3), 467-478.

Zhang, G, and L. Tsang (1998), Application of angular correlation function of clutter scat-
tering and correlation imaging in target detection, JEEE Trans. Geosci. Remote Sens.,
36, 1485-1493.

Zhang, G., L. Tsang, and Y. Kuga (1997a), Studies of the angular correlation function of
scattering by random rough surfaces with and without a buried object, IEEE Trans.
Geosci. Remote Sens., 35, 444-453.

Zhang, G., L. Tsang, and Y. Kuga (1997b), The angular correlation function of wave seatter-
ing by a buried object embedded in random discretic scatterers under a random rough
surface, Microwave Opt. Technol. Lett., 14, 144-151.

Zhang, G., L.. Tsang, and Y. Kuga (1998a), Numerical studies of the detection of targets em-
bedded in clutter by using angular correlation functions and angular correlation imaging,
Microwave Opt, Technol. Lett., 17(2), 82-86.

Zhang, G., L. Tsang, and K. Pak (1998b), Angular correlation function and scattering coef-
ficients of electromagnetic waves scattered by a buried object under a two-dimensional
rough surface, J. Opt. Soc. Am. A, 15(12), 2995-3002.
--- PAGE 611 ---
Scattering of Electromagnetic Waves: Numerical Simulations.
Leung Tsang, Jin Au Kong, Kung-Hau Ding, Chi On Ao.
Copyright © 2001 John Wiley & Sons, Inc,
ISBNs; 0-471-38800-9 (Hardback); 0-471-22430-8 (Hlectronic)

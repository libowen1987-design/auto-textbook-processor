# Sadiku《Elements of Electromagnetics》Chapter 12

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 660-709 of 926 (926 total)

---

## Waveguides

633
C H A P T E R
633
12.1  INTRODUCTION
As mentioned in the preceding chapter, a transmission line can be used to guide EM
energy from one point (generator) to another (load). A waveguide is another means of
achieving the same goal. However, a waveguide differs from a transmission line in some
respects, although we may regard the latter as a special case of the former. In the first place,
a transmission line can support only a transverse electromagnetic (TEM) wave, whereas
a waveguide can support many possible field configurations. Second, at microwave fre­
quencies (roughly 3–300 GHz), transmission lines become inefficient as a result of skin
effect and dielectric losses; waveguides are used at that range of frequencies to obtain
larger bandwidth and lower signal attenuation. Moreover, a transmission line may oper­
ate from dc 1 f 5 0 Hz2 to a very high frequency; a waveguide can operate only above a
certain frequency called the cutoff frequency and therefore acts as a high-pass filter. Thus,
waveguides cannot transmit dc, and they become excessively large at frequencies below
microwave frequencies.
Although a waveguide may assume any arbitrary but uniform cross section, common
waveguides are either rectangular or circular. Typical waveguides1 are shown in Figure 12.1.
Analysis of circular waveguides is involved and requires familiarity with Bessel functions,
which are beyond our scope.2 We will consider only hollow rectangular waveguides. By
assuming lossless waveguides 1sc . `, s < 02, we shall apply Maxwell’s equations with
the appropriate boundary conditions to obtain different modes of wave propagation and
the corresponding E and H fields. When we close both ends of a waveguide, a cavity is
formed. We will also consider optical fiber guide, which is basic to optical communications.
WAVEGUIDES
Reading makes a full man; conference makes a ready man; and writing makes an
accurate man.
—ANONYMOUS
1 For other types of waveguides, see J. A. Seeger, Microwave Theory, Components and Devices. ­Englewood Cliffs,
NJ: Prentice-Hall, 1986, pp. 128–133.
2 Analysis of circular waveguides can be found in advanced EM or EM-related texts (e.g., S. Y. Liao,
Microwave Devices and Circuits, 3rd ed. Englewood Cliffs, NJ: Prentice-Hall, 1990, pp. 119–141).
634  CHAPTER 12  WAVEGUIDES
Consider the rectangular waveguide shown in Figure 12.2, where a and b are the inner
dimensions of the waveguide. We shall assume that the waveguide is filled with a source-
free 1rv 5 0, J 5 02 lossless dielectric material 1s . 02 and that its walls are perfectly
conducting 1sc . `2. From eqs. (10.17) and (10.19), we recall that for a lossless medium,
Maxwell’s equations in phasor form become
=2Es 1 k2Es 5 0
(12.1)
=2Hs 1 k2Hs 5 0
(12.2)
FIGURE 12.2  A rectangular wave­
guide with perfectly conducting walls,
filled with a lossless material.
FIGURE 12.1  Typical waveguides.
12.2  RECTANGULAR WAVEGUIDES
12.2 Rectangular Waveguides  635
where
k 5 v !me
(12.3)
and the time factor e jt is assumed. If we let
Es 5 1Exs, Eys, Ezs2  and  Hs 5 1Hxs, Hys, Hzs2
each of eqs. (12.1) and (12.2) comprises three scalar Helmholtz equations. In other words,
to obtain the E and H fields, we have to solve six scalar equations. For the z-component,
for example, eq. (12.1) becomes
'2Ezs
'x2 1 '2Ezs
'y2 1 '2Ezs
'z2 1 k2Ezs 5 0
(12.4)
which is a partial differential equation. From Example 6.5, we know that eq. (12.4) can be
solved by separation of variables (product solution). So we let
Ezs1x, y, z2 5 X1x2 Y1y2 Z1z2
(12.5)
where X(x), Y(y), and Z(z) are functions of x, y, and z, respectively. Substituting eq. (12.5)
into eq. (12.4) and dividing by XYZ gives
X 1 Ys
Y 1 Zs
Z 5 2k2
(12.6)
Since the variables are independent, each term in eq. (12.6) must be constant, so the equa­
tion can be written as
2k2
x 2 k2
y 1 g2 5 2k2
(12.7)
where 2k2
x, 2k2
y, and 2 are separation constants. Thus, eq. (12.6) is separated as
Xs 1 k2
xX 5 0
(12.8a)
Ys 1 k2
yY 5 0
(12.8b)
Zs 2 g2Z 5 0
(12.8c)
The choice of 2 is due to the realization that the guided waves propagate along the guide
axis z in the positive or negative direction, and the propagation may result in Ezs and Hzs
that approach zero as z S 6`.
By following the same argument as in Example 6.5, we obtain the solution to eq. (12.8) as
X1x2 5 c1 cos kxx 1 c2 sin kxx
(12.9a)
Y1y2 5 c3 cos kyy 1 c4 sin kyy
(12.9b)
Z1z2 5 c5egz 1 c6e2gz
(12.9c)
636  CHAPTER 12  WAVEGUIDES
Substituting eq. (12.9) into eq. (12.5) gives
Ezs1x, y, z2 5 1c1 cos kxx 1 c2 sin kxx2 1c3 cos kyy
1 c4 sin kyy2 1c5egz 1 c6e2gz2
(12.10)
As usual, if we assume that the wave propagates along the waveguide in the 1z-direction,
the multiplicative constant c5 5 0 because the wave has to be finite at infinity [i.e.,
Ezs1x, y, z 5 `2 5 0]. Hence eq. (12.10) is reduced to
Ezs1x, y, z2 5 1A1 cos kxx 1 A2 sin kxx2 1A3 cos kyy 1 A4 sin kyy2e2gz
(12.11)
where A1 5 c1c6, A2 5 c2c6, A3  c3c6, and A4  c4c6. By taking similar steps, we get the
solution of the z-component of eq. (12.2) as
Hzs1x, y, z2 5 1B1 cos kxx 1 B2 sin kxx2 1B3 cos kyy 1 B4 sin kyy2e2gz
(12.12)
Instead of solving for other field components Exs, Eys, Hxs, and Hys in eqs. (12.1) and (12.2)
in the same manner, it is more convenient to use Maxwell’s equations to determine them
from Ezs and Hzs. From
= 3 Es 5 2jvmHs
and
= 3 Hs 5 jveEs
we obtain
'Ezs
'y 2
'Eys
'z 5 2jvmHxs
(12.13a)
'Hzs
'y 2
'Hys
'z 5 jveExs
(12.13b)
'Exs
'z 2 'Ezs
'x 5 2jvmHys
(12.13c)
'Hxs
'z 2 'Hzs
'x 5 jveEys
(12.13d)
'Eys
'x 2 'Exs
'y 5 2jvmHzs
(12.13e)
'Hys
'x 2 'Hxs
'y 5 jveEzs
(12.13f)
We will now express Exs, Eys, Hxs, and Hys in terms of Ezs and Hzs. For Exs, for example,
we combine eqs. (12.13b) and (12.13c) and obtain
12.2 Rectangular Waveguides  637
jveExs 5 'Hzs
'y 1
jvm a'2Exs
'z2 2 '2Ezs
'x'zb
(12.14)
From eqs. (12.11) and (12.12), it is clear that all field components vary with z according to
e2gz, that is,
Ezs ,  e2gz,  Exs ,  e2gz
Hence
'Ezs
'z 5 2gEzs,  '2Exs
'z2 5 g2Exs
and eq. (12.14) becomes
jveExs 5 'Hzs
'y 1
jvm ag2Exs 1 g'Ezs
'x b
2 1
jvm 1g2 1 v2me2 Exs 5
jvm 'Ezs
'x 1 'Hzs
Thus, if we let h2 5 g2 1 v2me 5 g2 1 k2,
Exs 5 2 g
h2 'Ezs
'x 2
jvm
h2  'Hzs
Similar manipulations of eqs. (12.13) yield expressions for Eys, Hxs, and Hys in terms of Ezs
and Hzs. Thus,
Exs 5 2 g
h2 'Ezs
'x 2
jvm
h2  'Hzs
Eys 5 2
'Ezs
'y 1
jvm
'Hzs
Hxs 5
jve
'Ezs
'y 2 g
'Hzs
Hys 5 2
jve
h2  'Ezs
'x 2 g
h2 'Hzs
(12.15a)
(12.15b)
(12.15c)
(12.15d)
where
h2 5 g2 1 k2 5 k2
x 1 k2
(12.16)
638  CHAPTER 12  WAVEGUIDES
Thus we can use eqs. (12.15) in conjunction with eqs. (12.11) and (12.12) to obtain Exs, Eys,
Hxs, and Hys.
From eqs. (12.11), (12.12), and (12.15), we notice that the field patterns or configura­
tions come in different types. Each of these distinct field patterns is called a mode. Four
­different mode categories can exist, namely:
1.	 Ezs 5 0 5 Hzs (TEM mode): In the transverse electromagnetic mode, both the E
and H fields are transverse to the direction of wave propagation. From eq. (12.15),
all field components vanish for Ezs 5 0 5 Hzs. Consequently, we conclude that a
hollow rectangular waveguide cannot support TEM mode.
2.	 Ezs 5 0, Hzs 2 0 (TE modes): For this case, the remaining components (Exs and
Eys) of the electric field are transverse to the direction of propagation az. Under this
condition, fields are said to be in transverse electric (TE) modes. See Figure 12.3(a).
3.	 Ezs 2 0, Hzs 5 0 (TM modes): In this case, the H field is transverse to the direc­
tion of wave propagation. Thus we have transverse magnetic (TM) modes. See
Figure 12.3(b).
4.	 Ezs 2 0, Hzs 2 0 (HE modes): In this case neither the E nor the H field is trans­
verse to the direction of wave propagation. Sometimes these modes are referred to
as ­hybrid modes.
We should note the relationship between k in eq. (12.3) and b of eq. (10.43a). The phase
constant b in eq. (10.43a) was derived for TEM mode. For the TEM mode, h 5 0, so from
eq. (12.16), g2 5 2k2 S  g 5 a 1 jb 5 jk; that is, b 5 k. For other modes, b 2 k. In
the subsequent sections, we shall examine the TM and TE modes of propagation separately.
FIGURE 12.3  Components of EM fields in a rectangular waveguide:
(a) TE mode Ez 5 0, (b) TM mode, Hz 5 0.
12.3  TRANSVERSE MAGNETIC MODES
For the TM case, the magnetic field has its components transverse (or normal) to the direc­
tion of wave propagation. This implies that we set Hz 5 0 and determine Ex, Ey, Ez, Hx, and
Hy by using eqs. (12.11) and (12.15) and the boundary conditions. We shall solve for Ez
and later determine other field components from Ez. At the walls (perfect conductors) of
12.3 Transverse Magnetic Modes  639
the ­waveguide in Figure 12.2, the tangential components of the E field must be continuous;
that is,
Ezs 5 0   at   y 5 0        (bottom wall)
(12.17a)
Ezs 5 0   at   y 5 b        (top wall)
(12.17b)
Ezs 5 0   at   x 5 0        (right wall)
(12.17c)
Ezs 5 0   at   x 5 a        (left wall)
(12.17d)
Equations (12.17a) and (12.17c) require that A1 5 0 5 A3 in eq. (12.11), so eq. (12.11)
­becomes
Ezs 5 Eo sin kxx sin kyy e2gz
(12.18)
where Eo 5 A2A4. Also eqs. (12.17d) and (12.17b) when applied to eq. (12.18) require,
respectively, that
sin kxa 5 0,  sin kyb 5 0
(12.19)
This implies that
kxa 5 mp,   m 5 1, 2, 3, . . .
(12.20a)
kyb 5 np,   n 5 1, 2, 3, . . .
(12.20b)
kx 5 mp
a ,  ky 5 np
b 
(12.21)
The negative integers are not chosen for m and n in eq. (12.20a) for the reason given in
­Example 6.5. Substituting eq. (12.21) into eq. (12.18) gives
Ezs 5 Eo sin ampx
b sin a
npy
b b e2gz
(12.22)
We obtain other field components from eqs. (12.22) and (12.15), bearing in mind that
Hzs 5 0. Thus
Exs 5 2 g
h2 amp
a b Eo cos ampx
b sin a
npy
b b e2gz
(12.23a)
Eys 5 2 g
h2 anp
b b Eo sin ampx
b cos a
npy
b b e2gz
(12.23b)
Hxs 5
jve
h2  anp
b b Eo sin ampx
b cos a
npy
b b e2gz
(12.23c)
Hys 5 2
jve
h2  amp
a b Eo cos ampx
b sin a
npy
b b e2gz
(12.23d)
640  CHAPTER 12  WAVEGUIDES
where
h2 5 k2
x 1 k2
y 5 c mp
a d
1 c np
b d
(12.24)
which is obtained from eqs. (12.16) and (12.21). Notice from eqs. (12.22) and (12.23)
that each set of integers m and n gives a different field pattern or mode, referred to as
TMmn mode, in the waveguide. Integer m equals the number of half-cycle variations in the
x-direction, and integer n is the number of half-cycle variations in the y-direction. We also
notice from eqs. (12.22) and (12.23) that if 1m, n2 is 10, 02, 10, n2, or 1m, 02, all field com­
ponents vanish. Thus neither m nor n can be zero. Consequently, TM11 is the lowest-order
mode of all the TMmn modes.
By substituting eq. (12.21) into eq. (12.16), we obtain the propagation constant
g 5 Å cmp
a d
1 c np
b d
2 k2
(12.25)
where k 5 v !me as in eq. (12.3). We recall that, in general, g 5 a 1 jb. In the case of
eq. (12.25), we have three possibilities depending on k (or ), m, and n:
CASE 1 (cutoff)
k2 5 v2me 5 c mp
a d
1 c np
b d
g 5 0
a 5 0 5 b
The value of  that causes this is called the cutoff angular frequency c; that is,
vc 5
!me Å c mp
a d
1 c np
b d
(12.26)
No propagation takes place at this frequency.
CASE 2 (evanescent)
k2 5 v2me , c mp
a d
1 c np
b d
g 5 a,
b 5 0
In this case, we have no wave propagation at all. These nonpropagating modes are said to
be evanescent.
12.3 Transverse Magnetic Modes  641
CASE 3 (propagation)
k2 5 v2me . c mp
a d
1 c np
b d
g 5 jb,        a 5 0
that is, from eq. (12.25) the phase constant b becomes
b 5 Åk2 2 c mp
a d
2 c np
b d
(12.27)
This is the only case in which propagation takes place, because all field components will
have the factor e2gz 5 e2jbz.
Thus for each mode, characterized by a set of integers m and n, there is a correspond­
ing cutoff frequency fc .
The cutoff frequency is the operating frequency below which attenuation occurs and
above which propagation takes place.
The waveguide therefore operates as a high-pass filter. The cutoff frequency is obtained
from eq. (12.26) as
fc 5 vc
2p 5
2p"me
Å cmp
a d
1 c np
b d
fc 5 ur
2  Å am
a b
1 an
(12.28)
where ur 5
"me
5 phase velocity of uniform plane wave in the lossless dielectric
­medium 1s 5 0, m, e2 filling the waveguide. The cutoff wavelength lc is given by
lc 5 ur
lc 5
Å am
a b
1 an
(12.29)
642  CHAPTER 12  WAVEGUIDES
Note from eqs. (12.28) and (12.29) that TM11 has the lowest cutoff frequency (or the longest
cutoff wavelength) of all the TM modes. The phase constant b in eq. (12.27) can be written
in terms of fc as
b 5 v !me Å1 2 c
f d
b 5 br Å1 2 c
f d
(12.30)
where br 5 v/ur 5 v !me 5 phase constant of uniform plane wave in the dielectric
medium. It should be noted that g for evanescent mode can be expressed in terms of
fc, namely,
g 5 a 5 br Å a
f b
2 1
(12.30)
The phase velocity up and the wavelength in the guide are, respectively, given by
up 5 v
br, l 5 2p
b 5
f 
(12.31)
The intrinsic wave impedance of the mode is obtained from eq. (12.23) as 1g 5 jb2
hTM 5 Ex
5 2
5 b
ve 5 Å
e Å1 2 c
f d
hTM 5 hr Å1 2 c
f d
(12.32)
where hr 5 !m/e is the intrinsic impedance of a uniform plane wave in the medium.
Note the difference between u, b, and h, and u, b, and h. The primed quantities are
wave characteristics of the dielectric medium unbounded by the waveguide, as dis­
cussed in Chapter 10 (i.e., for TEM mode). For example, u would be the velocity of the
wave if the waveguide were removed and the entire space were filled with the dielectric.
The unprimed quantities are the wave characteristics of the medium bounded by the
­waveguide.
12.4 Transverse Electric Modes  643
As mentioned before, the integers m and n indicate the number of half-cycle varia­
tions in the x–y cross section of the guide. Thus for a fixed time, the field configuration of
­Figure 12.4 results for TM21 mode, for example.
End view
Side view
FIGURE 12.4  Field configuration for TM21 mode.
12.4  TRANSVERSE ELECTRIC MODES
In the TE modes, the electric field is transverse (or normal) to the direction of wave
propagation. We set Ez 5 0 and determine other field components Ex, Ey, Hx, Hy, and
Hz from eqs. (12.12) and (12.15) and the boundary conditions just as we did for the TM
modes. The boundary conditions are obtained from the requirement that the tangential
components of the electric field be continuous at the walls (perfect conductors) of the
waveguide; that is,
Exs 5 0   at   y 5 0
(12.33a)
Exs 5 0   at   y 5 b
(12.33b)
Eys 5 0   at   x 5 0
(12.33c)
Eys 5 0   at   x 5 a
(12.33d)
From eqs. (12.15) and (12.33), the boundary conditions can be written as
'Hzs
'y 5 0   at   y 5 0
(12.34a)
'Hzs
'y 5 0   at   y 5 b
(12.34b)
'Hzs
'x 5 0   at   x 5 0
(12.34c)
'Hzs
'x 5 0   at   x 5 a
(12.34d)
644  CHAPTER 12  WAVEGUIDES
Imposing these boundary conditions on eq. (12.12) yields
Hzs 5 Ho cos ampx
b cos a
npy
b b e2gz
(12.35)
where Ho 5 B1B3. Other field components are easily obtained from eqs. (12.35) and (12.15) as
Exs 5
jvm
h2  anp
b b Ho cos ampx
b sin a
npy
b b e2gz
(12.36a)
Eys 5 2
jvm
h2  amp
a b Ho sin ampx
b cos a
npy
b b e2gz
(12.36b)
Hxs 5 g
h2 amp
a b Ho sin ampx
b cos a
npy
b b e2gz
(12.36c)
Hys 5 g
h2 anp
b b Ho cos ampx
b sin a
npy
b b e2gz
(12.36d)
where m 5 0, 1, 2, 3, . . . ; and n 5 0, 1, 2, 3, . . . ; h and g remain as defined for the TM
modes. Again, m and n denote the number of half-cycle variations in the x–y cross section
of the guide. For TE32 mode, for example, the field configuration is in Figure 12.5. The cut­
off frequency fc, the cutoff wavelength lc, the phase constant b, the phase velocity up, and
the wavelength l for TE modes are the same as for TM modes [see eqs. (12.28) to (12.31)].
For TE modes, 1m, n2 may be 10, 12 or 11, 02 but not 10, 02. Both m and n cannot be
zero at the same time because this will force the field components in eq. (12.36) to vanish.
This implies that the lowest mode can be TE10 or TE01 depending on the values of a and
b, the dimensions of the guide. It is standard practice to have a . b so that 1/a2 , 1/b2 in
eq. (12.28). Thus TE10 is the lowest mode because fcTE10 5 ur
2a , fcTE01 5 ur
2b. This mode is
End view
Top view
FIGURE 12.5  Field configuration for TE32 mode.
12.4 Transverse Electric Modes  645
called the dominant mode of the waveguide and is of practical importance. The cutoff
­frequency for the TE10 mode is obtained from eq. (12.28) as 1m 5 1, n 5 02
fc10 5 ur
2a
(12.37)
and the cutoff wavelength for TE10 mode is obtained from eq. (12.29) as
lc10 5 2a
(12.38)
Note that from eq. (12.28) the cutoff frequency for TM11 is
ur3a2 1 b241/2
2ab
which is greater than the cutoff frequency for TE10. Hence, TM11 cannot be regarded as the
dominant mode.
The dominant mode is the mode with the lowest cutoff frequency (or longest cutoff
wavelength).
Also note that any EM wave with frequency f , fc10 1or l . lc102 will not be propagated
in the guide.
The intrinsic impedance for the TE mode is not the same as for TM modes. From
eq. (12.36), it is evident that 1g 5 jb2
hTE 5 Ex
5 2
5 vm
5 Å
Å1 2 c
f d
hTE 5
Å1 2 c
f d
(12.39)
Note from eqs. (12.32) and (12.39) that hTE and hTM are purely resistive and vary with
­frequency, as shown in Figure 12.6. Also note that
hTE hTM 5 hr2
(12.40)
Important equations for TM and TE modes are listed in Table 12.1 for convenience and
quick reference.
646  CHAPTER 12  WAVEGUIDES
ηTE
ηTM
FIGURE 12.6  Variation of wave
impedance with frequency for TE
and TM modes.
TABLE 12.1 Important Equations for TM and TE Modes
TM Modes
TE Modes
Exs 5 2
h2 amp
a b Eo cos ampx
b sin a
npy
b b e2gz
Exs 5
jvm
h2  anp
b b Ho cos ampx
b sin a
npy
b b e2gz
Eys 5 2
h2 anp
b b Eo sin ampx
b cos a
npy
b b e2gz
Eys 5 2
jvm
h2  amp
a b Ho sin ampx
b cos a
npy
b b e2gz
Ezs 5 Eo sin ampx
b sin a
npy
b b e2gz
Ezs 5 0
Hxs 5
jve
h2  anp
b b Eo sin ampx
b cos a
npy
b b e2gz
Hxs 5
h2 amp
a b Ho sin ampx
b cos a
npy
b b e2gz
Hys 5 2
jve
h2  amp
a b Eo cos ampx
b sin a
npy
b b e2gz
Hys 5
h2 anp
b b Ho cos ampx
b sin a
npy
b b e2gz
Hzs 5 0
Hzs 5 Ho cos ampx
b cos a
npy
b b e2gz
h 5 hrÅ1 2 a
f b
h 5
Å1 2 a
f b
fc 5 ur
2  Å am
a b
1 an
lc 5 ur
b 5 brÅ1 2 a
f b
up 5 v
b 5 fl
where h2 5 amp
a b
1 anp
b b
, ur 5
"me
, br 5 v
ur , hr 5 Å
12.4 Transverse Electric Modes  647
From eqs. (12.22), (12.23), (12.35), and (12.36), we obtain the field patterns for the TM
and TE modes. For the dominant TE10 mode, m 5 1 and n 5 0, so eq. (12.35) becomes
Hzs 5 Ho cosapx
a b e2jbz
(12.41)
In the time domain,
Hz 5 Re1Hzse jvt2
Hz 5 Ho cosapx
a b cos1vt 2 bz2
(12.42)
Similarly, from eq. (12.36),
Ey 5 vma
p  Ho sinapx
a b sin1vt 2 bz2
(12.43a)
Hx 5 2ba
p  Ho sinapx
a b sin1vt 2 bz2
(12.43b)
Ez 5 Ex 5 Hy 5 0
(12.43c)
FIGURE 12.7  Variation of the field components
with x for TE10 mode.
648  CHAPTER 12  WAVEGUIDES
The variation of the E and H fields with x in an xy-plane, say plane cos1vt 2 bz2 5 1 for
Hz, and plane sin1vt 2 bz2 5 1 for Ey and Hx, is shown in Figure 12.7 for the TE10 mode.
The corresponding field lines are shown in Figure 12.8.
FIGURE 12.8  Field lines for TE10
mode, corresponding to components
(a), (b), and (c) in Figure 12.7.
Top view
Side view
End view
EXAMPLE 12.1
A rectangular waveguide with dimensions a 5 2.5 cm, b 5 1 cm is to operate below 15.1
GHz. How many TE and TM modes can the waveguide transmit if the guide is filled with
a medium characterized by s 5 0, e 5 4 eo, mr 5 1? Calculate the cutoff frequencies of
the modes.
Solution:
The cutoff frequency is given by
fcmn 5 ur
2  Å
a2 1 n2
12.4 Transverse Electric Modes  649
where a 5 2.5b or a/b 5 2.5, and
ur 5
"me
"mr er
5 c
fcmn 5 3"m2 1 6.25n2 GHz
(12.1.1)
We are looking for fcmn , 15.1 GHz. A systematic way of doing this is to fix m or n and
increase the other until fcmn is greater than 15.1 GHz. From eq. (12.1.1), it is evident that
fixing m and increasing n will quickly give us an fcmn that is greater than 15.1 GHz.
For TE01 mode 1m 5 0, n 5 12, fc01 5 312.52 5 7.5 GHz
TE02 mode 1m 5 0, n 5 22, fc02 5 3152 5 15 GHz
TE03 mode, fc03 5 317.52 5 22.5 GHz
Thus for fcmn , 15.1 GHz, the maximum n 5 2. We now fix n and increase m until fcmn is
greater than 15.1 GHz.
For TE10 mode 1m 5 1, n 5 02, fc10 5 3 GHz
TE20 mode, fc20 5 6 GHz
TE30 mode, fc30 5 9 GHz
TE40 mode, fc40 5 12 GHz
TE50 mode, fc50 5 15 GHz 1the same as for TE022
TE60 mode, fc60 5 18 GHz
That is, for fcmn , 15.1 GHz, the maximum m 5 5. Now that we know the maximum m
and n, we try other possible combinations in between these maximum values.
For TE11, TM11 (degenerate modes), fc11 5 3"7.25 5 8.078 GHz
TE21, TM21, fc21 5 3"10.25 5 9.6 GHz
TE31, TM31, fc31 5 3"15.25 5 11.72 GHz
TE41, TM41, fc41 5 3"22.25 5 14.14 GHz
TE12, TM12, fc12 5 3"26 5 15.3 GHz
Hence,
fcmn 5 c
4a Åm2 1 a2
b2 n2
3 3 108
412.5 3 10222  "m2 1 6.25n2
650  CHAPTER 12  WAVEGUIDES
Those modes, whose cutoff frequencies are less than or equal to 15.1 GHz, will be
transmitted—that is, 11 TE modes and 4 TM modes (all the foregoing modes except TE12,
TM12, TE60, and TE03). The cutoff frequencies for the 15 modes are illustrated in Figure 12.9.
PRACTICE EXERCISE  12.1
Consider the waveguide of Example 12.1. Calculate the phase constant, phase velocity,
and wave impedance for TE10 and TM11 modes at the operating frequency of 15 GHz.
Answer:  For TE10, b 5 615.6 rad/m, u 5 1.531 3 108 m/s, hTE 5 192.4 V; for TM11,
b 5 529.4 rad/m, u 5 1.78 3 108 m/s, hTM 5 158.8 V.
FIGURE 12.9  Cutoff frequencies of rectangular waveguide
with a 5 2.5b; for Example 12.1.
EXAMPLE 12.2
Write the general instantaneous field expressions for the TM and TE modes. Deduce those
for TE01 and TM12 modes.
Solution:
The instantaneous field expressions are obtained from the phasor forms by using
E 5 Re 1Ese jvt2  and  H 5 Re 1Hse jvt2
Applying these to eqs. (12.22) and (12.23) while replacing g with jb gives the following
field components for the TM modes:
Ex 5 b
h2 c mp
a d  Eo cos ampx
b sin a
npy
b b sin 1vt 2 bz2
Ey 5 b
h2 c np
b d  Eo sin ampx
b cos a
npy
b b sin 1vt 2 bz2
Ez 5 Eo sin ampx
b sin a
npy
b b cos 1vt 2 bz2
12.4 Transverse Electric Modes  651
Hx 5 2ve
h2  c np
b d  Eo sin ampx
b cos a
npy
b b sin 1vt 2 bz2
Hy 5 ve
h2  c mp
a d  Eo cos ampx
b sin a
npy
b b sin 1vt 2 bz2
Hz 5 0
Similarly, for the TE modes, eqs. (12.35) and (12.36) become
Ex 5 2vm
h2  c np
b d  Ho cos ampx
b sin a
npy
b b sin 1vt 2 bz2
Ey 5 vm
h2  c mp
a d  Ho sin ampx
b cos a
npy
b b sin 1vt 2 bz2
Ez 5 0
Hx 5 2 b
h2 c mp
a d  Ho sin ampx
b cos a
npy
b b sin 1vt 2 bz2
Hy 5 2 b
h2 c np
b d  Ho cos ampx
b sin a
npy
b b sin 1vt 2 bz2
Hz 5 Ho cos ampx
b cos a
npy
b b cos 1vt 2 bz2
For the TE01 mode, we set m 5 0, n 5 1 to obtain
h2 5 c p
b d
Ex 5 2vmb
p  Ho sin a
b b sin 1vt 2 bz2
Ey 5 0 5 Ez 5 Hx
Hy 5 2bb
p  Ho sin a
b b sin 1vt 2 bz2
Hz 5 Ho cos a
b b cos 1vt 2 bz2
For the TM12 mode, we set m 5 1, n 5 2 to obtain
Ex 5 b
h2 ap
a b Eo cos apx
a b sin a
2py
b b sin 1vt 2 bz2
Ey 5 b
h2 a2p
b b Eo sin apx
a b cos a
2py
b b sin 1vt 2 bz2
Ez 5 Eo sin apx
a b sin a
2py
b b cos 1vt 2 bz2
652  CHAPTER 12  WAVEGUIDES
Hx 5 2ve
h2  a2p
b b Eo sin apx
a b cos a
2py
b b sin 1vt 2 bz2
Hy 5 ve
h2  ap
a b Eo cos apx
a b sin a
2py
b b sin 1vt 2 bz2
Hz 5 0
where
h2 5 c p
a d
1 c 2p
b d
EXAMPLE 12.3
PRACTICE EXERCISE  12.2
At 15 GHz, an air-filled 5 cm  2 cm waveguide has
Ezs 5 20 sin 40px sin 50py e2jbz V/m
(a)  What mode is being propagated?
(b)  Find b.
(c)  Determine Ey/Ex.
Answer:  (a) TM21,  (b) 241.3 rad/m,  (c) 1.25 tan 40px cot 50py.
In a rectangular waveguide for which a 5 1.5 cm, b 5 0.8 cm, s 5 0, m 5 mo, and
e 5 4eo,
Hx 5 2 sin apx
a b cos a
3py
b b sin 1p 3 1011t 2 bz2 A/m
Determine
(a)	 The mode of operation
(b)	 The cutoff frequency
(c)	 The phase constant b
(d)	 The propagation constant g
(e)	 The intrinsic wave impedance h
Solution:
(a)	 It is evident from the given expression for Hx and the field expressions in
Example 12.2 that m 5 1, n 5 3; that is, the guide is operating at TM13 or TE13. Suppose
we choose TM13 mode (the possibility of having TE13 mode is left as an exercise in
Practice ­Exercise 12.3).
12.4 Transverse Electric Modes  653
PRACTICE EXERCISE  12.3
Repeat Example 12.3 if TE13 mode is assumed. Determine other field components for
this mode.
Answer:   fc 5 28.57 GHz, b 5 1718.81 rad/m, g 5 jb, hTE13 5 229.69 V
Ex 5 2584.1 cos apx
a b sin a
3py
b b sin 1vt 2 bz2 V/m
Ey 5 2459.4 sin apx
a b cos a
3py
b b sin 1vt 2 bz2 V/m,  Ez 5 0
Hy 5 11.25 cos apx
a b sin a
3py
b b sin 1vt 2 bz2 A/m
Hz 5 27.96 cos apx
a b cos a
3py
b b cos 1vt 2 bz2 A/m
(b)
fcmn 5 ur
2  Å
a2 1 n2
ur 5
"me
"mrer
5 c
Hence
fc13 5 c
4 Å
31.5 3 102242 1
30.8 3 102242
5 3 3 108
1"0.444 1 14.062 3 102 5 28.57 GHz
(c)
b 5 v"me Å1 2 c
f d
5 v"er
Å1 2 c
f d
v 5 2pf 5 p 3 1011  or  f 5 1011
5 50 GHz
b 5 p 3 1011122
3 3 108
Å1 2 c 28.57
50 d
5 1718.81 rad/m
(d)
g 5 jb 5 j1718.81 /m
(e)
hTM13 5 hr Å1 2 c
f d
5 377
"er
Å1 2 c 28.57
50 d
5 154.7 V
654  CHAPTER 12  WAVEGUIDES
Examination of eq. (12.23) or (12.36) shows that the field components all involve the terms
sine or cosine of 1mp/a2x or 1np/b2y times e2gz. Since
sin u 5 1
2j 1e ju 2 e2ju2
(12.44a)
cos u 5 1
2 1e ju 1 e2ju2
(12.44b)
a wave within the waveguide can be resolved into a combination of plane waves reflected
from the waveguide walls. For the TE10 mode, for example,
Eys 5 2
jvma
p  sin apx
a b e2jbz
5 2vma
2p  1e jpx/a 2 e2jpx/a2 e2jbz
(12.45)
5 vma
2p  3e2jb1z1px/ba2 2 e2jb1z2px/ba24
where Ho  1. The first term of eq. (12.45) represents a wave traveling in the positive ­
z-­direction at an angle
u 5 tan21a p
bab
(12.46)
with the z-axis. The second term of eq. (12.45) represents a wave traveling in the positive
z-direction at an angle 2u. The field may be depicted as a sum of two plane TEM waves
propagating along zigzag paths between the guide walls at x 5 0 and x 5 a as illustrated
in Figure 12.10(a). The decomposition of the TE10 mode into two plane waves can be
extended to any TE and TM mode. When n and m are both different from zero, four plane
waves result from the decomposition.
The wave component in the z-direction has a different wavelength from that of the
plane waves. This wavelength along the axis of the guide is called the waveguide wavelength
and is given by
l 5
Å1 2 c
f d
(12.47)
where lr 5 ur/f .
As a consequence of the zigzag paths, we have three types of velocity: the medium
­velocity u, the phase velocity up, and the group velocity ug. Figure 12.10(b) illustrates the
relationship between the three different velocities. The medium velocity ur 5 1/!me is as
12.5  WAVE PROPAGATION IN THE GUIDE
12.5 Wave Propagation in the Guide  655
explained in the preceding sections. The phase velocity up is the velocity at which loci of
up 5 v
(12.48a)
up 5
cos u 5
Å1 2 c
f d
(12.48b)
This shows that up $ ur, since cos u # 1. If ur 5 c, then up is greater than the speed of
light in vacuum. Does this violate Einstein’s relativity theory that messages cannot travel
faster than the speed of light? Not really, because information (or energy) in a waveguide
generally does not travel at the phase velocity. Information travels at the group velocity,
which must be less than the speed of light. The group velocity ug is the velocity with which
the resultant repeated reflected waves are traveling down the guide and is given by
ug 5
'b/'v
(12.49a)
ug 5 ur cos u 5 ur Å1 2 c
f d
(12.49b)
Wave path
FIGURE 12.10  (a) Decomposition
of the TE10 mode into two plane
waves. (b) Relationship between
u, up, and ug.
constant phase are propagated down the guide and is given by eq. (12.31); that is,
656  CHAPTER 12  WAVEGUIDES
Although the concept of group velocity is fairly complex and is beyond the scope of this
chapter, a group velocity is essentially the velocity of propagation of the wave-packet enve­
lope of a group of frequencies. It is the energy propagation velocity in the guide and is
always less than or equal to u. From eqs. (12.48) and (12.49), it is evident that
upug 5 ur2
(12.50)
This relation is similar to eq. (12.40). Hence the variation of up and ug with frequency is
similar to that in Figure 12.6 for hTE and hTM.
EXAMPLE 12.4
A standard air-filled rectangular waveguide with dimensions a 5 8.636 cm, b 5 4.318 cm
is fed by a 4 GHz carrier from a coaxial cable. Determine whether a TE10 mode will be
propagated. If so, calculate the phase velocity and the group velocity.
Solution:
For the TE10 mode, fc 5 ur/2a. Since the waveguide is air filled, ur 5 c 5 3 3 108. Hence,
fc 5
3 3 108
2 3 8.636 3 1022 5 1.737 GHz
As f 5 4 GHz . fc, the TE10 mode will propagate.
up 5
"1 2 1 fc/f 2 2 5
3 3 108
"1 2 11.737/42 2
5 3.33 3 108 m/s
ug 5 ur2
5 9 3 1016
3.33 3 108 5 2.702 3 108 m/s
PRACTICE EXERCISE  12.4
Repeat Example 12.4 for the TM11 mode.
Answer:  12.5 3 108 m/s, 7.2 3 107 m/s.
To determine power flow in the waveguide, we first find the average Poynting vector [given
earlier as eq. (10.78)],
ave 5 1
2 Re1Es 3 H*s2
(12.51)
12.6 POWER TRANSMISSION AND ATTENUATION
12.6 Power Transmission and Attenuation  657
In this case, the Poynting vector is along the z-direction so that
where h 5 hTE for TE modes or h 5 hTM for TM modes. The total average power trans­
mitted across the cross section of the waveguide is
Of practical importance is the attenuation in a lossy waveguide. In our analysis thus
far, we have assumed lossless waveguides 1s 5 0, sc . `2 for which a 5 0, g 5 jb.
When the dielectric medium is lossy 1s 2 02 and the guide walls are not perfectly con­
ducting 1sc 2 `2, there is a continuous loss of power as a wave propagates along the
guide. According to eq. (10.79), the power flow in the guide is of the form
Pave 5 Poe22az
(12.54)
In general,
a 5 ac 1 ad
(12.55)
where ac and ad are attenuation constants due to ohmic or conduction losses 1sc 2 `2 and
dielectric losses 1s 2 02, respectively.
To determine ad, recall that we started with eq. (12.1) assuming a lossless dielectric
medium 1s 5 02. For a lossy dielectric, we need to incorporate the fact that s 2 0. All our
equations still hold except that g 5 jb needs to be modified. This is achieved by replacing
« in eq. (12.25) by the complex permittivity of eq. (10.40). Thus, we obtain
g 5 ad 1 jbd 5 Å amp
a b
1 anp
b b
2 v2mec
(12.56)
where
ec 5 er 2 jes 5 e 2 j s
(12.57)
Substituting eq. (12.57) into eq. (12.56) and squaring both sides of the equation, we obtain
g2 5 a2
d 2 b2
d 1 2jadbd 5 amp
a b
1 anp
b b
2 v2me 1 jvms
ave 5 1
2 Re1ExsH*ys 2 EysH*xs2 az
0 Exs 0 2 1 0 Eys 0 2
(12.52)
Pave 5 3 ave # dS
5 3
x50
y50
0 Exs 0 2 1 0 Eys 0 2
dy dx
(12.53)
658  CHAPTER 12  WAVEGUIDES
Equating real and imaginary parts, we have
d 2 b2
d 5 amp
a b
1 anp
b b
2 v2me
(12.58a)
2adbd 5 vms  or  ad 5 vms
2bd
(12.58b)
Assuming that a2
d V b2
d, a2
d 2 b2
d . 2b2
d, so eq. (12.58a) gives
bd 5 Åv2me 2 amp
a b
2 anp
b b
5 v"me Å1 2 a
f b
(12.59)
which is the same as b in eq. (12.30). Substituting eq. (12.59) into eq. (12.58b) gives
ad 5
shr
Å1 2 a
f b
(12.60)
where hr 5 !m/e.
The determination of ac for TMmn and TEmn modes is time-consuming and tedious.
We shall illustrate the procedure by finding ac for the TE10 mode. For this mode, only Ey,
Hx, and Hz exist. Substituting eq. (12.43a) into eq. (12.53) yields
Pave 5 3
x50
y50
0 Eys 0 2
2h  dx dy 5 v2m2a2H2
2p2h
dy 3
sin2 px
a  dx
Pave 5 v2m2a3H2
4p2h
(12.61)
The total power loss per unit length in the walls is
PL 5 PL 0 y50 1 PL 0 y5b 1 PL 0 x50 1 PL 0 x5a
5 21PL 0 y50 1 PL 0 x502
(12.62)
since the same amount is dissipated in the walls y 5 0 and y 5 b or x 5 0 and x 5 a. For
the wall y 5 0,
PL 0 y50 5 1
2 Rechc 3 1 0 Hxs 0 2 1 0 Hzs 0 22 dxd `
y50
5 1
2 Rs c3
b2a2
p2  H2
o sin2 px
a  dx 1 3
o cos2 px
a  dxd 
(12.63)
5 RsaH2
a1 1 b2a2
p2 b
12.6 Power Transmission and Attenuation  659
where Rs is the real part of the intrinsic impedance hc of the conducting wall. From
eq. (10.56), we write
Rs 5
scd 5 Å
pfm
(12.64)
where d is the skin depth. The skin resistance of the wall Rs may be regarded as the
­resistance of 1 m by d by 1 m of the conducting material. For the wall x 5 0,
PL 0 x50 5 1
2 Rechc 3 1 0 Hzs 0 22 dyd  0 x50 5 1
2 Rs 3
o dy
5 RsbH2
(12.65)
Substituting eqs. (12.63) and (12.65) into eq. (12.62) gives
PL 5 RsH2
o cb 1 a
2 a1 1 b2a2
p2 b d 
(12.66)
For energy to be conserved, the rate of decrease in Pave must equal the time-average power
PL 5 2dPave
5 2aPave
a 5
2Pave
(12.67)
Finally, substituting eqs. (12.61) and (12.66) into eq. (12.67), we have
ac 5
RsH2
o cb 1 a
2 a1 1 b2a2
p2 b d  2p2h
v2m2a3H2
(12.68a)
It is convenient to express ac in terms of f and fc. After some manipulations, we obtain for
the TE10 mode
ac 5
2Rs
bhr
Å1 2 c
f d
2 a0.5 1 b
a c
f d
(12.68b)
By following the same procedure, the attenuation constant for the TEmn modes 1n 2 02
can be obtained as
ac 0 TE 5
2Rs
bhr
Å1 2 c
f d
2 ≥a1 1 b
ab c
f d
a ab
a m2 1 n2b
a2 m2 1 n2
a1 2 c
f d
b ¥ 
(12.69)
loss P  per unit length; that is,
660  CHAPTER 12  WAVEGUIDES
and for the TMmn modes as
ac 0 TM 5
2Rs
bhr
Å1 2 c
f d
2 c (b/a)3 m2 1 n2
(b/a)2 m2 1 n2 d 
(12.70)
The total attenuation constant a is obtained by substituting eqs. (12.60) and (12.69) or
(12.70) into eq. (12.55).
For either TM or TE modes, the surface current density K on the walls of the waveguide
may be found by using
K 5 an 3 H
(12.71)
where an is the unit outward normal to the wall and H is the field intensity evaluated on the
wall. The current flow on the guide walls for TE10 mode propagation can be found by using
eq. (12.71) with eqs. (12.42) and (12.43). The result is sketched in Figure 12.11.
The surface charge density rS on the walls is given by
rS 5 an # D 5 an # eE
(12.72)
where E is the electric field intensity evaluated on the guide wall.
A waveguide is usually fed or excited by a coaxial line or another waveguide. Most
often, a probe (central conductor of a coaxial line) is used to establish the field intensities
of the desired mode and achieve a maximum power transfer. The probe is located so as to
produce E and H fields that are roughly parallel to the lines of E and H fields of the desired
mode. To excite the TE10 mode, for example, we know from eq. (12.43a) that Ey has maxi­
mum value at x 5 a/2. Hence, the probe is located at x 5 a/2 to excite the TE10 mode as
FIGURE 12.11  Surface current on guide walls for TE10 mode.
12.7 WAVEGUIDE CURRENT AND MODE EXCITATION
12.7 Waveguide Current and Mode Excitation  661
shown in Figure 12.12(a), where the field lines are similar to those of Figure 12.8. Similarly,
the TM11 mode is launched by placing the probe along the z-direction as in Figure 12.12(b).
(a)
(b)
FIGURE 12.12  Excitation of modes in a rectangular waveguide:
(a) TE10 mode, (b) TM11 mode.
EXAMPLE 12.5
An air-filled rectangular waveguide of dimensions a 5 4 cm, b 5 2 cm transports energy
in the dominant mode at a rate of 2 mW. If the frequency of operation is 10 GHz, determine
the peak value of the electric field in the waveguide.
Solution:
The dominant mode for a . b is TE10 mode. The field expressions corresponding to this
mode 1m 5 1, n 5 02 are in eq. (12.36) or (12.43), namely,
Exs 5 0,  Eys 5 2jEo sin apx
a b e2jbz,  where Eo 5 vma
p  Ho
fc 5 ur
2a 5
3 3 108
214 3 10222 5 3.75 GHz
h 5 hTE 5
/ 1 2 c
f d
2 5
377
/ 1 2 c 3.75
10 d
2 5 406.7 V
662  CHAPTER 12  WAVEGUIDES
From eq. (12.53), the average power transmitted is
Pave 5 3
y50
x50
0 Eys 0 2
2h  dx dy 5 E2
2h 3
dy 3
sin2 apx
a b dz
5 E2
o ab
Hence,
o 5 4hPave
5 41406.72 3 2 3 1023
8 3 1024
5 4067
Eo 5 63.77 V/m
EXAMPLE 12.6
PRACTICE EXERCISE  12.5
In Example 12.5, calculate the peak value Ho of the magnetic field in the guide if
a 5 2 cm, b 5 4 cm, while other things remain the same.
Answer:  63.34 mA/m.
A copper-plated waveguide 1sc 5 5.8 3 107 S/m2 operating at 4.8 GHz is supposed to
deliver a minimum power of 1.2 kW to an antenna. If the guide is filled with polystyrene
1s 5 10217 S/m, e 5 2.55eo2 and its dimensions are a 5 4.2 cm, b 5 2.6 cm, calculate the
power dissipated in a length 60 cm of the guide in the TE10 mode.
Solution:
Let
Pd 5 power loss or dissipated
Pa 5 power delivered to the antenna
Po 5 input power to the guide
so that Po 5 Pd 1 Pa
From eq. (12.54),
Pa 5 Poe22az
Hence,
Pa 5 1Pd 1 Pa2e22az
Pd 5 Pa1e2az 2 12
12.7 Waveguide Current and Mode Excitation  663
Now we need to determine  from
a 5 ad 1 ac
From eq. (12.60),
ad 5
shr
Å1 2 c
f d
Since the loss tangent
ve 5
10217
2p 3 4.8 3 109 3 1029
36p 3 2.55
5 1.47 3 10217 V 1  1lossless dielectric medium2
then
hr . Å
e 5 377
"er
5 236.1
ur 5
"me
"er
5 1.879 3 108 m/s
fc 5 ur
2a 5
1.879 3 108
2 3 4.2 3 1022 5 2.234 GHz
ad 5
10217 3 236.1
Å1 2 c 2.234
4.8 d
ad 5 1.334 3 10215 Np/m
For the TE10 mode, eq. (12.68b) gives
ac 5
2Rs
bhr
Å1 2 c
f d
2 a0.5 1 b
a c
f d
where
Rs 5
scd 5 Å
pfm
5 Å
p 3 4.8 3 109 3 4p 3 1027
5.8 3 107
5 1.808 3 1022 V
664  CHAPTER 12  WAVEGUIDES
Note that ad V ac, showing that the loss due to the finite conductivity of the guide walls is
more important than the loss due to the dielectric medium. Thus
a 5 ad 1 ac . ac 5 4.218 3 1023 Np/m
and the power dissipated is
Pd 5 Pa 1e2az 2 12 5 1.2 3 1031e234.2183102330.6 2 12
5 6.089 W
EXAMPLE 12.7
PRACTICE EXERCISE  12.6
A brass waveguide 1sc 5 1.1 3 107 S/m2 of dimensions a 5 4.2 cm, b 5 1.5 cm is
filled with Teflon 1er 5 2.6, s 5 10215 S/m2. The operating frequency is 9 GHz. For
the TE10 mode:
(a)  Calculate ad and ac.
(b)  Find the loss in decibels in the guide if it is 40 cm long.
Answer:  (a) 1.205 3 10213 Np/m, 2 3 1022 Np/m,  (b) 0.06945 dB.
Sketch the field lines for the TM11 mode. Derive the instantaneous expressions for the
­surface current density of this mode.
Solution:
From Table 12.1, we obtain the fields for TM11 mode 1m 5 1, n 5 12 as
Ex 5 b
h2 ap
a b Eo cos apx
a b sin a
b b sin1vt 2 bz2
Ey 5 b
h2 ap
b b Eo sin apx
a b cos a
b b sin1vt 2 bz2
Ez 5 Eo sin apx
a b sin a
b b cos1vt 2 bz2
Hx 5 2ve
h2  ap
b b Eo sin apx
a b cos a
b b sin1vt 2 bz2
Hence
ac 5
2 3 1.808 3 1022 a0.5 1 2.6
4.2 c 2.234
4.8 d
2.6 3 1022 3 236.1
Å1 2 c 2.234
4.8 d
5 4.218 3 1023 Np/m
Hy 5 ve
h2  ap
a b Eo cos apx
a b sin a
b b sin1vt 2 bz2
Hz 5 0
For the electric field lines,
dx 5
5 a
b tan apx
a b cot a
b b
For the magnetic field lines,
dx 5
5 2b
a cot apx
a b tan a
b b
Notice that 1Ey/Ex2 1Hy/Hx2 5 21, showing that electric and magnetic field lines are
mutually orthogonal. This should also be observed in Figure 12.13, where the field lines
are sketched.
The surface current density on the walls of the waveguide is given by
K 5 an 3 H 5 an 3 1Hx, Hy, 02
At x 5 0, an 5 ax, K 5 Hy1
K 5 ve
h2  ap
a b Eo sin a
b b sin1vt 2 bz2 az
At x 5 a, an 5 2ax, K 5 2Hy1a, y, z, t2 az, or
K 5 ve
h2  ap
a b Eo sin a
b b sin1vt 2 bz2 az
At y 5 0, an 5 ay, K 5 2Hx1x, 0, z, t2 az, or
K 5 ve
h2  ap
b b Eo sin apx
a b sin1vt 2 bz2 az
At y 5 b, an 5 2ay, K 5 Hx1x, b, z, t2 az, or
K 5 ve
h2  ap
b b Eo sin apx
a b sin1vt 2 bz2 az
FIGURE 12.13  Field lines for TM11 mode; for
Example 12.7.
12.7 Waveguide Current and Mode Excitation  665
0, y, z, t  a ; that is,
666  CHAPTER 12  WAVEGUIDES
End view
Top view
Side view
FIGURE 12.14  Field lines for TE11 mode; for Practice Exercise 12.7.
PRACTICE EXERCISE  12.7
Sketch the field lines for the TE11 mode.
Answer:  See Figure 12.14. The strength of the field at any point is indicated by the den­
sity of the lines; the field is strongest (or weakest) where the lines are closest
together (or farthest apart).
Resonators are primarily used for energy storage. At high frequencies (100 MHz) the
RLC circuit elements are inefficient when used as resonators because the dimensions of the
circuits are comparable to the operating wavelength, and consequently, there is unwanted
radiation. Therefore, at high frequencies the RLC resonant circuits are replaced by electro­
magnetic cavity resonators. Such resonator cavities are used in klystron tubes, bandpass
­filters, and wave meters. The microwave oven essentially consists of a power supply, a
waveguide feed, and an oven cavity.
Consider the rectangular cavity (or closed conducting box) shown in Figure 12.15. We
notice that the cavity is simply a rectangular waveguide shorted at both ends. We therefore
expect to have standing wave and also TM and TE modes of wave propagation. Depending
on how the cavity is excited, the wave can propagate in the x-, y-, or z-direction. We will
choose the 1z-direction as the “direction of wave propagation.” In fact, there is no wave
propagation. Rather, there are standing waves. We recall from Section 10.9 that a standing
wave is a combination of two waves traveling in opposite directions.
12.8 WAVEGUIDE RESONATORS
12.8 Waveguide Resonators  667
FIGURE 12.15  Rectangular cavity.
A.  TM Mode to z
For propagation to z in TM mode, Hz 5 0 and we let
Ezs1x, y, z2 5 X1x2 Y1y2 Z1z2
(12.73)
be the product solution of eq. (12.1). We follow the same procedure taken in Section 12.2
and obtain
X1x2 5 c1 cos kxx 1 c2 sin kxx
(12.74a)
Y1y2 5 c3 cos kyy 1 c4 sin kyy
(12.74b)
Z1z2 5 c5 cos kzz 1 c6 sin kzz
(12.74c)
where
k2 5 k2
x 1 k2
y 1 k2
z 5 v2me
(12.75)
The boundary conditions are:
Ez 5 0
at   x 5 0, a
(12.76a)
Ez 5 0
at   y 5 0, b
(12.76b)
Ey 5 0, Ex 5 0  at  z 5 0, c
(12.76c)
As shown in Section 12.3, the conditions in eqs. (12.76a,b) are satisfied when c1 5 0 5 c3
and
kx 5 mp
a ,  ky 5 np
b 
(12.77)
where m 5 1, 2, 3, .  .  . , n 5 1, 2, 3, .  .  .  . To invoke the conditions in eq. (12.76c), we
notice that eq. (12.14) 1with Hzs 5 02 yields
jveExs 5
jvm a'2Exs
'z2 2 '2Ezs
'z 'xb
(12.78)
668  CHAPTER 12  WAVEGUIDES
Similarly, combining eqs. (12.13a) and (12.13d) 1with Hzs 5 02 results in
jveEys 5
2jvma '2Ezs
'y 'z 2
'2Eys
'z2 b
(12.79)
From eqs. (12.78) and (12.79), it is evident that eq. (12.76c) is satisfied if
'Ezs
'z 5 0  at  z 5 0, c
(12.80)
This implies that c6 5 0 and sin kzc 5 0 5 sin pp. Hence,
kz 5 pp
c 
(12.81)
where p 5 0, 1, 2, 3, .  .  .  . Substituting eqs. (12.77) and (12.81) into eq. (12.74) yields
Ezs 5 Eo sin ampx
b sin a
npy
b b cos a
ppz
c b
(12.82)
where Eo 5 c2c4c5. Other field components are obtained from eqs. (12.82) and (12.13).
The phase constant b is obtained from eqs. (12.75), (12.77), and (12.81) as
b2 5 k2 5 c mp
a d
1 c np
b d
1 c
c d
(12.83)
Since b2 5 v2me, from eq. (12.83), we obtain the resonant frequency fr
2pfr 5 vr 5
"me
5 bur
fr 5 ur
2  Å cm
a d
1 c n
b d
1 c
c d
(12.84)
The corresponding resonant wavelength is
lr 5 ur
Å cm
a d
1 c n
b d
1 c
c d
(12.85)
From eq. (12.84), we notice that the lowest-order TM mode is TM110.
12.8 Waveguide Resonators  669
B.  TE Mode to z
For propagation to z in TE mode, Ez 5 0 and
Hzs 5 1b1 cos kxx 1 b2 sin kxx2 1b3 cos kyy 1 b4 sin kyy2
1b5 cos kzz 1 b6 sin kzz2
(12.86)
The boundary conditions in eq. (12.76c) combined with eq. (12.13) yields
Hzs 5 0   at   z 5 0, c
(12.87a)
'Hzs
'x 5 0  at   x 5 0, a
(12.87b)
'Hzs
'y 5 0  at   y 5 0, b
(12.87c)
Imposing the conditions in eq. (12.87) on eq. (12.86) in the same manner as for TM mode
to z leads to
Hzs 5 Ho cos ampx
b cos a
npy
b b sin a
ppz
c b
(12.88)
where m 5 0, 1, 2, 3, .  .  . , n 5 0, 1, 2, 3, .  .  . , and p 5 1, 2, 3, .  .  .  . Other field
­components can be obtained from eqs. (12.13) and (12.88). The resonant frequency is
the same as that of eq. (12.84) except that m or n (but not both at the same time) can
be zero for TE modes. It is impossible for m and n to be zero at the same time because
the field components will be zero if m and n are zero. The mode that has the lowest
resonant frequency for a given cavity size (a, b, c) is the dominant mode. If a . b , c,
101. Note that for a . b , c,
the resonant frequency of TM110 mode is higher than that for TE101 mode; hence, TE101 is
dominant. When different modes have the same resonant frequency, we say that the modes
are degenerate; one mode will dominate others depending on how the cavity is ­excited.
A practical resonant cavity has walls with finite conductivity sc and is, therefore,
­capable of losing stored energy. The quality factor Q is a means of determining the loss.
The quality factor is also a measure of the bandwidth of the cavity resonator.
It may be defined as
Q 5 2p #
time average energy stored
energy loss per cycle of oscillation
5 2p # W
PLT 5 v W
(12.89)
it implies that 1/a , 1/b . 1/c; hence, the dominant mode is TE
670  CHAPTER 12  WAVEGUIDES
where T 5 1/f 5 the period of oscillation, PL is the time-average power loss in the cavity,
and W is the total time-average energy stored in electric and magnetic fields in the cavity.
Usually Q is very high for a cavity resonator compared with Q for an RLC resonant circuit.
By following a procedure similar to that used in deriving ac in Section 12.6, it can be shown
that the quality factor for the dominant TE101 is given by3
QTE101 5
1a2 1 c22abc
d32b1a3 1 c32 1 ac1a2 1 c22 4
(12.90)
where d 5
"pf101mosc
is the skin depth of the cavity walls.
EXAMPLE 12.8
An air-filled resonant cavity with dimensions a 5 5 cm, b 5 4 cm, and c 5 10 cm is made
of copper 1sc 5 5.8 3 107 S/m2. Find
(a)	 The five lowest-order modes
(b)	 The quality factor for TE101 mode
3 For the proof, see S. V. Marshall and G. G. Skitek, Electromagnetic Concepts and Applications, 3rd ed.
Englewood Cliffs, NJ: Prentice-Hall, 1990, pp. 440–442.
Solution:
(a) The resonant frequency is given by
fr 5 ur
2  Å c m
a d
1 c n
b d
1 c
c d
where
ur 5
"me
5 c
Hence
fr 5 3 3 108
Å c
5 3 1022 d
1 c
4 3 1022 d
1 c
10 3 1022 d
5 15"0.04m2 1 0.0625n2 1 0.01p2 GHz
Since c . a . b or 1/c , 1/a , 1/b, the lowest-order mode is TE101. Notice that TM101
and TE100 do not exist because m 5 1, 2, 3, . . . , n 5 1, 2, 3, . . . , and p 5 0, 1, 2, 3, . . .
for the TM modes, and m 5 0, 1, 2, . . . , n 5 0, 1, 2, . . . , and p 5 1, 2, 3, . . . for the
TE modes. The resonant frequency for the TE101 mode is
fr101 5 15"0.04 1 0 1 0.01 5 3.354 GHz
12.8 Waveguide Resonators  671
The next higher mode is TE011 (TM011 does not exist), with
fr011 5 15"0 1 0.0625 1 0.01 5 4.04 GHz
The next mode is TE102 (TM102 does not exist), with
fr102 5 15"0.04 1 0 1 0.04 5 4.243 GHz
The next mode is TM110 (TE110 does not exist), with
fr110 5 15"0.04 1 0.0625 1 0 5 4.8 GHz
The next two modes are TE111 and TM111 (degenerate modes), with
fr111 5 15"0.04 1 0.0625 1 0.01 5 5.031 GHz
The next mode is TM103 with
fr103 5 15"0.04 1 0 1 0.09 5 5.408 GHz
Thus the five lowest order modes in ascending order are
TE101
(3.35 GHz)
TE011
(4.04 GHz)
TE102
(4.243 GHz)
TM110
(4.8 GHz)
TE111 or TM111
(5.031 GHz)
(b)	 The quality factor for TE101 is given by
QTE101 5
1a2 1 c22 abc
d32b1a3 1 c32 1 ac1a2 1 c22 4
125 1 1002 200 3 1022
d381125 1 10002 1 50125 1 1002 4
61d 5
"pf101 mosc
5 "p13.35 3 1092 4p 3 1027 15.8 3 1072
5 14,358
PRACTICE EXERCISE  12.8
If the resonant cavity of Example 12.8 is filled with a lossless material 1mr 5 1, er 5 32 ,
find the resonant frequency fr and the quality factor for TE101 mode.
Answer:  1.936 GHz, 1.093 3 104.
672  CHAPTER 12  WAVEGUIDES
†12.9  APPLICATION NOTE—OPTICAL FIBER
In the mid-1970s, it was recognized that the existing copper technology would be unsuit­
able for future communication networks. In view of this, the telecommunication industry
invested heavily in research into optical fibers. Optical fiber provides an attractive alter­
native to wire transmission lines such as twisted pair and coaxial cable (or coax). Optical
fiber4 has the following advantages over copper:
•	 Bandwidth: It provides a very high capacity for carrying information. It has suf­
ficient bandwidth that bit-serial transmission can be used, thereby considerably
reducing the size, cost, and complexity of the hardware.
•	 Attenuation: It provides low attenuation and is therefore capable of transmitting
over a long distance without the need of repeaters.
•	 Noise susceptibility: It neither radiates nor is affected by electromagnetic interfer­
ence. The immunity from EMI is due to the absence of metal parts, which means
that there can be no conduction currents.
•	 Security: It is more secure from malicious interception because it is not easy to tap
a fiber-optic cable without interrupting communication.
•	 Cost: The cost of optical fibers has fallen considerably since the turn of the century
and will continue to fall. The cost of related components such as optical transmit­
ters and receivers also is falling.
These impressive advantages over electrical media have made fiber optics a popular trans­
mission medium in recent times. Although optical fiber is more expensive and is used
mainly for point-to-point links, there has been a rapid changeover from coax and twisted
pair to optical fibers for telecommunication systems, instrumentation, cable TV networks,
industrial automation, and data transmission systems.
An optical fiber is a dielectric waveguide operating at optical frequency.
Optical frequencies are on the order of 100 THz. As shown in Figure 12.16, an optical fiber
consists of three concentric cylindrical sections: the core, the cladding, and the jacket. The
core consists of one or more thin strands made of glass or plastic. The cladding is the glass
or plastic coating surrounding the core, which may be step index or graded index. In the
step-index core, the refractive index is uniform but undergoes an abrupt change at the
core–cladding interface, while the graded-index core has a refractive index that varies with
the radial distance from the center of the fiber. The jacket surrounds one or a bundle of
cladded fibers. The jacket is made of plastic or other materials to protect against moisture,
crushing, and other forms of damage.
A ray of light entering the core will be internally reflected when incident in the denser
medium and the angle of incidence is greater than a critical value. Thus a light ray is
4 There are several excellent books that can provide further exposition on optical fiber. See, for example, S. L. W.
Meardon, The Elements of Fiber Optics, Englewood Cliffs, NJ: Regents/Prentice Hall, 1993.
12.9 Application Note—Optical Fiber  673
­reflected back into the original medium and the process is repeated as light passes down
the core. This form of propagation is multimode, referring to the variety of angles that
will ­reflect, as shown in Figure 12.17. It causes the signal to spread out in time and limits
the rate at which data can be accurately received. When the radius of the core is reduced a
­single-mode propagation occurs. This eliminates distortion.
A fiber-optic system is similar to a conventional transmission system. As shown in
Figure 12.18, a fiber-optic system consists of a transmitter, a transmission medium, and a
­receiver. The transmitter accepts and converts to optical signals electrical signals input in
analog or digital form. The transmitter sends the optical signal by modulating the output
of a light source (usually an LED or a laser) by varying its intensity. The optical signal is
transmitted over the optical fiber to a receiver. At the receiver, the optical signal is con­
verted back into an electrical signal by a photodiode.
The performance of a fiber-optic link depends on the numerical aperture (NA), atten­
uation, and dispersion characteristics of the fiber. As signals propagate through the fiber,
they become distorted owing to attenuation and dispersion.
Numerical Aperture
The most important parameter of an optical fiber is its numerical aperture (NA). The
value of NA is dictated by the refractive indices of the core and cladding. By definition, the
­refractive index n of a medium is defined as
n 5
speed of light in a vacuum
speed of light in the medium
5 c
!moeo
!mmem
(12.91)
Jacket
Cladding
Core
Angle of
incidence
Angle of
reflection
Light at less than
critical angle is
absorbed in jacket
FIGURE 12.16  Optical fiber.
674  CHAPTER 12  WAVEGUIDES
(a)
(c)
(b)
Absorptive jacket
Core
Cladding
FIGURE 12.17.  Optical fiber transmission modes: (a) multimode, (b) multi­
mode graded index, (c) single mode. (From W. Stallings, Local and Metropolitan
Area Networks, 4th ed. New York: Macmillan, 1993, p. 85.)
Since mm 5 mo in most practical cases,
n 5 Å
5 "er
(12.92)
indicating that the refractive index is essentially the square root of the dielectric constant.
Keep in mind that «r can be complex, as discussed in Chapter 10. For common materials,
n 5 1 for air, n 5 1.33 for water, and n 5 1.5 for glass.
As a light ray propagates from medium 1 to medium 2, Snell’s law must be satisfied.
n1 sin u1 5 n2 sin u2
(12.93)
where 1 is the incident angle in medium 1 and 2 is the transmission angle in medium 2.
The total reflection occurs when 2 5 90, resulting in
u1 5 uc 5 sin21 n2
(12.94)
where c is the critical angle for total internal reflection. Note that eq. (12.94) is valid only
if n1 . n2, since the value of sin c must be less than or equal to 1.
Another way of looking at the light-guiding capability of a fiber is to measure the
­acceptance angle a, which is the maximum angle over which light rays entering the fiber
will be trapped in its core. We know that the maximum angle occurs when c is the critical
angle, thereby satisfying the condition for total internal reflection. Thus, for a step-index
fiber,
NA 5 sin ua 5 n1 sin uc 5 "n1
2 2 n2
(12.95)
where n1 is the refractive index of the core and n2 is the refractive index of the cladding, as
shown in Figure 12.19. Since most fiber cores are made of silica, n1 5 1.48. Typical values
of NA range between 0.19 and 0.25. The larger the value of NA, the more optical power the
fiber can capture from a source.
Because such optical fibers may support the numerous modes, they are called a multi­
mode step-index fibers. The mode volume V is given by
V 5 pd
l "n1
2 2 n2
(12.96)
Electrical data
input
Electrical-to-
optical
converter
Optical fiber cable
Transmission
medium
Light detector
Light source
Electrical data
output
Optical-to-
electrical
converter
FIGURE 12.18  A typical fiber-optic system.
12.9 Application Note—Optical Fiber  675
676  CHAPTER 12  WAVEGUIDES
where d is the fiber core diameter and l is the wavelength of the optical source. From
eq. (12.96), the number N of modes propagating in a step-index fiber can be estimated as
N 5 V2
2 
(12.97)
Attenuation
As discussed in Chapter 10, attentuation is the reduction in the power of the optical signal.
Power attenuation (or fiber loss) in an optical fiber is governed by
dz 5 2aP
(12.98)
where a is the attenuation and P is the optical power. In eq. (12.98), it is assumed that a
wave propagates along z. By solving eq. (12.98), the power P102 at the input of the fiber and
the power P1,2 of the light after  are related as
P1,2 5 P102e2a,
(12.99)
It is customary to express attenuation a in decibels per kilometer and length  of the fiber
in kilometers. In this case, eq. (12.99) becomes
a, 5 10 log10 P102
P1,2 
(12.100)
Thus, the power of the light reduces by a decibels per kilometer as it propagates through
the fiber. Equation (12.100) may be written as
P1,2 5 P102 # 102a,/10
(12.101)
n0  1
Core
Cladding
FIGURE 12.19  Numerical aperture and acceptance angle.
For , 5 100 km,
P1,2
P102 , e102100
for coaxial cable
1022
for optical fiber 
(12.102)
indicating that much more power is lost in the coaxial cable than in optical fiber.
Dispersion
The spreading of pulses of light as they propagate down a fiber is called dispersion. As the
pulses representing 0s spread, they overlap epochs that represent 1s. If dispersion is beyond
a certain limit, it may confuse the receiver. The dispersive effects in single-mode fibers are
much smaller than in multimode fibers.
EXAMPLE 12.9
A step-index fiber has a core diameter of 80 mm, a core refractive index of 1.62, and a
numerical aperture of 0.21. Calculate (a) the acceptance angle, (b) the refractive index that
the fiber can propagate at a wavelength of 0.8 mm, (c) the number of modes that the fiber
can propagate at a wavelength of 0.8 mm.
Solution:
(a)	 Since sin ua 5 NA 5 0.21, then
ua 5 sin21 0.21 5 12.12
(b)	 From NA 5 "n1
2 2 n2
2, we obtain
n2 5 "n1
2 2 NA2 5 "1.622 2 0.212 5 1.606
(c)
V 5 pd
l "n1
2 2 n2
2 5 pd NA
5 p180 3 10262 3 0.21
0.8 3 1026
5 65.973
Hence
N 5 V2
2 5 2176 modes
PRACTICE EXERCISE  12.9
A silica fiber has a refractive index of 1.48. It is surrounded by a cladding material with
a refractive index of 1.465. Find (a) the critical angle above which total internal reflec­
tion occurs, (b) the numerical aperture of the fiber.
Answer:  (a) 81.83,  (b) 0.21.
12.9 Application Note—Optical Fiber  677
678  CHAPTER 12  WAVEGUIDES
EXAMPLE 12.10
Light pulses propagate through a fiber cable with an attenuation of 0.25 dB/km. Determine
the distance through which the power of pulses is reduced by 40%.
Solution:
If the power is reduced by 40%, it means that
P1,2
P102 5 1 2 0.4 5 0.6
Hence
, 5 10
a  log10 P102
P1,2
5 10
0.25 log10 1
0.6
5 8.874 km
PRACTICE EXERCISE  12.10
A 10 km fiber with an attenuation of 0.2 dB/km serves as an optical link between two
cities. How much of input power is received?
Answer:  63.1%.
12.10  APPLICATION NOTE—CLOAKING AND INVISIBILITY
The practice of using metamaterials to hide an object is called metamaterial cloaking.
Metamaterials are ideal for cloaking because they are designed to have a negative refractive
index. All materials have an index of refraction, a number that describes that amount of
light, or electromagnetic wave, that is reflected as the wave passes through the material. All
materials that are found in nature have a positive refraction index, allowing the reflected
light to hit an observer’s eye, making the object visible. However, the negative refraction
index of metamaterials can bend the wave around an object instead of reflecting the light,
thus making the object invisible.
Many attempts at cloaking an object have been made and have been successful to some
degree, leaving only small reflections of the cloaked object. Recently, however, ­researchers
at Duke University discovered a method of cloaking an object completely, making it
­perfectly invisible. The research at Duke began in 2006, but the cloaking models suffered
from the common problem of reflected light. In 2011, David Smith and graduate ­student
Nathan Landy modified the models by altering the arrangement of the ­metamaterial
to a ­diamond-like configuration and shifting the metamaterial so that the reflections
were ­canceled by its mirror image at each intersection. With this adjustment, illustrated
­schematically in Figure 12.20, perfect invisibility was achieved.
12.10 Application Note—Cloaking and Invisibility  679
This perfect invisibility, however, comes at the price of a few caveats. An invisibility
cloak has been created only on the centimeter scale. Also, the object surrounded by this
metamaterial cloak is invisible only to microwaves. In other words, the researchers have
been able to bend microwaves but have not yet achieved the bending of light waves, which
are more difficult to bend because they have a higher frequency. Finally, the invisibil-
ity is unidirectional: that is, the object cloaked is invisible from only one specific angle.
Nonetheless, this research at Duke University marks a breakthrough in metamaterial cloak-
ing. These researchers, who were the first to bend waves without any reflection, now plan
to further develop the cloak to make it omnidirectional, hiding the object from every angle.
While using metamaterials to render objects invisible to the human eye may be
decades away, invisibility to microwaves has many practical applications in telecommuni-
cations and defense. Potential applications include radar and sensor detection, battlefield
communication, and infrastructure monitoring.
FIGURE 12.20  Showing bending of light.
% This script computes the cutoff frequencies of the first
% 10 waveguide modes, allowing the user to enter the
% dimensions (assuming a > b) and relative material properties.
% The script first finds the lowest 100 modes by cutoff frequency
% for both TE and TM, creating a list of 200 total modes, from
% which the lowest 10 of all (TE and TM) are found
clear
% Enter the frequency (in rad/s)
a = input(‛Enter the waveguide width\n >  ‛);
% Enter the propagation constant gamma (in a+j*b format)
b = input(‛Enter the waveguide height\n >  ‛);
% Enter the relative permittivity
er = input(‛Enter the relative permittivity \n >  ‛);
% Enter the propagation constant gamma (in a+j*b format)
ur = input(‛Enter the relative permeability\n >  ‛);
% Determine the first 100 TM modes
MATLAB 12.1
680  CHAPTER 12  WAVEGUIDES
index=1; % start a count
for m=1:10,
for n=1:10,
modes(index,1)=1; % store a 1 in row <index>, and
% column 1 for TM modes
modes(index,2)=m; % store m in row <index>, and column 2
modes(index,3)=n; % store n in row <index>, and column 3
modes(index,4)=3e8/sqrt(er*ur)*sqrt((m*pi/a)^2+(n*pi/b)^2);
% store cutoff in row <index>, and column 4
index=index+1; % increment counter
end
end
% Determine the first 100 TE modes
for m=0:9,
for n=0:9,
if m | n  % check if either m or n is nonzero and
% compute mode
modes(index,1)=2;
modes(index,2)=m;
modes(index,3)=n;
modes(index,4)=3e8/sqrt(er*ur)*sqrt((m*pi/
a)^2+(n*pi/b)^2);
index=index+1;
else
% do nothing, because m = n = 0
end
end
end
% Sort these 100 modes by lowest cutoff
% this command sorts the matrix by grouping the fourth
% column (the frequencies) in ascending order)
modes=sortrows(modes,4);
% Print out the lowest 10 modes of the lowest 100 modes
mode_string=’ME’;  % ‛M  is the first character, ‛E  is the second
disp(sprintf(‛\n’));  % format extra line
for k = 1:10
disp(sprintf(‛Mode: T%c%d%d, ‛,...
mode_string(modes(k,1)),modes(k,2), modes(k,3)))
disp(sprintf(‛Cutoff frequency = %0.3f GHz\n’,...
modes(k,4)/(2*pi*1e9)))
end
SUMMARY
1.  Waveguides are structures used in guiding EM waves at high frequencies. Assuming
a lossless rectangular waveguide 1sc . `, s . 02, we apply Maxwell’s equations in
analyzing EM wave propagation through the guide. The resulting partial differential
Summary  681
equation is solved by using the method of separation of variables. On applying the
boundary conditions on the walls of the guide, the basic formulas for the guide are
obtained for different modes of operation.
2.  Two modes of propagation (or field patterns) are the TMmn and TEmn, where m and n
are positive integers. For TM modes, m 5 1, 2, 3, .  .  . , and n 5 1, 2, 3, .  .  . and for
TE modes, m 5 0, 1, 2, .  .  . , and n 5 0, 1, 2, .  .  . , n 5 m 2 0.
3.  Each mode of propagation has an associated propagation constant and cutoff frequency.
The propagation constant g 5 a 1 jb does not depend only on the constitutive pa­ra­
meters 1e, m, s2 of the medium as in the case of plane waves in an unbounded space; it
depends on the cross-sectional dimensions 1a, b2 of the guide. The cutoff frequency is
the frequency at which g changes from being purely real (attenuation) to purely imagi­
nary (propagation). The dominant mode of operation is the lowest mode possible. It is
the mode with the lowest cutoff frequency. If a . b, the dominant mode is TE10.
4.  The basic equations for calculating the cutoff frequency fc, the phase constant b,
and the phase velocity up are summarized in Table 12.1. Formulas for calculating the
­attenuation constants due to lossy dielectric medium and imperfectly conducting
walls are also provided.
5.  The group velocity (or velocity of energy flow) ug is related to the phase velocity up of
the wave propagation by
upug 5 ur2
where ur 5 1/"me is the medium velocity (i.e., the velocity of the wave in the
­dielectric medium unbounded by the guide). Although up is greater than u, ug does
not exceed u.
6.  The mode of operation for a given waveguide is dictated by the method of
­excitation.
7.  A waveguide resonant cavity is used for energy storage at high frequencies. It is
waveguide. The resonant frequency for both the TE and the TM modes to z is given by
For TM modes, m 5 1, 2, 3, .  .  . , n 5 1, 2, 3, .  .  . , and p 5 0, 1, 2, 3, .  .  . , and for
TE modes, m 5 0, 1, 2, 3, .  .  . , n 5 0, 1, 2, 3, .  .  . , and p 5 1, 2, 3, .  .  . , m 5 n 2 0.
If a . b , c, the dominant mode (one with the lowest resonant frequency) is TE101.
8.  The quality factor, a measure of the energy loss in the cavity, is given by
Q 5 v W
9.  An optical fiber is a dielectric waveguiding structure operating at optical frequencies;
it consists of a core region and a cladding region.
10.  Advantages of optical fiber over copper wire include large bandwidth, low attenua­
tion, immunity to electromagnetic intererence, and low cost.
fr 5 ur
2 Å c m
a d
1 c n
b d
1 c
c d
nothing but a waveguide shorted at both ends. Hence its analysis is similar to that of a
682  CHAPTER 12  WAVEGUIDES
REVIEW
QUESTIONS
12.1	 At microwave frequencies, we prefer waveguides to transmission lines for transporting
EM energy because of all the following except that
(a)  losses in transmission lines are prohibitively large.
(b)  waveguides have larger bandwidths and lower signal attenuation.
(c)  transmission lines are larger than waveguides.
(d)  transmission lines support only TEM mode.
12.2	 An evanescent mode occurs when
(a)  a wave is attenuated rather than propagated.
(b)  the propagation constant is purely imaginary.
(c)  m 5 0 5 n so that all field components vanish.
(d)  the wave frequency is the same as the cutoff frequency.
12.3	 The dominant mode for rectangular waveguides is
(a)  TE11
(c)  TE101
(b)  TM11
(d)  TE10
12.4	 The TM10 mode can exist in a rectangular waveguide.
(a)  True
(b)  False
12.5	 For TE30 mode, which of the following field components exist?
(a)  Ex
(d)  Hx
(b)  Ey
(e)  Hy
(c)  Ez
12.6	 If in a rectangular waveguide for which a 5 2b, the cutoff frequency for TE02 mode is
12 GHz, the cutoff frequency for TM11 mode is
(a)  3 GHz
(d)  6!5 GHz
(b)  3!5 GHz
(e)  None of the above
(c)  12 GHz
12.7	 If a tunnel is 4 m by 7 m in cross section, a car in the tunnel will not receive an AM radio
signal 1e.g.,  f 5 10 MHz2.
(a)  True
(b)  False
12.8	 When the electric field is at its maximum value, the magnetic energy of a cavity is
(a)  at its maximum value
(b)  at !2 of its maximum value
(c)  at 1
!2 of its maximum value
(d)  at 1/2 of its maximum value
(e)  zero

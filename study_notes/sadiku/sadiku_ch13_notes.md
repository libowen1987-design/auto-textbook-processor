# Sadiku《Elements of Electromagnetics》Chapter 13

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 718-767 of 926 (926 total)

---

## Antennas

691
C H A P T E R
691
13.1  INTRODUCTION
Up until now, we have not asked ourselves how EM waves are produced. Recall that electric
charges are the sources of EM fields. If the sources are time varying, EM waves propagate
away from the sources and radiation is said to have taken place. Radiation may be thought
of as the process of transmitting electric energy. The radiation or launching of the waves
into space is efficiently accomplished with the aid of conducting or dielectric structures
called antennas. Theoretically, any structure can radiate EM waves, but not all structures
can serve as efficient radiation mechanisms.
An antenna may also be viewed as a transducer used in matching the transmission line
or as a waveguide (used in guiding the wave to be launched) to the surrounding medium,
or vice versa. Figure 13.1 shows how an antenna is used to accomplish a match between the
line or guide and the medium. The antenna is needed for two main reasons: for efficient
radiation and for matching wave impedances to minimize reflection. The antenna uses
voltage and current from the transmission line (or the EM fields from the waveguide) to
launch an EM wave into the medium. An antenna may be used for either transmitting or
receiving EM energy.
Typical antennas are illustrated in Figure 13.2. The dipole antenna in Figure 13.2(a)
consists of two straight wires lying along the same axis. The loop antenna, exemplified in
Figure 13.2(b), consists of one or more turns of wire. The helical antenna in Figure 13.2(c)
consists of a wire in the form of a helix backed by a ground plane. Antennas in Figure
13.2(a–c) are called wire antennas; they are used in automobiles, buildings, aircraft, ships,
and so on. The horn antenna in Figure 13.2(d), an example of an aperture antenna, is a
tapered section of waveguide providing a transition between a waveguide and the sur­
roundings. Since it is conveniently flush mounted, it is useful in various applications such
as aircraft communications. The parabolic dish reflector in Figure 13.2(e) utilizes the fact
that EM waves are reflected by a conducting sheet. When used as a transmitting antenna,
a feed antenna such as a dipole or horn is placed at the focal point. The radiation from the
source is reflected by the dish (acting like a mirror), and a parallel beam results. Parabolic
dish ­antennas are used in communications, radar, and astronomy.
ANTENNAS
A committee is a group of the unwilling, chosen from the unfit, to do the unnecessary.
—ANONYMOUS
692  CHAPTER 13  ANTENNAS
FIGURE 13.1  An antenna as a matching device between the
guiding structure and the surrounding medium.
FIGURE 13.2  Typical antennas.
13.2 Hertzian Dipole  693
The phenomenon of radiation is rather complicated, so we have intentionally delayed
its discussion until this chapter. We will not attempt a broad coverage of antenna theory;
our discussion will be limited to the basic types of antennas such as the Hertzian dipole, the
half-wave dipole, the quarter-wave monopole, and the small loop. For each of these types,
we will determine the radiation fields by taking the following steps:
1.	 Select an appropriate coordinate system and determine the magnetic vector
­potential A.
2.	 Find H from B 5 mH 5 = 3 A.
3.	 Determine E from = 3 H 5 e 'E
't  or E 5 hH 3 ak assuming a lossless medium
1s 5 02.
13.2  HERTZIAN DIPOLE
By “Hertzian dipole” we mean an infinitesimal current element I dl, where dl # l /10.
­Although such a current element does not exist in real life, it serves as a building block
from which the field of a practical antenna can be calculated by integration.
Consider the Hertzian dipole shown in Figure 13.3. We assume that it is located at the
origin of a coordinate system and that it carries a uniform current (constant throughout the
FIGURE 13.3  A Hertzian dipole carry­
ing current I 5 Io cos vt.
4. Find the far field and determine the time-average power radiated by using
Note that Prad throughout this chapter is the same as Pave in eq. (10.80).
Prad 5 3 ave # dS
where
ave 5 1
2 Re 1Es 3 H*s2
We will consider antenna arrays which produce particular directional properties of
the radiated field.  We will derive the Friis transmission equation for coupling between two
antennas.  Finally, we will consider the problem of electromagnetic interference (EMI).
694  CHAPTER 13  ANTENNAS
dipole), I 5 Io cos vt. From eq. (9.54), the retarded magnetic vector potential at the field
point P, due to the dipole, is given by
A 5 m3I4 dl
4p r  az
(13.1)
where [I] is the retarded current given by
3I4 5 Io cos v at 2 r
ub 5 Io cos 1vt 2 br2
5 Re 3Ioe j1vt2br24
(13.2)
where b 5 v/u 5 2p/l, and u 5 1/!me. The current is said to be retarded at point P
because there is a propagation time delay r/u or phase delay br from O to P. By substituting
eq. (13.2) into eq. (13.1), we may write A in phasor form as
Azs 5 mIodl
4pr  e2jbr
(13.3)
Transforming this vector from Cartesian to spherical coordinates yields
As 5 1Ars, Aus, Afs2
where
Ars 5 Azs cos u,  Aus 5 2Azs sin u,  Afs 5 0
(13.4)
Since Bs 5 mHs 5 = 3 As, we obtain the H field as
Hfs 5 Iodl
4p  sin u c
r 1 1
r2 d  e2jbr
(13.5a)
Hrs 5 0 5 Hus
(13.5b)
We find the E field by using = 3 H 5 e 'E/'t or = 3 Hs 5 jveEs,
Ers 5 hIodl
2p  cos u c 1
r2 2
br3 d  e2jbr
(13.6a)
Eus 5 hIodl
4p  sin u c
r 1 1
r2 2
br3 d  e2jbr
(13.6b)
Efs 5 0
(13.6c)
where
h 5 b
ve 5 Å
13.2 Hertzian Dipole  695
A close observation of the field equations in eqs. (13.5) and (13.6) reveals that we have
terms varying as 1/r3, 1/r2, and 1/r. The 1/r3 term is called the electrostatic field, since it cor­
responds to the field of an electric dipole [see eq. (4.82)]. This term dominates other terms
in a region very close to the Hertzian dipole. The 1/r2 term is called the inductive field, and
it is predictable from the Biot–Savart law [see eq. (7.3)]. The term is important only at near
field, that is, at distances close to the current element. The 1/r term is called the far field or
radiation field because it is the only term that remains at the far zone, that is, at a point very
far from the current element. Here, we are mainly concerned with the far field or radiation
zone 1br W 1 or 2pr W l2, where the terms in 1/r3 and 1/r2 can be ­neglected in favor of
the 1/r term. Also note that near-zone and far-zone fields are determined, respectively, to
be the inequalities br V 1 and br W 1. More specifically, we define the boundary between
the near and the far zones by the value of r given by
r 5 2d2
l 
(13.7)
where d is the largest dimension of the antenna. Thus at far field,
Hfs 5
jIobdl
4pr  sin u e2jbr,  Eus 5 h Hfs
(13.8a)
Hrs 5 Hus 5 Ers 5 Efs 5 0
(13.8b)
Note from eq. (13.8a) that the radiation terms of Hfs and Eus are in time phase and orthogo­
nal just as the fields of a uniform plane wave.
The time-average power density is obtained as
5 3
f50
u50
ohb2 dl2
32p2r2  sin2 u r2 sin u dud df
(13.10)
5 I2
ohb2 dl2
32p2  2p 3
sin3 u du
But
sin3 u du 5 3
11 2 cos2 u2 d12cos u2
5 cos3 u
2 cos u`
5 4
ave 5 1
2 Re1Es 3 H*s2 5 1
2 Re1Eus H*fsar2
5 1
2 h 0 Hfs 0 2 ar
(13.9)
Substituting eq. (13.8a) into eq. (13.9) yields the time-average radiated power as
Prad 5 3 ave # dS
696  CHAPTER 13  ANTENNAS
and b2 5 4p2/l2. Hence eq. (13.10) becomes
Prad 5 I2
o ph
c dl
l d
(13.11a)
If free space is the medium of propagation, h 5 120p and
Prad 5 40p2 c dl
l d
(13.11b)
This power is equivalent to the power dissipated in a fictitious resistance Rrad by current
Prad 5 I2
rms Rrad
Prad 5 1
2 I2
o Rrad
(13.12)
where Irms is the root-mean-square value of I. From eqs. (13.11) and (13.12), we obtain
Rrad 5 2Prad
(13.13a)
Rrad 5 80p2 c dl
l d
(13.13b)
The resistance Rrad is a characteristic property of the Hertzian dipole antenna and is called
its radiation resistance. From eqs. (13.12) and (13.13), we observe antennas with large
­radiation resistances are required to deliver large amounts of power to space. For example,
if dl 5 l/20, Rrad . 2 V, which is small in that it can deliver relatively small amounts of
power. It should be noted that Rrad in eq. (13.13b) is for a Hertzian dipole in free space. If
the dipole is in a different, lossless medium, h 5 "m/e is substituted in eq. (13.11a) and
Rrad is determined by using eq. (13.13a).
Note that the Hertzian dipole is assumed to be infinitesimally small 1b dl V 1 or
dl # l/102. Consequently, its radiation resistance is very small, and it is in practice dif­
ficult to match it with a real transmission line. We have also assumed that the dipole
has a uniform current; this requires that the current be nonzero at the end points of the
dipole. This is practically impossible because the surrounding medium is not conduct­
ing. However, our analysis will serve as a useful, valid approximation for an antenna with
dl # l/10. A more practical (and perhaps the most important) antenna is the half-wave
dipole, considered in the next section.
I 5 I  cos vt; that is,
13.3 Half-Wave Dipole Antenna  697
The half-wave dipole derives its name from the fact that its length is half a wavelength
1, 5 l/22. As shown in Figure 13.4(a), it consists of a thin wire fed or excited at the mid­
point by a voltage source connected to the antenna via a transmission line (e.g., a two-wire
line). The field due to the dipole can be easily obtained if we consider it as consisting of a
chain of Hertzian dipoles. The magnetic vector potential at P due to a differential length
dl 15 dz2 of the dipole [see Figure. 13.4(b)] carrying a phasor current Is 5 Io cos bz is
dAzs 5 mIo cos bz dz
4prr
e2jbrr
(13.14)
Notice that to obtain eq. (13.14), we have assumed a sinusoidal current distribution for two
reasons. First, the sinusoidal current assumption is based on the transmission line model
of the dipole. Second, the current must vanish at the ends of the dipole. A triangular cur­
rent distribution is also possible (see Problem 13.5) but would give less accurate results.
The actual current distribution on the antenna is not precisely known. It is determined
by ­solving Maxwell’s equations subject to the boundary conditions on the antenna, but
13.3  HALF-WAVE DIPOLE ANTENNA
FIGURE 13.4  (a) A half-wave dipole.
(b) Geometry for calculating the fields.
698  CHAPTER 13  ANTENNAS
the procedure is mathematically complex. However, the sinusoidal current assumption
approximates the distribution obtained by solving the boundary-value problem and is
commonly used in antenna theory.
If r W ,, as explained in Section 4.9 on electric dipoles (see Figure 4.20), then
r 2 rr 5 z cos u  or  rr 5 r 2 z cos u
Thus we may substitute rr . r in the denominator of eq. (13.14), where the magnitude
of the distance is needed. For the phase term in the numerator of eq. (13.14), the dif-
ference between br and br is significant, so we replace r by r 2 z cos u and not r. In other
words, we maintain the cosine term in the exponent while neglecting it in the denominator
because the exponent involves the phase constant while the denominator does not. Thus,
Azs 5 mIo
4pr 3
l/4
2l/4
2jb1r2z cos u2 cos bz dz
5 mIo
4pr e2jbr 3
l/4
2l/4
e jbz cos u cos bz dz
(13.15)
From the integral tables of Appendix A.8,
3 eaz cos bz dz 5 eaz 1a cos bz 1 b sin bz2
a2 1 b2
1 c
Applying this to eq. (13.15) gives
Azs 5 mIoe2jbre jbz cos u
4pr
1 jb cos u cos bz 1 b sin bz2
2b2 cos2 u 1 b2
2l/4
l/4
(13.16)
Since b 5 2p/l or b l/4 5 p/2 and 2cos2 u 1 1 5 sin2 u, eq. (13.16) becomes
Azs 5
mIoe2jbr
4prb2 sin2 u 3e j1p/22 cos u10 1 b2 2 e2j1p/22 cos u10 2 b2 4
(13.17)
Using the identity e jx 1 e2jx 5 2 cos x, we obtain
Azs 5
mIoe2jbr cos ap
2  cos ub
2prb sin2 u
(13.18)
We use eq. (13.4) in conjunction with the fact that Bs 5 mHs 5 = 3 As and = 3 Hs 5jveEs
to obtain the magnetic and electric fields at far zone (discarding the 1/r3 and 1/r2 terms) as
Hfs 5
jIoe2jbr cos ap
2   cos ub
2pr sin u
,  Eus 5 hHfs
(13.19)
13.3 Half-Wave Dipole Antenna  699
Notice again that the radiation terms Hfs and Es are in time phase and orthogonal.
By using eqs. (13.9) and (13.19), we obtain the time-average power density as
3ave 5 1
2 h 0 Hfs 0 2 ar
hI2
o cos2 ap
2  cos ub
8p2r2 sin2 u
ar
(13.20)
The time-average radiated power can be determined as
5 3
f50
u50
hI2
o cos2 ap
2  cos ub
8p2r2 sin2 u
r2 sin u du¥ df
5 hI2
8p2 2p 3
cos2 ap
2  cos ub
sin u
(13.21)
5 30 I2
o 3
cos2 ap
2  cos ub
sin u
where h 5 120p has been substituted assuming free space as the medium of propagation.
Due to the nature of the integrand in eq. (13.21),
p/2
cos2ap
2  cos ub
sin u
du 5 3
p/2
cos2ap
2  cos ub
sin u
This is easily illustrated by a rough sketch of the variation of the integrand with . Hence
Prad 5 60I2
o 3
p/2
cos2 ap
2  cos ub du
sin u
(13.22)
Changing variables, u 5 cos u, and using partial fraction reduces eq. (13.22) to
Prad 5 60I2
o 3
cos2 1
2pu
1 2 u2  du
5 30I2
o £
cos2 1
2pu
1 1 u  du 1 3
cos2 1
2pu
1 2 u  du§ 
(13.23)
Prad 5 3
ave # dS
700  CHAPTER 13  ANTENNAS
Replacing 1 1 u with v in the first integrand and 1 2 u with v in the second results in
Prad 5 30I2
o £
sin2 1
2pv
dv 1 3
sin2 1
2pv
dv §
5 30I2
o 3
sin2 1
2pv
(13.24)
Changing variables, w 5 pv, yields
Prad 5 30I2
o 3
sin2 1
2 w
5 15I2
o 3
11 2 cos w2
(13.25)
5 15I2
o 3
c w
2! 2 w3
4! 1 w5
6! 2 w7
8! 1 . . .d  dw
since cos w 5 1 2 w2
2! 1 w4
4! 2 w6
6! 1 w8
8! 2 . . .
. Integrating eq. (13.25) term by term and
evaluating at the limit leads to
Prad 5 15I2
o c
12p2 2
212!2 2
12p2 4
414!2 1
12p2 6
616!2 2
12p2 8
818!2 1 . . .d
. 36.56 I2
(13.26)
The radiation resistance Rrad for the half-wave dipole antenna is readily obtained from
eqs. (13.12) and (13.26) as
Rrad 5 2Prad
. 73 V
(13.27)
Note the significant increase in the radiation resistance of the half-wave dipole over that of
the Hertzian dipole. Thus the half-wave dipole is capable of delivering greater amounts of
power to space than the Hertzian dipole.
The total input impedance Zin of the antenna is the impedance seen at the terminals
of the antenna and is given by
Zin 5 Rin 1 jXin
(13.28)
13.4 Quarter-Wave Monopole Antenna  701
where Rin 5 Rrad for a lossless antenna. Deriving the value of the reactance Xin involves
a complicated procedure beyond the scope of this text. It is found that Xin 5 42.5 V, so
Zin 5 73 1 j42.5 V for a dipole length , 5 l/2. The inductive reactance drops rapidly to
zero as the length of the dipole is slightly reduced. For , 5 0.485 l, the dipole is resonant,
with Xin 5 0. Thus in practice, a l/2 dipole is designed such that Xin approaches zero and
Zin . 73 V. This value of the radiation resistance of the l/2 dipole antenna is the reason
for the standard 75 V coaxial cable. Also, the value is easy to match to transmission lines.
These factors in addition to the resonance property are the reasons for the dipole antenna’s
popularity and its extensive use.
13.4  QUARTER-WAVE MONOPOLE ANTENNA
Basically, the quarter-wave monopole antenna consists of half of a half-wave dipole anten­
na located on a conducting ground plane, as in Figure 13.5. The monopole antenna is per­
pendicular to the plane, which is usually assumed to be infinite and perfectly conducting.
It is fed by a coaxial cable connected to its base.
Using image theory of Section 6.6, we replace the infinite, perfectly conducting ground
plane with the image of the monopole. The field produced in the region above the ground
plane due to the l/4 monopole with its image is the same as the field due to a l/2 wave
dipole. Thus eq. (13.19) holds for the l/4 monopole. However, the integration in eq. (13.21)
is only over the hemispherical surface above the ground plane (i.e., 0 # u # p/2) because
the monopole radiates only through that surface. Hence, the monopole radiates only half
as much power as the dipole with the same current. Thus for a l/4 monopole,
Prad . 18.28 I2
(13.29)
and
Rrad 5 2Prad
Rrad . 36.5 V
(13.30)
By the same token, the total input impedance for a l/4 monopole is Zin 5 36.5 1 j21.25 V.
FIGURE 13.5  The monopole antenna.
702  CHAPTER 13  ANTENNAS
The loop antenna is of practical importance. It is used as a directional finder (or
search loop) in radiation detection and as a TV antenna for ultrahigh frequencies. The
term “small” implies that the dimensions (such as ro) of the loop are much smaller than l.
Consider a small filamentary circular loop of radius ro carrying a uniform current,
Io cos vt, as in Figure 13.6. The loop may be regarded as an elemental magnetic dipole. The
magnetic vector potential at the field point P due to the loop is
A 5 C
m3I4 dl
4prr 
(13.31)
where 3I4 5 Io cos 1vt 2 brr2 5 Re 3Ioe j1vt2brr24. Substituting [I] into eq. (13.31), we
obtain A in phasor form as
As 5 mIo
4p C
e2jbrr
rr  dl
(13.32)
Evaluating this integral requires a lengthy procedure. It can be shown that for a small
loop 1ro V l2, r can be replaced by r in the denominator of eq. (13.32) and As has only
a f-component given by
Afs 5 mIoS
4pr2 11 1 jbr2e2jbr sin u
(13.33)
where S 5 pr2
o 5 loop area. For a loop with N turns, S 5 Npr2
o. Using the fact that
Bs 5 mHs 5 = 3 As and = 3 Hs 5 jveEs, we obtain the electric and magnetic fields from
eq. (13.33) as
Efs 5
2jvmIoS
sin u c
r 1 1
r2 d  e2jbr
(13.34a)
Hrs 5
jvmIoS
2ph  cos u c 1
r2 2
br3 d  e2jbr
(13.34b)
Hus 5
jvmIoS
4ph  sin u c
r 1 1
r2 2
br3 d  e2jbr
(13.34c)
Ers 5 Eus 5 Hfs 5 0
(13.34d)
Comparing eqs. (13.5) and (13.6) with eq. (13.34), we observe the dual nature of the field
due to an electric dipole of Figure 13.3 and the elemental magnetic dipole of Figure 13.6
(see Table 8.2 also). At far field, only the 1/r term (the radiation term) in eq.  (13.34)
­remains. Thus at far field,
13.5  SMALL-LOOP ANTENNA
13.5 Small-Loop Antenna  703
Efs 5 vmIoS
4pr  b sin u e2jbr
5 hpIoS
rl2  sin u e2jbr
Efs 5 120p2Io
l2 sin u e2jbr,  Hus 5 2
Efs
h 
(13.35a)
Ers 5 Eus 5 Hrs 5 Hfs 5 0
(13.35b)
where h 5 120p for free space has been assumed. Though the far-field expressions in
eqs. (13.35) are obtained for a small circular loop, they can be used for a small square loop
with one turn 1S 5 a22 or with N turns 1S 5 Na22, or for any small loop, provided the loop
dimensions are small (d # l/10, where d is the largest dimension of the loop). It is left as
an exercise to show that using eqs. (13.13a) and (13.35) gives the radiation resistance of a
small loop antenna as
Rrad 5 320 p4S2
(13.36)
FIGURE 13.6  The small-loop antenna.
A magnetic field strength of 5 mA/m is required at a point on u 5 p/2, which is 2 km from
an antenna in air. Neglecting ohmic loss, how much power must the antenna transmit if
it is
(a)	 A Hertzian dipole of length /25?
(b)	 A half-wave dipole?
EXAMPLE 13.1
704  CHAPTER 13  ANTENNAS
(c)	 A quarter-wave monopole?
(d)	 A 10-turn loop antenna of radius ro 5 l/20?
Solution:
(a)	 For a Hertzian dipole,
0 Hfs 0 5 Iob dl sin u
4pr
where dl 5 l/25 or b dl 5 2p
# l
25 5 2p
25 . Hence,
5 3 1026 5
Io # 2p
25 112
4p 12 3 1032 5 Io
105
Io 5 0.5 A
Prad 5 40p2 c dl
l d
o 5 40p210.52 2
1252 2
5 158 mW
(b)	 For a l/2 dipole,
0 Hfs 0 5
Io cos ap
2  cos ub
2pr sin u
5 3 1026 5
Io # 1
2p 12 3 1032 # 112
Io 5 20p mA
Prad 5 1
2 I2
o Rrad 5 1
2  120p2 2 3 10261732
5 144 mW
(c)	 For a l/4 monopole,
Io 5 20p mA
as in part (b).
Prad 5 1
2 I2
o Rrad 5 1
2 120p2 2 3 1026136.562
5 72 mW
13.5 Small-Loop Antenna  705
(d)	 For a loop antenna,
0 Hus 0 5 pIo
r  S
l2 sin u
For a single turn, S 5 pr2
o. For N-turn, S 5 Npr2
o. Hence,
5 3 1026 5 pIo10p
2 3 103 c ro
l d
Io 5
10p2 c l
ro d
3 1023 5 202
p2 3 1023
5 40.53 mA
Rrad 5 320 p4 S2
5 320 p6 N2 c ro
l d
5 320 p6 3 100 c 1
20 d
5 192.3 V
Prad 5 1
2 I2
o Rrad 5 1
2 140.532 2 3 1026 1192.32
5 158 mW
PRACTICE EXERCISE  13.1
A Hertzian dipole of length l/100 is located at the origin in free space and fed with a
current of 0.25 sin 108t A. Determine the magnetic field at
(a)  r 5 l/5, u 5 30
(b)  r 5 200l, u 5 60
Answer:  (a) 0.2119 sin 1108t 2 20.5°2 af mA/m,  (b) 0.2871 sin 1108t 1 90°2 af
mA/m.
An electric field strength of 10 mV/m is to be measured at an observation point u 5 p/2,
500 km from a half-wave (resonant) dipole antenna operating in air at 50 MHz.
(a)	 What is the length of the dipole?
(b)	 Calculate the current that must be fed to the antenna.
(c)	 Find the average power radiated by the antenna.
(d)	 If a transmission line with Zo 5 75 V is connected to the antenna, determine the
standing wave ratio.
EXAMPLE 13.2
706  CHAPTER 13  ANTENNAS
Solution:
(a)	 The wavelength l 5 c
f 5 3 3 108
50 3 106 5 6 m.
Hence, the length of the half-dipole is , 5 l
2 5 3 m.
(b)	 From eq. (13.19),
0 Eus 0 5
hoIo cos ap
2  cos ub
2pr sin u
Io 5
0 Eus 0  2pr sin u
ho cos ap
2  cos ub
5 10 3 1026 2p 1500 3 1032 # 112
120p 112
5 83.33 mA
(c)
Rrad . 73 V
Prad 5 1
2 I2
o Rrad 5 1
2 183.332 2 3 1026 3 73
5 253.5 mW
(d)
G 5 ZL 2 Zo
ZL 1 Zo
1ZL 5 Zin in this case2
73 1 j42.5 2 75
73 1 j42.5 1 75 5
22 1 j42.5
148 1 j42.5
42.55l92.69°
153.98l16.02° 5 0.2763l76.67°
iii
s 5 1 1 0 G 0
1 2 0 G 0 5 1 1 0.2763
1 2 0.2763 5 1.763
PRACTICE EXERCISE  13.2
Repeat Example 13.2 with the dipole antenna replaced by a l/4 monopole.
Answer:  (a) 1.5 m,  (b) 83.33 mA,  (c) 126.8 mW,  (d) 2.265.
13.6 Antenna Characteristics  707
Having considered the basic elementary antenna types, we now discuss some important
characteristics of antennas as radiators of electromagnetic energy. These characteristics
A.  Antenna Patterns
When the amplitude of a specified component of the E field is plotted, it is called the field
pattern or voltage pattern. When the square of the amplitude of E is plotted, it is called
the power pattern. A three-dimensional plot of an antenna pattern is avoided by plotting
separately the normalized 0 Es 0  versus  for a constant f (this is called an E-plane pattern or
­vertical pattern) and the normalized 0 Es 0  versus f for u 5 p/2 (called the H-plane pattern
or horizontal pattern). The normalization of 0 Es 0  is with respect to the maximum value of
the 0 Es 0  so that the maximum value of the normalized 0 Es 0  is unity.
For the Hertzian dipole, for example, the normalized 0 Es 0  is obtained from eq. (13.8a) as
f1u2 5 0 sin u 0 
(13.37)
which is independent of f. From eq. (13.37), we obtain the E-plane pattern as the polar
plot of f() with  varying from 0° to 180°. The result is shown in Figure 13.7(a). Note that
the plot is symmetric about the z-axis 1u 5 02. For the H-plane pattern, we set u 5 p/2
so that f1u2 5 1, which is circle of radius 1 as shown in Figure 13.7(b). When the two
13.6  ANTENNA CHARACTERISTICS
FIGURE 13.7  Field patterns of the Hertzian dipole: (a) normalized
E-plane or vertical pattern (f 5 constant 5 0), (b) normalized H-plane
or horizontal pattern ( 5 p/2), (c) three-dimensional pattern.
include (a) antenna patterns, (b) radiation intensity, (c) directive gain, (d) power gain.
708  CHAPTER 13  ANTENNAS
plots of ­Figure 13.7(a) and (b) are combined, we have the three-dimensional field pattern
of Figure 13.7(c), which has the shape of a doughnut.
A plot of the time-average power, |ave| 5 ave, for a fixed distance r is the power
­pattern of the antenna. It is obtained by plotting separately ave versus  for constant f and
ave versus f for constant .
For the Hertzian dipole, the normalized power pattern is easily obtained from eqs.
(13.37) or (13.9) as
f 21u2 5 sin2 u
(13.38)
which is sketched in Figure 13.8. Notice that Figures 13.7(b) and 13.8(b) show circles
­because f() is independent of f and that the value of OP in Figure 13.8(a) is the relative
average power for that particular . Thus, at point Q 1u 5 45°2, the average power is half
the maximum average power (the maximum average power is at u 5 p/2).
An antenna pattern (or radiation pattern) is a three-dimensional plot of its radiation
at far field.
B.  Radiation Intensity
FIGURE 13.8  Power patterns of the Hertzian dipole: (a) (f 5 constant 5 0),
(b)  5 constant 5 p/2.
The radiation intensity of an antenna is defined as
U1u, f2 5 r2 ave
(13.39)
13.6 Antenna Characteristics  709
From eq. (13.39), the total average power radiated can be expressed as
Prad 5 C
ave dS 5 C
ave r2 sin u du df
5 3
U1u, f2 sin u du df
(13.40)
5 3
f50
u50
U1u, f2 dV
where dV 5 sin u du df is the differential solid angle in steradian (sr). Hence the radiation
intensity U1u, f2 is measured in watts per steradian (W/sr). The average value of U1u, f2
is the total radiated power divided by 4p sr; that is,
Uave 5 Prad
4p 
(13.41)
C.  Directive Gain
Besides the antenna patterns just described, we are often interested in measurable quanti­
ties such as gain and directivity to determine the radiation characteristics of an antenna.
The directive gain Gd(, ) of an antenna is a measure of the concentration of the
radiated power in a particular direction (, ).
It may be regarded as the ability of the antenna to direct radiated power in a given direc­
tion. It is usually obtained as the ratio of radiation intensity in a given direction 1u, f2 to
the average radiation intensity, that is,
Gd1u, f2 5 U1u, f2
Uave
5 4p U1u, f2
Prad
(13.42)
By substituting eq. (13.39) into eq. (13.42), ave may be expressed in terms of directive
gain as
The directive gain Gd1u, f2 depends on antenna pattern. For the Hertzian dipole (as well
as for l/2 dipole and l/4 monopole), we notice from Figure 13.8 that ave is maximum at
u 5 p/2 and minimum (zero) at u 5 0 or p. Thus the Hertzian dipole radiates power in
a direction broadside to its length. For an isotropic antenna (one that radiates equally in all
directions), Gd 5 1. However, such an antenna is not a physicality but an ideality.
The directivity D of an antenna is the ratio of the maximum radiation intensity to the
average radiation intensity.
ave 5 Gd
4pr2 Prad
(13.43)
710  CHAPTER 13  ANTENNAS
Obviously, D is the maximum directive gain Gd max. Thus
D 5 Umax
Uave
5 Gd max
(13.44a)
or, from eq. (13.41),
D 5 4p Umax
Prad
(13.44b)
For an isotropic antenna, D 5 1; this is the smallest value D can have. For the Hertzian ­dipole,
Gd1u, f2 5 1.5 sin2 u,  D 5 1.5
(13.45)
For the l/2 dipole,
Gd1u, f2 5
pRrad
f 21u2,  D 5 1.64
(13.46)
where h 5 120p, Rrad . 73 V, and
f1u2 5
cos ap
2  cos ub
sin u
(13.47)
D.  Power Gain
Our definition of the directive gain in eq. (13.42) does not account for the ohmic power loss
P, of the antenna. This power loss P, occurs because the antenna is made of a conductor with
finite conductivity. As illustrated in Figure 13.9, if Pin is the total input power to the antenna,
Pin 5 P, 1 Prad
5 1
2 0 Iin 0 2 1R, 1 Rrad2
(13.48)
where Iin is the current at the input terminals and R, is the loss or ohmic resistance of the
antenna. In other words, Pin is the power accepted by the antenna at its terminals during
the radiation process, and Prad is the power radiated by the antenna; the difference between
the two powers is P,, the power dissipated within the antenna.
rad
FIGURE 13.9  Relating Pin, P, and Prad.
13.6 Antenna Characteristics  711
We define the power gain Gp1u, f2 of the antenna as
Gp1u, f2 5 4p U1u, f2
Pin
(13.49)
The ratio of the power gain in any specified direction (, f) to the directive gain in that
hr 5 GP
5 Prad
Pin
Introducing eq. (13.48) leads to
hr 5 Prad
Pin
Rrad
Rrad 1 R,
(13.50)
For many antennas, hr is close to 100% so that GP . Gd. It is customary to express directiv­
ity and gain in decibels. Thus
D 1dB2 5 10 log10 D
(13.51a)
G 1dB2 5 10 log10 G
(13.51b)
It should be mentioned at this point that the radiation patterns of an antenna are mea­
sured in the far-field region. The far-field region of an antenna is commonly taken to exist
at a distance r $ rmin, where
rmin 5 2d2
l 
(13.52)
and d is the largest dimension of the antenna. For example, d 5 , for the electric dipole
­antenna and d 5 2ro for the small-loop antenna.
Show that the directive gain of the Hertzian dipole is
Gd1u, f2 5 1.5 sin2 u
and that of the half-wave dipole is
Gd1u, f2 5 1.64
cos2ap
2  cos ub
sin2 u
EXAMPLE 13.3
direction is referred to as the radiation efficiency h  of the antenna; that is,
712  CHAPTER 13  ANTENNAS
Solution:
Starting from eq. (13.42) and introducing the expressions for U(, f) and Prad, we obtain
Gd1u, f2 5
4p f 21u2
3 f 2 1u2 dV
(a)	 For the Hertzian dipole,
Gd1u, f2 5
4p sin2 u
f50
u50
sin3 u du df
5 4p sin2 u
2p 14/32
5 1.5 sin2 u
as required.
(b)	 For the half-wave dipole,
Gd1u, f2 5
4p cos2ap
2  cos ub
sin2 u
f50
u50
cos2ap
2  cos ub du df
sin u
From eq. (13.26), the integral in the denominator gives 2p11.21882. Hence,
Gd1u, f2 5
4p cos2ap
2  cos ub
sin2 u
2p 11.21882
5 1.64
cos2ap
2  cos ub
sin2 u
as required.
PRACTICE EXERCISE  13.3
Calculate the directivity of
(a)  The Hertzian monopole
(b)  The quarter-wave monopole
Answer:  (a) 3,  (b) 3.28.
13.6 Antenna Characteristics  713
Determine the electric field intensity at a distance of 10 km from an antenna having a
­directive gain of 5 dB and radiating a total power of 20 kW.
Solution:
5 5 Gd 1dB2 5 10 log10 Gd
0.5 5 log10 Gd S  Gd 5 100.5 5 3.162
From eq. (13.43),
ave 5 GdPrad
4pr2
But
ave 5
0 Es 0 2
Hence,
0 Es 0 2 5 hGdPrad
2pr2
5 120p13.1622 120 3 1032
2p 310 3 10342
0 Es 0 5 0.1948 V/m
PRACTICE EXERCISE  13.4
A certain antenna with an efficiency of 95% has maximum radiation intensity of
0.5 W/sr. Calculate its directivity when
(a)  The input power is 0.4 W
(b)  The radiated power is 0.3 W
Answer:  (a) 16.53,  (b) 20.94.
The radiation intensity of a certain antenna is
U1u, f2 5 e2 sin u sin3 f,
0 # u # p, 0 # f # p
elsewhere
Determine the directivity of the antenna.
EXAMPLE 13.4
EXAMPLE 13.5
714  CHAPTER 13  ANTENNAS
Solution:
The directivity is defined as
D 5 Umax
Uave
From the given U,
Umax 5 2
From eqs. (13.40) and (13.41), we get the expression for the average radiated intensity.
Uave 5 1
4p 3 U 1u, f2 dV
5 1
4p 3
f50
u50
2 sin u sin3 f sin u du df
5 1
2p 3
sin2 u du 3
sin3 f df
5 1
2p 3
2 11 2 cos 2u2 du 3
11 2 cos2 f2 d12cos f2
5 1
2p 1
2 au 2 sin 2u
b `
acos3 f
2 cos fb `
5 1
2p ap
2 b a4
3b 5 1
Hence
D 5
11/32 5 6
PRACTICE EXERCISE  13.5
Evaluate the directivity of an antenna with normalized radiation intensity
U1u, f2 5 esin u,
0 # u # p/2, 0 # f # 2p
otherwise
Answer:  2.546.
13.7 Antenna Arrays  715
In many practical applications (e.g., in an AM broadcast station), it is necessary to design
antennas with more energy radiated in some particular directions and less in other directions.
This is tantamount to requiring that the radiation pattern be concentrated in the direction of
interest. This is hardly achievable with a single antenna element. An antenna array is used to
obtain greater directivity than can be obtained with a single antenna element.
An antenna array is a group of radiating elements arranged to produce particular
­radiation characteristics.
It is practical and convenient that the array consists of identical elements, but this is not
fundamentally required. We shall consider the simplest case of a two-element array and
extend our results to the more complicated, general case of an N-element array.
Consider an antenna consisting of two Hertzian dipoles placed in free space along the
z-axis but oriented parallel to the x-axis as depicted in Figure 13.10. We assume that the
­dipole at 10, 0, d/22 carries current I1s 5 Iola and the one at 10, 0, 2d/22 carries current
I2s 5 Iol0, where a is the phase difference between the two currents. By varying the spacing
d and phase difference a, the fields from the array can be made to interfere constructively
(add) in certain directions of interest and interfere destructively (cancel) in other ­directions.
The total electric field at point P is the vector sum of the fields due to the individual elements.
If P is in the far-field zone, we obtain the total electric field at P from eq. (13.8a) as
Es 5 E1s 1 E2s
jhbIodl
ccos u1 e2jbr1
e ja au1 1 cos u2 e2jbr2
au2d 
(13.53)
Note that sin  in eq. (13.8a) has been replaced by cos  because the element of Figure 13.3
is z-directed, whereas those in Figure 13.10 are x-directed. Since P is far from the array,
u1 . u . u2 and au1 . au . au2. In the amplitude, we can set r1 . r < r2 but in the phase,
we use
r1 . r 2 d
2 cos u
(13.54a)
13.7  ANTENNA ARRAYS
FIGURE 13.10  A two-element array.
716  CHAPTER 13  ANTENNAS
r2 . r 1 d
2 cos u
(13.54b)
Thus eq. (13.53) becomes
Es 5
jhbIo dl
4p r  cos u e2jbre ja/23e j1bd cos u2/2e ja/2 1 e2j1bd cos u2/2e2ja/24 au
jhbIo dl
4p r  cos u e2jbre ja/22 cos c1
2 1bd cos u 1 a2d  au
(13.55)
Comparing this with eq. (13.8a) shows that the total field of an array is equal to the field of
single element located at the origin multiplied by an array factor given by
AF 5 2 cos c 1
2 1bd cos u 1 a2d  e ja/2
(13.56)
Thus, in general, the far field due to a two-element array is given by
E 1total2 5 1E due to single element at origin2 3 1array factor2
(13.57)
Also, from eq. (13.55), note that 0 cos u 0  is the radiation pattern due to a single element,
whereas the normalized array factor, 0 cos 31/21bd cos u 1 a2 4 0 , is the radiation pattern
the array would have if the elements were isotropic. These may be regarded as “unit pat­
tern” and “group pattern,” respectively. Thus the “resultant pattern” is the product of the
resultant pattern 5 unit pattern 3 group pattern
(13.58)
This is known as pattern multiplication, and it can be used to sketch, almost by inspec­
tion, the pattern of an array. Therefore, pattern multiplication is a useful tool in the
design of an array. We should note that while the unit pattern depends on the type of
elements comprising the array, the group pattern is independent of the element type
as long as the spacing d, the phase difference a, and the orientation of the elements
remain the same.
Let us now extend the results on the two-element array to the general case of an
eq. (13.57) once the array factor is known. For the uniform linear array, the array factor is
the sum of the contributions by all the elements. Thus,
AF 5 1 1 e jc 1 e j2c 1 e j3c 1 . . . 1 e j1N212c
(13.59)
N-element array shown in Figure 13.11. We assume that the array is linear in that the ele-
ments are spaced equally along a straight line and lie along the z-axis. Also, we assume
that the array is uniform so that each element is fed with current of the same magnitude
1s 5 Iol0
i, I2s 5 Iola
i, I3s 5 Iol2a
i , and so on.
We are mainly interested in finding the array factor; the far field can easily be found from
unit pattern and the group pattern; that is,
but of progressive phase shift a; that is, I
13.7 Antenna Arrays  717
where
c 5 bd cos u 1 a
(13.60)
phase shift. Notice that the right-hand side of eq. (13.59) is a geometric series of the form
1 1 x 1 x2 1 x3 1 . . . 1 xN21 5 1 2 xN
1 2 x 
(13.61)
Hence eq. (13.59) becomes
AF 5 1 2 e jNc
1 2 e jc 
(13.62)
which can be written as
AF 5 e jNc 2 1
e jc 2 1 5 e jNc/2
e jc/2  e jNc/2 2 e2jNc/2
e jc/2 2 e2jc/2
5 e j1N212c/2 sin 1Nc/22
sin 1c/22
(13.63)
The phase factor e j1N212c/2 would not be present if the array were centered about the origin.
Neglecting this unimportant term, we have
0 AF 0 5 4
sin Nc
sin c
4  ,  c 5 bd cos u 1 a
(13.64)
FIGURE 13.11  An N-element uniform linear array.
In eq. (13.60), b 5 2p/l, and d and a are, respectively, the spacing, and the interelement
718  CHAPTER 13  ANTENNAS
Note that this equation reduces to eq. (13.56) when 0 AF 0  is considered and N 5 2 as
expected. Also, note the following:
1.	 Since 0 AF 0  has the maximum value of N, the normalized 0 AF 0  is obtained by
dividing 0 AF 0
0 5 bd cos u 1 a  or  cos u 5 2 a
(13.65)
2.	 When 0 AF 0 5 0, 0 AF 0  has nulls (or zeros); that is,
2 5 6kp,  k 5 1, 2, 3, . . .
(13.66)
where k is not a multiple of N.
3.	 A broadside array has its maximum radiation directed normal to the axis of the
|     |
|     |
|     |
FIGURE 13.12  Array factors for uniform linear
arrays.
by N. The principal maximum occurs when c 5 0; that is,
array; that is, c 5 0, u 5 90º so that a 5 0.
13.7 Antenna Arrays  719
4.	 An end-fire array has its maximum radiation directed along the axis of the array,
that is,  c 5 0, u 5 c
so that a 5 c
2bd
These points are helpful in plotting 0 AF 0 . For N 5 2, 3, and 4, the plots of 0 AF 0  are
sketched in Figure 13.12.
For the two-element antenna array of Figure 13.10, sketch the normalized field pattern
when the currents are:
(a)  Fed in phase 1a 5 02, d 5 l/2
(b)  Fed 90° out of phase 1a 5 p/22, d 5 l/4
Solution:
The normalized field of the array is obtained from eqs. (13.55) to (13.57) as
f1u2 5 `cos u cos c 1
2 1bd cos u 1 a2 d `
(a)	 If a 5 0, d 5 l/2, bd 5 2p
l  l
2 5 p. Hence,
f1u2
0 cos u 0
`cos
2  1cos u2 `
resultant 5
unit
group
pattern
pattern
pattern
The sketch of the unit pattern is straightforward. It is merely a rotated version of that
in Figure 13.7(a) for the Hertzian dipole and is shown in Figure 13.13(a). To sketch a group
pattern, we must first determine nulls and maxima. For the nulls (or zeros),
cos ap
2  cos ub 5 0 S  p
2  cos u 5 6 p
u 5 0°, 180°
For the maxima,
cos ap
2  cos ub 5 1 S  cos u 5 0
EXAMPLE 13.6
720  CHAPTER 13  ANTENNAS
u 5 90°
The group pattern, shown in Figure 13.12(b), is the polar plot obtained by sketching
`cos ap
2  cos ub `  for u 5 0, 5°, 10°, 15°, .  .  . , 180° and incorporating the nulls and maxima
at u 5 0°, 180° and u 5 90°, respectively. Multiplying Figure 13.13(a) with Figure 13.13
(b) gives the resultant pattern in Figure 13.13(c). MATLAB can easily be used to do this. It
should be observed that the field patterns in Figure 13.13 are in the plane containing the
axes of the elements. Note the following: (1) In the yz-plane, which is normal to the axes of
the elements, the unit pattern 15 12 is a circle [see Figure 13.7(b)] while the group pattern
remains as in Figure 13.13(b); therefore, the resultant pattern is the same as the group pat-
tern in this case. (2) In the xy-plane, u 5 p/2, so the unit pattern vanishes while the group
pattern 15 12 is a circle.
(b)	 If a 5 p/2, d 5 l/4, and bd 5 2p
l  l
4 5 p
f1u2
0 cos u 0
`cos
4  1cos u 1 12 `
resultant 5
unit
group
pattern
pattern
pattern
The unit pattern remains as in Figure 13.13(a). For the group pattern, the null occurs when
cos p
4  11 1 cos u2 5 0 S  p
4  11 1 cos u2 5 p
cos u 5 1 S  u 5 0
FIGURE 13.13  For part (a) of Example 13.6: field patterns in the plane
containing the axes of the elements.
13.7 Antenna Arrays  721
The maxima and minima occur when
du ccos p
4  11 1 cos u2 d 5 0 S  sin u sin p
4  11 1 cos u2 5 0
sin u 5 0 S  u 5 0°, 180°
and
sin p
4  11 1 cos u2 5 0 S  cos u 5 21  or  u 5 180°
Each field pattern is obtained by varying u 5 0°, 5°, 10°, 15°, .  .  . , 180°. Note that
u 5 180° corresponds to the maximum value of 0 AF 0 , whereas u 5 0° corresponds to
the null. Thus the unit, group, and resultant patterns in the plane containing the axes of
the elements are shown in Figure 13.14. Observe from the group patterns that the broad­
side array 1a 5 02 in Figure 13.13 is bidirectional, while the end-fire array 1a 5 bd2 in
Figure 13.14 is unidirectional.
FIGURE 13.14  For part (b) of Example 13.6; field patterns in the plane
containing the axes of the elements.
PRACTICE EXERCISE  13.6
Repeat Example 13.6 for the following cases: (a) a 5 p, d 5 l/2, (b) a 5 2p/2,
d 5 l/4.
Answer:  See Figure 13.15.
722  CHAPTER 13  ANTENNAS
Consider a three-element array that has current ratios 121 as in Figure 13.16(a). Sketch
Each group is a two-element array with d 5 l/2, a 5 0, so that the group pattern of
the two-­element array (or the unit pattern for the three-element array) is as shown in
Figure 13.13(b). The two groups form a two-element array similar to Example 13.6(a)
with d 5 l/2, a 5 0, so that the group pattern is the same as that in Figure 13.13(b).
Thus, in this case, both the unit and group patterns are the same pattern in Figure
13.13(b). The ­resultant group pattern is obtained in Figure 13.17(c). We should note that
the pattern in Figure 13.17(c) is not the resultant pattern but the group pattern of the
three-element array. The resultant group pattern of the array is Figure 13.17(c) multi­
plied by the field pattern of the element type.
FIGURE 13.15  For Practice Exercise 13.6.
EXAMPLE 13.7
the group pattern in the plane containing the axes of the elements.
Solution:
For the purpose of analysis, we split the middle element in Figure 13.16(a) carrying cur-
rent 2Il0°
i into two elements each carrying current Il0°
i . This results in four elements
instead of three, as shown in Figure 13.16(b). If we consider elements 1 and 2 as a group
and elements 3 and 4 as another group, we have a two-element array of Figure 13.16(c).
13.7 Antenna Arrays  723
An alternative method of obtaining the resultant group pattern of the three-element
array of Figure 13.16 is by following steps similar to those taken to obtain eq. (13.59). We
obtain the normalized array factor (or the group pattern) as
1AF2 n 5 1
4 0 1 1 2ejc 1 e j2c 0
5 1
4 0 e jc 0 0 2 1 e2jc 1 e jc 0
5 1
2 0 1 1 cos c 0 5 `cos c
2 `
where c 5 bd cos u 1 a if the elements are placed along the z-axis but oriented parallel to
the x-axis. Since a 5 0, d 5 l/2, bd 5 2p
# l
2 5 p, and
1AF2 n 5  `cos ap
2  cos ub `
1AF2 n
5 `cos ap
2  cos ub `
`cos ap
2  cos ub `
resultant
unit
group
group pattern
pattern
pattern
The sketch of these patterns is exactly what is in Figure 13.17.
FIGURE 13.16  For Example 13.7: (a) a three-element
array with current ratios 121; (b) and (c) equivalent
two-element arrays.
724  CHAPTER 13  ANTENNAS
If two three-element arrays in Figure 13.16(a) are displaced by l/2, we obtain
a four-­element array with current ratios 1331 as in Figure 13.18. Two of such
four-element ­arrays, displaced by l/2, give a five-element array with current ratios
14641. Continuing this process results in an N-element array, spaced l/2 and
1N 2 12l/2 long, whose current ratios are the binomial coefficients. Such an array is
called a linear binomial array.
FIGURE 13.18  For Example
13.7 and Practice Exercise 13.7:
four-element array with current
ratios 1331.
FIGURE 13.17  For Example 13.7;
obtaining the resultant group pattern
of the three-element array of Figure
13.16(a).
PRACTICE EXERCISE  13.7
(a)  Sketch the resultant group pattern for the four-element array with current ratios
1331 shown in Figure 13.18.
(b)  Derive an expression for the group pattern of a linear binomial array of N elements.
Assume that the elements are placed along the z-axis, oriented parallel to the x-axis
with spacing d and interelement phase shift a.
Answer:  (a) See Figure 13.19,  (b) `cos c
2 `
N21
, where c 5 bd cos u 1 a.
FIGURE 13.19  For part (a) of Practice Exercise 13.7.
13.8 Effective Area and the Friis Equation  725
When the incoming EM wave is normal to the entire surface of a receiving antenna, the
This necessitates the idea of the effective area of a receiving antenna.
The concept of effective area or effective aperture (receiving cross section of an
antenna) is usually employed in the anaysis of receiving antennas.
The effective area Ae of a receiving antenna is the ratio of the time-average power
received Pr (or delivered to the load, to be strict) to the time-average power density
ave of the incident wave at the antenna.
to extract energy from a passing EM wave.
Let us derive the formula for calculating the effective area of the Hertzian dipole ­acting
as a receiving antenna. The Thévenin equivalent circuit for the receiving antenna is shown
in Figure 13.20, where Voc is the open-circuit voltage induced on the antenna terminals
by a remote transmitter, Zin 5 Rrad 1 jXin is the antenna impedance, and ZL 5 RL 1 jXL
Pr 5 1
2 c
0 Voc 0
2Rrad
Rrad
0 Voc 0 2
8 Rrad
(13.69)
†13.8  EFFECTIVE AREA AND THE FRIIS EQUATION
FIGURE 13.20  Thévenin equivalent of a receiving
antenna.
power received is
But in most cases, the incoming EM wave is not normal to the entire surface of the antenna.
Pr 5 3
ave # dS 5 aveS
(13.67)
That is,
From eq. (13.68), we notice that the effective area is a measure of the ability of the antenna
Ae 5 Pr
ave
(13.68)
is the external load impedance, which might be the input impedance to the transmission
line feeding the antenna. For maximum power transfer, ZL 5 Z*in and XL 5 2Xin. The
time-average power delivered to the matched load is therefore
726  CHAPTER 13  ANTENNAS
For the Hertzian dipole, eq. (13.13b) gives Rrad 5 80p21dl/l2 2 and Voc 5 E dl, where E is
the effective field strength parallel to the dipole axis. Hence, eq. (13.69) becomes
Pr 5 E2l2
640p2
(13.70)
Ae 5 3l2
8p 5 1.5 l2
Ae 5 l2
4p D
(13.72)
where D 5 1.5 is the directivity of the Hertzian dipole. Although eq. (13.72) was derived for
the Hertzian dipole, it holds for any antenna if D is replaced by Gd1u, f2. Thus, in general
Ae 5 l2
4p Gd1u, f2
(13.73)
Now suppose we have two antennas separated by distance r in free space as shown
in Figure 13.21. The transmitting antenna has effective area Aet and directive gain Gdt and
FIGURE 13.21  Transmitting and receiving antennas in free space.
Inserting eqs. (13.70) and (13.71) in eq. (13.68) gives
The time-average power at the antenna is
ave 5 E2
2h 5
240p
(13.71)
transmits a total power Pt 15 Prad2. The receiving antenna has effective area of Aer and
directive gain Gdr and receives a total power of Pr. At the transmitter,
Gdt 5 4pU
5 4pr2ave
ave 5
4pr2 Gdt
(13.74)
13.8 Effective Area and the Friis Equation  727
antenna to the power transmitted by the other, provided the two antennas are separated by
r $ 2d2/l, where d is the largest dimension of either antenna [see eq. (13.52)]. Therefore, to
apply the Friis equation, we must make sure that each antenna is in the far field of the other.
Find the maximum effective area of a l/2 wire dipole operating at 30 MHz. How much
power is received with an incident plane wave of strength 2 mV/m?
Solution:
Ae 5 l2
4p Gd1u, f2
l 5 c
f 5 3 3 108
30 3 106 5 10 m
Gd1u, f2 5
pRrad
f 21u2 5 120p
73p  f 21u2 5 1.64f 21u2
Gd max 5 1.64
Ae max 5 102
4p 11.642 5 13.05 m2
PRACTICE EXERCISE  13.8
Determine the maximum effective area of a Hertzian dipole of length 10 cm operating
at 100 MHz. If the antenna receives 3 mW of power, what is the power density of the
incident wave?
Answer:  1.074 m2, 2.793 mW/m2.
EXAMPLE 13.8
By applying eqs. (13.68) and (13.73), we obtain the time-average power received as
Substituting eq. (13.74) into eq. (13.75) results in
Pr 5 GdrGdtc l
4prd
(13.76)
This is referred to as the Friis transmission formula. It relates the power received by one
Pr 5 ave Aer 5 l2
4p Gdr ave
(13.75)
Pr 5 ave Ae 5 E0
2h Ae
12 3 10232 2
240p
13.05 5 69.23 nW
728  CHAPTER 13  ANTENNAS
The transmitting and receiving antennas are separated by a distance of 200 l and have
­directive gains of 25 dB and 18 dB, respectively. If 5 mW of power is to be received, calcu­
late the minimum transmitted power.
Solution:
Given that Gdt 1dB2 5 25 dB 5 10 log10 Gdt,
Gdt 5 102.5 5 316.23
Similarly,
Gdr 1dB2 5 18 dB  or  Gdr 5 101.8 5 63.1
Using the Friis equation, we have
Pr 5 GdrGdt c l
4prd
Pt 5 Pr c 4pr
l d
GdrGdt
5 5 3 1023 c 4p 3 200 l
163.12 1316.232
5 1.583 W
PRACTICE EXERCISE  13.9
An antenna in air radiates a total power of 100 kW so that a maximum radiated electric
field strength of 12 mV/m is measured 20 km from the antenna. Find (a) its ­directivity
in decibels, (b) its maximum power gain if hr 5 98%.
Answer:  (a) 20.18 dB,  (b) 9.408  103.
Radars are electromagnetic devices used for detection and location of objects. The term
radar is derived from the phrase radio detection and ranging. In a typical radar system, as
shown in Figure 13.22(a), pulses of EM energy are transmitted to a distant object. The same
antenna is used for transmitting and receiving, so the time interval between the ­transmitted
and reflected pulses is used to determine the distance of the target. If r is the distance
†13.9  THE RADAR EQUATION
EXAMPLE 13.9
13.9 The Radar Equation  729
between the radar and target and c is the speed of light, the elapsed time between the trans­
mitted and received pulse is 2r/c. By measuring the elapsed time, we determine r.
The ability of a target to scatter (or reflect) energy is characterized by its scattering cross
section  (also called the radar cross section). The scattering cross section has the units of
area and can be measured experimentally.
The scattering cross section is the equivalent area intercepting the amount of power
that, when scattering isotropically, produces at the radar a power density that is
equal to that scattered (or reflected) by the actual target.
That is,
where i is the incident power density at the target T while s is the scattered power
­density at the transceiver O as in Figure 13.22(b).
From eq. (13.43), the incident power density i at the target T is
The power received at transreceiver O is
Pr 5 Aer
FIGURE 13.22  (a) Typical radar
system. (b) Simplification of the
system in (a) for calculating the
target cross section s.
ps 5 lim
rS`
c si
4pr2 d
s 5 lim
rS`
4pr2 s
(13.77)
i 5 ave 5 Gd
4pr2 Prad
(13.78)
730  CHAPTER 13  ANTENNAS
Note that i and s are the time-average power densities in watts per square meter,
and  Prad and Pr are the total time-average powers in watts. Since Gdr 5 Gdt 5 Gd and
Aer 5 Aet 5 Ae, substituting eqs. (13.78) and (13.79) into eq. (13.77) gives
s 5 14pr22 2 Pr
Prad
Ae Gd
(13.80a)
Pr 5 AesGdPrad
14pr22 2 
(13.80b)
From eq. (13.73), Ae 5 l2Gd/4p. Hence,
Pr 5
1lGd2 2sPrad
14p2 3r4
(13.81)
This is the radar transmission equation for free space. It is the basis for measurement of
scattering cross section of a target. Solving for r in eq. (13.81) results in
r 5 c l2 G2
14p2 3 # Prad
1/4
(13.82)
Equation (13.82) is called the radar range equation. Given the minimum detectable power
of the receiver, the equation determines the maximum range for a radar. It is also useful for
obtaining engineering information concerning the effects of the various parameters on the
performance of a radar system.
The radar considered so far is the monostatic type because of the predominance of this
type of radar in practical applications. A bistatic radar is one in which the transmitter and
receiver are separated. If the transmitting and receiving antennas are at distances r1 and r2
from the target and Gdr 2 Gdt, eq. (13.81) for bistatic radar becomes
Pr 5 GdtGdr
4pr1r2
sPrad
(13.83)
Radar transmission frequencies range from 25 to 70,000 MHz. Table 13.1 shows radar
frequencies and their designations as commonly used by radar engineers.
s 5 Pr
Aer
(13.79)
13.9 The Radar Equation  731
An S-band radar transmitting at 3 GHz radiates 200 kW. Determine the signal power
­density at ranges 100 and 400 nautical miles if the effective area of the radar antenna is
9 m2. With a 20 m2 target at 300 nautical miles, calculate the power of the reflected signal
at the radar.
Solution:
The nautical mile is a common unit in radar communications.
1 nautical mile 1nm2 5 1852 m
l 5 c
f 5 3 3 108
3 3 109 5 0.1 m
Gdt 5 4p
l2  Aet 5
10.12 2 9 5 3600p
For r 5 100 nm 5 1.852 3 105 m
TABLE 13.1  Designations of Radar Frequencies
Designation
Frequency
UHF
300–1000 MHz
1000–2000 MHz
2000–4000 MHz
4000–8000 MHz
8000–12,500 MHz
12.5–18 GHz
18–26.5 GHz
Millimeter
.  35 GHz
EXAMPLE 13.10
Using eq. (13.80b)
Pr 5 Aes Gd Prad
34pr242
 5 GdtPrad
4pr2 5 3600p 3 200 3 103
4p 11.8522 2 3 1010
5 5.248 mW/m2
For r 5 400 nm 5 4 11.852 3 1052 m
 5 5.248
142 2 5 0.328 mW/m2
732  CHAPTER 13  ANTENNAS
where r 5 300 nm 5 5.556 3 105 m
Pr 5 9 3 20 3 3600p 3 200 3 103
34p 3 5.556242 3 1020
5 2.706 3 10214 W
The same result can be obtained by using eq. (13.81).
PRACTICE EXERCISE  13.10
A C-band radar with an antenna 1.8 m in radius transmits 60 kW at a frequency of
6000 MHz. If the minimum detectable power is 0.26 mW, for a target cross section of
5 m2, calculate the maximum range in nautical miles and the signal power density at
half this range. Assume unity efficiency and that the effective area of the antenna is 70%
of the actual area.
Answer:  0.031 nm, 501 W/m2.
†13.10  APPLICATION NOTE—ELECTROMAGNETIC
INTERFERENCE AND COMPATIBILITY
Every electronic device is a source of radiated electromagnetic fields called radiated
­emissions. These are often an accidental by-product of the design.
Electromagnetic interference (EMI) is the degradation in the performance of a ­device
due to the fields making up the electromagnetic environment.
Electromagnetic compatibility (EMC) is achieved when a device functions satisfacto­
rily without introducing intolerable disturbances to the electromagnetic environment
or to other devices in its neighborhood.
The electromagnetic environment consists of various apparatuses such as radio and TV
broadcast stations, radar, and navigational aids that radiate EM energy as they oper­
ate. Every electronic device is susceptible to EMI. Its influence can be seen all around
us. The results include “ghosts” in TV picture reception, taxicab radio interference with
police radio systems, power line transient interference with personal computers, and self-­
EMC1 is achieved when electronic devices coexist in harmony, such that each device func­
tions according to its intended purpose in the presence of, and in spite of, the others. EMI
1 For an in-depth treatment of EMC, see C. R. Paul, Introduction to Electromagnetic Compatibility, 2nd
ed. Hoboken, NJ: John Wiley & Sons, 2006.
oscillation of a radio receiver or transmitter circuit.
13.10 Application Note—Electromagnetic Interference and Compatibility   733
is the problem that occurs when unwanted voltages or currents are present to influence
the performance of a device, while EMC is the solution to the problem. The goal of EMC
is  system or subsystem compatibility, and this is achieved by applying proven design tech­
niques, the use of which ensures a system relatively free of EMI problems.
EMC is a growing field because of the ever-increasing density of electronic circuits in
modern systems for computation, communication, control, and so on. It is a concern not
only to electrical and computer engineers, but also to automotive engineers. The increas­
ing application of automotive electronic systems to improve fuel economy, reduce ­exhaust
emissions, ensure vehicle safety, and provide assistance to the driver has resulted in a grow­
ing need to ensure compatibility during normal operation. We will consider the sources
and characteristics of EMI. Later, we will examine EMI control techniques.
A.  Source and Characteristics of EMI
First, let us classify EMI in terms of its causes and sources. The classification will facilitate
recognition of sources and assist in determining means of control. As mentioned earlier,
any electronic device may be the source of EMI, although this is not the intention of the
designer. The cause of the EMI problem may be either within the system, in which case it
is termed an intrasystem problem, or from the outside, in which case it is called an intersys­
tem problem. Figure 13.23 shows intersystem EMI problems. The term “emitter” is com­
monly used to denote the source of EMI, while the term “susceptor” is used to designate a
victim device. Tables 13.2 and 13.3 present typical causes of intrasystem and intersystem
problems. Both intrasystem and intersystem EMI generally can be controlled by the sys­
tem design engineer by following some design guidelines and techniques. For intrasystem
EMI problems, for example, the design engineer may apply proper grounding and wiring
arrangements, shielding of circuits and devices, and filtering.
The sources of EMI can be classified as natural or artificial (manmade). The origins
of EMI are basically undesired conducted emissions (voltages and/or currents) or radiated
emissions (electric and/or magnetic fields). Conducted emissions are currents that are car­
ried by metallic paths (the unit’s power cord) and placed on the common power network,
where they may cause interference with other devices that are connected to the network.
Radiated emissions concern the electric fields radiated by the device that may be received
by other electronic devices causing interference in those devices. Figure 13.24 illustrates the
conceptual difference between conducted and radiated paths.
No single operating agency has jurisdiction over all systems to dictate actions necessary to
achieve EMC. Thus, EMC is usually achieved by industrial association, voluntary regulation,
government-enforced regulation, and negotiated agreements between the ­affected parties.
Frequency plays a significant role in EMC. Frequency allocations and ­assignments are made
according to the constraints established by international treaties. The Radio Regulations result­
ing from such international treaties are published by the ­International Telecommunication
Union (ITU). The Federal Communications Commission (FCC) has the authority over radio
and wire communications in the United States. The FCC has set limits on the radiated and
conducted emissions of electronic devices including calculators, televisions, printers, modems,
and personal computers. It is illegal to market an electronic device in the United States unless
its radiated and conducted emissions have been measured and do not exceed the limits of FCC
regulations. Therefore, any electronic device designed today that is designed without incorpo­
rating EMC design principles will probably fail to comply with the FCC limits.
734  CHAPTER 13  ANTENNAS
Microwave
relay link
Aircraft
Ship
Radar
Power lines
Telecommunications
Radio
Mobile TX
Handy talkie
FM/TV
broadcast
E = Emitters of interference
S = Susceptible equipment
FIGURE 13.23  Typical examples of intersystem EMI problems. Source: J. I. N. Violette et al.,
Electromagnetic Compatibility Handbook. New York: Van Nostrand Reinhold, 1987, p. 4.
TABLE 13.2  Intrasystem EMI Causes
Emitters
Susceptors
Power supplies
Relays
Radar transmitters
Radar receivers
Mobile radio transmitters
Mobile radio receivers
Fluorescent lights
Ordnance
Car ignition systems
Car radio receivers
TABLE 13.3  Intersystem EMI Causes
Emitters
Susceptors
Lightning strokes
Radio receivers
Computers
TV sets
Power lines
Heart pacers
Radar transmitters
Aircraft navigation systems
Police radio transmitters
Taxicab radio receivers
Fluorescent lights
Industrial controls
Aircraft transmitters
Ship receivers
13.10 Application Note—Electromagnetic Interference and Compatibility   735
B.  EMI Control Techniques
The three common design approaches used to control or suppress EMI are grounding,
shielding, and filtering. Although each technique has a distinct role in system design,
proper grounding may sometimes minimize the need for shielding and filtering; also
proper shielding may minimize the need for filtering. Therefore, we discuss the three
techniques, grounding, shielding, and filtering, in that order.
Grounding
Grounding is the establishment of an electrically conductive path between two points to
connect electrical and electronic elements of a system to one another or to some reference
point, which may be designated the ground. An ideal ground plane is a zero-potential, zero-
impedance body that can be used as a reference for all signals in associated circuitry and to
which any undesired current can be transferred for the elimination of its effects.
The purpose of the floating ground is to isolate circuits or equipment electrically from
a common ground plane. This type of grounding technique may cause a hazard. Single-
point grounding is used to minimize the effects of facility ground currents. Multiple-point
grounding minimizes ground lead lengths. The ground plane might be a ground wire that
is carried throughout the system or a large conductive body.
Bonding is the establishment of a low-impedance path between two metal surfaces.
Grounding is a circuit concept, while bonding denotes the physical implementation of that
concept. The purpose of a bond is to make a structure homogeneous with respect to the
flow of electrical currents, thus avoiding the development of potentials between the metal­
lic parts, since such potentials may result in EMI. Bonds provide protection from electrical
shock, power circuit current return paths, and antenna ground plane connections and also
minimize the potential difference between the devices. They have the ability to carry large
fault current.
There are two types of bonds: direct and indirect. The direct bond is a metal-to-metal
contact between the elements connected, while the indirect bond is a contact through the
use of conductive jumpers.
Radiated
interference
Transmitter
Receiver
Common ground
Common
power
source
Power cables
Conducted
interference
FIGURE 13.24  Differences
between conducted and radiated
emissions.
736  CHAPTER 13  ANTENNAS
The dc resistance Rdc of a bond is often used as an indication of bond quality. It is given by
Rdc 5 ,
sS
(13.84)
where  is the length of the bond, s is its conductivity, and S is its cross-sectional area. As
frequency increases, the bond resistance increases due to skin effect. Thus the ac resistance
Rac is given as
Rac 5
sdw
(13.85)
where w is the width of the bond and d is the skin depth.
Bonding effectiveness can be expressed as the difference (in dB) between the induced
voltages on an equipment case with and without the bond trap.
Shielding
The purpose of shielding is to confine radiated energy to a specific region or to prevent
radiated energy from entering a specific region. Shields may be in the form of partitions
and boxes as well as in the form of cable and connector shields.
Shield types include solid, nonsolid (e.g., screen), and braid, as is used on cables. In all
cases, a shield can be characterized by its shielding effectiveness. The shielding effectiveness
(SE) is defined as
SE 5 10 log10
incident power density
transmitted power density
(13.86)
where the incident power density is the power density at a measuring point before a shield is
installed and the transmitted power is the power density at the same point after the shield is in
place. In terms of the field strengths, the shielding effectiveness may also be defined as the ratio
of the field Et transmitted through to the inside to the incident field Ei. Thus, SE is given by
SE 5 20 log10 Ei
(13.87)
For magnetic fields,
SE 5 20 log10 Hi
(13.88)
a computer cabinet is much thicker than this, an aluminum case is considered a highly
­effective shield. A cabinet that effectively shields the circuits inside from external fields
is also highly effective in preventing radiation from those circuits to the external world.
Because of the effective shield, radiated emission from the computer system is caused by
openings in the cabinet such as cracks or holes from disk drives and from wires that pen­
etrate the cabinet such as power cords and cables to external devices.
For example, aluminum has s 5 3.5 3 107 S/m, e 5 eo, m 5 mo. An aluminum sheet
at 100 MHz has an SE of 100 dB at a thickness of 0.01 mm. Since an aluminum sheet for
13.11 Application Note—Textile Antennas and Sensors  737
Filtering
An electrical filter is a network of lumped or distributed constant resistors, inductors, and
capacitors that offers comparatively little opposition to certain frequencies, while blocking
the passage of other frequencies. A filter provides the means whereby levels of conducted
interference are substantially reduced.
The most significant characteristic of a filter is the insertion loss it provides as a func­
tion of frequency. Insertion loss (IL) is defined as
IL 5 20 log10 V1
(13.89)
where V1 is the output voltage of a signal source with the filter in the circuit, and V2 is the
output voltage of the signal source without the use of the filter. Low-pass filters are com­
monly used in EMC work. The insertion loss for the low-pass filters is given by
IL 5 10 log10 11 1 F22 dB
(13.90)
where
F 5 epfRC,
for a capacitive filter
pfL/R,
for an inductive filter
(13.91)
and f is the frequency.
Antennas for body-centric communication (Figure 13.25) have been introduced in recent
years. Antennas in this new class can be sewn directly onto clothes. Weaving antennas and
other electronic sensors into textiles heralds a new era for the apparel industry. The gar­
ments of the future will not only cover the human body and protect against the extremes of
nature, but also collect and transmit crucial information about the wearer’s vital signs and
current environment. These capabilities will be achieved by seamlessly tailoring biomedical
and environmental monitoring systems into fabric.
Researchers at the Ohio State University created a prototype using plastic film and
metallic thread. Some of the novel body-worn antennas and medical sensors they have
developed are based on embroidered conductive polymer fibers called e-fibers on textiles.
The flexible conductors are constructed from silver-coated p-phenylene-2,6-benzobisoxa­
zole (PBO) fibers. The e-fibers are composed of high-strength and flexible polymer cores
that incorporate conductive metallic coatings. They are readily embroidered onto regular
textiles and can also be laminated onto polymer dielectric substrates.
The e-fiber textiles exhibit an insertion loss of only 0.07 dB/cm at 1 GHz and 0.15 dB/
cm at 2 GHz. They provide inherent mechanical strength that is due to their polymer core,
together with high electrical conductivity resulting from the silver coating. These e-fibers
are twisted together to improve their conductivity. For instance, the 332-strand e-fibers
have a low resistivity of only 0.8 /m. More importantly, e-fibers are suitable for automatic
13.11  APPLICATION NOTE—TEXTILE ANTENNAS AND SENSORS
738  CHAPTER 13  ANTENNAS
embroidery onto textiles to realize various antenna and circuit designs. The embroidered
e-fiber textile electronics exhibit both mechanical and electrical advantages. Also, because
of their high conductivity, e-fibers provide much better antenna performance than other
textile antennas utilizing less conductive materials or embedded metal wires.
The e-fibers are sewn onto textiles via computerized embroidery processes to form
antennas or RF circuits. Because the fibers are so thin, they can be bundled to form much
thicker threads (664 strands per thread) for improved conductivity. During embroidery,
an “assistant” yarn is used to couch the e-fibers onto one side of the textile’s surface. This
procedure avoids abrasion damage to the silver coatings on the e-fiber’s polymer core. The
antenna and sensor designs are translated into embroidery software, followed by digitizing
stitches of the assistant yarn. As the sewing machine carries out each stitch, the e-fibers are
firmly and precisely placed onto the textile. To improve surface conductivity by minimizing
physical discontinuities and thread gaps, a second layer can be embroidered right on top of
frequency. This precaution is critical to realizing high-performance antennas and circuits.
Although primarily designed for military use, the e-fiber technology could potentially
be applied to the manufacture of gear for police officers, firefighters, and astronauts—
anybody who needs to keep the hands free for important work. The European Integrated
Project Proetex aims at developing such wearable textile systems chiefly for professional
firefighters and other first responders. A variety of sensors are being sewn inside and
tronic unit and transmitted to a base station. Suitable antennas that combine flexibility with
robustness and reliability are needed for this purpose. In other applications substrates at
least 2 mm thick are used to print the antennas. But since the clothes are usually thinner,
a flexible protective foam available in a variety of thicknesses and easily layered with gar­
ments such as firefighter suits is employed in the design. Proetex also contemplates design­
ing wearable textile systems for civilian victims of natural and other disasters.
Textile antennas find applications not only for continuous monitoring, but also for
therapeutic regimes. For instance, they can be made to produce hyperthermia for the treat­
ment of tumors and to monitor various physiological parameters. In addition to medical
applications, textile antennas serve as part of a biotelemetry system to establish wireless
communication links between implantable devices and exterior instruments.
FIGURE 13.25  Textile antenna.
outside the firefighter’s outfit, and the signals from them are processed in a wearable elec-
the first (double embroidery). It is recommended that the resultant e-fiber surface discon-
tinuities be kept to less than λ/20, where λ is the free-space wavelength of the operational
13.12 Application Note—Fractal Antennas  739
13.12  APPLICATION NOTE—FRACTAL ANTENNAS
Antennas whose shape is inherited from fractals are called fractal antennas. The
widespread use of wireless communication systems posed the necessity for the design of
sonal communication systems, satellite communication terminals, RFID, unmanned aerial
vehicles, and so on. The central idea in their design involves optimal appropriation of the
physical space either in planar or in 3-dimension. This accomplishes greater bandwidth of
operation from a low quality factor. Fractal concepts have been applied to many branches
of science and engineering, including fractal electrodynamics for radiation, propagation,
and scattering. They have been extended to antenna theory and design resulting in the
implementations of different fractal antenna elements and arrays.
There are broadly two categories of fractals: deterministic and random. Deterministic
fractals are generated from several scaled-down and rotated copies of themselves.
Examples are the von Koch snowflake and the Sierpinski gaskets. Recursive algorithms
are used to generate such fractals. Random fractals evince some degree of randomness
such as is found in natural phenomena. Fractal geometries can best be characterized and
generated using an iterative process suitable for self-similar and self-affinity structures.
Figure 13.26 illustrates this iterative process in generating few iterations of a Koch loop
and a Koch loop antenna at a chosen iteration. In a similar fashion, other shapes can be
generated. Figure 13.27 shows the stages of fractal tree dipole antenna. Figures 13.28
and 13.29 depict a fern leaf and the Sierpinski triangle, which can also be rendered as
antennas.
antennas. A small circular loop of quarter wavelength perimeter has low radiation resis­
tance, but a Koch loop occupying similar space has 35 times higher resistance. Higher
iterative geometries cause longer electrical lengths and exhibit lower resonant frequen­
cies. The meanderings of fractal contour impart distributive loading. For example, in
the Koch fractal loop inductance adds in a distributive way. The increase in inductance
Historically, antennas were called aerials; but they were so named because of their resem-
blance to insect antennae. Standard antennas come in various shapes, almost all of which
have mathematical description. Many shapes occurring in nature cannot be described in
terms of euclidean geometry. For example, a fern leaf, a thin snowflake, the shoreline, and a
statistically similar to a part thereof. These are characterized by fractal geometry. A fractal
is an iteratively generated geometry that has fractal dimensions. The underlying notions
were conceived by Benoit B. Mandelbrot. He investigated the relationship between these
iterated function systems and the nature around us using previous contributions of Gaston
Julia, Pierre Fatou, and Felix Hausdorff. He depicted many fractals existing in nature and
was able to accurately model certain phenomena. Also, he introduced new fractal mod-
els for more complex structures, including trees, clouds, and mountains, that possess an
inherent self-similarity and self-affnity by way of geometrical continuation in terms of
non-euclidean elements.
A useful feature of fractal antennas arises from their space-filling property that helps
in miniaturization while increasing the length. This permits low values of Q factors and
higher bandwidths. At resonance, the impedance is higher compared to that of traditional
class of crustaceans possess self-similarity, a property that the whole is deterministically or
wideband, or multiband, low-profile, small antennas. Their role became important in per-
740  CHAPTER 13  ANTENNAS
Koch loop antenna
FIGURE 13.26  Generating Koch loop antenna.
FIGURE 13.27  Fractal tree dipole antenna iteration after
iteration.
allows the monopole to be smaller than the corresponding linear monopole and still be
resonant. Most of the miniaturization benefits of the fractal dipoles occur within the first
five iterations, with meager marginal changes in the characteristics at greater complexi-
ties. Similar to several fractal antennas, Sierpinski gaskets possess desirable radiation

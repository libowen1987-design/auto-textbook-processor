# Sadiku《Elements of Electromagnetics》Chapter 10

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 500-549 of 926 (926 total)

---

## EM Wave Propagation

473
C H A P T E R
473
10.1  INTRODUCTION
Our first application of Maxwell’s equations will be in relation to electromagnetic wave
propagation. The existence of EM waves, predicted by Maxwell’s equations, was first inves­
tigated by Heinrich Hertz. After several calculations and experiments, Hertz succeeded in
generating and detecting radio waves, which are sometimes called Hertzian waves in his
honor.
In general, waves are means of transporting energy or information.
Typical examples of EM waves include radio waves, TV signals, radar beams, and light
rays. All forms of EM energy share three fundamental characteristics: they all travel at high
velocity; in traveling, they assume the properties of waves; and they radiate outward from a
source, without benefit of any discernible physical vehicles. The problem of radiation will
be addressed in Chapter 13.
In this chapter, our major goal is to solve Maxwell’s equations and describe EM wave
motion in the following media:
1.	 Free space 1s 5 0, e 5 eo, m 5 mo2
2.	 Lossless dielectrics 1s . 0, e 5 ereo, m 5 mrmo, or s V ve2
3.	 Lossy dielectrics 1s 2 0, e 5 ereo, m 5 mrmo2
4.	 Good conductors 1s . `, e 5 eo, m 5 mrmo, or s W ve2
where v is the angular frequency of the wave. Case 3, for lossy dielectrics, is the most
­general case and will be considered first. Once this general case has been solved, we ­simply
­derive the other cases (1, 2, and 4) from it as special cases by changing the values of s,
, and «. However, before we consider wave motion in those different media, it is appro­
priate that we study the characteristics of waves in general. This is important for proper
­understanding of EM waves. The reader who is conversant with the concept of waves may
skip Section 10.2. Power considerations, reflection, and transmission between two different
media will be discussed later in the chapter.
ELECTROMAGNETIC WAVE
PROPAGATION
Young people tell what they are doing, old people what they have done, and fools what
they wish to do.
—FRENCH PROVERB
474  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
A clear understanding of EM wave propagation depends on a grasp of what waves are in
general.
A wave is a function of both space and time.
Wave motion occurs when a disturbance at point A, at time to, is related to what happens
at point B, at time t . to. A wave equation, as exemplified by eqs. (9.51) and (9.52), is a
partial differential equation of the second order. In one dimension, a scalar wave equation
takes the form of
'2E
't2 2 u2 '2E
'z2 5 0
(10.1)
where u is the wave velocity. Equation (10.1) is a special case of eq. (9.51) in which the
medium is source free 1rv 5 0, J 5 02. It can be solved by following a procedure similar
to that in Example 6.5. Its solutions are of the form
E1 5 f (z 2 ut)
(10.2a)
E 5 g (z 1 ut)
(10.2b)
E 5 f (z 2 ut) 1 g (z 1 ut)
(10.2c)
where f and g denote any function of z 2 ut and z 1 ut, respectively. Examples of such
functions include z 6 ut, sin k1z 6 ut2, cos k1z 6 ut2, and ejk1z6ut2, where k is a constant.
It can easily be shown that these functions all satisfy eq. (10.1).
If we particularly assume harmonic (or sinusoidal) time dependence e jvt, eq. (10.1)
becomes
d2Es
dz2 1 b2Es 5 0
(10.3)
where b 5 v/u and Es is the phasor form of E. The solution to eq. (10.3) is similar to
Case 3 of Example 6.5 [see eq. (6.5.12)]. With the time factor inserted, the possible solu­
tions to eq. (10.3) are
E1 5 Aej1vt2bz2
(10.4a)
E2 5 Bej1vt1bz2
(10.4b)
where E means positive z-travel and E means negative travel. Combining E and E
leads to
E 5 Ae j 1vt2bz2 1 Be j 1vt1bz2
(10.4c)
where A and B are real constants.
†10.2 WAVES IN GENERAL
10.2 Waves in General  475
For the moment, let us consider the solution in eq. (10.4a). Taking the imaginary part
of this equation, we have
E 5 A sin1vt 2 bz2
(10.5)
This is a sine wave chosen for simplicity; a cosine wave would have resulted had we taken
the real part of eq. (10.4a). Note the following characteristics of the wave in eq. (10.5):
1.	 It is time harmonic because we assumed time dependence of the form e jvt to arrive
at eq. (10.5).
2.	 The amplitude of the wave A has the same units as E.
3.	 The phase (in radians) of the wave depends on time t and space variable z, it is the
term 1vt 2 bz2.
4.	 The angular frequency v is given in radians per second; b, the phase constant or
wave number, is given in radians per meter.
Because E varies with both time t and the space variable z, we may plot E as a func­
tion of t by keeping z constant and vice versa. The plots of E1z, t 5 constant2 and
E1t, z 5 constant2 are shown in Figure 10.1(a) and (b), respectively. From Figure 10.1(a),
we observe that the wave takes distance l to repeat itself and hence l is called the
FIGURE 10.1  Plot of E1z, t2 5 A sin 1vt 2 bz2: (a) with
­constant t, (b) with constant z.
476  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
wavelength (in meters). From Figure 10.1(b), the wave takes time T to repeat itself;
­consequently T is known as the period, in seconds. Since it takes time T for the wave to travel
distance l at the speed u, we expect
l 5 uT
(10.6a)
But T 5 1/f , where f is the frequency (the number of cycles per second) of the wave in
hertz (Hz). Hence,
u 5 f l
(10.6b)
Because of this fixed relationship between wavelength and frequency, one can identify
the position of a radio station within its band by either the frequency or the wavelength.
Usually the frequency is preferred. Also, because
v 5 2pf
(10.7a)
b 5 v
(10.7b)
and
T 5 1
f 5 2p
(10.7c)
we expect from eqs. (10.6) and (10.7) that
b 5 2p
l 5 u
(10.8)
Equation (10.8) shows that for every wavelength of distance traveled, a wave undergoes a
phase change of 2p radians.
We will now show that the wave represented by eq. (10.5) is traveling with a veloc­
ity u in the 1z-direction. To do this, we consider a fixed point P on the wave. We sketch
vt 2 bz 5 constant
dt 5 v
b 5 u
(10.9)
which is the same as eq. (10.7b). Equation (10.9) shows that the wave travels with veloc­
ity u in the 1z-direction. Similarly, it can be shown that the wave B sin 1vt 1 bz2 in
eq. (10.4b) is traveling with velocity u in the 2z-direction.
In summary, we note the following:
1.	 A wave is a function of both time and space.
2.	 Though time t 5 0 is arbitrarily selected as a reference for the wave, a wave is
without beginning or end.
eq. (10.5) at times t 5 0, T/4, and T/2 as in Figure 10.2. From the figure, it is evident that
as the wave advances with time, point P moves along the 1z­direction. Point P is a point
of constant phase, therefore
10.2 Waves in General  477
3.	 A negative sign in 1vt 6 bz2 is associated with a wave propagating in the
1z-­direction (forward-traveling or positive-going wave), whereas a positive sign
indicates that a wave is traveling in the 2z-direction (backward-traveling or
negative-going wave).
4.	 Since sin12c2 5 2sin c 5 sin1c 6 p2, whereas cos12c2 5 cos c,
sin1c 6 p/22 5 6cos c
(10.10a)
sin1c 6 p2 5 2sin c
(10.10b)
cos1c 6 p/22 5 7sin c
(10.10c)
cos1c 6 p2 5 2cos c
(10.10d)
where c 5 vt 6 bz. One of the relations in eqs. (10.10) can be used to represent
any time-harmonic wave in the form of sine or cosine.
A large number of frequencies visualized in numerical order constitute a spectrum.
Table 10.1 shows the frequencies at which various types of energy in the EM spectrum
occur. Frequencies usable for radio communication occur near the lower end of the EM
spectrum. As frequency increases, the manifestation of EM energy becomes dangerous to
human ­beings. Microwave ovens, for example, can pose a hazard if not properly shielded.
The practical difficulties of using EM energy for communication purposes also increase
as frequency increases, until finally it can no longer be used. As communication methods
­improve, the limit to usable frequency has been pushed higher. Today communication
satellites use frequencies near 14 GHz. This is still far below light frequencies, but in the
FIGURE 10.2  Plot of E1z, t2 5 A
sin1vt 2 bz2 at time (a) t 5 0,
(b) t 5 T/4, (c) t 5 T/2; P moves
in the 1z-direction with velocity u.
5. E and H are called uniform waves if they lie in a plane and are constant over such planes.
enclosed environment of fiber optics, light itself can be used for radio communication.
478  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
An electric field in free space is given by
E 5 50 cos1108t 1 bx2ay V/m
(a)	 Find the direction of wave propagation.
(b)	 Calculate b and the time it takes to travel a distance of l/2.
(c)	 Sketch the wave at t 5 0, T/4, and T/2.
Solution:
(a)  From the positive sign in 1vt 1 bx2, we infer that the wave is propagating along 2ax.
This will be confirmed in part (c) of this example.
(b)	 In free space, u 5 c:
b 5 v
c 5
108
3 3 108 5 1
b 5 0.3333 rad/m
If T is the period of the wave, it takes T seconds to travel a distance l at speed c. Hence to
travel a distance of l/2 will take
t1 5 T
2 5 1
2 2p
v 5 p
108 5 31.42 ns
Alternatively, because the wave is traveling at the speed of light c,
2 5 ct1  or  t1 5 l
But
l 5 2p
b 5 6p
TABLE 10.1  Electromagnetic Spectrum
EM Phenomena
Examples of Uses
Approximate Frequency Range
Cosmic rays
Physics, astronomy
1014 GHz and above
Gamma rays
Cancer therapy
1010–1013 GHz
X-rays
X-ray examination
108–109 GHz
Ultraviolet radiation
Sterilization
106–108 GHz
Visible light
Human vision
105–106 GHz
Infrared radiation
Photography
103–104 GHz
Microwave waves
Radar, microwave relays,
satellite communication
3–300 GHz
Radio waves
UHF television
470–806 MHz
VHF television, FM radio
54–216 MHz
Short-wave radio
3–26 MHz
AM radio
535–1605 kHz
EXAMPLE 10.1
10.2 Waves in General  479
Hence,
t1 5
213 3 1082 5 31.42 ns
as obtained before.
(c)	 At
t 5 0,
Ey 5 50 cos bx
t 5 T/4, Ey 5 50 cosav # 2p
4v 1 bxb 5 50 cos1bx 1 p/22
5 250 sin bx
t 5 T/2, Ey 5 50 cosav # 2p
2v 1 bxb 5 50 cos1bx 1 p2
5 250 cos bx
Ey at t 5 0, T/4, T/2 is plotted against x as shown in Figure 10.3. Notice that a point P
­(arbitrarily selected) on the wave moves along 2ax as t increases with time. This shows that
the wave travels along 2ax.
FIGURE 10.3  For Example 10.1;
wave travels along ax.
480  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
PRACTICE EXERCISE  10.1
In free space, H 5 0.1 cos12 3 108t 2 kx2ay A/m.
(a)  Calculate k, l, and T.
(b)  Calculate the time t1 it takes the wave to travel l/8.
(c)  Sketch the wave at time t1.
Answer:  (a) 0.667 rad/m, 9.425 m, 31.42 ns, (b) 3.927 ns, (c) see Figure 10.4.
10.3  WAVE PROPAGATION IN LOSSY DIELECTRICS
As mentioned in Section 10.1, wave propagation in lossy dielectrics is a general case from
which wave propagation in media of other types can be derived as special cases. Therefore,
this section is foundational to the next three setions.
A lossy dielectric is a medium in which an EM wave, as it propagates, loses power
owing to imperfect dielectric.
In other words, a lossy dielectric is a partially conducting medium (imperfect dielectric
or imperfect conductor) with s 2 0, as distinct from a lossless dielectric (perfect or good
­dielectric) in which s 5 0.
Consider a linear, isotropic, homogeneous, lossy dielectric medium that is charge free
1macroscopic rv 5 02. Assuming and suppressing the time factor e jvt, Maxwell’s equations
(see Table 9.2) become
= # Es 5 0
(10.11)
= # Hs 5 0
(10.12)
= 3 Es 5 2jvmHs
(10.13)
= 3 Hs 5 1s 1 jve2Es
(10.14)
FIGURE 10.4  For Practice Exercise
10.1(c).
10.3 Wave Propagation in Lossy Dielectrics  481
Taking the curl of both sides of eq. (10.13) gives
= 3 = 3 Es 5 2jvm1= 3 Hs2
(10.15)
Applying the vector identity
= 3 1= 3 A2 5 =1= # A2 2 =2A
(10.16)
to the left-hand side of eq. (10.15) and invoking eqs. (10.11) and (10.14), we obtain
=1= # Es2 2 =2Es 5 2jvm1s 1 jve2Es
=2Es 2 g2Es 5 0
(10.17)
where
g2 5 jvm1s 1 jve2
(10.18)
and g, in reciprocal meters, is called the propagation constant of the medium. By a similar
procedure, it can be shown that for the H field,
=2Hs 2 g2Hs 5 0
(10.19)
Equations (10.17) and (10.19) are known as homogeneous vector Helmholtz’s equations or
simply vector wave equations. In Cartesian coordinates, eq. (10.17), for example, is equiva­
lent to three scalar wave equations, one for each component of E along ax, ay, and az.
Since g in eqs. (10.17) to (10.19) is a complex quantity, we may let
g 5 a 1 jb
(10.20)
We obtain a and b from eqs. (10.18) and (10.20) by noting that
2Re g2 5 b2 2 a2 5 v2me
(10.21)
and
0 g2 0 5 b2 1 a2 5 vm "s2 1 v2e2
(10.22)
From eqs. (10.21) and (10.22), we obtain
⎯⎯→
a 5 vÇ
2  cÅ1 1 c s
ved
2 1d
b 5 vÇ
2  cÅ1 1 c s
ved
1 1d
(10.23)
(10.24)
482  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
only an x-component, then
Es 5 Exs1z2ax
(10.25)
We then substitute into eq. (10.17), which yields
1=2 2 g22Exs1z2 5 0
(10.26)
Without loss of generality, if we assume that a wave propagates in an unbounded
medium along az and that E has only an x-component that does not vary with x and y, then
'2Exs1z2
'x2
1 '2Exs1z2
'y2
1 '2Exs1z2
'z2
2 g2Exs1z2 5 0
c d2
dz2 2 g2d Exs1z2 5 0
(10.27)
This is a scalar wave equation, a linear homogeneous differential equation, with solution
(see eq. 6.5.13a in Case 3 of Example 6.5),
Exs1z2 5 Eoe2gz 1 Eroegz
(10.28)
where Eo and Ero are constants. The fact that the field must be finite at infinity requires that
Ero 5 0. Alternatively, because egz denotes a wave traveling along 2az, whereas we assume
wave propagation along az, Ero 5 0. Whichever way we look at it, Ero 5 0. Inserting the time
factor e jvt into eq. (10.28) and using eq. (10.20), we obtain
Ez, t2 5 Re3Exsz2e jvtax4 5 ReEoe2azejvt2bz2ax2
E1z, t2 5 Eoe2azcos1vt 2 bz2ax
(10.29)
A sketch of |E 0  at times t 5 0 and t 5 Dt is portrayed in Figure 10.5, where it is evident that
E has only an x-component and it is traveling in the 1z-direction. Having obtained E1z, t2,
we obtain H1z, t2 either by taking similar steps to solve eq. (10.19) or by using eq. (10.29) in
conjunction with Maxwell’s equations, as we did in Example 9.8. We will eventually arrive at
H1z, t2 5 Re1Hoe2azej1vt2bz2 ay2
(10.30)
where
Ho 5 Eo
h 
(10.31)
and h is a complex quantity known as the intrinsic impedance, in ohms, of the medium. It
can be shown by following the steps taken in Example 9.8 that
⎯⎯→
⎯⎯→
Without loss of generality, if we assume that a wave propagates along 1az and that Es has
10.3 Wave Propagation in Lossy Dielectrics  483
with
0 h 0 5
"m/e
c1 1 a s
veb
1/4,  tan 2uh 5 s
ve
(10.33)
H 5 Re c
0 h 0 e juh e2aze j 1vt2bz2 ayd
H 5 Eo
0 h 0  e2az cos1vt 2 bz 2 uh2 ay
(10.34)
Notice from eqs. (10.29) and (10.34) that as the wave propagates along az, it decreases or
attenuates in amplitude by a factor e2az, and hence a is known as the attenuation constant,
or attenuation coefficient, of the medium. It is a measure of the spatial rate of decay of
decibels per meter (dB/m). An attenuation of 1 neper denotes a reduction to e21 of the
original value, whereas an increase of 1 neper indicates an increase by a factor of e. Hence,
for voltages
1 Np 5 20 log10 e 5 8.686 dB
(10.35)
From eq. (10.23), we notice that if s 5 0, as is the case for a lossless medium and free
space, a 5 0 and the wave is not attenuated as it propagates. The quantity b is a measure
of the phase shift per unit length in radians per meter and is called the phase constant or
FIGURE 10.5  An E-field with
an x-component traveling in the
1z-direction at times t 5 0 and
t 5 Dt; arrows indicate instanta-
neous values of E.
h 5 Å
jvm
s 1 jve 5 0 h 0 luh 5 0 h 0 e juh
(10.32)
where 0 # uh # 45º. Substituting eqs. (10.31) and (10.32) into eq. (10.30) gives
the wave in the medium, measured in nepers per meter (Np/m), and can be expressed in
484  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
wave number. In terms of b, the wave velocity u and wavelength l are, respectively, given
by [see eqs. (10.7b) and (10.8)]
u 5 v
b,  l 5 2p
b 
(10.36)
We also notice from eqs. (10.29) and (10.34) that E and H are out of phase by uh at any
instant of time due to the complex intrinsic impedance of the medium. Thus at any time,
E leads H(or H lags E) by uh. Finally, we notice that the ratio of the magnitude of the con­
duction current density Jc to that of the displacement current density Jd in a lossy medium is
0 Jcs 0
0 Jds 0 5
0 sEs 0
0 jveEs 0 5 s
ve 5 tan u
tan u 5 s
ve
(10.37)
where tan u is known as the loss tangent and u is the loss angle of the medium as illustrated
in Figure 10.6. Although a line of demarcation between good conductors and lossy dielec­
trics is not easy to make, tan u or u may be used to determine how lossy a medium is. A
medium is said to be a good (lossless or perfect) dielectric if tan u is very small 1s V ve2
or a good conductor if tan u is very large 1s W ve2. From the viewpoint of wave propaga­
tion, the characteristic behavior of a medium depends not only on its constitutive param­
eters s, «, and m but also on the frequency of operation. A medium that is ­regarded as a
good conductor at low frequencies may be a good dielectric at high frequencies. Note from
eqs. (10.33) and (10.37) that
u 5 2uh
(10.38)
From eq. (10.14)
= 3 Hs 5 1s 1 jve2Es 5 jve c1 2
ved Es
5 jvecEs
(10.39)
FIGURE 10.6  Loss angle of a lossy medium.
10.3 Wave Propagation in Lossy Dielectrics  485
where
ec 5 e c1 2 j s
ved 5 e312j tan u4
(10.40a)
ec 5 er 2 jes
(10.40b)
with er 5 e, es 5 s/v, e 5 eoer; «c is called the complex permittivity of the medium. We
tan u 5 es
er 5 s
ve
(10.41)
In subsequent sections, we will consider wave propagation in media of other types
that may be regarded as special cases of what we have considered here. Thus we will simply
­deduce the governing formulas from those obtained  for the general case treated in this
section. The student is advised not just to memorize the formulas but to observe how they
are easily obtained from the formulas for the general case.
A lossy dielectric has an intrinsic impedance of 200 li
30° V at a particular radian frequency
v. If, at that frequency, the plane wave propagating through the dielectric has the magnetic
field component
H 5 10 e2ax cosavt 2 1
2 xbay A/m
find E and a.
Solution:
The given wave travels along ax so that ak 5 ax; aH 5 ay, so
2aE 5 ak 3 aH 5 ax 3 ay 5 az
aE 5 2az
Also Ho 5 10, so
5 h 5 200 li
30° 5 200 e jp/6 S  Eo 5 2000e jp/6
Except for the amplitude and phase difference, E and H always have the same form. Hence
E 5 Re12000e jp/6e2gxejvtaE2
EXAMPLE 10.2
observe that the ratio of « to « is the loss tangent of the medium; that is,
486  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
E 5 22e2ax cosavt 2 x
2 1 p
6 baz kV/m
But s
ve 5 tan 2uh 5 tan 60° 5 "3. Hence,
b 5 c 2 2 1
2 1 1 d
1/2
a 5
2"3
5 0.2887 Np/m
PRACTICE EXERCISE  10.2
A plane wave propagating through a medium with er 5 8, mr 5 2 has E 5 0.5
e2z/3 sin1108t 2 bz2ax V/m. Determine
(a)   b
(d)  Wave velocity
(b)  The loss tangent
(e)  H field
(c)  Intrinsic impedance
Answer:  (a) 1.374 rad/m,  (b) 0.5154,  (c) 177.72 liii
13.63° V, (d) 7.278 3 107 m/s,
(e) 2.817e2z/3 sin(108 t 2 bz 2 13.63°2ay mA/m.
Knowing that b 5 1/2, we need to determine 	. Since
a 5 vÇ
2  cÅ1 1 c s
ved
2 1d
and
b 5 vÇ
2  cÅ1 1 c s
ved
1 1d
b 5 ≥Å1 1 c s
ved
2 1
Å1 1 c s
ved
1 1
1/2
10.5 Plane Waves in Free Space  487
10.4  PLANE WAVES IN LOSSLESS DIELECTRICS
In a lossless dielectric, s V ve. It is a special case of that in Section 10.3 except that
s . 0,  e 5 eoer,  m 5 momr
(10.42)
Substituting these into eqs. (10.23) and (10.24) gives
a 5 0,  b 5 v"me
(10.43a)
u 5 v
b 5
"me
,  l 5 2p
b 
(10.43b)
Also
h 5 Å
e l0°
(10.44)
and thus E and H are in time phase with each other.
10.5  PLANE WAVES IN FREE SPACE
Plane waves in free space comprise a special case of what we considered in Section 10.3.
In this case,
s 5 0,  e 5 eo,  m 5 mo
(10.45)
a 5 0, b 5 v"moeo 5 v
c 
(10.46a)
u 5
"moeo
5 c, l 5 2p
b 
(10.46b)
where c . 3 3 108 m/s, the speed of light in a vacuum. The fact that EM waves
travel in free space at the speed of light is significant. It provides some evidence that
light is the manifestation of an EM wave. In other words, light is characteristically
electromagnetic.
This may also be regarded as a special case of Section 10.4. Thus we simply replace « by «o
and  by o in eq. (10.43), or we substitute eq. (10.45) directly into eqs. (10.23) and (10.24).
Either way, we obtain
488  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
By substituting the constitutive parameters in eq. (10.45) into eq. (10.33), uh 5 0 and
h 5 ho, where ho is called the intrinsic impedance of free space and is given by
E 5 Eo cos1vt 2 bz2 ax
(10.48a)
then
H 5 Ho cos1vt 2 bz2ay 5 Eo
cos1vt 2 bz2ay
(10.48b)
The plots of E and H are shown in Figure 10.7(a). In general, if aE, aH, and ak are unit
­vectors along the E field, the H field, and the direction of wave propagation; it can be shown
that (see Proble
ak 3 aE 5 aH
ak 3 aH 5 2aE
aE 3 aH 5 ak
(10.49)
Both E and H fields (or EM waves) are everywhere normal to the direction of wave propa­
gation, ak. That means that the fields lie in a plane that is transverse or orthogonal to the
FIGURE 10.7  Plots of E and H (a) as functions of z at t 5 0; and (b) at z 5 0. The arrows
­indicate instantaneous values.
ho 5 Å
5 120p . 377 V
(10.47)
m 10.69).
10.6 Plane Waves in Good Conductors  489
direction of wave propagation. They form an EM wave that has no electric or magnetic
field components along the direction of propagation; such a wave is called a transverse
electromagnetic (TEM) wave. A combination of E and H is called a uniform plane wave
because E (or H) has the same magnitude throughout any transverse plane, defined by
z 5 constant. The direction in which the electric field points is the polarization of a TEM
wave.1 The wave in eq. (10.29), for example, is polarized in the x-direction. This should
be observed in Figure 10.7(b), which illustrates uniform plane waves. A uniform plane
wave cannot exist physically because it stretches to infinity and would represent an infinite
energy. Such waves are characteristically simple and fundamentally important. They serve
as approximations to practical waves such as those from a radio antenna at distances suf­
ficiently far from radiating sources. Although our discussion after eq. (10.48) deals with
free space, it also applies for any other isotropic medium.
10.6  PLANE WAVES IN GOOD CONDUCTORS
s . `,  e 5 eo,  m 5 momr
(10.50)
Also, from eq. (10.32),
h 5 Å
jvm
5 Å
s  l45°
(10.52)
and thus E leads H by 45°. If
E 5 Eoe2azcos1vt 2 bz2ax
(10.53a)
then
H 5
e2az cos1vt 2 bz 2 45°2ay
(10.53b)
1 Polarization will be covered in Section 10.7.
Hence, eqs. (10.23) and (10.24) become
a 5 b 5 Å
vms
5 "pfms
(10.51a)
u 5 v
b 5 Å
ms,  l 5 2p
(10.51b)
Plane waves in good conductors comprise another special case of that considered in
Section 10.3. A perfect, or good conductor, is one in which s W ve, so that s
ve, W 1; that is,
490  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
Therefore, as the E (or H) wave travels in a conducting medium, its amplitude is attenuated
by the factor e2az. The distance d, shown in Figure 10.8, through which the wave amplitude
decreases to a factor e21 (about 37% of the original value) is called skin depth or penetration
depth of the medium; that is,
Eoe2ad 5 Eoe21
d 5 1
(10.54a)
The skin depth is a measure of the depth to which an EM wave can penetrate the
medium.
Equation (10.54a) is generally valid for any material medium. For good conductors,
eqs. (10.51a) and (10.54a) give
The illustration in Figure 10.8 for a good conductor is exaggerated. However, for a partially
conducting medium, the skin depth can be quite large. Note from eqs. (10.51a), (10.52),
and (10.54b) that for a good conductor,
Noting that for good conductors we have a 5 b 5 1
d, eq. (10.53a) can be written as
E 5 Eoe2z/d cosavt 2 z
dbax
showing that d measures the exponential damping of the wave as it travels through the
conductor. The skin depth in copper at various frequencies is shown in Table 10.2. From
Table 10.2, we notice that the skin depth decreases with increasing frequency. Thus, E and
H can hardly propagate through good conductors.
The phenomenon whereby field intensity in a conductor rapidly decreases is known
as the skin effect. It is a tendency of charges to migrate from the bulk of the conducting
material to the surface, resulting in higher resistance. The fields and associated currents are
confined to a very thin layer (the skin) of the conductor surface. For a wire of radius a, for
example, it is a good approximation at high frequencies to assume that all of the current
d 5
!pfms 5 1
(10.54b)
h 5 1
sd "2 ejp/4 5
1 1 j
(10.55)
10.6 Plane Waves in Good Conductors  491
flows in the circular ring of thickness d as shown in Figure 10.9. The skin effect appears in
different guises in such problems as attenuation in waveguides, effective or ac resistance of
transmission lines, and electromagnetic shielding. It is used to advantage in many applica­
tions. For example, because the skin depth in silver is very small, the difference in perfor­
mance between a pure silver component and a silver-plated brass component is negligible,
so silver plating is often used to reduce the material cost of waveguide components. For
the same reason, hollow tubular conductors are used instead of solid conductors in out­
door television antennas. Effective electromagnetic shielding of electrical devices can be
provided by conductive enclosures a few skin depths in thickness.
The skin depth is useful in calculating the ac resistance due to skin effect. The resis­
tance in eq. (5.16) is called the dc resistance, that is,
Rdc 5 ,
sS
We define the surface or skin resistance Rs (in V) as the real part of h for a good conductor.
Thus from eq. (10.55)
This is the resistance of a unit width and unit length of the conductor. It is equivalent to
the dc resistance for a unit length of the conductor having cross-sectional area 1 3 d. Thus
FIGURE 10.8  Illustration of skin depth.
TABLE 10.2  Skin Depth in Copper*
Frequency (Hz)
100
500
104
108
1010
Skin depth (mm)
20.8
8.6
6.6
2.99
0.66
6.6 3 1023
6.6 3 1024
Rs 5 1
sd 5 Å
pfm
(10.56)
*For copper, s 5 5.8 3 107 S/m, m 5 mo, d 5 66.1/!f  (in mm).
492  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
for a given width w and length , the ac resistance is calculated by using the familiar dc
­resistance relation of eq. (5.16) and assuming a uniform current flow in the conductor of
thickness d; that is,
Rac 5
sdw 5 Rs,
w 
(10.57)
where S . dw. For a conductor wire of radius a (see Figure 10.9), w 5 2pa, so
Rac
Rdc
s2pad
spa2
5 a
2d 5 a
2 !pfms
Since d V a at high frequencies, this shows that Rac is far greater than Rdc. In general, the
ratio of the ac to the dc resistance starts at 1.0 for dc and very low frequencies and increases
as the frequency increases. Also, although the bulk of the current is nonuniformly distrib­
uted over a thickness of 5d of the conductor, the power loss is the same as though it were
uniformly distributed over a thickness of d and zero elsewhere. This is one more reason
that d is referred to as the skin depth. For easy reference, the formulas for propagation
constants for different media are summarized in Table 10.3.
FIGURE 10.9  Skin depth at high frequencies, d V a.
TABLE 10.3  Formulas, for a, b, h, n, and l
Lossy Medium
Lossless Medium
Free Space
Conductor
a 5
2 DÑ1 1 a s
veb
2 1T T
1/2
"pfms
b 5
2 DÑ1 1 a s
veb
1 1T T
1/2
v"me
v"moeo
"pfms
h 5
jvm
s 1 jve
. 377
(1 1 j)a
n 5 v
b,       l 5 2p
10.6 Plane Waves in Good Conductors  493
In a lossless dielectric for which h 5 60p, mr 5 1, and H 5 20.1 cos1vt 2 z2ax 1
0.5 sin1vt 2 z2ay A/m, calculate «r, v, and E.
Solution:
From the given H field, E can be calculated in two ways: by using the techniques (based
on Maxwell’s equations) developed in this chapter or directly, by using Maxwell’s equations
as in Chapter 9.
Method 1:  To use the techniques developed in the present chapter, we let
H 5 H1 1 H2
where H1 5 20.1 cos1vt 2 z2ax and H2 5 0.5 sin1vt 2 z2ay and the corresponding
electric field
E 5 E1 1 E2
where E1 5 E1o cos1vt 2 z2aE1 and E2 5 E2o sin1vt 2 z2aE2. Notice that although H has
components along ax and ay, it has no component along the direction of propagation; it is
therefore a TEM wave.
For E1,
aE1 5 21ak 3 aH12 5 21az 3 2ax2 5 ay
E1o 5 hH1o 5 60p 10.12 5 6p
Hence
E1 5 6p cos1vt 2 z2ay
EXAMPLE 10.3
In this case, s 5 0, a 5 0, and b 5 1, so
h 5 "m/e 5 Å
5 120p
"er
"er 5 120p
5 120p
60p 5 2  S   er 5 4
b 5 v"me 5 v"moeo "mrer 5 v
c  "4 5 2v
v 5 bc
2 5 1 13 3 1082
5 1.5 3 108 rad/s
494  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
For E2,
aE2 5 21ak 3 aH22 5 21az 3 ay2 5 ax
E2o 5 hH2o 5 60p10.52 5 30p
Hence
E2 5 30p sin1vt 2 z2ax
Adding E1 and E2 gives E; that is,
E 5 94.25 sin11.5 3 108t 2 z2ax 1 18.85 cos11.5 3 108t 2 z2ay V/m
Method 2:  We may apply Maxwell’s equations directly
= 3 H 5 sE 1 e 'E
't  S   E 5 1
e 3= 3 H dt
because s 5 0. But
where H1o 5 20.1 and H2o 5 0.5. Hence
E 5 1
e 3= 3 H dt 5 H2o
ev  sin1vt 2 z2ax 2 H1o
ev  cos1vt 2 z2ay
5 94.25 sin1vt 2 z2ax 1 18.85 cos1vt 2 z2ay V/m
as expected.
⎯⎯→
PRACTICE EXERCISE  10.3
A plane wave in a nonmagnetic medium has E 5 50 sin1108t 1 2z2ay V/m. Find
(a)  The direction of wave propagation
(b)  l, f, and er
(c)  H
Answer:  (a) in the 2z-direction,  (b) 3.142 m, 15.92 MHz, 36,  (c) 0.7958
sin1108t 1 2z2ax A/m.
= 3 H 5 ∞
Hx1z2
Hy1z2
∞5 2
'Hy
'z ax 1 'Hx
'z ay
5 H2o cos1vt 2 z2ax 1 H1o sin1vt 2 z2ay
10.6 Plane Waves in Good Conductors  495
A uniform plane wave propagating in a medium has
E 5 2e2az sin1108t 2 bz2ay V/m
If the medium is characterized by er 5 1, mr 5 20, and s 5 3 S/m, find a, b, and H.
Solution:
We need to determine the loss tangent to be able to tell whether the medium is a lossy
­dielectric or a good conductor.
ve 5
108 3 1 3 1029
36p
5 3393 W 1
EXAMPLE 10.4
showing that the medium may be regarded as a good conductor at the frequency of opera-
tion. Hence,
a 5 b 5 Å
mvs
5 c 4p 3 1027 3 2011082 132
1/2
5 61.4
a 5 61.4 Np/m,  b 5 61.4 rad/m
Also
0 h 0 5 Å
s 5 c 4p 3 1027 3 2011082
1/2
5 Å
800p
tan 2uh 5 s
ve 5 3393  S   uh 5 45º 5 p
Hence
H 5 Hoe2az sinavt 2 bz 2 p
4 baH
where
aH 5 ak 3 aE 5 az 3 ay 5 2ax
and
Ho 5 Eo
0 h 0 5 2 Å
800p 5 69.1 3 1023
Thus
H 5 269.1 e261.4z sina108t 2 61.42z 2 p
4 bax mA/m
496  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
A plane wave E 5 Eo cos1vt 2 bz2ax is incident on a good conductor at z $ 0. Find the
current density in the conductor.
Solution:
Since the current density J 5 sE, we expect J to satisfy the wave equation in eq. (10.17);
that is, we expect to find
=2Js 2 g2Js 5 0
Also the incident E has only an x-component and varies with z. Hence J 5 Jx1z, t2ax and
dz2Jsx 2 g2Jsx 5 0
which is an ordinary differential equation with solution (see Case 2 of Example 6.5)
Jsx 5 Ae2gz 1 Be1gz
The constant B must be zero because Jsx is finite as z S  `. But in a good conductor,
g 5 a 1 jb 5 a11 1 j2 5
11 1 j2
and
Jsx 5 Ae2z111j2/d
Jsx 5 Jsx102 e2z111j2/d
where Jsx (0) is the current density on the conductor surface.
PRACTICE EXERCISE  10.4
A plane wave traveling in the 1y-direction in a lossy medium 1er 5 4, mr 5 1,
s 5 1022 S/m2 has E 5 30 cos1109p t 1 p/42az V/m at y 5 0. Find
(a)  E at y 5 1 m, t 5 2 ns
(b)  The distance traveled by the wave to have a phase shift of 10
(c)  The distance traveled by the wave to have its amplitude reduced by 40%
(d)  H at y 5 2 m, t 5 2 ns
Answer:  (a) 2.844az V/m,  (b) 8.349 mm,  (c) 542 mm,  (d) 222.6ax mA/m.
EXAMPLE 10.5
s W ve, so that a 5 b 5 1/d. Hence
10.6 Plane Waves in Good Conductors  497
For the copper coaxial cable of Figure 7.12, let a 5 2 mm, b 5 6 mm, and t 5 1 mm.
Calculate the resistance of a 2 m length of the cable at dc and at 100 MHz.
Solution:
Let
R 5 Ro 1 Ri
where Ro and Ri are the resistances of the inner and outer conductors.
At dc,
Ri 5 ,
sS 5
spa2 5
5.8 3 107p32 3 102342 5 2.744 mV
Ro 5 ,
sS 5
sp3 3b 1 t42 2 b24 5
sp3t2 1 2bt4
5.8 3 107p 31 1 124 3 1026
EXAMPLE 10.6
PRACTICE EXERCISE  10.5
Given the current density of Example 10.5, find the magnitude of the total current
through a strip of the conductor of infinite depth along z and width w along y.
Answer:  Jsx102wd
5 0.8429 mV
Hence Rdc 5 2.744 1 0.8429 5 3.587 mV.
At f 5 100 MHz,
Ri 5 Rs,
w 5
sd2pa 5
2pa Å
pfm
2p 3 2 3 1023 Å
p 3 108 3 4p 3 1027
5.8 3 107
5 0.41 V
Since d 5 6.6 mm V t 5 1 mm, w 5 2pb for the outer conductor. Hence,
Ro 5 Rs,
w 5
2pb Å
pfm
2p 3 6 3 1023 Å
p 3 108 3 4p 3 1027
5.8 3 107
5 0.1384 V
498  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
Hence,
Rac 5 0.41 1 0.1384 5 0.5484 V
which is about 150 times greater than Rdc. Thus, for the same effective current i, the ohmic
loss (i2R) of the cable at 100 MHz is greater than the dc power loss by a factor of 150.
PRACTICE EXERCISE  10.6
For an aluminum wire having a diameter 2.6 mm, calculate the ratio of ac to dc
­resistance at
(a)  10 MHz
(b)  2 GHz
Answer:  (a) 24.16,  (b) 341.7.
10.7  WAVE POLARIZATION
It is a common practice to describe an EM wave by its polarization. Polarization is an
important property of an EM wave, and the concept has been developed to describe the
various types of electric field variation and orientation. The polarization of an EM wave
depends on the transmitting antenna or source. It is determined by the direction of the
electric field for fields having more than one component.
Polarization may be regarded as the locus of the tip of the electric field (in a plane
perpendicular to the direction of propagation) at a given point as a function of time.
There are three types of polarization: linear or plane, circular, and elliptical. That means
that the tip of the electric field can describe a straight line, a circle, or an ellipse with
time, as shown in Figure 10.10. Wave polarization is important for radio and TV broad­
casting. Amplitude modulation (AM) radio broadcasting is with polarization vertical to
the earth’s surface, while frequency modulation (FM) broadcasting is generally circularly
polarized.
A uniform plane wave is linearly polarized if it has only one component or when
its  transverse components are in phase. For a wave traveling in the +z-direction, we
may have
Ex 5 Eox cos(t 2 bz 1 x )
(10.58)
Ey 5 Eoy cos(t 2 bz 1 y )
where Eox and Eoy are real. The composite wave
10.7 Wave Polarization  499
E 5 Eox cos(t 2 bz 1 x )ax 1 Eoy cos(t 2 bz 1 y )ay
(10.59)
is linearly polarized when the phase difference Df is
Df 5 fy 2 fx 5 np,    n 5 0, 1, 2, . . .
(10.60)
Df 5 fy 2 fx 5  (2n 1 1)p/2 ,    n 5 0, 1, 2, . . . 
(10.61)
FIGURE 10.10  Wave polarizations: (a) linear, (b) circular, (c) elliptical.
(a)
(b)
(c)
This allows the two components to maintain the same ratio at all times. If we observe the
wave in the direction of propagation (z in this case), we will notice that the tip of the elec­
can be generated by simple antennas (such as dipole antennas) or lasers.
Circular polarization takes place when the x­ and y­components are the same in
magnitude (Eox 5 Eoy 5 Eo) and the phase difference between them is an odd multiple of
p/2; that is,
tric field follows a line—hence, the term linear polarization. Linearly polarized plane waves
500  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
For example, the x- and y-components may be of the form
Ex 5 Eo cos(t 2 bz)
(10.62)
Ey 5 Eo cos(t 2 bz 1 /2)
The tip of the composite electric field as observed as a fixed point in the xy-plane moves
along a circle as time progresses. Circularly polarized waves can be generated by a helically
wound wire antenna or by two linear sources that are oriented perpendicular to each other
and fed with currents that are out of phase by 90. That the locus of total field traces a circle
can be seen if we examine the components at a point, say z 5 0,
Ex 5 Eo cos(t),     Ey 5 Eo cos(t 1 /2) 5 2Eo sin(t)
(10.63)
E2 5 E2
x 1 E2
5 E2
o 
(10.64)
which is the equation of a circle.
Linear and circular polarizations are special cases of the more general case of the ellip­
tical polarization. An elliptically polarized wave is one in which the tip of the field traces an
elliptic locus in a fixed transverse plane as the field changes with time. Elliptical polariza­
tion is achieved when the x- and y-components are not equal in magnitude Eox  Eoy and
the phase difference between them is an odd multiple of p
hat is,
Df 5 fy 2 fx 5  (2n 1 1)p/2,    n 5 0, 1, 2, . . . 
(10.65)
This allows the tip of the electric field to trace an ellipse in the xy-plane. To show that this
is the case, consider eq. (10.58) when z 5 0 and Df 5 fy 2 fx 5 p/2,
Ex 5 Eoz cos(t)  ⎯→  cos(t) 5 Ex
Eox
(10.66)
Ey 5 Eoy cos(t 1 /2) 5 2Eo sin(t)  ⎯→
2sin(t) 5
Eoy
Squaring and adding these equations yields
cos2 (t) 1 sin2 (t) 5 1  ⎯→  Ex
Eox
2 1
Eoy
2  5 1
(10.67)
which is the equation of an ellipse, as shown in Figure 10.10. Notice that if Eox 5 Eoy , we
have circular polarization. Thus, circular polarization is a special case of elliptical polariza­
tion. In fact, we can show that linear polarization is also a special case of elliptical polariza­
tion. Thus, the most general case is elliptical polarization.
Determine the polarization of a plane wave with:
(a)  E(z, t) 5 4e20.25z cos(t 2 0.8z)ax 1 3e20.25z sin(t 2 0.8z)ay V/m
(b)  Hs(z) 5 Ho e2jbz ax 2 2Ho e2jbz
Solution:
(a)  From the given E,
Ex5 4e20.25z cos(t 2 0.8z)
EXAMPLE 10.7
/2; t
10.7 Wave Polarization  501
Ey5 3e20.25z sin(t 2 0.8z)
In the z 5 0 plane, we have
4 Ex(0, t) 5 cos(t)
3 Ex(0, t) 5 sin(t)
Squaring and adding gives
16Ex
10,  t2 1 1
9Ey
10, t2 5 1
which describes an ellipse. Hence, the wave is elliptically polarized.
(b)  The two components of H are in phase; hence, the polarization is linear. For proper
characterization, it is expedient to find the electric field component. This can be done
in many ways. Using Maxwell’s equation,
 3 Hs 5 ∞
Hoe2jbz
22Hoe2jbz
∞ 5 j2bHoe2jbz ax 2 jbHoe2jbz ay
Dividing both sides by j« and setting h = b/« yields
Es 5 2Hoe2jbz ax 2 Hoe2jbz ay
In the time domain,
E(z, t)5 Re[Ese2jt] 5 2Hocos(t 2 bz)ax 2 Hocos(t 2 bz)ay
If we set z 5 0,
E(0, t) 5 (2Hoax 2 Hoay) cos(t)
At t 5 0, E has components 2hHo in the x-direction and hHo in the y-direction. The ratio
Ey/Ex remains the same as t changes. Hence, E is linearly polarized.
PRACTICE EXERCISE  10.7
Given that Es5 Eo (ay 2 jay)e2jbz, determine the polarization.
Answer:  Circular polarization.
  Hs  jEs ⎯⎯⎯→ Es 5
jve   Hs
502  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
10.8  POWER AND THE POYNTING VECTOR
As mentioned before, energy can be transported from one point (where a transmitter is
located) to another point (with a receiver) by means of EM waves. The rate of such energy
transportation can be obtained from Maxwell’s equations:
= 3 E 5 2m'H
't 
(10.68a)
= 3 H 5 sE 1 e'E
't 
(10.68b)
Dotting both sides of eq. (10.68b) with E gives
E # 1= 3 H2 5 sE2 1 E # e'E
et 
(10.69)
But for any vector fields A and B (see Appendix A.10)
= # 1A 3 B2 5 B # 1= 3 A2 2 A # 1= 3 B2
Applying this vector identity to eq. (10.69) 1letting A 5 H and B 5 E2 gives
H # 1= 3 E2 1 = # 1H 3 E2 5 sE2 1 E # e 'E
't 
(10.70)
5 sE2 1 1
2 e '
'tE2
Dotting both sides of eq. (10.68a) with H, we write
H # 1= 3 E2 5 H # a2m'H
't b 5 2m
2 '
't 1H # H2
(10.71)
and thus eq. (10.70) becomes
2 'H2
't 2 = # 1E 3 H2 5 sE2 1 1
2 e'E2
Rearranging terms and taking the volume integral of both sides,
= # 1E 3 H2dv 5 2 '
't 3
c 1
2 eE2 1 1
2 mH2d dv 2 3
sE2 dv
(10.72)
Applying the divergence theorem to the left-hand side gives
1E 3 H2 # dS 5 2 '
't 3
c 1
2 eE2 1 1
2 mH2d dv 2 3
sE2dv
(10.73)
total power
rate of decrease in
ohmic power
leaving the volume 5 energy stored in electric 2
dissipated
and magnetic fields
(10.74)
10.8 Power and the Poynting Vector  503
Equation (10.73) is referred to as Poynting’s theorem.2 The various terms in the equation
are identified using energy-conservation arguments for EM fields. The first term on the
right-hand side of eq. (10.73) is interpreted as the rate of decrease in energy stored in the
electric and magnetic fields. The second term is the power dissipated because the medium
is conducting 1s 2 02. The quantity E 3 H on the left-hand side of eq. (10.73) is known
as the Poynting vector , measured in watts per square meter (W/m2); that is,
5 E 3 H
(10.75)
It represents the instantaneous power density vector associated with the EM field at a given
point. The integration of the Poynting vector over any closed surface gives the net power
flowing out of that surface.
Poynting’s theorem states that the net power flowing out of a given volume v is equal to
the time rate of decrease in the energy stored within v minus the ohmic losses.
The theorem is illustrated in Figure 10.11.
It should be noted that  is normal to both E and H and is therefore along the
­direction of wave propagation ak for uniform plane waves. Thus
ak 5 aE 3 aH
(10.49)
The fact that  points along ak causes  to be regarded as a “pointing” vector.
Again, if we assume that
E1z, t2 5 Eoe2az cos1vt 2 bz2ax
then
H1z, t2 5 Eo
0 h 0  e2az cos1vt 2 bz 2 uh2ay
and
1z, t2 5 Eo
0 h 0  e22az cos1vt 2 bz2 cos1vt 2 bz 2 uh2az
2 0 h 0  e22az 3cos uh 1 cos12vt 2 2bz 2 uh2 4az
(10.76)
2 After J. H. Poynting, “On the transfer of energy in the electromagnetic field,” Philosophical Transactions,
vol. 174, 1883, p. 343.
504  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
FIGURE 10.11  Illustration of power
­balance for EM fields.
since cos A cos B 5 1
2 3cos1A 2 B2 1 cos1A 1 B2 4. To determine the time-average
Poynting vector ave(z) (in W/m2), which is of more practical value than the
instantaneous Poynting vector (z, t), we integrate eq. (10.76) over the period
T 5 2p/v; that is,
ave1z2 5 1
T 3
1z, t2 dt
(10.77)
It can be shown (see Problem 10.4 ) that this is equivalent to
ave1z2 5 1
2 Re1Es 3 H*s2
(10.78)
By substituting eq. (10.76) into eq. (10.77), we obtain
ave1z2 5
2 0 h 0  e22az cos uh az
(10.79)
The total time-average power crossing a given surface S is given by
Pave 5 3
ave # dS
(10.80)
10.8 Power and the Poynting Vector  505
We should note the difference between , ave, and Pave: whereas 1x, y, z, t2 is the
Poynting vector in watts per square meter and is time varying, ave(x, y, z), also in watts
per square meter, is the time average of the Poynting vector ; it is a vector but is time
invariant. ­Finally, Pave is a total time-average power through a surface in watts; it is a scalar.
In a nonmagnetic medium
E 5 4 sin12p 3 107t 2 0.8x2az V/m
Find
(a)	 «r , h
(b)	 The time-average power carried by the wave
(c)	 The total power crossing 100 cm2 of plane 2x 1 y 5 5
Solution:
(a)	 Since a 5 0 and b 2 v/c, the medium is not free space but a lossless medium:
b 5 0.8, v 5 2p 3 107, m 5 mo 1nonmagnetic2, e 5 eoer
EXAMPLE 10.8
Hence
b 5 v"me 5 v"moeoer 5 v
c  "er
"er 5 bc
v 5 0.813 3 1082
2p 3 107
5 12
er 5 14.59
h 5 Å
e 5 Å
eoer
5 120p
"er
5 120p # p
12 5 10p2
5 98.7 V
(b)  5 E 3 H 5 E2
h  sin21vt 2 bx2ax
ave 5 1
T 3
 dt 5 E2
2h ax 5
2 3 10p2 ax
5 81ax mW/m2
(c) On plane 2x 1 y 5 5 (see Example 3.5 or 8.5),
an 5
2ax 1 ay
506  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
PRACTICE EXERCISE  10.8
In free space, H 5 0.2 cos1vt 2 bx2az A/m. Find the total power passing through:
(a)  A square plate of side 10 cm on plane x 1 y 5 1
(b)  A circular disk of radius 5 cm on plane x 5 1.
Answer:  (a) 53.31 mW,  (b) 59.22 mW.
10.9  REFLECTION OF A PLANE WAVE AT NORMAL INCIDENCE
So far, we have considered uniform plane waves traveling in unbounded, homogeneous,
isotropic media. When a plane wave from one medium meets a different medium, it is
partly reflected and partly transmitted. The proportion of the incident wave that is reflected
or transmitted depends on the constitutive parameters 1e, m, s2 of the two media involved.
Here we will assume that the incident plane wave is normal to the boundary between the
media; oblique incidence of plane waves will be covered in the next section after we have
presented the simpler case of normal incidence.
Suppose that a plane wave propagating along the 1z-direction is incident normally on
the boundary z 5 0 between medium 11z , 02 characterized by s1, «1, m1 and medium
21z . 02 characterized by s2, «2, m2, as shown in Figure 10.12. In Figure 10.12, subscripts
i, r, and t denote incident, reflected, and transmitted waves, respectively. The incident,
reflected, and transmitted waves shown in Figure 10.12 are obtained as follows.
Incident Wave
1Ei, Hi2 is traveling along 1az in medium 1. If we suppress the time factor e jvt and assume
that
Eis1z2 5 Eioe2g1z
ax
(10.81)
Hence the total power is
Pave 5 3  ave # dS 5 ave # S an
5 181 3 1023ax2 # 1100 3 10242 c
2ax 1 ay
5 162 3 1025
5 724.5 mW
10.9 Reflection of a Plane Wave at Normal Incidence  507
then
His1z2 5 Hioe2g1z
ay 5 Eio
e2g1z
ay
(10.82)
Reflected Wave
1Er, Hr2 is traveling along 2az in medium 1. If
Ers1z2 5 Eroeg1z
ax
(10.83)
then
Hrs1z2 5 Hro eg1z12ay2 5 2Ero
eg1z
ay
(10.84)
where Ers has been assumed to be along ax. To satisfy the necessary boundary conditions
at the interface, we will consistently assume that for normal incidence Ei, Er, and Et have
the same polarization.
Transmitted Wave
1Et, Ht2 is traveling along 1az in medium 2. If
Ets1z2 5 Eto e2g2z
ax
(10.85)
then
Hts1z2 5 Hto e2g2z ay 5 Eto
e2g2z
ay
(10.86)
FIGURE 10.12  A plane wave incident normally on an interface
between two different media.
508  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
In eqs. (10.81) to (10.86), Eio, Ero, and Eto are, respectively, the magnitudes of the incident,
reflected, and transmitted electric fields at z 5 0.
Notice from Figure 10.12 that the total field in medium 1 comprises both the incident
E1 5 Ei 1 Er,  H1 5 Hi 1 Hr
E2 5 Et,  H2 5 Ht
At the interface z 5 0, the boundary conditions require that the tangential components
of E and H fields must be continuous. Since the waves are transverse, E and H fields
are entirely tangential to the interface. Hence at z 5 0, E1tan 5 E2tan and H1tan 5 H2tan
imply that
Ei102 1 Er102 5 Et102  S   Eio 1 Ero 5 Eto
(10.87)
Hi102 1 Hr102 5 Ht102  S   1
1Eio 2 Ero2 5 Eto
(10.88)
From eqs. (10.87) and (10.88), we obtain
Ero 5 h2 2 h1
h2 1 h1
Eio
(10.89)
and
Eto 5
2h2
h2 1 h1
Eio
(10.90)
We now define the reflection coefficient G and the transmission coefficient t from
eqs. (10.89) and (10.90) as
G 5 Ero
Eio
5 h2 2 h1
h2 1 h1
(10.91a)
Ero 5 GEio
(10.91b)
and
t 5 Eto
Eio
2h2
h2 1 h1
(10.92a)
Eto 5 tEio
(10.92b)
and the reflected fields, whereas medium 2 has only the transmitted field; that is,
10.9 Reflection of a Plane Wave at Normal Incidence  509
Note that
1.	 1 1 G 5 t
2.	 Both  and  are dimensionless and may be complex.
3.	 0 # 0 G 0 # 1
(10.93)
The case just considered is the general case. Let us now consider the following special
case: medium 1 is a perfect dielectric 1lossless, s1 5 02 and medium 2 is a perfect conduc­
tor 1s2 . `2. For this case, h2 5 0; hence, G 5 21, and t 5 0, showing that the wave is
totally reflected. This should be expected because fields in a perfect conductor must vanish,
so there can be no transmitted wave 1E2 5 02. The totally reflected wave combines with
the incident wave to form a standing wave. A standing wave “stands” and does not travel; it
consists of two traveling waves 1Ei and Er2 of equal amplitudes but in opposite ­directions.
Combining eqs. (10.81) and (10.83) gives the standing wave in medium 1 as
E1s 5 Eis 1 Ers 5 1Eioe2g1z 1 Eroeg1z2ax
(10.94)
But
G 5 Ero
Eio
5 21, s1 5 0, a1 5 0, g1 5 jb1
Hence,
E1s 5 2Eio1e jb1z 2 e2jb1z2ax
E1s 5 22jEio sin b1z ax
(10.95)
Thus
E1 5 Re1E1sejvt2
E1 5 2Eio sin b1z sin vt ax
(10.96)
By taking similar steps, it can be shown that the magnetic field component of the wave is
H1 5 2Eio
cos b1z cos vt ay
(10.97)
A sketch of the standing wave in eq. (10.96) is presented in Figure 10.13 for t 5 0, T/8, T/4,
3T/8, T/2, and so on, where T 5 2p/v. From Figure 10.13, we notice that the wave does
not travel but oscillates.
When media 1 and 2 are both lossless, we have another special case: s1 5 0 5 s2. In
this case, h1 and h2 are real and so are G and t. Let us consider two more cases:
510  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
CASE 1.
If h2
ted wave in medium 2. However, the incident and reflected waves have amplitudes that are
not equal in magnitude. It can be shown that a relative maximum of 0 E1 0  occurs at
2b1zmax 5 np
zmax 5 2np
5 2nl1
2 ,  n 5 0, 1, 2, . . .
(10.98)
and the minimum values of 0 E1 0  occur at
2b1zmin 5 12n 1 12 p
zmin 5 2
12n 1 12p
2b1
5 2
12n 1 12
l1,  n 5 0, 1, 2, . . .
(10.99)
CASE 2.
If h2 , h1, G , 0. For this case, the locations of 0 E1 0  maximum are given by eq. (10.99),
whereas those of 0 E1 0  minimum are given by eq. (10.98). All these are illustrated in
Figure 10.14. Note that
FIGURE  10.13  Standing waves E 5 2Eio sin b1z sin vt ax. The curves
0, 1, 2, 3, 4, . . . , are, respectively, at times t 5 0, T/8, T/4, 3T/8, T/2, . . . ;
l 5 2p/b1.
. h , G . 0. Again there is a standing wave in medium 1, but there is also a transmit­
10.9 Reflection of a Plane Wave at Normal Incidence  511
1.	 0 H1 0  minimum occurs whenever there is 0 E1 0  maximum, and vice versa.
2.	 The transmitted wave (not shown in Figure 10.14) in medium 2 is a purely travel­
ing wave, and consequently there are no maxima or minima in this region.
The ratio of 0 E1 0 max to 0 E1 0 min 1or 0 H1 0 max to 0 H1 0 min2 is called the standing wave
ratio s; that is,
s 5
0 E1 0 max
0 E1 0 min
0 H1 0 max
0 H1 0 min
5 1 1 0 G 0
1 2 0 G 0 
(10.100)
0 G 0 5 s 2 1
s 1 1
(10.101)
Since 0 G 0 # 1, it follows that 1 # s # `. The standing wave ratio is dimensionless, and it
is customarily expressed in decibels (dB) as
s dB 5 20 log10 s
(10.102)
In free space 1z # 02, a plane wave with
Hi 5 10 cos1108t 2 bz2ax mA/m
is incident normally on a lossless medium 1e 5 2eo, m 5 8mo2 in region z $ 0. Determine
the reflected wave Hr, Er and the transmitted wave Ht, Et.
FIGURE 10.14  Standing waves due to reflection at an interface between
two lossless media; l 5 2p/b1.
EXAMPLE 10.9
512  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
Solution:
This problem can be solved in two different ways.
Method 1:  Consider the problem as illustrated in Figure 10.15. For free space,
b1 5 v
c 5
108
3 3 108 5 1
h1 5 ho 5 120p
Given that Hi 5 10 cos1108t 2 b1z2ax mA/m, we expect that
Ei 5 Eio cos1108t 2 b1z2aEi
where
aEi 5 aHi 3 aki 5 ax 3 az 5 2ay
and
Eio 5 h1Hio 5 10 ho
Hence,
Ei 5 210ho cos1108t 2 b1z2ay mV/m
FIGURE 10.15  For Example 10.9.
For the lossless dielectric medium,
b2 5 v"me 5 v"moeo"mrer 5 v
# 142 5 4b1 5 4
h2 5 Å
e 5 Å
5 2 ho
10.9 Reflection of a Plane Wave at Normal Incidence  513
Now
Ero
Eio
5 G 5 h2 2 h1
h2 1 h1
5 2ho 2 ho
2ho 1 ho
5 1
Ero 5 1
3 Eio
Thus
Er 5 210
3  ho cosa108t 1 1
3 zbay mV/m
from which we easily obtain Hr as
Hr 5 210
3  cosa108t 1 1
3 zbax mA/m
Similarly,
Eto
Eio
5 t 5 1 1 G 5 4
3  or  Eto 5 4
3 Eio
Thus
Et 5 Eto cos1108t 2 b2z2aEt
where aEt 5 aEi 5 2ay. Hence,
Et 5 240
3  ho cosa108t 2 4
3 zbay mV/m
from which we obtain
Ht 5 20
3  cosa108t 2 4
3 zbax mA/m
Method 2:  Alternatively, we can obtain Hr and Ht directly from Hi by using
Hro
Hio
5 2G  and  Hto
Hio
5 t h1
Thus
Hro 5 21
3 Hio 5 210
Hto 5 4
3 ho
2ho
# Hio 5 2
3 Hio 5 20
514  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
and
Hr 5 210
3  cos1108t 1 b1z2ax mA/m
Ht 5 20
3  cos1108t 2 b2z2ax mA/m
as obtained by Method 1.
Notice that the boundary conditions at z 5 0, namely,
Ei102 1 Er102 5 Et102 5 240
3  ho cos1108t2ay
and
Hi102 1 Hr102 5 Ht102 5 20
3  cos1108t2ax
are satisfied. The boundary conditions can always be used to cross-check E and H.
PRACTICE EXERCISE  10.9
A 5 GHz uniform plane wave Eis 5 10 e2jbz ax V/m in free space is incident normally
on a large, plane, lossless dielectric slab 1z . 02 having e 5 4eo, m 5 mo. Find the
­reflected wave Ers and the transmitted wave Ets.
Answer:  23.333 exp1 jb1z2ax V/m, 6.667 exp12jb2z2ax V/m, where b2 5 2b1 5
200p/3.
Given a uniform plane wave in air as
Ei 5 40 cos1vt 2 bz2ax 1 30 sin1vt 2 bz2ay V/m
(a)	 Find Hi.
(b)	 If the wave encounters a perfectly conducting plate normal to the z-axis at z 5 0, find
the reflected wave Er and Hr.
(c)	 What are the total E and H fields for z # 0?
(d)	 Calculate the time-average Poynting vectors for z # 0 and z $ 0.
Solution:
(a)	 This is similar to the problem in Example 10.3. We may treat the wave as consisting of
two waves Ei1 and Ei2, where
Ei1 5 40 cos1vt 2 bz2ax,  Ei2 5 30 sin1vt 2 bz2ay
EXAMPLE 10.10
10.9 Reflection of a Plane Wave at Normal Incidence  515
At atmospheric pressure, air has er 5 1.0006 . 1. Thus air may be regarded as free space.
Let Hi 5 Hi1 1 Hi2.
Hi1 5 Hi1o cos1vt 2 bz2aH1
where
Hi1o 5 Ei1o
120p 5 1
aH1 5 ak 3 aE 5 az 3 ax 5 ay
Hence
Hi1 5 1
3p cos1vt 2 bz2ay
Similarly,
Hi2 5 Hi2o sin1vt 2 bz2aH2
where
Hi2o 5 Ei2o
120p 5 1
aH2 5 ak 3 aE 5 az 3 ay 5 2ax
Hence
Hi2 5 2 1
4p sin1vt 2 bz2ax
and
Hi 5 Hi1 1 Hi2
5 2 1
4p sin1vt 2 bz2ax 1 1
3p cos1vt 2 bz2ay mA/m
This problem can also be solved using Method 2 of Example 10.3.
(b)	 Since medium 2 is perfectly conducting,
ve2
W 1 S  h2 V h1
that is,
G . 21,  t 5 0
showing that the incident E and H fields are totally reflected:
Ero 5 G Eio 5 2Eio
Hence,
Er 5 240 cos1vt 1 bz2ax 2 30 sin1vt 1 bz2ay V/m
516  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
We can find Hr from Er just as we did in part (a) of this example or by using Method 2 of
Example 10.9, starting with Hi. Whichever approach is taken, we obtain
Hr 5 1
3p cos1vt 1 bz2ay 2 1
4p sin1vt 1 bz2ax A/m
(c)	 The total fields in air
E1 5 Ei 1 Er  and  H1 5 Hi 1 Hr
can be shown to be standing waves. The total fields in the conductor are
E2 5 Et 5 0,    H2 5 Ht 5 0
PRACTICE EXERCISE  10.10
The plane wave E 5 50 sin1vt 2 5x2ay V/m in a lossless medium 1m 5 4mo, e 5 eo2
encounters a lossy medium 1m 5 mo, e 5 4eo, s 5 0.1 S/m2 normal to the x-axis at
x 5 0. Find
(a)  G, t, and s
(b)  Er and Hr
(c)  Et and Ht
(d)  The time-average Poynting vectors in both regions
(d) For z # 0,
1ave 5
0 E1s 0 2
2h1
ak 5
2ho
3E2
ioaz 2 E2
roaz4
240p 3 1402 1 3022az 2 1402 1 3022az4
 0
For z $ 0,
2ave 5
0 E2S 0 2
2h2
ak 5 E2
2h2
az 5 0
Answer:  (a)  0.8186 lii
171.1°, 0.2295 lii
33.56°, 10.025, (b) 40.93 sin1vt 1 5x 1
171.9°2ay V/m, 254.3 sin1vt 1 5x 1 171.9°2az mA/m,
(c)  11.47 e26.021xsin1vt 27.826x 1 33.56º2ay V/m,
120.2 e26.021x sin1vt 2 7.826x 2 4.01º2az mA/m,
(d) 0.5469 ax W/m2, 0.5469 exp1212.04x2ax W/m2.
10.10 Reflection of a Plane Wave at Oblique Incidence  517
3 The phenomenon of signal distortion due to a dependence of the phase velocity on frequency is known as
dispersion.
†10.10  REFLECTION OF A PLANE WAVE AT OBLIQUE INCIDENCE
We now consider a more general situation than that in Section 10.9. To simplify the analy­
sis, we will assume that we are dealing with lossless media. (We may extend our analysis to
E1r, t2 5 Eo cos1k # r 2 vt2
5 Re3Eoej1k # r2vt24
(10.103)
where r 5 xax 1 yay 1 zaz is the radius or position vector and k 5 kxax 1 kyay 1 kzaz
is the wave number vector or the propagation vector; k is always in the direction of wave
propagation. The magnitude of k is related to v according to the dispersion relation:3
k2 5 k2
x 1 k2
y 1 k2
z 5 v2me
(10.104)
Thus, for lossless media, k is essentially the same as b in the preceding sections. With the
general form of E as in eq. (10.103), Maxwell’s equations for a source-free region reduce to
k 3 E 5 vmH
(10.105a)
k 3 H 5 2veE
(10.105b)
k # H 5 0
(10.105c)
k # E 5 0
(10.105d)
showing that (i) E, H, and k are mutually orthogonal, and (ii) E and H lie on the plane
k # r 5 kxx 1 kyy 1 kzz 5 constant
From eq. (10.105a), the H field corresponding to the E field in eq. (10.103) is
H 5 1
vm k 3 E 5 ak 3 E
(10.106)
Having expressed E and H in the general form, we can now consider the oblique inci­
dence of a uniform plane wave at a plane boundary as illustrated in Figure 10.16(a). The
plane defined by the propagation vector k and a unit normal vector an to the boundary is
called the plane of incidence. The angle ui between k and an is the angle of incidence.
that of lossy media by merely replacing « by « .) It can be shown (see Problems 10.69 and
10.72) that a uniform plane wave takes the general form of
518  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
ted (or refracted) wave is in medium 2. Let
Ei 5 Eio cos1kixx 1 kiyy 1 kizz 2 vit2
(10.107a)
Er 5 Ero cos1krxx 1 kryy 1 krzz 2 vrt2
(10.107b)
Et 5 Eto cos1ktxx 1 ktyy 1 ktzz 2 vtt2
(10.107c)
where ki, kr, and kt with their normal and tangential components are shown in
Figure  10.16(b). Since the tangential component of E must be continuous across the
boundary z 5 0,
Ei 1z 5 02 1 Er 1z 5 02 5 Et 1z 5 02
(10.108)
This boundary condition can be satisfied by the waves in eq. (10.107) for all x and y only if
1.	 vi 5 vr 5 vt 5 v
2.	 kix 5 krx 5 ktx 5 kx
3.	 kiy 5 kry 5 kty 5 ky
FIGURE 10.16  Oblique incidence of a plane wave: (a) illustration of i, r,
and t; (b) illustration of the normal and tangential components of k.
Again, both the incident and the reflected waves are in medium 1, while the transmit­
10.10 Reflection of a Plane Wave at Oblique Incidence  519
Condition 1 implies that the frequency is unchanged. Conditions 2 and 3 require that the
tangential components of the propagation vectors be continuous (called the phase-matching
conditions). This means that the propagation vectors ki, kt, and kr must all lie in the plane
of incidence. Thus, by conditions 2 and 3,
ki sin ui 5 kr sin ur
(10.109)
ki sin ui 5 kt sin ut
(10.110)
where ur is the angle of reflection and ut is the angle of transmission. But for lossless media,
ki 5 kr 5 b1 5 v"m1e1
(10.111a)
kt 5 b2 5 v"m2e2
(10.111b)
From eqs. (10.109) and (10.111a), it is clear that
ur 5 ui
(10.112)
so that the angle of reflection ur equals the angle of incidence ui, as in optics. Also from
eqs. (10.110) and (10.111),
where n1 5 c"m1e1 5 c/u1 and n2 5 c"m2e2 5 c/u2 are the refractive indices of the
media.
Based on these general preliminaries on oblique incidence, we will now consider two
special cases: one with the E field perpendicular to the plane of incidence and the other
with the E field parallel to it. Any other polarization may be considered as a linear combi­
nation of these two cases.
A.  Parallel Polarization
Figure 10.17, where the E field lies in the xz-plane, the plane of incidence, illustrates the case
of parallel polarization. In medium 1, we have both incident and reflected fields given by
Eis 5 Eio1cos ui ax 2 sin ui az2 e2jb11x sin ui1z cos ui2 
(10.115a)
where u 5 v/k is the phase velocity. Equation (10.113) is the well-known  Snell’s law, which
can be written as
n1 sin ui 5 n2 sin ut
(10.114)
sin ut
sin ui
5 ki
5 u2
5 Å
m1e1
m2e2
(10.113)
520  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
His 5 Eio
e2jb11x sin ui1z cos ui2ay
(10.115b)
Ers 5 Ero1cos ur ax 1 sin ur az2 e2jb11x sin ur2z cos ur2
(10.116a)
Hrs 5 2Ero
e2jb11x sin ur2z cos ur2ay
(10.116b)
where b1 5 v"m1e1. Notice carefully how we arrive at each field component. The
trick in deriving the components is to first get the propagation vector k as shown in
Figure 10.16(b) for incident, reflected, and transmitted waves. Once k is known, we
define Es such that = # Es 5 0 or k # Es 5 0 and then Hs is obtained from Hs 5
vm 3 Es 5  ak 3 E
The transmitted fields exist in medium 2 and are given by
Ets 5 Eto1cos ut ax 2 sin ut az2 e2jb21x sin ut1z cos ut2
(10.117a)
Hts 5 Eto
e2jb21x sin ut1z cos ut2ay
(10.117b)
where b2 5 v"m2e2. Should our assumption about the relative directions in eqs. (10.115)
to (10.117) be wrong, the final result will show us this by means of its sign.
Requiring that ur 5 ui and that the tangential components of E and H be continuous
at the boundary z 5 0, we obtain
1Eio 1 Ero2 cos ui 5 Eto cos ut 
(10.118a)
1Eio 2 Ero2 5 1
Eto
(10.118b)
Expressing Ero and Eto in terms of Eio, we obtain
FIGURE 10.17  Oblique incidence with
E ­par­allel to the plane of incidence.
10.10 Reflection of a Plane Wave at Oblique Incidence  521
Gy 5 Ero
Eio
5 h2 cos ut 2 h1 cos ui
h2 cos ut 1 h1 cos ui
(10.119a)
Ero 5 GyEio
(10.119b)
and
ty 5 Eto
Eio
2h2 cos ui
h2 cos ut 1 h1 cos ui
(10.120a)
Eto 5 tyEio
(10.120b)
Equations (10.119) and (10.120) are called Fresnel’s equations. Gy and ty are known as
Fresnel coefficients. Note that the equations ­reduce to eqs. (10.91) and (10.92) when
ui 5 ut 5 0 as expected. Since ui and ut are related according to Snell’s law of eq. (10.113),
eqs. (10.119) and (10.120) can be written in terms of ui by substituting
From eqs. (10.119) and (10.120), it is easily shown that
1 1 Gy 5 ty acos ut
cos ui
(10.122)
From eq. (10.119a), it is evident that it is possible that Gy 5 0 because the numerator
is the difference of two terms. Under this condition, there is no reflection 1Ero 5 02, and
the incident angle at which this takes place is called the Brewster angle uBy. The Brewster
angle is also known as the polarizing angle because an arbitrarily polarized incident wave
will be reflected with only the component of E perpendicular to the plane of incidence. The
Brewster effect is utilized in a laser tube where quartz windows are set at the Brewster angle
to control polarization of emitted light. The Brewster angle is obtained by setting ui 5 uBy
when Gy 5 0 in e
hat is,
h2 cos ut 5 h1 cos uBy
211 2 sin2 ut2 5 h1
211 2 sin2 uBy2
Introducing eq. (10.113) or (10.114) gives
sin2 uBy 5 1 2 m2e1/m1e2
1 2 1e1/e22 2 
(10.123)
cos ut 5 "1 2 sin2 ut 5 "1 2 1u2/u12 2sin2 ui
(10.121)
qs. (10.119); t
522  CHAPTER 10  ELECTROMAGNETIC WAVE PROPAGATION
It is of practical value to consider the case when the dielectric media are not only lossless
but nonmagnetic as well—that is, m1 5 m2 5 mo. For this situation, eq. (10.123) becomes
showing that there is a Brewster angle for any combination of «1 and «2.
B.  Perpendicular Polarization
When the E field is perpendicular to the plane of incidence (the xz-plane) as shown in
in medium 1 are given by
Eis 5 Eioe2jb11x sin ui1z cos ui2ay
(10.125a)
His 5 Eio
12cos ui ax 1 sin ui az2 e2jb11x sin ui1z cos ui2
(10.125b)
Ers 5 Eroe2jb11x sin ur2z cos ur2 ay
(10.126a)
Hrs 5 Ero
1cos ur ax 1 sin ur az2 e2jb11x sin ur2z cos ur2 
(10.126b)
while the transmitted fields in medium 2 are given by
Ets 5 Etoe2jb21x sin ut1z cos ut2 ay
(10.127a)
Hts 5 Eto
12cos ut ax 1 sin ut az2 e2jb21x sin ut1z cos ut2
(10.127b)
Notice that in defining the field components in eqs. (10.125) to (10.127), Maxwell’s equa­
tions (10.105) are always satisfied. Again, requiring that the tangential components of E
and H be continuous at z 5 0 and setting ur equal to ui, we get
Eio 1 Ero 5 Eto
(10.128a)
1Eio 2 Ero2 cos ui 5 1
Eto cos ut
(10.128b)
tan uBy 5 Å
5 n2
(10.124)
sin2 uBy 5
1 1 e1/e2
S  sin uBy 5 Å
e1 1 e2
Figure 10.18, we have perpendicular polarization. This may also be viewed as the case in
which the H field is parallel to the plane of incidence. The incident and reflected fields

# Sadiku《Elements of Electromagnetics》Chapter 11

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 580-629 of 926 (926 total)

---

## Transmission Lines

553
C H A P T E R
553
11.1  INTRODUCTION
Our discussion in Chapter 10 was essentially on wave propagation in unbounded media,
media of infinite extent. Such wave propagation is said to be unguided in that the uniform
plane wave exists throughout all space, and EM energy associated with the wave spreads
over a wide area. Wave propagation in unbounded media is used in radio or TV broadcast-
ing, where the information being transmitted is meant for everyone who may be interested.
Another means of transmitting power or information is by guided structures.
Guided structures serve to guide (or direct) the propagation of energy from the source
to the load. Typical examples of such structures are transmission lines and waveguides.
Waveguides are discussed in the next chapter; transmission lines are considered in this
chapter.
Transmission lines are commonly used in power distribution (at low frequencies)
and in communications (at high frequencies). Transmission lines such as twisted-pair and
coaxial cables (thinnet and thicknet) are used in computer networks such as the Ethernet
and the Internet.
A transmission line basically consists of two or more parallel conductors used to
connect a source to a load. The source may be a hydroelectric generator, a transmit-
ter, or an oscillator; the load may be a factory, an antenna, or an oscilloscope. Typical
transmission lines include coaxial cable, a two-wire line, a parallel-plate or planar line,
a wire above the conducting plane, and a microstrip line. These lines are portrayed in
Figure 11.1. Notice that each of these lines consists of two conductors in parallel. Coaxial
cables are routinely used in electrical laboratories and in connecting TV sets to antennas.
Microstrip lines (similar to that in Figure 11.1e) are particularly important in integrated
circuits, where metallic strips connecting electronic elements are deposited on dielectric
substrates.
Transmission line problems are usually solved by means of EM field theory and elec-
tric circuit theory, the two major theories on which electrical engineering is based. In this
chapter, we use circuit theory because it is easier to deal with mathematically. The basic
concepts of wave propagation (such as propagation constant, reflection coefficient, and
standing wave ratio) covered in the preceding chapter apply here.
TRANSMISSION LINES
Kind hearts are the garden. Kind thoughts are the roots. Kind words are the flowers.
Kind deeds are the fruits. Take care of your garden, And keep out the weeds. Fill it up
with sunshine, Kind words and kind deeds.
—LONGFELLOW
554  CHAPTER 11  TRANSMISSION LINES
Our analysis of transmission lines will include the derivation of the transmission line
equations and characteristic quantities, the use of the Smith chart, various practical appli-
cations of transmission lines, and transients on transmission lines.
(a)
(b)
(c)
(d)
(e)
FIGURE 11.1  Typical transmission lines in cross-sectional view: (a) coaxial line, (b) two-wire
line, (c) planar line, (d) wire above conducting plane, (e) microstrip line.
11.2  TRANSMISSION LINE PARAMETERS
It is customary and convenient to describe a transmission line in terms of its line param-
eters, which are its resistance per unit length R, inductance per unit length L, conductance
per unit length G, and capacitance per unit length C. Each of the lines shown in Figure 11.1
has specific formulas for finding R, L, G, and C. For coaxial, two-wire, and planar lines,
the formulas for calculating the values of R, L, G, and C are provided in Table 11.1. The
dimensions of the lines are as shown in Figure 11.2. Some of the formulas1 in Table 11.1
were derived in Chapters 6 and 8. It should be noted that
1.	 The line parameters R, L, G, and C are not discrete or lumped. Rather, they are dis-
tributed as shown in Figure 11.3. By this we mean that the parameters are ­uniformly
distributed along the entire length of the line.
1Similar formulas for other transmission lines can be obtained from engineering handbooks or data books—for
example, M. A. R. Gunston, Microwave Transmission-Line Impedance Data. London: Van Nostrand Reinhold, 1972.
11.2 Transmission Line Parameters  555
2.	 For each line, the conductors are characterized by sc, mc, ec 5 eo, and the homoge­
neous dielectric separating the conductors is characterized by s, m, .
3.	 G 2 1/R; R is the ac resistance per unit length of the conductors comprising the line,
and G is the conductance per unit length due to the dielectric medium ­separating
the conductors.
4.	 The value of L shown in Table 11.1 is the external inductance per unit length, that
is, L 5 Lext. The effects of internal inductance Lin 15 R /v 2 are negligible at the high
frequencies at which most communication systems operate.
5.	 For each line,
LC 5 me  and  G
C 5 s
(11.1)
As a way of preparing for the next section, let us consider how an EM wave propa­
gates through a two-conductor transmission line. For example, consider the coaxial
line connecting the generator or source to the load as in Figure 11.4(a). When switch
S is closed, the inner conductor is made positive with respect to the outer one so that
TABLE 11.1  Distributed Line Parameters at High Frequencies*
Parameters
Coaxial Line
Two-Wire Line
Planar Line
R 1V/m2
2pdsc
c 1
a 1 1
b d
padsc
wdsc
1d V a, c 2 b2
1d V a2
1d V t2
L 1H/m2
2p ln b
p cosh21 d
G 1S/m2
2ps
ln b
cosh21 d
C 1F/m2
2pe
ln b
cosh21 d
1w W d2
*d 5
"pfmcsc
5 skin depth of the conductor; cosh21 d
2a . ln d
a if c d
2ad
W 1.
FIGURE 11.2  Common transmission lines: (a) coaxial line,
(b) two-wire line, (c) planar line.
556  CHAPTER 11  TRANSMISSION LINES
the E field is ­radially outward as in Figure 11.4(b). According to Ampère’s law, the H
field ­encircles the current-carrying conductor as in Figure 11.4(b). The Poynting vector
1E 3 H2 points along the transmission line. Thus, closing the switch simply establishes
a disturbance, which appears as a transverse electromagnetic (TEM) wave propagating
along the line. This wave is a nonuniform plane wave, and by means of it, power is trans-
mitted through the line.
FIGURE 11.3  Distributed parameters of a two-conductor transmission line.
FIGURE 11.4  (a) Coaxial line connecting the generator to the load;
(b) E and H fields on the coaxial line.
11.3 Transmission Line Equations  557
As mentioned in Section 11.2, a two-conductor transmission line supports a TEM
wave; that is, the electric and magnetic fields on the line are perpendicular to each other
and transverse to the direction of wave propagation. An important property of TEM waves
is that the fields E and H are uniquely related to voltage V and current I, ­respectively:
V 5 23
E # dl,  I 5 C
H # dl
(11.2)
In view of this, we will use circuit quantities V and I in solving the transmission line
problem instead of solving field quantities E and H (i.e., solving Maxwell’s equations and
boundary conditions). The circuit model is simpler and more convenient.
Let us examine an incremental portion of length z of a two-conductor transmission
line. We intend to find an equivalent circuit for this line and derive the line equations. From
Figure 11.3, we expect the equivalent circuit of a portion of the line to be as in Figure 11.5.
The model in Figure 11.5 is in terms of the line parameters R, L, G, and C, and may repre­
sent any of the two-conductor lines of Figure
The model is called the L-type equiva­
By applying Kirchhoff’s voltage law to the outer loop of the circuit in Figure 11.5, we
obtain
V1z, t2 5 R Dz I1z, t2 1 L Dz 'I1z, t2
1 V1z 1 Dz, t2
2V1z 1 Dz, t2 2 V1z, t2
5 RI1z, t2 1 L 'I1z, t2
(11.3)
11.3  TRANSMISSION LINE EQUATIONS
FIGURE 11.5  An L-type equivalent circuit model of a two-conductor
transmission line of differential length Dz.
11.2.
lent circuit; there are other possible types. In the model of Figure 11.5, we assume that the
wave propagates along the 1z-direction, from the generator to the load.
558  CHAPTER 11  TRANSMISSION LINES
Taking the limit of eq. (11.3) as Dz S  0 leads to
2'V1z, t2
5 RI1z, t2 1 L 'I1z, t2
(11.4)
Similarly, applying Kirchhoff’s current law to the main node of the circuit in Figure 11.5
gives
I1z, t2 5 I1z 1 Dz, t2 1 DI
5 I1z 1 Dz, t2 1 G Dz V1z 1 Dz, t2 1 C Dz 'V1z 1 Dz, t2
2I1z 1 Dz, t2 2 I1z, t2
5 GV1z 1 Dz, t2 1 C 'V1z 1 Dz, t2
(11.5)
As Dz S  0, eq. (11.5) becomes
2'I1z, t2
5 GV1z, t2 1 C 'V1z, t2
(11.6)
If we assume harmonic time dependence so that
V(z, t) 5 Re[Vs(z) ejwt]
(11.7a)
I(z, t) 5 Re[Is(z) ejwt]
(11.7b)
where Vs1z2 and Is1z2 are the phasor forms of V1z, t2 and I1z, t2, respectively, eqs. (11.4)
and (11.6) become
2dVs
dz 5 1R 1 jvL2Is
(11.8)
2dIs
dz 5 1G 1 jvC2Vs
(11.9)
The differential eqs. (11.8) and (11.9) are coupled. To separate them, we take the second
derivative of Vs in eq. (11.8) and employ eq. (11.9) so that we obtain
d2Vs
dz2 5 1R 1 jvL2 1G 1 jvC2Vs
d2Vs
dz2 2 g2Vs 5 0
(11.10)
11.3 Transmission Line Equations  559
where
g 5 a 1 jb 5 "1R 1 jvL2 1G 1 jvC2
(11.11)
By taking the second derivative of Is in eq. (11.9) and employing eq. (11.8), we get
d2Is
dz2 2 g2Is 5 0
(11.12)
We notice that eqs. (11.10) and (11.12) are, respectively, the wave equations for voltage
and current similar in form to the wave equations obtained for plane waves in eqs. (10.17)
and (10.19). Thus, in our usual notations, g in eq. (11.11) is the propagation constant (in
per meter), a is the attenuation constant (in nepers per meter or decibels per meter),2 and
b is the phase constant (in radians per meter). The wavelength l and wave velocity u are,
respectively, given by
l 5 2p
b 
(11.13)
u 5 v
b 5 fl
(11.14)
The solutions of the linear homogeneous differential equations (11.10) and (11.12) are
similar to Case 2 of Example 6.5, namely,
Vs1z2 5 V1
o  e2gz 1 V2
o  egz
h 1z
2z v 
(11.15)
and
Is1z2 5 I1
o  e2gz 1 I2
o  egz
h 1z	 2z v 
(11.16)
where V1
o , V2
o , I1
o , and I2
o  are wave amplitudes; the 1 and 2 signs, respectively, denote
waves traveling along 1z- and 2z-directions, as is also indicated by the arrows. We obtain
the instantaneous expression for voltage as
V1z, t2 5 Re3Vs1z2 e jvt4
5 V1
o  e2az cos1vt 2 bz2 1 V2
o  eaz cos1vt 1 bz2
(11.17)
The characteristic impedance Zo of the line is the ratio of the positively traveling volt-
age wave to the current wave at any point on the line.
2Recall from eq. (10.35) that 1 Np 5 8.686 dB.
560  CHAPTER 11  TRANSMISSION LINES
The characteristic impedance Zo is analogous to h, the intrinsic impedance of the medium
of wave propagation. By substituting eqs. (11.15) and (11.16) into eqs. (11.8) and (11.9) and
equating coefficients of terms egz and e2gz, we obtain
Zo 5 V1
5 2V2
R 1 jvL
G 1 jvC
(11.18)
Zo 5 Å
R 1 jvL
G 1 jvC 5 Ro 1 jXo
(11.19)
where Ro and Xo are the real and imaginary parts of Zo. Do not mistake Ro for R—while
impedance Zo are important properties of the line because both depend on the line param­
eters R, L, G, and C and the frequency of operation. The reciprocal of Zo is the characteristic
­admittance Yo, that is, Yo 5 1/Zo.
The transmission line considered thus far in this section is the lossy type in that the
conductors comprising the line are imperfect 1sc 2 `2 and the dielectric in which the
conductors are embedded is lossy 1s 2 02. Having considered this general case, we may
now consider two special cases: the lossless transmission line and the distortionless line.
A.  Lossless Line (R = 0 = G)
A transmission line is said to be lossless if the conductors of the line are perfect
1sc < ` 2 and the dielectric medium separating them is lossless 1s . 02.
For such a line, it is evident from Table 11.1 that when sc . ` and s . 0,
R 5 0 5 G
(11.20)
This is a necessary condition for a line to be lossless. Thus for such a line, eq. (11.20) forces
eqs. (11.11), (11.14), and (11.19) to become
a 5 0,  g 5 jb 5 jv "LC
(11.21a)
u 5 v
b 5
"LC
5 fl
(11.21b)
Xo 5 0,  Zo 5 Ro 5 Å
(11.21c)
R is in ohms per meter, R  is in ohms. The propagation constant g and the characteristic
11.3 Transmission Line Equations  561
B.  Distortionless Line (R/L = G/C)
A signal normally consists of a band of frequencies; wave amplitudes of different frequency
components will be attenuated differently in a lossy line because a is frequency ­dependent.
Since, in general, the phase velocity of each frequency component is also ­frequency depen­
dent, this will result in distortion.
A distortionless line is one in which the attenuation constant a is frequency indepen-
dent while the phase constant b is linearly dependent on frequency.
From the general expression for a and b [in eq. (11.11)], a distortionless line results if the
line parameters are such that
L 5 G
(11.22)
Thus, for a distortionless line,
g 5 ÅRG a1 1
jvL
R b a1 1
jvC
G b
5 "RG a1 1
jvC
G b 5 a 1 jb
a 5 "RG,  b 5 v"LC
(11.23a)
showing that a does not depend on frequency, whereas b is a linear function of frequency. Also
Zo 5 Å
R 11 1 jvL/R2
G 11 1 jvC/G2 5 Å
G 5 Å
C 5 Ro 1 jXo
Ro 5 Å
G 5 Å
C,  Xo 5 0
(11.23b)
and
u 5 v
b 5
"LC
5 fl
(11.23c)
Note the following important properties.
1.	 The phase velocity is independent of frequency because the phase constant b
­linearly depends on frequency. We have shape distortion of signals unless a and u
are independent of frequency.
562  CHAPTER 11  TRANSMISSION LINES
2.	 Both u and Zo remain the same as for lossless lines.
3.	 A lossless line is also a distortionless line, but a distortionless line is not necessarily
lossless. Although lossless lines are desirable in power transmission, telephone lines
are required to be distortionless.
A summary of our discussion in this section is in Table 11.2. For the greater part of our
analysis, we shall restrict our discussion to lossless transmission lines.
An air line has a characteristic impedance of 70 V and a phase constant of 3 rad/m at
100 MHz. Calculate the inductance per meter and the capacitance per meter of the line.
Solution:
An air line can be regarded as a lossless line because s . 0 and sc S  `. Hence
R 5 0 5 G  and  a 5 0
Zo 5 Ro 5 Å
(11.1.1)
b 5 v "LC
(11.1.2)
Dividing eq. (11.1.1) by eq. (11.1.2) yields
b 5 1
C 5
vRo
2p 3 100 3 1061702 5 68.2 pF/m
From eq. (11.1.1),
L 5 R2
oC 5 1702 2168.2 3 102122 5 334.2 nH/m
EXAMPLE 11.1
TABLE 11.2 Transmission Line Characteristics
Case
Propagation Constant
g 5 a 1 jb
Characteristic Impedance
Zo 5 Ro 1 jXo
General
"1R 1 jvL2 1G 1 jvC2
R 1 jvL
G 1 jvC
Lossless
0 1 jv"LC
C 1 j0
Distortionless
"RG 1 jv"LC
C 1 j0
11.3 Transmission Line Equations  563
A distortionless line has Zo 5 60 V, a 5 20 mNp/m, u 5 0.6c, where c is the speed of
light in a vacuum. Find R, L, G, C, and l at 100 MHz.
Solution:
For a distortionless line,
RC 5 GL  or  G 5 RC
and hence
Zo 5 Å
(11.2.1)
a 5 "RG 5 R Å
L 5 R
(11.2.2a)
R 5 a Zo
(11.2.2b)
But
u 5 v
b 5
"LC
(11.2.3)
From eq. (11.2.2b),
R 5 a Zo 5 120 3 10232 1602 5 1.2 V/m
Dividing eq. (11.2.1) by eq. (11.2.3) results in
L 5 Zo
u 5
0.6 13 3 1082 5 333 nH/m
From eq. (11.2.2a),
G 5 a2
R 5 400 3 1026
1.2
5 333 mS/m
PRACTICE EXERCISE  11.1
A transmission line operating at 500 MHz has Zo 5 80 V, a 5 0.04 Np/m, b 51.5 rad/m.
Find the line parameters R, L, G, and C.
Answer:  3.2 V/m, 38.2 nH/m, 5 3 1024 S/m, 5.97 pF/m.
EXAMPLE 11.2
564  CHAPTER 11  TRANSMISSION LINES
Multiplying eqs. (11.2.1) and (11.2.3) together gives
uZo 5 1
C 5
uZo
0.6 13 3 1082 60 5 92.59 pF/m
l 5 u
f 5 0.6 13 3 1082
108
5 1.8 m
Consider a transmission line of length , characterized by g and Zo, connected to a load ZL
as shown in Figure 11.6(a). Looking into the line, the generator sees the line with the load
as an input impedance Zin. It is our intention in this section to determine the input imped­
ance, the standing wave ratio (SWR), and the power flow on the line.
Let the transmission line extend from z 5 0 at the generator to z 5 , at the load. First
of all, we need the voltage and current waves in eqs. (11.15) and (11.16), that is,
Vs1z2 5 V1
o e2gz 1 V2
o egz
(11.24)
Is1z2 5 V1
e2gz 2 V2
egz
(11.25)
where eq. (11.18) has been incorporated. To find V1
o  and V2
o , the terminal conditions must
be given. For example, if we are given the conditions at the input, say
Vo 5 V1z 5 02,  Io 5 I1z 5 02
(11.26)
11.4  INPUT IMPEDANCE, STANDING WAVE RATIO, AND POWER
PRACTICE EXERCISE  11.2
A telephone line has R 5 30 V/km, L 5 100 mH/km, G 5 0, and C 5 20 mF/km.
At f 5 1 kHz, obtain:
(a)  The characteristic impedance of the line
(b)  The propagation constant
(c)  The phase velocity
Answer:  (a) 70.75liii
21.367° V,  (b) 2.121 3 1024 1 j8.888 3 1023/m,
(c) 7.069 3105 m/s.
11.4 Input Impedance, Standing Wave Ratio, and Power  565
substituting these into eqs. (11.24) and (11.25) results in
o 5 1
2 1Vo 1 ZoIo2
(11.27a)
o 5 1
2 1Vo 2 ZoIo2
(11.27b)
If the input impedance at the input terminals is Zin, the input voltage Vo and the input
­current Io are easily obtained from Figure 11.6(b) as
Vo 5
Zin
Zin 1 Zg
Vg,  Io 5
Zin 1 Zg
(11.28)
On the other hand, if we are given the conditions at the load, say
VL 5 V1z 5 ,2,  IL 5 I1z 5 ,2
(11.29)
Substituting these into eqs. (11.24) and (11.25) gives
o 5 1
2 1VL 1 ZoIL2eg,
(11.30a)
o 5 1
2 1VL 2 ZoIL2e2g,
(11.30b)
FIGURE 11.6  (a) Input impedance due to a line terminated by
a load. (b) Equivalent circuit for finding Vo and Io in terms of
Zin at the input.
566  CHAPTER 11  TRANSMISSION LINES
Next, we determine the input impedance Zin 5 Vs1z2/Is1z2 at any point on the line. At
the generator, for example, eqs. (11.24) and (11.25) yield
Zin 5 Vs1z2
Is1z2 5 Zo1V1
o 1 V2
o 2
o 2 V2
(11.31)
Substituting eq. (11.30) into (11.31) and utilizing the fact that
eg, 1 e2g,
5 cosh g,,  eg, 2 e2g,
5 sinh g,
(11.32a)
tanh g, 5 sinh g,
cosh g, 5 eg, 2 e2g,
eg, 1 e2g,
(11.32b)
we get
Zin 5 Zo c ZL 1 Zo tanh g,
Zo 1 ZL tanh g,d         (lossy)
(11.33)
Although eq. (11.33) has been derived for the input impedance Zin at the generation end,
it is a general expression for finding Zin at any point on the line. To find Zin at a distance
 from the load as in Figure 11.6(a), we replace  by . A formula for calculating the
hyperbolic tangent of a complex number, required in eq. (11.33), is found in Appendix A.3.
For a lossless line, g 5 jb, tanh jb, 5 j tan b,, and Zo 5 Ro, so eq. (11.33) becomes
Zin 5 Zo c
ZL 1 jZo tan b,
Zo 1 jZL tan b,d        (lossless)
(11.34)
showing that the input impedance varies periodically with distance  from the load. The
quantity b in eq. (11.34) is usually referred to as the electrical length of the line and can be
expressed in degrees or radians.
We now define GL as the voltage reflection coefficient (at the load). The reflection coef­
GL 5 V2
o  eg,
o  e2g,
(11.35)
Substituting V2
o  and V1
o  in eq. (11.30) into eq. (11.35) and incorporating VL 5 ZLIL gives
GL 5 ZL 2 Zo
ZL 1 Zo
(11.36)
ficient G  is the ratio of the voltage reflection wave to the incident wave at the load; that is,
11.4 Input Impedance, Standing Wave Ratio, and Power  567
The voltage reflection coefficient at any point on the line is the ratio of the reflected
voltage wave to that of the incident wave.
That is,
G1z2 5 V2
o  egz
o  e2gz 5 V2
e2gz
But z 5 , 2 ,r. Substituting and combining with eq. (11.35), we get
G1z2 5 V2
e2g,e22g,r 5 GLe22g,r
(11.37)
The current reflection coefficient at any point on the line is the negative of the volt-
age reflection coefficient at that point.
Thus, the current reflection coefficient at the load is I2
o  eg,/I1
o  e2g, 5 2GL.
Just as we did for plane waves, we define the standing wave ratio s (otherwise denoted
by SWR) as
s 5 Vmax
Vmin
5 Imax
Imin
5 1 1 0 GL 0
1 2 0 GL 0 
(11.38a)
(11.38b)
It is easy to show that Imax 5 Vmax/Zo and Imin 5 Vmin/Zo. The input impedance Zin in
eq. (11.34) has maxima and minima that occur, respectively, at the maxima and minima of
the voltage standing wave. It can also be shown that
0 Zin 0 max 5 Vmax
Imin
5 sZo
(11.39a)
and
0 Zin 0 min 5 Vmin
Imax
5 Zo
s 
(11.39b)
As a way of demonstrating these concepts, consider a lossless line with characteristic
impedance of Zo 5 50 V. For the sake of simplicity, we assume that the line is terminated
in a pure resistive load ZL 5 100 V and the voltage at the load is 100 V (rms). The condi­
tions on the line are displayed in Figure 11.7. Note from Figure 11.7 that conditions on the
line repeat themselves every half-wavelength.
0 GL 0 5 S 2 1
S 1 1
568  CHAPTER 11  TRANSMISSION LINES
As mentioned at the beginning of this chapter, a transmission line is used in transfer­
ring power from the source to the load. The average input power at a distance  from the
load is given by an equation similar to eq. (10.78); that is,
Pave 5 1
2 Re3Vs1,2I*s 1,2 4
where the factor  1
2  is needed because we are dealing with the peak values instead of the rms
values. Assuming a lossless line, we substitute eqs. (11.24) and (11.25) to obtain
Pave 5 1
2 RecV1
o 1e jb, 1 Ge2jb,2 V1*
1e2jb, 2 G*e jb,2 d
5 1
2 Rec
0 V1
o 0 2
11 2 0 G 0 2 1 Ge22jb, 2 G*e2jb,2 d
Since the last two terms together become purely imaginary, we have
Pave 5
0 V1
o 0 2
2Zo
11 2 0 G 0 22
(11.40)
| V  |
| V  |
| I  |
βl (radians)
λ (wavelength)
FIGURE 11.7  Voltage and current standing wave patterns on a lossless line terminated
by a resistive load.
11.4 Input Impedance, Standing Wave Ratio, and Power  569
The first term is the incident power Pi, while the second term is the reflected power Pr.
Thus eq. (11.40) may be written as
Pt 5 Pi 2 Pr
where Pt is the input or transmitted power and the negative sign is due to the negative-
going wave (since we take the reference direction as that of the voltage/current traveling
toward the right). We should notice from eq. (11.40) that the power is constant and does
not depend on , since it is a lossless line. Also, we should notice that maximum power is
delivered to the load when G 5 0, as expected.
We now consider special cases when the line is connected to load ZL 5 0, ZL 5 `, and
ZL 5 Zo. These special cases can easily be derived from the general case.
A.  Shorted Line (ZL = 0)
For this case, eq. (11.34) becomes
Zsc 5 Zin`
ZL50
5 jZo tan b,
(11.41a)
Also, from eqs. (11.36) and (11.38)
GL 5 21,  s 5 `
(11.41b)
We notice from eq. (11.41a) that Zin is a pure reactance, which could be capacitive
or  inductive depending on the value of . The variation of Zin with  is shown in
­Figure 11.8(a).
B.  Open-Circuited Line (ZL = `)
In this case, eq. (11.34) becomes
Zoc 5
lim
ZLS`
Zin 5
j tan b, 5 2jZo cot b,
(11.42a)
and from eqs. (11.36) and (11.38),
GL 5 1,  s 5 `
(11.42b)
The variation of Zin with  is shown in Figure 11.8(b). Notice from eqs. (11.41a) and
(11.42a) that
ZscZoc 5 Z2
(11.43)
C.  Matched Line (ZL = Zo)
Zin 5 Zo
(11.44a)
The most desired case from the practical point of view is the matched line i.e., ZL = Zo. For
this case, eq. (11.34) reduces to
570  CHAPTER 11  TRANSMISSION LINES
and from eqs. (11.36) and (11.38),
GL 5 0,  s 5 1
(11.44b)
that is, V2
o 5 0; the whole wave is transmitted, and there is no reflection. The incident
power is fully absorbed by the load. Thus maximum power transfer is possible when a
transmission line is matched to the load.
A certain transmission line 2 m long operating at v 5 106 rad/s has a 5 8 dB/m,
b 5 1 rad/m, and Zo 5 60 1 j40 V. If the line is connected to a source of 10l0° V,
Zg 5 40 V and terminated by a load of 20 1 j50 V, determine
(a)  The input impedance
(b)  The sending-end current
(c)  The current at the middle of the line
FIGURE 11.8  Input impedance of
a lossless line: (a) when shorted,
(b) when open.
EXAMPLE 11.3
11.4 Input Impedance, Standing Wave Ratio, and Power  571
Solution:
(a)	 Since 1 Np 5 8.686 dB,
a 5
8.686 5 0.921 Np/m
g 5 a 1 jb 5 0.921 1 j1 /m
g, 5 210.921 1 j12 5 1.84 1 j2
Using the formula for tanh1x 1 jy2 in Appendix A.3, we obtain
tanh g, 5 1.033 2 j0.03929
Zin 5 Zo aZL 1 Zo tanh g,
Zo 1 ZL tanh g,b
5 160 1 j402 c
20 1 j50 1 160 1 j402 11.033 2 j0.039292
60 1 j40 1 120 1 j502 11.033 2 j0.039292 d
Zin 5 60.25 1 j38.79 V
(b)	 The sending-end current is I1z 5 02 5 Io. From eq. (11.28),
I1z 5 02 5
Zin 1 Zg
60.25 1 j38.79 1 40
5 93.03liii
221.15° mA
(c)	 To find the current at any point, we need V1
o  and V2
o . But
Io 5 I1z 5 02 5 93.03liii
221.15° mA
Vo 5 ZinIo 5 171.66liii
32.77°2 10.09303liii
221.15°2 5 6.667liii
11.62° V
From eq. (11.27),
o 5 1
2 1Vo 1 ZoIo2
5 1
2 36.667liii
11.62° 1 160 1 j402 10.09303liiii
221.15°2 4 5 6.687liii
12.08°
o 5 1
2 1Vo 2 ZoIo2 5 0.0518lii
260°
At the middle of the line, z 5 ,/2, gz 5 0.921 1 j1. Hence, the current at this point is
Is1z 5 ,/22 5 V1
e2gz 2 V2
egz
16.687e j12.08°2e20.9212j1
60 1 j40
10.0518e j260°2e0.9211j1
60 1 j40
572  CHAPTER 11  TRANSMISSION LINES
Note that j1 is in radians and is equivalent to j57.3°. Thus,
Is1z 5 ,/22 5 6.687e j12.08°e20.921e2j57.3°
72.1e j33.69°
2 0.0518e j260°e0.921e j57.3°
72.1e33.69°
5 0.0369e2j78.91° 2 0.001805e j283.61°
5 6.673 2 j34.456 mA
5 35.10lii
281° mA
PRACTICE EXERCISE  11.3
The transmission line shown in Figure 11.9 is 40 m long and has Vg 5 15l 0° Vrms,
(a)  The input impedance Zin
(b)  The sending-end current Iin and voltage Vin
(c)  The propagation constant g
Answer:  (a) 30 1 j60 V,  (b) 0.2236liii
263.43° A, 7.5l0° Vrms, (c) 0.0101 1
j0.02094 /m.
FIGURE 11.9  For Practice Exercise 11.3.
11.5  THE SMITH CHART
Prior to the advent of digital computers and calculators, engineers developed all sorts of aids
(slide rules, tables, charts, graphs, etc.) to facilitate their calculations for design and analysis.
To reduce the tedious manipulations involved in calculating the characteristics of transmis­
sion lines, graphical means were then developed. The Smith chart3 is the most commonly
3Devised by Phillip H. Smith in 1939. See P. H. Smith, “Transmission line calculator,” Electronics, vol. 12, pp. 29–31,
1939, and “An improved transmission line calculator,” Electronics, vol. 17, pp. 130–133, 318–325, 1944.
Zo 5 30 1 j60 V, and VL 5 5lii
248° Vrms. If the line is matched to the load and Zg 5 0,
calculate:
11.5 The Smith Chart  573
used of the graphical techniques. It is basically a graphical indication of the ­impedance of a
transmission line and of the corresponding reflection coefficient as one moves along the line.
It becomes easy to use after a small amount of experience. We will first ­ex­am­ine how the Smith
chart is constructed and later employ it in our calculations of transmission line characteristics
such as GL, s, and Zin. We will assume that the transmission line to which the Smith chart will
be applied is lossless 1Zo 5 Ro2, although this is not fundamentally required.
The Smith chart is constructed within a circle of unit radius 1 0 G 0 # 12 as shown in
Figure 11.10. The construction of the chart is based on the relation in eq. (11.36)4; that is,
G 5 ZL 2 Zo
ZL 1 Zo
(11.45)
G 5 0 G 0 luG
i 5 Gr 1 jGi
(11.46)
where Gr and Gi are the real and imaginary parts of the reflection coefficient G.
Instead of having separate Smith charts for transmission lines with different character­
istic impedances (e.g., Zo 5 60, 100, 120 V), we prefer to have just one that can be used for
any line. We achieve this by using a normalized chart in which all impedances are normalized
with respect to the characteristic impedance Zo of the particular line under ­consideration.
For the load impedance ZL, for example, the normalized impedance zL is given by
zL 5 ZL
5 r 1 jx
(11.47)
Substituting eq. (11.47) into eqs. (11.45) and (11.46) gives
G 5 Gr 1 jGi 5 zL 2 1
zL 1 1
(11.48a)
FIGURE 11.10  Unit circle on which the Smith chart
is constructed.
4 Whenever a subscript is not attached to G, we simply mean voltage reflection coefficient at the load 1GL 5 G2.
574  CHAPTER 11  TRANSMISSION LINES
zL 5 r 1 jx 5
11 1 Gr2 1 jGi
11 2 Gr2 2 jGi
(11.48b)
Normalizing and equating real and imaginary components, we obtain
r 5
1 2 G2
r 2 G2
11 2 Gr2 2 1 G2
(11.49a)
x 5
2 Gi
11 2 Gr2 2 1 G2
(11.49b)
Rearranging terms in eqs. (11.49) leads to
cGr 2
1 1 rd
1 G2
i 5 c
1 1 rd
(11.50)
and
3Gr 2 142 1 cGi 2 1
x d
5 c 1
x d
(11.51)
Each of eqs. (11.50) and (11.51) is similar to
1x 2 h2 2 1 1y 2 k2 2 5 a2
(11.52)
which is the general equation of a circle of radius a, centered at 1h, k2. Thus eq. (11.50) is
an r-circle (resistance circle) with
center at 1Gr, Gi2 5 a
1 1 r, 0b
(11.53a)
radius 5
1 1 r
(11.53b)
TABLE 11.3  Radii and Centers of r-Circles for Typical Values of r
Normalized Resistance (r)
Radius a
1 1 rb
Center a
1 1 r , 0b
1/2
2/3
1/2
1/3
1/6
(0, 0)
(1/3, 0)
(1/2, 0)
(2/3, 0)
(5/6, 0)
(1, 0)
11.5 The Smith Chart  575
For typical values of the normalized resistance r, the corresponding centers and radii of the
r-circles are presented in Table 11.3. Typical examples of the r-circles based on the data in
Table 11.3 are shown in Figure 11.11. Similarly, eq. (11.51) is an x-circle (reactance circle)
with
center at 1Gr, Gi2 5 a1, 1
xb
(11.54a)
radius 5 1
(11.54b)
Table 11.4 presents centers and radii of the x-circles for typical values of x, and Figure 11.12
shows the corresponding plots. Notice that while r is always positive, x can be positive (for
inductive impedance) or negative (for capacitive impedance).
If we superpose the r-circles and x-circles, what we have is the Smith chart shown in
Figure 11.13. On the chart, we locate a normalized impedance z 5 2 1 j, for example, as
the point of intersection of the r 5 2 circle and the x 5 1 circle. This is point P1 in Figure
11.13. Similarly, z 5 1 2 j 0.5 is located at P2, where the r 5 1 circle and the x 5 20.5
circle ­intersect.
Apart from the r- and x-circles (shown on the Smith chart), we can draw the s-circles
or constant standing wave ratio circles (always not shown on the Smith chart), which are
TABLE 11.4  Radii and Centers of x-Circles
for Typical Values of x
Normalized Reactance (x)
Radius a1
Center a1, 1
1/2
1/2
1/5
(1, `)
(1, 2)
(1, 1)
(1, 1/2)
(1, 1/5)
(1, 0)
FIGURE 11.11  Typical r-circles for
r 5 0, 0.5, 1, 2, 5, .
576  CHAPTER 11  TRANSMISSION LINES
FIGURE 11.12  Typical x-circles for
x 5 0, 0.5, 1, 2, 5, .
FIGURE 11.13  Illustration of the r-, x-, and s-circles on the Smith chart.
11.5 The Smith Chart  577
centered at the origin with s varying from 1 to `. The value of the standing wave ratio s is
determined by locating where an s-circle crosses the Gr axis. Typical examples of s-circles
for s 5 1, 2, 3, and ` are shown in Figure 11.13. Since 0 G 0  and s are related according to
eq. (11.38), the s-circles are sometimes referred to as 0 G 0 -circles, with 0 G 0  varying linearly
from 0 to 1 as we move away from the center O toward the periphery of the chart, while s
varies nonlinearly from 1 to `.
The following points should be noted about the Smith chart.
1.	 At point Psc on the chart r 5 0, x 5 0; that is, ZL 5 0 1 j0, showing that Psc repre­
sents a short circuit on the transmission line. At point Poc, r 5 ` and x 5 `, or
ZL 5 ` 1 j`, which implies that Poc corresponds to an open circuit on the line.
Also at Poc, r 5 0 and x 5 0, showing that Poc is another location of a short circuit
on the line.
2.	 A complete revolution (360°) around the Smith chart represents a distance of l/2
on the line. Clockwise movement on the chart is regarded as moving toward the
generator (or away from the load) as shown by the arrow G in Figure 11.14(a) and
(b). Similarly, counterclockwise movement on the chart corresponds to moving
toward the load (or away from the generator) as indicated by the arrow L in Figure
11.14. Notice from Figure 11.14(b) that at the load, moving toward the load does
not make sense (because we are already at the load). The same can be said of the
case when we are at the generator end.
3.	 There are three scales around the periphery of the Smith chart as illustrated in
Figure 11.14(a). The three scales are included for the sake of convenience but they
are actually meant to serve the same purpose; one scale should be sufficient. The
scales are used in determining the distance from the load or generator in degrees
or wavelengths. The outermost scale is used to determine the distance on the line
from the generator end in terms of wavelengths, and the next scale determines the
distance from the load end in terms of wavelengths. The innermost scale is a pro­
tractor (in degrees) and is primarily used in determining G; it can also be used to
determine the distance from the load or generator. Since a l/2 distance on the line
corresponds to a movement of 360° on the chart, l distance on the line corresponds
to a 720° movement on the chart.
 → 720°
(11.55)
Thus we may ignore the other outer scales and use the protractor (the innermost
scale) for all our G and distance calculations.
4.	 The voltage Vmax occurs where Zin, max is located on the chart [see eq. (11.39a)], and
that is on the positive Gr-axis or on OPoc in Figure 11.14(a). The voltage Vmin is located
at the same point where we have Zin, min
on OPsc in Figure 11.14(a). Notice that Vmax and Vmin (or Zin, max and Zin, min) are l/4
(or 180°) apart.
5.	 The Smith chart is used both as impedance chart and admittance chart 1Y 5 1/Z2.
As admittance chart (normalized admittance y 5 Y/Yo 5 g 1 jb2, the g- and
b-circles correspond to r- and x-circles, respectively.
on the chart, that is, on the negative G -axis or
578  CHAPTER 11  TRANSMISSION LINES
Based on these important properties, the Smith chart may be used to determine,
among other things, (a) G 5 0 G 0 luG and s; (b) Zin or Yin; and (c) the locations of Vmax and
Vmin ­provided that we are given Zo, ZL, l, and the length of the line. Some examples will
clearly show how we can find all these and much more with the aid of the Smith chart, a
compass, and a plain straightedge. A complete Smith chart is available in Appendix D. You
may copy this.
load
generator
FIGURE 11.14  (a) Smith chart illustrating scales around the periphery
and movements around the chart. (b) Corresponding movements along
the transmission line.
11.5 The Smith Chart  579
A lossless transmission line with Zo 5 50 V is 30 m long and operates at 2 MHz. The line
is terminated with a load ZL 5 60 1 j40 V. If u 5 0.6c on the line, find
(a)  The reflection coefficient G
(b)  The standing wave ratio s
(c)  The input impedance
Solution:
This problem will be solved with and without using the Smith chart.
Method 1  (without the Smith chart):
(a)	 G 5 ZL 2 Zo
ZL 1 Zo
60 1 j40 2 50
50 1 j40 1 50 5
10 1 j40
110 1 j40
5 0.3523l56º
(b)	 s 5 1 1 0 G 0
1 2 0 G 0 5 1 1 0.3523
1 2 0.3523 5 2.088
(c)	 Since u 5 v/b, or b 5 v/u,
b, 5 v,
u 5 2p12 3 1062 1302
0.613 3 1082
5 2p
3 5 120º
Note that b is the electrical length of the line.
Zin 5 Zo c
ZL 1 jZo tan b,
Zo 1 jZL tan b,d
50160 1 j40 1 j50 tan 120º2
350 1 j160 1 j402 tan 120º4
5016 1 j4 2 j5"32
15 1 4"3 2 j6"32
5 24.01l3.22°
5 23.97 1 j1.35 V
Method 2  (using the Smith chart):
(a)	 Calculate the normalized load impedance
zL 5 ZL
60 1 j40
5 1.2 1 j0.8
Locate zL on the Smith chart of Figure 11.15 at point P, where the r 5 1.2 circle and the
x 5 0.8 circle meet. To get G at zL, extend OP to meet the r 5 0 circle at Q and measure
OP and OQ. Since OQ corresponds to 0 G 0 5 1, then at P,
0 G 0 5 OP
OQ 5 3.2 cm
9.1 cm 5 0.3516
EXAMPLE 11.4
580  CHAPTER 11  TRANSMISSION LINES
Note that OP 5 3.2 cm and OQ 5 9.1 cm were taken from the Smith chart used by the
author; the Smith chart in Figure 11.15 is reduced, but the ratio of OP/OQ remains the same.
uG 5 angle POS 5 56º
Thus
G 5 0.3516 l56º
(b)	 To obtain the standing wave ratio s, draw a circle with radius OP and center at O.
This is the constant s or 0 G 0  circle. Locate point S where the s-circle meets the Gr-axis. [This
is easily shown by setting Gi 5 0 in eq. (11.49a).] The value of r at this point is s; that is,
s 5 r1for r $ 12
5 2.1
FIGURE 11.15  Smith chart for Example 11.4.
Angle  is read directly on the chart as the angle between OS and OP; that is,
11.5 The Smith Chart  581
(c)	 To obtain Zin, first express  in terms of l or in degrees:
l 5 u
f 5 0.613 3 1082
2 3 106
5 90 m
, 5 30 m 5 30
90 l 5 l
3 S  720º
5 240º
Since l corresponds to an angular movement of 720° on the chart, the length of the line
corresponds to an angular movement of 240°. That means we move toward the generator
(or away from the load, in the clockwise direction) 240° on the s-circle from point P to
point G. At G, we obtain
zin 5 0.47 1 j0.03
Hence
Zin 5 Zozin 5 5010.47 1 j0.032 5 23.5 1 j1.5 V
Although the results obtained using the Smith chart are only approximate, for engineering
purposes they are close enough to the exact ones obtained by Method 1. However, an inex­
pensive modern calculator can handle the complex algebra in less time and with much less
effort than are needed to use the Smith chart. The value of the Smith chart is that it allows
us to observe the variation of Z­in with .
PRACTICE EXERCISE  11.4
A 70  lossless line has s 5 1.6 and uG 5 300°. If the line is 0.6l long, obtain
(a)  G, ZL, Zin
(b)  The distance of the first minimum voltage from the load
A load of 100 1 j150 V is connected to a 75  lossless line. Find:
(a)  G
(b)  s
(c)  The load admittance YL
(d)  Zin at 0.4l from the load
(e)  The locations of Vmax and Vmin with respect to the load if the line is 0.6l long
(f)  Zin at the generator.
Solution:
(a)	 We can use the Smith chart to solve this problem. The normalized load impedance is
zL 5 ZL
100 1 j150
5 1.33 1 j2
EXAMPLE 11.5
Answer:  (a) 0.228 l300º
ii , 80.5 2 j33.6 V, 47.6 2 j17.5 V, (b)
/6.
582  CHAPTER 11  TRANSMISSION LINES
We locate this at point P on the Smith chart of Figure 11.16. At P, we obtain
0 G 0 5 OP
OQ 5 6 cm
9.1 cm 5 0.659
uG 5 angle POS 5 40º
Hence,
G 5 0.659 l40º
Check:
G 5 ZL 2 Zo
ZL 1 Zo
100 1 j150 2 75
100 1 j150 1 75
5 0.6598 /——
39.94°
FIGURE 11.16  Smith chart for Example 11.5.
11.5 The Smith Chart  583
(b)	 Draw the constant s-circle passing through P and obtain
s 5 4.82
Check:
s 5 1 1 0 G 0
1 2 0 G 0 5 1 1 0.659
1 2 0.659 5 4.865
(c)	 To obtain YL, extend PO to POP and note point P where the constant s-circle meets
POP. At P, obtain
yL 5 0.228 2 j0.35
The load admittance is
YL 5 YoyL 5 1
75 10.228 2 j0.352 5 3.04 2 j4.67 mS
Check:
YL 5 1
100 1 j150 5 3.07 2 j4.62 mS
(d)	 The 0.4l corresponds to an angular movement of 0.4 3 720º 5 288º on the constant
s-circle. From P, we move 288° toward the generator (clockwise) on the s-circle to reach
point R. At R,
zin 5 0.3 1 j0.63
Hence
Zin 5 Zozin 5 7510.3 1 j0.632
5 22.5 1 j47.25 V
Check:
b, 5 2p
l 10.4l2 5 360° 10.42 5 144°
Zin 5 Zo c
ZL 1 jZo tan b,
Zo 1 jZL tan b,d
751100 1 j150 1 j75 tan 144°2
375 1 j1100 1 j1502 tan 144°4
5 54.41l65.25
584  CHAPTER 11  TRANSMISSION LINES
Zin 5 21.9 1 j47.6 V
(e)	 The 0.6l corresponds to an angular movement of
0.6 3 720º 5 432º 5 1 revolution 1 72º
Thus, we start from P (load end), move clockwise along the s-circle 432°, or one revolution
plus 72°, and reach the generator at point G. Note that to reach G from P, we have passed
through point T (location of Vmin) once and point S (location of Vmax) twice. Thus, from
the load,
1st Vmax is located at 40º
720º l 5 0.055l
2nd Vmax is located at 0.0555l 1 l
2 5 0.555l
and the only Vmin is located at 0.055l 1 l/4 5 0.3055l
(f)	 At G (generator end),
zin 5 1.8 2 j2.2
Zin 5 7511.8 2 j2.22 5 135 2 j165 V
This can be checked by using eq. (11.34), where b, 5 2p
l  10.6l2 5 216°.
We can see how much time and effort are saved by using the Smith chart.
PRACTICE EXERCISE  11.5
A lossless 60 V line is terminated by a load of 60 1 j60 V.
(a)  Find G and s. If Zin 5 120 2 j60 V, how far (in terms of wavelengths) is the load
from the generator? Solve this without using the Smith chart.
(b)  Use the Smith chart to solve the problem in part (a). Calculate Zmax and Zin, min. How
far (in terms of l) is the first maximum voltage from the load?
Answer:  (a) 0.4472 /——
63.43°, 2.618, l
8 11 1 4n2, n 5 0, 1, 2, . . . , (b) 0.4457 /—
62°,
2.612, l
8 11 1 4n2, 157.1 V, 22.92 V, 0.0861 l.
11.6 Some Applications of Transmission Lines  585
Transmission lines are used to serve different purposes. Here we consider how transmis­
sion lines are used for load matching and impedance measurements.
A.  Quarter-Wave Transformer (Matching)
When Zo 2 ZL, we say that the load is mismatched and a reflected wave exists on the line.
However, for maximum power transfer, it is desired that the load be matched to the trans­
mission line 1Zo 5 ZL2 so that there is no reflection 1 0 G 0 5 0 or s 5 12. The matching is
achieved by using shorted sections of transmission lines.
We recall from eq. (11.34) that when , 5 l/4 or b, 5 12p/l2 1l/42 5 p/2,
Zin 5 Zo c
ZL 1 jZo tan p/2
Zo 1 jZL tan p/2 d 5 Z2
(11.56)
that is,
Zin
5 Zo
zin 5 1
S  yin 5 zL
(11.57)
Thus by adding a l/4 line on the Smith chart, we obtain the input admittance correspond­
ing to a given load impedance.
Also, a mismatched load ZL can be properly matched to a line (with characteristic
impedance Zo) by inserting prior to the load a transmission line l/4 long (with character­
istic impedance Z or) as shown in Figure 11.17. The l/4 section of the transmission line is
called a quarter-wave transformer because it is used for impedance matching like an ordi­
nary transformer. From eq. (11.56), Zro is selected such that 1Zin 5 Zo2
Zro 5 "ZoZL
(11.58)
11.6  SOME APPLICATIONS OF TRANSMISSION LINES
FIGURE 11.17  Load matching using a l/4 ­transformer.
586  CHAPTER 11  TRANSMISSION LINES
where Zro, Zo and ZL are all real. If, for example, a 120 V load is to be matched to a 75 V line,
the quarter-wave transformer must have a characteristic impedance of !1752 11202 .
95 V. This 95 V quarter-wave transformer will also match a 75 V load to a 120 V line. The
voltage standing wave patterns without and with the l/4 transformer are shown in Figure
11.18(a) and (b), respectively. From Figure 11.18, we observe that although a standing wave
still exists between the transformer and the load, there is no standing wave to the left of the
transformer due to the matching. However, the reflected wave (or standing wave) is elimi­
nated only at the desired wavelength (or frequency f ); there will be reflection at a slightly
different wavelength. Thus, the main disadvantage of the quarter-wave transformer is that
it is a narrow-band or frequency-sensitive device.
B.  Single-Stub Tuner (Matching)
The major drawback of using a quarter-wave transformer as a line-matching device is
eliminated by using a single-stub tuner. The tuner consists of an open or shorted section of
transmission line of length d connected in parallel with the main line at some distance  from
the load, as in Figure 11.19. Notice that the stub has the same characteristic impedance as the
main line, although stubs may be designed with different values of Zo. It is more difficult to
use a series stub although it is theoretically feasible. An open-circuited stub radiates some
energy at high frequencies. Consequently, shunt short-circuited parallel stubs are preferred.
Since we intend that Zin 5 Zo, that is, zin 5 1 or yin 5 1 at point A on the line, we first
draw the locus y 5 1 1 jb1r 5 1 circle2 on the Smith chart as shown in Figure 11.20. If a
shunt stub of admittance ys 5 2jb is introduced at A, then
yin 5 1 1 jb 1 ys 5 1 1 jb 2 jb 5 1 1 j0
(11.59)
FIGURE 11.18  Voltage standing
wave pattern of mismatched load:
(a) with­out a l/4 transformer,
(b) with a l/4 transformer.
FIGURE 11.19  Matching with a single-stub tuner.
11.6 Some Applications of Transmission Lines  587
as desired. Since b could be positive or negative, two possible values of ,1,l/22 can be
found on the line. At A, ys 5 2jb, , 5 ,A and at B, ys 5 jb, , 5 ,B as in Figure 11.20.
Because the stub is shorted 1yrL 5 `2, we determine the length d of the stub by finding the
distance from Psc (at which zrL 5 0 1 j0) to the required stub admittance ys. For the stub
at A, we obtain d 5 dA as the distance from Psc to A, where A corresponds to ys 5 2jb
located on the periphery of the chart as in Figure 11.20. Similarly, we obtain d 5 dB as the
distance from Psc to B1ys 5 jb2.
Thus we obtain d 5 dA and d 5 dB, corresponding to A and B, respectively, as shown
in Figure 11.20. Note that dA 1 dB 5 l/2 always. Since we have two possible shunted stubs,
we normally choose to match the shorter stub or one at a position closer to the load. Instead
of having a single stub shunted across the line, we may have two stubs. This arrangement,
which is called double-stub matching, allows for the adjustment of the load impedance.
C.  Slotted Line (Impedance Measurement)
At high frequencies, it is very difficult to measure current and voltage because measuring
devices become significant in size and every circuit becomes a transmission line. The slot­
ted line is a simple device used in determining the impedance of an unknown load at high
frequencies up into the region of gigahertz. It consists of a section of an air (lossless) line
with a slot in the outer conductor as shown in Figure 11.21. The line has a probe, along the
E field (see Figure 11.4), which samples the E field and consequently measures the potential
difference between the probe and its outer shield.
The slotted line is primarily used in conjunction with the Smith chart to determine
the standing wave ratio s (the ratio of maximum voltage to the minimum voltage) and
the load impedance ZL. The value of s is read directly on the detection meter when the
load is connected. To determine ZL, we first replace the load by a short circuit and note
the locations of voltage minima (which are more accurately determined than the maxima
because of the sharpness of the turning point) on the scale. Since impedances repeat every
half-wavelength, any of the minima may be selected as the load reference point. We now
determine the distance from the selected reference point to the load by replacing the short
circuit by the load and noting the locations of voltage minima. The distance  (distance of
Psc
FIGURE 11.20  Using the Smith chart
to determine  and d of a shunt-shorted
single-stub tuner.
588  CHAPTER 11  TRANSMISSION LINES
Vmin toward the load) expressed in terms of l is used to locate the position of the load of
an s-circle on the chart as shown in Figure 11.22.
The procedure for using the slotted line can be summarized as follows.
1.	 With the load connected, read s on the detection meter. With the value of s, draw
the s-circle on the Smith chart.
2.	 With the load replaced by a short circuit, locate a reference position for ZL at a
­voltage minimum point.
3.	 With the load on the line, note the position of Vmin and determine .
4.	 On the Smith chart, move toward the load a distance  from the location of Vmin.
Find ZL at that point.
To ge
FIGURE 11.21  (a) Typical slotted line; (b) Determining the location of
the load ZL and Vmin on the line.
s-C
load
FIGURE 11.22  Determining the load imped­
ance from the Smith chart by using the data
obtained from the slotted line.
11.6 Some Applications of Transmission Lines  589
With an unknown load connected to a slotted air line, s 5 2 is recorded by a standing wave
replaced by a short circuit, the minima are at 16 cm, 24 cm, .  .  .  . If Zo 5 50 V, calculate
l, f, and ZL.
Solution:
Consider the standing wave patterns as in Figure 11.23(a). From this, we observe that
2 5 19 2 11 5 8 cm  or   5 16 cm
f 5 u
l 5
3 3 108
16 3 1022 5 1.875 GHz
Electrically speaking, the load can be located at 16 cm or 24 cm. If we assume that the load
is at 24 cm, the load is at a distance  from Vmin, where
, 5 24 2 19 5 5 cm 5 5
16 l 5 0.3125 l
FIGURE 11.23  Determining ZL by
using the slotted line: (a) wave
­pattern, (b) Smith chart for
Example 11.6.
EXAMPLE 11.6
indicator, and minima are found at 11 cm, 19 cm, . . . , on the scale. When the load is
590  CHAPTER 11  TRANSMISSION LINES
This corresponds to an angular movement of 0.3125 3 720° 5 225° on the s 5 2 circle.
By starting at the location of Vmin and moving 225° toward the load (counterclockwise), we
reach the location of zL as illustrated in Figure 11.23(b). Thus
zL 5 1.4 1 j0.75
and
ZL 5 ZozL 5 5011.4 1 j0.752 5 70 1 j37.5 V
PRACTICE EXERCISE  11.6
The following measurements were taken by means of the slotted line technique: with
load, s 5 1.8, Vmax occurred at 23 cm, 33.5 cm, .  .  . ; with short, s 5 `, Vmax occurred
at 25 cm, 37.5 cm, .  .  .  . If Zo 5 50 V, determine ZL.
Answer:  32.5 2 j17.5 V.
An antenna with an impedance of 40 1 j30 V is to be matched to a 100 V lossless line with
a shorted stub. Determine
(a)  The required stub admittance
(b)  The distance between the stub and the antenna
(c)  The stub length
(d)  The standing wave ratio on each segment of the system
Solution:
(a)	 zL 5 ZL
40 1 j30
100
5 0.4 1 j0.3
Locate zL on the Smith chart as in Figure 11.24 and from this draw the s-circle so that yL
can be located diametrically opposite zL. Thus yL 5 1.6 2 j1.2. Alternatively, we may find
yL by using
yL 5 Zo
100
40 1 j30 5 1.6 2 j1.2
Locate points A and B where the s-circle intersects the g 5 1 circle. At A, ys 5 2j1.04 and
at B, ys 5 1j1.04. Thus the required stub admittance is
Ys 5 Yoys 5 6j1.04 1
100 5 6j10.4 mS
Both j10.4 mS and 2j10.4 mS are possible values.
EXAMPLE 11.7
11.6 Some Applications of Transmission Lines  591
(b)	 From Figure 11.24, we determine the distance between the load (antenna in this case)
yL and the stub. At A,
,A 5 l
2 2
162° 2 239°2l
720°
5 0.36l
and at B:
,B 5
162° 2 39°2l
720°
5 0.032l
FIGURE 11.24  Smith chart for Example 11.7.
592  CHAPTER 11  TRANSMISSION LINES
(c)	 Locate points A and B corresponding to stub admittance 2j1.04 and j1.04, respec­
tively. Determine the stub length (distance from Psc to A and B):
dA 5 88°
720° l 5 0.1222l
dB 5 272°
720°l 5 0.3778l
Notice that dA 1 dB 5 0.5l as expected.
(d)	 From Figure 11.24, s 5 2.7. This is the standing wave ratio on the line segment
between the stub and the load (see Figure 11.18); s 5 1 to the left of the stub because the
line is matched, and s 5 ` along the stub because the stub is shorted.
PRACTICE EXERCISE  11.7
A 75 V lossless line is to be matched to a load of 100 2 j80  with a shorted stub.
Calculate the stub length, its distance from the load, and the necessary stub admit­
tance.
Answer:  ,A 5 0.093l, ,B 5 0.272l, dA 5 0.126l, dB 5 0.374l, 6j12.67 mS.
†11.7  TRANSIENTS ON TRANSMISSION LINES
In our discussion so far, we have assumed that a transmission line operates at a single fre­
quency. In computer networks and in certain other practical applications, pulsed signals
may be sent through the line. From Fourier analysis, a pulse can be regarded as a super­
position of waves of many frequencies. Thus, sending a pulsed signal on the line may be
regarded as the same as simultaneously sending waves of different frequencies.
As in circuit analysis, when a pulse generator or battery connected to a transmission
line is switched on, it takes some time for the current and voltage on the line to reach steady
values. This transitional period is called the transient. The transient behavior just after clos­
ing the switch (or due to lightning strokes) is usually analyzed in the frequency domain by
using Laplace transformation. For the sake of convenience, we treat the problem in the time
domain.
Consider a lossless line of length  and characteristic impedance Zo as shown in Figure
11.25(a). Suppose that the line is driven by a pulse generator of voltage Vg with internal
impedance Zg at z 5 0 and terminated with a purely resistive load ZL. At the instant t 5 0
that the switch is closed, the starting current “sees” only Zg and Zo, so the initial situation
can be described by the equivalent circuit of Figure 11.25(b). From the figure, the starting
current at z 5 0, t 5 01 is given by
I10, 012 5 Io 5
Zg 1 Zo
(11.60)
11.7 Transients on Transmission Lines  593
and the initial voltage is
V10, 012 5 Vo 5 IoZo 5
Zg 1 Zo
Vg
(11.61)
After the switch is closed, waves I1 5 Io and V1 5 Vo propagate toward the load at the
speed
u 5
"LC
(11.62)
Since this speed is finite, it takes some time for the waves traveling in the positive direction
to reach the load and interact with it. The presence of the load has no effect on the waves
before the transit time given by
t1 5 ,
(11.63)
After t1 seconds, the waves reach the load. The voltage (or current) at the load is the sum
of the incident and reflected voltages (or currents). Thus
V1,, t12 5 V1 1 V2 5 Vo 1 GLVo 5 11 1 GL2Vo
(11.64)
and
I1,, t12 5 I1 1 I2 5 Io 2 GLIo 5 11 2 GL2Io
(11.65)
where GL is the load reflection coefficient given in eq. (11.36); that is,
GL 5 ZL 2 Zo
ZL 1 Zo
(11.66)
The reflected waves V2 5 GLVo and I2 5 2GLIo travel back toward the generator in addi-
tion to the waves Vo and Io already on the line. At time t 5 2t1, the reflected waves have
reached the generator, so
V10, 2t12 5 V1 1 V2 5 GGGLVo 1 11 1 GL2Vo
FIGURE 11.25  Transients on a transmission line: (a) a line driven
by a pulse generator, (b) the equivalent circuit at z 5 0, t 5 01.
594  CHAPTER 11  TRANSMISSION LINES
V10, 2t12 5 11 1 GL 1 GGGL2Vo
(11.67)
and
I10, 2t12 5 I1 1 I2 5 2GG12GLIo2 1 11 2 GL2Io
I10, 2t12 5 11 2 GL 1 GLGG2Io
(11.68)
where GG is the generator reflection coefficient given by
GG 5
Zg 2 Zo
Zg 1 Zo
(11.69)
Again the reflected waves (from the generator end) V1 5 GGGLVo and I1 5 GGGLIo propa­
absorbed by the resistors Zg and ZL.
Instead of tracing the voltage and current waves back and forth, it is easier to keep track of the
reflections using a bounce diagram, otherwise known as a lattice diagram. The bounce diagram
consists of a zigzag line indicating the position of the voltage (or current) wave with respect to
the generator end, as shown in Figure 11.26. On the bounce diagram, the voltage (or current) at
any time may be determined by adding those values that appear on the diagram above that time.
For the transmission line of Figure 11.27, calculate and sketch
(a)  The voltage at the load and generator ends for 0 , t , 6 ms
(b)  The current at the load and generator ends for 0 , t , 6 ms
FIGURE 11.26  Bounce diagram for (a) a voltage wave and
(b) a current wave.
EXAMPLE 11.8
gate toward the load, and the process continues until the energy of the pulse is actually
11.7 Transients on Transmission Lines  595
Solution:
(a)	 We first calculate the voltage reflection coefficients at the generator and load ends:
GG 5
Zg 2 Zo
Zg 1 Zo
5 100 2 50
100 1 50 5 1
GL 5 ZL 2 Zo
ZL 1 Zo
5 200 2 50
200 1 50 5 3
The transit time t1 5 ,
u 5 100
108 5 1 ms.
The initial voltage at the generator end is
Vo 5
Zo 1 Zg
Vg 5 50
150 1122 5 4 V
The 4 V is sent out to the load. The leading edge of the pulse arrives at the load at t 5 t1 5
1 ms. A portion of it, 413/52 5 2.4 V, is reflected back and reaches the generator at t 5
2t1 5 2 ms. At the generator, 2.411/32 5 0.8 is reflected and the process continues. The
whole process is best illustrated in the voltage bounce diagram of Figure 11.28.
FIGURE 11.27  For Example 11.8.
FIGURE 11.28  Voltage bounce diagram for Example 11.8.
596  CHAPTER 11  TRANSMISSION LINES
From the bounce diagram, we can sketch V10, t2 and V1,, t2 as functions of time as
shown in Figure 11.29. Notice from Figure 11.29 that as t S  `, the voltages approach an
asymptotic value of
V` 5
ZL 1 Zg
Vg 5 200
300 1122 5 8 V
This should be expected because the equivalent circuits at t 5 0 and t 5 ` are as shown
in Figure 11.30.
(b)	 The current reflection coefficients at the generator and load ends are 2GG 5 21/3
and 2GL 5 23/5, respectively. The initial current is
Io 5 Vo
5 4
50 5 80 mA
FIGURE 11.29  Voltage (not to
scale) for Example 11.8: (a) at
the generator end, (b) at the
load end.
11.7 Transients on Transmission Lines  597
Again, I10, t2 and I1,, t2 are easily obtained from the current bounce diagram shown in
­Figure 11.31. These currents are sketched in Figure 11.32. Note that I1,, t2 5 V1,, t2/ZL.
Hence, Figure 11.32(b) can be obtained either from the current bounce diagram of
Figure  11.31 or by scaling Figure 11.29(b) by a factor of 1/ZL 5 1/200. Notice from
Figures 11.30(b) and 11.32 that the currents approach an asymptotic value of
I` 5
Zg 1 ZL
5 12
300 5 40 mA
FIGURE 11.30  Equivalent circuits for the line in Figure 11.27 for (a) t 5 0
and (b) t 5 `.
FIGURE 11.31  Current bounce diagram for Example 11.8.
598  CHAPTER 11  TRANSMISSION LINES
PRACTICE EXERCISE  11.8
Repeat Example 11.8 if the transmission line is
(a)  Short-circuited
(b)  Open-circuited
Answer:  (a) See Figure 11.33, (b) See Figure 11.34.
FIGURE 11.32  Current (not to
scale) for Example 11.8: (a) at the
generator end, (b) at the load end.
11.7 Transients on Transmission Lines  599
0 V
4 V
FIGURE 11.33  For Practice Exercise 11.8(a).
600  CHAPTER 11  TRANSMISSION LINES
12 V
12 V
8 V
4 V
4 V
4 V
0 A
FIGURE 11.34  For Practice Exercise 11.8(b).
11.7 Transients on Transmission Lines  601
A 75 V transmission line of length 60 m is terminated by a 100 V load. If a rectangular
pulse of width 5 ms and magnitude 4 V is sent out by the generator connected to the line,
sketch I10, t2 and I1,, t2 for 0 , t , 15 ms. Take Zg 5 25 V and u 5 0.1c.
Solution:
In the previous example, the switching on of a battery created a step function, a pulse of
infinite width. In this example, the pulse is of finite width of 5 ms. We first calculate the
voltage reflection coefficients:
The initial voltage and transit time are given by
Vo 5
Zo 1 Zg
Vg 5 75
100 142 5 3 V
t1 5 ,
u 5
0.1 13 3 1082 5 2 ms
The time taken by Vo to go forth and back is 2t1 5 4 ms, which is less than the pulse dura­
tion of 5 ms. Hence, there will be overlapping.
The current reflection coefficients are
2GL 5 21
7  and  2GG 5 1
The initial current Io 5
Zg 1 Zo
100 5 40 mA.
Let i and r denote incident and reflected pulses, respectively. At the generator end:
0 , t , 5 ms,
Ir 5 Io 5 40 mA
4 , t , 9,
Ii 5 21
7 1402 5 25.714
Ir 5 1
2 125.7142 5 22.857
8 , t , 13,
Ii 5 21
7 122.8572 5 0.4082
Ir 5 1
2 10.40822 5 0.2041
EXAMPLE 11.9
GG 5 Zg 2 Zo
Zg 1 Zo
5 25 2 75
25 1 75 5 21
GL 5 ZL 2 Zo
ZL 1 Zo
5 100 2 75
100 1 75 5 1
602  CHAPTER 11  TRANSMISSION LINES
12 , t , 17,
Ii 5 21
7 10.20412 5 20.0292
Ir 5 1
2 120.02922 5 20.0146
and so on. Hence, the plot of I10, t2 versus t is as shown in Figure 11.35(a).
FIGURE 11.35  For Example 11.9 (not to scale).

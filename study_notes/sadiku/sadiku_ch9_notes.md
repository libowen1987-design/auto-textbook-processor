# Sadiku《Elements of Electromagnetics》Chapter 9

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 448-497 of 926 (926 total)

---

## Maxwell's Equations

421
C H A P T E R
421
9.1  INTRODUCTION
In Part 2 (Chapters 4–6) of this text, we mainly concentrated our efforts on electrostatic
fields denoted by E1x, y, z2; Part 3 (Chapters 7 and 8) was devoted to magnetostatic fields
represented by H1x, y, z2. We have therefore restricted our discussions to static, or time-
invariant, EM fields. Henceforth, we shall examine situations in which electric and mag­
netic fields are dynamic, or time varying. It should be mentioned first that in static EM
fields, electric and magnetic fields are independent of each other, whereas in dynamic
EM fields, the two fields are interdependent. In other words, a time-varying electric field
necessarily involves a corresponding time-varying magnetic field. Second, time-varying
EM fields, represented by E1x, y, z, t2 and H1x, y, z, t2, are of more practical value than
static EM fields. However, familiarity with static fields provides a good background for
understanding dynamic fields. Third, recall that electrostatic fields are usually produced by
static electric charges, whereas magnetostatic fields are due to motion of electric charges
with uniform velocity (direct current) or static magnetic charges (magnetic poles); time-
varying fields or waves are usually due to accelerated charges or time-varying currents such
as shown in Figure 9.1. Any pulsating current will produce radiation (time-varying fields).
It is worth noting that pulsating current of the type shown in Figure 9.1(b) is the cause of
­radiated emission in digital logic boards. In summary:
stationary charges
→ electrostatic fields
steady currents
→ magnetostatic fields
time-varying currents	 → electromagnetic fields (or waves)
Our aim in this chapter is to lay a firm foundation for our subsequent studies. This
will involve introducing two major concepts: (1) electromotive force based on Faraday’s
experiments and (2) displacement current, which resulted from Maxwell’s hypothesis.
As a result of these concepts, Maxwell’s equations as presented in Section 7.6 and the
boundary conditions for static EM fields will be modified to account for the time variation
of the fields. Maxwell’s equations, which summarize the laws of electromagnetism, shall be
MAXWELL’S EQUATIONS
Some people make enemies instead of friends because it is less trouble.
—E. C. MCKENZIE
422  CHAPTER 9  MAXWELL’S EQUATIONS
the basis of our discussions in the remaining part of the text. For this reason, Section 9.5
should be regarded as the heart of this text.
9.2  FARADAY’S LAW
After Oersted’s experimental discovery (upon which Biot–Savart and Ampère based their
laws) that a steady current produces a magnetic field, it seemed logical to find out whether
magnetism would produce electricity. In 1831, about 11 years after Oersted’s discovery,
Michael Faraday in London and Joseph Henry in New York discovered that a time-varying
magnetic field would produce an electric current.1
According to Faraday’s experiments, a static magnetic field produces no current flow;
but in a closed circuit, a time-varying field produces an induced voltage (called electromo­
tive force or simply emf) that causes a flow of current.
Faraday discovered that the induced emf, Vemf
equal to the time rate of change of the magnetic flux linkage by the circuit.
This is called Faraday’s law, and it can be expressed as
where l 5 N is the flux linkage, N is the number of turns in the circuit, and  is the flux
through each turn. The negative sign shows that the induced voltage acts in such a way as
FIGURE 9.1  Examples of time-varying current: (a) sinusoidal,
(b) rectangular, (c) triangular.
1 For details on the experiments of Michael Faraday (1791–1867) and Joseph Henry (1797–1878), see W. F. Magie,
A Source Book in Physics. Cambridge, MA: Harvard Univ. Press, 1963, pp. 472–519.
Vemf 5 2dl
dt 5 2N d
(9.1)
(in volts) in any closed circuit is
9.2 Faraday’s Law  423
to oppose the flux producing it. This behavior is described as Lenz’s law2. Lenz’s law states
Recall that we described an electric field as one in which electric charges experience
force. The electric fields considered so far are caused by electric charges; in such fields,
the flux lines begin and end on the charges. However, electric fields of other kinds are not
directly caused by electric charges. These are emf-produced fields. Sources of emf include
electric generators, batteries, thermocouples, fuel cells, and photovoltaic cells, which all
convert nonelectrical energy into electrical energy.
Consider the electric circuit of Figure 9.2, where the battery is a source of emf. The
electrochemical action of the battery results in an emf-produced field Ef. Due to the accu­
mulation of charge at the battery terminals, an electrostatic field Ee 1 5 2=V 2 also exists.
The total electric field at any point is
E 5 Ef 1 Ee
(9.2)
Note that Ef is zero outside the battery, Ef and Ee have opposite directions in the battery,
and the direction of Ee inside the battery is opposite to that outside it. If we integrate
eq. (9.2) over the closed circuit, we have
E # dl 5 C
Ef # dl 1 0 5 3
Ef # dl  1through battery2
(9.3a)
where A Ee # dl 5 0 because Ee is conservative. The emf of the battery is the line integral
of the emf-produced field, that is,
Vemf 5 3
Ef # dl 5 23
Ee # dl 5 IR
(9.3b)
since Ef and Ee are equal but opposite within the battery (see Figure 9.2). It may also be
regarded as the potential difference 1VP 2 VN2 between the battery’s open-circuit termi­
nals. It is important to note the following facts.
1.	 An electrostatic field Ee cannot maintain a steady current in a closed circuit, since
AL Ee # dl 5 0 5 IR.
2.	 An emf-produced field Ef is nonconservative.
3.	 Except in electrostatics, voltage and potential difference are usually not equivalent.
FIGURE 9.2  A circuit showing emf-producing field Ef
and electrostatic field Ee.
2After Heinrich Friedrich Emil Lenz (1804–1865), a Russian professor of physics.
the direction of current flow in the circuit is such that the induced magnetic field produced
by the induced current opposes change in the original magnetic field.
424  CHAPTER 9  MAXWELL’S EQUATIONS
9.3  TRANSFORMER AND MOTIONAL ELECTROMOTIVE FORCES
Having considered the connection between emf and electric field, we may examine how
Faraday’s law links electric and magnetic fields. For a circuit with a single turn 1N 5 12,
eq. (9.1) becomes
Vemf 5 2 dt 
(9.4)
In terms of E and B, eq. (9.4) can be written as
Vemf 5 C
E # dl 5 2 d
dt 3
B # dS
(9.5)
eS B # dS and S is the surface area of the circuit bounded by
the closed path L. It is clear from eq. (9.5) that in a time-varying situation, both electric
and magnetic fields are present and are interrelated. Note that dl and dS in eq. (9.5) are in
accordance with the right-hand rule as well as Stokes’s theorem. This should be observed
in Figure 9.3. The variation of flux with time as in eq. (9.1) or eq. (9.5) may be caused in
three ways:
1.	 By having a stationary loop in a time-varying B field
2.	 By having a time-varying loop area in a static B field
3.	 By having a time-varying loop area in a time-varying B field
Each of these will be considered separately.
A.  Stationary Loop in Time-Varying B Field (Transformer emf)
In Figure 9.3 a stationary conducting loop is in a time-varying magnetic B field.
Equation (9.5) becomes
Vemf 5 C
E # dl 5 23
# dS
(9.6)
FIGURE 9.3  Induced emf due to a stationary loop in a time-
varying B field.
where  has been replaced by
9.3 Transformer and Motional Electromotive Forces  425
This emf induced by the time-varying current (producing the time-varying B field) in a
­stationary loop is often referred to as transformer emf in power analysis, since it is due
to transformer action. By applying Stokes’s theorem to the middle term in eq. (9.6), we
­obtain
1= 3 E2 # dS 5 23
# dS
(9.7)
For the two integrals to be equal, their integrands must be equal; that is,
= 3 E 5 2'B
't 
(9.8)
This is one of the Maxwell’s equations for time-varying fields. It shows that the time-­
varying E field is not conservative 1= 3 E 2 02. This does not imply that the principles
of energy conservation are violated. The work done in taking a charge about a closed path
in a time-varying electric field, for example, is due to the energy from the time-varying
magnetic field. Observe that Figure 9.3 obeys Lenz’s law: the induced current I flows such
as to produce a magnetic field that opposes the change in B(t).
B.  Moving Loop in Static B Field (Motional emf)
When a conducting loop is moving in a static B field, an emf is induced in the loop. We
recall from eq. (8.2) that the force on a charge moving with uniform velocity u in a mag­
netic field B is
Fm 5 Qu 3 B
(8.2)
We define the motional electric field Em as
Em 5 Fm
Q 5 u 3 B
(9.9)
If we consider a conducting loop, moving with uniform velocity u as consisting of a large
number of free electrons, the emf induced in the loop is
Vemf 5 C
Em # dl 5 C
1u 3 B2 # dl
(9.10)
This type of emf is called motional emf or flux-cutting emf because it is due to motional
action. It is the kind of emf found in electrical machines such as motors, generators, and
alternators. Figure 9.4 illustrates a two-pole dc machine with one armature coil and a two-
bar commutator. Although the analysis of the dc machine is beyond the scope of this text,
we can see that voltage is generated as the coil rotates within the magnetic field. Another
426  CHAPTER 9  MAXWELL’S EQUATIONS
­example of motional emf is illustrated in Figure 9.5, where a rod is moving between a
pair of rails. In this example, B and u are perpendicular, so eq. (9.9) in conjunction with
eq. (8.2) becomes
Fm 5 I, 3 B
(9.11)
Fm 5 I,B
(9.12)
and eq. (9.10) becomes
Vemf 5 uB,
(9.13)
By applying Stokes’s theorem to eq. (9.10), we have
1= 3 Em2 # dS 5 3
= 3 1u 3 B2 # dS
= 3 Em 5 = 3 1u 3 B2
(9.14)
Notice that unlike eq. (9.6), there is no need for a minus sign in eq. (9.10) because Lenz’s
law is already accounted for.
FIGURE 9.4  A direct-current machine.
FIGURE 9.5  Induced emf due to a moving
loop in a static B field.
9.3 Transformer and Motional Electromotive Forces  427
To apply eq. (9.10) is not always easy; some care must be exercised. The following
points should be noted.
1.	 The integral in eq. (9.10) is zero along the portion of the loop where u 5 0. Thus
dl is taken along the portion of the loop that is cutting the field (along the rod in
Figure 9.5), where u has nonzero value.
2.	 The direction of the induced current is the same as that of Em or u 3 B. The limits
of the integral in eq. (9.10) are selected in the direction opposite to the induced
­current, thereby satisfying Lenz’s law. In Figure 9.5, for example, the integration
over L is along 2ay, whereas induced current flows in the rod along ay.
C.  Moving Loop in Time-Varying Field
In the general case, a moving conducting loop is in a time-varying magnetic field. Both
transformer emf and motional emf are present. Combining eqs. (9.6) and (9.10) gives the
total emf as
Vemf 5 C
E # dl 5 23
# dS 1 C
1u 3 B2 # dl
(9.15)
or from eqs. (9.8) and (9.14),
= 3 E 5 2'B
't 1 = 3 1u 3 B2 
(9.16)
Note that eq. (9.15) is equivalent to eq. (9.4), so Vemf can be found using either eq. (9.15) or
(9.4). In fact, eq. (9.4) can always be applied in place of eqs. (9.6), (9.10), and (915).
A conducting bar can slide freely over two conducting rails as shown in Figure 9.6.
Calculate the induced voltage in the bar
(a)  If the bar is stationed at y 5 8 cm and B 5 4 cos 106taz mWb/m2
(b)  If the bar slides at a velocity u 5 20ay m/s and B 5 4az mWb/m2
(c)  If the bar slides at a velocity u 5 20ay m/s and B 5 4 cos 1106t 2 y2 az mWb/m2
EXAMPLE 9.1
FIGURE 9.6  For Example 9.1.
428  CHAPTER 9  MAXWELL’S EQUATIONS
Solution:
(a)	 In this case, we have transformer emf given by
Vemf 5 23
# dS 5 3
0.08
y50
0.06
x50
4110232 11062 sin 106t dx dy
5 411032 10.082 10.062 sin 106t
5 19.2 sin 106t V
The polarity of the induced voltage (according to Lenz’s law) is such that point P on the bar
is at lower potential than Q when B is increasing.
(b)	 This is the case of motional emf:
Vemf 5 3
1u 3 B2 # dl 5 3
x5,
1uay 3 Baz2 # dx ax
5 24.8 mV
(c)	 Both transformer emf and motional emf are present in this case. This problem can be
solved in two ways.
Method 1:  Using eq. (9.15), we write
Vemf 5 23
# dS 1 3
1u 3 B2 # dl
(9.1.1)
5 3
0.06
x50
4.102311062  sin1106t 2 yr2dyr dx
1 3
0.06
320ay 3 4.1023 cos1106t 2 y2az4 # dx ax
5 240 cos1106t 2 yr2 `
2 80110232 10.062 cos1106t 2 y2
5 240 cos1106t 2 y2 2 240 cos 106t 2 4.8110232 cos1106t 2 y2
. 240 cos1106t 2 y2 2 240 cos 106t
(9.1.2)
because the motional emf is negligible compared with the transformer emf. Using trigono­
metric identity, we write
cos A 2 cos B 5 22 sin A 1 B
sin A 2 B
(9.1.3)
Vemf 5 2480 sina106t 2
2b sin
2 V
5 2uB, 5 220A4 3 10232 A0.062
9.3 Transformer and Motional Electromotive Forces  429
which is the same result in (9.1.2). Notice that in eq. (9.1.1), the dependence of y on time
is taken care of in e 1u 3 B2 # dl, and we should not be bothered by it in B/t. Why?
Because in computing the transformer emf, the loop is assumed stationary. This is a subtle
point one must keep in mind in applying eq. (9.1.1). For the same reason, the second
method is always easier.
PRACTICE EXERCISE  9.1
Consider the loop of Figure 9.5. If B 5 0.5az Wb/m2, R 5 20 V, , 5 10 cm, and the
rod is moving with a constant velocity of 8ax m/s, find
(a)  The induced emf in the rod
(b)  The current through the resistor
(c)  The motional force on the rod
(d)  The power dissipated by the resistor.
Answer:  (a) 0.4 V,  (b) 20 mA,  (c) 2ax mN,  (d) 8 mW.
Method 2: Alternatively, we can apply eq. (9.4), namely,
Vemf 5 2'
(9.1.4)
where
 5 3 B # dS
5 3
y50
0.06
x50
4 cos1106t 2 y2 dx dy
5 2410.062 sin1106t 2 y2 `
y50
5 20.24 sin1106t 2 y2 1 0.24 sin 106t mWb
But
dt 5 u S  y 5 ut 5 20t
Hence,
 5 20.24 sin1106t 2 20t2 1 0.24 sin 106t mWb
Vemf 5 2'
't 5 0.241106 2 202 cos1106t 2 20t2 2 0.2411062 cos 106t mV
. 240 cos1106t 2 y2 2 240 cos 106t V
(9.1.5)
430  CHAPTER 9  MAXWELL’S EQUATIONS
The loop shown in Figure 9.7 is inside a uniform magnetic field B 5 50ax mWb/m2. If
side DC of the loop cuts the flux lines at the frequency of 50 Hz and the loop lies in the
yz-plane at time t 5 0, find
(a)  The induced emf at t 5 1 ms
(b)  The induced current at t 5 3 ms
Solution:
(a)	 Since the B field is time invariant, the induced emf is motional, that is,
Vemf 5 3
1u 3 B2 # dl
where
dl 5 dlDC 5 dz az,  u 5 dlr
dt 5 r df
dt  af 5 rvaf
r 5 AD 5 4 cm,
v 5 2pf 5 100p
Because u and dl are in cylindrical coordinates, we transform B into cylindrical coordi­
nates by using eq. (2.9):
B 5 Boax 5 Bo1cos f ar 2 sin f af2
where Bo 5 0.05. Hence,
FIGURE 9.7  For Example 9.2; polarity is for
increasing emf.
EXAMPLE 9.2
u 3 B 5 †
Bo cos f
2Bo sin f
† 5 2rvBo cos f az
9.3 Transformer and Motional Electromotive Forces  431
and
1u 3 B2 # dl 5 2rvBo cos f dz 5 20.041100p2 10.052 cos f dz
5 20.2p cos f dz
Vemf 5 3
0.03
z50
2 0.2p cos f dz 5 26p cos f mV
To determine f, recall that
v 5 df
dt  S  f 5 vt 1 Co
where Co is an integration constant. At t 5 0, f 5 p/2 because the loop is in the yz-plane
at that time, Co 5 p/2. Hence,
f 5 vt 1 p
and
Vemf 5 26p cosavt 1 p
2 b 5 6p sin1100pt2 mV
At t 5 1 ms, Vemf 5 6p sin10.1p2 5 5.825 mV
(b)	 The current induced is
i 5 Vemf
5 60p sin1100pt2 mA
At t 5 3 ms,
i 5 60p sin10.3p2 mA 5 0.1525 A
PRACTICE EXERCISE  9.2
Rework Example 9.2 with everything the same except that the B field is changed to:
(a)  B 5 50ay mWb/m2—that is, the magnetic field is oriented along the y-direction
(b)  B 5 0.02tax Wb/m2—that is, the magnetic field is time varying.
Answer:  (a) 217.93 mV, 20.1108 A,  (b) 20.5 mV, 241.92 mA.
The magnetic circuit of Figure 9.8 has a uniform cross section of 1023 m2. If the circuit is
energized by a current i11t2 5 3 sin 100pt A in the coil of N1 5 200 turns, find the emf
induced in the coil of N2 5 100 turns. Assume that m 5 500 mo.
EXAMPLE 9.3
432  CHAPTER 9  MAXWELL’S EQUATIONS
Solution:
The flux in the circuit is
PRACTICE EXERCISE  9.3
A magnetic core of uniform cross section 4 cm2 is connected to a 120 V, 60 Hz
generator as shown in Figure 9.9. Calculate the induced emf V2 in the secondary
coil.
Answer:  72 V.
FIGURE 9.8  Magnetic circuit of
Ex­ample 9.3.
FIGURE 9.9  For Practice Exercise 9.3.
 5 
 5 N1i1
,/mS 5 N1i1mS
2pro
According to Faraday’s law, the emf induced in the second coil is
V2 5 2N2 d
dt 5 2N1N2mS
2pro
di1
5 2100 # 12002 # 15002 # 14p 3 10272 # 110232 # 300p cos 100pt
2p110 3 10222
5 26p cos 100pt V
9.4 Displacement Current  433
9.4  DISPLACEMENT CURRENT
In Section 9.3 we have essentially reconsidered Maxwell’s curl equation for electrostatic
fields and modified it for time-varying situations to satisfy Faraday’s law. We shall now
­reconsider Maxwell’s curl equation for magnetic fields (Ampère’s circuit law) for time-
varying conditions.
For static EM fields, we recall that
= 3 H 5 J
(9.17)
But the divergence of the curl of any vector field is identically zero (see Example 3.10).
Hence,
= # 1= 3 H2 5 0 5 = # J
(9.18)
The continuity of current in eq. (5.43), however, requires that
= # J 5 2'rv
't 2 0
(9.19)
Thus eqs. (9.18) and (9.19) are obviously incompatible for time-varying conditions. We
must modify eq. (9.17) to agree with eq. (9.19). To do this, we add a term to eq. (9.17) so
that it becomes
= 3 H 5 J 1 Jd
(9.20)
where Jd is to be determined and defined. Again, the divergence of the curl of any vector
is zero. Hence:
= # 1= 3 H2 5 0 5 = # J 1 = # Jd
(9.21)
In order for eq. (9.21) to agree with eq. (9.19),
= # Jd 5 2= # J 5 'rv
't 5 '
't 1= # D2 5 = # 'D
't 
(9.22a)
Jd 5 'D
dt 
(9.22b)
Substituting eq. (9.22b) into eq. (9.20) results in
= 3 H 5 J 1 'D
't 
(9.23)
This is Maxwell’s equation (based on Ampère’s circuit law) for a time-varying field. The
term Jd 5 'D/'t is known as displacement current density and J is the conduction current
434  CHAPTER 9  MAXWELL’S EQUATIONS
density 1J 5 sE2.3 The insertion of Jd into eq. (9.17) was one of the major contributions
of Maxwell. Without the term Jd, the propagation of electromagnetic waves (e.g., radio or
TV waves) would be impossible. At low frequencies, Jd is usually neglected compared with
J. However, at radio frequencies, the two terms are comparable. At the time of Maxwell,
­high-frequency sources were not available and eq. (9.23) could not be verified experi­
mentally. It was years later that Hertz succeeded in generating and detecting radio waves,
thereby verifying eq. (9.23). This is one of the rare cases of a mathematical argument paving
the way for experimental investigation.
Based on the displacement current density, we define the displacement current as
Id 5 3
Jd # dS 5 3
# dS
(9.24)
We must bear in mind that displacement current is a result of time-varying electric field. A
typical example of such current is the current through a capacitor when an alternating volt­
age source is applied to its plates. This example, shown in Figure 9.10, serves to illustrate
the need for the displacement current. Applying an unmodified form of Ampère’s circuit
law to a closed path L shown in Figure 9.10(a) gives
H # dl 5 3
J # dS 5 Ienc 5 I
(9.25)
where I is the current through the conductor and S1 is the flat surface bounded by L.
If we use the balloon-shaped surface S2 that passes between the capacitor plates, as in
Figure 9.10(b),
H # dl 5 3
J # dS 5 Ienc 5 0
(9.26)
because no conduction current 1J 5 02 flows through S2. This is contradictory in view
of the fact that the same closed path L is used. To resolve the conflict, we need to include
FIGURE 9.10  Two surfaces of integration
showing the need for Jd in Ampère’s circuit
law.
3 Recall that we also have J 5 rvu as the convection current density.
9.4 Displacement Current  435
the displacement current in Ampère’s circuit law. The total current density is J 1 Jd. In
eq. (9.25), Jd 5 0, so that the equation remains valid. In eq. (9.26), J 5 0, so that
H # dl 5 3
Jd # dS 5 d
dt 3
D # dS 5 dQ
dt 5 I
(9.27)
So we obtain the same current for either surface, although it is conduction current in S1
and displacement current in S2.
A parallel-plate capacitor with plate area of 5 cm2 and plate separation of 3 mm has a
­voltage 50 sin 103t V applied to its plates. Calculate the displacement current assuming
e 5 2eo.
Solution:
D 5 eE 5 e V
Jd 5 'D
't 5 e
d dV
Hence,
Id 5 Jd # S 5 eS
d  dV
dt 5 C dV
which is the same as the conduction current, given by
Ic 5 dQ
dt 5 S drs
dt 5 S dD
dt 5 eS dE
dt 5 eS
d  dV
dt 5 C dV
Id 5 2 # 1029
36p
# 5 3 1024
3 3 1023 # 103 3 50 cos 103t
5 147.4 cos 103t nA
PRACTICE EXERCISE  9.4
In free space, E 5 20 cos1vt 2 50x2 ay V/m. Calculate
(a)  Jd
(b)  H
(c)  v
Answer:  (a) 220veo sin1vt 2 50x2 ay A/m2,  (b) 0.4 veo cos1vt 2 50x2 az A/m,
(c) 1.5 3 1010 rad/s.
EXAMPLE 9.4
436  CHAPTER 9  MAXWELL’S EQUATIONS
9.5  MAXWELL’S EQUATIONS IN FINAL FORMS
The Scottish physicist James Clerk Maxwell (1831–1879) is regarded as the founder of
electromagnetic theory in its present form. Maxwell’s celebrated work led to the discovery
of electromagnetic waves.4 Through his theoretical efforts when he was between 35 and
40 years old, Maxwell published the first unified theory of electricity and magnetism. The
theory comprised all previously known results, both experimental and theoretical, on
electricity and magnetism. It further introduced displacement current and predicted the
existence of electromagnetic waves. Maxwell’s equations were not fully accepted by many
scientists until 1888, when they were confirmed by Heinrich Rudolf Hertz (1857–1894).
The German physicist was successful in generating and detecting radio waves.
The laws of electromagnetism that Maxwell put together in the form of four equations
were presented in Table 7.2 in Section 7.6 for static conditions. The more generalized forms
of these equations are those for time-varying conditions shown in Table 9.1. We notice
from the table that the divergence equations remain the same, while the curl equations have
been modified. The integral form of Maxwell’s equations depicts the underlying physical
laws, whereas the differential form is used more frequently in solving problems. For a field
to “qualify” as an electromagnetic field, it must satisfy all four Maxwell’s equations. The
importance of Maxwell’s equations cannot be overemphasized because they summarize all
known laws of electromagnetism. We shall often refer to them in the remainder of this text.
Since this section is meant to be a compendium of our discussion in this text, it is
worthwhile to mention other equations that go hand in hand with Maxwell’s equations.
The Lorentz force equation
F 5 Q1E 1 u 3 B2
(9.28)
TABLE 9.1  Generalized Forms of Maxwell’s Equations
Differential Form
Integral Form
Remarks
= # D 5 rv
D # dS 5 3
rv dv
Gauss’s law
= # B 5 0
B # dS 5 0
Nonexistence of isolated magnetic charge*
= 3 E 5 2'B
E # dl 5 2 '
't 3
B # dS
Faraday’s law
= 3 H 5 J 1 'D
H # dl 5 3
aJ 1 'D
't b # dS
Ampère’s circuit law
*This is also referred to as Gauss’s law for magnetic fields.
4 Maxwell’s work can be found in his two-volume Treatise on Electricity and Magnetism (New York: Dover, 1954).
9.5 Maxwell’s Equations in Final Forms  437
is associated with Maxwell’s equations. Also the equation of continuity
= # J 5 2'rv
't 
(9.29)
is implicit in Maxwell’s equations. The concepts of linearity, isotropy, and homogeneity of a
material medium still apply for time-varying fields; in a linear, homogeneous, and isotropic
medium characterized by s, «, and m, the constitutive relations
D 5 eE 5 eoE 1 P
(9.30a)
B 5 mH 5 mo1H 1 M2
(9.30b)
J 5 sE 1 rvu
(9.30c)
hold for time-varying fields. Consequently, the boundary conditions remain valid for time-
varying fields, where an is the unit normal vector to the boundary.
E1t 2 E2t 5 0  or   1E1 2 E22 3 an  5 0
(9.31a)
H1t 2 H2t 5 K   or  1H1 2 H22 3 an 5 K
(9.31b)
D1n 2 D2n 5 rs   or    1D1 2 D22 # an 5 rs
(9.31c)
B1n 2 B2n 5 0  or   1B2 2 B12 # an
5 0
(9.31d)
However, for a perfect conductor 1s . `2 in a time-varying field,
E 5 0,  H 5 0,  J 5 0
(9.32)
and hence,
Bn 5 0,  Et 5 0
(9.33)
For a perfect dielectric 1s . 02, eqs. (9.31) hold except that K 5 0. Though eqs. (9.28) to
(9.33) are not Maxwell’s equations, they are associated with them.
To complete this summary section, we present a structure linking the various potentials
and vector fields of the electric and magnetic fields in Figure 9.11. This electromagnetic flow
diagram helps with the visualization of the basic relationships between field quantities. It
also shows that it is usually possible to find alternative formulations, for a given problem, in
a relatively simple manner. It should be noted that in Figure 9.11(b) and (c), we introduce rm
as the free magnetic density (similar to rv), which is, of course, zero, Ae as the electric vector
potential (analogous to A), and Jm as the magnetic current density (analogous to J). Using
terms from stress analysis, the principal relationships are typified as follows:
(a)  compatibility equations
= # B 5 rm 5 0
(9.34)
438  CHAPTER 9  MAXWELL’S EQUATIONS
and
= 3 E 5 2'B
't 5 Jm
(9.35)
(b)  constitutive equations
B 5 mH
(9.36)
and
D 5 eE
(9.37)
(c)  equilibrium equations
= # D 5 rv
(9.38)
and
= 3 H 5 J 1 'D
't 
(9.39)
FIGURE 9.11  Electromagnetic flow diagrams showing the relationship between the poten­
tials and vector fields: (a) electrostatic system, (b) magnetostatic system, (c) electromag­
netic system. [Adapted with permission from the Publishing Department of the Institution
of Electrical Engineers.]
9.6 Time-Varying Potentials  439
†9.6  TIME-VARYING POTENTIALS
For static EM fields, we obtained the electric scalar potential as
V 5 3
rv dv
4peR
(9.40)
and the magnetic vector potential as
A 5 3
mJ dv
4pR 
(9.41)
We would like to examine what happens to these potentials when the fields are time vary­
ing. Recall that A was defined from the fact that = # B 5 0, which still holds for time-­
varying fields. Hence the relation
B 5 = 3 A
(9.42)
holds for time-varying situations. Combining Faraday’s law as expressed in eq. (9.8) with
eq. (9.42) gives
= 3 E 5 2 '
't 1= 3 A2
(9.43a)
= 3 aE 1 'A
't b 5 0
(9.43b)
Since the curl of the gradient of a scalar field is identically zero (see Practice Exercise 3.10),
the solution to eq. (9.43b) is
E 1 'A
't 5 2=V
(9.44)
E 5 2=V 2 'A
't 
(9.45)
From eqs. (9.42) and (9.45), we can determine the vector fields B and E, provided the
­potentials A and V are known. However, we still need to find some expressions for A and
V similar to those in eqs. (9.40) and (9.41) that are suitable for time-varying fields.
From Table 9.1 or eq. (9.38) we know that = # D 5 rv is valid for time-varying condi­
tions. By taking the divergence of eq. (9.45) and making use of eqs. (9.37) and (9.38), we obtain
= # E 5 rv
e 5 2=2V 2 '
't 1= # A2
440  CHAPTER 9  MAXWELL’S EQUATIONS
=2V 1 '
't 1= # A2 5 2rv
e 
(9.46)
Taking the curl of eq. (9.42) and incorporating eqs. (9.23) and (9.45) results in
= 3 = 3 A 5 mJ 1 em '
't a2=V 2 'A
't b
5 mJ 2 me = a'V
't b 2 me '2A
't2 
(9.47)
where D 5 eE and B 5 mH have been assumed. By applying the vector identity
= 3 = 3 A 5 =1= # A2 2 =2A
(9.48)
to eq. (9.47),
=2A 2 =1= # A2 5 2mJ 1 me = a'V
't b 1 me '2A
't2 
(9.49)
A vector field is uniquely defined when its curl and divergence are specified. The curl of
A has been specified by eq. (9.42); for reasons that will be obvious shortly, we may choose
the divergence of A as
= # A 5 2me 'V
't 
(9.50)
in mind when we chose = # A 5 0 for magnetostatic fields in eq. (7.59). By imposing the
Lorenz condition of eq. (9.50), eqs. (9.46) and (9.49), respectively, become
=2V 2 me '2V
't2 5 2rv
e 
(9.51)
and
=2A 2 me '2 A
't2 5 2mJ
(9.52)
which are wave equations to be discussed in the next chapter. The reason for choosing
the Lorenz condition becomes obvious as we examine eqs. (9.51) and (9.52). The Lorenz
­condition uncouples eqs. (9.46) and (9.49) and also produces a symmetry between
eqs. (9.51) and (9.52). It can be shown that the Lorenz condition can be obtained from
the ­continuity equation; therefore, our choice of eq. (9.50) is not arbitrary. Notice that
eqs. (6.4) and (7.60) are special static cases of eqs. (9.51) and (9.52), respectively. In other
words, potentials V and A satisfy Poisson’s equations for time-varying conditions. Just as
5 Not to be confused with Hendrick A. Lorentz, Ludvig V. Lorenz (1829–1891) was a Danish ­mathematician
and physicist.
This choice relates A and V, and it is called the Lorenz condition for potentials.  We had this
9.7 Time-Harmonic Fields  441
eqs. (9.40) and (9.41) are the solutions, or the integral forms of eqs. (6.4) and (7.60), it can
be shown that the solutions6 to eqs. (9.51) and (9.52) are
V 5 3
3rv4 dv
4peR 
(9.53)
and
A 5 3
m3J4 dv
4pR 
(9.54)
The term [rv] (or [J]) means that the time t in rv1x, y, z, t2 [or J1x, y, z, t2] is replaced by
the retarded time t given by
tr 5 t 2 R
(9.55)
where R 5 0r 2 rr 0  is the distance between the source point r and the observation
point r and
u 5
"me
(9.56)
is the velocity of wave propagation. In free space, u 5 c . 3 3 108 m/s is the speed of
light in a vacuum. Potentials V and A in eqs. (9.53) and (9.54) are, respectively, called the
retarded electric scalar potential and the retarded magnetic vector potential. Given rv and J,
V and A can be determined by using eqs. (9.53) and (9.54); from V and A, E and B can be
determined by using eqs. (9.45) and (9.42), respectively.
9.7  TIME-HARMONIC FIELDS
So far, our time dependence of EM fields has been arbitrary. To be specific, we shall assume
that the fields are time harmonic.
A time-harmonic field is one that varies periodically or sinusoidally with time.
Not only is sinusoidal analysis of practical value, but also it can be extended to most
waveforms by Fourier analysis. Sinusoids are easily expressed in phasors, which are more
convenient to work with. Before applying phasors to EM fields, it is worthwhile to have a
brief review of the concept of phasor.
A phasor is a complex number that contains the amplitude and the phase of a sinusoi­
dal oscillation. As a complex number, a phasor z can be represented as
z 5 x 1 jy 5 r lf
(9.57)
6 For example, see D. K. Cheng, Fundamentals of Engineering Electromagnetics. Reading, MA: ­Addison-Wesley,
1993, pp. 253–254.
442  CHAPTER 9  MAXWELL’S EQUATIONS
z 5 r ejf 5 r 1cos f 1 j sin f2
(9.58)
where j 5 "21, x is the real part of z, y is the imaginary part of z, r is the magnitude of
z, given by
r 5 0 z 0 5 "x2 1 y2
(9.59)
and f is the phase of z, given by
f 5 tan21
(9.60)
Here x, y, z, r, and f should not be mistaken as the coordinate variables, although they
look similar (different letters could have been used but it is hard to find better ones).
The phasor z can be represented in rectangular form as z 5 x 1 jy or in polar form as
z 5 r lf 5 r ejf. The two forms of representing z are related in eqs. (9.57) to (9.60) and
illustrated in Figure 9.12. Addition and subtraction of phasors are better performed in
rectangular form; multiplication and division are better done in polar form.
Given complex numbers
z 5 x 1 jy 5 r lf,  z1 5 x1 1 jy1 5 r1 lf1,  and  z2 5 x2 1 jy2 5 r2 lf2
the following basic properties should be noted.
addition:
z1 1 z2 5 1x1 1 x22 1 j1 y1 1 y22
(9.61a)
subtraction:
z1 2 z2 5 1x1 2 x22 1 j1 y1 2 y22
(9.61b)
multiplication:
z1z2 5 r1r2 liiii
f1 1 f2
(9.61c)
division:
5 r1
liiii
f1 2 f2
(9.61d)
FIGURE 9.12  Representation of a phasor
z 5 x 1 jy 5 r lf.
9.7 Time-Harmonic Fields  443
Square root:
"z 5 "r lii
f/2
(9.61e)
Complex conjugate:
z* 5 x 2 jy 5 rii
l2f 5 re2jf
(9.61f)
Other properties of complex numbers can be found in Appendix A.2.
To introduce the time element, we let
 5 t 1 
(9.62)
where u may be a function of time or space coordinates or a constant. The real (Re) and
imaginary (Im) parts of
rej 5 re j(t1) 5 rej ejt
(9.63)
are respectively given by
Re re jf 5 r cos(t 1 )
(9.64a)
and
Im re jf 5 r sin(t 1 )
(9.64b)
Thus, a sinusoidal current I(t) 5 Io cos(t 1 ), for example, equals the real part of Ioejejt.
The current I(t) 5 Io sin(t 1 ), which is the imaginary part of Ioejejt, can be repre­
sented as the real part of Ioe jejte2j90 because sin  5 cos( 2 90). However, in perform­
ing our mathematical operations, we must be consistent in our use of either the real part or
the imaginary part of a quantity, but never both at the same time.
The complex term Ioe j, which results from dropping the time factor ejt in I(t), is
called the phasor current, denoted by Is; that is,
Is 5 Ioe j 5 Io 
(9.65)
where the subscript s denotes the phasor form of I(t). Thus I(t) 5 Io cos(t 1 ), the instan­
taneous form, can be expressed as
I(t) 5 Re  Ise jt 
(9.66)
In general, a phasor is a complex quantity and could be a scalar or a vector. If a vector A(x,
y, z, t) is a time-harmonic field, the phasor form of A is As(x, y, z); the two quantities are
related as
A(x, y, z, t) 5 ReAs (x, y, z)ejt
(9.67)
Note that the phasor is a function of position, not a function of time. For example,
if A 5 Ao cos1vt 2 bx2 ay, we can write A as
A 5 Re1Aoe2jbxaye jvt2
(9.68)
444  CHAPTER 9  MAXWELL’S EQUATIONS
Comparing this with eq. (9.67) indicates that the phasor form of A is
As 5 Aoe2jbxay
(9.69)
Notice from eq. (9.67) that
't 5 '
't Re1Asejvt2
5 Re1jvAsejvt2 
(9.70)
showing that taking the time derivative of the instantaneous quantity is equivalent to mul­
tiplying its phasor form by jv. That is,
't  S  jvAs
(9.71)
Similarly,
3 A 't S  As
jv
(9.72)
Note that the real part is chosen in eq. (9.67) as in circuit analysis; the imaginary part
could equally have been chosen. Also notice the basic difference between the instantaneous
form A1x, y, z, t2 and its phasor form As1x, y, z2: the former is time dependent and real,
whereas the latter is time invariant and generally complex. It is easier to work with As and
obtain A from As whenever necessary by using eq. (9.67).
We shall now apply the phasor concept to time-varying EM fields. The field quantities
E1x, y, z, t2, D1x, y, z, t2, H1x, y, z, t2, B1x, y, z, t2, J1x, y, z, t2, and rv1x, y, z, t2 and their
derivatives can be expressed in phasor form by using eqs. (9.67) and (9.71).
Let us see how we can write Maxwell’s equations in phasor form.  For example, ­consider
 3 E (x, y, z, t) 5 2 '
't B (x, y, z, t)
(9.73)
We let
E (x, y, z, t) 5 Re Es(x, y, z)e jt
and
B (x, y, z, t) 5 Re Bs(x, y, z)e jt
Substituting these in eq. (9.73) gives
= 3 eRe3Esejvt4 f 5 2 '
't eRe3Bsejvt4 f
(9.74)
We consider the left-hand side of eq. (9.74). The curl operation operates only on
(x, y, z),
= 3 eRe3Esejvt4 f 5 Ree 3= 3 Es4ejvtf
(9.75)
9.7 Time-Harmonic Fields  445
We similarly consider the right-hand side of eq. (9.74), keeping in mind that Bs does not
depend on time:
2 '
't eRe3Bsejvt4 f 5 2ReeBs '
't ejvtf 5 2Re5jvBsejvt6
(9.76)
Comparing eqs. (9.75) and (9.76), we obtain
= 3 Es 5 2jvBs
(9.77)
which is the phasor form of eq. (9.73).  Other Maxwell’s equations can be treated in a
similar manner, and we obtain Table 9.2.  From Table 9.2, note that the time factor e jvt
disappears because it is associated with every term and therefore factors out, resulting in
time-independent equations. Herein lies the justification for using phasors: the time factor
can be suppressed in our analysis of time-harmonic fields and inserted when necessary.
Also note that in Table 9.2, the time factor e jvt has been assumed. It is equally possible
to have assumed the time factor e2jvt, in which case we would need to replace every j in
Table 9.2 with 2j.
TABLE 9.2  Time-Harmonic Maxwell’s Equations
Assuming Time Factor e jvt
Point Form
Integral Form
= # Ds 5 rvs
C Ds # dS 5 3 rvs dv
= # Bs 5 0
C Bs # dS 5 0
= 3 Es 5 2jvBs
C Es # dl 5 2jv 3 Bs # dS
= 3 Hs 5 Js 1 jvDs
C Hs # dl 5 3 1Js 1 jvDs2 # dS
Evaluate the complex numbers
(a)	 z1 5
j13 2 j42*
121 1 j62 12 1 j2 2
(b)	 z2 5 c
1 1 j
4 2 j8d
1/2
Solution:
(a)	 This can be solved in two ways: working with z in rectangular form or polar form.
Method 1  (working in rectangular form):
Let
z1 5 z3z4
z5z6
EXAMPLE 9.5
446  CHAPTER 9  MAXWELL’S EQUATIONS
where
z3 5 j
z4 5 13 2 j42* 5 the complex conjugate of 13 2 j42
5 3 1 j4
We note parenthetically that one can find the complex conjugate of a complex number
simply by replacing every j with 2j:
z5 5 21 1 j6
and
z6 5 12 1 j2 2 5 4 2 1 1 j4 5 3 1 j4
Hence,
z3z4 5 j13 1 j42 5 24 1 j3
z5z6 5 121 1 j62 13 1 j42 5 23 2 j4 1 j18 2 24
5 227 1 j14
and
z1 5
24 1 j3
227 1 j14
Multiplying and dividing z1 by 227 2 j14 (rationalization), we have
Method 2  (working in polar form):
z3 5 j 5 1 lii
90°
z4 5 13 2 j42* 5 15 liiii
253.132* 5 5 liii
53.13°
z5 5 121 1 j62 5 "37 liii°
99.46
z6 5 12 1 j2 2 5 1"5 liii
26.562 2 5 5 liii
53.13°
Hence,
z1 5
11 lii
90°2 15 liii
53.13°2
1"37 liii
99.46°2 15 liii
53.13°2
"37
liiiiii
90° 2 99.46° 5 0.1644 liiii
29.46°
5 0.1622 2 j0.027
as obtained before.
z1 5
124 1 j32 1227 2 j142
1227 1 j142 1227 2 j142 5
150 2 j25
272 1 142
5 0.1622 2 j0.027 5 0.1644 liii
29.46°
9.7 Time-Harmonic Fields  447
(b)	 Let
z2 5 cz7
z8 d
1/2
where
z7 5 1 1 j 5 "2 lii
45°
and
z8 5 4 2 j8 5 4"5 liii
263.4°
Hence
"2 lii
45°
4"5 liii
263.4°
5 0.1581 liii
108.4°
and
z2 5 "0.1581 liiii
108.4°/2
5 0.3976 lii
54.2°
PRACTICE EXERCISE  9.5
Evaluate these complex numbers:
(a)  j3 c
1 1 j
2 2 j d
(b)  6 l30° 1 j5 2 3 1 e j45°
Answer:  (a) 0.24 1 j0.32,  (b) 2.03 1  j8.707.
Given that A 5 10 cos1108t 2 10x 1 60°2 az and Bs 5 120/j2 ax 1 10 ej2px/3 ay, express A
in phasor form and Bs in instantaneous form.
Solution:
A 5 Re310e j1vt210x160°2az4
where v 5 108. Hence
As 5 10 e j160°210x2az
5 "2
4"5
l45° 2 263.4°
iiiiii
EXAMPLE 9.6
A 5 Re310ej160º210x2 az ejvt4 5 Re1Asejvt2
448  CHAPTER 9  MAXWELL’S EQUATIONS
Bs 5 20
j  ax 1 10ej2px/3ay 5 2j20ax 1 10ej2px/3ay
5 20e2jp/2ax 1 10e j2px/3ay
B 5 Re1Bsejvt2
5 Re c20e j1vt2p/22ax 1 10e j1vt12px/32ayd
5 20 cos1vt 2 p/22ax 1 10 cosavt 1 2px
3 bay
5 20 sin vt ax 1 10 cosavt 1 2px
3 bay
PRACTICE EXERCISE  9.6
If P 5 2 sin110t 1 x 2 p/42ay and Qs 5 e jx1ax 2 az2sin py, determine the phasor
form of P and the instantaneous form of Qs.
Answer:  2ej1x23p/42ay, sin p y cos1vt 1 x2 1ax 2 az2.
The electric field and the magnetic field in free space are given by
E 5 50
r  cos1106t 1 bz2af V/m
H 5 Ho
r  cos1106t 1 bz2ar A/m
Express these in phasor form and determine the constants Ho and b such that the fields
­satisfy Maxwell’s equations.
Solution:
The instantaneous forms of E and H are written as
E 5 Re1Ese jvt2,  H 5 Re1Hse jvt2
(9.7.1)
where v 5 106 and phasors Es and Hs are given by
Es 5 50
r  e jbzaf,  Hs 5 Ho
r  e jbzar
(9.7.2)
EXAMPLE 9.7
9.7 Time-Harmonic Fields  449
For free space, rv 5 0, s 5 0, e 5 eo, and m 5 mo
= # D 5 eo= # E 5 0  S  = # Es 5 0
(9.7.3)
= # B 5 mo= # H 5 0 S  = # Hs 5 0
(9.7.4)
= 3 H 5 sE 1 eo 'E
't   S  = 3 Hs 5 jveoEs
(9.7.5)
= 3 E 5 2mo 'H
S  = 3 Es 5 2jvmoHs
(9.7.6)
Substituting eq (9.7.2) into eqs. (9.7.3) and (9.7.4), it is readily verified that two Maxwell’s
equations are satisfied; that is,
= # Es 5 1
r '
'f 1Efs2 5 0
= # Hs 5 1
r '
'r 1rHrs2 5 0
Now
= 3 Hs 5 = 3 aHo
r  ejbzarb 5
jHob
r  ejbzaf
(9.7.7)
Substituting eqs. (9.7.2) and (9.7.7) into eq. (9.7.5), we have
jHob
r  ejbzaf 5 jveo 50
r  ejbzaf
Hob 5 50 veo
(9.7.8)
Similarly, substituting eq. (9.7.2) into eq. (9.7.6) gives
2jb 50
r  ejbzar 5 2jvmo Ho
r  ejbzar
b 5 50
vmo
(9.7.9)
Multiplying eq. (9.7.8) by eq. (9.7.9) yields
2 5 1502 2 eo
, so Maxwell’s equations become
450  CHAPTER 9  MAXWELL’S EQUATIONS
Dividing eq. (9.7.8) by eq. (9.7.9), we get
b2 5 v2moeo
b 5 6v"moeo 5 6v
c 5 6
106
3 3 108
5 63.33 3 1023
In view of eq. (9.7.8), Ho 5 0.1326, b 5 3.33 3 1023 or Ho 5 20.1326, b 523.33 3 1023;
only these will satisfy Maxwell’s four equations.
PRACTICE EXERCISE  9.7
In air, E 5 sin u
cos16 3 107t 2 br2af V/m.
Find b and H.
Answer:  0.2 rad/m, 2
12pr2 cos u sin16 3 107t 2 0.2r2ar 2
120pr sin u 3
cos16 3 107t 2 0.2r2au /m.
In a medium characterized by s 5 0, m 5 mo, e 5 4eo, and
E 5 20 sin1108t 2 bz2ay V/m
calculate b and H.
Solution:
This problem can be solved directly in time domain or by using phasors. As in Example 9.7,
we find b and H by making E and H satisfy Maxwell’s four equations.
Method 1  (time domain):
Let us solve this problem the harder way—in time domain. It is evident that Gauss’s law for
electric fields is satisfied; that is,
= # E 5
'Ey
'y 5 0
EXAMPLE 9.8
Ho 5 650"eo/mo 5 6 50
120p 5 60.1326
9.7 Time-Harmonic Fields  451
From Faraday’s law,
= 3 E 5 2m 'H
't   S   H 5 21
m 3 1= 3 E2 dt
But
= 3 E 5 ∞
∞5 2
'Ey
'z ax 1
'Ey
'x az
5 20b cos1108t 2 bz2 ax 1 0
Hence,
H 5 220b
m  3 cos1108t 2 bz2 dt ax
5 2 20b
m108 sin1108t 2 bz2 ax
(9.8.1)
It is readily verified that
= # H 5 'Hx
'x 5 0
showing that Gauss’s law for magnetic fields is satisfied. Lastly, from Ampère’s law
= 3 H 5 sE 1 e 'E
't  S   E 5 1
e 3 1= 3 H2 dt
(9.8.2)
because s 5 0.
But
= 3 H 5 ∞
∞5 'Hx
'z ay 2 'Hx
'y az
5 20b2
m108 cos1108t 2 bz2 ay 1 0
452  CHAPTER 9  MAXWELL’S EQUATIONS
where H in eq. (9.8.1) has been substituted. Thus eq. (9.8.2) becomes
E 5 20b2
me108 3 cos1108t 2 bz2 dt ay
5 20b2
me1016 sin1108t 2 bz2 ay
Comparing this with the given E, we have
20b2
me1016 5 20
b 5 6108"me 5 6108"mo # 4eo 5 6108122
5 6 108122
3 3 108
5 62
The b would be negative only in metamaterials, for an isotropic medium, b 5 2
From eq. (9.8.1),
H 5 1
20 12/32
4p # 102711082  sin a108t
3 b ax
H 5 1 1
3p sin a108t
3 bax A/m
Method 2  (using phasors):
E 5 Im1Ese jvt2  S   Es 5 20e2jbz ay
(9.8.3)
where v 5 108.
Again
= # Es 5
'Eys
'y 5 0
= 3 Es 5 2jvmHs  S   Hs 5 = 3 Es
2jvm
9.7 Time-Harmonic Fields  453
Hs 5
2jvm c2
'Eys
'z  axd 5 220b
vm e2jbzax
(9.8.4)
Notice that = # Hs 5 0 is satisfied.
= 3 Hs 5 jveEs  S   Es 5 = 3 Hs
jve
(9.8.5)
Substituting Hs in eq. (9.8.4) into eq. (9.8.5) gives
Es 5
jve 'Hxs
'z  ay 5 20b2e2jbz
v2me
Comparing this with the given Es in eq. (9.8.3), we have
20 5 20b2
v2me
b 5 1v"me 5 12
as obtained before. From eq. (9.8.4),
Hs 5 1 2012/32 e
jbz
10814p 3 10272  ax 5 1 1
3p e
jbzax
H 5 Im1Hse jvt2
5 ; 1
3p sin1108t
bz2ax A/m
as obtained before. It should be noticed that working with phasors is considerably simpler than
working directly in time domain. Also, notice that we have used
A 5 Im1Asejvt2
because the given E is in sine form and not cosine. If we had used
A 5 Re1Asejvt2
454  CHAPTER 9  MAXWELL’S EQUATIONS
sine would been expressed in terms of cosine, and eq. (9.8.3) would have been
E 5 20 cos1108t 2 bz 2 90º2ay 5 Re1Ese jvt2
Es 5 20e2jbz2j90°ay 5 2j20e2jbzay
and we follow the same procedure.
PRACTICE EXERCISE  9.8
A medium is characterized by s 5 0, m 5 2mo and e 5 5eo. If H 5 2
cos1vt 2 3y2az A/m, calculate  and E.
Answer:  2.846 3 108 rad/s, 2476.86 cos12.846 3 108t 2 3y2ax V/m.
†9.8  APPLICATION NOTE—MEMRISTOR
In 1971 Leon O. Chua of the University of California–Berkeley introduced the memristor
(Figure 9.13) as one of the four basic circuit elements, coequal in importance with the other
well-known circuit elements, namely, resistor (R), inductor (L), and capacitor (C). The new
element had not been physically realized when Chua proposed it. However, he was the
first to use this moniker. Not until 2008 was a physical approximation of such an element
fabricated, as a TiO2 nanodevice, by Stanley Williams’s group at Hewlett-Packard (HP).
FIGURE 9.13  Schematic of a memristor.
Chua characterized the memristor in terms of the electric charge and the mag­
netic flux. He also linked this relationship with the quasi-static expansion of Maxwell’s
9.9 Application Note—Optical Nanocircuits  455
­equations. A charge-controlled memristor can be defined as a two-terminal element sat­
isfying the constitutive relation 5 M(q), where  and q are magnetic flux and electric
charge, respectively, and M (qs) is a piecewise-differentiable function. Memristors have
interesting circuit-theoretic properties different from those of the classical circuit elements
R, L, and C. These properties, in turn, lead to remarkable applications not realizable with
the earlier circuits.
A charge-controlled memristor behaves somewhat like a nonlinear resistor RM satis­
fying a q-dependent Ohm’s law, v 5 RMi. The quantity RM is memresistance, measured in
webers per coulomb, and for all passive memristors RM 5 0. Since the voltage v is related to
dt , we can express the memresistance as RM 5
dfM1q2
. When current through a memris­
tor is turned off at t 5 t0, dq
5 0 implies q 5 q(t0). This allows us to view a memristor as
a nonvolatile analog memory. In particular, it can be used as a nonvolatile binary memory,
where two sufficiently different values of resistance are chosen to code binary states “\0”
and “\1,” respectively. The memristor reported by HP as well as many other nanodevices
proposed recently can be scaled down to atomic dimensions. Thus the memristor offers
immense potential for an ultra-low-power and ultradense nonvolatile memory technol­
ogy that could replace flash memories and dynamic random-access memories (DRAMs).
The most important common property of a memristor is the pinched hysteresis loop;
that is, the loci of (v(t), i(t)) due to any bipolar periodic current source i(t) or periodic volt­
age source v(t) must always be pinched at the origin in the sense that  (v(t), i(t)) 5 (0, 0)
must always lie on the (v,i)-loci. The pinched hysteresis loop phenomenon of the memris­
tor must hold for any bipolar periodic signal v(t), or i(t).
Although memristors have become popular only recently, they are known to abound
in many other forms. For example, the electric arc, dating back to 1801, has been identi­
fied as a memristor. Also, a very interesting and scientifically significant example is the
classic Hodgkin–Huxley axon circuit model of the squid giant axon. Chua showed that the
Hodgkin–Huxley time-varying potassium conductance is in fact a first-order memristor, and
the Hodgkin–Huxley time-varying sodium conductance is in fact a second-order memristor.
Besides serving as nonvolatile memories, locally passive memristors have been used
for switching electromagnetic devices, for field-programmable logic arrays, for synaptic
memories, and for learning. In addition, locally passive memristors have been found to
exhibit many exotic dynamical phenomena, such as oscillations, chaos, Hamiltonian vor­
tices, and autowaves.
†9.9  APPLICATION NOTE—OPTICAL NANOCIRCUITS
Circuit elements and electronic devices such as resistors, capacitors, inductors, switches,
diodes, and transistors were developed at low frequencies; higher frequencies, even radio
frequencies, were realized only later. With the development of metamaterials and nano­
technology, such elements have also been conceived at optical frequencies. Nader Engheta
and his group at the University of Pennsylvania have recently proposed circuit elements
at infrared and optical frequencies. The advantage of using lumped elements lies in their
456  CHAPTER 9  MAXWELL’S EQUATIONS
simplicity and modularity: when we want to use lumped elements by connecting them with
one another, we need to know only their in-terminal behavior and the functionality of the
overall circuit they comprise. Although it is difficult to pinpoint the frequency at which one
might consider an element to be lumped, as long as it is smaller than the wavelength but
larger than it is when the quantum effects begin to manifest, we can conveniently model an
arbitrary particle as a lumped circuit element.
〈V〉ufringe
I uimp
FIGURE 9.14  A nanoparticle used as a circuit element.
Optical lumped circuit elements with specific optical impedances have been realized
by means of deep-subwavelength nanostructures. The use of gyroscopic nanospheres has
permitted the identification of tunable circuit elements at infrared and optical frequencies.
This new area is called optical metatronics—a portmanteau term derived from metamaterials,
­optical, and electronics. The three fields of electronics, photonics, and magnetics can be brought
together seamlessly under one umbrella. In this paradigm, for information processing and data
storage at the nanoscale, the optical electric displacement currents or the optical magnetic dis­
placement currents play a more important role than the conventional drift of charged particles.
In such optical circuitry, nanostructures with specific values of permittivity (or permeability)
may act as lumped circuit elements (e.g., nanocapacitors, nanoinductors, nanoresistors).
By collecting properly arranging judiciously designed nanostructures, it is possible to
achieve a new circuit platform in which optical signals can be tailored and manipulated, thus
allowing optical information to be processed at the nanoscale. These nanostructures can be
considered to be the modules and building blocks of metatronic circuits in which optical elec­
trical fields and optical displacement currents are connected through the optical impedances of
the nanoscale lumped elements. Such optical lumped circuit elements and metatronic circuitry
afford the possibility of bringing many designs from RF electronics into the field of optics but
with a much higher level of miniaturization and higher bandwidth. Just as electrons play the
fundamental role in electronics, spins in spintronics, and photons in photonics, optical dis­
placement current is of fundamental importance in the field of metatronics.
If the real part of the permittivity of the material forming a given nanoparticle is
positive, its optical impedance is capacitive. If the imaginary part of the permittivity is
nonzero, then the particle impedance arises from a lumped conductance in parallel with
the lumped capacitance. Similarly, a plasmonic particle with negative real part for its per­
mittivity may possess an optical impedance that resembles the impedance of an inductor at
that frequency. These are fixed elements. But if we wish to make them variable, since it is
not possible to mechanically change their physical size, we can consider gyrotropic mate­
rials impressed with a dc magnetic field and still realize tunable circuit elements. These
nanocircuit elements play a vital role in metatronics for the design of various nanodevices.
Actual fabrication of optical nanofilters, left-handed/right-handed nanotransmission lines,
couplers, biosensors, information storage devices, and so on has become a reality, and more
surprises are in the offing.
†9.10  APPLICATION NOTE—WIRELESS POWER TRANSFER
AND QI STANDARD
Rapid growth in the area of high-speed wireless data transfer has resulted in the prolifera­
tion of cell-phones and various mobile devices that include even biomedical implants. In
turn, rapid charging of batteries and remote powering of electric circuits have become a
high priority and a pressing need. Especially the emergence of electric vehicles, aimed at
charging batteries. All along, recharging was done by connecting power cord battery, but to
increase mobility and ease of handling, doing this task cordlessly or, if possible, dispensing
by means of induction and resonant coupling. Induction machines, microwave heating,
and similar power devices developed historically, are all based on WPT. Since the distance
between the source and the receiver in these devices is usually small, the term wireless is
not highlighted when we refer to them.
We might achieve WPT in three broad ways: (i) near-field resonant reactive coupling,
field or non-radiative WPT is based on the near-field magnetic coupling of conductive
loops and can be either short range or mid-range in its applications. Far-field or radiative
WPT takes place from a transmitting antenna and propagates through a medium such as
air over distances that are several wavelengths long to a receiver where power is used to
energize the mobile device. This method of transferring power can be highly directive if the
locations of the receiver are predetermined or nondirective otherwise. In the latter case, the
f transmission is very low.
Wireless charging technology for portable electronic devices has escalated to the com­
mercialization stage with the introduction of the Qi (pronounced “chee”) Standard by the
Wireless Power Consortium (WPC), now (at the time of this writing) growing with a mem­
appears as a charging pad, on which is placed a compatible device, which receives energy
through resonant inductive coupling. The base station, connected to a power source, has
9.10 Application Note—Wireless Power transfer and Qi Standard  457
reducing environmental pollution, became a greater impetus for more efficient ways of
(ii) far-field directive power beaming, and (iii) far-field nondirective power transfer. Near-
efficiency o
bership of over 220 companies worldwide. The Qi system comprises a base station that
of batteries altogether would be better. Toward this goal, operating mobile devices through
wireless power transfer (WPT) became the preferred choice. The development in this area
has been rather slows, although the idea dates as far back as a century to Tesla, who
proposed that electric power can be transferred not only by means of radiation, but also
458  CHAPTER 9  MAXWELL’S EQUATIONS
planar coils that set up oscillating magnetic flux. Likewise, the mobile device has a receiver
coil that harvests energy into a power receiver. Proper shielding of coils and selection of
their parameters is done to ensure good inductive power transfer. To promote better cou­
pling and higher power transfer, relative alignment of the device is made in a guided way
by markings on the charging pad. Also, free positioning is allowed by the careful design
of coil geometry or using a technique that employs multiple cooperative flux generators.
A typical WPT charging unit is depicted in Figure 9.15. It shows the base station with the
charging pad on the top and a power transmitter section. It has a power conversion unit (PCU)
and a communications and control unit (CCU). The transmitting coil of the PCU underneath
the charging pad establishes the required oscillating magnetic flux. The Qi compatible mobile
device is equipped with the power receiver section, which essentially has the power pickup
unit (PPU) and a CCU similar to the one in the base station. A receiver coil above the charg­
ing pad collects the energy induced and conveys to the PPU, which then drives the load. The
CCUs are designed to regulate the transferred power to the required level at the highest pos­
Sensing & Control
Load
Load Power
Power Receiver
Charging Pad
Power Transmitter
Power
Conversion Unit
Communication
& Control Unit
Input Power
System Unit
Base Station
Mobile Device
Power
Pick up Unit
Communication
& Control Unit
FIGURE 9.15  A typical wireless
power transfer system for charging
a mobile device.
In terms of the Qi standards, the low-power specification delivers up to 5 W, typically
used to charge mobile devices, and the medium-power specification will deliver up to 120 W.
Usually this is allocated for power displays and laptops. In 2015, WPC demonstrated a
high-power specification that will deliver up to 1 kW, allowing the powering of kitchen
utensils among other high-power utilities. The Qi logo is depicted in Figure 9.16. As the Qi
standard gains popularity, it is forecast that Qi hotspots will begin to abound in all market
places, coffee shops, airports, sports arenas, etc. The technology of WPT developed for
electric vehicles and medical implants and other consumer power devices has begun to
explode and readers are encouraged to consult additional references.
sible transfer efficiency. Although Figure 9.15 does not show, in practice, the base station has
an array of transmitting coils to facilitate charging of numerous mobile devices. The system
unit in the base station contains additional user interfaces. Between the receiver and the trans-
mitter, communication is established with the aid of backscatter modulation.
9.10 Application Note—Wireless Power transfer and Qi Standard   459
% This script illustrates Matlab’s complex arithmetic abilities
% and assists the user to solve Practice Exercise 9.5
clear
% Matlab recognizes the input of complex numbers using i or j
% for example z = 7 - 6*j sets variable z to the complex value of
% 7 plus sqrt(-1) times 6, thus it is interactive with respect to
% entering and displaying complex values
z = input(‛Enter the complex number z in the format a+j*b... \n > ‛);
disp(sprintf(‛The real part of z is %f‛, real(z)))
% display the real part
disp(sprintf(‛The imaginary part of z is %f‛, imag(z)))
% display the imag part
disp(sprintf(‛The magnitude of z is %f‛, abs(z)))
% display the magnitude
disp(sprintf(‛The phase of z is %f degrees‛, angle(z)*180/pi))
% display the phase (degrees)
% Matlab also recognizes complex  numbers in polar form
% the exponential function accepts imaginary arguments, however it
% interprets the value as being in radians, not degrees, so if
% degrees are desired a conversion must be made
disp(‛Enter the complex number z in the a*exp(j*b) where b is‛);
z = input(‛ in radians... \n >  ‛);
disp(sprintf(‛The real part of z is %f‛, real(z)))
disp(sprintf(‛The imaginary part of z is %f‛, imag(z)))
disp(sprintf(‛The magnitude of z is %f‛, abs(z)))
disp(sprintf(‛The phase of z is %f degrees‛, angle(z)*180/pi))
% part a
% complex numbers may be handled with the same math operators
% as real numbers in matlab....
z = j^3 * ((1+j)/(2-j))^2;
disp(sprintf(‛\nPart (a)\nz = %0.2f ‛, real(z)))
MATLAB 9.1
FIGURE 9.16  Qi logo
460  CHAPTER 9  MAXWELL’S EQUATIONS
1.	 In this chapter, we have introduced two fundamental concepts: electromotive force
(emf), based on Faraday’s experiments, and displacement current, which resulted from
Maxwell’s hypothesis. These concepts call for modifications in Maxwell’s curl equations
obtained for static EM fields to accommodate the time dependence of the fields.
2.	 Faraday’s law states that the induced emf is given by 1N 5 12
For transformer emf, Vemf 5 23 'B
# dS
and for motional emf, Vemf 5 3 1u 3 B2 # dl.
3.	 The displacement current
Id 5 3 Jd # dS
where Jd 5 'D
't  (displacement current densit
law. This modification, attributed to Maxwell, predicted electromagnetic waves several
years before the phenomenon was verified experimentally by Hertz.
4.	 In differential form, Maxwell’s equations for dynamic fields are:
= # D 5 rv
= # B 5 0
= 3 E 5 2'B
= 3 H 5 J 1 'D
Each differential equation has its integral counterpart (see Tables 9.1 and 9.2) that can
be derived from the differential form by using Stokes’s theorem or the divergence theo­
disp(sprintf(‛ + j%0.2f ‛, imag(z)))
% part b
% note the conversion from degrees to radians in the
% exponential
z = 6*exp(j*30*pi/180) + j*5 - 3 +exp(j*45*pi/180);
disp(sprintf(‛\nPart (b)\nz = %0.3f ‛, real(z)))
disp(sprintf(‛ + j%0.3f ‛, imag(z)))
SUMMARY
Vemf 5 2'
y) is a modification to Ampère’s circuit
rem. Any EM field must satisfy the four Maxwell’s equations  simultaneously.
Review Questions  461
5.	 Time-varying electric scalar potential V1x, y, z, t2 and magnetic vector potential
A1x, y, z, t2 are shown to satisfy wave equations if Lorenz’s condition is assumed.
6.	 Time-harmonic fields are those that vary sinusoidally with time. They are easily
expressed in phasors, which are more convenient to work with. The cosine reference,
can be used to show that the instantaneous vector quantity A1x, y, z, t2 is related to its
­phasor form As1x, y, z2 according to
A1x, y, z, t2 5 Re3As1x, y, z2 ejvt4
9.1	 The flux through each turn of a 100-turn coil is 1t3 2 2t2 mWb, where t is in seconds. The
induced emf at t 5 2 s is
(a)  1 V
(d)  0.4 V
(b)  21 V
(e)  20.4 V
(c)  4 mV
9.2	 Assuming that each loop is stationary and the time-varying magnetic field B induces cur­
rent I, which of the configurations in Figure 9.17 are incorrect?
9.3	 Two conducting coils 1 and 2 (identical except that 2 is split) are placed in a uniform
magnetic field that decreases at a constant rate as in Figure 9.18. If the plane of the coils is
perpendicular to the field lines, which of the following statements is true?
(a)  An emf is induced in both coils.
(b)  An emf is induced in split coil 2.
(c)  Equal Joule heating occurs in both coils.
(d)  Joule heating does not occur in either coil.
REVIEW
QUESTIONS
FIGURE 9.17  For Review Question 9.2.
FIGURE 9.18  For Review Question 9.3.
462  CHAPTER 9  MAXWELL’S EQUATIONS
9.4	 A loop is rotating about the y-axis in a magnetic field B 5 Bo sin vt ax Wb/m2. The volt­
age induced in the loop is due to
(a)  Motional emf
(b)  Transformer emf
(c)  A combination of motional and transformer emf
(d)  None of the above
9.5	 A rectangular loop is placed in the time-varying magnetic field B 5 0.2 cos150ptaz Wb/m2
as shown in Figure 9.19. V1 is not equal to V2.
(a)  True
(b)  False
9.6	 The concept of displacement current was a major contribution attributed to
(a)  Faraday
(b)  Lenz
(c)  Maxwell
(d)  Lorenz
(e)  Your professor
9.7	 Identify which of the following expressions are not Maxwell’s equations for time-varying
fields:
(a)  = # J 1 'rv
't 5 0
(b)  = # D 5 rv
(c)  = # E 5 2'B
(d)  C
H # dl 5 3
asE 1 e 'E
't b # dS
(e)  C
B # dS 5 0
FIGURE 9.19  For Review Question 9.5.
Problems  463
9.8	 An EM field is said to be nonexistent or not Maxwellian if it fails to satisfy Maxwell’s
equations and the wave equations derived from them. Which of the following fields in free
space are not Maxwellian?
(a)  H 5 cos x cos 106t ay
(b)  E 5 100 cos vt ax
(c)  D 5 e210y sin1105t 2 10y2 az
(d)  B 5 0.4 sin 104t az
(e)  H 5 10 cos a105t 2 z
10b ax
(f)
(g)  B 5 11 2 r22 sin vt az
9.9	 Which of the following statements is not true of a phasor?
(a)  It may be a scalar or a vector.
(b)  It is a time-dependent quantity.
(c)  A phasor Vs may be represented as Vo lu or Voe jv where Vo 5 0 Vs 0 .
(d)  It is a complex quantity.
9.10	 If Es 5 10 e j4x ay, which of these is not a correct representation of E?
(a)  Re1Ese jvt2
(b)  Re1Ese2jvt2
(c)  Im1Ese jvt2
(d)  10 cos1vt 1 j4x2 ay
(e)  10 sin1vt 1 4x2 ay
Answers:  9.1b, 9.2b, d, 9.3a, 9.4c, 9.5a, 9.6c, 9.7a,c, 9.8b, d, 9.9b, 9.10d.
Sections 9.2 and 9.3—Faraday’s Law and Electromotive Forces
9.1	 A conducting circular loop of radius 20 cm lies in the z 5 0 plane in a magnetic field
B 5 10 cos 377t az mWb/m2. Calculate the induced voltage in the loop.
9.2	 The loop in Figure 9.20 exists in a magnetic field B  4cos(20t)az Wb/m2, where az is
directed out of the page. If the area enclosed by the circuit is 2 cm2, find the current i(t).
9.3	 A circuit conducting loop lies in the xy-plane as shown in Figure 9.21. The loop has
a radius of 0.2 m and resistance R  4 . If B  40 sin 104 taz mWb/m2, find the
currrent.
PROBLEMS
E 5 sin u
cos 1vt 2 rv"moeo2 au
464  CHAPTER 9  MAXWELL’S EQUATIONS
9.4	 Two conducting bars slide over two stationary rails, as illustrated in Figure 9.22. If
B  0.2az Wb/m2, determine the induced emf in the loop thus formed.
9.5	  A conductor located at 0 , y , 1.6 m moves with velocity 2ax m/s in a magnetic field,
B 5 10 cos byaz   Wb/m2 where b is a constant. Determine the induced voltage.
9.6	 A square loop of side a recedes with a uniform velocity uoay from an infinitely long fila-
ment carrying current I along az as shown in Figure 9.23. Assuming that r 5 ro at time
t 5 0, show that the emf induced in the loop at t . 0 is
Vemf 5
uoa2moI
2pr1r 1 a2
9.7	 A conducting rod moves with a constant velocity of 3 az m/s parallel to a long straight wire
carrying a current of 15 A as in Figure 9.24. Calculate the emf induced in the rod and state
which end is at the higher potential.
9.8	 A conducting rod has one end grounded at the origin, while the other end is free to move
in the z 5 0 plane.  The rod rotates at 30 rad/s in a static magnetic field B 5 60az mWb/m2.
If the rod is 8 cm long, find the voltage induced in the rod.
FIGURE 9.21  For Problem 9.3.
FIGURE 9.20  For Problem 9.2.
20 Ω
30 Ω
i(t)
FIGURE 9.22  For Problem 9.4.
1.2 m
5 m/s
15 m/s
FIGURE 9.23  For Problem 9.6.
9.9	 A rectangular coil has a cross-sectional area of 30 cm2 and 50 turns.  If the coil rotates at
60 rad/s in a magnetic field of 0.2 Wb/m2 such that its axis of rotation is perpendicular to
the direction of the field, determine the induced emf in the coil.
9.10	 Determine the induced emf in the V-shaped loop of Figure 9.25. Take B 5 0.6xaz Wb/m2
and u 5 5ax m/s. Assume that the sliding rod starts at the origin when t = 0.
9.11	 A car travels at 120 km/hr. If the earth’s magnetic field is 4.3 3 1025 Wb/m2, find the
induced voltage in the car bumper of length 1.6 m. Assume that the angle between the
earth’s magnetic field and the normal to the car is 65°.
FIGURE 9.24  For Problem 9.7.
FIGURE 9.25  For Problem 9.10.
30°
Problems  465
466  CHAPTER 9  MAXWELL’S EQUATIONS
9.12	 An airplane with a metallic wing of span 36 m flies at 410 m/s in a region where the verti­
cal component of the earth’s magnetic field is 0.4 mWb/m2. Find the emf induced on the
airplane wing.
9.13	 As portrayed in Figure 9.26, a bar magnet is thrust toward the center of a coil of 10 turns
and resistance 15 . If the magnetic flux through the coil changes from 0.45 Wb to
0.64 Wb in 0.02 s, find the magnitude and direction (as viewed from the side near the
­magnet) of the induced current.
9.14	 The cross section of a homopolar generator disk is shown in Figure 9.27. The disk has
inner radius r1 5 2 cm and outer radius r2 5 10 cm and rotates in a uniform magnetic
field 15 mWb/m2 at a speed of 60 rad/s. Calculate the induced voltage.
Section 9.4—Displacement Current
9.15	 A 50 V voltage generator at 20 MHz is connected to the plates of an air dielectric parallel-
plate capacitor with a plate area of 2.8 cm2 and a separation distance of 0.2 mm. Find the
maximum value of displacement current density and displacement current.
9.16	A dielectric material with  5 o, « 5 9«o  5 4 S/m is placed between the plates
of a parallel-plate capacitor. Calculate the frequency at which the conduction and
displacement currents are equal.
FIGURE 9.26  For Problem 9.13.
FIGURE 9.27  For Problem 9.14.
9.17	 The ratio J/Jd (conduction current density to displacement current density) is very impor­
tant at high frequencies. Calculate the ratio at 1 GHz for:
(a)  distilled water 1m 5 mo, e 5 81eo, s 5 2 3 1023 S/m2
(b)  seawater 1m 5 mo, e 5 81eo, s 5 25 S/m2
(c)  limestone 1m 5 mo, e 5 5eo, s 5 2 3 1024 S/m2
9.18	 In seawater ( 5 4 S/m, « 5 81«o,   o), find the ratio of the conduction to the dis­
placement currents at 10 MHz.
9.19	 Assume that dry soil has  5 104 S/m, «  3«o, and   o. Determine the frequency at
which the ratio of the magnitudes of the conduction current density and the displacement
current density is unity.
9.20	 In a dielectric ( 5 1024 S/m, mr 5 1, «r 5 4.5), the conduction current density is given
as Jc 5 0.4 cos12p 3 108 t2 A/m2. Determine the displacement current density.
9.21	 In a source-free region, H 5 Ho cos(wt 2 bz)ax   A/m. Find the displacement current
density.
9.22	 An ac voltage source is connected across the plates of a parallel-plate capacitor so that
E 5 25sin(103t)az    V/m. Calculate the total current crossing a 2 3 5 m area placed per­
pendicular to the electric field.  Assume that the capacitor is air filled.
Section 9.5—Maxwell’s Equations
9.23	 (a)  Write Maxwell’s equations for a linear, homogeneous medium in terms of Es and Hs,
assuming only the time factor e2jvt.
(b)  In Cartesian coordinates, write the point form of Maxwell’s equations in Table 9.2 as
eight scalar equations.
9.24	 Show that in a source-free region 1J 5 0, rv 5 02, Maxwell’s equations can be reduced to
two. Identify the two all-embracing equations.
9.25 	Show that fields
E  Eo cos x cos tay    and    H 5 Eo
sin x sin taz
do not satisfy all of Maxwell’s equations.
9.26	 Assuming a source-free region, derive the diffusion equation
=2E 5 ms 'E
9.27	 In a certain region,
J 5 12yax 1 xzay 1 z3az2 sin 104t A/m
find rv if rv1x, y, 0, t2 5 0.
Problems  467
468  CHAPTER 9  MAXWELL’S EQUATIONS
9.28	 In free space, the electric field is given by
E 5 Eo cosz costaz
Find the charge density ρv that will produce this field.
9.29 	In free space,
H 5 10 sin(108 t 1 x)ay A/m.
Find E and .
9.30	 In free space,
Find k, Jd, and H.
9.31	 The electric field intensity of a spherical wave in free space is given by
Find the corresponding magnetic field intensity H.
9.32	 In a certain region for which   0,   2o, and «  10«o
J  60 sin(109t 2 z)ax mA/m2
(a)  Find D and H.
(b)  Determine .
9.33	 Use Maxwell’s equations to derive the continuity equation.
9.34	 In a source-free region, show that
,2E 2 ms'E
't 2 me'2E
't2 5 0
9.35	 Check whether the following fields are genuine EM fields (i.e., they satisfy Maxwell’s equa­
tions). Assume that the fields exist in charge-free regions.
(a)  A 5 40 sin1vt 1 10x2az
(b)  B 5 10
r  cos1vt 2 2r2af
(c)  C 5 a3r2 cot f ar 1 cos f
afb sin vt
(d)  D 5 1
r sin u sin1vt 2 5r2au
E 5 50
r  cos1108 t 2 kz2arV/m
E 5 10
r  sin u cos1vt 2 br2au V/m
9.36	 Given the total electromagnetic energy
W 5 1
2 3 1E # D 1 H # B2 dv
show from Maxwell’s equations that
't 5 2C
1E 3 H2 # dS 2 3
E # J dv
9.37	 In air, E 5 cos(12px)sin(1011t 2 ay)az V/m. Find H and a.
9.38	 An AM radio signal propagating in free space has
E 5 Eo sin(1200pt 2 bz)ax
H 5 Eo
h  sin(1200pt 2 bz)ay
Determine  b and h.
9.39	 An antenna radiates in free space and
H 5 12 sin u
cos12p 3 108t 2 br2au mA/m
Find the corresponding E in terms of b.
Section 9.6—Time-Varying Potentials
9.40	 In free space Arv 5 0, J 5 02, show that
A 5 m0
4pr 1cos u ar 2 sin u au2e jv1t2r/c2
satisfies the wave equation in eq. (9.52). Find the corresponding V. Take c as the speed of
light in free space.
9.41	 Retrieve Faraday’s law in differential form from
E 5 2=V 2'A
9.42	 In free space, the retarded potentials are given by
V  x(z 2 ct)V,      A  x(z/c 2 t)az Wb/m
where c 
"moeo
(a)  Prove that = # A 5 moeo 'V
't .
(b)  Determine E.
9.43	 Let A 5 Ao sin(t 2 z)ax Wb/m in free space. (a) Find V and E. (b) Express b in terms
of , «o, and o.
Problems  469
470  CHAPTER 9  MAXWELL’S EQUATIONS
Section 9.7—Time-Harmonic Fields
9.44	 Evaluate the following complex numbers and express your answers in polar form:
(a)  14 li
30° 2 10 li
50°
2 1/2
(b)
1 1 j2
6 1 j8 2 7 lii
15°
(c)
13 1 j42 2
12 2 j7 1 126 1 j102*
(d)
13.6 lii
2200°
2 1/2
12.4 lii
45°
2 2125 1 j82*
9.45	 Determine the phasor forms of the following instantaneous vector fields:
(a)  H 5 210cos(106t 1 p/3)ax
(b)  E 5 4cos(4y)cos(104t 2 2x)az
(c)  D 5 5sin(104t 1 p/3)ax 2 8cos(104t 2 p/4)ay
9.46	 Find the instantaneous form for each of the following phasors:
(a)  As 5 j10ax 1 20
j ay
(b)  Bs 5 j4e2j2xax 1 6e1j2xaz
(c)  Cs 5 j2e220ze2jp/4az
9.47	 In a source-free vacuum region,
H 5 1
r cos1vt 2 3z2af A/m
(a)  Express H in phasor form.
(b)  Find the associated E field.
(c)  Determine .
9.48	 In a certain homogeneous medium, « 5 81«o, and  5 o,
Es 5 10e j(t 1 z)ay V/m
Hs 5 Hoe j(t 1 z)ax A/m
If  5 2 3 109 rad/m, find b and Ho.

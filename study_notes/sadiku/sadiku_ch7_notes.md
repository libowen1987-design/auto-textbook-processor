# Sadiku《Elements of Electromagnetics》Chapter 7

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 324-373 of 926 (926 total)

---

## Magnetostatic Fields

297
C H A P T E R
297
7.1  INTRODUCTION
In Chapters 4 to 6, we limited our discussions to static electric fields characterized by E or
D. We now focus our attention on static magnetic fields, which are characterized by H or
B. There are similarities and dissimilarities between electric and magnetic fields. As E and
D are related according to D 5 eE for linear, isotropic material space, H and B are related
according to B 5 mH. Table 7.1 further shows the analogy between electric and ­magnetic
field quantities. Some of the magnetic field quantities will be introduced later in this
­chapter, and others will be presented in the next. The analogy is presented here to show
that most of the equations we have derived for the electric fields may be ­readily used to
obtain corresponding equations for magnetic fields if the equivalent analogous quantities
are substituted. This way it does not appear as if we are learning new concepts.
A definite link between electric and magnetic fields was established by Oersted1 in
1820. As we have noticed, an electrostatic field is produced by static or stationary charges.
If the charges are moving with constant velocity, a static magnetic (or magnetostatic) field
is produced. A magnetostatic field is produced by a constant current flow (or direct cur­
rent). This current flow may be due to magnetization currents as in permanent magnets,
electron-beam currents as in vacuum tubes, or conduction currents as in current-carrying
wires. In this chapter, we consider magnetic fields in free space due to direct current.
Magnetostatic fields in material space are covered in Chapter 8.
Our study of magnetostatics is not a dispensable luxury but an indispensable necessity.
Motors, transformers, microphones, compasses, telephone bell ringers, television focusing
controls, advertising displays, magnetically levitated high-speed vehicles, memory stores,
magnetic separators, and so on, which play an important role in our everyday life,2 could
not have been developed without an understanding of magnetic phenomena.
MAGNETOSTATIC FIELDS
The highest happiness on earth is in marriage. Every man who is happily married is a
successful man even if he has failed in everything else.
—WILLIAM L. PHELPS
1Hans Christian Oersted (1777–1851), a Danish professor of physics, after 13 years of frustrating efforts discov­
ered that electricity could produce magnetism.
2Various applications of magnetism can be found in J. K. Watson, Applications of Magnetism. New York: John
Wiley & Sons, 1980.
298  CHAPTER 7  MAGNETOSTATIC FIELDS
There are two major laws governing magnetostatic fields: (1) Biot–Savart’s law,3 and (2)
Ampère’s circuit law. Like Coulomb’s law, Biot–Savart’s law is the general law of magnetostatics.
Just as Gauss’s law is a special case of Coulomb’s law, Ampère’s law is a special case of Biot–Savart’s
law and is easily applied in problems involving symmetrical current distribution. The two laws of
magnetostatics are stated and applied first, with their derivations provided later in the chapter.
TABLE 7.1  Analogy between Electric and Magnetic Fields*
Term
Electric
Magnetic
Basic laws
F 5 Q1Q2
4peR2 aR
dB 5
moI dl 3 aR
4pR2
C D # dS 5 Qenc
C H # dl 5 Ienc
Force law
F 5 QE
F 5 Qu 3 B
Source element
dQu 5 Idl
Field intensity
E 5 V
, 1V/m2
H 5 I
, 1A/m2
Flux density
D 5
S 1C/m22
B 5
S 1Wb/m22
Relationship between fields
D 5 eE
B 5 mH
Potentials
E 5 2=V
H 5 2=Vm 1J 5 02
V 5 3
rLdl
4peR
A 5 3
Flux
c 5 e D # dS
c 5 eS B # dS
c 5 Q 5 CV
c 5 LI
I 5 C dV
V 5 L dI
Energy density
wE 5 1
2 D # E
wm 5 1
2 B # H
Poisson’s equation
=2V 5 2
=2A 5 2mJ
*A similar analogy can be found in R. S. Elliot, “Electromagnetic theory: a simplified representation,”
IEEE Transactions on Education, vol. E-24, no. 4, Nov. 1981, pp. 294–296.
7.2  BIOT–SAVART’S LAW
Biot–Savart’s law states that the differential magnetic field intensity dH produced at a
point P, as shown in Figure 7.1, by the differential current element I dl is proportional
to the product I dl and the sine of the angle a between the element and the line joining
P to the element and is inversely proportional to the square of the distance R between
P and the element.
3The experiments and analyses of the effect of a current element were carried out by Ampère and by
Jean-Baptiste Biot and Felix Savart around 1820.
m I d,
4pR
7.2 Biot–Savart’s Law  299
That is,
dH ~  I dl sin a
(7.1)
dH 5 kI dl sin a
(7.2)
where k is the constant of proportionality. In SI units, k 5 1/4p, so eq. (7.2) becomes
dH 5 I dl sin a
4pR2 
(7.3)
From the definition of cross product in eq. (1.21), it is easy to notice that eq. (7.3) is
better put in vector form as
dH 5 I dl 3 aR
4pR2
5 I dl 3 R
4pR3 
(7.4)
where R 5 0 R 0  and aR 5 R/R; R and dl are illustrated in Figure 7.1. Thus the direction
of dH can be determined by the right-hand rule with the right-hand thumb pointing in
the ­direction of the current and the right-hand fingers encircling the wire in the direction
of dH as shown in Figure 7.2(a). Alternatively, we can use the right-handed-screw rule to
­determine the direction of dH: with the screw placed along the wire and pointed in the
­direction of current flow, the direction of rotation of the screw is the direction of dH as in
Figure 7.2(b).
It is customary to represent the direction of the magnetic field intensity H (or current I)
by a small circle with a dot or cross sign depending on whether H (or I) is out of the page,
or into it respectively, as illustrated in Figure 7.3.
Just as we can have different charge configurations (see Figure 4.5), we can have dif­
ferent current distributions: line current, surface current, and volume current as shown in
Figure 7.4. If we define K as the surface current density in amperes per meter and J as the
volume current density in amperes per meter squared, the source elements are related as
I dl ; K dS ; J dv
(7.5)
FIGURE 7.1  Magnetic field dH at P due to
current element I dl.
300  CHAPTER 7  MAGNETOSTATIC FIELDS
H 5 3
I dl 3 aR
4pR2   1line current2
(7.6)
H 5 3
K dS 3 aR
4pR2   1surface current2
(7.7)
H 5 3  J dv 3 aR
4pR2   1volume current2
(7.8)
where aR is a unit vector pointing from the differential element of current to the point of
­interest.
As an example, let us apply eq. (7.6) to determine the field due to a straight current-
carrying filamentary conductor of finite length AB as in Figure 7.5. We assume that the
FIGURE 7.2  Determining the direction of
dH using (a) the right-hand rule or (b) the
right-handed-screw rule.
FIGURE 7.3  Conventional repre­
sentation of H (or I) (a) out of the
page and (b) into the page.
FIGURE 7.4  Current distributions: (a) line current,
(b) surface current, (c) volume current.
Thus in terms of the distributed current sources, the Biot–Savart’s law as in eq. (7.4)  becomes
7.2 Biot–Savart’s Law  301
­conductor is along the z-axis with its upper and lower ends, respectively, subtending angles
a2 and a1 at P, the point at which H is to be determined. Particular note should be taken of
this assumption, as the formula to be derived will have to be applied accordingly. Note that
current flows from point A, where a 5 a1, to point B, where a 5 a2. If we consider the
contribution dH at P due to an element dl at 10, 0, z2,
dH 5 I dl 3 R
4pR3 
(7.9)
But dl 5 dz az and R 5 rar 2 zaz, so
dl 3 R 5 r dz af
(7.10)
Hence,
H 5 3
Ir dz
4p3r2 1 z243/2 af
(7.11)
Letting z 5 r cot a, dz 5 2r csc2 a da, 3r2 1 z243/2 5 r3 csc a3, and eq. (7.11) becomes
H 5 2 1
4p 3
r2 csc2 a da
r3 csc3 a  af
5 2 I
4pr af 3
sin a da
H 5
4pr 1cos a2 2 cos a12af
(7.12)
FIGURE 7.5  Field at point P due to a straight fila­
mentary conductor.
302  CHAPTER 7  MAGNETOSTATIC FIELDS
This expression is generally applicable for any straight filamentary conductor. The
­conductor need not lie on the z-axis, but it must be straight. Notice from eq. (7.12) that
H is always along the unit vector af (i.e., along concentric circular paths) irrespective of
the length of the wire or the point of interest P. As a special case, when the conductor is
semi-infinite (with respect to P) so that point A is now at O10, 0, 02 while B is at 10, 0, `2,
a1 5 90°, a2 5 0°, and eq. (7.12) becomes
H 5
4pr af
(7.13)
Another special case is found when the conductor is infinite in length. For this case, point
A is at 10, 0, 2`2 while B is at 10, 0, `2; a1 5 180°, a2 5 0°, and eq. (7.12) reduces to
H 5
2pr af
(7.14)
To find unit vector af in eqs. (7.12) to (7.14) is not always easy. A simple approach is to
determine af from
af 5 a, 3 ar
(7.15)
where a is a unit vector along the line current and ar is a unit vector along the perpendicu­
lar line from the line current to the field point.
The conducting triangular loop in Figure 7.6(a) carries a current of 10 A. Find H at
10, 0, 52 due to side 1 of the loop.
Solution:
This example illustrates how eq. (7.12) is applied to any straight, thin, current-carrying
conductor. The key point to keep in mind in applying eq. (7.12) is figuring out a1, a2, r, and
af. To find H at 10, 0, 52 due to side 1 of the loop in Figure 7.6(a), consider Figure 7.6(b),
where side 1 is treated as a straight conductor. Notice that we join the point of interest
10, 0, 52 to the beginning and end of the line current. Observe that a1, a2, and r are assigned
in the same manner as in Figure 7.5 on which eq. (7.12) is based:
cos a1 5 cos 90° 5 0,  cos a2 5
"29
,  r 5 5
To determine af is often the hardest part of applying eq. (7.12). According to eq. (7.15),
a, 5 ax and ar 5 az, so
af 5 ax 3 az 5 2ay
EXAMPLE 7.1
7.2 Biot–Savart’s Law  303
Hence,
H1 5
4pr1cos a2 2 cos a12af 5
4p152 a
"29
2 0b 12ay2
5 259.1ay mA/m
PRACTICE EXERCISE  7.1
Find H at 10, 0, 52 due to side 3 of the triangular loop in Figure 7.6(a).
Answer:  230.63ax 1 30.63ay mA/m.
Find H at 123, 4, 02 due to the current filament shown in Figure 7.7(a).
Solution:
Let H 5 H1 1 H2, where H1 and H2 are the contributions to the magnetic field intensity at
P123, 4, 02 due to the portions of the filament along x and z, respectively.
H2 5
4pr1cos a2 2 cos a12af
10 A
(a)
10 A
(b)
FIGURE 7.6  For Example 7.1: (a) conducting triangular loop, (b) side 1 of the loop.
EXAMPLE 7.2
At PA23, 4, 0B, r 5 A9 1 16B1/2 5 5, a1 5 90°, a2 5 0°, and af is obtained as a unit vector
along the circular path through P on plane z 5 0 as in Figure 7.7(b). The direction of af
304  CHAPTER 7  MAGNETOSTATIC FIELDS
is determined using the right-handed-screw rule or the right-hand rule. From the geom­
etry in Figure 7.7(b),
af 5 sin u ax 1 cos u ay 5 4
5 ax 1 3
5 ay
Alternatively, we can determine af from eq. (7.15). At point P, a and ar are as illustrated
in Figure 7.7(a) for H2. Hence,
af 5 2az 3 a23
5 ax 1 4
5 ayb 5 4
5 ax 1 3
5 ay
as obtained before. Thus
H2 5
4p152 11 2 02
14ax 1 3ay2
5 38.2ax 1 28.65ay mA/m
It should be noted that in this case af happens to be the negative of the regular af of cylin­
drical coordinates. H2 could have also been obtained in cylindrical coordinates as
H2 5
4p152 11 2 02 12af2
5 247.75af mA/m
Similarly, for H1 at P, r 5 4, a2 5 0°, cos a1 5 3/5, and af 5 az or af 5 a, 3
ar 5 ax 3 ay 5 az. Hence,
H1 5
4p142  a1 2 3
5b az
5 23.87az mA/m
3 A
3 A
FIGURE 7.7  For Example 7.2: (a) current filament along semi-infinite
x- and z-axes, a and ar for H2 only; (b) determining ar for H2.
7.2 Biot–Savart’s Law  305
Thus
H 5 H1 1 H2 5 38.2ax 1 28.65ay 1 23.87az mA/m
H 5 247.75af 1 23.87az mA/m
Notice that although the current filaments appear to be semi-infinite (they occupy
the positive z- and x-axes), it is only the filament along the z-axis that is semi-infinite with
respect to point P. Thus H2 could have been found by using eq. (7.13), but the equation
could not have been used to find H1 because the filament along the x-axis is not semi-­
infinite with respect to P.
PRACTICE EXERCISE  7.2
The positive y-axis (semi-infinite line with respect to the origin) carries a filamentary
current of 2 A in the 2ay direction. Assume it is part of a large circuit. Find H at
(a)  A12, 3, 02
(b)  B13, 12, 242
Answer:  (a) 145.8az mA/m,  (b) 48.97ax 1 36.73az mA/m.
A circular loop located on x2 1 y2 5 9, z 5 0 carries a direct current of 10 A along af.
Determine H at 10, 0, 42 and 10, 0, 242.
Solution:
Consider the circular loop shown in Figure 7.8(a). The magnetic field intensity dH at point
P10, 0, h2 contributed by current element I dl is given by Biot–Savart’s law:
d H 5 I dl 3 R
4pR3
where dl 5 r df af, R 5 10, 0, h2 2 1x, y, 02 5 2rar 1 haz, and
Hence,
d H 5
4p3r2 1 h243/2 1rh df ar 1 r2 df az2 5 dHr ar 1 dHz az
EXAMPLE 7.3
dl 3 R 5 †
r df
† 5 rh df ar 1 r2 df az
306  CHAPTER 7  MAGNETOSTATIC FIELDS
By symmetry, the contributions along ar add up to zero because the radial components pro­
duced by current element pairs 180° apart cancel. This may also be shown mathematically
by writing ar in rectangular coordinate systems (i.e., ar 5 cos f ax 1 sin f ay). Integrating
cos f or sin f over 0 # f # 2p gives zero, thereby showing that Hr  0. Thus
H 5 3 dHz az 5 3
Ir2 df az
4p3r2 1 h243/2 5
Ir22paz
4p3r2 1 h243/2
H 5
Ir2az
23r2 1 h243/2
(a)	 Substituting I 5 10 A, r 5 3, h 5 4 gives
H10, 0, 42 5
10132 2az
239 1 1643/2 5 0.36az A/m
(b)	 Notice from dl 3 R in the Biot–Savart law that if h is replaced by 2h, the ­z-component
of dH remains the same while the r-component still adds up to zero due to the axial sym­
metry of the loop. Hence
H10, 0, 242 5 H10, 0, 42 5 0.36az A/m
The flux lines due to the circular current loop are sketched in Figure 7.8(b).
FIGURE 7.8  For Example 7.3: (a) circular current loop, (b) flux lines
due to the current loop.
7.2 Biot–Savart’s Law  307
PRACTICE EXERCISE  7.3
A thin ring of radius 5 cm is placed on plane z 5 1 cm so that its center is at 10, 0, 1 cm2.
If the ring carries 50 mA along af, find H at
(a)  10, 0, 21 cm2
(b)  10, 0, 10 cm2
Answer: (a) 400az mA/m, (b) 57.3az mA/m.
A solenoid of length  and radius a consists of N turns of wire carrying current I. Show
that at point P along its axis,
H 5 nI
2 1cos u2 2 cos u12az
where n 5 N/,, u1 and u2 are the angles subtended at P by the end turns as illustrated in
Figure 7.9. Also show that if , W a, at the center of the solenoid,
H 5 nIaz
Solution:
Consider the cross section of the solenoid as shown in Figure 7.9. Since the solenoid con­
sists of circular loops, we apply the result of Example 7.3. The contribution to the magnetic
field H at P by an element of the solenoid of length dz is
dHz 5
I dl a2
23a2 1 z243/2 5
Ia2n dz
23a2 1 z243/2
where dl 5 n dz 5 1N/,2 dz. From Figure 7.9, tan u 5 a/z; that is,
dz 5 2a csc2 u du 5 2
3z2 1 a243/2
sin u du
FIGURE 7.9  For Example 7.4; cross
section of a solenoid.
EXAMPLE 7.4
308  CHAPTER 7  MAGNETOSTATIC FIELDS
Hence,
dHz 5 2nI
2  sin u du
Hz 5 2nI
2  3
sin u du
Thus
H 5 nI
2  1cos u2 2 cos u12az
as required. Substituting n 5 N/, gives
H 5 NI
2, 1cos u2 2 cos u12az
At the center of the solenoid,
cos u2 5
,/2
3a2 1 ,2/441/2 5 2cos u1
and
H 5
In,
23a2 1 ,2/441/2 az
If , W a or u2 . 0°, u1 . 180°,
H 5 nI az 5 NI
,  az
PRACTICE EXERCISE  7.4
The solenoid of Figure 7.9 has 2000 turns, a length of 75 cm, and a radius of 5 cm. If it
carries a current of 50 mA along af, find H at
(a)  10, 0, 02
(b)  10, 0, 75 cm2
(c)  10, 0, 50 cm2
Answer:  (a) 66.52az A/m,  (b) 66.52az A/m,  (c) 131.7az A/m.
7.4 Applications of Ampère’s Law  309
Ampère’s circuit law states that the line integral of H around a closed path is the
same as the net current Ienc enclosed by the path.
In other words, the circulation of H equals Ienc; that is,
H # dl 5 Ienc
(7.16)
By applying Stokes’s theorem to the left-hand side of eq. (7.16), we obtain
Ienc 5 C
H # dl 5 3
1= 3 H2 # dS
(7.17)
But
Ienc 5 3
J # dS
(7.18)
Comparing the surface integrals in eqs. (7.17) and (7.18) clearly reveals that
= 3 H 5 J
(7.19)
7.3  AMPÈRE’S CIRCUIT LAW—MAXWELL’S EQUATION
7.4  APPLICATIONS OF AMPÈRE’S LAW
We now apply Ampère’s circuit law to determine H for some symmetrical current distri­
butions as we did for Gauss’s law. We will consider an infinite line current, an infinite ­
sheet of current, and an infinitely long coaxial transmission line. In each case, we apply
ALH # dl 5 Ienc. For symmetrical current distribution, H is either parallel or perpendicular
to dl. When H is parallel to dl, 0H0 5 constant.
Ampère’s law is similar to Gauss’s law, since Ampère’s law is easily applied to determine
H when the current distribution is symmetrical. It should be noted that eq. (7.16) always
holds regardless of whether the current distribution is symmetrical or not, but we can use
the equation to determine H only when a symmetrical current distribution exists. Ampère’s
law is a special case of Biot–Savart’s law; the former may be derived from the latter.
This is the third Maxwell’s equation to be derived; it is essentially Ampère’s law in differ-
ential (or point) form, whereas eq. (7.16) is the integral form. From eq. (7.19), we should
observe that = 3 H 5 J 2 0; that is, a magnetostatic field is not conservative.
310  CHAPTER 7  MAGNETOSTATIC FIELDS
A.  Infinite Line Current
Consider an infinitely long filamentary current I along the z-axis as in Figure 7.10. To
determine H at an observation point P, we allow a closed path to pass through P. This path,
on which Ampère’s law is to be applied, is known as an Amperian path (analogous to the
term “Gaussian surface”). We choose a concentric circle as the Amperian path in view of
eq. (7.14), which shows that H is constant provided r is constant. Since this path encloses
the whole current I, according to Ampère’s law,
H 5
2pr af
(7.20)
as expected from eq. (7.14).
B.  Infinite Sheet of Current
Consider an infinite current sheet in the z 5 0 plane. If the sheet has a uniform current
density K 5 Kyay A/m as shown in Figure 7.11, applying Ampère’s law to the rectangular
closed path 1-2-3-4-1 (Amperian path) gives
C H # dl 5 Ienc 5 Kyb
(7.21a)
FIGURE 7.10  Ampère’s law applied to an infinite fila­
mentary line current.
To evaluate the integral, we first need to have an idea of what H is like. To achieve this, we
regard the infinite sheet as comprising filaments; dH above or below the sheet due to a pair
of filamentary currents can be found by using eqs. (7.14) and (7.15). As evident in Figure
7.11(b), the resultant dH has only an x-component. Also, H on one side of the sheet is the
negative of that on the other side. Owing to the infinite extent of the sheet, the sheet can be
I 5 3  Hfaf # r df af 5 Hf 3  r df 5 Hf # 2pr
7.4 Applications of Ampère’s Law  311
H 5 eHoax
z . 0
2Hoax
z , 0
(7.21b)
where Ho is yet to be determined. Evaluating the line integral of H in eq. (7.21a) along the
closed path in Figure 7.11(a) gives
C H # dl 5 a3
1 3
1 3
1 3
b H # dl
5 012a2 1 12Ho2 12b2 1 01a2 1 Ho1b2
(7.21c)
5 2Hob
From eqs. (7.21a) and (7.21c), we obtain Ho 5 1
2 Ky. Substituting Ho in eq. (7.21b) gives
H 5 µ
2 Kyax,
z . 0
2 Kyax,
z , 0
(7.22)
In general, for an infinite sheet of current density K A/m,
H 5 1
2 K 3 an
(7.23)
where an is a unit normal vector directed from the current sheet to the point of interest.
K = Kyay
Amperian path
(a)
dH1
dH2
dH1
dH2
(b)
FIGURE 7.11  Application of Ampère’s law to an infinite sheet: (a) closed path 1-2-3-4-1, (b)
symmetrical pair of current filaments with current along ay.
regarded as consisting of such filamentary pairs so that the characteristics of H for a pair
are the same for the infinite current sheet, that is,
312  CHAPTER 7  MAGNETOSTATIC FIELDS
C.  Infinitely Long Coaxial Transmission Line
Consider an infinitely long transmission line consisting of two concentric cylinders hav­
ing their axes along the z-axis. The cross section of the line is shown in Figure 7.12, where
the z-axis is out of the page. The inner conductor has radius a and carries current I, while
the outer conductor has inner radius b and thickness t and carries return current I.
We want to determine H everywhere, assuming that current is uniformly distributed in
both conductors. Since the current distribution is symmetrical, we apply Ampère’s law
along the ­Amperian path for each of the four possible regions: 0 # r # a, a # r # b,
b # r # b 1 t, and r $ b 1 t.
For region 0 # r # a, we apply Ampère’s law to path L1, giving
H # dl 5 Ienc 5 3
J # dS
(7.24)
Since the current is uniformly distributed over the cross section,
J 5
pa2 az,  dS 5 r df dr az
Ienc 5 3
J # dS 5
pa2 3
f503
r50
r df dr 5  I
pa2 pr2 5 Ir2
Hence eq. (7.24) becomes
Hf 3
dl 5 Hf 2pr 5 Ir2
Hf 5
2pa2
(7.25)
FIGURE 7.12  Cross section of
the transmission line; the positive
­z-direction is out of the page.
7.4 Applications of Ampère’s Law  313
For region a # r # b, we use path L2 as the Amperian path,
H # dl 5 Ienc 5 I
Hf2pr 5 I
Hf 5
2pr
(7.26)
since the whole current I is enclosed by L2. Notice that eq. (7.26) is the same as eq. (7.14),
and it is independent of a. For region b # r # b 1 t, we use path L3, getting
H # dl 5 Hf # 2pr 5 Ienc
(7.27a)
where
Ienc 5 I 1 3 J # dS
and J in this case is the current density (current per unit area) of the outer conductor and
is along 2az, that is,
J 5 2
p3 1b 1 t2 2 2 b24 az
Thus
Ienc 5 I 2
p3 1b 1 t2 2 2 b24 3
f50
r5b
r dr df
5 Ic1 2 r2 2 b2
t2 1 2bt d
Substituting this in eq. (7.27a), we have
Hf 5
2pr c1 2 r2 2 b2
t2 1 2bt d
(7.27b)
For region r $ b 1 t, we use path L4, getting
H # dI 5 I 2 I 5 0
314  CHAPTER 7  MAGNETOSTATIC FIELDS
Hf 5 0
(7.28)
Putting eqs. (7.25) to (7.28) together gives
H 5 g
2pa2 af,
0 # r # a
2pr af,
a # r # b
2pr c1 2 r2 2 b2
t2 1 2bt d  af,
b # r # b 1 t
r $ b 1 t
(7.29)
The magnitude of H is sketched in Figure 7.13.
From these examples, it can be observed that the ability to take H from under the
integral sign is the key to using Ampère’s law to determine H. In other words, Ampère’s law
can be used to find H only due to symmetric current distributions for which it is possible
to find a closed path over which H is constant in magnitude.
Planes z 5 0 and z 5 4 carry current K 5 210ax A/m and K 5 10ax A/m, respectively.
Determine H at
(a)  11, 1, 12
(b)  10, 23, 102
Solution:
The parallel current sheets are shown in Figure 7.14. Let
H 5 Ho 1 H4
FIGURE 7.13  Plot of Hf against r.
EXAMPLE 7.5
7.4 Applications of Ampère’s Law  315
EXAMPLE 7.6
where Ho and H4 are the contributions due to the current sheets z 5 0 and z 5 4, respec­
tively. We make use of eq. (7.23).
(a)	 At 11, 1, 12, which is between the plates 10 , z 5 1 , 42,
Ho 5 1/2 K 3 an 5 1/21210ax2 3 az 5 5ay A/m
H4 5 1/2 K 3 an 5 1/2110ax2 3 12az2 5 5ay A/m
Hence,
H 5 10ay A/m
(b)	 At 10, 23, 102, which is above the two sheets 1z 5 10 . 4 . 02,
Ho 5 1/21210ax2 3 az 5 5ay A/m
H4 5 1/2110ax2 3 az 5 25ay A/m
Hence,
H 5 0 A/m
PRACTICE EXERCISE  7.5
Plane y 5 1 carries current K 5 50az mA/m. Find H at
(a)  10, 0, 02
(b)  11, 5, 232
Answer:  (a) 25ax mA/m,  (b) 225ax mA/m.
A toroid whose dimensions are shown in Figure 7.15 has N turns and carries current I.
­Determine H inside and outside the toroid.
Solution:
We apply Ampère’s circuit law to the Amperian path, which is a circle of radius r shown
dashed in Figure 7.15. Since N wires cut through this path each carrying current I, the net
current enclosed by the Amperian path is NI. Hence,
FIGURE 7.14  For Example 7.5: par­
allel infinite current sheets.
316  CHAPTER 7  MAGNETOSTATIC FIELDS
C H # dl 5 Ienc S  H # 2pr 5 NI
H 5 NI
2pr,  for  ro 2 a , r , ro 1 a
where ro is the mean radius of the toroid as shown in Figure 7.15. An approximate value of H is
Happrox 5
2pro
5 NI
Notice that this is the same as the formula obtained for H for points well inside a very
long solenoid 1, W a2. Thus a straight solenoid may be regarded as a special toroidal
coil for which ro S  `. Outside the toroid, the current enclosed by an Amperian path is
NI 2 NI 5 0 and hence H 5 0.
PRACTICE EXERCISE  7.6
A toroid of circular cross section whose center is at the origin and axis the same as the
z-axis has 1000 turns with ro 5 10 cm, a 5 1 cm. If the toroid carries a 100 mA cur-
rent, find 0H 0  at
(a)  13 cm, 24 cm, 02
(b)  16 cm, 9 cm, 02
Answer:  (a) 0,  (b) 147.1 A/m.
FIGURE 7.15  For Example 7.6: a toroid with a circular cross
section.
7.5 Magnetic Flux Density—Maxwell’s Equation  317
The magnetic flux density B is similar to the electric flux density D. As D 5 eoE in free
space, the magnetic flux density B is related to the magnetic field intensity H according to
B 5 moH
(7.30)
per meter (H/m) and has the value of
mo 5 4p 3 1027 H/m
(7.31)
The precise definition of the magnetic flux density B, in terms of the magnetic force, will
be given in the next chapter.
The magnetic flux through a surface S is given by
where the magnetic flux Ψ is in webers (Wb) and the magnetic flux density is in webers per
square meter (Wb/m2) or teslas (T).
A magnetic flux line is a path to which B is tangential at every point on the line. It is
a line along which the needle of a magnetic compass will orient itself if placed in the pres­
ence of a magnetic field. For example, the magnetic flux lines due to a straight long wire are
shown in Figure 7.16. The flux lines are determined by using the same principle followed
in Section 4.10 for the electric flux lines. The direction of B is taken as that indicated as
“north” by the needle of the magnetic compass. Notice that each flux line is closed and has
no beginning or end. Though Figure 7.16 is for a straight, current-carrying conductor, it is
generally true that magnetic flux lines are closed and do not cross each other regardless of
the current distribution.
7.5  MAGNETIC FLUX DENSITY—MAXWELL’S EQUATION
FIGURE 7.16  Magnetic flux lines due to a
straight wire with current coming out of the page.
 5 3
B # dS
(7.32)
where m  is a constant known as the permeability of free space. The constant is in Henrys
318  CHAPTER 7  MAGNETOSTATIC FIELDS
sarily closed. Unlike electric flux lines, magnetic flux lines always close upon themselves
as in Figure 7.17(b). This is because it is not possible to have isolated magnetic poles (or
magnetic charges). For example, if we desire to have an isolated magnetic pole by dividing
a magnetic bar successively into two, we end up with pieces each having north and south
poles as illustrated in Figure 7.18. We find it impossible to separate the north pole from
the south pole.
An isolated magnetic charge does not exist.
Thus the total flux through a closed surface in a magnetic field must be zero; that is,
B # dS 5 0
(7.33)
FIGURE 7.17  Flux leaving a closed surface due to (a) isolated electric
charge c 5 AS D # dS 5 Q, (b) magnetic charge, c 5 AS B # dS 5 0.
FIGURE 7.18  Successive division of a bar magnet results in pieces
with north and south poles, showing that magnetic poles cannot
be isolated.
In an electrostatic field, the flux passing through a closed surface is the same as the
charge enclosed; that is,
5 AS D # dS 5 Q. Thus it is possible to have an isolated electric
charge as shown in Figure 7.17(a), which also reveals that electric flux lines are not neces-
7.6 Maxwell’s Equations for Static Fields  319
This equation is referred to as the law of conservation of magnetic flux or Gauss’s law for
magnetostatic fields, just as
is Gauss’s law for electrostatic fields. Although
the magnetostatic field is not conservative, magnetic flux is conserved.
By applying the divergence theorem to eq. (7.33), we obtain
B # dS 5 3
= # B dv 5 0
= # B 5 0
(7.34)
This equation is the fourth Maxwell’s equation to be derived. Equation (7.33) or (7.34)
shows that magnetostatic fields have no sources or sinks. Equation (7.34) suggests that
magnetic field lines are always continuous.
7.6  MAXWELL’S EQUATIONS FOR STATIC FIELDS
Having derived Maxwell’s four equations for static fields, we may take a moment to put
them together as in Table 7.2. From the table, we notice that the order in which the equa­
tions are presented differs from the order in which they were derived. This was done for
the sake of clarity.
The choice between differential and integral forms of the equations depends on a given
problem. It is evident from Table 7.2 that a vector field is defined completely by specify­
ing its curl and its divergence. A field can be electric or magnetic only if it satisfies the
corresponding Maxwell equations (see Problems 7.
and 7.
). It should be noted that
Maxwell’s equations as in Table 7.2 are only for static electric and magnetic fields. As will
be discussed in Chapter 9, the divergence equations will remain the same for time-varying
EM fields, but the curl equations will have to be modified.
TABLE 7.2  Maxwell’s Equations for Static Electric and Magnetic Fields
Differential (or Point) Form
Integral Form
Remarks
= # D 5 rv
D # dS 5 3
rv dv
Gauss’s law
= # B 5 0
B # dS 5 0
Nonexistence of magnetic monopole
= 3 E 5 0
E # dl 5 0
Conservative nature of electrostatic field
= 3 H 5 J
H # dl 5 3
J # dS
Ampère’s law
AS D # dS 5 Q
320  CHAPTER 7  MAGNETOSTATIC FIELDS
We recall that some electrostatic field problems were simplified by relating the electric
potential V to the electric field intensity E1E 5 2=V2. Similarly, we can define a potential
associated with magnetostatic field B. In fact, the magnetic potential could be scalar Vm or
vector A. To define Vm and A involves recalling two important identities (see Example 3.10
and Practice Exercise 3.10):
= 3 1=V2 5 0
(7.35a)
= # 1= 3 A2 5 0
(7.35b)
which must always hold for any scalar field V and vector field A.
Just as E 5 2=V, we define the magnetic scalar potential Vm (in amperes) as related
to H according to
H 5 2=Vm      if J 5 0
(7.36)
The condition attached to this equation is important and will be explained. Combining
eq. (7.36) and eq. (7.19) gives
J 5 = 3 H 5 = 3 12=Vm2 5 0
(7.37)
since Vm must satisfy the condition in eq. (7.35a). Thus the magnetic scalar potential Vm is
only defined in a region where J 5 0 as in eq. (7.36). We should also note that Vm satisfies
Laplace’s equation just as V does for electrostatic fields; hence,
=2Vm 5 0,  1J 5 02
(7.38)
We know that for a magnetostatic field, = # B 5 0 as stated in eq. (7.34). To satisfy
Wb/m) such that
B 5 = 3 A
(7.39)
Just as we defined
V 5 3 dQ
4peoR
(7.40)
we can define
A 5 3
moI dl
4pR       for line current
(7.41)
7.7  MAGNETIC SCALAR AND VECTOR POTENTIALS
eqs. (7.34) and (7.35b) simultaneously, we can define the magnetic vector potential A (in
7.7 Magnetic Scalar and Vector Potentials  321
A 5 3
moK dS
4pR       for surface current
(7.42)
A 5 3
moJ dv
4pR       for volume current
(7.43)
Rather than obtaining eqs. (7.41) to (7.43) from eq. (7.40), an alternative approach
would be to obtain eqs. (7.41) to (7.43) from eqs. (7.6) to (7.8). For example, we can derive
eq. (7.41) from eq. (7.6) in conjunction with eq. (7.39). To do this, we write eq. (7.6) as
B 5 mo
4p 3
I dlr 3 R
(7.44)
where R is the distance vector from the line element dl at the source point 1xr, yr, zr2 to
the field point 1x, y, z2 as shown in Figure 7.19 and R 5 0 R 0 , that is,
R 5 0 r 2 r9 0 5 3 1x 2 xr2 2 1 1y 2 yr2 2 1 1z 2 zr2 241/2
(7.45)
Hence,
=a 1
Rb 5 2
1x 2 xr2ax 1 1y 2 yr2ay 1 1z 2 zr2az
3 1x 2 xr2 2 1 1y 2 yr2 2 1 1z 2 zr2 243/2 5 2 R
R3 5 2=a 1
Rb  a5 aR
R2b
(7.46)
where the differentiation is with respect to x, y, and z. Substituting this into eq. (7.44), we
obtain
B 5 2mo
4p 3
I dlr 3 =a 1
Rb
(7.47)
FIGURE 7.19  Illustration of the source point
(x, y, z) and the field point (x, y, z).
322  CHAPTER 7  MAGNETOSTATIC FIELDS
We apply the vector identity
= 3 1 f F2 5 f = 3 F 1 1=f 2 3 F
(7.48)
where f is a scalar field and F is a vector field. Taking f 5 1/R and F 5 dlr, we have
dlr 3 =a 1
Rb 5 1
R= 3 dlr 2 = 3 adlr
R b
Since  operates with respect to 1x, y, z2 while dl is a function of 1xr, yr, zr2, = 3 dlr 5 0.
Hence,
dlr 3 =a 1
Rb 5 2= 3 dlr
R 
(7.49)
With this equation, eq. (7.47) reduces to
B 5 = 3 3
moI dlr
4pR 
(7.50)
Comparing eq. (7.50) with eq. (7.39) shows that
A 5 3
moI dlr
4pR
Thus the magnetic flux through a given area can be found by using either eq. (7.32)
or (7.51). Also, the magnetic field can be determined by using either Vm or A; the
choice is dictated by the nature of the given problem except that Vm can be used only
in a source-free region. The use of the magnetic vector potential provides a powerful,
elegant approach to solving EM problems, particularly those relating to antennas. As we
shall notice in Chapter 13, it is more convenient to find B by first finding A in antenna
problems­.
verifying eq. (7.41).
By substituting eq. (7.39) into eq. (7.32) and applying Stokes’s theorem, we obtain
 5 3
B # dS 5 3
1= 3 A2 # dS 5 C
A # dl
 5 C
A # dl
(7.51)
7.7 Magnetic Scalar and Vector Potentials  323
Given the magnetic vector potential A 5 2r2/4 az Wb/m, calculate the total magnetic flux
crossing the surface f 5 p/2, 1 # r # 2 m, 0 # z # 5 m.
Solution:
We can solve this problem in two different ways: using eq. (7.32) or eq. (7.51).
Method 1:
B 5 = 3 A 5 2'Az
'r  af 5 r
2 af,  dS 5 dr dz af
FIGURE 7.20  For Example 7.7.
EXAMPLE 7.7
Hence,
 5 3
B # dS 5 1
2 3
z50
r51
r dr dz 5 1
4 r2 `
152 5 15
 5 3.75 Wb
Method 2:
We use
 5 C
A # dl 5 1 1 2 1 3 1 4
where L is the path bounding surface S; Ψ1, Ψ2, Ψ3, and Ψ4 are, respectively, the evalua-
tions of eLA # dl along the segments of L labeled 1 to 4 in Figure 7.20. Since A has only a
z-component,
1 5 0 5 3
324  CHAPTER 7  MAGNETOSTATIC FIELDS
That is,
as obtained by Method 1. Note that the direction of the path L must agree with that of dS.
PRACTICE EXERCISE  7.7
A current distribution gives rise to the vector magnetic potential A 5 x2yax 1
y2x ay 2 4xyz az Wb/m. Calculate the following:
(a)  B at 121, 2, 52
(b)  The flux through the surface defined by z 5 1, 0 # x # 1, 21 # y # 4
Answer:  (a) 20ax 1 40ay 1 3az Wb/m2,  (b) 20 Wb.
If plane z 5 0 carries uniform current K 5 Kyay,
H 5 e1/2 Kyax,
z . 0
21/2 Kyax,
z , 0
This was obtained in Section 7.4 by using Ampère’s law. Obtain this by using the concept
of vector magnetic potential.
Solution:
Consider the current sheet as in Figure 7.21. From eq. (7.42),
dA 5 moK dS
4pR
In this problem, K 5 Kyay, dS 5 dxr dyr, and for z . 0,
R 5 0 R 0 5 0 10, 0, z2 2 1xr, yr, 02 0
5 3 1xr2 2 1 1yr2 2 1 z241/2
(7.8.1)
where the primed coordinates are for the source point while the unprimed coordinates
are for the field point. It is necessary (and customary) to distinguish between the two
points to avoid confusion (see Figure 7.19). Hence
EXAMPLE 7.8
 5 2 1 4 5 21
c 112 2 3
dz 1 122 2 3
dzd
5 21
4 11 2 42 152 5 15
5 3.75 Wb
7.7 Magnetic Scalar and Vector Potentials  325
dA 5
moKy dxr dyr ay
4p3 1xr2 2 1 1yr2 2 1 z241/2
dB 5 = 3 dA 5 2 '
'z d Ay ax
moKyz dxr dyr ax
4p3 1xr2 2 1 1yr2 2 1 z243/2
B 5
moKyzax
dxr dyr
3 1xr2 2 1 1yr2 2 1 z243/2
(7.8.2)
In the integrand, we may change coordinates from Cartesian to cylindrical for convenience
so that
B 5
moKyzax
rr50
fr50
rr dfr drr
3 1rr2 2 1 z243/2
moKyzax
2p 3
3 1rr2 2 1 z2423/2 1/2 d3 1rr2 24
moKyzax
3 1rr2 2 1 z241/2 `
rr50
moKyax
Hence
H 5 B
2  ax,  for z . 0
By simply replacing z by 2z in eq. (7.8.2) and following the same procedure, we obtain
H 5 2
2  ax,  for z , 0
FIGURE 7.21  For Example 7.8: infi­
nite current sheet.
326  CHAPTER 7  MAGNETOSTATIC FIELDS
PRACTICE EXERCISE  7.8
Repeat Example 7.8 by using Biot–Savart’s law to determine H at points 10, 0, h2 and
10, 0, 2h2.
†7.8  DERIVATION OF BIOT–SAVART’S LAW AND AMPÈRE’S LAW
Both Biot–Savart’s law and Ampère’s law may be derived by using the concept of magnetic
vector potential. The derivation will involve the use of the vector identities in eq. (7.48) and
= 3 = 3 A 5 =1= # A2 2 =2A
(7.52)
Since Biot–Savart’s law as given in eq. (7.4) is defined in terms of line current, we begin our
derivation with eqs. (7.39) and (7.41); that is,
B 5 = 3 C
moI dlr
4pR
5 moI
4p C
= 3 1
R dlr
(7.53)
where R is as defined in eq. (7.45). If the vector identity in eq. (7.48) is applied by letting
F 5 dlr and f 5 1/R, eq. (7.53) becomes
B 5 moI
4p C
c 1
R= 3 dlr 1 a=1
Rb 3 dlrd 
(7.54)
Since  operates with respect to 1x, y, z2 and dl is a function of 1xr, yr, zr2, = 3 dlr 5 0.
Also
R 5 3 1x 2 xr2 2 1 1y 2 yr2 2 1 1z 2 zr2 2421/2
(7.55)
=c 1
Rd 5 2
1x 2 xr2ax 1 1y 2 yr2ay 1 1z 2 zr2az
3 1x 2 xr2 2 1 1y 2 yr2 2 1 1z 2 zr2 243/2 5 2aR
R2
(7.56)
where aR is a unit vector from the source point to the field point. Thus eq. (7.54) (upon
dropping the prime in dl) becomes
B 5 moI
4p C
dl 3 aR
(7.57)
which is Biot–Savart’s law.
7.8 Derivation of Biot–Savart’s Law and Ampère’s Law  327
Using the identity in eq. (7.52) with eq. (7.39), we obtain
= 3 B 5 =1= # A2 2 =2A
(7.58)
For reasons that will be obvious in Chapter 9, we choose
= # A 5 0
(7.59)
which is called Coulomb’s gauge. Upon replacing B with moH and using eq. (7.19),
eq. (7.58) becomes
=2A 5 2mo= 3 H
=2A 5 2moJ
(7.60)
which is called the vector Poisson equation. It is similar to Poisson’s equation 1=2V 5 2rv/e2
in electrostatics. In Cartesian coordinates, eq. (7.60) may be decomposed into three scalar
equations:
=2Ax 5 2moJx
=2Ay 5 2moJy
(7.61)
=2Az 5 2moJz
which may be regarded as the scalar Poisson equations.
It can also be shown that Ampère’s circuit law is consistent with our definition of the
magnetic vector potential. From Stokes’s theorem and eq. (7.39),
H # dl 5 3
= 3 H # dS
5 1
= 3 1= 3 A2 # dS
(7.62)
From eqs. (7.52), (7.59), and (7.60),
= 3 = 3 A 5 2=2 A 5 moJ
Substituting this into eq. (7.62) yields
H # dl 5 3
J # dS 5 I
which is Ampère’s circuit law.
328  CHAPTER 7  MAGNETOSTATIC FIELDS
Lightning is the discharge of static electricity generated in clouds by natural processes.
Lightning may also be regarded as a transient, high-current electric discharge. It is a major
natural source of electromagnetic radiation that interferes with modern electronics and
communication systems. Lightning strikes somewhere on the surface of the earth about 100
times every second. Lightning, the thunderbolt from mythology, has long been feared as an
atmospheric flash of supernatural origins: the great weapon of the gods. Today, scientific
rather than mystical techniques are used to explain lightning, with experimental procedures
replacing intuitive concepts. Yet, we remain in awe of lightning, which still shines with its
mystery, and rightly so. Deaths and injuries to livestock and other animals, ­thousands of
forest and brush fires, and millions of dollars in damage to buildings, communications sys­
tems, power lines, and electrical systems are among the results of lightning.
Since lightning can reach from clouds to the ground or to other clouds, lightning may
be classified into two types: (1) cloud-to-cloud and (2) cloud-to-ground. A typical cloud-to-
is important for aircraft in flight. However, cloud-to-ground lightning has been studied more
extensively because of its practical interest (e.g., as the cause of injuries and death or disturbanc­
es in power and communication systems). A typical cloud-to-ground lightning carries about 10
C to 20 C at an average height of 5 km above the ground. The portion of the cloud-to-ground
discharge that produces physical damage at ground level by virtue of its high current is called
the return stroke. The current in a return stroke is typically 10 kA but can be as high as 200 kA.
Under good weather conditions, an electric field of the order 100 V/m exists near
the earth’s surface. Movements inside a cloud cause the cloud to become an electric
dipole, with negative charges in the lower part and positive charges in the upper part.
†7.9  APPLICATION NOTE—LIGHTNING
FIGURE 7.22  A cloud-to-ground lightning.
ground lighting is shown in Figure 7.22. The cloud-to-cloud discharge is more common and
7.10 Application Note—Polywells  329
A polywell is a polyhedral group of metal rings; inside each ring is a coil, which produces
a magnetic field. As schematically illustrated in Figure 7.23, the position of each of the
rings and the direction of current flow in each coil are set to create a null magnetic field at
The approach of the negatively charged particles to the ground induces more positive
charges, especially on tall, sharp structures. A lightning bolt follows the path of least
resistance at the moment of initiation; this is rarely a straight line, and it is unique for
each strike. However, if we ­assume that lightning strokes arrive in the vertical direction,
we can estimate the striking distance as a function of the amplitude of the current of the
return stroke. The base striking distance D in meters, and the current I, in kiloamperes,
are related as
D 5 10I0.65
(7.63)
Humans and animals within the striking distance may be hurt.
A common way to protect people, buildings, and other structures from lightning is to
use lightning rods. Originally developed by Benjamin Franklin, a lightning rod is a pointed
metal rod attached to the roof of a building. It is connected to a copper or aluminum wire,
and the wire is connected to a conductive grid buried in the ground nearby. Lightning rods
provide a low-resistance path to ground that can be used to conduct the enormous ­electrical
currents when lightning strikes occur. When lightning strikes, the system attempts to carry
the harmful electrical current away from the structure and safely to ground.
7.10  APPLICATION NOTE—POLYWELLS
FIGURE 7.23  Coils in a polywell.
330  CHAPTER 7  MAGNETOSTATIC FIELDS
y = x2
P(–0.5, 0.5, 0)
MATLAB 7.1
the center of the cube. On two opposing sides of the cube a stream of electrons is injected
through the rings. These injected electrons are pushed by the magnetic field toward the
(magnetically null) center of the cube, forming a cloud of electrons. When this cloud of
electrons is large enough, it will create what is known as an electrostatic potential well.
produces.
In a nuclear fusion reactor two lighter atomic particles fuse together to form a heavier
particle, releasing large amounts of energy. The normal activity inside a nuclear fusion
field that acts as an electrostatic potential well. Then the radial electric field accelerates ions
to fusion-revelant energies and confines them in the central grid region.
The fusion reactor system, however, suffers from substantial energy loss due to colli­
sions between the grid itself and the ions. The polywell overcomes this problem by replac­
ing the physical cathode with a virtual cathode, the electron cloud. In the polywell the ion
streams are injected into the polyhedron through the remaining four rings. These ions are
attracted to the electron cloud and are accelerated to the energy at which fusion can occur.
All these parts—the polywell and the electron and ion guns—are encapsulated in a
collection sphere, with all of this inside a vacuum chamber. This collection sphere captures
the energy released from the fusion process in the form of alpha particles, which come
from the fusion, inside the electron cloud, of boron and hydrogen ions. The use of boron
and hydrogen in nuclear fusion is becoming more popular than the use of deuterium
and tritium as fuel. Unlike the fusion of deuterium and tritium, the fusion of boron and
hydrogen produces little to no radiation and, since the only by-product is helium, there is
no radioactive waste.
The polywell’s name comes from its polyhedral shape and the electrostatic potential well
reactor is as follows: Two spherically concentric, gridded electrodes create a radial electric
Suppose a 0.5 mA segment of current travels along the parabola y 5 x2 between a 5 10, 0, 02 and
b 5 11, 1, 02 cm. Using the Biot–Savart law, determine the magnetic field at point P(–0.5, 0.5, 0) due
to the segment.
7.10 Application Note—Polywells  331
H 5 3
Idl 3 aR
4pR2
The unit vector from the incremental current filament at 1xr, yr, 02 to the observation point P
(x, y, z) is
aR 5
1x 2 xr2ax 1 1y 2 yr2ay 1 zaz
R 5 "1x 2 xr2 2 1 1y 2 yr2 2 1 z2
IdL 5 I1dxrax 1 dyray2
The cross product is
IdL 3 aR 5 I1dxray 1 dyray2 3
1x 2 xr2ax 1 1y 2 yr2ay 1 zaz
"1x 2 xr2 2 1 1y 2 yr2 2 1 1z 2 zr2 2
Thus
H 5 3
IdL 3 aR
4pR2
5 I
4p3
3 1y 2 yr2dxr 2 1x 2 xr2dyr4az 2 z dxray 1 z dyrax
3 1x 2 xr2 2 1 1y 2 yr2 2 1 z241.5
This integral is numerically evaluated as 0.85I; thus the magnetic field at P is given by:
H 5 1.9437az
clear
I=0.5e-3;   % the current value
% prompt for observation point
disp(‛Enter the observation point (in the ‛);
p0 = input(‛format [x y z])... \n >  ‛);
if isempty(p0); p0 = [0 0 0]; end
xpstart = 0; xpend = 1e-2;   % start and end points for
%integration variable x prime
dxp=1e-7;   % integration variable increment dx
H = [0, 0, 0]; % initial field values before integration sum
zp = 0;        % current lies only in the xy-plane
for xp=xpstart:dxp:xpend,   % begin integration loop
yp=xp^2*1e2;   % make substitution for y prime in terms
% of x prime
We will find the general solution and evaluate at the observation point. We use the Biot–Savart law
to obtain the magnetic field at point P:
The incremental current element is given by
332  CHAPTER 7  MAGNETOSTATIC FIELDS
% the 1e2 is to offset the 1e-2 squared
% term which relates x prime and y prime
% in space
dyp=2*3*dxp;    % make substitution for dy prime in terms
% of dx prime
num = [(p0(3)-zp)*dyp,-(p0(3)-zp)*dxp,((p0(2)-yp)*dxp-...
(p0(1)-xp)*dyp)];   % numerator
den = ((p0(1)-xp)^2+(p0(2)-yp)^2)^(3/2);   % denominator
H = H + num/den; % total field including all three coordinates
end
H=H*I/(4*pi);
% display the output
disp(‛’)
disp(‛The magnetic field at‛);
disp(sprintf(‛ (%f, %f, %f) cm \nis (%f %f %f) A/m’, ...
p0(1), p0(2), p0(2), H(1), H(2), H(3)))
% This script allows the user to specify a current
% directed out of the page (+z direction) that lies on the origin,
% is assumed infinite, and points in the z direction
% and plot the vector magnetic field in the xy-plane
% inputs: I (value of the current), x and y limits of the plot
% outputs: the magnetic field vector plot
clear
% prompt user for input materials
disp(‛Enter the graph limits ‛);
plotlim = input(‛ [xmin xmax ymin ymax]... \n >  ‛);
if isempty(plotlim); plotlim = [-1 1 -1 1]; end
% check if entered
correctly
I = input(‛Enter the current in Amperes... \n >  ‛);
if isempty(I); I = 1; end    % check if current is entered
dx=(plotlim(2)-plotlim(1))/10;
dy=(plotlim(4)-plotlim(3))/10;
xrange=plotlim(1):dx:plotlim(2);
yrange=plotlim(3):dy:plotlim(4);
[X,Y]=meshgrid(xrange,yrange);
U=zeros(length(xrange), length(yrange));
V=zeros(length(xrange), length(yrange));
for x=1:length(xrange)
MATLAB 7.2
Summary  333
for y=1:length(yrange)
r=sqrt(xrange(x)^2+yrange(y)^2);
% the distance from the current
phiuvector=[-yrange(y),xrange(x)]/r;
% the unit vector in the phi direction
H=I/(2*pi*r)*phiuvector;
% Ampere’s law for an infinite current
% fill matrices which contain the vector
% components in x and y direction
U(y, x)=H(1);   % vector x corresponds to columns
V(y, x)=H(2);   % vector x corresponds to columns
end
end
% Display results
figure
quiver(xrange,yrange,U,V)
axis square
axis(plotlim)
xlabel(‛X location (m)’)
ylabel(‛Y location (m)’)
disp(‛Value of first vector to the right of’);
disp(sprintf(‛ origin = %f A/m’,I/(2*pi*dx)))
1.	 The basic laws (Biot–Savart’s and Ampère’s) that govern magnetostatic fields are discussed.
Biot–Savart’s law, which is similar to Coulomb’s law, states that the magnetic field intensity
dH at r due to current element I dl at r is
dH 5 I dl 3 R
4pR3     (in A/m)
where R 5 r 2 rr and R 5 0 R 0 . For surface or volume current distribution, we replace
I dl with K dS or J dv, respectively; that is,
I dl ; K dS ; J dv
2.	 Ampère’s circuit law, which is similar to Gauss’s law, states that the circulation of H
around a closed path is equal to the current enclosed by the path; that is,
H # dl 5 Ienc 5 3
J # dS
SUMMARY
334  CHAPTER 7  MAGNETOSTATIC FIELDS
= 3 H 5 J    (third Maxwell equation to be derived)
When current distribution is symmetric so that an Amperian path (on which H 5 Hfaf
is constant) can be found, Ampère’s law is useful in determining H; that is,
Hf C
dl 5 Ienc  or  Hf 5 Ienc
where B is the magnetic flux density (in Wb/m2). In free space,
B 5 moH
where mo 5 4p 3 1027 H/m 5 permeability of free space.
4.	 Since an isolated or free magnetic monopole does not exist, the net magnetic flux
through a closed surface is zero:
= # B 5 0    (fourth Maxwell equation to be derived)
5.	 At this point, all four Maxwell equations for static EM fields have been derived, namely:
= # D 5 rv
= # B 5 0
= 3 E 5 0
= 3 H 5 J
6.	 The magnetic scalar potential Vm is defined as
H 5 2=Vm,  if J 5 0
and the magnetic vector potential A as
B 5 = 3 A
where = # A 5 0. With the definition of A, the magnetic flux through a surface S can
be found from
3. Th e magnetic fl ux through a surface S is given by
 5 3
B # dS  (in Wb)
 5 C
B # dS 5 0
 5 C
A # dl
where L is the closed path defining surface S (see Figure 3.21). Rather than using Biot–
Savart’s law, the magnetic field due to a current distribution may be found by using A, a
powerful approach that is particularly useful in antenna theory. For a current element I
dl at r, the magnetic vector potential at r is
A 5 3 moI dl
4pR ,  R 5 0 r 2 rr 0
7.	 Elements of similarity between electric and magnetic fields exist. Some of these are
listed in Table 7.1. Corresponding to Poisson’s equation =2V 5 2rv/e, for example, is
=2A 5 2moJ
8.	 Lightning may be regarded as a transient, high-current electric discharge. A common way
to protect people, buildings, and other structures from lightning is to use lightning rods.
7.1	 One of the following is not a source of magnetostatic fields:
(a)  A dc current in a wire
(b)  A permanent magnet
(c)  An accelerated charge
(d)  An electric field linearly changing with time
(e)  A charged disk rotating at uniform speed
7.2	Identify the configuration in Figure 7.24 that is not a correct representation of I
and H.
7.3	 Consider points A, B, C, D, and E on a circle of radius 2 as shown in Figure 7.25. The items
in the right-hand list are the values of af at different points on the circle. Match these items
with the points in the list on the left.
(a)  A    (i)
(b)  B    (ii)	 2ax
(c)  C    (iii)	 ay
(d)  D    (iv)	 2ay
REVIEW
QUESTIONS
FIGURE 7.24  For Review Question 7.2.
Review Questions  335
336  CHAPTER 7  MAGNETOSTATIC FIELDS
(e)  E    (v)
ax 1 ay
(vi)
2ax 2 ay
(vii)
2ax 1 ay
(viii)
ax 2 ay
7.4	 The z-axis carries filamentary current of 10p A along az. Which of these is incorrect?
(a)  H 5 2ax A/m at 10, 5, 02
(b)  H 5 af A/m at 15, p/4, 02
(c)  H 5 20.8ax 2 0.6ay at 123, 4, 02
(d)  H 5 2af at 15, 3p/2, 02
7.5	 Plane y 5 0 carries a uniform current of 30az mA/m. At 11, 10, 222, the magnetic field
intensity is
(a)  215ax mA/m
(d)  18.85ay nA/m
(b)  15ax mA/m
(e)  None of the above
(c)  477.5ay mA/m
7.6	 For the currents and closed paths of Figure 7.26, calculate the value of AL H # dl.
7.7	 Which of these statements is not characteristic of a static magnetic field?
(a)  It is solenoidal.
(b)  It is conservative.
(c)  It has no sinks or sources.
(d)  Magnetic flux lines are always closed.
(e)  The total number of flux lines entering a given region is equal to the total number of
flux lines leaving the region.
FIGURE 7.25  For Review Question 7.3.
Review Questions  337
7.8	 Two identical coaxial circular coils carry the same current I but in opposite directions. The
magnitude of the magnetic field B at a point on the axis midway between the coils is
(a)  Zero
(b)  The same as that produced by one coil
(c)  Twice that produced by one coil
(d)  Half that produced by one coil.
7.9	 Which one of these equations is not Maxwell’s equation for a static electromagnetic field
in a linear homogeneous medium?
(a)  = # B 5 0
(d)  AS D # dS 5 Q
(b)  = 3 D 5 0
(e)  =2A 5 moJ
(c)  AL B # dl 5 moI
7.10	 Two bar magnets with their north poles having strength Qm1 5
A # m and
Qm2 5 10 A # m (magnetic charges) are placed inside a volume as shown in Figure 7.27.
The magnetic flux leaving the ­volume is
(a)  200 Wb
(d)  0 Wb
(b)  30 Wb
(e)  210 Wb
(c)  10 Wb
Answers:  7.1c, 7.2c, 7.3 (a)-(ii), (b)-(vi), (c)-(i), (d)-(v), (e)-(iii), 7.4d, 7.5a, 7.6 (a) 10 A, (b)
220 A, (c) 0, (d) 210 A, 7.7b, 7.8a, 7.9e, 7.10d.
FIGURE 7.26  For Review Question 7.6.
FIGURE 7.27  For Review Question 7.10.
338  CHAPTER 7  MAGNETOSTATIC FIELDS
Section 7.2—Biot–Savart’s Law
7.1	 (a)  State Biot–Savart’s law.
(b)  The y- and z-axes, respectively, carry filamentary currents 10 A along ay and 20 A
along 2az. Find H at 123, 4, 52.
7.2	 A long, straight wire carries current 2A. Calculate the distance from the wire when the
magnetic field strength is 10 mA/m.
7.3	 Two infinitely long wires, placed parallel to the z-axis, carry currents 10 A in opposite
directions as shown in Figure 7.28. Find H at point P.
7.4	 Two current elements I1dl1 5 4 3 1025 ax A.m at (0, 0, 0) and I2dl2 5 6 3 1025 ay A.m
at (0, 0, 1) are in free space. Find H at (3, 1, –2).
7.5	 A conducting filament carries current I from point A10, 0, a2 to point B10, 0, b2. Show
that at point P1x, y, 02,
H 5
4p"x2 1 y3 c
"x2 1 y2 1 b2 2
"x2 1 y2 1 a2d  af
7.6	 Consider AB in Figure 7.29 as part of an electric circuit. Find H at the origin due  to AB.
7.7	 Line x 5 0, y 5 0, 0 # z # 10 m carries current 2 A along az. Calculate H at points
(a)  15, 0, 02
(c)  15, 15, 02
(b)  15, 5, 02
(d)  15, 215, 02
*7.8	 (a)  Find H at 10, 0, 52 due to side 2 of the triangular loop in Figure 7.6(a).
(b)  Find H at 10, 0, 52 due to the entire loop.
PROBLEMS
10 A
10 A
FIGURE 7.28  For Problem 7.3.
6 A
FIGURE 7.29  For Problem 7.6.
Problems  339
7.9	 An infinitely long conductor is bent into an L shape as shown in Figure 7.30. If a direct
current of 5 A flows in the conductor, find the magnetic field intensity at (a) 12, 2, 02, (b)
10, 22, 02, and (c) 10, 0, 22.
7.10	 Find H at the center C of an equilateral triangular loop of side 4 m carrying 5 A of current
as in Figure 7.31.
7.11	 A rectangular loop carrying 10 A of current is placed on z 5 0 plane as shown in
Figure 7.32. Evaluate H at
(a)  12, 2, 02
(b)  14, 2, 02
(c)  14, 8, 02
(d)  10, 0, 22
7.12	 A square conducting loop of side 4 cm lies on the z 5 0 plane and is centered at the
­origin. If it carries a current 5 mA in the counterclockwise direction, find H at the center
of the loop.
*7.13	(a)  A filamentary loop carrying current I is bent to assume the shape of a regular ­polygon
of n sides. Show that at the center of the polygon
H 5 nI
2pr sin p
where r is the radius of the circle circumscribed by the polygon.
(b)  Apply this for the cases of n 5 3 and n 5 4 and see if your results agree with those for
the ­triangular loop of Problem 7.10.
FIGURE 7.30  Current filament for Problem 7.9.
5 A
5 A
FIGURE 7.31  Equilateral triangular
loop for Problem 7.10.
FIGURE 7.32  Rectangular loop
of Problem 7.11.
FIGURE 7.33  Filamentary loop of Problem 7.14 (not drawn to scale).
100 cm
10 A
10 A
4 cm
340  CHAPTER 7  MAGNETOSTATIC FIELDS
(c)  As n becomes large, show that the result of part (a) becomes that of the circular loop
of Example 7.3.
7.14	 For the filamentary loop shown in Figure 7.33, find the magnetic field strength at O.
7.15	 Figure 7.34 shows a portion of a circular loop. Find H at the origin.
7.16	 Two identical loops are parallel and separated by distance d as shown in Figure 7.35.
Calculate H at (0, 0, d) assuming that a 5 3 cm, d 5 4 cm, and I 5 10 A.
7.17	 A solenoid of radius 4 mm and length 2 cm has 150 turns/m and carries a current of
500 mA. Find (a) 0 H 0  at the center, (b) 0 H 0  at the ends of the solenoid.
7.18	 Plane x 5 10 carries a current of 100 mA/m along az, while line x 5 1, y 5 22 carries a
filamentary current of 20p mA along az. Determine H at 14, 3, 22.
FIGURE 7.34  Problem 7.15.
Problems  341
Section 7.3—Ampère’s Circuit Law
7.19	 (a)  State Ampère’s circuit law.
(b)  A hollow conducting cylinder has inner radius a and outer radius b and carries cur-
rent I along the positive z-direction. Find H everywhere.
7.20	 Current sheets of 20ax A/m and 220ax A/m are located at y 5 1 and y 5 21, respectively.
Find H in region 21 , y , 1.
7.21	 The z 5 0 plane carries current K 5 10ax A/m, while current filament situated at
y 5 0, z 5 6 carries current I along ax. Find I such that H10, 0, 32 5 0.
7.22	 A conducting cylinder of radius a carries current I along 1az. (a) Use Ampère’s law to find
H for   a and  . a. (b) Find J.
7.23	 An infinitely long cylindrical conductor of radius a is placed along the z-axis. If the
­current density is J 5 Jo
az, where Jo is constant, find H everywhere.
7.24	 Let H 5 y2ax 1 x2ay A/m. (a) Find J. (b) Determine the current through the strip
z 51, 0  x  2, 1  y < 5.
7.25	 Let H 5 koar
abaf, r , a, where ko is a constant. (a) Find J for r , a. (b) Find H for r . a.
7.26	 Let H 5 y2ax 1 x2ay A/m. Find J at (1, 24, 7).
7.27	 Assume a conductor, H 5 103ρ2af A/m. (a) Find J. (b) Calculate the current through the
surface  0  ρ  2, 0    2, z 5 0.
Loop 1
Loop 2
FIGURE 7.35  Problem 7.16.
342  CHAPTER 7  MAGNETOSTATIC FIELDS
7.28	 A cylindrical conductor of radius a 5 1 cm carries current I which produces H 5 4ρaf
A/m. Find I.
7.29	 An infinitely long filamentary wire carries a current of 2 A along the z-axis in the
1z-direction. Calculate the following:
(a)  B at 123, 4, 72
(b)  The flux through the square loop described by 2 # r # 6, 0 # z # 4, f 5 90°.
7.30	 Consider the two-wire transmission line whose cross section is illustrated in Figure 7.36. Each
wire is of radius 2 cm, and the wires are separated 10 cm. The wire centered at 10, 02 carries a
current of 5 A, while the other centered at 110 cm, 02 carries the return current. Find H at
(a)  15 cm, 02
(b)  110 cm, 5 cm2
7.31	 An electron beam forms a current of density
J 5 eJo112r2@a22az
0,           r . a
,     r , a
(a)  Determine the total current.
(b)  Find the magnetic field intensity everywhere.
Section 7.5—Magnetic Flux Density
7.32	 Determine the magnetic flux through a rectangular loop 1a 3 b2 due to an infinitely long
conductor carrying current I as shown in Figure 7.37. The loop and the straight conduc­
tors are separated by distance d.
7.33	 A semicircular loop of radius a in free space carries a current I. Determine the magnetic
flux density at the center of the loop.
FIGURE 7.36  Two-wire line of Problem 7.30.
Problems  343
FIGURE 7.38  Cross section of a brass ring enclosing a long straight wire; for Problem 7.35.
FIGURE 7.37  For Problem 7.32.
7.34	 In free space, the magnetic flux density is
B 5 y2ax 1 z2ay 1 x2az Wb/m2
(a)  Show that B is a magnetic field
(b)  Find the magnetic flux through x 5 1, 0 , y , 1, 1 , z , 4.
(c)  Calculate J.
(d)  Determine the total magnetic flux through the surface of a cube defined by 0 < x
< 2, 0  y  2, 0  z  2.
*7.35	A brass ring with triangular cross section encircles a very long straight wire concentrically
as in Figure 7.38. If the wire carries a current I, show that the total number of magnetic
flux lines in the ring is
5 moIh
2pb cb 2 a ln a 1 b
Calculate C if a 5 30 cm, b 5 10 cm, h 5 5 cm, and I 5 10 A.
344  CHAPTER 7  MAGNETOSTATIC FIELDS
7.36	 The electric motor shown in Figure 7.39 has field
H 5 106
r  sin 2f ar A/m
Calculate the flux per pole passing through the air gap if the axial length of the pole is 20 cm.
7.37	 In free space, B 5 20
sin2 faz Wb/m2. Determine the magnetic flux crossing the strip
z = 0, 1  r  2 m, 0  f  /4.
7.38	 If B 5 2
r3 cos uar 1 1
sin uau Wb/m2, find the magnetic flux through the spherical cap
r 5 1,   /3.
7.39	 In a hydrogen atom, an electron revolves at velocity 2.2 3 106 m/s. Calculate the magnetic
flux density at the center of the electron’s orbit. Assume that the radius of the orbit is
R 5 5.3 3 10211 m.
Section 7.6—Maxwell’s Equations
7.40	 Consider the following arbitrary fields. Find out which of them can possibly represent an
electrostatic or magnetostatic field in free space.
(a)  A 5 y cos axax 1 1y 1 e2x2az
(b)  B 5 20
r  ar
(c)  C 5 r2 sin u af
FIGURE 7.39  Electric motor pole of Problem 7.36.
7.41	 Reconsider Problem 7.40 for the following fields.
(a)  D 5 y2zax 1 21x 1 12yzay 2 1x 1 12z2az
(b)  E 5
1z 1 12
cos f ar 1 sin f
(c)  F 5 1
r2 12 cos u ar 1 sin u au2
Section 7.7—Magnetic Scalar and Vector Potentials
7.42	 A current element of length L carries current I in the z direction. Show that at a very
­distant point,
A 5 moIL
4pr  az
Find B.
7.43	 In free space, A 5 10 sin  yax 1 (4 1 cos  x)az Wb/m. Find H and J.
7.44	 Given that A 5 2cosu
ar 1 sinu
r3 au  Wb/m exists in free space.
(a)  show that = ? A 5 0
(b)  Find B at point T(1, 30°, 60°)
7.45	 For a current distribution in free space,
A 5 12x2y 1 yz2ax 1 1xy2 2 xz32ay 2 16xyz 2 2x2y22az Wb/m
(a)  Calculate B.
(b)  Find the magnetic flux through a loop described by x 5 1, 0 , y , 2, 0 , z , 2.
(c)  Show that = # A 5 0 and = # B 5 0.
7.46	 In free space, a small circular loop of current produces
A 5 k
r2 sinuaf
where k is a constant. Find B.
7.47	 The magnetic vector potential of a current distribution in free space is given by
A 5 15e2r sin f az Wb/m
Find H at 13, p/4, 2102. Calculate the flux through r 5 5, 0 # f # p/2, 0 # z # 10.
Problems  345
7.48	 Given that A 5 10
sin uaf Wb/m, find H at point (4, 60o, 30o).
7.49	 An infinitely long conductor of radius a carries a uniform current with J 5 Jo az. Show that
the magnetic vector potential for r , a is
A 5 21
4 moJor2az
7.50	 Find the B field corresponding to the magnetic vector potential
A 5 sin px
2  cos
2  az
7.51	 The magnetic vector potential at a distant point from a small circular loop is given by
A 5 Ao
r2  sin u af Wb/m
where Ao is a constant.  Determine the magnetic flux density B.
7.52	 The magnetic field intensity in a certain conducting medium is
H 5 xy2ax 1 x2zay 2 y2zaz A/m
(a)	 Calculate the current density at point P 12, 21, 3 2.
(b)  What is 'rv
't  at P?
7.53	 Let A 5 10r2az mWb/m.
(a)  Find H and J.
(b)  Determine the total current crossing the surface z 5 1, 0  r  2, 0    2.
7.54	 Prove that the magnetic scalar potential at 10, 0, z2 due to a circular loop of radius a
shown in Figure 7.8(a) is
Vm 5 I
2 c1 2
3z2 1 a241/2d
7.55	 The z-axis carries a filamentary current 12 A along az. Calculate Vm at (4, 30°, 22)
if Vm 5 0 at (10, 60°, 7).
7.56	 Plane z 5 22 carries a current of 50ay A/m. If Vm 5 0 at the origin, find Vm at
(a)  122, 0, 52
(b)  110, 3, 12
346  CHAPTER 7  MAGNETOSTATIC FIELDS

# Sadiku《Elements of Electromagnetics》Chapter 4

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 138-187 of 926 (926 total)

---

## Electrostatic Fields

111
C H A P T E R
111
4.1  INTRODUCTION
Having mastered some essential mathematical tools needed for this course, we are now pre­
pared to study the basic concepts of EM. We shall begin with those fundamental concepts
that are applicable to static (or time-invariant) electric fields in free space (or ­vacuum). An
electrostatic field is produced by a static charge distribution. A typical example of such a
field is found in a cathode-ray tube.
Before we commence our study of electrostatics, it might be helpful to examine briefly
the importance of such a study. Electrostatics is a fascinating subject that has grown up
in diverse areas of application. Electric power transmission, X-ray machines, and light­
ning protection are associated with strong electric fields and will require a knowledge of
electrostatics to understand and design suitable equipment. The devices used in solid-
state electronics are based on electrostatics. These include resistors, capacitors, and active
devices such as bipolar and field effect transistors, which are based on control of electron
motion by electrostatic fields. Almost all computer peripheral devices, with the exception
of magnetic memory, are based on electrostatic fields. Touch pads, capacitance keyboards,
cathode-ray tubes, liquid crystal displays, and electrostatic printers are typical examples. In
medical work, diagnosis is often carried out with the aid of electrostatics, as incorporated
in electrocardiograms, electroencephalograms, and other recordings of the electrical activ­
ity of organs including eyes, ears, and the stomach. In industry, electrostatics is applied in
a variety of forms such as paint spraying, electrodeposition, electrochemical machining,
and separation of fine particles. Electrostatics is used in agriculture to sort seeds, for direct
spraying of plants, to measure the moisture content of crops, to spin cotton, and for speed-
baking bread and smoking meat.1,2
ELECTROSTATIC FIELDS
Who is wise? He that learns from every one. Who is powerful? He that governs his
passions. Who is rich? He that is content. Who is that? Nobody.
—BENJAMIN FRANKLIN
1 For various applications of electrostatics, see J. M. Crowley, Fundamentals of Applied Electrostatics. New York:
John Wiley & Sons, 1999; A. D. Moore, ed., Electrostatics and Its Applications. New York: John Wiley & Sons,
1973; and C. E. Jowett, Electrostatics in the Electronics Environment. New York: John Wiley & Sons, 1976.
2 An interesting story on the magic of electrostatics is found in B. Bolton, Electromagnetism and Its Applications:
An Introduction. London: Van Nostrand, 1980, p. 2.
112  CHAPTER 4  ELECTROSTATIC FIELDS
We begin our study of electrostatics by investigating the two fundamental laws gov­
based on experimental studies, and they are interdependent. Although Coulomb’s law is
applicable in finding the electric field due to any charge configuration, it is easier to use
Gauss’s law when charge distribution is symmetrical. Based on Coulomb’s law, the concept
of electric field intensity will be introduced and applied to cases involving point, line,
surface, and volume charges. Special problems that can be solved with much effort using
Coulomb’s law will be solved with ease by applying Gauss’s law. Throughout our discussion
in this chapter, we will assume that the electric field is in a vacuum or free space. Electric
fields in material space will be covered in the next chapter.
4.2  COULOMB’S LAW AND FIELD INTENSITY
Coulomb’s law is an experimental law formulated in 1785 by Charles Augustin de Coulomb,
then a colonel in the French army. It deals with the force a point charge exerts on another point
charge. By a point charge we mean a charge that is located on a body whose dimensions are
much smaller than other relevant dimensions. For example, a collection of electric charges on a
pinhead may be regarded as a point charge. Electrons are regarded as point charges. The polarity
of charges may be positive or negative; like charges repel, while unlike charges attract. Charges
are generally measured in coulombs (C). One coulomb is approximately equivalent to 6 3 1018
electrons; it is a very large unit of charge because one electron charge e 5 21.6019 3 10219 C.
Coulomb’s law states that the force F between two point charges Q1 and Q2 is:
1.  Along the line joining them
2.  Directly proportional to the product Q1Q2 of the charges
3.  Inversely proportional to the square of the distance R between them.3
Expressed mathematically,
F 5 k Q1Q2
(4.1)
where k is the proportionality constant whose value depends on the choice of system of
units. In SI units, charges Q1 and Q2 are in coulombs (C), the distance R is in meters (m),
and the force F is in newtons (N) so that k 5 1/4peo. The constant o is known as the
­permittivity of free space (in farads per meter) and has the value
eo 5 8.854 3 10212 .  1029
36p F/m
k 5
4peo
.  9 3 109 m/F
(4.2)
3 Further details of experimental verification of Coulomb’s law can be found in W. F. Magie, A Source Book in
Physics. Cambridge, MA: Harvard Univ. Press, 1963, pp. 408–420.
erning electrostatic fields: (1) Coulomb’s law and (2) Gauss’s law. Both of these laws are
4.2 Coulomb’s Law and Field Intensity  113
Thus eq. (4.1) becomes
F 5 Q1Q2
4peoR2
(4.3)
If point charges Q1 and Q2 are located at points having position vectors r1 and r2, then
the force F12 on Q2 due to Q1, shown in Figure 4.1, is given by
F12 5 Q1Q2
4peoR2 aR12
(4.4)
where
R12 5 r2 2 r1
(4.5a)
R 5 0 R12 0  
(4.5b)
aR12 5 R12
R  
(4.5c)
By substituting eq. (4.5) into eq. (4.4), we may write eq. (4.4) as
F12 5 Q1Q2
4peoR3 R12
(4.6a)
F12 5 Q1Q2 1r2 2 r12
4peo 0 r2 2 r1 0 3
(4.6b)
It is worthwhile to note that
1.  As shown in Figure 4.1, the force F21 on Q1 due to Q2 is given by
F21 5 0 F12 0 aR21 5 0 F12 0 12aR122
F21 5 2F12
(4.7)
since
aR21 5 2aR12
2.  Like charges (charges of the same sign) repel each other, while unlike charges
­attract. This is illustrated in Figure 4.2.
FIGURE 4.1  Coulomb vector force on point
charges Q1 and Q2.
114  CHAPTER 4  ELECTROSTATIC FIELDS
3.	 The distance R between the charged bodies Q1 and Q2 must be large compared
with the linear dimensions of the bodies; that is, Q1 and Q2 must be point charges.
4.	 Q1 and Q2 must be static (at rest).
5.	 The signs of Q1 and Q2 must be taken into account in eq. (4.4). For like charges,
Q1 Q2  0. For unlike charges, Q1 Q2  0.
constant.
If we have more than two point charges, we can use the principle of superposition to
determine the force on a particular charge. The principle states that if there are N charges
Q1, Q2, . . . , QN located, respectively, at points with position vectors r1, r2, . . . , rN, the
resultant force F on a charge Q located at point r is the vector sum of the forces exerted on
Q by each of the charges Q1, Q2, . . . , QN. Hence,
F 5 F1 1 F2 1 F3 1 . . . 1 FN
F 5
4peo
k51
Qk1r 2 rk2
0 r 2 rk 0 3 
(4.8)
We can now introduce the concept of electric field intensity.
The electric field intensity (or electric field strength) E is the force that a unit
positive charge experiences when placed in an electric field.
Thus
E 5 lim
QS0
(4.9)
or simply
E 5 F
(4.10)
For Q  0, the electric field intensity E is obviously in the direction of the force F and is
measured in newtons per coulomb or volts per meter. The electric field intensity at point r
due to a point charge located at r is readily obtained from eqs. (4.6) and (4.10) as
E 5
4peoR2 aR 5
Q1r 2 r92
4peo 0 r 2 r9 0 3
(4.11a)
or simply
E 5
4peor2 ar
(4.11b)
FIGURE 4.2  (a), (b) Like charges repel.
(c) Unlike charges attract.
6. Charges cannot be created or destroyed; the quantity of total charge remains
5 QQ11r 2 r12
4peo 0 r 2 r1 0 3 1 QQ21r 2 r22
4peo 0 r 2 r2 0 3 1 . . . 1 QQN1r 2 rN2
4peo 0 r 2 rN 0 3
4.2 Coulomb’s Law and Field Intensity  115
For N point charges Q1, Q2, .  .  . , QN located at r1, r2, .  .  . , rN, the electric field inten­
sity at point r is obtained from eqs. (4.8) and (4.10) as
E 5 E1 1 E2 1 E3 1 . . . 1 EN
E 5
4peo
k51
Qk1r 2 rk2
0 r 2 rk 0 3 
(4.12)
Point charges 1 mC and 22 mC are located at 13, 2, 212 and 121, 21, 42, respectively.
Calculate the electric force on a 10 nC charge located at 10, 3, 12 and the electric field
intensity at that point.
Solution:
F 5 a
k51,2
QQk
4peoR2 aR 5 a
k51,2
QQk1r 2 rk2
4peo 0 r 2 rk 0 3
4peo
e 10233 10, 3, 12 2 13, 2, 212 4
0 10, 3, 12 2 13, 2, 212 0 3
2 2 # 10233 10, 3, 12 2 121, 21, 42 4
0 10, 3, 12 2 121, 21, 42 0 3
5 1023 # 10 # 1029
4p # 1029
36p
123, 1, 22
19 1 1 1 42 3/2 2
211, 4, 232
11 1 16 1 92 3/2 d
5 9 # 1022 c
123, 1, 22
14"14
122, 28, 62
26"26
F 5 26.512ax 2 3.713ay 1 7.509az mN
At that point,
E 5 F
5 126.512, 23.713, 7.5092 #
1023
10 # 1029
E 5 2651.2ax 2 371.3ay 1 750.9az kV/m
PRACTICE EXERCISE  4.1
Point charges 5 nC and 22 nC are located at 12, 0, 42 and 123, 0, 52, respectively.
(a)  Determine the force on a 1 nC point charge located at 11, 23, 72.
(b)  Find the electric field E at 11, 23, 72.
Answer:  (a)  21.004ax 2 1.284ay 1 1.4az nN.
(b)  21.004ax 2 1.284ay 1 1.4azV/m.
EXAMPLE 4.1
Q11r 2 r12
4peo 0 r 2 r1 0 3 1
Q21r 2 r22
4peo 0 r 2 r2 0 3 1 . . . 1
QN1r 2 rN2
4peo 0 r 2 rN 0 3
116  CHAPTER 4  ELECTROSTATIC FIELDS
Two point charges of equal mass m and charge Q are suspended at a common point by two
threads of negligible mass and length ,. Show that at equilibrium the inclination angle a of
each thread to the vertical is given by
Q2 5 16p eomg,2 sin2 a tan a
If a is very small, show that
a 5 Å
16peomg,2
Solution:
Consider the system of charges as shown in Figure 4.3, where Fe is the electric or Coulomb
force, T is the tension in each thread, and mg is the weight of each charge. At A or B
T sin a 5 Fe
T cos a 5 mg
Hence,
sin a
cos a 5 Fe
mg 5 1
4peor2
r 5 2, sin a
Hence,
Q2 cos a 5 16peomg,2 sin3 a
Q2 5 16peomg,2 sin2 a tan a
as required. When a is very small
FIGURE 4.3  Suspended charged particles;
for Example 4.2.
EXAMPLE 14.2
But r 5 AB is given by
4.2 Coulomb’s Law and Field Intensity  117
tan a .  a .  sin a
and so
Q2 5 16peomg,2a3
a 5 Å
16peomg,2
PRACTICE EXERCISE  4.2
Three identical small spheres of mass m are suspended from a common point by threads
of negligible masses and equal length ,. A charge Q is divided equally among the spheres,
and they come to equilibrium at the corners of a horizontal equilateral tri­angle whose
sides are d. Show that
Q2 5 12peomgd3 c,2 2 d2
3 d
21/2
where g  acceleration due to gravity.
Answer: Proof.
A practical application of electrostatics is in electrostatic separation of solids. For example,
Florida phosphate ore, consisting of small particles of quartz and phosphate rock, can
be separated into its components by applying a uniform electric field as in Figure 4.4.
Assuming zero initial velocity and displacement, determine the separation between the
particles after falling 80 cm. Take E 5 500 kV/m and Q/m 5 9 mC/kg for both positively
and negatively charged particles.
EXAMPLE 4.3
FIGURE 4.4  Electrostatic separation of solids;
for Example 4.3.
118  CHAPTER 4  ELECTROSTATIC FIELDS
Solution:
Ignoring the coulombic force between particles, the electrostatic force is acting horizontally
while the gravitational force (weight) is acting vertically on the particles. Thus,
QE 5 m d2x
dt2 ax
d2x
dt2 5 Q
m E
Integrating twice gives
x 5 Q
2m Et2 1 c1t 1 c2
where c1 and c2 are integration constants. Similarly,
2mg 5 m
d2y
dt2
d2y
dt2 5 2g
Integrating twice, we get
y 5 21/2gt2 1 c3t 1 c4
Since the initial displacement is zero,
x1t 5 02 5 0 S  c2 5 0
y1t 5 02 5 0 S  c4 5 0
Also, because of zero initial velocity,
dt `
t50
5 0 S  c1 5 0
dt `
t50
5 0 S  c3 5 0
Thus
x 5 QE
2m t2,  y 5 21
2 gt2
4.3 Electric Fields due to Continuous Charge Distributions  119
When y 5 280 cm 5 20.8 m
t2 5 0.8 3 2
9.8
5 0.1633
and
x 5 1/2 3 9 3 1026 3 5 3 105 3 0.1633 5 0.3673 m
The separation between the particles is 2x 5 73.47 cm.
PRACTICE EXERCISE  4.3
An ion rocket emits positive cesium ions from a wedge-shaped electrode into the region
described by x . 0 y 0 . The electric field is E 5 2400ax 1 200ay kV/m. The ions have
single electronic charges e 5 21.6019 3 10219 C and mass m 5 2.22 3 10225 kg,
and they travel in a vacuum with zero initial velocity. If the emission is confined to
240 cm , y , 40 cm, find the largest value of x that can be reached.
Answer:  0.8 m.
4.3  ELECTRIC FIELDS DUE TO CONTINUOUS
CHARGE DISTRIBUTIONS
So far we have considered only forces and electric fields due to point charges, which are
essentially charges occupying very small physical space. It is also possible to have continuous
charge distribution along a line, on a surface, or in a volume, as illustrated in Figure 4.5.
It is customary to denote the line charge density, surface charge density, and volume charge
density by rL (in C/m), rS (in C/m2), and rv (in C/m3), respectively. These must not be confused
with r (without subscript), used for radial distance in cylindrical coordinates.
The charge element dQ and the total charge Q due to these charge distributions are
obtained from Figure 4.5 as
dQ 5 rL dl S Q 5 3
rL dl   1line charge2
(4.13a)
FIGURE 4.5  Various charge distributions
and charge elements.
120  CHAPTER 4  ELECTROSTATIC FIELDS
dQ 5 rS dS S  Q 5 3
rS dS   1surface charge2
(4.13b)
dQ 5 rv dv S  Q 5 3
rv dv   1volume charge2
(4.13c)
The electric field intensity due to each of the charge distributions rL, rS, and rv may be
regarded as the summation of the field contributed by the numerous point charges making
with charge element dQ 5 rL dl, rS dS, or rv dv and integrating, we get
E 5 3
rL dl
4peoR2 aR  1line charge2
(4.14)
E 5 3
rS dS
4peoR2 aR  1surface charge2
(4.15)
E 5 3
rv dv
4peoR2 aR  1volume charge2
(4.16)
It should be noted that R2 and aR vary as the integrals in eqs. (4.14) to (4.16) are evaluated.
We shall now apply these formulas to some specific charge distributions.
A.  A Line Charge
Consider a line charge with uniform charge density rL extending from A to B along the
z-axis as shown in Figure 4.6. The charge element dQ associated with element dl 5 dz of
the line is
dQ 5 rL dl 5 rL dz
FIGURE 4.6  Evaluation of the E field due
to a line charge.
up the charge distribution. We treat dQ as a point charge. Thus by replacing Q in eq. (4.11)
4.3 Electric Fields due to Continuous Charge Distributions  121
and hence the total charge Q is
Q 5 3
rL dz
(4.17)
The electric field intensity E at an arbitrary point P 1x, y, z2 can be found by using
eq. (4.14). It is important that we learn to derive and substitute each term in eqs. (4.14) to
(4.16) for a given charge distribution. It is customary to denote the field point4 by 1x, y, z2
and the source point by 1xr, yr, zr2. Thus from Figure 4.6,
dl 5 dzr
R 5 1x, y, z2 2 10, 0, zr2 5 xax 1 yay 1 1z 2 zr2az
R 5 rar 1 1z 2 zr2az
R2 5 0 R 0 2 5 x2 1 y2 1 1z 2 zr2 2 5 r2 1 1z 2 zr2 2
R2 5
0 R 0 3 5
rar 1 1z 2 zr2az
3r2 1 1z 2 zr2 243/2
Substituting all this into eq. (4.14), we get
E 5
4peo
rar 1 1z 2 zr2az
3r2 1 1z 2 zr2 243/2 dzr
(4.18)
To evaluate this, it is convenient that we define a, a1, and 2 as in Figure 4.6.
R 5 3r2 1 1z 2 zr2 241/2 5 r sec a
zr 5 OT 2 r tan a,  dzr 5 2r sec2 a da
Hence, eq. (4.18) becomes
E 5 2rL
4peo
r sec2 a 3cos a ar 1 sin a az4 da
r2 sec
2 a
5 2
4peor 3
3cos a ar 1 sin a az4 da
(4.19)
Thus for a finite line charge,
E 5
4peor 321sin a2 2 sin a12ar 1 1cos a2 2 cos a12az4
(4.20)
4 The field point is the point at which the field is to be evaluated.
122  CHAPTER 4  ELECTROSTATIC FIELDS
As a special case, for an infinite line charge, point B is at 10, 0, `2 and A at 10, 0, 2`2 so
that a1 5 p/2, a2 5 2p/2; the z-component vanishes and eq. (4.20) becomes
E 5
2peor ar
(4.21)
Bear in mind that eq. (4.21) is obtained for an infinite line charge along the z-axis so that
r and ar have their usual meaning. If the line is not along the z-axis, r is the perpendicular
distance from the line to the point of interest, and ar is a unit vector along that distance
­directed from the line charge to the field point.
B.  A Surface Charge
Consider an infinite sheet of charge in the xy-plane with uniform charge density rS. The
charge associated with an elemental area dS is
dQ 5 rS dS
(4.22)
From eq. (4.15), the contribution to the E field at point P10, 0, h2 by the charge dQ on the
elemental surface 1 shown in Figure 4.7 is
dE 5
4peoR2 aR
(4.23)
From Figure 4.7,
R 5 r12ar2 1 haz,  R 5 |R| 5 3r2 1 h241/2
FIGURE 4.7  Evaluation of the E field due to an infinite sheet of charge.
aR 5 R
R,  dQ 5 rS dS 5 rS r df dr
4.3 Electric Fields due to Continuous Charge Distributions  123
Substitution of these terms into eq. (4.23) gives
dE 5
rS r df dr 32rar 1 haz4
4peo3r2 1 h243/2
(4.24)
Owing to the symmetry of the charge distribution, for every element 1, there is a corre­
sponding element 2 whose contribution along ar cancels that of element 1, as illustrated in
Figure 4.7. Thus the contributions to Er add up to zero so that E has only z-component. This
can also be shown mathematically by replacing ar with cos f ax 1 sin f ay. Integration of
cos f or sin f over 0 , f , 2p gives zero. Therefore,
E 5 3
dEz 5
4peo
f50
r50
hr dr df
3r2 1 h243/2 az
5 rSh
4peo
2p 3
3r2 1 h2423/2 1
2 d1r22az
5 rSh
2eo
e2 3r2 1 h2421/2 f
E 5 rS
2eo
az 
(4.25)
that is, E has only z-component if the charge is in the xy-plane. Equation (4.25) is valid for
h  0; for h  0, we would need to replace az with az. In general, for an infinite sheet of
charge
E 5 rS
2eo
an
(4.26)
where an is a unit vector normal to the sheet. From eq. (4.25) or (4.26), we notice that
the electric field is normal to the sheet and it is surprisingly independent of the distance
between the sheet and the point of observation P. In a parallel-plate capacitor, the electric
field existing between the two plates having equal and opposite charges is given by
E 5 rS
2eo
an 1 2rS
2eo
12an2 5 rS
an
(4.27)
C.  A Volume Charge
Next, let us consider a sphere of radius a centered at the origin. Let the volume of the
sphere be filled uniformly with a volume-charge density rv (in C/m3) as shown in
­Figure 4.8. The charge dQ associated with the elemental volume dv chosen at (r, , ) is
dQ 5 rv dv
124  CHAPTER 4  ELECTROSTATIC FIELDS
and hence the total charge in a sphere of radius a is
Q 5 3
rv dv 5 rv 3
dv
(4.28)
5 rv 4pa3
The electric field dE outside the sphere at P10, 0, z2 due to the elementary volume charge is
dE 5
rv dv
4peoR2 aR
where aR 5 cos a az 1 sin a ar. Owing to the symmetry of the charge distribution, the
contributions to Ex or Ey add up to zero. We are left with only Ez, given by
Ez 5 E # az 5 3
dE cos a 5
4peo
dv cos a
(4.29)
Again, we need to derive expressions for dv, R2, and cos a:
dv 5 rr2 sin ur drr dur dfr
(4.30)
Applying the cosine rule to Figure 4.8, we have
R2 5 z2 1 rr2 2 2zrr cos ur
rr2 5 z2 1 R2 2 2zR cos a
FIGURE 4.8  Evaluation of the E field due to a volume charge
distribution.
4.3 Electric Fields due to Continuous Charge Distributions  125
It is convenient to evaluate the integral in eq. (4.29) in terms of R and r. Hence we express
cos ur, cos a, and sin ur dur in terms of R and r, that is,
cos a 5 z2 1 R2 2 rr2
2zR
(4.31a)
cos ur 5 z2 1 rr2 2 R2
2zrr
(4.31b)
Differentiating eq. (4.31b) with respect to  and keeping z and r fixed, we obtain
sin ur dur 5 R dR
z rr 
(4.32)
As  varies from 0 to , R varies from (z  r) to (z  r) if P is outside the sphere.
Substituting eqs. (4.30) to (4.32) into eq. (4.29) yields
Ez 5
4peo
fr50
dfr 3
rr50
z1rr
R5z2rr
rr2 R dR
zrr  drr z2 1 R2 2 rr2
2zR
5 rv2p
8peoz2 3
rr50
z1rr
R5z2rr
rr c1 1 z2 2 rr2
d  dR drr
rvp
4peoz2 3
rr cR 2
1z2 2 rr22
z2rr
z1rr
drr
rvp
4peoz2 3
4rr2 drr 5
4peo
z2 a4
3 pa3rvb
E 5
4peoz2 az
(4.33)
This result is obtained for E at P10, 0, z2. Owing to the symmetry of the charge distribu­
tion, the electric field at P1r, u, f2 is readily obtained from eq. (4.33) as
E 5
4peor2 ar
(4.34)
which is identical to the electric field at the same point due to a point charge Q located at
the origin or the center of the spherical charge distribution. The reason for this will become
obvious as we cover Gauss’s law in Section 4.5.
A circular ring of radius a carries a uniform charge L C/m and is placed on the xy-plane
with axis the same as the z-axis.
(a)	 Show that
E10, 0, h2 5
rLah
2eo3h2 1 a243/2 az
EXAMPLE 4.4
126  CHAPTER 4  ELECTROSTATIC FIELDS
(b)	 What values of h give the maximum value of E?
(c)	 If the total charge on the ring is Q, find E as a S  0.
Solution:
(a)  Consider the system as shown in Figure 4.9. Again the trick in finding E by using
eq. (4.14) is deriving each term in the equation. In this case,
dl 5 a df,  R 5 a12ar2 1 haz
R 5 0 R 0 5 3a2 1 h241/2,  aR 5 R
R2 5
0 R 0 3 5
2aar 1 haz
3a2 1 h243/2
Hence
E 5
4peo
f50
12aar 1 haz2
3a2 1 h243/2  a df
By symmetry, the contributions along a add up to zero. This is evident from the fact that
for every element dl there is a corresponding element diametrically opposite that gives an
equal but opposite dE so that the two contributions cancel each other. Thus we are left
with the z-component. That is,
E 5
rLahaz
4peo3h2 1 a243/2 3
df 5
rLahaz
2eo3h2 1 a243/2
as required.
FIGURE 4.9  Charged ring; for
Example 4.4.
4.3 Electric Fields due to Continuous Charge Distributions  127
(b)
For maximum E, d 0 E 0
dh 5 0, which implies that
3h2 1 a241/2 3h2 1 a2 2 3h24 5 0
a2 2 2h2 5 0  or  h 5 6 a
(c)	 Since the charge is uniformly distributed, the line charge density is
rL 5
2pa
so that
E 5
4peo3h2 1 a243/2 az
As a S  0
E 5
4peoh2 az
or in general
E 5
4peor2 aR
which is the same as that of a point charge, as one would expect.
PRACTICE EXERCISE  4.4
A circular disk of radius a is uniformly charged with rS C/m2. The disk lies on the z 5 0
plane with its axis along the z-axis.
(a)  Show that at point 10, 0, h2
E 5 rS
2eo
e1 2
3h2 1 a241/2 faz
(b)  From this, derive the E field due to an infinite sheet of charge on the z 5 0 plane.
(c)  If a V h, show that E is similar to the field due to a point charge.
Answer:  (a) Proof,  (b) rS
2eo
az,  (c) Proof.
d 0 E 0
dh 5 rLa
2eo
3h2 1 a243/2112 2 3
2 1h22h3h2 1 a241/2
3h2 1 a243
128  CHAPTER 4  ELECTROSTATIC FIELDS
The finite sheet 0 # x # 1, 0 # y # 1 on the z 5 0 plane has a charge density
rS 5 xy1x2 1 y2 1 252 3/2 nC/m2. Find
(a)	 The total charge on the sheet
(b)	 The electric field at 10, 0, 52
(c)	 The force experienced by a 21 mC charge located at 10, 0, 52
Solution:
(a)	 Q 5 3
rS dS 5 3
0 3
xy1x2 1 y2 1 252 3/2 dx dy nC
Since x dx 5 1/2 d1x22, we now integrate with respect to x2 (or change variables: x2 5 u
so that x dx 5 du/2).
Q 5 1
2 3
y 3
1x2 1 y2 1 252 3/2 d1x22 dy nC
5 1
2 3
y 2
5 1x2 1 y2 1 252 5/2 `
5 1
5 3
2 3 1y2 1 262 5/2 2 1y2 1 252 5/24 d1y22
5 1
# 2
7 3 1y2 1 262 7/2 2 1y2 1 252 7/24 `
5 1
35 3 1272 7/2 1 1252 7/2 2 21262 7/24
Q 5 33.15 nC
(b)	 E 5 3
rS dS aR
4peor2 5 3
rS dS 1 r 2 rr 2
4peo 0 r 2 rr 0
where r 2 rr 5 10, 0, 52 2 1x, y, 02 5 12x, 2y, 52. Hence,
E 5 3
0 3
1029xy1x2 1 y2 1 252 3/212xax 2 yay 1 5az2dx dy
4p # 1029
36p 1x2 1 y2 1 252 3/2
5 9 c23
x2 dx 3
y dy ax 2 3
x dx 3
y2dy ay 1 5 3
x dx 3
y dy azd
5 9a21
6 , 21
6 , 5
5 121.5, 21.5, 11.252 V/m
(c)	 F 5 qE 5 11.5, 1.5, 211.252 mN
EXAMPLE 4.5
4.3 Electric Fields due to Continuous Charge Distributions  129
PRACTICE EXERCISE  4.5
A square plate described by 22 # x # 2, 22 # y # 2, z 5 0 carries a charge
12 0 y 0  mC/m2. Find the total charge on the plate and the electric field intensity at 10, 0, 102.
Answer:  192 mC, 16.6 az MV/m.
Planes x 5 2 and y 5 23, respectively, carry charges 10 nC/m2 and 15 nC/m2. If the line
x 5 0, z 5 2 carries charge 10p nC/m, calculate E at 11, 1, 212 due to the three charge
­distributions.
Solution:
Let
E 5 E1 1 E2 1 E3
where E1, E2, and E3 are, respectively, the contributions to E at point 11, 1, 212 due to the
infinite sheet 1, infinite sheet 2, and infinite line 3 as shown in Figure 4.10(a). Applying
eqs. (4.26) and (4.21) gives
E1 5
rS1
2eo
12ax2 5 210 # 1029
2 # 1029
36p
ax 5 2180pax
E2 5
rS2
2eo
5 15 # 1029
2 # 1029
36p
5 270pay
FIGURE 4.10  For Example 4.6: (a) three charge distributions,
(b) finding r and ar on plane y 5 1.
EXAMPLE 4.6
130  CHAPTER 4  ELECTROSTATIC FIELDS
and
E3 5
2peor ar
where ar (not regular ar but with a similar meaning) is a unit vector along LP perpen­
dicular to the line charge and r is the length LP to be determined from Figure 4.10(b).
Figure 4.10(b) results from Figure 4.10(a) if we consider plane y 5 1 on which E3 lies.
From Figure 4.10(b), the distance vector from L to P is
R 5 23az 1 ax
r 5 0 R 0 5 "10,  ar 5 R
0 R 0 5
"10
ax 2
"10
Hence,
E3 5 10p # 1029
2p # 1029
36p
# 1
10 1ax 2 3az2
5 18p1ax 2 3az2
Thus by adding E1, E2, and E3, we obtain the total field as
E 5 2162pax 1 270pay 2 54paz V/m
Note that to obtain ar, ar, or an, which we always need for finding F or E, we must go
from the charge (at position vector rr) to the field point (at position vector r); hence ar, ar,
or an is a unit vector along r 2 rr. In addition, r and rr are defined locally, not globally.
­Observe this carefully in Figures 4.6 to 4.10.
PRACTICE EXERCISE  4.6
In Example 4.6 if the line x 5 0, z 5 2 is rotated through 90 about the point 10, 2, 22
so that it becomes x 5 0, y 5 2, find E at 11, 1, 212.
Answer:  2282.7ax 1 565.5ay V/m.
The flux due to the electric field E can be calculated by using the general definition of flux
in eq. (3.13). For practical reasons, however, this quantity is not usually considered to be
the most useful flux in electrostatics. Also, eqs. (4.11) to (4.16) show that the electric field
intensity is dependent on the medium in which the charge is placed (free space in this
­chapter). Suppose a new vector field D is defined by
D 5 eoE
(4.35)
4.4 ELECTRIC FLUX DENSITY
4.4 Electric Flux Density  131
We use eq. (3.13) to define electric flux  in terms of D, namely,
In SI units, one line of electric flux emanates from 11 C and terminates on 21 C.
Therefore, the electric flux is measured in coulombs. Hence, the vector field D is called the
electric flux density and is measured in coulombs per square meter. For historical reasons,
the electric flux density is also called electric displacement.
From eq. (4.35), it is apparent that all the formulas derived for E from Coulomb’s law
in Sections 4.2 and 4.3 can be used in calculating D, except that we have to multiply those
formulas by o. For example, for an infinite sheet of charge, eqs. (4.26) and (4.35) give
D 5 rS
2  an
(4.37)
and for a volume charge distribution, eqs. (4.16) and (4.35) give
D 5 3
rv dv
4pR2 aR
(4.38)
Note from eqs. (4.37) and (4.38) that D is a function of charge and position only; it is
independent of the medium.
Determine D at 14, 0, 32 if there is a point charge 25p mC at 14, 0, 02 and a line charge
3p mC/m along the y-axis.
Solution:
Let D 5 DQ 1 DL, where DQ and DL are flux densities due to the point charge and line
charge, respectively, as shown in Figure 4.11:
DQ 5 eoE 5
4pR2 aR 5 Q 1r 2 rr2
4p 0 r 2 rr 0 3
where r 2 rr 5 14, 0, 32 2 14, 0, 02 5 10, 0, 32. Hence,
DQ 5 25p # 102310, 0, 32
4p 0 10, 0, 32 0 3
5 20.139 az mC/m2
Also
DL 5 rL
2pr ar
In this case
ar 5
14, 0, 32 2 10, 0, 02
0 14, 0, 32 2 10, 0, 02 0 5
14, 0, 32
r 5 0 14, 0, 32 2 10, 0, 02 0 5 5
EXAMPLE 4.7
 5 3
D # dS
(4.36)
132  CHAPTER 4  ELECTROSTATIC FIELDS
Hence,
DL 5
2p1252  14ax 1 3az2 5 0.24ax 1 0.18az mC/m2
Thus
D 5 DQ 1 DL
5 240ax 1 41.1az mC/m2
PRACTICE EXERCISE  4.7
A point charge of 30 nC is located at the origin, while plane y 5 3 carries charge
10 nC/m2. Find D at 10, 4, 32.
Answer:  5.076ay 1 0.0573az nC/m2.
FIGURE 4.11  Flux density D
due to a point charge and an
­infinite line charge.
Gauss’s5 law constitutes one of the fundamental laws of electromagnetism.
Gauss’s law states that the total electric flux c through any closed surface is equal
to the total charge enclosed by that surface.
5 The German mathematician Carl Friedrich Gauss (see Chapter 3 opening) developed the di­vergence theo­
rem of Section 3.6, popularly known by his name. He was the first physicist to measure electric and magnetic
quantities in absolute units. For details on Gauss’s measurements, see W. F. Magie, A Source Book in Physics.
Cambridge, MA: Harvard Univ. Press, 1963, pp. 519–524.
4.5 GAUSS’S LAW—MAXWELL’S EQUATION
4.5 Gauss’s Law—Maxwell’s Equation  133
5 total charge enclosed Q 5 3
rv dv
(4.40)
Q 5 C
D # dS 5 3
rv dv
(4.41)
By applying divergence theorem to the middle term in eq. (4.41), we have
D # dS 5 3
= # D dv
(4.42)
Comparing the two volume integrals in eqs. (4.41) and (4.42) results in
rv 5 = # D
(4.43)
which is the first of the four Maxwell’s equations to be derived. Equation (4.43) states that
the volume charge density is the same as the divergence of the electric flux density.6 It is
equivalent to Coulomb’s law of force between point charges.
Note that:
1.	 Equations (4.41) and (4.43) are basically stating Gauss’s law in different ways;
eq. (4.41) is the integral form, whereas eq. (4.43) is the differential or point form of
Gauss’s law. Equation (4.43) is sometimes called the source equation.
2.	 Gauss’s law is an alternative statement of Coulomb’s law; proper application of the
divergence theorem to Coulomb’s law results in Gauss’s law.
3.	 Gauss’s law provides an easy means of finding E or D for symmetrical charge
distributions such as a point charge, an infinite line charge, an infinite cylindri­
cal surface charge, and a spherical distribution of charge. A continuous charge
distribution has rectangular symmetry if it depends only on x (or y or z), cylindri­
cal symmetry if it depends only on r, or spherical symmetry if it depends only on
r (independent of u and f). It must be stressed that whether the charge distribution
is symmetric or not, Gauss’s law always holds. For example, consider the charge
6This should not be surprising to us from the way we defined divergence of a vector in eq. (3.32):
= # D 5
lim
DvSf  A D # dS
, which reduces to DQ
Dv 5 rv.
Thus
 5 Qenc
(4.39)
that is,
 5 C
d 5 C
D # dS
134  CHAPTER 4  ELECTROSTATIC FIELDS
FIGURE 4.12  Illustration of
Gauss’s law: flux leaving v1 is 5 nC
and that leaving v2 is 0 C.
The procedure for applying Gauss’s law to calculate the electric field involves first know­
ing whether symmetry exists. Once it has been found that symmetric charge distribution
exists, we construct a mathematical closed surface (known as a Gaussian surface). The
surface is chosen such that D is normal or tangential to the Gaussian surface. When D is
normal to the surface, D # dS 5 D dS because D is perpendicular to the surface. When D
is tangential to the surface, D # dS 5 0. Thus we must choose a surface that has some of
the symmetry exhibited by the charge distribution. The choice of an appropriate Gaussian
surface, where there is symmetry in the charge distribution comes from intuitive reason­
ing and a slight degree of maturity in the application of Coulomb’s law. We shall now apply
these basic ideas to the following cases.
A.  Point Charge
Suppose a point charge Q is located at the origin. To determine D at a point P, it is easy to
see that choosing a spherical surface containing P will satisfy symmetry conditions. Thus,
a spherical surface centered at the origin is the Gaussian surface in this case and is shown
in Figure 4.13.
Q 5 C
D # dS 5 Dr C
dS 5 Dr 4pr2
(4.44)
distribution in Figure 4.12 where v1 and v2 are closed surfaces (or volumes). Th e
total fl ux leaving v1 is 10 2 5 5 5 nC because only 10 nC and 25 nC charges are
enclosed by v1. Although charges 20 nC and 15 nC outside v1 do contribute to the
fl ux crossing v1, the net fl ux crossing v1, according to Gauss’s law, is irrespective
of those charges outside v1. Similarly, the total fl ux leaving v2 is zero  because no
charge is enclosed by v2. Th us we see that Gauss’s law,  5 Qenc, is still obeyed even
though the charge distribution is not symmetric. However, we cannot use the law to
determine E or D when the charge distribution is not symmetric; we must resort to
Coulomb’s law to determine E or D in that case.
Since D is everywhere normal to the Gaussian surface, that is, D 5 Drar, applying
Gauss’s law ( 5 Qenc) gives
4.6 APPLICATIONS OF GAUSS’S LAW
4.6 Applications of Gauss’s Law  135
where AdS 5 e
f50 e
u50r2 sin u du df 5 4pr2 is the surface area of the Gaussian surface. Thus
D 5
4pr2 ar
(4.45)
as expected from eqs. (4.11) and (4.35).
B.  Infinite Line Charge
Suppose the infinite line of uniform charge rL C/m lies along the z-axis. To determine D
at a point P, we choose a cylindrical surface containing P to satisfy the symmetry condi­
tion as shown in Figure 4.14. The electric flux density D is constant on and normal to the
cylindrical Gaussian surface; that is, D 5 Drar. If we apply Gauss’s law to an arbitrary
length , of the line
rL, 5 Q 5 3
D # dS 5 Dr 3
dS 5 Dr 2pr,
(4.46)
where e dS 5 2pr, is the surface area of the Gaussian surface. Note that eD # dS evalu­
ated on the top and bottom surfaces of the cylinder is zero, since D has no z-component;
that means that D is tangential to those surfaces. Thus
FIGURE 4.13  Gaussian surface about a point charge.
Line
FIGURE 4.14  Gaussian surface about an infinite line
charge.
136  CHAPTER 4  ELECTROSTATIC FIELDS
D 5 rL
2pr ar
(4.47)
as expected from eqs. (4.21) and (4.35).
C.  Infinite Sheet of Charge
Consider an infinite sheet of uniform charge rS C/m2 lying on the z 5 0 plane. To deter­
mine D at point P, we choose a rectangular box that is cut symmetrically by the sheet of
charge and has two of its faces parallel to the sheet as shown in Figure 4.15. As D is normal
to the sheet, D 5 Dzaz, and applying Gauss’s law gives
rS 3
dS 5 Q 5 C
D # dS 5 Dz c3
top
dS 1 3
bottom
dSd 
(4.48)
Note that D # dS evaluated on the sides of the box is zero because D has no components
rSA 5 Dz1A 1 A2
(4.49)
and thus
D 5 rS
2  az
E 5 D
2eo
az
(4.50)
as expected from eq. (4.25).
FIGURE 4.15  Gaussian surface about
an infinite line sheet of charge.
along a  and a . If the top and bottom area of the box each has area A,  eq. (4.48) becomes
4.6 Applications of Gauss’s Law  137
D.  Uniformly Charged Sphere
Consider a sphere of radius a with a uniform charge ro C/m3. To determine D everywhere,
we construct Gaussian surfaces for cases r # a and r $ a separately. Since the charge has
spherical symmetry, it is obvious that a spherical surface is an appropriate Gaussian ­surface.
For r # a, the total charge enclosed by the spherical surface of radius r, as shown in
Figure 4.16(a), is
Qenc 5 3
rvdv 5 ro 3
dv 5 ro 3
f50
u50
r50
r2 sin u dr du df
(4.51)
5 ro 4
3 pr3
Dr 4pr2 5 4pr3
3  ro
D 5 r
3 ro ar  0 , r #  a
(4.53)
For r $ a, the Gaussian surface is shown in Figure 4.16(b). The charge enclosed by the
surface is the entire charge in this case, that is,
Qenc 5 3
rv  dv 5 ro 3
dv 5 ro 3
f50
u50
r50
r2 sin u dr du df
5 ro 4
3 pa3
(4.54)
FIGURE 4.16  Gaussian surface for a uniformly
charged sphere when (a) r  a and (b) r  a.
and
 5 C
D # dS 5 Dr C
dS 5 Dr 3
f50
u50
r2 sin u du df
5 Dr 4pr2
(4.52)
Hence,  5 Qenc gives
138  CHAPTER 4  ELECTROSTATIC FIELDS
while
c 5 C
D # dS 5 Dr 4pr2
(4.55)
just as in eq. (4.52). Hence,
Dr 4pr2 5 4
3 pa3ro
D 5 a3
3r2 roar,        r $  a
(4.56)
Thus from eqs. (4.53) and (4.56), D everywhere is given by
D 5 µ
3 roar,
0 , r # a
3r2 roar,
r $ a
(4.57)
and 0 D 0  is as sketched in Figure 4.17.
Notice from eqs. (4.44), (4.46), (4.48), and (4.52) that the ability to take D out of the
integral sign is the key to finding D using Gauss’s law. In other words, D must be constant
on the Gaussan surface.
Given that D 5 zr cos2f az C/m2, calculate the charge density at 11, p/4, 32 and the total
charge enclosed by the cylinder of radius 1 m with 22 # z # 2 m.
Solution:
rv 5 = # D 5 'Dz
'z 5 r cos2 f
FIGURE 4.17  Sketch of D against r for a uniformly
charged sphere.
EXAMPLE 4.8
4.6 Applications of Gauss’s Law  139
At 11, p/4, 32, rv 5 1 # cos21p/42 5 0.5 C/m3. The total charge enclosed by the cylinder
can be found in two different ways.
Method 1:  This method is based directly on the definition of the total volume charge.
Q 5 3
rv dv 5 3
r cos2 f r df dr dz
5 3
z522
dz 3
f50
cos2 f df 3
r50
r2 dr 5 41p2 11/32
5 4p
3  C
Method 2: Alternatively, we can use Gauss’s law
Q 5  5 CS
D # dS 5 c3
1 3
1 3
d  D # dS
5 s 1 t 1 b
where s, t, and b are the flux through the sides (curved surface), the top surface, and
the bottom surface of the cylinder, respectively (see Figure 3.18). Since D does not have
component along a, s 5 0, for t, dS 5 r df dr az so
t 5 3
r50
f50
zr cos2 f r df dr `
z52
5 2 3
r2 dr 3
cos2 f df
5 2a1
3bp 5 2p
and for b, dS 5 2r df dr az, so
b 5 2 3
r50
f50
zr cos2 f r df dr `
z522
5 2 3
r2 dr 3
cos2 f df
5 2p
Thus
Q 5  5 0 1 2p
3 1 2p
3 5 4p
3  C
as obtained earlier.
140  CHAPTER 4  ELECTROSTATIC FIELDS
PRACTICE EXERCISE  4.8
If D 5 12y2 1 z2ax 1 4xyay 1 xaz C/m2, find
(a)  The volume charge density at 121, 0, 32
(b)  The flux through the cube defined by 0 # x # 1, 0 # y # 1, 0 # z # 1
(c)  The total charge enclosed by the cube
Answer:  (a) 24 C/m3,  (b) 2 C,  (c) 2 C.
Solution:
The charge distribution is similar to that in Figure 4.16. Since symmetry exists, we can
apply Gauss’s law to find E.
eo C
E # dS 5 Qenc 5 3
rv dv
(a)	 For r , R
eoEr 4pr2 5 Qenc 5 3
0 3
rvr2 sin u df du dr
5 3
4pr2 ror
R  dr 5 ropr4
E 5 ror2
4eoR ar
(b)	 For r . R,
eoEr4pr2 5 Qenc 5 3
0 3
rvr2 sin u df du dr
5 3
ror
R  4pr2 dr 1 3
0 # 4pr2 dr
5 proR3
EXAMPLE 4.9
A charge distribution with spherical symmetry has density
rv 5 •
ror
R ,
0 # r # R
r . R
Determine E everywhere.
4.7 Electric Potential  141
E 5 roR3
4eor2 ar
PRACTICE EXERCISE  4.9
A charge distribution in free space has rv 5 2r nC/m3 for 0 # r # 10 m and zero
otherwise. Determine E at r 5 2 m and r 5 12 m.
Answer:  226ar V/m, 3.927ar kV/m.
From our discussions in the preceding sections, we can obtain the electric field intensity E
due to a charge distribution from Coulomb’s law in general or, when the charge distribu­
tion is symmetric, from Gauss’s law. Another way of obtaining E is from the electric scalar
potential V, to be defined in this section. In a sense, this way of finding E is easier because
it is easier to handle scalars than vectors.
Suppose we wish to move a point charge Q from point A to point B in an electric field
E as shown in Figure 4.18. From Coulomb’s law, the force on Q is F 5 QE so that the work
done in displacing the charge by dl is
dW 5 2F # dl 5 2QE # dl
(4.58)
The negative sign indicates that the work is being done by an external agent. Thus the total
work done, or the potential energy required, in moving Q from A to B, is
W 5 2Q 3
E # dl
(4.59)
Dividing W by Q in eq. (4.59) gives the potential energy per unit charge. This quantity,
denoted by VAB, is known as the potential difference between points A and B. Thus
VAB 5 W
Q 5 23
E # dl
(4.60)
Note that
1.	 In determining VAB, A is the initial point while B is the final point.
2.	 If VAB is negative, there is a loss in potential energy in moving Q from A to B; this
implies that the work is being done by the field. However, if VAB is positive, there is
a gain in potential energy in the movement; an external agent performs the work.
3.	 VAB is independent of the path taken (to be shown a little later).
4.	 VAB is measured in joules per coulomb, commonly referred to as volts (V).
4.7 ELECTRIC POTENTIAL
142  CHAPTER 4  ELECTROSTATIC FIELDS
As an example, if the E field in Figure 4.18 is due to a point charge Q located at the
origin, then
E 5
4peor2 ar
(4.61)
so eq. (4.60) becomes
VAB 5 23
4peor2 ar # dr ar 
(4.62a)
4peo
c 1
2 1
VAB 5 VB 2 VA
(4.62b)
where VB and VA are the potentials (or absolute potentials) at B and A, respectively. Thus
the potential difference VAB may be regarded as the potential at B with reference to A. In
problems involving point charges, it is customary to choose infinity as reference; that is,
we assume the potential at infinity is zero. Thus if VA 5 0 as rA S  ` in eq. (4.62), the
potential at any point 1rB S  r2 due to a point charge Q located at the origin is
V 5
4peor
(4.63)
Note from eq. (4.62a) that because E points in the radial direction, any contribution from a dis­
placement in the u or f direction is wiped out by the dot product E # dl 5 E cos a dl 5 E dr,
where  is the angle between E and dl. Hence the potential difference VAB is independent of
the path as asserted earlier. In general, vectors whose line integral does not depend on the path
of integration are called conservative. Thus, E is conservative.
The potential at any point is the potential difference between that point and a
chosen point (or reference point) at which the potential is zero.
FIGURE 4.18  Displacement of point charge
Q in an electrostatic field E.
4.7 Electric Potential  143
In other words, if one assumes zero potential at infinity, the potential at a distance r from
the point charge is the work done per unit charge by an external agent in transferring a test
charge from infinity to that point. Thus
V 5 23
E # dl
(4.64)
If the point charge Q in eq. (4.63) is not located at the origin but at a point whose posi­
tion vector is r, the potential V(x, y, z) or simply V(r) at r becomes
V1r2 5
4peo 0 r 2 rr 0 
(4.65)
We have considered the electric potential due to a point charge. The same basic ideas
apply to other types of charge distribution because any charge distribution can be regarded
as consisting of point charges. The superposition principle, which we applied to electric
fields, applies to potentials also. For n point charges Q1, Q2, .  .  . , Qn located at points with
position vectors r1, r2, .  .  . , rn, the potential at r is
V1r2 5
4peo 0 r 2 r1 0 1
4peo 0 r 2 r2 0  1 . . . 1
4peo 0 r 2 rn 0
V1r2 5
4peo
k51
0 r 2 rk 0   1point charges2
(4.66)
For continuous charge distributions, we replace Qk in eq. (4.66) with charge element rL dl,
rS dS, or rv dv and the summation becomes an integration, so the potential at r becomes
V1r2 5
4peo
rL1rr2dlr
0 r 2 rr 0    1line charge2 
(4.67)
V1r2 5
4peo
rS1rr2dSr
0 r 2 rr 0    1surface charge2
(4.68)
V1r2 5
4peo
rv1rr2dvr
0 r 2 rr 0    1volume charge2
(4.69)
where the primed coordinates are used customarily to denote source point location and
the unprimed coordinates refer to field point (the point at which V is to be determined).
The following points should be noted:
1.	 We recall that in obtaining eqs. (4.63) to (4.69), the zero potential (reference)
point has been chosen arbitrarily to be at infinity. If any other point is chosen as
­reference, eq. (4.63), for example, becomes
144  CHAPTER 4  ELECTROSTATIC FIELDS
V 5
4peor 1 C
(4.70)
where C is a constant that is determined at the chosen point of reference. The same idea
applies to eqs. (4.65) to (4.69).
2.	 The potential at a point can be determined in two ways depending on whether the
charge distribution or E is known. If the charge distribution is known, we use one of
eqs. (4.65) to (4.70) depending on the charge distribution. If E is known, we simply use
V 5 23 E # dl 1 C
(4.71)
The potential difference VAB can be found generally from
VAB 5 VB 2 VA 5 23
E # dl 5 W
Q 
(4.72)
Two point charges 24 mC and 5 mC are located at 12, 21, 32 and 10, 4, 222, respectively.
Find the potential at 11, 0, 12, assuming zero potential at infinity.
Solution:
Let
Q1 5 24 mC,  Q2 5 5 mC
V1r2 5
4peo 0 r 2 r1 0 1
4peo 0 r 2 r2 0 1 Co
If V1 `2 5 0, Co 5 0,
0 r 2 r1 0 5 0 11, 0, 12 2 12, 21, 32 0 5 0 121, 1, 222 0 5 "6
0 r 2 r2 0 5 0 11, 0, 12 2 10, 4, 222 0 5 0 11, 24, 32 0 5 "26
Hence
V11, 0, 12 5
1026
4p 3 1029
36p
c 24
"26
5 9 3 103 121.633 1 0.98062
5 25.872 kV
PRACTICE EXERCISE  4.10
If point charge 3 mC is located at the origin in addition to the two charges of Example
4.10, find the potential at 121, 5, 22, assuming V1 `2 5 0.
Answer:  10.23 kV.
EXAMPLE 4.10
4.7 Electric Potential  145
A point charge of 5 nC is located at 123, 4, 02, while line y 5 1, z 5 1 carries uniform
charge 2 nC/m.
(a)	 If V 5 0 V at O10, 0, 02, find V at A15, 0, 12.
(b)	 If V 5 100 V at B11, 2, 12, find V at C122, 5, 32.
(c)	 If V 5 25 V at O, find VBC.
Solution:
Let the potential at any point be
V 5 VQ 1 VL
where VQ and VL are the contributions to V at that point due to the point charge and the
line charge, respectively. For the point charge,
VQ 5 2e E # dl 5 23
4peor2 ar # dr ar
4peor 1 C1
For the infinite line charge,
VL 5 23 E # dl 5 23
2peor ar # dr ar
5 2 rL
2peo
ln r 1 C2
Hence,
V 5 2 rL
2peo
ln r 1
4peor 1 C
where C 5 C1 1 C2 5 constant, r is the perpendicular distance from the line y 5 1,
z 5 1 to the field point, and r is the distance from the point charge to the field point.
(a)	 If V 5 0 at O10, 0, 02, and V at A15, 0, 12 is to be determined, we must first determine
the values of r and r at O and A. Finding r is easy; we use eq. (2.31). To find r for any point
1x, y, z2, we utilize the fact that r is the perpendicular distance from 1x, y, z2 to line y 5 1,
z 5 1, which is parallel to the x-axis. Hence r is the distance between 1x, y, z2 and 1x, 1, 12
because the distance vector between the two points is perpendicular to ax. Thus
Applying this for r and eq. (2.31) for r at points O and A, we obtain
rO 5 0 10, 0, 02 2 10, 1, 12 0 5 "2
rO 5 0 10, 0, 02 2 123, 4, 02 0 5 5
EXAMPLE 4.11
r 5 0 1x, y, z2 2 1x, 1, 12 0 5 "1y 2 12 2 1 1z 2 12 2
146  CHAPTER 4  ELECTROSTATIC FIELDS
rA 5 0 15, 0, 12 2 15, 1, 12 0 5 1
rA 5 0 15, 0, 12 2 123, 4, 02 0 5 9
Hence,
VO 2 VA 5 2 rL
2peo
ln rO
4peo
c 1
2 1
5 22 # 1029
2p # 1029
36p
ln "2
1 5 # 1029
4p # 1029
36p
c 1
5 2 1
9 d
0 2 VA 5 236 ln "2 1 45 a1
5 2 1
VA 5 36 ln "2 2 4 5 8.477 V
Notice that we have avoided calculating the constant C by subtracting one potential from
another and that it does not matter which one is subtracted from which.
(b)	 If V 5 100 at B11, 2, 12 and V at C122, 5, 32 is to be determined, we find
rB 5 0 11, 2, 12 2 11, 1, 12 0 5 1
rB 5 0 11, 2, 12 2 123, 4, 02 0 5 "21
rC 5 0 122, 5, 32 2 122, 1, 12 0 5 "20
rC 5 0 122, 5, 32 2 123, 4, 02 0 5 "11
VC 2 VB 5 2 rL
2peo
ln rC
4peo
c 1
2 1
VC 2 100 5 236 ln "20
1 45 # c
"11
"21
5 250.175 V
VC 5 49.825 V
(c)	 To find the potential difference between two points, we do not need a potential refer­
ence if a common reference is assumed.
VBC 5 VC 2 VB 5 49.825 2 100
5 250.175 V
4.8 Relationship between E and V—Maxwell's Equation  147
PRACTICE EXERCISE  4.11
A point charge of 5 nC is located at the origin. If V 5 2 V at 10, 6, 282, find
(a)  The potential at A123, 2, 62
(b)  The potential at B11, 5, 72
(c)  The potential difference VAB
Answer:  (a) 3.929 V,  (b) 2.696 V,  (c) 1.233 V.
As shown in the preceding section, the potential difference between points A and B is
independent of the path taken. Hence,
VBA 5 2VAB
that is, VBA 1 VAB 5 AL E # dl 5 0
E # dl 5 0
(4.73)
This shows that the line integral of E along a closed path as shown in Figure 4.19 must be
zero. Physically, this implies that no net work is done in moving a charge along a closed
path in an electrostatic field. Applying Stokes’s theorem to eq. (4.73) gives
E # dl 5 3
1= 3 E2 # dS 5 0
= 3 E 5 0
(4.74)
Any vector field that satisfies eq. (4.73) or (4.74) is said to be conservative, or irrotational,
as discussed in Section 3.9. In other words, vectors whose line integral does not depend on
FIGURE 4.19  The conservative nature of an
electrostatic field.
4.8 RELATIONSHIP BETWEEN E AND V—MAXWELL’S EQUATION
148  CHAPTER 4  ELECTROSTATIC FIELDS
the path of integration are called conservative vector fields. Thus an electrostatic field is a
conservative field. Equation (4.73) or (4.74) is referred to as Maxwell’s equation (the second
Maxwell’s equation to be derived) for static electric fields. Equation (4.73) is the integral
form, and eq. (4.74) is the differential form; they both depict the conservative nature of an
electrostatic field.
From the way we defined potential, V 5 2eE # dl, it follows that
dV 5 2E # dl 5 2Ex dx 2 Ey dy 2 Ez dz
But from calculus of multivariables, a total change in V(x, y, z) is the sum of partial changes
with respect to x, y, z variables:
dV 5 'V
'x  dx 1 'V
'y  dy 1 'V
'z  dz
Comparing the two expressions for dV, we obtain
Ex 5 2'V
'x ,  Ey 5 2'V
'y ,  Ez 5 2'V
'z 
(4.75)
Thus,
E 5 2= V
(4.76)
that is, the electric field intensity is the gradient of V. The negative sign shows that the
direction of E is opposite to the direction in which V increases; E is directed from higher
to lower levels of V. Since the curl of the gradient of a scalar function is always zero
(= 3 =V 5 0), eq. (4.74) obviously implies that E must be a gradient of some scalar func­
tion. Thus eq. (4.76) could have been obtained from eq. (4.74).
Equation (4.76) shows another way to obtain the E field apart from using Coulomb’s or
Gauss’s law. That is, if the potential field V is known, the E can be found by using eq. (4.76).
One may wonder how one function V can possibly contain all the information that the three
components of E carry. The three components of E are not independent of one another: they
are explicitly interrelated by the condition = 3 E 5 0. The potential ­formulation exploits
this feature to maximum advantage, reducing a vector problem to a scalar one.
Given the potential V 5 10
r2  sin u cos f,
(a)	 Find the electric flux density D at 12, p/2, 02.
(b)	 Calculate the work done in moving a 10 mC charge from point A11, 30°, 120°2 to
B14, 90°, 60°2.
Solution:
(a)	 D 5 eoE
EXAMPLE 4.12
4.8 Relationship between E and V—Maxwell's Equation  149
But
E 5 2=V 5 2c 'V
'r  ar 1 1
r 'V
'u  au 1
r sin u 'V
'f afd
5 20
r3  sin u cos f ar 2 10
r3  cos u cos f au 1 10
r3  sin f af
At 12, p/2, 02,
D 5 eoE 1r 5 2, u 5 p/2, f 5 02 5 eoa20
8  ar 2 0au 1 0afb
5 2.5eoar C/m2 5 22.1 ar pC/m2
(b)	 The work done can be found in two ways, using either E or V.
Method 1:
W 5 2Q3
E # dl  or  2W
Q 5 3
E # dl
and because the electrostatic field is conservative, the path of integration is immaterial.
Hence the work done in moving Q from A11, 30°, 120°2 to B14, 90°, 60°2 is the same as that
in moving Q from A to Ar, from Ar to Br, and from Br to B, where
A11, 30°, 120°2
B14, 90°, 60°2
T dl 5 dr ar
dl 5 r du au
c dl 5 r sin u df af
Ar14, 30°, 120°2
Br14, 90°, 120°2
That is, instead of being moved directly from A to B, Q is moved from A S  Ar, Ar S  Br,
Br S B, so that only one variable is changed at a time. This makes the line integral much
easier to evaluate. Thus
5 2 1
Q 1WAAr 1 WArBr 1 WBrB2
5 a3
AAr
1 3
ArBr
1 3
BrB
b E # dl
5 3
r51
20 sin u cos f
dr `
u530º, f5120º
1 3
90º
u530º
210 cos u cos f
r du `
r54, f5120º
1 3
60º
f5120º
10 sin f
r sin u df `
r54, u590º
150  CHAPTER 4  ELECTROSTATIC FIELDS
5 20 a1
2b a21
2 b c2 1
2r2 `
r51
2 10
1212
sin u`
30°
90°
1 10
16 112 c2 cos f`
120°
60°
Q 5 275
32 1 5
32 2 10
W 5 45
16 Q 5 28.125 mJ
Method 2:
Since V is known, this method is much easier.
W 5 2Q3
E # dl 5 QVAB
5 Q1VB 2 VA2
5 10 a10
16 sin 90° cos 60° 2 10
1  sin 30° cos 120°b # 1026
5 10 a10
32 2 25
2 b # 1026
5 28.125 mJ as obtained before
PRACTICE EXERCISE  4.12
Given that E 5 13x2 1 y2ax 1 xay kV/m, find the work done in moving a  22 mC
charge from 10, 5, 02 to 12, 21, 02 by taking the straight-line pat
(a)  10, 5, 02 S  12, 5, 02 S  12, 21, 02
(b)  y 5 5 2 3x
Answer:  (a) 12 mJ,  (b) 12 mJ.
An electric dipole is formed when two point charges of equal magnitude but oppo-
site sign are separated by a small distance.
The importance of the field due to a dipole will be evident in the subsequent chapters.
Consider the dipole shown in Figure 4.20. The potential at point P1r, u, f2 is given by
4.9 AN ELECTRIC DIPOLE AND FLUX LINES
4.9 An Electric Dipole and Flux Lines  151
V 5
4peo
c 1
2 1
d 5
4peo
c r2 2 r1
r1r2
d 
(4.77)
where r1 and r2 are the distances between P and 1Q and P and 2Q, respectively. If r W d,
r2 2 r1 .  d cos u, r2r1 . r2, and eq. (4.77) becomes
V 5
4peo
d cos u
(4.78)
Since d cos u 5 d # ar, where d 5 daz, if we define
p 5 Qd
(4.79)
as the dipole moment, eq. (4.78) may be written as
V 5 p # ar
4peor2
(4.80)
Note that the dipole moment p is directed from 2Q to 1Q. If the dipole center is not at
the origin but at r, eq. (4.80) becomes
V1r2 5
p # 1r 2 r92
4peo 0 r 2 r9 0 3
(4.81)
The electric field due to the dipole with center at the origin, shown in Figure 4.20, can
be obtained readily from eqs. (4.76) and (4.78) as
E 5 2=V 5 2 c 'V
'r  ar 1 1
r 'V
'u  aud
5 Qd cos u
2peor3  ar 1 Qd sin u
4peor3  au
FIGURE 4.20  An electric dipole.
152  CHAPTER 4  ELECTROSTATIC FIELDS
E 5
4peor3 12 cos u ar 1 sin u au2
(4.82)
where p 5 0 p 0 5 Qd.
Notice that a point charge is a monopole and its electric field varies inversely as r2 while
its potential field varies inversely as r [see eqs. (4.61) and (4.63)]. From eqs. (4.80) and (4.82),
we notice that the electric field due to a dipole varies inversely as r3, while its ­potential varies
inversely as r2. The electric fields due to successive higher-order multipoles (such as a quad­
rupole consisting of two dipoles or an octupole consisting of two quadrupoles) vary inversely
as r4, r5, r6, . . . , while their corresponding potentials vary ­inversely as r3, r4, r5, . . . .
The idea of electric flux lines (or electric lines of force as they are sometimes called) was
introduced by Michael Faraday (1791–1867) in his experimental investigation as a way of
visualizing the electric field.
An electric flux line is an imaginary path or line drawn in such a way that its direction
at any point is the direction of the electric field at that point.
In other words, they are the lines to which the electric flux density D is tangential at
every point.
Any surface on which the potential is the same throughout is known as an equipoten­
tial surface. The intersection of an equipotential surface and a plane results in a path or
line known as an equipotential line. No work is done in moving a charge from one point to
another along an equipotential line or surface 1VA 2 VB 5 02 and hence
E # dl 5 0
(4.83)
on the line or surface. From eq. (4.83), we may conclude that the lines of force or flux
lines (or the direction of E) are always normal to equipotential surfaces. Examples of
equipotential surfaces for point charge and a dipole are shown in Figure 4.21. Note from
Flux line
Flux line
FIGURE 4.21  Equipotential surfaces for (a) a point charge and (b) an electric dipole.
4.9 An Electric Dipole and Flux Lines  153
these examples that the direction of E is everywhere normal to the equipotential lines. We
shall see the importance of equipotential surfaces when we discuss conducting bodies in
electric fields; it will suffice to say at this point that such bodies are equipotential volumes.
A typical application of field mapping (flux lines and equipotential surfaces) is found
in the study of the human heart. The human heart beats in response to an electric field
potential difference across it. The heart can be characterized as a dipole with the field map
similar to that of Figure 4.21(b). Such a field map is useful in detecting abnormal heart
position.7 In Section 14.2, we will discuss a numerical technique for field mapping.
Two dipoles with dipole moments 25az nC # m and 9az nC # m are located at points
10, 0, 222 and 10, 0, 32, respectively. Find the potential at the origin.
Solution:
V 5 a
k51
pk # rk
4peork
4peo
p1 # r1
1 p2 # r2
where
p1 5 25az,   r1 5 10, 0, 02 2 10, 0, 222 5 2az,   r1 5 0 r1 0 5 2
p2 5 9az,
r2 5 10, 0, 02 2 10, 0, 32 5 23az,   r2 5 0 r2 0 5 3
Hence,
V 5
4p # 1029
36p
c 210
2 27
33 d # 1029
5 220.25 V
PRACTICE EXERCISE  4.13
An electric dipole of 100 az pC # m is located at the origin. Find V and E at points
(a)  10, 0, 102
(b)  11, p/3, p/22
Answer:  (a) 9 mV, 1.8ar mV/m,  (b) 0.45 V, 0.9ar 1 0.7794au V/m.
EXAMPLE 4.13
7For more information on this, see R. Plonsey, Bioelectric Phenomena, New York: McGraw-Hill, 1969.
154  CHAPTER 4  ELECTROSTATIC FIELDS
4.10  ENERGY DENSITY IN ELECTROSTATIC FIELDS
To determine the energy present in an assembly of charges, we must first determine the
amount of work necessary to assemble them. Suppose we wish to position three point charges
Q1, Q2, and Q3 in an initially empty space shown shaded in Figure 4.22. No work is required
to transfer Q1 from infinity to P1 because the space is initially charge free and there is no
electric field [from eq. (4.59), W 5 0]. The work done in transferring Q2 from infinity to P2
is equal to the product of Q2 and the potential V21 at P2 due to Q1. Similarly, the work done
in positioning Q3 at P3 is equal to Q31V32 1 V312, where V32 and V31 are the potentials at P3
due to Q2 and Q1, respectively. Hence the total work done in positioning the three charges is
WE 5 W1 1 W2 1 W3
5 0 1 Q2V21 1 Q31V31 1 V322
(4.84)
If the charges were positioned in reverse order,
WE 5 W3 1 W2 1 W1
5 0 1 Q2V23 1 Q11V12 1 V132
(4.85)
where V23 is the potential at P2 due to Q3, V12 and V13 are, respectively, the potentials at P1
due to Q2 and Q3. Adding eqs. (4.84) and (4.85) gives
2WE 5 Q11V12 1 V132 1 Q21V21 1 V232 1 Q31V31 1 V322
5 Q1V1 1 Q2V2 1 Q3V3
WE 5 1
2 1Q1V1 1 Q2V2 1 Q3V32
(4.86)
where V1, V2, and V3 are total potentials at P1, P2, and P3, respectively. In general, if there
are n point charges, eq. (4.86) becomes
WE 5 1
2 a
k51
QkVk        (in joules)
(4.87)
FIGURE 4.22  Assembling of
charges.
4.10 Energy Density in Electrostatic Fields  155
If, instead of point charges, the region has a continuous charge distribution, the sum­
mation in eq. (4.87) becomes integration; that is,
WE 5 1
2 3
rLV dl  1line charge2
(4.88)
WE 5 1
2 3
rSV dS  1surface charge2
(4.89)
WE 5 1
2 3
rvV dv  1volume charge2 
(4.90)
Since rv 5 = # D, eq. (4.90) can be further developed to yield
WE 5 1
2 3
1= # D2 V dv
(4.91)
But for any vector A and scalar V, the identity
= # VA 5 A # =V 1 V1= # A2
1= # A2V 5 = # VA 2 A # =V
(4.92)
holds. Applying the identity in eqs. (4.92) to (4.91), we get
WE 5 1
2 3
1= # VD2 dv 2 1
2 3
1D # =V2 dv
(4.93)
By applying divergence theorem to the first term on the right-hand side of this equation,
we have
WE 5 1
2 C
1VD2 # dS 2 1
2 3
1D # =V2 dv
(4.94)
From Section 4.9, we recall that V varies as 1/r and D as 1/r2 for point charges; V varies as
1/r2 and D as 1/r3 for dipoles; and so on. Hence, VD in the first term on the right-hand side
of eq. (4.94) must vary at least as 1/r3 while dS varies as r2. Consequently, the first integral
in eq. (4.94) must tend to zero as the surface S becomes large. Hence, eq. (4.94) reduces to
WE 5 21
2 3
1D # =V2 dv 5 1
2 3
1D # E2 dv
(4.95)
and since E 5 2=V and D 5 eoE, the electrostatic energy is
156  CHAPTER 4  ELECTROSTATIC FIELDS
WE 5 1
2 3
D # E dv 5 1
2 3
eoE2 dv
(4.96)
From this, we can define electrostatic energy density wE (in J/m3) as
wE 5 dWE
dv 5 1
2 D # E 5 1
2 eoE2 5 D2
2eo
(4.97)
so eq. (4.95) may be written as
WE 5 3
wE dv
(4.98)
The point charges 21 nC, 4 nC, and 3 nC are located at 10, 0, 02, 10, 0, 12, and 11, 0, 02,
­respectively. Find the energy in the system.
Solution:
Method 1:
W 5 W1 1 W2 1 W3
5 0 1 Q2V21 1 Q31V31 1 V322
5 Q2 #
4peo 0 10, 0, 12 2 10, 0, 02 0
1 Q3
4peo
0 11,0,02 2 10,0,02 0 1
0 11,0,02 2 10,0,12 0 d
4peo
aQ1Q2 1 Q1Q3 1 Q2Q3
4p # 1029
36p
a24 2 3 1 12
b # 10218
5 9a 12
2 7b nJ 5 13.37 nJ
Method 2:
W 5 1
2 a
k51
QkVk 5 1
2 1Q1V1 1 Q2V2 1 Q3V32
5 Q1
2  c
4peo112 1
4peo112 d 1 Q2
2  c
4peo112 1
4peo1"22
EXAMPLE 4.14
4.10 Energy Density in Electrostatic Fields  157
1 Q3
2  c
4peo112 1
4peo1"22
4peo
aQ1Q2 1 Q1Q3 1 Q2Q3
5 9a 12
2 7b nJ 5 13.37 nJ
PRACTICE EXERCISE  4.14
Point charges Q1 5 1 nC, Q2 5 22 nC, Q3 5 3 nC, and Q4 5 24 nC are posi-
tioned one at a time and in that order at 10, 0, 02, 11, 0, 02, 10, 0, 212, and 10, 0, 12,
­respectively. Calculate the energy in the system after each charge is positioned.
Answer:  0, 218 nJ, 229.18 nJ, 268.27 nJ.
A charge distribution with spherical symmetry has density
rv 5 cro,
0,      0 # r # R
r . R
Determine V everywhere and the energy stored in region r , R.
Solution:
The D field has already been found in Section 4.6D using Gauss’s law.
(a)	 For r $  R, E 5 roR3
3eor2 ar.
Once E is known, V is determined as
V 5 23 E # dl 5 2roR3
3eo
3 1
r2 dr
5 roR3
3eor 1 C1,  r $  R
Since V1r 5 `2 5 0, C1 5 0.
(b)	 For r #  R, E 5 ror
3eo
ar.
EXAMPLE 4.15
158  CHAPTER 4  ELECTROSTATIC FIELDS
Hence,
V 5 23 E # dl 5 2 ro
3eo
3 r dr
5 2ror2
6eo
1 C2
From part (a) V1r 5 R2 5 roR2
3eo
. Hence,
R2ro
3eo
5 2R2ro
6eo
1 C2 S  C2 5 R2ro
2eo
and
V 5 ro
6eo
13R2 2 r22
Thus from parts (a) and (b)
V 5 ≥
roR3
3eor,
r $ R
6eo
13R2 2 r22,
r # R
(c)	 The energy stored is given by
W 5 1
2 3
D # E dv 5 1
2 eo 3
E2 dv
For r #  R,
E 5 ror
3eo
Hence,
W 5 1
2 eo
9eo
2 3
r50
u50
f50
r2 # r2 sin u df du dr
18eo
4p # r5
5 `
5 2pro
2 R5
45eo
PRACTICE EXERCISE  4.15
If V 5 x 2 y 1 xy 1 2z V, find E at 11, 2, 32 and the electrostatic energy stored in a
cube of side 2 m centered at the origin.
Answer:  23ax 2 2az V/m, 0.2358 nJ.
4.11 Application Note—Electrostatic Discharge  159
†4.11  APPLICATION NOTE—ELECTROSTATIC DISCHARGE
Electrostatic discharge (ESD) (or static electricity, as it is commonly known) refers to the
sudden transfer (discharge) of static charge between objects at different electrostatic poten­
tials. A good example is the “zap” one feels after walking on a synthetic carpet and then
touching a metal doorknob.
ESD belongs to a family of electrical problems known as electrical overstress (EOS).
Other members of the EOS family include lightning and electromagnetic pulses (EMPs).
ESD poses a serious threat to electronic devices and affects the operation of the systems
that contain those devices. An ESD can destroy an integrated circuit (IC), shut down a
computer system, cause a fuel tank to explode, and so on. ESD is a rapid-discharge event
that transfers a finite amount of charge between two bodies at different potentials. ESD
costs industry many billions of dollars annually. The damage to an IC depends on the
current densities and voltage gradients developed during the event. The harmful effects
of ESD are now recognized as a major contributor to poor product yield and long-term
unreliability in many electronic assemblies. Most electronics companies now regard all
semiconductor devices as ESD sensitive. For this reason, a good understanding of ESD is
required in industry. It is considered the responsibility of the design engineer to ensure that
electronic systems are designed and protected against damage from ESD.
What causes ESD? Static charge is a result of an unbalanced electrical charge at rest. For
example, it is created by insulator surfaces rubbing together or pulling apart. One surface
gains electrons, while the other loses electrons. If the charge transfer causes an excess of
electrons on an object, the charge is negative. On the other hand, a deficiency of electrons on
the object makes the static charge positive. When a static charge moves from one surface to
another, it becomes ESD. ESD events occur to balance the charge between two objects. The
movement of these charges often occurs rapidly and randomly, leading to high currents.
ESD can occur in one of the following four ways:
•	 A charged body touches a device such as an IC.
•	 A charged device touches a grounded surface.
•	 A charged machine touches a device.
•	 An electrostatic field induces a voltage across a dielectric that is sufficient to cause
breakdown.
There are two sources of ESD-generated events: people and equipment. ESD from a
person can vary depending on footwear, posture (standing or sitting), and what the person
has in his or her hand (metal or dielectric). The capacitance of a person could double if
the individual were sitting instead of standing. The generated voltage is the driving force
behind the ESD event. For example, walking across a synthetic carpet on a dry day may
generate a potential of 20 kV on the person’s body.
An ESD event takes place in the following four stages.
1. Charge generation: This could be triboelectricity, induction, or conduction.
Triboelectricity requires physical contact between two different materials or the rubbing
­together of two materials. For example, a person who walks across a synthetic carpet
becomes charged by the process of triboelectrification. Fundamental electrostatics tells us
that some materials tend to charge positively, while others tend to charge negatively. The
triboelectric series (see Table 4.1) summarizes this propensity. A material near the top of
160  CHAPTER 4  ELECTROSTATIC FIELDS
Material
Polarity of Charge
Air
Human hands
Rabbit fur
Glass
Mica
Human hair
Fur
Lead
Silk
Aluminum
Paper
Cotton
Steel
Wood
Amber
Wax
Hard rubber
Nickel, copper
Gold
Polyester
Polyethylene
PVC (vinyl)
Silicon
Teﬂon
TABLE 4.1  The Triboelectric Series
Table 4.1 is charged positively when rubbed by a material below it. For example, comb-
ing your hair with a hard rubber comb leaves your hair positively charged and the comb
negatively charged. Inductive charging takes place when a conducting object comes close
to a charged object and is then removed. Conductive charging, which involves the physical
contact and balancing of voltage between two objects at different potentials, often occurs
during automated testing.
2. Charge transfer: This is the second stage in an ESD event. Charge transfers from the
higher potential body to the lower potential body until the potentials between them are
equal. Charge transfer is characterized by the capacitance of the two bodies involved and
the impedance between them.
3. Device response: At this stage, we analyze how a circuit responds to a pulse and
how it withstands the redistribution of charge. When an ESD event begins, charge starts to
redistribute, and this movement of charge generates currents and induces voltages.
4. Device failure: The last stage involves assessing the kind of failure, if any. This is
when we determine whether the device survived. There are three kinds of failure: hard
failure (i.e., physical destruction), soft failure, and latent failure.
The importance of ESD has led standards organizations to develop guidelines for
control and prevention of ESD. The ESD Association has developed a standard known as
ANSI/ESD S20.20 (2007) to establish and maintain ESD control. The standard identifies

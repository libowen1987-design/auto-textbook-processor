# Sadiku《Elements of Electromagnetics》Chapter 8

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 376-425 of 926 (926 total)

---

## Magnetic Forces and Materials

349
C H A P T E R
349
8.1  INTRODUCTION
8.2  FORCES DUE TO MAGNETIC FIELDS
Having considered the basic laws and techniques commonly used in calculating magnetic
field B due to current-carrying elements, we are prepared to study the force a magnetic
field exerts on charged particles, current elements, and loops. Such a study is important to
problems on electrical devices such as ammeters, voltmeters, galvanometers, cyclotrons,
plasmas, motors, and magnetohydrodynamic generators. The precise definition of the
magnetic field, deliberately sidestepped in the preceding chapter, will be given here. The
concepts of magnetic moments and dipole will also be considered.
Furthermore, we will consider magnetic fields in material media, as opposed to the mag-
netic fields in vacuum or free space examined in the preceding chapter. The results of Chapter
7 need only some modification to account for the presence of materials in a magnetic field.
Further discussions will cover inductors, inductances, magnetic energy, and magnetic circuits.
There are at least three ways in which force due to magnetic fields can be experienced. The
force can be (a) due to a moving charged particle in a B field, (b) on a current element in
an external B field, or (c) between two current elements.
A.  Force on a Charged Particle
According to our discussion in Chapter 4, the electric force Fe on a stationary or moving
electric charge Q in an electric field is given by Coulomb’s experimental law and is related
to the electric field intensity E as
Fe 5 QE
(8.1)
This shows that if Q is positive, Fe and E have the same direction.
MAGNETIC FORCES, MATERIALS,
AND DEVICES
Always be kind to your A and B students.  Someday one of them will return to your
campus as a good professor. And also be kind to your C students. Someday one of
them will return and build you a two-million dollar science laboratory.
—YALE UNIVERSITY PRESIDENT
350  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
A magnetic field can exert force only on a moving charge. From experiments, it is
found that the magnetic force Fm experienced by a charge Q moving with a velocity u in a
magnetic field B is
Fm 5 Qu 3 B
(8.2)
This clearly shows that Fm is perpendicular to both u and B.
From eqs. (8.1) and (8.2), a comparison between the electric force Fe and the magnetic
force Fm can be made. We see that Fe is independent of the velocity of the charge and can
perform work on the charge and change its kinetic energy. Unlike Fe, Fm depends on the
charge velocity and is normal to it. However, Fm cannot perform work because it is at right
angles to the direction of motion of the charge 1Fm # dl 5 02; it does not cause an increase
in kinetic energy of the charge. The magnitude of Fm is generally small in comparison to
Fe except at high velocities.
For a moving charge Q in the presence of both electric and magnetic fields, the total
force on the charge is given by,
F 5 Fe 1 Fm
F 5 Q1E 1 u 3 B2
(8.3)
This is known as the Lorentz force equation.1 It relates mechanical force to electrical
force. If the mass of the charged particle moving in E and B fields is m, by Newton’s ­second
law of motion.
F 5 mdu
dt 5 Q1E 1 u 3 B2
(8.4)
The solution to this equation is important in determining the motion of charged particles
in E and B fields. We should bear in mind that in such fields, energy can be transferred
only by means of the electric field. A summary on the force exerted on a charged particle
is given in Table 8.1.
Since eq. (8.2) is closely parallel to eq. (8.1), which defines the electric field, some
authors and instructors prefer to begin their discussions on magnetostatics from eq. (8.2),
just as discussions on electrostatics usually begin with Coulomb’s force law.
B.  Force on a Current Element
To determine the force on a current element I dl of a current-carrying conductor due to the
magnetic field B, we modify eq. (8.2) using the fact that for convection current [see eq. (5.7)]:
J 5 rnu
(8.5)
1 After Hendrik Lorentz (1853–1928), who first applied the equation of motion in electric fields.
8.2 Forces due to Magnetic Fields  351
From eq. (7.5), we recall the relationship between current elements:
I dl 5 K dS 5 J dv
(8.6)
Combining eqs. (8.5) and (8.6) yields
I dl 5 rnu dv 5 dQ u
Alternatively, I dl 5 dQ
dt dl 5 dQdl
dt 5 dQ u
Hence,
I dl 5 dQ u
(8.7)
This shows that an elemental charge dQ moving with velocity u (thereby producing con­
vection current element dQ u) is equivalent to a conduction current element I dl. Thus
the force on a current element I dl in a magnetic field B is found from eq. (8.2) by merely
replacing Qu by I dl; that is,
dF 5 I dl 3 B
(8.8)
If the current I is through a closed path L or circuit, the force on the circuit is given by
F 5 C
I dl 3 B
(8.9)
In using eq. (8.8) or (8.9), we should keep in mind that the magnetic field produced by
the current element I dl does not exert force on the element itself, just as a point charge
does not exert force on itself. The B field that exerts force on I dl must be due to another
element. In other words, the B field in eq. (8.8) or (8.9) is external to the current element
I dl. If instead of the line current element I dl, we have surface current elements K dS
or a volume current element J dv, we simply make use of eq. (8.6) so that eq. (8.8) becomes
dF 5 K dS 3 B  or  dF 5 J dv 3 B
(8.8)
while eq. (8.9) becomes
F 5 3
K dS 3 B  or  F 5 3
J dv 3 B
(8.9)
TABLE 8.1  Force on a Charged Particle
State of Particle
E Field
B Field
Combined E and B Fields
Stationary
Moving
Qu 3 B
Q1E 1 u 3 B2
352  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
From eq. (8.8)
The magnetic field B is defined as the force per unit current element.
Alternatively, B may be defined from eq. (8.2) as the vector that satisfies Fm/q 5 u 3 B,
just as we defined electric field E as the force per unit charge, Fe/q. Both these definitions
of B show that B describes the force properties of a magnetic field.
C.  Force between Two Current Elements
Let us now consider the force between two elements I1 dl1 and I2 dl2. According to Biot–
Savart’s law, both current elements produce magnetic fields. So we may find the force
d(dF1) on element I1 dl1 due to the field dB2 produced by element I2 dl2 as shown in
­Figure 8.1. From eq. (8.8),
d1dF12 5 I1 dl1 3 dB2
(8.10)
But from Biot–Savart’s law,
dB2 5
moI2 dl2 3 aR21
4pR21
(8.11)
Hence,
d1dF12 5
moI1 dl1 3 1I2 dl2 3 aR212
4pR21
(8.12)
This equation is essentially the law of force between two current elements and is analogous
to Coulomb’s law, which expresses the force between two stationary charges. From eq. (8.12),
we obtain the total force F1 on current loop 1 due to current loop 2 shown in Figure 8.1 as
F1 5 moI1I2
4p  C
dl1 3 1dl2 3 aR212
R21
(8.13)
FIGURE 8.1  Force between two current
loops.
8.2 Forces due to Magnetic Fields  353
Although this equation appears complicated, we should remember that it is based on
eq. (8.10). It is eq. (8.9) or (8.10) that is of fundamental importance.
The force F2 on loop 2 due to the magnetic field B1 from loop 1 is obtained from
eq. (8.13) by interchanging subscripts 1 and 2. It can be shown that F2 5 2F1; thus F1 and
F2 obey Newton’s third law that action and reaction are equal and opposite. It is worthwhile
to mention that eq. (8.13) was experimentally established by Oersted and Ampère; Biot and
Savart (Ampère’s colleagues) actually based their law on it.
A charged particle of mass 2 kg and charge 3 C starts at point 11, 22, 02 with velocity
4ax 1 3az m/s in an electric field 12ax 1 10ay V/m. At time t 5 1 s, determine
(a)	 The acceleration of the particle
(b)	 Its velocity
(c)	 Its kinetic energy
(d)	 Its position
Solution:
(a)	 This is an initial-value problem because initial values are given. According to ­Newton’s
second law of motion,
F 5 ma 5 QE
where a is the acceleration of the particle. Hence,
a 5 QE
m 5 3
2 112ax 1 10ay2 5 18ax 1 15ay m/s2
a 5 du
dt 5 d
dt 1ux, uy, uz2 5 18ax 1 15ay
(b)	 Equating components and then integrating, we obtain
dux
dt 5 18 S  ux 5 18t 1 A
(8.1.1)
duy
dt 5 15 S  uy 5 15t 1 B
(8.1.2)
duz
dt 5 0 S  uz 5 C
(8.1.3)
where A, B, and C are integration constants. But at t 5 0, u 5 4ax 1 3az. Hence,
ux1t 5 02 5 4 S  4 5 0 1 A  or  A 5 4
uy1t 5 02 5 0 S  0 5 0 1 B  or  B 5 0
uz1t 5 02 5 3 S  3 5 C
EXAMPLE 8.1
354  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Substituting the values of A, B, and C into eqs. (8.1.1) to (8.1.3) gives
u1t2 5 1ux, uy, uz2 5 118t 1 4, 15t, 32
Hence
u1t 5 1 s2 5 22ax 1 15ay 1 3az m/s
(c)	 Kinetic energy 1K.E.2 5 1
2m 0 u 0 2 5 1
2 122 1222 1 152 1 322
5 718 J
(d)	 u 5 dl
dt 5 d
dt1x, y, z2 5 118t 1 4, 15t, 32
Equating components yields
dt 5 ux 5 18t 1 4 S  x 5 9t2 1 4t 1 A1
(8.1.4)
dt 5 uy 5 15t  S  y 5 7.5t2 1 B1
(8.1.5)
dt 5 uz 5 3  S  z 5 3t 1 C1
(8.1.6)
At t 5 0, 1x, y, z2 5 11, 22, 02; hence,
x1t 5 02 5 1 S  1
5 0 1 A1   or   A1 5 1
y1t 5 02 5 22 S  22 5 0 1 B1
B1 5 22
z1t 5 02 5 0 S  0
5 0 1 C1  or   C1 5 0
Substituting the values of A1, B1, and C1 into eqs. (8.1.4) to (8.1.6), we obtain
1x, y, z2 5 19t2 1 4t 1 1, 7.5t2 2 2, 3t2
(8.1.7)
Hence, at t 5 1, 1x, y, z2 5 114, 5.5, 32.
By eliminating t in eq. (8.1.7), the motion of the particle may be described in terms
of x, y, and z.
PRACTICE EXERCISE  8.1
A charged particle of mass 1 kg and charge 2 C starts at the origin with zero initial
velocity in a region where E  3az V/m. Find the following:
(a)  The force on the particle
(b)  The time it takes to reach point P(0, 0, 12 m)
8.2 Forces due to Magnetic Fields  355
A charged particle of mass 2 kg and 1 C starts at the origin with velocity 3ay m/s and travels
in a region of uniform magnetic field B 5 10az Wb/m2. At t 5 4 s, do the following.
(a)	 Calculate the velocity and acceleration of the particle.
(b)	 Calculate the magnetic force on it.
(c)	 Determine its K.E. and location.
(d)	 Find the particle’s trajectory by eliminating t.
(e)	 Show that its K.E. remains constant.
Solution:
(a)	 F 5 mdu
dt 5 Qu 3 B
a 5 du
dt 5 Q
m u 3 B
Hence
dt 1uxax 1 uyay 1 uzaz2 5 1
2 †
† 5 51uyax 2 uxay2
By equating components, we get
dux
dt 5 5uy
(8.2.1)
duy
dt 5 25ux
(8.2.2)
duz
dt 5 0 S  uz 5 Co
(8.2.3)
We can eliminate ux or uy in eqs. (8.2.1) and (8.2.2) by taking second derivatives of one
equation and making use of the other. Thus
d2ux
dt2 5 5
duy
dt 5 225ux
d2ux
dt2 1 25ux 5 0
EXAMPLE 8.2
(c)  Its velocity and acceleration at P
(d)  Its K.E. at P
Answer:  (a) 6az N,  (b) 2 s,  (c) 12az m/s, 6az m/s2,  (d) 72 J.
356  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
which is a linear differential equation with solution (see Case 3 of Example 6.5)
ux 5 C1 cos 5t 1 C2 sin 5t
(8.2.4)
From eqs. (8.2.1) and (8.2.4),
5uy 5 dux
dt 5 25C1 sin 5t 1 5C2 cos 5t
(8.2.5)
uy 5 2C1 sin 5t 1 C2 cos 5t
We now determine constants Co, C1, and C2 using the initial conditions. At t 5 0, u 5 3ay.
Hence,
ux 5 0 S  0 5 C1 # 1 1 C2 # 0 S  C1 5 0
uy 5 3 S  3 5 2C1 # 0 1 C2 # 1 S  C2 5 3
uz 5 0 S  0 5 Co
Substituting the values of Co, C1, and C2 into eqs. (8.2.3) to (8.2.5) gives
u 5 1ux, uy, uz2 5 13 sin 5t, 3 cos 5t, 02
(8.2.6)
Hence,
u1t 5 42 5 13 sin 20, 3 cos 20, 02
5 2.739ax 1 1.224ay m/s
a 5 du
dt 5 115 cos 5t, 215 sin 5t, 02
and
a1t 5 42 5 6.121ax 2 13.694ay m/s2
(b)
F 5 ma 5 12.2ax 2 27.4ay N
F 5 Qu 3 B 5 112 12.739ax 1 1.224ay2 3 10az
5 12.2ax 2 27.4ay N
(c)	 K.E. 5 1
2m0u 0 2 5 1
2 122 12.7392 1 1.22422 5 9 J
ux 5 dx
dt 5 3 sin 5t S  x 5 23
5 cos 5t 1 b1
(8.2.7)
8.2 Forces due to Magnetic Fields  357
uy 5
dt 5 3 cos 5t S  y 5 3
5 sin 5t 1 b2
(8.2.8)
uz 5 dz
dt 5 0 S  z 5 b3
(8.2.9)
where b1, b2, and b3 are integration constants. At t 5 0, 1x, y, z2 5 10, 0, 02 and hence,
x1t 5 02 5 0 S  0 5 23
# 1 1 b1 S  b1 5 0.6
y1t 5 02 5 0 S  0 5 3
# 0 1 b2 S  b2 5 0
z1t 5 02 5 0 S  0 5 b3
Substituting the values of b1, b2, and b3 into eqs. (8.2.7) to (8.2.9), we obtain
1x, y, z2 5 10.6 2 0.6 cos 5t, 0.6 sin 5t, 02
(8.2.10)
At t 5 4 s,
1x, y, z2 5 10.3552, 0.5478, 02
(d)	 From eq. (8.2.10), we eliminate t by noting that
1x 2 0.62 2 1 y2 5 10.62 2 1cos2 5t 1 sin2 5t2,  z 50
1x 2 0.62 2 1 y2 5 10.62 2,  z 5 0
which is a circle on plane z 5 0, centered at 10.6, 0, 02 and of radius 0.6 m. Thus the
­particle gyrates in an orbit about a magnetic field line.
(e)
K.E. 5 1
2 m 0 u 0 2 5 1
2 122 19 cos2 5t 1 9 sin2 5t2 5 9 J
which is the same as the K.E. at t 5 0 and t 5 4 s. Thus the uniform magnetic field has no
effect on the K.E. of the particle.
Note that the angular velocity v 5 QB/m and the radius of the orbit r 5 uo/v, where
uo is the initial speed. An interesting application of the idea in this example is found in a
common method of focusing a beam of electrons. The method employs a uniform mag­
netic field directed parallel to the desired beam as shown in Figure 8.2. Each electron
emerging from the electron gun follows a helical path and returns to the axis at the same
focal point with other electrons. If the screen of a cathode-ray tube were at this point, a
single spot would appear on the screen.
358  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
A charged particle moves with a uniform velocity 4ax m/s in a region where E 5 20 ay V/m
and B 5 Boaz Wb/m2. Determine Bo such that the velocity of the particle remains constant.
Solution:
If the particle moves with a constant velocity, it is implied that its acceleration is zero.
In other words, the particle experiences no net force. Hence,
0 5 F 5 ma 5 Q1E 1 u 3 B2
0 5 Q120ay 1 4ax 3 Boaz2
220ay 5 24Boay
Thus Bo 5 5.
This example illustrates an important principle employed in a velocity filter shown in
Figure 8.3. In this application, E, B, and u are mutually perpendicular so that Qu 3 B is
FIGURE 8.2  For Example 8.2:
magnetic focusing of a beam of
electrons: (a) helical paths of
­electrons, (b) end view of paths.
PRACTICE EXERCISE  8.2
A proton of mass m is projected into a uniform field B  Boaz with an initial velocity aax
 baz. (a) Find the differential equations that the position vector r  xax  yay  zaz
must satisfy. (b) Show that a solution to these equations is
x 5 a
v sin vt,  y 5 a
v cos vt,  z 5 bt
where v  eBo/m and e is the charge on the proton. (c) Show that this solution describes
a circular helix in space.
Answer:  (a) dx
dt 5 a cos vt,
dt 5 2a sin vt, dz
dt 5 b,  (b) and  (c) Proof.
EXAMPLE 8.3
359
directed opposite to QE, regardless of the sign of the charge. When the magnitudes of the
two vectors are equal,
QuB 5 QE
u 5 E
This is the required (critical) speed to balance out the two parts of the Lorentz force.
Particles with this speed are undeflected by the fields; they are “filtered” through the aper­
ture. Particles with other speeds are deflected down or up, depending on whether their
speeds are greater or less than this critical speed.
FIGURE 8.3  For Example 8.3: a velocity filter for charged particles.
PRACTICE EXERCISE  8.3
Uniform E and B fields are oriented at right angles to each other. An electron moves
with a speed of 8  106 m/s at right angles to both fields and passes undeflected through
the field.
(a)  If the magnitude of B is 0.5 mWb/m2, find the value of E.
(b)  Will this filter work for positive and negative charges and any value of mass?
Answer:  (a) 4 kV/m,  (b) yes.
EXAMPLE 8.4
A rectangular loop carrying current I2 is placed parallel to an infinitely long filamentary
wire carrying current I1 as shown in Figure 8.4(a). Show that the force experienced by the
loop is given by
F, 5 2moI1I2b
c 1
ro 1 a d ar N
8.2 Forces due to Magnetic Fields
360  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Solution:
Let the force on the loop be
F, 5 F1 1 F2 1 F3 1 F4 5 I2 C
dl2 3 B1
where F1, F2, F3, and F4 are, respectively, the forces exerted on sides of the loop labeled 1,
2, 3, and 4 in Figure 8.4(b). Owing to the infinitely long wire
B1 5 moI1
2pro
Hence,
F1 5 I2 3
dl2 3 B1 5 I2 3
z50
dz az 3 moI1
2pro
5 2moI1I2b
2pro
ar  1attractive2
F1 is attractive because it is directed toward the long wire; that is, F1 is along 2ar because
loop side 1 and the long wire carry currents along the same direction. Similarly,
F3 5 I2 3
dl2 3 B1 5 I2 3
z5b
dz az 3
moI1
2p1ro 1 a2  af
moI1I2b
2p1ro 1 a2  ar  1repulsive2
F2 5 I2 3
ro1a
r5ro
dr ar 3
moI1 af
2pr
FIGURE 8.4  For Example 8.4:
(a) rec­tangular loop inside the field
produced by an infinitely long wire,
(b) forces acting on the loop
and wire.
8.3 Magnetic Torque and Moment  361
5 moI1I2
2p  ln ro 1 a
az  1parallel2
F4 5 I2 3
r5ro1a
dr ar 3
moI1af
2pr
5 2moI1I2
2p  ln ro 1 a
az  1parallel2
The total force F on the loop is the sum of F1, F2, F3, and F4; that is,
F, 5 moI1I2b
c 1
ro 1 a d 12ar2
which is an attractive force trying to draw the loop toward the wire. The force Fw on the
wire, by Newton’s third law, is 2F,; see Figure 8.4(b).
PRACTICE EXERCISE  8.4
In Example 8.4, find the force experienced by the infinitely long wire if I1  10 A, I2  5 A,
ro  20 cm, a  10 cm, b  30 cm.
Answer:  5ar mN.
8.3  MAGNETIC TORQUE AND MOMENT
Now that we have considered the force on a current loop in a magnetic field, we can deter­
mine the torque on it. The concept of a current loop experiencing a torque in a magnetic
field is of paramount importance in understanding the behavior of orbiting charged par­
ticles, dc motors, and generators. If the loop is placed parallel to a magnetic field, it experi­
ences a force that tends to rotate it.
The torque T (or mechanical moment of force) on the loop is the vector product of
the moment arm r and the force F.
That is,
T 5 r 3 F
(8.14)
and its units are newton-meters 1N # m2.
Let us apply this to a rectangular loop of length  and width w placed in a uniform
magnetic field B as shown in Figure 8.5(a). From Figure 8.5(a), we notice that dl is parallel
to B along sides AB and CD of the loop and no force is exerted on those sides. Thus
362  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
F 5 I3
dl 3 B 1 I3
dl 3 B
5 I3
dz az 3 B 1 I3
dz az 3 B
F 5 Fo 2 Fo 5 0
(8.15)
where 0 Fo 0 5 IB, because B is uniform. Thus, no force is exerted on the loop as a whole.
However, Fo and 2Fo act at different points on the loop, thereby creating a couple. If the
normal to the plane of the loop makes an angle a with B, as shown in the cross-sectional
view of Figure 8.5(b), the torque on the loop is
0 T 0 5 0 Fo 0  w sin a
T 5 BI,w sin a
(8.16)
But ,w 5 S, the area of the loop. Hence,
T 5 BIS sin a
(8.17)
We define the quantity
m 5 ISan
(8.18)
as the magnetic dipole moment (in A # m2) of the loop. In eq. (8.18), an is a unit normal vec­
tor to the plane of the loop and its direction is determined by the right-hand rule: fingers
in the direction of current and thumb along an.
FIGURE 8.5  (a)  Rectangular planar loop in a uniform magnetic
field. (b) Cross-sectional view of part (a).
8.4 A Magnetic Dipole  363
The magnetic dipole moment is the product of current and area of the loop; its
­direction is normal to the loop.
Introducing eq. (8.18) in eq. (8.17), we obtain
T 5 m 3 B
(8.19)
Although this expression was obtained by using a rectangular loop, it is generally applicable
in determining the torque on a planar loop of any arbitrary shape. The only limitation is
that the magnetic field must be uniform. It should be noted that the torque is in the direc­
tion of the axis of rotation (the z-axis in the case of Figure 8.5(a)). It is directed with the
aim of reducing a so that m and B are in the same direction. In an equilibrium position
(when m and B are in the same direction), the loop is perpendicular to the magnetic field
and the torque will be zero as well as the sum of the forces on the loop.
8.4  A MAGNETIC DIPOLE
A magnetic dipole consists of a bar magnet or small current-carrying loop. The reason for this
and what we mean by “small” will soon be evident. Let us determine the magnetic field B at
an observation point P1r, u, f2 due to a circular loop carrying ­current I as in Figure 8.6. The
magnetic vector potential at P is
A 5 moI
4p C dl
(8.20)
It can be shown that in the far field r W a, so that the loop appears small at the observation
point, A has only f-component and it is given by
A 5
moIpa2 sin u af
4pr2
(8.21a)
FIGURE 8.6  Magnetic field at P due to a
current loop.
364  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
A 5 mo m 3 ar
4pr2
(8.21b)
where m 5 Ipa2az, the magnetic moment of the loop, and az 3 ar 5 sin u af. We deter­
mine the magnetic flux density B from B 5 = 3 A as
B 5 mom
4pr3 12 cos u ar 1 sin u au2
(8.22)
TABLE 8.2  Comparison between Electric and Magnetic Monopoles and Dipoles
8.4 A Magnetic Dipole  365
It is interesting to compare eqs. (8.21) and (8.22) with similar expressions in eqs.
(4.80) and (4.82) for electrical potential V and electric field intensity E due to an electric
dipole. This comparison is done in Table 8.2, in which we notice the striking similari­
ties between B in the far field due to a small current loop and E in the far field due to
an electric dipole. It is therefore reasonable to regard a small current loop as a magnetic
­dipole. The B lines due to a magnetic dipole are similar to the E lines due to an electric
­dipole. Figure 8.7(a) illustrates the B lines around the magnetic dipole m 5 IS.
A short permanent magnetic bar, shown in Figure 8.7(b), may also be regarded as a
magnetic dipole. Observe that the B lines due to the bar are similar to those due to a small
current loop in Figure 8.7(a).
Consider the bar magnet of Figure 8.8. If Qm is an isolated magnetic charge (pole
strength) and  is the length of the bar, the bar has a dipole moment Qm<. (Notice that Qm
does exist; however, it does not exist without an associated 2Qm. See Table 8.2.) When the
bar is in a uniform magnetic field B, it experiences a torque
T 5 m 3 B 5 Qm< 3 B
(8.23)
where < points south to north. The torque tends to align the bar with the external magnetic
field. The force acting on the magnetic charge is given by
F 5 QmB
(8.24)
Since both a small current loop and a bar magnet produce magnetic dipoles, they are
equivalent if they produce the same torque in a given B field, that is, when
T 5 Qm,B 5 ISB
(8.25)
FIGURE 8.7  The B lines due to
magnetic dipoles: (a) a small
current loop with m 5 IS, (b) a
bar magnet with m 5 Qm.
FIGURE 8.8  A bar magnet in an external magnetic
field.
366  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Hence,
Qm, 5 IS
(8.26)
showing that they must have the same dipole moment.
Determine the magnetic moment of an electric circuit formed by the triangular loop of
­Figure 8.9.
Solution:
If a plane intercepts the coordinate axes at (a, 0, 0),  (0, b, 0), and (0, 0, c), its equation is
given by
a 1
b 1 z
c 5 1 h bcx 1 cay 1 abz 5 abc
For the present problem, a = b = c = 2. Hence
x 1 y 1 z 5 2
Thus, we can use
m 5 ISan
where
S 5 loop area 5 1
2 3 base 3 height 5 1
2 12"22 12"22sin 60°
5 4 sin 60°
FIGURE 8.9  Triangular loop of Example 8.5.
EXAMPLE 8.5
8.4 A Magnetic Dipole  367
If we define the plane surface by a function
f 1x, y, z2 5 x 1 y 1 z 2 2 5 0
an 5 6
0 =f 0 5 6
1ax 1 ay 1 az2
We choose the plus sign in view of the direction of the current in the loop (using the right-
hand rule, m is directed as in Figure 8.9). Hence
m 5 514 sin 60°2
1ax 1 ay 1 az2
5 101ax 1 ay 1 az2 A # m2
PRACTICE EXERCISE  8.5
A rectangular coil of area 10 cm2 carrying current of 50 A lies on plane
2x  6y  3z  7 such that the magnetic moment of the coil is directed away from the
origin. Calculate its magnetic moment.
Answer:  (1.429ax  4.286ay  2.143az)  102 A . m2.
EXAMPLE 8.6
A small current loop L1 with magnetic moment 5az A # m2 is located at the origin while
­another small loop current L2 with magnetic moment 3ay A # m2 is located at 14, 23, 102.
Determine the torque on L2.
Solution:
The torque T2 on the loop L2 is due to the field B1 produced by loop L1. Hence,
T2 5 m2 3 B1
Since m1 for loop L1 is along az, we find B1 using eq. (8.22):
B1 5 mom1
4pr3 12 cos u ar 1 sin u au2
Using eq. (2.23), we transform m2 from Cartesian to spherical coordinates:
m2 5 3ay 5 31sin u sin f ar 1 cos u sin f au 1 cos f af2
At 14, 23, 102,
r 5 "42 1 1232 2 1 102 5 5"5
368  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
tan u 5 r
z 5 5
10 5 1
2 S  sin u 5
,  cos u 5
tan f 5
x 5 23
4  S  sin f 5 23
5 ,  cos f 5 4
Hence,
B1 5 4p 3 1027 3 5
4p 625 "5
a 4
ar 1
aub
5 1027
625  14ar 1 au2
m2 5 3c2 3ar
5"5
2 6au
5"5
4af
5 d
and
T 5
1027 132
62515"52
123ar 2 6au 1 4"5af2 3 14ar 1 af2
5 4.293 3 10211 128.944ar 1 35.777au 1 21af2
5 20.384ar 1 1.536au 1 0.9015af nN # m
PRACTICE EXERCISE    8.6
The coil of Practice Exercise 8.5 is surrounded by a uniform field 0.6ax  0.4ay  0.5az
Wb/m2.
(a)  Find the torque on the coil.
(b)  Show that the torque on the coil is maximum if placed on plane 2x  8y  4z 
"84. Calculate the magnitude of the maximum torque.
Answer:  (a) 0.03ax 2 0.02ay 2 0.02az N # m, (b) 0.0439 N # m.
8.5  MAGNETIZATION IN MATERIALS
Our discussion here will parallel that on polarization of materials in an electric field. We
shall assume that our atomic model is that of an electron orbiting about a positive ­nucleus.
We know that a given material is composed of atoms. Each atom may be regarded as
consisting of electrons orbiting about a central positive nucleus; the electrons also rotate
8.5 Magnetization in Materials  369
(or spin) about their own axes. Thus an internal magnetic field is produced by electrons
orbiting around the nucleus as in Figure 8.10(a) or electrons spinning as in Figure 8.10(b).
Both these electronic motions produce internal magnetic fields Bi that are similar to the
magnetic field produced by a current loop of Figure 8.11. The equivalent current loop has
a magnetic moment of m 5 IbSan, where S is the area of the loop and Ib is the bound cur­
rent (bound to the atom).
Without an external B field applied to the material, the sum of m’s is zero due to
random orientation as in Figure 8.12(a). When an external B field is applied, the magnetic
moments of the electrons more or less align themselves with B so that the net magnetic
moment is not zero, as illustrated in Figure 8.12(b).
The magnetization M, in amperes per meter, is the magnetic dipole moment per
unit volume.
Electron
Electron
FIGURE 8.10  (a) Electron orbiting around the
nucleus. (b) Electron spin.
FIGURE 8.11  Circular current loop
equivalent to electronic motion of
Figure 8.10.
FIGURE 8.12  Magnetic dipole
moment in a volume Dn: (a) before
B is applied, (b) after B is applied.
If there are N atoms in a given volume n and the kth atom has a magnetic moment mk,
M 5
lim
DnS0 a
k51
(8.27)
370  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
A medium for which M is not zero everywhere is said to be magnetized. For a differential
volume dv, the magnetic moment is dm 5 M dvr. Recall that we denote the field point by
the unprimed coordinates (x, y, z) and the source point by the primed coordinates (x9, y9, z9).
From eq. (8.21b), the vector magnetic potential due to dm is
dA 5 moM 3 aR
4pR2
dvr 5 moM 3 R
4pR3
dvr
R3 5 =r1
Hence,
A 5 mo
4p 3
M 3 =r 1
R dvr
(8.28)
Using eq. (7.48) gives
M 3 =r1
R 5 1
R=r 3 M 2 =r 3 M
Substituting this into eq. (8.28) yields
A 5 mo
4p 3
=r 3 M
dvr 2 mo
4p 3
=r 3 M
R  dvr
Applying the vector identity
=r 3 F dvr 5 2C
F 3 dS
to the second integral, we obtain
A 5 mo
4p 3
=r 3 M
dvr 1 mo
4p C
M 3 an
dSr
5 mo
4p 3
Jb dvr
1 mo
4p C
Kb dSr
(8.29)
Comparing eq. (8.29) with eqs. (7.42) and (7.43) (upon dropping the primes) gives
Jb 5 = 3 M
(8.30)
and
From eq. (7.46) we can write
8.5 Magnetization in Materials  371
Kb 5 M 3 an
(8.31)
where Jb is the bound volume current density or magnetization volume current density, in
amperes per meter squared, Kb is the bound surface current density, in amperes per meter,
and an is a unit vector normal to the surface. Equation (8.29) shows that the potential of
a magnetic body is due to a volume current density Jb throughout the body and a surface
current Kb on the surface of the body. The vector M is analogous to the polarization P in
dielectrics and is sometimes called the magnetic polarization density of the medium. In
another sense, M is analogous to H and they both have the same units. In this respect, as
J 5 = 3 H, so Jb 5 = 3 M. Also, Jb and Kb for a magnetized body are similar to rpv and
rps for a polarized body. As is evident in eqs. (8.29) to (8.31), Jb and Kb can be derived from
M; therefore, Jb and Kb are not commonly used.
In free space, M 5 0 and we have
= 3 H 5 Jf  or  = 3 a B
mob 5 Jf
(8.32)
where Jf is the free current volume density. In a material medium M 2 0, and as a result,
B changes so that
= 3 a B
mob 5 Jf 1 Jb 5 J
5 = 3 H 1 = 3 M
B 5 mo1H 1 M2
(8.33)
The relationship in eq. (8.33) holds for all materials whether they are linear or not. The
concepts of linearity, isotropy, and homogeneity introduced in Section 5.7 for dielectric
media equally apply here for magnetic media. For linear materials, M (in A/m) depends
linearly on H such that
M 5 xmH
(8.34)
where xm is a dimensionless quantity (ratio of M to H) called magnetic susceptibility of the
medium. It is more or less a measure of how susceptible (or sensitive) the material is to a
magnetic field. Substituting eq. (8.34) into eq. (8.33) yields
B 5 mo11 1 xm2H 5 mH
(8.35)
B 5 momrH
(8.36)
where
372  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
mr 5 1 1 xm 5 m
(8.37)
The quantity m 5 momr is called the permeability of the material and is measured in
­henrys per meter; the henry is the unit of inductance and will be defined a little later.
The dimensionless quantity mr is the ratio of the permeability of a given material to that
of free space and is known as the relative permeability of the material.
It should be borne in mind that the relationships in eqs. (8.34) to (8.37) hold only for
linear and isotropic materials. If the materials are anisotropic (e.g., crystals), eq. (8.33) still
holds but eqs. (8.34) to (8.37) do not apply. In this case, m has nine terms [similar to  in
eq. (5.37)] and, consequently, the fields B, H, and M are no longer parallel.
†8.6  CLASSIFICATION OF MATERIALS
In general, we may use the magnetic susceptibility xm or the relative permeability mr to
classify materials in terms of their magnetic property or behavior. A material is said to be
nonmagnetic if xm 5 0 (or mr 5 1); it is magnetic otherwise. Free space, air, and materials
with xm 5 0 (or mr < 1) are regarded as nonmagnetic.
Roughly speaking, materials may be grouped into three major classes: diamag­
netic, paramagnetic, and ferromagnetic. This rough classification is depicted in
r ( 1 (i.e., very small negative xm).
It is paramagnetic if mr * 1 (i.e., very small positive xm). If mr W 1 (i.e., very large positive
xm), the material is ferromagnetic. Table B.3 in Appendix B presents the values mr for some
that mr . 1 for diamagnetic and paramagnetic materials. Thus, we may regard diamagnetic
and paramagnetic materials as linear and nonmagnetic. Ferromagnetic materials are always
nonlinear and magnetic except when their temperatures are above curie temperature (to be
explained later). The reason for this will become evident as we more closely examine each
of these three types of magnetic material.
Diamagnetism occurs when the magnetic fields in a material that are due to electronic
motions of orbiting and spinning completely cancel each other. Thus, the permanent (or
­in­trinsic) magnetic moment of each atom is zero and such materials are weakly affected
by a magnetic field. For most diamagnetic materials (e.g., bismuth, lead, copper, silicon,
diamond, sodium chloride), xm is of the order of 21025. In certain materials, called super­
conductors, “perfect diamagnetism” occurs at temperatures near absolute zero: xm 5 21
or mr 5 0 and B 5 0. Thus superconductors cannot contain magnetic fields.2 Except for
superconductors, the diamagnetic properties of materials are seldom used in practice.
Although the diamagnetic effect is overshadowed by other stronger effects in some materi­
als, all materials exhibit diamagnetism.
2 An excellent treatment of superconductors is found in M. A. Plonus, Applied Electromagnetics. New York:
McGraw-Hill, 1978, pp. 375–388. Also, the August 1989 issue of the Proceedings of IEEE is devoted to
­superconductivity.
Figure 8.13. A material is said to be diamagnetic if it has m
materials. From Table B.3, it is apparent that for most practical purposes we may assume
8.6 Classification of Materials  373
Materials whose atoms have nonzero permanent magnetic moment may be paramag­
netic or ferromagnetic. Paramagnetism occurs when the magnetic fields produced in a
­material by orbital and spinning electrons do not cancel completely. Unlike diamagnetism,
paramagnetism is temperature dependent. For most paramagnetic materials (e.g., air,
platinum, tungsten, potassium), Xm is of the order 11025 to 11023 and is temperature
dependent. Such materials find application in masers.
Ferromagnetism occurs in materials whose atoms have relatively large permanent mag­
netic moment. They are called ferromagnetic materials because the best-known member is
iron. Other members are cobalt, nickel, and their alloys. Ferromagnetic materials are very
useful in practice. As distinct from diamagnetic and paramagnetic materials, ferromagnetic
materials have the following properties:
1.	 They are capable of being magnetized very strongly by a magnetic field.
2.	 They retain a considerable amount of their magnetization when removed from the field.
3.	 They lose their ferromagnetic properties and become linear paramagnetic materi­
als when the temperature is raised above a certain temperature known as the curie
temperature. Thus if a permanent magnet is heated above its curie temperature
(770°C for iron), it loses its magnetization completely.
4.	 They are nonlinear; that is, the constitutive relation B 5 momrH does not hold for
ferromagnetic materials because mr depends on B and cannot be represented by a
single value.
Thus, the values of mr cited in Table B.3 for ferromagnetics are only typical. For example,
for nickel mr 5 50 under some conditions and 600 under other conditions.
As mentioned in Section 5.9 for conductors, ferromagnetic materials, such as iron
and steel, are used for screening (or shielding) to protect sensitive electrical devices from
disturbances from strong magnetic fields. In the example of a typical iron shield shown in
­Figure 8.14(a), the compass is protected. Without the iron shield, as in Figure 8.14(b), the
compass gives an erroneous reading owing to the effect of the external magnetic field. For
perfect screening, it is required that the shield have infinite permeability.
Even though B 5 mo1H 1 M2 holds for all materials including ferromagnetics, the
relationship between B and H depends on previous magnetization of a ferromagnetic
material—its “magnetic history.” Instead of having a linear relationship between B and H
(i.e., B 5 mH), it is only possible to represent the relationship by a magnetization curve or
B–H curve.
Materials
FIGURE 8.13  Classification of materials.
374  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
A typical B–H curve is shown in Figure 8.15. First, note the nonlinear relationship
between B and H. Second, at any point on the curve, m is given by the ratio B/H and not
by dB/dH, the slope of the curve.
If we assume that the ferromagnetic material whose B–H curve in Figure 8.15 is ini-
tially unmagnetized, as H increases (owing to increase in current) from O to maximum
­applied field intensity Hmax, curve OP is produced. This curve is referred to as the virgin
or initial magnetization curve. After reaching saturation at P, if H is decreased, B does not
­follow the initial curve but lags behind H. This phenomenon of B lagging behind H is called
hysteresis (which means “to lag” in Greek).
If H is reduced to zero, B is not reduced to zero but to Br, which is referred to as the per-
manent flux density. The value of Br depends on Hmax, the maximum applied field ­intensity.
The existence of Br is the cause of having permanent magnets. If H increases negatively (by
reversing the direction of current), B becomes zero when H becomes Hc, which is known as
the coercive field intensity. Materials for which Hc is small are said to be magnetically hard.
The value of Hc also depends on Hmax.
FIGURE 8.14  Magnetic screening: (a) iron shield protecting a small compass,
(b) compass gives erroneous reading without the shield.
FIGURE 8.15  Typical magnetization (B–H) curve.
8.6 Classification of Materials  375
Further increase in H in the negative direction to reach Q and a reverse in its direc­
tion to reach P gives a closed curve called a hysteresis loop. Hysteresis loops vary in shape
from one material to another. Some ferrites, for example, have an almost rectangular
hysteresis loop and are used in digital computers as magnetic information storage ­devices.
The area of a hysteresis loop gives the energy loss (hysteresis loss) per unit volume during
one cycle of the periodic magnetization of the ferromagnetic material. This energy loss
is in the form of heat. It is therefore desirable that materials used in electric generators,
motors, and transformers have tall but narrow hysteresis loops so that hysteresis losses
are minimal.
Region 0 # z # 2 m is occupied by an infinite slab of permeable material 1mr 5 2.52. If
B 5 10yax 2 5xay mWb/m2 within the slab, determine: (a) J, (b) Jb, (c) M, (d) Kb on z 5 0.
Solution:
(a)	 By definition,
J 5 = 3 H 5 = 3
momr
4p 3 102712.52 a
'By
'x 2 'Bx
'y baz
5 106
p  125 2 1021023az 5 24.775az kA/m2
(b)	    Jb 5 xmJ 5 1mr 2 12J 5 1.5124.775az2 # 103
5 27.163az kA/m2
(c)	  M 5 xmH 5 xm
momr
1.5110yax 2 5xay2 # 1023
4p 3 102712.52
5 4.775yax 2 2.387xay kA/m
(d)	 Kb 5 M 3 an. Since z 5 0 is the lower side of the slab occupying 0 # z # 2, an 5 2az.
Hence,
Kb 5 14.775yax 2 2.387xay2 3 12az2
5 2.387xax 1 4.775yay kA/m
EXAMPLE 8.7
PRACTICE EXERCISE  8.7
In a certain region (m  4.6mo),
B  10eyaz mWb/m2
find: (a) xm, (b) H, (c) M.
Answer:  (a) 3.6,  (b) 1730eyaz A/m,  (c) 6228eyaz A/m.
376  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
We define magnetic boundary conditions as the conditions that H (or B) field must satisfy
at the boundary between two different media. Our derivations here are similar to those in
Section 5.9. We make use of Gauss’s law for magnetic fields
B # dS 5 0
(8.38)
and Ampère’s circuit law
H # dl 5 I
(8.39)
Consider the boundary between two magnetic media 1 and 2, characterized, respec-
tively, by m1 and m2 as in Figure 8.16. Applying eq. (8.38) to the pillbox (Gaussian surface)
of Figure 8.16(a) and allowing Dh S  0, we obtain
B1n DS 2 B2n DS 5 0
(8.40)
Thus
B1n 5 B2n    or    m1H1n 5 m2H2n
(8.41)
since B 5 mH. Equation (8.41) shows that the normal component of B is continuous at the
boundary. It also shows that the normal component of H is discontinuous at the boundary;
H undergoes some change at the interface.
Similarly, we apply eq. (8.39) to the closed path abcda of Figure 8.16(b), where surface
current K on the boundary is assumed normal to the path. We obtain
K # Dw 5 H1t # Dw 1 H1n # Dh
2 1 H2n # Dh
8.7  MAGNETIC BOUNDARY CONDITIONS
FIGURE 8.16  Boundary conditions between two magnetic media: (a) for B, (b) for H.
8.7 Magnetic Boundary Conditions  377
2H2t # Dw 2 H2n # Dh
2 2 H1n # Dh
(8.42)
As Dh S  0, eq. (8.42) leads to
H1t 2 H2t 5 K
(8.43)
This shows that the tangential component of H is also discontinuous. Equation (8.43) may
be written in terms of B as
B1t
2 B2t
5 K
(8.44)
In the general case, eq. (8.43) becomes
1H1 2 H22 3 an12 5 K
(8.45)
where an12 is a unit vector normal to the interface and is directed from medium 1 to
medium 2. If the boundary is free of current or the media are not conductors (for K is free
current density), K 5 0 and eq. (8.43) becomes
H1t 5 H2t        or        B1t
5 B2t
(8.46)
Thus the tangential component of H is continuous while that of B is discontinuous at the
boundary.
If the fields make an angle u with the normal to the interface, eq. (8.41) results in
B1 cos u1 5 B1n 5 B2n 5 B2 cos u2
(8.47)
while eq. (8.46) produces
sin u1 5 H1t 5 H2t 5 B2
sin u2
(8.48)
Dividing eq. (8.48) by eq. (8.47) gives
tan u1
tan u2
5 m1
(8.49)
which is [similar to eq. (5.65)] the law of refraction for magnetic flux lines at a boundary
with no surface current.
Given that H1 5 22ax 1 6ay 1 4az A/m in region y 2 x 2 2 # 0, where m1 5 5mo,
­calculate
(a)	 M1 and B1
(b)	 H2 and B2 in region y 2 x 2 2 $ 0, where m2 5 2mo
EXAMPLE 8.8
378  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Solution:
Since y 2 x 2 2 5 0 is a plane, y 2 x # 2 or y # x 1 2 is region 1 in Figure 8.17. A
point in this region may be used to confirm this. For example, the origin 10, 02 is in this
region because 0 2 0 2 2 , 0. If we let the surface of the plane be described by f 1x, y2 5
y 2 x 2 2, a unit vector normal to the plane is given by
an 5
0=f 0 5
ay 2 ax
(a)
M1 5 xm1H1 5 1mr1 2 12 H1 5 15 2 12 122, 6, 42
5 28ax 1 24ay 1 16az A/m
B1 5 m1H1 5 momr1H1 5 4p 3 1027152 122, 6, 42
5 212.57ax 1 37.7ay 1 25.13az m Wb/m2
(b)	 H1n 5 1H1 # an2an 5 c 122, 6, 42 # 121, 1, 02
121, 1, 02
5 24ax 1 4ay
But
H1 5 H1n 1 H1t
Hence,
H1t 5 H1 2 H1n 5 122, 6, 42 2 124, 4, 02
5 2ax 1 2ay 1 4az
Using the boundary conditions, we have
H2t 5 H1t 5 2ax 1 2ay 1 4az
B2n 5 B1n S  m2H2n 5 m1H1n
µ2  2µ0
FIGURE 8.17  For Example 8.8.
8.7 Magnetic Boundary Conditions  379
H2n 5 m1
H1n 5 5
2 124ax 1 4ay2 5 210ax 1 10ay
Thus
H2 5 H2n 1 H2t 5 28ax 1 12ay 1 4az A/m
and
B2 5 m2H2 5 momr2H2 5 14p 3 10272 122 128, 12, 42
5 220.11ax 1 30.16ay 1 10.05az m Wb/m2
PRACTICE EXERCISE    8.8
Region 1, described by 3x 1 4y $ 10, is free space, whereas region 2, described
by 3x 1 4y # 10, is a magnetic material for which m . 10mo. Assuming that
the boundary between the material and free space is current free, find B2 if
B1 5 0.1ax 1 0.4ay 1 0.2az Wb/m2.
Answer:  21.052ax 1 1.264ay 1 2az Wb/m2.
The xy-plane serves as the interface between two different media. Medium 1 1z , 02 is
filled with a material whose mr 5 6, and medium 2 1z . 02 is filled with a material whose
mr 5 4. If the interface carries current 11/mo2 ay mA/m, and B2 5 5ax 1 8az mWb/m2,
find H1 and B1.
Solution:
In Example 8.8, K 5 0, so eq. (8.46) was appropriate. In this example, however, K 2 0, and
we must resort to eq. (8.45) in addition to eq. (8.41). Consider the problem as illustrated in
Figure 8.18. Let B1 5 1Bx, By, Bz2 in mWb/m2.
B1n 5 B2n 5 8az S  Bz 5 8
(8.9.1)
But
H2 5 B2
4mo
15ax 1 8az2mA/m
(8.9.2)
and
H1 5 B1
6mo
1Bxax 1 Byay 1 Bzaz2 mA/m
(8.9.3)
EXAMPLE 8.9
380  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Having found the normal components, we can find the tangential components by using
1H1 2 H22 3 an12 5 K
H1 3 an12 5 H2 3 an12 1 K
(8.9.4)
Substituting eqs. (8.9.2) and (8.9.3) into eq. (8.9.4) gives
6mo
1Bxax 1 Byay 1 Bzaz2 3 az 5
4mo
15ax 1 8az2 3 az 1 1
Equating components yields
By 5 0,  2Bx
5 25
4 1 1,   or  Bx 5 6
4 5 1.5
(8.9.5)
From eqs. (8.9.1) and (8.9.5), we have
B1 5 1.5ax 1 8az mWb/m2
H1 5 B1
5 1
10.25ax 1 1.33az2 mA/m
and
H2 5 1
11.25ax 1 2az2 mA/m
Note that H1x is 1/mo mA/m less than H2x because of the current sheet and also that
B1n 5 B2n.
FIGURE 8.18  For Example 8.9.
PRACTICE EXERCISE    8.9
A unit normal vector from region 2 1m 5 2mo2 to region 1 1m 5 mo2 is an21 5
16ax 1 2ay 2 3az2/7. If H1 5 10ax 1 ay 1 12az A/m and H2 5 H2xax 2 5ay 14az A/m,
determine
8.8 Inductors and Inductances  381
A circuit (or closed conducting path) carrying current I produces a magnetic field B that
causes a flux C 5 e B # dS to pass through each turn of the circuit as shown in Figure 8.19.
If the circuit has N identical turns, we define the flux linkage l as
l 5 N C
(8.50)
Also, if the medium surrounding the circuit is linear, the flux linkage l is proportional to
the current I producing it; that is,
l ~  I
l 5 LI
(8.51)
where L is a constant of proportionality called the inductance of the circuit. The inductance
L is a property of the physical arrangement of the circuit. It is the ability of the physical
arrangement to store magnetic energy. A circuit or part of a circuit that has inductance is
called an inductor. The inductance L of an inductor is the ratio of the magnetic flux linkage
 to the current I through the inductor.
The unit of inductance is the henry (H), which is the same as webers per ampere. Since the
henry is a fairly large unit, inductances are usually expressed in millihenrys (mH).
(a)  H2x
(b)  The surface current density K on the interface
(c)  The angles B1 and B2 make with the normal to the interface
Answer:  (a) 5.833,  (b) 4.86ax 2 8.64ay 1 3.95az A/m,  (c) 76.27°, 77.62°.
8.8  INDUCTORS AND INDUCTANCES
FIGURE 8.19  Magnetic field B produced by a circuit.
L 5 l
I 5 N
(8.52)
382  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
The inductance defined by eq. (8.52) is commonly referred to as self-inductance, since
regarded as a measure of how much magnetic energy is stored in an inductor. The magnetic
energy (in joules) stored in an inductor is expressed in circuit theory as
Wm 5 1
2LI2
(8.53)
L 5 2Wm
I2 
(8.54)
Thus the self-inductance of a circuit may be defined or calculated from energy
­considerations.
If instead of having a single circuit, we have two circuits carrying current I1 and I2 as
shown in Figure 8.20, a magnetic interaction exists between the circuits. Four component
fluxes C11, C12, C21, and C22 are produced. The flux C12, for example, is the flux passing
through circuit 1 due to current I2 in circuit 2. If B2 is the magnetic flux density due to I2
and S1 is the area of circuit 1, then
FIGURE 8.20  Magnetic interaction between
two circuits.
12 5 3
B2 # dS
(8.55)
M12 5 l12
5 N112
(8.56)
Similarly, the mutual inductance M21 is defined as the flux linkages of circuit 2 per unit
current I1; that is,
M21 5 l21
5 N221
(8.57a)
the linkages are produced by the inductor itself. Like capacitance, inductance may be
The mutual inductance M12 is the ratio of the flux linkage
on circuit 1 to
current I2.
l12 5 N112
8.8 Inductors and Inductances  383
It can be shown by using energy concepts that if the medium surrounding the circuits is
linear (i.e., in the absence of ferromagnetic material),
M12 5 M21
(8.57b)
The mutual inductance M12 or M21 is expressed in henrys and should not be confused with
the magnetization vector M expressed in amperes per meter. Mutual inductance is funda­
mental to the operation of transformers.
We define the self-inductance of circuits 1 and 2, respectively, as
where C1 5 C11 1 C12 and C2 5 C21 1 C22. The total energy in the magnetic field is the
sum of the energies due to L1, L2, and M12 (or M21); that is,
Wm 5 W1 1 W2 1 W12
5 1
2 L1I1
2 1 1
2 L2I2
2 6 M12I1I2
(8.60)
The positive sign is taken if currents I1 and I2 flow such that the magnetic fields of the two
circuits strengthen each other. If the currents flow such that their magnetic fields oppose
each other, the negative sign is taken.
As mentioned earlier, an inductor is a conductor arranged in a shape appropriate to store
magnetic energy. Typical examples of inductors are toroids, solenoids, coaxial transmission
lines, and parallel-wire transmission lines. The inductance of each of these inductors can be
determined by following a procedure similar to that taken in determining the capacitance of
a capacitor. For a given inductor, we find the self-inductance L by taking these steps:
1.	 Choose a suitable coordinate system.
2.	 Let the inductor carry current I.
The mutual inductance between two circuits may be calculated by taking a similar
procedure.
In an inductor such as a coaxial or a parallel-wire transmission line, the inductance
produced by the flux internal to the conductor is called the internal inductance Lin while
that produced by the flux external to it is called external inductance Lext. The total induc­
tance L is
L1 5 l11
5 N11
(8.58)
and
L2 5 l22
5 N22
(8.59)
3. Determine B from Biot–Savart’s law (or from Ampère’s law if symmetry exists)
and calculate  from  5
4. Finally fi nd L from L 5 l
I 5 N
I .
eS B # dS.
384  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
L 5 Lin 1 Lext
(8.61)
Just as it was shown that for capacitors
RC 5 e
(6.35)
it can be shown that
LextC 5 me
(8.62)
Thus Lext may be calculated using eq. (8.62) if C is known.
A collection of formulas for some fundamental circuit elements is presented in
Table 8.3. All formulas can be derived by taking the steps just outlined.3
Just as the potential energy in an electrostatic field was derived as
WE 5 1
2 3 D # E dv 5 1
2 3 eE2 dv
(4.96)
we would like to derive a similar expression for the energy in a magnetostatic field. A
simple approach is using the magnetic energy in the field of an inductor. From eq. (8.53),
Wm 5 1
2LI2
(8.53)
The energy is stored in the magnetic field B of the inductor. We would like to express
eq. (8.53) in terms of B or H.
3 Additional formulas can be found in standard electrical handbooks or in H. Knoepfel, Pulsed High
Magnetic Fields. Amsterdam: North-Holland, 1970, pp. 312–324.
8.9  MAGNETIC ENERGY
FIGURE 8.21  A differential
volume in a magnetic field.
TABLE 8.3  A Collection of Formulas for Inductance of Common Elements
386  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Consider a differential volume in a magnetic field as shown in Figure 8.21. Let the
volume be covered with conducting sheets at the top and bottom surfaces with current I.
We assume that the whole region is filled with such differential volumes. From eq. (8.52),
each volume has an inductance
where DI 5 H Dy. Substituting eq. (8.63) into eq. (8.53), we have
DWm 5 1
2DL DI2 5 1
2 mH2 Dx Dy Dz
(8.64)
DWm 5 1
2 mH2 Dv
The magnetostatic energy density wm (in J/m3) is defined as
wm 5
lim
DvS0 DWm
5 1
2 mH2
Hence,
wm 5 1
2mH2 5 1
2 B # H 5 B2
2m
(8.65)
Thus the energy in a magnetostatic field in a linear medium is
Wm 5 3 wm dv
Wm 5 1
2 3 B # H dv 5 1
2 3 mH2 dv
(8.66)
which is similar to eq. (4.96) for an elctrostatic field.
Calculate the self-inductance per unit length of an infinitely long solenoid.
Solution:
We recall from Example 7.4 that for an infinitely long solenoid, the magnetic flux inside
the solenoid per unit length is
B 5 mH 5 mIn
EXAMPLE 8.10
DL 5 D
DI 5 mH Dx Dz
(8.63)
8.9 Magnetic Energy  387
where n 5 N/, 5 number of turns per unit length. If S is the cross-sectional area of the
­solenoid, the total flux through the cross section is
and thus the inductance per unit length is
Lr 5 L
, 5 lr
I 5 mn2S
Lr 5 mn2S        H/m
EXAMPLE 8.11
PRACTICE EXERCISE  8.10
A very long solenoid with 2 3 2 cm cross section has an iron core 1mr 5 10002 and
4000 turns per meter. It carries a current of 500 mA. Find the following:
(a)  Its self-inductance per meter
(b)  The energy per meter stored in its field
Answer:  (a) 8.042 H/m,  (b) 1.005 J/m.
Determine the self-inductance of a coaxial cable of inner radius a and outer radius b.
Solution:
The self-inductance of the inductor can be found in two different ways: by taking the four
steps given in Section 8.8 or by using eqs. (8.54) and (8.66).
Method 1: Consider the cross section of the cable as shown in Figure 8.22. We recall from
eq. (7.29) that by applying Ampère’s circuit law, we obtained for region 1 10 # r # a2,
B1 5 mIr
2pa2 af
and for region 2 1a # r # b2,
B2 5 mI
2pr af
We first find the internal inductance Lin by considering the flux linkages due to the inner
conductor. From Figure 8.22(a), the flux leaving a differential shell of thickness dr is
5 BS 5 mInS
Since this flux is only for a unit length of the solenoid, the linkage per unit length is
lr 5 l
, 5 n 5 mn2IS
388  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
because I is uniformly distributed over the cross section for dc excitation. Thus, the total
flux linkages within the differential flux element are
dl1 5 mIr dr dz
2pa2
# r2
For length  of the cable,
l1 5 3
r50
z50
mIr3 dr dz
2pa4
5 mI,
Lin 5 l1
I 5 m,
(8.11.1)
The internal inductance per unit length, given by
Lrin 5 Lin
, 5 m
8p        H/m
(8.11.2)
We now determine the external inductance Lext by considering the flux linkages between
the inner and the outer conductor as in Figure 8.22(b). For a differential shell of thickness dr,
FIGURE 8.22  Cross section of the coaxial cable: (a) for region 1,
0 , r , a, (b) for region 2, a , r , b; for Example 8.11.
d1 5 B1 dr dz 5 mIr
2pa2 dr dz
The flux linkage is dΨ1 multiplied by the ratio of the area within the path enclosing the flux
to the total area, that is,
dl1 5 d1 # Ienc
5 d1 # pr2
pa2
d2 5 B2 dr dz 5 mI
2pr dr dz
is independent of the radius of the conductor or wire. Since the inductance does not depend
cable to finding the inductance of any infinitely long straight conductor of finite radius.
on a, we can make the wire as thin as possible. Thus eqs. (8.11.1) and (8.11.2) are also appli-
8.9 Magnetic Energy  389
In this case, the total current I is enclosed within the path enclosing the flux. Hence,
Lext 5 l2
I 5 m,
2p ln b
Thus
L 5 Lin 1 Lext 5 m,
2p c 1
4 1 ln b
a d
or the inductance per length is
Lr 5 L
, 5 m
2p c 1
4 1 ln b
a d        H/m
Method 2: It is easier to use eqs. (8.54) and (8.66) to determine L, that is,
Wm 5 1
2 LI2  or  L 5 2Wm
where
Wm 5 1
2 3 B # H dv 5 3 B2
2m dv
Hence
Lin 5 2
I2 3
2m dv 5 1
I2m 9  m2I2r2
4p2a4 r dr df dz
4p2a4 3
dz 3
df 3
r3 dr 5 m,
Lext 5 2
I2 3
2m dv 5 1
I2m 9  m2I
4p2r2 r dr df dz
5 m
4p2 3
dz 3
df 3
r 5 m,
2p ln b
and
L 5 Lin 1 Lext 5 m,
2p c 1
4 1 ln b
a d
as obtained previously.
l2 5 2 5 3
r5a
z50
mI dr dz
2pr
5 mI,
2p  ln b
390  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Determine the inductance per unit length of a two-wire transmission line with separation
Solution:
We use the two methods of Example 8.11.
Method 1:  We determine Lin just as we did in Example 8.11. Thus for region 0 # r # a,
we obtain
l1 5 mI,
as before. For region a # r # d 2 a, the flux linkages between the wires are
The flux linkages produced by wire 1 are
l1 1 l2 5 mI,
8p 1 mI,
2p  ln d 2 a
l 5 21l1 1 l22 5 mI,
p  c 1
4 1 ln d 2 a
d 5 LI
If d W a, the self-inductance per unit length is
Lr 5 L
, 5 m
p c 1
4 1 ln d
a d        H/m
Method 2:  From Example 8.11, we have
Lin 5 m,
PRACTICE EXERCISE    8.11
Calculate the self-inductance of the coaxial cable of Example 8.11 if the space ­between
the line conductor and the outer conductor is made of an inhomogeneous material
having m 5 2mo/11 1 r2.
Answer:  mo,
8p 1 mo,
p clnb
a 2 ln
11 1 b2
11 1 a2 d .
EXAMPLE 8.12
l2 5 2 5 3
d2a
r5a
z50
2pr dr dz 5 mI,
2p  ln d 2 a
distance d. Each wire has radius a as shown in Figure 11.2 (b).
By symmetry, the same amount of flux is produced by current 2I in wire 2. Hence the
total linkages are
8.9 Magnetic Energy  391
Now
Lext 5 2
I2 3 B2 dv
5 1
I2m 9  m2I2
4p2r2 r dr df dz
5 m
4p2 3
dz 3
df 3
d2a
5 m,
2p ln d 2 a
Since the two wires are symmetrical,
L 5 2 1Lin 1 Lext2
5 m,
p  c 1
4 1 ln d 2 a
d H
as obtained earlier.
PRACTICE EXERCISE    8.12
Two #10 copper wires (2.588 mm in diameter) are placed parallel in air with a sepa­
ration distance d between them. If the inductance of each wire is 1.2 mH/m, calculate
(a)  Lin and Lext per meter for each wire
(b)  The separation distance d
Answer:  (a) 0.05 and 115 mH/m,  (b) 40.79 cm.
Two coaxial circular wires of radii a and b 1b . a2 are separated by distance h 1h W a, b2
as shown in Figure 8.23. Find the mutual inductance between the wires.
Solution:
Let current I1 flow in wire 1. At an arbitrary point P on wire 2, the magnetic vector potential
due to wire 1 is given by eq. (8.21a), namely
A1 5 mI1a2 sin u
4r2
af 5
mI1a2baf
43h2 1 b243/2
If h W b
A1 . mI1a2b
4h3  af
EXAMPLE 8.13
392  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
PRACTICE EXERCISE    8.13
Find the mutual inductance of two coplanar concentric circular loops of radii 2 m
and 3 m.
Answer:  2.632 mH.
†8.10  MAGNETIC CIRCUITS
The concept of magnetic circuits is based on solving some magnetic field problems by using
a circuit approach. Magnetic devices such as toroids, transformers, motors, generators, and
relays may be considered as magnetic circuits. The analysis of such circuits is made simple if an
analogy between magnetic circuits and electric circuits is exploited. Once this has been done,
we can directly apply concepts in electric circuits to solve their analogous magnetic circuits.
The analogy between magnetic and electric circuits is summarized in Table 8.4 and
portrayed in Figure 8.24. The reader is advised to pause and study Table 8.4 and Figure 8.24.
First, we notice from Table 8.4 that two terms are new. We define the magnetomotive force
(mmf) , in ampere-turns (A # t), as
FIGURE 8.23  Two coaxial circular wires;
for ­Exam­ple 8.13.
Hence,
12 5 C A1 # dl2 5 mI1a2b
4h3  2pb 5 mpI1a2b2
2h3
and
M12 5 12
5 mpa2b2
2h3
8.10 Magnetic Circuits  393
5 NI 5 C H # dl
(8.67)
The source of mmf in magnetic circuits is usually a coil-carrying current as in Figure 8.24.
We also define reluctance , in ampere-turns per weber, as
5 ,
mS
(8.68)
where  and S are, respectively, the mean length and the cross-sectional area of the mag­
netic core. The reciprocal of reluctance is permeance . The basic relationship for circuit
elements is Ohm’s law 1V 5 IR2:
^ 5  5
(8.69)
Based on this, Kirchhoff’s current and voltage laws can be applied to nodes and loops of
a given magnetic circuit just as in an electric circuit. The rules of adding voltages and for
TABLE 8.4  Analogy between Electric and Magnetic Circuits
Electric
Magnetic
FIGURE 8.24  Analogy between
(a) an electric circuit and (b) a
magnetic circuit.
Conductivity
Permeability 
Field intensity E
Field intensity H
Current I 5 e J # dS
Magnetic fl ux  5 e B # dS
Current density J 5 I
S 5 sE
Flux density B 5
S 5 mH
Electromotive force (emf) V
Magnetomotive force (mmf) 
Resistance R
Reluctance 
Conductance G 5 1
Permeance  5 1
Ohm’s law R 5 V
I 5 ,
Ohm’s law  5 
5 ,
or    V 5 E, 5 IR
or     5 H, 5   5 NI
Kirchhoff ’s laws:
g I 5 0
Kirchhoff ’s laws:
g  5 0
g V 2 g RI 5 0
g  2 g   5 0
394  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
combining series and parallel resistances also hold for mmfs and reluctances. Thus for n
magnetic circuit elements in series
Some differences between electric and magnetic circuits should be pointed out. Unlike
an electric circuit, where the current I flows, magnetic flux does not flow. Also, conduc­
tivity s is independent of current density J in an electric circuit, whereas permeability m
varies with flux density B in a magnetic circuit. This is because ferromagnetic (nonlinear)
materials are normally used in most practical magnetic devices. These differences not­
withstanding, the magnetic circuit concept serves in the approximate analysis of practical
magnetic devices.
†8.11  FORCE ON MAGNETIC MATERIALS
It is of practical interest to determine the force that a magnetic field exerts on a piece of
magnetic material in the field. This is useful in electromechanical systems such as elec­
tromagnets, relays, and rotating machines and in magnetic levitation (see Section 8.12).
Consider, for example, an electromagnet made of iron of constant relative permeability as
shown in Figure 8.25. The coil has N turns and carries a current I. If we ignore fringing,
the magnetic field in the air gap is the same as that in iron 1B1n 5 B2n2. To find the force
between the two pieces of iron, we calculate the change in the total energy that would result
were the two pieces of the magnetic circuit separated by a differential displacement dl. The
work required to effect the displacement is equal to the change in stored energy in the air
gap (assuming constant current), that is,
(8.74)
where S is the cross-sectional area of the gap, the factor 2 accounts for the two air gaps,
and the negative sign indicates that the force acts to reduce the air gap (or that the force is
­attractive). Thus
1 5 2 5 3 5  . . . 5 n
(8.70)
and
 5 1 1 2 1 . . . 1 n
(8.71)
For n magnetic circuit elements in parallel,
5 1 1 2 1 3 1 . . . 1 n
(8.72)
and
1 5 2 5 3 5 . . . 5 n
(8.73)
2 F dl 5 dWm 5 2 c 1B2
2mo
S dld
8.11 Force on Magnetic Materials  395
F 5 22a B2S
2mo
b 
(8.75)
Note that the force is exerted on the lower piece and not on the current-carrying upper piece
giving rise to the field. The tractive force across a single gap can be obtained from eq. (8.75) as
F 5 2B2S
2mo
(8.76)
Notice the similarity between eq. (8.76) and that derived in Example 5.8 for electrostatic
case. Equation (8.76) can be used to calculate the forces in many types of devices includ­
ing relays, rotating machines, and magnetic levitation. The tractive pressure (in N/m2) in
a magnetized surface is
p 5 F
S 5 B2
2mo
5 1
2BH
(8.77)
which is the same as the enery density wm in the air gap.
The toroidal core of Figure 8.26(a) has ro 5 10 cm and a circular cross section with
a 5 1 cm. If the core is made of steel 1m 5 1000 mo2 and has a coil with 200 turns, calcu­
late the amount of current that will produce a flux of 0.5 mWb in the core.
Solution:
This problem can be solved in two different ways: by using the magnetic field approach
(direct) or by using the electric circuit analog (indirect).
Method 1:  Since ro is large compared with a, from Example 7.6,
B 5 mNI
5 momrNI
2pro
FIGURE 8.25  An electromagnet.
EXAMPLE 8.14
396  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
Hence,
as obtained with Method 1.
FIGURE 8.26  (a) Toroidal core of Example 8.14. (b) Its equivalent
electric circuit analog.
PRACTICE EXERCISE    8.14
A conductor of radius a is bent into a circular loop of mean radius ro (see Figure 8.26(a)).
If ro 5 10 cm and 2a 5 1 cm, calculate the internal inductance of the loop.
Answer:  31.42 nH.
5 BS 5 momrNI pa2
2pro
I 5
2ro
momrNa2 5
2110 3 10222 10.5 3 10232
4p 3 1027110002 12002 11 3 10242
5 100
5 3.979 A
Method 2: The toroidal core in Figure 8.26(a) is analogous to the electric circuit of
 5 NI 5  5  ,
mS 5  2pro
momrpa2
I 5
2ro
momrNa2 5 3.979 A
Figure 8.26(b). From the circuit and Table 8.4,
8.11 Force on Magnetic Materials  397
In the magnetic circuit of Figure 8.27, calculate the current in the coil that will produce
a magnetic flux density of 1.5 Wb/m2 in the air gap, assuming that m 5 50mo and that all
branches have the same cross-sectional area of 10 cm2.
Solution:
The magnetic circuit of Figure 8.27 is analogous to the electric circuit of Figure 8.28. In
Figure 8.27, 1, 2, 3, and a are the reluctances in paths 143, 123, 35 and 16, and 56
(air gap), respectively. Thus
EXAMPLE 8.15
FIGURE 8.27  Magnetic circuit for
Ex­am­ple 8.15.
1 5 2 5
momrS 5
30 3 1022
14p 3 10272 1502 110 3 10242
5 3 3 108
20p
3 5
9 3 1022
14p 3 10272 1502 110 3 10242 5 0.9 3 108
20p
a 5
1 3 1022
14p 3 10272 112 110 3 10242 5 5 3 108
20p
We combine 1 and 2 as resistors in parallel. Hence,
1 y 2 5
12
1 1 2
5 1
2 5 1.5 3 108
20p
The total reluctance is
T 5 a 1 3 1 1 y 2 5 7.4 3 108
20p
The mmf is
 5 NI 5 aT
398  CHAPTER 8  MAGNETIC FORCES, MATERIALS, AND DEVICES
PRACTICE EXERCISE  8.15
The toroid of Figure 8.26(a) has a coil of 1000 turns wound on its core. If ro 5 10 cm
and a 5 1 cm, find the current required to establish a magnetic flux of 0.5 mWb
(a)  If the core is nonmagnetic
(b)  If the core has mr 5 500
Answer:  (a) 795.8 A,  (b) 1.592 A.
FIGURE 8.28  Electric circuit analog of the magnetic circuit in
Figure 8.27.
A U-shaped electromagnet shown in Figure 8.29 is designed to lift a 400 kg mass (which
includes the mass of the keeper). The iron yoke 1mr 5 30002 has a cross section of 40 cm2
and mean length of 50 cm, and the air gaps are each 0.1 mm long. Neglecting the reluctance
of the keeper, calculate the number of turns in the coil when the excitation current is 1 A.
Solution:
The tractive force across the two air gaps must balance the weight. Hence
F 5 2
1Ba
2S2
2mo
5 mg
2 5
mgmo
5 400 3 9.8 3 4p 3 1027
40 3 1024
Ba 5 1.11 Wb/m2
EXAMPLE 8.16
But a 5  5 BaS. Hence
I 5 BaST
5 1.5 3 10 3 1024 3 7.4 3 108
400 3 20p
5 44.16 A

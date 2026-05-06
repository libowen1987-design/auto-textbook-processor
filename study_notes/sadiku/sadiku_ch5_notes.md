# Sadiku《Elements of Electromagnetics》Chapter 5

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 204-251 of 926 (926 total)

---

## Electric Fields in Material Space

177
C H A P T E R
177
5.1  INTRODUCTION
5.2  PROPERTIES OF MATERIALS
In the last chapter, we considered electrostatic fields in free space or a space that has no
materials in it. Thus what we have developed so far under electrostatics may be regarded as
the “vacuum” field theory. By the same token, what we shall develop in this chapter may be
regarded as the theory of electric phenomena in material space. As will soon be evident, most of
the formulas derived in Chapter 4 are still applicable, though some may require modification.
Just as electric fields can exist in free space, they can exist in material media. Materials
are broadly classified in terms of their electrical properties as conductors and nonconduc­
tors. Nonconducting materials are usually referred to as insulators or dielectrics. A brief
discussion of the electrical properties of materials in general will be given to provide a basis
for ­understanding the concepts of conduction, electric current, and polarization. Further
discussion will be on some properties of dielectric materials such as susceptibility, permit­
tivity, linearity, isotropy, homogeneity, dielectric strength, and relaxation time. The concept
of boundary conditions for electric fields existing in two different media will be ­introduced.
In a broad sense, materials may be classified in terms of their conductivity s, in mhos per
meter (
/m) or, more usually siemens per meter (S/m), as conductors and nonconductors,
or technically as metals and insulators (or dielectrics). The conductivity of a material usually
ELECTRIC FIELDS IN
MATERIAL SPACE
Knowledge will forever govern ignorance:  and a people who mean to be their own
Governors, must arm themselves with the power which knowledge gives.
—JAMES MADISON
A discussion of the electrical properties of materials may seem out of place in a text of this
kind. But questions such as why an electron does not leave a conductor surface, why a cur-
rent-carrying wire remains uncharged, why materials behave differently in an electric field,
and why waves travel with less speed in conductors than in dielectrics are easily answered
by considering the electrical properties of materials. A thorough discussion of this subject is
usually found in texts on physical electronics. Here, a brief discussion will suffice to help us
understand the mechanism by which materials influence an electric field.
178  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
depends on temperature and frequency. A material with high conductivity 1s W 12 is referred
to as a metal, whereas one with low conductivity 1s V 12 is referred to as an insulator. A
material whose conductivity lies somewhere between those of metals and insulators is called a
semiconductor. The values of conductivity of some common materials are shown in Table B.1 in
Appendix B. From this table, it is clear that materials such as ­copper and aluminum are metals,
silicon and germanium are semiconductors, and glass and rubber are insulators.
The conductivity of metals generally increases with decrease in temperature. At tem­
peratures near absolute zero 1T 5 0 K2, some conductors exhibit infinite conductivity and
are called superconductors. Lead and aluminum are typical examples of such metals. The
conductivity of lead at 4 K is of the order of 1020 S/m. The interested reader is referred to
the literature on superconductivity.1
We shall be concerned only with metals and insulators in this text. Microscopically, the
major difference between a metal and an insulator lies in the number of electrons available
for conduction of current. Dielectric materials have few electrons available for conduction
of current, whereas metals have an abundance of free electrons. Further discussion on the
behavior of conductors and dielectrics in an electric field will be given in subsequent sections.
5.3  CONVECTION AND CONDUCTION CURRENTS
Electric voltage (or potential difference) and current are two fundamental quantities in
electrical engineering. We considered potential in the last chapter. Before examining how
the electric field behaves in a conductor or dielectric, it is appropriate to consider electric
current. Electric current is generally caused by the motion of electric charges.
The current (in amperes) through a given area is the electric charge passing through
the area per unit time.
That is,
I 5 dQ
dt 
(5.1)
Thus in a current of one ampere, charge is being transferred at a rate of one coulomb per
second.
We now introduce the concept of current density J. If current DI flows through a ­planar
surface DS, the current density is
J 5 DI
1 The August 1989 issue of the Proceedings of IEEE was devoted to “Applications of Superconductivity.”
5.3 Convection and Conduction Currents  179
DI 5 JDS
(5.2)
assuming that the current density is perpendicular to the surface. If the current density is
not normal to the surface,
DI 5 J # DS
(5.3)
Thus, the total current flowing through a surface S is
I 5 3
J # dS
(5.4)
Depending on how I is produced, there are different kinds of current density: convection
current density, conduction current density, and displacement current density. We will
consider convection and conduction current densities here; displacement current density
will be considered in Chapter 9. What we need to keep in mind is that eq. (5.4) applies to
any kind of current density. Compared with the general definition of flux in eq. (3.13), eq.
(5.4) shows that the current I through S is merely the flux of the current density J.
CASE A: CONVECTION CURRENT
Convection current, as distinct from conduction current, does not involve conductors and
consequently does not satisfy Ohm’s law. It occurs when current flows through an insulat-
ing medium such as liquid, rarefied gas, or a vacuum. A beam of electrons in a vacuum
tube, for example, is a convection current.
Consider a filament of Figure 5.1. If there is a flow of charge, of density rv, at velocity
u 5 uyay, from eq. (5.1), the current through the filament is
DI 5 DQ
Dt 5 rv DS
Dt 5 rv DS uy
(5.5)
The current density at a given point is the current through a unit normal area at that point.
The y-directed current density Jy is given by
Jy 5 DI
DS 5 rvuy
(5.6)
FIGURE 5.1  Current in a filament.
180  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
Hence, in general
J 5 rvu
(5.7)
The current I is the convection current and J is the convection current density in amperes
per square meter (A/m2).
CASE B: CONDUCTION CURRENT
Conduction current requires a conductor. A conductor is characterized by a large number
of free electrons that provide conduction current due to an impressed electric field. When
an electric field E is applied, the force on an electron with charge 2e is
F 5 2eE
(5.8)
Since the electron is not in free space, it will not experience an average acceleration
under the influence of the electric field. Rather, it suffers constant collisions with
the atomic lattice and drifts from one atom to another. If an electron with mass m is
moving in an electric field E with an average drift velocity u, according to Newton’s
law, the average change in momentum of the free electron must match the applied
force. Thus,
t 5 2eE
(5.9a)
u 5 2et
m E
(5.9b)
where t is the average time interval between collisions. This indicates that the drift velocity
of the electron is directly proportional to the applied field. If there are n electrons per unit
volume, the electronic charge density is given by
rv 5 2ne
(5.10)
Thus the conduction current density is
J 5 rvu 5 ne2t
m  E 5 sE
J 5 sE
(5.11)
where s 5 ne2t/m is the conductivity of the conductor. As mentioned earlier, the values
of  for common materials are provided in Table B.1 in Appendix B. The relationship in
eq. (5.11) is known as the point form of Ohm’s law.
5.4 Conductors  181
CASE A: ISOLATED CONDUCTOR
Consider an isolated conductor, such as shown in Figure 5.2(a). When an external electric
field Ee is applied, the ­positive free charges are pushed along the same direction as the
applied field, while the negative free charges move in the opposite direction. This charge
migration takes place very quickly. The free charges do two things. First, they accumulate
on the surface of the conductor and form an induced surface charge. Second, the induced
charges set up an internal induced field Ei, which cancels the externally applied field Ee. The
result is illustrated in Figure 5.2(b). This leads to an important property of a conductor:
A perfect conductor (  ) cannot contain an electrostatic field within it.
A conductor is called an equipotential body, implying that the potential is the same every­
where in the conductor. This is based on the fact that E 5 2=V 5 0.
Another way of looking at this is to consider Ohm’s law, J 5 sE. To maintain a finite
current density J, in a perfect conductor 1s S  `2, requires that the electric field inside
the conductor s 5 ` vanish. In other words, E S  0 because s S  ` in a perfect con­
ductor. If some charges are introduced in the interior of such a conductor, the charges will
move to the surface and redistribute themselves quickly in such a manner that the field
inside the conductor vanishes. According to Gauss’s law, if E 5 0, the charge density rv
must be zero. We conclude again that a perfect conductor cannot contain an electrostatic
field within it. Under static conditions,
E 5 0,  rv 5 0,  Vab 5 0 inside a conductor
(5.12)
ρv = 0
E = 0
(a)
(b)
FIGURE 5.2  (a) An isolated conductor under the influence of an applied field. (b) A conductor
has zero electric field under static conditions.
5.4  CONDUCTORS
A conductor has an abundance of charge that is free to move. We will consider two cases
involving a conductor.
182  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
where Vab is the potential difference between points a and b in the conductor. This implies
that a conductor is equipotential medium since the electric potential is the same at every point.
CASE B: CONDUCTOR MAINTAINED AT A POTENTIAL
We now consider a conductor whose ends are maintained at a potential difference V, as
shown in Figure 5.3. Note that in this case, E 2 0 inside the conductor, as in Figure 5.2.
What is the difference? There is no static equilibrium in Figure 5.3, since the conductor is
not isolated but is wired to a source of electromotive force, which compels the free charges
to move and prevents the eventual establishment of electrostatic equilibrium. Thus in the
case of Figure 5.3, an electric field must exist inside the conductor to sustain the flow of
current. As the electrons move, they encounter some damping forces called resistance.
Based on Ohm’s law in eq. (5.11), we will derive the resistance of the conducting mate­
rial. Suppose the conductor has a uniform cross ­section of area S and is of length . The
direction of the electric field E produced is the same as the direction of the flow of positive
charges or current I. This direction is opposite to the direction of the flow of electrons. The
E 5 V
(5.13)
Since the conductor has a uniform cross section,
J 5 I
(5.14)
Substituting eqs. (5.11) and (5.13) into eq. (5.14) gives
S 5 sE 5 sV
, 
(5.15)
Hence,
R 5 V
I 5 ,
sS
(5.16)
R 5 rc,
S 
FIGURE 5.3  A conductor of uniform cross
­section under an applied E field.
electric field applied is uniform, and its magnitude is given by
5.4 Conductors  183
where rc 5 1/s is the resistivity of the material. Equation (5.16) is useful in determining the
resistance of any conductor of uniform cross section. If the cross section of the ­conductor
is not uniform, eq. (5.16) is not applicable. However, the basic definition of resistance R as
the ratio of the potential difference V between the two ends of the conductor to the current
I through the conductor still applies. Therefore, applying eqs. (4.60) and (5.4) gives the
­resistance of a conductor of nonuniform cross section; that is,
R 5 V
I 5 eL E # dl
eS sE # dS
(5.17)
Note that the negative sign before V 5 2eE # dl is dropped in eq. (5.17) because
eE # dl , 0 if I . 0. Equation (5.17) will not be utilized until we get to Section 6.5.
Power P (in watts) is defined as the rate of change of energy W (in joules) or force
times velocity. Hence,
P 5 3
rv dv E # u 5 3
E # rvu dv
P 5 3
E # J dv
(5.18)
which is known as Joule’s law. The power density wP (in W/m3) is given by the integrand
in eq. (5.18); that is,
wP 5 dP
dv 5 E # J 5 s 0 E 0 2
(5.19)
For a conductor with uniform cross section, dv 5 dS dl, so eq. (5.18) becomes
P 5 3
E dl 3
J dS 5 VI
P 5 I2R
(5.20)
which is the more common form of Joule’s law in electric circuit theory.
If J 5 1
r3 12 cos u ar 1 sin u au2 A/m2, calculate the current passing through
(a)	 A hemispherical shell of radius 20 cm, 0 , u , p/2, 0 , f , 2p
(b)	 A spherical shell of radius 10 cm
Solution:
EXAMPLE 5.1
I 5 eS
J # dS,
where dS 5 r 2 sin u df du ar in this case.
184  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
(a)	 I 5 3
p/2
u50
f50
r3 2 cos u r2 sin u df du`
r50.2
5 2
r 2p 3
p/2
u50
sin u d1sin u2 `
r50.2
5 4p
0.2 sin2 u
p/2
5 10p 5 31.4 A
(b)	 The only difference here is that we have 0 # u # p instead of 0 # u # p/2 and
r 5 0.1 m. Hence,
I 5 4p
0.1 sin2 u
5 0
Alternatively, for this case
since = # J 5 0. We can show this:
= # J 5 1
r2 '
c 2
r cos ud 1
r sin u '
c 1
r3 sin2 ud 5 22
r4  cos u 1 2
r4 cos u 5 0
PRACTICE EXERCISE  5.1
For the current density J  10z sin2 f ar A/m2, find the current through the cylindrical
surface r  2, 1  z  5 m.
Answer:  754 A.
A typical example of convective charge transport is found in the Van de Graaff genera­
tor, where charge is transported on a moving belt from the base to the dome as shown in
Figure 5.4. If a surface charge density 1027 C/m2 is transported by the belt at a velocity of
2 m/s, calculate the charge collected in 5 s. Take the width of the belt as 10 cm.
Solution:
If rS 5 surface charge density, u 5 speed of the belt, and w 5 width of the belt, the
­current on the dome is
I 5 rSuw
The total charge collected in t 5 5 s is
Q 5 It 5 rSuwt 5 1027 3 2 3 0.1 3 5
5 100 nC
EXAMPLE 5.2
I 5 AS J # dS 5 ev= # J dv 5 0
5.4 Conductors  185
PRACTICE EXERCISE  5.2
In a Van de Graaff generator, w  0.1 m, u  10 m/s, and from the dome to the
ground there are leakage paths having a total resistance of 1014 . If the belt car-
ries charge 0.5 mC/m2, find the potential difference between the dome and the base.
Note: In the steady state, the current through the leakage path is equal to the charge
transported per unit time by the belt.
Answer:  50 mV.
A wire of diameter 1 mm and conductivity 5 3 107 S/m has 1029 free electrons per cubic
meter when an electric field of 10 mV/m is applied. Determine
(a)	 The charge density of free electrons
(b)	 The current density
(c)	 The current in the wire
(d)	 The drift velocity of the electrons (take the electronic charge as e 5 21.6 3 10219 C)
Solution:
(In this particular problem, convection and conduction currents are the same.)
(a)	 rv 5 ne 5 110292 121.6 3 102192 5 21.6 3 1010 C/m3
(b)	 J 5 sE 5 15 3 1072 110 3 10232 5 500 kA/m2
(c)	 I 5 JS 5 15 3 1052 apd2
4 b 5 5p
4 3 1026 3 105 5 0.393 A
(d)	 Since J 5 rvu, u 5 J
5 3 105
1.6 3 1010 5 3.125 3 1025 m/s
EXAMPLE 5.3
FIGURE 5.4  Van de Graaff generator; for
Example 5.2.
186  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
PRACTICE EXERCISE  5.3
The free charge density in copper is 1.81  1010 C/m3. For a current density of 8  106
A/m2, find the electric field intensity and the drift velocity. Hint: Refer to Table B.1 in
Appendix B.
Answer:  0.138 V/m, 4.42  104 m/s.
A lead 1s 5 5 3 106 S/m2 bar of square cross section has a hole bored along its length of
4 m so that its cross section becomes that of Figure 5.5. Find the resistance between the
square ends.
EXAMPLE 5.4
Solution:
Since the cross section of the bar is uniform, we may apply eq. (5.16); that is,
R 5 ,
where S 5 d2 2 pr2 5 32 2 pa1
5 a9 2 p
4  b cm2.
Hence,
R 5
5 3 10619 2 p/42 3 1024 5 974 mV
PRACTICE EXERCISE  5.4
If the hole in the lead bar of Example 5.4 is completely filled with copper
(  5.8  107 S/m), determine the resistance of the composite bar.
Answer:  461.7 m.
FIGURE 5.5  Cross section of the lead bar of Example 5.4.
5.5 Polarization in Dielectrics  187
In Section 5.2, we noticed that the main difference between a conductor and a dielectric
lies in the availability of free electrons in the outermost atomic shells to conduct current.
Although the charges in a dielectric are not able to move about freely, they are bound by
­finite forces, and we may certainly expect a displacement when an external force is applied.
To understand the macroscopic effect of an electric field on a dielectric, consider an
atom of the dielectric as consisting of a negative charge 2Q (electron cloud) and a positive
charge 1Q (nucleus) as in Figure 5.6(a). A similar picture can be adopted for a dielectric
molecule; we can treat the nuclei in molecules as point charges and the electronic structure
as a single cloud of negative charge. Since we have equal amounts of positive and nega-
tive charge, the whole atom or molecule is electrically neutral. When an electric field E
is applied, the positive charge is displaced from its equilibrium position in the direction
of E by the force F1 5 QE, while the negative charge is displaced in the opposite direc-
tion by the force F2 5 QE. A dipole results from the displacement of the charges, and the
dielectric is said to be polarized. In the polarized state, the electron cloud is distorted by the
applied electric field E. This distorted charge distribution is equivalent, by the principle of
superposition, to the original distribution plus a dipole whose moment is
p 5 Qd
(5.21)
where d is the distance vector from 2Q to 1Q of the dipole as in Figure 5.6(b). If there are
N dipoles in a volume Dv of the dielectric, the total dipole moment due to the electric field is
Q1d1 1 Q2d2 1 . . . 1 QNdN 5 a
k51
Qkdk
(5.22)
As a measure of intensity of the polarization, we define polarization P (in coulombs per
meter squared) as the dipole moment per unit volume of the dielectric; that is,
P 5
lim
DvS0
k51
Qkdk
(5.23)
Thus we conclude that the major effect of the electric field E on a dielectric is the cre-
ation of dipole moments that align themselves in the direction of E. This type of dielectric
5.5  POLARIZATION IN DIELECTRICS
FIGURE 5.6  Polarization of a nonpolar atom or molecule.
188  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
is said to be nonpolar. Examples of such dielectrics are hydrogen, oxygen, nitrogen, and the
rare gases. Nonpolar dielectric molecules do not possess dipoles until the application of
the electric field as we have noticed. Other types of molecule such as water, sulfur dioxide,
hydrochloric acid, and polystyrene have built-in permanent dipoles that are randomly ori-
ented as shown in Figure 5.7(a) and are said to be polar. When an electric field E is applied
to a polar molecule, the permanent dipole experiences a torque tending to align its dipole
moment parallel with E as in Figure 5.7(b).
Let us now calculate the field due to a polarized dielectric. Consider the dielectric material
shown in Figure 5.8 as consisting of dipoles with dipole moment P per unit volume. According
to eq. (4.80), the potential dV at an exterior point O due to the dipole moment P dv is
dV 5 P # aR dvr
4peoR2 
(5.24)
where R2 5 1x 2 xr2 2 1 1 y 2 yr2 2 1 1z 2 zr2 2 and R is the distance between the volume
element dv at 1xr, yr, zr2 and the field point O (x, y, z). We can transform eq. (5.24) into
a form that facilitates physical interpretation. It is readily shown (see Section 7.7) that the
gradient of 1/R with respect to the primed coordinates is
=r a 1
Rb 5 aR
where =r is the del operator with respect to 1xr, yr, zr2. Thus,
P # aR
5 P # =ra 1
FIGURE 5.7  Polarization of a polar molecule:
(a) permanent dipole (E 5 0), (b) alignment
of permanent dipole (E  0).
FIGURE 5.8  A block of dielectric material
with dipole moment P per unit volume.
5.5 Polarization in Dielectrics  189
Applying the vector identity =r # f A 5 f=r # A 1 A # =rf ,
P # aR
5 =r # aP
Rb 2 =r # P
(5.25)
Substituting this into eq. (5.24) and integrating over the entire volume v of the dielectric,
we obtain
V 5 3
4peo
c=r # P
R 2 1
R=r # Pd dvr
Applying divergence theorem to the first term leads finally to
V 5 C
P # arn
4peoR dSr 1 3
2=r # P
4peoR  dvr
(5.26)
where arn is the outward unit normal to surface S of the dielectric. Comparing the two
terms on the right side of eq. (5.26) with eqs. (4.68) and (4.69) shows that the two terms
denote the potential due to surface and volume charge distributions with densities (upon
dropping the primes):
rps 5 P # an
rpv 5 2= # P
15.27a2
15.27b2
In other words, eq. (5.26) reveals that where polarization occurs, an equivalent volume
charge density rpv is formed throughout the dielectric, while an equivalent surface charge
density rps is formed over the surface of the dielectric. We refer to rps and rpv as bound
(or polarization) surface and volume charge densities, respectively, as distinct from free
surface and volume charge densities rS and rv. Bound charges are those that are not free to
move within the dielectric material; they are caused by the displacement that occurs on a
molecular scale during polarization. Free charges are those that are capable of moving over
macroscopic distance, as do electrons in a conductor; they are the stuff we control. The
total positive bound charge on surface S bounding the dielectric is
Qb 5 C P # dS 5 C rps dS
(5.28a)
while the charge that remains inside S is
2Qb 5 3
rpv dv 5 23
= # P dv
(5.28b)
If the entire dielectric were electrically neutral prior to application of the electric field and
if we have not added any free charge, the dielectric will remain electrically neutral. Thus
the total charge of the dielectric material remains zero, that is,
190  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
total charge 5 C
rps dS 1 3
rpv dv 5 Qb 2 Qb 5 0
We now consider the case in which the dielectric region contains free charge. If rv is the
volume density of free charge, the total volume charge density rt is given by
rt 5 rv 1 rpv 5 = # eoE
(5.29)
Hence,
rv 5 = # eoE 2 rpv
5 = # 1eoE 1 P2
(5.30)
5 = # D
where
D 5 eoE 1 P
(5.31)
We conclude that the net effect of the dielectric on the electric field E is to increase D
inside it by the amount P. In other words, the application of E to the dielectric material
causes the flux density to be greater than it would be in free space. It should be noted that
the definition of D in eq. (4.35) for free space is a special case of that in eq. (5.31) because
P 5 0 in free space.
For some dielectrics, P is proportional to the applied electric field E, and we have
P 5 xeeoE
(5.32)
where xe, known as the electric susceptibility of the material, is more or less a measure of
how susceptible (or sensitive) a given dielectric is to electric fields.
5.6  DIELECTRIC CONSTANT AND STRENGTH
By substituting eq. (5.32) into eq. (5.31), we obtain
D 5 eo11 1 xe2 E 5 eoerE
(5.33)
D 5 eE
(5.34)
where
e 5 eoer
(5.35)
5.7 Linear, Isotropic, and Homogeneous Dielectrics  191
and
er 5 1 1 xe 5 e
(5.36)
In eqs. (5.33) to (5.36),  is called the permittivity of the dielectric, o is the permittiv­
ity of free space, defined in eq. (4.2) as approximately 1029/36p F/m, and r is called the
dielectric constant or relatve permittivity.
The dielectric constant (or relative permittivity) r is the ratio of the permittivity of
the dielectric to that of free space.
per meter. The approximate values of the dielectric constants of some common materials
are given in Table B.2 in Appendix B. The values given in Table B.2 are for static or low-
frequency 1,1000 Hz2 fields; the values may change at high frequencies. Note from the
table that r is always greater than or equal to unity. For free space er 5 1.
The theory of dielectrics we have discussed so far assumes ideal dielectrics. Practically
speaking, no dielectric is ideal. When the electric field in a dielectric is sufficiently large,
it begins to pull electrons completely out of the molecules, and the dielectric becomes
conducting. Dielectric breakdown is said to have occurred when a dielectric becomes con­
ducting. Dielectric breakdown occurs in all kinds of dielectric materials (gases, liquids, or
solids) and depends on the nature of the material, temperature, humidity, and the amount
of time that the field is applied. The minimum value of the electric field at which dielectric
breakdown occurs is called the dielectric strength of the dielectric material.
The dielectric strength is the maximum electric field that a dielectric can tolerate or
withstand without electrical breakdown.
Table B.2 also lists the dielectric strength of some common dielectrics. Since our theory
of dielectrics does not apply after dielectric breakdown has taken place, we shall always
assume ideal dielectric and avoid dielectric breakdown.
†5.7  LINEAR, ISOTROPIC, AND HOMOGENEOUS DIELECTRICS
A material is said to be linear if D varies linearly with E and nonlinear otherwise. Materials
for which  (or ) does not vary in the region being considered and is therefore the same
at all points (i.e., independent of x, y, z) are said to be homogeneous. They are said to be
­inhomogeneous (or nonhomogeneous) when  is dependent on the space coordinates. The
atmosphere is a typical example of an inhomogeneous medium; its permittivity varies with
altitude. Materials for which D and E are in the same direction are said to be isotropic. That is,
It should also be noticed that  and x  are dimensionless, whereas  and  are in farads
is, isotropic dielectrics are those that have the same properties in all directions. In anisotropic
192  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
(or nonisotropic) materials, D, E, and P are not parallel;  or xe has nine ­components that are
collectively referred to as a tensor. For example, instead of eq. (5.34), we have
§ 5 £
exx
exy
exz
eyz
eyy
eyz
ezx
ezy
ezz
§ £
§ 
(5.37)
for anisotropic materials. Crystalline materials and magnetized plasma are anisotropic.
A dielectric material (in which D  E applies) is linear if  does not change with the
applied E field, homogeneous if  does not change from point to point, and isotropic
if  does not change with direction. Although eqs. (5.24) to (5.31) are for ­dielectric
materials in general, eqs. (5.32) to (5.34) are only for linear, isotropic ­materials.
The same idea holds for a conducting material in which J 5 sE applies. The material is
linear if  does not vary with E, homogeneous if  is the same at all points, and isotropic
if  does not vary with direction.
For most of the time, we will be concerned only with linear, isotropic, and homoge­
neous media. Such media are called simple materials. For such media, all formulas derived
in Chapter 4 for free space can be applied by merely replacing o with or. Thus Coulomb’s
law of eq. (4.4), for example, becomes
F 5
Q1Q2
4peoerR2 aR
(5.38)
and eq. (4.96) becomes
W 5 1
eoerE2 dv
(5.39)
when applied to a dielectric medium.
A dielectric cube of side L and center at the origin has a radial polarization given by
P 5 a r, where a is a constant and r 5 xax 1 yay 1 zaz. Find all bound charge densities
and show explicitly that the total bound charge vanishes.
Solution:
For each of the six faces of the cube, there is a surface charge density rps. For the face located
at x 5 L/2, for example,
rps 5 P # ax`
x5L/2
5 ax`
x5L/2
5 aL
The total bound surface charge is
EXAMPLE 5.5
5.7 Linear, Isotropic, and Homogeneous Dielectrics  193
Qs 5 3
rps dS 5 6 3
L/2
2L/2
L/2
2L/2
rps dy dz 5 6aL
2  L
5 3aL3
The bound volume charge density is given by
rpv 5 2= # P 5 21a 1 a 1 a2 5 23a
and the total bound volume charge is
Hence, the total charge is
Qt 5 Qs 1 Qv 5 3aL3 2 3aL3 5 0
PRACTICE EXERCISE  5.5
A thin rod of cross-sectional area A extends along the x-axis from x  0 to x  L. The
polarization of the rod is along its length and is given by Px  ax2  b. Calculate rpv and
rps at each end. Show explicitly that the total bound charge vanishes in this case.
Answer:  0, 2aL, b, aL2  b, proof.
The electric field intensity in polystyrene (er 5 2.55) filling the space between the
plates of a parallel-plate capacitor is 10 kV/m. The distance between the plates is 1.5 mm.
Calculate:
(a)	 D
(b)	 P
(c)	 The surface charge density of free charge on the plates
(d)	 The surface density of polarization charge
(e)	 The potential difference between the plates
Solution:
(a)	 D 5 eoerE 5 1029
36p 3 12.552 3 104 5 225.4 nC/m2
(b)	 P 5 xeeoE 5 11.552 3 1029
36p 3 104 5 137 nC/m2
(c)	 rS 5 D # an 5 6 Dn 5 6 225.4 nC/m2
(d)	 rps 5 P # an 5 6 Pn 5 6 137 nC/m2
(e)	 V 5 Ed 5 10411.5 3 10232 5 15 V
EXAMPLE 5.6
Qv 5 3
v rpv dv 5 23a 3
v dv 5 23aL3
194  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
PRACTICE EXERCISE  5.6
A parallel-plate capacitor with plate separation of 2 mm has a 1 kV voltage applied to
its plates. If the space between its plates is filled with polystyrene (r  2.55), find E, P,
and rps. Assume that the plates are located at x  0 and x  2 mm.
Answer:  500ax kV/m, 6.853ax mC/m2, 6.853 mC/m2.
A dielectric sphere 1er 5 5.72 of radius 10 cm has a point charge of 2 pC placed at its
­center. Calculate:
(a)	 The surface density of polarization charge on the surface of the sphere
(b)	 The force exerted by the charge on a24 pC point charge placed on the sphere
Solution:
(a)  Assuming that the point charge is located at the origin, we apply Coulomb’s or Gauss’s
law to obtain
E 5
4peoerr2 ar
P 5 xeeoE 5
xeQ
4perr2 ar
rps 5 P # ar 5
1er 2 12Q
4perr2
14.72 2 3 10212
4p15.72 100 3 1024
5 13.12 pC/m2
(b)	 From Coulomb’s law, we have
F 5
Q1Q2
4peoerr2 ar 5
1242 122 3 10224
4p 3 1029
36p 15.72 100 3 1024
5 21.263ar pN
PRACTICE EXERCISE  5.7
In a dielectric material, Ex 5 5 V/m and P 5
10p 13ax 2 ay 1 4az2 nC/m2.
Calculate:
(a)  xe
(b)  E
(c)  D
Answer:  (a) 2.16, (b) 5ax 2 1.67ay 1 6.67az V/m, (c) 139.7ax 2 46.6ay 1
186.3az pC/m2.
EXAMPLE 5.7
5.7 Linear, Isotropic, and Homogeneous Dielectrics  195
Find the force with which the plates of a parallel-plate capacitor attract each other. Also
determine the pressure on the surface of the plate due to the field.
Solution:
From eq. (4.26), the electric field intensity on the surface of each plate is
E 5 rS
2e an
where an is a unit normal to the plate and rS is the surface charge density. The total force
on each plate is
F 5 QE 5 rSS # rS
2e an 5 rS
2 S
2eoer
F 5 rS
2 S
2e 5 Q2
2eS
The pressure of force per area is r2
2eoer
. Notice that the dielectric affects the force or ­pressure.
PRACTICE EXERCISE  5.8
Shown in Figure 5.9 is a potential-measuring device known as an electrometer. It is basi-
cally a parallel-plate capacitor with the guarded plate being suspended from a balance
arm so that the force F on it is measurable in terms of weight. If S is the area of each
plate, show that
V1 2 V2 5 c 2 Fd2
eoS d
1/2
Answer:  Proof.
EXAMPLE 5.8
FIGURE 5.9  An electrometer; for Practice
Exercise 5.8.
196  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
5.8  CONTINUITY EQUATION AND RELAXATION TIME
From the principle of charge conservation, the time rate of decrease of charge within a
given volume must be equal to the net outward current flow through the surface of the
­volume. Thus current Iout coming out of the closed surface is
Iout 5 C J # dS 5 2dQin
(5.40)
where Qin is the total charge enclosed by the closed surface. Invoking the divergence
­theorem, we write
J # dS 5 3
= # J dv
(5.41)
But
2dQin
5 2 d
dt 3
rv dv 5 23
'rv
't  dv
(5.42)
Substituting eqs. (5.41) and (5.42) into eq. (5.40) gives
= # J dv 5 23
'rv
't  dv
= # J 5 2'rv
't 
(5.43)
which is called the continuity of current equation or just continuity equation. It must be
kept in mind that the continuity equation is derived from the principle of conservation
of charge and essentially states that there can be no accumulation of charge at any point.
For steady currents, 'rv/'t 5 0, and hence = # J 5 0, showing that the total charge leav­
ing a volume is the same as the total charge entering it. Kirchhoff’s current law follows
from this.
Having discussed the continuity equation and the properties  and  of materials,
it is appropriate to consider the effect of introducing charge at some interior point of a
given material (conductor or dielectric). We make use of eq. (5.43) in conjunction with
Ohm’s law
J 5 s E
(5.44)
and Gauss’s law
5.8 Continuity Equation and Relaxation Time  197
= # E 5 rv
e 
(5.45)
Substituting eqs. (5.44) and (5.45) into eq. (5.43) yields
= # sE 5 srv
5 2'rv
'rv
't 1 s
erv 5 0
(5.46)
This is a homogeneous linear ordinary differential equation. By separating variables in
eq. (5.46), we get
'rv
5 2s
e't
(5.47)
and integrating both sides gives
ln rv 5 2st
e 1 ln rvo
where ln rvo is a constant of integration. Thus
rv 5 rvoe2t/Tr
(5.48)
where
Tr 5 e
(5.49)
and Tr is the time constant in seconds.
In eq. (5.48), rvo is the initial charge density (i.e., rv at t 5 0). The equation shows
that the introduction of charge at some interior point of the material results in a decay of
volume charge density rv. Associated with the decay is charge movement from the interior
point at which it was introduced to the surface of the material. The time constant Tr is
known as the relaxation time or rearrangement time.
Relaxation time is the time it takes a charge placed in the interior of a material to
drop to e1 ( 36.8%) of its initial value.
Relaxation time is short for good conductors and long for good dielectrics. For example,
for copper s 5 5.8 3 107 S/m, er 5 1, and
198  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
Tr 5 ereo
s 5 1 3 1029
36p 3
5.8 3 107
5 1.53 3 10219 s
(5.50)
showing a rapid decay of charge placed inside copper. This implies that for good conduc­
tors, the relaxation time is so short that most of the charge will vanish from any interior
point and appear at the surface (as surface charge) almost instantaneously. On the other
hand, for fused quartz, for instance, s 5 10217 S/m, er 5 5.0,
Tr 5 5 3 1029
36p 3
10217
5 51.2 days
(5.51)
showing a very large relaxation time. Thus for good dielectrics, one may consider the
­introduced charge to remain wherever placed for times up to days.
5.9  BOUNDARY CONDITIONS
So far, we have considered the existence of the electric field in a homogeneous medium. If
the field exists in a region consisting of two different media, the conditions that the field
must satisfy at the interface separating the media are called boundary conditions. These
conditions are helpful in determining the field on one side of the boundary if the field on
the other side is known. Obviously, the conditions will be dictated by the types of material
the media are made of. We shall consider the boundary conditions at an interface separating
•	 Dielectric 1er12 and dielectric 1er22
Conductor and dielectric
•	 Conductor and free space
To determine the boundary conditions, we need to use Maxwell’s equations:
(5.52)
and
D # dS 5 Qenc
(5.53)
where Qenc is the free charge enclosed by the surface S. Also we need to decompose the
electric field intensity E into two orthogonal components:
E 5 Et 1 En
(5.54)
where Et and En are, respectively, the tangential and normal components of E to the
­interface of interest. A similar decomposition can be done for the electric flux density D.
E # dl 5 0
5.9 Boundary Conditions  199
A.  Dielectric–Dielectric Boundary Conditions
Consider the E field existing in a region that consists of two different dielectrics character­
ized by e1 5 eoer1 and e2 5 eoer2 as shown in Figure 5.10(a). The fields E1 and E2 in media
1 and 2, respectively, can be decomposed as
E1 5 E1t 1 E1n
(5.55a)
E2 5 E2t 1 E2n 
(5.55b)
We apply eq. (5.52) to the closed path abcda of Figure 5.10(a), assuming that the path is
very small with respect to the spatial variation of E. We obtain
0 5 E1t Dw 2 E1n
2 2 E2n
2 2 E2t Dw 1 E2n
2 1 E1n
2 
(5.56)
where Et 5 0 Et 0  and En 5 0 En 0 . The Dh
2  terms cancel, and eq. (5.56) becomes
0 5 1E1t 2 E2t2Dw
E1t 5 E2t
(5.57)
Thus the tangential components of E are the same on the two sides of the boundary. In
other words, Et undergoes no change on the boundary and it is said to be continuous across
the boundary. Since D 5 eE 5 Dt 1 Dn, eq. (5.57) can be written as
D1t
5 E1t 5 E2t 5 D2t
D1t
5 D2t
(5.58)
FIGURE 5.10  Dielectric–dielectric boundary: (a) determining E1t 5 E2t, (b) determining D1n 5 D2n.
200  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
that is, Dt undergoes some change across the interface. Hence Dt is said to be discontinuous
across the interface.
Similarly, we apply eq. (5.53) to the pillbox (cylindrical Gaussian surface) of
­Figure 5.10(b). The contribution due to the sides vanishes. Allowing Dh S  0 gives
DQ 5 rS DS 5 D1n DS 2 D2n DS
D1n 2 D2n 5 rS
(5.59)
where rS is the free charge density placed deliberately at the boundary. It should be borne in
mind that eq. (5.59) is based on the assumption that D is directed from region 2 to region
1 and eq. (5.59) must be applied accordingly. If no free charges exist at the interface (i.e.,
charges are not deliberately placed there), rS 5 0 and eq. (5.59) becomes
D1n 5 D2n
(5.60)
Thus the normal component of D is continuous across the interface; that is, Dn undergoes
no change at the boundary. Since D 5 eE, eq. (5.60) can be written as
e1E1n 5 e2E2n
(5.61)
showing that the normal component of E is discontinuous at the boundary. Equations
(5.57) and (5.59) or (5.60) are collectively referred to as boundary conditions; they must be
satisfied by an electric field at the boundary separating two different dielectrics.
As mentioned earlier, the boundary conditions are usually applied in finding the elec-
tric field on one side of the boundary given the field on the other side. Besides this, we can
use the boundary conditions to determine the “refraction” of the electric field across the
interface. Consider D1 or E1 and D2 or E2 making angles 1 and 2 with the normal to the
interface as illustrated in Figure 5.11. Using eq. (5.57), we have
E1 sin u1 5 E1t 5 E2t 5 E2 sin u2
FIGURE 5.11  Refraction of D or E
at a dielectric–dielectric boundary.
5.9 Boundary Conditions  201
E1 sin u1 5 E2 sin u2
(5.62)
Similarly, by applying eq. (5.60) or (5.61), we get
e1E1 cos u1 5 D1n 5 D2n 5 e2E2 cos u2
e1E1 cos u1 5 e2E2 cos u2
(5.63)
Dividing eq. (5.62) by eq. (5.63) gives
tan u1
5 tan u2
(5.64)
Since e1 5 eoer1 and e2 5 eoer2, eq. (5.64) becomes
tan u1
tan u2
5 er1
er2
(5.65)
This is the law of refraction of the electric field at a boundary free of charge (since rS 5 0 is
assumed at the interface). Thus, in general, an interface between two dielectrics produces
bending of the flux lines as a result of unequal polarization charges that accumulate on the
opposite sides of the interface.
B.  Conductor–Dielectric Boundary Conditions
Figure 5.12 shows the case of conductor–dielectric boundary conditions. The conductor is
assumed to be perfect (i.e., s S  ` or rc S  0). Although such a conductor is not realiz­
able for most practical purposes, we may regard conductors such as copper and silver as
though they were perfect conductors.
FIGURE 5.12  Conductor–dielectric boundary.
202  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
To determine the boundary conditions for a conductor–dielectric interface, we follow
the same procedure used for the dielectric–dielectric interface except that we incorporate
the fact that E 5 0 inside the conductor. Applying eq. (5.52) to the closed path abcda of
Figure 5.12(a) gives
0 5 0 # Dw 1 0 # Dh
2 1 En # Dh
2 2 Et # Dw 2 En # Dh
2 2 0 # Dh
2 
(5.66)
As Dh S  0,
Et 5 0
(5.67)
Similarly, by applying eq. (5.53) to the cylindrical pillbox of Figure 5.12(b) and letting
Dh S  0, we get
DQ 5 Dn # DS 2 0 # DS
(5.68)
because D 5 eE 5 0 inside the conductor. Equation (5.68) may be written as
Dn 5 DQ
DS 5 rS
Dn 5 rS
(5.69)
Thus under static conditions, the following conclusions can be made about a perfect
conductor:
1.	 No electric field may exist within a conductor; that is, considering our conclusion
in Sectio
rv 5 0,  E 5 0
(5.70)
2.	 Since E 5 2=V 5 0, there can be no potential difference between any two points
in the conductor; that is, a conductor is an equipotential body.
3.	 An electric field E must be external to the conductor and must be normal to its
surface; that is,
Dt 5 eoerEt 5 0,  Dn 5 eoerEn 5 rS
(5.71)
An important application of the fact that E 5 0 inside a conductor is in electrostatic screen­
ing or shielding. If conductor A kept at zero potential surrounds conductor B as shown in
Figure 5.13, B is said to be electrically screened by A from other electric circuits, such as
conductor C, outside A. Similarly, conductor C outside A is screened by A from B. Thus
n 5.4,
5.9 Boundary Conditions  203
conductor A acts like a screen or shield, and the electrical conditions inside and outside the
screen are completely independent of each other.
C.  Conductor–Free Space Boundary Conditions
The conductor–free space boundary conditions, illustrated in Figure 5.14, comprise a
special case of conductor–dielectric conditions. The boundary conditions at the interface
between a conductor and free space can be obtained from eq. (5.71) by replacing r by 1
(because free space may be regarded as a special dielectric for which er 5 1). The electric
field E must be external to the conductor and normal to its surface. Thus the boundary
conditions are
Dt 5 eoEt 5 0,  Dn 5 eoEn 5 rS
(5.72)
It should be noted again that eq. (5.72) implies that the E field must approach the conducting
­surface normally.
FIGURE 5.13  Electrostatic screening.
FIGURE 5.14  Conductor–free space boundary.
Conductor (E = 0)
204  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
Two extensive homogeneous isotropic dielectrics meet on plane z 5 0. For z . 0, er1 5 4
and for z , 0, er2 5 3. A uniform electric field E1 5 5ax 2 2ay 1 3az kV/m exists for
z $ 0. Find
(a)	 E2 for z # 0
(b)	 The angles E1 and E2 make with the interface
(c)	 The energy densities (in J/m3) in both dielectrics
(d)	 The energy within a cube of side 2 m centered at 13, 4, 252
Solution:
Let the problem be as illustrated in Figure 5.15.
(a)	 Since az is normal to the boundary plane, we obtain the normal components as
E1n 5 E1 # an 5 E1 # az 5 3
E1n 5 3az
E2n 5 1E2 # az2 az
Also
E 5 En 1 Et
Hence,
E1t 5 E1 2 E1n 5 5ax 2 2ay
Thus
E2t 5 E1t 5 5ax 2 2ay
EXAMPLE 5.9
FIGURE 5.15  For Example 5.9.
5.9 Boundary Conditions  205
Similarly,
D2n 5 D1n  S   er2 E2n 5 er1 E1n
E2n 5 er1
er2
E1n 5 4
3 13az2 5 4az
Thus
E2 5 E2t 1 E2n
5 5ax 2 2ay 1 4az kV/m
(b)  Let a1 and a2 be the angles E1 and E2 they make with the interface while 1 and 2 are
the angles they make with the normal to the interface as shown in Figure 5.15; that is,
a1 5 90 2 u1
a2 5 90 2 u2
Since E1n 5 3 and E1t 5 "25 1 4 5 "29
tan u1 5 E1t
E1n
5 "29
5 1.795 S  u1 5 60.9°
Hence,
a1 5 29.1°
Alternatively,
E1 # an 5 0 E1 0 # 1 # cos u1
cos u1 5
"38
5 0.4867 S  u1 5 60.9°
Similarly,
E2n 5 4,  E2t 5 E1t 5 "29
tan u2 5 E2t
E2n
5 "29
5 1.346 S  u2 5 53.4°
Hence,
a2 5 36.6°
206  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
Note that  tan u1
tan u2
5 er1
er2
is satisfied.
(c)	 The energy densities are given by
wE1 5 1
2 e1 0 E1 0 2 5 1
2 3 4 3 1029
36p 3 125 1 4 1 92 3 106
5 672 mJ/m3
wE2 5 1
2 e2 0 E2 0 2 5 1
2 3 3 3 1029
36p 125 1 4 1 162 3 106
5 597 mJ/m3
(d)  At the center 13, 4, 252 of the cube of side 2 m, z 5 25 , 0; that is, the cube is in
­region 2 with 2 # x # 4, 3 # y # 5, 26 # z # 24. Hence
WE 5 3 wE2 dv 5 3
x52
y53
z526
wE2 dz dy dz 5 wE2122 122 122
5 597 3 8 mJ 5 4.776 mJ
PRACTICE EXERCISE  5.9
A homogeneous dielectric 1er 5 2.52 fills region 1 1x , 02 while region 2 1x . 02 is
free space.
(a)  If D1 5 12 ax 2 10 ay 1 4 az nC/m2, find D2 and 2.
(b)  If E2 5 12 V/m and u2 5 60°, find E1 and 1. Take 1 and 2 as defined in ­
Example 5.9.
Answer:  (a) 12 ax 2 4 ay 1 1.6 az nC/m2, 19.75°,  (b) 10.67 V/m, 77°.
Region y , 0 consists of a perfect conductor while region y . 0 is a dielectric medium
1e1r 5 22 as in Figure 5.16. If there is a surface charge of 2 nC/m2 on the conductor, deter­
mine E and D at
(a)	 A13, 22, 22
(b)	 B124, 1, 52
Solution:
(a)	 Point A13, 22, 22 is in the conductor since y 5 22 , 0 at A. Hence,
E 5 0 5 D
(b)	 Point B124, 1, 52 is in the dielectric medium since y 5 1 . 0 at B.
Dn 5 rS 5 2 nC/m2
EXAMPLE 5.10
5.10 Application Note—Materials with High Dielectric Constant  207
Hence,
D 5 2ay nC/m2
and
E 5 D
eoer
5 2 3 1029 3 36p
3 109ay 5 36p ay
5 113.1ay V/m
PRACTICE EXERCISE  5.10
It is found that E 5 60ax 1 20ay 2 30az mV/m at a particular point on the interface
between air and a conducting surface. Find D and rS at that point.
Answer:  0.531ax 1 0.177ay 2 0.265az pC/m2, 0.619 pC/m2.
FIGURE 5.16  For Example 5.10.
†5.10  APPLICATION NOTE—MATERIALS WITH HIGH
DIELECTRIC CONSTANT
This section is included in recognition of the growing importance of high dielectric
constant materials to the semiconductor industry. As we noticed earlier in this chapter,
the dielectric constant of a material is a property that determines its ability to become
electrically ­polarized. The higher the dielectric constant, the more charge you can store,
208  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
and the smaller you can make electronic circuits. High dielectric constant materials are
increasingly ­important for pushing the state of the art in semiconductor integrated circuits.
These materials, which find ­numerous technological applications, are necessary when high
capacitance values are required. For example, to reduce the size of a dielectric resonator
it is necessary to increase the dielectric constant of the material used. This is because at
a fixed frequency, the diameter of the resonator is inversely proportional to the square root
of the dielectric constant. Unfortunately, the higher the dielectric constant of a material, the
higher its dielectric loss, as will be shown in Chapter 10.
High dielectric constants have been discovered in oxides of the type ACu3Ti4O12. The
most exceptional behavior is exhibited by a perovskite-related oxide containing calcium
(Ca), copper (Cu), titanium (Ti), and oxygen (O) in the formula CaCu3Ti4O12. This material
is unusual in that it has an extremely high dielectric constant—about 11,000 (measured at
100 kHz). In addition, unlike most dielectric materials, this one retains its enormously high
dielectric constant over a wide range of temperatures, from 100 to 600 degrees kelvin (K)
High dielectric constant materials are of great interest for other high-performance
electric devices as well. One technology currently under development uses barium stron­
tium titanate (BST), planned for use in dynamic random access memories (DRAMs).
­Although the dielectric constants are considerable, one disadvantage is the need for plati­
num electrodes. Another example occurs in radio frequency identification (RFID) chips,
which require high capacitance to store charge. Frequently these use separate discrete
devices, which are undesirably high in cost and low in yield.2
5.11  APPLICATION NOTE—GRAPHENE
All solid materials are supposed to have three dimensions. But graphene is a
two-dimensional material made up of a single planar array of carbon atoms densely
packed in a honeycomb or chicken-wire fashion, as shown in Figure 5.17. It has the small­
est thickness and yet is one of the strongest of solids. Both the electrical conductivity and
transparent, yet so dense that even the smallest atom, helium, cannot pass through it.
Graphene has drawn enormous curiosity on account of its unusual properties, which have
many potential applications.
Every pencil lead has graphite, and a line drawn by a pencil is a primitive form of
­graphene. Around 1947 Philip Wallace first studied the theoretical aspects of graphite as
its thickness was reduced. The name graphene was first coined in 1987 by S. Mouras and
coworkers to describe the graphite layers that had various compounds inserted between
them. In a sense, carbon nanotubes are rolled-up graphene sheets.
Originally, graphene was thought to be unstable in its free form; but in 2003, Andre
Geim and Kostya Novoselov at the University of Manchester succeeded in producing the
2 For more information about high dielectric constant materials, see H. S. Nalwa, Handbook of Low and High
Dielectric Constant Materials and Their Applications. San Diego, CA: Academic Press, 1999, vols. 1 and 2.
(or 173 to 327°C), making it ideal for a wide range of applications.
the thermal conductivity of graphene are very, very high. Graphene is almost completely
5.11 Application Note—Graphene  209
first isolated graphene flakes, and their work was published in 2004. Their groundbreak­
ing experiments, for which they received the 2010 Nobel Prize for Physics, showed how
isolated graphene can be put to use in real-life applications. After the 2004 publication by
Geim and Novoselov, other researchers began studying the properties of graphene. The
Manchester group further showed that graphene at room temperature exhibits the quan­
tum Hall effect, which had not been seen in other materials. The carrier mobility of gra­
phene is very high, and this property can be exploited in making fast electronic devices.
its carbon–carbon bond length of about 0.142 nm, graphene can also be considered as an
indefinitely large aromatic molecule, the limiting case of the family of polycyclic aromatic
hydrocarbons.
Electrodes with a very high surface area and very low electrical resistance can be made
from graphene. Adding graphene to epoxy composites may result in stronger/stiffer com­
ponents than can be made from epoxy composites containing a similar weight of carbon
nanotubes. Graphene appears to bond better to the polymers in the epoxy, allowing more
effective coupling of the graphene into the structure of the composite. This property could
result in the manufacture of components with high strength-to-weight ratio for such uses
as windmill blades or aircraft components.
Today, materials used in making solar cells are expensive, and the required manufac­
turing techniques are complicated. But if graphene is used as an electrode, while buckyballs
and carbon nanotubes are employed to absorb light and generate electrons, it is possible
to make solar cells more efficiently and at lower cost. Other potential applications of
graphene include making high-speed electronic transistors, integrated circuits, and low-
cost display screens for mobile devices. Lithography techniques can be used to fabricate
integrated circuits based on graphene. It is also forecast that graphene can replace indium-
device display screens that require low power consumption. The use of graphene instead
FIGURE 5.17  The structure of graphene.
Also, graphene could be used as a chemical sensor to detect molecules of adsorption. With
based electrodes in organic light-emitting diodes (OLEDs), which are used in electronic
210  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
of indium not only reduces the cost but eliminates the use of metals in the OLED, which
may make devices easier to recycle. In yet another application, graphene layers are used to
increase the binding energy of hydrogen to the graphene surface in a fuel tank, resulting in
more hydrogen storage and therefore a lighter weight fuel tank. Such a component could
be useful in the development of practical hydrogen-fueled cars.
†5.12  APPLICATION NOTE—PIEZOELECTRICS
The surfaces of many crystals acquire charge upon deformation. While the total charge in
the material cannot change merely by deformation, charges of opposite sign whose total
is zero appear at different parts of the surface as a result of mechanical stimulus applied
to them. Such materials are called piezoelectrics. Examples include quartz, Rochelle salt,
tourmaline, and many other crystalline materials. Experiments conducted with mechani­
cal inputs in various directions reveal that only in certain fixed directions called polar axes
the surface perpendicular to these polar axes. On the surfaces opposing the polar axes,
charges of opposite polarity are found under uniform strain. Further, it is found that if the
vice versa, the polarities of the induced charges also get reversed. The direction of the force
need not be in the direction of the polar axes, but if the resulting stress has a component
along the polar axes, one finds the accumulation of the charges on the surfaces.
Since different directions along a polar axis are not equivalent, if a crystal is rotated
through 180 around an axis perpendicular to the polar axis, the latter coincides with
itself but the crystal will not. As a result, crystals having a center of symmetry cannot
be piezoelectrics. The necessary condition for the piezoelectric effect to manifest upon
application of uniform deformation is therefore the absence of a center of symmetry in the
given crystal. The symmetry properties of the crystal lattice are determined by the polar
axes. Generally, a crystal has multiple polar axes. The piezoelectric effect was discovered
by Pierre and Jacques Curie in 1880.
Piezoelectric properties depend on temperature. If at a certain temperature the crystal
lattice is rearranged so that a center of symmetry is formed, piezoelectric properties of the
crystal vanish at this temperature. If a material were to exhibit strong electromechanical
coupling, the polarized atoms and molecules must be aligned well. The dipoles are oriented
with respect to one another through a process called poling. Poling is usually brought about
by heating the piezoelectric material up above its Curie temperature and then placing it in
a strong electric field (typically, 2000 V/mm). The combination of heating and electric field
produces motion of the electronic dipoles. Since the material is softer at higher tempera­
tures, heating permits the dipoles to rotate freely. The electric field produces an alignment
of the dipoles along the direction of the electric field. What resembles annealing to some
extent, a quick reduction in the temperature and removal of the electric field produces a
material whose electric dipoles are oriented in the same direction. This direction is referred
to as the poling direction of the material. Ionic crystals are found to possess piezoelectric
properties. There exists some difference in the deformation of sublattice of positive ions
the effect is pronounced to a maximal degree, with charges being induced on the parts of
deformation is reversed, that is, if the deformation is compression instead of expansion, or
compared to that of negative ions causing crystal polarization and consequential surface
charge distribution. To a first approximation, the polarization is directly proportional to
the strain and in turn to the external force. The electric potential difference between the
oppositely charged faces is therefore proportional to the applied force, which is exploited in
and remote event detection.
Just as mechanical force applied to the piezoelectric crystal causes charges and hence
potential to appear across the faces as per the direct piezoelectric effect, application of
external electric field can bring about deformation of the crystal, and this is the inverse
piezoelectric effect. When a piezoelectric body is deformed, work is expended to raise the
energy of elastic deformation and also the energy of the electric field appearing as a result
of the piezoelectric effect. In this event, it is necessary to overcome an additional force
besides the elastic force of the crystal, which impedes the deformation. This is responsible
for the inverse piezoelectric effect. As a compensatory measure, we should apply an exter­
nal electric field opposite to that arising from the direct piezoelectric effect. This establishes
that, to deform the piezoelectric in a given dimension by an external field, this field must
be equal and opposite to the field that would appear under the given deformation due to
the direct piezoelectric effect. If a certain potential difference appears between the faces of a
piezoelectric, which are perpendicular to its polar axis, upon a deformation along this axis,
a potential difference of the same magnitude but of opposite sign must be applied to these
faces to attain the same deformation without applying mechanical forces. The mechanism
of the inverse piezoelectric effect is similar to that of the direct effect: under the action of an
external field, the crystal sublattices of positive and negative ions are deformed differently,
which causes physical deformation of the crystal. The inverse piezoelectric effect also has
numerous practical applications. For instance, quartz ultrasonic vibrators are widely used.
Two of the most popular piezoelectric materials are lead-zirconate-titanate (PZT)
5.12 Application Note—Piezoelectrics  211
numerous transducer applications such as pressure transducers, microphones, automation,
which is a ceramic, and polyvinylidene fluoride (PVDF), which is a polymer. In addition
to the piezoelectric effect, piezoelectric materials exhibit a pyroelectric effect, according to
which electric charges begin to appear when the material is subjected to temperature. This
effect is used as the underlying principle of several thermal sensors. A sublattice of positive
ions in some piezoelectrics turns out to be displaced relative to the sublattice of negative
ions in the state of thermodynamic equilibrium. As a result, such crystals are polarized in
the absence of an external electric field. Thus, these crystals possess a spontaneous electric
polarization. Usually, the presence of such a spontaneous polarization is masked by free
surface charges induced on the surface of the crystal from the surrounding medium by
the electric field due to spontaneous polarization. This process occurs until the electric
field is completely neutralized, that is, until the presence of spontaneous polarization is
totally masked. However, as the temperature of the sample changes, for example, as a result
of heating, the ionic sublattices become displaced relative to one another, which causes
a change in spontaneous polarization, and electric charges appear on the surface of the
crystal. The appearance of these charges is called the direct pyroelectric effect, and the
corresponding crystals are called pyroelectrics. Every pyroelectric is a piezoelectric, but
the converse is not true. This is due to the fact that a pyroelectric has a preferred direction
along which spontaneous polarization takes place, while a piezoelectric generally does not
have such a direction. The inverse pyroelectric effect is also known to exist: a variation of
the electric field in an adiabatically isolated pyroelectric is accompanied by a change in its
212  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
temperature. The existence of the inverse effect can be proved on the basis of a thermody­
namic analysis of the process and be demonstrated experimentally. When conditions are
suitable for spontaneous polarlzation, a dielectric tends to go over to such a state in which,
mum. Under these conditions, domains are formed. The factors that weaken the interac­
tion of dipole moments of molecules cause the disappearance of spontaneous polarization
and the transition from the ferroelectric state to the state of a polar dielectric. Piezoelectric
materials are used widely in transducers such as ultrasonic transmitters and receivers, in
sonar for underwater applications, and as actuators for precision positioning devices.
% This script computes parts (a) and (b) for Example 5.1
% using discrete summation approximation for the integration
clear
% the parameters of the shell
r = 0.2;
% Part (a)
sum=0;         % set initial total sum to zero
theta_inc=1/10;  % choose a suitably small increment
% for the integral
phi_inc=1/10;    % choose a suitably small increment
% for the integral
dtheta=theta_inc*pi/2;
dphi=phi_inc*2*pi;
for theta=0:dtheta:pi/2, % outer integral loop
for phi=0:dphi:2*pi,  % inner integral loop
% add the partial sums to the total sum
sum=sum + 1/r^3*2*cos(theta)*r^2*sin(theta)*dtheta*dphi;
end
end
% display the output
disp(‛’)
disp(sprintf(‛The total current through the ‘))
disp(sprintf(‛ hemispherical shell is %f A’, sum))
% Part (b)
sum=0;         % set initial total sum to zero
r = 0.1;
dtheta=theta_inc*pi;
dphi=phi_inc*2*pi;
for theta=0:dtheta:pi, % outer integral loop
for phi=0:dphi:2*pi,  % inner integral loop
% add the partial sums to the total sum
sum=sum + 1/r^3*2*cos(theta)*r^2*sin(theta)*dtheta*dphi;
end
end
% display the output
disp(‛’)
disp(sprintf(‛The total current through the’))
disp(sprintf(‛ spherical shell is %f A’, sum))
MATLAB 5.1
on the one hand, spontaneous polarization exists and, on the other, the field energy is mini-
MATLAB 5.2
% This script allows the user to enter an electric field
% on either side of a dielectric boundary and compute the
% electric field on the other side of the boundary
% The boundary is assumed to be the plane z=0, with E1 the
% field in
% the region z >=0 and E2 the field in the region z <= 0
% inputs: E1 or E2, er1 and er2 (the relative permittivities
% of both media outputs: E1 or E2, the field not input by
% the user
clear
% prompt user for input materials
disp(‛Enter the relative permittivity in the region ‛);
er1 = input(‛ z > 0... \n >  ‛);
if isempty(er1); er1 = 1; elseif er1 < 1; er1 = 1; end
% check if dielectric is physical
disp(‛Enter the relative permittivity in the region ‛);
er2 = input(‛ z < 0... \n >  ‛);
if isempty(er2); er2 = 1; elseif er2 < 1; er2 = 1; end
% check if dielectric is physical
% prompt the user for the region
disp(‛Enter the side of the interface where the electric‛);
side = input(‛field is known (given)... \n >  ‛);
% if user entered something other than ‟r” ‟c” or ‟s”
% set default as ‟r”
if isempty(side); side = 1; elseif side > 2; side = 2; end
% check if dielectric is physical
if side == 1;
% prompt the user for the field
disp(‛Enter the electric field in side 1 in the ‛);
E1 = input(‛ form [Ex Ey Ez]... \n >’);
E1n = E1(3)*[0 0 1];   % normal direction is +z
E2n = E1n*er1/er2;  % e-field boundary condition
% for normal component
E1t = E1 - E1n;   % tangential component of E1
E2t = E1t;        % e-field boundary condition for
% tangential component
E2 = E2t + E2n;
elseif side == 2;
% prompt the user for the field
disp(‛Enter the electric field in side 2 in the ‛);
E2 = input(‛ form [Ex Ey Ez]... \n >’);
E2n = E2(3)*[0 0 1];     % normal direction is +z
E1n = E2n*er2/er1;  % e-field boundary condition
% for normal component
E2t = E2 - E2n;   % tangential component of E2
5.12 Application Note—Piezoelectrics  213
214  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
E1t = E2t;       % e-field boundary condition for
%tangential component
E1 = E1t + E1n;
else
disp(‛Invalid specification, please re-try \n’);
end
% Display results
disp(sprintf(‘The electric fields are ‘));
disp(sprintf(‘\n E1 = (%d, %d, %d) V/m’,E1(1), E1(2), E1(3)));
disp(sprintf(‘\n E2 = (%d, %d, %d) V/m’,E2(1), E2(2), E2(3)));
1.  Materials can be classified roughly as conductors 1s W 1, er 5 12 and dielectrics
1s V 1, er $ 12 in terms of their electrical properties  and r, where  is the con­
ductivity and r is the dielectric constant or relative permittivity.
2.  Electric current is the flux of electric current density through a surface; that is,
I 5 3 J # dS
3.  The resistance of a conductor of uniform cross section is
R 5 ,
4.  The macroscopic effect of polarization on a given volume of a dielectric material is to
“paint” its surface with a bound charge Qb 5 AS rps dS and leave within it an accumu­
lation of bound charge Qb 5 ev rpv dv, where rps 5 P # an and rpv 5 2= # P.
5.  In a dielectric medium, the D and E fields are related as D 5 eE, where e 5 eoer is
the permittivity of the medium while E and P are related as P 5 xeeoE.
6.  The electric susceptibility xe 15 er 2 12  of a dielectric measures the sensitivity of the
material to an electric field.
7.  A dielectric material is linear if D 5 eE holds, that is, if  is independent of E. It is
homogeneous if  is independent of position. It is isotropic if  is a scalar.
8.  The principle of charge conservation, the basis of Kirchhoff’s current law, is stated in
the continuity equation
= # J 1 'rv
't 5 0
9.  The relaxation time, Tr 5 e/s, of a material is the time taken by a charge placed in its
interior to decrease by a factor of e21 or to .37% of its original magnitude.
10.  Boundary conditions must be satisfied by an electric field existing in two different
media separated by an interface. For a dielectric–dielectric interface
E1t 5 E2t
D1n 2 D2n 5 rS  or  D1n 5 D2n  if  rS 5 0
SUMMARY
Review Questions  215
For a dielectric–conductor interface,
Et 5 0,  Dn 5 eEn 5 rS
because E 5 0 inside the conductor.
11.  Materials of high dielectric constant are of great interest for high-performance elec­
tronic devices.
5.1	 Which is not an example of convection current?
(a)  A moving charged belt
(b)  Electronic movement in a vacuum tube
(c)  An electron beam in a television tube
(d)  Electric current flowing in a copper wire
5.2	 What happens when a steady potential difference is applied across the ends of a conduct­
ing wire?
(a)  All electrons move with a constant velocity.
(b)  All electrons move with a constant acceleration.
(c)  The random electronic motion will, on the average, be equivalent to a constant veloc­
ity of each electron.
(d)  The random electronic motion will, on the average, be equivalent to a nonzero con­
stant acceleration of each electron.
5.3	 The formula R 5 ,/1sS2 is for thin wires.
(a)  True
(c)  Not necessarily
(b)  False
5.4	 Seawater has er 5 80. Its permittivity is
(a)  81
(c)  5.162 3 10210 F/m
(b)  79
(d)  7.074 3 10210 F/m
5.5	 Both o and xe are dimensionless.
(a)  True
(b)  False
5.6	 If = # D 5 e= # E and = # J 5 s= # E in a given material, the material is said to be
(a)  Linear
(d)  Linear and homogeneous
(b)  Homogeneous
(e)  Linear and isotropic
(c)  Isotropic
(f)  Isotropic and homogeneous
REVIEW
QUESTIONS
216  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
5.7	 The relaxation time of mica 1s 5 10215 S/m, er 5 62 is
(a)  5 3 10210 s
(d)  10 hr
(b)  1026 s
(e)  15 hr
(c)  5 hr
5.8	 The uniform fields shown in Figure 5.18 are near a dielectric–dielectric boundary but on
opposite sides of it. Which configurations are correct? Assume that the boundary is charge
free and that 2 > 1.
5.9	 Which of the following statements are incorrect?
(a)  The conductivities of conductors and insulators vary with temperature and frequency.
(b)  A conductor is an equipotential body in steady state, and E is always tangential to the
conductor.
(c)  Nonpolar molecules have no permanent dipoles.
(d)  In a linear dielectric, P varies linearly with E.
FIGURE 5.18  For Review Question 5.8.
Problems  217
5.10	 The electric conditions (charge and potential) inside and outside an electric screening are
completely independent of one another.
(a)  True
(b)  False
Answers: 5.1d, 5.2c, 5.3c, 5.4d, 5.5b, 5.6d, 5.7e, 5.8e, 5.9b, 5.10a.
Section 5.3—Convection and Conduction Currents
5.1
Let the current density be J 5 e2x cos 4 yax 1 e2x sin 4 yay A/m2. Determine the current
crossing the surface x 5 2,  0  y  p/3,  0  z  4.
5.2
In a certain region, J 5 10
r  e2103tar A/m2 . Determine how much current is crossing
surface r 5 4 m at t 5 2 ms.
5.3
Given that J 5 10
r  sin f ar A/m2, determine the current flowing through the surface
r 5 2, 0 , f , p, 0 , z , 5 m.
5.4
In a cylindrical conductor of radius 4 mm, the current density is J 5 5e210raz A/m2.
Find the current through the conductor.
5.5
The current density is
J 5 20 cosu
r 1 3 ar  A/m2
Determine the current through the surface r 5 3, p/4  u  p/2, 0  f  2p.
Section 5.4—Conductors
5.6
A 1 MV resistor is formed by a cylinder of graphite–clay mixture having a length of 2 cm
and a radius of 4 mm. Determine the conductivity of the resistor.
5.7
If the ends of a cylindrical bar of carbon 1s 5 3 3 104 S/m2 of radius 5 mm and length
8 cm are maintained at a potential difference of 9 V, find (a) the resistance of the bar,
(b) the current through the bar, (c) the power dissipated in the bar.
5.8
A conducting wire is 2 mm in radius and 100 m in length. When a dc voltage of 9 V
is applied to the wire, it results in a current of 0.3 A. Find: (a) the E-field in the wire,
(b) the conductivity of the wire.
5.9
Two wires have the same diameter and same resistance. If one is made of copper, and the
other is of silver, which wire is longer?
5.10
A long wire with circular cross section has a diameter of 4 mm. The wire is 5 m long and
it carries 2 A when a 12 V voltage is applied across its ends. Determine the conductivity
of the wire.
PROBLEMS
218  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
FIGURE 5.19  For Problem 5.12.
5.11
A composite conductor 10 m long consists of an inner core of steel of radius 1.5 cm and
an outer sheath of copper whose thickness is 0.5 cm. Take the resistivities of copper and
steel as 1.77 3 1028 and 11.8 3 1028 V # m, respectively.
(a)  Determine the resistance of the conductor.
(b)  If the total current in the conductor is 60 A, what current flows in each metal?
(c)  Find the resistance of a solid copper conductor of the same length and cross-sectional
areas as the sheath.
5.12
The cross section of a conductor made with two materials with resistivities 1 and 2 is
shown in Figure 5.19. Find the resistance of length  of the conductor.
5.13
A 12 V voltage is applied across the ends of a silver wire of length 12.4 m and radius
0.84 mm. Determine the current through the wire.
Sections 5.5–5.7—Polarization and Dielectric Constant
5.14
At a particular temperature and pressure, a helium gas contains 5 3 1025 atoms/m3. If a
10 kV/m field applied to the gas causes an average electron cloud shift of 10218 m, find
the dielectric constant of helium.
5.15
A dielectric material contains 2 3 1019 polar molecules/m3, each of dipole moment
1.8 3 10227 C # m. Assuming that all the dipoles are aligned in the direction of the elec­
tric field E 5 105ax V/m, find P and r.
5.16
A 10 mC point charge is embedded in wood, which has e 5 4.0. Assuming that the
charge is located at the origin, find P at r = 1 m.
5.17
In a certain dielectric for which er 5 3.5, given that P 5 100
r ar nC/m2, find E and D at
r 5 2 m.
5.18
A cylindrical slab has a polarization given by P 5 po a. Find the polarization charge
density pv inside the slab and its surface charge density ps.
5.19
A spherical shell has r 5 1.2 cm and r 5 2.6 cm as inner and outer radii, respectively. If
P 5 4rar pC/m2, determine (a) the total bound surface charge on the inner surface, (b)
the total bound surface charge on the outer surface, (c) the total bound volume charge.
Problems  219
FIGURE 5.20  For Problem 5.23.
ε = ε0
ε = 5ε0
ε = 2ε0
ε = ε0
5.20
In a slab of Teflon 1e 5 2.1 eo2, E 5 6ax 1 12ay 2 20az V/m, find D and P.
5.21
The potential distribution in a dielectric material (e 5 8eo2 is V 5 4x2yz3 V. Find V, E,
and P at point (–2, 5, 3).
5.22
In a dielectric material 1e 5 5eo2, the potential field V 5 10x2yz 2 5z2 V, determine
(a) E, (b) D, (c) P, (d) rv.
5.23
Concentric spheres r 5 a, r 5 b, and r 5 c have charges 4 C, 26 C, and 10 C, respec-
tively, placed on them. If the regions separating them are filled with different dielectrics
as shown in Figure 5.20, find E, D, and P everywhere.
5.24
Consider Figure 5.21 as a spherical dielectric shell so that e 5 eoer for a , r , b and
e 5 eo for 0 , r , a. If a charge Q is placed at the center of the shell, find
(a)  P for a , r , b
(b)  rpv for a , r , b
(c)  rps at r 5 a and r 5 b
5.25	 Two point charges in free space are separated by distance d and exert a force 2.6 nN on
each other. The force becomes 1.5 nN when the free space is replaced by a homogeneous
dielectric material. Calculate the dielectric constant of the material.
*5.26	 A conducting sphere of radius a has a total charge Q uniformly distributed on its surface.
(a)  If the sphere is embedded in a medium with permittivity , find the energy stored.
(b)  Repeat part (a) if the permittivity varies as « 5 «o a1 1 a
r b
220  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
5.27	 A solid sphere of radius a and dielectric constant r has a uniform volume charge
­density of ro.
(a)  At the center of the sphere, show that
V 5 roa2
6eoer
12er 1 12
(b)  Find the potential at the surface of the sphere.
5.28	 In an anisotropic medium, D is related to E as
§ 5 eo £
§ £
Find D due to E 5 Eo1ax 1 ay 2 az2 V/m.
Section 5.8—Continuity Equation and Relaxation Time
5.29
For static (time-independent) fields, which of the following current densities are
­possible?
(a)  J 5 2x3yax 1 4x2z2ay 2 6x2yzaz
(b)  J 5 xyax 1 y1z 1 12ay 1 2yaz
(c)  J 5 z2
r ar 1 z cos f az
(d)  J 5 sin u
r2  ar
5.30
If J 5 e22y sin 2xax 1 e22y cos 2xay 1 zaz A/m2, find the rate of change of the electric
charge density.
5.31
If J 5 100
r2  ar A/m2, find (a) the time rate of increase in the volume charge density, (b) the
total current passing through surface defined by r 5 2, 0 , z , 1, 0 , f , 2p.
5.32 	 An excess charge placed within a conducting medium becomes one-half of its initial
value in 80 ms. Calculate the conductivity of the medium and the relaxation time.
Assume that its dielectric constant is 7.5.
FIGURE 5.21  For Problem 5.24.
Problems  221
5.33
Let rv be the volume charge density of charges in motion. If u is their velocity, show that
(u # =2rv 1 rv= # u 1 'rv
't 5 0.
5.34
The current density is given by J 5 0.5 sin xax A/m2. Determine the time rate of
increase of the charge density (i.e., dv/dt) at point (2, 4, 23).
5.35
Determine the relaxation time for each of the following media:
(a)  Hard rubber 1s 5 10215 S/m, e 5 3.1eo2
(b)  Mica 1s 5 10215 S/m, e 5 6eo2
(c)  Distilled water 1s 5 1024 S/m, e 5 80eo2
5.36
Lightning strikes a dielectric sphere of radius 20 mm for which er 5 2.5, s 5
5 3 1026 S/m and deposits uniformly a charge of 1 C. Determine the initial volume
charge density and the volume charge density 2 ms later.
Section 5.9—Boundary Conditions
5.37
Show that the normal and tangential components of the current density J at the interface
between two media with conductivities s1 and s2 satisfy
J1n 5 J2n,    J1t
J2t
5 s1
5.38
Let z < 0 be region 1 with dielectric constant er1 5 4, while z  0 is region 2 with
er2 5 7.5. Given that E1 5 60ax 2 100ay 1 40az V/m, (a) find P1, (b) calculate D2.
5.39
Region 1 is x  0 with, e1 5 4eo, while region 2 is x  0 with e 5 2eo. If
E2 5 6ax 2 10ay 1 8az V/m, (a) find P1, and P2, (b) calculate the energy densities in
both regions.
5.40
A dielectric interface is defined by 4x 1 3y 5 10 m. The region including the origin is
free space, where D1 5 2ax 2 4ay 1 6.5az nC/m2. In the other region, er2 5 2.5. Find D2
and the angle u2 that D2 makes with the normal.
5.41
Regions 1 and 2 have permittivities e1 5 2eo and e2 5 5eo. The regions are separated
by a plane whose equation is x + 2y + z = 1 such that x + 2y + z  1 is region 1. If
E1 5 20ax 2 10ay 1 40az V/m, find: (a) the normal and tangential components of E1,
(b) E2.
5.42
Given that E1 5 10ax 2 6ay 1 12az V/m in Figure 5.22, find (a) P1, (b) E2 and the angle
E2 makes with the y-axis, (c) the energy density in each region.
5.43
Two homogeneous dielectric regions 1 1r # 4 cm2 and 2 1r $ 4 cm2 have dielectric
constants 3.5 and 1.5, respectively. If D2 5 12ar 2 6af 1 9az nC/m2, calculate (a) E1
and D1, (b) P2 and rpv2, (c) the energy density for each region.
222  CHAPTER 5  ELECTRIC FIELDS IN MATERIAL SPACE
5.44	 A conducting sphere of radius a is half-embedded in a liquid dielectric medium of
permittivity 1 as in Figure 5.23. The region above the liquid is a gas of permittivity
2. If the total free charge on the sphere is Q, determine the electric field intensity
everywhere.
5.45	 A dielectric sphere e1 5 2eo is buried in a medium with e2 5 6eo. Given that
E2 5 10sinuar 1 5cosuau in the medium, calculate E1 and D1 in the dielectric
sphere.
*5.46	 Two parallel sheets of glass 1er 5 8.52 mounted vertically are separated by a uniform
air gap between their inner surface. The sheets, properly sealed, are immersed in oil
1er 5 3.02 as shown in Figure 5.24. A uniform electric field of strength 2 kV/m in
the horizontal direction exists in the oil. Calculate the magnitude and direction of the
electric field in the glass and in the enclosed air gap when (a) the field is normal to the
glass surfaces and (b) the field in the oil makes an angle of 75° with a normal to the glass
surfaces. Ignore edge effects.
ε2 = 4.5ε0
ε1 = 3ε0
FIGURE 5.22  For Problem 5.42.
FIGURE 5.23  For Problem 5.44.
Problems  223
30°
ε1 = 2ε0
ε2 = 3ε0
FIGURE 5.25  For Problem 5.49.
Glass
Oil
Oil
Air
FIGURE 5.24  For Problem 5.46.
5.47
At a point on a conducting surface, E 5 30ax 2 40ay 1 20az mV/m. Calculate the surface
charge density at that point.
5.48
(a)  Given that E 5 15ax 2 8az V/m at a point on a conductor surface, what is the
­surface charge density at that point? Assume e 5 eo.
(b)  Region y $ 2 is occupied by a conductor. If the surface charge on the conductor
is 220 nC/m2, find D just outside the conductor.
5.49
Two planar slabs of equal thickness but with different dielectric constants are shown in
Figure 5.25. Eo in air makes an angle of 30° with the z-axis. Calculate the angle that E
makes with the z-axis in each of the two dielectric layers.
Pierre-Simon de Laplace  (1749–1827), a French ­astronomer and math­
ematician, discovered the Laplace transform and Laplace’s equation, to be
discussed in this chapter. He believed the world was entirely deterministic.
To Laplace, the universe was nothing but a giant problem in calculus.
Born of humble origins in Beaumont-en-Auge, Normandy, Laplace
became a ­professor of mathematics at the age of 20. His mathematical
abilities inspired the famous mathematician Siméon Poisson, who called
Laplace the Isaac Newton of France. Laplace made important contributions
in potential theory, probability theory, astronomy, and celestial ­mechanics.
He was widely known for his work Traité de Mécanique Céleste (Celestial Mechanics), which
­supplemented the work of Newton on astronomy. Laplace is one of the few giants in the history of
probability and statistics. He was born and died a Catholic.
Siméon-Denis Poisson  (1781–1840), a French mathematical physicist
whose name is attached to a wide area of ideas: Poisson’s integral, Poisson’s
equation in potential theory (to be discussed in this chapter), Poisson
brackets in differential equations, Poisson’s ratio in elasticity, the Poisson
distribution in probability theory, and Poisson’s ­constant in ­electricity.
Born at Pithviers, south of Paris, the son of a retired soldier, Siméon
Poisson was originally forced to study medicine by his family, but he began
to study mathematics in 1798 at the École Polytechnique at the age of 17.
His abilities excited the interest of his teachers Lagrange and Laplace, whose
friendship he retained to the end of their lives. A paper on finite differences, written when Poisson
was 18, attracted the attention of ­Legendre. Poisson’s chief interest lay in the application of mathemat­
ics to physics, ­especially in electrostatics and magnetism. Poisson made important contributions to
­mechanics, theory of elasticity, optics, calculus, differential geometry, and probability ­theory. He
published between 300 and 400 ­mathematical works.

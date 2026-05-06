# Sadiku《Elements of Electromagnetics》Chapter 1

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 30-57 of 926 (926 total)

---

## Vector Algebra

C H A P T E R
1.1  INTRODUCTION
Electromagnetics (EM) may be regarded as the study of the interactions between electric
charges at rest and in motion. It entails the analysis, synthesis, physical interpretation, and
application of electric and magnetic fields.
Electromagnetics (EM) is a branch of physics or electrical engineering in which
electric and magnetic phenomena are studied.
EM principles find applications in various allied disciplines such as microwaves, antennas,
electric machines, satellite communications, bioelectromagnetics, plasmas, nuclear research,
fiber optics, electromagnetic interference and compatibility, electromechanical energy conver­
sion, radar meteorology, and remote sensing.1,2 In physical medicine, for example, EM power,
in the form either of shortwaves or microwaves, is used to heat deep tissues and to stimulate
certain physiological responses in order to relieve certain pathological conditions. EM fields
are used in induction heaters for melting, forging, annealing, surface hardening, and soldering
operations. Dielectric heating equipment uses shortwaves to join or seal thin sheets of plastic
materials. EM energy offers many new and exciting possibilities in agriculture. It is used, for
example, to change vegetable taste by reducing acidity.
EM devices include transformers, electric relays, radio/TV, telephones, electric motors,
transmission lines, waveguides, antennas, optical fibers, radars, and lasers. The design of
these devices requires thorough knowledge of the laws and principles of EM.
1For numerous applications of electrostatics, see J. M. Crowley, Fundamentals of Applied Electrostatics. New
York: John Wiley & Sons, 1986.
2For other areas of applications of EM, see, for example, D. Teplitz, ed., Electromagnetism: Paths to Research.
New York: Plenum Press, 1982.
VECTOR ALGEBRA
Books are the quietest and most constant friends; they are the most accessible and
wisest of counselors, and most patient of teachers.
—CHARLES W. ELLIOT
4  CHAPTER 1  VECTOR ALGEBRA
The subject of electromagnetic phenomena in this book can be summarized in Maxwell’s
equations:
= # D 5 rv
(1.1)
= # B 5 0
(1.2)
= 3 E 5 2'B
(1.3)
= 3 H 5 J 1 'D
(1.4)
where = 5 the vector differential operator
D 	5 the electric flux density
B 	5 the magnetic flux density
E 	5 the electric field intensity
H 	5 the magnetic field intensity
v 5 the volume charge density
J 	5 the current density
Maxwell based these equations on previously known results, both experimental and theore­
tical. A quick look at these equations shows that we shall be dealing with vector quantities. It
is consequently logical that we spend some time in Part 1 examining the mathematical tools
required for this course. The derivation of eqs. (1.1) to (1.4) for time-invariant conditions
and the physical significance of the quantities D, B, E, H, J, and v will be our aim in Parts 2
and 3. In Part 4, we shall reexamine the equations for time-varying situations and apply
them in our study of practical EM devices such as transmission lines, waveguides, antennas,
fiber optics, and radar systems.
†1.2  A PREVIEW OF THE BOOK
1.3  SCALARS AND VECTORS
Vector analysis is a mathematical tool with which electromagnetic concepts are most con­
veniently expressed and best comprehended. We must learn its rules and techniques before
we can confidently apply it. Since most students taking this course have little exposure to
vector analysis, considerable attention is given to it in this and the next two chapters.3 This
chapter introduces the basic concepts of vector algebra in Cartesian coordinates only. The
next chapter builds on this and extends to other coordinate systems.
A quantity can be either a scalar or a vector. A scalar is a quantity that is completely
specified by its magnitude.
†Indicates sections that may be skipped, explained briefly, or assigned as homework if the text is covered in one
semester.
3The reader who feels no need for review of vector algebra can skip to the next chapter.
1.4 Unit Vector  5
A scalar is a quantity that has only magnitude.
Quantities such as time, mass, distance, temperature, entropy, electric potential, and popu­
lation are scalars. A vector has not only magnitude, but direction in space.
A vector is a quantity that is described by both magnitude and direction.
Vector quantities include velocity, force, momentum, acceleration displacement, and electric
field intensity. Another class of physical quantities is called tensors, of which scalars and vectors
are special cases. For most of the time, we shall be concerned with scalars and vectors.4
To distinguish between a scalar and a vector it is customary to represent a vector by
a letter with an arrow on top of it, such as A
and B
, or by a letter in boldface type such as
A and B. A scalar is represented simply by a letter—for example, A, B, U, and V.
EM theory is essentially a study of some particular fields.
A field is a function that specifies a particular quantity everywhere in a region.
A field may indicate variation of a quantity throughout space and perhaps with time.
If the quantity is scalar (or vector), the field is said to be a scalar (or vector) field. Examples
of scalar fields are temperature distribution in a building, sound intensity in a theater, electric
potential in a region, and refractive index of a stratified medium. The gravitational force on
a body in space and the velocity of raindrops in the atmosphere are examples of vector fields.
1.4  UNIT VECTOR
A vector A has both magnitude and direction. The magnitude of A is a scalar written as
A or 0 A 0 . A unit vector aA along A is defined as a vector whose magnitude is unity (i.e., 1)
and its direction is along A; that is,
aA 5 A
0 A 0 5 A
(1.5)
Note that 0 aA 0 5 1. Thus we may write A as
A 5 AaA
(1.6)
which completely specifies A in terms of its magnitude A and its direction aA.
A vector A in Cartesian (or rectangular) coordinates may be represented as
1Ax, Ay, Az2        or        Axax 1 Ayay 1 Azaz
(1.7)
4For an elementary treatment of tensors, see, for example, A. I. Borisenko and I. E. Tarapor, Vector and Tensor
Analysis with Applications. New York: Dover, 1979.
6  CHAPTER 1  VECTOR ALGEBRA
where Ax, Ay, and Az are called the components of A in the x-, y-, and z-directions, respec-
tively; ax, ay, and az are unit vectors in the x-, y-, and z-directions, respectively. For example,
ax is a dimensionless vector of magnitude one in the direction of the increase of the x-axis.
The unit vectors ax, ay, and az are illustrated in Figure 1.1(a), and the components of A along
the coordinate axes are shown in Figure 1.1(b). The magnitude of vector A is given by
A 5 "Ax
2 1 Ay
2 1 Az
(1.8)
and the unit vector along A is given by
aA 5
Axax 1 Ayay 1 Azaz
"Ax
2 1 Ay
2 1 Az
(1.9)
FIGURE 1.1  (a) Unit vectors ax, ay, and az, (b) components of A
along ax, ay, and az.
1.5  VECTOR ADDITION AND SUBTRACTION
Two vectors A and B can be added together to give another vector C; that is,
C 5 A 1 B
(1.10)
The vector addition is carried out component by component. Thus, if A 5 1Ax, Ay, Az)
and B 5 1Bx, By, Bz).
C 5 1Ax 1 Bx2ax 1 1Ay 1 By2ay 1 1Az 1 Bz2az
(1.11)
Vector subtraction is similarly carried out as
D 5 A 2 B 5 A 1 12B2
5 1Ax 2 Bx2ax 1 1Ay 2 By2ay 1 1Az 2 Bz2az
(1.12)
1.6 Position and Distance Vectors  7
Graphically, vector addition and subtraction are obtained by either the parallelogram rule
or the head-to-tail rule as portrayed in Figures 1.2 and 1.3, respectively.
The three basic laws of algebra obeyed by any given vectors A, B, and C are summa­
rized as follows:
Law
Addition
Multiplication
Commutative
A 1 B 5 B 1 A
kA 5 Ak
Associative
A 1 1B 1 C2 5 1A 1 B2 1 C
k(,A) 5 (k,)A
Distributive
k1A 1 B2 5 kA 1 kB
where k and , are scalars. Multiplication of a vector with another vector will be discussed
in Section 1.7.
FIGURE 1.3  Vector subtraction
D 5 A 2 B: (a) parallelogram rule,
(b) ­head-to-tail rule.
FIGURE 1.2  Vector addition C 5 A 1 B: (a) parallelogram rule,
(b) head-to-tail rule.
1.6  POSITION AND DISTANCE VECTORS
A point P in Cartesian coordinates may be represented by (x, y, z).
The position vector rP (or radius vector) of point P is defined as the directed dis­
tance from the origin O to P; that is,
rP 5 OP 5 xax 1 yay 1 zaz
(1.13)
8  CHAPTER 1  VECTOR ALGEBRA
The position vector of point P is useful in defining its position in space. Point (3, 4, 5), for
example, and its position vector 3ax 1 4ay 1 5az are shown in Figure 1.4.
The distance vector is the displacement from one point to another.
If two points P and Q are given by (xP, yP, zP) and (xQ, yQ, zQ), the distance vector (or
separation vector) is the displacement from P to Q as shown in Figure 1.5; that is,
rPQ 5 rQ 2 rP
5 1xQ 2 xP2ax 1 1yQ 2 yP2ay 1 1zQ 2 zP2az
(1.14)
The difference between a point P and a vector A should be noted. Though both P
and A may be represented in the same manner as (x, y, z) and (Ax, Ay, Az), respectively,
the point P is not a vector; only its position vector rP is a vector. Vector A may depend on
point P, however. For example, if A 5 2xyax 1 y2ay 2 xz2az and P is 12, 21, 42, then A at
P would be 24ax 1 ay 2 32az. A vector field is said to be constant or uniform if it does
not depend on space variables x, y, and z. For example, vector B 5 3ax 2 2ay 1 10az is a
uniform vector while vector A 5 2xyax 1 y2ay 2 xz2az is not uniform because B is the
same everywhere, whereas A varies from point to point.
FIGURE 1.4  Illustration of position vector
rP 5 3ax 1 4ay 5 5az.
FIGURE 1.5  Distance vector rPQ.
EXAMPLE 1.1
If A 5 10ax 2 4ay 1 6az and B 5 2ax 1 ay, find (a) the component of A along ay, (b) the
magnitude of 3A 2 B, (c) a unit vector along A 1 2B.
1.6 Position and Distance Vectors  9
Solution:
(a)  The component of A along ay is Ay 5 24.
(b)  3A 2 B 5 3110, 24, 62 2 12, 1, 02
5 130, 212, 182 2 12, 1, 02
5 128, 213, 182
Hence,
0 3A 2 B 0 5 "282 1 12132 2 1 1182 2 5 "1277
5 35.74
(c)  Let C 5 A 1 2B 5 110, 24, 62 1  14, 2, 02 5 114, 22, 62.
A unit vector along C is
ac 5 C
0 C 0 5
114, 22, 62
"142 1 1222 2 1 62
ac 5 0.9113ax 2 0.1302ay 1 0.3906az
Note that 0 ac 0 5 1 as expected.
PRACTICE EXERCISE  1.1
Given vectors A 5 ax 1 3az and B 5 5ax 1 2ay 2 6az, determine
(a)	 uA 1 Bu
(b)	 5A 2 B
(c)	 The component of A along ay
(d)	 A unit vector parallel to 3A 1 B
Answer:  (a) 7,  (b) (0, 22, 21),  (c) 0,  (d) 6(0.9117, 0.2279, 0.3419).
Points P and Q are located at (0, 2, 4) and 123, 1, 52. Calculate
(a)  The position of vector rP
(b)  The distance vector from P to Q
(c)  The distance between P and Q
(d)  A vector parallel to PQ with magnitude of 10
EXAMPLE 1.2
10  CHAPTER 1  VECTOR ALGEBRA
Solution:
(a)  rP 5 0ax 1 2ay 1 4az 5 2ay 1 4az
(b)  rPQ 5 rQ 2 rP 5 123, 1, 52 2 10, 2, 42 5 123, 21, 12
or rPQ 5 23ax 2 ay 1 az
(c)  Since rPQ is the distance vector from P to Q, the distance between P and Q is the mag­
nitude of this vector; that is,
d 5 0 rPQ 0 5 "9 1 1 1 1 5 3.317
Alternatively:
d 5 "1xQ 2 xP2 2 1 1yQ 2 yP2 2 1 1zQ 2 zP2 2
5 "9 1 1 1 1 5 3.317
(d)  Let the required vector be A, then
A 5 AaA
where A 5 10 is the magnitude of A. Since A is parallel to PQ, it must have the same unit
vector as rPQ or rQP. Hence,
aA 5 6
rPQ
0 rPQ 0 5 6
123, 21, 12
3.317
and
A 5 610123, 21, 12
3.317
5 6129.045ax 2 3.015ay 1 3.015az2
PRACTICE EXERCISE  1.2
Given points P(1, 23, 5), Q(2, 4, 6), and R(0, 3, 8), find (a) the position vectors of P and
R, (b) the distance vector rQR, (c) the distance between Q and R.
Answer:  (a) ax 2 3ay 1 5az, 3ax 1 8az,  (b) 22ax 2 ay 1 2az, (c) 3.
A river flows southeast at 10 km/hr and a boat floats upon it with its bow pointed in the
direction of travel. A man walks upon the deck at 2 km/hr in a direction to the right and
perpendicular to the direction of the boat’s movement. Find the velocity of the man with
respect to the earth.
Solution:
Consider Figure 1.6 as illustrating the problem. The velocity of the boat is
5 7.071ax 2 7.071ay km/hr
EXAMPLE 1.3
ub 5 101cos 45° ax 2 sin 45° ay2
1.7 Vector Multiplication  11
PRACTICE EXERCISE  1.3
An airplane has a ground speed of 350 km/hr in the direction due west. If there is a wind
blowing northwest at 40 km/hr, calculate the true air speed and heading of the airplane.
Answer:  379.3 km/hr, 4.275° north of west.
FIGURE 1.6  For Example 1.3.
1.7  VECTOR MULTIPLICATION
When two vectors A and B are multiplied, the result is either a scalar or a vector depending
on how they are multiplied. Thus there are two types of vector multiplication:
1.	 Scalar (or dot) product: A # B
2.	 Vector (or cross) product: A 3 B
uab 5 um 1 ub 5 5.657ax 2 8.485ay
0 uab 0 5 10.2l256.3°
iii
that is, 10.2 km/hr at 56.3° south of east.
The velocity of the man with respect to the boat (relative velocity) is
um 5 212 cos 45° ax 2 sin 45° ay2
5 21.414ax 2 1.414ay km/hr
Thus the absolute velocity of the man is
12  CHAPTER 1  VECTOR ALGEBRA
Multiplication of three vectors A, B, and C can result in either:
3.	 Scalar triple product: A # 1B 3 C2
4.	 Vector triple product: A 3 1B 3 C2
A.  Dot Product
The dot product of two vectors A and B, written as A ? B, is defined geometrically
as the product of the magnitudes of A and B and the cosine of the smaller angle
between them when they are drawn tail to tail.
Thus,
A # B 5 AB cos uAB
(1.15)
where uAB is the smaller angle between A and B. The result of A # B is called either the scalar
product because it is scalar or the dot product due to the dot sign. If A 5 1Ax, Ay, Az2 and
B 5 1Bx, By, Bz), then
A # B 5 AxBx 1 AyBy 1 AzBz
(1.16)
which is obtained by multiplying A and B component by component. Two vectors A and B
are said to be orthogonal (or perpendicular) with each other if A # B 5 0.
Note that dot product obeys the following:
(i)  Commutative law:
A # B 5 B # A
(1.17)
(ii)	 Distributive law:
A # 1B 1 C2 5 A # B 1 A # C
(1.18)
(iii)
A # A 5 0 A 0 2 5 A2
(1.19)
Also note that
ax # ay 5 ay # az 5 az # ax 5 0
(1.20a)
ax # ax 5 ay # ay 5 az # az 5 1
(1.20b)
It is easy to prove the identities in eqs. (1.17) to (1.20) by applying eq. (1.15) or (1.16).
If A # B 5 0, the two vectors A and B are orthogonal or perpendicular.
1.7 Vector Multiplication  13
B.  Cross Product
The cross product of two vectors A and B, written as A 3 B, is a vector quantity
whose magnitude is the area of the parallelogram formed by A and B (see Figure 1.7)
and is in the direction of advance of a right-handed screw as A is turned into B.
Thus,
A 3 B 5 AB sin uABan
(1.21)
where an is a unit vector normal to the plane containing A and B. The direction of an is
taken as the direction of the right thumb when the fingers of the right hand rotate from
A to B as shown in Figure 1.8(a). Alternatively, the direction of an is taken as that of the
advance of a right-handed screw as A is turned into B as shown in Figure 1.8(b).
The vector multiplication of eq. (1.21) is called cross product owing to the cross
sign; it is also called vector product because the result is a vector. If A 5 1Ax, Ay, Az) and
B 5 1Bx, By, Bz), then
A 3 B 5 3
(1.22a)
5 1AyBz 2 AzBy2ax 1 1AzBx 2 AxBz2ay 1 1AxBy 2 AyBx2az
(1.22b)
which is obtained by “crossing” terms in cyclic permutation, hence the name “cross
product.”
FIGURE 1.7  The cross product of A and B is a vector with magnitude equal
to the area of the parallelogram and direction as indicated.
14  CHAPTER 1  VECTOR ALGEBRA
Note that the cross product has the following basic properties:
(i)	 It is not commutative:
A 3 B 2 B 3 A
(1.23a)
It is anticommutative:
A 3 B 5 2B 3 A
(1.23b)
(ii)	 It is not associative:
A 3 1B 3 C2 2 1A 3 B2 3 C
(1.24)
(iii)  It is distributive:
A 3 1B 1 C2 5 A 3 B 1 A 3 C
(1.25)
(iv)  Scaling:
kA 3 B 5 A 3 kB 5 k1A 3 B2
(1.26)
(v)
A 3 A 5 0
(1.27)
Also note that
ax 3 ay 5 az
ay 3 az 5 ax
(1.28)
az 3 ax 5 ay
which are obtained in cyclic permutation and illustrated in Figure 1.9. The identities in eqs.
(1.23) to (1.28) are easily verified by using eq. (1.21) or (1.22). It should be noted that in
obtaining an, we have used the right-hand or right-handed-screw rule because we want to
FIGURE 1.8  Direction of A 3 B and an using (a) the right-hand rule and (b) the
right-handed-screw rule.
1.7 Vector Multiplication  15
be consistent with our coordinate system illustrated in Figure 1.1, which is right-handed.
A right-handed coordinate system is one in which the right-hand rule is satisfied: that is,
ax 3 ay 5 az is obeyed. In a left-handed system, we follow the left-hand or left-handed
screw rule and ax 3 ay 5 2az is satisfied. Throughout this book, we shall stick to right-
handed coordinate systems.
Just as multiplication of two vectors gives a scalar or vector result, multiplication of
three vectors A, B, and C gives a scalar or vector result, depending on how the vectors are
multiplied. Thus we have a scalar or vector triple product.
C.  Scalar Triple Product
Given three vectors A, B, and C, we define the scalar triple product as
A # 1B 3 C2 5 B # 1C 3 A2 5 C # 1A 3 B2
(1.29)
obtained in cyclic permutation. If A 5 1Ax, Ay, Az), B 5 1Bx, By, Bz), and C 5 1Cx, Cy, Cz),
then A # 1B 3 C2 is the volume of a parallelepiped having A, B, and C as edges and is easily
obtained by finding the determinant of the 3 3 3 matrix formed by A, B, and C; that is,
A # 1B 3 C2 5 3
(1.30)
Since the result of this vector multiplication is scalar, eq. (1.29) or (1.30) is called the scalar
triple product.
D.  Vector Triple Product
For vectors A, B, and C, we define the vector triple product as
A 3 1B 3 C2 5 B1A # C2 2 C1A # B2
(1.31)
FIGURE 1.9  Cross product using cyclic permutation. (a) Moving
clockwise leads to positive results. (b) Moving counterclockwise
leads to negative results.
16  CHAPTER 1  VECTOR ALGEBRA
which may be remembered as the “bac-cab” rule. It should be noted that
1A # B2C 2 A1B # C2
(1.32)
but
1A # B2C 5 C1A # B2
(1.33)
1.8  COMPONENTS OF A VECTOR
A direct application of scalar product is its use in determining the projection (or compo­
nent) of a vector in a given direction. The projection can be scalar or vector. Given a vector
A, we define the scalar component AB of A along vector B as [see Figure 1.10(a)]
AB 5 A cos uAB 5 0 A 0 0 aB 0  cos uAB
AB 5 A # aB
(1.34)
The vector component AB of A along B is simply the scalar component in eq. (1.34) multi­
plied by a unit vector along B; that is,
AB 5 ABaB 5 1A # aB2aB
(1.35)
Both the scalar and vector components of A are illustrated in Figure 1.10. Notice from Figure
1.10(b) that the vector can be resolved into two orthogonal components: one ­component AB par­
allel to B, another 1A 2 AB2 perpendicular to B. In fact, our Cartesian representation of a vector
is essentially resolving the vector into three mutually orthogonal components as in Figure 1.1(b).
We have considered addition, subtraction, and multiplication of vectors. However, divi­
sion of vectors A/B has not been considered because it is undefined except when A and B are
parallel so that A 5 kB, where k is a constant. Differentiation and integration of vectors will be
considered in Chapter 3.
FIGURE 1.10  Components of A along B: (a) scalar component AB,
(b) vector component AB.
1.8 Components of a Vector  17
Given vectors A 5 3ax 1 4ay 1 az and B 5 2ay 2 5az, find the angle between A and B.
Solution:
The angle uAB can be found by using either dot product or cross product.
A # B 5 13, 4, 12 # 10, 2, 252
5 0 1 8 2 5 5 3
0 A 0 5 "32 1 42 1 12 5 "26
0 B 0 5 "02 1 22 1 1252 2 5 "29
cos uAB 5 A # B
0 A 0 0 B 0 5
"1262 1292
5 0.1092
uAB 5 cos21
Alternatively:
A 3 B 5 3
5 1220 2 22ax 1 10 1 152ay 1 16 2 02az
5 1222, 15, 62
0 A 3 B 0 5 "12222 2 1 152 1 62 5 "745
sin uAB 5
0 A 3 B 0
0 A 0 0 B 0
"745
"1262 1292
5 0.994
uAB 5 sin21 0.994 5 83.73°
PRACTICE EXERCISE  1.4
If A 5 ax 1 3az and B 5 5ax 1 2ay 2 6az, find uAB.
Answer:  120.6°.
Three field quantities are given by
P 5 2ax 2 az
Q 5 2ax 2 ay 1 2az
R 5 2ax 2 3ay 1 az
Determine
(a)  1P 1 Q2 3 1P 2 Q2
(b)  Q # R 3 P
(c)  P # Q 3 R
EXAMPLE 1.4
EXAMPLE 1.5
0.1092 5 83.73°
18  CHAPTER 1  VECTOR ALGEBRA
(d)	 sin uQR
(e)	 P 3 1Q 3 R2
(f)	 A unit vector perpendicular to both Q and R
(g)	 The component of P along Q
Solution:
(a)
1P 1 Q2 3 1P 2 Q2 5 P 3 1P 2 Q2 1 Q 3 1P 2 Q2
5 P 3 P 2 P 3 Q 1 Q 3 P 2 Q 3 Q
5 0 1 Q 3 P 1 Q 3 P 2 0
5 2Q 3 P
5 2 3
5 211 2 02 ax 1 214 1 22 ay 1 210 1 22 az
5 2ax 1 12ay 1 4az
(b)	 The only way Q # R 3 P makes sense is
Q # 1R 3 P2 5 12, 21, 22 # 3
5 12, 21, 22 # 13, 4, 62
5  6 2 4 1 12 5 14
Alternatively:
Q # 1R 3 P2 5
To find the determinant of a 3 3 3 matrix, we repeat the first two rows and cross multiply;
when the cross multiplication is from right to left, the result should be negated as shown
diagrammatically here. This technique of finding a determinant applies only to a 3 3 3
matrix. Hence,
Q # 1R 3 P2 5        5
5 16 1 0 2 2 1 12 2 0 2 2
5 14
as obtained before.
1.8 Components of a Vector  19
(c)	 From eq. (1.29)
P # 1Q 3 R2 5 Q # 1R 3 P2 5 14
P # 1Q 3 R2 5 12, 0, 212 # 15, 2, 242
5 10 1 0 1 4
5 14
(d)
sin uQR 5
0 Q 3 R 0
0 Q 0 0 R 0
15, 2, 242 0
0 12, 21, 22 0 0 12, 23, 12 0
5 "45
3"14
5 "5
"14
5 0.5976
(e)
P 3 1Q 3 R2 5 12, 0, 212 3 15, 2, 242
5 12, 3, 42
Alternatively, using the bac-cab rule,
P 3 1Q 3 R2 5 Q1P # R2 2 R1P # Q2
5 12, 21, 22 14 1 0 2 12 2 12, 23, 12 14 1 0 2 22
5 12, 3, 42
(f)  A unit vector perpendicular to both Q and R is given by
a 5 6Q 3 R
0 Q 3 R 0 5 615, 2, 242
"45
5 610.745, 0.298, 20.5962
Note that 0 a 0 5 1, a # Q 5 0 5 a # R. Any of these can be used to check a.
(g)	 The component of P along Q is
PQ 5 0 P 0  cos uPQaQ
5 1P # aQ2aQ 5
1P # Q2Q
0 Q 0 2
14 1 0 2 22 12, 21, 22
14 1 1 1 42
5 2
9 12, 21, 22
5 0.4444ax 2 0.2222ay 1 0.4444a
20  CHAPTER 1  VECTOR ALGEBRA
PRACTICE EXERCISE  1.5
Let E 5 3ay 1 4az and F 5 4ax 2 10ay 1 5az.
(a)  Find the component of E along F.
(b)  Determine a unit vector perpendicular to both E and F.
Answer:  (a) (20.2837, 0.7092, 20.3546),  (b) 6(0.9398, 0.2734, 20.205).
Derive the cosine formula
a2 5 b2 1 c2 2 2bc cos A
and the sine formula
sin A
5 sin B
5 sin C
using dot product and cross product, respectively.
Solution:
Consider a triangle as shown in Figure 1.11. From the figure, we notice that
a 1 b 1 c 5 0
that is,
b 1 c 5 2a
Hence,
a2 5 a # a 5 1b 1 c2 # 1b 1 c2
5 b # b 1 c # c 1 2b # c
a2 5 b2 1 c2 2 2bc cos A
where (p 2 A) is the angle between b and c.
The area of a triangle is half of the product of its height and base. Hence,
` 1
2a 3 b` 5 ` 1
2b 3 c` 5 ` 1
2c 3 a`
ab sin C 5 bc sin A 5 ca sin B
Dividing through by abc gives
sin A
5 sin B
5 sin C
EXAMPLE 1.6
1.8 Components of a Vector  21
EXAMPLE 1.7
FIGURE 1.11  For Example 1.6.
PRACTICE EXERCISE  1.6
Show that vectors a 5 (4, 0, 21), b 5 (1, 3, 4), and c 5 (25, 23, 23) form the sides
of a triangle. Is this a right angle triangle? Calculate the area of the triangle.
Answer:  Yes, 10.5.
Show that points P115, 2, 242, P211, 1, 22, and P3123, 0, 82 all lie on a straight line.
Determine the shortest distance between the line and point P413, 21, 02.
Solution:
The distance vector rP1P2 is given by
rP1P2 5 rP2 2 rP1 5 11, 1, 22 2 15, 2, 242
5 124, 21, 62
Similarly,
rP1P3 5 rP3 2 rP1 5 123, 0, 82 2 15, 2, 242
5 128, 22, 122
rP1P4 5 rP4 2 rP1 5 13, 21, 02 2 15, 2, 242
5 122, 23, 42
rP1P2 3 rP1P3 5 3
5 10, 0, 02
showing that the angle between rP1P2 and rP1P3 is zero 1sin u 5 02. This implies that P1, P2,
and P3 lie on a straight line.
Alternatively, the vector equation of the straight line is easily determined from Figure
1.12(a). For any point P on the line joining P1 and P2
rP1P 5 lrP1P2
where λ is a constant. Hence the position vector rP of the point P must satisfy
rP 2 rP1 5 l1rP2 2 rP12
22  CHAPTER 1  VECTOR ALGEBRA
that is,
rP 5 rP1 1 l1rP2 2 rP12
5 15, 2, 242 2 l14, 1, 262
rP 5 15 2 4l, 2 2 l, 24 1 6l2
This is the vector equation of the straight line joining P1 and P2. If P3 is on this line, the
position vector of P3 must satisfy the equation; r3 does satisfy the equation when l 5 2.
The shortest distance between the line and point P413, 21, 02 is the perpendicular
distance from the point to the line. From Figure 1.12(b), it is clear that
d 5 rP1P4 sin u 5 0 rP1P4 3 aP1P2 0
0 122, 23, 42 3 124, 21, 62 0
0 124, 21, 62 0
5 "312
"53
5 2.426
Any point on the line may be used as a reference point. Thus, instead of using P1 as a reference
point, we could use P3. If jP4P3 P2 5 , then
d 5 0 rP3P4 0  sin ur 5 0 rP3P4 3 aP3P2 0
PRACTICE EXERCISE  1.7
If P1 is (1, 2, 23) and P2 is (24, 0, 5), find
(a)  The distance P1P2
(b)  The vector equation of the line P1P2
(c)  The shortest distance between the line P1P2 and point P3 (7, 21, 2)
Answer:  (a) 9.644,  (b) (1 2 5l)ax 1 2(1 2 l)ay 1 (8l 2 3)az,  (c) 8.2.
FIGURE 1.12  For Example 1.7.
Summary  23
1.	 A field is a function that specifies a quantity in space. For example, A(x, y, z) is a vector
field, whereas V(x, y, z) is a scalar field.
2.	 A vector A is uniquely specified by its magnitude and a unit vector along it, that is, A 5 AaA.
3.	 Multiplying two vectors A and B results in either a scalar A # B 5 AB cos uAB or a
vector A 3 B 5 AB sin uAB an. Multiplying three vectors A, B, and C yields a scalar
A # 1B 3 C2 or a vector A 3 1B 3 C2.
4.	 The scalar projection (or component) of vector A onto B is AB 5 A # aB, whereas vector
projection of A onto B is AB 5 ABaB.
5.	 The MATLAB commands dot(A,B) and cross(A,B) are used for dot and cross products,
respectively.
% This script allows the user to input two vectors and
% then compute their dot product, cross product, sum,
% and difference
clear
vA = input(‵Enter vector A in the format [x y z]... \n >  ‵);
if isempty(vA); vA = [0 0 0]; end    % if the input is
% entered incorrectly set the vector to 0
vB = input(‵Enter vector B in the format [x y z]... \n >  ‵);
if isempty(vB); vB = [0 0 0]; end
disp(‵Magnitude of A:’)
disp(norm(vA))            % norm finds the magnitude of a
% multi-dimensional vector
disp(‵Magnitude of B:’)
disp(norm(vB))
disp(‵Unit vector in direction of A:’)
disp(vA/norm(vA))         % unit vector is the vector
% divided by its magnitude
disp(‵Unit vector in direction of B:’)
disp(vB/norm(vB))
disp(‵Sum A+B:’)
disp(vA+vB)
disp(‵Difference A-B:’)
disp(vA-vB)
disp(‵Dot product (A . B):’)
disp(dot(vA,vB))         % dot takes the dot product of vectors
disp(‵Cross product (A x B):’)
disp(cross(vA,vB))       % cross takes cross product of vectors
MATLAB 1.1
SUMMARY
24  CHAPTER 1  VECTOR ALGEBRA
1.1	 Tell which of the following quantities is not a vector: (a) force, (b) momentum, (c) accelera­
tion, (d) work, (e) weight.
1.2	 Which of the following is not a scalar field?
(a)  Displacement of a mosquito in space
(b)  Light intensity in a drawing room
(c)  Temperature distribution in your classroom
(d)  Atmospheric pressure in a given region
(e)  Humidity of a city
1.3	 Of the rectangular coordinate systems shown in Figure 1.13, which are not right handed?
1.4	 Which of these is correct?
(a)  A 3 A 5 0 A 0 2
(d)  ax # ay 5 az
(b)  A 3 B 1 B 3 A 5 0
(e)  ak 5 ax 2 ay , where ak is a unit vector
(c)  A # B # C 5 B # C # A
1.5	 Which of the following identities is not valid?
(a)  a1b 1 c2 5 ab 1 bc
(d)  c # 1a 3 b2 5 2b # 1a 3 c2
(b)  a 3 1b 1 c2 5 a 3 b 1 a 3 c
(e)  aA # aB 5 cos uAB
(c)  a # b 5 b # a
1.6	 Which of the following statements are meaningless?
(a)  A # B 1 2A 5 0
(c)  A1A 1 B2 1 2 5 0
(b)  A # B 1 5 5 2A
(d)  A # A 1 B # B 5 0
1.7	 Let F 5 2ax 2 6ay 1 10az and G 5 ax 1 Gyay 1 5az. If F and G have the same unit
vector, Gy is
(a)  6
(c)  0
(b)  23
(d)  6
1.8	 Given that A 5 ax 1 aay 1 az and B 5 aax 1 ay 1 az, if A and B are normal to each
other, α is
(a)  22
(d)  1
(b)  21/2
(e)  2
(c)  0
1.9	 The component of 6ax 1 2ay 2 3az along 3ax 2 4ay is
(a)  212ax 2 9ay 2 3az
(d)  2
(b)  30ax 2 40ay
(e)  10
(c)  10/7
REVIEW
QUESTIONS
Problems  25
1.10	 Given A 5 26ax 1 3ay 1 2az, the projection of A along ay is
(a)  212
(d)  7
(b)  24
(e)  12
(c)  3
Answers: 1.1d, 1.2a, 1.3b,e, 1.4b, 1.5a, 1.6a,b,c, 1.7b, 1 .8b, 1.9d, 1.10c.
Section 1.4—Unit Vector
1.1	 Determine the unit vector along the direction OP, where O is the origin and P is
point (4, 25, 1).
1.2	 Points A(4, 26, 2), B(22, 0, 3), and C(10, 1, 27) form a triangle. Show that rAB 1 rBC 1
rCA = 0.
Sections 1.5–1.7—Vector Addition, Subtraction, and Multiplication
1.3	 If A 5 4ax 2 2ay 1 6az and B 5 12ax 1 18ay 2 8az, determine:
(a)  A 2 3B
(b)  12A 1 5B2/|B|
(c)  ax 3 A
(d)  1B 3 ax2 # ay
1.4	 Let vectors A 5 10ax 2 6ay 1 8az and B 5 ax 1 2az. Find: (a) A  B, (b) A 3 B,
(c) 2A – 3B.
FIGURE 1.13  For Review Question 1.3.
PROBLEMS
26  CHAPTER 1  VECTOR ALGEBRA
1.5	 Let A 5 22ax 1 5ay 1 az, B 5 ax 1 3az, and C 5 4ax 26ay 1 10az.
(a)  Determine A 2 B 1 C
(b)  Find A  (B 3 C)
(c)  Calculate the angle between A and B
1.6	 Let A 5 ax 2 az, B 5 ax 1 ay 1 az, C 5 ay 1 2az, find:
(a)  A # 1B 3 C2
(b)  1A 3 B2 # C
(c)  A 3 1B 3 C2
(d)  1A 3 B2 3 C
1.7	 Given that the position vectors of points T and S are 4ax 1 6ay 2 az and 10ax 1 12ay 1
8az, respectively, find: (a) the coordinates of T and S, (b) the distance vector from T to
S,  (c) the distance between T and S.
1.8	 Let A 5 4ax 1 2ay 2 az and B 5 aax 1 bay 1 3az
(a)  If A and B are parallel, find a and b
(b)  If A and B are perpendicular, find a and b
1.9	 Let A 5 10ax 1 5ay 2 2az. Find: (a) A 3 ay, (b) A  az, (c) the angle between A and az.
1.10	 (a) Show that
1A # B2 2 1 |A 3 B|2 5 1AB2 2
(b)  Show that
ax 5
ay 3 az
ax # ay 3 az
,  ay 5
az 3 ax
ax # ay 3 az
,  az 5
ax 3 ay
ax # ay 3 az
1.11	 Given that
P 5 2ax 2 ay 2 2az
Q 5 4ax 1 3ay 1 2az
R 5 2ax 1 ay 1 2az
find: (a) 0 P 1 Q 2 R 0 , (b) P # Q 3 R, (c) Q 3 P # R, (d) 1P 3 Q2 # 1Q 3 R2,
(e)  1P 3 Q2 3 1Q 3 R2, (f) cos uPR, (g) sin uPQ.
1.12	 If A 5 4ax 2 6ay 1 az and B 5 2ax 1 5az , find:
(a)  A  B + 2|B|2
(b)  a unit vector perpendicular to both A and B
Problems  27
1.13	 Determine the dot product, cross product, and angle between
P 5 2ax 2 6ay 1 5az        and        Q 5 3ay 1 az
1.14	 Prove that vectors P 5 2ax 1 4ay 2 6az and Q 5 5ax 1 2ay 2 3az are orthogonal ­vectors.
1.15	 Simplify the following expressions:
(a)  A 3 1A 3 B2
(b)  A 3 3A 3 1A 3 B2 4
1.16	 A right angle triangle has its corners located at P1(5, 23, 1), P2(1, 22, 4), and P3(3, 3, 5).
(a) Which corner is a right angle? (b) Calculate the area of the triangle.
1.17  Points P, Q, and R are located at 121, 4, 82, 12, 21, 32, and 121, 2, 32, respectively.
Determine (a) the distance between P and Q, (b) the distance vector from P to R,
(c) the angle between QP and QR, (d) the area of triangle PQR, (e) the perimeter of
triangle PQR.
1.18	 Two points P12, 4, 212 and Q(12, 16, 9) form a straight line. Calculate the time taken for
a sonar signal traveling at 300 m/s to get from the origin to the midpoint of PQ.
1.19	 Find the area of the parallelogram formed by the vectors D 5 4ax 1 ay 1 5az and
E 5 2ax 1 2ay 1 3az.
*1.20	 (a)  Prove that P 5 cos u1ax 1 sin u1ay and Q 5 cos u2ax 1 sin u2ay are unit vectors in
the xy-plane, respectively, making angles u1 and u2 with the x-axis.
(b)  By means of dot product, obtain the formula for cos1u2 2 u12. By similarly formu­
lating P and Q, obtain the formula for cos1u2 1 u12.
(c)  If u is the angle between P and Q, find 1
2 0 P 2 Q 0  in terms of u.
1.21	 Consider a rigid body rotating with a constant angular velocity v radians per second
about a fixed axis through O as in Figure 1.14. Let r be the distance vector from O to P,
the position of a particle in the body. The magnitude of the velocity u of the body at P is
0 u 0 5 d 0 v 0 5  0 r 0  sin u 0 v 0  or u 5 v 3 r. If the rigid body is rotating at 3 rad/s about
an axis parallel to ax 2 2ay 1 2az and passing through point 12, 23, 12, determine the
velocity of the body at (1, 3, 4).
1.22	 A cube of side 1 m has one corner placed at the origin.  Determine the angle between the
diagonals of the cube.
1.23	 Given vectors T 5 2ax 2 6ay 1 3az and S 5 ax 1 2ay 1 az, find (a)  the scalar projection
of T on S, (b)  the vector projection of S on T, (c)  the smaller angle between T and S.
*Single asterisks indicate problems of intermediate difficulty.
28  CHAPTER 1  VECTOR ALGEBRA
FIGURE 1.14  For Problem 1.21.
Section 1.8—Components of a Vector
1.24	 Given two vectors A and B, show that the vector component of A perpendicular to B is
C 5 A 2 A # B
B # B
1.25	 Let A 5 20ax 1 15ay 2 10az and B 5 ax 1 ay. Find: (a) A  B, (b) A 3 B, (c) the compo-
nent of A along B.
1.26	 Figure 1.15 shows that A makes specific angles with respect to each axis. For
A 5 2ax 2 4ay 1 6az, find the direction angles a, b, and g.
1.27	 If H 5 2xyax 2 1x 1 z2ay 1 z2az, find:
(a)  A unit vector parallel to H at P11, 3, 222
(b)  The equation of the surface on which 0 H 0 5 10
1.28	 Let P 5 2ax 2 4ay 1 az and Q 5 ax 1 2ay. Find R which has magnitude 4 and is perpen-
dicular to both P and Q.
1.29	 Let G 5 x2ax 2 yay 1 2zaz and H 5 yzax 1 3ay 2 xzaz. At point (1, 22, 3),  (a) calculate
the magnitude of G and H,  (b) determine G  H, (c) find the angle between G and H.
1.30	 A vector field is given by H 5 10yz2ax 2 8xyzay 1 12y2az
(a)  Evaluate H at P(21, 2, 4)
(b)  Find the component of H along ax 2 ay at P.
1.31	 E and F are vector fields given by E 5 2xax 1 ay 1 yzaz and F 5 xyax 2 y2ay1 xyzaz.
Determine:
(a)  0 E 0  at (1, 2, 3)
(b)  The component of E along F at (1, 2, 3)
(c)  A vector perpendicular to both E and F at 10, 1, 232 whose magnitude is unity
1.32	 Given two vector fields
D 5 yzax 1 xzay 1 xyaz    and    E 5 5xyax 1 6(x2 1 3)ay 1 8z2az
(a)  Evaluate C 5 D 1 E at point P(21, 2, 4). (b) Find the angle C makes with the x-axis at P.
FIGURE 1.15  For Problem 1.26.
Problems  29
The Accreditation Board for Engineering and Technology (ABET) establishes eleven criteria for
accrediting engineering, technology, and computer science programs. The criteria are as follows:
A.	 Ability to apply mathematics science and engineering principles
B.	 Ability to design and conduct experiments and interpret data
C.	 Ability to design a system, component, or process to meet desired needs
D.	Ability to function on multidisciplinary teams
E.	 Ability to identify, formulate, and solve engineering problems
F.	 Ability to understand professional and ethical responsibility
G.	Ability to communicate effectively
H.	Ability to understand the impact of engineering solutions in a global context
I.	 Ability to recognize the need for and to engage in lifelong learning
J.	 Ability to know of contemporary issues
K.	 Ability to use the techniques, skills, and modern engineering tools necessary for
engineering practice
Criterion A applies directly to electromagnetics. As students, you are expected to study math­
ematics, science, and engineering with the purpose of being able to apply that knowledge to the
solution of engineering problems. The skill needed here is the ability to apply the fundamentals of
EM in solving a problem.  The best approach is to attempt as many problems as you can. This will
help you to understand how to use formulas and assimilate the material.  Keep nearly all your basic
mathematics, science, and engineering textbooks. You may need to consult them from time to time.
ENHANCING YOUR SKILLS AND CAREER

# Sadiku《Elements of Electromagnetics》Chapter 2

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 58-85 of 926 (926 total)

---

## Coordinate Systems

C H A P T E R
2.1  INTRODUCTION
In general, the physical quantities we shall be dealing with in EM are functions of space
and time. In order to describe the spatial variations of the quantities, we must be able to
­define all points uniquely in space in a suitable manner. This requires using an appropriate
coordinate system.
A point or vector can be represented in any curvilinear coordinate system, which may
be orthogonal or nonorthogonal.
An orthogonal system is one in which the coordinate surfaces are mutually perpendicular.
Nonorthogonal systems are hard to work with, and they are of little or no practical use.
Examples of orthogonal coordinate systems include the Cartesian (or rectangular), the cir­
cular cylindrical, the spherical, the elliptic cylindrical, the parabolic cylindrical, the conical,
the prolate spheroidal, the oblate spheroidal, and the ellipsoidal.1 A considerable amount of
work and time may be saved by choosing a coordinate system that best fits a given problem.
A hard problem in one coordinate system may turn out to be easy in another system.
In this text, we shall restrict ourselves to the three best-known coordinate systems:
the Cartesian, the circular cylindrical, and the spherical. Although we have considered the
Cartesian system in Chapter 1, we shall consider it in detail in this chapter. We should bear
in mind that the concepts covered in Chapter 1 and demonstrated in Cartesian coordinates
are equally applicable to other systems of coordinates. For example, the procedure for find­
ing the dot or cross product of two vectors in a cylindrical system is the same as that used
in the Cartesian system in Chapter 1.
COORDINATE SYSTEMS
AND TRANSFORMATION
History teaches us that man learns nothing from history.
—HEGEL
1For an introductory treatment of these coordinate systems, see M. R. Spiegel and J. Liu, Mathematical Handbook
of Formulas and Tables. New York: McGraw-Hill, 2nd ed., 1999, pp. 126–130.
32  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
Sometimes, it is necessary to transform points and vectors from one coordinate
system to another. The techniques for doing this will be presented and illustrated with
examples.
2.2  CARTESIAN COORDINATES (x, y, z)
2.3  CIRCULAR CYLINDRICAL COORDINATES (r, f, z)
As mentioned in Chapter 1, a point P can be represented as 1x, y, z2 as illustrated in
Figure 1.1. The ranges of the coordinate variables x, y, and z are
2` , x , `
2` , y , `
(2.1)
2` , z , `
A vector A in Cartesian (otherwise known as rectangular) coordinates can be written as
1Ax, Ay, Az2  or  Axax 1 Ayay 1 Azaz
(2.2)
where ax, ay, and az are unit vectors along the x-, y-, and z-directions as shown in Figure 1.1.
The coordinate system may be either right-handed or left-handed. See Figure 1.13. It is cus­
tomary to use the right-handed system.
The circular cylindrical coordinate system is very convenient whenever we are dealing with
problems having cylindrical symmetry, such as dealing with a coaxial transmission line.
A point P in cylindrical coordinates is represented as 1r, f, z2 and is as shown in
­Figure 2.1. Observe Figure 2.1 closely and note how we define each space variable: r is the
FIGURE 2.1  Point P and unit vectors in the
cylindrical coordinate system.
2.3 Circular Cylindrical Coordinates (r, , z)  33
radius of the cylinder passing through P or the radial distance from the z-axis; f, called the
azimuthal angle, is measured from the x-axis in the xy-plane; and z is the same as in the
Cartesian system. The ranges of the variables are
0 # r , `
0 # f , 2p
(2.3)
2` ,  z , `
A vector A in cylindrical coordinates can be written as
1Ar, Af, Az2  or  Arar 1 Afaf 1 Azaz
(2.4)
where ar, af, and az are unit vectors in the r-, f-, and z-directions as illustrated in
Figure 2.1. Note that af is not in degrees; it assumes the units of A. For example, if a
force of 10 N acts on a particle in a circular motion, the force may be represented as
F 5 10af N. In this case, af is in newtons.
The magnitude of A is
0 A 0 5 1Ar
2 1 Af
2 1 Az
22 1/2 
(2.5)
Notice that the unit vectors ar, af, and az are mutually perpendicular because our coor­
dinate system is orthogonal; ar points in the direction of increasing r, af in the direction
of increasing f, and az in the positive z-direction. Thus,
ar # ar 5 af # af 5 az # az 5 1
(2.6a)
ar # af 5 af # az 5 az # ar 5 0
(2.6b)
ar 3 af 5 az
(2.6c)
af 3 az 5 ar
(2.6d)
az 3 ar 5 af
(2.6e)
where eqs. (2.6c) to (2.6e) are obtained in cyclic permutation (see Figure 1.9). They also show
that the system is right-handed, following the cyclic ordering r S  f S  z S r S f S . . . .
The relationships between the variables 1x, y, z2 of the Cartesian coordinate system
and those of the cylindrical system 1r, f, z2 are easily obtained from Figure 2.2 as
r 5 "x2 1 y2,  f 5 tan21
x,  z 5 z
(2.7)
x 5 r cos f,  y 5 r sin f,  z 5 z
(2.8)
Whereas eq. (2.7) is for transforming a point from Cartesian 1x, y, z2 to cylindrical
1r, f, z2 coordinates, eq. (2.8) is for 1r, f, z2 S  1x, y, z2 transformation.
34  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
The relationships between 1ax, ay, az2 and 1ar, af, az2 are obtained geometrically from
Figure 2.3:
ax 5 cos f ar 2 sin f af
ay 5 sin f ar 1 cos f af
(2.9)
az 5 az
ar 5 cos f ax 1 sin f ay
af 5 2sin f ax 1 cos f ay
(2.10)
az 5 az
Finally, the relationships between 1Ax, Ay, Az2 and 1Ar, Af, Az2 are obtained by simply
substituting eq. (2.9) into eq. (2.2) and collecting terms. Thus,
FIGURE 2.2  Relationship between (x, y, z) and
(r, f, z).
FIGURE 2.3  Unit vector transformation: (a) cylindrical components of ax,
(b) cylindrical components of ay.
2.4 Spherical Coordinates (r, , )  35
A 5 1Ax cos f 1 Ay sin f2ar 1 12Ax sin f 1 Ay cos f2af 1 Azaz
(2.11)
Ar 5 Ax cos f 1 Ay sin f
Af 5 2Ax sin f 1 Ay cos f
(2.12)
Az 5 Az
In matrix form, we write the transformation of vector A from 1Ax, Ay, Az2 to
1Ar, Af, Az2 as
§ 5 £
cos f
sin f
2sin f
cos f
§ £
§ 
(2.13)
The inverse of the transformation 1Ar, Af, Az2 S  1Ax, Ay, Az2 is obtained as
§ 5 £
cos f
sin f
2sin f
cos f
§ 
(2.14)
or directly from eqs. (2.4) and (2.10). Thus,
§ 5 £
cos f
2sin f
sin f
cos f
§ £
§ 
(2.15)
An alternative way of obtaining eq. (2.13) or (2.15) is by using the dot product. For
example,
§ 5 £
ax # ar
ax # af
ax # az
ay # ar
ay # af
ay # az
az # ar
az # af
az # az
§ £
§ 
(2.16)
The derivation of this is left as an exercise.
Keep in mind that eqs. (2.7) and (2.8) are for point-to-point transformation, while eqs.
(2.13) and (2.15) are for vector-to-vector transformation.
2.4  SPHERICAL COORDINATES (r, , f)
Although cylindrical coordinates are covered in calculus texts, the spherical coordinates
are rarely covered. The spherical coordinate system is most appropriate when one is deal­
ing with problems having a degree of spherical symmetry. A point P can be represented
36  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
as 1r, u, f2 and is illustrated in Figure 2.4. From Figure 2.4, we notice that r is defined as
the distance from the origin to point P or the radius of a sphere centered at the origin and
passing through P;  (called the colatitude) is the angle between the z-axis and the position
vector of P; and f is measured from the x-axis (the same azimuthal angle in cylindrical
coordinates). According to these definitions, the ranges of the variables are
0 # r , `
0 # u # p 
(2.17)
0 # f , 2p
A vector A in spherical coordinates may be written as
1Ar, Au, Af2  or  Arar 1 Auau 1 Afaf
(2.18)
where ar, a, and af are unit vectors along the r-, -, and f-directions. The magnitude of
A is
0 A 0 5 1Ar
2 1 Au
2 1 Af
2 2 1/2
(2.19)
The unit vectors ar, a, and af are mutually orthogonal, ar being directed along the
­radius or in the direction of increasing r, a in the direction of increasing , and af in the
­direction of increasing f. Thus,
ar # ar 5 au # au 5 af # af 5 1
ar # au 5 au # af 5 af # ar 5 0
ar 3 au 5 af
(2.20)
au 3 af 5 ar
af 3 ar 5 au
FIGURE 2.4  Point P and unit
vectors in spherical coordinates.
2.4 Spherical Coordinates (r, , )  37
Equation (2.20) shows that the coordinate system is orthogonal and right-handed.
The space variables 1x, y, z2 in Cartesian coordinates can be related to variables
1r, u, f2 of a spherical coordinate system. From Figure 2.5 it is easy to notice that
r 5 "x2 1 y2 1 z2,  u 5 tan21
"x2 1 y2
,  f 5 tan21
(2.21)
x 5 r sin u cos f,  y 5 r sin u sin f,  z 5 r cos u
(2.22)
In eq. (2.21), we have 1x, y, z2 S  1r, u, f2 point transformation and in eq. (2.22), it
is 1r, u, f2 S  1x, y, z2 point transformation.
The unit vectors ax, ay, az and ar, a, af are related as follows:
ax 5 sin u cos f ar 1 cos u cos f au 2 sin f af
ay 5 sin u sin f ar 1 cos u sin f au 1 cos f af
(2.23)
az 5 cos u ar 2 sin u au
ar 5 sin u cos f ax 1 sin u sin f ay 1 cos u az
au 5 cos u cos f ax 1 cos u sin f ay 2 sin u az
(2.24)
af 5 2sin f ax 1 cos f ay
The components of vector A 5 1Ax, Ay, Az2 and A 5 1Ar, Au, Af2 are related by ­substituting
eq. (2.23) into eq. (2.2) and collecting terms. Thus,
FIGURE 2.5  Relationships between space variables (x, y, z),
(r, , f), and (, f, z,).
y = ρ sin φ
x = ρ cos φ
ρ = r sin θ
z = r cos θ
P (x, y, z) = P (r, θ, φ) = P (ρ, φ, z)
38  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
A 5 1Ax sin u cos f 1 Ay sin u sin f 1 Az cos u2ar 1 1Ax cos u cos f
1 Ay cos u sin f 2 Az sin u2au 1 12Ax sin f 1 Ay cos f2af
(2.25)
and from this, we obtain
Ar 5 Ax sin u cos f 1 Ay sin u sin f 1 Az cos u
Au 5 Ax cos u cos f 1 Ay cos u sin f 2 Az sin u
(2.26)
Af 5 2Ax sin f 1 Ay cos f
In matrix form, the 1Ax, Ay, Az2 S  1Ar, Au, Af2 vector transformation is performed
according to
§ 5 £
sin u cos f
sin u sin f
cos u
cos u cos f
cos u sin f
2sin u
2sin f
cos f
§ £
§ 
(2.27)
The inverse transformation 1Ar, Au, Af2 S  1Ax, Ay, Az2 is similarly obtained, or we obtain
it from eq. (2.23). Thus,
§ 5 £
sin u cos f
cos u cos f
2sin f
sin u sin f
cos u sin f
cos f
cos u
2sin u
§ £
§ 
(2.28)
Alternatively, we may obtain eqs. (2.27) and (2.28) by using the dot product. For
example,
§ 5 £
ar # ax
ar # ay
ar # az
au # ax
au # ay
au # az
af # ax
af # ay
af # az
§ £
§ 
(2.29)
For the sake of completeness, it may be instructive to obtain the point or vector
transformation relationships between cylindrical and spherical coordinates. We shall use
Figures 2.5 and 2.6 (where f is held constant, since it is common to both systems). This
will be left as an exercise (see Problem 2.16). Note that in a point or vector transformation,
the point or vector has not changed; it is only expressed differently. Thus, for example, the
magnitude of a vector will remain the same after the transformation, and this may serve as
a way of checking the result of the transformation.
The distance between two points is usually necessary in EM theory. The distance d
­between two points with position vectors r1 and r2 is generally given by
d 5 0 r2 2 r1 0 
(2.30)
2.4 Spherical Coordinates (r, , )  39
d2 5 1x2 2 x12 2 1 1y2 2 y12 2 1 1z2 2 z12 2 1Cartesian2
(2.31)
d2 5 r2
2 1 r1
2 2 2r1r2 cos1f2 2 f12 1 1z2 2 z12 2 1cylindrical2
(2.32)
d2 5 r2
2 1 r1
2 2 2r1r2 cos u2 cos u1
2 2r1r2 sin u2 sin u1 cos1f2 2 f12 1spherical2
(2.33)
Given point P122, 6, 32 and vector A 5 yax 1 1x 1 z2ay, express P and A in cylindrical
and spherical coordinates. Evaluate A at P in the Cartesian, cylindrical, and spherical ­systems.
Solution:
At point P: x 5 22, y 5 6, z 5 3. Hence,
r 5 "x2 1 y2 5 "4 1 36 5 6.32
f 5 tan21y
x 5 tan21 6
22 5 108.43º
z 5 3
r 5 "x2 1 y2 1 z2 5 "4 1 36 1 9 5 7
u 5 tan21
"x2 1 y2
5 tan21 "40
5 64.628
Thus,
P122, 6, 32 5 P16.32, 108.438, 32 5 P17, 64.628, 108.4382
In the Cartesian system, A at P is
A 5 6ax 1 ay
FIGURE 2.6  Unit vector transformations for
­cylindrical and spherical coordinates.
EXAMPLE 2.1
40  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
For vector A, Ax 5 y, Ay 5 x 1 z, Az 5 0. Hence, in the cylindrical system
§ 5 £
cos f
sin f
2sin f
cos f
§ £
x 1 z
Ar 5 y cos f 1 1x 1 z2 sin f
Af 5 2y sin f 1 1x 1 z2 cos f
Az 5 0
But x 5 r cos f, y 5 r sin f, and substituting these yields
A 5 1Ar, Af, Az2 5 3r cos f sin f 1 1r cos f 1 z2 sin f4ar
1 32r sin2f 1 1r cos f 1 z2 cos f4af
At P
r 5 "40,  tan f 5 6
Hence,
cos f 5 22
"40
,  sin f 5
"40
A 5 c"40 # 22
"40
"40
1 a"40 # 22
"40
1 3b #
"40
d ar
1 c2"40 # 36
40 1 a"40 # 22
"40
1 3b # 22
"40
d af
5 26
"40
ar 2
"40
af 5 20.9487ar 2 6.008af
Similarly, in the spherical system
§ 5 £
sin u cos f
sin u sin f
cos u
cos u cos f
cos u sin f
2sin u
2sin f
cos f
§ £
x 1 z
Ar 5 y sin u cos f 1 1x 1 z2sin u sin f
Au 5 y cos u cos f 1 1x 1 z2cos u sin f
2.4 Spherical Coordinates (r, , )  41
A 5 2y sin  1 (x 1 z) cos 
But x 5 r sin u cos f, y 5 r sin u sin f, and z 5 r cos u. Substituting these yields
A 5 1Ar, Au, Af2
5 r3sin2 u cos f sin f 1 1sin u cos f 1 cos u2 sin u sin f4ar
1 r3sin u cos u sin f cos f 1 1sin u cos f 1 cos u2 cos u sin f4au
1 r32sin u sin2 f 1 1sin u cos f 1 cos u2 cos f4af
At P
r 5 7,  tan f 5 6
22,  tan u 5 "40
Hence,
cos f 5 22
"40
,  sin f 5
"40
,  cos u 5 3
7,  sin u 5 "40
A 5 7 # c 40
# 22
"40
"40
1 a"40
# 22
"40
1 3
7b # "40
"40
d ar
1 7 # c "40
# 3
"40
# 22
"40
1 a"40
# 22
"40
1 3
7b # 3
"40
d au
1 7 # c 2"40
# 36
40 1 a"40
# 22
"40
1 3
7b # 22
"40
d af
5 26
7  ar 2
7"40
au 2
"40
5 20.8571ar 2 0.4066au 2 6.008af
Note that 0 A 0  is the same in the three systems; that is,
0 A1x, y, z2 0 5 0 A1r, f, z2 0 5 0 A1r, u, f2 0 5 6.083
PRACTICE EXERCISE  2.1
(a)	 Convert points P11, 3, 52, T10, 24, 32, and S123, 24, 2102 from Cartesian to
cylindrical and spherical coordinates.
(b)	 Transform vector
Q 5
"x2 1 y2ax
"x2 1 y2 1 z2 2
yzaz
"x2 1 y2 1 z2
to cylindrical and spherical coordinates.
(c)	 Evaluate Q at T in the three coordinate systems.
42  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
Express the vector
B 5 10
r  ar 1 r cos u au 1 af
in Cartesian and cylindrical coordinates. Find B123, 4, 02 and B15, p/2, 222.
Solution:
Using eq. (2.28):
§ 5 £
sin u cos f
cos u cos f
2sin f
sin u sin f
cos u sin f
cos f
cos u
2sin u
§ D
r cos u
Bx 5 10
r  sin u cos f 1 r cos2 u cos f 2 sin f
By 5 10
r  sin u sin f 1 r cos2 u sin f 1 cos f
Bz 5 10
r  cos u 2 r cos u sin u
But r 5 "x2 1 y2 1 z2, u 5 tan21
"x2 1 y2
, and f 5 tan21
Hence,
sin u 5 r
r 5
"x2 1 y2
"x2 1 y2 1 z2,  cos u 5 z
r 5
"x2 1 y2 1 z2
sin f 5
r 5
"x2 1 y2,  cos f 5 x
r 5
"x2 1 y2
Answer:  (a)  P13.162, 71.56°, 52, P15.916, 32.31°, 71.56°2, T14, 270°, 32,
T15, 53.13°, 270°2, S15, 233.1°, 2102, S111.18, 153.43°, 233.1°2.
(b)  
"r2 1 z2 1cos f ar 2 sin f af 2 z sin f az2, sin u1sin u cos f 2
r cos2 u sin f2ar 1 sin u cos u1cos f 1 r sin u sin f2au 2 sin u sin f af.
(c)  0.8ax 1 2.4az, 0.8af 1 2.4az, 1.44ar 2 1.92au 1 0.8af.
EXAMPLE 2.2
2.4 Spherical Coordinates (r, , )  43
Substituting all these gives
Bx 5
10"x2 1 y2
1x2 1 y2 1 z22
"x2 1 y2 1
"x2 1 y2 1 z2
1x2 1 y2 1 z22
z2x
"x2 1 y2 2
"x2 1 y2
10x
x2 1 y2 1 z2 1
xz2
"1x2 1 y22 1x2 1 y2 1 z22
"1x2 1 y22
By 5
10"x2 1 y2
1x2 1 y2 1 z22
"x2 1 y2 1
"x2 1 y2 1 z2
x2 1 y2 1 z2 #
z2y
"x2 1 y2 1
"x2 1 y2
10y
x2 1 y2 1 z2 1
yz2
"1x2 1 y22 1x2 1 y2 1 z22
"x2 1 y2
Bz 5
10z
x2 1 y2 1 z2 2
z"x2 1 y2
"x2 1 y2 1 z2
B 5 Bx ax 1 By ay 1 Bz az
where Bx, By, and Bz are as just given.
At 123, 4, 02, x 5 23, y 5 4, and z 5 0, so
Bx 5 230
25 1 0 2 4
5 5 22
By 5 40
25 1 0 2 3
5 5 1
Bz 5 0 2 0 5 0
Thus,
B 5 22ax 1 ay
For spherical to cylindrical vector transformation (see Problem 2.16),
§ 5 £
sin u
cos u
cos u
2sin u
§ D
r cos u
Br 5 10
r  sin u 1 r cos2 u
Bf 5 1
Bz 5 10
r  cos u 2 r sin u cos u
But r 5 "r2 1 z2 and u 5 tan21 r
44  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
Thus,
sin u 5
"r2 1 z2,  cos u 5
"r2 1 z2
Br 5
10r
r2 1 z2 1 "r2 1 z2 #
r2 1 z2
Bz 5
10z
r2 1 z2 2 "r2 1 z2 #
r2 1 z2
Hence,
B 5 a
10r
r2 1 z2 1
"r2 1 z2b ar 1 af 1 a
10z
r2 1 z2 2
"r2 1 z2b az
At 15, p/2, 222, r 5 5, f 5 p/2, and z 5 22, so
B 5 a50
29 1
"29
b ar 1 af 1 a220
29 1
"29
b az
5 2.467ar 1 af 1 1.167az
Note that at 123, 4, 02,
0 B1x, y, z2 0 5 0 B1r, f, z2 0 5 0 B1r, u, f2 0 5 2.907
This may be used to check the correctness of the result whenever possible.
PRACTICE EXERCISE  2.2
Express the following vectors in Cartesian coordinates:
(a)	 A 5 rz sin f ar 1 3r cos f af 1 r cos f sin f az
(b)	 B 5 r2 ar 1 sin u af
Answer:  (a)  A 5
"x2 1 y2 3 1xyz 2 3xy2ax 1 1zy2 1 3x22ay 1 xyaz4.
(b)  B 5
"x2 1 y2 1 z2 53x1x2 1 y2 1 z22 2 y4ax 1
3y1x2 1 y2 1 z22 1 x4ay 1 z1x2 1 y2 1 z22az6.
2.5  CONSTANT-COORDINATE SURFACES
Surfaces in Cartesian, cylindrical, or spherical coordinate systems are easily generated by
keeping one of the coordinate variables constant and allowing the other two to vary. In the
2.5 Constant-Coordinate Surfaces  45
Cartesian system, if we keep x constant and allow y and z to vary, an infinite plane is gener­
ated. Thus we could have infinite planes
x 5 constant
y 5 constant
(2.34)
z 5 constant
which are perpendicular to the x-, y-, and z-axes, respectively, as shown in Figure 2.7. The
intersection of two planes is a line. For example,
x 5 constant,  y 5 constant
(2.35)
is the line RPQ parallel to the z-axis. The intersection of three planes is a point. For ­example,
x 5 constant,  y 5 constant,  z 5 constant
(2.36)
is the point P1x, y, z2. Thus we may define point P as the intersection of three orthogonal
infinite planes. If P is 11, 25, 32, then P is the intersection of planes x 5 1, y 5 25, and
z 5 3.
Orthogonal surfaces in cylindrical coordinates can likewise be generated. The
­surfaces
r 5 constant
f 5 constant
(2.37)
z 5 constant
are illustrated in Figure 2.8, where it is easy to observe that r 5 constant is a circular cylin­
der, f 5 constant is a semi-infinite plane with its edge along the z-axis, and z 5 constant
is the same infinite plane as in a Cartesian system. Where two surfaces meet is either a line
or a circle. Thus,
z 5 constant,  r 5 constant
(2.38)
FIGURE 2.7  Constant x, y, and z surfaces.
46  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
is a circle QPR of radius r, whereas z 5 constant, f 5 constant is a semi-infinite line. A
point is an intersection of the three surfaces in eq. (2.37). Thus,
r 5 2,  f 5 608,  z 5 5
(2.39)
is the point P12, 608, 52.
The orthogonal nature of the spherical coordinate system is evident by considering
the three surfaces
r 5 constant
u 5 constant
(2.40)
f 5 constant
which are shown in Figure 2.9, where we notice that r 5 constant is a sphere of radius r
with its center at the origin; u 5 constant is a circular cone with the z-axis as its axis and
the origin as its vertex; f 5 constant is the semi-infinite plane as in a cylindrical system.
A line is formed by the intersection of two surfaces. For example,
r 5 constant,  f 5 constant
(2.41)
FIGURE 2.8  Constant r, f, and z surfaces.
FIGURE 2.9  Constant r, , and f surfaces.
2.5 Constant-Coordinate Surfaces  47
is a semicircle passing through Q and P. The intersection of three surfaces gives a point.
Thus,
r 5 5,  u 5 308,  f 5 608
(2.42)
is the point P15, 30°, 60°2. We notice that in general, a point in three-dimensional space can be
identified as the intersection of three mutually orthogonal surfaces. Also, a unit normal vector
to the surface n 5 constant is 6an, where n is x, y, z, r, f, r, or . For example, to the plane
x 5 5, a unit normal vector is 6ax and to the plane f 5 20°, a unit normal vector is af.
Two uniform vector fields are given by E 5 25ar 1 10af 1 3az and F 5 ar1
2af 2 6az. Calculate
(a)  0 E 3 F 0
(b)  The vector component of E at P15, p/2, 32 parallel to the line x 5 2, z 5 3
(c)  The angle that E makes with the surface z 5 3 at P
Solution:
(a)	 E 3 F 5 †
5 1260 2 62ar 1 13 2 302af 1 1210 2 102az
5 1266, 227, 2202
0 E 3 F 0 5 "662 1 272 1 202 5 74.06
(b)  Line x 5 2, z 5 3 is parallel to the y-axis, so the component of E parallel to the given
line is
1E # ay2ay
But at P15, p/2, 32
ay 5 sin f ar 1 cos f af
5 sin p/2 ar 1 cos p/2 af 5 ar
Therefore,
1E # ay2ay 5 1E # ar2ar 5 25ar  1or 25ay2
(c)	 Since the z-axis is normal to the surface z 5 3, we can use the dot product to find the
angle between the z-axis and E, as shown in Figure 2.10:
E # az 5 0 E 0 112 cos uEz S  3 5 "134 cos uEz
cos uEz 5
"134
5 0.2592 S  uEz 5 74.98°
EXAMPLE 2.3
48  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
Hence, the angle between z 5 3 and E is
908 2 uEz 5 15.028
Given a vector field
D 5 r sin f ar 2 1
r sin u cos f au 1 r2af
determine
(a)  D at P110, 1508, 33082
(b)  The component of D tangential to the spherical surface r 5 10 at P
(c)  A unit vector at P perpendicular to D and tangential to the cone u 5 1508
FIGURE 2.10  For Example 2.3(c).
PRACTICE EXERCISE  2.3
Given the vector field
H 5 rz cos f ar 1 e22 sin f
2 af 1 r2az
at point 11, p/3, 02, find
(a)	 H # ax
(b)	 H 3 au
(c)	 The vector component of H normal to surface r 5 1
(d)	 The scalar component of H tangential to the plane z 5 0
Answer:  (a) 20.0586,  (b) 20.06767 ar,  (c) 0 ar,  (d) 0.06767.
EXAMPLE 2.4
2.5 Constant-Coordinate Surfaces  49
Solution:
(a)	 At P, r 5 10, u 5 1508, and f 5 3308. Hence,
D 5 10 sin 3308 ar 2 1
10 sin 1508 cos 3308 au 1 100 af 5 125, 20.043, 1002
(b)  Any vector D can always be resolved into two orthogonal components:
D 5 Dt 1 Dn
where Dt is tangential to a given surface and Dn is normal to it. In our case, since ar is
­normal to the surface r  10,
Dn 5 r sin f ar 5 25ar
Hence,
Dt 5 D 2 Dn 5 20.043au 1 100af
(c)  A vector at P perpendicular to D and tangential to the cone u 5 1508 is the same as the
A unit vector along this is
a 5
2100ar 2 5af
1002 1 52 5 20.9988ar 2 0.0499af
PRACTICE EXERCISE  2.4
If A 5 3ar 1 2au 2 6af and B 5 4ar 1 3af, determine
(a)	 A # B
(b)	 0 A 3 B 0
(c)	 The vector component of A along az at 11, p/3, 5p/42
Answer:  (a) 26,  (b) 34.48,  (c) 20.116ar 1 0.201au.
vector perpendicular to both D and au. Hence,
D 3 au 5 †
0.043 100
5 2100ar 2 5af
50  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
% This script allows the user to input a coordinate in either
% rectangular, cylindrical, or spherical coordinates and
% retrieve the answer in the other coordinate systems
clear
% prompt the user for the coordinate system
disp(‘Enter the coordinate system of the input coordinate’);
coord_sys = input(‘ (r, c, or s)... \n >  ‘,’s’);
% if user entered something other than “r” “c” or “s”
% set default as “r”
if isempty(coord_sys); coord_sys = ‘r’; end
if coord_sys == ‘r’;
% prompt the user for the coordinate
disp(‘Enter the rectangular coordinate in the ‘);
crd = input(‘format [x y z]... \n >  ‘);
% check input to see if empty and set to 0 if so
if isempty(crd); crd = [0 0 0]; end
disp(‘Cylindrical coordinates [rho phi(rad) z]:’)
% display the result... the [ ] and enclose a
% three-dimensional vector
disp([sqrt(crd(1)^2+crd(2)^2) atan2(crd(2),crd(1)) crd(3)])
disp(‘Spherical coordinates [r phi(rad) theta(rad]:’)
disp([norm(crd) atan2(crd(2),crd(1)) acos(crd(3)/
norm(crd))])
elseif coord_sys == ‘c’;   % if not r but c execute this block
disp(‘Enter the cylindrical coordinate in the format’);
crd = input(‘ [\rho \phi z]... \n >  ‘);
% check input to see if empty and set to 0 if so
if isempty(crd); crd = [0 0 0]; end
disp(‘Rectangular coordinates [x y z]:’)
disp([crd(1)*cos(crd(2)) crd(1)*sin(crd(2)) crd(3)])
disp(‘Spherical coordinates [r phi(rad) theta(rad]:’)
disp([sqrt(crd(1)^2+crd(3)^2) crd(2) crd(3)*cos(crd(3))])
else coord_sys == ‘s’;  % if not r nor c but s execute this block
disp(‘Enter the spherical coordinate in the’);
crd = input(‘format [\rho \phi \theta]... \n >  ‘);
if isempty(crd); crd = [0 0 0]; end
disp(‘Rectangular coordinates [x y z]:’)
disp([crd(1)*cos(crd(2))*sin(crd(3)) ...
crd(1)*sin(crd(2))*sin(crd(3)) crd(1)*cos(crd(3))])
disp(‘Cylindrical coordinates [r phi(rad) theta(rad]:’)
disp([crd(1)*sin(crd(3)) crd(2) crd(1)*cos(crd(3))])
end
MATLAB 2.1
% This script allows the user to input a non-variable vector
% in rectangular coordinates and obtain the cylindrical, or
% spherical components. The user must also enter the point
% location where this transformation occurs; the result
MATLAB 2.1
Summary  51
1.	 The three common coordinate systems we shall use throughout the text are the
­Cartesian (or rectangular), the circular cylindrical, and the spherical.
2.	 A point P is represented as P1x, y, z2, P1r, f, z2, and P1r, u, f2 in the Cartesian, cylin­
drical, and spherical systems, respectively. A vector field A is represented as 1Ax, Ay, Az2
or Axax 1 Ayay 1 Azaz in the Cartesian system, as 1Ar, Af, Az2 or Arar 1 Afaf 1 Azaz
in the cylindrical system, and as 1Ar, Au, Af2 or Arar 1 Auau 1 Afaf in the spherical
system. It is preferable that mathematical operations (addition, subtraction, product,
etc.) be performed in the same coordinate system. Thus, point and vector transforma­
tions should be performed whenever necessary. A summary of point and vector trans­
formations is given in Table 2.1.
3.	 Fixing one space variable defines a surface; fixing two defines a line; fixing three defines
a point.
4.	 A unit normal vector to surface n 5 constant is 6an.
% depends on the vector’s observation point
clear
% prompt the user for the vectors and check to see if entered
% properly, else set to 0
disp(‘Enter the rectangular vector (in the ‘);
v = input(‘ format [x y z])... \n >  ‘);
if isempty(v); v = [0 0 0]; end
disp(‘Enter the location of the vector (in the ‘);
p = input(‘ format [x y z])... \n >  ‘);
if isempty(p); p = [0 0 0]; end
disp(‘Cylindrical components [rho phi(rad) z]:’)
phi = atan2(p(2),p(1));
% Create the transformation matrix
cyl_p=[cos(phi) sin(phi) 0; ...  % The ellipses allow a single
% command over multiple lines
-sin(phi) cos(phi) 0; ...
0 0 1];
disp((cyl_p*v’)’)   % the ’  denotes a transpose from a row
% vector to a column vector
% The second transpose converts the column
% vector back to a row vector
disp(‘Spherical components [r phi(rad) theta(rad]:’)
phi = atan2(p(3),sqrt(p(1)^2+p(2)^2));
theta = atan2(p(2),p(1));
% Create the transformation matrix
sph_p=[sin(theta)*cos(phi) sin(theta)*sin(phi) cos(theta); ...
cos(theta)*cos(phi) cos(theta)*sin(phi) -sin(theta);...
-sin(phi) cos(phi) 0];
disp((sph_p*v’)’)
SUMMARY
52  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
2.1	 The ranges of  and f as given by eq. (2.17) are not the only possible ones. The following
are all alternative ranges of  and f, except
(a)  0 # u , 2p, 0 # f # p
(b)  0 # u , 2p, 0 # f , 2p
(c)  2p # u # p, 0 # f # p
(d)  2p/2 # u # p/2, 0 # f , 2p
(e)  0 # u # p, 2p # f , p
(f)  2p # u , p, 2p # f , p
REVIEW
QUESTIONS
TABLE 2.1  Relationships between Rectangular, Cylindrical, and Spherical Coordinates
Rectangular to Cylindrical
Cylindrical to Rectangular
Rectangular to Spherical
Spherical to Rectangular
Variable
change
Variable
change
Component
change
Variable
change
Component
change
x 5 r cos f
y 5 r sin f
z 5 z
Ap 5 Ax cos f 1 Ay sin f
Af 5 2Ax sin f 1 Ay cos f
Az 5 Az
Variable
change
r 5 #x2 1 y2
f 5 tan21a
z 5 z
sin f 5
#x2 1 y2
cos f 5
#x2 1 y2
Component
change
Ax 5 Ar
#x2 1 y2 2 Af
#x2 1 y2
Ay 5 Ar
#x2 1 y2 1 Af
#x2 1 y2
Az 5 Az
Component
change
Ax 5
Arx
#x2 1 y2 1 z2 1
Auxz
#1x2 1 y22 1x2 1 y2 1 z22
Afy
#x2 1 y2
Ay 5
Ary
#x2 1 y2 1 z2 1
Auyz
#1x2 1 y22 1x2 1 y2 1 z22
Afx
#x2 1 y2
Az 5
Arz
#x2 1 y2 1 z2 2
Au#x2 1 y2
#x2 1 y2 1 z2
r 5 #x2 1 y2 1 z2
u 5 cos21
#x2 1 y2 1 z2 e
cos u 5
#x2 1 y2 1 z2
sin u 5
#x2 1 y2
#x2 1 y2 1 z2
x 5 r sin u cos f
y 5 r sin u sin f
z 5 r cos u
f 5 tan21a
xb d
cos f 5
#x2 1 y2
sin f 5
#x2 1 y2
Ar 5 Ax sin u cos f 1 Ay sin u sin f
1 Az cos u
Au 5 Ax cos u cos f 1 Ay cos u sin f
2 Az sin u
Af5 2Ax sin f 1 Ay cos f
Adopted with permission from G. F. Miner, Lines and Electromagnetic Fields for Engineers. New York: Oxford Univ. Press, 1996, p. 263.
Review Questions  53
2.2	 At Cartesian point 123, 4, 212, which of these is incorrect?
(a)  r 5 25
(c)  u 5 tan21 5
(b)  r 5 !26
(d)  f 5 tan21 4
2.3	 Which of these is not valid at point 10, 4, 02?
(a)  af 5 2ax
(c)  ar 5 4ay
(b)  au 5 2az
(d)  ar 5 ay
2.4	 A unit normal vector to the cone u 5 308 is:
(a)  ar
(c)  af
(b)  a
(d)  none of these
2.5	 At every point in space, af # au 5 1.
(a)  True
(b)  False
2.6	 If H 5 4ar 2 3af 1 5az, at 11, p/2, 02 the component of H parallel to surface
r 5 1 is
(a)  4ar
(d)  23af 1 5az
(b)  5az
(e)  5af 1 3az
(c)  23af
2.7	 Given G 5 20ar 1 50au 1 40af, at 11, p/2, p/62 the component of G perpendicular to
surface u 5 p/2 is
(a)  20ar
(d)  20ar 1 40au
(b)  50a
(e)  240ar 1 20af
(c)  40af
2.8	 Where surfaces r 5 2 and z 5 1 intersect is
(a)  an infinite plane
(d)  a cylinder
(b)  a semi-infinite plane
(e)  a cone
(c)  a circle
2.9	 Match the items in the list at the left with those in the list at the right. Each answer can be
used once, more than once, or not at all.
(a)  u 5 p/4
(i)       infinite plane
(b)  f 5 2p/3
(ii)     semi-infinite plane
(c)  x 5 210
(iii)    circle
(d)  r 5 1, u 5 p/3, f 5 p/2
(iv)     semicircle
(e)  r 5 5
(v)      straight line
(f)  r 5 3, f 5 5p/3
(vi)     cone
(g)  r 5 10, z 5 1
(vii)    cylinder
54  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
(h)  r 5 4, f 5 p/6
(viii)  sphere
(i)  r 5 5, u 5 p/3
(ix)    cube
(x)     point
2.10	A wedge is described by z 5 0, 308 , f , 608. Which of the following is
incorrect?
(a)  The wedge lies in the xy-plane.
(b)  It is infinitely long.
(c)  On the wedge, 0 , r , `.
(d)  A unit normal to the wedge is 6az.
(e)  The wedge includes neither the x-axis nor the y-axis.
Answers: 2.1b,f, 2.2a, 2.3c, 2.4b, 2.5b, 2.6d, 2.7b, 2.8c, 2.9a-(vi), b-(ii), c-(i), d-(x), e-(vii), f-(v),
g-(iii), h-(iv), i-(iii), 2.10b.
Sections 2.3 and 2.4—Cylindrical and Spherical Coordinates
2.1	 Convert the following Cartesian points to cylindrical and spherical coordinates:
(a)  P12, 5, 12
(b)  Q123, 4, 02
(c)  R16, 2, 242
2.2	 Express the following points in Cartesian coordinates:
(a)  P112, 308, 52
(b)  P211, 908, 232
(c)  P3110, p/4, p/32
(d)  P414, 308, 6082
2.3	 The rectangular coordinates at point P are (x 5 2, y 5 6, z 5 24). (a) What are its
­cylindrical coordinates? (b) What are its spherical coordinates?
2.4	 The cylindrical coordinates of point Q are r 5 5,  5 120°, z 5 1. Express Q as ­rectangular
and spherical coordinates.
2.5	 Given point T(10, 60, 30) in spherical coordinates, express T in Cartesian and cylindrical
coordinates.
2.6	 (a)	 If V 5 xz 2 xy 1 yz, express V in cylindrical coordinates.
(b)  If U 5 x2 1 2y2 1 3z2, express U in spherical coordinates.
2.7	 Convert the following vectors to cylindrical and spherical systems:
(a)  F 5
xax 1 yay 1 4az
"x2 1 y2 1 z2
PROBLEMS
Problems  55
(b)  G 5 1x2 1 y22 c
xax
"x2 1 y2 1 z2 1
yay
"x2 1 y2 1 z2 1
zaz
"x2 1 y2 1 z2d
2.8	 Let B 5 "x2 1 y2 ax 1
"x2 1 y2 ay 1 zaz . Transform B to cylindrical coordinates.
2.9	 Given vector A 5 2ar 1 3a 1 4az, convert A into Cartesian coordinates at point
(2, /2, 21).
2.10	 Express the following vectors in rectangular coordinates:
(a)  A 5 r sin f ar 1 r cos f af 2 2z az
(b)  B 5 4r cos f ar 1 r au
2.11	  Given the vector field F 5 4ar
r2 , express F in rectangular coordinates.
2.12	 If B 5 r sin ar 2 r2 cos faf, (a) find B at (2, p/2, 3p/2), (b) convert B to Cartersian coordi­
nates.
2.13	 Let B 5 xaz. Express B in
(a)  cylindrical coordinates,
(b)  spherical coordinates.
2.14	 Prove the following:
(a)  ax 3 ar 5 cos f
ax 3 af 5 2sin f
ay 3 ar 5 sin f
ay 3 af 5 cosf
(b)  ax 3 ar 5 sin u cos f
ax 3 au 5 cos u cos f
ay 3 ar 5 sin u sin f
(c)  ay 3 au 5 cos u sin f
az 3 ar 5 cos u
az 3 au 5 2sin u
2.15	 Prove the following expressions:
(a)  ar 3 af 5 az
az 3 ar 5 af
af 3 az 5 ar
(b)  ar 3 af 5 af
az 3 ar 5 au
au 3 af 5 ar
2.16	 (a)	 Show that point transformation between cylindrical and spherical coordinates is
­obtained using
r 5 "r2 1 z2,  u 5 tan21 r
z,  f 5 f
56  CHAPTER 2  COORDINATE SYSTEMS AND TRANSFORMATION
r 5 r sin u,  z 5 r cos u,  f 5 f
(b)  Show that vector transformation between cylindrical and spherical coordinates is
­obtained using
§ 5 £
sin u
cos u
cos u
2sin u
§ £
§ 5 £
sin u
cos u
cos u
2sin u
§ £
(Hint: Make use of Figures 2.5 and 2.6.)
2.17	 At point P(2,0,21), calculate the value of the following dot products:
(a)  ar ? ax, (b)af ? ay, (c)ar ? az
2.18	 Show that the vector fields
A 5 r sin  ar 1 r cos a 1 raz
B 5 r sin ar 1 r cos a 2 raz
are perpendicular to each other at any point.
2.19	 Given that A 5 3ar 1 2a 1 az and B 5 5ar 2 8az , find:
(a)  A 1 B,   (b) A  B,   (c) A 3 B,   (d) the angle between A and B.
2.20	 Given that G 5 3rar 1r cos a 2 z2az, find the component of G along ax at point
Q(3,24,6).
2.21	 Let G 5 yzax 1 xzay 1 xyaz. Transform G to cylindrical coordinates.
2.22	 The transformation 1Ar, Af, Az2 S  1Ax, Ay, Az2 in eq. (2.15) is not complete. Complete it
by expressing cos f and sin f in terms of x, y, and z. Do the same thing to the transforma­
tion 1Ar, Au, Af2 S  1Ax, Ay, Az2 in eq. (2.28).
2.23	 In Practice Exercise 2.2, express A in spherical and B in cylindrical coordinates. Evaluate
A at 110, p/2, 3p/42 and B at 12, p/6, 12.
2.24	 Calculate the distance between the following pairs of points:
(a)  12, 1, 52 and 16, 21, 22
(b)  13, p/2, 212 and 15, 3p/2, 52
(c)  110, p/4, 3p/42 and 15, p/6, 7p/42
2.25	 Calculate the distance between points P(4, 30, 0) and Q(6, 90, 180).
Problems  57
2.26	 At point (0, 4, 21), express ar and a  in Cartesian coordinates.
2.27	 Let A 5 (2z 2 sin )ar 1 (4r 1 2 cos )a 2 3rzaz and B 5 r cos ar 1 sin a 1 az.
(a)  Find the minimum angle between A and B at (1, 60, 21).
(b)  Determine a unit vector normal to both A and B at (1, 90, 0).
2.28	 Given vectors A 5 2ax 1 4ay 1 10az and B 5 25ar 1 af 2 3az, find
(a)  A 1 B at P10, 2, 252
(b)  The angle between A and B at P
(c)  The scalar component of A along B at P
2.29	 Given that B 5 r2 sin ar 1 (z 2 1) cos a 1 z2az, find B  ax at (4, p/4, 21).
2.30	 A vector field in “mixed” coordinate variables is given by
G 5 x cos f
ax 1
2yz
r2  ay 1 a1 2 x2
r2b az
Express G completely in the spherical system.
Section 2.5—Constant-Coordinate Surfaces
2.31	 Describe the intersection of the following surfaces:
(a)  x 5 2,
y 5 5
(b)  x 5 2,
y 5 21,  z 5 10
(c)  r 5 10,	 u 5 308
(d)  r 5 5,	 f 5 408
(e)  f 5 608,	z 5 10
(f)  r 5 5,
f 5 908
2.32	 If J 5 r sin u cos f ar 2 cos 2u sin f au 1 tan u
2 ln r af at T12, p/2, 3p/22, determine the
vector component of J that is:
(a)  Parallel to az
(b)  Normal to surface f 5 3p/2
(c)  Tangential to the spherical surface r 5 2
(d)  Parallel to the line y 5 22, z 5 0
2.33	 If H 5 r2 cos ar 2 r sin a, find H  ax at point P(2, 60°, 21).
2.34	 If r 5 xax 1 yay 1 zaz, describe the surface defined by:
(a)  r # ax 1 r # ay 5 5
(b)  0 r 3 az 0 5 10
George Gabriel Stokes  (1819–1903), mathematician and physicist, was one
of Ireland’s preeminent scientists of all time. He made significant ­contributions
to the fields of fluid dynamics, optics, and mathematical physics.
Born in Sligo, Ireland, as the youngest son of the Reverend Gabriel
Stokes, George Stokes was a religious man. In one of his books, he detailed
his view of God and his relationship to the world.
Although Stokes’s basic field was physics, his most important contribu­
tion was in fluid mechanics, where he described the motion of viscous fluids.
These equations are known today as the Navier–Stokes equations and are
considered fundamental equations. Stokes was an applied mathematician working in physics, and like
many of his predecessors, he branched out into other areas while continuing to develop his own spe­
cialty. His mathematical and physical papers were published in five volumes. Several discoveries were
named for him. For example, the Stokes’s theorem, to be discussed in this chapter, ­reduced selected
surface integrals to line integrals.
Carl Friedrich Gauss (1777–1855), German mathematician, astronomer,
and physicist, is considered to be one of the leading mathematicians of all
time because of his wide range of contributions.
Born in Brunswick, Germany, as the only son of uneducated parents,
Gauss was a prodigy of astounding depth. Gauss taught himself reading
and arithmetic by the age of 3. Recognizing the youth’s talent, the Duke of
Brunswick in 1792 provided him with a stipend to allow him to pursue his
education. Before his 25th birthday, he was already famous for his work
in mathematics and astronomy. At the age of 30 he went to Göttingen to
become director of the observatory. From there, he worked for 47 years until his death at almost age 78.
He found no fellow mathematical collaborators and worked alone for most of his life, engaging in an
amazingly rich scientific activity. He carried on intensive empirical and theoretical research in many
branches of science, including observational astronomy, celestial mechanics, surveying, geodesy,
capillarity, geomagnetism, electromagnetism, actuarial science, and optics. In 1833 he constructed
the first telegraph. He published over 150 works and did important work in almost every area of
mathematics. For this reason, he is sometimes called the “prince of mathematics.” Among the discov­
eries of C. F. Gauss are the method of least squares, Gaussian ­distribution, Gaussian quadrature, the
­divergence theorem (to be discussed in this chapter), Gauss’s law (to be discussed in ­Chapter 4), the
Gauss–Markov theorem, and Gauss–Jordan elimination. Gauss was deeply religious and conserva­
tive. He dominated the mathematical community during and after his lifetime.

# Sadiku《Elements of Electromagnetics》Chapter 3

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 86-135 of 926 (926 total)

---

## Vector Calculus

C H A P T E R
3.1  INTRODUCTION
Chapter 1 has focused mainly on vector addition, subtraction, and multiplication in
Cartesian coordinates, and Chapter 2 extended all these to other coordinate systems. This
chapter deals with vector calculus—integration and differentiation of vectors.
The concepts introduced in this chapter provide a convenient language for expressing
certain fundamental ideas in electromagnetics or mathematics in general. A student may
feel uneasy about these concepts at first—not seeing what they are “good for.” Such a stu­
dent is advised to concentrate simply on learning the mathematical techniques and to wait
for their applications in subsequent chapters.
VECTOR CALCULUS
This nation was founded by men of many nations and background. It was founded
on the principle that all men are created equal, and that the rights of every man are
diminished when the rights of one man are threatened.
—JOHN F. KENNEDY
3.2  DIFFERENTIAL LENGTH, AREA, AND VOLUME
Differential elements in length, area, and volume are useful in vector calculus. They are
defined in the Cartesian, cylindrical, and spherical coordinate systems.
A.  Cartesian Coordinate Systems
From Figure 3.1, we notice that the differential displacement dl at point S is the vector from
point S(x, y, z) to point B(x  dx, y  dy, z  dz).
60  CHAPTER 3  VECTOR CALCULUS
FIGURE 3.1  Differential elements in the
right-handed Cartesian coordinate system.
FIGURE 3.2  Differential normal surface areas in Cartesian coordinates:
(a) dS 5 dy dz ax, (b) dS 5 dx dz ay, (c) dS 5 dx dy az.
2.	 Differential normal surface area is given by
dS 5 dy dz ax
dx dz ay
dx dy az
(3.2)
and illustrated in Figure 3.2.
1.	 Differential displacement is given by
dl 5 dx ax 1 dy ay 1 dz az
(3.1)
3.	 Differential volume is given by
dv 5 dx dy dz
(3.3)
﻿ ﻿  61
3.2 Differential Length, Area, and Volume  61
These differential elements are very important as they will be referred to throughout
the book. The student is encouraged not to memorize them, but to learn how to derive
them from Figures 3.1 and 3.2. Notice from eqs. (3.1) to (3.3) that dl and dS are vectors,
whereas dv is a scalar. Observe from Figure 3.1 that if we move from point P to Q (or Q to
P), for example, dl 5 dy ay because we are moving in the y-direction, and if we move from
Q to S (or S to Q), dl 5 dy ay 1 dz az because we have to move dy along y, dz along z, and
dx 5 0 (no movement along x). Similarly, to move from D to Q (or Q to D) would mean
that dl 5 dx ax 1 dy ay 1 dz az.
The way dS is defined is important. The differential surface (or area) element dS may
generally be defined as
dS 5 dS an
(3.4)
where dS is the area of the surface element and an is a unit vector normal to the surface
dS (and directed away from the volume if dS is part of the surface describing a volume). If
we consider surface ABCD in Figure 3.1, for example, dS 5 dy dz ax, whereas for surface
PQRS, dS 5 2dy dz ax because an 5 2ax is normal to PQRS.
What we have to remember at all times about differential elements is dl and how to get
dS and dv from it. When dl is remembered, dS and dv can easily be found. For example, dS
along ax can be obtained from dl in eq. (3.1) by multiplying the components of dl along ay
and az; that is, dy dz ax. Similarly, dS along az is the product of the components of dl along
components of dl, that is, dx dy dz. The idea developed here for Cartesian coordinates will
now be extended to other coordinate systems.
B.  Cylindrical Coordinate Systems
From Figure 3.3, the differential elements in cylindrical coordinates can be found as
­follows:
1.	 Differential displacement is given by
dl 5 dr ar 1 r df af 1 dz az
(3.5)
2.	 Differential normal surface area is given by
dS 5 r df dz ar
dr dz af
r dr df az
(3.6)
and illustrated in Figure 3.4.
3.	 Differential volume is given by
dv 5 r dr df dz
(3.7)
a  and a ; that is, dx dy a . Also, dv can be obtained from dl as the product of the three
62  CHAPTER 3  VECTOR CALCULUS
FIGURE 3.3  Differential elements in
cylindrical coordinates.
ρ dφ
ρ dφ
(a)
(b)
(c)
FIGURE 3.4  Differential normal surface areas in cylindrical coordinates:
(a) dS 5 r df dz ar, (b) dS 5 dr dz af, (c) dS 5 r dr df az.
As mentioned in the preceding section on Cartesian coordinates, we need only
remember dl; dS and dv can easily be obtained from dl. For example, dS along az is the
of the three components of dl, that is, dr r df dz.
C.  Spherical Coordinate Systems
From Figure 3.5, the differential elements in spherical coordinates can be found as
follows:
1.	 The differential displacement is
dl 5 dr ar 1 r du au 1 r sin u df af
(3.8)
product of the components of dl along a  and a , that is, dr r df a . Also, dv is the product
﻿ ﻿  63
3.2 Differential Length, Area, and Volume  63
2.	 The differential normal surface area is
dS 5 r2 sin u du df ar
r sin u dr df au
r dr du af
(3.9)
and illustrated in Figure 3.6.
FIGURE 3.5  Differential elements
in the spherical coordinate system.
r dθ
(a)
(b)
(c)
r sin θ dφ
r sin θ dφ
r dθ
FIGURE 3.6  Differential normal surface areas in spherical coordinates:
(a) dS 5 r2 sin  d df ar, (b) dS 5 r sin  dr df a, (c) dS 5 r dr d af.
3.	 The differential volume is
dv 5 r2 sin u dr du df
(3.10)
64  CHAPTER 3  VECTOR CALCULUS
Again, we need to remember only dl, from which dS and dv are easily obtained. For
example, dS along au is obtained as the product of the components of dl along ar and au, that is,
dr # r sin u df; dv is the product of the three components of dl, that is, dr # r du # r sin u df.
EXAMPLE 3.1
FIGURE 3.7  For Example 3.1.
Consider the object shown in Figure 3.7. Calculate
(a)  The length BC
(d)  The surface area ABO
(b)  The length CD
(e)  The surface area AOFD
(c)  The surface area ABCD
(f)  The volume ABDCFO
Solution:
Although points A, B, C, and D are given in Cartesian coordinates, it is obvious that the
­object has cylindrical symmetry. Hence, we solve the problem in cylindrical coordinates.
The points are transformed from Cartesian to cylindrical coordinates as follows:
A15, 0, 02 S  A15, 08, 02
B10, 5, 02 S  Ba5, p
2 , 0b
C10, 5, 102 S  Ca5, p
2 , 10b
D15, 0, 102 S  D15, 08, 102
(a)  Along BC, dl 5 dz; hence,
BC 5 3
dl 5 3
dz 5 10
(b)  Along CD, dl 5 r df and r 5 5, so
CD 5 3
p/2
r df 5 5 f `
p/2
5 2.5p
﻿ ﻿  65
3.2 Differential Length, Area, and Volume  65
(c)	 For ABCD, dS 5 r df dz, r 5 5. Hence,
area ABCD 5 3
dS 5 3
p/2
f50
z50
r df dz 5 5 3
p/2
df 3
dz `
r55
5 25p
(d)	 For ABO, dS 5 r df dr and z 5 0, so
area ABO 5 3
p/2
f50
r50
r df dr 5 3
p/2
df 3
r dr 5 6.25p
(e)	 For AOFD, dS 5 dr dz and f 5 0°, so
area AOFD 5 3
r50
z50
dr dz 5 50
(f)	 For volume ABDCFO, dv 5 r df dz dr. Hence,
v 5 3
dv 5 3
r50
p/2
f50
z50
r df dz dr 5 3
dz 3
p/2
df 3
r dr 5 62.5p
FIGURE 3.8  For Practice Exercise 3.1 (and also
Review Question 3.3).
r dθ
PRACTICE EXERCISE  3.1
Refer to Figure 3.8; disregard the differential lengths and imagine that the object is part
of a spherical shell. It may be described as 3 # r # 5, 60° # u # 90°, 45° # f # 60°
where surface r 5 3 is the same as AEHD, surface u 5 60° is AEFB, and surface f 5 45°
is ABCD. Calculate
(a)  The arc length DH
(d)  The surface area ABDC
(b)  The arc length FG
(e)  The volume of the object
(c)  The surface area AEHD
Answer:  (a) 0.7854,  (b) 2.618,  (c) 1.179,  (d) 4.189,  (e) 4.276.
66  CHAPTER 3  VECTOR CALCULUS
The familiar concept of integration will now be extended to cases in which the integrand
involves a vector. By “line” we mean the path along a curve in space. We shall use terms
such as line, curve, and contour interchangeably.
The line integral 3
A # dl is the integral of the tangential component of A along
curve L.
Given a vector field A and a curve L, we define the integral
A # dl 5 3
0 A 0  cos u dl
(3.11)
as the line integral of A around L (see Figure 3.9). If the path of integration is a closed curve
such as abca in Figure 3.9, eq. (3.11) becomes a closed contour integral
A # dl
(3.12)
which is called the circulation of A around L. A common example of a line integral is the
work done on a particle. In this case A is the force F and
F # d1 5 3
Fx dx 1 3
Fy dy 1 3
Fz dz
Given a vector field A, continuous in a region containing the smooth surface S, we
­define the surface integral or the flux of A through S (see Figure 3.10) as
3.3  LINE, SURFACE, AND VOLUME INTEGRALS
FIGURE 3.9  Path of integration of vector field A.
 5 3
0 A 0  cos u dS 5 3
A # an dS
﻿ ﻿  67
3.3 Line, Surface, and Volume Integrals  67
or simply
where, at any point on S, an is the unit normal to S. For a closed surface (defining a ­volume),
eq. (3.13) becomes
which is referred to as the net outward flux of A from S. Notice that a closed path defines
We define the integral
rv dv
(3.15)
as the volume integral of the scalar v over the volume v. The physical meaning of a line,
surface, or volume integral depends on the nature of the physical quantity represented by
A or v. Note that dl, dS, and dv are all as defined in Section 3.2.
FIGURE 3.10  The flux of a vector field A
through surface S.
Given that F 5 x2ax 2 xzay 2 y2az, calculate the circulation of F around the (closed) path
shown in Figure 3.11.
Solution:
The circulation of F around path L is given by
F # dl 5 a 3
1 3
1 3
1 3
b F # dl
where the path is broken into segments numbered 1 to 4 as shown in Figure 3.11.
For segment  1  , y 5 0 5 z
F 5 x2ax 2 xzay 2 y2az,  dl 5 dx ax
Notice that dl is always taken as along 1ax so that the direction on segment   1   is taken
care of by the limits of integration. Also, since dl is in the ax-direction, only the ax compo­
nent of vector F will be integrated, owing to the definition of the dot product. Thus,
EXAMPLE 3.2
 5 3
A # dS
(3.13)
 5 C
A # dS
(3.14)
an open surface, whereas a closed surface defines a volume (see Figures 3.12 and 3.17).
68  CHAPTER 3  VECTOR CALCULUS
F # dl 5 3
x2dx 5 x3
3  `
5 21
For segment   2  , x 5 0 5 z, F 5 x2ax 2 xzay 2 az, dl 5 dy ay, F # dl 5 0. Hence,
2  F # dl 5 0
For segment   3  , y 5 1, F 5 x2ax 2 xzay 2 az, and dl 5 dx ax 1 dz az, so
3 F # dl 5 3 1x2dx 2 dz2
But on   3  , z 5 x; that is, dx 5 dz. Hence,
F # dl 5 3
1x2 2 12 dx 5 x3
3 2 x `
5 22
For segment   4  , x 5 1, so F 5 ax 2 zay 2 y2az, and dl 5 dy ay 1 dz az. Hence,
4 F # dl 5 3 12z dy 2 y2dz2
But on   4  , z 5 y; that is, dz 5 dy, so
F # dl 5 3
12y 2 y22 dy 5 2
2 2
3  `
5 5
By putting all these together, we obtain
F # dl 5 21
3 1 0 2 2
3 1 5
6 5 21
FIGURE 3.11  For Example 3.2.
﻿ ﻿  69
3.4 Del Operator  69
FIGURE 3.12  For Practice Exercise 3.2, L is a closed path.
60°
PRACTICE EXERCISE  3.2
Calculate the circulation of
A 5 r cos f ar 1 z sin f az
in Figure 3.12.
Answer:  1.
The del operator, written , is the vector differential operator. In Cartesian coordinates,
= 5 '
'x ax 1 '
'y ay 1 '
'z az
(3.16)
This vector differential operator, otherwise known as the gradient operator, is not a vector in
itself, but when it operates on a scalar function, for example, a vector ensues. The operator
is useful in defining
1.	 The gradient of a scalar V, written as V
2.	 The divergence of a vector A, written as = # A
3.	 The curl of a vector A, written as = 3 A
4.	 The Laplacian of a scalar V, written as 2V
Each of these will be defined in detail in the subsequent sections. Before we do that, it
is appropriate to obtain expressions for the del operator  in cylindrical and spherical
­coordinates. This is easily done by using the transformation formulas of Sections 2.3
and 2.4.
3.4  DEL OPERATOR
around the edge L of the wedge defined by 0 # r # 2, 0 # f # 60°, z 5 0 and shown
70  CHAPTER 3  VECTOR CALCULUS
To obtain  in terms of r, f, and z, we recall from eq. (2.7) that1
r 5 "x2 1 y2,  tan f 5
Hence
'x 5 cos f '
'r 2 sin f
'f
(3.17)
'y 5 sin f '
'r 1 cos f
(3.18)
Substituting eqs. (3.17) and (3.18) into eq. (3.16) and making use of eq. (2.9), we obtain 
in cylindrical coordinates as
= 5 ar '
'r 1 af 1
r '
'f 1 az '
'z
(3.19)
Similarly, to obtain  in terms of r, , and f, we use
r 5 "x2 1 y2 1 z2,  tan u 5
"x2 1 y2
,  tan f 5
to obtain
'x 5 sin u cos f '
'r 1 cos u cos f
'u 2 sin f
'f
(3.20)
'y 5 sin u sin f '
'r 1 cos u sin f
'u 1 cos f
(3.21)
'z 5 cos u '
'r 2 sin u
(3.22)
Substituting eqs. (3.20) to (3.22) into eq. (3.16) and using eq. (2.23) results in  in spherical
coordinates:
= 5 ar '
'r 1 au 1
r '
'u 1 af
r sin u '
'f
(3.23)
Notice that in eqs. (3.19) and (3.23), the unit vectors are placed to the left of the differential
operators because the unit vectors depend on the angles.
1 A more general way of deriving , = # A, = 3 A, V, and 2V is by using the curvilinear ­coordinates.
See, for example, M. R. Spiegel, Vector Analysis and an Introduction to Tensor Analysis. New York: McGraw-Hill,
1959, pp. 135–165.
﻿ ﻿  71
3.5 Gradient of a Scalar  71
The gradient of a scalar field at any point is the maximum rate of change of the field at
that point.
The gradient of a scalar field V is a vector that represents both the magnitude and
the direction of the maximum space rate of increase of V.
A mathematical expression for the gradient can be obtained by evaluating the difference in
the field dV between points P1 and P2 of Figure 3.13, where V1, V2, and V3 are contours on
which V is constant. From calculus,
dV 5 'V
'x  dx 1 'V
'y  dy 1 'V
'z  dz
5 a'V
'x  ax 1 'V
'y  ay 1 'V
'z  azb # 1dx ax 1 dy ay 1 dz az2
(3.24)
For convenience, let
G 5 'V
'x  ax 1 'V
'y  ay 1 'V
'z  az
(3.25)
Then
dV 5 G # dl 5 G cos u dl
FIGURE 3.13  Gradient of a scalar.
3.5  GRADIENT OF A SCALAR
72  CHAPTER 3  VECTOR CALCULUS
dl 5 G cos u
(3.26)
where dl is the differential displacement from P1 to P2 and  is the angle between G and
dl. From eq. (3.26), we notice that dV/dl is a maximum when u 5 0, that is, when dl is in
the direction of G. Hence,
dl  `
max
5 dV
dn 5 G
(3.27)
where dV/dn is the normal derivative. Thus G has its magnitude and direction as those of
the maximum rate of change of V. By definition, G is the gradient of V. Therefore:
grad V 5 =V 5 'V
'x  ax 1 'V
'y  ay 1 'V
'z  az
(3.28)
By using eq. (3.28) in conjunction with eqs. (3.16), (3.19), and (3.23), the gradient of V can
be expressed in Cartesian, cylindrical, and spherical coordinates. For Cartesian ­coordinates
=V 5 'V
'x  ax 1 'V
'y  ay 1 'V
'z  az
for cylindrical coordinates,
=V 5 'V
'r ar 1 1
r 'V
'f af 1 'V
'z  az
(3.29)
and for spherical coordinates,
=V 5 'V
'r  ar 1 1
r 'V
'u  au 1
r sin u 'V
'f af
(3.30)
The following computation formulas on gradient, which are easily proved, should be
noted:
(i)    =1V 1 U2 5 =V 1 =U
(3.31a)
(ii)  =1VU2 5 V=U 1 U=V
(3.31b)
(iii)  =c V
Ud 5 U=V 2 V =U
(3.31c)
(iv)  =V
n 5 nV
n21 =V
(3.31d)
where U and V are scalars and n is an integer.
Also take note of the following fundamental properties of the gradient of a scalar  field V:
1.	 The magnitude of V equals the maximum rate of change in V per unit distance.
2.	 V points in the direction of the maximum rate of change in V.
﻿ ﻿  73
3.5 Gradient of a Scalar  73
3.	 V at any point is perpendicular to the constant V surface that passes through that
point (see points P and Q in Figure 3.13).
4.	 The projection (or component) of V in the direction of a unit vector a is =V # a
and is called the directional derivative of V along a. This is the rate of change of V
in the direction of a. For example, dV/dl in eq. (3.26) is the directional derivative
of V along P1P2 in Figure 3.13. Thus the gradient of a scalar function V provides us
with both the direction in which V changes most rapidly and the magnitude of the
maximum directional derivative of V.
5.	 If A 5 =V, V is said to be the scalar potential of A.
Find the gradient of the following scalar fields:
(a)  V 5 e2z sin 2x cosh y
(b)  U 5 r2z cos 2f
(c)  W 5 10r sin2 u cos f
Solution:
(a)  =V 5 'V
'x  ax 1 'V
'y  ay 1 'V
'z  az
5 2e2z cos 2x cosh y ax 1 e2z sin 2x sinh y ay 2 e2z sin 2x cosh y az
(b)  =U 5 'U
'r ar 1 1
r 'U
'f af 1 'U
'z  az
5 2rz cos 2f ar 2 2rz sin 2f af 1 r2 cos 2f az
(c)  =W 5 'W
'r  ar 1 1
r 'W
'u  au 1
r sin u 'W
'f  af
5 10 sin2 u cos f ar 1 10 sin 2u cos f au 2 10 sin u sin f af
EXAMPLE 3.3
PRACTICE EXERCISE  3.3
Determine the gradient of the following scalar fields:
(a)	 U 5 x2y 1 xyz
(b)	 V 5 rz sin f 1 z2 cos2 f 1 r2
(c)	 f 5 cos u sin f ln r 1 r2f
Answer:  (a) y12x 1 z2ax 1 x1x 1 z2ay 1 xyaz
(b) 1z sin f 1 2r2ar 1 az cos f 2 z2
r sin 2fbaf 1
1r sin f 1 2z cos2 f2az
(c) acos u sin f
1 2rfbar 2 sin u sin f
ln r au 1
acot u
cos f ln r 1 r csc ubaf
74  CHAPTER 3  VECTOR CALCULUS
Given W 5 x2y2 1 xyz, compute W and the directional derivative dW/dl in the direction
3ax 1 4ay 1 12az at 12, 21, 02.
Solution:
=W 5 'W
'x  ax 1 'W
'y  ay 1 'W
'z  az
5 12xy2 1 yz2ax 1 12x2y 1 xz2ay 1 1xy2az
At 12, 21, 02: =W 5 4ax 2 8ay 2 2az
Hence,
dl 5 =W # al 5 14, 28, 222 # 13, 4, 122
5 244
Find the angle at which line x 5 y 5 2z intersects the ellipsoid x2 1 y2 1 2z2 5 10.
Solution:
Let the line and the ellipsoid meet at angle  as shown in Figure 3.14. On line x 5 y 5 2z, for
two unit increments along z, there is a unit increment along x and a unit increment along y.
Thus, the line can be represented by
r1l2 5 2l ax 1 2l ay 1 l az
where l is a parameter. Where the line and the ellipsoid meet,
12l2 2 1 12l2 2 1 2l2 5 10 S  l 5 61
Taking l 5 1 (for the moment), the point of intersection is 1x, y, z2 5 12, 2, 12. At this
point, r 5 2ax 1 2ay 1 az.
EXAMPLE 3.4
EXAMPLE 3.5
PRACTICE EXERCISE  3.4
Given 5 xy 1 yz 1 xz, find gradient  at point 11, 2, 32 and the directional deriva­
tive of  at the same point in the direction toward point 13, 4, 42.
Answer:  5ax 1 4ay 1 3az, 7.
FIGURE 3.14  For Example 3.5; plane of intersection of a
line with an ellipsoid.
﻿ ﻿  75
3.6 Divergence of a Vector and Divergence Theorem  75
PRACTICE EXERCISE  3.5
Calculate the angle between the normals to the surfaces x2y 1 z 5 3 and
x log z 2 y2 5 24 at the point of intersection 121, 2, 12.
Answer:  73.4°.
The surface of the ellipsoid is defined by
f1x, y, z2 5 x2 1 y2 1 2z2 2 10
The gradient of f is
=f 5 2xax 1 2yay 1 4zaz
At 12, 2, 12, =f 5 4ax 1 4ay 1 4az. Hence, a unit vector normal to the ellipsoid at the
point of intersection is
an 5 6
0 =f 0 5 6
ax 1 ay 1 az
Taking the positive sign (for the moment), the angle between an and r is given by
cos u 5 an # r
0 an # r 0 5 2 1 2 1 1
"3"9
3"3
5 sin c
possible angles, given by sin c 5 65/13"32.
3.6  DIVERGENCE OF A VECTOR AND DIVERGENCE THEOREM
From Section 3.3, we have noticed that the net outflow of the flux of a vector field A from
a closed surface S is obtained from the integral A A # dS. We now define the divergence of
A as the net outward flow of flux per unit volume over a closed incremental surface.
The divergence of A at a given point P is the outward flux per unit volume as the volume
shrinks about P.
Hence,
div A 5 = # A 5
lim
DvS0
A # dS
(3.32)
Hence, c 5 74.21°. Because we had choices of 1 or 2 for l and a , there are actually four
76  CHAPTER 3  VECTOR CALCULUS
where Dv is the volume enclosed by the closed surface S in which P is located. Physically, we
may regard the divergence of the vector field A at a given point as a measure of how much the
field diverges or emanates or originates from that point. Figure 3.15(a) shows that the diver­
gence of a vector field at point P is positive because the vector diverges (or spreads out) at P.
In Figure 3.15(b) a vector field has negative divergence (or convergence) at P, and in Figure
3.15(c) a vector field has zero divergence at P. The divergence of a vector field can also be
viewed as simply the limit of the field’s source strength per unit volume (or source density);
it is positive at a source point in the field, and negative at a sink point, or zero where there is
neither sink nor source.
We can obtain an expression for = # A in Cartesian coordinates from the definition
in eq. (3.32). Suppose we wish to evaluate the divergence of a vector field A at point
P1xo, yo, zo2; we let the point be enclosed by a differential volume as in Figure 3.16. The
surface integral in eq. (3.32) is obtained from
A # dS 5 a33
front
1 33
back
1 33
left
1 33
right
1 33
top
1 33
bottom
b A # dS (3.33)
A three-dimensional Taylor series expansion of Ax about P is
Ax1x, y, z2 5 Ax1xo, yo, zo2 1 1x 2 xo2 'Ax
'x  `
1 1y 2 yo2 'Ax
'y  `
1 1z 2 zo2 'Ax
'z `
1 higher-order terms
(3.34)
For the front side, x 5 xo 1 dx/2 and dS 5 dy dz ax. Then,
front
A # dS 5 dy dz cAx1xo, yo, zo2 1 dx
2  'Ax
'x  `
d 1 higher-order terms
For the back side, x 5 xo 2 dx/2 and dS 5 dy dz12ax2. Then,
back
A # dS 5 2dy dz cAx1xo, yo, zo2 2 dx
2  'Ax
'x  `
d 1 higher-order terms
FIGURE 3.15  Illustration of the divergence of a vector field at P: (a) positive
divergence, (b) negative divergence, (c) zero divergence.
﻿ ﻿  77
3.6 Divergence of a Vector and Divergence Theorem  77
Hence,
front
A # dS 1 33
back
A # dS 5 dx dy dz 'Ax
'x  `
1 higher-order terms
(3.35)
By taking similar steps, we obtain
left
A # dS 1 33
right
A # dS 5 dx dy dz
'Ay
'y  `
1 higher-order terms
(3.36)
and
top
A # dS 1 33
bottom
A # dS 5 dx dy dz 'Az
'z  `
1 higher-order terms
(3.37)
Substituting eqs. (3.35) to (3.37) into eq. (3.33) and noting that Dv 5 dx dy dz, we get
lim
DvS0
AS A # dS
5 a'Ax
'x 1
'Ay
'y 1 'Az
'z b `
at P
(3.38)
because the higher-order terms will vanish as Dv S 0. Thus, the divergence of A at point
P1xo, yo, zo2 in a Cartesian system is given by
= # A 5 'Ax
'x 1
'Ay
'y 1 'Az
'z 
(3.39)
Similar expressions for = # A in other coordinate systems can be obtained directly
from eq. (3.32) or by transforming eq. (3.39) into the appropriate coordinate system. In
cylindrical coordinates, substituting eqs. (2.15), (3.17), and (3.18) into eq. (3.39) yields
= # A 5 1
r '
'r 1rAr2 1 1
'Af
'f 1 'Az
'z 
(3.40)
FIGURE 3.16 Evaluation of = # A at point
P(xo, yo, zo).
78  CHAPTER 3  VECTOR CALCULUS
Substituting eqs. (2.28) and (3.20) to (3.22) into eq. (3.39), we obtain the divergence of A
in spherical coordinates as
= # A 5 1
r2 '
'r 1r2Ar2 1
r sin u '
'u 1Au sin u2 1
r sin u
'Af
'f 
(3.41)
Note the following properties of the divergence of a vector field:
1.	 It produces a scalar field (because scalar product is involved).
2.	 = # 1A 1 B2 5 = # A 1 = # B
3.	 = # 1VA2 5 V= # A 1 A # =V
From the definition of the divergence of A in eq. (3.32), it is not difficult to
expect that
A # dS 5 3
= # A dv
(3.42)
This is called the divergence theorem, otherwise known as the Gauss–Otrogradsky ­theorem.
The divergence theorem states that the total outward flux of a vector field A through
the closed surface S is the same as the volume integral of the divergence of A.
To prove the divergence theorem, subdivide volume v into a large number of small
cells. If the kth cell has volume Dvk and is bounded by surface Sk
A # dS 5 a
A # dS 5 a
A # dS
Dvk
Dvk
(3.43)
Since the outward flux to one cell is inward to some neighboring cells, there is cancellation
on every interior surface, so the sum of the surface integrals over the Sk’s is the same as the
surface integral over the surface S. Taking the limit of the right-hand side of eq. (3.43) and
incorporating eq. (3.32) gives
A # dS 5 3
= # A dv
(3.44)
which is the divergence theorem. The theorem applies to any volume v bounded by the
closed surface S such as that shown in Figure 3.17 provided that A and = # A are con­
tinuous in the region. With a little experience, one comes to understand that the vol­
ume ­integral on the right-hand side of eq. (3.42) is easier to evaluate than the surface
integral(s) on the left-hand side of the equation. For this reason, to determine the flux
﻿ ﻿  79
3.6 Divergence of a Vector and Divergence Theorem  79
of A through a closed surface, we simply find the right-hand side of eq. (3.42) instead
of the left-hand side of the equation.
surface S
FIGURE 3.17  Volume v enclosed by surface S.
EXAMPLE 3.6
Determine the divergence of these vector fields:
(a)  P 5 x2yzax 1 xzaz
(b)  Q 5 r sin f ar 1 r2z af 1 z cos f az
(c)  T 5 1
r2 cos u ar 1 r sin u cos f au 1 cos u af
Solution:
(a)	 = # P 5 '
'xPx 1 '
'yPy 1 '
'zPz
5 '
'x 1x2yz2 1 '
'y 102 1 '
'z 1xz2
5 2xyz 1 x
(b)	 = # Q 5 1
r '
'r 1rQr2 1 1
r '
'f Qf 1 '
'z Qz
5 1
r '
'r 1r2 sin f2 1 1
r '
'f 1r2z2 1 '
'z 1z cos f2
5 2 sin f 1 cos f
(c)	 = # T 5 1
r2 '
'r 1r2Tr2 1
r sin u '
'u 1Tu sin u2 1
r sin u '
'f 1Tf2
5 1
r2 '
'r 1cos u2 1
r sin u '
'u 1r sin2 u cos f2 1
r sin u '
'f 1cos u2
5 0 1
r sin u 2r sin u cos u cos f 1 0
5 2 cos u cos f
80  CHAPTER 3  VECTOR CALCULUS
PRACTICE EXERCISE  3.6
Determine the divergence of the following vector fields and evaluate them at the speci­
fied points.
(a)	 A 5 yzax 1 4xyay 1 yaz at 11, 22, 32
(b)	 B 5 rz sin f ar 1 3rz2 cos f af at 15, p/2, 12
(c)	 C 5 2r cos u cos f ar 1 r1/2af at 11, p/6, p/32
Answer:  (a) 4x, 4,  (b) 12 2 3z2z sin f, 21,  (c) 6 cos u cos f, 2.598.
If G1r2 5 10e22z1rar 1 az2, determine the flux of G out of the entire surface of the cylin­
der r 5 1, 0 # z # 1. Confirm the result by using the divergence theorem.
Solution:
If  is the flux of G through the given surface, shown in Figure 3.18, then
where t, b, and s are the fluxes through the top, bottom, and sides (curved surface) of
the cylinder as in Figure 3.18.
For t, z 5 1, dS 5 r dr df az. Hence,
5 10pe22
EXAMPLE 3.7
FIGURE 3.18  For Example 3.7.
 5 C
G # dS 5 t 1 b 1 s
t 5 33G # dS 5 3
r50
f50
10e22r dr df 5 10e2212p2 r2
2 `
﻿ ﻿  81
3.6 Divergence of a Vector and Divergence Theorem  81
PRACTICE EXERCISE  3.7
Determine the flux of D 5 r2 cos2 f ar 1 z sin f af over the closed surface of the cyl­
inder 0 # z # 1, r 5 4. Verify the divergence theorem for this case.
Answer:  64p.
For b, z 5 0 and dS 5 r dr df12az2. Hence,
b 5 3
G # dS 5 3
r50
f50
10e0r dr df 5 21012p2 r2
2  `
5 210p
For s, r 5 1 and dS 5 r dz df ar. Hence,
s 5 3
G # dS 5 3
z50
f50
10e22zr2 dz df 5 10112 212p2 e22z
22  `
5 10p11 2 e222
Thus,
 5 t 1 b 1 s 5 10pe22 2 10p 1 10p11 2 e222 5 0
lternatively, since S is a closed surface, we can apply the divergence theorem:
 5 C
G # dS 5 3
1= # G2 dv
But
= # G 5 1
r '
'r 1rGr2 1 1
r '
'f Gf 1 '
'z Gz
5 1
r '
'r 1r210e22z2 2 20e22z
5 1
r120re22z2220e22z 5 0
showing that G has no outward flux. Hence,
 5 3
1= # G2 dv 5 0
82  CHAPTER 3  VECTOR CALCULUS
In Section 3.3, we defined the circulation of a vector field A around a closed path L as the
integral ALA # dl.
The curl of A is an axial (or rotational) vector whose magnitude is the maximum cir-
culation of A per unit area as the area tends to zero and whose direction is the normal
direction of the area when the area is oriented to make the circulation maximum.2
That is,
curl A 5 = 3 A 5 a lim
DSS0
AL A # dl
max
an
(3.45)
where the area DS is bounded by the curve L and an is the unit vector normal to the surface
DS and is determined by using the right-hand rule.
To obtain an expression for = 3 A from the definition in eq. (3.45), consider the dif­
ferential area in the yz-plane as in Figure 3.19. The line integral in eq. (3.45) is obtained as
A # dl 5 a3
1 3
1 3
1 3
b A # dl
(3.46)
We expand the field components in a Taylor series expansion about the center point P1xo, yo, zo2 as
in eq. (3.34) and evaluate eq. (3.46). On side ab, dl 5 dy ay and z 5 zo 2 dz/2, so
A # dl 5 dy cAy1xo, yo, zo2 2 dz
'Ay
'z  `
d 
(3.47)
On side bc, dl 5 dz az and y 5 yo 1 dy/2, so
A # dl 5 dz cAz1xo, yo, zo2 1
2  'Az
'y  `
d 
(3.48)
3.7  CURL OF A VECTOR AND STOKES’S THEOREM
2 Because of its rotational nature, some authors use rot A instead of curl A.
FIGURE 3.19 Contour used in evaluating the
x-component of   A at point P(xo, yo, zo).
﻿ ﻿  83
3.7 Curl of a Vector and Stokes’s Theorem  83
On side cd, dl 5 dy ay and z 5 zo 1 dz/2, so
A # dl 5 2dy cAy1xo, yo, zo2 1 dz
'Ay
'z  `
d 
(3.49)
On side da, dl 5 dz az and y 5 yo 2 dy/2, so
A # dl 5 2dz cAz1xo, yo, zo2 2
2  'Az
'y  `
d 
(3.50)
Substituting eqs. (3.47) to (3.50) into eq. (3.46) and noting that DS 5 dy dz, we have
lim
DSS0
A # dl
5 'Az
'y 2 'Ay
1curl A2 x 5 'Az
'y 2 'Ay
'z 
(3.51)
The y- and x-components of the curl of A can be found in the same way. We obtain
1curl A2 y 5 'Ax
'z 2 'Az
'x 
(3.52a)
1curl A2 z 5
'Ay
'x 2
'Ax
'y 
(3.52b)
The definition of = 3 A in eq. (3.45) is independent of the coordinate system. In
Cartesian coordinates the curl of A is easily found using
= 3 A 5 ∞
(3.53)
= 3 A 5 c 'Az
'y 2
'Ay
'z d  ax 1 c 'Ax
'z 2 'Az
'x d ay
1 c 'Ay
'x 2
'Ax
d  az
(3.54)
By transforming eq. (3.54) using point and vector transformation techniques used in
­Chapter 2, we obtain the curl of A in cylindrical coordinates as
84  CHAPTER 3  VECTOR CALCULUS
= 3 A 5 1
r ∞
r af
rAf
= 3 A 5 c 1
'Az
'f 2
'Af
'z d  ar 1 c
'Ar
'z 2 'Az
'r d  af
1 1
r c
'1rAf2
'Ar
'f d  az
(3.55)
and in spherical coordinates as
= 3 A 5
r2 sin u ∞
r au
r sin u af
rAu
r sin u Af
= 3 A 5
r sin u c
'1Af sin u2
2 'Au
'f d  ar
1 1
r c
sin u 'Ar
'f 2
'1rAf2
d  au 1 1
r c '1rAu2
2 'Ar
'u d  af
(3.56)
Note the following properties of the curl:
1.	 The curl of a vector field is another vector field.
2.	 = 3 1A 1 B2 5 = 3 A 1 = 3 B
3.	 = 3 1A 3 B2 5 A1= # B2 2 B1= # A2 1 1B # =2A 2 1A # =2B
4.	 = 3 1VA2 5 V= 3 A 1 =V 3 A
5.	 The divergence of the curl of a vector field vanishes; that is, = # 1= 3 A2 5 0.
6.	 The curl of the gradient of a scalar field vanishes; that is, = 3 =V 5 0 or
= 3 = 5 0.
Other properties of the curl are given in Appendix A.10.
The physical significance of the curl of a vector field is evident in eq. (3.45); the curl
provides the maximum value of the circulation of the field per unit area (or circulation
density) and indicates the direction along which this maximum value occurs. The curl of
a vector field A at a point P may be regarded as a measure of the circulation or how much
the field curls around P. For example, Figure 3.20(a) shows that the curl of a vector field
around P is directed out of the page. Figure 3.20(b) shows a vector field with zero curl.
﻿ ﻿  85
3.7 Curl of a Vector and Stokes’s Theorem  85
Also, from the definition of the curl of A in eq. (3.45), we may expect that
A # dl 5 3
1= 3 A2 # dS
(3.57)
This is called Stokes’s theorem.
Stokes’s theorem states that the circulation of a vector field A around a (closed) path
L is equal to the surface integral of the curl of A over the open surface S ­bounded by L
(see Figure 3.21), provided A and   A are continuous on S.
The proof of Stokes’s theorem is similar to that of the divergence theorem. The surface
S is subdivided into a large number of cells as in Figure 3.22. If the kth cell has surface area
DSk and is bounded by path Lk,
A # dl 5 a
A # dl 5 a
A # dl
DSk
DSk
(3.58)
As shown in Figure 3.22, there is cancellation on every interior path, so the sum of the
line integrals around the Lk’s is the same as the line integral around the bounding curve L.
Therefore, taking the limit of the right-hand side of eq. (3.58) as DSk S  0 and incorporat­
ing eq. (3.45) leads to
A # dl 5 3
1= 3 A2 # dS
which is Stokes’s theorem.
FIGURE 3.20  Illustration of a curl: (a) curl at P points
out of the page, (b) curl at P is zero.
FIGURE 3.21  Determining the sense of
dl and dS involved in Stokes’s theorem.
path L
86  CHAPTER 3  VECTOR CALCULUS
The direction of dl and dS in eq. (3.57) must be chosen using the right-hand rule or
right-handed-screw rule. Using the right-hand rule, if we let the fingers point in the direc­
tion of dl, the thumb will indicate the direction of dS (see Figure 3.21). Note that whereas
the divergence theorem relates a surface integral to a volume integral, Stokes’s theorem
relates a line integral (circulation) to  suface integral.
FIGURE 3.22  Illustration of Stokes’s theorem.
Determine the curl of each of the vector fields in Example 3.6.
Solution:
(a)	 = 3 P 5 a'Pz
'y 2
'Py
'z b ax 1 a'Px
'z 2 'Pz
'x b ay 1 a
'Py
'x 2 'Px
'y b az
5 10 2 02ax 1 1x2y 2 z2ay 1 10 2 x2z2az
5 1x2y 2 z2ay 2 x2zaz
(b)	 = 3 Q 5 c 1
r 'Qz
'f 2
'Qf
'z d ar 1 c
'Qr
'z 2 'Qz
'r d af 1 1
r c '
'r 1rQf2 2
'Qr
'f d az
5 a2z
r  sin f 2 r2b ar 1 10 2 02af 1 1
r 13r2z 2 r cos f2az
5 21
r 1z sin f 1 r32ar 1 13rz 2 cos f2az
(c)	 = 3 T 5
r sin u c '
'u 1Tfsin u2 2 '
'f Tud  ar
1 1
r c
sin u '
'f Tr 2 '
'r 1rTf2 d  au 1 1
r c '
'r 1rTu2 2 '
'u Trd  af
r sin u c '
'u 1cos u sin u2 2 '
'f 1r sin u cos f2 d  ar
1 1
r c
sin u '
1cos u2
2 '
'r 1r cos u2 d  au
EXAMPLE 3.8
﻿ ﻿  87
3.7 Curl of a Vector and Stokes’s Theorem  87
1 1
r c '
'r 1r2 sin u cos f2 2 '
1cos u2
d  af
r sin u 1cos 2u 1 r sin u sin f2ar 1 1
r 10 2 cos u2au
1 1
r a2r sin u cos f 1 sin u
r2 b af
5 acos 2u
r sin u 1 sin fb ar 2 cos u
au 1 a2 cos f 1 1
r3b sin u af
EXAMPLE 3.9
PRACTICE EXERCISE  3.8
Determine the curl of each of the vector fields in Practice Exercise 3.6 and evaluate
the curls at the specified points.
Answer:  (a)  ax 1 yay 1 14y 2 z2az, ax 2 2ay 2 11az
(b)  26rz cos f ar 1 r sin f af 1 16z 2 12z cos f az, 5af
(c)  cot u
r1/2  ar 2 a2 cot u sin f 1
2r1/2bau 1 2 sin u cos f af,
1.732ar 2 4.5au 1 0.5af.
If A 5 r cos f ar 1 sin f af, evaluate A A # dl around the path shown in Figure 3.23.
Confirm this by using Stokes’s theorem.
Solution:
Let
A # dl 5 c3
1 3
1 3
1 3
d A # dl
where path L has been divided into segments ab, bc, cd, and da as in Figure 3.23.
FIGURE 3.23  For Example 3.9.
88  CHAPTER 3  VECTOR CALCULUS
Along ab, r 5 2 and dl 5 r df af. Hence,
A # dl 5 3
30°
f560°
r sin f df 5 212cos f2 `
60°
30°
5 21"3 2 12
Along bc, f 5 30° and dl 5 dr ar. Hence,
A # dl 5 3
r52
r cos f dr 5 cos 30° r2
2  `
5 21"3
Along cd, r 5 5 and dl 5 r df af. Hence,
A # dl 5 3
60°
f530°
r sin f df 5 512cos f2 `
30°
60°
5 5
2 1"3 2 12
Along da, f 5 60° and dl 5 dr ar. Hence,
A # dl 5 3
r55
r cos f dr 5 cos 60° r2
2  `
5 221
Putting all these together results in
A # dl 5 2"3 1 1 1 21"3
1 5"3
2 5
2 2 21
5 27
4  1"3 2 12 5 4.941
From Stokes’s theorem (because L is a closed path),
A # dl 5 3
1= 3 A2 # dS
But dS 5 r df dr az and
= 3 A 5 arc 1
r 'Az
'f 2
'Af
'z d 1 af c
'Ar
'z 2 'Az
'r d 1 az 1
r c '
'r 1rAf2 2
'Ar
'f d
5 10 2 02ar 1 10 2 02af 1 1
r 11 1 r2 sin f az
Hence:
1= 3 A2 # dS 5 3
60°
f530°
r52
r 11 1 r2 sin f r dr df
﻿ ﻿  89
3.7 Curl of a Vector and Stokes’s Theorem  89
PRACTICE EXERCISE  3.9
Use Stokes’s theorem to confirm your result in Practice Exercise 3.2.
Answer:  1.
PRACTICE EXERCISE  3.10
For a scalar field V, show that   V  0; that is, the curl of the gradient of any scalar
field vanishes.
Answer:  Proof.
EXAMPLE 3.10
For a vector field A, show explicitly that = # = 3 A 5 0; that is, the divergence of the curl
of any vector field is zero.
Solution:
This vector identity, along with the one in Practice Exercise 3.10, is very useful in EM. For
simplicity, assume that A is in Cartesian coordinates.
= # = 3 A 5 a '
'x, '
'y, '
'zb # ∞
5 a '
'x, '
'y, '
'zb # c a'Az
'y 2
'Ay
'z b, 2a'Az
'x 2 'Ax
'z b, a
'Ay
'x 2 'Ax
'y b d
5 '
'x a'Az
'y 2
'Ay
'z b 2 '
'y a'Az
'x 2 'Ax
'z b 1 '
'z a
'Ay
'x 2 'Ax
'y b
5 '2Az
'x 'y 2
'2Ay
'x 'z 2 '2Az
'y 'x 1 '2Ax
'y 'z 1
'2Ay
'z 'x 2 '2Ax
'z 'y
5 0
because '2Az
'x 'y 5 '2Az
'y 'x, and so on.
5 3
60°
30°
sin f df 3
11 1 r2dr
5 2cos f `
30°
60°
ar 1 r2
2 b `
5 27
4  1"3 2 12 5 4.941
90  CHAPTER 3  VECTOR CALCULUS
For practical reasons, it is expedient to introduce a single operator that is the composite of
gradient and divergence operators. This operator is known as the Laplacian.
The Laplacian of a scalar field V, written as 2V, is the divergence of the gradient of V.
Thus, in Cartesian coordinates,
Laplacian V 5 = # =V 5 =2V
5 c '
'x ax 1 '
'y ay 1 '
'z azd # c 'V
'x  ax 1 'V
'y  ay 1 'V
'z  azd
(3.59)
that is,
=2V 5 '2V
'x2 1 '2V
'y2 1 '2V
'z2 
(3.60)
Notice that the Laplacian of a scalar field is another scalar field.
The Laplacian of V in other coordinate systems can be obtained from eq. (3.60) by
transformation. In cylindrical coordinates,
=2V 5 1
r '
'r ar 'V
'r b 1 1
r2 '2V
'f2 1 '2V
'z2 
(3.61)
and in spherical coordinates,
=2V 5 1
r2 '
'r ar2'V
'r b 1
r2 sin u '
'u asin u 'V
'u b 1
r2 sin2 u '2V
'f2
(3.62)
A scalar field V is said to be harmonic in a given region if its Laplacian vanishes in that
region. In other words, if
=2V 5 0
(3.63)
is satisfied in the region, the solution for V in eq. (3.63) is harmonic (it is of the form of
sine or cosine). Equation (3.63) is called Laplace’s equation. This equation will be solved
in Chapter 6.
We have considered only the Laplacian of a scalar. Since the Laplacian operator 2 is
a scalar operator, it is also possible to define the Laplacian of a vector A. In this context,
2A should not be viewed as the divergence of the gradient of A. Rather, 2A is defined
as the gradient of the divergence of A minus the curl of the curl of A. That is,
=2A 5 =1= # A2 2 = 3 = 3 A
(3.64)
This equation can be applied in finding 2A in any coordinate system. In the Cartesian
3.8  LAPLACIAN OF A SCALAR
﻿ ﻿  91
3.8 Laplacian of a Scalar  91
­system (and only in that system), eq. (3.64) becomes3
=2A 5 =2Axax 1 =2Ayay 1 =2Azaz
(3.65)
EXAMPLE 3.11
Find the Laplacian of the scalar fields of Example 3.3; that is,
(a)  V 5 e2z sin 2x cosh y
(b)  U 5 r2z cos 2f
(c)  W 5 10r sin2 u cos f
Solution:
The Laplacian in the Cartesian system can be found by taking the first derivative and later
the second derivative.
(a)  =2V 5 '2V
'x2 1 '2V
'y2 1 '2V
'z2
5 '
'x 12e2z cos 2x cosh y2 1 '
'y 1e2z sin 2x sinh y2
1 '
'z 12e2z sin 2x cosh y2
5 24e2z sin 2x cosh y 1 e2z sin 2x cosh y 1 e2z sin 2x cosh y
5 22e2z sin 2x cosh y
(b)  =2U 5 1
r '
'r ar'U
'r b 1 1
r2 '2U
'f2 1 '2U
'z2
5 1
r '
'r 12r2z cos 2f2 2 1
r2 4r2z cos 2f 1 0
5 4z cos 2f 2 4z cos 2f
5 0
(c)  =2W 5 1
r2 '
'r ar2'W
'r b 1
r2 sin u '
'u asin u 'W
'u b 1
r2 sin2 u '2W
'f2
5 1
r2 '
'r 110r2 sin2 u cos f2 1
r2 sinu '
'u 110r sin 2u sin u cos f2
2 10r sin2 u cos f
r2 sin2 u
5 20 sin2 u cos f
1 20r cos 2u sin u cos f
r2 sin u
1 10r sin 2u cos u cos f
r2 sin u
2 10 cos f
5 10 cos f
12 sin2 u 1 2 cos 2u 1 2 cos2 u 2 12
5 10 cos f
11 1 2 cos 2u2
3 For explicit formulas for 2A in cylindrical and spherical coordinates, see M. N. O. Sadiku, Numerical Techniques
in Electromagnetics with MATLAB, 3rd ed. Boca Raton, FL: CRC Press, 2009, p. 647.
92  CHAPTER 3  VECTOR CALCULUS
PRACTICE EXERCISE  3.11
Determine the Laplacian of the scalar fields of Practice Exercise 3.3, that is,
(a)  U 5 x2y 1 xyz
(b)  V 5 rz sin f 1 z2 cos2 f 1 r2
(c)  f 5 cos u sin f ln r 1 r2 f
Answer:  (a) 2y,  (b) 4 1 2 cos2 f 2 2z2
r2  cos 2f,  (c) 1
r2 cos u sin f 11 2 2 ln r
csc2 u ln r2 1 6f.
A vector field is uniquely characterized by its divergence and curl. Neither the ­divergence
nor the curl of a vector field is sufficient to completely describe the field. All vector
fields can be classified in terms of their vanishing or nonvanishing divergence or curl
as ­follows:
(a)	 = # A 5 0, = 3 A 5 0
(b)	 = # A 2 0, = 3 A 5 0
(c)	 = # A 5 0, = 3 A 2 0
(d)	 = # A 2 0, = 3 A 2 0
Figure 3.24 illustrates typical fields in these four categories.
A vector field A is said to be solenoidal (or divergenceless) if  = # A 5 0
†3.9  CLASSIFICATION OF VECTOR FIELDS
(a)
(b)
(c)
(d)
FIGURE 3.24  Typical fields with vanishing and nonvanishing divergence or curl.
(a)	 A 5 kax, = # A 5 0, = 3 A 5 0,
(b)	 A 5 kr, = # A 5 3k, = 3 A 5 0,
(c)	 A 5 k 3 r, = # A 5 0, = 3 A 5 2k,
(d)	 A 5 k 3 r 1 cr, = # A 5 3c, = 3 A 5 2k.
3.9 Classification of Vector Fields﻿  93
Such a field has neither source nor sink of flux. From the divergence theorem,
A # dS 5 3
= # A dv 5 0
(3.66)
Hence, flux lines of A entering any closed surface must also leave it. Examples of sole­
noidal fields are incompressible fluids, magnetic fields, and conduction current density
under steady-state conditions. In general, the field of curl F (for any F) is purely solenoidal
because = # 1= 3 F2 5 0, as shown in Example 3.10. Thus, a solenoidal field A can always
be expressed in terms of another vector F; that is,
then
= # A 5 0
A # dS 5 0   and   A 5 = 3 F
(3.67)
A vector field A is said to be irrotational (or potential) if  = 3 A 5 0.
That is, a curl-free vector is irrotational.4 From Stokes’s theorem
1= 3 A2 # dS 5 C
A # dl 5 0
(3.68)
Thus in an irrotational field A, the circulation of A around a closed path is identically
zero. This implies that the line integral of A is independent of the chosen path. Therefore,
an irrotational field is also known as a conservative field. Examples of irrotational fields
include the electrostatic field and the gravitational field. In general, the field of gradient V
(for any scalar V) is purely irrotational, since (see Practice Exercise 3.10)
= 3 1=V2 5 0
(3.69)
Thus, an irrotational field A can always be expressed in terms of a scalar field V; that is,
then
= 3 A 5 0
A # dl 5 0   and   A 5 2=V
(3.70)
For this reason, A may be called a potential field and V the scalar potential of A. The nega­
tive sign in eq. (3.70) has been inserted for physical reasons that will become evident in
Chapter 4.
4 In fact, curl was once known as rotation, and curl A is written as rot A in some textbooks. This is one reason
to use the term irrotational.
94  CHAPTER 3  VECTOR CALCULUS
A vector A is uniquely prescribed within a region by its divergence and its curl. If we let
= # A 5 rv
(3.71a)
and
= 3 A 5 rS
(3.71b)
rv can be regarded as the source density of A and rS its circulation density. Any vector A
satisfying eq. (3.71) with both rv and rS vanishing at infinity can be written as the sum
of two vectors: one irrotational (zero curl), the other solenoidal (zero divergence). This is
called Helmholtz’s theorem. Thus we may write
A 5 2=V 1 = 3 B
(3.72)
If we let Ai 5 2=V and As 5 = 3 B, it is evident from Example 3.10 and Practice
­Exercise 3.10 that = 3 Ai 5 0 and = # As 5 0, showing that Ai is irrotational and As is
solenoidal. Finally, it is evident from eqs. (3.64) and (3.71) that any vector field has a
Laplacian that satisfies
=2A 5 =rv 2 = 3 rS
(3.73)
EXAMPLE 3.12
Show that the vector field A is conservative if A possesses one of these two properties:
(a)  The line integral of the tangential component of A along a path extending from a point
P to a point Q is independent of the path.
(b)  The line integral of the tangential component of A around any closed path is zero.
Solution:
(a)  If A is conservative, = 3 A 5 0, so there exists a potential V such that
A 5 2=V 5 2c 'V
'x  ax 1 'V
'y  ay 1 'V
'z  azd
Hence,
A # dl 5 23
c 'V
'x  dx 1 'V
'y  dy 1 'V
'z  dzd
5 23
c 'V
'x  dx
ds 1 'V
ds 1 'V
'z  dz
ds d  ds
5 23
ds  ds 5 23
A # dl 5 V1P2 2 V1Q2
3.9 Classification of Vector Fields﻿  95
showing that the line integral depends only on the end points of the curve. Thus, for a
conservative field, e
A # dl is simply the difference in potential at the end points.
(b)	 If the path is closed, that is, if P and Q coincide, then
C A # dl 5 V1P2 2 V1P2 5 0
PRACTICE EXERCISE  3.12
Show that B  (y  z cos xz)ax  xay  x cos xz az is conservative, without computing
any integrals.
Answer:  Proof.
% This script allows the user to compute the integral of
% a function using two different methods:
%   1. the built-in matlab ‘quad’ function
%   2. user-defined summation
%  The user must first create a separate file for the function
%      y = (–1/20)*x^3+(3/5)*x.^2–(21/10)*x+4;
%  The file should be named fun.m and stored in the same
%  directory as this file, and it should contain the following
%  two lines:
%        function y = fun(x)
%        y = (-1/20)*x.^3+(3/5)*x.^2–2.1*x+4;
% We will determine the integral of this function from x = 0
% to x = 8
clear
% First we’ll plot the function, creating a vector x and y
x=0:0.01:8;
y=fun(x);
figure(1)   % create a figure
plot(x,y, ‘LineWidth’, 2)      % plot x versus y
axis([0 10 0 4]) % sets the axis appropriately
xlabel(‘x variable’)    % axes labels
ylabel(‘y variable’)    % axes labels
% Next we’ll use the built-in Matlab function to find the
% quadrature integral
Q = quad(@fun,0,8);   % The @ is an address operator to
% point to fun.m
% Finally we’ll create a custom summation to compute the
% integral quadrature integral
MATLAB 3.1
96  CHAPTER 3  VECTOR CALCULUS
disp(‘Enter a increment size for the integral, recommended ’);
disp(‘ 0.1 to 1 (the smaller the better, but’);
dx=input(‘smaller requires more computation time)! ... >’);
sum=0; % set initial total sum to zero
for x=0:dx:8,
sum=sum+fun(x)*dx;  % add the partial sums to the total sum
end
disp(‘’)
disp(‘The computed integrals of the function y(x) between’);
disp(‘ x = 0 and x = 8 are’)
% The tab %f outputs the floating point number given in the
% variables Q and sum, similar to C/C++
disp(sprintf(‘ quad integral =’);
disp(sprintf(‘ %f\n custom summation integral = %f’, Q, sum))
% Now plot the function with the sub-areas used in the
% approximation create rectangular patches for each sub-area
figure(2)   % create another figure number 2
for x=0:dx:8,
patch([x–dx/2; x–dx/2; x+dx/2; x+dx/2], ...
[0; fun(x); fun(x); 0], [0.5 0.5 0.5])
end
% now plot original function
hold on
x=0:0.01:8;
y=fun(x);
h=plot(x,y, ‘LineWidth’, 2)      % plot x versus y
axis([0 10 0 4]) % sets the axis appropriately
xlabel(‘x variable’)    % axes labels
ylabel(‘y variable’)    % axes labels
function y = fun(x)
y = (–1/20)*x.^3+(3/5)*x.^2–2.1*x+4;
% This script allows the user to find the divergence and curl
% of a vector field given in symbolic form
% It uses the built-in symbolic derivative function
% called diff() to compute the derivatives
clear
syms x y z   % declare x,y,z to be symbols (variables)
% Prompt the user to enter the symbolic vector
%    For example the user could enter [y*z 4*x*y y]
disp(‘Enter the symbolic vector (in the format ‘);
A = input(‘[ fx(x,y,z) fy(x,y,z) fz(x,y,z)])... \n >  ‘);
% The divergence of A
% e.g. diff(A(2),z) means the derivative of the
MATLAB 3.2
Summary  97
% y-component of vector A with respect to z
divA=diff(A(1),x)+...
diff(A(2),y)+...
diff(A(3),z)
% evaluate divergence at point (x,y,z) = (1, –2, 3)
subs(divA,{x,y,z},{1, –2, 3})
% The curl of A
% e.g. diff(A(2),z) means the derivative of the
% y-component of vector A with respect to z
curlA=[diff(A(3),y)–diff(A(2),z),...
–diff(A(3),x)+diff(A(1),z),...
diff(A(2),x)–diff(A(1),y)]
% evaluate curl at point (x,y,z) = (1, –2, 3)
subs(curlA,{x,y,z},{1, –2, 3})
SUMMARY
1.	 The differential displacements in the Cartesian, cylindrical, and spherical systems are,
respectively,
dl 5 dx ax 1 dy ay 1 dz az
dl 5 dr ar 1 r df af 1 dz az
dl 5 dr ar 1 r du au 1 r sin u df af
Note that dl is always taken to be in the positive direction; the direction of the displace­
ment is taken care of by the limits of integration.
2.	 The differential normal areas in the three systems are, respectively,
dS 5 dy dz ax
dx dz ay
dx dy az
dS 5 r df dz ar
dr dz af
r dr df az
dS 5 r2 sin u du df ar
r sin u dr df au
r dr du af
Note that dS can be in the positive or negative direction depending on the surface
under consideration.
3.	 The differential volumes in the three systems are
dv 5 dx dy dz
dv 5 r dr df dz
dv 5 r2 sin u dr du df
98  CHAPTER 3  VECTOR CALCULUS
4.  The line integral of vector A along a path L is given by eL A # dl. If the path is closed,
the line integral becomes the circulation of A around L, that is, AL A # dl.
5.  The flux or surface integral of a vector A across a surface S is defined as eS A # dS.
When the surface S is closed, the surface integral becomes the net outward flux of A
across S, that is, AS A # dS.
6.  The volume integral of a scalar rv over a volume v is defined as ev rv dv.
7.  Vector differentiation is performed by using the vector differential operator . The
gradient of a scalar field V is denoted by V, the divergence of a vector field A by
= # A, the curl of A by = 3 A, and the Laplacian of V by 2V. All of these are point
functions since differentiation is always at a point.
8.  The divergence theorem, AS A # dS 5 ev = # A dv, relates a surface integral over a
closed surface to a volume integral.
9.  Stokes’s theorem, AL A # dl 5 eS 1= 3 A2 # dS, relates a line integral over a closed
path to a surface integral.
10.  If Laplace’s equation, =2V 5 0, is satisfied by a scalar field V in a given region, V is
said to be harmonic in that region.
11.  A vector field is solenoidal if = # A 5 0; it is irrotational or conservative if = 3 A 5 0.
12.  A summary of the vector calculus operations in the three coordinate systems is pro­
vided on the inside back cover of the text.
13.  The vector identities = # = 3 A 5 0 and = 3 =V 5 0 are very useful in EM. Other
vector identities are in Appendix A.10.
REVIEW
QUESTIONS
3.1	 Consider the differential volume of Figure 3.25. Match the items in the left-hand column
with those on the right.
(a)  dl from A to B
(i)	 dy dz ax
(b)  dl from A to D
(ii)	 2dx dz ay
(c)  dl from A to E
(iii)	 dx dy az
(d)  dS for face ABCD
(iv)	 2dx dy az
(e)  dS for face AEHD
(v)	 dx ax
(f)  dS for face DCGH
(vi)	 dy ay
(g)  dS for face ABFE
(vii)	 dz az
FIGURE 3.25  For Review Question 3.1.
Review Questions  99
3.2	 For the differential volume in Figure 3.26, match the items in the left-hand list with those
on the right.
(a)  dl from E to A
(i)	 2r df dz ar
(b)  dl from B to A
(ii)	 2dr dz af
(c)  dl from D to A
(iii)	 2r dr df az
(d)  dS for face ABCD
(iv)	 r dr df az
(e)  dS for face AEHD
(v)	 dr ar
(f)  dS for face ABFE
(vi)	 r df af
(g)  dS for face DCGH
(vii)	 dz az
3.3	 Consider the object shown in Figure 3.8. For the volume element, match the items in the
left-hand column with those on the right.
(a)  dl from A to D
(i)	 2r2 sin u du df ar
(b)  dl from E to A
(ii)	 2r sin u dr df au
(c)  dl from A to B
(iii)	 r dr du af
(d)  dS for face EFGH
(iv)	 dr ar
(e)  dS for face AEHD
(v)	 r du au
(f)  dS for face ABFE
(vi)	 r sin u df af
3.4	 If r 5 xax 1 yay 1 zaz, the position vector of point 1x, y, z2 and r 5 0 r 0 , which of the
­following is incorrect?
(a)  =r 5 r/r
(c)  =21r # r2 5 6
(b)  = # r 5 1
(d)  = 3 r 5 0
(a)  = 3 = ? A
(c)  = (=V)
(b)  = ? (= ? A)
(d)  = (= ? A)
3.6	 Which of the following is zero?
(a)  grad div
(c)  curl grad
(b)  div grad
(d)  curl curl
3.7	 Given field A 5 3x2yzax 1 x3zay 1 1x3y 2 2z2az, it can be said that A is
(a)  Harmonic
(d)  Rotational
(b)  Divergenceless
(e)  Conservative
(c)  Solenoidal
FIGURE 3.26  For Review Question 3.2.
ρ dφ
3.5 Which of the following is mathematically defined?
100  CHAPTER 3  VECTOR CALCULUS
3.8	 The surface current density J in a rectangular waveguide is plotted in Figure 3.27. It is evi­
dent from the figure that J diverges at the top wall of the guide, whereas it is divergenceless
at the side wall.
(a)  True
(b)  False
3.9	 Stokes’s theorem is applicable only when a closed path exists and the vector field and its
derivatives are continuous within the path.
(a)  True
(c)  Not necessarily
(b)  False
3.10	 If a vector field Q is solenoidal, which of these is true?
(a)  AL Q # dl 5 0
(d)  = 3 Q 2 0
(b)  AS Q # dS 5 0
(e)  =2Q 5 0
(c)  = 3 Q 5 0
Answers: 3.1a-(vi), b-(vii), c-(v), d-(i), e-(ii), f-(iv), g-(iii), 3.2a-(vi), b-(v), c-(vii), d-(ii), e-(i),
f-(iv), g-(iii), 3.3a-(v), b-(vi), c-(iv), d-(iii), e-(i), f-(ii), 3.4b, 3.5d, 3.6c, 3.7e, 3.8a,
3.9a, 3.10b.
PROBLEMS
FIGURE 3.27  For Review Question 3.8.
Section 3.2—Differential Length, Area, and Volume
3.1 Using the differential length dl, find the length of each of the following curves:
(a) r 5 3, p/4 , f , p/2, z 5 constant
(b) r 5 1, u 5 30°, 0 , f , 60°
(c) r 5 4, 30° , u , 90°, f 5 constant
3.2 Calculate the areas of the following surfaces using the differential surface area dS:
(a) r 5 2, 0 , z , 5, p/3 , f , p/2
(b) z 5 1, 1 , r , 3, 0 , f , p/4
(c) r 5 10, p/4 , u , 2p/3, 0 , f , 2p
(d) 0 , r , 4, 60° , u , 90°, f 5 constant
Problems  101
3.3	 Use the differential volume dv to determine the volumes of the following regions:
(a)  0 , x , 1, 1 , y , 2, 23 , z , 3
(b)  2 , r , 5, p/3 , f , p, 21 , z , 4
(c)  1 , r , 3, p/2 , u , 2p/3, p/6 , f , p/2
3.4	 Find the length of a path from P1(4, 0, 0) to P2(4, 30, 0).
3.5	 Calculate the area of the surface defined by r = 5, 0 , u , p/4, 0 , f , p/2.
3.6	 Calculate the volume defined by 2 , r , 5, 0 , f , 30, 0 , z , 10.
Section 3.3—Line, Surface, and Volume Integrals
3.7	 Let H 5 xy2ax
1 x2yay. Evaluate the line integral along the parabola x 5 y2 joining point
P(1, 1, 0) to point Q(16, 4, 0).
3.8
Evaluate the line integral eL (2x2 2 4xy)dx 1 3xy 2 2x2y)dy over the straight path L joining
point P(1,21, 2) to Q(3, 1, 2).
3.9	 If the integral e
A F # dl is regarded as the work done in moving a particle from A to B,
find the work done by the force field
F 5 2xyax 1 1x2 2 z22ay 2 3xz2az
on a particle that travels from A10, 0, 02 to B12, 1, 32 along
(a)  The segment 10, 0, 02 S  10, 1, 02 S  12, 1, 02 S  12, 1, 32
(b)  The straight line 10, 0, 02 to 12, 1, 32
3.10	 A vector field is represented by F 5 r2ar 1 zaf 1 cos faz Newtons. Evaluate
the work done or eL  F # dl, where L is from P(2, 0°, 0) to Q12, p/4, 32. Assume
that L consists of the arc r 5 2, 0 , f , p/4, z 5 0, followed by the line
r 5 2, f 5 p/4, 0 , z , 3.
3.11	 If
H 5 1x 2 y2ax 1 1x2 1 zy2ay 1 5yzaz
evaluate eL  H # dl along the contour of Figure 3.28.
FIGURE 3.28  For Problem 3.11.
FIGURE 3.29  For Problem 3.12.
x = 1
102  CHAPTER 3  VECTOR CALCULUS
3.12	 Determine the circulation of B 5 xyax 2 yzay 1 xzaz around the path L on the x 5 1
plane, shown in Figure 3.29.
3.13	 Let A 5 yax 1 zay 1 xaz. Find the flux of A through surface y 5 1, 0 , x , 1, 0 , z , 2.
3.14	 If D 5 x2zax 1 y3ay 1 yz2az, calculate the flux of D passing through the volume bounded
by planes x 5 21, x 5 1, y 5 0, y 5 4, z 5 1, and z 5 3.
3.15	 A vector field is specified as A 5 rar 2 3au 1 5faf. Find the flux of the field out of the
closed surface defined by 0 , r , 4, 0 , u , p/2, 0 , f , 3 , p/2.
3.16	 (a)  Evaluate 3
xy dv, where v is defined by 0 , x , 1, 0 , y , 1, 0 , z , 2.
(b)  Determine 3
rz dv, where v is bounded by r 5 1, r 5 3, f 5 0, f 5 p, z 5 0, and z 5 2.
Section 3.5—Gradient of a Scalar
3.17	 Calculate the gradient of:
(a)  V1 5 6xy 2 2xz 1 z
(b)  V2 5 10r cos f 2 rz
(c)  V3 5 2
r cos f
3.18	 Find the gradient of the following scalar fields and evaluate the gradient at the specified
point.
(a)  V(x, y, z) 5 10xyz 2 2x2z at P(21, 4, 3)
(b)  U(r, f, z) 5 2r sin f 1 rz at Q(2, 908, 21)
(c)  W(r, u, f) 5 4
r sin u cos f at R(1, p/6, p/2)
3.19	 If r 5 xax 1 yay 1  zaz is the position vector of point (x, y, z), r = |r|, and n is an integer,
show that =rn 5 nrn22r.
3.20	 The temperature in an auditorium is given by T 5 x2 1 y2 2 z. A mosquito located at
11, 1, 22 in the auditorium desires to fly in such a direction that it will get warm as soon
as possible. In what direction must it fly?
3.21	 A family of planes is described by F 5 x 2 2y 1 z. Find a unit normal an to the planes.
3.22	 Consider the scalar function T 5 r sin  cos f. Determine the magnitude and direction
of the maximum rate of change of T at P(2, 68, 308).
3.23	 Let f 5 x2y 2 2xy2 1 z3. Find the directional derivative of f at point (2, 4, 23) in the
direction of ax 1 2ay 2 az.
3.24	 (a)  Using the gradient concept, prove that the angle between two planes
ax 1 by 1 cz 5 d
ax 1 by 1 gz 5 d
 5 cos21
aa 1 bb 1 cg
"1a2 1 b2 1 c22 1a2 1 b2 1 g22
Problems  103
(b)  Calculate the angle between two planes x 1 2y 1 3z 5 5 and x 1 y 5 0.
3.25	 Let V(x, y, z) 5 4xyez. Find the maximum rate of change of V at (3, 1, 22) and the direc­
tion in which it occurs.
3.26	 (a)  Prove that for scalar fields V and U,
=(UV) 5 U=V 1 V=U
(b)  Verify part (a) by assuming that V 5 5x2y 1 2yz and U 5 3xyz.
Section 3.6—Divergence of a Vector and Divergence Theorem
3.27	 Evaluate the divergence of the following vector fields:
(a)  A 5 xyax 1 y2ay 2 xzaz
(b)  B 5 rz2ar 1 r sin2 f af 1 2rz sin2 f az
(c)  C 5 rar 1 r cos2 u af
3.28	 (a)  If A 5 x2yax 1 xay 1 2yzaz, find =  A at point (23, 4, 2).
(b)  Given that B 5 3r sin far 2 5r2zaf 1 8z cos2 faz, find =  B at point (5, 308, 1).
(c)  Let C 5 r2 cos far 1 2raf, find =  C at point (2, p/3, p/2).
3.29	 The heat flow vector H 5 k=T, where T is the temperature and k is the thermal con­
ductivity. Show that if
T 5 50 sin px
2  cosh
then = # H 5 0.
3.30	 (a)  Prove that
= # 1VA2 5 V= # A 1 A # =V
where V is a scalar field and A is a vector field.
(b)  Evaluate = # 1VA2 when A 5 2xax 1 3yay 2 4zaz and V 5 xyz.
3.31	 If r 5 xax 1 yay 1 zaz and T 5 2zyax 1 xy2ay 1 x2yzaz, determine
(a)  1= # r2T
(b)  1r # =2T
(c)  = # r1r # T2
(d)  1r # =2r2
3.32	 If A 5 2xax 2 z2ay 1 3xyaz, find the flux of A through a surface defined by r 5 2,
0 , f , p/2, 0 , z , 1.
3.33	 Let D 5 2rz2ar 1 r cos2 f az. Evaluate
(a)  AS D # dS
(b)  ev = # D dv
over the region defined by 2 # r # 5, 21 # z # 1, 0 , f , 2p.
104  CHAPTER 3  VECTOR CALCULUS
3.34	 If
H 5 10 cos uar,
evaluate
eS H # dS
over
hemisphere
defined
r 5 1, 0 , f , 2p, 0 , u , p/2.
3.35	 Evaluate both sides of the divergence theorem for the vector field
H 5 2xyax 1 x2 1 z22ay 1 2yzaz
and the rectangular region defined by 0 , x , 1, 1 , y , 2, 21 , z , 3.
3.36	 Let H 5 4r2ar 2 2zaz. Verify the divergence theorem for the cylindrical region defined
by r = 10, 0 , f , 2p, 0 , z , 3.
*3.37	 Apply the divergence theorem to evaluate C
A # dS, where A 5 x2ax 1 y2ay 1 z2az and S
is the surface of the solid bounded by the cylinder r 5 1 and planes z 5 2 and z 5 4.
3.38	 Verify the divergence theorem for the function A 5 r2ar 1 r sin u cos f au over the ­
surface of a quarter of a hemisphere defined by 0 , r , 3, 0 , f , p/2, 0 , u , p/2.
3.39	 Calculate the total outward flux of vector
F 5 r2 sin f ar 1 z cos f af 1 rzaz
through the hollow cylinder defined by 2 # r # 3, 0 # z # 5.
Section 3.7—Curl of a Vector and Stokes’s Theorem
3.40	 Evaluate the curl of the following vector fields:
(a)  A 5 xyax 1 y2ay 2 xzaz
(b)  B 5 rz2ar 1 r sin2 f af 1 2rz sin2 f az
(c)  C 5 rar 1 r cos2 u af
3.41	 Evaluate = 3 A and = # 1= 3 A2 if:
(a)  A 5 x2yax 1 y2zay 2 2xzaz
(b)  A 5 r2zar 1 r3af 1 3rz2az
(c)  A 5 sin f
r2  ar 2 cos f
r2  au
3.42	 Let H 5 r sin far 1 r cos faf 2 raz ; find = 3 H and = 3 = 3 H.
3.43	 Let A 5
xax 1 yay 1 zaz
1x2 1 y2 1 z22 3/2 ; show that = 3 A 5 0.
*3.44	 Given that F 5 x2yax 2 yay, find
(a)  AL F # dl, where L is shown in Figure 3.30.
(b)  eS 1= 3 F2 # dS, where S is the area bounded by L.
(c)  Is Stokes’s theorem satisfied?
Problems  105
3.45	 Let A 5 r sin f ar 1 r2af; evaluate AL A # dl if L is the contour of Figure 3.31.
3.46	 If F 5 2rzar 1 3z sin f af 2 4r cos f az, verify Stokes’s theorem for the open surface
defined by z 5 1, 0 , r , 2, 0 , f , 45°.
3.47	 Let A 5 4x2e2yax 2 8xe2yay. Determine = 3 3=1= # A2 4.
3.48	 Let V 5 sin u cos f
. Determine:
(a)  =V,        (b) = 3 =V,        (c) = # =V
**3.49  A vector field is given by
Q 5
"x2 1 y2 1 z2
"x2 1 y2
3 1x 2 y2ax 1 1x 1 y2ay4
FIGURE 3.30  For Problem 3.44.
FIGURE 3.31  For Problem 3.45.
**Double asterisks indicate problems of highest difficulty.
FIGURE 3.32  Volume in form of ice
cream cone for Problem 3.49.
106  CHAPTER 3  VECTOR CALCULUS
Evaluate the following integrals:
(a)  eL Q # dl, where L is the circular edge of the volume in the form of an ice cream cone
shown in Figure 3.32.
(b)  eS1 1= 3 Q2 # dS, where S1 is the top surface of the volume
(c)  eS2 1= 3 Q2 # dS, where S2 is the slanting surface of the volume
(d)  eS1 Q # dS
(e)  eS2 Q # dS
(f)  ev = # Q dv
How do your results in parts (a) to (f) compare?
*3.50	 A rigid body spins about a fixed axis through its center with angular velocity . If u is
the velocity at any point in the body, show that v 5 1/2 = 3 u.
3.51	 Given that H 5 2xzax 1 5xyzay 1 8(y + z)az, find (a) = ? H (b) = 3 H.
3.52	 Let B 5 r2ar 1 4r cos 2uau. Find the divergence and curl of B.
3.53	 For a vector field A and a scalar field V, show in Cartesian coordinates that
(a)  = # 1V = V2 5 V =2 V 1 0 = V 0 2
(b)  = 3 1VA2 5 V = 3 A 1 =V 3 A
3.54	 If B 5 x2yax 1 (2x2 1 y)ay 2 (y 2 z)az, find
(a)  =  B
(b)  = 3 B
(c)  = (=  B)
(d)  = 3 = 3 B
Section 3.8—Laplacian of a Scalar
3.55	 Find 2V for each of the following scalar fields:
(a)  V1 5 x3 1 y3 1 z3
(b)  V2 5 rz2 sin 2f
(c)  V3 5 r211 1 cos u sin f2
3.56	 Find the Laplacian of the following scalar fields and compute the value at the specified
point.
(a)  U 5 x3y2exz, 11, 21, 12
(b)  V 5 r2z1cos f 1 sin f2, 15, p/6, 222
(c)  W 5 e2r sin u cos f, 11, p/3, p/62
Problems  107
3.57	 If r 5 xax 1 yay 1 zaz is the position vector of point 1x, y, z2, r 5 0 r 0 , show that:
(a)  =1ln r2 5 r
(b)  =21ln r2 5 1
3.58
(a)  If U(x, y, z) 5 xy2z3, find =U and =2U.
(b)  If V(r, f, z) 5 sin f
r , find =V and =2V.
(c)  If W(r, u, f,) 5 r2 sin u cos f, find =W and =2W.
3.59	 Given that V 5 r2z cos f, find =V and =2V.
3.60	 If V 5 5 cos f
, find: (a) =V, (b) = # =V, (c) = 3 =V.
3.61	 Let U 5 4xyz2 1 10yz. Show that =2U 5 =  =U.
*3.62	 In cylindrical coordinates,
If G 5 2r sin far 1 4r cos faf 1 1z2 1 12raz, find =2G.
3.63	 According to eq. (3.64), = 3 (= 3 A) 5 = (=  A) 2 =2A. Show that
A 5 xzax 1 z2ay 1 yzaz satisfies this vector identity.
Section 3.9—Classification of Vector Fields
3.64	 Consider the following vector fields:
A 5 xax 1 yay 1 zaz
B 5 2r cos far 2 4r sin faf 1 3az
C 5 sin ar 1 r sin af
Which of these fields are (a) solenoidal and (b) irrotational?
3.65	 Given the vector field
G 5 116xy 2 z2ax 1 8x2ay 2 xaz
(a)  Is G irrotational (or conservative)?
(b)  Find the net flux of G over the cube 0 , x, y, z , 1.
(c)  Determine the circulation of G around the edge of the square z 5 0, 0 , x, y , 1.
Assume anticlockwise direction.
=2A 5 a=2Ar 2 2
'Af
'f 2
r2 bar 1 a=2Af 1 2
'Ar
'f  2
r2 baf 1 =2Azaz
108  CHAPTER 3  VECTOR CALCULUS
3.66	 The electric field due to a line charge is given by
E 5
2pPr ar
where l is a constant. Show that E is solenoidal. Show that it is also conservative.
3.67	 A vector field is given by H 5 10
ar. Show that C
H #  dI = 0 for any closed path L.
3.68	 Show that the vector field B = (3x2z 1 y2)ax 1 2xyay + x3az is conservative.
3.69	 Show that the vector field D = (3r 1 1) sin faz is solenoidal.
3.70	 The field of an electric dipole is given by
E 5 k
(2cosuar 1 sinuau2
where k is a constant. Show that E is conservative.

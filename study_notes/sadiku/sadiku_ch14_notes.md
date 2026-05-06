# Sadiku《Elements of Electromagnetics》Chapter 14

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 784-833 of 926 (926 total)

---

## Numerical Methods

757
C H A P T E R
757
14.1  INTRODUCTION
In the preceding chapters we considered various analytic techniques for solving EM prob­
lems and obtaining solutions in closed form. A closed-form solution is one in the form of
an explicit, algebraic equation in which values of the problem parameters can be substi­
tuted. Some of these analytic solutions were obtained assuming certain situations, thereby
making the solutions applicable to those idealized situations. For example, in deriving the
formula for calculating the capacitance of a parallel-plate capacitor, we assumed that the
fringing effect was negligible and that the separation distance was very small compared
with the width and length of the plates. Also, our application of Laplace’s equation in
Chapter 6 was restricted to problems with boundaries coinciding with coordinate surfaces.
Analytic solutions have an inherent advantage of being exact. They also make it easy to
observe the behavior of the solution when there is variation in the problem parameters.
However, analytic solutions are available only for problems with simple configurations.
When the complexities of theoretical formulas make analytic solution intractable, we
resort to nonanalytic methods, which include (1) graphical methods, (2) experimental
methods, (3) analog methods, and (4) numerical methods. Graphical, experimental, and
analog methods are applicable to solving relatively few problems. Numerical methods have
come into prominence and have become more attractive with the advent of fast digital
computers. The three most commonly used simple numerical techniques in EM are the
moment method, the finite difference method, and the finite element method. Most EM
problems involve either partial differential equations or integral equations. Partial differen­
tial equations are usually solved by using the finite difference method or the finite element
method; integral equations are solved conveniently by using the moment method. Although
numerical methods give ­approximate solutions, the solutions are sufficiently ­accurate for
engineering purposes. We should not get the impression that analytic techniques are out­
dated because of numerical methods; rather, they are complementary. As will be observed
later, every numerical method involves analytic simplification until the method can be easily
applied.
The MATLAB codes developed for computer implementation of the concepts
developed in this chapter are simplified and self-explanatory for instructional purposes.
(Appendix C provides a short tutorial on MATLAB.) The notations used in the programs
NUMERICAL METHODS
Young men think old men are fools, but old men know young men are fools.
—GEORGE CHAPMAN
758  CHAPTER 14  NUMERICAL METHODS
are as close as possible to those used in the main text; some are defined wherever neces­
sary. These programs are by no means unique; there are several ways of writing a computer
program. Therefore, users may decide to modify the programs to suit their objectives.
†14.2  FIELD PLOTTING
In Section 4.9, we used field lines and equipotential surfaces for visualizing an electrostatic
field. However, the graphical representations in Figure 4.21 for electrostatic fields and in
Figures 7.8(b) and 7.16 for magnetostatic fields are very simple, trivial, and qualitative.
Accurate pictures of more complicated charge distributions would be more helpful. This
section presents a numerical technique that may be developed into an interactive computer
program. It generates data points for electric field lines and equipotential lines for arbitrary
configuration of point sources.
Electric field lines and equipotential lines can be plotted for coplanar point sources
with simple programs. Suppose we have N point charges located at position vectors
r1, r2, .  .  . , rN, the electric field intensity E and potential V at position vector r are given,
respectively, by
E 5 a
k51
Qk 1r 2 rk2
4pe 0 r 2 rk 0 3
(14.1)
and
V 5 a
k51
4pe 0 r 2 rk 0 
(14.2)
If the charges are on the same plane 1z 5 constant2, eqs. (14.1) and (14.2) become
E 5 a
k51
Qk3 1x 2 xk2ax 1 1y 2 yk2ay4
4pe3 1x 2 xk2 2 1 1 y 2 yk2 243/2
(14.3)
V 5 a
k51
4pe3 1x 2 xk2 2 1 1 y 2 yk2 241/2
(14.4)
To plot the electric field lines, follow these steps:
1.	 Choose a starting point on the field line.
2.	 Calculate Ex and Ey at that point using eq. (14.3).
3.	 Take a small step along the field line to a new point in the plane. As shown in
­Figure 14.1, a movement D along the field line corresponds to movements Dx and Dy
in the x- and y-directions, respectively. From Figure 14.1, it is evident that
D, 5 Ex
E 5
3Ex
2 1 Ey
241/2
14.2 Field Plotting  759
Dx 5
D, # Ex
3Ex
2 1 Ey
241/2
(14.5)
Similarly,
Dy 5
D, # Ey
3Ex
2 1 Ey
241/2
(14.6)
Move along the field line from the old point 1x, y2 to a new point xr 5 x 1 Dx,
yr 5 y 1 Dy.
4.	 Go back to steps 2 and 3 and repeat the calculations. Continue to generate new
points until a line is completed within a given range of coordinates. On ­completing
the line, go back to step 1 and choose another starting point. Note that since there
are an infinite number of field lines, any starting point is likely to be on a field line.
The points generated can be plotted by a plotter as illustrated in ­Figure 14.2.
To plot the equipotential lines, follow these steps:
1.	 Choose a starting point.
2.	 Calculate the electric field 1Ex, Ey2 at that point by using eq. (14.3).
3.	 Move a small step along the line perpendicular to the E-field line at that point.
Utilize the fact that if a line has slope m, a perpendicular line must have slope
21/m. Since an E-field line and an equipotential line meeting at a given point are
mutually ­orthogonal there,
Dx 5
2D, # Ey
3Ex
2 1 Ey
241/2
(14.7)
Dy 5
D, # Ex
3Ex
2 1 Ey
241/2
(14.8)
move along the equipotential line from the old point 1x, y2 to a new point
1x 1 Dx, y 1 Dy2. As a way of checking the new point, calculate the potential at
FIGURE 14.1  A small displacement on a field line.
760  CHAPTER 14  NUMERICAL METHODS
the new and old points using eq. (14.4); the potentials must be equal because the
points are on the same equipotential line.
4.	 Go back to steps 2 and 3 and repeat the calculations. Continue to generate new
points until a line is completed within the given range of x and y. After completing
the line, go back to step 1 and choose another starting point. Join the points gener­
ated by a plotter as illustrated in Figure 14.2.
By following the same reasoning, we can use the Biot–Savart law to plot the magnetic
field line due to various current distributions. Programs for determining the magnetic field
line due to line current, a current loop, a Helmholtz pair, and a solenoid can be developed.
Programs for drawing the electric and magnetic field lines inside a rectangular waveguide
or the power radiation pattern produced by a linear array of vertical half-wave electric
dipole antennas can also be written.
Write a program to plot the electric field and equipotential lines due to:
(a)  Two point charges Q and 24Q, located at 1x, y2 5 121, 02 and 11, 02, respectively.
(b)  Four point charges Q, 2Q, Q, and 2Q, located at 1x, y2 5 121, 212, 11, 212,
11, 12, and 121, 12, respectively. Take Q/4pe 5 1 and D, 5 0.1. Consider the range
25 , x , 5, 2 5 , y , 5.
Solution:
Based on the steps given in Section 14.2, the program in Figure 14.3 was developed.
Enough comments are inserted to make the program as self-explanatory as possible. For
example, to use the program to generate the plot in Figure 14.4(a), load program plotit in
your MATLAB directory. At the command prompt in MATLAB, type
plotit 1 31 244, 321 0; 1 04, 1, 1, 0.1, 0.01, 8, 2, 5)
where the numbers have meanings provided in the program. Further explanation of the
program is provided in the following paragraphs.
FIGURE 14.2  Generated points on E-field lines
(shown thick) and equipotential lines (dotted).
EXAMPLE 14.1
Since the E-field lines emanate from positive charges and terminate on negative
charges, it seems reasonable to generate starting points 1xs, ys2 for the E-field lines on small
circles centered at charge locations 1xQ, yQ2; that is,
xs 5 xQ 1 r cos u
(14.1.1a)
ys 5 yQ 1 r sin u
(14.1.1b)
function plotit(charges,location,ckEField,ckEq,DLE,DLV,NLE,NLV,PTS)
figure;
hold on;
% Program for plotting the electric field lines
% and equipotential lines due to coplanar point charges
% the plot is to be within the range -5<x,y<5
% This is the correct usage:
% function plotit(charges,location,ckEField,ckEq,DLE,DLV,NLE,NLV,PTS)
% where,
%    charges = a vector containing the charges
%   location = a matrix where each row is a charge location
%   ckEField = Flag set to 1 plots the Efield lines
%       ckEq = Flag set to 1 plots the Equipotential lines
% DLE or DLV = the increment along E & V lines
%        NLE = No. of E-Field lines per charge
%        NLV = No. of Equipotential lines per charge
%        PTS => Plots every PTS point (i.e. if PTS = 5 then plot
every 5th point)
% note that constant Q/4*Pie*ErR is set equal to 1.0
% Determine the E-Field LInes
% For convenience, the starting points (XS,YS) are radially
distributed about charge locations
Q=charges;
XQ = location(:,1);
YQ = location(:,2);
JJ=1;
NQ = length(charges);
if (ckEField)
for K=1:NQ
for I =1:NLE
THETA = 2*pi*(I-1)/(NLE);
XS=XQ(K) + 0.1*cos(THETA);
YS=YQ(K) + 0.1*sin(THETA);
XE=XS;
YE=YS;
JJ=JJ+1;
if (~mod(JJ,PTS))
FIGURE 14.3  Computer program for Example 14.1.
14.2 Field Plotting  761
762  CHAPTER 14  NUMERICAL METHODS
plot (XE,YE);
end
while(1)
% FIND INCREMENT AND NEW POINT (X,Y)
EX=0;
EY=0;
for J=1:NQ
R =sqrt((XE-XQ(J))^2 + (YE - YQ(J))^2);
EX = EX +Q(J)*(XE-XQ(J))/(R^3);
EY = EY +Q(J)*(YE-YQ(J))/(R^3);
end
E = sqrt(EX^2 + EY^2);
% CHECK FOR A SINGULAR POINT
if (E <=.00005)
break;
end
DX = DLE*EX/E;
DY = DLE*EY/E;
% FOR NEGATIVE CHARGE, NEGATE DX & DY SO THAT INCREMENT
% IS AWAY FROM THE CHARGE
if (Q(K) < 0)
DX = -DX;
DY = -DY;
end
XE = XE + DX;
YE = YE + DY;
% CHECK WHETHER NEW POINT IS WITHIN THE GIVEN RANGE OR
TOO
% CLOSE TO ANY OF THE POINT CHARGES - TO AVOID SINGULAR
POINT
if ((abs(XE) >= 5) | (abs(YE) >= 5))
break;
end
if (sum(abs(XE-XQ) < .05 & abs(YE-YQ) < .05) >0)
break;
end
JJ=JJ+1;
if (~mod(JJ,PTS))
plot (XE,YE);
end
end % while loop
end % I =1:NLE
end   % K = 1:NQ
end % if
% NEXT, DETERMINE THE EQUIPOTENTIAL LINES
% FOR CONVENIENCE, THE STARTING POINTS (XS,YS) ARE
% CHOSEN LIKE THOSE FOR THE E-FIELD LINES
if (ckEq)
FIGURE 14.3  (Continued)
JJ=1;
DELTA = .2;
ANGLE = 45*pi/180;
for K =1:NQ
FACTOR = .5;
for KK = 1:NLV
XS = XQ(K) + FACTOR*cos(ANGLE);
YS = YQ(K) + FACTOR*sin(ANGLE);
if ( abs(XS) >= 5 | abs(YS) >=5)
break;
end
DIR = 1;
XV = XS;
YV = YS;
JJ=JJ+1;
if (~mod(JJ,PTS))
plot(XV,YV);
end
% FIND INCREMENT AND NEW POINT (XV,YV)
N=1;
while (1)
EX = 0;
EY = 0;
for J = 1:NQ
R = sqrt((XV-XQ(J))^2 + (YV-YQ(J))^2);
EX = EX + Q(J)*(XV-XQ(J))/(R^3);
EY = EY + Q(J)*(YV-YQ(J))/(R^3);
end
E=sqrt(EX^2 + EY^2);
if (E <= .00005)
FACTOR = 2*FACTOR;
break;
end
DX = -DLV*EY/E;
DY = DLV*EX/E;
XV = XV + DIR*DX;
YV = YV + DIR*DY;
% CHECK IF THE EQUIPOTENTIAL LINE LOOPS BACK TO (X,YS)
R0 = sqrt((XV - XS)^2 + (YV - YS)^2);
if (R0 < DELTA & N < 50)
FACTOR = 2*FACTOR;
break;
end
% CHECK WHETHER NEW POINT IS WITHIN THE GIVEN RANGE
% IF FOUND OUT OF RANGE, GO BACK TO THE STARTING POINT
% (XS,YS)BUT INCREMENT IN THE OPPOSITE DIRECTION
if (abs(XV) > 5 | abs(YV) > 5)
DIR = DIR -2;
XV = XS;
FIGURE 14.3  (Continued)
14.2 Field Plotting  763
764  CHAPTER 14  NUMERICAL METHODS
YV = YS;
if (abs(DIR) > 1)
FACTOR = 2*FACTOR;
break;
end
else
if (sum(abs(XV-XQ) < .005 & abs(YV-YQ) < .005) >0)
break;
end
end
JJ=JJ+1;
if (~mod(JJ,PTS))
N=N+1;
plot(XV,YV);
end
end % WHILE loop
end  % KK
end   % K
end % if
(a)
(b)
FIGURE 14.4  For Example 14.1;
plots of E-field lines and equipo­
tential lines due to (a) two point
charges and (b) four point charges
(a two-dimensional qua­drupole).
where r is the radius of the small circle 1e.g., r 5 0.1 or 0.052, and u is a prescribed angle
chosen for each E-field line. The starting points for the equipotential lines can be generated
in different ways: along the x- and y-axes, along line y 5 x, and so on. However, to make
the program as general as possible, the starting points should depend on the charge loca­
tions like those for the E-field lines. They could be chosen by using eq. (14.1.1) but with
fixed u (e.g., 45°) and variable r (e.g., 0.5, 1.0, 2.0,  .  .  .).
The value of incremental length D is crucial for accurate plots. Although the smaller
the value of D, the more accurate the plots, we must keep in mind that the smaller the
value of D, the more points we generate, and memory storage may be a problem. For
example, a line may consist of more than 1000 generated points. In view of the large num­
ber of points to be plotted, the points are usually stored in a data file and a graphics routine
is used to plot the data.
For both the E-field and equipotential lines, different checks are inserted in the pro­
gram in Figure 14.3:
(a)	 Check for singular point (E = 0?).
(b)	 Check whether the point generated is too close to a charge location.
(c)	 Check whether the point is within the given range of 25 , x , 5, 2 5 , y , 5,
(d)	 Check whether the (equipotential) line loops back to the starting point.
The plot of the points generated for the cases of two point charges and four point
charges are shown in Figure 14.4(a) and (b), respectively.
PRACTICE EXERCISE  14.1
Write a complete program for plotting the electric field lines and equipotential lines
due to coplanar point charges. Run the program for N 5 3; that is, there are three
point charges 2Q, 1Q, and 2Q, located at 1x, y2 5 121, 02, 10, 12, and 11, 02, ­
respectively. Take Q/4pe 5 1, D, 5 0.1 or 0.01 for greater accuracy and limit your plot
to 25 , x , 5, 2 5 , y , 5.
Answer:  See Figure 14.5.
FIGURE 14.5  For Practice
Exercise 14.1.
14.2 Field Plotting  765
766  CHAPTER 14  NUMERICAL METHODS
The finite difference method1 (FDM) is a simple numerical technique used in solving prob­
lems like those solved analytically in Chapter 6. A problem is uniquely defined by three things:
1.	 A partial differential equation such as Laplace’s or Poisson’s equation
2.	 A solution region
3.	 Boundary and/or initial conditions
A finite difference solution to Poisson’s or Laplace’s equation, for example, proceeds in
three steps: (1) dividing the solution region into a grid of nodes, (2) approximating the
differential equation and boundary conditions by a set of linear algebraic equations (called
difference equations) on grid points within the solution region, and (3) solving this set of
algebraic equations.
Step 1: Suppose we intend to apply the finite difference method to determine the electric
potential in a region shown in Figure 14.6(a). The solution region is divided into rect­
angular meshes with grid points or nodes as in Figure 14.6(a). A node on the boundary
of the region where the potential is specified is called a fixed node (fixed by the prob­
lem), and interior points in the region are called free points (free in that the potential is
unknown).
Step 2: Our objective is to obtain the finite difference approximation to Poisson’s equation
and use this to determine the potentials at all the free points. We recall that Poisson’s equa­
tion is given by
=2V 5 2rv
e 
(14.9a)
1 For an extensive treatment of the finite difference method, see G. D. Smith, Numerical Solution of Partial
Differential Equations: Finite Difference Methods, 3rd ed. Oxford: Oxford Univ. Press, 1985.
FIGURE 14.6  Finite difference solution pattern: (a) division of the
­solution into grid points, (b) finite difference five-node molecule.
14.3  THE FINITE DIFFERENCE METHOD
14.3 The Finite Difference Method  767
For two-dimensional solution region such as in Figure 14.6(a), '2V
'z2 5 0, so
'2V
'x2 1 '2V
'y2 5 2rv
e 
(14.9b)
From the definition of the derivative of V1x, y2 at point 1xo, yo2,
Vr 5 'V
'x `
x5xo
V1xo 1 Dx, yo2 2 V1xo 2 Dx, yo2
2Dx
Vi11, j 2 Vi21, j
2 Dx
(14.10)
where Dx is a sufficiently small increment along x. For the second derivative, which is the
derivative of the first derivative V,
Vs 5 '2V
'x2  `
x5xo
5 'Vr
'x .
Vr1xo 1 Dx/2, yo2 2 Vr1xo 2 Dx/2, yo2
V1xo 1 Dx, yo2 2 2V1xo, yo2 1 V1xo 2 Dx, yo2
1Dx2 2
Vi11, j 2 2Vi, j 1 Vi21, j
1Dx2 2
(14.11)
Equations (14.10) and (14.11) are the finite difference approximations for the first and
­second partial derivatives of V with respect to x, evaluated at x 5 xo. The approximation
in eq. (14.10) is associated with an error of the order of the Dx while that of eq. (14.11) has
an associated error on the order of 1Dx2 2. Similarly,
'2V
'y2  `
y5yo
V1xo, yo 1 Dy2 2 2V1xo, yo2 1 V1xo, yo 2 Dy2
1Dy2 2
Vi, j11 2 2Vi, j 1 Vi, j21
1Dy2 2
(14.12)
Substituting eqs. (14.11) and (14.12) into eq. (14.9b) and letting Dx 5 Dy 5 h gives
Vi11, j 1 Vi21, j 1 Vi, j11 1 Vi, j21 2 4Vi, j 5 2h2rv
Vi, j 5 1
4 aVi11, j 1 Vi21, j 1 Vi, j11 1 Vi, j21 1 h2rv
e b
(14.13)
768  CHAPTER 14  NUMERICAL METHODS
where h is called the mesh size. Equation (14.13) is the finite difference approximation to Poisson’s
equation. If the solution region is charge free 1rv 5 02, eq. (14.9) becomes Laplace’s equation:
=2V 5 '2V
'x2 1 '2V
'y2 5 0
(14.14)
The finite difference approximation to this equation is obtained from eq. (14.13) by setting
rv 5 0; that is,
Vi, j 5 1
4 1Vi11, j 1 Vi21, j 1 Vi, j11 1 Vi, j212
(14.15)
This equation is essentially a five-node finite difference approximation for the potential at
the central point of a square mesh. Figure 14.6(b) illustrates what is called the finite differ­
ence five-node molecule. The molecule in Figure 14.6(b) is taken out of Figure 14.6(a). Thus
eq. (14.15) applied to the molecule becomes
Vo 5 1
4 1V1 1 V2 1 V3 1 V42
(14.16)
This equation clearly shows the average-value property of Laplace’s equation. In other
words, Laplace’s equation can be interpreted as a differential means of stating the fact that
the potential at a specific point is the average of the potentials at the neighboring points.
Step 3: To apply eq. (14.16) [or eq. (14.13)] to a given problem, one of the following two
methods is commonly used.
A.  Iteration Method
We start by setting initial values of the potentials at the free nodes equal to zero or to any
reasonable guessed value. Keeping the potentials at the fixed nodes unchanged at all times,
we apply eq. (14.16) to every free node in turn until the potentials at all free nodes have
been calculated. The potentials obtained at the end of this first iteration are just approxi­
mate. To increase the accuracy of the potentials, we repeat the calculation at every free
node, using old values to determine new ones. The iterative or repeated modification of the
potential at each free node is continued until a prescribed degree of accuracy is achieved or
until the old and the new values at each node are satisfactorily close.
B.  Band Matrix Method
Equation (14.16) applied to all free nodes results in a set of simultaneous equations of the form
3A4 3V4 5 3B4
(14.17)
where [A] is a sparse matrix (i.e., one having many zero terms), [V] consists of the
unknown potentials at the free nodes, and [B] is another column matrix formed by the
14.3 The Finite Difference Method  769
known potentials at the fixed nodes. Matrix [A] is also banded in that its nonzero terms
appear clustered near the main diagonal because only nearest neighboring nodes affect the
potential at each node. The sparse, band matrix is easily inverted to determine [V]. Thus
we obtain the potentials at the free nodes from matrix [V] as
3V4 5 3A421 3B4
(14.18)
The finite difference method can be applied to solve time-varying problems. For
example, consider the one-dimensional wave equation of eq. (10.1), then
Figure 14.7 are
Where Dx and Dt are increments along x and t. Inserting eqs. (14.20) and (14.21) in
eq. (14.19) and solvin
where
a 5 c u Dt
Dx d
(14.23)
FIGURE 14.7  Finite difference ­solution
pattern for the wave  equation: eq. (14.19).
u2 '2
'x2 5 '2
't2
(14.19)
'2
'x2  `
x5xo
i21, j 2 2i, j 1 i11, j
1Dx2 2
(14.20)
'2
't2  `
t5to
i, j21 2 2i, j 1 i, j11
1Dt2 2
(14.21)
i, j11 . a i21, j 1 i11, j2 1 211 2 a2 i, j 2 i, j21
(14.22)
g for i,j11 gives
where u is the wave velocity and F is the E- or H-field component of the EM wave. The
difference approximations of the derivatives at the 1xo, to2 or 1i, j2th node shown in
770  CHAPTER 14  NUMERICAL METHODS
It can be shown that for the solution in eq. (14.22) to be stable, a # 1. To start the finite
­difference algorithm in eq. (14.22), we use the initial conditions. We assume that at t 5 0,
be obtained directly from eq. (14.22). Note that the three methods discussed for solving
eq. (14.16) do not apply to eq. (14.22) because eq. (14.22) can be used directly with
eq. (14.25) as the starting formula. In other words, we do not have a set of simultaneous
equations; eq. (14.22) is an explicit formula.
The FDM concept can be extended to Poisson’s, Laplace’s, or wave equations in other
coordinate systems. The accuracy of the method depends on the fineness of the grid and
the amount of time spent in refining the potentials. We can reduce computer time and
increase the accuracy and convergence rate by the method of successive overrelaxation, by
making reasonable guesses at initial values, by taking advantage of symmetry if possible,
by making the mesh size as small as possible, and by using more complex finite difference
molecules. One limitation of the finite difference method is that interpolation of some
kind must be used to determine solutions at points not on the grid. One obvious way to
overcome this is to use a finer grid, but this requires a greater number of computations and
a larger amount of computer storage.
EXAMPLE 14.2
'i,0 /'t 5 0 and use (central) difference approximation (see Review Question 14.2) to get
With eq. (14.25) as the “starting” formula, the value of F at any point on the grid can
'i,0
i,1 2 i,21
2Dt
5 0
i,1 5 i,21
(14.24)
Substituting eq. (14.24) into eq. (14.22) and taking j 5 0 1t 5 02, we obtain
i,1 . a1i21,0 1 i11,02 1 211 2 a2i,0 2 i,1
i,1 . 1
2 3a1i21,0 1 i11,02 1 211 2 a2i,04
(14.25)
Solve the one-dimensional boundary-value problem 2s 5 x2, 0 # x # 1, subject to
102 5 0 5 112. Use the finite difference method.
Solution:
First, we obtain the finite difference approximation to the differential equation s 5 2x2,
which is Poisson’s equation in one dimension. Next, we divide the entire domain
0 # x # 1 into N equal segments each of length h 15 1/N2 as in Figure 14.8(a) so that
there are 1N 1 12 nodes.
2xo
2 5 d2
dx2  `
x5xo
. 1xo 1 h2 2 21xo2 1 1xo 2 h2
14.3 The Finite Difference Method
the degree of accuracy desired. For a one-dimensional problem such as this, ni 5 50 may
suffice. For two- or three-dimensional problems, larger values of ni would be required (see
later: Table 14.1). It should be noted that the values of F at end points (fixed nodes) are
held fixed. The solutions for N 5 4 and 10 are shown in Figure 14.10.
FIGURE 14.8  For Example 14.2.
Using this finite difference scheme, we obtain an approximate solution for various values
of N. The MATLAB code is shown in Figure 14.9. The number of iterations ni depends on
2xj
2 5
j11 2 2j 1 21
Thus
22j 5 2j
2h2 2 j11 2 j21
j 5 1
2 1j11 1 j21 1 xj
2 h22
We may compare this with the exact solution obtained as follows. Given that
d2/dx2 5 2x2, integrating twice gives
 5 2x4
12 1 Ax 1 B
where A and B are integration constants. From the boundary conditions,
102 5 0 S  B 5 0
112 5 0 S  0 5 2 1
12 1 A  or  A 5 1
Hence, the exact solution is  5 x11 2 x32/12, which is calculated in Figure 14.9 and
found to be very close to case N 5 10.
771
772  CHAPTER 14  NUMERICAL METHODS
% ONE-DIMENSIONAL PROBLEM OF EXAMPLE 14.2
% SOLVED USING FINITE DIFFERENCE METHOD
% h = MESH SIZE
% ni = NO. OF ITERATIONS DESIRED
P = [ ];
n=20;
ni=500;
1=1.0;
h = 1/n;
phi=zeros(n+1,1);
x=h*[0:n]’;
x1=x(2:n);
for k=1:ni
phi([2:n])=[phi(3:n+1)+phi(1:n-1)+x1.^2*h^2]/2;
end
%  CALCULATE THE EXACT VALUE ALSO
phiex=x.*(1.0-x.^3)/12.0;
diary a:test.out
[[1:n+1]’ phi phiex]
diary off
FIGURE 14.9  Computer program for Example 14.2.
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
FIGURE 14.10  For Example 14.2: plot of F(x). Continuous curve is for
N 5 10; dashed curve is for N 5 4.
14.3 The Finite Difference Method  773
Determine the potential at the free nodes in the potential system of Figure 14.11 using
the finite difference method.
Solution:
This problem will be solved by using the iteration method first, and then the band matrix
method.
Method 1 (Iteration Method):  We first set the initial values of the potential at the free
nodes equal to zero. We apply eq. (14.16) to each free node, using the newest surrounding
potentials each time the potential at that node is calculated. For the first iteration:
V1 5 1/410 1 20 1 0 1 02 5 5
V2 5 1/415 1 0 1 0 1 02 5 1.25
V3 5 1/415 1 20 1 0 1 02 5 6.25
V4 5 1/411.25 1 6.25 1 0 1 02 5 1.875
FIGURE 14.11  For Example 14.3.
EXAMPLE 14.3
PRACTICE EXERCISE  14.2
Solve the differential equation d2y/dx2 1 y 5 0 with the boundary conditions y102 5 0,
y112 5 1 by using the finite difference method. Take Dx 5 1/4.
Answer:  Compare your result with the exact solution y1x2 5 sin1x2
sin112 .
774  CHAPTER 14  NUMERICAL METHODS
and so on. To avoid confusion, each time a new value at a free node is calculated, we cross out the
old value as shown in Figure 14.12. After V8 is calculated, we start the second iteration at node 1:
V1 5 1/410 1 20 1 1.25 1 6.252 5 6.875
V2 5 1/416.875 1 0 1 0 1 1.8752 5 2.187
and so on. If this process is continued, we obtain the uncrossed values shown in Figure 14.12
after five iterations. After 10 iterations (not shown in Figure 14.12), we obtain
V1 5 10.04,  V2 5 4.956,  V3 5 15.22,  V4 5 9.786
V5 5 21.05,  V6 5 18.97,  V7 5 15.06,  V8 5 11.26
Method 2 (Band Matrix Method):  This method reveals the sparse structure of the
­problem. We apply eq. (14.16) to each free node and keep the known terms (prescribed
FIGURE 14.12  For Example 14.3; the values not crossed out are the
solutions after five iterations.
14.3 The Finite Difference Method  775
potentials at the fixed nodes) on the right side; the unknown terms (potentials at free
nodes) are on the left side of the resulting system of simultaneous equations, which will be
expressed in matrix form as 3A4 3V4 5 3B4.
For node 1,
24V1 1 V2 1 V3 5 220 2 0
For node 2,
V1 1 4V2 1 V4 5 20 2 0
For node 3,
V1 2 4V3 1 V4 1 V5 5 220
For node 4,
V2 1 V3 2 4V4 1 V6 5 20
For node 5,
V3 2 4V5 1 V6 5 220 2 30
For node 6,
V4 1 V5 2 4V6 1 V7 5 230
For node 7,
V6 2 4V7 1 V8 5 230 2 0
For node 8,
V7 2 4V8 5 20 2 0 2 30
Note that since we are using a five-node molecule, we have five terms at each node. The
eight equations obtained are put in matrix form as
X H
X 5 H
220
220
250
230
230
230
3A4 3V4 5 3B4
776  CHAPTER 14  NUMERICAL METHODS
where [A] is the band, sparse matrix, [V] is the column matrix consisting of the unknown
potentials at the free nodes, and [B] is the column matrix formed by the potential at the
fixed nodes. The “band” nature of [A] is shown by the dotted loop.
Notice that matrix [A] could have been obtained directly from Figure 14.11 without writ­
ing down eq. (14.16) at each free node. To do this, we simply set the diagonal (or self) terms
Aii 5 24 and set Aij 5 1 if i and j nodes are connected or Aij 5 0 if i and j nodes are not
directly connected. For example, A23 5 A32 5 0 because nodes 2 and 3 are not connected,
whereas A46 5 A64 5 1 because nodes 4 and 6 are connected. Similarly, matrix [B] is obtained
directly from Figure 14.11 by setting Bi equal to minus the sum of the potentials at fixed nodes
connected to node i. For example, B5 5 2120 1 302 because node 5 is connected to two fixed
nodes with potentials 20 V and 30 V. If node i is not connected to any fixed node, Bi 5 0.
By using MATLAB to invert matrix [A], we obtain
3V4 5 3A421 3B4
V1 5 10.04,  V2 5 4.958,  V3 5 15.22,  V4 5 9.788
V5 5 21.05,  V6 5 18.97,  V7 5 15.06,  V8 5 11.26
which compares well with the result obtained by means of the iteration method.
PRACTICE EXERCISE  14.3
Use the iteration method to find the finite difference approximation to the potentials at
points a and b of the system in Figure 14.13.
Answer:  Va = 10.135 V, Vb = 28.378 V.
FIGURE 14.13  For Practice Exercise 14.3.
14.3 The Finite Difference Method  777
Obtain the solution of Laplace’s equation for an infinitely long trough whose rectangu­
lar cross section is shown in Figure 14.14. Let V1 5 10 V, V2 5 100 V, V3 5 40 V, and
V4 5 0 V.
Solution:
We shall solve this problem by using the iteration method. In this case, the solution region
has a regular boundary. We can easily write a program to determine the potentials at the
grid points within the trough. We divide the region into square meshes. If we decide to
use a 15 3 10 grid, the number of grid points along x is 15 1 1 5 16 and the number of
grid points along y is 10 1 1 5 11. The mesh size h 5 1.5/15 5 0.1 m. The 15 3 10 grid
is illustrated in Figure 14.15. The grid points are numbered 1i, j2 starting from the lower
left-hand corner of the trough. The computer program in Figure 14.16, for determining the
potential at the free nodes, was developed by applying eq. (14.15) and using the iteration
method. At points 1x, y2 5 10.5, 0.52, 10.8, 0.82, 11.0, 0.52, and 10.8, 0.22 corresponding
to 1i, j2 5 15, 52, 18, 82, 110, 52, and 18, 22, respectively, the potentials after 50, 100, and
200 iterations are shown in Table 14.1. The exact values obtained by using the method
of separation of variables and a program similar to that of Figure 6.11 are also shown. It
should be noted that the degree of accuracy depends on the mesh size h. It is always desir­
able to make h as small as possible. Also note that the potentials at the fixed nodes are held
constant throughout the calculations.
EXAMPLE 14.4
FIGURE 14.14  For Example 14.4.
FIGURE 14.15  For Example 14.4;
a 15 3 10 grid.
778  CHAPTER 14  NUMERICAL METHODS
%   USING FINITE DIFFERENCE (ITERATION) METHOD
%   THIS PROGRAM SOLVES THE TWO-DIMENSIONAL BOUNDARY-VALUE
%   PROBLEM (LAPLACE’S EQUATION) SHOWN IN FIG. 14.14.
%   ni = NO. OF ITERATIONS
%   nx = NO. OF X GRID POINTS
%   ny = NO. OF Y GRID POINTS
%   v(i,j) = POTENTIAL AT GRID POINT (i,j) OR (x,y) WITH
%   NODE NUMBERING STARTING FROM THE LOWER LEFT-HAND
%   CORNER OF THE TROUGH
v1 = 10.0;
v2 = 100.0;
v3 = 40.0;
v4 = 0.0;
ni = 200;
nx = 16;
ny = 11;
% SET INITIAL VALUES EQUAL TO ZEROES
v = zeros(nx,ny);
% FIX POTENTIALS ARE FIXED NODES
for i=2:nx-1
v(i,1) = v1;
v(i,ny) = v3;
end
for j=2:ny-1
v(1,j) = v4;
v(nx,j) = v2;
end
v(1,1) = 0.5*(v1 + v4);
v(nx,1) = 0.5*(v1 + v2);
v(1,ny) = 0.5*(v3 + v4);
v(nx,ny) = 0.5*(v2 + v3);
% NOW FIND v(i,j) USING EQ. (14.15) AFTER ni ITERATIONS
for k=1:ni
for i=2:nx-1
for j=2:ny-1
v(i,j) = 0.25*( v(i+1,j) + v(i-1,j) + v(i,j+1) + v(i,j-1) );
end
end
end
diary a:test1.out
[v(6,6), v(9,9), v(11,6), v(9,3)]
[ [1:nx, 1:ny] v(i,j) ]
diary off
FIGURE 14.16  Computer program for Example 14.4.
14.4 The Moment Method  779
PRACTICE EXERCISE  14.4
Consider the trough of Figure 14.17. Use a five-node finite difference scheme to find
the potential at the center of the trough using (a) a 4 3 8 grid, and (b) a 12 3 24 grid.
Answer:  (a) 31.08 V,  (b) 42.86 V.
TABLE 14.1  Solution of Example 14.4 (Iteration
Method) at Selected Points
Number of Iterations
Coordinates
(x, y)
100
200
Exact Value
(0.5, 0.5)
20.91
22.44
22.49
22.44
(0.8, 0.8)
37.7
38.56
38.59
38.55
(1.0, 0.5)
41.83
43.18
43.2
43.22
(0.8, 0.2)
19.87
20.94
20.97
20.89
FIGURE 14.17  For Practice Exercise 14.4.
2 The term “moment method” was first used in the Western literature by Harrington. For further ­exposition on
the method, see R. F. Harrington, Field Computation by Moment Methods. New York: IEEE Press, 1993.
14.4  THE MOMENT METHOD
Like the finite difference method, the moment method,2 or the method of moments
(MOM), has the advantage of being conceptually simple. While the finite difference
method is used in solving differential equations, the moment method is commonly used
in solving integral equations.
780  CHAPTER 14  NUMERICAL METHODS
For example, suppose we want to apply the moment method to solve Poisson’s
­equation in eq. (14.9a). It can be shown that an integral solution to Poisson’s equation is
V 5 3
rv dv
4per
(14.26)
We recall from Chapter 4 that eq. (14.26) can be derived from Coulomb’s law. We also recall
that given the charge distribution rv1x, y, z2, we can always find the potential V1x, y, z2,
the electric field E1x, y, z2, and the total charge Q. If, on the other hand, the potential V is
known and the charge distribution is unknown, how do we determine rv from eq. (14.26)?
In that situation, eq. (14.26) becomes what is called an integral equation.
An integral equation is one involving the unknown function under the integral sign.
It has the general form of
V1x2 5 3
K1x, t2 r1t2 dt
(14.27)
where the functions K1x, t2 and V1t2 and the limits a and b are known. The unknown
function r1t2 is to be determined; the function K1x, t2 is called the kernel of the equation.
The moment method is a common numerical technique used in solving integral equations
such as in eq. (14.27). The method is probably best explained with an example.
Consider a thin conducting wire of radius a, length L1L W a2 located in free space
as shown in Figure 14.18. Let the wire be maintained at a potential of Vo. Our goal is to
determine the charge density rL along the wire by using the moment method. Once we have
determined rL, related field quantities can be found. At any point on the wire, eq. (14.26)
reduces to an integral equation of the form
Vo 5 3
rL dl
4peor
(14.28)
FIGURE 14.18  Thin conducting wire held
at a constant potential.
14.4 The Moment Method  781
Since eq. (14.28) applies for observation points everywhere on the wire, at a fixed point yk
known as the match point.
Vo 5
4peo
rL1y2 dy
0 yk 2 y 0 
(14.29)
We recall from calculus that integration is essentially finding the area under a curve. If Dy
is small, the integration of f(y) over 0 , y , L is given by
f1y2 dy . f1y12 Dy 1 f1y22 Dy 1 . . . 1 f1yN2Dy
5 a
k51
f1yk2Dy
(14.30)
where the interval L has been divided into N units, each having length Dy. With the wire
divided into N segments of equal length D as shown in Figure 14.19, eq. (14.29) becomes
4peoVo .
r1 D
0 yk 2 y1 0 1
r2 D
0 yk 2 y2 0 1 . . . 1
rN D
0 yk 2 yN 0 
(14.31)
where D 5 L/N 5 Dy. The assumption in eq. (14.31) is that the unknown charge ­density
rk on the kth segment is constant on that segment. The kth term in eq. (14.31) has
|yk – yk| in the denominator and causes numerical problems. We shall soon circumvent this
problem by modeling the line ­segment by means of a cylindrical surface charge. Thus in
eq. (14.31), we have unknown constants r1, r2, .  .  . , rN. Since eq. (14.31) must hold at all
points on the wire, we obtain N ­similar equations by choosing N match points at y1, y2, . . . ,
yk, . . . , yN on the wire. Thus we obtain
4peoVo 5
r1 D
0 y1 2 y1 0 1
r2 D
0 y1 2 y2 0 1 . . . 1
rND
0 y1 2 yN 0 
(14.32a)
4peoVo 5
r1 D
0 y2 2 y1 0 1
r2 D
0 y2 2 y2 0 1 . . . 1
rND
0 y2 2 yN 0 
(14.32b)
4peoVo 5
r1 D
0 yN 2 y1 0 1
r2 D
0 yN 2 y2 0 1 . . . 1
rND
0 yN 2 yN 0
(14.32c)
The idea of matching the left-hand side of eq. (14.29) with the right-hand side of the equa­
tion at the match points is similar to the concept of taking moments in mechanics. Here
lies the reason this technique is called the moment method. Notice from Figure 14.19 that
the match points y1, y2, . . . , yN are placed at the center of each segment. Equation (14.32)
can be put in matrix form as
3B4 5 3A4 3r4
(14.33)
782  CHAPTER 14  NUMERICAL METHODS
where
3B4 5 4peoVo F
(14.34)
3A4 5 F
A11
A12
. . .
A1N
A21
A22
. . .
A2N
AN1
AN2
. . .
ANN
(14.35a)
Amn 5
0 ym 2 yn 0 ,  m 2 n
(14.35b)
3r4 5 F
(14.36)
In eq. (14.33), [r] is the matrix whose elements are unknown. We can determine [r] from
eq. (14.33) by using Cramer’s rule, matrix inversion, or the Gaussian elimination technique.
With matrix inversion,
3r4 5 3A421 3B4
(14.37)
FIGURE 14.19  Division of the wire into N segments.
14.4 The Moment Method  783
where 3A421 is the inverse of matrix [A]. In evaluating the diagonal elements (or self terms)
of matrix [A] in eq. (14.35), caution must be exercised. Since the wire is conducting, a
surface charge density rS is expected over the wire surface. Hence at the center of each
segment,
V 1center2 5
4peo
D/2
2D/2
rSa df dy
3a2 1 y241/2
5 2parS
4peo
ln e D/2 1 3 1D/22 2 1 a241/2
2D/2 1 3 1D/22 2 1 a241/2 f
Assuming D W a,
V 1center2 5 2parS
4peo
2 ln aD
a b
(14.38)
5 2rL
4peo
ln aD
a b
where rL 5 2p arS. Thus, the self terms 1m 5 n2 are
Ann 5 2 ln aD
a b
(14.39)
Equation (14.33) now becomes
ln aD
a b
0 y1 2 y2 0
. . .
0 y1 2 yN 0
0 y2 2 y1 0
2 ln aD
a b
. . .
0 y2 2 yN 0
0 yN 2 y1 0
0 yN 2 y2 0
. . .
2 ln aD
a b
Y F
V 5 4peoVo F
(14.40)
Using eq. (14.37) with eq. (14.40) and letting Vo 5 1 V, L 5 1 m, a 5 1 mm, and
N 5 20 1D 5 L/N2, a MATLAB code such as in Figure 14.20 can be developed. The pro­
gram in Figure 14.20 is self-explanatory. It inverts matrix [A] and plots rL against y. The
plot is shown in Figure 14.21. The program also determines the total charge on the wire
using
Q 5 3 rL dl
(14.41)
784  CHAPTER 14  NUMERICAL METHODS
%  THIS PROGRAM DETERMINES THE CHARGE DISTRIBUTION
%  ON A CONDUCTING THIN WIRE, OF RADIUS AA AND
%  LENGTH L, MAINTAINED AT VO VOLT
%  THE WIRE IS LOCATED AT 0 < Y < L
%  ALL DIMENSIONS ARE IN S.I. UNITS
%  MOMENT METHOD IS USED
%  N IS THE NO. OF SEGMENTS INTO WHICH THE WIRE IS DIVIDED
%  RHO IS THE LINE CHARGE DENSITY, RHO = INV(A)*B
%  FIRST, SPECIFY PROBLEM PARAMETERS
ER = 1.0;
EO = 8.8541e-12;
VO = 1.0;
AA = 0.001;
L = 1.0;
N = 20;
DELTA = L/N;
%  SECOND, CALCULATE THE ELEMENTS OF THE COEFFICIENT
%  MATRIX A
I=1:N;
Y=DELTA*(I-O.5);
for i=1:N
for j=1:N
if(i ~=j)
A(i,j)=DELTA/abs(Y(i)-Y(j));
else
A(i,j)=2.0*log(DELTA/AA);
end
end
end
%  NOW DETERMINE THE MATRIX OF CONSTANT VECTOR B
%  AND FIND Q
B = 4.0*pi*EO*ER*VO*ones(N,1);
C = inv(A);
RHO = C*B;
SUM = 0.0;
for I=1:N
SUM = SUM + RHO(I);
end
Q=SUM*DELTA;
diary  a:exam145a.out
[EO,Q]
[ [1:N]’ Y’ RHO ]
diary off
%  FINALLY PLOT RHO AGAINST Y
plot(Y,RHO)
xlabel(‛y (m)’), ylabel(‛rho_L (pC/m)’)
FIGURE 14.20  MATLAB code for calculating the charge distribution on the wire in Figure 14.18.
14.4 The Moment Method  785
which can be written in discrete form as
Q 5 a
k51
rk D
(14.42)
With the chosen parameters, the value of the total charge was found to be Q 5 8.5793 pC.
If desired, the electric field at any point can be calculated by using
E 5 3 rL dl
4peoR2 aR
(14.43)
which can be written as
E 5 a
k51
rk D R
4peoR3
(14.44)
where R 5 0 R 0  and
R 5 r 2 rk 5 1x 2 xk2ax 1 1y 2 yk2ay 1 1z 2 zk2az
r 5 1x, y, z2 is the position vector of the observation point, and rk 5 1xk, yk, zk2 is that of
the source point.
Notice that to obtain the charge distribution in Figure 14.21, we have taken N 5 20. It
should be expected that a smaller value of N would give a less accurate result and a larger
value of N would yield a more accurate result. However, if N is too large, we may have the
computation problem of inverting the square matrix [A]. The capacity of the computing
facilities at our disposal can limit the accuracy of the numerical experiment.
8.5
0.1
L (pC/m)
0.2
0.3
0.4
0.5
y (m)
0.6
0.7
0.8
0.9
9.5
10.5
FIGURE 14.21  Plot of rL against y.
786  CHAPTER 14  NUMERICAL METHODS
Use the moment method to find the capacitance of the parallel-plate capacitor of
Figure 14.22. Take a 5 1 m, b 5 1 m, d 5 1 m, and er 5 1.0.
Solution:
Let the potential difference between the plates be Vo 5 2 V so that the top plate P1 is
maintained at 11 V while the bottom plate P2 is at 21 V. We would like to determine the
­surface charge density rS on the plates so that the total charge on each plate can be found as
Q 5 3 rS dS
Once Q is known, we can calculate the capacitance as
C 5 Q
5 Q
To determine rS by means of the moment method, we divide P1 into n subsections: DS1,
DS2, .  .  . , DSn and P2 into n subsections: DSn11, DSn12, . . . , DS2n. The potential Vi at the
center of a typical subsection DSi is
Vi 5 3
rS dS
4peoR . a
j51
4peo
DSi
rj dS
Rij
5 a
j51
rj 1
4peo
DSj
Rij
It has been assumed that there is uniform charge distribution on each subsection. The last
equation can be written as
Vi 5 a
j51
rj Aij
where
Aij 5
4peo
DSi
Rij
EXAMPLE 14.5
FIGURE 14.22  Parallel-plate
capacitor; for Example 14.5.
14.4 The Moment Method  787
Thus
V1 5 a
j51
rj A1j 5 1
V2 5 a
j51
rj A2j 5 1
Vn 5 a
j51
rj Anj 5 1
Vn11 5 a
j51
rj An11, j 5 21
V2n 5 a
j51
rj A2n, j 5 21
yielding a set of 2n simultaneous equations with 2n unknown charge densities rj. In matrix form,
A11
A12
. . .
A1,2n
A21
A22
. . .
A2,2n
A2n,1
A2n,2
. . .
A2n,2n
W G
r2n
W 5 G
3A4 3r4 5 3B4
Hence,
3r4 5 3A421 3B4
where [B] is the column matrix defining the potentials and [A] is a square matrix con-
taining elements Aij. To determine Aij, consider the two subsections i and j shown in
Figure 14.23 where the subsections could be on different plates or on the same plate.
Aij 5
4peo
y5y1
x5x1
dx dy
Rij
788  CHAPTER 14  NUMERICAL METHODS
where
Rij 5 3 1xj 2 xi2 2 1 1yj 2 yi2 2 1 1zj 2 zi2 241/2
For the sake of convenience, if we assume that the subsections are squares,
x2 2 x1 5 D, 5 y2 2 y1
it can be shown that
Aij 5
DSi
4peoRij
1D,2 2
4peoRij  i 2 j
and
Aii 5 D,
peo
ln11 1 "22 5 D,
peo
10.88142
With these formulas, the MATLAB code in Figure 14.24 was developed. With n 5 9,
C = 26.52 pF, with n 5 16, C 5 27.27 pF, and with n 5 25, C 5 27.74 pF.
%   USING THE METHOD OF MOMENT,
%   THIS PROGRAM DETERMINES THE CAPACITANCE OF A
%   PARALLEL-PLATE CAPACITOR CONSISTING OF TWO CONDUCTING
%   PLATES, EACH OF DIMENSION AA x BB, SEPARATED BY A
%   DISTANCE D, AND MAINTAINED AT 1 VOLT AND -1 VOLT
%   ONE PLATE IS LOCATED ON THE Z=0 PLANE WHILE THE OTHER
%   IS LOCATED ON THE Z=D PLANE
%   ALL DIMENSIONS ARE IN S.I. UNITS
%   N IS THE NUMBER IS SUBSECTIONS INTO WHICH EACH PLATE IS
DIVIDED
FIGURE 14.24  MATLAB program for Example 14.5.
FIGURE 14.23  Subsections i and j;
for Example 14.5.
14.4 The Moment Method  789
FIGURE 14.24  (Continued)
%   FIRST, SPECIFY THE PARAMETERS
ER = 1.0;
EO = 8.8541e-12;
AA = 1.0;
BB = 1.0;
D = 1.0;
N = 9;
NT = 2*N;
M = sqrt(N);
DX = AA/M;
DY = BB/M;
DL = DX;
%   SECOND, CALCULATE THE ELEMENTS OF THE COEFFICIENT
%   MATRIX A
K = 0;
for K1=1:2
for K2=1:M
for K3=1:M
K = K + 1;
X(K) = DX*(K2 - 0.5);
Y(K) = DY*(K3 - 0.5);
end
end
end
for K1=1:N
Z(K1) = 0.0;
Z(K1+N) = D;
end
for I=1:NT
for J=1:NT
if(I==J)
A(I,J) = DL*0.8814/(pi*EO);
else
R = sqrt( (X(I)-X(J))^2 + (Y(I)-Y(J))^2 + (Z(I)-Z(J))^2 );
A(I,J) = DL^2/(4.*pi*EO*R);
end
end
end
%  NOW DETERMINE THE MATRIX OF CONSTANT VECTOR B
for K=1:N
B(K) = 1.0;
B(K+N) = -1.0;
end
%  INVERT A AND CALCULATE RHO CONSISTING OF
%  THE UNKNOWN ELEMENTS
%  ALSO CALCULATE THE TOTAL CHARGE Q AND CAPACITANCE C
F = inv(A);
790  CHAPTER 14  NUMERICAL METHODS
FIGURE 14.25  Parallel conducting wires for Practice
­Exercise 14.5.
TABLE 14.2  Capacitance
for Practice Exercise 14.5
xo (m)
C (pF)
0.0
4.91
0.2
4.891
0.4
4.853
0.6
4.789
0.8
4.71
1.0
4.643
RHO = F*B’;
SUM = 0.0;
for I=1:N
SUM = SUM + RHO(I);
end
Q = SUM*(DL^2);
VO = 2.0;
C = abs(Q)/VO;
diary
[C]
[ [1:NT]’  X   Y’  Z’  RHO ]
diary off
PRACTICE EXERCISE  14.5
Use the moment method to write a program to determine the capacitance of two iden­
tical parallel conducting wires separated at a distance yo and displaced by xo as shown
in Figure 14.25. If each wire is of length L and radius a, find the capacitance for cases
xo 5 0, 0.2, 0.4, . . . , 1.0 m. Take yo 5 0.5 m, L 5 1 m, a 5 1 mm, er 5 1.
Answer:  For N 5 10 5 number of segments per wire, see Table 14.2.
14.5 The Finite Element Method  791
The finite element method (FEM) has its origin in the field of structural analysis. The
method was not applied to EM problems until 1968.3 Like the finite difference method,
the finite element method is useful in solving differential equations. As noticed in Section
14.3, the finite difference method represents the solution region by an array of grid points;
its application becomes difficult with problems having irregularly shaped boundaries. Such
problems can be handled more easily by using the finite element method.
The finite element analysis of any problem involves basically four steps: (a) discretizing
the solution region into a finite number of subregions or elements, (b) deriving governing
equations for a typical element, (c) assembling all the elements in the solution region, and
(d) solving the system of equations obtained.
A.  Finite Element Discretization
We divide the solution region into a number of finite elements as illustrated in Figure 14.26,
where the region is subdivided into four nonoverlapping elements (two triangular and two
quadrilateral) and seven nodes. We will assume only triangular elements in this section. We
seek an approximation for the potential Ve within an ­element e and then interrelate the poten­
tial distributions in various elements such that the potential is continuous across interelement
boundaries. The approximate solution for the whole region is
V1x, y2 . a
e51
Ve1x, y2
(14.45)
where N is the number of triangular or quadrilateral elements into which the solution
region is divided.
The most common form of approximation for Ve within an element is polynomial
­approximation, namely,
Ve1x, y2 5 a 1 bx 1 cy
(14.46)
for a triangular element and
Ve1x, y2 5 a 1 bx 1 cy 1 dxy
(14.47)
14.5  THE FINITE ELEMENT METHOD
3 See P. P. Silvester and R. L. Ferrari, Finite Elements for Electrical Engineers, 3rd ed. Cambridge, U.K.:
Cambridge Univ. Press, 1996.
FIGURE 14.26  A typical finite element
subdivision of an irregular domain.
792  CHAPTER 14  NUMERICAL METHODS
for a quadrilateral element. The potential Ve in general is nonzero within element e but
zero outside e. It is difficult to approximate the boundary of the solution region with quad­
rilateral elements; such elements are useful for problems whose boundaries are sufficiently
regular. In view of this, we prefer to use triangular elements throughout our analysis in this
section. Notice that our assumption of linear variation of potential within the triangular
element as in eq. (14.46) is the same as assuming that the electric field is uniform within
the element; that is,
Ee 5 2=Ve 5 21b ax 1 c ay2
(14.48)
B.  Element-Governing Equations
Consider a typical triangular element, as shown in Figure 14.27. The potential Ve1, Ve2, and
Ve3 at nodes 1, 2, and 3, respectively, are obtained by using eq. (14.46); that is,
Ve1
Ve2
Ve3
§ 5 £
§  £
§ 
(14.49)
The coefficients a, b, and c are determined from eq. (14.49) as
§ 5 £
Ve1
Ve2
Ve3
§ 
(14.50)
Substituting this into eq. (14.46) gives
Ve 5 31 x y4 1
2A £
1x2y3 2 x3y22
1x3y1 2 x1y32
1x1y2 2 x2y12
1y2 2 y32
1y3 2 y12
1y1 2 y22
1x3 2 x22
1x1 2 x32
1x2 2 x12
§  £
Ve1
Ve2
Ve3
Ve 5 a
i51
ai1x, y2 Vei
(14.51)
FIGURE 14.27  Typical triangular element; the
local node numbering 1-2-3 must be counterclock­
wise as indicated by the arrow.
14.5 The Finite Element Method  793
where
a1 5 1
2A 3 1x2y3 2 x3y22 1 1y2 2 y32 x 1 1x3 2 x22 y4
(14.52a)
a2 5 1
2A 3 1x3y1 2 x1y32 1 1y3 2 y12 x 1 1x1 2 x32 y4
(14.52b)
a3 5 1
2A 3 1x1y2 2 x2y12 1 1y1 2 y22 x 1 1x2 2 x12 y4
(14.52c)
and A is the area of the element e; that is,
2A 5 †
5 1x1y2 2 x2y12 1 1x3y1 2 x1y32 1 1x2y3 2 x3y22
A 5 1/2 3 1x2 2 x12 1y3 2 y12 2 1x3 2 x12 1y2 2 y12 4
(14.53)
The value of A is positive if the nodes are numbered counterclockwise (starting from any
node) as shown by the arrow in Figure 14.27. Note that eq. (14.51) gives the potential at
any point 1x, y2 within the element, provided the potentials at the vertices are known. This
is unlike the situation in finite difference analysis, where the potential is known at the grid
points only. Also note that ai are linear interpolation functions. They are called the element
shape functions, and they have the following properties:
ai1xj, yj2 5 e1,
i 5 j
i 2 j
(14.54a)
i51
ai1x, y2 5 1
(14.54b)
The shape functions a1 and a2, for example, are illustrated in Figure 14.28.
FIGURE 14.28  Shape functions a1
and a2 for a triangular element.
794  CHAPTER 14  NUMERICAL METHODS
The energy per unit length associated with the element e is given by eq. (4.96); that is,
We 5 1
2 3
e 0 E 0 2 dS 5 1
2 3
e 0 =Ve 0 2 dS
(14.55)
where a two-dimensional solution region free of charge 1rV 5 02 is assumed. But from
eq. (14.51),
=Ve 5 a
i51
Vei =ai
(14.56)
Substituting eq. (14.56) into eq. (14.55) gives
We 5 1
2 a
i51
j51
eVei c3
=ai # =aj dSd  Vej
(14.57)
If we define the term in brackets as
Cij
1e2 5 3
=ai # =aj dS
(14.58)
we may write eq. (14.57) in matrix form as
We 5 1
2 e 3Ve4T 3C1e24 3Ve4
(14.59)
where the superscript T denotes the transpose of the matrix
3Ve4 5 £
Ve1
Ve2
Ve3
§ 
(14.60a)
and
3C1e24 5 D
C11
1e2
C12
1e2
C13
1e2
C21
1e2
C22
1e2
C23
1e2
C31
1e2
C32
1e2
C33
1e2
(14.60b)
The matrix [C(e)] is usually called the element coefficient matrix. The matrix element Cij
1e2 of
the coefficient matrix may be regarded as the coupling between nodes i and j; its value is
obtained from eqs. (14.52) and (14.58). For example,
C12
1e2 5 3 =a1 # =a2 dS
4A2 3 1y2 2 y32 1y3 2 y12 1 1x3 2 x22 1x1 2 x32 4 3
dS
(14.61a)
5 1
4A 3 1y2 2 y32 1y3 2 y12 1 1x3 2 x22 1x1 2 x32 4
14.5 The Finite Element Method  795
Similarly:
C11
1e2 5 1
4A 3 1y2 2 y32 2 1 1x3 2 x22 24
(14.61b)
C13
1e2 5 1
4A 3 1y2 2 y32 1y1 2 y22 1 1x3 2 x22 1x2 2 x12 4
(14.61c)
C22
1e2 5 1
4A 3 1y3 2 y12 2 1 1x1 2 x32 24
(14.61d)
C23
1e2 5 1
4A 3 1y3 2 y12 1y1 2 y22 1 1x1 2 x32 1x2 2 x12 4
(14.61e)
C33
1e2 5 1
4A 3 1y1 2 y22 2 1 1x2 2 x12 24
(14.61f)
Also
C21
1e2 5 C12
1e2,  C31
1e2 5 C13
1e2,  C32
1e2 5 C23
1e2
(14.61g)
However, our calculations will be easier if we define
P1 5 1y2 2 y32,  P2 5 1y3 2 y12,  P3 5 1y1 2 y22
(14.62a)
Q1 5 1x3 2 x22,  Q2 5 1x1 2 x32,  Q3 5 1x2 2 x12
With Pi and Qi 1i 5 1, 2, 3 are the local node numbers2, each term in the element coef­
ficient matrix is found as
Cij
1e2 5 1
4A 3PiPj 1 QiQj4
(14.62b)
where
A 5 1
2 1P2Q3 2 P3Q22
(14.62c)
Note that P1 1 P2 1 P3 5 0 5 Q1 1 Q2 1 Q3 and hence a
i51
C1e2
ij 5 0 5 a
j51
C1e2
ij .
This may be used in checking our calculations.
C.  Assembling All the Elements
Having considered a typical element, the next step is to assemble all such elements in the
solution region. The energy associated with the assemblage of all elements in the mesh is
W 5 a
e51
We 5 1
2 e 3V4T 3C4 3V4
(14.63)
796  CHAPTER 14  NUMERICAL METHODS
where
3V4 5 F
(14.64)
n is the number of nodes, N is the number of elements, and [C] is called the overall or global
coefficient matrix, which is the assemblage of individual element coefficient matrices. The
major problem now is obtaining [C] from 3C1e24.
The process by which individual element coefficient matrices are assembled to obtain
the global coefficient matrix is best illustrated with an example. Consider the finite element
mesh consisting of three finite elements as shown in Figure 14.29. Observe the numberings
of the nodes. The numbering of nodes as 1, 2, 3, 4, and 5 is called global numbering. The
numbering i-j-k is called local numbering, and it corresponds with 1-2-3 of the element
in Figure 14.27. For example, for element 3 in Figure 14.29, the global numbering 3-5-4
corresponds to local numbering 1-2-3 of the element in Figure 14.27. Note that the local
­numbering must be in counterclockwise sequence starting from any node of the element.
For element 3, for example, we could choose 4-3-5 or 5-4-3 instead of 3-5-4 to correspond
with 1-2-3 of the element in Figure 14.27. Thus the numbering in Figure 14.29 is not
unique. However, we obtain the same [C] whichever numbering is used. Assuming the
particular numbering in Figure 14.29, the global coefficient matrix is expected to have the
form
3C4 5 E
C11
C12
C13
C14
C15
C21
C22
C23
C24
C25
C31
C32
C33
C34
C35
C41
C42
C43
C44
C45
C51
C52
C53
C54
C55
(14.65)
which is a 5 3 5 matrix, since five nodes 1n 5 52 are involved. Again, Cij is the coupling
between nodes i and j. We obtain Cij by utilizing the fact that the potential distribution
FIGURE 14.29  Assembly of three elements: i-j-k
corresponds to local numbering 1-2-3 of the
­element in Figure 14.27.
14.5 The Finite Element Method  797
must be continuous across interelement boundaries. The contribution to the i, j position in
[C] comes from all elements containing nodes i and j. To find C11, for example, we observe
from Figure 14.29 that global node 1 belongs to elements 1 and 2 and it is local node 1 in
both; hence,
C11 5 C11
112 1 C11
122
(14.66a)
For C22, global node 2 belongs to element 1 only and is the same as local node 3; hence,
C22 5 C33
112
(14.66b)
For C44, global node 4 is the same as local nodes 2, 3, and 3 in elements 1, 2, and 3, respec­
tively; hence,
C44 5 C22
112 1 C33
122 1 C33
132
(14.66c)
For C14, global link 14 is the same as the local links 12 and 13 in elements 1 and 2, respec­
tively; hence,
C14 5 C12
112 1 C13
122
(14.66d)
Since there is no coupling (or direct link) between nodes 2 and 3,
C23 5 C32 5 0
(14.66e)
Continuing in this manner, we obtain all the terms in the global coefficient matrix by
inspection of Figure 14.29 as
3C4 5 F
C11
112 1 C11
122
C13
112
C12
122
C12
112 1 C13
122
C31
112
C33
112
C32
112
C21
122
C22
122 1 C11
132
C23
122 1 C13
132
C12
132
C21
112 1 C31
122
C23
112
C32
122 1 C31
132
C22
112 1 C33
122 1 C33
132
C32
132
C21
132
C23
132
C22
132
(14.67)
Note that element coefficient matrices overlap at nodes shared by elements and that there
are 27 terms (nine for each of the three elements) in the global coefficient matrix [C]. Also
note the following properties of the matrix [C]:
1.	 It is symmetric 1Cij 5 Cji2 just like the element coefficient matrix.
2.	 Since Cij 5 0 if no coupling exists between nodes i and j, it is evident that for a
large number of elements [C] becomes sparse and banded.
3.	 It is singular. Although this is less obvious, it can be shown by using the element
coefficient matrix of eq. (14.60b).
798  CHAPTER 14  NUMERICAL METHODS
D.  Solving the Resulting Equations
From variational calculus, it is known that Laplace’s (or Poisson’s) equation is satisfied
when the total energy in the solution region is minimum. Thus we require that the partial
derivatives of W with respect to each nodal value of the potential be zero; that is,
'V1
5 'W
'V2
5 . . . 5 'W
'Vn
5 0
'Vk
5 0,  k 5 1, 2, . . ., n
(14.68)
For example, to get 'W/'V1 5 0 for the finite element mesh of Figure 14.29, we substitute ­
eq. (14.65) into eq. (14.63) and take the partial derivative of W with respect to V1. We obtain
0 5 'W
'V1
5 2V1C11 1 V2C12 1 V3C13 1 V4C14 1 V5C15
1 V2C21 1 V3C31 1 V4C41 1 V5C51
0 5 V1C11 1 V2C12 1 V3C13 1 V4C14 1 V5C15
(14.69)
In general, 'W/'Vk 5 0 leads to
0 5 a
i51
Vi Cik
(14.70)
where n is the number of nodes in the mesh. By writing eq. (14.70) for all nodes
k 5 1, 2, . . . , n, we obtain a set of simultaneous equations from which the solution of
3V4T 5 3V1, V2, . . . , Vn4 can be found. This can be done in two ways similar to those used
in solving finite difference equations obtained from Laplace’s (or Poisson’s) equation.
Iteration Method
The iterative approach is similar to that used in the finite difference method. Let us assume
that node 1 in Figure 14.29, for example, is a free node. The potential at node 1 can be
obtained from eq. (14.69) as
V1 5 2 1
C11
i52
ViC1i
(14.71)
In general, the potential at a free node k is obtained from eq. (14.70) as
Vk 5 2 1
Ckk
i51,i2k
ViCik
(14.72)
14.5 The Finite Element Method  799
This is applied iteratively to all the free nodes in the mesh with n nodes. Since Cki 5 0 if
node k is not directly connected to node i, only nodes that are directly linked to node k
contribute to Vk in eq. (14.72).
Thus if the potentials at nodes connected to node k are known, we can determine Vk
by using eq. (14.72). The iteration process begins by setting the potentials at the free nodes
equal to zero or to the average potential.
Vave 5 1
2 1Vmin 1 Vmax2
(14.73)
where Vmin and Vmax are the minimum and maximum values of the prescribed potentials
at the fixed nodes. With those initial values, the potentials at the free nodes are calculated
by using eq. (14.72). At the end of the first iteration, when the new values have been calcu­
lated for all the free nodes, these values become the old values for the second iteration. The
procedure is repeated until the change between subsequent iterations is negligible.
Band Matrix Method
If all free nodes are numbered first and the fixed nodes last, eq. (14.63) can be written such
that
W 5 1
2 e 3Vf Vp4 cCff
Cfp
Cpf
Cppd  cVf
Vpd 
(14.74)
where subscripts f and p, respectively, refer to nodes with free and fixed (or prescribed)
­potentials. Since Vp is constant (it consists of known, fixed values), we differentiate only
with respect to Vf , so that applying eq. (14.68) to eq. (14.74) yields
CffVf 1 CfpVp 5 0
3Cff4 3Vf4 5 23Cfp4 3Vp4
(14.75)
This equation can be written as
3A4 3V4 5 3B4
(14.76a)
3V4 5 3A421 3B4
(14.76b)
where 3V4 5 3Vf4, 3A4 5 3Cff4, and 3B4 5 23Cfp4 3Vp4. Since [A] is, in general, non-
singular, the potential at the free nodes can be found by using eq. (14.75). We can solve
for [V] in eq. (14.76a) by using the Gaussian elimination technique. We can also use
matrix inversion to solve for [V] in eq. (14.76b) if the size of the matrix to be inverted
is not large.
800  CHAPTER 14  NUMERICAL METHODS
Notice that as from eq. (14.55) onward, our solution has been restricted to a two-
dimensional problem involving Laplace’s equation, =2V 5 0. The basic concepts developed
in this section can be extended to finite element analysis of problems involving Poisson’s
equation 1=2V 5 2rv/e, =2A 5 2mJ2 or the wave equation 1=2f 2 g2f 5 02. A major
problem associated with finite element analysis is the relatively large amount of computer
memory required for storing the matrix elements, as well as the associated computational
time. However, several algorithms have been developed to alleviate the problem to some
degree.
The finite element method has a number of advantages over the finite difference
method and the method of moments. First, the FEM can easily handle the complex solu­
tion region. Second, the generality of the FEM makes it possible to construct a general-
purpose program for solving a wide range of problems. A single program can be used to
solve different problems (described by the same partial differential equations) with differ­
ent solution regions and different boundary conditions; only the input data to the problem
need be changed. However, the FEM has its own drawbacks. It is harder to understand and
program than the other methods (FDM and MOM). It also requires preparing input data,
a process that could be tedious.
Consider the two-element mesh shown in Figure 14.30(a). Using the finite element meth­
od, determine the potentials within the mesh.
FIGURE 14.30  For Example 14.6: (a) two-
element mesh, (b) local and global numbering
of the elements.
EXAMPLE 14.6
14.5 The Finite Element Method  801
Solution:
The element coefficient matrices can be calculated by using one of the relations of
eq. (14.62). For element 1, consisting of nodes 1-2-4 corresponding to the local numbering
1-2-3 as in Figure 14.30(b),
P1 5 21.3,  P2 5 0.9,
P3 5 0.4
Q1 5 20.2,  Q2 5 20.4,  Q3 5 0.6
A 5 1/2 10.54 1 0.162 5 0.35
Substituting all these into eq. (14.62b) gives
3C1124 5 £
1.236
20.7786
20.4571
20.7786
0.6929
0.0857
20.4571
0.0857
0.3714
§ 
(14.6.1)
Similarly, for element 2, consisting of nodes 2-3-4 corresponding to local numbering 1-2-3,
as in Figure 14.30(b),
P1 5 20.6,  P2 5 1.3,  P3 5 20.7
Q1 5 20.9,  Q2 5 0.2,  Q3 5 0.7
A 5 1/2 10.91 1 0.142 5 0.525
Hence,
3C1224 5 £
0.5571
20.4571
20.1
20.4571
0.8238
20.3667
20.1
20.3667
0.4667
§ 
(14.6.2)
Applying eq. (14.75) gives
cC22
C24
C42
C44d  cV2
V4d 5 2cC21
C23
C41
C43d  cV1
V3d 
(14.6.3)
This can be written in a more convenient form as
C22
C24
C42
C44
¥  ≥
¥ 5 ≥
2C21
2C23
2C41
2C43
¥  cV1
d 
(14.6.4a)
3C4 3V4 5 3B4
(14.6.4b)
802  CHAPTER 14  NUMERICAL METHODS
The terms of the global coefficient matrix are obtained as follows:
C22 5 C22
112 1 C11
122 5 0.6929 1 0.5571 5 1.25
C42 5 C24 5 C23
112 1 C13
122 5 0.0857 2 0.1 5 20.0143
C44 5 C33
112 1 C33
122 5 0.3714 1 0.4667 5 0.8381
C21 5 C21
112 5 20.7786
C23 5 C12
122 5 20.4571
C41 5 C31
112 5 20.4571
C43 5 C32
122 5 20.3667
Note that we follow local numbering for the element coefficient matrix and global number­
ing for the global coefficient matrix. Thus the square matrix [C] is obtained as
3C4 5 ≥
1.25
20.0143
20.0143
0.8381
¥ 
(14.6.5)
and the matrix [B] on the right-hand side of eq. (14.6.4a) is obtained as
3B4 5 ≥
4.571
10.0
3.667
¥ 
(14.6.6)
By inverting matrix [C] in eq. (14.6.5), we obtain
3V4 5 3C4213B4 5 ≥
3.708
10.0
4.438
Thus V1 5 0, V2 5 3.708, V3 5 10, and V4 5 4.438. Once the values of the potentials at
the nodes are known, the potential at any point within the mesh can be determined by
using eq. (14.51).
14.5 The Finite Element Method
Write a program to solve Laplace’s equation by means of the finite element method. Apply
the program to the two-dimensional problem shown in Figure 14.32(a).
Solution:
The solution region is divided into 25 three-node triangular elements with the total num-
ber of nodes being 21, as shown in Figure 14.32(b). This step is necessary to have input
data defining the geometry of the problem. Based on our discussions thus far, a general
MATLAB program for solving problems involving Laplace’s equation by using three-node
triangular elements was developed as in Figure 14.33. The development of the program
basically involves four steps indicated in the program and explained as follows.
Step 1: This involves inputting the necessary data defining the problem. This is the only step
that depends on the geometry of the problem at hand. Through a data file, we input the num-
ber of elements, the number of nodes, the number of fixed nodes, the prescribed values of the
potentials at the free nodes, the x- and y-coordinates of all nodes, and a list identifying the
FIGURE 14.31  For Practice Exercise 14.6.
EXAMPLE 14.7
PRACTICE EXERCISE 14.6
Calculate the global coefficient matrix for the two-element mesh shown in
Figure 14.31 when (a) node 1 is linked with node 3 and the local numbering (i-j-k) is
as indicated in Figure 14.31(a), (b) node 2 is linked with node 4 with local numbering
as in Figure 14.31(b).
Answer:  (a) ≥
0.9964
0.05
20.2464
20.8
0.05
0.7
20.75
0.0
20.2464
20.75
1.5964
20.75
20.8
0.0
20.75
1.4
¥ .
(b) ≥
1.333
20.7777
0.0
21.056
20.0777
0.8192
20.98
0.2386
0.0
20.98
2.04
21.06
21.056
0.2386
21.06
1.877
¥ .
803
804  CHAPTER 14  NUMERICAL METHODS
FIGURE 14.32  For Example
14.7: (a) two-dimensional elec­
trostatic problem, (b) solution
region divided into 25 triangular
elements.
%  FINITE ELEMENT SOLUTION OF LAPLACE’S EQUATION FOR
%  TWO-DIMENSIONAL PROBLEMS
%  TRIANGULAR ELEMENTS ARE USED
%  ND = NO. OF NODES
%  NE = NO. OF ELEMENTS
%  NP = NO. OF FIXED NODES (WHERE POTENTIAL IS PRESCRIBED)
%  NDP(I) = NODE NO. OF PRESCRIBED POTENTIAL, I=1,2,...,NP
%  VAL(I) = VALUE OF PRESCRIBED POTENTIAL AT NODE NDP(I)
%  NL(I,J) = LIST OF NODES FOR EACH ELEMENT I, WHERE
FIGURE 14.33  Computer program for Example 14.7.
14.5 The Finite Element Method  805
%           J=1,2,3 REFERS TO THE LOCAL NODE NUMBER
%  CE(I,J) = ELEMENT COEFFICIENT MATRIX
%  C(I,J) = GLOBAL COEFFICIENT MATRIX
%  B(I) = RIGHT-HAND SIDE MATRIX IN THE SYSTEM OF
%  SIMULTANEOUS EQUATIONS; SEE EQ. (14.6.4)
%  X(I), Y(I) = GLOBAL COORDINATES OF NODE I
%  XL(J), YL(J) = LOCAL COORDINATES OF NODE J=1,2,3
%  V(I) = POTENTIAL AT NODE I
%  MATRICES P(I) AND Q (I) ARE DEFINED IN EQ. (14.62a)
%  ****************************************************
%  FIRST STEP - INPUT DATA DEFINING GEOMETRY AND
BOUNDARY CONDITIONS
%  ****************************************************
clear
input(‘Name of input data file = ‛)
% ******************************************************
%  SECOND STEP - EVALUATE COEFFICIENT MATRIX FOR EACH
ELEMENT AND ASSEMBLE GLOBALLY
% ******************************************************
B = zeros(ND,1);
C = zeros(ND,ND);
for I=1:NE
% FIND LOCAL COORDINATES XL(J), YL(J) FOR ELEMENT I
K = NL(I,[1:3]);
XL = X(K);
YL = Y(K);
P=zeros(3,1);
Q=zeros(3,1);
P(1) = YL(2) - YL(3);
P(2) = YL(3) - YL(1);
P(3) = YL(1) - YL(2);
Q(1) = XL(3) - XL(2);
Q(2) = XL(1) - XL(3);
Q(3) = XL(2) - XL(1);
AREA = 0.5*abs( P(2)*Q(3) - Q(2)*P(3) );
%  DETERMINE COEFFICIENT MATRIX FOR ELEMENT I
CE=(P*P’+Q*Q’)/(4.0*AREA);
%  ASSEMBLE GLOBALLY - FIND C(I,J) AND B(I)
for J=1:3
IR = NL(I,J);
IFLAG1=0;
%  CHECK IF ROW CORRESPONDS TO A FIXED NODE
for K = 1:NP
if (IR == NDP(K))
FIGURE 14.33  (Continued)
806  CHAPTER 14  NUMERICAL METHODS
nodes belonging to each element in the order of the local numbering 1-2-3. For the problem
in Figure 14.32, the three sets of data for coordinates, the element–node relationship, and the
prescribed potentials at fixed nodes are shown in Tables 14.3, 14.4, and 14.5, respectively.
Step 2: This step entails finding the element coefficient matrix [C(e)] for each element and
the global coefficient matrix [C]. The procedure explained in Example 14.6 is applied.
Equation (14.6.4) can be written in general form as
Cff
d  cVP
d 5 c
2Cfp
d  3Vp4
C(IR,IR) = 1.0;
B(IR) = VAL(K);
IFLAG1=1;
end
end % end for K = 1:NP
if(IFLAG1 == 0)
for L = 1:3
IC = NL(I,L);
IFLAG2=0;
%  CHECK IF COLUMN CORRESPONDS TO A FIXED NODE
for K=1:NP
if ( IC == NDP(K) ),
B(IR) = B(IR) - CE(J,L)*VAL(K);
IFLAG2=1;
end
end % end for K=1:NP
if(IFLAG2 == 0)
C(IR,IC) = C(IR,IC) + CE(J,L);
end
end  % end for L=1:3
end   %end if(iflag1 == 0)
end  % end for J=1:3
end % end for I=1:NE
% ***************************************************
%   THIRD STEP - SOLVE THE SYSTEM OF EQUATIONS
% ***************************************************
V = inv(C)*B;
V=V’;
% ***************************************************
%   FOURTH STEP - OUTPUT THE RESULTS
% ***************************************************
diary exam147.out
[ND, NE, NP]
[ [1:ND]’ X’ Y’ V’]
diary off
FIGURE 14.33  (Continued)

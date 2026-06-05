# Sadiku《Elements of Electromagnetics》Chapter 6

> **Source:** Sadiku, *Elements of Electromagnetics*, 7th Ed. (Oxford University Press, 2017)  
> **PDF:** pages 252-301 of 926 (926 total)

---

## Boundary Value Problems

225
C H A P T E R
225
6.1  INTRODUCTION
The procedure for determining the electric field E in the preceding chapters has generally
been to use either Coulomb’s law or Gauss’s law when the charge distribution is known, or
E 5 2=V when the potential V is known throughout the region. In most practical situ­
ations, however, neither the charge distribution nor the potential distribution is known.
In this chapter, we shall consider practical electrostatic problems where only electro­
static conditions (charge and potential) at some boundaries are known and it is desired to
find E and V throughout the region. Such problems are usually tackled using Poisson’s or
Laplace’s equation or the method of images, and they are usually referred to as boundary-
value problems. The concepts of resistance and capacitance will be covered. We shall use
Laplace’s equation in deriving the resistance of an object and the capacitance of a capaci­
tor. Example 6.5 should be given special attention because we will refer to it often in the
remaining part of the text.
ELECTROSTATIC BOUNDARY-
VALUE PROBLEMS
Wise men profit more from fools than fools from wise men; for the wise men shun the
mistakes of the fools, but fools do not imitate the successes of the wise.
—MARCUS P. CATO
6.2  POISSON’S AND LAPLACE’S EQUATIONS
Poisson’s and Laplace’s equations are easily derived from Gauss’s law (for a linear, isotropic
material medium):
= # D 5 = # eE 5 rv
(6.1)
and
E 5 2=V
(6.2)
226  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Substituting eq. (6.2) into eq. (6.1) gives
= # 12e=V2 5 rv
(6.3)
for an inhomogeneous medium. For a homogeneous medium, eq. (6.3) becomes
=2V 5 2rv
e 
(6.4)
This is known as Poisson’s equation. A special case of this equation occurs when rv 5 0
(i.e., for a charge-free region). Equation (6.4) then becomes
=2V 5 0
(6.5)
which is known as Laplace’s equation. Note that in taking « out of the left-hand side
of eq. (6.3) to obtain eq. (6.4), we have assumed that « is constant throughout the
­region in which V is defined; for an inhomogeneous region, « is not constant and
eq. (6.4) does not follow eq. (6.3). Equation (6.3) is Poisson’s equation for an inho­
mogeneous medium; it becomes Laplace’s equation for an inhomogeneous medium
when rv 5 0.
Recall that the Laplacian operator 2 was derived in Section 3.8. Thus Laplace’s equa­
tion in Cartesian, cylindrical, or spherical coordinates, respectively, is given by
'2V
'x2 1 '2V
'y2 1 '2V
'z2 5 0
(6.6)
r '
'r ar'V
'r b 1 1
r2 '2V
'f2 1 '2V
'z2 5 0
(6.7)
r2 '
'r ar2 'V
'r b 1
r2sin u '
'u asin u 'V
'u b 1
r2sin2 u '2V
'f2 5 0
(6.8)
depending on the coordinate variables used to express V, that is, V1x, y, z2, V1r, f, z2,
or V1r, u, f2. Poisson’s equation in those coordinate systems may be obtained by simply
­replacing zero on the right-hand side of eqs. (6.6), (6.7), and (6.8) with 2rv/e.
Laplace’s equation is of primary importance in solving electrostatic problems involv­
ing a set of conductors maintained at different potentials. Examples of such problems
include capacitors and vacuum tube diodes. Laplace’s and Poisson’s equations are not
only useful in solving electrostatic field problem; they are used in various other field
problems. For example, V would be interpreted as magnetic potential in magnetostatics,
as temperature in heat conduction, as stress function in fluid flow, and as pressure head
in seepage.
6.3 Uniqueness Theorem  227
Since there are several methods (analytical, graphical, numerical, experimental, etc.) of
solving a given problem, we may wonder whether solving Laplace’s equation in differ­
ent ways gives different solutions. Therefore, before we begin to solve Laplace’s equation,
we should answer this question: if a solution of Laplace’s equation satisfies a given set of
boundary conditions, is this the only possible solution? The answer is yes: there is only one
solution. We say that the solution is unique. Thus any solution of Laplace’s equation that
satisfies the same boundary conditions must be the only solution regardless of the method
used. This is known as the uniqueness theorem. The theorem applies to any solution of
Poisson’s or Laplace’s equation in a given region or closed surface.
The theorem is proved by contradiction. We assume that there are two solutions V1 and
V2 of Laplace’s equation, both of which satisfy the prescribed boundary conditions. Thus
=2V1 5 0,   =2V2 5 0
(6.9a)
V1 5 V2   on the boundary
(6.9b)
We consider their difference
Vd 5 V2 2 V1
(6.10)
which obeys
=2Vd 5 =2V2 2 =2V1 5 0 
(6.11a)
Vd 5 0  on the boundary
(6.11b)
according to eq. (6.9). From the divergence theorem
= # A dv 5 C
A # dS
(6.12)
where S is the surface surrounding volume v and is the boundary of the original problem.
We let A 5 Vd =Vd and use a vector identity
= # A 5 = # 1Vd=Vd2 5 Vd=2Vd 1 =Vd # =Vd
But =2Vd 5 0 according to eq. (6.11a), so
= # A 5 =Vd # =Vd
(6.13)
Substituting eq. (6.13) into eq. (6.12) gives
=Vd # =Vd dv 5 C
Vd =Vd # dS
(6.14)
From eqs. (6.9) and (6.11), it is evident that the right-hand side of eq. (6.14) vanishes.
†6.3  UNIQUENESS THEOREM
228  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Hence,
0  =Vd 0 2 dv 5 0
Since the integrand is everywhere positive,
0 =V 0 d 5 0
(6.15a)
Vd 5 V2 2 V1 5 constant everywhere in v
(6.15b)
But eq. (6.15) must be consistent with eq. (6.9b). Hence, Vd 5 0 or V1 5 V2 ­everywhere,
showing that V1 and V2 cannot be different solutions of the same problem.
This is the uniqueness theorem: If a solution to Laplace’s equation can be found that
satisfies the boundary conditions, then the solution is unique.
Similar steps can be taken to show that the theorem applies to Poisson’s equation and to
prove the theorem for the case where the electric field (potential gradient) is specified on
the boundary.
Before we begin to solve boundary-value problems, we should bear in mind the three
things that uniquely describe a problem:
1.	 The appropriate differential equation (Laplace’s or Poisson’s equation in this
­chapter)
2.	 The solution region
3.	 The prescribed boundary conditions
A problem does not have a unique solution and cannot be solved completely if any of the
three items is missing.
6.4  GENERAL PROCEDURES FOR SOLVING POISSON’S OR
LAPLACE’S EQUATION
The following general procedure may be taken in solving a given boundary-value problem
involving Poisson’s or Laplace’s equation:
1.	 Solve Laplace’s (if rv 5 0) or Poisson’s (if rv 2 0) equation using either (a) direct
integration when V is a function of one variable or (b) separation of variables if V
is a function of more than one variable. The solution at this point is not unique but
is expressed in terms of unknown integration constants to be determined.
2.	 Apply the boundary conditions to determine a unique solution for V. Imposing
the given boundary conditions makes the solution unique.
3.	 Having obtained V, find E using E 5 2=V, D from D 5 eE, and J from J 5 sE.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  229
4.	 If required, find the charge Q induced on a conductor using Q 5 eS rS dS, where
rS 5 Dn and Dn is the component of D normal to the conductor. If necessary, the
capacitance of two conductors can be found using C 5 Q/V or the resistance of an
object can be found by using R 5 V/I, where I 5 e
S J # dS.
Solving Laplace’s (or Poisson’s) equation, as in step 1, is not always as complicated as
it may seem. In some cases, the solution may be obtained by mere inspection of the prob­
lem. Also a solution may be checked by going backward and finding out if it satisfies both
Laplace’s (or Poisson’s) equation and the prescribed boundary condition.
EXAMPLE 6.1
Current-carrying components in high-voltage power equipment can be cooled to carry
away the heat caused by ohmic losses. A means of pumping is based on the force transmit­
ted to the cooling fluid by charges in an electric field. Electrohydrodynamic (EHD) pump­
ing is modeled in Figure 6.1. The region between the electrodes contains a uniform charge
ro, which is generated at the left electrode and collected at the right electrode. Calculate the
pressure of the pump if ro 5 25 mC/m3 and Vo 5 22 kV.
Solution:
Since rv 2 0, we apply Poisson’s equation
=2V 5 2rv
The boundary conditions V1z 5 02 5 Vo and V1z 5 d2 5 0 show that V depends only on
z (there is no r or f dependence). Hence,
d2V
dz2 5 2ro
Integrating once gives
dz 5 2roz
1 A
Integrating again yields
V 5 2roz2
2e 1 Az 1 B
0 V
FIGURE 6.1  An electrohydrodynamic pump; for
Example 6.1.
230  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
where A and B are integration constants to be determined by applying the boundary condi­
tions. When z 5 0, V 5 Vo,
Vo 5 20 1 0 1 B S  B 5 Vo
When z 5 d, V 5 0,
0 5 2rod2
2e 1 Ad 1 Vo
A 5 rod
2e 2 Vo
The electric field is given by
E 5 2=V 5 2dV
dz  az 5 aroz
e 2 Abaz
5 c Vo
d 1 ro
e  az 2 d
2b daz
The net force is
F 5 3
rvE dv 5 ro 3 dS 3
z50
E dz
5 roS c Voz
1 ro
2e 1z2 2 dz2 d `
F 5 roSVoaz
The force per unit area or pressure is
r 5 F
S 5 roVo 5 25 3 1023 3 22 3 103 5 550 N/m2
PRACTICE EXERCISE  6.1
In a one-dimensional device, the charge density is given by rv 5 rox/a. If E 5 0 at
x 5 0 and V 5 0 at x 5 a, find V and E.
Answer:  ro
6ea 1a3 2 x32, rox2
2ae  ax.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  231
EXAMPLE 6.2
Recombination
FIGURE 6.2  For Example 6.2.
The xerographic copying machine is an important application of electrostatics. The surface
of the photoconductor is initially charged uniformly as in Figure 6.2(a). When light from
the document to be copied is focused on the photoconductor, the charges on the lower
surface combine with those on the upper surface to neutralize each other. The image is
developed by pouring a charged black powder over the surface of the photoconductor. The
electric field attracts the charged powder, which is later transferred to paper and melted
to form a permanent image. We want to determine the electric field below and above the
surface of the photoconductor.
Solution:
Consider the modeled version of Figure 6.2(a) shown in Figure 6.2(b). Since rv 5 0 in this
case, we apply Laplace’s equation. Also the potential depends only on x. Thus
=2V 5 d2V
dx2 5 0
Integrating twice gives
V 5 Ax 1 B
Let the potentials above and below x 5 a be V1 and V2, respectively:
V1 5 A1x 1 B1,  x . a
(6.2.1a)
V2 5 A2x 1 B2,  x , a
(6.2.1b)
232  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
The boundary conditions at the grounded electrodes are
V11x 5 d2 5 0
(6.2.2a)
V21x 5 02 5 0
(6.2.2b)
At the surface of the photoconductor,
V11x 5 a2 5 V21x 5 a2
(6.2.3a)
D1n 2 D2n 5 rS`
x5a
(6.2.3b)
We use the four conditions in eqs. (6.2.2) and (6.2.3) to determine the four unknown con­
stants A1, A2, B1, and B2. From eqs. (6.2.1) and (6.2.2),
0 5 A1d 1 B1 S  B1 5 2A1d
(6.2.4a)
0 5 0 1 B2 S  B2
5 0
(6.2.4b)
From eqs. (6.2.1) and (6.2.3a),
A1a 1 B1 5 A2a
(6.2.5)
To apply eq. (6.2.3b), recall that D 5 eE 5 2e=V so that
rS 5 D1n 2 D2n 5 e1E1n 2 e2E2n 5 2e1 dV1
dx 1 e2 dV2
rS 5 2e1A1 1 e2A2
(6.2.6)
Solving for A1 and A2 in eqs. (6.2.4) to (6.2.6), we obtain
E1 5 2A1ax 5
rSax
e1 c1 1 e2
a 2 e2
e1 d
,  a # x # d
E2 5 2A2ax 5
2rSad
a 2 1b ax
e1 c1 1 e2
a 2 e2
e1 d
,  0 # x # a
PRACTICE EXERCISE  6.2
For the model of Figure 6.2(b), if rS 5 0 and the upper electrode is maintained at Vo
while the lower electrode is grounded, show that
E1 5
2Vo ax
d 2 a 1 e1
,  E2 5
2Vo ax
a 1 e2
d 2 e2
Answer:  Proof.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  233
EXAMPLE 6.3
Semi-infinite conducting planes at f 5 0 and f 5 p/6 are separated by an infinitesimal
­insulating gap as shown in Figure 6.3. If V1f 5 02 5 0 and V1f 5 p/62 5 100 V, calcu­
late V and E in the region between the planes.
Solution:
Since V depends only on f, Laplace’s equation in cylindrical coordinates becomes
=2V 5 1
r2 d2V
df2 5 0
Since r 5 0 is excluded owing to the insulating gap, we can multiply by r2 to obtain
d2V
df2 5 0
which is integrated twice to give
V 5 Af 1 B
We apply the boundary conditions to determine constants A and B. When f 5 0, V 5 0,
0 5 0 1 B S  B 5 0
When f 5 fo, V 5 Vo,
Vo 5 Afo S  A 5 Vo
Hence,
V 5 Vo
FIGURE 6.3  Potential V1f2 due to
semi-infinite conducting planes.
234  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
and
E 5 2=V 5 21
r dV
df af 5 2 Vo
rfo
Substituting Vo 5 100 and fo 5 p/6 gives
V 5 600
p  f  and  E 5 2600
pr  af
Check: =2V 5 0, V1f 5 02 5 0, V1f 5 p/62 5 100.
EXAMPLE 6.4
PRACTICE EXERCISE  6.3
Two conducting plates of size 1 3 5 m are inclined at 45 to each other with a gap of
width 4 mm separating them as shown in Figure 6.4. Determine an approximate value
of the charge per plate if the plates are maintained at a potential difference of 50 V.
Assume that the medium between them has er 5 1.5.
Answer:  22.2 nC.
Two conducting cones 1u 5 p/10 and u 5 p/62 of infinite extent are separated by an
infinitesimal gap at r 5 0. If V1u 5 p/102 5 0 and V1u 5 p/62 5 50 V, find V and E
between the cones.
Solution:
Consider the coaxial cone of Figure 6.5, where the gap serves as an insulator between the
two conducting cones. Here V depends only on , so Laplace’s equation in spherical coor­
dinates becomes
=2V 5
r2 sin u d
du csin u dV
du d 5 0
FIGURE 6.4  For Practice Exercise 6.3.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  235
Since r 5 0 and u 5 0, p are excluded, we can multiply by r2 sin u to get
du csin u dV
du d 5 0
Integrating once gives
sin u dV
du 5 A
du 5
sin u
Integrating this results in
V 5 A 3 du
sin u 5 A 3
2 cos u/2 sin u/2
5 A 3 1/2 sec2 u/2 du
tan u/2
5 A 3 d1tan u/22
tan u/2
5 A ln1tan u/22 1 B
We now apply the boundary conditions to determine the integration constants A and B.
V1u 5 u12 5 0 S  0 5 A ln1tan u1/22 1 B
B 5 2A ln1tan u1/22
Gap
FIGURE 6.5  Potential V(u) due to conducting cones; for
Example 6.4.
236  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Hence,
V 5 A lnc tan u/2
tan u1/2 d
Also
V1u 5 u22 5 Vo S  Vo 5 A lnc tan u2/2
tan u1/2 d
A 5
lnc tan u2/2
tan u1/2 d
Thus
V 5
Vo lnc tan u/2
tan u1/2d
lnc tan u2/2
tan u1/2 d
E 5 2=V 5 21
r dV
du  au 5 2
r sin u au
5 2
r sin u lnc tan u2/2
tan u1/2 d
Taking u1 5 p/10, u2 5 p/6, and Vo 5 50 gives
V 5
50 lnc tan u/2
tan p/20d
lnc tan p/12
tan p/20 d
5 95.1 lnc tan u/2
0.1584 d  V
and
E 5 2 95.1
r sin u au V/m
Check: =2V 5 0, V1u 5 p/102 5 0, V1u 5 p/62 5 Vo.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  237
Gap
FIGURE 6.6  For Practice Exercise 6.4.
EXAMPLE 6.5
PRACTICE EXERCISE  6.4
A large conducting cone 1u 5 45°2 is placed on a conducting plane with a tiny gap
separating it from the plane as shown in Figure 6.6. If the cone is connected to a 50 V
source, find V and E at 123, 4, 22.
Answer:  27.87 V, 11.35a V/m.
(a)	 Determine the potential function for the region inside the rectangular trough of infi­
nite length whose cross section is shown in Figure 6.7.
(b)	 For Vo 5 100 V and b 5 2a, find the potential at x 5 a/2, y 5 3a/4.
Solution:
(a)	 The potential V in this case depends on x and y. Laplace’s equation becomes
=2V 5 '2V
'x2 1 '2V
'y2 5 0
(6.5.1)
FIGURE 6.7  Potential V1x, y2 due to
a conducting rectangular trough; for
Example 6.5.
238  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
We have to solve this equation subject to the following boundary conditions:
V1x 5 0, 0 # y , a2 5 0
(6.5.2a)
V1x 5 b, 0 # y , a2 5 0
(6.5.2b)
V10 # x # b, y 5 02 5 0
(6.5.2c)
V10 , x , b, y 5 a2 5 Vo
(6.5.2d)
We solve eq. (6.5.1) by the method of separation of variables; that is, we seek a product
solution of V. Let
V1x, y2 5 X1x2 Y1y2
(6.5.3)
where X is a function of x only and Y is a function of y only. Substituting eq. (6.5.3) into
eq. (6.5.1) yields
XsY 1 YsX 5 0
Dividing through by XY and separating X from Y gives
2Xs
X 5 Ys
Y 
(6.5.4a)
Since the left-hand side of this equation is a function of x only and the right-hand side is a
function of y only, for the equality to hold, both sides must be equal to a constant l; that is,
2Xs
X 5 Ys
Y 5 l
(6.5.4b)
The constant l is known as the separation constant. From eq. (6.5.4b), we obtain
Xs 1 lX 5 0
(6.5.5a)
and
Ys 2 lY 5 0
(6.5.5b)
Thus the variables have been separated at this point and we refer to eq. (6.5.5) as separated
equations. We can solve for X(x) and Y(y) separately and then substitute our solutions into
eq. (6.5.3). To do this requires that the boundary conditions in eq. (6.5.2) be separated, if
possible. We separate them as follows:
V10, y2 5 X102Y1y2 5 0 S  X102 5 0
(6.5.6a)
V1b, y2 5 X1b2Y1y2 5 0 S  X1b2 5 0
(6.5.6b)
V1x, 02 5 X1x2Y102 5 0 S  Y102 5 0
(6.5.6c)
V1x, a2 5 X1x2Y1a2 5 Vo 1inseparable2
(6.5.6d)
To solve for X(x) and Y(y) in eq. (6.5.5), we impose the boundary conditions in eq. (6.5.6).
We consider possible values of l that will satisfy both the separated equations in eq. (6.5.5)
and the conditions in eq. (6.5.6).
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  239
CASE 1.
If l 5 0, then eq. (6.5.5a) becomes
Xs 5 0  or  d2X
dx2 5 0
which, upon integrating twice, yields
X 5 Ax 1 B
(6.5.7)
The boundary conditions in eqs. (6.5.6a) and (6.5.6b) imply that
X1x 5 02 5 0 S  0 5 0 1 B  or  B 5 0
and
X1x 5 b2 5 0 S  0 5 A # b 1 0  or  A 5 0
because b 2 0. Hence our solution for X in eq. (6.5.7) becomes
X1x2 5 0
which makes V 5 0 in eq. (6.5.3). Thus we regard X1x2 5 0 as a trivial solution and we
conclude that l 2 0.
CASE 2.
If l , 0, say l 5 2a2, then eq. (6.5.5a) becomes
Xs 2 a2X 5 0  or  1D2 2 a22X 5 0
where D 5 d
dx, that is,
DX 5 6aX
(6.5.8)
showing that we have two possible solutions corresponding to the plus and minus signs.
For the plus sign, eq. (6.5.8) becomes
dx 5 aX  or  dX
X 5 a dx
Hence,
3 dX
X 5 3 a dx  or  ln X 5 ax 1 ln A1
where ln A1 is a constant of integration. Thus
X 5 A1eax
(6.5.9a)
240  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Similarly, for the minus sign, solving eq. (6.5.8) gives
X 5 A2e2ax
(6.5.9b)
The total solution consists of what we have in eqs. (6.5.9a) and (6.5.9b); that is,
X1x2 5 A1eax 1 A2e2ax
(6.5.10)
Since cosh ax 5 1eax 1 e2ax2/2 and sinh ax 5 1eax 2 e2ax2/2 or eax 5 cosh ax 1
sinh ax and e2ax 5 cosh ax 2 sinh ax, eq. (6.5.10) can be written as
X1x2 5 B1 cosh ax 1 B2 sinh ax
(6.5.11)
where B1 5 A1 1 A2 and B2 5 A1 2 A2. In view of the given boundary conditions, we pre­
fer eq. (6.5.11) to eq. (6.5.10) as the solution. Again, eqs. (6.5.6a) and (6.5.6b) require that
X1x 5 02 5 0 S  0 5 B1 # 112 1 B2 # 102  or  B1 5 0
and
X1x 5 b2 5 0 S  0 5 0 1 B2 sinh ab
Since a 2 0 and b 2 0, sinh ab cannot be zero. This is due to the fact that sinh x 5 0 if
and only if x 5 0 as shown in Figure 6.8. Hence B2 5 0 and
X1x2 5 0
This is also a trivial solution and we conclude that l cannot be less than zero.
CASE 3.
If l . 0, say l 5 b2, then eq. (6.5.5a) becomes
Xs 1 b2X 5 0
FIGURE 6.8  Sketch of cosh x and
sinh x showing that sinh x 5 0 if and
only if x 5 0; for Case 2 of Example 6.5.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  241
that is,
1D2 1 b22X 5 0  or  DX 5 6jbX
(6.5.12)
where j 5 !21. From eqs. (6.5.8) and (6.5.12), we notice that the difference between
Cases 2 and 3 is the replacement of a by jb. By taking the same procedure as in Case 2, we
obtain the solution as
X1x2 5 Coe jbx 1 C1e2jbx
(6.5.13a)
Since e jbx 5 cos bx 1 j sin bx and e2jbx 5 cos bx 2 j sin bx, eq. (6.5.13a) can be written as
X1x2 5 go cos bx 1 g1 sin bx
(6.5.13b)
where go 5 Co 1 C1 and g1 5 j1Co 2 C12.
In view of the given boundary conditions, we prefer to use eq. (6.5.13b). Imposing the
conditions in eqs. (6.5.6a) and (6.5.6b) yields
X1x 5 02 5 0 S  0 5 go # 112 1 0  or  go 5 0
and
X1x 5 b2 5 0 S  0 5 0 1 g1 sin bb
Suppose g1 2 0 (otherwise we get a trivial solution), then
sin bb 5 0 5 sin np S  bb 5 np
b 5 np
b ,  n 5 1, 2, 3, 4, . . .
(6.5.14)
Note that, unlike sinh x, which is zero only when x 5 0, sin x is zero at an infinite ­number
of points as shown in Figure 6.9. It should also be noted that n 2 0 because b 2 0; we
have already considered the possibility b 5 0 in Case 1, where we ended up with a triv­
ial solution. Also we do not need to consider n 5 21, 22, 23, 24,  .  .  . because l 5 b2
FIGURE 6.9  Sketch of sin x showing that sin x 5 0 at infinite
number of points; for Case 3 of Example 6.5.
242  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
would remain the same for positive and negative integer values of n. Thus for a given n,
eq. (6.5.13b) becomes
Xn1x2 5 gn sin npx
b 
(6.5.15)
Having found X(x) and
l 5 b2 5 n2p2
b2 
(6.5.16)
we solve eq. (6.5.5b), which is now
Ys 2 b2Y 5 0
Y1y2 5 ho cosh by 1 h1 sinh by
The boundary condition in eq. (6.5.6c) implies that
Y1y 5 02 5 0 S  0 5 ho # 112 1 0  or  ho 5 0
Hence our solution for Y(y) becomes
Yn1y2 5 hn sinh
npy
b 
(6.5.17)
Substituting eqs. (6.5.15) and (6.5.17), which are the solutions to the separated equations
in eq. (6.5.5), into the product solution in eq. (6.5.3) gives
Vn1x, y2 5 gnhn sin npx
b  sinh
npy
This shows that there are many possible solutions V1, V2, V3, V4, and so on, for n 5
1, 2, 3, 4, and so on.
By the superposition theorem, if V1, V2, V3, . . . , Vn are solutions of Laplace’s equation,
the linear combination
V 5 c1V1 1 c2V2 1 c3V3 1 . . . 1 cnVn
(where c1, c2, c3, .  .  . , cn are constants) is also a solution of Laplace’s equation. Thus the
solution to eq. (6.5.1) is
V1x, y2 5 a
n51
cn sin npx
b  sinh
npy
b 
(6.5.18)
where cn 5 gnhn are the coefficients to be determined from the boundary condition in
eq. (6.5.6d). Imposing this condition gives
V1x, y 5 a2 5 Vo 5 a
n51
cn sin npx
b  sinh npa
b 
(6.5.19)
The solution to this is similar to eq. (6.5.11) obtained in Case 2; that is,
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  243
which is a Fourier series expansion of Vo. Multiplying both sides of eq. (6.5.19) by
sin mpx/b and integrating over 0 , x , b gives
Vo sin mpx
b  dx 5 a
n51
cn sinh npa
b  3
sin mpx
b  sin npx
b  dx
(6.5.20)
By the orthogonality property of the sine or cosine function (see Appendix A.9).
sin mx sin nx dx 5 c0,
m 2 n
p/2,
m 5 n
Incorporating this property in eq. (6.5.20) means that all terms on the right-hand side of
eq. (6.5.20) will vanish except one term in which m 5 n. Thus eq. (6.5.20) reduces to
Vo sin npx
b  dx 5 cn sinh npa
b  3
sin2 npx
b  dx
2Vo b
np cos npx
b `
5 cn sinh npa
b  1
2 3
a1 2 cos 2npx
b dx
Vob
np  11 2 cos np2 5 cn sinh npa
# b
cn sinh npa
5 2Vo
np  11 2 cos np2
5 •
4Vo
n 5 1, 3, 5, . . .
n 5 2, 4, 6, . . .
that is,
cn 5 µ
4Vo
np sinh npa
n 5 odd
n 5 even
(6.5.21)
Substituting this into eq. (6.5.18) gives the complete solution as
V1x, y2 5 4Vo
n51,3,5, . . .
sin npx
b  sinh
npy
n sinh npa
(6.5.22)
Check: =2V 5 0, V1x 5 0, y2 5 0 5 V1x 5 b, y2 5 V1x, y 5 02, V1x, y 5 a2 5 Vo. The
solution in eq. (6.5.22) should not be a surprise; it can be guessed by mere observation
of the potential system in Figure 6.7. From this figure, we notice that along x, V varies
244  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
from 0 1at x 5 02 to 0 1at x 5 b2 and only a sine function can satisfy this requirement.
Similarly, along y, V varies from 0 1at y 5 02 to Vo 1at y 5 a2 and only a hyperbolic sine
function can satisfy this. Thus we should expect the solution as in eq. (6.5.22).
To determine the potential for each point 1x, y2 in the trough, we take the first few terms
of the convergent infinite series in eq. (6.5.22). Taking four or five terms may be sufficient.
(b)	 For x 5 a/2 and y 5 3a/4, where b 5 2a, we have
Vaa
2, 3a
4 b 5 4Vo
n51,3,5, . . .
sin np/4 sinh 3np/8
n sinh np/2
5 4Vo
p   c sin p/4 sinh 3p/8
sinh p/2
1 sin 3p/4 sinh 9p/8
3 sinh 3p/2
1 sin 5p/4 sinh 15p/8
5 sinh 5p/2
1 . . .d
5 4Vo
p  10.4517 1 0.0725 2 0.01985 2 0.00645 1 0.00229 1 . . .2
5 0.6374Vo
It is instructive to consider a special case of a 5 b 5 1 m and Vo 5 100 V. The potentials
at some specific points are calculated by using eq. (6.5.22), and the result is displayed in
Figure 6.10(a). The corresponding flux lines and equipotential lines are shown in Figure
6.10(b). A simple MATLAB program based on eq. (6.5.22) is displayed in Figure 6.11. This
self-explanatory program can be used to calculate V1x, y2 at any point within the trough.
In Figure 6.11, V1x 5 b/4, y 5 3a/42 is typically calculated and found to be 43.2 V.
FIGURE 6.10  For Example 6.5: (a) V1x, y2 calculated at some points, (b) sketch of
flux lines and equipotential lines.
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  245
h=0.1;
vo=100;
a=1.0;
b=a;
c=4*vo/pi;
IMAX = a/h;
JMAX = b/h;
NMAX = 13;
for I=1:IMAX
x=h*I;
for J=1:JMAX
y=h*J;
sum=0.0;
for n =1:2:NMAX
a1=sin(n*pi*x/b);
a2=sinh(n*pi*y/b);
a3=n*sinh(n*pi*a/b);
sum= sum + c*a1*a2/a3;
end
V(I,J)=sum;
end
end
mesh(V);
PRACTICE EXERCISE 6.5
For the problem in Example 6.5, take Vo 5 100 V, b 5 2a 5 2 m, and find V and E at
(a)  1x, y2 5 1a, a/22
(b)  1x, y2 5 13a/2, a/42
Answer:  (a) 44.51 V, 299.25ay V/m,  (b) 16.5 V, 20.6ax 2 70.34ay V/m.
100
120
(b)
FIGURE 6.11  (a) MATLAB program for Example 6.5, (b) the output of the MATLAB program.
(a)
246  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
V1x, y2 5 a
n51
cn sin npx
b  sinh
npy
b 
(6.6.1)
in accordance with eq. (6.5.18). But instead of eq. (6.5.19), we now have
V1y 5 a2 5 Vo 5 10 sin 3px
5 a
n51
cn sin npx
b  sinh npa
By equating the coefficients of the sine terms on both sides, we obtain
cn 5 0,  n 2 3
For n 5 3,
10 5 c3 sinh 3pa
c3 5
sinh 3pa
Thus the solution in eq. (6.6.1) becomes
V1x, y2 5 10 sin 3px
sinh
3py
sinh 3pa
(b)	 Similarly, instead of eq. (6.5.19), we have
Vo 5 V1y 5 a2
2 sin px
b 1 1
10 sin 5px
5 a
n51
cn sin npx
b  sinh npa
Equating the coefficient of the sine terms:
cn 5 0,  n 2 1, 5
EXAMPLE 6.6
Find the potential distribution in Example 6.5 if Vo is not constant but
(a)	 Vo 5 10 sin 3px/b, y 5 a, 0 # x # b
(b)	 Vo 5 2 sin px
b 1 1
10 sin 5px
b , y 5 a, 0 # x # b
Solution:
(a)  In Example 6.5, every step before eq. (6.5.19) remains the same; that is, the solution is
of the form
6.4 General Procedures for Solving Poisson’s or Laplace’s Equation  247
For n 5 1,
2 5 c1 sinh pa
b   or  c1 5
sinh pa
For n 5 5,
10 5 c5 sinh 5pa
b   or  c5 5
10 sinh 5pa
Hence,
V1x, y2 5
2 sin px
b  sinh
sinh pa
sin 5px
b  sinh
5py
10 sinh 5pa
PRACTICE EXERCISE  6.6
In Example 6.5, suppose everything remains the same except that Vo is replaced by
Vo sin 7px
b , 0 # x # b, y 5 a. Find V1x, y2.
Answer:
Vo sin 7px
b  sinh
7py
sinh 7pa
EXAMPLE 6.7
Obtain the separated differential equations for potential distribution V1r, f, z2 in a
charge-free region.
Solution:
This example, like Example 6.5, further illustrates the method of separation of variables.
Since the region is free of charge, we need to solve Laplace’s equation in cylindrical coor­
dinates; that is,
=2V 5 1
r '
'r ar 'V
'r b 1 1
r2 '2V
'f2 1 '2V
'z2 5 0
(6.7.1)
We let
V1r, f, z2 5 R1r2 F 1f2 Z1z2
(6.7.2)
248  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
where R,
, and Z are, respectively, functions of , , and z. Substituting eq. (6.7.2) into
eq. (6.7.1) gives
r  d
dr ar dR
dr b 1 RZ
r2  d2
df2 1 R
d2Z
dz2 5 0
(6.7.3)
We divide through by RFZ to obtain
rR d
dr ar dR
dr b 1
df2 5 21
Z d2Z
dz2
(6.7.4)
The right-hand side of this equation is solely a function of z, whereas the left-hand side
does not depend on z. For the two sides to be equal, they must be constant; that is,
rR d
dr ar dR
dr b 1
df2 5 21
Z d2Z
dz2 5 2l2
(6.7.5)
where 2l2 is a separation constant. Equation (6.7.5) can be separated into two parts:
Z d2Z
dz2 5 l2
(6.7.6)
Z s 2 l2Z 5 0
(6.7.7)
and
R d
dr ar dR
dr b 1 l2r2 1 1
df2 5 0
(6.7.8)
Equation (6.7.8) can be written as
R  d2R
dr2 1 r
R dR
dr 1 l2r2 5 2 1
df2 5 m2
(6.7.9)
where 2 is another separation constant. Equation (6.7.9) is separated as
s 1 m2
5 0
(6.7.10)
and
r2Rs 1 rRr 1 1r2l2 2 m22R 5 0
(6.7.11)
6.5 Resistance and Capacitance  249
Equations (6.7.7), (6.7.10), and (6.7.11) are the required separated differential equations.
Equation (6.7.7) has a solution similar to the solution obtained in Case 2 of Example 6.5;
that is,
Z1z2 5 c1 cosh lz 1 c2 sinh lz
(6.7.12)
The solution to eq. (6.7.10) is similar to the solution obtained in Case 3 of Example 6.5;
that is,
 1f2 5 c3 cos mf 1 c4 sin mf
(6.7.13)
Equation (6.7.11) is known as the Bessel differential equation and its solution is beyond the
scope of this text.1
6.5  RESISTANCE AND CAPACITANCE
In Section 5.4 the concept of resistance was covered and we derived eq. (5.16) for finding
the resistance of a conductor of uniform cross section. If the cross section of the conductor
is not uniform, eq. (5.16) becomes invalid and the resistance is obtained from eq. (5.17):
R 5 V
I 5 eL E # dl
eS sE # dS
(6.16)
The problem of finding the resistance of a conductor of nonuniform cross section can be
treated as a boundary-value problem. Using eq. (6.16), the resistance R (or conductance
G 5 1/R) of a given conducting material can be found by following these steps:
1.	 Choose a suitable coordinate system.
2.	 Assume Vo as the potential difference between conductor terminals.
3.	 Solve Laplace’s equation 2V 5 0 to obtain V. Then determine E from E 5 2=V
and find I from I 5 eS sE # dS.
4.	 Finally, obtain R as Vo/I.
In essence, we assume Vo, find I, and determine R 5 Vo/I. Alternatively, it is possible
to assume current Io, find the corresponding potential difference V, and determine R from
1 For a complete solution of Laplace’s equation in cylindrical or spherical coordinates, see, for ­example,
D. T. Paris and F. K. Hurd, Basic Electromagnetic Theory. New York: McGraw-Hill, 1969, pp. 150–159.
PRACTICE EXERCISE 6.7
Repeat Example 6.7 for V1r, u, f2.
Answer:  If V1r, u, f2 5 R1r2 F1u2
1f2,
s 1 l2
5 0, Rs 1 2
rRr 2 m2
r2 R 5 0,
Fs 1 cos u Fr 1 1m2 sin u 2 l2 csc u2 F 5 0.
250  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
R 5 V/Io. As will be discussed shortly, the capacitance of a capacitor is obtained using a
similar technique.
Generally speaking, to have a capacitor we must have two (or more) conductors car­
rying equal but opposite charges. This implies that all the flux lines leaving one conduc­
tor must necessarily terminate at the surface of the other conductor. The conductors are
sometimes referred to as the plates of the capacitor. The plates may be separated by free
space or a dielectric.
Consider the two-conductor capacitor of Figure 6.12. The conductors are maintained
at a potential difference V given by
V 5 V1 2 V2 5 23
E # dl
(6.17)
where E is the electric field existing between the conductors and conductor 1 is assumed to
carry a positive charge. (Note that the E field is always normal to the conducting surfaces.)
We define the capacitance C of the capacitor as the ratio of the magnitude of the charge
on one of the plates to the potential difference between them; that is,
C 5 Q
V 5
e eS E # dS
eL E # dl
(6.18)
The negative sign before V 5 2eL E # dl has been dropped because we are interested in
the absolute value of V. The capacitance C is a physical property of the capacitor and is
are specified in microfarads (mF) or picofarads (pF). We can use eq. (6.18) to obtain C for
any given two-conductor capacitance by following either of these methods:
1.	 Assuming Q and determining V in terms of Q (involving Gauss’s law)
C 5 Q
2.	 Assuming V and determining Q in terms of V (involving solving Laplace’s equation)
C 5 Q
(assume)
(find)
(find)
(assume)
FIGURE 6.12  A two-conductor
­capacitor.
measured in farads (F). Most capacitances are practically much smaller than a farad and
6.5 Resistance and Capacitance  251
We shall use the former method here, and the latter method will be illustrated in
Examples 6.10 and 6.11. The former method involves taking the following steps:
1.	 Choose a suitable coordinate system.
2.	 Let the two conducting plates carry charges 1Q and 2Q.
3.	 Determine E by using Coulomb’s or Gauss’s law and find V from V 5 2eL E # dl. The
negative sign may be ignored in this case because we are interested in the absolute
value of V.
4.	 Finally, obtain C from C 5 Q/V.
We will now apply this mathematically attractive procedure to determine the capaci­
tance of some important two-conductor configurations.
A.  Parallel-Plate Capacitor
Consider the parallel-plate capacitor of Figure 6.13(a). Suppose that each of the plates has
an area S and they are separated by a distance d. We assume that plates 1 and 2, respectively,
carry charges 1Q and 2Q uniformly distributed on them so that
rS 5 Q
S 
(6.19)
FIGURE 6.13  (a) Parallel-plate
capacitor. (b) Fringing effect due
to a parallel-plate capacitor.
252  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
An ideal parallel-plate capacitor is one in which the plate separation d is very small com­
pared with the dimensions of the plate. Assuming such an ideal case, the fringing field
at the edge of the plates, as illustrated in Figure 6.13(b), can be ignored so that the field
between them is considered uniform. If the space between the plates is filled with a homo­
geneous dielectric with permittivity « and we ignore flux fringing at the edges of the plates,
from eq. (4.27), D 5 2rSax or
E 5 rS
e  12ax2
5 2 Q
eS ax
(6.20)
Hence,
V 5 23
E # dl 5 23
c2 Q
eS axd # dx ax 5 Qd
eS 
(6.21)
and thus for a parallel-plate capacitor
C 5 Q
V 5 eS
d 
(6.22)
This formula offers a means of measuring the dielectric constant «r of a given dielectric.
By measuring the capacitance C of a parallel-plate capacitor with the space between the
plates filled with the dielectric and the capacitance Co with air between the plates, we
find «r from
er 5 C
(6.23)
Using eq. (4.96), it can be shown that the energy stored in a capacitor is given by
WE 5 1
2 CV2 5 1
2 QV 5 Q2
2C
(6.24)
To verify this for a parallel-plate capacitor, we substitute eq. (6.20) into eq. (4.96) and ­obtain
WE 5 1
2 3
e Q2
e2S2 dv 5 eQ2Sd
2e2S2
5 Q2
2  a d
eSb 5 Q2
2C 5 1
2 QV
as expected.
6.5 Resistance and Capacitance  253
B.  Coaxial Capacitor
A coaxial capacitor is essentially a coaxial cable or coaxial cylindrical capacitor. Consider
length L of two coaxial conductors of inner radius a and outer radius b 1b . a2 as shown in
Figure 6.14. Let the space between the conductors be filled with a homogeneous dielectric
with permittivity «. We assume that conductors 1 and 2, respectively, carry 1Q and 2Q
uniformly distributed on them. By applying Gauss’s law to an arbitrary Gaussian cylindrical
surface of radius r 1a , r , b2, we obtain
Q 5 e C
E # dS 5 eEr2prL
(6.25)
Hence,
E 5
2perL ar
(6.26)
Neglecting flux fringing at the cylinder ends,
V 5 23
E # dl 5 23
2perL ard # dr ar
(6.27a)
2peL ln b
(6.27b)
Thus the capacitance of a coaxial cylinder is given by
C 5 Q
V 5 2peL
ln b
(6.28)
C.  Spherical Capacitor
A spherical capacitor is the case of two concentric spherical conductors. Consider the inner
sphere of radius a and outer sphere of radius b 1b . a2 separated by a dielectric medium
with permittivity « as shown in Figure 6.15. We assume charges 1Q and 2Q on the inner
FIGURE 6.14  A coaxial capacitor.
254  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
and outer spheres, respectively. By applying Gauss’s law to an arbitrary Gaussian spherical
surface of radius r 1a , r , b2, we have
Q 5 e C
E # dS 5 eEr4pr2
(6.29)
that is,
E 5
4per2 ar
(6.30)
The potential difference between the conductors is
V 5 23
E # dl 5 23
4per2 ard # dr ar
4pe c 1
a 2 1
b d
(6.31)
Thus the capacitance of the spherical capacitor is
C 5 Q
V 5
4pe
a 2 1
(6.32)
By letting b S  `, C 5 4pea, which is the capacitance of a spherical capacitor whose
outer plate is infinitely large. Such is the case of a spherical conductor at a large distance
from other conducting bodies—the isolated sphere. Even an irregularly shaped object of
about the same size as the sphere will have nearly the same capacitance. This fact is useful
in estimating the stray capacitance of an isolated body or piece of equipment.
Recall from network theory that if two capacitors with capacitance C1 and C2 are in series
(i.e., they have the same charge on them) as shown in Figure 6.16(a), the total capacitance is
C 5 1
1 1
FIGURE 6.15  A spherical capacitor.
6.5 Resistance and Capacitance  255
C 5
C1 C2
C1 1 C2
(6.33)
If the capacitors are in parallel (i.e., if they have the same voltage across their plates) as
shown in Figure 6.16(b), the total capacitance is
C 5 C1 1 C2
(6.34)
Let us reconsider the expressions for finding the resistance R and the capacitance C of
an electrical system. The expressions were given in eqs. (6.16) and (6.18):
R 5 V
I 5 eLE # dl
eSsE # dS
(6.16)
C 5 Q
V 5
e AS E # dS
eLE # dl
(6.18)
The product of these expressions yields
RC 5 e
(6.35)
which is the relaxation time Tr of the medium separating the conductors. It should be
remarked that eq. (6.35) is valid only when the medium is homogeneous; this is easily
­inferred from eqs. (6.16) and (6.18). Assuming homogeneous media, the resistance of vari­
ous capacitors mentioned earlier can be readily obtained using eq. (6.35). The following
examples are provided to illustrate this idea.
For a parallel-plate capacitor,
C 5 eS
d ,  R 5 d
sS
(6.36)
FIGURE 6.16  Capacitors (a) in series
and (b) in parallel.
256  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
For a cylindrical capacitor,
C 5 2 peL
ln b
,  R 5
ln b
2 psL
(6.37)
For a spherical capacitor,
C 5
4pe
a 2 1
,  R 5
a 2 1
4ps 
(6.38)
And finally for an isolated spherical conductor,
C 5 4pea,  R 5
4psa
(6.39)
It should be noted that the resistance R in each of eqs. (6.35) to (6.39) is not the resistance
of the capacitor plate but the leakage resistance between the plates; therefore,  in those
equations is the conductivity of the dielectric medium separating the plates.
EXAMPLE 6.8
A metal bar of conductivity  is bent to form a flat 90 sector of inner radius a, outer radius
b, and thickness t as shown in Figure 6.17. Show that (a) the resistance of the bar between
the vertical curved surfaces at r 5 a and r 5 b is
R 5
2 ln b
spt
and (b) the resistance between the two horizontal surfaces at z 5 0 and z 5 t is
Rr 5
sp1b2 2 a22
FIGURE 6.17  Bent metal bar
for Exam­ple 6.8.
6.5 Resistance and Capacitance  257
Solution:
(a)	 Between the vertical curved ends located at r 5 a and r 5 b, the bar has a nonuniform
cross section and hence eq. (5.16) does not apply. We have to use eq. (6.16). Let a poten­
tial difference Vo be maintained between the curved surfaces at r 5 a and r 5 b so that
V1r 5 a2 5 0 and V1r 5 b2 5 Vo. We solve for V in Laplace’s equation =2V 5 0 in
cylindrical coordinates. Since V 5 V1r2,
=2V 5 1
r d
dr ar dV
dr b 5 0
As r 5 0 is excluded, upon multiplying by r and integrating once, this becomes
r dV
dr 5 A
dr 5 A
Integrating once again yields
V 5 A ln r 1 B
where A and B are constants of integration to be determined from the boundary conditions.
V1r 5 a2 5 0 S  0 5 A ln a 1 B  or  B 5 2A ln a
V1r 5 b2 5 Vo S  Vo 5 A ln b 1 B 5 A ln b 2 A ln a 5 A ln b
a  or  A 5 Vo
ln b
Hence,
V 5 A ln r 2 A ln a 5 A ln r
a 5 Vo
ln b
ln r
E 5 2=V 5 2dV
dr ar 5 2A
r ar 5 2 Vo
r ln b
J 5 sE,  dS 5 2r df dz ar
I 5 3
J # dS 5 3
p/2
f50
z50
Vos
r ln b
dz r df 5 p
2  tVos
ln b
258  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Thus
R 5 Vo
I 5
2 ln b
spt
as required.
(b)	 Let Vo be the potential difference between the two horizontal surfaces so that
V1z 5 02 5 0 and V1z 5 t2 5 Vo. V 5 V1z2, so Laplace’s equation =2V 5 0 becomes
d2V
dz2 5 0
Integrating twice gives
V 5 Az 1 B
We apply the boundary conditions to determine A and B:
V1 z 50 2 50  S 0 50 1B  or  B 50
V1 z 5t 2 5Vo S Vo 5At  or  A 5 Vo
Hence,
V 5 Vo
t  z
E 5 2=V 5 2dV
dz  az 5 2Vo
t  az
J 5 sE 5 2sVo
t  az,  dS 5 2r df dr az
I  5 3
J # dS 5 3
r50
p/2
f50
V0s
t  r df dr
5 Vos
# p
2  r2
2 `
5 Vo s p 1b2 2 a22
Thus
Rr 5 Vo
I 5
sp1b2 2 a22
Alternatively, for this case, the cross section of the bar is uniform between the horizon­
tal surfaces at z 5 0 and z 5 t and eq. (5.16) holds. Hence,
6.5 Resistance and Capacitance  259
Rr 5 ,
sS 5
4 1b2 2 a22
sp1b2 2 a22
as required.
PRACTICE EXERCISE  6.8
A disk of thickness t has radius b and a central hole of radius a. Taking the conductivity
of the disk as , find the resistance between
(a)  The hole and the rim of the disk
(b)  The two flat sides of the disk
Answer:  (a)
ln b
2pts,  (b)
sp1b2 2 a22 .
EXAMPLE 6.9
A coaxial cable contains an insulating material of conductivity . If the radius of the central
wire is a and that of the sheath is b, show that the conductance of the cable per unit length
is [see eq. (6.37)]
G 5 2ps
ln b
Solution:
Consider length L of the coaxial cable as shown in Figure 6.14. Let Vo be the potential differ­
ence between the inner and outer conductors so that V1r 5 a2 5 0 and V1r 5 b2 5 Vo,
which allows V and E to be found just as in part (a) of Example 6.8. Hence,
J 5 sE 5 2sVo
r ln b
ar,  dS 5 2r df dz ar
I 5 3
J # dS 5 3
f50
z50
Vos
r ln b
r dz df
5 2pLsVo
ln b
260  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
The resistance of the cable of length is given by
R 5 Vo
# 
L 5
lnb
ps
and the conductance per unit length is
G 5 1
R 5 2ps
ln1 b
as required.
PRACTICE EXERCISE  6.9
A coaxial cable contains an insulating material of conductivity 1 in its upper half and
another material of conductivity 2 in its lower half (similar to the situation shown later
in Figure 6.19b). If the radius of the central wire is a and that of the sheath is b, show
that the leakage resistance of length  of the cable is
R 5
p,1s1 1 s22  ln b
Answer:  Proof.
EXAMPLE 6.10
Conducting spherical shells with radii a 5 10 cm and b 5 30 cm are maintained at a
potential difference of 100 V such that V1r 5 b2 5 0 and V1r 5 a2 5 100 V. Determine
V and E in the region between the shells. If er 5 2.5 in the region, determine the total
charge induced on the shells and the capacitance of the capacitor.
Solution:
Consider the spherical shells shown in Figure 6.18 and assume that V depends only on r.
Hence Laplace’s equation becomes
FIGURE 6.18  Potential V(r) due to conducting
spherical shells.
6.5 Resistance and Capacitance  261
=2V 5 1
r2 d
dr cr2 dV
dr d 5 0
Since r 2 0 in the region of interest, we multiply through by r2 to obtain
dr cr2 dV
dr d 5 0
Integrating once gives
r2 dV
dr 5 A
dr 5 A
Integrating again gives
V 5 2A
r 1 B
As usual, constants A and B are determined from the boundary conditions.
When r 5 b, V 5 0 S  0 5 2A
b 1 B    or    B 5 A
Hence,
V 5 A c 1
b 2 1
r d
Also when r 5 a, V 5 Vo S  Vo 5 A c 1
b 2 1
a d
A 5
b 2 1
Thus
V 5 Vo
c 1
r 2 1
b d
a 2 1
262  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
E 5 2=V 5 2dV
dr  ar 5 2A
r2 ar
r2 c 1
a 2 1
Q 5 3
eE # dS 5 3
u50
f50
eoerVo
r2 c 1
a 2 1
b d
r2 sin u df du
5 4peoerVo
a 2 1
Alternatively,
rs 5 Dn 5 eEr,     Q 5 3
rsdS
The capacitance is easily determined as
C 5 Q
4pe
a 2 1
which is the same as we obtained in eq. (6.32); there in Section 6.5, we assumed Q and
found the corresponding Vo, but here we assumed Vo and found the corresponding Q to
­determine C. Substituting a 5 0.1 m, b 5 0.3 m, Vo 5 100 V yields
V 5 100
c 1
r 2 10
3 d
10 2 10/3 5 15 c 1
r 2 10
3 d  V
Check: =2V 5 0, V1r 5 0.3 m2 5 0, V1r 5 0.1 m2 5 100.
E 5
100
r2 310 2 10/34 ar 5 15
r2  ar V/m
Q 5 64p # 1029
36p
# 12.52 # 11002
10 2 10/3
5 64.167 nC
The positive charge is induced on the inner shell; the negative charge is induced on the
outer shell. Also
C 5
0 Q 0
5 4.167 3 1029
100
5 41.67 pF
6.5 Resistance and Capacitance  263
FIGURE 6.19  For Practice
Exercises 6.9, 6.10, and 6.12.
PRACTICE EXERCISE  6.10
If Figure 6.19 represents the cross sections of two spherical capacitors, determine their
capacitances. Let a 5 1 mm, b 5 3 mm, c 5 2 mm, er1 5 2.5, and er2 5 3.5.
Answer:  (a) 0.53 pF, (b) 0.5 pF.
EXAMPLE 6.11
In Section 6.5, it was mentioned that the capacitance C 5 Q/V of a capacitor can be found
by either assuming Q and finding V, as in Section 6.5, or by assuming V and finding Q, as
in Example 6.10. Use the latter method to derive eq. (6.22).
Solution:
Assume that the parallel plates in Figure 6.13 are maintained at a potential difference
Vo so that V1x 5 02 and V1x 5 d2 5 Vo. This necessitates solving a one-dimensional
boundary-value problem; that is, we solve Laplace’s equation
=2V 5 d2V
dx2 5 0
Integrating twice gives
V 5 Ax 1 B
where A and B are integration constants to be determined from the boundary conditions.
At x 5 0, V 5 0 S  0 5 0 1 B, or B 5 0, and at x 5 d, V 5 Vo S  Vo 5 Ad 1 0 or
A 5 Vo/d.
Hence,
V 5 Vo
d  x
Notice that this solution satisfies Laplace’s equation and the boundary conditions.
We have assumed the potential difference between the plates to be Vo. Our goal is to
find the charge Q on either plate so that we can eventually find the capacitance C 5 Q/Vo.
The charge on either plate is
264  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Q 5 3
rS dS
But rS 5 D # an 5 eE # an, where
E 5 2=V 5 2dV
dx  ax 5 2Aax 5 2Vo
d  ax
On the lower plate, an 5 ax, so
rS 5 2eVo
d   and  Q 5 2eVoS
On the upper plate, an 5 2ax, so
rS 5 eVo
d   and  Q 5 eVoS
As expected, Q is equal but opposite on each plate. Thus
C 5
0 Q 0
5 eS
which is in agreement with eq. (6.22).
EXAMPLE 6.12
PRACTICE EXERCISE  6.11
Derive the formula for the capacitance C 5 Q/Vo of a cylindrical capacitor in eq. (6.28)
by assuming Vo and finding Q.
Determine the capacitance of each of the capacitors in Figure 6.20. Take er1 5 4, er2 5 6,
d 5 5 mm, S 5 30 cm2.
Solution:
(a)	 Since D and E are normal to the dielectric interface, the capacitor in Figure 6.20(a) can
be treated as consisting of two capacitors C1 and C2 in series as in Figure 6.16(a).
C1 5 eoer1S
d/2
5 2eoer1S
,  C2 5 2eoer2S
The total capacitor C is given by
C 5
C1C2
C1 1 C2
5 2eoS
1er1er22
er1 1 er2
6.5 Resistance and Capacitance  265
5 2 # 1029
36p
# 30 3 1024
5 3 1023 # 4 3 6
10 
(6.12.1)
C 5 25.46 pF
(b)	 In this case, D and E are parallel to the dielectric interface. We may treat the capacitor
as consisting of two capacitors C1 and C2 in parallel (the same voltage across C1 and C2) as
in Figure 6.16(b).
C1 5 eoer1S/2
5 eoer1S
2d ,  C2 5 eoer2S
The total capacitance is
C 5 C1 1 C2 5 eoS
2d  1er1 1 er22
5 1029
36p
30 3 1024
2 # 15 3 10232
# 10 
(6.12.2)
C 5 26.53 pF
Notice that when er1 5 er2 5 er, eqs. (6.12.1) and (6.12.2) agree with eq. (6.22) as ­expected.
FIGURE 6.20  For Example 6.12.
PRACTICE EXERCISE  6.12
Determine the capacitance of 10 m length of the cylindrical capacitors shown in ­Figure 6.19.
Take a 5 1 mm, b 5 3 mm, c 5 2 mm, er1 5 2.5, and er2 5 3.5.
Answer:  (a) 1.54 F,  (b) 1.52 nF.
EXAMPLE 6.13
A cylindrical capacitor has radii a 5 1 cm and b 5 2.5 cm. If the space between the plates
is filled with an inhomogeneous dielectric with er 5 110 1 r2/r, where r is in centimeters,
find the capacitance per meter of the capacitor.
266  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Solution:
The procedure is the same as that taken in Section 6.5 except that eq. (6.27a) now becomes
V 5 23
2peoerrL dr 5 2
2peoL 3
ra10 1 r
2peoL 3
10 1 r 5
2peoL ln 110 1 r2 `
2peoL ln 10 1 b
10 1 a
Thus the capacitance per meter is 1L 5 1 m2
C 5 Q
V 5
2peo
ln 10 1 b
10 1 a
5 2p # 1029
36p
ln 12.5
11.0
C 5 434.6 pF/m
PRACTICE EXERCISE  6.13
A spherical capacitor with a 5 1.5 cm, b 5 4 cm has an inhomogeneous dielectric of
e 5 10eo/r. Calculate the capacitance of the capacitor.
Answer:  1.13 nF.
6.6  METHOD OF IMAGES
The method of images, introduced by Lord Kelvin in 1848, is commonly used to determine
V, E, D, and rS due to charges in the presence of conductors. By this method, we avoid
solving Poisson’s or Laplace’s equation but rather utilize the fact that a conducting surface
is an equipotential. Although the method does not apply to all electrostatic problems, it can
reduce a formidable problem to a simple one.
The image theory states that a given charge configuration above an infinite ground-
ed perfect conducting plane may be replaced by the charge configuration itself, its
image, and an equipotential surface in place of the conducting plane.
Typical examples of point, line, and volume charge configurations are portrayed in Figure
6.21(a), and their corresponding image configurations are in Figure 6.21(b).
6.6 Method of Images  267
In applying the image method, two conditions must always be satisfied:
1.	 The image charge(s) must be located in the conducting region.
2.	 The image charge(s) must be located such that on the conducting surface(s) the
­potential is zero or constant.
The first condition is necessary to satisfy Poisson’s equation, and the second condition
ensures that the boundary conditions are satisfied. Let us now apply the image theory to
two specific problems.
A. A  Point Charge above a Grounded Conducting Plane
Consider a point charge Q placed at a distance h from a perfect conducting plane of infinite
extent as in Figure 6.22(a). The image configuration is in Figure 6.22(b). The electric field
in the region above the plane at point P1x, y, z2 is given by
FIGURE 6.21  Image system: (a) charge configurations above a perfectly conducting plane,
(b) image configuration with the conducting plane replaced by equipotential surface.
FIGURE 6.22  (a) Point charge and grounded conducting plane. (b) Image configuration
and field lines.
268  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
E 5 E1 1 E2
(6.40)
Q r1
4peor1
3 1 2Q r2
4peor2
(6.41)
The distance vectors r1 and r2 are given by
r1 5 1x, y, z2 2 10, 0, h2 5 1x, y, z 2 h2
(6.42)
r2 5 1x, y, z2 2 10, 0, 2h2 5 1x, y, z 1 h2
(6.43)
so eq. (6.41) becomes
E 5
4peo
xax 1 yay 1 1z 2 h2az
3x2 1 y2 1 1z 2 h2 243/2 2
xax 1 yay 1 1z 1 h2az
3x2 1 y2 1 1z 1 h2 243/2 d 
(6.44)
It should be noted that when z 5 0, E has only the z-component, confirming that E is
normal to the conducting surface.
The potential at P is easily obtained from eq. (6.41) or (6.44) using V 5 2eL E # dl.
Thus
V 5 V1 1 V2
4peor1
4peor2
(6.45)
V 5
4peo
3x2 1 y2 1 1z 2 h2 241/2 2
3x2 1 y2 1 1z 1 h2 241/2 f
for z $ 0 and V 5 0 for z # 0. Note that V1z 5 02 5 0.
The surface charge density of the induced charge can also be obtained from eq. (6.44) as
rS 5 Dn 5 eoEn`
z50
2Qh
2p3x2 1 y2 1 h243/2
(6.46)
The total induced charge on the conducting plane is
Qi 5 3 rS dS 5 3
2Qh dx dy
2p3x2 1 y2 1 h243/2
(6.47)
By changing variables, r2 5 x2 1 y2, dx dy 5 r dr df, and we have
Qi 5 2Qh
2p 3
r dr df
3r2 1 h243/2
(6.48)
6.6 Method of Images  269
Integrating over f gives 2p, and letting r dr 5 1
2d 1r22, we obtain
Qi 5 2Qh
2p 2p 3
3r2 1 h2423/2 1
2 d1r22
3r2 1 h241/2 `
(6.49)
5 2Q
as expected, because all flux lines terminating on the conductor would have terminated on
the image charge if the conductor were absent.
B. A  Line Charge above a Grounded Conducting Plane
Consider an infinite line charge with density rL C/m located at a distance h from the
grounded conducting plane at z 5 0. This may be regarded as a problem of a long conduc­
tor over the earth. The image system of Figure 6.22(b) applies to the line charge except that
Q is replaced by rL. The infinite line charge rL may be assumed to be at x 5 0, z 5 h, and
the image 2rL at x 5 0, z 5 2h so that the two are parallel to the y-axis. The electric field
at point P is given (from eq. 4.21) by
E 5 E1 1 E2
(6.50)
2peor1
ar1 1
2rL
2peor2
ar2
(6.51)
The distance vectors 1 and 2 are given by
r1 5 1x, y, z2 2 10, y, h2 5 1x, 0, z 2 h2
(6.52)
r2 5 1x, y, z2 2 10, y, 2h2 5 1x, 0, z 1 h2
(6.53)
so eq. (6.51) becomes
E 5
2peo
c xax 1 1z 2 h2az
x2 1 1z 2 h2 2 2 xax 1 1z 1 h2az
x2 1 1z 1 h2 2 d
(6.54)
Again, notice that when z 5 0, E has only the z-component, confirming that E is normal
to the conducting surface.
The potential at P is obtained from eq. (6.51) or (6.54) using V 5 2eL E # dl. Thus
V 5 V1 1 V2
5 2 rL
2peo
ln r1 2 2rL
2peo
ln r2
5 2 rL
2peo
ln r1
(6.55)
270  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
Substituting r1 5 0 r1 0  and r2 5 0 r2 0  in eqs. (6.52) and (6.53) into eq. (6.55) gives
V 5 2 rL
2peo
lnc x2 1 1z 2 h2 2
x2 1 1z 1 h2 2 d
1/2
(6.56)
for z $ 0 and V 5 0 for z # 0. Note that V1z 5 02 5 0.
The surface charge induced on the conducting plane is given by
rS 5 Dn 5 eoEz`
z50
2rLh
p1x2 1 h22
(6.57)
The induced charge per length on the conducting plane is
ri 5 3
rS dx 5 2rLh
p  3
x2 1 h2
(6.58)
By letting x 5 h tan a, eq. (6.58) becomes
ri 5 2rLh
p  3
p/2
2p/2
5 2rL
(6.59)
as expected.
EXAMPLE 6.14
A point charge Q is located at point 1a, 0, b2 between two semi-infinite conducting planes
intersecting at right angles as in Figure 6.23. Determine the potential at point P1x, y, z2 in
region z $ 0 and x $ 0 and the force on Q.
Solution:
The image configuration is shown in Figure 6.24. Three image charges are necessary to
­satisfy the two conditions listed at the beginning of this section. From Figure 6.24(a), the
potential at point P1x, y, z2 is the superposition of the potentials at P due to the four point
charges; that is,
V 5
4peo
c 1
2 1
1 1
2 1
where
r1 5 3 1x 2 a2 2 1 y2 1 1z 2 b2 241/2
r2 5 3 1x 1 a2 2 1 y2 1 1z 2 b2 241/2
r3 5 3 1x 1 a2 2 1 y2 1 1z 1 b2 241/2
r4 5 3 1x 2 a2 2 1 y2 1 1z 1 b2 241/2
6.6 Method of Images  271
From Figure 6.24(b), the net force on Q is
F 5 F1 1 F2 1 F3
5 2
4peo12b2 2 az 2
4peo12a2 2 ax 1
Q212aax 1 2baz2
4peo3 12a2 2 1 12b2 243/2
16peo
e c
1a2 1 b22 3/2 2 1
a2 d  ax 1 c
1a2 1 b22 3/2 2 1
b2 d  az f
The electric field due to this system can be determined similarly, and the charge induced
on the planes can also be found.
In general, when the method of images is used for a system consisting of a point charge
between two semi-infinite conducting planes inclined at an angle f (in degrees), the number
of images is given by
N 5 a360°
2 b
FIGURE 6.23  Point charge between two semi-infinite
conducting planes.
FIGURE 6.24  Determining (a) the potential at P and (b) the force on charge Q.
272  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
because the charge and its images all lie on a circle. For example, when f 5 180, N 5 1 as
in the case of Figure 6.22; for f 5 90, N 5 3 as in the case of Figure 6.23; and for f 5 60,
we expect N 5 5 as shown in Figure 6.25.
FIGURE 6.25  Point charge between two semi-
infinite conducting walls inclined at f 5 60 to
each other.
PRACTICE EXERCISE  6.14
If the point charge Q 5 10 nC in Figure 6.25 is 10 cm away from point O and along the
line bisecting f 5 60, find the magnitude of the force on Q due to the charge induced
on the conducting walls.
Answer:  60.54 mN.
†6.7  APPLICATION NOTE—CAPACITANCE OF MICROSTRIP LINES
The increasing application of integrated circuits at microwave frequencies has generated
interest in the use of rectangular and circular microstrip disk capacitors as lumped-element
circuits. The fringing field effects of such capacitors were first observed in 1877 by Kirchhoff,
who used conformal mapping to account for the fringing. But his analysis was limited by
the assumption that the capacitor is air filled. In microstrip applications, the capacitor plates
are separated by a dielectric material instead of free space. Lately, others have come up with
better approximate closed-form solutions to the problem taking into account the presence of
the dielectric material and fringing. We consider only the circular disk ­capacitor.
The geometry of the circular microstrip capacitor, with radius r and separation dis­
tance d, is shown in Figure 6.26. Again, if disk area S1S 5 pr22 is very large compared
with the separation distance (i.e., !S W d), then fringing is minimal and the capacitance
is given by
C 5 eoerpr2
(6.60)
6.7 Application Note—Capacitance of Microstrip Lines  273
Several researchers have attempted to account for the effect of fringing and to obtain a
closed-form solution. We consider the following cases.
CASE 1.
According to Kirchhoff,2 the fringing capacitance is
DC 5 eoerr alog 16pr
2 1b
(6.61)
so that the total capacitance is
CT 5 eoerpr2
1 eoerr alog 16pr
2 1b
(6.62)
It should be noted that Kirchhoff’s approximation is valid only for er 5 1.
CASE 2.
According to Chew and Kong,3 the total capacitance including fringing is
CT 5 eoerpr2
e1 1 2d
perr clna r
2db 1 11.41er 1 1.772 1 d
r 10.268er 1 1.652 d f
(6.63)
CASE 3.
Wheeler used interpolation to match the three cases of small, medium, and large disk sizes.
According to Wheeler,4 we first define the following
Cks 5 eorc411 1 er2 1 erpr
d d 
(6.64)
FIGURE 6.26  Circular microstrip capacitor.
2 L. D. Landau and E. M. Lifshitz, Electrodynamics of Continuous Media. Oxford: Pergamon Press,  1960, p. 20.
3 W. C. Chew and J. A. Kong, “Effects of fringing fields on the capacitance of circular microstrip disk,” IEEE
Transactions on Microwave Theory and Techniques, vol. 28, no. 2, Feb. 1980, pp. 98–103.
4 H. A. Wheeler, “A simple formula for the capacitance of a disc on dielectric on a plane,” IEEE Transactions on
Microwave Theory and Techniques, vol. 30, no. 11, Nov. 1982, pp. 2050–2054.
274  CHAPTER 6  ELECTROSTATIC BOUNDARY-VALUE PROBLEMS
where k 5 er. When k 5 1, eq. (6.64) becomes
C1s 5 eorc8 1 pr
d d 
(6.65)
The total capacitance is
CT 5 Cks
kcC1s
C1 1 a1 2 1
bC2Cks
(6.66)
where
C1 5 eorc8 1 pr
d 1 2
ln a1 1 0.81r/d2 2 1 10.31r/d2 4
1 1 0.91r/d2
b d
(6.67)
C2 5 1 2
4 1 2.6 r
d 1 2.9 d
(6.68)
kc 5 0.37 1 0.63er
(6.69)
A MATLAB program was developed by using eqs. (6.62) to (6.69). With specific values
of d 5 10 mil and er 5 74.04, the values of C and CT for 10 , r , 200 mil are plotted in
Figure 6.27 for the three cases. The curve for Kirchhoff’s approximation coincides with the
case without fringing.
250
200
150
100
Capacitance (pF)
200
180
160
140
120
100
Radius (mil)
Chew and Kong
Wheeler
Kirchhoff, without fringing
FIGURE 6.27  Capacitance of the circular microstrip capacitor.

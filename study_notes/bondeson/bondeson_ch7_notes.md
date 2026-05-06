# Bondeson《Computational Electromagnetics》第7章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 167-203 of 231 (231 total)

---

## The Method of Moments

7 The Method of Moments
as the capacitance calculation in Chapter 3, where the potential is known on
conducting boundaries and charges occur only on these boundaries. Then, the
potential φ was given on the boundaries, φ = φspec = 0 on the outer conductor
and φ = φspec = 1 on the inner one. As an alternative to solving Laplace’s
equation for the potential in the vacuum region, we can calculate the charges
ρs on the conducting walls S by solving the integral equation
ρs(r′)
4πϵ0|r −r′|dS′ = φspec(r).
(7.3)
In the 2D capacitor problem, the surface integral reduces to a line integral,
and we instead use the potential from a line charge −(ρl/2πϵ0) ln |r −r′| as
weighting, that is,
2πϵ0
ρl(r′) ln |r −r′|dl′ = φspec(r).
(7.4)
Here, we “derived” the integral equations by referring to well-known expres-
sions from electrostatics. However, it is useful to derive them in a more math-
ematical fashion, and also introduce the concept of a Green’s function. The
same procedures will be used to derive the electric ﬁeld integral equation for
the complete Maxwell system.
A characteristic property of the integral formulation is that it deals readily
with open geometries. Consider the parallel plate capacitors illustrated in
Figure 7.1. In Figure 7.1(a), the capacitor is enclosed in a conducting box,
and in this case, diﬀerential equation solvers such as ﬁnite diﬀerences or ﬁnite
elements work well. However, if there is no surrounding box, these methods
have diﬃculties with truncating the open computational region, whereas the
MoM works very well and has no diﬃculties with the open geometry; see
Figure 7.1(b). (In fact, the open geometry simpliﬁes the MoM calculation,
because it reduces the number of surfaces on which charges can reside.)
7.1.1 Green’s Function
Here, we introduce the concept of a Green’s function G(r, r′), which represents
the “ﬁeld” at r produced by a point source at r′. In electrostatics, the Green’s
function represents the electric potential at r produced by a unit charge at
r′. In three dimensions, this is
G(r, r′) =
4πϵ0|r −r′|.
(7.5)
We will show how the Green’s function for electrostatics can be found by
solving Poisson’s equation. This also serves as a preparation for the more
complicated time-harmonic case, treated in Section 7.3.
The potential from a point charge in three dimensions satisﬁes Poisson’s
equation,
7.1 Integral Formulation of Electrostatics
Fig. 7.1. Parallel plate capacitor in (a) closed geometry and (b) open geometry.
Diﬀerential equation solvers can easily deal with the closed geometry (a), but the
MoM is better adapted to deal with the open geometry (b).
−ϵ0∇2φ(r) = δ3(r −r′).
(7.6)
Here, δ3(r −r′) is the 3D Dirac delta function, which represents a unit point
charge. It vanishes at all r ̸= r′, and at r = r′ it is inﬁnitely large, in such a
way that the total charge
V δ3(r −r′)dV = 1 for all volumes V where r′ is
an interior point. The solution φ(r) to (7.6) is the Green’s function G(r, r′).
Thus, for electrostatics,
−ϵ0∇2
rG(r, r′) = δ3(r −r′),
(7.7)
where the subscript r indicates that the diﬀerential operator acts on the r
argument, the ﬁeld point. By symmetry, the electrostatic potential that solves
(7.7) can depend only on the distance R = |r −r′| between the source and
observation point. Therefore, except at the singularity R = 0, G satisﬁes
dRR2 dG
dR = 0,
R > 0.
(7.8)
This equation has two types of solutions, G1 = a1 and G2 = a2/R, where a1
and a2 are constants. The solution G1 = a1 is not of interest, since it produces
no electric ﬁeld. Therefore, the relevant solution of (7.7) is
G = G2 = a2
The coeﬃcient a2 can be determined by integrating (7.7) over a sphere with
(the arbitrary) radius R0 around the source point. In physical terms, this
7 The Method of Moments
means that we equate the ﬂux of electric displacement D = ϵ0E through the
surface of the sphere to the enclosed charge. By means of Gauss’s theorem,
the integral of the left-hand side of (7.7) is
R<R0
∇· ∇GdV = −ϵ0
R=R0
∇G · ˆndS
= −ϵ0
· 4πR2
0 = 4πϵ0a2
(7.9)
This must be equal to the integral of the right-hand side (the enclosed charge),
which is unity by deﬁnition. Therefore, a2 = 1/4πϵ0, so the Green’s function
for 3D electrostatics is
G(r, r′) =
4πϵ0|r −r′|.
(7.10)
To be precise, we add that the Green’s function derived here is the one valid
for free space, with no boundaries. The Green’s function can also be deﬁned
for cases with conductors and dielectrics, but then one needs more elaborate
methods to calculate it.
Assuming that all the charges reside on the surfaces of conductors, the
potential can be written as
φ(r) =
Conductors
G(r, r′)ρs(r′)dS′.
(7.11)
The two formulations, Poisson (7.1) and Coulomb (7.2) or (7.11), are
equivalent. To see that, we apply the Laplace operator to (7.11), and use
rG(r, r′) = −δ3(r −r′)/ϵ0 to verify that the potential satisﬁes Poisson’s
equation (7.1)
G(r, r′)ρ(r′)dV ′ =
rG(r, r′)]ρ(r′)dV ′
= −1
δ3(r −r′)ρ(r′)dV ′ = −ρ(r)
Therefore, the integral formulation (7.11) is equivalent to Poisson’s equation.
7.1.2 General Formulation
After having formulated the electrostatic potential problem as an integral
equation, we can formalize the idea to a more general problem.
Consider a diﬀerential equation
Df = s,
(7.12)
7.1 Integral Formulation of Electrostatics
where D is a diﬀerential operator, f is a ﬁeld, and s is the source distribution.
Let G(r, r′) be the ﬁeld at r produced by a point source at r′, that is, G
satisﬁes
DrG(r, r′) = δ3(r −r′).
(7.13)
By the principle of superposition, which holds for linear systems, the diﬀer-
ential equation (7.12) can be rewritten as the integral equation
f(r) =
G(r, r′)s(r′)dV ′.
(7.14)
Direct substitution shows that (7.14) is a solution to (7.12).
The integral formulation is eﬃcient when the sources reside on small sur-
faces, and it deals very easily with problems in “open” geometry, where dif-
ferential equation solvers have diﬃculties.
7.1.3 FEM Solution
Usually some parts of ﬁnite element methodology are used for solving the
integral equation. The procedures will be outlined in this section.
Basis Functions
The charge distribution is expanded in, say, N basis functions sk(r):
ρs(r) =
aksk(r).
(7.15)
In early applications of the MoM, the basis functions were often chosen as
global functions, and one tried to use as much knowledge of the solution as
possible to ﬁnd expansions that gave accurate results with a small number of
basis functions (sometimes only 1!). Nowadays, it is more common to divide
the surfaces with sources into small elements and use local basis functions.
This requires less knowledge and works for much more general problems.
For convenience of notation, we introduce the potential generated by a
basis function:
φk(r) =
G(r, r′)sk(r′)dS′.
(7.16)
Then, the approximate potential becomes
¯φ(r) =
akφk(r).
(7.17)
7 The Method of Moments
Fig. 7.2. Suitable 2D grid for MoM solution of an electrostatics problem. The charge
density can be expanded in piecewise constants, and the matching points (o) can be
placed at the center of each element.
Testing Procedures
We want to enforce the condition ¯φ = φspec on the conducting surfaces where
the potential is known; that is, minimize the residual r = 
k akφk −φspec on
the conductors. Two methods are commonly used for minimizing the residual.
Point matching, also known as collocation and the Nystrom method.
Choose testing points rj,
j = 1, 2, . . . , N (as many as the basis func-
tions), and impose
¯φ(rj) = φspec(rj),
j = 1, 2, . . . , N.
(7.18)
To get a well-behaved scheme, the testing points should be chosen so that
each feels mainly the eﬀects of one particular basis function. If this criterion
is not fulﬁlled, the computed charge distribution may show a spurious os-
cillatory behavior, simply because the oscillating components of the charge
distribution are not detected at the observation points. A good recipe for
electrostatics is to choose piecewise constant basis functions and place the
collocation points in the middle of each element, as shown in Figure 7.2.
Weighted residuals. Choose weighting functions wj, j = 1, 2, . . . , N (as
many as the basis functions), and impose
Conductor
wj(r)[¯φ(r) −φspec(r)]dS = 0.
(7.19)
Here Galerkin’s method uses wj(r) = sj(r). If we use global basis func-
tions, as was common practice in the early applications of the boundary
element method, Galerkin’s weighting procedure (7.19) can be seen as a
way of taking moments of the mismatch in the potential. This is why
the electromagnetics community usually refers to the boundary element
7.2 Capacitance Problem in an Unbounded 2D Region
method as the MoM. Point matching corresponds to taking the test func-
tions as delta functions wj(r) = δ(r −rj).
The integrations required for (7.18) and (7.19) are generally done numer-
ically, and the singularity of the Green’s function at r = r′ needs particular
attention.
Both collocation and the method of weighted residuals lead to an N × N
system of equations
Ajkak = bj,
j = 1, 2, . . . , N,
Ajk =
wj(r)φk(r)dS =
dS wj(r)
dS′ G(r, r′)sk(r′),
bj =
wj(r)φspec(r)dS.
(7.20)
For the self-adjoint Poisson’s equation, the Green’s function is symmetric,
G(r, r′) = G(r′, r), which is referred to as reciprocity. If one uses Galerkin’s
method to construct the MoM equations in (7.20), the matrix also becomes
symmetric, i.e., Ajk = Akj.
Review Questions
7.1-1 Compare integral formulations with diﬀerential equation formulations.
Mention some pros and cons of integral formulations.
7.1-2 Give an example of suitable weighting and basis functions for (7.3).
7.1-3 What is a Green’s function?
7.1-4 Derive the Green’s function for Poisson’s equation in 3D free space.
7.1-5 Why does the electromagnetics community refer to boundary element
methods as method of moments?
7.1-6 Generalize the technique for square elements, demonstrated in Sec-
tion 7.1.3, to a discretization that consists of triangles. Is it possible to
combine squares and triangles? Could such a combination be useful?
7.1-7 What is the diﬀerence between point matching and weighted residuals?
7.2 Capacitance Problem in an Unbounded 2D Region
We will illustrate the MoM by solving a simple problem: calculate the ca-
pacitance per unit length of two equal and parallel conducting strips in free
space, as illustrated in Figure 7.3. The MoM is particularly useful for this
open geometry.
To set up the equations for a 2D geometry, we note that the poten-
tial from a line charge at r′ = (x′, y′), with line charge density density ρl
(Coulomb/meter), is
7 The Method of Moments
-V / 2, -Q
+V / 2, +Q
Fig. 7.3. Cross section of the capacitor.
φ = −ρl
2πϵ0
ln |r −r′|
where r0 is an arbitrary constant. For the parallel plate capacitor, this gives
φ(x, y) = −
2πϵ0
 w/2
−w/2
x′, a
(x −x′)2 +
y −a
2πϵ0
 w/2
−w/2
x′, −a
(x −x′)2 +
y + a
dx′(7.21)
This particular problem has two symmetries, both left–right symmetry,
ρs(−x′, a/2) = ρs(x′, a/2),
and up–down antisymmetry
ρs(x′, −a/2) = −ρs(x′, a/2).
7.2.1 Integration
We divide each capacitor plate into elements x′ ∈[xi, xi+1] and use piecewise
constant basis functions to represent the charge density. The testing will be
done as point matching at the midpoints of each element xtest,i = xi+ 1
2(xi + xi+1). This gives a good coupling between each basis function, which
is constant on an element, and the corresponding testing point. If we chose
the testing points as the nodes, they would not be able to detect the potential
resulting from a charge distribution where neighboring elements have opposite
charges, because contributions from two adjacent elements cancel at a node
on the element boundary.
To get the potential from a piecewise constant charge distribution, we need
to integrate. The singular kernel complicates the integration over the element
7.2 Capacitance Problem in an Unbounded 2D Region
on which the observation point is located, but the piecewise constant elements
in 2D allow an exact analytical integration
I(xs, xe, d) = −
2πϵ0
 xe
x2 + d2 dx
2πϵ0
2x ln(x2 + d2) −x + d arctan(x/d)
(7.22)
This simpliﬁcation is helpful, and we will use it. If we take into account the
left–right symmetry and up–down antisymmetry, it is enough to discretize
only the right half of the upper plate. We divide this into N elements with
endpoints xi, i = 0, 1, 2, . . . , N. Then the potential at the point (x, y) from
the assumed charge distribution can be written as
φ(x, y) =
ρi+ 1
2 [ I(xi −x, xi+1 −x, y −a/2)
+I(−xi+1 −x, −xi −x, y −a/2)
−I(xi −x, xi+1 −x, y + a/2)
−I(−xi−1 −x, −xi −x, y + a/2)].
(7.23)
By choosing the testing points as xi+ 1
2 for i = 0, 1, . . . , N −1, on the upper
plate we get the system of equations
Ar = v,
where
Aij = I(xj −xi+ 1
2 , xj+1 −xi+ 1
2 , 0) + I(−xj+1 −xi+ 1
2 , −xj −xi+ 1
2 , 0)
−I(xj −xi+ 1
2 , xj+1 −xi+ 1
2 , a) −I(−xj+1 −xi+ 1
2 , −xj −xi+ 1
2 , a),
and v is a column vector where all the elements are set to the potential on
the upper plate V/2, where V is the voltage across the capacitor. Solution of
this system will give the charge density on each element in the vector r.
7.2.2 MATLAB: MoM for General, 2D Geometries
In the introductory example, we treated a very simple geometry, with a high
degree of symmetry and plane plates. However, it is easy to generalize this to
a completely general 2D geometry with no symmetry and curved conductors.
Figure 7.4 shows one element and the observation point, which is assumed to
lie at the normal distance d from a straight-line extension of the element. The
contribution from this element to the potential at the observation point is
2πϵ0
 ξe
x2 + d2 dx = −ρs
2πϵ0
2x ln(x2 + d2) −x + d arctan(x/d)
(7.24)
7 The Method of Moments
    
    
    
element
charge
observation point
Fig. 7.4. Coordinates aligned with an element.
In the following routine, we use the exact integration to generate the sys-
tem matrix for point matching and general 2D geometry. Each charge-carrying
element is speciﬁed by the arrays xs and ys for the starting coordinates, xe
and ye for the endpoints, and phi for the potential. No assumption about the
geometry of the plates is used.
% --------------------------------------------------------------
% Compute charge distribution for 2D electrostatics by MoM
% --------------------------------------------------------------
function [charge, sigma] = MoM2D(xs, ys, xe, ye, phi)
% Arguments:
= x-coordinate for starting points
= y-coordinate for starting points
= x-coordinate for ending points
= y-coordinate for ending points
= the potential
% Returns:
sigma
= charge density for each element
charge = total charge on each element
xobs = 0.5*(xs + xe);
% Observation points
yobs = 0.5*(ys + ye);
h = sqrt((xe-xs).ˆ2 + (ye-ys).ˆ2);
% Length of elements
% Loop over elements
for k = 1:length(xs)
s = (
(xobs-xs(k))*(xe(k)-xs(k)) ...
+ (yobs-ys(k))*(ye(k)-ys(k)))/h(k)ˆ2;
d = sqrt(
(xobs-xs(k)).ˆ2 ...
+ (yobs-ys(k)).ˆ2 ...
- s.ˆ2*h(k)ˆ2 + 1e-24);
xis = -s*h(k);
xie = (1-s)*h(k);
7.2 Capacitance Problem in an Unbounded 2D Region
temp =
0.5*xie.*log(xie.ˆ2+d.ˆ2) ...
- xie + d.*atan(xie./d) ...
-(0.5*xis.*log(xis.ˆ2+d.ˆ2) ...
- xis + d.*atan(xis./d));
A(:,k) = - temp(:)/(2*pi*8.854187);
sigma = (A\phi’)’;
% Charge density
charge = h.*sigma;
% Charge per element
[The theory behind the geometrical transformations is that a point on
the straight line through rs = (xs, ys) and re = (xe, ye) is r = rs + s(re −
rs), −∞< s < ∞. The minimum distance d on this line to the observation
point at ro occurs for s = (ro −rs) · (re −rs)/|re −rs|2 and it is given by
d2 = |ro −rs|2 −[(ro −rs) · (re −rs)]2/|re −rs|2.]
The routine gives the charge on the elements, and this can be summed to
compute the capacitance per meter. For this example, we initiate the potential
to 0.5 V on the top plate and −0.5 V on the bottom one. Then the capacitance
is the sum of the charges on the top plate. The computation can be called as
follows (where n must be an even integer):
a = 1;
% Separation distance between capacitor plates
w = 1;
% Width of capacitor plates
= 10;
% Number of unknowns
nh = round(n/2); % Number of elements on each plate
= a/nh;
% Length of the elements
% X-coordinates for starting and ending points
xs = zeros(1,n);
xe = zeros(1,n);
xs(1:nh)
= linspace(0,a-h,nh);
xs(nh+1:2*nh)
= linspace(0,a-h,nh);
= xs + h;
% Y-coordinates for starting and ending points
ys = zeros(1,n);
ye = zeros(1,n);
ys(1:nh)
= 0.5*w;
ys(nh+1:2*nh)
= -0.5*w;
= ys;
% Potential for the elements
= zeros(1,n);
V(1:nh)
= 0.5;
V(nh+1:2*nh)
= -0.5;
% Solve the electrostatic problem
[charge, sigma] = MoM2D(xs, ys, xe, ye, V);
C = sum(charge(1:nh))
7 The Method of Moments
The results from runs with varying numbers of points are shown in Ta-
ble 7.1. Figure 7.5 shows that the convergence is linear in h.
n [-]
h [m]
C [pF/m]
0.20000 18.03138 50
0.10000 18.37294 02
0.06666 18.49101 21
0.04000 18.58699 26
0.02857 18.62854 17
100 0.02000 18.65986 68
140 0.01428 18.68082 79
200 0.01000 18.69658 95
Table 7.1. Capacitance for a = w = 1, uniform grid and analytic integration.
0.05
0.15
18.1
18.2
18.3
18.4
18.5
18.6
18.7
18.8
h [m]
C [pF/m]
Fig. 7.5. Capacitance for a = w = 1, uniform grid and analytic integration, plotted
versus h.
Accurate values can be obtained from extrapolation using polynomial
ﬁts. A linear ﬁt gives C = 18.72858 78 (pF/m), quadratic 18.73349 99, cu-
bic 18.73350 34, quartic 18.73350 27, and quintic 18.73350 27. The answer to
nine digits is 18.73350 27 pF/m. For a single computation to get to within 1%
of the correct answer, about 50 elements are needed.
7.2 Capacitance Problem in an Unbounded 2D Region
7.2.3 Charge Distribution
The charge distribution on the top plate, resolved with 15 elements, is shown
in Figure 7.6.
x [m]
ρs [C/m2]
Fig. 7.6. Charge distribution on the top plate, resolved by 15 elements in a uniform
grid. The relative error of the computed capacitance is 1.3%.
The charge distribution for the parallel plate capacitor is singular. In this
respect it is similar to the capacitance problem in Chapter 3. The nature
of such singularities can be determined analytically. As an analytically solv-
able illustration, we consider the behavior of the electrostatic potential in the
vicinity of a conductor edge in vacuum, that is, a 2D corner.
Fig. 7.7. Conducting edge.
Suppose the conductor subtends an angle β < 180o, and the vacuum
region, where the potential satisﬁes Laplace’s equation, subtends the angle
α = 360o −β > 180o; see Figure 7.7. In cylindrical coordinates, with the edge
7 The Method of Moments
oriented along the z-axis, the potential φ satisﬁes
∂rr∂φ
∂r + 1
∂θ2 = 0,
0 < θ < α,
(7.25)
and φ = 0 for θ = 0, α. Relevant solutions can be found by the method
of separation of variables φ(r, θ) = f(r)g(θ). Substituting this ansatz into
Laplace’s equation (7.25) and multiplying by r2/(f(r)g(θ)), we obtain
r(rf ′(r))′
f(r)
= −g′′(θ)
g(θ) .
Since the left-hand side depends only on r and the right-hand side only on
θ, both must be constant, say p2. This gives g(θ) = a sin pθ + b cos pθ and
f(r) = crp + dr−p. If p > 0 we must choose d = 0 to keep the potential
bounded. Thus, the acceptable solutions of separable form are
φ = (a sin pθ + b cos pθ)rp.
Next, we want to determine the power p. The boundary condition φ = 0 at
θ = 0 gives b = 0, and φ = 0 at θ = α then gives pα = nπ, n = integer.
Thus, the lowest-order solution is φ = rp sin pθ with p = π/α. For a general
opening angle α, the power p is noninteger and the smallest p is less than
one if α > π. For this solution, both Er and Eθ vary as r(−1+π/α). Thus, the
ﬁeld components tend to inﬁnity at the corner if α > π. For the edge of the
capacitor plate we have α = 2π, so that Eθ ∝r−1/2. This implies that the
charge density on the plate varies as r−1/2 near the edge.
7.2.4 Adaptivity
We will use the parallel plate capacitor to illustrate the beneﬁts of adaptive
grid reﬁnement. The elements in the middle of the strips, where the charge
density is small, give small contributions to the total charge and capacitance.
Some of these elements would be more eﬃciently used near the edges, where
the charge density is high. A simple rule of thumb, which works well for
adjusting the length of an element in an adaptive grid, is that the total charge
on each element should be the same.
We initialize the computation with a grid where the elements have equal
length to compute a ﬁrst approximation. Then, the computed charge distri-
bution can be used to generate a new grid where one seeks to distribute the
charge uniformly on the elements. Such a routine is easy to implement, how-
ever, the procedure needs to be iterated several times to equalize the charge
on the elements enough for a careful convergence study. The adaptively com-
puted capacitance values are given in Table 7.2.
A plot versus h2 shows that the adaptivity has restored the O(h2) [i.e.,
O(N −2)] convergence that one expects for a smooth charge distribution. Now
7.2 Capacitance Problem in an Unbounded 2D Region
x [m]
ρs [C/m2]
Fig. 7.8. Charge distribution on the top plate, resolved by 15 elements in an adap-
tive grid (equal charge). The relative error of the computed capacitance is 0.28%.
The areas of the bars correspond to the charges on the corresponding elements.
n [-]
h [m]
C [pF/m]
0.20000 18.32465 80
0.10000 18.61846 85
0.06666 18.68061 49
0.04000 18.71396 25
0.02857 18.72342 35
100 0.02000 18.72852 34
140 0.01428 18.73094 84
200 0.01000 18.73224 60
Table 7.2. Capacitance for a = w = 1 and adaptive mesh.
we get 1% accuracy with fewer than 20 elements, compared to about 50 for a
uniform grid. On the other hand, the calculation for each cell size had to be
repeated several times to adapt the grid, so we have not really won in terms
of computing time. The main use of adaptivity is in large 3D problems, where
suﬃcient accuracy cannot be obtained without adaptivity. Another approach,
which may minimize the computing time, is handmade adaptivity, where one
uses knowledge about the geometry and the singularities to construct meshes
that resolve the solution as well as possible with the available number of
elements.
Even though the lowest order error for the adaptive grid is proportional to
h2, the extrapolations based on ﬁtting the computed results to polynomials
in h2 are not very accurate. The reason for this is that the power series
for the adaptive results also contains odd powers of h, such as h3 and h5.
If we ﬁt the results versus polynomials in h, quadratic extrapolation gives
18.73732 85, quartic 18.73351 51, and sixth-order 18.73350 26. The adaptive
7 The Method of Moments
grid strongly improves the accuracy for a given number of elements, but in
fact, the extrapolated results are somewhat less accurate than for a uniform
grid.
7.2.5 Numerical Integration
As an alternative to exact analytical integration, one can use numerical in-
tegration. Then, the logarithmic singularity causes diﬃculties, and there are
several possibilities to deal with this. Letting x represent points at the middle
of an element, we could choose:
Midpoint integration:
 x+h/2
x−h/2 f(x′)dx′ ≈hf(x). This diverges for the “self
contribution” where the observation point is the midpoint of the element
xobs = x.
Trapezoidal rule:
 x+h/2
x−h/2 f(x′)dx′ ≈1
2h[f(x −h/2) + f(x + h/2)] (relative
error O(h2) for regular functions). However, this gives a large error for
f(x) = ln x.
Gaussian integration:
 x+h/2
x−h/2 f(x′)dx′ ≈1
2h[f(x1) + f(x2)], where x1,2 =
x ± (h/2)/
3, error O(h4) for regular functions. This, too, gives a large
error if f(x) = ln x.
Special integration for a logarithmic singularity
 x+h/2
x−h/2
f(x′)dx′ ≈1
2h[f(x1) + f(x2)],
x1,2 = x ± (h/2)/e.
The error is O(h2) for regular functions, and the formula is exact for
f(x) = ln x.
To test these integration schemes, we compare results for the approxima-
tions
 x+h/2
x−h/2
f(x)dx ≈h
2 [f(x −ηh/2) + f(x + ηh/2)]
(7.26)
with diﬀerent values of the parameter η. Tests show that η ≈1/e gives the
most accurate results. Results for numerical integration and the two-strip
capacitor, with η = 1/e with and without adaptivity, are shown in Table 7.3.
For η = 1/e, the convergence on a uniform grid is close to linear in h.
Polynomial ﬁts to the results for a uniform grid in Table 7.3 gives the fol-
lowing extrapolations: for a linear ﬁt 18.781, a quadratic ﬁt 18.757, and a
cubic ﬁt 18.747. This is less accurate than for the exact integration because
the integration scheme does not properly account for the contributions from
neighboring cells, which are also aﬀected by the singularity of the Green’s
function.
Figure 7.9 shows the results for the analytic and numerical integration with
adaptive grid reﬁnement. Evidently, errors can come from the integration as
7.2 Capacitance Problem in an Unbounded 2D Region
n [-]
h [m]
C [pF/m]
C [pF/m]
uniform
adaptive
0.20000 18.14722 18.48546 67
0.10000 18.44493 18.71508 74
0.06666 18.54435 18.74847 85
0.04000 18.62297 18.75628 29
0.02857 18.65609 18.75413 22
100 0.02000 18.68052 18.75026 85
140 0.01428 18.69650 18.74659 82
200 0.01000 18.70824 18.74326 22
Table 7.3. Capacitance for a = w = 1 with numerical integration (7.26), η = 1/e,
and with uniform and adaptive mesh.
0.01
0.02
0.03
0.04
18.3
18.4
18.5
18.6
18.7
18.8
h [m ]
C [pF/m]
analytic integration
numerical integration η = 1/e
Fig. 7.9. Results for numerical and analytic integration and adaptive mesh versus
well as from the expansion in ﬁnite elements, but the diﬀerence between the
exact and numerical integration is rather small, about 1% on the coarsest
grid.
Review Questions
7.2-1 Why is point-matching attractive for a charge distribution that is ex-
panded in piecewise constant basis functions?
7 The Method of Moments
7.2-2 Derive, in two dimensions, the asymptotic behavior for the electrostatic
potential and ﬁeld in the vicinity of a metal corner with an opening angle
7.2-3 Adaptivity typically involves solving the same problem several times,
which implies some additional work. Still, adaptivity is often very useful.
Why?
7.2-4 Describe a simple adaptive scheme for a parallel plate capacitor prob-
lem.
7.2-5 List some integration rules that can be used for (7.21).
7.2-6 Mention an example in which numerical integration can be useful.
7.3 Electromagnetic Scattering
The MoM is frequently applied to scattering problems in the frequency do-
main. Electromagnetic scattering can be used for many detection applications,
such as detecting aircraft by radar. A more demanding goal is to determine
the properties of the scattering object from the scattered ﬁeld. This is called
inverse scattering, which is an important method for nondestructive testing.
The MoM is also used for magnetostatics [70] and eddy current problems,
for example to handle currents induced on thin conducting shells. The book
of Peterson [51] gives a good account of how the MoM can be applied to
electromagnetic scattering problems.
Consider a plane wave Ei incident on a perfectly conducting object. The
incident wave produces surface currents Js on the conductor, which generate
a scattered electric ﬁeld Es. The scattered ﬁeld is determined by the boundary
condition
ˆn × (Ei + Es) = 0,
r ∈∂Ωc,
(7.27)
which states that the total tangential electric ﬁeld vanishes on the conductor
surface ∂Ωc. This is used for the electric ﬁeld integral equation.
7.3.1 Representation by Potentials and a Lorentz Gauge
To determine the surface currents, we express the scattered ﬁeld Es in terms
of Js, which means that we must ﬁnd the appropriate Green’s function. (Note
that the incident wave has sources far away from the scatterer, “at inﬁnity.”)
For this purpose, it is convenient to introduce scalar and vector potentials
such that
E = −∇φ −∂A
∂t ,
B = ∇× A.
(7.28)
With this representation, Faraday’s law ∂B/∂t = −∇× E is automatically
satisﬁed. We substitute the potential representation (7.28) into Amp`ere’s law
∇× B = µ0J + ϵ0µ0
∂t .
(7.29)
7.3 Electromagnetic Scattering
Using ∇× B = ∇× ∇× A = ∇(∇· A) −∇2A (and assuming exp(jωt) time
dependence), this gives
∇(∇· A) −∇2A = µ0J −jωϵ0µ0(∇φ + jωA).
(7.30)
As pointed out previously for eddy current problems, the potentials A and φ
are not uniquely determined; one can always make a “gauge transformation”
A′ = A + ∇U and φ′ = φ −∂U/∂t without changing the physical ﬁelds E
and B. To solve for the potentials uniquely, we have to specify a condition
that determines the gauging potential U. This is called the gauge condition.
One choice that makes (7.30) particularly easy to solve is the Lorentz gauge,
which makes the two gradient terms in (7.30) cancel:
∇· A = −jωϵ0µ0φ.
(7.31)
Equation (7.30) with the Lorentz gauge condition (7.31) reduces to the vector
Helmholtz equation
∇2 + ω2
A = µ0J.
7.3.2 Green’s Function for the Vector Potential
The Cartesian components of A satisfy scalar Helmholtz equations
−(∇2 + k2)Ai = µ0Ji,
k = ω/c,
(7.32)
which can be solved component by component. Here, the subindex i is x, y, or
z. The Helmholtz equation (7.32) is similar to Poisson’s equation, for which
we derived the integral representation in Section 7.1. We proceed in similar
ways here.
We deﬁne the Green’s function for the vector potential G(r, r′) as the ith
component of the vector potential produced by a “point current” in the ith
direction J = ˆxiδ3(r −r′). Then, G satisﬁes
r + k2
G(r, r′) = δ3(r −r′).
(7.33)
The vector potential constructed by superposition
Ai(r) =
G(r, r′)Ji(r′)dV ′
(7.34)
then satisﬁes the Helmholtz equation (7.32).
The derivation of the Green’s function closely parallels that in electrostat-
ics. We start by noting that G(r, r′) can depend only on the distance between
the source and observation points R = |r−r′|. Therefore, in three dimensions,
(7.33) gives
7 The Method of Moments
dRR2 dG
dR + k2G
= 0,
R > 0.
It is easy to verify that two independent solutions of this equation are G1 =
exp(jkR)/R and G2 = exp(−jkR)/R. When these are combined with the
assumed exp(jωt) time dependence, G1 produces constant phase surfaces such
that kR+ωt is constant, or dR/dt = −ω/k = −c. That is, the constant phase
surfaces move towards the source with the speed of light. Thus G1 represents
incoming waves, which are absorbed by the “source” currents, and these waves
are called advanced solutions. Although they are indeed solutions of Maxwell’s
equations, they do not respect the principle of causality, and are not of physical
interest. For G2 ∝exp(−jkR)/R, on the other hand, the constant phase
surfaces satisfy dR/dt = ω/k = c, so G2 represents waves radiated away from
the source. These solutions respect causality and are called retarded. They
are the relevant solutions to (7.33). Thus, we pick G(r, r′) = a exp(−jkR)/R.
To determine the normalization constant a, we proceed as in Section 7.1.1.
Integrate (7.33) over a sphere of radius R0, and to simplify the evaluation, we
let R0 tend to zero. The integral of the left-hand side becomes
R<R0
r + k2
G dV = −1
R<R0
∇r · ∇rG dV + O(k2R2
Only the ﬁrst term remains nonzero in the limit R0 →0. By Gauss’s theorem,
this piece can be rewritten as a surface integral
R=R0
∇G · ˆn dS = −1
R=R0
4πR2
= −a
exp(−jkR0)4πR2
→4πa
R0 →0.
This must be equal to the integral over the right-hand side in (7.33), which is
1 by deﬁnition. Therefore, the normalizing coeﬃcient is a = µ0/4π, and the
Green’s function for the vector potential is
G = µ0
exp(−jkR)
R = |r −r′|.
(7.35)
Using superposition and the fact that all currents occur on the surfaces
of conductors, we can write the solution of (7.32) for each component of the
vector potential as
Ai(r) =
G(r, r′) ˆxi · Js(r′) dS′
with the Green’s function (7.35), where ˆxi · Js is component i of the surface
current Js. Therefore, the full vector potential is
7.3 Electromagnetic Scattering
A(r) = µ0
exp(−jkR)
Js(r′)dS′.
(7.36)
We can ﬁnd an equation for the scalar potential φ by taking the divergence
of Amp`ere’s law (7.29), substituting the potential representation for E, and
using the Lorentz gauge condition
−(∇2 + k2)φ =
∇· J = ρ
(7.37)
Here, we used the equation of continuity for charge
jωρ + ∇· J = 0.
Equation (7.37) is again a scalar Helmholtz equation with the solution
φ(r) =
4πϵ0
exp(−jkR)
ρ(r′)dS′.
(7.38)
7.3.3 The Electric Field Integral Equation
We now have expressions for the potentials in terms of the surface currents.
The scattered electric ﬁeld is given by
Es = −jωA −∇φ
= −jωµ0
exp(−jkR)
Js(r′)dS′
4πϵ0ω ∇
exp(−jkR)
∇′ · Js(r′)dS′.
(7.39)
The condition the surface currents have to satisfy is that the tangential compo-
nent of the total ﬁeld, which is the sum of the incident ﬁeld and the scattered
ﬁeld generated by the surface currents, vanish on the surface of the conductor:
tan + Ei
tan = 0.
(7.40)
Combining this with (7.39), we obtain the electric ﬁeld integral equation
(EFIE)
tan = jωµ0
exp(−jkR)
Js(r′)dS′

4πϵ0ω ∇
exp(−jkR)
∇′ · Js(r′)dS′

(7.41)
Unfortunately, integral equations such as the EFIE are somewhat diﬃcult
to solve numerically. First of all, as will be discussed in Section 7.4, it is neces-
sary to take proper account of the singularity in the Green’s function to get a
7 The Method of Moments
scheme that converges to the correct answer when the resolution is increased.
The presence of this singularity causes diﬃculties for the integration. Numer-
ical integration schemes that work well for smooth integrands can give very
inaccurate results, and in practice, the singularity needs special treatment.
One successful approach is to pull out some simpliﬁed part of the Green’s
function that contains the singularity and use an analytic integration for this
part. The remaining, nonsingular, part of the Green’s function can then be
integrated by a standard numerical integration formula.
A more physics-related diﬃculty with the EFIE is the presence of “internal
resonances.” Consider a scattering problem in which the scatterer consists of
a closed PEC surface, e.g., a conducting sphere. If we solve this problem using
the EFIE, the integral equation has no information to tell it that the interior
of the sphere is conducting. Therefore, the EFIE allows cavity eigenmodes
that are internal to the sphere. At the resonance frequencies for these modes,
they can be part of the solution without excitation by external sources, and
the system matrix becomes singular. There is a cure for the problem of inter-
nal resonances, which consists in adding the magnetic ﬁeld integral equation
(MFIE) to the EFIE. The MFIE has diﬀerent internal resonances than the
EFIE, and with a suitable weighting of the two integral equations, all internal
resonances are eliminated [51]. The summed equation is called the combined
ﬁeld integral equation (CFIE).
FEM Solution
To solve the EFIE (7.41) for a 3D problem using ﬁnite elements and Galerkin’s
method, we ﬁrst need a suitable base for expanding Js:
Js(r) =
aisi(r).
(7.42)
To see what kind of elements are required, we work out the form of the matrix
elements, which are obtained by multiplying the EFIE by a test (= basis)
function si(r) and integrating over the PEC surfaces. We integrate the second
term in (7.41) by parts and assume that no current can leave or enter the
conductor, so that the edge term vanishes:
si · ∇φ dS =
[∇· (siφ) −φ∇· si] dS
∂∂Ωc
ˆn · siφ dl −
φ∇· si dS = −
φ∇· si dS.
This then gives the system of equations
si · Ei
tan dS =
Aijaj,
(7.43)
7.3 Electromagnetic Scattering
where the matrix elements are given by
Aij = −jωµ0
si(r) ·
sj(r′)exp(−jkR)
dS′dS
4πϵ0ω
∇· si(r)
∇′ · sj(r′)exp(−jkR)
dS′dS. (7.44)
Choice of Elements
Equation (7.44) indicates that we need basis functions for which ∇· s is
nonsingular. This requirement is diﬀerent from that for the diﬀerential form
of Maxwell’s equations, where ∇× E has to be square integrable. For the
diﬀerential formulation of Maxwell’s equations, the successful choice is curl-
conforming edge elements, whose tangential component is continuous at cell
interfaces. The integral formulation requires divergence-conforming elements,
whose normal component is continuous across cell boundaries. For a 2D prob-
lem with a 1D boundary, say J = Jz(z)ˆz, this can be achieved using piecewise
linear elements. In 3D domains, with 2D boundaries, divergence-conforming
elements can be constructed as the cross product of the edge elements on a
surface and the surface normal ˆn:
sRWG(r) = ˆn × N(r).
(7.45)
These are called Rao–Wilton–Glisson (RWG) elements after their inven-
tors [55]. In polar coordinates with respect to the corner opposing the edge
with which each basis function is associated, sRWG(r) ∝rˆr. A complete basis
function extending over two triangles is shown in Figure 7.10.
Fig. 7.10. Rao–Wilton–Glisson basis function extending over two triangular ele-
ments.
7 The Method of Moments
Integration
To carry out the integration in (7.44) we must decide how to deal with the sin-
gularity of the integrand. The most successful approach [29] exploits the fact
that the 3D singularity 1/R can be integrated exactly on triangles. Therefore,
this piece can be pulled out and done exactly, while the remaining, bounded
terms can be integrated by standard numerical integration schemes. We will
use these considerations to derive and solve a 1D problem for a thin conduct-
ing wire in Section 7.4.
7.3.4 The Magnetic Field Integral Equation
The technical details of the derivation of the MFIE are somewhat subtle and
lengthy as compared to the EFIE. For a complete derivation of the MFIE,
the reader is referred to the literature [53, 82]. Here, we settle for stating the
result for smooth PEC scatterers (that do not have sharp corners or edges)
tan = 1
2 ˆn × Js(r) + 1
4π −
exp(−jkR)
× Js(r ′)dS ′

. (7.46)
Here, the integral (with the bar) is evaluated in the principal-value sense [53],
and it is interpreted in the following way. The domain of integration excludes
an inﬁnitesimal area around the observation point, and the contribution from
the excluded area is accounted for by the term 1
2 ˆn × Js(r). As previously
mentioned, the MFIE also allows cavity eigenmodes that are internal to a
conducting body. However, the MFIE has diﬀerent internal resonances than
the EFIE. It should be noted that the MFIE is valid only for closed surfaces,
while the EFIE can be applied to both closed and open surfaces.
FEM Solution, Choice of Elements, and Integration
A FEM solution that parallels the one for the EFIE would use triangular
elements. It is then useful to consider the current that ﬂows on a single ﬂat
triangle K. We note that for the case when both the observation point r
and the source point r′ are located on K, both the gradient of the Green’s
function and the surface current density are in the plane of K, and therefore,
their cross product is perpendicular to K. Since only the tangential component
is included in the MFIE, the contribution from element K to the integral in
(7.46) is zero when the observation point r is located on K. This is the case
when the MFIE is tested, and therefore, the singularity of the integrand in
the MFIE does not feature in the same way as for the EFIE. In fact, it has
already been integrated analytically during the derivation of the MFIE, and
it is included in the term 1
2 ˆn × Js(r).
To solve the MFIE for a 3D problem using ﬁnite elements and Galerkin’s
method, we use the same basis for the current as we employed for the EFIE;
7.3 Electromagnetic Scattering
i.e., the current is expanded in the RWG basis functions as shown in (7.42),
and we test with ˆn × si. This gives the system of linear equations
(ˆn × si) · Hi
tandS =
Bijaj,
(7.47)
where the matrix elements are given by
Bij = 1
(ˆn × si) · (ˆn × sj)dS
(ˆn × si) · −
exp(−jkR)
× sj dS ′dS. (7.48)
7.3.5 The Combined Field Integral Equation
With a suitable linear combination of (7.43) and (7.47), often referred to as the
combined ﬁeld integral equation (CFIE), the problems associated with internal
resonances can be avoided [51]. This gives the system of linear equations
si · Ei
tandS + (1 −α)Z0
(ˆn × si) · Hi
tandS =
Cijaj, (7.49)
where the matrix elements are given by Cij = αAij −(1 −α)Z0Bij, and
0 < α < 1 is a weighting parameter.
Review Questions
7.3-1 What boundary conditions are used in the derivation of the EFIE?
7.3-2 What relation between the scalar and vector potential is used to deﬁne
the Lorentz gauge? What are the consequences of this particular gauge?
7.3-3 Derive the Green’s function for the scalar and vector potential for the
3D free-space case combined with the Lorentz gauge.
7.3-4 List some diﬃculties and useful techniques concerning the evaluation of
the integrals that occur in the EFIE.
7.3-5 Describe, in words, the problems with internal resonance and mention
a remedy.
7.3-6 Use the FEM to write down a system of linear equations that correspond
to the EFIE. List the steps of the assembling procedure needed for this
problem.
7.3-7 What basis function should be used for a PEC body treated with the
EFIE and why? How does this relate to the MFIE and the CFIE?
7.3-8 What boundary conditions are satisﬁed by (7.36) and (7.38)?
7.3-9 Show that the matrix associated with the EFIE derived by FEM tech-
niques and Galerkin’s method is symmetric.
7.3-10 Relate the divergence-conforming and curl-conforming basis functions
on triangles.
7.3-11 Why is the CFIE useful?
7 The Method of Moments
7.4 Scattering on Thin Wires
Here we consider scattering of electromagnetic waves by thin conducting wires.
The analysis can be extended to study dipole antennas of ﬁnite length and
thickness. We consider a plane wave incident on a wire of length L and radius
a, aligned with the z-axis; see Figure 7.11.
Fig. 7.11. Electromagnetic wave incident on thin wire.
For simplicity we assume normal incidence
z = E0 exp(−jkx),
k = ω/c.
If the wire is very thin compared with a wavelength, ka ≪1, the incident wave
is nearly constant, Ei
z ≈E0, on the surface of the wire, and the surface current
must be approximately Js ≈Jz(z)ˆz. Then, (7.41) gives for the z-component
of the scattered ﬁeld
E0 = −Es
z = jωµ0
 L/2
−L/2
 2π
exp(−jkR)
Jz(z′) a dθ′dz′
+jωµ0
4πk2
 L/2
−L/2
 2π
exp(−jkR)
∂Jz(z′)
a dθ′dz′. (7.50)
In the integration over the wire surface, Jz is independent of θ′, so the only
θ′-dependence comes from R. According to the cosine theorem, the distance
between two points on the wire surface satisﬁes
7.4 Scattering on Thin Wires
R2 = (z −z′)2 + a2 + a2 −2a2 cos(θ −θ′) = (z −z′)2 + 4a2 sin2 θ −θ′
Carrying out the θ′-integration in (7.50), we obtain, for |z| ≤L/2,
4πE0
jωµ0
 L/2
−L/2
G(z −z′)I(z′)dz′ + 1
 L/2
−L/2
G(z −z′) dI
dz′ (z′)dz′. (7.51)
Here I = 2πaJz is the total current on the surface of the wire, and the kernel
of the resulting 1D integral equation is
G(z −z′) = 1
 2π
exp(−jkR)
dθ′.
(7.52)
7.4.1 Hall´en’s Equation
The 1D version of the EFIE in (7.51) can be simpliﬁed by means of a refor-
mulation found by Hall´en. Integrating the second term in (7.51) by parts and
using I(±L/2) = 0 and (d/dz′)G(z −z′) = −(d/dz)G(z −z′), the equation
can be written as
4πE0
jωµ0
1 + 1
(7.53)
H(z) =
 L/2
−L/2
G(z −z′)I(z′)dz′.
(7.54)
Equation (7.53) can be regarded as a diﬀerential equation for H, and this equa-
tion is easy to solve. Its general solution is an arbitrary homogeneous solution,
for instance 4πE0/jωµ0, added to the general solution of the homogeneous
equation C cos kz + D sin kz. When the incident wave has no z-dependence,
the solution must be symmetric with respect to the midpoint of the wire.
Therefore, D = 0, and the solution is
H(z) + C cos kz = 4πE0
jωµ0
|z| ≤L/2.
Combining this with (7.54), we obtain
 L/2
−L/2
G(z −z′)I(z′)dz′ + C cos kz = 4πE0
jωµ0
(7.55)
which is known as Hall´en’s equation. The diﬀerential order of the integral
equation (7.51) has been reduced at the expense of introducing an extra con-
stant of integration.
7 The Method of Moments
7.4.2 Valid Approximation for the 1D Kernel
As mentioned earlier, it is important to evaluate the 1/R singularity of the
EFIE correctly, and this should be respected when we seek an expression for
the 1D Green’s function G. We isolate the singularity by writing
exp(−jkR)
R + exp(−jkR) −1
where only the ﬁrst part is singular. This gives
G = G0 + G1,
G0 = 1
 2π
G1 = 1
 2π
exp(−jkR) −1
dθ′.
(7.56)
The advantage of the splitting is that the singular part G0 can be evaluated
exactly:
G0(ζ) =
ζ2 + 4a2 K
ζ2 + 4a2
ζ = z −z′,
where
K(m) =
 π/2
1 −m sin2 φ
is the complete elliptic integral of the ﬁrst kind. The function G0(ζ), which
contains the singular part of the 3D Green’s function, is logarithmically sin-
gular when ζ →0.
For the nonsingular part G1, we can use less accurate approximations suit-
able for thin wires, such as replacing the current on the wire surface with the
total current placed at the center of the wire. This means that we approximate
(z −z′)2 + a2 in G1, which is then straightforward to calculate. Thus,
the total kernel is approximated as
G(ζ) ≈
ζ2 + 4a2 K
ζ2 + 4a2
+ exp(−jk
ζ2 + a2) −1
ζ2 + a2
ζ = z −z′.
(7.57)
Nonsingular Kernel Gives Spurious Solutions
If we used the approximation R ≈
(z −z′)2 + a2 also in G0 (that is, ap-
proximate the current on the wire surface by the same total current on its
axis), the 1D kernel would lose its singularity. It can be shown that Hall´en’s
equation (7.55) with such a smoothed kernel does not have regular solutions.
If one tries to solve Hall´en’s equation with a nonsingular approximation for
G(z), the solution does not converge, but instead develops more and more
short-wavelength oscillations when the resolution is increased. The reason for
this is that a smooth Green’s function G(z) underestimates the ﬁelds created
7.4 Scattering on Thin Wires
by short-wavelength currents. To create the short-wavelength components of
the electric ﬁeld that occur near the endpoints of the wire (for |z| > L/2), the
smooth approximation of G requires too strong short-wavelength components
in the current. As a consequence, the current density does not converge as the
resolution increases.
Nevertheless, such approximations of the Green’s function have been used
in the past, for instance, in old versions of the NEC code, which is popular for
work on thin wires. It produces acceptable results as long as the resolution
in the z-direction is coarse compared to the radius of the wire, ∆z ≫a.
However, when the resolution is increased so that ∆z < a, the current develops
oscillations and the computation diverges rather than converge as the mesh
is reﬁned. This is yet another example of spurious solutions.
7.4.3 Numerical Solution
To evaluate the integrals in (7.54), we can either do numerical integration
adapted to a logarithmic singularity, as discussed in Section 7.2.5, or attempt
a more rigorous treatment, where the logarithmic singularity is separated out
and integrated exactly. To avoid excessive work on a problem that is already
an approximation, we settle for numerical integration. The elliptic integral
can be accurately evaluated by using a series expansion such as given by
Abramowitz and Stegun [2].
We divide the wire into elements, and expand the current in piecewise
linear functions and use point matching. For piecewise linear current, the
point matching of Ez should be made at the nodes, since this is where the
piecewise linear basis function has its main inﬂuence. The boundary condition
I(±L/2) = 0 eliminates the unknowns for I on the endpoints. To determine
the constant C in (7.55) we use the condition that the equation is satisﬁed
also at the endpoint z = L/2. This gives us as many conditions as we have
unknowns.
7.4.4 MATLAB: Hall´en’s Equation
In the following routine, we use the techniques described above to solve
Hall´en’s equation. Each current-carrying element is speciﬁed by the arrays
zs for the starting coordinates, ze for the endpoints, and E0 for the electric
ﬁeld.
% --------------------------------------------------------------
% Compute current distribution for Hallen’s equation by MoM
% --------------------------------------------------------------
function [Iz, C, Imi] = EFIE(zs, ze, E0, a, k0)
% Arguments:
= z-coordinate for starting points
= z-coordinate for ending points
7 The Method of Moments
= the incoming Ez and Iz the total current on
each element
= the radius of the wire
= the wavenumber
% Returns:
= the current density along the wire
= the constant for the homogeneous solution ’cos(k0*z)’
= the current density on the midpoint of the wire
= 0.5 - sqrt(0.25-exp(-2)); % an integration parameter
= length(zs) - 1;
% number of unknowns equals
% the number of interior nodes
zobs = ze;
= zs + xi*(ze-zs);
% Integration points
= ze + xi*(zs-ze);
% Integration points
= (zs-ze)/2;
= 4*aˆ2;
% Precomputation of constant
= zeros(n+1);
% System matrix
% Loop over elements
for idx = 1:n+1
= zobs - z1(idx);
= z.ˆ2;
= sqrt(zsq+aˆ2);
= eval_EIK(as4./(as4 + zsq));
temp1 = 2*EIK./(pi*sqrt(as4 + zsq)) + (exp(j*k0*za)-1)./za;
= zobs - z2(idx);
= z.ˆ2;
= sqrt(zsq+aˆ2);
= eval_EIK(as4./(as4 + zsq));
temp2 = 2*EIK./(pi*sqrt(as4 + zsq)) + (exp(j*k0*za)-1)./za;
if (idx > 1)
A(:,idx-1) = A(:,idx-1) ...
+ hh(idx)*((1-xi)*temp1(:) + xi*temp2(:));
if (idx < n+1)
A(:,idx)
= A(:,idx)
+ hh(idx)*(xi*temp1(:) + (1-xi)*temp2(:));
lastrow = A(n+1,1:n);
7.4 Scattering on Thin Wires
for i = 1:n
A(n+1,i) = 0.5*(lastrow(i)+lastrow(n+1-i));
A(n+1,n+1) = cos(k0*zs(1));
for i = 1:n
A(i,n+1) = cos(k0*ze(i));
= (A\E0’)’;
= I(1:n);
Imi = I(round((n+1)/2));
= I(n+1);
% --------------------------------------------------------------
% Evaluate the complete elliptic integral of the first kind
% by means of a polynomial approximation [M Abramowitz and
% I A Stegun, Handbook of Mathematical Functions, National
% Bureau of Standards, 1965]
% --------------------------------------------------------------
function EIK = eval_EIK(x)
% Arguments:
= argument for K(x) in the interval 0 <= x < 1
% Returns:
= the value of the complete elliptic integral of
the first kind (with an error less than 2e-8)
= [0.01451196212; 0.03742563713; 0.03590092383; ...
0.09666344259; 1.38629436112];
= [0.00441787012; 0.03328355346; 0.06880248576; ...
0.12498593597; 0.50000000000];
= 1 - x;
EIK = polyval(a,m1) - polyval(b,m1).*log(m1);
The routine computes the current distribution I(z) and the constant C in
Hall´en’s equation (7.55). Next, we present some numerical results, where, for
example, Figure 7.12 can be generated by the following script.
= 200;
% Number of cells
= 1;
% Wavenumber
= 0.02; % Radius
= 3.0;
% Length
= L/n;
% Cell size
7 The Method of Moments
% Z-coordinate for starting and ending points of the segments
= zeros(1,n);
= zeros(1,n);
zs(1:n) = linspace(-L/2, L/2-h, n);
= zs + h;
= ones(1,n);
% Solve Hallen’s equation
[Iz, C, Imi] = EFIE(zs, ze, E0, a, k0);
% Plot the results
figure(1), clf
plot([zs(1) zs(1:end-1)+h/2 ze(end)], ...
[0 real(Iz) 0], ’k-’), hold on
plot([zs(1) zs(1:end-1)+h/2 ze(end)], ...
[0 imag(Iz) 0], ’k--’)
xlabel(’z [m]’), ylabel(’I [A]’)
7.4.5 Numerical Results
Figure 7.12 shows the current distribution on a dipole with kL = 3 and
ka = 0.02 when the dipole is resonantly excited. The calculation used the
approximation (7.57) for G, which has the correct singularity. The current
has steep gradients near the endpoints of the dipole, and here the charge
density ∝dI/dz is singular. This is similar to the singular charge distribution
we found for electrostatics near the edge of the parallel plate capacitor.
Figure 7.13 shows the induced current at the midpoint of the wire as a
function of L for k = 1 and a = 0.02. Note the resonances around kL = nπ,
where n is an odd integer.
One may wonder why there are no resonances when kL/π is an even inte-
ger. Figure 7.14 shows the current distribution on a dipole with kL = 5.9 and
ka = 0.02 when the dipole is not strongly excited. Nevertheless, the dipole
has a natural oscillation mode near this frequency. However, this mode has a
full wavelength oscillation over the wire and is odd around the center point.
Therefore, it does not get excited by the incident plane wave. The current
induced on the wire for kL = 5.9 is even around the midpoint of the wire, and
this is not a resonant mode of the wire at this frequency.
Figure 7.15 shows the current distribution on a dipole with kL = 9.2 and
ka = 0.02 when the dipole is resonant. The natural oscillation mode of the
dipole at this frequency has a 1.5 wavelength, and this mode has a net coupling
to the incident plane wave.
7.4 Scattering on Thin Wires
−1.5
−0.5
−0.8
−0.7
−0.6
−0.5
−0.4
−0.3
−0.2
−0.1
z [m]
I [A]
Fig. 7.12. Induced current on a wire with kL = 3, ka = 0.02: solid curve - real part
and dashed curve - imaginary part.
−0.8
−0.6
−0.4
−0.2
L [m]
Imid [A]
Fig. 7.13. Induced current at the midpoint of a wire as a function of L for k = 1,
and a = 0.02: solid curve - real part and dashed curve - imaginary part.
7 The Method of Moments
−0.25
−0.2
−0.15
−0.1
−0.05
z [m]
I [A]
Fig. 7.14. Induced current on a wire with kL = 5.9, ka = 0.02: solid curve - real
part and dashed curve - imaginary part.
−0.8
−0.6
−0.4
−0.2
z [m]
I [A]
Fig. 7.15. Induced current on a wire with kL = 9.2, ka = 0.02: solid curve - real
part and dashed curve - imaginary part.
7.4 Scattering on Thin Wires
Review Questions
7.4-1 Derive (7.50) from (7.41). What assumptions did you use?
7.4-2 Perform the derivations required to arrive at Hall´en’s equation.
7.4-3 Write the Green’s function for 3D free space as a sum of a singular part
and a regular part. Show that the regular part is bounded as R →0.
7.4-4 Describe the steps and assumptions required to arrive at (7.57).
7.4-5 What can happen if the Green’s function is too smooth; i.e., its singu-
larity is neglected?
7.4-6 Give an example of weighting and basis functions that can be used for
Hall´en’s equation. Write down the corresponding system of linear equa-
tions.
7.4-7 Why does Figure 7.13 show resonances at kL = nπ only for odd integers
n and not even integers?
Summary
Consider a problem modeled by the diﬀerential equation Df = s, where D
is a diﬀerential operator, f is a ﬁeld and s is the source. The Green’s func-
tion G(r, r ′) satisﬁes DrG(r, r ′) = δ(r −r ′), where Dr takes derivatives
with respect to the unprimed coordinates. Given the Green’s function, the
diﬀerential equation can be written as an integral equation
f(r) =
G(r, r ′)s(r ′)dV ′.
For Poisson’s equation −ϵ0∇2φ = ρ, we have
the 3D Green’s function G(r, r ′) = |r −r ′|/(4πϵ0) and
the 2D Green’s function G(r, r ′) = −1/(2πϵ0) ln |r −r ′|.
The method of moments (MoM) solves an integral equation by a ﬁnite
element expansion; i.e., the sources s(r) ≈
k αksk(r) are expanded in
terms of basis functions sk(r). Choose as many weighting functions wk(r)
as there are basis functions. Determine the coeﬃcients αk by multiplying
the Green’s function expression for f −fprescribed and integrating in space.
Two usual choices for the weighting functions are
collocation with wk(r) = δ3(r −rk), which evaluates the ﬁeld at the
point r = rk, and
Galerkin’s method wk(r) = sk(r).
The integrand of the integrals in a MoM formulation are often decomposed
into a singular part and a regular part. Preferably, the singular part is
treated analytically and the nonsingular part by numerical integration.
Scattering from conducting bodies is often treated by MoM. In the Lorentz
gauge, the scattered electric ﬁeld can be expressed as
Es =
jωϵ0µ0
[∇(∇· A) + k2A],
7 The Method of Moments
where A is expressed in the induced surface current as
A = µ0
 e−jkR
Js(r ′)dS′,
where R = |r −r ′|. Equivalently, Es = −jωA −∇φ with A as above and
4πϵ0
 e−jkR
ρs(r ′)dS′,
where jωρs + ∇· Js = 0. The equation ˆn × (Es + Einc) = 0 is solved by
the MoM on the surfaces of the conductors. The current Js should be ex-
panded in Rao–Wilton–Glisson basis functions, since they have continuous
normal components at cell edges.
The EFIE suﬀers from “internal resonances”. At these resonance frequen-
cies, the solution is wrong and the system matrix may become singular.
The MFIE has diﬀerent internal resonances than the EFIE, and with a
suitable linear combination of the two integral equations, the internal res-
onances (and the problems associated with them) can be avoided. The
summed equation is called the CFIE.
Scattering from thin wires is often treated by the MoM combined with
certain approximations. If the surface current is replaced by a line current
I(z) on axis, the MoM does not converge as the resolution is increased,
but increasing wiggles appear. Short-wavelength oscillations are screened
by the distance from the center to the surface of the wire. Convergence
is achieved by using a more accurate Green’s function that keeps the cor-
rect singularity at r = r ′. Then, the electric ﬁeld produced by ﬁne-scale
variations in the current is better represented.
Problems
P.7-1 Green’s functions are normally constructed so that the boundary con-
ditions are accounted for. Given the free-space Green’s function in (7.10),
derive the corresponding Green’s function that can be used for a problem
with a PEC ground plane at z = 0. Such a Green’s function allows for an
algorithm that avoids an explicit discretization of the ground plane.
P.7-2 Show that the MoM matrix in (7.20) is symmetric and positive deﬁnite
if Galerkin’s method is used. How does this relate to the corresponding
matrices derived by the FEM?
P.7-3 In Section 7.2, compare the capacitor problem with and without the
exploitation of symmetries. How much computational resources, in terms
of memory requirements and ﬂoating point operations, can be saved by
the use of symmetry?
P.7-4 Can the algorithm in Section 7.2 be generalized to also include dielectric
materials? Discuss how the formulation would change.
7.4 Scattering on Thin Wires
P.7-5 Apart from sharp metal corners, are there other situations in which a
reduced order of convergence can be expected?
P.7-6 Does the distance between two similar sharp metal corners inﬂuence
the order of convergence? What order of convergence do you expect from
a problem with two diﬀerent sharp metal corners?
P.7-7 Use (7.36) to derive a Green’s function for the vector potential that
includes a PEC ground plane at z = 0. Perform the same derivation for
the scalar potential in (7.38). Given the ﬁelds
E = −∇φ −jωA,
B = ∇× A,
verify that the boundary conditions are satisﬁed at the ground plane.
P.7-8 Derive the EFIE directly from Maxwell’s equations.
P.7-9 For a 2D problem where a PEC cylinder is aligned with the z-axis,
choose basis functions for the current Js(x, y), and charge distributions
ρs(x, y). Does the choice depend on whether the TE or TM case is con-
sidered?
P.7-10 Show that (7.39) can also be written as Es = c2(∇∇· A + k2A)/jω
with A given by (7.36).
P.7-11 Is the matrix (7.48) associated with the MFIE symmetric?
P.7-12 Write down the RWG basis functions for a rectangle.
P.7-13 Try to solve (7.55) with only one basis function. What type of basis
function do you choose?
Computer Projects
C.7-1 Use the algorithm in Section 7.2 to compute the capacitance for two
parallel circular cylinders of radius a and a separation distance d, which
also can be solved for analytically. What order of convergence do you
expect, and do your expectations agree with the numerical experiment?
C.7-2 Evaluate (7.56) by brute force and compare the result to the approxi-
mation in (7.57). Conclusions?
C.7-3 Use the approach described in Section 7.4 to implement the MoM for
scattering from thin wires. Reproduce some of the results presented in Sec-
tion 7.4 for validation. Can you generalize your formulation and program
so that you can solve problems where three wires or more are connected
at the same point? What type of basis function do you need at such a
junction and how do you test the integral equation?
C.7-4 Use the approach described in Section 7.3 to implement the MoM for
scattering from metal surfaces. Discretize a PEC sphere by triangles and
solve the scattering problem. How does the solution compare with analyt-
ical results [4]? Try to reproduce the problem with internal resonances.
Summary and Overview
The goal of any analysis or optimization is to achieve suﬃcient accuracy with
minimum eﬀort, where eﬀort usually is interpreted as computational cost in
terms of computational time and memory requirements. However, there may
also be a considerable eﬀort associated with other issues such as the program-
ming of the numerical algorithm or the construction of geometrical descrip-
tions suitable for the the computations at hand.
Faced with an electromagnetic problem, say an antenna in the vicinity
of a human body, we need to ﬁnd a numerical algorithm that can yield suf-
ﬁciently accurate results without an excessive eﬀort. Naturally, there are a
number of aspects that will guide the choice of computational method. For
example, the electromagnetic problem at hand may involve boundary condi-
tions that are necessary for a realistic model but diﬃcult to treat for some
computational methods. Complex materials with nonlinearities, anisotropies,
or dispersive characteristics can also eliminate some numerical algorithms.
The typical length scales of the problem is another important aspect that
should be considered. In linear problems, the wavelengths present are deter-
mined by the frequency contents of the excitation and the materials. Other
length scales that should be considered are the skin-depth and the size of
the geometrical features present. Each of these length scales typically covers
a certain range, and the combination of them can yield a signiﬁcant interval
(which can require certain approximations if a direct analysis is not feasible).
In a typical low-frequency application, for example, the wavelength is on the
order of thousands of kilometers, and the geometrical size on the order of me-
ters (possibly down to millimeters for laminations and thin wires) while the
skin-depth is typically in the range from millimeters to centimeters.
In some situations, one method is competitive for a part of the prob-
lem while another algorithm is better suited for the remaining parts. It is
then attractive to combine the diﬀerent algorithms to form a so-called hybrid
method. Such methods can be challenging to construct, and many attempts
have failed to preserve important properties of Maxwell’s equations. However,

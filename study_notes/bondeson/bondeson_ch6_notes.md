# Bondeson《Computational Electromagnetics》第6章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 102-166 of 231 (231 total)

---

## The Finite Element Method

6 The Finite Element Method
Line
Triangle
Square
Tetrahedron
Pyramid
Prism
Cube
Fig. 6.1. Diﬀerent element shapes: a line in one dimension, a triangle and square in
two dimensions, and a tetrahedron, prism, pyramid, and cube in three dimensions.
6.1 General Recipe
We start by giving the general recipe for how to solve a diﬀerential equation
by the FEM. The equation is written as L[f] = s, where L is an operator, s
the source, and f the unknown function to be computed in the region Ω.
Subdivide the solution domain Ωinto cells, or elements. For example, a
2D domain can be subdivided into triangles or quadrilaterals.
Approximate the solution by an expansion in a ﬁnite number of basis
functions, i.e., f(r ) ≈n
i=1 fiϕi(r ), where fi are (unknown) coeﬃcients
multiplying the basis functions ϕi(r ). The basis functions are generally
low-order polynomials that are nonzero only in a few adjacent elements.
Form the residual r = L[f]−s, which we want to make as small as possible.
In general, it will not be zero pointwise, but we require it to be zero in the
so-called weak sense by setting a weighted average of it to zero.
Choose test, or weighting, functions wi, i = 1, 2, . . . , n (as many as there
are unknown coeﬃcients) for weighting the residual r. Often, the weighting
functions are the same as the basis functions, wi = ϕi, and this method is
then called Galerkin’s method.
Set the weighted residuals to zero and solve for the unknowns fi; i.e., solve
the set of equations ⟨wi, r⟩=
Ωwi r dΩ= 0, i = 1, 2, . . . , n.
In mathematical deﬁnitions, the term ﬁnite element usually refers to an
element (e.g., a triangle) together with a polynomial space deﬁned in this
element (e.g., the space of linear functions) and a set of degrees of freedom
deﬁned on this space (e.g., the values of the linear functions in the corners
(nodes) of the triangle). This deﬁnition is seldom used in electrical engineering,
6.2 1D Finite Element Analysis
where one tends to focus on the basis functions used to expand the solution
instead.
Review Questions
6.1-1 List some pros and cons of the ﬁnite element method.
6.1-2 Compare the steps of the general recipe for the FEM to the typical
discretization procedure employed for ﬁnite diﬀerence methods. Identify
similarities and diﬀerences.
6.1-3 What is a ﬁnite element?
6.2 1D Finite Element Analysis
As the ﬁrst model problem we choose a second-order ordinary diﬀerential
equation, namely the 1D Helmholtz equation:
α df
+ βf = s,
a < x < b,
(6.1)
f(a) = fa,
(6.2)
f(b) = fb.
(6.3)
Here f = f(x) is the sought solution, and the material properties α = α(x)
and β = β(x) and the source s = s(x) are prescribed functions of x.
There are many physical systems that are modeled by (6.1), for example,
a transversal wave in a 1D medium, such as a light wave propagating and
being reﬂected in dielectric layers. In this case we have f(x) = Ez(x), and
the coeﬃcients are α(x) = 1/µ(x), β(x) = jωσ(x) −ω2ϵ(x), where ω is the
angular frequency, and s(x) = −jωJz(x) (which vanishes, unless there are
current-carrying conductors).
We seek the function f(x) on the interval a < x < b. According to the
general recipe for the FEM, we ﬁrst divide this interval into subintervals
(elements). Let us assume, for example, a = −2 and b = 5 and divide the
x-axis into 7 equally large elements. We call the endpoints of each element
nodes, and they have the coordinates xi = i −3 where i = 1, 2, . . . , 8. We
introduce the nodal basis functions ϕi(x), which are linear on each interval,
one at node i and zero at all other nodes, as shown in Figure 6.2. These basis
functions are often called “tent functions.”
We seek approximate solutions that are expanded in the basis functions
(in the following, f will denote this approximate solution):
f(x) =
fjϕj(x).
(6.4)
6 The Finite Element Method
x [m]
Basis functions [−]
Fig. 6.2. 1D linear elements. In particular, the basis function ϕ4(x) is emphasized
by a thick line.
Note that f(xi) = fi, so that the expansion coeﬃcients are the values of f
at the nodes. Since f(a) = fa and f(b) = fb are known, we set f1 = fa and
f8 = fb.
In the next step, we follow Galerkin’s method and choose the test functions
wi(x) = ϕi(x), where i = 2, 3, . . . , 7 (the endpoints are excluded because the
corresponding function values are known). We multiply the residual of (6.1) by
the test function wi(x) and integrate from x = a to x = b. To move one of the
derivatives from f to the test function wi, we use integration by parts. This
gives the weak form of the original problem, which is the weighted average of
the residual:
(αw′
if ′ + βwif −wis) dx = 0.
(6.5)
In this case, the boundary term [wiαf ′]b
a vanishes, since wi(a) = wi(b) = 0.
By substituting (6.4) into the weak form (6.5) and choosing w2(x) = ϕ2(x),
we generate an equation involving six unknowns: the coeﬃcients fj for the
interior nodes xj, where j = 2, 3, . . . , 7. Next, we pick w3(x) = ϕ3(x) to
generate a second equation, and so on. In the end, we have six equations and
six unknowns, and this is formulated as a system of linear equations Az = b
with
Aij =
j + βϕiϕj
(6.6)
zj = fj,
(6.7)
bi =
ϕis dx.
(6.8)
6.2 1D Finite Element Analysis
Here, i = 2, 3, . . . , 7 (for the equations) and j = 1, 2, . . . , 8 (for the coeﬃ-
cients), so A has 8 columns and 6 rows, z has 8 rows, and b has 6 rows. The
coeﬃcients f1 and f8 are known from the boundary conditions and can be
moved to the right-hand side:
A22 A23 . . . A27
A32 A33 . . . A37
A72 A73 . . . A77
⎢⎢⎢⎣
⎥⎥⎥⎦=
⎢⎢⎢⎣
⎥⎥⎥⎦−
⎢⎢⎢⎣
A21f1 + A28f8
A31f1 + A38f8
A71f1 + A78f8
⎥⎥⎥⎦.
The part of the system matrix A that remains on the left-hand side is square;
that is, we have as many unknowns as equations. In the present case, the func-
tion values at the endpoints are known, and we do not use the corresponding
weighting functions. The matrix A is sparse because the basis functions give
only nearest-neighbor coupling of the unknowns. Also note that A is sym-
metric, Aij = Aji. This is related to the fact that the Helmholtz operator is
self-adjoint and we used Galerkin’s method.
The boundary conditions (6.2) and (6.3) specify the value of the function
f(x) at the boundary. Other types of boundary conditions can specify the
derivative of f(x) or a linear combination of f(x) and its derivative. At either
boundary, for instance the left one x = a, we can apply conditions of the
following standard types:
f(a) = p
(6.9)
f ′(a) + γf(a) = q.
(6.10)
Equation (6.9) is called a Dirichlet boundary condition, and it eliminates
an unknown. Equation (6.10) is called a Neumann boundary condition when
γ = 0 and a Robin boundary condition when γ ̸= 0. For the Neumann and
Robin boundary conditions, f(a) must be introduced as an extra unknown.
We generate the extra equation by testing with w1(x) = ϕ1(x). Dirichlet
boundary conditions are referred to as essential, whereas Neumann and Robin
boundary conditions are called natural. Further, if q or p is zero, the boundary
conditions are called homogeneous.
Review Questions
6.2-1 Write down an explicit expression for the nodal basis function ϕi(x) and
its derivative for a nonuniform discretization in one space dimension.
6.2-2 Explain the terms Galerkin’s method and weak form.
6.2-3 How many test functions are needed for a 1D ﬁnite element problem?
6.2-4 Explain the diﬀerence between Dirichlet, Neumann, and Robin bound-
ary conditions.
6.2-5 Are the numbers of basis functions and test functions always the same?
6 The Finite Element Method
6.3 2D Finite Element Analysis
We extend the model problem (6.1) to two dimensions, but still f is a scalar-
valued function:
−∇· (α∇f) + βf = s in S,
(6.11)
f = p on L1,
(6.12)
ˆn · (α∇f) + γf = q on L2.
(6.13)
The boundary of the solution domain S has two parts, L1 and L2, with dif-
ferent types of boundary conditions.
Analogously to the 1D model problem, there are many physical situations
that can be modeled by (6.11). Let us consider a speciﬁc example where
we wish to compute the resistance between the left and bottom edges of
the conducting plate shown in Figure 6.3. In this case, f is the electrostatic
potential, α the conductivity, β = 0, and s = 0. The electric potential along
the thick solid line on the boundary is set to 10 V, i.e., a Dirichlet boundary
condition f = 10. Along the thick dashed line the potential is set to 0 V. The
remaining part of the boundary is an insulating material. On this part of the
boundary, we use a Neumann boundary condition, ˆn·∇f = 0, which means no
ﬂux of charge across the boundary. We now continue with the derivation based
on the general model problem, and at the end of this section, we will show
the solution for the speciﬁc example concerning the resistance computation.
−0.5
−0.6
−0.4
−0.2
x [m]
y [m]
Fig. 6.3. A 2D conducting plate. The computational domain S, i.e., the plate, is
divided into triangular elements. Automatically, the boundary of S is discretized
into line segments. This boundary divides into the two parts, denoted by L1 and
L2, with diﬀerent types of boundary condition according to (6.12) and (6.13).
We multiply (6.11) by a test function wi and integrate over S:
6.3 2D Finite Element Analysis
wi [−∇· (α∇f) + βf] dS =
wis dS.
Next, integrate by parts using the identity
∇· [wi(α∇f)] = α∇wi · ∇f + wi∇· (α∇f)
(6.14)
and Gauss’s theorem in 2D:
∇· F dS =
L1+L2
ˆn · F dl,
with F = wiα∇f. This gives the weak form of (6.11)–(6.13):
(α∇wi · ∇f + βwif) dS −
wi(q −γf) dl =
wis dS,
(6.15)
where we have used the boundary condition (6.13). The boundary integral
over the part of the boundary where the solution is known (L1) vanishes
because the test functions vanish there. It should be noted that in addition to
the diﬀerential equation with the sources, the weak form (6.15) also contains
the boundary conditions.
The nodes are labeled by the integers i and they are located at ri, where
i = 1, 2, . . . , Nn. The elements are triangles, and again, we choose piecewise
linear, or nodal, basis functions ϕi(r ) where the subindex i refers to the node
associated with the basis function. The nodal basis functions are linear inside
each triangle, with ϕi(ri) = 1 and ϕi(rj) = 0 when i ̸= j. There is one
such basis function associated with each node, and two of them are shown in
Figure 6.4. The ﬁnite elements associated with the nodal basis functions are
called nodal elements.
Fig. 6.4. Illustration of two nodal basis functions, one on the boundary and one in
the interior of the solution domain.
We expand the, again approximate, solution f(r ) in terms of the basis
functions:
f(r ) =
fjϕj(r ).
(6.16)
6 The Finite Element Method
Next, we substitute (6.16) into the weak form (6.15) and use Galerkin’s
method, i.e., choose wi(r ) = ϕi(r ) for all nodes where f is unknown. This
gives a linear system of equations Az = b, where the elements are given by
Aij =
(α∇ϕi · ∇ϕj + βϕiϕj) dS +
γϕiϕj dl,
(6.17)
zj = fj,
(6.18)
bi =
ϕis dS +
ϕiq dl.
(6.19)
Here, the index j runs over all nodes, and i only over those nodes where f is
unknown (not those on the boundary L1 with the Dirichlet condition). The
variables are reordered to collect those where f is known in the vector ze,
while zn denotes the remaining unknowns,

= Aeze + Anzn = b.
The matrix A is partitioned in the same way. This results in a square matrix
An and a rectangular part Ae accounting for the Dirichlet boundary condi-
tion. The ﬁnal system of equations to be solved for zn is Anzn = b −Aeze,
where An and b −Aeze contain only known numbers. In Section 6.2, this
procedure is shown at a very detailed level. Here, it is expressed in terms of
matrices and vectors, which is more convenient for 2D and 3D problems.
Finally, we return to the speciﬁc example in which we wanted to compute
the resistance of the metal plate, where the thickness of the plate is denoted
by h. The numerical solution, i.e., the approximate electrostatic potential, is
shown in Figure 6.5. Based on the potential, the resistance can be computed
in two ways:
Integrate the normal component of the current density J = −σ∇φ over
a cross-section of the plate to obtain the total current that ﬂows through
the plate. For example,
 0.5
σ ∂φ

y=−0.5
(6.20)
The resistance is then obtained from R = U/I, where U = ∆φ = 10 V.
Compute the total power dissipation in the plate (see Section 6.3.3 for a
similar approach used for a capacitance computation);
J · E dV =
σ|∇φ|2 dV = hzTAz = hzTb,
(6.21)
and then calculate the resistance from P = U 2/R, which gives R = U 2/P.
The latter approach is generally preferred, since it is trivial to compute and
often leads to better accuracy.
6.3 2D Finite Element Analysis
−0.5
−0.5
y [m]
x [m]
Fig. 6.5. The potential distribution in the conducting plate.
6.3.1 The Assembling Procedure
In practice, the matrix and vector components in (6.17)–(6.19) are computed
by assembling contributions from all elements. To illustrate the assembling
procedure, we consider the capacitance calculation in Section 3.1. The diﬀer-
ential equation is again ∇2φ = 0, and only the boundary conditions diﬀer
from the previous example.
The elements Aij of the system matrix are computed by evaluating the
integral
S ∇ϕi · ∇ϕj dS over the domain S between the inner and outer con-
ductors. In the assembling procedure, we break up this integral into integrals
over each element Se, and sum the contributions from all the elements, i.e.,
Aij =
∇ϕi · ∇ϕj dS =
Se ∇ϕi · ∇ϕj dS,
(6.22)
where Ne is the total number of elements.
Now we will concentrate on evaluating the integrals restricted to a single
element. We use a local numbering of the nodes for the element e, as shown
in Figure 6.6, and denote the coordinates of the nodes by r e
1 , r e
2 , and r e
respectively.
The Nodal Basis Functions
The local basis functions (i.e., the basis functions restricted to one element) are
denoted by ϕe
i(x, y), where the superindex labels the element (e = 1, . . . , Ne)
and the subindex the local node number (i = 1, 2, 3). There is one local basis
function associated with each node of the element, and these are shown in
Figure 6.7. The global basis function associated with node i is built up by the
6 The Finite Element Method
−0.8
−0.6
−0.4
−0.2
−0.2
x [m]
y [m]
Fig. 6.6. The numbering of local nodes for the element e.
local basis functions associated with that particular node in the surrounding
elements.
Fig. 6.7. The three basis functions for element e. The adjacent elements sharing an
edge with element e are also shown.
The basis functions have the following properties:
Inside each element, they are linear in x and y, i.e.,
i(x, y) = ae
i + be
ix + ce
(6.23)
They equal unity on one node and vanish on the others:
i(xe
i, ye
i ) = 1,
i(xe
j, ye
j) = 0, ∀i ̸= j.
(6.24)
We will now construct explicit expressions for ϕe
i(x, y) with these prop-
erties. To do this, we divide the element e into three triangles as shown in
Figure 6.8. Here, Ae
i is the area of subtriangle i, opposing vertex i of the
element, and Ae
tot = Ae
1 + Ae
2 + Ae
evaluate ϕe
i(x, y), has the position r = xˆx + yˆy.
6.3 2D Finite Element Analysis
−0.8
−0.6
−0.4
−0.2
−0.2
x [m]
y [m]
(x,y)
Fig. 6.8. Partition used to construct ϕe
i (x, y).
The basis functions ϕe
i(x, y) can be constructed by means of the area
coordinates Ae
i as
i(x, y) = Ae
(6.25)
[We note that the functions ϕe
i also are called simplex coordinates and
barycentric coordinates.] It is easy to verify that these elements satisfy the
requirements (6.23)–(6.24). Ae
i can be written as
1 = 1
2 ˆz · (r e
3 −r e
2 ) × (r −r e
2 ) ,
2 = 1
2 ˆz · (r e
1 −r e
3 ) × (r −r e
3 ) ,
3 = 1
2 ˆz · (r e
2 −r e
1 ) × (r −r e
1 ) ,
or more compactly
i = 1
2(r −r e
i+1) · ˆz × si,
(6.26)
where
si = r e
i−1 −r e
(6.27)
is the edge in the counterclockwise direction opposing node i. The total area
of the element is
tot = 1
2 ˆz · s2 × s3.
(6.28)
Now it is simple to ﬁnd the gradients of the local basis functions,
i = ˆz × si
(6.29)
and these are, of course, constant inside each element. Therefore, the integral
over one element e, contributing to the system matrix in (6.22), can be evalu-
ated by multiplying the scalar product of the local basis functions by the area
6 The Finite Element Method
of the element:
ij =
Se ∇ϕe
i · ∇ϕe
j dS = si · sj
(6.30)
Notice that we need to relate the three local node numbers of element e
to their corresponding global node numbers before we add the element con-
tributions Ae
ij to the global system matrix A.
The Element Matrix
Here we give a MATLAB function that computes all the contributions to A
from a single ﬁnite element described by its coordinates given in the argument
xy. Since there are three basis functions in each element, we can store all its
contributions in a 3 × 3 matrix, which we will refer to as the element matrix.
We name the MATLAB function CmpElMtx, and for the element shown in
Figure 6.6, this should be called with the argument xy = [-0.5 0.0 0.6;
0.5 -0.2 0.4].
% --------------------------------------------------------------
% Compute element matrix for a triangle and its node basis
% --------------------------------------------------------------
function Ae = CmpElMtx(xy)
% Arguments:
xy = the coordinates of the nodes of the triangle
% Returns:
Ae = element matrix corresponding to the Laplace operator
% Edges
s1 = xy(:,3)-xy(:,2);
s2 = xy(:,1)-xy(:,3);
s3 = xy(:,2)-xy(:,1);
% Area of the triangle
Atot = 0.5*(s2(1)*s3(2)-s2(2)*s3(1));
% Check whether area is negative (nodes given counterclockwise)
if (Atot < 0)
error(’The nodes of the element given in wrong order’)
% Compute the gradient of the vectors.
grad_phi1e = [-s1(2);s1(1)]/(2*Atot);
grad_phi2e = [-s2(2);s2(1)]/(2*Atot);
grad_phi3e = [-s3(2);s3(1)]/(2*Atot);
grad_phi = [grad_phi1e grad_phi2e grad_phi3e];
6.3 2D Finite Element Analysis
% Compute all the integrals for this particular element.
for iIdx = 1:3
for jIdx = 1:3
Ae(iIdx,jIdx) = grad_phi(:,iIdx)’ * grad_phi(:,jIdx) * Atot;
The right-hand side b is constructed following the same assembling pro-
cedure, i.e., by summing the contributions be
i from each element. Often, Ae
and be
i are evaluated by numerical rather than analytical integration.
Now, we have one row in A and b for every node in the mesh, since we
have tested the diﬀerential equation at all the nodes, including those where
the solution is known from the Dirichlet boundary condition. This is not
exactly what we want, since the test function must be zero along the Dirichlet
boundary. We correct this by removing the rows in A and b corresponding to
nodes where the solution is known. A more eﬃcient approach, in particular
for large problems, is to compute the local contribution for each element but
assemble only the rows that are not associated with a Dirichlet boundary.
6.3.2 Unstructured Meshes in Practice
When writing FEM programs it is important to treat unstructured meshes in
an eﬃcient and well-organized way. The most common way is explained here
for the small mesh shown in Figure 6.9. The mesh consists of 6 nodes and 4
triangular elements.
−0.5
−0.4
−0.2
x [m]
y [m]
Fig. 6.9. A 2D mesh. The node numbers are shown next to the corresponding nodes
and the element numbers in the center of the corresponding triangles.
We will use the fact that a triangle is built up by three nodes. Therefore,
we store the coordinates of the nodes in a table no2xy; i.e., given a global
node number the table no2xy provides its coordinates. Next, we construct the
6 The Finite Element Method
triangles by listing the nodes that are the vertices of each triangle in another
table el2no; i.e., given an element number the table el2no provides its global
node numbers. For the mesh shown in Figure 6.9, the information in no2xy is
given in Table 6.1, and el2no in Table 6.2.
Node
0.0 -0.5 -0.8 0.6 0.0 1.0
1.0 0.5 0.0 0.4 -0.2 -0.1
Table 6.1. Given a global node number, this table (no2xy) provides its coordinates.
Element 1 2 3 4
Node 1
1 4 3 5
Node 2
2 2 5 6
Node 3
4 5 2 4
Table 6.2. Given an element number, this table (el2no) provides its global node
numbers.
This is how it looks in MATLAB:
>> no2xy
no2xy =
-0.5000
-0.8000
0.6000
1.0000
1.0000
0.5000
0.4000
-0.2000
-0.1000
>> el2no
el2no =
The same idea can be used to store other types of elements such as lines and
quadrilaterals.
6.3.3 MATLAB: 2D FEM Using Nodal Basis Functions
We will present a program showing the assembling procedure for the capac-
itance calculation in Section 3.1. However, ﬁrst it is useful to show how the
mesh can be generated and used for computation in MATLAB.
6.3 2D Finite Element Analysis
Generate a Mesh of Triangles
Mesh generation is a discipline in itself, and it is an active ﬁeld of research. An
overview of both commercial and free mesh generators (a program that creates
a FEM mesh) is available at the Meshing Research Corner [50]. Many of these
programs use their own input and output format. However, most likely the
output is based on the ideas presented in Section 6.3.2. Thus, if we understand
the basic principles of how an unstructured mesh is organized, we can extract
the necessary information from most mesh generators. Of course, we will need
the documentation of the mesh generator and to work with simple examples
in the beginning.
Solving the Laplace Equation
Now we are ready to write the program solving for the potential φ(r ) =
j=1 φjϕj(r ) at the nodes (vector z). Once the potential is known, the
capacitance per unit length C can be computed from the energy relation
C = 2W/U 2, where W is the electrostatic energy per unit length and U is the
potential diﬀerence between the inner and outer conductors. The electrostatic
energy per unit length can be computed using the following quadratic form
(see Section 6.7):
W[φ] = 1
E · DdS = 1
ϵ0|∇φ|2dS
= ϵ0
∇ϕi · ∇ϕj dS
= ϵ0
2 zTAz.
The MATLAB calculation can be done as follows:
% Physical constants
mu0 = 4*pi*1e-7;
% Permeability in vacuum
c0 = 299792456;
% Speed of light in vacuum
eps0 = 1/(mu0*c0*c0);
% Permittivity in vacuum
% Voltage between inner and outer conductor.
U = 1;
% Read the grid from the file ’unimesh0.mat’.
% This file contains the variables no2xy, el2no, noInt, noExt
load unimesh0
noNum = size(no2xy,2);
elNum = size(el2no,2);
% Scale the domain to measure 2cm x 2cm.
6 The Finite Element Method
% The initial mesh fitted the unit square:
% -1 < x < 1 and -1 < y < 1.
no2xy = 1e-2*no2xy;
% Assemble the matrix A and vector b.
A = zeros(noNum);
b = zeros(noNum,1);
for elIdx = 1:elNum
% Get the nodes and their coordinates
% for the element ’elIdx’.
no = el2no(:,elIdx);
xy = no2xy(:,no);
% Compute the element matrix and add
% the contribution to the global matrix.
A_el = CmpElMtx(xy);
A(no,no) = A(no,no) + A_el;
% Get the indices of the nodes.
no_ess = union(noInt, noExt);
no_all = 1:noNum;
no_nat = setdiff(no_all, no_ess);
% Pick out the parts of the matrix and the vectors
% needed to solve the problem.
A_ess
= A(no_nat,no_ess);
A_nat
= A(no_nat,no_nat);
= b(no_nat);
= zeros(length(no_all),1);
z(noInt) = U*ones(length(noInt),1);
z_ess
= z(no_ess);
% Solve the system of linear equations.
z_nat = A_nat\(b - A_ess*z_ess);
% Build up the total solution.
z = zeros(length(no_all),1);
z(no_ess) = z_ess;
z(no_nat) = z_nat;
% Compute the capacitance.
W = 0.5*eps0*(z’*A*z);
C = 2*W/Uˆ2;
disp([’C per unit length [pF/m] = ’ num2str(C/1e-12)])
6.3 2D Finite Element Analysis
The potential distribution computed by the MATLAB program is shown in
Figure 6.10, and the calculated value of the capacitance is 91.47360 pF/m. Not
all these digits are correct, and we will discuss how to improve the accuracy
in the next section. Note that there are large gradients near the reentrant
corners of the inner conductor where the electric ﬁeld is singular, but these
gradients are not well resolved on the rather coarse mesh in Figure 6.10.
−0.01
0.01
−0.01
0.01
x [m]
y [m]
φ [V]
Fig. 6.10. The potential distribution between the inner conductor (φ = 1 V) and
the outer conductor (φ = 0 V).
Review Questions
6.3-1 Explain how Dirichlet, Neumann, and Robin boundary conditions are
incorporated into the system of linear equations for a FEM.
6.3-2 Derive the weak forms of the 2D Helmholtz equation with homogeneous
Dirichlet and homogeneous Neumann boundary conditions. What are the
diﬀerences between the two weak forms?
6.3-3 What is done in the assembly procedure?
6.3-4 Explain the diﬀerence between local and global node numbers.
6.3-5 Is a solution expanded in nodal basis functions ϕi guaranteed to be
continuous?
6.3-6 How are unstructured ﬁnite element meshes constructed, represented,
and stored by computers?
6.3-7 List the steps involved in computing the capacitance for a coaxial cable
by the FEM.
6 The Finite Element Method
6.4 Adaptivity
Triangular elements allow for local reﬁnement of the mesh. Hence high reso-
lution can be used where it is required, for example close to singularities and
ﬁne geometrical features, whereas lower resolution can be used where that is
suﬃcient. This allows us to use the computational power where it contributes
the most to the overall accuracy.
In general, one does not know a priori how to reﬁne the mesh in order
to get optimal eﬃciency. Therefore, adaptive schemes are usually based on a
posteriori error estimates or error indicators (see, e.g., [66, 45]).
A typical
adaptive algorithm repeats the following steps until a satisfactory solution is
obtained:
3. Reﬁne the mesh by splitting the elements with largest errors into smaller
elements.
Algorithms for splitting selected elements into smaller elements may be quite
complicated (see, e.g., [9]). However, software for mesh generation often in-
cludes this functionality.
To illustrate the advantages of adaptivity, we return to the capacitance
calculation that we have already used as an illustration in Sections 3.1 and
6.3 (see also Appendix A.3). For uniform meshes, this singularity reduces the
convergence from O(h2) = O(1/Nn) to O(h4/3) = O(N −2/3
), where Nn is
the number of nodes in the mesh. By using FEM with adaptively generated
meshes it is possible to restore quadratic convergence so that the error scales
as O(1/Nn) despite the singularity. We use the code shown in Section 6.3.3 and
two sets of meshes. The ﬁrst set of meshes is generated by uniform reﬁnement
(all elements are split into smaller elements), and the second set is generated
by adaptive reﬁnement (only selected elements are reﬁned). A close-up of one
of the adaptively reﬁned meshes is shown in Figure 6.11.
The relative error of the computed capacitance is shown in Figure 6.12
for both uniformly and adaptively reﬁned meshes. The horizontal axis shows
the total number of nodes Nn in the mesh. The circles show the relative
error |C(Nn) −C0|/C0 of the computed capacitances for diﬀerent Nn. The
exact value of C0 is unknown in this case, but a suﬃciently accurate refer-
ence solution (C0 = 90.6145 pF with 6 correct digits) is obtained by careful
extrapolation of the computed values.
The solid curves in Figure 6.12 ﬁt the error model e(Nn) = α/N p
n to
computed values of the capacitance C(Nn). With uniform mesh reﬁnement we
ﬁnd that the capacitance converges as N −0.7
∝h1.4. This is quite close to the
theoretical asymptotic convergence rate h4/3. With adaptive mesh reﬁnement
we ﬁnd that the convergence rate is restored to N −1 ∝h2, which is the rate
we get for uniformly reﬁned meshes when the solution is smooth (suﬃciently
regular).
6.4 Adaptivity
0.48
0.49
0.51
0.52
0.48
0.485
0.49
0.495
0.505
0.51
0.515
0.52
x [m]
y [m]
Fig. 6.11. The mesh after adaptive mesh reﬁnement at one of the corners of the
inner conductor where the potential changes rapidly. The smallest triangles at the
corner measure approximately 40 µm.
Nn [−]
Relative error [−]
Uniform refinement
Adaptive refinement
Fig. 6.12. The relative error in the capacitance as a function of the number of
nodes in the mesh.
Review Questions
6.4-1 Why and when is adaptivity useful? List advantages and disadvantages
of adaptivity. Write down a general formulation, in words, for the objective
of an adaptive computation. How could you achieve this objective?
6 The Finite Element Method
6.4-2 Can adaptivity restore the nominal order of convergence even if the
solution is singular? What implications does this have for the error as a
function of the number of degrees of freedom?
6.5 Vector Equations
In this section, we will discuss a vector equation: the curl-curl equation of elec-
tromagnetics. However, as an intermediate step, we will ﬁrst see how to choose
elements for the 1D Maxwell equations written in terms of two variables, one
component each of E and H.
6.5.1 Mixed-Order FEM for Systems of First-Order Equations
In Section 6.2 we studied the model problem (6.1), i.e., the second-order equa-
tion for the electric ﬁeld E in one dimension:
+ ω2ϵE = 0.
(6.31)
The second-order equation can be split into two ﬁrst-order equations involving
also the magnetic ﬁeld H (a factor of j is removed in order to avoid complex
variables):
dx −ωµH = 0,
(6.32)
dx + ωϵE = 0.
(6.33)
To solve this pair of ﬁrst-order equations, we ﬁrst seek ﬁnite element represen-
tations for E and H that are suited for this. Somewhat arbitrarily, we choose
to expand E, as before, in piecewise linear functions li(x) (often referred to
as “tent functions”). This gives
E(x) =
Eili(x).
(6.34)
Equation (6.32) then leads us to expand H in the same class of functions as
dE/dx, that is, in piecewise constants ci(x) (“top-hat functions”). This gives
H(x) =
Hi+ 1
2 ci+ 1
2 (x),
(6.35)
where ci+ 1
2 (x) = 1 if xi < x < xi+1, and otherwise, ci+ 1
2 (x) = 0. Figure 6.13
shows the tent and top-hat functions together with their derivatives.
6.5 Vector Equations
dH/dx
dE/dx
Fig. 6.13. Basis functions for the electric and magnetic ﬁelds together with their
derivatives.
To solve the set of ﬁrst-order equations (6.32)–(6.33), we try a form of
Galerkin’s method. Since (6.32) contains H and dE/dx, which are both piece-
wise constant, we multiply (6.32) by piecewise constant weighting functions
ci+ 1
2 (x) and integrate over x. After division by the step length h this gives
Ei+1 −Ei
−ωµHi+ 1
2 = 0,
(6.36)
which is exactly the simplest ﬁnite diﬀerence approximation for (6.32) on a
staggered grid.
Equation (6.33), on the other hand, contains E. Therefore, we multiply it
by a piecewise linear weighting function and integrate over x:
 xi+1
xi−1
dx + ωϵE
li(x)dx = 0.
(6.37)
We substitute the representations (6.34) and (6.35) into (6.37) and obtain
 xi+1
xi−1
(Hi+ 1
2 −Hi−1
2 )δ(x −xi)li(x)dx + ωϵ
 xi
xi−1
Ei−1li−1(x)li(x)dx
 xi+1
xi−1
Eil2
i (x)dx +
 xi+1
Ei+1li(x)li+1(x)dx
= 0.
(6.38)
Evaluation of the integrals and division by h gives
Hi+ 1
2 −Hi−1
+ ωϵ
3Ei + 1
6(Ei−1 + Ei+1)
= 0.
(6.39)
Thus, the FEM equations corresponding to the coupled system (6.32)–
(6.33) of ﬁrst-order equations are
Ei+1 −Ei
= ωµHi+ 1
(6.40)
6 The Finite Element Method
Hi+ 1
2 −Hi−1
= −ωϵ
3Ei + 1
6(Ei−1 + Ei+1)
(6.41)
This FEM-discretized system looks almost the same as the ﬁnite diﬀerence
approximation of (6.32)–(6.33) with staggered meshes. It diﬀers only in the
form for E on the right-hand side of (6.41). The similarity comes from the
choice of basis and test functions. E was expanded in piecewise linear func-
tions that are centered on the nodes: the integer mesh. H was expanded in
piecewise constant functions that are centered on the midpoints or the half-
mesh. Furthermore, (6.40) is centered on the half-grid. We constructed it this
way by multiplying (6.32) by the piecewise constants ci+ 1
2 (x) before integra-
tion. Similarly, (6.41) is centered on the integer grid, because we multiplied
(6.33) by the piecewise linear functions li(x).
This is a simple example of mixed elements. We can make the following
analogy with staggered meshes for ﬁnite diﬀerences:
A variable expanded in piecewise linear functions (FEM) is placed on the
integer mesh (FD).
A variable expanded in piecewise constant functions (FEM) is placed on
the half mesh (FD).
An equation multiplied by piecewise linear functions (FEM) is evaluated
on the integer mesh (FD).
An equation multiplied by piecewise constant functions (FEM) is evaluated
on the half mesh (FD).
To emphasize the similarity between ﬁnite element and ﬁnite diﬀerence meth-
ods, we mention that if the integration in (6.38) is made by the trapezoidal
rule,
 xi+1
f(x)dx ≈(h/2)[f(xi)+f(xi+1)], the ωϵE term becomes “lumped”,
(4Ei + Ei−1 + Ei+1)/6 →Ei, and the FEM scheme becomes identical to the
ﬁnite diﬀerence scheme.
One can see that the discretization (6.40)–(6.41) is in fact a Galerkin
method, because the equation for ωE has been tested with the basis functions
for E and the equation for ωH has been tested with the basis functions for H.
It may also be noted that Faraday’s law is identically satisﬁed by the FEM
representation for E and H, while Amp`ere’s law (6.33) is satisﬁed only in the
weak sense, that is, as a weighted average.
6.5.2 The Curl-Curl Equation and Edge Elements
So far, we have discussed basis functions only for scalar equations, and used
piecewise linear (nodal) and piecewise constant basis functions. To deal with
vector quantities, such as the electric ﬁeld, a ﬁrst attempt might be to expand
each vector component separately in nodal basis functions. It turns out that
such an approach leads to nonphysical solutions, referred to as spurious modes.
This can be avoided by using edge elements [48], which are very well suited
for approximating electromagnetic ﬁelds. The (basis functions for) edge ele-
ments are constructed such that their tangential components are continuous
6.5 Vector Equations
across element borders, whereas their normal components are allowed to be
discontinuous. Edge elements are also called curl-conforming because the con-
tinuous tangential components imply that the curl of an edge element does
not contain delta functions at the element boundaries. Thus, an electric ﬁeld
that is expanded in terms of edge elements has a curl that is square integrable.
In this section, we will show how edge elements can be applied to solve
the curl-curl equation for E:
µ−1∇× E
ω2ϵ −jωσ
E = −jωJs in S,
(6.42)
ˆn × E = P on L1,
(6.43)
ˆn ×
µ−1∇× E
+ γ ˆn × ˆn × E = Q on L2.
(6.44)
Again, we have both Dirichlet and Robin boundary conditions, and Js is an
imposed source current.
We proceed along similar lines as in the scalar problem (6.11)–(6.13). Thus,
we take the scalar product of (6.42) and the test function W i and integrate
over the computational domain S using the vector identity (4.4):
W i ×
µ−1∇× E
= µ−1 (∇× W i) · (∇× E)
−W i · ∇×
µ−1∇× E
(6.45)
The divergence term in (6.45) is integrated using Gauss’s law in two dimen-
sions
S ∇· F dS =
L1+L2 F · ˆn dl, which gives the weak form of the vector
Helmholtz equation
µ−1 (∇× W i) · (∇× E) −
ω2ϵ −jωσ
W i · E
W i · (Q −γ ˆn × ˆn × E) dl = −jω
W i · JsdS.
(6.46)
The major diﬀerence from the scalar problem lies in the choice of basis func-
tions, where we use the edge element basis functions N i(r) instead of nodal
basis functions ϕi in this case.
Edge elements associate the degrees of freedom to the edges of the mesh
rather than the nodes (this is why they are usually referred to as edge elements
in the ﬁrst place). Therefore, we have to number all the edges in the mesh
and also give them reference directions. We will discuss the basis functions in
more detail later. The edges are labeled by integers 1, 2, . . . , Ne. We expand
the solution E(r ) in terms of the basis functions:
E(r ) =
EjN j(r ),
(6.47)
where Ej is the tangential electric ﬁeld along the jth edge, in the direction of
its reference direction.
6 The Finite Element Method
We follow Galerkin’s method, choose the test functions W i(r ) = N i(r ),
and substitute (6.47) and the test functions into the weak form (6.46). This
gives a linear system of equations Az = b with
Aij =
µ−1 (∇× N i) · (∇× N j) −
ω2ϵ −jωσ
N i · N j
γ (ˆn × N i) · (ˆn × N j) dl,
(6.48)
zj = Ej,
(6.49)
bi = −jω
N i · Js dS −
N i · Q dl.
(6.50)
The index j labels all edges and i all edges where E is unknown, i.e., all edges
excluding those on the boundary L1.
6.5.3 Edge Elements on Cartesian Grids
Here, we give explicit expressions for the edge basis functions N i. For sim-
plicity, we ﬁrst study those on a rectangular element that occupies the region
deﬁned by xe
a ≤x ≤xe
b and ye
a ≤y ≤ye
b. The local numbering of the nodes
and the edges is shown in Figure 6.14 together with the local reference direc-
tions of the edges.
x [m]
y [m]
Fig. 6.14. Local numbering for the element e. The local reference directions for the
edges are indicated by arrows, and the corresponding local edge numbers are shown
inside the arrows.
The local basis functions N e
i for a rectangular ﬁnite element are shown in
Figure 6.15 and can be expressed explicitly as
6.5 Vector Equations
1 = + ye
b −y
b −yea
2 = + x −xe
b −xea
3 = −y −ye
b −yea
4 = −xe
b −x
b −xea
(6.51)
Fig. 6.15. Local basis functions N e
1, N e
2, N e
3, and N e
4 on a rectangular element,
shown in this order from left to right.
The global basis functions must be chosen such that the tangential com-
ponents of E are continuous across element boundaries. However, the normal
component is allowed to be discontinuous [since ∇· E does not appear in the
FEM matrix (6.48)]. Therefore, it is natural to associate the basis functions
with the value of the electric ﬁeld along the edges. The required representation
is simply
Ex(x, y) =
Ex|i,j ci+ 1
2 (x)lj(y),
Ey(x, y) =
Ey|i,j li(x)cj+ 1
2 (y).
(6.52)
Two such global basis functions are shown in Figure 6.16.
Note that the edge elements have a mixed order of representation. Within
each cell, Ex is constant in x and linear in y, and vice versa for Ey. The edge
elements are not complete to ﬁrst order, but represent a subset that is suitable
for the curl-curl equation.
Edge Elements on Bricks and Hexahedra
We extend edge elements on rectangles to brick elements (hexahedra) in three
dimensions. The electric ﬁeld is represented as
6 The Finite Element Method
Fig. 6.16. Two global basis functions for rectangular edge elements on a grid.
Ex(x, y, z) =
Ex|i,j,k ci+ 1
2 (x)lj(y)lk(z),
Ey(x, y, z) =
Ey|i,j,k li(x)cj+ 1
2 (y)lk(z),
(6.53)
Ez(x, y, z) =
Ez|i,j,k li(x)lj(y)ck+ 1
2 (z).
These edge elements are the FEM equivalent of the Yee cell. For instance,
Ex in the Yee cell is located at the midpoint of the element in the x-direction,
and the FEM basis function is the piecewise constant ci+ 1
2 (x), also associated
with the midpoint in x. In the y and z directions, the Yee cell puts Ex on
the integer grid, and the FEM representation is in terms of piecewise linears,
which are also associated with the integer grid.
For the magnetic ﬁeld, we choose a representation that corresponds to the
curl of the electric ﬁeld. For instance, from the x-component of Faraday’s law,
jωµHx = ∂Ey/∂z −∂Ez/∂y, and the edge element representation (6.53) for
E, we see that the equation can be satisﬁed exactly if Hx is expanded with
piecewise linears in x, and piecewise constants in y and z. Thus, for H, we
choose the representation
Hx(x, y, z) =
Hx|i,j,k li(x)cj+ 1
2 (y)ck+ 1
2 (z),
Hy(x, y, z) =
Hy|i,j,k ci+ 1
2 (x)lj(y)ck+ 1
2 (z),
(6.54)
Hz(x, y, z) =
Hz|i,j,k ci+ 1
2 (x)cj+ 1
2 (y)lk(z).
This representation of H also conforms to the Yee arrangement. Each com-
ponent of H is associated with the midpoint of a face that has the same
6.5 Vector Equations
normal direction as the H component. For instance, Hx is associated with
the midpoints of the cell boundaries with x constant. The basis functions we
have chosen for H are referred to as face elements. These basis functions are
divergence-conforming, because the normal components are continuous at all
cell boundaries.
It should be pointed out that this representation of E and H gives exactly
the FDTD algorithm if matrices such as the one in (6.48) are assembled using
trapezoidal integration.
6.5.4 Eigenfrequencies of a Rectangular Cavity
Here, we use the edge elements to compute the eigenfrequencies and the eigen-
modes for a 2D rectangular cavity. First, we consider a 2×2-element resonator
to demonstrate the features of edge elements. Then, we increase the resolution
and study a more realistic case.
2 × 2-Element Resonator
We choose a square domain with width ax = 2 m and height ay = 2 m. The
cavity resonator is discretized by 2 × 2 square elements, which is the smallest
possible system that gives meaningful results. The mesh with numbering of
nodes, edges, and elements is shown in Figure 6.17. The positive reference
directions (in this case chosen arbitrarily) for the edges are indicated by the
arrows.
−0.5
−0.5
x [m]
y [m]
Fig. 6.17. Grid for 2 × 2-element resonator. The nodes (with numbers) are shown
by black dots, and the edges (with numbers and positive directions) are indicated
by the arrows centered on the edges of the grid. The element numbers are shown in
the circles, centered in the corresponding elements.
6 The Finite Element Method
The numbering is systematically organized in Table 6.3 for the nodes,
Table 6.4 for the edges, and Table 6.5 for the elements.
Node
−1.0 0.0
1.0 −1.0 0.0 1.0 −1.0 0.0 1.0
−1.0 −1.0 −1.0 0.0 0.0 0.0 1.0 1.0 1.0
Table 6.3. Given a node number we get the coordinates of that node.
Edge
1 2 3 4 5 6 7 8 9 10 11 12
Node 1 1 5 9 5 8 7 4 1 6 2
Node 2 2 2 6 8 9 8 7 4 3 3
Table 6.4. Given an edge number we get the node numbers of that edge.
Element 1 2 3 4
Node 1
6 1 7 6
Node 2
5 2 4 9
Node 3
2 5 5 8
Node 4
3 4 8 5
Table 6.5. Given an element number we get the node numbers of that element.
The boundary of the computational domain is metal and the interior S is
air, i.e., σ = 0, µ = µ0 and ϵ = ϵ0. Thus, the eigenvalue problem is stated as
∇× ∇× E = ω2ϵ0µ0E in S,
(6.55)
ˆn × E = 0 on L1.
(6.56)
We use (6.45) to arrive at the weak form
(∇× W i) · (∇× E) dS = k2
W i · E dS,
(6.57)
where k2 = ω2ϵ0µ0. We expand the electric ﬁeld in terms of the basis functions,
i.e., approximate the electric ﬁeld by (6.47), and test with W i = N i. Then,
we get a generalized eigenvalue problem Sz = k2Mz, from which we solve
for the eigenvalues k2 and the eigenvectors z = [z2, z4, z11, z12], where z2, z4,
z11, and z12 correspond to edges in the interior of the cavity. The remaining
coeﬃcients in (6.47) are zero because of the PEC boundary. The elements in
S and M are given by
6.5 Vector Equations
Sij =
(∇× N i) · (∇× N j) dS,
(6.58)
Mij =
N i · N j dS,
(6.59)
where the indices i and j run over all edges except those on the metal bound-
ary, i.e., i = 2, 4, 11, 12 and j = 2, 4, 11, 12. By terminology borrowed from
mechanical engineering, S is called the stiﬀness matrix and M is called the
mass matrix.
For realistic cases, however, we do not evaluate Sij and Mij by (6.58) and
(6.59). It is more convenient to use the assembling procedure described in
Section 6.3.1. Consequently, we evaluate the element matrices Se
ij and M e
ij by
ij =
 ye
 xe
(∇× N e
i) ·
∇× N e
dx dy,
(6.60)
ij =
 ye
 xe
i · N e
j dx dy.
(6.61)
Thus, we exploit the expressions for N e
i and the corresponding local num-
bering and reference directions of the edges given in Section 6.5.3 for an ar-
bitrary element e; see Figure 6.14. We evaluate (6.60) for the element e that
gives the element stiﬀness matrix
Se =
x/le
x/le
y/le
y/le
x/le
x/le
y/le
y/le
(6.62)
where the edges of the rectangle have lengths le
x = xe
b −xe
a and le
y = ye
b −ye
along the x- and y-axes, respectively. Evaluation of (6.61) for the element e
gives the corresponding element mass matrix
Me = le
0 −1 0
0 −1
−1 0
0 −1 0
(6.63)
The assembling procedure gives the global matrices S and M shown be-
low, where the subindices in brackets show the index of the element that
contributed to the matrix element. For edge elements, the reference direction
of the edges must be compared for the local and global elements. If one of the
two edges is reversed between the local and global ordering, the sign of the
corresponding row and column in the element matrix must be changed before
it is added to the global matrix:
6 The Finite Element Method
+1 0 0 −1
0 0 0 0
0 0 0 0
−1 0 0 +1
Element 1
+1 0 +1 0
0 0 0 0
+1 0 +1 0
0 0 0 0
Element 2
0 +1 +1 0
0 +1 +1 0
Element 3
0 0 0 0
0 +1 0 −1
0 0 0 0
0 −1 0 +1
Element 4
+1[1] + 1[2]
+1[2]
−1[1]
+1[3] + 1[4]
+1[3]
−1[4]
+1[2]
+1[3]
+1[2] + 1[3]
−1[1]
−1[4]
+1[1] + 1[4]
Global matrix
M = 1
+2 0 0 0
0 0 0 0
0 0 0 0
0 0 0 +2
Element 1
+2 0 0 0
0 0 0 0
0 0 +2 0
0 0 0 0
Element 2
0 +2 0 0
0 0 +2 0
Element 3
0 0 0 0
0 +2 0 0
0 0 0 0
0 0 0 +2
Element 4
+2[1] + 2[2]
+2[3] + 2[4]
+2[2] + 2[3]
+2[1] + 2[4]
Global matrix
To summarize, we solve the eigenvalue problem
0 1 −1
2 1 −1
1 2 0
−1 −1 0 2
= k2
2/3 0
Table 6.6 shows the eigenvalues and eigenvectors for this particular set-
ting. Analytical treatment of this particular problem shows that there is
an inﬁnitely degenerate eigenvalue k2 = 0 that corresponds to electrostatic
6.5 Vector Equations
modes E = −∇φ. The electromagnetic modes have k2 = (π/2)2(n2
x + n2
for nx = 0, 1, . . . and ny = 0, 1, . . ., where the combination nx = ny = 0 is
excluded. The lowest nonzero eigenvalues are associated with the two (degen-
erate) modes with k2 = (π/2)2 ≈2.5 and one mode with k2 = 2(π/2)2 ≈5.0.
Mode k2
+1/2
+1/2
−1/2
+1/2
3 −1/
2 +1/
2 +1/
+1/2
+1/2
+1/2
−1/2
Table 6.6. Numerical eigenvalues and eigenvectors for the four-element cavity.
The ﬁgures below show the four numerical eigenmodes computed on the
2 × 2-element discretization. Figure 6.18 shows the electrostatic mode on this
mesh. It can be expressed in terms of a scalar potential, i.e., E = −∇φ,
where the electric potential φ is expanded in piecewise bilinear nodal based
ﬁnite elements, with φ = 0 on the metal boundary and φ ̸= 0 on the central
node. This static mode has the eigenvalue k2 = 0.
−0.5
−0.5
x [m]
y [m]
Fig. 6.18. Electric ﬁeld for mode 1 with k2 = 0. This is a static ﬁeld that can be
expressed in terms of a scalar potential, i.e., E = −∇φ.
The next two modes are shown in Figure 6.19, and they correspond to the
physical modes with the lowest resonance frequency. The two modes of the
discretized system have the same eigenvalue k2 = 3 and are therefore said to
be degenerate. The corresponding analytical eigenvalue is k2 = (π/2)2 ≈2.5.
6 The Finite Element Method
−0.5
−0.5
x [m]
y [m]
−0.5
−0.5
x [m]
y [m]
Fig. 6.19. Electric ﬁeld for mode 2 and 3. The two have the eigenvalue k2 = 3,
and thus, they are degenerate. They correspond to the two degenerate fundamental
resonances of the cavity.
Figure 6.20 shows the third resonance of the cavity. It has the eigenvalue
k2 = 6, and the corresponding analytical eigenvalue is k2 = 2(π/2)2 ≈5.0.
Observe that a linear combination of the four numerical eigenmodes can
represent any solution on the 2 × 2-element discretization that satisﬁes the
boundary condition.
Better-Resolved Resonator
Next, we study a rectangular domain with width ax = 1.3 m and height
ay = 0.9 m. We choose square cells of side 0.1 m, which gives a grid with
13×9 elements. We follow the approach outlined above, and the fundamental
6.5 Vector Equations
−0.5
−0.5
x [m]
y [m]
Fig. 6.20. Electric ﬁeld for mode 4 with the eigenvalue k2 = 6. This mode corre-
sponds to the third resonance of the cavity.
eigenmode, which corresponds to the lowest resonance frequency, is shown in
Figure 6.21. The corresponding analytic eigenmode is E = E0 sin(πx/ax)ˆy.
x [m]
y [m]
Fig. 6.21. The fundamental eigenmode on a rectangle with width ax = 1.3 m and
height ay = 0.9 m.
The numerical eigenvalues k2 are shown in Figure 6.22 by circles and the
analytical eigenvalues k2 = (πnx/ax)2 +(πny/ay)2 by crosses. Again, we have
nx = 0, 1, 2, . . . and ny = 0, 1, 2, . . ., where the combination nx = ny = 0 is
excluded.
6 The Finite Element Method
mode [−]
k2 [1/m2]
Fig. 6.22. Spectrum of eigenvalues for a rectangle with width ax = 1.3 m and
height ay = 0.9 m. The numerically computed eigenvalues are shown by circles and
their analytical counterparts by crosses.
An important and very good property of the edge elements is that there
is a one-to-one correspondence between the lowest nonzero numerical eigen-
modes and the lowest nonzero analytical eigenmodes. This can be seen in
Figure 6.22 for our particular problem. The nodal elements, which we do
not use for vector-valued electromagnetic ﬁelds, do not share this property,
and the drawbacks of nodal elements can be clearly seen by examining the
spectrum of the curl-curl operator. Instead of exact zero eigenvalues for the
∇× ∇×-operator corresponding to electrostatic modes E = −∇φ, the nodal
elements produce many eigenvalues between 0 and the smallest physical one.
This is called spectral pollution, because it adds nonphysical eigenvalues in
between the correct eigenvalues shown in Figure 6.22. The eigenfunctions of
the spurious solutions have rapid space variation associated with nonzero di-
vergence. The nodal elements also cause much dispersion at short wavelengths
(similar to the 1D result for ﬁrst-order derivatives on nonstaggered meshes,
discussed in Section 3.2), and this phenomenon also contributes to the spectral
pollution.
By contrast, the edge elements produce exactly one zero eigenvalue for
each interior node. Each such eigenvalue corresponds to a mode E = −∇φ,
which has a zero eigenvalue, since ∇×∇×(−∇φ) = 0 = k2(−∇φ) gives k2 =
representation, because the modes E = −∇φ, where φ is piecewise bilinear,
belong to the set of edge elements. In our problem with the rectangular cavity,
there are 12 × 8 = 96 interior nodes and therefore 96 zero eigenvalues, and
these are given the mode number zero in Figure 6.22.
6.5 Vector Equations
It is in particular with respect to the electrostatic modes that the node-
based elements fail for electromagnetic problems. Node-based elements do
not contain the proper null-space for the curl-operator. The reason for this is
that the potential modes E = −∇φ for continuous, piecewise linear φ do not
have continuous normal components and therefore do not belong to the node-
based elements for E, which are divergence conforming. The edge elements
are not divergence conforming but allow jumps in the normal component at
cell boundaries.
6.5.5 Edge Elements on Triangles
Edge elements can also be formulated on triangles, tetrahedra, pyramids, and
prisms. Figure 6.23 shows the local numbering of the nodes and the edges of
a triangle.
−0.2
−0.1
−0.2
−0.1
x [m]
y [m]
Fig. 6.23. Local numbering for the element e. The local reference directions for the
edges are chosen to be from lower to higher (local) node number and are indicated
by arrows. The corresponding local edge numbers are shown in the arrows.
The edge element basis functions on a triangle can be expressed in the
nodal basis functions ϕe
1 = ϕe
1∇ϕe
2 −ϕe
2∇ϕe
2 = ϕe
1∇ϕe
3 −ϕe
3∇ϕe
(6.64)
3 = ϕe
2∇ϕe
3 −ϕe
3∇ϕe
Figure 6.24 shows the local basis functions. These basis functions are propor-
tional to the vector ﬁeld r ˆφ, where r and φ are local polar coordinates around
the node opposite to the edge on which the basis function has a nonzero tan-
gential component. The magnitudes of the basis functions are made such that
the tangent line integral of the basis function along the edge it is associated
with is 1.
6 The Finite Element Method
Fig. 6.24. N e
1(r ) is shown to the left, N e
2(r ) in the middle, and N e
3(r ) to the
right.
Some important properties of the edge elements on triangles are worth
pointing out. Just as for the rectangular edge elements, one constructs global
basis functions such that the tangential component of E is continuous over
element interfaces.
A global edge basis function is shown in Figure 6.25. Note that the normal
component is discontinuous at the edges. Similar to the edge elements on
rectangles, the tangential component is constant along one edge and zero
along all the other edges of the rectangle.
Fig. 6.25. Global edge basis function in 2D, spanning two triangles.
Also similar to their rectangular counterparts, the edge elements on tri-
angles have mixed order. One can add three more functions, constructed in a
similar way as those in (6.64), but with the minus signs replaced by plus, to
make the basis complete to ﬁrst order. The “missing” ﬁrst-order edge elements
6.5 Vector Equations
are gradients of scalar functions. Whether or not it is useful to include these
gradients depends on the problem. Since the gradients do not contribute to
∇× E, it is often more eﬃcient not to leave them out. The edge elements we
have discussed here are often referred to as order (0, 1), where 1 refers to those
components that contribute to the curl, and 0 to the gradient part. There are
also higher-order edge elements available [83, 37], which often can be more
economical to use. However, these are not considered in this book.
6.5.6 Edge Elements in Practice
In practice, the administration of edge elements requires certain special tech-
niques, which are nonstandard in the context of the conventional FEM with
node-based elements. These issues can to some extent be avoided on struc-
tured meshes of squares or cubes. For unstructured meshes, however, it is
necessary to have eﬃcient and reliable techniques, to for example, number
the edges in the mesh and associate a reference direction with each edge. It
is useful to remember the ﬁeld representation E(r ) = Ne
j=1 EjN j(r ) when
such techniques are designed.
The reference direction is usually based on the global node numbers at the
endpoints of the edge under consideration; for example, the vector ﬁeld of an
edge element basis function N i is directed from the lower to the higher global
node number when the coeﬃcient for the basis function is positive. One or
several of the basis functions on the local elements that share an edge may
be deﬁned in the reverse direction. One way to deal with this problem is to
multiply all local basis functions with reverse direction by −1; i.e., the local
basis function N e
i relates to the global basis function as N i = −N e
i. Another
way to deal with this problem is to sort the nodes of all individual element in
ascending order. Since the basis functions deﬁned in (6.64) are directed from
lower to higher local node number; this implies that they are also directed from
lower to higher global node number. This is the approach we will take in the
next section, where a MATLAB program based on triangular edge elements
is presented.
Each unknown (or coeﬃcient Ej and its basis function) must also be as-
sociated with an edge in the unstructured mesh. We assume that all edges in
the mesh are deﬁned by its start and end nodes and that they also have been
assigned a global edge number. To simplify the assembly procedure, we want
to create a table el2ed that contains the global edge numbers for the three
edges of each element. This can be done rather eﬃciently based on sorting
techniques; see [39] for a more details. In MATLAB, this can be done by the
function unique.
6.5.7 MATLAB: FEM with Triangular Edge Elements
We will here present a MATLAB function that given a triangular mesh on
the form presented in Section 6.3.2, computes the mass and stiﬀness matrices
6 The Finite Element Method
M and S. A routine for plotting a ﬁeld, given the vector with coeﬃcients Ej
that corresponds to the ﬁeld, is also provided.
We begin by sorting the nodes of the individual elements in ascending
order. Together with the deﬁnition of the basis functions in (6.64), this ensures
that the edges–and therefore the tangential components of the basis functions–
always are directed from lower to higher global and local node numbers.
Next we rewrite the basis functions in (6.64) using ϕ1 = 1−ϕ2−ϕ3. The ba-
sis function can then be expressed as N e
i = Ni2(ϕ2, ϕ3)∇ϕ2+Ni3(ϕ2, ϕ3)∇ϕ3.
Noting that ∇ϕi, i = 1, 2, 3, are constant within each element, we can write
the local mass matrix of element e as
ij =
i · N e
j dx dy =
∇ϕk · ∇ϕl
NikNjl dx dy.
(6.65)
The integrals
e N e
ikN e
jl dx dy are scalar and can be computed through a
mapping to a reference element with nodes (0, 0), (1, 0), and (0, 1). The de-
terminant of this mapping is
det(Je) = (le
1 × le
2) · ˆz,
(6.66)
where le
i refers to edge i of element e. Depending on the order of the nodes,
det(Je) is equal to plus or minus 2Ae, where Ae is the area of element e. We
then get the following expression for M e
ij = | det(Je)|
∇ϕ2 · ∇ϕ2M 22
ij + ∇ϕ2 · ∇ϕ3M 23
ij + ∇ϕ3 · ∇ϕ3M 33
(6.67)
where M kl
ij are independent of the shape of the triangles and therefore can be
precomputed:
M kk
ij =
ϕ2=0
 1−ϕ2
ϕ3=0
NikNjk dϕ2 dϕ3,
(6.68)
M kl
ij =
ϕ2=0
 1−ϕ2
ϕ3=0
[NikNjl + NilNjk] dϕ2 dϕ3,
k ̸= l.
(6.69)
Here δkl denotes the Kronecker delta. With the basis functions in (6.64) we
get the following matrices Mkl:
M22 = 1
+3 +1 −1
+1 +1 −1
−1 −1 +1
⎦, M23 = 1
+3 +3 +1
+3 +3 −1
+1 −1 −1
⎦, M33 = 1
+1 +1 +1
+1 +3 +1
+1 +1 +1
(6.70)
The stiﬀness matrix is also computed using a mapping to the same refer-
ence element. First we use the chain rule:
∇× N e
i = ∇× (Ni2∇ϕ2 + Ni3∇ϕ3) = ∇Ni2 × ϕ2 + ∇Ni3 × ϕ3
= ∂Ni2
∇ϕ3 × ∇ϕ2 + ∂Ni3
∇ϕ2 × ∇ϕ3 =
det(Je)
∂Ni2
−∂Ni3
6.5 Vector Equations
Then we obtain
ij =
(∇× N e
i) · (∇× N e
j) dx dy
| det(Je)|2
∂Ni2
−∂Ni3
 ∂Nj2
−∂Nj3
dx dy
| det(J2)|
ϕ2=0
 1−ϕ2
ϕ3=0
∂Ni2
−∂Ni3
 ∂Nj2
−∂Nj3
dϕ2 dϕ3
| det(J2)|,
where S00 is independent of the shape of the element and can be precomputed:
S00 =
+2 −2 +2
−2 +2 −2
+2 −2 +2
(6.71)
% --------------------------------------------------------------
% Compute the stiffness and mass matrix for edge elements on
% a triangular grid
% --------------------------------------------------------------
function [M, S, el2ed] = edgeFEM2D(no2xy, el2no)
% Arguments:
no2xy = x- and y-coordinates of the nodes
el2no = node indices of the triangles
% Returns:
= Mass matrix
= Stiffness matrix
el2ed = a table that contain the three edge numbers related
to each element
% Sort the nodes of each element
el2no = sort(el2no);
% Assign a number to each edge in the grid and create el2ed
n1 = el2no([1 1 2],:);
n2 = el2no([2 3 3],:);
[ed2no,trash,el2ed] = unique([n1(:) n2(:)],’rows’);
el2ed = reshape(el2ed,3,size(el2no,2));
% Compute det(Jˆe), grad phi_2 and grad phi_3
e1 = no2xy(:,el2no(2,:)) - no2xy(:,el2no(1,:)); % 1st edge in
% all elements
e2 = no2xy(:,el2no(3,:)) - no2xy(:,el2no(1,:)); % 2nd edge in
% all elements
detJ = e1(1,:).*e2(2,:) - e1(2,:).*e2(1,:);
% det(Jˆe) for
% all elements
6 The Finite Element Method
g2 = [+e2(2,:)./detJ; -e2(1,:)./detJ];
% grad phi_2
g3 = [-e1(2,:)./detJ; +e1(1,:)./detJ];
% grad phi_3
% Define element shape independent matrices
m22 = [+3 +1 -1; +1 +1 -1; -1 -1 +1] / 12;
m23 = [+3 +3 +1; +3 +3 -1; +1 -1 -1] / 12;
m33 = [+1 +1 +1; +1 +3 +1; +1 +1 +1] / 12;
s00 = [+2 -2 +2; -2 +2 -2; +2 -2 +2];
% Compute local matrices and indices for all elements
mloc = m22(:) * (abs(detJ).*sum(g2.*g2)) + ...
m23(:) * (abs(detJ).*sum(g2.*g3)) + ...
m33(:) * (abs(detJ).*sum(g3.*g3));
sloc = s00(:) * abs(1./detJ);
rows = el2ed([1 2 3 1 2 3 1 2 3],:);
cols = el2ed([1 1 1 2 2 2 3 3 3],:);
% Assemble.
S = sparse(rows,cols,sloc);
M = sparse(rows,cols,mloc);
The presented MATLAB function assumes that the material parameters
are constant in the entire mesh. It also assumes homogeneous Neumann
boundary conditions, i.e., ˆn × ∇× E = 0, which corresponds to a perfectly
magnetic conducting (PMC) boundary. If we instead solved for the magnetic
ﬁeld H, we would have ˆn×∇×H = 0, which corresponds to a PEC boundary.
The function edgeFEM2D can easily be extended to treat problems where the
material parameters vary between elements, but are constant within each el-
ement, and problems with homogeneous Dirichlet boundary conditions. How-
ever, this is left as a computer exercise.
A function for plotting a solution, expressed as a (real) vector with coeﬃ-
cients, is given below. The ﬁeld is plotted on a ﬁner mesh than the mesh that
was used to compute the solution. The reason for this is to see how the ﬁeld
varies within, and on the interface between, elements. Arrows and color are
used to visualize the ﬁeld itself and its curl respectively.
% --------------------------------------------------------------
% Plot a 2D vector field described by edge elements
% --------------------------------------------------------------
function plotfield(no2xy, el2no, el2ed, sol)
% Arguments:
no2xy = x- and y-coordinates of the nodes
el2no = node indices for all triangles
el2ed = edge indices for all elements
= Coefficient vector (each entry in the vector
corresponds to one edge in the mesh)
% Returns:
6.5 Vector Equations
% Sort the nodes of each element
el2no = sort(el2no);
% Local coordinates for subgrid plotting
phi_1 = [4 3 2 1 0 3 2 1 0 2 1 0 1 0 0]’ / 4;
phi_2 = [0 1 2 3 4 0 1 2 3 0 1 2 0 1 0]’ / 4;
phi_3 = [0 0 0 0 0 1 1 1 1 2 2 2 3 3 4]’ / 4;
% Gradients of the simplex functions
% (constant within each element)
edge1 = no2xy(:,el2no(2,:)) - no2xy(:,el2no(1,:));
edge2 = no2xy(:,el2no(3,:)) - no2xy(:,el2no(1,:));
detJ = edge1(1,:).*edge2(2,:) - edge1(2,:).*edge2(1,:);
grad_phi_2x =
edge2(2,:)./ detJ;
grad_phi_2y = -edge2(1,:)./ detJ;
grad_phi_3x = -edge1(2,:)./ detJ;
grad_phi_3y =
edge1(1,:)./ detJ;
grad_phi_1x = 0 - grad_phi_2x - grad_phi_3x;
grad_phi_1y = 0 - grad_phi_2y - grad_phi_3y;
% Solution values associated to the 1st, 2nd, and
% 3rd edges in each element
sol1 = sol(el2ed(1,:)).’;
sol2 = sol(el2ed(2,:)).’;
sol3 = sol(el2ed(3,:)).’;
% Field values
Ex = phi_1 * ( grad_phi_2x.*sol1 + grad_phi_3x.*sol2) + ...
phi_2 * (-grad_phi_1x.*sol1 + grad_phi_3x.*sol3) + ...
phi_3 * (-grad_phi_1x.*sol2 - grad_phi_2x.*sol3);
Ey = phi_1 * ( grad_phi_2y.*sol1 + grad_phi_3y.*sol2) + ...
phi_2 * (-grad_phi_1y.*sol1 + grad_phi_3y.*sol3) + ...
phi_3 * (-grad_phi_1y.*sol2 - grad_phi_2y.*sol3);
Hz = (sol1 - sol2 + sol3)./detJ;
% Create subgrid
p1 = no2xy(:,el2no(1,:));
p2 = no2xy(:,el2no(2,:));
p3 = no2xy(:,el2no(3,:));
psub = kron(p1,phi_1’) + kron(p2,phi_2’) + kron(p3,phi_3’);
% Initiate plotting
ih = ishold;
ax = newplot;
6 The Finite Element Method
% Plot the curl of the field (constant within each element)
patch(’faces’,el2no’,’vertices’,no2xy’,’facevertexcdata’,Hz(:), ...
’facecolor’,get(ax,’defaultsurfacefacecolor’), ...
’edgecolor’,get(ax,’defaultsurfaceedgecolor’));
axis equal, hold on
% Plot the field itself as arrows
quiver(psub(1,:),psub(2,:),Ex(:)’,Ey(:)’,’k’);
% Plot the mesh
xy1 = no2xy(:,el2no(1,:));
xy2 = no2xy(:,el2no(2,:));
xy3 = no2xy(:,el2no(3,:));
xy = [xy1; xy2; xy3; xy1; NaN*xy1];
plot(xy(1:2:end),xy(2:2:end),’k’)
% Create a new colormap
mrz = max(abs(Hz(:)));
caxis([-mrz, mrz]);
c = (0:64)’/64; d = [c c ones(size(c))];
colormap([d ;1 1 1; d(end:-1:1,end:-1:1)]);
if ˜ih, hold off, end
We exploit this implementation to compute the eigenmodes H and eigen-
values k2 for a cavity resonator with a circular metal boundary of radius
a = 1 m. The solution satisﬁes the eigenvalue problem ∇× ∇× H = k2H
with boundary condition ˆn × ∇× H = 0, where H = ˆxHx(x, y) + ˆyHy(x, y).
A relatively coarse grid is used to compute the fundamental mode shown in
Figure 6.26. The numerical mode has ka = 2.4412, and this computed value
compares well with the analytical counterpart, i.e., the ﬁrst zero ka = 2.4049
of the Bessel function J0(ka). The next mode is degenerated, and analytically
it has ka = 3.8318, which corresponds to the ﬁrst zero of J1(ka). The two
numerically computed eigenmodes are shown in Figure 6.27, and they have
ka = 3.8831 and ka = 3.8846. The ten lowest eigenvalues are shown in Fig-
ure 6.28, where the crosses indicate the analytical solution and the circles the
numerical result. We note that there are no spurious modes, the multiplicity
of the lowest modes is correct, and the error for the higher-order modes is sur-
prisingly small. There are 48 zero eigenvalues and Nn = 49 nodes in the mesh,
which includes all the nodes on the boundary. The zero eigenvalues correspond
to modes H = ∇ψ, where the potentials ψ are diﬀerent linear combinations
of nodal basis functions ϕi. However, while there are 49 linearly independent
potentials ψ, there are only 48 linearly independent modes H = ∇ψ, since a
constant (but nonzero) ψ corresponds to zero magnetic ﬁeld.
6.5 Vector Equations
−0.8
−0.6
−0.4
−0.2
Fig. 6.26. The fundamental mode with ka = 2.4412, and this compares well with
the analytical counterpart ka = 2.4049.
−0.8
−0.6
−0.4
−0.2
−0.8
−0.6
−0.4
−0.2
Fig. 6.27. Two degenerate modes associated with the second-smallest ka = 3.8831
and ka = 3.8846, which compares well with the analytical counterpart ka = 3.8318.
mode [−]
ka [−]
Fig. 6.28. Nomalized eigenvalues ka for the lowest 10 eigenmodes: circles, numerical
result; and crosses, analytical values.
6 The Finite Element Method
6.5.8 Time-Dependent Problems
Now we consider a time evolution problem for the vector wave equation. Let
us choose a simple example with a lossless region (i.e., σ = 0) and metal
boundary conditions. There are no driving currents, and instead we excite the
problem with a nonzero initial ﬁeld. The problem can be stated as
µ∇× E
+ ϵ∂2E
∂t2 = 0
in S,
(6.72)
ˆn × E = 0
on L1,
(6.73)
E(r, t = 0) = E0(r )
in S,
(6.74)
∂E(r, t)
t=0 = 0
in S.
(6.75)
Besides the boundary condition (6.73) we need two initial conditions (6.74)
and (6.75), because the equation is of second order in time. The electric ﬁeld
is expanded in edge elements, and the coeﬃcients Ej are now time dependent:
E(r, t) =
Ej(t)N j(r ).
(6.76)
Equation (6.72) is tested by taking the scalar product with the weighting
function W i = N i(r ) and integrated (the ∇× µ−1∇×-term by parts) over
the computational domain.
So far, we have discretized in space but not in time. The result is a system
of coupled ordinary diﬀerential equations (ODE) for the expansion coeﬃcients
Sz(t) + c−2
0 M ∂2z(t)
= 0,
where S and M are given by (6.58)–(6.59). To solve this system of ODEs, we
can use either ﬁnite diﬀerences or ﬁnite elements in time. A ﬁrst attempt for
time-stepping might be the centered ﬁnite diﬀerence scheme
zn+1 −2zn + zn−1
= −(c0∆t)2 Szn,
(6.77)
where we need to specify z1 and z2 as initial conditions. This scheme is subject
to the time-step limitation discussed in Section 4.4.1, ∆t ≤2/ωmax. Yet it is
implicit, because the mass matrix M must be inverted at every time step.
zn+1 = 2zn −zn−1 −(c0∆t)2M−1Szn.
Thus, straightforward time-stepping for FEM has two drawbacks: it is
slow, because of the inversion, and the time-step is limited. There are two
ways to improve on this. One can be used if the mass matrix is suﬃciently
close to diagonal that it can be approximated by a diagonal matrix. This is
6.5 Vector Equations
known as “mass lumping” in mechanics and leads to explicit time-stepping.
Mass lumping works well for the edge elements on quadrilaterals. In fact, with
some additional lumping of the stiﬀness matrix, time-stepped edge elements
on rectangles are equivalent to the FDTD scheme. This solution gives a low
number of operations per time-step, but still the time-step is limited by the
CFL condition.
Mass lumping does not work for edge elements on triangles or tetrahedra,
and for these elements, one must invert a system of equations on each time
step. A much better method in this case is to apply a scheme that is even more
implicit, so that it is stable for arbitrarily large time steps. This is achieved
by averaging the stiﬀness term in time:
zn+1 −2zn + zn−1
= −(c0∆t)2 S
θzn+1 + (1 −2θ)zn + θzn−1
(6.78)
This scheme is stable for any time-step if θ ≥1/4. However, the scheme
becomes inaccurate if the time-step is long compared with the characteristic
time on which the solution evolves.
The time-stepping scheme in (6.78) was introduced in 1959 by New-
mark [49], and it is often referred to as the Newmark scheme. One interest-
ing feature of the Newmark scheme is that it reduces to the ﬁnite diﬀerence
scheme (6.77) when the implicitness parameter θ is zero. In fact, the Newmark
scheme can be viewed as a strict FEM scheme based on Galerkin’s method and
a piecewise linear expansion of the electric ﬁeld in time [61]. The implicitness
parameter enters through a linear combination of exact and trapezoidal inte-
gration applied to the weak form of the problem. Equation (6.78) is recovered
if we use the weights 1 −6θ and 6θ for the exact and trapezoidal integration,
respectively. This makes it possible to combine [60] ﬁnite diﬀerence schemes
(with explicit time-stepping) with FEM (with implicit time-stepping), and
moreover, it is feasible to construct relatively simple proofs of stability based
on von Neumann analysis. Since the lowest term in the error expansion is of
second order in ∆t for the FEM with Galerkin’s method, this also applies to
both (6.77) and (6.78).
Review Questions
6.5-1 Derive the Helmholtz equation from the system of ﬁrst-order equations,
i.e., dE/dx −ωµH = 0 and dH/dx + ωϵE = 0.
6.5-2 Why is the electric ﬁeld expanded in tent functions and the magnetic
ﬁeld in top-hat functions for the mixed 1D problem in Section 6.5.1?
6.5-3 Relate the FEM expressions for the system of ﬁrst-order equations
(dE/dx −ωµH = 0 and dH/dx + ωϵE = 0) to the corresponding ﬁnite-
diﬀerence approximations. Do you need to apply special techniques for a
one-to-one correspondence?
6.5-4 How do tent and top-hat functions relate to the integer and half-mesh
used for ﬁnite diﬀerence approximations?
6 The Finite Element Method
6.5-5 Describe the diﬀerences and similarities between the FEM for scalar
and vector equations.
6.5-6 Why are edge elements needed? Why are they called edge elements?
Why are they referred to as curl-conforming elements? List some of the
characteristic properties of edge elements.
6.5-7 What is the physical meaning of the degrees of freedom for a vector
ﬁeld expanded in terms of edge elements? How does this translate to an
electric ﬁeld that can be represented as the gradient of a scalar potential?
6.5-8 Derive the weak form of the vector Helmholtz equation, ∇× (µ−1∇×
E) −(ω2ϵ −jωσ)E = −jωJs, with some suitable boundary conditions.
6.5-9 Write down the explicit expressions for the edge elements on a rectangle.
6.5-10 Describe the functions (with respect to x, y, and z) that are used for
the x-components of the electric and magnetic ﬁelds, respectively, on a
grid of brick elements.
6.5-11 Derive explicit expressions for the matrix elements in (6.60) and (6.61)
by evaluating the integrals by hand. Use the expressions in (6.51) for the
basis and test functions.
6.5-12 How many static modes are supported by the mesh in Figure 6.21 and
why? How many static modes are supported by the mesh in Figure 6.26?
6.5-13 Write down explicit expressions for edge elements on triangles in terms
of (a) polar coordinates and (b) nodal basis functions.
6.5-14 Show that for triangles, the tangential component of a given basis
function is constant along one edge and zero along the other edges of the
element. Does this also hold for rectangular edge elements?
6.5-15 Are there any advantages of the implicit Newmark scheme compared
to explicit time-stepping schemes?
6.6 Magnetostatics and Eddy Current Problems
Two-dimensional scalar calculations can be applied to problems involving
magnetic materials and eddy currents. Eddy current calculations are gen-
erally made by applying the low-frequency approximation, which consists in
ignoring the displacement current and setting ϵ0 = 0. Roughly speaking, the
low-frequency approximation works when the geometrical dimensions of the
computational domain are much smaller than a wavelength λ = c/f.
The low-frequency equations are usually solved by introducing the mag-
netic vector potential A, such that B = ∇× A. The advantage of this is that
the condition of solenoidal magnetic ﬁeld ∇· B = 0 is automatically satis-
ﬁed. Note, however, that although the magnetic ﬁeld is uniquely determined,
the vector potential is not; any gradient of a scalar potential can be added
to A without changing the magnetic ﬁeld B. The electric ﬁeld is given by
E = −∂A/∂t −∇φ. With this representation for B and E, Faraday’s law is
automatically satisﬁed. Amp`ere’s law gives
6.6 Magnetostatics and Eddy Current Problems
∇× 1
µ∇× A + σ
∂t + ∇φ
= Js,
(6.79)
where Js is an imposed source current, usually representing currents in coils,
and σE = −σ(∂A/∂t + ∇φ) is the conduction current. As a consequence of
the low-frequency approximation ϵ0 = 0, both sides of Poisson’s equation, ∇·
(ϵ∇φ) = −ρ, vanish, and therefore, the electrostatic potential is undetermined
in the low-frequency approximation.
6.6.1 2D Formulation
For 2D problems with currents ﬂowing in the z-direction and variations only
in the x- and y-directions, the potentials can be chosen in a simple way:
A = Az(x, y)ˆz,
φ = 0.
(6.80)
Then the magnetic ﬁeld is B = ∇Az × ˆz and the current density is
µ∇Az × ˆz
= −ˆz∇· 1
µ∇Az.
(6.81)
If the time-dependence is harmonic ∝exp(jωt), the z-component of Amp`ere’s
law gives
−∇· 1
µ∇Az + jωσAz = Js
(6.82)
which is a complex, scalar Helmholtz equation. The boundary condition of the
continuous normal component for B is fulﬁlled if Az is continuous. The bound-
ary condition of continuous ˆn × H = ˆn × µ−1(∇Az × ˆz) = −ˆzµ−1∂Az/∂n
requires continuity of µ−1∂Az/∂n.
In microwave terminology, the 2D formulation in (6.80) and (6.82) cor-
responds to TM polarization. This 2D problem is readily solved using nodal
elements for the vector potential Az, and we have discussed the techniques
for this in Section 6.3.
6.6.2 A 2D Application Problem
As a practical application, we consider the 2D electromagnet shown in Fig-
ure 6.29. The magnetic circuit consists of an iron core (µr = 4000) shaped
like the letter C and two rectangular copper conductors. The left and right
copper conductors carry source currents +Js
z and −Js
z, respectively.
First we solve the static problem −∇· (µ−1
r ∇Az) = µ0Js
z. We have dis-
cussed all the techniques necessary for this in Section 6.3, and they have been
implemented in a user-friendly way in the MATLAB toolbox pdetool. The
computed magnetic ﬂux lines (equipotential lines for Az) are shown in Fig-
ure 6.29. Note the almost uniform distribution of magnetic ﬂux lines in the
6 The Finite Element Method
−0.015
−0.01
−0.005
0.005
0.01
0.015
−0.015
−0.01
−0.005
0.005
0.01
0.015
x [m]
y [m]
Fig. 6.29. Magnetic ﬂux density lines in the static case are shown by thin lines,
and the geometry is shown by thick lines.
core. There is also some leakage of ﬂux, especially in the vicinity of the air
gap where signiﬁcant fringing occurs.
For ﬁnite frequencies, we solve (6.82). The resulting magnetic ﬂux lines for
the frequencies f = 1.0 Hz and f = 10 Hz are shown in Figure 6.30. We have
used the conductivities σFe = 107 S/m for the iron core and σCu = 5.8·107 S/m
for the copper conductors. The electrical conductivity reduces the penetration
of the magnetic ﬁeld into the iron (and to a lesser extent, into the copper)
as the frequency increases. This is called the skin eﬀect. The skin depth,
over which the magnetic ﬁeld decays by 1/e, can be found from (6.82) as
δ = 1/√πfµσ. At f = 1.0 Hz the skin depths are 2.5 mm and 66 mm for iron
and copper, respectively. For f = 10 Hz the skin depths are 0.8 mm (rather
thin!) in iron and 21 mm in copper.
Time variation, i.e., nonzero frequency, introduces eddy currents in the
conducting regions. One can see in Figure 6.30 that the eddy currents in the
iron core squeeze the magnetic ﬂux to the inner surface of the iron core. This
is where the circumference traversed by the ﬁeld lines is the smallest. Note
that despite the localization of the ﬂux to one side of the iron, the ﬁeld lines
spread out evenly in the air gap. Here, the ﬂux density (density of contours)
is almost uniform. The reason for this is that the air gap gives the dominant
contribution to the magnetic reluctance.
Contour lines for the total power dissipation density Pt = σ|Jt
z|2 at f = 1.0
Hz and f = 10 Hz are shown in Figure 6.31. The total current Jt
z is the sum of
the source current Js
z and the eddy current Je
z. The source current is prescribed
as a constant value in the copper region. In practice, the copper region would
most likely consist of a single thin wire wound many turns around the core.
6.6 Magnetostatics and Eddy Current Problems
−0.015
−0.01
−0.005
0.005
0.01
0.015
−0.015
−0.01
−0.005
0.005
0.01
0.015
x [m]
y [m]
−0.015
−0.01
−0.005
0.005
0.01
0.015
−0.015
−0.01
−0.005
0.005
0.01
0.015
x [m]
y [m]
Fig. 6.30. Magnetic ﬂux density lines at f = 1.0 Hz and f = 10 Hz are shown to
the left and the right, respectively.
This can be modeled as a uniform current distribution. The eddy currents are
computed from the vector potential, Je
z = σEz = −jωσAz.
At power frequencies, eddy currents reduce the regions where the mag-
netic ﬁeld penetrates the iron to very thin layers. To avoid this one can use
laminations that prevent eddy currents from ﬂowing in certain directions. For
the 2D electromagnet shown here, laminations in the xy-plane will inhibit the
eddy currents completely. We reiterate that the 2D eddy current problem is
well handled by nodal elements. This technique is extensively described in the
textbook of Silvester and Ferrari [70].
−0.015
−0.01
−0.005
0.005
0.01
0.015
−0.015
−0.01
−0.005
0.005
0.01
0.015
x [m]
y [m]
−0.015
−0.01
−0.005
0.005
0.01
0.015
−0.015
−0.01
−0.005
0.005
0.01
0.015
x [m]
y [m]
Fig. 6.31. Contour lines for the power dissipation density at f = 1.0 Hz (left) and
f = 10.0 Hz (right).
6 The Finite Element Method
6.6.3 3D Eddy Current Calculations
Here, we will give a brief introduction to eddy current calculations in three
dimensions. This is a complex subject, so the discussion will be kept general,
and leave out many details. Several diﬀerent formulations are used for solving
the low-frequency equation (6.79). Before proceeding to discuss two of these
formulations, we note that the divergence of Amp`ere’s law with ϵ0 = 0 shows
that the current density has zero divergence. This must hold, both for the
coil current Js and the conduction currents −σ(jωA + ∇φ). Therefore, the
low-frequency problem can be stated as
∇× 1
µ∇× A + σ
∂t + ∇φ
= Js,
(6.83)
∇· σ
∂t + ∇φ
= 0,
∇· Js = 0,
We outline how this set of equations can be solved using nodal and edge
elements.
Solution by Nodal Elements for the Components of A
The method based on nodal elements for the components of the vector po-
tential is still used in commercial codes, despite some known diﬃculties. The
ﬁrst diﬃculty comes from the fact that the null-space solutions for the curl-
curl operator cannot be represented by divergence-conforming elements. This
problem can be cured by removing the null-space (which does not contribute
to the magnetic ﬁeld anyway) by adding a so-called penalty term −∇µ−1∇·A
to Amp`ere’s law, so that the set of equations becomes
∇× 1
µ∇× A −∇1
µ∇· A + σ
∂t + ∇φ
= Js,
(6.84)
∇· σ
∂t + ∇φ
= 0.
(6.85)
This procedure makes the diﬀerential operator in (6.84) similar to a Laplacian
and removes highly oscillatory, spurious solutions. The system (6.84)–(6.85)
can be solved using Galerkin’s method, where (6.84) is tested with the basis
functions for A (vectorial nodal elements) and (6.85) is tested with the basis
functions for φ (scalar nodal elements).
Taking the divergence of (6.84) and using (6.85), we get
∇2 1
µ∇· A = 0.
(6.86)
Thus, µ−1∇· A satisﬁes the Laplace equation, and if ∇· A vanishes on the
boundaries, this implies ∇·A = 0 everywhere. Therefore, the penalty term in
6.6 Magnetostatics and Eddy Current Problems
(6.84) is numerically zero, so that it does not change Amp`ere’s law. (Actually,
it is nonzero for the spurious solutions, which are removed by adding the
penalty term.) One of the advantages of the penalty term is that it changes the
conditioning of the matrix by removing small eigenvalues, and therefore makes
the system easier to solve by an iterative solver. Note that for this formulation,
the condition of zero divergence for the conduction currents (6.85) is essential
and cannot be left out. This condition is not a gauge condition, but it indirectly
enforces ∇· A = 0, which is called the Coulomb gauge.
It turns out that this method works well, except at edges and corners
where the magnetic permeability µ changes. At such edges, the magnetic
ﬁeld is unbounded, and the penalty formulation is not accurate. Recent work
suggests that this problem can be overcome by removing the penalty term
locally around such singularities.
Solution by Edge Elements for A
Edge elements work better for low-frequency problems, but the procedures
for an eﬃcient implementation are not simple [43]. As a ﬁrst attempt, one
can set the scalar potential to zero and expand the solution of (6.83) in edge
elements. If the frequency is zero, one must note that the curl-curl operator
has a large null-space. For the lowest-order edge elements, this null-space
consists of A = ∇U, where U is a piecewise linear scalar variable. Therefore,
(6.83) can be solved only if Js has no projection on this null-space. One can
ensure this, either by representing Js as the curl of a current potential, or by
subtracting the gradient of a scalar U from Js and imposing the condition
⟨∇¯U, Js −∇U⟩= 0 for all piecewise linear test functions ¯U. This procedure
works excellently for static problems. It does not suﬀer from the accuracy
problems that occur for the nodal representation at edges where µ has jumps.
If one straightforwardly extends this procedure to ﬁnite frequency, the
matrix becomes ill-conditioned, and iterative solvers converge very slowly. The
cure for this is a somewhat surprising procedure, which consists in introducing
a scalar potential φ and not prescribing a gauge condition. Instead of a gauge
condition, one requires the divergence of the conduction current to be zero,
so that the system of equations is
∇× 1
µ∇× A + σ (jωA + ∇φ) = Js,
(6.87)
∇· σ (jωA + ∇φ) = 0.
(6.88)
Note that this system of equations is degenerate, because the second equation
is the divergence of the ﬁrst (assuming ∇· Js = 0). Moreover, φ occurs only
in the combination jωA + ∇φ = −E, so that any change of A and φ that
leaves this combination unchanged is permitted. This is precisely a gauge
transformation, which does not change the physical ﬁelds. Thus, the system
(6.87)–(6.88) permits any gauge, and the method is referred to as the ungauged
6 The Finite Element Method
formulation. Of course, the indeterminacy of the solutions implied by gauge
transformations means that the matrix is singular. However, iterative methods
work also for singular matrices, provided that the right-hand side is consistent,
that is, has no projection on the null-space.
The ungauged formulation greatly reduces the number of iterations for
Krylov solvers (to which an introduction is given in Appendices A and B).
The ungauged formulation can be viewed as a form of preconditioner for the
curl-curl equation, and it improves the complex eigenvalue spectrum of the
operator. The advantage of the edge elements over the nodal element formula-
tion with a penalty term is that the edge elements give good approximations
also at corners of magnetic materials.
Eddy current calculations are more frequently carried out on hexahedral
meshes than on tetrahedral ones. One reason for this is that eddy current
problems often involve currents in thin layers, within the skin depth δ =
(2/ωµσ)1/2 of conductor surfaces. The skin depth is typically in the millimeter
to centimeter range, which is small compared to the global dimensions of a
motor, generator, or transformer. Therefore, high resolution is required in
the direction normal to the surface of a conductor, whereas the resolution
requirements in the perpendicular direction can be much less demanding.
This anisotropy is easier to achieve on a hexahedral mesh than a tetrahedral
one. Another anisotropy can be introduced by laminations, and these are
much easier to treat on a hexahedral mesh, which can be aligned with the
laminations.
Review Questions
6.6-1 What is the low-frequency approximation and when is it applicable?
6.6-2 Consider a 2D low-frequency problem in the xy-plane. Use Maxwell’s
equations to derive a partial diﬀerential equation for the z-component
of the vector potential. How can boundary conditions for the ﬁelds be
formulated in terms of the vector potential?
6.6-3 Is the vector potential uniquely deﬁned? If not, what conditions do you
need to uniquely determine the vector potential?
6.6-4 Why is the electrostatic potential undetermined in the low-frequency
approximation?
6.6-5 What is the diﬀerence between the magnetostatic problem and the low-
frequency eddy current problem? Give examples of how the characteristic
features of the solution change. Does this inﬂuence the choice of numerical
algorithms and discretizations?
6.6-6 What is a penalty term and why is it used?
6.6-7 Mention some drawbacks associated with representing the components
of the vector potential in a 3D eddy current problem by nodal elements.
6.6-8 Explain what a gauge transformation is.
6.6-9 Under what conditions is it possible to solve a system of linear equations
where the system matrix is singular?
6.7 Variational Methods
6.7 Variational Methods
The FEM can also be introduced as a variational method. Variational methods
are intimately related with essential conservation laws of the system, and can
give valuable insights into the application problem.
As an illustration, we study an example of electrostatics in a source free
region. Here D = ϵE and E = −∇φ, where φ is the electric potential. The
natural choice of a variational quantity is the electrostatic ﬁeld energy:
W[φ] = 1
E · DdV = 1
ϵ|∇φ|2dV.
(6.89)
The potential for which (6.89) gives the energy does not have to be the true
solution, but it must fulﬁll the boundary conditions. The remarkable thing is
that the true potential distribution, satisfying the boundary conditions and
Poisson’s equation −∇· (ϵ∇φ) = 0, is exactly the function that minimizes
(6.89); i.e., it gives the smallest electrostatic energy of all allowed φ.
To show this, let φ0 be the potential that minimizes (6.89). Then, change
the potential slightly by adding a perturbation δφ, and compute the electro-
static energy for the perturbed potential φ = φ0 + δφ:
W[φ0 + δφ] = W[φ0] +
ϵ∇δφ · ∇φ0dV + O
(δφ)2
(6.90)
When δφ is small, the higher-order terms O((δφ)2) can be dropped. When the
electrostatic energy W has a minimum, the ﬁrst variation δW = W[φ0 +δφ]−
W[φ0] must be zero. After an integration by parts, (6.90) gives the following
condition for the energy to be stationary:
δW =
δφ [−∇· (ϵ∇φ0)] dV = 0.
(6.91)
If this is to hold for all perturbations δφ, the potential φ0 must satisfy −∇·
(ϵ∇φ0) = 0 everywhere in V ; i.e., the diﬀerential equation of electrostatics in
a source-free region is satisﬁed.
6.7.1 Relation Between Linear Diﬀerential Equations and
Quadratic Forms
In more general terms, the solution f of a self-adjoint linear diﬀerential equa-
tion L[f] = s in a domain Ωcorresponds to a stationary point for the quadratic
form
I[f] = 1
2⟨f, L[f]⟩−⟨f, s⟩.
(6.92)
We use the scalar product ⟨f, g⟩=
Ωfg dΩ, where f and g are real functions.
An operator L is self-adjoint if ⟨g, L[f]⟩= ⟨f, L[g]⟩for all f and g. The factor 1
6 The Finite Element Method
in the ﬁrst term of (6.92) is needed in order to produce the correct diﬀerential
equation, because the ﬁrst term in I is quadratic, while the second is linear.
Now let δf be a small variation of f. We will consider variations only up
to linear order in δf. We let δI denote the ﬁrst-order variation of I[f] when
f →f + δf and say that I[f] is stationary if
δI = 0, ∀δf.
(6.93)
Since f represents a minimum, the rate of change of I at f must be zero. Let
us expand I[f + δf] in powers of δf:
I[f + δf] = 1
2⟨f + δf, L[f + δf]⟩−⟨f + δf, s⟩
2⟨f, L[f]⟩−⟨f, s⟩
2⟨δf, L[f]⟩+ 1
2⟨f, L[δf]⟩−⟨δf, s⟩
2⟨δf, L[δf]⟩
= I[f] + δI + O((δf)2).
(6.94)
The ﬁrst variation is the part that is linear in δf, that is,
δI = 1
2⟨δf, L[f]⟩+ 1
2⟨f, L[δf]⟩−⟨δf, s⟩.
In order for I[f] to be stationary, the ﬁrst variation must vanish:
δI = 1
2(⟨δf, L[f]⟩+ ⟨f, L[δf]⟩) −⟨δf, s⟩= 0,
∀δf.
(6.95)
Now L is self-adjoint, i.e., ⟨f, L[δf]⟩= ⟨L[f], δf⟩, so the condition for I sta-
tionary becomes ⟨δf, L[f]⟩−⟨δf, s⟩= ⟨δf, L[f] −s⟩= 0. Thus, for every
admissible variation δf we have
⟨δf, L[f] −s⟩=
δf(L[f] −s)dΩ= 0.
(6.96)
Since δf is an arbitrary function, this requires that the residual r = L[f] −s
vanish everywhere in Ω; that is, that the diﬀerential equation L[f] = s be
satisﬁed.
The discussion above shows that we can solve the diﬀerential equation
L[f] = s by ﬁnding the function f that makes I[f] stationary. Often, I rep-
resents the energy, and the solution of the diﬀerential equation is the one
that minimizes the energy. The electrostatics problem we just discussed is an
example of this.
6.7 Variational Methods
A 1D Example
To illustrate some features of the variational method, we study a simple ex-
ample in one dimension. Let L[f] = −f ′′ and s = x2 with the boundary
conditions f(0) = f(1) = 0. We make a guess for the solution f containing
only two parameters a and b. The function f(x) = ax(1−x)3 +bx2(1−x) sat-
isﬁes the boundary conditions for arbitrary a and b. We seek the combination
of a and b such that the diﬀerential equation is satisﬁed as well as possible. If
it is not possible to ﬁnd an exact solution, we want the “best” combination
of a and b.
This can be done by computing the quadratic form I and ﬁnding its
stationary point. Since the operator L[f] is self-adjoint, it corresponds to
a quadratic form given by I[f] = 1
2⟨f, L[f]⟩−⟨f, s⟩, that is,
I[f] = −a
140 −b
30 + 1
3a2
35 + 2b2
(6.97)
I is a quadratic function in the parameters a and b, and Figure 6.32 shows
level contours for the quadratic form I with respect to these parameters.
−0.2
−0.1
−0.1
a [−]
b [−]
Fig. 6.32. Level contours for the quadratic form I. The stationary point is shown
by the dot labeled A, and this combination of a and b solves −f ′′ = x2. B and C are
not stationary points, and they do not solve the diﬀerential equation.
There is a global minimum for I indicated by the dot labeled A in Fig-
ure 6.32. To ﬁnd the values of a and b for this minimum we set the gradient
of I equal to zero:
6 The Finite Element Method
∂a = −1
140 + 3 a
35 = 0
(6.98)
∂b = −1
30 + 2 b
15 = 0
(6.99)
which gives the solution a = 1/12 and b = 1/4. The corresponding solution
f(x) = x(1 −x3)/12 indeed solves −f ′′ = x2, and it is shown in Figure 6.33
by the solid curve labeled A. If the basis functions had been chosen in a less
clever way, so that the true solution could not be constructed, the variational
approach would have given the “best” approximation of f(x).
−0.01
0.01
0.02
0.03
0.04
0.05
0.06
x [−]
f [−]
Fig. 6.33. The function solving −f ′′ = x2 is shown by the solid curve labeled A.
The two other functions labeled B and C do not satisfy the diﬀerential equation.
Let us see what happens if we change the values of a and b away from the
minimum A in Figure 6.32, e.g., to the points B and C. The new combinations
of a and b and their values of I are shown in Table 6.7 together with the
correct solution. The functions f corresponding to B and C are also shown in
Figure 6.33.
Label
I[f]
1/12 1/4 -4.46
1/7 1/5 -4.15
-1/7 3/8 -1.23
Table 6.7. Three diﬀerent combinations of the parameters. The true solution is
labeled A.
6.7 Variational Methods
6.7.2 Rayleigh–Ritz Method
The variational formulation gives a procedure, the Rayleigh–Ritz method, for
ﬁnding approximate solutions of self-adjoint linear equations. It consists of
the following steps:
Approximate f by an expansion in a ﬁnite set of basis (or trial) functions
ϕi, i = 1, 2, . . . , N:
f(r ) =
fiϕi(r ).
(6.100)
Evaluate the quadratic variational form I as a function of the expansion
coeﬃcients
I(f1, f2, . . . , fN) = I[f] = 1
2⟨f, L[f]⟩−⟨f, s⟩
fifj⟨ϕi, L[ϕj]⟩−
fi⟨ϕi, s⟩
Lijfifj −
sifi,
(6.101)
where Lij = ⟨ϕi, L[ϕj]⟩and si = ⟨ϕi, s⟩. Note that the “matrix” L is
symmetric, Lij = Lji, because the operator L is self-adjoint.
Determine the expansion coeﬃcients fi by demanding that I be stationary
with respect to all the coeﬃcients:
0 = ∂I
Lkjfj + 1
Likfi −sk =
Lkifi −sk.
(6.102)
Equation (6.102) is a linear symmetric N ×N system Lf = s for the expansion
coeﬃcients.
6.7.3 Galerkin’s Method
Galerkin’s method is intimately connected to the variational formulation. In
fact, the Rayleigh–Ritz formulation (6.102) leads to Galerkin’s method for
self-adjoint systems. Using the deﬁnitions of the matrix elements Lki and sk,
we have from (6.102)
Lkifi −sk =
⟨ϕk, L[fiϕi]⟩−⟨ϕk, s⟩
= ⟨ϕk, L[
fiϕi] −s⟩= ⟨ϕk, L[f] −s⟩
ϕk(L[f] −s) dΩ= 0.
(6.103)
6 The Finite Element Method
This is Galerkin’s method for solving L[f] = s, since the weighting functions
are equal to the basis functions. It is also the same as the variational condition
(6.96), but the previously arbitrary weighting function δf for the residual
r = L[f] −s is now restricted to lie in the space of the basis functions. This
shows that Galerkin’s method can be derived from variational calculus.
We stress some important facts:
For self-adjoint diﬀerential equations, the Rayleigh–Ritz and Galerkin
methods are equivalent.
The Galerkin method can be used also for non-self-adjoint problems where
no variational principle can be found.
In the more general Petrov–Galerkin method, the weighting functions wi
are diﬀerent from the basis functions ϕi.
6.7.4 A Variational Method for Maxwell’s Equations
Maxwell’s equations can be put in variational form in a few diﬀerent ways.
One way is to apply the general prescription (6.92) to the lossless self-adjoint
curl-curl equation
∇× µ−1∇× E + ϵ∂2E/∂t2 = −∂J/∂t,
(6.104)
integrate both in space and time, and ignore the boundary terms. This gives
the quadratic form
 ⎛
2µ|∇× E|2 −ϵ


+ E · ∂J
⎠dV dt.
(6.105)
For a small variation of the electric ﬁeld E →E + δE, the ﬁrst-order change
of L is
δL =
  1
µ∇× E · ∇× δE −ϵ∂E
∂t · ∂δE
+ ∂J
∂t · δE
dV dt,
and an integration by parts (ignoring boundary terms) gives
δL =
 
∇× 1
µ∇× E + ϵ∂2E
∂t2 + ∂J
· δE dV dt.
Thus, if E is a solution of Maxwell’s equations, then δL = 0 for any δE, which
means that L[E] is stationary. Conversely, to make L stationary, i.e., δL = 0
for an arbitrary δE, the curl-curl equation (6.104) must be satisﬁed.
A slight reformulation of the variational principle that is more directly
related to physical quantities uses the vector and scalar potentials as inde-
pendent variables. The ﬁelds are represented as
6.7 Variational Methods
B = ∇× A,
E = −∇φ −∂A
∂t .
(6.106)
The quadratic form is the magnetic minus the electric energy, plus terms
involving the sources, integrated in space and time:
 B2
2µ −A · J −ϵE2
+ ρφ
dV dt.
(6.107)
We get Maxwell’s equations by setting the ﬁrst variation of L with respect to
φ and A to zero. For φ →φ+δφ, integration by parts gives the ﬁrst variation
δL =
(ϵ∇δφ · E + ρδφ) dV dt
(ρ −∇· ϵE) δφ dV dt = 0.
(6.108)
Therefore, δL = 0 for all δφ if and only if Poisson’s equation ∇· ϵE = ρ is
satisﬁed.
For A →A + δA the same procedure gives
δL =
  1
µ∇× δA · B + ∂δA
· ϵE −δA · J
dV dt
 
∇× B
µ −∂
∂tϵE −J
· δA dV dt = 0.
(6.109)
Therefore, δL = 0 for all δA if and only if Amp`ere’s law ∇× (B/µ) =
∂(ϵE)/∂t+J holds everywhere. Faraday’s law and ∇·B = 0 are automatically
satisﬁed because of the potential representation (6.106).
Review Questions
6.7-1 Motivate why variational methods are useful.
6.7-2 What are a quadratic form, functional, variation, and stationary point?
6.7-3 List and describe the steps involved in the Rayleigh–Ritz method.
6.7-4 What conditions must be fulﬁlled for the Rayleigh–Ritz formulation and
Galerkin’s method to be equivalent? Given such conditions, show that they
are equivalent.
6.7-5 For Maxwell’s equations, write down the quadratic form in terms of
the electric ﬁeld and show that a solution that makes the quadratic form
stationary satisﬁes Maxwell’s equations.
6.7-6 Repeat the previous problem when the quadratic form is expressed
in terms of the potentials. Provide a physical interpretation of the con-
stituents of the quadratic form.
6 The Finite Element Method
Summary
The FEM is in short:
To solve L[f] = s, divide the solution region into elements and expand
the sought solution f in local basis functions f(r ) = N
i=1 fiφi(r ).
Make the residual r = L[f] −s orthogonal to N weighting functions
wi, i = 1, 2, . . . , N (the method of weighted residuals).
Galerkin’s method wi = φi is a popular choice for the weighting functions.
Other choices, i.e., wi ̸= φi, are referred to as Petrov–Galerkin, and some
possibilities are collocation wi = δ(r −ri), least squares wi = L[φi], and
least square stabilized Galerkin wi = φi + cL[φi], where the parameter c
is optimized.
In one dimension with uniform meshes and f in piecewise linear elements,
Galerkin’s method gives
dx2 →fi+1 −2fi + fi−1
f →fi+1 + 4fi + fi−1
where lumping (which in this case is obtained by trapezoidal integration)
gives f →fi; i.e., the ﬁnite diﬀerence approximation is recovered for the
Helmholtz equation in one dimension.
For the Helmholtz scalar equation in 2D, we can use a continuous linear
approximation of the solution f on a mesh of triangles. The expansion
f(r) ≈
i fiϕi(r) is then used to represent the solution, where ϕi is a
piecewise linear basis function with ϕi(ri) = 1 and ϕi(rj) = 0 when i ̸= j.
The FEM formulation typically involves matrix entries of the type
−∇2 →Sij =
∇ϕi · ∇ϕj dS,
1 →Mij =
ϕiϕj dS.
By terminology borrowed from mechanics, S is referred to as the stiﬀness
matrix and M as the mass matrix.
Adaptivity can often restore nominal convergence for singular problems.
Mixed elements for a system of coupled ﬁrst-order diﬀerential equations
∂x = ωµH,
∂x = −ωϵE,
are treated with E expanded in piecewise linear functions (connected with
integer mesh) and H expanded in piecewise constants (connected with half
mesh). This gives
Ei+1 −Ei
= ωµHi+ 1
Hi+ 1
2 −Hi−1
= −ωϵ
3Ei + 1
6(Ei−1 + Ei+1)
6.7 Variational Methods
where the term ωϵE can be lumped by the trapezoidal rule
 xi+1
f(x)dx ≈
(h/2)[f(xi) + f(xi+1)]; i.e., we have (4Ei + Ei−1 + Ei+1)/6 →Ei.
Edge elements N i have continuous tangential components, which makes
the curl of the solution square integrable. They are often referred to as
curl-conforming elements, and some distinguishing features are:
the basis functions N i have unit tangential components along one edge
and zero along all the other edges,
spurious solutions and spectral contamination are avoided,
the null-space of the curl operator is correctly represented.
The formulation for the vector Helmholtz equation involves terms of the
type
∇× ∇× →Sij =
(∇× N i) · (∇× N j) dS,
1 →Mij =
N i · N j dS.
Time-dependent problems use time-dependent coeﬃcients for the spatial
expansion of the ﬁeld. The wave equation Sz(t) + c−2
0 M ∂2z(t)/∂t2 = 0
can be time-stepped with the ﬁnite diﬀerence scheme
zn+1 −2zn + zn−1
= −(c0∆t)2 Szn,
which requires a suﬃciently small time-step ∆t for stability. An even more
implicit scheme, derived by averaging the stiﬀness term in time, gives un-
conditional stability (provided that the implicitness parameter θ is greater
than or equal to 1/4):
zn+1 −2zn + zn−1
= −(c0∆t)2 S
θzn+1 + (1 −2θ)zn + θzn−1
The solution f of a self-adjoint linear diﬀerential equation L[f] = s is a
stationary point of the quadratic form
I[f] = 1
2⟨f, L[f]⟩−⟨f, s⟩.
A self-adjoint operator L satisﬁes ⟨f, L[g]⟩= ⟨g, L[f]⟩for all f and g.
The Rayleigh–Ritz method solves L[f] = s by expanding f in global ba-
sis functions f(r ) ≈N
i=1 fiφi(r ) and evaluating the quadratic form
I(f1, f2, . . . , fN). Coeﬃcients are determined by ∂I/∂fi = 0 for all i =
1, 2, . . . , N. For self-adjoint problems, the equivalent Galerkin formulation
is to make the residual r = L[f] −s orthogonal to all the basis functions,
i.e.,
(L[f] −s)ϕidΩ= 0 for all i.
Problems
P.6-1 Derive the ﬁnite element approximation of the 1D Helmholtz equation
−(d2/dx2 + k2)f = 0 for piecewise linear elements on a nonequidistant
mesh and show for the system matrix
6 The Finite Element Method
Aij = Sij −k2Mij
that the elements are
Si,i−1 = −
xi −xi−1
Mi,i−1 = xi −xi−1
Si,i =
xi+1 −xi
xi −xi−1
Mi,i = xi+1 −xi−1
Si,i+1 = −
xi+1 −xi
Mi,i+1 = xi+1 −xi
Show that for a uniform mesh with cell size h this gives a discretiza-
tion that is similar to the ﬁnite diﬀerence approximation, except that
the mass term is weighted between adjacent nodes. Substitute a complex
exponential f = exp(jkx) and show that the FEM approximation gives
FEM = 24 sin2(kh/2)/[2 + 4 cos2(kh/2)] ≈k2(1 + k2h2/12), so that the
FEM eigenvalue converges from above. Note that the error has the same
magnitude, but the opposite sign, as the FD approximation (3.18). Based
on this, can you ﬁnd a three-point discretized operator that gives an error
O(k4h4)?
P.6-2 Consider a scattering problem where both the geometry and the sources
are independent of the z-coordinate. Derive the weak formulation for the
Helmholtz equation
µ∇Esc
−ω2ϵEsc
z = 0,
where Esc
is the scattered electric ﬁeld from a metal cylinder. Impose
the boundary condition Esc
= −Einc
on the surface of the scatterer,
where Einc
is the incident wave. The ﬁnite element mesh discretizes the
region around the metal cylinder and extends some distance from the
scatterer. At the exterior boundary of the mesh we apply the absorbing
boundary condition ˆn · ∇Esc
z = −jkEsc
z to mimic an open region prob-
lem. What criteria must be fulﬁlled for this boundary condition to be
accurate? To answer this question, it is useful to consider a plane wave
z = E0 exp(−jk · r) that is incident on such an absorbing boundary.
P.6-3 A rectangular ﬁnite element occupies the region deﬁned by xa ≤x ≤xb
and ya ≤y ≤yb. This element has four nodes and, also, four nodal basis
functions:
1 = xb −x
xb −xa
· yb −y
yb −ya
2 = x −xa
xb −xa
· yb −y
yb −ya
3 = x −xa
xb −xa
· y −ya
yb −ya
4 = xb −x
xb −xa
· y −ya
yb −ya
Is it feasible to apply the FEM to a mesh where such a rectangular ﬁnite
element is connected to a triangular ﬁnite element so that the two share
one edge? Suggest a situation in which it can be useful to discretize the
solution domain with both triangles and rectangles.
6.7 Variational Methods
P.6-4 In addition to the organization of nodes and elements, it is often nec-
essary to include various materials and boundary conditions in the dis-
crete representation of a FEM problem. The data structures discussed
in Section 6.3.2 can also be extended to deal with postprocessing steps,
e.g., integration along a contour. Discuss how the representation of the
geometrical information relating to materials, boundary conditions, and
postprocessed quantities could be implemented in a FEM computer pro-
gram.
P.6-5 Consider the electrostatic problem −∇· (ϵ0∇φ) = 0. For a solution
computed by the FEM with linear triangles, the potential is piecewise
linear, and the corresponding electric ﬁeld is piecewise constant. Given
such a FEM solution, evaluate Qt =
Lt D · ˆn dl applied to a single
triangle, where Lt is the boundary of the triangle. Evaluate also Qe =
Le D·ˆn dl applied to a single edge shared by two triangles, where Le is an
integration contour enclosing the edge. Interpret the derived expressions
for Qt and Qe. How do these quantities depend on the variation in the
solution as compared to the cell size? Since the charge density is supposed
to be zero, the dissatisfaction of Gauss’s law could be used as a physics
based indication of inaccuracy. Note that Qt and Qe do not give a bound
on the actual error in the solution φ. Bounds on the error in the solution
can be derived mathematically [27], but such a derivation is beyond the
scope of this book.
P.6-6 In Section 6.6, we computed the vector potential A = Az(x, y)ˆz on
an unstructured mesh of triangles. Given this solution, we used a routine
that plots equipotential lines of the vector potential to visualize the ﬂux
lines of the magnetic ﬂux density. Show that a contour where Az(x, y) is
constant is also a ﬂux line for the magnetic ﬂux density B.
P.6-7 Eliminate the magnetic ﬁeld from (6.40) and (6.41). Compare this result
with the FEM applied to the Helmholtz equation in one dimension,
+ ω2ϵEz = 0,
where the element matrices have been evaluated with either exact or trape-
zoidal integration. How do these methods relate to ﬁnite diﬀerences ap-
plied to the 1D Helmholtz equation?
P.6-8 Consider a scattering problem where both the geometry and the sources
are independent of the z-coordinate. Here, we solve for the electric ﬁeld
E(x, y) = ˆx Ex(x, y) + ˆy Ey(x, y), and the computational mesh is trun-
cated at a constant radius R from the origin. The scatterer is located at
the origin. Modify the matrix entries (6.48) and the vector entries (6.50)
to impose the Sommerfeld radiation condition
ˆr × (∇× E) + jkˆr × (ˆr × E) = ˆr × (∇× Einc) + jkˆr × (ˆr × Einc)
combined with an external source that produces the prespeciﬁed inci-
dent ﬁeld Einc. What boundary condition should be imposed on a metal
6 The Finite Element Method
scatterer? Which criteria must be fulﬁlled for the Sommerfeld radiation
condition to be accurate?
P.6-9 A rectangular ﬁnite element occupies the region deﬁned by xe
a ≤x ≤xe
and ye
a ≤y ≤ye
b. This element has four nodes and also four nodal basis
functions:
1 = xe
b −x
b −xea
· ye
b −y
b −yea
2 = x −xe
b −xea
· ye
b −y
b −yea
3 = x −xe
b −xea
· y −ye
b −yea
4 = xe
b −x
b −xea
· y −ye
b −yea
Consider an electric potential φ = 4
j=1 φjϕe
j on this rectangle. Show that
the gradient of this potential falls into the space of the edge elements;
i.e., the equality E = −∇φ is satisﬁed pointwise. In other words, given
arbitrary values for φj, show that there exist values for Ej such that
j=1 EjN e
j = −4
j=1 φj∇ϕe
j for every point inside the rectangle.
P.6-10 Prove that (6.78) is stable for an arbitrary time-step when θ ≥1/4
by carrying out a von Neumann stability analysis for eigenmodes of Sz =
λMz, where λ = ω2/c2.
P.6-11 How are solutions of the type E = −∇φ treated by (6.72), (6.77), and
(6.78)?
P.6-12 What is the natural choice of a variational quantity for the steady elec-
tric current problem −∇·(σ∇φ) = 0 that was treated in Section 6.3? How
are boundary conditions treated in this case? Give a physical interpreta-
tion of the minimization of this functional and derive its ﬁrst variation.
Computer Projects
C.6-1 Write a program that automatically generates a triangulation for a
rectangular domain. You can use a structured mesh of rectangles and
divide the rectangular elements on the diagonal to create the triangles.
C.6-2 Modify the program in Section 6.3.3 so that you can compute the ca-
pacitance of a capacitor with an inhomogeneous dielectric. Let the spatial
dependence of the permittivity be a prespeciﬁed function of your own
choice. Note that if the triangles are small compared to the variations
in the permittivity, you can sample ϵ at the center of each element and
assume it to be constant inside that element. How does the error scale
with the cell size given such an assumption? Will this have any impact
on the order of convergence for the ﬁnal algorithm? Can you improve the
performance of such a method?
C.6-3 Rewrite (6.55)–(6.56) in terms of the z-component of the magnetic ﬁeld.
Use the program in Section 6.3.3 as a starting point for an implementation
that solves this eigenvalue problem on a mesh of triangles. Will the static
eigenvalue(s) ω = 0 be reproduced by this formulation? Explain your
ﬁndings.
6.7 Variational Methods
C.6-4 Implement a FEM that solves ∇×∇×E = k2E by means of rectangular
ﬁnite elements. Apply your program to a 2D cavity with metal boundary
and compute the eigenfrequencies. Find a test case for which the analytical
result is known and perform a convergence study of the lowest eigenvalues.
What order of convergence do you expect? Is this order of convergence
reproduced by your program?
C.6-5 Modify the FEM function edgeFEM2D (in Section 6.5.7) so that it can
treat problems where the material parameters are diﬀerent in diﬀerent
cells. Add two extra input arguments, which are vectors with relative elec-
tric permittivity and magnetic permeability for all elements. Also modify
the function such that homogeneous Dirichlet boundary conditions can be
used. Can the same plot routine be used after these changes?
The Method of Moments
In this chapter we introduce the integral formulation of both electrostatics
and the complete Maxwell system. In general, the electromagnetics commu-
nity refers to the integral formulation as the method of moments (MoM),
for reasons that will be explained later. In mathematics, the MoM is often
referred to as the boundary element method (BEM).
We will reformulate electrostatics, for which we have previously used Pois-
son’s and Laplace’s equations, as an integral equation. In the following sec-
tions on scattering problems, we will rewrite the full Maxwell equations as
an integral equation for currents on the surfaces of conductors, and apply
this formulation to a scattering problem. The scattered electric ﬁeld can be
expressed in terms of surface currents on conductors. The condition that the
tangential electric ﬁeld vanishes on conductor surfaces then gives an integral
equation from which we can compute the surface currents. For the interested
reader, more information on the MoM can be found in, e.g., [51, 82, 19].
7.1 Integral Formulation of Electrostatics
In electrostatics, the electric potential φ is determined from the sources ac-
cording to Poisson’s equation
∇2φ = −ρ
(7.1)
This is the diﬀerential equation formulation. The solution of Poisson’s equa-
tion in free space can be constructed by superposing the contributions φ(r) =
q/4πϵ0|r −r′| from point charges q = ρvdV at locations r′:
φ(r) =
ρ(r′)dV ′
4πϵ0|r −r′|.
(7.2)
If the potential φ is known, (7.2) can be seen as an integral equation for
the charge density ρ. The integral formulation is suited for problems such

# Bondeson《Computational Electromagnetics》第3章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 36-52 of 231 (231 total)

---

## Finite Differences

3 Finite Diﬀerences
f(x + h) −2f(x) + f(x −h)
= f ′′(x) + O(h2).
(3.4)
We note that the O(h2) errors in (3.2)–(3.3) are achieved only if the solution
is suﬃciently regular (for example, if f ′′(x), f ′′′(x), etc are bounded).
3.1 A 2D Capacitance Problem
As an application of ﬁnite diﬀerences to an electrostatic potential problem,
we will compute the capacitance of a coaxial transmission line. The two-
dimensional (2D) geometry shown in Figure 3.1 consists of an inner conductor
of rectangular cross section a × b, placed coaxially with an outer waveguide
of rectangular cross section c × d.
Fig. 3.1. Geometry of the coaxial transmission line.
In the vacuum region between the inner and outer conductors, the elec-
trostatic potential φ satisﬁes Laplace’s equation
∇2φ = ∂2φ
∂x2 + ∂2φ
∂y2 = 0,
(3.5)
where the potential is constant on the conductors. We let φ1 denote the value
for the potential on the inner conductor, and correspondingly, the potential
on the outer conductor is denoted by φ2.
We assume that the geometry can be ﬁtted on a grid of squares. (It is pos-
sible to use nonsquare, and even nonuniform, ﬁnite diﬀerence grids. However,
ﬁnite diﬀerence grids are often uniform and square, and we will not go beyond
that. Nonuniformities are better treated by ﬁnite elements.)
We use the square grid
3.1 A 2D Capacitance Problem
xi = ih, i = . . . , −1, 0, 1, 2, . . . ,
yj = jh, j = . . . , −1, 0, 1, 2, . . . ,
illustrated in Figure 3.2, and introduce the potential at the grid points
fi,j = φ(ih, jh)
as unknowns.
(i, j)
(i, j+1)
(i+1, j)
(i-1, j)
(i, j-1)
Fig. 3.2. 2D ﬁnite diﬀerence grid.
Then the discretized Laplace’s equation becomes
∂x2 + ∂2φ
∂y2 ≈fi−1,j + fi+1,j + fi,j−1 + fi,j+1 −4fi,j
= 0.
(3.6)
Equation (3.6) applies for all internal points (xi, yj) on the grid. As boundary
conditions, we let φ take the value φ2 = 0 V on the outer conductor (fi,j = 0
for all the points that fall on the outer conductor) and φ1 = 1 V on the inner
conductor (fi,j = 1 for all the points that fall on the inner conductor). We will
compute the charge per unit length Q from the solution. Then the capacitance
per unit length is C = Q/V = Q, since the voltage across the capacitor is
V = 1 V.
3.1.1 Iterative Solution of Laplace’s Equation
Here, we introduce some straightforward (but rather old) methods, known as
Jacobi and Gauss–Seidel iteration, to solve the discretized Laplace’s equation
(3.6). These methods do not require that the system of linear equations be
formed and stored explicitly. Thus, only the solution itself must be stored
in the computer memory, which allows us to solve larger problems given the
3 Finite Diﬀerences
amount of memory available on the computer at hand. An iterative method
starts with an initial guess for the solution fi,j at all internal grid points, e.g.,
fi,j = 0 or some other arbitrarily chosen numbers. The iterative method then
updates these values until we reach a converged solution that satisﬁes the
ﬁnite diﬀerence approximation (3.6) at all internal grid points. Obviously, fi,j
is set to its prescribed values on the boundaries, where the solution is known
from the boundary conditions, and these values are kept ﬁxed.
The Jacobi iteration can be motivated by rewriting (3.6) as
fi,j = 1
4 (fi−1,j + fi+1,j + fi,j−1 + fi,j+1) ,
which states that at every grid point, the potential is the average of the
potential at the four nearest neighbors. The Jacobi scheme uses this as the
prescription for assigning new values
f (n+1)
f (n)
i−1,j + f (n)
i+1,j + f (n)
i,j−1 + f (n)
i,j+1
where superscripts denote the iteration count. This scheme gives very slow
convergence, but one can do better by simple modiﬁcations. One modiﬁca-
tion is the so-called Gauss–Seidel iteration, where the “old” values of f are
immediately overwritten by new ones, as soon as they are computed. If f is
updated in the order of increasing i and j, the Gauss–Seidel scheme is
f (n+1)
f (n+1)
i−1,j + f (n)
i+1,j + f (n+1)
i,j−1 + f (n)
i,j+1
The other improvement is “overrelaxation,” which means that the correction
in going from iteration level n to n+1 is multiplied by a relaxation parameter
f (n+1)
= f (n)
i,j + R
f (n+1)
i−1,j + f (n)
i+1,j + f (n+1)
i,j−1 + f (n)
i,j+1
−f (n)
(3.7)
R > 1 greatly improves the convergence, but for stability reasons R must be
less than 2. For the Laplace’s equation, a heuristic estimate for the optimal
value of R varies with the number of grid points in one direction, N, as
Ropt = 2 −c/N,
where c is an N-independent number that depends on the geometry [6].
3.1.2 Computing the Capacitance
We now have all the elements needed to compute the capacitance between
the two conductors. The computation can be broken down into the following
parts:
3.1 A 2D Capacitance Problem
points. For the particular problem here, we can exploit the symmetry
and compute only on the upper right quarter, to reduce the number of
unknowns. (Around a line of symmetry with a constant i, we enforce the
symmetry by fi+n,j = fi−n,j, where n is a positive integer. Symmetry
lines with a constant j are treated analogously)
tor and f = V = 1 on the inner conductor.
the potential is computed from Laplace’s equation.
the potential.
inner conductor Q can be computed from Gauss’s law
Q = ϵ0
E · ˆn dl = −ϵ0
 ∂φ
∂ndl,
(3.8)
where the closed integration contour encircles the inner conductor.
iterating.
olate the result to zero cell size.
3.1.3 MATLAB: Capacitance of Coaxial Cable
We will compute the capacitance for the geometry shown in Figure 3.1 with
a = b = 1 cm and c = d = 2 cm. Here, the capacitance is expressed in
terms of the charge on the inner conductor. As an alternative to the Gauss–
Seidel iteration, we could use MATLAB routines for solving linear systems of
equations. However, we take this opportunity to introduce a simple, yet quite
eﬃcient, iterative method. More advanced iterative methods are discussed in
Appendices A and B.
The following MATLAB function computes the capacitance following the
outline in Section 3.1.2.
% --------------------------------------------------------------
% Compute capacitance per unit length of
% a coaxial pair of rectangles
% --------------------------------------------------------------
function cap = capacitor(a, b, c, d, n, tol, rel)
% Arguments:
width of inner conductor
= height of inner conductor
width of outer conductor
= height of outer conductor
3 Finite Diﬀerences
= number of points in the x-direction (horizontal)
tol = relative tolerance for capacitance
rel = relaxation parameter
(a good choice is 2-c/n, where c is about pi)
% Returns:
cap = capacitance per unit length [pF/m]
% Make grids
= 0.5*c/n;
% Grid size
na = round(0.5*a/h);
% Number of segments on ’a’
= linspace(0,0.5*c,n+1);
% Grid points along x-axis
= round(0.5*d/h);
% Number of segments on ’d’
mb = round(0.5*b/h);
% Number of segments on ’b’
= linspace(0,0.5*d,m+1);
% Grid points along y-axis
% Initialize potential and mask array
f = zeros(n+1,m+1);
% 2D-array with solution
mask = ones(n+1,m+1)*rel;
% 2D-array with relaxation
% [mask(i,j) = 0 implies
unchanged f(i,j)]
for i = 1:na+1
for j = 1:mb+1
mask(i,j) = 0;
f(i,j)
= 1;
% Gauss Seidel iteration
oldcap = 0;
for iter = 1:1000
% Maximum number of iterations
f = seidel(f,mask,n,m);
% Perform Gauss-Seidel iteration
cap = gauss(n,m,h,f);
% Compute the capacitance
if (abs(cap-oldcap)/cap<tol)
break
% Stop if change in capacitance
% is sufficiently small
else
oldcap = cap;
% Contiue until converged
str = sprintf(’Number of iterations = %4i’,iter); disp(str)
% --------------------------------------------------------------
% Make one Seidel iteration
% --------------------------------------------------------------
function f = seidel(f, mask, n, m)
% Arguments:
= 2D-array with solution
mask = 2D-array with relaxation
3.1 A 2D Capacitance Problem
= number of points in the x-direction (horizontal)
= number of points in the y-direction (vertical)
% Returns:
= 2D-array with solution after Gauss-Seidel iteration
% Gauss seidel iteration
for i = 2:n
for j = 2:m
f(i,j) = f(i,j) + mask(i,j)* ...
(0.25*(
f(i-1,j) + f(i+1,j) ...
+ f(i,j-1) + f(i,j+1)) - f(i,j));
% Symmetry on left boundary i-1 -> i+1
i = 1;
for j = 2:m
f(i,j) = f(i,j) + mask(i,j)* ...
(0.25*(
f(i+1,j) + f(i+1,j) ...
+ f(i,j-1) + f(i,j+1)) - f(i,j));
% Symmetry on lower boundary j-1 -> j+1
j = 1;
for i = 2:n
f(i,j) = f(i,j) + mask(i,j)* ...
(0.25*(
f(i-1,j) + f(i+1,j) ...
+ f(i,j+1) + f(i,j+1)) - f(i,j));
% --------------------------------------------------------------
% Compute capacitance from the potential
% --------------------------------------------------------------
function cap = gauss(n, m, h, f)
% Arguments:
= number of points in the x-direction (horizontal)
= number of points in the y-direction (vertical)
= cell size
= 2D-array with solution
% Returns:
cap = capacitance per unit length [pF/m]
q = 0;
for i = 1:n
q = q + (f(i,m)+f(i+1,m))*0.5; % integrate along upper boundary
3 Finite Diﬀerences
for j = 1:m
q = q + (f(n,j)+f(n,j+1))*0.5; % integrate along right boundary
cap = q*4;
% 4 quadrants
cap = cap*8.854187;
% epsilon0*1e12 gives answer in pF/m
Table 3.1 shows some results of calling the function with diﬀerent grid
sizes and a = b = 1 cm, c = d = 2 cm, the tolerance 10−9, and the relaxation
paramter 1.9. When the results are plotted against hp, they appear to fall
on a straight line for p ≈1.5. If we had the patience to wait for longer
runs, write more eﬃcient MATLAB code, or program the calculation in a
language such as Fortran or C, the resolution could be improved, and we
would ﬁnd that the asymptotic order of convergence is 4/3. An important
thing to learn from this example is that the convergence is slower than the
normal O(h2) convergence for the diﬀerence formula (3.4). In fact, the O(h2)
convergence occurs only when the solution is suﬃciently regular, and the
decreased order of convergence in this example is the result of the singular
behavior of the solution at the corners of the inner conductor. As will be
shown in Chapter 7, the potential at such a “reentrant” corner, where the
angle in the solution region is 270o, varies as the distance r to the corner to
the power 2/3. This implies that the electric ﬁeld is singular, E ∝r−1/3. With
the computed results in Table 3.1, and assuming that the order of convergence
is 1.5, a second- or higher-order polynomial ﬁt of the data versus h1.5 gives
an extrapolated answer for the capacitance as C = 90.6 pF/m.
n [-]
h [m] C [pF/m]
0.1000 92.09715
0.0500 91.18849
0.0333 90.94575
0.0250 90.83912
0.0200 90.78080
Table 3.1. Capacitance vs. cell size for ﬁnite diﬀerence solution.
Appendix A contains some information on more eﬃcient algorithms for
the solution of linear systems. Many of these algorithms are also available in
MATLAB. Thus, we could use some of these routines to solve larger problems
and get better resolution. Another way to improve the convergence when the
solution is singular is adaptive grid reﬁnement. However, this is more easily
done with ﬁnite elements than with ﬁnite diﬀerences.
Review Questions
3.1-1 What are the constituents of a ﬁnite-diﬀerence method?
3.2 Finite Diﬀerence Derivatives of Complex Exponentials
3.1-2 Derive (3.2)–(3.4) given (3.1). When are O(h2) errors achieved?
3.1-3 Use (3.4) to deduce (3.6). What will the corresponding discrete Laplace
operator look like in three dimensions?
3.1-4 How can a known potential distribution be used to compute the capac-
itance of a coaxial cable?
3.1-5 What is the order of convergence for the problem shown in Figure 3.1?
3.2 Finite Diﬀerence Derivatives of Complex
Exponentials
For Laplace’s equation, straightforward application of ﬁnite diﬀerences works
well. However, when derivatives of odd order are involved, a diﬀerent technique
is required to get good results. To get some insight into this, it is instructive
to consider how the diﬀerence approximations (3.2)–(3.4) act on complex ex-
ponentials. Two reasons for studying complex exponentials are these:
All functions can be decomposed as sums over complex exponentials (the
Fourier transform).
The complex exponentials exp(jkx), where j is the imaginary unit and k is
the wavenumber (k = 2π/λ, where λ is the wavelength) are eigenfunctions
of the derivative operator, (∂/∂x) exp(jkx) = jk exp(jkx).
We consider a uniform 1D grid with grid points
xi = ih,
i = . . . , −2, −1, 0, 1, 2, . . . ,
and we will examine the diﬀerence approximations by evaluating them for
complex exponentials, f = exp(jkx). The wavenumbers can be restricted so
that |kh| ≤π. This is because, when any harmonic function is represented
on a grid of points with spacing h, one can always shift kh by any integer
multiple of 2π so that kh ∈[−π, π], without changing the value of f at any
grid point.
Derivative operators can be deﬁned as
Dx = f ′/f,
Dxx = f ′′/f,
(3.9)
and for f = exp(jkx), the exact analytical results are
Dx = jk , Dxx = D2
x = −k2.
(3.10)
3.2.1 First-Order Derivative
For the ﬁrst derivative, the numerical diﬀerence formulas applied to f(x) =
ejkx give the results shown as functions of kh in Figure 3.3:
3 Finite Diﬀerences
Equation (3.2), derivative across two cells, f ′ on the “integer grid”:
Dx = f ′(xi)
f(xi) = f(xi + h) −f(xi −h)
2h f(xi)
= ejkh −e−jkh
h sin kh. (3.11)
This gives an eﬀective numerical wavenumber
ktwo-cell
= sin kh
1 −k2h2
+ · · ·
(3.12)
The leading term in the expansion is correct, and the relative error is
−k2h2/6, so the error increases with decreasing wavelength.
Equation (3.3), derivative across one cell, f ′ on the half-grid:
Dx =
f ′(xi+ 1
f(xi+ 1
2 ) = f(xi + h) −f(xi)
hf(xi + h/2)
= ejkh/2 −e−jkh/2
= 2j
h sin kh
(3.13)
This gives an approximation with a smaller error
kstaggered
h sin kh
2 = k
1 −k2h2
+ · · ·
(3.14)
Such an arrangement, where the ﬁrst derivative is computed on the half-
grid, is called staggered grids.
The diﬀerence formula across two cells gives very poor results when kh >
π/2. In particular, for kh = π, it gives the rather strange result f ′ = 0 and
ktwo-cell
= 0. Figure 3.4 illustrates how this comes about: when kh = π, f(xi)
jumps between plus and minus the same value between neighboring points.
Points at the distance of 2h have the same value of f, and therefore f ′ = 0 at
every point on the integer grid. Thus, the most rapidly oscillating function has
the derivative equal to zero everywhere on the integer grid. Notice also that
the two-cell diﬀerence formula gives ∂ktwo-cell
/∂k < 0 for π/2 < kh < π. In a
wave-propagation problem, this would have the consequence that the group
velocity (vg = ∂ω/∂k) changes sign, and signals propagate in the wrong
direction.
The expression (3.14) for the more compact derivative on the staggered
grid is clearly better at the shortest wavelength kh = π. Although the result
kstaggered
h = 2 for kh = π is not very accurate, it is at least nonzero and this
arrangement gives no negative group velocity.
3.2.2 Spurious Solutions and Staggered Grids
The inability of the diﬀerence formula across two cells to see rapid oscillations
can cause diﬃculties known as “spurious modes.” By spurious modes we mean
solutions of a discretized equation that do not correspond to an analytic (or
“physical”) solution.
3.2 Finite Diﬀerence Derivatives of Complex Exponentials
kh/π [−]
knumh/π [−]
analytic
staggered
non−staggered
Fig. 3.3. Finite diﬀerence approximation of wavenumber from ﬁrst derivative k =
−jf ′/f, with f = exp(jkx) for staggered and nonstaggered grids. Note the bad
approximation of the nonstaggered form when kh →π.
As an example to illustrate how spurious solutions can appear, we take
the ﬁrst-order equation
f ′ = jλf,
x > 0,
f(0) = 1
If this is discretized on a uniform grid of step length h, the nonstaggered
approximation using (3.2) is
f(xi+1) −f(xi−1)
= jλf(xi).
(3.15)
This will have solutions of the form exp(jkx), and the wavenumber can be de-
termined from (3.12): ktwo-cell
= λ. Evidently, this gives two solutions, because
ktwo−cell
(kh) is nonmonotonic as shown by Figure 3.3. One is an acceptable
approximation k1h = arcsin(λh), but the other is a bad approximation, or
“spurious mode,” having kspurioush = π −arcsin(λh) = π −k1h. If λh is
small, this branch for kh approaches π, so that the solution resembles the
most rapidly oscillating function shown in Figure 3.4, even though the correct
solution varies slowly on the scale of the grid. If we use the approximation on
a staggered grid, with the stencil
f(xi+1) −f(xi)
= jλ
2 [f(xi+1) + f(xi)] ,
(3.16)
such spurious solutions do not occur (however, the behavior is not entirely
physical for this representation either when kh →π).
3 Finite Diﬀerences
−1.5
−0.5
x/h [−]
f [−]
df/dx = 0
Fig. 3.4. Fastest oscillating function on a ﬁnite diﬀerence grid with kh = π has the
derivative equal to zero at all integer points on the grid.
The more compact formula (3.3) for the ﬁrst derivative gives an approxima-
tion with acceptable behavior even when kh = π. The derivative is computed
on the half-grid, and the grids are staggered. A 3D generalization of this is
used in the FDTD method for Maxwell’s equations, as will be described in
Chapter 5. Equations (3.11) and (3.13) show that the relative error of the
discretized derivatives is proportional to k2h2.
3.2.3 Second-Order Derivative
For the second derivative, the standard diﬀerence formula (3.4) applied to
f(x) = ejkx gives
Dxx = ejkh −2 + e−jkh
= −4
h2 sin2 kh
(3.17)
Therefore,
num = (kstaggered
)2 = 4
h2 sin2 kh
2 = k2
1 −k2h2
+ · · ·
(3.18)
which is illustrated in Figure 3.5.
The result is only moderately accurate at the shortest wavelength (−Dxx =
4/h2, when kh = π, to be compared with the analytic result π2/h2). But
at least −Dxx grows monotonically with k, so this approximation does not
introduce spurious solutions. To achieve 1% accuracy in computed frequencies
3.2 Finite Diﬀerence Derivatives of Complex Exponentials
kh/π [−]
(knumh/π)2 [−]
analytic
discretized
Fig. 3.5. Finite diﬀerence approximation of k2 = −f ′′/f, with f = exp(jkx) ana-
lytically and with standard three-point diﬀerence formula.
(which means 2% accuracy in Dxx), one needs k2h2 < 0.24, or 13 grid points
per wavelength. If we consider the problem of calculating the ﬁelds from a
mobile telephone, at 900 MHz with λ = 33 cm, in a car of length 5 m, we
see that the number of cells in one direction required to get 1% phase (or
frequency) error is at least 13 × 5/0.33 ≈200. Evidently, a 3D computation
for mobile phones in cars requires several million cells. We emphasize the
absolute error will accumulate as the wave propagates. When the wave has
propagated 15 wavelengths with 1% relative phase error, the absolute phase
error is 15 · 360/100 = 54 degrees.
Review Questions
3.2-1 Why is it useful to study ﬁnite diﬀerence derivatives of complex expo-
nentials?
3.2-2 Why is the wavenumber restricted by |kh| ≤π on a grid with cell size
3.2-3 Derive the results in (3.12) and (3.14). Establish a value for kh when
the ﬁrst two terms in the expansions give 0.5% error of the numerical
wavenumber. Repeat this analysis for (3.18).
3.2-4 What is a staggered grid and why is it useful?
3.2-5 What is a spurious solution? Can such solutions be avoided? Give an
example of a situation where spurious solutions occur and explain why
they exist under the given circumstances.
3 Finite Diﬀerences
3.2-6 Can the ﬁnite diﬀerence approximation of Dxx be expressed in terms
of a ﬁnite diﬀerence approximation of Dx? Which approximation do you
choose for the ﬁrst-order derivative?
Summary
Derivatives can be approximated by diﬀerences between neighboring points
on a grid. A so-called uniform grid uses a constant grid point spacing h;
i.e., the grid points are given by xn+i = xn + ih, where i is an integer.
The ﬁrst-order derivative of a function f on a staggered grid (evaluated
at the midpoint (xi+1 + xi)/2) is
i+1/2 ≈fi+1 −fi
and that across two cells (evaluated at the center grid point xi) is
i ≈fi+1 −fi−1
The second-order derivative (evaluated at the center grid point xi) is
f ′′
i ≈fi+1 −2fi + fi−1
The discretized Laplacian operator is
∇2f = ∂2f
∂x2 + ∂2f
∂y2 ≈fi−1,j + fi+1,j + fi,j−1 + fi,j+1 −4fi,j
Two iterative procedures for solving Laplace’s equation are Jacobi and
Gauss–Seidel iteration. These can be accelerated with so-called overrelax-
ation.
Numerical derivatives acting on complex exponentials f(x) = exp(jkx) are
useful when analyzing ﬁnite diﬀerence schemes. The ﬁrst-order derivative
on a staggered grid gives
i+ 1
fi+ 1
fi+ 1
fi+1 −fi
= 2j
h sin
First-order derivatives across two cells with no staggering should be
avoided, since
fi+1 −fi−1
h sin (kh) ,
which is nonmonotonic and gives a zero derivative for solutions that vary
on the scale of the grid, i.e., kh →π.
The second-order derivative gives
f ′′
fi+1 −2fi + fi−1
= −4
h2 sin2
3.2 Finite Diﬀerence Derivatives of Complex Exponentials
Problems
P.3-1 Use the technique in Section 3.1.1 to solve the Laplace’s equation at
the midpoint of a square 3 × 3 grid where the potential is known on the
boundary. How does the solution depend on the cell size?
P.3-2 Show that if the grid is nonuniform, the ﬁnite diﬀerence approximation
of the second-order derivative is
f ′′(xi) ≈
xi+1 −xi−1
 fi+1 −fi
xi+1 −xi
−fi −fi−1
xi −xi−1
Derive the leading error term for this ﬁnite diﬀerence approximation. A
nonuniform grid implies that xi+1 −xi does not have to be equal to xi −
xi−1. Discuss when nonuniform grids can be useful for computations.
P.3-3 Derive a ﬁnite diﬀerence expression for f ′(0) in terms of f(0), f(h), and
f(2h) that has an O(h2) error.
P.3-4 For a problem with the grid points xi = ih, where i = 0, 1, 2, . . ., de-
rive a ﬁnite diﬀerence approximation of the Neumann boundary condition
f ′(0) = 0 by the use of a “ghost” grid point x−1 = −h (outside the com-
putational domain) such that the error is O(h2).
P.3-5 The capacitance can also be computed from C = 2W/V 2, where W is
the electrostatic energy and V the potential diﬀerence between the two
conductors of the capacitor. Write down an expression for W in terms of
the electrostatic potential distribution and suggest a method for comput-
ing W given the ﬁnite diﬀerence solution to an electrostatic problem.
P.3-6 Discuss how the derivative operators in (3.9) and (3.10) can be related
to, and useful in the context of, the one-way wave equation ∂f/∂x ±
(jω/c)f = 0, where c is the speed of the wave.
P.3-7 Show that the Helmholtz equation, ∂2f/∂x2 + (ω/c)2f = 0, can be
factorized into
∂x + jω
  ∂
∂x −jω
f = 0
and interpret the two factors of the Helmholtz operator. Discretize the
above factorized operator by ﬁnite diﬀerences (on staggered grids) and
multiply the two factors to derive the corresponding Helmholtz operator.
P.3-8 Discuss how the derivative operators in (3.9) and (3.10) can be re-
lated to, and useful in the context of, the wave equation ∂2f/∂x2 −
c−2∂2f/∂t2 = 0, where c is the speed of the wave f = f(x, t). Here,
f(x+ct) and f(x−ct) solve the wave equation, and the lines where x+ct
and x −ct are constant are referred to as characteristics.
P.3-9 Demonstrate that the Helmholtz equation is equivalent to the two cou-
pled equations ∂f/∂x + (jω/c)g = 0 and ∂g/∂x + (jω/c)f = 0. What is
the meaning of the new function g? How should the ﬁrst-order system of
coupled equations be discretized by ﬁnite diﬀerences?
P.3-10 Show that the analysis with complex exponentials applied to (3.16)
gives λ = (2/h) tan(kh/2), so that λ →∞as kh →π.
3 Finite Diﬀerences
P.3-11 The 1D Helmholtz equation for a transversal wave Ez in a homoge-
neous medium with losses reads
∂x2 + jωµσ −ω2µϵ
Ez = 0.
Use the ﬁnite diﬀerence approximation to discretize this equation. Calcu-
late and compare the dispersion relation of the continuous and the dis-
cretized problems. Does the discretized problem reproduce the physics for
well-resolved solutions? What happens for poorly resolved solutions? How
does the angular frequency ω and the material parameters µ, ϵ, and σ in-
ﬂuence the accuracy of the dispersion relation of the discretized equation?
Computer Projects
C.3-1 Write down the system of linear equations that results from the dis-
cretization of the capacitance problem shown in Figure 3.1. Let c = d =
3a = 3b and use a square grid with one grid point between the inner and
outer conductors. Let the potential be φ1 on the inner conductor and φ2
on the outer conductor. How are these boundary conditions incorporated
into the system of linear equations? Is it possible to use symmetries in the
solution of this problem?
Generalize the result so that it is possible to specify the number of points
between the inner and outer conductors. Write a computer program that
generates the system of linear equations Af = b in terms of a matrix A
and a vector b, where the solution vector f stores the potential values at
grid points between the inner and outer conductors.
C.3-2 Write a computer program that uses Jacobi and Gauss–Seidel itera-
tion to solve for the electrostatic potential on a square domain of side a.
Use the boundary conditions φ(x, 0) = φ(0, y) = 0, φ(x, a) = φ0 · (x/a)
and φ(a, y) = φ0 · (y/a), where φ0 is a constant. Study and compare the
convergence of the iterative methods in Section 3.1.1. Implement the over-
relaxation method and investigate how the value of R inﬂuences the con-
vergence. The analytical solution to this problem is φ(x, y) = φ0 ·(xy/a2).
C.3-3 Use the ﬁnite diﬀerence scheme to compute the capacitance for a coaxial
cable of two concentric circular cylinders with inner radius a and outer
radius b. For this case, the capacitance per unit length can be calculated
analytically, and it is 2πϵ/ ln(b/a). The circular boundaries do not fall on
grid points in a natural way, and one way to proceed is to approximate
these boundaries in some sense given the structured Cartesian grid. This
type of approximation is often referred to as the staircase approximation.
How does the error depend on the cell size h? Can you extrapolate the
results to zero cell size?
C.3-4 Try to reformulate the previous problem using polar coordinates (it can
be reduced to a 1D problem) to avoid the staircase approximation and
3.2 Finite Diﬀerence Derivatives of Complex Exponentials
use the ﬁnite diﬀerence scheme to solve for the capacitance. Determine
the order of convergence. Is it possible to extrapolate the capacitance to
zero cell size?
Eigenvalues
4.1 Maxwell’s Equations
Maxwell’s equations can be solved either in the time domain, by evolving
an initial condition in time, or in the frequency domain, assuming harmonic
exp(jωt) time dependence. In both cases, the application can be either a driven
system, where one seeks the response to a source, for instance an antenna, or
an eigenvalue calculation, where one seeks the natural oscillation frequencies
of the system.
In a linear, dispersion-free medium (i.e., ϵ and µ depend only on the coor-
dinate vector), Maxwell’s equations can be written as the single second-order
curl-curl equation (1.11) for the electric ﬁeld
−ϵ∂2E
∂t2 = ∇× 1
µ∇× E + ∂J
∂t .
(4.1)
In the absence of sources, J = 0, and with harmonic time dependence
exp(jωt), the curl-curl equation gives the following eigenvalue problem:
mϵEm = ∇× 1
µ∇× Em.
(4.2)
For nontrivial solutions (Em ̸= 0), ω2
m plays the role of an eigenvalue, and Em
is the corresponding eigenfunction, or eigenmode. (Sometimes the subindex
m is omitted in order to simplify the notation.) If the region Ω, where (4.2)
applies, is a closed cavity with a perfectly conducting boundary ∂Ω(i.e.,
ˆn × E = 0), the operator on the right-hand side, L ≡∇× µ−1∇×, is self-
adjoint, that is,
E1 · L[E2]dV =
E2 · L[E1]dV
(4.3)
for all vector ﬁelds E1 and E2 that satisfy the boundary conditions. This can
be shown using the vector identity

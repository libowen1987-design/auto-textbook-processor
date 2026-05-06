# Bondeson《Computational Electromagnetics》第2章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 29-35 of 231 (231 total)

---

## Convergence

2 Convergence
2.1 Extrapolation to Zero Cell Size
We will use a very simple problem, namely to calculate the electrostatic po-
tential on the symmetry axis of a uniformly charged square, to illustrate how
computed results can be extrapolated to zero cell size. The square is the region
−a < x < a, −a < y < a, z = 0, the surface charge density ρs(x, y) = ρs0
is constant, and we seek the potential φ at two points on the symmetry axis:
(0, 0, a) and (0, 0, 0). Using the symmetry, we can write the potential from
this charge distribution as
φ(0, 0, z) = ρs0
4πϵ0
x′=−a
y′=−a
(x′2 + y′2 + z2)1/2 = ρs0
I(z, a),
with
I(z, a) ≡
x′=0
y′=0
(x′2 + y′2 + z2)1/2 .
(2.1)
To do the integral I(z, a) numerically, we split the square into n2 smaller
squares of side h = a/n, and on each square, apply a simple integration rule
such as midpoint integration
 x+h
f(x)dx ≈hf
x + h
(2.2)
or Simpson’s rule
 x+h
f(x)dx ≈h
f(x) + 4f
x + h
+ f(x + h)
(2.3)
in two dimensions. The integration can be written as a MATLAB function.
% --------------------------------------------------------------
% Compute potential on symmetry axis of square plate
% --------------------------------------------------------------
function pot = integr(z, a, n, rule)
% Arguments:
= the height over the plate
= the side of the square
= the number of elements along each side of the plate
rule = a string ’midpoint’ or ’simpson’ that specifies
the integration rule
% Returns:
pot = the potential at the point (0,0,z)
= linspace(0, a, n+1);
= linspace(0, a, n+1);
= a/n;
zs = zˆ2;
2.1 Extrapolation to Zero Cell Size
if (strcmp(rule, ’midpoint’))
% Midpoint integration
xs(1:n) = (x(1:n) + h/2).ˆ2;
ys(1:n) = (y(1:n) + h/2).ˆ2;
[xxs, yys] = meshgrid(xs,ys);
int = sum(sum(1./sqrt(xxs + yys + zs)));
elseif (strcmp(rule, ’simpson’))
% Simpson’s rule
int = 0;
for i = 1:n
x1 = x(i)ˆ2; x2 = (x(i) + h/2)ˆ2; x3 = (x(i) + h)ˆ2;
y1(1:n) = y(1:n).ˆ2;
y2(1:n) = (y(1:n) + h/2).ˆ2;
y3(1:n) = (y(1:n) + h).ˆ2;
int = int + sum(
1./sqrt(x1+y1+zs) + 1./sqrt(x1+y3+zs) ...
+ 1./sqrt(x3+y1+zs) + 1./sqrt(x3+y3+zs)...
+ 4./sqrt(x2+y1+zs) + 4./sqrt(x2+y3+zs)...
+ 4./sqrt(x1+y2+zs) + 4./sqrt(x3+y2+zs)...
+ 16./sqrt(x2+y2+zs))/36;
else
error([’Only midpoint integration and Simpson’’s rule are ’ ...
’implemented’])
pot = int*hˆ2;
We call this function with z = a = 1 [integr(1,1,n,rule)] and diﬀerent
numbers of grid points n for rule = ’simpson’ and ’midpoint’, and then
extrapolate the results to zero cell size to get as accurate an answer as possible.
The ﬁrst step is to establish the order of convergence. Table 2.1 shows some
results of calling the function for diﬀerent cell sizes h = 1/n.
We can carry out the extrapolation using MATLAB routines, by collecting
the values of h, Imidp, and ISimpson in vectors. Plotting Imidp versus h to
some power p, we ﬁnd an almost straight line for p = 2, as shown in Figure
2.1. This indicates that the midpoint rule gives quadratic convergence, i.e.,
Imidp(h) = I0 + I2h2 + · · · where I0 is the extrapolated result. The term I2h2
in the Taylor expansion of Imidp is the dominant contribution to the error
2 Convergence
n [-]
h [m]
Imidp(1, 1) [m] ISimpson(1, 1) [m]
0.20000 0.79432 30171
0.79335 94378
0.14286 0.79385 04952
0.79335 92042
0.10000 0.79359 97873
0.79335 91413
0.06667 0.79346 60584
0.79335 91252
0.05000 0.79341 92684
0.79335 91225
Table 2.1. Integral I(1, 1) from numerical integration with diﬀerent cell sizes.
when h is suﬃciently small, and for such resolutions the higher-order terms
in the Taylor expansion can be neglected.
0.01
0.02
0.03
0.04
0.793
0.7935
0.794
0.7945
h2 [m2]
Imidp [m]
Fig. 2.1. Values of the integral I(1, 1) computed by the midpoint rule, plotted
versus h2.
We extrapolate the computed results as a polynomial ﬁt in h2 using the
MATLAB command
pfit = polyfit(h.ˆ2,I,m)
Here, m is the order of the polynomial, and the extrapolated value of the
integral is the coeﬃcient for h0. [With the MATLAB convention for storing
polynomials, this is the (m+1)th component of pfit]. A ﬁrst-order ﬁt (m = 1)
gives the extrapolation I(1, 1) ≃0.79335 88818, second-order (m = 2) gives
0.79335 91208, and a third-order ﬁt gives 0.79335 91213.
The results from the Simpson integration fall on an almost straight line
when plotted against h4, and we conclude that the dominant error scales as
2.1 Extrapolation to Zero Cell Size
h4. A ﬁt of ISimpson(1, 1) to a linear polynomial in h4 gives the extrapolation
0.79335 91207, and quadratic and cubic ﬁts give 0.79335 91202.
The correct answer to eight digits is 0.79335 912. Extrapolation allows us to
establish this degree of accuracy with a rather moderate eﬀort: a second-order
ﬁt of the low-order midpoint rule versus h2, using data computed for rather
coarse grids h ≥0.05. This gives eight-digit accuracy of the extrapolation
even though the computed data has only three to four correct digits. Thus,
extrapolation can bring very signiﬁcant improvements of accuracy. Another
advantage of extrapolation is that it makes us aware of how good the accuracy
is. The example shows that good accuracy can also be obtained by using the
higher-order Simpson integration, even without extrapolation, on a grid of
moderate size.
A simple way to estimate the order of convergence is to carry out compu-
tations for a geometric sequence of cell sizes such that hi/hi+1 = hi+1/hi+2.
Assuming that the lowest-order term in the expansion of the error is suﬃcient,
i.e. I(h) = I0 + Iphp, and that the cell sizes form a geometric series, one can
then estimate the order of convergence as
p = ln
 I(hi) −I(hi+1)
I(hi+1) −I(hi+2)
 hi
hi+1
(2.4)
When applied to the computed results for h = 0.2, 0.1 and 0.05, this formula
gives p = 2.002 for the midpoint rule and p = 3.985 for Simpson, indicat-
ing that the convergence is quadratic and quartic, respectively, for the two
methods.
2.1.1 A Singular Problem
It is instructive to consider a more singular problem, such as the potential on
the midpoint of the plate, z = 0. Now, the integrand is singular, but the inte-
gral is nevertheless convergent. For this problem, Simpson integration gives a
divergent result and cannot be used. (This illustrates the fact that high-order
methods often experience diﬃculties in the presence of singularities.) How-
ever, the midpoint integration still works, and for the cell sizes above we ﬁnd
the following values for Imidp(0, 1): 1.684320, 1.706250, 1.722947, 1.736083,
1.742700. Plots of Imidp versus hp reveal that the order of convergence is now
lower, p = 1. Nevertheless, we can still extrapolate using ﬁts to polynomials
in h. The results are linear, 1.762015; quadratic, 1.762745; cubic, 1.762748.
This integral can be done analytically: I(0, 1) = 2 ln(1 +
2) ≈1.762747.
Thus, despite the singularity, the midpoint rule gives six-ﬁgure accuracy with
h ≥0.05 and quadratic extrapolation.
Review Questions
2.1-1 What is meant by resolution in the context of numerical computations?
Give some examples.
2 Convergence
2.1-2 How can the error in a computation be estimated?
2.1-3 What inﬂuences the error and the order of convergence?
2.1-4 Give a couple of examples of numerical integration rules and provide
a simple comparison. Especially consider the diﬀerences for smooth and
singular integrands.
2.2 Practical Procedures
The example we have just studied is very simple. Real application problems
have more complex geometry than a square, but on the other hand, six-digit
accuracy is very rarely needed, or even possible to achieve. Furthermore, nu-
merical results converge in the very regular way we found here only if the grid
can be reﬁned uniformly over the whole computational region. When this is
not possible, the convergence may be oscillatory, and the extrapolation to
zero cell size becomes more diﬃcult. In practice, it is often possible to extract
a main power of convergence with the number of grid cells, but the remain-
der is too oscillatory to be convincingly ﬁt by higher-order polynomials. A
more robust and practical procedure for such cases is to use a linear ﬁt of
the computed results to hp, where p is the estimated order of convergence.
When the converged answer is not known, but the convergence is suﬃciently
regular, the order of convergence can be estimated from results for three dif-
ferent resolutions. To ascertain that the estimated order of convergence is not
accidental, at least four diﬀerent resolutions should be used. Once the order
of convergence is established, extrapolation to zero cell size can be made by
ﬁtting a lowest-order expansion
I(h) = I0 + Iphp
(2.5)
to the computed results.
Review Question
2.2-1 Why can extrapolation to zero cell size be diﬃcult for nonuniformly
reﬁned grids?
Summary
The accuracy of a numerical result depends on resolution. For example,
a domain of integration can be divided into segments of size h, and a
numerical evaluation of the integral I is then expressed as I(h) = I0 +
Iphp + · · · , where I0 is the exact result, Iphp is the dominant error term
(provided that h is suﬃciently small), and p is the order of convergence.
2.2 Practical Procedures
The order of convergence p can be estimated from
p = ln
 I(hi) −I(hi+1)
I(hi+1) −I(hi+2)
 hi
hi+1
which requires at least three computations and where hi/hi+1 = hi+1/hi+2.
The result should preferably be veriﬁed for at least four resolutions to as-
certain that the estimated p is not accidental.
A simple method to estimate the error of a given computation is to (i)
do a convergence test by uniform grid reﬁnement, (ii) ﬁnd the order of
convergence, and (iii) extrapolate the computed results to zero cell size.
The order of convergence depend on the method and the regularity of the
solution. Singular behavior of the solution decreases the order of conver-
gence p in many real-world problems.
Problems
P.2-1 Derive the order of convergence for midpoint integration (2.2) and Simp-
son’s rule (2.3) under the assumption that the integrand is regular. How
does a singular integrand inﬂuence your derivation?
P.2-2 Show that (2.4) gives an estimate for p. Under what conditions is this
estimate accurate?
Computer Projects
C.2-1 Repeat the calculations of I(1, 1) and I(0, 1), where I(z, a) is deﬁned
in (2.1), using two-point Gaussian integration
 x+h
f(x)dx = h
x + h
1 −1
x + h
1 + 1
and ﬁnd the order of convergence.
C.2-2 Calculate the integral
0 x−αdx, with a singular integrand, numerically
by dividing the interval into equal elements and applying midpoint inte-
gration on each. Investigate the cases α = 0.5 and 0.8, ﬁnd the order
of convergence, and extrapolate to zero cell size. The exact integral is
1/(1 −α).
Finite Diﬀerences
Maxwell’s equations are usually formulated as diﬀerential equations. There-
fore, it is quite natural to solve them by ﬁnite diﬀerence methods, where the
derivatives are approximated by diﬀerences between neighboring points on
a grid. In a one-dimensional (1D) problem on the x-axis, a ﬁnite diﬀerence
method introduces a set of grid points x1, x2, . . . , xN where a sought function
f(x) takes the values f(x1), f(x2), . . . , f(xN).
We will ﬁrst recapitulate expressions for ﬁrst- and second-order diﬀerences
on a uniform grid with grid points xn+i = xn + ih, where i is an integer and
h is the distance between the grid points (often referred to as cell size). The
basis for this is the Taylor expansion
f(x + δ) = f(x) + δf ′(x) + δ2
2 f ′′(x) + δ3
6 f ′′′(x) + · · ·
(3.1)
To get the ﬁrst derivative on a grid point x, we could use the noncentered
diﬀerence [f(x + h) −f(x)]/h = f ′(x) + O(h), but the error here is of ﬁrst
order in h. One way to increase the order of approximation is to take the
diﬀerence across two cells, which gives
f(x + h) −f(x −h)
= f ′(x) + O(h2).
(3.2)
As we shall see shortly, this becomes very inaccurate for short wavelengths, in
particular, when the wavelength is less than four grid cells. A better alternative
is to use “staggered grids” and compute the ﬁrst-order derivative on the “half-
grid” xi+ 1
2 = xi + h/2:
f(x + h) −f(x)
= f ′
x + h
+ O(h2).
(3.3)
A diﬀerence formula for the second derivative on an equidistant grid can be
developed by applying (3.3) repeatedly, which gives

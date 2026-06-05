# Bondeson《Computational Electromagnetics》第5章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 72-101 of 231 (231 total)

---

## The Finite-Difference Time-Domain Method

5 The Finite-Diﬀerence Time-Domain Method
for instance scattering problems, selected time signals from an FDTD simu-
lation can be Fourier transformed while the simulation proceeds, and a single
FDTD run can produce frequency-domain results at any desired number of
frequencies. This is a major advantage of time-domain methods.
The FDTD algorithm was originally proposed by K.S. Yee in 1966 [87].
Since then, it has been used for a variety of applications, and many extensions
of the basic algorithm have been developed. The literature on the FDTD is
vast, and over the period 1975–1995 the number of research papers in which
the FDTD method was used grew exponentially in time. By now, the FDTD
is considered a basic tool in CEM, and research articles now tend to be on
more complicated methods. The books by Taﬂove et al. [75, 77, 76] give a
good overview and describe many important extensions of the FDTD. Much
information on the FDTD method can also be found at www.fdtd.org [68].
5.1 The 1D Wave Equation
To solve the wave equation (1.12) numerically, we divide the z-axis into inter-
vals of length ∆z and the time axis into intervals of length ∆t (see Figure 5.1).
Fig. 5.1. The grid used to numerically solve the 1D wave equation.
Let |r be an index that refers to the z-coordinate and let |n refer to the
time coordinate such that E|n
r = E(r∆z, n∆t). We get the discrete equation
by using standard diﬀerence approximations for the derivatives:
E|n+1
−2 E|n
r + E|n−1
(∆t)2
= c2 E|n
r+1 −2 E|n
r + E|n
(∆z)2
(5.1)
5.1 The 1D Wave Equation
Equation (5.1) gives an explicit expression for E at the next time level n + 1
in terms of E at the previous levels:
E|n+1
= 2 E|n
r −E|n−1
c∆t
(E|n
r+1 −2 E|n
r + E|n
r−1),
(5.2)
which is identical to (4.19) when the speed of the wave c is set to unity. Two
time levels of E must be given as initial conditions. For the analytical wave
equation one needs E and ∂E/∂t as functions of z at t = 0.
The dispersion relation for the ﬁnite diﬀerence approximation in (5.1) can
be found by substituting E|n
r with exp(jω n∆t −jk r∆z) and dividing the
equation by exp(jω n∆t −jk r∆z):
ejω∆t −2 + e−jω∆t
(∆t)2
= c2 e−jk∆z −2 + ejk∆z
(∆z)2
This can be rewritten as
ejω∆t/2 −e−jω∆t/2
c∆t
2 ejk∆z/2 −e−jk∆z/2
Taking the square root, we get the dispersion relation for the numerical
scheme:
sin ω∆t
= ±c∆t
∆z sin k∆z
(5.3)
For the numerical solutions, the angular frequency ω is only approximately
a linear function of the wavenumber k, unless ∆z = c∆t. Consequently,
waves with diﬀerent wavenumbers will propagate with diﬀerent velocities.
This means that a wave package containing several diﬀerent spatial frequen-
cies will change shapes as it propagates. This is referred to as the dispersion
of the numerical scheme, or numerical dispersion for short.
5.1.1 Dispersion and Stability
How does the choice of ∆t and ∆z aﬀect the dispersion? Equation (5.3) shows
that the important parameter is R = c∆t/∆z, that is, how many grid cells the
exact solution propagates in one time-step. Dispersion relations for diﬀerent
values of R ≤1 are shown in Figure 5.2.
We have the following distinct situations:
R = 1: If ∆t = ∆z/c, then R = 1 and (5.3) simpliﬁes to ω = ±ck, which is
exactly the analytical dispersion relation (1.14). This choice of ∆t is called
the magic time step. The errors of the spatial and temporal diﬀerence
approximations cancel, and the signals propagate exactly one cell per time-
step, in either direction.
5 The Finite-Diﬀerence Time-Domain Method
k∆z [−]
ω∆z/c [−]
R = 1
R = 0.8
lim R → 0
Fig. 5.2. Numerical dispersion relations for diﬀerent values of R = c∆t/∆z.
R < 1: If ∆t < ∆z/c, the numerical dispersion relation diﬀers from the an-
alytical. The smaller R is, the stronger is the numerical dispersion (see
Figure 5.2). The dispersion properties improve as ∆t approaches the magic
time-step.
R > 1: If ∆t > ∆z/c, then R > 1 and (5.3) yields complex angular fre-
quencies for wavenumbers such that | sin k∆z/2| > ∆z/c∆t = 1/R. As a
consequence, some waves will be exponentially growing in time, i.e., the
algorithm is unstable. This exempliﬁes the type of instability discussed in
Section 4.4.1. When c∆t > ∆z, the signal of the true solution propagates
more than one cell per time-step, and that is not possible with the explicit
scheme in (5.2), which involves only nearest neighbors. The stability con-
dition c∆t ≤∆z is often called the Courant (or Courant–Friedrichs–Levy,
CFL) condition. Similar conditions, implying that the signal can propa-
gate at most one grid cell per time-step, hold for practically all explicit
schemes for any diﬀerential equation.
Example: A Square Wave
A square wave can be represented as an inﬁnite sum of harmonic components
with diﬀerent frequencies, and it is rich in high-frequency components. When
such a wave propagates in a dispersive medium, the diﬀerent sine waves prop-
agate with diﬀerent velocities, and the shape of the wave will change as it
propagates. The 1D wave equation can be time-stepped using selected parts
of the MATLAB function Wave1D given in Section 4.4.2. Figures 5.3–5.5 show
the propagation of a square wave for three diﬀerent values of R.
5.1 The 1D Wave Equation
−0.8 −0.6 −0.4 −0.2
E [V/m]
z [m]
t = 0
t = 100
t = 200
Fig. 5.3. Propagation of a square wave when ∆t is equal to the magic time-step,
R = c∆t/∆z = 1. There is no dispersion: the shape of the pulse stays the same as
it propagates.
−0.8 −0.6 −0.4 −0.2
E [V/m]
z [m]
t = 0
t = 100
t = 200
Fig. 5.4. Propagation of a square wave when ∆t is smaller than the magic time-step,
R = c∆t/∆z = 1/
3 ≈0.58. In this case, there is signiﬁcant numerical dispersion:
the shape of the pulse changes as it propagates.
−0.8 −0.6 −0.4 −0.2
E [V/m]
z [m]
t = 0
t = 18∆t
Fig. 5.5. Propagation of a square wave when ∆t is slightly greater than the magic
time-step, R = c∆t/∆z = 1.01. The scheme is unstable and the wave amplitude
increases rapidly in an unphysical way.
Example: A Smooth Wave
An initial condition in the form of a square wave highlights the dispersion
of the numerical scheme. As a second example, we take as initial condition a
Gaussian pulse that is well resolved on the grid, with 12 points across the 1/e
width; see Figure 5.6. This pulse can propagate many pulse widths before the
dispersion becomes apparent to the eye, even when R = 1/
an important point: numerical results are accurate only when the solution is
well resolved by the grid. Of course, a square wave is not well resolved on any
grid.
Similarly, if we compute a Gaussian pulse with insuﬃcient resolution, the
dispersion will be strong. Figure 5.7 shows a case in which the 1/e width of the
5 The Finite-Diﬀerence Time-Domain Method
−0.8 −0.6 −0.4 −0.2
E [V/m]
z [m]
t = 0
t = 100
t = 200
Fig. 5.6. Propagation of a Gaussian pulse with 12 points across the 1/e width when
∆t is smaller than the magic time-step, R = c∆t/∆z = 1/
has some dispersion, it is hard to see with the naked eye when the pulse is well
resolved.
Gaussian is 6 points. Here, the dispersion manifests itself as short-wavelength
oscillations trailing behind the main pulse. The oscillations are behind the
main pulse because the phase velocity is smaller for short wavelengths.
−0.8 −0.6 −0.4 −0.2
E [V/m]
z [m]
t = 0
t = 100
t = 200
Fig. 5.7. Propagation of a Gaussian pulse with 6 points across the 1/e width when
∆t is smaller than the magic time-step, R = c∆t/∆z = 1/
is not very good, and the eﬀect of the dispersion is clearly visible to the eye.
Review Questions
5.1-1 List some pros and cons of the FDTD scheme.
5.1-2 What is a dispersion relation? Derive the dispersion relation for the 1D
wave equation discretized by the standard ﬁnite diﬀerence approximation.
Compare the numerical dispersion relation with its analytical counterpart.
5.1-3 Under what conditions will E(z, t) = E+(z −c t) + E−(z + c t) satisfy
the discretized 1D wave equation?
5.1-4 Generally, higher resolutions lead to more accurate results, but in some
cases this is not true. Give an example of this and explain why.
5.1-5 Explain how and why a pulse is distorted when propagated by the wave
equation discretized by ﬁnite diﬀerences.
5.2 The FDTD Method: Staggered Grids
5.2 The FDTD Method: Staggered Grids
The wave equation is a second-order diﬀerential equation for the electric ﬁeld
only. It can also be stated as a system of coupled ﬁrst-order diﬀerential equa-
tions for both E and H. In three dimensions, Maxwell’s equations (1.9)–(1.10)
in a source-free region give six scalar equations, three for Amp`ere’s law,
ϵ∂Ex
= ∂Hz
∂y −∂Hy
∂z ,
(5.4)
ϵ∂Ey
= ∂Hx
∂z −∂Hz
∂x ,
(5.5)
ϵ∂Ez
= ∂Hy
∂x −∂Hx
∂y ,
(5.6)
and three for Faraday’s law,
µ∂Hx
= ∂Ey
∂z −∂Ez
∂y ,
(5.7)
µ∂Hy
= ∂Ez
∂x −∂Ex
∂z ,
(5.8)
µ∂Hz
= ∂Ex
∂y −∂Ey
∂x .
(5.9)
The FDTD is a ﬁnite diﬀerence scheme particularly suited to the structure of
these six ﬁrst-order equations. In particular, it uses diﬀerence formulas that
are as local as possible and centered.
5.2.1 One Space Dimension
To illustrate the use of staggered grids, which is central to the FDTD, we
will start with a 1D problem. Consider a plane wave propagating in the z-
direction through a medium such that all quantities are constant in planes
perpendicular to the z-axis. We assume that the electric ﬁeld is oriented in
the x-direction, and the magnetic ﬁeld in the y-direction. Then, (5.4)–(5.9)
reduce to
ϵ∂Ex
= −∂Hy
∂z ,
(5.10)
µ∂Hy
= −∂Ex
∂z .
(5.11)
The “trick” used to get a good algorithm is to put the diﬀerent E- and H-
components at diﬀerent positions on the grid, and also to evaluate the equa-
tions at diﬀerent positions. As we saw in Section 3.2, ﬁrst-order derivatives
are much more accurately evaluated on staggered grids, such that if a vari-
able is located on the integer grid, its ﬁrst derivative is best evaluated on
5 The Finite-Diﬀerence Time-Domain Method
the half-grid, and vice versa. This holds with respect to both space and time.
Therefore, if we choose to place Ex on the integer points both in space and
in time, Hy should be on the half-grids in both variables, as illustrated in
Figure 5.8. This arrangement is called “staggered grids.”
Let |r be an index that refers to the z-coordinate and let |n refer to the time
coordinate such that f|n
r ≡f(r∆z, n∆t). Then, (5.10) is applied at integer
space points (indexed by r) and half-integer time points (indexed by n + 1/2)
using centered and local ﬁnite diﬀerences in both z and t. Similarly, (5.11)
is applied at half-integer space points (indexed by r + 1/2) and integer time
points (indexed by n) points, also using centered and local ﬁnite diﬀerences
in both z and t. The ﬁnite diﬀerence approximation of (5.10)–(5.11) on the
staggered grids reads
Ex|n+1
−Ex|n
= −1
n+ 1
r+ 1
2 −Hy|
n+ 1
(5.12)
n+ 1
r+ 1
2 −Hy|
r+ 1
= −1
Ex|n
r+1 −Ex|n
(5.13)
As initial conditions we need one time level for Ex and one for Hy.
For problems with variable permittivity and permeability, it is important
to keep in mind that (5.12) is evaluated on the integer grid and (5.13) is evalu-
ated on the half-grid. Consequently, it is natural to sample the permittivity on
the integer grid that gives ϵ = ϵ(zr) with z = r∆z. Similarly, the permeability
is evaluated on the half-grid which gives that µ = µ(zr+ 1
2 ).
Interfaces between regions with homogeneous but diﬀerent material pa-
rameters can be treated in the following way: we place a grid point zr (where
the electric ﬁeld is deﬁned) at the interface and choose the permittivity at this
grid point to be the average of the permittivities in the two media sharing
the interface, i.e., ϵ = (ϵA + ϵB)/2 at zr, where ϵA and ϵB denote the permit-
tivities in the two media. The permeability is then unproblematic, since it is
evaluated at least half a cell from the interface. This approach maintains the
order of convergence for the FDTD scheme, whereas other approaches may
yield deteriorated convergence properties.
It is instructive to eliminate Hy from (5.12)–(5.13):
Ex|n+1
−2Ex|n
r + Ex|n−1
(∆t)2
5.2 The FDTD Method: Staggered Grids
{rearrange} = 1
Ex|n+1
−Ex|n
−Ex|n
r −Ex|n−1
{(5.12)} = −1
n+ 1
r+ 1
2 −Hy|
n+ 1
r+ 1
2 −Hy|
{rearrange} = −1
n+ 1
r+ 1
2 −Hy|
r+ 1
n+ 1
2 −Hy|
{(5.13)} =
ϵµ∆z
Ex|n
r+1 −Ex|n
−Ex|n
r −Ex|n
{rearrange} = c2 Ex|n
r+1 −2Ex|n
r + Ex|n
(∆z)2
(5.14)
Thus, Ex evolved according to the coupled ﬁrst-order equations (5.12)–(5.13)
on the staggered grid satisﬁes the 1D wave equation on standard integer grids,
which we studied in Section 5.1. Therefore, the dispersion properties and the
stability condition of the coupled ﬁrst-order system are the same as for the
wave equation; for instance, ∆t ≤∆z/c is necessary for stability.
If we had not used staggered grids for Ex and Hy, but taken the ﬁrst
derivative in z across two cells, then the resulting diﬀerence approximation
for the second-order z-derivative in (5.14) would involve Ex|n
r+2 and Ex|n
r−2.
This is less accurate and makes the grids with r even and odd decouple. Ex
components with r odd would evolve completely independently of those with
r even. We conclude that in order to get the same accuracy and robustness
as the 1D wave equation for Ex, it is necessary to place one of Ex and Hy on
a half-grid; that is, we must use a staggered grid for the coupled ﬁrst-order
equations.
5.2.2 Three Space Dimensions
The Yee scheme extends the staggering to three dimensions with a special
arrangement of all the components of E and H. The electric ﬁeld components
are computed at “integer” time-steps and the magnetic ﬁeld at “half-integer”
time-steps. Space is divided into bricks with sides ∆x, ∆y, and ∆z (usually
one uses cubes with ∆x = ∆y = ∆z = h). The diﬀerent ﬁeld components are
placed in the grid according to the unit cell shown in Figure 5.9.
The electric ﬁeld components are placed at the midpoints of the corre-
sponding edges; Ex is placed at the midpoints of edges oriented in the x-
direction, Ey at the midpoints of edges oriented in the y-direction, and Ez at
the midpoints of edges oriented in the z-direction. Thus, Ex is on the half-grid
in x and on the integer grids in y and z, etc. The magnetic ﬁeld components
are placed at the centers of the faces of the cubes and oriented normal to the
faces. Hx components are placed at the centers of faces in the yz-plane, Hy
components are centered on faces in the xz-plane, and Hz components are
5 The Finite-Diﬀerence Time-Domain Method
n = t /    t
r = z /    z
Fig. 5.8. Staggered grid used in the 1D leap-frog algorithm. The two “stencils”
show which values of Ex and Hy are used in solving (5.13) with (r = 1, n = 3) and
in solving (5.12) with (r = 4, n = 1).
p+1/2
q+1/2
r+1/2
Fig. 5.9. Unit cell in the 3D FDTD algorithm.
centered on faces in the xy-plane. Thus, Hx is on the integer grid in x and on
the half-grids in y and z, etc. This arrangement was introduced by Yee [87],
and the unit cell in Figure 5.9 is also known as the Yee cell. We will see in
Chapter 6 that the same spatial arrangement for E and H is natural also
for the ﬁnite element representation on hexahedral grids. Such FEM arrange-
5.2 The FDTD Method: Staggered Grids
ments are used both for frequency-domain microwave calculations and eddy
current calculations.
Let |p,q,r be indices that refer to the x, y, and z coordinates and let |n refer
to the time coordinate such that f|n
p,q,r ≡f(p∆x, q∆y, r∆z, n∆t). With the
Yee arrangement for the ﬁeld components, the ﬁnite diﬀerence approximation
of Maxwell’s equations (5.4)–(5.9) reads
Ex|n+1
p+ 1
2 ,q,r −Ex|n
p+ 1
2 ,q,r
n+ 1
p+ 1
2 ,q+ 1
2 ,r −Hz|
n+ 1
p+ 1
2 ,q−1
2 ,r
n+ 1
p+ 1
2 ,q,r+ 1
−Hy|
n+ 1
p+ 1
2 ,q,r−1
(5.15)
Ey|n+1
p,q+ 1
2 ,r −Ey|n
p,q+ 1
2 ,r
n+ 1
p,q+ 1
2 ,r+ 1
2 −Hx|
n+ 1
p,q+ 1
2 ,r−1
n+ 1
p+ 1
2 ,q+ 1
2 ,r −Hz|
n+ 1
2 ,q+ 1
2 ,r
(5.16)
Ez|n+1
p,q,r+ 1
2 −Ez|n
p,q,r+ 1
n+ 1
p+ 1
2 ,q,r+ 1
2 −Hy|
n+ 1
2 ,q,r+ 1
n+ 1
p,q+ 1
2 ,r+ 1
2 −Hx|
n+ 1
p,q−1
2 ,r+ 1
(5.17)
n+ 1
p,q+ 1
2 ,r+ 1
2 −Hx|
p,q+ 1
2 ,r+ 1
Ey|n
p,q+ 1
2 ,r+1 −Ey|n
p,q+ 1
2 ,r
Ez|n
p,q+1,r+ 1
2 −Ez|n
p,q,r+ 1
(5.18)
n+ 1
p+ 1
2 ,q,r+ 1
2 −Hy|
p+ 1
2 ,q,r+ 1
Ez|n
p+1,q,r+ 1
2 −Ez|n
p,q,r+ 1
Ex|n
p+ 1
2 ,q,r+1 −Ex|n
p+ 1
2 ,q,r
(5.19)
5 The Finite-Diﬀerence Time-Domain Method
n+ 1
p+ 1
2 ,q+ 1
2 ,r −Hz|
p+ 1
2 ,q+ 1
2 ,r
Ex|n
p+ 1
2 ,q+1,r −Ex|n
p+ 1
2 ,q,r
Ey|n
p+1,q+ 1
2 ,r −Ey|n
p,q+ 1
2 ,r
(5.20)
The Yee scheme, or FDTD, has proven very successful for microwave problems.
All derivatives are centered and as compact as possible, that is, they are taken
across a single cell.
5.2.3 MATLAB: Cubical Cavity
In this example we will use the FDTD to compute the resonant frequencies
of an air-ﬁlled, cubical cavity with metal walls. By evolving the electric ﬁeld
in time and sampling it at some locations in the cavity, we get the electric
ﬁelds at these locations as functions of time. We then use a discrete Fourier
transform to ﬁnd the resonant frequencies of the cavity.
Discretization
First the cavity must be discretized. Let us divide the cavity into Nx×Ny×Nz
cells. A cavity divided into 3 × 4 × 2 cells is shown in Figure 5.10. To store
the ﬁelds both inside the cavity and on the cavity wall, we need to store the
values of
Ex at 3 × 5 × 3 =
× (Ny + 1) × (Nz + 1) positions,
Ey at 4 × 4 × 3 = (Nx + 1) ×
× (Nz + 1) positions,
Ez at 4 × 5 × 2 = (Nx + 1) × (Ny + 1) ×
positions,
Hx at 4 × 4 × 2 = (Nx + 1) ×
positions,
Hy at 3 × 5 × 2 =
× (Ny + 1) ×
positions, and
Hz at 3 × 4 × 3 =
× (Nz + 1) positions.
Boundary Conditions
At microwave frequencies, metal surfaces behave, to a good approximation, as
perfect electric conductors (PEC). Therefore, we set the tangential component
of the electric ﬁeld to zero on the metal boundaries.
Taking into account the arrangement of E and H, with the PEC boundary
condition, we can write FORTRAN-styled loops over indices, for updating Hx
as follows:
% Update Hx
for i = 1:Nx+1
for j = 1:Ny
5.2 The FDTD Method: Staggered Grids
Fig. 5.10. An illustration of how the diﬀerent ﬁeld components are placed on a grid
with 3 × 4 × 2 cells. The dotted lines indicate the number of unknowns (cells) that
have to be stored.
for k = 1:Nz
Hx(i,j,k) = Hx(i,j,k) + (Dt/mu0)* ...
((Ey(i,j,k+1)-Ey(i,j,k))/Dz - (Ez(i,j+1,k)-Ez(i,j,k))/Dy);
Hy and Hz are updated in corresponding ways. For Ex the scheme becomes
% Update Ex everywhere except on boundary
for i = 1:Nx
for j = 2:Ny
for k = 2:Nz
Ex(i,j,k) = Ex(i,j,k) + (Dt /eps0) * ...
((Hz(i,j,k)-Hz(i,j-1,k))/Dy-(Hy(i,j,k)-Hy(i,j,k-1))/Dz);
5 The Finite-Diﬀerence Time-Domain Method
Note that only the most recent values of the ﬁeld components have to be
stored. Therefore, we store the updated values at the same location in memory
as the old values in order to reduce memory requirements.
Although this will produce the correct result, it may execute rather slowly
in MATLAB. To improve on eﬃciency, operations should be done on entire
arrays or matrices. This is accomplished by rewriting the three nested for
loops as single statements:
% Update Hx everywhere
Hx = Hx + (Dt/mu0)*((Ey(:,:,2:Nz+1)-Ey(:,:,1:Nz))/Dz ...
- (Ez(:,2:Ny+1,:)-Ez(:,1:Ny,:))/Dy);
% Update Ex everywhere except on boundary
Ex(:,2:Ny,2:Nz) = Ex(:,2:Ny,2:Nz) + (Dt /eps0) * ...
((Hz(:,2:Ny,2:Nz)-Hz(:,1:Ny-1,2:Nz))/Dy ...
- (Hy(:,2:Ny,2:Nz)-Hy(:,2:Ny,1:Nz-1))/Dz);
Finally, the diﬀerences in the discretized curl operator can be written even
more compactly by using the diff function, as will be shown in the complete
program that follows.
Initial Conditions
In order to observe an eigenfrequency in the resulting frequency spectrum,
the corresponding eigenmode must be excited. An initial condition for E in
the form of a random ﬁeld ensures that most modes are excited. [This leads to
∇·E ̸= 0 in the initial condition. Since there is no electric current, the resulting
electrical charge density ρ = ϵ0∇·E should be time-independent. Fortunately,
one of the good properties of the FDTD scheme is that it preserves this
property of Maxwell’s equations exactly.]
Sampling
It is important to sample the ﬁelds in such a way that all desired frequencies
(modes) are detected. With only a bit of bad luck, some modes will have a
node (zero) at the chosen detector location. To avoid this problem, it is a good
idea to record several ﬁeld components at several detector locations.
Choice of Time Step
The larger the time step, the smaller the dispersion and the faster the simu-
lation. Therefore, we choose ∆t as big as possible, i.e., at the stability limit
(5.33).
5.2 The FDTD Method: Staggered Grids
A MATLAB program that simulates the ﬁeld inside a brick-shaped cavity
with PEC walls is listed below. In the time-stepping part, (5.15)–(5.20) are
evaluated using the MATLAB function diff. For a vector X, of length N,
diff(X) is the vector [X(2)-X(1) X(3)-X(2) ... X(N)-X(N-1)] of length
N −1. The second argument of diff is the order of the diﬀerence, in this
case 1, for the ﬁrst derivative. The third argument speciﬁes the dimension in
which diﬀerences are taken (x →1, y →2, z →3).
% Physical constants
eps0 = 8.8541878e-12;
% Permittivity of vacuum
= 4e-7 * pi;
% Permeability of vacuum
= 299792458;
% Speed of light in vacuum
% Parameter initiation
Lx = .05; Ly = .04; Lz = .03; % Cavity dimensions in meters
Nx =
25; Ny =
20; Nz =
15; % Number of cells along each axis
Cx = Nx / Lx;
% Inverse cell dimensions
Cy = Ny / Ly;
Cz = Nz / Lz;
Nt = 8192;
% Number of time steps
Dt = 1/(c0*norm([Cx Cy Cz])); % Time step
% Allocate field matrices
Ex = zeros(Nx
, Ny+1, Nz+1);
Ey = zeros(Nx+1, Ny
, Nz+1);
Ez = zeros(Nx+1, Ny+1, Nz
Hx = zeros(Nx+1, Ny
, Nz
Hy = zeros(Nx
, Ny+1, Nz
Hz = zeros(Nx
, Ny
, Nz+1);
% Allocate time signals
Et = zeros(Nt,3);
% Initiate fields with noise (except on the boundary)
Ex( :
, 2:Ny, 2:Nz) = rand(Nx
, Ny-1, Nz-1) - 0.5;
Ey(2:Nx,
, 2:Nz) = rand(Nx-1, Ny
, Nz-1) - 0.5;
Ez(2:Nx, 2:Ny,
) = rand(Nx-1, Ny-1, Nz
) - 0.5;
% Time stepping
for n = 1:Nt;
% Update H everywhere
Hx = Hx + (Dt/mu0)*(diff(Ey,1,3)*Cz - diff(Ez,1,2)*Cy);
Hy = Hy + (Dt/mu0)*(diff(Ez,1,1)*Cx - diff(Ex,1,3)*Cz);
Hz = Hz + (Dt/mu0)*(diff(Ex,1,2)*Cy - diff(Ey,1,1)*Cx);
% Update E everywhere except on boundary
Ex(:,2:Ny,2:Nz) = Ex(:,2:Ny,2:Nz) + (Dt /eps0) * ...
(diff(Hz(:,:,2:Nz),1,2)*Cy - diff(Hy(:,2:Ny,:),1,3)*Cz);
5 The Finite-Diﬀerence Time-Domain Method
Ey(2:Nx,:,2:Nz) = Ey(2:Nx,:,2:Nz) + (Dt /eps0) * ...
(diff(Hx(2:Nx,:,:),1,3)*Cz - diff(Hz(:,:,2:Nz),1,1)*Cx);
Ez(2:Nx,2:Ny,:) = Ez(2:Nx,2:Ny,:) + (Dt /eps0) * ...
(diff(Hy(:,2:Ny,:),1,1)*Cx - diff(Hx(2:Nx,:,:),1,2)*Cy);
% Sample the electric field at chosen points
Et(n,:) = [Ex(4,4,4) Ey(4,4,4) Ez(4,4,4)];
The frequency spectrum we get from the Fourier transform of the columns
of Et is plotted in Figure 5.11 together with the analytical resonant frequen-
cies:
fmnp = c
(m/Lx)2 + (n/Ly)2 + (p/Lz)21/2 .
(5.21)
In this case there are two kinds of modes, referred to as TMmnp and TEmnp
modes (see, e.g., [18]). For TMmnp modes, m ̸= 0, n ̸= 0. For TEmnp modes,
p ̸= 0, m or n is nonzero.
f [GHz]
E [V/m]
Fig. 5.11. Frequency spectrum obtained from an FDTD simulation of an air-ﬁlled
brick-shaped cavity. The solid curve shows the frequency spectrum of the sum of
the sampled Ex, Ey, and Ez components. The dotted lines show the exact eigenfre-
quencies.
5.2.4 Integral Interpretation of the FDTD Method
The Yee-scheme, (5.15)–(5.20), can also be derived using the integral repre-
sentation of Maxwell’s equations:
5.2 The FDTD Method: Staggered Grids
∂(ϵE)
· dS =
H · dl,
(5.22)
∂(µH)
· dS = −
E · dl.
(5.23)
To obtain the equation for ∂Hz/∂t we ﬁrst compute the surface integral over
a face on the grid cells z = r∆z, p∆x < x < (p+1)∆x, q∆y < y < (q +1)∆y:
∂(µH)
· dS ≈µ
n+ 1
p+ 1
2 ,q+ 1
2 ,r −Hz|
p+ 1
2 ,q+ 1
2 ,r
∆x∆y.
(5.24)
The corresponding line integral of E along the line circulating Hz|p+ 1
2 ,q+ 1
2 ,r
according to the right-hand rule, shown in Figure 5.12, is calculated as
E · dl ≈Ex|n
p+ 1
2 ,q,r∆x + Ey|n
p+1,q+ 1
2 ,r∆y
−Ex|n
p+ 1
2 ,q+1,r∆x −Ey|n
p,q+ 1
2 ,r∆y.
(5.25)
Here, the Yee arrangement has the nice property that the components of E
that are needed for this integral appear exactly at the midpoint of the edges
along which they are to be integrated.
Combining (5.23)–(5.25) we obtain
n+ 1
p+ 1
2 ,q+ 1
2 ,r −Hz|
p+ 1
2 ,q+ 1
2 ,r
Ey|n
p+1,q+ 1
2 ,r −Ey|n
p,q+ 1
2 ,r
Ex|n
p+ 1
2 ,q+1,r −Ex|n
p+ 1
2 ,q,r
(5.26)
which is exactly the same as the previously derived (5.20).
Another interesting property of the Yee scheme is that the condition of
solenoidal magnetic ﬂux density (1.4) is implicitly enforced for all times, pro-
vided that the initial conditions are correct. To demonstrate this, we ap-
ply Gauss’s theorem to (1.4), and this gives
S B · ˆndS = 0, where the
closed surface S is taken as the surface of the unit cell shown in Figure 5.9.
This integral is divided into three Cartesian components:
S B · ˆn dS =
Sp B · ˆn dS +
Sq B · ˆn dS +
Sr B · ˆn dS. For example, Sp is the two surfaces
in the yz-plane that are deﬁned by constant index p and p + 1. It is instruc-
tive to study the time derivative of
Sp B · ˆndS in the discrete setting. The
integrals over the surfaces p and p + 1 are evaluated as in (5.24), and given
this result, we form the time derivative (in the leap-frog sense) centered at
n. Next, we change the order of the (numerical) time derivative and surface
integral, which yields an expression that features the time derivative of the
normal component of the magnetic ﬁeld for the two surfaces. These are shown
in (5.18), which is the x-component of Faraday’s law, and we use this relation
5 The Finite-Diﬀerence Time-Domain Method
p+1/2
q+1/2
p−1/2
p+1/2
q+1/2
q−1/2
Fig. 5.12. An illustration showing how Hz and Ez are “circulated” by four electric
and magnetic components respectively in the Yee grid.
to replace the time derivative of the magnetic ﬁeld with the curl of the electric
ﬁeld, still working only with the x-component. The last step is to rewrite the
x-components of the curl into the circulation of the electric ﬁeld along the
contour of the surfaces p and p + 1. Here are the detailed calculations:
B · ˆn dS ≈µ0
n+ 1
p+1,q+ 1
2 ,r+ 1
2 −Hx|
n+ 1
p,q+ 1
2 ,r+ 1
∆y∆z
p+1,q+ 1
2 ,r+ 1
2 −Hx|
p,q+ 1
2 ,r+ 1
∆y∆z
= µ0
Hx|
n+ 1
p+1,q+ 1
2 ,r+ 1
2 −Hx|
p+1,q+ 1
2 ,r+ 1
n+ 1
p,q+ 1
2 ,r+ 1
2 −Hx|
p,q+ 1
2 ,r+ 1
∆y∆z
Ey|n
p+1,q+ 1
2 ,r+1 −Ey|n
p+1,q+ 1
2 ,r
Ez|n
p+1,q+1,r+ 1
2 −Ez|n
p+1,q,r+ 1
Ey|n
p,q+ 1
2 ,r+1 −Ey|n
p,q+ 1
2 ,r
Ez|n
p,q+1,r+ 1
2 −Ez|n
p,q,r+ 1
∆y∆z
5.2 The FDTD Method: Staggered Grids
Ey|n
p+1,q+ 1
2 ,r+1∆y −Ez|n
p+1,q+1,r+ 1
2 ∆z −Ey|n
p+1,q+ 1
2 ,r∆y
+Ez|n
p+1,q,r+ 1
2 ∆z −Ey|n
p,q+ 1
2 ,r+1∆y −Ez|n
p,q,r+ 1
2 ∆z
+Ey|n
p,q+ 1
2 ,r∆y + Ez|n
p,q+1,r+ 1
2 ∆z
The corresponding results for the other two surface integrals, evaluated over
Sq and Sr, are given by cyclic permutations of the ﬁnal result for Sp. When
these three expressions are added, we ﬁnd that the circulations on the six
faces of the cube give, in total, two contributions to each edge of the unit cell
that cancel each other. Consequently, the condition of solenoidal magnetic ﬂux
density (1.4) is preserved numerically at all times, given appropriate initial
conditions. A similar analysis can be applied to Gauss’s law (1.3).
5.2.5 Dispersion Analysis in Three Dimensions
To simplify the dispersion analysis (and also to allow later comparison with
the ﬁnite element approach in Chapter 6), we note that one can eliminate H
by forming the second-order time derivative for E, in the same way as we did
for the 1D case in (5.14). Starting from (5.15)–(5.20), a somewhat lengthy
calculation (assuming that ϵ and µ are constant) gives
Ex|n+1
p+ 1
2 ,q,r −2Ex|n
p+ 1
2 ,q,r + Ex|n−1
p+ 1
2 ,q,r
(∆t)2
(5.27)
Ex|n
p+ 1
2 ,q+1,r −2Ex|n
p+ 1
2 ,q,r + Ex|n
p+ 1
2 ,q−1,r
(∆y)2
Ex|n
p+ 1
2 ,q,r+1 −2Ex|n
p+ 1
2 ,q,r + Ex|n
p+ 1
2 ,q,r−1
(∆z)2
Ey|n
p+1,q+ 1
2 ,r −Ey|n
p,q+ 1
2 ,r −Ey|n
p+1,q−1
2 ,r + Ey|n
p,q−1
2 ,r
∆x∆y
Ez|n
p+1,q,r+ 1
2 −Ez|n
p,q,r+ 1
2 −Ez|n
p+1,q,r−1
2 + Ez|n
p,q,r−1
∆x∆z
This is the ﬁnite diﬀerence form of
∂2Ex
 ∂2
∂y2 + ∂2
Ex −∂
∂Ey
∂y + ∂Ez
which, in turn, is the x-component of the curl-curl equation for E:
∂t2 = ∇2E −∇(∇· E) = −∇× ∇× E.
(5.28)
5 The Finite-Diﬀerence Time-Domain Method
The dispersion relation for FDTD in three dimensions can be found in
several diﬀerent ways. For instance, one can start from the electric ﬁeld for-
mulation (5.28) for all three components and plug in a plane wave solution
E = (ex, ey, ez) exp[j(ωt−kxx−kyy −kzz)]. From the analysis in Section 3.2,
we know that on staggered grids, where ﬁrst-order derivatives are taken across
one cell and second-order derivatives across two cells, numerical derivatives
acting on such exponentials simply multiply the function by the following
imaginary factors:
∂t →Dt = 2j
∆t sin ω∆t
∂x →Dx = −2j
∆x sin kx∆x
∂y →Dy = −2j
∆y sin ky∆y
(5.29)
∂z →Dz = −2j
∆x sin kz∆z
Thus, for complex exponentials, the matrix equation corresponding to the
three vector components of (5.28) is
y + D2
z −D2
t /c2
−DxDy
−DxDz
−DxDy
x + D2
z −D2
t /c2
−DyDz
−DxDz
−DyDz
x + D2
y −D2
t /c2
(5.30)
where Dt = jω for the continuous case and Dt = (2j/∆t) sin(ω∆t/2) for the
discretized system, etc. By setting the determinant of the matrix to zero, we
ﬁnd two roots,
t = c2(D2
x + D2
y + D2
(5.31)
representing transverse electromagnetic waves with two polarizations e ⊥k.
We get the usual (and exact) dispersion relation for light waves ω2 = c2(k2
y +k2
z) by replacing Dt →jω and Dx,y,z →−jkx,y,z, where the polarizations
of the two solutions are completely orthogonal as expected. In addition, there
is one root D2
t = 0 of (5.30), which translates into ω = 0. This represents
an “electrostatic” solution with e ∥k, i.e., a longitudinal, time-independent
solution. Note that this solution does not propagate. It gives a purely static
response of the electric ﬁeld to space charge.
It is interesting to see how the electrostatic solutions are treated by the
FDTD. Clearly, any electrostatic ﬁeld E = −∇φ, with φ constant in time, and
an arbitrary function of space, is a solution of the curl-curl equation (5.28).
One can verify that a solution E = −∇φ does not evolve in time with the
FDTD algorithm. This time-independent solution corresponds to the root
t = 0 of (5.30). Thus, the Yee scheme preserves the null-space of the curl-
curl operator, and this is one of its many good properties.
5.2 The FDTD Method: Staggered Grids
The numerical dispersion relation for the electromagnetic waves is obtained
by substituting the discrete derivative operators (5.29) into the general dis-
persion relation (5.31):
sin2 ω∆t/2
(c∆t)2
= sin2 kx∆x/2
(∆x)2
+ sin2 ky∆y/2
(∆y)2
+ sin2 kz∆z/2
(∆z)2
(5.32)
This is a natural generalization of the result in one dimension (5.3). Taylor
expansion of the sine functions shows that ω2 = c2(k2
x +k2
y +k2
z)[1+O(k2h2)],
so that the deviation from the correct dispersion relation for electromagnetic
waves is O(k2h2) for a cubic grid with ∆x = ∆y = ∆z = h. Note that
the dispersion is anisotropic. The wave propagation is the slowest along the
coordinate directions, and faster (and closer to the correct result) in oblique
directions.
The maximum time-step for stability follows from the requirement
sin2(ω∆t/2) ≤1 for all k,
just as in one dimension, and this gives
c∆t ≤
(∆x)2 +
(∆y)2 +
(∆z)2
−1/2
(5.33)
For a cubic grid with ∆x = ∆y = ∆z = h, the stability condition simpliﬁes
∆t ≤
(5.34)
In comparison with the 1D case, the maximum time-step has been reduced by
a factor
error is generally larger than the temporal discretization error for the FDTD
scheme in three dimensions, but they cancel each other to some extent. This
means, for example, that there is no magic time-step in this case. (Actually, for
ﬁelds varying equally fast in all directions, |kxh| = |kyh| = |kzh|, the stability
limit (5.34) is the magic time-step, but this works only for propagation in
those particular directions.)
Waves propagating along the coordinate axes suﬀer most from numerical
dispersion. To quantify the eﬀects of the numerical disperions, we consider a
wave propagating in the x-direction, i.e., kx = k and ky = kz = 0. Further,
we assume that ∆x = ∆y = ∆z = h and c∆t/h = 1/
simpliﬁes to
sin(ω∆t/2) =
3 sin(kh/2).
(5.35)
An expression for the phase velocity vp = ω/k of this wave can be derived
from a series expansion of (5.35):
vp = ω
k = c
1 −k2h2
+ O(k4h4)
(5.36)
5 The Finite-Diﬀerence Time-Domain Method
If we demand the relative error in phase velocity to be less than 1%, we require
(kh)2 < 36/100, which, since k ≡2π/λ, leads to λ/h < π/
0.09 ≈10.5,
that is, at least 10.5 cells per wavelength. This takes account of the partial
cancellation of the spatial and temporal errors in (5.32).
The same assumptions as in the preceding paragraph yield the following
expression for the group velocity:
vg = ∂ω
∂k = c
1 −k2h2
+ O(k4h4)
(5.37)
From this we ﬁnd that a resolution of about 18 cells per wavelength is required
to reduce the relative error of the group velocity to 1%. This is a stricter
requirement on the resolution as compared to the result derived from (5.36).
Typically, about 18 cells per wavelength is used as a rule of thumb for problems
that involve only a few wavelengths and engineering accuracy requirements.
The FDTD often requires even higher resolutions if one asks for a ﬁxed
absolute phase error across the whole computational domain, in particular
for problems that are large in terms of wavelengths, since the phase errors
accumulate. The absolute phase error is
ephase = (˜k −k)L =
c(1 −(kh)2/36 + · · · ) −ω
L ≈k3h2L
(5.38)
for a system with ﬁxed size L. To keep ephase constant, the cell size must
scale with frequency as ω−3/2, and consequently, the computational time is
proportional to 1/(h3∆t) ∝ω6.
The error associated with the numerical dispersion relation provides im-
portant understanding for one of the contributions to the total error. It must
be emphasized that convergence studies or other means of estimating the ac-
tual error are, in general, necessary to achieve reliable results for real-world
problems.
Review Questions
5.2-1 Draw the unit cell for the FDTD scheme in three space dimensions and
add all the ﬁeld components for both the electric ﬁeld and the magnetic
ﬁeld.
5.2-2 Reduce the FDTD scheme for the full Maxwell’s equations to one and
two dimensions. Derive the corresponding wave equations by eliminating
the magnetic (or the electric) ﬁeld.
5.2-3 How many time-levels of the electric and magnetic ﬁelds must be stored
in the computer’s memory for the FDTD scheme?
5.2-4 Derive the Yee scheme from the integral representation of Maxwell’s
equations.
5.2-5 Show that (5.27) can be derived from (5.15)–(5.20).
5.2-6 Derive the stability condition given the numerical dispersion relation.
Motivate the steps in your derivation.
5.3 Boundary Conditions for Open Regions
5.3 Boundary Conditions for Open Regions
The FDTD is often applied to microwave problems such as calculation of:
Radiation patterns from antennas
Radar cross sections (RCS) for diﬀerent targets, e.g., aircraft
These problems involve open regions, and in principle, the computational
domain extends to inﬁnity. Of course it is not practical to discretize an inﬁnite
region, and instead, special boundary conditions can be applied to terminate
the computational region. Such boundary conditions serve to absorb outgoing
waves, and are called absorbing boundary conditions (ABC). Then, the ﬁelds in
the near zone can be transformed to the far zone, several wavelengths or more
from the antenna, by means of a so-called near-to-far-ﬁeld transformation
(NTF). Figure 5.13 illustrates its use in an FDTD calculation of the radiation
pattern of an antenna.
Antenna
Near-to-far field transformation
                                                                                                                                                                                                                                                                                                                                                                                                            

















surface
Absorbing layer, e.g. PML
Perfect Electric Conductor
Fig. 5.13. Typical setup for computing the radiation pattern of an antenna with
the FDTD.
5.3.1 The Perfectly Matched Layer
A popular set of absorbing boundary conditions is the perfectly matched layer
(PML) invented by B´erenger [8]. The PML is a layer of artiﬁcial material
surrounding the computational region and designed to damp waves propagat-
ing in the normal direction. The region is then terminated by a PEC. If the
waves are suﬃciently damped out in the absorbing layer, very little reﬂection
will occur at this PEC surface. The thicker the absorbing layer is, the more
eﬃcient is the damping that can be achieved.
5 The Finite-Diﬀerence Time-Domain Method
Here, we indicate how B´erenger’s PML works. The basic idea behind the
method is to introduce both an electric conductivity σ and a magnetic con-
ductivity σ∗in the absorbing layer:
∂t + σE = ∇× H,
(5.39)
∂t + σ∗H = −∇× E.
(5.40)
One can deﬁne a wave impedance as the ratio of the transversal electric and
magnetic ﬁelds, and for such an artiﬁcial material, it takes the value
ZP ML =
µ0 + σ∗/jω
ϵ0 + σ/jω
1/2
For a wave that is normally incident on such a layer, the wave reﬂection
coeﬃcient is [4]
Γ0 = Z0 −ZP ML
Z0 + ZP ML
where Z0 ≡
µ0/ϵ0 is the wave impedance in free space. Evidently, if the
magnetic and electric conductivities are related as
(5.41)
we get ZP ML = Z0, and there is no reﬂection at any frequency.
For oblique incidence, things become more complicated, and it is harder to
avoid reﬂection. However, B´erenger found a trick that achieves this. It consists
in splitting each component of E and H into two parts, for instance, Ex =
Exy + Exz, according to the direction of the curl operator that contributes
to ∂E/∂t. Then, one uses nonzero σ and σ∗only for the derivative in the
direction normal to the absorbing layer.
As an example, let us assume that the PML has ˆz as the normal direction.
The two equations for Ex and Ey are split into four:
ϵ∂Exy
= ∂(Hzx + Hzy)
(5.42)
ϵ∂Exz
= −∂(Hyz + Hyx)
−σzExz,
(5.43)
ϵ∂Eyz
= ∂(Hxy + Hxz)
−σzEyz,
(5.44)
ϵ∂Eyx
= −∂(Hzx + Hzy)
(5.45)
The evolution equation for Ez is not modiﬁed for a layer with ˆz as normal.
The magnetic ﬁeld is treated in a similar way. What is achieved with this
5.3 Boundary Conditions for Open Regions
trick is that the layer modiﬁes the propagation only in the z-direction, which
is the normal direction of the PML, not in the tangential directions x and
y. Therefore, no reﬂection occurs even for waves obliquely incident on the
B´erenger PML.
In practice, some reﬂection occurs if σ varies strongly on the scale of
the grid. Therefore, one often chooses proﬁles for the conductivity, such as
parabolic σ(z) = σ0[(z −z0)/Lz]2, for a layer that extends from z = z0 to
z = z0+Lz. Such layers are very good absorbers; 6–8 cells can give a reﬂection
coeﬃcient of −60 to −80 dB.
The PML works well, even when placed very close to the radiating struc-
ture or scatterer. This means that it is eﬀective in decreasing the number of
cells and consequently reducing the computational cost.
There are alternatives to B´erenger’s PML. One that gives the same dis-
persion properties, without splitting the ﬁeld components, uses anisotropic,
tensorial
=ϵr and
µr [52]:
=ϵr=
1 −jσ/ωϵ
1 −jσ/ωϵ
(1 −jσ/ωϵ)−1
(5.46)
This involves modiﬁcations of the time-stepping.
5.3.2 Near-to-Far-Field Transformation
Figure 5.13 shows a typical setup for computing the radiation pattern of an
antenna. The result of main interest is the ﬁelds in the far zone, several wave-
lengths from the antenna. This can be computed without extending the com-
putational domain to the far zone by using a near-to-far-ﬁeld transformation
(NTF) close to the antenna and adding an ABC just outside the NTF surface.
Formulas for the NTF can be found in the book on FDTD by Taﬂove [75].
Without going through the derivation, we state the formulas for the far ﬁeld in
frequency domain based on the Fourier transform of the near ﬁeld computed
by the FDTD scheme. (The Fourier transform can be computed as part of the
time-stepping procedure for selected frequencies.) The ﬁeld can be expressed
in terms of the electric (A) and magnetic (F ) vector potentials as
E = −jω
k2 ∇× ∇× A −1
∇× F ,
H = −jω
k2 ∇× ∇× F + 1
∇× A.
The potentials can be calculated from the equivalent electric current Js =
ˆn × H and magnetic current M s = −ˆn × E on the NTF surface (ˆn denotes
the outward normal of the NTF surface ∂Ω):
5 The Finite-Diﬀerence Time-Domain Method
A = µ0
Js(r′)exp(−jkR)
dS′,
F = ϵ0
M s(r′)exp(−jkR)
dS′.
(5.47)
Here R denotes the distance between the source point, r′, and the point
where we observe the ﬁeld, r. For large distances, one can approximate R
in the denominators of (5.47) as a constant, R0, and in the argument of the
exponential as R ≈R0 −r′ cos ψ, where ψ is the angle between r and r′. The
ﬁelds in the radiation zone are
E ≈jω(ˆr × ˆr × A + Z0ˆr × F ),
H ≈jω
ˆr × ˆr × F −1
ˆr × A
Review Questions
5.3-1 What is meant by an open-region problem and how are these problems
handled by FDTD programs?
5.3-2 Use the wave impedance to explain why a normally incident wave is not
reﬂected by the PML at any frequency.
5.3-3 How did B´erenger avoid reﬂections by the PML for oblique incidence?
5.3-4 How are the electric and magnetic conductivity proﬁles usually chosen
for the PML in an FDTD implementation? What reﬂection coeﬃcients
can be achieved with a PML that is 6–8 cells thick?
5.3-5 Outline a technique for the computation of the ﬁelds in the far zone given
an FDTD solution in the near zone. Mention some practical situations in
which this technique can be used.
Summary
The FDTD is a standard tool for microwave problems in which the geo-
metrical dimensions are comparable to the wavelength. Its main advantage
is that it is both eﬃcient and simple to implement.
Although the FDTD scheme is very popular, the method suﬀers from some
drawbacks:
A main drawback of the FDTD is the way it deals with curved and
oblique boundaries, where the standard FDTD solution, known as
“staircasing,” does not give very accurate results. In this respect, ﬁnite
elements can do much better.
Another disadvantage of the FDTD (in common with ﬁnite elements)
is that the phase error can become signiﬁcant when the computational
domain is many wavelengths. In this respect, the method of moments
is better.
5.3 Boundary Conditions for Open Regions
Furthermore, the time-step is limited by ∆t ≤h/(c
3), which means
that the FDTD cannot be used for eddy current problems.
The time-dependent system of two ﬁrst-order equations (Faraday’s and
Amp`ere’s laws) allows for staggering in both space and time. The dis-
cretization of this system exploits centered diﬀerences and oﬀers explicit
time-stepping. In 1D, we discretize
= −µ∂Hy
∂t ,
−∂Hy
= ϵ∂Ex
∂t ,
with Ex = Ex(r, n) and Hy = Hy(r+ 1
2, n+ 1
2), where r is an integer space
index and n is an integer time index. [The corresponding wave equation
∂2E/∂t2 = c2∂2E/∂x2 can be treated by centered second-order diﬀerences
and explicit time-stepping.]
Staggering in three dimensions:
Ex|n
p+ 1
2 ,q,r,
Ey|n
p,q+ 1
2 ,r,
Ez|n
p,q,r+ 1
n+ 1
p,q+ 1
2 ,r+ 1
n+ 1
p+ 1
2 ,q,r+ 1
n+ 1
p+ 1
2 ,q+ 1
2 ,r.
Electric ﬁeld components are placed on the midpoint of the edges aligned
with the ﬁeld components. Magnetic ﬁeld components are centered on the
surfaces normal to the ﬁeld components.
Numerical dispersion relations (relations between ω and k for E
exp[j(ωt−k ·r)]) are derived from the ﬁnite-diﬀerence equations. In three
dimensions, we get
sin2(ω∆t/2)
(c∆t)2
= sin2(kx∆x/2)
(∆x)2
+ sin2(ky∆y/2)
(∆y)2
+ sin2(kz∆z/2)
(∆z)2
The stability condition (Courant condition) c∆t/h < 1/√n in n dimen-
sions. This can be derived from the numerical dispersion relation.
Several extensions of the FDTD, such as absorbing boundary conditions,
near-to-far-ﬁeld transformation, and subgrid models for thin wires and
slots have been developed, and these allow the FDTD to be applied to a
wide range of problems.
Problems
P.5-1 For ﬁnite diﬀerence computations on unbounded domains, the ﬁnite
grid must be terminated by boundary conditions that mimic a free-space
problem. Use (1.13) to derive boundary conditions for (5.2) when R = 1.
P.5-2 Consider a speciﬁc point z0 at a speciﬁc time t0 in Figure 5.1. A pertur-
bation of the ﬁeld at this point and time inﬂuences the ﬁeld at later times
5 The Finite-Diﬀerence Time-Domain Method
t > t0 in the region z0−c(t−t0) < z < z0+c(t−t0). Similarly, the ﬁeld val-
ues at earlier times t < t0 within the region z0−c(t0−t) < z < z0+c(t0−t)
will have an inﬂuence on the ﬁeld at z = z0 and t = t0, and this region is
referred to as the light-collecting sector. Relate the stability condition for
the 1D FDTD scheme to the light-collecting sector. What happens when
the light-collecting sector covers a larger angle than the stencil in (5.2)?
P.5-3 Show that the dispersion relation of the 1D wave equation (5.1) can be
expanded as
ω = ck
1 −(k∆z)2
(1 −R2) + O((k∆z)4)
(5.48)
How many points per wavelength are required to get the frequency correct
(a) to 1%, (b) to 0.1% if R = 1/
P.5-4 Consider the case in which the coupled ﬁrst-order system shown in
(5.12) and (5.13) is applied to solve a problem with continuously varying
material parameters. Where should ϵ(z) and µ(z) be evaluated on the
grid? How would the corresponding problem be treated when the wave
equation
µ(z)
−ϵ(z)∂2Ex
is used instead? Where should ϵ(z) and µ(z) be evaluated in this case?
P.5-5 Consider the case in which the coupled ﬁrst-order system shown in
(5.12) and (5.13) is applied to a problem with piecewise continuous mate-
rials; i.e., there are material discontinuities. Let the grid points associated
with an electric ﬁeld tangential to the material interface be placed on
the material interface. How should ϵ(z) and µ(z) be evaluated in order
to maintain an O(h2) error? How would the corresponding problem be
treated when the wave equation
µ(z)
−ϵ(z)∂2Ex
is used instead? Where are ϵ(z) and µ(z) evaluated in this case? Can
optimal convergence be maintained?
P.5-6 Suppose that a current-carrying and electrically perfectly conducting
wire with radius r0 ≪h, where h = ∆x = ∆y = ∆z denotes the grid spac-
ing, runs along the z-axis. Use the near-ﬁeld approximations Hϕ ∝1/r
and Er ∝1/r (in cylindrical coordinates) to derive appropriate diﬀerence
approximations taking into account the wire.
P.5-7 Maxwell’s equations can be written in terms of the scalar potential φ
and the vector potential A:
E = −∇φ −∂A
∂t ,
B = µH = ∇× A.
How should the potentials be placed on the grid in order to match Yee’s
locations for the ﬁelds?
5.3 Boundary Conditions for Open Regions
P.5-8 In two dimensions (say the solution is independent of z), one can sep-
arate electromagnetic ﬁelds into TE components, with Ez = 0, and TM,
with Hz = 0. The simplest way to compute these is to use the wave equa-
tions for Hz and Ez, respectively, in two dimensions. However, it is also
possible to describe TE polarization by a set of ﬁrst-order equations for
Ex, Ey, and Hz, while TM polarization can be described by ﬁrst-order
equations for Hx, Hy, and Ez. Write down the relevant sets of equations
and show how suitable staggered ﬁnite diﬀerence schemes can be found,
e.g., as subsets of the 3D Yee scheme.
P.5-9 Derive the ﬁnite diﬀerence equation for updating Ex|p+ 1
2 ,q,r starting
from the integral form of Amp`ere’s law (5.22).
P.5-10 Show that about 11 points per wavelength gives 1% error in the numer-
ical dispersion relation for a cubic grid by Taylor expanding the disper-
sion relation (5.32) for ω2(k) to order k4h4 and using the approximation
ω2 = c2(k2
x + k2
y + k2
z) in the term ∝ω4. When the time-step is at the
stability limit of (5.34), the result can be written
c2 = k2
x + k2
y + k2
z −h2
72[(k2
x −k2
y)2 + (k2
y −k2
z)2 + (k2
z −k2
x)2].
[Thus, when the time-step is at the stability limit, only solutions that
propagate maximally obliquely have zero dispersion. In all other direc-
tions, the spatial dispersion dominates, and the phase speed is below c.
For smaller time steps, the phase speed is less than c in all directions.]
P.5-11 The curl-curl equation (5.28) also has electrostatic solutions that are
linear functions of time, i.e. E(r, t) = t∇φ(r ). Can such a solution appear
in an FDTD simulation without sources?
P.5-12 Does the FDTD scheme preserve the electric charge if there are no
electric currents?
P.5-13 Carry out the derivation of the numerical dispersion relation for the
3D FDTD scheme by rewriting (5.28) in matrix form and setting the
determinant of this matrix to zero.
P.5-14 Derive the impedance ZP ML from (5.39)–(5.40) by assuming that the
ﬁeld components vary as exp(−jk·r) and that E and H are perpendicular
to k.
P.5-15 Consider the computation of an electrical motor at f = 50 Hz and a
spatial resolution of h = 5 mm. How many time-steps are needed if we
want to time-step 5 wave periods, or 0.1 s?
P.5-16 We note that 1% relative phase error is obtained with about 10 points
per wavelength. How much does the computation time for a 3D problem
increase if we want to reduce the relative phase error by a factor 10?
5 The Finite-Diﬀerence Time-Domain Method
Computer Projects
C.5-1 Propose some diﬀerent ways of visualizing the numerical dispersion re-
lation (5.32). Write a program that given the diﬀerent parameters needed
implements your ideas for the visualization. Experiment with diﬀerent res-
olutions, spatial and temporal. It can be beneﬁcial to use kx = k sin θ cos φ,
ky = k sin θ sin φ, and kz = k cos θ. How do the results depend on the di-
rection of propagation?
C.5-2 Implement the 1D FDTD scheme for 0 ≤z ≤a; see Section 5.2.1.
Extend your program to include the losses shown in (5.39)–(5.40). Let
ϵ = ϵ0, µ = µ0 and introduce a conductive region for a −w ≤z ≤
a where the losses satisfy the condition shown in (5.41) and w is the
width of the conductive region. Where should σ(z) and σ∗(z) be evaluated
on the staggered grid? Set up a numerical experiment so that you can
study the reﬂection coeﬃcient for the electric ﬁeld Ex(z, t), which satisﬁes
the boundary conditions Ex(0, t) = g(t) and Ex(a, t) = 0. Let g(t) =
exp[−(t −t0)2/d2
0] sin[2πf0(t −t0)] and choose appropriate values for t0,
d0, and f0. Experiment with diﬀerent conductivity proﬁles σ(z) and σ∗(z)
given by (5.41). Try a constant conductivity proﬁle and optimize the value
σconst for the conductivity. A very common choice is the quadratic proﬁle
σ(z) = σmax[(z −(a −w))/w]2, where σmax is a constant to be optimized.
Plot the reﬂection coeﬃcient as a function of σconst and σmax. Explain
your ﬁndings. What happens if the condition (5.41) is violated? How does
the reﬂection coeﬃcient depend on frequency?
C.5-3 Write a program that implements the 2D FDTD scheme. Use it to
compute the resonant frequencies of a circular cavity with metal bound-
aries. How do you represent the circular boundary on the Cartesian grid?
How do you excite the problem? Suggest and implement some diﬀerent
excitations and compare the approaches.
C.5-4 Modify the program in Section 5.2.3 so that inhomogeneous materials
ϵ(r) and µ(r) can be considered. Extend the implementation so that also
a source current J(r) can be included. Let the electric and magnetic ﬁeld
be identically zero as an initial condition. Is the condition of solenoidal
magnetic ﬂux density (1.4) preserved numerically at all times? Does the
solution computed by your program satisfy the equation of continuity for
electric charge?
The Finite Element Method
The ﬁnite element method (FEM) is a standard tool for solving diﬀerential
equations in many disciplines, e.g., electromagnetics, solid and structural me-
chanics, ﬂuid dynamics, acoustics, and thermal conduction. Jin [38, 39] and
Peterson [51] give good accounts of the FEM for electromagnetics. More math-
ematical treatments of the same topic are given in [45, 11]. This chapter gives
an introduction to FEM in general and FEM for Maxwell’s equations in par-
ticular. Practical issues, such as how to handle unstructured grids and how to
write (simple) FEM programs, will be discussed in some detail.
A very strong point of the FEM, and the main reason why it is a favorite
method in many branches of engineering, is its ability to deal with complex ge-
ometries. Typically, this is done using unstructured grids, which are commonly
referred to as (unstructured) meshes. These meshes may consist of triangles
in two dimensions and tetrahedra in three dimensions. However, there are
several types of element shapes, as shown in Figure 6.1: triangles and quadri-
laterals in two dimensions, tetrahedra, prisms, pyramids, and hexahedra in
three dimensions.
Unstructured meshes with, for instance, tetrahedra allow good represen-
tations of curved objects, which are hard to represent on the Cartesian grids
used by ﬁnite diﬀerence methods. Moreover, unstructured meshes allow for
higher resolution locally in order to resolve ﬁne structures of the geometry
and rapid variations of the solution. Another nice property of the FEM is
that the method provides a well-deﬁned representation of the sought func-
tion everywhere in the solution domain. This makes it possible to apply many
mathematical tools and prove important properties concerning stability and
convergence.
A disadvantage of the FEM, compared to the FDTD, is that explicit for-
mulas for updating the ﬁelds in time-domain simulations cannot be derived in
the general case. Instead, a linear system of equations has to be solved in order
to update the ﬁelds. Consequently, provided that the same number of cells are
used for the two methods, the FEM requires more computer resources, both
in terms of CPU time and memory.

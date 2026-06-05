# Bondeson《Computational Electromagnetics》第4章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 53-71 of 231 (231 total)

---

## Eigenvalues

4 Eigenvalues
A × 1
µ(∇× B)
µ(∇× A) · (∇× B) −A · ∇× 1
µ∇× B.
(4.4)
For all electric ﬁelds E1 and E2 satisfying the boundary condition, ˆn×E = 0,
(4.4) gives
E1 · ∇× 1
µ∇× E2dV =
µ∇× E1 · ∇× E2dV
E2 · ∇× 1
µ∇× E1dV,
(4.5)
where we have applied integration by parts twice. Integrating (4.2), multiplied
by the complex conjugate of E over Ω, and integrating by parts once, we
obtain ω2 
Ωϵ|E|2dV =
Ωµ−1|∇×E|2dV . This gives the following expression
for the eigenvalue:
ω2 =
Ωµ−1|∇× E|2dV
Ωϵ|E|2dV
(4.6)
which is manifestly real and nonnegative. Thus, the eigenfrequencies ω are real
for any lossless region bounded by perfect conductors. Damping can appear
if there is dissipation of energy, for example from regions with ﬁnite electrical
conductivity, or if the region is not completely enclosed by a perfect conductor.
Review Questions
4.1-1 What is an eigenvalue problem? What does the solution consist of and
physically correspond to? To what extent is the solution uniquely deﬁned?
4.1-2 What is required for an operator to be self-adjoint?
4.1-3 Show that (4.5) is valid.
4.1-4 Show that the eigenfrequencies ω are real for any lossless region bounded
by perfect conductors. What are the physical implications of this result?
4.2 Model Problems
In the previous section we showed that Maxwell’s equations are self-adjoint in
the absence of losses, and that this leads to real eigenfrequencies. Self-adjoint
equations occur in many branches of science and technology. One example is
the Schr¨odinger equation, where real eigenvalues describe well-deﬁned energy
levels of states with inﬁnite lifetime. Another example is provided by the
equations of linear elasticity, which have many properties in common with
Maxwell’s equations. This similarity comes from the fact that both can be
written as a vector equation with second-order derivatives in time and space.
The only diﬀerence is that the curl-curl operator of the Maxwell equations is
replaced by another second-order vector operator, involving the modulus of
elasticity for bulk compression and shearing. Because of the many similarities
4.3 Frequency-Domain Eigenvalue Calculation
between the two ﬁelds, it has been possible to carry over techniques originally
developed in computational mechanics (see, e.g., [36]) to CEM.
The self-adjoint curl-curl equation (4.2) leads us to consider eigenvalue
problems of the type
L[f] = −ω2f
in Ω
(4.7)
together with a suitable boundary condition on ∂Ω. We will assume that L is a
linear self-adjoint operator with nonpositive eigenvalues. As a simple example
to illustrate general principles, we will study the 1D Helmholtz equation:
dx2 = −k2f,
0 < x < a,
f(0) = f(a) = 0.
(4.8)
This equation models many 1D wave phenomena, not only in electromagnet-
ics. We will use it to introduce both frequency- and time-domain techniques
that will be used later to determine eigenfrequencies of more complex electro-
magnetic systems in two and three dimensions.
The eigenvalue problem (4.8) is easy to solve analytically. The solutions of
the diﬀerential equation are of the form f = A cos kx+B sin kx. The boundary
condition f(0) = 0 gives A = 0, and then f(a) = 0 gives sin ka = 0. Therefore,
the wavenumber k can take the following values:
km = mπ
m an integer,
so the eigenvalues −k2
m = −m2π2/a2 are all real and negative. The three
lowest eigenfunctions, or eigenmodes, are shown in Figure 4.1.
Review Question
4.2-1 Calculate analytical eigenvalues and eigenfunctions to the eigenvalue
problem d2f/dx2 = −k2f with f(0) = f(a) = 0.
4.3 Frequency-Domain Eigenvalue Calculation
Frequency-domain eigenvalue problems of the form L[f] = λf are generally
transformed into corresponding algebraic eigenvalue problems of the form
Af = λf by, for example, a ﬁnite diﬀerence approximation. Therefore, the
numerical solution of a frequency-domain eigenvalue problem involves the so-
lution of an algebraic eigenvalue problem.
4.3.1 MATLAB: The 1D Helmholtz Equation
To discretize the 1D Helmholtz equation (4.8) by ﬁnite diﬀerences, we divide
the interval [0, a] into N subintervals of equal length h = a/N. The simplest
ﬁnite diﬀerence approximation of (4.8) is
4 Eigenvalues
−1.5
−0.5
x/a [−]
Amplitude [−]
m = 1
m = 2
m = 3
Fig. 4.1. The three lowest eigenmodes of the 1D Helmholtz equation with f = 0
on the boundaries.
fi−1 −2fi + fi+1
= −k2fi,
i = 1, 2, . . . , N −1.
(4.9)
The boundary conditions are f0 = fN = 0, so there is no reason to include f0
and fN as unknowns. Equation (4.9) can be written as a linear system with
an (N −1) × (N −1) matrix A:
Af = λf.
Note that the matrix A is tridiagonal, with nonzero elements on the main
diagonal and one lower and one upper subdiagonal; for six interior points, it
A = 1
−2 1
1 −2 1
1 −2 1
1 −2 1
1 −2 1
1 −2
When n is large, A consists mostly of zeros, and this can be exploited by sav-
ing the matrix in sparse form (see MATLAB example below). Note that when
the right-hand side is as simple as in (4.9), the physical eigenvalues −k2 are
simply the eigenvalues of the matrix A. These eigenvalues can be computed
with the MATLAB routine eig, which computes all eigenvalues and corre-
sponding eigenvectors of an algebraic eigenvalue problem. We will use this
4.3 Frequency-Domain Eigenvalue Calculation
routine without discussing how it ﬁnds the eigenvalues. The following MAT-
LAB program computes the eigenvalues, that correspond to wavenumbers, for
the discretized 1D Helmholtz equation.
% --------------------------------------------------------------
% Compute eigenvalues of 1D Helmholtz equation using FD
% --------------------------------------------------------------
function k = HFD1D(a, N)
% Arguments:
a = length of interval
N = number of subintervals (equal length)
% Returns:
k = eigenvalues
h = a/N;
% Grid size
A = spalloc(N-1, ...
% Allocate sparse matrix
N-1, ...
% with 3*(N-1) nonzeros
3*(N-1));
d = -2/hˆ2;
% Value of diagonal entries
s = 1/hˆ2;
% Value of upper and lower
% diagonal entries
% Initialize the diagonal entries
for i = 1:N-1
A(i,i) = d;
% Diagonal entries
% Initialize the upper and lower diagonal entries
for i = 1:N-2
A(i,i+1) = s; % Upper diagonal entries
A(i+1,i) = s; % Lower diagonal entries
% Computing the eigenvalues
lambda = eig(A);
k = sqrt(sort(-lambda));
For this small example, we can rely on the MATLAB routine eig. It should be
noted that eig is limited to systems with at most a few thousand unknowns.
This means it is very useful in one dimension, and works for moderate-sized 2D
problems. In three dimensions, more powerful routines, such as the MATLAB
routine eigs, are generally needed.
We calculate the ﬁrst two numerical wavenumbers k on the interval [0, π]
for four diﬀerent resolutions. The analytical results are k = 1, 2, 3, . . ., and the
numerical results are shown in Table 4.1.
Plots of km versus hp show a straight line when p = 2, which means that
the convergence is quadratic. Extrapolation of the ﬁrst eigenvalue to zero
cell size using polyfit gives the following values for k1: linear extrapolation
4 Eigenvalues
N [-]
h [m]
k1 [1/m]
k2 [1/m]
0.1000 0.99589 27352 4357 1.96726 32861 6693
0.0500 0.99897 22332 4854 1.99178 54704 8714
0.0333 0.99954 31365 0068 1.99634 65947 4160
0.0250 0.99974 29988 6918 1.99794 44664 9703
Table 4.1. The two lowest wavenumbers from FD discretizations with diﬀerent
resolutions.
0.99999 93697 896, quadratic 0.99999 99999 437, and cubic 0.99999 99999 997,
which is very close to the exact value 1. For the second eigenvalue, linear
extrapolation gives 1.99997 98747 162, quadratic 1.99999 99928 090, and cubic
1.99999 99999 989. Thus, the two lowest eigenvalues could be computed with
12-digit accuracy using the cubic ﬁt for extrapolation, even though the com-
putations have only about 4-digit accuracy. The accuracy of the extrapolated
values may at ﬁrst be surprising, but it is typical for problems where the so-
lution is completely regular, i.e., has bounded derivatives of arbitrarily high
order. However, if the problem contains some singular behavior, caused for
instance by a reentrant 270o-degree corner, as in Figure 3.1, or a tip in three
dimensions, the derivatives of the solution will diverge at the corner, the order
of convergence decreases, and extrapolation becomes more diﬃcult.
The error is larger for the second eigenmode. The second eigenmode os-
cillates twice as fast and needs twice the resolution to be computed with the
same accuracy as the ﬁrst, as is conﬁrmed by Table 4.1.
Review Questions
4.3-1 Use ﬁnite diﬀerences to discretize the eigenvalue problem d2f/dx2 =
−k2f with f(0) = f(a) = 0. Write down the corresponding matrix eigen-
value problem.
4.3-2 What is the order of convergence for k in (4.9)?
4.3-3 Why is the error, in general, larger for higher eigenmodes? What situ-
ations could change this?
4.4 Time-Domain Eigenvalue Calculation
One common way of determining eigenfrequencies in CEM is to time-step a
solution, using for example a ﬁnite diﬀerence program, record the ﬁeld at some
location, and then Fourier transform this signal to locate its main frequency
components. This technique can be used for more general methods than the
ﬁnite diﬀerences. It can be used to ﬁnd the eigenvalues of any spatial operator
L with real and negative eigenvalues,
L[f] = −ω2f.
(4.10)
4.4 Time-Domain Eigenvalue Calculation
Equation (4.10) is written in such a form that it is the frequency-domain form
of the time-domain equation
∂t2 = L[f],
(4.11)
which is, most likely, what the eigenvalue problem (4.10) was derived from.
The simplest time-discretization of (4.11) is
f (n+1) −2f (n) + f (n−1)
(∆t)2
= L[f (n)],
(4.12)
where ∆t is the time step. An important advantage of this formulation is that
the time-stepping is explicit, that is, no matrix inversion is needed to compute
f (n+1):
f (n+1) = 2f (n) −f (n−1) + (∆t)2L[f (n)].
(4.13)
Such time-stepping schemes, often referred to as “leap-frog,” are very eﬃcient,
and allow determination of the complete eigenvalue spectrum of (4.10). An
important issue for explicit time-stepping schemes is how to choose the time-
step ∆t. This is mainly determined by stability.
4.4.1 Stability Analysis
Before working out a speciﬁc example, we discuss how one can analyze the
stability of a time-stepping algorithm such as (4.13). The following technique
is known as von Neumann stability analysis.
The analysis is based on the fact that any discrete time equation, which has
no explicit time dependence, has solutions of the form f (n) = fωρn, that is, ge-
ometrical sequences in discrete time. This is true even if the equation involves
space-dependent coeﬃcients, as long as it has no explicit time-dependence.
Here, ρ is called the ampliﬁcation factor of the eigenmode fω, and stability
requires |ρ| ≤1 for all eigenmodes. Substituting f (n) = fωρn into (4.13), and
using L[fω] = −ω2fω, we obtain a quadratic equation for the ampliﬁcation
factor
ρ2 −[2 −(ω∆t)2]ρ + 1 = 0
(4.14)
with the solutions
ρ = 1 −1
2(ω∆t)2 ± jω∆t
1 −1
4(ω∆t)2.
(4.15)
If (ω∆t)2 ≤4, there are two complex conjugate solutions such that
|ρ|2 = (Reρ)2 + (Imρ)2 = 1.
On the other hand, if (ω∆t)2 > 4, there are two real solutions, whose product
is unity, so one of them has modulus larger than 1. Figure 4.2 shows how the
roots move in the complex plane as ω∆t varies.
4 Eigenvalues
−2.5
−1.5
−0.5
−1.5
−0.5
Re(ρ) [−]
Im(ρ) [−]
instability for ω∆t > 2
ω∆t = 2
ω∆t = 0
Fig. 4.2. Trajectories in the complex plane of the two roots for the ampliﬁcation
factor ρ in (4.15).
The roots stay on the unit circle |ρ| = 1 as long as |ω∆t| ≤2, but when
|ω∆t| > 2, one root has modulus larger than unity. Therefore, if |ω∆t| > 2, the
solution will grow exponentially in time, and the scheme for time-stepping is
unstable. Thus, the explicit time-stepping scheme in (4.13) has a stability limit
for the time-step: ∆t ≤2/|ω|. Since this has to hold for all the eigenmodes of
(4.10), the condition on the time-step for the explicit scheme is
∆t ≤
|ωmax|.
(4.16)
This means that the time-step times the highest eigenfrequency fmax =
ωmax/2π should be at most 1/π.
If we apply this stability limit to the operator L = d2/dx2 discretized on a
uniform grid with cell size h, the largest numerical eigenvalue is ω2
max = 4/h2
[see (3.17)]. Thus, ωmax = 2/h, and stability requires ∆t ≤2/ωmax = h.
We conclude that the time-step for our simple explicit scheme for the wave
equation ∂2f/∂t2 = ∂2f/∂x2 should not be larger than the space step, for
stability reasons.
We can also see how well the time-stepping reproduces the true oscillation
frequency. The ampliﬁcation factor per time-step ought to be
exp(±jωt) = 1 ± jωt −1
2(ω∆t)2 ∓j
6(ω∆t)3 + · · · ,
whereas (4.15) gives
4.4 Time-Domain Eigenvalue Calculation
ρ = 1 ± jωt −1
2(ω∆t)2 ∓j
8(ω∆t)3 + · · · .
The diﬀerence between ρ and exp(jωt) is ±j(ω∆t)3/24, which corresponds to
a relative frequency error of (ω∆t)2/24.
The von Neumann stability analysis is closely related to the analysis in
Section 3.2.3. To see the connection, assume that the solution f of the time-
discretized problem varies harmonically in time, f ∝exp(jΩt), i.e., f (n) ∝
exp(jnΩ∆t). We will examine how the frequency Ωof the time-discretized
solution is related to ω of the frequency-domain eigenvalue problem L[f] =
−ω2f. [Of course, this is just redoing the analysis leading to (4.15), replacing
the ampliﬁcation factor ρ by exp(jΩt).] Using the same rewrite for the second
derivative as in (3.17), we obtain
(∆t)2 sin2 Ω∆t
= ω2
(4.17)
for the frequencies Ωgenerated by the leap-frog time-stepping. [This is also
the same as the numerical second-order derivative in (3.18).] In order for (4.17)
to have real solutions for Ω, ω∆t must not exceed 2 for any ω.
In the FEM chapter, we will also study implicit time-stepping schemes,
which make it possible to remove the limit on the time-step. The price to pay
for this is that one has to solve a system of equations to update the solution
at each time step. Also, the accuracy may be poor if the time-step becomes
too large.
4.4.2 MATLAB: The 1D Wave Equation
As a simple illustration of how to extract spectral information by explicit
time-stepping, we seek the spectrum −ω2 of the operator L = ∂2/∂x2 on the
interval 0 < x < a with the boundary conditions f(0, t) = f(a, t) = 0. The
true eigenfrequencies are
ωm = mπ
m = 1, 2, . . . .
The spectrum of L can be found by solving the wave equation
∂t2 = ∂2f
∂x2 ,
0 < x < a,
f(0, t) = f(a, t) = 0.
(4.18)
We use the simplest ﬁnite diﬀerence scheme:
f (n+1)
= 2f (n)
−f (n−1)
 ∆t
2 
f (n)
i+1 + f (n)
i−1 −2f (n)
(4.19)
We will write this as a MATLAB function that records two signals [f(t) at
two locations, the midpoint and a point close to the left boundary] and stores
4 Eigenvalues
them in arrays to be analyzed afterwards. More than one signal is recorded
because some eigenmodes can be undetected if the eigenfunction f has a node
(i.e., zero amplitude) at the “detector” location. An eigenmode may also be
undetected if the initial condition does not excite it at suﬃcient amplitude.
% --------------------------------------------------------------
% Time step 1D wave equation using two time-levels f0 & f1
% --------------------------------------------------------------
function [omega, s1, s2] = Wave1D(a, time, nx)
% Arguments:
= the length of the interval
time
= the total time interval for the simulation
= the number of subintervals in the domain (0,a)
% Returns:
omega = the angular frequencies
= the complex Fourier transform of data at x = a/5
= the complex Fourier transform of data at x = a/2
= randn(nx+1, 1); % Initialize with random numbers
f0(1,1)
= 0;
% Boundary condition at x = 0
f0(nx+1,1) = 0;
% Boundary condition at x = a
= randn(nx+1, 1); % Initialize with random numbers
f1(1,1)
= 0;
% Boundary condition at x = 0
f1(nx+1,1) = 0;
% Boundary condition at x = a
= a/nx;
% The cell size
d2tmax
= 1.9*dx;
% The time step must satisfy
% 2*dt < 2*dx for stability
ntime = round(time/d2tmax + 1);
% The number of time steps
dt = time/(2*ntime);
% The time step
% Initialize the coefficient matrix for updating the solution f
A = spalloc(nx+1,nx+1,3*(nx+1)); % Sparse empty matrix with
% 3*(nx+1) nonzero entries
for i = 2:nx
A(i,i)
= 2*(1-(dt/dx)ˆ2);
% Diagonal entries
A(i,i+1) = (dt/dx)ˆ2;
% Upper diagonal entries
A(i,i-1) = (dt/dx)ˆ2;
% Lower diagonal entries
% Time step and sample the solution
% Sample location #1 is close to the left boundary
% Sample location #2 is at the midpoint of the domain
for itime = 1:ntime % Every ’itime’ means two time steps ’dt’
= A*f1 - f0;
% Update
4.4 Time-Domain Eigenvalue Calculation
sign1(2*itime-1) = f0(round(1+nx/5));
% Sample at location #1
sign2(2*itime-1) = f0(round(1+nx/2));
% Sample at location #2
= A*f0 - f1;
% Update
sign1(2*itime)
= f1(round(1+nx/5));
% Sample at location #1
sign2(2*itime)
= f1(round(1+nx/2));
% Sample at location #2
% Compute the discrete Fourier transform of
% the time-domain signals
spectr1
= fft(sign1);
spectr2
= fft(sign2);
% In the MATLAB implementation of the function fft(),
% the first half of the output corresponds to positive frequency
s1(1:ntime) = spectr1(1:ntime);
s2(1:ntime) = spectr2(1:ntime);
% Frequency vector for use with ’s1’ and ’s2’
omega
= (2*pi/time)*linspace(0, ntime-1, ntime);
We call the routine by
[omega,s1,s2] = Wave1D(pi,200,30);
to compute the spectrum of the second derivative on the interval [0, π]. Figures
4.3 and 4.4 show the absolute values of s1 and s2 versus angular frequency.
The spectral peaks fall very close to integers, as they should. Because of the
spatial locations of the observation points, the even peaks are absent in s2 and
those divisible by 5 in s1. These are the eigenmodes that have zero amplitudes
(nodes) at the respective observation points.
A signiﬁcant advantage of such a time-domain calculation is that we can
ﬁnd the whole spectrum (except the few peaks that are accidentally missed)
from a single simulation.
4.4.3 Extracting the Eigenfrequencies
Let us brieﬂy consider how to extract the eigenfrequencies from a time-domain
simulation. We ﬁrst run the simulation and record the signals. The longer the
simulation is run, the sharper the spectral peaks become, and the better the
eigenfrequencies are determined, but the convergence of the estimated fre-
quencies is slow. One can see that when there is no damping, the estimates
are sensitive to how close the various frequency components are to making
an integer number of oscillations during the simulation. This is because the
fast Fourier transform (FFT), which is used to transform the recorded sig-
nal into the frequency domain, treats the signal as if it were periodic with
a period equal to the simulated time. If the time interval is not an integer
4 Eigenvalues
1000
1500
2000
ω [rad/s]
|s1| [−]
Fig. 4.3. Amplitude of Fourier coeﬃcient s1 (measured at one-ﬁfth from the left
boundary) versus angular frequency for the 1D wave equation. Every ﬁfth mode is
undetected because the detector is located at a node for the eigenfunction.
1000
1500
2000
2500
ω [rad/s]
|s2| [−]
Fig. 4.4. Amplitude of Fourier coeﬃcient s2 (measured at the midpoint of the
interval) versus angular frequency for the 1D wave equation. All modes with even
number are undetected because the detector is at a node for those modes.
4.4 Time-Domain Eigenvalue Calculation
number of wave periods, either the signal or its time derivative will have a
jump at the end of the time window, and this broadens the Fourier spectrum
of a sinusoidal signal. As an example, compare the spectrum obtained by
calling the time-stepping routine by Wave1D(pi,20*pi,30), which gives 10
(analytical) oscillation periods for the ﬁrst mode, and where all the low-order
modes make approximately an integer number of oscillations, with that ob-
tained from Wave1D(pi,21*pi,30), where the ﬁrst mode has 10.5 oscillation
periods and all the odd modes will be strongly broadened by the FFT. In the
ﬁrst case, where the low-order modes make an integer number of oscillations,
the FFT ﬁnds very sharp peaks for these modes, despite the rather short time
interval; see Figure 4.5. In the second case, see Figure 4.6, the odd modes,
with half-integer number of periods, are broad.
1000
1200
ω [rad/s]
|s1| [−]
Fig. 4.5. FFT spectrum for the 1D wave equation when the time interval is 10
periods for the lowest mode (and an integer number of modes for all the lowest
modes).
One way to avoid the dependence on how the time sequence is terminated
is to multiply the time signal by an exponential damping factor exp(−γt),
and choose γ such that γtmax is large enough, say in the range of 3 to 5.
(This makes the FFT an approximation of the Laplace transform.) Now the
FFT produces a cleaner spectrum. The frequencies can be extracted almost
automatically by ﬁtting the output from the FFT (Laplace transform) to a
so-called Pad´e approximation. This consists in ﬁtting the frequency response
by a ratio of polynomials
4 Eigenvalues
ω [rad/s]
|s1| [−]
Fig. 4.6. FFT spectrum for the 1D wave equation when the time interval is 10.5
periods for the lowest mode (and a half-integer number of modes for all the odd
modes).
s(ω) = P(ω)
Q(ω).
(4.20)
The idea behind this (which is correct only when the signal decays to zero at
the end of the recorded interval) is that we expect the Laplace transform to
consist of simple poles
s(ω) ≈
ω −ωn
(4.21)
and this pole expansion is a rational function of the same type as the Pad´e
approximation (4.20).
4.4.4 MATLAB: Pad´e Approximation
The following MATLAB function computes the coeﬃcients of P and Q and
then uses MATLAB’s residue function to ﬁnd the poles ωn and residues cn
in (4.21).
% --------------------------------------------------------------
% Pade approximation for s(omega)
% --------------------------------------------------------------
function [poles, res] = Pade(omega, s, l, n)
% Arguments:
omega = the array of the independent frequency
4.4 Time-Domain Eigenvalue Calculation
= the function of omega to be Pade approximated as
the ratio of polynomials P(omega)/Q(omega)
= discrete index of center frequency
= degree of polynomials P and Q
% Returns:
poles = the poles of the Pade approximation
= the residues of the Pade approximation
% Setup the matrix for computing coefficients of P and Q
A = zeros(2*n+1);
for i = 1:2*n+1
% Shift frequencies
oshift(i) = omega(l-1-n+i)-omega(l);
% P entries
for k = 1:n+1
A(i,k) = oshift(i)ˆ(k-1);
% Q entries
for k = 1:n
A(i,n+1+k) = -s(l-1-n+i)*oshift(i)ˆk;
% Q_0 set to 1
x(i) = s(l-1-n+i);
% Compute the coefficients
coef = (A\(x.’)).’;
for k = 1:n+1
P(k) = coef(n+2-k);
for k = 1:n
Q(k) = coef(2*n+2-k);
Q(n+1) = 1;
% Find the poles and the residues
[res, poles] = residue(P, Q);
poles
= poles + omega(l);
% Restore the frequency shift
Applying this routine to an approximate Laplace transform, one can make
the frequencies converge very well with about 10 periods of oscillation. A
standard method used for frequency determination in the literature is Prony’s
method; see for instance [75]. However, more modern techniques of signal
4 Eigenvalues
processing can be used to give much more eﬃcient extraction of frequencies,
in particular when the frequency spectrum is dense [62].
Review Questions
4.4-1 How are the eigenvalues extracted from a time-domain eigenvalue calcu-
lation? Can the corresponding eigenmodes be extracted in a simple way?
4.4-2 What considerations should be taken into account in selecting the time-
step ∆t?
4.4-3 What is an explicit time-stepping method?
4.4-4 Describe the meaning and the use of the ampliﬁcation factor in words.
4.4-5 How does the highest eigenfrequency relate to the maximal stable time-
step for (4.13)?
4.4-6 How well is the true oscillation frequency reproduced by (4.15)? Quan-
tify your answer.
4.4-7 How do the excitation and detector positions inﬂuence the frequency
spectrum computed from a time-domain method?
4.4-8 Why are the frequency estimates of the FFT sensitive to how close
the various undamped resonances are to making an integer number of
oscillations during the simulation?
Summary
The solution of the eigenvalue problem L[fm] = λmfm consists of pairs of
eigenvalues λm and eigenvectors fm, where the pairs typically are indexed
by an integer m. (Sometimes the subindex m is omitted in order to simplify
the notation.) Here, the operator L and boundary conditions are given. For
Maxwell’s equations, we have
∇× µ−1∇× Em = ω2
mϵEm,
where the eigenfunction is Em and the eigenvalue is ω2
For the 1D Helmholtz equation d2f/dx2 = −k2f on the interval 0 < x < a
with the boundary conditions f(0) = f(a) = 0, the eigenvalues are k2 =
(πm/a)2 with integer m = 1, 2, . . . for the continuous problem, and the
discretized problem has
k2 = 4
h2 sin2
πmh
for the cell size h and m = 1, 2, . . . , N, where N is the number of internal
nodes in the grid.
A time-domain computation of eigenvalues is based on the inverse Fourier
transform of L[f] = −ω2f, i.e., L[f] = ∂2f/∂t2, and a ﬁnite diﬀerence
discretization with respect to time gives
4.4 Time-Domain Eigenvalue Calculation
L[f (n)] = f (n+1) −2f (n) + f (n−1)
(∆t)2
The substitution f (n) = fωρn, where ρ is an ampliﬁcation factor and
L[fω] = −ω2fω, gives
ρ = 1 −1
2(ω∆t)2 ± jω∆t
1 −1
4(ω∆t)2.
We have |ρ| = 1 for ω∆t ≤2. If ∆t < 2/|ωmax|, no mode will grow, and
every mode is multiplied by a phase-factor in each time-step. Thus, stable
time-stepping is achieved for ∆t < 2/|ωmax|, where ωmax is the highest
eigenfrequency.
The output s(t) from a time-domain simulation can be represented by its
Fourier transform:
s(ω) ≈P(ω)
Q(ω) =
ω −ωn
Peaks in the spectrum of s(ω) fall close to the resonance frequencies ωn.
Problems
P.4-1 Calculate the eigenvalues k2 of the vector wave equation ∇× ∇× E =
k2E for a 2D rectangular cavity with PEC boundaries. Consider the two
cases with E = ˆzEz(x, y) and E = ˆxEx(x, y) + ˆyEy(x, y), where the
second case is easier to treat if it is reformulated in terms of the magnetic
ﬁeld.
P.4-2 Show that the eigenvalues of the discretized 1D Helmholtz equation
(4.9), for a = π, are
−k2 = −4
h2 sin2 mh
m = 1, 2, 3, . . . ,
and ﬁnd how the error in k depends on the mode number and resolution.
P.4-3 Let the electric ﬁeld be E = ˆzEz(x) for a 1D cavity with PEC walls
and constant µ and ϵ. Use the ﬁnite diﬀerence scheme and show that (4.6)
can be rewritten as
ω2 = 1
eTAe
eTe ,
where e is a vector with the electric ﬁeld at the interior grid points. Deter-
mine A and interpret the products eTAe and eTe in terms of a numerical
integration scheme.
P.4-4 In one dimension, Helmholtz equation gives L = d2/dx2. Find a nonzero
solution f that yields L[f] = 0 and solve (4.10) and (4.11) for that par-
ticular solution. Can this solution exist in a region of ﬁnite size, and if so,
what boundary conditions are satisﬁed by this solution?
4 Eigenvalues
P.4-5 Consider the questions in the previous exercise when the operator
L = d2/dx2 is discretized by ﬁnite diﬀerences. How do you treat the
boundary conditions so that the order of convergence associated with the
ﬁnite diﬀerence stencils of the interior grid points is preserved? How does
the discretized problem compare to its continuous counterpart? Does the
discretized problem have a nonzero solution f with L[f] = 0?
P.4-6 Discretize L = ∂2/∂x2 with ﬁnite diﬀerences so that the dominant term
in the error is O(h4) (more than three points are needed) and derive the
stability limit on ∆t for (4.13). Compare the stability limit with the case
in which the error is O(h2).
P.4-7 Compute the discrete Fourier transform of the signal sin(ωt) sampled
at t = n∆t, where n = 0, 1, . . . , N −1. Compare some arbitrarily chosen
value of ω with the special case ω = 2πq/(N∆t) for some integer q =
0, 1, . . . , N −1. How and why do these cases diﬀer?
P.4-8 For three resonances, rewrite (4.21) as a ratio of polynomials s(ω) =
P(ω)/Q(ω). Consider the output signal y(ω) = s(ω)x(ω), where x(ω)
is the input signal to the system. Use the inverse Fourier transform to
derive the time-domain expression for Q(ω)y(ω) = P(ω)x(ω). Interpret
your ﬁndings.
Computer Projects
C.4-1 The transverse electric (TE) modes and the corresponding eigenvalues
t for a closed metal waveguide satisfy
−∇2Hz = k2
t Hz in S,
ˆn · ∇Hz = 0 on L.
Similarly, the transverse magnetic (TM) modes and their eigenvalues k2
fulﬁll
−∇2Ez = k2
t Ez in S,
Ez = 0 on L.
Here, the metal boundary of the waveguide cross section is denoted by
L, and it encloses the interior S of the waveguide. Write a program that
solves for the eigenmodes and the eigenvalues based on a ﬁnite diﬀerence
discretization of the TE and TM problem for a waveguide with rectangular
cross section. The analytical eigenvalues are k2
t = (mπ/a)2 + (nπ/b)2 for
integers m and n excluding the combination m = n = 0 for the TE case
and mn = 0 for the TM case. Here, the rectangular cross section has
width a and height b.
C.4-2 Equation (4.2) with losses and constant permeability is given by ∇×
∇× E = µ(ω2ϵ −jωσ)E, and for a problem with E = ˆzEz(x, y), we get
4.4 Time-Domain Eigenvalue Calculation
−∇2Ez = µ(ω2ϵ −jωσ)Ez,
which is a nonlinear eigenvalue problem in ω. Rewrite this problem to a
linear eigenvalue problem in terms of Ez and ωEz. Implement a ﬁnite-
diﬀerence algorithm and solve for the resonance frequencies and quality
factors of a square cavity with a boundary of a PEC. For constant ma-
terial parameters, derive the analytical eigenfrequencies and compare the
numerical and analytical results. How is the spectrum inﬂuenced by losses?
Explore the case in which σ > 0 in a part of the domain and study the
dependence of the lowest eigenmodes as a function of σ. Try to explain
your ﬁndings.
The Finite-Diﬀerence Time-Domain Method
The ﬁnite-diﬀerence time-domain method, or FDTD for short, is one of the
most popular computational methods for microwave problems; it is simple to
program, highly eﬃcient, and easily adapted to deal with a variety of prob-
lems. A major weakness of the method lies in the way it deals with boundaries
that are not aligned with the Cartesian grid: for oblique boundaries, FDTD
programs typically resort to the “staircase approximation.” The error due to
the staircase approximation can be diﬃcult to assess, but some examples can
be found in the literature [13, 60]. The ﬁnite element method (FEM), which
will be discussed in Chapter 6, is better suited for problems with oblique and
curved boundaries and ﬁne structures that may need higher resolution locally.
However, the FDTD allows for explicit time-stepping, and this makes it much
more eﬃcient than time-domain FEM, which in general is implicit (i.e., a
system of equations must be solved at each time step). Another advantage
of the FDTD is that no matrix has to be stored. This reduces memory con-
sumption and makes it possible to solve problems with a very large number
of unknowns.
The FDTD has a time-step limit ∆t < h/c
3 in three dimensions, where
∆t is the time-step, h is the cell size, and c is the speed of light (in vacuum,
the speed of light is c0 = 299 792 458 m/s). This is a serious limitation in
problems involving time scales much longer than it takes a light wave to cross
the simulation region. An important example of this is eddy current problems,
in which the FDTD cannot be used because of its short limit to the time-step.
The type of problems for which the FDTD is particularly suited involves
the propagation of electromagnetic waves and geometries where characteristic
lengths are comparable to a wavelength. This typically includes microwave
problems. Similar conditions also apply for optical devices whose dimensions
are comparable to the wavelength.
A powerful way to ﬁnd several resonant frequencies of a microwave cavity
is to perform an FDTD simulation and then Fourier transform selected signals
in time. This is the same procedure that we discussed for ﬁnding the eigen-
values of the 1D Helmholtz equation in Chapter 4. For many applications,

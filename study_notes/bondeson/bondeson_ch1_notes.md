# Bondeson《Computational Electromagnetics》第1章

> **Source:** Anders Bondeson, Thomas Rylander, Pär Ingelström, *Computational Electromagnetics*, Springer 2005  
> **PDF:** pages 20-28 of 231 (231 total)

---

## Introduction

1 Introduction
tools developed for electromagnetics problems. CEM allows for a faster and
cheaper design process, where the use of expensive and time-consuming pro-
totypes is minimized. These tools can also provide crucial information and
understanding of a device’s electromagnetic operation, which may be diﬃcult
or even impossible to achieve by means of experiments or analytical calcu-
lations. Automation of computations allows for extensive parametric studies.
It is only relatively recently that optimization by computation has been used
for electromagnetic design problems. In times of a rapid pace of development,
analysis and optimization of electromagnetic devices by CEM tools may be
crucial for maintaining competitiveness.
Today, there is a broad selection of commercially available computer pro-
grams that provide implementations of popular and powerful CEM algorithms.
These programs can handle many engineering and research problems. How-
ever, a well-informed choice and correct use of software for reliable results
and conclusions require good knowledge of CEM. Furthermore, problems that
extend beyond the applicability of commercially available software packages
demand modiﬁcations or additions that again rely on a good command of
CEM.
1.1 Computational Electromagnetics
CEM is a young discipline. It is still growing, in response to the steadily
increasing demand for software for the design and analysis of electrical devices.
Ten years ago, most electrical devices were designed by building and testing
prototypes, a process that is both costly and slow. Today the design can
be made faster and cheaper by means of numerical computation. CEM has
become a main design tool in both industrial and academic research.
There are numerous application areas for CEM, and here we mention a few.
In electric power engineering, computation is well established for the analysis
and design of electrical machines, generators, transformers, and shields. In
applications to microwaves, CEM is a more recent tool, but it is now used for
designing microwave networks and antennas, and even microwave ovens. The
analysis and optimization of radar cross sections (RCS) for stealth devices
has been the driving force for the development of many new techniques in
CEM. The clock frequencies of modern microprocessors are approaching the
region where circuits occupy a large fraction of a wavelength. Then ordinary
circuit theory no longer applies and it may be necessary to solve Maxwell’s
equations to design smaller and faster processors. The increased demand for
electromagnetic compatibility (EMC) also poses new computational problems.
The performance of CEM tools is increasing rapidly. One reason for this is
the steady growth of computer capacity over half a century. Another equally
important reason is improvements in algorithms. The purpose of this book
is to give an introduction to the most frequently used algorithms in CEM.
1.2 Maxwell’s Equations
These are ﬁnite diﬀerences (FD) (usually in the time domain), the ﬁnite el-
ement method (FEM), and the boundary element method (BEM), which is
usually referred to, for historical reasons, as the method of moments (MoM).
Finite diﬀerence methods are more or less straightforward discretizations of
Maxwell’s equations in diﬀerential form, using the ﬁeld components, or the
potentials, on a structured grid of points as unknowns. Finite diﬀerences in
general, and the ﬁnite-diﬀerence time-domain (FDTD) method in particular,
are very eﬃcient and require few operations per grid point. The FDTD is one
of the most widespread methods in CEM, and it can be applied to a large vari-
ety of microwave problems. One drawback of ﬁnite diﬀerence methods is that
they work well only on uniform Cartesian (structured) grids, and typically
use the so-called staircase approximation of boundaries not aligned with a the
grid. Finite element methods in which the computational region is divided
into unstructured grids (typically triangles in two dimensions and tetrahedra
in three dimensions) can approximate complex boundaries much better, but
are considerably slower in time-domain calculations. The FEM is mainly used
for time-harmonic problems, and it is the standard method for eddy current
calculations. The MoM discretizes Maxwell’s equations in integral form, and
the unknowns are sources such as currents or charges on the surfaces of con-
ductors and dielectrics. This method is advantageous for problems involving
open regions, and when the current-carrying surfaces are small. The MoM is
often applied to scattering problems. We will discuss how the three types of
methods, FD, FEM, and MoM, can be applied to diﬀerent electromagnetics
problems, in both the time domain and the frequency domain (time-harmonic
ﬁelds and currents). Some other methods will be mentioned in Chapter 8.
1.2 Maxwell’s Equations
Before discussing how to solve electromagnetics problems, we will ﬁrst write
down Maxwell’s equations in the form in which they can be found in most
textbooks on electromagnetics, see e.g. [18, 30, 4]. They are usually stated as
Amp`ere’s law
∇× H = J + ∂D
∂t ,
(1.1)
Faraday’s law
∇× E = −∂B
∂t ,
(1.2)
Poisson’s equation
∇· D = ρ,
(1.3)
and the condition of solenoidal magnetic ﬂux density
∇· B = 0.
(1.4)
1 Introduction
Here H is the magnetic ﬁeld, J is the current density, D is the electric
displacement, E is the electric ﬁeld, B is the magnetic ﬂux density, ρ is the
electric charge density, and t denotes the time variable. Moreover, we have
H = B
D = ϵ0E + P ,
where µ0 = 4π · 10−7 Vs/Am is the free-space magnetic permeability, ϵ0 =
1/(c2
0µ0) ≈8.854 · 10−12 As/Vm is the free-space electric permittivity, M is
the magnetization and P is the polarization. In vacuum, the speed of light is
c0 = 299 792 458 m/s.
In this book, we will restrict attention to linear, isotropic and nondispersive
materials for which the constitutive relations
B = µH,
D = ϵE
hold with frequency-independent electric permittivity ϵ and magnetic perme-
ability µ. The permittivity is often written as ϵ = ϵ0ϵr, where ϵr is called the
relative permittivity. Similarly, the permeability is often written µ = µ0µr
where µr is called the relative permeability.
For electrically conductive materials, an electric ﬁeld causes a current den-
sity
J = σE
where σ is the electric conductivity.
1.2.1 Boundary Conditions
Consider the situation in which one medium, characterized by ϵ1 and µ1,
shares an interface with another medium, characterized by ϵ2 and µ2. We use
the subindices 1 and 2 to denote quantities that are associated with media
1 and 2, respectively. At the interface, the tangential and normal ﬁelds must
satisfy so-called boundary conditions, which are consequences of Maxwell’s
equations. For example, (1.4) states the condition of solenoidal magnetic ﬂux
density, and Gauss’s theorem
∇· B dV =
B · ˆn dS,
(1.5)
where ∂V is the surface enclosing the volume V , applied to this conservation
law yields the boundary condition
ˆn · (B2 −B1) = 0,
where ˆn is a unit normal to the interface that points into medium 2. Similarly,
Poisson’s equation (1.3) gives
ˆn · (D2 −D1) = ρs,
1.2 Maxwell’s Equations
where ρs is the surface charge density on the interface. Stokes’s theorem
(∇× E) · dS =
E · dl,
(1.6)
where ∂S is the curve enclosing the surface S, applied to Faraday’s law (1.2)
yields
ˆn × (E2 −E1) = 0
and, analogously, Amp`ere’s law (1.1) gives
ˆn × (H2 −H1) = Js,
where Js is the surface current on the interface between the two media.
The electric ﬁeld inside a perfect electric conductor (PEC) is zero and,
consequently, also the electric displacement. We get the boundary conditions
ˆn · D2 = ρs and ˆn × E2 = 0 when medium 1 is a PEC. At ﬁnite frequencies,
Faraday’s law yields that the magnetic ﬂux density is zero inside a PEC
(which also applies to the magnetic ﬁeld) and we get the boundary conditions
ˆn · B2 = 0 and ˆn × H2 = Js when medium 1 is a PEC.
Another kind of boundary conditions, which do not correspond to any
physical boundary, are absorbing boundary conditions (ABC). These are used
to truncate the computational domain in case of open region problems and
can be implemented using a variety of techniques. The most popular ABC is
the perfectly matched layer (PML), which will be described in Section 5.3.1.
For a more detailed discussion on boundary conditions, the reader is re-
ferred to a textbook on electromagnetics; see, e.g., [18, 30, 4].
1.2.2 Energy Relations
For Maxwell’s equations, it is useful (and in some cases essential) to regard
the energy as being stored in the ﬁelds. For electrostatics, we have the energy
density we = ϵ|E|2/2 and the work to assemble a static charge distribution is
W = 1
ϵ|E|2dV.
(1.7)
There are alternative expressions for the evaluation of W in terms of the
charge distribution and the electrostatic potential. In magnetostatics, the
corresponding energy density is wm = |B|2/(2µ). For a time-varying electro-
magnetic ﬁeld, we have the energy density we + wm and this quantity is often
used to form energy conservation expressions that involve the electromagnetic
phenomena.
1 Introduction
1.2.3 Time Evolution
Before discussing schemes for evolving Maxwell’s equations (1.1)–(1.4) in time,
we must note that they are not all independent. For example, Poisson’s equa-
tion (1.3) is best viewed as an initial condition for the charge density. To see
this, take the divergence of Amp`ere’s law, which gives
∂t∇· D + ∇· J = 0.
(1.8)
Replacing ∇· J from the equation of continuity for electric charge
∂t + ∇· J = 0,
we see that the divergence of Amp`ere’s law (1.8) is the time derivative of
Poisson’s equation ∇· D = ρ. Therefore, if the initial ﬁelds satisfy Poisson’s
equation, time advancement of Amp`ere’s law together with the conservation of
charge will ensure that Poisson’s equation holds at later times. Similarly, the
divergence of Faraday’s law shows that the time derivative of ∇· B vanishes,
so ∇· B = 0 need only be given as an initial condition. Thus, ∇· B = 0 can
be seen as a restriction on valid initial conditions for Faraday’s law.
We conclude that the time evolution of the ﬁelds is completely speciﬁed
∂t = ∇× H −J,
(1.9)
∂t = −∇× E.
(1.10)
This form is used in the FDTD method to advance E and H in time, as will
be described in Chapter 5. The initial conditions for this set of equations are
the electric and magnetic ﬁelds E and H, and they must satisfy (1.3) and
(1.4).
The system of two ﬁrst-order equations can be combined to a single second-
order equation for E:
ϵ∂2E
∂t2 + ∇× 1
µ∇× E = −∂J
∂t ,
(1.11)
which is often referred to as the curl-curl equation or the vector wave equation.
We will use Maxwell’s equations in this form in Chapter 6 on the FEM. The
initial conditions that need to be speciﬁed for (1.11) are the electric ﬁeld and
its time derivative. In particular, FEM is generally used to solve the frequency
domain form of the curl-curl equation, sometimes referred to as the vector
Helmholtz equation, where exp(jωt) time dependence is assumed, so that the
time derivative ∂/∂t is replaced by jω, where j is the imaginary unit and ω
is the angular frequency.
1.2 Maxwell’s Equations
The full Maxwell equations (1.9)–(1.10) or (1.11) are commonly used for
microwave problems, such as antennas and microwave circuits. One of the dif-
ﬁculties one has to face in solving these equations is that the computational
domain may extend over many wavelengths in all three coordinate directions,
and that consequently the required number of unknowns needed for an accu-
rate computation may be very large. To complicate matters, one may have to
deal with complex three-dimensional (3D) geometry, including details, such as
wires, that are much smaller than a wavelength. Moreover, microwave prob-
lems often involve open regions, and to model this, the computational domain
has to be truncated by means of absorbing boundary conditions.
1.2.4 Dispersion Relation and Wave Velocities
The propagation of electromagnetic waves is often characterized in terms
of the dispersion relation, which relates spatial and temporal variation of
a monochromatic solution by means of its wavevector k and frequency ω, re-
spectively. Often, we deal with nondispersive situations where the frequency
is directly proportional to the wavenumber k. When the frequency is not pro-
portional to the wavenumber, we have dispersion and this occurs physically
for wave propagation in some media and waveguides. However, the discretiza-
tion process may also cause dispersion, which is often referred to as numerical
dispersion. In general, dispersion implies that a wave packet containing sev-
eral diﬀerent spatial frequencies will change shape as it propagates. Naturally,
it is important that the numerical dispersion is small in comparison to the
physical dispersion of interest.
To provide a brief introduction to dispersion and related issues, we use
(1.11) to deduce the corresponding 1D wave equation:
∂t2 E(z, t) = c2 ∂2
∂z2 E(z, t),
(1.12)
where the transverse electric ﬁeld is denoted E(z, t). Here, the speed of light c
in the medium is constant. The exact solutions of (1.12) on an inﬁnite interval
have the form
E(z, t) = E+(z −c t) + E−(z + c t),
(1.13)
where E+ and E−represent waves traveling in the positive and negative z-
directions, respectively. This solution typically involves a range of frequencies
and, next, we consider one of these, i.e. the monochromatic case.
To obtain the dispersion relation for the 1D wave equation, we substitute
E = exp(jωt −jkz) in (1.12), and then divide both sides by exp(jωt −jkz),
which gives ω2 = c2k2. Consequently, the dispersion relation for the 1D wave
equation is
ω = ck.
(1.14)
The angular frequency ω is a linear function of the wavenumber k and this
implies that all frequency components of a transient wave propagate with the
1 Introduction
same velocity. The phase velocity vp, deﬁned as the velocity of a constant
phase surface, satisﬁes (d/dt)(ωt −kz) = ω −kvp = 0, which gives
vp = ω/k.
(1.15)
Next, we consider the superposition of the two signals EA = exp[j(ω−∆ω)t−
j(k −∆k)z] and EB = exp[j(ω + ∆ω)t −j(k + ∆k)z]. The sum wave EA + EB
can be written as a carrier wave exp(jωt−jkz) times a slowly varying envelope
which is 2 cos(t∆ω −z∆k). We see that the propagation speed of the envelope
is ∆ω/∆k and, in the limit where ∆ω and ∆k become small, this is called the
group velocity
vg = ∂ω
∂k .
(1.16)
The envelope can be identiﬁed with a wave-packet and, if an energy density
is associated with the magnitude of the wave, the transportation of energy
occurs with the group velocity.
For the wave equation (1.12), both the phase and group velocities are
constant and equal to the speed of light vp = vg = c. This is also evident
from the explicit solution (1.13). Given this analytical treatment, all waves
propagate with the same speed, independent of their wavenumber k. Therefore
we say that there is no dispersion. However, a numerical treatment of (1.12)
will, in almost all cases, suﬀer from numerical dispersion and this is discussed
in Chapter 3, 4, and 5.
1.2.5 Low-Frequency Approximation
A special case of (1.11) is the “low-frequency approximation,” used for in-
stance for electrical machines, generators, and transformers. The low-frequency
approximation consists in setting ϵ0 = 0, that is, one neglects the displacement
current in (1.11):
∇× 1
µ∇× E + σ ∂E
∂t = −∂Jexternal
(1.17)
where the electrical current density was taken as J = σE + Jexternal, and
σ is the electrical conductivity. The low-frequency approximation gets rid of
the electromagnetic waves present in the full Maxwell equations (1.9)–(1.10)
and makes it possible to take time steps on the much longer time scale as-
sociated with the penetration of eddy currents in conductors. However, the
low-frequency approximation is mathematically more complicated, because in
regions where σ = 0, the time derivative of E drops out of (1.17). As a conse-
quence, (1.17) gives no information about ∇·E in the nonconducting regions,
so that E itself is not actually known. Since the low-frequency equations are
important in the area of both electric power engineering and electromagnetic
compatibility, we will discuss, brieﬂy, some methods used to solve these equa-
tions in Section 6.6. Some challenges that frequently occur in eddy current
problems come from extremely complicated 3D geometry and thin layers of
currents caused by the skin eﬀect.
1.2 Maxwell’s Equations
1.2.6 Integral Formulation
A simple special case is electrostatics, where there is no time-dependence. For
static conditions, Faraday’s law implies ∇× E = 0, so that E = −∇φ, where
φ is the electrostatic potential. Poisson’s equation then becomes
∇· (ϵ∇φ) = −ρ.
(1.18)
The formulations mentioned so far are all diﬀerential equations. However,
sometimes integral equations are useful. In three dimensions, the “solution”
to Poisson’s equation in free space is
φ(r ) =
ρ(r′)dV ′
4πϵ0|r −r′|.
(1.19)
This formulation is used in the MoM to solve for the charges on conductors
needed to produce speciﬁed potential distributions, as discussed in Chapter 7.
Similar reformulations in terms of surface integrals exist also for the time-
dependent Maxwell system. The integral equations are called the electric ﬁeld
integral equation (EFIE), the magnetic ﬁeld integral equation (MFIE), and
the combined ﬁeld integral equation (CFIE). We will derive and employ the
EFIE for a scattering problem in Chapter 7, which also contain discussions
on the MFIE and CFIE.
Convergence
When using numerical tools, one must keep in mind that they never give the
exact answer. The accuracy of the numerical result depends on the resolution.
Resolution may mean the number of grid points per wavelength in microwave
problems, or how well the geometry of an electrical motor is represented by
a ﬁnite element mesh. If the method works correctly, the computed answer
will converge to the exact result as the resolution increases. However, with
ﬁnite resolution, the error is nonzero, and one must estimate it to ensure that
its magnitude is acceptable. This is particularly true for large systems, where
it may be hard to resolve details of the geometry or to aﬀord a suﬃcient
number of points per wavelength. Examples of this state of aﬀairs are found
in 3D-modeling of electrical motors and generators, large array antennas, and
computation of the radar cross sections of aircrafts.
Applied mathematicians have derived a posteriori error estimates, which
can be evaluated after an approximate numerical solution has been com-
puted. However, such error estimates are only beginning to be established
for Maxwell’s equations, and discussion of these would take us far beyond an
introductory course. For further information on this topic, see, e.g., [66, 45].
Nevertheless, error estimates are useful because they can be exploited for
adaptive mesh reﬁnement in regions that give large contributions to the error.
A simpler method to estimate the error of a given computation is to do a
convergence test by increasing the resolution uniformly, ﬁnding out the or-
der of convergence, and then extrapolating the computed results to inﬁnite
resolution. That is the approach we will follow.
In general, one does not know the order of convergence of a computational
method for a given problem a priori. Even though standard centered ﬁnite
diﬀerences or linear ﬁnite elements converge with an error of order h2 (where
h is the grid spacing or the cell size) for regular problems, singular behavior of
the solution decreases the order of convergence in most application problems.
Singularities are introduced by sharp edges and tips of objects such as metallic
conductors, dielectrics, and magnetic materials.

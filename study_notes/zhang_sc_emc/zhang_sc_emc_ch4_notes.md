# Zhang《Spacecraft EMC Technologies》第4章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 4. Introduction to Spacecraft EMC Prediction Analysis Methods

Chapter 4
Introduction to Spacecraft EMC
Prediction Analysis Methods
4.1
EMC Electromagnetic Field Analysis Methods
4.1.1
Tasks and Characteristics of EMC Analysis
Analysis and design are important engineering processes in the spacecraft EMC, and
analysis is the prerequisite of design. The main task of EMC analysis is to evaluate
the EMC characteristics and the state of the system or equipment, including the ﬁeld
strength of EMI and EM coupling, or the state of the interfered devices or equipment.
In particular, EMC prediction of the equipment or systems is an analytical prediction
of the EMC status of an equipment or a system during the design phase and is crucial
for EMC design.
EMC analysis features:
(1) Complexity. Unlike the performance analysis and design of a single microwave
component in other EM engineering, EMC analysis generally involves mutual
interference between multiple equipment or components, or the radiation ﬁeld
of a radiation source in a complex environment. The degree of interference is
affected not only by the coupling path, but also by the environment. For example,
the coupling interference of EM waves between the aperture and the equipment
cavity is not only related to the shape of the aperture, but also to the structure of
the resonant cavity equivalent to the device casing. By complex and electrically
large size (the physical size is tens of times of the electrical wavelength or more),
it is necessary to model the ﬁne structure of the EM radiation source, and to
assess the impact on the environmental level caused in the environment and on
other equipment, which may involve the convergence of analytical problems in
two scales.
(2) Randomness. In the actual EMC engineering, the characteristics of the inter-
ference source and its relative position to the interfered devices are random.
For example, when the interference source is a spurious level of the source, the
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_4
57


58
4
Introduction to Spacecraft EMC Prediction Analysis Methods
amplitude phase is highly random; or in the coupling of EM waves and equip-
ment cables, the cable swing direction and the angle of incidence of EM waves
are also random. Therefore, the magnitude of EMI should also correspond to a
random quantity that conforms to a certain probability distribution. The tradi-
tional EM analysis methods mostly focus on solving Maxwell’s equations using
ﬁxed parameter values, which fall into the study of deterministic problems and
cannot fully characterize the quantity of EMC and EMI.
(3) Nonlinearity. EMI often not only appears strongly at the operating frequency of
the EM source and its harmonics, but also weakly at other spurious frequencies.
However, if a nonlinear EM response factor exists in the transmitting circuit
or in the surrounding environment, a new interference frequency point may be
formed at the intermodulation frequency of several transmitting frequencies.
4.1.2
Electromagnetic Field Analysis Method for EMC
In terms of the EMI coupling paths, there are conducted coupling and radiated
coupling, and corresponding “path” analysis and “ﬁeld” analysis methods. There-
fore, the EM ﬁeld analysis method for EMC is actually an analysis method for the
radiated coupling in EMC.
The EM ﬁeld analysis method is applicable to various EMC engineering problems,
such as mutual coupling between the antennas’ radiation and the antenna on complex
platforms, the radiated coupling between the cables, the mutual coupling between the
cables and external EM waves, and the coupling by external EM waves (or internal
radiation source of the equipment) through the equipment chassis aperture.
The EM ﬁeld analysis method for EMC is to solve Maxwell’s equations under the
excitation and boundary conditions in EMC engineering, and obtain corresponding
EMC parameters such as coupling factor and shielding effectiveness.
4.2
EM Field Numerical Analysis Method
4.2.1
Fundamentals of EM Field Analysis Method
4.2.1.1
Maxwell’s Equations and Boundary Conditions
Maxwell’s equations are the governing equations describing the laws of EM wave
motion. Maxwell equations were presented by J. Maxwell in 1873 in the form of a
Cartesian component and later expressed as a vector form by O. Heaviside:
∇× ⃗H(⃗r, t) = ∂
∂t
⃗D(⃗r, t) + ⃗J(⃗r, t) (Ampere’s law),
(4.2.1)


4.2 EM Field Numerical Analysis Method
59
∇× ⃗E(⃗r, t) = −∂
∂t
⃗B(⃗r, t) (Faraday’s law of EM induction),
(4.2.2)
∇· ⃗D(⃗r, t) = ρ(⃗r, t) (Gauss’ law for electric ﬁeld),
(4.2.3)
∇· ⃗B(⃗r, t) = 0 (Gauss’ law for magnetic ﬁeld),
(4.2.4)
where
⃗E, ⃗B, ⃗H, ⃗D, ⃗J, and ρ are the real variables of position and time;
⃗E(⃗r, t) is the electric ﬁeld strength (V/m);
⃗D(⃗r, t) is the electric displacement vector (C/m2);
⃗B(⃗r, t) is the magnetic ﬂux density (Wb/m2);
⃗J(⃗r, t) is the current density (A/m2);
⃗H(⃗r, t) is the magnetic ﬁeld strength (A/m);
ρ(⃗r, t) is the charge density (C/m3).
The most important time-varying EM ﬁeld is the one that shows a harmonic
(sine/cosine) variation over time, i.e., the time-harmonic EM ﬁeld, also known as
monochromatic wave (single frequency wave) or continuous wave (CW). Many engi-
neering applications are in time-harmonic ﬁelds, and any time-varying EM ﬁeld can
be transformed into a superimposed time-harmonic ﬁeld of different frequencies
through Fourier analysis.
Maxwell’s equations of the simple harmonic ﬁeld can be written as
∇× ⃗H(⃗r) = jω ⃗D(⃗r) + ⃗J(⃗r) = jωε

1 + σ
ω

⃗E,
(4.2.5)
∇× ⃗E(⃗r) = −jω ⃗B(⃗r),
(4.2.6)
∇· ⃗D(⃗r) = ρ(⃗r),
(4.2.7)
∇· ⃗B(⃗r) = 0.
(4.2.8)
Correspondingly, the constitutive parameter therein is also a complex quantity,
and σ is the conductivity of the medium.
Maxwell’s equations take many forms. By arithmetic operators, it can also be
divided into the differential forms described above and the integral form besides,
which will not be described in detail here.
Due to the properties of the differential operators in Eqs. (4.2.1) to (4.2.4), it is
only applicable to the case where the ﬁeld quantity is continuous and derivable. At
the interface of two different media, the change in the EM ﬁeld shall satisfy the
following boundary conditions:


60
4
Introduction to Spacecraft EMC Prediction Analysis Methods
ˆn ×

⃗E2 −⃗E1

= 0,
(4.2.9)
ˆn ×

⃗H2 −⃗H1

= ⃗Js,
(4.2.10)
ˆn ·

⃗D2 −⃗D1

= ρs,
(4.2.11)
ˆn ·

⃗B2 −⃗B1

= 0,
(4.2.12)
where
ˆn is the normal unit vector of medium 1 directing to medium 2 on the boundary
surface;
⃗Js is the surface current density on the interface (A/m);
ρs is the surface charge density on the interface (C/m2).
Maxwell’s equations and the boundary conditions can fully describe the laws of
motion and variation of EM ﬁelds within a region. This theory has played a central
role in many practical applications, such as EM ﬁeld analysis.
4.2.1.2
Boundary Value Problem of EM Field and Analysis Method
Using Maxwell’s equations and boundary conditions, the motion and variation of the
EM ﬁeld in actual EM engineering can be completely described, which equivalents
to the boundary value problems in mathematics. The boundary value problems in
EM engineering are the same as those in mathematical models in many physical
systems, both of which can be deﬁned by the governing equations in the  region
(the Poisson equation, the scalar wave equation, and the vector wave equation for
EM ﬁeld) and the boundary conditions on boundary  of the surrounding regions
(may be the Dirichlet condition for the ﬁrst type and the Neumann condition for the
second type, or the impedance and radiation boundary conditions, etc.).
Lu = g within region Ω,
(4.2.13)
Bu = q on boundary Γ,
(4.2.14)
where
L and B are the linear differential or integral operators in the region and on the
boundary;
u is an independent variable;
g, q are the source items within the region and boundary.


4.2 EM Field Numerical Analysis Method
61
For EM engineering, the operators are differential or integral operators derived
from Maxwell’s equations, while the independent variable is usually a magnitude of
EM ﬁeld or a potential function.
If the source term in Eqs. (4.2.13) and (4.2.14) is zero, it involves the eigenvalues,
which correspond to the solution of the resonant frequency, and propagation constant
in microwave engineering. If the source term is not zero, it is called the deterministic
problem, i.e., the response resolution problem of a particular microwave structure
under a speciﬁc excitation, such as the solution of microwave radiation and scat-
tering problems, equivalent network parameters, etc. In analysis, analytical methods,
approximate analytical methods, and the widely used numerical methods are most
commonly used.
(1) Analytical methods
Analytical methods include the separation variable method and the math-transform
method; the former is for differential equations, and the latter for integral equa-
tions. The analytical method can obtain the closed-form solution of the function to
be solved, but can only be used for several simple and classical microwave struc-
tures, such as rectangular or hexahedral structures, cylindrical or elliptical column
structures, and circular or spherical structures.
(2) Approximate analytical methods
Approximate analytical methods include variational method, perturbation method,
HF and LF approximations, and linear method.
Many complex microwave engineering problems can be regarded as some kind
of variation of a simple, analytical solution. Both the variational methods and the
perturbation methods can give out approximate solutions (called a trial function in
the variation method) to such problems; the main term of the solution corresponds to
the solution of a simple structure. By comparison, the variation method utilizes the
stationary characteristics of the variation expression of the solution, so its solution
is more accurate than that of the perturbation method.
The HF approximation methods include physical optics, geometric optics,
geometrical diffraction theory, etc. They are the simpliﬁed calculations using the
optical approximation of the microwave and its interaction with the target, often
used for the EM scattering and radiation problems, when the electrical size (the
ratio of the geometry dimension to the microwave operating wavelength) of the scat-
terer or radiator is large (generally deﬁned as greater than 10λ). Correspondingly,
the LF approximation method is the simpliﬁed calculation using electrostatic ﬁeld
approximation when the electrical size of the microwave structure is small.
The linear method means that in solving multidimensional problems, analytic
functions are used in some dimension directions, while discrete and interpolation
method are used in other dimension directions.


62
4
Introduction to Spacecraft EMC Prediction Analysis Methods
(3) Numerical methods
The commonly used numerical methods are the Method of Moment (MoM) based
on integral equations and its fast algorithms such as fast multipole, Finite Element
Method(FEM),andFinite-DifferenceTime-Domain(FDTD)method.Thenumerical
methods can also be divided into the MoM and FEM based on the weighted residual
method, and the FDTD based on difference principles. The details will be given in
the next section.
4.2.2
Weighted Residual Method and Numerical Solution
Method
In case of a complicated geometry structure and a complex material composition of
the solution region and boundary, the approximate solutions of (4.2.13) and (4.2.14)
can only be obtained by numerical calculation. Many numerical calculation methods,
such as the MoM and the FEM, rely on weighted residuals to ensure the accuracy of
the calculations.
4.2.2.1
Weighted Residual Method
Assume that the approximate solutions of Eqs. (4.2.13) and (4.2.14) are ˜u
˜u =
N

i=1
αiui,
(4.2.15)
substitutingitintoEqs.(4.2.13)and(4.2.14)yieldsanonzeroresidual,thenweighting
function is used to form the corresponding error functional:
Ri = ⟨ui, L ˜u −g⟩Ω + ⟨ui, B ˜u −q⟩Γ = 0.
(4.2.16)
In Eq. (4.2.16), the chosen weighting function, called the Galerkin method, is
equivalenttothebasisfunction.Thisequationisoneofthemostwidelyusedweighted
residual methods that can be arbitrarily selected. Note that the subscripts of the two
different inner products in the equation represent the respective integration regions.
Consider the case of i = 1, 2, …, N, in fact, Eq. (4.2.16) corresponds to an N-
dimensional matrix equation:
[A][α] = [b],
(4.2.17)
where matrix A element is Ai j =

ui, Lu j

Ω +

ui, Bu j

Γ , vector b element is
bi = ⟨ui, g⟩Ω + ⟨ui, q⟩Γ .


4.2 EM Field Numerical Analysis Method
63
Theoretically, as the dimension N increases, the approximate solution should
become closer to the real solution. Therefore, the MoM and FEM based on the
weighted residual method have very high computational correctness and play an
important role in microwave engineering and other engineering. This kind of solution
is also called the variable decomposition method. Like the variation method in the
approximate analytical method, it is based on the processing of the corresponding
functional of the physical problem. The difference is that the trial function of the
ordinary variation method generally uses an analytical solution similar to a simple
structure as the main term, supplemented by a higher order function, while here it
is approximated by an orthogonal complete function expansion of a certain inner
product space.
4.2.2.2
Frequency-Domain and Time-Domain Methods for EM Field
Solution
The MoM and FEM are also called the frequency-domain methods in the numer-
ical analysis methods of EM ﬁeld, and each calculation is performed at a speciﬁc
frequency point, that means, the obtained result is the response of a continuous wave
(monochromatic wave). When the analysis object involves an EM signal which is a
complex time-domain waveform containing many spectral components, it is neces-
sary to simulate separately at multiple frequency points and obtain the response of
its time-domain signal through time-, frequency-domain transformations.
Directly solving Eqs. (4.2.1) to (4.2.4) can obtain the time-domain response of the
EM signal. This solution is mostly based on the principle of the difference method,
that is, discretely approximates the continuous operators, e.g.:
d f
dx

x=a
= f (a + x) −f (a)
x
.
(4.2.18)
In 1966, K. S. Yee used the difference format to simulate the Spatio-temporal
evolution of EM ﬁelds in the microwave problem in space and time domain for the
original time-domain Maxwell equations, called FDTD.
In this algorithm, the values of electric and magnetic ﬁelds in space are taken at an
interval and they alternate at a varying time step ni. A block diagram of the simulation
processisshowninFig.4.1.Itisshownthat,unlikethemethodsbasedontheweighted
residual method, the difference method is to simulate the motion and variation of the
EM ﬁeld by differential approximation. There is no error functional method and other
measures to ensure the correctness of the solution, and it is susceptible to numerical
dispersion.
In recent years, many achievements have been made in the research of electro-
magnetic ﬁeld numerical analysis methods, most of which focus on the actual EM
analysis requirements, such as large electrical-size targets, fast calculation methods,
multiscale structural analysis objects, and periodic structural analysis objects. The
basic principles are mostly based on MoM, FEM, and FDTD, and correspondently,


64
4
Introduction to Spacecraft EMC Prediction Analysis Methods
Fig. 4.1 Block diagram of
the FDTD method
EM field component 
initial value
End
Start
Source exciting
Calculate the electric field component in the 
simulated region
nt=nt+1/2
Boundary condition
nt=nt+1/2
Calculate the magnetic field component 
in the simulated area
nt
Nt
Yes
No
commercial software such as Ansys HFSS (mainly for FEM), FEKO (mainly for
MoM), and CST (mainly for FDTD) are widely used in practical EM engineering
due to their powerful capabilities of modeling, dissection, calculation analysis, and
post-processing.


4.3 Statistical Electromagnetics Analysis Method
65
4.3
Statistical Electromagnetics Analysis Method
4.3.1
Fundamentals of Statistical Electromagnetics
In physics, when the research object is no longer a small number of individuals, but
a large group, it will lead to fundamental changes in the nature of the law and the
research methods. The statistical laws followed by a large number of event systems
cannot be attributed to the laws of mechanics, so a statistical physics method is
required. In addition, the EM signals in the random physical world are random,
so fully understanding their random property is the prerequisite for logical EM
engineering design.
The randomness of EM signals in mobile communications is well-known and
fully-studied.. When the EM signal is radiated from the transmitter antenna direc-
tionally or omni-directionally, it reaches the receiver antenna through the open space.
Because of the occlusion and reﬂection of buildings, vehicles, mountains, in the
natural space, by the geometric ray theory of EM wave propagation, there are multiple
propagation paths from the transmitter to the receiver, maybe directly between the
transmitter and the receiver, but more are reﬂected by the surrounding environment.
The propagation path depends on the geometric position distribution of the space
environment (determining the length of the path) and the material properties (deter-
mining the strength and phase of the reﬂection), and are also related to the character-
istics of the transmitting and receiving antenna patterns. The wider the pattern lobe,
the more multipath signals may be received. The natural environment in which the
signals are reﬂected is changing all the time, so the paths of the reﬂected signals
are random, especially in mobile communication. The multipath signals arriving
at the receiver have randomness due to the phase difference caused by different
lengths of the paths, resulting in ﬂuctuation jitter (fading) on the receiver. This is
called multipath effect, and its effect on the signal is generally described in terms
of the parameters such as fading level probability distribution, level crossing rate,
and correlation bandwidth and correlation time. The multipath effect will obviously
have an impact on the service quality of mobile communication, so it is necessary
to take corresponding technical measures such as adaptive equalization. Whether it
is the design of mobile communication links or the adaptive equalization, the basic
design inputs are required with a fading level probability distribution, the relevant
bandwidth, and the correlation time.
The reverberation chambers, which are widely used in the EMC and wireless
communication engineering, may be used in the tests such as radiated emission
(RE), radiation immunity, antenna efﬁciency, shielding effectiveness, and wireless
communication environment simulation. In order to obtain a statistically uniform,
isotropic, and randomly polarized EM environment, one or several mechanical agita-
tors are usually installed in the shielded chamber to create an ever-changing reﬂec-
tive boundary condition. The statistics of the EM ﬁeld distribution is crucial for
the reverberation chamber design, and is also the input condition for the EMC
experiments.


66
4
Introduction to Spacecraft EMC Prediction Analysis Methods
In case of EMI and EM damage, EM waves in space enter the electronic equipment
through antennas, cables, and chassis apertures of the disturbed equipment, causing
interference to the normal operation or even damage to the components. In contrast to
the path into the equipment through the antenna (so-called “front door”), EM waves
can also enter the equipment through the device cable and the chassis aperture (so-
called “back door”) and be coupled into the electronic circuit. In practice, the angle
between the incident EM wave and the cable and the chassis aperture is random,
so the interference amplitude is coupled into the electronic circuit. Moreover, an
important task is to evaluate the random distribution of interference in EMI and anti-
interference research. In the analysis, it is often necessary to evaluate the worst-case
conditions, which are important input indicative parameters for reinforcement or
interference design.
In the machining and assembling of microwave components, antennas, and
antenna arrays, errors are inevitable. Due to the different processing technology
and assembly processes, the laws of error randomness vary. This kind of random-
ness can lead to random variations in the performance of microwave components,
antennas, and antenna arrays. Evaluation of the performance variations of different
processes is required in many EM engineering designs.
From the abovementioned EM engineering, it is found that the randomness of
the EM signals mainly depends on the randomness of the environment. In fact, the
EM signal source itself is also random. Most of the signal sources in modern EM
engineering are mature solid-state microwave sources, which use microwave oscil-
lators to generate microwave signals, such as Gunn-tube oscillators, avalanche-tube
oscillators, and transistor-locked oscillators. The carrier concentration and conduc-
tivity of the semiconductor in the thermal equilibrium state have statistical properties,
so the output amplitude and frequencies of the microwave solid-state source signal
will have random ﬂuctuations. In addition to the output EM signals at the oper-
ating frequency, the microwave solid-state source also outputs EM signals at other
frequencies, which is called spurious signals. The difference between the intensity
of the signal at the operating frequency (i.e., carrier) and that of the spurious signal
is generally presented in terms of the logarithmic form of their ratio dBc. In the
general signal source design, the requirements on the intensity of the spurious signal
are usually deﬁned. The spur of the solid source commonly used in engineering
can reach 70 dBc, which means, the spur is generally a random signal 70dB lower
than the carrier. Spurious signals not only affect the operational characteristics of
the equipment itself, but also affect the normal operation of other equipment in the
system. In a word, it is a critical EMI source.
Inshort,thestatisticalpropertiesofEMsignalsareanimportantfeatureinpractical
EM engineering, and also an essential part of EM engineering analysis and design.


4.3 Statistical Electromagnetics Analysis Method
67
4.3.2
Analytical Methods of Statistical Electromagnetics
IntheEMnumericalanalysismethod,Maxwell’sequationsandtheirboundarycondi-
tions are the governing equations to be solved. Under certain excitation conditions,
in the domain to be solved, the EM ﬁeld distribution is calculated and various EM
parameters are obtained, such as antenna gain, pattern distribution, standing wave,
and insertion loss for S-parameter characteristics. From the perspective of equa-
tion solving, it is a kind of a determined incentive term, a kind of solution under a
boundary condition. Because it is mainly solved by numerical methods such as the
weighted residual method, it is generally called the EM ﬁeld numerical method or
computational electromagnetics method.
Computational electromagnetics analysis can only analyze and evaluate the phys-
ical problems under determined parameters; it cannot simulate and analyze the
random distribution of the output caused by the randomness of the input parameters
of the physical problem, which means, the excitation term or boundary condition in
the governing equation to be analyzed is no longer a certain value, but a possible
range, such as the amplitude of a varying radiation source, the position of an antenna
element, the geometry of an EM wave environment, and the coupling relationship
with its target. Correspondingly, the obtained solution, such as antenna gain, standing
wave, antenna radiation ﬁeld value and S-parameters of phase and passive compo-
nents, and EM ﬁeld coupling coefﬁcient, is no longer a value, but a possibility within
a range. Mathematically, it is the statistical probability distribution in the solution
space, including the maximum, minimum, and range of the output solution, as well as
the probability density distribution function of the output solution. So, corresponding
to the computational electromagnetics, it is called statistical electromagnetics.
The statistical electromagnetics has been applied to the analysis and calculation of
EM engineering problems (such as antenna array performance analysis, EM coupling
analysis, and complex cavity problems) since the 1970s, all of which analyze the
random distribution of the EM response where one or several parameters are random
amplitudes. The randomness of the input parameters requires prior knowledge. This
distribution may be related to processing technology, environmental characteristics,
etc. Assume that its value is x, generally, it is a probability distribution function in a
range between the minimum value xmin and maximum value xmax. If its probability
distribution function is given without prior knowledge, it can be assumed to be a
uniform distribution, as shown in Fig. 4.2.
Fig. 4.2 Probability density
distribution function of a
uniform distribution
P(x)
xmax
xmin
Range Rx


68
4
Introduction to Spacecraft EMC Prediction Analysis Methods
Then its probability density distribution function is 1/Rx, where Rx = xmax −xmin.
Accordingly, using analytical and numerical analysis methods, the characteristics
of the probability density distribution of EM response can be further analyzed.
For EM engineering problems where the input parameters are explicitly related to
the output parameters, an analytical method can be used. For cases where only one
input parameter is random, let its relationship with the output to be solved be f (x). If
X is random in the range Rx and the possibility of its occurrence at each position in
Rx can be expressed by the Probability Density Function (pdf), then let it be PX(x).
The probability for the random input X between x′ and x′ + dx can be expressed
as PX(x′)dx, and f (x) can be derived, and its derivative f ′′(x) > 0 (or there is a constant
f ′(x) < 0). If the input random X changes into dx, then the output f (x) will change
into
d f (x) = f ′
x′	
dx
(4.3.1)
In addition, the probability density of the output Y = f (X) to occur between f (x′)
and f (x′) + df (x) can be written as PY(y), and
PY(y) = PX

x′	
| f ′(x′)|
(4.3.2)
This equation shows that the probability density of the output Y = f (X) to occur
between f (x′) and f (x′) + d f (x) is equal to that of the input X to occur between x′
and x′ + dx divided by the variation between the output x′ and x′ + dx.
Similarly, if two design input parameters are random, let them be x and y, and their
probability density distribution functions are p(x) and p(y), respectively, in Rx and
Ry, and there is no statistically independent quantity between the two parameters.
The probability density distribution function of the EM response output f (x′, y′) can
be obtained as
p

f

x′, y′	
=
p

x′	

δf (x′)
δx
 ·
p

y′	

δf (y′)
δy
.
(4.3.3)
However, many EM engineering problems have no explicit relationship between
the input and the output, so they can only be calculated by a numerical method to
obtain their responsive relationship. Therefore, it is necessary to use a combination
of computational and statistical electromagnetics methods to obtain the probability
density distribution function of the output. The Monte Carlo data statistics method
is well suited to be combined with the computational electromagnetics.
The Monte Carlo method, also called the stochastic simulation method, is referred
to as a random sampling technique or a statistical test method. Its basic concept is as
follows: in order to solve problems in mathematics, physics, engineering technology,
and production management, ﬁrst, establish a probability model or a stochastic


4.3 Statistical Electromagnetics Analysis Method
69
process, such that its parameters are equal to the solution of the problem, then calcu-
late the statistical characteristics of the parameters being solved by observing the
model or through the process or sampling test, and ﬁnally get the approximate values
of the solution. The accuracy of the solution can be expressed by the standard error
of the estimation.
4.4
Analysis of Mutual Coupling S-Parameters Between
Elements
4.4.1
Principle of Mutual Coupling Between Elements
and Its Effect on EMC
EMC in satellite systems is an important part of the electromagnetic environmental
effects (E3). When various subsystems and equipment work together in one system
and can all perform properly, it is called intra-system EMC. The normal operation of
antenna connection equipment (also called frequency equipment) is very important.
If the receiver connected to the antenna cannot receive the signal normally, it will be
a serious task failure, so the antenna layout is a core task of intra-system EMC.
If the system is well reinforced, with good EMC in subsystems and equipment,
satisﬁed grounding and electrical bonding, intra-system EMC should be in normal
condition. Most of the EMC problems arise in antenna-connected equipment (trans-
mitters and receivers), especially the receiver which is susceptible to performance
degradation due to interference from harmonics, spurs, etc., coupled from the trans-
mitter antenna. Another interference that may degrade the receiver performance is the
harmonic of the microprocessor clock signal (or the harmonics of each crystal oscil-
lator) coupled from the cables within the system. The interference coupling path,
which is second only to the mutual coupling between the antennas, is the mutual
coupling between the cables, especially the impact of the power lines on the video
and audio signal lines.
Various antennas are arranged in the narrow space on the satellite platform.
Transmitters of application loads, such as communications, may have very strong
interference to a variety of receivers with high sensitivity through antenna mutual
coupling. As a result, many effective EMC measures (such as isolation) cannot be
used, thus making it very difﬁcult to control its EMI. In this case, high reliability
of the whole system can be achieved only by accurately predicting the system EMC
at the beginning of the whole design and optimizing the parts that do not meet the
EMC requirements.
The RF signal power output by the radio transmitter is sent to the antenna through
a feeder (cable), and radiated by the antenna in the form of EM waves. After arriving
at the receiving location, the EM waves are received by the antenna (only a small part
of the power is received) and sent to the radio receiver through a feeder, as shown
in Fig. 4.3. Obviously, the antenna is an important radio equipment for transmitting


70
4
Introduction to Spacecraft EMC Prediction Analysis Methods
Receiving antenna
Low noise amplifier
Mixer and filter
MF amplifier and detector
Fig. 4.3 Diagram of an antenna and its connected receiver
and receiving EM waves—no antennas, no radios.
For an antenna, the radiation and receiving of electromagnetic waves are direc-
tional. To meet different needs, it can be omnidirectional, such as base station
antennas for cellular mobile communications, or highly directional, such as terres-
trial antennas for geostationary satellite communications. The directional radiation
characteristic of the antenna can be quantitatively described by a pattern as shown
in Fig. 4.3. The antenna directionality is spatially distributed like a lobe, so it is also
called the lobe pattern. The energy radiated by the antenna (or received, which is
reciprocal) is mainly concentrated in the direction of the main lobe, while the energy
in the direction of the side lobes is relatively low. This cluster characteristic of energy
is similar to the ampliﬁcation feature in the spatial domain and can be expressed in
terms of gain. Quantitatively, the gain can be deﬁned as the product of the direc-
tivity coefﬁcient and efﬁciency. The directivity coefﬁcient is deﬁned as the ratio of
the radiation intensity of the antenna in a given direction to the average radiation
intensity for the same radiated power:
D(θ, φ) = E2(θ, φ)
E2
0
,
(4.4.1)
and the gain is deﬁned as
G = E2
E2
0
= ηD,
(4.4.2)
where η is the efﬁciency, namely, the ratio of the radiated power to the input power.
Figure 4.4 shows the diagram of the antenna directionality.
According to the characteristics of the EM ﬁeld radiated by the antenna, the
antenna radiation area can be subdivided into the near ﬁeld and the far ﬁeld. The EM
ﬁeld in the near ﬁeld is called the reactance ﬁeld, and that in the far ﬁeld is called the
radiation ﬁeld, whose power attenuates with range by square rate. For the division
of the far ﬁeld and the near ﬁeld, if the antenna is a symmetric vibrator, it is divided
according to a 10λ distance; if the antenna is an aperture type, and the aperture is
D, then it is divided according to a distance of 2D/λ. The transmission of EM wave


4.4 Analysis of Mutual Coupling S-Parameters Between Elements
71
Fig. 4.4 Schematic diagram
of the antenna directionality
Main lobe width
First side lobe
Second side lobe
energy may occur between any pair of transmitting antennas and receiving antennas.
In the far ﬁeld of the antenna, the inﬂuence received by the receiving antennas with
a distance R from the transmitting antenna can be expressed by Eq. (4.4.3):
PR
PT
= GT G R
λ2
(4πR)2 ,
(4.4.3)
where the subscript T represents the transmitter, R represents the receiver, therefore,
PT is the transmitter power, GT is the transmitter antenna gain, and λ is the wave
wavelength.
It can be seen that Eq. (4.4.3) represents the process in which the transmitter power
is radiated through the antenna, spatially propagated, and coupled into the receiver
by the receiver antenna. If the EM wave coupled to the receiver is an undesirable
signal, i.e., the noise that interferes with the normal operation of the receiver, such
interference path is called antenna mutual coupling. The transmitter power received
by the receiver is the strength of the mutual coupling between the antennas, which
is proportional to the gain in the line-of-sight (LOS) direction of the two antennas
and inversely proportional to the distance of the antenna’s electrical wavelength R/λ.
Although this conclusion is derived from the formula in the far ﬁeld, it also has
reference value for the mutual coupling of antennas in the near ﬁeld. Note that there
is no quantitative concept of far-ﬁeld gain in the near ﬁeld. In engineering, Eq. (4.4.3)
is often expressed in decibels (dB), and written as the intensity of coupling IC. In
the far ﬁeld, the value of IC can be approximated as
IC = GT + G R + 20 lg
4πR
λ

+ Diffraction coefﬁcient
+ Occlusion coefﬁcient + Polarization loss.
(4.4.4)


72
4
Introduction to Spacecraft EMC Prediction Analysis Methods
In the free space where the transmitting and receiving antennas can look directly
at each other, the spatial attenuation term in Eq. (4.4.4) can be approximated as
20 lg
4πR
λ

= 22 + 20 lg R
λ .
(4.4.5)
Equation (4.4.5) can be used to approximate the IC change caused by the distance
between the transmitting and receiving antennas, which means, if the distance
between the antennas is 10 electrical wavelengths, the IC loss caused by spatial
attenuation is about 42 dB, and the attenuation will increase by about 6 dB for every
doubling of the distance.
If the transmitter power (interference) received by the receiver exceeds the sensi-
tivity of the receiver, the normal operation of the receiver will be affected, EMI is
then generated.
As shown in Fig. 4.5, the working frequency bands of the transmitter and receiver
may not coincide. Therefore, the frequency in Eq. (4.4.4) (corresponding to the
wavelengthλ)maybethefrequencyontheworkingfrequencybandofthetransmitter,
then it corresponds to the larger transmission power Pt, and the antenna gain Gt is also
larger; it may also be a frequency outside the transmitter’s working frequency band,
then the corresponding transmit power Pt is the transmitter’s out-of-band spur. If the
transmitter uses an electric vacuum device such as a traveling wave tube, the spurs
may be around 100 dBc; if it is a solid-state source, the spurs may be 60–80 dBc, and
the antenna gain Gt is also relatively smaller, because the increase of out-of-band
reﬂection greatly reduces its efﬁciency. Similarly, the frequency of Eq. (4.4.5) may be
Sensitive 
equipment
Interference
equipment
Fig. 4.5 Spectrums of the transmitter (interference source) and receiver (sensitive source)


4.4 Analysis of Mutual Coupling S-Parameters Between Elements
73
the frequency within the working frequency band of the receiver, where the sensitivity
value of the receiver (corresponding to dBm) is related to its receiving sensitivity,
typically on a very small magnitude, while the antenna gain and efﬁciency are also
in the optimal range of the design. If the frequency falls out of the receiver’s working
frequency band, the sensitivity depends on the following frequency characteristics
of components, such as the out-of-band attenuation of the ﬁlter in the receiver, the
out-of-band reﬂection of the receiving antenna, and the frequency of the low-noise
ampliﬁer. If the frequency is far from the working frequency band, the sensitivity
can be more than 80 dB higher than the receiver sensitivity. It is predictable that the
closer the transmitter’s working frequency to the receiver’s working frequency, the
greater the probability of mutual interference.
When the transmitter and the receiver antennas are in the near ﬁeld, Eq. (4.4.4)
is no longer applicable; when there is an occlusion between the transmitting and the
receiving antennas, or direct LOS between them no longer exists, or the surrounding
environment is complicated, or there are multipath effects, then Eq. (4.4.5) is no
longer applicable.
4.4.2
Mutual Coupling S-Parameter Analysis Method
Between Elements
All antennas, carrier platforms, and radiated space on a complex carrier platform can
be viewed as a complex multi-port network. The IC between individual antennas can
be characterized and calculated by the [S] parameters of the network.
Assuming that the transmitted power of the transmitting antenna is Pt, the received
power on the receiving antenna is Pr, under ideal conditions, the coupling from the
transmitting antenna to the receiving antenna is
C = 10lg
 Pr
Pt

= 10lg
|S21|2	
.
(4.4.6)
According to the above deﬁnition, the larger the C value, the greater the coupling
between the antennas, and the greater the mutual interference.
However, it is difﬁcult to achieve ideal matching impedance between the transmit-
ting and the transmitter antennas, or between the receiving antenna and the receiver.
In most cases, there is energy reﬂection between the antenna and the terminated
equipment. Therefore, it is necessary to analyze how to accurately calculate the IC
between antennas in case of impedance mismatch.
Due to this impedance mismatch, the input power of the transmitter is not equal to
the net input power of the transmitting antenna (the power transmitted by the trans-
mitting antenna), and the power received by the receiving antenna is not equal to the
net output power of the receiving antenna (the power received by the receiver). There-
fore, the calculation of the IC between the antennas must fully consider the energy


74
4
Introduction to Spacecraft EMC Prediction Analysis Methods
reﬂection problem caused by the impedance mismatch, and the antenna and its termi-
nated equipment should be considered as a whole—the antenna system. Because the
coupling interference between the antennas is actually an EMI generated by the
transmitting antenna system to the receiving antenna system, this interference ﬁnally
acts on the receiving antenna terminated load (receiver). For example, the intermod-
ulation interference between radio systems is caused by the nonlinear characteristics
of the receiver after the signals are mixed into the receiver through the receiving
antenna. When the level of the interference signal exceeds the sensitivity threshold
of the receiver, the receiver will be interfered with. Therefore, for system EMC,
especially for the electronic equipment on the complex carrier platform, the antenna
mutual coupling should be studied as a coupling interference problem between the
transmitting and the receiving antenna systems.
Accordingtotheaboveanalysis,inthestudyofcommunicationsystem’sEMC,the
deﬁnition of coupling suitable for study in a communication system can be expressed
as
C = Plr

Pa,
(4.4.7)
where
Plr is the power absorbed by the receiving antenna load;
Pa is the available power transmitted by the transmitter.
This coupling deﬁnition takes into account the mutual interference between the
transmitting and receiving antenna systems, both the interference source and the
victim equipment are included in the scope of the study, instead of calculating the
coupling effect between the antennas separately. Plr in Eq. (4.4.7) is the power
absorbed by the receiving antenna load, which reﬂects the interference signal strength
mixed into the receiver through the receiving antenna, and provides a basis for accu-
rately determining whether the receiver is disturbed and the degree. Pa is the avail-
able power transmitted by the transmitter, which characterizes the maximum output
power and the operational characteristics of the transmitter. If the operating parame-
ters and the coupling of the transmitter of the communication system are known, we
can directly obtain the intensity of the interference signal received by the receiver
using Eq. (4.4.7), then compare the interference signal with the receiver sensitivity
threshold, and determine the interference of the receiver.
Given the above, we obtained the coupling deﬁnition expression (4.4.7) suitable
for the mutual interference study of communication systems in the context of system
EMC. The following is an explanation of the calculation method using microwave
network theory. Without loss of generality, a communication system consisting of
two antennas is taken for an example as shown in Fig. 4.6. Assuming that antenna 1
is a transmitting antenna and antenna 2 is a receiving antenna. The communication
system can be regarded as equivalent to a two-port microwave network model, as
shown in Fig. 4.7. The transmitter is equivalent to an internal resistance Zg and a
source Eg, and the receiver is equivalent to a load impedance ZL, where Γ g is the


4.4 Analysis of Mutual Coupling S-Parameters Between Elements
75
Transmit antenna
Transmitter 
Receiver
Receive antenna
Fig. 4.6 Transmitter and receiver antenna systems
Fig. 4.7 Equivalent two-port network
source reﬂection coefﬁcient, Γ in is the input reﬂection coefﬁcient of port 1, and Γ L
is the load reﬂection coefﬁcient.
According to the two-port network theory, the power absorbed by the load is
Plr = 1
2|b2|2
1 −|ΓL|2	
= 1
8
|S21|21 −Γg
2
1 −|ΓL|2	
|1 −S22ΓL|21 −ΓgΓin
2

−
E g

2
.
(4.4.8)
The input power is
Pin = 1
2|a1|2
1 −|Γin|2	
= 1
8
1 −Γg
2
1 −|Γin|2	
1 −ΓgΓin
2

−
E g

2
.
(4.4.9)
The signal source power Pa is the maximum output power when the input
impedance Zin of the network is conjugated with the source internal resistance Zg,
at this time, Γg = Γin, the coupling between the communication systems is obtained
as below


76
4
Introduction to Spacecraft EMC Prediction Analysis Methods
C = Plr
Pa
=
|S21|2
1 −
Γg
2
1 −|ΓL|2	
|1 −S22ΓL|21 −ΓgΓin
2
.
(4.4.10)
From Eq. (4.4.10), the coupling between communication systems is not only
related to the equivalent two-port network, but also to S22, Γ in, Γ g, and Γ L. It is
noteworthy that, when Γ L = Γ g = 0, Eq. (4.4.10) degenerates into Eq. (4.4.7). Γ g
= 0 indicates that the transmitting antenna matches the signal source (transmitter)
impedance, Γ L = 0 indicates that the receiving antenna matches its load (receiver)
impedance. At this time, the power received by the receiving antenna is equal to the
net output power of the receiving antenna.
The coupling is analyzed from the perspective of system EMC for EMI caused by
antenna coupling between various communication system equipment. The system
IC not only considers the intra-system mismatch loss problem, but also intuitively
reﬂects the level of interference to sensitive equipment, which is more suitable for
the prediction and evaluation of system EMC than that of the traditional antenna.
The EMI margin of communication equipment is deﬁned as the difference between
the signal power from the transmitter received by the receiver PR and the receiver
sensitivity threshold SR:
PR −SR
(4.4.11)
When evaluating the EMI of the communication system, if we obtain the system
couplingbycalculation,wecandirectlygettheinterferenceofthereceiver.Therefore,
the system coupling has greater practical engineering signiﬁcance for the calcula-
tion and prediction of radiated interference between radio subsystems in a complex
system.
4.5
Spectrum Compatibility Analysis
Spectrum compatibility analysis is the basis for spacecraft system-level RF EMC
analysis and design, and is of vital importance for spacecraft RF frequency planning.
Generally, before the spacecraft frequency is designed and applied for approval,
spectrum compatibility analysis is required to ensure a reasonable design and reduce
the probability of radio frequency EMI.
The main task of frequency compatibility analysis is to determine whether there
is a possible interference pair between the frequency transmitting and receiving
equipment. This judgment only considers the frequency and bandwidth, not the
amplitude for the time being. For instance, the magnitude of the fundamental and
the harmonics transmitted by the frequency equipment are considered the same in
this judgment.


4.5 Spectrum Compatibility Analysis
77
The frequency compatibility analysis mainly involves the crystal oscillator, local
oscillator, transmission frequency, bandwidth, the intermediate frequency generated
on the transmitting link of the frequency transmitting equipment, and the receiving
frequency, local oscillator, bandwidth of the frequency receiving equipment on the
spacecraft. It determines whether various interferences exist between the transmitting
and receiving equipment.
The spectrum compatibility analysis is generally divided into two steps. The ﬁrst
step is the preliminary screening; the purpose is to make a preliminary prediction of
the four interference margins that the spacecraft system may generate in a fast and less
accurate manner. These four margins are as follows: the fundamental interference
margin, the transmitter interference margin, the receiver interference margin, and
the clutter interference margin. The fundamental interference margin refers to the
fundamental transmission of the transmitter and the fundamental response of the
receiver; the transmitter interference margin refers to the transmitter’s fundamental
transmission and the receiver’s spurious response; the receiver interference margin
refers to the transmitter’s spurious transmission and the fundamental response of the
receiver; and the clutter interference margin refers to the spurious transmission of
the transmitter and the spurious response of the receiver.
According to the experience on EMC engineering design, in the preliminary
frequency analysis, the following transmitter and receiver frequency limits are
assumed: the minimum spurious frequency of the transmitter is (f s)min or 0.1 f s; the
maximum spurious frequency of the transmitter is (f s)max or 10 f s; the minimum
spurious frequency of the receiver is (f r)min or 0.1f r; the maximum spurious
frequency of the receiver is (f r)max or 10 f r.
Based on the above assumptions, the following judgments are made:
• if |f s – f r| < 0.2 × f r there is a fundamental interference margin;
• if 0.1 × f s < 10 × f r there is a transmitter interference margin;
• if 0.1 × f s < f r < 10 × f s there is a receiver interference margin;
• if 0.1 × f s < 10 × f r or 0.1 × f r < 10 × f s there is a clutter interference margin,
where f s is the transmitting center frequency and f r is the receiving center frequency.
During the preliminary screening, the transmitting and the receiving frequency
range can be widely set, in order to get a preliminary interference judgment, which
is only qualitative. The details will be analyzed in the second step.
The second step is a detailed analysis of the frequency compatibility, which
generally includes fundamental interference analysis, harmonic interference anal-
ysis, subharmonic interference analysis, local oscillator interference analysis, inter-
modulation interference analysis, image interference analysis, and combined inter-
ference analysis. By these analyses, if the generated interference signal band overlaps
with the receiving frequency band, it is considered that frequency interference occurs,
and vice versa. Figure 4.8 shows the basis for interference judgment.
The following are the descriptions and methods of various types of spectrum
compatibility analysis.


78
4
Introduction to Spacecraft EMC Prediction Analysis Methods
Fig. 4.8 Schematic diagram
of frequency interference
judgment
(1) Fundamental interference analysis. It refers to analyzing whether there is inter-
ference between the transmitting and receiving fundamental frequencies. The judg-
ment basis is whether there is an overlap between the two fundamental frequencies.
If their relationship satisﬁes Eq. (4.5.1), it is considered that there is no fundamental
interference problem, and vice versa.

fs −Bs
2
fs + Bs
2

∩

fr −Br
2
fr + Br
2

= 0,
(4.5.1)
where
Bs is the bandwidth of the transmitting frequency band;


4.5 Spectrum Compatibility Analysis
79
Br is the bandwidth of the receiving frequency band.
(2) Harmonic interference analysis. Harmonic is the integer multiple of the
working frequency or the component whose Fourier series in one cycle is greater
than 1. It analyzes the harmonic component of all transmitters to see whether it falls
in the receiving pass band to form interference. The analysis generally focuses on
the harmonic orders such as the 2nd, 3rd, 5th, and 7th order. If the harmonic analysis
result satisﬁes Eq. (4.5.2), it is considered that there is no harmonic interference
problem, and vice versa.

n × fs −n × Bs
2 n × fs + n × Bs
2

∩

fr −Br
2
fr + Br
2

= 0,
(4.5.2)
where n is the analyzed order.
In this compatibility analysis method, any one of the transmitting sources is
analyzed in pairs with one receiving equipment, and ﬁnally, all the transmitting
sources and receiving equipment are analyzed on a pair-by-pair basis.
Equation (4.5.2) is a relatively rigorous analysis. For speciﬁc transmitting equip-
ment, if the harmonic bandwidth is the same as the fundamental bandwidth, then, in
the ﬁrst bracket of Eq. (4.5.1), the coefﬁcient n multiplied by the bandwidth of the
transmitting equipment can be set to 1.
(3)Subharmonicinterferenceanalysis.Subharmonicreferstotheunwantedhigher
harmonics of the crystal oscillator frequency of a transmitter designed with the
frequency doubling principle. The subharmonic interference analysis is to analyze
the harmonic component of the crystal oscillator frequency of all transmitters to see
whether it falls in the receiving pass band to form interference. The number of orders
of the subharmonic interference analysis can exceed 100. If the harmonic analysis
result satisﬁes Eq. (4.5.3), it is considered that there is no harmonic interference
problem, and vice versa.

n × fc −n × Bc
2 n × fc + n × Bc
2

∩

fr −Br
2
fr + Br
2

= 0,
(4.5.3)
where
f c is the transmitter’s crystal oscillator frequency;
Bc is the transmitter’s crystal oscillator frequency bandwidth.
Similarly, this analysis also requires performing paired analysis by any one of
the transmitting sources and one receiving equipment, and ﬁnally completing the
compatibility analysis between the frequencies of all the transmitting sources and
the receiving equipment pair by pair. For a speciﬁc transmitter crystal oscillator, if
the harmonic bandwidth is the same as crystal oscillator frequency bandwidth, the
coefﬁcient n multiplied by the bandwidth in the ﬁrst bracket of Eq. (4.5.3) can be
set to 1.
Similar tothesubharmonicinterferenceanalysis, higher harmonics has arelatively
great inﬂuence on the crystal oscillator and switching frequencies of all equipment on
thespacecraft(notlimitedtoRFtransmittingequipment),whichisanimportantcause


80
4
Introduction to Spacecraft EMC Prediction Analysis Methods
of conducted emission testing (CE102) and incident radiation emission (RE102) in
thepowerlineduringEMCtest.InthespacecraftEMCanalysisanddesign,thecrystal
oscillator and switching frequency harmonics can also be analyzed by Eq. (4.5.3).
However, it should be noted that the frequency in Eq. (4.5.3) in this case is not
limited to the crystal oscillator frequency of the transmitter, but the crystal oscillator
or switching frequencies of all equipment.
(4) Local oscillator interference analysis. Local oscillator interference is the inter-
ference caused by the leakage EM ﬁeld generated by the local oscillator source in the
superheterodyne receiver. If the shielding or circuit design is not satisﬁed, the local
oscillator source of the receiver is likely to cause various spurious emission leak-
ages, such as fundamental frequency, harmonics, and subharmonics, thus forming a
potential interference. The local oscillator interference analysis is exactly a frequency
analysis of the potential interference of the local oscillator leakage to the receiver
pass band. If the analysis result satisﬁes Eq. (4.5.4), it is considered that there is no
local oscillator interference problem, and vice versa.

n × fLO −n × BLO
2
n × fLO + n × BLO
2

∩

fr −Br
2
fr + Br
2

= 0,
(4.5.4)
where
f LO is the receiver’s local oscillator frequency;
BLO is the receiver’s local oscillator frequency bandwidth.
Similarly, in this analysis, it is required to analyze the pairs by any one of the
transmitting source and one receiving equipment, and ﬁnally analyze all the local
oscillators and receiving equipment. In Eq. (4.5.4), it can be determined whether the
bandwidth multiplication coefﬁcient n in the ﬁrst bracket is set to 1 according to the
speciﬁc local oscillator bandwidth characteristics.
(5) Intermodulation interference analysis. Intermodulation interference means
that two or more signals are mixed in a nonlinear element and produce new signal
frequency components that are equal to the linear combination of an integer multiple
of each signal frequency, and its interference frequency is predictable. Intermodula-
tion interference analysis is to analyze whether this linear combination falls in the
receiving pass band. The intermodulation frequency product analysis is
 fm = |±a × fs1 ± b × fs2 ± · · · ± n × fsN|
Bm = |a × Bs1 + b × Bs2 + · · · + n × BsN| ,
(4.5.5)
where
f m is the center frequency of the intermodulation interference;
Bm is the bandwidth of the intermodulation interference band;
f sN is the center frequency of the Nth transmitting equipment;
BsN is the bandwidth of the Nth transmitting equipment;
a, b, …, n are natural numbers greater than or equal to 1; and a + b + n is the
order for intermodulation interference analysis.


4.5 Spectrum Compatibility Analysis
81
For speciﬁc equipment, the bandwidth in Eq. (4.5.5) can also be calculated using
the following equation:
Bm = max{BsN}.
(4.5.6)
If the intermodulation interference analysis result satisﬁes Eq. (4.5.7), it is
considered that there is no intermodulation interference problem, and vice versa.

fm −Bm
2
fm + Bm
2

∩

fr −Br
2
fr + Br
2

= 0
(4.5.7)
The intermodulation interference analysis method is applied to both the active
intermodulation interference analysis mentioned in this section and the frequency
analysis in the passive intermodulation interference analysis.
(6) Image interference analysis. The image response is a spurious response unique
to a heterodyne receiver for signals with twice the medium frequency (MF) of the
tuning frequency. When the normal signal is one MF lower than the local oscillator
frequency,theimageinterferenceisoneMFhigherthanthelocaloscillatorfrequency,
and vice versa. The image interference analysis is to analyze the interference formed
in the image MF pass band that should not appear. For a heterodyne frequency
converter, only one of the two frequencies generated by the beat is selected, another
unwanted frequency must be ﬁltered out.
(7) Combined interference analysis. Combined interference is often related to the
nonlinearityofthetransmissionchannel.Whenthetransmittedsignalandthereceiver
local oscillator signal are mixed at the mixer to generate a new signal frequency
component, and this frequency component falls in the receiver’s MF band, it will
produce combined interference. The combined interference frequency is equal to a
linear combination of the transmitted signal frequency and an integer multiple of the
local oscillator frequency, and is predictable. The combined interference analysis is
to analyze whether this linear combination falls within the MF band of the receiver.
The combined frequency product analysis is
 fc = |±a × fs ± b × fLO|
Bc = |±a × Bs ± b × BLO| ,
(4.5.8)
where
f c is the center frequency of the combined interference;
Bc is the bandwidth of the combined interference frequency band;
a, b are natural numbers greater than or equal to 1, and a + b is the order of the
combined interference analysis.
If the combined interference analysis result satisﬁes Eq. (4.5.9), it is considered
that there is no combined interference problem, and vice versa.

fc −Bc
2
fc + Bc
2

∩

fr −Br
2
fr + Br
2

= 0
(4.5.9)


82
4
Introduction to Spacecraft EMC Prediction Analysis Methods
The spectrum compatibility analysis plays an important role in spacecraft system-
level EMC analysis, design, and testing. For example, in the design of a remote
sensing satellite, the monitoring frequency was intended to adopt the S-band. In order
to report an appropriate frequency for approval, several rounds of multiple spectrum
compatibility analyses were carried out for frequency planning of the whole satellite.
The determined ﬁnal monitoring frequency ensured that there was no fundamental
interference, no harmonic interference within the 20th order, no intermodulation
interference within the 7th order, or combined interference, which laid a good foun-
dation for satellite RF EMC. In another example of a communication satellite, due to
the limiting values in frequency planning, a second-order intermodulation interfer-
ence frequency component was generated between the Ku-band transponder down-
link frequency and the S-band monitoring downlink frequency and just fell in the
Ku transponder uplink frequency band. This became a satellite EMC problem that
needs to be highly concerned and a targeted designed. A special intermodulation
interference test was also designed in the satellite system-level EMC test, and was
fully veriﬁed to ensure the EMC of the satellite.
The spectrum compatibility analysis is required to be conducted in the early stages
of spacecraft demonstration and design so as to detect the potential EMI risks early
and lay a good foundation for the spacecraft EMC design. Besides, it also needs
to be performed in the later stages of the spacecraft EMC tests. For the frequency
interference problems, special test veriﬁcations should be designed.
4.6
Summary
The EM ﬁelds numerical analysis methods based on Maxwell’s equations are an
important basis for the inter- and intra-system spacecraft EMC analysis. In general,
the full-wave analysis method has high accuracy and is suitable for spacecraft with
not very electrically large size. The HF approximation method can solve the problem
of spacecraft EMC analysis with large physical size or higher frequency bands, but its
accuracy is not as good as that of full-wave analysis. In terms of the full-wave analysis
methods, the time-domain method is applicable for broadband analysis, while the
frequency-domain method is more suitable for narrowband analysis. In terms of RF
compatibility analysis, the spectrum compatibility analysis is the preliminary and
primary process. Inter-antenna mutual coupling is usually analyzed by S-parameter
methods. Due to the complexity, randomness, and nonlinearity of spacecraft system
EMC analysis, the statistical EM analysis method does provide an important idea
to solve practical engineering problems, but its practical application still needs to
be promoted. However, in most cases, the spacecraft system EMC is guaranteed by
safety margins.


4.6 Summary
83
With the implementation of projects such as Internet satellite networking around
the world, the EM spectrum environment in space is more complicated. Theoretically,
the frequency compatibility between the GEO satellite broadband system and the
LEO satellite constellation Internet system can be implemented. However, a more
accurate design is needed, and more innovative analysis methods need to be studied.

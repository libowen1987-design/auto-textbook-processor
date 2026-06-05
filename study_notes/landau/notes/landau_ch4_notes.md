# Landau & Lifshitz《Electrodynamics of Continuous Media》第4章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter IV: Static Magnetic Field

CONSTANT MAGNETIC FIELD

## Section §27: Constant magnetic field

A CONSTANT magnetic field in matter satisfies two of Maxwell’s equations,
obtained by averaging the microscopic equations
l⟨e⟩ 4
divh=0, curlh = -—+—pv. (27.1)
cot ¢
The mean magnetic field is usually called the magnetic induction and denoted
by B:
Ret (27.2)
Hence the result of averaging the first equation (27.1) is
divB = 0. (27.3)
In the second equation, the time derivative gives zero on averaging, since the
mean field is supposed constant, and so we have
curlB = (4n/c)pv. (27.4)
The mean value of the microscopic current density is in general not zero
in either conductors or dielectrics. The only difference between these two
classes is that in dielectrics we always have
f p¥-df = 0, (27.5)
where the integral is taken over the area of any cross-section of the body; in
conductors, this integral need not be zero. Let us suppose to begin with that
there is no net current in the body if it is a conductor, i.e. that (27.5) holds.
The vanishing of the integral in (27.5) for every cross-section of the body
means that the vector pv can be written as the curl of another vector,
| . usually denoted by cM:
pv = ceurlM, (27.6)
where M is zero outside the body; compare the similar discussion in §6.
For, integrating over a surface bounded by a curve which encloses the body
and nowhere enters it, we have {pv-_f = c fcurl M-df = c§M-dl = 0.

114 Constant Magnetic Field §27
The vector M is called the magnetisation of the body. Substituting it in
(27.4), we find

curlH = 0, (27.7)
where the vector H and the magnetic induction B are related by

B= H+4™M, (27.8)

which is analogous to the relation between the electric field E and induction
D. Although H is, by analogy with E, usually called the magnetic field, it
must be remembered that the true mean field is really B and not H.

To see the physical significance of the quantity M, let us consider the
total magnetic moment due to all the charged particles moving in the body.
By the definition of the magnetic moment,t this is

fexpvaV/2c = 3[rxeurlMdr.
Since pv = 0 outside the body, the integral can be taken over any volume
which includes the body. We transform the integral as follows:
frxeurlMdy = — fr x(M xdf)— [(M xgrad) xrdV.

The integral over the surface outside the body is zero. In the second term
we have (Mxgrad)xr = —Mdivr+M = —2M. Thus we obtain

1 =

sft xavaV = [MaV. (27.9)

2c.
We see that the magnetisation vector is the magnetic moment per unit
volume.}

The equations (27.3) and (27.7) must be supplemented by a relation between H and B in order to complete the system of equations. For example,
in non-ferromagnetic bodies in fairly weak magnetic fields, B and H are
linearly related. In isotropic bodies, this linear relation becomes a simple
proportionality:

B= »H. (27.10)
‘The coefficient pis called the magnetic permeability. We also have M = xH,
where the coefficient
x= -1)/4a (27.11)
is called the magnetic susceptibility.

t See The Classical Theory of Fields, §5-9, Addison-Wesley Press, Cambridge (Mass.),
1951; Pergamon Press, London, 1959. |

{ ‘The quantity M is completely determined only when this relation is established. The
relation (27.6) inside the body, and M = 0 outside it, do not uniquely define M: the gradient
of any scalar could be added to M inside the body without affecting (27.6) (cf. the similar
remark in the first footnote to §6).

§27 Constant magnetic field 115

Unlike the dielectric constant «, which always exceeds unity, the magnetic
permeability may be either greater or less than unity. (It is, however, always
positive, as we shall prove in §30. The reason for the differing behaviour of
p and e¢ is discussed in §31.) The magnetic susceptibility x may correspondingly be either positive or negative.

Another, quantitative, difference is that the magnetic susceptibility of the
great majority of bodies is very small in comparison with the dielectric
susceptibility. This difference arises because the magnetisation of a (nonferromagnetic) body is a relativistic effect, of order v?/c?, where v is the
velocity of the electrons in the atoms. t

From the equations div B= 0, curl H =0 it follows (cf. §6) that at a
boundary between two different media we must have

Beebe | Ha re (27.12)
This system of equations and boundary conditions is formally identical with
those for the electrostatic field in a dielectric in the absence of free charges,
differing only in that E and D are replaced by H and B respectively. Since
curl H = 0, we can put H = —grad ¥; the equations for the potential 4
are the same as those for the electrostatic potential. Thus the solutions of
the various problems of electrostatics discussed in Chapter II can be immediately applied to problems with a constant magnetic field. In particular,
the formulae derived in §8 for a dielectric ellipsoid in a uniform electric
field hold also, with appropriate substitutions, for a magnetic ellipsoid in a
uniform magnetic field.

The tangential component of the magnetic induction, unlike its normal
component, is discontinuous at a surface separating two media. The magnitude of the discontinuity can be related to the current density on the surface.
To do this, we integrate both sides of equation (27.4) over a small interval
Al crossing the surface along the normal. We then let A/ tend to zero; the
integral {pv di may tend to some finite limit. The quantity

g= frvat (27.13)
may be called the surface current density; it gives the charge passing per unit
time across unit length of a line in the surface. We take the direction of g
at a given point on the surface as the y-axis, and the direction of the normal
from medium 1 to medium 2 as the x-axis. Then the integration of equation
(27.4) gives

0B, 0Bz 4a 4a
(-Z) dx = —gy = —8.
iz (Ox c €
Since By is continuous, the derivative 9B,/dz is finite, and so its integral
tends to zero with Al. The integral of @B,/€« gives the difference in the

+ The ratio o/c appears with H in the Hamiltonian of the interaction of the body with

the magnetic field, and again in the magnetic moments of the atoms or molecules.

116 Constant Magnetic Field §28
values of Bz on the two sides of the surface. Thus Be,—Biz = —4ng/c.
This can be written in vector form:

4ng/c = nx(Bz—B) = 47n x(Mz—M)), (27.14)
where n is a unit vector along the normal into region 2; the last member of
(27.14) is obtained by using the continuity of the tangential component of H.

## Section §28: Magnetic symmetry of crystals

There is a profound difference between the electric properties of crystals
and their magnetic properties, which results from a difference in the behaviour of charges and currents with respect to a change in the sign of the
time.

The invariance of the equations of motion with respect to this change
means that the formal substitution t > —t, on being applied to any state of
thermodynamic equilibrium of a body, must give some possible equilibrium
state. There are then two possibilities: either the state obtained by changing
the sign of ¢ is the same as the original state, or it is not.

In this section we denote by p(x, y, 2) and j(x,y, 2) the true (microscopic) charge and current densities at any given point in the crystal, averaged
only over time, and not over “physically infinitesimal” volumes as in the
macroscopic theory. These are the functions which determine the electric
and magnetic structure of the crystal respectively.

When t is replaced by —t, j changes sign. If the state of the body remains
unchanged, it follows that j = —j, i.e. j= 0. Thus there is a reason why
bodies can exist in which the function j(x, y, z) is identically zero. In such
bodies, not only the current density but also the (time) average magnetic
field and magnetic moment vanish at every point (we are speaking, of course,
of states in the absence of an external magnetic field). Such bodies may
be said to have no “magnetic structure”, and indeed the great majority of
bodies fall into this category.

The charge density p, on the other hand, is unchanged when t > —t.
There is therefore no reason why this function should be identically zero. In
other words, there are no crystals without “electric structure”, and herein
lies the essential difference, mentioned at the beginning of this section,
between the electric and the magnetic properties of crystals.

Let us now consider crystals for which the change from ¢ to —¢ results
in a change of state, so that j # 0. We shall say that such bodies have a
magnetic structure. First of all, we note that, although j is not zero, there
can be no total current in an equilibrium state of the body, i.e. the integral
JjdV taken over an elementary cell must always be zero.t Otherwise the |

+ It should be emphasised that the cell spoken of here is the true elementary cell, whose
definition involves the magnetic structure of the crystal, and which may be different from
the purely crystallographic cell, which relates only to the symmetry of the charge distribution in the lattice.

§28 Magnetic symmetry of crystals 117
current would produce a macroscopic magnetic field, and the crystal would
have a magnetic energy per unit volume increasing rapidly with its dimensions. Since such a state is energetically unfavourable, it could not correspond to thermodynamic equilibrium.

The currents j may, however, produce a non-zero macroscopic magnetic
moment, i.e. the integral frxjdV, again taken over an elementary cell,
need not be zero. Accordingly, the bodies for which j # 0 may be divided
into two types: those in which the macroscopic magnetic moment is not
zero, called ferromagnetics, and those in which it is zero, called antiferromagnetics.

The symmetry of the current distribution j can be conveniently regarded
as the symmetry of the arrangement and orientation of the magnetic moments
of the individual atoms in the crystal. If j= 0, all these moments are
changing their orientation in the course of time in an entirely random
manner, so that the mean value of each moment is zero. In a ferromagnetic,
the atomic moments are oriented mainly in one direction, causing a non-zero

total moment in each elementary cell. In an antiferromagnetic, the mean
atomic moments are not zero, i.e. they are not randomly oriented, but they
are so arranged as to balance one another in each cell.

What are the possible symmetry groups of the current distribution
(x, y, 2)? This symmetry contains, first of all, the usual rotations, reflections

| and translations, and so the possible symmetry groups of j always include the
usual 230 crystallographic space symmetry groups. These, however, are by
no means all. As has already been mentioned, the substitution t > —t
changes the sign of the vector j. For this reason a new symmetry element
comes in, namely that resulting from the reversal of all currents; we shall
denote this transformation by R. If the current distribution itself has the
symmetry R, it follows that j = —j, i.e. j= 0, and the body has no magnetic structure. A non-zero function j(x, y, 2) may, however, be symmetrical
with respect to various combinations of R with the other symmetry elements
(rotations, reflections and translations). Thus the problem of determining
the possible types of symmetry of the current distribution (the magnetic
Space groups) amounts to the enumeration of all possible groups containing
both the transformations of the ordinary space groups and the combinations
of these with R.

If the symmetry of the current distribution is given, the crystallographic
symmetry of the particle distribution, which is also the symmetry of the
function p(x, y, 2), is determined. It is the symmetry of the space group
which is obtained from the symmetry group of j by formally regarding the
transformation R as the identity (as it is with respect to the function p).

| If only the macroscopic properties of the body are of interest, however, it
is not necessary to know the complete symmetry group of the function
j(*, y, 2). These properties depend only on the direction in the crystal, and
the translational symmetry of the lattice does not affect them. As regards
crystallographic structure, the “symmetry of directions” is specified by the

118 Constant Magnetic Field §28
32 crystal classes. These are the symmetry groups consisting of rotations
and reflections only, and are obtained from the space groups by regarding
every translation as the identity, and the screw axes and glide planes as

simple axes and planes of symmetry. As regards the magnetic properties,
the macroscopic symmetry can be classified by groups (consisting of rotations,
reflections and combinations of these with R) which may be called the magnetic crystal classes. They are related to the magnetic space groups in the
same way as the ordinary crystal classes to the ordinary space groups. They
include, firstly, the usual 32 classes, and those classes augmented by the
element R. These augmented classes are, in particular, the macroscopic
symmetry groups for all bodies having no magnetic structure, but they occur
also in bodies with magnetic structure. This happens if the magnetic space
symmetry group of such bodies includes R only in combination with translations, and not alone.

There are also 58 classes in which R enters only in combination with
rotations or reflections. Each of these becomes one of the ordinary crystal
classes if R is replaced by the identity.t

It should be noted that the occurrence of magnetic structure (ferromagnetic or antiferromagnetic) always involves comparatively weak interactions.t Hence the crystal structure of a magnetic body is only a slight
modification of that in the non-magnetic phase, which usually changes into
the magnetic phase when the temperature is reduced. In this respect ferromagnetics, in particular, differ from ordinary pyroelectrics, but are analogous
to ferroelectrics.

If the magnetic crystal class of a body is specified, its macroscopic magnetic properties are qualitatively determined. The most important of these
is the presence or absence of a macroscopic magnetic moment, i.e. of spontaneous magnetisation in the absence of an external field. The magnetic
moment M is a vector, behaving as an axial vector (the vector product of
two polar vectors) under rotation and reflection, and changing sign under
the operation R. The crystal will possess spontaneous magnetisation if it
has one or more directions such that a vector M in that direction and having

+ These classes are isomorphous with those discovered by A. V. SHuBNIKov for the
symmetry groups of polyhedra with faces of two colours (called by him groups of mixed
polarity). "The element R corresponds to the operation of changing the colour of each face.
See A. V. SHUBNIKOV, Symmetry and antisymmetry of finite figures (Simmetriya i antisimmetriya konechnykh figur), Moscow, 1951. A direct derivation as symmetry groups for
the magnetic properties of bodies is given by B. A. ‘TavcER and V. M. Zaitsev, Zhurnal
éksperimental’not i teoreticheskol fiziki 30, 564, 1956; Soviet Physics JETP 3, 430, 1956.

‘The total number of magnetic space groups is 1651; they are derived (as Shubnikov
groups) by N. V. Brrov, N. N. NeRonova and T. S. Sminnova, Trudy Instituta Kristallografii 11, 33, 1955; A. M. Zamorzakv, Kristallografiya 2, 15, 1957; Soviet Physics: Crystallography 2, 10, 1958.

{ The exchange interaction between the magnetic moments of atoms usually results in
the saturation of the valency bonds and the formation of non-magnetic structures. A magnetic structure results only from the relatively weak exchange interactions between deeplying d and f electrons of atoms of elements in the intermediate groups of Mendeleev’s
system.

§29 The magnetic field of a constant current 119
the above-mentioned properties is invariant under all transformations belonging to the magnetic crystal class concerned.

We must again emphasise the difference between these (macroscopic)
properties and the corresponding ones in electrostatics. The latter are
qualitatively determined by the ordinary crystal class. In particular, a body
is pyroelectric if its crystal class admits the existence of a polar vector P
(the polarisation). It would, however, be entirely wrong to base conclusions
about the existence or otherwise of a macroscopic magnetic moment on the
behaviour of the axial vector M with respect to the transformations of the
non-magnetic crystal class of the body concerned.

As an illustration, let us consider a tetragonal lattice of identical atoms,
with magnetic moments parallel to the tetragonal axis.t The magnetic
crystal class comprises the fourth-order axis C4, two second-order axes
combined with R (C2R and C2R), the plane of symmetry oj perpendicular to the z-axis, and two vertical planes of symmetry combined with
R(ooR and oyWR). This group admits the existence of a vector M along
the tetragonal axis. The crystallographic symmetry class is obtained by
replacing R by unity, i.e. it is the class D4,. This class does not admit the
existence of an axial vector M, since the components M;, My, M, would
change sign on reflection in the planes o®, o, o® respectively.

The properties of bodies with a spontaneous non-zero macroscopic
magnetic moment (ferromagnetics) will be discussed in detail in Chapter V.
In all other crystals, in fairly weak fields, the relation between B and H is
linear:

Bi = virHh, (28.1)
with no inhomogeneous term. The magnetic permeability tensor pix, is symmetrical. This follows from thermodynamic relations which will be derived
in §30, in exactly the same way as the symmetry of the tensor ei (§13).

We may also mention two further phenomena possible in principle. One
is piezomagnetism, resulting from the existence of a linear relation between
the magnetic field and the deformation of a body (analogously to piezoelectricity; see §17). The other results from a linear relation between the '

magnetic and electric fields in a substance, which would cause, for example,
a magnetisation proportional to the electric field.{ Both these phenomena can
occur for certain magnetic crystal symmetry classes. ||

## Section §29: The magnetic field of a constant current

If a conductor carries a non-zero total current, the mean current density

in it can be written as py = c curl M+j. The first term, resulting from the
+ Such, for example, is the lattice of iron in its ferromagnetic phase. Crystallographically,
it is a cubic lattice slightly distorted along one of the fourth-order axes.
| t Effects of this type but quadratic in the field must in principle exist even in isotropic
pes ey Pee iven by I. E. DzvaLosumsxil, Zhurnal éksperimental’not i teoreticheshot } isiki 33, 807, 1957; 37, 881, 1959 (Soviet Physics JETP 6 (33), 621, 19585
10 7), 628, 1960).

120 Constant Magnetic Field §29
magnetisation of the medium, makes no contribution to the total current,
so that the net charge transfer through a cross-section of the body is given
by the integral j j-df of the second term. The quantity j is called the conduction current density.t The statements made in §20 apply to this current; in
particular, the energy dissipated per unit time and volume is E-j.

The distribution of the current j over the volume of the conductor is given
by the equations of §20, which do not involve the magnetic field due to j
itself, if we neglect the effect of this field on the conductivity of the body.
Hence the magnetic field of the currents must be determined for a given
current distribution. The equations satisfied by this field differ from those
in §27 by the presence of a term 4nj/c on the right-hand side of (27.7):

div B = 0, (29.1)

. curlH = 4nj/c. (29.2)

The conduction current density j, which is proportional to the electric field,

does not become infinite, and in particular is finite on a surface separating

two media. Hence the term on the right of (29.2) does not affect the boundary condition that the tangential component of H is continuous.

To solve equations (29.1), (29.2), it is convenient to use the vector potential
A, defined by

B= curlA, (29.3)
so that equation (29.1) is satisfied identically. Equation (29.3) does not
uniquely define the vector potential, to which the gradient of any scalar may
be added without affecting (29.3). For this reason we can impose on A a
further condition, which we take to be

divA = 0. (29.4)
The equation for A is obtained by substituting (29.3) in (29.2). If the linear
relation B = »H holds we have
1
curl (cust) = 4njje. (29.5)
. ye
In this form the equation is valid for any medium, homogeneous or not.
In a homogeneous medium, » = constant, and since
curl curl A = grad divA—AA = —AA
we find from (29.5)
AA = —4ayj[e. (29.6)
If we have two or more adjoining media of different magnetic permeability
vy, the general equation (29.5) has the form (29.6) in each homogeneous

+ The quantity c curl M is sometimes called the molecular current density. This name,
however, is not in complete accordance with the actual physical picture of motion of charges
in a conductor. For example, in a metal the conduction electrons, as well as those moving
in the atoms, contribute to the magnetization .

§29 The magnetic field of a constant current 121
medium, while at the interfaces the tangential component of the vector
(1/#) curl A must be continuous. Moreover, the tangential component of
A itself must be continuous, since a discontinuity would mean that the
induction B was infinite at the boundary.

The field equations are simpler in the two-dimensional problem of finding
the magnetic field in a medium infinite and homogeneous in one direction
(which we take as the z-direction), the currents which produce the field
being everywhere in that direction, with the current density j, = j depending only on # and y. We make the plausible assumption (to be confirmed
by the result) that the vector potential of such a field is also in the z-direction:
A, = A(x, y). The condition (29.4) is then satisfied identically ; the magnetic
field is everywhere parallel to the xy-plane. We denote by k a unit vector
in the z-direction; then

curlA = curl Ak = grad A xk,
1 dA dA
curl (-eusta) = curl (== xk) = —kdiv82S4
7 # #
Hence equation (29.5) becomes
d A An.
div 2284 _ _ ey), (29.7)
B c
| i.e. we in fact obtain one equation for the one scalar quantity A(x, y). For
a piecewise homogeneous medium, (29.7) becomes
AA = —4npjley)/c, (29.8)
with the boundary condition that A and (1/u) 0A/@n are continuous at an
interface.t

The magnetic field is easily found if the current distribution is symmetrical about the z-axis: jz =j(r) (where r is the distance from that axis).
In this case the lines of magnetic force are evidently the circles r = constant.
The magnitude of the field is found at once from the formula

be
fad = = feat (29.9)
which is the integral form of (29.2). Thus
HO) = ler, (29.10)
where J(r) is the total current within the radius r.
+ It should be noticed that the two-dimensional problem with a constant magnetic field
is equivalent to the two-dimensional electrostatic problem of determining the electric field
| due to extraneous charges of density feats) in a dielectric medium. The equation to be
solved in the latter problem is div (e grad ¢) = —4mpex, where ¢ is the field potential;
this differs from (29.7) only in that A, j/c and y are replaced by ¢, pex and 1/e respectively.
The boundary conditions on A and ¢ are the same. A difference occurs, however, on passing
to E and B from ¢ and A respectively. The vectors E= — grad ¢ ‘and B = curl A are
the same in magnitude but in perpendicular directions at any given point.

122 Constant Magnetic Field §29
The reduction of the vector equation (29.5) to a single scalar equation is
possible also if the current distribution is axially symmetrical and has in
cylindrical co-ordinates 7, $, z the form j, =jz =0, jg =j(r, 2). We
seek the vector potential in the form A, = A, =0, Ay=A(r, 2). The
components of the magnetic induction B =curlA are B, = —@A/dz,
B, = (1/r)@(rA)/ér, Bz = 0, and the ¢-component of equation (29.2) gives
-(-=) C7 ~<tral) * ) 29.11
—(-—]+~(—<I-. = ——j(r, 2). E
da \u ox +aleat ] Ce (29.11)
The equations for the magnetic field of the currents can be solved in a
general form in the important case where the magnetic properties of the
medium may be neglected, i.e. where we can put « = 1. The vector potential then satisfies in all space the equation AA = —4zj/c with no conditions
at the interfaces between different media (including the surface of the
conductor on which the current flows). The solution of this equation which
vanishes at infinity ist
A= 13 dV, 29.12)
: Al R (29.12)
where R is the distance from the volume element dV to the point at which
A is to be calculated. In taking the curl of this equation, we must remember
that the integrand j/R is to be differentiated with respect to the co-ordinates
of this point, of which j is independent, so that
curl (j/R) = grad (1/R) xj = —Rxj/R3,
where the radius vector R is from dV to the point under consideration.
Thus
7 1pjxR
B=H= /ae” (29.13)
cJ R8
If the conductor on which the current flows is sufficiently thin (a thin
wire), and if we are interested only in the field in the surrounding space, the
thickness of the wire may be neglected. In what follows we shall often discuss such linear currents. The integration over the volume of the conductor
is then replaced by an integration along its length: the formulae for linear
currents are obtained from those for volume currents by making the substitution jdV ->Jdl, where J is the total current in the conductor. For
example, from formulae (29.12) and (29.13) we have
Jal J j dixR
aa"§S watg SS. 29.14
of R c RS ( )
The latter formula is Biot and Savart’s law.
t See The Classical Theory of Fields, §5-8.

§29 The magnetic field of a constant current 123

This simple formula for the magnetic field of a linear current does not

depend on the assumption that 4 = 1. Since we neglect the thickness of the

conductor, no boundary conditions at its surface need be applied, and the

magnetic properties of the conducting material are of no importance (it may

even be ferromagnetic). The solution of equation (29.6) for the field in the
medium surrounding the conductor is therefore

By fs by f dlxR

A=—|-, B=—|—— 29.15

cJR € R? ( )

whatever the magnetic susceptibility of that medium. Thus the presence

of the medium simply changes the magnetic induction by a factor u. The

field H = B/y is unchanged.

The problem of determining the magnetic field of linear currents can also
be solved as a problem of potential theory. Since we neglect the volume of
conductors, we are in fact determining the field in a region containing no
currents except along certain line singularities. In the absence of currents,
a constant magnetic field has a scalar potential, which in a homogeneous
medium satisfies Laplace’s equation. There is, however, an important
difference between the magnetic field potential and the electrostatic potential: the latter is always a one-valued function, because curl E = 0 in all

| space (including charged regions) and so the change in the potential in going
round any closed contour (i.e. the circulation of E round that contour) is
zero. The circulation of the magnetic field round a contour enclosing a
linear current is not zero, but 47J/c. Hence the potential changes by this
amount on each passage round a contour enclosing a linear current, i.e. it is
a many-valued function.

If the currents lie in a finite region of space (and » = 1 everywhere), the
vector potential of the magnetic field at a great distance from the conductors
is

A= “xRIR, (29.16)
where

M = [rx jaV 2c (29.17)
is the total magnetic moment of the system.t

For a linear current, this becomes

M = Ihe x dlj2c,
and can be transformed into an integral over a surface bounded by the line
of the current. The product df = }r x dl is equal in magnitude to the area

t See The Classical Theory of Fields, §5-9. In the derivation there given, we use explicitly
the idea of a current as the result of the motion of individual charged particles. Such a

| derivation is, of course, quite general, but formula (29.16) can also be obtained by macroscopic arguments (see Problem 4).

124 Constant Magnetic Field §29
of the triangular surface element formed by the vectors r and dl. The
vector fdf is independent of the particular surface (bounded by the current)
over which it is taken. Thus the magnetic moment of a closed linear current
is

M = J fase. (29.18)
In particular, for a plane closed linear current the magnetic moment is
simply JS/c, where S is the area of the plane enclosed by the current.

To conclude this section, we may briefly discuss the energy flux in a
conductor. The energy dissipated as Joule heat in the conductor is derived
from the energy of the electromagnetic field. In a steady state, the “equation
of continuity” which expresses the law of conservation of energy is

—divS =j-E, (29.19)
where S is the energy flux density, given in a conductor by

S = cExH/4n, (29.20)
which is formally the same as the expression for the Poynting vector for the
field in a vacuum. This is easily verified directly by calculating div S from
the equations curl E = 0 and (29.2), when we obtain (29.19).

Formula (29.20) also follows independently from the obvious condition
that the normal component of S must be continuous at the surface of a
conductor, if we use the continuity of E; and H; and the validity of (29.20)
in the vacuum outside the body.

PROBLEMSt{

ProsieM 1. Determine the scalar potential of the magnetic field of a closed linear current.

SOLUTION. We transform the line integral into one over a surface bounded by the line,
obtaining

alga _t ij A
—- “SR =) MxeradE,
J 1
B= curl = —7 { (at-grad) grad 5
c R
(where we have used the fact that A(1/R) = 0). Since B = —grad 4, we have for the
scalar potential ; 1 fea
o- {fated ~2/e
The integral is, geometrically, the solid angle Q subtended by the closed contour at the point
. considered. The above-mentioned many-valuedness of the potential is seen from the fact
that, as this point describes a closed path round the wire, the angle 0 changes suddenly
from 2m to —2m.

Prosiem 2. Find the magnetic field of a linear current flowing in a circle of radius a.

SoLUTION. We take the origin of cylindrical co-ordinates r, ¢, x at the centre of the circle,
with the angle ¢ measured from the plane which passes through the z-axis and the point at

+ In Problems 1-4, » =1.

/
§29 The magnetic field of a constant current 125
which the field is calculated. ‘The vector potential has only one component, Ay = A(r, 2),
and by formula (29.14) we have
J {cos ¢ dl
end 2f R
/
~ 4] ___sentas
a ) Viet+r+2?—2ar cos $)
Putting 9 = #($—n), we find
4J fa
= /t1a-naK-.
4e= 2/210 -H9K-2),
where k* = 4ar/[(a+r)*+2"], and K and E are complete elliptic integrals of the first and
second kinds:
. _
do
= f__*% _ = [ Vd—# sin’) a0.
K | acme E Jvc sin®) do
The components of the induction are
By = 0,
aap _ J de AL rt at
Ce ene iareel [-*+ Gopal
1a J 2 [ apt }
_ a rr————=—=“‘“=E
Ae =o aan Goneeat
| Here we have used the easily verified formulae :
aK EE Kak EK
ak R(1—#) OR? ok k
On the axis (r = 0) we have By = 0, Bs = 2natJ/c(a?+2%)*/2, as can also be found by
straightforward calculation.

Prose 3. Determine the magnetic field in a cylindrical hole in a cylindrical conductor
of infinite length carrying a current uniformly distributed over its cross-section (*Fig. 17).*
y| Y

(|S we
Fic. 17

126 Constant Magnetic Field §30

SoLution. If there were no hole, the field in the cylinder would be given by H’s =
—2njyle, H’y = 2njxle. The dimensions and axes are as shown in *Fig. 17. If a current of*
density —j were to flow in the inner cylinder, it would produce a field Hs = 2njy’/c, H’’y
= —2njx’//c. The required field in the hole is obtained by superposing these two fields.
Since x—x’ = OO’ =h, and y = y’, we have Hz = 0, Hy = 2njh[c = 2AJ|(8?—a®)e, ive. a
uniform field in the y-direction.

PROBLEM 4. Derive from (29.12) the formula (29.16) for the vector potential of the field
far from the currents.

SouurIoN. We write R = Ro—r, where Ro and r are the radius vectors from the origin
(situated somewhere among the currents) to the point considered and to the volume element
dV respectively. Expanding the integrand in powers of r and using the fact that [jdV = 0,
we have As & (Ru/eR3) f xj: dV. The suffix 0 to R is omitted. Integrating by parts the
identity J xie divj dV = 0 gives § (jexe+jexs) dV = 0. Hence we can write

Ag = (Re/2cR) § (sage —xaje) AV,
which is (29.16).

PRoBLEM 5. Determine the magnetic field produced by a linear current ina magnetically
anisotropic medium (A. S. VicLIN).

SoLuTION. In the anisotropic medium surrounding the conductor we have

div B = pu dHe/ ax = 0, (1)
where jx is the magnetic permeability tensor of the medium. Instead of introducing the
vector potential by B = curl A, we use another vector C defined by

He = esuipem2Cy/ xm, Q)
where eri is the antisymmetrical unit tensor. Then equation (1) is again satisfied identically.
‘We can also impose on the vector C thus defined the condition

diy C = aC;/ax; = 0, (3)
Substituting (2) in curl H = 4aj/ce, we obtain es 0Hi/Oxe = —pep2Cs/OxnOxy = 4ajile
(using the condition (3) and the fact that eseimn = 8im3en—8in3em). The equation thus
obtained for C is the same in form as that for the electric field potential resulting from
charges in an anisotropic medium (§13, Problem 2). The solution is

cu 1 f jdV

ed V(laletaReRe)”
where |u| is the determinant of the tensor iz, and R the radius vector from the point considered to dV. For a linear current we have
c= J § dl
evel J Vue RRs)”

## Section §30: Thermodynamic relations in a magnetic field

The thermodynamic relations for a magnetic substance in a magnetic
field are, as we shall see, very similar to the corresponding relations for a
dielectric in an electric field. Their derivation, however, is quite different
from that given in §10. This difference is ultimately due to the fact that a
magnetic field, unlike an electric field, does no work on charges moving in it
(since the force acting on a charge is perpendicular to its velocity). Hence,
to calculate the change in the energy of the medium when a magnetic field is
applied, we must examine the electric fields induced by the change in the
magnetic field and determine the work done by these fields on the currents
which produce the magnetic field.

§30 Thermodynamic relations in a magnetic field 127

Thus the equation which relates electric and variable magnetic fields must
be used. This equation is

1B
1E = --—; 30.1
cur! an (30.1)
it follows immediately on averaging the microscopic equation (1.3).

During a time 8, the field E does work 8tf j-EdV on the currents j.
This quantity with the opposite sign is the work 5R “done on the field” by
the external e.m.f. which maintains the currents. Substituting

j =c curl H/47,
we have
R= ~8:2{E-eurl av
€ ¢
= af div(E xH)dV— oe [a- curl EdV.

4n. Ann.
The first integral, on being transformed to an integral over an infinitely
distant surface, is seen to be zero. In the second integral we substitute
curl E from (30.1) and put 5B = 5t @B/ét for the change in the magnetic
induction, obtaining finally

| : 8R = [H-3BdV//4n. (30.2)

This formula appears entirely analogous to the expression (10.2) for the
work done in an infinitesimal change in the electric field. It must be pointed
out, however, that the physical analogy between the two formulae is actually
not complete, since H, unlike E, is not the mean value of the microscopic
field.

Having derived formula (30.2), we can write down all the thermodynamic
relations for a magnetic substance in a magnetic field by analogy with those
given in §10 for a dielectric in an electric field, simply replacing E and D
by H and B respectively. We shall give some of these formulae here for
purposes of reference. The differentials of the total free energy and the
total internal energy are

8F = — ¥ST+ [H-3BdV/4z,
(30.3)
du = T39+ [H-3BdV/4z,
|
and those of the corresponding quantities per unit volume are
dF = —SdT+dp+H-dB/47, cays
dU = TdS+fdp+H-dB/4z. 4)

128 Constant Magnetic Field §30
We need also the thermodynamic potentials
U = U-H-B/4r, F = F-H-B/4z, (30.5)
for which
df = — SdT+{dp—B-dH/47, 40.6
d0 = TdS+fdp—B-dH/4z. (30.6)
If the linear relation B = “H holds, we can write the expressions for all
these quantities in the form
U = US, p)+B%/8np, F = Fo(T,p)+B2/8xp, De)
O = US, p)—pH?/8a, fF = F(T, p)—pH?/8. :
The work 5R (or, what is the same thing, the change SF at constant
temperature) can be written in a different form, in terms of the current
density and the vector potential of the magnetic field. For this purpose we
put 6B = curl $A and
1
8F)p = —|H-curlS5AdV
(Fn = = [Hour
= * {ci (Hx3A)dV+ fa 1HaV.
=-5 liv (H x 8A) ra “curl .
The first integral is again zero, and the second gives
(Fr = [j-8AdV Ic. (30.8)
A similar transformation gives
(Fn = fA-3dV/c. (30.9)
It is useful to note that in macroscopic electrodynamics the currents
(sources of the magnetic field) are mathematically analogues of the potentials, not of the charges (the sources of the electric field). This is seen by
comparing formulae (30.8) and (30.9) with the corresponding results for an
electric field:
(Fr =[spdV, (SFr = - fossa (30.10)
(see (10.13), (10.14)). We observe that the charges and potentials appear in
these formulae in the opposite order to the currents and potentials in formulae (30.8), (30.9). |
On account of the complete formal correspondence between the thermodynamic relations (expressed in terms of field and induction) for electric
and magnetic fields, the thermodynamic inequalities derived in §18 can also

§31 The total free energy of a magnetic substance 129
be applied to magnetic fields. In particular, we have seen that it follows
from these inequalities that « > 0. In the electric case this result was of no
interest, because it was weaker than the inequality « > 1 which follows on
other grounds. In the magnetic case, however, the corresponding inequality
» > Ois very important, as it is the only restriction on the values which can
be taken by the magnetic permeability.

## Section §31: The total free energy of a magnetic substance

In §11 expressions have been derived for the total free energy F of a
dielectric in an electric field. One of the thermodynamic properties of this
quantity is that the change in it gives the work done by the electric field on
the body when the charges producing the field remain constant. In a magnetic field a similar part is played by the free energy #, since for given
currents producing the field the change in ¥ is the work done on the body.
The following derivation is entirely analogous to that given in §11. The
“total” quantity F is defined as
9?
$= f(#+Z) av, (1.1)
8n,
where § is the magnetic field which would be produced by the given currents in the absence of the magnetisable medium. The plus sign appears in
the parenthesis (instead of the minus sign as in (11.1)) because the value of
F for a magnetic field in a vacuum is — f(§?/87) dV (see (30.7). The
integration in (31.1) is taken over all space, including the volume occupied
by the conductors in which flow the currents producing the field. +
Let us calculate the change in F (for a given temperature and no departure from thermodynamic equilibrium in the medium) corresponding to an
infinitesimal change in the field. Since 8f = —B-5H/47, we have
| sF = — [(B-SH-§-8§) dV/4a
= — [(-$)-39 dV /4r— [B-(GH-3§) dV /4a— [(B—H)-38 dV /4z.
(31.2)
Introducing the vector potential 2 of the field §, we can write in the
first term
] (H-$)-3 = (H-§)-curl 5a
| = div [8% -(H—§)]+5%-curl(H-§).
+ In §11 we took the integration in (11.1) over all space except the volume occupied by
the charged conductors producing the field. This was possible because there is no electric
| field in a conductor, charged or not. ‘There is a magnetic field, however, inside the conductors which carry the currents, and they cannot be excluded in calculating the total free energy.

130 Constant Magnetic Field $31
By definition, the fields H and § are produced by the same currents j, the
distribution of which over the volume of the conductors is (see §29) independent of the field which they produce, i.e. is independent of the presence
or absence of magnetic substances in the surrounding medium. Hence
curl H and curl § are both equal to 4yj/c, and so curl(H-§) =0.
The integral of div[8%-(H—$)] is transformed into an integral over an
infinitely distant surface, and so vanishes.

Similarly, we see that the second term on the right of (31.2) is zero; thus

aF = — [(B-H)-39dV/4r
= —JM.sgar. (31.3)
The expression which we have obtained for 8¥ is exactly similar to (11.3)
for the electrostatic problem. In particular, in a uniform magnetic field §
we have for d¥ an expression analogous to (11.5):
: dF = —7AT-M-Ag, (31.4)
where M is the total magnetic moment of the body.

Without repeating the subsequent calculations, we shall write down the
following formulae by analogy with those in §11. If the linear relation
B =H holds, we have |

$-FAV,T) = -f3H-Mav. (31.5)
In particular, if the external field is homogeneous, then
F-FV,T) = -3H-M. (31.6)
In the general case of an arbitrary relation between B and H, ¥ can be |
calculated from the formula
H-B
#= {(F ——_ 4M. ) av
+ Mo
H-B
5 J(F-<S-a-5) av. (31.7)
: 8x

In §11 we gave also the simpler formulae obtained when the dielectric
susceptibility is small. The analogous case for the magnetic problem is
especially important because, as mentioned above, the magnetic susceptibility of the majority of bodies is indeed small. In this case

F-Fo = -4y[ Grav. (31.8)

§32 The energy of a system of currents 131
We can also derive results for the magnetic field analogous to those
obtained in §14. These concern the change in the thermodynamic quantities
resulting from an infinitesimal change in the magnetic permeability y, the
field sources being assumed unchanged. It is clear from the foregoing that
we must consider the change in F, and not that in F as in §14. We shall not
repeat the derivation, which is similar to that of (14.1), but merely give the

result:
- f 3 HAV 8m. (31.9)

In §14 we used this formula to deduce that the dielectric susceptibility of
any substance is positive. In the magnetic case we cannot draw this conclusion, and the magnetic susceptibility may be of either sign. The reason for
this marked difference is that the Hamiltonian of a system of charges moving
in a magnetic field contains not only terms linear in the field (as in the
electric case) but also quadratic terms. Hence, in determining the change
in the free energy of the body in the magnetic field by means of perturbation
theory as in (14.2), we have a contribution in the first approximation as well
as the second. In such a case no general conclusion can be drawn concerning
the sign of the variation. It is positive for paramagnetic bodies and negative
for diamagnetic ones.

In §14 we also drew conclusions concerning the direction of motion of
bodies in an electric field. Similar conclusions follow from (31.9), but, since
» may be either greater or less than 1, there is no universal result. For
example, in an almost uniform field paramagnetic bodies (u > 1) move in
the direction of H increasing, and diamagnetic bodies (u < 1) in the opposite
direction.

## Section §32: The energy of a system of currents

Let us consider a system of conductors with currents flowing in them
and assume that neither the conductors nor the medium surrounding them
are ferromagnetic, so that B = »H everywhere. According to §30, the total
free energy of the system is given in terms of the magnetic field of the
currents by

F = [H-BaV/8x. (32.1)
Here we omit the quantity Fo, which is a constant (at a given temperature)
and is not related to the currents. The integration in (32.1) is taken over all
space, both inside and outside the conductors. .
The same energy can also be expressed in terms of the currents by means
of the integral
F = [A-jaV 2c; (32.2)

132 Constant Magnetic Field §32
cf. the derivation of (30.8) from (30.2). Here the integration extends only
over the conductors, because j = 0 outside them. :
Since the field equations are linear, the magnetic field can be written as
the sum of the fields resulting from each current alone with no current in
the other conductors: H = Hy. Then the total free energy (32.1) is
F =TF qt X Far, (32.3)
@ ad
where
_ f Hy-BadV/87, Fav = [Ha-BodV/4z. (32.4)
We have put Fay = Fog, since Hy+By = wHa-Hy = Hy-Ba, where yu is the
magnetic permeability at any point. The quantity Faq may be called the
free self-energy of the current in the ath conductor, and Fqy the interaction
energy of the ath and bth conductors. It should be borne in mind, however,
that these names are strictly correct only if the magnetic properties of both
the conductors and the medium are neglected. Otherwise the field, and
therefore the energy, of each current depend on the position and magnetic
permeability of the other conductors.
The quantities (32.4) can also be expressed in terms of the currents ja
in each conductor, in accordance with formula (32.2):
Fan = [jarAadWal2e, Fan = [jarAvdVale = [jeAadVo]e. (32.5) |
The integral in Faq is here taken only over the volume of the ath conductor;
Fp can be written as either of the two expressions, in which the integration
is over the volume of the ath and bth conductor respectively.
When the distribution of the current density over the volume of the
conductor is given, Faq depends only on the total current Ja passing through
a cross-section. Both the current density j and the field which it produces !
will be proportional to Ja. Hence the integral Faq is proportional to Jn2,
and we write it
Fan = LaaJa?/2c?, (32.6)
where Iga is called the self-inductance of the conductor. Similarly, the
interaction energy of two currents is proportional to the product JoJo:
Fav = LarJaJo|c?. (32.7)
The quantity Zap is called the mutual inductance of the conductors. Thus |
the total free energy of a system of currents is |
1 1 1
F = gt 2 baale +g D Laredo = Pad 2 label (32.8)

§32 The energy of a system of currents 133

The condition that this quadratic form should be positive definite places
certain restrictions on the values of the coefficients. In particular Lag > 0
for all a, and LgaLep > Lar?.

The calculation of the energy of currents in the general case of arbitrary
three-dimensional conductors requires a complete solution of the field
equations, and is a difficult problem. It becomes simpler if the magnetic
permeability of both the conductors and the surrounding medium can be
taken as unity. It should be noted that the energy of the currents is then no
longer dependent on the thermodynamic state (in particular, on the temperature) of the bodies, and hence the free energy in the above formulae may
be referred to simply as the energy.

For » =1 the vector field potential due to the currents j is given by
formula (29.12). Hence the self-energy of the ath conductor is

Fan = zal fever, (32.9)
2c2 R
where both integrations are taken over the volume of the conductor considered, and R is the distance between dV and dV’. Similarly, the mutual
energy of two conductors is
1 ¢ (jaf
| Fn=5 f f *Paved¥y (32.10)
where dV, and dV» are volume elements in the two conductors.

The mutual energy of two linear currents is particularly easy to calculate.
In formula (32.10) we change from volume currents to linear ones by replacing jadVq and jodV» by Jadla and Jodly respectively, and we find that the
mutual inductance is Lap = ffdlg-dly/R. In this approximation, therefore, Lg» depends only on the shape, size and relative position of the two
currents, and not on the distribution of current over the cross-section of each
wire. It must be emphasised that this simple formula can be obtained for
linear currents without imposing the condition that 1 = 1. In the approximation where the thickness of the wires is neglected, their magnetic properties have no effect on the field which they produce, and therefore no
effect on their mutual energy. If the magnetic permeability 4 of the medium
surrounding the wires is different from unity, the vector potential is, by
(29.15), simply multiplied by 4, and therefore so is the magnetic induction.
The mutual inductance is therefore multiplied by the same factor, so that

Lap = vf dla-dla/R. (32.11)

The self-inductance of linear conductors is much more difficult to calculate;
we shall discuss it in §33.

The total energy of a system of linear currents can be written in still

’
134 Constant Magnetic Field $32
another form. To do this, we return to the integral (32.2), which for linear
currents becomes
1
Fa A-dla, 32.

gah Atl (32:12)
where A is the vector potential of the total field at the element dl, of the ath
conductor. The main error in going from (32.2) to (32.12) arises from
neglecting the change in the field (including the field of the current considered) over the cross-section of the wire. Each of the contour integrals in
(32.12) can be transformed into a surface integral:

f Ardla = fourl A-df = JB-d,
ie. it is the flux of the magnetic induction or magnetic flux through the
circuit of the ath current. We denote this flux by ®. Then
1
F=5 2 Ta Pa. (32.13)

Similarly, the free energy F of a linear current J in an external magnetic
field, ie. the energy without the self-energy of the field sources, can be
expressed in terms of the magnetic flux. Evidently

F = Jc, (32.14)
where © is the flux of the external field through the circuit of the current J.
If the external field is uniform, and « = 1 in the external medium, then
® = §- fdf. Introducing the magnetic moment of the current in accordance with (29.18), we have ¥ = M-§.

Knowing the energy of a system of currents as a function of their shape,
size and relative position, we can determine the forces on the conductors by
simply differentiating with respect to the appropriate co-ordinates. Here,
however, the question arises which characteristics of the currents should be
kept constant in the differentiation. It is most convenient to differentiate
at constant current. In this case the free energy is represented by ¥, and
so the generalised force Fg in the direction of a generalised co-ordinate g is
Fy = —(@F/0q)7,7. The suffixes show that the differentiation is effected
at constant current and constant temperature. Since we omit the term
independent of the currents in the free energy, F and F differ only in
sign, and so

oF OF 1 Lav
F,--() -(“) -=— i, 32.15
* (a), (a), aa Dd 0q ¢ ) |
here and henceforward the suffix T to the derivatives is omitted, for brevity.

§32 The energy of a system of currents 135
In particular, the forces exerted on a conductor by its own magnetic field
are given by the formula
F, u Hed 32.16)
0 al ap (32.
where L is the self-inductance of the conductor. The nature of these forces
can be seen as follows. For given current (and temperature), ¥ tends to be
a minimum. Since ¥ = ~LJ?/2c®, this means that the forces on the conductor will tend to increase its self-inductance. The latter, having the
dimensions of length, must be proportional to the dimension of the conductor. Thus the effect of the magnetic field is to increase the size of the
conductor.
For a current in an external magnetic field we havet
CO ES (32.17)
In all the above formulae for the energy it is assumed that there is a
linear relation between the magnetic field and induction. In the general
case where this relation is arbitrary, analogous differential relations can be
set up. The change in the free energy resulting from an infinitesimal change
in the field (at constant temperature) is, by (30.8), 5F = fj-SAdV/c or,
for a system of linear currents,
1
SF =- SA-dlg.
| cae a
| Proceeding as in the derivation of (32.13) from (32.12), we have
1
8F =- SDy. 32.18
7D Jabe (32.18)
| Similarly, we find from (30.9)
1
3F = ~ 2D Ooo (32.19)
Thus we can say that, for a system of linear currents, F is the thermodynamic potential with respect to the magnetic fluxes, and ¥ with respect
to the currents, the two potentials being related by
1
F= a Jaa. (32.20)
+ The factor $ which appears in (31.6) is absent in (32.17) because the magnetic moment
of the current in the latter equation is independent of the field, whereas the magnetic moment
in (31.6) is itself due to the field.
To

136 Constant Magnetic Field §33
Whatever the magnetic properties of the substance, therefore, the thermodynamic relations
Jaleo = 2@F 00g, Dale = —2F [Ja (32.21)
hold. If these formulae are applied to the case where the field and induction
are linearly related, so that F is given by (32.8), we obtain
1
O = — . 32.22)
a cael C (32.22)
Thus the inductances are the coefficients of proportionality between the
magnetic fluxes and the currents which produce the magnetic field. The
product LgpJe/c is the magnetic flux through the circuit of the current Ja
due to the current Jy(b # a), and LaaJalc is that due to the current Jy itself.

## Section §33: The self-inductance of linear conductors

In calculating the self-inductance of a linear conductor its thickness
cannot be entirely neglected as it was in calculating the mutual inductance of
two conductors. If it were, we should obtain from (32.9) the self-inductance
L = §§dl-dl’/R, where both integrals are taken along the same circuit,
and this integral is logarithmically divergent because of the contribution
from small R.

The exact value of the self-inductance of a conductor depends on the
distribution of current in it, which may vary with the manner of excitation
of the current, i.e. with the manner of application of the electromotive force.
For a linear conductor, however, the self-inductance does not, to a fairly
high accuracy, depend on the distribution of current over the cross-section. t

Let us write the self-inductance as L = Le+Ly, where Le and Ly result
from the magnetic field energy outside and inside the conductor respectively. For a linear conductor, the “external” part L, makes the main
contribution to the self-inductance. This is because most of the magnetic
energy of a closed linear circuit resides in the field at distances from the
wire large compared with its thickness. For the energy per unit length of
an infinite straight wire is

(1e]8m) JH2-2err dr = (e]8x) S(2Tlor)-2er dr = (HeJ?|e2) Serr
where r is the distance from the axis of the wire and se the magnetic permeability of the external medium. This integral diverges logarithmically for |
large r. For a closed linear circuit, of course, this divergence disappears,
because the integral is “cut off” at distances of the order of the dimension

+ More precisely, it is independent of the distribution of current provided that the current |
density varies appreciably only over distances comparable with the thickness a of the wire.
If, however, the distribution is such that the current density varies appreciably over distances
small compared with a (as happens, for particular reasons, in the skin effect and in superconductors), then the self-inductance does depend on the distribution.

§33 The self-inductance of linear conductors 137
of the circuit. We obtain an approximate value for the energy on multiplying this integral by the total length / of the wire, and taking / as the upper
limit and the radius a of the wire as the lower limit. The result is (ueJ*l/c?) log(I/a), and hence the self-inductance is
L = 2 log(i/a). (33 1)
This expression is said to be of logarithmic accuracy: its relative error is of
the order of 1/log(//a), and the ratio I/a is assumed to be so large that its
logarithm is large.

A particular case of a linear conductor is a solenoid, which consists of a |
wire wound in a helix, with the turns very close together. Neglecting the
thickness of the wire and the distance between the turns, we have simply a
conducting cylindrical surface with a “surface” conduction current on it.
The equation curl H = 4xj/c within the conductor is here replaced by the
boundary condition.

| nx(H2—M)) = 47g/c, (33.2)

_ where g is the surface current density, Hi and He the fields on each side of
the surface, and n the unit normal vector into medium 2; cf. the derivation
of (27.14).

If the solenoid is of infinite length, the magnetic field which it produces

can be found very simply. The surface currents flow in circles, and their
density g = nJ, where J is the current in the wire and n the number of turns
per unit length of the solenoid. The field outside the cylinder is zero; the
_ field inside is uniform and along the axis of the cylinder, and is H = 4anJ|c.
For this field evidently satisfies the equations divH = 0, curlH =0 in
all space outside the conducting surface, and also the boundary condition
(33.2) at that surface.
Accordingly, the field energy per unit length of the cylinder is
| peEarb2/8r = 2n2n?Bg]?/c2,
| where b is the radius of the cylinder and je pertains to the material within
the solenoid. Neglecting the end effects, we can apply this formula also to
a solenoid whose length h is finite, but large compared with b. Then the
self-inductance is
L = 4n2n2b%hie = Impenbl, (33.3)
where | = 27bnh is the total length of the wire. ‘The greater self-inductance
of a solenoid as compared with that of a straight wire of equal length (cf.
(33.1)) is, of course, due to the mutual induction between adjoining turns.

t The assertion made above that the self-inductance is independent of the current .
distribution actually applies not only to the approximation (33.1) but also to the next
approximation, in which terms not containing the large logarithm are included (or, what
is the same thing, the argument of the logarithm includes a coefficient); see the Problems at
the end of this section.

138 Constant Magnetic Field §33
PROBLEMSt

PronieM 1, Determine the self-inductance of a closed circuit of thin wire of circular crosssection.

SoLuTiN. ‘The magnetic field in the wire can be taken to be the same as that inside an
infinite straight cylinder: H = 2Jr[ca?, where 7 is the distance from the axis of the wire and
aits radius. Hence we find the internal part of the self-inductance:

28
= | mar = 4m, 0)
where J is the length of the wire.

To calculate Ls, we notice that the field outside a thin wire is independent of the distribution of current over its cross-section. In particular, the energy F, of the external magnetic
field is unchanged if we assume that the current flows only on the surface of the wire. The
field inside the wire is then zero, and F, may be calculated as the total energy from formula
(32.2). On account of the assumed surface distribution of the current, the integral in this
formula becomes a line integral along the axis of the wire, and so the external part of the
self-inductance is 
ct J
La ee faired,
where the value of A in the integrand is taken at the surface of the wire. In obtaining this
formula we also use the fact that, in the approximation used here, the field is constant over
the perimeter of a cross-section.

Having reduced the problem to that of calculating A for r = a, we now make a different
assumption concerning the current distribution, namely that the whole current J flows
along the axis of the wire. The field on the surface of the wire is, in the approximation
considered, unchanged by this assumption (nor would it be changed for a straight wire of
circular cross-section), ‘Then, by formula (29.14), we have

Af
Alea =~] ><
(Alr-s= "19% 2
where R is the distance from the element dl of the axis to a given point on the surface of the
wire. We divide the integral into two parts, one for which R > A and the other for which
R< A, where A is a distance small compared with the dimension of the circuit but large
compared with the radius a of the wire. In the integral where R > A, a may be neglected
and R taken simply as the distance between two points on the circuit. ‘The vector integral
where R < A may be assumed to be along the tangent at the point considered. Denoting by
t the unit vector in that direction, we have
at fal
S) xt [—S = 2t sinh-4 AV)
[fil... ‘yam as
Rea ca
& 2t log(2A/a).
‘This expression can be written as the integral
f aur,
pointe
where R is again the distance between points on the circuit. Adding the two integrals for
R> Aand R< A, we obtain Aa
Alea=2 [ 5 |
Dt
for which the arbitrary parameter A has disappeared, as it should.

} In Problems 1-6 we put e = 1. =

{ Assimilar procedure was used to calculate the capacity of a thin ring in §2, Problem 4.

|

§33 The self-inductance of linear conductors 139

The final result is therefore

dl-av’
t= [[. @
oie
The integration here extends over all pairs of points on the circuit whose distance apart
exceeds ta.

PronteM 2. Determine the self-inductance of a thin wire ring (of radius b) of circular crosssection (of radius a).

SoLUTION. ‘The integrand in (2), Problem 1, depends only on the central angle ¢ subtended
by the chord R, and R = 2b sin 34, while dl-dl’ = didi’ cos $. Hence

5
“2nb-b
L,=2 f c08 92nd b ds 4 ot log tan 440-2 cos 44).
2b sin 3d
$0
The lower limit of integration is determined from 25 sin 440 = 4a, whence So ~ a/2b.
Substituting this value and adding Ly = mb, we have to the required accuracy
L = 4abflog (8b/a)—2+4u1].
In particular, for ys = 1 we obtain
L = 4nbflog (8b/a)—(7/4)].

ProsieM 3. Determine the extension of a ring of wire (with ys = 1) under the action of
the magnetic field of a current flowing in it.

Souurion. The internal stresses parallel and perpendicular to the axis are, by (32.16),
given by

yt a jy? aL
2¢, = 22 -f#
| nity Say) Unabou= 35-5
Substituting L from Problem 2, we have
as [s 8 3] Bt
=| 9% 3 = 2
ae L8G 4) 2 oR
Hence the required relative extension of the ring ist
Ab 1 ui % 3
pm Bl teow) = Taplow yz t2):
where Eis Young’s modulus and Poisson's ratio for the wire.

Prosiem 4. Determine the self-inductance per unit length of a system of two parallel
straight wires (with 44 = 1) having circular cross-sections of radii a and b, with their axes
a distance h apart, and carrying equal currents J in opposite directions (*Fig. 18).*

ee eA
A
_ Fic, 18 |
| + See Theory of Elasticity, §5, Pergamon Press, London, 1959.

140 Constant Magnetic Field §33

SoLuTIon. The vector potential of the magnetic field of each current is parallel to the
axes of the wires, and so the two vector potentials can be added algebraically. For the magnetic field of wire 1, with a uniformly distributed current +J, we have in cylindrical coordinates

A= Ac- 5) forr<a,
cA a’
A:= Ac-1-2 toez) forr> a,
where C is an arbitrary constant; A; is continuous at the surface of the wire. The formulae
for wire 2 are obtained by substituting b for a and changing the sign of J. Integration over
the cross-section of wire 1 in formula (32.2) gives
cia f ( ne ( ra }
gf (2c ame)
aa
aw ne W+n2—2hri cos $) _zZ ( 4)
~ tea |) (1-3 Hoe = |r db drs = 3(5 +2 lo 5).
‘The integration over the cross-section of wire 2 gives the same thing with a in place of }.
‘The required self-inductance per unit length of the double wire is therefore
L =1+2 log(h?/ab).
ProBLEM 5. Determine the self-inductance of a toroidal solenoid.
2
ax DD,
Ni ae ay,
Fic. 19

SOLUTION. We regard the solenoid as a toroidal conducting surface carrying surface
currents of density g = NJ/2nr, where N is the total number of turns and J the current;
the co-ordinates and dimensions are as shown in *Fig. 19. The magnetic field outside the*
solenoid is zero, and inside the solenoid Hir = Hiz = 0, Hig = 2NJlcr, where 1, x, ¢ are
cylindrical co-ordinates; for this solution satisfies the equations divH = 0, curlH =0
and the boundary condition (33.2).t ‘The energy of the magnetic field in the solenoid is

J@e/8n) AV = (NY*c*)§z dr/r,
where the integration is taken along the perimeter of the cross-section, and is easily effected
by putting z = asin 8, r = b+a.c0s 8. The self-inductance is found to be
L = 42N—V(P—a)]. |

ProBLem 6. Determine the end-effect correction of order l/h to the expression (33.3)
with #45 = 1) for the self-inductance of a cylindrical solenoid.

t It is valid also for an annular solenoid of any cross-section.

§34 Forces in a magnetic field 141

Soxution. The self-inductance is calculated as a double integral over the surface of the
solenoid:

_ 1 pp gigs
L=5[[eBan,
where g is the surface current density (g = nJ). In cylindrical co-ordinates
Rade
. cos ¢ df dai dza
L = 2nb*nt Sy RCN TC RACE TT
2 ! ! J Vea 21)? 408 sin? 49]
ae
(h—0) cos $ dg de
= Babin? ii hl cel dd
3 { V(2+482 sin? $4)
where ¢ is the angle between the diametral planes through df: and dfs, and { = 22—a1.
Effecting the integration with respect to {, we have for hS> b
t h
& Sabtn? ——— i
Les {beers + 2b sin 44] cos #44,
| and finally
L = 41°b?n?[h—8b/37].

Prosiem 7. Determine the factor by which the self-inductance of a plane circuit changes
when it is placed on the surface of a half-space of magnetic permeability jz.. ‘The internal
Part of the self-inductance is neglected.

SoLuTIon. It is evident from symmetry that, in the absence of the half-space, the magnetic
field of the current is symmetrical about the plane of the circuit, and the lines of magnetic
force cross that plane normally. Let this field be Ho. We can satisfy the field equations and
the boundary conditions on the surface of the half-space by putting H = 2,Ho(i4g+1) in
the vacuum and B = psH = 2y4¢Ho/(ue+1) in the medium: By and Hy are then continuous
at the boundary, and the circulation of H along any line of force is equal to that of Ho. Hence
we easily see that, when the medium is present, the total energy of the field, and therefore the
self-inductance of the circuit, are multiplied by 2¢/(He+1).

| §34. Forces in a magnetic field
To determine the forces on matter in a magnetic field hardly any further
calculations are necessary, on account of the complete analogy with electrostatics. The analogy is due mainly to the fact that the expressions for the
thermodynamic quantities in a magnetic field differ from those for an electric
field only in that E and D are replaced by H and B respectively. In calculating the stress tensor in §15 we used the fact that the electric field satisfies
the equation curl E = 0, and is therefore a potential field. The magnetic

field satisfies the equation

curlH = 4nj/c, (34.1)
which reduces to curl H = 0 only in the absence of conduction currents.
In calculating the stress tensor, however, we must always put j = 0. Since
jinvolves the derivatives of the magnetic field, an allowance for the currents
in calculating the stresses would amount to adding to the stress tensor oi

142 Constant Magnetic Field §34
the very small corrections due to the non-uniformity of the field; cf. the
second footnote to §15.

Thus all the formulae obtained in §§15 and 16 for the stress tensor can
be applied immediately for a magnetic field. For example, in a fluid medium
with B = nH we have

H2 Oe. pHiHy
= —po(p, T)8ixe-——| u—p{—) |Sae-+——. 34.2)
on = Polo, MBa~—[n~o( =) four (34.2)
From this the volume forces are calculated by the formula f; = do] xz. If
the medium is a conductor carrying a current, the calculation differs from
that in §15 in that the equation curl H = 0 is replaced by (34.1).
Differentiating (34.2) and using also the equation div B = div (uH) = 0,
we find
1 Oe HB
f= —grad po+—grad | H%p(") | -—gradp—
grad pot gra [ (=I gy Brad
: — + grad H+" (H-grad)H.
8a 4
By a well-known formula of vector analysis,
(H-grad)H = } grad H?~HxcurlH
= $grad H?+47jxH/c.
Thus
1 C) H?
f= —gradpo+—grad [#%0(=) | a gradu ttjxH. (34.3)
8a 8p! p. 80 e

The last term does not appear in the corresponding formula (15.12). It
would, however, be incorrect to suppose that the presence of this term means
that a force can be isolated in f which is due to the conduction current.
The reason is that, by (34.1), the current j is inseparable from non-uniformity
of the field, and another term in (34.3) also involves the space derivatives
of the field. When the magnetic permeability of the medium is appreciably
different from unity, all the terms in (34.3) are in general of the same order
of magnitude.

If, however, as usually happens, is close to 1, the last term in (34.3)
gives the main contribution to the force when a conduction current is present,
and the remaining terms form only a small correction. In calculating the
forces we can put = 1, obtaining simply |

f =jxH/c. (344)
The term —grad fo is of no interest henceforward, and we omit it. For
# = 1 the properties of the substance have no effect on the magnetic phenomena, and the expression (34.4) for the force is equally valid for fluid and for

§34 Forces in a magnetic field 143
solid conductors. The total force exerted by a magnetic field on a conductor carrying a current is given by the integral

F =f xHdV/c. (34.5)
Formula (34.4) can, of course, be very easily obtained from the familiar
expression for the Lorentz force. The macroscopic force on a body at rest
in a magnetic field is just the averaged Lorentz force exerted on the charged
particles in the body by the microscopic field h:f = pyxh/c. For up =1
the field h is equal to the mean field H, and the mean value of pv is the
conduction current density.

When a conductor moves, the forces (34.4) do mechanical work on it. At
first sight it might appear that this contradicts the result that the Lorentz
forces do no work on moving charges. In reality, of course, there is no
contradiction, since the work done by the Lorentz forces in a moving conductor includes not only the mechanical work but also the work done by the

electromotive forces induced in the conductor during its motion. These
two quantities of work are equal and opposite; see the second footnote
to $49.

In the expression (34.4) H is the true value of the magnetic field due both
to external sources and to the currents themselves on which the force (34.4)
acts. In calculating the total force from (34.5), however, we can take H
to be simply the external field $ in which the conductor carrying a current
is placed. The field of the conductor itself cannot, by the law of conservation
of momentum, contribute to the total force acting on the conductor.

The calculation of the forces is particularly simple for a linear conductor.
Its magnetic properties are of no significance, and, if « = 1 in the surrounding medium, the total force on the conductor is given by the line integral

F = Jf dl x§/c. (34.6)
This expression can be written as an integral over a surface bounded by the
current circuit. Using Stokes’ theorem, we replace dl by the operator
dfx grad, obtaining fdlx = f(dfxgrad)xH. Now
(dfx grad) xH = — dfdivH+ grad (df-§)
= —dfdiv$+ dfxcurl §+(df-grad)§.
But div § =0, and in the space outside the currents curl § =0 also. .
Thus
F = J{(df-grad)gjc. (34.7)
In particular, in an almost uniform external field $ can be taken outside

144 Constant Magnetic Field §35
the integral, together with the operator grad. With the magnetic moment
of the current given by (29.18), we then have the obvious result

F = (M-grad)g. (34.8)
Since M in this formula is constant, we can also write

F = grad(M-§), (34.9)
in agreement with the expression (32.17) for the energy of the current. The
torque acting on a current in an almost uniform field is easily seen to be given
by the usual expression

K = Mxg. (34.10)
PROBLEM

Determine the force on a straight wire carrying a current J and parallel to an infinite
circular cylinder with magnetic permeability y, radius a and axis at a distance b from the
wire.

SoLvTIon. On account of the relation, mentioned in the second footnote to §29, between
two-dimensional problems of electrostatics and magnetostatics, the field of the current is
obtained from the result in §7, Problem 3, by changing the notation. The field in the space
round the cylinder is the same as that produced in a vacuum by the current J and currents
+J’ and —J’ through A and O’ (*Fig. 11, §7) respectively, where J’ = (u—1)J/(u+1).*
"The field within the cylinder is the same as that due to a current J” = 2J/(u+1) through O.
‘The force per unit length of the conductor is

= JBle= eS -)

B= JBle=—s\64 20)
2Jea*(u—1)

5? —a®)(u + 1c?

Similarly we find (see §7, Problem 4) that a linear conductor passing through a cylindrical
hole in a magnetic medium is attracted to the nearest surface of the hole by a force

F = 2J?(u—1)(a?—b)(u+ 1c

## Section §35: Gyromagnetic phenomena

The possibilities of magnetising (non-ferromagnetic) bodies without
applying an external magnetic field are severely limited by the requirement
of invariance with respect to a change in the sign of the time. The electric
polarisation of many bodies can be achieved without an external electric field
by, for example, deforming them if they are piezoelectrics. Piezomagnetism,
however, if it occurs at all, is a very rare phenomenon (see the end of §28),
and certainly cannot occur in bodies having no magnetic structure. |

Magnetisation without an external magnetic field generally involves setting
the body in motion. A uniform translation, of course, is of no use, by
Galileo’s relativity principle. A uniform rotation, however, causes a magnetisation which is linearly dependent on the angular velocity 2 (the Barnett
effect); this relation between the vectors # and Q is possible because both
|

§35 Gyromagnetic phenomena 145
change sign when the sign of the time is reversed. Since both are axial
vectors, the relation can hold even in an isotropic body, where it reduces
to a simple proportionality between # and 2.

There must also be an inverse effect: a freely suspended body, on being
magnetised, begins to rotate (the Einstein-de Haas effect). There is a simple
thermodynamic relation between the two effects; it can be derived as follows.

As we know,t the thermodynamic potential with respect to the angular
velocity (for given temperature and volume of the body) is the free energy
F' of the body in a system of co-ordinates rotating with it. The angular
momentum L of the body is

L= —aF/aQ. (35.1)

The gyromagnetic phenomena are described by adding to the free energy
a further term which is the first term, in an expansion in powers of Q and of
the magnetisation M at each point in the body, which contains both Q and
M. This term is linear in both, ice. it is

F eno = — PM dV = — nde, (35.2)
where Aj; is a constant tensor, in general unsymmetrical.

According to (35.1) and (35.2) the angular momentum acquired by the
body as a result of magnetisation is related to its total magnetic moment by
Leyrot =AuM. It is usual to replace Aw by the inverse tensor, defined
as giz = (2mc/e)A-1z, where e and m are the electron charge and mass, The
dimensionless quantities gi are called gyromagnetic coefficients. Then

M; = (¢/2me)gnLeyro,c- (35.3)

The expression (35.2) also shows that, as regards its magnetic effect, the

rotation of the body is equivalent to an external field §; = AxiQz or

Ht = (2mele)g-hyi Qe. (35.4)
We thus have the possibility, in principle, of calculating the magnetisation
caused by the rotation. For example, if the magnetic susceptibility yu of
the body is small, the magnetic moment which it acquires is independent of
its shape and is

As = xueHu = (2mele)xng-nQ1.
Formulae (35.3) and (35.4) represent respectively the Einstein-de Haas and
Barnett effects. We see that both effects are determined by the same tensor
Stk
t See Statistical Physics, §26, Pergamon Press, London, 1958.



---


## 中文翻译

> **中文：** 第IV章——恒定磁场。

### 主要内容
恒定电流产生恒定磁场。基本方程：$\nabla\times\mathbf{H} = 4\pi\mathbf{j}/c$（安培定律），$\nabla\cdot\mathbf{B} = 0$。磁感应强度$\mathbf{B}$与磁场强度$\mathbf{H}$的关系$\mathbf{B} = \mu\mathbf{H}$（各向同性介质），其中$\mu$为磁导率。

### 关键概念
- **矢量势**：$\mathbf{B} = \nabla\times\mathbf{A}$，规范选择$\nabla\cdot\mathbf{A} = 0$（库仑规范）
- **磁场能量**：$U = \int \mathbf{H}\cdot\mathbf{B}/8\pi \, dV$
- **磁标势**：在无电流区域，可引入磁标势$\phi_m$使$\mathbf{H} = -\nabla\phi_m$
- **电磁铁**：电流在铁芯中产生强磁场
- **多极展开**：磁偶极子、四极子等

### 应用
电磁铁设计、磁场测量、粒子加速器磁铁。

# Landau & Lifshitz《Electrodynamics of Continuous Media》第1章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter I: Electrostatics of Conductors

ELECTROSTATICS OF CONDUCTORS

## Section §1: The electrostatic field of conductors

Like all macroscopic theories, the theory of electromagnetic fields in matter
deals with physical quantities averaged over elements of volume which are
“physically infinitesimal”, ignoring the microscopit variations of the quantities which result from the molecular structure of matter. For example,
instead of the actual “microscopic” value of the electric field e, we discuss
its averaged value, denoted by E:
⟨e⟩ =E. (1.1)

The fundamental equations of the electrodynamics of continuous media
are obtained by averaging the equations for the electromagnetic field in a
vacuum. This method of obtaining the macroscopic equations from the
microscopic was first used by H. A. Lorentz.

The form of the equations of macroscopic electrodynamics and the
significance of the quantities appearing in them depend essentially on the
physical nature of the medium, and on the way in which the field varies with
time. It is therefore reasonable to derive and investigate these equations
separately for each type of physical object.

It is well known that all bodies can be divided, as regards their electric
properties, into two classes, conductors and dielectrics, differing in that any
electric field causes in a conductor, but not in a dielectric, the motion of
charges, i.e. an electric current.t

Let us begin by studying the constant electric fields produced by charged
conductors, that is, the electrostatics of conductors. First of all, it follows
from the fundamental property of conductors that, in the electrostatic case,
the electric field inside a conductor must be zero. For a field E which was
not zero would cause a current; the propagation of a current in a conductor
involves a dissipation of energy, and hence cannot occur in a stationary state
(with no external sources of energy).

Hence it follows, in turn, that any charges in a conductor must be located.
on its surface. The presence of charges inside a conductor would necessarily
cause an electric field in it;{ they can be distributed on its surface, however,

+ It should be mentioned that the conductor is here assumed to be homogeneous (in
composition, temperature, etc.). In an inhomogeneous conductor, as we shall see later,
there may be fields which cause no motion of charges.

} This is clearly seen from equation (1.8) below.

2 Electrostatics of Conductors §1
in such a way that the fields which they produce in its interior are mutually
balanced.

Thus the problem of the electrostatics of conductors amounts to determining
the electric field in the vacuum outside the conductors and the distribution of
charges on their surfaces.

At any point far from the surface of the body, the mean field E in the
vacuum is almost the same as the actual field e. The two fields differ only

, in the immediate neighbourhood of the body, where the effect of the irregular
molecular fields is noticeable, and this difference does not affect the averaged
field equations. The exact microscopic Maxwell’s equations in the vacuum are

dive = 0. . (1.2)
curle = —(1/c)dh/at, (1.3)
where h is the microscopic magnetic field. Since the mean magnetic field is
assumed to be zero, the derivative 0b/0¢ also vanishes on averaging, and we
find that the constant electric field in the vacuum satisfies the usual equations
div E = 0, curl E = 0, (1.4)
i.e. it is a potential field with a potential ¢ such that
E = —grad ¢, (1.5)
and ¢ satisfies Laplace’s equation
A¢ = 0. (1.6)
The boundary conditions on the field E at the surface of a conductor
follow from the equation curlE = 0, which, like the original equation
(1.3), is valid both outside and inside the body. Let us take the z-axis in the
direction of the normal to the surface at some point on the conductor. The
component E, of the field takes very large values in the immediate neighbourhood of the surface (because there is a finite potential difference over a
very small distance). This large field pertains to the surface itself and depends on the physical properties of the surface, but is not involved in our
electrostatic problem, because it falls off over distances comparable with the
distances between atoms. It is important to note, however, that, if the
surface is homogeneous, the derivatives 0E;/@x, 2E,/@y along the surface
remain finite, even though E, itself becomes very large. Hence, since
(curl E), = 0E,/@y—dE,/dz = 0, we find that @E,/dz is finite. This means
that Hy is continuous at the surface, since a discontinuity in Hy would mean
an infinity of the derivative dE,/dz. The same applies to Ez, and since
E=0 inside the conductor, we reach the conclusion that the tangential
components of the external field at the surface must be zero:
E, = 0. (1.7)
Thus the electrostatic field must be normal to the surface of the conductor
at every point. Since E = —grad ¢, this means that the field potential must
be constant on the surface on any particular conductor. In other words,

§2 The energy of the electrostatic field of conductors 3
the surface of a homogeneous conductor is an equipotential surface of the
electrostatic field.

The component of the field normal to the surface is very simply related to
the charge density on the surface. The relation is obtained from the general
electrostatic equation dive = 4p, which on averaging gives

div E = 4nj, (1.8)
p being the mean charge density. The meaning of the integrated form of this
equation is well known: the flux of the electric field through a closed surface
is equal to the total charge inside that surface, multiplied by 47. Applying
this theorem to a volume element lying between two infinitesimally close unit
areas, one on each side of the surface of the conductor, and using the fact that
E=0 on the inner area, we find that E, = 470, where o is the surface
charge density, i.e. the charge per unit area of the surface of the conductor.
Thus the distribution of charges over the surface of the conductor is given by
the formula
4no = En = —09/0n, (1.9)
the derivative of the potential being taken along the outward normal to the
surface. The total charge on the conductor is
1 ¢ ad
=-—o-—d, 1.10
: ra an cee)
the integral being taken over the whole surface.

The potential distribution in the electrostatic field has the following remarkable property: the function ¢(x, y, 2) can take maximum and minimum
values only at boundaries of regions where there is a field. This theorem can
also be formulated thus: a test charge e introduced into the field cannot be
in stable equilibrium, since there is no point at which its potential energy ep
would have a minimum.

The proof of the theorem is very simple. Let us suppose, for example,
that the potential has a maximum at some point A not on the boundary of a
region where there is a field. Then the point A can be surrounded by a small
closed surface on which the normal derivative 04/8 < 0 everywhere. :
Consequently, the integral over this surface §(24/2n) df < 0. But by Laplace’s equation §(24/n) df = J A¢ dV = 0, giving a contradiction.

## Section §2: The energy of the electrostatic field of conductors

Let us calculate the total energy &% of the electrostatic field of charged

conductors, t
1
un = f E2dV, (2.1)

+ The square E? is not the same as the mean square é” of the actual field near the surface
of a conductor or inside it (where E = 0 but, of course, & + 0). By calculating the integral
(2.1) we ignore the internal energy of the conductor as such, which is here of no interest,
and the affinity of the charges for the surface.

4 Electrostatics of Conductors §2
where the integral is taken over all space outside the conductors. We transform this integral as follows:

1 ifr. 1 7

u= ~< | Beraas av = -5, | aiv (#E) ard div Eav.

8a 80 80
The second integral vanishes by (1.4), and the first can be transformed into
integrals over the surfaces of the conductors which bound the field and over
an infinitely remote surface. The latter of these vanishes, because the field
diminishes sufficiently rapidly at infinity. Denoting by ¢q the constant value
of the potential on the ath conductor, we havet

1 1
ane FD $ $Ea of = a En df.
80 — 80 =
Finally, since the total charges eg on the conductors are given by (1.10)
we obtain
U=t Zea bas (2.2)

which is analogous to the expression for the energy of a system of point
charges.

The charges and potentials of the conductors cannot both be arbitrarily
prescribed; there are certain relations between them. Since the field equations in a vacuum are linear and homogeneous, these relations must also
be linear, i.e. they must be given by equations of the form

fa = E Cap do, (2.3)
where the quantities Cya, Cay have the dimensions of length and depend on
the shape and relative position of the conductors. The quantities Cua are
called capacity coefficients, and the quantities Cyy (a # 6) are called electrostatic induction coefficients. In particular, if there is only one conductor, we
have e = C¢, where C is the capacity, which in order of magnitude is equal
to the linear dimension of the body. The converse relations, giving the

. potentials in terms of the charges, are
$a = Cavern, (2.4)
where the coefficients C—4, form a matrix which is the inverse of the matrix
Cap.

Let us calculate the change in the energy of a system of conductors caused
by an infinitesimal change in their charges or potentials. Varying the original

t In transforming volume integrals into surface integrals, both here and later, it must be
borne in mind that En is the component of the field along the outward normal to the conductor. This direction is opposite to that of the outward normal to the region of the volume
integration, namely the space outside the conductors. The sign of the integral is therefore
changed in’the transformation.

§2 The energy of the electrostatic field of conductors 5
expression (2.1), we have 5Y = (1/4m) [ E-SE dV. This can be further
transformed by two equivalent methods. Putting E= —grad ¢ and using
the fact that the varied field, like the original field, satisfies equations (1.4)
(so that div 5E = 0), we can write
1 1
3u = — 7 [ grad g.38 av = - 7 |aiv ($85) dv
4a 4a
1
=— > da $ SE df,
ne
that is
Ba = E da Be, (25)
which gives the change in energy due to a change in the charges. This result
is obvious; it is the work required to bring infinitesimal charges Seq to the
various conductors from infinity, where the field potential is zero.
On the other hand, we can write
1 1
bu = - 7 | Beraaag dV = -; | av (E84) dV
1
= 5 p End,

that is

6u= z ea Shay (2.6)
which expresses the change in energy in terms of the change in the potentials
of the conductors.

Formulae (2.5) and (2.6) show that, by differentiating the energy Y with
respect to the charges, we obtain the potentials of the conductors, and the
derivatives of Y with respect to the potentials are the charges:

BW)dea = $a, 82 /dba = ear (2.7)

But the potentials and charges are linear functions of each other. Using

(2.3) we have 2%/@¢a0¢o = Gey] G2 = Coa, and by reversing the order of
differentiation we get Cy». Hence it follows that

Cav = Coa (2.8)

and similarly C-1,, = C-1pg. The energy & can be written as a quadratic

form in either the potentials or the charges:

U =4 5 Cav dabo = 4 Cran caer. (2.9)

This quadratic form must be positive definite, like the original expression
(2.1). From this condition we can derive various inequalities which the

6 Electrostatics of Conductors §2
coefficients Cj, must satisfy. In particular, all the capacity coefficients are
positive:
Cua > 0 (2.10)
(and also C~lyq > 0).+
All the electrostatic induction coefficients, on the other hand, are negative:
Cav <0 (a# db). (2.11)
That this must be so is seen from the following simple arguments. Let us
suppose that every conductor except the ath is earthed, i.e. their potentials
are zero. Then the charge induced by the charged ath conductor on another
(the bth, say) is ¢» = Coada. It is obvious that the sign of the induced charge
must be opposite to that of the inducing potential, and therefore Cyp < 0.
This can be more rigorously shown from the fact that the potential of the
electrostatic field cannot reach a maximum or minimum outside the conductors. For example, let the potential ¢q of the only conductor not earthed be
positive. Then the potential is positive in all space, its least value (zero)
"being attained only on the earthed conductors. Hence it follows that the
normal derivative ¢/2n of the potential on the surfaces of these conductors
is positive, and their charges are therefore negative, by (1.10). Similar
arguments show that C-, > 0.

The energy of the electrostatic field of conductors has a certain extremum
property, though this property is more formal than physical. To derive it,
let us suppose that the charge distribution on the conductors undergoes an
infinitesimal change (the total charge on each conductor remaining unaltered),
in which the charges may penetrate into the conductors; we ignore the fact
that such a charge distribution cannot in reality be stationary. We consider
the change in the integral &@ = (1/87) f E*dV, which must now be extended
over all space, including the volumes of the conductors themselves (since
after the displacement of the charges the field E may not be zero inside the
conductors). We write

8U z] erade bE dV

u div (¢8E) dV: : div SE dV.

al liv (¢5E) + fs iv :
The first integral vanishes, being equivalent to one over an infinitely remote
surface. In the second integral, we have by (1.8) div 5E = 478, so that
5% = J $5p dV. This integral vanishes if ¢ is the potential of the true electrostatic field, since then ¢ is constant inside each conductor, and the integral
J 8pdV over the volume of each conductor is zero, since its total charge
remains unaltered.

+t We may also mention that another inequality which must be satisfied if the form (2.9)
is positive is CaaCo» > Cav®.

§2 The energy of the electrostatic field of conductors 7

Thus the energy of the actual electrostatic field is a minimumt relative
to the energies of fields which could be produced by any other distribution
of the charges on or in the conductors ( Thomson’s theorem).

From this theorem it follows, in particular, that the introduction of an
uncharged conductor into the field of given charges (charged conductors)
reduces the total energy of the field. To prove this, it is sufficient to compare
the energy of the actual field resulting from the introduction of the uncharged conductor with the energy of the fictitious field in which there are
no induced charges on that conductor. The former energy, since it has the
least possible value, is less than the latter energy, which is also the energy
of the original field (since, in the absence of induced charges, the field would
penetrate into the conductor, remaining unaltered). This result can also
be formulated thus: an uncharged conductor remote from a system of given
charges is attracted towards the system.

Finally, it can be shown that a conductor (charged or not) brought into
an electrostatic field cannot be in stable equilibrium under electric forces
alone. This assertion generalises the theorem for a point charge proved at
the end of §1, and can be derived by combining the latter theorem with
Thomson’s theorem. We shall not pause to give the derivation in detail.

Formulae (2.9) are useful for calculating the energy of a system of conductors at finite distances apart. The energy of an uncharged conductor
in a uniform external field €, which may be imagined as due to charges at
infinity, requires special consideration. According to (2.2), this energy is
& = teh, where e is the remote charge which causes the field, and ¢ is the
potential at this charge due to the conductor. % does not include the energy
of the charge e in its own field; since we are interested only in the energy of
the conductor. The charge on the conductor is zero, but the external field
causes it to acquire a dipole electric moment, which we denote by 7. The
potential of the electric dipole field at a large distance r from it is¢ = P-r/r3.
Hence Y = eP-r/2r3, But —er/r? is just the field © due to the charge e.
Thus

U= PE. (2.12)

Since all the field equations are linear, it is evident that the components
of the dipole moment # are linear functions of the components of the field
€. The coefficients of proportionality between # and © have the dimensions of length cubed, and are therefore proportional to the volume of the
conductor:

Fi = VoEr, (2.13)
where the coefficients a, depend only on the shape of the body. The quantities
Vo4x form a tensor, which may be called the polarisability tensor of the body.

f We shall not give here the simple arguments which demonstrate that the extremum is
a minimum.

8 Electrostatics of Conductors §2
This tensor is symmetrical: a = 4, a statement which will be proved in

## Section §11: Accordingly, the energy (2.12) is

U = — Wann. (2.14)
PROBLEMS

Prosiem 1. Express the mutual capacity C of two conductors (with charges -ke) in terms
of the coefficients Cav.

SoLution. The mutual capacity of two conductors is defined as the coefficient C in the
relation e = C($2—41), and the energy of the system is given in terms of C by & = 4¢2/C.
Comparing with (2.9), we obtain

1/C = C7Ay 2072+ Coen
= (Cut+2Ci2t Co2)/(Cr1C22—Cis?).

ProBLeM 2, A point charge e is situated at O, near a system of earthed conductors, and
induces on them charges es. If the charge e were absent, and the ath conductor were at
potential ¢’a, the remainder being earthed, the field potential at O would be ¢’o. Express the
charges eq in terms of ¢’a and ¢o.

SouTto. If charges eg on the conductors give them potentials $2, and similarly for
e‘a and ¢’a, it follows from (2.3) that

z Gala = % baCard'n == Pata
We apply this relation to two states of the system formed by all the conductors and the
charge e (regarding the latter as a very small conductor). In one state the charge e is present,
the charges on the conductors are ea, and their potentials are zero. In the other state the charge
eis zero, and one of the conductors has a potential ¢’a # 0. Then we have e4’o-+ea$’a = 0,
whence ea = —e¢’o/'a.

For example, if a charge ¢ is at a distance 7 from the centre of an earthed conducting sphere
of radius a(< 7), then $’o = ¢’aa/r, and the charge induced on the sphere is e, = —ea/r.

As a second example, let us consider a charge e placed between two concentric conducting
spheres of radii a and 6, at a distance r from the centre such that a <r <b. If the outer
sphere is earthed and the inner one is charged to potential ¢’a, the potential at distance r is

e165
ere
Hence the charge induced on the inner sphere by the charge ¢ is ea = —ea(b—r)/r(b—a).
Similarly the charge induced on the outer sphere is e» = —eb(r—a)/r(b—a).

Prosizm 3. Two conductors, of capacities C1 and Cs, are placed at a distance r apart
which is large compared with their dimensions. Determine the coefficients Ca».

Souvtion. If conductor 1 has a charge e1, and conductor 2 is uncharged, then in the first
approximation $1 = ¢1/C1, ¢2 = e1/r; here we neglect the variation of the field over conductor
2 and its polarisation. Thus C-411 = 1/C1, C-412 = 1/r, and similarly C-!22 = 1/C2. Hence
we findt

aC: CxC; Cir
Cum alte), c= -S, ca = c(1+ 2,
ra 7 7

t The subsequent terms in the expansion are in general of order (in 1/r) one higher than
those given. If, however, r is taken as the distance between the “centres of charge” of the
two bodies (for spheres, between the geometrical centres), then the order of the subsequent
terms is two higher.

§3 Methods of solving problems in electrostatics 9

Prosiem 4. Determine the capacity of a ring (radius 5) of thin conducting wire of circular
cross-section (radius a <5).

SoLution. Since the wire is thin, the field at the surface of the ring is almost the same as
that of charges distributed along the axis of the wire (for a right cylinder, it would be exactly
the same). Hence the potential of the ring is

e pal
#5 d >
where r is the distance from a point on the surface of the ring to an elemént dl of the axis of
the wire, the integration being over all such elements. We divide the integral into two parts
corresponding to r << A and r > A, A being a distance such that a< A <b. Then for
r < A the segment of the ring concerned may be regarded as straight, and therefore
alfa
f= | ——~ = 2 log(2A/a).

$5 = J aan = Pons

Boro La
In the range r > A the thickness of the wire may be neglected, i.e. 7 may be taken as the
distance between two points on its axis. Then

df _bag

fa2{/— = -21 ,

$7? | same Ty
5a %
where ¢ is the angle subtended at the centre of the ring by the chord r, and the lower limit
of integration is such that 26 sin 4¢o = A, whence ¢o % A/b. When the two parts of the
integral are added, A cancels, and the capacity of the ring is
e ab
C=—=—_.
$a log(8b/a)

## Section §3: Methods of solving problems in electrostatics

The general methods of solving Laplace’s equation for given boundary
conditions on certain surfaces are studied in mathematical physics, and we
shall not give a detailed description of them here. We shall merely mention
some of the more elementary procedures and solve various problems of
intrinsic interest. t

(1) The method of images. The simplest example of the use of this method
is to determine the field due to a point charge e outside a conducting medium
which occupies a half-space. The principle of the method is to find fictitious
point charges which, together with the given charge or charges, produce a
field such that the surface of the conductor is an equipotential surface. In
the case just mentioned, this is achieved by placing a fictitious charge
e’ = —e at a point which is the image of e in the plane which bounds the
conducting medium. The potential of the field due to the charge e and its
image e’ is

11
g=e(--—), (a)
ror

+ The solutions of many more complex problems are given by W. R. SMyTHE, Static and
Dynamic Electricity, 2nd ed., McGraw-Hill, New York, 1950; G. A. Grinserc, Selected
Problems in the Mathematical Theory of Electric and Magnetic Phenomena (Izbrannye voprosy
‘matematicheskot teorii élektricheskikh i magnitnykh yavlenit), Moscow, 1948.

10 Electrostatics of Conductors §3
where 7 and r’ are the distances of a point from the charges e and e’.. On
the bounding plane, 7 =r’ and the potential has the constant value zero,
so that the necessary boundary condition is satisfied and (3.1) gives the solution of the problem. It may be noted that the charge e is attracted to the
conductor by a force e#/(2a)? (the image force; a is the distance of the charge
from the conductor), and the energy of their interaction is —e2/4a.

The distribution of surface charge induced on the bounding plane by the
point charge e is given by

1 fa
_ -2(4] Soe (3.2)
4 Lond, or Qn 73
It is easy to see that the total charge on the plane is fodf = —e, as it should
be.

The total charge induced on an originally uncharged insulated conductor
by other charges is, of course, zero. Hence, if in the present case the conducting medium (in reality a large conductor) is insulated, we must suppose
that, besides the charge —e, a charge +e is also induced, which, however,
has no finite density, being distributed over the large surface of the conductor.

Next, let us consider a more difficult problem, that of the field due to a
point charge e near a spherical conductor. To solve this problem, we use
the following result, which can easily be proved by direct calculation. The
potential of the field due to two point charges e and —e’, namely ¢ = e/r—e'|r’,
vanishes on the surface of a sphere whose centre is on the line joining the
charges (but not between them). If the radius of the sphere is R and its
centre is distant / and I’ from the two charges, then //I’ = (e/e’)?, R? = Il’.

Let us first suppose that the spherical conductor is maintained at a constant potential ¢ = 0, i.e. it is earthed. Then the field outside the sphere due
to the point charge e at A (*Fig. 1), at a distance /from the centre of the sphere,*

is the same as the field due to two charges, namely the given charge e and
a fictitious charge —e’ at A’ inside the sphere, at a distance /' from its centre,
where

U = Rl, e = eRIl. (3.3)
The potential of this field is
e eR
=o, 34
§55 G4)
rand r’ being as shown in *Fig. 1. A non-zero total charge —e’ is induced on*
the surface of the sphere. The energy of the interaction between the charge
and the sphere is
U = —hee'|(l-I’) = —} &R/(2— R2), (3.5)
and the charge is attracted to the sphere by a force F= —2%/al =
—eIR|(?2—R2)2.

§3 Methods of solving problems in electrostatics 11
If the total charge on the spherical conductor is kept equal to zero (an
insulated uncharged sphere), a further fictitious charge must be introduced,
such that the total charge induced on the surface of the sphere is zero, and
the potential on that surface is still constant. This is done by placing a
charge +e’ at the centre of the sphere. The potential of the required field
is then given by the formula
ee @é
$= 2-545, 6.6)
pte thy
= P
|
OA=1
OP OA‘
*Fig. 1
The energy of interaction in this case is*
1 1 e&RS
U = tee'(--__} = -—__—_., 3.7,
bee (; 7) 2B — RB (3.7)
Finally, if the charge e is at A’ (*Fig. 1) in a spherical cavity in a conducting*
medium, the field inside the cavity must be the same as the field due to the
charge e at A’ and its image at A outside the sphere, regardless of whether
the conductor is earthed or insulated:
e eR
(Jo) rae (3.8)
r lr
(2) The method of inversion. There is a simple method whereby in some
cases a known solution of one electrostatic problem gives the solution of
another problem. This method is based on the invariance of Laplace’s
equation with respect to a certain transformation of the variables.
In spherical co-ordinates Laplace’s equation has the form
107/06) 1
—=[p2)4— =O
r al" a) “ re Ant :
where Aq denotes the angular part of the Laplacian operator. It is easy to
see that this equation is unaltered in form if the variable r is replaced by
a new variable 7’ such that
r= Rr! (3.9)

12 Electrostatics of Conductors 3
(the inversion transformation) and at the same time the unknown function ¢
is replaced by $’ such that
$=r¢'[R. (3.10)
Here R is some constant having the dimensions of length (the radius of
inversion). Thus, if the function ¢(r) satisfies Laplace’s equation, then so
does the function
Se") = RGR)". (.11)

Let us assume that we know the electrostatic field due to some system of
conductors, all at the same potential ¢9, and point charges. The potential
¢(r) is usually defined so as to vanish at infinity. Here, however, we shall
define ¢(r) so that it tends to —¢p at infinity. Then ¢ = 0 on the conductors.

We may now ascertain what problem of electrostatics will be solved by
the transformed function (3.11). First of all, the shapes and relative positions of all the conductors of finite size will be changed. The boundary
condition of constant potential on their surfaces will be automatically satisfied, since ¢’ = 0 if ¢ = 0. Furthermore, the positions and magnitudes of
all the point charges will be changed. A charge e at a point ro moves to
1’ = Rro/ro? and takes a value e’ which can be determined as follows. As
r—>ro the potential ¢(r) tends to infinity as e/|Sr|, where 5r = r—ro.
Differentiating the relation r = R?x'/r’2, we find that the magnitudes of the
small differences 5r and Sr’ = r’—r'o are related by (8r)? = R4(8r’)?/r’o4.
Hence, as r’ -> ro, the function ¢’ tends to infinity as eR/r’o|St| = er’o/RISr'|,
corresponding to a charge

e! = er'ofR = eR. (3.12)
Finally, let us examine the behaviour of the function ¢’(r’) near the origin.
For r’ = 0 we have r -> 00 and ¢(r) + —do. Hence, as r’ 0, the function ¢’ tends to infinity as —R¢po/r’. This means that there is a charge
€0 = —R¢po at the point r’ = 0.

We shall give, for reference, the way in which certain geometrical figures
are transformed by inversion. A spherical surface of radius a and centre ro
is given by the equation (r—ro)?=a%. On inversion, this becomes
([R2r’/r'2]—r0)? = a2, which, on multiplying by 7’? and rearranging, can be
written (r’—r’o)? = a’2, where

rp = —Rxof(a2—102), a” = aR®/\a®@—102|. (3.13)
Thus we have another sphere, of radius a’ and centre r‘o. If the original
sphere passes through the origin (a = 70), then a’ = 00. In this case the
sphere is transformed into a plane perpendicular to the vector ro and distant
1'9—a’ = R2(a+79) = R2/2a from the origin.

(3) The method of conformal mapping. A field which depends on only
two Cartesian co-ordinates (x and y, say) is said to be two-dimensional.

§3 Methods of solving problems in electrostatics 13
‘The theory of functions of a complex variable is a powerful means of solving
two-dimensional problems of electrostatics. The theoretical basis of the
method is as follows.

An electrostatic field in a vacuum satisfies two equations: curl E = 0,
div E = 0. The first of these makes it possible to introduce the field potential, defined by E= —grad ¢. The second equation shows that we can
also define a vector potential A of the field, such that E= curl A. In the
two-dimensional case, the vector E lies in the xy-plane, and depends only
on «andy. Accordingly, the vector A can be chosen so that it is perpendicular to the xy-plane. Then the field components are given in terms of the
derivatives of ¢ and A by

Ez, = —0$/dx = dAléy, Ey = —0¢/@y = —OAldx. (3.14)
These relations between the derivatives of ¢ and A are, mathematically, just
the well-known Cauchy—Riemann conditions, which express the fact that
the complex quantity
w= ¢-iA (3.15)
is an analytic function of the complex argument z = x+iy. This means that
the function w(z) has a definite derivative at every point, independent of
the direction in which the derivative is taken. For example, differentiating
along the x-axis, we find dw/dz = 0¢/@x—idA/ Ax, or
dw/dz = —Ez+iEy. (3.16)
The function w is called the complex potential.

The lines of force are defined by the equation dx/E, = dy/E,. Expressing
E, and Ey as derivatives of A, we can write this as (04/0x)dx+(2A/dy)dy
=4d4A=0, whence A(x,y) = constant. Thus the lines on which the
imaginary part of the function w(z) is constant are the lines of force. The
lines on which its real part is constant are the equipotential lines. The
orthogonality of these families of lines is ensured by the relations (3.14),
according to which

eRe eae (0)
Ox Ox dy dy

Both the real and the imaginary part of an analytic function w(z) satisfy
Laplace’s equation. We could therefore equally well take im w as the field
potential. The lines of force would then be given by re w = constant.
Instead of (3.15) we should have w = A+id.

The flux of the electric field through any section of an equipotential line
is given by the integral § E,dl = —$(0¢/@n)dl, where di is an element of
length of the equipotential line and n the direction of the normal to it.
According to (3.14) we have 04/@ = —@A/@l, the choice of sign denoting
that J is measured to the left when one looks along n. Thus $ Endl
= §(8A/al)d] = Az—Aj, where Az and Aj are the values of A at the ends

14 Electrostatics of Conductors 3
of the section. In particular, since the flux of the electric field through a
closed contour is 47e, where e is the total charge enclosed by the contour
(per unit length of conductors perpendicular to the plane), it follows that

e = (1/47)AA, (3.17)
where AA is the change in A on passing counterclockwise round the closed
equipotential line.

The simplest example of the complex potential is that of the field of a
charged straight wire passing through the origin and perpendicular to the
plane. The field is given by E, = 2e/r, Ey = 0, where 1,6 are polar coordinates in the xy-plane, and e is the charge per unit length of the wire.
The corresponding complex potential is

w= —2elogz = —2e log r—2ied. (3.18)
If the charged wire passes through the point (xo, yo) instead of the origin,
the complex potential is
w = —2¢ log(z—29), (3.19)
where 2 = xo +iyo.

Mathematically, the functional relation w = w(z) constitutes a conformal
mapping of the plane of the complex variable z on the plane of the complex
variable w. Let C be the cross-sectional contour of a conductor in the
xy-plane, and ¢o its potential. It is clear from the above discussion that the
problem of determining the field due to this conductor amounts to finding a
function (z) which maps the contour C in the z-plane on the line w = do,
parallel to the axis of ordinates, in the w-plane. Then rew gives the
potential of the field. (If the function w(z) maps the contour C on a line
parallel to the axis of abscissae, then the potential is im w.)

e
e
aK,
Za
Fic. 2

(4) The wedge problem. We shall give here, for reference, formulae for
the field due to a point charge e placed between two intersecting conducting
half-planes. Let the z-axis of a system of cylindrical co-ordinates (7, 8, 2)
be along the apex of the wedge, the angle @ being measured from one of the
planes, and let the position of the charge e be (a, y, 0) (*Fig. 2). The angle «*
between the planes may be either less or greater than 7; in the latter case
we have a charge outside a conducting wedge.

3 Methods of solving problems in electrostatics 15

The field potential is given byt
$ e fi sinh (nf/a) sinh (nf/«)

= —_ J J —____ rt x

av/(2ar) J \cosh (aE/a)— cos [(0= la] cosh (w]e) — cos [n(0+ y)/a]
at (3.20)
x——, coshy = (a2 +72 + 22)/2ar, > 0.
“V(cosh £—cosh 7) 1=( Una
The potential ¢ = 0 on the surface of the conductors, i.e. for 9 = 0 or a.

In particular, for « = 2m we have a conducting half-plane in the field of a
point charge. In this case the integral in (3.20) can be evaluated explicitly,
giving

et —cosk(@—y)\ 1 —cos $(4+ )
#-ffos(SEY gor ( SEO}
a\R cosh}n Rr cosh 47 (G21)
R2 = a2+12+22—2arcos(y—9), .
R® = a+12422—-2arcos(y+98).
In the limit as the point (r, 0, z) tends to the position of the charge e, the
potential (3.21) becomes
e wy
= ¢'+eR, hy y= - i [1+]. 3.22
b= +eR, wheres = [1477]. 3.22)
The second term is just the Coulomb potential, which becomes infinite as
R +0, while ¢’ is the change caused by the conductor in the potential at
the position of the charge. The energy of the interaction between the charge
and the conducting half-plane is
2 a
U = heb! = - 2 [14+ I. (3.23)
4na siny
PROBLEMS

Prosiem 1. Determine the field near an uncharged conducting sphere of radius R placed
in a uniform external electric field ©.

SotuTion. We write the potential in the form ¢ = ¢o+¢1, where ¢o = —-r is the
potential of the external field and ¢1 is the required change in potential due to the sphere.
By symmetry, the function ¢1 can depend only on the constant vector @. The only such solution of Laplace’s equation which vanishes at infinity is .

$1 = —constant x €-grad (1/r) = constant x €-r/r°,
the origin being taken at the centre of the sphere. On the surface of the sphere ¢ must be
constant, and so the constant in ¢1 is R®, whence
RS RS
$= (1-4) = —Gr cos (1-4).

where 0 is the angle between @ and r. The distribution of charge on the surface of the
sphere is given by

o = —(1/4n)[ 2$/ar]ran = (3/42) cos 8.

+ This formula was first given by H. M. Macponatp (1895). Its derivation is given by
him in Electromagnetism, Beli, London, 1934, p. 79.

16 Electrostatics of Conductors §3
‘The total charge e = 0. The dipole moment of the sphere is most easily found by comparing
¢1 with the potential #-r/r3 of an electric dipole field, whence ? = R°G.

ProseM 2. The same as Problem 1, but for an infinite cylinder in a uniform transverse
field.

Sotution. We use polar co-ordinates in a plane perpendicular to the axis of the cylinder.
The solution of the two-dimensional Laplace’s equation which depends only on a constant
vector is

$1 = constant x G-grad (log r) = constant x -r/r?.
Adding ¢o = —@-r and putting the constant equal to R®, we have
R*
ae a(t = =)

g ‘Er cos ay
‘The surface charge density is o = (€/2m) cos @. The dipole moment per unit length of the
cylinder can be found by comparing ¢ with the potential of a two-dimensional dipole field,
namely 2-grad (log r) = 2#-r/r?, so that P = 4R°E.

PRoBLEM 3. Determine the field near a wedge-shaped projection on a conductor.

So.uTIon. We take polar co-ordinates r, @ in a plane perpendicular to the apex of the
wedge, the origin being at the vertex of the angle 0 of the wedge. The angle @ is measured
from one face of the wedge, the region outside the conductor being 0 < @ < 27—@. Near
the apex of the wedge, the potential can be expanded in powers of r, and we shall be interested
in the first term of the expansion (after the constant term), which contains the lowest power
of r. The solutions of the two-dimensional Laplace’s equation which are proportional to
7” are r™ cos nO and r*sinn§. The solution having the smallest 2 which satisfies the condition ¢ = constant for 8 = 0 and 8 = 27—® (i.e. on the surface of the conductor) is

$ = constant X r" sin 76, n= n/(2n—60).
‘The value of the constant can be determined only by solving the problem for the whole field.
The field varies as r*-1, For do < 7 (n <1), therefore, the field becomes infinite at the apex
of the wedge. In particular, for a very sharp wedge (0 <1, 2 & 4) E increases as r-* as.
7-0. Near a wedge-shaped concavity in a conductor (6) > 7, > 1) the field tends to
zero.

Prosiem 4. Determine the field near the end of a sharp conical point on the surface of a
conductor.

SoxuTion. We take spherical co-ordinates, with the origin at the vertex of the cone and
the polar axis along the axis of the cone. Let the angle of the cone be 200 <1, so that the
region outside the conductor corresponds to polar angles in the range 80 < 9 < 7. We seek
a solution for the variable part of the potential, which is symmetrical about the axis, in the
form

$=rf(0), qa)
with the smallest possible value of n. Laplace’s equation
1 8/,a¢ He) ( . %)
=—— (2) += (sin o£) = 0,
7 = ( 7) + ein 0 30 VP a5
after substitution of (1), gives
1d af
— = (sin @— Df = 0. 2)
spag (80 OG) tert ng 0)
‘The condition of constant potential on the surface of the cone means that we must have
f(60) = 0.

For small 6 we seek a solution by assuming that » <1 and f(8) is of the form
constant x[1-+¥(6)], where ¥ <1. (For 6 — 0, i.e. an infinitely sharp point, we should
expect that ¢ tends to a constant almost everywhere near the cone.) The equation for ¥ is

1d dy
— = (sino) = —n. 3)
sin 046 (sia @) . Sy
|

33 Methods of solving problems in electrostatics 17
The solution having no singularities outside the cone (in particular, at @= 7) is (0)
= 2n log sin 38.

For 6 ~ 00 <1, ¥ is no longer small. Nevertheless, this expression remains valid, since
the second term in equation (2) may be neglected because 0 is small. To determine the constant n in the first approximation we must require that the function f = 1+ vanishes for
@ = 0. Thust n = —1/2 log 4. The field increases to infinity as ~(1-") in the neighbourhood of the vertex, i.e. essentially as 1/r.

Prosiem 5. The same as Problem 4, but for a sharp conical depression on the surface of a
conductor.

Souvion. ‘The region outside the conductor now corresponds to the range 0 < @ < 60.
As in Problem 4, we seek ¢ in the form (1), but now n> 1. Since @ <1 for all points in the
field, equation (2) of Problem 4 becomes

1dyaf

1 (gV) 1 nf = 0.

3 aa Fa Biaciel:
This is Bessel’s equation, and the solution having no singularities in the field is Jo(n@). The
value of 2 is determined as the smallest root of the equation Jo(n6o) = 0, whence n = 2-4/6.

ProsieM 6. Determine the energy of the attraction between an electric dipole and a plane
conducting surface.

So.uTion. We take the x-axis perpendicular to the surface of the conductor, and passing
through the dipole; let the dipole moment vector # lie in the xy-plane. The image of the
dipole is at the point —x and has a moment 9’, = Pz, 9’, = —#,. The required energy
of attraction is half the energy of the interaction between the dipole and its image, and is
U = —(2P2+Py*)/16x9.

Prostem 7. Determine the mutual capacity per unit length of two parallel infinite conducting cylinders of radii a and 6, their axes being at a distance ¢ apart.f

-e
te
OA .
yo
0 O0'=¢
OA =a, a
Oa,
Fie. 3

Sotution. The field due to the two cylinders is the same as that which would be produced
(in the region outside the cylinders) by two charged wires passing through certain points
‘A and A’ (*Fig. 3). The wires have charges -te’ per unit length, equal to the charges on the*
cylinders, and the points A and A’ lie on OO’ in such a way that the surfaces of the cylinders
are equipotential surfaces. For this to be so, the distances OA and O’A’ must be such

+ A more rigorous calculation gives the formula n = 1/2 log (2/60), containing a coefficient
in the (large) logarithm, which cannot really be obtained by the simple method given here.

The corresponding problem for two, spheres cannot be solved in closed form. The
difference arises because, in the field of two parallel wires bearing equal and opposite charges,
all the equipotential surfaces are circular cylinders, whereas in the field of two equal and
opposite point charges the equipotential surfaces are not spheres.

18 Electrostatics of Conductors i]
that OA + OA’ = a3, O’A'- O'A = BY, ie. di(c—da) = a®, do(c—ds) = B®. Then, for each
cylinder, the ratio r/r’ of the distances from A and A’ is constant. On cylinder 1, r/r’ = a/OA’
= a/(c—d2) = dia, and on cylinder 2, r’/r = da/b. Accordingly, the potentials of the cylinders are $1 = —2e log (r/r’) = —2e log (dila), $2 = 2e log (da/b), $2—$1 = 2e log (dida/ab).
Hence we find the required mutual capacity C = e/(¢2—¢1):

1/C = 2 log (dids/ab) = 2 cosh [(c?—a? —B*)/2ab].

In particular, for a cylinder of radius a at a distance h (> a) from a conducting plane, we
put c = +h and take the limit as b > 00, obtaining 1/C = 2 cosh} (h/a).

If two hollow cylinders are placed one inside the other (c < 5—a), there is no field outside,
while the field between the cylinders is the same as that due to two wires of charges +e
passing through A and A’ (*Fig. 4). The same method gives*

1/C = 2 cosh [(a?-+52—c2)/2ab}.
Prosiem 8. The boundary of a conductor is an infinite plane with a hemispherical projection. Determine the charge distribution on the surface.
O0'e
Fic. 4
Soxution. In the field determined in Problem 1, whose potential is
a
= stant X. - Zz)
$ = constan + 5)
the plane z = 0 with a projection r = R is an equipotential surface, on which ¢ = 0. Hence
it can be the surface of a conductor, and the above formula gives the field outside the conductor. The charge distribution on the plane part of the surface is given by
- 1] = o( Re)
oad a)!
we have taken the constant in ¢ as —4709, so that oo is the charge density far from the projection. On the surface of the projection we have
1 [2] Ban.
o=-—|*] = .
falorlen "R

PRosLEM 9. Determine the dipole moment of a thin conducting cylindrical rod, of length
21 and radius a <I, in an electric field € parallel to its axis.

Soxurion. Let 7(z) be the charge per unit length induced on the surface of the rod, and
# the co-ordinate along the axis of the rod, measured from its midpoint. The condition of
constant potential on the surface of the conductor is

1 Ff nerds’ ag
a3
neers, { [no
an
RP = (2’—2)?-+-4a? sin® 44,

§3 Methods of solving problems in electrostatics 19.
where ¢ is the angle between planes passing through the axis of the cylinder and through two
points on its surface at a distance R apart. We divide the integral into two parts, putting
1(2’) = 7(2)+[7(2’)—7(2)]. Since 15> a, we have for points not too near the ends of the rod
ae .
x2) i dz’d$ | x2) i Poe 4(2—22)
2s R= 20 J 108 a unegg 1 = 7) los
using the result that flog sin ¢dg = —zlog2. In the integral which contains the diff‘°
erence 7(z’)—7(z), we can neglect the a® term in R, since it no longer causes the integral to
diverge. Thus
1
Be: =
Ez = x(z) log flat), + f me 118) ay,
a J eal
The quantity 7 is almost proportional to z, and in this approximation the integral gives
—2r(z), the result being
oa) = —_ = _.
log [4(@—a*)/a2]—2°
This expression is invalid near the ends of the rod, but in calculating the dipole moment
that region is unimportant. In the above approximation we have
1 1
€ at 2
o= | ayeas = [ ["~ tos (1-F)] ae
7 °
cay 1/4
= alt Zb— "2)}
where L = log (2l/a)—1 is large, or (with the same accuracy)
g-— __
3 log (4l/a)—7

Prosiem 10. Determine the capacity of a hollow conducting cap of a sphere.

SoLvTION. We take the origin O at a point on the rim of the cap (*Fig. 5), and carry out the*
inversion transformation r = /?/r’, where 1 is the diameter of the cap. ‘The cap then becomes
the half-plane shown by the dashed line in *Fig. 5, which is perpendicular to the radius AO*
of the cap and passes through the point B on its rim. The angle y = 7—0, where 20 is the
angle subtended by the diameter of the cap at the centre of the sphere.

A
R,
o. =m
OO
ee
NN
Fie. 5

If the charge on the cap is e and its potential is taken as zero, then as 7 —> 00 the potential
$ +—$o-te/r. Accordingly, in the transformed problem, as r’ > 0 the potential is ¢” > [$/r’
= —Ido/r’-+e/l, where the first term corresponds to a charge e’ = —I¢o at the origin.

20 Electrostatics of Conductors 4

According to formula (3.22), we have

ioe @
€-5- lt aa)
(the potential near a charge e’ at a distance / from the edge of a conducting half-plane at zero
potential). Comparing the two expressions, we have for the required capacity C = e/do
L e R,.
c= x(t+ =) = Gin 048),
where R is the radius of the cap.

ProieM 11, Determine the correction due to edge effects on the value C = S/4nd for
the capacity of a plane condenser (S being the area of the plates, and d < 1S the distance
between them).

dole
@) -of-----=----= 40
4-42
&
; °
Fic. 6

SoLvTION. Since the plates have free edges, the distribution of charge over them is not
uniform. ‘To determine the required correction in a first approximation, we consider
points which are at distances x from the edge such that d <x <+/S. For example, taking
the upper layer (at potential ¢ = 440, *Fig. 6a) and neglecting its distance 4d from the midplane (the equipotential surface $ = 0), we have the problem of the field near the boundary*
between two parts of a plane having different potentials (*Fig. 6b). ‘The solution is elementaryt, and the excess charge (relative to the value of o far from the edge) is Ao = En/40*
= $0/8x2x, so that the total excess charge is Lf Ac dx = (foL/8n) log (¥/S/d), where L is
the perimeter of the plate. In calculating the logarithmically divergent integral, we have
taken the limits as those of the region d <x < /S. Hence we find the capacityt

Ss L VS
C= Fa + ana BG
4. A conducting ellipsoid

The problem of the field of a charged conducting ellipsoid and that of an
ellipsoid in a uniform external field are solved by the use of ellipsoidal coordinates. These are related to Cartesian co-ordinates by the equation

ow 1 @rb>g (4.1)
TTT a>b>c). 7
@iu Btu &+u

t See §22. In formula (22.2) for the potential we must here put $a» = $49, @ = =.

t¢ A more exact calculation (determining the coefficient in the argument of the logarithm)
demands considerably more elaborate methods, and the result depends on the shape of the
plates, If these are circular, of radius R, we obtain Kirchhoff’s formula

ROR 160R
c= St Eee -1).

4 A conducting ellipsoid 21
This equation, a cubic in u, has three different real roots &, », £, which lie in
the following ranges:
&>-0%, -2%>y>-0, -BP>le-a (4.2)
These three roots are the ellipsoidal co-ordinates of the point x, y, z. Their
geometrical significance is seen from the fact that the surfaces of constant
£, and ¢ are respectively ellipsoids and hyperboloids of one and two sheets,
all confocal with the ellipsoid
P/a2+y2/B24 22/2 = 1, (4.3)

One surface of each of the three families passes through each point in
space, and the three surfaces are orthogonal. The formulae for transformation from ellipsoidal to Cartesian co-ordinates are given by solving three
simultaneous equations of the type (4.1), and aret

on 2, f[eemoreneeen)
TENT Ge aa—ay |
E+ b2)(n + b2)(0 +b?
ym a, ff emer 7, a
(2-Bya—F)
a :/[ E+ejgteryC+e?) |
“VU @-ae-a)
The element of length in ellipsoidal co-ordinates is
dI2 = hy2d€? + hy? dy? + hg? dl?,
In = VUE-n)E-DY2Rp he = Vin—-H(n- 41/2, (4.5)
hg = VU(E-E)(S—n)V2Ry Rv = (u+a?)(ur bute), .
u=Enb
Accordingly, Laplace’s equation in these co-ordinates is
A¢ 4
= ——______x
EMH (46)

[ DR, ~. (Rae) + 1-or,~ Ro) + e-R(R *)| 0.

x|@m— ae - p(t - —}|=0.
@ cag | Rege ( val "On Ge) x ( 3,

If two of the semiaxes a, b, c become equal, the system of ellipsoidal coordinates degenerates. Let a= > c. Then the cubic equation (4.1)
becomes a quadratic,

my 2 = ata ye 47
au atu 2. 7)

t Strictly speaking, the ellipsoidal co-ordinates should be taken not as ¢, 7, { themselves
but as +/(a? + 2), +/(b? + Ds v(e2 + é). Then the double signs would not appear in
(4.4), and the two systems of co-ordinates would be in one-to-one correspondence, as they
should be,

22 Electrostatics of Conductors 4
with two roots whose values lie in the ranges > —c?, —c? > » > —a®. The
co-ordinate surfaces of constant ¢ and 7 become respectively confocal oblate
spheroids and confocal hyperboloids of revolution of one sheet (*Fig. 7).*
As the third co-ordinate we can take the polar angle ¢ in the xy-plane
(x = pcos¢, y=psin¢). For a=b the ellipsoidal co-ordinate ¢ degenerates to a constant, —a?. Its relation to the angle ¢ is given by the way
in which it tends to —a? as b tends to a, namely
cosd = V/[(a? + 2)/(a?—6?)] as b >a. (4.8)
f,
\ % ”
\ re /
S {oie/
4 7
‘ete! pee
\_ ia
— ao a Te
a + \
/ Hl \
‘
'
Fie. 7
This is easily seen from (4.4) or directly from (4.1). The relation between the
co-ordinates 2, p and é, 7 is given, according to (4.4), by
E+ eatery _ (fE+e)nta)
ve zy | Deere | a J a— ct iF 49)
The co-ordinates £, 7, ¢ are called oblate spheroidal co-ordinates.t
Similarly, for a > 6 = c ellipsoidal co-ordinates become prolate spheroidal
co-ordinates. Two co-ordinates £ and ¢ are roots of the equation
x2 pe
sta = 1 2 = y2 + 22 4.10)
@tu P+u i 2 sa)
where é > —b?, —b2 > £ > —a®. The surfaces of constant ¢ and { are
prolate spheroids and hyperboloids of revolution of two sheets (*Fig. 8).*
The co-ordinate 7 degenerates to a constant, —B2, for c > b, and we have
cosh = y[(?+7)/(B?—c?)], (4.11)
where ¢ is the polar angle in the yz-plane. The relation between the coordinates x, p and é, ¢ is given by
+a (+a?) Be KGa a 9)
= +/| a—b2 |: e=J[ Bea? ]: (4.12)
+ We here use the definition of spheroidal co-ordinates such that they are the limit of
ellipsoidal co-ordinates. Other definitions are used in the literature, but are easily related to ours.

4 A conducting ellipsoid 2

In a system of oblate spheroidal co-ordinates the foci of the spheroids and
hyperboloids lie on a circle of radius »/(a2—c?) in the xy-plane; in *Fig. 7
AA’ is a diameter of this circle. Let us draw a plane passing through the*
z-axis and some point P. It intersects the focal circle at two points; let
their distances from P be ri, 72. If the co-ordinates of P are p, 2, then

re = [p—V(a?—02) 2 +22, ree = [pt >/(a?—c?2) 2 +22.
Fy
et
Le
NN T _
S i
“Sy 1 ca
SL AL -a a £28 p
we
€
Paria
a 1 —
“ I ~
Fic. 8
The spheroidal co-ordinates £, 7 are given in terms of ri, 72 by
€ = Urni+r2)?—-a, 7 = Un—-n)?P-a@. (4.13)

In a system of prolate spheroidal co-ordinates the foci are the points
x= +4/(a@—3?) on the x-axis (the points A, A’ in *Fig. 8). If ry and rz*
are the distances of these foci from P, then

re = p2+[z—V(@2-B)P, 22 = p?+[z+-V/(2-B)P,
and the spheroidal co-ordinates é, { are given in terms of 71, r2 by the same
formulae (4.13), with £ in place of ».

Let us now turn to the problem of the field of a charged ellipsoid whose
surface is given by the equation (4.3). In ellipsoidal co-ordinates this is the
surface = 0. It is therefore clear that, if we seek the field potential as a
function of £ only, all the ellipsoidal surfaces £ = constant, and in particular the surface of the conductor, will be equipotential surfaces. .Laplace’s
equation (4.6) then becomes

d d

AR t) =0,

dg\ * dé

whence

eae

#@ - afF.
ra

O :

24 Electrostatics of Conductors 4
The upper limit of integration is taken so that the field is zero at infinity.
The constant A is most simply determined from the condition that at large
distances 7 the field must become a Coulomb field and ¢ ~ e/r, where e is
the total charge on the conductor. When r > 00, £ + 00, and x 7%, as
we see from equation (4.1) with w= For large € we have R, ~ &/,
and ¢ ~ 2A/,/é = 2A/r. Hence 2A = e, and therefore
wae
He) = ¥e[ (4.14)
€
é
‘The integral is an elliptic integral of the first kind. The surface of the conductor corresponds to £ = 0, and so the capacity of the conductor is given
' by
afc
= =3(— 415
anf nm (4.15)
0
The distribution of charge on the surface of the ellipsoid is determined by
the normal derivative of the potential:
1 (=) 1 [ 1 *] e 1
o= —-—|— = -—|—— = ——_,
4a Lénl - 0 4nlhy leo 40 -V(nb)
From equations (4.4) we easily see that for § = 0
rr
ae a ape
Hence
ext y2 att
= bap oe le 4.16
° = “fnabe (3 a a) (#16)
For a spheroid the integrals (4.14), (4.15) degenerate and can be expressed
in terms of elementary functions. For a prolate spheroid (a > b = c) the
field potential is
2 Be
6 = —— tanh Aine (4.17)
Ve) fe
and the capacity is - aor
: c= VE) (4.18)
cosh=1(a/b) :
For an oblate spheroid (a = 6 > c) we have
2 2 . 2 2
¢= sa [SS C= Ve — 2) (4.19)
f(a?) E+ cos~}(c/a)

4 A conducting ellipsoid 25.
In particular, for a circular disc (a = , c = 0)
C = 2aln. (4.20)

Let us now consider the problem of an uncharged conducting ellipsoid
in a uniform external electric field €. Without loss of generality we may
take the field & to be along one of the axes of the ellipsoid. In any other case
this field may be resolved into components along the three axes, and the
resultant field is a superposition of those arising from each component
separately.

The potential of a uniform field € along the x-axis (the a-axis of the ellipsoid) is, in ellipsoidal co-ordinates,

do = —Ex = —Ey[(E+0")(9 +a*)(E + a2)((B2— a2)(c2— a), (4.21)
We write the field potential outside the ellipsoid as $ = ¢o+¢’, where ¢’
gives the required perturbation of the external field by the ellipsoid, and
seek ¢’ in the form ,
$' = goF(é). (4.22)
In this function the factors depending on 7 and £ are the same as in ¢o; this
enables us to satisfy the boundary condition at é = 0 for arbitrary 7, £
(i.e. on the surface of the ellipsoid). Substituting (4.22) in Laplace’s equation
(4.6), we obtain for F() the equation
@F dFd
—+—— = log [R{é+a?)] = 0.
Tat ap ag RE +o)
One solution of this equation is F = constant, and the other is
. bd dé
F@ =A f — 4.23
© J eran; (4.23)
‘The upper limit of integration is taken so that ¢’ + 0 for € > oo. The integral
is an elliptic integral of the second kind.

We must have ¢ = constant on the surface of the ellipsoid. For this condition to be satisfied with = 0 and arbitrary , f, the constant value of ¢
must be zero. Determining the coefficient A in F(é) so that F(0) = —1, we
obtain the following final expression for the field potential:

4 aft i ds f ds | 4.24)
7 a” (s+a)Rs | (s+a)R, J «.

Let us find the form of the potential ¢’ at large distances r from the ellipsoid. For large r, the co-ordinate é is large, and £ ~ 72, as follows at once
from equation (4.1). Hence

f ds i ds 2
J (s+a8)Re es 2 2
r

26 Electrostatics of Conductors 4
and the potential ¢’ = © xV/4nn'r3, where V = $nabc is the volume of
the ellipsoid and n@, n, n®) are defined by
© ©
ds ds
n® = habe [ nD = abe [ —S
(s+a?)Rs F (st+B2)Rs
0
(4.25)
a .
n@) = tbe |.
(s+e)Rs
0
The expression for ¢’ is, as we should expect, the potential of an electric
dipole: ¢’ = x,/r8, where the dipole moment of the ellipsoid is
Pz = ExV/4an', (4.26)
Analogous expressions give the dipole moment when the field € is along the
. y or 2 axis.

The positive constants n‘*), nv), n@ depend only on the shape of the
ellipsoid, and not on its volume; they are called the depolarisation coefficients.t
If the co-ordinate axes do not necessarily coincide with those of the ellipsoid, formula (4.26) must be written in the tensor form

(40/V nxePa = Gi. (4.27)
The quantities n@, n, n@) are the principal values of the symmetrical
tensor m4 of rank two.

In the general case of arbitrary a, 6, ¢, it follows from the definitions of
n®, nW), n®) that

1 <n <n® ifa>b>e. (4.28)
Further, by adding the integrals for n™, n™, n) and using as the variable
of integration u = R,?, we find
T du
n® +n 4+n®@ = sabe J =,
3/2
(ade):
whence
n@+n+n®@ = 1, (4.29)
The sum of the three depolarisation coefficients is thus unity; in tensor notation, mj; = 1. Since these coefficients are positive, none can exceed unity.

For a sphere (a = b = ¢) it is evident from symmetry that

n® =n = n® = 4. (4.30)
For a cylinder with its axis in the x-direction (a -> 0), we havet
nM =), WW =n =}, (4.31)

{ Useful tables of these coefficients have been given by E. C. Stoner (Philosophical
Magazine [7] 36, 803, 1945).

t These values for a sphere and a cylinder agree, of course, with those found in §3,
Problems 1 and 2.

4 A conducting ellipsoid 27
The elliptic integrals (4.25) can be expressed in terms of elementary functions if the ellipsoid is a spheroid. For a prolate spheroid (a > 6 = c) of
eccentricity e = +/(1—b?/a”),
1-e 1+e
ne) = (10 <i x) nO =n = K1—n), (4.32)
== (tog —~*-20), H1-n@), 4.32)
If the spheroid is nearly spherical (e < 1) we have approximately
MD = A see2, nD = ni = bt dye?. (4.33)
For an oblate spheroid (a = b > c)
1+e
n® = ——“(e-tanle), ni = n = 4(1—n®%, (4.34)
e
where e = »/(a?/c2—1). Ife < 1, then
n® = fp wge?, nl) = nW = 4—dee?, (4.35)
PROBLEMS
Prosixm 1. Find the field of a charged conducting circular disc of radius a, expressing it
in cylindrical co-ordinates. Find the distribution of charge on the disc.
Soxution. The charge distribution is obtained by taking the limit of formula (4.16) as
+0, 2 +0, with [ce = /(1—r2/a2) (where r? = 22+-9%), in accordance with (4.3). ‘This
ives
. = ft-2)"
Fae at) *
‘The field potential is given in all space by formula (4.19), where we put c = 0 and express £
in terms of r and z by means of equation (4.1) with c = 0, u = £,a = b:
Ons 2a? U
$~ Suet acaF Tie FTA .
2
,
We
o WP
D
@ @
Fic. 9
‘Near the edge of the disc, we replace r and x by co-ordinates p and @ such that z = psin 0,
r = a—pcos 0 (*Fig. 9; p <a), obtaining*
ws 2e
#2 (b—9/ Zain),
in agreement with the general result derived in §3, Problem 3.

on a _
28 Electrostatics of Conductors 4

Prostem 2. Determine the electric quadrupole moment of a charged ellipsoid.

Souvtion. ‘The quadrupole moment tensor of a charged conductor is defined as Dix
= e(3xuxv—r?8xx), where e is the total charge, and the bar denotes an average such as

=a
wine = =f aune df.
It is evident that the axes of the ellipsoid are also the principal axes of the tensor Dx. Using
formula (4.16) for ¢, and for the element of surface of the ellipsoid the expression
_ dedy dey 1/2 a =)
yn aN latatal
we obtain
ae J = 4c:
ren’ xzdxdy = 37;
the integration over x and y covers twice the area of the cross-section of the ellipsoid by the
xy-plane. Thus
Dez = Se(2a2—b?—c2), Dyy = 4e(28*°—8—a?), Dee = Se(2c?—a?—B%).

Prosem 3. Determine the distribution of charge on the surface of an uncharged conducting ellipsoid placed in a uniform external field.

SoLurton. According to formula (1.9) we have

a
Go -4 [2] = -[-4l A
‘4alondeno Ak, BE leno
by (4.5) the element of length along the normal to the surface of the ellipsoid is indg. Substituting (4.24) and using the fact that
[ir Slo baa]
|e
n 2le-o — L2a% Je-0
(where y is a unit vector along the normal to the surface), we have ¢ = Gvz/4nn(*) when the
external field is in the x-direction. When the direction of the external field is arbitrary this
becomes
1 1 pve yy ve
0 pourtatte = 7 [e+ G+ 6].

Prosiem 4. The same as Problem 3, but for a plane circular disc of radius a lying parallel
to the field. Determine also the dipole moment of the disc.

Sourton. Let us regard the disc as the limit of a spheroid when the semiaxis c tends to
zero. ‘The depolarisation coefficient along this axis (the z-axis) tends to 1, and those along
the x and y axes tend to zero: nl) = 1—ne/2a, n'#) = nv) = nc/4a, by (4.34). The component vz of the unit. vector along the normal to the surface of the spheroid tends to zero:

x (®@ty2 att ow wel, attyty A

: wed +a) aot)
Hence the charge density is

= £2 _ Goss
ofa n@) — aa/(a?—pa)?
where p and ¢ are polar co-ordinates in the plane of the disc.

The dipole moment of the disc is obtained from formula (4.26), and is # = 4a°€/37.
‘Thus it is proportional to a, and not to the “volume” a% of the disc.

+ The problem for a disc lying perpendicular to the field is trivial: the field remain
uniform in all space, and charges o = +€/4m are induced on the two sides of the disc.

4 A conducting ellipsoid 29
Prostem 5. Determine the field potential outside a conducting spheroid with its axis of
symmetry parallel to a uniform external field.
Sovution. For a prolate spheroid (a > b = c, with the field © in the x-direction) we find,
on calculating the integral in formula (4.24),
_ —trf1— tanh? WAP P CE Fe Ve PIE Fe)
tanh? (1 —6?/a®) — (1 —B7/a®) :
‘The co-ordinate ¢ is related to x and p = /(y?-+2%) by
2 at
4+ =1,
Bret ate
with 0 < £ < © in the space outside the ellipsoid.
For an oblate spheroid (a = 6 > ¢) tHe field € is along the 2-axis. We must therefore replace s+a? by s-+c? and put ¢o = —Cz in the integrals in (4.24). Then
$= ~Ga{1— V (a? —c)/(E-+e%)] tan! V[(a?-0*)/(E+c%) |
V (a1) — tan /(a2/e2—1) B
where the co-ordinate £ is related to z and p = /(x?+y%) by
fea 2
sata =h
ait t Bre
PropLeM 6. The same as Problem 5, but with the axis of symmetry perpendicular to the
external field.
SowvTion. For a prolate spheroid (with the field along the z-axis)
_ -€-{1- VE+a%) (E40) —(a? 6%) tanh VE MKE Fo)
a/b®—(a*—5%)-* tanh +/(1 —b?/a%) 7
For an oblate spheroid (with the field along the x-axis)
a Gt _ (ato) tan Vila?) (E+) — VE+eD(E+0%) }
a ant V@E 1) — cla 5
Prosizm 7. A uniform field & in the z-direction (in the half-space x < 0) is bounded by
an earthed conducting plane at z = 0, containing a circular aperture. Determine the field
and charge distribution on the plane.
SoLuTIon. The xy-plane with a circular aperture of radius a and centre at the origin may
be regarded as the limit of the hyperboloids of revolution of one sheet
pot
son Ha1 Patty,
aa bd *
as [| + 0. These hyperboloids are one of the families of co-ordinate surfaces in a system of
oblate spheroidal co-ordinates with c = 0. The Cartesian co-ordinate z, according to (4.9),
is given in terms of ¢ and 7 by x = ¥/(£|nl)/a, and /£ must be taken with the positive and
negative sign in the upper and lower half-space respectively.
| Let us seek a solution in the form ¢ = —Cz F(£). For the function F(é) we obtain
dé a a
ae eee ts)
F(£) = constant xf eta ‘constant X Pa tan mal 3
the constant of integration is put equal to zero in accordance with the condition ¢ = 0 for
z> +0, ie. &—> -+0. The inverse tangent of a negative quantity must be taken as
tan! (a/—/) = 7—tan“ (a//), and not as —tan=! (a/+/£) since the potential would
then be discontinuous at the aperture (£ = 0). ‘The constant coefficient is chosen so that, for
2 —00 (i.e. for / > —c and tan-! (a/+/£) > 2), 6 > —Ez, and so we finally have
Ez a a € ve @
= ——]tant 4-4] = - = ~ tant —1].
‘ =I ve val ave an ve ]
On the conducting plane 7 = 0 and the potential is zero, as it should be.

30 Electrostatics of Conductors 4

At large distances r = \/(2?-+ p%) from the aperture we have £ & r®, and the potential (in
the upper half-plane) is

2 —
ox SOY=4 _ Gadz/3nr3,
3m COE
i.e. we have a dipole field, the moment of the dipole being ? = €a®/37.

‘The field decreases as 1/73, and therefore the flux of the field through an infinitely remote
surface (in the half-space z > 0) is zero. This means that all the lines of force passing through
the aperture reach the upper side of the conducting plane.

‘The distribution of charge on the conducting plane is given by

_ 44 = 77% 4 Sle -4)
Gelacleno * aeveov—a * anil” VE” VE
where the 7 signs refer to the upper and lower sides of the plane respectively. According
to the formula
pat
elas ih
ere e
which relates { to p, z, we have /f = ++/(p—a®) on the plane z = 0. Thus the charge
distribution on the lower side of the conducting plane is given by the formula
€ ( @ @
o = ——(r—sint 2 + Ts)
4n? pV (22%)
As p-> © we have o = —C/4z, as we should expect. On the upper side
° a ( oe — sin %)
waAVR—A a

ProBLEM 8. The same as Problem 7, but for a plane with a slit of width 2b,

SouutioN. The xy-plane with a slit along the x-axis may be regarded as the limit of the
hyperbolic cylinders

* #4
ee ee .
as |7| 0. These hyperbolic cylinders are one of the families of co-ordinate surfaces in a
system of ellipsoidal co-ordinates with a0, c->0. The Cartesian co-ordinate
z= V(Ela/)/b.
[As in Problem 7, we seek a solution in the form ¢ = —€zF(é), obtaining for the function F
dé
F = constant X Jaa
sV/(E+8")
Here the coefficient and the constant of integration are determined by the conditions that
F =0 and 1 for z> +0 and —o respectively (i.e. for /f > +0 and —o), and the
final result is
€
$a plete) F va vial,

where we now take +/£ positive and the two signs + correspond to the regions z > 0 and
2<0.

At large distances from the slit we have in the upper half-space £ = y?-+2" = r?, and the
potential is $ = 45 V(|n] £) = 4€0%2/r%, i.e. the field of a two-dimensional dipole of moment
$b? per unit length of the slit (see the formula in §3, Problem 2).

The distribution of charge on the conducting plane is given by

€ y
— #1).
° ale .

5 The forces on a conductor 31

## Section §5: The forces on a conductor

In an electric field certain forces act on the surface of a conductor. These.
forces are easily calculated as follows.
The momentum flux density in an electric field in a vacuum is given by
the Maxwell stress tensor :+
1
— on = —(GE%Sx— ExEx).
An
The force on an element df of the surface of the body is just the “flux” of
momentum through it from outside, and is therefore oidf, = oieredf (the
sign is changed because the normal vector n is outwards and not inwards).
The quantity o;xnz is thus the force Fs per unit area of the surface. Since, at
the surface of a conductor, the field E has no tangential component, we
obtain
F, = nE?/8z, (5.1)
or, introducing the surface charge density o,
F, = 2n02n = 4oE.
We therefore conclude that a “negative pressure” acts on the surface of a
| conductor; it is directed along the outward normal to the surface, and its
magnitude is equal to the energy density in the field.
The total force F on the conductor is obtained by integrating the force
(5.1) over the whole surface:
F= § (E2/87) df. (5.2)
Usually, however, it is more convenient to calculate this quantity from the
general laws of mechanics, by differentiating the energy Y. The force, in
the direction of a co-ordinate g, acting on a conductor is —@%/ég, where
the derivative signifies the rate of change of energy when the body is trans. lated in the q-direction, The energy must be expressed in terms of the
charges on the conductors (which give rise to the field), and the differentiation is performed with the charges constant. Denoting this by the suffix e,
we write
Fy = — (84/29). (63)
Similarly, the projection, on any axis, of the total moment of the forces on
the conductor is .
K= -(6%/04p)e, (5.4)
where y is the angle of rotation of the body about that axis.
+ See The Classical Theory of Fields, §4-8, Addison-Wesley Press, Cambridge (Mass.),
1951; Pergamon Press, London, 1959. —or is there denoted by Tg.
Inthe present case we are applying this formula to a surface which does not precisely
coincide with that of the body, but is some distance away, in order to exclude the effect of
the field structure near the surface (see §1).

32 Electrostatics of Conductors §5
If, however, the energy is expressed as a function of the potentials of the
conductors, and not of their charges, the calculation of the forces from the
energy requires special consideration. The reason is that, to maintain
constant the potential of a moving conductor, it is necessary to use other
bodies. For example, the potential of a conductor can be kept constant by
connecting it to another conductor of very large capacity, a “charge reservoir”. On receiving a charge eg, the conductor takes it from the reservoir,
whose potential ¢g is unchanged on account of its large capacity, although
its energy is reduced by éa¢a. When the whole system of conductors receives
charges eg, the energy of the reservoirs connected to them changes by a
total of —Zeg¢q. Only the energy of the conductors, and not that of the
reservoirs, appears in Y%. In this sense we can say that Y pertains to a
system which is not energetically closed. Thus, for a:‘system of conductors
whose potentials are kept constant, the part of the mechanical energy is
played not by %, but by
& = U- Seba. (5)
Substituting (2.2), we find that Y and Y differ only in sign:
&=-4U.z (5.6)
The force Fy is obtained by differentiating @ with respect to g for constant
potentials, i.e.
Fy = — (00/00), = (8% 00)5. (6.7)
Thus the forces acting on a conductor can be obtained by differentiating %
either for constant charges or for constant potentials, the only difference
being that the derivative must be taken with the minus sign in the first case
and with the plus sign in the second.

The same result could be obtained more formally by starting from the
differential identity .

dU = Bbq deg—Fydg, (5.8)
in which % is regarded as a function of the charges on the conductors and the
co-ordinate g. This identity states that 0Y/deq = ¢g and d%/aq = —Fy.
Using the variables ¢g instead of eg, we have

q d% = —Zeadda— Fa dg, (5.9)
which gives (5.7).

At the end of §2 we have discussed the energy of a conductor in a uniform
external electric field. The total force on a conductor in a uniform field is,
of course, zero. The expression for the energy (2.14) can, however, be
used to determine the force acting on a conductor in a quasi-uniform field

§ The forces on a conductor 33
G, i.e. a field which varies only slightly over the dimensions of the conductor, In such a field the energy can still be calculated, to a first approximation, from formula (2.14), and the force F is the gradient of this energy:

F = —grad Y = }aixV grad (&Ex). (5.10)

The total torque K is in general non-zero even in a uniform external field.
By the general laws of mechanics K can be determined by considering an
infinitesimal virtual rotation of the body. The change in energy in such a
rotation is related to K by 8Y = —K-dwp, dtp being the angle of the rotation. A rotation through an angle Sw in a uniform field is equivalent to a
rotation of the field through an angle —8w relative to the body. The change
in the field is 8¢ = —&ep x &, and the change in energy is

SY = (8U/02E)-3E = —Sp-Ex IY/E.
But 8%/8& = —Y, as we see from a comparison of formulae (2.13) and
(2.14). Hence 8% = —P x E-5p, whence
K= 9xG, (5.11)
in accordance with the usual expression given by the theory of fields in a
vacuum.

If the total force and torque on a conductor are zero, the conductor remains
at rest in the field, and effects involving the deformation of the body (called
electrostriction) become important. The forces (5.1) on the surface of the
conductor result in changes in its shape and volume. Because the force is
an extending one, the volume of the body increases. A complete determina
tion of the deformation requires a solution of the equations of the theory of
elasticity, with the given distribution of forces (5.1) on the surface of the body.

| If, however, we are interested only in, the change in volume, the problem
can be solved very simply. .

| To do so, we must bear in mind that, if the deformation is slight (as in
fact is.true for electrostriction), the effect of the change of shape on the
change of volume is of the second order of smallness. In the first approximation, therefore, the change in volume can be regarded as the result of deformation without change in shape, i.e. as a volume expansion under the action

| of some effective excess pressure Ap which is uniformly distributed over
the surface of the body and replaces the exact distribution given by (5.1).
The relative change in volume is obtained by multiplying Ap by the coefficient of uniform expansion of the substance. The pressure Ap is given,
according to a well-known formula, by the derivative of the electric energy
% of the body with respect to its volume: Ap = —8%/8V.+

Let the deforming field be due to the charged conductor itself. Then the
energy &% = }e2/C, and the pressure is Ap = —4e20C—1/0V. For a given

+ The quantity thus determined is the pressure exerted on the surface by the body itself;
the pressure acting on the surface from outside is obtained by changing the sign.

34 Electrostatics of Conductors §5
shape, the capacity of the body (having the dimensions of length) is proportional to the linear dimension, i.e. to V1/3, Hence

Ap = &/6CV = ed /6V. (5.12)

If an uncharged conductor is situated in a uniform external field , its
energy is given by formula (2.14). The extending pressure is therefore

Ap = houeEiEe. (5.13)
PROBLEMS

Prostem 1. A small conductor of capacity c (equal in order of magnitude to its dimension)
is ata distance r from the centre of a spherical conductor of large radius a (> c). The distance
r—a from the conductor to the surface of the sphere is supposed large compared with c,
but not large compared with a. The two conductors are joined by a thin wire, so that they are
at the same potential ¢. Determine the force of their mutual repulsion.

SoLuTton. Since the conductor ¢ is small, we can suppose that its potential is the sum of
the potential ¢a/r at a distance r from the centre of the large sphere and the potential e/c
due to the charge e on the conductor itself. Hence $ — $a/r-+elc, or e = cd (1—ajr). ‘The
required force of interaction F is the Coulomb repulsion between the charge e on the con
_ ductor and the charge a¢ on the sphere:
of ( @
te Py 4).
r 1)
‘This expression is correct to within terms of higher order in c. Thus the small conductor is
repelled from the sphere with a force which decreases as it approaches the surface.

ProsteM 2. A charged conducting sphere is cut in half. Determine the force of repulsion
between the hemispheres.

Souutton. We imagine the hemispheres separated by an infinitely narrow slit, and determine the force F on each of them by integrating over the surface the force (E?/8n) cos 8,
which is the projection of (5.1) on a direction perpendicular to the plane of separation of the
hemispheres. In the slit E = 0, and on the outer surface E = e/a®, where a is the radius of
the sphere and e the total charge on it. The result is F = e%/8a2.

ProsieM 3, ‘The same as Problem 2, but for an uncharged sphere in a uniform external
field € perpendicular to the plane of separation.

Souvution. As in Problem 2, except that the field on the surface of the sphere is
E =3 € cos 6 (§3, Problem 1). The required force is F = 9a°G?/16.

Prosiem 4, Determine the change in volume and in shape of a conducting sphere in a
uniform external electric field.

Souution. The change in volume AV/V = Ap/K, where K is the modulus of volume
expansion of the material, and Ap is given by formula (5.13). For a sphere, ae = Su
= 38u/47 (§3, Problem 1), so that AV/V = 3G2/87K.

‘Asa result of the deformation, the sphere is changed into a prolate spheroid. To determine
the eccentricity, we may regard the deformation as a uniform pure shear in the volume of
the body, just as, to determine the change in the total volume, we regarded it as a uniform

«volume expansion.

The condition of equilibrium for a deformed body may be formulated as requiring that
the sum of the electrostatic and elastic energies should be a minimum. The former is, by
(2.12) and (4.26),

Vv 3VG 3 a—b,
=-te,y ES 2
Yon = FPS ite RO
+ In Problems 2 and 3 we assume that the hemispheres are at the same potential.

§5 The forces on a conductor 35
where R is the original radius of the sphere, a and b the semiaxes of the spheroid, and
nc }—4(a—b)/15R is the depolarisation coefficient (see (4.33).)

‘Since the deformation is axially symmetrical about the direction of the field (the x-axis),
only the components uzz and yy = uze of the strain tensor are non-zero. Since we are
considering equilibrium with respect to a change in shape, we can regard the volume as
unchanged, i.e. wiz = 0. Hence the elastic energy may be written}

Uear= tunco%V = ors—ovy)(uer—uy)V,
where opis the elastic stress tensor. We have ozs—cyy = 2(uzz—tyy), where # is the modulus of rigidity of the material, and uzz—uyy = (a—b)/R. Hence
Woy = §yla—bPV RP.
Making the sum %es+%e1 a minimum, we have (a—b)/R = 9€?/40mp.

Prosiem 5. Find the relation between frequency and wavelength for waves propagated
on a charged plane surface of a liquid conductor (in a gravitational field). Obtain the condition for this surface to be stable (Ya. I. FRENKEL’, 1935).

SOLUTION. Let the wave be propagated along the x-axis, with the z-axis vertically upwards.
‘The vertical displacement of points on the surface of the liquid is { = aet(#*-at), When the
surface is at rest, the field above it is Ez = E = 47700, and its potential ¢ = —4maoz, where
0 is the surface charge density. The potential of the field above the oscillating surface can
be written as ¢ = —4a00z+¢1, with ¢1 = constant x ef(#2~at) e-z, $1 being a small correction which satisfies the equation A¢i = 0 and vanishes for z > 00. On the surface itself,
the potential must have a constant value, which we take to be zero, and so ¢1 = 4:roof for
z=0.

‘According to (5.1), an additional negative pressure acts on the charged surface of the liquid;
this pressure is, as far as terms of the first order in $1, E®/8a ~ E2/8x ~ 2n00?+[Roog1]s-0

=2n008+4n00%kt. The constant term 2700? is of no importance, since it can be included in
the constant external pressure.

‘The consideration of the hydrodynamical motion in the wave is entirely analogous to the
theory of capillary wavesf, differing only by the presence of the additional pressure mentioned
above. At the surface of the liquid we have the boundary condition pg£-+ p[ 20/at]:—0—

—adt/ax2—4na0% = 0, where a is the surface-tension coefficient, p the density of the
liquid, and © its velocity potential. ® and £ are also related by 2¢/2t = [8®/d2]z-0. Substituting in these two relations { = ae‘*=-o!) and ® = Aet(k=-ot) and eliminating a and A,
we find the required relation between k and w:

eo? = k(gp—4zo0%h-+0k2)/p. (ey

If the surface of the liquid is to be stable, the frequency w must be real for all values of k
(since otherwise there would be complex w with a positive imaginary part, and the factor
e~twt would increase indefinitely). ‘The condition for the right-hand side of (1) to be positive
is (4na02)?—4gpa < 0, or aot < gpa/4n®. This is the condition for stability.

ProsLem 6. Find the condition of stability for a charged spherical drop (RAYLEIGH, 1882).

So.vuTion. The sum of the electrostatic and surface energies of the drop is ¥@ = e?/2C+aS,
where « is the surface-tension coefficient of the liquid, C the capacity of the drop and S its
surface area. Instability occurs (with increasing e) with respect to deformation of the sphere
into a spheroid, and does so when & becomes a decreasing function of the eccentricity (for
agiven volume). The spherical shape always corresponds to an extremum of %; the stability
condition is therefore [2%4/4(a—b)"]a-» > 0, where a and b are the semiaxes of the spheroid,
and the differentiation is carried out with ab? = constant. Using the formula for the surface
‘of a spheroid and (4.18) for its capacity, we find after a somewhat lengthy calculation
e? < 16ma%o.,

+ See Theory of Elasticity, §4, Pergamon Press, London, 1959.

} See Fluid Mechanics, §61, Pergamon Press, London, 1959.



---


## 中文翻译

> **中文：** 第I章——导体的静电场。本笔记基于朗道《连续介质电动力学》原文整理。

### §1 导体的静电场
宏观电动力学处理的是物理量在"物理无穷小"体积元上的平均值。所有物质按电学性质分为导体和介电体两类。在静电场中，导体内电场必须为零（否则会产生电流）。因此导体上的电荷只能分布在表面上。

### §2 导体静电场的能量
带电导体系统的静电能$U = \frac{1}{2}\sum_i e_i\phi_i$（$e_i$为面电荷密度，$\phi_i$为表面势）。该能量也可表示为电场能量密度$w = \mathbf{E}\cdot\mathbf{D}/8\pi$在空间中的积分。

### §3 静电场问题的求解方法
主要解法包括：镜像法（通过引入虚拟电荷满足边界条件）、保角映射法（用于二维问题）和分离变量法。

### §5 作用在导体上的力
导体表面单位面积受到的电场力（静电压强）$p = \mathbf{E}^2/8\pi$，方向垂直于导体表面向外。此力试图将导体表面的电荷拉入真空中。

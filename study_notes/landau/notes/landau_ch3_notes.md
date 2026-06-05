# Landau & Lifshitz《Electrodynamics of Continuous Media》第3章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter III: Steady Current

CONSTANT CURRENT

## Section §20: The current density and the conductivity

Ler us now consider the steady motion of charges in conductors, i.e. constant electric currents. We shall denote by j the mean charge flux density or
electric current density.t In a constant current, the spatial distribution of j
is independent of time, and satisfies the equation

divj = 0, (20.1)
which states that the mean total charge in any volume of the conductor
remains constant.

The electric field in the conductor in which a constant current flows is also
constant, and therefore satisfies the equation

curl E = 0, (20.2)
ie. it is a potential field.

Equations (20.1) and (20.2) must be supplemented by an equation relating
j and E. This equation depends on the properties of the conductor, but in
the great majority of cases it may be supposed linear (Ohm’s law). If the
conductor is homogeneous and isotropic, the linear relation is a simple
proportionality:

j= oE. (20.3)
The coefficient o depends on the nature and state of the conductor; it is
called the electrical conductivity.

In a homogeneous conductor, « = constant and, substituting (20.3) in
(20.1), we have divE = 0. In this case the electric field potential satisfies
Laplace’s equation: Ad = 0. |

At a boundary between two conducting media, the normal component of
the current density must, of course, be continuous. Moreover, by the
general condition that the tangential field component is continuous (which |
follows from curl E = 0; cf. (1.7) and (6.9)), the ratio jz/o must be continuous. Thus the boundary conditions on the current density are

jut = je, Jn/or = juse/oe, (20.4)
or, as conditions on the field,
o1Em = o2En2, En = Ep. (20.5)

+ In this chapter we ignore the magnetic field due to the current, and therefore the
reaction of that field on the current. If this effect is to be taken into account, the definition
of the current density must be refined, which we do in §29.

92 :

§20 The current density and the conductivity 93
At a boundary between a conductor and a non-conductor we have simply
jn = 0, or Ey = 0.¢

An electric field in the presence of a current does mechanical work on the
current-carrying particles moving in the conductor; the work done per unit
time and volume is evidently equal to the scalar product j-E. This work is
dissipated into heat in the conductor. Thus the quantity of heat evolved per
unit time and volume in a homogeneous conductor is

j-E = of? = jo. (20.6)
This is Foule’s law. ‘

The evolution of heat results in an increase in the entropy of the body.
When an amount of heat dQ = j-E dV is evolved, the entropy of the volume
element dV increases by dQ/7. The rate of change of the total entropy of
the body is therefore

dy |dt = f (j-B/T)V. (20.7)
Since the entropy must increase, this derivative must be positive. Putting
j= E, we see that the conductivity o must therefore be positive.

In an anisotropic body (a single crystal), the directions of the vectors j
and E are in general different, and the linear relation between them is

j= onky, (20.8)
where the quantities o, form a tensor of rank two, the conductivity tensor,
which is symmetrical (see below).

The following remark should be made here. The symmetry of the crystal
would admit also an inhomogeneous term in the linear relation between j
and E, giving ji = onEy+ji, with j© a constant vector. The presence of
this term would mean that the conductor was “pyroelectric”, there being a

| non-zero field in it when j= 0. In reality, however, this is impossible,
because the entropy must increase: the term jE in the integrand in (20.7)
could take either sign, and so d.Y/dt could not be invariably positive.

Just as, for an isotropic medium, d¥/dt > 0 leads to o > 0, so for an
anisotropic medium this condition means that the principal values of the
tensor o7z must be positive.

The dependence of the number of independent components of the tensor
ou, on the symmetry of the crystal is the same as for any symmetrical tensor
of rank two (see §13): for biaxial crystals, all three principal values are different, for uniaxial crystals two are equal, and for cubic crystals all three are

+ It should be noticed that the equations curl E = 0, div(oE) = 0 and the boundary
conditions (20.5) thereon are formally identical with the equations for the electrostatic field
in a dielectric, the only difference being that « is replaced by ¢. ‘This enables us to solve
problems of the current distribution in an infinite conductor if the solutions of the corresponding electrostatic problems are known. When the conductor is bounded by a nonconductor this analogy does not serve, because in electrostatics there is no medium for
“In Russian “Joule and Lenz’s law”.

94 Constant Current §20
equal, i.e. a cubic crystal behaves as an isotropic body as regards its conductivity.

The symmetry of the conductivity tensor

Cik = oxi (20.9)
is a consequence of the symmetry of the kinetic coefficients. This general
principle, due to L. ONsacER, may be conveniently formulated, for use here
and in §§25, 26, as follows.t

. Let %1,%2,... be some quantities which characterise the state of the
body at every point. We define also the quantities
Xa = —0S/0xa, (20.10)
where S is the entropy of unit volume of the body, and the derivative is taken
at constant energy of the volume. In a state close to equilibrium, the
quantities xg are close to their equilibrium values, and the Xq are small.
Processes will occur in the body which tend to bring it into equilibrium. The
rates of change of the quantities xg at each point are usually functions only
of the values of the xq (or Xg) at that point. Expanding these functions
in powers of X, and taking only the linear terms, we have
axq/8t = — EZ yavXo. (20.11)
Then we can assert that the coefficients yap (the kinetic coefficients) are
symmetrical with respect to the suffixes a and b:

Yab = You (20.12)

In order to make practical use of this principle, it is necessary to choose
the quantities xq (or their derivatives %q) in some manner, and then to determine the X,. This can usually be done very simply by means of the formula
for the rate of change of the total entropy of the body

df Oxa

—=- Xa— dV, 20.13

dt J 2 at ney
where the integration is extended over the whole volume of the body.

When a current flows in a conductor, dY/d¢ is given by (20.7). Comparing this with (20.13), we see that, if the components of the current density
vector j are taken as the quantities x, then the quantities X, will be the
components of the vector —E/T. A comparison of formulae (20.8) and
(20.11) shows that the kinetic coefficients in this case are the components of
the conductivity tensor, multiplied by 7. Thus the symmetry of this tensor
follows immediately from the general relation (20.12).

+ See Statistical Physics, §119, Pergamon Press, London, 1958; Fluid Mechanics, §58,
Pergamon Press, London, 1959.

§20 The current density and the conductivity 95
PROBLEMS
Prosieo 1. A system of electrodes maintained at constant potentials $a is immersed in a
conducting medium. A current Ja flows from each electrode. Determine the total amount
of Joule heat evolved in the medium per unit time.
SoLutIon. The required amount of heat Q is given by the integral
Q =Jj-Eav = ~Jj-grad ¢ av = —J divgi) av,
taken over the volume of the medium. We transform this into a surface integral, using the
fact that jn = 0 at the outer boundary of the medium, while on the surfaces of the electrodes
$ =constant = ¢a. The result is Q = 3 ¢aJa.
PRoBLeM 2, Determine the potential distribution in a conducting sphere with a current J
entering at a point O and leaving at the point O’ diametrically opposite to O.
°
o
Fic. 14
Soivtion. Near O and O’ (*Fig. 14) the potential must be of the forms ¢ = J/27oR1*
and ¢ = —J/27oRe respectively, Ri and Re being the distances from O and O’. These functions satisfy Laplace’s equation, and the integrals —o J grad $-df over infinitesimal hemispheres about O and O’ are equal to -t J. We seek the potential at an arbitrary point P in the
sphere in the form
scl
$= rally Ra
| where # is a solution of Laplace’s equation having no poles in or on the sphere. It is evident
from symmetry that #, like ¢, is a function of the spherical co-ordinates 7 and @ only.
On the surface of the sphere (r = a) we must have 24/ar = 0. Differentiating, we find the
boundary condition on #:
ay 1/1 1
dR)
If f(r, @) is any solution of Laplace’s equation, then the function
oi)
r,
fre
r
é
is also a solution.t Comparing this with the above boundary condition, we see that the
+ This is easily seen either by direct calculation or from the fact that any solution f(r, @)
of Laplace’s equation depending only on r and @ can be written f = Ecar"Pn (cos 8), where
the cn are constants and the Py are Legendre polynomials.

96 Constant Current §21
condition is met by the solution
fet ya
Ir
3) Gena) > :
Substituting Rie = v/(a?-+7252ar cos 6) and effecting the integration, we have finally
Jt _ 1, 1¢, atreos@ | arcosé
a aeal RT zara cre a ae) )}

Prose 3. Show that the current distribution in a conductor is such that the energy
dissipated is a minimum.

SouvrIon. The minimum concerned is that of the intergal [j-EdV = f (j*/0) dV, with
the subsidiary condition div j = 0 (conservation of charge). Varying with respect to j the
integral J[(j2/e)—2¢ div j]dV, where 2¢ is an undetermined Lagrangian multiplier, and equating the result to zero, we obtain the equation j = —o grad ¢ or curl (j/2) = 0, which is the
same as (20.2) and (20.3).

## Section §21: The Hall effect

If a conductor is in an external magnetic field H, the relation between the
current density and the electric field is again given by j; = oi Ex, but the
components of the conductivity tensor oi are functions of H and, what
is particularly important, they are no longer symmetrical with respect to the
suffixes 7 and k. The symmetry of this tensor was proved in §20 from the
symmetry of the kinetic coefficients. In a magnetic field, however, this
principle must be formulated somewhat differently: when the suffixes are
interchanged, the direction of the magnetic field must be reversed.t Hence
we now have for the components o;4(H) the relations

ou(H) = ov(—H). (21.1)
The quantities o4,(H) and oj:(H) are not equal.
Like any tensor of rank two, oi can be divided into symmetrical and antisymmetrical parts, which we denote by siz and aiz:
ik = Sikt+ Giz. (21.2)
By definition
su(H) = sie(H), — aix(H) = —axi(H), (21.3) |
and from (21.1) it follows that
six(H) = sxi(—H) = siz(—H), (21.4)
au(H) = ax(—H) = —an(—H).
Thus the components of the tensor sj are even functions of the magnetic
field, and those of aiz are odd functions.
+ See Statistical Physics, §119.

§21 The Hall effect 97

Any antisymmetrical tensor aj of rank two corresponds to some axial
vector, whose components are

Gz = Ay, = Ay = —Aza = 4g = Aay (21.5)

In terms of this vector, the components of the product a4,E, can be written
as those of the vector product Exa:

hi = ounEx = sxEe+(Exa)s. (21.6)

The Joule heat generated by the passage of the current is given by the
product j-E. Since the vectors Exa and E are perpendicular, their scalar ‘
product is zero identically, and so

jE = sucEiEx, (21.7)
i.e. the Joule heat is determined (for a given field E) only by the symmetrical
part of the conductivity tensor.

‘The external magnetic field may usually be supposed weak, and the components of the conductivity tensor accordingly expanded in powers of that
field. Since the function a(H) is odd, the expansion of this vector will
involve only odd powers. The first terms are linear in the field, i.e. they
are of the form

a = vnHy. (21.8)
| The vectors a and H are both axial, and the constants az therefore form an
ordinary (polar) tensor. The expansion of the even functions sy(H) will
involve only even powers. The first term is the conductivity oo, in the
absence of the field, and the next terms are quadratic in the field:
Sik = 004k + BiximEhHm. (21.9)
The tensor Bi:1m is symmetrical with respect to 7, k and J, m.

‘Thus the principal effect of the magnetic field is linear in the field and is
given by the term Ex a; it is called the Hall effect. As we see, it gives rise
to a current perpendicular to the electric field, whose magnitude is proportional to the magnetic field. It should be borne in mind, however, that, for
an arbitrary anisotropic medium, the Hall current is not the only current
perpendicular to E; the current sy, also has a component in such a
direction.

The Hall effect may be differently regarded if we use the inverse formulae
which express E in terms of the current density: Ej = o—\yxjx. The inverse
tensor oly, like og itself, can be resolved into a symmetrical part pi, and
an antisymmetrical part which may be represented by an axial vector b:

Ey = pujet(jxb)i. (21.10)

The tensor pix and the vector b have the same properties as sy and a. In
particular, in weak magnetic fields the vector b is linear in the field. In formu
la (21.10) the Hall effect is represented by the term j x b, i.e. by an electric

98 Constant Current §21
field perpendicular to the current and proportional to the magnetic field and
to the current j.

The above relations are much simplified if the conductor is isotropic.
The vectors a and b must then be parallel to the magnetic field, by symmetry. The only non-zero components of the tensor py are prs = pyy and
Pzz, the field being in the z-direction. Denoting these two quantities by p,
and p, and taking the current to lie in the xz-plane, we have

Ez =pijz Ey= —bjn Ez = pyjn (21.11)
\ Hence we see that, in an isotropic conductor, the Hall field is the only
electric field which is perpendicular to both the current and the magnetic

field.

In weak magnetic fields, the vectors b and H are related (in an isotropic
body) by

b= -RH (21.12)
simply. The constant R (called Hail’s constant) may be either positive or
negative. The form of the terms quadratic in H in the relation between E
and j, which enter through the tensor pi, is easily seen from the fact that the
only vectors linear in j and quadratic in H which can be constructed from j
and H are (j-H)H and Hj. Hence the general form of the relation between
E and j in an isotropic body, as far as the terms quadratic in H, is

E = puj+ Rx j+ Bllj+ Palj HDB. (21.13)
PROBLEM
Express the components of the inverse tensor o~ix in terms of those of su and a.
SoxurIoN. The calculations are most simply effected by taking a system of co-ordinates
in which the axes are the principal axes of the tensor sir; the form of the results in an arbitrary
co-ordinate system can easily be deduced from their form in this particular case. The determinant |o| is |
Sez 2 ay
I= Ls a
@y —az see
= SaxSyy8z2t S2xO2"+ Syyay?+ seas?
In the general case we evidently have
Jol = [s|+seacae.
From the minors of this determinant we find the components of the inverse tensor:
oles = pre = (Syyseztax*)/lol,
ogy = paytbs = (azay—azs22)/lo], ...
‘The general expressions which give these for the particular system of co-ordinates chosen |
are
pur = {sNals]tarax}/[o], bs = —sirax/ol.
This completes the solution.

§22 The contact potential 99

## Section §22: The contact potential

In order to remove a charged particle through the surface of a conductor,
work must be done. The work required for a thermodynamically reversible
removal of the particle is called the work function. This quantity is always
positive; this follows immediately from the fact that a point charge is attracted to any neutral body, and therefore to any conductor (see §14). It
will be more convenient to refer this work to unit (positive) charge; the sign
of the work function W thus defined is the same as that of the charge on the
particle removed.

The work function depends both on the nature of the conductor (and its
thermodynamic state, i.e. its temperature and density) and on that of the
charged particle. For example, the work function for a given metal is different for the removal of a conduction electron and for the removal of an ion
from the surface. It must also be emphasised that the work function is
characteristic of the surface of the conductor. It therefore depends, for
instance, on the treatment of the surface and the “contamination” of it. If
the conductor is a single crystal, then the work function is different for
different faces.

To ascertain the physical nature of the dependence of the work function
on the properties of the surface, let us establish its relation to the electric
structure of the surface layer. If p(x) is the charge density not averaged over
physically infinitesimal segments of the x-axis (perpendicular to the layer),
we can write Poisson’s equation in that layer as d’ffdx? = —4mp. Let the
conductor occupy the region x < 0. Then a first integration gives

dé ra
=" ~ Ae fi pdx,
and a second integration (by parts) gives
z z
$-H— 20) = —4ax [ pdx-t4e f xpde.
0 co
For x -> 00, the integral
z
fe dx
—e
tends very rapidly to zero (since the surface of an uncharged conductor is
electrically neutral). Hence
©
$+ 00)—(— 00) = dar f xp de.
—e

100 Constant Current §22
The integral on the right is the dipole moment of the charges near the surface
of the body. These charges form a “double layer”, in which charges of
opposite sign are separated and the dipole moment is non-zero. The structure of the double layer, of course, depends on the properties of the surface
(its crystallographic direction, contamination, etc.). The difference in the
work function for different surfaces of a given conductor is determined by
the difference in the dipole moments.

If two different conductors are placed in contact, an exchange of charged
particles may occur between them. Charges pass from the body with the
smaller work function to that with the greater until a potential difference
between them is set up which prevents further movement of charge. This is
called a contact potential.

ce
SR
LPS
Oe
ines
| mas b
A “ G
o Y,
Wc
. Fro. 15

*Fig. 15 shows a cross-section of two conductors in contact (a and b) near*
their surfaces AO and OB. Let the potentials of these surfaces be ¢a and
¢» respectively. Then the contact potential is ¢ay = ¢y—¢a- The quantitative relation between this potential and the work functions is given by the
condition of thermodynamic equilibrium. Let us consider the work which
must be done on a particle of charge e to remove it from the conductor @
through the surface AO, transfer it to the surface OB, and finally carry it
into the conductor 5. In a state of thermodynamic equilibrium, this work
must be zero.t The work done on the particle in the three stages mentioned
is eWz, e($>—¢a), and —eW, respectively. Putting the sum of these equal to
zero, we find the required relation:

dav = Wo- Wa. (22.1)
Thus the contact potential of the neighbouring free surfaces of two conductors in contact is equal to the difference in their work functions.

The existence of the contact potential results in the appearance of an
electric field in the space outside the conductors. It is easy to determine

+ Of course, in reality a particle can pass from one conductot to another only through
their surface of contact, and not through the space adjoining them, but the work done is
independent of the path.

§23 The galvanic cell 101
this field near the line of contact of the surfaces. In a small region near this
line (the point O in *Fig. 15), the surfaces may be regarded as plane. The*
field potential outside the conductors satisfies the equation
10/06) 1
= -—(r—)+—— = 0,
A$ r al") 7? Be

where 7 and @ are polar co-ordinates with origin at O; on AO and OB the ;
potential takes given constant values. We are interested in the solution
which contains the lowest power of r; this is the leading term in an expansion
of the potential in powers of the small distance r. The solution concerned is
¢ = constant x @. Measuring the angle @ from AO and arbitrarily taking
the potential on AO as zero, we have

$ = $ard/a, (22.2)
where « is the angle AOB. Thus the equipotential lines in the plane of the
diagram are straight lines diverging from O. The lines of force are arcs of
circles centred at O. The field is

1 dav 1
ej er ee 22.3
7 00 ar (22.3)

it decreases inversely as the distance from O.

As has been said above, “contact” potentials also exist between the various
faces of a single crystal of metal. Hence an electric field of the kind just
described must exist near the edges of the crystal. +

If several metallic conductors (at equal temperatures) are connected
together, the potential between the extreme conductors is, as we easily deduce from formula (22.1), simply the difference of their work functions, as
it is for two conductors in direct contact. In particular, if the metal at each
end is the same, the contact potential between the ends is zero. This is
evident, however, because if there were a potential difference between two
like conductors, a current would flow when they were connected, in contra
| diction to the second law of thermodynamics.

## Section §23: The galvanic cell

The statement at the end of §22 ceases to be valid if the circuit includes
conductors in which the current is carried by different means (e.g. metals
and solutions of electrolytes). Because the work function of a conductor is
different for different charged particles (electrons and ions), the total contact
potential in the circuit is not zero even when the conductors at each end are
similar. This total potential difference is called the electromotive force or
e.m.f. in the circuit; it is just the potential difference between the two like
conductors before the circuit is closed. When the circuit is closed, a current
flows in it; this is the basis of the operation of what are called galvanic cells.

+ In reality, all such fields are usually compensated by the field of ions from the atmosphere which “adhere”’ to the surface of the crystal.

102 Constant Current §23
‘The energy which maintains the current in the circuit is supplied by chemical
transformations occurring in the cell.

When we go completely round any closed circuit the field potential must,
of course, return to its original value, i.e. the total change in the potential
must be zero. Let us consider, for example, a contour on the surface of the
conductors. When we pass from one conductor to another, the potential has
a discontinuity ¢ay. The potential drop across any conductor is RJ; where J
is the total current flowing through it and R is its resistance. Hence the
total change in the potential round the circuit is Z¢,,—ZJR. Putting this
equal to zero and using the facts that J is the same at every point in the
circuit and X¢qp is the electromotive force &, we find

J=uR = 6, (23.1)
so that the current in a circuit containing a galvanic cell is equal to the e.m.f.
divided by the total resistance of all the conductors in the circuit (including,
of course, the internal resistance of the cell itself).

Although the e.m.f. of a galvanic cell can be expressed as a sum of contact
potentials, it is very important to note that it is in reality a thermodynamic
quantity, determined entirely by the states of the conductors and independent
of the properties of the surfaces separating them. This is clear; because &
is just the work per unit charge which must be done on a charged particle
when it is carried reversibly along the closed circuit.

To illustrate this, let us consider a galvanic cell consisting of two electrodes
of metals A and B immersed in solutions of electrolytes AX and BX, Xbeing any anion. Let £4 and fg be the chemical potentials of the metals 4
and B, and {4x and fpx those of the electrolytes in solution.t If an elementary charge e is carried along the closed circuit, an ion A+ passes into solution
from the electrode A and an ion Bt passes out of solution to the electrode
B, the change in the charges on the electrodes being compensated by the
passage of an electron from A to B through the external circuit. The result |
is that the electrode A loses one neutral atom, the electrode B gains one,
and in the electrolyte solution one molecule of BX is replaced by one of AX.
Since the work done in a reversible process (at constant temperature and
pressure) is equal to the change in the thermodynamic potential of the system, we have

e&ap = (fa—ex)—(fa—Cax), (23.2)
which expresses the e.m.f. of the cell in terms of the properties of the material
of the electrodes and of the electrolyte solution. |
From (23.2) we can also draw the following conclusion. If the solution
contains three electrolytes 4X, BX, CX and three metallic electrodes A,
B, C, then the e.m.f.s between each pair of them are related by
@ant+€xe = Cac. (23.3)
+ In this section we use the ordinary chemical potentials, i.e. those defined with respect
to one particle.

§24 Electrocapillarity 103
Using the general formulae of thermodynamics, we can relate the e.m.f.
of a galvanic cell to the heat evolved when a current flows, which of course is
actually an irreversible phenomenon. Let Q be the amount of heat generated
(both in the cell itself and in the external circuit) when the unit charge passes.
along the circuit; Q is just the heat of the reaction which occurs in the cell
when a current flows. By a well-known formula of thermodynamics,¢ it is
related to the work & by
aé
= -T?—(—}. 23.4
2 oT ( 7) (23.4)
The definition of the partial derivative with respect to temperature depends
on the conditions under which the process occurs. For example, if the current
flows at constant pressure (as usually happens), then the differentiation is
effected at constant pressure.

## Section §24: Electrocapillarity

The presence of charges on the boundary between two conducting media
affects the surface tension there. This phenomenon is called electrocapillarity.
In practice, the media concerned are both liquids; usually one is a liquid
metal (mercury) and the other is a solution of an electrolyte.

Let ¢1, ¢2 be the potentials of the two conductors, and ¢, e2 the charges
at the surface of separation. These charges are equal in magnitude and
opposite in sign, and thus form a double layer on the surface.

The differential of the potential go of a system of two conductors at given
temperature and pressure is, taking into account the surface of separation,

dg = «dS—e, ddr —e2ddo, (24.1)
where the term adS is the work done in a reversible change dS in the
area S of the surface of separation; « is the surface-tension coefficient.t

The thermodynamic potential go in (24.1) may be replaced by its “‘sur
face part” gs, since the volume part is constant for given temperature and
pressure, and is therefore of no interest here. Putting e, = —e2 = e and
the potential difference $1—¢2 = ¢, we can write (24.1) as
dys = adS—edg. (24.2)
Hence
(26/25), = 2 (24.3)
« being expressed as a function of ¢. Integrating, we find that gs = aS.

See Statistical Physics, §89.

t See Statistical Physics, §139.

104 Constant Current §25
Substitution in (24.2) gives d(aS) = adS—ed¢, or Sda = —edd, whence

o = —(8%/04)p,2, (24.4)
where o = e/S is the charge per unit area of the surface. The relation (24.4),
first derived by G. LrppMaNn and J. W. Grnss, is the fundamental formula
in the theory of electrocapillarity.

In a state of equilibrium, the thermodynamic potential go must be a
minimum for given values of the electric potentials on the conductors.
Regarding it as a function of the surface charges e, we can write the necessary
conditions for a minimum as

Ogps/de = 0 22 g5/0e2 > 0, (24.5)
where the derivatives are taken at constant area S. To calculate these, we
express gos in terms of the thermodynamic potential gos = gos (e):

Ps = gose)— err — cada = gose)—ep. (24.6)
The vanishing of the first derivative gives
Ogos _ Ogos
sd (I)
be Ge u
and then the condition for the second derivative to be positive becomes
Pgs Poors op 1 op
eh aD ety a )
be? be Ge Sia
or
80/84 > 0. (24.7)
This result was to be expected, since the double layer on the surface may be
regarded as a condenser of capacity de/a¢.

Differentiating equation (24.4) with respect to ¢ and using (24.7), we find
that

ax/Op? < 0. (24.8)
This means that the point where da/2¢ = —o = 0 is a maximum of « as
a function of ¢. |

## Section §25: Thermoelectric phenomena |

The condition that there should be no current in a metal is that there is
thermodynamic equilibrium with respect to the conduction electrons. This
means not only that the temperature must be constant throughout the body,
but also that the sum ef+{ should be constant, where {p is the chemical
potential of the conduction electrons in the metal (for ¢ = 0).+ If the metal

+ See Statistical Physics, §25. Here we take { to be the chemical potential defined in the
usual manner, viz. per unit particle (electron).

§25 Thermoelectric phenomena 105
is not homogeneous, fo is not constant throughout the body even if the
temperature is constant. Hence the constancy of the electric potential ¢ in
this case does not mean the absence of a current in the metal, although the
field E = —grad ¢ is zero. This makes the ordinary definition of (as the
average of the true potential) inconvenient, if we wish to take inhomogeneous
conductors into consideration.

It is natural to redefine the potential as ¢+Zo/e, and we shall write this
henceforward as ¢ simply.t In a homogeneous metal, the change amounts to
the adding of an unimportant constant to the potential. Accordingly, the
“field” E = —grad ¢ (which we shall use henceforward) is the same as the
true mean field only in a homogeneous metal, and in general the two differ
by the gradient of some function of the state.

With this definition, the current and field are both zero in a state of
thermodynamic equilibrium with respect to the conduction electrons, and
the relation between them is j = oE (or j; = oiEx) even if the metal is not
homogeneous.

Let us now consider a non-uniformly heated metal, which cannot be in
thermodynamic equilibrium (with respect to the electrons). Then the field
E is not zero even if the current is zero. In general, when both the current
density j and the temperature gradient grad T are not zero, the relation
between these quantities and the field can be written

E = j/o+agradT. (25.1)

| Here a is the ordinary conductivity, and « is another quantity which is an
electrical characteristic of the metal. Here we suppose for simplicity that

the substance is isotropic (or of cubic symmetry), and therefore write the
proportionality coefficients as scalars. The linear relation between E and
grad T is, of course, merely the first term of an expansion, but it is sufficient

in view of the smallness of the temperature gradients occurring in practice.

‘The same formula (25.1), in the form

j = o(B-agrad 7), (25.2)
shows that a current can flow in a non-uniformly heated metal even if the
field E is zero.

As well as the electric current density j, we can consider the energy flux
density q. First of all, this quantity contains an amount ¢j resulting simply

| from the fact that each charged particle (electron) carries with it an energy
eg. The difference q—¢j, however, does not depend on the potential, and
can be generally written as a linear function of the gradients grad 6 = —E
and grad T, similarly to formula (25.2) for the current density. We shall
for the present write this as .
— = q—4j = BE—ygrad T.

+ This definition can also be formulated as follows: the new e¢ is the change in the free
energy when one electron is isothermally brought into the metal. In other words, $ = aF/dp,
where F is the free energy of the metal and p the charge on the conduction electrons per unit

106 Constant Current §25
The symmetry of the kinetic coefficients gives a relation between the coefficient B and the coefficient « in (25.2). To derive this, we calculate the rate
of change of the total entropy of the conductor. The amount of heat evolved
per unit time and volume is —div q. Hence we can put
df di
af i ay.
dt T
Using the equation div j = 0, we have
di 1 1 Ej
SS = A faiv (qa) +aiv gi} = 7 divla—$)——F
The first term is integrated by parts, giving
df Ej (q—¢j)-grad T
— = |—-dV- | >. x
dt J op f T? ee)

This formula shows that, if we take as the quantities Oxq/@t (see §20)
the components of the vectors j and q—dj, then the corresponding quantities
X, are the components of the vectors —E/T and grad T/T. Accordingly
in the relations

E dT
ja oT on Te,
T T?
E grad T
—¢j = BT ——yT? 2 —_,
q- 4 = BT Pe
the coefficients oT? and BT must be equal. Thus B = oaT, so that
q—¢j = o«TE—y grad T. Finally, expressing E in terms of j and grad T
by (25.1), we have the result
q = ($+aT)j— «grad T, (25.4)
where x = y—T2c is simply the ordinary thermal conductivity, which
gives the heat flux in the absence of an electric current.

It should be pointed out that the condition that dY/dt should be positive
places no new restriction on the thermoelectric coefficients. Substituting
(25.1) and (25.4) in (25.3), we obtain

df yp? «(grad o)

— = |(-—+—-..—_] dV > 0, 25.5;

dt ) ( of 72 ° ess) |
whence we find only that the coefficients of thermal and electrical conductivity must be positive.

In the above formulae it was tacitly assumed that an inhomogeneity of |
pressure (or density) at constant temperature cannot cause a field (or current)
to appear in the conductor, and consequently no term in grad p was included in (25.2) or (25.4). The existence of such terms would, in fact, contradict the law of the increase of entropy: the integrand in (25.5) would then

§25 Thermoelectric phenomena 107 ~
contain terms in the products j-grad p and grad T-grad p, which could
be of either sign, and so the integral could not be necessarily positive.

The relations (25.1) and (25.4) indicate various thermoelectric effects.
Let us consider the amount of heat —divq evolved per unit time and
volume in the conductor. Taking the divergence of (25.4), we have

Q =—divq
= div(«grad T)+ E-j+j-grad(«T),
or, substituting (25.1), 5
Q = div(«grad T)+_— 7j-grada. (25.6)
o
The first term on the right pertains to ordinary thermal conduction, and the
second term, proportional to the square of the current, is the Joule heat.
The term of interest here is the third, which gives the thermoelectric effects.

Let us assume the conductor to be homogeneous. Then the change in «
is due only to the temperature gradient, and grad « = (da/dT) grad T; if,
as usually happens, the pressure is constant through the body, da/d7' must
be taken as (8/27). Thus the amount of heat evolved (called the Thomson
effect) is

pjgradT, where p = —Tda/dT. (25.7)
The coefficient p is called the Thomson coefficient. It should be noticed
| that this effect is proportional to the first power of the current, and not to
the second power like the Joule heat. It therefore changes sign when the
current is reversed. The coefficient p may be either positive or negative.
If p > 0, the Thomson heat is positive (i.e. heat is emitted) when the current
flows in the direction of increasing temperature, and heat is absorbed when

it flows in the opposite direction; if p < 0 the reverse is true.

Another effect, called the Peltier effect, occurs when a current passes
through a junction of two different metals. At the surface of contact, the
temperature, the potential and the normal components of the current density
and energy flux density are all continuous. Denoting by the suffixes 1 and 2
the values of quantities for the two metals and equating the normal components of q (25.4) on the two sides, we have, since ¢, T and jz are continuous,

[— aT ax] = —j2T(e2—m),
the x-axis being taken along the normal to the surface. If the positive
direction of this axis is from metal 1 to metal 2, then the expression on the
left-hand side of this equation is the amount of heat taken from the surface
per unit time and area by thermal conduction. This heat loss is balanced by
the evolution at the junction of an amount of heat given by the right-hand
side of the equation. Thus the amount of heat generated per unit time and
area Is

jllie, where Mig = — T(a2—«1). (25.8)

108 Constant Current §25
The quantity IIj2 is called the Peltier coefficient. Like the Thomson effect,
the Peltier effect is proportional to the first power of the current, and changes
sign when the direction of the current is reversed. The Peltier coefficient
is additive: II1s = Iy2+ M23, where the suffixes 1, 2, 3 refer to three different
metals.
A comparison of formulae (25.7) and (25.8) shows that the Thomson and
Peltier coefficients are related by
-rs =) 25.9
) pp = T 7 7). (25.9)
Next, let us consider an open circuit containing two junctions, the two
end conductors being of the same metal (1 in *Fig. 16). We suppose that the*
junctions b and c are at different temperatures T, and T2, while the temperature at each end (a and d) is the same. Then there is a potential difference
called a thermoelectromotive force, which we denote by &7, between the ends.
a b c a
a SN
q hh
Fie. 16
To calculate this force, we put in (25.1) j= 0 and integrate the field
E = «grad T along the circuit (taken to be the x-axis):
a a
dT
or = foge = foar.
dx
a a
The integrations from a to 6 and from ¢ to d are over temperatures from
T2to T; in metal 1, and that from 6 to c is over temperatures from T to Tz
in metal 2. Thus
T, ‘
op = f (xg—o1) dT. (25.10)
Ty
Comparing this with (25.8), we see that the thermo-e.m.f. is related to the
Peltier coefficient by
T, 0
or = - for (25.11)
tT,
Formulae (25.9) and (25.11) are called Thomson's relations.
To conclude this section, we shall give the formulae for the current and
heat flux in an anisotropic conductor. These are derived from the symmetry

§25 Thermoelectric phenomena 109
of the kinetic coefficients in exactly the same way as formulae (25.1) and
(25.4), and the results are
Ey = ot hanje + oin0T]Oxx,
amet eens (25.12)
U-Pit = Toxijn— KOT] Oxe.
Here oi is the tensor inverse to the conductivity tensor oj, and the tensors
ow and x are symmetrical. The thermoelectric tensor «4, however, is
in general not symmetrical. 7
PROBLEM

Find the relations between the coefficients of the various thermogalvanomagnetic effects,
ite., those which occur when a current flows in the simultaneous presence of an electric field,
a magnetic field, and a temperature gradient.

SoxuTION. The discussion is entirely similar to that given above for thermoelectric effects.
It is conveniently carried out in tensor form, so as to be applicable to both isotropic and
anisotropic conductors. We write the electric current density j and the heat flux q as

._ Ee ay.
i= aw +be(r)
ay
tis = ewe! +da2(4)
BOS Op OAT)
where all the coefficients are functions of the magnetic field. ‘The symmetry of the kinetic
coefficients gives
au(H) = ae(—H), — du(H) = dee(—H), @)
ba(H) = cx(—H).
Expressing E and q—dj in terms of j and grad T from (1), we have
Ec = olaje toned] Axe, 8)
1 — Hie = Birje— xe T] Oxx,
where the tensors 0-1, a, 8, « are certain functions of the tensors a, b, ¢, d, and have the following symmetry properties resulting from (2):
o7te(H) = o“h(—H), “
«a(H) = xe(—H), Ba) = Toxs(—H).
‘These are the required relations in their most general form. They generalise those found in
§25 for the case where there is no magnetic field and in §21 for the case where there is no
temperature gradient.

For an isotropic conductor in a weak magnetic field we have, as far as the first-order terms
in H,

E = j/o+a grad T+RHXj-+NHXxgrad T, ()

a—$j = «Tj—« grad T+ NTHXj+LHXxgrad T. ©

Here o and « are the ordinary coefficients of electrical and thermal conductivity, « is the

thermoelectric coefficient which appears in (25.1), R is the Hall coefficient, and N and L

are new coefficients. The term NHxgrad T may be regarded as representing the effect

of the magnetic field on the thermo-e.m-f. (called the Nernst effect), and the term LH x grad T

as representing the effect of this field on the thermal conduction (called the Leduc-Righi
effect).

‘At a boundary between media, the normal components of the vectors j and q are continuous, and therefore so is that of the vector —« grad T-+a7j+NTHxj+LHxgrad T.
‘The term NTHxj gives the influence of the magnetic field on the Peltier effect (called the
Ettingshausen effect).

110 Constant Current §26
‘The amount of heat evolved in the conductor per unit time and volume is Q = —div q.

Here we must substitute q from (6) and replace —grad ¢ = E in accordance with (5).
If the conductor is homogeneous, then the quantities «, N, L, etc. are functions of temperature alone, and so their gradients are proportional to grad T. In the calculation we neglect
all quantities of the second order in H, and to the same approximation we can take curl (j/2)
curl E = 0. We also note that the external field H (arising from sources outside the
conductor under consideration) is such that curl H = 0.t Finally, divj = 0, as for any
constant current. The result is

Pa 1d ;

Q =L 4div(« grad T)—Tj-grad «+ ——(oNT?j x H-grad T.

o oT dT
The last term gives the change in the Thomson effect resulting from the presence of the
magnetic field.

## Section §26: Diffusion phenomena

The presence of diffusion causes certain phenomena in electrolyte solutions which do not occur in solid conductors. We shall assume, for simplicity,
that the temperature is the same everywhere in the solution, and so consider
only pure diffusion phenomena, uncomplicated by thermoelectric effects.

Instead of the pressure p and the concentration ¢, it is more convenient
to take as independent variables the pressure and the chemical potential ¢.
We here define { as the derivative of the thermodynamic potential of unit

~ mass of the solution with respect to its concentration ¢ (at constant p and
T); by the concentration we mean the ratio of the mass of electrolyte in a
volume element to the total mass of fluid in the same volume.t It may be
recalled that the constancy of the chemical potential is (like that of the
pressure and the temperature) one of the conditions of thermodynamic
equilibrium.

The definition of the electric field potential given in §25 has to be somewhat modified in this case, since the current is now carried by the ions of
the dissolved electrolyte, and not by the conduction electrons. A suitable
definition is (cf. the second footnote to §25) ¢ = (@0/8p)-, where ® is the |
thermodynamic potential and p the sum of the ion charges in unit volume
of the solution (after differentiating we put p = 0, of course, because the
solution is electrically neutral). The derivative is taken at constant mass
concentration, i.e. at a given sum of the masses of ions of both signs in
unit volume.

+ This neglects the very weak effect on the evolution of heat resulting from the magnetic |
fields of the currents themselves.

t The chemical potentials are usually defined as {1 = @®/8m1, {2 = 2®/an2, where © is
the thermodynamic potential of any mass of the solution, and 7, nz the numbers of particles
of solute and solvent in that mass of solution. If ® is the thermodynamic potential of unit
mass, then the numbers m and m2 are related by mmi+ nama = 1 (where m1, me are the
masses of the two kinds of particle), and the concentration ¢ = mm. Hence we have

pa 20 20 Om OO om te
“Ge Om ae” Ong Bc moma”
where { is the chemical potential as here defined.

§26 Diffusion phenomena 1
When a gradient of the chemical potential is present, a term proportional
to it is added to the expression for the current density:
j = o(B~Bgradd), (26.1)
in analogy with the added term in (25.2). We shall see below that, for a
given gradient of the chemical potential (and of the temperature), j must
be independent of the pressure gradient, and so no term in grad p appears
in (26.1).t
As well as the electric current, we have to consider the transport of the
mass of the electrolyte which takes place at the same time. It must be borne
in mind that the passage of a current through the solution may be accompanied by a macroscopic motion of the fluid. The mass flux density of the
electrolyte resulting from this motion is pcv, where v is the velocity and p
the density of the solution. The electrolyte is also transported by molecular
diffusion. We denote the diffusion flux density by i, so that the total flux
density is pcv+i. The irreversible processes of diffusion cause a further
increase in entropy; the rate of change of the total entropy ist
cae Ed ay fa. (26.2)
dt T T
Like the electric current density, the diffusion flux may be written as a
linear combination of E and grad @, or of j and grad. Using the symmetry of the kinetic coefficients, we can relate one of the coefficients in this
combination to the coefficient f in (26.1), in exactly the same way as we did
for j and q—dj in §25. The result is
i PP geadt +i 26.3
1= -— 8a J.
(Bfoejpaae + cd
The coefficient of grad ¢ is here expressed in terms of the ordinary diffusion
coefficient. ||
The inadmissibility in (26.1) and (26.3) of terms proportional to the
pressure gradient follows, as in §25, from the law of the increase of entropy:
such terms would make the derivative of the total entropy (26.2) a quantity
of variable sign.
Formulae (26.1) and (26.3) give all the diffusion phenomena in electrolytes,
but we shall not pause here to examine them more closely.
t It should be emphasised, however, that, for a given concentration gradient j does
depend on the pressure gradient:
grad £ = (8/a)p,7 gradc + (9¢/0p)o,r grad p.
t The derivation of the second term is given in Fluid Mechanics, §57.
|| For j = 0 and constant pressure and temperature we have i = —pD grad c.

112 Constant Current §26
PROBLEM

‘Two parallel plates of a metal A are immersed in a solution of an electrolyte AX. Find the
current density as a function of the potential difference applied between the plates.

Souvrion. When the current passes, metal is dissolved from one plate and deposited on
the other. ‘The solvent (water) remains at rest, and a mass flux of metal of densityt
po = jmje occurs in the solution, where j is the electric current density, and m and e are the
mass and charge of an ion A+, This flux is also given by pv = i-+ poe, where i is as shown
in (26.3); assuming the pressure constant throughout the liquid, we have

de m
pe = [ "a i,

D5 = [p= a-o)]; ”
where x is the co-ordinate in the direction of a line joining the electrodes. Since j = constant
in the solution, this gives

fi pDde
i- [7 <, 2)
#* | m= 2
where ci, c2 are the concentrations at the surfaces of the plates, and J is the distance between
them.

The potential difference & between the plates is most simply found from the total amount
of energy Q dissipated per unit time and unit area of the plates, which must equal j@. By
(26.1), (26.2) we have

ay pyit at ydeya
== [0 a
O=TE SlEre Ee feed a)
and therefore, using (1),
es os
pD de ay, om
‘-(—"ao J ele- 1-9] ae 3)
ammo * J abe 12)
ac 7
Formulae (2) and (3) implicitly solve the problem.

If the current j is small, the concentration difference c2—c1 is also small. Replacing the

integrals by ca—ci times the integrands, we find the effective specific resistance of the solution:
e411 au m 2
LL
ee)

. ‘The first term in (3) gives the potential drop (f (j/c) dx) due to the passage of the current.
"The second term is the e.m.f. due to the concentration gradient in the solution (in a certain
sense analogous to the thermo-e.m.f.). ‘This latter expression is independent of the conditions of the particular one-dimensional problem considered, and is the general expression
for the e.m.f. of a “concentration cell”.

} It may be recalled that the hydrodynamic velocity v in a solution is defined so that p
is the momentum of unit volume of the liquid; see Fluid Mechanics, §57. Hence the fact
that in this case only the dissolved metal is moving (relative to the electrodes) does not
affect the calculation of pv.

{ The change in pressure due to the motion of the liquid gives only terms of a higher
order of smallness.



---


## 中文翻译

> **中文：** 第III章——恒定电流。

### 主要内容
本章讨论导电介质中的恒定电流。电流密度$\mathbf{j}$满足电荷守恒定律$\nabla\cdot\mathbf{j} = 0$（恒定电流情况）。欧姆定律$\mathbf{j} = \sigma\mathbf{E}$，其中$\sigma$为电导率。在两种导体界面上的边界条件为：$\mathbf{j}$法向分量连续，$\phi$（电势）连续。

### 关键概念
- **焦耳热**：单位体积内的热耗散功率$q = \mathbf{j}\cdot\mathbf{E} = \sigma E^2$
- **不均匀导体**：当电导率或温度不均匀时，可能出现非稳态现象
- **热电效应**：塞贝克效应和珀尔帖效应

### 应用
电路理论、接地系统设计、电热分析。

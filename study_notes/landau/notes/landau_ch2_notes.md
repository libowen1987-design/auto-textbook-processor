# Landau & Lifshitz《Electrodynamics of Continuous Media》第2章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter II: Electrostatics of Dielectrics

ELECTROSTATICS OF DIELECTRICS

## Section §6: The electric field in dielectrics

WE SHALL now go on to consider a constant electric field in another class of
substances, namely dielectrics. The fundamental property of dielectrics is
that a constant current cannot flow in them. Hence the constant electric
field need not be zero, as in conductors, and we have to derive the equations
which describe this field. One equation is obtained by averaging equation
(1.3), and is again
curl E = 0. (6.1)
A second equation is obtained by averaging the equation div e = 4p:
div E = 47p. (6.2)
Let us suppose that no charges are brought into the dielectric from outside, which is the most usual and important case. Then the total charge
in the volume of the dielectric is zero; even if it is placed in an electric
field we have f pdV = 0. This integral equation, which must be valid for
a body of any shape, means that the average charge density can be written
as the divergence of a certain vector, which is usually denoted by —P:
p= —div P, (6.3)
while outside the body P = 0. For, on integrating over the volume bounded
by a surface which encloses the body but nowhere enters it, we find fpdV
= — fdivP dV = —$P-df=0. P is called the dielectric polarisation, or
simply the polarisation, of the body. A dielectric in which P differs from zero
is said to be polarised. The vector P determines not only the volume charge
density (6.3), but also the density o of the charges on the surface of the
polarised dielectric. If we integrate formula (6.3) over an element of volume
lying between two neighbouring unit areas, one on each side of the dielectric surface, we have, since P = 0 on the outer area (cf. the derivation of
formula (1.9)),

o = Pr, (6.4)
where P,, is the component of the vector P along the outward normal to the
surface.

To see the physical significance of the quantity P itself, let us consider
the total dipole moment of all the charges within the dielectric; unlike the

§6 "The electric field in dielectrics 37
total charge, the total dipole moment need not be zero. By definition, it is
the integral f rad. Substituting p from (6.3) and again integrating over
a volume which includes the whole body we have

_ f rpdv = —f x div Pav = — § x(4f-P)+ f (P-grad)r dV.
The integral over the surface is zero, and in the second term we have
(P-grad)r = P, so that

fraav = [ Par. (6.5)

Thus the polarisation vector is the dipole moment (or electric moment) per
unit volume of the dielectric.t

Substituting (6.3) in (6.2), we obtain the second equation of the electrostatic field in the form

divD = 0, (6.6)
where we have introduced a quantity D defined by

D = E+4nP, (6.7)
called the electric induction.t The equation (6.6) has been derived by
averaging the density of charges in the dielectric. If, however, charges not
belonging to the dielectric are brought in from outside (we shall call these
extraneous charges), then their density must be added to the right-hand side
of equation (6.6):
div D = 4pex. (6.8)
On the surface of separation between two different dielectrics, certain
boundary conditions must be satisfied. One of these follows from the equation curl E = 0. If the surface of separation is uniform as regards physical
properties, || this condition requires the continuity of the tangential component of the field:

Ex = Ens; (6.9)
cf. the derivation of the condition (1.7). The second condition follows from
the equation div D = 0, and requires the continuity of the normal component of the induction:

Din = Dan. (6.10)

+ It should be noticed that the relation (6.3) inside the dielectric and the condition P = 0
outside do not in themselves determine P uniquely; inside the dielectric we could add to
P any vector of the form curl f. P can be completely determined only by establishing its
connection with the dipole moment.

t Sometimes the electric displacement, a term due to MAaxweLt., but one which is obsolete.

|| ‘That is, as regards composition of the adjoining media, temperature, etc. If the
dielectric is a crystal, the crystallographic direction of the surface must be constant, i.e. the
surface must be a plane.

38 Electrostatics of Dielectrics 7
For a discontinuity in the normal component D, = Dz would involve an
infinity of the derivative 0D;/0z, and therefore of div D.

Ata boundary between a dielectric and a conductor, E; = 0, and the condition on the normal component is obtained from (6.8):

E,=0, Dn = 470, (6.11)
where o is the charge density on the surface of the conductor.

## Section §7: The dielectric permeability

In order that equations (6.1) and (6.6) should form a complete set of
equations determining the electrostatic field, they must be supplemented
by a relation between the induction D and the field E. In the great majority
of cases this relation may be supposed linear. It corresponds to the first
terms in an expansion of D in powers of E, and its correctness is due to the
smallness of the external electric fields in comparison with the internal
molecular fields.

The linear relation between D and E is especially simple in the most important case, that of an isotropic dielectric. It is evident that, in an isotropic
dielectric, the vectors D and E must be in the same direction. The linear
relation between them is therefore a simple proportionality:+

D=<. (7.1)
The coefficient ¢ is the dielectric permeability or dielectric constant of the
substance and is a function of its thermodynamic state.

As well as the induction, the polarisation also is proportional to the field:

P = cE = (c—1)E/4n. (7.2)
The quantity « is called the polarisation coefficient of the substance, or its
dielectric susceptibility. Later (§14) we shall show that the dielectric permeability always exceeds unity; the polarisability, accordingly, is always
positive. The polarisability of a rarefied medium (a gas) may be regarded as
proportional to its density.

The boundary conditions (6.9) and (6.10) on the surface separating two
isotropic dielectrics become

Ea = Ep, abn = Ene. (7.3)
Thus the normal component of the field is discontinuous, changing in
inverse proportion to the dielectric permeability of the medium.

+ It should be mentioned, however, that this relation, which assumes that D and E vanish
simultaneously, is, strictly speaking, valid only in dielectrics which are homogeneous as
regards physical properties (composition, temperature, etc.). In inhomogeneous bodies D
may be non-zero even when E = 0, and is determined by the gradients of thermodynamic
quantities which vary through the body. The corresponding terms, however, are very
small, and in practice are of no importance. We shall therefore use the relation (7.1) in
what follows, even for inhomogeneous bodies.

97 The dielectric permeability 39

In a homogeneous dielectric, «= constant, and then it follows from
divD = 0 that divP=0. By the definition (6.3) this means that the
volume charge density in such a body is zero (but the surface density (6.4)
is in general not zero). On the other hand, in an inhomogeneous dielectric
we have a non-zero volume charge density

e-1 1 e-1 1
p= —divP = —div tec D we grad ae grade.

If we introduce the electric field potential by E = —grad ¢, then equation (6.1) is automatically satisfied, and the equation div D = diveE = 0
gives

div (egrad¢) = 0. (7.4)
This equation becomes the ordinary Laplace’s equation only in a homogeneous dielectric medium. The boundary conditions (7.3) can be rewritten as the following conditions on the potential:
$1 = $2, (75)
€1041/8n = e2Gdpo/dn;
the continuity of the tangential derivatives of the potential is equivalent to
the continuity of ¢ itself.

In a dielectric medium which is piecewise homogeneous, equation (7.4)
reduces in each homogeneous region to Laplace’s equation A¢ = 0, so
that the dielectric permeability appears in the solution of the problem only
through the conditions (7.5). These conditions, however, involve only the
ratio of the dielectric permeabilities of two adjoining media. In particular,
the solution of an electrostatic problem for a dielectric body of permeability
€2, surrounded by a medium of permeability «1, is the same as for a body of
permeability ¢g/e1, surrounded by a vacuum.

Let us consider how the results obtained in Chapter I for the electrostatic
field of conductors will be modified if these conductors are not in a vacuum
but in a homogeneous and isotropic dielectric medium. In both cases the
potential distribution satisfies the equation A¢ = 0, with the boundary
condition that ¢ is constant on the surface of the conductor, and the only
difference is that, instead of Ey = —04/0n = 420, we have

Dn = —€0d/0n = 4r0, (7.6)
giving the relation between the potential and the surface charge. Hence it
is clear that the solution of the problem of the field of a charged conductor
in a vacuum gives the solution of the same problem with a dielectric in place
of the vacuum if we make the formal substitution ¢ > ef, e +e or 6 > 4,
e->e/e. For given charges on the conductors, the potential and the field
are reduced by a factor ¢ in comparison with their values in a vacuum.
This reduction in the field can be explained as the result of a partial ‘‘screening” of the charge on the conductor by the surface charges on the adjoining

40 Electrostatics of Dielectrics §7
polarised dielectric. If, on the other hand, the potentials of the conductors are
maintained, then the field is unchanged but the charges are increased by a
factor e.

Finally, it may be noted that in electrostatics we may formally regard a
conductor (uncharged) as a body of infinite dielectric permeability, in the
sense that its effect on an external electric field is the same as that of a dielectric (of the same form) as « > 00. For, since the boundary condition on
the induction D is finite, D must remain finite in the body even for « > 00.
This means that E + 0, in accordance with the properties of conductors.

PROBLEMS

PROBLEM 1, Determine the field due to a point charge e at a distance h from a plane boundary separating two different dielectric media.

So.urion, Let O be the position of the charge e in medium 1, and O’ its image in the plane
of separation, situated in medium 2 (*Fig. 10). We shall seek the field in medium 1 in the form*
of the field of two point charges, e and a fictitious charge e’ at O’ (cf. the method of images,
§3): $1 = elewte'/ar’, where r and r’ are the distances from O and O’ respectively. In
medium 2 we seek the field as that of a fictitious charge e” at O: $2 = e”/ea. On the boundary plane (r =r’) the conditions (7.5) must hold, leading to the equations e—e’ =e”,
(e+e)/er = e”/e2, whence

ef = eei—ea)i(eatex), — e” = ene/(erten). (O)
Pe
y ,
@ = :
o a ao
« &
Fic. 10

For ex -> 00 we have e’ = —e, $2 =0, i.e. the result obtained in §3 for the field of a
point charge near a conducting plane.

"The force acting on the charge e (the “image force’) is

pote (y a-e
~ Qh 2h) eileen)’
F > 0 corresponds to repulsion.

PROBLEM 2. The same as Problem 1, but for an infinite charged straight wire parallel to
a plane boundary surface at a distance h.

Souvrion. As in Problem 1, except that the field potentials in the two media are
$1 = —(2e/e1) log r—(2e’/e1) log r’, $2 = —(2e’/ea) log r, where e, e’, e” are the charges per
unit length of the wire and of its images, and r, r’ are the distances in a plane perpendicular
to the wire. The same expressions (1) are obtained for e’, e”, and the force on unit length of
the wire is F = 2ee’/2her = e*(e1—«2)/hea(erte2).

7 The dielectric permeability 41
PROBLEM 3. Determine the field due to an infinite charged straight wire in a medium with
dielectric constant «1, lying parallel to a cylinder of radius a and dielectric constant e2, at a
distance b (> a) from its axis.+
Soxurion. We seek the field in medium 1 as that produced in a homogeneous dielectric
(with constant «1) by the actual wire (passing through O in *Fig. 11), with charge e per unit .*
length, and two fictitious wires with charges e’ and —e’ per unit length, passing through A
and O’ respectively. ‘The point A is at a distance a?/b from the axis of the cylinder. Then,
for all points on the circumference, the distances r and r’ from O and A are in a constant
ratio r’/r = a/b, and so it is possible to satisfy the boundary conditions on this circumference.
In medium 2 we seek the field as that produced in a homogeneous medium (with constant ea)
by a fictitious charge e” on the wire passing through O.
00" =b
AO’ =0% 8
: ,
ON 28
om a
A o
4 ©
Fie. 11
‘The boundary conditions on the surface of separation are conveniently formulated in
terms of the potential ¢ (E = —grad ¢) and the vector potential A (cf. §3), defined by
D = curl A (in accordance with the equation divD = 0). In a two-dimensional problem,
A is in the z-direction (perpendicular to the plane of the figure). ‘The conditions of continuity for the tangential components of E and the normal component of D are equivalent
to $1 = $2, Ai = Av.
For the field of a charged wire we have in polar co-ordinates r, 8: $ = —(2e/e) log r+
constant, A = 2e6-+constant; cf. (3.18). Hence the boundary conditions are
2"
Ze logr—e logr’+e’ log a) = — a log 7+ constant,
7
2ed-+e'’—e'(8-+6')] = 28,
where the angles are as shown in *Fig. 11, and we have used the fact that OO’B and BO’A*
are similar triangles. Hence ea(e+e’) = ee”, e—e’ =e”, and the expressions for e’ and e”
are again formulae (1) of Problem 1.
‘The force acting on unit length of the charged wire is parallel to OO’, and is
~es)a?
peen (4-4) - are
a \OA~ 00) ~ a(atenb(b?—a?)
| F > 0 corresponds to repulsion.
ProsieM 4. The same as Problem 3, but for the case where the wire is inside a cylinder of
dielectric permeability ¢2(b < a).
+ The corresponding problem of a point charge near a dielectric sphere cannot be solved
in closed form.

42 Electrostatics of Dielectrics §8
So.ution. We seek the field in medium 2 as that due to the actual wire, of charge e per
unit length (O in *Fig. 12), and a fictitious wire of charge e’ per unit length passing through*
A, which is now outside the cylinder. In medium 1 we seek the field as that of wires with
charges e” and e—e” passing through O and O’ respectively. By the same method as in the
preceding problem we find e” = —e(e1.—es)/(e1-+2), e” = 2ae/(aite2). For e2> athe
wire is repelled from the surface of the cylinder by a force
| part 1 __2eana)b
"a 0A aatalat—e)
aS
A
4
00%
OA: 0%
Fie. 12

Prose 5. Show that the field potential ¢ 4(rs) at a point rg in an arbitrary inhomogeneous
dielectric medium, due to a point charge e at ra, is equal to the potential $a(ra) at ra due
to the same charge at rz.

Souvrion. The potentials $(r) and ¢a(r) satisfy the equations

div (¢ grad $4) = —4ne8(r—r4), div (c grad $2) = —4ne8(r—rp).
Multiplying the first by ¢p and the latter by $4 and subtracting, we have
div ($x € grad $4)—div (¢. € grad dz) = —47e8(r—r4)$n(t)-+4e3(r—ra)$.4(2)Integration of this equation over all space gives the required relation:
ga(te) = da(ra).

## Section §8: A dielectric ellipsoid

The polarisation of a dielectric ellipsoid in a uniform external electric
field has some unusual properties which render this example particularly
interesting.

Let us consider first a simple special case, that of a dielectric sphere in an
external field €. We denote its dielectric constant by e“, and that of the
medium surrounding it by «©. We take the origin of spherical co-ordinates
at the centre of the sphere, and the direction of © as the polar axis, and seek
the field potential outside the sphere in the form $@ = &-r+ A€-r/r3; the
first term is the potential of the external field imposed, and the second,
which vanishes at infinity, gives the required change in potential due to the
sphere (cf. §3, Problem 1, solution). Inside the sphere, we seek the field
potential to the form $4 = —B€-r, the only function which satisfies
Laplace’s equation, remains finite at the centre of the sphere, and depends
only on the constant vector & (which is the only parameter of the problem).

The constants A and B are determined by the boundary conditions on
the surface of the sphere. It may be seen at once, however, that the field

§8 A dielectric ellipsoid 43
in the sphere E®) = B& is uniform and differs only in magnitude from the
applied field €

The boundary condition of continuity of the potential gives
E® = €(1—A/R®), where R is the radius of the sphere, and the
condition of continuity of the normal component of the induction gives

D® = e@G(1+2A/R3).
Eliminating A from these two equations, we obtain
3(DO + 2OE0) = Og (8.1)
or, substituting D® = «EW,
EO = 3OE/(2e0+ 0), (8.2)

The problem of an infinite dielectric cylinder in an external field perpendicular to its axis is solved in an entirely similar manner (cf. §3, Problem 2). The field inside the cylinder, like that inside the sphere in the above
example, is uniform. It satisfies the relation

}(DO+ OR) = OG, (8.3)
or
EO = 2G /(L) + A), (8.4)

The relations (8.1) and (8.3), in which the dielectric constant ¢) of the
sphere or cylinder does not appear explicitly, are particularly important
because their validity does not depend on a linear relation between E and
D within the body; they hold whatever the form of this relation (e.g. for
anisotropic bodies). The analogous relations

EO= € (8.5)
| or a cylinder in a longitudinal field and
Do = OE (8.6)
for a flat plate in a field perpendicular to it are similarly valid; these
relations are evident at once from the boundary conditions.

‘The property of causing a uniform field within itself on being placed in a
uniform external field is found to pertain to any ellipsoid, whatever the ratio
of the semiaxes a, b, c. The problem of the polarisation of a dielectric ellipsoid is solved by the use of ellipsoidal co-ordinates, in the same way as the
corresponding problem for a conducting ellipsoid in §4.

Let the external field be again in the x-direction. The field potential outside the ellipsoid may again be sought in the form (4.22): ¢’.=¢oF(é),
with the function F (£) given by (4.23). Such a function cannot, however,
appear in the field potential 4; inside the sphere, since it does not satisfy the
condition that the field must be finite everywhere inside the ellipsoid. For let
us consider the surface £ = —c®, which is an ellipse in the xy-plane, lying
within the ellipsoid. For + —c®, the integral (4.23) behaves as «/(£+c2).

44 Electrostatics of Dielectrics §8
The field, i.e. the potential gradient, therefore behaves as 1/4/(€+¢?), and
becomes infinite at € = —c?. Thus the only solution suitable for the field
inside the ellipsoid is F(£) = constant, so that ¢; must be sought in the
form ¢; = B¢o. We see that the potential ¢; differs only by a constant
factor from the potential ¢o of the uniform field. In other words, the field
inside the ellipsoid is also uniform.

We shall not pause to write out the formulae for the field outside the
ellipsoid, which are of little interest. The uniform field inside the ellipsoid
can be found without actually writing out the boundary conditions, by using
some results already known.

Let us first suppose that the ellipsoid is in a vacuum (e) = 1). Then there
must be a linear relation between the vectors E®, D® and & (which are all
in the x-direction), of the form aE,+bDz = Gz, where the coefficients a, b
depend only on the shape of the ellipsoid, and not on its dielectric permeability «®, The existence of such a relation follows from the form of
the boundary conditions, as we saw above in the examples of the sphere and
the cylinder.

To determine a and b we notice that, in the trivial particular case «# = 1,
we have simply E= D = &, and so a+b = 1. Another particular case for
which the solution is known is that of a conducting ellipsoid. In a conductor
E®) — 0, and the induction D®, though it has no direct physical significance,
may be regarded formally as being related to the total dipole moment of the
ellipsoid by D=4nP = 4r@/V. According to (4.26) we then have
Dz= Ez|n™, ie. b = n@, and so a= 1—n®), Thus we conclude thatt

(1—n®) BO, 4.1 DO, = E,. (8.7)
Similar relations, but with other coefficients, hold for the fields in the y and
z directions. Like the particular formulae (8.1) and (8.3), they are valid
whatever the relation between E and D inside the ellipsoid.

The field inside the ellipsoid, when € is in the x-direction, is found from
(8.7) by putting DO, = eOF®,:

EO, = Eq/[1 + (O— 1], (8.8)
and the total dipole moment of the ellipsoid is

Pa = WPz = (E—1)VESz/4er = dabe(—1)Eq/[1+(— 1). (8.9)

If the field © has components along all three axes, then the field inside the
ellipsoid is still uniform, but in general not parallel to €. For an arbitrary
choice of co-ordinate axes we can write the relation (8.7) in the general form

B®, + nyx(D_— B%) = Gj, (8.10)

+ This result can also be written Ez = €z—4nn(®)Pz. The quantity 4nn'*)Pz is sometimes called the depolarising field. A similar formula holds for a magnetised ellipsoid in a
uniform external magnetic field (see §27). In this case n'#), nlv), n() are called demagnetisation coefficients,

§9 The dielectric permeability of a mixture 45
The transition to the case where the dielectric permeability of the medium
differs from unity is effected by simply replacing «# by e®/e@, Then
formula (8.7) becomes
(1-n@) OHO, + AODO, = dE, (8.11)
This formula can be applied, in particular, to the field inside an ellipsoidal
cavity in an infinite dielectric medium. In this case ¢ = 1.
PROBLEMSt

Prostem 1. Determine the torque on a spheroid in a uniform electric field.

Souurton. According to the general formula (16.13), the torque on an ellipsoid is
K = #X G, where # is the dipole moment of the ellipsoid. In a spheroid, the vector # is
in a plane passing through the axis of symmetry and the direction of €. The torque is perpendicular to this plane, and a calculation of its magnitude from formulae (8.9) gives

Ka ERD Aan AY sin 22

~ 8aine-+1—n]{(1—ne+1 +n)’ :
where a is the angle between the direction of © and the axis of symmetry of the spheroid,
and n is the depolarisation coefficient along the axis (so that the depolarisation coefficients
in the directions perpendicular to the axis are }(1—n)). The torque is directed so that it
tends to turn the axis of symmetry of a prolate (n < 4) or oblate (1 > 4) ellipsoid parallel or
Perpendicular to the field respectively.

For a conducting ellipsoid (¢ > 00) we have
[1 —3n| :
K =~ v@ sin 2a.
Bal =n) V@ sin 2a.

Prose 2. A hollow dielectric sphere (of dielectric constant ¢ and internal and external
radii b and a) is in a uniform external field €. Determine the field in the cavity.

So.vrion. As above in the problem of a continuous sphere, we seek the field potentials
in the vacuum outside the sphere (region 1) and in the cavity (region 3) in the forms
$1 = —€ cos 0 (r—A/r*), $3 = —BEr cos 6, and that in the dielectric (region 2) as ¢2
= —CE cos 6 (r—Djr2), where A, B, C, D are constants determined from the conditions of
continuity of ¢ and ¢ 0¢/@r at the boundaries 1—2 and 2—3. Thus the field Es = BE in
the cavity is uniform, but the field Ez in the sphere is not. A calculation of the constant gives
the result

Es = %eG/[(e+2)(2e+1) —2(e—1)%(b/a)*].

Prostem 3. The same as Problem 2, but for a hollow cylinder in a uniform transverse
field. t

Soxurion. As in Problem 2, with the result

Es = 4e€/[(c-+1)?—-(e—1)*/a)¥].

## Section §9: The dielectric permeability of a mixture

If a substance is a finely dispersed mixture (an emulsion, powder mixture,
etc.), we can consider the electric field averaged over volumes which are
| large compared with the scale of the inhomogeneities. The mixture is a
| homogeneous and isotropic medium with respect to such an average field,
| oe
} In these three Problems the body is assumed to be in a vacuum.
t In a longitudinal field the solution is clearly Es = €.

46 Electrostatics of Dielectrics 99
: and so may be characterised by an effective dielectric permeability, which
we denote by emix. If E and D are the field and induction averaged in this
way, then, by the definition of emix,
D = emsE. (9.1)
If all the particles in the mixture are isotropic, and the differences in their
dielectric permeabilities are small in comparison with ¢ itself, it is possible
to calculate «mixin a general form which is correct as far as terms of the
second order in these differences.
We write the local field as E = E+ 8E, and the local dielectric permeability
as €+5e, where
é= (1) fea (9.2)
is obtained by averaging over the volume. Then the mean induction is
DB = (€+58(E+5E) = £43055, (9.3)
since the mean values of Se and SE are zero by definition. In the zero-order
approximation emix = é; the first non-zero correction term will, of course, be
of the second order in Se, as we see from (9.3).
From the non-averaged equation div D = 0 we have, as far as small terms
of the first order,
div{ (€+ 8e)(E +8E)] = edivsE+E-grad Se = 0,
or, substituting 8E = —grad 34, ¢A8¢ = E-grad 5c. Taking the gradient,
we have
ASE = —(1/2)(E-grad) grad be. (9.4)
The averaging of the product 8c5E in (9.3) is done in two stages. We first
average over the volume of particles of a given kind, i.e. for a given de.
The value of SE thus averaged is easily obtained from equation (9.4): on
account of the isotropy of the mixture as a whole, the operator 0?/@x,2x%
on the right-hand side of (9.4) becomes, after averaging, 451% A, so that we
have ASE = —(1/32)EASc, whence SE = —(1/32)ESe. Multiplying
by 8¢ and effecting the final averaging over all components of the mixture,
we obtain 5<dE = —(1/3e)E(8e)?. Finally, substituting this expression in
(9.3) and comparing with (9.1), we have the required result:
emix = €—(1/3e)Be. 9.5)
This formula can be written in another manner if we put
SS Ser
a = @F8et = a1),
this is accurate to terms of the second order. Then
emi! = el, (9.6)

§10 Thermodynamic relations for dielectrics in an electric field 47
Thus we can say that, in this approximation, the cube root of ¢ is additive.
PROBLEM

Determine the dielectric permeability of an emulsion of low concentration but with an
arbitrary difference between the dielectric permeabilities of the medium (e1) and the disperse
Phase (¢2).

Soxution. In the integral

1 =

a f (D—ak) dV =D—ak
the integrand is zero except within particles of the emulsion. It is therefore proportional to
the volume concentration ¢ of the emulsion, and in calculating it we can assume that the particles are in an external field which equals the mean field E. Assuming the particles spherical
and using formula (8.2), we obtain for the proportionality coefficient between D and E

émix = €1-+3cex(ex—e1) (en +241).

‘This formula is correct to terms of the first order in c. When «1 and ¢2 are nearly equal it is
the same (to the first order in ¢ and the second in ¢2—«1) as the result given by formula (9.6)
for small c.

## Section §10: Thermodynamic relations for dielectrics in an electric field

The question of the change in thermodynamic properties owing to the
presence of an electric field does not arise for conductors. Since there is no
electric field inside a conductor, any change in its thermodynamic properties

| amounts simply to an increase in its total energy by the energy of the field
which it produces in the surrounding space.t This quantity is quite independent of the thermodynamic state (and, in particular, of the temperature)
| of the body, and so does not affect the entropy, for example.

On the other hand, an electric field penetrates into a dielectric and so has
a great effect on its thermodynamic properties. To investigate this effect,
let us first determine the work done on a thermally insulated dielectric
when the field in it undergoes an infinitesimal change.

The electric field in which the dielectric is placed must be imagined as due
to various external charged conductors, and the change in the field can then
be regarded as resulting from changes in the charges on these conductors.¢
Let us suppose for simplicity that there is only one conductor, of charge e
and potential ¢. The work which must be done to increase its charge by an
infinitesimal amount 6e is

8R = $8e; (10.1)
this is the mechanical work done by the given field on a charge Se brought
from infinity (where the field potential is zero) to the surface of the conductor,

+ We here neglect the energy of the attachment of the charge to the substance of the
conductor; this will be discussed in §22.

+ The final results which we shall obtain involve only the values of the field inside the
dielectric, and therefore are independent of the origin of the field. For this reason there is
no need for special discussion of the case where the field is produced, not by charged conductors, but (for instance) by extraneous charges placed in the dielectric itself or by pyroelectric polarisation of it (§13).

48 Electrostatics of Dielectrics §10
ie. through a potential difference of ¢. We shall put 5R in a form which
is expressed in terms of the field in the space filled with dielectric which
surrounds the conductor.

If Dy is the component of the electric induction vector in the direction of
the normal to the surface of the conductor (out of the dielectric and into the
conductor), then the surface charge density on the conductor is —D,/47,
so that

u pp df 1 $ D-df.
e= tn Mn = ri i.
Since the potential ¢ is constant on the surface of the conductor, we can write
1 1
8R = doe = —_.$ #0D-<f = --f div (¢8D) dV.
The last integral is taken over the whole volume outside the conductor.
Since the varied field, like the original field, must satisfy the field equations,
we have div 5D = 0, and so div ($8D) = ¢ div 5D+5D-grad ¢ = —E-85D.
Thus the following important formula is obtained:
aR = | (E-8D/4n) aV. (10.2)
It should be emphasised that the integration in (10.2) is over the whole field,
including the vacuum if the dielectric does not occupy all space outside the
conductor.

The work done on a thermally insulated body is just the change in its
energy at constant entropy. Hence the expression (10.2) must be included
in the thermodynamic relation which gives the infinitesimal change in the
total energy of the body; the latter contains also the energy of the electric
field. Denoting the total energy by %, we therefore have

1
8U= Tag +— | E-sDdY, (10.3)
where T is the temperature of the body and its entropy.t

Accordingly we have for the total free energy} F = Y—-TS

1
8F = - oT += E-SDAY. (10.4)

Similar thermodynamic relations can be obtained for the quantities pertaining to unit volume of the body. Let U, S and p be the internal energy,

+ The body in general becomes inhomogeneous in an electric field, and so the volume
(whose differential is usually included in the expression for 5%) no longer characterises the
state of the body.

t This quantity is meaningful only when the temperature is constant throughout the body.

§10 Thermodynamic relations for dielectrics in an electric field 49
entropy and mass of unit volume. It is well known that the ordinary thermodynamic relation (in the absence of a field) for the internal energy of unit
volume is dU = TdS+Cdp, where ¢ is the chemical potential of the substance.t In the presence of a field in a dielectric, there must be added the
integrand in (10.3):

dU = TdS+Udp+E-dD/4z. (10.5)
For the free energy per unit volume of the dielectric, F = U—TS, we
therefore have

dF = —SdT+{dp+E-dD/42. (10.6)
These relations are the basis of the thermodynamics of dielectrics.

We see that U and F are the thermodynamic potentials with respect to S,
p, D and T, p, D respectively. In particular, we can obtain the field by differentiating these potentials with respect to the components of the vector D:

E = 4n(9U/@D)s, = 40(2F/@D)r,,. (10.7)
The free energy is more convenient in this respect, since it is to be differentiated at constant temperature, whereas the internal energy must be expressed
in terms of the entropy, which is less easy.

Together with U and F, it is convenient to introduce thermodynamic
potentials in which the components of the vector E, instead of D, are the
independent variables. Such are

i = U-E-Dj/4z, F = F-E-D/4z. (10.8)
On differentiating these we have
dU = TdS+Cdp—D-dE/4z, (10.9)
df = —SdT+{dp—D-dE/47. °
Hence, in particular,
D = —4n(dU/2E)s,. = —40(2F/2E)z,,. (10.10)
| It should be noticed that the relation between the thermodynamic quantities with and without the tilde is exactly that which occurs in §5 for the
energy of the electrostatic field of conductors in a vacuum. For the integral
J E-D dV can be transformed in an exactly similar manner to the one at the
t See Statistical Physics, §24, Pergamon Press, London, 1958. Instead of the mass
density we there use the number of particles N per unit volume, which is related to the
density by p = Nm, where m is the mass of one particle. For this reason the chemical
| potentials as defined here and in Statistical Physics differ by a constant factor (the potential
here being referred to unit mass, and there to one particle).
‘We here denote the chemical potential by { instead of the more usual letter y. ‘The use
of the letter p for the mass density as well as the charge density cannot lead to any misunderstanding, because the two quantities never appear together.

50 Electrostatics of Dielectrics §10
beginning of §2, with the equation div D = 0 inside the dielectric and the
boundary condition Dx = 476 on the surfaces of conductors :
1 1
—|E-DdV = —— d¢-DdV
zl in J grad¢
1
= Dy) $oDn df = Edate. (10.11)
Hence we have for the internal energy, for example,
E-D
& = a— | ar = U-Eate, (10.12)
in agreement with the definition (5.5).

It is useful to derive also the formulae for infinitesimal changes in these
quantities, expressed in terms of the charges and potentials of the conductors
(the sources of the field). For example, the variation in the free energy (for
a given temperature) is

(F \r = 8R = Xdadea. (10.13)
For the variation of F we have
(F )r = (8F )\r—SEpata = — Eeadpa. (10.14)
We can say that the quantities without the tilde are the thermodynamic
potentials with respect to the charges on the conductors, while those with
it are thermodynamic potentials with respect to their potentials.

It is known from thermodynamicst that the various thermodynamic
potentials have the property of being minima in a state of thermodynamic
equilibrium, relative to various changes in the state of the body. In formulating these conditions of equilibrium in an electric field, it is necessary to
state whether changes of state with constant charges on the conductors (the
field sources) or those with constant potentials are being considered. For
example, in equilibrium ¥ and ¥ are minima with respect to changes in
state occurring at constant temperature and (respectively) constant charges
and potentials of the conductors (the same is true for Y and Y at constant
entropy).

If any processes (such as chemical reactions) which are not directly related
to the electric field can occur in the body, the condition of equilibrium with
respect to these processes is that F is a minimum for given density, temperature and induction D, or that F is a minimum for constant density, temperature and field E.

Hitherto we have made no assumptions concerning the dependence of D
on E, so that all the thermodynamic relations derived above are valid

t See Statistical Physics, §15.

§10 Thermodynamic relations for dielectrics in an electric field 51
whatever the nature of this dependence. Let us now apply them to an
isotropic dielectric, where a linear relation D = cE holds. In this case
integration of (10.5) and (10.6) gives
= Uy D?/8re,
U = UdS, p) + D2/8re (10.15)
F = F(T, p)+ D?/87e,
where Up and Fo pertain to the dielectric in the absence of the field. Thus
in this case the quantity D?/8me == «E?/87 = ED/8m is the change in the
internal energy (for given entropy and density) or in the free energy (for
given temperature and density), per unit volume of the dielectric medium,
resulting from the presence of the field.
The expressions for the potentials 0 and F are similarly
O = US, p)— <E2/82,
lo(S, p) — «E?/ (10.16)
# = FT, p)— E2/8n.
We see that the differences U—Upy and U—Up in this case differ only in
sign, as they did for an electric field in a vacuum (§5). Ina dielectric medium,
however, this simple result holds good only when there is a linear relation
between D and E.
We shall write out also, for future reference, formulae for the entropy
density S and the chemical potential £, which follow from (10.15):
Ge oF ER D? x)
~ (Ge (Tse) + | ar),
E2/
= So(T,p)+—(—] » 10.17)
ot ars zi), ou
oF E2/ de
=(—) =e) -—(—) . 10.18,
: (Fen f0(7 ) slp) ¢ )
These quantities, of course, differ from zero only inside the dielectric.
The total free energy is obtained by integrating (10.15) over all space.
By (10.11) we have
F-Fy= f E-DdV/8r = 43eaba- (10.19)
This last expression is formally identical with the energy of the electrostatic
field of conductors in a vacuum. The same result can be obtained directly
by starting from the variation 8 (10.13) for an infinitesimal change in the
charges on the conductors. In the present case, when D and E are linearly
related, all the field equations and their boundary conditions are also linear.
Hence the potentials of the conductors must (as for the field in a vacuum)
be linear functions of their charges, and integration of equation (10.13) gives
(10.19).
It should be emphasised that these arguments do not presuppose the dielectric to fill all space outside the conductors. If, however, this is so, we

52 Electrostatics of Dielectrics §11
can go further and use the results at the end of §7 to draw the following
conclusion, For given charges on the conductors, the presence of the dielectric medium reduces by a factor e both the potentials of the conductors
and the field energy, as compared with the values for a field in a vacuum.
If, on the other hand, the potentials of the conductors are maintained constant, then their charges and the field energy are increased by a factor «.
PROBLEM

Determine the height 4 to which a liquid rises in a vertical plane condenser.

Souurion. For given potentials on the condenser plates, ¥ must be a minimum. ¥ includes the energy tpgh? of the liquid under gravity. From this condition we easily obtain
h = (e—1)E%/8apg.

## Section §11: The total free energy of a dielectric

The total free energy F (or the total internal energy %), as defined in §10,
includes the energy of the external electric field which polarises the dielectric. It is also meaningful to consider the total free energy less the energy
of the field which would be present in all space if the body were absent. We
denote this field by €. Then the total free energy in this sense is

J@-@p8x)av, (11.1)
where F is the free energy density. Here we shall denote this quantity by
the letter F, which in §10 signified f FdV. It should be emphasised that the
difference between the two definitions of F is a quantity independent of the
thermodynamic state and properties of the dielectric, and hence it has no
effect on the fundamental differential relations of thermodynamics pertaining to this quantity.t

Let us calculate the change in F resulting from an infinitesimal change
in the field which occurs at constant temperature and does not destroy the
thermodynamic equilibrium of the medium. Since 6¥ = E-8D/47, we have
8H = [ (E-SD—€-8€)dV//4z. This expression is identically equal to

8F = f (D-©)- dE dV /4r+
+ [B-(@D-3€)dV/4r— [(D—E)-3EdV/4n. (11.2)
In the first integral we write 5¢ = —grad 5¢ (where ¢o is the potential of
the field ©) and integrate by parts:
J grad 540-(D-€)dV = $ S¢o(D -€)-df— f Stodiv(D-€) av.

+ It may be noted that there would be no sense in subtracting E?/87 from F, because E
is the field as modified by the presence of the dielectric, and so the difference F—E?/8n
could not be regarded as the free energy density of the dielectric as such. |

§11 The total free energy of a dielectric 53
It is easy to see that both the integrals on the right-hand side are zero. For
the volume integral this follows at once from the equations div D = 0 and
div © = 0 which the induction in the dielectric and the field in the vacuum
must respectively satisfy. The surface integral is taken over the surfaces of
the conductors which produce the field and over an infinitely distant surface.
The latter of these is, as usual, zero, and for each of the conductors
840 = constant, so that $ 849(D—)-df = 54 $(D—€)-df. The field ©, by
definition, is produced by the same sources as the field E and induction D
(i.e. by the same conductors with given total charges e). Hence the two
integrals § Dadf and § Endf are both equal to 47e, and their difference is
zero.

Similarly, we can see that the second term in (11.2) is also zero, by putting
E = —grad ¢ and using the same transformation. Finally, we have

— JD-B)-8€dV//4x = — [P-3€ar. (11.3)
It should be noticed that the integral in this expression need be taken only
over the volume of the dielectric medium, since outside it P = 0.

However, we must emphasise that the integrand P-5€ cannot be interpreted as the variation of the free energy density in the same way as was done
with formulae (10.3), (10.4). First of all, this density must exist outside the 5
body, which modifies the field in the surrounding space also. It is clear, ~
moreover, that the energy density at any point in the body can depend only
on the field actually present there, and not on the field which would be
present if the body were removed.

If the external field € is uniform, then

8F = —3€. [Pav = — P-&, (11.4)
where # is the total electric dipole moment of the body. Hence the thermodynamic identity for the free energy can be written in this case as

dF = —fdT— P-d. (11.5)

The total electric moment of the body can therefore be obtained by differentiating the total free energy:

P = —(dF [0€)r. (11.6)

The latter formula can also be obtained directly from the general statistical
formula

8H 0d = (AF [Ar)x,
where # is the Hamiltonian of the body as the system of its component
particles, and A is any parameter characterising the external conditions in
which the body is placed.t For a body in a uniform external field , the

t See Statistical Physics, §§11, 15.

54 Electrostatics of Dielectrics §11
Hamiltonian contains a term —€-P, where F is the dipole moment operator. Taking © as the parameter A, we obtain the required formula.

If D and E are connected by the linear relation D = cE, we can similarly
calculate explicitly not only the variation 8¥ but F itself. We have

F-F) = | (E-D-©)dV/8r.
This can be identically transformed into
F—-Fo= | (E+€)-D-G)AV/8x— [ €-(D-E)dV/8r.

The first term on the right is zero, as we see by putting

E+€ = —grad ($+¢0)
and again using the same transformation. Hence we have

F-FA\V,T) = -4/-Pay. (11.7)

Jn particular, in a uniform external field

F-FA\V,T) = --P. (11.8)

This last equation can also be obtained by direct integration of the relation (11.3) if we notice that, since all the field equations are linear when
D=éE, the electric moment # must be a linear function of €.

The linear relation between the components of # and € can be written

FP, = Vax, (11.9)
as for conductors (§2). For a dielectric, however, the polarisability depends
not only on the shape but also on the dielectric constant. The symmetry of
the tensor a4, mentioned in §2, follows at once from the relation (11.6); it
is sufficient to notice that the second derivative 02F/8E,6E; = —OP;/ OC,
= —Voaiz is independent of the order of differentiation.

Formula (11.7) becomes still simpler in the important case where « is
close to 1, i.e. the dielectric susceptibility « = («—1)/4z is small. In this
case, in calculating the energy, we can neglect the modification of the field
due to the presence of the body, putting P = «E ~ «€. Then

F-Fo= —h (EUV, (11.10)
the integral being taken over the volume of the body. In a uniform field,
the dipole moment # = VG, and the free energy is

F-Fo = — VE (11.11)

§12 Electrostriction of isotropic dielectrics 55

In the general case of an arbitrary relation between D and E, the simple
formulae (11.7) and (11.8) do not hold. Here the formula

2 E-D
F = f(e-E) w= Jlp-o-ae-¢] av (11.12)
8rr, 80
may be useful in calculating F; its derivation is obvious after the above
discussion. Here also the integrand in the latter integral is zero outside the
body, so that the integration is taken only over the volume of the body.
PROBLEM

Derive the formula which replaces (11.7) when the body is not in a vacuum but in a
medium of dielectric permeability ‘¢),

SoLuTIoN. Using the same transformations as before, we find

1
F—F— ~~ [ €-D—08) av.

## Section §12: Electrostriction of isotropic dielectrics

For a solid dielectric in an electric field the concept of pressure cannot be
defined as for an isotropic body in the absence of a field, because the forces
acting on a dielectric (which we shall determine in §§15, 16) vary over the
body, and are anisotropic even if the body itself is isotropic. An exact
determination of the deformation (electrostriction) of such a body involves
the solution of a complex problem of the theory of elasticity.

However, matters are much simpler if we are interested only in the change
in the total volume of the body. As we saw in §5, the shape of the body
may then be regarded as unchanged, i.e. the deformation may be regarded
as a uniform volume compression or expansion.

We shall neglect the dielectric properties of the external medium (the atmosphere, for instance) in which the body is situated, i.e. we suppose that « = 1.
This medium thus serves merely to exert a uniform pressure on the surface
of the body, which we shall denote by p. If F is the total free energy of the
body, then we have the thermodynamic relation p = —(@F/V)7, and
accordingly the expression for the differential d¥ contains a term —pdV.
For example, in a uniform external field, (11.5) becomes

dF = —SAT—p dV—P-dE.
We introduce the total thermodynamic potential of the body in accordance
with the usual thermodynamic relation
w= Ftp. (12.1)
The differential of this quantity in a uniform external field is
dgo = —~f£dT+Vdp— Pd. (12.2)

56 Electrostatics of Dielectrics §12
The change in the thermodynamic quantities in an external electric field is
usually a relatively small quantity. It is knownt that a small change in the
free energy (for given T and V) is equal to the small change in the thermodynamic potential (for given T and p). Hence, besides (11.8), we can write
analogously

= go-kE-P (12.3)
for the thermodynamic potential of a body in a uniform external field. Here
gpo is the value for the body in the absence of the field and for given values
of p and T, while Fo in (11.8) is the free energy in the absence of the field

. and for given values of V and T.

Making explicit the dependence of the dipole moment on V and accord
ing to (11.9), we can rewrite (12.3) as
wp = gop, T)—WanEEr, (12.4)

where the correction term must be expressed as a function of temperature
and pressure by means of the equation of state for the body in the absence
of the field. In particular, for a substance of small dielectric susceptibility
this formula becomes simply

gp = gp, T)-3KVE; (12.5)
ef, (11.11).

The required change in volume V—Vp in the external field can now be
obtained immediately by differentiating go with respect to pressure for
constant T and ©. For example, from (12.5) we have

V—Vo = IA xVVep]. (12.6)
‘This quantity may be either positive or negative (whereas, in electrostriction of conductors, the volume is always greater in the presence of the field).

Similarly, we can calculate the amount of heat Q absorbed in a dielectric
when an external electric field is isothermally applied (the external pressure
being constant).t Differentiation of go—goo with respect to temperature
gives the change in the entropy of the body, and by multiplying this by T
we obtain the required quantity of heat. For example, from (12.5) we obtain

OQ = YET [A KV eT p. (12.7)
Positive values of Q correspond to absorption of heat.
PROBLEMS

ProsiEM 1. Determine the change in volume and the electrocaloric effect for a dielectric
ellipsoid in a uniform electric field parallel to one of its axes.

t See Statistical Physics, §15.

} If the body is thermally insulated, the application of the field results in a change of
temperature AT = —Q/Cp, where Cp is the specific heat at constant pressure.

§12 Electrostriction of isotropic dielectrics 57

Soution. From formulae (12.3) and (8.9) we have

Vooe-1
= goo— —-——_—_ ©.
ae oe i—n

‘The relative change in volume is found to be

V—Vo -¢ e-1 1 1 (2) ]

Vi &alneti—nK (ne+1—n)*\ap) 7)”
and the electrocaloric effect
3 = 1 ae
o=- TO ott sora) |
82 Lneti—n | (ne+1—n)NOT) >.

where 1/K = —(1/V)(aV/ap)r is the compressibility of the body, and a = (1/V)(@V/2T)p
the thermal expansion coefficient.

In particular, for a plane disc in a field perpendicular to it, n = 1, so that

V-Vo _ ae 101 (&) ]
Vo Ble Ke Nepal”
° res + 1 (35) ]
= | a+ =() |.
ar Le 2\ar) >.
For a similar disc (or any cylinder) in a longitudinal field, n = 0, and
a re 2 a
YoYo _ G11 _ (8) 9 HELA tae(2) J.
Vo 8al K ep) 7 8 aT)»

PRoBLEM 2. Determine the difference between the heat capacity 4 of a plane disc in a
field perpendicular to it, with a constant potential difference between its faces, and the heat
capacity @p at constant induction, the external pressure being maintained constant in
each case. t

Souution. According to the results of Problem 1, the entropy of the disc is

ago V@pe-1_ | 1/2
2- (5) ¢° 100 fe HB}
( are oe D+ St alae),
‘The induction inside the disc is the same as the external field: D = €. Hence, to calculate
the heat capacity @p, we must differentiate £ for constant €. The potential difference
between the faces of the disc is $ = El = € /e, where Js its thickness. For a uniform compression or expansion of a body, / is proportional to V+. Hence, to calculate the heat capacity
€ 4, we must differentiate / for constant EVi/e. The required difference is found to be
TVG 1 a) Wf 1/ a
creo FE econ 6) JEG) -F]
op = [et AGr), aT), te

ProsieM 3. Determine the electrocaloric effect in a homogeneous dielectric whose total
volume is kept constant.

Souution. Strictly speaking, when an external field is applied the density of the body
changes (and ceases to be uniform), even if the total volume is kept constant. In calculating
the change in the total entropy, however, we can ignore this and assume the density p constant
at every point.}

t @¢ is the heat capacity of a disc between the plates of a plane condenser in circuit
with a constant e.m.f. In an unconnected condenser with constant charges on the plates,
the heat capacity of the disc is © p.

The change in density 3p is of the second order with respect to the field (~E®), and the
consequent change in the total entropy is of the fourth order: the term in the change of
total entropy which is linear in 3p is (@S0/2p){ 8p dV, and the integral is zero because the

total mass of the body is unaltered.

58 Electrostatics of Dielectrics §13

According to (10.17) the total entropy of the body is

S= Flo, T)+ > (=) f mar,
= AM IT aT). Q
where the integration is over the volume of the body. The amount of heat absorbed is
T/ 2
= (5) | Bav.
2- slr), J

Prostem 4. Determine the difference 4 —@ p (see Problem 2) when the total volume of
the disc is kept constant.

Souution. When the volume, and therefore the thickness, of the disc are constant, differentiation for constant potential difference is equivalent to differentiation for constant field E.
Using the formula of Problem 3 for the entropy we have

TVE% de) ®
2p = T= (Z)
BD “Fae NOT) y

ProsLem 5. A condenser consists of two conducting surfaces at a distance h apart which is
small compared with their dimensions; the space between them is filled with a substance
of dielectric permeability «1. A sphere of radius a <h and dielectric permeability es is
placed in the condenser. Determine the change in capacity.

SouvTIoN. Let the sphere be placed in the condenser in such a way that the potential
difference $ between the plates remains unchanged. ‘The free energy for constant potentials of the conductors is #. In the absence of the sphere, ¥ = —4Cog®, where Co is the
original capacity of the condenser. Since the sphere is small, we may imagine it to be brought
into a uniform field € = ¢/h, and the change in F is small. The small change in ¥ at con‘stant potentials is equal to the small change in ¥ at constant charges on the sources of the
field. Using the formula derived in §11, Problem, and (8.2), we have

F = —4Cog? —faPele(el — led) $2/(2el) + elt) h?,
whence the required capacity is
C= Cot adelr(elt)—ele)/(2(6-+ eH) 2,

## Section §13: Dielectric properties of crystals

In ‘an anisotropic dielectric medium (a crystal) the linear relation between
the electric induction and the electric field is less simple, and does not reduce
to a simple proportionality.

The most general form of such a relation is

Dy = Doi + «xE, (13.1)
~ where Do is a constant vector, and the quantities «;, form a tensor of rank
two, called the dielectric permeability tensor (or simply the dielectric tensor).
The inhomogeneous term Dp in (13.1) does not, however, appear for all
crystals. The majority of the types of crystal symmetry do not admit this
constant vector (see below), and we then have simply
Dt = exEx. (13.2)
The tensor «4, is symmetrical: y
tk = eke (13.3)

§13 Dielectric properties of crystals 59
In order to prove this, it is sufficient to use the thermodynamic relation
(10.10) and to observe that the second derivative —470°F/0E,0E; = 0D;/0Ex
= «qx is independent of the order of differentiation.

For F itself we have (when (13.2) holds) the expression

F = Fo- pF yEx|80. (13.4)
The free energy F is
F = FLED, 40 = FoteeDDi/8r. (13.5)

Like every symmetrical tensor of rank two, the tensor «4, can be brought
to diagonal form by a suitable choice of the co-ordinate axes. In general,
therefore, the tensor ¢ is determined by three independent quantities, namely
the three principal values €“), e®), ¢), All these are necessarily greater than
unity, just as « > 1 for an isotropic body (see §14).

The number of different principal values of the tensor «4, may be less than
three for certain symmetries of the crystal.t

In crystals of the triclinic, monoclinic and rhombic systems, all three
principal values are different; such crystals are said to be biaxial.t In
crystals of the triclinic system, the directions of the principal axes of the
tensor ¢4z are not uniquely related to any directions in the crystal. In those
of the monoclinic system, one of the principal axes must coincide with the
axis of symmetry of the second order or be perpendicular to the plane of
symmetry of the crystal. In crystals of the rhombic system, all three principal axes of the tensor ex are crystallographically fixed.

Next, in crystals of the tetragonal, rhombohedral and hexagonal systems,
two of the three principal values are equal, so that there are only two independent quantities; such crystals are said to be uniaxial. One of the principal
axes coincides with the axis of crystal symmetry of the fourth, third or sixth

order, but the directions of the other two principal axes can be chosen
arbitrarily. ||

Finally, in crystals of the cubic system all three principal values of the
tensor «4x are the same, and the directions of the principal axes are entirely
arbitrary.tt This means that the tensor ¢4% is of the form e4,, i.e. it is determined by a single scalar e. In other words, as regards their dielectric properties, crystals of the cubic system are no different from isotropic bodies.

+ The fairly obvious symmetry properties of the tensor e that are given below can be
very simply obtained by using a result of tensor algebra: to every symmetrical tensor of rank
two there corresponds a tensor ellipsoid, the lengths of whose semiaxes are proportional to
the Principal values of the tensor. The symmetry of the ellipsoid corresponds to that of the
OP This name refers to the optical properties of the crystals; see §§78, 79.

|] In this case the tensor ellipsoid degenerates into a spheroid, completely symmetrical
about the longitudinal axis. It should be emphasised that, as regards the physical properties
of the crystal which are determined by a symmetrical tensor of rank two, the presence of
an axis of symmetry of the third or higher order is equivalent to complete isotropy in the
plane perpendicular to this axis.

tt The tensor ellipsoid here degenerates into a sphere.

60 Electrostatics of Dielectrics §13
Let us now examine the dielectric properties of crystals for which the
constant term Do appears in (13.1). The presence of this term signifies that
the dielectric is spontaneously polarised even in the absence of an external
electric field. Such bodies are said to be pyroelectric. The magnitude of this
- spontaneous polarisation is, however, in practice always very small (in comparison with the molecular fields). This is because large values of Do would
lead to strong fields within the body, which is energetically unfavourable and
therefore could not correspond to thermodynamic equilibrium. The smallness of Do also ensures the legitimacy of an expansion of D in powers of E,
of which (13.1) represents the first two terms.

The thermodynamic quantities for a pyroelectric body are found by

integrating the relation —470F/0E; = Di = Doi +eixEx, whence
F = Fo— cxE(Ex/8x—E,Doi/4z. (13.6)
The free energy is
F = F+E,Di/4a = Fot ee EiEx|80
= Fo+ee(Di— Doi)(Dz— Dox)/87. (13.7)
It should be noted that the term in F linear in E; does not appear in F.t

The total free energy of a pyroelectric can be calculated from formula
(11.12) by substituting (13.7) and (13.1). If there is no external field, € = 0,
and we have simply

F = [ [Fo—(E-Do/82)] dV. (13.8)
It is remarkable that the free energy of a pyroelectric in the absence of an
external field depends, like the field E, not only on the volume of the body
but also on its shape.

As has already been pointed out, the phenomenon of pyroelectricity is
not possible for every crystal symmetry. Since, in any symmetry transformation, all the properties of the crystal must remain unchanged, it is clear that
the only crystals which can be pyroelectric are those in which there is a
direction which is unchanged (and, in particular, not reversed) in all symmetry transformations, and that this will be the direction of the constant
vector Do.

This condition is satisfied only by those symmetry groups which consist
of a single axis together with planes of symmetry which pass through the
axis. In particular, crystals having a centre of symmetry certainly cannot be

+ It should also be noted that in these formulae we neglect the piezoelectric effect, i.e. the
effect of internal stresses on the electric properties of a body; see §17. ‘The formulae given
here are therefore, strictly speaking, applicable only when the fields are uniform throughout
the body, and internal stresses do not arise. |

§13 Dielectric properties of crystals 61
pyroelectric. We may enumerate those out of the 32 crystal classes in which
pyroelectricity occurs:

triclinic system: C,

monoclinic system: C's, Co

rhombic system: Coy

tetragonal system: C4, Cay

thombohedral system: C3, C3y

hexagonal system: Cg, Cgp.
There are, of course, no pyroelectric cubic crystals. In a crystal of class
C, the direction of the pyroelectric vector Do is not related to any direction
fixed in the crystal; in one of class C,, it must lie in the plane of symmetry.
In all-the remaining classes listed above the direction of Do is that of the
axis of symmetry.

It should be mentioned that, under ordinary conditions, pyroelectric
crystals have zero total electric dipole moment, although their polarisation
is not zero. The reason is that there is a non-zero field E inside a spontaneously polarised dielectric. Since a body usually has a small but non-zero
conductivity, the presence of a field gives rise to a current, which flows until
the free charges formed on the surface of the body annihilate the field inside
it. The same effect is produced by ions deposited on the surface from the
air. Experimentally, pyroelectric properties are observed when a body is

| heated and a change in its spontaneous polarisation is detected.
| PROBLEMS

Prose 1. Determine the field of a pyroelectric sphere in a vacuum.

SoLution. The field inside the sphere is uniform, and the field and induction are related
by 2E = —D (as follows from (8.1) when © = 0, i.e. when there is no applied external
field). Substituting in (13.1), we obtain the equation 2E:-+ «Et = —Dox. We take the coordinate axes to be the principal axes of the tensor «. Then this equation gives Ex =

| —Doi/(2-+€). The polarisation of the sphere is Pt = (Di—E;)/4x = 3Doi/4n(2+ el"). .
‘The field outside the sphere is that of an electric dipole of moment ? = PV.

PROBLEM 2. Determine the field of a point charge in a homogeneous anisotropic medium.

SoLution. The field of a point charge is given by the equation div D = 4ze8(r) (the
charge being at the origin). In an anisotropic medium D; = exEx = —ex 0¢/dxx; taking
the co-ordinate axes x, y, along the principal axes of the tensor «ix, we obtain for the poten
tial the equation

2) 224] Ox2-+ €(W) 224] By2+ (2) 024/22 = —4ne8(x) By) (2).

By the introduction of new variables
vaxlye, 9 =ylVe, 2! = ale, on)
this becomes
ee eh aH 4ne » gran ren
geet aya tae ~~ yeamicinaay 20°) 907) 2,
t In Problems 2-5 the anisotropic dielectric is assumed not to be pyroelectric.

62 Electrostatics of Dielectrics §13
which formally differs from the equation for the field in a vacuum only in that e is replaced
by ¢/v/(el#elWel®)), Hence
Ao a + =]:
7 Wem Lea "WT ,
In tensor notation, independent of the system of co-ordinates chosen, we have
$= elV (leletnxixe),
where |e| is the determinant of the tensor «ix.

ProsieM 3. Determine the capacity of a conducting sphere, of radius a, in an anisotropic
dielectric medium.

SotuTIoN. By the transformation shown in Problem 2, the determination of the field of a
sphere with charge e in an anisotropic medium reduces to the determination of the field in a
vacuum due to a charge e’ distributed over the surface of the ellipsoid «itx’ix’e = ¢(*)x'2+
-+<Wy’24 el2)2’2 = a®, Using formula (4.14) for the potential due to an ellipsoid, we find
the required capacity to be given by

1 1 ; a a ayy
37 yaaa | [Bl S\( Sl] a

ProsieM 4, Determine the field in a flat anisotropic plate in a uniform external field €.

SoLUTION. From the condition of continuity of the tangential component of the field it
follows that E = €+An, where € is the uniform field outside the plate, n a unit vector
normal to its surface, and A a constant. The constant is determined from the condition of
continuity of the normal component of the induction, n-D = n-@, or mexEr = menEe+
+ Acunne = En. Hence A = —(ctx—8in)niCe/ermninm.

PRoBLEM 5. Determine the torque on an anisotropic dielectric sphere, of radius a, in a
uniform external field © in a vacuum.

SoLuTIon. According to (8.2) we have for the field inside the sphere Ex = 3Gz/(e)+2),
and similarly for Ey, Ez. Here the axes of x, y, 2 are taken to be the principal axes of the
tensor ey. Hence the components of the dipole moment of the sphere are

4 a1
Pr= yz Pr= wan” Ez, ete.
‘The components of the torque on the sphere are
Kz = (PX@)s = 308 Ee G, (2) ew) (e+ (004.2),
and similarly for Kz, Ky.

ProsteM 6. An infinite anisotropic medium contains a spherical cavity of radius a. Express
the field in the cavity in terms of the uniform field E‘¢) far from the cavity.

SoLUTION. The transformation (1) of Problem 2 reduces the equation for the field potential
in the medium to Laplace’s equation for the field in a vacuum. The equation for the field in
the cavity is transformed into that for the field in a medium with dielectric constants 1/e),
1/e, 1/e#), Moreover, the sphere is transformed into an ellipsoid with semiaxes a/+/«(*),
alVeW), a/c), Let ni), n), n(*) be the depolarisation coefficients of such an ellipsoid
(given by formulae (4.25)). Applying formula (8.7) to the field of this ellipsoid, we obtain
the relation

ag — nl) agi — aged
dante) 2 4 7
(an) a Ta ag ax?
and similarly for the y and 2 directions. Returning to the original co-ordinates, we have
7 ag/ax’ = v/«) a$/0x = V/<@Ez, so that the field in the cavity is
(Wg 2 —__ pe,
EO, = <2) —n@e@)—1) Lies
|

§14 The sign of the dielectric susceptibility 63

## Section §14: The sign of the dielectric susceptibility

To elucidate the way in which the thermodynamic quantities for a dielectric in a field depend on its dielectric constant, let us consider the formal
problem of the change in the electric component of the total free energy of
the body when « undergoes an infinitesimal change.

For an isotropic (not necessarily homogeneous) body we have by (10.19)
F—F = §(D?/8me)dV. When « changes, so does the induction, and the
variation in the free energy is therefore

D-sD D E-8D E
3g = i aw feeadea” J ——dV J a oeaV.
The first term in the last member is the same as (10.2), which gives the work
done in an infinitesimal change in the field sources (i.e. charges on conductors). In the present case, however, we are considering a change in the field
but no change in the sources. This term therefore vanishes, leaving
8F = —- J 8<(B?/8n)aV. (14.1)

From this formula there follows, first of all, an important result: any increase in the dielectric constant of the medium, even if in only a part of it .
(the sources of the field remaining unchanged), reduces the total free energy.
In particular, we can say that the free energy is always reduced when un
charged conductors are brought into a dielectric medium, since these
conductors may (in electrostatics) be regarded as bodies whose dielectric
constant is infinite. This conclusion generalises the theorem (§2) that the
energy of the electrostatic field in a vacuum is diminished when an uncharged
conductor is placed in it.

Formula (14.1) can also be used to prove the statement in §7 that the dielectric constant of any body exceeds unity, i.e. the dielectric susceptibility
(«—1)/4z is positive. To show this, we must first show independently
that the total change in the free energy of a dielectric when it is placed in an
electric field is negative.t This can be done by the use of thermodynamic
perturbation theory, the change in the free energy of the body being regarded
as the result of a perturbation of its quantum energy levels by the electric
field. According to this theory we havet

1x 'Vamlgm—tn) 1 ——a—
F-F,= Pen 5 D2, go-go 3eE Pm PnP (14.2)

+ The change proportional to the square of the field is meant. It may be recalled that,
in pyroelectric bodies, the change in the free energy contains also a term linear in the field,
which is of no interest here.

t See Statistical Physics, §32, formulae (32.5), (32.6). The formulae given here differ
from those in Statistical Physics only in form.

64 Electrostatics of Dielectrics §15
Here E, are the unperturbed levels, Vmn the matrix elements of the perturbing energy, and the bar denotes a statistical averaging with respect to the
Gibbs distribution wy = exp {((Fo—En©)/kT}.

The term Van in formula (14.2), which is linear in the field, is zero except
in pyroelectric bodies. The quadratic change in the free energy, which is of
interest here, is given by the remaining terms. It is evident from the form
in which they are written here that they are negative.

If we formally consider the change in the free energy as the result of a
gradual change in the dielectric constant of the body from 1 to a given value
«, it follows from formula (14.1) that #—Fo is negative only if « > 1.
This completes the proof.

In the same way we can prove the inequalities « > 1 for the principal
values of the tensor ¢;; in an anisotropic dielectric medium. To do so, it is
evidently sufficient to consider the energy of a field parallel to each of the
three principal axes in turn.

The total free energy is diminished, in particular, when any charge is
brought up to a dielectric body from infinity (a process which may be
regarded as an increase of ¢ in a certain volume of the field round the charge).
In order to conclude from this that any charge is attracted to a dielectric,
we should, strictly speaking, prove also that F cannot attain a minimum for
any finite distance between the charge and the body. We shall not pause
here to prove this statement, especially as the presence of an attractive
force between a charge and a dielectric may be regarded as a fairly evident
consequence of the interaction between the charge and the dipole moment of
the dielectric, which it polarises.

We can deduce immediately from formula (14.1) the direction of motion
of a dielectric body in an almost uniform electric field, i.e. one which may
be regarded as uniform over the dimensions of the body. In this case E?
is taken outside the integral, and the difference F —Fo is a negative quantity,
proportional to E?. In order to take a position in which its free energy is a
minimum, the body will therefore move in the direction of E increasing.

## Section §15: Electric forces in a fluid dielectric

The problem of calculating the forces (called ponderomotive forces) which
act on a dielectric in an arbitrary non-uniform electric field is fairly complicated and requires separate consideration for fluids (liquids or gases) and
for solids. We shall take first the simpler case, that of fluid dielectrics. We
denote by fdV the force on a volume element dV, and call the vector f the
force density.

It is well known that the forces acting on any finite volume in a body can
be reduced to forces applied to the surface of that volume.t+ This is a consequence of the law of conservation of momentum. The force acting on the

+ See Theory of Elasticity, §2, Pergamon Press, London, 1959.

1
§5 Electric forces in a fluid dielectric 65
matter in a volume dV is the change in its momentum per unit time. This
change must be equal to the amount of momentum entering the volume
through its surface per unit time. If we denote the momentum flux tensor
by —o, then
frav . peas (15.1)
where the integration on the right is over the surface of the volume V. The
tensor oi is called the stress tensor. It is evident that oidfe = oimmedf is
the ith component of the force on a surface element df (n being a unit vector
along the normal to the surface outwards from the volume under consideration).

Similarly, the total torque acting on a given volume also reduces to a
surface integral, by virtue of the law of conservation of angular momentum.
This reduction is possible because of the symmetry of the stress tensor
(ou = oxi), Which thus expresses the conservation law mentioned.

On transforming the surface integral in (15.1) into a volume integral, we
obtain f fidV = J (Gou/axx)dV, whence, since the volume of integration is
arbitrary,

Si = Ooi] Oxx. (15.2)
This is a well-known formula giving the body forces in terms of the stress
tensor.

Let us now calculate the stress tensor. Any small region of the surface
may be regarded as plane, and the properties of the body and the electric
field near it as uniform. Hence, to simplify the derivation, we can with no
loss of generality consider a plane-parallel layer of material (of thickness h
and uniform composition, density and temperature) in an electric field
which is uniform but whose direction is arbitrary.t This field may be
imagined to be due to conducting planes, bearing appropriate charge distributions, applied to the surfaces of the layer.

Following the general method for determining forces, we subject one of
the conducting planes (the upper one, say) to a virtual translation over an
infinitesimal distance &, whose direction is arbitrary and need not be that of
the normal n. We shall suppose that the potential of the conductor remains
unchanged at every point, and that the homogeneous deformation of the
dielectric layer, resulting from the translation, is isothermal.

A force —oixn is exerted by the layer on unit area of the surface. In the
virtual displacement this force does work —omzf;. ‘The work done in an
isothermal deformation at constant potential is equal to the decrease in f FdV,
ice. in AF per unit surface area. Thus

outine = SAF) = hdF + Fh. (15.3)

+ We thus ignore any terms in the stress tensor depending on the gradients of temperatare, field, etc. These terms, however, are vanishingly small in comparison with terms which
do not contain derivatives, in the same way as any terms containing derivatives which might

appear in the relation between D and E.

66 Electrostatics of Dielectrics §15
The thermodynamic quantities for the fluid depend (for given temperature and field) only on its density; deformations which do not change the
density (i.e. pure shears) do not affect the thermodynamic state. We can
therefore write for an isothermal variation 5F in a fluid
oF oF
BP = (=) -3E+(=) Bp
2E/r,, op /x,r
ae ( a) 3 (15.4)
~ an Vapler” :
The change in the density of the layer is related to the change in its thickness by 5p = —pdh/h. The variation of the field is calculated as follows.
At a given point in space (with radius vector r) there appears matter which
was originally at r—u, where u is the particle displacement vector in the
layer. Since, under the conditions stated (homogeneous deformation, and
constant potential on the conducting planes), each particle carries its potential with it, the change in the potential at a given point in space is 5¢
= ¢(r—u)—¢(r) = —u-grad ¢ = u-E, where E is the uniform field in the
undeformed layer. Since the deformation is homogeneous, however, we
have
u = 2t/h, (15.5)
where 2 is the distance from the lower surface. Hence the variation of the
field is
8E = —n(E-&)/h. (15.6)
Substituting the above expressions in (15.4) and using also the fact that
5h = €, = E-n, we obtain
1 oF
owkine = 7-(n-D)E-E)—E-np—_+E-nF
4a ép
E:D, oF
= {pp 54.4 FS, | .
{ trap et ne fame.
Hence we have finally the tollowing expression for the stress tensor:
ow = [F—p(aF/dp) 2,7 ]8ie+ ExDy/ 4a. (15.7)
In isotropic media, which are those here considered, E and D are parallel.
Hence E;D; = E,D;, and the tensor (15.7) is symmetrical, as it should be.
If the linear relation D = cE holds, then
F = Fo(p, T)— <E2/8a; (15.8)
see (10.16). Fo is the free energy per unit volume in the absence of the field.
|

§15 Electric forces in a fluid dielectric 67
According to a well-known thermodynamic relation, the derivative of the free
energy per unit mass with respect to the specific volume is the pressure:
a /F OF
[aaie) la Cp)”
a(1/p)\ p Ir ap Ir
po = po(p,T) is the pressure which would be found in the medium in the
absence of a field and for given values of p and 7. Hence, substituting (15.8)
in (15.7), we have
E2 de cEiEx
a T)8i%——|<«-—p{—) \Se+——. 15.9
ou = —polp, T)dix =I (=),] 7 (15.9)
In a vacuum, this expression becomes the familiar Maxwell stress tensor of
the electric field:t
ote = (EE —2ES;x)/47.

The forces exerted on the surface of separation by two adjoining media
must be equal and opposite: oinp = —o'sn's, where the quantities with
and without the prime refer to the two media. The normal vectors n and
n’ are in opposite directions, so that

Ou = OEM. (15.10)

At the boundary of two isotropic media the condition of equality of the

tangential forces is satisfied identically. For, substituting (15.7) in (15.10)

and taking the tangential component, we obtain E,D, = E’;D'y. This equa
tion is satisfied by virtue of the boundary conditions of continuity on E;

and Dn. The condition of equality of the normal forces is, however, a
non-trivial condition on the pressure difference between the two media.

For example, let us consider a boundary between a liquid and the atmosphere (for which we can put «= 1). Denoting by a prime quantities
pertaining to the atmosphere, and using formula (15.9) for oi, we have

E? (de €
= ple, T4505) + (Ea BA)
80 \ap/7 80
1
= Pain + 5 (B'n? — E').
Using the boundary conditions E; = E's, Dn = «En = D'n = E'n, we can
rewrite this equation as
pE®/de\ «—1
Po(p, T)—Ppatm = (5) ———(cEn? + E). (15.11)
82 \ap/p = 80
This relation is to be taken as determining the density p of the liquid near
its surface from the electric field in it.
ast ape Classical Theory of Fides, §4-8, Addison-Wesley Press, Cambridge (Mass.),

68 Electrostatics of Dielectrics §15

Let us now determine the body forces acting in a dielectric medium.
Differentiating (15.9) in accordance with (15.2) gives

a E? (de FE? ⟨e⟩ 1 é é
= >—|-potspl—-) | -s-=— t+] —$¢-—F2+—(EDy)}.
f Ong [ be P(e 82 x tal Lary ¥ Bax’ i »|
On using the equation div D = @Dx/@xx = 0, the expression in the brackets
in the last term can be reduced to
OEx OE; OE, dE;
—Ey—+Dy— = —D, (--5-)
ee be Oa "Vax Op
which is zero, since curl E = 0. Thus we have
1 de E2
f = —grad po(p, 7) +—grad| BYp(—) |-xeraa cm (15.12)
8a op/7\ 80

If the dielectric contains extraneous charges of density pex, the force f
contains a further term E div D/4z, or, since div D = 4zpex,

PexE; (15.13)
however, it should not be supposed that this result is obvious (cf. §16,
Problem 3).

In a gas, as already mentioned in §7, we can assume the difference «—1
to be proportional to the density. Then pd«/8p = «—1, and formula (15.12)
takes the simpler form

-1
f= ~ grad po+ {grad B®. (15.14)

Formula (15.12) is valid for media of both uniform and non-uniform
composition. In the latter case ¢ is a function not only of p and T but also
of the concentration of the mixture, which varies through the medium. In
a body of uniform composition, on the other hand, « is a function only of p
and T, and grad ¢ can be written as

grade = (dc/0T), grad T+ (d«/dp)r grad p.
Then (15.12) becomes
f d po(p, T) + a[z =) | (+) a7. (15.15)
=- 5 —gra —) |-—(—) eradT. 5
grad pulp, 7)+£-arad[2°(=*) | 5 ( 55 cc
Tf the temperature also is constant through the body, the third term on the
right is zero, and in the first term grad pp can be replaced by p grad fp, in
accordance with the thermodynamic identity for the chemical potential in
the absence of a field, pdf = dpo—SodT. Thus
E2/d¢
f = —pgrad [»-=(<) |: (15.16)
80r\ p/r.
|

§16 Electric forces in solids 69
The expression in the brackets is just the chemical potential £ in an electric
field (see (10.18)), and therefore f = —p grad ¢.

In particular, the condition of mechanical equilibrium f = 0 is, for constant temperature,

. € = So—(E?/82)(e/2p)r = constant, (15.17)
in accordance with the thermodynamic condition of equilibrium.t This
condition can usually be written still more simply. The change in density
of the medium due to the field is proportional to E?. Hence, if the medium
is of uniform density in the absence of the field, we can put p = constant in
the last two terms in (15.15) when the field is present; an allowance for the
change in p is beyond the accuracy of formulae which assume the linear
relation D= cE. Then, equating to zero f from (15.15), we obtain the
equilibrium condition at constant temperature in the form

Po(p, T)—(pE?/8m)(d«/0p)r = constant, (15.18)
which differs from (15.17) in that { is replaced by fo/p.

## Section §16: Electric forces in solids

The dielectric properties of a solid body change not only when its density
changes (as with liquids) but also under deformations (pure shears) which
do not affect the density. Let us first consider bodies which are isotropic in
the absence of the field. In general, the deformed body is no longer isotropic; in consequence, its dielectric properties also become anisotropic,
and the scalar dielectric permeability ¢ is replaced by the dielectric tensor
tk.

| The state of a slightly deformed body is described by the strain tensor
1 ( an =)
ux = >(>—-+5—}>
a) Oxy — Oxy
| where u(x,y,2) is the displacement vector for points in the body. Since these
quantities are small, only the first-order terms in 1% need be retained in the
variation of the components «. Accordingly, we represent the dielectric
tensor of the deformed body as
ete = odie t aitix + aouadix. (16.1)
Here ¢p is the dielectric permeability of the undeformed body, and the other
two terms, which contain the scalar constants aj, dz, form the most general
tensor of rank two which can be constructed linearly from the components
tik.

Let us now see where the derivation given in §15 must be modified.
Since, in a solid body, # depends on all the components of the strain tensor,
we must replace (15.4) by $F = —D-8E/4a+(aF/duy)5uye. For the virtual

+ See Statistical Physics, §25.

70 Electrostatics of Dielectrics §16
displacement considered, the vector u is given by formula (15.5), so that the
strain tensor is wx = (e+ xmi)/2h. Substituting this in 8f and using the
symmetry of the tensor uj, and therefore of the derivatives 0F/duix, we
obtain

8F = —D-5E/4r+ (€ime/h)OF du. (16.2)
It is now evident that we find, instead of (15.7), the following expression for
the stress tensor:t

oun = FSi, + (OF Cux)r e+ EiDp/4n. (16.3)

Formula (16.3) is valid whatever the relation between D and E. For a
body which is neither pyroelectric nor piezoelectric, so that Dj = eixEx,
F is given by formula (13.4) and the required derivatives are OF/duix
= OF o/ Ou, —(a1E:Ex + a2E*5;x)/87. We then put e% = €o5ix everywhere in
(16.3) and obtain the following formula for the stress tensor:

oie = 0 ppt (eo — a1) ErEx| 8a — (co + a2) E°Six/ 87. (16.4)
oz is the stress tensor in the absence of an electric field, determined by the
moduli of rigidity and compression according to the ordinary formulae of
the theory of elasticity.

Let us now make similar calculations for anisotropic solids.t The necessary modification of the above argument is as follows. When the layer
undergoes a virtual deformation, its crystallographic axes are rotated, and
their orientation relative to the electric field is therefore changed. On account
of the anisotropy of the dielectric properties of the crystal, this leads to an
additional change in f not shown in (16.2). To calculate this change we
can equally well suppose that the crystal axes rotate through some angle 5p
relative to the field E, or that the field rotates through an angle —S¢ relative
to the axes, and the latter approach is the more convenient.

Thus the variation of the field (15.6) considered above must be augmented
by the change in E on rotation through an angle —S@: SE = —n(E-8)/h—
—dxE. The angle S@ is related to the displacement vector u in the
deformation by 8 = } curl u; this equation is easily obtained by noticing
that, when the body rotates through an angle 86, its points are displaced by
u = 5xr. Substituting u from (15.5), we find 8 = curl 2€/2h = nx&/2h,

+ The quantity # in this formula, and in all preceding formulae, is the free energy per
unit volume. In the theory of elasticity, however, a somewhat different definition is usual?
the thermodynamic quantities are referred to the amount of matter contained in unit volume
of the undeformed body, which may after deformation occupy some other volume. It is
easy to go from one definition to the other by expressing the relative volume change in the
deformation in terms of the tensor uz; on account of the presence of the derivative with
respect to wx in (16.3), this must be done with allowance for second-order terms. As a
result, the first two terms on the right of (16.3) combine into one of the form @F/ dum, in
accordance with the usual formula of elasticity theory.

We shall see in §17 that the phenomenon of electrostriction in crystals may, for some
types of symmetry, differ markedly from that in isotropic bodies. Such crystals are said to
be piezoelectric. Here, however, we discuss only electrostriction in non-piezoelectric bodies.

§16 Electric forces in solids 71
and dE = —n(E-€)/h+Ex(nx&)/2h = —[n(E-E)+&(n-E)]/2h. The first
term in (16.2) becomes
1 1 1
——D-8E = ——[(n-D)(§-E -D)(n-E)] = —£inp (ED + ExD)).
ig D-BE = 5 [(a-D)G-B) + E-D\n-B)] = [fim AED + ED)
Hence we see that the product E;,D, in (16.3) must be replaced by the second
factor in the last expression:
oF 1
on = FSi +—+—(EDx+ ExD)). (16.5)
Ou 8a
This expression is symmetrical in the suffixes 7 and k, as it should be.

The expression (16.1) for the dielectric tensor, involving two scalar con
stants, must be replaced in the case of a dielectric crystal by

ie = Og + Armttm, (16.6)
where ajxtm is a constant tensor of rank four, symmetrical with respect to
the pairs of suffixes 7, k and J, m (but not with respect to an interchange of
these pairs). The number of independent non-zero components of this
tensor depends on the crystal class.

We shall not pause to write out here the formula for the stress tensor
(analogous to (16.4)) which is obtained by using (16.6).

The formulae which we have obtained give the stresses inside a solid dielectric. They are not needed, however, if we wish to determine the total
force F or the total torque K exerted on the body by the external field. Let
us consider a body immersed in a fluid medium and kept at rest there.
The total force on it is equal to the integral $ ojmpdf, taken over the surface.
Since the force oj is continuous, it does not matter whether this integral
is calculated from the values of oi given by (16.4) or from formula (15.9),
which relates to the medium surrounding the body. Let us suppose that
this medium is in mechanical and thermal equilibrium. Then the calculation is further simplified if we use the condition of equilibrium (15.18).
From this condition, part of the stress tensor (15.9) is constant through the
body, being a uniform compressing or expanding pressure and making no
contribution to the total force F and torque K acting on the body. These can
therefore be calculated by writing oj as

cin = (€/40)(EEx— $B) (16.7)
simply, where E is the field in the fluid and ¢ its dielectric permeability; this
expression differs only by a factor « from the Maxwell stress tensor of the
electric field in a vacuum. Thus
Fe= (</4z)$ [E(n-E)—}E2n] df, (16.8)
K = (</4z)$ [x x E(n-E)—4Er x n] df. (16.9)

72 Electrostatics of Dielectrics §16
It may also be noted that, since the fluid is in equilibrium, we can take
these integrals over any closed surface which surrounds the body in question
(but, of course, does not enclose any of the charged bodies which are sources
of the field).
* The calculation of the total force on a dielectric in an electric field in a
vacuum can also be approached in another way by expressing this force,
not in terms of the actual field, but in terms of the field © which would be
produced by the given sources in the absence of the dielectric; this is the
“external field” in which the body is placed. Here it is assumed that the
distribution of charges producing the field is unchanged when the body is
brought in. This condition may not be fulfilled in practice—for example, if
the charges are distributed over the surface of an extended conductor and the
dielectric is brought to a finite distance from it.

In a virtual translation of the body over an infinitesimal distance u, the
total free energy of the body varies, according to (11.3), by SF = — fP-8EdV,
where 5& = E(r+u)—C(r) = (u-grad)€ is the change in the field at any
given point in the body. Since u = constant and curl € = 0, we have
P-(u-grad)¢ = P.grad(u-€) = u-(P-grad)€, so that

8F = —u:- |(P-grad)€ dV.
But 5% = —u-F, and we therefore have for the required forcet
F = { (P-grad)€dV. (16.10)

Similarly, the total torque on the body can be determined. We shall not
go through the calculation, but merely give the result:

K = [ Px€dV+/rx(P-grad)edV. (16.11)

In an almost uniform field, which may be regarded as constant over the
dimensions of the body, formula (16.10) gives to a first approximation

F= (f PdV-grad)& = (P-grad)&, (16.12)
where # is the total dipole moment of the polarised dielectric; this result,
of course, could have been obtained by direct differentiation of F from

. (11.8). In formula (16.11) we neglect the second term in the first approximation and reach the natural conclusion that
K = Pxe. (16.13)

+ It should be emphasised, however, that the integrand in (16.10) cannot be interpreted
as the force density. ‘The reason is that the local forces in the dielectric arise not only from
the field € but also from the internal fields which, by Newton's third law, contribute nothing |
to the total force, though they modify the distribution of forces over the volume of the body.

§17 Piezoelectrics 73
PROBLEMS

ProsteM 1. A dielectric sphere of radius a in a uniform external field € is cut in half by a
plane perpendicular to the field. Determine the force of attraction between the hemispheres.

Sowution. We imagine the hemispheres separated by an infinitely narrow slit and determine the force from formula (16.8) with ¢ = 1, integrating over the surface of a hemisphere ;
Eis the field in the vacuum near the surface. According to (8.2) the field E‘ inside the sphere
is uniform and equal to 3G/(2-+«), where ¢ is the dielectric constant of the sphere. ‘The field
in the slit is perpendicular to the surface and is E = D( = 3¢€/(2+<). On the outer surface
of the sphere we have

3e 3
= DO, = 6, = EM = ———_ Esin 8,
Ey = Diy = TE cos Eq = Eg ay Ein
where 0 is the angle between the radius vector and the direction of @. A calculation of the
integral gives an attractive forcet
F = e—1)? a? G2/16(e-+2)%,

ProsiEM 2. Determine the change in shape of a dielectric sphere in a uniform external
electric field.

Souution. As in §5, Problem 4. In determining the change in shape, we assume the
volume of the sphere to be unchanged.} The elastic part of the free energy is given by the
same expression as in §5, Problem 4. The electric part is given by

Vo 1
-1?-€=—-—_—_“____@
a 82 1+n(€)—~1) and the dielectric permeability in the x-direction is, by (16.1), €) = eo+a1uzz = eo+
-+$ai(uzz—uyy) = €0-+$a1(a—b)/R. From the condition that the total free energy is a
minimum we find
| a—b 9G? (co—1)?+5a1
R 40m (co+2)® *
For 9 > © this tends to the value for a conducting sphere.

PropLeM 3. Determine the body forces in an isotropic solid dielectric, assumed homogeneous, when extraneous charges are present in it.

SoLvTION. Assuming ¢o, ai, a2 constant and using the equations curl E = 0, divD &
codiv E = 4zpex, we have from (16.4)

Bou 20%, 1 Et ( a
=e - See 4+ (1-) per Es.
Fa ae Ta emt a + ia) oie

## Section §17: Piezoelectrics

The internal stresses which occur in an isotropic dielectric in an electric
field are proportional to the square of the field. The effect is similar in
crystals belonging to some of the crystal classes. For certain types of
symmetry, however, the electrostriction properties of the crystals are quite
different. The internal stresses in these piezoelectric bodies resulting from

+ It is by chance that, in the limit ¢ > 00, this expression tends to the result obtained
in §5, Problem 3, for a conducting sphere (indeed, the forces are in opposite directions).
‘The two cases are evidently not physically equivalent, because there is no field in the slit
between two conducting hemispheres at the same potential, whereas in this problem there
is a field in the slit.

t The change in volume is determined in §12, Problem 1.

vi Electrostatics of Dielectrics §17
an electric field are proportional to the field itself. The converse effect also
occurs: the deformation of a piezoelectric is accompanied by the appearance
in it of a field proportional to the deformation.

Since in a piezoelectric only the principal (linear) effect is of interest, we
can neglect the terms quadratic in the field in the general formula (16.5).
Then on = F8i,+(0F/Ousz)7z- In this section we shall use the thermodynamic quantities referred to the matter in unit volume of the undeformed
body (see the first footnote to §16). Taking F in this sense, we have simply

on = (OF Oun)re, (17.1)
Accordingly, the thermodynamic relation for the differential df is
dF = —SdT+ c%duy—D- dE/47. (17.2)
The following remark should be made concerning the last term. In the form
given here, this term (taken from (10.9)) pertains, strictly speaking, to unit
volume of the deformed body. By ignoring this fact, we commit an error
which, in the case of a piezoelectric, is of a higher order of smallness
than the remaining terms in (17.2).

The independent variables in (17.2) include the components of the tensor
ux. It is sometimes convenient to use instead the components og. To do so,
we must introduce the thermodynamic potential, defined as

® = F-ugon. (17.3)
For the differential of this quantity we have
d@ = —SdT—uy doy —D- dE/4z. (17.4)
It must be emphasised that the use of the thermodynamic potential © in
electrodynamics in accordance with formulae (17.3) and (17.4) rests on
the validity of (17.1) and so is possible only for piezoelectric bodies.

Having thus defined the necessary thermodynamic quantities, let us now
ascertain the piezoelectric properties of crystals. If oy and Ey are taken as
independent variables, the induction D must be regarded as a function of
them, and an expansion of this function must include the linear terms in
them. The linear terms in the expansion of the components of a vector in
powers of the components of a tensor of rank two can be written, in the
most general case, as 47ryiz1 o¢1, Where the constants 7:1 form a tensor of
rank three, and the factor 47 is introduced for convenience. Since the tensor |
ox, is symmetrical, it is clear that the tensor i. may also be supposed to
have the symmetry property

Yokl = Yidke (17.5)
For clarity we separate the symmetrical suffixes from the remaining one by
acomma. We call yj x1 the piezoelectric tensor. If it is known, the piezoelectric properties of the crystal are entirely determined.

§17 Piezoelectrics 75
Adding the piezoelectric terms to the expression (13.1) for the electric
induction in the crystal, we have
Dy = Dott «xEn + 4ryinon- (17.6)
Corresponding additional terms appear in the thermodynamic quantities.
The thermodynamic potential of a non-piezoelectric crystal in the absence of a
field is & = © = ©y—4yeImotncrm, where Qo pertains to the undeformed
body, and the second term is the ordinary elastic energy, determined by
the elastic constant tensor jizim.t For a piezoelectric we have
© = Oo—dytermonorm — «nF Ex/8 — EyDoi[40— yinE vou. (17.7)
The form of the last three terms is given by the fact that the derivatives of ®
with respect to E; (for given temperature and internal stresses), found from
the relation D; = —4786/@E;, must accord with (17.6).
Knowing ®, we can obtain from (17.4) a formula giving the strain tensor
in terms of the stresses oy, and the field E:
te = —(88/2ou) 728 = parimormt vKEr. (17.8)
It should be mentioned that to regard the quantities jizim and ei for a
piezoelectric as elastic constants and dielectric permeability is to some extent
conventional. With the definitions used here, they give respectively the
strains as functions of the elastic stresses for a given field, and the induction
as a function of the field for given stresses. If, however, the deformation
occurs with a given value of the induction, or we consider the induction as a
function of the field for given strains, the elastic constants and the dielectric
permeability will be represented by other quantities, which can be expressed
as somewhat complex functions of the components of the tensors 1, ¢ and y.
The field in a piezoelectric body must be determined together with its
deformation, leading to a problem in both electrostatics and elasticity
theory. We must seek a simultaneous solution of the electrostatic equations
divD=0, curlE=0, (17.9)
with D given by (17.6), and the equations of elastic equilibrium
dou/dxy = 0, (17.10)
with the appropriate boundary conditions at the surface of the body and use
of the relation (17.8) between oj and the strains. In general this problem is
very complex.
t The tensor pixim determines the relation between stress and strain:
ik = — 90/20 = pHkimoimIn Theory of Elasticity, $10, the converse relation ow = Aiimuim is used. It is evident that
the symmetry properties of the tensor jitim are exactly the same as those of \ikim.
‘The free energy F contains the elastic energy with the plus sign:
Fe = d\gimusttim.
‘The thermodynamic potential is obtained from F by subtracting ouu, and so
er = Fer — ome = — Aarmeettim = — pteimoseorm.

76 Electrostatics of Dielectrics §17

The problem is much simplified for a body of ellipsoidal form with a free
surface (i.e. one subject to no external mechanical forces). In this case
(§8), the field inside the body is uniform; the deformation is therefore
homogeneous, and the elastic stresses oi = 0. ,

Finally, let us consider which types of crystal symmetry allow the existence
of piezoelectricity; in other words, what are the restrictions imposed on the
components of the tensor y;42 by the symmetry conditions. In general, this
tensor (which is symmetrical in the suffixes k and /) has 18 independent nonzero components, but in reality the number of independent components is
usually much smaller.

In all symmetry transformations of a given crystal, the components of the
tensor i,xz must remain unaltered in value. Hence it follows at once that
no piezoelectric body can have a centre of symmetry or, in particular, be
isotropic. For, on reflection in the centre (i.e. change of sign of all three coordinates), the components of a tensor of rank three change sign.

Of the 32 crystal classes, only 20 allow piezoelectricity. These comprise
the ten enumerated in §13 as allowing pyroelectricity (all pyroelectrics are
also piezoelectrics) and the ten following classes:

rhombic system: Dz

tetragonal system: D4, Dea, Sa
rhombohedral system: Dg
hexagonal system: De, C3n, Dan
cubic system: T, Ta.

The non-zero components of the piezoelectric tensor for each class are
given in the following Problems.

PROBLEMS

Prosiem 1, Determine the non-zero components of the tensor 7,4 for non-pyroelectric
crystal classes which allow piezoelectricity.

SouuTION. ‘The class Ds has three mutually perpendicular axes of symmetry of the second
order, which we take as the axes of x, y and z. Rotations through 180° about these axes
change the sign of two out of the three co-ordinates. Since the components 74,11 are trans~
formed as the products xine, the only non-zero components are those with three different
suffixes: yzyz Y22y Yv.er. (The other non-zero components are equal to these, since
‘Yi.41 = yik.) Accordingly, the piezoelectric part of the thermodynamic potential ist

Opie = —2Ayeye Exoyst Yas Eyoest ys,ay Exozy). (i)

"The class Dea is obtained by adding to the axes of class Dz two planes of symmetry passing
through one axis (the z-axis, say) and bisecting the angles between the other two. Reflection
in one of these planes gives the transformation x > y, y > x, # > z. Hence the components
int which differ by interchange of x and y must be equal, so that only two out of the three
coefficients in (1) are now independent: yz,2y, Yee = Yu.ze
+ To avoid misunderstanding it should be recalled that, if we calculate the components
of the strain tensor wx by direct differentiation of the actual expression for ® with respect
to ov, the derivatives with respect to components oi with i # k give twice the correspond~
ing components wiz; see Theory of Elasticity, §10, Problem, footnote.

§17 Piezoelectrics 77

The class T is obtained from the class De by adding four diagonal axes of symmetry of
the third order, rotations about which effect a cyclic permutation of x, y, 2, e.g. x > 3,
yx, zy. Hence all three coefficients in (1) are equal: yz,yz = Yzav — Yv.zz. ‘The same
result is obtained for the cubic class Ta.

‘The class D4 has one axis of symmetry of the fourth order (the z-axis, say) and four of the
second order lying in the xy-plane. Here the symmetry elements of the class Dz are supplemented by a rotation through 90° about the z-axis, i.e. the transformation x > y, y > —x,
z-» z. Consequently, one of the coefficients in (1) must be zero (yz,zy = —Yeve = —Ys,ay
= 0), and the other two are equal, but opposite in sign: yz,yz = —Yy.2z. The same result is
obtained for the class Dg.

The class $4 includes the transformations xy, y—> —x, z—> —z and x —> —x,
y>—y, #2. The non-zero components are Yz.2y, Yee = Yue, Yers = —Yevy
‘2,22 = —Yy,zy. One of these can be made to vanish by a suitable choice of the x and y axes.

The class Ds has one axis of symmetry of the third order (the z-axis, say), and three of the
second order lying in the xy-plane; let one of these be the x-axis. To find the restrictions
imposed by the presence of a third-order axis, we make a formal transformation by introducing
the complex “co-ordinates” £ = x+iy, 7 = x—iy; the co-ordinate z remains unchanged.
‘We must also transform the tensor 71,t to these new co-ordinates, in which the suffixes take
the values £, 7, 2. In a rotation through 120° about the z-axis these co-ordinates undergo
the transformation £ + £e®*6'3, » > ye-2"0/3, x > =. ‘The only components of the tensor ¥4,41
which remain unchanged and so may be different from zero are ying, Ym.2¢> Yéséns YEéé> Yn
and 72,22. A rotation through 180° about the x-axis gives the transformation x > x,y > —¥,
a> —3, or € + 9,7 > £2 > —25 Yong and 72,22 Change sign and so must be zero, while the
remaining components listed above are mutually transformed in pairs, giving y).2¢ = —Y¢,2n»
Y€4€ = Ynm- In order to write an expression for pie, we must form the sum —y1,eZon1,
in’ which the suffixes take the values , 7, 2:

Dyte = —2yiqy2e (Ey 70g — Ee om) —e,8¢ (Egoee + Eq om)
Here the components E; and oi in the co-ordinates ¢, 7, x must also be expressed in terms of
those in the original co-ordinates x, y, z. This is easily done by using the fact that the components of a tensor are transformed as the products of the corresponding co-ordinates.
Hence, for example, from £# = x?—y?- 2ixy, we have oge = o2z—oyy+2iczy. The result is
pie = 2a(Eyors—Ezory)+b[2Ey ory —Ex(oze— ovy)], Q)
where a = 2iyy,2¢ and b = 2y¢,g¢ are real constants. The relations between the components

yixt in the co-ordinates x, y, z are, as we see from (2),t

Yass = Yay SO, Yysy = —Ye,2x = Yew =

‘The class Don is obtained from the class Ds by adding a plane of symmetry (the xy-plane)
perpendicular to the axis of the third order. Reflection in this plane changes the sign of z,
and so ¥,2¢ = 0, so that only the term with the coefficient b remains in (2).

‘The class Cg, has an axis of the third order and a plane of symmetry perpendicular to it.
Reflection in this plane changes the sign of 2, and so all components 1,1 whose suffixes

contain z an odd number of times must be zero. Taking into account also the restrictions
derived above which are imposed by the third-order axis of symmetry, we find that only the
two components ¥),qn and yg,¢¢ are not zero. These quantities must be complex conjugates
in order that should be real. Putting 2y.m = a-+ib, 2y¢,¢¢ = a—ib, we find
D pe= a[2Ey oxy —Ex( os — oyy)] + 0[2Ezezy + Ey(oz2— yy)]. @)
Either a or b can be made to vanish by a suitable choice of the x and y axes.

Pros.em 2, The same as Problem 1, but for the crystal classes which allow pyroelectricity.

t In non-orthogonal co-ordinates such as £, 7, 2 the covariant and contravariant components of tensors must be distinguished. This should have been done in returning to the
original co-ordinates x, y, s. We avoid this necessity, however, by obtaining the required
relations between the components 71,4: in the co-ordinates x, y, = directly from the form

of the scalar combination (2).

73 Electrostatics of Dielectrics §17

SoLvTION. Let the z-axis be the axis of symmetry of the second, third, fourth or sixth
order, or in the class C, be perpendicular to the plane of symmetry. In the classes Cnv the
xz-plane is a plane of symmetry. By a suitable choice of axes three more components can be
made zero in the class Ci, and one component in the classes Cs, Cn
‘We give below for each class all the components 7i,é: which are not zero.

Class Ci: all yi,x.

Ce: all those in which the suffix z appears twice or not at all.

Covi Yana, Yeuys Ye 20) Yavtes Yuu

Cz: the same, together with yz,yz, Yu.2z) Yz.zy
Cari Y2,a2 = Yew, Ye,22) Yous = Yuya

C4: the same, together with yz,y2 = —Yv.22
Covi Y2,22) Ye,2e = Yuve Year = —Yeuy = —Yuawy Year = Yevye
Cs: the same, together with yzyz = —Yuem Yyze = —Yuwy = Yeaye
Covi Ye,22) Y2,20 = Yue Yeza = Yevys

Ce: the same, together with yz,ye = —Yy,z2
PROBLEM 3. Determine Young’s modulus (the coefficient of proportionality between the
extending stress and the relative extension) for a flat slab of a non-pyroelectric piezoelectric
in the following cases: (a) where the slab is stretched by the plates of a short-circuited
condenser, (b) where it is stretched by those of an uncharged condenser, (c) where it is
stretched parallel to its plane with no external field.

Soxurion. (a) In this case the field E inside the slab is zero. ‘The only non-zero component
of the tensor ow is the extending stress oze (the 2-axis being perpendicular to the slab).t
From (17.8) we have uzz = fizezzoez, whence Young’s modulus is E = 1/yzez2
(b) In this case we have in the slab Ey = Ey =0, Dz =0. From (17.6) and (17.8)
we have Dz = ¢e2E2+4myz,22022 = 0, use = Meze20z2+Y2,22E2. Eliminating Ez, we obtain
VE = peeee—Ayz,227ezz.

(c) In this case also, Ez = Ey = 0, Dz = 0, but the extension is along the x-axis, say.
Here we have Dz = ¢z2E2+4ayz,22022 = 0, uz = Perzz02c+7z,22Ez. Eliminating Ez,
we obtain 1/E = pzrez—4myezz"/er2.

ProBLEM 4. Obtain an equation for the velocity of sound in a piezoelectric medium.

Soxurion. In this problem it is more convenient to use wiz as the independent variables,
ns tead of oi. We write # in the form

i 1
F = Pot dducim wie tim — = ee Ee — — ExDovt Biot Eves,
8a 4n
where
Bice = —Duneer Yes
whence
our = OF | Que = Murmur BrteE.
‘The equations of motion from the theory of elasticity are
bon duim oEt
fig = = Nim '
on a car + Bios
where u is the displacement vector, related to ux by
au, Guy
wo = 3 ae + aa
‘The equation div D = 0 gives
aE a
cra" — 4nBoar = 0,
Ox xt
and the field can be expressed in terms of the field potential: E: = — 04/21, which takes
into account the equation curl E = 0.
+ It is not assumed to coincide with any particular crystallographic direction.

§18 Thermodynamic inequalities 79

Ina plane sound wave, u and ¢ are proportional to exp[i(k-r—wt)], and we find from the
above equations that

aug = Meimkekium —Br,ekekid,
eukikeh + 47 Bierkikeu = 0.
Eliminating $, we can write the condition of compatibility of the resulting equations for
uy as
]a®Six—Aseimhikm —427(Bi,mskikm)(Bp, okpka)/erekrka] = 0.
For any given direction of the wave vector k, this equation determines three phase velocities
of sound w/k, which are in general different. A characteristic property of a piezoelectric
medium is the involved relation between the velocity and direction of the wave.

## Section §18: Thermodynamic inequalities

According to the formulae of §10, the total free energy can be written as
the integral
F =[F(T,p,D)aV, (18.1)
taken over all space. We shall suppose that the function D(x, y, 2) which
appears in the integrand satisfies only the equation
divD =0 (18.2)
inside a dielectric and the condition
§ D- df = 4re (18.3)
on the surface of a conductor which carries a given charge. These equations
establish the relation between the field and its sources. Otherwise we regard
the function D(x, y, 2) as arbitrary, and in particular we do not require it to
satisfy the second field equation curl E = 0 (where E = 47@F/@D) or the
boundary condition ¢ = constant on the surface of a conductor. We shall
show that these equations can then be obtained from the condition that the
integral (18.1) is a minimum with respect to changes in the function
D(x, y, 2) which satisfy equations (18.2) and (18.3). It should be emphasised
| that the possibility of this derivation is not a priori evident, since the field
distributions which come into consideration in determining the minimum of
the integral (18.1) do not necessarily correspond to physically possible states
(because they do not satisfy all the field equations), whereas, in the thermodynamic condition that the free energy is a minimum, only the various
physically possible states are considered.

The problem of finding the minimum of the integral (18.1) with the
subsidiary conditions (18.2) and (18.3) is solved by Lagrange’s method of
multipliers, We multiply the variation of the condition (18.2) by some as
yet undetermined function —d/4m of the co-ordinates, and that of the

80 Electrostatics of Dielectrics §18
condition (18.3) by some undetermined constant ¢o/47, and then equate to
zero the sum of variations

al

forav-Z fe div ears $2 fen. df = 0.
In the first term we writet
8F = (aF/OD)z,,-8D = E-8D/47,
and the second can be integrated by parts: { ¢ div 5D dV = $¢3D-df—
— f8D-grad$dV. The result is
(B+ grad $)-SDdV + $(fo—9)8D- df = 0.

Hence we conclude that, throughout the volume, we must have E = —grad ¢
(and so curl E = 0), and on the surface of a conductor ¢ = $9 = constant.
These are the correct equations for the field, and the Lagrangian multiplier
¢ is its potential.

Similarly it can be shown that the equations for the electric induction are
obtained from the condition that the integral F= f F(T, p, E)dV is a minimum, in which the function E(x, y, z) is varied with the subsidiary conditions
E = —grad ¢ and ¢ = constant on the surface of a conductor. For

8# = [(F/oB)-dEAV=|D-grad 3$dV/4n
= $86 D- dff4n— [56 div DdV/4x = 0.
The first integral is zero because 5¢ = 0 on the surface, and from the second
we find the required equation div D = 0, since 5¢ is arbitrary in the volume.

If the body is not in an external electric field (in particular, if there are no
charged conductors), it may be possible to formulate the condition of thermodynamic equilibrium as the condition that the total free energy (18.1) has
an absolute (unconditional) minimum. This amounts to the condition that the
free energy density F is a minimum as a function of the independent variable
D: aF/aD = E/4n = 0, ie. the field must be zero in all space. If it is possible to find a distribution of the induction such that div D = 0, this state
will correspond to thermodynamic equilibrium.t

+ The free energy is the minimum for a given temperature. The variation is with respect
to two independent quantities D and p. Here we are interested only in the result of varying
with respect to D. The variation of the integral (18.1) with respect to density (with the
subsidiary condition of constant mass, i.e. constant Jp di”) gives one of the usual conditions
of thermal equilibrium, namely the constancy of the chemical potential {.

t Here we are considering bodies in which D need not be zero even if E = 0 (see §19).
Otherwise we have simply the trivial result E = D = 0 in all space.

§18 Thermodynamic inequalities . 81

Equating to zero the first variation of the free energy, we find necessary but
not sufficient conditions for this energy to be a minimum. The calculation
of the sufficient conditions requires a discussion of the second variation.
These conditions take the form of certain inequalities (called thermodynamic
inequalities) and are the conditions which ensure the stability of the state of
the body.

When there is a linear relation between D and E, the situation is much
simplified, and the thermodynamic inequality of interest here (relating to
the dielectric properties of the body) becomes evident. The total free energy
is Fot+ [(D?/8me)dV. It is clear that this can have a minimum only if *
« > 0, since otherwise the integral could be made to take any large negative
value by making D? large enough. Thus in this case nothing new is learnt,
since we know already that the dielectric permeability must in fact be not
only positive but greater than unity (see §14).

In the general case of an arbitrary relation between D and E, however, it
is necessary to consider the second variation of the integral (18.1), and to
vary simultaneously both D and p (leaving only the temperature constant).
Inan isotropic body, F(T, p, D) depends only on the magnitude of the vector
D, but its three components vary independently. We take the direction of
the vector D before variation as the z-axis. Then the change in the magnitude of D is given in terms of the changes in its components, as far as the
second-order terms, by 8D = 8Dz+(8Dz)?/2D+(8Dy)?/2D. The first and
second variations of the integral (18.1) are both contained in the expression

oF oF 1 @F @F 1@F
—8D +—4p + - ——(8D)?+ 8D 8p += 8) par.
ie +98 5 apa OOM + apap he +3 FeaP)
Substituting 8D and collecting the second-order terms, we find the second
variation
Sap aplOm* 8Dy)?] dV.
sp apa + ODy)81aV +
1 @F er 12F
+ |{-—(8D,)?++ ——8D Sp += (8p)?} dV. 18.
Sea + apap Pee pally (18.4)
‘These two terms are independent. The first is positive if (1/D)@F/@D > 0.
But aF/@D = E/4m, so that the derivative @F/@D is positive or negative
according as the vectors D and E are in the same or opposite directions.
Thus these vectors must be in the same direction.
The conditions for the second term in (18.4) to be positive are
@F/dp? > 0, (18.5)
OF oF ( ar ' 0 18.6
——~-|=—) > 0. 5.
dp? 2D? \ apaD, (18.6)
t See Statistical Physics, §21.

82 Electrostatics of Dielectrics §18
Since aF/dp = {, 0F/@D = E/4r, the first of these gives
(8¢/ép)p,r > 0, (18.7)
and the second can be rewritten as a Jacobian:
aak[@D, Fle) _ 1 2D. 4
aD.) tn Dip)
Changing from the variables D, p to D, £, we have
OES) HE, £) aD,o) _ (3) (=) +0:
D,p) aD, £) {D,p) \aD/,\ep/p~ —”
by (18.7), this gives
(2E/8D),.7 > 0. (18.8)
Thus we have derived the required thermodynamic inequalities. In the
absence of a field, the inequality (18.7) becomes the usual condition that the
isothermal compressibility is positive: (2p/@p)r > 0.+ The inequality (18.8)
gives « > 0, since when E -> 0 the induction D > cE.
Of the two inequalities (18.5), (18.6) the latter is the stronger; it may be
violated while the first is not, whereas the reverse is impossible. The equation
er er ( er y BD _ 4
p2 8D? \apaD) ~—-A(D, p)
corresponds to what’ is called the critical state.t This condition is more
conveniently written in a different form by multiplying it by the non-zero
factor aD, p)/A(E, p):
aE, H/O(E, p) = (8£/2p)z,r = 0. (18.9)
The determination of further conditions for the stability of the critical state
of matter requires a study of the third and fourth variations; we shall not
pause to do this, but simply give the results:
(&/0p2)z.r = 0, (18.10)
(23¢/0p%)z.7 > 0, (18.11)
in analogy with those found in the absence of an electric field.
+ It should be recalled that, in the absence of a field, { is the thermodynamic potential
of unit mass and, by the ordinary thermodynamic relations, its differential
al = dp/p — (S/p) aT,
so that (8£/8p)r = (1/p)(2p/2p)r. In the above derivation the second of the ordinary |
thermodynamic inequalities (that the specific heat is positive) is ignored.
T See Statistical Physics, §80.

§19 Ferroelectrics , 83
PROBLEM

Determine the displacement of the critical point of a dielectric substance in an electric
field.

SoLvrion. Substituting in (18.9) the expression for { from (10.18), we find (8f0/p)r—
—(E?/8n)(8%«/dp)r =0. For the chemical potential when E =0 we have (2%0/ap)r 7
= (1/p)(ap/ap)r (see the penultimate footnote to this section), where p = p(p, T) is the
equation of state in the absence of the field. Thus (ap/2p)r = (pE®/87)(2%«/dp*)r. When
there is no field, the critical point is given by the equation (2p/2p)r = 0, and if it is stable
we must also have (2*p/dp")r = 0. Hence

ep ap p
@, 2 Fptet Sear a SAT,
where AT and Ap are the displacements of the critical temperature and density (assumed to
be of the same order of smallness, which is confirmed by the result). The temperature
displacement is therefore
pE*/ Bey | op
arm Sol sear

‘The displacement of the critical pressure is Ap = (8p/2T),AT. To determine the displacement Ap, equation (18.10) must be used in a similar manner.

## Section §19: Ferroelectrics

The various crystalline modifications of a given substance may include
some which are pyroelectric and some which are not. If the change from
one to the other takes place by means of a second-order phase transition,
then near the transition point the substance has a number of unusual properties which distinguish it from ordinary pyroelectrics; these are called ferroelectric properties.

In an ordinary pyroelectric crystal, a change in the direction of the spontaneous polarisation involves a considerable reconstruction of the crystal

lattice. Even if the final result of this reconstruction is energetically favourable, its realisation may still be impossible because it would require the
surmounting of very high energy barriers.

In a ferroelectric body, however, the situation is quite different because,
near a second-order phase transition point (a Curie point), the arrangement
of the atoms in the crystal lattice of the pyroelectric phase is only comparatively little different from the arrangement in the non-pyroelectric lattice
(and so the spontaneous polarisation also is small). For this reason the change
in direction of the spontaneous polarisation here requires only a relatively
slight reconstruction of the lattice (a slight displacement of the atoms) and 5
can occur quite easily.

The actual nature of the ferroelectric properties of a body depends on its
crystal symmetry. The direction of the spontaneous polarisation of the pyroelectric phase (which we shall call the ferroelectric axis) is determined by the
structure of the non-pyroelectric phase beyond the Curie point. In some
cases it is uniquely determined, in the sense that the ferroelectric axis can

lie in only one, crystallographically determinate, direction; the direction of

84 Electrostatics of Dielectrics §19
the spontaneous polarisation is then determined apart from sign, since in the
non-pyroelectric phase the two opposite directions parallel to the ferroelectric axis must be entirely equivalent (otherwise this form of the crystal
would also be pyroelectric). In other cases, the symmetry of the nonpyroelectric phase may be such as to allow spontaneous polarisation in any
of several crystallographically equivalent directions. t

The quantitative theory of ferroelectricity can be developed in terms of
the general theory of second-order phase transitions;} this has been done
by V. L. Grnzpure (1945).

The basis of the following considerations will be the thermodynamic

. stability of states. From this point of view the transition is characterised by
the fact that, on one side of it, a state with D = 0 can be stable, but on the
other side any such state is unstable, and so there must be a non-zero induction even when the field E is zero. For definiteness, we shall suppose below
that the pyroelectric phase (D # 0) corresponds to temperatures T < ©
(where @ is the transition point), but it should be emphasised that this disposition of the phases, though the more usual, is not obligatory, and the
opposite case is also found in Nature.

Since our prime interest is in the dielectric properties of the substance, we
shall first suppose that there are no internal stresses in the body. To determine the stability conditions, we can start from the condition that the total
thermodynamic potential of the body is a minimum (for a given temperature
and zero stresses). As we have seen in §18, this reduces to the condition that
the second variation of the thermodynamic potential per unit volume ®
should be positive. For a state in which the induction is almost zero, the
second variation of ® is simply ®—@p = (1/87)e~1y.DiDr.

If we take the co-ordinate axes to be the principal axes of the tensor ex,
then

11,1 pe _
o-& = x(a? + Dit De ). (19.1)
The state with D = 0 satisfies the stability conditions (i.e. can correspond to
a minimum of ®) so long as all three coefficients 1/e“) are positive. Hence
the pyroelectric phase can be formed only when one of these three coeffi- |
cients changes sign. The point at which the second-order phase transition
takes place is determined by the vanishing of that coefficient.

} An instance of the first type is sodium potassium tartrate, whose non-pyroelectric
phase has a rhombic symmetry. The ferroelectric axis appears in it (at the Curie point)
in a completely definite crystallographic direction (one of the second-order axes), and the
lattice becomes monoclinic.

An instance of the second type is barium titanate. Its non-pyroelectric modification has
a cubic lattice, and any of the three cubic axes may become the ferroelectric axis. After the
spontaneous polarisation has appeared at the Curie point, these three directions, of course,
are no longer equivalent. ‘The ferroelectric axis becomes the only fourth-order axis, and the
lattice becomes tetragonal.

§ See Statistical Physics, Chapter XIV. The discussion here following, however, is not
based on the usual formulation.

§19 Ferroelectrics 85 :

The ferroelectric axis is then the one for which 1/e) is zero. Here various
cases can arise, depending on the symmetry of the non-pyroelectric phase. If
this symmetry is such that «@) ¢ <) % «®), only one of the coefficients
in (19.1) is zero, and the position of the ferroelectric axis is uniquely defined.
If <@) = ¢W) = ¢®) (for which the symmetry must be cubic), all three coefficients vanish simultaneously, and the ferroelectric axis may be in one of
several directions (see below). Finally, if the symmetry is such that «@)
= «) 4 ¢®), either one or two of the coefficients in (19.1) will vanish at
the transition point.

Let us consider first the case where the position of the ferroelectric axis, :
which we take as the z-axis, is uniquely determined. The dielectric properties
of the crystal in the x and y directions then exhibit no anomalies, and to
investigate the properties in the z-direction we need consider only those
terms in the thermodynamic potential which contain Dz.

‘The expression (19.1) represents the leading terms in an expansion of ©
in powers of D. Since 1/e®) is small near the transition point, it is necessary
to take into account the next term beyond the quadratic in the expansion in
powers of Dz. There can be no odd powers in this expansion, since they would
change sign with D, (and so ® would change), whereas here the two directions along the z-axis are equivalent. The next term after the quadratic
therefore involves D;4:

o= 6 1 D2 Z DA.
= +5 DE+ De.
In order that the state with Dz = 0 should be stable at the point T= 0,
it is clearly necessary that the coefficient B should be positive there, and so
positive in the neighbourhood of that point. Near the transition point,
1/e® can be expanded in powers of the difference 7—Q; the first term in
the expansion is of the form «(T—@), the coefficient « being positive (so
that 1/e@ > 0 for T > ©). Thus
® = 1/x(T—0), (19.2)
and the thermodynamic potential is
LCL
® = G+ ue DZ +76, Pe . (19.3)

‘These formulae are sufficient for the calculation of all ferroelectric properties of present interest near the transition point. First of all, from the formula
Ez = 4n0/éD; we have

E, = «(T—0)Dz+ BDS. (19.4)
This is the fundamental relation giving the field as a function of the induction
in a ferroelectric.

For T > @ (in the non-pyroelectric phase), Dz is zero for E; = 0. As E,

increases (for a given value of T—Q), the induction at first increases linearly

° 86 Electrostatics of Dielectrics §19
(Dz = E,/«(T—O)), but for sufficiently large values of Ez, we have
D, = (E-{B)+. The proportionality coefficient e%) in the linear relation is the
dielectric constant of the non-pyroelectric phase. For 7 > @ it increases
without limit in inverse proportion to T—O, but the linear relation then
ceases to be valid.

For T < © (in the pyroelectric phase), the value Dz = 0 cannot correspond toa stable state. For Ez = 0 the induction has a non-zero value, which
by (19.4) is

Dz = Di = £/[e(O—T)B]. (19.5)
Thus the spontaneous polarisation Pz = Dzo/42 of a ferroelectric decreases
towards the Curie point as «/(Q—T).

The “dielectric constant” of the pyroelectric phase may be defined as the
value of the derivative dD,/dE, for Ez;=0. From (19.4) we have
1 = [—«(O—T)+3BD]dD,/dE,; substituting (19.5), we have dDz/dEz
= 1/2«(@—T) for E, = 0. For sufficiently small E,, the relation between Dz
and E, becomes

Dz—Dz = Ez/2«(0—T). (19.6)
A comparison of (19.2) and (19.6) shows that the “dielectric constant” of
the pyroelectric phase is half its value in the non-pyroelectric phase at the
same distance from the Curie point.

Differentiating ® (19.3) with respect to temperature, we can find the
entropy S = —(@0/@T)p = So—aD,7/8n. Here the fourth-order term can
be omitted, since the quadratic term is not zero. In the pyroelectric phase
with E, = 0 we have also Dz; = 0, so that S = So. For the pyroelectric
phase, substituting Dz from (19.5), we find S = Sp—o*(@—T)/8mB. Hence
the specific heat of this phase at the transition point itself is

Cp = TaS/OT = Cy + 20/8nB, (19.7)
where Cyo is the specific heat of the non-pyroelectric phase at this point.
Thus, if the transition of the ferroelectric from one phase to the other takes
place with E, = 0, it is accompanied by a sudden change in the specific heat,
as happens in ordinary second-order phase transitions. Moreover, Cp > Cyo,
i.e. the specific heat increases when pyroelectricity appears.

Let us further investigate equation (19.4) in the pyroelectric phase (i.e.
for T < @). Figure 13 shows the approximate curve of the function D(Ez) |
given by this equation. We see, first of all, that the part CC’ of the curve
(shown dashed in *Fig. 13) does not correspond to stable states which can*
occur in Nature: on CC’ we have 0EF,/8Dz = 47020/@D,2 < 0, whereas
the condition that the second variation of the thermodynamic potential
should be positive requires this derivative to be positive also. The
ordinates of the points C and C’ are given by the equation dE,/éDz = 0,
and so we conclude that the possible values of |Dz| in the pyroelectric phase
are bounded below by the condition

DZ > «(@—T)/3B. (19.8)

§19 Ferroelectrics 87

If we consider states of a ferroelectric with given values of E;, there is still
an ambiguity in the value of Dz, in the range of abscissae between C and C’,
and the question arises of the physical significance of the two values. We
shall assume the ferroelectric to be a homogeneous flat slab, with the ferroelectric axis perpendicular to it, lying between the plates of a condenser,
which are maintained at given potentials, i.e. which set up a given uniform .
field E = E;.

For given potentials on the conductors, the condition of stability requires
that the thermodynamic potential = ®—E-D/47 be a minimum. In
particular, for E = 0 there are two states in which D, has opposite signs (the
points A and A’ in *Fig. 13) but (= ®) is the same. These two states,*
therefore, are equally stable, i.e. they are two “phases” which can exist in
contact.

a 8
a
¢ \
<
SL B
\
Vor
A
Fa

Fic. 13

Hence it is clear that the portions AC and A’C’ of the curve correspond to
states which are metastable but not absolutely stable. It is easy to see directly
that the values of on AC and A’C’ are in fact greater than its values of A’B’
and AB for the same value of E,. The ordinates of A and A’ are given by

| formula (19.5). Thus the range of metastability is
«@-T)/3B < D2 < e(@-T)B. (19.9)

The existence of these two “phases” with E = 0 is very important, since
it means that a ferroelectric body can be divided into a number of separate
regions or domains in which the polarisation is in opposite directions. On
the surfaces separating these domains, the normal component of D and the
tangential component of E must be continuous. The latter condition is
satisfied identically, because E = 0. From the former condition it follows
that the domain boundaries must be parallel to the z-axis.

88 Electrostatics of Dielectrics §19
The actual shapes and sizes of the domains are determined by the condi
tion that the total thermodynamic potential of the body should be a mini
mum. This subject has not yet been much studied for ferroelectrics.

If we are not interested in the details of the structure, and consider portions of the body which are large compared with the domains, we can use
the induction DB averaged over such portions. Its component D; can evidently take values in the range between the ordinates of A and A’ in *Fig. 13,*
Le.

—V[a(O-T)/B] < Dz < V[e(@-T)/B]. (19.10)
In other words, if Dz in *Fig. 13 is taken as the induction averaged in this way,*
the vertical segment AA’ corresponds to the region of domain structure, and
the thick curve BAA’B’ gives all stable states of the body.

A ferroelectric must, in particular, have a domain structure if it is not in
an external electric field. For we have seen in §18 that the conditions of
thermodynamic equilibrium in the absence of an external field reduce to the
condition that ® should be an absolute minimum as a function of D, with
E = 0 everywhere.t

Let us consider ferroelectrics which belong (in the non-pyroelectric phase)
to the cubic system. The cubic symmetry requires that ¢@ = ev) = ¢)
= «, and admits two independent fourth-order invariants formed from the
components of the vector D, which may, for example, be taken as Dz4+Dy4+
+D-Aand D,?D/+D?D2+DD7. Hence the expansion of the thermodynamic potential is of the form

® = O+a(T—O)(Dz? + Dy? + D2)/8+ B(Dz4+ Dy*+ DA)/160+
+C(Dz2D,2+ Dz2D2+ Dy2D2)/87, (19.11)
where we have again put 1/e = o(7—Q), and «, B, C are constants.

It must be borne in mind, however, that cubic symmetry may admit also
a third-order invariant DD,D-; this happens for the crystal classes T and
Ta, where there is no centre of symmetry. In these cases the state with
D = 0 certainly cannot satisfy the stability condition (that ® should be a |
minimum), and so no Curie point can exist. Hence the ferroelectric transition can occur only in crystals of the classes O, T;,, On of the cubic system,
in accordance with the expansion (19.11).

The sum of the fourth-order terms in (19.11) must be essentially positive.
Hence we must have

B>0, C>-B. (19.12)

The spontaneous polarisation of a ferroelectric in the absence of an
external field is determined, as already stated, by the condition that ® should |

+ It should be emphasised that here we are speaking of complete thermodynamic equilibrium. This exists in ferroelectrics, but cannot do so in ordinary pyroelectrics, because of
the difficulty, already mentioned, of reorienting the polarisation and so forming domains

§19 Ferroelectrics 89
be a minimum as a function of D. In particular, since the second-order
term in (19.11) is independent of the direction of D, the direction of the
spontaneous polarisation is determined by the condition that the fourthorder terms are a minimum for a given absolute value of D. Two cases are
possible. If C > B, the minimum of ® corresponds to D being along any
one of the axes x, y, 2, ie. along any of the three edges of the cube (the
crystallographic directions [001], [010], [100]). If, however, C < B, ® takes
its minimum values when D is along any one of the spatial diagonals of the
cube (the crystallographic directions [111], [111], etc.) ic. when Dz? = D,?
= D/? = 3D*. In the former case the spontaneously polarised pyroelectric
phase of the ferroelectric has tetragonal symmetry, and in the latter case it
has rhombohedral symmetry.

Let us consider in more detail, for example, the first case (C > B), and
take as the z-axis the direction of the spontaneous polarisation below the
Curie point. The magnitude of this polarisation is determined by the minimum of the expression — «(@— T)D2?/82 + BD4/167, whence

Do? = «(O-T)/B. (19.13)
The “dielectric permeability” in the z-direction below the Curie point is,
of course, different from that in the x and y directions. If the field E is
small, then Dz, Dy and Dz—Dp are also small. Differentiating the expression
(19.11) gives
Ez = 4n00/8D, = —a(@—T)Dz+ BDS = 2BDo(Dz— Dp),
E, = 4700/0Dz = [CDp2—a(@—T)]Dz, whence
Dz—Do = E;|2a(@ —T), (19.14)
Dz = BEz/«(@—T)(C-B).

Above the Curie point the dielectric permeability of a cubic ferroelectric is

the same in all directions:
= 1/a(T-@). (19.15)
Finally, let us briefly consider the elastic properties of ferroelectrics.
According to its crystallographic class, the non-pyroelectric phase of a ferroelectric may or may not be piezoelectric.t Here particular interest attaches
to piezoelectric crystals whose symmetry admits a piezoelectric relation
between the deformation and the polarisation in the direction of the ferroelectric axis. These include the classes Dz, Deg and S4; in each case the
induction D; in the direction of the ferroelectric axis appears in the piezoelectric part of the thermodynamic potential through a termt—A, 2yDzozy.

+ The non-pyroelectric phase of a ferroelectric is piezoelectric if it belongs to one of
eight out of the ten classes listed at the end of §17: Ds, Ds, Dea, Ss, Ds, Ds, Can, Dan.

Since we are using here the potential ®, and not & as in §17, the piezoelectric tensor
Aikt is not the same as the tensor yi,x1 introduced previously, but their symmetry properties

are, of course, identical.

90 Electrostatics of Dielectrics §19
In the elastic energy of these crystals, the component ozy appears in a term
—HayzySxy®. Thus the thermodynamic potential near the Curie point is

® = O+0(T— To)Dz2/80 + BDA/167—ADzo2y— pony, (19.16)
where for brevity we have put Azzy = A, uzyzy = wu. The terms involving the
other components are of no interest, since they lead to no anomaly of the
piezoelectric properties near the Curie point.

Differentiating © with respect to Dz and czy, we find the field Ez and the
deformation ugy:t

Ez = 4n0®/0Dz = a(T—T)Dz+ BDS—4mozy, (19.17)
Ugy = 4ADz + poxy. (19.18)
In the non-pyroelectric region when E is small we can neglect the term in
D# in (19.17):
Ez, = o(T— 1 )Dz—4mAczy.
Substituting Dz from (19.18), we find
A Et [ + 2nd? |
“ev Qa T—To) LY o(T—To)]
The coefficient of ozy in this formula represents the modulus of elasticity
for deformations in which the field Ez is kept constant, while « in formula
(19.18) is the modulus for constant induction Dz. Hence we can write
p® = p)+ 2nd2/o(T— Tp), (19.19)
where the superscripts indicate the nature of the deformation. We see that
the two coefficients behave entirely differently near the Curie point: whereas
#®) is a finite constant, u) increases without limit as the Curie point is
approached.

In the pyroelectric region, formula (19.18) shows that the spontaneous
polarisation results in a certain deformation of the body. If there are no
internal stresses and the field E is zero, the deformation uzy is proportional
to Dzo, i.e. by (19.5) it is proportional to ~/(9—T).

If the symmetry (cubic, for example) of the non-pyroelectric phase of a
ferroelectric does not admit a piezoelectric effect linear in D, then the first
non-vanishing terms in an expansion of the thermodynamic potential in
powers of oj and D are quadratic in the components Dj, i.e. they are of the |
form

—vizimDiDrorm, (19.20)
where yix1m is a tensor of rank four, symmetrical with respect to the pairs of
suffixes i, k and 1, m.

+ See the first footnote to §17, Problem 1, concerning differentiation with respect to the

components ux.

§19 Ferroelectrics 91

Doubt might be cast on the legitimacy of using the expression (19.20) in
the thermodynamic potential, on the grounds that, as stated in §17, this
potential can be used only when quadratic effects are neglected. However,
the ferroelectrics form an exception because, near the Curie point, the field
E is smallt compared with the induction D. The use of the thermodynamic
potential involves the neglect of quantities of the order of EDuy (or, what
is the same thing, EDo,), whereas the expression (19.20) is of the order
of Dox.

+ This is seen, for instance, from formula (19.4): the first term on the right-hand side

contains the small quantity T — @, and the second term is of the third order in D.



---


## 中文翻译

> **中文：** 第II章——介电体的静电场。

### 主要内容
本章讨论介电体中静电场的基本理论。介电体在电场中会被极化，产生束缚电荷。引入**极化强度$\mathbf{P}$**（单位体积内的电偶极矩）和**电位移矢量$\mathbf{D} = \mathbf{E} + 4\pi\mathbf{P}$**。对各向同性介电体，$\mathbf{D} = \varepsilon\mathbf{E}$，其中$\varepsilon$为介电常数。

### 关键概念
- **退极化场**：极化产生的束缚电荷在介电体内部产生与外加电场相反的退极化场
- **边界条件**：$\mathbf{D}$的法向分量和$\mathbf{E}$的切向分量在介电体界面上连续
- **椭球介电体**：退极化场可以通过退极化因子解析求解
- **Clausius-Mossotti关系**：分子极化率与宏观介电常数之间的关系

### 应用
介电常数测量、电容器设计、电磁材料表征。

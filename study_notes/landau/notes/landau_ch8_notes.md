# Landau & Lifshitz《Electrodynamics of Continuous Media》第8章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter VIII: Magnetostatics of Magnetic Materials

THE ELECTROMAGNETIC WAVE EQUATIONS

## Section §56: The field equations in a dielectric in the absence of dispersion

| In §45 we gave the equations for a variable electromagnetic field in a metal:
curlH = 4rcE/c, curlE = — (1/c) @B/ét, (56.1)
which hold when the field changes sufficiently slowly: the frequencies of the
field must be such that the dependence of j on E (and of B on H, if needed)
is that corresponding to the static case. f
We shall now examine the corresponding problem for a variable electromagnetic field in a dielectric, and shall formulate equations valid for fre| quencies such that the relations between D and E, and B and H, are the same
as when the fields are constant. If, as usually happens, these relations are
| simple proportionalities, this means that we can put
| D=<&, B-=4H, (56.2)
with the static values of ¢ and p.
| These relations are not valid (or, as we say, ¢ and exhibit dispersion) at
| frequencies comparable with the eigenfrequencies of the molecular or
electronic vibrations which lead to the electric or magnetic polarisation of
the matter. The order of magnitude of such frequencies depends on the
substance concerned, and varies widely. It may also be entirely different
for electric and for magnetic phenomena.}

The equations

div B = 0, (56.3)

eurlE = — (1/c) 0B/dt (56.4)

are obtained immediately by replacing e and h in the exact microscopic

Maxwell’s equations by their averaged values E and B, and therefore are
always valid. The equation

divD = 0 (56.5)

is obtained (§6) by averaging the exact microscopic equation dive = 4zp,

+ The condition 1 <A does not relate to the validity of equations (56.1) as they stand.
In the problems discussed in Chapter VII this condition was necessary in order to justify
the neglect of retardation effects in the field outside the conductor.

} In diamond, for example, the electric polarisation is due to the electrons, and the
dispersion of e begins only in the ultra-violet. In a polar liquid such as water, the polarisation
is due to the orientation of molecules with permanent dipole moments, and the dispersion
of ¢ appears at frequencies w ~ 104, i.e. in the centimetre wavelength range. ‘The dispersion
of » in ferromagnetics may begin at even lower frequencies.

240 The Electromagnetic Wave Equations §56
using only the fact that the total charge on the body is zero. This result is
evidently independent of the assumption made in §6 that the field is static,
and equation (56.5) is therefore valid in variable fields also.

A further equation is to be obtained by averaging the exact equation

1a 4n
curl h = -—~ + pv. (56.6)
cot oc
A direct averaging gives
10E 47_
curl B = -—+—pv. (56.7)
c at €
When the macroscopic field depends on time, the establishment of the relation between the mean value pv and the other quantities is fairly difficult.
It is simpler to effect the averaging in the following more formal way.

Let us assume for the moment that extraneous charges of volume density
pex are placed in the dielectric. The motion of these charges causes an
“extraneous current” jex, and the conservation of charge is expressed by an
equation of continuity:

apex|dt + divjex = 0.
Instead of equation (56.5) we have divD = 4zpex; see (6.8). Differentiating this equation with respect to time and using the equation of continuity,
we obtain a(div D)/at = 42pex/2t = — 47 div jex, or
@D
div| — jex} = 0.
iv( a * tries)
Hence it follows that the vector in parentheses can be written as the curl of
another vector, which we denote by cH. Thus
4n 16D
1H = —j -——. 56.8)
cus c dex 7 c ot )

Outside the body this must be the same as the exact Maxwell’s equation
for the field in a vacuum, and therefore H is the magnetic field. Inside the
body, in the static case, the current jex is related to the magnetic field by the
equation curl H = 4njex/c, where H is the quantity introduced in §27 and
related in a definite manner to the mean field B. Hence it follows that, in
the limit of zero frequency, the vector H in equation (56.8) is the static
quantity H(B), and our present assumption that the field varies “slowly”
means that the same relation H(B) holds between these variable fields. Thus
H is a definite quantity, so that we can drop the auxiliary quantity jex and
obtain the final equation

eurlH = (1/c) aD/ét. (56.9)

§56 The field equations in a dielectric in the absence of dispersion 241
This equation replaces in dielectrics the first equation (56.1) for the field
in metals. It might be supposed that the term in dE/@t ought to be included
when this equation is used for variable fields in metals also, giving
4a oE
curlH = cE +=—. (56.10)
c ce ét
In good conductors such as the true metals, however, the introduction of
this term is pointless. The two terms on the right-hand side of (56.10) are
essentially the first two terms in an expansion in powers of the field frequency. Since this frequency is assumed small, the second term must represent at most a small correction. In actual fact, in metals the corrections for
the effect of the spatial non-uniformity of the field become important sooner
than the frequency correction (see the sixth footnote to §45).

There are, however, substances, namely poor conductors, for which
equation (56.10) may be meaningful. For such reasons as the small number
of conduction electrons in semiconductors, or the small mobility of the ions
in electrolyte solutions, these substances exhibit anomalously low conductivity, and hence the second term on the right of equation (56.10) may be
comparable with, or even exceed, the first term at frequencies for which o
and « may still be regarded as constants. In a field of a single frequency w,
the ratio of the second term to the first is «w/4mo. If this ratio is small,
the body behaves as an ordinary conductor of conductivity o. At frequencies
w > 4io/e, it behaves as a dielectric with dielectric constant e.

In a homogeneous medium with constant ¢ and p, equations (56.3)-(56.5)
and (56,9) become

divE=0, divH=0, (56.11)
éH oE
eulE=—-' curl =<. (56.12)
c at c ot
Eliminating E in the usual manner, we obtain
@ PH
eurleurlH = <—curlE = — ——
cat ce Oe
and, since curl curl H = grad div H—- AH = — AH, we reach the
‘wave equation .
eu CH
H -——— = 0.
. a
A similar equation for E can be obtained by eliminating H. We see that
the velocity of propagation of electromagnetic waves in a homogeneous
dielectric is
ol/(e)- (56.13)

242, The Electromagnetic Wave Equations §56

The electromagnetic energy flux density in a dielectric is given by the
same formula as in a metal:

S = cE x H/47. (56.14)
This is easily seen by calculating div S. Using equations (56.4) and (56.9),
we obtain
divS = LG-eurl E — E-eurlH)
1 eD B ou
= -—{E-— +H) =-—, 56.15
4a ( ot ot ot ( ) |
in accordance with the expression dU = (E-dD+H-dB)/47 for the differential of the internal energy of a dielectric at given density and entropy.

The general requirements of relativistic invariance have the result that
the energy flux density must be the same, apart from a factor c, as the space
density of the field momentum, { which is therefore

E x H/42c. (56.16)

This expression must, in particular, be used in determining the forces on a

dielectric in a variable electromagnetic field. The force f per unit volume

may be calculated from the stress tensor ojx: fi = 004%/ Axx. Here, however,

it must be remembered that oj is the momentum flux density, which in
cludes the momentum of both the matter and the electromagnetic field. If fis

taken as the force on the medium, the rate of change of the field momentum
per unit volume must be subtracted:

don =8 (EX Hy

, ee eee 56.17

fi Ox, = Ot 4c ( )

In a constant field the last term is zero, and so this question did not arise

previously.

Since the field varies “slowly”, the stress tensor may be taken to have the
same value as in a constant field. For instance, in a fluid dielectric, o4x is
given by the sum of the electric part (15.9) and the magnetic part (34.2). In
differentiating these expressions with respect to the co-ordinates we must
use the fact that the equations curl E = 0, curl H = 0 for a constant field
(in the absence of currents) are replaced by equations (56.12). The result is

FE Ge) EX) H?
f= — grad po — — grade + ad [o(—) =l-= d,
Brad po — o gtade grad |p Op) 78x 3,8? Bt
Op e—-10
+ a[(%) e] +S hex. 56.18)
grad lola) acl * aac ee core)

+ This follows from the symmetry of the four-dimensional energy-momentum tensor;
see The Classical Theory of Fields, §4-7, Addison-Wesley Press, Cambridge (Mass.), 1951;
Pergamon Press, London, 1959.

§57 The electrodynamics of moving dielectrics 243

## Section §57: The electrodynamics of moving dielectrics

The motion of a medium results in an interaction between the electric and
magnetic fields. Such phenomena for conductors have been discussed in
§49; we shall now discuss them for dielectrics. Here we are in practice
concerned with the phenomena occurring in moving media when external
electric or magnetic fields are present. It should be emphasised that they
are in no way related to the appearance of fields as a result of the motion
itself (§§35, 50).

Our starting point in §49 was the formulae giving the transformation of

| the field when the frame of reference is changed. There it was sufficient to

| know the general formulae for the transformation of electric and magnetic
fields in a vacuum, the averaging of which gives immediately the formulae

| for the transformation of E and B. In dielectrics the problem is considerably
more complex, because the electromagnetic field is described by a greater
number of quantities.

In the motion of macroscopic bodies, the velocities involved must in
practice be small compared with the velocity of light. To obtain the necessary
approximate transformation formulae, however, it is simplest to use the
exact relativistic formulae which hold for all velocities.

In the electrodynamics of the field in a vacuum, the components of the
electric and magnetic field vectors e and h are actually components of an
antisymmetrical four-dimensional tensor (or “four-tensor”) of rank two.
‘The same is true of E and B, which are the mean values of e and h. Thus
there is a four-tensor F;, whose components are given byt

| 0 B, —By, —iEz |
Fy =|7Be 9 By, —iEy | (57.1)
By -B, 0 —~iEz
1Ey iEy iEz 0
Using this tensor, the first two Maxwell’s equations,
divB=0, curlE = — (1/c) @B/at, (57.2)
can be written in the four-dimensional form
Fe OF OF
sorta t+ = 82 57.3
Oxy Oxg Oxy SE)
This shows the relativistic invariance of the equations. The applicability of
equations (57.2) to moving bodies is evident, since they are obtained directly
from the exact microscopic Maxwell’s equations by replacing e and h by
their averaged values E and B.

+ See The Classical Theory of Fields, §§3-9, 4-1.

} In the present section (but not in the Problems) the tensor suffixes take the values 1, 2,
3, 4, corresponding to the four-dimensional co-ordinates x1 = x, x2 = y, x3 = =, x4 = ict.

244 The Electromagnetic Wave Equations §57

The second pair of Maxwell’s equations |

divD =0, — curl H = (1/c) eD/dt (57.4)
also retain their form in moving media. This is seen from the arguments
given in §56, in which we used only general properties of bodies (e.g. that
the total charge is zero), equally valid for moving bodies and bodies at rest.
However, the relations between D and E, and B and H, need not be the same
as in bodies at rest.

Since they are valid for bodies both at rest and in motion, equations
(57.4) must be unaltered by the Lorentz transformation. For a field in
a vacuum, the vectors D and H are the same as E and B, and the relativistic invariance of the second pair of Maxwell’s equations appears in the
fact that they also can be written in four-dimensional form, using the same
tensor Fiz: OF y/Ox, = 0.t Hence it is clear that, to ensure the relativistic
invariance of equations (57.4), it is necessary that the components of the
vectors D and H should be transformed as the components of a four-tensor
exactly similar to Fiz, which we denote by Hix:

0 H, —Hy -iDz
-— Hz 0 Hz —iDy
Hx = 57.5.
il Hy -He 0 —-iD, (67.5)
iDz iDy iDz 0
Using this tensor, we can write equations (57.4) in the form
2HulOxe = 0. (57.6)

Having elucidated that the quantities E, D, H, B form four-dimensional
tensors, we have also ascertained the law of their transformation from one
frame of reference to another. However, we are interested rather in the
relations between the quantities in a moving medium, which generalise the
relations D = <E and B = pH valid in a medium at rest.

We denote by 1; the velocity four-vector of the medium; its components
are related to the three-dimensional velocity v by

v ; v2
naa ennfellt-Z) =i Jb-2)
From this four-vector and the four-tensors Fi, and Hix we form combinations which become E and D in a medium at rest. These combinations are
the four-vectors Fu, and Hiyuz; for v = 0 their time components are
t See The Classical Theory of Fields, §4-5.

§57 The electrodynamics of moving dielectrics 245

zero and their space components are E and D respectively. The four
dimensional generalisation of the equation D = cE is therefore evidently¢
Huy = Fur. (57.7)

Similarly, we see that the generalisation of B = 1H is the four-dimensional

equation
Fay + Fei + Fug = p( Huan + He + Hux). (57.8)
Returning from the four-dimensional to the three-dimensional notation,
we derive from these two equations the vector relationst
Dt+vxH/c = (E+vx Bic),
le = ¢) 579)
B+Ex v/ce = p(H+ Dx v/c).
These formulae, first derived by H. Minkowski (1908), are exact in the
sense that no assumption has yet been made concerning the magnitude of
the velocity. If the ratio v/c is assumed small the equations can be solved
for D and B as far as terms of the first order to give
D = E+ (qm — 1)v x Hic, (57.10)
B = pH + (eu — 1)E x vc. (57.11)
These formulae, together with Maxwell’s equations (57.2) and (57.4), form
the basis for the electrodynamics of dielectrics in motion.

The boundary conditions on Maxwell’s equations are also somewhat
modified. From the equations div D = 0, div B = 0 the continuity of the
normal components of the inductions follows as before:

Dm = Dn, Bm = Bno. (57.12)
The conditions on the tangential components of the fields are most simply
obtained by changing from the fixed frame of reference K to another, K’,
which moves with the surface element considered, whose velocity along the
normal n we denote by uv». The usual conditions, namely that E’; and H’;
are continuous, hold in the frame K’. By the relativistic transformation
formulae,|| these are equivalent to the continuity of the tangential components of the vectors E+vxB/c and H—vxD/c. Taking the components
perpendicular to n and using equations (57.12), we obtain the required
boundary conditions:
nx + Ej) = vn(Be — Bi)/c,
ee ie (57.13)
n x (Hy — Hy) = — vp(D2 — Dy)/e.

+ It should be noted that, by writing down relations involving only the local value of the
velocity, we neglect slight effects due to the possibility of a velocity gradient, such as gyromagnetic effects (§35).

{ If either of the relations D = ¢E and B = 4H does not hold in the medium at rest,
the corresponding relation (57.9) is replaced by a different functional relation between the
vector sums on the two sides of the equation.

|| See The Classical Theory of Fields, §3-10.

‘ 246 The Electromagnetic Wave Equations §57

If we substitute here the expressions (57.10) and (57.11), and neglect
terms of higher order in v/c, we obtain

n x (Ez — Ei) = op(u2 — 41)Hie, (57.14)
n x (Hz — Hh) = — on(e2 — a1) Ee. :
In this approximation the values of H and E on the two sides of the surface
need not be distinguished on the right-hand sides of equations (57.14).

If the body moves so that its surface moves tangentially to itself (e.g. a
solid of revolution rotating about its axis), then vp = 0. Only in this case
do the boundary conditions (57.13) or (57.14) reduce to the usual conditions that E; and H; are continuous.

PROBLEMS

Prostxm 1. A dielectric sphere rotates uniformly in a vacuum in a uniform constant
magnetic field $. Determine the resulting electric field near the sphere.

SoLvTIoN. In calculating the resulting electric field, the magnetic field may be taken to
be the same as for a sphere at rest, since an allowance for the reciprocal effect of the magnetic
field variation would give corrections of a higher order of smallness. Within the sphere, the
magnetic field has the uniform value H = 3$/(2+y); ef. (8.2).

Since the rotation is steady, the resulting electric field is constant and, like any constant
electric field, has a potential: E= —grad ¢. Outside the sphere, the potential satisfies the
equation Ag(e) = 0; inside the sphere, it satisfies

AG = Acu—1)Q-H|ce, qa)
where Q is the angular velocity. ‘The latter equation is obtained from divD = 0 by substituting for D the expression (57.10) with vy =§2Xr. The condition that the normal
component of D is continuous at the surface of the sphere gives

agit) pt agter
-f2 TT {Q-HW—(Q-n)(HW-ny) = Fy . 2
(] + (o-mHo-ny =~] @
Here a is the radius of the sphere and n a unit radial vector.

From the symmetry of the sphere, the required electric field is determined by only two
constant vectors, & and {. From the components of these vectors we can form a bilinear
scalar $-@ and a bilinear tensor $:%+ $2 —43u-@, the sum of whose diagonal terms
is zero. Accordingly, we seek the field potential outside the sphere in the form

1 ae 1, mm
() = =D, () = 2D, 7
$0 Pe eater) — PS
where Dir is a constant tensor (with Du = 0), the electric quadrupole moment tensor of
the sphere. t No term of the form constant/r can appear in ¢'¢), since such a term would
give a non-zero total electric flux through a surface surrounding the sphere, whereas the
sphere is uncharged. The field potential inside the sphere is sought in the form
2 -1
6 = 2 Danm+ “9.407224, (4)
2a® 3ce
‘The first term is the solution of the homogeneous equation Ag = 0, and the coefficient is
chosen so as to give continuity of the potential, and therefore of Ez, at the surface of the
sphere. Substituting (3) and (4) in (2), we obtain
a 3(e4—1)
= 1510 24-48 -Q].
Dx 2 G+200+—) HiMe+ HO —F5x-H -Q], (5)
t See The Classical Theory of Fields, §5-6.

§58 The dispersion of the dielectric permeability 247
‘Thus. a quadrupole electric field is formed near the rotating sphere, and the quadrupole
moment of the sphere is given by formula (5).t In particular, if the axis of rotation (the
z-axis) is parallel to the external field, Da has only the diagonal components
a 4(eu—1)
= -— $0, Drz = Dyy = —*Diz.
Dis 7 G+200+ mo” sz = Dyy 22.

PRosLem 2. A magnetised sphere rotates uniformly in a vacuum about its axis, which is
parallel to the direction of magnetisation. Determine the resulting electric field near the
sphere.

Souurion. ‘The magnetic field inside the sphere is uniform, and is expressed in

| terms of the constant magnetisation M by the equations B+2H = 0 (cf. (8.1)) and
BO—H® = 42M, whence BU = 82M/3, H® = —4cM/3. The second of formulae
(57.9) does not hold in this case, because the formula B = pH is not valid for a ferromagnetic at rest; from the first of (57.9) we have, inside the sphere,
D = B+evxBe—vx Hc
= E+4n(2e+1)v x M/3c.
The potential of the resulting electric field outside the sphere satisfies the equation
Ag(e) = 0, and that inside the sphere satisfies Ag) = 8u(2e+1)MQ/3ce.
‘The boundary condition that Ds is continuous at the surface of the sphere gives
A #)/ (4):
28] 2M aarsin = [28],
or Irma 3c or Ipma
where @ is the angle between the normal n and the direction of & and M (the z-axis). We
seek $(¢) and 6 in the forms
Dunn — Diz,
) = 219 —
4 Seb = gaat c0s"9—1),
r 4n(2e+1)
(0) = 7D, .(3 cos?8—1) + ai? —a?).
$9 = ZDed(3 cos*9—1) + na)
From the boundary condition we obtain the following expressions for the electric quadrupole
moment of the rotating sphere:
_ _ 4Qe+1) , ne
Da= 3e(2er3)* OM, Dzz = Dy = —4Dzz,
where @ is the total magnetic moment of the sphere. For a metal sphere we must take
«> ©, giving
Diz = —40.Ma"/3c.

## Section §58: The dispersion of the dielectric permeability

Let us now go on to study the important subject of rapidly varying electromagnetic fields, whose frequencies are not restricted to be small in comparison
with the frequencies which characterise the establishment of the electric and
magnetic polarisation of the substances concerned.
An electromagnetic field variable in time must necessarily be variable in
space also. For a frequency «, the spatial periodicity is characterised by a

+ Similarly, a quadruple magnetic field occurs near a sphere rotating in a uniform electric
field. ‘The magnetic quadrupole moment is given by (5) if the sign is changed and ¢, 4, §
are replaced by y, ¢, € respectively.

t If the direction of magnetisation is not the same as that of the axis of rotation, the
problem is considerably changed, since the sphere then emits electromagnetic waves.

248 The Electromagnetic Wave Equations §58
wavelength A ~ c/w. As the frequency increases, A eventually becomes
comparable with the atomic dimensions a. The macroscopic description of
the field is thereafter invalid.

‘The question may arise whether there is any frequency range in which, on
the one hand, dispersion phenomena are important but, on the other hand,
the macroscopic formulation still holds good. It is easy to see that such a
range must exist. The most rapid manner of establishment of the electric or
magnetic polarisation in matter is the electronic mechanism. Its relaxation
time is of the order of the atomic time a/v, where v is the velocity of the
electrons in the atom. Since v < c, even the wavelength A ~ ac/v corresponding to these times is large compared with a.

In what follows we shall assume the condition A > a to hold.t It must |
be borne in mind, however, that this condition may not be sufficient: for
metals at low temperatures there is a range of frequencies in which the
macroscopic theory is inapplicable, although the inequality c/w >a is
satisfied (see §67).

The formal theory given below is equally applicable to metals and to
dielectrics. At frequencies corresponding to the motion of the electrons
within the atoms (optical frequencies) and at higher frequencies, there is,
indeed, not even a quantitative difference in the properties of metals and
dielectrics.

It is clear from the discussion in §56 that Maxwell’s equations

divD=0, divB=0, (58.1)

curlE = —(1/c)@B/at, curlH = (1/c) @D/at (58.2)

remain formally the same in arbitrary variable electromagnetic fields. These

equations are, however, largely useless until the relations between the

quantities D, B, E and H which appear in them have been established. At

the high frequencies at present under consideration, these relations bear no

resemblance to those which are valid in the static case and which we have
used for variable fields in the absence of dispersion.

First of all, the principal property of these relations, namely the dependence of D and B only on the values of E and H at the instant considered,
no longer holds good. In the general case of an arbitrary variable field, the
values of D and B at a given instant are not determined only by the values of
E and H at that instant. On the contrary, they depend in general on the
values of E(t) and H(#) at every previous instant. This expresses the fact
that the establishment of the electric or magnetic polarisation of the matter
cannot keep up with the change in the electromagnetic field. The frequencies
at which dispersion phenomena first appear may be completely different for
the electric and the magnetic properties of the substance.

+ The effects (called the natural optical activity) resulting from terms of the next order
in the small ratio a/A will be considered in §83.

§58 The dispersion of the dielectric permeability 249

In the present section we shall refer to the dependence of D on E; the
specific features of the dispersion of magnetic properties will be discussed
in §60.

The polarisation vector P has been introduced in §6 by means of the
definition 5 = —div P, p being the true (microscopic) charge density. This
equation expresses the electric neutrality of the body as a whole, and together
with the condition P = 0 outside the body it shows that the total electric
moment of the body is {P dV. This derivation is evidently valid for variable

| as well as for constant fields. Thus in any. variable field, even if dispersion
is present, the vector P = (D—E)/4z retains its physical significance: it is
the electric moment per unit volume.

In rapidly varying fields, the field strengths involved are in practice always
fairly small. Hence the relation between D and E can always be taken to
be linear.} The most general linear relation between D(z) and the values of
the function E(¢) at all previous instants can be written in the integral form

2
| D(t) = E(t) + { f@E(t — 7) dr. (58.3)
0
It is convenient to separate the term E(f), for reasons which will become
evident later. In equation (58.3) f(z) is a function of time and of the properties of the medium. By analogy with the electrostatic formula D = <E,
we write the relation (58.3) in the symbolic form D = ¢E, where é is a
linear integral operator whose effect is shown by (58.3).
Any variable field can be resolved by a Fourier expansion into a series of
components of a single frequency, in which all quantities depend on time
through the factor e~t, For such fields the relation (58.3) between D and
| E becomes
D = cw)E, (58.4)
where the function ¢(«) is defined as
©
ew) = 1+ f freer dr. (85) 7 =
0
Thus, for periodic fields, we can regard the dielectric permeability (the
coefficient of proportionality between D and E) as a function of the frequency
as well as of the properties of the medium. The dependence of « on the
frequency is called its dispersion law.

+ Here we assume that D depends linearly on E alone, and not on H. In a constant field,
a linear dependence of D on H is excluded by the requirement of invariance with respect
to a change in the sign of the time. In a variable field, this condition no longer applies, and
a linear relation between D and H is possible if the substance possesses symmetry of various
kinds. It is, however, a small effect of the order of a/A, and is indeed the effect mentioned in
the last footnote.

250 The Electromagnetic Wave Equations §58

The function ¢(w) is in general complex. We denote its real and imaginary
parts by ¢’ and ¢”:

<(w) = €(w) + te’(w). (58.6)
From the definition (58.5) we see at once that
<(— w) = e*(w). (58.7)
Separating the real and imaginary parts, we have
<(-w)=(w), e(—w) = — (a). (58.8)
Thus ¢’ is an even function of the frequency, and ¢’ is an odd function.

For frequencies which are small compared with those at which the dispersion is large, we can expand «(w) as a power series in w. The expansion
of the even function ¢’(w) includes only even powers, and that of the odd
function ¢(w) includes only odd powers. In the limit as w — 0, the function «(w) in dielectrics tends, of course, to the electrostatic dielectric constant,
which we here denote by «o. In dielectrics, therefore, the expansion of
¢(w) begins with the constant term <0, while that of e’’() begins, in general,
with a term in w.

The function ¢(w) at low frequencies can also be discussed for metals, if
it is defined in such a way that, in the limit w > 0, the equation

curlH = (1/c) dD/at
becomes the equation
curlH = 47cE/c

for a constant field in a conductor. Comparing the two equations, we see
that for w +0 we must have @D/ét > 47oE. But, in a periodic field,
@D/ét = —iweE, and we thus obtain the following expression for ¢e(w) in
the limit of low frequencies:

e(w) = 4rio/w. (58.9)

Thus the expansion of the function e(w) in conductors begins with an
imaginary term in 1/w, which is expressed in terms of the ordinary conductivity o for constant currents.j The next term in the expansion of ¢(w) is
a real constant, although for metals this constant does not have the same
electrostatic significance as it does for dielectrics.t

Moreover, this term of the expansion may again be devoid of significance
if the effects of the spatial non-uniformity of the field of the electromagnetic

. wave appear before those of its periodicity in time.

+ The imaginary part of the function ¢(w) is sometimes represented in the form (58.9)
for all frequencies; this amounts to introducing a new function o(«), which has no physical
significance apart from its relationship to «”(w).

‘} To avoid misunderstanding, we should point out a slight change in notation in comparison with §56. In equation (56.10) for poor conductors, ¢(w) is (4mia/w) + ¢.

§60 The dispersion of the magnetic permeability 251

In superconductors there is always considerable non-uniformity, resulting
from the smallness of the “penetration depth” of the magnetic field. It is
not yet clear whether the concept of the dielectric permeability «(w) has any
meaning for superconductors.

## Section §59: The dielectric permeability at very high frequencies

In the limit as w -> oo, the function ¢(w) tends to unity. This is evident
from simple physical considerations: when the field changes sufficiently
rapidly, the polarisation processes responsible for the difference between the
field E and the induction D cannot occur at all.

It is possible to establish the limiting form of the function «(w) at high
frequencies, which is valid for all bodies, whether metals or dielectrics. The
field frequency is assumed large compared with the “frequencies” of the
motion of all, or at least the majority, of the electrons in the atoms forming
the body. When this condition holds, we can calculate the polarisation of
the substance by regarding the electrons as free and neglecting their interaction with one another and with the nuclei of the atoms.

| The velocities v of the motion of the electrons in the atoms are small
compared with the velocity of light. Hence the distances v/w which they

| traverse during one period of the electromagnetic wave are small compared
with the wavelength c/w. For this reason we can assume the wave field
uniform in determining the velocity acquired by an electron in that field.

| The equation of motion is m dv’ /dt = eE = eEye~!, where e and m are
the electron charge and mass, and v’ is the additional velocity acquired by
the electron in the wave field. Hence v’ = icE/mw. The displacement r of
the electron due to the field is given by # = v’, and therefore r = —eE/mw®.
The polarisation P of the body is the dipole moment per unit volume.
Summing over all electrons, we find P = Ler = —e2NE/mo?, where N is
the number of electrons in all the atoms in unit volume of the substance. By

the definition of the electric induction, we have D = <E = E+4nP. We
thus have the formula

| ew) = 1 — 40Ne2/mo?. (59.1)

The range of frequencies over which this formula is applicable begins, in
practice, at the far ultra-violet for light elements and at the X-ray region

| for heavier elements. +

## Section §60: The dispersion of the magnetic permeability

Unlike the dielectric polarisability, the magnetic susceptibility ceases to
have any physical meaning at relatively low frequencies. To take account
of the deviation of (2) from unity would then be an unwarrantable refinement.

+ If e(w) is to retain the significance which it has in Maxwell’s equations, the frequency
must also satisfy the condition w <c/a. We shall see later (§97), however, that the expression (59-1) can be allotted a certain physical significance even at higher frequencies.

252 The Electromagnetic Wave Equations §60
To show this, let us investigate to what extent the physical meaning of the
quantity M = (B—H)/4z, as being the magnetic moment per unit volume,
is maintained in a variable field. The magnetic moment of a body is, by
definition, the integral
1
5 | 8 var. (60.1)
The mean value of the microscopic current density is related to the mean
field by equation (56.7):
1B Soe + poe 60.2:
cue ONE ae ed
Subtracting the equation curl H = (1/c)@D/ét, we obtain
pv = ccurlM + @P/éat. (60.3)
The integral (60.1) can, as shown in §27, be put in the form {M dV only if
pv =c curl M and M = 0 outside the body.

Thus the physical meaning of M, and therefore of the magnetic susceptibility, depends on the possibility of neglecting the term dP/dt in (60.3). °
Let us see to what extent the conditions can be fulfilled which make this
neglect permissible.

For a given frequency, the most favourable conditions for measuring the
susceptibility are those where the body is as small as possible (to increase
the space derivatives in curl M) and the electric field is as weak as possible
(to reduce P). The field of an electromagnetic wave does not satisfy the
latter condition, because Z ~ H. Let us therefore consider a variable field,
say in a solenoid, with the body under investigation placed on the axis. The
electric field is due only to induction by the variable magnetic field, and the
order of magnitude of E inside the body can be obtained by estimating the
terms in the equation curlE = —(1/c)@B/at, whence E/l ~ wH/c or
E ~ (al/c)H, where 1 is the dimension of the body. Putting «—1 ~ 1, we
have OP/at ~ wE ~ wlH/c. For the space derivatives of the magnetic
moment M = xH we have |c curl M| ~ cyH/l. If |@P/dt| is small compared with |c curl Mj, we must have

RB < xc2/w®. (60.4)
It is evident that the concept of magnetic susceptibility can be meaningful
only if this inequality allows dimensions of the body which are (at least) just
macroscopic, i.e. if it is compatible with the inequality / > a, where a is
the atomic. dimension. This condition is certainly not fulfilled for the
optical frequency range; for such frequencies, the magnetic susceptibility is
always ~ v2/c2, where v is the electron velocity in the atom;+ but the optical

+ The relaxation times for any paramagnetic or ferromagnetic processes are certainly
large in comparison with the optical periods.

§61 The field energy in dispersive media 253
frequencies themselves are ~ v/a, and therefore the right-hand side of the
inequality (60.4) is ~ a.

Thus there is certainly no meaning in using the magnetic susceptibility
from optical frequencies onward, and in discussing such phenomena we
must put » = 1. To distinguish between B and H in this frequency range
would be an over-refinement. Actually, the same is true for many phenomena even at frequencies well below the optical range.

## Section §61: The field energy in dispersive media

The formula

S =cExH/47 (61.1)
for the energy flux density remains valid in variable electromagnetic fields,
even if dispersion is present. This is evident from the arguments given at
the end of §29: on account of the continuity of the tangential components
of E and H, formula (61.1) follows from the condition that the normal
component of S is continuous at the boundary of the body and the validity
of a similar formula in the vacuum outside the body.

The rate of change of the energy in unit volume of the body is div S.
Using Maxwell’s equations, we can write this expression as

divS 1 p.2? u.); 61.2
iv = (ES +H); (61.2)
see (56.15). In a dielectric medium without dispersion, when « and p are
real constants, this quantity can be regarded as the rate of change of the
electromagnetic energy
U = (cE? + pH2)/8z, (61.3)
which has an exact thermodynamic significance: it is the difference between
the internal energy per unit volume with and without the field, the density
and entropy remaining unchanged.

In the presence of dispersion, no such simple interpretation is possible.
Moreover, in the general case of arbitrary dispersion, the electromagnetic
energy cannot be rationally defined as a thermodynamic quantity. This is
because the presence of dispersion in general signifies a dissipation of energy,
ie, a dispersive medium is also an absorbing medium.

To determine this dissipation, let us consider an electromagnetic field of
a single frequency. By averaging with respect to time the expression (61.2),
we find the steady rate of change of the energy, and this is the mean quantity
Q of heat evolved per unit time and volume.

Since the expression (61.2) is quadratic in the fields, all quantities must
be written in real form. If, as is convenient for a field of a single frequency,
we take E and H to be complex, then in (61.2) we must substitute for E and
@D/ét respectively 4(E+E*) and }(—iweE+iwe*E*), and similarly for H

254 The Electromagnetic Wave Equations §61
and @B/ét. On averaging with respect to time, the products E-E and E*-E*,
which contain factors e¥2it, give zero, leaving

tw o

Q = Siler — QE-E* + (uh — EH] = 2(e"(BP + uIP),

16m 80

This expression can also be written
Q = w(eE? + 2"H2)/47, (61.4)

where E and H are the real fields, and the bar denotes an average with |
respect to time.

This important formula shows that the absorption (dissipation) of energy
is determined by the imaginary parts of « and ». The two terms in (61.4)
are called the electric and magnetic losses respectively. On account of the
law of increase of entropy, the sign of these losses is determinate: the dissipation of energy is accompanied by the evolution of heat, i.e. Q > 0. It
therefore follows from (61.4) that the imaginary parts of « and p are always
positive:

>0, pb’ >0 (61.5)
for all substances and at all frequencies. ‘The signs of the real parts of «
and p for w # 0 are subject to no physical restriction.

Any non-steady process in an actual body is to some extent thermodynamically irreversible. The electric and magnetic losses in a variable
electromagnetic field therefore always occur to some extent, however slight.
That is, the functions <’’(w) and .’"(w) are not exactly zero for any frequency
other than zero. We shall see in §62 that this statement is of fundamental
importance, although it does not exclude the possibility of only very small
losses in certain frequency ranges. Such ranges, in which ¢’’ and ” are
very small in comparison with ¢’ and yp’, are called transparency ranges. It
is possible to neglect the absorption in these ranges and to introduce the
concept of the internal energy of the body in the electromagnetic field, in
the same sense as in a constant field. To determine this quantity, it is not
sufficient to consider a field of only a single frequency, since the strict
periodicity results in no steady accumulation of electromagnetic energy. Let
us therefore consider a field whose components have frequencies in a narrow
range about some mean value wo. The field strengths can be written

E = Eq(tjet4o, = H = Ho(t)e#ot, (61.6)

} Strictly speaking, this statement applies to bodies which, in the absence of the variable
field, are in thermodynamic equilibrium; we assume this condition to hold. If the body is
not in thermal equilibrium, then Q may in principle be negative. The second law of thermodynamics requires only a net increase in entropy as a result of the effects of the variable
electromagnetic field and of the absence of thermodynamic equilibrium, the latter effect
being independent of the presence of the field. A hypothetical example of such a body is
one in which all the atoms have been excited artificially (i.e. otherwise than by spontaneous
thermal excitation).

§61 The field energy in dispersive media 255 .
where E(t) and Ho(¢) are functions of time which vary only slowly in comparison with the factor e~#of, The real parts of these expressions are to be
substituted on the right-hand side of (61.2), and we then average with
respect to time over the period 27/wo, which is small compared with the time
of variation of the factors Eo and Ho.
The first term in (61.2), with E written in complex form, is
HE + E*)-4@ + D*)/4x,
and similarly for the second term. The products E-D and E*-D* vanish
| when averaged over time, and can therefore be ignored, leaving
1 éD* oD
——|E.-—— + E*.—}. 61.7)
int ot ¥ a) OEE
We write the derivative @D/dt as fE, where f is the operator 0¢/dt, and
ascertain the effect of this operator on a function of the form (61.6). If Eo
were a constant, we should have simply fE = f (w)E, where f(w) = —iwe(w).
| We expand the function Eo(#) as a series of Fourier components Ep,e~*,
with constant Eo,. Since Eo(#) varies only slowly, this series will include
| only components with « < wo. We can therefore put
FEoae- 0+) = f(a + ep) Epge Hoo +
qj
~ f (wo) Eoge-too + + aifleo)_ Ege-il%o+ 2,
dwo
| Summing the Fourier components, we have
d al
PPe()e-t = fon) Boe te + # LOO) Pet,
| day at
Omitting henceforward the suffix 0 to w, we thus obtain
oD d(we) Eo
= = ~iwdw)E + ete, 1.8
ae OE ta ae ® (61.8)
Substituting this expression in (61.7) and neglecting the imaginary part of
€(w) gives
1 d(we) /,, ,, Eo dEo* 1 d(we) d
oe ait —— ) = —- + (E-E*),
16m de (re a + * a) ioe da at”)
since E-E* = Eo-Eo*. Adding a similar expression involving the magnetic
field, we conclude that the steady rate of change of the energy in unit volume
is given by dU/dt, where
1 [d(we) d(wp)
= [SO gee 4 SOP ne), :
Wy rel do + dw | Ge

256 The Electromagnetic Wave Equations §62
In terms of the real fields E and H this expression can be written
1 fd(we)— dwn) =
U0 Pat do E2 + ‘lo i. (61.10)

This is the required result: 0 is the mean value of the electromagnetic
part of the internal energy per unit volume of a transparent medium. If there
is no dispersion, ¢ and yz are constants, and (61.10) becomes the mean value
of (61.3), as it should.

If the external supply of electromagnetic energy to the body is cut off, the
absorption which is always present (even though very small) ultimately
converts the energy U entirely into heat. Since, by the law of increase of
entropy, there must be evolution and not absorption of heat, we must have
O > 0. It therefore follows, by (61.9), that the inequalities d(we)/dw > 0,
d(wp)/dw > 0 must hold. In reality, these conditions are necessarily fulfilled, by virtue of more stringent inequalities always satisfied by the functions
«(w) and p(w) in transparency ranges (see §64).}

Considerable interest attaches to the determination of the (time) average
stress tensor giving the forces on matter in a variable electromagnetic field.
This problem is meaningful for both absorbing and non-absorbing media,
whereas that concerning the internal energy can be proposed only if absorption is neglected. The corresponding formulae, however, have not yet been
derived.

## Section §62: The relation between the real and imaginary parts of ¢(w)

The function f(r) in (58.3) is finite for all values of 7, including zero.t
For dielectrics it tends to zero as r + co. This simply expresses the fact
that the value of D(z) at any instant cannot be appreciably affected by the
values of E(z) at remote instants. The physical agency underlying the
integral relation (58.3) consists in the processes of the establishment of the
electric polarisation. Hence the range of values in which the function f(z)
differs appreciably from zero is of the order of the relaxation time which
characterises these processes.

The above statements are true also of metals, the only difference being
that the function f(z) — 470, rather than f(z) itself, tends to zero as t > co.
This difference arises because the passage of a steady conduction current,
though it does not cause any actual change in the physical state of the metal,
in our equations leads formally to the presence of an induction D such that

+ The sum of the inequalities (64.1) and (64.2) shows, in fact, that the derivative d(we)/de
always exceeds unity.

{ It was to ensure this that the term E(t) was separated in (58.3), since otherwise the
function f(r) would have a delta-function singularity at = 0.

§62 The relation between the real and imaginary parts of «(w) 257
(1/c)@D/ét = 420E/c or
t oo
Dit) = f 4roE(z) dt = 40 j E(t —7)dr.
= 6
We have defined the function «(w) by
”
ew) = 1+ | eerf(a)dr. (62.1)
| 0
It is possible to derive some: very general relations concerning this function
by using the methods of the theory of functions of a complex variable. To
do so, we regard w as a complex variable (w = o’+iw"’), and ascertain
the properties of the function ¢(w) in the upper half of the w-plane. From
the definition (62.1) and the above-mentioned properties of the function
(2), it follows that «(w) is a one-valued regular function everywhere in the
upper half-plane. For, when w” > 0, the integrand in (62.1) includes the
exponentially decreasing factor e~ or and, since the function f(z) is finite
throughout the region of integration, the integral converges. The function :
| ¢(«) has no singularity on the real axis (w”” = 0), except possibly at the origin
(where, for metals, «(«w) has a simple pole).}
| It is useful to notice that the conclusion that «(w) is regular in the upper
half-plane is, physically, a consequence of the causality principle. The
- integration in (58.3) is, on account of this principle, taken only over times
previous to t, and the region of integration in formula (62. 1) therefore
extends from 0 to oo rather than from — 09 to oo.
It is evident also from the definition (62.1) that
€(— w*) = €*(w). (62.2)
This generalises the relation (58.7) for real w. In particular, for purely
imaginary w we have ¢(iw"’) = ¢*(iw"’), ie. the function ¢(w) is real on the
imaginary axis:
ime =0 for w= iw". (62.3)
| It should be emphasised that the property (62.2) merely expresses the fact
that the operator relation D = 2E must give real values of D for real E. If
| the function E(t) is given by the real expression
E = Ege tot + Eptei*, (62.4)
_ __f In the lower half-plane, the definition (62.1) is invalid, since the integral diverges.
Hence the function «(«) can be defined in the lower half-plane only as the analytical continuation of formula (62.1) from the upper half-plane, and in general has singularities.
"The function «(w) has a physical as well as a mathematical significance in the upper halfplane: it gives the relation between D and E for fields whose amplitude increases as e®'.
In the lower half-plane, this physical interpretation is not possible, if only because the
presence of a field which is damped as e~!@"It implies an infinite field for t > — 00.

258 The Electromagnetic Wave Equations §62
then, applying the operator @ to each term, we have

D = e(w)Eoe-* + €(— w*)Ep*eto*t,
and the condition for this to be real is just (62.2).

According to the results of §61, the imaginary part of e(w) is positive for
positive real w = w’, i.e. on the right-hand half of the real axis. Since, by
(62.2), im «(—w’) = —im ¢(w’), the imaginary part of «(w) is negative on
the left-hand half of thjs axis. Thus |

ime 20 for w= wo’ 20. (62.5) |
At w =0, ime changes sign, passing through zero for dielectrics and
through infinity for metals. This is the only point on the real axis for which
im e(w) can vanish,

When » tends to infinity in any manner in the upper half-plane, «(w)
tends to unity. This has been shown in §59 for the case where w tends to
infinity along the real axis. The general result is seen from formula (62.1):
if w + 0 in such a way that w’’ -> oo, the integral in (62.1) vanishes because
of the factor e~ "7 in the integrand, while if w’’ remains finite but |«’| > 00
the integral vanishes because of the oscillating factor et.

The above properties of the function <(w) are sufficient to prove the
following theorem: the function «(w) does not take real values at any finite
point in the upper half-plane except on the imaginary axis, where it decreases monotonically from «9 > 1 (for dielectrics) or from +o (for metals)
at w = 10 to 1 at w = ioo. Hence, in particular, it follows that the function
¢(w) has no zeros in the upper half-plane.

We shall not pause to prove this theorem, because it is identical with a
general theorem concerning the “generalised susceptibility” (and the properties of e(w) enumerated above exhibit a similar analogy).{ For the same
reason, the function «(w) satisfies the general relations between the real and
imaginary parts of the generalised susceptibility. We shall repeat here the
derivation of these relations, in order to emphasise certain differences between
dielectrics and metals.

Let us take some real value wo of w, and integrate the expression
(«—1)/(w— 9) round the contour C shown in *Fig. 29. This contour in*
c
C1
Fie. 29

} See Statistical Physics, §122, Pergamon Press, London, 1958. The generalised suscep
tibility (a) used there corresponds to «(w) — 1, which vanishes as w —> 00.

§62 The relation between the real and imaginary parts of «(w) 259
cludes the whole of the real axis, indented upwards at the point w = wo > 0,
and also at the point w = 0 if the latter is (as in metals) a pole of the function «(w), and is completed by a semicircle of infinite radius. At infinity
« > 1, and the function (e—1)/(w— w) therefore tends to zero more rapidly
than 1/w. The integral
-1
J So te (62.6)
@ — wo

é
consequently converges; since «(w) is regular in the upper half-plane, and
the point w = wo has been excluded from the region of integration, the
function (¢—1)/(w— 9) is analytic everywhere inside the contour C, and
the integral is therefore zero.

The integral along the semicircle at infinity is also zero. We pass round
the point wo along a semicircle whose radius p ->0. The direction of
integration is clockwise, and the contribution to the integral is —im[e(wo) — 1].
If the function ¢(w) pertains to a dielectric, the indentation at the origin is

| unnecessary, and we therefore have
—pt am co)
li —_ dane 1] =0
biel [ Soaeet [ Saagte} atte tro
co p+ uo
The expression in the braces is the integral from —o to oo, taken as a
principal value. Thus we have
f«-1
P f —— dw — in[ (wo) — 1] = 0. (62.7)
w— wo
qc

Here the variable of integration w takes only real values. We replace it
by x, call the given real value w instead of wo, and write the function ¢(w)
of the real variable w, as in §58, in the form «(w) = <'(w)+ie"(w). Taking
the real and imaginary parts of (62.7), we obtain the following two formulae:

1. Pex)
<(w)-1=-P J ——dx, (62.8)
7 x—-w
=)
1 fe(#)-1
e"(w) = --P f Ont Ey (62.9)
wT x—-w
—®
first derived by H. A. Kramers and R. pe L. Kronic (1927). It should be
emphasised that the only important property of the function «(w) used in

260 The Electromagnetic Wave Equations §62
the proof is that it is regular in the upper half-plane.t Hence we can say
that Kramers and Kronig’s formulae, like this property of «(w), are a direct
consequence of the causality principle.

Using the fact that <’’(x) is an odd function, we can rewrite (62.8) as

OM ou
e(w)-1= tp [Oa + *p [ae
Tv x—-w 7 x+o
o 0
2 Fea)
= “pf aly (62.10) |

If a metal is concerned, the function ¢(w) has a pole at the point. w = 0,
near which ¢ = 47ia/w (58.9). The passage along a semicircle round this
point gives a further real term —(470/«o)7, which must be added to the
left-hand side of equation (62.7). Thus formula (62.9) becomes

1 Pe(e)-1, 4a

"(w) = ~ =P [ae (62.11)

7 ad x—w w
but (62.8) and (62.10) remain unchanged. A further remark is also necessary
as regards metals. We have said at the end of §58 that there may be ranges
of frequency for metals in which the function «(w) becomes physically
meaningless on account of the spatial non-uniformity of the field. In the
formulae given here, however, the integration must be taken over all frequencies. In such cases e(w) must be taken, in the frequency ranges concerned, as the function obtained by solving the formal problem of the
behaviour of the body in a fictitious uniform periodic electric field (and not
in the necessarily non-uniform field of the electromagnetic wave).

Formula (62.10) is of particular importance: it makes possible a calculation of the function e(w) if the function ¢’(w) is known even approximately
(for example, empirically) for a given body. It is important to note that, for
any function <'(w) satisfying the physically necessary condition <” > 0

- for w > 0, formula (62.10) gives a function ¢‘(~) consistent with all physical
requirements, i.e. one which is in principle possible (the sign and magnitude
of e’ are subject to no general physical restrictions). This makes it possible
to use formula (62.10) even when the function ¢<’(w) is approximate.
Formula (62.9), on the other hand, does not give a physically possible
function e’’(w) for an arbitrary choice of the function ¢’(w), since the condi
tion that <’’(w) > 0 is not necessarily fulfilled.

+ The property «> 1 as w > © is not important: if the limit «(co) were other than
unity, we should simply take « — «(00) in place of « — 1, with corresponding obvious
changes in formulae (62.8), (62.9).

§62 The relation between the real and imaginary parts of e(w) 261
In dispersion theory the expression for <'(w) is customarily written in
the form
' fret f Ste)
e(w)-1= Pl as (62.12)
0
where e and m are the charge and mass of the electron, and f(w) dw is
called the oscillator strength (or “number of dispersion electrons”) in the
frequency range dw. According to (62.10), this quantity is related to ¢(w)
by
m
fe) = 555") (62.13)
For metals, f(w) tends to a finite limit as w > 0.
For sufficiently large w, x2 can be neglected in comparison with «? in
| the integrand in (62.10). Then
| wo t= 2 fered
e(w)-1= os xe’’(x) dx.
| Qa
For the dielectric constant at high frequencies, on the other hand, formula
| (59.1) holds, and a comparison shows that
© ©
m
ary f we''(w) dw = J flw)dw = N, (62.14)
a 0
where N is the total number of electrons per unit volume.
If e’(w) is regular at w = 0, we can take the limit w > 0 in formula
| (62.10), obtaining
©
20 et
e(0)-1=- f LC) ay. (62.15)
7 x
| 3
If the point w = 0 is a singularity of ’“(w) (as in metals), the limit of the
integral (62.10) as w — 0 is not what is obtained by simply deleting the term
in w. To calculate the limit, we must first replace ¢’’(x) in the integrand by
e'"(x)—470/x; the value of the integral is unchanged, because
P fp dx _
i) ew °.
é

262 The Electromagnetic Wave Equations §62
For a dielectric, formula (62.15) can be rewritten as
4ne2N —
«9 — 1 = ——w, (62.16)
m
where the bar denotes averaging with respect to the “number of oscillators”:
~
— 1
oro} feu
0
The expression (62.16) may be useful in estimating ¢o. |
The following formula relates the values of «(w) on the upper half of
the imaginary axis to those of ¢’(w) on the real axis:
2
. 2 xe'"(x)
-1l=-|—— Sd. 17)
(ew) sl| x2 + oP (62.17)
O
Integrating this relation over all w, we obtain
f [e(iw) -— 1] dw = J <"(w) do. (62.18)
0 0
All the above results are applicable, apart from slight changes, to the
magnetic permeability u(w). The differences are due principally to the fact
that the function (w) ceases to be physically meaningful at relatively low
frequencies. Hence, for example, Kramers and Kronig’s formula must be
applied to p(w) as follows. We consider not an infinite but a finite range of
(from 0 to 1), which extends only to frequencies where y is still meaningful but no longer variable, so that its imaginary part may be taken as zero;
let the real quantity (#1) be denoted by x1. Then formula (62.10) must be
written as
1
7 pl
p(w) - 1 = —P f 20) ay, (62.19)
7 x2 —
0
Unlike «9, the value jo of (0) may be either less than or greater than unity.
The variation of 4(w) along the imaginary axis is again a monotonic decrease,
from pio to pu. < po.
t See Statistical Physics, formula (122.19).

§63 A plane wave of a single frequency 263

## Section §63: A plane wave of a single frequency

Maxwell’s equations (58.2) for a wave of a single frequency are
iwp(w)H = ceurlE, iwe(w)E = — ccurlH. (63.1)
These equations as they stand are complete, since equations (58.1) follow
from (63.1) and so do not require separate consideration. Assuming the
medium homogeneous, and eliminating H from equations (63.1), we obtain
the second-order equation
| AE + <u(w2/c2)E = 0; (63.2)
elimination of E gives a similar equation for HLet us consider a plane electromagnetic wave propagated in an infinite
homogeneous medium. In a plane wave in a vacuum, the space dependence
of the field is given by a factor etkr, with a real wave vector k. In considering wave propagation in matter, however, it is in general necessary
to take k complex: k = k’+zk”, where the vectors k’ and k” are real.

Taking E and H as proportional to ek:r, and carrying out the differentia
tion with respect to the co-ordinates in equations (63.1), we obtain
opH = ckxE, oweE = —ckxH. (63.3)
Eliminating E and H from these two equations, we obtain for the square of
the wave vector
Re =k? — kh’? + Qik’ ek" = epw?/c?. (63.4)
We see that k can be real only if « and ys are real and positive. Even then,
however, k may still be complex if k’-k’’ = 0; we shall meet with such a
case in discussing total reflection in §66.

It must be borne in mind that, in the general case of complex k, the term
“plane wave” is purely conventional. Putting ek:r = eik -re-k’-r, we see
that the planes perpendicular to the vector k’ are planes of constant phase.
The planes of constant amplitude, however, are those perpendicular to k’”’,
the direction in which the wave is damped. The surfaces on which the field
itself is constant are in general not planes at all. Such waves are called
inhomogeneous plane waves, in contradistinction to ordinary “homogeneous”
plane waves.

The general relation between the electric and magnetic field components
is given by formulae (63.3). In particular, taking the scalar product of these
formulae with k, we obtain

kE=0, kH=0, (63.5)
and, squaring either and using (63.4),
E2 = pHy/e, (63.6)
It must be remembered, however, that because all three vectors k, E and H
are complex these formulae do not in general have the same evident significance as when the vectors are real.

264 “The Electromagnetic Wave Equations §63
We shall not give the cumbersome relations valid in the general case, but
consider only the most important particular cases. Especially simple results
are obtained for a wave propagated without damping in a non-absorbing
(transparent) homogeneous medium. The wave vector is real, and its
magnitude is
k= V(eu)wle = noe, (63.7)
where n = 4/(«u) is called the refractive index of the medium. The electric
and magnetic fields are both in a plane perpendicular to the vector k (a pure
transverse wave); they are mutually perpendicular, and are related by
H = V(e/u)l x E, (63.8)
where Lis a unit vector in the direction of k. Hence it follows that <E? = »H2,
but this does not mean (as it would in the absence of dispersion) that the
electric and magnetic energies in the wave are equal, since these energies
are given by different expressions (namely, the two terms in formula (61.10).
The velocity u with which the wave is propagated in the medium is given
by the familiar expression for the group velocity:
dw c (63.9)
“= = S
dk = d(nw)/dw
It is easy to verify that
u= S/0, (63.10)
in accordance with its significance as the velocity of transfer of energy in the
wave packet; here U is the energy density given by formula (61.9), and
= ¢ fe
S= < [fee (63.11)
80N
is the mean value of the Poynting vector. In the absence of dispersion, when
the refractive index is independent of frequency, the expression (63.9)
becomes simply c/n; cf. (56.13).

Next, let us consider 2 more general case, the propagation of an electromagnetic wave in an absorbing medium, the wave vector having a definite
direction (i.e. k’ and k’”’ being parallel). Then the wave is literally plane,
since the surfaces of constant field in it are planes perpendicular to the
direction of propagation (a homogeneous plane wave).

In this case we can introduce the “length” & of the wave vector, given by
k = Al (1 being a unit vector in the direction of k’ and k’’), and from (63.4)
we have k = 4/(eu)w/c. The complex quantity +/(«) is usually written in
the form n+ix, with real ” and x, so that

k= Veu)ole = (n + ix)wfe. (63.12)

+ When considerable absorption occurs, the group velocity cannot be used, since in an

absorbing medium wave packets are not propagated but rapidly “ironed out’’.

§63 A plane wave of a single frequency 265
The quantity 2 is called the refractive index of the medium, and x the
absorption coefficient; the latter gives the rate of damping of the wave during
its propagation. It should be emphasised, however, that the damping of
the wave need not be due to true absorption: dissipation of energy occurs
only when « and » are complex, but « is different from zero if « and pw are
real and of opposite sign.

We may express and « in terms of the real and imaginary parts of the
dielectric constant (taking 4 = 1), From the equation

ne — 2+ Zink = = €' + ie’
we have n2—«2 = e’, 2nx = e’. Solving these equations for m and x, we
havet
n= Viale + V(c? + “e)]}, (63.13)
w= VEL- e+ V(e? + DT}.
In particular, for metals and in the frequency range where formula (58.9) is
| valid, the imaginary part of « is large compared with its real part, and is
related to the conductivity by <’ = 4zr0/w; neglecting ¢’ in comparison with
é”, we find that n and « are equal:
n= k= /(2n0/w). (63.14)

The relation between the fields E and H in this homogeneous plane wave
is again given by formula (63.8), but « and yz are now complex. The formula
again shows that the two fields and the direction of propagation are mutually
perpendicular. If ~ = 1, we write +/e = +/(n®+K2) exp[i tan“ (x/n)],
which shows that the magnetic field is ./(n?+«2) times the electric field in
magnitude and tan~1(«/n) from it in phase; in particular, when (63.14)
holds, the phase difference is }7.

PROBLEM

At a given instant ¢ = 0 an electromagnetic perturbation occurs in some region of space.
The perturbation is not maintained by external agencies, and is therefore damped in time.
Find the damping decrement.

Soxvution. We expand the initial perturbation as a Fourier integral with respect to the
co-ordinates, and consider a component having a (real) wave vector k. The time dependence
of this component is given, for sufficiently large t, by a factor et with a complex “frequency” «, which is to be determined; the damping decrement is —im .

From the equations —F{/c = curl E = ikxE, )/c = curl H = ik x H we have, eliminating H,

Bie =kx(kxE). (1)
We take the direction of k as the x-axis. The “longitudinal” part of the perturbation therefore satisfies Dz = 0, whence Dz ~ 0.

t Since <’ > 0, the signs of 7 and « must be the same, in accordance with the fact that
the wave is damped in the direction of propagation. ‘The choice of positive signs in (63.13)
corresponds to a wave propagated in the positive x-direction.

266 The Electromagnetic Wave Equations §64

‘The relation between Dz and Ez is of the form

‘

Ex(t) = Dz = f F(t—1)De(r) dr; (2)

cf. §58. Since we have Ds(r) = 0 for 7 > 0, it follows that
°
Ex{t) = [ F(t—1)Dz(1) dr (3)
<2
Hence we see that, for large t, the time dependence of Ez is given essentially by that of the |
function F(t).
For a field of a single frequency, (2) gives
1 2
oe fox
re) { F(x)et* dx,
or, conversely,
moni pyro
2a} Ca) a

To estimate this integral for large t, we displace the path of integration into the lower halfplane of «w, where the integrand decreases rapidly. The singularities of the function 1/¢(w),
ive. the zeros and branch points of e(w), must be excluded from the contour. The integral
is then essentially proportional to e~0t, where wo is the singularity nearest the real axis.
This gives the solution for the longitudinal part of the perturbation.

For the transverse components, we have from (1) Dy,</¢?+-k*Ey,2 = 0. A similar analysis
gives the result that the required “frequency” wo is in this case the zero or branch point
of the function w%e(w)—c®k® which lies nearest the real axis.

## Section §64: Transparent media

Let us apply the general formulae derived in §62 to media which absorb
only slightly in a given range of frequencies, i.e. assuming that for these
frequencies the imaginary part of the dielectric permeability may be
neglected.

In such a case there is no need to take the principal value in formula
(62.10), since the point x = w does not in practice lie in the region of
integration. The integral can then be differentiated in the usual way with
respect to the parameter , giving

de 4w f x8)

—_—=— | ——_

dw 7 é (w2 — x2)2
Since the integrand is positive throughout the region of integration, we
conclude that

de(w)/dw > 0, (64.1)

i.e: if absorption is absent the dielectric constant is a monotonically increasing
function of the frequency.

§64 Transparent media 267

Similarly, in the same frequency range we obtain another inequality,

d to P_a8e'"(x)
mrt 1)) a J @ ae > 0,
or
de/dw > 2(1 — «)/w. (64.2)
If « < 1, this inequality is more stringent than (64.1).
It may be noted that the inequalities (64.1) and (64.2) (together with the
corresponding ones for («)) ensure that the inequality u < c is satisfied by
the velocity of propagation of waves. For example, if » = 1 we have
n = 4/e and, replacing « by n? in (64.1) and (64.2),
d(nw)/dw >, — d(nw)/dw > 1/n. (64.3)
Thus we obtain two inequalities for the velocity u (63.9): u < c/n and
u < cn, whence u < c whether n < 1 or n > 1. These inequalities also
show that u > 0, i.e. the group velocity is in the same direction as the wave
vector. This is quite natural, even if not logically necessary.

Let us suppose that the weak absorption extends over a wide range of
frequencies, from w to wg (> «;), and consider frequencies w such that
1 < w < we. The region of integration in (62.10) divides into two parts,
x < wand x > ws. In the former region we can neglect x in comparison
with w, and in the latter region w in comparison with x, in the denominator
of the integrand:

oe
2F dx 2
ew) = 14+ - J <"(x)— -— J wel’(x) dx, (64.4)
7 x mw
bp 6
ie. the function «(w) in this range is of the form a—b/w?, where a and 5
are positive constants. The constant 5 can be expressed in terms of the
“number of dispersion electrons” Nj responsible for the absorption in the
range from 0 to ay (cf. (62.14)):
<(w) = a — 4rNye2/mu. (64.5)

From this expression it follows, in particular, that, when the region of
weak absorption is sufficiently wide, the dielectric permeability in general
passes through zero. In this connection it should be recalled that a literally
“transparent” medium is one in which ¢(w) is not only real but also positive;
if € is negative, the wave is damped inside the medium, even though no
true dissipation of energy occurs.

For the frequency at which « = 0 the induction D is zero identically,
and Maxwell’s equations admit a variable electric field satisfying the single
equation curl E = 0, with zero magnetic field. In other words, longitudinal
electric waves can occur. To determine their velocity of propagation, we

268 The Electromagnetic Wave Equations §64
must take into account the dispersion of the dielectric permeability not only
in frequency, but also with respect to the wave vector. The value of w for
which ¢ = 0 is also a function of the wave vector. If the medium is isotropic, the next term after the zero-order term in the expansion of the scalar
function w(k) for which «[«(k)] = 0 is proportional to k2: w = wo+ tak?.
Hence the velocity of propagation is u = dw/dk = ok, and is proportional
to the wave vector itself.
|
PROBLEM

A plane electromagnetic wave with a sharply defined forward front is incident normally
on the boundary of a half-space (x > 0) occupied by a transparent medium with 4 = 1.
Determine the structure of the front of the transmitted wave (A. SoMMERFELD and L.
BriLLoum, 1914).

SoLuTIoN. Let the wave be incident on the boundary of the medium at time t = 0, so
that at x = 0 the field (E or H) of the incident wave is E = 0 for t< 0, E ~ eo! for
t > 0. Expanding this field as a Fourier integral with respect to time, we reduce the problem to that of waves of various frequencies and infinite extent incident on the boundary.
‘The amplitude of the Fourier component of frequency w is proportional to

°
f etlw-wo)t dr. |
a |
When a wave of frequency w is incident, the transmitted wave is of the form a(w) e~twtHuns le,
where the amplitude a(w) is a slowly varying function of frequency. Hence the wave field in
the medium in the present problem is
© ©
E ~ fae a(w)etotttonaie f elm w9)7 dr,
= a

In the region near the wave front, the important values of w in this integral are those
close to wo. Using a new variable = w—wo, we replace a(w) by a(wo), and expand the
exponent in powers of £. Omitting unimportant constants and phase factors, we have

rr A x) u’
E~ f J expli¢(e—e+ *) sie} dé dz,
23 u
where 1 = u(wo) is the velocity of propagation (63.9), and u’ = [du/de]y-ug- Effecting
the integration over é, we easily bring E to the form
E~ fe dn, w= (x—ut)/V(2s|u'l),
w
the sign in the exponent depending on that of u’. The intensity distribution near the wave
front is given by
oy a
I~| fet dn |.
»

‘This expression is of the same form as that which gives the intensity distribution near the
edge of the shadow in Fresnel diffraction.t For w > 0 the intensity decreases monotonically with increasing w, but for w < 0 it oscillates with decreasing amplitude about a constant
value to which it tends as w -> — 0. «

+ See The Classical Theory of Fields, §7-8.

J At large distances preceding the front here considered there are found “precursors”?
propagated with velocity c. These correspond to the high-frequency Fourier components,
for which «> 1.



---


## 中文翻译

> **中文：** 第VIII章——麦克斯韦方程组。

### 主要内容
麦克斯韦统一了电学、磁学和光学，建立了经典电磁理论的完整框架。真空中麦克斯韦方程组：
$$\nabla\cdot\mathbf{E} = 4\pi\rho,\quad \nabla\times\mathbf{B} = \frac{1}{c}\frac{\partial\mathbf{E}}{\partial t} + \frac{4\pi}{c}\mathbf{j}$$
$$\nabla\cdot\mathbf{B} = 0,\quad \nabla\times\mathbf{E} = -\frac{1}{c}\frac{\partial\mathbf{B}}{\partial t}$$

### 关键概念
- **位移电流**：$\partial\mathbf{E}/\partial t$项保证了电荷守恒
- **电磁波**：自由空间中麦克斯韦方程组导出波动方程，预言了电磁波以光速$c$传播
- **玻印廷定理**：$-\nabla\cdot\mathbf{S} = \partial u/\partial t + \mathbf{j}\cdot\mathbf{E}$，其中$\mathbf{S} = c\mathbf{E}\times\mathbf{H}/4\pi$，$u = (\mathbf{E}^2 + \mathbf{H}^2)/8\pi$
- **电磁势**：$\mathbf{E} = -\nabla\phi - \partial\mathbf{A}/\partial t$，$\mathbf{B} = \nabla\times\mathbf{A}$，规范变换

### 应用
所有电磁现象的理论基础，从无线电波到光学。

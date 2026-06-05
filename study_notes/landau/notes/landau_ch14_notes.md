# Landau & Lifshitz《Electrodynamics of Continuous Media》第14章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter XIV: Dispersion and Absorption

DIFFRACTION OF X-RAYS IN CRYSTALS

## Section §97: The general theory of X-ray diffraction

Tue phenomenon of X-ray diffraction in crystals occupies a special place
in the electrodynamics of matter, since the wavelengths concerned are
comparable with the distances between atoms. For this reason the usual
macroscopic approach to matter as a continuous medium is entirely invalid,
and we must begin by considering scattering by individual charged particles,
and essentially by electrons; the scattering by nuclei is unimportant, because
of their much greater mass.

The frequencies of the motion of electrons in the atom are of order
wo ~ v/a, where v is their velocity and a the dimension of the atom. If
A~ a, then, since v <c, these frequencies are small compared with the
X-ray frequency w ~ c/\. This makes it possible to write the equation of
motion of an electron in the field of the electromagnetic wave as

my' = cE, (97.1)
i.e. the electrons may be regarded as free (see §59).

From (97.1) we find the additional velocity acquired by the electron under
the action of the wave field: v’ = ieE/mw.

Let n(x, y, 2) be the number density of electrons in a crystal, averaged
over the quantum states of the electrons and over the statistical distribution
of the thermal motion of the nuclei in the lattice. It should be emphasised
that the usual macroscopic averaging over physically infinitesimal volume
elements is ot included, i.e. n(x, y, 2) is the actual density of the “electron
cloud” in the crystal lattice. The corresponding current density due to the
wave field is:

j = env’ = ienE/mw. (97.2)

We substitute this current in the microscopic Maxwell’s equations:

eurlE = iwH/c, (97.3)
curlH = — iwE/c + 4nj'/c
i 4nen
--2(1- ae. (97.4)
¢ mor
We thereby take account of its reciprocal effect on the field, i.e. scattering.

§97 The general theory of X-ray diffraction 399
It is, of course, assumed that this effect is small, i.e. that the inequality
421en|ma® < 1 (97.5)
holds. Putting D = <E, where
2,
<=1-4mn (97.6)
mo?
in accordance with the usual definition of the induction, we reduce equation
(97.4) to the usual form curl H = —iwD/c. Thus, in this sense, the expression (97.6) for the dielectric permeability (cf. (59.1)) can be used even for
wavelengths A ~ a, though it must of course be remembered that the
symbols E and D no longer retain their previous meanings: they now pertain
to the field which has not been averaged over physically infinitesimal volumes,
and ¢ is accordingly a function of the co-ordinates. .

In the scattering of X-rays by heavy atoms it may happen that the condition w > wp is fulfilled for the outer electron shells but not for the inner
ones, where w < wo and so the inequality A > a holds. In this case the
dielectric permeability can still be regarded as the coefficient of proportionality between D and E, but the formula corresponding to (97.6) gives
only the contribution of the outer electrons. That of the inner electrons must
in principle be calculated by averaging over the volume of their shells. Thus,
if we put D = <E with « a function of the co-ordinates, all possible cases
are allowed for. In what follows we shall, for definiteness, use the expression
(97.6).

In effecting the averaging of the electron density in (97.2) to obtain
n(x, y, 2) independent of time, we exclude a possible change of frequency on
scattering. That is, we consider only strictly coherent scattering, with no
change in frequency.

Eliminating H from the two equations (97.3) and (97.4), we obtain
curl curl E = w2D/c2. Here we substitute E = D+ 42e’nE/mu2 and expand the expression curl curl E, using the fact that div D = 0, as follows
from (97.4). Then

AD + wD/c? = curl curl (47e2nE/mw?). (97.7)
On the right-hand side of this equation, which already contains the small
quantity 47¢2n/mw*, E must be taken as the given field of the incident wave.
Let us find the solution of equation (97.7) in the region outside the scattering
crystal and at large distances from it.{ Since this equation is of the same
form as equation (91.3), the required solution is obtained immediately by

t In solving equation (91.3) it was not possible to consider the field outside the body,
since the boundary conditions on the surface would have had to be taken into account (the
quantity ¢’ on the left-hand side being different inside and outside the body). The left-hand
side of equation (97.7), however, is the same in all space.

400 Diffraction of X-rays in Crystals §97
analogy with (91.4):
& exp (ikRo)
E = —-———_F' x(k’ —iq: 6 B

mat Ro x(k’ x Ey) f mexp( igq-r) dV. (97.8)
Here R is the distance from the origin, which is within the crystal, to the
point considered; q = k’—k; k =k’ = w/c; Eo is the amplitude of the
incident wave. We put E instead of D on the left-hand side because the two
are equal in the vacuum outside the crystal.

To characterise the intensity of X-ray diffraction we use an effective crosssection c, defined as the ratio of the intensity diffracted into a solid angle
do’ to the energy flux density in the incident wave. By (97.8) we have

e2 \2 2
do = (5) sin? | i} n exp (— 7q-r) av| do’, (97.9)
me?
where 0 is the angle between Ep and k’. If the incident radiation is “natural”
(not polarised), the factor sin?@ in this formula becomes }(1+cos? 9),
where 9 is the angle between k and k’ (see the second footnote to §72):
1/2 \2 2
do = (S) (1 + cos? 9)| f mexp(- iq-nar| do’. (97.10)
2\me2
In what follows we shall, for definiteness, consider this particular case.

We see that the intensity of radiation diffracted in a given direction is

essentially proportional to the squared modulus of the integral

f nexp(—ia-r)dV, (97.11)
ite. the Fourier space component (with the appropriate value of q) of the
electron density. As q - 0 this integral becomes simply the electron density
fi averaged over a lattice cell. If n is replaced by # in equations (97.3) and
(97.4), we obtain the usual macroscopic Maxwell’s equations, with dielectric
permeability <(w) = 1—47e%/i/mw*. According to these equations, when
X-rays pass through a crystal they are refracted according to the ordinary
laws of refraction, with refractive index 4/<. Thus diffraction through small
angles amounts to ordinary refraction, which is of no interest here. In what
follows we shall always assume that q is appreciably different from zero.

The electron density, like any function of position in a crystal lattice, can
be expanded as a Fourier series:

n= z mp exp (2mib-r), (97.12)
where the summation is taken over all periods b of the reciprocal lattice. t
} See Statistical Physics, §132, Pergamon Press, London, 1958.

§97 The general theory of X-ray diffraction 401
When (97.12) is substituted in (97.11) and the result is integrated over the
volume of the crystal, we obtain practically zero except for values of q close
to some 2b. Between these values the intensity is negligible. We can
therefore consider each diffraction maximum separately, putting
n = mp exp (27ib-r)

with the appropriate value of b. Substitution in (97.10) gives

1/e\2

do = a(S) (1 + cos? $)|np|2 x
2\me2,
2
x | f exet- tk’ —k—2nb)-r}AV[ do’, (97.13)
The strongest maxima occur in directions for which the equation
k’ — k = 2nb (97.14)
(Laue’s equation) is exactly satisfied, and are called principal maxima. For
given b, however, a principal maximum does not occur for an arbitrary
direction and frequency of the incident radiation. If the equation (97.14)
is written as k’ = k+27b and squared, and we use the fact that k? = k’2,
we have
b-k = — 7b? (97.15)

This equation determines the values of the wave vector k for which principal
maxima occur with the given value of b. Geometrically, equation (97.15)
represents a plane in k-space perpendicular to the vector b at a distance 7b
from the origin. In particular, we see that k > 7b.

Since |k’—k| = 2k sin 39, it follows from (97.14) that

hsin}9 = ab (97.16)
(Bragg and Vul’f’s equation), which determines the angle of diffraction at
the principal maximum.

Any vector b of the reciprocal lattice determines a family of crystal planes
represented by the equations r-b = constant integer. These planes are
perpendicular to b, and the vectors k and k’ corresponding to the condition
(97.14) make equal angles of incidence and reflection with the planes (*Fig.
45), For this reason, diffraction at a principal maximum is sometimes spoken*
of as “reflection” from the corresponding crystal planes.

The total intensity of the diffraction “spot” near a maximum is obtained
by integrating (97.13) over a solid angle about the direction of k’. Let us
determine the intensity near a principal maximum. We denote by k’o the
value of k’ corresponding to Laue’s equation for a given k: k’p = k+2mb,
and put also x = k’—k’p, Near the maximum, x is small; since k’ and k’9

402 Diffraction of X-rays in Crystals §97
differ only in direction, x is perpendicular to k’9. The solid angle element
can therefore be written
do! = dig diy/h? = dig dey/h2, (97.17)
where the z-axis is taken in the direction of k’y. Thus
Ley? . 2
o= aa(—s) (1 + cos? 9)faol? [ dizday If exp(— ix-r)dV|.
2ab
AN
/ S
He \
Ya \
ie \
» ¢
Us| Ye
Fie. 45
In the volume integral we can effect the integration with respect to z, since
exp(—ix-r) is independent of z: f exp(—ix-r)dV = JZ exp(—ix-r) df,
where df = dx dy and Z = Z(x, y) is the length of the body in the direction
of k’. Finally, using a well-known formula in the theory of Fourier integrals:
1
f IblPdee dey = = J Pdedy, (97.18)
where
1
ge = Gay J (x,y) exp(— ix-r)dxdy
are the two-dimensional Fourier components, we obtain
Qn f eB \2
oH =(5) (1 + cos? 8}fml2 [ Zea
2/ea\2
= —{_ in2. 2 2
=F (5) sin?49(1 + cos? 9)|mul2 [ Z2df. (97.19)
The integral is of the order of L4, where L is the linear dimension of the body.
Thus the total effective cross-section, and therefore the total intensity of the
spot, are proportional to 4/8, where V is the volume of the body. The
maximum intensity, however, follows a different law. For k’—k = 2nb,

§97 The general theory of X-ray diffraction 403
the integral in (97.13) is just V, and so do is proportional to V?:

do yey?

(3) 5 () (1 + cos? 9)|ns|272. (97.20)

do’/ max — 2\mec?
The sharpness of the maximum is shown by the fact that the maximum
intensity is proportional to a higher power of V than the total intensity. The
“width” of the peak is evidently proportional to V4/3/V2 = V-28,

The theory given above is valid only if the diffraction effect is small. We
now see that this requirement imposes a certain condition on the dimension
of the crystal: ¢ must be small compared with the geometrical cross-section
of the body (~ L?), whence

ed
——|m| < 1. (97.21)
me? k

PROBLEMS

PROBLEM 1. Determine the intensity distribution in the diffraction spot round a principal
maximum in diffraction by a crystal in the form of a cuboid of sides Lz, Ly, Lz.

Souvrion. As above, we use the vector * = k’—k’o, and take the axes of co-ordinates
parallel to the sides of the cuboid, with the origin at its centre.

‘The integral fexp(—ix-r) dV becomes a product of three integrals of the form

Le 2

exp(—ikex) dx = — sin dueLe.
La a
‘Thus
ey 1 . 7 7
da 35) + cost im * aay sin? beads sin? Say sin® hale do’

The components of the vector % are not independent, being related by the condition
x-k’o = 0.

ProsieM 2. The same as Problem 1, but for diffraction by a spherical crystal of radius a.

SoLvTion. We again put x = k’—k’o, and take the z-axis in the direction of %, with
the origin at the centre of the sphere. Then

. .
J exp(—ixz) dV = f m(a®—2%) exp(—ixz) dz
=
4
= “sin xa—xa cos xa).
Pe
‘Thus

ace era eee ee 2 do’

= 80 cos* 8))rgl? (sin xa~ a cos xa) do’.

ProsiEM 3. Determine the total intensity of the diffraction spot round a subsidiary
maximum.

Soxution. In this case the wave vector k of the incident wave does not satisfy the condition (97.15). As shown above (97.15) is the equation of a plane perpendicular to the vector
b. Let the small displacement of the terminus of the vector k from this plane be 7b, where

a <1. That is, we put k = ko-+b, where ko satisfies equation (97.15) (*Fig. 46).*

404 Diffraction of X-rays in Crystals §98
The maximum intensity in the spot occurs for a direction of k’ for which the difference
k’—(k+2nb) has its least magnitude (so that the integral in (97.13) has its maximum
value). The magnitude of the difference of two vectors, one of which is arbitrary in direction, has its least value when they are parallel. Hence, since k’ = k, we have
[k’—k —2b|min = k—|k-+27b]
_ Ba(k+20b)?
~ hele 2ab]
pb
%o,
arb
Fic. 46
Since k is close to ko and we are considering the region near the maximum, k’ = k+27b
and the denominator can be replaced by 2k. In the numerator, we expand the squared
parenthesis and obtain
2k -2nb—(2nb)? = [—2ko-2nb—(2ab)"]—2nb-2nb = —4nnb2,
‘Thus |k’—k—2nb|min = —2anb?/k.
Next, we put
2Qanb?
k= (e+ 20b)(1— Pe) a,
and take the z-axis in the direction of k+27b. This reduces the problem to the calculation
of the integral (cf. the derivation of formula (97.19))
J face dey] f exp(2arinb®/k—2 i'r} AV |?
sin (anb®Z/R) 2
= ff dre as}f ene a| .
Finally, using formula (97.18), we obtain
2n2/ ef sin? (wnb?Z/R)
pect a) 29)[n,|2 | —————- df.
on Fees) Creat (ai a
As 7 0 this formula becomes (97.19). If #b®Z/k5> 1 (which is compatible with 7 <1),
the squared sine can be replaced by its mean value 4, and we have
2 2 1+cos%9
o= (Fa) as
where S is the area of the “shadow”, i.e. the projection of the body on the xy-plane.

## Section §98: The integral intensity

The formulae derived in §97 give the diffracted intensity when a plane
wave of a single frequency is incident on a crystal. Let us now consider
some cases where these conditions are not fulfilled.

§98 The integral intensity 405

First, let the incident wave be plane but not of a single frequency,f its
spectral resolution including waves with wave vectors k whose directions are
the same but whose magnitudes k = w/c are not. Let p(k) be the frequency
distribution of the incident radiation intensity, normalised by the condition
fo(k) dk = 1.

The total intensity of the diffraction spot is determined by the effective
cross-section, which is obtained by multiplying the expression (97.13) by
p(k) and integrating with respect to o’ and k:

1/ e \2 2
o= (5) |npl2 f f | f exp[— i(k’ - k— 2nb)-a]aP | x
2\me2,
x (1 + cos? 9)p(k)do’dk. (98.1)

We put temporarily K = k’—k—2zb and write the squared modulus as a

double integral:
| [ exp(-iK-x)avpe = ff exp [K-(re — n1)]dVidV2.
Using instead of r; and r2 the variables 4(r1+-r2) and r = rp—r, and integrating with respect to the first gives | fexp(@K-r) dV? = V fexp(K-r) dV. In
the remaining integral we can effect the integration over all space,t and the
result is
| [ exp @K-x) dV? = (2n)378(K). (98.2)
Substituting this result in (98.1), we obtain
e@\2
o= 4n0(<) \mol2V(1 + cos? 9p) x
x ff 8(e’ — k — 2nb)o(h) do’ dhs (98.3)
on account of the presence of the delta function, the factor 1+ cos? > in the
integrand can be replaced by its value at 9 = %, where 9o is the angle
between the k and k’ which satisfy Laue’s condition (denoted by kp and
k’o = ko+2zb).

The integration with respect to o’ can be carried out by noticing that it

is equivalent to an integration with respect to
dk’ = k'2dk' do’ = 4k’ d(k’2) do’,

+ Corresponding to Laue’s method in the X-ray analysis of crystals.

1 ‘This is possible because we require only the total intensity of the diffraction spot, and
not its width.

406 Diffraction of X-rays in Crystals §98
if an additional factor (2/k)8(k’2 — 2) is included in the integrand. Thus the
integral in (98.3) becomes
2
f i zoe — k — 2mb)5(k’? — k®)p(k) dk’ dk.
Effecting the integration with respect to k’ by means of the first delta function, we can replace k’2 by (k+27b)? in the second delta function, and the
result is
2 1
J = 8(412b2 + 4arb-k)p(k) dk = fangotot + 7b2)p(k) dk,
k 2nk
so that
e \2 1
o= 2ne(-<) |ngl2V(1 + cos? 90) f gblb-k + mbt)p(R)dk. (98.4)
me’

Finally, we have to carry out the integration over k (the direction
n=k/k being given). The argument of the delta function is zero for
k = ho, and the integral is p(ko)/ko|b-n| = p(Ro)/|b-ko| = p(Ao)/7b2. Thus

2 \ 2
ao 2n(<) |nvl2V(A + cos? 9o)p(ho)/02. (98.5)
me
Let us now consider another case, where the incident wave is of a single
frequency but its components have varying directions of k which differ by
rotation about some axis;} let 1 be a unit vector along that axis, and y the
angle of rotation about it. Let p(y) be the angular distribution of the incident
radiation intensity, normalised by the condition

Qn
Je(b)dy = 1.

The calculations leading to formula (98.4) are valid in this case also,
except that the integration with p(k) dk must be replaced by one with
p(y) dy: 7 Lo

c= 2n0(<) |nv|2V/(1 + cos? $0) f qilb-k + ab?)p(p) dy. (98.6)
me’
We again denote by ko the value of k for which the argument of the delta
function is zero, and measure % from the plane of 1 and ko. For small ,
k = ko+(Ixko)y. Then the integral in (98.6) becomes
1
J {2-4 > kod)e(d) a = p(0)/b-1 > a)
= p(0)/A2[b-1 x mol
= p(0) sin? (}90)/n62|b-1 x no].

+ Corresponding to Bragg’s method (the rotation method) in X-ray analysis. The rotation

referred to is that of the crystal about I, not that of the direction of k.

§99 Diffuse thermal scattering of X-rays 407
Thus
: ( =) sin? 490(1 +-c0s89o)[ml27 2 (98.7)
= —(——] sin’ + ———, 7
o= a =) sit cos?$p)|n9| [b-lx nal

Finally, let us consider the diffraction of a plane wave, of a single frequency, from a body consisting of crystallites arranged at random.t

Let k’o and bo be values of k’ and b such that Laue’s condition
k'p = k+2mbp is satisfied. The directions of k’g and bo are not uniquely
determined, since Laue’s condition is, of course, still fulfilled when the
triangle k, 2mbo, k’o is rotated about the direction of k. Thus the principal
maximum corresponds to directions of k’ occupying a conical surface of
vertical angle 299. Instead of a diffraction “spot” we now have a “ring”.

The required total effective cross-section is determined by a formula which
differs from (98.4) only in that the integration with p(k) dk is replaced by
an averaging over the directions of b:

e \2 1 do»
o= av() |np|2(1 + cos?) fee m0, (98.8)
mez k 4n
where do, is an element of solid angle about the direction of b. Denoting
by « the angle between k and b, we can write the integral in (98.8) as
1 2nd cosa 1 1
= —— = —— sin?
f pk cone +-nbt}—— = ope = pace sin? 499.

Each of the three cases considered in this section corresponds to a particular
method of averaging the diffraction pattern. The dependence of the total
averaged diffraction intensity on the volume of the body reduces, as we
should expect, to a simple proportionality. In the pattern which is not
averaged, the intensity and its distribution over the spot depend more
markedly on the volume.

## Section §99: Diffuse thermal scattering of X-rays

In §§97 and 98 we have taken n(x, y, z) to be the time average electron
density in the crystal: various density oscillations were thereby excluded,
and consequently so was the corresponding (non-coherent) scattering of
X-rays. One cause of non-coherent scattering is the thermal fluctuations of
density. This scattering is ‘‘diffusely” distributed in all directions, but it is
characterised by a relatively high intensity near directions corresponding to
the sharp lines of the “structural” scattering described in the preceding
sections. Here we shall discuss these maxima of the thermal scattering
(W. H. Zacuartasen, 1940).

The thermal oscillations of the crystal lattice can be represented as combinations of ‘‘sound” waves. As we shall see, the maxima of the thermal
scattering arise from wavelengths large compared with the lattice constant.

+ Corresponding to Debye and Scherrer's method (the powder method) in X-ray analysis.

408 Diffraction of X-rays in Crystals §99
The change in the electron density due to such a wave can be regarded, at
any point, as due to a simple displacement of the lattice by an amount equal
to the local value of the displacement vector u in the wave. Thus the change
in the density (not averaged with respect to time) when a given sound wave
passes can be expressed in terms of the mean density by
82 = n(r—u)—a(r) = —u- on/or.

In considering diffuse scattering near a given line, we must replace n by
n, exp(2mib-r) with the appropriate b, so that

6n = —2mib-um, exp(2zib- r). (99.1)

The scattering by density fluctuations is, of course, not coherent with that
by the mean density, and the two therefore do not interfere. Hence the
effective cross-section for diffuse scattering can be obtained from (97.10),
substituting 5” for n and then carrying out the statistical averaging over
fluctuations:

e@ \2
do = 2n(=) |ns|2(1 + cos®s) x
me?

x | J b-uexp(—iK-r)dV[2 do’, (99.2)
where K = k’—k—2zb. The scattered intensity is large for directions where
K < 2nb.

The integral { uexp(—iK-r) dV gives the Fourier space component of u
whose wave vector is K, and we can therefore take u to be simply the displacement vector in a sound wave having this wave vector. The inequality
K < 2b therefore implies that the wavelength of the scattering sound wave
is large compared with the dimension of the crystal lattice cell.

Thus we can put

u = 4[u exp(iK - r)+ uo* exp(—iK - r)], (99.3)
so that {(b-u) exp(—iK-r) dV = }Vb-up and the effective cross-section is
mye \2
do = (Ss) |mp!2(1 + cos®9)bybxuoiton V2 do’. (99.4)
2\ me%

The products of the components of up are averaged as in §96 for a sound
wave in an isotropic medium. The elastic energy per unit volume of a
deformed crystal is }Aizzmtixtim, Where ux is the strain tensor and Axim the
elastic modulus tensor.t Hence the mean elastic energy of the whole crystal
is 1V\ermuixtim. We substitute

( buy + =)
ux = -| —+—
kod 2\ dxp~ Oxy
= fre {((iKxuor+iKiwox) exp(iK - r)}.
t See Theory of Elasticity, §10, Pergamon Press, London, 1959.

§99 Diffuse thermal scattering of X-rays 409

| ,
The terms containing exp( + 2/K-r) give zero on averaging. Using also the
symmetry of the tensor Aj1m with respect to interchange of i, k, or J, m, or

| 2, k and J, m, we obtain 4V AmKyKmuoittor* or $V gixuoitiox*, where

ge = AnnmKiKm- (99.5)

According to the general theory of thermodynamic fluctuations, we can at

once write down the required mean values:
uoiton* = (4T/V) gtx, (99.6)
| where g-14 is the tensor inverse to gj, and the effective scattering crosssection is
er \2
do = 2ne(<) TV |ny2(1 + cos? B)bibeg-tix od’. (99.7)
me’

Thus the diffusely scattered intensity is, as we should expect, proportional

| to the volume of the crystal. A characteristic feature of this scattering is the
way in which its intensity is distributed over the area of the spot. Apart
from the factor 1+cos? $, which is almost constant for a given spot, the
intensity is given by the expression g-1,4b4bz. This expression is the product
of 1/K2 and a fairly involved function of the direction of the vector K with
respect to the crystal axes. For scattering near a principal maximum the
diffusely scattered intensity is itself a maximum where K = 0 (the expression (99.7) becomes infinite for K = 0 and is, of course, invalid). If the
condition (97.15) b-k = —7? is not satisfied, however, K cannot be zero,
and the maximum of the diffusely scattered intensity lies at some K different
from zero, which in general does not coincide with the maximum of the
structural scattering. In either case the diffuse scattering forms a background
whose intensity falls off essentially as 1/K2, that is, considerably more
slowly than the intensity in the sharp structural-scattering line superposed
upon it,

t See Statistical Physics, §110. If the probability distribution for fluctuating quantities
x1, x2, ... is of the form exp(— 4Auxexe), then xexr = X1y. A factor 2 in (99.6) appears
because each of the complex uo: involves two independent quantities.

a7*

APPENDIX
CURVILINEAR CO-ORDINATES
We give below, for reference, certain formulae relating to vector operations
in curvilinear co-ordinates, both general and particular.

In an arbitrary system of orthogonal curvilinear co-ordinates 1, ue, us,
the squared element of length is d/? = hj? duj2+hg®dus?+ hg? dug’, where
the /; are functions of the co-ordinates. The element of volume is

dV = hyhehg dus due dug.
The various vector operations can be expressed in terms of the functions
hy as follows. For vector operations on a scalar:
1 of
df) = - >
(grad f): Ih bun
1 0 (hohs of )
AS iciigD Bas han)
where the summation is over cyclic interchanges of the suffixes 1, 2, 3. For
vector operations on a vector:
1 7
divA = ——~— > ——(heh3Ai),
ao Iyhohs > oun ae)
(curl A) 1 [tiny ~-(inAs)|
cur! =| -— .
a pare irae a
The remaining components of curl A are obtained by cyclic interchanges
of the suffixes.

Cylindrical co-ordinates 1, $, 2.

Element of length: d/2 = dr? + r2 dg? + d2?;

hp = 1, ger, he = 1.

Vector operations:

107 1 ef af
at- 5%) * aap te
14 160A, 0Az
Pe 5 EC yes ei er cel,
divA Aree Ir) + 7 Ob + de

Curvilinear Co-ordinates 411
104, ay
(eu = ap ae"
1A), = 0A, 0Az
(outs = Sat
1a 1 0A,
1A), = -— -==p
(curl A): ror (As) r 0d
4 A 2 ae
(AA) = A I Ee ap
446 2 ode
(AM = AAs a aap”
(AA): = AA:
In the expressions for the components of AA, AA; signifies the result of
the operator A acting on A; regarded as a scalar.
Spherical co-ordinates r, 9, $.
Element of length: d/2 = dr? + 72 dé? + 72 sin? 6 d¢?;
hy = 1, hg = 1, hg = rsin@.
Vector operations:
13, a 1 a;. a 1 a
= ——_{p ee 6 4,
ara al” a) + ind wal a) + a sinte 242”
ld) 1 @ 1 0A
divA = ——(r2A,) + ———(Ag si +
- r rad 1) + in 20 osin®) + 0 ob
1 a) 0A
(curl A), = ale sin 6) — arab
rsin6L06 Op
1 0A 10a
(curl A), = ———" - -—(rA,),
rsin@ 06 =r ér
1p a OAr
IA), = -|— ———
(curt), = [ay - I],
2 1 2@ 1 0A,
A)y = AA, - —] A, + ———(Ag sin ® <5 3|
(AA = Ad al r+ Fn 060 9199) + oo ap
270A, Ay cos? dA,
A) = A4p+ | —
ee oe aL 2 2sin?O sin?O Op |
2 7a, a4, Ay
A), = AAs + ———|—— + cot —— —- —*_}.
(Aa) = 4 + zanal yeaa) rel

INDEX
Absorption coefficient, 265 Contact potential, 100
Absorption of electromagnetic waves by Cotton—Mouton effect, 336
small particles, 303£. Critical field, 1734.
Acceleration, excitation of currents by, 210ff. Critical opalescence, 393ff.
Airy function, 286 Critical state, 82f.
Anisotropic media, electromagnetic waves Crystals
in (XI), 313ff. biaxial, 59, 324ff.
Antiferromagnetic Curie point, 165f. dielectric properties of, 58ff., 313ff.
Antiferromagnetics, 117 enantiomorphic, 341
magnetic properties of, 116ff.
Barnett effect, 144 natural optical activity of, 341f.
Binormal, 326 piezoelectric, 76
Biot and Savart’s law, 122 pyroelectric, 60
Biradial, 326 uniaxial, 59, 321ff.
Black-body radiation in a transparent negative, 322
medium, 367£. positive, 322
Bragg and Vul’f’s equation, 401 X-ray diffraction in (XV), 398ff.
Bragg’s method, 406n. general theory of, 398ff.
Brewster angle, 276 Curie point
antiferromagnetic, 165f.
Capacity, 4, 8£., 19. 62, 202. ferroelectric, 83
coefficients, 4, 6, 8 ferromagnetic, 146
of conducting ellipsoid, 24f. Curie-Weiss law, 148
of conducting sphere, 62 Current
mutual, 8, 17 boundary conditions for, 92f.
Causality, 257, 260 conduction, 120
Charge distribution constant (III), 92ff.
on conducting disc, 27, 28 magnetic field of, 119ff.
on conducting ellipsoid, 24, 28 in a crystal, 398
‘on conductors, 1ff., 18 density, 92
Charges eddy, 1894.
in a dielectric, 68 electric, 1
extraneous, 37 excitation by acceleration, 210ff.
Cherenkov radiation, 357. linear, 122; see also Linear current
Conduction current density, 120 molecular, 120n.
Conductivity, electrical, 92 in a moving conductor, 206
tensor, 93, 96 superconductivity, 169ff.
Conductors, 1ff. surface, 115
cylindrical, 16, 17, 18, 125, 194 Curvilinear co-ordinates, 410£.
disc-shaped, 27, 28 Cylinder
electrostatics of (I), 1ff. conducting, 16, 17, 18, 125, 194
electrostriction of, 33f. dielectric, 43, 57, 58
ellipsoidal, 20f.
forces on, 31ff., 62, 142ff., 221 Debye relaxation time, 392
motion in a magnetic field, 205ff. Debye and Scherrer’s method, 407n.
turbulent, 234ff. Demagnetisation coefficients, 44n., 169
spherical, 15f., 34£., 95f., 193ff., 209f., 212 Depolarisation coefficients, 26f., 302
Conformal mapping, 14 Depolarising field, 44n.
method of, 12ff. Dielectric axes, principal, 316
Conical refraction Dielectric constant, see Dielectric permeaexternal, 328 bility
internal, 326, 328 Dielectric crystals, 58ff., 313ff.

414 Index
Dielectric cylinder, 43, 57 Eikonal, 269, 317
Dielectric disc, 43, 57, 58, 62 Finstein—de Haas effect, 145
Dielectric ellipsoid, 42ff., 56f. Elastic constant tensor, 75
Dielectric fluid, forces in, 64%. Elastic-optical constants, 330
Dielectric permeability Electric displacement, 37n.
analytical properties of, 256ff. Electric field, constant
of crystals, 313ff. of conductors, 1ff.
dispersion of, 247. boundary conditions, 2f., 39f., 92
electrostatic, 38 energy of, 3ff.
at high frequencies, 251 in dielectrics, 36ff.
at low frequencies, 250 boundary conditions, 37ff.
of a mixture, 45ff. thermodynamics of, 47ff.
spatial variation of, 337. See also Electromagnetic field
tensor, 58, 69ff., 329ff., 339, 385f. Electric induction, 37
Dielectric polarisation, 36 Electric moment, 37
Dielectrics, 1 Electrocaloric effect, 56ff.
electrostatics of (II), 36ff. Electrocapillarity, 103f.
electrostriction of isotropic, SSff. Electromagnetic field
moving, 243ff. boundary conditions, 273, 280£., 290
boundary conditions, 245¢. fluctuations, 361ff.
thermodynamics of, 47ff. in moving media, 243ff.
total free energy of, 52. quasi-static (VII), 186ff.
Dielectric solid, forces in, 69ff. in dielectrics, 239ff.
Dielectric sphere, 42f., 45, 61, 62, 73, 246f. variable, 247ff.
Dielectric susceptibility, 38 Electromagnetic fluctuations (XIII), 360.
sign of, 63f, Electromagnetic wave equations (IX), 239f
Dielectric tensor, 58; see also Dielectrie Electromagnetic waves, 239ff.
permeability tensor absorption of, by small particles, 303f.
Diffraction in anisotropic media (XI), 313ff.
by a plane screen, 308ff. extraordinary, 322ff.
by a wedge, 304ff. ordinary, 322
of X-rays in crystals (XV), 398ff. plane
general theory of, 398ff. in an absorbing medium, 264f.
Diffusion phenomena, 110ff. in anisotropic media, 3158.
Dipole moment homogeneous, 264
of conducting cylinder, 16, 18f. inhomogeneous, 263
of conducting disc, 28 of a single frequency, 263ff., 268
of conducting sphere, 16 in a transparent medium, 264
of conductor, 7 propagation of (X), 269f.
of dielectric, 36f., 54 in an inhomogeneous medium, 284ff.
Disc in waveguides, 293ff.
conducting, 27, 28 reflection and refraction of, 272ff., 283f.
dielectric, 43, 57, 58, 62 in resonators, 290ff.
superconducting, 173 scattering of (XIV), 377ff.
Discontinuities in a magnetic fluid, 224ff. by small particles, 299ff.
Discontinuity Electromotive force, 101
contact, 225 Electrostatic induction coefficients, 4, 6
rotational, 226ff. Electrostatics
tangential, 225ff. of conductors (I), 1ff.
stability of, 2274. of dielectrics (II), 36ff.
Dispersion relation, 220 Electrostriction
Displacement, electric, 37n. of conductors, 33ff.
Dissipative function, 204 of dielectrics, 55f.
Domains, 87ff., 152ff., 158ff., 179ff. Ellipsoid
Double circular refraction, 335 conducting, 20ff.
Double refraction, 323 dielectric, 42ff., 56f.
in an electric field, 329ff. ferromagnetic, 157f.
superconducting, 169f., 182
Easy magnetisation, direction of, 150 Ellipsoidal co-ordinates, 20ff.
Eddy currents, 189. Em. 101

Index 415
Energy Image, 9
of conductors, 3ff., 124 force, 10, 40
of a system of currents, 131ff. Images, method of, ff.
of dielectrics, 48ff., 52ff., 79ff. Impedance, 197ff.
of fields in dispersive media, 253ff. matrix, 201
flux (Poynting vector) 124, 191, 242, 253, __ surface, 280ff., 314f.
271, 274, 280, 314 Inductance
in a plane wave, 264, 315f. mutual, 132
in a resonator, 291f. self-, 132
in a waveguide, 295f. Induction
free self-, 132 electric, 37
interaction, 132 extraneous fluctuating, 361
of magnetic substances, 129ff., 149ff., 156, correlations of, 363ff.
15948, unipolar, 2088.
Ettingshausen effect, 109 Inversion
E waves, 2858, 294ff. method of, 11f.
Extinction coefficient radius of, 12
differential, 384 transformation, 12
total, 384 Tonisation losses by fast particles, 344f.
Extraneous charges, 37 relativistic, 3494.
Extraordinary waves, 322ff.
| Joule’s law, 93
Faraday effect, 338 in a moving conductor, 206
Faraday’s law, 207 Kerr effect, 329
Fast particles, passage of through matter Kinetic coefficients, 94
(XII), 344ff. symmetry of, 94, 96, 314, 331, 3386.
Fermat's principle, 270 Kramer’s and’ Kronig’s formulae, 259ff.,
Ferroelectric axis, 83 282f,
Ferroelectrics, 834.
domains in, 87. Laue’s equation, 401
Ferromagnetics, 117, Laue’s method, 405n.
near the Curie point, 146ff Leduc-Righi effect, 109
domain structure of, 152ff., 158ff. Linear currents, 122ff., 133ff., 197ff., 210,
thermodynamics of, 147 12
Ferromagnetism (V), 146ff. fluctuations of, 360f.
Fluctuations mutual inductance of, 133
of anisotropy, 388 self-inductance of, 136ff.
of current in linear circuits, 3608. Lorentz condition, 350
electromagnetic (XIII), 360f. Losses 2
electromagnetic field, 361ff. a
Fresnel ellipsoid, 321 magnetic, 254
Fresnel’s equation, 317, 324ff. >
Fresnel’s formulae, 2734. Magnetic anisotropy energy, 146n., 148n.,
14988.
Ct Magnetic crystal classes, 118
Geometrical optics, 2694. Magnetic field, 114
Group velocity, 220, 270, 318 boundary conditions, 115, 187f.
Gyration vector, 333n., 339 conductor moving in, 205ff.
Gyromagnetic coefficients, 145 constant (IV), 1134.
| Gyromagnetic phenomens, T14f- eed pee in, 21368
Gyrotropic media, 319n., 5326 forces on matter in, 1414f., 221
thermodynamics of, 126f.
Hall effect, 97 See also Electromagnetic field
Hall’s constant, 98 Magnetic fiuid dynamics (VIII), 213ff.
H waves, 285, 287£., 2948. Magnetic flux, 134
Hydromagnetic waves, 221n. Magnetic induction, 113
absorption of, 223 Magnetic moment, 114
Hysteresis, 151 in variable field, 252

416 Index
Magnetic-optical effects, 331ff. Potential
Magnetic permeability, 114 contact, 100
analytic properties of, 262 electric
of crystals, 313 complex, 13
dispersion of, 251ff. scalar, 2f., 350
tensor, 119 vector, 13, 350
Magnetic polarisability tensor, 192 magnetic, vector, 120
Magnetic space groups, 117 Powder method, 407n.
Magnetic structure, 116 Poynting vector, see Energy flux
Magnetic susceptibility, 114f. Principal section, 322
sign of, 115, 129 Principal waves in waveguides, 296ff.
Magnetisation, 114 damping of, 2974.
by rotation, 1446. Pyroelectricity, 60f.
regions of spontaneous, 152
Magnetoelastic energy, 156
Magnetostatics and clectrostatics compared, Quadrupole moment tensor, 28
115, 116, 126ff., 1416, 146 of conducting ellipsoid, 28
Magnetostriction, 155f. Quality of a resonator, 292n,
Mandel’shtam-Brillouin doublet, 390 Quasi-static fields, 186, 364
Maxwell effect, 331
Maxwellian relaxation time, 392
Maxwell’s equations, 2, 113, 315, 349 Raman-Landsberg-Mandel’shtam effect,
Maxwell stress tensor, 31 387
Mechanical-optical effects, 330f. Ray surface, 317ff.
Molecular attraction between solid bodies, Ray vector, 317ff.
368ff. Reactance, 198n.
Momentum density, 242 Reciprocity theorem, 289£.
Mutual inductance, 132 Reflection coefficient, 274, 277ff., 283¢.
Refractive index, 264, 265, 269, 316n., 322,
Natural optical activity, 248n., 337ff. oe 198n.
of crystals, 341f. complex, 197
Nernst effect, 109 Resonators, 2904.
quality of, 292n.
Ohm’s law, 92, 200 Rotation method, 406n.
Optical axis, 321, 326
Optical frequencies, 248
Optical ray axis, 326 Scattering
Ordinary waves, 322 in amorphous solids, 395ff.
Oscillator strength, 261 anti-Stokes, 377
antisymmetrical, 383
combination, 387
Peltier coefficient, 108 effective cross-section for, 300ff.
Peltier effect, 107£. of electromagnetic waves (XIV), 377ff.
Penetration depth, 189, 279f. by small particles, 299ff.
in a superconductor, 167 by fluctuations, 388ff.
Phase velocity, 219, 270 principle of detailed balancing for, 383 ff.
Piezoelectricity, 60n., 70n., 73ff. Rayleigh, in gases and liquids, 387ff.
Piezoelectric tensor, 74, 76ff. scalar, 383
Piezomagnetism, 119 with small change in frequency, 385ff.
Polarisability tensor, 7£., 192 Stokes, 377
Polarisation, 36 symmetrical, 383
coefficient, 38 Self-inductance, 132
of dielectric in variable field, 249 of linear circuits, 136ff.
of electromagnetic waves in anisotropic _of superconductors, 171
medium, 319ff. Shock waves in a magnetic fluid, 229ff.
in geometrical optics, 271 weak, 231
in gyrotropic medium, 335ff. in weak magnetic fields, 231f.
in uniaxial crystal, 323 Skin effect, 136n., 195ff.
Ponderomotive forces, 64 Solenoid, 137, 140f.

Index AIT
Sphere ‘Thomson’s theorem, 7
conducting, 15f., 34f., 62, 95, 193ff, Total polarisation, angle of, 276
2098., 212 ‘Total reflection, 277
dielectric, 42£., 45, 61, 62, 73, 246f. angle of, 277
Spheroidal co-ordinates ‘Transparency ranges, 254
oblate, 22 ‘Transparent media, 266ff.
prolate, 22 black-body radiation in, 367f.
Stewart-Tolman effect, 212 ‘Turbulence in conducting fluid, 234ff.
Stimulated emission, 377n. ‘Two-dimensional field, 12f.
Stopping power, 346
Stress tensor, 65ff., 70f. i imducti
Sumercondoctivity (VI), 1674 Unipolar induction, 208f.
eater Velocity of light in moving medium, 271,
Superconductors
critical field in, 1734. Waveguides, 2934.
currents in, 168ff. Waves
ellipsoidal, 169f., 182 on a charged liquid surface, 35
impedance of, 281f. electric-type, 294
intermediate state of, 179ff. electromagnetic, see Electromagnetic
magnetic properties of, 167ff. waves
multiply connected, 170ff. extraordinary, 322ff.
rotating, 212 hydromagnetic, 22in.
self-inductance of, 171 absorption of, 223
thermodynamics of, 173ff. magnetic-type, 294
ordinary, 322
‘Telegrapher’s equation, 298 principal, 296
‘Tensor ellipsoid, 59n. shock, see Shock waves
‘Thermodynamic inequalities, 81ff. Wave-vector surface, 317ff., 322, 324ff.,
‘Thermoelectric phenomena, 104ff. 334n.
‘Thermoelectromotive force, 108 Wedge problem, 14f.
‘Thermogalvanomagnetic effects, 109f. Work function, 99
‘Thomson coefficient, 107
| ‘Thomson effect, 107 X-ray diffraction in crystals (XV), 398ff.
Thomson’s formula, 203 general theory of, 398ff.
Thomson's relations, 108 X-rays, diffuse thermal scattering of, 407ff.

: THE JOURNAL OF THE
FRANKLIN INSTITUTE
The Journal of the Franklin Institute
covers the traditional branches of
mathematics and the physical sciences,
both pure and applied, as well as the new
composite sciences, combining two or
more disciplines. Dedicated to honour
Ben Franklin, America’s great inventor,
writer and scientist, the journal provides
a platform for the dissemination of
« scientific ideas and research, and draws
its authors and readership from more than
sixty countries throughout the world.
Major papers describing theoretical and
experimental researches are accepted for
publication on the basis of their lasting
value. The journal also publishes brief
communications of exceptional interest
and reviews a number of current books in
each issue.
Demonstrating the extreme flexibility of
the editorial policy, special issues have
been published on topics that are timely
and fall within the broad range of interest
of the journal.
Since its initial publication in 1826, the
journal has proved its ability to relate to
the times by bridging the gap from one era j
to another, becoming one of the most 7
highly respected publications in the
world of science and engineering. © ’
Today, the Journal of the Franklin
/nstitute remains as relevant, for present
and future generations of scientific
workers, as it was for its founders, almost
fifteen decades ago.
Write for a specimen copy of the
latest issue and details of related
Pergamon journals.
Pergamon Press
Headington Hill Hall, Oxford OX3 OBW
Maxwell House, Fairview Park,
Elmsford, New York 10523.
207 Queen's Quay West, Toronto 1
19a Boundary Street, Rushcutters Bay,
NSW 2011, Australia
Vieweg & Sohn GmbH, Burgplatz 1,
Braunschweig
Printed in Great Britain/Bradley

- COURSE OF THEORETICAL PHYSICS pS
by L. D. LANDAU (Deceased) and E. M. LIFSHITZ saab
Institute of Physical Problems, USSR Academy of Sciences
The complete Course of Theoretical Physics by Landau and Lifshitz, recognized as two of the world’s
outstanding physicists, is being published in full by Pergamon Press. It comprises nine volumes, .
covering all branches of the subject; translations from the Russian are by leading scientists.

Typical of the many statements made by experts, reviewing the series, are the following :
“The titles of the volumes in this series cover a vast range of topics, and there seems to be little in
physics on which the authors are not very well informed.” Nature
“The remarkable nine-volume Course of Theoretical Physics . . . the clearness and accuracy of the
authors’ treatment of theoretical physics is well maintained.”
Proceedings of the Physical Society
Sapte ee eS
Of individual volumes, reviewers have written :
MECHANICS
“The entire book is a masterpiece of scientific writing. There is not a superfluous sentence and the (@) rr
authors know exactly where they are going. . . . It is certain that this volume will be able to hold its =
own amongst more conventional texts in classical mechanics, as a scholarly and economic exposition (eo) @O
of the subject.” Science Progress
QUANTUM MECHANICS (Non-relativistic Theory) : a } (a)
“.., throughout the five hundred large pages, the authors’ discussion proceeds with the clarity and loan eo
* succinctness typical of the very best works on theoretical physics.” Technology mame =
FLUID MECHANICS =] (eo)
“The ground covered includes ideal fluids, viscous fluids, turbulence, boundary layers, conduction Sc
and diffusion, surface phenomena and sound. Compressible fluids are treated under the headings of Qe.
shock waves, one-dimensional gas flow and flow past finite bodies. There is a chapter on the fluid (eo)
dynamics of combustion while unusual topics discussed are relativistic fluid dynamics, dynamics of ~<
superfluids and fluctuations in fluid dynamics . . . a valuable addition to any library covering the (=
mechanics of fluids.” Science Progress ~ =
THE CLASSICAL THEORY OF FIELDS (Second Edition) pe¥)
“This is an excellent and readable volume. It is a valuable and unique addition to the literature of
theoretical physics.” Science
“The clarity of style, the concisement of treatment, and the originality and variety of illustrative problems <
make this a book which can be highly recommended.” Proceedings of the Physical Society me
STATISTICAL PHYSICS on
“ _. stimulating reading, partly because of the clarity and compactness of some of the treatments put QO. (7, )
forward, and partly by reason of contrasts with texts on statistical mechanics and statistical thermo- =e
dynamics better known to English sciences. . . . Other features attract attention since they do not
always receive comparable mention in other textbooks.” New Scientist eY) (eo)
THEORY OF ELASTICITY bm |
“| shall be surprised if this book does not come to be regarded as a masterpiece.”
Journal of the Royal Institute of Physics (now the Physics Bulletin)
“the book is well constructed, ably translated, and excellently produced.”
Journal of the Royal Aeronautical Society
ELECTRODYNAMICS OF CONTINUOUS MEDIA
“Within the volume one finds everything expected of a textbook on classical electricity and magnetism,

: and a great deal more. It is quite certain that this book will remain unique and indispensable for many
years to come.” Science Progress
“The volume on electrodynamics conveys a sense of mastery of the subject on the part of the authors
which is truly astonishing.” Nature

Ge
Sat
08 0160190 Pergamon
-% J

---


---

*Notes generated from: Landau & Lifshitz, "Electrodynamics of Continuous Media", Pergamon Press*

## 中文翻译

> **中文：** 第XIV章——电磁波动方程。

### 主要内容
本章详细讨论各种条件下的电磁波动方程求解，包括有源区、波导和谐振腔中的波动方程。

### 关键概念
- **波导中的电磁波**：金属波导支持TE（横电）和TM（横磁）模式，截止频率$f_c = c/(2a)$（矩形波导TE$_{10}$模）
- **谐振腔**：封闭金属空腔支持的驻波模式，具有离散的谐振频率
- **格林函数(Green's Function)**：用于求解有源波动方程
- **辐射条件**：无穷远处的索莫菲辐射条件
- **惠更斯原理**：波前上的每一点都是次级球面波源

### 应用
微波传输线设计、谐振腔设计、天线辐射分析、电磁兼容。

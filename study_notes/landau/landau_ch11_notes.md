# Landau & Lifshitz《Electrodynamics of Continuous Media》第11章

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter XI: Scattering and Diffraction

THE PASSAGE OF FAST PARTICLES THROUGH
MATTER

## Section §84: Ionisation losses by fast particles in matter: the non-relativistic

case

A rast charged particle, in passing through matter, ionises the atoms and
thereby loses energy.t In gases, the ionisation losses can be regarded as
being due to collisions between the fast particle and individual atoms. In
a solid or liquid medium, however, several atoms interact simultaneously
with the particle. The effect of this on the energy loss by the particle can
‘be macroscopically regarded as resulting from the dielectric polarisation of
the medium by the charge. Let us first consider this effect for non-relativistic
velocities of the particle. We shall see that the polarisation of the medium
then has only a slight effect on the losses. The derivation of this result is |
of interest because the method can be extended to other cases.

Let us first of all ascertain the conditions under which the phenomenon
can be macroscopically considered. The spectral resolution of the field
produced at a distance r from the path of a particle moving with velocity v
consists chiefly of terms whose frequency is of the order v/r (the reciprocal
of the “collision time”). The ionisation of an atom can be effected by field
components of frequency w 2 wo, where wo is some mean frequency corresponding to the motion of the majority of the electrons in the atom. The
particle therefore interacts simultaneously with many atoms if v/«p is large
compared with the distances between the atoms. In solids and liquids
these distances are of the same order of magnitude as the dimension a of the
atoms themselves. Thus we obtain the condition v > aw, i.e. the velocity
of the ionising particle must be large compared with the velocities of the
atomic electrons (or at least of the majority of them).}

Let us now determine the field produced by a charged particle moving
through matter. In the non-relativistic case it is sufficient to consider only
the electric field, defined by the scalar potential ¢. This potential satisfies

. Poisson’s equation
eAd = — 4nedi(r — ve), (84.1)

+ We speak, as is customary, of “ionisation losses”’, but these are, of course, understood
to include losses due to the excitation of atoms to discrete energy levels.

t The corresponding condition for the energy E of the particle is E5> MI/m, where M is
the mass of the particle, m that of the electron, and J some mean ionisation energy for the
majority of the electrons in the atom.

§84 Ionisation losses by fast particles in matter 345
in which the “dielectric constant” is written as an operator, and the expression e3(r—vé) on the right-hand side is the density due to a point charge e
moving with constant velocity v.}
We expand ¢ as a Fourier space integral:
¢= f dx exp (ik-r) dk. (84.2)
Taking the Laplacian of this equation, we have
©
Ag = — f dub? exp (ik-r) dk,
whence it is seen that the Fourier component of Ad is (Ad)x = —Fdy.
‘Taking the Fourier component of equation (84.1) gives
1
(Ade = -B i} 4ne5(e — vt) exp (— ike-r) dV
: itv
pg HPC
Thus é, = (e/27?k?) exp (—itv-k), and ¢, therefore depends on time
through a factor exp (—itv-k). The operator @ acting on a function exp (—iw#)
multiplies it by «(w). Hence
e
= ———_—__ exp (~ itv-k).
$e = FaRiellen) OP
The Fourier components of the field and of the potential are related by
E,, exp (ik-r) = —grad [¢, exp (ik-r)] = —ik¢y exp (sk-r), or E, = —ikd,.
Thus
E ied ity +k 4.3)
HF ate(eewy) OPC HY )e (84.3)
The total field strength is obtained by inverting the Fourier transform:
E = Bxexp(ik-r) dk. (84.4)
The energy loss by the moving particle is just the work done by
the force eE exerted on the particle by the field which it produces. Taking
the value of the field at the point occupied by the particle, namely
+ We assume that the particle moves in a straight line, and thereby neglect scattering, as
is always permissible in problems of this type.
If the charge on the particle is ze, then all the formulae pertaining to energy loss in this
and the following sections should be multiplied by 22.

346 The Passage of Fast Particles Through Matter §84
r = vt, we obtain in the integrand in (84.4) a factor exp (itv-k) which
cancels with the factor exp (—itv-k) in the expression (84.3) for E,. Hence
the force F is
©
r--< J * at
"One J Re(kkev)
—o

It is evident that the direction of the force F is opposite to that of the
velocity v; let the latter be the x-direction. Puttingkyv = w,g = +/(hy? +k?)
and replacing dkydk, by 2mq dg, we can write the magnitude of F as

2 2%
F= "(ats . (84.5)
a J J ce)(qe? +o)
26
The choice of go is discussed below.

The following remark should be made concerning the integration with
respect to w in formula (84.5). As w > oo the function «(w) -> 1, and the
integral is logarithmically divergent. This happens because we ought to
have subtracted from the field E the field which would be present if the
particle were moving in a vacuum (i.e. if « = 1); this field evidently does |
not affect the energy lost by the particle in matter.

If this subtraction were effected, 1/e in the integrand of (84.5) would
be diminished by unity, and the integral would converge. The same result
can be obtained by taking the integration from —R to +R and then letting
R tend to infinity. Since the function ¢(w) is even, the real part of the
integrand is an odd function of the frequency, and gives zero. The integral
of the imaginary part of the integrand converges.

In what follows we shall sometimes find it convenient to use the notation

Jeo) = nw) = nf +a", (84.6)
with 7'(w) and 7'’(«) respectively even and odd functions, and 7’ = —e’’/|e|®
< 0. Formula (84.5) can be rewritten in the explicitly real form
2 ee 1”
F= a J gt Ga de, (84.7)
733 (gv? + w?)
The energy loss per unit path length is the work done by the force over
that distance, which is just F; it is called the stopping power of the substance
with respect to the particle.

According to the general rules of quantum mechanics, the Fourier component of the field whose wave vector is k transmits to the 5-electron released
in ionisation a momentum Ak. For sufficiently large q (> wo/v) we have
RB = g?+ w/v? x g?, so that the momentum transferred is approximately
fig. A given value of q corresponds to collisions with impact parameter
~ 1/q. Hence the condition for the macroscopic treatment to be valid is
1/q > a. Accordingly, we take as the upper limit of integration a value go

§84 Ionisation losses by fast particles in matter 247
such thap wo/v < go < 1/a. The quantity F(qo) is the energy loss of a fast
particle with transfer of momentum not exceeding /igo to the atomic electron.
Integrating with respect to q in (84.7), we obtain
©
as " ov
Faw) = = [ ofy"(@)| og do. (84.8)
me wo
This formula cannot be further transformed in a general manner, but it
can be written in a more convenient form as follows. We first calculate the
integral
f ann!"(w) dw = —# | (w/e)do.
0 ce
To do so, we notice that, if the integration is taken in the complex «-plane
along a contour consisting of the real axis and a very large semicircle o in
the upper half-plane, the integral is zero, since the integrand has no poles
in the upper half-plane. For large values of w, the function ¢(w) is given by
formula (59.1):
4re&N
dw) = 1-7, (84.9)
mu
The integration along the large semicircle o can be carried out by using this
formula, and the result ist
a 2miNe ¢ dw
- f eon!(w) da = — AE i SO _ on2Netm. (84.10)
Ci) of
We define a mean frequency of the motion of the atomic electrons by
Ps
J on") log ado
Cy
loga = ———_—_—_—_—_—_
©
| o9"(w) da
0
©
-sal "(w)] log e deo (84.11)
zeane | 01M") lowed ;
+ This is the same as the value of the integral
f we"(e) deo
é
(see (62.14), as it should be, since, as || > 00, «| > 1 and 7” > — e”.

348 The Passage of Fast Particles Through Matter §84
Then formula (84.8) can be written a
F(qo) = (4nNeA/me®) log (goo/3). (84.12)

The following remark should be made here. It might seem from the form
of (84.7) or (84.11) that the main contribution to the ionisation losses
(84.12) comes from frequencies at which there is considerable absorption.
This is not so; these formulae may contain a considerable contribution

- from ranges in which ¢’’ is small. The reason is that in such ranges the
function «(w) x ¢’(w) may pass through zero. It is seen from formula
(84.5) that the zeros of e(w) are poles of the integrand. In reality, of course, |
<’'(w) is not exactly zero, and so the zeros of e(w) are not on the real axis but
just below it. Hence, when the expression used for e(w) is real and passes
through zero, the contour must be indented upwards at the pole of the
integrand, and so a contribution to the integral occurs. For example, if the
function «(w) is given by (64.5), the contribution to the retarclation (84.12) |
from the poles + (where ¢(w1) = 0) is easily seen, by direct calculation |
from (84.7), to be (42Ne*/mv?a?) log (q1v/«1). |

In order to find the energy loss F(q1) with transfer of momentum not |
exceeding some value fig, > higo, we must “join’”’ formula (84.12) to that |
given by the quantum theory of collisions, corresponding to energy loss by
collisions with single atoms. This can be done by using the fact that the
ranges of applicability of the two formulae overlap. As we know from the
theory of collisions, the energy loss with transfer of momentum in a range
of hdg is

dF = (40Net/mv?) dq/q, (84.13)
and this formula is applicable (in the non-relativistic case) for any value of
q > «w/v which is compatible with the laws of conservation of momentum
and energy, provided that the energy transferred is small compared with
the initial energy. of the fast particle. The energy loss with all values of g
between go and qi is accordingly (47Ne4/mv2) log (qi/qo). When this quantity
is added to formula (84.12), go is replaced by gi, so that

F(qi) = (47 NeA/mo*) log (qiv/ 0). (84.14)

If a momentum fig; large compared with the atomic momenta is given to
an atomic electron, its energy is FE, = hq2/2m. Thus we can write

F(E\) = (20Ne!/mv®) log (2mv?E;/h?a?). (84.15)

+ See Quantum Mechanics, §121, Pergamon Press, London, 1958. The “effective retardation” used there differs from F by a factor N.

Formula (84.13) applies to collisions with free electrons. Its range of applicability as
hitherto determined (q5> wo/v), however, extends to values of g for which the atomic
electrons cannot be regarded as free. ‘The condition for this is g > wo/vo, where vo is the
order of magnitude of the velocity of the majority of the atomic electrons; the energy f'q?/2m
of the 8-electron is then large compared with atomic energies.

|

§85 Tonisation losses by fast particles: the relativistic case 349

This formula gives the energy loss of a fast particle (an electron, for
example) by ionisation with a transfer of energy not exceeding Fy. It differs
from the usual formula derived from a microscopic discussion of collisions,
neglecting interactions between atoms, } only by the definition of the “‘ionisation energy”, which is here represented by ia. The mean (with respect to
the electrons) ionisation energy of an atom is usually almost independent
of its interaction with other atoms, being determined mainly by the electrons
of the inner shells, which are almost unaffected by that interaction. Moreover, this quantity appears here only in a logarithm, and so the exact definition
of it has even less effect on the magnitude of the energy loss.

The maximum energy which can be transmitted to an atomic electron in
its interaction with a fast heavy particle is 2mv2, and is small compared with
the original energy of the heavy particle.{ Substituting this value for 2,
in (84.15), we obtain the total ionisation losses of a heavy particle:

F = (4nNe4/mv?) log (2mv?/ha). (84.16)
This differs from the usual formulal| only in the definition of the ionisation
energy as fia.

## Section §85: Ionisation losses by fast particles in matter: the relativistic case

| At velocities comparable with that of light, the effect of the polarisation
of the medium on its stopping power with respect to a fast particle may
become very important even in gases. tt

To derive the appropriate formulae, we use a method analogous to that
used in §84, but it is now necessary to begin from the complete Maxwell’s
equations. When extraneous charges are present with volume density pex,
and extraneous currents with density jex, these equations areft

10H
divH =0, curlE = —--—, (85.1)

; c ot

A 10eE 4n,
div@E = 4pex, curlH = -—— + —jex. (85.2)
c at c
In the present case the extraneous charge and current distribution are
given by

pex = e8(r— vi), jex = ev (r — ve). (85.3)

+ See Quantum Mechanics, formula (121.13).

$ When a heavy particle collides with an electron, the maximum transferable momentum
higmax is small compared with the momentum Mo of the heavy particle. The change in the
energy of this particle is therefore v- fig, and equating this to the electron energy we have
Fq?[2m = hv-q < fivg, whence figmax = 2mv, E1,max = 2mv®.

|| See Quantum Mechanics, formula (122.10).

tt This effect was pointed out by E. Fert (1940), who performed the calculation for the
Particular case of a gas whose atoms are regarded as harmonic oscillators. The general
derivation given here is due to L. LANDAU.

tt We put p(w) = 1, since matter does not exhibit magnetic properties at the frequencies
important as regards ionisation losses.

350 The Passage of Fast Particles Through Matter §85
We introduce scalar and vector potentials, with the usual definitions:
10A
H=curlA, E= —-—-grad¢, (85.4)
ce ot
so that equations (85.1) are satisfied identically. The additional condition
. 1de¢
divA+-—-=0 (85.5)
ce at
is imposed on the potentials A and 4; this is a generalisation of the usual
Lorentz condition in the theory of radiation. Then, substituting (85.4) in
(85.2), we obtain the following equations for the potentials:
A & @A 4n
AA- Aras = ul &(r — vz), e509 |
ae Ad é =) 4ne &(r — v2).
———]) = — 4ne &r — vt).
°( 2 ott
We expand A and ¢ as Fourier space integrals. Taking the Fourier com- |
ponents of equations (85.6), we have (cf. §84)
Poy ed (= itv-k)
——— = —exp(— itv-k),
@ OP Qnte
alyogss & Su) _
aoe + Ar ) = Pre oe itv-k).
Hence we see that A, and ¢, depend on time through a factor exp (—itv-k).
We again put w = k-v = k,v, and obtain
A e v 7)
= —— int,
«Dac 2 — wake a)/c CH)
>= : tut
= ay Sey Ie
The Fourier component of the electric field is
Ex = iwAy/c — ik. (85.8)
From these formulae the force F = eE acting on the particle is found in
the same way as in §84.} Using the same notation, we now have
1
ee (= - S)ondade
ie ve
F=— OO (85.9)
7 : 2 1 €
0 [Pte a
t The magnetic force ev X H/c is seen by symmetry to be zero, and in any case is perpendicular to the velocity of the particle and so does no work on it.

§85 Tonisation losses by fast particles: the relativistic case 351
As c -> oo this formula tends, of course, to (84.5).

Let us first carry out the integration with respect to frequency. In order
to effect an integration in the complex w-plane, we first ascertain the poles
of the integrand in the upper half-plane. The function «(w) has no singularity and no zero in this half-plane, and so the required poles can only be
the zeros of the expression

« 1
“(a-a)-#
We shall show that, for any value of the positive real quantity q?, this expression vanishes for only one value of .
The proof is as follows. Let
_ fd) 1
| fo= ofS ah
We consider the integral
1 pdf(w) dw
Al dw f(w)-a’
taken along a contour C consisting of the real axis and a large semicircle
(*Fig. 42). The function («) has no pole in the upper half-plane or on the*
real axis; the integral in question therefore gives the number of zeros of
the function f(w)—a in the upper half-plane. To calculate its value, we
write it as
a f af (85.10)
2ni 2, f-a
=
(\\N
| 6 se
c
@
(oON
Ne
Fic. 42
. + For metals e(w) has a pole at w = 0, but we always tends to zero with w.

352 The Passage of Fast Particles Through Matter §85
For w = 0, f = 0. For positive real w we have im f > 0, and for negative
real w imf < 0. At infinity f tends to — w2[(1/o®)—(1/c®)], and therefore
J goes round a large circle when w goes round the large semicircle. Hence
we see that the path of integration C’ in the f-plane is of the kind shown
in *Fig. 42. Let a = q be a positive real number, as in Fig. 42. Then,*
in going round C’, the argument of the complex number f—a changes by
2, and the integral (85.10) is equal to unity. This completes the proof.}
Furthermore, it is easy to see that this single root of the equation
J(~)—@? = 0 lies on the imaginary w-axis: for purely imaginary w the
function f(w), like e(w), is real and takes all values from 0 to oo, including 92. |
Let us now return to the integral with respect to w in (85.9): |
1 1
r (= - s)e dw
Pe)
| 2 off _ 1 :
3 ¢-“(5-3)
This can be written as the difference between the integral along the contour
C and that along the large semicircle. The latter is [dw/w = im, and the
former is 27i times the residue of the integrand at its only pole. Let «(q)
be the function defined by the equation
€ 1
oS _ =) =@. (85.11)
Then, since the residue of an expression f(z)/¢(z) at a pole z = 2 is
f(%0)/$'(z0), the integral along C is
1 1 1 1
Pee (aa) 5 (aoa)
om We y] © Om gide
~ dol” (3 2
Collecting these expressions and substituting in (85.9), we have
% 1 1
F=e —————- + 1 ]qdq
5 gdg/dw
t Ifa is negative the argument of f — a changes by 4 on going round C’, so that the
integral (85.10) is equal to 2, i.e. the function f (w) + [al has two zeros in the upper halfplane.

§85 Ionisation losses by fast particles: the relativistic case 353
or, replacing the integration with respect to q in the first term by one with
respect to w, :
Qo) 1 1
Foe J [sap - alo +4eq0
vw)
(0)
wo)
& 1
=— f [=~ todo + deme + 7
2 (w)
0)
1 1
+1¢(5-Z)lo%@)- XO). (85.12)
v a
Large values of g correspond to large absolute values w of the root of equation (85.11). Using therefore the expression (84.9) for «(w), we find
5 er, 4nNe?
(go) = ~ i ( +e ). .
where we have put B = +/[1—v%/c2]. Substitution in (85.12) gives
tvaolp
2 1 2nNet ep?
F=— 4 -— - = (0); 85.13
vw ) lea Joes me? 3a ) ( )
0)
in the integral, only the leading term ivgo/f need be retained in w(go).
| The integration in (85.13) is over purely imaginary values of w. We use
the real variable w'’ = /i, with the lower limit § = o(0)/i, and again put
1/e = 7 (84.6). The required integral is
vale
— f fre”) - te” de”.
&
The values of the function 7(w) on the imaginary axis can be expressed in
terms of its imaginary part on the real axis:
| . 2 P am'(x)
yy opel fe
en) =! Perera
6
(cf. (62.17)). Hence the integral is (if we neglect x in comparison with vgo)
ol o
2 ee ln! (x)leo! deo" de 1 oqo?
2 Fs ae 1 Fs gO te
dy e+e? 7 B(x? + 2)

354 The Passage of Fast Particles Through Matter §85
We substitute this result in (85.13), and for simplicity put
logQ = }log(w? + &), (85.14)
where the bar denotes an averaging with weight w[n’’ (w)|, as in (84.11).
Then
4nNe* gov 2nNeA ef
= —— log—— - ——- + 2 85.15
Ma) mo? Be pa mee 7 22 ° ( )
Two cases must be considered in the further examination of this formula.
Let us first suppose that the medium is a dielectric, and that the velocity of
the particle satisfies the condition
2 < Ale, (85.16)
where ¢9 = «(0) is the electrostatic value of the dielectric permeability. On
the imaginary axis the function «(w) decreases monotonically from ¢«p > 1
for w = 0 to 1 for w = ico. The expression on the left-hand side of equation (85.11) therefore increases monotonically from 0 to oo, and for g = 0
(85.11) gives w = 0. Thus we must put € = 0 in (85.15); then Q becomes
the mean atomic frequency & (84.11), and
4nNe* gv =
F(qo) = ———|log — - => ]- 85.17)
(a) - [oe Se 3 (85.17)
For v < ¢ this formula becomes (84.12), as it should.
The value of go is such that go < 1/a, where a is the order of magnitude
_ _ of the distances between the atoms (in solids and liquids equal to the dimension of the atoms). In order to extend the formula to higher values of the
transferred momentum and energy, it must be “joined” to-the formulae
of the ordinary theory of collisions, as in §84, but the joining must now be
carried out in two stages. First, using formula (84.13), we enter the range
of g corresponding to energy transfers large compared with atomic energies
but not yet relativistic. Formula (85.17) is unchanged in form, but now
involves the 5-electron energy /2q2/2m. Calling this Ei, we have
2nNe* 2mvE, v
F(E)) = or [los gaat - SI: (85.18)
We can now go on to the relativistic values of Ey by using a formula of relativistic collision theory, according to which the stopping power with energy
transfer between E’ and E’+dE’ is
(2nNe4/mv®) dE’/E’ (85.19)
if E’ is small compared with the maximum transfer F),max compatible with
the laws of conservation of momentum and energy for a collision between
the fast particle concerned and a free electron. (In the non-relativistic
case, this formula is the same as (84.13).) Since the integration of (85.19)

§85 Tonisation losses by fast particles: the relativistic case 355
gives a term in log F’, it is clear that formula (85.18) is unchanged in form,
and it is therefore valid for all E) < E1max. .
The maximum energy transfer to an electron from a heavy particle is{
E,,max © 2mv2/B?. If Ei max is small compared with the total energy E of
the fast particle (ie. if E < M%c?/m), the differential expression for the
energy lost by free electrons is
2
uN (F _# ) ae
mo? \E’ Ume,
for all E’, whatever the kind of heavy particle concerned. The energy loss
additional to (85.18), with energy transfer from E; to Ey,max (with
E, < Ei,max) is then
2nNeA 2B, QnNed / 2mv® v2
22K (loge _Po=) = aS (lose - “). (85.20)
mv Ey 2mc2 mo BE,
Adding this to (85.18), we find the total stopping power with respect to the
heavy particle:
4nNe4 (, - 2mv® =v?
F- = (lve; aan 5): (85.21)
moe pia
Formulae (85.18) and (85.21) differ from those of the usual theory only in
that the “ionisation energy” is ia.
Let us now turn to the second case, namely that where
vw > Cleo, (85.22)
| which, in particular, always holds for metals, where <9 = 00. The expression
w(</e2— 1/v2) on the left-hand side of equation (85.11) then has two zeros
on the imaginary w-axis, one at w = 0 and the other at w = if, where é is
defined by
| (if) = 2/0 (85.23)
In the range from 0 to ié the expression w%(c/c?— 1/v) is negative, and for
| Jo] > & it takes all positive values from 0 to oo. As q 0, therefore, the
root of equation (85.11) in this case tends to é, which is the value to be
substituted in (85.14) and (85.15).
Two limiting cases may be considered. If € is small compared with the
| atomic frequencies wo, then the last term in (85.15) may be neglected, and
Q x &. Thus we return to formula (85.17). The opposite limiting case,
where & > wo, is of particular interest. Since, for large , the function
¢(ié) tends to 1, it is evident from (85.23) that this case corresponds to
ultra-relativistic velocities of the particle. Using formula (84.9) for e(w), we
can write equation (85.23) as 1+4Ne2/mé2 = c?/v®, whence
€2 = 4nNe2v®/me?f? ~ 4nNe?/mB?.
t See The Classical Theory of Fields, §2-5, Addison-Wesley Press, Cambridge (Mass.),
1951; Pergamon Press, London, 1959.

356 The Passage of Fast Particles Through Matter §85 |

As the velocity of the particle increases, the condition £ > w is ultimately fulfilled in any medium, i.e. whatever the electron density N (even
in a gas). The velocity required is, however, the greater, the smaller N, i.e.
the more rarefied the medium.

From (85.14) we then have simply Q ~ é. Putting also v ~ c, we find
that the last two terms in (85.15) cancel, leaving

F(qo) = (21Ne4/mc®) log (me®qo2/4nNe®).
Extending this formula, in the same manner as above, to large values of
the momentum and energy transfer, we find the following expression for |
the energy loss of an ultra-relativistic particle with an energy transfer not
exceeding Ey (< Ey,max):
F(E,) = (20Ne4/mc®) log (m?c?E,/20Ne?h?). (85.24) |

This result is considerably different from that obtained in the ordinary
collision theory, which neglects the polarisation of the medium. According to
that theory, in the ultra-relativistic range the stopping power F(E1) continues
to increase (though only logarithmically) with the energy of the particle.
The polarisation of the medium results in a screening of the charge, and
the increase in the losses is thereby finally stopped; it tends to the
constant value (independent of ) given by formula (85.24).

For heavy particles a formula can also be derived for the total stopping
power with any energy transfer up to Ej ,max (if the latter is small compared
with the energy of the particle itself). Again using the expression (85.20), in
which we can now put v = ¢, we find

pa NA Ng Oy 85.25
me [los TNO RB |: a
We see that the total stopping power continues to increase with the velocity of
the particle, owing to “close” collisions with a large energy transfer, for
which the polarisation of the medium has no screening effect. This increase,
however, is rather slower than that given by the theory when the polarisation
is neglected.

It may also be noted that the presence of the electron density N in the
argument of the logarithm in formulae (85.24) and (85.25) results in the
following property of energy losses of ultra-relativistic particles: when such a
particle passes through different substances containing the same number of
electrons per unit surface area, the losses are smaller in media with
larger N.

Finally, we may point out that a measurement of the energy losses of fast
particles in matter makes possible, in principle, the determination of the
function ¢(i£) for the substance concerned. It is easy to show that the exact
expression for F for the case (85.22) is such that

= 2 72
AF = Foye?) aS ee (85.26)
div?) 2c2

§86 Cherenkov radiation 357
where Fo is the quantity given by formula (85.18) or (85.21). F is measured;
the derivative d(Fov®)/d(v?) contains only the known quantities NV and v, and
can be calculated. Thus, using (85.26), each value of € can be related to a
value of v, and the value of ¢(ié) can then be calculated from (85.23).

## Section §86: Cherenkov radiation

A charged particle moving in a transparent medium emits, in certain circumstances, an unusual type of radiation, first observed by P. A. CHERENKOV
and S. I. Vavitov, and theoretically interpreted by I. E. Tamm and I. M.
Frank (1937). It must be emphasised that this radiation is entirely unrelated
to the bremsstrahlung which is almost always emitted by a rapidly moving
electron. The latter radiation is emitted by the moving electron itself when
it collides with atoms. The Cherenkov effect, however, involves radiation
emitted by the medium under the action of the field of the particle moving
in it. The distinction between the two types of radiation appears with
particular clarity when the particle has a very large mass: the bremsstrahlung
disappears, but the Cherenkov radiation is unaffected.

The wave vector and frequency of an electromagnetic wave propagated
in a transparent medium are related by k = nw/c, where n = v/e is the :
refractive index, which is real.f We have seen that the frequency of the
Fourier component of the field of a particle moving uniformly in the x-direction
in a medium is related to the x-component of the wave vector by w = kgv.
If this component is a freely propagated wave, these two relations must be
consistent. Since k > kz, it follows that we must have

| v > ¢fn(w). (86.1)
Thus radiation of frequency w occurs if the velocity of the particle exceeds
the phase velocity of waves of that frequency in the medium concerned.

Let 6 be the angle between the direction of motion of the particle and
the direction of emission. We have kz = k cos @ = (nw/c) cos @ and, since
kz = w/v, we find that

cos 9 = c/nv. (86.2)
Thus a definite value of the angle 6 corresponds to radiation of a given frequency. That is, the radiation of each frequency is emitted forwards, and
is distributed over the surface of a cone of vertical angle 20, where 6 is
given by (86.2). The distributions of the radiation in angle and in frequency
are thus related in a definite manner.
| + We again suppose the medium isotropic and non-magnetic. The Cherenkov radiation
in an anisotropic medium has been discussed by V. L. Ginzsunc, Zhurnal éksperimental’not
i teoreticheskoi fiziki 10, 608, 1940; A. A. Kotomensktr, Doklady Akademii Nauk SSSR 86,
1097, 1952; M. I. Kacanov, Zhurnal tekhnicheskot fiziki 23, 507, 1953.

‘A review of various cases in the theory of Cherenkov radiation and an extensive biblio
graphy is given by B. M. Bouorovskil, Uspekhi fizicheskikh nauk 67, 201, 1957.

358 The Passage of Fast Particles Through Matter §86
The emission of electromagnetic waves, if it occurs, involves a loss of
energy by the moving particle. This loss forms part, through a small part,
of the total losses calculated in §85.f In this sense the name ‘ionisation
losses” is not quite accurate. We shall now find the corresponding part of
the total losses, and thus determine the intensity of the Cherenkov radiation.
According to (85.9), the energy loss in the frequency interval dw is
ie® 1 1 qdq
dF = —dw— —-~—) f—_*?* __
waa | eac1\.
old
ce yt
where the summation is over terms with w = +|w|, We introduce as a
new variable
- f(s _ 1
Then
ie? 1 1 dé
dF = — dos Do(5 - =) Je
In integrating along the real é-axis we must pass round the singular point
€ = 0 (for which g?+,2 = k®) in some manner, which is determined by
the fact that, although we suppose «(w) real (the medium being transparent), it actually has a small imaginary part, which is positive for w > 0
and negative for w < 0. Accordingly, has a small negative or positive
imaginary part, and the path of integration ought to pass below or above
the real axis respectively. This means that, when the path of integration is
displaced to the real axis, we must pass below or above the singular point
respectively. This gives a contribution to dF, and the real parts cancel in
the sum. Indenting the path of integration with infinitesimal semicircles,
we find
Bw | dé/é = Dime.
Thus the final formula is
e 2
dF = S(t - <a)e de, (86.3)
e vn
which gives the intensity of the radiation in a frequency interval dw.
According to (86.2), this radiation is emitted in an angle interval
c dn
dé = ———_——dw. 86.4
ont sind dw (864)
+ The bremsstrahlung is not included therein.

§86 Cherenkov radiation 359
The total intensity of the radiation is obtained by integrating (86.3) over
all frequencies for which the medium is transparent.

It is easy to determine the polarisation of the Cherenkov radiation. As
we see from (85.7) the vector potential of the radiation field is parallel to
the velocity v. The magnetic field H, = ikxA, is therefore perpendicular
to the plane containing v and the ray direction k. The electric field (in the
“<wave region”) is perpendicular to the magnetic field, and therefore lies in
that plane.

In connection with our discussion of the radiation emitted by a particle
moving in matter, we may mention another effect whose existence has been
deduced by V. L. Gryzeurc and I. M. Frank: a particle must emit radiation

on passing from one medium to another. This “transition” radiation is in
principle different from the Cherenkov radiation, in that it must occur for
any velocity of the particle, not necessarily exceeding the phase velocity of
light in the medium. It is also unrelated to the bremsstrahlung which also
occurs when charged particles are incident on a surface separating two
media. As with Cherenkov radiation, the distinction is particularly clear
for a particle of infinite mass, for which the bremsstrahlung is zero but the
transition radiation is not. f
c a =x sino desist of the formulae for the transition radiation is given by G. M.
JETP 6 (33), 1079, Mopemmetia acl i teoreticheskot fiziki 33, 1403, 1957; Soviet Physics



---


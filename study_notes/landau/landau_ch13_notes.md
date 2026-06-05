# Landau & Lifshitz《Electrodynamics of Continuous Media》第13章

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter XIII: Field at High Frequencies

SCATTERING OF ELECTROMAGNETIC WAVES

## Section §91: The general theory of scattering in isotropic media

In THE theory of propagation of electromagnetic waves in transparent media
discussed in Chapters IX-XI, a phenomenon has been neglected which,
though not prominent, is of fundamental importance: scattering. Scattering
results in the appearance of scattered waves of small intensity, whose frequencies and directions are not those of the main wave.

Scattering is ultimately due to the change in the motion of the charges in
the medium under the influence of the field of the incident wave, resulting
in the emission of the scattered waves. The microscopic mechanism of
scattering must be investigated by quantum methods, but this investigation
is not needed in developing the macroscopic theory described below. We
shall therefore give only some brief remarks on the nature of the processes
which cause the change in the wave frequency on scattering.

The basic scattering process consists in the absorption of the original
quantum hw by the scattering system and the simultaneous emission by that
system of another quantum fw’. The frequency w’ of the scattered quantum
may be either less or greater than w; these two cases are called respectively
Stokes scattering and anti-Stokes scattering. In the former case the system
absorbs an amount of energy A(w—’); in the latter case it emits fi(w’— w)
and makes a transition to a state of lower energy. In the simple case of a
gas, for example, scattering takes place at individual molecules, and the
change in frequency may be due either to a transition of the molecule to
another energy level or to a change in the kinetic energy of its motion.

Another kind of process occurs when the primary quantum hw remains
unchanged but causes the scattering system to emit two quanta: one of
energy iw, with the same frequency and direction, and a “‘scattered”” quantum fiw’. The energy /i(w+w’) is obtained from the scattering system.
Processes of this type, however, are, under ordinary conditions, very rare
in comparison with those of the first type, and are of little importance as
regards the phenomenon of scattering. f

Proceeding now to consider the macroscopic theory of scattering, we
must first make precise the meaning of the averaging processes performed
in that theory. As already mentioned at the beginning of §88, the averaging
of quantities in macroscopic electrodynamics can be regarded as comprising

+ We shall see in §92 that this stimulated emission is unimportant at all temperatures
T <h(w+t w’). It may become significant for radio waves.

378 Scattering of Electromagnetic Waves §91
two operations, that of averaging over a physically infinitesimal volume with
a given position of all the particles in it, followed by that of averaging the
result with respect to the motion of the particles. In the theory of scattering, however, this procedure is impossible, because the averaging with respect
to the motion of the particles annuls the very phenomenon which is to be
discussed. Thus (e.g.) the field and induction of the scattered wave which
appear in the theory of scattering must be taken to be those resulting from
the first averaging only. The single-frequency components of the fields in
the scattered wave, taken in this sense, will be denoted in this section by
E’, H’, D’ and B’.

The fields in the incident wave will be denoted by the unprimed letters
E, H. In the present chapter we always suppose the incident wave to be of a
single frequency w.

In the propagation of the scattered wave we have the relation D’ = ¢(w’)E’
between the electric induction and field (the scattering medium being
assumed isotropic), but this relation does not reveal the phenomenon of
scattering, ie. the formation of the scattered wave from the incident wave.
To describe this, additional small terms must be included in the expression
for D’. In the first approximation, these terms must be linear in the field of
the incident wave. The most general form of the relation is then.

Di, = EF, + ceFn + Bake. (91.1)
Here ¢’ denotes e(w'); «iz and By are tensors which characterise the scattering properties of the medium. In general they are not symmetrical, and their
components are functions both of the frequency w’ of the scattered wave and
of the primary frequency w.t}

The last term in (91.1) pertains to the part of the scattering which results
from processes of stimulated emission. All the terms on the right-hand side
of equation (91.1) must correspond to the same frequency w’ as D on the
left-hand side. Since E* has the frequency — w, the frequency of the quantities By,must be w + w’ to make the frequency of the products Bj,E,* equal to w’.
But w+ ’ is the frequency which characterises processes of stimulated emission. Because this effect is small, as mentioned above, we can neglect the
corresponding term in (91.1), and in what follows we shall write

Di, = Ey + wieEn. (91.2)

Similar formulae give the relation between B’ and H’. We shall, however,
neglect the magnetic properties of the medium, which are usually of no
importance as regards the scattering of light, and therefore put B’ = H’.

Maxwell’s equations for the field in the scattered wave are curl E’
= iw'H'/c, curl H’ = —iw'D'/c. Eliminating H’ from these equations, we

+. The fact that « and # are tensors does not, of course, contradict the assumed isotropy
of the medium. Only the fully averaged properties of the medium are isotropic; the local
deviations from the average properties, which include the additional terms in (91.1), need
not be isotropic.

991 The general theory of scattering in isotropic media 379
find curl curl E’ = w"2D'/c2. Substituting from (91.2) E’ = D’/e’—a-E/e’,
where aE denotes the vector whose components are ajcEx, and using the
equation div D’ = 0, we obtain for D’ the equation

AD’ + k2D’ = — curlcurl(a-E), (91.3)
where k! = w4/e'/c is the wave number of the scattered wave.

For an exact formulation of the conditions under which equation (91.3)
is to be solved, we divide the scattering medium into small regions (whose
dimensions are still large compared with molecular distances). On account
of the molecular nature of the scattering processes, their correlation at different points in the medium (assumed non-crystalline) extends in general
only to molecular distances.f Hence the scattered light from the various
regions is non-coherent. We can therefore treat scattering from one region
as if the light were not scattered at all in the remainder of the medium. In
this way we calculate the field of the scattered wave at a large distance from
the scattering region. Using a well-known approximation for the retarded
potentials at a large distance from the source,t we can immediately derive
the required solution of equation (91.3):

al exp (tk’ Ro)
D’ = — curl curl——— fuk exp(—ik’-r)dV. (91.4)
40 Ro
Here Rp is the radius vector from some point within the scattering volume
(the integration being over that volume) to the point where the field is to be
calculated; the vector k’ is in the direction of Ro. The integral in (91.4) is
independent of the co-ordinates of the point considered; retaining in the
differentiation, as usual, only terms in 1/Ro, we obtain
exp (ik’Ro)
D' = —-——— KF x [k' x | a-Eexp(— ik’-r) dV].
Tako # * UK % J a-E exp (~ ik’-2) 47]
Since, at the point considered, the medium is regarded as not scattering, the
relation between D’ and E’ there is given by D’ = ¢’E’ simply. In the field
of the incident wave E we separate a factor periodic in space, putting E
= Eoexp (ik-r). Then, with the notation
G = [ a-Eo exp(—ia-r)dV, (91.5)
where q = k’—k, we have
exp (ik’Ro)
E = —-————_k x {k’ x G). 91.6
4aRoe (k’ x G) (91.6)
+ Exceptions may occur for particular cases of scattering, which will be discussed in §94.
In such cases the dimensions of the scattering regions must be supposed large in comparison
with the wavelength of the light.
$ See The Classical Theory of Fields, §9-2, Addison-Wesley Press, Cambridge (Mass.),
1951; Pergamon Press, London, 1959.

380 Scattering of Electromagnetic Waves §91
The vector E’ is perpendicular to the direction k’ of the scattered wave, and
is given by the component of the vector G perpendicular to k’.

Having thus determined the non-averaged field in the scattered wave, we
can now investigate the intensity and polarisation of the scattered light. To
do so, we form the tensor

Tig = EGE's*, (91.7)
where the bar denotes the final averaging over the motion of the particles,
which so far has not been carried out. The averaging of a quadratic expression gives, of course, a result which is not zero. Since E’ is perpendicular to
k’, the tensor J, has non-zero components only in the plane perpendicular
to k’. These components form a two-dimensional tensor J,, in that plane
(Greek suffixes take two values). The tensor I, is, by definition, Hermitian:
Tap = Ipat. It can be reduced to “principal axes”, and the ratio of its two
principal values gives the degree of depolarisation, while their sum is proportional to the total intensity.

The products E’;E’,* involve products of integrals G;, which must also
be averaged. Writing the product as a double integral, we have

GiGi" = EaEom* | { oaa%em2* exp[— iqe(rs — x2)]dVidVe. (91.8)

The suffixes 1 and 2 indicate that the values of « are taken at two different
points in space.

In averaging the integrand it must be remembered that the correlation
between the values of « at different points in the body extends in general only
over molecular distances. After averaging, therefore, the integrand will be
appreciably different from zero only for |rz—11| ~ @, where a is of the order
of molecular distances. The exponent is ~ a/A, where A is the wavelength
of the scattered wave; but a/A < 1 if the macroscopic theory is applicable,
and so we can replace the exponential factor by unity.}

Next, the integration with respect to the co-ordinates r) and rp can be
replaced by one with respect to 4(r1 +12) and r = r1—r2. Since the integrand
depends, after averaging, on r only, we have

GiGi = VEnBon* { ca,1%em.2* dV, (91.9)
where V is the volume of the scattering region. It is evident a priori that the
scattering must be proportional to V. It should be noted that the direction
of the wave vector k in the incident wave appears neither in (91.9) nor,
consequently, in the following formulae.

+ See Classical Theory of Fields, §6-7. The reduction of an Hermitian tensor to principal
axes means putting it in the form Iv = Ainume:* + Aaniamea*, where nx, na are, in general,
perpendicular complex “unit” vectors: mien;* = 1, ngen* = 1, mema* = 0. The principal values Ai, Az of an Hermitian tensor are real.

'{ This procedure requires further discussion in the case of Rayleigh scattering (§94).

991 The general theory of scattering in isotropic media 381
‘The integrals in (91.9) form a tensor of rank four, which depends only on
the properties of the scattering medium. Since the medium is isotropic,
the most general form of this tensor is
f cartem2* AV = Ha + c)SaStm + 4(4 — €)SimBua + b5ix51m, (91.10)
where a, b and care scalar functions of w and w’. This tensor is automatically
symmetrical with respect to an interchange of the suffixes 7, J and k, m;
this interchange is equivalent to taking the complex conjugate, since the points
1 and 2 are equivalent; the tensor (91.10) is therefore real, and so are a, 6, ¢.
Substituting (91.10) in (91.9) we obtain
GiGe* = Vika + ¢)EoEox* + Ha — ¢)Eot*Eor + bEwHoi*5ix}. (91.11)
This expression could have been written down at once, since it is the most
general Hermitian tensor of rank two which is quadratic in Eo and involves
no other particular directions. This tensor is, of course, not transverse to
k’. The required general form of the tensor I, is obtained by “projecting”
the tensor (91.11) on a plane perpendicular to k’; to do this, it is sufficient
to take a co-ordinate system with one axis in the direction of k’ and find the
components of the tensor along the other two axes.

Let us consider the scattering of a linearly polarised wave. The amplitude
of the field Eo can be defined as a real quantity.| The components of the
tensor I, for the scattered light are therefore also real. This means that the
scattered light is partially polarised, and can be divided into two independent
(non-coherent) waves, each of which is linearly polarised. Since there are only
two distinctive directions (those of Eo and k’) on which the tensor I,g can

| depend, it is evident that one of these waves must be polarised with E’ in
the plane of Eo and k’, and the other with E’ perpendicular to this plane. The
intensities of the two scattered-light components will be denoted by J, and J2;

they are the principal values of the tensor I,,.

For real Eo, the expression (91.11) becomes
GiGi = V{aE Eo + DE*%u}- (91.12)
We may note first of all that the scattering of linearly polarised light is determined by two, not three, independent constants. To find i and Is, we
take the components of Ep in the two directions mentioned. The correspond
ing components of the tensor (91.12) give the result

th ~ asin?6 + 6, Ib ~b, (91.13)
the coefficients of proportionality being the same; 0 is the angle between Eo
and the direction of scattering k’. The intensity of the scattered-light component whose electric field is polarised perpendicular to the plane of Eo and

k’ is independent of the direction of scattering.

t See The Classical Theory of Fields, §§6-5, 6-7. We shall not consider here the scattering

of elliptically polarised light, on account of the complexity of the formulae.

382 Scattering of Electromagnetic Waves §91
When natural light passes through a medium, the scattered light is partially polarised, and it is evident from symmetry that the two non-coherent
components are linearly polarised, with their electric fields parallel and perpendicular to the scattering plane (the plane of k and k’). Let the intensities of these components be J, and J, respectively. To determine these,
we average (91.11) over all directions of the vector Ep in the plane perpendicular tok. The averaging of the product EoiZox* gives
Eoikox* = 3|Eo|*(5u — minx), (91.14)
where n is a unit vector in the direction of k. This is a tensor of rank two
which depends only on the direction of k, gives |Eo|2 on contraction, and
satisfies the condition HosEox* = (n-+Eo)Eox* = 0. Thus we have, when
natural light is scattered,
GiGe* = V|Eo|2(a(Sx ~ no) + 68). (91.15)
Finally, taking the components of this tensor in the two directions of polarisation, we obtain the required formulae:
I, ~hacot9+b, I, ~ hat, (91.16)
where $ is the scattering angle (i.e. that between k and k’).

Let us return to formula (91.10), which relates the scalar quantities a, b and
¢ to the tensor aj. Like any tensor of rank two, «4 can be written, in general,
as a sum of three independent parts:

ain = Faden + Sik + ain, (91.17)
where « = a is a scalar, sj, a symmetrical tensor whose trace is zero
(Six = Skis Sig = 0) and aj an antisymmetrical tensor. We substitute this
in (91.10) and contract with respect to various pairs of suffixes, obtaining the
three equations}

_—__—— 1
6a + 3b + 3c = f eaten" dV = foqas* dV,
3a+9b = [amacna*dV
= Efe dV + [Smasma* dV + [arena dV, + (91.18)
6a + 3b-3c = foeazca* dV
= 4 foaea* dV + |suxrsina* dV — | aix,raizo* dV.

+ The integrals on the right-hand sides of these equations are positive, since each can
be written as a square by a transformation inverse to that whereby (91.8) becomes (91.9).
Expressing the three integrals in terms of a, 6, ¢ (i.e. solving equations (91.18) for these integrals) we obtain the inequalities 2a + b + ¢ > 0, 2b-+c—a>0, 2b+a—c > 0. From
these, in particular, it follows that 6 > 0.

§92 The principle of detailed balancing applied to scattering 383
The right-hand sides of these equations, and therefore their solutions for
a, b, c, do not involve cross-products of «, six and ai. This means that
scattering can always be regarded as a superposition of three types of process,
which may be called scalar, symmetrical and antisymmetrical scattering. We
shall discuss each of these in turn.
Retaining only the first terms on the right of equations (91.18), we have
1 ¢—
a=c= 5 fa dy o_O: (91.19)
It is seen from (91.13) that, in scalar scattering of polarised light, the scattered
light is itself completely polarised, and its angular intensity distribution is
given by J = (3/2) sin?@. (Here and henceforward the expressions for J are
normalised so as to give unity on averaging over directions.) In scattering of
natural light, however, the angular distribution of the total intensity and the
degree of depolarisation of the scattered light are given, according to (91.16),
by 1=1, +1, = %(1+co0s®9), 1,/I, = cos*d; see the second footnote
to §72.
For symmetrical scattering, equations (91.18) give
1 1 1 r-—_—>°
= —-b=—-~c=— ino* AV. 91.20
a=; aaa i} Sik 18iK,2! (91.20)
In scattering of polarised light we have I = h+k= #o(6+sin?6),
Ie/h = 3/(3+ sin26), and in scattering of natural light J = £(14-sin?9),
I,/I, = 1-4 sin?s.
Finally, for antisymmetrical scattering we obtain
1¢——
| bac=-a= 5 | aaaaina a (91.21)
in scattering of polarised light I = $(1+c0s%8), Ji/J2z = cos®8, and in scatter| ing of natural light J = (2+ sin?9), I,/Z, = 1/(1+ sin?9).

## Section §92: The principle of detailed balancing applied to scattering

| The general principle of detailed balancing} can be used to obtain a
relation between the intensities in various scattering processes.

Let dene be the probability that a quantum /iw) is scattered (on a path of
unit length) and gives rise to a quantum /iwg in the solid angle element dog;
| let dw; be the probability of the converse process, in which a quantum hw,

yields a quantum fiw in the solid angle element doi. According to the
principle of detailed balancing we have dw12/ko2 dog = dag /k:2dor, where
| kyand keare the wave numbers of the two quanta. Substituting ky? = e1w1?/c*,
ho? = egwg2/c? (where «1 = ¢(w1), €2 = e(we)), we obtain
err? daye/doz = €2e22 die; /do1. (92.1)
+ See Quantum Mechanics, §116, Pergamon Press, London, 1958.

384 Scattering of Electromagnetic Waves §92

Here it is assumed that the initial and final states of the scattering system
correspond to discrete energy levels Ey and Ez, related by E1+hw, = Eo+hwe.
This statement of the problem is not quite true to reality, since the energy
levels of a macroscopic body are extremely closely spaced and can be regarded
as quasi-continuous.

Instead of the scattering probability dw)2 with an exactly determined frequency change, we must therefore use the probability of scattering into a
frequency range dw», i.e. of the body’s entering a state whose energy lies
in a range dE; = fidwe. Denoting this probability (again per unit path
length) by diz, we have dhyz = dwy2dI', = dewja(dI'2/dE2)h dwe, where dy
is the number of quantum states of the body in the energy range dE2. Instead
of (92.1), we therefore have

di. due dl, dha
dB, dopdag — dEa” doiden

According to a well-known relation between the statistical weight of a
macroscopic state of a body and its entropy , the derivative dI'/dE is
essentially exp /, so that (dIy/dE1):(dI'x/dE2) = exp (A1— 2). Since the
relative change in the energy of the body resulting from the scattering of one
quantum is negligible, the relative change in entropy is also small, and can
be taken as 41-2 = (dSY/dE)(E,—E2) = (E:—E2)/T = hi(we—o)/T.
Using this result, we can write the final expression of the principle of detailed
balancing for scattering in the form

dhe hor
Percy %&——— = Ten eng?
eevee = Chena (92.2)

The quantity dh, whose dimensions are cm-1, is called the differential
extinction coefficient for scattering of light. It can also be defined as follows:
dh is the ratio of the number of quanta scattered in the direction do and the
frequency range dw per unit time and volume to the incident photon flux
density. By integrating dh over all directions and frequencies of the scattered light, we obtain the total extinction coefficient, which represents the
damping decrement of the photon flux density as the light passes through the
scattering medium.

Let w2< «;. The relation (92.2) connects the intensities (extinction
coefficients) of Stokes (1 > 2) and anti-Stokes (2 > 1) scattering. We see
that the latter is in general less than the former by approximately the factor
e-Mw,-v)/T, This is a very general result, and corresponds to the fact that
the transfer of energy from the body to the electromagnetic field reduces the
probability of the process by a factor e~44/T, where AF is the energy transferred. In particular, the stimulated emission, in which the body gives up
an energy ii(w1+ 2) in each scattering process, is therefore usually very
weak. The probability of such a process, when /i(w1+ 2) > T, contains the
small factor eMectos/P,

§93 Scattering with small change of frequency 385
The general relation (92.2) is much simplified in the important case of
scattering with a relatively small change in frequency. We shall denote #1
by w simply, and the small difference w2— 1 by Aw(<a), and put for
brevity dij2/doz dw: = I(w, Aw). In the non-exponential factors «w? in
(92.2) we can neglect the difference Aw; these factors then cancel, leaving
I(w, Aw)eRolT = Tw + Aw, — Aw)eMo + anit,
In the first argument of the function I(w+Aw, —Aw), which gives the
initial frequency of the light, we can neglect Aw, i.e. refer the scattered
intensity to a somewhat displaced frequency of the incident light. Then
I(w, Aw) = I(w, — Aw)eP40/7, (92.3)
In this approximation I on each side of the equation refers to the same
frequency of the incident light. In other words, the relation (92.3) gives a
simple relation between Stokes and anti-Stokes scattering of the same light
with the same magnitude of the frequency change Aw.

## Section §93: Scattering with small change of frequency

The theory given in §91 is entirely general, and is applicable to all cases
of scattering in an isotropic medium, whatever the mechanism of scattering.
Such a general discussion, of course, cannot proceed very far, and a further
investigation of the phenomenon of scattering requires some restrictive
assumptions.

In most practical cases the scattering of light involves only a relatively
small change in frequency, Aw = w’—w. The calculations given below
pertain to this case. Besides the condition Aw < w, we shall suppose that
the relative change in the refractive index of the medium over the frequency
range Aw is small. This condition means that the frequency must not
lie close to a range in which the scattering medium is also absorbing.

If w is in the optical range, the microscopic mechanism of scattering with
small Aw may involve various kinds of motion of atoms and molecules (as
opposed to the purely electronic motions which give rise to optical transitions), including intramolecular vibrations of atoms, rotations or vibrations
of molecules, etc.

Let g = q(t) denote the set of co-ordinates describing the motion which
causes the scattering.f Since this motion is relatively slow, the macroscopic
description of the motion can be regarded from a different standpoint by
introducing the dielectric permeability tensor ¢4(g), whose components at
any instant depend only on the values of the co-ordinates g at that instant as
parameters. ‘This property follows from the assumed smallness of the
relative change in «. The dielectric permeability thus defined pertains to
the field averaged with respect to the electron motion for a given position of

+ For simplicity, we shall give a classical discussion. The results are actually still valid
when quantum mechanics is used to describe the motion of the nuclei.

386 Scattering of Electromagnetic Waves §93
the nuclei. When the averaging of the field with respect to the motion of
the nuclei is carried out, the dielectric permeability reduces to the scalar
«(w). Let the deviation of ei, from this value be Sei:

eu) = Bix + den(g). (93.1)

The tensor ey gives the relation between the field and the induction as
functions of time. It should be emphasised that the incident wave is still
assumed to have a single frequency w, but the field E’ in the scattered wave
is now regarded as a function of time, not resolved into single-frequency
components. The total field consists of the field E in the incident wave and
the field E’ in the scattered wave. Thus Dj+D'; = ix(Ex+ E's). Cancelling
D; = ¢E; and omitting the second-order term 5<E’,, we obtain

Diy = «B'; + den(Q)Ex. (93.2)

The relation (93.2) is of the same form as (91.2). There is a difference,
however, in that with this approach it is clear that the tensor ag, = Seq is
symmetrical. This follows at once from the general theorem concerning the
symmetry of the dielectric permeability tensor. Furthermore, since this
tensor is real for a transparent medium, the tensor Se; is also real.

Since the tensor a has no antisymmetrical part, there is no antisymmetrical scattering (§91) with small change in frequency.

Let us calculate the total scattered intensity with all frequency changes
Aw < w. This can easily be done as follows. In equation (91.3) for the
field in the scattered wave we can replace k’ by k = w/e/c (and take the
value of « for w’ = w); this equation does not then involve o’, ie. it is the
same for every component of the spectral resolution of the field. The equation is therefore valid for the unresolved field in the scattered wave, which
we shall denote by the same letter E’. Using the solution (91.6), we obtain

=— RA 4
jEP = ———_[GP sint@ = —“___|GP sinta,
16722Ry? 16n?Rorct
where 6 is the angle between k and G, and the bar denotes, as in §91, the
final average with respect to the motion of the particles (i.e. with respect to
the time dependence of ).

We define the extinction coefficient h as the ratio of the total intensity of
light scattered in all directions per unit volume of the scattering medium to
the incident flux density:

beef mtmea = ot
= pipe ) EP Rode! = oar Be

t This definition differs by a factor w’/w from the general definition (in terms of the
number of scattered quanta) given in §92. In the present case this factor may be taken as
unity, and the two definitions are equivalent.

§94 Rayleigh scattering in gases and liquids 387
As we have seen in §91, in calculating the mean value [GP we can replace
the exponential factor in the integrand in G by unity, so that
[GB = EoBou* [ 5adV J Send.
‘The expression to be averaged is a tensor of rank two and, since the medium
is isotropic, the result of the averaging is
re 2
feacdV | Sxa¥ = Wa { 8andP) .
Thus we have finally
at } 93.3
h=—— & av) ’ F
18act 7( J me —
or
h = (w/187c4)V(Sem)v?, (93.4)
where the suffix V denotes an averaging over the volume V.
The mean value of the squared integral can be written as the mean value of
a double integral, and is found to be proportional to the volume V (cf. §91).
Hence the value of the extinction coefficient is independent of the scattering
volume, as it should be, and also of the polarisation of the incident light.
Formula (93.4) can be regarded in the following way. We can say formally
that scattering would not occur in a completely homogeneous medium (ie.
one whose dielectric permeability is exactly constant). The scattering can be
| macroscopically described as resulting from inhomogeneities in the medium.
p Ss ge
The variation of these inhomogeneities with time, when resolved into spectral
components, gives the change in frequency of the light when it is scattered.

## Section §94: Rayleigh scattering in gases and liquids

Two types of scattering can be distinguished, depending on the change in
frequency of the light: (1) combination scattering, which is the RamanLandsberg-Mandel’ shtam effect and results in the appearance in the scattered
| light of lines whose frequency differs from that of the incident light, (2)
Rayleigh scattering, in which the frequency is essentially unchanged.
Combination scattering in gases results from a change, due to the incident
light, in the vibrational, rotational or electronic state of the molecule.
Rayleigh scattering, on the other hand, does not involve a change in the
internal state of the molecule. In the limiting case of a rarefied gas, when
the mean free path J of the molecules is large compared with the wavelength A of the light, scattering takes place independently at each molecule,
and can be discussed microscopically, using quantum mechanics.
+ Under ordinary observational conditions, electronic transitions are unimportant.

388 Scattering of Electromagnetic Waves §94

Here we shall discuss the opposite limiting case, where J < ,f and the
Rayleigh scattering in gases can be divided into two parts. One part is due
to irregularities in the orientation of the molecules (called fluctuations of
anisotropy). The other part is scattering by fluctuations in the gas density.
The orientation of the molecules is entirely changed by a few collisions, i.e.
after a time of the order of the mean free time 7. Hence the scattering by
fluctuations of anisotropy results in the appearance of a relatively broad line
with its peak at w’ = w and width ~ fi/r. The scattering by fluctuations of
density gives a much sharper line superposed on the other. As we shall see
below, fluctuations of density in volumes ~ 8 are of importance in the
scattering of light with wavelength A. Since these volumes are large, the
fluctuations in them occur comparatively slowly, and so the scattered line
is narrow. In what follows we shall regard this sharp line as being undisplaced.

The scattering by density fluctuations is scalar scattering (see the end of
§91): since the density p is a scalar, so is the change in the dielectric permeability Se resulting from a change in p. The change in the dielectric
permeability in fluctuations of anisotropy, on the other hand, is described by
a symmetrical tensor Se, with zero trace. The latter property follows from
the fact that the effect must vanish on averaging over all directions. Thus
the scattering by anisotropy fluctuations is symmetrical scattering.

In liquids the situation is less simple. Combination scattering can arise
only from a change in the vibrational or electronic state of the molecule;
rotational combination lines do not occur for scattering in liquids. The
reason is that, because of the strong interaction between molecules in a
liquid, they cannot rotate freely so as to acquire discrete rotational energy
levels. The rotation of the molecules, therefore, like any motion in which
their relative position changes, contributes in a liquid only to the relatively
broad scattering line at w’ = w, which in this case may be regarded as the
effect of Rayleigh scattering. The relaxation time of such motions depends
on the viscosity of the liquid.

The possibility of separating from the total Rayleigh scattering in a liquid
a part due to thermodynamic fluctuations (of density or temperature) depends
on the magnitudes of the various relaxation times. It is necessary that the
relaxation times of all processes of establishment of equilibrium in the liquid
should be small in comparison with the times characterising the fluctuations
concerned. In this case a narrow “undisplaced” line and a broader one are
observed. The undisplaced line corresponds to scalar scattering. The
broader background, however, does not in general correspond, as it does in
gases, to purely symmetrical scattering with no scalar part.

The total intensity of the undisplaced line is easily calculated by means of

+ More precisely, the necessary condition is / < Asin 9, where 9 is the scattering angle.
‘This is because the expression (94.4) which gives the scattered intensity involves the frequency only in the expression q = (2w/c) sin $8.

§94 Rayleigh scattering in gases and liquids 389
the general formula (93.4). For scalar scattering Se = deSx, and the
extinction coefficient is therefore
ot
h = ——V(8e)p?. 94.1
Gaca Pew (94.1)
If Sp and 87 are the changes in density and temperature, then
Be = (de/Ap)z8p + (d€/2T),ST.
The fluctuations of density and temperature are statistically independentt
(8T8p = 0), and their mean squares are
GF = ThoceV, — Bplv® = (TolV | 2P)n,
where cy is the specific heat per unit mass. Thus we have finally
a a Be\ 2 T2/de\2
= Sal) Ce toectar),b
act | P\Bp) p\p) 7 peo \8T,
‘This formula was first derived by A. Ernsrern (1910).

For gases formula (94.2) becomes much simpler. The dielectric permeability of a gas (at optical frequencies) is almiost independent of temperature,
and hence the second term in the brackets can be neglected. The density
dependence is that e— 1 is proportional to p, and hence

p(de/Op\r % «— 1% An 1),
where n = 4/e is the refractive index. Since, from the equation of state of a
perfect gas, (1/p)(dp/ap)r = 1/NT, where N is the number of particles in
unit volume, we find that
h = 2o'(n — 1)2/3nc4N. (94.3)
This formula was first derived by RayLeIGH (1881).

Let us now examine the fine structure of the undisplaced line. This
requires a consideration of the time variation of the fluctuations. In this
respect, thermodynamic fluctuations fall into two classes.t Adiabatic fluctuations of pressure in a fluid are propagated as undamped waves with the _
velocity of sound u; we here neglect the absorption of sound, since it causes
only a broadening of the line (see below). Fluctuations of entropy at constant
pressure, however, are not propagated relative to the fluid, and are damped
only gradually as a result of thermal conduction.

The time variation of the intensity (not averaged with respect to time) is
given by the squared modulus of the integral

Git) = J 8e(t).exp(— iq-r) dV”.Eo, (94.4)

+ See Statistical Physics, $111, Pergamon Press, London, 1958,

See Fluid Mechanics, §79, Pergamon Press, London, 1959.

390 Scattering of Electromagnetic Waves §94
in which Se is regarded as a function of time. In order to determine the shape
of the scattering line, G(¢) must be resolved into spectral components (i.e.
c(t) must be so resolved); the distribution of intensity as a function of Aw
will then be given by the squared modulus of the component G,,,.. However,
the factor exp(—iq-r) in (94.4) cannot be replaced by unity, as we have
done hitherto. The reason is that the quantity |G,,|? depends markedly on
the correlation of the time variation of the fluctuations at different points in
space. This is clear when |G,,|? is written as a double integral
J [ 8(2)8e(e’) expl— iq-(# — ’)]exp[iAw(t ~ 1)] dV dv” de de’.

On account of the wave propagation of sound disturbances, the time variation
of pressure fluctuation is correlated even at great distances. This fact was of
no importance in determining the total intensity of the line, which is obtained
by averaging the square |G(z)? with respect to time; since, in this case,
G(t) and G*(é) are taken at the same instant, it follows that only the correlation between the values of S¢ at different points at the same instant is of
importance, and this correlation extends only over short distances.

Let us first consider the changes Se which result from pressure fluctuations.
The quantity (94.4) is the Fourier space component of the fluctuation de
whose wave vector is q; its time dependence is given by e~4%, where
Aw = +qu. Since w x w’, we have g = |k’—k| = (2w/c) sin}9, where 9
is the angle between k and k’. If the corresponding value of Aw is denoted
by Aap, then

Awy = qu = + (2wu/c) sing. (94.5)
Thus the scattering by pressure fluctuations results in the appearance of a
doublet (called the Mandel’shtam-Brillouin doublet), the distance 2Awo
between whose components depends on the angle of scattering.

The fluctuations of entropy have zero frequency, as stated above, and so
scattering by them gives a central line with Aw = 0.

Let us determine the intensities of the doublet and the central line. The
total intensity of the undisplaced line is given by formula (94.2), so that it is
sufficient to determine, say, Jaoupiet/Jtotai (where Iaoupiet is the combined
intensity of the two components of the doublet, i.e. twice the intensity of each
component}). Since the doublet lines are due to scattering by adiabatic pressure fluctuations, their intensity is given by the mean square («/2p)s?(5p) v”.

Using the formula for adiabatic pressure fluctuations and a simple transformation by means of the formula for the ratio of adiabatic and isothermal

+ The difference between the intensities of the two components is, according to formula
(92.3), usually negligible, since #Awo < T.

994 Rayleigh scattering in gases and liquids 391
compressibilities, we obtain
Ge ®—— pT (0p\ (de \?
(5), - (3) Le)
op! 5 V \ap/ s\ep/'s
#2) (=).
~ V Xap) s\2p/ 5
Tey (a e\?
_P (2) (=) : (94.6)
Vep \Op/ 7\ Op! s
The adiabatic derivative (de/@p)s can be expressed in terms of more convenient quantities by transforming it to the variables p and T:
(2l@p)s = (B€/p)x + (Tleop?)(2p/27),(2¢/0T),The required ratio of intensities is given by the ratio of (94.6) to the mean
square total fluctuation (the expression in brackets in (94.2)). We shall not
give the cumbersome general formula, but only the simpler form obtained
when the temperature dependence of ¢ is neglected:
haouviet/Atotaa = Cv/ep (94.7)
(L. Lanpau and G. Praczex, 1933).

To determine the shape of the lines, it is necessary to consider the dissipative processes which result in the “decay” of the fluctuations. These
processes cause a damping of the fluctuation amplitude as e-vt, where y is
a definite constant. If the “eigenfrequency” of the oscillations is Awo, the
total time dependence is given by e~“/4%-+”), The intensity distribution in
the line is proportional to the squared moduli of the Fourier components of
this factor, i.e.

Jo Y
dI = —————_——— dha, 94.8)
7 (Aw Aut ee)
where Jp is the total intensity of the line. This is called the dispersion form
of the line. The “width” is y.
According to formulae derived in the theory of absorption of sound, the
damping coefficient for sound fluctuations with wave vector q is
putt (a)
= =| ++ «(—-—}],
, 2p 3” as cy op
where 7, ¢ are the viscosity coefficients of the fluid and « its thermal conductivity. Substituting g? = 2(w/c)%(1—cos $), we obtain the following expression for the width of the doublet components:
w? 4 1 1
y= 5 ~ con 9) in + f+ (<-=)]- (94.9)
pee 3 Cy Cp
t See Fluid Mechanics, §77.

392 Scattering of Electromagnetic Waves §94
The damping of isobaric fluctuations of entropy (and therefore of temperature) is determined by the heat-conduction equation @7/ét = y AT, where x
is the thermometric conductivity. For fluctuations with wave vector q (i.e.
spatial variation as exp(iq-r)), we therefore have
7 = xP = 2x(w2/e2)(1 — cos 9). (94.10)
The shape of the central line is given by (94.8) with Awo = 0, the width y
being (94.10).

As already mentioned at the beginning of this section, the above theory is
applicable to scattering in a liquid if all the relaxation times in it are small
compared with those characterising the fluctuations. It should be borne in
mind that, in any liquid, there are relaxation times of various orders of
magnitude. The most rapid relaxation process, apparently, is the “decay” of
elastic stresses in the liquid. The corresponding Maxwellian relaxation time
is ty ~ 7/G, where G is the modulus of rigidity.t The reorientation of the
molecules, i.e. the “decay” of the anisotropy fluctuations, takes place less
rapidly. The corresponding Debye relaxation time is tp ~ ya*/kT, where a
is the dimension of the molecule; the difference between ty and tp is
particularly large in liquids with large molecules. Finally, various other
slow relaxation processes leading to the dispersion of sound are also possible
(e.g. chemical reactions, slow transfer of energy to vibrational degrees of
freedom of the molecule). The important processes as regards scattering are
those for which 1/7 is comparable with the frequency of the “sound” disturbances which cause the scattering. There is as yet no complete survey of all
the possible cases, and we shall not give one here, but merely mention that,
when the viscosity of the liquid is sufficiently high, and so

tm > I/qu ~ ¢/wu sin}9,
the liquid behaves as an amorphous solid with respect to the scattering of
light.

Finally, we may note an unusual type of scattering which occurs at the free
surface of a liquid. The fluctuations have the result that this surface is no
longer perfectly plane, and the consequent “roughness” causes a partial
scattering of the light reflected from it (L. I. MANpeL’sHTam, 1913).

PROBLEM

Light is scattered in a gas whose molecules are linear, with polarisabilities «, and @,
along and across the axis respectively. Determine the intensity resulting from the various
types of scattering.

SoLvuTIoN. The total intensity of scattered light (for given vibrational and electronic
states of the molecules) includes the Rayleigh scattering and the rotational part of the combination scattering. Since the scattering takes place at the individual molecules of the gas,

+ See Theory of Elasticity, §31, Pergamon Press, London, 1959.

{ See L. I. Manvet’staM, Annalen der Physik 41, 609, 1913, where a calculation is given
for light scattered in the plane of incidence.

§95 Critical opalescence 393
the total extinction coefficient is most simply obtained from formula (72.3), by multiplying
by the number of particles per unit volume N and replacing the squared polarisability by
dan? = Hat+ 20,2):
8xo0tN
ha atte). a
‘The undisplaced Rayleigh line is due to the scalar part of the polarisability, i.e. it is the
same as if the polarisability tensor of the molecule were da6ix. ‘The same formula, (72.3),
therefore gives
82wtN
Irasasey = “yo q (rte) @
"The difference htotat—hundisp includes the “background” (scattering by anisotropy fluctua
tions) and the rotational combination scattering. In order to separate the former, we must
first average the polarisability tensor of the molecule with respect to rotation about some
particular axis (perpendicular to the axis of the molecule). The polarisability along the axis
of rotation averaged in this way is evidently ¢,, and that along any direction in a plane
perpendicular to the axis of rotation is 4(2,-+a,). In other words, a molecule rotating
about a given axis is to be regarded as a particle for which the principal values of the polarisability tensor are a, 4(a,-+e,), 4(¢,+4,). Using these, fwe calculate the symmetrical
tensor c4x—tan5:, whose trace is zero, and then a procedure similar to the derivation of
formulae (1) and (2) gives
82wtN (0,—o1)?
honees = “pea oo )
Finally, the intensity of the rotation combination scattering is obtained by subtracting (2)
and (3) from (1):
A _ 8rwtN (@,—a,)?
combin = 9 _

## Section §95: Critical opalescence

| The isothermal compressibility (2p/@p)7 increases without limit as the
| critical state is approached. The expression (94.2) for the total intensity due
to scalar Rayleigh scattering therefore increases also. This indicates a marked
increase in scattering near the critical point, called critical opalescence.t The
formula (94.2) itself is, however, inapplicable, because the expressions for
| the thermodynamic fluctuations used in its derivation are no longer correct.
The increase in intensity does not take place for all three components of
| the fine structure of the Rayleigh line, but only for the central component.
. According to (94.2) and (94.7), the intensity of the doublet is
A wt (22) (=)
doublet ~ ~—7——{5-} |] ™ 6nct cp \ap) r\ép) r
The thermodynamic formula
pace = Tle) 3
P? (eplép)r
} Asimilar phenomenon occurs for scattering in a solid near the critical point of a secondorder phase transition. It has been discussed by V. L. Gryzpurc, Doklady Akademii Nauk
SSSR 105, 240, 1955.

394 Scattering of Electromagnetic Waves §95
gives near the critical point
wt prey Oe\2
h = osama): BI
doublet = 5-5 moma ie (95.1)
As we shall see below, the factor exp(—iq-r) in (94.4) cannot be replaced
by unity near the critical point, even in calculating the total scattered
intensity. Let dh be the differential extinction coefficient, relating to scattering into a given solid angle do (corresponding to a given value of q = k—k’).
Considering, for definiteness, the scattering of unpolarised light, and using
the result that the angular dependence (for scalar scattering) is given by the
expression }(1-+ cos? $), we have
dh a! iq-t) dV) A(1 + cos? 9°. 95.2;
= TS exp(— as . IS —. od
Feat p J Beesp(— iar) dV) 41 + cos 9}. (95.2)
Near the critical point, the density fluctuations increase but the temperature fluctuations remain finite. It is therefore sufficient to consider
Se = (/p)78p, so that
wt (a2 1f,. do’
dh = ——|—} —||§ — iq: av. 1+ cos? $)—. (95.3
falc) F| f Peexp(— saz) dr]. 201 + costa), 05.3)
According to the theory of fluctuations, the mean square density fluctuation near the critical point can be expressed in terms of the coefficients a
and 6 in the formula
F — F = }a(dp)? + 46(grad dp), (95.4)
where F is the free energy per unit volume. t
This formula gives the leading terms in an expansion of the change in the
free energy in powers of Sp and of its gradient; the latter has to be taken into
account because of the amplification of local inhomogeneities in the body
near the critical point. The constant a is expressed in terms of the ordinary
thermodynamic quantities byt
a = (1/o)(&p/ap)r. (95.5)
The mean square in (95.3) can be expressed in terms of a and 6 by
\,; 2
| { Seexp(—ig-r)av]| = VI(a + 64"). (95.6)
+ See Statistical Physics, §116.
4. The derivative (2F/dp)r is the thermodynamic potential per unit mass, and the second
derivative is therefore a = (2°F/0p?)r = (2/8p)r = (1/p)( ap/ ap)r

§96 Scattering in amorphous solids 395
Substituting in (95.3), we obtain the final result
2
dh = aaalz), ee (95.7)
as (2) +2 5(1 — cos 9)
p\oplr
This formula was first derived by L. S. OrnsTeIn and F, ZerntKe (1914).
When the angle 9 is not small, the first term in the denominator may be
neglected, and .
2 2 2
dh sans) 1+ costo a (98.8)
6472c2b\ dp) 7 1 — cos 9
The total intensity scattered in all directions is obtained by integrating
(95.7) with respect to o’. When (ap/dp)r = 0, i.e. at the critical point, the
integral is logarithmically divergent for small angles. In reality, the integration should be extended only to angles of the order of the diffraction angle
| (~ AJL, where L is the dimension of the body). The total intensity therefore
depends logarithmically on the dimension of the scattering body.

## Section §96: Scattering in amorphous solids

Rayleigh scattering in amorphous solids differs considerably from that in
fluids. In an isotropic solid there are two velocities of propagation of
sound, 1; (longitudinal) and uw; (transverse). The fine structure of the
Rayleigh line therefore includes not one but two Mandel’shtam-Brillouin
doublets. They are due to scattering by transverse and longitudinal “sound
waves”, and their distances from the centre of the line are respectively
+A, +Aoz, where Aw; = gu;, Aw: = que. Since uj > up, it follows that
Aw; > Aw. The central component of the line is again due to fluctuations
which are not propagated relative to the medium. In this case the main
fluctuations of the latter type are those of structure. In an amorphous body,
where the atoms are not arranged in an ordered manner, these fluctuations
are comparatively large and vary only slowly with time (on account of the
extreme slowness of the diffusion processes in a solid). Scattering by these
fluctuations leads to a strong line whose width is almost zero, As regards
polarisation and angular distribution, this line results from a superposition
of scalar and symmetrical scattering.

Next, let us consider the doublet components of the Rayleigh line in
amorphous bodies. Here we cannot put exp(—iq-r) = 1 in the integral G,
as we did for fluids, even in calculating the total intensity (and polarisation)
of the scattered light; moreover, the scattering cannot be classified according
to dependence on angle as in §91. The reason is that, in a solid, the effect of
any deformation (in this case, fluctuations) extends to considerable distances.
Hence the fluctuations at different points in the body at the same instant are
correlated even at distances large compared with 1/g.

396 Scattering of Electromagnetic Waves §96
The field in the scattered wave is
a wexp(ikRo) _, ,
E’ = bre x(n’ x G), (96.1)
where
Gi = | deuexp(— ig-r) dV’. Bow, (96.2)
and n’ is a unit vector in the direction of scattering. The change in the
dielectric permeability resulting from the deformation of an isotropic body is
Sexy = aitix + anundix, (96.3)
where uy, is the strain tensor (see (81.1)). Since the integral (96.2) isolates
; from Sq the Fourier space component with wave vector q, ux in (96.3)
must be taken as the deformation in a sound wave with this wave vector. We
therefore write the displacement vector as
u = re{upexp(iq'r)} = 4[upexp(iq-r) + up*exp(—iq-r)], (96.4)
whence the strain tensor is
as 5 *)
un = (— + —
 WNome ” axe
= re{ti(uoige + wong) exp(éq-r)},
and the volume integral is
J maexp(— ig-t)dV = HV(uorge + toegs). (96.5)
Let us first consider scattering by transverse “sound” waves. Since in a
transverse wave u is perpendicular to q, and uy = 0, Sex = ain. Using
(96.5), we therefore have
G = Vay{u0(q: Eo) + (uo: Eo)}- (96.6)
A transverse sound wave can have two independent directions of polarisation: the vector u may be in the plane of k and k’, or perpendicular to
that plane. Since E is perpendicular to k, it is easy to see that in the first
case the component of G in the plane perpendicular to k’ is zero. Thus
transverse sound waves “polarised” in the plane of k and k’ do not scatter
light.
If the vector u is perpendicular to the plane of k and k’, a simple calculation, using (96.1) and (96.6), gives for the field in the scattered wave
2 ih,
E,= re ONS) aie cos}. Ey,
ia (96.7)
, w? exp (ikRo) .
Ey = ER tM quo cos$3. Ey.

§96 Scattering in amorphous solids 397
Here $ is, as usual, the angle between k and k’, and the suffixes || and |
denote components in the plane of scattering and perpendicular to that
plane. The coefficient of proportionality in these two formulae involves the
same fluctuation up. This means that no depolarisation occurs on scattering:
linearly polarised light remains so (though it is polarised in a different
plane).

Since the coefficients in formulae (96.7) are exactly the same, the extinction coefficient dh does not depend on the state of polarisation of the incident
light, and is

2qj\2
dh = (<4) Vial cos? 49 do. (96.8)
It remains to determine the mean square amplitude of the fluctuation uo.
From the point of view of the general theory of thermodynamic fluctuations,
the sound wave (96.4) may be regarded as a combination of two classical
oscillators (waves propagated to the right and to the left), each having a
mean kinetic energy 47. Since the frequency of the oscillations is here
Aw = qu:, the mzan kinetic energy is $V pa2 = }Vp(ug)?|uol®. Equating
this to 2.47, we have
ful = 47/V purge. (96.9)
Finally, substituting (96.9) in (96.8), we obtain
aPzutT
= cos?
dh = Cac 49-do. (96.10)
‘The angular dependence of the scattering is totally different from that which
occurs in fluids.

Let us now consider scattering by longitudinal “sound” waves. In these

waves u is parallel to q, and from (96.3) and (96.4) we find
EX
G= HV {= + aE.
A simple calculation gives for the field in the scattered wave
wexp(ikRo) . .
By = SPOR) 7 uogank,,
oad 96.11
wexp(ikRo) , . LeD)
E, = Tako HV uoalbon + ($41 + az) cos $]E,.
In this case also there is no depolarisation on scattering. The angular distribution and the extinction coefficient, however, depend on the state and
direction of the polarisation of the incident light. We shall not pause to
write out the relevant formulae, which are somewhat cumbersome. The
calculations are wholly similar to those given above, and the expression for
|uol? differs only in that u; is replaced by w; in (96.9).



---


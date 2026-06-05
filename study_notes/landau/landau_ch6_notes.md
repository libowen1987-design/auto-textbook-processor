# Landau & Lifshitz《Electrodynamics of Continuous Media》第6章

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter VI: Superconductivity

QUASI-STATIC ELECTROMAGNETIC FIELD

## Section §45: Eddy currents !

So Far we have discussed only constant electric and magnetic fields, and have
used Maxwell’s equation
1E aah (45.1)
eurlE = —-— 5
¢ at
only as a step in deriving the expression for the energy of a magnetic field
(§30).

The nature of the variable electromagnetic fields in matter depends greatly
on the kind of matter concerned and on the order of magnitude of the frequency of the field. In the present section we shall consider the phenomena
which occur in extended conductors placed in a variable external magnetic
field. We shall assume that the rate of change of the field is not too large,
and therefore satisfies various conditions which will be derived below.
Electromagnetic fields and currents which satisfy these conditions are said
to be quasi-static.

We shall first of all suppose that the wavelength ) ~ c/w which corresponds
(in the vacuum or dielectric surrounding the conductor) to the field frequency
w is large compared with the dimension / of the body: w < c/l. Then the
magnetic field distribution outside the conductor at any instant can be
described by the equations of a static field:

divB=0, curlH =0, (45.2)
all effects due to the finite velocity of propagation of electromagnetic disturbances being neglected. Of course, this neglect is permissible only at
distances from the body which are small compared with A; these are the only
distances which need be considered in determining the field inside the body.

The complete system of field equations inside the conductor consists of
(45.1) together witht

divB = 0, (45.3)
curlH = 4z0E/c. (45.4)

} In an anisotropic body, oE on the right-hand side of (45.4) must be replaced by the
vector onEx.

$45 Eddy currents 187
The second of these equations has been derived, strictly speaking, only for
constant currents and magnetic fields. It is therefore necessary to specify
conditions under which this equation can reliably be used for variable fields.
In equation (45.4) the current has been written in terms of the electric field
in accordance with the relation j = cE with constant o, which holds for a
steady state. This relation remains valid if the period of the field is large
compared with the characteristic times of microscopic conduction. That is,
the field frequency must be small compared with the reciprocal mean free
time of the electrons in the conductor. For typical metals at room temperature, the limiting frequencies given by this condition lie in the infra-red
region of the spectrum. t

There is another condition which restricts the applicability of the equations
in this case. Being macroscopic equations, they presuppose that the electron
mean free path is small compared with the distances over which the field
changes appreciably. We shall return to this condition later.

In equations (45.1) and (45.4), E is the induced electric field resulting from
the variation of the magnetic field. When H is known, the field E can be
immediately determined by equation (45.4). The equation for H is obtained
by eliminating E from (45.1) and (45.4):

Boy (45.5)
e et o

In a homogeneous medium of constant conductivity ¢ and constant magnetic permeability 4, the factor 1/o can be taken in front of the curl operator,
and by (45.3) we have divB = divH =0. Hence curl curl H = — AH,
and we obtain the equation

4npo 0H
AH 2h (45.6)
With the equation div H = 0 this suffices to determine the magnetic field.
It may be noted that equation (45.6) is a heat-conduction equation, the
thermometric conductivity y being represented by ¢?/4y0.
The boundary conditions on the magnetic field at the surface of a conductor are evident from the form of the equations, and are as before
Bu = Bn, Ha = Hr. (45.7)
+ For poor conductors (e.g. semiconductors), equation (45.4) is valid only if a further
condition, which may be more stringent, is satisfied. For such bodies it may be possible to
define both a conductivity and a dielectric constant. Then a term — (¢/c) @E/ét is added
to the right-hand side of (45.4), and the condition for this term to be small in comparison
with 470E/c is o/wS> . In good conductors (e.g. metals), on the other hand, o/w > 1
throughout the frequency range in which the conductivity can be regarded as constant (see
also the sixth footnote to this section).

|
188 Quasi-static Electromagnetic Field 45
The expression on the right-hand side of equation (45.4), being bounded,
does not affect the second of (45.7). For # = 1 we can put simplyt
Hi = Bp. (45.8)

The continuity of H; implies that of (curl H), and therefore, by (45.4),
that of (cE),. Outside the conductor, ¢ = 0, and we therefore conclude
that on the surface En; = 0, where the suffix 7 denotes the field inside the
conductor. Since Ey is zero, so is jn = cEy. Thus the system of equations
under consideration necessarily implies the vanishing of the normal component of the current density on the surface of the conductor. In other |
words, in this approximation a variable magnetic field cannot cause the
appearance of free charges on the surface of the conductor.

The boundary condition (45.8) is insufficient for a complete formulation
of the problem if the conductor is composite and its parts have different conductivities. At the interfaces between the parts we must use both the
continuity of H and that of E;; the latter implies the condition

(curlH)/o1 = (curl H)2/o2 (45.9)
on the magnetic field.

Having established the basic equations, let us now examine the nature of
the variable fields which they describe. Suppose that a conductor is placed
in an external magnetic field which is suddenly removed. The field in and
around the conductor does not vanish immediately; the manner of its decay
with time is given by equation (45.6). To solve a problem of this kind, we
use the following procedure. We seek solutions of equation (45.6) which
have the form H = H,,(x, y, z)e~7!, where ym is a constant. The equation
for the function H,»(x, y, 2) is then

(2/470) Hm = —ymHm- (45.10)
For a conductor of given shape, this equation has non-zero solutions (satisfying the necessary boundary conditions) only for certain ym, the eigenvalues
of (45.10), all of which are real and positive. The corresponding functions

+ For ordinary diamagnetic and paramagnetic bodies, » is very nearly 1, and the inclusion
of 4 in the following formulae would be a pointless refinement. Values of » differing considerably from 1 occur in ferromagnetic metals, whose magnetic properties (in sufficiently weak
fields) can be described in terms of a large constant permeability. For quite moderate frequencies, however, such substances exhibit a dispersion of (i.e. a dependence of pon the frequency
w), together with a decrease of u almost to 1. We shall therefore put » = 1 in the present
one ris is easily seen as follows. So as to avoid having to take account of the boundary
conditions at the surface of the body, we start from equation (45,5) and suppose o to vanish
continuously outside the body. Multiplying both sides of the equation

— 4rymHm/c? = — curl [(1/0) curl Hn]
by Hn® and integrating over all space, we have
er f [Halt av = [Het-cut 2B ay = [*loustHtnl®av,
¢ o o
whence it is evident that the ym are real and positive.

§45 Eddy currents 189
Hyn(x, y, 2) form a complete set of orthogonal vector functions. Let the field
distribution at the initial instant be Ho(x, y, 2). On expanding this in terms
of the functions Hy:
Ho(295 2) = E emElm(%, 9 2)

we obtain the solution of the problem:

| H(x,y, 2,1) = Zcme-?m"Hn(x, 9, 2) (45.11)
gives the manner of decay of the field with time.

The rate of decay is determined principally by the term in the sum for
which ym is least; let this be 1. The ‘decay time” of the field may be defined
ast = 1/71. The order of magnitude of 7 is evident from equation (45.10).
Since AH ~ H/l2, where / is the dimension of the conductor, we have

7 ~ 4Anol?/c2. (45.12)
| Another type of problem concerns the behaviour of a conductor in an
external magnetic field which varies with frequency w. The magnetic field
penetrates into the conductor and induces in it a variable electric field,
which in turn causes currents to appear; these are called eddy currents.t
A general idea of the way in which the field penetrates into the conductor
can be obtained from the analogy already mentioned between equation
(45.6) and the equation of thermal conduction. It is known from the theory
of thermal conduction that a quantity which satisfies such an equation is
“propagated” through a distance ~ +/(x#) in time t, We can therefore
immediately conclude that the magnetic field penetrates into the conductor
to a distance 8, given in order of magnitude by 8 ~ +/(c?/ow). The same is
true, of course, of the induced electric field and currents.

Ina variable field of frequency «, all quantities depend on the time through

a factor e~, Equation (45.6) then becomes
AH = —4ricwH/c?. (45.13)

Let us consider two limiting cases. If the penetration depth 8 is large compared with the dimension of the body (low frequencies), we can put the righthand side of (45.13) equal to zero as a first approximation. Then the magnetic
field distribution at any instant will be the same as it would be in a steady
state with the same external field. Let this solution be Ht; it is independent
of the frequency (or rather involves the frequency only in the time factor
et), The induced electric field appears only in the next approximation,
being absent in the steady state. This corresponds to the fact that curl Het

= 0, and so the value of Est obtained from (45.4) is zero. To calculate E,

+ In Russian “Foucault currents”.

|
190 Quasi-static Electromagnetic Field §45
therefore, we must use equation (45.1), according to which
curlE = iwHs/c. (45.14)
This equation, together with div E = 0 (which follows from (45.4) when o
is constant in the body), entirely determines the electric field distribution.
It is seen to be proportional to the frequency w.

The opposite limiting case is that where 5 < / (high frequencies). The
condition for the macroscopic field equations to be applicable, mentioned at
the beginning of this section, requires that 8 should still be large compared
with the mean free path of the conduction electrons.t |

When 6 < / the magnetic field penetrates only into a thin surface layer of
the conductor. In calculating the field outside the conductor we can neglect
the thickness of this layer, ie. assume that the magnetic field does not
penetrate into the conductor at all. In this sense a conductor in a highfrequency magnetic field behaves like a superconductor in a constant field,
and the field outside it must be calculated by solving the corresponding
steady-state problem for a superconductor of the same shape.

The true field distribution in the surface layer of the conductor can be
investigated in a general manner by regarding small regions of the surface
as plane. It is necessary to solve equation (45.13) for a conducting medium
bounded by a plane surface, outside which the field has a given value
Hoe~, say. This vector is obtained as shown above, by solving the problem for a semi-infinite medium, and is parallel to the surface of the conductor.
The boundary condition (45.8) shows that the magnetic field in the conductor
is also Hoe“? at the surface.

We take. the surface of the conductor as the xy-plane, the conducting
medium being in z > 0. Since the conditions of the problem are independent of x and y, the required field H depends only on the z co-ordinate
(and on the time). We therefore have divH = 0H,/@z =0, and since
H, = 0 at the boundary it must be zero everywhere. By (45.13), the equation
for H is @H/é2?+k?H =0, where k = «/(4icw/c?) = (1+1)4/(270w)/c.
The solution of this equation which vanishes far from the surface is ef*2,
Using the boundary condition at z = 0, we obtain

H = Hoe*eiz/-tut (45.15)
where the penetration depth 6 is
8= c/4/(270w) and k = (1+1)/8. (45.16)

The electric field is now determined by means of equation (45.4). If n is

a unit vector in the z-direction, we have
E = V(w/8r0)(1-1)H xn. (45.17)
Thus E ~ H6/A.

+ This condition is, in fact, the first to be violated in metals as the frequency increases.
The condition w < 1/7, where 7 is the mean free time, may, however, be the more stringent
for semiconductors of low conductivity.

§45 Eddy currents 191
If the field Hye~* is “linearly polarised”, then Hp can be made real by a
suitable choice of the origin of time. We then take the direction of Ho as
the y-axis. Taking the real part in (45.16) and (45.17), we have
zB
H = Hy = Hoe-*cos G- at),
Fl (45.18)
zB
SO Hy (wltno)e-**c0s(2— ot).
The eddy current density j = oE has the same distribution as E.

The presence of eddy currents implies a dissipation of. the field energy,
which appears as Joule heat. The time average energy Q dissipated in the
conductor per unit time is Q = [j-EdV =f cE?dV. It can also be calculated
as the mean field energy entering the conductor per unit time:

Q = fB-df = (c/4n)fExH-af, (45.19)
the integral being taken over the surface of the conductor. t

We have already seen that, in the limiting case 5 > J, the amplitude of the
magnetic field inside the conductor is independent of the frequency, while
that of the electric field is proportional to w. The energy dissipation Q at
low frequencies is therefore proportional to w®, When 6 < J, on the other
hand, the magnetic and electric fields on the surface of the conductor are
given by formulae (45.15) and (45.17) with z = 0. The Poynting vector is
normal to the surface, and its mean value is 5 = (¢/16m)\/(w/270)|Hol?,
the variation of Hp over the surface being given by the solution of the problem of the static field outside a superconductor of the same shape (cf. above).
The energy dissipation is

c w
=— /—— Pdf. 45.20)
2 es {ie i. ‘ )
Thus at high frequencies it is proportional to ~/w.

The energy dissipation can also be expressed in terms of the total magnetic moment JM acquired by the conductor in the magnetic field. In a
periodic field, the magnetic moment is likewise a periodic function of time,
with the same frequency. According to formula (31.4), the rate of variation
of the free energy is given by —.@-d§/dt, where § is a uniform external

} If any two quantities a(2) and b(¢) are written in ccmplex form (proportional to el),
the real parts must of course be taken before calculating their product. If, however, we are

interested only in the time average value of the product, it may be calculated as 4 re ab*.
‘The terms containing e#%#t give zero on averaging, and so ¢(a+a*)O+0%) = Y(ab*-+a*b).
In particular, 8 can be calculated as the real part of the “complex Poynting vector””:
g- re[ St x |. (45.19a)

|
192 Quasi-static Electromagnetic Field 445 i
field in which the conductor is placed. This expression does not immediately give the required energy dissipation, because the energy of the body
changes not only on account of dissipation but also by the periodic movement of energy between the body and the surrounding field. If we average
over time, however, the latter contribution vanishes, and the mean dissipa‘tion of energy per unit time is
Q = —A-dg/at. (45.21)
If M and § are written in complex form, then dH/dt = —iwf, and Q can
be calculated as
'Q = —hre(inM-H*) = tw im(M-H*). (45.22)
The origin of the factor 4 is explained in the last footnote.

The components of the magnetic moment # are linear functions of the
external field:

AM, = VairDn, (45.23)
where the dimensionless coefficients «(w) depend on the shape of the body
and on its orientation in the external field, but not on its volume V. In this
formula we assume that and § are written in complex form, so that the
%x are also in general complex. The tensor Vaix may be called the magnetic
polarisability tensor for the body as a whole. This tensor is symmetrical:+

ik = Opt. (45.24)
We can therefore write
MD = Vai Si* He= Vain Hi* Hx + HiHe*)
= Vox re(SiHx*).
If also we write the complex quantities a as az’ +io4x”, the energy dissipation (45.22) becomes
OQ = Werna!’20( S54). (45.25)

Thus the energy dissipation is determined by the imaginary part of the
magnetic polarisability. We have already seen that Q is proportional to w2
for low frequencies, and to »/w for high frequencies. We can therefore
conclude that the quantities a,’ in these two limiting cases are proportional
to w and to 1/+/w respectively. Since they decrease both as w >0 and
@ > 00, they must have a maximum in between.

The magnetic moment of a conductor in a variable magnetic field is due
mainly to the conduction currents set up in the body; it is not zero even if
» =1, when the moment in a constant field vanishes. The latter can be
obtained from .#(w) by taking the limit as w +0. Hence it follows that
the real part oi’ of the polarisability tends to a constant limit as w +0

+ See Statistical Physics, §124, Pergamon Press, London, 1958.

$45 Eddy currents 193
(the limit being zero for » = 1), corresponding to magnetisation in a constant
field. In the limit w -> 00, when the magnetic field does not penetrate into
the body, a’ tends to a different constant limit, corresponding to the steady
magnetisation of a superconductor of the same shape.

PROBLEMS

ProseM 1. Determine the magnetic polarisability of an isotropic conducting sphere of
radius a in a uniform periodic external field.

Souutton. The field Hy inside the sphere satisfies the equations AH;+iH;, = 0,
divH; = 0, where k = (1-+i)/8. We write this field in the form Hy = curl A, where A
satisfies the equation AA+H%A = 0; since H is an axial vector, A is a polar vector. By
symmetry, the only constant vector on which the required solution can depend is the external field §. We denote by f the spherically symmetrical solution, finite for 7 = 0, of the
scalar equation Af+h%f = 0, namely f = (1/r) sin kr. ‘Then the polar vector A, which
satisfies the vector equation AA+#A = 0 and depends linearly on the constant axial
vector §, can be written as A =f curl (f%), where f is a constant. Thus we have ’

Hy = B curl curl (f 9)
if? ap?
= of Z +97) 5—0L +4 )om-690,
where n is a unit vector in the direction of r; the second derivative f ” has been eliminated
by means of the equation Af+k®f = 0.

The field Hz outside the sphere satisfies the equations curl H, = 0, divH, = 0. We
put H, = —grad $+9; ¢ satisfies the equation Ag = 0 and vanishes at infinity. Since ¢
depends linearly on the constant vector $, we have $= —Va $-grad(1/r), where
V = 4na®/3. Thus

H, = Va grad [(H-grad)(1/r)]+
Va
= B(a-$)n—$1+ 9.
It is evident that Vag is the magnetic moment of the sphere, so that Va is its magnetic
polarisability (by symmetry, the tensor a reduces to a scalar «5it).

‘On the surface of the sphere (r = a), all the components of H must be continuous. Equating separately the components parallel and perpendicular to n, we obtain two equations to
determine « and B. The polarisability per unit volume is found to be

pnp 3.3
am ebie” = -g[- at qo),
5d fs 38 sinh (2a/8)—sin 20/9)
«= ~ Bal’ 2a cosh (2a/8)—cos (2a/8)1”
oe fi a sinh (2a/3)-+sin Gai)
~*~ F6natl” ~ 8 cosh (2a/8)—cos (2a/8)1"
In the limit of low frequencies (55> a),
, 1 (¢ 4 fn atotat
— insals) ~~ {0s a?
nwt (e) =<
= 20m ) = Foe
For high frequencies (5 <a),
, 3 [: 33] 3 [i 3c |
a = —2f1—-=2] = —=f1-—__*_
Sal’ 2a Sal’ 2aVQnow)!
98 9c
a” == =
l6ra = 16nax/(270w)

194 Quasi-static Electromagnetic Field §45
‘The limiting value Vx’ = —4a corresponds to the magnetic moment of a superconducting
sphere; the corresponding value of «” could be found from formula (45.20), using the
expression (42.3) for the field at the surface of a superconducting sphere.

Prostem 2. The same as Problem 1, but for a conducting cylinder (of radius a) in a
uniform periodic magnetic field perpendicular to its axis.

Souvtion. This problem is the “two-dimensional analogue” of Problem 1. In what
follows all vector operations are two-dimensional operations in a plane perpendicular to the
axis of the cylinder, and r is the radius vector in that plane. ‘The field inside the cylinder
is of the form

Hy = curl curl (f $)
yf? oe
= (5 +47) 9-0(— +H) 0-590, |
where f = Jo(kr) is the symmetrical solution of the two-dimensional equation Af+Af=0 |
which is finite for r = 0. The field outside the cylinder is
H, = —2Va grad [(§-grad) log r+
2Va
- SE pta-$)n-9)+5,
where 7 = na®. The magnetic moment per unit length of the cylinder is Va (see §3,
Problem 2). From the condition Hy = H, for r = a, as in Problem 1, we obtain
i fi 2 Tia))
a= —2f1- 22
Jal ka Jo(ka)?
using the relation Jo((kr) = —kji(kr).
For 55> a, expanding the Bessel functions in powers of ka, we have
1 fayt—_ atow?
oe -3() ao
Daa\5 oe
aot (2) aow
w= (2) = S22
Bn\5) ~ 48
For 8 <a, we use the asymptotic expressions for the Bessel functions, obtaining
2S ) OW aa/(Qnow))”
18 c
a
' Ia InaV Anew)

Prosiem 3. The same as Problem 2, but for a magnetic field parallel to the axis of the
cylinder.

Souution. The magnetic field is everywhere parallel to the axis of the cylinder. Outside
the cylinder we have Hy = §, and inside it Hi = f $, where f is the symmetrical solution of the two-dimensional equation Af+-k%f = 0 which is i for r = a and finite for
r= 0: Hy = $Jo(kr)|Jo(ka). ‘The eddy currents in the cylinder are azimuthal (i.e. the only
non-zero component is j4), and are given in terms of the field He = H by 4njle = —@H/er.
‘The magnetic moment generated per unit length of the cylinder by the conduction currents
is M = naaS = (1/20) fir dV = —}§(@H|éryr2 dr; it is parallel to the axis, Evaluating
the integral, we have

« 4 Zit
4b ka Joka)"
‘Thus the longitudinal polarisability of the cylinder is half the transverse polarisability derived in Problem 2.

Prostem 4. Determine the least decay coefficient for the magnetic field in a conducting

sphere.

§46 The skin effect 195

SOLUTION. The solutions of equations (45.10) for a sphere include functions of various
symmetries. ‘The most symmetrical solution is that which is defined by an arbitrary constant
scalar. This solution is inapplicable, however, for the following reason: it would be spherically symmetrical (H = H,(r)) and would have to be H = constant/r in order to satisfy the
equation div HH = (1/r)a(rH)/ér = 0, which is valid both outside and inside the sphere;
but this function is not finite at the centre of the sphere.

‘The least value of y corresponds to one of the solutions defined by an arbitrary constant
vector. The form of these solutions is evidently the same as has been found in Problem 1,
the only difference being that the constant term in the field He must be omitted so as to
have H = 0 at infinity. ‘The quantity k is now real (=-/(4noy/c%)), and the vector § is
the arbitrary constant vector. From the boundary condition Hy = H, at r = a we obtain
two equations, and on eliminating « and f we find sin ka = 0. ‘The smallest non-zero root
of this equation is ka = 7, and so the smallest value of y is 7c*/4oa®.
$46. The skin effect

Let us consider the distribution of current density over the cross-section
of a conductor in which a non-zero and variable total current is flowing.
From the results of §45 we should expect that, as the frequency increases,
the current will tend to be concentrated near the surface of the conductor.
This phenomenon is called the skin effect.

The exact solution of the problem of the skin effect depends, in general,
not only on the shape of the conductor but also on the manner of excitation
of the current in it, ie. the nature of the variable external magnetic field
which induces the current. An important particular case, however, is that
where the current flows in a wire of thickness small compared with its
length; here the current distribution is independent of the manner of
excitation.

In calculating the current distribution over the cross-section of a thin
wire, the latter may be regarded as straight. The electric field is parallel to
the axis of the wire, and the magnetic field vector H is in a plane perpendicuJar to the axis.

Let us consider a wire of circular cross-section. This is a particularly
simple case, because the form of the field outside the wire is immediately
obvious. By symmetry, E = constant over the surface of the wire (though
the value of the constant varies with time). With this boundary condition,
the only solution of the equations div E = 0, curlE =0 outside the wire
is E = constant. Similarly, the magnetic field outside the wire must be the
same as it would be outside a wire carrying a constant current equal to the
instantaneous value of the variable current.

Inside the wire, the electric field satisfies the equation AE = (4ro/c®)dE/at,
which is the same as equation (45.6) for H; it is obtained by eliminating H
from (45.1) and (45.4), just as (45.6) was obtained by eliminating E. In
cylindrical co-ordinates, with the 2-axis along the axis of the wire, the only
non-zero component of E is Ez, which depends only on r. For a periodic
field of frequency w we have

10/ 6E V(2i) Ati
-—(r—]+RE = 0, k= —— =, 46.1
r al or ) , 8 5 (46.1)

196 Quasi-static Electromagnetic Field 46
where 6 is the penetration depth (45.16). The solution of this equation
which remains finite at r = 0 is

E = E, = constant x Jo(kr)e-, (46.2)
where Jo is the Bessel function. The current density j = oE is similarly
distributed.

The magnetic field H; = H is found from the electric field by equation
(45.1):

iwH,Jc = (curlE), = — aE;/ér. (46.3)
Since Jo'(u) = —Ji(u), we obtain
H = Hy = — constant x ix/(4r0i]) fa(hr)e-t, (46.4)
the constant being the same as in (46.2); it is easily determined from the
condition that H = 2J/ca on the surface of the wire, a being the radius of the
wire and J the total current in it.

In the limiting case of low frequencies (a/8 < 1) we can take the first few
terms of the expansions of the Bessel functions at every point in the crosssection:

a 1
E, = constant x [i ~ r18P— 55018] ett,
(46.5)
H, tant x yf 1 jsy-—2 15] tot,
= x—r] 1-4 - Feds
[s = constant 7 -| rad 7B" e
The amplitude of E, and therefore that of the current density, increase as
1+ (7/28)* with increasing distance r from the axis.

In the opposite limiting case of high frequencies (a/5 > 1) we can use
the asymptotic formula

Sofu/(2i)] ~ u-tel-ou, (46.6)
- which is valid for large values of the argument, over most of the cross
section. Retaining only the rapidly varying exponential factor, we have

Ez = constant x e~@-r¥etia—10-tw ,
, (46.7)
ro
H, = constant x (1+i) | ee reat,
w

These formulae are, of course, the same as (45.15)-(45.17), which are valid
near the surface of a conductor of any shape when the skin effect is strong.

In the general case of a wire whose cross-section is not circular, the exact
calculation of the skin effect is considerably more involved, since the fields
inside and outside the wire must be determined simultaneously. Only in the
limiting case of strong skin effect is the problem again simplified, because
the field outside the wire may then be determined as the static field outside
a superconductor of the same shape (§45).

§47 The complex resistance 197

## Section §47: The complex resistance

If the frequency of the variable current is low, the instantaneous current

Jit) in a linear circuit is determined by the instantaneous e.m.f. &:
&) = RIO, (47.1)
where R is the resistance of the wire to a constant current. !

There is no reason, however, to expect a direct relation between the
values of & and J at the same instant for all frequencies. We can say only
that the value of J(#) must be a linear function of the values of &(¢) at all
previous instants. This relation may be symbolically written as J = 2-16
or, conversely,

é=Z), (47.2)
where Zis some linear operator.t If the functions &() and J(¢) are expanded
as Fourier integrals, then for each “monochromatic” component (depending
on time through a factor e~), the effect of the linear operator Z is simply

multiplication by a quantity Z which depends on the frequency:
€ = Z(w)J. (47.3)
The function Z(w) is in general complex. It is called the complex resistance
or impedance of the conductor.

It is evident from a comparison of (47.3) and (47.1) that the ordinary
resistance R is the zero-order term in an expansion of the function Z(w)
in powers of w. To find the next term, we must take account both of R and
of the self-inductance L of the conductor.}

Let us consider a linear circuit containing a variable e.m.f. &(t). By the
definition of &, the work done per unit time by the electric field on the
charges moving in the wire is €J. This work goes partly into Joule heat and
partly to change the energy of the magnetic field of the current. By the
definition of R and L, the Joule heat evolved in the wire per unit time is
RJ?, and the magnetic energy of the current is L,J?/2c?.. The law of conservation of energy therefore gives the equation

d Lp 1a
6] = RP? +—— = RP+—L)-,
T= RP a8 P+ Jy
or
1d
€ = RJ+—L—. 47.4

U+ale, (47.4)

+ We shall not pause here to discuss the general properties of this operator, since they
are enticely analogous to those of the operator 2, which will be examined in detail in §§58
°"f Here, and in what follows, R and L denote the values for constant current.

198 Quasi-static Electromagnetic Field 47

In order to use the quadratic expressions @J and J? we must write
& and J as real functions. Having derived the linear equation (47.4), however, we can take complex monochromatic components: & = &e~,

J =Joe~t. Then equation (47.4) gives the algebraic relation
e= (R-5et) oA
a
whence
i
Z= Rol. (47.5) |
Taking the real part in J = &/Z, we have
&
t) = —_—_____ t—$), tang = wL/c?R, 47.6
JO = Fea et) tend = oL/PR (47-6)
which determines the amplitude of the current and the phase difference
between the current and the e.m.f.

The real part of the expression (47.5) is the resistance R, which determines the energy dissipation in the circuit. It is easy to see that, whatever
the function Z(w), a similar relation holds between re Z and the energy
dissipation for a given current. On averaging with respect to time the power
&J required to maintain the periodic current in the circuit, we obtain the
part of this power which continually makes good the dissipative losses. The
energy dissipation in the circuit per unit time is therefore Q = $re (€J*),
where & and J are expressed in complex form; see the penultimate footnote
to ¥45. Substituting & = ZJ and denoting the real and imaginary parts of
Z by Z’ and Z” respectively :t

Z= 2Z'+iZ", (47.7)
we obtain Q = }$2Z’[J/? or, in terms of the real function J(t),

Q = 2(o)f, (47.8)
which gives the required relation.

It may be noted that, since Q is necessarily positive, Z’ is also positive:

Z>0. : 47.9)

We may calculate Z(w) for a wire of circular cross-section for any frequency,t i.e. without neglecting the skin effect. To do so, we again use the
law of conservation of energy, but in a different form. We divide the power
&J (where & and J are real) into two parts, one being the change in the
magnetic field energy outside the wire, and the other the total energy consumed inside the wire (both in changing the field and in evolution of

+ Sometimes called the resistance and reactance (in Russian: active and reactive resistances).

t That is, any which satisfies the quasi-steady condition.

447 The complex resistance 199
heat). The second part can be calculated as the total energy flux entering
the conductor through its surface per unit time. Thus we have
d/L.J?\ cEH Le Ay
6] = ——_)+—— - 2nal = —J——+ 3cEHal,
J a 2c + Tap cl ater rata
where Le is the external part of the self-inductance of the wire, E and H
the electric and magnetic fields at its surface, a its radius, and / its length.
The field H is related to the current J by H = 2J/ca. Hence, dividing the
above equation by J, we have
1g
é€ =—L.— +H.
ode +
This is a linear equation, and hence we can use complex quantities. Then ‘
ae ser
2
whence
5
tw EL iw 2El
Z = -=1e+— = —-—Le+—.. 47.10
2 a J ait caH ¢ )
For general frequencies, E and H are given by (46.2) and (46.4), and we
have
ten Jo(a)
Z = ——I,+4}Rka—_, 47.11
mma (7) (47.11)
where R = I/na2c. When the skin effect is weak, we use the expansions
(46.5); taking terms as far as (a/8)4 and separating the real part, we find
z R(t , ( ait : (=")' 47.11
=Rittaels) | Ri tala) | 7)
In the opposite case of a strong skin effect we use the expressions (46.7),
obtaining
Z = Raj28 = (I[ca)x/(w/270), 47.12)
ze o tet 1] a) [z+ Ic |
ee [ a} oa an/(2row))”
It is seen from (47.11a) that we can put Z’ = R if (mowa?/c?)? < 12. We
also have Z”/Z’ = wL/2R = (rowa?|c?) 2 log (Ia), where L is given by
(33.1). Comparing this with the inequality just given, we see that the range
of frequencies in which the expression (47.5) can be used to take the selfinductance into account depends on the ratio J/a and is fairly narrow.

In practice, however, the most important case is that in which the selfinductance of the circuit is due mainly to coils in it, whose self-inductance
is large compared with that of an uncoiled wire (see §33). In such circuits

200 Quasi-static Electromagnetic Field 47
formula (47.5) (i.e. equation (47.4) with constant R and L) can be used
over a fairly wide range of frequencies.

Let us consider a circuit in a variable external magnetic field H., which
may be generated in any manner. We denote by E, the electric field which
would be induced by the variable field Hy in the absence of conductors. Both
H, and E, vary only very slightly over the thickness of a thin wire (unlike
the field of the currents in the wire). We can therefore discuss the circulation of E, round the current circuit without specifying the exact position of
the contour of integration in the wire. This circulation is just the e.m.f. &
induced in the circuit by the variable external magnetic field. By the integral |
form of Maxwell’s equation we have

10 1do,
6 = oE,-dl = —-—|H,-df = —-—_, 47.13
f : c al c dt’ ( )
where ®, is the flux of the external field through the circuit. Substituting
this expression in equation (47.4), we obtain.
1d 1d®
RJ+—L— = --—. 47.14)
y+ e dt ce dt ( )
Taking the self-inductance term to the right-hand side, we have
1d® Ld 1d®
RJ = 2 _2y | ———
e dt cdt ec dt
where © = ©,+L/]/c is the total magnetic flux from the external magnetic
field and the field of the current. In this form the equation gives Ohm’s
law for the whole circuit, i.e. the equality of RJ to the total e.m.f. in the
circuit.

The formulation of equation (47.14) as expressing Ohm’s law makes possible a generalisation of it to the case where the shape of the circuit also
varies with time. The self-inductance L is then a function of time, and
(47.14) becomes

Ry= 2 y-1 2% (47.13)
dt c dt" :
In deriving this from the law of conservation of energy we should have to
take into account also the work done in deforming the conductor.

If there are several circuits in proximity, carrying currents Ja, then for
each of them ©, in equation (47.14) is the sum of the magnetic fluxes due to
all the other circuits (and to the external field, if any). The magnetic flux
through the ath circuit due to the current Jy is LanJofc, where Lap is the
mutual inductance of the two circuits. We therefore have the following
set of equations for the variable currents in the circuits:

1 do
Reet Danae = Se (47.16)

47 The complex resistance 201
The sum over 6 includes the self-inductance term (b =a), and & is the
e.m.f. produced in the ath circuit by sources external to the system of
currents considered.

For periodic currents of a single frequency, the system of differential
equations (47.16) becomes a set of algebraic equations:

EZarJo = Ea, (47.17)
where the quantities
iw 7
Zan = BarRa—Flar (47.18)
form the impedance matrix. Like (47.5), the expressions (47.18) represent

the first terms in an expansion of the functions Zjy(w) in powers of the

_ frequency.

] It should be noted that, in this approximation, the circuits have no mutual
effect on the real parts of their impedances. Such an effect arises because
the magnetic field of the variable current in one conductor generates eddy
currents, and therefore an additional dissipation of energy, in the other
conductor. For linear conductors this effect is negligible, but it may become
important if extended conductors are located near them.

Finally, let us consider how the equations of variable currents in linear
circuits obtained in this section are related to the general equations of a
variable magnetic field in arbitrary conductors. We shall take the simple
example of the current set up in a circuit when a constant e.m.f. & is
removed at time ¢ = 0. From equation (47.4) we havet

= &/R for t < 0,
J | : (47.19)
J = (60/R)e-PR for t > 0.
We see that, after the removal of the e.m.f., the current decays exponentially
with time, the decrement being
y = ORL. (47.20)
If the problem is exactly formulated, this y is the smallest of the ym obtained
by solving the exact equation (45.10) for the conductor in question. Among
the ym for a linear conductor there is one, the smallest, which is less than
the others by a factor of the order of log (//a), and this is (47.20).

t Strictly speaking, these formulae are invalid for very small t, when the high-frequency
terms in the Fourier expansions of the functions are important and so equation (47.4) cannot
be used. During this short interval of time, however, the current J cannot change significantly, and so formula (47.19) gives the current at subsequent times with sufficient accuracy.

,

202 Quasi-static Electromagnetic Field §48

## Section §48: Capacity in a quasi-steady current circuit

A variable current, unlike a constant one, can flow in an open circuit as
well as in a closed one. Let us consider a linear circuit whose ends are connected to the plates of a condenser, which are at a small distance apart.
When a variable current flows in the circuit, the condenser plates will be
periodically charged and discharged, thereby acting as sources and sinks of
current in the open circuit.

Since the distance between the condenser plates is small, the magnetic
energy of the current can again be taken as LJ?/2c2, where L is the self- |
inductance of the closed circuit which would be obtained by joining the |
condenser plates by a short piece of wire. In applying the law of conservation of energy, however, we must take into account not only the magnetic
energy but also that of the electric field in the condenser. The latter energy
is e?/2C, where C is the capacity of the condenser and + e(t) the charges on
its plates. Proceeding as in the derivation of equation (47.4), we obtaint

dLlf? d & 1_ dj ede
6] = RP + tan = RP+ GI +
J = RY dt 2c2 dt 2C ey a Jay Cdt
The current J is equal to the rate of decrease and increase of the charges on
the two plates: J = de/dé. Dividing both sides of the equation by J and
expressing J in terms of e, we have
1_d’e de e
—L—+R—+— = @€. 48.4
@ de® dt C (48.1)
This is the required equation for a variable current in a circuit with a capacity.

If & is a periodic function of time having frequency w, then equation
(48.1) reduces to an algebraic relation between & and the charge e, or between
@ and the current J = — iwe. We have, in fact, JZ = &, where the impedance
Z is defined by

Z=R (< 1 ) (48.2)
Z = R-i{(—-—). :
2 wl,
Taking real parts in the relation J = &/Z, we obtain
&ocos (wt—¢)
t) = ——_*
JO = ort }
fo pe
Jl®(e-ce) |
(48.3)
oL 1)\1
tang = (=-—)>
2 wC/R .
which give the current in a circuit to which an external e.m.f. & = & cos wt
is applied.
+ In the present section we neglect the skin effect.

48 Capacity in a quasi-steady current circuit 203 ,

If & =0, the current in the circuit consists of “free” electric oscillations.
The (complex) frequency of these oscillations is given by Z = 0, whence

Re f J ca x) (48.4)
en or* Fea Gz . "
We may have either periodic oscillations damped with decrement Ree/2L
or an aperiodically damped discharge, depending on the sign of the radicand.
In the limit as R +0 we have undamped oscillations whose frequency is
given by Thomson’s formula: w = ¢/-/(LC).

Equation (48.1) can be immediately generalised to a system of several
inductively coupled circuits containing condensers. The current Ja in the
ath circuit is related to the charges + eq on the corresponding condenser by
Ja = dea/dt, and equation (48.1) is replaced by the set of equations

1. dey dea a
—Lav— + Ra + — = 6a 48.5
2a wget Reg te = (48.5)
|
For periodic (monochromatic) currents, these equations give the algebraic
equations
ZZavfo = 6u (48.6)
the matrix elements Zap being given by the formulae
i iw
Zav = Bao( Rat) ~G lav (48.7)
wCg)
The eigenfrequencies of the current system are given by the condition of
compatibility of equations (48.6) when & = 0, ie. by the condition for the
determinant |Zgp| to vanish:
|Zav| = 0. (48.8)
If the resistances R are not zero, all the “frequencies” have a non-zero imaginary part, and the electric oscillations are therefore damped.

It should be noticed that equations (48.5) are formally identical with the
mechanical equations of motion of a system with several degrees of freedom
which executes small damped oscillations. The generalised co-ordinates
are represented by the charges ea, and the generalised velocities by the
currents Jg = dea/dt. The “Lagrangian” of the system is

1 -_ ea?
g= Daaleeto- Doc, +2 Su (48.9)

\
204 Quasi-static Electromagnetic Field 448
The kinetic and potential energies of the mechanical system are represented
by the magnetic and electric energies of the current system, and the quantities & correspond to the externally applied forces which cause the forced
oscillations of the system. The quantities Ra appear in the dissipative

function

R = & 3 Rae. (48.10)

Equations (48.5) are the analogues of Lagrange’s equations |

d af 0 OR (48.11) /

dt dé, dea em : |

PROBLEMS

ProsteM 1. Determine the eigenfrequencies of electric oscillations in two inductively
coupled circuits containing self-inductances Li and Lz and capacities C1 and Ca, neglecting
the resistances Ry and Re.

SoLuTIoN. The required frequencies are determined from the condition

.— [Zaol = Z1Ze2—Zis? = 0,
where
o 1 o 1 iw
m=-(2n-+), z = -i($u-—), Zum — “in,
we i(Qa 2), m= (te), ta ln
Calculation gives
am plat LACrt VUE LaCs)* + 4C,CoL a4]
oun 2C:Ca(LiL —Lis*) .

Both frequencies are purely real, owing to the fact that Ri and Re have been neglected. As
Lia 0, w1 and wa tend to ¢//(LiCy) and ¢//(L2C2). These are the frequencies for the two
circuits separately.

Prostem 2. The same as Problem 1, but for a circuit consisting of a resistance R, a
capacity C and an inductance L connected in parallel.

Sotution. The impedances of the three branches are Zi=R, Zz=1i/wC,
Zs = —iwL/c®, and the currents in them are such that Jit+Je+Js = 0, Z1J: = ZaJ2= ZsJs.
Hence we have 1/Z:+1/Z2+1/Zs = 0, whence

_ ‘i - A [ Gal 1
eo ~ 2RE *N LEC ac]:

PROBLEM 3. Discuss the propagation of electric oscillations in a circuit consisting of an
infinite succession of identical meshes containing impedances

w 1 w 1
=-i(Sn-—) “= -i(2n-—},
oe (3 * aa) ° (Gs wa)
as shown in *Fig. 25. Find the range of frequencies which can be propagated in the circuit*
without damping. t

+ The condition for the quasi-steady theory to be applicable to such a periodic circuit is

that the dimension of one mesh should be small compared with the “wavelength” c/w.

$49 Motion of a conductor in a magnetic field 205
SoLuTion. The current in mesh « is denoted by iz, as shown in *Fig. 25. Kirchhoff’s*
second law gives for this mesh Ztia-+Za(2ia—ia-1—ia+1) = 0. This is a linear difference
equation in the integral variable «, with constant coefficients. We seek the solution in the
form ia = constant x q*, obtaining for the parameter q the equation
Zi
a—(2+ Z)att =0. a
Z;

Let —4Z Z:/Z2<0, corresponding to values of w* lying between c/LiCi and
(4/Ca+1/C1)(4L2+L1). Then equation (1) has two complex conjugate roots with moduli
q| =1. This means that the current does not decrease from one mesh to the next, i.e. the
electric oscillations are propagated in the circuit without being damped. Putting q = eft,
where J is the length of one mesh and & is the “‘wave number” of the oscillations propagated

| in the circuit, we can calculate the velocity of propagation u from the general result
u = du/dk.
Fic. 25 ,

If, however, w is outside the range mentioned, equation (1) has two real roots qi and qa,
say; since qiga = 1, one root (q1, say) is less than 1 in absolute magnitude, while qa is greater.
It is easy to see that the propagation of undamped oscillations in the circuit is then impossible. To elucidate the reason for this, let us consider a circuit of large but finite length.
An initial oscillatory impulse is given to one end of the circuit, the other end being closed in
some manner. This closure corresponds mathematically to a certain boundary condition,
by means of which we can determine the ratio of the coefficients cx and cz in the general
solution c1q1~(*k-®) + cqo~("x-*), where a is the “‘co-ordinate”’ of the end of the circuit. This
ratio is of the order of unity. As ax—a increases, the second term in the solution rapidly
becomes very small compared with the first term, because |gz| > 1. Thus the solution is
ia = cigi~*k-®) everywhere except for a small part near the end of the circuit, and |ia| decreases towards the end of the circuit.

It should be emphasised that this damping does not involve dissipative absorption, because
there is no resistance in the circuit; it can be imagined as being the result of reflection of
the oscillatory impulse from each successive mesh of the circuit.

## Section §49: Motion of a conductor in a magnetic field

Hitherto we have tacitly assumed that a conductor in an electromagnetic
field is at rest in the frame of reference K in which E, H, etc. are defined.
In particular, the relation j = oE between the current and the field is generally
valid only for conductors at rest.

To determine the corresponding relation in a moving conductor, we
change from the frame K to another frame K’ in which the conductor, or
some part of it, is at rest at the instant considered. In this frame we have
j = EF’, where E’ is the electric field in K’. The well-known formula for
the transformation of fieldst gives E’ in terms of the fields in K:

E’ = E+vxBjc, (49.1)

+t. See The Classical Theory of Fields, §3-10, Addison-Wesley Press, Cambridge (Mass.)

1951; Pergamon Press, London, 1959. ‘he microscopic values of the electric and magnetic
fields are replaced by their averaged values € = E, h = B.

206 Quasi-static Electromagnetic Field 49
where v is the velocity of K’ relative to K, i.e. in this case the velocity of the
conductor, which we of course suppose small compared with the velocity of
light. Thus we find

j= o(E+vxBj/c). (49.2)

This gives the relation between the current and the field in moving conductors. The following remark should be made concerning its derivation.
In going from one frame of reference to the other we have transformed the
field but left the current j unaltered. The correct transformation of the
current density gives only terms of a higher order of smallness if v < c.
In formula (49.2) the second term, which appears as a result of the field |
transformation, is in general not small compared with the first term, despite |
the factor v/c. For example, if the electric field is due to electromagnetic induction from a variable magnetic field, its order of magnitude contains a factor
1/c as compared with the magnetic field.

The energy dissipation in a conductor when a given current flows in it
cannot, of course, depend on the motion of the conductor. The rate of
evolution of Joule heat per unit volume in a moving conductor is therefore
given in terms of the current density by the same expression j2/o as for a
conductor at rest. The expression j-E, however, is replaced byt j?/o
= j-(E+vxB/c).

Thus, in a moving conductor, the sum E+vxB/e acts as an ‘‘effective”’
electric field producing the conduction current. Hence the e.m.f. acting
in a closed linear circuit C is given by the integral

& = G(E+-vxBie)-dl. (49.3)
c
This expression can be transformed as follows. According to Maxwell’s
equation, curl E = —(1/c)@B/dt, and so
1@é
gE-dl = [curl E-df = -2< {peat
cc is c arg
or, denoting by © the magnetic flux through the surface S, which spans the
circuit C,
1/8
fE-dl = (5) .
c\ dt /v=0

t It is seen from this formula that the additional heat evolved in time 8t in a conductor

moving in a magnetic field is

Btfj-vxBdV/c = —fujxBdV ic,
where u = vot is the displacement in time 5t. This expression is equal and opposite to the
work done on the conductor in time 5t by the volume forces f= jx B/c. This explains the
apparent contradiction mentioned in §34.

§49 Motion of a conductor in a magnetic field 207
The time derivative with the suffix v = 0 denotes the rate of change of the
magnetic flux due to the time variation of the magnetic field, the position of
the contour C remaining unchanged.
In the second term in (49.3), we put v = du/dt, where du is an infinitesimal
displacement of the circuit element d/. Then
gv xB-dl = fduxB-dl/dt = - §B-df/de,
c 8
where df = duxdl is an element of area on the “‘side” surface s between
two infinitely close positions C and C’ of the current circuit, which it occupies
at times ¢ and t+dé (*Fig. 26). Since the total magnetic flux through any*
closed surface is zero, the flux through s must evidently equal the difference
of the fluxes through surfaces spanning C and C’. Thus
vxBedl = —(00/0t)B-constant,
e
where the time derivative denotes the rate of change of the magnetic flux due
to the motion of the conductor in a constant field.
s, S ‘
Fic. 26
Adding the two terms, we have finally
6 = —(1/c)d@/de, (49.4)
where the time derivative now denotes the total rate of change of the magnetic
flux through the moving circuit. Thus the expression (49.4), which is
Faraday’s law, is valid whatever the reason for the change in the magnetic
flux, whether variation of the field itself (already discussed in §47, formual
(47.13)) or motion of the conductor.

In a constant magnetic field, the change in the flux is due entirely to the
motion of the circuit. If the circuit moves in such a way that every point
of it moves along a line of force, then the flux through the circuit does not
vary. This is an obvious result of the fact that the magnetic flux through
any closed surface is zero, and the flux through the “‘side” surface described
by the moving circuit is in this case identically zero (since By = 0 on this
surface). Thus we can say that, to induce an e.m-f., the conductor must
certainly move so as to cross lines of magnetic force.

208 Quasi-static Electromagnetic Field 49

The electromagnetic field in a moving conductor is given by the equations

curlE = —(1/c)dB/2t,
curlH = 4yj/c = (4n0/c)(E+ vx B/c),
divB = 0.
Expressing E in terms of H by means of the second equation and substituting
in the first, we obtain
6B a curlH
—-curl B) = ——curl { ——}. 49.5
rr curl (v x B) Geourl ( a) (49.5) |
In a homogeneous conductor with constant conductivity o and constant |
magnetic permeability 4, we have
oF curl(vxH) = —“—AH, divH = 0. 49.6)
—-—curl(vxH) = ——-AH, =0. .
a trou au é
‘These equations generalise those obtained in §45.

It should be pointed out, however, that, if there is only one conductor
moving as a whole (without change of shape) in an external magnetic field,
then the solution of the problem is considerably simplified if we use a
system of co-ordinates fixed in the conductor. In this system the conductor
is at rest, and the external field varies with time in a given manner, so that we
return to the eddy-current problems discussed in §45. This possibility does
not depend on Galileo’s (or on Einstein’s) relativity principle, since the new
system of co-ordinates is in general not inertial. The equivalence of the
problems results from the above-mentioned fact that the electromagnetic
induction is independent of the cause of the change in the magnetic flux.
This equivalence can also be demonstrated mathematically. ‘To do so, we
expand the expression curl (vxB), using the facts that div B = 0 and (for
motion of the body as a whole) div v = 0 (i.e. the body is “incompressible”.
Then the left-hand side of equation (49.5) becomes

6B/dt+(v-grad)B—(B-grad)v. (49.7)
This sum is just the time derivative of B with respect to axes fixed in a
rotating body. For the sum of the first two terms is the “substantial” time
derivative dB/dt, which gives the rate of change of B at a point moving with
velocity v. The third term takes into account the change in the direction
of B relative to the body; it is zero for pure translation (v = constant) and
equals —2xB for rotation (v = Qxr, where Q is the angular velocity).

To conclude this section, let us consider the phenomenon of unipolar
induction, which occurs when a magnetised conductor rotates. If a stationary
wire is connected to the rotating magnet by means of two sliding contacts 4
and B (*Fig. 27) then a current flows in the wire. It is not difficult to calculate*
the e.m.f. which produces the current; the simplest procedure is to use a
system of co-ordinates rotating with the magnet. If Q is the angular velocity

$49 Motion of a conductor in a magnetic field 209
of rotation of the magnet, then in the new system the wire rotates with angular
velocity — 2, while the magnet is at rest. Thus we have a conductor moving
in a given constant magnetic field B duc to a fixed magnet. We neglect the
distortion of the field by the wire itself. According to formula (49.3), the
e.m.f. between the ends of the wire is
1 1
€=-— | vxBedl = —- | Bx(rxQ)-dl, (49.8)
c c
ACB ‘ACB
_ taken along the wire. This is the required solution.
2
- 4
re
Fic. 27
PROBLEMS

Prosiem 1. Determine the magnetic moment of a conducting sphere (with » = 1) rotating
uniformly in a uniform constant magnetic field, and the torque on the sphere.

SouuTION. Let the external field have components $2, 0, $2 in a fixed system of coordinates with the z-axis in the direction of the angular velocity vector 2. In a co-ordinate
system , 7, z which rotates with the sphere, the field components are Sz = Hz cos Mt,
‘9, = —Sz8in Mt, Gs, or, in complex form, Gz = Hee, Gy = —~IHxe-™, Ge.

"Thus variable fields of frequency @ act along the ¢ and 7 axes, and the magnetic moment
which they induce is

Me = V re (ae) = VGz(a’ cos +a” sin M1),

Mn = V re (2Gn) = VGx(—4’ sin Nt-+«” cos Qt),
where Va is the complex magnetic polarisability of the sphere, which has been determined
in §45, Problem 1. Along the z-axis, on the other hand, the magnetic field is constant, and
therefore causes no magnetic moment (if » = 1). The components of the magnetic moment
in the fixed system of co-ordinates are Mz = Va'Sz, My = Va"Gz, M2= 0. Thus in this
problem a’ and «” give the components of the magnetic moment of the sphere respectively
parallel and perpendicular to the plane of the vectors @ and 9.

‘The torque on the sphere is K = M X §. Its components relative to the fixed axes are
Kz = Ve"$:G2, Ky = —Va' $2 Ke = —Va''$2?.

Prosiem 2. Determine the e.m.f, due to unipolar induction between the pole and the
equator (*Fig. 27) of a uniformly magnetised sphere rotating uniformly about the direction*
of magnetisation.

SoLuTION. When the sphere rotates about its direction of magnetisation, it generates a
constant field, and, since no currents flow within the sphere, we find from (49.5) that
curl (vxB) = 0. Hence the integral of vxB along the closed contour OACBO (*Fig. 27)*

210 Quasi-static Electromagnetic Field §50
is zero, and so the integration along ACB in formula (49.8) may be replaced by one along
the path AOB, which lies inside the sphere. The integral along the segment AO of the axis
of rotation is zero, since & and r are parallel; the integral along the radius OB gives, since
B and & are parallel within the sphere,
e=- f BoQrdr = BoQa?/2c,

“9
where a is the radius of the sphere and Bo the magnetic induction in it. In a uniformly
magnetised sphere (in the absence of an external field) the induction is related to the mag- |
netisation by Bo+2H = 0 (cf. (8.1)) and Bo—H = 4xM, whence Bo = 87M/3. In terms
of the total magnetic moment of the sphere we have finally & = 0.4/ca.

Prosiem 3. Determine the total charge which flows along a closed linear circuit when the |
magnetic flux through the circuit changes for any reason from one constant value (1) to
another (®s).

So.urion. The required total charge is the integral

fra.
where J(t) is the induction current in the circuit. Mathematically, this integral is the Fourier
component of the function J(¢) that has the frequency w» = 0. It is therefore related to the
corresponding component of the e.m.f. by
fea = 200) f Fats
see (47.3). Putting Z(0) = R, where R is the resistance of the circuit to a constant current
and & = —(1/c) d®/dt, we have
r 1
free Sera,
cR
a

## Section §50: Excitation of currents by acceleration

In discussing the motion of a conductor in §49 we have neglected possible
effects of the acceleration, if any. The accelerated motion of a metal, however, is equivalent to the action of additional inertia forces on the conduction
electrons. If ¥ is the acceleration of the conductor and m the mass of the
electron, then the force on an electron is —mv. It affects the electron in the
same way as an electric field mv/e, where —e is the charge on the electron,
Thus the “effective” electric field on the conduction electrons in an accelerated metal is

E’ = E+mv/e. (50.1)
The current density is accordingly
j = cE’ = o(E+mv/e). (50.2)

§50 Excitation of currents by acceleration 211
Expressing E in terms of E’ from (50.1), we substitute in the equation curl E
= —(1/c)@H/€t (as usual, we put « = 1). Then
10H m
. eurlE’ = —-——+— curly. (50.3)
cat oe
We write v as asum vy = u+xr, where u is the translational velocity and
Q the angular velocity of rotation of the body. Differentiating with respect
to time, we find the acceleration to be ¥ =u+Q2xv+Qxr =u+Qxu+
+Q2x(Qxr)+Qxx. The first two terms are independent of r, and there| fore give zero on differentiation with respect to the co-ordinates. ‘The third
term can be written as @x(Qxr) = —} grad (Qxr)?, and its curl is therefore zero. Finally, curl (xr) = 29. Thus, substituting for ¥ in equation
(50.3), we have curlE’ = —(1/c)@H/t+2m&2/e or
1 0H’
ceurlE’ = —-—_, (50.4)
c at
where
H’ = H-2mcQ/e. (50.5)
Since Q is independent of the co-ordinates, the equation curl H = 4zj/c
is still valid if H is replaced by H’:
eurlH’ = 41oE’/c. (50.6)
Eliminating E’ from equations (50.4) and (50.6), we obtain for H’ the equation
AH’ = (410/c2)dH'/ét, (50.7)
which is the same as the equation for H in a conductor at rest.

Outside the body, the field satisfies the equation AH = 0 (the wavelength
being supposed large compared with the dimension of the body), and H’
satisfies the same equation.

Finally, on the surface of the conductor H’, like H, is continuous. The
only difference is in the condition at infinity, where H tends to zero but H’
tends to the limit —2mcQ/e.

Thus the problem of determining the variable magnetic field H near a
non-uniformly rotating body is equivalent to that of determining the field
H’ near a body at rest in a uniform external magnetic field

H = —2mcQ/e. (50.8)
The required field Hz outside the conductor is obtained by subtracting §
from the solution H’ of this latter problem.t

+ Misunderstanding may arise from the appearance of the angular velocity Q itself, and
not its time derivative, in formula (50.8). We may therefore emphasise that the above discussion, and therefore the significance here attached to the quantity (50.8), pertain only to
non-uniform rotation. In particular, the field (50.8) is unrelated to the gyromagnetic effect
(which appears even when the rotation is uniform, and is a small quantity here neglected),

212 Quasi-static Electromagnetic Field §50
The magnetic field thus produced, like any variable field, induces electric
currents in the conductor itself. In a simply-connected body, these currents
appear in the form of a magnetic moment. In a non-uniformly rotating
ring, the effect appears as an e.m.f.—the Stewart-Tolman effect.
PROBLEMS

ProsteM 1. Determine the magnetic moment of a non-uniformly rotating sphere of
radius a. The rate of rotation is assumed so small that the penetration depth 55> a.

: Souvrion. ‘The magnetic moment of the sphere in the field $(t) (50.8) is M = Vag,
where & is an operator whose action on the Fourier components of the function $(2) is given
by the formulae of §45, Problem 1. For the components with frequencies w such that |
85a we have M = Va(w)h ~ —4nmarciv®/15ce. This formula, when written
M = (Anma'o/15ce) dQ/dt, does not contain w explicitly, and is therefore valid also for
the functions and & themselves, as well as their individual Fourier components (on the
assumption that the Fourier expansion contains chiefly terms whose frequencies satisfy the
above condition).

Prostem 2. Determine the total charge which flows along a thin circular ring when it
ceases a uniform rotation about an axis perpendicular to its plane.

Souurton. In the formula obtained in §49, Problem 3, ® must be taken as the flux of
the field $ (50.8). The total charge transferred when the angular velocity changes from &
10 zero is

- 2me moV,
t = — ont? = ™ 9,
) ce eRe 2ne
where 6 is the radius of the ring and V its volume.

ProsieM 3. Determine the current in a superconducting circular ring which ceases to
rotate uniformly.

SoLvTion. From the condition that the total magnetic flux through the ring is constant
(see (42.5), we have

2me? me%Q
J = Orb? =
eL 2e[log (8b/a) —2]
See the third footnote to §42 concerning the value of L.



---


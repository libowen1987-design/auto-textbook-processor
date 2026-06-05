# Landau & Lifshitz《Electrodynamics of Continuous Media》第7章
> **中英双语版**

> 本笔记基于原文整理，100% 来源于原书内容。

## Chapter VII: Static Electric Field in Conductors

MAGNETIC FLUID DYNAMICS
- §51, The equations of motion for a fluid in a magnetic field
Ir a conducting fluid moves in a magnetic field, electric fields are induced in
it and electric currents flow. The magnetic field exerts forces on these currents
which may considerably modify the flow. Conversely, the currents themselves modify the magnetic field. ‘Thus we have a complex interaction
between the magnetic and the fluid-dynamic phenomena, and the flow must
be examined by combining the field equations with those of fluid dynamics.
| We shall use equations (49.6) as the field equations in a moving conducting medium. The magnetic permeability of the media considered in magnetic
fluid dynamics differs only slightly from unity, and the difference is unimportant as regards the phenomena under discussion. We shall therefore take
y =1 throughout the present chapter. The equations are then
div H = 0, (51.1)
@H/at = curl (v x H) + (c?/470) AH. (51.2)
By using these equations we assume that certain conditions are fulfilled.
The period of variation of the field must be large compared with the mean
free time of the conduction electrons. Then the relation between the current
and the electric field involves the same conductivity o as for a constant
current (see §45).t Here we assume that o is constant in the medium, and
therefore, in particular, that the conductivity is independent of the magnetic
field. For this to be so, the mean free path of the electrons must be small in
comparison with the radius of curvature of their orbits in the magnetic field.
That is, the mean free time must be small compared with the reciprocal of
the electron Larmor frequency eH/mc. This condition may not hold if the
medium is rarefied and the magnetic field is strong.
The equations of fluid dynamics are the equation of continuity
ap/at + div(pv) = 0, (51.3)
+ In the second footnote to §45 the further condition o/w >> 1 was mentioned as being
necessary for poor conductors. In good conductors this condition is always satisfied if the
other conditions are. In the present case the frequency is represented by V/L, where L and
V are characteristic parameters of length and velocity which determine the properties of
the flow. ‘Thus we assume the condition oL/V 5>1 to hold.

214 Magnetic Fluid Dynamics §51
where p is the fluid density, and the Navier-Stokes equation
ov 1 n 1 7 f
>=, + (v-grad)v = — - gradp + —Av + -(£ + }y) grad divv + -,
at p Pp Pp p
where 7 and ¢ are the two coefficients of viscosity for the fluid, and f is the
volume density of external (in this case, electromagnetic) forces. By formula
(34.4) we have f = jxH/c = (curl H)xH/4z. Thus the equation of motion
of the fluid is
ov 5 a
H+ (vegradyy |
1 1 ” 1 .
= —-gradp —-——H x curlH + - Av + —(£ + 4) graddivv. (51.4)
Pp 4up Pp P
To these equations we must add the equation of state
P= pp, T), (51.5)
which relates the pressure, density and temperature of the fluid, and the
equation of heat transfer. In ordinary fluid dynamics the latter ist
a a
ot(= + w-grads) = on + div(« grad T).
at OxK
Here s is the entropy per unit mass of the fluid, and the left-hand side of the
equation is the quantity of heat generated per unit time and volume in a
moving fluid particle. The right-hand side is the energy dissipated per unit
time and volume. The first term is due to viscosity; 0’ is the viscous stress
tensor:
ON Ov, =2 =) Ory
‘ie = 9(—— + — - 8x Sie.
ed ol . Ox, «3 id Oxy + Bu Oxy
The second term gives the dissipation due to thermal conduction, « being
the thermal conductivity. In a conducting fluid, a term giving the Joule heat
must be added. The rate of evolution of this heat per unit volume is j2/o
= (c2/167?o)(curl H)?. The equation of heat transfer in magnetic fluid
dynamics is therefore
(4 ds) tg + di Cas 1H). (51.6)
— + vegr = — + di ig = 5 c
Pp G vegrads vw iv (« gra ) + Tera, (eur eC
Equations (51.1)-(51.6) form a complete system of equations of magnetic
fluid dynamics, on the assumptions stated at the beginning of this section.
+ See Fluid Mechanics, §49, Pergamon Press, London, 1959.

§51 The equations of motion for a fluid in a magnetic field 215
Equations (51.4) and (51.6) can also be written in forms which express the
Jaws of conservation of momentum and energy respectively. The NavierStokes equation of ordinary fluid dynamics can be written (using the equation
of continuity) in the formt
a(pur)/at = — Ox/Oxes (51.7)
where II is the momentum flux density tensor: Ti = pUire+ pSiz—o' tk.
Equation (51.4) can be brought to the same form, but II now contains an
additional term. We have Hxcurl H = } grad H?—(H-grad)H. Thus
Tue = poe + pS — 0’ — (Hilly — $H°8ix)/40. (51.8)
The added term is the Maxwell stress tensor of the magnetic field, as it
should be.

The equation of heat transfer can be transformed (using the other equations of fluid dynamics) into an equation of conservation of energy. In
ordinary fluid dynamics we have 0(}pv?+ pe)/at = —div q, where q is the
energy flux density:

q = pv(gv? + w) — veo’ — xgrad T;
cand w =e+p/p are respectively the internal energy and heat function per
unit mass of fluid. When a magnetic field is present in the conducting
medium, the energy density includes also the magnetic energy H?/8m, and
the energy flux density includes also the Poynting vector cExH/4. Expressing E in the latter in terms of H we obtain
1
q = pv(30? + Carre! x (vxH) —
a :
= GpqgH x cwlH—vio'—agradT, (61.9)

and the equation of conservation of energy is

2 (soe Zs di 51.10

= (dpe! + pe-+ =) = ~ diva. (51.10)
It is not difficult to verify by direct calculation that equations (51.6) and
(51.10) are equivalent.

The equations are somewhat simplified if the moving fluid can be supposed incompressible. The equation of continuity (51.3) then reduces to
div v =0, while in equation (51.4) the last term is zero. For reference, we
shall write out here the complete system of equations for an incompressible
fluid (in equations (51.2) and (51.4) we have transformed the terms

+ See Fluid Mechanics, §15.

216 Magnetic Fluid Dynamics §51
curl(vxH) and HxcurlH respectively by the appropriate formulae of
vector analysis) :
divH =0, divv = 0, (51.11)
OH/ét + (v-grad)H = (H-grad)v + (c2/47c) AH, (51.12)
ov A
rs + (v-grad)v
1 Hy 1
= ~<grad (p+ =) +——(H-grad)H+vAv, (51.13)
p 87/ 4np
where v = 7/p is the kinematic viscosity. Equation (51.6) is not needed in |
solving the problem of incompressible flow unless we are interested in the
temperature distribution and its effect on the flow.
Let us return to the general equation (51.2). In the limiting case of very
high conductivity it becomes
OH/ét = curl(v x H), (51.14)
an equation which has a very important physical interpretation. We expand
the right-hand side, using the fact that div H = 0:
6H/ét = (H-grad) v — (v-grad)H — H divv.
Substituting from the equation of continuity (51.3)
. lap v-gradp
divv = —-— - ——_,
p ot p
we obtain after a simple rearrangement of terms
7] H fH
& + werad) —= (—-eraa) v.
at p p
The left-hand side is the “substantial” derivative, which gives the rate of
change of H/p for a given fluid particle as it moves about. Denoting this
derivative by d/dt, we have
d H
= ap) = (-eraa) o (51.15)
dt Pp
Let us now consider some “fluid line”, i.e. a line which moves with the fluid
particles composing it. Let 51 be an element of length of this line; we shall
determine how 41 varies with time. If v is the fluid velocity at one end of the
element 51, then the fluid velocity at the other end is v+(S1-grad)v. During
a time interval dt, the length of 51 therefore changes by dt(5I-grad)v, i.e.
d(8l)/dt = (81-grad)v. We see that the rates of change of the vectors 51
and H/p are given by identical formulae. Hence it follows that, if these
vectors are initially in the same direction, they will remain parallel, and their
lengths will remain in the same ratio. In other words, if two infinitely close

§1 The equations of motion for a fluid in a magnetic field 217
fluid particles are on the same line of force at any time, then they will always
be on that line of force, and the value of H/p will be proportional to the distance between the particles.

Passing now from particles at an infinitesimal distance apart to those at
any distance apart, we conclude that every line of force moves with the
fluid particles which lie on it. We can picture this by saying that (in the
limit o > co which we are considering) the lines of magnetic force are
“frozen” in the fluid and move with it. The quantity H/p varies at every

point proportionally to the extension of the corresponding “fluid line”. If
the fluid may be supposed incompressible p = constant, and the field H
_ varies as the extension of the lines of force.

These results can be viewed in another way: as any closed fluid contour
moves about in the course of time, it cuts no line of force, i.e. the “number”
of lines of force passing through the contour remains unchanged. This
means (cf. §49) that the flux of the magnetic field through any surface
spanning the fluid contour does not vary with time.

To the question of when in fact dissipative processes in the fluid may be
neglected there is no general answer, since the necessary conditions depend
_ greatly on the nature of the motion and are, for instance, completely different
for steady and for non-steady flows. We shall not investigate the general
problem here.
PROBLEM

Determine the velocity distribution in an incompressible viscous conducting fluid in
steady flow between two parallel solid planes, when a uniform external magnetic field Ho
is applied perpendicular to the planes (J. HARTMANN, 1937).

SoLuTION. It is natural to assume that the fluid velocity is everywhere in the same direction, which we take as that of the x-axis, and depends only on the co-ordinate 2 (whose
direction is perpendicular to the planes). ‘The same is true of the longitudinal field Hz
resulting from the motion. The pressure p, however, depends on x also, because there must
be a constant pressure gradient in the direction of motion in order to maintain a steady flow.
The equation div v = 0 is satisfied identically, while from divH = 0 it follows that
Hz = constant = Ho. The z-component of equation (51.13) gives

Hi?
ety P(x), ay
where P(x) is a function of x only. ‘The pressure gradient in the x-direction is
—2ap|ax = —dP/dx = constant.
‘The x-components of equations (51.12) and (51.13) give
du | 2 d’He
Hag tno dat @)
@v | Ho dHs _ 4@P
Tat} de ae ment a
‘The boundary conditions for viscous flow are v = 0 for z = +a, where 2a is the distance
between the solid planes, and the plane 2 = 0 lies half-way between them. The magnetic
field must satisfy the conditions Hz = 0 for z = +a, since the magnetic field outside the
fluid is just Ho, and the tangential magnetic field component is continuous at the boundary.

218 Magnetic Fluid Dynamics §52
‘The solution of equations (2) and (3) which satisfies these conditions is
y= vp ah (ald) —cosh (2/4)
= 9,
cosh (a/A)—1
_ an (z/a) sinh (a/A)—sinh (2/A)
Hz = —vw-v(on) Serer > 1)
where A = (c/Ho)V(n/0). The constant vo is the fluid velocity on the median plane z = 0.
Its relation to the pressure gradient is given by substituting (4) in (3). The fluid velocity
averaged over the cross-section is
1 dP aA A
a a
b= — | ode = ———(coth— ——}).
° al? ee (ems 3) |
“a
The effect of the magnetic field on the flow is characterised by the ratio |
[4 = (aHo|c)V(o/n).
For a/A <1 we have
_ ( 1 *) dP @
iid er) ae Po
in accordance with the results of ordinary fluid dynamics. If a/A>> 1, then
dP ac
= vol —e(a-tetyay oo
oho 8 ae Hoven
‘When the magnetic field increases, the velocity profile is flattened over the major part of the
cross-section, and the mean velocity is reduced (for a given pressure gradient).

## Section §52: Hydromagnetic waves

Let us consider the propagation of small disturbances in a homogeneous
conducting medium in a uniform constant magnetic field Ho. We shall assume
that the viscosity, thermal conductivity and electric resistance (1/c) of the
medium are so small that their effects, due to the dissipation of energy, on
the propagation of perturbations may be neglected in a first approximation. +
Then the perturbations will be propagated as undamped waves.t
Omitting all dissipative terms, we can rewrite the fundamental equations
(51.1)-(51.4) as
divH = 0, (52.1)
OH/ét = curl(v x H), (52.2)
ap/ét + div(pv) = 0, (52.3)
ov ad 1
& y (wegeadyy = — 82°? * (eurtny xo. (52.4)
ot 7 4ap
t It should be noted that, by putting 1/0 = 0, we extend the range of frequencies in
which the equations are applicable: the conditions that « should exhibit no dispersion and
should be independent of the magnetic field are now irrelevant.
+ The condition for this approximation to be valid is that the wave damping coefficient
(calculated in the Problem at the end of this section) should be small.

§52 Hydromagnetic waves 219
Equation (51.6) reduces to the equation of conservation of entropy (the
condition for adiabatic flow). If the unperturbed medium is homogeneous,
then this condition means that s = constant in the perturbed medium also,
i.e. the flow is isentropic.

We write

H=Ho+h, p=potp’, pP=pot?’ (52.5)
where the suffix 0 denotes the constant equilibrium value, and h, p’ and p’
are the small variations in the wave. The velocity v, which is zero in equilibrium, is a small quantity of the same order. Since the flow is isentropic,
the changes in pressure and density are related by p’ = (2p[ap)sp’. But
(]2p)s is the square of the velocity of sound, which we denote by uo:
p’ = up’. Neglecting terms of higher order than the first in equations
(52.1)-(52.4), we obtain the linear equations

divh = 0, dh/ét = curl(v x H),
ap'/at + p divv = 0, | (52.6)

av/at = — (uo?/p) grad p’ — (H x curl h)/47>p.
Here and in what follows we omit, for brevity, the suffix zero to the equilibrium values. For a perturbation periodic in time, the first of these equations
follows from the second and can be omitted.

We shall seek solutions of these equations which are proportional to
exp [i(k-r—w1)], ic. which describe the propagation of plane waves with
wave vector k and frequency w. The system of equations (52.6) then gives
the algebraic equations

—wh=kx (vx H), wp’ = pk+v,
— wv + (uo?/p)p'k = — Hx (kx h)/4zp.

The first of these shows that the vector h is perpendicular to the wave vector
k, which we shall take to be along the x-axis, with the plane of k and H as
the xy-plane. We also introduce the phase velocity of the wave, u = alk.
Eliminating p’ from the third equation by means of the second equation, and
rewriting the result in components, we have

uh; = —U2Hz, uv, = — Hzh,/4np, (52.7)
uhy = vgHy — vyHz, uvy = — Hzhy|4zp,

uo? 52.8)

oft") =a

‘We have here separated the equations into two groups, the first involving
only hz and v, and the second only hy, vz and vy. It therefore follows that
perturbations of the two groups of variables are propagated independently.
The density, and therefore the pressure, belong to the second group, since

p’ = pvz/u. (52.9)

220 Magnetic Fluid Dynamics §52

The compatibility condition for the two equations (52.7) is

u = uw = Hz/V/(4np). (52.10)

In these waves the component h; of the magnetic field which is perpendicular

to the directions of propagation and of the constant field H oscillates, and
with it the velocity vz, which is related to hz by

Ve = — hel/(4ap). (52.11)

The relation between w and k (the dispersion relation, as it is called) given

by (52.10) involves the direction of the wave vector:

w= Hek/y (np).
‘The physical velocity of propagation of the waves is called the group velocity
and is given by the derivative dw/@k. In the present case we have dw/dk
= H/+/(47p), which does not involve the direction of k. The direction of
propagation of the wave, in the sense of the direction of its group velocity, is
the direction of H.

Let us now consider waves described by equations (52.8). Equating to

zero the determinant of these equations, we obtain
H,? wH,?
18 — w9(2 =) a=
( 0") tp tp
The roots of this quartic equation for u aret
Joes Ma)
u23 = 3) | (uo® + — +———] +
2 Aap -V (mp)
He A,
+ 4 (ve a “yl. (52.12)
4up /(mp)
Thus we obtain two more types of wave. In these waves the quantities
hy, Vz and vy (and the density p’) oscillate. The vectors h and v are in the
plane of H and k.

In the limiting case where H? < 4rpuo? we have ug ~ uo, and it follows
from equations (52.8) that vy < vz. In other words, in the limit waves of this
type become ordinary sound waves propagated with velocity up. The weak
transverse field in the wave is related to vz by hy ~ vzHy/uo.

In the same limiting case, ug is the same as m1 to a first approximation, and
Uz Z 0, ty X —hy/+/(4np) as in a wave of the first type, but with the vectors
vand h parallel to the plane of k and H instead of perpendicular to it.

We see also that in an incompressible fluid (corresponding formally to the
limit up + 00) only one type of wave occurs, with two independent directions of polarisation. The dispersion relation for these waves is given by

+ The roots of the quartic equation x4+- px?+ g = 0 can be written

x= tHV(—pt2vq) +t V(—p— 2V4)}

§52 Hydromagnetic waves 221
formula (52.10); the vectors v and h are perpendicular to k and are related by

v= —h/V/(4zp). (52.13)
Such waves were first discussed by H. ALFvEN (1942).

There is a simple interpretation of the result that, in a longitudinal magnetic field, transverse displacements of the fluid are propagated in the form
of waves. We have seen at the end of §51 that the lines of magnetic force
behave like fluid lines when o -> 00. The transverse displacement of the
fluid particles results in a curvature of these lines, and therefore in their

| stretching and, at some points, in their compression. The forces in a magnetic field (expressed by the Maxwell stress tensor) are such as would
occur if the lines of magnetic force tended to contract and also to repel one
another.t Hence a curvature of the lines results in “quasi-elastic” forces
which tend to straighten them, leading to further oscillations.

It is interesting that, in an incompressible fluid, the plane hydromagnetic
wave given by formulae (52.10) and (52.13) is in fact an exact solution of the
equations, valid for any transverse field h (not necessarily small). (This state
| ment does not apply, however, to a superposition of several plane waves
propagated in different directions.) For, let us return to the exact equations
| (52.1)-(52.4). In an incompressible fluid, equation (52.3) becomes div v = 0.
If we seek a solution in which all quantities depend on only one co-ordinate
| x and the time 2, we find from this equation that vz = constant, and by taking
another system of co-ordinates moving uniformly in the x-direction we can
put v, =0. From the equation divH =0 it follows that H, = constant.
Denoting the transverse components of H by h, we obtain from equations
(52.2) and (52.4) (with v, = 0) dh/dt = H,Ov/ax, dv/dt = (Hz/47p)0h| dx,
i.e. the exact equations necessarily reduce to the linear equations for a plane
wave with the phase velocity (52.10), v and h being related by (52.13).
The x-component of equation (52.4) is
1 1 oh ig
pox 4np ax
whence
p + h2/8m = constant, (52.14)
which gives the manner of variation of pressure in the wave.

Let us return to formulae (52.8) and (52.12), and consider the opposite
limiting case, where H? > 47puo?. We then have, in the first approximation, ug = H]/-/(47p). Since this expression is independent of k, the group
velocity is of magnitude ug and its direction is that of k. In this wave the

+ They are sometimes called hydromagnetic waves. In the general case, where the magnetic
fields are not small, the waves cannot be divided into hydromagnetic waves and ordinary
oP mon let “a line of force be along the z-axis. Then the longitudinal stress IIzs (51.8)

Seay negative term — H2/8z, and the transverse stressesIIzz and [yy contain a positive

222 Magnetic Fluid Dynamics §5
vector v is perpendicular to H (*Fig. 28), and its magnitude is given in terms*
of h=hy by v =h/./(4zp). For ug we have in this limiting case
ug = uoH,/H. The group velocity is dw/@k = uoH/H. The vector v in this
case is antiparallel to H, and its magnitude is given by v = hH2/4mpuoHy.
When the relation between H? and pup? is arbitrary, both uz and ug depend
on the direction of the wave vector. When the angle between k and H
increases, ug increases monotonically and ug decreases monotonically. It is
easy to see that the inequalities
us < uy < te, uz 2 uo, ug < uo (52.15)
always hold. If k is parallel to H (Hy =0, Hz = H), ue and ug are respectively equal to the greater and the smaller of ug and u; = H//(4zp). If k
is perpendicular to H (Hz = 0, Hy = H), then
He
= z+-—}), 52.16
” df (w ¥ i) (52.16)
while u; and ug are zero, i.e. only one type of wave exists.
ie
k
H
v
y
Us
Fie. 28
In this last case it is possible to find exact solutions of the equations of
magnetic fluid dynamics for a plane wave, without assuming its amplitude
to be small (S. A. Karan and K. P. Stanyuxovicu, 1954). When Hz = 0,
Hy = H, equation (52.1) is satisfied identically, and equations (52.2)-(52.4)
give
OH/ét + Wv2H)/ax = 0, (52.17)
@p/dt + a(vap)/éx = 0, (52.18)
Ovz Ovz 1 0H? 1 &
= +s E -- 52.19)
a + "Ge t Sap os pox (2.19)
From the first two of these equations it is easily seen that the ratio H/p = 6
satisfies the equation 0b/@t-+v,0b/8x =0 or db/dt =0, where the total
derivative signifies the rate of change in a given fluid particle as it moves

§52 Hydromagnetic waves 223
about. Hence, if the fluid is homogencous at some initial instant, so that 6
is constant, then at all subsequent instants we havet
Hip = b = constant. (52.20)
Substituting in the third equation H = pb, we obtain
Ovg Ovz 1a Be
tor = +o"). 52.21
a” Ox ? xl? 8a" (62.21)
| Thus the magnetic field has been eliminated from the equations, and the
problem reduces to the solution of equations (52.18) and (52.21). These
equations differ from those for one-dimensional motion in ordinary fluid
dynamics only by a change in the equation of state of the gas: the true
pressure p = p(p) (for given entropy s) must be replaced by P*(p) = 0(p)+
+5%p2/8. ‘This fact enables us to apply the results of ordinary fluid dynamics to this case of magnetic fluid flow. In particular, the formulae giving
the exact solution for one-dimensional travelling waves (Riemann’s solution)t
| can be applied, the velocity of sound being represented by
| ‘ap* Be
wo UG), Lae)
| ap le tn
der)
= | (w+ 7},
4np,
in accordance with formula (52.16).
PROBLEM

Determine the absorption coefficient (assumed small) for a hydromagnetic wave in an
incompressible fluid.

SoLuTion. The absorption coefficient for a wave is defined as y = 0/24, where ( is
the (time) average energy dissipated per unit time and volume, and q is the mean energy
flux density in the wave. The amplitude of the wave decreases as e~”* during its propagation.
Q is given by the right-hand side of equation (51.6); in an incompressible fluid we have for
a wave propagated in the x-direction (and so vz = 0)

Q = 9 dv] dx)?+ (c2/160%0)( dh/ ax)?
In the energy flux density (51.9), we can omit the small dissipative terms, leaving
qz = —Hzh-v/4z. Using formulae (52.10) and (52.13), we have the result
wt in &
1 Bat ane)

+ In accordance with the general results (§51) concerning the relation between H/p and
“fluid”? lines of force, if we take into account the invariability of the length of these lines
with time in the present case.

§ See Fluid Mechanics, §94.

224 Magnetic Fluid Dynamics §53

## Section §53: Tangential and rotational discontinuities

The equations of motion for an “ideal” magnetic fluid (having zero viscosity, thermal conductivity and electric resistance) admit discontinuous
flows as in ordinary fluid dynamics. To elucidate the conditions which must
be satisfied on a surface of discontinuity, let us consider an element of the
surface and use a system of co-ordinates in which it is at rest.t

First of all, the mass flux must be continuous at a surface of discontinuity:
the mass of fluid entering from one side must be equal to the mass leaving
on the other side. Thus pivin = p2v2n, where the suffixes 1 and 2 refer to
the two sides of the discontinuity, and the suffix n denotes the component of
a vector normal to the surface. In what follows we shall denote the difference
between the values of any quantity on the two sides of the surface of discontinuity by enclosing it in square brackets. Thus [pvp] = 0.

Next, the energy flux must be continuous. Using the expression (51.9) and
omitting the dissipative terms, we obtain

[gn] = [pun($0® + w) + UnH?/4 — Hnv-H/47] = 0.
The momentum flux must also be continuous. This condition means that
{Tixx] =0, where [Iq is the momentum flux density tensor, and n is a unit
vector normal to the surface. Using (51.8), we therefore have
[p+ pon? + (2 — H2)/8n] = 0,
[penv: — HnHi/47] = 0,
where the suffix ¢ denotes the component tangential to the surface.

Finally, the normal component of the magnetic field and the tangential
component of the electric field must be continuous. If the conductivity of
the medium is infinite, the induced electric field is given by E = —vxH/c,
and the condition [E,] = 0 leads to [Hnv:—Hywn] = 0.

In what follows it is more convenient to use the specific volume of the
fluid (V = 1/p) in place of its density. The mass flux density through the
discontinuity is denoted by j = pon = Un/V.

Since j and Hp are continuous, we can write the remaining boundary conditions in the following form:

jlw + 3j2V? + 3v2 + VH2/47] = Ap[He-vi)/47, (53.1)

[p] + 7°(V] + HEY/8n = 0, (53.2)

Jv] = Ho[Hi]/47, (53.3)

A, [vi = j[VHd- (53.4)

This is the fundamental system of equations of discontinuities in magnetic
fluid dynamics.

+ This condition fixes only the velocity of the co-ordinate system in the direction norma
to the surface. Any constant vector may be added to its tangential velocity.

§53 Tangential and rotational discontinuities 225

In ordinary fluid dynamics, discontinuities of two entirely different kinds

are possible: shock waves and tangential discontinuities. + Mathematically,
the two types occur because some of the boundary conditions can be written
as the vanishing of a product of two factors, and the two different solutions
are obtained by equating the factors to zero in turn. This feature is not
present in magnetic fluid dynamics, and it might therefore be supposed
that only one type of discontinuity occurs. In reality, however, it is found

| that essentially different types of discontinuity again occur (F. DE HorFMANN
and E. TELLER, 1950). :

| Let us consider, first of all, discontinuities for which j = 0. This means
that vin = zn =0, ie. the fluid moves parallel to the surface of discon
tinuity. If Hp # 0, we see from equations (53.1)-(53.4) that the velocity,
pressure and magnetic field must be continuous. The density (and therefore
the entropy, temperature, etc.) may have any discontinuity. Such a surface
may be called a contact discontinuity, and is simply the boundary between
two media at rest which have different densities and temperatures.

If both j and Hp are zero, then three of the four equations (53.1)-(53.4)

| are satisfied identically, and therefore this is clearly a special case. We thus
find a type of discontinuity which may be called a tangential discontinuity, as
| in ordinary fluid dynamics. At such a discontinuity the velocity and the
| magnetic field are tangential and can have any discontinuity in both magnitude and direction:
| j=0 He=0, [40 [¥0. (53.5)
The density discontinuity also can take any value, but the pressure discontinuity is related to that of H; by equation (53.2):
| HP
(v1 #0, [» + =| =0. (53.6)
8a
The discontinuities of the other thermodynamic quantities (entropy, temperature, etc.) are related to those of V and p by the equation of state.

Another type of discontinuity is one in which the fluid density is continuous. Since the flux j = v/V is continuous, the normal velocity component is therefore continuous also:

#0, [V]=0, [mn] =0. (53.7)
On the right-hand side of equation (53.4) we can take V outside the brackets
and divide this equation by equation (53.3), obtaining
J = Anil V(GrV) (53.8)
and
Iv] = VV /47) TH). (53.9)
t See Fluid Mechanics, §81.

226 Magnetic Fluid Dynamics §53
In equation (53.1) we put w = «+pV; since V is continuous, this equation
can be rewritten as
2 V_\2
std +iv[p +55] +4i[(— / Cat) | =o,

Hy, being replaced in accordance with (53.8). The second term is zero by
(53.2) and the third term is zero by (53.9), so that we find [e] = 0, ie. the
internal energy also is continuous. Every other thermodynamic quantity is
determined if « and V are given. Hence all the other thermodynamic quantities, including the pressure, are continuous. It then follows from (53.2)
that H;? is continuous, i.e.

[P]=0, [HJ =0. (63.10)
The fact that H; and H;, are both continuous means that the magnitude of H
itself and its angle to the surface are likewise continuous.

Formulae (53.7)-(53.10) give all the properties of the discontinuities under
consideration. The thermodynamic quantities are continuous, but the magnetic field is turned through an angle about the normal, its magnitude
remaining unchanged. The vector H;, and therefore (by (53.9)) the tangential velocity component, are discontinuous, but the normal velocity
component v, =jV is continuous, and its value is

On = Huy(V/4n) = Hals/ np). (53.11)
We shall call these rotational discontinuities.

It is useful to note that, by a suitable choice of the co-ordinate system,
we can always ensure that the fluid velocity is parallel to the field on each
side of a rotational discontinuity. To achieve this, we use a co-ordinate system
moving with velocity viz—Hir/(V/47) = vat—Hor/(V 47). (Compare the
first footnote to this section.) In the new system the ratio of each component
of v to the corresponding component of H on either side of the discontinuity
is /(V/4n), ie.

vi = HivV(V/47), ve. = Hey/(V/4z). (53.12)
Thus in this system of co-ordinates the velocity is rotated with the magnetic
field, its magnitude and angle to the normal remaining unchanged.

The velocity vp is also minus the velocity of propagation of the discontinuity relative to the fluid. This is equal to the phase velocity 1 of one of
the three types of hydromagnetic wave (§52). The occurrence of this equality
for all rotational discontinuities is to some extent accidental, but when the
discontinuities of the various quantities are small the equality must hold.
For such a discontinuity is a weak perturbation, in which the velocity v
and the magnetic field H receive small increments perpendicular to the plane
through H and the normal n. This perturbation is of the type whose phase
velocity is u1. The physical velocity of propagation of the front of a small
perturbation is the normal component of the group velocity, i.e. its compo

§53 Tangential and rotational discontinuities 227
nent in the direction of the vector k. Since the relation between w and k
is linear, we have k- w/dk = w, and so this component is the same as the
phase velocity w/k =m.

Although tangential and rotational discontinuities form two different
types, there are also discontinuities having the properties of both. These
discontinuities are such that v and H are tangential in direction and continuous in magnitude.

In ordinary fluid dynamics, tangential discontinuities are always unstable
with respect to infinitesimal perturbations, and so are rapidly broadened into
turbulent regions. A magnetic field, however, has a stabilising effect on the
motion of a conducting fluid, and in this case tangential discontinuities may be |
stable. This result is a natural consequence of the fact that a perturbation
involving fluid displacements transverse to the field leads to a stretching of
the lines of magnetic force “frozen” in it, and therefore to the appearance of
forces which tend to restore the unperturbed flow. An investigation of such
discontinuities in an incompressible fluid by S. I. Syrovatsxri (1953) has
given the following two inequalities, which must both be satisfied if the

_ discontinuity is stable:
2 2 2
Hy? + He? > 2npv?, (53.13)
(Hh, x He)? > 2mp{(Hi x v)? + (He x v)?},
where v = v2—v1 is the discontinuity of the velocity; see Problem 1.t

In reality, however, the existence of a small but finite viscosity and electric
resistance in the fluid means that such tangential discontinuities cannot exist
indefinitely, even if the conditions (53.13) are fulfilled. Although no turbulence occurs, the sharp discontinuity is replaced by a gradually widening
transitional region, in which the velocity and the magnetic field change
smoothly from one value to another. This is easily seen from the equations
of motion (51.12) and (51.13) if the dissipative terms are retained. We take
the x-axis in the direction of the normal to the discontinuity. Assuming all
quantities to depend on x (and possibly on the time), we can write the transverse components of these equations as

= (2 2 2

OH,/dt = (c2/420) 07H;/2x?, 63.14)

Ov; Ot = vd%v,]/Ox?,
the fluid being supposed incompressible. If we assume steady flow, the
left-hand sides of equations (53.14) are zero, and the only solution which
remains finite as x > +00 is H; = constant, vy = constant, which contradicts the assumption that these quantities undergo a change at the discontinuity. Thus a tangential discontinuity cannot have a constant width such
as is found for (e.g.) a weak shock wave. Equations (53.14) are heat-conduction

+ If the densities of the incompressible fluids on the two sides of the discontinuity are
different, then p in these inequalities must be replaced by 2p1p2/(e1+ p2).

228 Magnetic Fluid Dynamics §53
equations. As we know from the theory of thermal conduction, a discontinuity in a quantity satisfying such an equation is gradually smoothed out
into a transitional region, whose width increases as the square root of the time.
Since the coefficients in the two equations (53.14) are different, the widths
Sy and 8y of the transitional regions for the velocity and the magnetic field
are also different:
d~ Vet), 8x = V(eH/o). (53.15)
Rotational discontinuities in an incompressible fluid are stable with respect
to infinitesimal perturbations, whatever the strength of the magnetic field
(S. I. Syrovarsxii, 1953). Like tangential discontinuities, however, they
cannot have constant widths, but are gradually smoothed out by the viscosity
and electric resistance of the fluid (see Problem 2).
PROBLEMS
Prosiem 1, Derive the condition for the stability of a tangential discontinuity in an
incompressible perfectly conducting non-viscous fluid in a magnetic field (S. I. SyRovATsK1i).
. So.ution.t We write v = vot+v’, p = po+p’, H = Ho+H’, where vo, po and Hp are
the constant (on each side of the discontinuity) unperturbed values, and v’, p’ and H’ are
small perturbations. Substituting in equations (51.11)-(51.13), we have for an ideal fluid
divu’=0, divv’ =0, qa)
du’/at = (u-grad)v’—(v-grad)u’ Q)
= +(v-gradyv’ = —1 grad p’—ux curl u’
P
1
= — 7, Brad (9'+ pau’)-+(u-grad)u’, (3)
where for brevity we have omitted the suffix 0 and put u = H/+/(4mp). We take the divergence of equation (3) and use (1), obtaining
A(p’+ pu-u’) = 0. 4)
Let « = 0 be the plane of the discontinuity, to which the vectors v and u are parallel.
In each of the half-spaces x > 0 and x < 0 we seek all quantities v’, u’, p’ in a form proportional to exp{i(k-r—wt)-+xx}, where k is a vector in the yz-plane. From equation (4)
we find that k?—x? = 0, so that we must put « = k for x < 0 and x = —k for x > 0.
We eliminate v’ from the x-components of equations (2) and (3), obtainingt
Pitan! = —u'g "(kev —(K-w)). 3)
keux
Let £ = &(y, 2, t) be the displacement of the surface of discontinuity in the x-direction
due to the perturbation. The conditions (53.5) and (53.6) must hold on the displaced
surface:
[p+ p(ut+u)?] = [p’+ pu-u’] = 0,
unitu'n & u’r1—ur-grad £ = 0, (6)
una-bu'na & u'sa—ua-grad { = 0;
+ Cf. Fluid Mechanics, §30.
} The case where the expression in braces vanishes is of no interest, since w is then real,
whereas instability can occur only for complex w.

§54 Shock waves 229
the condition of zero mass flux through the surface is satisfied automatically. Putting
{ = constant x expfi(k-r—wt)} and eliminating {, we1 and uza from the three equations (6),
we obtain an equation giving the possible values of w:
(w—k-v1)?+(w—k-va)? = (kk-un)?+(k-us)*.
‘This quadratic equation has no complex root if
2(ke-us)? + 2(ke-us)?— fe -(va—va)}? > 0,
or
{2ussure + 2uaiwax —(ve1—011)(v2e—014) }Rike > 0.

‘This quadratic form is positive-definite if the trace and determinant of the tensor of rank
two in the braces are both positive, and hence we obtain the conditions (53.13).

Prosiem 2. Find the manner of widening of a rotational discontinuity with time. |

SouuTION. Assuming all quantities to depend only on the co-ordinate x (and on the time),
we find from the equations div v = 0 and div H = 0 that vz = constant and Hz = constant.
Let the co-ordinate system be such that the values of v and H on each side of the discontinuity (outside the transitional layer) are related by (53.12). Then vz = uz, where u has
the same meaning as in Problem 1. For the transverse components u; and v; we have from
equations (51.12) and (51.13)

ave ct oy
Fe tt = wet 4 ES,
at ox ax" 4x0 ax? w
ove + ove ur + ave
a a ae
Since the difference v;—u; tends to zero for x > +00, because of the relations (53.12),
this difference must be small in the transitional layer in comparison with the sum v:+ur.
‘Adding the equations (1), we can therefore neglect a term in v;—us, obtaining
a tu) = 1 ( Gd = +
att w) = GT +) path te).
From this we see that the width of the discontinuity varies in a manner given by
a
s~ J (CG +}

## Section §54: Shock waves :

Let us now consider the type of discontinuity in which

j#9, [V] #0. (54.1)
Such discontinuities are called shock waves, as in ordinary fluid dynamics.
They are characterised by a discontinuity of density and by the fact that the
gas moves through them (vai and ung being non-zero). ‘The normal component of the magnetic field may or may not be zero.

On comparing equations (53.3) and (53.4) we see that, when Hn # 0, the
vectors Hyg—Hy and V2Hye— ViHyn are parallel to the same vector ver— vit,
and therefore to each other. Hence it follows that Hy and Hye are parallel,
ie. the vectors Hi, Hz and the normal to the surface are coplanar, unlike
what happens (in general) in tangential and rotational discontinuities. This
result holds also when Hp, = 0; in this case, which we shall discuss later, it
follows from (53.4) that ViHn = VeHie.

230 Magnetic Fluid Dynamics §54
The velocity discontinuity vzi—vie lies in the same plane as Hy and He.
We can evidently, without loss of generality, assume that the vectors vy and
Ve themselves lie in this plane, so that the motion in the shock wave is twodimensional. Furthermore, it is easy to see that, if H, # 0, a suitable transformation of the co-ordinates will always ensure that the vectors v and H
are parallel on each side of the discontinuity. To achieve this, we use a coordinate system which moves with velocity v;—(0nm/Hn)H: = vi—(jV/Hn)He
(the value of this expression is the same on each side of the discontinuity,
by (53.4)). In the following formulae, however, the choice of this particular
co-ordinate system is not implied. |
Let us derive the relation for shock waves in magnetic gas dynamics which
corresponds to the shock adiabatic (Hugoniot adiabatic) in ordinary gas__ |
dynamics. Eliminating [vi] from (53.3) and (53.4) we have
PVH] = Hn? [Hi]/405 (54.2)
here we have replaced H; by H;, since Hy; and Hy are parallel. In order to
eliminate [v;] from equation (53.1), we rewrite that equation as
F H, td
fol + atv) +a (me) | +
+ [VHP] 40 — Hy?[H?]/320°}? = 0.
The third term is zero by equation (53.3) and so v; does not appear. In the
last term we substitute j? from (54.2) and in the second term from (53.2),
ie.
B= {po — pi + (His? — Ha?)/8a}/(Vi — Ve). (54.3)
A simple calculation then gives
eg — «1+ 3(p2 + pil(V2 — Vi) +
+ (Va — Vi)(Hin — Hn)®/160 = 0. (54.4)
This is the equation of the shock adiabatic in magnetic gas dynamics. It
differs from the ordinary equation by the presence of the third term.
We may also write out again equation (53.3), which gives the discontinuity
of v¢ in terms of that of Hz:
v2 — ta = Hn(Hie — Hy)/47j. (54.5)
Equations (54.2)-(54.5) form a complete system of equations of shock waves.
As the discontinuities of all quantities tend to zero, the velocity of propagation of the shock wave must tend to its value for small perturbations. In
ordinary gas dynamics this means that the velocity of a weak shock wave
tends to the velocity of sound. In magnetic gas dynamics, however, there
are two different velocities ug and ug with which weak shock waves can be
propagated. t
+ The velocity u1 is, as mentioned in §53, the velocity of propagation of perturbations
corresponding to rotational discontinuities.

§54 Shock waves 231
Let us consider weak shock waves in more detail, and ascertain in which
direction the various quantities change in them. Expanding equation (54.4)
in powers of the discontinuities of pressure and entropy, we obtaint
1/@V 5
T(s2 — s1) al ope ) te pa)
1 av
- seal ap) —p\(Hia- Hay. (54.6)
‘When the gas passes through the shock wave, its entropy can only increase:
s2 > 1. By an inequality of thermodynamics, we have (8V/ép)s < 0, and
the derivative (02V/ép2)s is in fact positive for all the substances in question
here. Hence we see from (54.6) that the inequality sz > s: implies that
p2 > pr, and therefore Ve < Vi. Thus we have a compression wave, as in
ordinary gas dynamics. This result, which we have proved for weak shock
waves, seems to hold for shock waves of any intensity.
| For weak shock waves we can also derive certain results concerning the
direction of variation of the magnetic field. The changes in the various
| quantities when the state of the gas undergoes a slight perturbation are related
by formulae (52.8) and (52.9). The changes Sp = p2—pi and d(H?)
= Hy? —Hy2are such that 8(H,2) = 87(u®—up?)Sp. Since ug > uo and ug < uo
(see (52.15)), and from the above we necessarily have 5p > 0, we see that the
quantities H,2, and therefore H? = H2+H,?, vary in opposite directions in
the two kinds of weak shock wave. The magnetic field is increased in a
shock moving with velocity ~ us, but it is reduced in one moving with
velocity ~ us.

Let us now consider shock waves in weak magnetic fields, i.e. assume that
H? < pu® on either side of the discontinuity. No restriction is placed on the
discontinuity of any quantity; in particular, the discontinuity in the magnetic
field may be comparable with the magnitude of that field.

There are again two-possibilities. If the discontinuities of density and
pressure are not small, we can neglect, in a first approximation, the last term
in equation (54.4) and the magnetic field in formula (54.3). We thereby
return to the formulae of ordinary fluid dynamics. Thus the relation between
the discontinuities of the various thermodynamic quantities, and the rate of
propagation of the shock, will be the same as for ordinary shock waves. The
change in the magnetic field can be found from the relation (54.2). Since
the right-hand side of this equation is of the third order of smallness with
respect to the field, the same must be true of the left-hand side. As a first approximation we can put [VHj] = VaHie—ViHa = 0, whence Hie/Hn

= Vi[V2 = poipi. Since in an ordinary shock wave we always have Vi > Ve,
we see that the magnetic field is strengthened in a shock of this type.

t See Fluid Mechanics, §83.

232 Magnetic Fluid Dynamics §54

Equations (54.2)-(54.4) admit also another type of solution. The assump
tion that the field is small is also compatible with equation (54.2) for a wave

in which Vj ~ V2 and j? is the second-order quantity

P= Ap2l/AnV, (54.7)

where V is the common value of Vy and V2. It is seen from equation (54.3)
that if we put V; = Ve, we must to the same approximation put

po- pi = — (Ha? — Ha2)/8m. (54.8)

The continuity of the density means that a shock wave of this type can be
regarded as a discontinuity in an incompressible fluid. The vector H; (and
therefore v;) has a discontinuity in magnitude but not in direction, and the
discontinuity of pressure is given in terms of that of the magnetic field by
formula (54.8) when the density is continuous. The rate of propagation of
the discontinuity is ong = 0m =jV = Hay/(V/4n). This is a natural result,
and the necessity for the existence of such discontinuities could have been
foreseen. We saw in §52 that, in an incompressible fluid, there is only one
velocity of propagation of small perturbations of the magnetic field, namely
H/V(47p). Hence the fronts of small perturbations move with velocity
4; = Hn/-/(4zp), whether the change SH in the field is parallel or perpendicular to the plane of H and n. The latter case corresponds to weak rotational
discontinuities (already discussed in §53) and the former, when the discontinuities are small, is the type just considered.

To ascertain the direction of variation of the magnetic field strength in such
discontinuities, we return to equation (54.4), which has not yet been used,
and rewrite it in the form (54.6), in whose derivation the discontinuity in the
magnetic field was not assumed small compared with that field itself. Substituting p2~pi from (54.8), we find that the second term on the right of (54.6)
is of the fourth order in the field, whereas the first term is of the sixth order
and may be omitted. It follows at once from the condition s2 > s; that
Hz < Hn, i.e. that the magnetic field is weakened in such a discontinuity.

Returning now to shock waves of any intensity in magnetic fields of any
strength, we may consider two particular cases. Let the magnetic field in
medium 1 be perpendicular to the shock wave front, i.e. Hu = 0. Then equation (54.2) becomes j2V2Hie = Hn®Hi2/4r. Hence it follows that either
Hy = 0, or j? = Hn2/4V2 with no restriction on Hyg. In the former case
the magnetic field remains perpendioular to the surface of the discontinuity,
and does not affect the properties of the shock wave, since it does not appear
in the equations. In the second alternative we have a shock wave in which
the field changes direction, propagated with velocity ung =jV2 = Hy|V/(47p2)
relative to the gas behind it.

Another particular case is a shock wave parallel to the field on either
side of it (Hn =0).+ From (54.5) we then have v2 = vu, i.e. the tangential

+ For Hn = 0 there is only one type of shock wave, in accordance with the fact that us
is zero. The shock waves corresponding to us become weak tangential discontinuities at
rest relative to the fluid.

§54 Shock waves 233
velocity component is continuous. By a suitable choice of co-ordinates
therefore, we can always ensure that 7; = 0 on either side of the discontinuity,
i.e. the gas moves perpendicularly to the discontinuity, and we shall henceforth assume this. From equation (54.2) we have V2H2 = Viti. This relation shows that equations (54.3) and (54.4) can be written
5? = (bo —pi*)[(Vi- Va), 2* —a* + H(p2* + 1*)(V2— Vi) = 0,
which differ from the ordinary equations for shock waves in the absence of a
magnetic field only by a change in the equation of state: the true equation of state p =p(V,s) must be replaced by p* =p*(V, s), where
p* =p+2/8nV2, and b denotes the constant product HV. Accordingly «*
must be defined so as to satisfy the thermodynamic relation (de*/8V)s = —p*,
whence «* = €+52/8nV.

It has been shown in §53 that there are discontinuities which exhibit the
properties of both tangential and rotational discontinuities. The discontinuities discussed here are related in this way to shock waves also. The
transition between shock waves and rotational discontinuities is formed by
a discontinuity in which there is no change in density and the only change in
the magnetic field is that Hy is reversed. The transition between shock waves
and tangential discontinuities is formed by discontinuities in which v, = 0,
Hy = 0, and Hy has any discontinuity in magnitude but none in direction.

We may summarise as follows the discontinuities discussed in §§53-4:

| (1) Contact discontinuities:
| §=9 [vw] =0, [V] 40, [p]}=0, Hn #0, [He] = 0.
(2) Tangential discontinuities:
| . A?
| j=0, fw 40, (V4, [p+ =] -9 Hy = 0, (H #0.
(3) Rotational discontinuities:
j#0, [vw] #0, [V]=0, [p]=0, Hn #0,
H; changes direction but not magnitude.
(4) Shock waves:
j#0, [V] #0, Hh, He and n coplanar.
The following diagram shows the possible transitional cases:
3)
|

234 Magnetic Fluid Dynamics §55

## Section §55: The spontaneous magnetic field in turbulent motion of a conducting fluid

Turbulent motion of a conducting fluid has the remarkable property that
it may lead to spontaneous magnetic fields which are quite strong. There are
always small perturbations in a conducting fluid, resulting from causes
extraneous to the fluid motion itself, t and accompanied by very weak electric
and magnetic fields. The question is whether these perturbations are, on
the average, amplified or damped by the turbulent motion in the course of
time. The following arguments show that either may occur, depending on |
the properties of the fluid itself.t

The manner of variation with time of magnetic field perturbations, once
they have arisen, is determined by two physical agencies. The dissipation
of magnetic energy, which is converted into the Joule heat of the induced
currents, tends to diminish the field. The magnetic field tends to increase,
on the other hand, by the purely magnetic effect of the “stretching” of
the lines of force. We have shown at the end of §51 that, when a fluid of
sufficiently high conductivity is in motion, the lines of magnetic force move
as fluid lines, and the magnetic field varies proportionally to the stretching
at each point on each line of force. In turbulent motion any two neighbouring particles move apart, on the average, in the course of time. As a result,
the lines of force are stretched and the magnetic field is strengthened.

We shall show that in certain conditions these two opposite tendencies
may balance, and this will provide a criterion distinguishing the cases where
the magnetic field perturbations increase from those where they are damped.

While the magnetic field resulting from the motion remains weak its

! reciprocal effect on the motion can be neglected. That is, we may consider
ordinary fluid turbulence as providing a given “background” on which the
magnetic perturbations develop. We assume a steady turbulent velocity
distribution, the word “steady” being used in the sense usual in turbulence
theory, i.e. referring to the average values of the motion.||

Mathematically, we neglect the terms quadratic in the field in the equation
of motion (51.13), returning to the ordinary Navier-Stokes equation:

Ov/at + (v-grad)v = — grad (p/p) +vAv
(the fluid being supposed incompressible). If we use the formula (v-grad)v
= } grad v?—v x curl v and take the curl of the above equation, we obtain
0Q/dt = curl(v x Q) + vAQ, (55.1)
where we have put for brevity 2 = } curl v.

{ For example, the magnetomechanical effect in rotating parts of a fluid, or even thermal
fluctuations.

t The results in §55 are due to G. K. Barcumtor (1950).

i] The averaging is over times which are of the order of the periods of the corresponding
turbulent fluctuations, but are, of course, small compared with the total time during which
the system is observed.

§55 Spontaneous magnetic field in turbulent motion of conducting fluid 235
Let us compare this equation with (51.2):

@H/ét = curl(v x H) + (c?/47c) AH, (55.2)
which (for a given velocity distribution) determines the time variation of the
magnetic field. We see that 2 and H satisfy equations of the same form, which
become identical if v = c2/47ro. In this case, therefore, there is a solution of
equation (55.2) for which

H = constant x 2. (55.3)
Thus, if ,
v = 2/4no, (55.4)
a steady magnetic field (in the same sense of the word “‘steady”’) can exist.
This field, on the average, neither increases nor decreases, whatever the value
of the constant coefficient in (55.3). We may say that there is neutral equilibrium, in which the two factors, mentioned above as determining the magnetic
| field, are exactly balanced.
Hence, in turn, it is evident that, if the conductivity of the fluid exceeds
| 2/4mv, the dissipative loss of electromagnetic energy will be insufficient to
compensate the increase of the magnetic field by the stretching of the lines
| of force. Thus we obtain the inequality
| 4nvo[c2 > 1 (55.5)
as the condition for the spontaneous appearance of magnetic fields by the
growth of small magnetic perturbations. t
We can say that this is the condition for turbulent motion to be unstable
| with respect to infinitesimal magnetic perturbations. It is noteworthy that
the criterion can be established quantitatively, and not merely in orders of
magnitude.t
The condition (55.5) as a criterion of the behaviour of the field is valid
so long as the neglect of the reciprocal effect of the magnetic field on the flow,
on which the derivation of (55.5) is based, holds good. The field will increase
until some steady state, in which the reciprocal effect of the field cannot be
neglected, is set up. Although, strictly speaking, the fluid-mechanical
properties of the turbulence in this state are not those given a priori, the
qualitative distribution and the order of magnitude of the resulting magnetic
field can be determined as if they were.
+ The condition (55.5) is very stringent. For example, in mercury (o & 10! sec},
» = 1-210"? cm?sec), the quantity on the left of (55.5) is only 1-5 10-7. Since o and »
increase with the mean free paths of the corresponding carriers of charge and mass, the
condition (55.5) may be fulfilled, for example, in the Sun’s chromosphere and corona, and
in the ionised interstellar gas.
f It should be mentioned that the foregoing arguments, however convincing, are not
entirely conclusive. For example, Ya. B. ZEL'DOVICH has shown (Zhurnal éksperimental’not
i teoretichesko fiziki 31, 154, 1956; Soviet Physics JETP 4, 460, 1957) that they are invalid
in a hypothetical case of “two-dimensional” turbulence.

236 Magnetic Fluid Dynamics §55

It is easy to see that the magnetic field distribution must be similar to the
turbulent distribution of 2. For 2 may be regarded as the angular velocity
of the fluid at any given point. Since the lines of magnetic force move with
the fluid, the vector H rotates with the same angular velocity. Hence, if at
any two points of a turbulent flow the instantaneous values of 2 are uncorrelated, the vectors H at those points will rotate in an uncorrelated manner,
and their relative direction will vary randomly with time.

In this connection we may refer to some purely fluid-mechanical properties
of turbulence.t Turbulent flow may be regarded as a superposition of turbulent eddies of various sizes, from the largest J (the “external scale” of the |
turbulence) to the smallest Ao (the “‘internal scale”). The former is equal
to a characteristic length which gives the size of the region in which the
turbulent flow occurs. The quantity Ao gives, in order of magnitude, the
distances at which viscosity, and the energy dissipation which it entails,
become important; it can be expressed in terms of J and the Reynolds
number R ~ ul/v of the turbulent flow as a whole (u being of the order of
the change in the mean velocity over a distance /), or in terms of the energy
¢ dissipated in unit mass of the fluid in unit time:

do ~ (/e)t ~ IRE (55.6)

The correlation between the velocities v; and v2 at two points 1 and 2 at
a distance ) apart is determined mainly by the eddies of size A. According
to Kolmogorov and Obukhov’s law, we have, for distances A > Ag, AvjAvy
~ 2/3, where Av =ve—vi. At distances \ < Ao, on the other hand,
Av;Avy ~ 2. From this we can easily find the correlation of angular velocities. Since the components of 9) and Qp are expressed in terms of the
derivatives of v; and ve, we find, by differentiating AvjAv;z once with respect
to the co-ordinates of point 1 and once with respect to those of point 2,

~ A-4/8
OQex ~ X for A > Ao, (55.7)
Qy;Qe~ ~ constant for A < Ao.
These formulae show that an appreciable correlation between the angular
velocities exists only at distances up to those of the order of Ao, falling off
rapidly at greater distances.

From the above discussion, the distribution of the steady spontaneous
magnetic field must be similar. The distribution is correlated only over
regions of dimension ~ Ag. At greater distances the relative direction of the
vectors H is practically random.

The order of magnitude of the magnetic field can now be easily determined by estimating the terms in the complete equation of motion

Ov/at + (v-grad)v = — grad (p/p) + vAv — (1/47p)H x curl H.

t See Fluid Mechanics, §§31-33.

§55 Spontaneous magnetic field in turbulent motion of conducting fluid 237
Since the vector H changes its direction completely over distances ~ o,
the order of magnitude of the last term on the right-hand side is H?/47pAo.
Let us now estimate the term (v-grad)v. For eddies of size A it is of the
order of v)2/A, where v) is the change in the velocity over a distance 2.
According to the formulae of turbulence theory we have
~ #
v, ~ u(A/Dt for A > Ao, (53.8)
v, ~ u(A/l)/R for A < Ao.
Hence the ratio 0)2/A~ A-1/8 for A > Ap and ~ Afor A < Ao. Its greatest value
is therefore reached when A ~ do. Thus (v-grad)v ~ 0 92/Ao. Finally, if
the two terms are comparable in magnitude, we have
Fw 4npv,?2. (55.9)
According to (55.6) and (55.8), vj) ~ uR-¥4 ~ (ev)#/4, Hence we can also
write
H? ~ 4npu?/s/R ~ 4upv/(o). (55.10)

These formulae give the order of magnitude of the spontaneous magnetic
field. It is of interest to compare the energy of this field with the
kinetic energy of the turbulent flow. The latter energy resides mainly in the
largest eddies (of size ~ 1), and its order of magnitude is pu®. The magnetic energy resides mainly in the “magnetic eddies”, which are of small size
(~ do). By (55.9), it is comparable with the kinetic energy of the turbulent
eddies of this same size, but, by (55.10), it is small in comparison with the
total kinetic energy. A more exact mathematical formulation of these statements can be attained by expanding the spatial distribution of velocity and
magnetic field as Fourier integrals. The kinetic energy then resides mainly
in the components with small wave numbers (k ~ 1/l), while the magnetic
energy is mainly in those with large wave numbers (k ~ 1/Ao).

Turbulent flow results in a continuous transfer of energy from large eddies
to small ones, with almost no viscous dissipation. This “energy flux” is
dissipated only in the eddies of size Ao. In the absence of a magnetic field,
the dissipation is due entirely to the viscosity of the fluid, but in the turbulence here considered the energy in the eddies of size Xo is partly dissipated
by viscosity, partly converted into the energy of the magnetic field and only
then dissipated as Joule heat.

Let us estimate the time required to establish the steady state. For this
purpose we return to equation (55.2). The two terms on the right-hand
side are in order of magnitude respectively Hv /Ao = Hvy,ho/Ao® ~ Hv/Ao?
and c2H/4moo?. Since we know precisely the condition (55.4) for the occurrence of neutral equilibrium, we also know the exact relation between the
coefficients in these two terms, and can write

oH oe ) H
at ( 4a) oP”

. \
238 Magnetic Fluid Dynamics §55
Hence we see that small perturbations increase with time according to the
exponential function
a ) : } 55.11
oool(>- aah oy
If 4zov/c? > 1 we have simply exp(vt/Ao2). The time + during which an
initial small perturbation ~ Ho develops into the steady field H (55.10) is
then, in order of magnitude,
r®, HR jv\t_ ple)
rm logs ~ a) tog (35.12)
The random variation of the magnetic field with time in turbulent flow
means that the (time) average value of H is zero. In other words, we can
say that, in the case considered here (i.e. when a spontaneous field is possible),
a non-zero mean field is incompatible with turbulence. The result must be
that, when a moderate external magnetic field is applied to a fluid in turbulent motion (in a finite volume), the latter will behave like a superconductor.
A strong field (H? >= pu®) must necessarily penetrate into the fluid and will
suppress the turbulence.



---


## 中文翻译

> **中文：** 第VII章——电磁感应。

### 主要内容
法拉第电磁感应定律：变化的磁场产生电场。积分形式$\oint \mathbf{E}\cdot d\mathbf{l} = -\frac{1}{c}\frac{d}{dt}\int \mathbf{B}\cdot d\mathbf{S}$，微分形式$\nabla\times\mathbf{E} = -\frac{1}{c}\partial\mathbf{B}/\partial t$。

### 关键概念
- **自感$L$**：线圈中电流产生的磁链与电流之比，${\cal E} = -L\,dI/dt$
- **互感$M$**：两个线圈之间的磁耦合，${\cal E}_1 = -M\,dI_2/dt$
- **涡电流(Foucault currents)**：变化磁场在导体中感应的环流，引起能量耗散
- **趋肤效应**：高频下电流集中在导体表面
- **磁能存储**：$U = \frac{1}{2}LI^2$

### 应用
变压器、感应加热、无线电能量传输、磁场传感器。

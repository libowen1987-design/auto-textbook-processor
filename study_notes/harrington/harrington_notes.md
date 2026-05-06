# Time-Harmonic Electromagnetic Fields

**Author:** Roger F. Harrington  
**Publisher:** IEEE Press (Classic Reissue)  
**Subject:** Electromagnetic Field Theory

---

## Chapter 1: Fundamental Concepts

FUNDAMENTAL CONCEPTS &

## Section 1-1: Introduction
 The topic of this book is the theory and analysis
of electromagnetic phenomena that vary sinusoidally in time, henceforth
called a-c (alternating-current) phenomena. The fundamental concepts
which form the basis of our study are presented in this chapter. It is
assumed that the reader already has some acquaintance with electromagnetic field theory and with electric circuit theory. The vector analysis concepts that we shall need are summarized in Appendix A.

We shall view electromagnetic phenorfiena from the “macroscopic”
standpoint, that is, linear dimensions are large compared to atomic dimensions and charge magnitudes are large compared to atomic charges. This
allows us to neglect the granular structure of matter and charge. We
assume all matter to be stationary with respect to the observer. No
treatment of the mechanical forces associated with the electromagnetic
field is given.

The rationalized mksc system of units is used throughout. In this
system the unit of length is the meter, the unit of mass is the kilogram,
the unit of time is the second, and the unit of charge is the coulomb.
We consider these units to be fundamental units. The units of all other
quantities depend upon this choice of fundamental units, and are called
secondary units. The mksc system of units is particularly convenient
because the electrical units are identical to those used in practice.

The concepts necessary for our study are but a few of the many electromagnetic field concepts. We shall’start with the familiar Maxwell equations and specialize them to our needs. New notation and nomenclature,
more convenient for our purposes, will be introduced. For the most part,
these innovations are extensions of a-c circuit concepts.

## Section 1-2: Basic Equations
 The usual electromagnetic field equations are
expressed in terms of six quantities. These are

&, called the electric intensity (volts per meter)

%, called the magnetic intensity (amperes per meter)

D, called the electric flux density (coulombs per square meter)

®, called the magnetic flux density (webers per square meter)

J, called the elettric current density (amperes per square meter)

qv, called the electric charge density (coulombs per cubic meter)

2 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ds
ds
Ts
c s
*Fig. 1-1. di and ds on an open surface. Fig. 1-2. ds on a closed surface.*
We shall call a quantity well-behaved wherever it is a continuous function
and has continuous derivatives. Wherever the above quantities are wellbehaved, they obey the Maxwell equations
vxe--% v-@=0
ot
aD (1-1)
Vxe=>+9 V'D=q
These equations include the information contained in the equation of
continuity
= - 2% Vij= OE (1-2)
which expresses the conservation of charge. Note that we have used
boldface script letters for the various vector quantities, since we wish to
reserve the usual boldface roman letters for complex quantities, introduced in Sec. 1-7.
Corresponding to each of Eqs. (1-1) are the integral forms of Maxwell’s
equations
fea--$ [fads fh @-as =0
at
d (1-3)
sed = f, [[ 248+ [[ a2 ff: ds = [[[ ma
These are actually more general than Eqs. (1-1) because it is no longer
required that the various quantities be well-behaved. In the equations
of the first column, we employ the usual convention that dl encircles ds
according to the right-hand rule of *Fig. 1-1. In the equations of the*
last column, we use the convention that ds points outward from a closed
surface, as shown in *Fig. 1-2. The circle on a line integral denotes a*
closed contour; the circle on a surface integral denotes a closed surface.
The integral form of Eq. (1-2) is
d
2 == 1-4
fs ds fff wa (1-4)

FUNDAMENTAL CONCEPTS 3
where the same convention applies. This is the statement of conservation of charge as it applies to a region.

We shall use the name field quantity to describe the quantities discussed above. Associated with each field quantity there is a circutt
quantity, or integral quantity. These circuit quantities are

v, called the voltage (volts)
i, called the electric current (amperes)
q, called the electric charge (coulombs)
y, called the magnetic flux (webers)
y*, called the electric flux (coulombs)
u, called the magnetomotive force (amperes)
The explicit relationships of the field quantities to the circuit quantities
can be summarized as follows:
v= fea v= ff a-as
i=|f a-ds ve & [f o-as (1-5)
a=[[fade u= [aa
All the circuit quantities are algebraic quantities and require reference
conditions when designating them. Our convention for a “‘line-integral”
quantity, such as voltage, is positive reference at the start of the path of
integration. This is illustrated by *Fig. 1-3. Our convention for a*
“surface-integral”’ quantity, such as current, is positive reference in the
direction of ds. This is shown in *Fig. 1-4. Charge is a “‘net-amount”’*
quantity, being the amount of positive charge minus the amount of negative charge. .

We shall call Eqs. (1-1) to (1-4) field equations, since all quantities
appearing in them are field quantities. Corresponding equations written
in terms of circuit quantities we shall describe as circuit equations. Equa
+°@
\
i
v A >
{ dl { \ > ds
‘ou
i} % ON)
\ \
& _*Fig. 1-3. Reference convention for Fig. 1-4. Reference convention for*
voltage. current.

4 TIME-HARMONIC ELECTROMAGNETIC FIELDS
tions (1-3) are commonly written in mixed field and circuit form as
fea=--% dpa-as=0
dt
din (1-6)
fed = +i fh@-as = 4
Similarly, the equation of continuity in mixed field and circuit form is
-_¥
fp j-ds=- (1-7)
Finally, the various equations can be written entirely in terms of circuit
quantities. For this, we shall use the notation that = denotes summation
over a closed contour for a line-integral quantity, and summation over a
closed surface for a surface-integral quantity. In this notation, the circuit forms of Eqs. (1-6) are
di
ot - (1-8)
yen Gt yers
and the circuit form of Eq. (1-7) is
; dq
» t= a (1-9)
Note that the first of Eqs. (1-8) is a generalized form of Kirchhoff’s voltage law, and Eq. (1-9) is a generalized form of Kirchhoff’s current law.
It is apparent from the preceding summary that many mathematical
forms can be used to present a single physical concept. An understanding of the concepts is an invaluable aid to remembering the equations.
While an extensive exposition of these concepts properly belongs in an
introductory textbook, let us here summarize them. Consider the sets
of Eqs. (1-1), (1-3), (1-6), and (1-8). The first equation in each set is
essentially Faraday’s law of induction. It states that a changing magnetic flux induces a voltage in a path surrounding it. The second equation in each set is essentially Amp're’s circuital law, extended to the
time-varying case. It is a partial definition of magnetic intensity and
magnetomotive force. The third equation of each set states that magnetic flux has no “‘flux source,” that is, lines of @ can have no beginning
or end. The fourth equation in each set is Gauss’ law and states that
lines of D begin and end on electric charge. It is essentially a partial
definition of electric flux. Finally, Eqs. (1-2), (1-4), (1-7), and (1-9) are
all forms of the law of conservation of charge. They state that charge

FUNDAMENTAL CONCEPTS 5
can be neither created nor destroyed, merely transported. Lines of current must begin and end at points of increasing or decreasing charge
density.

## Section 1-3: Constitutive Relationships
 In addition to the equations of
Sec. 1-2 we need equations specifying the characteristics of the medium
in which the field exists. We shall consider the domain of we H# as
the electromagnetic field and express D, ®, and g in terms of 8 and &.
Equations of the general form

D = D(8,K)
B = B(E,5C) (1-10)
I = I(E,5)
are called constitutive relationships. Explicit forms for these can be found
by experimentation or deduced from atomic considerations.

The term free space will be used to denote vacuum or any other medium
having essentially the same characteristics as vacuum (such as air). The
constitutive relationships assume the particularly simple forms

D =
B = pos in free space (1-11)
j=0
where eo is the capacitivity or permittivity of vacuum, and po is the tnductivity or permeability of vacuum. It is a mathematical consequence of
the field equations that (eo#0)-% is the velocity of propagation of an
electromagnetic disturbance in free space. Light is electromagnetic in
nature, and this velocity is called the velocity of lightc. Measurements
have established that
c= a = 2.99790 X 108 ~ 3 X 108 meters per second (1-12)
V cout
The choice of either eo or zo determines a system of electromagnetic units
according to our equations. By international agreement, the value of po
has been chosen as
Ho = 44 X 10-7 henry per meter (1-13)
for the mksc system of units. It then follows from Eq. (1-12) that
€9 = 8.854 X 10-2? = ate x 10-9 farad per meter (1-14)
for the mksc system of units.

Under certain conditions, the constitutive relationships become simple

proportionalities for many materials, We say that such matter is linear

6 TIME-HARMONIC ELECTROMAGNETIC FIELDS
in the simple sense, and call it simple matter for short. Thus
D=c'
B= | in simple matter (1-15;
j=
where, as in the free-space case, c is called the capacitivity of the medium
and yp is called the inductivity of the medium. The parameter g is called
the conductivity of the medium. We originally made the qualifying statement that Eqs. (1-15) hold “under certain conditions.” They may not
hold if & or 5C are very large, or if time derivatives of & or 3Care very large.

Matter is often classified according to its values of c, e, and 4. Materials having large values of o are called conductors and those having small
values of o are called insulators or dielectrics. For analyses, it is often
convenient to approximate good conductors by perfect conductors, characterized by o = ~, and to approximate good dielectrics by perfect dielectrics, characterized by c = 0. The capacitivity e of any material is never
less than that of vacuum e), The ratio c, = €/eo is called the dielectric
constant or relative capacitivity. The dielectric constant of a good conductor is hard to measure but appears to be unity. For most linear
matter, the inductivity » is approximately that of free space uo. There
is a class of materials, called diamagnetic, for which u is slightly less than
no (of .the order of 0.01 per cent). There is a class of materials, called
paramagnetic, for which p is slightly greater than po (again of the order of
0.01 percent). A third class of materials, called ferromagnetic, has values
of » much larger than yo, but these materials are often nonlinear. For
our purposes, we shall call all materials except the ferromagnetic ones
nonmagnetic and take » = wofor them. The ratio», = u/po is called the
relative inductivity or relative permeability and is, of course, essentially
unity for nonmagnetic matter.

Quite often the restriction on the time rate of change of the field,
made on the validity of Eqs. (1-15), can be overcome by extending the
definition of linearity. We say that matter is linear in the general sense,
and call it linear matter, when the constitutive relationships are the
following linear differential equations:

2:
p= btaetact -aB= p+ me + oe +c: in linear matter (1-16)
2
I=8 tne toast =:
Even more complicated formulas for the constitutive relationships may

FUNDAMENTAL CONCEPTS 7
be necessary in some cases, but Eqs. (1-16) are the most general that we
shall consider. Note that Eqs. (1-16) reduce to Eqs. (1-15) whenthetime
derivatives of & and 3C become sufficiently small.

The physical significance of the extended definition of linearity is as
foilows. The atomic particles of matter have mass as well as charge,
so when the field changes rapidly the particles cannot “follow athe field.
For example, suppose an electron has been accelerated by the a, and
then the direction of & changes. There will be a time lag before the
electron can change direction, because of its momentum. Such a picture
holds for g if the electron is a free electron. It holds for D if the electron
is a bound electron. A similar picture holds for ® except that the magnetic moment of the electron is the contributing quantity. We'shall not
attempt to give significance to each term of Eqs. (1-16). It will be shown
in Sec. 1-9 that all terms of Eqs. (1-16) contribute to an ‘‘admittivity”
and an “impedivity”’ of a material in the time-harmonic case.

## Section 1-4: The Generalized Current Concept
 It was Maxwell who first
noted that Amp're’s law for statics, Vx # = J, was incomplete for
time-varying fields. He amended the law to include an electric displacement current @D/dt in addition to the conduction current. He visualized
this displacement current in free space as a motion of bound charge in
an “ether,” an ideal weightless fluid permeating all space. We have
since discarded the concept of an ether, for it has proved undetectable
and even somewhat illogical in view of the theory of relativity. In
dielectrics, part of the term @D/dt is a motion of the bound particles
and is thus a current in the true sense of the word. However, it is convenient to consider the entire @D/dt term as a current. In view of the
symmetry of Maxwell’s equations, it also is convenient to consider the
term 9@/dt as a magnetic displacement current. Finally, to represent
sources, we amend the { field equations to include impressed currents, electric and magnetic. These are the currents we view as the cause of the
field. We shall see in the next section that the impressed currents repre~
sent energy sources.

The symbols g and om will be used to denote electric and magnetic
currents in general, with superscripts indicating the type of current. As
discussed above, we define total currents

J = ° + x + J
on (1-27)
mM = 3 + .
where the superscripts t, c, and z denote total, conduction, and impressed
currents. The symbols i and k will be used to denote net electric and
magnetic currents, 4nd the same superscripts will indicate the type.

8 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Thus, the circuit form corresponding to Eqs. (1-17) is
eae M ere
aw (1-18)
ta OY i
k dl +h
The and k are, of course, related to the g and M by
i= ff a-as k= [[ m-ds (1-19)
where these apply to any of the various types of current.

In terms of the generalized current concept, the basic equations of

electromagnetism become, in the differential form,
vVx'=---om' VxK= 3 (1-20)
and in the integral form,
fed =- f/ ont - ds se dh = [| gi-ds (1-21)
Also, the mixed field-circuit form is
ped=-K gxe-d=# (1-22)
and the circuit form is
Dv = -kt Zu =i (1-23)
Note that these look simpler than the equations of Sec. 1-2. Actually,
we have merely included many concepts in the functions mt‘ and g'; so
some of the information contained in the original Maxwell equations has
become hidden. However, our study comprises only a small portion of
the general theory of electromagnetism, and the forms of Eqs. (1-20) to
(1-23) are well suited to our purposes.

Note that we have omitted the “divergence equations” of Maxwell
from our above sets of equations. We have done so to emphasize that
this information is included in the above sets. For example, taking the
divergence of each of Eqs. (1-20), we obtain

vVem=0 vV-g=0 (1-24)
for V-V X @ = 0 is an identity. Similarly, Eqs. (1-21) applied to
closed surfaces became

fpo-ds=0 dpgi-ds=0 (1-25)
Thus, the total currents are solenoidal. Lines of total current _haye no
beginning or end but must be continuous.
a e

FUNDAMENTAL CONCEPTS 9

As an illustration of the general- g
ized- Current concept, consider the a
circuits of Figs. 1-5 and 1-6. In
*Fig. 1-5, the “current source” g'*
produces a conduction current gc
through the resistor and a displace- Source fs 4 #
ment current gj? = dD/dt through 4
the capacitor. In *Fig. 1-6, the*
“voltage source” SR? produces an .
electrie current in the wire which in Fis. 1-5. Types of electric current.
turn causes the magnetic displacement current Ic = d@/dt in the magnetic core. In these pictures we
have used the convention that a single-headed arrow represents an electric current, a double-headed arrow represents a magnetic current.

# large }
i
>
di tTP
Source GD Hitt sal
Crp
Fie. 1-6. Types of magnetic current.

It is not possible at this time to give the reader a complete picture of
the usefulness of impressed currents. Figures 1-5 and 1-6 anticipate one
application, namely, that of representing sources. More generally, the
impressed currents are those currents we view as sources. In a sense,
the impressed currents are those currents in terms of which the field is

expressed. In one problem, a conduction
dg current might be considered as the source,
or impressed, current. In another problem, a polarization or magnetization current
might be considered as the source current.
Our understanding of the concept will grow

as we learn to use it.

## Section 1-5: Energy and Power
 Consider a re
s gion of electromagnetic field, as suggested
Fro. 1-7. A region containing by *Fig. 1-7. The field obeys the Maxwell*
sources. ‘ equations, which in generalized current

10 TIME-HARMONIC ELECTROMAGNETIC FIELDS
notation are Eqs. (1-20). As an extension of circuit concepts, it can
be shown that a product &- Lis a power density. This suggests a scalar
a par . .
multiplication of the second of Eqs. (1-20) by &. Also, in view of the
vector identity
V-(8X H)=HR-VxXE--&.v x 4
a scalar multiplication of the first of Eqs. (1-20) by 3c is suggested. The
difference of the resulting two equations is
V(X KH) +8-9+ 3-9 =0 (1-26)
If this equation is integrated throughout a region, and the divergence
theorem applied to the first term, there results
Pie x se-ds + fff 94 50-90) dr = 0 (1-27)
We shall interpret these as equations for the conservation of energy, Eq.
(1-26) being the differential form and Eq. (1-27) being the integral form,
The generally accepted interpretation of Eqs. (1-26) and (1-27) is as
follows. The Poynting vector
S=ExK (1-28)
is postulated to be a density-of-power flux. The point relationship
Pr =V*S=V-(8X 3) (1-29)
is then a volume density of power leaving the point, and the integral
r= fis-ds = fhe x ads (1-30)
is the total power leaving the region bounded by the surface of integration. The other terms of Eq. (1-26) can then be interpreted as the
rate of increase in energy density at a point. Similarly, the other terms
of Eq. (1-27) can be interpreted as the rate of increase in energy within
the region. Further identification of this energy can be made in particular cases.
For media linear in the simple sense, as defined by Eqs. (1-15), the
last two terms of Eq. (1-26) become
a/1 :
BH = TF) +osrte.gi
at \2
a/l (1-31)
. c- ~~ fs 2 . i
e+ om ae (ase) +e om
where J‘ and om‘ represent possible source currents. The terms
We = Wes? Wm = Wyse? (1-32)

FUNDAMENTAL CONCEPTS 11
are identified as the electric and magnetic energy densities of static fields,
and this interpretation is retained for dynamic fields. The term

pa = 08? (1-33)
is identified as the density of power converted to heat energy, called
dissipated power. Finally, the density of power supplied by Re source
currents is defined as

pe = -(8+ g' + > T) (1-34)
The reference direction for source power is opposite to that for dissipated
power, as evidenced by the minus sign of Eq. (1-34). In terms of the
above-defined quantities, we can rewrite Eq. (1-26) as

te)
Ps = Pp + pa + a (we + Wm) (1-35)
A word statement of this equation is: At any point, the density of power
supplied by the sources must equal that Iaving the point plus that dissipated plus the rate of increase in stored electric and magnetic energy
densities.

A more common statement of the conservation of energy is that which
refers to an entire region. Corresponding to the densities of Eqs. (1-32),
we define the net electric and magnetic energies within a region as

wea ss [[ferdr Wa= 5 fff userar (1-36)
Corresponding to Eq. (1-33), we define the net power converted to heat
energy as

G1 = [ff o8tar (1-37)

Finally, corresponding to Eq. (1-34), we define the net power supplied
by sources within the region as

= - [ff (+9 + 5+ me) dr (1-38)
In terms of these definitions, Eq. (1-27) can be written as

P= 0, + OF 5 (We + Wn) (1-89)
Thus, the power supplied by the sources within a region must equal that
leaving the region plus that dissipated within the-region plus the rate of
increase in electric and magnetic energies stored within the region.

If we proceed to the general definition of linearity, Eqs. (1-16), the
separation of power'into a reversible energy change (storage) and an

12 TIME-HARMONIC ELECTROMAGNETIC FIELDS

irreversible energy change (dissipation) is no longer easy. Contributions
to energy storage and to energy dissipation may originate from both
conduction and displacement currents. However, Eqs. (1-35) and (1-39)
still apply to media linear in the general sense. We merely cannot
identify the various terms. In Sec. 1-10 we shall see that for a-c fields
the division of energy into stored and dissipated components again
assumes a simple form.

## Section 1-6: Circuit Concepts
 The usual equations of circuit theory are
specializations of the field equations. Our knowledge of circuit concepts
can therefore be of help to us in understanding field concepts. In this
section we shall quickly review this relationship of circuits to fields.

Kirchhoff’s current law for circuits is an application of the equation of
conservation of charge to surfaces enclosing wire junctions. To demonstrate, consider the parallel RLC circuit of *Fig. 1-8. Let the letter 0*
denote the junction, and the letters a, b, c, d denote the upper terminals
of the elements. We apply Eq. (1-7) to a surface enclosing the junction,
as represented by the dotted line in *Fig. 1-8. The result is*

~ =

. : . : » , dg _

toa + top + toe + toa +t + gy = 0
where the ion are the currents in the wires, 7; is the leakage current crossing the surface outside of the wires, and g is the charge on the junction.
The term dg/di can be thought of as the current through the stray capacitance between the top and bottom junctions. In most circuit applications both 7; and dg/dt are negligible, and the above equation reduces to

Toa + tos + toe + toa = 0

This is the usual expression of the Kirchhoff current law for the circuit of
*Fig. 1-8.

Kirchhoff’s voltage law for circuits is an application of the first Maxwell equation to closed contours following the connecting wires of the*
circuit and closing across the terminals of the elements. To demonstrate,
consider the series RLC circuit of *Fig. 1-9. Let the letters a to h denote*

a Sa ie a Q a) aes
eS ‘
Gu) Fro. 1-8. A parallel RLC
c circuit.

FUNDAMENTAL CONCEPTS 13
R
b)0UOCSe
o d
. | !
Fro. 1-9. A series RLC 1 & L
circuit. | !
1 |
h e
Bom eG,
Cc
the terminals of the elements as shown. We apply the first of Eqs. (1-6)
to the contour abcdefgha, following the dotted lines between terminals.
This gives
dy
Yar + V6 + Vea + Yse + vec + 40 + Yon + Ure + Gp = 0
where the vm, are the voltage drops along the contour and y is the magnetic flux enclosed. The voltages vss, va, Ves, and v,, are due to the resistance of the wire. The term dy/dt is the voltage of the stray inductance
of the loop. When the wire resistance and the stray inductance can be
neglected, the above equation reduces to
Ue + Vde + Vjg + Ura = 0
This is the usual form of Kirchhoff’s voltage law for the circuit of *Fig. 1-9.
In addition to Kirchhoff’s laws, circuit theory uses a number of*
“element laws.’’? Ohm’s law for resistors, »v = Ri, is a specialization of
the constitutive relationship g = c&. The law for capacitors, g = Cv,
expresses the same concept as D = «&. We have from the equation
of continuity 7 = dg/dt, so the capacitor law can also be written as
i = Cdv/dt. The law for inductors, y = It, expresses the same concept as ® = 3. From the first Maxwell equation we have v = dy/dt,
so the inductor law can also be written asv = Ldi/dt. Finally, the various energy relationships for circuit theory can be considered as specializations of those for field theory. Detailed expositions of the various
specializations mentioned above can be found in ‘elementary textbooks.
Table 1-1 summarizes the various correspondences between field concepts
and circuit concepts.

## Section 1-7: Complex Quagtities
 When the fields are a-c, that is, when the
time variation is harmonic, the mathematical analysis can be simplified

14 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TaBLE 1-1. CoRRESPONDENCES BETWEEN Circuit Concepts AnD FieLp Concepts
Circuit concepts Field concepts
Voltage v Electric intensity &
Current i Electric current density J
or magnetic intensity 3
Magnetic flux y Magnetic flux density @
Charge q Charge density qo
or electric flux density D
Kirchhoff’s voltage law (generalized) | Maxwell-Faraday equation
dy IB
m= -- vxs=-> dt x ot
Kirchhoff’s current law (generalized) | Equation of continuity
dq 89e
A= -- vega
» , a 5 a
Element laws (linear) Constitutive relationships (linear in the simple
. | sense)
Resistors i = R” Conductors g° = o&
Capacitors g = Cv Dielectrics D = &
dv 0&
or i= CF or fi =er
Inductors y = Li Magnetic properties ® = p3C
L di ome aH
or v=L- or =p
dt a at
Power flow py = vi Power fowS =&X XH
Power dissipation in resistors Power dissipation
al a= 89 = 08?
Ca=u= R v? p
Energy in capacitors Electric energy
We = }aqu = 34Cv? we = D+ & = }4e8?
ee
Energy in inductors Magnetic energy
Wm = boyi = deli? wm = BK = }eni?

FUNDAMENTAL CONCEPTS 15
by using complex quantities. The basis for this is Euler’s identity
e* = cosa+ jsina
where 7 = V-1. This gives us a relationship between real sinusoidal
functions and the complex exponential function.
Any a-c quantity can be represented by a complex quantity. Ajgalar
quantity is interpreted according to! J
v = V2 |V|cos (wt + a) = V2 Re (Ve*) (1-40)
where v is called the instantaneous quantity and V = |V|e’* is called the
complex quantity. The notation Re (_ ) stands for “the real part of,”
that is, the part not associated with 7. Other names for V are “phasor
quantity” and “vector quantity,” the last name causing confusion with
space vectors. Inournotationv represents a voltage, hence V isacomplex
voltage. Equation (1-40) with v replaced by i and V replaced by I would
define a complex current, and so on. Note that the complex quantity is
not a function of time but it may be a function of position. Note also
that the magnitude of the complex quantity is the effective (root-meansquare) value of the instantaneous quantity. We have chosen it so
because (1) a-c quantities are usually specified or measured in effective
values in practice, and (2) equations for complex power and energy retain
the same proportionality factors as do their instantaneous counterparts.
For example, in circuit theory the instantaneous power is p = v7, and
complex power is P = VI*. A factor of 14 appears in the equation for
complex power if peak values of v and 7 are used for |V| and |J|.
Complex notation can readily be extended to vectors having sinusoidal
time variation. A complex E is defined as related to an instantaneous &
according to
& = \/2 Re (Ee’**) (1-41)
This means that the spatial components of E are related to the spatial
components of & by Eq. (1-40). For example, the z components of E
and & are related by
& = V2 Re (E.e*) = /2 |E,| cos (wt + az)
where E, = |E,Je’*s Similar equations relate the y and z components of
Eand&. The phase of each component may be different from the phases
of the other two components, that is, az, ay, and a, are not necessarily
equal. In our notation & is an electric intensity, hence E is called the complex electric intensity. Equation (1-41) with E replaced by H and & by #
1 The convention v = +/2 Im (Vei#*) can also be used, where Im (_) stands for
“the imaginary part of.” The factor 1/2 can be omitted if it is desired that |V| be the
peak value of v. e

16 TIME-HARMONIC ELECTROMAGNETIC FIELDS

defines a complex magnetic intensity H, representing the instantaneous
magnetic intensity 5, and so on. Note that the magnitude of a component of the complex vector is the effective value of the corresponding
component of the instantaneous vector. This choice corresponds to that
taken for complex scalars and has essentially the same advantages.

A real vector, such as & or 3, can be thought of as a triplet of real
scalar functions, namely, the z, y, and z components. At any instant of
time, the vector has a definite magnitude and direction at every point in
space and can be represented in three dimensions by arrows. A complex
vector, such as E or H, is a group of six real scalar functions, namely,
the real and imaginary parts of the z, y, and zcomponents. It cannot be
represented by arrows in three-dimensional space except in special cases.
One such special case is that for which a, = a, = a, so that the vector
hasarealdirectionin space. In this case the instantaneous vector always
points in the same direction (or opposite direction), at a point in space,
changing only in amplitude. We could define a “complex magnitude”
and a “complex direction” for a complex vector as extensions of the
corresponding definitions for real vectors, but these would have little use.

Throughout this book we shall use the following notation. Instantaneous quantities are denoted by script letters or lower-case letters.
Complex quantities which represent the instantaneous quantities are
denoted by the corresponding capital letter. Vectors are denoted vy
boldface type.

## Section 1-8: Complex Equations
 The symbol Re ( ) can be considered as a
mathematical operator which selects the real part of a complex quantity.
A set of rules for manipulating the operator Re ( ) can be formulated
from the properties of complex functions. The following are the rules
we shall need. Let a capital letter denote a complex quantity and a
lower-case letter denote a real quantity. Then

Re (A) + Re (B) = Re (A + B)
Re (aA) = a Re (A)
a _ aA 1-42
5 Re (A) = Re(34) (1-42)
[ Re (A) az = Re(f Adz)
The proof of these is left to the reader.

In addition to the above equations we shall need the following lemma.
If A and B are complex quantities, and Re (Ae) = Re (Be**) for all t,
then A = B. We can readily show this by first taking c = 0, obtaining
Re (A) = Re (B), and then taking wt = 7/2, obtaining Im (A) = Im (B).
Thus, A = B, for the above two equalities are the definition of this.

To illustrate the derivation of an equation for complex quantities from

FUNDAMENTAL CONCEPTS 17
one for instantaneous quantities, consider
v= fea
Expressing v and & in terms of their complex counterparts, we have
V2Re (Veiwt) = f V/2Re (Ee) - dl &
By steps justifiable by Eqs. (1-42), this reduces to
V2Re (Vo) = V2Re (ci [ E-al)
Cancellation of the 1/2’s and application of the above lemma then gives
v=feE-a
Note that this is of the same form as the original instantaneous equation.
We have illustrated the procedure with a scalar equation, but the same
steps apply to the components of a vector Equation.

From our rules for manipulation of the Re (__) operator, it should be
apparent that any equation linearly relating instantaneous quantities
and not involving time differentiation takes the same form for complex
quantities. Thus, the complex circuit quantities V, I, U, and K are
related to the complex field quantities E, H, J, and M according to

v-fEea u-/Ha

(1-43)

t=f[{J-as K=f[M-ds
There is no time differentiation explicit in the field equations written in
generalized current notation. Thecomplex forms of these must therefore
also be the same as the instantaneous forms. For example, the complex
form of Eqs. (1-20) is

vxE=-M vxH=J (1-44)
Even though these complex equations look the same as the corresponding
instantaneous equations, we should always keep in mind the difference in
meaning.

As an illustration of the procedure when the instantaneous equation
exhibits a time differentiation, consider the equation

3B
Vx'=-- OL
Again we express the instantaneous quantities in terms of the complex
:

18 TIME-HARMONIC ELECTROMAGNETIC FIELDS
quantities, and obtain
Vv X [V2 Re (Ee*")] = - z [/2 Re (Be**)]
The time variation is explicit, and the differentiation can be performed.
By steps justifiable by Eqs. (1-42), the above equation becomes
V2 Re (V x Eci*t) = - 1/2 Re (jwBei*t)
By the foregoing lemma, this reduces to
Vv xX E = -jwB

It should now be apparent that each time derivative in a linear instantaneous equation is replaced by a jw multiplier in the corresponding complex equation. For example, the Maxwell equations in complex form
corresponding to Eqs. (1-1) are

VX E = -joB v-B=0

Vx H=jD+J v-D=Q4, (1-45)
The other forms of these can be obtained in a similar fashion.

## Section 1-9: Complex Constitutive Parameters
 The constitutive relationships for matter linear in the general sense can be specialized to the a-c
case by the procedure of the preceding section. To illustrate, consider
the first of Eqs. (1-16), which is

) a?
a-(ctad+eg+ tice ‘ye
The complex form of this equation is readily found as
D = (€ + jwer - wep + + + *)E
The quantity (e€ + jwe, - we, + - - -) is just a complex function of w,
which we shall denote by '(w). Thus, the complex equation
D = &(w)E
which looks like the form for simple media, is actually valid for media
linear in the general sense.

The other two of Eqs. (1-16) simplify in a similar manner; so we have

the a-c constitutive relationships
D = @(w)E
B = a(w)H (1-46)
J* = c(w)E
for linear media. We call @ the complex permittivity of the medium, a
the complex permeability of the medium, and c the complex conductivity

FUNDAMENTAL CONCEPTS 19
of the medium. Remember that these parameters are not necessarily
the d-c parameters, but

#2), Ble), 88) > 6 mo
The d-c parameters may apply over a wide range of frequencies for some
materials but never over all frequencies (vacuum excepted).

In terms of the generalized current concept, the induced currents
(caused by the field) are &

J = @ + jwe)E = G(w)E

M = joaH = 2(w)H (1-47)
The parameter §(w) has the dimensions of admittance per length and will
be called the admittivity of the medium. The parameter 2(w) has the
dimensions of impedance per length and will be called the impedivity
of the medium. Note that % is a combination of the c and @ parameters.
A measurement of 9@ is relatively simple, but it is difficult to separate c
from '. The distinction is primarily philosophical. If the current is due
to free charge, we include its effect in c. If the current is due to bound
charge, we include its effect in @. Thus, when talking of conductors, the
usual convention is to let g = c + jweo. When discussing dielectrics,
it is common to let § = jwe.

To represent sources, impressed currents are added to the induced
currents of Eqs. (1-47). Thus, the general form of the a-c field equations
1s

-V X E = 24(0)H + M*

V XH = HWE + J (1-48)
The 2(w) and §(w) specify the characteristics of the media. The J‘ and
Mi represent the sources. Equations (1-48) are therefore two equations
for determining the complex field E, H. Solutions to these equations are
the principal topic of this book.

## Section 1-10: Complex Power
 In Sec. 1-5 we considered expressions for
instantaneous power and energy in terms of the instantaneous field
vectors. We shall show now that similar expressions in terms of the
complex field vectors represent time-average power and energy in a-c
fields. For this, we shall need the concept of complex conjugate quantities, denoted by *, and defined as follows. If A = a’ + ja” = |Ale’s,
the conjugate of A is A* = a’ - ja” = |Ale~**. It follows from this
that AA* = |A|?.

Let us first consider any two a-c quantities @ and ®, which may be
scalars or components of vectors. These are in general of the form

@ = V2|A| cos (wt + a) = /2 Re (Ae)
@ = V/2|B| cos (wt + B) = »/2 Re (Be*)

TIME-HARMONIC ELECTROMAGNETIC FIELDS
(aot A = |Ale* and B = |Ble*®. The product of two such quantities is
20
QB = V2 |A| cos (wt + a) V/2 |B cos (wt + 8)
= |A| |Bl{cos (a - 8) + cos (2wt + a + f)] (1-49)
We shall denote the time average of a quantity by a bar over that quantity. The time average of the above expression is
@B = |A| |B cos (a - 8)
We also note that =
AB* = |A| |B|[cos (a - 8) + § sin (a - B)]
so it is evident that
@B = Re (AB*) (1-50)
This identity forms the basis_of definitions of complex power.
oe The instantaneous Poynting vector [Eq. (1-28)] can be expanded in
* rectangular coordinates as
This is a sum of term: h of which is the of Eg. (1-49). therefore fatale - Bae) F a ae SS he JO TS Os od
5=&xX K = Re(E X H*)
In view of this we define a_compler Poynting vector
S=Ex H* (1-51)
whose real part is the time average of the instantaneous Poynting vector,
or
5 = Re (S) (1-52)
We shall interpret the imaginary part of S later.

We can obtain an equation in which S appears by operating on the
complex field equations in a manner similar to that used in the instantaneous case. Starting from Eqs. (1-44), we scalarly multiply the first by
H* and the conjugate of the second by E. The difference of the resulting
two equations is

E-v x H* -H*-v x E=E-J* +4 H*.M!
The left-hand term is -V-(E X H*) by a mathematical identity; so
we have
V-(E x H*) +E-J* + H*-M‘*=0 (1-53)
The integral form of this is obtained by integrating throughout a region

FUNDAMENTAL CONCEPTS 21
and applying the divergence theorem. This results in
pe x Ht-ds + fff (E-J*+H*-M)dr=0 (1-54)
Compare these with Eqs. (1-26) and (1-27). We shall call Eqs. (1-53)
and (1-54) expressions for the conservation of complex power, the former
applying at a point and the latter applying to an entire region.

The various terms of the above equations are interpreted & follows.
As suggested by Eqs. (1-29) and (1-52), we define a complex volume density
of power leaving a point as

pp =V-S=V-(EX H*) (1-55)
The real part of this is a time-average volume density of power leaving a
point, or
Re (By) = By (1-56)
where py is defined by Eq. (1-29). Similarly, we define the complex
power leaving a region as
P, = fpS-ds = PB x H*- ds (1-57)
It is evident from Eqs. (1-30) and (1-52) that the real part of this is the
time-average power flow, or
Re (Ps) = @, (1-58)
Note that these relationships are quite different from those used to interpret most complex quantities [Eqs. (1-40) and (1-41)]. This is because
8, p, and © are not sinusoidal quantities but are formed of products of
sinusoidal quantities.

To interpret the other terms of Eq. (1-53), let us first specialize to the
case of a source-free field in media linear in the simple sense. We then
have

Ji = gE = (06 + jue)E
M! = 2H = jonH
so E- J* = olE]? - juelE|?
H* - M! = jop|H|?
where |E|? means E - E* and |H|? means H- H*. In terms of the instantaneous energy and power definitions of Eqs. (1-32) and (1-33), we have
pa = o| El
we = YelEl? in simple media (1-59)
Bm = Mull
We can now write Eq. (1-53) as
VS + pat j2ultin - 3.) = 0 (1-60)

a
(22) TIME-HARMONIC ELECTROMAGNETIC FIELDS
Thus, the imaginary part of #, as defined by Eq. (1-55) is 2w times the
difference between the time-average electric and magnetic energy densities. The integral relationships corresponding to Eqs. (1-59) are
Ox = [[[ ore
w= s/// c|E|? dr in simple media (1-61)
wn =4/ ff ala
nm 2
where @z, We, and W,, are defined by Eqs. (1-36) and (1-37). The
specialization of Eq. (1-54) to source-free simple media is therefore
GPS + ds + B1 + j20(Wm - W.) = 0 (1-62)
corresponding to the point relationship of Eq. (1-60). Note that this
interpretation of complex power is precisely that chosen in circuit theory.
If sources are present, a complex power density supplied by the sources
can be defined as
p. = -(E-J* + H*- MS) (1-63)
The real part of this is the time-average power density supplied by the
sources, or
Re (p.) = Ds (1-64)
where p, is defined by Eq. (1-34). We can write Eq. (1-53) in general as
pe = Ps + Ba + j2w(tim - w) (1-65)
where all terms have been identified for simple media. Similarly, the
total complex power supplied by sources within a region can be defined as
p,= - [f[f @-J* +H". M) dr (1-66)
where, from Eq. (1-38), it is evident that
Re (P.) = ® (1-67)
Then the form of Eq. (1-65) applicable to an entire region is
Pr = Py t+ 0a + j20(Wn - W) (1-68)
The real part of this represents a time-average power balance. The
imaginary part is related to time-average energies, and, in conformity with
circuit theory nomenclature, is called reactive power.
Note that we have never defined @z, Wm, or W. for media linear in the
general sense. We can, however, continue to use Eq. (1-68) for the

FUNDAMENTAL CONCEPTS 23
general case of linear media by extending our definitions. This is done
as follows. The time-average power dissipation is defined in general as

b= Re[ {ff lel + ani) ar | (1-69)
which reduces to the first of Eqs. (1-61) in simple media. The first
term of the integrand represents both conduction and dielectric logses, and
the second term represents magnetic losses. The ithe averaplbeieetris
and magnetic energies are defined in general as

®.= anim f/f a1 dr)
f (1-70)
= Lim ii 2\H* dr)
20
which reduce to the last two of Eqs. (1-61) in simple media. The first of
Eqs. (1-70) includes kinetic energy stored by free charges as well as the
usual field and polarization energies. More discussion of this concept
is given in the next section. a

## Section 1-11: A-C Characteristics of Matter
 In source-free regions, the complex field equations read
-VXE=2%o)H VX H = g)E
In free space, 2 and # assume their simplest forms, being
G(w) = joeo | F
A . in free space 1-71
2(w) = joo P a7)
These hold for all frequencies and all field intensities. In metals, the
conductivity remains very close to the d-c value for all radio frequencies,
that is, up to the infrared frequency spectrum. The permittivity of
metals is hard to measure but appears to be approximately that of
vacuum. Thus,
Ie) ve + Jeo | in nonmagnetic metals (1-72)
2(w) = jopo
In ferromagnetic metals, zo would be replaced by a. We shall consider
this case later.
In good dielectrics, it is common practice to neglect c and express 9
entirely in terms of @. Thus,
Ge) = Jot | in nonmagnetic dielectrics (1-73)
2(w) = jwno
Let us now consider '(w) in more detail.!. We can express ' in both rec1A. Von Hipple, ‘Dielectric Materials and Applications,’ John Wiley & Sons,
Inc., New York, 1954. ’

24 TIME-HARMONIC ELECTROMAGNETIC FIELDS
tangular and polar form as

e(w) = e - jel’ = [ele (1-74)
where c’, c’’, and 6 are real quantities. We call c’ the a-c capac itivity,
'” the dielectric loss factor, and 6 the dielectric loss angle. In Sec. 1-13 we
shall see that they are related to the capacitance, resistance, and loss
angle, respectively, of an ideal circuit capacitor. In terms of power and
energy, we have from Kgs. (1-69) and (1-70) that

w= 5 If '|E|? dr

(1-75)

ba = If we|Bl* dr
Thus, c’ contributes to stored energy (acts like c in simple matter), and
we’ contributes to power dissipation (acts like o in simple matter).
Measured values of '(w) are usually expressed in terms of c’ and tan 6, or
in terms of c’ and c’. We shall use the latter representation.

A “perfect dielectric’? would be one for which c’ = 0. The only
perfect dielectric is vacuum. A “good dielectric” is defined to be one
for which c’ remains almost constant at all radio frequencies and for
which e” is very small. Examples of good dielectrics are polystyrene,
paraffin, and Teflon. Figure 1-10 shows c’ and c’’ versus frequency for
polystyrene to illustrate the characteristics of a good dielectric. There
is also a group of “lossy dielectrics,” characterized by a varying c and
a large c” in the radio-frequency range. Examples of lossy dielectrics
are Plexiglas, porcelain, and Bakelite. Figure 1-11 shows c and c’’
versus frequency for Plexiglas to illustrate the characteristics of a lossy
dielectric. There is a group of dielectrics which have unusually high
dielectric constants. The titanate and ferrite ceramics fall into this

3
KER
; B
goole Ltt tt ttt
oooet iL | | | tt ft ft tLe
Pt tt tt tt
0.0004 >
Fp ee oe
ol o L tl _| cea
10 102 103 104 105 106 107 108 109 1010
Frequency, cycles per sec
Fie, 1-10. &w) = «’ - je’ versus frequency for polystyrene at 25°C,

FUNDAMENTAL CONCEPTS 25
ow, a tt | | tt ttt
PT ATT TT TT YT
|. \
ost a} PSA] | TT TT
Pt tk eR HI
! ees
° ° v 3
onl ELA
* 010+ 2 Se
Leo
_ SS)
“,
005+ 1 =
PT tT PSN Tf
ol 0 ee es ed PD
10 102 103 104 105 106 10? 10% 109 101°
Frequency, cycles per sec
*Fig. 1-11. '(w) = c - je” versus frequency for Plexiglas at 25°C.*
class (the latter also being ferromagnetic). Such dielectrics are usually
lossy. A qualitative explanation of the behavior of @ can be made in
terms of atomic concepts, but we shall view @ as simply a measured
parameter. A table of @ for some common dielectrics is given in
Appendix B.

---

## Chapter 2: Introduction to Waves

INTRODUCTION TO WAVES

## Section 2-1: The Wave Equation
 A field that is a function of both time and
space coordinates can be called a wave. We shall, however, be a bit
more restrictive in our definition and use the term wave to denote a solution to a particular type of equation, called a wave equation. Electromagnetic fields obey wave equations, so the terms wave and field are
synonymous for time-varying electromagnetism. In this chapter we
shall consider a number of simple wave solutions to introduce and illustrate various a-c electromagnetic phenomena.

For the present, let us consider fields in regions which are source-free
(J‘ = M' = 0), linear (' and g independent of || and |H|), homogeneous
(2 and % independent of position), and isotropic (2 and g are scalar).
The complex field equations are then

VXxE= -2H
VxH=gE (21)
The curl of the first equation is
VxXxVXE=-2VvxH
which, upon substitution for V x H from the second equation, becomes
VXVXE= -2§E
The frequently encountered parameter
k= V=H (2-2)
is called the wave number of the medium. In terms of k, the preceding
equation becomes
VXVXE-FE=0 (2-3)
which we shall call the complex vector wave equation. If we return to
Eqs. (2-1), take the curl of the second equation, and substitute from the
first equation, we obtain
" vxvxH-PH=0 (2-4)
Thus, H is a solution to the same complex wave equation as is E.

38 TIME-HARMONIC ELECTROMAGNETIC FIELDS
The wave equation is often written in another form by defining an
operation
VA=V(V-A)-VXVXA
In rectangular components, this reduces to
WA = u.V’?A, + u,V?A, + u.V?A,
where u., u,, and u, are the rectangular-coordinate unit vectors and V?
is the Laplacian operator. It is implicit in the wave equations that
vV-E=0 v-H=0 (2-5)
shown by taking the divergence of Eqs. (2-3) and (2-4). Using Eqs. (2-5)
and the operation defined above, we can write Eqs. (2-3) and (2-4) as
VE+ KE=0
VH + PH = 0 2-6)
These we shall also call vector wave equations. They are not, however,
so general as the previous forms, for they do not imply Eqs. (2-5). In
other words, Eqs. (2-6) and Eqs. (2-5) are equivalent to Eqs. (2-3) and
(2-4). Thus, the rectangular components of E and H satisfy the complex
scalar wave equation or Helmholtz equation!
Vy+ky=0 (2-7)
We can construct electromagnetic fields by choosing solutions to Eq. (2-7)
for E., E,, and E, or H., H,, and H., such that Eqs. (2-5) are also satisfied.
To illustrate the wave behavior of electromagnetic fields, let us construct a simple solution. Take the medium to be a perfect dielectric,
in which case § = jwe, 2 = jwp, and
k=aVeu (2-8)
Also, take E to have only an z component independent of z and y. The
first of Eqs. (2-6) then reduces to
PE, ap _
re +E, =0
which is the one-dimensional Helmholtz equation. Solutions to this are
linear combinations of e** and e~**. In particular, let us consider a
solution
E, = Eye“ (2-9)
This satisfies V - E = 0 and is therefore a possible electromagnetic field.
1 We shall use the symbol y to denote “wave functions,” that is, solutions to
Eq. (2-7). Do not confuse these y’s with magnetic flux.

INTRODUCTION TO WAVES 39
The associated magnetic field is found according to
jouH = -V X E = u,jkE
which, using Eg. (2-8), can be written as
E,= Ji H, (2-10)
Ratios of components of E to components of H have the dimensions of
impedance and are called wave impedances. The wave impedance associated with our present solution,
Ez |p
= y= J (2-11)
is called the intrinsic impedance of the medium. In vacuum,
- a
no = J = 1207 ~ 377 ohms (2-12)
0
We shall see later that the intrinsic impedance of a medium enters into
wave transmission and reflection problems in the same manner as the
characteristic impedance of transmission lines.
To interpret this solution, let /’) be real and determine & and # according to Eq. (1-41). The instantaneous fields are found as
& = V2 Eo cos (wt - kz)
2 2-13
KR, = vo, cos (wt - kz) ( )
This is called a plane wave because the phase (kz) of & and X is constant
over a set of planes (defined by z = constant) called equiphase surfaces.
It is called a uniform plane wave because the amplitudes (Zo and E/n) of
& and % are constant over the equiphase planes. 6& and 3c are said to be
in phase because they have the same phase at any point. Atsome specific
time, & and 3 are sinusoidal functions of z. The vector picture of *Fig. 2-1
illustrates & and 3 along the z axis att = 0. The direction of an arrow*
represents the direction of a vector, and the length of an arrow represents
the magnitude of a vector. If we take a slightly later instant of time,
the picture of *Fig. 2-1 will be shifted in the +z direction. We say*
that the wave is traveling in the +z direction and call it a traveling wave.
The term polarization is used to specify the behavior of & lines. In this
wave, the & lines are always parallel to the x axis, and the wave is said to
be linearly polarized in the x direction.
The velocity at which an equiphase surface travels is called the phase

40 TIME-HARMONIC ELECTROMAGNETIC FIELDS
velocity of the wave. An equiphase plane z = 2z, is defined by
wt - kzp = constant
that is, the argument of the cosine functions of Eq. (2-13) is constant.
As c increases, the value of z, must also increase to maintain this constancy, and the plane z = z, will move in the +zdirection. This is illustrated by *Fig. 2-2, which is a plot of & for several instants of time. To*
obtain the phase velocity dz,/dt, differentiate the above equation. This
gives
dz,
w-k ried 0
The phase velocity of this wave is called the intrinsic phase velocity vp 07
the dielectric and is, according to the above equation,
dz, _ wo 1
= EAE We (2-14)
In vacuum, this is the velocity of light: 3 X 108 meters per second. :
The wavelength of a wave is defined as the distance in which the phase
increases by 27 at any instant. This distance is shown on *Fig. 2-2. The*
wavelength of the particular wave of Eqs. (2-13) is called the intrinsic
wavelength » of the medium. It is given by kA = 2z, or
2r - 2x, v.
eS ew S'S 
: =. ; (2-15)
where f is the frequency in cycles per second. The wavelength is often
used as a measure of whether a distance is long or short. The range of
wavelengths encountered in electromagnetic engineering is large. For
example, the free-space wavelength of a 60-cycle wave is 5000 kilometers,
whereas the free-space wavelength of a 1000-megacycle wave is only 30
centimeters. Thus, a distance of 1 kilometer is very short at 60 cycles,

xX
Direction of travel -->»
'
Zz
HA
Y
*Fig. 2-1. A linearly polarized uniform plane traveling wave.*

INTRODUCTION TO WAVES 41
's
ot=c
ot = 1/4
2p ot = 1/2
Zz
a

Fia. 2-2. & at several instants of time in a linearly polarized uniform plane traveling
wave.
but very long at 1000 megacycles. The usual circuit theory is based on
the assumption that distances are much sh'rter than a wavelength.

## Section 2-2: Waves in Perfect Dielectrics
 In this section we shall consider
the properties of uniform plane waves in perfect dielectrics, of which
free space is the most common example. We have already given a special
case of the uniform plane wave in the preceding section. To summarize,

E, = Ey-® Hy, = Bo ins
7
where k=oVe= tae
? (2-16)
-f
n=.f/6
€
It is an z-polarized, +z traveling wave. Because of the symmetry of the
rectangular coordinate system, other uniform plane-wave solutions can
be obtained by rotations of the coordinate axes, corresponding to cyclic
interchanges of coordinate variables. We wish to restrict consideration
to +z and -z traveling waves; so we shall consider only the transformations (z,y,z) to (-y,z,z), to (z,-y, -z), and to (y,z,-z). This procedure,
together with our original solution, gives us the four waves
A. .
E,t = Ae-it H,t = Sei
7
E,*+ = Be-i** Ha = -B enik
o . (2-17)
Es = Ceit* Hy = = ike
?
E, = Dei* He = D ike

42 TIME-HARMONIC ELECTROMAGNETIC FIELDS

where the previously used E> has been replaced by A, B, C, or D. The
superscript + denotes a +z traveling wave, and the superscript - denotes
a -z traveling wave. The most general uniform plane wave is a superposition of Eqs. (2-17).

We have already interpreted the first wave of Eqs. (2-17) in Sec. 2-1.
This also constitutes an interpretation of the other three waves if the
appropriate interchanges of coordinates are made. We have not yet
mentioned power and energy considerations, so let us do so now. Given
the traveling wave

EL = Eige7ik# H, = Bo ine
ul]
we evaluate the various energy and power quantities as
Ww, = 5 &? = eEo? cos? (wt - kz)
Wn = 5 at = Eo? cos? (wt - kz)
2 (2-18)
S=EXKH= us 7 Eo? cos? (wt - kz)
2
S=ExH*=u,2"
ul]
Thus, the electric and magnetic energy densities are equal, half of the
energy of the wave being electric and half magnetic. We can define a
velocity of propagation of energy v. as
_ power flow density _ s
ve energy density We + Wm (2-19)
For the uniform plane traveling wave, from Eqs. (2-18) and (2-19) we find
v= 1
“Vue
which is also the phase velocity [Eq. (2-14)]. These two velocities are
not necessarily equal for other types of electromagnetic waves. In general, the phase velocity may be greater or less than the velocity of light,
butthe velocity of propagation of energy is never greater than the velocity
of light.

Another property of waves can be illustrated by the standing wave

E, = Eo sin kz H,= j* cos kz (2-20) \
obtained by combining the first and third waves of Eqs. (2-17) with

INTRODUCTION TO WAVES 43
A -C =jE,/2. The corresponding instantaneous fields are
& = V2 Ey sin kz cos wt KR, = = V2 eos ke sin ot
Note that the phase is now independent of z, there being no ‘rageling
motion; hence the name standing wave. A picture of & and % at®some
instant of time is shown in *Fig. 2-3. The field oscillates in amplitude,*
with & reaching its peak value when JC is zero, and vice versa. In other
words, & and 3c are 90° out of phase. The planes of zero & and 3 are
fixed in space, the zeros of & being displaced a quarter-wavelength from
the zeros of 3C. Successive zeros of & or of 5C are separated by a halfwavelength, as shown on *Fig. 2-3. The wave is still a plane wave, for*
equiphase surfaces are planes. Itisstilla uniform wave, for its amplitude
is constant over equiphase surfaces. It is still linearly polarized, for &
always points in the same direction (or opposite direction when & is
negative). a
The energy and power quantities associated with this wave are
We = 58 = eff," sin? kz cos? wt
Wn = 5 3? = e€E,? cos? kz sin? wt
By (2-21)
S=EXK= -u. 57 sin 2kz sin 2wt
, 2
S=Ex H*¥= ay, tee sin 2kz
2
The time-average Poynting vector § = Re (S) is zero, showing no power
flow on the average. The electric energy density is a maximum when
the magnetic energy density is zero, and vice versa. A picture of energy
xX
' es
7. 1 LPs
AL PR Zr AI Le
Zz
l ee"
y
c
*Fig. 2-3. A linearly polarized uniform plane standing wave.*

44 TIME-HARMONIC ELECTROMAGNETIC FIELDS
lE:|
A+Cc
A-C
hoes N/2 asi
Zz

*Fig. 2-4. Standing-wave pattern of two oppositely traveling waves of unequal amplitudes.*
oscillating between the electric and magnetic forms can be used for this
wave. Note that we have planes of zero electric intensity at kz = nz,
nan integer. Thus, perfect electric conductors can be placed over one
or more of these planes. If an electric conductor covers the plane z = 0,
Eqs. (2-20) represent the solution to the problem of reflection of a uniform
plane wave normally incident on this conductor. If two electric conductors cover the planes kz = mz and kz = nor, Eqs. (2-20) represent
the solution of a one-dimensional “resonator.”

A more general z-polarized field is one consisting of waves traveling
in opposite directions with unequal amplitudes. This is a superposition
of the first and third of Eqs. (2-17), or

= Aenite 4+ Ceite
E ‘ e-# + Ce (2-22)
H, = = (Ae - Cei*)
0
If A = OorC = 0, we have a pure traveling wave, and if |A| = |C|, we
have a pure standing wave. For A # C, let us take A and C real! and
express the field in terms of an amplitude and phase. This gives
stan-1 (4-8
B. = VE FOF TAC costes e " GFe"*) (2.03)
The rms amplitude of E is
a/ A? + GC? + 2AC cos 2kz

which is called the standing-wave pattern of the field. This is illustrated
by *Fig. 2-4. The voltage output of a small probe (receiving antenna)*
connected to a detector would essentially follow this standing-wave pat
1 This is actually no restriction on the generality of our interpretation, for it corresponds to a judicious choice of z and c origins.

INTRODUCTION TO WAVES 45
tern. Fora pure traveling wave, the standing-wave pattern is a constant,
and for a pure standing wave, it is of the form |cos kz|, that is, a “rectified”? sine wave. The ratio of the maximum of the standing-wave pattern to the minimum is called the standing-wave ratio (SWR). From
*Fig. 2-4, it is evident that &*

A+C /
= 2-24
SWR=4, 6 (2-24)

because the two traveling-wave components [Eqs. (2-22)] add in phase at
some points and add 180° out of phase at other points. The distance
between successive minima is \/2. The standing-wave ratio of & pure =
traveling wave is unity, that of a pure standing wave is infinite. Plane
traveling waves reflected by dielectric or imperfectly conducting boundaries will result in partial standing waves, with SWR’s between one and
infinity.

Let us now consider a traveling wave in*which both B, and E, exist.
This is a superposition of the first and second of Eqs. (2-17), that is,

E = (u,A B)e~#

(u,A + u,B)e ; (2-25) ;
: H = (-u,B + u,A) 3 ewe
If B = 0, the wave is linearly polarized in the x direction. If A = 0,
the wave is linearly polarized in the y direction. If A and B are both
real (or complex with equal phases), we again have a linearly polarized
wave, with the axis of polarization inclined at an angle tan-! (B/ A) with
respect to the z axis. This is illustrated by *Fig. 2-5a. If A and B are*
complex with different phase angles, & will no longer point in a single
spatial direction. Letting A = |Ale*and B = |Ble’, we have the instanY bf ters .
7 + rotates in
fi vibrates on Baia this direction
Vie }--"S at = 50/4 RTS
| x : wt=0
V2A of = 7 \ 7 x
N a a/A
ot = 37/4 = ria 2/2
@ 5 (6)
*Fig. 2-5. Polarization of a uniform plane traveling wave. (a) Linear polarization;*
(b) elliptical polarization. %

46 TIME-HARMONIC ELECTROMAGNETIC FIELDS
taneous electric intensity given by
& = V/2|A| cos (wt - kz + a)
& = V/2 |B| cos (wt - kz + b)
A vector picture of & for various instants of time changes in both amplitude and direction, going through this variation once each cycle. For
example, let |A| = 2|B|,a =0, and b =7/2. A plot of & for various
values of c in the plane z = 0 is shown in *Fig. 2-5b. The tip of the arrow*
in the vector picture traces out an ellipse, and the field is said to be
elliptically polarized. Depending upon A and B, this ellipse can be of
arbitrary orientation in the zy plane and of arbitrary axial ratio. 7sinear
polarization can be considered as the special case of elliptic polarization
for which the axial ratio is infinite.
~ If the axial ratio is unity, the tip of the arrow traces out a circle, and
the field is said to be circularly polarized. The polarization is said to be
right-handed if & rotates in the direction of the fingers of the right hand
when the thumb points in the direction of propagation. The polarization
is said to be left-handed if & rotates in the opposite direction. The specialization of Eq. (2-25) to right-handed circular polarization is obtained by
setting A = jB = Ep, giving
= (u, - ju,) Eye
; E = (u. - ju,) we (2-26)
H = (u. - juy)j Toe
A vector picture of the type of *Fig. 2-1 for this wave would show & and 3c*
in the form of two corkscrews, with & perpendicular to 3c at each point.
As time increases, this picture would rotate giving a corkscrew type of
motion in the z direction. The various energy and power quantities
associated with this wave are
w= £89 = By
oS
Dm = 5a? = eE,?
2 (2-27)
BBR te Ey
S=Ex H* = u.2 Bet
Thus, there is no change in energy and power densities with time or
space. Circular polarization gives a steady power flow, analogous to
circuit-theory power transmission in a two-phase system.

INTRODUCTION TO WAVES 47
As a final example, consider the circularly polarized standing-wave field
specified by
_ - ink
E = (u,+ ia) Ee sin kz (2-28)
H = (uz + ju,) 2 cos kz
n
This is the superposition of Eqs. (2-17) for which A = a, jE/2,
D = -B = E)/2. The corresponding instantaneous fields are
& = (uzcos wt - u, sin wt) ~/2 Ey sin kz
H = (u,coswt - u,sinuwt) +/2 20s kz
Note that & and # are always parallel to each other. A vector picture
of 8and # at t = Oisshown in *Fig. 2-6. As time progresses, this picture*
rotates about the z axis, the amplitudes of & and # being independent of
time. It is only the direction of 8 and # which changes with time. The
amplitudes of & and & are, however, a function of z, giving a standingwave pattern in the z direction. The energy and power densities associated with this wave are
w= 5° = «By sin? kz
Un = 5 ae = cE,? cos? kz
8=8xK=0 (2-29)
S= -u, : Eo? sin 2kz
It is interesting to note that the instantaneous energy and power densities
are independent of time. This field can represent resonance between two
perfectly conducting planes situated where EF is zero. It thus seems that
the picture of energy oscillating between the electric and magnetic forms
x
€
+ Zz
H
&
Ul
Fie. 2-6. A circularly polarized uniform plane standing wave.
*%

48 TIME-HARMONIC ELECTROMAGNETIC FIELDS

is not generally valid for resonance. However, the circularly polarized
standing wave is the sum of two linearly polarized waves which can exist
independently of each other. We actually have two coincident resonances (called a degenerate case), and the picture of energy oscillating
between electric and magnetic forms applies to each linearly polarized
resonance.

## Section 2-3: Intrinsic Wave Constants
 When the wave aspects of electromagnetism are emphasized, the wave number k and the intrinsic impedance 9, given by

k=V-4 n= mt (2-30)
play an important role. The second equation is a generalization of Eq.
(2-11), obtained in the same manner as Eq. (2-11) when 2 and @ are not
specialized to the case of a perfect dielectric. We can solve Eqs. (2-30)
for 2 and %, obtaining

a=jly g-% (2-31)
A knowledge of k and 7 is equivalent to a knowledge of 2 and #, and
hence specifies the characteristics of the medium.

The wave number is, in general, complex, and may be written as

k =k’ - jk’ (2-32)
where k’ is the intrinsic phase constant and k” is the intrinsic attenuation
constant. We have already seen that when k = k’, it enters into the
phase function of the wave. We shall see in the next section that k’’
causes an exponential attenuation of the wave amplitude. The behavior
of k can be illustrated by a complex diagram relating k to 2 and @.

This is shown in *Fig. 2-7. In the*
Im expressions
2 G =o t+ we’ + jue’
ay $ 2 = op" + jon!

o, e”, and yp” are always positive in
ld source-free media, for they account
es for energy dissipation. The paramR! { ! Re eterse’ and uw’ are usually positive but
Seek may be negative for certain types of
atomic resonance. Thus, 2 and §
- usually lie in the first quadrant of the
complex plane, as shown in *Fig. 2-7.
Fig. 2-7. Complex diagram relating kto The product -2g then usually lies*
Zand 9. in the bottom half of the complex

INTRODUCTION TO WAVES 49
Im
Zz
5
*Fig. 2-8. Complex diagram relating xx = 7*
to Zand 9.
\--- Re
R
1/3
plane. The principal square root, k = ~/-2%, lies in the fourth quadrant, showing that k’ and k” are usually posjtive. Even when '’ or p’ is
negative, k’’ is positive; it is only k’ that cotta conceivably be negative.
In lossless media, 7 = jwe, 2 = jw, and k is real.

The intrinsic wave impedance can be considered in an analogous

manner. Expressing 7 in rectangular components, we have

n= K+ jx (2-33)
where & is the intrinsic wave resistance and & is the intrinsic wave reactance. Fora wave ina perfect dielectric, 7 is purely resistive and is therefore the ratio of the amplitude of & to 3c. We shall see in Sec. 2-4 that
x introduces a phase difference between & and %. The complex diagram
relating 7 to % and 2 in general is shown in *Fig. 2-8. In source-free*
regions, g, '’, and yw” are always positive, and c’ and yp’ are usually positive. Thus 2 usually lies in the first quadrant and 1/9 in the fourth
quadrant. The ratio 2/9 therefore usually lies in the right half plane
and 7 in the sector +45° with respect to the positive real axis. When
' or p’ is negative, 7 may lie anywhere in the right half plane, but ® is
never negative. In lossless media, the wave impedance is real.

There are several special cases of particular interest to us. First, consider the case of no magnetic losses. From the first of Eqs. (2-31), we
have

_ 2 &k* _ _ jk*2
7 jk) ek*~ ~ lal Tal
the last equality following from Eqs. (2-30). Now for 2 = jon = Jlal,
we have
a k* .
7= a no magnetic losses (2-34)

50 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TasLe 2-1. Wave NuMBER (k = k’ - jk’) anp INTRINSIC
IMPEDANCE (y = R +jX = |nle**)
cp [=e
General ReV/ -29 | -Im-V/-29| Re Ji Im Ji
: __ a K Ke!
No magnetic losses Im WV jouh Re MV jong il ia
Perfect. dielectric oV ue 0 y" 0
€
iclectri 7 vet [i 2 “ [=
Good dielectric | oV ne NE we Ve
lwo wo woe wp
Good conductor | Neow | Nae Nis No
Separation into real and imaginary parts is shown explicitly in row 2 of
Table 2-1. A similar simplification can be made for the case of no electric losses. (See Prob. 2-13.) Three special cases of materials with no
magnetic losses are (1) perfect dielectrics, (2) good dielectrics, and (3)
good conductors. The perfect dielectric case is that for which
k=oVue = vi
This is summarized in row 3 of Table 2-1. A good dielectric is characterized by 4 = jwu, § = we’ + jue’, with &’ >”. In this case, we have
77 ”
k= "(1 -jh)\x me (i-7&
@ a/e ( j 7) o Vue (: J5g
k* a ( wet?
=" 2 fF(1 4585
7 Tal NE + i538
which is summarized in row 4 of Table 2-1. Finally, a good conductor is
characterized by 2 = juz, § = 0 + jue, witha > we In this case, we have
k = V-joulo + jue) ~ VW -jouo
k* jou
,-i es aft
{a o
The last row of Table 2-1 shows these parameters separated into real and
imaginary parts.

INTRODUCTION TO WAVES 51

## Section 2-4: Waves in Lossy Matter
 The only difference between the wave
equation, Eq. (2-7), for lossy media and loss-free media is that k is complex in lossy media and real in loss-free media. Thus, Eq. (2-9) is still a
solution in lossy media. In terms of the real and imaginary parts of k,
it is
E, = Byeni#® = Bye-#"se-i¥'* ®e-35)
Also, H is still given by Eq. (2-10), except that 7 is now complex. Thus,
the H associated with the E of Eq. (2-35) is
H, = Eo ots = Eo ote tree ik' (2-36)
7 In] 8
where 7 = |nle. The instantaneous fields corresponding to Eqs. (2-35)
and (2-36) are
6. = V/2 Eve-*’”? cos (wt - k’z)
= E a 2-37
By = V2 FA es 00s (ut % Be - 5) (2-30)
Thus, in lossy matter, a traveling wave is attenuated in the direction of
travel according to e~*, and 3c is no longer in phase with &. A sketch
of & and 3c versus z at some instant of time would be similar to *Fig. 2-1
except that the amplitudes of & and 3 would decrease exponentially with*
z, and 3 would not be in phase with & (3c usually lags 8). A sketch of
&, versus z for several instants of time is shown in *Fig. 2-9 for a case of*
fairly large attenuation. A sketch of JC, versusz would be similar in form.
&
Direction of travel) --->
oy
a Envelope ~ e- *”?
~nL
Zz
Z- ot = 7/2
aoe ot = 2/4 y
“t=9
*Fig. 2-9. & at several instdnts of time in a linearly polarized uniform plane traveling*
wave in dissipative matter.
nH

52 TIME-HARMONIC ELECTROMAGNETIC FIELDS
The wave of Eq. (2-37) is still uniform, still plane, and still linearly
polarized. So that our definitions of phase velocity and wavelength will
be unchanged for lossy media, we should replace k and k’ in the loss-free
formulas, or

ae le (2-38)
Then 2, is still the velocity of a plane of constant phase, and 2 is still
the distance in which the phase increases by 27.

Two cases of particular interest are (1) good dielectrics (low-loss), and
(2) good conductors (high-loss). For the first case, we have (see Table
2-1)

ki = 0V/pe
”
yy DET TR
was ve
in good dielectrics (e” _c’) (2-39)
“1 '
c = tan ay
Thus, the attenuation is very small, and § and 5 are nearly in phase.
The wave is almost the same as in a loss-free dielectric. For example, in
polystyrene (see *Fig. 1-10), a 10-megacycle wave is attenuated only 0.5*
per cent per kilometer, and the phase difference between & and % is
only 0.003°. The intrinsic impedance of a dielectric is usually less than
that of free space, since usually e’ > c9 and » = yo. The intrinsic phase
velocity and wavelength in a dielectric are also less than those of free
space.
In the high-loss case (see Table 2-1), we have
ra [HE
k 2
Kl = Ve
z in good conductors (a >> we) (2-40)
= ,|%H
hl = |
Tv
tq
Thus, the attenuation is very large, and 3c lags & by 45°. The intrinsic
impedance of a good conductor is extremely small at radio frequencies,
having a magnitude of 1.16 X 10-* ohm for copper at 10 megacycles.
The wavelength is also very small compared to the free-space wavelength.
For example, at 10 megacycles the free-space wavelength is 30 meters,
while in copper the wavelength is only 0.131 millimeter. The attenuation

INTRODUCTION TO WAVES 53
in a good conductor is very rapid. For the above-mentioned 10-megacycle wave in copper the attenuation is 99.81 per cent in 0.131 millimeter of travel. Thus, waves do not penetrate metals very deeply. A
metal acts as a shield against electromagnetic waves.

A wave starting at the surface of a good conductor and propagating
inward is very quickly damped to insignificant values. The fd is
localized in a thin surface layer, this phenomenon being known as skin
effect. The distance in which a wave is attenuated to 1/e (36.8 per cent)
of its initial value is called the skin depth or depth of penetration 6. This
is defined by k’’6 = 1, or

hy ae Oe
$= oad De (2-41)
where \,, is the wavelength in the metal. The skin depth is very small for
good conductors at radio frequencies, for \, is very small. For example,
the depth of penetration into copper at 10 megacycles is only 0.021
millimeter. The density of power flow into*the conductor, which must,
also be that dissipated within the conductor, is given by

S=E x H* = uJHol?nm
where Ho is the amplitude of H at the surface. The time-average power
dissipation per unit area of surface cross section is the real part of the
above power flow, or

Oz = |H\?R watts per square meter (2-42)
where ® = Re (y,,) is the intrinsic resistance of the metal. ® is also
called the surface resistance and 1m the surface impedance of the metal.
Eq. (2-42) is strictly true only when the wave propagates normally into
the conductor. In the next section we shall see that this is usually so.
In most problems Eq. (2-42) can be used to calculate power losses in
conducting boundaries. (An important exception to this occurs at sharp
points and corners extending outward from conductors.)

More general waves can be constructed by superposition of waves of
the above type with various polarizations and directions of propagation.
For waves uniform in the zy plane, the four basic waves, corresponding
to Eqs. (2-17), are

Es = Ae **c-ik's A,* = A enh te -ik es
i]
Pern -B ye, i!
E,* = Be-*"*e-ik'= Hit = -- e7*tce-ik's
_ (2-43)
B= = Cek=eik'= A, = ek tgik’e
e 7
E,- = Dette Hy = P errens

54 TIME-HARMONIC ELECTROMAGNETIC FIELDS
The preceding discussion of this section applies to each of these waves if
the appropriate interchange of coordinates is made.

A superposition of waves traveling in opposite directions, for example

EB, = Ae*'*e-i¥= 4 Cek'teit’?

H, = : (Aem#"=e-k= - Cek'zeik') (2-44)
gives us standing-wave phenomena. However, it is no longer possible
to have two “equal” waves traveling in opposite directions. One wave
is attenuated in the +2 direction, the other in the -z direction; hence
they can be equal only at one plane. Suppose that the wave components
are equal at z = 0, that is, A = C.in Eq. (2-44). There will then be
standing waves in the vicinity of z = 0, which will die out in both the +z
and -z directions. This is illustrated by *Fig. 2-10 for a material having*
fairly large losses. Far in the +2 direction the +z traveling wave has
died out, leaving only the -z traveling wave. Similarly, far in the -z
direction we have only the +z traveling wave. The standing-wave ratio
is now a function of z, being large in the vicinity of z = 0 and approaching
unity as |z| becomes large. For very small amounts of dissipation, say
in a good dielectric, the attenuation of the wave is small, and standingwave patterns are almost the same as for the dissipationless case.

Other superpositions of Eqs. (2-43) can be formed to give elliptically
and circularly polarized waves. In a picture of a circularly polarized
wave traveling in dissipative media, the ‘“‘corkscrews” for & and # would
be attenuated in the direction of propagation. Also, & would be somewhat out of phase with #. A circularly polarized standing wave would
be a localized phenomenon in dissipative media, just as alinearly polarized
standing wave is localized.

## Section 2-5: Reflection of Waves
 We saw in Sec. 1-14 that the tangential
components of E and H must be continuous across a material boundary.

lz
ee) ed nk, eft
aes -,
he ee 2 7, Pet
Zz
Fie. 2-10. Standing-wave pattern of two oppositely traveling waves ip dissipative
matter.

INTRODUCTION TO WAVES 55
A ratio of a component of E to a com- . .
ponent of H is called the wave imped- Region (1) Region (2)
ance in the direction defined by the
cross-product rule applied to the two components. Thus, continuity of tan- Incident 4 :
gential E and H requires that wave _Transgitted
° . Reflected
impedances normal to a material bound- -<----ary must be continuous.
The simplest reflection problem is
that of a uniform plane wave nor- Z
mally incident upon a plane boundary *Fig. 2-11. Reflection at a plane dibetween two media. Thisisillustrated electric interface, normal incidence.*
by *Fig. 2-11. In region 1 the field will*
be the sum of an incident wave plus a reflected wave. The ratio of the
reflected electric intensity to the incident electric intensity at the interface
is defined to be the reflection coefficient T. Hence, for region 1
EB, = Eo(e-*! + Pei)
Hy = Eo (e7 ihe = Tet)
m1
In region 2 there will be a transmitted wave. The ratio of the transmitted electric intensity to the incident electric intensity at the interface
is defined to be the transmission coefficient T. Hence, for region 2
BE) = EoTe*
H,® = Eo Te ike
n2
For continuity of wave impedance at the interface, we have
Z _ E, _ 14+7T_
7 | 20 = H,® |,20 = 7 en n2
where m and 72 are the intrinsic wave impedances of media 1 and 2.
Solving for the reflection coefficient, we have
nz - Mm
r= --- 2-45,
m+ 11 ( )
From the continuity of E, at z = 0, we have the transmission coefficient
given by
2
Telcr=-2 |. (2-46)
mtm }
If region 1 is a perfect dielectric, the standing-wave ratio is
. E®, 14+!
* SWR = [= (2-47
SWR = 5a = To (2-47)

56 TIME-HARMONIC ELECTROMAGNETIC FIELDS
¥ \
\
i
\ 3
NN 40,00
es ee SS RC
y’ sf SK, ee
2 Tix. 7
ee cd 1. Zz
an re
ais ' <a
ae \ x
» ' N.
S Th aie
1e .. 13% ON
NU"
€ Ks \.
z NS vA
\

*Fig. 2-12. A plane wave propagating at an angle & with respect to the z-z plane.*
because the incident and reflected waves add in phase at some points and
add 180° out of phase at other points. The density of power transmitted
across the interface is

Stam = REE x H*+u,| | = Sie(l - [P/) (2-48)
where Sine = Ho?/m: is the incident power density. The difference
between the incident and transmitted power must be that reflected, or

Srett = Sino I]? (2-49)
We have used an z-polarized wave for the analysis, but the results are
valid for arbitrary polarization, since the z axis may be in any direction
tangential to the boundary. Those of us familiar with transmission-line
theory should note the complete analogy between the above plane-wave
problem and the transmission-line problem.

Another reflection problem of considerable interest is that of a plane
wave incident at an angle upon a plane dielectric boundary. Before
considering this problem, let us express the uniform plane wave in coordinates rotated with respect to the direction of propagation. Let *Fig. 2-12
represent a plane wave propagating at an angle & with respect to the rz*
plane. An equiphase plane z’ in terms of the unprimed coordinates is

2’ =zcost+ysint
and the unit vector in the y’ direction in terms of the unprimed coordinate
unit vectors is
uy = u, cos - - u, sin §

INTRODUCTION TO WAVES 57
The expression for a uniform plane wave with E parallel to the z = 0
plane is the first of Eqs. (2-17) with all coordinates primed. Substituting
from the above two equations, we have
E, = Eeni#ein €+2 008 &)
H = (u, cos & - u, sin £) Eo sty sin Bt e000 8 a eho)
1
The wave impedance in the z direction for this wave is
E. ”
= t= 2-51
2s H, cos & (2-51)
In a similar manner, from the second of Eqs. (2-17), the expression for a
uniform plane wave with H parallel to the z = 0 plane is found to be
E = (u,cos & - uz sin £) Zoe sin t+ 08 €)
H,=-- Ey enik(y sin E42 cos &) (2-52)
] 4,
The wave impedance in the z direction for this wave is
Z=-- z =ncost (2-53)
Thus, the z-directed wave impedance for E parallel to the z = 0 plane
is always greater than the intrinsic impedance, and for H parallel to the
z = 0 plane it is always less than the intrinsic impedance of the medium.
Now suppose that a uniform plane wave is incident at an angle § = 0;
upon a dielectric interface at 2 = 0, as shown in *Fig. 2-13. Part of the*
wave will be reflected at an angle = w - 0,, and part transmitted at an
angle = = 6,. Eachof these partial fields will be of the form of Eqs. (2-50)
if E is parallel to the interface or of the form of Eqs. (2-52) if H is parallel
to the interface. (Arbitrary polarization is a superposition of these two
Region (1) Region (2)
*Fig. 2-13. Reflection at Gy garni*
a plane dielectric inter- 6, ais
face, arbitrary angle of esas bens) B
incidence. 6; A
i
a
e
Ze
%

58 TIME-HARMONIC ELECTROMAGNETIC FIELDS
cases.) For continuity of tangential E and H over the entire interface,
the y variation of all three partial fields must be the same. This is so if
ky sin 6; = ky sin 6, = ka sin @,
From the first equality, we have
0, = 6 (2-54)
that is, the angle of reflection is equal to the angle of incidence. From the
second equality, we have
sin @ ky _ 2 _ fey
sin®; ke v1 ‘eoue (2-55)
where v is the phase velocity. Equation (2-55) is known as Snell’s law
of refraction. The direction of propagation of the transmitted wave is
thus different from that of the incident wave unless e141 = eo2. In
practically all low-loss dielectrics, 41 = ue = wo. If medium 2 is free
space and medium | is a nonmagnetic dielectric, the right-hand side of
Eq. (2-55) becomes ~/e:/e0 = Ver, which is called the index of refraction
of the dielectric.
The magnitudes of the reflected and transmitted fields depend upon the
polarization. For E parallel to the interface, we have in region 1
BE, = A (e~ik12 c08 85 + Teikiz eos 8)
H,® = A COS O;(e7#1# e088 - Preitr2 con 8)
m
where A includes the y dependence. Thus, tie z-directed wave impedance
in region 1 at the interface is
ZO = BO _ nm itt
H,® ~ cos#:1 -T
This must be equal to the z-directed wave impedance in region 2 at the
interface, which is Eq. (2-51) with & = @. Thus, --_ 12sec 6, - m sec 9; _
re nz sec 0 + m1 Sec 6; (2-56)
Note that this is of the same form as the corresponding equation for
normal incidence, Eq. (2-45). The intrinsic impedances are merely
replaced by the z-directed wave impedances of single traveling waves.
It should be apparent from the form of the equations that, for H parallel
to the interface, the reflection coefficient is given by
_ 72 COS 4 - 71 Cos 6; 7
r= 72 COS 6; + m1 Cos 6; (2-57)

INTRODUCTION TO WAVES 59
In both cases we have standing waves in the z direction, the standing-wave
ratio being given by Eq. (2-47).

Two cases of special interest are (1) that of total transmission and (2)
that of total reflection. The first case occurs when Tl = 0. For E
parallel to the interface, we see from Eq. (2-56) that T = 0 when

ple
cos 4 cas 6;
Substituting for 6, from Eq. (2-55) and for the y’s from Eq. (2-11) we
obtain
2/€1 - bo/ mr
sin Be = jae (2-58)
wi/w2 - Be/ pa
as the angle at which no reflection occurs. This does not always have a
real solution for @;. In fact,
sin 0; -> &
mira
For nonmagnetic dielectrics (ui = we = fo) there is no angle of total
transmission when E is parallel to the boundary. For the case of H
parallel to the boundary, we find from Eq. (2-57) that T = 0 when
€/€. - jlo/,
sin 0; = (ae -hark (2-59)
€,/€, - €1/€2
Again this does not always have a real solution for arbitrary u» and e.
But in the nonmagnetic case
. €2 Ey
8; = sin ,/-~- = tan, |- 2-60)
om de + €: ee AE ( )
There is usually an angle of total transmission when H is parallel to the
boundary. The angle specified by Eq. (2-60) is called the polarizing angle
or Brewster angle. If an arbitrarily polarized wave is incident upon a
nonmagnetic boundary at this angle, the reflected wave will be polarized
with E parallel to the boundary.

The case of total reflection occurs when |f'| = 1. We are considering
lossless media; so the 7’s are real. It is apparent from Eqs. (2-56) and
(2-57) that |I'| # 1 for real values of 6; and @. However, when e141 >
242, Eq. (2-55) says that sin @ can be greater than unity. What does
this mean? Our initial assumption was that the transmitted wave was
a uniform plane wave. But Eqs. (2-50) specify a solution to Maxwell’s
equations regardless of the value of sin It can be real or complex.
All that is changed: is our interpretation of the field. To illustrate, sup

60 TIME-HARMONIC ELECTROMAGNETIC FIELDS
pose sin - > 1 in Eqs. (2-50) and let
ksint = 86
koost =k V1 - sin? - = +ja (2-61)
If we choose the minus sign for a, Eqs. (2-50) become
E, = Eve7iue-o*
w= - (u,2% 4 y,8) Be eitvern (2-62)
k k} 9
which is a field exponentially attenuated in the z direction. Note the
_ 90° phase difference between FE, and H,; so the wave impedance in the z
direction is imaginary, and there is no power flow in the z direction. A
similar interpretation applies to Eqs. (2-52) when sin' > 1. Returning
now to our reflection problem, from Eq. (2-55) it is evident that sin 6,
is greater than unity when sin 0; > ~/e2u2/'1. Thus, the point of transition from real values of 6 (wave impedance real in region 2) to imaginary
values of @ (wave impedance imaginary in region 2) is
sin 8; = {# (2-63)
€1M1
The angle specified by Eq. (2-63) is called the critical angle. A wave
incident upon the boundary at an angle equal to or greater than the
critical angle will be totally reflected. Note that there is a real critical
angle only if ei: > e2u2 or, in the nonmagnetic case, if c. > €2. Thus,
total reflection occurs only if the wave passes from a ‘‘dense” material
into a “less dense”? material. The reflection coefficient, Eq. (2-56) or
Eq. (2-57), becomes of the form
po k-ix
~ R+ GX
when total reflection occurs. It is evident in this case that |I'| is unity.
Remember that the field in region 2 is not zero when total reflection
occurs. It is an exponentially decaying field, called a reactive field or an
evanescent field. Optical prisms make use of the phenomenon of total
reflection. /
All the theory of this section can be applied to dissipative media if the
7’s and 6’s are allowed to be complex. Of particular interest is the case
: of a plane wave incident upon a good conductor at an angle 6;. When
region 1 is a nonmagnetic dielectric and region 2 is a nonmagnetic conductor, Eq. (2-55) becomes
sins _ hy. five
sin @; ke a

INTRODUCTION TO WAVES 61
T I+dI
, R ‘
N+ + |
bv Vveav \
| | |»
1 \ he dz -- "dz --}
(2) (6)
*Fig. 2-14. A transmission line according to circuit concepts. (a) Physical line; (b)*
equivalent circuit.
This is an extremely small quantity for good conductors. For most practical purposes, the wave can be considered to propagate normally into the
conductor regardless of the angle of incidence.

## Section 2-6: Transmission-line Concepts
 Let us review the circuit concept
of a transmission line and then show its felationship to the field concept.
Let *Fig. 2-14a represent a two-conductor transmission line. For each*
incremental length of line dz there is a series voltage drop dV and a shunt
current dJ. The circuit theory postulate is that the voltage drop is
proportional to the line current J. Thus,

dV = -IZ dz
where Z is a series impedance per unit length. It is also postulated that
the shunt current is proportional to the line voltage V. Thus,
dI = -VY dz
where Y is a shunt admittance per unit length. Dividing by dz, we have
the a-c transmission-line equations
dV dl
ae = = -64
i IZ Zz VY (2-64)
Implicit in this development are the assumptions that (1) no mutual
impedance exists between incremental sections of line and (2) the shunt
current dJ flows in planes transverse to z. The transmission line is said
to be uniform if Z and Y are independent of z.
Taking the derivative of the first of Eqs. (2-64) and substituting from
the second, we obtain .
ay at
qe ~ 2YV =0 a ~ 2Y1=0 (2-65)
c
which are one-dimensional Helmholtz equations. The general solution

62 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TaBLE 2-2. COMPARISON OF TRANSMISSION-LINE WAVES
to UnirormM PLanE Waves
Transmission line | Uniform plane wave
av @E,
oy = “= + BE, =0
am” v=0 dat +
a @H,
Oe yp = Oe on =
aa 7 v= 0 | Gat Hy = 0
y= VEY | jk=V09
V = Vote + Vore?* | E, = Ey*te-ik® + By-eikt
IT = Inte" + ye | Hy = Hote-i** + Ho-eike
7a ¥t_ ve fe Be. ft
a a a
P=VI* | S, = B,H*
is a sum of a +z traveling wave and a -z traveling wave, with propagation constant ~s
y= VZY (2-66)
Choosing the +z traveling wave
Vr = Voe-? It = Iye-?®
we have from Eqs. (2-64) that
V2 7
roy Y¥
Substituting for y from Eq. (2-66), we have
vt Z
2 = ve = V2 (2-67)
which is called the characteristic impedance of the transmission line. The
imaginary parts of Z and Y are usually positive, and it is common practice
to write
Z=R+ jol Y =G@ + jo? (2-68)
The equivalent circuit of the transmission line is then as shown in *Fig.
2-14b. The reader has probably already noted the complete analogy*
between the linearly polarized plane wave and the transmission line.
This analogy is summarized by Table 2-2.
In the circuit theory development, we assumed no mutual coupling

INTRODUCTION TO WAVES 63
between adjacent elements of the transmission line. From the field
theory point of view, this is equivalent to assuming that rio E, or Hz
exists. Such a wave is called transverse electromagnetic, abbreviated
TEM. This is not the only wave possible on a transmission line, for
Maxwell’s equations show that infinitely many wave types can exist.
Each possible wave is called a mode, and a TEM wave is cated a transmission-line mode. All other waves, which must have an F, or an H,
or both, are called higher-order modes. The higher-order modes are
usually important only in the vicinity of the feed point, or in the vicinity
of a discontinuity on the line. In this section we shall restrict consideration to transmission-line, or TEM, modes.

For the TEM mode to exist exactly, the conductors must be perfect,
or else an E, is required to support the z-directed current. Let us therefore specialize the problem to that of perfect conductors immersed in a
homogeneous medium. We assume E, = H, = 0 and z dependence of
the form e, Expansion of the field equations, Eqs. (2-1), then gives

yEy=-#H, Hy = GE
yEz = 2H, yH. = -§Ey
aE, _ aE. _ 4 aH, _ 2H: _ 4
Ox oy ox oy
It follows from these equations that
y = jk (2-69)
The propagation constant of any TEM wave is the intrinsic propagation
constant of the medium. The proportionality of components of E to
those of H expressed by the above equations can be written concisely as
E=HXu, H=2u.xE (2-70)
Thus, the z-directed wave impedance of any TEM wave is the intrinsic
wave impedance of the medium. Finally, manipulation of the original six
equations shows that each component of E and H satisfies the twodimensional Laplace equation. We can summarize this by defining a
transverse Laplacian operator
we yw 2-71
o> 978 + ay? (2-71)
and writing VZE = 0 V7H = 0
The boundary conditions for the problem are *
E,=0
+ Hy, =0 at the conductors (2-72)
Thus, the boundary-value problem for E is the same as the electrostatic

64 TIME-HARMONIC ELECTROMAGNETIC FIELDS
oO problem having the sameconducting boundaries. The
/ Ay boundary-value problem for H is the same as the mag\ Q@ )2 netostatic problem having “anticonducting” (no H_)
Sat we, boundaries. It is for this reason that “static” capaci| tances and inductances can be used for transmission
[ce lines even though the field is time-harmonic.
[ To show the relationship of the static L’s an'1 C’s to
the Z, of the transmission line, consider a cross section
“A of the line as represented by *Fig. 2-15. In the transmission-line problem, the line voltage and current are*
Pre. 215. Gross related to the fields by
mission line.
vaf,B-a T= [.,H#-a (2-73)
where C, and C, are as shown on *Fig. 2-15. From the second of these and*
the second of Eqs. (2-70) we have
=i wx Baa 2 f E, dl
SCs n JC:
But in the corresponding electrostatic problem the capacitance is
c=f=5] Ba
VV Je
Thus, the characteristic impedance of the transmission line is related to
the electrostatic capacitance per unit length by
4
Z= To 1G (2-74)
Similarly, from the first of Eqs. (2-73) and (2-70) we have
V= 1 [#1 x u-dl =1f,,Hadl
In the corresponding magnetostatic problem we have
=¥a#
L= T= T Jo H,dl
Therefore, the characteristic impedance of the line is related to the
magnetostatic inductance per unit length by
4 L
Zo= TA7 (2-75)
Note also that L and C are related to each other through Eqs. (2-74) and
(2-75). The electrostatic and magnetostatic problems heve E and H
everywhere orthogonal to each other and are ca'led conjugate problems.

INTRODUCTION TO WAVES 65
TasLe 2-3. CHARACTERISTIC IMPEDANCES OF SoME Common TRANSMISSION LINES
Line Geometry Characteristic impedance
oiete 2D
Two wire e Q Zo~ log D a
kD " da
Va
Y c b
i Y A Yo = lop 2
Coaxial 3 y Zo oe log =
y
Pe, J
oe q Com Y _2, b+ Vere
Confocal elliptic Zo= oe log = Sued
inate %
few ->| b
Parallel plate cb Zo 1- w>db
eas w
Coli k-D- 1, 4D
‘ollinear plate = A |Z ~7bg- Dw
Awe 7 w
+
Wire above ground plane h OF Zoe log a h>d
d Qn d
ZZ
odky ” ‘2s D2 - s? D>d
Shielded pai j Z a2 sae
cael ” Go J 2 ~ Tl8\G Dts a>d
+% = h
a | ee ” 4w ah >d
w a - Wire in trough FV Aen Zo = a log (2 tanh *) w>d
Once the electrostatic C or the magnetostatic L is known, the Zo of the
corresponding transmission line is given by Eq. (2-74) or Eq. (2-75). Table
2-3 lists the characteristic impedances of some common transmission lines.
When the dielectric is lossy but the conductors still assumed perfect,
all of our equations still apply. Zo (proportional to 7) and y “(a

66 TIME-HARMONIC ELECTROMAGNETIC FIELDS
become complex. The most important effect of this is that the wave is
attenuated in the direction of travel. The attenuation constant in this
case is the intrinsic attenuation constant of the dielectric (Table 2-1,
column 2, row 4). When the conductors are imperfect, the field is no
longer exactly TEM, and exact solutions are usually impractical. However, the waves will still be characterized by a propagation constant
y= a+ jB. Hence a +2z-traveling wave will be of the form
, 4
= Ver tatibe T=4 0 Z,
and the power flow is given by
2
P,=VI* = Vel e724 = Pye-2az
zy
or, in terms of time-average powers,
@, = Re (Py) = Re (Po)e7?*
The rate of decrease in @, versus z equals the time-average power dissipated per unit length ®,, or
- d®,
Ca = - or = 2a,
Thus, the attenuation constant is given by
_ 8a
«= 25, (2-76)
While this equation is exact if ®, and @, are determined exactly, its
greatest use lies in approximating a by approximating @z. For example,
attenuation due to losses in imperfect conductors can be approximated by
assuming that Eq. (2-42) holds at their surface. We shall carry out
such a calculation for the rectangular waveguide in the next section.

## Section 2-7: Waveguide Concepts
 The
x % waves on a transmission line can be
viewed as being guided by the conductors. This concept of wave guidance is quite general and applies to
many configurations of matter. In
> general, systems which guide waves
are called waveguides. Apart from
transmission lines, the most commonly used waveguide is the rectanb Y - gular waveguide, illustrated by Fig.
Fie. 2-16. The rectangular waveguide. 2-16. It is a hollow conducting tube

INTRODUCTION TO WAVES 67
of rectangular cross section. Fieldsexisting within this tube must be characterized by zero tangential components of E at the conducting walls.

Consider two uniform plane waves traveling at the angles - and -£
with respect to the zz plane (see *Fig. 2-12). If the waves are x-polarized,*
we use Eq. (2-50) and write &

Ez, = A(enitusint - exkw sin £) @rik2 000 &

= -2jA sin (ky sin §) en tke con
Let Eo denote (-2jA) and define

k, = ksin & y = jkoost .

In view of the trigonometric identity sin’ £ + cos? £ = 1, the parameters
y and k, are related by
y= he - k (2-77)
The above field can now be written as ,
EB, = Eqsin (key) -% (2-78)
Let us see if this field can exist within the rectangular waveguide. There
is only an Z,; so no component of E is tangential to the conductors z = 0
andz =a. Also, E, = 0 at y = 0;so there is no tangential component
of E at the wall y =0. There remains the condition that E, = 0 at
y = 6, which is satisfied if
=F n=1,2,3,... (2-79)
These permissible values of k, are called eigenvalues, or characteristic
values of the problem.

Each choice of n in Eq. (2-79) determines a possible field, or mode.
The modes in a waveguide are usually classified according to the existence
of z components of the field. A mode having no E, is said to be a transverse electric (TE) mode. One having no H, is said to be a transverse
magnetic (TM) mode. All the modes in the rectangular waveguide fall
into one of these two classes. The modes represented by Eqs. (2-78)
and (2-79) have no E, and are therefore TE modes. The particular modes
that we are considering are TEon modes, the subscript 0 denoting no
variation with z, and the subscript n denoting the choice by Eq. (2-79).
The complete system of modes will be considered in Sec. 4-3.

For k real (loss-free dielectric), the propagation constant y can be
expressed as ‘

z ne
‘ 3 n
iio - (%) k> >
v= , (2-80)
ne
“w= \(<) = k< >

68 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where wand Bare real. This follows from Eqs. (2-77) and (2-79). When
y = jB, we have wave propagation in the z direction, and the mode is
called a propagating mode. When y = a, the field decays exponentially
with z, and there is no wave propagation. In this case, the mode is
called a nonpropagating mode, or an evanescent mode. The transition
from one type of behavior to the other occurs at a = 0 or k = nr/b.
Letting k = 2nf ~/eu, we can solve for the transition frequency, obtaining
eK 2-81
fe = 2b Ven cc mM )
This is called the cutoff frequency of the TEo, mode. The corresponding
intrinsic wavelength
2b
re = a (2-82)
is called the cutoff wavelength of the TEo, mode. At frequencies greater
than f. (wavelengths less than \.), the mode propagates. At frequencies
less than f, (wavelengths greater than \.), the mode is nonpropagating.
A knowledge of f, or \< is equivalent to a knowledge of k.; so they also
are eigenvalues. In particular, from Eqs. (2-79), (2-81), and (2-82), it is
evident that
he = OF = Onfe Ven (2-83)
Using the last equality and k = 2xf ~/eu in Eq. (2-80), we can express 7
as
fe 2
je = jk 1- (6) f>fe
y= 5 (2-84)
w=hyi-(£) f<h
Thus, the phase constant 6 of a propagating mode is always less than the
intrinsic phase constant k of the dielectric, approaching k as f- ,
The attenuation constant of a nonpropagating mode is always less than
k,, approaching k, as f- 0. When a mode propagates, the concepts of
wavelength and phase velocity can be applied to the mode field as a
whole. Thus, the guide wavelength i, is defined as the distance in which
the phase of £ increases by 27, that is, BA, = 27. Using 6 from Eq.
: (2-84), we have
»
y= oo 2-85
"= Vi Gane 289)
showing that the guide wavelength is always greater than the intrinsic
wavelength of the dielectric. The guide phase velocity v, is defined as the

INTRODUCTION TO WAVES 69
velocity at which a point of constant phase of § travels. Thus, in a
manner analogous to that used to derive Eq. (2-14), we find
w Up
v,=e2e= --4 2-86
*- E> Vi- Gp 286)
where 0, is the intrinsic phase velocity of the dielectric. The Bye phase
velocity is therefore greater than the intrinsic phase velocity. >

Another important property of waveguide modes is the existence of a
characteristic wave impedance. To show this, let us find H from the E of
Eq. (2-78) according to V X E = -jwuH. The result is

E, = Egsin (ky) e~?
= 2 Bs 1 ;
Hy jon Eosin (ky) e (2-87)
H, = Be Eo cos (key) e~*
Jou
where FE, has been repeated for convenience. The wave impedance in
the z direction is
E, jup
4.55 = 2-88
Hy, ¥ (2-88)
This is called the characteristic impedance of the mode and plays the
same role in reflection problems as does the Zo of transmission lines. If
we substitute into the above equation for y from Eq. (2-84), we find
1
---SS== l>kh
_- 2
Z=4,= i ae (2-89)
a
V(/f? = 1 .
Thus, the characteristic impedance of a TEon propagating mode is always
greater than the intrinsic impedance of the dielectric, approaching 7 as
f- ©. The characteristic impedance of a nonpropagating mode is
reactive and approaches zero as f > 0.

All our discussion so far has dealt with waves traveling in the +z
direction. For each +z traveling wave, a -z traveling wave is possible,
obtained by replacing y by -y in Eqs. (2-87). The simultaneous
existence of +z and -z traveling waves in the same mode gives rise to
standing waves. The concepts of reflection coefficients, standing-wave
ratios, etc., used in the case of uniform plane-wave reflection, also apply
to waveguide problems. .

The mode with the lowest cutoff frequency in a particular guide is
called the dominant mode. The dominant mode in a rectangular waveguide, assuming b > a, is the TEo: mode. (This we have not shown, for

70 TIME-HARMONIC ELECTROMAGNETIC FIELDS
y| y|
PTET | Siig sees , pan eee
Pititgl *: aT goes ‘3 be me NV
Fe 2) x behch (x ey ply ( 0) pe dixt («
poet 7 Ne LAN PRN
2 ANN ols APE
ee ee ee
x Zz
E-----_-> Lines into paper x x x
H------- > Lines out of paper + + «
*Fig. 2-17. Mode pattern for the TEo: waveguide mode.*
we have not considered all modes.) From Eq. (2-82) with n = 1, we
see that the cutoff wavelength of the TEo: mode is A, = 2b. Thus, wave
propagation can take place in a rectangular waveguide only when its
widest side is greater than a half-wavelength.! A sketch of the instantaneous field lines at some instant is called a mode pattern. The mode
pattern of the TE»: mode in the propagating state is shown in *Fig. 2-17.
This figure is obtained by determining & and # from the E and H of*
Eqs. (2-87) and specializing the result to some instant of time. As time
progresses, the mode pattern moves in the z direction.

It is admittedly confusing to learn that many modes exist on a given
guiding system. It is not, however, so bad as it seems at first. If only
one mode propagates in a waveguide, this will be the only mode of
appreciable magnitude except near sources or discontinuities. The
rectangular waveguide is usually operated so that only the TE»: mode
propagates. This is therefore the only wave of significant amplitude
along the guide except near sources and discontinuities.

Because of the importance of the TE», mode, let us consider it in a
little more detail. Table 2-4 specializes our preceding equations to this
mode and includes some additional parameters which we shall now
consider.

The power transmitted along the waveguide can be found by integrating the axial component of the Poynting vector over a guide cross section.
This gives

P,= [° [? Bunt de dy = |B? ©

t= Jy Jy Uety y 0 az
which, above cutoff, is real and is therefore the time-average power transmitted. Below cutoff, the power is imaginary, indicating no time-average

1 We are referring to the intrinsic wavelength of the dielectric filling the waveguide,
which is usually free space.

. INTRODUCTION TO WAVES 71
TasiE 2-4. Summary OF WAVEGUIDE PARAMETERS FOR THE DoMINANT MopE
(TEn) in a RecrancuLtaR WAVEGUIDE
E, = Ey sin ” ew
Complex field H, = 28 sin TY e- &
Zo b
Eofe mY
H, = - - cos - e~?*
inf b
Cutoff frequency fe 1
2b Ven
Cutoff wavelength Ae = 2b
P . iB =jkV1i-(h/f? fF >fe
ropagation constant 72%, 2. _--aa SVI~ fe? I<
Characteristic impedance Zo _ jee = | WAV 1 - (f/f)? [oh
7 JUV (f/f)? -1) of <fe
N
Guide wavelength = -_[___| "WI = /f)
Guide phase velocity Bp = es
Vi = if)?
Power transmitted P= |Bol?ab
2Zo
Attenuation due to lossy dielectric | ay) = “ aWV1 - (f/f)?
2
Attenuation due to imperfect conductor ae = ___*____-~ [: + 2a (£) |
an V1 - (f/f)? aM,
power transmitted. (The preceding equation applies only at z = 0 below
cutoff unless the factor e~**7 is added.) _ It is also interesting to note that
the time-average electric and magnetic energies. per unit length of guide
are equal above cutoff (see Prob. 2-32). .

In contrast to the transmission-line mode, there is no unique voltage
and current associated with a waveguide mode. However, the amplitude
of a modal traveling wave (Eoin Table 2-4) enters into waveguide reflection problems in the same manner as V in transmission-line problems.

72 TIME-HARMONIC ELECTROMAGNETIC FIELDS
To emphasize this correspondence, it is common to define a mode voltage V
and a mode current I such that
4 *
Zo = T P=VI (2-90)
From Table 2-4, it is evident that
lab _vV
Vn Be feer T=7 (2-91)
satisfy this definition. Remember that we are dealing with only a +z
traveling wave. In the -z traveling wave, ] = -V/Z». When waves
in both directions are present, the ratio V/J is a function of z. Other
definitions of mode voltage, mode current, and characteristic impedance
can be found in the literature. These alternative definitions will always
be proportional to our definitions (see Prob. 2-34).

Our treatment has so far been confined to the ideal loss-free guide.
When losses are present in the dielectric but not in the conductor, all
our equations still apply, except that most parameters become complex.
There is no longer a real cutoff frequency, for y never goes to zero. Also,
the characteristic impedance is complex at allfrequencies. The behavior
of y = a + jf in the low-loss case is sketched in *Fig. 2-18. The behavior*
of y for the loss-free case is shown dashed. The most important effect
of dissipation is the existence of an attenuation constant at all frequencies.
In the low-loss case, we can continue to use the relationship

< ts He fe)?
y= at j6 ~jkail - Ff
provided f is not too close to f.. Letting k = k’ - jk’’ and referring to
jh
. *Fig. 2-18. Propagation*
constant for a lossy waveguide (loss-free case
k, a
€ B shown dashed).
(0) ke f

INTRODUCTION TO WAVES 73
Table 2-1, we find
a 2
aa DB (£) (2-92)
2 €
This is the attenuation constant due to a lossy dielectric in guide.
Even more important is the attenuation due to imperfectly
guide walls. Our solution is no longer exact in this case, because the
boundary conditions are changed. The tangential component of E is
now not quite zero at the conductor. However, for good conductors, the
tangential component of E is very small, and the field is only slightly
changed, or “perturbed,” from the loss-free solution. The loss-free
solution is used to approximate H at the conductor, and Eq. (2-42) is
used to approximate the power dissipated in the conductor. Such a
procedure is called a perturbational method (see Chap. 7). The power per
unit length dissipated in the wall y = 0 is
@
~ ‘a XN f\ [+
6,| =a f lH, |? de = azar (4) f dx
ye 0 af} Jo
nara(S)
=R a { 2
\Bera (4)
and an equal amountis dissipated in the wall y = b. The power per unit
length dissipated in the wall z = 0 is
_ b
Bal = [Cite + LEP) ay
° | sin? (wy/b) fe\? on TY
= 2 = zoe
R| El ip [ Zi + at) °° > dy
b f.\? b
= 247 oy) =
azo [a7 + (4) 5]
and an equal amount is dissipated in the wall z = a. The total power
dissipated per unit length is the sum of that for the four walls, or
be = alBl?| 2, + (ZY (20 + »|
Zo \nf,
Equation (2-76) is valid for any traveling wave; so using the above a,
and @, = P of Table 2-4, we have
_ AZo[ 6 f.\? .
a = Gel 2+ (4) (2a +b)
a 2a (/f.\?
-avituml'**Q)] 28
+ a V1- C/I) | oV
This is the attenuation constant due to conductor losses. When both

74 TIME-HARMONIC ELECTROMAGNETIC FIELDS
x dielectric losses and conductor losses
need to be considered, the total
attenuation constant is
Z = 0g te es (2-94)
for by Eq. (2-76) we merely add the
two losses.
2-8, Resonator Concepts. In Sec
a Wena 2-2 we noted a similarity between
yee standing waves and circuit theory
yt resonance. Intheloss-free case, eleca tromagnetic fields can exist within
b Y a source-free region enclosed by a
Fia. 2:19. The rectangular cavity. perfect conductor. These fields can
exist only at specific frequencies,
called resonant frequencies. When losses are present, a source must
exist to sustain oscillations. The input impedance seen by the source
behaves, in the vicinity of a resonant frequency, like the impedance of an
LC circuit. Resonators can therefore be used for the same purposes at
high frequencies as LC resonators are used at lower frequencies.

To illustrate resonator concepts, consider the “rectangular cavity”
of *Fig. 2-19. This consists of a conductor enclosing a dielectric, both of*
which we will assume to be perfect at present. We desire to find solutions to the field equations having zero tangential components of E over
the entire boundary. The TE»; waveguide mode already satisfies this
condition over four of the walls. We recall that standing waves have
planes of zero field, which suggests trying the standing-wave TEp: field.
For E, to be zero at z = 0, we choose

E, = EB, +E, = Asin Zw - cif)
= E, sin (2) sin Bz
For E, to be zero at z = c, we choose Bc = z, which, according to Table
2-4, is
p 1
wr=ck,J1-(F = of Ver sf - 5
J ' ) (2b ~/eu f)?
Solving for the resonant frequency f = f,, we have
1 jet+e
= pee 2-95
f 2be on ( )
When a is the smallest cavity dimension, this is the resonant frequency of

INTRODUCTION TO WAVES 75
the dominant mode, called the TE ;: mode. The additional subscript 1
indicates that we have chosen the first zero of sin 6z. The higher zeros
give higher-order modes, that is, modes with higher resonant frequencies.
Setting 8 = 7/c in the above expression for E, and determining H from the
Maxwell equations, we have for the TE»1: mode &
E. = Eysin 4 sin
b c
WvEy . Ty cra
WV, = -4==-= sin = cos - 2-96
iver b c (2-96)
H,=-- __JeBo cos = sin 7% :
avVbete? b c
Note that E and H are 90° out of phase; so & is maximum when & is
minimum and vice versa. A sketch of the instantaneous field lines at some
time when both & and & exist is given jn *Fig. 2-20. Also of interest is*
the energy stored within the cavity. From the conservation of complex
power, Eq. (1-68), we know that W,, = W.. Thus, the time-average
electric and magnetic energies are
v,=B=5 [ff |EP dr = ; | Eo)2abe (2-97)
* cavity
We also know from conservation of energy, Eq. (1-39), that the total
energy within the resonator is independent of time. If we choose a time
for which 3 is zero, W,, will be zero, and W. will be maximum and twice
its average value. Therefore,
w = 20, = i |E|?abe (2-98)
is the total energy stored within the cavity.
x xX xX >
KX KK a -=~\
Kx KK 1 Vor P a NY
phos gos Vy
> b ple le eee ef el
pl wet. Jd H
ar At [\ Ss-~<---4 } H
o7ce \S~-- 4 --- /
tee hc NDT Tore
hay _--E---__> K---> *Fig. 2-20. Mode pattern for the TEo: cavity mode.*

76 TIME-HARMONIC ELECTROMAGNETIC FIELDS
When the resonator has losses, we define its quality factor as
_ w X energy stored _ oW
Q= average power dissipated a (2-99)
by analogy to the Q of an LC circuit. If the losses are dielectric losses,
we have
we fff \EPdr gs
Q=-4 = 5 (2-100)
wel! fff |E/}dr
so the Q of the resonator is that of the dielectric, Eq. (1-79). This is
valid for any mode in a cavity of arbitrary shape. Usually more important in determining the Q is the loss due to imperfect conductors. This
is determined to the same approximation as we used for waveguide
attenuation. We assume H at walls to be that of the loss-free mode
and calculate @; by Eq. (2-42). To summarize,
= Q|E,|?
= 2 = 2 2 3 3
G1 =A $ HI ds = aarp 4 gx lbe(* + *) + 2a(b* + 8]
valle,
Substituting this, Eq. (2-98), and Eq. (2-95) into Eq. (2-99), we have
_7 a(b? + c?)%
Qe = D6 BoE cD HF Dad? + A) (2-101)
From the symmetry of Q. in b and c, it is evident that b = c for maximum Q. For a “‘square-base’”’ cavity (b = c), we have
1 1.11y
_ __ . = - 2-102
f bV/2en Q (1 + b/2a) ( )
The Q also increases as a increases, but if a > b we no longer have the
dominant mode. As an example of the Q’s obtainable, consider a cubic
cavity constructed of copper. In this case we have
Q. = 1,07 X 10°/+/f (2-103)
which, at microwave frequencies, gives Q’s of several thousand. This
idealized Q will, however, be lowered in practice by the introduction of a
feed system, by imperfections in the construction, and by corrosion of
the metal. When both conductor losses and dielectric losses are considered, the Q of the cavity becomes
1 1 1
zEeats 2-104
0° ate (2-104)
which is evident from Eq. (2-99).

INTRODUCTION TO WAVES 77

## Section 2-9: Radiation
 We shall now show that a source in unbounded space
is characterized by a radiation of energy. Consider the field equations
V XE = -jopH VX H = jwE + J (2-105)
where J is the source, or impressed, current. These equations apply
explicitly to a perfect dielectric, but the extension to loss media is
effected by replacing jwn by 2 and jwe by g. In homogeneous media,
the divergence of the first equation is
v-H=0
Any divergenceless vector is the curl of some other vector; so.
H=vVXA (2-106) ~
where A is called a magnetic vector potential.1 Substituting Eq. (2-106)
into the first of Eqs. (2-105), we have
Vv xX (E+ joy) = 0
Any curl-free vector is the gradient of some scalar. Hence,
E + jopA = -VO (2-107)
where ® is an electric scalar potential. To obtain the equation for A,
substitute Eqs. (2-106) and (2-107) into the second of Eqs. (2-105).
This gives
VXVXA-K?A = J - jueVb (2-108)
which, by a vector identity, becomes
v(vV-A) -VA- KA = J - jueVb
Only V x A was specified by Eq. (2-106). We are still free to choose
v-A. If we let
V-A = -jweh (2-109)
the equation for A simplifies to
VA+ KA = -J (2-110)
This is the Helmholtz equation, or complex wave equation. Solutions
to Eq. (2-110) are called wave potentials. In terms of the magnetic wave
potential, we have
. 1
E = -jopA + joe v(V-A) (2-111)
H=VXxA
1In general electromagnetic theory it is more common to let A be the vector potential of B. In homogeneous media the two potentials are in the ratio », a constant.

78 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Z obtained from Eqs. (2-106), (2-107),
and (2-109). The principal advantages of using A instead of E or H
are (1) rectangular components of A
r have corresponding rectangular components of J as their sources and (2)
6 .
A need not be divergenceless.
Let us first determine A for a curIl rent J extending over an incremental
% ¥ length J, forming a current element or
electric dipole of moment Jl. Take
*Fig. 2-21. A z-directed current element this current element to be z-directed*
at the coordinate origin. and situated at the coordinate origin,
as shown in *Fig. 2-21. The current*
is z-directed; so we take A to have only a z component, satisfying
WA. + hA, =0
everywhere except at the origin. The scalar quantity A, has a point
source IZ and should therefore be spherically symmetric. Thus, let
A, = A,(r), and the above equation reduces to
1d dA,
oF fees 24 =
ser i) + A, 9
This has the two independent solutions
1 ear 1 eskr
Tr Tr
the first of which represents an outward-traveling wave, and the second
an inward-traveling wave. (In dissipative media, k = k’ - jk’, and the
first solution vanishes as r- o, and the second solution becomes
infinite.) We therefore choose the first solution, and take
A, = c en akr
T
where C is a constant.1 As k->0, Eq. (2-110) reduces to Poisson’s
equation, for which the solution is
Il
Aa Gr
1To be precise, C might be a function of k, but the solution must also reduce to
the static field asr- 0. Hence, C is not a function of k.

INTRODUCTION TO WAVES 79
Our constant C must therefore be
Il
CO" &
and hence A, = au ew ahr (2-112)
* 4ar
is the desired solution for the current element of *Fig. 2-21. A. outward-traveling wave represented by Eq. (2-112) is called a spherical wave,*
since surfaces of constant phase are spheres.
The electromagnetic field of the current element is obtained by substituting Eq. (2-112) into Eqs. (2-111). The result is
aH (143 ,
E, = ae I (3 i) cos @
By = bm (Toe 2 1) ing (2-113)
4a r r? © Jwer®
_Il 4, (ik 1
Hs =e (F+3 sih 0
Very close to the current element, the E reduces to that of a static charge
dipole, the H reduces to that of a constant current element, and the field
is said to be quasi-static. Far from the current element, Eqs. (2-113)
reduce to
Es=1 TE eae sin 6
jl r>aA (2-114)
a LT ek gj
As nr ° mr sin @
which is called the radiation field. At intermediate values of r the field is
called the induction field. The outward-directed complex power over a
sphere of radius r is
Qe ” :
P, = fp x H*-ds = i ae f dor? sin 0 EyHt
_ elle fl, oF _
= | [} oa (2-115)
The time-average power radiated is the real part of Py, or
x, Qn | Il |?
=yqale 2-116
P= zy | x | ( )
This is independent of r and can be most simply obtained from the radiation field, Eq. (2-114). The reactive power, which is negative, indicates
that there is an excess of electric energy over magnetic energy in the
near field. e

80 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz
r-r .
(x,y1.2') (x,y,2) *Fig. 2-22. Radius vector notation.*
r
¥
x
To obtain the field of an arbitrary distribution of electric currents,
we need only superimpose the solutions for each element, for the equations are linear. A superposition of vector potentials is usually the most
convenient one. For this purpose, we shall use the radius vector notation
illustrated by *Fig. 2-22. The “field coordinates” are specified by*
r=uz+ wy + uz
and the “‘source coordinates” by
r= ut’ + uy’ + wz’
In Eq. (2-112), 7 is the distance from the source to the field point. For
Ii not at the coordinate origin, r should be replaced by
Se ner rner ener TEETER
kor =V@--2 FUP tee)
Note the direction of the vector potential is that of the current; so Eq.
(2-112) can be generalized to a current element of arbitrary orientation
by replacing Il by Jl and A, by A. Thus, the vector potential from
current element of arbitrary location and orientation is
Tl e~#Flt-#'1
A= 4n|r - 1]
To emphasize that A is evaluated at the field point (z,y,z) and [1 is situated at the source point (2’,y’,z’), we shall use the notation A(r) and
I(r’). The above equation then becomes
I(r" ee
AC) = er =F (2-117)
Finally, for a current distribution J, the current element contained in a
volume element dr is J dr, and a superposition over all such elements is
1 Jere,
A(t) = z fff a dr (2-118)

INTRODUCTION TO WAVES 81
The prime on dr’ emphasizes that the integration is over the source
coordinates. Equation (2-118) is called the magnetic vector potential integral. It is intended to include the cases of surface currents and filamentary currents by implication. We therefore have a formal solution
for any problem characterized by electric currents in an pnboundelghomegeneous medium. The medium may be dissipative if k is considered to
be complex.

## Section 2-10: Antenna Concepts
 A device whose primary purpose is to
radiate or receive electromagnetic energy is called an antenna. To illustrate antenna concepts, we shall consider the linear antenna of *Fig. 2-23.
It consists of a straight wire carrying a current J(z). When it is energized at the center, it is called a dipole antenna. The magnetic vector*
potential, Eq. (2-118), for this particular problem is

1), ikle-e'
4-4 [ EAC aaemeier (2-119)
4m Jor \u-t'|
where jr -r'| = Vr? 4 2” - 2rz’ cos 6 (2-120)
The radiation field (r large) is of primary interest, in which case
|r -1'| =r - 2’ cos 6 r>>2’ (2-121)
enkr L/2 ;
and A, ~ - I T(z’ ei?" 2088 dz! r>L (2-122)
4nr } 12
Note that the second term of Eq. (2-121) must be retained in the ‘‘phase
term” e~*'-r'l, but not in the “amplitude term” |r - r’|-!._ To obtain
the field components, substitute Eq. (2-122) into Eqs. (2-111) and retain
only the 1/r terms. This gives
Eo = jou sin 6 A; Zz
Hs -1n, r large wy
(2-123) ip A A
This result is equivalent to superimposing Eqs. (2-114) for all ele- dz’
ments of current.

To evaluate the radiation field,
we must know the current on the
antenna. An exact determination ™ Y
of the current requires the solution y T(z)
to a boundary-value problem. Fortunately, the radiation field is relatively insensitive to minor changes in -L/e
current distribution, and much use- *Fig. 2-23. The linear antenna,*

82 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ful information can be obtained from an approximate current distribution.
We have already seen that on transmission lines the current is a harmonic
function of kz. This is also true for the principal mode on a single thin
wire. The current on the dipole antenna must be zero at the ends of the
wire, symmetrical in z, and continuous at the source (2 = 0). Thus, we
choose
I(z) = I, sin [* (5 - H) (2-124)
The vector potential in the radiation zone can now be evaluated as
a Ine (PP L , jks! cos 8 iz!
A, = ie sin[ e(§ lz ')| ' dz’
L L
Ine" 2 [cos (i 3 008 D) - cos (« ty]
dar k sin? @
From Eq. (2-123), the radiation field is
. _ ay | COS ke cos 0 - cos pe
By = Tne | NBN (2-125)
“e Qrr sin 6
with Hy = Eo/n. Note that the radiation field is linearly polarized, for
there is only an EZ». The density of power radiated is the r component
of the Poynting vector
2
all? cos (ee cos D) - cos (« )
= E,H* = Teel NS _
S, = Eo} Qari dnd (2-126)
The total power radiated is obtained by integrating S, over a large sphere,
or
. Qn fx
6,= f i S, 7? sin 6d dc
0 0
. 2
alZl? [cos (4 eos D) - cos (t ty)
“Se Jo Sin@St™~S a6 (2-127)
The radiation resistance R, of an antenna is defined as
= os
R, = WE (2-128)
where I is some arbitrary reference current. For the dipole antenna,
the reference current is usually picked as J,,. Hence,
7” 2
, [eos ( z cos D) - cos ( tI
R,= ap Jy ine de (2-129)

INTRODUCTION TO WAVES 83
=~ TTT
[||

29) FER EH
Frc, 2-24. Radiation re- 3, 100[- OVNI

sistance of the dipole 120 jks / lA
- SEL NAH
“CALL TEE ETT)
0 /2 » 30/2 2a

L
This integral can be evaluated in terms of tabulated functions (see Prob.
2-44). A graph of R, versus L is given in *Fig. 2-24.

The radiation field pattern of an antenna is a plot of |Z] at constant r*
in the radiation zone. For a dipole antenna, the radiation field pattern
is essentially the bracketed term of Eq. (2-125). This is shown in *Fig.
2-25 for KL small (short dipole), kL = + (half-wavelength dipole), and*
kL = 2x (full-wavelength dipole). The radiation power pattern, defined
as a plot of |S,| at constant r, is an alternative method of showing radiation characteristics. When the radiation field is linearly polarized, as
it is for the dipole antenna, the power pattern is the square of the field
pattern. The gain g of an antenna in a given direction is defined as the
ratio of the power required from an omnidirectional antenna to the power

‘ \
ly £XC' anew, Short dipole
Zorg Lpeox
MILE ow
DCN OEN
aes OW Saree
PARRA oN
4a LR AWREHA TT WN
Geese soem
se S=
NGaee CORARSS THY
NSERC
OSIRIA
SK SHIT SRNL LP
LOD -Oe {/
\y SAK <caaee, nag yA
4
*Fig. 2-25. Radiation field patterns for the dipole antenna.*

84 TIME-HARMONIC ELECTROMAGNETIC FIELDS
required from the actual antenna, assuming equal power densities in the
given direction. Thus,
2,
g(o) = 4277S-(6) (2-130)
Oy
For L < , the maximum gain of a dipole antenna occurs at 6 = 7/2.
From Eqs. (2-126) and (2-128), we have
2 2
altel (1 - cos He) a(1 - cos)
of
g 6) > Oy > rR, (2-131)
In the limit KL - 0, we have g(r/2) = 1.5; so the maximum gain of a
short dipole is 1.5. For a half-wave dipole, we can use *Fig. 2.24 and*
calculate a maximum gain of 1.64. Similarly, for a full-wave dipole,
the maximum gain is 2.41.

The input impedance of an antenna is the impedance seen by the source,
that is, the ratio of the complex terminal voltage to the complex terminal
current. A knowledge of the reactive power, which cannot be obtained
from radiation zone fields, is needed to evaluate the input reactance.
The input resistance accounts for the radiated power (and dissipated
power if losses are present). We define the input resistance of a lossfree antenna as

ee MER / 
R; = var (2-132)
where ®, is the power radiated and J; is the input current. If losses are
present, a ‘‘loss resistance”? must be added to Eq. (2-132) to obtain the
input resistance. For the dipole antenna,

- kL
I; = In sin
and the input resistance is
R,
Ri = SATO (2-133)
In the limit as kL is made small, we find
2
R,= mk Ly" L& (2-134)
24a
The short dipole therefore has a very small input resistance. For example, if L = 4/10, the input resistance is about 2 ohms. For the halfwavelength dipole, we use *Fig. 2-24 and Eq. (2-133) and find*
Ri=R,=731ohms L=) (2-135)

INTRODUCTION TO WAVES 85
For the full-wavelength dipole, Eq. (2-133) shows Rj = ©. This incorrect result is due to our initial choice of current, which has a null at the
source. The input resistance of the full-wavelength dipole is actually
large, but not infinite, and depends markedly on the wire diameter (see
*Fig. 7-13).*

## Section 2-11: On Waves in General
 A complex function of c@grdinates
representing an instantaneous function according to Eq. (1-40) is called a
wave function. A wave function y, which may be either a scalar field or
the component of a vector field, may be expressed as

¥ = A(zy,z)erew (2-136)
where A and @are real. The corresponding instantaneous function is

V2 A(z,y,2) cos [wt + ®(z,y,2)] (2-137)

The magnitude A of the complex function is the rms amplitude of the
instantaneous function. The phase ® of the complex function is the
initial phase of the instantaneous function. Surfaces over which the
phase is constant (instantaneous function vibrates in phase) are called
equiphase surfaces. These are defined by

&(z,y,z) = constant (2-138)
Waves are called plane, cylindrical, or spherical according as their equiphase surfaces are planes, cylinders, or spheres. Waves are called uniform when the amplitude A is constant over the equiphase surfaces.
Perpendiculars to the equiphase surfaces are called wave normals. These
are, of course, in the direction of V@ and are the curves along which the
phase changes most rapidly. :

The rate at which the phase decreases in some direction is called the
phase constant in that direction. (The term phase constant is used even
though it is not, in general, a constant.) For example, the phase constants in the cartesian coordinate directions are

Ob ad ad
Br = - 5 B= - 3, B= ae (2-139)
These may be considered as components of a vector phase constant defined
by
6=---Ve (2-140)
The maximum phase constant is therefore along the wave normal and is
of magnitude |V4]. k

The instantaneous phase of a wave is the argument of the cosine func
tion of Eq. (2-137). A surface of constant phase is defined as
e
wt + (x,y,z) = constant (2-141)

86 TIME-HARMONIC ELECTROMAGNETIC FIELDS
that is, the instantaneous phase is constant. At any instant, the surfaces of constant phase coincide with the equiphase surfaces. As time
increases, ® must decrease to maintain the constancy of Eq. (2-141), and
the surfaces of constant phase move in space. For any increment ds the
change in ® is
Om 6b OP
Vb: =- = + ds qn t+ yy + a @
To keep the instantaneous phase constant for an incremental increase in
time, we must have
wdti+ Vb-ds=0
That is, the total differential of Eq. (2-141) must vanish. The phase
velocity of a wave in a given direction is defined as the velocity of surfaces
of constant phase in that direction. For example, the phase velocities
along cartesian coordinates are
AE
= @b/ax iB,
a w
i Sa e (2-142)
i= =
£ 0b/dz B,
The phase velocity along a wave normal (ds in the direction of -V®) is
w 2)
»D= a] 73 (2-143)
which is the smallest phase velocity forthe wave. Phase velocity is not a
vector quantity.
We can also express the wave function, Eq. (2-136), as
y= eOewey (2-144)
where © is a complex function whose imaginary part is the phase ®.
A vector propagation constant can be defined in terms of the rate of change
of Oas
y= -VO=e+36 (2-145)
where 6 is the phase constant of Eq. (2-140) and a is the vector attenuation constant. The components of a are the logarithmic rates of change
of the magnitude of y in the various directions.
In the electromagnetic field, ratios of components of E to components
of H are called wave impedances. The direction of a wave impedance is
defined according to the right-hand “‘cross-product”’ rule of comvonent E

INTRODUCTION TO WAVES 87
rotated into component H. For example,
E.
Ey _g + =f, (2-146)
H, ¥
is a wave impedance in the +2 direction, while
~ B24, = 2 (2-147)
Hy, ”
is a wave impedance in the -z direction. The wave impedance in the
+2 direction involving F, and Hz is
ae = Dyct = Bye (2-148)
The Poynting vector can be expressed in terms of wave impedances.
For example, the z component is
S, = (BX H*), = Blt - EH?
= Zaj*|H,|? + Syst Hel? (2-149)
The concept of wave impedance is most useful when the wave impedances are constant over equiphase surfaces. .
Let us illustrate the various concepts by specializing them to the unlform plane wave. Consider the z-polarized z-traveling wave in lossy
matter,
E, = Eye*e7**
H, = Eo enh ee ik’
7
The amplitude of E, is Ege-*”* and its phase is -k’z. Equiphase surfaces are defined by -k’z = constant, or, since k! is constant, by 2 = constant. These are planes; so the wave is a plane wave. The amplitude
of E, is constant over each equiphase surface; so the wave 18 uniform.
The wave normals all point in the z direction. The cartesian components of the phase constant are B. = By = 0, B. = k’; so the vector phase
constant is § = u.k’. The phase velocity in the direction of the wave .
normals isv, = w/k’. The cartesian components of the attenuation constant are a, = a, = 0, a =k”; so the vector attenuation constant is
a =u,k’. The vector propagation constant is
y= at 9G = WC" + jk = was
The wave impedance in the z direction is Z, = Zy* = E,/H, = 1- Note
that the various parameters specialized to the uniform plane traveling
wave are all intrifisic parameters. This is, by definition, the meaning of
the word ‘‘intrinsic.””

88 TIME-HARMONIC ELECTROMAGNETIC FIELDS
PROBLEMS
“>
&2-1) Show that E, = Eye~## satisfies Eq. (2-6) but not Eq. (2-5). Show that it
does not satisfy Eq. (2-3). This is not a possible electromagnetic field.
“(2-2 Derive the “wave equations” for inhomogeneous media
VX (2°V XE) +9E=0
Vv X 9 7V XH) + 2H =0
Are these valid for nonisotropic media? Do Eqs. (2-5) hold for inhomogeneous
media?

## Section 2-3: Show that for any lossless nonmagnetic dielectric
k=kVe g= eu
Ve
do c
’\=-= ==
Ve P Ve
where e, is the dielectric constant and ko, 0, do, and c are the intrinsic parameters of
vacuum

- 2-4. Show that the quantities of Eqs. (2-18) satisfy Eq. (1-35). Repeat for Eqs.
(2-21), (2-27), and (2-29).

## Section 2-6: For the field of Eqs
 (2-20), show that the velocity of propagation of energy
as defined by Eq. (2-19) is
pastes sin 2kz sin 2ot < 1
*"Veu 1 = cos 2kz cos 2ut = V7ey

## Section 2-6: For the field of Eqs
 (2-22), show that the phase velocity is
1 f(A+C 4, ,A-C.,
Vp Va GH cos? kz + LEC sin ie)

## Section 2-7: For the field of Eqs
 (2-28), show that the z-directed wave impedances are
E, zs
Zx° = , = -jn tan kz
-E, :
Zu? = a oa = -jn tan kz
Would you expect Zzy+ = Z,.* to be true for all a-c fields?
© 2-8. Given a uniform plane wave traveling in the +z direction, show that the wave
is circularly polarized if
E._ 43
E, +3
being right-handed if the ratio is +j and left-handed if the ratio is -j.

## Section 2-9: Show that the uniform plane traveling wave of Eq
 (2-25) can be expressed as
the sum of a right-hand circularly polarized wave and a left-hand circularly polarized
wave.

## Section 2-10: Show that the uniform plane traveling wave of Eq, (2-25) can be expressed as
E = (E + jEs)e"i*

INTRODUCTION TO WAVES 89
where E; and Ez are real vectors lying in the zy plane
 Relate E, and Ez to A and B.

## Section 2-11: Show that the tip of the arrow representing & for an arbitrary complex E
traces out an ellipse in space
 {Hint: let E = Re (E) + j Im (E) and use the results
of Prob. 2-10.]

## Section 2-12: For the frequencies 10, 100, and 1000 megacycles, determine k = - jk”
and 7 = ® + j&X for (a) polystyrene, Fig
 1-10, (b) Plexiglas, *Fig. 1-11, (c) A,*
*Fig. 1-12, e- = 10, and (d) copper, c = 5.8 X 107.*

o 2-18. Show that when all losses are of the magnetic type (c = «’’ = 0),
at o¥ jk
TS Tl we 7 we

## Section 2-14: Show that for nonmagnetic dielectrics ,
Bozo Vp’ (1 + i

8Q?
el gfe,
wo NEC a)
2 Q>1
a~ Vt (.- )
' 8Q?
eae (r-8
<= 90 Ve C 50)
where Q is defined by Eq. (1-79).

## Section 2-16: Show that for nonmagnetic conductors
aN Q
k 3 (: + 3)
we = a (1-9)
fi o Q«1
~ Affe ~
ax s (Q: + 3)
~ ai 2
t= VE(1 3)
where Q is defined by Eq
 (1-79).

## Section 2-16: Show that for metals
=a0+j) k=ta-j wad
” 7 gud 66
where @ is the surface resistance, 5 is the skin depth, and o is the conductivity

## Section 2-17: Derive the following formulas
& (silver) = 2
52 X 10-7 Vf *
& (copper) = 2.61 X 10-7 Vf
G (gold) = 3.12 X 10-7? V/f
& (aluminum) = 3.26 X 10-7 Vf
# - Q (brass) = 5.01 X 10-7 Vf
where f is the frequency in eycles per second.

90 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 2-18: Find the power per square meter dissipated in a copper sheet if the rms magnetic intensity at its surface is 1 ampere per meter at (a) 60 cycles, (b) 1 megacycle,
(c) 1000 megacycles

## Section 2-19: Make a sketch similar to Fig
 2-6 for a circularly polarized standing wave in
dissipative media. Give a verbal description of & and x.

## Section 2-20: Given a uniform plane wave normally incident upon a plane air-to-dielectric
interface, show that the standing-wave ratio is

SWR = Ve, = index of refraction
where e, is the dielectric constant of the dielectric (assumed nonmagnetic and loss-free)

## Section 2-21: Take the index of refraction of water tobe 9, and calculate the percentage of
power reflected and transmitted when a plane wave is normally incident on a calm lake

## Section 2-22: Calculate the two polarizing angles (internal and external) and the critical
angle for a plane interface between air and (a) water, «, = 81, (b) high-density glass,
«, = 9, and (c) polystyrene, c, = 2
56.

## Section 2-23: Suppose a uniform plane wave in a dielectric just grazes a plane dielectricto-air interface
 Calculate the attenuation constant in the air [a as defined by Eq.
(2-61)] for the three cases of Prob. 2-22. Calculate the distance from the boundary
in which the field is attenuated to 1/e (36.8 per cent) of its value at the boundary.
What is the value of a at the critical angle?

## Section 2-24: From Eqs
 (2-66) and (2-68), show that when R Kwl andG «K wC

a~-R_ ,evile
2VL/C 2
BxewVLC
where y = a + jp.

## Section 2-26: Show that 7 and C of a transmission line are related by
_ we! 4, ad'a
Sarl S Da
when the dielectric Is homogeneous
 Show that F of a transmission line is approximately equal to the d-c resistance per unit length of hollow conductors having thickness 6 (skin depth) provided H is approximately constant over each conductor and the
radius of curvature of the conductors is large compared to 6.

## Section 2-26: Using results of Prob
 2-25, show that for the two-wire line of Table 2-3
Rawk a>
“ad D>d
and that for the coaxial line
Ra+b
R= 2s ab a>s
and that for the parallel-plate line
Rx 2 w>b
w

## Section 2-27: Verify Eqs
 (2-70).

## Section 2-28: Consider a parallel-plate waveguide formed by conductors covering the planes
y =Oandy =
 Show that the field

E,= Bo sin "FY ewe n=1,2,3,...

INTRODUCTION TO WAVES 91
defines a set of TE, modes and the field
Hz = Ho cos “£4 em n=0,1,2,...
defines a set of TM, modes, where

Gl

in both cases. Show that the cutoff frequencies of the TE, and TM, modes are
n
I Va

Show that Eqs. (2-83) to (2-86) apply to the parallel-plate waveguide modes.

## Section 2-29: Show that the power transmitted per unit width (zx direction) of the parallel
plate waveguide of Prob
 2-28 is
DIE dl? . (Fy
Pp = ho 1, - (£
2 f
for the TE, modes, and a
_ blHl?y Vi = (ey
P= -3z- Vi 7
for the TM, modes (n = 0).

## Section 2-30: For the parallel-plate waveguide of Prob
 2-28, show that the attenuation
due to conductor losses is
ae = OF _
“bn V1 = C/E
for the TE, modes, and
2a
a
bn VI - IA?
for the TM, modes (n # 0).

## Section 2-31: Show that the TM» mode of the parallel-plate waveguide as defined in Prob

2-28 is actually a TEM mode. Show that for this mode the attenuation due to conductor losses is

es
Crcseeeie 4
Compare this with a obtained by using the results of Probs. 2-26 and 2-24.

## Section 2-32: For the TEs rectangular waveguide mode, show that the time-average elec
tric and magnetic energies per unit length are
We = Wn = F |Baltab
Can this equality of W, and W, be predicted from Eq
 (1-62)?

## Section 2-33: Show that the time-average velocity of propagstion of energy down a rectangular waveguide is
& im z
n-&- 1 Vi)
c wo Ven J
for the TE: mode

92 TIME-HARMONIC ELECTROMAGNETIC FIELDS :

## Section 2-34: For the TE»: rectangular waveguide mode, define a voltage V as fE+ dl across
the center of the guide and a current J as the total z-directed current in the guide wall
z=0
 Show that these are '

V =aEye-i® [= 2bEo fe
aZo
Show that P # VI*. Why? Define a characteristic impedance Zyr = V/J and
show that it is proportional to Zp of Table 2-4.

## Section 2-36: Let a rectangular waveguide have a discontinuity in dielectric at z = 0,
that is, «1, 41 for z <0 and e:, we for z > 0
 Show that the reflection and transmission coefficients for a TE»: wave incident from z < 0 are

_ Zon - Za _ 2202
"Zab "lat Za
where Zo; and Zoz are the characteristic impedances z < 0 and z > 0, respectively.
These results are valid for any waveguide mode.

## Section 2-36: Show that there is no reflected wave for the TEo: mode in Prob
 2-35 when

Lo fete? = a?)

Ser B2(uier - p2e1)
where fa is the cutoff frequency z <0. Note that we cannot have a reflectionless
interface when both dielectrics are nonmagnetic. This result is valid for any TE
mode.

## Section 2-37: Take a parallel-plate waveguide with e:, 4: for z2 <0 and e:, we for z > 0

Show that there is no reflected wave for a TM mode incident from z < 0 when

Le a[ nets a
Ses ex(eie - enti)
For nonmagnetic dielectrics, this reduces to
fete
Ser @
Compare this to Eq. (2-60). These results are valid for any TM mode.

## Section 2-38: Design a square-base cavity with height one-half the width of the base to
resonate at 1000 megacycles (a) when it is air-filled and (b) when it is polystyrenefilled
 Calculate the Q in each case.

## Section 2-39: For the rectangular cavity of Fig
 2-19, define a voltage V as that between
mid-points of the top and bottom walls and a current J as the total z-directed current in the side walls. Show that

Vena 1-8 verre

™

Define a mode conductance G asG = §4/|V|? and show that

G= Albe(b? + c?) + 2a(b? + c*))

er

Define a mode resistance R as R = §a/|J|? and show that
R = TAlbe(b? +o) + 2a(b3 + c’))

32(b? + c?)?

INTRODUCTION TO WAVES 93

## Section 2-40: Derive Eqs
 (2-123).

## Section 2-41: Consider the small loop of constant current J as shown in Fig
 2-26. Show
that the magnetic vector potential is

™ Ta [ / de!
Ag -4,|,_, -Z/, tf cos c' dc
5 5? + a? - 2ra sin 6 cos c’)
where p= Boi VE at - ra sin 008 4")
/r? + a? - 2ra sin 6 cos c'
Expand f in a Maclaurin series about a = 0 and show that
Tra se (TE 4 VY oi .
As-> ream & +f) sine
The quantity Iza? = JS is called the magnetic moment of the loop.
Zz
4 r
@
*Fig. 2-26. A circular loop |*
of current. ;
I CUD
Ae a 2
go ae ~J
x >

## Section 2-42: Show that the field of the small current loop of Prob
 2-41 is
Is jk 1
H,= on enikr & + a) cos 6
Is Ke gk | 1).
= Pew (fy ye
Ho= pet ( = +45 +3) sine
= US 6 ite e - i) i
By =e? 7 7 sin 6
Show that the radiation resistance of the small loop referred to J is
Qn (kS\?
z= a (#8)

## Section 2-43: Consider the current element of Fig
 2-21 and the current loop of *Fig. 2-26
to exist simultaneously. Show that the radiation field is everywhere circularly*
polarized if .

Il = kIS
2-44, In terms of the tabulated functions
. zsin z < = cost
Si(z) = I 2a, Cilz) = - f 82 ae

94 TIME-HARMONIC ELECTROMAGNETIC FIELDS
show that Eq. (2-129) can be expressed as
R, = x [ C + log kL - CikL + sin kL (348i 2kL - SikL)
+ 4 cos et (c + log Ke + Ci2hL - acitL) |
where C = 0.5772 - - - is Euler’s constant.

## Section 2-45: If the linear antenna of Fig
 2-23 is an integral number of half-wavelengths
long, the current will assume the form
T(2) = Im sin k(z + 5)
regardless of the position of the feed as long as it is not near a current null. Such an
antenna is said to be of resonant length. Show that the radiation field of the antenna is
cos ‘Gi cos )
ainlm 5 in 2
Bem oe o sino-s« OCC
sin (F cos D)
a tlm gine \2 J
Eg= Dar’ sin 0 neven
where n = 2L/) is an integer.

## Section 2-46: For an antenna of resonant length (Prob
 2-45), show that the radiation
resistance referred to 7,, is
R, = Ez [C + log 2nx - Ci(2nz)]
where n = 2L/A, C = 0.5772, and Ci is as defined in Prob. 2-44. Show that theinput
resistance for a loss-free antenna with feed point at z = ad is
R,
Re= Soe Fa
Specialize this result to L = 4/2, a = 0 (the half-wave dipole) and show that
R; = 73 ohms.

&

---

## Chapter 3: Some Theorems and Concepts

SOME THEOREMS AND CONCEPTS

## Section 3-1: The Source Concept
 The complex field equations for linear

media are

-VxE=2H+M VxH=jE+J (3-1)
where J and M are sources in the most general sense. We have purposely omitted superscripts on J and M because their interpretations
vary from problem to problem. In one Problem, they might represent
actual sources, in which case we would call them impressed currents. In
another problem, J might represent a conduction current that we wish to
keep separate from the gE term. In still another problem, M might
represent a magnetic polarization current that we wish to keep separate
from the 2H term, and so on. We can think of J and M as “mathematical sources,” regardless of their physical interpretation.

For our first illustration, let us show how to represent “circuit sources”
in terms of the “field sources” J and M. The current source of circuit
theory is defined as one whose current is independent of the load. In
terms of field concepts it can be pictured as a short filament of impressed
electric current in series with a perfectly conducting wire. This is shown
in *Fig. 3-la. That it has the characteristics of the current source of circuit theory can be demonstrated as follows. We make the usual circuit*
assumption that the displacement current through the surrounding
medium is negligible. It then follows from the conservation of charge
that the current in the leads is equal to the impressed current, independent of the load. The field formula for power, Eq. (1-66), reduces to

I I

-o SS
FS : :

*Fig. 3-1. Circuit sources*
in terms of impressed
currents. (a2) Current Er Vv Ki Vv
source; (6) voltage
source. ’ |

(a) (8)

95 %

96 TIME-HARMONIC ELECTROMAGNETIC FIELDS

the circuit formula for this source. We have only electric currents; hence
P,= - fff Be Jear = -1 fe-asvie

The “internal impedance” of the source is infinite, since a removal of the

impressed current leaves an open circuit.

The voltage source of circuit theory is defined as one whose voltage is
independent of the load. In terms of field concepts it can be pictured
as a small loop of impressed magnetic current encircling a perfectly conducting wire. This is illustrated by *Fig. 3-1b. To show that it has the*
characteristics of the voltage source of circuit theory, we neglect displacement current and apply the field equation K = - $E-dl to a path
coincident with the wire and closing across the terminals. The E is zero
in the wire; so the line integral is merely the terminal voltage, that is,
Ki = -V. The impressed current, and therefore the terminal voltage,
is independent of load. The field formula for power, Eq. (1-66), reduces
in this case to

P,= - fff H*-M'ar = -KeG H*-al = VI"
which is the usual circuit formula. The internal impedance of the source
is zero, since a removal of the impressed current leaves a short circuit.

We can use the circuit sources in field problems when the source and
input region are of “circuit dimensions,” that is, of dimensions small
compared to a wavelength. Given a pair of terminals close together,
we can apply the current source of *Fig. 3-1la, that is, a short filament of*
impressed electric current. Given a conductor of small cross section,
we can apply the voltage source of *Fig. 3-1b, that is, a small loop of*
impressed magnetic current. As an example of the use of a circuit
source, consider the linear antenna of *Fig. 2-23. The geometry of the*
physical antenna is two sections of wire separated by a small gap at the
input. To excite the antenna, we can place a current source (a short
filament of electric current) across the gap, which causes a current in the
antenna wire. An exact solution to the problem involves a determination
of the resulting current in the wire. This is difficult to do. Instead, we
approximate the current in the wire, drawing on qualitative and experimental knowledge. We then use this current, plus the current source
across the gap, in the potential integral formula to give us an approximation to the field.

We shall find much use for the concept of current sheets, considered in
Sec. 1-14. As an example, suppose we have a J, over the cross section
of a rectangular waveguide, as shown in *Fig. 3-2. Furthermore, we postulate that this current should produce only the TEo1 waveguide mode,*

SOME THEOREMS AND CONUEPTS 97
x
: &
FRED! be
a i [JP iro Zz
a '
7 |
cs le
b
wu
Fia. 3-2. A sheet of current in a rectanguiar waveguide.
which propagates outward from the current sheet. Abstracting from
Table 2-4, we have the wave
Bat = Asin} ov
A. ry _.
+ = 2 gin 7% ost: z>0
Hy, Z, sin |e
Ht = aa cos 2 eres
where the constant. A specifies the mode amplitude. The -z traveling
wave is of the same form with 8 replaced by -8 and Zo by -Zo. Thus,
Ep = Bsin™? om
Bi. ry,
Hy = - 7, sin oi z2<0
__ Bf. Ty
He = -= cos ei
* inf b
where B is the mode amplitude of the -z traveling wave. At z= 0,
Eqs. (1-86) must be satisfied. Take the (1) side to be z > 0, so that
n = u,, and obtain
-u,[H,+ - H,-].-0 = J. {E.+ - Ex \en0 =0
Substitution for H, and E, from above reduces these equations to
A+B. ry _ _Be=
us Zz - sing = Je A-B=0
Let J, = uJosin u (3-2)

98 TIME-HARMONIC ELECTROMAGNETIC FIELDS
The preceding equations then have the solution A = B = -JoZ0/2.
Thus, if the current of Eq. (3-2) exists over the guide cross section z = 0,
then

- iZe sin o e ibe z>0

E,= Tod, , (3-3)

- SS sin es z<0
It would admittedly be difficult to obtain the current of Eq. (3-2) in
practice, but this is not of concern at present. We shall learn how to
treat more practical problems later. Note that our approach in this
problem was to assume the field and find the current. This we shall find
to be a very powerful concept.

## Section 3-2: Duality
 If the equations describing two different phenomena
are of the same mathematical form, solutions to them will take the same
mathematical form. The formal recognition of this is called the concept
of duality. Two equations of the same mathematical form are called dual
equations. Quantities occupying the same position in dual equations are
called dual quantities. Note that the field equations, Eqs. (3-1), are
duals of each other. A systematic interchange of symbols changes the
first equation into the second, and vice-versa.

A duality of importance to us is that between a problem for which
all sources are of the electric type and a problem for which all sources
are of the magnetic type. The first two rows of Table 3-1 give the field
equations in each case. The last two formulas of column (1) were
derived in Sec. 2-9 for homogeneous space. The corresponding equations for the magnetic source case are evidently the last two formulas of
column (2), obtained by systematically interchanging symbols. The
particular interchange of symbols is summarized by Table 3-2. The
reader should check for himself that a replacement of the symbols of

TaBLe 3-1. DuaL EquaTIons FoR PROBLEMS IN WHICH (1) ONLY ELECTRIC

Sources Exist anp (2) Onty Macnetic Sources Exist
(1) Electric sources | (2) Magnetic sources
VXH=gE+J -VXE=2H+M
-v XE=2H | vVXH=4E
H=vXA | E=-vXF
1 Jenne 1 Me-#lt-r'
=- dy’ =- --$dr'
A + fff ir - P| 7 F 4x jr -r'| dr

SOME THEOREMS AND CONCEPTS 99

TasLe 3-2. DuaL QuaANTITIES FOR PROBLEMS IN WuicH (1) ONLY ELEcTRIC

Sources Exist, anp (2) Onty Macneric Sources Exist
(1) Electric (2) Magnetic
sources sources

E H

H -E &

J M

A F

9 z

2 7]

k k

7 1/y :
column (1) of Table 3-2 by those of column (2) in the equations of column
(1) of Table 3-1 results in the equations of column (2). The quantity F
of these tables is called an electric vector potential, in analogy to A, a magnetic vector potential. %

The concept of duality is important for several reasons. It is an aid to
remembering equations, since almost half of them are duals of other equations. It shows us how to take the solution to one type of problem, inter- .
change symbols, and obtain the solution to another type of problem. We
can also use a physical or intuitive picture that applies to one type of
problem and carry it over tothe dual problem. For example, the picture
of electric charge in motion giving rise to an electric current can also be
used for magnetic case. That is, we can picture magnetic charge in
motion as giving rise to magnetic current. Such a picture can serve as
a guide to the mathematical development but cannot, of course, serve to
argue for the existence of magnetic charges in nature. The concept of
duality is based wholly on the mathematical symmetry of equations.

It is often convenient to divide a single problem into dual parts, thus
cutting the mathematical labor in half. For example, suppose we have
both electric and magnetic sources in a homogeneous medium of infinite
extent. The field equations, Eqs. (3-1), are linear; so the total field can
be considered as the sum of two parts, one produced by J and the other
by M. To be explicit, let

E=E +E’ H = H’+H"”

where VX H’=gE'+J -V X E’ = 2H’
and vV xX H” = gE” -V xX E” =2H”+M
We have the solution for each of these partial problems in Table 3-1.
The complete solution is therefore just the superposition of the two partial
solutions, or 
E=-vVxF+f7UvxvxA--J) (3-4)

W=vxA+e'(V¥ X VX F-M)

100 TIME-HARMONIC ELECTROMAGNETIC FIELDS
1 r’ -jkir-r’}
where A(r) = 4 fff esr dr
3-5
woe? ffm G5)
ae ror)
We thus have the formal solution for any problem consisting of electric
and magnetic currents in an unbounded homogeneous region. The above
formulas are meant to include by implication sheets and filaments of
currents.

It is instructive to show that an infinitesimal dipole of magnetic current
is indistinguishable from an infinitesimal loop of electric current. We might
suspect this from the circuit source representations of *Fig. 3-1. However, rather than rely on this argument, let us consider the fields explicitly.*
A z-directed magnetic current dipole of moment KJ at the coordinate
origin is the dual problem to the electric current dipole (*Fig. 2-21). An*
interchange of symbols, according to Table 3-2, in Eqs. (2-113) will give
us the field of the magnetic current element. For example, the electric
intensity is

_ -Kl (ik 1\.
Es = e (2 +5 sin 6
The small loop of electric current is considered in Probs. 2-41 and 2-42
and is pictured in *Fig. 2-26. Abstracting from Prob. 2-42, we have the*
electric intensity given by
= WS sy a _ ik 5
Es dn e T po) sin 6
A comparison of the above two equations shows that they are identical if
Kl = joplS (3-6)
This equality is illustrated by *Fig. 3-3. Thus, effect of an element of*
magnetic current can be realized in practice by a loop of electric current.

## Section 3-3: Uniqueness
 A solution is said to be unique when it is the only

one possible among a given class of solutions. It is important to have
n
i Kl cis
Ss
(a) (b)
*Fig. 3-3. These two sources radiate the Fig. 3-4. S encloses linear matter and*
same field if Kl = jwplS. (a) Magnetic sources J, M.
current element; (b) electric current loop.

SOME THEOREMS AND CONCEPTS 101
precise theorems on uniqueness for several reasons. First of all, they tell
us what information is needed to obtain the solution. Secondly, it is
comforting to know that a solution is the only solution. Finally, uniqueness theorems establish conditions for a one-to-one correspondence of a
field to its sources. This allows us to calculate the sources from, field,
as well as the more usual reverse procedure.

Suppose we have a set of sources J and M acting in a region of linear
matter bounded by the surface S, as suggested by *Fig. 3-4. Any field*
within S must satisfy the complex field equations, Eqs. (3-1). Consider
two possible solutions, E*, H* and E®, H®. (These can be thought of as
the fields when the sources outside of S are different.) We form the
difference field 5E, 5H according to

6E = E*- & 6H = H* - H*

Subtracting Eqs. (3-1) for the a field from those for the b field, we obtain

-vxXsE=20H|

vx sH = 768 | within S
Thus, the difference field satisfies the source-free field equations within S.
The conditions for uniqueness are those for which 5E = 6H = 0 everywhere within S, for then E* = E® and H? = H?.
We now apply Eq. (1-54) to the difference field and obtain
op (oE x oH*)-ds + fff (eloH7l? + glob |") ar = 0

Whenever of (0B x 8H") -ds = 0 (3-7)
over S, the volume integral must also vanish. Thus, if Eq. (3-7) is true,
then

ff [Re (4)|sH|? + Re (g)|sEZ|"] dr = 0

(3-8)

fff [Im (4)|6H|? - Im (g)|5E|?] dr = 0
For dissipative media, Re (2) and Re (g) are always positive. If we
assume some dissipation everywhere, however slight, then Eqs. (3-8) are
satisfied only if 5E = 6H = 0 everywhere within S.

Some of the more important cases for which Eq. (3-7) is satisfied, and
therefore uniqueness is obtained in lossy regions, are as follows. (1) The
field is unique among a class E, H having n X E specified on S, for then
n X dE =Oover 8. (2) The field is unique among a class E, H having
n X H specified on S, for then n x 6H = 0 over S. (3) The field is
unique among a clasy E, H having n X E specified over_part of S and
n X Hspecified over the rest of S. These possibilities can be summarized
by the following uniqueness theorem. A fieldin a lossy region is uniquely PP

LLG TNE O88Y TEPON 18 UMTUY

102 TIME-HARMONIC ELECTROMAGNETIC FIELDS
specified by the sources within the region plus the tangential components of E _
over the boundary, or the tangential components of H over the boundary, or_
the former over part of the boundary and the latter over the rest of the boundary
Note that our uniqu n ss proof breaks down for dissipationless media.
To obtain uniqueness in this case, we consider the field in a dissipationless
medium to be the limit of the corresponding field in a lossy medium as the
dissipation goes to zero.

We have explicitly considered only volume distributions of sources and
closed surfaces in our development, but the results are much more general
than this. Singular sources, such as current sheets and current filaments,
can be thought of as limiting cases of volume distributions and therefore
are included by implication. Surfaces of infinite extent can be thought of
as closed at infinity and can be included by appropriate limiting procedures. Of particular importance is the case for which the bounding surface is a sphere of radius r- ©, so that all space is included. If the
sources are of finite extent, the vector potential solution of Eqs. (3-4) and
(3-5) vanishes exponentially as e-*’", r- «©, We therefore have

lim bE x H*-ds = 0 (3-9)

roe
for this solution (in lossy media). According to our uniqueness proof
this must be the only solution for a class E, H satisfying Eq. (3-9).
Thus, given sources of finite extent in an unbounded lossy region, any solution satisfying Eq. (3-9) must be identically equal to the potential integral
solution. The loss-free case can be treated as the limit of the lossy case.
as dissipation vanishes, - 
To illustrate the above concepts, consider the current element of Fig.

## Section 2-21: Our solution at large r is Eq
 (2-114). Let this be the a solution
of our uniqueness proof, or

He = i ei sin @ Eye = Ht
It can be shown that the inward-traveling wave
He = sit e*sin@ Bot = -nH,P
is also a solution to the equations at larger. In Sec. 2-9, we threw out ;
this second solution by reasoning that waves must travel outward from
* the source, not inward. Let us now consider these two solutions in the
light of the uniqueness theorem. The difference field in this case is
6H, = Hee - Hy = iz cos kr sin @
Il. .
6h, = Bet - Ee = nx; sin kr sin 6

SOME THEOREMS AND CONCEPTS 103
In dissipationless media (k real), we can pick a sphere r = constant such
that either 5H, or 5£, vanishes. Thus, Eq. (3-7) can be satisfied without
obtaining uniqueness of the solution. However, in lossy media, sin kr
and cor kr havenozerosr > 0, and Eq. (3-7) cannot be satisfied for any r.
In this case, only the a solution vanishes as r- ©. It is therefore the

desired solution in loss-free media. &
yaa, 3-4 Image Theory. Problems for which the field in a given Tregion
Be Yor space is determined from a knowledge of the field over the boundary of
Y2- the region are called boundary-value problems. The rectangular wave. guide of Sec. 2-7 is an example of a boundary-value problem. We shall
% now consider a class of boundary-value problems for which the boundary surface is a perfectly conducting plane. The procedure is known as

image theory.

The boundary conditions at_a perfect electric conductor are vanishing
ment of source, radiating in free space, produce zero tangential compo‘nents of E over the plane bisecting the litte joining the tsyo elements,
‘Accerding to uniqueness concepts, the solution to this problem is also
the solution for a current element adjacent to a plane conductor. The
necessary orientation and excitation of image elements is summarized by
*Fig. 3-5. Matter also can be imaged. For example, if a conducting*
sphere is adjacent to the plane conductor in the original problem, then
two conducting spheres at image points are necessary in the image problem. In other words, we must maintain symmetry in the image problem.
The procedure also applies to magnetic conductors in a dual sense. The
application of image theory in a-c fields is much more restricted than in
d-c fields. It is exact only when the plane conductor is perfect.

As an example of image theory, consider a current element normal to
the ground (conducting) plane, as shown in *Fig. 3-6a. This must produce the same field above the ground plane as do the two elements of*
*Fig. 3-6b. Let us determine the radiation field. The*
radius vector from each current element is then parallel 4
to that from the origin and given by

_ { fa
To = 7 -dcos'
aay tod -> ->Il
where subscripts o and 7 refer to original and image
elements, respectively. The radiation field of a single f f KL
element is given by Eq. (2-114); so the radiation field >> Kl
of the two elements of *Fig. 3-6b is the superposition*
Hy -2(= +) sino
eX \c To : Fie. 3-5. A sumx ut er cos(kd cos @) sin @ (3-10) theory. of image

104 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz Zz
@ je a 3
r Il Ti
d
7 eee ea aie
Il
(a) (6)
*Fig. 3-6. A current element adjacent to a ground plane. (a) Original problem; (6)*
image problem.
and E, = H,. According to image theory, this must also be the solution to *Fig. 3-6a above the ground plane.*

The problem of *Fig. 3-6a represents the antenna system of a short*
dipole antenna adjacent to a ground plane. The total power radiated
by the system is

oy = [yf BqH% ds = 2rq Ir? |H,l2r? sin 6 do
aphere
where integration is over the large hemisphere z > 0, r- «©. Substituting from Eq. (3-10) and integrating, we have
~ Tl\?{1 cos2kd , sin 2kd
oy = 2 |s| [3 (kaye * aaa | (-11)
Askd- o, the power radiated is equal to that radiated by an isolated
element [Eq. (2-116)]. As kd- 0, the power radiated is double that
radiated by an isolated element. The gain of the antenna system over
an omnidirectional radiator, according to Eq. (2-130), is
- Snrnl Hel?
I> 8,
2
© 1 _ cos 2kd sin 2kd (3-12)
3 (2kd)? (2kd)*
along the ground plane. This isg = 3 at kd = 0, andg = 6 askd- o.
The maximum gain occurs at kd = 2.88, for which g = 6.57. Thus, a
gain of more than four times that of the isolated element (1.5) can be
achieved. Figure 3-7 shows the radiation field patterns for the cases

SOME THEOREMS AND CONCEPTS 105
fea
cost Tay,
SSR
XSL
PKA
ESTER
LENT ee el
HEE ENS SN
1S EEE EN
Fie. 3-7. Radiation field patterns for the current element of *Fig. 3-6a. A*
Wat vt ar oe
shake | ep De | a RN ee
ee | Sia ae | a 2 ee
SS | ae RSS | Saeed, Wok ceed a
| rn i ae Ra |
(a)
l
_
Sa |
Pi ~ ° | x
N |
; a
coals
2 < |
27 |
i; !
| .
(6)
tube; @) current clement inva conducting weige nen Bconducting

106 TIME-HARMONIC ELECTROMAGNETIC FIELDS
d = 0 (element at the gound plane surface) and d = 0.459\ (maximum
gain).

Image theory also can be applied in certain problems involving more
than one conducting plane. Two such cases are illustrated by *Fig. 3-8.
In the case of a conducting tube (Fig. 3-8a), an infinite lattice of images*
is needed. In the case of a conducting wedge (*Fig. 3-8b), a finite set of*
images results. Image theory can be used for conducting wedges when
the wedge angle is 180°/n (n an integer).

## Section 3-5: The Equivalence Principle
 Many source distributions outside
a given region can produce the same field inside the region. For example,
the image current element of *Fig. 3-6b produces the same field above the*
plane z = 0 as do the currents on the conductor of *Fig. 3-6a. Two*
sources producing the same field within a region of space are said to be
equivalent within that region. When we are interested in the field in a
given region of space, we do not need to know the actual sources. Equivalent sources will serve as well.

A simple application of the equivalence principle is illustrated by Fig.

## Section 3-9: Let Fig
 3-9a represent a source (perhaps a transmitter and antenna)
internal to S and free space external to S. We can set up a problem
equivalent to the original problem external to S as follows. Let the
original field exist external to S, and the null field internal to S, with
free space everywhere. This is shown in *Fig. 3-9b. To support this field,*
there must exist surface currents J,, M, on S according to Eqs. (1-86).
These currents are therefore

J,=nxH M,=EXn (3-18)
where n points outward and E, H are the original fields over S. Since
the currents act in unbounded free space, we can determine the field from
them by Eqs. (3-4) and (3-5). From the uniqueness theorem, we know
that the field so calculated will be the originally postulated field, that is,
E, H external to S and zero internal to S._ The final result of this procedure is a formula for E and H everywhere external to S in terms of the
tangential components of E and H on S.

E,H EH
-_-~ z _- n
/ BH ra { - NY
f \ Zero
\ Sources field \ =
Re } \
S~~__-7 SSM, = EXn
fa) (b)
*Fig. 3-9. The equivalent currents produse the same field external to S as do the*
original sources.

SOME THEOREMS AND CONCEPTS 107
EsHe pH
\ n f n
J fr ~~ or ~
/ \ = ‘ 4
\ f E,He \ ( E’,HO \ i
7 } \ )
sy. Sr
(a) (b)
Es,He Ep }
\ aif n A n
ee ns ----.
ae, ~.
77 \ a \
(> ( f \ ,
\ EH \ eae ‘
\ Ips, \A, Jp
Btcoce -# S-~ sy
M, -™M,
(e) (d)
*Fig. 3-10. A general formulation of the equivalence principle. (a) Original a problem; (b) original b problem; (c) equivalent to a external to S and to b internal to S;*
(d) equivalent to b external to S and to a internal to S.

We were overly restrictive in specifying the null field internal to S in
the preceding example. Any other field would serve as well, giving us
infinitely many equivalent currents as far as the external region is con
_ cerned. This general formulation of the equivalence principle is represented by *Fig. 3-10. We have two original problems consisting of currents in linear media, as shown in Fig. 3-10a and b. We can set up a*
problem equivalent to a external to S and equivalent to b internal to S
as follows. External to S, we specify that the field, medium, and sources
remain the same asin thea problem. Internal to S, we specify that the
field, medium, and sources remain the same asin theb problem. Tosupport this field, there must be surface currents J,andM,onS. According ;
to Eqs. (1-86), these are given by

J. =n X (H* - H’) M, = (E*--E') Xn (3-14)
where E*, H° is the field of the @ problem and E®, H? is the field of the
b problem. This equivalent problem is shown in *Fig. 3-10c. We can*
also set up a problem equivalent to b external to S and toa internal to S
in an analogous manner, as shown in *Fig. 3-10d. In this case the necessary surface currents arg the negative of Eqs. (3-14). Note that in each*
case we must keep the original sources and media in the region for which
we keep the field. Note also that we cannot use Eqs. (3-4) and (3-5) to

108 TIME-HARMONIC ELECTROMAGNETIC FIELDS

E,H EH E,H

-- L n n n
fo EH ~ Zero Zero
( A Sources \ field field
i Magnetic
ON conto,
so 5 M=EXn 9 J. = aXH
(a) (b) (c)

*Fig. 3-11. The field external to S is the same in (a), (b), and (c). (a) Original problem; (b) magnetic current backed by an electric conductor; (c) electric current backed*
by a magnetic conductor.
determine the field of the currents unless the equivalent currents radiate
into an unbounded homogeneous region. Finally, note that the restricted
form of the equivalence principle (*Fig. 3-9) is the special case of the*
general form for which all a sources and matter lie inside S and all b
sources are zero.

So far, we have used the tangential components of both E and H in
setting up our equivalent problems. From uniqueness concepts, we know
that the tangential components of only E or H are needed to determine
the field. We shall now show that equivalent problems can be found in
terms of only magnetic currents (tangential E) or only electric currents
(tangential H).

Consider a problem for which all sources lie within S, as shown in
*Fig. 3-lla. We set up the equivalent problem of Fig. 3-11b as follows.*
Over S we place a perfect electric conductor, and on top of this we place
a sheet of magnetic current M,. External to S we specify the same field
and medium as in the original problem. Since the tangential components
of E are zero on the conductor (just behind M,), and equal to the original
field components just in front of M,, it follows from Eqs. (1-86) that

M.=EXa (3-15)
We now have the same tangential components of E over S in both *Fig.
3-11a and 6; so according to our uniqueness theorem the field outside of S*
must be the same in both cases. We can derive the alternative equivalent problem of *Fig. 3-1lc in an analogous manner. For this we need*
the perfect magnetic conductor, that is, a boundary of zero tangential
components of H. We then find that the electric current sheet

J.=nxH (3-16)
over a perfect magnetic conductor covering S produces the same field
external to S as do the original sources.

By now, the general philosophy of the equivalence principle should be

SOME THEOREMS AND CONCEPTS 109
apparent. It is based upon the one-to-one correspondence between fields
and sources when uniqueness conditions are met. If we specify the field
and matter everywhere in space, we can determine all sources. We
derived our various equivalences in this manner.

Considerable physical interpretation can be given to the oguivalea
principle. For example, in the problem of *Fig. 3-9}, the field internal to*
Sis zero. It therefore makes no difference what matter is within S as
far as the field external to S is concerned. We have previously assumed
that free space existed within S, so that the potential integral solution
could be applied. We could just as well introduce a perfect electric conductor to back the current sheets of *Fig. 3-9b. It can be shown by*
reciprocity (Sec. 3-8) that an electric current just in front of an electric
current conductor produces no field. (We can think of the conductor as
shorting out the current.) Therefore, the field is produced by the magnetic currents alone, in the presence of the electric conductor, which is
*Fig. 3-11b. Alternatively, we could back th'equivalent currents of Fig.*
3-9b with a perfect magnetic conductor and obtain the equivalent problem of *Fig. 3-1lc. When matter is placed within S in Fig. 3-9b, the*
partial fields produced by J, alone and M, alone will change external to S,
but the total field must remain unchanged.

Perhaps it would help us to understand the equivalence principle if we
considered the analogous concept in circuit theory. Consider a source
(active network) connected to a passive network, as shown in *Fig. 3-12a.*
We canset up a problem equivalent to this as far as the passive network
is concerned, as follows. The original source is switched off, leaving the

\ source impedance connected. A current source J, equal to the terminal
current in the original problem, is placed across the terminals. A voltage
a vy
9 Passi ° (~<) Oo ;
Source | } Vv | assive Source Pre | Passive
network Impedance network
o_o? ° ra)
(a) + ®)
+ io
Passive Passive
| ei if network
2°
(c) (@)
*Fig. 3-12. A circuit theory analogue to the equivalence principle. (a) Original problem; (b) equivalent sources; (c) source impedance replaced by a short circuit; (d)*
source impedance replaced by an open circuit.

110 TIME-HARMONIC ELECTROMAGNETIC FIELDS

source V, equal to the terminal voltage in the original problem, is placed
in series with the interconnection. This is illustrated by *Fig. 3-12b. It*
is evident from the usual circuit concepts that there is no excitation of
the source impedance from these equivalent sources, whereas the excitation of the passive network is unchanged. Thus, *Fig. 3-12b is the*
circuit analogue to *Fig. 3-9b.*

Since there is no excitation of the source impedance in *Fig. 3-120, we*
may replace it by an arbitrary impedance without affecting the excitation
of the passive network. This is analogous to the arbitrary placement of
matter within S in the field equivalence of *Fig. 3-9b. In particular, let*
the source impedance be replaced by a short circuit. This short-circuits
the current source and leaves only the voltage source exciting the network
(recall circuit theory superposition). Thus, the voltage source alone, as
illustrated by *Fig. 3-12c, produces the same excitation of the passive network as does the original source. This is analogous to the field problem*
of *Fig. 3-11b. Now consider the source impedance of Fig. 3-12 replaced*
by an open circuit. This leaves only the current source exciting the network, as shown in *Fig. 3-12d. This is analogous to the field problem of*
*Fig. 3-1lc.*

## Section 3-6: Fields in Half-space
 A combination of the equivalence principle
and image theory can be used to obtain solutions to boundary-value
problems for which the field in half-space is to be determined from its
tangential components over the bounding plane. To illustrate, let the
original problem consist of matter and sources z < 0, and free space
z > 0, as shown in *Fig. 3-13a. An application of the equivalence concepts of Fig. 3-11b yields the equivalent problem of Fig. 3-13b. This*
consists of the magnetic currents of Eq. (3-15) adjacent to an infinite

z=0 z=0 z=0
|
EH | EH zZer0 EH oe
| field field
Sources and | 5
matter | 8
3
| SM, =Exn M, = 2EXn
PP eo
| g
|
= n n n
(a) @) (©)
Fie. 3-13. Illustration of the steps used to establish Eq. (3-17).

SOME THEOREMS AND CONCEPTS 111
Z Zz
r r
i}
U @ |
ra |
A
‘es
|
? a]
x x $ |
b
P
\
a) (a) (6) 4
*Fig. 3-14. A coaxial line opening onto a ground lane. (a) Original problem; (b)*
equivalent problem.
ground plane. We now image the magnetic currents in the ground plane, :
according to *Fig. 3-5. The images are equal in magnitude to, and essentially coincident with, the M, of Fig. 3-13b. Thus, as pictured in Fig.*
3-13c, the magnetic currents 2M, radiating into unbounded space produce the same field z > 0 as do the original sources. They produce an
image field z < 0, which is of no interest to us. The field of *Fig. 3-13c is*
then calculated according to Eqs. (3-4) and (3-5) with A = 0. This can
be summarized mathematically by
E ee E(t’) x ds’ 3417
(1) = -V x Oar ar EO) x 48 (3-17)
plane
This is a mathematical identity valid for any field E satisfying Eq. (2-3).
The H field satisfies Eq. (2-4), which is identical to Eq. (2-3); so the
above identity must also be valid for E replaced by H. We can show
this by reasoning dual to that used to establish Eq. (3-17).

The above result is particularly useful for problems involving apertures
in conducting ground planes. Asan example, suppose we have a coaxial
transmission line opening into a ground plane (*Fig. 3-14a). According to*
the above discussion, the field must be the same as that produced by *Fig.
3-14b. Note that M, exists only over the aperture (coax opening), for*
tangential E is zero over the ground plane. Let us‘asume that the field
over the aperture is the transmission-line mode of the coax, that is

‘ =.
Be = Soe (7a)

112 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where V is the line voltage. To this approximation, the magnetic current in *Fig. 3-14b is*
4
M, = ~~
* ~ p log (6/a)
This is a loop of magnetic current which, if b <\X, acts as an electric
dipole (dual to *Fig. 3-3). Visualize this current as a continuous distribution of magnetic current filaments of strengthdK = M,dp. The total*
moment of the source is then
_ 2 _ aV 6
KS [v0 dK log (67a) wa | pdp
_ V(b? - a?)
~ 2 log (b/a) (3-18)
The equivalent electric current element must satisfy the equation dual to
Eq. (3-6), or
Il = -juweKS (3-19)
We have now reduced the problem to that of *Fig. 3-6a with kd = 0.*
From Eq. (3-10) and the above equalities, we have the radiation field
given by
- eT VO = O°) te gi
Hy = “Dvr log (b/a) er sin 6 (3-20)
and Ey = 7H. Thus, the radiation field pattern is the d = 0 curve of
*Fig. 3-7. The gain of the antenna system is g = 3.*
The power radiated is Eq. (3-11) with kd = 0 and JI given by Eqs.
(3-18) and (3-19), or
=~ werV (b? - a?) |22
Or= 2rn| 2 log (b/ay | 3
_ 4n|?2(b? - a®)V |?
= |e Ora) (621)
Note that the power radiated varies inversely as \4. Note also that our
i answers are referred to a voltage, characteristic of aperture antennas.
This is in contrast to answers referred to current for wire antennas. For
aperture antennas we define a radiation conductance according to
i O;
=o 3-22
= 9h (3-22)
i where V is an arbitrary reference voltage. In the coaxial radiator of
i *Fig. 3-14 it is logical to pick this V to be the coaxial V at the aperture.*
Hence, the radiation conductance is
4nd b2 - a2 2
0.= 3 [tee wray| 628)

SOME THEOREMS AND CONCEPTS 113
E=E+E E
+E a n
f Source
a Obstacle Obstacle H} J; = HixXn
LP My = XE
(a) (b) &

*Fig. 3-15. Illustration of the induction theorem. (a) Original problem; (b) induction*
equivalent.
For the usual coaxial line, G, is small, and the coaxial line sees nearly an
open circuit. As a and b are made larger, the radiation becomes more
pronounced, but our formulas must then be modified.!

## Section 3-7: The Induction Theorem
 We now consider a theorem closely
related in concept to the equivalence principle. Consider a problem in
which a set of sources are radiating in the presence of an obstacle (material
body). ‘This is illustrated by *Fig. 3-15c, Define the incident field E',*
Hi as the field of the sources with the obstacle absent. Define the
‘scattered field E*, H' as the difference between the field with the obstacle
present (E, H) and the incident field, that is,

E=E-E H=H-H (3-24)
This scattered field can be thought of as the field_ produced by the currents (conduction _and polarization) on the obstacle. External to_the
obstacle, both E, H and E‘, Hi have the same sources. The scattered field
E:, H' is therefore a source-free field external to the obstacle.

We now construct a second problem as follows. Retain the obstacle,
and postulate that the original field E, H exists internal to it and that
the scattered field E*, H* exists external to it. Both these fields are
source-free in their respective regions. To support these fields, there
must be surface currents on S according to Eqs. (1-86), that is,

J. =n X (H' - H) M, = (E*- E) Xn

where n points outward from S._ According to Eqs. (3-24), these reduce to
JZ.=Hxa M, =n x E (3-25)
It follows from the uniqueness theorem that these currents, radiating in
the presence of the obstacle, produce the postulated field (E, H internal
to S, and E*, H* external to S). This is the induction theorem, illustrated

by *Fig. 3-15b. .*
_ It is instructive to compare the induction theorem with the equiva1H. Levine and C. Ff, Papas, Theory of the Circular Diffraction Antenna, J. Appl.

Phy., vol. 22, no. 1, pp. 29-43, January, 1951.

114 TIME-HARMONIC ELECTROMAGNETIC FIELDS
lence theorem. The latter postulates E, H internal to S and zero field
external to S, which must be supported by currents

J.=Hxn M,=nxE
on S. These currents can be considered as radiating into an unbounded
medium having constitutive parameters equal to those of the obstacle.
Thus, we can use Eqs. (3-4) and (3-5) to calculate the field of the above
currents. However, we do not know J, and M, until we know E, H on S,
that is, until we have the solution to the problem of *Fig. 3-15a. We can,*
however, approximate J, and M, and from these calculate an approximation to E, H within S.

In contrast to the above, the induction theorem yields known currents
(Eqs. (3-25)]. (This assumes that E’, H‘ is known.) We cannot, however, use Eqs. (3-4) and (3-5) to calculate the field from J,, M,, for they
radiate in the presence of the obstacle. A determination of this field is a
boundary-value problem of the same order of complexity as the original
problem (*Fig. 3-15a). We can, however, approximate the field of J,, M,*
and thereby obtain an approximate formula for E, H internal to S and
E’, H: external to S.

A simplification of the induction theorem occurs when the obstacle.is._
a perfect cenductor. This situation is represented by *Fig. 3-16a. The*
solution E must satisfy the boundary condition n X E = 0 on S (zero
tangential E). It then follows from the first of Eqs. (3-24) that

n X Et = -n x Ei on S (3-26)
We now know the tangential components of E* over S; so we can construct the induction representation of *Fig. 3-16b as follows. We keep*
the perfectly conducting obstacle and specify that external to S the field
E’, H’ exists. Tosupport this field, there must be magnetic currents on
S given by
M,=E*'xn=nxXE (3-27) .
We can visualize this current as causing the tangential components of E
to jump from zero at the conductor to those of E* just outside M,. The
E=Ei+ Es E
n n
f Source
<A
conductor conductor
LE M. = nXEi
(a) ()
Fie. 3-16. The induction theorem as applied to a perfectly conducting obstacle. (a)
Original problem; (b) induction equivalent.

SOME THEOREMS AND CONCEPTS 115
Ei + Es Es
Incident wave | / 4
Conducting Conducting
plate plate
(a) (0)

*Fig. 3-17. Scattering by a conducting plate. (a) Original problem; (b) induction*
equivalent.
tangential components of E in *Fig. 3-16b therefore have been forced to |*
be E.. Thus, according to uniqueness concepts, the currents of Eq. (3-27) #
radiating in the presence of the conducting 'bstacle must produce E*, H*
external to S. :

It is interesting to compare this result with the previous one (Fig. aw
3-15b). We found that, in general, both electric and magnetic currents
exist on S in the induction representation. How, then, can both *Fig.
3-15b and Fig. 3-16b be correct for a perfectly conducting obstacle? The*
answer must be that an electric current impressed along a perfect electric
conductor produces no field. If the conductor is plane, this is evident
from image theory. We can prove it, in general, by using the reciprocity
concepts of the next section.

To illustrate an application of the induction theorem, consider the
problem of determining the back scattering, or radar echo, from a large
conducting plate. This problem is suggested by *Fig. 3-17a. For normal*
incidence, let the plate lie in the z = 0 plane and let the incident field be
specified by

Et = Eo e~it (3-28)
According to the induction theorem, the scattered field is produced by
the currents M, = Eo on the side facing the source and M, = -E on
the side away from the source. These currents radiate in the presence
of the original conducting plate, as represented by *Fig. 3-17b. Let the*
field from each element of current be approximated by the field from an
element adjacent to a ground plane. According to image theory, this
means that each element of 17, seen by the receiver radiates as 2M, = 2Eo
‘n free space. Hence, far from the plate, it contributes

be dhs = Dak OAS ine
* 2Qur

116 TIME-HARMONIC ELECTROMAGNETIC FIELDS
in the back-scatter direction. Each element not seen by the receiver
contributes nothing to the back-scattered field. Summing over the entire
plate, we have the distant back-scattered field given by

Ey = i] / dbs = IRE ne (3-29)

our
plate

where A is the area of the plate.

The echo area or radar cross section of an obstacle is defined as the area
for which the incident wave contains sufficient power to produce, by
omnidirectional radiation, the same back-scattered power density. In
mathematical form, the echo area is

A, = lim (190 *) (3-30)
mo S'
where $' is the incident power density and 8' is the scattered power
density. For our problem, §* = |/o|?/n and, from Eq. (3-29),
=, _ L| REA |?
sis | Qqur |
The echo area of a conducting plate is therefore
keA* - 4A? °
A, = oar y oe (3-31)
valid for large plates and normal incidence.

## Section 3-8: Reciprocity
 In its simplest sense, a reciprocity theorem states
that a response of a system to a source is unchanged when source and
measurer are interchanged. In a more general sense, reciprocity theorems relate a response at one source due to a second source to the response
at the second source due to the first source. We shall establish this type
of reciprocity relationship for a-c fields. The reciprocity theorem of circuit theory is a special case of this reciprocity theorem for fields.

Consider two sets of a-c sources, J*, M* and J*, M?, of the same frequency, existing in the same linear medium. Denote the field produced
by the a sources alone by E*, H’, and the field produced by the b sources
alone by E’, H®. The field equations are then

VxH°=jE*+J Vv xX Ho = gE + J°
-V xX E*=2He+M* -v x E = 2H? + M?
We multiply the first equation scalarly by E® and the last equation by H*
and add the resulting equations. This gives
-V- (Ex H*) = gE*- E? + 4H°- H? + E®. Je -+ He- M?

SOME THEOREMS AND CONCEPTS 117
where the left-hand term has been simplified by the identity
v-(AxXB)=B-VXA---A-VXB
An interchange of a and b in this result gives
-V-(E* x H’) = gE*- E+ He. He + E*- J+ He. We .
A subtraction of the former equation from the latter yields
-V- (E* x He - E> x H?) = E*- J’ + H?- Me - E’- Jo - He- M®
(3-32)
At any point for which the fields are source-free (J = M + 0), this
reduces to
v-(E* x H’ - E’ x H*) = 0 (3-33)
\
which is called the Lorentz reciprocity theorem. If Eq. (3-33) is integrated
throughout a source-free region and the clivergence theorem applied, we
have
fp (B x HY - B x He) -ds = 0 (3-34)
which is the integral form of the Lorentz reciprocity theorem for a sourcefree region.
For a region containing sources, integration of Eq. (3-32) throughout
the region gives
- dp (x H - BP x He) -ds
= [ff (E*- Jo - He- Mb - E>. Je + H?- M2) dr (3-35)
Let us now postulate that all sources and matter are of finite extent.
Distant from the sources and matter, we have (see Sec. 3-13)
Ey = nl, Ey = -1Ho
The left-hand term of Eq. (3-35), integrated over a sphere of radius
r- o, is then
7 ff (Hele + HoH,” - HeHe - HyH,*) ds = 0
Equation (3-35) now reduces to
If (B+ J? - He. M®) dr = fff (B+ J* - H®- M*) dr (3-36)
where the integration extends over all space. This is the most useful
form of the reciprodity theorem for our purposes. Equation (3-36) also
applies to regions of finite extent whenever Eq. (3-34) is satisfied. For
ww

118 TIME-HARMONIC ELECTROMAGNETIC FIELDS
example, fields in a region bounded by a perfect electric conductor satisfy
Eq. (3-34); hence Eq. (3-36) applies in this case.

The integrals appearing in Eq. (3-36) do not in general represent power,
since no conjugates appear. They have been given the name reaction.!
By definition, the reaction of field a on source b is

(a,b) = [ff +3) - Be MP) dr (3-37)
In this notation, the reciprocity theorem is
(a,b) = (b,a) (3-38)
that is, the reaction of field a on source b is equal to the reaction of
field b on source a. Reaction is a useful quantity primarily because
of this conservative property. For example, reaction can be used as a
measure of equivalency, since a source must have the same reaction with
all fields equivalent over its extent. This equality of reaction is a necessary, but not sufficient, test of equivalence as defined in Sec. 3-5. We
shall use the term self-reaction to denote the reaction of a field on its own
sources, that is, (a,a).

A valuable tool for expositional purposes can be obtained by using the
circuit sources of *Fig. 3-1 in the reaction concept. For a current source*
(*Fig. 3-la), we have*

(ap) = [Bra = Pf Beal = -yey
where V° is the voltage across the 6 source due to some (as yet unspecified) asource. For a voltage source (*Fig. 3-1b), we have K* = -V*, and*
(ad) = - He Kea = -Kp Hed = VP
where /* is the current through the b source due to some a source. To
summarize, the ‘‘circuit reactions” are
-vere b a current source
b) = =

(a,b) | +V?Ie b a voltage source (3-39)
If we use a unit current source (J* = 1), then (a,b) is a measure of V*
(the voltage at b due to another source a). If we use a unit voltage
source (V® = 1), then (a,b) is a measure of J* (the current at b due to
another source a).

To relate our reciprocity theorem to the usual circuit theory statement of reciprocity, consider the two-port (four-terminal) network of

1V. H. Rumsey, The Reaction Concept in Electromagnetic Theory, Phys. Rev.,
ser. 2, vol. 94, no. 6, pp. 1483-1491, June 15, 1954.

SOME THEOREMS AND CONCEPTS 119
*Fig. 3-18. The characteristics of a linear network can be described by*
the impedance matrix [z] defined by
a [as el [7
= 3-40
[ V2 221 Z22 I, ( )
Suppose we apply a current source J; at port 1 and a current 7 Iz at
port 2. Let the partial response V;; be the voltage at port 7 due*to source
I, at port j. Each current source sees the other port open-circuited (see
*Fig. 3-la); hence*
Va
=,
In terms of the circuit reactions [Eq. (3-39)], (j,i) = - Vali; hence
City
4 = - 41
25 Tl; (3-41)
Thus, the elements of the impedance matrix are the various reactions
among two unit current sources. The r'ciprocity theorem [Eq. (3-38)],
applied to Eq. (3-41), shows that
ij = Bi (3-42)
which is the usual statement of reciprocity in circuit theory. Equations
(3-41) and (3-42) also apply to an N-port network. The use of voltage
sources instead of current sources gives reactions proportional to the elements of the admittance matrix [y], and reciprocity then states that
Yas = Yai
The proofs of many other theorems can be based on the reciprocity
theorem. For example, the preceding paragraph is a proof that any
network constructed of linear isotropic matter has a symmetrical impedance matriz. This “network” might be the two antennas of *Fig. 3-19.
Reciprocity in this case can be stated as: The voltage at b due to a current source at a is equal to the voltage at a due to the same current*
source at b. If the b antenna is infinitely remote from the a antenna,
its field will be a plane wave in the vicinity of a, and vice versa. The
receiving pattern of an antenna is defined as the voltage at the antenna
qh hh \
rs -_> <_. (6)
" (1) (2) Ve @ ° \
Network
*Fig. 3-18. A two-port network, Fig. 3-19, Two antennas.*

120 TIME-HARMONIC ELECTROMAGNETIC FIELDS

terminals due to a plane wave incident upon the antenna. The reciprocity theorem for antennas can thus be stated as: The receiving pattern
of any antenna constructed of linear isotropic matter is identical to its transmitting pattern.

In Secs. 3-5 and 3-7, we used the fact that an electric current impressed
along the surface of a perfect electric conductor radiated no field. The
reciprocity theorem proves this, in general, as follows. Visualize a set of
terminals a on the conductor and another set of terminals b in space
away fromthe conductor. A current element at b produces no tangential
component of E along the conductor; so Vay (V at a due to Js) is zero.
By reciprocity, Via (V at b due to J.) is zero. The terminals b are arbitrary; so the current element along the conductor (at a) produces no V
between any two points in space; hence it produces no E. We can think
of 7, as inducing currents on the conductor such that these currents produce a free-space field equal and opposite to the free-space field of J,.

3-9, Green’s Functions. Our reciprocity relationships are formulas
symmetrical in two field-source pairs. Mathematical statements of reciprocity (symmetrical in two functions) are called Green’s theorems. The
difference between a Green’s theorem and a reciprocity theorem is that
no physical interpretation is given to the functions in the former.

The scalar Green’s theorem is based on the identity

V-(WV9) = WVG4 VY Vo
When this is integrated throughout a region and the divergence theorem
applied to the left-hand term, we obtain Green’s first identity
ae
fp seas = ||] (v8 + ¥¥- v6) dr (3-48)
Interchanging y and c in this identity and subtracting the interchanged
equation from the original equation, we obtain Green’s second identity or
i Green’s theorem
86 _ 4 W) 9, 2 2
: ff (52 - oft) as = [f[ wre - var Gay
This is a statement of reciprocity for scalar fields y and c.
The vector analogue to Green’s theorem is based on the identity
vV-(AXVXB)=VXA:VXB---A-VXVXB
An integration of this throughout a region and an application of the
divergence theorem yields the vector analogue to Green’s first identity
fp (Ax ¥ x B)-as = fff (VX A-VXB--A-VXVXB)dr
(3-45)

SOME THEOREMS AND CONCEPTS 121
. ds
Fie. 3-20. Region to (\)
which Green’s theorem is <p is
applied. 0 ON
s
We can interchange A and B and subtract the resulting equation from
the original equation. This gives the vector analogue to Green’s second
identity, or the vector Green’s theorem,
ff(AxvxB-Bx Vx A)-ds
= fff (BeVXVXA--A-VXVXB)dr (3-46)
Our reciprocity theorem [Eq. (3-35)], for a homogeneous medium, is
essentially Eq. (3-46) with A = E* and B = E*. For an inhomogeneous ‘
medium, still another vector Green’s theorem corresponds to our reciprocity theorem (see Prob. 3-28).

Green’s theorems have been used extensively in the literature as
follows. Suppose we desire the field E at a pointr’inaregion. Instead
of solving this problem directly, a point source is placed at 1’, and its
field is called a Green’s function G. We then substitute E = A and
G =B in Eq. (3-46). This gives a formula for E at r’, as we shall discuss below. What we have done is solve the reciprocal problem (source
at the field point of the original problem) and then apply reciprocity.
The equivalence principle gives the solution more directly.

Let us summarize the various Green’s functions used in the literature.
Stratton chooses!

G, =cc (3-47)
ec-ikle-r"1
where o= irr] (3-48)
and c isa constant vector. A comparison of Eq. (3-47) with Eq. (2-117)
shows that G,; is the vector potential of a current element /1 = 47ec.
Hence, G; is a solution to Eq. (2-108), or
VxVxXGi-Gi=0(V-Gi) rr’ (3-49)
Now suppose we wish to find E at r’ ina source-free region enclosed by S.
The source of G, is placed at r’ and surrounded by an infinitesimal sphere s,
as shown in *Fig. 3#20. Equation (3-46) with A = E and B = G; is now*
1J. A. Stratton, “Electromagnetic Theory,” p. 464, McGraw-Hill Book Company,
Inc., New York, 1941. rJe

122 TIME-HARMONIC ELECTROMAGNETIC FIELDS
applied to the region enclosed by S and s._ The result is

-4re-E = fpex vVxGi-Gix VXE+EV-Gi)+ds (3-50)

which is a formula for calculating E at r’ in terms of n X E,n X V X E,
andn-E on 8S. Furthermore, it is required that E be continuous and
have continuous first derivatives on S. This is a severe restriction on
the usefulness of Eq. (3-50), although it can be amended to admit singular
E’s on S.

A choice of Green’s function which overcomes some of the disadvantages of Eq. (3-50) is!

G.=VX cd (3-51)
where c is given by Eq. (3-48). Thisis evidently the magnetic field of a
current element J] = 4rc. Hence, G, is a solution to
VxvxG.-i*G,=0 rr (3-52)
We now apply Eq. (3-46) with A = E and B = G, to the region enclosed
by S and s in *Fig. 3-20. The result is?*
4nc-V' XE = dp(Gix VXE-EXVXG)-ds (3-53)
8
This is a formula for V’ x E (hence for H) at r’ in terms of n X E and
nxXVXEonS. Equation (3-53) does not require E to be continuous
on S, nor do we need to know n-E on S. Thus, Eq. (3-53) is a substantial improvement over Eq. (3-50). In fact, Eq. (3-53) can be shown
to be identical to the formula obtained from the equivalence principle of
*Fig. 3-9, applied to a homogeneous medium.*
Another useful Green’s function is
G;=VxXVxXcd (3-54)
where c is given by Eq. (3-48). This is proportional to the electric field
of an electric current element; so G; also satisfies Eq. (3-52). An application of Eq. (3-46) would yield a formula for E at r’, similar in form to
Eq. (3-53).

All of the G’s considered so far are “‘free-space’’ Green’s functions,
that is, they are fields of sources radiating into unbounded space. We
can choose other G’s such that they satisfy boundary conditions on S.

1J. R. Mentzer, “Scattering and Diffraction of Radio Waves,” p. 14, Pergamon
Press, New York, 1955.

? The left-hand side of this equation is a function only of the primed coordinates.
Hence, a prime is placed on V’ to indicate operation on 1’ instead of r.

SOME THEOREMS AND CONCEPTS 123
For example, let
G. = Go + Ga (3-55)
such that Gy satisfies Eq. (3-52) and
nxVxGi=0 onS % (3-56)
The physical interpretation of G, is that it is the magnetic field of a
current element /1 = 4c radiating in the presence of a perfect electric
conductor over S. The Gz is the incident field, and the G,' is the scattered field. Application of Eq. (3-46) with A = E and B = G, results in
Eq. (3-53) with the last term zero, because of Eq. (3-56). Thus,
fnew’ x B= dB (Ge X V XE) ds (3-57)
which is a formula for V’ x E in terms of only n X V X EoverS. The
same formula can be obtained from the 'quivalence principle of *Fig. 3-11,*
as it applies to a homogeneous region. :
Similarly, defining a G; such that »
nxG;=0 on S (3-58)
we can obtain a formula
anc V' XE = ~ fh (EX V x Gs)-ds (3-59)
$
and so on. All these various formulas, and many more, can be directly
obtained from the equivalence principle. We have discussed the Green’s
function approach merely because it has been used extensively in the
literature.

## Section 3-10: Tensor Green’s Functions
 We shall henceforth use the term
“Green’s function” to mean “field of a point source.’’? Suppose we have
a current element /1 at r’ and we wish to evaluate the field E at r. The
most general linear relationship between two vector quantities can be
represented by a tensor. Hence, the field E is related to the source /1 by

E =([rjii (3-60)
where [I’] is called a tensor Green’s function. In rectangular components
and matrix notation, Eq. (3-60) becomes

E, Tir Ty Vax | [ol
Ey| = |Vyz Vw Tye | | Lly (3-61)
E, Te. Ty Tal Lh
’
Thus, I';; is the 7th component of E due to a unit j-directed electric current element. The E might be the free-space field of J1, in which “Fo

124 TIME-HARMONIC ELECTROMAGNETIC FIELDS

[I] would be the “free-space Green’s function.”’ Alternatively, E might
be the field of Zl radiating in the presence of some matter, and [T] would
then be called the “‘Green’s function subject to boundary conditions.”
Still other Green’s functions are those relating H to /I, those relating
E to Kl, and so on.

Our principal use of tensor Green’s functions will be for concise mathe
matical expression. For example, the equation
B= /ff (rar (3-62)
where [I] is the free-space Green’s function defined by Eq. (3-60), represents the solution of Eq. (2-111), which is
E = -jupA + v(v- A)
Jenn (3-63)
A= = Equation (3-62) also represents the field of currents in the vicinity of a
material body if [I'] represents the appropriate Green’s function, and so
on. In other words, Eq. (3-62) is symbolic of the solution, regardless of
whether or not we can find [I].

Even though we shall not use tensor Green’s functions to find explicit
solutions, it should prove instructive to find an explicit [I]. Let us take
[I] to be the free-space Green’s function defined by Eq. (3-60). If J] is
z-directed,

Ten ier)
Al= Gro ¥
a 1 0?A,
and E, = -jopA, + joc a®
_ 1 dA,
Pe Fae ay On
_ 1 0a?A,
Be = Fe Oe dn
Comparing this with Eq. (3-61) for Il, = Il, = 0, we see that
. 1 3
Ti. = (- ion + ix aa)Y
2,
nee be
joe OY OX
_ 1 ay
Ta = jwe Oz Ox
h enikir-rl 64
where y= ir FT (3-64)

SOME THEOREMS AND CONCEPTS 125
The other elements of [I] are found by taking J1 to be y-diregted and
then z-directed. From symmetry considerations, the other I’,;’s will differ
only by a cyclic interchange of (z,y,z). The result {s therefore
5 1 3
Ti = (-ien + jue a) y 4, 65
hah oe tAj ”
4 jae 81 a 4
with y given by Eq. (3-64). The reciprocity theorem is reflected in the’
symmetry .
Ty,(t,0’) = Ty(r’,x) (3-66)
which can be proved for I'’s subject to boundary conditions as well. i

## Section 3-11: Integral Equations
 An integral equation is one for which the ”
unknown quantity appears in an integrandy We already have the con- :
cepts needed to construct integral equations. For example, the potential
integral of Eq. (2-118) is essentially an integral equation when J is :
unknown. Most problems can be formulated either in terms of integral :
equations or in terms of differential equations. When ezact solutions
are desired, the differential equation approach is usually the simpler one.
An important use of integral equations is to obtain approximate solutions.
There is good reason for this. Integration is a summation process, and
it is not necessary that each element of the summation be correct. Errors
in some elements of the summation may be compensated for by errors in
other elements. Also, all elements do not contribute equally to a summation. It is much more important that the elements contributing most
to the summation be correct than that the elements of minor contribution be correct. This is why we were able to obtain useful results by
assuming the current on the linear antenna of *Fig. 2-23, by assuming the*
field of each element of magnetic current in *Fig. 3-17b, and so on.*
To illustrate the formulation of an integral equation, consider the
induction theorem of *Fig. 3-16. Let [I'(r,r’)] be the tensor relating the*
E field at r due to an element of M at r’ radiating in the presence of the ,
conductor over S. In equation form, this is
dE(r) = [I(r,r’)] dM(r’)
The total scattered field for the problem is then the summation
E\(r) = ff (P(r,r’)JM,(r’) ds’
a .
where M, is given by Eq. (3-27). When r is on S, Eq. (3-26) must
we

126 TIME-HARMONIC ELECTROMAGNETIC FIELDS
also be true; hence
nX Ei(r) =n X ff [Tar JE(r’) x ds’ ronS (3-67)
8
The incident field E* is assumed to be known; so Eq. (3-67) is an integral
equation for determining [[]. As we mentioned earlier, an exact solution
to Eq. (3-67) would be difficult even for the simplest specialization.

Problems involving a region homogeneous except for small ‘‘islands’’
of matter are commonly encountered. Examples of such problems are
the linear antenna of *Fig. 2-23 and the obstacle of Fig. 3-15a. To illustrate the general concepts involved, suppose we have an inhomogeneous*
region, possibly containing sources J‘ and M‘. Within this region, the
field satisfies

--VxE=4H+Mi VXH=gE4+]J*
where @ and # are functions of position. We can define normal values of
impedivity and admittivity, 2; and #1, which may be any convenient constants (usually the most common 2 and ¥ in the region). We can now
rewrite the field equations as
-VxXE=2H+M VxH=7E+J
where the effective currents are
M = (' - 4)H + M*
~ A : 3-68
J=(@G- WE+F 98)
These effective currents can then be treated as source currents in a homogeneous region. Since J and M are functions of E and H, a solution in
terms of them will lead to an integral equation. However, if 2 = 2, and
9 = g, except in small subregions, we can assume J and M in the subregions and obtain approximate expressions for E and H elsewhere.
(Recall the linear antenna problem, where we assumed J on the antenna
wire.) Note that, when the normal 4 and % are taken as the free-space
parameters, Eqs. (3-68) reduce to
M = jo(@ - yo)H + Mi
- ; 3-69
J =jo(e- «E+ oE + 69)
The effective currents in excess of the true sources (M‘ and J‘) are now
just those due to the motion of atomic particles in vacuum.

Let us reconsider the problem of scattering by an obstacle in the light
of the above concepts. Given the problem of *Fig. 3-15a, we can consider*
the total field to be the potential integral solution of Eqs. (3-4) and (3-5),
with J and M given by Eqs. (3-69). The incident field is that produced

SOME THEOREMS AND CONCEPTS 127
by J‘ and Mi outside of the obstacle, and the scattered field is that produced by

M = jo(@ - o)H
J = jul? - e)E + 0E (3-70)
throughout the obstacle. To be explicit, outside of the obstacle %
B= --vxF4 tyxvxa (3-71)
Jweo
-iklr-r'l
where A= L co dz’
40 jr -1'|
obstacle
A (3-72)
Fe 1 Meriter 5,
4a jr - 1
obstacle '
with J and M given by Eq. (3-70). If we can guess J and M with ‘
reasonable accuracy, then Eqs. (3-71) and (3-72) will give us an approxi- :
mate solution. For a nonmagnetic obstacle, M, and consequently F, will be zero. For a good conductor, J reduces to cE, and this current :
resides primarily on the surface of the obstacle. If we assume the
obstacle perfectly conducting, then J becomes a true surface current.
The solution in this case reduces to
ba 1 Jie ,
Et = Goo, ¥ XV x fp fo (3-73)
Ss
If we specialize this equation to S, then Eq. (3-26) must be met, and we
have an ihtegral equation for determining J..
An approximation to J,, known as the physical optics approximation,
is as follows. Let *Fig. 3-2l1a represent a perfectly conducting obstacle*
illuminated by some source. In terms of the total field, the surface current on the conductor is given by
J.=nxXH
When the obstacle is large, we assume that the total field is negligible in
Ei + Es Es(approx.)
n _ a n
x
Incident wave : '
--_-> J:=2nxHy
‘ /
y $ Ss U7
x aaa
(a) (6)
e
Fig. %-21. The physical optics approximation. (a) Original problem; (b) the
approximation.
ws

428 TIME-HARMONIC ELECTROMAGNETIC FIELDS
the ‘‘shadow”’ region. Furthermore, if the obstacle is smooth and gently
curved, each element of surface behaves similarly to an element of a
ground plane. According to image theory, the tangential components
of H at a ground plane are just twice those from the same source in
unbounded space. We therefore approximate the current on the obstacle
by
J, ~ 2n x Hi _ overS’ (3-74)
where S’ is the illuminated portion of S. The physical optics approximation to the scattered field is therefore
i) -ikle-r'
Ext -yxvx [f/f exer ay (3-75)
2rJweo |r -1’|
‘si

This approximation is illustrated by *Fig. 3-21b.*

As an explicit application of the physical optics approximation, again
consider the large conducting plate of *Fig. 3-17a. The incident E is*
given by Eq. (3-28); hence

H, = Bo ine
n
The physical optics approximation to the obstacle current [Eq. (3-74)] is
therefore
y, = 2Be
n
Each element of this radiates as a current element in free space, as
analyzed in Sec. 2-9. The contribution to the radiation field in the
back-scatter direction from each J; ds is
dE = -IkEo ds enter
2Qur
The total] distant back-scattered field is therefore
jkEyA _.
Es = dEg = - Tot eine 7
i] | E. Sar (3-76)
plate

which is identical to Eq. (3-29), the approximation obtained from the
induction theorem. The physical optics approximation to the echo area
of the plate is therefore that of Eq. (3-31). This equality of the two
approximations to back scattering [Eqs. (3-29) and (3-76)] is no coincidence. It can be shown that the two approaches always give the same
back scattering but do not give the same scattering in other directions.'

1R. F. Harrington, On Scattering by Large Conducting Bodies, JRE Trans.
vol. AP-7, no. 2, pp. 150-153, April, 1959.

SOME THEOREMS AND CONCEPTS 129

## Section 3-12: Construction of Solutions
 So far, we have explicitly considered
only two types of solutions to the field equations, namely, uniform plane
waves and the potential integrals. In the next three chapters, we shall
learn how to construct many other solutions. A general method of
obtaining these solutions is considered here.
In a homogeneous source-free region, the field satisfies % ~

-VXE-=2H v-H=0

VXH=jE v-E=0 @-77)
In view of the divergenceless character of E and H, we can express the
field in terms of a magnetic vector potential A or in terms of an electric
vector potential F. More important, we can employ superposition and
express part of the field in terms of A and part in terms of F. The A
must be a solution to Eq. (2-108) with J = 0, and the F a solution to the
dual equation. The general equations for vector potentials are therefore.

VxXVXA-- RA 4 -Gve
Vx VX F-- KF = -ivo/ (3-78) :
where & and # are arbitrary scalars. The electromagnetic field in terms ;
of A and F is given by Eqs. (3-4) with J = M = 0, or

E=-vxF+lyxvxA
i (3-79)
H=VXA+ZVXVXF
Equations (3-78) and (3-79) are the general form for fields and potentials
in homogeneous source-free regions.
There is a great deal of arbitrariness in the choice of vector potentials.
For instance, we can choose the arbitrary ’s according to
V-A= -Ge VF = -2 (3-80)
This reduces Eqs. (3-78) to
VA + KA =0
VE + kF = 0 G81)
Solutions to these equations are called wave potentials. Note that the
rectangular components of the wave potentials satisfy the scalar wave
equation, or Helmholtz equation, z
vy +ky =0 (3-82)
Also, when Eqs. (3-80) are satisfied, we can alternatively write Eqs.

130 TIME-HARMONIC ELECTROMAGNETIC FIELDS
(3-79) as
E=-v x F-'A+ i vw-a)
1 y (3-83)
H=VXA- GF +5V(V °F) :
We have yet to decide how to divide the field between A and F. Asa
word of caution, do not make the mistake of thinking of A as due to J
and F as due to M. This happened to be our choice for the potential
integral solution, where we considered the sources everywhere. We are
now concerned with regions of finite extent, and we can represent a field
in terms of A or F or both, regardless of its actual source.
Let us now consider some particular choices of potentials. If we take
F = 0 and
A= uy (3-84)
then E = --2ZA+ Avy +A) H=vxA (3-85)
This can be expanded in rectangular coordinates as
-1 oy _
Bs an oa He= 5)
_law __% .
EB, = jy a2 H, = a (3-86)
B.-2(2428 H, = 0
5. = G(s y =e
A field with no H, is called transverse magnetic toz (TM). Weshall find it
possible to choose y sufficiently general to express an arbitrary TM field
in a homogeneous source-free region according to the above formulas.
In the dual sense, if we choose A = 0 and
F=uy (3-87)
then E=-vxF H=-gF +1yv-¥) (3-88)
Expanded in rectangular coordinates, this is
-_% _1 0%
Bs = oy He= 2 dx dz
ov -1 9%
Ey = 35 Hy =3 dy dz (3-89)
E,=0 H,= 1 & +k )y
* = 8\e2?
A field with no Z, is called transverse electric toz (TE). We shall find it
possible to choose y sufficiently general to express any TE field in a
homogeneous source-free region according to the above formulas.

SOME THEOREMS AND CONCEPTS 131
Now suppose we have a field neither TE nor TM. We can determine
a y according to
aye toe
oe + PY = OR:
which will generate a field TM to z according to Eqs. (3-86). bt ™
field will have the same £, as does the original field; so the diff'rence
between the two will be a TE field. We can therefore determine this
difference field according to Eqs. (3-89), where the y is found from
ay p
O22 + key = 2H,
Thus, an arbitrary field in a homogeneous source-free region can be expressed
as the sumofa TMI field anda TE field. Explicit expressions for the field
would be superposition of Eqs. (3-86) and (3-89), with superscripts a and ,
f added to the y’s to distinguish between them. Since the z direction is ;
arbitrary, we can express this independentyof the coordinate system by
defining
A = cy* F = cy (3-90) i
where c is a constant vector. The field is then given by Eqs. (3-79),
which become
E = -V x (cy) tly x VX (cy)
ad (3-91)
H = VX (cy) +30 xv x (oy)
where the ’s are solutions to Eq. (3-82). We must therefore study solutions to the scalar Helmholtz equation to learn how to pick the y’s.
If the region is not source-free but is still homogeneous, our starting
equations are
-VxE=H+M
VXH=gE+J (3-92)
instead of Eqs. (3-77). General solutions to Eqs. (3-92) can be constructed as the sum of any possible solution, called a particular solution, .
plus a solution to the source-free equations, called a complementary solution. We already have a particular solution, namely, the potential integral solution of Sec. 3-2. Therefore, solutions in a homogeneous region
containing sources are given by
E=E,+E, H=H,+H. (3-93)
where the particular solution (ps) is formed according to Eqs. (3-4) and
(3-5), and the complementary solution (cs) is constructed according to
Eqs. (3-91). We can’think of the particular solution as the field due to

132 TIME-HARMONIC ELECTROMAGNETIC FIELDS
sources inside the region and the complementary solution as the field
due to sources outside the region. ;

## Section 3-13: The Radiation Field
 It is easier to evaluate the radiation
(distant) field from sources of finite extent than to evaluate the near field.
(See, for example, Secs. 2-9 and 2-10.) In this section, we shall formalize
the procedure for specializing solutions to the radiation zone.

Consider a distribution of currents in the vicinity of the coordinate
origin, immersed in a homogeneous region of infinite extent. The complete solution to the problem is represented by Eqs. (3-4) and (3-5). If
we specialize to the radiation zone (r >> r/,,x), a8 suggested by *Fig. 3-22,*
we have

jr -r’| >r-r'cost (3-94)
where £ is the angle between r andr’. Furthermore, the second term of
Eq. (3-94) can be neglected in the ‘magnitude factors,” |r - r’|-}, of
Eqs. (3-5). It cannot, however, be neglected in the ‘‘phase factors,”
exp (-jk|r - 1’), unless rf. <A. Thus, Eqs. (3-5) reduce to

A= em Jr") eit’ c08 € de?
4ar
ric" M(x’) cite! «0 € dr! @99)

Aor
in the radiation zone. Note that we now have the r dependence shown
explicitly. Many of the operations of Eqs. (3-4) can therefore be
performed.

Rather than blindly expanding Eqs. (3-4), let us draw upon some
previous conclusions. In Sec. 2-9 it was shown that the distant field of
an electric current element was essentially outward-traveling plane waves.
The same is true of a magnetic current element, by duality. Hence, the

Zz To distant
field point
r-r \
ze
rm Fie. 3-22. Geometry for
6. evaluating the radiation
Zs | field.
“L |
N I Y
~
x ; nace a
“NY

SOME THEOREMS AND CONCEPTS 133
Zz
Zzh~~
e
=S
*Fig. 3-23. Conventional A LY*
coordinate orientation. 8 { y
+9
| 7 Y
x >} Pl Aa
. ens
radiation zone must be characterized by
Ey = Hy Es = -7H (3-96) ‘
since it is a superposition of the fields fromymany current elements. We ,
can evaluate the partial H field due to J according to H’ = v x A (see
Sec. 3-2). Retaining only the dominant terms (r~! variation), we have ©
Hy = (VX A)o = JkAg
Hy, =(V X A)y = -jkAg
with E’ given by Eqs. (3-96). Similarly, for the partial E field due to M,
we have, in the radiation zone,
Ey = -(V X F)o = -jkFs
Ey = -(V X F)s = jkFo
with H” given by Eqs. (3-96). The total field is the sum of these partial
fields, or
Eq = -jupAs - jkFy
. - 3-97
Ey = -jopAs + jkFo (3-97)
in the radiation zone, with H given by Eqs. (3-96). Thus, no differentiation of the vector potentials is necessary to obtain the radiation field.
Also, for future reference, let us determine 7’ cos c as a function of the
source coordinates. The three coordinate systems of primary interest
are the rectangular, cylindrical, and spherical, as illustrated by *Fig. 3-23.
For the conventional orientation shown, we have the transformations*
x =rsin@cosc z= pcosc
y =rsin@sinc y = psing (3-98)
z=rcos' z2=2
To obtain r’ cos & we form
rrcost =r-er = x2’ + yy’ +22! (3-99)

134 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Substituting for z, y, z from the first set of Eqs. (3-98), we obtain
r’ cos § = (x’ cos c + y' sin c) sin 6 + z’ cos 6 (3-100)
which is the desired form when rectangular coordinates are chosen for
the source. Substituting into Eq. (3-100) for 2’, y’, z’ from the second _
set of Eqs. (3-98), we obtain
r’ cos - = p’ sin 6 cos (c - c’) + 2’ cos 8 (3-101)
which is the desired form when cylindrical coordinates are chosen for the
source. Finally, substituting into Eq. (3-100) for x’, y’, 2’ from the first
set of Eqs. (3-98), we have
r’ cos £ = r'[cos @ cos 6’ +. sin @ sin 6’ cos (c - c’)] (3-102)
which is the desired form when spherical coordinates are chosen for the
source.
PROBLEMS

## Section 3-1: Show that a current sheet
J=uJo
over the z = 0 plane produces the outward-traveling plane waves
- we enike z>0
E, = 9
-_ ww eike z<0
in an infinite homogeneous medium

## Section 3-2: Instead of the electric current sheet, suppose that the magnetic current sheet
M, = uM sin #
exists over the cross section z = 0 in the waveguide of Fig
 3-2. Show that this
magnetic current produces a field
- Me gin BY git 2>0
E,= M
a sin a enbe z2<0

## Section 3-3: Suppose now that the two current sheets
_ A
 xy
je = uz Z sin "7 7
M, = 1,4 sin

SOME THEOREMS AND CONCEPTS 135
o
exist simultaneously over the cross section z = 0 of *Fig. 3-2. Show that these produce a field*
zn | Asin ei 2 >0
0 z<0
This source is a ‘directional coupler.” %

## Section 3-4: In Fig
 3-2, suppose that a ‘“‘shorting plate” (conductor) is placed over the
cross section z = -d. Show that the current sheet of Eq. (3-2) now produces a field
_ ho (1 - e782) sin 24 e-vee 2>0 .
es 2 b
-jJ oZoe-iP4 sin “Hsin (ad +2)] -d<z<0
Note that when d is an odd number of guide quarter-wavelengths, Ez for z > 0 is
twice that for the current sheet alone [see Eq. (3-3)], but when d is an integral number; of guide half-wavelengths, no E, exists for z > 0. ?

## Section 3-5: The TE and TM modes of a parallel-plate, waveguide (Prob
 2-28) are almost
dual to each other. Show that the field dual to the TE, mode of Prob. 2-28 is the
TM, mode for the parallel-plate guide having conductors over the planes y = b/2
and y = -b/2. Show that the field dual to the TM, mode of Prob. 2-28 is the TE, s
mode of this new waveguide.

## Section 3-6: Obtain the field of an infinitesimal loop of magnetic current having z-directed
moment KS
 Show that this produces the same field as the electric current element
of *Fig. 2-21 if*
Il = -jueKS

## Section 3-7: Figure 3-24a shows the cross section of a ‘‘twin-slot”’ transmission line
 Show
that the field distribution is dual to that of the collinear plate line of *Fig. 3-24b. By*
integrating along the contours shown in *Fig. 3-24c, determine the line voltages and*
E H
3 cl¥ the
w Ve
hie < |
D H E cy { C,
a
NS
E H
(a) ) (c)
*Fig. 3-24. Figures for Prop. 3-7. (a) Twin-slot line; (b) collinear plate line; (c) integration contours.*
Fl
wi

136 TIME-HARMONIC ELECTROMAGNETIC FIELDS
currents of both the slot line and the plate line. Show that
2
Zo)stot tine = Fy Ze)sot tne 4(Zo)piate tine
From Table 2-3, it follows that
ino slid
Conse ~ Fee EBay P?*
The two transmission lines are said to be complementary structures (see Babinet’s
principle, Sec. 7-12).
co 3-8. Show that the field
Jobo sin 7 iB z>0
2 b
Be Vy ay
Zo TY pipe
gq sine z<0
is also a mathematical solution to the problem of *Fig. 3-2 with J, given by Eq. (3-2).*
What do our uniqueness theorems say about this second solution? What can we say
about it on physical grounds? Give a couple of other possible solutions to the
problem, and interpret them physically.
* ® 3-9. Show that the current sheets
= aug FE gine (Ik 3) i
i= us re u (2 +a sin 6
Il (jou . 2 1 .
= -uy - enta (IPR 4 7
M. Ww ger (2 +3 + 5h) sine
over the spherer = a produce the field of Eqs. (2-113) r > a and zero field r < a.

## Section 3-10: If E is well-bchaved in a homogeneous region bounded by S, and if
2H = -V XE, show that the currents
J= “gE -}¥ XV XE
will support this and only this field among a class E, H having identical tangential
components of E on S
 Show that the same E, but different H, can be obtained
within this class if magnetic sources K are allowed in addition to J.

## Section 3-11: Suppose there exists within the rectangular cavity of Fig
 2-19 a field
E, = Eysin*} sinh y2
where y = V/ (a/b)? - k? and k is complex (lossy dielectric). Show that this field
can be supported by the source
M, = -u,Ep sin 7H sinh ye
at the wall z =c. Show that for a low-loss dielectric, M. almost vanishes at the
resonant frequency [Eq. (2-95)], that is, a small M, produces a large E.
c 3-12. Consider a z-directed current element Jl a distance d in front of a ground
plane covering the y = 0 plane, as shown in *Fig. 3-25. Show that the radiation field*
is given by
Ey = - 2! e-aw sin 9 sin (kd sin 6 sin 6)

SOME THEOREMS AND CONCEPTS 137
and 7H, = Es. Find the power radiated and show that the radiation resistance
referred to I is

R= nl? [5 __ sin 2kd _ cos 2kd | sin 2kd
"> \P 137 ~okd ~ (kd)? +, kd)?
For d < /4, the maximum radiation is in the y direction. Show that
32317d? %
Reo 1M
and that the gain is 7.5 for d small, 4.15 for d = X/4, and approximately 6 for d large.
Z
| x) r
8. \
| ?
*Fig. 3-25. Current ele- |*
ment parallel to a ground ek | oN
plane. | ¥
|
Ky |
LI Sa
Boer N
san ee

## Section 3-13: In Fig
 3-6a, suppose we have a small loop of electric current with z-directed
moment JS, instead of the current element. Show that the radiation field is given by
By = T22IS 5 ir sin (kd cos 6) sin 0
Mr
and 7H» = -E». Find the power radiated and show that the radiation resistance
referred to J is
kS\? [1 | cos 2kd _ sin 2kd
Ry = 2ay (=) [3 + Grae eae |
jnnISkd
For small d, Es foo ee ak sin 26
R ™ (82 2
" kd015 »
Thus, maximum radiation is at @ = 45° for small d. The gain at small dis 15. For
large d, the maximum radiation lies close to the ground plan', and the gain is 6.

## Section 3-14: In Fig
 3-25, suppose we have a small loop of electric current with z-directed
moment JS, instead of the current element. Show that the radiation field is given by
tS iy, A .
Es = Sap oN sin @ cos (kd sin c sin 6)

138 TIME-HARMONIC ELECTROMAGNETIC FIELDS
and 7H» = -Eg,. Show that the radiation resistance referred to I is
_ kS\?[2 | sin 2kd , cos2kd _ sin 2kd

Ry = an (2) [5 + “oa + kay? ce |

The maximum radiation is along the ground plane, in the z direction. For small kd,
dy (KS)? .
Raat s (5)

which is twice that for the isolated loop. For d = 0, the gain is 3; ford = X/4, it is
7.1; and ford- o, itis 6.

## Section 3-15: The monopole antenna consists of a straight wire perpendicular to a ground
plane, fed at the ground plane, as shown in Fig
 3-26. Show that the field is the same
as that from the dipole antenna (*Fig. 2-23), fed at the center. Show that the gain*
of the monopole is twice that of the corresponding dipole and that the radiation
resistance is one-half. For example, the radiation resistance of the \/4 monopole is
36.6 ohms.

*Fig. 3-26. The monopole*
T(z) antenna.

## Section 3-16: Consider an open-ended coaxial line (Fig
 3-14a without the ground plane)
of small radii a and b. Treat the problem according to the equivalence principle
as applied to a surface just enclosing the coax. Assume n X H is essentially zero
over the entire surface and that tangential E is that of the transmission-line mode
over the open end. Show that to this approximation the radiated field is one-half
that of Eq. (3-20) and that the radiation conductance is one-half that of Eq. (3-23).

## Section 3-17: A slot antenna consists of a slot in a conducting ground plane, as shown in
Fig
 3-27. It is called a dipole slot antenna when fed by a voltage impressed across
the center of the slot. -The slot and ground plane can be viewed as a transmission
line, and the field in the slot will be essentially a harmonic function of kz. Assume

Vn L
E,= oral [x G - )]
in the slot, and obtain the magnetic current equivalent of the form of *Fig. 3-13c.*
For w small, show that this equivalent representation is the dual problem to the
dipole antenna of Sec. 2-10. Using duality, show that the radiation field is
L L
GV neni*" cos (x 00s 6) - cos ( a) _ { He y>0
nT sin 0 -He y<0
Nefine the radiation conductance of this antenna asG, = ®;/|Vm|?, and show that.
4(R,) wire dipol
(G,)etot dipole = ACR) wive aipote oD) = me

SOME THEOREMS AND CONCEPTS 139
Z|
a
Lis
4!
*Fig. 3-27. A slot antenna. |*
LPN 1 ¥
& |
\ |
Asia
Ly We ON
© te
\
where R, is as plotted in *Fig. 2-24. The input voltage V; is related toV, by Vi = Vin 3*
sin (kL/2); so the input conductance is given by a
ire a
in? (k% ~
sint (& 5)

## Section 3-18: For the antenna of Fig
 3-27, assume E, in the slot the same as in Prob. 3-17,
and show that for arbitrary w
IV mete ‘2 He y>0
nar 4@,6) = { -He y <0
sin (£¥ cos c sin °) cos (#E cos 0) - cos (« §)
where $8.) = A}
w . sin 6
k Z cos sin 6

## Section 3-19: Figure 3-28 shows an-aperture antenna consisting of a rectangular waveguide
opening onto a ground plane
 Assume that Fz in the aperture is that of the TEo:
Z
Io,
r
= |
*Fig. 3-28. A rectangular Laer |*
waveguide opening onto {
a ground plane.
bt ty ie ¥
4 N |
Al A KPA |
L) A Lyn
" Bs ey
wu

140 TIME-HARMONIC ELECTROMAGNETIC FIELDS
waveguide mode, and show that the radiation field is
sin («5 cos c sin *) cos («3 cos )
Ho = MbBeES Nes? nN 2h
a cos c[x? - (kb cos 6)7}

## Section 3-20: Figure 3-29 represents a rectangular condueting plate of width a in the y
direction and b in the z direction
 Let the incident plane wave be specified by
E,§ = Eei#= coe boty sin $y)
Use the induction theorem with the same approximation as was used in the problem
YX
a
*Fig. 3-29. Scattering by*
$ a rectangular plate.
to
a
I ‘
of *Fig. 3-17, and show that at large r the scattered field in the zy plane is*
» _ KEoabe~i* sin [k(a/2)(sin c + sin co)]
Be ~ ier R(a/2)(sin @ + sin ge) °° ®
Show that the echo area is
; Awd [bers cosine sin oo)"
ina dkasin go

## Section 3-21: Repeat Prob
 3-20 for the orthogonal polarization, that is,
Hi = H ceik(z condatuein $9)
and show that at large r the scattered field in the zy plane is
_ dkHoabe™*' sin [k(a/2)(sin c + sin c0)]
He = “a7 F(a/2)(sin 6 Fin oa) °°
Show that the echo area is the same as obtained in Prob. 3-20.

## Section 3-22: Use reciprocity to evaluate the radiation field of the dipole antenna of Sec

## Section 2-10: To do this, place a 6-directed current element at large r, and apply Eq
 (3-36),
obtaining Eq. (2-125).
® 3-23. By applying voltage sources to the network of *Fig. 3-18, show that the*
admittance matrix [y] defined by

[p| ‘a [as Hall [Fe]
qt ya yd LV2
satisfies the reciprocity relationship yi2 = yz. when Eq. (3-38) is valid.

SOME THEOREMS AND CONCEPTS 141
fo
*Fig. 3-30. Differential*
scattering.
© 3-24. Let *Fig. 3-30 represent two antennas in the presence of an obstacle. Let*
V; be the voltage received at antenna 1 when a unit current source is applied at
antenna 2 and Vz be the voltage received at antenna 2 when a unit current source is
applied at antenna 1. Let Vi‘ and V2‘ be the corresponding voltages when the
\ obstacle is absent. Define the scattered voltages as i
Ve=Vi - Vi Var =V¥2 - Vat
and show that Vit = V2".

## Section 3-25: For the problem of Fig
 3-2, define the input impedance of the sheet of
current as
(a,a)
Za where (a,a) is the self-reaction of the currents and / is the total current of the sheet.
Evaluate Z when the field is given by Eqs. (3-3).

## Section 3-26: Repeat Prob
 3-25 for the current sheet and field of Prob. 3-4.

## Section 3-27: In the vector Green’s theorem (Eq
 (3-46)], let A = E* and B = E® in a
homogeneous isotropic region, and show that it reduces to Eq. (3-35).

## Section 3-28: Use the vector identity
vV°-(AXcV XB)=cVXA'VXB-A‘VX OV XB
and derive the modified vector Green’s theorem
dp oa xVXB--BXvV¥XA)-ds
=fff (B-V X $V XA -A-¥V X ov X B) dr
Let A = Es, B = E>, c = 2"! in an inhomogeneous region, and show that the above
theorem reduces to Eq
 (3-35).

## Section 3-29: Derive the left-hand term of Eq
 (3-50), that is, show
(EXVXGi-GiXV XE+EvV:G:):ds--> 4rc -E
Ir-r'|0
.

142 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 3-30: Let Gs be the magnetic field of a z-directed current element situated y > 0
and radiating in the presence of a perfect electric conductor covering the y = 0 plane

In other words, let c = u, and S be the y = 0 plane. Show that

G=vXu (= = =)
1 T2
where n=V(ae--2P+y-y)? + (2-2)?
r= V(e- 2)? + (y $y’)? + (2 - 2’)?

## Section 3-31: Specialize the G, of Prob
 3-30 to m1 -> ©, and apply Eq. (3-57) to the problem of *Fig. 3-28. Show that this gives the same answer as obtained in Prob. 3-19.*

## Section 3-32: Apply duality to Eqs
 (3-65), and evaluate the magnetic tensor Green’s
function [I] defined by

H = [rKl
in free space.

## Section 3-33: Evaluate the Ty; for the free-space tensor Green’s function defined by
H=(ry/l

3-34
 Repeat Prob. 3-20 using the physical optics approximation, and show that
the answer for £,* differs from that of Prob. 3-20 by an interchange of c and co.
Show that the echo area is identical to that of Prob. 3-20.

## Section 3-35: Repeat Prob
 3-21 using the physical optics approximation, and show that
the answer for H.* differs from that of Prob. 3-21 by an interchange of c and co.
Show that the echo area is identical to that of Prob. 3-21.

## Section 3-36: Let y = e~**” in Eqs
 (3-86), and evaluate the electromagnetic field. Classify
this field in as many ways as you can (wave-type, polarization, etc.).

## Section 3-37: Lety = e~## in Eqs
 (3-89), and evaluate the electromagnetic field. Classify
this field in as many ways as you can.

## Section 3-38: Let c = uz, ¥* = e7*, yf = je*™, and evaluate Eqs
 (3-91). Classify this
field in as many ways as you can.

## Section 3-39: Derive Eqs
 (3-97) by expanding Eqs. (3-4) with A and F as given by Eqs.
(3-95).

SUIEAAAAISERAEAIEYNGUNEPOREIEEEEBETENEEETENNEWANEREEERURUAENIESHNSNNENOCEATNUEEDYRUCRNGINEAEMINEEBEMT TEEN OVESSHRNTEREEEEISMENAIEEENENTERAAAOIEEEEATOEEE EE SSEENESTENESETENEATTAREERATENTEYT



---

## Chapter 4: Plane Wave Functions

PLANE WAVE FUNCTIONS :

## Section 4-1: The Wave Functions
 The problems that we have considered so
! far are of two types: (1) those reducible to sources in an unbounded
homogeneous region, and (2) those solvable by using one or more uniform plane waves. Equations (3-91) show us how to construct general
solutions to the field equations in homogeneous regions once we have
general solutions to the scalar Helmholtz equation. By a method called
separation of variables, general solutions to the Helmholtz equation can be
constructed in certain coordinate systems.! In this section, we use the
method of separation of variables to obtain solutions for the rectangular
coordinate system.
The Helmholtz equation in rectangular coordinates is
Oy OY OW py =
Qa2 + ayit jaz + PY = 0 (4-1)
The method of separation of variables seeks to find solutions of the form
¥ = X@)YY)Ze) (4-2)
that is, solutions which are the product of three functions of one coordinate each. Substitution of Eq. (4-2) into Eq. (4-1), and division by y,
yields
1a?x 1 @’yY 1aZ 2
Xd +yaet+Zaat¥=0 (43)
Each term cari depend, at most, on only one coordinate. Since each
coordinate can be Varied independently, Eq. (4-3) can sum to zero for
all coordinate values only if each term is independent of z, y, and z.
Thus, let
PME ogy EW sey ETL 3,
X dx? * Y dy* 7 Z dz* J
where k,, k,, and k, are constants, that is, are independent of a, y, and z.
(The choice of minus a constant squared is taken for later convenience.)
1It has been shown by Eisenhart (Ann. AMath., vol. 35, p. 284, 1934) that the
Helmholtz equationis separable in 11 three-dimensional orthogonal coordinate systems.

144 TIME-HARMONIC ELECTROMAGNETIC FIELDS
We now have Eq. (4-1) separated into the trio of equations
aX 2
me + k2X =0
ay
ey +k?Y =0 (4-4)
PZ
a + k?Z =0
where, by Eq. (4-3), the separation parameters must satisfy
ke + ky + ke = ht (4-5)
This last equation is called the separation equation.

Equations (4-4) are all of the sameform. They will be called harmonic
equations. Any solution to the harmonic equation we shall call a
harmonic function,! and denote it, in general, by h(k.z). Commonly
used harmonic functions are

h(k.x) ~ sin ka, cos ka, ei", emits (4-6)
Any two of these are linearly independent. A constant times a harmonic
functign is still a harmonic function. A sum of harmonic functions is
still a harmonic function. From Eqs. (4-2) and (4-4) it is evident that
Wrakyke = h(ksx)h(kyy)h(kez) (4-7)
are solutions ‘to the Helmholtz equation when the k; satisfy Eq. (4-5).
These solutions are called elementary wave functions.

Linear combinations of the elementary wave functions must also be
solutions to the Helmholtz equation. As evidenced by Eq. (4-5), only
two of the k; may be chosen independently. We can therefore construct
more general wave functions by summing over possible choices for one or
two separation parameters. For example,

v= Bik Weskyks
= DY Bas (ket) hay)h(ke2) (4-8)
Ke ky

where the B;; are constants, is a solution to the Helmholtz equation. The
values of the k; needed for any particular problem are determined by the
boundary conditions of the problem and are called eigenvalues or characteristic values. The elementary wave functions corresponding to specific
eigenvalues are called eigenfunctions.

1 The term harmonic function also is used to denote a solution to Laplace’s equation.
This is not the present meaning of the term.

PLANE WAVE FUNCTIONS 145

Still more general wave functions can be constructed™by integrating
over one or two of the k;. For example, a solution to the Helmholtz
equation is

v= | [Hk ran, dhe dy
ke ky
= | [Heb )h(kex)h(byy)h(kee) dhe dy (4-9)
kz ky
where f(k.,ky) is an analytic function, and the integration is over any
path in the complex k, and k, domains. Equation (4-9) exhibits a continuous variation of the separation parameters, and we say that there
exists a continuous spectrum of eigenvalues. We shall see that solutions
for finite regions (waveguides and cavities) are characterized by discrete
spectra of eigenvalues, while solutions for unbounded regions (antennas)
often require continuous spectra. Wave functions of the form of
Eq. (4-9) are most commonly used to construct Fourier integrals.

We should be familiar with the mathematical properties and with the
physical interpretations of the various harmonic functions so that we can
properly choose them for particular problems. Keep in mind that wave
functions represent instantaneous quantities, according to Eq. (1-40).
Solutions of the form h(kr) = e~** (k positive real) represent waves
traveling unattenuated in the +2 direction. If k is complex and
Re (k) > 0, we have +2 traveling waves which are attenuated or augmented according as Im (k) is negative or positive. Similarly, solutions
of the form h(kx) = e’*#, [Re (k) > 0] represent -z traveling waves,
attenuated or augmented if k is complex. If k is purely imaginary, the
above two harmonic functions represent evanescent fields. Solutions of
the form h(kx) = sin kx and h(kx) = cos kx with k real represent pure
standing waves. If kis complex, they represent localized standing waves.
If k is purely imaginary, say k = -ja with a real, then the “trigonometric
functions” sin kx and cos kz can be expressed as “hyperbolic functions’’
sinh ax and coshaz. We should get used to thinking of the various
functions as defined over the entire complex kz plane. The trigonometric
and hyperbolic functions are then just specializations of the complex harmonic functions. Table 4-1 summarizes the above discussion. (The
convention k = 8 -ja with a and B real is used.) Note that the
degenerate case k = 0 hhs the harmonic functions h(0r) = 1,z. The
choice of the proper harmonic functions in any particular case is largely
a matter of experience, and facility in this respect will be gained as we
use them.

## Section 4-2: Plane Waves
 Consider an elementary wave function of the form

Y= er tezg hyve ahe (4-10)

146 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TaBLeE 4-1. PROPERTIES OF THE HaRMoNic FuNcTIONS*
Specializa- . .
AMkx) Zerost Infinitiest | tions of Special | __ Physical
b= p- ja] Tepresentations interpretation
k real ibe +z traveling wave
eis | kr -jo kz- jo | kimaginary | e-az Evanescent field
k complex | e-aze-iBz Attenuated traveling wave
k real eiBe -z traveling wave
cits | kr jo kz-+ -je | k imaginary | eas Evanescent field
k complex | eazeiBs Attenuated traveling wave
k real sin Br Standing wave
sin kz | kz = nx kz-» je | k imaginary | -j sinh ex Two evanescent fields
kcomplex | sin Bzcoshaz _| Localized standing waves
-jcos Bz sinhaz
k real cos Bz Standing wave
cos kx | kx = (n + 34)" | kx -> +jo | kimaginary | cosh ar Two evanescent fields
keomplex | cos Bz cosh az _| Localized standing waves
+j sin Bz sinh az
* For & = 0, the harmonic functions are h(Oz) = 1,z.
t For an essential singularity, this column gives the asymptotic behavior.
The k; must satisfy Eq. (4-5), which is of the form of the scalar product
of a vector ~.
‘ k = uk, + uyky + uk, (4-11)
with itself. Note that in terms of k and the radius vector
r=uzrct+ uy t+ uz (4-12)
we can express Eq. (4-10) as
y= eet (4-13)
For k real, we apply Eq. (2-140) and determine the vector phase constant
6= --V(-k-r)=k
Hence, the equiphase surfaces are planes perpendicular to k. The amplitude of the wave is constant (unity). Equation (4-13) therefore represents a scalar uniform plane wave propagating in the direction of k.
Figure 4-1 illustrates this interpretation.
For k complex, we define two real vectors
k=6- je (4-145
and determine the vector propagation constant according to Eq. (2-145).
This gives
Y= -V(-jk +1) = jk = a + 58
We now have equiphase surfaces perpendicular to 8 and equiamplitude

PLANE WAVE FUNCTIONS 147
Equiphase Direction of
Z surface Propagation
*Fig. 4-1. A uniform plane*
wave.
Va
¥
Xx
surfaces perpendicular to a. Thus, when k is complex, Eq. (4-13) represents a plane wave propagating in the direction of 6 and attenuating in
the direction of a. It isa uniform plane wave only if $6 and @ are in the
same direction. Note that definitions k = 6 - ja and k = k’ - jk’ do
not imply that 8 equals k’ or that a equals k’’ in general. In fact, for
loss-free media,
k? =k-k = 6? - a? - j2a-6
must be positive real. Hence, either a = 0 ore@-8=0. When «a = 0
we have the uniform plane wave discussed above. When a and 6 are
mutually orthogonal we have an evanescent field, such as was encountered
in total reflection [Eq. (2-62)].

The elementary wave functions of Eq. (4-10) or Eq. (4-13) are quite
general, since sinusoidal wave functions are linear combinations of the
exponential wave functions. Wave functions of the type of Eqs. (4-8)
and (4-9) are linear combinations of the elementary wave functions. We
therefore conjecture that all wave functions can be expressed as superpositions of plane waves.

Let us now consider the electromagnetic fields that we can construct
from the wave functions of Eq. (4-10). Fields TM to z are obtained if
y is interpreted according to A = u,y. This choice results in Eqs. (3-86),
which, for the y of Eq. (4-10), become

He= -wjkyy + wjkep
= Vy Xu. = jyu. X k (4-15)
and GE = jk.(usjke + uyjky + u.gke)y + uky
= (-kk + u.k*)p (4-16)
For k real, H is perpendicular to k by Eq. (4-15), and E is perpendicular
to k, since
gk E = (-k,k? + k.k*)y =0

148 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Thus, the wave is TEM to the direction of propagation (as well as TM
to z). For k complex, define a and 6 by Eq. (4-14). It then follows
that the wave is not necessarily TEM to the direction of propagation
(that of 8). It will be TEM to 6 only if a and 6 are in the same direction, that is, if

k = 6 - ja = (ul + uym + u.n)k
with 1, m, n real. In this case, B = k’, a = k”’, and l, m, n are the
direction cosines.

The dual procedure applies when y is interpreted according to F = u.y.
In this case, Eqs. (3-89) apply, giving

E = jyk X u,
2H = (-kk + wlk)y (4:17)
which are dual to Eqs. (4-15) and (4-16). For k real, this is a wave
TEM to kand TE toz. Its polarization is orthogonal to the corresponding TM-to-z wave. For k complex, the wave is not necessarily TEM to
the dir'ction of propagation. All these fields are plane waves. An arbitrary electromagnetic field in a homogeneous region can be considered
as a superposition of these plane waves.

## Section 4-3: The Rectangular Waveguide
 The problem of determining modes
in a rectangular waveguide provides a good illustration of the use of elementary wave functions. In Sec. 2-7 we considered only the dominant
mode. In this section we shall consider the complete mode spectrum.
The geometry of the rectangular waveguide is illustrated by *Fig. 2-16.

It is conventional to classify the modes in a rectangular waveguide as*
TM toz (no H,) and TE to z (no E.)._ Modes TM to z are expressible in
terms of an A having only azcomponent ¥. We wish to consider traveling waves; hence we consider wave functions of the form

W = h(kex)h(kyy)e (4-18)
The electromagnetic field is given by Eqs. (3-86). In particular,
B=) kay
y

The boundary conditions on the problem are that tangential components
of E vanish at the conducting walls. Hence, #, must be zero at x = 0,
xz =a,y=0,and y=b. The only harmonic functions having two or
more zeros are the sinusoidal functions with k; real. Thus, choose

h(k.2) = sin kz ky =" m=1,2,3,...

A(kyy) = sinkyy ky = : n=1,2,3,...

PLANE WAVE FUNCTIONS 149
so that the boundary conditions on £, are satisfied. Each integer m and
n specifies a possible field, or mode. The TMmn mode functions are
therefore

Yna™ = sin ™™ gin DEY pate (4-19)
a b
with m = 1,2,3,...,andn = 1,2,3,... , and the separation parameter equation [Eq. (4-5)] becomes

ma\* na \*

as sus k2 = ke 
(=) +BY +8 (4-20)
The TM,.., mode fields are obtained by substituting the Yan™ into Eqs.
(3-86).

Modes TE to z are expressible in terms of an F having only a z component y. Again, we wish to find traveling waves; so the y must be of
the form of Eqs. (4-18). The electromagnetic field this time will be given
by Eqs. (3-89). In particular,

= ot

Es oy Ey = dx
the first of which must vanish at y = 0, y = b, and the second at « = 0,
x =a. Harmonic functions satisfying these boundary conditions are

h(k.x) = cos kx k, = m=0,1,2,...

h(kyy) =coskyy ky -7 n=0,1,2,...
Each integer m and n, except m = n = 0 (in which case E vanishes
identically), specifies a mode. Hence, the TEm, mode functions are

Wmn"® = COS MAE ogg PTY g-ites (4-21)
a b

with m =0,1,2,... iq =0,1,2,...;m =n =Oexcepted. The
separation parameter equation remains the same as in the TM case [Eq.
(4-20)].. The TE, mode fields are obtained by substituting the Pmn™
into Eqs. (3-89).

Interpretation of each mode is similar to that of the dominant TE
mode, considered in Sec. 2-7. Equation (4-20) determines the mode
propagation constant y = jk.. For k real, the propagation constant
vanishes when k is

yan er Pw)
(22) + (22) = den (4-22)

150 TIME-HARMONIC ELECTROMAGNETIC FIELDS
The (k.)mn is called the cutoff wave number of the mn mode. For other
values of k, we have
Ye = jhe = [1B
a= V(k)inn? - k<ke
Thus, for k > k. the mode is propagating, and for k < k, the mode is
nonpropagating (evanescent). From Eq. (4-22) we determine the cutoff
frequencies
=-he _ __ 1 f(m\, (n¥ Wee = Ta BvaNe) +(5)
and the cutoff wavelengths
Qn 2
Adan = 4-25
Come = Be Veale (w/b om
In terms of the cutoff frequencies, we can re-express the mode propagation
constants as
ae
ieaaegi-(B) ss
y = jhe = wes (4-26)
w= healt -(£) S<fh
Je
where mode indices mn are implied. We can also define mode wavelengths for each mode by Eq. (2-85) and mode phase velocities by Eq.
(2-86), where mode indices are again implied.

It is apparent that y = jk. for each mode has the same interpretation
as y for the TEs: mode. It is the physical size (compared to wavelength)
of the waveguide that determines which modes propagate. Table 4-2
gives a tabulation of some of the smaller eigenvalues for various ratios
b/a. Whenever two or more modes have the same cutoff frequency, they
are said to be degenerate modes. The corresponding TEm, and TMmn
modes are always degenerate in the rectangular guide (but not in othershaped guides). In the square guide (b/a = 1), the TEma,; TEam, TMmn;
and TM,,, modes form a foursome of degeneracy. Waveguides are usually constructed so that only one mode propagates, hence b/a > 1 usually.
For b/a = 2, we have a 2:1 frequency range of single-mode operation,
and this is the most common practical geometry. It is undesirable to
make b/a greater than 2 for high-power operation, since, if the guide is
too thin, arcing may occur. (The breakdown power is proportional to
a for fixed b.) To illustrate the use of Table 4-2, suppose we wish to
design an air-filled waveguide to propagate the T Eo: mode at 10,000 megacycles (A = 3 centimeters). We do not wish to operate too close to fe,
since the conductor losses are then large (see Table 2-4). If we take

PLANE WAVE FUNCTIONS 151
(ke)mn _ (felmn _ (re)ou
aSeime seem = --"* ror THE RecTancuLar WavEcuivE, b > a
Mee ean kfle Oda

b TE TE | TEn | TE2

5 | TBs | TE: tM,, | TE | TEs | pats | TMa | TMs | TE"

1 1 1 1.414 2 2 2.236 | 2.236 | 2.828 3

1.5 1 1.5 1.803 2 3 2.500 | 3.162 | 3.606 3

2 1 2 2.236 2 4 2.828 | 4.123 | 4.472 3

3 1 3 3.162 2 6 3.606 | 6.083 | 6.325 3

© 1 © © 2 | co © © 3

i
b = 2 centimeters, then A. = 4 centimeters for the TE», mode, and we
are operating well above cutoff. The next modes to become propagating
are the TE and TEo: modes, at a frequency of 15,000 megacycles. The
TE, and TMi: modes become propagating at 16,770 megacycles, and
so on.

The mode patterns (field lines) are also of interest. For this, we determine E and H from Eqs. (3-86) and (4-19) or Eqs. (3-89) and (4-21),
and then determine &, # from Eq. (1-41). The mode pattern is a plot
of lines of & and 3c at some instant. (A more direct procedure for obtaining the mode patterns is considered in Sec. 8-1.) Figure 4-2 shows
sketches of cross-sectional mode patterns for some of the lower-order
modes. When a line appears to end in space in these patterns, it actually
loops down the guide. A more complete picture is shown for the TE
mode in *Fig. 2-17.

In addition, each mode is characterized by a constant (with respect to*

=FHIERE]| FRE] Re

pani | 
ey we y= mi]
| | | - ZN AA ;

=|- 4 || Pees ra

(a) TEo. (0) TE (c) TMi

¥. iB LJ

Fa, SRE] LAA AEA
BY Hey (A ahs a)

_ 3
PARES ORES) EARN a

(d) TEo2 (e) TEi2z (f) TMiz

€ --_- > A---->
Fig, 4-2, Rectangular waveguide mode patterns,

152 TIME-HARMONIC ELECTROMAGNETIC FIELDS
2x, y) 2-directed wave impedance. For the TEm, modes in loss-free media,
we have from Eqs. (3-89) and (4-21)
: 7 O :
jouH. = -jhe 4 = -jh.E,
+ . O .
jouH, = -jk. x = jk,E.,
The TE., characteristic wave impedances are therefore
on
=a sk
Zadn® = FF = - pe = oh = |B (4-27)
ee RE och
a
Similarly, for the TM modes, we have from Eqs. (3-86) and (4-19)
. 1, O .
jweBs = ~ jk = jkHy
. _ _ 4, OW _ Ls
jweB, = -jk, ay = jkeHz
Thus, the TM,,, characteristic wave impedances are
ff
a > fe
(Zo)ma™ = Es _ -By _ ke _ \ we (4-28)
H, A, we a f<f
joe .
It is interesting to note that the product (Zo)mn™(Zo)ma™ = 7? at all frequencies. By Eq. (4-26), 8 < k for propagating modes; so the TE characteristic wave impedances are always greater than y, and the TM characteristic wave impedances are always less than 7. For nonpropagating
modes, the TE characteristic impedances are inductive, and the TM
characteristic impedances are capacitive. Figure 4-3 illustrates this
behavior.

Attenuation of the higher-order modes due to dielectric losses is given
by the same formula as for the dominant mode (see Table 2-4). Attenuation due to conductor losses is given in Prob. 4-4.

## Section 4-4: Alternative Mode Sets
 The classification of waveguide modes
into sets TE or TM to z is important because it applies also to guides of
nonrectangular cross section. However, for many rectangular waveguide
problems, more convenient classifications can be made. We now consider these alternative sets of modes.

If, instead of Eq. (3-84), we choose

A= wy (4-29)

PLANE WAVE FUNCTIONS 153
2n -;-- --$$
Ro f>fe
ZLo=
EAH ME I<
Pt tad TT SKE TTT
PTT VET TP Pee EE
1 r_]
PT TA Ty fT Pe 4
P| lA hem rem, TT TT |
Re EE
ZEEE see
Oo 1 2 3
fife
*Fig. 4-3. Characteristic impedance of waveguide modes.*
we have an electromagnetic field given by a set of equations differing
from Eqs. (3-86) by a cyclic interchange of x, y, z. To be specific, the
field is given by
B,=2 (2 py, H, =0
*~Gglan th )Y Wem
a) do = & By = G Ax dy Hy = dz (4-30)
oi By: eae
Ene Y Ox dz H. = oy
This field is TM to x. Similarly, if, instead of Eq. (3-87), we choose
F=uy (4-31)
we have an electromagnetic field given by
- a1(@ 4
E,=0 He =3(Fath)y
= _ _1 ay
Ey = dz Ay= Zax dy (4°32)
_ wy _ 1 ay
B= ay Hs = Garas

154 TIME-HARMONIC ELECTROMAGNETIC FIELDS
This field is TE to x. According to the concepts of Sec. 3-12, an arbitrary field can be constructed as a superposition of Eqs. (4-30) and (4-32).
The choice of w’s to satisfy the boundary conditions for the rectangular
waveguide (*Fig. 2-16) is relatively simple. For modes TM to x (TMzmn*
modes) we have
Yan? = cos ™ sin BEY gate (4-33)
a b
where m=0, 1, 2,...; n= 1, 2,3,... 3 and k, is given by Eq.
(4-26). The electromagnetic field is found by substituting Eq. (4-33)
into Eqs. (4-30). For modes TE to x (TEzm, modes) we have
Voat®® = sin ™ eos BY pits (4-34)
a b
where m = 1, 2, 3,...;n=0,1, 2,... ; and k, is again given by
Eq. (4-26). The field is obtained by substituting Eq. (4-34) into Eqs.
(4-32). Note that the TMzo, modes are the TE>, modes of Sec. 4-3,
and the TEzmo modes are the TEm modes. All other modes of Eqs.
(4-33) and (4-34) are linear combinations of the degenerate sets of TE
and TM modes. Note that our present set of modes have both an E,
and H, (except for the 0-order modes). Such modes are called hybrid.
The mode patterns of these hybrid modes can be determined in the
usual manner. (Determine E, H, then &, %, and specialize to some
instant of time.) The TEz,,. mode patterns are those of the TE.) modes,
and the TMzo, mode patterns are those of the TEo, modes. Figure 4-4
shows the mode patterns for the TEx: and TMzi modes, to illustrate
the character of the higher-order mode patterns.
The characteristic impedances of the hybrid modes are also of interest.
For the TMz modes, we have from Eqs. (4-30) and (4-33)
2
joe, = [* - a) \ H, = -jkep
Hence, the z-directed wave impedances are
k® - (mm/a)?
pe lal a >fe
Coyosme = Bs B= mma Ve
ew Hy, wel, k? - (mr/a)?*
mae CUS SK
wen
Note that for a small, the cutoff TMz,,, modes, m ¥ 0, have capacitive
Zy’s, while the cutoff TMzon modes have inductive Zo’s. Similarly, from

PLANE WAVE FUNCTIONS 155
ae oH =a -S
y SSS?
aS ¥ "| tad
y =
pop. Wand
i | MS ES
Vy ty
(a) TEx.
= = --d
uN * SOUNSSSSI KR?
V(? {) H
i
4 SS
<S \) \
Hy A KEN KE
fy ' ¥
(6) TMxi1
*Fig. 4-4. Hybrid mode patterns.*
Eqs. (4-32) and (4-34) we find
ous
: aah fhe
(Zoduntee = Ev ithe) (mena! (4-36)
H, k? - (mm/a)? jen f<f
k? - (ax/a)? .
Note that for a small, the cutoff TEz,,, modes all have inductive characteristic impedances.

Sets of modes TM and TE to y can be determined by letting A = u,y
and F = u,y, respectively. The fields would be given by equations
similar to Eqs. (4-30) and (4-32) with x, y, z properly interchanged.
The TMy and TEy mode functions would be given by Eqs. (4-33) and
(4-34) with mz/a and ng/b interchanged.

## Section 4-5: The Rectangular Cavity
 We considered the dominant mode of
the rectangular cavity in Sec. 2-8. We shall now consider the complete
mode spectrum. The geometry of the rectangular cavity is illustrated
by *Fig. 2-19.

The problem is symmetrical in x, y, 2; so we can express the fields as*
TE or TM to any one of these coordinates. It is conventional to choose
the z coordinate, and then the cavity modes are standing waves of the
usual TE and TM waveguide modes. The wavefunctions of Eq. (4-19)

156 TIME-HARMONIC ELECTROMAGNETIC FIELDS
satisfy the boundary condition of zero tangential E at four of the walls.
It is merely necessary to repick h(k,z) to satisfy this condition at the
remaining two walls. This is evidently accomplished if
_ Mn. nay pre
ys, = sin = sin > cos - (4-37)
with m = 1, 2,3,...;n=1,2,3,...;p =0,1,2,... ;and Eq.
(4-20) becomes
2 2 2
(xye(sye(@y-~ as
a b c
The field of the TM», mode is given by substitution of Eq. (4-37) into
Eqs. (3-86). Similarly, the TE,,, mode functions are given by
Vinp = COs TRE eos TY sin PR? (4-39)
a b c
with m = 0,1,2,... ;n =0,1,2,... ;p=1,2,3,...j;m=n=0
excepted. The separation equation remains Eq. (4-38). The TEnnp
mode field is given by substitution of Eq. (4-39) into Eqs. (3-89).

As indicated by Eq. (4-38), each mode can exist at only a single k,
given a,b,c. Setting k = 2nf Ven, we solve Eq. (4-38) for the resonant
frequencies

+ 1 m 2 n 2 Dp 2
r)mnp = --=4](-) +(5) + ( (4-40)
ew rane) *(3) *(

For a < b <c, the dominant mode is the TEo11 mode. Table 4-3 gives
the ratio (f,)mnp/(fr)o11 for cavities of various side lengths. Note that
TasLp 4-3, dees FoR THE RecTanGcuiar Cavity, a <b <ec

rou
l T™
2) S lrg PEs TMas0) yy |TEovaT Ben] Pan) TBiee TMizo] TMaso| pp
1 1 1 1 1 1.22 | 1.58] 1.58] 1.58] 1.58] 1.58 | 1.58 | 1.73
1 2 1 1 1.26 | 1.34 |1.26/1.84]1.84]1.26| 2.00 | 2.00 | 1.55
2 2 1 |1.58] 1.58 | 1.73 }1.58)1.58]2.91}2.00] 2.00 | 2.91 | 2.12
2 4 1 |1.84] 2.00 | 2.05 ]1.26)1.84]3.60|2.00] 2.53 | 3.68 | 2.19
4 4 1 |2.91) 2.91 | 3.00 |1.58/1.5815.71]3.16] 3.16 | 5.71 | 3.24
4 8 1 |3.62] 3.65 | 3.66 | 1.26] 1.84]7.20]3.65] 4.03 | 7.25 | 3.82
4 |16 1 |3.88} 4.00 | 4.01 |1.08|1.96]7.76|3.91] 4.35 | 7.83 | 4.13

PLANE WAVE FUNCTIONS 157
the TE,,,, and TMmn, modes, mnp all nonzero, are always degenerate.
When two or more sides of the cavity are of equal length, still other
degeneracies occur. The greatest separation between the dominant mode
and the next lowest-order mode is obtained for a square-base cavity
(b = c) with height one-half or less of the base length (b/a > 2). In
this case, the second resonance is V% = 1.58 times the first resonance.

The mode patterns of the rectangular cavity are similar to those of the
TE or TM waveguide modes in a z = constant plane, and similar to the
hybrid mode patterns in the other two cross sections. The most significant difference between the waveguide patterns and the cavity patterns
is that & is shifted from # by A,/4 in the latter case. Also, & and # are
90° out of phase in a cavity; so & is zero when # is maximum, and vice
versa. The TEou mode pattern is shown in *Fig. 2-20. To illustrate*
higher-order mode patterns, *Fig. 4-5 shows the TEi2; mode pattern.*

The quality factor Q of each cavity mode can be determined by the
method used in Sec. 2-8 for the dominant mode. The Q due to dielectric
losses is the same for all modes, given by Eq. (2-100). The Q’s due to
conductor losses for the various modes are given in Prob. 4-10. Note
that the Q increases as the mode order increases. The Q varies roughly
as the ratio of volume to surface area of the cavity, since the energy is

Ke
oop XxX Foood xx
B se x 4 x ° 8 ° _
x MY
(3 x ° x o
xX ooo KxXXK fete
b {xx 000 XKR fore
KX eco XXX oo
a }-----4- c
XL =e lo x ° x
Section A
-jOO0, oop KX 9 S009 xxx OO}
FCO EMP
& a
° fe} x ° Ld
EeWMesse Nl Leh UML sest tes ddl de
Section C Section B
Fia. 4-5. Rectangular cavity mode pattern for the TE;2: mode.

158 TIME-HARMONIC ELECTROMAGNETIC FIELDS
x Z
pas Fie. 4-6. A partially dielectric-filled rectangular
a Farsi waveguide.
« S
REM
9 b Y
stored in the dielectric and the losses are dissipated in the conducting
walls.

## Section 4-6: Partially Filled Waveguide
! Consider a waveguide that is
dielectric filled between z = 0 and z = d (orhas two dielectrics). Thisis
illustrated by *Fig. 4-6. The problem contains two homogeneous regions,*
o< z <dandd <x <a. Such problems are solved by finding solutions in each region such that tangential components of E and H are continuous across the common boundary. An attempt to find modes either
TE to z or TM to z will prove unsuccessful, except for the TEmo case.
Most modes ‘are therefore hybrid, having both Z, and H,. An attempt
to find modes TE or TM to z will prove successful, as we now show.

For fields TM to z, we choose y’s in each region (region 1 is z < d,
region 2 is z > d) to represent the x component of A, as in Eq. (4-29).
The field in terms of the y’s is then given by Eqs. (4-30). To satisfy the
boundary conditions at the conducting walls, we take

vi = Ci cos kaix sin ae Clad
mi. (4-41)
W2 = C2 cos [kz2(a - z)] sin Til e okt
with n = 1, 2,3,.... It has been anticipated that ky = na/b and
k, must be the same in each region for matching tangential E and H at
az =d. Theseparation parameter equations in the two regions are
2
Ken? + (F) + kh? = ky? = wes
‘nm\? (4-42)
Keo? + 9) + ke? = ke? = weope

1L, Pincherle, Electromagnetic Waves in Metal Tubes Filled Longitudinally with

Two Dielectrics, Phys. Rev., vol. 66, no. 5, pp. 118-130, 1944.

PLANE WAVE FUNCTIONS 159
From Eqs. (4-30) and (4-41) we calculate
Ey = ou Cikes 3 sin kat cos ROY 6 ike
joer 6 6
1 nn. 1
Ey: = Fue Crkz2 > sin [ke2(a - x)] cos oe enthe
Ea = ao Cikak, sin k,.x sin PAY ottes
wer b
1 F A
Bay = - =~ Cakath, sin [kx(a - 2)] sin ae ee
Continuity of BE, and E, at x = d requires that
2 Cikersin kad = - 1 Coker sin (kex(a - 0] (4-43)
1 2
Similarly, from Eqs. (4-30) and (4-41) we calculate
Hy, = -jk.C1 cos kz. sin oe ene
Hy = -jk.C2 cos [kz2(a - x)] sin ae emake
Ha =" Cy cos kext cos “@Y eit
6 b
Ha = > C2 cos [kz2(a - x)] cos Fe ete
Continuity of H, and H, at x = d requires that
Ci cos kad = C, cos [kz2(a - d)) (4-44)
Division of Eq. (4-43) by Eq. (4-44) gives
Stan kad = - “tan [hela - d)] (4-48)
1 2
Both ka and kz. are functions of k, by Eqs. (4-42); so the above is a
transcendental equation for determining possible k,’s (mode-propagation
constants). Once the desired k, is found, ka and k,2 are given by Eqs.
(4-42), and the ratio C2/C4 is given by Eq. (4-43) or Eq. (4-44).

For fields TE to z, we choose y’s in each region to represent the « componentof F. Tosatisfy the boundary conditions at the conducting walls,
we take

vi = Cisin kit cos ae en tkee
(4-46)
v2 = Cr sin [k.2(a - z)] cos EY eins

160 TIME-HARMONIC ELECTROMAGNETIC FIELDS
with n = 0, 1, 2,..:. The separation parameter equations are again
Eqs. (4-42). The field is calculated from the y’s by Eqs. (4-32). A
matching of tangential E and H at x = d yields-the characteristic equation
ker Kea
-cot kid = - - cot [ko(a - d)] (4-47)
wy Be
The_ka and kz: are functions of k. by Eqs. (4-42); so the above is a
transcendental equation for determining k.’s for the modes TE to z.

The modes of the partially filled rectangular waveguide are distorted
versions of the TEx and TMz modes of Sec. 4-4. The mode patterns are
similar to those of *Fig. 4-4, except that the field tends to concentrate in*
the material of highere andy. In the lossless case, the cutoff frequencies
(kz = 0) of the various modes will always lie between those for the corresponding modes of a guide filled with a material c1, u1, and those of a
guide filled with a material €2, uw». (This can be shown by the perturbational procedure of Sec. 7-4.) In contrast to the filled guide, the cutoff
frequencies of the corresponding TEx and TMz modes will be different.
Also, a knowledge of the cutoff frequencies of the partially filled guide is
not sufficient to determine k, at other frequencies by Eq. (4-26). We
have to solve Eqs. (4-45) and (4-47) at each frequency.

Of special interest is the dominant mode of a partially filled guide.
For b > a, this is the mode corresponding to the TMzo: mode of the
empty guide, which is also the TEo mode of the empty guide. For a
given n, Eq. (4-45) has a denumerably infinite set of solutions. We shall
let m denote the order of these solutions, as follows. The mode with the
lowest cutoff frequency is denoted by m = 0, the next mode by m = 1,
andsoon. Thisnumbering system ischosen so that the TMzm, partially
filled waveguide modes correspond to the TMzmn empty-guide modes.
The dominant mode of the partially filled guide is then the TMzo1 mode
when b > a. Hence, the propagation constant of the dominant mode is
given by the lowest-order solution to Eq. (4-45) when the k,’s are given
by Eqs. (4-42) with n = 1. Figure 4-7 shows some calculations for the
case € = 2.45ce.

When ky is not very different from k:, we should expect kz: and kz.
to be small (k, is zero in an empty guide). If this is so, then Eq. (4-45)
can be approximated by

kavd _ -kes*(a - d) (4-48)

€1 €2
With this explicit relationship between kz; and k,2, we can solve Eqs.
(4-42) simultaneously for k.1 and k, (given w). Note that when kz: is
real, k,) is imaginary, and vice versa. The cutoff frequency is obtained
by setting k, = 0 in Eqs. (4-42). Using Eq. (4-48), we have for the

PLANE WAVE FUNCTIONS 161
16 T ia |
i CECE
12 =
WZ er
b-| - |
Sol 4 ZAnnnEee
ra
| LTP i7zT Py yy
" PEELE
0 01 0.2 03 0.4 0.5 0.6
a/ro
*Fig. 4-7. Propagation constant for a rectangular waveguide partially filled with*
dielectric, « = 2.45, a/b = 0.45, d/a = 0.50. (After Frank.)
dominant mode
T 2
ka? +45) = wenn
b
zed), my _ oo
Sta - a) ka? + 9) weope
These we solve for the cutoff frequency » = w,, obtaining
7 ex(a - d) + ed
am | a aoe 4-49
° b Vn - d)eopo + endeypy ( )
valid when Eq. (4-48) applies. When p; = ue = yu, this reduces to
wot J -d)+ed (4-50)
b Beye20
Note that this is the equation for resonance of a parallel-plate transmission line, shorted at each end, and having
= C= €1€2
L = wa ata - d) + ad
per unit width. All cylindrical (cross section independent of z) waveguides at cutoff are two-dimensional resonators.

A waveguide partially filled in the opposite manner (dielectric boundary
parallel to the narrow side of the guide) is the same problem with a > b.
The dominant mode of the empty guide is then the TExio mode, or TE;
mode. The dominant mode of the partially filled guide will also be a

162 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TEx mode; so the eigenvalues are found from Eq. (4-47) with n = 0.
We shall order the modes by m as follows. That with the lowest cutoff
frequency is denoted by m = 1, that with the next lowest by m = 2, and
soon. This numbering system corresponds to that for the empty guide,
the dominant mode being the TEx. mode. When k; is not too different
from k2, we might expect kz and k,, to be close to the empty-guide value
k, = /a. An approximate solution to Eq. (4-47) could then be found
by perturbing k. and kz. about z/a. For the cutoff frequency of the
rE a
Zo=n | Zo = 2
T W), Boh | Bak
b yy 2,42 |
1 Ui) jg +a -dd --+
(a) (b)
*Fig. 4,8. (a) Partially filled waveguide; (b) transmission-line resonator. The cutoff*
frequenty of the dominant mode of (a) is the resonant frequency of (b).
16
d/ua=1
ee a PE
Y 7 pg
pOEe esas
12 Lis 4 ws A =e = 0.375|
L L\e Z| call =< |
eo | | | be
# oe WL) AVAL bso
er) ae PT
Aff lA, WA
SaR/7aneee
it mina Big
PEL ETT | pai |
ie} 0.2 0.4 0.6 0.8 10
a/ro
*Fig. 4-9. Propagation constant for a rectangular waveguide partially filled with*
dielectric, c = 2.45e0. (After Frank.)

PLANE WAVE FUNCTIONS 1 163 7%
x
Fia. 4-10. The dielectric- £0,HO
slab waveguide. =
YY Vip
vA
Z ZA GU
dominant mode, Eqs. (4-42) become
kay? = hy? = wey
Kao? = koe? = wPeope
and Eq. (4-47) becomes
1 cot kud = - + cot fire(a - d)] (451)
1 . ne
It is interesting to note that this is the equation for resonance of two shortcircuited transmission lines having Z,’s of m1 and 72, and f’s of ki. and Kae,
as illustrated by *Fig. 4-8. The reason for this is, at cutoff, the TEx*
mode reduces to the parallel-plate transmission-line mode that propagates
in the z direction. This viewpoint has been used extensively by Frank.

Some calculated propagation constants for the dominant mode are
shown in *Fig. 4-9 for the case e = 2.45co. Similar results for a centered*
dielectric slab are shown in *Fig. 7-10, and the characteristic equation for*
that case is given in Prob. 4-19.

## Section 4-7: The Dielectric-slab Guide
 It is not necessary to have conductors for the guidance or localization of waves. Such phenomena also
occur in inhomogeneous dielectrics. The simplest illustration of this
is the guidance of waves by a dielectric slab. The so-called slab waveguide is illustrated by *Fig. 4-10.

We shall consider the problem to be two-dimensional, allowing no*
variation with the y coordinate. It is desired to find z-traveling waves,
that is, e~* variation. Modes TE and TM to either z or z can be found,
and we shall choose the lgtter representation. For modes TM to z, Eqs.
(3-86) reduce to

_ ak. dy nd aa 2 = oy
E, = ne BE E, = Fut (k ka?) H,.= az (4-52)
We shall consider separately the two cases: (1) y an odd function of z,
denoted by y’, and (2) y an even function of z, denoted by ¥*. For case

1N. H. Frank, Wave Guide Handbook, MIT Rad. Lab. Rept. 9, 1942.

164 TIME-HARMONIC ELECTROMAGNETIC FIELDS
(1), we choose in the dielectric region
va? = Asin uz ee |z| < 5 (4-53)
and in the air region
Va? = Ben™=e-ihe a> 5
a (4-54)
Wa? = -Berte-itet na<-2
We have chosen kzg = wand kz) = jv for simplicity of notation. (It will
be seen later that wu and » are real for unattenuated wave propagation.)
The separation parameter equations in each region become
w+ k2 = ka? = wea
=v? +k? = ko? = weopto (4-56)
Evaluating the field components tangential to the air-dielectric interface,
we hav'
E, = A. u’ sin ux e7* a
Joea || < 3
sH, = -Aucos ux em
Hy = Boe7*!\eH= |z| > 5
E, = =B ee aid ad z>c
jJweo 2
E, = BD yrgozg-ike re?
Jweo 2
Continuity of Z, and H, at x = +a/2 requires that
A asin MF = ~B p2eral?
€a 2 €0
Au cos $ = -Bye-*s!?
The ratio of the first equation to the second gives
ua ua _ «ava “y tan 5 a2 (4-56)
This, coupled with Eqs. (4-55), is the characteristic equation for deterMining k,’s and cutoff frequencies of the odd TM modes.

PLANE WAVE FUNCTIONS 165

For TM modes which are even functions of z, we choose

wat = A cos ux ee |z| < 5
a (4-57)
Yat = Beles |a| > 5
The separation parameter equations are still Eqs. (4-55). The field com-ponents are still given by Eqs. (4-52). In this case, matching E, and
H,at x = +a/2 yields
Ud gag Ma _ ge 00 .
-¥> cot x GR (4-58)
This is the characteristic equation for determining the k.’s and cutoff
frequencies of the even TM modes.

There is complete duality between the TM and TE modes of the slab
waveguide; so the characteristic equations must be dual. For the TE
modes with odd y we have

ua ua _ Hava 3 tan 3 Pap (4-59)
as the characteristic equation, and for the TE modes with even y we have
Eee cote ies eee 7
5 cot 5 ro) (4-60)
as the characteristic equation. The w’s and v’s still satisfy Eqs. (4-55).
The odd wave functions generating the TE modes are those of Eqs. (4-53)
and (4-54), and the even wave functions generating the TE modes are
those of Eqs. (4-57). The fields are, of course, obtained from the y’s by
equations dual to Eqs. (4-52), which are, explicitly,
_ _ kz op a 2 he _ oy
H,= ou ot H, = a (k k*)p BE, = 3g (4-61)
These are specializations of Eqs. (3-89).

The concept of cutoff frequency for dielectric waveguides is given a
somewhat different interpretation than for metal guides. Above the
cutoff frequency, as we define it, the dielectric guide propagates a mode
unattenuated (k, is real). Below the cutoff frequency, there is attenuated propagation (k, = 8 - ja). Since the dielectric is loss free, this
attenuation must be accounted for by radiation of energy as the wave
progresses. Dielectric guides operated in a radiating mode (below cutoff)
are used as antennas. The phase constant of an unattenuated mode lies
between the intrinsic phase constant of the dielectric and that of air;
that is,

ko < ky < ka

166 TIME-HARMONIC ELECTROMAGNETIC FIELDS

This can be shown as follows. Equations (4-55) require that u and v be
either real or imaginary when k, is real. The characteristic equations
have solutions only when v is real. Furthermore, v must be positive,
else the field will increase with distance from the slab [see Eqs. (4-54) or
(4-57)]. When »v is real and positive the characteristic equations have
solutions only when u is also real. Hence, both u and v are real, and it
follows from Eqs. (4-55) that ko < k, < ka. This result is a property of
cylindrical dielectric waveguides in general.

The lowest frequency for which unattenuated propagation exists is
called the cutoff frequency. From the above discussion, it is evident that
cutoff occurs as k, > ko, in which case v0. The cutoff frequencies
are therefore obtained from the characteristic equations by setting
u = Vk? - ko and v = 0. The result is

0 poe ae C0 a pee a
tan (5 Vika - a) =0 cot (5 V kat - a) = 0

which apply to both TE and TM modes. These equations are satisfied
wher

5 Vie ke = n= 0,12...
This we solve for the cutoff wavelengths

, _ 2a fea, _

ne = 22 [at 1 n=0,1,2,... (4-62)
and the cutoff frequencies

fe = -- n= 01,2 (4-63)

. 2a Vata - €oHo poe
The modes are ordered as TM, and TE, according to the choice of n in
Eqs. (4-62) and (4-63). Note that f. for the TEs and TMo modes is zero.
In other words, the lowest-order TE and TM modes propagate unattenuated
no matter how thin the slab. This is a general property of cylindrical
dielectric waveguides; the cutoff frequency of the dominant mode (or
modes) is zero. However, as the slab becomes very thin, k, > ko and
v- 0, so the field extends great distances from the slab. This characteristic is considered further in the next section. Finally, observe from
Eq. (4-62) that when egug >> eouo, the cutoffs occur when the guide width
is approximately an integral number of half-wavelengths in the dielectric,
zero half-wavelength included.

Simple graphical solutions of the characteristic equations exist to
determine k, at any frequency above cutoff. Let us demonstrate this

PLANE WAVE FUNCTIONS 167
for the TE modes. Elimination of k, from Eqs. (4-55) gives
u? + v? = ka? - ko? = w?(eaua - €opto)
Using this relationship, we can write the TE characteristic equations as
Ho ua ua
Piers (22 ces - ano - (22)
_ sa P . ma > () (€apta - €op0) - (“)
Values of ua/2 for the various modes are the intersections of the plot
of the left-hand terms with the circle specified by the right-hand term.
Figure 4-11 shows a plot of the left-hand terms for na = wo. A representative plot of the right-hand term is shown dashed. As w or ea is
varied, only the radius of the circle changes. (For the case shown, only
three TE modes are above cutoff.) If ua # yo, the solid curves must be
redrawn. Thegraphical solution forthe TM mode eigenvalues is similar.
Sketches of the mode patterns are also of interest. Figure 4-12 shows
the patterns of the TE, and TM; modes. These can also be interpreted
as the mode patterns of the TMo and TE, modes if & and & are interchanged, for there is complete duality between the TE and TM cases.
fel 8)
a ae Oe
LT ES TT EEE
pe
g
; EPAPER
| tet AE
2 LLU LUT YT TT TT
ee eee
a LTA TTA ETAT TT TT
ptt iVi tt Vit | VT Tt |
A n/2 A 7 A 30/2 20
oe 8 @& @
Fie. 4-11. Graphical solution of the characteristic equation for the slab waveguide.

168 TIME-HARMONIC ELECTROMAGNETIC FIELDS
\ ° / i \ x / --.~ \e /
/ \
o\ f° / \A\ >: / \ °\ pe
\° FOR \ |< | Taw \ \°|
AGE i \ ht] wae
° x °
of2 ofe {2 *h fifehs i “foytef>
° yi ° x x x ° c °
lo, lo x Pil ix \ Jo} jor
] Y NZ 7 | iN cre 4
i a aa
° o \ fr % x \ / 4 °
sans Lb X’s 7 | \
° \ en at / Seth tat / = \
(@)
4 x ° x
ARC aan Cae
x ° x
we 8 -- x xe
°o
5D i@ Gey): (esp)
o 8 = x a)
(Es 20 8 SDE
x ° x
(6)
Fia. 4-12. Mode patterns for the dielectric-slab waveguide. (a) TEo mode (3 lines
dashed); (b) TM, mode (& lines solid).
As the mode number increases, more loops appear within the dielectric,
but not in the air region.

## Section 4-8: Surface-guided Waves
 We shall show that any “reactive
boundary” will tend to produce wave guidance along that boundary.
The wave impedances normal to the dielectric-to-air interfaces of the
slab guide of *Fig. 4-10 can be shown to be reactive. A simple way of*
obtaining a single reactive surface is to coat a conductor with a dielectric
layer. This is shown in *Fig. 4-13.

The modes of the dielectric-coated conductor are those of the dielectric*
slab having zero tangential E over the x = 0 plane. These are the TM,,
n = 0, 2,4, . . . , modes (odd y) and the TE,, = 1, 3,5, . . . , modes

PLANE WAVE FUNCTIONS 169
(even y) of the slab. We shall retain the same mode designations for the
coated conductor. The characteristic equations for the TM modes of
the coated conductor are therefore Eq. (4-56) with a/2 replaced by t
(coating thickness). The characteristic equation for the TE modes is
Eq. (4-66) with a/2 replaced by t. The cutoff frequencies are specified
by Eq. (4-63), which, for the coated conductor, becomes
n

fa = eng es (4-64)

“ 4t-Veana - €osto
where for TM modes n = 0, 2, 4,. .., and for TE modes n = 1, 3,
5, .... The dominant mode is the TM» mode, which propagates
unattenuated at all frequencies. The mode pattern of the TMo mode
is sketched in *Fig. 4-14.

Let us consider in more detail the manner in which the dominant mode*
decays with distance from the boundary. In the air space, the’ field
attenuates as e~*. For thick coatings, k, > ka, and, from Eq. (4-55),

»--> ho i -1 (4-65)
t large Eno
This attenuation is quite large for most dielectrics. For example, if the
coating is polystyrene (eg = 2.56c0, za = po), the field in 0.12 has decayed
to 36.8 per cent of its value at the surface. However, for thin coatings,
x
€0,F0
IRB?BCTMEK GV
WW’. z
*Fig. 4-13. A dielectric-coated conductor.*
° x °
° x °
fo ™ {as
Hee VERE A .\ekbls
*Fig. 4-14. The TMo mode pattern for the coated conductor (& lines solid.)*

170 TIME-HARMONIC ELECTROMAGNETIC FIELDS
x
d
Zz

*Fig. 4-15. A corrugated conductor.*

the field decays slowly. In this case, k, > ko, and
Ha _ eo) t DR 2tko (# A) x (4-66)

If the polystyrene coating were 0.0001 wavelength thick, we would have
to go 40 wavelengths from the surface before the field decays to 36.8 per
cent, of its value at the surface. We say that the field is “ tightly bound”
to a thick dielectric coating and “loosely bound” to a thin dielectric
coating.

Another way of obtaining a reactive surface is to ‘‘corrugate”’ a conducting surface, as suggested by *Fig. 4-15. Fora simple treatment of*
the problem, let us assume that the “teeth” are infinitely thin, and that
there are many slots per wavelength. The teeth will essentially short
out any E,, permitting only E, and E, at the surface. The TM fields of
the dielectric-slab guide are of this type; hence we shall assume that this
field exists in the air region. Extracting from Sec. 4-7, we have

g = ay,
WED
E, = =i v2e-te-iket u>d
jweo
H, = Bue-*e-itet
: where -v? + k,? = ko? = weouo (4-67)
The wave impedance looking into the corrugated surface is
_E, _ jv
Zz = H, 7 ace (4-68)
Note that this is inductively reactive; so to support such a field, the
interface must be an inductively reactive surface. (The TE fields of
Sec. 4-7 require a capacitively reactive surface.) In the slots of the
corrugation, we assume that the parallel-plate transmission-line mode

PLANE WAVE FUNCTIONS 171
exists. These are then short-circuited transmission lines, of characteristic wave impedance yo. Hence, the input wave impedance is

Z_. = jnotan kod (4-69)
For kod < 2/2, this is inductively reactive. Equating Eqs. (4-68) and
(4-69), we have
v = ky tan kod (4-70)
and, from Eq. (4-67), we have

Kee = kyo V1 tan? hood (4-71)
It should be pointed out that this solution is approximate, for we have
only approximated the wave impedance at x = d. In the true solution,
the fields must differ from those assumed in the vicinity of z = d. (We
should expect E£, to terminate on the edges of the teeth.)

When the teeth are considered to be of finite width, an approximate
solution can be obtained by replacing Eq. (4-69) by the average wave
impedance. This is found by assuming Eq. (4-69) to hold over the gaps,
and by assuming zero impedance over the region occupied by the teeth.
The result is?

2
k= koafl + (4) tan? kod
where g = width of gaps and t = width of teeth.

While at this time we lack the concepts for estimating the accuracy
of the above solution, it has been found to be satisfactory for small
kod. Note that, from Eq. (4-70), the wave is loosely bound for very
small kod, becoming more tightly bound as kod becomes larger (but still
less than 7/2). The mode pattern of the wave is similar to that for the
TM, coated-conductor mode (*Fig. 4-14), except in the vicinity of the*
corrugations.

## Section 4-9: Modal Expansions of Fields
 The modes existing in a waveguide
depend upon the excitation of the guide. The nonpropagating modes
are of appreciable magnitude only in the vicinity of sources or discontinuities. Given the tangential components of E (or of H) over a waveguide cross section, we can determine the amplitudes of the various waveguide modes. This we shall illustrate for the rectangular waveguide.

Consider the rectangular waveguide of *Fig. 2-16. Let H, = 0 and*
E, = f(z,y) be known over the z = 0 cross section. We wish to determine the field z > 0, assuming that the guide is matched (only outwardtraveling waves exist). The TEx modes of Sec. 4-4 have no £.; so let us

1C. C. Cutler, Electromagnetic Waves Guided by Corrugated Conducting Surfaces,
Bell Telephone Lab. Rept. MM-44-160-218, October, 1944.

172 TIME-HARMONIC ELECTROMAGNETIC FIELDS
take a superposition of these modes. This is
y= » > Ann SiN = cos at ETnnt (4-72)
m=1n=0
where A,,, are mode amplitudes and the ym, are the mode-propagation
constants, given by Eq. (4-23). In terms of y, the field is given by Eqs.
(4-32). In particular, H, at z = 0 is given by
E, | = a +3 YmnAmn SiN MOF cog DEY
2=0 a b
m=1n=0
Note that this is in the form of a double Fourier series: a sine series in x
and a cosine series in y (see Appendix C). It is thus evident that Ymn4mn
are the Fourier coefficients of E,, or
- Ann = E. = [ae fia E, sin eos MY (4-73)
eicemins mab Jo 0 Yh 20 a b
where en = 1 forn = Oande, = 2 forn > 0(Neumann’s number). The
Ayn, and hence'the field, are now evaluated. The solution for Ez = f(z,y)
and E, = 0 given over the z = 0 cross section can be obtained from the
above solution by a rotation of axes. The general case for which both
E,zand E, are given over the z = 0 cross section is a superposition of the
two cases EF, = 0 and EF, =0. The solution for the case Hz and H,
given over the z = 0 cross section can be obtained in a dual manner.
For a large class of waveguides, when many modes exist simultaneously,
each mode transmits energy as if it existed alone. We shall show that
the rectangular waveguide has this property. Given the wave function
of Eq. (4-72), specifying a field according to Eqs. (4-32), the z-directed
complex power at z = 0 is
a >
pe [[exurude=- [as [artes
24 0 °
a 'b
= i ac [ a> Enn Sin ME oon MH]
0 0 a b
in ;
= () |
aT Bx gin PA ogg IY
x » jouye, ES, sin a °° 5
Pe
Because of the orthogonality relationships for the sinusoidal functions,

PLANE WAVE FUNCTIONS 173
ty ty
ea mi, Incident wave
eb
se i zZ
< oe
-- |
*Fig. 4-16. A capacitive waveguide junction.*
this reduces to
P=) Y Wotdiea? 2 (4-74)
m=1n=0 ™
where (Yo)mn are the TEx wave admittances, given by the reciprocal of
Eqs. (4-36). The above equation is simply a summation of the powers
for the individual modes. In a lossless guide, the power for a propagating
mode is real and that for a nonpropagating mode is imaginary.

To illustrate the above theory, consider the waveguide junction of Fig.

## Section 4-16: The dimensions are such that only the dominant mode (T Eo)
propagates in each section
 Let there be a wave incident on the junction from the smaller guide, and let the larger guide be matched. For
an approximate solution, assume that EZ, at the junction is that of the
incident wave

~ Wr
z,| es {ins y<e (4-75)
7-0 0 y>ec
From Eq. (4-73), the only nonzero mode amplitudes are
By = ywAiw = 7
2 yon (4-76)
.. us
Ein = YinAin = ie a
Thus, only the m = 1 term of the m summation remains in Eq. (4-72).
Let us use this solution to obtain an ‘aperture admittance” for the
junction. From Eqs. (4-44) and (4-76), the complex power at z = 0 is
_ ac? * « [sin (nmc/b) ??
P= yh {rom +2 y (Yoh [sane
n=1
where, from Eqs. (4-36),
_ R= G/a)? _Vi- c/fP
(Yo)10 = sub wk 7
k? - (n/a)? j2b(Yo)10
(Yo). = ---- = ----jopo dy Vn? - (2b/rs)?

174 TIME-HARMONIC ELECTROMAGNETIC FIELDS
3 T T 1 : T T T T T T T T T
ENEREEREEE |
AKT [ote Ji
. E c
2 0. \ il,
Ee WATT | || LE = sin(wx /a) x
3 PANE R eee
N
a NNN
NN
i_-E TT INSANE TTT TET TTT
TT TT INSAN TTT TT TT
TTT TT SNA TT
Ltt | ASS
. PCN SSSc0
Oo 0.2 0.4 0.6 0.8 10
c/b
*Fig. 4-17. Susceptance of a capacitive aperture.*
The f. and d, are those of the TEio mode. We shall refer the aperture
admittance to the voltage across the center of the aperture, which is
V =c. The aperture admittance is then
Rs a . 2a = sin? (nwc/b)
Yo = ap = (VY ay - | (4-77
°= IVE (Yo)10 [x +3 ws oy (nxc/b)?-V nt - aS ( )
n=l
The imaginary part of this is the aperture susceptance
2a = sin? (nrc/b)
Ba = > UEP 4-78
“Meo *, (nae/b)? in? - (2b/24)* on)
n=1
where A, and Zo are those of the dominant mode. Calculated values for
Ba are shown in *Fig. 4-17. For small c/b, we have!*
AZo c 2b\?
bq Be ~ - log {0.050 § [1 + 4/1 =) || (4-79)
1This equation is a quasi-static result. The direct specialization of Eq. (4-78) to
small c/b yields a numerical factor of 0.379 instead of 0.656.

PLANE WAVE FUNCTIONS 175
Ax Ax
i E Incident
= wave >
Ye Zz
_ ann
a -*
Fia. 4-18. An inductive waveguide junction.
The aperture susceptance is a quantity that will be useful for the treatment of microwave networks in Chap. 8. Note that the susceptance is
capacitive (positive); so the original junction is called a capacitive waveguide junction. Remember that our solution is only approximate, since
we assumed E in the aperture. (We shall see in Sec. 8-9 that the true
susceptance cannot be greater than our present solution.) We have
assumed that only one mode propagates in the guide; hence our solution is
explicit only for
v<Leifr4(2y
fe b
When a second mode propagates, it contributes to the aperture conductance, and Eq. (4-78) would be summed from n = 2 to », and so on.
Another problem of practical interest is that of the waveguide junction
of *Fig. 4-18. Again we assume only the dominant mode propagates in*
each section. Take a wave incident on the junction from the smaller
guide, and let the larger guide be matched. For an approximate solution, we assume Z, in the aperture to be that of the incident wave
. az
Ey |eno = sin z a<e (4-80)
0 z>ec
From Eqs. (4-73), we determine the only nonzero mode amplitudes as
; 2c sin (mmc/a)
= -81
Bao xa{l - (me/a)] (4-81)
Thus, only the n = 0 term of the n summation remains in Eq. (4-72).
Again we can find an aperture admittance for the junction. From
Eqs. (4-74) and (4-81), the complex power at z = 0 is
_ 2be? « | sin (mmc/a) |?
P= Ta > von [ = (mc/a)*
m=1

176 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where, from Eqs. (4-36),
eo _ V1 = (f/f)?
You = = = Me
(Y)r0 ous 7
2 2 a |
(Van = Elo = Em)" m>1
Jona ul) 2a
The voltage across the center of the aperture is V = b. The aperture
admittance referred to this voltage is therefore
_ 2c? sin (1c/a) \
Y, ~~ gab (#2, (Yo)i0
j sin (mmc/a) | ‘ma\2
-s EY eee PAY my) -1 4-82
7 », [i - (me/a)? (2 (4-82)
m=2
The imaginary part of this is the aperture susceptance
_ -2r0(c\ Xt [sin (mac/a) 7 we 2 ‘a\?
Bom eb (‘) Be [ 1 = (me/a)? a) - (°) (83)
m=2
which is plotted in *Fig. 4-19. The susceptance is inductive (negative);*
so the original junction is called an inductive waveguide junction. For
single-mode propagation, we must have a < A; so our explicit interpreAMEE a5 aces
-|-J c
==
0.2 SRS =< ap = 0.5 Tf
Swed 07 - te B
4 SS i
zz BANNE! E = sin (7x/c) xX
S .
7 08 K INNA N an |
= EEEEEEEFERSRRAE EEE
js |
NX
SSNCaE
- PSS
o> _LIT TT TTT Titi ttt it Ts
0.2 0.4 0.6 0.8 10
c/a
*Fig. 4-19. Susceptance of an inductive aperture.*

PLANE WAVE FUNCTIONS 177
tation of the solution is restricted to this range. For wave propagation
in the smaller guide, we must have c > \/2 if it is air-filled. However,
if the smaller guide is dielectric-filled, we can have wave propagation in it
when c < A/2. Moreover, the aperture susceptance is defined only in
terms of EF, in the aperture and has significance independent of the
manner in which this Z, is obtained.

## Section 4-10: Currents in Waveguides
 The problems of the preceding section
might be called “‘aperture excitation” of waveguides. We shall now consider ‘current excitation’? of waveguides. This involves the determination of modal expansions in terms of current sheets over a guide cross
section. The only difference between aperture excitation and current
excitation is that the former assumes a knowledge of the tangential electric field and the latter assumes a knowledge of the discontinuity in the
tangential magnetic field. The equivalence principle plus duality can be
used to transform an aperture-type problem into a current-type problem,
and vice versa.

To illustrate the solution, consider a rectangular waveguide with a
sheet of z-directed electric currents over the z = 0 cross section. This is
illustrated by *Fig. 3-2, where J, = u.f(z,y) is now arbitrary. We shall*
assume that only waves traveling outward from the current are present,
that is, the guide is matched in both directions. At z = 0 we must have
E,, E,,and H, continuous. H, must also be antisymmetric about z = 0;
hence it must be identically zero, and it is convenient to use the TMz
modes of Sec. 4-4. (Note that J and its images are z-directed; so it is
to be expected that an z-directed A is sufficient for representing the field.)
Superpositions of the TMz modes are

y= > > Brant cos = sin MEU g-toat z>0
mao nal (4-84)
y= » » Bram cos = sin MY orant z2<0
a b
m=0n=1
where superscripts + anfl - refer to the regions z > 0 and z < 0, respectively. The field in terms of the w’s is given by Eqs. (4-30). Continuity
of E, and E, at z = 0 requires that
Brat = Baa = Bun (4-85)
The remaining boundary condition is the discontinuity in H, caused by
Jz, which is
Jz = [Hy - H,*).-0 = », » 2YmnBmn COS = sin oe
m=O0n=1

178 TIME-HARMONIC ELECTROMAGNETIC FIELDS
This is a Fourier cosine series in z and a Fourier sine series in y. It is
evident that 27mnBmn are the Fourier coefficients of J., that is,
_ 2m [* b maz . nary

2 mnBmn = Imn = a }} dz Vi dy Jz cos {7 (4-86)
This completes the determination of the field. The solution for a
y-directed current corresponds to a rotation of axes in the above solution. When both J, and Jy exist, the solution is a superposition of the
two cases Jy = OandJ, = 0. Thesolution for a magnetic current sheet
in the waveguide is obtained in a dual manner. A 2z-directed electric
current can be treated as a loop of magnetic current in the cross-sectional
plane, according to *Fig. 3-3. A z-directed magnetic current is the dual*
problem. Thus, we have the formal solution for all possible cases of
currents in a rectangular waveguide.

It is also of interest to find the power supplied by the currents in a
waveguide. This is most simply obtained from

& e >
P=- [J Seas = -f{, dz [, dy Jt Bz 290
ze
We express J, in its Fourier series and evaluate E, by Eqs. (4-30) applied
to the above solution. Because of the orthogonality relationships, the
power reduces to
ab
P= (Zo) mnlT mal? 4 (4-87)
m=On=1 ‘ad
where (Zo)mn are the TMz wave impedances, given by Eqs. (4-35).
This is a summation of the powers that each J,,, alone would produce
in the guide. In a lossless guide, the power associated with each propagating mode is real, and that associated with a nonpropagating mode is
imaginary.

As an example of the above theory, consider the coax to waveguide
junction of *Fig. 4-20. This is a waveguide “probe feed,” the probe*
being the center conductor of the coax. If the probe is thin, the current
on it will have approximately a sinusoidal distribution, as on the linear
antenna. With the probe joined to the opposite waveguide wall, as
shown in *Fig. 4-20, the current maximum is at the joint z =a. We*
therefore assume a current on the probe

I(x) ~ cos k(a - 2) (4-88)
The current sheet approximating this probe is
Jz = I(x)5(y - c) (4-89)

PLANE WAVE FUNCTIONS 179
fe
c->| & ey
Pe Matched ia Matched
i load *) load
4
loee a
Coax
*Fig. 4-20. A coax to waveguide junction.*
where 6(y - c) is the impulse function, or delta function (see Appendix
C). The Fourier coefficients for the current are then obtained from
Eq. (4-86) as
2e,ka sin ka sin nxc/b
m= ooo" 4-90
Joe = -T1CEayE - (rr) (490)
This, coupled with our earlier formulas, determines the field.

In terms of this solution, let us consider the input impedance seen by
the coaxial line. The power supplied by the stub is given by Eq. (4-87).
The impedance seen by the coax is then

P aye

Z= ire Ry + 9X:

where, from Eq. (4-88), the input current is
I; = cos ka
Assume that the waveguide dimensions are such that only the TEo: mode
propagates. Then only the m = 0, = 1 term of Eq. (4-87) is real, and
2
R= F(R | du
_a,, tanka\? .. , mc

= 5 odor ( ka ) sin’ > (4-91)
All other terms of the summation of Eq. (4-87) contribute to X; However, since we assumed a filamentary current, the series for X; diverges.
To obtain a finite X,;, we must consider a conductor of finite radius. For
small a, the reactance will be capacitive. In the vicinity of a = d/4,
we have a resonance, above which the reactance is inductive. Note that
Eq. (4-91) says that the input resistance is infinite at this resonance.
This is incorrect for an actual junction, and the error lies in our assumed
current. Equation (4-91) gives reliable input resistances only when we
are somewhat removed from resonant points. [This is similar to our
linear antenna solution (Sec. 2-10)]. Feeds in waveguides with arbi
trary terminations are considered in Sec. 8-11.

180 TIME-HARMONIC ELECTROMAGNETIC FIELDS
| oan
Incident F
> - a }-________»
wave YL Z
*Fig. 4-21. A parallel-plate guide radiating into half-space.*

## Section 4-11: Apertures in Ground Planes
 We have already solved the problem of determining the field from apertures in ground planes, in Sec. 3-6.
At this time, however, we shall take an alternative approach and obtain
a diff'rent form of solution. By the uniqueness theorem, the two forms
of solution must be equal. One form may be convenient for some calculations, and the other form for other calculations.

Let us demonstrate the theory for an aperture in the ground plane
y = 0, illustrated by *Fig. 4-21. We further restrict consideration to the*
case E, = 0, there being only an FE, in the aperture. Taking a clue from
our waveguide solution (Sec. 4-9), let us consider Fourier transforms (see
Appendix C). The transform pair for HZ, over the y = 0 plane is

Baez) = gz [tke [dhs BAbgk oho
: ee (4-92)
E(kz,k2) = [ dx [ dz E.(x,0,2z)e**e-#*
where a bar over a symbol denotes transform. The form of the transformation suggests that we choose as a wave function
y= ao ii _ dhe he dk, f(Reeshe)otberoibwveshr (4-93)
which is a superposition of the form of Eq. (4-9). For our present problem, we take Eq. (4-93) as representing a field TE to z, according to
Eqs. (3-89). There is a one-to-one correspondence between a function
and its transform; hence it is evident that the transform of y is
Y = f(keyhe)eh (4-94)

PLANE WAVE FUNCTIONS 181
We also can rewrite Eqs. (3-89) in terms of transforms as
a ‘ 7 -kiks
E, = -jkyp Hz = Faas v
Ra ties 7 -hyks
By = ghd By =a v (4-95)
- - 2_ pe
E,=0 A, = Behe? y
Jon
Specializing the above to the y = 0 plane, we have
Ey \yoo = -Jhyf(kaske)
A comparison of this with Eqs. (4-92) shows that
-l.
G(keyke) = a E(kz,k:) (4-96)
jhy
where £, is given by the second of Eqs. (4-92). This completes the solution. Asa word of caution, k, = + /k? - k? - k? is double-valued,
and we must choose the correct root. For Eq. (4-94) to remain finite as
y- ©, we must choose
e hate + ke - he? k< Vee + ke (4.97)
oe VERSE SRR b> Vite
The minus sign on the lower equality is necessary to remain on the
same branch as designated by the upper equality.

The extension of this solution to problems in which both EZ, and E,
exist over the y = 0 plane can be effected by adding the appropriate TE
to field to the above TE to z field. It can also be obtained asthe sum
of fields TE and TM toz, or toz, ortoy. The case of Hz and Hy, specified over the y = 0 plane is the dual problem and can be obtained by
an interchange of symbols.

For simplicity, we shall choose our illustrative problems to be twodimensional ones. Let *Fig. 4-21 represent a parallel-plate waveguide*
opening onto a ground eK If the incident wave is in the transmissionline mode (TEM to y), it is apparent from symmetry that H, will be the
only component of H. Let us therefore take H, as the scalar wave function and construct

=e il ” Seetroiw dhe, (4-98)
From this, it is evident that the transform of H, is
A, = f(kejem (4-99)

182 TIME-HARMONIC ELECTROMAGNETIC FIELDS
From the field equations, we relate the transform of E to H, as
gaba, b--%a, (4-100)
we we
Specializing F, to y = 0, we have
z,| = v7Q.) = f B(x,0)e-# de (4-101)
y=0 we ~e
from which f(kz) may be found. For an approximate solution to *Fig.
4-21 for y > 0, we assume #, in the aperture to be of the form of the*
incident mode, that is,
1 [l< 3
z,| ad a (4-102)
ly=0
0 |z| > 5
Using this in Eq. (4-101), we find
B:|) yey = an (re E, He = act ks) =| sin (« 5) (4-103)
To complete. the solution, we must also choose the root of k, for proper
behavior as yo ©. From Eq. (4-99), it is evident that this root is
; 2__ 2
b= (? ViFSE! be thd (4-104)
--VkR-kA k> |kel
The fields are found from the transforms by inversion.

A parameter of interest to us in future work is the aperture admittance.
To evaluate this, we shall make use of the integral form of Parseval’s
theorem (Appendix C), which is

- 1 [? [sore a = % [oad at

We can express the power per unit width (z direction) transmitted by
the aperture as

P= - I ” EH i)-ode = - I [BT yao dhe
From Eqs. (4-100) and (4-102), this becomes

~_ ve f* lis, _ _4 [* sin? (k.a/2)

P=-5 i i |B.) dks = a - kage Ue

PLANE WAVE FUNCTIONS 183 7%
4
TAT Ti Ts
= MN T E=1 )
*Fig. 4-22. Aperture ad- 2 BENENG am TE |*
mittance of a capacitive ) | TN | INwe | |
st ace PC Ne= PAR
1
LT TT NTT TY
Pi TT | RE
0 0.2 04 06 08 10
a/s
We now define the aperture admittance referred to the aperture voltage
V =aas
_ P* _ -4 [* sin? (k,a/2)
¥e= ro ie [2a ae
Note that, by Eq. (4-104), the above integrand is real for |k.| < k and
imaginary for |k.| > k. We can therefore separate Y, into its real and
imaginary parts as
k nz
G.= ve, sin? (k,a/2) dk.
Aya? J _y ky? Vk - ka?
4 he °\ sin? (k,a/2)
Be => + = -- dk,
os ae (2 i ave =e"
The above integrals can be simplified to give
ka/2 in?
MiG. = 2 i, sin? w dw
0 wr (ka/2)? - w?
7 a. (4-105)
sin? w dw
MBs = 2 i ao She do =
ka/2 W? Vw? - (ka/2)?
For small ka, these arely
(ka)?
» ws 1 - 2
Ga [ om $<o1 (4-106)
AB, ~ 3.1385 - 2 log ka
For intermediate ka, the aperture conductance and susceptance are
plotted in *Fig. 4-22. For large ka, we have*
1The formula for Bz is a quasi-static result. The direct specialization of the
second of Eqs. (4-105) to small ka gives a numerical factor of 4.232 instead of 3.135.

184 TIME-HARMONIC ELECTROMAGNETIC FIELDS
»
AnGa = x
A 25 (4-107)
ANB. = x 1-4 Peas (28 +2 | s
mee \ra 2Va x 4)*
The aperture is capacitive, since B, is always positive.

Another problem of practical interest is that of *Fig. 4-21 when the*
incident wave is in the dominant TE mode (TE to y). In this case,
E, will be the only component of E, and we shall take FE, as our scalar
wave function. Analogous to the preceding problem, we construct

R= a [ ” s(kadeteelw dk, (4-108)
In terms of Fourier transforms, this is
EB, = f(kz)e* (4-109)
From “the field equations, we find the transform of H to be
Aa She, a keg, (4-110)
oe wh
The f(kz) is evaluated by specializing Eq. (4-109) to y = 0, which gives
B.|_, = fe) = [7 Bue de (4-111)
For an approximate solution, we assume the /, in the aperture of *Fig.
4-21 to be that of the incident TE mode, that is,*
cos = |z] < 5
z,| ed a (4-112)
vo
0 |z| > 3
Substituting this into the preceding equation, we find
5 _ _ 2a cos (kza/2)
B,| = se) = sos ee) (4-113)
The choice of the root for ky is the same as in the preceding example,
given by Eq. (4-104). This completes the formal solution.

Let us again calculate the aperture admittance. The power trans
mitted by the aperture is
P= I ” [BH tlyods = i * [BLA 0 dhe
_ 2nr J-«
where we have used Parseval’s theorem. From Eqs. (4-110) and (4-113),

PLANE WAVE FUNCTIONS 185
0.8
CP, Doo
06 - see | | tt | er
0.4 E ers: (ex/a) oeda
LTT TTT TT Pri Ty yt
02 PL ve eft
[Peet tT TE tt tT
[Lie eT
Oo 0.5 1.0 15
a/
*Fig. 4-23. Aperture admittance of an inductive slot radiator.*
this becomes
-1 [ = -2ra? [* k* cos? (k,a/2)
DT. +H dk, = - ¥ 2! dk.
F 2rop [ KLE ak wh fm [n? - (k2a)?)? dk.
We shall refer the aperture admittance to the voltage per unit length of
the aperture, which is V = 1. This gives
_ P* _ -2na? [* k, cos? (kza/2)
Yen ipp tae ae
The integrand is real for |k.| < k and imaginary for |k.| > k. A separation
of Y, into real and imaginary parts is therefore accomplished in the same
manner as in the preceding example. The result is
7 1 [*/2 /(ka/2)? - w? cos? w
-G.=5 SNA dw
(@/2)* = wil (4114)
1p = =) [* Wut = lka/2)' cost w 4,
NOS 2 Seale (Gr/2)? - w}?
For small ka, we have 5
ca * 2 (3) a
" 5 <1 (4-115)
7 Ba = -0.194
For intermediate ka, the aperture conductance and susceptance are
plotted in *Fig. 4-23. For large ka,*
n a a
Z a =< 4-116
,%~ xR yrds ( )

186 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz

*Fig. 4-24. A sheet of z-di*
rected currents in the

y = 0 plane.

Y

x
and -B, is negligible. The aperture is inductive since B. is always
negative.

## Section 4-12: Plane Current Sheets
 The field of plane sheets of current can,

. of course, be determined by the potential integral method of Sec. 2-9.
We now reconsider the problem from the alternative approach of constructing transforms. The procedure is similar to that used in the preceding section for apertures. In fact, if the equivalence principle plus
image theory is applied to the results of the preceding section, we have
complete duality between apertures (magnetic current sheets) and electric current sheets. However, rather than taking this short cut, let us
follow the more circuitous path of constructing the solution from basic
concepts.

Suppose we have a sheet of z-directed electric currents over a portion
of the y = 0 plane, as suggested by *Fig. 4-24. The field can be expressed*
in terms of a wave function representing the z-component of magnetic
vector potential. (This we know from the potential integral solution.)
The problem is of the radiation.type, requiring continuous distributions
of eigenvalues. We anticipate the wave functions to be of the transform
type, such as Eq. (4-93). From Eqs. (3-86), we have the transforms of
the field components for the TM to z field, given by

A,= jh B= By

Ra =p 8,2 bey (4-117)
© = x que

- ad ke - k2

H,=0 E, = Fe y

PLANE WAVE FUNCTIONS 187
These are dual to Eqs. (4-95). We construct the transform of ¥ as
vt = fr(ke kev yy > 0
= Flkakowe - y <0 (£118)
For the proper behavior of the fields at large |y|, we must choose k,*,
as in Eq. (4-97), and ky as the other root. That is,
i 4/k2 +k? - bP ‘ht + he?
bt = -hy =e [PVR 8 k< Vike +h? (4 119)
-VE hehe k> VRP ERE
Our boundary conditions at the current sheet are continuity of Hz and
E,, and a discontinuity in H,, according to Eq. (1-86). The boundary
condition on E, and E, leads to ft = f-, and the boundary condition on
H, then leads to
H(kek.) = f(kak) = sho J. Iba) = FUkaske) = 505 Je (4-120)
where Js the transform of J,, is
Jaeaks) = f°, f°, Deeg)e re dt de (4-121)
This completes the determination of the field transforms. The field is
given by the inverse transformation.

Our two solutions (potential integral and transform) plus the uniqueness theorem can be used to establish mathematical identities. For
example, consider the current element of *Fig. 2-21. The potential integral solution is A = u,y where*

y= Ile"
Aur (4-122)
r=Vetyp re
For the transform solutipn,
J, = I16(x) 8(z)
a, = oat ica i J etete het dx dz = Jt
P An? Jin Joa” An?
Hence, for y > 0 we have A = u.y where
y= it L. c. Lette de dhe (4-123)
where k, = k,+ is given by Eq. (4-119). In this example, yas well as the

188 TIME-HARMONIC ELECTROMAGNETIC FIELDS
field is unique. Hence, equating Eqs. (4-122) and (4-123), we have
the identity
Fe oa ee
-_- = - ----- -- -- eteitse dk dk, (4-124)
ee A oe ee
This holds for all y, since k, changes sign as y changes sign.

We have considered explicitly only sheets of z-directed current. The
solution for z-directed current can be obtained by a rotation of coordinates. When the current sheet has both x and z components, the solution is a superposition of the x-directed case and the z-directed case. The
solution for magnetic current sheets is dual to that for electric current
sheets. Finally, if the sheet contains y-directed electric currents, we can
convert to the equivalent z- and z-directed magnetic current sheet for a
solution, and vice versa for y-directed magnetic currents.

A two-dimensional problem to which we shall have occasion to refer in
the next chapter is that of a ribbon of axially directed current, uniformly
distributed. This is shown in *Fig. 4-25. The parameter of interest to us*
is the ‘impedance per unit length,” defined by

P

Z= ip (4-125)
where P is the complex power per unit length and J is the total current.
Rather than work through the details, let us apply duality to the aperture
problem of *Fig. 4-22. According to the concepts of Sec. 3-6, the field*
y > 0 is unchanged if the aperture is replaced by a magnetic current
ribbon K = 2V. This ribbon radiates into whole space; so the power
per unit length is twice that from the aperture. The admittance of the

magnetic current ribbon is thus

Z Pe Pree ,
Y rnne rib = [KP 1 pve ba" wy apert
where the aperture admittance
as Yopet = Ga + jBa
is given by Eq. (4-105), which we can
y represent by :
Yapert = Pred
< By duality, we have the radiation imfs pedance of the electric current ribbon
Y" given by
ain _v

Fia. 4-25. A ribbon of current. Zocor = 2 x1 (ka) 2 Yao (4-126)

PLANE WAVE FUNCTIONS 189
(Compare this with Prob. 3-7. The factor-of-two difference arises
because the aperture of *Fig. 4-22 radiates into half-space and the twinslot line sees all-space.) For narrow ribbons, we have from Eqs. (4-106)*
and (4-126)
2 :
Zeroo rio roe) dy [rt + j(3.135 - 2 log ka)} (4-127)
This we shall compare to the corresponding Z for a cylinder of current in
Sec. 5-6.
PROBLEMS

## Section 4-1: Show that Eq
 (4-9) is a solution to the scalar Helmholtz equation.

## Section 4-2: For k = 8 - ja, show that
sin kz = sin 8z cosh ax - j cos @z sinh ax
cos kz = cos 6x cosh ax + j sin Bz sinh at

4-3
 Derive Eqs. (4-17).

4-4, Following the method used to establish Eq. (2-93), show that the attenuation
constant due to conductor losses in a rectangular waveguide is given by Eq. (2-93)
for all TEo, modes and by

= 2H PED 4 {FG bm? + ant
(oom = [55 Vi- Ua Vi- (Oi: on
for TEm, modes, m and n nonzero, and by
(cxe)mn = -- 2_ mtb + ntat
nab Jt - (f/f)? mb? + na?
for TMmn modes.

## Section 4-6: An air-filled rectangular waveguide is needed for operation at 10,000 megacycles
 It is desired to have single-mode operation over a 2:1 frequency range, with
center frequency 10,000 megacycles. It is also desired to have maximum powerhandling capacity under these conditions. Determine the waveguide dimensions and
the attenuation constant of the propagating mode for copper walls.

## Section 4-6: For a parallel-plate waveguide formed by conductors covering the y = 0 and
y = b planes, show that {

YntE = cos EY erite n=1,2,3,
..
are the mode functions generating the two-dimensional TE, modes according to Eqs.
(3-89), and
vn™ = sin a evike on 1,2,3,...
are the mode functions generating the two-dimensional TM, modes according to Eqs.
(3-86). Show that the TEM mode is generated by
oTM = yernike

190 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 4-7: Show that an alternative set of mode functions for the parallel-plate waveguide of Prob
 4-6 are
YaTF* = cos me en ike n=0,1,2,...
which generate the TEz, modes according to Eqs. (4-32), and
UnTMe = sin SY erie n=1,2,3,...
which generate the TMz, modes according to Eqs. (4-30). Note that n = 0 in the
above TEz mode function gives the TEM mode.

## Section 4-8: Show that the TEz and TMz modes of Sec
 4-4 are linear combinations of the
TE and TM modes of Sec. 4-3, that is,

Emnt®* = A(Emn™® + BEmn™)
Hra™? = C(HmnT® + DHmn™)
Determine A, B, C, and D.

4-9, Show that the resonant frequencies of the two-dimensional (no z variation)
resonator formed by conducting plates over thez = 0,z = a, y = 0,and y = b planes
are the cutoff frequencies of the rectangular waveguide.

## Section 4-10: Following the method used to establish Eq
 (2-101), show that the Q due to
conductor losses for the various modes in a rectangular cavity are

@ ye = nabck,?
clone 2R(bek,? + acky? + 2abk.2)
TE nabck,?
(Qe)mop = 557 a OPP a
2 (ack,? + 2bck,? + 2abk.?)
(Qt, = nabekeythe?
Sime?" AR[bc(kay* + kythe*) + ac(key* + hatha?) + abkey*k,?]
™ nabck,®
(Q)nno = 5a OF 8 ot Oey
2A(abk,? + 2bek.? + 2ack,?)
(Qo™, = nabckzy*k,
simn? 4gib(a + c)kz? + a(b + c)ky?)
plied ani = 2
where ke = = ky D ke c
key = Vit hy? ke = VE +R

## Section 4-11: Calculate the first ten higher-order resonant frequencies for the rectangular
cavity of Prob
 2-38.

## Section 4-12: Consider the two-dimensional parallel-plate waveguide formed by conductors
over thez = Oandz = aplanes, and dielectrics e: forO < z < dandezford <z <a

Show that for modes TM to z the characteristic equation is Eq. (4-45) with

her = Vote - ke ker = Vootenua - Ta?
and for modes TE to z the characteristic equation is Eq. (4-47). Note that no mode
TEM to z (the direction of propagation) is possible.

PLANE WAVE FUNCTIONS 191

## Section 4-13: Show that the lowest-order TM to z mode of Prob
 4-12 reduces to the
transmission-line mode either as « - « and yi-> we or as d+ 0. Show that, if
aX,

wy afselnd + n2(a - d)}
. a(a -d) + ed
for the dominant mode. Show that the static inductance and capacitance per unit
width and length of the transmission line are
= iz eae) Cases

L = wid + u:(a - d) Cc aan dsb
The usual transmission-line formula k, = w \/£C therefore applies if a is small.
Also, the field is almost TEM.

## Section 4-14: Consider the dominant mode of the partially filled guide (Fig
 4-6) for b > a.
When d is small, Eq. (4-45) can be approximated by Eq. (4-48) for the dominant
mode. Denote the empty-guide propagation constant (d = 0) by

at, . ee
= Ajkt = (5
po = Aka (;)
and show, from the Taylor expansion of Eq. (4-48) about d = 0 and k, = Bo, that for
small d
= eo (ka? - ka®\ d
lel aired aera

## Section 4-15: Consider the dominant mode of the partially filled guide (Fig
 4-6) fora > b.
Denote the empty-guide propagation constant (d = 0) by
a
Bo = Wks? - (:)
and show, from the Taylor expansion of the reciprocal of Eq. (4-47) about d = 0 and
k, = Bo, that for small d
= wim (a\Pd | wr (2)
hy = Bo + oS (2) o + Ee et - be) (5

## Section 4-16: Show that the resonant frequencies of a partially filled rectangular cavity
(Fig
 4-6 with additional conductors covering the z = 0 and z = c planes) are solutions to Eqs. (4-45) and (4747) with

kat + (#)’ + (2) = ht
6 c
24 (ney 4 (BE) = ky
ket +(¥) +(®) ks
wheren = 0,1,2,...;p =0,1,2,...3;n = p = 0 excepted.

## Section 4-17: For the partially filled cavity of Prob
 4-16, show that if c > b >a, the
resonant frequency of the dominant mode for small d is given by

lfm _ a |
ba =eo[1 ale =

192 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where wo is the resonant frequency of the empty cavity,
oa MCs) +)
oo = --- 5) +{Vem: b c
Hint: Use the results of Prob. 4-14.

## Section 4-18: For the partially filled cavity-of Prob
 4-16, show that if c >a > b, the

resonant frequency of the dominant mode for small d is given by
= [1-828 a dye (at - 1) d ‘|
eo 0 we a +c?a Buz \erme a

where wo is the resonant frequency of the empty cavity

van MG) +)

oo = = pd Hatta ol (oo

Vem V\a c
Hint: Use the results of Prob. 4-15.

## Section 4-19: Consider a rectangular waveguide with a centered dielectric slab, as shown in
the insert of Fig
 7-10. Show that the characteristic equation for determining the
propagation constants of modes TE to z is

kz a--d\ _ka ( d
“cot (es 134) =n tan ( kat 3
and for modes’ TM to z it is
ke tan (ko 9) = Fe cot (ta )
€0 2 a 2
no\*
where haat + (FE)! + het = het = wean
2
ka? + (¥) bk? = hat = wes
The dominant mode is the lowest-order TE mode (smallest root for n = 0).

## Section 4-20: Derive Eq
 (4-58).

## Section 4-21: A plane slab of polystyrene (er = 2
56) is 34 centimeter thick. What slabguide modes will propagate unattenuated at a frequency of 30,000 megacycles? Calculate the cutoff frequencies of these modes. Using *Fig. 4-11, determine the propagation constants of the propagating TE modes at 30,000 megacycles. Determine the*
propagation constants of the propagating TM modes by numerical solution of Eq.
(4-56) or (4-58). How can the cutoff frequencies of corresponding TE and TM modes
be the same, yet the propagation constants be different?

## Section 4-22: By a Taylor expansion of Eq
 (4-56) about a = 0, v = 0, show that the
dominant TM mode of the slab guide (*Fig. 4-10) is characterized by*

= (Es - 5) 2
ye (ka? - ko?) 3
for small a. Similarly, show that the dominant TE mode is characterized by
=“ Ke - Kye
st (ka? - ko) 3

PLANE WAVE FUNCTIONS 193
forsmalla, In each case, the propagation constant is given by
v?
ke = ko + Bo

## Section 4-23: A plane conductor has been coated with shellac («, = 3
0) to a thickness of
0.005 inch. It is to be used in a 30,000-megacycle field. Will any tightly bound
surface wave be possible? Calculate the attenuation constant in the direction perpendicular to the coated conductor.

## Section 4-24: For the corrugated conductor of Fig
 4-15, it is desired that the field be
attenuated to 36.8 per cent of its surface value at one wavelength from the surface.
Determine the minimum depth of slot needed.

## Section 4-25: Suppose that the slots of the corrugated conductor of Fig
 4-15 are filled
with a dielectric characterized by ea, na. Show that for this case

v = ky tan kad
€4
ky = ko Vi + S$ tan? kad
auto
where kg = w Vana.

## Section 4-26: Use the TEx mode functions of Prob
 4-7 for the parallel-plate waveguide
formed by conductors covering the y = 0 and y = b planes. Show that a field having
no E, is given by Eqs. (4-32) with

y= » A, cos "FY e-1at 2>0
n=0
_awen b ney
where A, Ts I, B,|_ 008 5 dy

## Section 4-27: Consider the junction of two parallel-plate transmission lines of height c for
z <0 and height b for z > 0, with the bottom plate continuous
 (The cross section
is that of the second drawing of *Fig. 4-16.) Using the formulation of Prob. 4-26,*
show that the aperture susceptance per unit width referred to the aperture voltage is

pwd ) sin? (nze/b)
a possess Soni 077 Aaa
Wr Ly, (nee/b)? Vat - (2b/d)*
where a constant E, has been assumed in the aperture. Compare this with Eq. (4-78).

## Section 4-28: The centered capacitive waveguide junction is shown in Fig
 4-26. Show
that the aperture susceptancg referred to the maximum aperture voltage is given by
Eq. (4-78) with 4, replaced ty 2d). It is assumed that Ey, in the aperture is that of
the incident mode.

Ay Incident AY
wave
aT +t
+
he cb
9 ee ares bi cee
< >
| Zz
*Fig. 4-26. A centered capacitive waveguide junction*

194 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Ax hal
=x. |
T 5 Incident
>

if = wave

[L es Sea ee
-&-b- Zz

*Fig. 4-27. A centered inductive waveguide junction.*

## Section 4-29: Consider the centered inductive waveguide junction of Fig
 4-27. Assuming
that FE, in the aperture is that of the incident mode, show that the aperture susceptance referred to the maximum aperture voltage is given by

©
RB -8r (:)' y [e (neat m\? a\?
20) [Pes eo
wd \al ot (me/a) 2 r

4-30, In Eq. (4-83), note that as c/a- 0 the summation becomes similar to an

integration, Use the analogy mc/a ~ z and c/a ~ dz to show that
bn Lf? fsinwe\*
Fran le (FYE) ee
Integrate by parts, and use the identity!
esin 2rz, _ f2rsiny, _
fp Bee a = i SRY dy = Si(2r)
to show that - tp, + SIZ") _ 9.206
» c/a>0 Qn

## Section 4-31: Let there be a sheet of y-directed current J, over the z = 0 plane of a parallelplate waveguide formed by conductors over the y = O and y = b planes
 The guide
is matched in both the +z and -z directions. Show that the field produced by the
current sheet is

. H
REY eral = { 7 z>0
J, An cos "Fe id _H. 2<0
n=0
aif? nay
where An = sf, Jy(y) cos B dy

## Section 4-32: Let the current sheet of Prob
 4-31 be z-directed instead of y-directed. Show
that field produced by this z-directed current sheet is
E.= ») Ba sin 7EY orale
n=l
je b
he = Jeon f -(y) sin 27
where Ba yb Jo J.(y) sin ; dy

1D. Bierens de Haan, “Nouvelles tables d’int'grales d'finies,” p. 225, table 161,

no. 3, Hafner Publishing Company, New York, 1939 (reprint).

PLANE WAVE FUNCTIONS 195

## Section 4-33: Consider the coax to waveguide junction of Fig
 4-28a. Only the TEo: mode
propagates in the waveguide, which is matched in both directions. Assume that the
current on the wire varies as cos (kl), where / is the distance from the end of the wire.
Show that the input resistance seen by the coax is
_a sin (c/b) sin my
Re = § Zon | eae ke Fa)
where (Zo)o1 is the TEo: characteristic wave impedance.
x xX
_-- b
. T T
a a
cy
d d
aa He
k#-e- * f-e Coax
(a) (b)
*Fig. 4-28. Coax to waveguide junctions.*

## Section 4-34: Suppose that the coax to waveguide junction of Prob
 4-33 is changed to
that of *Fig. 4-28b. Show that the input resistance seen by the coax is now*
_@ sin (rc/b)[sin k(c +d) - sin nel}?
Ri = 5 Zodor { ka cos k(c + d)

## Section 4-35: By expanding (sin w/w)? in a Taylor series about w = 0, show that the first
of Eqs
 (4-105) becomes
1 (ka\? 1 (ka\* 1 ka\®
me = [1-9 (E)' + 66(S) - 00s (Z) + > ‘|
Im

## Section 4-36: Consider the second of Eqs

(4-105) as the contour integral w plane
f Ces
AB, = Re [ i) Sl C
C1 w? y/w? - (ka/2)?
where C, is shown in *Fig. 4-29. Consider*
the closed contour C; + C2 +C, + Co, R
and express \7B. in terms of a contour ka/2 CQ e
integral over Cz; and Co. Show that as
ka/2 becomes large, this last contour
integral reduces to the second of Eqs.
(4-107).
Fie. 4-29. Contours for Prob. 4-36.

196 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 4-37: By expanding cos? w/[(x/2)? - w?]? in a Taylor series about w = 0, show
that the first of Eqs
 (4-114) becomes
1g, =2 a\"
2c.-2 ¥ 0,(2)
n=l
where b = +1.0
b: = -0.467401
bs = +0.189108
b, = -0.055613
bs = +0.012182
bs = -0.002083

## Section 4-38: Specialize the second of Eqs
 (4-114) to the case a = 0, integrate by parts,
and use the identity (see Prob. 4-30)
e sin2zdz _2 f*siny, _2,.
iF Gt at ah vy 8)
a le 2
to show that, x Bo a, Si@) -aA= 0.194

## Section 4-39: Show that the first of Eqs
 (4-114) reduces to the contour integral
a ka (1 + ei) dw
1G aes Rel [ote we]
where C; is shown in Fig, 4-30. Consider the closed contour Ci; + C2 + C,, + Co,
and express G, in terms of a contour integral over C, and Cy. Evaluate this last
contour integral, and show that
” ka
0 Gane de
Im x
Coo
w plane
C2
TT
ie i
Y
a
ve 4
a 7/2 Re |
Fie, 4-30. Contours for Prob. 4-39. *Fig. 4-31. Two parallel-plate transmission lines radiating into half-space.*

## Section 4-40: Two parallel-plate transmission lines opening onto a conducting plane are
excited in opposite phase and equal magnitude, as shown in Fig
 4-31. Assume E; in

PLANE WAVE FUNCTIONS 197
the aperture is a constant for each line, and show that the aperture susceptance
referred to the aperture voltage of one line is

g.=-2% 3 5

“da Jo wt (ka)? - w?

B, <8 fc sint w dw

° dn Jeg w/w? - (ka)?

## Section 4-41: Construct the vector potential A = u,y for a sheet of z-directed currents
over the y = 0 plane (Fig
 4-24) by (a) the potential integral method and (b) the
transform method. Show by use of Green’s second identity [Eq. (3-44)] that the
two y’s are equal. Specialize the potential integral solution to r+ ©, and show that

oP Tok i k
> Fe =
v 2 Ge e( cos c sin 6, cos 6)
where J,(kz,k.) is given by Eq. (4-121).

## Section 4-42: Suppose that the current in Fig
 4-25 is z-directed rather than z-directed,
and of magnitude
J. = me a
cos Iz] < 3
Show that the impedance per unit length, defined by Eq. (4-125), where J is the
current per unit length, is given by Eq. (4-126), where Yapert is now the aperture
admittance of *Fig. 4-23.
i*



---

## Chapter 5: Cylindrical Wave Functions

CYLINDRICAL WAVE FUNCTIONS

## Section 5-1: The Wave Functions
 Problems having boundaries which coincide with cylindrical coordinate surfaces are usually solved in cylindrical
coordinates.! We shall usually orient the cylindrical coordinate system
as shown in *Fig. 5-1. We first consider solutions to the scalar Helmholtz*
equation. Once we have these scalar wave functions, we can construct
electromagnetic fields according to Eqs. (3-91).
The scalar Helmholtz equation in cylindrical coordinates is
la oy 1 ay, ay _
ed ee (5-1)
which is Eq. (2-7) with the Laplacian expressed in cylindrical coordinates. Following the method of separation of variables, we seek to find
solutions of the form
¥ = R(p)&(4)4(z) (5-2)
Substitution of Eq. (5-2) into Eq. (5-1) and division by ¥ yields
1 d/ dR ld@d, 1@Z 2
wee (0S) + aoe ea, =0
The third term is explicitly independent of p and c. It must also be
independent of z if the equation is to sum to zero for all p, c,2. Hence,
1dZ §

Z ae ~ -* (5-8)
where k, is a constant. Substitution of this into the preceding equation
and multiplication by p? gives

PL a aR 1 Ph 2 2) 52 . Rage) tant kp = 0
Now the second term is independent of p and z, and the other terms are
+The term “cylindrical” is often used in a more general sense to include cylinders
of arbitrary cross section, We are at present using the term to mean “circularly
cylindrical.”

CYLINDRICAL WAVE FUNCTIONS 199
independent of c. Hence, 2
1d?6
gag" A) e
where n is a constant. The pre- z
ceding equation then becomes
oS x
pad dk). 2 fp.%)p? = oN
ba (0 Se) - w+ (8 baer = 0
(5-5)
tae wo. Fia. 5-1. Cylindrical coordinates.
which is an equation in p only.
The wave equation is now separated. To summarize, define k, as
k,? + k? =k (5-6)
and write the separated equations (Eqs. (5-3), (5-4), and (5-5)] as
d/( dk
-_> - 2 2 =
o£ (0S) + ee)? - mk = 0
2
_ + ne =0 (5-7)
BZ
dz? +k2Z=0
The © and Z equations are harmonic equations, giving rise to harmonic
functions. These we denote, in general, by hae and h(k.z). The R
equation is Bessel’s equation of order n, solutions of which we shall denote
in general by B,(k,p).1_ Commonly used solutions to Bessel’s equation
are
Balkop) ~ Inlkop)s Nalkop), Ha‘? (kop), Hn (kop) (5-8)
where J,(k,p) is the Bessel function of the first kind, Nn(k,p) is the
Bessel function of the second kind, H,“”(k,p) is the Hankel function of
the first kind, and H,”(k,p) is the Hankel function of the second kind.
These functions are considered in some detail in Appendix D, and we
shall discuss them later in this section. Any two of the functions of Eq.
(5-8) are linearly independent solutions; so B,(k,p) is, in general, a linear
combination of any two of them. According to Eq. (5-2), we can now
form solutions to the Helmholtz equation as
Vipna, = Ballop)h(rXp (kez) 6-9)
1 It is more usual to denote solutions to Bessel’s equation by Z,(kpp), but we wish to
avoid confusion with our Z(z) function and with impedances,

200 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where k, and k, are interrelated by Eq. (5-6). We call these y elementary
wave functions, =
Linear combinations of the elementary wave functions are also solutions to the Helmholtz equation. We can sum over possible values
(eigenvalues) of n and k,, or of n and k, (but not over k, and k, for they
are interrelated). For example,
y= > » Cae Wr penis
n ke
= VY Cor Balkop)h(nd)h (haz) (5-10)
n ke
where the C,,x, are constants, is a solution to the Helmholtz equation.
We can also integrate over the separation constants, although n is usually discrete (this is discussed below). We shall, however, have occasion
to integrate over either k, or k,. Thus, possible solutions to the Helmholtz equation are
v=), fi Salk) Balkoo)h(nd)h (liz) di, (5-11)
fn
¥ =D fi, 9n(ee)Ba (op) h (ng )R(ks2) dle (5-12)
Ly Ske
where the integrations are over any contour in the complex plane and
fn(kz) and gn(k,) are functions to be determined from boundary conditions. We shall use Eq. (5-11) to construct Fourier integrals, as we did
inChap.4. Equation (5-12) is used to construct Fourier-Bessel integrals.

We discussed the interpretation of the harmonic functions in Sec. 4-1,
a summary being given in Table 4-1. The z coordinate of the cylindrical

: coordinate system is also one of the rectangular coordinates; so the same
considerations that dictated the choice of A(k.z) in Chap. 4 apply at
present. The c coordinate is an angle coordinate and, as such, places
restrictions on the choice of h(nc) andn. For example, if we desire the
field in a cylindrical region containing all c from 0 to 2z, it is necessary
that ¥(c) = ¥(c + 2m) if w is to be single-valued. This means that
h(nc) must be periodic in c, in which case n must be an integer. In
most cases, we choose sin (nc) or cos (nc) or a linear combination of the
two, although in some cases the exponentials e’** and e~i** are more
descriptive, or easier to deal with analytically. Thus, the n summations
of Eqs. (5-10) to (5-12) are usually Fourier series on c.

Now, consider the various solutions to Bessel’s equation. Graphs of
the lower-order Bessel functions are given in Appendix D. We note that
only the J,(k,p) functions are nonsingular at p = 0. Hence, if a field is
to be finite at p = 0, the B,(k,p) must be J,(k,p), and the elementary

CYLINDRICAL WAVE FUNCTIONS 201
wave functions are of the form
Vipnks = In(kpp)einters p = O included (5-18)
We have written the harmonic functions in exponential form, which is
still general since sines and cosines are linear combinations of them.
Note from Eq. (5-6) that k, = + Wk? -k,? is indeterminate with
respect to sign. Our convention will be to choose the root whose real
part is positive, that is, Re (k,) > 0.1 Now consider the asymptotic
expressions for the various solutions to Bessel’s equation [Eqs. (D-11)
and (D-13)]. Note that H,®(k,p) are the only solutions which vanish
for large p if k, is complex. They represent outward-traveling waves if
k, is real. Therefore, if there are no sources at infinity, the B,(k,p) must
be H,(k,p) if p- © is to be included. Hence, the elementary wave
functions become
pak, = Hp (Kpp)emtertt p- © included (5-14)
Other choices of cylinder functions are convenient in certain cases, as we
shall see when we apply them.

Insight into the behavior of solutions to Bessel’s equation can be gained
by noting their similarities to harmonic functions. It is evident from the
asymptotic formulas of Appendix D that, except for an attenuation of
1/Vkp, the following qualitative analogies can be made:

J.(kp) analogous to cos kp
N (kp) analogous to sin kp
H,(kp) analogous to e** (5-15)
H,(kp) analogous to e~#
For example, J, and N,, exhibit oscillatory behavior for real k, as do the
sinusoidal functions. Hence, these solutions represent cylindrical standing waves. The H, and H, functions represent traveling waves for
k real, as do the exponential functions. They therefore represent cylindrical traveling waves, H,‘ representing inward-traveling waves and
H, representing outward-traveling waves.? If k is complex, the traveling waves are attenuated or augmented in the direction of travel (in
addition to the 1/-/kp factor). When k is imaginary (k = -ja), it is
conventional to use the modified Bessel functions I, and K,, defined by
In(ap) = j*Sn(-Jap)
P : 5-16
K (ap) = 3 (-i)*H(-fap) 6-19)

1 If kp isimaginary, choose the root according to the limit Im (k) > 0.

* This direction of wave travel is a consequence of our choice of e# time variation.
If we had initially chosen ei‘, then our interpretation of H,‘ and H,) would be
reversed.

202 TIME-HARMONIC ELECTROMAGNETIC FIELDS
These are real when ap is real. From their asymptotic behavior, Eqs.
-(D-19), it is evident that we have the qualitative analogies

I,(ap) analogous to ev? (5-17)

K,(ap) analogous to e~7*

From these it is apparent that the modified Bessel functions are used to
represent evanescent-type fields. That the various analogies of Eqs.
(5-15) and (5-17) exist is no coincidence. Both Bessel’s equation and
the harmonic equation are specializations of the wave equation. In the
case of waves on water, a dropped stone would give rise to ‘‘Bessel function’’ waves, while the wind gives rise to “harmonic function”’ waves.

Table 5-1 summarizes the properties of solutions to Bessel’s equation.
Our understanding of the physical interpretation, given in the last column, will increase as we apply the various functions to specific problems.
When k = 0, we have the degenerate Bessel functions

Bo(0p) ~ 1, log p

B,(O0p)~ p",e* = n#0
Note that these are essentially the small-argument expressions for J»
and JN,,.

To express an electromagnetic field in terms of the wave functions y,
the method of Sec. 3-12 can be used. The unit z-coordinate vector is a
constant vector; so we can obtain a field TM to z by letting A = up
and expanding Eqs. (3-85) in cylindrical coordinates. The result is

_1 ay la
Bo 5 ap a2 He = 7 a6
1 ay oy
=e =-@ 1
By Fp 36 02 Hy 2p (5-18)
B,-1(24\y H,=0
* 9 \az?
which are sufficiently general to express any TM (no H,) field existing in
a homogeneous source-free region. Similarly, we can obtain a field TE
to z by letting F = u,y and expanding Eqs. (3-88) in cylindrical coordinates. The result is
= 1% -1 oy
Ey = p od H, = 2 dp dz
=o = eer 5-19
Be= a, Hs = 5 a6 a2 ( )
E,=0 iH, = 7 a +k )p
* 8 \a2?

g
ry g 3 i
3 2 |
a 7. £ 3 i
2 = a w 3 ®
ane z 3 2 z 8
a > 3 3 3 g : Z
$32): 3 5 i 3 id
a 3 3 ' 3 3 i af i i
g Boa &§ a 3 2 . 8 ‘ : i
3 : > 3 Jil,
Paeiyi gd po ye 3 i
Z 3 i ;
3 8 3 2 § &, Pp ae :
8 2 2 2. = FS 2% £ 7 3g i
pata b # ae lle og |
ao iT Be £ > L fe dle }
gos 1 fF 3 2 3 - 3 5/7 4 |
5B BBs a 2 tel a
* Teali ' ei? ali? i
“ani la £ 8 EE
28 c | € & B' |
se fe :
r a : .
= :
% 5 2
‘ 1 2 a 2
i i : : : ; 2 2 2 3
: : = 3
: A 2 = 2 = ;
‘ - - 3 23a" =
Z i 5 FA 2 aD 3.
- sagt Safes =
: Bess | 28223 :
°° & gaze. adi. :
: 1 i eae 6 a i
c s 3
= ; : Pr) ae T
: ; v 1 kia
1
a : =
: kaw : !
2 . :
: 3 :
8 o 7
gai j i.
i} ba .
53 : : , : c
H : : Ts ay
B Fs f 2 i. A ai
£3 if & a
g FB als al? lel zak 2
i “ Bs
B aa ; i
:
io} o o A ° . n ° A A : . i
fe an ' uy
~ “Ty . foe
2 26 - i
a a _ =.
& 8 a > 1? ° ° > - i
& 8 3 £12 als ' : ° an 3, 38
poi 22] 28 Ry) bt of | elt Ns 23
fg OES g _ 8 g\k¥ 7 8
a4 rare F : 7:
74 ee “un Ts sito Sl 33
a as “ik ! an ao si ;
: 7 lz + S|& « $ = x8
Y alE + $ - 7
~ 3 = a ry
4g “ : ; :
a 3 3 7
< : I
a
3 = 7
P am 3 : : fr
Hl : ‘ s = 33
| : : z = rs
; g 5 = 1 1
“ g 5 3 ale at
: = $ : i
& = Li
s * : ii
: ' = * 3 3 3 3
3 g : 3 3
= = 3
. * 203

204 TIME-HARMONIC ELECTROMAGNETIC FIELDS

-which are sufficiently general to express any TE (no £,) field existing in
a homogeneous source-free region. An arbitrary field (one having both
an E, and an H,) can be expressed as a superposition of Eqs. (5-18) and
(5-19).

## Section 6-2: The Circular Waveguide
 The propagation of waves in a hollow
conducting tube of circular cross section, called the circular waveguide,
provides a good illustration of the use of cylindrical wave functions.
Qualitatively, the phenomenon is similar to wave propagation in the
rectangular waveguide, considered in Sec. 4-3. The coordinates to be
used are shown in *Fig. 5-2.

For modes TM to z, we may express the field in terms of an A having*
only a z component y. The field is finite at p = 0; so the wave functions must be of the form of Eqs. (5-13). It is conventional to express
the c variation by sinusoidal functions; hence

_ sinnc| _., 7
= Jatlae) {32 28 ea (5-20)
is the desired form of the mode functions. Either sin nc or cosnc may
be chosen; so we have a mode degeneracy except for the cases n = 0.
The TM field is found from Eqs. (5-18) applied to the above y. In
particular,
1
EB, = (k? - ke)y

9
which must vanish at the conducting walls p = a. Hence, we must have
Jnr(kpa) = 0 (5-21)
from which eigenvalues for k, may be determined. The functions J,(z)
are shown in Fig. D-1. Note that for each n there are a denumerably
infinite number of zeros. These are ordered and designated by yy, the

x
zZ
Fie. 5-2. The circular
waveguide,
D>
[7 Y

CYLINDRICAL WAVE FUNCTIONS 205
Tasie 5-2. ORDERED ZEROS Znp OF J,(2)
0 1 2 3 4 5
1 2.405 3.832 5.136 6.380 7.588 8.771
2 5.520 7.016 8.417 9.761 11.065 12.339
3 8.654 10.173 11.620 13.015 14.372
4 11.792 13.324 14.796
first subscript referring to the order of the Bessel function and the second
to the order of the zero. The lower order z,, are tabulated in Table 5-2.
Equation (5-21) is now satisfied if we choose
k, =" (5-22)
a
Substituting this into Eq. (5-20), we have the TM,, mode functions
™ = Znpp\ |sinnd\ a,
vam = Ja (Fur?) [30 08 (6-23)
wheren = 0,1,2,...,andp=1,2,3,.... The electromagnetic
field is then determined from Eqs. (5-18) with the ebove y. The mode
phase constant k, is determined according to Eq. (5-6), that is,
+k? =k?! (5-24)
Subscripts np on the k, are sometimes used to indicate explicitly that it
depends on the mode number.

Modes TE to z are expressed in terms of an F having only a z component y. This wave function must be of the form of Eq. (5-20), with the
field determined by Eqs. (5-19). The Z, component is dy/dp, which must.
vanish at p = a; hence the condition

Ji(k,a) = 0 (5-25)
must be satisfied. The J, are oscillatory functions; hence, the J‘, also
are oscillatory functions. (For example, Jj = -J1.). The J/(z) have
a denumerably infinite number of zeros, which we order as xj,. (The
prime is used to avoid confusion with the zeros of the Bessel function
itself.) The lower-order zeros are tabulated in Table 5-3.

Tae 5-3. ORDERED ZEROS z,, oF J,(2’)
1} 1 2 3 4 5
1 3.832 1.841 3.054 4,201 5.317 6.416
2 7.016 5.331 6.706 8.015 9.282 10.520
3 10.173 8.536 9.969 11.346 12.682 13.987
4 13.324 11.706 13.170

206 TIME-HARMONIC ELECTROMAGNETIC FIELDS
We now satisfy Eq. (5-25) by choosing
Zy
k, = =e (5-26)
Using this in the wave function of Eq. (5-20), we have the TE,, mode
functions
w’,,p\ {sinnd) _
TE = ZnpP ik, =
np Ja( i ) (snrsl € (5-27)
wheren = 0,1,2,...,and p=1,2,3,.... The electromagnetic
field is given by Eqs. (5-19) with the above y. The mode propagation
constant is determined by Eq. (5-6), which with Eq. (5-26) becomes
tee\?
(2) +k? = k? (5-28)
This completes our determination of the mode spectrum for the circular
waveguide.

The interpretation of the mode propagation constants is the same as
for those of the rectangular guide and, in fact, is the same for all cylindrical guides of arbitrary cross section if the dielectric is homogeneous.
(This we show in Sec. 8-1.) The cutoff wave number of a mode is that
for which the mode propagation constant vanishes. Hence, from Eqs.
(5-24) and (5-28), we have

In zi,
(ke)np™ = a2 (ke)np™ = =e (5-29)
If k > k., the mode propagates, and if k < k. the mode is cutoff. Letting
k. = Inf. Ven, we obtain the cutoff frequencies
™ - __7nap (fag = np = 5-30
(fe)np na Vea Je)np Ona Ven (5-30)
Alternatively, setting k, = 2r/A,., we obtain the cutoff wavelengths
2ra 2ra
™ - “7% te = 27" (Ac) np = (Ac)ne Zz, (5-31)
Thus, the cutoff frequencies are proportional to the z,, for TM modes,
and to the 2), for the TE modes. Referring to Tables 5-2 and 5-3, we
note that the zeros in ascending order of magnitude are x41, 201, £21, C11)
and 2, etc. Hence, the modes in order of ascending cutoff frequencies
are TEn, TMo, TEn, TMi, and TEo: (a degeneracy), etc.

Circular waveguides are used in applications where rotational symmetry is needed. The dominant TE; “mode” is actually a pair of
degenerate modes (sin c and cos c variation) ; hence there is no frequency

CYLINDRICAL WAVE FUNCTIONS 207
(a) TE (6) TMor (c) TEa
SEN ee
a fi ws ie
He) (CC) Exe
UH CID BOY
NEADS ais yay
LASS LAS
(d@) TMi () TEx (f) [Mar
e-> K--*Fig. 5-3. Circular waveguide mode patterns.*
range for single-mode propagation. (Recall that single-mode operation
over a 2:1 frequency range is possible in the rectangular waveguide.)
Note that, except for the degeneracies between TEo, and TMi, modes,
TE and TM modes have different cutoff frequencies and hence different
propagation constants. The modes of the circular waveguide have
z-directed wave impedances of the same form as we found in the rectangular waveguide. For example, in a TE mode,
E, E. 2)
TE ee a - $9 Oe
(Zo) H, He ~ i (5-32)
which is the same as Eq. (4-27). The behavior of the Zy’s is therefore
the same as in the rectangular waveguide, which is plotted in *Fig. 4-3.
Attenuation of waves in circular waveguides due to conduction losses in*
the walls is given in Prob. 5-9. Modal expansions in circular waveguides
can be obtained by the general treatment of Sec. 8-2.

The mode patterns for some of the lower-order modes are shown in
*Fig. 5-3. These can be determined in the usual manner (find & and 3,*
and specialize to some instant of time). Field lines ending in the crosssectional plane loop down the guide, in the same manner as they did in
the rectangular waveguide.

Solutions for cylindrical waveguides of other cross sections also can be
expressed in terms of elementary cylindrical wave functions. Representative cross sections are shown in *Fig. 5-4. Note that all of these*

208 TIME-HARMONIC ELECTROMAGNETIC FIELDS
(0) }
(a) (6) (c)
= ZX |
@) (e) 2)
Fie. 5-4. Some waveguide cross sections for which the mode functions are elementary
wave functions. (a) Coaxial; (b) coaxial with baffle; (c) circular with baffle; (d) semicircular; (e) wedge; (f) sectoral.
are formed by conductors covering complete p = constant and c = constant coordinate surfaces. Wave functions for the guides of *Fig. 5-4 are*
given in Probs. 5-5 to 5-7.

## Section 6-3: Radial Waveguides
 In the circular waveguide we have plane
waves, that is, the equiphase surfaces are parallel planes. Wave functions of the form

V = Balkpp)h(kezleurt
with B,(k,p) and h(k,z) real, have equiphase surfaces which are intersecting planes (the c = constant surfaces). Such waves travel in the
circumferential direction, and we shall call them circulating waves.
Examples are given in Prob. 5-10. Finally, we might have wave functions of the form
H, (kp)

y = h(kz)h(ng) { H.(kep)
with h(k,z) and h(n@) real. These waves have cylindrical equiphase surfaces (p = constant), and travel in the radial direction. We shall call
them radial waves.! In this section some simple waveguides capable of
guiding radial waves will be considered.

Radial wavescan besupported by parallel conducting plates. Depend
1 These are true cylindrical waves as defined in Sec. 2-11, but we are using the term
“cylindrical wave function” to mean “a wave function in the cylindrical coordinate
system,” regardless of its equiphase surfaces.

CYLINDRICAL WAVE FUNCTIONS 209
Zz Z
a
z Y
Le a a L|
@) “x c|> //
Lee $0 x
Pras, ae $ alt ™~y
(6) (c)
Fie. 5-5. Radial waveguides. (a) Parallel plate; (b) wedge; (c) horn.
ing upon the excitation, waves between the plates may be either plane or
radial. When the waves are of the radial type, we call the guiding plates
a parallel-plate radial waveguide. Figure 5-5a shows the coordinate system we shall use. The TM wave functions satisfying the boundary conditions Z, = E, = 0 atz = 0 and z =a are
™ mn Hy‘ (kp) Wn cos ( 7 2) cos nd a (5-33)
where m=0,1,2,... ,and n=0,1,2,..., and, by Eq. (5-6),
2
ky =A fie = (™*) (5-34)
a
The electromagnetic field is given by Eqs. (5-18) with the above y. The
TE wave functions satisfying the boundary conditions are
TE = gj mr Ha (kp) =
Vinn sin( a :) cos nd {raceme (5-35)
where m = 1, 2, 3,...,andn=0, 1, 2,..., and Eq. (5-34) still
applies. The electromagnetic field for the TE modes is found from Eqs.
(5-19) with the above y. In both the TM and TE cases, the H,‘”(k,p)
represent inward-traveling waves (toward the z axis), and the H,?(k,p)
represent outward-traveling waves. For a complete set of modes, those
with sin n@ variation must also be included.

Radial waves are characterized by a phase constant which is a function
of radial distance. Following the general definition of Sec. 2-11, we have
the phase constants for the above y’s given by

_@ _1 Na(kpp)
8. = 3, [ten Tn (Ege)
2 1
Ss 5-36)
x0 Tea) + No) ©38)

210 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Using asymptotic formulas for the Bessel functions, we find that for real k,
B, fase k, (5-37)
This is to be expected, because at large radii the waves should be similar
to plane waves on the parallel-plate guide. Note that the phase constant
of Eq. (5-36) is that of the mode function and not that for the field.
Components of E and H transverse to p are not generally in phase. They
become in phase at large radii.

Each mode of the radial waveguide is also characterized by a single
radially directed wave impedance. Using Eqs. (5-33) and (5-18), we find
for outward-traveling TM modes

E, k, Hn (kop)
™ = - -f = Pp - ia
Zee Hy ~ jae Hy” yp) (638)
while for inward-traveling TM modes
E, ky Hn (kop)
™ - - - Le =
70 Hy ~~ joe Hoye) oe)
Note that for real k, we have Z_,™ = Z,,™*. Similarly, for TE modes
we find
z,.te - Be _ jon Hn’ (hop)
+ He ky Ha (kp) 5.
gm = - Bs _ jon Hn "(ksp) (5-40)
~ H k, Ha (Ep)
where the first equation applies to outward-traveling waves and the
second equation to inward-traveling waves. Note that the TE wave
admittances are dual to the TM wave impedances.

It is seen from Eq. (5-34) that k, is imaginary if mx/a > k. In this

case, let k, = -ja, and
Hy(-ja) = 2 >K,(a)
where K, is the modified Bessel function (see Appendix D). The mode
functions are now everywhere in phase, and there is no wave propagation.
The radial wave impedances become imaginary, indicating no power flow.
For example, from Eq. (5-38), if k, = -ja,
m - ~Je Ha (jap) _ ja Kn(ap)

240 = Fae HyP"(-jap) ~ we K(a) @41)
which are always capacitively reactive, since K, is positive and Kj, is
negative. Hence, whenever a < \/2, the modes m > 0 are nonpropagating (evanescent). For small a, only the TMon modes propagate, for

CYLINDRICAL WAVE FUNCTIONS 211
which Eq. (5-33) reduces to
H»” (kp)
™ =
Yon cos np (fae (5-42)
From Egs. (5-38) and (5-39) we have the wave impedances for these
modes given by
. H,®(kp)
Z4o™ = Z_,™* = -jn H,®"(kp)
= te , '
De epi tp ~ Habe Uke) + Natkorwetho|} (6-43)
A consideration of the behavior of the Bessel functions (Figs. D-1 and
D-2) reveals that for arguments kp <n the N, functions and their
derivatives become large in magnitude. Hence, when 2xp < nd, the
wave impedances become predominantly reactive. Figure 5-6 illustrates
this behavior by showing X/R, where Z,,™ = R + jX, for the first five
TMon modes. Weshall call kp = n the point of gradual cutoff, the wave
impedances being predominantly resistive when kp > n and predominantly reactive when kp <n. Note that these gradual cutoffs occur
when the circumference of the radial waveguide is an integral number
of wavelengths. i
From the above discussion it is evident that the TMoo mode is dominant, that is, propagates energy effectively at smaller radii than any
other mode. For this mode we have
kz
E> = joc Ho (kp) Hy = kHy(kp) (5-44)
representing inward-traveling waves, and
k?
Et = - Ho™(kp) 4
jue es) “OOo
Hot = RH (kp) 3 Tt [least TI
which represent outward-traveling HH ee
waves. Note that there are no p & 2h
components of E or H, the mode s _I\ | IV ITT
being TEM to p. It is called the 1 AWN 1 NENBNEe
transmission-line mode of the paral- BIENBNANEE
lel-plate radial guide, because of its | jo =--- 2S
similarity with plane transmission- 0 1 2 3 4 5
line modes. For example, at a given kp
radius we can calculate a unique Fie. 5-6. Ratios of wave reactance to
voltage between the platesandanet wave resistance for the TMon radial
radially directed current on one of modes on the parallel-plate waveguide.

212 TIME-HARMONIC ELECTROMAGNETIC FIELDS

the plates. Also, the radial transmission line can be analyzed by the
classical transmission-line equations with L and C a function of p (Prob.
5-13).

Radial waves also can be supported by inclined conducting planes,
called a wedge radial waveguide, as shown in Fig, 5-5b. We shall assume
no z variation of the field, considering the problem as two-dimensional,
TM wave functions satisfying the boundary condition FE, = 0 at c =0
and c = co are

m™ - ot { 27 HS? aokp)
vam = sin (Fe) ten (49)
where p = 1, 2, 3, . . . , and the electromagnetic field is given by Eqs.
(5-18). TE wave functions satisfying the boundary condition E, = 0 at
c = Oand c = coare
TE pr HS? jel ke)
ware = cos (a) (a @4?)
where p = 0,1, 2, . . . , and the electromagnetic field is given by Eqs.
(5-19). The interpretation of the modes is essentially the same as that
for the TMo, parallel-plate modes, except that nonintegral orders of
Hankel functions appear. This introduces no conceptual difficulties, but
if numerical results are desired we would be hampered by a lack of tables
for functions of arbitrary fractional order.

The radial wave impedances for the wedge-guide modes are of the same
form as for the parallel-plate guide [Eqs. (5-38) to (5-40)]. We need only
replace n by pa/co and k, by k. These wave impedances exhibit the
same characteristic of gradual cutoff for fractional-order Hankel functions as they do for integral-order Hankel functions. Again the transitional point is that for which the argument and order are equal, that is,
pr/o = kp. The radii so determined correspond to those for which the
arc subtending the wedge is an integral number of half-wavelengths long.
This is as we should expect from our knowledge of plane waves between
parallel plates (the limiting case co- 0).

The dominant mode is evidently the TE» mode, in which case, from
Eqs. (5-47) and (5-19), we have

2
Ey = -kH (kp) 9 Ho = = By(hp) (548)
jou
for inward-traveling waves, and
2
Egt = -kH (kp) Het = © Hyp) (5-49)
jon
for outward-traveling waves. This is a transmission-line mode, charac

CYLINDRICAL WAVE FUNCTIONS 213
terized by no E, or H, and possessing a unique voltage and current at
any given radii. This mode also can be analyzed by the classical transmission-line equations for nonuniform lines (L and C a function of p).
Note that the field is dual to that of the parallel-plate line [Eqs. (5-44)
and (5-45)].

Finally, simple radial waves can be supported by the horn-shaped
guide of *Fig. 5-5c, called a sectoral horn waveguide. The TM modes*
are specified by the wave functions

mr \. H® (ke

Ymp™ = cos (@ 2) sin (% ) | phere i} (5-50)
where m= 0,1,2,...,andp=1,2,3,.... The field is given by
Eqs. (5-18), and

2
k, = a{k? - (“") (5-51)
a
The TE modes are specified by the mode functions
_ (mn H®).(k

Vnp™ = sin (= 2) cos (& *) (rae (5-52)
where m = 1, 2,3,...,andp=0,1,2,.... The field is given by
Eqs. (5-19), and k, by Eq. (5-51). These modes are qualitatively similar
to the hybrid modes of the rectangular waveguide (Sec. 4-4). There is,
of course, no transmission-line mode, because of the single conducting
boundary. Only the TMo, modes propagate if a < \/2; these plus the
TM,, and TE,, modes propagate if \/2 <a <j; and so on. Each
propagating mode has a radius of
gradual cutoff, this being the radius Z
at which the guide cross section is
about the same size as a rectangular
waveguide at cutoff. The TMn
mode is usually considered as the
dominant mode. (If a > /2 one
might argue that the TE. mode is
dominant at small radii.)

## Section 5-4: The Circular Cavity
 If a c@
section of circular waveguide is closed
by conductors over two cross sections, we have a resonator known as
the circular cavity. This is shown KP Y
in *Fig. 5-7. It is a simple matter x*
to modify the circular waveguide
mode functions to satisfy the addi- Fia. 5-7. The circular cavity.

214 TIME-HARMONIC ELECTROMAGNETIC FIELDS
tional boundary conditions of zero tangential E at 2 = 0 and z= d.
The result is a set of modes TM to z, specified by
mu = y, (ta20) {sinnd gn Vie, In a ) (oa = cos (% :) (5-53)
where n = 0,1, 2,...;p=1, 2, 3,...;andqg=0,1,2,....
The field is given by Eqs. (5-18). The set of modes TE to z is specified by
Znpe\ fsinnd| .. (gx
Tm - ~npP ZF Wire Inf = ){sare| sin (Fe (5-54)
wheren =0,1,2,...;p=1,2,3,...3;q=1,2,3,... ;and the
field is given by Eqs. (5-19). The separation constant equation [Eq.
(5-6)] becomes
es 2 qr 2 ies
Gy «(gy >
Tap)? 4 (ae) _ ia
y+ (GY
for the TM and TE modes, respectively. Setting k = 2xf~/eu, we can
solve for the resonant frequencies
2
a
Be = sae Vim" + (=)
PMN (5-55)
1 “ , gra
ee = a Ata + (=)
ire Qra Ven ss d
Each n except n = 0 denotes a pair of degenerate modes (cos nc or sin nd
variation). Thez,,and z,, are given in Tables 5-2 and 5-3. The resonant frequencies for various ratios of d/a are tabulated in Table 5-4.
TaBLe 5-4, ao FOR THE CircuLar Cavity oF Rapius a AND LENGTH d
1) dominant
d
© | TMoe | TEs | TMiso | TMon| TEs: | 7M! | Tey, | TMae | TMoe
a TEou
1) 1.0 © 1.59 Cy ° °° ° 2.13 2.29
0.5 1.0 2.72 1.59 2.80 2.90 3.06 5.27 2.13 2.29
1.0 1.0 1.50 1.59 1.63 1.80 | 2.05 2.72 2.13 2.29
2.0 1.0 1.0 1.59 1.19 1.42 1.72 1.50 2.13 2.29
3.0 1.13 1.0 1.80 1.24 1.52 1.87 1.32 2.41 2.60
4.0 1.20 1.0 1.91 1.27 1.57 1.96 1.20 | 2.56 3.00
od 1.31 1.0 2.08 1.31 1.66 2.08 1.0 2.78 3.00

CYLINDRICAL WAVE FUNCTIONS 215
- xxx ur
aN Piriiil
7 #% = aN \ x eR KK
/ { ay. Nil
Wek. -l
WE -tot 2
\ Po on.0 wale
ee eae
Soe aah rae
Fia. 5-8. Mode pattern for the TMoio mode (dominant when d/a < 2).
Note that for d/a < 2 the TMoo mode is dominant, while for d/a > 2
the TEi: mode is dominant. If d/a <1, the second resonance is 1.59
times the first resonant frequency. Note that this is very similar to the
square-base rectangular cavity of small height (the mode separation is
1.58 in that case).

The TMow mode corresponds to the first resonance of a short-circuited
radial transmission line. The field pattern of this mode, which is dominant for small d, is shown in *Fig. 5-8. The TE, mode corresponds to*
the first resonance of a short-circuited circular: waveguide operating in
the TE;: mode. Its mode pattern is thus that of a standing wave in a
circular waveguide, similar to *Fig. 5-3a. The case d/a- © corresponds*
to that of a two-dimensional circular resonator, for which the resonant
frequencies are the cutoff frequencies of the circular waveguide. The
last row of Table 5-4 therefore is also the cutoff frequency spectrum of
the circular waveguide.

The Q’s of the circular cavity are also of interest, especially the Q of
the TMoo mode (dominant for small d). From Eqs. (5-53) and (5-18)
we determine the field components of the mode as

B= By, (tue
+ joe” °Va
= TH Top
Hy = a a( a )
Following the procedure of Sec. 2-8, we calculate the stored energy. in
the cavity as
Ww = 20. = fff ier ar
4 a
= ona if pJo (222) dp
wre o a

216 TIME-HARMONIC ELECTROMAGNETIC FIELDS
This is a known integral,! the result being
kA 2
ap = THe 52203) (5-56)
wre
The power dissipated in the conducting walls is approximately
02 = aff [HI ds
2 oa
= a (2) on [ eantcen) +2 I ans (222) dp|
a 0 a
where @ is the intrinsic wave resistance of the metal walls. The above
integral is again known,! and we obtain
- Zo1\?
2 =R ci 2ma(d + a)J17(x01) (5-57)
The Q of the cavity is therefore
Q= ow k4 da®
~ 8a 2weRo2(d + a)
Recalling that the condition for resonance is ka = 2, = 2.405, we can
simplify this to
_ 1,202n
®= aa + af (6-58)
where 7 is the intrinsic impedance of the dielectric. This can be compared to the Q of a square-base rectangular cavity [Eq. (2-102)]. It is
seen that, for the same height-to-diameter ratio, the circular cavity has
an 8.3 per cent higher Q than the rectangular cavity. This is to be
expected, since the volume-to-area ratio is higher for a circular cylinder
than for a square cylinder. The Q’s for the other modes of the circular
cavity are given in Prob. 5-16. ,

## Section 6-5: Other Guided Waves
 The geometries of some other cylindrical
systems capable of supporting guided waves are shown in Figs. 5-9 and
5-10.. We treated the analogous plane-wave systems in Chap. 4. The
methods of solution for the systems of Figs. 5-9 and 5-10, as well as their
qualitative behavior, are similar to those of Chap. 4.

For the partially filled radial waveguide of *Fig. 5-9a, we can obtain*
fields TM to z which satisfy the conditions Z, = E, = 0 at z = 0 and
z = a by choosing

vi = Ci cos kz cos nd Hy (k,p) (5-59)
¥2 = C2 cos [k.2(a - 2z)] cos nd H,,)(k,p)

1¥. Jahnke and F. Emde, “Tables of Functions,” p. 146, Dover Publications, New

York, 1945 (reprint).

CYLINDRICAL WAVE FUNCTIONS 217
Z| Z
Conductor £0,H0
: ta YLUHYY YY,
GGG i
TAL. Udldill *
Conductor Pp
(a) (6)
Zz Z
HO |
Y
MM EYa 2
Conductor rs Conductor P
(©) @
*Fig. 5-9. Some radial waveguides. (a) Partially filled; (b) dielectric slab; (c) coated*
conductor; (d) corrugated conductor.
where nm = 0,1, 2,.... The subscripts 1 and 2 refer to the regions
z<d and z > d, respectively. We have anticipated that the p and c
variations must be the same in both regions to satisfy boundary conditions at z = d. Equations (5-59) represent outward-traveling waves.
Inward-traveling waves would be of the same form but with H, replaced
by H,. The k’s in each region must, of course, satisfy the separation
relationships
k,? + kes? = ky? = wer 7
k,? + Kes” = ky? = wreoue 6 60)
The field vectors themselves are obtained from Eqs. (5-18), using the y’s
of Eqs. (5-59).
To evaluate the C’s and k,, we must satisfy the conditions that E,, Ey,
H,, and H, be continuous at z = d. For E, we have
1f @ fil 1
[Ep1 - Epilena = a [so @ wi ~ = +), =0
which reduces to
k C... C..
ay sin kad = -kgs iz; on k,2(a - d) (5-61)
For E, we have
Ja a /1i 1 ys
[Eo1 - Ego] = jad [seas @ vi - a +) =0

218 TIME-HARMONIC ELECTROMAGNETIC FIELDS
which also reduces to Eq. (5-61). For H, we have
Wn - Hele *[2o.-vo] 0
which reduces to
Ci cos kid = C2 cos k,2(a - d) (5-62)
Finally, for Hy we have
(Ha - Hels = - [2 - v9] 0
ip lend
which again reduces to Eq. (5-62). Division of Eq. (5-61) by Eq. (5-62)
yields
ka kaa
A tankyad = - = tan [k.2(a - d)] (5-63)
The k,, and k,2 are functions of k, according to Eq. (5-60); so Eq. (5-63)
is a transcendental equation for determining possible k,’s. Once k, is
evaluated, the ratio Ci/C, may be obtained from either Eq. (5-61) or
Eq. (5-62). :
For fields TE to z we can satisfy the condition E, = E, = Oatz =a
by choosing
ti = Ci sin kz cos no H,(k,p) (5-64)
Yo = C2 sin k.2(a - z) cos nd H, (kp)
where n = 0, 1, 2,. . . ; and Eqs. (5-60) must again be satisfied. The
field components are found from these y’s by Eqs. (5-19). Matching
tangential components of E and H at z = d yields
Fe oot kad = - * cot [ki2(a - d)] (5-65)
Mi Ha
as the equation for determining k, for TE modes. It is interesting to
note that the characteristic equations for the partially filled radial waveguide [Eqs. (5-63) and (5-65)] are of the same form as those for the
partially filled rectangular waveguide [Eqs. (4-45) and (4-47)]. This we
could have anticipated, since at large p the Hankel functions reduce to
plane waves, as shown by Eqs. (D-13).

The modes of the partially filled radial guide can be ordered in the
same manner as were the modes of the partially filled rectangular waveguide. The dominant mode is the lowest-order TM mode (logically
designated the TMoo mode). It reduces to the radial transmission-line
mode in the empty guide and has no cutoff frequency. Fora «Ait can
be analyzed by conventional transmission-line concepts.

It should be apparent from our treatment of the waveguide of *Fig. 5-9a*
that the characteristic equations for the radial waveguides of *Fig. 5-9b, c,*

CYLINDRICAL WAVE FUNCTIONS 219
and d will be of the same form as those for the plane waveguides of Figs.
4-10, 4-13, and 4-15. We need only to replace the k,’s by k,’s. Hence,
for the dielectric-slab radial waveguide of *Fig. 5-9b, the characteristic*
equations are

ua ua
zr tan 2
af = ua ua (5-66)
€0 -- =
3 cot 3
for modes TM to z, and
ua ua
> tan a
Ha : Sf ue (5-67)
Ho - 4 oot 9
3 cot 3
for modes TE to z. The u and »v are related to k, by
w+tik,? = ky? = wena (5-68)
0? + ky? = ky? = weno
Possible solutions to these equations can be obtained graphically by the
method of *Fig. 4-11. Just as in the plane-wave case, the lowest TE and*
TM modes have no cutoff frequencies. The cutoff frequencies of the
modes in general are given by Eq. (4-63).

The modes of the coated-conductor radial waveguide of *Fig. 5-9c are*
those of the slab waveguide having E, = E, = 0 over the mid-plane of
the slab. The dominant mode is the lowest TM mode, which has no
cutoff frequency. The cutoff frequencies of the modes in general are
given by Eq. (4-64). Finally, for the corrugated-conductor radial line
of *Fig. 5-9d, the characteristic equation for the dominant mode is*

k, = ko -V/1 + tan? kod (5-69)
This is analogous to Eq. (4-71) in the plane-wave case.

The circular waveguide systems of *Fig. 5-10 are interesting, because,*
except for rotationally symmetric fields, the modes are neither TE nor
TM to any cylindrical coordinate. The systems of *Fig. 5-10a, b, and c*
have the common property that they are ‘‘two-dielectric”’ problems.
We can consider them all at once, as follows. Let region 1 be the inner
dielectric cylinder in each case and region 2 the outer one. We then
choose electric and magnetic y’s as

y™ = AB,™(kpip) cos nd et

¥? = BB,"(kpip) sin nd eH (6-70)
in region 1, and wn? = CB," (kp2p) cos np eat (5-71)

y? = DB,!? (kop) sin np eH

220 TIME-HARMONIC ELECTROMAGNETIC FIELDS
x Z x
4
S 2,b2
Sy oe
CIA y (Se ?
Conductor
(a) (6)
x Zz 5 Z
2,H2
K =
er Ey y
’- Conductor
(©) (d)
*Fig. 5-10. Some circular waveguides. (a) Partially filled; (b) dielectric slab; (c)*
coated conductor; (d) corrugated conductor.
in region 2. The y determine partial fields according to Eqs. (5-18)
and the y* determine partial fields according to Eqs. (5-19). The total
field is the sum of the two partial fields in each region. The B,(k,p)
denote appropriate solutions to Bessel’s equation of order n, chosen so as
to satisfy all boundary conditions except those at the interface p = a.
In each region the y’s must satisfy the separation relationships
Ky? + ke = ky? = wen
Keys? +k? = ky? = were (6-72)
The requirements that H., E,, Hy, and Ey be continuous at p = a lead to
erkpPABa™(Kpa) = erky2?CBya”*(kp2a)
Bak, BB (kya) = prkp2®?DBa?(k,2a)
Bkn Dkn
Aky:Ba™™ (ka) + oma B,"'(k,1a) = Ck,2Ba™™ (kp2a) + ona B,*(kp2a)
AKyn Ck,n
“maa Ba" insa) + BlyBat" (pa) = 2 Ba™*(tpst) + DyaBat™ (Kyra)
These equations have a nontrivial solution only if the determinant of the

CYLINDRICAL WAVE FUNCTIONS 221
coefficients of A, B, C, and D vanishes. Hence, defining,
F, = B,™(k,.a) Fy = Ba" (kp1@)
Py = Bom(kya) Fe = Buy.) ©73)
The characteristic equation in determinantal form is
exkpFy 0 exky2?F's 0
0 wok Ps 0 wikps Fy
kn kn
7 8 7 zi _
kei ona F, kok oma =0 (5-74)
kn » Kn 1"
weal? kek oad Fs kya,
When n = 0, the field separates into modes TE and TM to z, and the
characteristic equation is much simpler. It is
kis - kaFiFs = 0 (5-75)
for TM modes (n = 0), and
kyoF oy - kaFoFs = 0 (5-76)
for TE modes (n = 0). J

We must now pick the proper F functions for the various cases. For
the partially filled circular waveguide (*Fig. 5-10a), the field must be*
finite at p = 0; hence

Fy = F, = Ja(kps@) (5-77)

To satisfy E, = 0 at p = b, we choose

F3 = Ja(kp2@)Na(kp2b) - Na(kp2@)J n(kp2b) (5-78)
Furthermore, to satisfy E, = 0 at p = b, we choose

Fg = Jq(Kp2)N4 (Kya) - Ny (kp20)J%, (Kab) (5-79)
The dominant mode is the lowest-order n = 1 mode, which reduces to the
TEn mode of the empty guide. A solution for the k, of this dominant
mode is plotted in *Fig. 5-11 for the case «. = 1060, €2 = €0, #1 = M2 = Hoy*
b = 0.4r0.

For the dielectric-rod waveguide (*Fig. 5-10b), the field must again*
be finite at p = 0; so Eqs. (5-77) still apply. However, external to the
rod, the field must decay exponentially above the cutoff frequency and
represent outward-traveling waves below the cutoff frequency. Hence,
we choose

Pa = Fa = Kal ikpaa) = 5 (- Ha (Kyat) (6-80)
Once again, the dominant mode is the lowest n = 1 mode, and its cutoff

222 TIME-HARMONIC ELECTROMAGNETIC FIELDS
|
wet tA
LLL} E
a }
| SECC
0 0.2 0.4 06 0.8 1.0
a/b
Fie. 5-11. Phase constant for the partially filled circular waveguide, «1: = 10e:,
b =0.4r2. (After H. Seidel.)
frequency is zero.!_ Some solutions for the k, of the dominant mode are
shown in *Fig. 5-12 for the case e. = e9 and pi = 2 = wo. Note that*
ko < k, < ky, which is the same relationship that applies to the dielectricslab guide of Sec. 4-7.
For the coated conductor of *Fig. 5-10c we must again have exponential*
decay of the field as p- ©; so Eqs. (5-80) still apply. However, to
18. A. Schelkunoff, ‘Electromagnetic Waves,” pp. 425-428, D. Van Nostrand
Company, Inc., Princeton, N.J., 1943.
ek
«=10%
el get he [epee
eat ee |
3 | |
PL eet Ti
JI “Tt | €= 2.56
erie
fey ce
0 0.2 04 06 0.8 1.0
a/%o
*Fig. 5-12. Phase constant for the circular dielectric rod. (After M. C. Gray.)*

CYLINDRICAL WAVE FUNCTIONS 223

satisfy the condition E, = 0 at p = b, we should choose

Fy = Talkpr)Na (kid) - Na(kor4)In(kpd) (5-81)
and, to satisfy E, = 0 at p = b,

Fa = Jn(kpra) Ni (kod) - Nalkpra) J, (Korb) (5-82)
For this guide the dominant mode is the lowest n = 0 TM mode, which
has no cutoff frequency. (Compare it with the dominant mode of the
plane coated conductor of Sec. 4-8.) Copper wire with an enamel coating can be used as an efficient waveguide for some applications.!

Finally, the corrugated wire of *Fig. 5-10d can be analyzed in a manner*
similar to that used for the corrugated plane (*Fig. 4-15). The field external to the corrugated wire will be essentially the dominant TM (n = 0)*
mode of the coated wire. The field in the corrugations will be essentially
that of the shorted parallel-plate radial transmission line. The characteristic equation is obtained by matching wave impedances at the corrugated surface. As the radius of the corrugated cylinder becomes large,

. the solution approaches that for the corrugated plane.

## Section 6-6: Sources of Cylindrical Waves
 In this section we shall consider
two-dimensional sources of cylindrical waves, that is, sources independent
of the z coordinate. The extension to three dimensions can be effected
by a Fourier transformation with respect to z (see Sec. 5-11).

Suppose we have an infinitely long filament of constant a-c current
along the z axis, as shown in *Fig. 5-13a. From the theory of Sec. 2-9,*
we should expect the field to be TM to z, expressible in terms of an A
having only a zcomponenty. From symmetry, y should be independent

1G. Goubau, Surface-wave Transmission Lines, Proc. IRE, vol. 39, no. 6, pp. 619624, June, 1951.

Z x,
I P-P
¥ T(p') P
’
x c
Pp
x

(a) (6)
*Fig. 5-13. An infinite filament of constant a-c current (a) along the z axis and (b) displaced parallel to the z axis.*

224 TIME-HARMONIC ELECTROMAGNETIC FIELDS
of candz. To represent outward-traveling waves, we choose
A, = = CHo® (kp)
where C is a constant to be determined according to
lim f Hep dp = I
e370
Evaluating H = V x A, we find
= -~# _ _c 2 [H(kpy] - PE
Hyg = op = Ca [Ho (kp)] kp>0 7p
The preceding equation then yields
I
OG
Hence, A,=y= 4 He) (5-83)
is the desired solution. The line current is the elemental two-dimensional source, just as the current element (Sec. 2-9) is the elemental threedimensional source.
The electromagnetic field is obtained from Eqs. (5-18), using the of
Eq. (5-83)... The result is
-khl -k1
EN= Se Hy (kp) A, = a Ho" (kp) (5-84)
Thus, lines of electric intensity run parallel to the current, and lines of
magnetic intensity encircle it. Equiphase surfaces are cylinders, but E
and H are not in general in phase. However, at large distances we have
E, = -kl .| 2 crite
Sak, '
; ae p> (5-85)
= -ik,
Hy = KI lee .
|
which is essentially an outward-traveling plane wave. The amplitude of
the wave decreases as p~’*, in contrast to the r-! variation in the threedimensional case. The outward-directed complex power crossing a cylin- i
der of unit length and radius p is
P, = fpbEx H*-ds = - |," B-Hte ae
= GB (IPH (ko o (ke)I* (5-86)
The real part of this is the time-average power flow @;, which, by virtue

CYLINDRICAL WAVE FUNCTIONS 225
of the Wronskian [Eq. (D-17)]}, reduces to
- nk
Gy = Re (Ps) = FI (5-87)
Hence, the time-average power is independent of the distance from the
source, as we should expect. It could be more simply obtained from
Eqs. (5-85).

If the current filament is not along the z axis but parallel to it, we can
extend Eq. (5-83) by replacing p by the distance from the current to the
field point. In radius vector notation, we specify the field point by

@ = use + Wy
and the source point (current filament) by

ef =u’ + uy’
as shown in *Fig. 5-13b. The distance from the source point to the field*
point is then

le- el =V@-2)+y-y)?
= Vp? + p® - 2pp' cos (o - $')
We emphasize that A, is evaluated at e by writing A.(p) and that J is
located at o’ by writing I(9’). We can now generalize Eq. (5-83) to read
I(o’ ;
Ao) = NE) (He - ol) (5-88)

This is our free-space Green’s function for two-dimensional fields.

The solution for two or more filaments of z-directed current can be
represented by a summation of the A,’s from each current element. Suppose we have two filaments of equal magnitude but opposite phase, as
represented by *Fig. 5-14a. As the separation s > 0 and the magnitude*
I - © such that Js remains constant, we have a two-dimensional dipole

Y Y
f -1\41 e
-1I c Fo | c
ge ES 7
S)
(@) rat
Fia. 5-14. Sources of higher-order waves. (a) Dipole source; (b) quadrupole source.

226 TIME-HARMONIC ELECTROMAGNETIC FIELDS
source. Note that A, at a point (z,y) due to a current filament at (x’,0)
is the same as A, at (x - z’,y) due toa current filament at (0,0). Hence,
for *Fig. 5-14a, the vector potential is*
8
A, = as(z - $v) - As (2+ $u)
where A,! is that due to a single current filament at the origin [Eq.
(5-83)]. In the limit s - 0 the above equation becomes
0A _ Isa ®
A. 8 Sp = Gane (kp)]
The differentiation yields
A,= “ H (kp) cos & (5-89)
Thus, the vector potential of a dipole line source is a cylindrical wave
function of order n = 1.

For the quadrupole source of *Fig. 5-14b we have, by reasoning similar*

to that above,

F, a2A,! 0A,

2 --> 8182 5 = - S83
par Ox Oy oy
where A,® is the vector potential of the dipole source, given by Eq.
(5-89). Hence,
me -kIss_ 0

A, = -- - [Hk

A, = STEPS (Hs (kp) 008 6]

. KI sys Q
which reduces to A, = va H,(kp) sin 26 (5-90)
Thus, the vector potential of a quadrupole line source is a wave function
of order n = 2.

This procedure can be continued to obtain sources for the higher-order
wave functions. It can be shown (Prob. 5-29) that, when A, is a wave
function of order n, a possible source consists of 2n current filaments
equispaced on an infinitesimal cylinder. We shall call such a source a
multipole source of order n. The dual analysis applies to the case of magnetic current filaments. It is merely necessary to replace J by K and
A by F in the various vector-potential formulas of this section. For
example, from Eq. (5-88), the electric vector potential at » due to a
magnetic current filament at 9’ is

Ko!
Fale) = AIS) a (kle - ofl 6-91)
Using both electric and magnetic multipoles, we can generate an arbitrary source-free field in homogeneous space (p > 0).

CYLINDRICAL WAVE FUNCTIONS 227
Zz
dz
*Fig. 5-15. A cylinder of*
uniform current.
¥,
x $
Pp
The field due to a cylinder of currents can be obtained quite simply by
treating the problem as a boundary-value problem. We shall consider
here only a cylinder of uniform z-directed surface current. (The general
case is considered in Prob. 5-30.) The geometry of the problem is illustrated by *Fig. 5-15. Because of the rotational symmetry, we choose*
v= A, = CyWJo(kp) p<a
- (AY = Croke) pp >a
The boundary conditions to be satisfied are
Eo = E> Het --Hy =J,
where J; is the density of the z-directed current sheet. Using Eqs. (5-18)
with the above y, and satisfying the boundary conditions, we obtain
= 5 aka Ho (ka) J o(ke) p<a
E, = = (5-92)
- 5 thal oJ o(ka) Ho (kp) p>a
as the only component of EL Let us calculate an impedance per unit
length for this source, as we did for the ribbon of current in Sec. 4-12.
By definition,
P
7 > TF
where P is the complex power per unit length
oe
P= - [." BJtadp = -2naJ3h, |.

228 TIME-HARMONIC ELECTROMAGNETIC FIELDS
and / is the total z-directed current
I= [," Jado = 2naJ,
Hence, the impedance per unit length is
nk
Z= tT J o(ka)H (ka) (5-93)
Using smail-argument formulas for Jo and Ho, we obtain
n _; yka 7
Z ja OK (« j2 log se) (5-94)
where y = 1.781. Compare this with the Z of a ribbon of current [Eq.
(4-127)]. The resistances (real parts) are identical. The reactance of a
cylinder of current of small diameter d is approximately equal to the
reactance of a ribbon of current of width w = 2d. More generally, it
can be shown! by a quasi-static approximation that the impedance per
unit length of a small elliptic cylinder of minor axis a and major axis b
is the same as that of a circular cylinder of diameter
. d= (a+ b)
A ribbon is the special case a = 0 and b = w.

## Section 6-7: Two-dimensional Radiation
 We can construct the solution for
an arbitrary two-dimensional distribution of currents by dividing the
source into elemental filaments of current and summing the fields from
all elements. For example, if we have a J,, independent of z, each element J, ds’ produces a vector potential

J, ds’
dA, = “Ge Ho (kle - e'l)

where ds’ is an element of area perpendicular to z. Summing over the
entire source, we have

A, = i ff 1.090 te - ol) ae
where the integration extends over a cross section of the source. Since
the equations for A, due to Jz and for A, due to J, are of the same
form as those for A, due to J., the above equation also applies for z
replaced by x or y. Combining components, we have the vector equation

1
Ao) = # [f Hed Gle - ot) as (5-95)
1R. W. P. King, “The Theory of Linear Antennas,’ pp. 16-20, Harvard Uni
versity Press, Cambridge, Mass., 1956.

CYLINDRICAL WAVE FUNCTIONS 229
representing the solution for an arbitrary two-dimensional distribution of
electric currents. The cases of surface currents and current filaments
are included by implication. The electromagnetic field is obtained, as
usual, from H = VX A. The electric vector potential due to twodimensional magnetic currents M is given by the formula dual to Eq.
(5-95), or

Foo) = 7 [f MoH (tle - oD ae (5-06)
‘The electromagnetic field in this case is given by E = -V X F.

When the field point is distant from the source, our formulas simplify
to a form similar to those for three-dimensional radiation (Sec. 3-13).
For kle - o’| large, the Hankel function can be represented by the
asymptotic formula

27 5
(2) (Ig) -q' pik |p-o"|
Ho (ko o') > aap yore
Furthermore, when p > p’, as shown in *Fig. 5-16, we have*

le - 0'| > p - p’ cos (c ~ c’) (5-97)
The second term must be retained in the phase factor, exp (-jklo - 0'|),
but not in the magnitude factor, |p - 9’|-. Hence, the vector potentials of Eqs. (5-95) and (5-96) reduce to

A= ea Il Jo" )etko" con (9-99 ds!
Sirk,
eis (5-98)
PE 202 M(0') cite’ 208 (@-4) ds!
V8jnkp // i
provided p > p/.,,.. These are the radiation-zone formulas corresponding
to Eqs. (3-95) in the three-dimensional case.
To distant
field point
e P-P’
*Fig. 5-16. Geometry for*
determining the radia- ys
tion field. “3
Le ¥ c
x

230 TIME-HARMONIC ELECTROMAGNETIC FIELDS

We now have the p variation explicitly shown in Eqs. (5-98), and simplified formulas for the radiation field can be obtained. As evidenced by
Eq. (5-85), the distant field of a single current filament is essentially an
outward-traveling plane wave; so the superposition of fields from all current elements should also be of this type. Hence, in the radiation zone,

Es = nH, E, = -nHs (5-99)
which can be verified by direct expansion of Eqs. (3-4), using Eqs. (5-98).
To obtain the field components, let us again divide the field into that due
to J, given by H’ = V X A, and that due to M, given by E” = -V x F.
Retaining only the dominant terms (p~™ variation), we obtain
Hi, = jkA, El = -jkF,
HL = -jkAg By! = jkFy
in the radiation zone. The corresponding E, E?, Hi’, and H/’ can be
determined from Eqs. (5-99). The total field is simply the sum of the
primed and double-primed components, or
. Es = -jopA, - jkF,
oe eee! (5-100)
E, = -jouA, + jkFs
in the radiation zone, with H given by Eqs. (5-99). These formulas
correspond to Eqs. (3-97) in the three-dimensional case. Note that,
except for the contrasting p~* and r~! dependences, the radiation fields
are of similar mathematical forms in two and three dimensions.

## Section 6-8: Wave Transformations
 It is often convenient to express the
elementary wave functions of one coordinate system in terms of those of
another coordinate system.! We refer to expressions of this type as
wave transformations. Some representative wave transformations are
derived in this section. Others will be derived as they are needed.

Suppose we have the plane wave e~*, which we wish to express in terms
of cylindrical waves. (The conventional coordinate orientation of *Fig.
5-1 is assumed.) This wave is finite at the origin and periodic in 27 on c.*
Hence, it must be expressible as

ecit = gr ipcond And n(p)e?
2.
where the a, are constants. To evaluate the a,, multiply each side by
e-*# and integrate from 0 to 27 on c. This gives
hr ein cor beim dg = 2rdnJ m(p)

1 Two coordinate systems are considered to be distinct if their origins or orienta
tions are different, even though they may be geometrically the same.

CYLINDRICAL WAVE FUNCTIONS 231
The left-hand side is actually a well-known integral, but we need not
recognize this. The mth derivative of the left-hand side with respeci to
p evaluated at p = 0 is
Qe im
if cos” c eI" dod = ony”
0) 2™
The mth derivative of the right-hand side evaluated at p = 0 is 2ra,,/2™.
Hence,
an = j-™
and we have shown that
emit = gripes = y j- a(pem? (5-101)
and also that
Jn(e) = i OT erie conde-ind dp (5-102)
~ Qn Jo
Equation (5-101) is the wave transformation expressing the plane wave
e-# in terms of cylindrical wave functions. It is closely related to the
so-called “generating function” of Bessel functions.!
Another wave transformation of interest is that which corresponds to
a translation of cylindrical coordinate origin. Consider the wave function
¥ = Ho (lo - 9'|) = Ho lV p? + p’? - 2pp’ cos (c - $’)]
where p and p’ are as defined in *Fig. 5-13b. We can think of y as the*
field of a line source at p’ in terms of a cylindrical wave function having
its origin at the source. We shall reexpress y in terms of wave functions
referred to p = 0. In the region p < p’, permissible wave functions are
J,(p)e"*, n an integer, for y is finite at p = 0 and periodic in 27 on c.
In the region p > p’, permissible wave functions are H,)(p)e"*, n an
integer, for y must represent outward-traveling waves. Also, y must be
symmetric in primed and unprimed coordinates (reciprocity). Hence,
y is of the form
») bnH a (p')T alpen? pp < p!
v = ne=-o .
¥ bad n(n’) Hn (pen? p > pp!
where the b, are constants. To evaluate the bn, let p’ > © and c’ = 0,
and use the asymptotic formulas for the Hankel functions. Our original
1R. V. Churchill, ‘‘ Fourier Series and Boundary Value Problems,” p. 147, McGrawHill Book Company, Inc., New York, 1941.

232 TIME-HARMONIC ELECTROMAGNETIC FIELDS
expression for y then becomes
Y= Holo - of) oo 2h evens
ee Nap
o’=0
and our constructed expression for y becomes
5 5
Y¥- 2 ae bngJ n(p)en*
eo Nip
=0 n=-®
These are now representations of a plane wave, and, from Eq. (5-101),
it follows that b, = 1. Thus,
XY Hae alo en op <p!
Ao(lo - e') = 4" S” (5-103)
») Fao )Hn® (p)em?-#) pp > p!
This equation is known as the addition theorem for Hankel functions.
It is also valid for superscripts (2) replaced by superscripts (1), since
H,® = H,®*. Adding the addition theorem for Ho to that for Ho,
we obtain
Tolle - e'|) = ») Tn(p')Ia(p)ere# (5-104)
which is the addition theorem for Bessel functions of the first kind. An
addition theorem for Bessel functions of the second kind is obtained by
subtracting that for Ho from that for Ho”.

## Section 5-9: Scattering by Cylinders
 A source radiating in the presence of a
conducting cylinder is one of the simplest ‘‘wave-scatter”’ problems for
which an exact solution can be obtained. We shall at present consider
only two-dimensional cases. Extension to three-dimensional cases can
be effected by the method of Sec. 5-12.

Let us first consider a plane wave incident upon a conducting cylinder,
as represented by *Fig. 5-17. Take the incident wave to be z-polarized,*
that is,

Ek = Eyenit® = Byeniovont (5-105)
Using the wave transformation of Eq. (5-101), we can express the incident
field as
Es = Ey ») j-*In(kp)ee
note

CYLINDRICAL WAVE FUNCTIONS 233
Y
p
Fie. 5-17. A plane wave
incident upon a conduct- ae
ing cylinder.
Inci a $
incident AN
wave Conductor x
The total field with the conductin, i i
nos g cylinder present is th
incident and scattered fields, that is, 7 siete
E, = Es + Es
To represent outward-traveling waves, the scattered field must be of the
form
Bg = Bo YF tanta (kp)em* (5-106)
hence the total field is
By = Ey Yj Salo) + ana (ko)]o"* (5-107)
At the cylinder the boundary condition E, = 0 at p = a must be met.
It is evident from the above equation that this condition is met if
-Jn(ka)
ae A 5a = FF (ka) (5-108)
which completes the solution.
The surface current on the cylinder may be obtained from
1 dF,
J.= | = te
He p=a Jon Op \p=a
Using Eqs. (5-107) and (5-108), and simplifying the result by Eq. (D-17),
we obtain
-2E,4 potent
= - a -1
J. = Gara y Hf, (ka (5-109)
me thin wire then = 0 term becomes dominant, and we have essentially
lament of current. Using the small-argument formula for Ho”, we

234 TIME-HARMONIC ELECTROMAGNETIC FIELDS
find the total current as
al 2rEo
I= i Jadd =e log ka (5-110)
Hence, the current in a thin wire is 90° out of phase with the incident
field.

The pattern of the scattered field is also of interest. At large distances
from the cylinder we can use the asymptotic formulas for H,, and Eq.
(5-106) becomes

Bien i
Es -» Eo ./-- e-i#? a,ei#
pe akp
where the a, are given by Eq. (5-108). The magnitude of the ratio of
the scattered field to the incident field is therefore
\E.| [2 | Falke) in 11
. IEs| ~ Nako| Ly Hea) ea)
Thisisthe scattered-field pattern. For small ka, the n = 0 term becomes
dominant and
|E.*| 7 Pz
{E,] ia 2 log ka Vxkp (5-112)
The scattered-field pattern for a thin wire is therefore a circle, which is
to be expected, since the wire is essentially a filament of current.

When the incident field is polarized transversely to z, it can be expressed

as
H,} = Hoe-** = Ho ») i" a(kep) eine (5-113)
Again, the total field is considered as the sum of the incident and reflected
fields, that is,
H,= H+ Hs
To represent outward-traveling waves, the scattered field is of the form
Hy = Ho ») j-*D nH y\(Kep)ein?

and the total field is given by

H, = Ho ») Falke) + ban (kp)lem* (5-114)

CYLINDRICAL WAVE FUNCTIONS 235
caations our boundary condition is Es = 0 at p = a. From the field
he es
Ey = Sas (Vv xX u.H.)c
= IR a. Spm (kp) + Bob "(pyle
=U, Ho FUT kp) + ba Hn’ (ko) le
n=0
and the boundary condition is met if
-Ji (ka)
be = Fares) (5-115)
An incident wave of arbitrary polarization can be treated as a superposition of Eqs. (5-105) and (5-113).
When the incident wave is polarized transversely to z, the surface current on the cylinder is
- = Bus ete Teas \.. = Tha 71,2(ka) (5-116)
For small ka, the n = 0 term becomes dominant. However, then = +1
verms radiate more efficiently and cannot be neglected, as we shall now
show. At large distances from the cylinder, the scattered field becomes
Hes -+ Ho J 2h emits » byeint
kp rkp
with b, given by Eq. (5-115). The magnitude of the ratio of the scattered
to incident field is thus
\He| [2 Tika) 5
He ~Neke| 2y Hae”Ga) on
For small ka we find
1: 2
7 ie(ha) n=0
Tika) _ +) jn(ka)?
Hea) =) a inl = 1
jx (ea/2)?""
relat =e
Hence, for thin wires the scattered-field pattern is
HH," ka)? | 2_
Wel 9 ee en - 2cos 9} (5-118)
The n = 0 term of Eq. (5-116) is equivalent to a z-directed magnetic

236 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Y
P
Current
, filament Fie. 5-18. A current fila
K<|> $ e ment parallel to a con
oN ducting cylinder.

* Z-\ \ #

x
Conductor
current filament, while the n = +1 terms are equivalent to a y-directed
electric dipole.

A more general problem is that of a current filament parallel to a con~
ducting cylinder, as shown in *Fig. 5-18. (Plane-wave incidence is the*
special case p’- ©.) When the filament is an electric current J, the
incident field is

A Ei= maui’ Ho(klp - e'|) (5-119)
. 4we
For p < p’ we have, by the addition theorem [Eq. (5-103)],
Ej = eT y Ha (kp’) J n(kp)e* 4-9)
‘ 4we ” °
To this we must add a scattered field of the same form, but with the J,
replaced by H,°), namely,
-kh I , inlo-o"
Es = aren CrH (kp’) Hn (kp)e-9? (5-120)
WE
From the preceding two equations it is evident that
AC)

o = - FF,@(ka) (121)
satisfies the boundary condition FE, = E,)+ E,,=0. Thus, our final
solution is

hI H,,(kp" (2)(Kp) ]ein(e-#) ’
ae a (kp')[Tn(kp) + Cnn (kp) Je’ p<p
E, = name
=I , 1) \ein(o-4" ,
Ser DD, Ha (ke Talo!) + Cala (keene p> p
WE
(5-122)

CYLINDRICAL WAVE FUNCTIONS 237
Note that our answer is symmetrical
in p, c and 9’, c’ (reciprocity). Note THRE
also that the “reflection coefficients” thE SS
of Eq. (5-121) are equal to those of PERS
Eq. (5-108) and are, in general, in- AKER
dependent of the incident field. HALES \
Specializing the second of Eqs. FORM
(5-122) to the far zone, we have HOST N
= SZZsa'
esx ST a9 Weer)
* poe Jl) J” | In(kep SSH TY
aane ANS SAL
_ Yalka) py 02 (K9") | einto-0 NWA T LT i
{Banoo RRL
The magnitude of this is the radia- TESS SEP
Ee
tion field pattern. Figure 5-19 shows mee, TAs <P)
the radiation pattern of a current fila- AAS
ment 0.25\ away from a conducting rT 3
cylinder of radius 3.75\. The radia- apes
tion pattern of a current filament _
0.25\ in front of a plane reflector is *Fig. 5-19. Radiation pattern for a curh for comparison. The patterns rent filament 0.25 away from a cylin8 own P: sO Pi drical reflector of radius 3.75\ (plane*
of *Fig. 5-19 are also valid for current reflector case shown dashed).*
elements of finite length as long as
the reflector is of infinite extent.
If the line source of *Fig. 5-18 is a magnetic current filament K, we have*
He = SEs Ho®(kle - e'l)
instead of Eq. (5-119). The problem is dual to the electric current case,
except that the reflection coefficients at the conducting cylinder must be
those of Eq. (5-115) instead of those of Eq. (5-121). Therefore, the final
solution will be dual to Eq. (5-122), or
-K H,,(kp')[J. HH, inle-$") ’
dep n(Kkp')[Jn(kp) + ban (kp)e p<p
H, = anne
MK H,®(kp)[Jn(kp’) + baH a (kep’) Jen o-# > p!
ca a (kp) [J n(ke’ nl (kp) Je p>p
(5-123)
where the b, are given by Eq. (5-115). According to the equivalence

238 TIME-HARMONIC ELECTROMAGNETIC FIELDS
~ principle, the field of a narrow slot in
aap \ a conducting cylinder is the same as
YI <L 7 the field of a magnetic current on the
SAEEAS surface of a conducting cylinder.

TERR Specializing the second of Eqs. (5-123)

PIRES to the case p’ = a, c’ = 0,p > ©, we

RSS have

WOOO ATT sop

ROWPKAAV A H, = a ik as

Nreeeee rr] | 10 Ly Hao")

| SEE .

UI OLA LT TY The magnitude of this is the radiation

PASSSLAL]

PHI OXOKT 7 LT} pattern of a ‘‘slitted cylinder.” FigATS SOL ure 5-20 shows a slitted-cylinder pat
MO tern for the casea = 2X. The pattern

SOS for a slit in an infinite ground plane
IND SZ is shown for comparison. The patLTS SS terns of *Fig. 5-20 are also valid for*
P1\ a slits of finite length as long as the
es conductor is of infinite extent.
*Fig. 5-20. Radiation pattern for a 5-10. Scattering by Wedges. A*
slitted cylinder of radius 2d (slit ina source radiating in the presence of a
ground plane shown dashed). conducting wedge is also a relatively
simple problem.! We again restrict
consideration to the two-dimensional case at this time. We shall solve
for the field of current filaments in the vicinity of wedges and obtain
solutions for plane-wave illumination and aperture radiation as special
cases. A wedge of vanishingly small angle is the classical conducting
half-plane problem.

Consider first the case of a filament of electric current at p’, c’ adjacent to a conducting wedge defined by c = a and c = 2m - a (wedge
angle = 2a). This is shown in *Fig. 5-21. The incident field is given by*
Eq. (5-119) and has only a z component of E. The total field also will
have only a z component of E, since this is sufficient to satisfy the boundary conditions. We construct

Y, aH (ko")Ja(kp) sin (6" - a) sinv(p- a) p <p
E.= 5
Y aedo(kp") He (kp) sin v(g! - @) sinv(p - a) p>
(5-124)

1 Problems involving conductors over complete coordinate surfaces are usually easy

to solve. In this case the wedge covers two c = constant coordinate surfaces.

CYLINDRICAL WAVE FUNCTIONS 239
which satisfies reciprocity and insures continuity of FE, at p = p’. To
satisfy the boundary conditions FE, = 0 over c = a and c = 2a - a, we
choose

mn
Vag ay MALDB-- (5-125)
The a, are determined by the nature of the source.

To evaluate the a,, we view the current element as an impulse of current on the surface p = p’. The boundary condition to be satisfied at a
current sheet is

J. = Ho(o'+) - Hole’-)
Using the field equations and Eq. (5-124), we find
x » a.H,®(kp’)Ji(kp) sin v(c’ - @) sin v(c - @) p<p’
Hy = , .
isi BY a,J ,(kp')H,."(kp) sin v(c’ - a) sin vo(c - a) p>p
Thus, using the Wronskian [Eq. (D-17)], we have the surface current
given by
= Y a, sin o(c’ - a) sin v(c - a)
wump
>
This is simply a Fourier series for the current on p = p’. The Fourier
sine series for an impulsive current of strength J at = $’ on p = p’ is
J,= ar) sin v(c’ - a) sin o(c - a)
(x - a)p By comparison of the preceding two
equations it is evident that
I Y
mg HES & = 50a) (5-126)
This completes the solution. °
To obtain the radiation pattern of Current
pt filament
a current J near a wedge, use the
asymptotic formula for H,®)(kp) in e Conductor
the second of Eqs. (5-124). This, @
with Eq. (5-126), gives x
Ex-> Sle) ) i°Folke!)
v *Fig. 5-21. A current filament adjacent*
sin v(c’ - a) sinv(@ - a) to a conducting wedge.

240 TIME-HARMONIC ELECTROMAGNETIC FIELDS
a
ZESRSS
Beas
CX ERASS
Yj FoR
Givaauns i.
LSTA N
LTE EDOA NO
LD
NORIO SOM
War POW F Oe Ee
CNCRSS eZEETTT| |
SEES SSH
SS tsge SQ
Sm SET
SA RSMOSCAT
Fia. 5-22. Radiation patterns for an electric current filament adjacent to a conducting
half plane, p’ =a, 6’ =2/4. (After J. R. Wait.)
where v is given by Eq. (5-125). Figure 5-22 shows some radiation patterns for the special case a = 0 (the conducting half plane).

Another special case of interest is that of plane-wave illumination.
This is obtained by letting the source recede to infinity. In this case,
the incident field becomes

Be = SET re - ell
= reel | aa Eiko’ gikp cos ($-#")
This is recognized as the plane-wave field
Ei = E gett con (o-#)
where Ey = el ed (5-127)
The total field in the vicinity of the wedge is obtained by specializing the
first of Eqs. (5-124) to large p’. This gives
E,--_ , | 22, ike" v0 i ’ i
se Nirkp’ eo a,j°J (kp) sin v(o’ - a) sin v(d - a)

CYLINDRICAL WAVE FUNCTIONS 241
Finally, substituting for a, from Eq. (5-126) and for I from Eq. (5-127),
we obtain
2rE. Z . .

E,= Pree YP) sin v(c! - a) sin o(c - @) (5-128)
where v is given by Eq. (5-125). This is the solution for a plane z-polarized wave incident at the angle $’ on a wedge of angle 2a. For a = 0
we have

,
E, = 2E> y 5°? J nialkep) sin ee sin “e (5-129)
nel
which is the solution for a plane wave incident on a conducting half plane.
The “almost dual” problem (dual except for boundary conditions) is
that of a magnetic-current filament K at p’, c’ in *Fig. 5-21. We construct a solution*

J, bo (kod aC) cosv($’ - a) cosv(p- a) pe <P
H.=S~

J, bad kp" He (kp) c0s (4 - a) 05 (> - a) p>e’

° (6-130)
which is similar to Eq: (5-124) except for the sines replaced by cosines.
The boundary conditions BE, = 0 at c = and c = 2x - a can now be
satisfied by choosing

mr _ _
»=3Gq a) m=0,1,2,... (5-131)
The coefficients b, are determined by the nature of the source, in a
manner analogous to that used to obtain Eq. (5-126). The result is
-s v=0
bat) SS (6-132)
_omK - y59
2(" - 2)
which completes the solution.

The radiation pattern of a magnetic current K near a wedge is obtained
from the second of Eqs. (5-130) by using the asymptotic expression for
H,®(kp). The result is

H, 2 Ho) J, ec*To( ko") c08 0(9" - a) cos (6 - @)

242 TIME-HARMONIC ELECTROMAGNETIC FIELDS

where Neumann’s number c, is 1 forv = Oand 2forv > 0. Figure 5-23
shows some radiation patterns for the special case a = 0. When c’ =a
we have the solution for a radiating slit in a conducting wedge.

Finally, for plane-wave incidence we can specialize the first of Eqs.
(5-130) to the case p’-» ~. The procedure is analogous to that used to
establish Eq. (5-128), and the result is

a, = 2H > e.J°Jo(kp) cos v($’ - a) cos v(f - a) (5-133)
-a
This is the field due to a plane wave polarized orthogonally to z incident
at an angle c’ on a wedge of angle 2ax The case a = 0 gives
H. = Ho » end”? nixlkp) cos “ cos ” (5-134)
n=0
which is the solution for a plane wave incident on a conducting half plane.

## Section 5-11: Three-dimensional Radiation
 A three-dimensional problem
having-cylindrical boundaries can be reduced to a two-dimensional problem by applying a Fourier transformation with respect to z (the cylinder

AER
ETSI
OPERAS
STALKS
SSP RRA
KS OE DER
PERSIE EO
PQ BS \
EERE ee
(Gia \\ Zee aN
.aaS BET) | | IN
ZF. a,
LEAN TT |
SISO
SERA LT]
ORR KN
Fie. 5-23. Radiation patterns for a magnetic current filament adjacent to a conducting
half plane, p’ =a, c’ = 7/4. (After J. R. Wait.)

CYLINDRICAL WAVE FUNCTIONS 243
axis).1_ For example, if y(z,y,z) is Z
a solution to the three-dimensional -_
wave equation =
a gz 92 ; T(z) |
(tga tpth)y=o ;
then J
° ; 1
Hesyw) = [7 veaa)e* de
Y
will be a solution to the two-dimen- $ Po!
sional wave equation
a, , \ %
(35 + ay +k ) y=0
where x? = k? - w». Once the twodimensional problem for 9 is solved, yg. 5-24. A filament of current along
the three-dimensional] solution is ob- the z axis.
tained from the inversion
1 ° .
Yea) = 5 [ Uxsysw)et dw
rt |
This is usually a difficult operation. Fortunately, in the radiation zone
the inversion becomes quite simple. We shall now obtain this far-zone
inversion formula.

Consider the problem of a filament of z-directed current along the z axis,
as illustrated by *Fig. 5-24. The only restriction placed on the current*
I(z) is that it be Fourier-transformable. In the usual way, we construct
a solution

H=VXA A= uy (5-135)
where y is a wave function independent of c and representing outwardtraveling waves at large p. Anticipating the need for Fourier transforms, we construct

b= [Manteo VF = whom aw
which is of the general form of Eq. (5-11). The Fourier transform of y is
evidently
V = fw) Ho (9 Vi =u")
The f(w) is determined by the nature of the source, according to
an = .
fy" Hee a6 - Tw)
1 This applies to cylinders of arbitrary cross section as well as to circular cylinders.

244 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where A’, and J are the transforms of Hy and J. From the small-argument formula for Ho’, we have
7 _ _ ow 25
Hy = % wars col (w)
and the preceding equation yields
_ T(w)
fw) = a
Hence, the ‘transform solution” to the problem of *Fig. 5-24 is*
ve al T(w) Ho (p VEE = w?)e%* dw (5-136)
where I(w) = L T(z’ )e-* dz’ (5-137)
The field is obtained from y according to Eqs. (5-135). Compare the
equations of this paragraph to those of the second paragraph of Sec. 5-6.
The transformed equations in the three-dimensional problem are of the
same form as the equations in the two-dimensional problem.
Another solution to the problem of *Fig. 5-24 is the “potential integral*
solution” of See. 2-9. This is
¥ ” 1@) e-ikV/ PEE uw (6-138)
= 2!) pes dz f. 4 /p? + (2 - 2’)?
with the field given by Eqs. (5-135). It can be shown that the y is unique
in this problem. Hence, Eqs. (5-136) and (5-138) are equal, giving us a
mathematical identity. For example, if J(z) isa short current element of
moment Jl, then I(w) = Il and Eq. (5-136) becomes
y= al Hop 4 / ke = weit dw !
d Eq. (5-138) b die |
and Eq. (5-138) becomes y= = |
Equating these two w’s we have the identity |
jkr o
-- 3/ Ho (p VE - wie dw (6-139)
Many other identities can be established in a similar fashion.
It is convenient to have two forms for y because some operations are
easier to perform on one form than on the other. For example, it is
simple to specialize Eq. (5-138) to the radiation zone, and we did so in
Sec. 2-10. In particular, the specialization is given by Eq. (2-122), which

CYLINDRICAL WAVE FUNCTIONS 245
can be written as
ike
¥ -> <~ i(k cos 6) (5-140)
roe Agr
where I(w) is given by Eq. (5-137). By Eq. (3-97) we have
Ey - > -jouAs = jou sin oy
. eTokr .
or Es -> jon Tr 50 6 I(-k cos 6) (5-141)
Hence, the radiation field is simply related to the transform of the source
evaluated at w = -kcos@. More important, the specialization of Eq.
(5-140) must also be the corresponding specialization of Eq. (5-136).
We therefore have the identity
oo nike =
| I(w) Ho (p Wk? - w?) ef dwu-> 2j- I(-k cos 6) (5-142)
which holds for any function /(w). Equation (5-142) can also be established by contour integration, using the method of steepest descent.!
Finally, we shall need a formula similar to Eq. (5-142) valid for Hankel
functions of arbitrary order. The desired generalization can be effected
by considering the asymptotic expression
® 4d ine:
H,, (2) = fs eae
from which it is evident that
H(t) -> jr (2)
As long as @ ¥ O orm, we havep- » asr- ,sincep = rsin@. Also,
if k is complex (some dissipation assumed), then »/k? - w? is never zero
on the path of integration. We are then justified in using the asymptotic
formula for Hankel functions and can replace the Ho of Eq. (5-142) by
j-*H,™. The result is
8 ike .
/ I(w) Hal (p VEE = wie dw -> 2 aa jet1T(-k cos @) (5-143)
We shall have use for this formula in the radiation problems that follow.

## Section 5-12: Apertures in Cylinders
2 Consider a conducting cylinder of
infinite length in which one or more apertures exist. The geometry is
1 A. Erdelyi, “Asymptotic Expansions,” pp. 26-27, Dover Publications, New York,
1956.
2 Silver and Saunders, The External Field Produced by a Slot in an Infinite Circular Cylinder, J. Appl. Phy., vol. 21, no. 5, pp. 153-158, February, 1950.

246 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz
ee
|
|
< |
|
1 *Fig. 5-25. An aperture in*
=A | a conducting cylinder.
SI | Y
I
pal
x
shown in *Fig. 5-25. We seek a solution for the field external to the*
cylinder‘in terms of the tangential components of E over the apertures,
Anticipating that we shall use transforms of the fields, let us define the
“cylindrical transforms” of the tangential components of E on the
cylinder as
A, ‘2x 2
Buono) = xe [ae [de Bsla,e,z)ermterm
' 0 =
L(t e (5-144)
E,(nw) = 5- dc dz E4(a,c,z)e™*e-"*
2m Jo -=
The inverse transformation is
B.(a,4,2) = 2b » int / B,(n,w)e* dw
us -o 1
(5-145)
E,(a,c,2) = x > ent [ B(n,w)e** dw
nase i
Note that these are Fourier series on c and Fourier integrals onz. The i
field external to the cylinder can be expressed as the sum of a TE component and TM component. According to the concepts of Sec. 3-12, the
field is given by
E=-vx F -joeA + vv-A
Y" (5-146)
H=VXA-jweF + - VV-F
jou
where A =u,A, F=uF, (5-147)

CYLINDRICAL WAVE FUNCTIONS 247
We now construct the wave functions A, and F, as
A, = =~ y one [ Sn(W) Hn (p /K? - wi) ef* dw
Ls -*°
“i (5-148)
F,= - k ome f Qn(w) Ha (p Vk? - w)er* dw
which are of the form of Eq. (5-11). We choose the Bessel functions as
H,® to represent outward-traveling waves. We choose the c and z
functions such that the field will be of the same form as Eqs. (5-145).
To determine the f,,(w) and g,(w) in Eqs. (5-148), let us calculate E,
and E, according to Eqs. (5-146). The result is
1 ° -E.(,$2) = yo by one [ (kt - wf (0) Ha (0 VP = wie dw
2rjwe _
Bslo,62) = pe » ene [ [- BE fu(w) Ha (9 ~/E* = w?)
us _ Joe
+ ga(w) VB? = w? Hn? (p Sk? - w| es dw
Since these equations specialized to p = a must equal Eqs. (5-145), we
have
ee 2)
Fale) (k? - w)H,2 (ark? - w?)
< 1 a
(oy = SS ____-_____- | FE, (nw 5-149
nt ea ES | (re) (5-149)
nw a
+ ak? - = wi) B.n0)]
This completes the solution. +
The inversions of Eqs. (5-148) are difficult except for the far zone, in
which case we can use Eq. (5-143). Hence, we have
eck - :
A; = ae » einopn+1f,(-k cos 8)
PCS (5-150)
F,--> ee etjntty, (-k cos 8)
oie In

248 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Z Zz
|I-a.
i} 1
t

Heale~ | *Fig. 5-26. A conducting*

F ‘Lbea- cylinder and (a) an axial

L WwW slot, (b) a circumferential

L ie slot.

| i}
a_T|-o_ an i
(a) ()
Finally, in the radiation zone Eqs. (3-97) apply; hence
er i :
Ee -> jou -- sin 0 » emoj>+1f,(-k cos 0)
re 7
\ "We (5-151)
at
Ey = -jk = sin 0 » emsjntig, (-k cos 6)
Thus, the radiation pattern of apertures in cylinders is relatively easy to
calculate. The only difficulty is that the number of significant terms in
the summation becomes very large for cylinders of large diameter.

To illustrate the theory, let us consider the thin rectangular slot in the
two orientations shown in *Fig. 5-26. For the axial slot we shall assume*
in the aperture

Vv - & <z< z
Ey = - cos (5-152)
aa L afte o< a
2 2
and E, = 0. (This approximates the case of excitation by a rectangular
waveguide.) For a very narrow slot (2-0) the transforms of Eq.
(5-144) become
5 _ VL cos (wL/2)
; Bln) = Ft (Day

CYLINDRICAL WAVE FUNCTIONS 249
and £,(n,w) = 0. From Eqs. (5-149) we then have f,(w) = 0 and
ga(w) = VL cos (wL/2)
. [x? - (Lw)"]a Vk? - w? H,'(a Vk? - w?)
Finally, by Eqs. (5-151) we have the radiation field given by Zs = 0 and
cos ( cos 0) =
_ VLe7* z jnene
Bs = iar (# y » Hitka sin) 153)
1 -|- cos 6 nae
w
which can be further simplified to a cosine series in c. The radiation
pattern in the plane @ = 90° is identical to that of the slitted cylinder; so
for a = 2) the pattern is given in *Fig. 5-20. The ‘‘vertical” pattern in*
the c = 0 plane is almost indistinguishable from the radiation pattern of
the same slot in an infinite ground plane.!
For the circumferential slot of *Fig. 5-26b, we assume in the aperture*
v ~F<e<F
E, = << cos ™? (5-154)
woe -~2<e<$
2 2
and E, = 0. (Again this approximates excitation by a rectangular waveguide.) For a narrow slot (W-0) the transforms of Eq. (5-144)
become
= _ Va cos (na/2)
E,(n,w) = ay (na)?
and E,(n,w) = 0. Then from Eqs. (5-149) and (5-151) we can calculate
the radiation field as
Ea= kV ae-* j” cos (na/2) e*
° Fer sin 0 {x? - (na)*]H, (ka sin 6)
ee (5-155)
R=- Vae-** cot 6 nj” cos (na/2) ein
+ “prka sin 0 (x? - (na)*JH, (ka sin 6)
n=-e
In the principal planes 6 = +/2and c = 0, the field is entirely 6-polarized.
However, in other directions, the cross-polarized component Ey may be
appreciable. The radiation patterns for circumferential slots in reasonably large cylinders are very close to the radiation patterns for the same
1L. L. Bailin, The Radiation Field Produced by a Slot in a Large Circular Cylinder,
IRE Trans., vol. AP-3, no. 3, pp. 128-137, July, 1955.

250 TIME-HARMONIC ELECTROMAGNETIC FIELDS

TAOS

TAA YS\

YX XS
EX OY KX ”
07 LOX ae \ *Fig. 5-27. Radiation patWPAN \"| tern for a circumferential*
(Zar kl | slot of length 0.65. in a
sam conducting cylinder of
SSE | | diameter 3d (same slot
IRSALTTT J in a ground plane shown
Rey
TSO
SSCL
POS
slot in an infinite ground plane. To illustrate this, *Fig. 5-27 shows the*
radiation pattern in the plane @ = 7/2 for a circumferential slot 0.65
long in-a cylinder 3) in diameter. The radiation pattern for the same
slot in an infinite ground plane is shown dashed.

## Section 6-13: Apertures in Wedges
 The problem of diffraction by a conductor is reciprocal to the problem of radiation by apertures in the conductor. By this, we mean that a solution to one of these problems is
readily converted to a solution to the other by using the reciprocity
theorem. We shall illustrate the procedure for the case of conducting
wedges.

Figure 5-28 shows the reciprocal problems of (a) a current element and
a conducting wedge and (b) an aperture in a conducting wedge. To keep
the theory simple, we shall consider only the case of a distant current element and the radiation field of the aperture. For the z-directed electriccurrent element of *Fig. 5-28a the field will be TM to z, expressible in terms*
ofan A =u.y. The incident field is

‘ en skle-r'l
Oo aE
which, when r >> 7’, reduces to
- emake an
Yi = 1] - eite’cos 6 gikp’ sin 8 con (4-#") (5-156)
4ar
This is simply a plane wave incident upon the wedge. The y in this
three-dimensional problem is subject to the same boundary condition
(w = 0) on the wedge as is H, in the two-dimensional problem of Sec.

CYLINDRICAL WAVE FUNCTIONS 251

## Section 5-10: Hence the solution must be of the same form as Eq
 (5-128), that
is,
v= ory. y jrJa(hp! sin 8) sin v(g! - @) sin v(@ - a) (5-157)
‘ ena
where yo = Il Tat kz" con 8
¥ (5-158)
y= om = 1,2,3
2(r - a) py eyes
In terms of y, the field is given by Eqs. (5-18). Thi
tion to *Fig. 5-28a. y Eqs. (5-18). This completes the solu' . obtain the solution to Fig. 5-28b, we apply reciprocity [Eq. (3-35)]*
o the region bounded by the conducting wedge. Because of the boundary conditions on E at the conductor, Eq. (3-35) reduces to
- [[ Bete ds = NE? (5-159)
apert
where the superscripts a and b refer to the fields of Figs. 5-28a and },
respectively. From Eqs. (5-18) and (5-157) we calculate
He = 2 y vjed o(kp” sin 0) cos v(" - a) sin v( - a)
p' (x - a)
Z Z
Il
iy Aperture J
ay |
@ 8 |
| 1 \
| y)
NS Y ~N | Y
Zt | ps 1 | tn
ig if
xX,
@) ()
Fra. 5-28. The reciprocal problems of (a) ® current element and a conducting wedge
and (b) an aperture in a conducting wedge.

252 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Specializing this to the surface c’ = a, we can reduce Eq. (5-159) to
© © a
IE, = - | dz f dp’ -2mvoli” Dy) Felt! sin 0) sin 0(c - a)
-= ° p(x - a)
Finally, fo is given by Eq. (5-158), and in the radiation zone
E.
By= - sin 6
Hence, the 6 component of E in the radiation zone is given by
enikr _ ,
Ey = eG @) ain y vj sin uc - a) f.(k cos 6, ksin @) (5-160)
where fulwju) = | * eset dz I; * Jo(up) dp > Balo,a,2) (5-161)
a °
Note that f,(w,u) is of the form of a Fourier transform onz and a FourierBessel (or Hankel) transform on p.!

In a similar manner, the Z, component of the radiation field can be
obtained by applying reciprocity to *Fig. 5-28a with JI replaced by KI.*
This z-directed magnetic-current element gives rise to a field TE to z,
expressible according to F = u,v. The incident field is then specified by
Eq. (5-156) with‘Y replaced by K. Again the three-dimensional problem
is essentially the same as the two-dimensional problem of Sec. 5-10. The
solution is then of the form of Eq. (5-133), that is,

mo a 1 gi ,
y= aap €.J°J o(kp’ sin 6) cos v(c’ - a) cosv(c - a) (5-162)
, er
where Yo = Kl -- eit’ cont
4nr
(5-163)
v= - som = 01,2
2x - a) ws
The electromagnetic field is found from y according to Eqs. (5-19).
To relate this solution to the field from an aperture in a conducting
wedge, we again apply reciprocity [Eq. (3-35)]. This reduces to
| f (EPH, - E,'H*) ds = KlH (5-164)
apert
where superscripts a and b refer to the fields of *Fig. 5-28a with J replaced*
by Kl, and of *Fig. 5-280, respectively. From Eqs. (5-19) and (5-162) we*

1]. N. Sneddon, “Fourier Transforms,” p. 6, McGraw-Hill Book Company, Inc.,

New York, 1951.

CYLINDRICAL WAVE FUNCTIONS 253
calculate
ak? sin 9 cos 6 So Td ot ,
HH, = Soule a) Yo » €v3°J (kp! sin 8) cos v(c’ - &) cos v(c - a)
2 sin?
He = es vo y €oJ°J o(kp’ sin 0) cos v(c’ - a) cos v(c - a)
Finally, we evaluate Eq. (5-164) and use the radiation-zone relationship
=- = aH,
Es He sin 6
The result is
BR, - eS » i° cos (6 - a)[eos 0 g.(k cos 6, k sin 6)
a J? - a)[cos 69. ,
* = iG a) J” cos u(@ - a@)[cos 6 g.(k cos sin (5-165)
+ jsin 6h,(k cos 6, k sin 6)]
where g.(w,u) = fC eee a Ji (up) dp E,(p,0,2)
=~ be (5-166)
hy(wyu) = [7 ee de f,” Jo(up) dp B, (rs,2)
We now have a complete solution for the radiation field from apertures in
conducting wedges.
As an example, let us calculate the radiation from a narrow axial slot
of length L, as shown in *Fig. 5-29. We shall assume that in the slot*
E, = Va(p - a) cos r (5-167)
is the only tangential component of E.
The f, g, and h functions [Eqs. (5-161)
and (5-166)] are then found to be
f=0 g =0
_ 2nVL cos (wL/2)
hy = 2 (Lu)? J (ua) 7
From Eq. (5-160) we see that Hs = 0, L
and from Eq. (5-165) we have 4
_ . cos [k(L/2) cos 6] igad
Be = f(r) sin 6 Te (EL cos 8)?
y €J° cos v(c - a) J,(kasin@) (5-168)
° Fria. 5-29. A narrow axial slot in a
where v = 4, 1, 34,.... Plots of conducting half plane.

254 TIME-HARMONIC ELECTROMAGNETIC FIELDS
SEER
2 Ss
CSA EIR = 0.16.

AXLE BOATERS
ASKER
HREM Y\

CN \
LTA Ben ta
CARERS ee eal
Sel Ebay

MES Se L |
LL seme
Panes
*Fig. 5-30. Radiation patterns for axial slots in a conducting half plane (the slot in*
an infinite ground plane is shown dashed).
the radiation pattern in the plane 6 = 90° are shown in *Fig. 5-30 for the*
case a = 0 (half plane). The cases a = 0.16) and a = 0.96) are shown,
with the infinite ground-plane pattern shown dashed for comparison.
‘
PROBLEMS

## Section 5-1: Show that'Eq
 (5-12) is a solution to the scalar Helmholtz equation.

## Section 5-2: Show that y = (log p)e~** is a solution to the scalar Helmholtz equation

Determine the TM field generated by this ¥ according to Eqs. (5-18). Sketch the
€ and & lines in a z = constant plane. What physical system supports this wave?
Repeat for the TE case.

## Section 5-3: For two-dimensional fields (no z variation) show that an arbitrary field in a
source-free homogeneous region can be expressed in terms of two scalar wave functions, ¥, and y2, according to Eqs
 (3-79) where

A = wpyi F = upp:
Note that this corresponds to choosing
a(A ep 9 (Ff,
a= -22 (4) y= 22 ()
Dep\ ep ® 2ap\p
instead of Eqs. (3-80).

## Section 5-4: A circular waveguide has a dominant mode cutoff frequency of 9000 megacycles
 What is its inside diameter if it is air-filled? Determine the cutoff frequencies for the next ten lowest-order modes. Repeat for the case c = 4.

## Section 5-5: All the waveguides whose cross sections are shown in Fig
 5-4 are characterized
by wave functions of the form

¥ = Balkop)h(nd)e*itt
where TM modes are determined by Eqs. (5-18) and TE modes by Eqs. (5-19). The
phase constant is given by
kee = VB hep?

CYLINDRICAL WAVE FUNCTIONS 255
Let a denote the inner radius and b the outer radius of the coaxial waveguide of *Fig.
5-4a. Show that for TM modes*
Ba(kpp) = Nn(kpa)In(kep) - Jn(kpa)Nn (kop)
h(ng) = sinng or cosnd
where n = 0,1, 2, ... , and k,isa root of
Inlkpa)Nn(kpb) - In(kpb)N,(kpa) = 0
Show that for TE modes
Ba(kop) = Ny(kpa)In(kop) ~ Jn (koa) N n(kop)
h(nd) =sinnd or cosnd
wheren =0,1,2,. ., and k, isa root of
Tila), (Keb) - Ni (koa) J, (kb) = 0

## Section 5-6: Show that the modes of the coaxial waveguide with a baffle (Fig
 5-4b) are
characterized by the same B,(k,p) functions as the coaxial guide (Prob. 5-5), but for
TM modes
A(nc) =sinn@' n= 4,1, %,2,.-.
and for TE modes
h(ng) = cosng n=0,¥%,1,%,...
where the baffle is at c = 0. The dominant mode is the lowest TE mode with
n=.

## Section 5-7: Show that the wedge waveguide of Fig
 5-4e supports TM modes specified by
y™ = Jn(kpp) sin ng e*7
a 2x 3m
where not, 2%...
0 d0 $0
and k,a is a zero of Jn(kpa). Show that it supports TE modes specified by
yTE = In(kpp) cos np eXthe
2a
h =0,2,%,.-where n=0, $e re
and k,a is a zero of J,(k,a). The guides of Figs. 5-4c and d are the special cases
co = 2m and z, respectively.

## Section 5-8: Show that the cutoff wavelength for the dominant mode of the circular waveguide with baffle (Fig
 5-4c) is
2na
= T16

## Section 5-9: Using the perturbational method of Sec
 2-7, show that the attenuation constants due to conductor losses in a circular waveguide are given by
ee
na V1 - (f./f)?
for all TM modes, and by
a nt -\?
wo a V1 it leres ” (j) |
9a V1 - (f/f)? | np)? - 07 f

256 TIME-HARMONIC ELECTROMAGNETIC FIELDS
for all TE modes. Note that for the ‘‘circular electric’? modes (n = 0) the attenuation decreases without limit as f- ©.

## Section 5-10: Consider the two-dimensional “‘circulating waveguide” formed of concentric
conducting cylinders p = aand p = b
 Show that the wave function
¥ = [AJn(kp) + BN a (kp)]e“in*
specifies circulating modes TM to z according to Eqs. (5-18) if n is a root of
_ B_ Inlka) _ _Jn(kb)
A Na(ka) - -Nn(kb)
Show that the above wave function specifies modes TE to z according to Eqs. (5-19) if
nis a root of
B _ Jilka) _ Ja(kb)
--- = =
A Nika) Ni(kb)

## Section 6-11: For the TM radial wave specified by Eq
 (5-33), show that the radial phase
constant of E, is given by Eq. (5-36), while the radial phase constant of Hc is
a -2)1-(2y 1
e kip) | Wn(kon)I* + IN (koe)?
Show that Eq. (5-37) is also valid for this phase constant.

## Section 5-12: Gonsider the TM radial wave impedances of Eqs
 (5-38) and (5-39). Show
that for large radii
Z4p™ = Z_,™ --> 4
kpp
and that for small radii
. 2 j log =
Zap™ = Zp™* oe\? fig\em
be (Gi) GE) + a] ne
where y = 1.781.

## Section 5-13: Consider the radial parallel-plate waveguide of Fig
 5-5a. For the transmission-line mode (Eqs. (5-45)], one can define a voltage and current as
Vio) = -aE, I(o) = 2xpHy
Show that V and J satisfy the transmission-line equations
av dl :
idee -jobl an -joCV
where L and C are the “static” parameters
b=22 came
Qxp a
Why should we expect circuit concepts to apply for this mode?

## Section 5-14: Consider the wedge guide of Fig
 5-50. For the dominant mode (Eq. (5-49)],
one can define a voltage and current as
Ve) = Espo I(p) = Ha

CYLINDRICAL WAVE FUNCTIONS 257
Show that V and J satisfy the transmission-line equation (Prob. 5-13) with
L = Hee ga
a edo

## Section 6-15: Show that the resonant frequencies of the two-dimensional cylindrical cavity
(no z variation, conductor over p = a) are equal to the cutoff frequencies of the
circular waveguide

## Section 5-16: Following the perturbational method used to derive Eq
 (5-58), show that the
Q due to conductor losses for the various modes in the circular cavity of *Fig. 5-7 are*

rans > nInp
(Qiao = SR + a/d)
Na
ha
7 i np? + (=)
(Qe)ipo = em EY
Fee 2K(1 + 2a/d)
1 alz,3 + (gra/d) 42,5, - n*)
(Qe)or0 = TWhnera\ = c, ealee\e 5, |
ngm ,
on| ("2") + 26 +3 (=) [CA ~]

## Section 5-17: The circular cavity of Fig
 5-7 has dimensions a = d = 3 centimeters.
Determine the first ten resonant frequencies and the Q of the dominant mode if the
walls are copper.

## Section 5-18: Consider the dominant mode of the partially filled radial waveguide of Fig

5-9a. Show that for small a and large p the phase constant is

B~k Vt le = Dada
* NT + (e/a - Ida
Compare this to the uniform transmission-line formula (Eq. (2-66)], using the static
approximations
C= 2mevexp pa td + m(a - 4)
ata -d) bed Qap

## Section 5-19: Consider the dielectric-slab radial guide of Fig
 5-9b. Let « = 4eo and
#1 = Hoanda = do. Which modes can propagate unattenuated in the slab? Repeat
the problem for the coated-conductor guide of *Fig. 5-9c with t = a/2.*

## Section 5-20: For the partially filled circular waveguide (Fig
 5-10a), show that the characteristic equation [Eq. (5-74)] for the n = 1 modes reduces to

{AN i(Kp2b) + BJi(kpab) AN; (Road) + BJ (kp2b)] = 0
where A = kepaJi (kor) Tx(Kepr) - pad (epra)Js (Kepra)
B = kp2Ny(kp2a)Ji(k pra) - kor (pa) Ni (kp2a)

## Section 6-21: Consider the dominant (n = 1) mode of the dielectric-rod waveguide of
Fig
 5-10b. Show that for small a the characteristic equation becomes
(ur + ws) (er + 2)
ist V 2u2e2K o(va)
where w=k? - ko pt =k? - ka?
Note that there is no cutoff frequency.

258 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 6-22: The field external to a dielectric-rod waveguide varies as Ki(vp)
 Using the
results of Prob. 5-21, show that for a small (@ < di), nonmagnetic (#1 = p2) rod
log 2 ~ Late
8 yea ~ Una)? a - @
where y = 1.781. Take e: = 9e2 and a = 0.1), and calculate the distance from the
axis for which the field is 10 per cent of its value at the surface of the rod.

## Section 6-23: Consider the circular cavity with concentric dielectric rod, as shown in Fig

5-3la. Show that the dominant resonant frequency is the smallest root of
LJe(ke) _ 1 [ No(koa)So(koc) - Jo(koa)No(kec)
a Joke) no | No(koa)Jo(koc) - Jo(koa)Na(koc)
For small c/a, show that resonant frequency o, is related to the empty-cavity resonance
he = 2.405
Os = Feu Zor = 2.
. w,- wo 7 No(Zo1) c\t
ding ti a ty (e, - 1) (=
according to we qo Ti(zex) (e (:)
a?
= -1.86(e, - 1) ()
where c = €/eo.
~‘ G
%
wt
d da
cr
b
a
() (6)
*Fig. 5-31. Partially filled cavities.*

## Section 5-24: Consider the circular cavity with a dielectric slab, as shown in Fig
 5-31b.
Show that the characteristic equation for the resonant frequency of the dominant
mode is

ks0 tan ko(d -b) = - tan kb
© €
where Keo? = ko? - (2) ke =k - (2)
a a
Show that when both d and 6 are small
wp fa = (1 - 1/e,)b/d
PONT (ee = 18/4
where wo is the empty-cavity resonant frequency, given in Prob. 5-23, and « = e/eo
and pr = /Ho.

CYLINDRICAL WAVE FUNCTIONS 259
Ee]
iy
Fie. 5-32. Wedge in a cir- a
cular cavity. 0

## Section 6-25: Consider the circular cavity with a conducting wedge, as shown in Fig
 5-32
Show that, for d small, the resonant frequency of the dominant mode is given by
w
fe Qa Ven
where w is the first root of J;(w) = 0 and v = x/(2a - $0). Some representative
values of w are
v 0.5 0.6 0.7 0.8 0.9 1.0
w 3.14 3.28 3.42 3.56 3.70 3.83

## Section 6-26: Figure 5-33a shows a linear density of z-directed current elements along the
zaxis
 Show that the field is given by H = V X A where
Jil
A, = ms Ho (kp)
Show that the field is identical to that produced by the magnetic dipole formed of
z-directed magnetic currents +K aty = -s/2 and -Katy = s/2 in the limit s- 0.

## Section 6-27: Show that the field of the magnetic-dipole source of Fig
 5-33b in the limit
s- Ois given by E = -V X u.y where
kKs *
v= ore Hy (kp) sin &

## Section 5-28: Consider the quadrupole source of Fig
 5-33c in the limit s; > 0 and s2- 0.
Show that the field is given by H = V X u. where
2
y = EEE [- Hake) + Hsp) cos 26)

## Section 6-29: Figure 5-33d represents a source of 2n current filaments, equal in amplitude
but alternating in sign, on a cylinder of radius p = a
 Show that, in the limit a- 0,

260 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Y Y
F Pp
$ vith hs
s
xl x +.-K x
(a) (b)
Y Y
Ty) +7
.
St $1 + TIe o-I
las as! “ye levenr
+I -I-1 47 X +Ie °-I x
fe rT,
+I -I1
(©) (d)
\ *Fig. 5-33. Some two-dimensional sources.*
%
the field is given by H = V X uw where
\ _ al ka\" ;
Y= aga (FY HaGe) sin no

## Section 5-30: Let the cylinder of current in Fig
 5-15 be an arbitrary function of c, but still
independent of z. Show that the field is given by H = V X uy with
«
Hd, AntalkayHa(be)eint - p> a
v= =.
5D Ants haSalkodeind pp <a
Tete
1 :
where A, = x Se sf Jeenine dg
A cylinder of z-directed magnetic currents is dual to this problem.

## Section 5-31: Show that the radiation field from a ribbon of uniform z-directed current
(Fig
 4-25) is given by
. (ka
ne -juopae~? , sin (F cos +)
* V8xrjkp * “(ka/2) cos c
and Hg = -E,/n.

CYLINDRICAL WAVE FUNCTIONS 261

## Section 6-32: Consider the slot antenna of Fig
 4-21, and make the assumption that tangential E in the slot is u.Eo, a constant. Show that the radiation field is

- (ka
2 wise007" sin G cvs #)
‘ V2rjkp -° (ka/2) cos $
and Ey = 7H..

## Section 5-33: Derive the following wave transformations:
°
cos (p sin $) = ) 'nJ n(p) CoS 2nd
n=0
sin (p sin c) = 2 ») Jim4r(p) sin (2n + 1)c
n=0

6-34
 Let the cylinder of *Fig. 5-17 be dielectric with parameters ez, nz. For a TM*
incident plane wave [Eq. (5-105)], show that the scattered field is given by Eq. (5-106)
with

ag = wink) | cadn(kaa) /ckaaTn(kaa) - Jn(ka) (kat o(ka)

"Hn (ka) | ead (kaa) /ekaad (kaa) - H,,?' (ka) /kaH (ka)
and that the field internal to the cylinder is given by
BE, =Ey y jrend n(ap)ei#
n=-%
- 1
=-- k (2)

with on = Fa) {Jn(ka) + duff »\?) (ka))
Note that this solution reduces to the solution for the conducting cylinder when
a 2.

## Section 5-35: Repeat Prob
 5-34 for the opposite polarization, that is, when the incident
field is given by Eq. (5-113). Note that this problem is completely dual to Prob. 5-34;
so the solution is obtainable by using the interchange of symbols of Table 3-2. Note
that the solution reduces to the solution for a conducting cylinder as pe - 0.

## Section 5-36: Show that the solution of Prob
 5-34 in the nonmagnetic case reduces to

~jxEo
Et -~+> -~- (ka)*(e - 1) Ho (kp)
ka 0. 4
where c = ea/'. Repeat for the opposite polarization, using the result of Prob. 5-35.

## Section 6-37: Consider a conducting half plane covering the c = 0 surface and a z-polarized
plane wave of magnitude E> incident at an angle $’
 The solution is given by Eq.
(5-129). Show that the current on the half plane is

a ,
Ju = 2B YS njeeduathe) sin 8
depo. I,

262 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Show that near the edge of the half plane
2 2. c!
TB Eo Nick 8 2
2jko . c' .
and E, me 2Eo ic sin 2 sin 3
Hence, E, vanishes as ~/kp, and J; becomes infinite as 1/./kp. This is a general
characteristic of knife edges.

## Section 6-38: Consider the half plane of Prob
 5-37 with the incident plane wave polarized
transverse to z. The solution is given by Eq. (5-134) Show that the current on the
half plane is

Jo = 2Ho J enin'Fnilko) cos “F
n=0
Show that near the knife edge
»2.
Jp me 2Ho
- 2 cos % sin #
E, mo nHo Vas cos “5 sin 5
where c’ is the angle of incidence and c the angle to the field point. Note that J, is
finite at p = 0, while Fy, becomes infinite as 1/+/kp. This is also a general characteristic of knife edges.

## Section 5-39: Figure 5-34a shows a conducting cylinder with an axially pointing magnetic

dipole Kt on its surface at c = 0, 2 = 0
 Show that the radiation field is given by
s ©
Ey=- Kle-ie 'nj® COS NG _
o* ~ Rear L, Hx" (ka sin 6)
n=0
where c, is Netynann’s number.
Z| ‘ Zz Zz
ap ap
| ca a
| | KL | Au Il
x x x
b>
(a) (b) (c)
Fic, 5-34. Conducting cylinder with (a) axial magnetic dipole on its surface, (b) axial
electric dipole a distance b from the axis, and (c) radial electric dipole on its surface.

## Section 5-40: Consider the axially pointing electric dipole a distance b from the axis of a
conducting cylinder of radius a, as shown in Fig
 5-34b. Show that the radiation field
is given by

=e) cing VY ZaladNnlB) - NolaFn(B) np;
Eo = f(r) sin ) Zola) Nal6) -RaledZa() jngne
nee
where a = kasin @ and 8 = kbsin 6.

CYLINDRICAL WAVE FUNCTIONS 263

## Section 6-41: Consider the radially pointing electric dipole on a conducting cylinder of
radius a, as shown in Fig
 5-34c. Show that in the z = 0 plane (in which Jl lies) the
radiation field is given by

= nj” sin nd
Hpi~ flo) > H,(ka)
n=
The field in other directions has both @ and c components.

## Section 6-42: Figure 5-35a shows a conducting half plane with a magnetic dipole parallel
to the edge, a distance a from it, and on the side c = 0
 Show that the radiation
field is

: 2
Es, = dEKt e7* sin 6 'nj”!?Jnin(ka sin 6) cos 2
4ar 2
n=0
where ', is Neumann’s number.

## Section 5-43: Suppose that the magnetic dipole of Fig
 5-35a points in the x direction
instead of the z direction. Show that the radiation field is then given by
_ _Kle7ikr . on - _ nd ‘
Eg = Parana ) nj”'?J ni(ka sin 6) sin z
n=l
jkKi , .
By = oe cir sin a) enjrl*S'yq(ka sin 8) cos
Anr 2
n=0
Z x
Pp
$
Il
xi}
x
ka
a
Fia. 5-35. A conducting half plane witha Fia. 5-36. Electric current element on the
magnetic dipole on the side c = 0a dis- edge of a conducting wedge.
tance a from the edge.

## Section 5-44: Consider the z-directed electric dipole on the edge of a conducting wedge, as
shown in Fig
 5-36. Show that in the plane of the element the radiation field is given
by

= in
Es = f(p) sin eed
For a half plane, the pattern is a cardioid with a null in the c = 0 direction.



---

## Chapter 6: Spherical Wave Functions

SPHERICAL WAVE FUNCTIONS

## Section 6-1: The Wave Functions
 The spherical coordinate system is the
simplest one for which a coordinate surface (r = constant) is of finite
extent. The usual definition of spherical coordinates is shown in *Fig. 6-1.
Once again we must determine solutions to the scalar Helmholtz equation,*
from which we may construct electromagnetic fields.
In spherical coordinates the Helmholtz equation is
la/ 4 1 af. jay a are 7 mG 3) + sin 0 90 (sin 930) + pramt bag? tH = 9 (6)
Again we use the method of separation of variables and let
‘ ¥ = R(r)H(8)8(9) (6-2)
Substituting this into Eq. (6-1), dividing by y, and multiplying by
r? sin? 6, we obtain
sinto dy dR sn'd/(. dH 1d’ 22 in? A x
aaa aG a) + re (sin oh) + ade? + kr? sin? @ = 0
The c dependence is now separated out, and we let
1d 7
de m (6-3)
where m is a constant. Substitution of this into the preceding equation
and division by sin? 6 yields
1d/,dk 1 d(/.. ,dH m? ae
ag a) + raw odo (0 Ge) ainto t =0
This separates the r and 6 dependence. An apparently strange choice of
separation constant n is made according to
1 d(... ,dH m?
Tawa (8 Gp) ~ ara 7 -ae ey) 6-4)
because the properties of the H functions depend upon whether or not n

SPHERICAL WAVE FUNCTIONS 265
Zz
r
|
‘
Fie. 6-1. The spherical \
coordinate system.
XN | ¥
> |
$a |
x 4
N
is an integer. With this choice the preceding equation becomes
ld dR
_-_-- 2 - re = =<
a i) n(n + 1) + kr 0 (6-5)
which completes the separation procedure.
Collecting the above results, we have the trio of separated equations
d/(_,4ak a _
AG a) + [(kr)? - n(n+ 1)]R =0
1 d/. jd m?
mo 5 io sin oT) + [mcm +1) - an?o i| H=0 (6-6)
ap
qe + mb =0
Note that there is now no interrelationship between separation constants.
The ® equation is the familiar harmonic equation, giving rise to solutions
h(mc). The R equation is closely related to Bessel’s equation. Its solutions are called spherical Bessel functions, denoted b,(kr), which are
related to ordinary Bessel functions by
Ea
b,(kr) = as Buyy(kr) (6-7)
(see Appendix D). The @ equation is related to Legendre’s equation, and
its solutions are called associated Legendre functions. We shall denote
solutions in general by Ln™(cos 6). Commonly used solutions are
L,™(cos 0) ~ P,™(cos 8), Qn™(cos 6) (6-8)
where P,,™(cos 6) are the associated Legendre functions of the first kind
and Q,™(cos @) are the associated Legendre functions of the second kind.
These are considered in some detail in Appendix E. We can now form

266 TIME-HARMONIC ELECTROMAGNETIC FIELDS
product solutions to the Helmholtz equation as

Ymn = bn(kr)Ln™(cos 6)h(md) (6-9)
These are the elementary wave functions for the spherical coordinate
system.

Again we can construct more general solutions to the Helmholtz equation by forming linear combinations of the elementary wave functions.
The most general form that we shall have occasion to use is a summation
over possible values of m and n

0 = YY Contin
= YY Cornba(ler)Lnm (cos aYA(mg) (6-10)
where the C,,,, are constants. Integrations over m and n are also solutions to the Helmholtz equation, but such forms are not needed for our
purposes.

The harmonic functions h(mc) have already been considered in Sec.

## Section 4-1: Ifa single-valued y in the range 0 to 27 on c is desired, we must
choose h(mc) to be a linear combination of sin (mc) and cos (mc), or of
emand e~"*, with m an integer
 A study of solutions to the associated
Legendre equation shows that all solutions have singularities at 6 = 0 or
6 = m except the P,”(cos 6) with n aninteger. Thus, if y is to be finite
in the range 0 to 7 on 6, then n must also be an integer and L,”(cos 6)
must be P,*(cos 6). The spherical Bessel functions behave qualitatively
in the same manner as do the corresponding cylindrical Bessel functions.
Thus, for k real, j7,(kr) and n,(kr) represent standing waves, ha‘ (kr)
represents an inward-traveling wave, and h,)(kr) represents an outwardtraveling wave. Incidentally, it turns out that the spherical Bessel
functions are simpler in form than the cylindrical Bessel functions. For
example, the zero-order functions are

jo(kr) = SPB mer) =
kr gkr (6-11)
no(kr) = - SSFP payor) = kr jkr
The higher-order functions are polynomials in 1/kr times sin (kr) and
cos (kr), which can be readily obtained from the recurrence formula.
The only spherical Bessel functions finite at r = 0 are the j,(kr). Thus,
to represent a finite field inside a sphere, the elementary wave functions
are
Yn = ju(kr)P»™(cos 6)e™* - r = 0 included (6-12)

SPHERICAL WAVE FUNCTIONS 267
with m and n integers. To represent a finite field outside of a sphere, we
must choose outward-traveling waves (proper behavior at infinity).
Hence,

Wn = ha (kr)P,™(cos dem? r- o included (6-13)
with m and n integers, are the desired elementary wave functions.

To represent electromagnetic fields in terms of the wave functions y,
we can use the method of Sec. 3-12. This involves letting y be a rectangular component of A or F._ The z component is most simply related
to spherical components; hence the logical choice is

A = uy = u,v cos 6 - uy sin 6 (6-14)
which generates a field TM to z Explicit expressions for the field components in terms of y are given in Prob. 6-1. The dual choice is

F = uy = u,ycos 6 - ueysin 6 (6-15)
which generates a field TE to z. Explicit expressions for the field components are given in Prob. 6-1. An arbitrary electromagnetic field in
terms of spherical wave functions can be constructed as a superposition
of its TM and TE parts.

An alternative, and somewhat simpler, representation of an arbitrary
electromagnetic field is also possible in spherical coordinates. Suppose
we attempt to construct the field as a superposition of two parts, one TM
tor and the other TE tor. For this we choose A = u,A, andF = u,F,,
with the field being given by Eq. (3-79). The A, and F, are not solutions
to the scalar Helmholtz equation, because V?A, # (V?A),. To determine
the equations that A, and F, must satisfy, we return to the general equations for vector potentials [Eqs. (3-78)]._ For the magnetic vector potential we let A = u,A, and expand the first of Eqs. (3-78). The @ and c
components of the resulting equation are, respectively,

Ar ph OAs _ _ Oot
ar 00 "3p 06 arae-S
where © is an arbitrary scalar. Note that the above two equations are
satisfied identically if we choose
az, _ OA;
gee = or (6-16)
Substituting this into the r-component equation obtained from the expansion of Eq. (3-78), we have
0°A, 1 Of. (0A, 1 0?A, oA 8
art + Fin 6 90 (sin 8 *) + rsint 6 oe? +BA,=0 (6-17)

268 TIME-HARMONIC ELECTROMAGNETIC FIELDS
It readily can be shown that this equation is
A,

(V? + k?) = 0 (6-18)
so A,/r is a solution to the scalar Helmholtz equation. A dual development applies to the electric vector potential. To be explicit, if we take
F = u,F,, substitute into the second of Eqs. (3-78), and choose

oF,
-sp = Cor 2e oF (6-19)
we find that (V? + k?) ' =0 (6-20)
is the equation for F,. Thus, electromagnetic fields can be constructed
by choosing
A = ry F =r (6-21)
where r = u,r is the radius vector from the origin and the y’s are solutions to the Helmholtz equation. The field is found from the above
vector potentials by Eq. (3-79), which is explicitly
E= -vxw+ivxvxw
1 (6-22)
H=vxwe+3,V xv x
These we shall find sufficiently general to express any a-c field in a sourcefree homogeneous region of space.

The y’s of Eqs. (6-22) are always multiplied by 7, and, because of this,
it is convenient to introduce another type of spherical Bessel function,
defined as

Bakr) = krba(hr) = 4]8” Basa) (6-23)
These are the spherical Bessel functions used by Schelkunoff.! Their
qualitative behavior is the same as the corresponding cylindricat Bessel ~
function. The differential equation that they satisfy is
@ 4, nntl))p _

[# +h- 7 |B, =0 (6-24)
which can be obtained by substituting for b, in terms of B, in the first of
Eqs. (6-6). General forms for the A, and F, in terms of the spherical

1§. A. Schelkunoff, ‘Electromagnetic Waves,” pp. 51-52, D. Van Nostrand Company, Inc., Princeton, N.J., 1943,

SPHERICAL WAVE FUNCTIONS 269
Bessel functions of Eq. (6-23) are

Y, CunBa(kr)Lnm(cos 8h (mg) (6-25)
where the Cn,, are constants. The considerations involved in choosing
specific forms for B,(kr), Ln™(cos 6), and h(m@) are the same as those used
in Eqs. (6-12) and (6-13).

For future reference, let us tabulate explicit formulas for finding the
field components in terms of A, and F,. Letting A = u,A, and F = u,F,,
and expanding Eqs. (3-79), we obtain

= 1 ce 2
E, = j (= +k ) A,
-1 oF, , 10°A,
Ee= rsin 6 06 + 5; 5r a0
1 oF. 1 @A
Es =-324+5->-5555
: ie gr sin @ dr 0b (6-26)
H, = (33+ w)F,
-_ 1 0A, , 1 OF,
He = an ag + Erdr 00
104A, 1 oF,
He= - 7 a9 + isin 0 or 86
When F, = 0, that is, when only A, exists, we have a field TM to r.
Similarly, when A, = 0, the above equations represent a field TE to r.

## Section 6-2: The Spherical Cavity
 Figure 6-2 shows the spherical cavity,
formed of a conducting sphere of radius a enclosing a homogeneous dielectric «, ». We shall find it possible to satisfy the boundary conditions
(tangential components of E vanish at r = a) using single wave functions.
For modes TE to r we choose
F, = F.(kr)P."(cos 6) | cos me Zz

sin md

(6-27)
where m and n are integers. The J,
is chosen because the field must be
finite at r = 0; the P,™ is chosen be- 7
cause the field must be finite at 6 = 0 y
and z. The field components are
then found from Eq. (6-26) with
A, = 0 and F, as given above. Note x
that Ep = Ez; = Oatr=aif

JZ n(ka) = 0 (6-28) Fig, 6-2, The spherical cavity,

270 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Tasie 6-1. ORDERED ZEROS Unp OF Jn(u)

N 1 2 3 4 5 6 7 8
AN uieistesieat
1 4.493 5.763 6.988 8.183 9.356 | 10.513 | 11.657 | 12.791
2 7.725 9.095 | 10.417 | 11.705 | 12.967 | 14.207 | 15.431 | 16.641
3 10.904 12.323 | 13.698 | 15.040 | 16.355 | 17.648 | 18.923 | 20.182

4 14.066 15.515 | 16.924 | 18.301 | 19.653 | 20.983 | 22.295

5 17.221 18.689 | 20.122 | 21.525 | 22.905

6 20.371 21.854
Hence ka must be a zero of the spherical Bessel function. The denumerably infinite set of zeros of J,(u) are ordered as uny. Table 6-1 gives the
lower-order zeros.

We now satisfy the boundary conditions by choosing

u
k = Ue .

a (6-29)
which is the condition for resonance. Hence, the TE tor mode functions
are

r cos mp
(Fans = In (tar 2) Pamtoos 9) { 2° m4) (6-30)
‘\.
where m= 0, 1,2,...57=1,2,3,... ;andp=1, 2,3,....
The field is given by Eqs. (6-26) with A, = 0.
Ifan A, is.chosen of the form of Eq. (6-27), we generate a field TM tor.
The boundary conditions Ey = E, = 0 at r = aare then satisfied if
Tika) = 0 (6-31)
soka must be a zero of the derivative of the spherical Bessel function for
TM modes. The denumerably infinite set of zeros of J/(u’) are ordered
as u;,, and the lower-order ones are given in Table 6-2.
Tape 6-2. Orverep Zeros u',, or J/,(w’)
bi fig 2 3 4 5 6 7 8
gases icaseaacaasenaepoteecaanasenans acaeaaaasavadpasseeenaisiasta panastaaneistn Uaasisssieaadspusiassiseeaied stntaastesiaa
1 2.744 3.870 4.973 6.062 7.140 8.211 9.275 | 10.335
2 6.117 7.443 8.722 9.968 | 11.189 | 12.391 | 13.579 | 14.753
3 9.317 10.713 | 12.064 | 13.380 | 14.670 | 15.939 | 17.190 | 18.425
4 12.486 13.921 | 15.314 | 16.674 | 18.009 | 19.321 | 20.615 | 21.894
5 15.644 17.103 | 18.524 | 19.915 | 21.281 | 22.626
6 18.796 20.272 | 21.714 | 23.128
7 21.946

SPHERICAL WAVE FUNCTIONS 271

Our boundary conditions are now satisfied by choosing

_ Une
k= oad (6-32)
which is the condition for resonance. The TM to r mode functions are
therefore
a Rifas Pe cos mp _
(A,)map = Vin (v4 i) P,™(cos 0) | in al (6-33)
where m= 0, 1, 2,...;n=1, 2,3,...;andp=1, 2,3,....
~ The field is given by Eqs. (6-26) with F, = 0.
The resonant frequencies of the TE and TM modes are found from
Eqs. (6-29) and (6-32), respectively. Letting k = 2rf, ~/eu, we have
u,
QW. = 5 =
2ra v7 eu (6-34)
(fm, = aes
i ae Ee or
Note that there are numerous degeneracies (same resonant frequencies)
among the modes, since f, is independent of m. For example, the three
lowest-order TE modes are defined by
(F,)oaa = Si (4.493 A) cos 6
(For = Ji (4493 4) sin 8 cos
(Ft = J (4498 r) sin 6 sin c
where superscripts “even” and ‘odd’ have been added to denote the
choice cos mc and sin mc, respectively. These three modes have the
same mode patterns except that they are rotated 90° in space from each
other. The next higher TE resonance has a fivefold degeneracy, the
modes being ordered (0,2,1), (1,2,1) even, (1,2,1) odd, (2,2,1) even, and
(2,2,1) odd. In this case there are two characteristic mode patterns.
For each integer increase in n, the degeneracy increases by two, since
P,™(cos 6) exists only for m <n. The situation for TM modes is analogous.

We see by Eqs. (6-34) that the resonant frequencies are proportional
to the ua, and uj. Hence, from Tables 6-1 and 6-2 it is evident that the
modes in order of ascending resonant frequencies are TMmnaa, TMm,2,1,
TEnaa, TMn3,1, TEn,2,1, and soon. The lowest-order modes are there

272 TIME-HARMONIC ELECTROMAGNETIC FIELDS
SE, =
Ce Coes, =
(~~) Vf yoey?
-, Lf. (3.) ‘1
aay, \ \eer “hy
GS SEY
EES ' Ss
H-e Se
*Fig. 6-3. Mode pattern for the dominant modes of the spherical cavity.*
fore the three TM,,1,, modes. Except for a rotation in space, these three
modes have the same mode pattern, which is sketched in *Fig. 6-3.
The Q of the lowest-order modes is also of interest. For this calculation, consider the TMo,1,1 mode. The magnetic field is given by*
H,=14, (2.744 4) sin 6
r a
Following the procedure of Sec. 2-8, we calculate the stored energy as
Ww = 20m =u [ff Har
- wf de i: do f dr Hg?r?sin 0
The @ ant integrations are easily performed, giving
w = 8, [pr (2744 *) ar
\ 3 0 a
This last integral is evaluated as!
i, * Jt(kr) dr = $ [I:%(ka) - Fo(ka)I(ka)]
0
which, for ka = 2.744, is numerically equal to 1.14/k. Thus, the stored
energy is
_ Stu
W= 3, (1.14) (6-35)
The power dissipated in the conducting walls is approximately
8a = ap HI? ds = w@ 8 7,2(2.744) (6-36)
3
Hence, the Q of the cavity is
oW (1.14) Lu]
-Q == = - = 10S 6-37
o- k@d 2 (2.744) R 63
1B, Jahnke and F. Emde, “Tables of Functions,” p. 146, Dover Publications, New
York, 1945 (reprint).

SPHERICAL WAVE FUNCTIONS 273
Comparing this with Eqs. (5-58) and (2-102), we see that the spherical
cavity has a Q that is 25 per cent higher than the Q of a circular cavity of
height equal to its diameter and 35 per cent higher than the Q of a cubic
cavity. The Q’s of higher-order modes are given in Prob. 6-4.

## Section 6-3: Orthogonality Relationships
 In many ways the Legendre polynomials are qualitatively similar to sinusoidal functions. For example,
the P,,(cos @), sometimes called zonal harmonics, form a complete orthogonal set in the interval 0 to z on 6. An arbitrary function can therefore
be expanded in a series of Legendre polynomials in this interval, similar
to the Fourier series in sinusoidal functions. The functions P,”(cos 6)
cos md and P,™(cos 6) sin mc, sometimes called tesseral harmonics, form
a complete orthogonal set on the surface of a sphere. Hence, an arbitrary function defined over the surface of a sphere can be expanded in a
series of tesseral harmonics. We shall, in this section, derive the neces
_ sary orthogonality relationships.
For our proof it is convenient to use Green’s theorem [Eq. (3-44)],
which is
2, OW _ " 2
ff (32 - 4238) as = fff wavy - 40% ar 6-38)
The right-hand side vanishes if ¥: and y2 are well behaved solutions to
thesame Helmholtzequation. Assuming this to be the case and applying
Eq. (6-38) to a sphere of radius 7, we have
is . . Ope oy
2 -_ - - = =
r [ ae f d' sin a(n or yo a) 0 (6-39)
In particular, choose
vi = g.(kr)P.(cos 0) v2 = j,(kr)P,(cos @)
which are solutions to the Helmholtz equation. Equation (6-39) then
becomes
Qakr*(jng?, - Jol”) in P,P, sin 0d0 =0
This must be valid for all r; so, if n # g, the integral itself must vanish.
Hence,
fr P,,(cos 6)P,(cos 6) singd9=0 nx¥q (6-40)
When n = g, we have
7 : 2
rn 2 = - 6-41
i, [P,.(cos 6)]? sin 6 d' nf (! )
which can be obtained by using Eq. (E-10) and integrating by parts.

274 TIME-HARMONIC ELECTROMAGNETIC FIELDS
To obtain a Legendre polynomial representation of a function f(6) in
0 to z on 6, we assume
f(0) = ) a,Pa(cos 8) 050m (6-42)
n=0
Multiply each side by P,(cos 6) sin 6 and integrate from 0 to z on 6.

i f(0)P,(cos 6) sin 6d@ = de Ie P,(cos @)P,(cos 6) sin 6 d'
Each integral on the right vanishes by Eq. (6-40), except the one n = p,
which is given by Eq. (6-41). The result is

a, = tt i * {(0)Pa(cos 8) sin 0 d6 (6-43)
0)
Equation (6-42) with the coefficients determined by Eq. (6-43) is called a
Fourier-Legendre series. It converges in the same sense as the usual
Fourier series.
For a more general result, define the tesseral harmonics as
‘ e = p.m
\ T nn*(8,c) = P,™(cos 8) cos mo (6-44)
‘\ Tmn°(0,c) = Pr™(cos 6) sin md
and assume two solutions to the Helmholtz equation as
NM
V1 = In(kr)Tmn'(9,6) 2 = Folk) T yo'( 8,0)
These are well behaved within a sphere of radius 7; hence Eq. (6-39) applies
and reduces to
-. a Qe ® om acs
kr? (Gnd - Jan) f de i dO Tmn*T yp Sin 0d6 = 0
The term outside the integral vanishes for arbitrary r only when n = g;
hence
Jy" de JF 49 Tmni(6,0)Tos(0,0) sin @=0 ng
For the c integration, we have the known orthogonality relationships
fe" sin mdc sin pp dd = 0
ar. . _ a _ {0 mp
i sin me sin pp dp = f, cos mb cos pe ds = | ° m=p#0
(6-45)

SPHERICAL WAVE FUNCTIONS 275
Hence, the final orthogonality can be expressed as
Qn ©
do 8 Tmn°(8,) T'pq°(8,) sin 8 = 0
fy” Ic )T'50°(8,8) 6-46)
A d' ih 48 Tnn'(8,$)T pai(8,6) sin@=0 mn# p,q
where i = coro. When™m,n = p, g, we have
4a
ay m=0,i=e
Qn z . . 2n +1 ,
| d' i 48 [Toni(@,0)P? Sin = DT On mt 7
ImFifn-m! ™
(6-47)
which can be obtained by using Eq. (E-16) for P,™ and integrating on 6
by parts.

A two-dimensional Fourier-Legendre series can now be obtained for a

function f(6,c) on a spherical surface. For this we assume
40.8) = YY C@neTnat + bmn Tne’)
n=0m=0
= YY Gna cos mb + bmn sin md)Pxm(cos 6) (6-48)
n=0m=0
multiply each side by 7’,,,' sin 6, and integrate over 0 to 27 on c and 0 to
xon'. Allterms except those having m,n = p, q vanish by Eqs. (6-46),
and by Eqs. (6-47)
_ 2n+1 [? *
don = mitt f ao [ d' f(8,6) Pa(cos 6)
_ 2n+1(n-m)! [* 7 . .
Onn = Eyl fy d' | do S(9,6)Tmn°(8,) sin @ (6-49)
_ 2n+1(n-m)! [2 * > .
bun = SG mt fo 2 fy GLG.4) Tmn(0, 6) sin 0
The series Eq. (6-48) with coefficients Eqs. (6-49) converges in the same
sense as the usual Fourier series.

Still another orthogonality relationship is of interest when dealing with
vector fields. To establish the desired relationship, we start from the
Lorentz reciprocity theorem [Eq. (3-34)], which is

fp (E* x H® - E’ x He)-ds =0 (6-50)
valid when no sources are within the surface of integration.! Fer the

1 We could just as well use the vector Green’s theorem, Eq. (3-46).

276 TIME-HARMONIC ELECTROMAGNETIC FIELDS
a and b fields, choose those obtained from Eqs. (6-26) with F, = 0 and
Ay = In(kr)Tmn'(8,6) AP = Felkr)Trei(8,0)
respectively. Applying Eq. (6-50) to a sphere of radius 7, we obtain
lis, a) [er 7 AT mui IT pg, 1 AT mn OT pe!
SII q - Sida nt ee oe Cen Se) =
ced I rf as ao(sino fap St rd Og =p ) 0
For arbitrary r and n ¥ gq this equation can be satisfied only if the integral vanishes. Also, by the orthogonality relationships of Eqs. (6-45)
the integral vanishes ifm ~ pandi #j. Thus,
an * AT mn’ OT pg. 1 OT mnt OT pg
I ao f ao (sin o a at sind ap 06) °
m,nt#~p,aj (6-51)
When m,n, = p,q,j, we have
on * . OT mn’ \? 1 (dT mn'\?
I a ff ao[ sin o 255" ) + i(33) |
4an(n + 1) m=0,i=e
ete (6-52)
~ ) 2nn(n + 1) (n+ m)! #0
‘ n+l (n-mi ™
s,
which can be obtained by integrating once by parts and using Eq. (6-47).

## Section 6-4: Space, as a Waveguide
 We have seen that in a complete
spherical-shell region (0 < 6 < 7,0 < c < 2z7) only spherical wave functions of integral m and n give a finite field. The fields specified by these
wave functions can be thought of as the “modes of free space.” When
viewed in this manner, the space is often called a spherical waveguide,
even though there is no material guiding the waves.
The spherical coordinate system is defined in *Fig. 6-1. There exists a*
set of modes TM to r, generated by
; P A. (kr)

(Ay) mn? = Tran'(9,6) | A (kr) (6-53)
where n = 1, 2,3,...;m=0,1,2,...,n;andi=eoro. The
T functions are defined by Eqs. (6-44), and the field is given by

Hi = VX u(Aret ER =v x HE (6-54)

WE
Inward-traveling waves are represented by the A,“ and outwardtraveling waves by the #,@. In the dual sense there exists a set of

SPHERICAL WAVE FUNCTIONS 277
modes TE to r, generated by
. , A, (kr)

(Fr)mn = Tnni(8,4) Westie (6-55)
where n = 1, 2,3,...;m=0,1,2,...,n;andi=eoro. The
field is given by

E™ =v xu(Pei HI =--- vx Er (656)
jou
The set of TM plus TE modes is complete, that is, a summation of them
can be used to represent an arbitrary field in a source-free region. Mode
patterns for the TMo: and TE,, modes are sketched in *Fig. 6-4. The*
TM and TE modes are dual to each other; so an interchange of E by H
and H by -E in *Fig. 6-4 gives the TE: and TMo mode patterns.*

The spherical modes are qualitatively similar to the radial modes of
Sec. 5-3. Thereis no well-defined cutoff wavelength but rather a “cutoff
radius.” To illustrate, consider the radially directed wave impedances
for the TM modes

Eyt + . ne?!
Zym = Be Bet, BAO" br)
Hy Het A, (kr) (6-57)
sad a axel elf ea nr cP)
~ Hs He am A (kr)
where the superscripts + and - denote outward- and inward-traveling
waves, respectively. Note that, for realy and k, Z_,™ = (Z,,™)*. For
Bee NP
to) Le
MEE FBS
1 hygbe er TERN
NWP LEB, IND,
SS VATE GON RRS
as, VA ne? LERAY +
YAS Li Ma eS a” YN
NEO SHARE OS
AN HT) ACRE
WY 1 OW OAR CRA Yt
YW; \ RASS Cepia 1
/ We Lega
QRS CEES”
Sy fe re ia
SS =y c =e 3 SG
~s.J Len
@ & a----->
Fia. 6-4. Mode patterns for the (2) TMo: and (b) TEo3 modes of free space.

278 TIME-HARMONIC ELECTROMAGNETIC FIELDS
the TE modes the radially directed wave impedances are
Zy7h = Eat = - Eyt = --jn A. (kr)
H,t Hot A,” (kr)
(6-58)
ZfB= - Boe = Ee- = jn AO (kr)
7 Hy He A" (kr)
The behavior of these wave impedances is qualitatively similar to the
behavior of the two-dimensional wave impedances, illustrated by Fig.

## Section 5-6: In other words, the wave impedances of Eqs
 (6-57) and (6-58) are
predominantly reactive when kr < n, and predominantly resistive when
kr >n. The value kr = n is the point of gradual cutoff. Note that
this cutoff is independent of the mode number m.

The frequency derivative of the various wave impedances is of interest
for determining the bandwidth of various devices (see Sec. 6-13). A
novel way of representing this frequency derivative, which also illustrates
the above cutoff phenomenon, was devised by Professor Chu.! He took
the wave impedances and, using the recurrence formulas for spherical
Bessel functions, obtained a partial fraction expansion. For example,
for the TM impedance of outward-traveling waves

n 1
Bee ea + mot, i
“jet
\ :
; (6-59)
1
oe rs
jkr 1
Fer +1
This can be interpreted as a ladder network of series capacitances and
shunt inductances, as shown in *Fig. 6-5a. The equivalent circuit for the*
TE,.n modes is shown in *Fig. 6-5b. Those of us familiar with filter theory*
will recognize the equivalent circuits as high-pass filters. The dissipation
in the resistive element at the end of the network represents the transmitted power in the field problem. It is therefore apparent that, for
fixed r, the higher the mode number 7 the less easily power is transmitted
by a spherical waveguide mode.

1L. J. Chu, Physical Limitations of Omnidirectional Antennas, J. Appl. Phy., vol.

19, pp. 1163-1175, December, 1948.

SPHERICAL WAVE FUNCTIONS 279
er
oe Ens
oo - ----]f- pe pace ae oe Sa
7M lth ur
2ma -~ arr 20-5 R=7
(a)
_ er er
CaF 20-5
o-_-___--. fE <j - - --=
“pr pe
Li i E “}
(4)
Fia. 6-5. Equivalent circuits for the (@) TMmn and (b) TE,,, modes of free space.

A quality factor Q, fer modes of order n can now be defined as

20. =

= Wee

Qn = = (6-60)
20 Wm
St en >
e

where W, and W,, are the average electric and magnetic energies stored
in the C’s and L’s, and @ is the power dissipated in the resistance. In
TM waves ¥. >‘W., while in TE waves W, > ‘W.. However, the two
cases are dual to each other; so the Q’s of TM waves are equal to the Q’s
of the corresponding TE waves. An approximate calculation of the Q’s
for Q > 1 is shown in *Fig. 6-6. Note that for kr > n the wave impedances are low Q and for kr < n they are high Q. This again illustrates*
the cutoff phenomenon that occurs at kr = n.

## Section 6-5: Other Radial Waveguides
 A number of structures capable of
supporting radially traveling waves can be obtained by covering 6 = con.
stant and c = constant surfaces with conductors. Such “radial waveguides” are shown in *Fig. 6-7.

We can have waves outside or inside a single conducting cone, as shown*
in *Fig. 6-7a and b. These two cases are actually a single problem with*
two different values of 6. The fields must be periodic in 2x on c and

|
ATA
ERAN
aN NN
“AAAS
ARN
ISS
tee cole
ieee
a ee te eos

SPHERICAL WAVE FUNCTIONS 281
Zz
Z| zl <I>
|
~ |
| ea ,,
9;
[x ;
(a) (0) (c)
72 | Z|
be |
behy ee
en
dort pane ‘
Th
<{
SB, NS
(d) e) (ta)
*Fig. 6-7. Some spherically radial waveguides. (a) Conical (waves external); (b)*
conical (waves internal); (c) biconical; (d) coaxial; (e) wedge; (f) horn.
Because of a scarcity of tables for the eigenvalues », it is difficult to obtain
numerical values. The field components are, of course, obtained from
the A, and F, by Eqs. (6-26).

The biconical and coaxial guides of *Fig. 6-7c and d are again a single*
mathematical problem. Now both @ = 0 and @ = z are excluded from
the region of field; so two Legendre solutions, P.™(cos @) and Q,™(cos @),
or P,™(cos 6) and P,”(- cos 6), are needed. Choosing the latter two
solutions, we find modes TM to r defined by
(A,)ms = [P."(cos @) P.™(-cos 6:) - P»™(-cos 6) P,(cos 6:)]

cosmc| » & 4
| sae 3 BL (kr) (6-65)
where m = 0, 1, 2, . . . , and the v are determined by the roots of
P.™(cos 62)P."(- cos 61) - P,»™(- cos 62)P»(cos 61) = 0 (6-66)
|

282 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Similarly, for the modes TE to r we have

_ m dP.™(- cos) pay _ dP,™(cos 61)
(Fy) mo = [P. (cos 6) in P,™(- cos 6) Tae

cos m}| » _
(3° ms A, (kr) (6-67)

where m = 0, 1, 2, . . . , and the v are determined by the roots of
dP,™(cos 62) dP»™(- cos 61) _ dPs™(- cos 82) dP.™(cos 61) _
Wd da 88)
Again the field components are found fromthe A, and F, of Eqs. (6-65)
and (6-67) according to Eqs. (6-26).

The dominant mode of the biconical and coaxial guides is a TEM, or
transmission-line, mode. The eigenvalues m = 0, v = 0 satisfy both
Eqs. (6-66) and (6-68), but the A, and F, of Eqs. (6-65) and (6-67) vanish.
We could redefine Eq. (6-65) such that the limit v > 0 exists, but instead
let us separately define the TEM mode as a TMoo mode defined by

a i %
(A,)oo = Qoleos #)Ho(kr) = log cot 5 (Fae (6-69)
The field components of this mode, determined from Eqs. (6-26), are
XX
~ EF = ih etikr
f wer ae (6-70)
‘ Fut bike
Ae + sino”
where the upper signs refer to inward-traveling waves and the lower signs
to outward-traveling waves. The wave impedance in the direction of
travel is
Egt
+= oO
z Hyt
1p = (6-71)
Fists Ee
a a
which is the same as for TEM waves on ordinary transmission lines.
The characteristic impedance defined in terms of voltage and current is
of greater interest. Ata given, the voltage is defined as
_ fr _o cot (61/2) sine 7
vf Eor a6 = jn log (9,79) &" (6-72)
and the current as
2
I= hk "Hy rsin 0d = F2njexie (6-73)

SPHERICAL WAVE FUNCTIONS 283
At small r these are the usual circuit quantities. The characteristic
impedance is
V+ V- oa cot (01/2)
Zo= = - = 2,8 cot (,/2) (6-74)
Note that the various equations are the same as for the usual uniform
transmission lines. For this reason the biconical and coaxial radial lines
are called uniform radial transmission lines.

Spherical waves on the wedge waveguide of *Fig. 6-7e exist for all 6*
but only for restricted c. Hence, the wave functions will contain only
the P,”(cos 6) with n an integer and w determined by the boundary conditions. We then find TM modes defined by

(A,)nw = Pa®(cos 8) sin wp A, (kr) (6-75)
where n = 1, 2,3, ..., and

= Pr
w= h (6-76)

with p = 1, 2,3, .... The TE modes are defined by

(Fr)nw = Px®(cos 6) cos wo H,, (kr) (6-77)
where n = 1, 2, 3,... , and w is given by Eq. (6-76) with p = 0, 1,
2,.... There is no TEM spherical mode, the TEM mode being a
cylindrical wave defined by Eqs. (5-48) and (5-49).

Finally, the spherical-horn waveguide of *Fig. 6-7f will require Legendre*
functions L,”(cos @) of nonintegralyandw. The TM modescan be defined
by Eqs. (6-65) and (6-66) with m changed to w and only the sin wc functions allowed. The values of w are those of Eq. (6-76). Similarly, the
TE modes can be defined by Eqs. (6-67) and (6-68) with m changed to w
and only the cos w@ functions allowed. Again, w is given by Eq. (6-76).
There will, of course, be no TEM mode.

## Section 6-6: Other Resonators
 Resonators having modes expressible in terms
of single spherical wave functions can be obtained by closing each of the
radial waveguides of *Fig. 6-7 by one or two conducting spheres. Some*
examples are shown in *Fig. 6-8. The fields in each case can be expressed*
in terms of mode functions which are the same as for the radial waveguides of the preceding section, except that the traveling-wave functions
A, (kr) and A,®(kr) are replaced by standing-wave functions T A(kr)
andN,(kr). Numerical calculations are hampered by a scarcity of tables
of eigenvalues.

Let us calculate the Q’s for the dominant modes of the first three cavities of *Fig. 6-8. For the hemispherical cavity of Fig. 6-8a, the dominant*
mode is the dominant TM to r mode of the complete spherical cavity,

284 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Z 0
2| Zz Hy
9
(VV
-.- [a L
(a) (8) (2)
Z| Zz |
|
Pty
‘
<\ 4 a,
\ 1
(@ © 2)
*Fig. 6-8. Some cavities having modes expressible in terms of single spherical wave*
functions. (a) Hemispherical; (b) hemisphere with cone; (c) biconical; (d) conical;
(e) wedge; (f) segment.
considered in Sec. 6-2. The magnetic field is
He =13, (2.748 ) sin 0
Tr a
and the stored energy is one-half that for the complete spherical cavity
[Eq. (6-35)]; hence
= tm
w= SF (114)
The power dissipated in the hemispherical part of the walls is one-half
that dissipated in the walls of the complete spherical cavity; hence
(Pa)vemiepnore = att (1.13)
The power dissipated in the plane wall is
(douse = 82 fH ,__, 7dr = G82x(0.571)

SPHERICAL WAVE FUNCTIONS 285
Thus, the Q of the resonator is
ow 7]
= = = 0.573 = 6Q 8, a (6-78)
If we compare this with the Q of a rectangular cavity [Eq. (2-102)] and
with the Q of a circular cavity [Eq. (5-58)] we see that, for the same
height-to-diameter ratios, the hemispherical cavity Q is only 3.2 per cent
higher than the rectangular cavity Q, and 4.5 per cent lower than the
circular cavity Q. The hemispherical cavity Q is 54 per cent less than
the spherical cavity Q, but we have removed the mode degeneracy.
From Tables 6-1 and 6-2 we find that the second resonant frequency is
1.41 times the lowest resonant frequency for the hemispherical cavity,
compared to approximately 1.58 for the rectangular and circular cavities.
The cavities of *Fig. 6-8b and c are theoretically important because they*
have circuit terminals available. In other words, a voltage and current
calculated at the cone tips have the usual circuit theory interpretation.
The dominant mode
_ Acosk(a - r) _ . , sin k(a - 7)
He = - rsind Ba=jnA r sin @
will be excited if the cavity is fed across the cone tips. The voltage
seen by the source is
Via = lim ipa Er d@ = 2njAZo sin ka
roo Jam
where Zp is the characteristic impedance [Eq. (6-74)]. The current at
the source is
: 20
Tn = lim f, Hor d' = 2nA cos ka

r>0 JO

Hence, the input impedance seen by the source is
Vin _

Zin = Z~ = Jo tan ka (6-79)
which is the usual formula for the input impedance of a short-circuited
uniform transmission line. (We saw in the preceding section that the
TEM mode of the biconical guide is a uniform transmission-line mode.)
The resonances occur when ka = nz/2, or

nr
o, = - (6-80)
"2a Ven
where n = 1, 2,3, .... In the loss-free case, the input impedance is
infinite for n odd (antiresonance) and zero for n even. When small
losses are present, the input impedance is large for n odd and small for
n even,

286 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Let us consider the lowest resonance (n = 1) in more detail. The
input conductance at resonance can be determined from the power
losses as
6, = 84, = 2W
Viol? QLVial?
The energy stored W is simply calculated as
rad
W=p |H|? dr = a |A|?Zo
_ awZo<, ) Ae
Thus Gin = OQrZ.)? ~ 420 (6-81)
where Z, is given by Eq. (6-74) and Q can be calculated in the usual
manner as!
_ 77 esc 6; + csc 02 -1
O= FR {1 + 0.824 1 Teot (0:/2) tan orpa (6-82)
This Q is maximum when 6; = 7 - 62 = 33.5°, in which case
= a
Q = 0.350 R
Note tig this is smaller than the Q’s of other cavities that we have considered bevause of the introduction of the biconical feed system. In the
special case 6. = 90°, we have the cone-fed hemispherical cavity of *Fig.
6-8b, for which,*
_™ 1+cse 6, |-? 7
Q= 4K [2 + 0.824 log cot oo | (6-83)
This Q is maximum when @: = 24.1°, in which case
= 2
Q = 0.276 a
This is a lower Q than that for the hemispherical cavity without the cone
[Eq. (6-78)}, because of the feed system. The input conductance [Eq.
(6-81)] is not minimum when Q is maximum, because Zo is also a function
of 6: and 6. For the biconical resonator (*Fig. 6-8c), the input conductance is minimum when the cone angles are 61 = 7 - 6; = 9.2°. For the*
cone-fed hemispherical cavity (*Fig. 6-8b), the minimum conductance is*
obtained when 6, = 7.5°.

## Section 6-7: Sources of Spherical Waves
 The sources of the lowest-order
spherical waves are current elements, treated in Sec. 2-9. For exam18. A. Schelkunoff, ‘Electromagnetic Waves,” pp. 288-290, D. Van Nostrand
Company, Inc., Princeton, N.J., 1943.

SPHERICAL WAVE FUNCTIONS 287
Zz Zz Zz
r
@
ml | Kl + fF
ON
Y Y a
> I
$ \| 1
x x x
(a) (0) (c)
Zz Zz Zz
i Il Il x ' 4
IL 1
Pas, Y es ¥ JA Y Y
% se ‘a lesz >|
(d) (e) pn
Fia. 6-9. Some sources of spherical waves.
ple, the electric-current element of *Fig. 6-9a radiates a field given by*
H=VxAwith
Zh. kil
= Se gcikr = BAF og A, in? Gi ho (kr) (6-84)
where ho‘) is the spherical Hankel function of Eq. (6-11). Alternatively,
the field can be represented by a radially directed A given by
= ikl 1) ein
A;.= te 1h ae e-*” cos 6
= HE (kr) P,(00s 0) (6-85)
The field of the current element is discussed in detail in Sec. 2-9. The
dual source is the magnetic-current element of *Fig. 6-9b. The field of*
this source is given by E = -V xX F where F, or F, is the same as A, or
A, with I replaced by K.

The fields of the dipole and higher-multipole sources, represented by
*Fig. 6-9c to f, can be obtained by the same method as used in Sec. 5-6.*
For example, for the dipole source of *Fig. 6-9c,*

=A) - S\_ 4p s
Ay= 48 (2,42-§)- At (mets)

288 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where A,! is the potential from a single current element [Eq. (6-84)].
As the separation s is made small,
OAS _ jkils 9 4 yy
Bae 8a ae Be
where r = +/z? + y?+ 2%. Also,
© hol (er) = Kio” (kr) e058 @ = -khy\® (kr) Ps (cos 0)
Hence for the dipole of *Fig. 6-9c*
k?Ils

A,= ig hi® (kr) Ps(cos 6) (6-86)
and H=Vvx A. Thus, the vector potential is a first-order spherical
wave function.

For the dipole source of *Fig. 6-9d, we have*

aA _ jkils 8 4 oy)
A, =o ase ae 3g (kr)
12
%\ = urs ho (kr) sin 6 cos c
\ Tv
which can be written as
2
A, = "2!8 4,00(kr)P11(cos 6) cos c (6-87)
Anj
This is a first-order wave function of n = 1, m = 1. Similarly, for the
dipole source of *Fig. 6-9e, we find*
2
A, = E218 50> (er)P,Me0s 6) sin (6-88)
4a]
Thus, all wave functions of order one can be interpreted as the A, of
dipole sources.

This procedure can be extended to higher-multipole sources in a
straightforward manner. For example, for the quadrupole source of
*Fig. 6-9f, we have*

A aA; aA,
2 8182 Oy a2 = 78 ay
where A,() is for the dipole of *Fig. 6-9c, given by Eq. (6-86). We also*

SPHERICAL WAVE FUNCTIONS 289
have

' ya Zz

2 [hy =2Z2) pw z
a [hi\ (kr) Pi(cos 6)] On [* (kr) :]
=- ue ho (kr) = -kh2(kr) sin 6 cos 6 sin
k
=3 h2(kr) P2'(cos 6) sin
Hence the vector potential of the quadrupole of *Fig. 6-9f is*
jk? Il. .
Ay = FETS 4 (kr)P2'(c0s 8) sin (6-89)
In this manner we can identify each wave function of order n with the
A, of a multipole source of 2n z-directed current elements.

## Section 6-8: Wave Transformations
 Now that we have wave functions in
three basic coordinate geometries available, the number of possible wave
transformations becomes very large. We shall here establish only a few
representative transformations involving spherical wave functions. A
convenient method of obtaining the desired results is that of Sec. 5-8.

Let us first consider the plane wave e* and express it in terms of spherical wave functions. This wave is finite at the origin and independent
of c; hence an expansion of the form

ef = eircond = ») anjn(7)Pn(cos 4)
n=0
must be possible (see *Fig. 6-1 for the coordinate orientation). To evaluate the a,, multiply each side by P,(cos 6) sin @ and integrate from 0 to*
mon 6. Because of orthogonality [Eq. (6-40)], all terms except g = n
vanish, and by Eq. (6-41) we have
7 . 2a,
Jr cos 8 P ) = nm a
[ e P,(cos @) sin 6 d' mm 1”)
The nth derivative of the left-hand side with respect to r evaluated at
r =0Ois
a [Ton . jn arent)?
j f cos" 6 P,(cos 6) sin 6d@ = Qn ¥ i)!
The nth derivative of the right-hand side evaluated at r = 0 is
Qn N)2
Qn FDQn FI
Hence, equating the preceding two expressions, we obtain
an = jr(2n + 1)

290 TIME-HARMONIC ELECTROMAGNETIC FIELDS
which, substituted back into our starting equation, gives
ot = ohent = Y Fn + Vialr)Pa(cos 8) (6-90)
n=0
Note that we have also established the identity
ja(r) = _ [ * circos ® P, (cos 6) sin 6 d8 (6-91)
0
Equation (6-90) is the desired transformation expressing a plane wave in
terms of spherical wave functions.

Transformations from cylindrical waves to spherical waves can be
obtained in a similar fashion. For example, consider the cylindrical wave
Jo(p), which is finite at r = 0, independent of $, and symmetrical about
6 = 7/2. Hence, there exists an expansion

Jo(o) = Jo(r sin 6) = PY bajan(r)Paa(cos 6)
n=0
As before, we multiply each side by P,(cos 6) sin @ and integrate from
Otorwon 6. The result is
~~ . Jo(r sin 0)P2n(cos 6) sin @d@ = -2bn (r)
Jo an +17™
S,
To determine the bz, we differentiate each side 2n times with respect to r
and set r = 0. ».This gives
b= (=1)"(4n + I(2n - 1)!
a 2?*-In Wn - 1)!
Hence the desired wave transformation is
_ . (-1)"(4n + 1)(2n - 1)! ..
Jo(o) = Jo(r sin 0) = by Seigler sa@)Pan(cos oy
n=0
(6-92)
Note also that the two equations preceding Eq. (6-92) establish an integral formula for j2,(r).

Now let us consider wave transformations corresponding to changes
from one spherical coordinate system to another. To illustrate, consider
the field of a point source at r’

o enile-F'
ho (lr - rl) = rr

SPHERICAL WAVE FUNCTIONS 291
Zz
source
x r-r
o Field
point
Fia. 6-10. Spherical coor- f r}
dinates of r and r’. |
e. \ |
= bs
\ Sek !
' a aa |
e >, | ~
x N
where r and r’ are defined in *Fig. 6-10. We desire to express this field in*
terms of wave functions referred tor = 0. The field has rotational symmetry about the r’ axis; so let us express the wave functions in terms of
the angle - where
cos £ = cos 6 cos 6’ + sin @sin 6’ cos (6 - c’) (6-93)
Allowable wave functions in the region r <r’ are jn(r)Pa(cos §), and
allowable wave functions r > r’ are ha®)(r)Pa(cos £). Furthermore, the
field is symmetric in r and r’; hence we construct
» Cnn (7’)jn(7)Pa(cos £) r<r
h(x - x) = 1 "2°
») €njn(r’ Ra (r) Pn (cos €) r>r
n=0
where the c, are constants. If we let the source recede to infinity, the
field in the vicinity of the origin is a plane wave. Using the asymptotic
formula
ete 7
ha®(z) = Te
we have for the left-hand side of the preceding equation
hot? ([r - rl’) aS git 008 0
a0
and for the right-hand side
jen :
ame ple CnJ"(r)P n(Cos 6)
0 St

292 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz
r
|
|
*Fig. 6-11. A plane wave*
|? incident on a conducting
sphere.
| Y
|
~ |
N
xX
i) Incident plane wave
A comparison of these two expressions with Eq. (6-90) shows that
Cn = 2n + 1; hence
Y at hat Gjal)Paleos ) or <a"
ho®(lr - r']) = 4 "5° (6-94)
y (2n + 1)j,(7)ha®(r)P2(cos &) r>fr
‘ 4
\ n=0
NS,
This is the addition theorem for spherical Hankel functions. Since
ha? = ha*, Eq. (6-94) is also valid for superscripts (2) replaced by
(1). The real part of Eq. (6-94) is an addition theorem for jo(|r - r’|),
and the imaginary part is an addition theorem for no(|r - r’|).

Finally, one can express the zonal harmonics P,(cos ) in terms of the
tesseral harmonics P,”(cos 6)h(mc). In other words, a wave function
referred to the - = 0 axis of *Fig. 6-10 can be expressed in terms of wave*
functions referred to the 6 = 0 axis. The identity is

- !

P, = oI (n= m)! pn sm G -c’) (6-95)

(cos £) » € (nm)! P,"(cos 0)Pn™(cos 6’) cos m(c - c’) (' )

m=1

where em is Neumann’s number (1 for m = 0 and 2 for m > 0). The
proof of Eq. (6-95), plus some other wave transformations that we have
not treated explicitly, can be found in Stratton’s book.1. Equation (6-95)
is an addition theorem for Legendre polynomials.

## Section 6-9: Scattering by Spheres
 Figure 6-11 represents a conducting
sphere illuminated by an incident plane wave. Take the incident wave

1J. A. Stratton, “Electromagnetic Theory,” pp. 406-414, McGraw-Hill Book Company, Inc., New York, 1941.

SPHERICAL WAVE FUNCTIONS 293
to be z-polarized and z-traveling, that is,
Ep = Ee-ik* = Egemikreond
H,} = Eo ins = Bo itr cos (6-96)
7 7
For convenience in applying boundary conditions, we express this incident
field as the sum of components TM and TE tor, that is, in terms of an
F, and an A,. From Eqs. (6-26) we see that A, can be obtained from
E,, and F, from H,. The r component of E is
iL ; is cos } a -ikr cos 8
E,i = cos csin 6 E, Eo Gk 30 (e7? )
Using Eq. (6-90), we can write this as
iL cos wn . oO
E,i = Eo fi yi (2n + 1)jn(kr) a5 P,,(cos 0)
n=0
Finally, using Eq. (6-23) and the relationship dP,,/d0 = P,', we obtain!
i= JE cos c i-n, 1 7)
E; (ker)? » pn(2n + 1)J,(kr) Pn (cos 8)
n=1
Noting the form of E,*, we construct the magnetic vector potential as
Eo
Afs= oy £98 c Hy and ,(ker)P'(cos 0) (6-97)
a
n=l
and evaluate E,' by Eqs. (6-26). Simplifying the result by Eq. (6-24),
we obtain
Bf = - 70008 8 NN a in(n + 1) aller) PaX(cos 8)
1 (kr)? n n
n=1
Comparing this expression with the preceding formula for E£,', we see that
_ Fn + 1) 7
a,= nin £1) (6-98)
A similar procedure using H,‘ and F,' gives
~_ Eo..
Fi= ; sin @ dnd (kr) Pn (cos 6) (6-99)
n=l
where the a, are again given by Eq. (6-98).
1 Note that the n = 0 term of the summation drops out because Po! = 0.

294 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Now that the incident field is expressed in terms of radially TE and
TM modes, the rest of the solution parallels the cylinder problem (Sec.
5-9). The scattered field will be generated by an A, and F, of the same
form as the incident field with J, replaced by f.°%. Hence, we construct scattered potentials as
Eo
As = ou o bat, (kr)P n'(cos 8)
"! (6-100)
Ey. .
Fy = = sin o Cnn (kr)Pa'(cos 6)
n=1
The total field is, of course, the sum of the incident and scattered fields.
Therefore E and H are given by Eqs. (6-26) where
Eo * 2
ee =, 0°83 o [a,Jn(kr) + bf (kr)|P,1(cos 8)
op
sai (6-101)
\ Peo Fo sin c > [anPa(kr) + cafs((kr)|Ps (cos 8)
N n=l
The boundary conditions are Ey = E, = 0 at r = a, which require that
Jka)
b, = -4a, = -A," (ka)
5 ay oe: 10)
= ” f, (ka)
This completes the solution. Note that the problem can be viewed as
a short-circuited radial transmission line (Sec. 6-4) with many modes
superimposed.
The surface current on the sphere can be found according to
J.=u,X Hatr=a. The result is
j . sin 6 P,“(cos @) jPxi(cos 6)
Sy = Fy 8 YS g, [BGP aM (cos 8) , _jPa\(cos 0)
Oka A. '(ka) sind A, (ka)
be (6-103)
Foe ip, sin 7 _ Pxa(cos 6) __ sin @ P,”’(cos 8)
eq ka "sin @ A,2” (ka) 7A, (ka)
n=l
where the a, are given by Eq. (6-98). The distant scattered field can be

SPHERICAL WAVE FUNCTIONS 295
found from the general expressions by using the asymptotic formula
A, (kr) - jr tenth
and retaining only the terms varying as 1/r._ The result is
pe - LE ite in ‘ v az Een |
Ec =e os Di [basin 0, (cos 0) - Cn Sin 8
nt (6-104)
» TEs ie ‘|, Pni(cos@) 1
Es kr ee sin yi [> ain c, sin @ P,!'(cos 6)
n=1
where the b, and c, are given by Eqs. (6-102). Of particular interest is
the back-scattered field
Ey = Be = Mel
O=0 b="
oa o=-x/2
From this we can calculate the echo area according to Eq. (3-30), which is
. Ey?
c= tim (407 Tp)
Making use of the relationships
P,,\(cos 6) (-1)"
sind or 2 n(n + 1)
sin 6 P,’(cos 6) awed i n(n + 1)
and the Wronskian of the spherical io
Bessel functions, we find lp
id 2
A= x (-1)*(2n + 1) ad |
°° Er) Ly (ka), (ka) 1 Lk,
ae
(6-105) % M
>
A plot of A./d? is shown in *Fig. 6-12. < Ai*
For small ka, the n = 1 term of Eq. 01 HY
(6-105) becomes dominant and
On?
“*' (ka) A. jut de (ka)& (6-106)
cae . . 0.01
which is a good approximation when 0 02 04 06 08 10 12
a/\ <0.1. Equation (6-106) is a/r
known as the Rayleigh scattering *Fig. 6-12. Echo area of a conducting*
law. It states that the echo area of sphere of radius a (optical approximasmall spheres varies as \~4 and was __ tion shown dashed).

296 TIME-HARMONIC ELECTROMAGNETIC FIELDS

first used to explain the blueness of the sky. For large spheres
Ae (6-107)

which is the physical optics solution. The region between the Rayleigh

and optical approximations is called the resonance region and is charac
terized by oscillations of the echo area.

Let us now look at the field scattered by the small conducting sphere.
Using small-argument formulas for the spherical Bessel functions, we find
from Eq. (6-102) and (6-98) that

_ntl 2"(n - 1)! ]? (ka)?nt?
bn ka-0 n on a [ ~~ (Qn) pet (6-108)

so the n =1 terms of Eqs. (6-104) become dominant for small ka.
Hence, at large distances from small spheres,

-jkr

Ey -> Ey ° (ka)? cos $ (cos 6 - ¥4)
ka-0 kr
ike (6-109)
E,' me Ey - (ka)* sin c (34 cos 8 - 1)
A comparison of this result with the radiation field of dipoles shows that
the scattered field is the field of an z-directed electric dipole
bats
I = Ey 2% (ka) (6-110)
x n
plus the field of a y-directed magnetic dipole
Qn

Kl= Fora (ka)* (6-111)
The ratio of the magnetic to electric dipole moments is |KI/J1| = 4/2.
Figure 6-13 illustrates the origin of these two dipole moments. A surface

Z Z
Je Je
7 ° °
(a) (6)

Fia. 6-13. Components of surface current giving rise to the dipole moments of a conducting sphere. (a) Electric moment; (b) magnetic moment.

SPHERICAL WAVE FUNCTIONS 297
current in the same direction on each side of the sphere gives rise to the
electric moment, while a circulating current gives rise to the magnetic
moment. In general, the scattered field of any small body can be
expressed in terms of an electric dipole and a magnetic dipole. For a
conducting body, the magnetic moment may vanish, but the electric
moment must always exist.

Now consider the case of a dielectric sphere, that is, let the region
r <a of *Fig. 6-11 be characterized by e2, wz, and the region r > a by*
€0, Ho. In addition to the field external to the sphere, specified by potentials of the form of Eqs. (6-101), there will be a field internal to the
sphere, specified by
__ Bo » ;
A, = - cos c dyJ n(kar)Pa'(cos 0)
OL
id (6-112)
__ By.. 2
P-= |, sino y end n(kar)P (cos 0)
° n=1
The superscripts - denote the region r < a, and superscripts + denote
the region r > a. Boundary conditions to be met at r = a are
Egt = Eo Hot = He
E,t = Es- H,* = Hethat is, tangential components of E and H must be continuous. Determining the field components by Eqs. (6-26), using Eqs. (6-101) for r > a
and Eqs. (6-112) for r < a, and imposing the above boundary conditions,
we find
bg = Matte Palo) I a(kaa) + V costa In (oa) I (haa)
(aS
Veto 1," (koa) SF a(kaa) - VW eona 1, (koa) J’, (kaa)
= Vato Falko) Fi (kaa) + Vectta Th (koa) J »(kea)
Cx = pee ee Ee en
V eato A,® (koa) J 3, (kaa) - V cotta A," (koa) J a(ka@) (6-113)
a= -j Veao a,
Veato A, (koa) Fn (kaa) - V cota Ba ® (Keo) I’, (kaa)
ty = ee ee on
Veaito Hy (koa) S' (kaa) - Veana Hy (ieoa)d (aa)
where a, is given by Eq. (6-98). The conducting sphere can be obtained
as the specialization yz- 0, eg > ~, such that kg remains finite. Note
that, in contrast to static-field problems, ez-> © is not sufficient to
specialize to a conductor.
In the special case of a small dielectric sphere, the n = 1 coefficients

298 TIME-HARMONIC ELECTROMAGNETIC FIELDS
are dominant and reduce to
-1
= 3 &
bi Fah ~ (hoa)? 5
-1
1 -> - (Koa)?
koa 0 3 Mr + 2 (6-114)
4 Fb Ge Fe)
9
°* goad Bjes(2 Fp)
where c = €2/€9 and uy = wa/uo. A calculation of the scattered field
reveals that it is the field of the two dipoles
_ Anj 3@-1
l= u:Bo Re (ka) aro
Ani 1 (6-115)
=uk, Ls ed
Kl = u,Eo a (ka) a)
Note that the magnetic dipole vanishes if the dielectric is nonmagnetic,
that is, if », = 1. Similarly, a magnetic material with e, = 1 would
scatter no electric dipole field. The field internal to the sphere is uniform in both E and H for the small sphere. In fact, the specialization
represented by Eqs. (6-114) is the “quasi-static” solution. It can be
obtained by taking the d-c electric and magnetic polarizations and
assuming that they vibrate in phase quadrature with the incident field.

## Section 6-10: Dipole and Conducting Sphere
 Figure 6-14a shows a radially
directed electric dipole near a conducting sphere. Figure 6-14b shows a
problem reciprocal to that of *Fig. 6-14a in the following sense. The*
component of E® in the direction of Jl’ equals the component of E® in
Zz Zz
y. mm
Il XC
8 6.
y ZL
@
7
(a) ue ®)
*Fig. 6-14. The conducting sphere and a radially directed dipole. (a) Original problem; (b) reciprocal problem,*

SPHERICAL WAVE FUNCTIONS 299
the direction of Jie. (Superscripts refer to *Fig. 6-14a and b.) If the*
Il of *Fig. 6-14b recedes to infinity, we have the plane-wave scatter problem treated in the preceding section. Hence, the radiation field of Fig.*
6-14a can be simply obtained from the results of Sec. 6-9.

In particular, in the vicinity of the conducting sphere we have
(E,*)* -> -dopll em ikteikr! cos
ras dar
which is a plane wave. Letting
= Toul its
Ey es (6-116)
we have the wave of Eq. (6-96). Hence, the field of *Fig. 6-14b is specified by Eqs. (6-101) with coordinates primed. To relate this solution to*
that of Vig. 6-14a, we need the r’ component of E, which is
1 e
ye = - ( -_ 1-2 >
Be = (an +k ) Ay
= Fos c" > n(n + fant a(kb) + ball, (kb)]P.'(cos 6’)
3 n=l
Finally, by reciprocity, E,’ evaluated at r’ =b, & =7- 6, c’ =0
equals - Ey* at r, 0, c Hence,
Ey = ie y n(n + MlanSa(kb) + baffn (kb)|(-1)"P.'(cos 6) (6-117)
n=1
where ay, bn, and Eo are given by Eqs. (6-98), (6-102), and (6-116),
respectively. In the special case b = a, that is, when the current element is on the surface of the sphere, Eq. (6-117) reduces to
_ all ig, HAR +D py 6-118
Ey = gil ev? y A.™(ka) P,,'(cos 6) ( )
n=l
This is the radiation field of a radially directed electric dipole on the
surface of a conducting sphere. Figure 6-15 shows the radiation patterns
for spheres of radii a = 4/4 anda = 2X. The pattern for the very small
sphere is the usual dipole pattern. For a very large sphere it approaches
the pattern of a dipole on a ground plane but always with some diffraction around the sphere. The radiation field for dipoles of other orientations, and also for magnetic dipoles, can be obtained in a similar manner.
The field in the entire regionr > b can be determined from the radiation

|
300 TIME-HARMONIC ELECTROMAGNETIC FIELDS
pre
SSE
SEES
SSS
lI RES Senna, EEX
LRN
CSW TITS SS
(apse: (otter
NMBBRyeS- ae 2ceCeumell
RO CAINR RA Ly
SMS SEO
SRL?
sen n eee
. GEES
ey Late ts
*Fig. 6-15. Radiation patterns for the radially directed dipole on a conducting sphere*
ofradiusa.
field as follows. Fromsymmetry considerations (*Fig. 6-14a) we conclude*
that H = u,H4, and therefore the field can be expressed in terms of an
A=u,A,. Also, A, must be independent of c and represent outward
traveling waves; hence
A, = ) a,ff,,(kr)P,, (cos 6) r>b (6-119)
From this we can calculate Ee by Eqs. (6-26), obtaining
Ey = ue y nj", (r)P, (cos 6)
= =), anj"Px! (cos 6) (6-120)
The a, are then evaluated by equating this expression to the radiation

SPHERICAL WAVE FUNCTIONS 301

field previously determined. For ex- Z
ample, in the special case b = a we r
equate Eq. (6-120) to Eq. (6-118) and
obtain &

a, = Lin + 1) (6-121) La %

4nkff ©" (ka) \

The field everywhere can now be ob- BPS
tained from Eqs. (6-26), (6-119), and wa
(6-121). Z-~

## Section 6-11: Apertures in Spheres
 In x
Sec. 4-9 we saw how to express the
field in a matched rectangular waveguide in terms of the field over a
cross section of the guide. In Sec. *Fig. 6-16. Slotted conducting sphere.*
6-4 wesaw thatspace could be viewed
as a spherical waveguide. A given sphere r = ais a cross section of the
spherical guide. If r > a contains only free space, then the guide is
matched, that is, there are no incoming waves. By writing the general
expansion for outward-traveling waves and specializing to r = a, we
obtain the field r > a. When apertures exists in a conducting sphere
of radius r = a, the tangential components of E are zero except in the
apertures. Ourformulas for the field r > a then reduce to ones involving
only the tangential components of E over the apertures.

A general treatment of the problem is messy; so let us restrict consideration to the rotationally symmetric TM case, that is, one having
only an Hs. The slotted conducting sphere of *Fig. 6-16 gives rise to*
such a field if there exists only an Ey independent of cintheslot. The
field is expressible in terms of an A, of the form

A, = JY. anfl,®(kr)Pq(cos 0) (6-122)
n=1
From Eqs. (6-26) we calculate
Ey = Y ant," (er) & P,(c0s 6) (6-123)
jue mS 00
n=l
Noting dP,/d0 = P,', we multiply each side of the above equation by
P,\(cos 6) sin @ and integrate from 0 to 7 on 6. By the orthogonality
relationship [Eqs. (6-46) and (6-47)], we obtain
bd . 2rn(n + 1)
1 =7 ay aint
i: EoP,,\(cos @) sin 6 d' jr anf" (kr) on +1

302 TIME-HARMONIC ELECTROMAGNETIC FIELDS
b-e
1\ | 77
SERS
COSHIEERRYD
SHEER
CP ef SHALES
LT HLA XS ARS
APSE SO
LTTE SSS an
PORES Tee at TV
SIRT
OS KTR op
SASS RAAT
SOKA ESAS?
SIRES OS
SAI ADS
\ CATT AS
Fra. 6-17. Radiation patterns for the slotted sphere, 00 = 7/2.
Specializing this to r = a, we have the coefficients a, determined as
a, = an as ie Eg |. P,\(cos 6) sin@d@ (6-124)
The field simplifies to some extent in the radiation zone. Using the
asymptotic forms for 7, in Eq. (6-123), we obtain
E6 me 2 ewtkr ) anj"P ‘(cos 8) (6-125)
This result could also be obtained from the plane-wave scatter result of
Sec. 6-9, using reciprocity.
For the slotted sphere of *Fig. 6-16, let us assume a small slot width,*
so that Ee is essentially an impulse function at r = a. Hence, we assume
By |. = ¥ 5 - 60) (6-126)

SPHERICAL WAVE FUNCTIONS 303
where V is the voltage across the slot. Then Eq. (6-124) reduces to
jV(2n + 1)P,}(cos 60) sin 0
On aan(n + 1)A,"(ka)
and the radiation field [Eq. (6-125)] becomes
V7 o-ikr in
E, = we* sin 09 ye + 1)P.'(cos 60) P,\(cos @) (6-127)
7 n(n + 1)! (ka)
n=1

Figure 6-17 shows radiation patterns for the case 6) = 7/2, that is, when
the conductor is divided into hemispheres. Patterns for spheres of radii
d/4 and 2 are shown. Very small spheres produce a dipole pattern,
while very large spheres produce an almost omnidirectional pattern with
severe interference phenomena in the @ = 0 and 6 = = directions. In
the limit 6. 0 we obtain the patterns of *Fig. 6-15, which is to be*
expected in view of the equivalence of a small magnetic current loop and
an electric current element.

The general problem of finding the field in terms of arbitrary tangential
components of E over a sphere is treated in the literature.’

## Section 6-12: Fields External to Cones

The general treatment of the prob- Zz

lem of sources external to a conduct
ing cone is also messy but can be

found in the literature! We shall

here restrict consideration to the

rotationally symmetric case of ‘‘ring
source” excitation of a conducting 7
cone. The geometry of the problem Bean 2 Zl es

is shown in *Fig. 6-18. The special Kei / ee*

case of a magnetic current ring on A,

the conical surface gives the field of x

a slotted cone. The limit as the

magnetic current ring approaches the

cone tip gives the field of an axially

directed electric current element on F16- 6-18. Ring excitation of a conductthe tip. ing cone.

Consider first the case of an electric current ring. From symmetry
considerations, it is evident that E will have only a c component; so the
field is TE to r. The modes of the “conical waveguide” are considered
in Sec. 6-5, Eqs. (6-61) to (6-64). In the region r < a we have standing
waves, while in the region r >a we have outward-traveling waves.

1L. Bailin and §. Silver, Exterior Electromagnetic Boundary Value Problems
for Spheres and Cones, JRE Trans., vol. AP-4, no. 1, pp. 5-15, January, 1956.

304 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Hence, we construct
> a,P,(cos 6)A, (kr) r>a
F,=(2 (6-128)
») b.P.(cos 6)J (kr) r<a
where the v are ordered solutions to
d
[ #P-tcos ol... =0 (6-129)
Continuity of E, at r = a requires that’
a, ff, (ka) = bed (ka) (6-130)
Finally, He at r = a must be discontinuous by an amount equal to the
surface-current density (in our case it is an impulse function). Thus,
k t) > .
= o£ @y -b,J!
Js Joma >. 39 Pe(cos 6)[a, ff," (ka) - bJ!(ka)]
which, using Eq. (6-130) and the Wronskian of the spherical Bessel functions, becomes
\, n=) dp. 0) =e 6-131
\ + 5a 36 (cos#) T.lka) ( )
By the methods of Sec. 6-3 the following orthogonality relationship can
be derived:
ala a P _ fo w ov
i (3 P.) (3 Ps) sin 6d@ = | Ny wad (6-132)
- vu +1)f . eP,
where N,= WT [sn OP, a lhe (6-133)
Hence, multiplying each side of Eq. (6-131) by P,(cos @) sin 6 and integrating from 0 to 6; on 6, we obtain
_ 7a Le a . _
a = J ,(ka) i Js ay; [P.(cos 6)] sin 6 do (6-134)
This completes the solution for an arbitrary c-directed current sheet at
7 =a. For the current filament,
Je = £50 - 02) (6-135)
and Eq. (6-134) reduces to
_ als : a
a =H J <ka) sin 02 ah P,(cos 62) (6-136)

SPHERICAL WAVE FUNCTIONS 305
Numerical calculations are difficult because of the problem of obtaining
the eigenvalues v and the eigenfunctions P,.

When the ring source of *Fig. 6-18 is a magnetic current, the problem is*
dual to the electric-current case, except for boundary conditions. Hence,
we construct

J eaPa(cos )AM(kr) > a
A= i (6-137)
t Y, dP u(cos )Fu (kr) r<a
where the w are ordered solutions to
P.(cos 6:) = 0 (6-138)
in contrast to the v which were solutions to Eq. (6-129). Continuity of
Hy, at r = @ requires that
cul (ka) = dud u(ka) (6-139)
At r = a we have E» discontinuous by an amount equal to the surfacecurrent density. Thus, analogous to Eq. (6-131), we have
=~ 252 ou 6-14
Ms ji > 50 P.(cos @) F.ka) ( 0)
The orthogonality relationship for the eigenvalues defined by Eq. (6-138)
is
fa a £ 0 wre
ap \(2 : = 1
f (5,7) (j5P«) snees es wau (6-141)
u(u + 1)[.- OP, 0Pu
= dS oh 1

where MM. ou kT [sin 0 3G ou los, (6-142)

Multiplying each side of Eq. (6-140) by P.(cos 8) sin 8 and integrating

from 0 to 6; on @, we obtain

~ =% zyna) [ay (Palcos 0} sin edo (6-143)
ou = OM. * , Moa '»(COS

This completes the solution for an arbitrary c-directed magnetic current

sheet atr =a. For the magnetic current filament,

M, = © (0 - 6») (6-144)
and Eq. (6-143) reduces to
oe = TE tule) sin 62 2 Pu (cos &2) (6-145)
« oM,* 00.”

306 TIME-HARMONIC ELECTROMAGNETIC FIELDS
@
el By,
SEER
SEES
SER
LESSER.
SER TT ee
HERES \
PSEC es «|
NOS ASSIA]
LECCE LH]
“ SLIT MPSS Vy
SRP?
CHETAN SX)
OTE ES
\ Eaaninse
*Fig. 6-19. radiation patterns for the slotted conducting cone. (After Bailin and*
Silver.)
Again a ire of the eigenvalues u and the eigenfunctions P, is
difficult.

"li we now let 6. = 6, and set K = V in the magnetic current solution,
we have the case of a cone slotted at r = a with a voltage V across the
slot. For r > a Eq. (6-137) becomes

A, = 2 sin? 6; > ir P’, (cos 6:)Pu(cos 6)Ju(ka) A. (kr)
Using the asymptotic for #H,® and evaluating E, by Eq. (6-26),
we find for the radiation fie’
Some radiation patterns for slotted cones with cone angle 30° are shown
in *Fig. 6-19. A discussion of the problem of plane-wave scattering by a*
cone is given by Mentzer.!
> 1. x Mentzer, Scattering and Diffraction of Radio Waves,” pp. 81-93, Pergamon

SPHERICAL WAVE FUNCTIONS 307

## Section 6-13: Maximum Antenna Gain
 The general form of the field in a
spherical space external to all sources is Eqs. (6-26) with

A,= ») Omnll (kr)Px™(cos 8) cos (md + amn)
ne (6-147)
F, = ») brnfl x‘ (kr)Px™(cos 6) cos (md + Bmn)
mn
Given an arbitrary field at r = rj, the field can be projected backward
toward the origin as far as desired. Atsomespherer = a we can determine sources by the equivalence principle (Sec. 3-5), which will support
this field. Hence, it appears that sources on an arbitrarily small sphere
can support any desired radiation field.

The gain of an antenna is defined by Eq. (2-130) in general. We shall

here consider the largest gain
2
g = 22S)ans (6-148)
O;

where (S,)max is the maximum power density in the radiation zone and
@, is the power radiated. By the discussion of the preceding paragraph,
it appears that arbitrarily high gain can be obtained, regardless of antenna
size. In practice, however, the gain of a directive antenna is found to be
related to its size. A uniformly illuminated aperture! type of antenna is
found to give the highest practical gain. This apparent discrepancy
between theory and practice can be resolved if the concepts of cutoff
and Q of spherical waves are properly applied.

Let us orient our spherical coordinate system so that maximum radiation is in the @ = 0 direction. The radially directed power flux in this
direction is then

(S:)mex = E,H¥ - E,H* (6-149)
From Eqs. (6-147) and (6-26) we find
evikr - .
Ez = > n(n + 1)j"(q Gin COS ain - Bin SiN Bin)
2Qyr
ec ake . .
E,= Or n(n + 1)j"(-9 ain SiN ain - bin COS Bin)
ie: (6-150)
ewakr . . 1
Hz = Dr y n(n + 1)j* (a. sin ain - 5 bin cos bx)
enikr . 1 .
H, = Or n(n + 1)9" { Gin COS Qin + 7 bin SiN Bin

1 The term “uniformly illuminated aperture” is used to describe antennas for which
the source (primary or secondary) is constant in amplitude and phase over a given area
on a plane, and zero elsewhere.

308 TIME-HARMONIC ELECTROMAGNETIC FIELDS
in the 6 = 0 direction of the radiation zone. The total radiated power is
found by integrating the Poynting vector over a large sphere. The
result is
_ nin + Ia + mle oi ln py
= 4e y LEE LM (alanal? + * fbn?) (6-151)
mn
where c«, = 1form =0 and e, = 2form > 0. We used the orthogonality relationships of Eqs. (6-51) in the derivation of Eq. (6-151).
Equations (6-148) to (6-151) give a general formula for gain in terms
of spherical waves. We shall now consider under what conditions g is a
maximum. Note that the numerator of Eq. (6-148) involves only the
a, and by, coefficients. Hence, the denominator can be decreased without changing the numerator, by setting
Ann = Onn = 0 m1 (6-152)
Also, both numerator and denominator of g are independent of a, and
Bin; So they may be chosen for convenience without loss of generality.
In particular, let a}, = rand Bin = 7/2, and the gain formula reduces to
2
‘, | by (An + B,) |
‘s g= - (6-153)
--- 2 2
. 2 sate (4a + bi
where A, = jyn(n + Iain B, = jn(n + 1)dia (6-154)
The denominator of Eq. (6-153) is independent of the phases of A, and
B,; so we can maximize the numerator by choosing A, and B, real.
Furthermore, gis symmetric in A, and B,; hence the maximum exists when
A, = B, = real (6-155)
The maximum gain therefore will be found among those specified by
2
(4)
9= aS FF (6-156)
as( bh
™\2n +1
where A, is real. As long as 7 is unrestricted, this g is unbounded, as we
anticipated earlier.
If the field, specified by Eqs. (6-147), contains only wave functions of
order n < N, then an upper limit to g exists. Setting ag/9A; = 0 for

SPHERICAL WAVE FUNCTIONS 309
all Aj, we find
N
Gat= ») (Qn +1) = N?42N (6-157)
n=1
and also A, = mt Ai (6-158)
Equation (6-157) represents the highest possible gain using spherical
waveguide modes of order n < N. A similar limitation to the nearzone gain also exists.!

To relate gain to antenna size, we define the radius a of an antenna as
the radius of the smallest sphere that can contain the antenna. We saw
in Sec. 6-4 that spherical modes of order n were rapidly cut off when
ka <n. Hence, it is reasonable to assume that modes of order n > ka
are not normally present to any significant extent in the field of an
antenna of radius a. We define the normal gain of an antenna of radius
aas

Joormat = (ka)? + 2ka (6-159)
which is obtained by setting N = ka in Eq. (6-157). Hence, the normal
gain is maximum gain obtainable when only uncutoff modes are present.
It is interesting to note that, for large ka, a circular, uniformly illuminated aperture of radius a has the same gain as the above-defined normal
gain.? It is therefore not surprising that the uniformly illuminated
aperture gives the highest antenna gain in practice. i

The normal gain is not an absolute upper limit to the gain of an |
antenna. Antennas having higher gain are a distinct possibility and
will be called swpergain aniennas. We shall use the Q concept of Sec. 6-4
to show that (1) supergain antennas must necessarily be narrow-band
devices, and (2) supergain techniques yield only a small increase in gain
over normal gain for large antennas. Other characteristics which we
shall not demonstrate here are (3) supergain antennas have high field
intensities at the antenna structure and (4) they tend to have excessive
power loss in the antenna structure.

The Q of a loss-free antenna is defined as

mee W.> Wn

Q= a (6-160)
2eWn >
Oy = 5

1R. F. Harrington, Effect of Antenna Size on Gain, Bandwidth, and Efficiency,
J. Research NBS, vol. 64D, no. 1, pp. 1-12, January, 1960.

2S. Ramoand J. R. Whinnery, “ Fields and Wavesin Modern Radio,” 2d ed., p. 533,
John Wiley & Sons, Inc., New York, 1953.

310 TIME-HARMONIC ELECTROMAGNETIC FIELDS

l WU

rete

10° *Fig. 6-20. Quality factors*
e for ideal loss-free anten
nas adjusted for maxi10? mum gain using modes of
The | \ \ mens
; BATNIN
1
0 5 10 15 20 25
ka
where W, and W,, are the time-average electric and magnetic energies
and @, is the power radiated. We shall define an ideal loss-free antenna
of radius a as one having no energy storage r <a. The Q of this ideal
antenrtg must be less than or equal to the Q of any other loss-free antenna
of radiusa having the same field r > a, since fields r < a can only add to
energy storage. If the Q of an antenna is large, it can be interpreted as
the reciprocal of the fractional bandwidth of the input impedance. If
the Q is small, the antenna has broadband potentialities.

Antennas adjusted for maximum gain according to Eq. (5-158) have
equal excitation of TM and TE modes. The Q, of spherical modes,
defined by Eq. (6-60) and plotted in *Fig. 6-6, involve W, for TM modes*
and W,, for TE modes. We need Q’s defined in terms of the same energy
for all modes, and it is convenient to deal with Q’s for equal TM and
TE modes. The Q for equal TM, and TE, modes is

Q,™HE = 14Q, ka < N (6-161)
because the W, is essentially that of the TM, mode alone and the @; is
twice that of the TM, mode alone. When Q, < 1, we take it as unity.

Because of the orthogonality of energy and power in the spherical
modes, the total energy and power in any field is the sum of the modal
energies and powers. Hence, the Q of our ideal loss-free antenna is

1
TM+TE 2 1
2
ye 2), 42 (51)

SPHERICAL WAVE FUNCTIONS 311
where P, is the transmitted power in the TM, and TE, modes. Using
Eq. (6-158), this becomes

N
DY Gn + 1)Q,(ka)
Q= TaN (6-162)
where the Q, are given in *Fig. 6-6. Curves of antenna Q for several N*
are shown in *Fig. 6-20. Note that the Q rises sharply for ka < N, showing that supergain antennas must necessarily be high Q, or frequency*
itive.
~The of *Fig. 6-20 is a lower bound to the Q of any loss-free antenna*
of radius a. By picking a Q, we can calculate an upper bound to the
gain of an antennaofradiusa. Figure 6-21 shows the ratio of this upper
bound to the normal gain. Note that for large ka the increase in gain
over normal gain possible by supergain techniques is small. For small
ka supergain can give considerable improvement over normal gain. In
fact, as ka - 0 the supergain condition is unavoidable. All very small
antennas are supergain antennas by our definition. The problems of
narrow bandwidth and high losses associated with small antennas are
well-known in practical antenna work.
10
Vt} Pt tT PT ET PTET TT TY
9
eet | Tit ttt tty Pty yt tt
e7IN TTT TET TTT Ty yt
eet TTT ETT TT Py et
PN TT TT tT TT PPT ET
3 IN
T.ASSee TTT TT Te
@ 3 HS (ee ia a
2 2 Ree R ee TTT TT |
ik Pe ie EAE Pee Es
Oo 10 20 30 40 50 60 70 80 90
ka
*Fig. 6-21. Maximum possible increase in gain over normal gain for a given Q.*

312 TIME-HARMONIC ELECTROMAGNETIC FIELDS
PROBLEMS

## Section 6-1: Use Eqs
 (3-85) and the wave potential of Eq. (6-14) to show that a general
expression for fields TM to z is
. 1 a [cos@ @ 1 a .
E, = -jouy cos 6 + iar [= rod (ry) - sind 30 (y sin? |]
_: . 1 afcos@a_, 1 @ .
Eo = jouy sin @ + joa 30 [es x (ry) - rain 9 99 sin? 0 |
_ 1 9 fcos@ 9 |, uo .
Es = ior sn 0 al 7? or ) - Sing ag (Sin? »|
_ lay
H=7 36
_ cot 6 ay
Ho = > OG
-l . a a
He = =e [sin os (ry) + 96 cos |
where y is a solution to the scalar Helmholtz equation.

## Section 6-2: Verify that Eqs
 (6-17) and (6-18) are identical.

## Section 6-3: Consider an air-filled spherical resonator of radius 5 centimeters bounded by
copper walls
 Determine the first ten resonant frequencies and the Q of the dominant
mode.

## Section 6-4: For the spherical cavity of Fig
 6-2, show that the Q due to conductor losses is,
for TM Yyodes,

* me 1 fy nm +1)
(QO = 35 [ Mog
where the Uns are given in Table 6-2, and, for TE modes,
TE _ Tsp
(Qd mms = oR
where the un, are given in Table 6-1.

## Section 6-5: Consider the cavity lying between concentric conducting spheres r = a and
r =b, withb >a
 Show that the characteristic equation for modes TM to r is
Filkb) _ Nike)
Tika) Ni(ka)
and for modes TE to r it is
Fn(kb) _ Nn(kd)
Fn(ka) - -N.(ka)

## Section 6-6: In the concentric-sphere cavity of Prob
 6-5 let a <b, and show that the
resonant frequency w is related to the empty cavity resonant frequency wo by
- Ny(2.744) (a\*
eH 40 xo 744)? eee a
@o ‘SY (2.744) \b
where wo = 2.744/b ~/en. [Hint: Express the characteristic equation in the form
S(k,a) = 0, and expand in a Taylor series about ky = wo ~/ep.]

SPHERICAL WAVE FUNCTIONS 313

## Section 6-7: Consider the partially filled spherical cavity formed by a conductor covering
r =b and containing a dielectric «1, 41 for r < a and a dielectric e, », fora <r <b

Show that the characteristic equation for the dominant mode is

Ni (ead) Fi(k2a) - Si (ad) 8 (ea) _ om Fiera)
By (kab)F (kaa) - Fy(kab)N i(kza) 92 Sa(kxa)
where ky = V/eyu; and ky = w Venus.

## Section 6-8: In the partially filled spherical cavity of Prob
 6-7, let a «bd and e, = €) and
#2 =o. By expanding the characteristic equation in a Taylor series about the
empty-cavity resonant frequency wo, show that the resonant frequency w is given by

o
OS OO we 34 (2.744)? Ni@.744) «-1/(a\
0 Jy (2.744) & +2\0
where c, = e:/eo and wo = 2.744/b >/eouo. Compare this with the answer to Prob.
6-6.

## Section 6-9: Consider the function
1 0<8<5
S(8,c) = x

0 5<6<n
and determine the coefficients am, and bm, for the two-dimensional Fourier-Legendre
series of the form of Eq
 (6-48).

## Section 6-10: Let A and B be two vectors and 6 be the angle between them
 Define

c =A - Band show that, for B > A,
1 1 1 > (3)
a rr =) P.(cos @
C VAT+ B= 24Beos@ BL \B (cos 8)
n=

## Section 6-11: Consider the characteristic impedances of the spherical modes of space [Eqs

(6-57)]. Show that
-1
kro
Zy:™ = Z_,™* | n
02" ker
and ZTE = y2/Z™, Show also that the change from primarily resistive to primarily
reactive wave impedances occurs at kr = n.

## Section 6-12: Show that the field of an electric current element JI is the dominant TM
spherical mode of space, and the field of a magnetic-current element KI is the dominant TE mode

## Section 6-13: Using the usual perturbational method, show that the attenuation constant
due to conductor losses for the TEM mode of the biconical or coaxial radial guide
(Fig
 6-7c and d) is given by

a = Hi ose 81 + ese 62
2nr log cot 6/2
cot 62/2

## Section 6-14: Show that the dominant spherical TE mode of the wedge guide (Fig
 6-7e)

is the free-space field of a z-directed magnetic-current element.

314 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 6-15: Use the qualitative behavior of the spherical Hankel functions to justify the
statement that the spherical-horn guide of Fig
 6-7f has a “cutoff radius” approximately equal to that radius for which the cross section is the same as a rectangular
guide at cutoff.

## Section 6-16: Consider a hemispherical cavity (Fig
 6-8a) constructed of copper with
a = 10 centimeters, and air-filled. Determine the first ten resonant frequencies and
the Q of the dominant mode.

## Section 6-17: Consider the second resonance [n = 2 in Eq
 (6-80)] of the biconical cavity of
*Fig. 6-8c. Calculate the Q of the mode and the input resistance seen at the cone tips.*

## Section 6-18: Consider the conical cavity of Fig
 6-8d. Show that modes TM tor are given
by H =V Xu,A, where
(Ay) mep = Ps*(cos 8) cos mo Jy (w:, :)
a
where w,,, is the pth zero of J\(w) and v is a solution to Eq. (6-62). Similarly, show
that modes TE to 7 are given by E = -V X u,F, where
(Fe)mep = Po™(cos 8) cos mo J, (w»2)
where w,, is the pth zero of CD) and v is a solution to Eq. (6-64). For a complete
set of modes the sin m@ variation must also be included.

## Section 6-19: Let the current elements of Fig
 6-9c be replaced by magnetic-current elements Kl. Show that, in the limit s - 0, the field is given by E = -V Xu,F, where
Klis
= SF ay
\ F, inj hi (kr)Pi(cos 6)
‘
SZ
\ 6-20. Consider the quadrupole source of
*Fig. 6-22 where each element is an elecMy tric current Zl. Show that, in the limit*
¥ Sl 8: 0 and s:- 0, the field is given by
LVt 7 HAY Xwd, where
Y 1 KT I3,82
A i A: = “Odaj [ho (kr)P2(cos 0) - 3cho(kr)]
x F 7
*Fig. 6-22. A quadrupole source.*

## Section 6-21: Derive the following wave transformation:
[ 1 ~
eer 1 f(r’) Bn? !
Foam gerd, On + DE arco Yr >
n=0
where ~ is the angle between r and r’

## Section 6-22: Derive the following wave transformation:
Salo) =) Aniamen(?)Pamen%(c0s 6)
m=0
- (-1)™**(4m + 2n + 1)(2m)!
where An = “2m Fn) im!

SPHERICAL WAVE FUNCTIONS 315

6-23
 Derive the following formula:

1 Qjo(r’ )ho?(r) r>r’
ho? (jr - r’}) d =
L (jr - r'|) d(cos £) | Qjolr)ho'?(r") v>r
where c is the angle between r and r’.

## Section 6-24: Consider the scattering of a plane-polarized wave by a small conducting
sphere (Fig
 6-11). Show that the distant scattered field is plane polarized in the
direction 6 = 60°.

## Section 6-25: Consider an z-polarized, z traveling plane wave incident on a conducting
sphere encased in a concentric dielectric ¥
coating, as shown in Fig
 6-23. Show z
that the field is given by Eqs. (6-26),
where for r > b the A, and F, are given ~0 }
by Eqs. (6-101), and fora <r <b

z fuel wy
A, =~” cos @ bY dn W (kad a (Kr) y |
- By
n=
- Fi(ka)Rn(kr)|Pa'(cos 8) | 7
F, = sin c enlNn (ka) (kr)
ne x \]
- F,(ka)N (kr)|P.'(cos 6)
i A locident
Impose boundary conditions on the tan- wave
gential components of Eat Hatr =, Fyg. 6-23. A plane wave incident on a
and obtain expressions for bn, Cn, dr, ANd - eoated conducting sphere.
e, in terms of an, given by Eq. (6-98).

## Section 6-26: Consider a radially directed magnetic dipole KI adjacent to a conducting
sphere (Fig
 6-14 with J! replaced by Ki). Show that the radiation field is given by
Es = -nHoand

Kl. ¥ . .
Ho = 7 eit n(n + fant .(kb) + enff x (kb)}(-1)"P a} (cos 8)
4Aankr 4,
n=
where a, is given by Eq. (6-98) and cn by Eq. (6-102).

## Section 6-27: Consider a radially directed electric dipole adjacent to a dielectric sphere
(Fig
 6-14 with the sphere now dielectric). Show that the radiation field is then
given by Eq. (6-117) if b, is given by Eq. (6-113) instead of Eq. (6-102).

## Section 6-28: Consider a loop of uniform current J of radius a, as shown in Fig
 2-26.
Show that the radiation field is given by

Ti 2n+1 .
Bg = Bein Y tT pase zt
e re evi , inte pi ‘A wP1(0)P,1(cos @)
n=
where An = Sa(ka)
and nHs = -Ey.

316 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 6-29: Figure 6-24 shows a conducting sphere of radius R concentric with a loop of
uniform current / of radius a
 Show that the radiation field is of the same form as
given in Prob. 6-28 except that
IMER)N (ka) - 0, (kR)S (ka)
Aan! = An (ka) - = 21 (ke
(ko) - 7 OER)N, (ka) - Walk R)S,(ka) 2”
Show that this reduces to the answer for Prob. 6-28 as R - 0.
Z
Zz
: r
6 r
|
Ar) 4
NSHP”
See |
\ |
$-" |
x \y
*Fig. 6-24. A conducting sphere with a Fig. 6-25. Current element at the tip of a*
concentric ring of electric current. conducting cone.
~.

## Section 6-30: Fiduye 6-25 shows a current element // at the tip of a conducting cone

Show that the'radiation field is given by
. Eo = f(r) sin 0 P.,(cos 6)
N
where u is the first root of P,(cos 6:) = 0. Some approximate eigenvalues are
r- fh | ie | 10° | 24° | 37° | 49° | 60° | 69° | 77° | 84° | g0°
u O1 0.2 | 03 104 | 0.5 |] 06 | 0.7 0.8 | 0.9 1.0

## Section 6-31: By considering the equivalent circuit of Fig
 6-5 and the definition of Eq.
(6-60) for Q, show that the Q of the n = 1 spherical mode is
1 1
a= at Une
If equal TE and TM waves are present, the total Q is approximately one-half this
value. A small antenna (say ka < 1) will have minimum Q if only the n = 1 modes
are present inits field. Hence, the minimum possible Q for a small loss-free antenna is
1fpl 1
Qin = 3 la + |
where a is the radius of the smallest sphere that can contain the antenna.



---

## Chapter 7: Perturbational and Variational Techniques

PERTURBATIONAL AND VARIATIONAL TECHNIQUES

## Section 7-1: Introduction
 The differential equation approach of the preceding three chapters leads to an exact solution of the mathematical problem.
However, many problems cannot be treated by this method. We sawin
Sec. 3-11 that electromagnetic field problems can be expressed in integral
equation form. This formis particularly useful for (1) obtaining approximate solutions and (2) for general expositions of theory. In this chapter,
we shall consider two techniques useful for integral equations arising in
electromagnetic theory.

Perturbational Methods. The word “‘perturb” means to disturb or to
change slightly. The perturbational methods are useful for calculating
changes in some quantity due to small changes in the problem. Usually
two problems are involved: the “unperturbed” problem, for which the
solution is known, and the “ perturbed” problem, which is slightly different from the unperturbed one. We have already used perturbational
methods for calculating resonator quality factors and waveguide attenuation constants. Further uses are given in Secs. 7-2 to 7-4.

Variational Methods. The variational methods are useful for determining characteristic quantities, such as resonant frequencies, impedances, and so on. In contrast to the perturbational procedure, the
variational procedure gives an approximation to the desired quantity
itself, rather than to changes in the quantity. The variational procedure differs from other approximation methods in that the formula is
“stationary” about the correct solution. This means that the formula
is relatively insensitive to variations in an assumed field about the correct field. If the desired quantity is real, the variational formula may
be an upper orlower bound to the quantity. Furthermore, if an assumed
field is expressed as a series of functions with undetermined coefficients,
then the coefficients can be adjusted by the Ritz procedure (Sec. 7-6).
In fact, if a complete set of functions is used for the assumed field, the
exact solution can sometimes be obtained, at least in principle.

## Section 7-2: Perturbations of Cavity Walls
 Figure 7-la represents a resonant
cavity formed by a conductor covering S and enclosing the loss-free
region 7. Figure 7-1b represents a deformation of the original cavity

318 TIME-HARMONIC ELECTROMAGNETIC FIELDS
n n
Cny (a)
(a) (b)

Fi. 7-1. Perturbation of cavity walls. (a) Original cavity; (b) perturbed cavity.
such that the conductor covers S’ = S - AS and encloses r’ = 7 - Ar.
We wish to determine the change in the resonant frequency due to the
change of the cavity wall.

Let Eo, Ho, wo represent the field and resonant frequency of the original
cavity, and let E, H, w represent the corresponding quantities of the
perturbed cavity. In both cases the field equations must be satisfied,
that is,

-V xX Eo = jwouHo --V XE = jwonH (7-1)
V X Ho = jwoeEo VX H = jweE
We scalarly multiply the last equation by Ef and the conjugate of the
first equation by H. The resulting two equations are
‘. E}- VX H = juweE+ EF
--H-Vv X E} = -jwouH} -H
Adding these and applying the identity
vV-(AXB)=B-VxXA---A-VXB
we have
V+ (H X E}) = jweE+ EF - joonH} - H
By analogous operations on the second and third of Eqs. (7-1), we obtain
V- (Hi xX E) = jopH- Hi - jwoeE} + E
These last two equations are now added, and the sum integrated throughout the volume of the perturbed cavity. The divergence theorem is
applied to the left-hand terms, one of which vanishes, because n X E = 0
on S’.. The resulting equation is
px x E*-ds = jlo - wo) fff (E+ E* + pH-H¥) dr (7-2)
Finally, since n X Ey = 0 on S, we have
ff Hx Ef-ds =0

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 319
and the left-hand side of Eq. (7-2) can be written as
H x Ej-ds = H x E}- ds = - gbH x Ej -ds
f £. f
The last term is taken as negative, to conform to the convention that
ds points outward. We can now rewrite Eq. (7-2) as
iff H x BF -as
© - w) = = 8 (7-3)
fff (cE EX + pH 8 dr
This is an exact formula for the change in resonant frequency due to an
inward perturbation of the cavity walls. Note that our development
assumes that c and p are real, that is, we have assumed no losses. Problem 7-1 gives the general formulation in the lossy case.

The crudest approximation to be made in Eq. (7-3) is that of replacing
E, H by the unperturbed field Eo, Ho. For small perturbations this is
certainly reasonable in the denominator and should be valid in the
numerator if the deformation is shallow and smooth. With this approximation the integral in the numerator of Eq. (7-3) becomes

fpH x E}-ds ~ dp (Ho x E%) -ds
as 4S
= joo [ff (Lo)? - ull?) ar
ar
The last equality follows from the conservation of complex power [Eq.
(1-62)]. Substituting this into Eq. (7-3), and also substituting Eo, Ho
for E, H in the denominator, we have
If (u|Hol? - eB o]?) dr
wo- Wo b:
OO pe Be (7-4)
wo fff (lH + Bol) ar
Note that the terms in the numerator are proportional to the electric and
magnetic energies ‘“‘removed” by the perturbation, while the denominator
is proportional to the total energy stored. Hence, Eq. (7-4) can be
written as
o-v AWn - AW, (7-5)
oo Ww
where AW,, and AW, are time-average electric and magnetic energies
originally contained in Ar and ‘W is the total energy stored in the original

320 TIME-HARMONIC ELECTROMAGNETIC FIELDS
cavity. Finally, if Az is of small extent, we can approximate the AW’s
by Az times the energy densities at the position of 47. Furthermore,
Ww can be written as r times a space-average energy density #. Thus,
Eq. (7-5) can be written as

@ - oo _ (Wm - We) Ar _ Ar

: wo fe wr mie 7 (7-6)
where C depends only on the cavity geometry and the position of the
perturbation.

It is evident from the preceding equations that an inward perturbation
will raise the resonant frequency if it is made at a point of large H (high
tm), and will lower the resonant frequency if it is made at a point of
large E (high #.). The opposite behavior results from an outward perturbation. It is also evident that the greatest changes in resonant frequency
will occur when the perturbation is at a position of maximum £ and zero
H, or vice versa.

Numerical calculations using Eqs. (7-4) to (7-6) are easy for the cavities treated previously, because we calculated W when we determined the
Q’s. Kor the dominant mode of the rectangular cavity of *Fig. 2-19, W is*
given by Eq. (2-98), or

W= 5 |El?r
For Az located at the mid-point of the base (maximum £) we use Eqs.
(2-96) to find AW,, = 0, and
AW, = 5 |Bol? dz
Hence, from Eq. (7-5) we find
ea. 9M (7-7)
Wo T
If the perturbation occurs at the mid-point of the longer side wall (maximum H), we have AW, = 0 and
= _ e|E ol?
AW = 30+ 7B)
Hence, from Eq. (7-5) we find
Ww - wo 2 Ar
oo STE ET “s)
Note that for a square-base cavity (b = c) the change in resonant frequency due to Av at maximum H is only one-half as great (and in the
opposite direction) as that due to A7 at maximum £.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 321
‘Taste 7-1. Toe Parameter C or Eq. (7-6) ror DerorMaTions (a) aT MAXIMUM
E anv (b) at Maximum H or THE Dominant Move
Cavity | Geometry Cc
ZA TE (a) -2
Rectangular @i__ + « 2
(@sdso) a ©) Spe
a c (c/b)
Short cylinder my “A (a) -1.85
(d < 2a) = “(at (b) 0.5
; Pee (a) -0.843
Long cylinder oO 2.86
(d = 2a) (e) 1+ 7la/a?
()
: (a) -0.361
Spherical (b) 0.680
Hemispherical hs ios (b) 0.680
Lal

Table 7-1 gives the value of C in Eqs. (7-6) for cavities of several
geometries for Az located at (2) maximum F and (b) maximum H. These
values have been obtained using the crude approximations of replacing
E, H by Eo, Ho in Eq. (7-3). They are therefore valid only for smooth,
shallow deformations. In general, the frequency shift depends on the
shape of the deformation as well as on the shape of the cavity. The
formulas for deformations of the form of small spheres or small cylinders
can be obtained from the results of the next section by letting eand p-> 0.

## Section 7-3: Cavity-material Perturbations
 Let us now investigate the change
in the resonant frequency of a cavity due to a perturbation of the material
within the cavity. . Figure 7-2a represents the original cavity containing
matter e, ». Figure 7-2b represents the same cavity but with the matter
changed to € + Ae, p + Ap.

322 TIME-HARMONIC ELECTROMAGNETIC FIELDS
n n
Fie. 7-2. Perturbation of
matter in a cavity. (a)
Original cavity; (b) perSs Ss turbed cavity.
(a) (b)

Let Eo, Ho, wo represent the field and resonant frequency of the original
cavity, and let E, H, w represent the corresponding quantities of the
perturbed cavity. Within S the field equations apply, that is,

-V X Eo = jwouHo --V X E = jw(u + Au)H (7-9)
V X Ho = jwoeEo V XH = jole + Ad)E
As in the preceding section, we scalarly multiply the last equation by
Ej and the conjugate of the first equation by H, and add the resulting
two equations. This gives
v-(H X Ef) = jo(e + AQE + EX - juuHt -H
Analggous operation on the second and third of Eqs. (7-9) gives
_ V+ (HS X E) = go(u + Au)H- Hf - joocE} + E
The sum of the preceding two equations is integrated throughout the
cavity, and the divergence theorem is applied to the left-hand terms.
The left-hand terms then vanish, because both n X E = 0 on S and
n xX E,=0onS. The result is
0= fff Mole + Ae) - ool + BF + [olu + An) - oon - HE} dr
Finally, this can be rearranged as
a *
® [[[ (ES + oH HD ar
This is an exact formula for the change in resonant frequency, due to a
change in e and/or » within a cavity. Once again our development has
assumed the loss-free case, that is, c and » arereal. The general formulation when losses are present is given in Prob. 7-5.
In the limit, as Ae 0 and Au- 0, we can approximate E, H, w by
Eo, Ho, wo and obtain
won fff BelBel? + Aultfol®) dr
a (7-11)
0 If (e Eo]? + | Hol?) dr

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 323
This states that any small increase in « and/or » can only decrease the
resonant frequency. Any large change in c and/or p» can be considered
as a succession of many small changes. Hence, any increase in € and/or p
within a cavity can only decrease the resonant frequency.

We can recognize the various terms of Eq. (7-11) as energy expressions
and rewrite it as

ee = = i (= . + *H tn) dr (7-12)
where W is the total energy contained in the original cavity. Now if
the change in c and y occupies only a small region Av, we can further
approximate Eq. (7-12) by

eS -3 (#2 + SH ng)

w we Bb T
ak (« A 4 c,8H) (7-13)

€ B r

where z is the space average of W. The parameters C; and C2 depend
only on the cavity geometry and the position of Av. Note that a small
change in c at a point of zero E or asmall change in u at a point of zero H
does not change the resonant frequency. If we compare Eq. (7-13) with
Eq. (7-6), it is evident that C = C, - Ci. For the cases considered in
Table 7-1, Ar is either at a point of zero H, in which case C, = 0, or ata
point of zero EZ, in which case C; = 0. To be explicit, for a material
perturbation at (a) of Table 7-1 we have C; = -C and C, = 0, while for
a material perturbation at (b) of Table 7-1 we have C, = 0 and C2 = C.

The preceding approximations require that Ae, Ay, and Ar all be small.
We shall now consider a procedure for removing these restrictions on Ae
and Ay. This introduces the further complication that the change in
frequency depends on the shape of Az, as well as on its location. The
modification is accomplished by using a quasi-static approximation to the
field internal to Ar. This assumes that the field internal to Az is related
to the field external to Ar in the same manner as for static fields. The
procedure is justifiable, because, in a region small compared to wavelength, the Helmholtz equation can be approximated by Laplace’s
equation.

There are four types of samples for which this quasi-static modification
to the perturbational solution is very simply accomplished. These are
shown in *Fig. 7-3 for the dielectric case. For the magnetic case, it is*
merely necessary to replace E by H ande by u. For the thin slab with
E normal to it (*Fig. 7-3a), we must have continuity of the normal com*

324 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ee
(2) (6) (c) (d)
Fia. 7-3. Some small dielectric objects for which the quasi-static solutions are simple.
ponent of D, so that
1
Eva = = Euxt (7-14)
This approximation is valid regardless of the cross-sectional shape of the
cylinder. For the long thin cylinder with E tangential to it (*Fig. 7-30),*
we must have continuity of the tangential component of E, so that
Bist = Bose (7-15)
Again this approximation is independent of the cross-scctional shape of
the cylinder. For E normal to a long thin circular cylinder (*Fig. 7-8c),*
we can, use the static solution,! which is
“ Em = -- 5, (7-16)
int = Tope Best Finally, for E rformal to a small sphere (*Fig. 7-3d), we can use the static*
solution,? which is
amiga (7-17)
2+6
The static solution for a dielectric ellipsoid in a uniform field is also
known but is not very simple in form.”
To use the above quasi-static approximations, we approximate E (and i
H in the magnetic case) in the numerator of Eq. (7-10) by E,,: of the
preceding equations. In the denominator we can still use the approximations E = Ey and H = Hp, because the contribution from Ar is small
compared to that from the rest of r. Hence, our quasi-static correction
to the perturbational formula is
ome [ff dBi» BS ar
fae - (7-18)
@o 2fff e|Eol? dr
1W.R. Smyth, “Static and Dynamic Electricity,’ pp. 67-68, McGraw-Hill Book
Company, Inc., New York, 1950.
2 J. A. Stratton, ‘Electromagnetic Theory,” pp. 205-213, McGraw-Hill Book Company, Inc., New York, 1941.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 325
a x 3 » N IJAE @
a Ss N er
_---os™ g a
de |
(a) (b) (c)
*Fig. 7-4. Cavities used to illustrate the perturbational formulas.*
for the case Au = 0. (The denominator has been simplified by equating
‘W,, to W,..) The corresponding formula for the frequency shift due to
a magnetic material would be of same form, but with E replaced by H
and c by u« throughout.

Equation (7-18) is, of course, most valuable for problems for which
the exact solution is not known. However, so that we may gain confidence in the results as well as practice in the procedure, let us apply
Eq. (7-18) to problems for which we have the exact solution. These are
illustrated in *Fig. 7-4. For a dielectric slab on the base of a rectangular*
cavity (*Fig. 7-4a), we have EF, given by Eq. (7-14). The field and energy*
expressions for the unperturbed cavity are given in Sec. 2-8. Application of Eq. (7-18) then yields

oo lead (7-19)

wo 2 & G@

where d is the slab thickness and a is the cavity height. A comparison
of this with the result of Prob. 4-17 for yw: = we = po and €2 = €9 shows
that our answer is identical to the first term of the expansion for w in
powers of d/a. In fact, if A is also nonzero and we treat it to the same
degree of approximation (match tangential H), we again get the correct
first term of the expansion. To illustrate the improvement obtained by
using the quasi-static field, we can compare Eq. (7-19) to the result
obtained from Eq. (7-11), which is

@ - Wo 1 d

vag THe DG
It is apparent that the above formula is accurate only for e, ~ 1, that is,
when Ae is small.

A nonmagnetic dielectric slab at a side wall of the rectangular cavity
(*Fig. 7-4b) has but little effect on the resonant frequency, because E is*
zero at the wall. In this case E is tangential to the air-dielectric interface; so Eq. (7-15) should apply. Note that Eqs. (7-18) and (7-11) give

326 TIME-HARMONIC ELECTROMAGNETIC FIELDS
identical approximations in this case. In particular, we obtain
-_ = cd
OF OL («= 1) > | sin? dr
wo a ) a
a d 3
~-=(Q- = 7-20
3 - (2) (7-20)
A comparison of this with the answer to Prob. 4-18 shows that we again
have the correct first term of the expansion when Ap = 0.

As a final example, consider the spherical cavity with a concentric
dielectric sphere (*Fig. 7-4c). The field of the unperturbed cavity is*
defined by

1 r\ .
Hye= 5 dh (2.744 i) sin 6

and the stored energy is given by Eq. (6-35). Applying Eq. (7-18),
using the quasi-static Eq. (7-17), we obtain

@ 0 . 9.991% - 1 (2 744%)

ag 078 ale ats
where wis the radius of the small dielectric sphere and b is the radius of
the conductor. This we can compare to the exact solution (Prob. 6-8),
which is the same. The perturbational method used in conjunction with
the quasi-static approximation gives excellent accuracy when properly
used. This shift in resonant frequency caused by the introduction of a
dielectric sample into a resonant cavity can be used to measure the
constitutive parameters of matter.

## Section 7-4: Waveguide Perturbations
 We shall now consider waveguides
cylindrical in the general sense, that is, all z = constant cross sections
are identical. Figure 7-5a represents a cross section of the unperturbed
waveguide, *Fig. 7-5b represents a wall perturbation, and Fig. 7-5c represents a material perturbation. All perturbations must, of course, be*
independent of z. The guide boundary is taken as perfectly conducting
in all cases.

n a n
Eo, Ho Bs
$ Asdac e+ As
Pa B+ 4p
Cc Cc c
(a) (6) (c)
*Fig. 7-5. Perturbations of cylindrical waveguides. (a) Original cross section;*
() wall perturbation; (c) material perturbation.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 327

At the cutoff frequency a cylindrical waveguide is a two-dimensional
resonator. We should therefore expect formulas similar to those for
perturbations of cavities to apply to waveguides at cutoff. In fact, we
can apply the cavity derivations directly to the region formed by the
cylindrical waveguide bounded by two z = constant planes, changing
only some of the explanations. For example, in deriving Eq. (7-2), the
left-hand side results from the integral

dp (Hx Ef + Hh x E)-ds
taken over the perturbed surface. For a length of a cylindrical waveguide at cutoff, the fields are independent of z; so the surface integrals
over the two z = constant cross sections cancel each other. This leaves
only the surface integral on the left-hand side of Eq. (7-2) taken over the
wall of the waveguide. Following the derivation further, we find that
Eq. (7-3) applies directly for calculating the change in waveguide cutoff
frequency. But both numerator and denominator involve an integration
with respect to z, which reduces to the length of the segment of the cylindrical waveguide. Hence, from Eq. (7-3) we obtain the change in cutoff
frequency Aw, due to an inward perturbation of the waveguide wall as
j H x Ex-ndl
Aw, = _ i fjo HX BE n dl (7-21)
{/ (E+ EX + pH - H¥) ds
“i
where AC is the contour about the volume of the perturbation and S’ is
the cross section of the perturbed waveguide (see *Fig. 7-5b).*

The crude approximation of replacing the perturbed fields E, H by the
unperturbed fields Eo, Ho in Eq. (7-21) gives good results for smooth,
shallow perturbations. This leads to

Jf tHe? - B0l*) ds
ce ee (7-22)
we ff lta? + el Bal?) as
8
which is analogous to Eq. (7-4). Hence, an inward perturbation of the
waveguide walls at a position of high EF will lower the cutoff frequency,
while one at a position of high H will raise the cutoff frequency. For
perturbations not shallow and smooth, we can obtain a better approximation to Aw, by using a quasi-static approximation for H in the numerator of Eq. (7-21). An example of the perturbation of waveguide walls
is the “ridge waveguide,” formed from the rectangular waveguide by

328 TIME-HARMONIC ELECTROMAGNETIC FIELDS

adding ridges along the center of the top and bottom walls.!_ Such ridges
will lower the cutoff frequency of the dominant mode and will raise the
cutoff frequency of the next higher mode (see Prob. 7-12). Hence, a
greater range of single-mode operation can be obtained. The ridges also
decrease the characteristic impedance of the guide; hence, they are used
for impedance matching.

The formulas for material perturbations in cavities can also be specialized to the case of material perturbations in waveguides at cutoff. The
reasoning is essentially the same as that used for the wall-perturbation
case. Hence, from Eq. (7-10) we can obtain the exact formula for the
change in cutoff frequency due to a change of matter with the waveguide.
It is

Aes i | (AcE - EX + AuH - H¥) ds 28)
@e [[ (85+ u- HD ds
where the integrals are taken over the guide cross section. Note that
an increase in either « or » can only decrease the cutoff frequency of a
waveguide. If Ae and Ay are small, we can replace E, H by Eo, Ho and
obtain
‘ (Ac| EI? + Aul Hol?) ds
i Fisaldp eastde 2 eens (7-24)
; we J] (Bd? + ule) as
This is analogous to Eq. (7-11). If Ae and Ap are large, but of small
spatial extent, we can improve our approximation by using the quasistatic method of Sec. 7-3. For example, analogous to Eq. (7-18) we have
in the nonmagnetic case
tw. | f SB Ef ds
Se - + (7-25)
we 2ff e\Eo|? ds
where E;,. is given by the appropriate one of Eqs. (7-14) to (7-16).

As long as the perturbed guide is homogeneous in ce and p», we can
determine the propagation constant at any frequency from the cutoff
frequency according to

2
je = 5k ft =(@) o> 0,
y= (7-26)
w 2
a= kali -(2) wo <a
We

1§. B. Cohn, Properties of Ridge Waveguide, Proc. IRE, vol. 35, no. 8, pp. 783-788,

August, 1947.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 329
(This is proved in Sec. 8-1.) If the perturbed guide is inhomogeneous,
no such simple relationship exists. In such cases we can obtain perturbational formulas for the change in y. In theloss-free case we can express
the unperturbed fields as
Ep = Eo(z,y)e-#o
Ho = Aio(z,y)e~#o (7-27)
and the perturbed fields as
E = E(r,y)e*
H = A(z,y)e-* (7-28)
The perturbational formulas are then
$6 (Bt x H)-ndl
&- p= -i > (7-29)
[ (Bt x +E x At) -u, ds
Ss
in the case of a wall perturbation, and
[ff (B- BF + anh AD as
B - By = w Se (7-30)
ff (Bt x H+ x AY-u,ds
Ss
in the case of a material perturbation. The perturbational formulas in the
lossy case are given in Probs. 7-15 and 7-16.

To illustrate the derivation of the above formulas, consider a material
perturbation. The unperturbed and perturbed fields satisfy Eqs. (7-9)
with w = wo, for the frequency is kept unchanged. The two equations
following Eqs. (7-9) are still valid, and, with w) = w, their sum becomes

v-(H x Ej + Hi x E) = jw(AcE- E¥ + ApH: Hf)
Integrating this equation throughout a region and applying the divergence theorem to the left-hand term, we obtain
pu x Et + Hi x E)-ds = jo fff (cE + E* + ApH -H¥) dr (7-31)
This is an identity for any two fields of the
same frequency in a region for which « and Le
u are changed to e+ Ae and »+ Ap. For “tk
material perturbations in a cylindrical wave- NS 4)
guide, we express the fields according to Eqs.

(7-27) and (7-28) and apply Eq. (7-31) to Fra. 7-6. Differential slice of a
the differential slice of *Fig. 7-6. On the cylinder.*

330 TIME-HARMONIC ELECTROMAGNETIC FIELDS
waveguide walls both n X Eandn x E) vanish;so this part of the surface
integral vanishes. Also, since the thickness of the slice is a differential
distance,
+ |[ =a2]] = -j@-s)a
= Re = J 0
top bottom 8 Ss
The right-hand side of Eq. (7-31) can be expressed as the integral over
the cross section times dz; hence Eq. (7-31) reduces to
-i(B - 60) [[ (A x BS + Ay x B)-u,as
8
=o ff (Ach B* + ApH - H*) ds
8
Rearrangement of this equation gives Eq. (7-30). In the derivation of
Eq. (7-29), the right-hand side of Eq. (7-31) is zero, and the left-hand
side equated to zero leads to the desired result.

Equations (7-29) and (7-30) as they stand are exact. To use them,
we must make various approximations for E and H, just as we did in
the cavity problems of Secs. 7-3 and 7-4. For example, in the case of
shallow, smooth deformations of waveguide walls, we can approximate
£,H by*E,, Ay in Eq. (7-29). Using the conservation of complex power
(Eq. (1-62)], we arrive at the result

\ Jf (aor - Bol) as
B-8) =o ei ~ = ~ (7-32)
[[ Ge x Bo + B x Ag) - us ds
Ss
(The denominator is twice the time-average power flow in the unperturbed guide.) If the perturbation is not shallow and smooth, better
results can be obtained using a quasi-static modification. Similarly, for
small Ae and Ap we have the approximation for material perturbations
I i (Ae|Bol? + Au| fol?) ds
8 - By w = 8 __________ (7-38)
fl (Bt x Ay + B x Af) + ds
Ss
For large Ae and Ap we can obtain better results by using the quasi-static
approximation for the fields within Ae and Au.

As an example of the perturbational approach applied to a waveguide
problem, consider a circular waveguide of radius b containing a concentric dielectric rod of radius a, The exact solution to this problem was

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 331
10 Exact /\_|
solution
0.9 y
*Fig. 7-7. Comparison of G Bea*
the perturbational solu- 0.8 vA
tion with the exact soo = @ Y | 4 Perturbation
lution for the partially 07 EK }=~"| solution
filled circular waveguide, ek
€ = 10e, b = 0.4%0. 06
° soap es a ee
Oo 0.1 0.2 0.3
a/b
considered in Sec. 5-5, and a numerical example is shown in *Fig. 5-11.
For the perturbational solution we shall use Eq. (7-30) with Ap = 0. In*
the numerator we make the quasi-static approximation of Eq. (7-16),
and in the denominator we approximate £, A by E., Ho. The unperturbed field of the dominant TEn mode for the circular waveguide is
1 p\ .- E.
B, = 1s, (1841 8) sin c H, = -Z
_ 1841, p _E,
Bs => J (1.8818 cos c He = 7,
where Zo is the characteristic impedance (Eq. (5-32)]. The denominator
of Eq. (7-30) then becomes
2 [a [ «fo (@
at do | dp p(E,? + Ey”) = 0.7892- 1-\>
Zo Jo a) n o
where w- is the cutoff frequency. The numerator is easily evaluated as
we-l a\?
5rd «(1.841 )
and Eq. (7-30) reduces to
B - Bo 2.146 « -1/a\’
Pol #i*) te 7-34
ko V1 - (@,/e)? & +1\b ( )
Figure 7-7 compares this solution to the exact solution of *Fig. 5-11. Our*
approximations give good results for small a/b. At frequencies near the
unperturbed cutoff frequency, the w, in Eq. (7-34) may be taken as that
of the perturbed guide.

## Section 7-5: Stationary Formulas for Cavities
 Suppose we have a resonant
cavity formed by a perfect conductor enclosing a dielectric, possibly inhomogeneous. The “wave equations” are

vVxulv x E-o,*E =0
Vv xX ev XH - o,'xH = 0 (7-85)

332 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where w, is the resonant frequency. These reduce to the usual Helmholtz
equations when «and z are constants. If the first of Eqs. (7-35) is scalarly
multiplied by E and the resulting equation integrated throughout the
cavity, we obtain
[[[ Boy x wow x Bar
2 = SS __________ (7-36)
[ff ean
Similarly, multiplying the second of Eqs. (7-35) scalarly by H and integrating throughout the cavity, we obtain
[[[ Fey xv x Har
wo? = 2A (7-37)
[fore
Equations (7-36) and (7-37) are identities, but, even more important,
they are useful for approximating w, by assuming field distributions in a
cavity. They are particularly well-suited for this latter application
because of their ‘‘stationary”’ character, which we shall now discuss.
We take Eq. (7-36) and substitute for the true field E a trial field
NY Evia = E-+ AE = E + pe (7-38)
_
where p isan arbitrary parameter. This procedure gives
~ ff] B+ pe)-¥ x wv x E+ pe) dr
w(p) = (7-39)
Lf e(E + pe)- (E + pe) dr
where we show w? as a function of p for fixed e. The Maclaurin expansion of w? is
Ow? p? dw?
2, = w2 ao poo wae =
wp) = ot +p] + SS] + (7-40)
Note that the first term is the true resonant frequency, because
w?(0) = w,?. In the variational notation! the above expansion is written
as
2
o(p) = we? + pis? + - Sw. (7-41)
By definition, each term of Eq. (7-41) equals the corresponding term of
Eq. (7-40). The term 'w? is called the first variation of w*, the term 6%w?
is called the second variation, and so on. A formula for w? is said to be
1 F. B. Hildebrand, ‘‘ Methods of Applied Mathematics,” p. 130, Prentice-Hall, Inc.,
Englewood Cliffs, N.J., 1952,

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 333
stationary if the first variation of w? vanishes. This is equivalent to
dw? |
“ =0 7-42
OP |p=0 (7-42)
The extension to more than one p parameter is straightforward.
We now wish to show that Eq. (7-39) is stationary. The derivative
of the numerator N(p) evaluated at p = 0 is
nro) = [[[ @iv xy Keb ey x WIV XE) dr
It is a vector identity that
[ff #9 x wily x edr =fff pow xe-V X Edr
+ fp (uv x e) xX Ej: ds
The last term vanishes, because n X E = 0 on S. A similar identity
states
[[[ wo xed x Bar = ffferw x wy x Bar
- fp (uv x E) x elds
Using these two identities and the first of Eqs. (7-35), we obtain
N'(0) = 2oe [ff ce Edr - ff (u-t¥ x B) x el ds
The derivative of the denominator D(p) of Eq. (7-39) is, for p = 0,
Dio) =2 fff «Ea
We then obtain
_ D(O)N"(0) - N(O)D'O)
D*(0)
((etv XE) x e]- ds
=- (7-43)
eB? dr
which has been simplified, using Eq. (7-36). The above equation vanishes if n X e = 0 on S, which requires n X Eyin = 0 on S. Hence, Eq.
(7-36 is a stationary formula for the resonant frequency if the tangential
components of the trial E vanish on the cavity walls,

334 TIME-HARMONIC ELECTROMAGNETIC FIELDS

Equation (7-36) can be put into a more symmetrical form by applying
the identity
[[fev x wtV x Edr = If wV X E-V x Edr

+ dp (uv x E) x E]-ds
The last term vanishes, because n X E =0 on S. Substituting this
identity into Eq. (7-36), we obtain
If u-(V x E)? dr
ao, = $2 (7-44)
[[[ era
This formula proves to be stationary, provided n X Eyia =OonS. If
we look carefully at the first variation of Eq. (7-44), it is evident that the
requirement n X E,,: = 0 on S can be relaxed if the term
2 ff [uv x EB) x E]-ds
is added to the numerator. This gives
Sf ff ww x By de + 2.b (ut x E) x Ele ds
wp? = 622 --___________, + __________________ (7-45)
: ff eB? dr
which is stationary, even if n X Ex: #0 o0n S. This is an important
modification, because it is not always easy to find a trial field with vanishing tangential components on the cavity walls, especially if the geometry
is complicated. Still further modifications in our formulas are required
ifn X Eorn X (u~!v X E) are discontinuous over some surface within
the cavity. All such modifications can be quite simply effected by the
reaction concept of Sec. 7-7.

A similar procedure shows that Eq. (7-37) is a stationary formula in .
terms of H, provided n x (e-!'V X H) =00n S. The H-field formula
corresponding to Eq. (7-44) is

e\(v x H)?dr
wo? = [pf < i >~---. (7-46)
[foe
which turns out to be stationary subject to no boundary conditions on S.
Further modifications to account for discontinuities in n X H or n X
(eV xX H) over surfaces within the cavity can be made. These modifications again follow directly from the methods of Sec. 7-7.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 335
2 @2
2
wy? “At
= o2 l
1 1
w,2 H
|
2
Oo Pp P oO Pp “P
(a) (b)
*Fig. 7-8. Illustration of w? versus p for (a) astationary formula and (0) a nonstationary*
formula.

Let us now briefly consider the advantages of a stationary formula
over a nonstationary one. Figure 7-8 shows pictorally the primary
advantage. Given a class of trial fields of the form of Eq. (7-38), the
parameter w?(p) determined from a stationary formula such as Eq. (7-39)
will have a minimum or maximum at p = 0.! This is shown in *Fig.
7-8a. The parameter w? determined from a nonstationary formula must*
have some definite slope at p = 0, as shown in *Fig. 7-8b. For a given*
error in the assumed field, say AE = pyje, the corresponding error in the
resonant frequency is w;? - w,”. It is evident that for small pi the stationary formula gives a smaller error in w? than does the nonstationary
formula. This property is sometimes summarized as follows: ‘‘ A parameter determined by a stationary formula is insensitive to small variations
of the field about the true field.” An error of the order of 10 per cent
in the assumed field gives an error of the order of only 1 per cent in the
parameter. In some cases the true field can be shown to yield an absolute minimum or maximum for the parameter. The stationary formula
then gives upper or lower bounds to the parameter. Our formulas for w?
give upper bounds, as we shall show later.

We might also inquire about the general procedure of establishing
stationary formulas. One characteristic of all such formulas is that the
numerator and denominator contain squares of the trial field. This
insures that amplitude of the trial field will have no effect on the calculation. Classically, the method of establishing stationary formulas is to
construct formulas of the proper form and then separate the stationary
ones from the nonstationary ones by testing the first variation. In Sec.
7-7 we shall give a general procedure which leads directly to the various
stationary formulas.

1 A complex parameter would have a saddle point at p = 0.

336 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Now let us apply some of our stationary formulas to a problem for
which we have an exact answer, so that we may get an idea of the accuracy obtainable. Consider the dominant mode of the circular cavity
(*Fig. 5-7), for the case d < 2a. The TMoo mode is dominant and the*
exact resonant frequency is
oy = 24088 (7-47)
a Ven
The field is sketched in *Fig. 5-8 and is given mathematically by*
E, = J4(2.405 2) H, = 2405 j, (2.405 2)
g a a a
Substitution of this true field into any of our stationary formulas must,
of course, give us Eq. (7-47).
Suppose we first try a formula that requires no boundary conditions
[Eq. €7-46)]. Assume as a trial field
H=up VxH=u,2
Equation (7-46) then becomes
= w= ds fed de - 3
= @ > 2
. «uf, pvdp «Ma
and our approximation is
2.818
Op, (7-48)
a Vea
This is 16 per cent too high, which is a relatively poor result. This suggests that our trial field was too crude an approximation. We can
improve our trial field by assuming
- 2° = _?
w= u(p-%) vxH~ua(1~2)
which is chosen to satisfy the condition n X E=0 on S. Equation
(7-46) then yields
‘a 2
-_2
ae f a(i 2) edp 180
@ 2p\’ eu3la?
a i (- - 20!) pdp
and our approximation is now
2.410
oO, & 7-49)
1 en c

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 337
This is only 0.2 per cent in error. Even though a formula is stationary,
we must use care in choosing trial fields. It is advisable to meet the
physical boundary conditions as closely as possible, for this will help to
obtain a trial field close to the true field. If the same trial field is used in
Eq. (7-37), we again get Eq. (7-49), sincen X E = 0onS.

Now consider a stationary E-field formula, say Eq. (7-44). This

formula requires n X E = 0 on S; hence we choose
p 1
E=u.(1--- Vx E=u,a a
Substituting this into Eq. (7-44), we obtain
* p
2 i, a dp _ 6
o= Tal p\? ~ Ga?
“EC
Our approximation is therefore
wp = 2849 (7-50)
ave
which is 1.8 per cent too high. If we had chosen a trial E field not
satisfying n X E = 0 on S, we would have had to use Eq. (7-45).

Note that all our approximations are too high. This suggests that the
true resonant frequency is an absolute minimum, which we shall now
show. For example, take Eq. (7-39), and, by means of various identities,
put it into the form

[ff pe+(V X pV X pe - w,*epe) dr

wo? - w,?2 = 2 (7-51)

fff (EB + pe)? dr
It is known that the eigenfunctions, that is, the fields of the various
modes, form a complete set of orthogonal functions in the cavity space.!

Hence, the error field pe can be expanded in a series

pe = ») AE;

where the A; are constants and the E; are the various mode fields. Substituting the above equation into Eq. (7-51), making use of the wave

1 Philip M. Morse and Herman Feshbach, “‘ Methods of Theoretical Physics,” part I,
Chap. 6, McGraw-Hill Book Company, Inc., New York, 1953.

338 TIME-HARMONIC ELECTROMAGNETIC FIELDS
equation and the orthogonality relationships, we obtain
D we - we [ff Bear
@? = wo? = $-___________ (7-52)
J ff Gea)? dr

where the w; are the resonant frequencies of the 7th modes. Since we
have chosen w, as the lowest eigenvalue, Eq. (7-52) is always positive.
Hence, any w calculated from Eq. (7-36) will be an upper bound to the
true resonant frequency. Also, if we choose a trial field orthogonal to
the field of the lowest mode, we have an upper bound to the next higher
resonant frequency, and so on. This, of course, requires that the dominant mode be known exactly, which is seldom the case for complicated
geometries.

Look now at Eq. (7-46). The trial field H = constant vector is a
permissible trial field, since no boundary conditions are required. The
result is w, = 0, which is less than the true resonant frequency [Eq.
(7-47)]._ Why do we not have an upper bound in this case? The answer
lies in the fact that we have overlooked the ‘“‘static mode.”’ A static
magnetic field (w, = 0) can exist in a cavity bounded by a perfect electric
condtgtor. Fortunately, it is easy to insure that our trial field is orthogonal to ail static fields, thereby obtaining an upper bound to the dominant
a-c mode. Any trial field satisfying

N V-pH =0 nH, = 0onS (7-53)
is orthogonal to all static fields, as we shall now prove. The desired
orthogonality is

[ff HH + Hyus. dr = 0
where, in general, Hy... = -WU. By virtue of the identity
V+ (UpH) = pH: VU + ;UV- pH
the preceding equation becomes
[[f oy - maar - fb Uutt-as = 0
This requirement is met for all U by the conditions of Eq. (7-53). Our
choices for H in the foregoing examples satisfied Eq. (7-53); so we
obtained upper bounds to the dominant TMo1o mode, as desired.

## Section 7-6: The Ritz Procedure
 A further advantage of the variational
formulation is that one can choose the best approximation to a stationary
quantity obtainable from a given class of trial fields. This is done by

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 339
including adjustable constants, or variational parameters, in the definition
of the trial field and then choosing those parameters which will give a
minimum or maximum of the stationary quantity. For example, if we
choose

Evist = Evia(Ai,A, ... , An) (7-54)
where the A; are variational parameters, and substitute into the stationary formula Eq. (7-36), we obtain

w? = w(Ay,As,. ~~ , An) (7-55)
The best approximation to w,? will be the minimum value of w?, which
can be chosen by requiring
Ou” ;

3a 70 t=1,2,...,7 (7-56)

This general method is known as the Ritz procedure.
The most common way to include variational parameters is to express
the trial field as a linear combination of functions
Euiot = E,+ AiEy + A:E2 +: + AnEn (7-57)
Since the labor of the calculations increases approximately as the square
of the number of terms in Eq. (7-57), it is desirable to keep n small.
However, it is also necessary that some choice of the A; will give a
reasonably close approximation to the true field. When a complete set
of functions E, is used, the method may, in principle, lead to an exact
solution. It is also sometimes convenient to choose the E; as an orthogonal set.
For an example of the Ritz method, let us again consider the circular
cavity of *Fig. 5-7 and trial fields of the form*
H = uy(o9 + Ap?) vx H = u(2 + 3Ap) (7-58)
where A is a variational parameter. Note that H satisfies no boundary
conditions on S; so we choose Eq. (7-46) as the stationary formula.
Substituting the trial field into Eq. (7-46), we obtain
fp @ + 340)%e dp
gee
uf. (0 + Ao?)* dp
_ 15 8 +16Aa + 9(Aa)? (7-59)
@ep 15 + 24Aa + 10(Aa)?
1 The method is also referred to as the “ Rayleigh-Ritz procedure.”

340 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Note that the approximation of Eq. (7-49) is the special case Aa = -%.
To determine A by the Ritz method, we set
Ow?
3A 0
and obtain 24 + 55Aa + 28(Aa)? = 0
This can be solved for Aa as
-55 + V/337 _ { -1.3100

Aa=- 56 _ | -0.6543 (7-60)

A substitution of the second of these values into Eq. (7-59) gives
w = 24087 (7-61)
a Ven

which is smaller than what the first of Eq. (7-60) gives. Hence, Eq.
(7-61) is the desired “best”? approximation to the true resonant frequency [Eq. (7-47)]. The solution Aa = -1.31 gives ka = 7.191, which
is an approximation to the next higher eigenvalue 5.520. If the trial
field has two variational parameters, we obtain approximations to the
lowest three eigenvalues, and so on. The Ritz procedure also gives us
an aDgroximation to the true field, but it is difficult to establish the
nature of the approximation.

## Section 7-7: The Reaction Concept
! A general procedure for establishing
stationary fermulas can be obtained, using the concept of reaction as
defined in Sec. 3-8. To reiterate, the reaction of field a on source 6 is

(a,b) = [ (E+ ay’ - He- aM) (7-62)
If all sources can be contained in a finite volume, the reciprocity theorem
[Eq. (3-36)] is
(a,b) = (b,a) (7-63)
The linearity of the field equations is reflected in the identities
(a,b + c) = (a,b) + (a,c)

(Aa,b) = A(a,b) = (a,Ad) op)
where the notation Aa means the a field and source are multiplied by
the number A.

Many of the parameters of interest in electromagnetic engineering are
proportional to reactions. For example, the impedance parameters of a

1V.H. Rumsey, The Reaction Concept in Electromagnetic Theory, Phys. Rev., ser.
2, vol. 94, no. 6, pp. 1483-1491, June 15, 1954.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 341
multiport “network” are proportional to reactions, as shown by Eqs.
(3-41). Approximations to the desired reactions can be obtained by
assuming trial fields (or sources) to approximate the true fields (or
sources). It is then argued that the best approximation to a desired
reaction is that obtained by equating reactions between trial fields to
the corresponding reactions between trial and true fields. To be specific,
suppose we want an approximation to the reaction (c.,c.). (The symbol
c stands for “correct.’’) The approximation (a,b) is then best if we
subject it to

(a,b) = (cab) = (a,cs) (7-65)
because we have imposed all possible constraints. Equation (7-65) can
be thought of as the statement that all trial sources look the same to
themselves as to the correct sources.

The reaction (a,b) obtained from Eq. (7-65) is also stationary for small
variations of a and b about ca and ~. This we can prove by letting

@ =Ca + Palo b = cy + pols
and showing that
a(a,b) | (a,b)
a Set bd = =0 7-66)
OPa \po=pr=0 OD, |po=p»=0 ( )
Substituting for a and b into Eqs. (7-65), we have the three relationships
(a,b) = (casCo) + Po(lascs) + Po(ca,eo) + DaPo(Caso)
= (ca;Co) + Po(Caeo)
= (ca,Cs) + Palla,Cr)
Using the last two equations in the first equation, we obtain
(a,b) = (ca,co) - PaPo(Cases)
It is now evident that Eqs. (7-66) are satisfied, proving the stationary
character of (a,b).

We have a slightly different case when the reaction concept is used to
determine resonant frequencies of cavities. The true field at resonance
is a source-free field; so the reaction of any field with the true source is
zero. Hence, if we let a = b represent a trial field and associated source,
Eq. (7-65) reduces to

(aa) = 0 (7-67)
We can think of this as stating that the resonant frequencies are zeros
of the input impedance.

To apply Eq. (7-67), we assume a trial field and determine its sources
from the field equations. For example, an assumed E field can be sup

342 TIME-HARMONIC ELECTROMAGNETIC FIELDS
- - n n n
- - “a =_--, - <4
CIE) ED
\ 1
\ yy, \ J
ee ne eee,
(a) (6) ()
*Fig. 7-9. Sources needed to support (a) a trial E field, (b) a trial H field, and (c) both a*
trial E field and a trial H field.
ported by the electric currents
J = -joeE - Pad x (uv x E) (7-68)
However, if the trial field does not satisfy n X E = 0 on S, we need the
additional magnetic surface currents
M,=nxE on S (7-69)
to support the discontinuity in Eat S. This is illustrated by *Fig. 7-9a.*
We now substitute from Eqs. (7-68) and (7-69) into Eq. (7-67) and obtain
1
0 = we) = [[[s ear fu (Ze x ) as
3 -jo [ff e-ear+2 [/fe-v x (u-" x E) dr
a - i «(uo
2 ff (a x B)+ (wx E) ds
If n x E =0 on S, this reduces directly to Eq. (7-36). If n x E#0
on S, the above equation reduces to Eq. (7-45).
If a stationary formula in terms of the H field is desired, we consider
the trial field to be supported by the sources
M = -jopH - ty X (eV x H)
12 (7-70)
M, =n x (sv x H) on S
Jue
as represented by *Fig. 7-9b. Application of Eq. (7-67) now leads to Eq.*
(7-46), or to Eq. (7-37) if M, = 0.

Stationary formulas in terms of both E and H are also possible. This
time we consider both electric and magnetic currents, as shown in *Fig.
7-9c. They are found from the trial fields according to*

J = -jwowE+V XH
M = -jopH -V XE (7-71)
M,=nxE on S

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 343
Equation (7-67) then gives
0= [[[ @:-3-H-eM ar - fH: Mas
= [|] (-icet? +B-¥ XH+H-V x E+ jouH?) dr
- PE Xx H-ds
which can be rearranged to
[[[@-vxH+Hev x E)dr ~ dpE x H-ds
w = je (7-72)
ii (uH? - eB?) dr
This is sometimes called a ‘‘mixed-field” stationary formula. The minus
sign in the denominator might seem strange, but it is easily shown that
E and H are 90° out of phase in the loss-free case (see Sec. 8-4). Hence,
the denominator is twice the stored energy in the cavity.

Finally, if the trial fields have discontinuities in n x E orn X H over
surfaces within the cavity, we must add the appropriate surface currents
to support the discontinuities. This procedure leads to additional surface integrals in the stationary formulas, as shown in Probs. 7-27 and

## Section 7-28: Earlier we showed that reactions constrained according to Eq
 (7-65)
were stationary. But in the above cavity formulas we calculated w by
forcing the reaction to vanish. We shall now prove that the w so determined is stationary about the true resonant frequency. In the usual
manner, we let the trial field be the true field plus a parameter times an
error field, represented by

a=c-+ pe
For fixed e the reaction (a,a) is a function of both w and p. Equation
(7-67) constrains (a,a) to vanish; hence, as w and p are varied, we have
aaa)} 4, 4 Ha)! ag
00 |omw, OD \wruw
p=0 p=0
The second term of this equation vanishes because (a,a) is stationary
about p = 0. The coefficient of the first term is not in general zero; so
bo = 0
Thus, the first variation of w vanishes, and all formulas for w derived
from Eq. (7-67) are stationary.

The reaction concept also provides us with an alternative way of

viewing the Ritz procedure for improving the trial field or source. We

344 TIME-HARMONIC ELECTROMAGNETIC FIELDS
assume the trial field or source to be a linear combination of functions,
represented by
a= Uu+Vv+--- (7-73)

where U, V,... are numbers to be determined. According to the
reaction concept, all trial fields should look the same to themselves as
to the true source; hence we should enforce the conditions

(a,u) = (c,u)

(a,v) = (cw) (7-74)
Substituting from Eq. (7-73), we obtain the set of equations

Uluju) + V(vju) + + > + = (yu)

Utu) + Vio) + + + + = (vr) (7-75)
which can be solved for the parameters U, V, .... The solution so
obtained is identical to that obtained by the Ritz procedure.

To illustrate, let us reconsider the example of Sec. 7-6, which was the
Ritz procedure applied to the circular cavity (*Fig. 5-7). Our trial field*
was Eq. (7-58); so for the same approximation by the reaction concept
we choose

H* = usp H? = ugp? (7-76)
The sources of these fields, according to Eq. (7-70), are
M+ = -uyjoup my = 2
e
. . (7-77)
M’ = -u (ionot + 2) M," = Sia
WE WE
Calculating the various reactions according to Eq. (7-62), we obtain
- @ 2
= 2 S44 f
(uu) = 2nda (ioe a +32)
. @ 2
(u,v) = (v,u) = 2nda? (i$ + 2) (7-78)
5 Jwe
. a 9
= 4 dle Bian
(vv) = 2xda (jon 6 + 723)
All reactions with the correct source are zero, because the true field is
source-free. Hence, (c,u) = (c,v) = 0 and Eqs. (7-75) reduce to
Utu,u) + Viv,u) = 0
U(uv) + Viv») = 0

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 345
These equations can have a nontrivial solution only if the determinant
of the coefficients of U and V vanishes. Hence,
(u,u){v,v) - (uv)? = 0 (7-79)
is the equation from which w is to be found. The solution of Eq. (7-79),
with the reactions of Eqs. (7-78), yields Eq. (7-61).

## Section 7-8: Stationary Formulas for Waveguides
 At cutoff, a waveguide is
a two-dimensional resonator; so we should expect stationary formulas
for the cutoff frequencies to be of the same form as those for the resonant
frequencies of cavities. We must, of course, be careful in applying the
reciprocity theorem, because the sources of our trial fields are not of
finite extent. However, if we take a slice of the waveguide, as was done
in Sec. 7-4, surface integrals over the top and bottom just cancel at
resonance. The height of the slice is common to all terms and therefore
cancels. Starting from Eq. (7-67), we arrive at stationary formulas differing from our cavity formulas only in that volume integrals are replaced
by surface integrals and surface integrals by line integrals. Hence, the
E-field formula corresponding to Eq. (7-45) is

[fw x Beds +2 f [Gv x E) x B)-ndl
wo? = 14. (7-80)
l/ cE? ds
where n is the outward-pointing unit vector normal to the waveguide
walls. The H-field formula corresponding to Eq. (7-46) is
[[ ow x wads
oe? = a (7-81)
f | uH? ds
and the mixed-field formula corresponding to Eq. (7-72) is
[[ @-v xH+H-vxB)ds-fExH-ndl
We = J 0 Pg ee (7-82)
[[ qin = 2 as
None of the above formulas require boundary conditions on the trial
fields. Corrections for discontinuous trial fields can be made as outlined in the preceding section.

As an example, consider the partially filled rectangular waveguide of
*Fig. 4-8a. In Sec. 4-6 we obtained a transcendental equation for the*
cutoff frequency [Eq. (4-51)]. For a variational solution, let us use Eq.
(7-80) and a trial field

E = wsin =

346 TIME-HARMONIC ELECTROMAGNETIC FIELDS
which is the empty-guide field. The result is!

w= rae [1t 2S 8 (E-Zine (7-83)

a Venue €2 a Qn a

Note that this is an explicit formula for w., in contrast to the exact equation, which is transcendental. Table 7-2 compares the above result with
the exact solution for the case c, = 2.450 and c2 = €. We should expect
the approximation to become worse as €,/e2 becomes larger, since the
field then tends to concentrate more in the dielectric.

TaBLe 7-2. Ratio or Wavecuipe WipTH To CuTorr WAVELENGTH FOR THE

RECTANGULAR WAVEGUIDE WITH D1eLEcTRIC SLAB
(“Exact” values read from curves by Frank)
d/a a/d. (exact) | a/d. (approximate)
0 0.500 0.500
0.167 0.485 0.486
0.286 0.450 0.455
0.500 0.375 0.383
0.600 0.350 0.352
1.000 0.319 0.319
\, a a

A knowledge of the cutoff frequency of a waveguide homogeneous in
«and up is sufficient to determine the propagation constant at any other
frequency according to Eq. (7-26). If the guide is inhomogeneously
filled, as for 'xample the above-treated rectangular waveguide with
dielectric slab, there is no simple relationship between the cutoff frequency and the propagation constant. We therefore have need of stationary formulas for propagation constants.

Tn all of the previous examples, the field equations were given by an
operator which was self-adjoint with respect to the desired integration.?
For inhomogeneously filled waveguides, the field equations lead to an
operator which is not self-adjoint. Hence, an appropriate adjoint operator must be found and the derivation of the stationary formulas suitably
modified. It turns out that the operator for waves traveling in the -z
direction is the adjoint of the operator for waves traveling in the +z
direction, and the derivation proceeds as follows.

Define +2 traveling waves as

Et = E*(c,y)e = (E, + u,B, je

Ht = At(z,y)e* = (AL + uF, Je“ (7-84)

1A. D. Berk, Variational Principles for Electromagnetic Resonators and Waveguides, JRE Trans., vol. AP-4, no. 2, pp. 104-110, April, 1956.

?B. Friedman, “Principles and Techniques of Applied Mathematics,” John Wiley
and Sons, Inc., New York, 1956, p. 44,

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 347

Substituting these into the field equations, we obtain

Vv x Et + jouH* = ju, x B+

Vv X Ht - jweE+ = jpu, x Ht
Using analogous definitions for ~z traveling waves, we find

Vv x E- + joxH- = -j6u, x E
Vv x H- - jwek~ = -j@u, x HBy direct substitution, it can be shown that for any +z traveling wave
solution there exists a -z traveling wave solution given by

E- = E-(z,y)e® = (B, - u,B,)e%*

H- = B-(ry)o = (-B, + u.ff,)o* (7-85)
where the E,, Hi, &., and 4, of Eqs. (7-84) and (7-85) are the same
functions.

Now multiply the first of the +z wave equations scalarly by H-, and
the second of the -z wave equations by Et, and add the two resultant
equations. This gives
A--v x B+ 4 Bt. 0 x A + jopH-- At -jocBt-B
= -26f, x A,-u,
which, when integrated over the guide cross section and rearranged, yields
[ff (edit Be = onli AO + jf v x B+ + JB v x AO) ds
B oS SSS eee eee
2/f Bx Huds
(7-86)
This is a mixed-field formula, stationary ifn x E=0onC.

For the E-field formulation, eliminate H from the +z and -z wave
equations, and proceed as in the derivation of Eq. (7-86). The resultant
formula is
a? | f wba ds - 328 [fw BB, as

+ ff Wow x BY + (V x B+) - wrt B4ds = 0 (7-87)
stationary ifn x E = OonC. The H-field formula is given by Eq. (7-87)
with c, u, E replaced by u, e, H, and it is stationary with no boundary
conditions on H. Equations (7-86) and (7-87) remain stationary in the
lossy case, for which 78 should be replaced by y = a + jp.

For an example of the calculation of propagation constants, consider
the centered dielectric slab in a rectangular waveguide, as shown in the
insert of *Fig. 7-10. As a trial field, take*

_ 0x
£ = usin 7

348 TIME-HARMONIC ELECTROMAGNETIC FIELDS
1.6 T
oh db
elt
14 Z re d/a= 1.0-/ke---a-__+ x L- Soar
= 7 0.3
12 (32450 0 Yew Le=
: | LE :
2 = 0.1
= 4 Ls
08 7 a <I ie)
Exact --Approximate ---~
0 0.2 0.4 0.6 0.8 1.0 12
afro
*Fig. 7-10. Comparison of approximate and exact propagation constants for the*
rectangular waveguide with centered dielectric slab, « = 2.45c. (After Berk.)
and use Eq. (7-87). The result is!
NBL e-efd, 1. xd am \?|%
ko [2 + €0 (2 + zon x) (c) | (788)
The exact solution is given in Prob. 4-19 and requires the solution of a
transcendental equation. A comparison of a values obtained from Eq.
(7-88) with the exact values for 8/ko is shown in *Fig. 7-10 for the case*
€ = 2.45ce0.

## Section 7-9: Stationary Formulas for Impedance
 A formula for impedance
in terms of reaction is given by Eq. (3-41). Such a formula, when constrained according to Eq. (7-65), is a stationary formula for impedance.

Figure 7-11 represents a perfectly conducting antenna excited by a
current source. The resultant current on the antenna will distribute
itself so that tangential components of the total electric field vanish on
the conductor. The antenna terminals are close together; so the reaction
of any field with the current source isof theform -VJ. If atrial-current
distribution J,* is assumed on the antenna, the formula for input impedance [Eq. (3-41)] is

a,a 1
2, = - 90 = - Fgh Jot ds (7-89)
1 Berk, op. cit.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 349
where J is the input current. The impedance as calculated by Eq. (7-89) is stationary about the true current,
as we shall now show. On the antenna surface, the tangential components of the true field E* are zero except at
the input; hence
(ca) = -Vel = -P Zin = (a,a) sf
Also, (c,a) = (a,c) by reciprocity; so the constraints of
Eq. (7-65) have been met, and Eq. (7-89) is a stationary
formula.

Equation (7-89) was used to calculate impedance before its stationary character was noticed.!. This method
should not be confused with the induced emf method *Fig. 7-11. An*

1 antenna excited
2n= - GaGhE-Jras (7-90) by a current
| 1 source.
which is based on the conservation of complex power.
Equation (7-90) is not stationary unless both the true current and the
trial current are real. When the trial current is assumed real, we get
the same answer from Eqs. (7-89) and (7-90). Hence, the input impedances for waveguide feeds calculated in Sec. 4-10 are also variational
solutions to the same problems.

If we have two sets of input terminals, as, for example, in the case of
the two linear antennas shown in *Fig. 7-12, the variational formula for*
mutual impedance is

Za = - GH) =) Bae. tds (7-91)
where J, and J; are the input currents at terminals a and 8, respectively.
The demonstration that the constraints of Eq. (7-65) are met is similar
to that for self-impedance. Note that Eq. (7-91) involves the assumption of currents due to both sources, since E* is the field of J.*. The
extension to N sets of terminals is straightforward.

The calculation of mutual impedance is usually simpler than the calculation of self-impedance because the source and field points are separated.
Let us therefore take a mutual-impedance problem as our first example.
Consider the parallel linear antennas of length \/2 as shown in the insert
of *Fig. 7-12. No appreciable error will be incurred by assuming the currents as filamentary, as long as the antenna diameters are small compared*
to wavelength and compared to antenna separation. Let the z axis lie

1P.S. Carter, Circuit Relations in Radiating Systems and Applications to Antenna
Problems. Proc. IRE, vol. 20, no. 6, pp. 1004-1041, June, 1932,

350 TIME-HARMONIC ELECTROMAGNETIC FIELDS
80
el ‘
60
a via
40 i
g \_
- 20
AaxN
| \ // : - |
ik | | i:
~ 40
*Fig. 7-12. Mutual impedance Zs = Res + JjXas between parallel \/2 linear antennas in*
free space.
along antenna a, and assume
- = tecos2 BB I, cos 2% (7-92)
\ aN A
Our formula for mutual impedance [Eq. (7-91)] becomes, in this case,
1 4 nerd
a= - Tals le eee
By the usual vector-potential method we have
op 1 (P41 pe) ye
B. =i (S+K) a.
where, at antenna b,
1 7 en skV Eee
Af = i | 1°(2’) 5 di’
4m J yy Va + (2 - 2/)
Substituting for #,* and J* in our expression for Zs, we obtain
»/4 »/4 ,
Za = - dz dz’ cos 2ne cos 2n2 G(2,2") (7-93)
=v/4 =r/4 » »
1 ry en skV EF EF
= a 2 ~
where G(z,2’) Tajo (a3 +k ) ViPGs (7-94)

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 351
The integrations of Eq. (7-93) can be expressed in terms of sine integrals
and cosine integrals. The details of the integration can be found in the
literature.! Letting

Za = Ra + jXo
we obtain for the result
Ra = Ze (2 Cilkd) - Cid)? +? + 4] - Cit aye +? = 2°}
Xos = Z" [2S8i(kd) - Sil Ed)? +e? + x4] - Sil (hd)? Fx? - 27}}
oT
(7-95)

where Ci(x) and Si(x) are as defined in Prob. 2-44. Figure 7-12 shows a
plot of Eqs. (7-95). The mutual impedance between linear antennas of
other lengths and orientations can be found in the literature.)

The evaluation of the self-impedance of a linear antenna is more difficult because of the singular integrands encountered. Let us use this
problem to illustrate the use of adjustable parameters in the trial current. The geometry of the center-fed linear antenna is shown in the
insert of *Fig. 7-13. Let the current on the antenna be represented by*
two functions, according to Eq. (7-73). Our trial current is then a surface current of the form

J, = Uj + VJ." (7-96)
where U and V are adjustable parameters. According to the reaction
concept, the trial functions should look the same to the assumed current
as to the true current; hence we enforce the conditions

(a,u) = U(u,u) + V(o,u) = (oyu)
{a,v) = U(uv) + Viv,v) = (c,v)
where (c,u) and (c,v) can be calculated, as we shall later show. Solving
for U and V, we have in matrix notation
U| _ | (uu) @,u) [| (o,u)
[l= [ies Gal Le: (eee
Substituting for U and V into Eq. (7-96) and calculating the self-reaction,
we obtain
= (uu) (vu) |? | (c,u)
(asa) = Ken) ew) [rd Oud 11 fond (7-98)
1P.S. Carter, Circuit Relations in Radiating Systems and Applications to Antenna
Problems, Proc. IRE, vol. 20, no. 6, pp. 1004-1041, June, 1932.

2G. Brown and R. King, High Frequency Models in Antenna Investigations, Proc.

TRE, vol. 22, no. 4, pp. 457-480, April, 1934,

352 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ee a a
I eat
wala il
SE
» 3000
: Pt TT TA TT yt
6
2) LT ee
2000 : : Lt | tt eres tT
JL LEYT NNO
> (a)
SEEETT TAL LETT
poe a
Lc} | | TA TTT TT
eee
eee Ae
s o | | ArN\ | | CA I
f | | itm=w\\| Erm | | |
ol VA | | | Fy] | tf
HAT HAA H |_|
ba Se
- 1600
SA oN SZ
ve a GA A
L iets TT Tae TT |
Oo 2 4 6 8 10 12
kL
(b)
*Fig. 7-13. Variational solution for the input impedance of the symmetrical cylindrical*
antenna. (After Y. Y. Hu.) (a) Input resistance; (6) input reactance.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 353
Equations (7-97) and (7-98) also apply to the case of N adjustable constants if the various matrices are extended to N rows and/or columns.
Expanding Eq. (7-98), using the reciprocity condition (u,v) = (v,u), we
obtain
(ajay = (e20%o) = Aesnd(esy(u0) + (eys)*u)
, (uju)(vyv) - (u,v)?
Now note that n X E* = 0 on the antenna surface except at the feed; so
(ct) = -Viels
for any z, where V,, is the input voltage and J, is the x current at the
input. Using the above two relationships in Eq. (7-89), we obtain
2. = 7 I,%(uju) - 21.1.(uv) + 1.2(v,v)
noes (ur)? = (uju)v,v)
which can be rearranged to read
z uu) = (r4,1)(0,0)
Bu = Tuju) - 21, 1,{u,v) + 1.2(v,v) (7-99)
where J, and J, are the values of the wu and v trial currents at the input.
Let us now look at the form of the reactions. The currents will be
rotationally symmetric z-directed surface currents on the cylinder p = a,
where a is the antenna radius. These currents can be expressed as
1
Je = ona P)u (7-100)
where I? is the total current and x = u, v. By the potential integral
method we can calculate the field of the current J.” as
pe=-t (m4 2) [ we [ avrca 7-101)
fray (# +S) [ae [Paws, 7.
e sk 0? Fat 2pa cos (6- $+ @= 2)?
where G = Se eee (7-102)
Vp? + a? - 2pa cos (c - 6’) + (@ - 2’)?
The various reactions of Eq. (7-99) are then given by
L/2 2a
(x,y) = | de i adg Ee Jy (7-103)
-L/2 0
where £,? is given by Eq. (7-101) with p = a. Note the singular nature
of the Green’s function [Eq. (7-102)} at p = a.
A precise evaluation of Eq. (7-103) would be difficult; so the following
approximation is usually used. The field of the current is approximated
by the field of a filamentary current of the same magnitude. This is

354 TIME-HARMONIC ELECTROMAGNETIC FIELDS
equivalent to replacing Eq. (7-102) for p = a by
enV att ee)
@ = -=---_ (7-104)
Vet e-2’)?
For thin antennas, the error introduced by Eq. (7-104) is negligible, as
can be shown by the following argument. The field of the filament of
current is a source-free field in the region external to the linear antenna.
We can therefore assume that this field exists and calculate the equivalent currents on the surface of the antenna. As long as the equivalent
magnetic currents are negligible, as they will be for thin antennas, we can
take the equivalent electric currents for our trialcurrents. The resultant
current is essentially that of Eq. (7-100). Using the above approximation for G, we obtain from Eq. (7-103)
LP ae [az eye (ee + @)@ (7-105
= 2 v nan Co) = aia [ote [1 Pe (i+ Fe (7-105)
where G is given by Eq. (7-104). Note that, to this approximation, the
self-reaction is equal to the mutual reaction between two identical antennas fed in phase and separated by a distance a. Hence, Eqs. (7-95) with
d replied by a give the first-order (one trial function) variational solution for ‘the input impedance of a \/2 linear antenna. In particular,
note that for very small a = d, Eqs. (7-95) reduce to
‘ Ri = 73.1 Xin = 42.5 (7-106)
as is evident from *Fig. 7-12. Resonance (X = 0) occurs for L slightly*
less than d/2.
For trial functions in the second-order solution,
I* = sin aC - il)
L (7-107)
r=1- cos k (5 = ))
have been used in the literature. The evaluation of Eq. (7-105) for
(x,y) = (u,u), (u,v), and (v,v) is long and involved, and formulas in terms
of sine integrals and cosine integrals have been given by Storer! and Hu.?
Numerical values of the input impedance are given in *Fig. 7-13. The*
antenna is said to be resonant when X is zeroandkL ~ nz, nodd. Itis
said to be antiresonant when X iszeroandkL =~ nm,neven. Note that,
1J. E. Storer, Variational Solution to the Problem of the Symmetrical Cylindricai
Antenna, Crufi Lab. Rep. TR 101, Cambridge, Mass., 1952.
2 Y.Y. Hu, Back-scattering Cross Sections of a Center-loaded Cylindrical Antenna,
IRE Trans., vol AP-6, no. 1, pp. 140-148, January, 1958.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 355
in the vicinity of resonance, F is in- E=Ei+E* n
sensitive to antenna thickness. It
is in these regions that the analysis Ksource Obstacle
of Sec. 2-10 gives good results. Both
trial currents of Eqs. (7-107) are zero
at the input for kL = 4x. Hence, *Fig. 7-14. Wave scattering by an obthe input impedance calculated there- stacle.*
from cannot be valid in the vicinity
of kL = 4x. Perhaps a better choice for the v current would be

raha

which is finite at z = 0 for all L > 0. However, calculations have not
been made for this choice.

## Section 7-10: Stationary Formulas for Scattering
 Let us first treat the backscattering, or radar echo, type of problem by the variational method.
The problem is represented by *Fig. 7-14. It consists of a source and one*
or more obstacles, and we wish to determine the field scattered back to
the source. For simplicity, the obstacle will be considered a perfect conductor and the source a current element Jl. The more general case of
dielectric obstacles is considered in Sec. 7-11.

Let the incident field, that is, the free-space field of the source alone,
be denoted by E*. The total field E with the obstacle present is then the
sum of the incident field E* plus the scattered field E*. The reaction of
the scattered field on the current element is

(s,i) = IlEy = -IV* (7-108)
where V* is the scattered voltage appearing across J. Let the echo be
defined as the ratio of Ey to Il. Then, using reciprocity, we have

_ Ev _ (si) _ 8)

Echo = Fp = (in? ~ UD

1 .
= i. J, d: -109
am f ® J. ds (7-109)
where J, is the current induced on the perfectly conducting obstacle.
The boundary condition at the obstacle is n X E = 0, or

nx Ei = --n XE’ on S (7-110)

Hence, Eq. (7-109) can be written as

_ 7! _ _ 0) 
Echo = am PE J.ds = - pp (7-111)
where (c,c) stands for the self-reaction of the “correct” currents induced
on the obstacle by the source.

356 TIME-HARMONIC ELECTROMAGNETIC FIELDS
For a stationary formula, we assume a current J* on S and approximate
(c,c) by (a,a), subject to the constraint
(a,a) = (ca) = -(i,a) (7-112)
The last equality results from Eq. (7-110). To express this constraint in
a form for which (a,a) is insensitive to the amplitude of J*, we take
- (ay
(a,a) = (aa)
and, replacing (c,c) by (a,a) in Eq. (7-111), we have
. 2
-tiay _ _ (PEs Fas)
Echo = ayy = - (7-118)
(1) (a,a) (1)? ff Es. Jeds
where E2 is the field produced by the assumed currents J*. This is the
variational formulation of the problem. Note the close similarity of the
echo problem to the impedance problem of the preceding section. The
impedance problem is essentially an echo problem for which the source is
at thegbstacle. A more general formulation of the echo problem can be
made byreplacing Jl with an arbitrary source.

The tensor Green’s functions of Sec. 3-10 can be used to put Eq. (7-113)
into a more descriptive form. Define [I'(r,r’)] as the tensor of proportionality betw'en a current element dJ* at r’ and the field dE* that it
produces at r, that is,

aBo(r) = (Pr) dyer’)
Then Eq. (7-113) can be written as
2
-_ fp Ei(r) - Jo(r) ds
Il
Echo = ---$$_$____-__op as db as’ J) WENT)
This equation is in a form characteristic of variational solutions in general.

A commonly calculated parameter is the echo area, defined by Eq.

(3-30). For linearly polarized fields, the echo area is given by
3 , | Bt?
A. = lim (Coa | i ’) (7-114)
rs 1
If, in *Fig. 7-14, we let IZ be z-directed and located on the z axis, and then*
let r = x- ~, we have, in the vicinity of the obstacle,
Ei= wet ei = u, Heit

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 357

“ETT TTT TTT TT

o + tt tt ttt tt fe
pi tt of || ft
EI i] |
L
1.5 Hi
| L/a = 150
5 > 20
‘ott | [| |
1.0
Pi TAT | Ty fat I
BE Gee l\ew
0.5 | \ |
SEF INS kee
-CUISSES
Oo 2 4 6 8 10 12
kL
*Fig. 7-15. Broadside echo area A, of a wire. (After Y. Y. Hu.)*
Also, by definition, we have echo = £,*/J1; hence from Eq. (7-113)
2
nBo uz+ J°e* ds
we eh):
52dr ff E*- J°ds
Therefore, by Eq. (7-114), our stationary formula for echo area is
a (fp J reike ds)" i
Ae = 7 | PAY (7-115)
ff E*. Jeds
when the incident plane wave is z-polarized and -z traveling.

As an example, consider the scattering of a plane wave by a thin conducting wire, as represented by the insert of *Fig. 7-15. The integral in*
the denominator of Eq. (7-115) is just the self-reaction of the assumed current on the wire. This is the same type of reaction that we encountered
in the linear-antenna problem, approximated by Eq. (7-105). Defining
A as the self-reaction, we have

= re a = 1 _ Lp ! Ja, ‘a(2! 2 id
A= ff® Jeds ~ ma [a “pt POLE) e+ 55)@

(7-116)

358 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where G is given by Eq. (7-104). For the current on the wire we should
expect a constant current “forced” by the incident field plus a “‘naturalmode” sinusoidal current. At the ends of the wire, the current should
be practically zero; hence we assume for our trial current
I* = cos kz - cos ne (7-117)
Equation (7-116) can then be evaluated as
Re (A) = 4 [(kKL + kL cos kL - 2 sin kL) Si (kL)
7
+ log 2ykL - Ci (2kL) - sin? (kL)]
(7-118)
=" 258i i ais
Im (A) = i {cx +kL cos kL -2sin kL) [ci (kL) + log |
+ Si (2kL) - (1 + cos kL) sin ix}
where y = 1.781. The integral in the numerator of Eq. (7-115) evaluates to
LR _1 . kL kKL\ _ B
it, I*(z) dz = i? sin - kL cos *) =F (7-119)
which defines B. Hence, the echo area is
Z n2 | Bt 2
x =-|77- 7-120
. Ae 16x*| A/y | ( )
with A and B given by Eqs. (7-118) and (7-119). This solution gives
good accuracy out to about kL = 8. Figure 7-15 shows a plot of A./d?
for the second-order solution (two trial functions), as calculated by
Y. Y. Hu. The results for plane waves incident at an arbitrary angle
are given by Tai.? He also shows the effect of choosing different trial
functions.

In two-dimensional problems, the quantity echo width L. corresponds
to the echo area of the three-dimensional problems. The echo width is
defined as the width of incident wave which carries sufficient power to
produce, by cylindrically omnidirectional radiation, the same backscattered power density. In equation form, the echo width is

L, = lim (2° x) (7-121)
poe s

1Y. Y. Hu, Back-scattering Cross Section of a Center-loaded Cylindrical Antenna,
IRE Trans., vol. AP-6, no. 1, pp. 140-148, January, 1958.

2C. T. Tai, Electromagnetic Back-scattering from Cylindrical Wires, J. Appl. Phy.,
vol. 23, no. 8, pp. 909-916, August, 1952.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 359
or, for linear polarization, 8 .
yh
ra | 7
L, = lim (2x0|5/') (iz) =o gk OE OUT
oe hu 4*
where superscripts s and stand for < 4
“scattered” and “incident,” respec- | | | LA |
tively. Going through a develop- 2 vA,
ment similar to that used for Eq. | +] | |
(7-115), except that a line source is {|
used, we obtain 0 02 04 06 O08 10
a/x
2\2
om (f Je dl) *Fig. 7-16. Echo width L, of a conductL.= 12 ST | (7-128) ing ribbon of width a.*
p Bete dl
if the incident field is z-polarized and -x traveling. Similarly,
22
Jeol dl
t= | a (p terete ary (7-124)
2d | c Es: Jedl
if the incident field is y-polarized and -z traveling. From symmetry,
J* in Eq. (7-124) should have no z component. In both Eqs. (7-123)
and (7-124), it is assumed that the scatterers are cylinders generated by
elements parallel to the z axis and the line integrals are in a transverse
(z = constant) plane.

For an example of a two-dimensional problem, consider a z-polarized
plane wave normally incident on a conducting ribbon of width a. This is
illustrated by the insert of *Fig. 7-16. Assume that the current induced*
on the ribbon is uniform, that is,

Je=1 (7-125)
Because the current is real, the integral in the denominator of Eq. (7-123)
is

2/2 ate = [% Weyer =
[20 Bede dy = [°" Bele* dy = -P
where P is the complex power per unit length supplied by J... But we
have already analyzed the ribbon of uniform current in Sec. 4-12, the
result being
ri
P= 'PZ = a? & Vanes

where Y,,.c is plotted in *Fig. 4-22. The echo width, according to Eq.*

360 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Receiver
7
*Fig. 7-17. Differential*
scattering.
n
Transmitter
h Obstacle
(7-123), is then
7 na® eS 2r | 1 [
pee |e 2] 7-126
b= Klagyveal ~ laren (7-128)
A plot of this is shown in *Fig. 7-16. For large a we can use Eq. (4-107)*
and obtain
2ra?
Loe (7-127)
which is also the physical optics approximation (see *Fig. 3-21).*
The.more general case of differential scattering, or transmission,! is
represented by *Fig. 7-17. The problem consists of a transmitter, which*
illuminates:the obstacle, and a receiver at which we wish to evaluate the
scattered signal. For simplicity, let us consider both the source and
receiver to be tnit electric currents. Then, according to Eq. (3-39), the
voltage across the receiving current due to the transmitting current is
Vz = -(tyr)ovstacte present (7-128)
where c and r refer to the source or field of the transmitter and receiver,
respectively. The total signal received is the superposition of the incident field, due to the transmitter alone, plus the scattered field, due to
the currents c on the obstacle. Hence,

V, = V+ Ve = -(tr) - (er) (7-129)
where (t,r) is calculated with the obstacle absent and (c,r) involves the
free-space field of the currents on the obstacle. The transmitter and
receiver currents are assumed to be known (they are current elements in
our simplified case); so V,* can, in principle, be calculated exactly. Our
problem is to obtain the variational formula for V,*.

We shall here consider only the simple case of a perfectly conducting
obstacle, the general case being considered in Sec. 7-11. Applying reci
1 A transmission problem involves the evaluation of the total field at the receiver,
while a scattering problem involves the evaluation of only the scattered field.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 361
procity, we have, for the scattered voltage at the receiver,
~V? = (er) = (re) = fp (E')" - (J)! ds (7-130)
where (J.°)' is the surface current induced on the obstacle by the transmitter and (E')' is the field of the receiver current calculated with the
obstacle absent (the incident field). Our boundary conditions on the
various true fields aren X E = 0 at the obstacle boundary; hence

nx (E)yr = -n x (FE)

n x (Ei) = -n x (E)! (7-131)
where superscripts i and s refer to incident and scattered components,
and c and r refer to transmitter and receiver sources. Hence, by Eqs.
(7-130) and (7-131), we have

Ve = fp EY: (Go! ds = ene) (7-182)
where (c,,c:) stands for the reaction between the field of the “correct”
currents induced on the obstacle by the receiver and the “correct” currents induced by the transmitter. For our stationary formula, we
approximate (c;,cr) by (a,,a), where the a’s denote assumed currents on
the obstacle, and constrain the latter according to Eq. (7-65), which is

(dy,2) = (Cry) = (az,ct) (7-133)
In the language of the reaction concept, Eq. (7-183) says that the assumed
currents look the same to each other as to their respective true currents.
By Eqs. (7-131) and reciprocity, Eqs. (7-133) become

(art) = (Cre) = - (1,04) (7-134)

(a,,as) = (dryer) = (Cr) = -(t,ar)

Substituting from Eqs. (7-134) into Eq. (7-132), we have for our variational formula
(rade,
yim = Mott
V; (ay) (a,c)
(E*)" . (J.7)t ds (E*)* . (j.*)" ds
Ig Ig 1 aan
dp BY Ge)'ds
where (E*)' is the field due to the assumed currents (J.°)’, which approximate the currents induced by the receiver. Note that Eq. (7-135)
involves the assumption of currents on the obstacle due to sources at
both the transmitter and receiver. Note also that Eq. (7-135) reduces
to the formula for back-scattering [Eq. (7-113)] when the transmitter
and receiver coincide.

362 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 7-11: Scattering by Dielectric Obstacles
 The problem of differential
scattering by a dielectric obstacle is represented by *Fig. 7-17 if the*
obstacle is now considered as a dielectric body. We shall assume it to
be nonmagnetic (u = po), but it may be lossy if « is complex. The
extension to magnetic obstacles is given in Prob. 7-42.
When the obstacle is excited by a source, there will be induced in it
polarization currents given by
Je = jo(e - e)E = cE = x(E* + E*) (7-136)
Superscripts c or r will be added to the various quantities to indicate that
the exciting source is at the transmitter or receiver, respectively. The
treatment of differential scattering of the preceding section made no
assumptions about the nature of the obstacle in the derivation of Eq.
(7-130); hence for unit currents at c and r
=Ve = (re) = fff eo +d ar (7-187)
where the notation is the same as in the preceding section. Using the
relationship E‘ = E - E* and Eq. (7-136), we can rewrite Eq. (7-137) as
‘NY --Vf= If KU) + (J) dr - If (E*)'+ (J) dr
a = F(e,,c1:) - (Cree) (7-138)
which defines~the functional F. Note that F is symmetrical in c, and
c, and is actually the reaction between E* and (J*)t with the obstacle
present.
To obtain a stationary formula for the scattered voltage at the receiver,
we approximate the true currents c by trial currents a and set
-V = F(a,,a:) - (dy,a:) = G(a,,a:) (7-139)
subject to constraints of the form of Eq. (7-65) applied toG. Such constraints are
G(a,,a2) = G(c,,a1) = G(dr,cr) (7-140)
and we find
Gear) = (ran) = [ff (EA + (Ie) dr
(7-141)
Carer) = (tar) = fff CB) Oey ar
Combining the preceding equations to render V,* insensitive to the ampli1M. H. Cohen, Application of the Reaction Concept to Scattering Problems, IRE
Trans., vol. AP-3, no. 4, pp. 193-199, October, 1955.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 363
tudes of the trial functions, we have the variational formula
_yse- (r,a1)(tyar)
r F(a, ,a.) - (47,4)
Uffer-ore| [ff ere] a sun
[ [foo Dota = fff Bor Tide
For the lossy case, « = jue + o- For a perfectly conducting obstacle,
o- o;hence x?- 0 and Eq. (7-142) reduces to Eq. (7-135).

When the transmitter and receiver are represented by the same source,
we have the back-scattering problem. Using the definition of Eq. (7-109)
for echo, when the source is a unit current, we have

_ Ve @a)/)?
Echo = 2" = Flaa) - (aa)
1 i 2
(i [[***)
-- os 7d ae (7-143)
ii KJ *)? dr - If E*: Jcdr
The echo area, defined by Eq. (7-114), can be obtained from Eq. (7-148)
by letting the source recede to infinity. The steps parallel those used to
obtain Eq. (7-115). Fora z-polarized, -z traveling incident wave, we
obtain
2 2
J Pert? dr
A.=r|2 SH Eile Eee ) (7-144)
X fff ey dr - [ff B-dea
In two-dimensional problems, the echo width, defined by Eq. (7-122), is
found to be
2 2
" J ee* ds
L, = a aU ee ay ) (7-145)
X| ff rsa)? ds - [[ Bededs
if the incident wave is -z traveling and z-polarized, and
2 2
n J ye* ds
Le= 1 AUP ee J : ) (7-146)
X) ff ee)? ds - [[ B-Ieas

if the incident wave is -z traveling and y-polarized. Tie surface inte
grals in Eqs. (7-145) and (7-146) are over the cross section of the obstacle

in az = constant plane.

364 TIME-HARMONIC ELECTROMAGNETIC FIELDS
To illustrate the accuracy that we might expect from the variational
formulas, let us consider a problem for which the exact solution is available, the circular dielectric cylinder. The incident wave is z-polarized,
and the cylinder is defined by p = a = do/2, as shown in the insert of
*Fig. 7-18. For our first approximation, let us take*
J° = ue* (7-147)
where k = w ~/euo is the wave number of the dielectric. This very crude
assumption yields curve (b) of *Fig. 7-18. For a better approximation,*
which yields curve (c) of *Fig. 7-18, take*
Je = u,(e** + Ae) (7-148)
where A is a variational parameter to be determined either by the Ritz
procedure or by the reaction concept. While Eq. (7-148) is a better
approximation than Eq. (7-147), it is still crude. The integrations
occurring in the various reactions were accomplished by expressing the
exponentials and Hankel functions as Bessel function series, according to
Sec. 5:8. The resulting series converged fairly rapidly.
An alternative procedure for treating dielectric obstacles can be given
: ; [fi
0.00012 T
Ars !
/
xo ke /
0.00008
< oy)
> I a) cc)
4 aw [OTN |
. LTAve |
N“. N
NL Y\)
0.00004 Z| IN ~ ty) A | | | ti
1.00 104 1.08 1.12 1.16 1.20 1.24 1.28
</eo
Fia. 7-18. Scattering by a dielectric cylinder (a) exact solution, (b) first-order variational solution, and (c) second-order variational solution. (After Cohen.)

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 365
in terms of equivalent currents over the surface of the obstacle.!_ This
method leads to more than one formula for the desired parameter, and
Rumsey discusses how to choose the best approximation according to
the reaction concept.

## Section 7-12: Transmission through Apertures
 The problem of transmission
through apertures in an infinitely thin, perfectly conducting plane is
closely related to the problem of scattering by plane obstacles. The precise interrelationship is shown by the following extension of Babinet’s
principle for optics.

Consider the three cases of a given source (a) radiating in free space,
(b) radiating in the presence of an electrically conducting screen, and (c)
radiating in the presence of a magnetically conducting screen, as shown
in *Fig. 7-19. The electric and magnetic screens are said to be complementary if the two screens superimposed cover the entire y = 0 plane*
with no overlapping. (The aperture of one is identical to the obstacle
of the other.) Let the fields y > 0 be designated (E‘,H*), (E*,H’), and
(E",H™) for the cases (a), (b), and (c), respectively. Then Babinet’s
principle for complementary screens states that

E+E" =E H + H" = Hi (7-149)
proved as follows. Let S, be the screen surface of *Fig. 7-19b, and S. be*
the aperture surface of *Fig. 7-19b. The total field in each case is the*
incident field E‘ plus the scattered field E* produced by the currents on
the screen. An element of electric current produces no components of
H tangential to any plane containing the element (see Sec. 2-9). The
currents induced on the screen thus produce no tangential H over the
y = 0 plane; hence

n X He =n x Hi over Sa
On the screen itself we have the boundary condition
nx E*=0 over S,
For the complementary magnetic screen, following similar reasoning,
we find
n X E™=n Xx Et over S,
n xX H™=0 over Sa
By the above four equations, the sum E* + E, H* + H* satisfies
n X (Ec+ E*) =n X EF over S,
n X (H*+ H™) =n x HE over Sa

1V. H. Rumsey, The Reaction Concept in Electromagnetic Theory, Phys. Rev.,

2 ser., vol, 94, no. 6, pp. 1485-1491, June 15, 1954,

366 TIME-HARMONIC ELECTROMAGNETIC FIELDS

Hence, the e + m field has the same n X Eas the incident field over part
of the y = 0 plane and the same n X H over the rest of the y = 0 plane.
These conditions are sufficient to determine E, H in the region y > 0
according to the uniqueness theorem (Sec. 3-3); so Babinet’s principle
[Eq. (7-149)] follows.

An alternative statement of Babinet’s principle can be given in terms
of the dual problem to *Fig. 7-19c, shown in Fig. 7-19d. If the original*
source is replaced by its dual (J replaced by K), the magnetic screen
replaced by an electric screen, and the medium replaced by its “reciprocal”’ (q by 1/n), then E will be numerically equal to -H™ and H numerically equal to E™ (see Table 3-2). If the field of this dual problem is

|
Electric conductor | S*
| Ei, Hi 1 Es, He, 0
|
f Sourde | { Source Sa
|
| 8
. fa n
|
y=0 yx=0
(a) (6)
\s Is,
|
Em, H™, 10 E4, H', 1/n0
Sa Sa
4 source Magnetic conductor A ouat source | Electric conductor
| |
| Ss Is,
-T Ln
|
y=0 y=0
() (d)
*Fig. 7-19. Illustration of Babinet’s principle.*

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 367

Electric conductor | Et Ei+Es

Magnetic oa
Na aX y ly
Transmitter Receiver Transmitter Receiver
(a) (6)

*Fig. 7-20. The transmitted field E‘ of (a) is equal to the scattered field E* of (b).*

denoted by E+, H4, Babinet’s principle [Eq. (7-149)] becomes

E+ Ht = Et He - E* = Ht (7-150)
The problem of *Fig. 7-19d is more easily approximated physically than is*
the problem of *Fig. 7-19c.*

The direct application of Babinet’s principle to the problems of *Fig.
7-20a and b shows that the field transmitted by an aperture in a planeconducting screen is equal to the negative of the field scattered by the*
complementary obstacle. Hence, stationary formulas for, the signal at
a receiver on the shadow side of a screen are of the same form as the
stationary formulas for the scattered signal at a receiver in the complementary problem. In *Fig. 7-20b, let the sources at the transmitter and*
receiver be magnetic currents across the ‘‘terminals” 1, and 1,. Then,
dual to Eq. (7-135), we have at the receiver

[{[ c+ ameyas] [ff cea aney as]

Heel, = - 4 -______-'s (7-151)
ik ii (H*)r - (M,*)' ds

where M,* denotes the assumed magnetic current on the obstacle. It
approximates the true magnetic current

M, = (E+ - E-) Xn =2E'Xn (7-152)
where E+ and E~ denote E in the regions y > 0 and y < 0, respectively,
and n=u,. The interrelationships between *Fig. 7-20a and b can be*
expressed as

Hi = -H Et = --E

368 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Hence, from Eq. (7-151), we obtain for the aperture problem
Uff (Hi): (n x B*)‘ds | [ff (H)!. (n x B+) ds]
Hed, = S5-_______= =" 4+______________~ (7-153)
ff (He) - (n x E*)* ds

where E* is an assumed field in the aperture and H? is the magnetic field
calculated from the E*. The sources of H‘ are magnetic current elements
across |, and 1,, and, to apply Eq. (7-153), we must assume an n X E in
the aperture due to (H')! alone and due to (H*)’ alone. If 1; and 1, are
images of each other, as they appear in *Fig. 7-20, then the aperture*
problem becomes the same as an echo problem, because of the symmetry
of the plane screens about y = 0.

Sometimes it is the total power transmitted through the aperture that
is of interest. We define the transmission coefficient T of an aperture
as the ratio of the power transmitted through an aperture to the power
incident on the aperture, that is,

Re [[ Bx H*-ds
‘ T = see eg) (7-154)
‘ Re [[Eix H*-ds
apert
Note that 7 depends on both the nature of the source and the geometry
of the aperture. Another quantity sometimes defined is the transmission
area, which is the transmission coefficient times the area of the aperture.

We shall explicitly consider uniform plane waves normally incident on

an aperture in a plane screen, as shown in *Fig. 7-2la. Let the incident*
i Complete electric
Electric conductor | P conductor
Et, He Et, Ht
Incident
plane wave
-- M.
cs n
7 y=0 y=0
(a) (6)
Fia. 7-21. (a) Transmission through an aperture, and (b) equivalent problem for the
region y > 0.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 369
wave be specified by
Hi = ue” Ei = ,H' X wy (7-155)
where u is any unit vector orthogonal to uy. In the proof of Babinet’s
principle, we noted that in the aperture
nx H‘=n x Hi (7-156)
because the currents on the conducting screen produce no tangential
components of H in the y = 0 plane. Equation (7-155) chooses H? to be
real in the y = 0 plane; so by Eq. (7-156) n X His real in the aperture.
Hence,
3 = Re [f Bix H-ds = Re [[ Bx He ds (7-187)
apert apert
Now consider the problem of *Fig. 7-21b, which for*
M,=ExXn (7-158)
is equivalent to *Fig. 7-2la in the region y > 0. Hence, in the equivalent*
problem,

& = -- Re IJ M, - H!- ds = Re (cc) (7-159)
where (c,c) is the self-reaction of the correct magnetic currents radiating
in the presence of an electric conductor covering the entire y = 0 plane.

For a variational formulation, we approximate (c,c) by (a,a) and constrain (a,a) according to Eqs. (7-65), that is,
(c,c) = (a,a) = (c,a) = (a,c)
heer sources radiate in the presence of the conducting plane. We
new ) ae by reciprocity, and (c,a) can be calculated because we
nx =n xX H‘. Hence, our stationary formula for (c,c) is
2
Hi. M,* ds
to) = Ek = ee ait) (7-160)
He - M,* ds
where H? is the field of the assumed current M,°. For the incident field
of Eq. (7-155), we have the power incident on the aperture given by
0; =7A (7-161)
where A is the area of the aperture. Hence, combining Eqs. (7-154) to
(7-161), we have
2
u-n X Eds
7 = Re ([[ wn x Bas) (7-162)
A [[ eon x Beds

370 TIME-HARMONIC ELECTROMAGNETIC FIELDS
2.0 where E* is the assumed tangential
| electric field in the aperture and His
15 Ei } af the magnetic field calculated from E*
by the methods of Sec. 3-6.
& 10 Exact As an example, let us consider the
Variational two-dimensional problem of trans05 mission through a slot, as shown in
the insert of *Fig. 7-22. If we assume*
E* in the slot to be real, then
Oo 02 #04 06 08 1.0
a/d E* x He* = (E* x H*)*
*Fig. 7-22, Transmission coefficient for and the denominator of Eq. (7-162)*
a slotted conductor, incident wave is
polarized transverse toslotaxis. (After
Miles.) [ | He-n x Eeds =
([[ ®: x He*- as)"
In Sec, 4-11 we defined the admittance of an aperture as
Vayu = we ff ® x H*-ds
and calculated it for a slot for particular assumed E’s. Hence, applying
Eq. (7-162) to a unit length of our two-dimensional slot, we have
re) [ u-Ee x “|
a (2 (7163)
where a is the width of the slot. When the incident wave is polarized
transverse to the slot, we have the case of *Fig. 4-22; hence we take*
Ee =1 (7-164)
in the slot. Now Eq. (7-163) reduces to
1 1
= - 7.

T 7a Re (=) (7-165)
where Yipee = Go + jBz is shown in *Fig. 4-22. From Eqs. (4-106) we*
have for small a

T m (7-166)
and from Eqs. (4-107) we have for large a
T- +1 (7-167)
hae

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 371
This last result is the geometrical optics approximation. The variational
solution is compared to the exact solution, which can be obtained by
solving the wave equation in elliptic coordinates! (*Fig. 7-22). The case*
of a plane wave at an arbitrary angle of incidence is considered by Miles.”
If the incident wave is polarized parallel to the axis of the slot, we have
the case of *Fig. 4-23; so to make use of the analysis of Sec. 4-11 we would*
assume
Ee = cos = (7-168)
in the slot. Equation (7-163) then reduces to
4a 1
T = - Re( = 7-169
aa Vive ( )
where Yup: = Ga + jBa is shown in *Fig. 4-23. From Eqs. (4-115), we*
have for small a
a 3
T Fay 8-85 (:) (7-170)
For large a we should expect the field in the aperture to be uniform.
Hence, we should not expect the trial field of Eq. (7-168) to give good
results for large a, say a > A. Equation (7-169) actually approaches
0.81 for large a, instead of the expected value 1.
PROBLEMS

## Section 7-1: Suppose the cavities of Fig
 7-1 contain lossy material characterized by c, c,
and». Show that the perturbational formula corresponding to Eq. (7-3) is
iff H Xx Ey: ds
AS
@ ~ wy =
fff [E+ Ey - pH Hy} dr
Note that both w and w» must be complex. A complex resonance in the low-loss case
can be interpreted according to
= mis
oe (1 + 5)
where w, is the real resonant frequency and Q is the quality factor (see Sec. 8-14).

## Section 7-2: Consider the perturbation of a cavity (say Fig
 7-1a) from one having perfectly conducting walls to one having a wall impedance Z, defined by
nXE= ZH:
1 Morse and Rubenstein, The Diffraction of Waves by Ribbons and Slits, Phys. Rev.,
vol. 54, no. 11, pp. 895-898, December, 1938.
2J. W. Miles, On the Diffraction of an Electromagnetic Wave through a Plane
Screen, J. Appl. Phy., vol. 20, no. 8, pp. 760-770, August, 1949.

372 TIME-HARMONIC ELECTROMAGNETIC FIELDS
at the walls. Show that the exact perturbational formula is
<j ff ZH + Hods
oe - a = =
ff (B+ Ey - pH: Hy) dr
where the subscript 0 denotes unperturbed quantities. Note that wo is real but w is
complex if Z has a real part.

## Section 7-3: Use the results of Prob
 7-2 and the approximations
E+E, =|E| HH ~ Hy =3|Ho
to show that
j fp Z\|H,|? ds
wo - oo &
[ff ea + attra ar
Use the relationships
= i = R
i o(1 +3) Z=A+5u
and show that the perturbational formula gives
‘ ff cima as wn fff trae ae
‘ O, - wo = - --------_ Te ee
2fff plHol? dr off alzte as
Note that the formula for Q is identical to the one that we have been using if
® = Re (yn), where 7 is the intrinsic impedance of the conducting walls.

## Section 7-4: Use the results of Prob
 7-3, and show that the fractional change in resonance
due to metal walls is
ee = 00 gt
wo 2Q
where wo is the resonant frequency of the cavity with perfectly conducting walls.

## Section 7-5: Suppose the cavities of Fig
 7-2 are characterized by o ando + Ao in addition
toe, »ande + Ac, » + dp. Show that the perturbational formula corresponding to
Eq. (7-10) is then
[ff ee = i0/s)B + By - au + Hol dr
oo
° Jf [ e -ie/oe - By = uit He dr
Both w and w are complex if c and c + Ao are not identically zero.

## Section 7-6: Use the result of Prob
 7-5 for the case « = 0, and let E ~ Ey = |Egl,
H = Ho = j|Hol, w ~ wr + jwo/2Q, to show that
a f f | e\Eol? dr
=
J [f seb ae
and that Eq. (7-11) still applies with w changed to o.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 373

## Section 7-7: Suppose that a small sample of lossy dielectric is introduced into a cavity
whose unperturbed resonant frequency is wo
 Show that
' -« =
€” ° = 29 wo where @ = c’ - je’’ is the complex permittivity of the sample and w, is the perturbed
resonant frequency. If the losses of the unperturbed cavity are significant, then
1 dost
QQ 2%
where Q, and Qp are the Q’s of the cavity with and without the sample, respectively.

## Section 7-8: Consider a rectangular cavity with a small centered dielectric cylinder, as
shown in Fig
 7-23a. Show that the change in the resonant frequency of the dominant mode due to the introduction of the dielectric is
ww _ 2A
wo be I~)
where A is the cross-sectional area of the cylinder. Use a quasi-static approximation.
Area A
Za BON Pe
t jie ie ges
a ooo c LO adhe
ae \- 7
= c Va ss ©
a baa
(a) (0)
*Fig. 7-23. Rectangular cavity with (a) dielectric cylinder and (b) dielectric sphere.*

## Section 7-9: Consider the rectangular cavity with a small centered dielectric sphere, as
shown in Fig
 7-23b. Show that the change in the resonant frequency of the dominant mode due to the introduction of the dielectric is

wo _ _ de 1
o abce +2
where d is the diameter of the sphere. Use a quasi-static approximation.

## Section 7-10: Consider the circular waveguide of Fig
 5-2. Suppose the wall is slightly
flattened at the point c = 90°. Show that the change in cutoff frequency for the
a-polarized (E in the center points in the z direction) dominant mode is

fee. oss,
@e xa’
where A is the cross-sectional area of the deformation and w, = 1.841/a ~/en is the
unperturbed cutoff frequency. For the y-polarized dominant mode,
dee 149A
We 7a
Hence, the mode degeneracy has been removed.

374 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 7-11: Figure 7-24a shows a small centered dielectric cylinder in a rectangular
waveguide
 Show that the change in cutoff frequency of the dominant mode from
that for the empty guide is

Aes oo Pe
we Babe, 1
wherew, = 7/b »/eu. Usea perturbational method and a quasi-static approximation.
7 -- 4
7 © a
sea
Hd k(a) (0)
*Fig. 7-24. Rectangular waveguide with (a) dielectric cylinder and (b) conducting*
ridges.
%

## Section 7-12: Consider the rectangular waveguide with small semicircular ridges, as shown
in Fig
 7-245. Use a perturbational method and a quasi-static approximation to show
that the dominant-mode cutoff frequency differs from the TE: rectangular guide
cutoff, according. to

Bide = Or
w 2ab
where w, = 7/b+/eu. Show that the next higher mode (b < 2a) cutoff frequency
differs from the TEs: rectangular guide cutoff, according to
Aw. _ rd?
ae
@ 4ab
where w. = 27/b »/eu. Hence, the mode separation is increased.

## Section 7-13: Consider the rectangular waveguide with the bottom covered by a thin
dielectric slab (Fig
 4-6 with d <a). Use a perturbational method and quasi-static
approximation to show that the phase constant is

a eg ki? - k?d
Be Bot oie G
where fo = kz V/1 - (f./f)? is the empty-guide phase constant. Note that this is
the same as the first term of an expansion of the exact characteristic equation, as
given in Prob. 4-14.

## Section 7-14: Consider the rectangular waveguide with a centered dielectric cylinder, as
shown in Fig
 7-242. Use a perturbational method and quasi-static approximation to
show that,

B= Bo _ rd*e -1 1
ko 2ab e +1 4/7 - (we/)?
where w, can be taken as the cutoff frequency of the perturbed guide, given in Prob

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 375
7-11, if w is close to w,. Show that at the unperturbed TE: cutoff frequency
wh a[r@e tl
Be nN Tab I

## Section 7-15: Suppose that a waveguide is filled with lossy material, and consider a perturbation of its perfectly conducting walls
 Represent the unperturbed fields (subscript
0) and the perturbed fields (no subscript) by

E, = Boon E = Ber
Ho = Hoew™ HH = Her
Note tiie opposite directions of propagation. Show that the formula corresponding
to Eq. (7-29) is
$ £ XH-nd
ac
Yo = FE
[f (Eo X H - E X Ao): u, ds
‘s?
Show that this reduces to Eq. (7-29) in the loss-free case.

## Section 7-16: Consider the perturbation of material in a lossy waveguide from e, », o to
« + Ac, » + Ap, o + Ac
 Represent the fields as in Prob. 7-15, and show that the
formula corresponding to Eq. (7-30) is

[fio de 5 a0 )B Bo - w anit Hol ds
1
[[ Geox - 8 x fy ards
Show that this reduces to Eq. (7-30) in the loss-free case.

## Section 7-17: Use the results of Prob
 7-16, and let the unperturbed guide be loss-free.
Denote the propagation constant of the perturbed guide by y= a@ + J8, and let
E ~ Eg and H ~ -Hj. Show that the resultant approximation for 6 is Eq. (7-33)
and

f f do (Bol? ds
2
ane ff B x At-u, ds
Note that this is an approximate form of Eq. (2-76).

## Section 7-18: Consider the perturbation of the walls of a waveguide from a perfect conductor to an impedance sheet Z such that
n XE = ZH
Represent the unperturbed and perturbed fields as in Prob
 7-15, and show that
fp zit fia a
YO YO Re laa
[[ Sx -8 x fy - weds

## Section 7-19: Use the results of Prob
 7-18 and let the unperturbed guide be loss-free,

so that yo = jf. In the perturbed guide, let Z=Q+jX, y =a +j6, E = Ej,

376 TIME-HARMONIC ELECTROMAGNETIC FIELDS
H = -Hy}, and show that
fp silt
BE Be
2Re [ f By x At- ude
f alfa at
i
aRe ff EB, X A}: u,ds
If Z =, the intrinsic impedance of metal walls, the above formula for a is the
approximation that we have been using to calculate attenuation in metal waveguides.

## Section 7-20: Show that
[fiw xara
pie Fe
J | i] Bl? dr
is a stationary formula for the resonant frequency of a loss-free cavity, provided
n XE = 0onS, but is not stationary if losses are present

## Section 7-21: Show that Eq
 (7-46) is a stationary formula for w,?, with no boundary conditions r'quired on H.

## Section 7-22: Consider the rectangular cavity (Fig
 2-19) and the stationary formula (Eq.
(7-44)]. Use a trial field

E = uzy2ly - b)(2 - c)
and show that Eq." (7-44) gives
_ V10 . fot Fo?
Or be V on
In the exact solution [Eq. (2-95)], the numerical factor is x instead of 4/10.

## Section 7-23: Consider a small deformation of the walls of a cavity, such as represented by
Fig
 7-1. Take the variational formula [Eq. (7-45)], which requires no boundary conditions on E, and take the unperturbed cavity field Eo as a trial field. Show that
Eq. (7-45) reduces to

[ff ours - ea ae
wt - ow, “ar
7 =F
“ J ff dese ar
Show that this formula is essentially the same as Eq. (7-4).

## Section 7-24: Figure 5-31) shows a partially filled circular cavity
 Use Eq. (7-46) and a
trial field
H = wii (2-405 A)
to show that the dominant mode resonance is
2.405 b ( 2)
3 SS A (Se
we a Veouo V d &.
Compare with the results of Prob. 5-24.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 377

## Section 7-25: Consider a waveguide whose cross section is an equilateral triangle of side
lengtha
 Use variational formulas to approximate the lowest cutofffrequency. The
exact solution is

4
We =
3a Ven

## Section 7-26: Consider the rectangular cavity (Fig
 2-19) and the mixed-field variational
formula [Eq. (7-72)]. Choose a trial field

E = u, sin 4 sin @
6 c
H = w,Aj sin 5 cos ~ + ws cos 7 sin
where A; and A: are variational parameters. Determine A: and «iz by the Ritz
method, and show that the resultant formula for w, is the exact formula [Eq. (2-95)].
Why do we get an exact solution in this case?

## Section 7-27: In Fig
 7-25, the surface S represents a perfect electric conductor enclosing a
cavity. A variational solution is desired in terms of a trial field satisfying n X E = 0
n
*Fig. 7-25. Trial fields are discontinuous over s.*
on Sand n X (u-!¥V X E) continuous at s, but with n X E discontinuous at s. Show
that the stationary E-field formula is
[[[ioxmaseff (i -B) XL vx Eds
Ce 7 2 ee
pe
where subscripts 1 and 2 refer to regions 1 and 2 (*Fig. 7-25). Show also that a variational solution in terms of trial fields satisfying n X E = 0 on Sandn X Econtinuous*
at s, but with n X (u-!V X E) discontinuous at s, is given by Eq. (7-44).

## Section 7-28: Show that the variational H-field formula for Prob
 7-27 is of the same form
as the above E-field formula, given by replacing E by H, « by », and# by «. Show
that no boundary conditions at S are required in the H-field formula.

## Section 7-29: Consider a perturbation of material in a cavity, such as represented by Fig

## Section 7-2: Take the mixed-field variational formula [Eq
 (7-72)], and take the unperturbed
cavity field Eo, Ho as a trial field. Show that Eq. (7-72) then reduces to Eq. (7-11).

## Section 7-30: Repeat Prob
 7-26, using the reaction concept of Sec. 7-7.

## Section 7-31: Consider the partially filled rectangular waveguide of Fig
 4-8a. Use the
E-field variational formula [Eq. (7-8)], and the trial field

Pe
E = u,sin =

378 TIME-HARMONIC ELECTROMAGNETIC FIELDS
and show that
we =[1 +828 a(' - isin 224) |
a & a Qn a
Compare some calculated points with the exact solution (*Fig. 4-9).*

## Section 7-32: Use the reaction concept to derive the mixed-field variational formula for
waveguide phase constants
off wht + of) ds -7 GE XH-ndl
Bie a Ee
2f if Bx A-uds
which corresponds to Eq
 (7-85) if n X E =0 on C. No boundary conditions are
required in the above formula.

## Section 7-33: Consider the variational formula of Prob
 7-32 and a perturbation of waveguide walls, as illustrated by *Fig. 7-5a and b. Use the unperturbed field Ep, Ho as a*
trial field, and show that the formula of Prob. 7-32 reduces to Eq. (7-32).

## Section 7-34: Consider the variational formula of Eq
 (7-85) and a perturbation of matter
in a waveguide, represented by *Fig. 7-5a andc. Use the unperturbed field Eo, Hy as*
a trial field, and show that Eq. (7-85) reduces to Eq. (7-33).

## Section 7-35: Figure 7-26 shows a coaxial stub to parallel-plate waveguide feed system

Assume a &.) so that a reasonable trial current is a uniform current. Show by the
variational method that the impedance seen by the coax is

-2 ykd
Zz ~2ha(i - dz log a)
where y = 1.781.
‘f
eed
matched a matched
load load

-_
| Pe

*Fig. 7-26. Coax to parallel-plate feed.*

## Section 7-36: In Prob
 7-35, remove the restriction on a and assume a trial current on the
stub

I = cos k(a - 2)
Obtain the input impedance seen by the coax by the variational method.

## Section 7-37: Repeat Prob
 7-36 for the second-order variational solution, assuming trial
currents

I* = cos k(a - 2) Ir=1
Note that only one new reaction is needed in addition to those obtained in Probs.
7-35 and 7-36. Specialize the result toa = A/4.

## Section 7-38: Consider the two-dimensional problem of plane-wave scattering by a con
ducting ribbon, shown in the insert of Fig
 7-16, but with the opposite polarization.

PERTURBATIONAL AND VARIATIONAL TECHNIQUES 379
n other words, Hi is parallel to the axis of the ribbon. Use the trial current
Jay cos =
ind show that the variational solution is
32a* 1 |?
t= TR arama
where 7Yepert is given in *Fig. 4-23. Show that as ka- © this answer reduces to*
0.66 times the physical optics solution. Why should we expect the above formula
to be inaccurate for large ka?

## Section 7-39: Consider plane-wave scattering by a wire, represented by Fig
 7-1 5. Atthe
first resonance (L ~ 4/2), the current is
Ie = cos kz
and we know that (see *Fig. 2-24)*
(aa) ~ 73
The imaginary part of (a,a) is zero because the length is adjusted for resonance.
Using Eq. (7-115), show that at resonance the echo area is
A. = 0.860?
This is relatively insensitive to the diameter of the wire.

## Section 7-40: Figure 7-27 represents a resonant length of wire illuminated by a uniform
plane wave at the angle 6, polarized in the r-z plane
 Using the approximations of
Prob. 7-39, show that the back-scattering area is

7 4
le 6 cos |
x 2) -~--A, = 0.86 Sin 0
Again this is relatively insensitive to the diameter of the wire.
Zz | ry’ (to receiver)
lee
re r(to transmitter)
L
*Fig. 7-27. Scattering by a resonant wire (L ~ 4/2).*
7-41, Repeat Prob. 7-40 for the case of differential scattering, showing that the
differential echo area is
2
cos (5 cos ) cos G cos "))
= $)) SS =
A.) = OEE sin 0 sin 0”
where A, is defined by Eq. (7-114) with E* evaluated in the 6’ direction.

380 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 7-42: Consider differential scattering by a magnetic obstacle (Fig
 7-17) and define
Ke = jole - 60) m= jo(u - uo)
Show that, instead of Eq. (7-143), we have
= - {i,a)/D?
Bcho = Faq) - @a)
where (Ga) = [ff (Ei - Je - Hts M2) dr
F(aa) = i] f { [ee MI 2)2 = ee (MP) dr
(a,a) =fff (E*- Jo - He+ Me) dr
In the above formulas, E‘, H' is the incident field, Jt and M®@ are the assumed electric
and magnetic polarization currents on the obstacle, and E*, H* is the field from J*, Ms.

## Section 7-43: Figure 7-28a represents a metal antenna cut from a plane conductor and fed
across the slot ab
 Figure 7-28 represents the aperture formed by the remainder of
the metal plane left after the metal antenna was cut. The aperture antenna, fed
Y 4,
Vi Ls
(a) (0)

*Fig. 7-28. (a) A sheet-metal antenna and (}) its complementary aperture antenna.*
across cd, is said to be complementary to the metal antenna. Let Z,, be the input
impedance of the metal antenna and Y, be the input admittance to the slot antenna,
and show that

Zn _ 1
Y 4
Hint: Consider line integrals of E and H from a to b and c to d, and use duality.

## Section 7-44: Consider a narrow resonant slot of approximate length \/2 in a conducting
screen, Show that the transmission coefficient is
T ~052>
w
where w is the width of the slot
 Hint: Use the result of Prob. 7-43 and assumptions
similar to those of Prob, 7-39,



---

## Chapter 8: Microwave Networks

MICROWAVE NETWORKS

## Section 8-1: Cylindrical Waveguides
 Several Y
special cases of the cylindrical waveguide, _
such as the rectangular and circular guides,
already have been considered. Wenowwish ,
to give a general treatment of cylindrical x
(cross section independent of 2) waveguides hb
consisting of a homogeneous isotropic dielec- . ,
tric bounded by a perfect electric conductor. eitadvio cross mectiqn of a
Figure 8-1 represents the cross section of one al waveguide,
such waveguide. Our formulation of the problem will be similar to that
given by Marcuvitz.’
‘As shown in See. 3-12, general solutions for the field in a homogeneous
region can be constructed from solutions to the Helmholtz equation
vy + hy =0 (8-1)
In cylindrical coordinates, this equation can be partially separated by
taking
¥ = ¥(z,y)Z@) (8-2)
The resultant pair of equations are
ven + kev = 0 (8-3)
wa
W441 Keg = =
ie +k2Z =0 (8-4)
where the separation constants k, and k, are related by
ke tke = (8-5)
and V, is the two-dimensional (transverse to z) del operator
0
=V---u,- 8-l
Vv: Ww (8-6)
1N. Marcuvitz, “ Waveguide Handbook,” MIT Radiation Laboratory Series, vol.
10, sec. 1-2, McGraw-Hill Book Company, Inc., New York, 1951.

382 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Solutions to Eq. (8-4) are of the general form
Z(z) = Ae? 4 Beir (8-7)
which, for k, real, is a superposition of +z and -z traveling waves. The
k, are determined from Eq. (8-5) after the k, (cutoff wave numbers) are
found by solving the boundary-value problem.
For TE modes, we take F = u,y* (superscript e denotes TE) and
determine
= yl aye _ “ze
E = ay + Wop = (u, X Vial)Z (8-8)
The component of E tangential to the waveguide boundary C is
Ey =1- (u. X Vel) = (n+ Val) Zs
where 1 is the unit tangent to C and nis the unit normal to C (see *Fig. 8-1).*
The boundary is perfectly conducting; hence E; = 0on C and
owe
a 0 onC (8-9)
The associated magnetic field is given by
<= ath 1 any aye aye
He = Fon ¥ * E = 2, (u $e + ya + ukep
For more concise notation, we define a transverse field vector as
H, = H -- uz (8-10)
and rewrite the above as
J 2) a2 oa Fe gege
Hy = Fon (VY) 7 H, * eee (8-11)
It is evident from Eqs. (8-8) and (8-11) that lines of & and 3; are everywhere perpendicular to each other.
For TM modes, we take A = u,¥™ (superscript m denotes TM) and,
dual to Eq. (8-8), we determine
H™ = -(u, X Vebn)Z™ (8-12)
Defining the transverse electric iivld vector 2, by Eq. (8-10) with H
replaced by E, we have, dual to Eq. (8-11),
m= 1 m dZm m- ke mam
E; = Ts (vam) pO Sart Z (8-13)
From the second of these equations, it is evident that for Z,to vanish on
C we must meet the boundary condition
w=0 onC (8-14)

MICROWAVE NETWORKS 383
provided k, #0. Note that Eq. (8-14) also satisfies the condition
1-E,=0 on C. When the waveguide cross section is multiply connected, such as in coaxial lines, it is possible to have k, = 0. In this case,
the necessary boundary condition is ¥" = constant on each conductor.
The corresponding field is TEM to z and is a transmission-line mode.

It should be kept in mind that Eq. (8-3) subject to boundary conditions
is an eigenvalue problem, giving rise to a discrete set of modes. These
modes can be suitably ordered, and the various equations of this section
then apply to each mode. It is convenient to introduce mode functions
e(z,y) and h(z,y), mode voltages V(z), and mode currents I(z) according to

Ee =eVe Em = ey"
He=be Hm = bem (8-15)
Comparing Eqs. (8-15) with Eqs. (8-8) and (8-11), we see that we may
choose
e=uxXVeare=h xu, Ve= Ze
he = -Vele = u, X ef r= i d' (8-16)
jon dz
for TE modes, and, comparing Eqs. (8-15) with Eqs. (8-12) and (8-13),
mm _ 1 dZm
e"™ = -Vi¥"™ =h™ Xu, yr= ju de (8-17)
hm = -u, X V: ¥" = u, X e” Im = Z™
for TM modes. Furthermore, we normalize the mode vectors according
to
[f erras = [f Gerrds =1
(8-18)
Lf (em)? ds = lf (hm)? ds = 1
where the integration extends over the guide cross section. Hence, all
amplitude factors are included in the V’s and I’s.

We shall now show that all eigenvalues are real. Consider the two
dimensional divergence theorem
[[¥eAds= pana
and let A = ¥*V,¥. Then,
Vir A = Vit Ve + WAVED = [VEY]? - ke)
and the divergence theorem becomes
ow
2 bp thy? = f pa
I (wav? - kj?) ds = G ¥* al

384 TIME-HARMONIC ELECTROMAGNETIC FIELDS
But the boundary conditions on the eigenfunction ¥ are either Y = 0 or
dv/dn = O0onC. Hence, the right-hand term vanishes and
fi | [vee ds
k= -__-___ (8-19)
yi ii |wlt ds
The eigenvalue k,” is therefore positive real. There is also no loss of
generality if we take all eigenfunctions W to be real. To justify this statement, suppose Y is not real, and let Y = u + jv. Then the Helmholtz
equation is
Vev + kv = Veu + ku + j(Vev + k2v) = 0
which, since k,? is real, represents two Helmholtz equations for the real
functions u and v. The boundary conditions, either
Va=ut+jy=0 on C
ov du . ov
or a an +3 zn (0) onC
are satisfied independently by u and v; so wand v are solutions to the same
boundary-value problem. Hence, u and v for a particular k, can differ
only by a constant, and W is in phase over a guide cross section. We can
take it to be real and include any phase in the V and J functions.
Let us now look at the propagation constant y = jk. For e and uz
real, we have a cutoff wavelength
w= = (8-20)
and a cutoff frequency
ke
So 8-21
f Ta (8-21)
Then, from Eq. (8-5), we have the propagation constant given by
; ‘f.\?
5B = jk 1-() I>fe
7 = de = " (8-22)
nah Ji- (8 f<r
fe
These are, of course, just the relationships that we previously established
for the rectangular and circular waveguides. Figure 2-18 illustrates the
behavior of a and 8 versus f. When the mode is propagating (f > f.),
the concepts of guide wavelength,
Qr r
i we Se a 8-23)
"3" Vi= Ga

MICROWAVE NETWORKS 385
where A is the intrinsic wavelength in the dielectric, and guide phase
velocity,

o Vp

y= 5 =O Som (8-24)

eB VI E/IP
where v, is the intrinsic phase velocity, ar ful
are discussed in Sec. 2-7. y, are useful. These parameters
ene Th, to the mode voltages and currents, we see from their
Hone ions [Eqs. (8-16) and (8-17)] that V and J satisfy Eq. (8-4).

ce, in general they are of the form of Eq. (8-7), or

V(z) = Vte + Ve

Tie) = [te + [oe (8-25)
where superscripts + and - denote positively and negatively traveling
(or attenuating) wave components. Also, from Eqs. (8-4), (8-16), and
(8-17) it is apparent that

vt Y=

FA Zo = aa -Zo (8-26)

where the characteristic impedance Zo is, for TE modes,
on 1
= SS f>fhe
; B =a
ge ie) BO VI ID (8-27)
Y jon _ JOH ff,
a ke V1 - (8/fe)*
and, for TM modes,
2
( £-rJi-() f>fe
y we f
Zo" =- = = (8-28)
jue [2-#Si-(f hes
jue je fe °
Note that these are just the characteristic wave impedances that we previously defined for rectangular and circular waveguides. Figure 4-3
illustrates the behavior of the Zo’s versus frequency. Finally, from Eqs.
(8-4), (8-16), and (8-17), we can show that V and I also satisfy the transmission-line equations
av = --7Zo1
(8-29)
dI
azn -YYoV
where Yo = 1/Zp is the characteristic admittance. Hence, the analogy

386 TIME-HARMONIC ELECTROMAGNETIC FIELDS
{2
(a)
hP/ joe |
=| me es
| |
| : |
| jue |
| I
| |
}-__4z >|
(b)
*Fig. 8-2. Equivalent transmission lines for waveguide modes (series elements labeled*
in ohms, shunt elements in mhos). (a) TE modes, (b) TM modes.
with transmission lines is complete, and all of the techniques for analyzing
transmission lines can be applied to each waveguide mode.!

We may define an equivalent transmission line for each waveguide mode
as one for which y and Zo are the same as those of the waveguide mode.
Such an equivalent circuit may help us to visualize waveguide behavior
by presenting it in terms of the more familiar transmission-line behavior.
For a dissipationless transmission line, we have

IZ IX
a= Ve - NB
y= VZY =jVXB
(see Sec. 2-6). Equating the above %, and y to those of a ‘TE waveguide
mode, we obtain
- - 5 . k?
X = jw, B= joe + - 8-30)
JX =jop JB =j Fa (8-30)
Thus, the transmission line equivalent to a TE mode is as shown in *Fig.
8-2a. Similarly, for a TM mode we obtain*
. : k? . .
jX = jou + Foe JB = jue (8-31)

1 For example, see Wilbur LePage and Samuel Seely, ‘‘General Network Analysis,”

Chaps. 9 and 10, McGraw-Hill Book Company, Inc., New York, 1952.

MICROWAVE NETWORKS 387
The transmission line equivalent to a TM mode is therefore as shown in
*Fig. 8-2b. If the dielectric is lossy, the equivalent transmission will also*
have resistances, obtained by replacing jwe by c + jwe in Eqs. (8-30) and
(8-31). In the light of filter theory, we can recognize the equivalent
transmission lines as high-pass filters.

The power transmitted along the waveguide is, of course, obtained by
integrating the Poynting vector over the guide cross section. Hence, for
the +2 direction,

P,= [[ Ex H*-uds=VI* [fe x h*-u,ds
=vi* ff eds = VI* (8-32)
and the time-average power transmitted is
&. = Re (VI*) (8-33)
Hence, in terms of the mode voltage and current, power is calculated by
the usual circuit-theory formulas.

It is also worthwhile to note that the mode patterns, that is, pictures
of lines of & and at some instant, can be obtained directly from the
W’s. For TE modes, H; is proportional to Ve¥*, and E is perpendicular
to H:. Hence, lines of constant ¥° are also lines of instantaneous & Lines
of instantaneous 3; are everywhere perpendicular to lines of instantaneous & Similarly, for TM modes, lines of constant ¥™ are also lines of
instantaneous 3€, and lines of instantaneous & are everywhere perpendicular to lines of instantaneous 3. It is therefore quite easy to sketch the
mode patterns directly from the eigenfunctions ¥.

Recognizing that the general exposition of cylindrical waveguides has
been quite lengthy, let us summarize the results. Table 8-1 lists the
more important relationships that we have derived. Those equations
common to both TE and TM modes are written centered in the table.
Keep in mind that all of the equations apply to each mode and that many
modes may exist simultaneously in any given waveguide.

Finally, for future reference, let us tabulate the normalized eigenfunctions for the special cases already treated. For the rectangular
waveguide of *Fig. 2-16, we can pick the W’s from Eqs. (4-19) and (4-21)*
and normalize them according to Eq. (8-18). The result is

1 = ”
vat = aaetanee (Ea)eoe(e)
SS oe -34)
_ 2 ab . (mr . (nr
von = Near way sm (@ 2) sm (F 1)
where m,n = 0, 1,2, ...,(m=n = O excepted). Similarly, for the

388 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TaBLe 8-1. Summary or Equations For THE CYLINDRICAL WAVEGUIDE
(TEM Moves nor INcLupED)
TE modes TM modes
Transverse Helmholtz equation Vee + kev =0
: ove
Boundary relations wn =0 on C
mn
e =u X Vee em = -Viy"
be = -vive h™ = -ur X Vie”
Mode vectors | ________.
e=hXu
h=u,Xe
Normalization l/ eds = lf h?ds =1
Propagation constant ly =jke = | 58 = jk Vi- (GN I > fe
| a@=kVI- Uff <f
Characteristic Z and Y Ze = Jou _ a Zope =
7 Yo joe Yor
dV
= + 7Zol = 0
soos ge . dz
Transmission-line equations a
=~ +7¥oV =0
dz
V = Vte-v! + Vreve
M
ode voltage and current, le i (Vier - vers)
Zo
E, = eV
Transverse field H, = bl
ke ki?
Longitudinal field Hye =-- weve Ey = -= yn]™
jon joe
z-directed power P, = VI*

MICROWAVE NETWORKS 389
circular waveguide of *Fig. 5-2, we can pick the W’s from Eqs. (5-23) and*
(5-27) and normalize them. The result is

Vee = En J n(2ipp/@) {sin no
np “T7>’ \2 - n21 Jr)
Nai(z1,)? - m7] J. (zh,) cos nc (8-35)
n= ie _In(Enpp/a) | sin no
™P T Inp I nti(tnp) | cosnd
where n = 0, 1,2,...,andp=1,2,3,.... Thez,, are given by
Table 5-2, and the x}, are given by Table 5-3. Normalized eigenfunctions for the parallel-plate guide are given in Prob. 8-1. Normalized
eigenfunctions for the coaxial and elliptic waveguides are given by
Marcuvitz.*

## Section 8-2: Modal Expansions in Waveguides
 An arbitrary field inside a
section of waveguide can be expanded as a sum over all possible modes.
This concept was used in Sec. 4-4 for the special case of the rectangular
waveguide. We now wish to consider such expansions for cylindrical
waveguides in general. The equations in Sec. 8-1 apply to each mode.
Henceforth, to identify a particular mode, we shall use the subscript 7 to
denote the mode number.

Let us first show that each mode vector e; is orthogonal to all other
mode vectors. For this, we shall use the divergence theorem in two
dimensions,

[[ vedas = Ga-ndl
Green’s first identity in two dimensions,
I[ (Wh Vib + YES) ds = Gy 24 al
an
and Green’s second identity in two dimensions,
ag oy
24 2, = gp _ gg OY
/| (VAs - ove) ds § (v3 os )al
First, consider two TE modes and form the product
ef-e? = hye he = V+ Vey?
Letting y = Wi and c = W;,* in Green’s first identity, we obtain
ff eee ds = - (k;*)? [/ We, ds
Using the same substitution in Green’s second identity, we have
(hee)? - (kes) [f warts ds = 0

1N. Marcuvitz, “‘Waveguide Handbook,’ MIT Radiation Laboratory Series, vol.

10, chap. 2, McGraw-Hill Book Company, Inc., New York, 1951.

390 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Hence, if ke ~ k,;*, the integral must vanish, and the preceding equation
becomes!
[ff ef-efds=0 ix] (8-36)
A dual analysis applies to the TM modes, and we have
fl em-etds=0 ix (8-87)
Finally, we must consider the TE-TM cross products
ef-e" = hye ° h = -(u. x Viv) Vi V,"
If we let A = ¥;"u. X Vi¥# in the divergence theorem, the contour
integral vanishes because of the boundary conditions, and we obtain
| { vil -u, xX Vale ds =0
Comparing the preceding two equations, we see that
f f et-eds=0 foralli,j (8-38)
The orthogonality relationships [Eqs. (8-36) to (8-38)] also are valid for
the e’s replaced by the h’s.
At any cross section along a cylindrical waveguide, the field can be
expressed as a summation over all possible modes:
E, = Verve + enV"
‘ (8-39)
Hy = Y pels + berm
7
Because of the orthogonality of the mode vectors, we can determine the
mode voltages and/or mode currents at any cross section by multiplying
each side of Eqs. (8-39) by an arbitrary mode vector and integrating over
the guide cross section. Noting that the mode vectors are normalized,
we obtain
I E,-e?ds = Vi?
(8-40)
f/ H,-h?ds = I?
where p = eor m. Since there are two independent constants in V and I
for each mode, as shown by Eqs. (8-25) and (8-26), we need two “cross1 A discretespectrum of eigenvaluesisassumed. However, orthogonal sets of mode
functions for degenerate cases can also be found.

MICROWAVE NETWORKS 391
sectional” boundary conditions. These may be (1) matched waveguide
and E; over one cross section, (2) matched waveguide and H; over one
cross section, (3) E, over two cross sections, (4) H; over two cross sections,
and (5) E; over one cross section and H, over another cross section. The
solutions of Sec. 4-9 are examples of case (1). Furthermore, when we
have currents in a waveguide, we can obtain additional cases involving
discontinuities in E, and/or H, over waveguide cross sections. The solutions of Sec. 4-10 are examples of this situation.

It is also of interest to note that, when many modes exist simultaneously in a cylindrical waveguide, each mode propagates energy as if it exists
alone. Hence, the equivalent circuit of a section of waveguide in which
N modes exist is N separate transmission lines of the form of *Fig. 8-2.
To show this power orthogonality, we calculate the z-directed complex*
power

P. = [[ Bx H*-u.ds =[[Qew) x (Yur) was
w -- ;
= ) Vt ff e:-ejds = y Vut (8-41)

i 5
which is a summation of the powers carried by each mode. (We have
used the indices 7 and j to order both TE and TM modes in the above
proof.) The energy stored per unit length in a waveguide is also the
sum of the energies stored in each mode (see Prob. 8-3).

## Section 8-3: The Network Concept
 In Sec. 3-8, we saw that, given N sets
of “circuit”? terminals, the voltages at the terminals were related to the
currents by an impedance matrix. This impedance matrix was shown to
be symmetrical, that is, the usual circuit-theory reciprocity applied if the
medium was isotropic. We shall now show that the same network
formulation applies if, instead of circuit voltages and currents, the modal
voltages and currents of waveguide “ports” are used.

Let *Fig. 8-3 represent a general “microwave network,” thatis, asystem*
for which a closed surface separating the network from the rest of space
can be found such that n X E = 0 on the surface except over one or
more waveguide cross sections. Suppose that only one mode propagates

(2)
Fic, 8-3. A microwave a
network.
(2)
(3)

392 TIME-HARMONIC ELECTROMAGNETIC FIELDS
in each waveguide.!_ Then, assuming we are far enough along each waveguide for higher-order modes to die out, only the dominant mode exists in
eachguide. A knowledge of themode V or J inthe guide is equivalent to
a knowledge of E, or H:, respectively, since the mode vectors depend only
on the geometry. Hence, according to the uniqueness concepts of Sec.
3-3, a knowledge of V (or J) in all guides is sufficient to determine J
(or V) in all guides. Furthermore, the relationship must be linear if the
medium is linear, and an impedance matrix [z] is defined by
Vi Zu 212 213} | Ii
Vo| =| 21 222 203 In (8-42)
Vs Z31 232 233 Ts
where V, and J, are the mode voltage and current in the nth waveguide.
The inverse relationship to Eq. (8-42) defines an admittance matrix [y]
according to
qy yu Ys ysl [Vi
In| =| yor Yer Yes || V2 (8-43)
I; Yar Yar Yas Vs
Equations (8-42) and (8-43) have been written explicitly for the threeport network of *Fig. 8-3 but, of course, can be similarly written for any*
N-port network. Now that we have established these linear sets of
equations, we can use all the usual techniques for solving linear equations.
The electrical engineer knows these techniques by the name of ‘“‘network
theory.”?
It is also of interest to show that, for isotropic media,
tg 2 Y= Ya (8-44)
that is, microwave networks are reciprocal in the same sense as are the
usual lumped-element networks. To prove this, let us apply the Lorentz
reciprocity theorem [Eq. (3-34)]. It states that
op E* x HP «ds = dp E x He -ds
for two fields E*, H* and E?, H? in linear, isotropic media. We visualize
a surface surrounding an N-port microwave network such that E, = 0 on
S except over the waveguide cross sections, where
(Et)n = @nVn = (Ha = Buln
1 If N modes propagate in a single waveguide, then that guide will be represented by
N ports on the equivalent network.
2 For example, see C. D. Montgomery, R. H. Dicke, and E. M. Purcell (eds.),
“Principles of Microwave Circuits,’’ Chap. 4, MIT Radiation Laboratory Series, vol. 8,
McGraw-Hill Book Company, Inc., New York, 1948.

MICROWAVE NETWORKS 393
(The n here refers to the nth waveguide, not the nth mode.) Hence, the
desired surface integrals become
N N
E* xX H’- ds = Vila’ GD en X bh,+ ds = Viel ne?
$ 2 vee g$ 2
and the Lorentz reciprocity theorem reduces to
N N
Y Verte = Y Vata (8-45)
n=l n=1
Toshow that Eq. (8-45) is equivalent to Eqs. (8-44), it is merely necessary
to consider the special cases (1) all 7,° = 0 except J;* and (2) all 7,5 = 0
except J; Then V,* = 2yJ;° and V,* = 2,;J;', and Eq. (8-45) reduces to
zi; = 2. Similarly, taking all V,* = 0 except V.*, and all V,>=0
except Vin Eq. (8-45) establishes yi; = yj:.

## Section 8-4: One-port Networks
 A one-port network is characterized by a
single impedance or admittance element. Visualize a surface enclosing
the network such that the field is zero on the surface except where it
crosses the input guide, as shown in *Fig. 8-4. We then have*

P, = - PE x H*-ds = -VI* fhe x h-ds = VI"
where V and J are the mode voltage and current at the “reference plane,”
that is, at the cross section cut by the surface enclosing the network.
Because of the conservation of complex power [Eq. (1-62)], we have
VI* = Pin = Pa + [20(Wmn - We) (8-46)
where @ is the power dissipated, W,, is the magnetic energy stored, and
W. is the electric energy stored in the network. The input impedance to
the network is therefore
Pin las sa Fay
Z= ie = mg (Pa + j2u(Wn - We)] (8-47)
which is well known for lumped-element network theory. Similarly, the
ds
Fie. 8-4. A one-port network and a surface enclosing it.
s

394 TIME-HARMONIC ELECTROMAGNETIC FIELDS
input admittance is
Y= Phd [G2 - j20(W, - W.)] (8-48)
IVP [VP °
As usual, we define the real and imaginary parts of Z to be resistance and
reactance, and the real and imaginary parts of Y to be conductance and
susceptance, respectively.
Z=R+ 5X Y=G+ jB (8-49)
From Eqs. (8-47) to (8-49) we can draw the following conclusions.
(1) A dissipationless network has R = G = 0. (2) The R and G cannot
be negative in the lossy case. (3) At resonance (X = B = 0) the electric
and magnetic energies are equal. (4) The Z and ¥ satisfy
Z*(-w) = Z(w) Y*(-o) = Y()
and hence R and G are even functions of w and X and B are odd functions
of w.

In the lossless case, VJ* is imaginary, and hence V must be 90° out of
phase with J. We shall now show that everywhere within the network E
is in phase with V and Hisin phase with J. Hence, E is 90° out of phase
with H. Suppose we choose our reference plane such that V is real.
Then n X E is real over the reference cross section of the input guide and
zero over the rest of the enclosing surface (see *Fig. 8-4). These boundary*
conditions, as well as the field equations

VXE= -jopH VX 4A = jocE (8-50)
can be satisfied by assuming E real and H imaginary. This is therefore
a possible solution, and, assuming uniqueness,! it must be the only
solution.

Let us now consider the effect of a change in frequency. The frequency derivatives of Eqs. (8-50) are

0E . .
vxa5= -juH - jon
lw Ow
oH dE (8-51)
VX SS = jE + joe =
x jo 7 + jwe Jo
If we scalarly multiply the first of these by H* and the conjugate of the
1It may be recalled that the uniqueness theorem of Sec. 3-3 required some dissipation for its proof. Hence, our conclusions apply only if we visualize some slight loss.
However, even in the loss-free case, any field having n X E = 0 over the entire boundary would be uncoupled to the input ports, and would have no influence on the external
behavior of the network.

MICROWAVE NETWORKS 395
second of Eqs. (8-50) by dE/dw, and subtract, we obtain
0E . . dH - dE
(x H+) = - 2 of . HY * o%

Vv (2 x ) JulH |? - jo a5 H* + jucE Io
Similarly, if we scalarly multiply the second of Eqs. (8-51) by E* and
the conjugate of the first of Eqs. (8-50) by @H/dw, and subtract, we obtain

oH *)_ aime. 7. OE, pe _ 5 » 0H
v (Sx et) = sa6 + joes E - jonH* + 5
We now subtract the above equation from the preceding one and obtain
dE 0H . .
v(z x H* - 90 * z+) = ~-jul|H|? - jelEl? (8-52)
Finally, this equation is integrated throughout a region of space, and the
divergence theorem applied to the left-hand term.
c (oE oH (= x Ht - 5 x B*) ds =-j If (ul? + EP) dr (8-53)
Note that the right-hand side is proportional to the total electromagnetic
energy contained within the region.

Equation (8-53) is now applied to the one-port network (*Fig. 8-4).*
The field vanishes over the enclosing surface except where it crosses the
input port, and the left-hand side of Eq. (8-53) becomes

OV oy , Ol ve _ _ (7+9V al
(@ +5, exh-ds= Pot V* 55
where V and J are the mode voltage and current at the input reference
plane. Hence, we can write Eq. (8-53) as
av or.
4 OV a Of _ 2 E|?) d:
Eg yeh a5 fff our + deryar
= 23(Wn + We) (8-54)
The input reactance X and susceptance B are given by
. 4 j
IX=7--B
Their frequency derivatives are therefore
dX _ sj aa
do --*T.- dw Ireonstant
‘ 8-55,
aBy J orl eo)
do VV da |V constant

396 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Hence, from Eq. (8-54), it follows that
dX 2 = =
= a (Wn + BW)
dw {II
dB 2 (8-56)
do” nak (Wm + W)
Equations (8-56) state that the slope of the reactance or susceptance for a
loss-free one-port network is always positive. This is known as Foster’s
reactance theorem. From Eqs. (8-47) and (8-48) we also have for lossfree networks
X= it (®, - ®.)
2 (8-57)
B= VP (We - Wn)
Solving Eqs. (8-56) and (8-57) for the energies, we obtain
2 2
wy, = HE (2X _ X) _ IVE (dB, B
4 \dw wo 4 \dw ‘ w (8-58)
w, = UP (eX , X)_ IVP (dB _ B
"4 \dw wo) 4 \dwo wo
Because the energies are positive, it follows that
dX _ xX dB _B
de? o lo? o (8-59)
that is, the slope of the reactance or susceptance is always greater than
the slope of a straight line from the origin to the point of consideration.
Relationships (8-56) to (8-59) were first established in lumped-element
network theory.!

An important consequence of Eqs. (8-56) and (8-57) is that all poles
and zeros of the reactance or susceptance function for a loss-free one-port
network are simple. To prove this, suppose X vanishes at a resonant
frequency wo. The Taylor series about wo is then

X(w) = ai(w - a) + a2(w - wo)? + ++ *
and X’(wo) = a:, which must be positive by Foster’s reactance theorem.
Hence, X has a simple zero at w) and B = 1/X has a simple pole at wo.
Similar reasoning shows that the zeros of B are simple; hence the poles
of X are simple. Furthermore, the poles and zeros for the reactance or
susceptance function of a loss-free one-port network must alternate along

1R. M. Foster, A Reactance Theorem, Bell System Tech. J., vol. 3, pp. 259-267,
April, 1924,

MICROWAVE NETWORKS 397
,
or |
B
o
(a)
ee BE,
(6) (c)
*Fig. 8-5. (a) Typical reactance or susceptance function, (b) a Foster equivalent network of the first type, and (c) a Foster equivalent network of the second type.*
the w axis; else X’(w) will not always be greater than zero. Figure 8-5a
illustrates the general behavior of a reactance or susceptance function.
Equivalent circuits for reactance functions of the Foster type! are illustrated by *Fig. 8-5b and c. Other equivalent circuits of the Cauer type,!*
or of mixed Foster-Cauer type, can be found. An important difference
between microwave networks (distributed elements) and lumped-element
networks is that the former have infinitely many resonances, while the
latter have a finite number of resonances.

The loss-free network is, of course, only an approximation to physical
networks. It is therefore desirable to know how the behavior of networks with small losses differs from the behavior of loss-free networks.
It is known from the usual network theory that a slight amount of dissipation shifts the poles and zeros of the impedance function from the
w axis to points above it. Hence, the reactance (imaginary part of Z)
of aslightly dissipative network would not become infinite for any real w
but would be somewhat like that shown in *Fig. 8-6. Also, since Z(w) is*
an analytic function of w, the resistance (real part of Z) is not independent
of X. A study of the resistance corresponding to the reactance of *Fig.
8-6 reveals that it would behave somewhat like the dashed curve of Fig.*

## Section 8-6: An example of a lossy one-port network is the linear antenna of
Fig
 7-13, for which the power “‘loss”’ is actually radiated power. The
effect of small losses can be shown in the equivalent circuits by adding

1 For example, see M. Van Valkenburg, ‘‘ Network Analysis,” Chap. 12, PrenticeHall, Inc., Englewood Cliffs, N.J., 1955,

398 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Enn fe large resistances in parallel with the
\R \ LC resonators of *Fig. 8-5b and by*
Mo i adding small resistances in series
= ~~ > with the LC resonators of *Fig. 8-5c.*
Ad 8-5. Two-port Networks. The
primary uses of two-port networksin
microwave theory are (1) transmission of energy from one place to
Fis. ss. The effect of small losseson the another and (2) filtering of signals
Impedance of & microwave newwor’s from one another. While much of
the theory can be presented in terms of the impedance matrix [z], defined by
| [i zn] [7]
= 8-60)
[y 221 Z22 | IT, ( )
or in terms of the admittance matrix
ty} = [el (8-61)
it is often more convenient to use other matrices which emphasize the
waveguide character of the ports. The port voltages and currents can be
considered to be the superposition of incident and reflected components.
Hence, for port 1,
Vi=V¥4Vr
: 1 i 8-62
T,=1i+ Ty = z- (Vit - Vr) ( )
o1
and similar equations apply to port 2. Figure 8-7 suggests this travelingwave concept. Mathematically, Eqs. (8-62) are merely a linear transformation from the two quantities Vi, J; to Vi‘, V1’, and it is apparent
that Zo: can be arbitrarily chosen. However, it is usually convenient to
make the natural choice that Zo: is the characteristic impedance of the
waveguide connected to port 1. Another choice, convenient from a
mathematical viewpoint, is to normalize the characteristic impedance by
choosing all Zo’s equal to unity. We shall make the former choice.
From the traveling-wave viewpoint, a possible matrix for describing
h=h4+n> <h=b+kh
+ o_o +
Mi=Vi+ “4 Zo | (1) Network (2) Zoe i =Vit VE
io
Fia. 8-7. Traveling waves for a two-port network.

MICROWAVE NETWORKS 399
vi> fo ~<V
- mee =
*Fig. 8-8. N two-port networks cascaded.*
two-port microwave networks is the transmission matrix [T], defined by
Kor Ti, il [ee
[Ss . 8-63
ESA lee Too} | Vir (8-63)
This matrix is particularly convenient when microwave networks are
cascaded, as illustrated by *Fig. 8-8. The incident and reflected waves*
at the input of network n+ 1 are the reflected and incident waves,
respectively, at the output of network n. Hence, the 7’ matrix of the
over-all network is the product of the 7 matrices of the individual networks, that is,
(T] = [Tw][Ty--a} «+ + [T2][Ta] (8-64)
Another matrix commonly used to describe microwave networks is the
scattering matrix [S] defined by
Vr} _ [Su Si} | Vit
[V2] = Fs Sal LV (8-65)
This matrix is convenient for considerations of impedance matching. It
can also be easily extended to the case of multiport networks. Note
that Si: is the reflection coefficient seen at port 1 when port 2 is matched
and S»2 is the reflection coefficient seen at port 2 when port 1 is matched.
The various matrices defined for a two-port network are, of course,
related to one another. For example, [y] is the inverse of [z], as stated
by Eq. (8-61). The relationship of [S] to [z] is more complicated.
Defining the matrix
_|4o 0
leo] = [3 Zo2
we have [S] = [2 - adlz + 207? (8-65)
Similarly, the transmission matrix is related to the scattering matrix by
Sn - S22Si1 S22
[T] = Bi Sie (8-67)
_ Sn 1
Sn Sh.
The derivation of Eqs. (8-66) and (8-67), along with other relationships
among the various matrices, can be found in vol. 8 of the Radiation

400 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Laboratory Series.!_ For networks constructed of linear isotropic matter,
the reciprocity relationships [Eqs. (8-44)] apply. From Eq. (8-66), it is
evident that reciprocity requires
Sy = Si (8-68)
in the scattering matrix. From Eq. (8-67), it follows that reciprocity
requires
Z
Tula - TrTa = 3" (8-69)
ol

in the transmission matrix. Equations (8-66) and (8-68) also apply to
multiport networks.

There are realizability conditions imposed on the matrices by the conservation of energy theorem. These conditions can be obtained from
the corresponding one-port conditions by terminating the two-port network in various ways to forma one-port. For example, if port 2 is opencircuited (J, = 0), then 2; is the input impedance. Similarly, when
port 1 is open-circuited, z22 is the input impedance looking from port 2.
Hence, by Eq. (8-47) we know

Re (21) > 0 Re (z22) > 0 (8-70)
Similarly, using the y matrix and short circuits on the ports, we obtain
from Eq. (8-48) that
Re (yn) > 0 Re (y22) = 0 (8-71)
More generally, since Eqs. (8-47) and (8-48) must be valid for any
passive termination, we can show that
Re (11) Re (z22) - Re (212) Re (22) 2 0 (8-72)
Re (yi1) Re (y22) - Re (yz) Re (yx) 2 0
Finally, when the network is loss-free, the elements of the impedance and
admittance matrices become imaginary, and restrictions on them can be
obtained from the corresponding restrictions in the one-port case. Such
considerations are particularly useful in the theory of filters.”

Our principal concern for the remainder of this chapter wilt be to
obtain equivalent circuits for microwave networks. For any particular
network, an infinite number of equivalent circuits will exist. One of our
tasks will be to choose a “natural” equivalent circuit, that is, one which
suggests the physical nature of the network. For example, a section of

1C. D. Montgomery, R. H. Dicke, and E. M. Purcell (eds.), “Principles of Microwave Circuits,’ Chap. 4, MIT Radiation Laboratory Series, vol. 8, McGraw-Hill Book
Company, Inc., New York, 1948.

2M. Van Valkenburg, ‘Network Analysis,” Chap. 13, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1955. .

MICROWAVE NETWORKS 401
Al nil jXe <2
+ +
Vi Zor jXb IX’, Zoo V2
Nes 7d le -s|
Fie. 8-9. A typical equivalent circuit for a loss-free two-port microwave network.
waveguide would not be represented by an equivalent tee or pi circuit,
since this would hide the transmission-line character of the guide. For
loss-free networks, we shall use the symbolism of Table 8-2 in equivalent
circuits. It should be emphasized that it is only the sign of a reactance
or susceptance that dictates whether an inductor or capacitor is chosen.
The reactance or susceptance does not, in general, have the simple frequency dependence of a lumped-element inductor or capacitor. Figure
8-9 illustrates a typical equivalent circuit for a loss-free two-port network.
TasLe 82. Sympotism Usep 1n EquivaLent Circuits or Loss-rFREE NETWORKS
Element Symbol Represents
eee IX Positive reactance
Inductor
BL Negative susceptance
ex Negative reactance
Capacitor |_|
4238 Positive susceptance
nil
Ideal transformer 3 f Change in impedance level
---Z
Transmission line -- Waveguide section

402 TIME-HARMONIC ELECTROMAGNETIC FIELDS
I. T T
ne 2
' Zo Zo
ed ° O
(a) (b)
Fra. 8-10. (a) Asymmetrical obstacle in a cylindrical waveguide, and (b) an equivalent
circuit.

In the case of dissipative networks, resistors in series with X or in
parallel with B can be used to represent the losses. Similarly, the characteristic impedances and propagation constants of the equivalent transmission lines can be assumed complex to account.for losses. Most of the
networks used in microwave practice are only slightly lossy, and the
small losses introduce only second-order corrections to the reactances
calculated on a loss-free basis.

## Section 8-6: Obstacles in Waveguides
 An object in a cylindrical waveguide
can be represented as a two-port network. Figure 8-10a shows an
obstacle, symmetric about the cross section T, in a waveguide. Figure
8-10b shows a possible equivalent circuit. In the more general case of an
unsymmetrical object, the two Z,’s would probably be different from each
other, and it might even be desirable to choose two reference planes 7.
In the loss-free case, the Z’s will all be 7X’s.

Before considering the obstacle problem, let us consider ‘‘dominantmode sources” in cylindrical waveguides. Figure 8-11 shows the electric
source J, in a waveguide terminated at z = 0 by a magnetic conductor
and matched asz > -«. The method of treating this problem is that
used in Sec. 3-1 for rectangular guides, as, for example, *Fig. 3-2. Let*
superscripts (1) denote the region -1 < z <0, and superscripts (2)
denote the region z < -l. Then in region 1 there will be an incident
wave plus a reflected wave such that H: = 0 atz = 0. Hence,

E,Y = A(e- + ei)e = 2A cos (62) e
A, ; 2A. (8-73)
HLM = 4 (eo: - gife)yy = 24
t! Zo (e eibr) PA sin (6z) h
where e and h are the mode vectors, 8 is the phase constant, and Zo is the
characteristic impedance, all of the dominant mode (see Table 8-1). In
region (2) there will be only a wave in the -z direction; hence
E: = Beibte
-B
(2) - = eipe
H: Z, ° h
Continuity of E; at z = -l requires that
2A cos Bl = Be-#t

MICROWAVE NETWORKS 403
which determines B in terms of A. The boundary condition on H at
z= -lis

u, X {H™ _ H®] = J.
which leads to j.=- 2A eb e

Zo
A quantity of interest to us is the self-reaction of the current sheet
2A? ;
(s,s) = E-J.ds = - z (1 + 8) (8-74)
0
We shall use dominant-mode current sheets as mathematical “ waveguide
probes”’ to determine the equivalent circuit impedances.

Now return to the original problem, *Fig. 8-10a._ We define even excitation of the waveguide as the case of equal incident waves from bothz < 0*
and z > 0, phased so that E; is maximum and H; is zeroatz = 0. By
symmetry arguments, the H: scattered by the obstacle will also be zero in
the z = 0 cross section; so a magnetic conductor can be placed over the
z = 0 plane without changing the field. This divides the problem into
two isolated parts, one of which is shown in *Fig. 8-12a. The excitation is*
provided by the dominant-mode source J,, which we have just analyzed.
The equivalent circuit of *Fig. 8-12a is shown in Fig. 8-12b. (The magnetic conductor is equivalent to an open circuit, and the J, is equivalent*
to a shunt current source J.)

We now further restrict the problem to the loss-free case. Then the
dominant mode will be a pure standing wave in the region -1 < z < 0 of
*Fig. 8-12a. If J, is located where E; = 0, then by the usual transmissionline formulas*

Z_%&+2Z,_ _.
wes Za = -j tan pl (8-75)
Yor the source of arbitrary J, the total reaction on J, is
Reaction = [[ B-Seas = [/ (E' + E*)- J, ds
G9) + G9)
where E* is the field of J, alone, and E* is the field of the current on the
<<- Matched guide | Magnetic oe
->
ae ae F 7
*Fig. 811. A domiuant-mode source in a waveguide terminated by a magnetic*
conductor.

404 TIME-HARMONIC ELECTROMAGNETIC FIELDS

Tt T QT T

fa]
Matched Mag.
~< Js cond. ) T Zo
guide
>_> © °
__;__| Z |__|
(a) (b)
¥:

TQ T 2 a
ee Os
Matched Elect.
<= cond. Zo
guide Ms

a ° 9

._1 4] z 
(©) (d)
*Fig. 8-12. Even excitation of Fig. 8-10 is represented by (a), which has an equivalent*
network (b). Odd excitation of *Fig. 8-10a is represented by (c), which has an equivalent network (d).*
obstacle alone, both radiating in the waveguide terminated by the magnetic conductor at z = 0. If l is adjusted to a cross section for which
E, = 0, then the reaction vanishes and the above equation becomes
2A? .
(es) = - (9) = 7A + orm
0
where the last equality is Eq. (8-74). Taking A as real, we have
2
Re (c,s) = 2M (1 + cos 261)
0
2
Im (c,s) = eas (sin 261)
Zo
and, using the identity
tan® = sin a
2 1+ cosa
Eq. (8-75) becomes
Xp + 2X, _ Im (c,s)
Fe oo Re les) (8-76)
We have replaced the Z, and Z, by 7X. and jX» because only the loss-free
case is being considered. By reciprocity,
(€,8) = (se) =f Br dye (8-77)
obst
where E* is the incident field, given by Eq. (8-73), and J‘ is the current on

MICROWAVE NETWORKS 405
the obstacle.! Note that the problem is now identical to the echo problems of Secs. 7-10 and 7-11, except that all currents radiate in the environment of the waveguide plus the magnetic conductor.

For the case of a perfectly conducting object, the obstacle current is a
surface current J,°, and n X E = 0 on its boundary. Hence,
n X E* = -n X E*
and (50) = -(c0) = - ff BF-Jueds (8-78)
where (c,c) represents the self-reaction of the currents induced on the
obstacle. By Eqs. (8-76) to (8-78), we therefore have

Xo +2Xq _ Im (c,c)

Te 7 Rees) em
Our problem is now one of finding the self-reaction of the currents induced
by the incident field of Eq. (8-73) with A real.

For a stationary formula, we assume currents J,* on the obstacle and
calculate (a,a) subject to the constraints
(a,a) = (ca) = (a,c)
(see Sec. 7-7). The last equality is met by reciprocity, and, since
n X E* = -n x E‘ on the obstacle surface,
(ca) = -(a)
Hence, our stationary formula for (c,c) is
ww (8a)?
(c,c) = (a,a) (8-80)
This, coupled with Eq. (8-79), represents the variational solution to the
problem. If the trial current is taken as real, then (s,a) is real because
E* is real. Equation (8-80) can then be written as
~ | 48a) *
Cox) = [22% F (a)
and Eq. (8-79) becomes
X,+ 2X, _ Im (a,a)
Zo ™~ Re (a,a) (8-81)
This formula applies only when J,? is real, which is usually the case. The
change of sign in going from Eq. (8-79) to Eq. (8-81) can be explained by
noting that J,° is not real for the given E*, but is usually at some constant
phase.
1 The obstacle may be a conductor, a nonmagnetic dielectric, or a magnetic dielectric (u # 4). In the latter case the term -JH*+dM* must be added to the righthand side of Eq. (8-77).

406 TIME-HARMONIC ELECTROMAGNETIC FIELDS
We define odd excitation of the waveguide (*Fig. 8-10a) as the case of*
equal incident waves from both z < 0 and z > 0, phased so that E: = 0
and H; is maximum at z = 0. By symmetry, the E; scattered by the
obstacle must also be zero in the z = 0 cross section, and so an electric
conductor can be placed over the z = 0 plane without changing the field.
This divides the problem into two isolated parts, one of which is shown in
*Fig. 8-12c. The excitation is provided by a dominant-mode magnetic*
source M,, which, together with the electric conductor covering the
z = 0 plane, is dual to *Fig. 8-11. The equivalent circuit of Fig. 8-12c is*
shown in *Fig. 8-12d. (The electric conductor at z = 0 is equivalent toa*
short circuit, and the M, is equivalent to a series voltage source V.)
The analysis of *Fig. 8-12c is dual to that used for Fig. 8-12a. Hence,*
dual to Eqs. (8-73), in the region -1 < z < 0 we have a source field
He = 2C cos (6z) h
: 'e 2C .. (8-82)
Es = Vo sin (Bz) e
where Yo = 1/Z is the characteristic admittance of the dominant mode.
Dual to Eq. (8-79) we have
J 1 _ Ime 8-83
YoZs YoXs, - Re (c,c) ( )
where (c,c) is the self-reaction of the obstacle currents radiating in the
presence of an electric conductor over the z = 0 cross section (see *Fig.
8-12c). Finally, for a variational solution, currents J,* are assumed on*
the obstacle, and their self-reaction (a,a) is calculated. If the J,* is real,
then dual to Eq. (8-81) we have
1 Im (a,a)
SF = 5S 8-84
YoXp Re (a,a) ( )
where (a,a) is calculated with an electric conductor over the z = 0 plane.

## Section 8-7: Posts in Waveguides
 Some variational solutions for circular
posts in rectangular waveguides can be carried out relatively simply.
Figure 8-13 illustrates three classes of obstacles: (1) those cylindrical to y,
hy hy hy
| ws Le
Hoe Lk LG x
(2) (6) (c)
*Fig. 8-13. Posts in a rectangular waveguide, (a) cylindrical to y, (b) cylindrical to 2,*
and (c) otherwise.

MICROWAVE NETWORKS 407
| te |
| |
| \ | |
| | | |
|
“5 ! Sh =o A yy | Ad
I | a | |
| | | |
| | | |
| | | |
.
*Fig. 8-14. Image system for the circular post in a rectangular waveguide.*
(2) those cylindrical to z, and (3) all other cases. [The cylinders are not
necessarily circular, and case (1) is different from case (2) only because of
the excitation.] It is assumed that the incident wave in each case is the
dominant mode with E parallel to y and H; parallel to z. Then the field
of case (1) will be TM to y, expressible in terms of a single wave function
Ay = (see Sec. 4-4). The field of case (2) will be TE to z, expressible in
terms of a single wave function PF: = y. Type (3) problems require two
scalar wave functions to express the field (see Sec. 3-12).

We shall consider only the centered circular post, as shown in the insert
of *Fig. 8-15. For even excitation (Fig. 8-12a), assume a constant current*
on the post

I
Ie = WG (8-85)
The field produced by J.* in the waveguide closed by the magnetic conductor will be the same as the free-space field from the image system of
*Fig. 8-14. Hence, we can write*
Ey? = Eyrot + E,jmasce
where the first term is the free-space field of J,* and the second term is
the free-space field from all its images. The self-reaction of J,* in the
waveguide with magnetic conductor is one-half that for the complete
post in a waveguide; hence
1 fe 2nd
(aa)=5 | dy | 546 (J,E,)
2 Jo 0 2
al [
= - (E,pet + E,jm*ee*) dc (8-86)
4m Jo

408 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Now the “‘post”’ term is independent of c since the J,* is independent of
c. The “image”’ term is a source-free field in the vicinity of the post and
can therefore be expressed as
Bye =) Anta(ko)err?
(see Sec. 5-8). Thus,
as d d :
Eyjmee'dd = 2wAgo( ks) = 2tJo( ks ) By
° 2 2 jp =0
and Eq. (8-86) reduces to
al d :
(aa) = [ zr |. ate (« 5) Bios |_.| (8-87)
The field of a single cylinder of constant current was calculated in Sec. 5-6.
Abstracting from Eq. (5-92), we have
d d
By = - 7 kde (' A) Hoke) p25
The field from each image is also of the above form, with p replaced by the
distance to the image. Hence, Eq. (8-87) becomes
d d
(a,a) = K | Ho kg + Jo ks 2 (-1)"Ho(nkb) | (8-88)
n=1
where K = - 2 kalJo( ) ,
is an unimportant constant. Equation (8-88) is an exact evaluation of
(a,a) for the assumed current of Eq. (8-85).

Unfortunately, the Hankel function summation in Eq. (8-88) converges
slowly and is not convenient for computation. However, we shall now
show that it can be transformed to

. 2 1 .
-1)"Ho (nkb) = = | ------- - 5
> Hd (aks) = 2) ees Fi

+i(5 log 20 - 1 + s)| (8-89)

2 r
where y = 1.781 and S is the rapidly convergent summation
b . 1 1
s(2)= re 8-90
(3) » [va = (26/9)? ‘| ee

MICROWAVE NETWORKS 409
The free-space field of a filament of current is given by Eq. (5-84).
Hence, the left-hand side of Eq. (8-89) is the Ey from all images of the
filament
-2
I= ke
across the center of the original waveguide. (This problem is *Fig. 8-14
with J.* replaced by the above I.) Then, by the method of Sec. 4-10,*
we can find the total field in the z = 0 cross section due to the above I.
It is
2 sin (1z/b) “MO sin (nx /2) sin |
EB, = = | + ee 8-91
. © Presse =i? Jn? - (2b/d)? (6-91)
n=2
where only the first term isreal because itisassumed that 1 < (2b/r) < 2.
For large n, the above summation has terms equal to those of
1. (nr\ .. 7 cos nb
Sialaber)- Se
n=l n=1,3,5,.-_ (e®)n (3 1+ e\ _ (3 jsin 6
= Re » a Re 3 08 es a= Re 5 108 T= cos § sat
n=1,3,,...
= Re(110c -4 -_i $
= Re (3 log tan im) =-3 log tan 5
Hence, letting 7 = (b/2) + p in Eq. (8-91) and 5 = ap/b in the above
identity, we can add and subtract the latter from the former and obtain
2 1 fi 2b
Ey“! -> = | -----_- siog@ -148
S| ear t (2-1 +)
The free-space EB, from the same filament J is
1 2
= (2) = =Ey = ¥Ho" (ke) =e + jz log re,
When this is subtracted from the total Ey, and p set equal to zero, we
have the right-hand side of Eq. (8-89).
Returning now to the self-reaction, we substitute Eq. (8-89) into Eq.
(8-88) and obtain
2 X
Re (aa) = C 5S cw
(axa) V (bn)? - 1 b (8-92)
_ _ ®No(kd/2) 2yd _
Im (a,a) c| Do(kd/2) + log > 2+ 28

410 TIME-HARMONIC ELECTROMAGNETIC FIELDS
where C is the unimportant constant,
= - Th yo (1,4
Cc tq Po (« 3
Equation (8-92) is still exact for the current assumed in Eq. (8-85).
However, because of the crudeness of our initial trial current, we can
expect our result to be valid only for small d/A. Hence, we use smallargument formulas for the Bessel functions and obtain
4b
Im (a,a) = C log -2428 (8-93)
Now, substituting from Eqs. (8-92) and (8-93) into Eq. (8-81), we have
Xo +2X__ bd 4b b
ay, [085 2+ 28 (:)| (8-94)
where S is given by Eq. (8-90).
For odd excitation (*Fig. 8-12c), we assume a current*
jJ.c = u,sin > (8-95)
induced on the post. The appropriate variational formula is Eq. (8-84),
12 7
IN TT PT | ts wi
vot NL | TT t (==
: F
NN Xadg/Zob 4
AY - Top view End view
0.8 a ( r
= X CS < > ae 5X
3 NY) Zo x, 2
3 06 XN °
SL] perso yet --1_
quivalent circur
,aRRE CANN econo
| PT | Per TSS pay
oot | | | | J tT | CASS
LE ty [vec | SSS
[| L[ | +++
QO 0.05 0.10 0.15 0.20
d/b
Fia. 8-15. The centered circular inductive post in a rectangular waveguide. (After
Marcuvitz.)

MICROWAVE NETWORKS 411
the exact evaluation of which follows steps T
similar to those used to derive Eq. (8-94).
The result is d
Xs b [rad\? |
G8 y (=) (8-96)_§_ 7.
*Fig. 8-16. A small obstacle*
Figure 8-15 shows X_ and X; as calculated in a waveguide.
from a second-order_ variational solution.?
Our solution [Eqs. (8-94) and (8-96)] is accurate for small d/b, the error
being of the order of 10 per cent for d/b = 0.15. Formulas and calculations for off-centered posts are also available.! A solution for the circular
capacitive post (*Fig. 8-130) is given in Prob. 8-12.*

## Section 8-8: Small Obstacles in Waveguides
 Figure 8-16 represents a small
obstacle in a waveguide of arbitrary cross section. If the obstacle is
symmetrical about a transverse plane, the equivalent circuit is as shown
in *Fig. 8-10b. If the obstacle is loss-free, the Z’s are j7X’s. The formulation of the problem for a conducting obstacle is that of Sec. 8-6. An*
approximate evaluation of the reactions, made possible because the
obstacles are small and not too near the guide walls, will now be discussed.

Consider even excitation of the guide (*Fig. 8-12a). The effect of a*
small obstacle is small; hence Z, is small and Z, is large. Equation (8-81)
is then

X_. _ 1Im(a,a) =
Z ~ 2 Re (a,a) (8-97)
where (a,a) is the self-reaction of the assumed currents in the waveguide.

Let us first make some qualitative observations. In a rectangular
waveguide, the reaction (a,a) is the free-space self-reaction of the obstacle
plus the mutual reaction with all itsimages. For real current, the imaginary part of the free-space self-reaction becomes extremely large as the
obstacle becomes small. Hence, for sufficiently small obstacles, we can let

Im (a,a) = Im (4,0)trce space (8-98)
In contrast to this, the real part of the free-space reaction approaches a
constant, independent of the size of the obstacle, as the obstacle becomes
small. The mutual reaction between the obstacle and its images therefore cannot be neglected. However, because the real part of the reaction
is independent of the size and shape of the obstacle, we can calculate the
dipole moment JI of the free-space obstacle and let
Re (a,a) ~ Re (JI, 11) (8-99)

1 N. Marcuvitz, “‘ Waveguide Handbook,’’ MIT Radiation Laboratory Series, vol. 10,

pp. 257-263, McGraw-Hill Book Company, Inc., New York, 1951.

412 TIME-HARMONIC ELECTROMAGNETIC FIELDS
x} xf- b-+
nm a
*° |
Zz
a or ee x
Side view End view
*Fig. 8-17. A small conducting sphere centered in a rectangular waveguide.*

The right-hand term represents the self-reaction of a current element JJ in
the waveguide.

As an example, consider the small sphere of radius c in the center of a
rectangular waveguide, as shown in *Fig. 8-17. As our trial current,*
assume J,* is that which produces the dipole field external to the sphere.
This current, even though we shall not need it explicitly, is approximately

ll.
jJ.0 = -ue Jno? 50 0 (8-100)
where @ is measured from the z direction. Because the above current
produces the same field as an z-directed element of moment JI, the
imaginary part of the free-space self-reaction is the imaginary part of
Eq. (2-115) evaluated atr = c. Hence,
Qn (II\? {13
Im (0A)ree me = -9 (4) (Fe)
Equation (8-98) is therefore
_ nrc)?
Im (a,a) ~ 129?ga (8-101)
For the real part of (a,a), we can use the analysis of Sec. 4-10 for a
current sheet
a b
s.=1s(2-3)s(¥-2)
Because the current is real, we can set Re (J1,Jl) = -Re (P) of Eq. (4-87)
and obtain
Re (It,Il) = - 2 2Ju)?
where, from Eq. (4-86),
2
Ju = a Il
Hence, Eq. (8-99) becomes
- - Zorg - _ Mo yzy2
Re (a,a) ~ x (Il)? = abn (Il) (8-102)

MICROWAVE NETWORKS 413

Substituting from Eqs. (8-101) and (8-102) into Eq. (8-97), we have

X. dab

Sew ~ 8-103

Zo 24m?h,c* ( )
This is the small-obstacle approximation for a centered sphere in a rectangular waveguide. Our free-space reaction is the Rayleigh approximation [Eq. (6-106)], which is valid for c/\ < 0.1. Hence, we should
expect Eq. (8-103) to be accurate when c/A < 0.1 and c<a/2.

Now consider odd excitation of the guide (*Fig. 8-12c). The evaluation*
of X, can then be made according to Eq. (8-84). Taking the current as
real, we evaluate the imaginary part of (a,a) according to the free-space
approximation [Eq. (8-98)]. However, because of the symmetry of the
obstacle and of the excitation, there can be no net electric dipole moment,
and Eq. (8-99) does not apply. There will be a magnetic moment Kl
(unless the obstacle has zero axial thickness), which can be calculated
from the assumed current. Then, analogous to Eq. (8-99), we use the
approximation

Re (a,a) ~ Re (K1,Kl) (8-104)
where the right-hand term represents the self reaction of a magnetic
current element KI in the waveguide.

Return now to the specific problem of a conducting sphere in a rectangular guide (*Fig. 8-17). It is evident from symmetry that, for odd*
excitation, the resultant magnetic dipole will be y-directed. For the
trial current, assume that which produces the magnetic dipole field
external tothesphere. The free-space self-reaction of this current isthen
just the dual of that for the electric dipole, given by Eq. (8-101). Hence,

MKY?
Im (a,a) = Im (4,)trce space = glare? (8-105)
For the real part of (a,a), we evaluate the right-hand side of Eq. (8-104)
by methods dual to those used to establish Eq. (8-102). For the centered
y-directed magnetic current element in the rectangular guide, we obtain
~ _ Yo 2 2
Re (a,a) ~ Re (KLKl) = 2 (Kl)? = aa, (Kl)
Substituting from this and from Eq. (8-105) into Eq. (8-84), we have
Zo _ _ abd, _
X, ~~ Wats (8-106)
The accuracy of this formula is at least as good as that of Eq. (8-103).
The evaluation of other small-obstacle equivalent circuits can be found in
the literature.?

1A. A. Oliner, Equivalent Circuits for Small Symmetrical Longitudinal Apertures

and Obstacles, JRE Trans. vol. MTT-8, no. 1, January, 1960.

414 TIME-HARMONIC ELECTROMAGNETIC FIELDS
T T T
Yo Yo
eee oS cos 2
_ ° °
(a) ()
*Fig. 8-18. (a) A diaphragm in a waveguide, and (6) an equivalent circuit.*

## Section 8-9: Diaphragms in Waveguides
 Figure 8-18a represents a cylindrical waveguide of arbitrary cross section with an infinitely thin electric
conductor covering part of the z = 0 plane. This conductor is called a
diaphragm, and the opening in it is called a window. The diaphragm plus
the window cover the entire z = 0 cross section. The exact equivalent
circuit is just a shunt element, as shown in *Fig. 8-18b. Depending upon*
the shape of the diaphragm or window, the susceptance may be positive
(capacitive), negative (inductive), or change from positive to negative as
the frequency is varied (resonant when B = 0).

To evaluate the shunt susceptance, we can use the method of Sec. 8-7.
Taking the case of even excitation (*Fig. 8-12a), the diaphragm problem*
reduces to *Fig. 8-19a. The equivalent circuit is shown in Fig. 8-190.*
The appropriate stationary formula is Eq. (8-81), which reduces to

2Yo Im (a,a) “B ~~ Re (a,ay (8-107)
where (a,a) is the self-reaction of the assumed current J,° on the diaDiaphragm Ms
lag.
ad Matched ) cond. C4) I B/2 |
>
ll ; _.] 2 |__ ; --_4]
(a) (b)
o
m- Matshed nf Mag. cond.
Elect. cond.}_.
_-_ ; +] 2 _-(ce) (a)
*Fig. 8-19. Symmetrical excitation of Fig. 8-10a is represented by (a), which has an*
equivalent circuit (b). Symmetrical excitation of *Fig. 8-10a is also represented by*
(c), which has an equivalent circuit (d).

MICROWAVE NETWORKS 415
phragm. We can think of *Fig. 8-19a as being constructed by placing*
pieces of electric conductor on top of a magnetic conductor.

Because the diaphragm problem is self-dual, we have the alternative
representation of *Fig. 8-19c. This can be viewed as a construction of*
the window by placing pieces of magnetic conductor on top of an electric
conductor. The source has been changed to a magnetic current sheet,
instead of the electric current sheet of *Fig. 8-19a, so that complete duality*
is preserved. Then, dual to Eq. (8-107), we have

B _ Im (4,4)m

2¥, Re (a,a)m (8-108)
where the subscripts m are added to emphasize that (a,a)m is the self
reaction of assumed magnetic currents M,* on the window, that is,
(aan =~ ff He- Meds (8-109)
Because the M.,° is related to the tangential E in the window of the

original problem according to

Me =u.xE (8-110)
Eq. (8-108) is known as an aperture-field formulation of the problem.
This is in contrast to Eq. (8-107) which is an obstacle-current formulation.
Note that Eq. (8-108) can also be viewed as a specialization of Eq. (8-84).

To illustrate the theory, consider a capacitive diaphragm in a rectangular waveguide (*Fig. 8-20). (Note that it must be capacitive, because it is*
a special case of *Fig. 8-13b.) Take the E-field formula [Eq. (8-108)] and*
note that

(a,0)m = -ff He. M,-ds = -ffe x H-u,ds
=(- [[ =x H*-u,ds)* = P*
because E is real. Hence, the problem is the same as those treated in
T yt _ T T
Z
] | EZ |
iil | pa ay
ial ds
Side view End view
(a) (6)
*Fig. 8-20. (a) Capacitive diaphragm, and (b) an equivalent circuit.*

416 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Sec. 4-9. In particular, if we assume
. 7zL
By ={sn oye (8-111)
eno 0 y>ec
in the window, we then have precisely the problem of *Fig. 4-17. Hence,*
from Eq. (4-77), we have
(a0) = Pt = (VY. = IVI (Yo + iB)
where Y, is the aperture admittance. Finally, substituting from the
above into Eq. (8-108), we obtain
. B _ 40B, _ 8b /d,Ba
ace ated C7 eu)
where the quantity in parentheses is plotted in *Fig. 4-17.

A more general treatment of the problem proceeds as follows. We*
know from the discussion of *Fig. 8-13 that the field must be TE to z, and*
so the most general form for the tangential field in the window is

cd
Be| _ \" sin y<e (8-113)
z=0 0 y>ec
Then, by the methods of Sec. 4-9, we calculate
b 1
(4,0)m = P* = > Y = (Yo)an| Bal?
a=0”
where, by Eq. (4-73), the Fourier coefficients E1, are
=@ /[* nry
Bn = & [se cos FY dy
and the characteristic admittances of the TEz;, modes are
j2bY,
Yo), = -- 2 8-114
(Yo)x Vat = Gy ( )
The Yo and A, pertain to the dominant mode, which is the only mode
having real characteristic impedance, because of our assumption that only
the dominant mode propagates. Hence, Eq. (8-108) becomes
[¥olin| Zan|?
ad
2¥o° 2 ol Lil?

MICROWAVE NETWORKS 417
which, upon substitution from the preceding equations, becomes
y a [ [1 cos “4 av}
Vat = Gir) | Jo D
B_ 8baai
| a a a (8-115)
0 ry e
[ i Sy) av
0
Equation (8-112) represents the special case f(y) = 1. Better approximations to B/Y can be obtained by using a better choice for f(y), or by
applying the Ritz procedure.

The stationary formula in terms of obstacle current [Eq. (8-107)] is
specialized to the capacitive diaphragm as follows. The field is TE to z,
given by Eqs. (4-32) with

y= sin = » An COs a ern?
n=0
_ T\? mm? ae
where Y. = 4 () + (7) k
The current on a diaphragm backed by a magnetic conductor (*Fig. 8-19a)*
is then
sat
J,= H, = JT cos nA, sin 27¥
2-0 0 ©- QDwe a b
n=0
2 2
Jy = -1,| a (fay - I e sin™™ A, cos “24
2=0 jon a b
n=0
Hence, the current has both z and y components, but the A, can be determined from the y component alone. The x component then adjusts
itself to make the field TE to z. If we assume a current
. WL
Jv" = g(y) sin (8-116)
and define Fourier coefficients
b
Jn = 2 | gly) cos 4 dy (8-117)
b J. b
= Se 7, = Be
then A, = Ga? = Bile 7 Ja

418 TIME-HARMONIC ELECTROMAGNETIC FIELDS
5 -,;- Also, at z = 0, the tangential electric
ye intensity is given by E, = 0, and
4 2 .
ge nie |(o~ E, = - sin yun con 22
ape = (cy n=0
° & e==4== 55 =a Hence, in the same manner as Eq.
= seep eT (4-74) was derived, we find the self=? reaction of J,° as
b
1 (aa) = © » + (Zonda?
2 fn
n=0
where the characteristic impedances
0 0.1 0.2 03 04 (Zo)n are the reciprocals of Eqs.
b/s (8-114). Because only the dominant
*Fig. 8-21. The capacitive diaphragm mode propagates, only the n =0*
with c= 2. @ eet solution, ® term of the summation is real, and
crude aperture-fel variational solu- _ vA
tion, (c) crude obstacle-current varia- Eq. 8 107) reduces to
tional solution, and (d) crude quasi- ad
static solution. ») (Zo) nd n®
2¥o ney
B WZ odo?
Substituting for J, from Eq. (8-117) and for (Zo)n = 1/(Yo)in from Eq.
(8-114), we finally have
b 2 b 2
dy ver (RY [foo copa
Yo _ Ayn=1 ° ‘
ele Ot Red See 8-118
B 8b a 2 ( )
, 90) dy
This is the stationary formula in terms of obstacle current for the capacitive diaphragm of *Fig. 8-20.

Figure 8-21 compares various solutions to the capacitive diaphragm*
problem for the case of a diaphragm covering half the guide cross section.
Curve (a) is called the exact solution because the estimated error is less
than the accuracy of the graph. This solution is obtained by finding a
quasi-static field and then using it in the variational formula, Eq.
(8-115).!. Curve (0) is the crude aperture-field variational solution, Eq.
(8-112), which is also Eq. (8-115) with f(y) = 1. Curve (c) is a crude

2. N. Marcuvitz, ‘‘ Waveguide Handbook,” MIT Radiation Laboratory Series, vol. 10,
secs. 3-5 and 5-1, McGraw-Hill Book Company, Inc., New York, 1951.

MICROWAVE NETWORKS 419
obstacle-current variational solution, Eq. (8-118), with
= sn TY AO

g(y) = sin Xb =o) (8-119)
(If the case g = 1 is tried, the solution diverges, because the boundary
condition that the current vanishes at y = c is violated.) Curve (d) is
a first-order quasi-static solution to the problem!

a ~ x lo ese oh (8-120
In practice, waveguides are usually operated with b/A, < 0.25; so this
last solution is a good approximation for most purposes.

Note that the aperture-field variational solution, curve (b), is above the
true solution, and the obstacle-current variational solution, curve (c), is
below the true solution. That this is so for any trial functions f(y) and
g(y) follows from the fact that Eqs. (8-115) and (8-118) are positive
definite and hence are an absolute minimum for the true fields. Since
Eq. (8-115) gives B/Yo and Eq. (8-118) gives Yo/B, the former yields
upper bounds and the latter yields lower bounds to the true B/Yo. The
existence of variational formulas for both upper and lower bounds is not
very common and is a consequence of the self-duality of the problem plus
the positive-definite nature of the resulting variational formulas.

Our crude variational solutions give an error of the order of 20 per cent,
butit is remarkable that they areas close as that. A quasi-static solution
to the problem is

= 008 (ry 25) SY) = Tan Gee/2by - sin® (ay/3B) (8-121)
which actually has a singularity at y = c. Hence, our approximation
f(y) = 1 was an exceedingly crude choice, yet it led to usable results.
Our approximation to g(y) [Eq. (8-119)] is equally crude. If we were to
use Eq. (8-121) in Eq. (8-115), the result would be very close to the true
solution.

It is interesting to note that the three diaphragms shown in *Fig. 8-22
all have the same equivalent circuits. This is evident, because the image*
systems for all three cases are identical.

The treatment of the inductive diaphragm (*Fig. 8-23) is similar to that*
of the capacitivediaphragm. The general variational formulas for upper
and lower bounds are given in Probs. 8-14 and 8-15. For a crude aperture-field solution, we san assume Eq. (4-75) for H,* in the aperture.
1W. R. Smythe, “Static and Dynamic Electricity,” 2d ed., Sec. 15-10, McGrawHill Book Company, Inc., New York, 1950.

420 TIME-HARMONIC ELECTROMAGNETIC FIELDS
i commaaemars i a 2
=e
ZY
| (LA, ibe |”;
c b c
iL de IE
(a) (0) (c)
*Fig. 8-22. These three diaphragms give rise to the same shunt capacitance.*
T x A b-+
'Z
Wl r r
al
‘ Yo JB Yo
bd
Eee _
Side view End view
(a) (6)
*Fig. 8-23. (a) Inductive diaphragm, and (6) an equivalent circuit.*
This procedure gives
B__ Mw [ral - (c/a)? |? (nb _
Yo ao [ c sin (e/a) IN Ba (8-122)
where B, is the aperture susceptance plotted in *Fig. 4-19. The values of*
-B/Y> calculated from Eq. (8-122) will be higher than the true values
(of the order of 20 per cent higher). The problem can also be treated by
quasi-static methods, a first-order solution being!
B No 27C 2 FC
y, ~ q ( + ese 3a cot’ 3a (8-123)
A combination of the quasi-static and variational methods can be used to
obtain solutions of high accuracy.”

## Section 8-10: Waveguide Junctions
 We shall now consider waveguide junctions formed by butting two cylindrical guides together, possibly with a
diaphragm covering part of the z = 0 cross section. Figure 8-24 represents the general problem. No longer is there symmetry about the z = 0
cross section; so the methods of Sec. 8-6 do not apply directly. We there
1W. R. Smythe, “Static and Dynamic Electricity,’ 2d ed., p. 555, McGraw-Hill
Book Company, Inc., New York, 1950.

2 N. Marcuvitz, ‘““ Waveguide Handbook,” MIT Radiation Laboratory Series, vol. i0,
sec. 5-2, McGraw-Hill Book Company, Inc., New York, 1951.

MICROWAVE NETWORKS 421
fore take the more fundamental approach of constructing complete solutions in each region and enforcing

[[ Bt x Hteas = [[ Bx Ho-ds (8-124)
v0 220
where superscripts + and - refer to regions z > 0 and z < 0, respectively. In terms of the reaction concept, we can think of Eq. (8-124) as
stating that the reaction is conserved at the junction.

An equivalent network for the junction is shown in *Fig. 8-24b. It is*
evident that only a shunt element is required to represent the junction,
because an electric conductor placed across the entire z = 0 cross section
presents a short circuit to both waveguides. The characteristic admittances of the equivalent transmission lines are taken to be the characteristic wave admittances of the guides, and the ideal transformer represents
the change in admittance level. If the characteristic admittance of the
right-hand transmission line were chosen as n? times the characteristic
wave admittance of the guide, then the transformer would not be needed.
We shall use Eq. (8-124) to obtain stationary formulas for B and n?.

It is assumed that the excitation is at z = - ©; hence in the region
z2<0

; . Vo >
- = (c-ibe Be 7 oaite,
Er (e774 + To) Ve e+) Ve ey
7. : (8-125)
Hy = Yo-(e~*# - Tei#) THE ho - > YiV.e%*h;
where e,, h; are the mode vectors, a; are the cutoff mode-attenuation constants, Y¥; are the characteristic admittances, and I is the reflection
coefficient for the dominant mode. The subscripts 0 denote dominantmode parameters. Matched conditions are assumed at z = ©; hence in
T
T lin T
Side view End view
(a) (b)
*Fig. 8-24. (a) A waveguide junction, and (b) an equivalent circuit.*

422 TIME-HARMONIC ELECTROMAGNETIC FIELDS
the region z > 0
Et = Doen#Go + > Die-A8;
‘ (8-126)
Ht = Youths +) PPete
where the carets distinguish the various parameters from their z <0
counterparts. The application of Eq. (8-124) to the above field expressions yields
a 1-T
YorP r+ > PV = Dp Fo Vo? - y ¥iV2 (8-127)
Now the relative admittance seen from the left-hand guide is
1-T Y G . B
Tor 7 Ye 7¥etiye @-128)
Remembering that the Yo are real and the Y;, 7 ¥ 0, are imaginary, for
real V; and V; we have
Dvre+) Pve
FL - 1 2c
Yo Yove (8-129)
G _ Yor
Yo ~ YoVe
From our equivalent circuit, with matched conditions at z = ©, it is
evident that
G@ _ ia ¥st
Yo" Yo
V2
hence Re = as (8-130)
o
Finally, to obtain the V;and P,, we need only specialize Eqs. (8-125) and
(8-126) to z = 0 and, using the methods of Sec. 8-2, obtain
Vi= ff Beds
apert
(8-131)
Vv; = E;+ 6; ds
L
Note that the integration extends only over the aperture, because E: = 0
on the conductor. Equations (8-129) and (8-130), with V; and P; given
by Eq. (8-131), are formulas stationary with respect to small variations

MICROWAVE NETWORKS 423
in the aperture E; about the correct field. Alternative stationary formulas in terms of current on the conducting wall at z = 0 can also be
obtained (see Prob. 8-18). Note that Eq. (8-129) specialized to the case
of two identical guides is the diaphragm solution of the preceding section.

To illustrate the theory, consider the rectangular waveguide junctions
of Sec. 4-9. For the capacitive junction (*Fig. 4-16), the dominant-mode*
vectors are

(2. mx - 2. 9x

eo = uy 4/2 sin be = uy a[2 sin
Hence, regardless of our assumed tangential E in the aperture
Ey = u,f(y) sin = (8-132)
we have by Eqs. (8-130) and (8-131)
nae (8-133)
This is therefore the exact transformation ratio of the ideal transformer,
In Sec. 4-9, we calculatwu the aperture susceptance corresponding to the
crude choice f(y) = 1. The first summation in the numerator of Eq.
(8-129) then vanishes, and the second summation is related to the
aperture susceptance of Eq. (4-78) by
> 202 =sIVPB, = jetBe
7
But, for f(y) = 1, we have V.? = ac/2; hence, by Eq. (8-129),
B _ 2c?Bs _ 4c (Zo
Yo acYo | (9 B.) (8-134)
where the quantity in parentheses is plotted in *Fig. 4-17. The general*
expression [Eq. (8-129)} is positive definite in our particular case; so
Eq. (8-134) gives values of B/Y higher than the true values. However,
because the field in the aperture is less singular at the edge of a step than
at a knife edge, we should expect the assumption f(y) = 1 to give better
results in the junction problem than in the corresponding diaphragm
problem. Our approximate answer [Eq. (8-134)] gives an accuracy of
the order of 10 per cent, as illustrated by Table 8-3. This can be compared to the 20 per cent accuracy in the corresponding diaphragm problem, illustrated by *Fig. 8-21.
The inductive junction of Fig. 4-18 is treated in a similar manner. In*
general, the field in the aperture is of the form Ey, = f(x), and for the

424 TIME-HARMONIC ELECTROMAGNETIC FIELDS
TasLE 8-3. Comparison or Eq. (8-134) To THE Exact SoLUTION! FOR THE CASE
c/b = 0.5
MB
b c¥o
ro
Exact Approximate
0 1.57 1.63
0.2 1.69 1.84
0.3 1.93 2.10
0.4 2.44 2.67
1.N. Marcuvitz, “Waveguide Handbook,” MIT Radiation Laboratory Series, vol. 10,
sec. 5-24, McGraw-Hill Book Company, Inc., New York, 1951.
solution of Sec. 4-9 we assumed
Ee = u,f(2) = u, sin (8-135)
By Eq. (8-130), we then find the transformation ratio of the ideal transformer as
4c [ sin (rc/a) |?
2m SS nm F = (c/a)? (8-136)
and, by Eq. (8-129), the normalized shunt susceptance as
B - 2% (_ 1b
Y-~* 2s ( y Be (8-137)
where the quantity in parentheses is plotted in *Fig. 4-19. Note that,*
in contrast to Eq. (8-133), the transformation ratio [Eq. (8-136)] depends
on the assumed aperture field and is therefore approximate. Note also .
that the characteristic wave impedances of the two guides, z < 0 and
z > 0, are now different; so the superscript - has been retained on Yo~ in
Eq. (8-137). Finally, the value of -B/Yo- obtained from Eq. (8-137)
will be larger than the true solution, because of the positive definiteness
of the variational formula.
The alternative equivalent circuit of *Fig. 8-25 illustrates a very useful*
r . pn (Way of viewing the waveguide junction
Lin > of *Fig. 8-24a. We have separated the*
_ + shunt susceptance into two parts, which,
Yo° |jB- Yo by Eq. (8-129), can be identified as
oe CO we > Phe
*Fig. 8-25. Alternative equivalent jB- =i jB* = eee*
circuit for *Fig. 8-24a. Yoo YoVo? Yor yitP,2*
(8-138)

MICROWAVE NETWORKS 425
T T nil T
(9) Yog You
Side view End view
(a) (b)

*Fig. 8-26. (a) A thin coax-to-waveguide feed, and (6) an equivalent circuit.*
where the V,; and ?; are given by Eq. (8-131). Note that B- depends
only on guide z < 0, and in particular is one-half the shunt susceptance
of a diaphragm, assuming E, in the aperture is unchanged. This assumption is, of course, incorrect, but our formulas are stationary; so B~ in the
junction problem is approximately B/2 in the corresponding diaphragm
problem. Similarly, B+ is approximately B/2 for the diaphragm problem corresponding to the guide z > 0. Hence, by defining aperture susceptances according to Eqs. (8-138), we effectively divide the problem
into two parts, each part relatively insensitive to the other. An aperture
susceptance calculated for the aperture and one guide, such as Figs. 4-17
and 4-19, thereby becomes useful for a wide variety of problems.

## Section 8-11: Waveguide Feeds
 We shall now consider thin coax-to-waveguide feeds, as illustrated by *Fig. 8-26a. By thin, we mean that the*
dimension in the axial (z) direction is small. The analysis will be exact
only for zero-thickness junctions. An equivalent circuit when only one
mode propagates is shown in *Fig. 8-266. When more than one mode*
propagates, say N modes, there will be N ideal transformers in series,
each coupling to one mode. The justification for this equivalent circuit
will be found in the analysis.

Let the feed be viewed as a sheet of current J, in the z = 0 cross section. (This neglects the effect of the gap, which is usually small.) Then,
in the region z > 0, we have

E,t = ee (e-# + Tytet*)e;
T+Tr : $
: (8-139)
Ht = » Vi¥e (e-¥# - Tytev*)h;
t 1 + T+ + .f
i
where I;+ is the +2 reflection coefficient of the ith mode referred to

426 TIME-HARMONIC ELECTROMAGNETIC FIELDS
z=0. Similarly, forz < 0,
Ve
Er = eae os (ew + Tre-7)e;
* vy (8-140)
Hr = - yee (er - Tre-t*)h;
where I~ is the -z reflection coefficient of the ith mode referred to
z=0. We have ensured continuity of E, at z = 0 by choosing coefficients V; the same in both Eqs. (8-139) and (8-140). The boundary condition on H at z = 0 is
J. =u, x (Hit - Hr) |.-0
1=Te, 1 Te
= . Wis (eae + 7) u, X hy (8-141)
Multiplying each side by e; and integrating over the guide cross section,
we have
V=TF | v= TAY.
ViY; GE + i) = If jJ.:e:ds (8-142)
The field is then completely determined if the f’s and J, are known.
We now use the stationary formula of Eq. (7-89) to determine the
impedance seen by the coax. This formula is
1
Zin = - fi [[B-tas
where the integration extends over the z = 0 guide cross section and
Jy, is the current at the reference plane T’. Using the first of Eqs.
(8-139) for E, and Eq. (8-141) for J,, we obtain
i oy (l-Pe, l-ret
Zn = Ty ¥ v(; Fre ti +)
Finally, substituting for V; from Eq. (8-142), we have
2
Lg aff bon
°" 3 TST OT OM)
c
where Z; is the characteristic impedance of the ith mode. This is a stationary formula for the input impedance of a zero-thickness coax-to-waveguide feed, We can put it into a slightly different form by noting that

MICROWAVE NETWORKS 427
the wave impedance of an ith mode referred to z = 0 is
ag ttl 2, = 25 i (8-144)
Hence, Eq. (8-143) can also be written as
1 2 BeBe
2a 73 Dy (ff tres) gop es)
This shows that the guides z > 0 and z < 0 appear in parallel for each
mode. Nonpropagating modes decay exponentially from the junction
and their I’; may be taken as zero unless some obstacle is close to the feed.
If we assume that only one mode propagates, then all Z; are imaginary
except 7 = 0, and all r; = 0 except 7 = 0, provided the terminations are
not too close to the feed. Equation (8-143) or (8-145) can then be
written as
-T> -Tot\-!
B= niZy (te 4g Pee 4 ix
1+T7c 1+ To
fete aes
=n? 0 St + 5X
2c+4-"?
2 1 2
where n? = Te (ff J.+ eo as) (8-147)
2
iX=oh » Zz, i Jue as) (8-148)
= 140
Equation (8-146) is, of course, just that for the equivalent circuit of
*Fig. 8-26b.*
As an example, consider a probe in a rectangular guide (*Fig. 8-27).*
Assume
_ { uzsin k(d - x) d(y - c) a<d
where k = 27/) is the wave number of free space. The dominant-mode
vector is
~ a. .|2 sin ™
@o = Uz i sin >
Equation (8-147) is therefore
V/2/ab i) @ i , . ry
n= -akd Jo dx F dy sin k(d - x) 8(y - c) sin 3
giving n= - sin? F tan? (: 5) (8-150)
The summation for X [Eq. (8-148)] diverges, because the current was

428 TIME-HARMONIC ELECTROMAGNETIC FIELDS
taken as filamentary. If the probe is

, a oe taken as circular in cross section, the

i reactance can be evaluated by methods

4 similar to those used in Sec. 8-7. How' r ever, if the probe is very thick, we shall
i || Zo have to modify the equivalent circuit
of *Fig. 8-26b. The reactance of a short*
. probe can be estimated by the small*Fig. 827. Probe in a rectangular . .*

waveguide. obstacle approximation of Sec. 8-8. It
is evident from the small-obstacleanalysis that X is capacitive (negative) for a short probe and is of the order of

magnitude of X for a probe over a conducting ground plane.

Note that our present solution [Eqs. (8-146) to (8-148)], specialized to
a rectangular waveguide matched in both directions, is the same problem
treated in Sec. 4-10. From our equivalent circuit (*Fig. 8-26), it is evident that the coax sees*

=n? Zo
Ri, = 7 3
under matched conditions. Hence,
2Rin
n= zy, (8-151)
where R;, is the quantity calculated in Sec. 4-10. For example, when
the probe is connected to the opposite wall of the waveguide, as in *Fig.
4-20, we have from Eq. (4-91)*
2
ne = 28 (“2*) sin? 3 (8-152)
Other possible feeds are shown in *Fig. 4-28.

## Section 8-12: Excitation of Apertures*
 We now wish to consider conducting
bodies containing apertures excited by waveguides. The general problem is represented by *Fig. 8-28a. As far as the waveguide is concerned,*
the aperture appears simply as a load across the reference plane T. A
variational solution to the problem can be obtained by assuming tangential E in the aperture, calculating the resultant fields on each side of the
aperture, and then conserving the flux of reaction by

ff (E X H+ ds).xt = ff (E X H-ds)ine (8-153)
apert apert
This is the same approach that we took in Sec. 8-10 for the waveguide
junction. Indeed, we can think of our present problem as a junction
between the waveguide and external space.

MICROWAVE NETWORKS 429
Once the tangential E in the aperture is assumed, the problem separates
into two parts, external and internal. We have anticipated this separation by taking the equivalent circuit as shown in *Fig. 8-28b, where 7B*
represents the internal susceptance of the diaphragm and Y,,... the
external admittance of the aperture. The ideal transformer accounts
for possible differences of impedance reference in the internal and external
problems. The internal problem is identical to one-half of the waveguide-junction problem. Let us therefore abstract from Eq. (8-138)
B ») Y.V?
BLT Yo YoVo? & 154)
where Vi= [f Be-eds (8-155)
apert
These formulas give the internal shunt susceptance B in terms of an
assumed E,* in the aperture. For the external problem, we define an
aperture admittance as
1
Yapert = yi I E,* x H*-ds (8-156)
apert
where V is some reference voltage and H® is the external magnetic field
calculated from the assumed E,*. Examples of some aperture-admittance calculations are given in Sec. 4-11. (These calculations were made
on a conservation of power basis, but, because E* was assumed real, they
are the same as variational solutions.) To determine n? we note that the
dominant-mode voltage coupled to the aperture is Vo, but we have
referred the aperture admittance to V; hence
y?
ae 8-157
w= ( )
where Vo is given by Eq. (8-155) applied to the dominant mode.
mi lin
Conductor 2
Waveguide r be
fy s
ca ?
| Aperture
Side view End view
(a) (6)
*Fig. 8-28. (a2) An aperture excited by a waveguide, and (b) an equivalent circuit.*

430 TIME-HARMONIC ELECTROMAGNETIC FIELDS
es A
|
0.002 | =
| -F =.
cio = 225,
= t ll eel
B
0 --| Sa ee =-- - [= -|
0.2 ve fF 06 08 10
5 Ze" I + af >
ne 7 a/b=1 :
7G
-0.002 7
Pani
1, vr
COL | Gey
-0.004 I ao
" jk a >
cost Mtl PS] rg ga ee
*Fig. 8-29. Aperture »dmittance for rectangular apertures in ground planes, referred*
to the dominant-mode witage of a rectangular waveguide of the same dimensions.
(After Cohen, Crowley, and Levis.)

An aperture of practical importance is the rectangular aperture in a
conducting ground plane, as shown in the insert of *Fig. 8-29. The aperture admittance has been calculated for the assumed field*

Ee = vy, sin (8-158)
in the aperture, referred to the voltage
ye J (8-159)
2
which is the dominant-mode voltage for a waveguide of the same dimensions as the aperture. Hence, when the aperture is simply the flanged
open end of a rectangular waveguide, then n = 1. The field due to Ee
in the aperture can be found by the methods of Sec. 3-6, and the aperture
admittance calculated by Eq. (8-156). The mathematical details are
tedious but can be found in the literature.! Figure 8-29 shows the aperture admittances for a square aperture and for a rectangular aperture
with sides in the ratio 1 to 1 and 2.25 to 1.?

1 Cohen, Crowley, and Levis, The Aperture Admittance ofa Rectangular Waveguide
Radiating into Half-space, Ohio State Univ. Antenna Lab. Rept. ac 21114 SR no. 22,
1953.

2 Additional calculations have been made by R. J. Tector, The Cavity-backed Slot
Antenna, Univ. Illinois Antenna Lab. Rept. 26, 1957.

MICROWAVE NETWORKS 431
As an example, suppose we have a square waveguide of height and
width a feeding a rectangular aperture with sides in the ratio a/b = 2.25,
as shown in *Fig. 8-30. The waveguide is excited in the dominant y-polarized mode, for which*
e@o = Wy v2 sin
a a
Hence, by Eqs. (8-155) and (8-158), we have
v2 i * if . 9 TL b
Vo=-]| d d 2 = -_
0 a |, x H y sin? = Tp
and so, by Eqs. (8-157) and (8-159),
nt =F = 2.25
The shunt susceptance B is one-half that for the diaphragm of *Fig. 8-22b.*
An approximation to B is therefore given by Eq. (8-120) with B replaced
by B/2, b by a/2, and c by b/2, giving
B_ 8a ab a
Y,* x, 08 3g = 3.54
Hence, the terminating admittance seen by the waveguide is
Y ~ 73.54 © + 2.25Y sen
Xo
where Yopert iS given by the a/b = 2.25 curves of *Fig. 8-29.

## Section 8-13: Modal Expansions in Cavities*
 Consider a cavity formed by a
perfect conductor enclosing a dielectric medium. Each mode must
Y
es
--- Poaaan4
Ti iy
fe a
| Lt
Side view End view
Fra. 8-30, A square waveguide feeding a rectangular aperture in a ground plane.

432 TIME-HARMONIC ELECTROMAGNETIC FIELDS
satisfy the field equations
Vx Ey = -jopHi VX Ay = juek; (8-160)
where 7 is a mode index. Either E; or H; may be eliminated from the
above pair of equations, giving the wave equations
Vv xX (wv X E,) - wieE; = 0
vx (CV XH) - otal: = 0 (8-161)
valid even if « and p are functions of position. Each of these wave equations, coupled with the boundary condition
nx E; =n xX (e'v xX Hi) =0 on S (8-162)
where n is the unit normal directed outward from the cavity boundary S,
is an eigenvalue problem in the classical sense.1_ Hence, for c and p real
(no dissipation), the eigenvalues w; (resonant frequencies) are real, and
the eigenfunctions E;, H; form a complete orthogonal set in the Hermitian
sense. Furthermore, we wish to normalize the mode vectors, so that the
orthogonality relationships are
0 tA
+ E* =
[ff Be BF ar i 5 (8-163)
which can be derived from Eqs. (8-160) in the usual manner. Normalization of the E; also normalizes the H;, because
[ff ema ar = fff sta ar
that is, the time-average electric and magnetic energies are equal.
Hence, the orthogonality relationships for the H; corresponding to the
orthonormal E; are
0 tA
. * = -.
[ff Me HE a {3 toy (8-164)
We have already shown in Sec. 8-4 that if E; is chosen real, then the corresponding H; is imaginary, and vice versa.
Now suppose that electric sources exist within the cavity, as suggested
by *Fig. 8-3la. The field equations are then*
V XE = -jopH Vx H = juE+J
and the wave equation is
Vv xX (uv X E) - wxE = -joJ (8-165)
1Philip M. Morse and Herman Feshbach, ‘Methods of Theoretical Physics,’’
chap. 6, part I, McGraw-Hill Book Company, New York, 1953.

MICROWAVE NETWORKS 433
n n
Fie. 8-31. A cavity containing (a) electricsources,
and (b) magnetic sources.
Ss Ss
(a) (6)
Because the E; are a complete set, we can let
B= ) AE (8-166)
Substituting this into Eq. (8-165), we have
> Adv X (wv X Ei) - o%E] = -joJ
5
which, by Eq. (8-161), can be written as
¥ Aw? - w)Es = -juJ
If each side is now multiplied scalarly by E} and integrated over the
volume of the cavity, all terms except 7 = j vanish because of orthogonality [Eq. (8-163)], and we have
(2 - w)As = -jo ff J-Etdr (8-167)
which determines the A;. Hence, Eq. (8-166) becomes
p=) BPs, [ff s-zre (8-168)
w? -= w,? t
<
and the corresponding H, obtained from the field equations, is
je BG
wa) fe fff s-zra (8-169)
i
Note that the field becomes extremely large as w approaches some
resonant frequency. In fact, the field becomes infinite at a resonant frequency in the loss-free case, which is to be expected. Actually, in any
physical problem there will always be some dissipation; so the w; are complex. Hence, the field is large, but finite, at all real resonant frequencies.
The dual problem is that of magnetic sources in a cavity, represented
by *Fig. 8-31b. In this case, the wave equation in H is*
Vv X (e"V X A) - wypH = -joM (8-170)

434 TIME-HARMONIC ELECTROMAGNETIC FIELDS
We then expand H in terms of the orthonormal mode vectors H; as
H= ) BH; (8-171)
y
where, dual to Eq. (8-167), the B; are given by
(o? - 0) B = -jo [ff MH ar (8-172)
Hence, the expansion of H due to magnetic currents M is!
w= YP fff esr ar (8-173)
- wo” - Wy
F
and the corresponding E field is
_ Vi dod He _
E yes fff Hi dr (8-174)
i
If both electric and magnetic sources exist within the cavity, we can
superimpose Eqs. (8-168) and (8-174) for a solution.

## Section 8-14: Probes in Cavities
 Mathematically, we can represent a probe
in a cavity in terms of electric currents in the cavity, as shown in *Fig.
8-3la. The impedance seen at the input terminals to the probe can then*
be calculated by the variational formula

1
Zin = ff] ese (8-175)
where J* is the assumed current distribution on the probe, and J is the
corresponding input current. All mode vectors E; will be chosen real;
so the field produced by J* is given by Eq. (8-168) with the * dropped.
Substituting this equation into Eq. (8-175), we obtain
jw az
Za= - 7p » 3a = oA (8-176)
Fi
where a= f f il E; + J* dr (8-177)
The analysis neglects the effect of the aperture through which the probe
isfed. This effect is usually negligible and can be taken into account by
the methods of the next section.

As long as there is no dissipation, the input impedance will be purely
reactive. However, if the cavity is lossy but high Q, the effect of dissipa
1The eigenvalue w; = 0 must be included in both Eqs. (8-168) and (8-173). The
modes associated with w; = 0 account for the irrotational parts of Eand H. See, for
example, Teichmann and Wigner, J. Appl. Phy., vol. 24, March, 1953.

MICROWAVE NETWORKS 435,
tion can be taken into account by 7
letting the resonant frequencies be 4
complex, according to! L Cc

wet = ea(1 + 3) (8-178)

+ + *Fig. 8-32. An equivalent circuit for a*
where Q is the quality factor. Inthe oi. fod cavity in the vieinity of
vicinity of a resonant frequency, say .sonance.
wo (not necessarily the dominant resonant frequency), we can approximate Eq. (8-176) by

. jia(ao/ 1)?
Za = j{X -- =o 8-179
IN FH wll $570) e179)
where X is the reactance due to all modes except the 7 = 0 mode
r w a,?
xX=- Pp ¥ Bat (8-180)
+20
The effect of dissipation in modes not near resonance is negligible; hence,
it is not included in Eq. (8-180). An equivalent circuit which represents
Eq. (8-179) is shown in *Fig. 8-32. To determine the values of R, L, and*
C, we need only compare the formula for the impedance of the parallel
RLC circuit
wo? = =
aa jw/C ° LC
Fool F7 gi k_ R
oL woL
with the last term of Eq. (8-179). It is then evident that
_ Q (a? _ ao \? _ I 2
R= ows L= Too C= a (8-181)
where dp is obtained from Eq. (8-177).
To illustrate the theory, consider a probe in a rectangular avity
(*Fig. 8-33). The normalized mode vector of the dominant mode is*
2 - TY. 72
E, = uz, -S-- sin ~ sin - 8-182
° * Veabe b c ( )
where the normalization factor was obtained from Eq. (2-97). For the
current on the probe, we assume
sin k(d - 2) _y a
Je= ( lanka ay - v’)a(y - c’) a<d (8-183)
0 z>d
1M. E. Van Valkenberg, “Network Analysis,” p. 364, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1955.

436 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ty ty
ke b
T° - fF
Z x
<_ -_-Ax
+ a
Zz c e
~<
*Fig. 8-33. Probe in a rectangular cavity.*
Then, by Eq. (8-177), we have
,
oo a tan (#5) sin (= ) sin (7° (8-184)
I kVeabe 2 b c
The other parameters needed to evaluate R, L, and C are the resonant
frequency f, = wo/2z, given by Eq. (2-95), and the quality factor Q, given
by Eq. (2-101). The evaluation of the series reactance X is a much more
difficult problem. We cannot, of course, use the filamentary current of
Eq. (8-183) to evaluate X, since the resulting reactance would be infinite.
The actual diameter of the stub must be considered. To a very rough
approximation, X will be of the same order of magnitude as for a stub
over aground plane. Hence, for short stubs, the reactance is capacitive.
When the stub is bent into a small loop and joined to the cavity wall,
the system is often called a loop feed. The treatment of loops in cavities
is essentially the same as the treatment of stubs, once a current is assumed
on the loop. The series reactance X for small loops is inductive, in contrast to the small-stub case, for which it is capacitive. Some explicit
loop feeds are considered in Probs. 8-24 and 8-26.

## Section 8-15: Aperture Coupling to Cavities
 The general problem of coupling
a cavity to a waveguide through an aperture is represented by *Fig. 8-34a.*
For a variational treatment of the problem, we assume an aperture field
E,* and conserve reaction according to
[[ Ge x He-ds)eu = ff (Be x H+ ds)ensy (8-185)
apert apert

MICROWAVE NETWORKS 437
For a given E,*, each side of this equation can be considered separately,
which amounts to dividing the original problem into two parts, as shown
in *Fig. 8-34b andc. The equivalent current*
My =n x Es (8-186)
in the cavity part is the negative of the terminating current in the waveguide part. The waveguide part of the problem is identical to the problems treated in Secs. 8-10 and 8-11, and is therefore of the form
[J (Be x He ds)euse = -YVE + Y ¥AVe!
apert n#0
where the V, are the various mode voltages, the Y, are the mode-characteristic admittances, and Y is the admittance seen by the dominant mode.
Hence, we can rewrite Eq. (8-185) as
¥ = 5B, - ha [fe x Hea a (8-187)
Yo YoVo? alate
‘apert
where Y, is the characteristic admittance of the dominant mode and
Bae-j 5 Js @ (8-188)
£ Yo \Vo
nz0
an n
ots
(2) (b)
T lin R
A 1
{|-™. c
©) (@)
Fra. 8-34. (a) Aperture coupling from a waveguide to a cavity can be divided into two
parts, (b) the cavity, and (c) the waveguide. An equivalent. circuit in the vicinity
of resonance is shown in (d).

438 TIME-HARMONIC ELECTROMAGNETIC FIELDS
is the shunt susceptance introduced by the waveguide part of the problem. The calculation of B, was treated in Sec. 8-10.

For the cavity part of the problem, we can determine the field by Eq.
(8-173) with the current given by Eq. (8-186). Taking the mode vectors
H; as real, we obtain

jwH,
He = y = niall /[ Ee X Hi-ds
Cy ww? - a!
The right-hand side of Eq. (8-185) is then given by
7 2
ll (Ee X H+ ds)evity = y Ja? (8-189)
wo - wo,’
apert i
where b = ff Be x Hy-ds (8-190)
In the vicinity of a resonant frequency, we again take losses into account
_by Eq. (8-178), and Eq. (8-187) can be written as
Ys jo b? bo? |
Kor 5Bo YoV 0? Dr - uw? + w* - wo(1 + 7/Q)
ix
The first term in the brackets represents the susceptance due to all nonresonant modes in the cavity, and the second term gives the resonantmode effect. The above equation can therefore be written as
Y . ne. jw(bo/ V)?
= ~jB,+ | IB - == oy 8-191
Yo JBa + aE wo - wor(1 + 9/Q) ( )
where the susceptance due to nonresonant cavity modes is
wo b?
B= -%, » zt (8-192)
iA
and, to account for an arbitrary reference-voltage V, we have introduced
the ideal transformer
2 Ley 8-193
n= (F) (8-198)
Finally, we can represent the last term of Eq. (8-191) as a series RLC
circuit, as shown in *Fig. 8-34d. The formula for admittance of a series*
RLC circuit is
2 - 25
ye -jo/L enleine
~ oF = wor(1 + 5/Q) Q= oe
~ oR waCR

MICROWAVE NETWORKS 439
Comparing this with the last term of Eq. (8-191), we see that
1 Qfbo\? _ {bo \ _ (VV
Ro 2() C= (Fe L= be (8-194)
where by is obtained from Eq. (8-190).

Let us illustrate the above theory by a treatment of the rectangular
waveguide to rectangular cavity junction, shown in *Fig. 8-35. The waveguide part of the problem is identical to problems previously considered.*
In particular, B, will be approximately one-half of Eq. (8-120) with the
appropriate interchange of symbols, or

B, _ 4a’ ad
yh’ log ese aa (8-195)
For the cavity part of the problem, let us make our often-used assumption
Ey = usin e (8-196)
in the aperture. Also, let us refer the cavity admittances to
v= (8-197)
2
which is the waveguide dominant-mode voltage that would be excited by
Eq. (8-196) if the waveguide were the same height as the aperture (n?
would be 1 in that case). In our particular problem, the waveguide
dominant-mode voltage is Vo = a/ba’/2; hence
d
v= 7 (8-198)
Rather than calculating Eq. (8-192) directly, let us view the aperture as
the junction between two waveguides of height a’ and a. The susceptee
Waveguide | Cavity i
*Fig. 8-35. Aperture cou- 4*
pling from a rectangular r --- 7
waveguide to a rectangu- Top view
lar cavity. <_ t
az it
Side view

440 TIME-HARMONIC ELECTROMAGNETIC FIELDS
ance B, referred to the mode voltage of a waveguide of height a could
then be approximated by Eq. (8-195) with a’ replaced by a. But we
wish to refer it to the V of Eq. (8-197); so we should multiply by d/a
and obtain
4d ad
Be = ra log ese 5a (8-199)
Finally, to determine the R, L, and C, we need the normalized dominantmode vector, which is
2 - Ty TZ Ty . 72
BH = === ( wb sin = cos - - u.ccossin-} (8-200
~/ nabc(b? + c?) ( i b c v Cc c )
Hence, from Eqs. (8-190), (8-196), and (8-197), we obtain
bo\? _ 2d
(7) ~ pact + 6/6)? (6-201)
The resonant frequency f, = wo/2m is given by Eq. (2-95) and the quality
factor Q by Eq. (2-101). Hence, all parameters of the equivalent circuit
(*Fig. 8-34d) have been evaluated.*
PROBLEMS

## Section 8-1: Consider the parallel-plate waveguide formed by conductors covering the
y = 0 and y =b planes
 Show that the eigenfunctions, normalized on a per unit
width basis, are

oY
Wo’ Ve
vn" = v2 sin 27Y
ne 6
age = VED gg RY
nt b
where n = 1, 2,3,....

## Section 8-2: Consider an z-directed current element Il at the point 2’, y’, 2’ in a rectangular waveguide (Fig
 2-16). Show that the field is given by formulas of Table
8-1 where W’s are given by Eqs. (8-34) and, for n, m #0,

'b a
Vinn™ = VE fon Vint = - AVE fan
where
/Gmb)* + (nayt yo ,
Fan = T(E) nn LORIE 0? gos MEE i, MEY gale
and, for m = 0,
Vont = -I1(Zo) on Nea sin is enYonle=*'1

MICROWAVE NETWORKS 441

## Section 8-3: For the general cylindrical waveguide (Fig
 8-1), show that the time-average
electric energy per unit length of guide is

= 1) kes™\*
B= 5) evel + elven + «(AY trem
A we
i
and the time-average magnetic energy per unit length of guide is
a ch "1 ket?
Fu = 5), leet + alte + (BE) [rep
7
Note that these are just the sum of the energies in each mode alone.

## Section 8-4: Let the T equivalent circuit of Fig
 8-10b represent a section of waveguide of

length /, propagation constant jf, and characteristic impedance Zp. Show that
Ze = ~jZo csc pl
Zy = 5% tan pl/2

## Section 8-5: Using the usual perturbational method, show that, for general cylindrical wave
guides, the attenuation constant due to conductor loss is
1Qk am)?

nao ep (S) @

for TM modes, and
= 18214 (ask § oral]
w= a5 elf (ar) are poy 7

for TE modes
 & denotes intrinsic resistance of the metal walls, » intrinsic impedance
of the dielectric, and the other symbols correspond to their usage in Table 8-1.

## Section 8-6: Use the above formulas to determine the attenuation in rectangular waveguides
(Prob
 4-4) and“in circular waveguides (Prob. 5-9).

## Section 8-7: Consider a one-port network, and define the reflection coefficient fT = V"/V*

Show that, for Zp» real,

ba = (1 - IF )|V*I2/Zo
and Wn - B= 2 [VI Im (E)/20
Hence, in a source-free network, {I'|? < 1, and, at resonance, I is real.

## Section 8-8: Derive Eqs
 (8-72).

## Section 8-9: Let the characteristic impedances of ports (1) and (2) of Fig
 8-7 be normalized to unity. Show that the transmission matrix [T']] is related to the impedance
matrix [z] by

2Pu = en +2 - 2u)(en - 1)
212
1
2Tia = -201 + 5 1 + 211) (22 - 1)
Wu =n +2 andes +0)
212
2 = -en +2 tendon +1)
Show that in the loss-free case T;, = T3, and Ti: = Tn.

442 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 8-10: Add a magnetic current sheet M, coincident with the electric current sheet J

of *Fig. 8-11. Determine M, and J. such that they are a unidirectional dominantmode source, sending waves in the +z direction only. Determine the self-reaction*
of this source in the presence of the magnetic conductor terminating the guide.

## Section 8-11: Derive Eq
 (8-96).

## Section 8-12: Consider the centered capacitive post in a rectangular waveguide, shown in
Fig
 8-36. Show that the equivalent network parameters are
Be Yo_ xd?
Yo Be 2an, :
The approximations are good for d/a < 0.3 and a/dy < 0.2.
JB
T j_-b-+| T t 7
a Yo jBa jBa Yo
a
pee
Side view End view Equivalent circuit
*Fig. 8-36. Centered capacitive post in a rectangular waveguide.*

## Section 8-13: Consider the inductive diaphragm of Fig
 8-23. Approximating E; in the
aperture by
E, = u, sin =
show that Eq. (8-122) is a crude variational solution for the shunt susceptance.

## Section 8-14: The inductive diaphragm (Fig
 8-23) has boundaries cylindrical to y. The
incident mode is TM to y; hence, the entire field must be TM to y. Express the field
as H = Vv X wy where
2
_ nee
y= ») An sin ~~ eve
n=
In the aperture, tangential E must be of the form
E: = u,f()
Show that
a Fy 2
SOO imate
B_ 2 a=2 a
“Fe” a 6 rd id
Lf F(z) sin ac |
is a variational formula for the shunt susceptance. Note that it gives upper bounds
to -B/Y>. Problem 8-33 is the special case f(z) = sin (xz/c).

## Section 8-15: Consider the inductive diaphragm (Fig
 8-23) and the variational formula in
terms of obstacle current [Eq. (8-107)]. On the diaphragm, the current is of the form
Js = wy9(2)

MICROWAVE NETWORKS 443
Show that
. 1
@ Pe =
wy (z) sin - dz
Toran Lf#
Yo a nae (n/2) (a/x) e a
BY 2d, [foo sin = ar |’
c a
is the variational formula for lower bounds to -B/Yo.

## Section 8-16: Show that the shunt susceptance of the capacitive diaphragm of Fig
 8-37 is
given by the same formula as applies to *Fig. 8-22a.*
_ RSS SS | SS
*Fig. 8-37. A capacitive 2c ; rc t-~s@Y*
diaphragm (metal shown 4b F RRR
dashed). fe ee
KX

## Section 8-17: Consider the capacitive junction of Fig
 8-38. Show that the parameters of
the equivalent circuit are
Bt abr, a
Yo vy 8 opt
a a
Yo hy 8 8 b=
bva
Use the approximation of Eq. (8-120).
T z lin T
iB-2c iB
Let Yo Yo
i al
Side view End view Equivalent circuit
*Fig. 8-38. A capacitive junction.*

## Section 8-18: Consider the waveguide junction of Fig
 8-24a and the equivalent circuit of
*Fig. 8-25. Show that, analogous to Eqs. (8-138),*
Sas Sate
pre Yor
JB Ge To® = GBF Zgt Bot
and n? = 1,?/f,%, The mode currents are given by
I= ff Hovhids f= If Hy ficds
where H,*+ and H,~ denote tangential H on the +z and -z sides of the junction,
respectively. Variational formulas are obtained by assuming H,* and H,~ subject to
the restriction H,+ = H,~ in the aperture.

444 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 8-19: Let ¥(z,y) = f(p,c) be a solution to the two-dimensional source-free Helm
holtz equation p <a
 Prove that
** sla,syent dg = F Fa(kaylesPy(0))
) , a"
where e’”? is an operator defined by
+ 10a 1a

sin D = 5 3g cosD = 55,
and ei"Py(0) means e’"¥(z,y) evaluated at z = 0, y =0. This is a kind of meanvalue theorem.

## Section 8-20: Consider the coax to waveguide feed of Fig
 4-20. Let d denote the diameter
of the coaxial stub, and leta <2. Show that, for the equivalent circuit of *Fig. 8-26b,*

nia 28 sint ;
92 log ee
Xz x log 2
where 7 = 1.781.

## Section 8-21: Let the rectangular aperture of Fig
 8-29 be thin (b « \) and of resonant
length (a ~ 2/2). Show that
b
Yapert = 0.004 x
Hint: Use the duality concept of Prob. 7-43 and the approximations of Prob. 7-39.
Note that the aperture radiates only into half-space.

## Section 8-22: Figure 8-39 represents a parallel-plate transmission line radiating through a
slot into half-space
 Let *Fig. 8-28b represent the equivalent circuit, and evaluate the*
parameters, using the aperture admittance of *Fig. 4-22.

t Fie. 8-39. A parallela TFT plate transmission line*
t $ radiating into balf.

y g into half-space.

MICROWAVE NETWORKS 445

## Section 8-23: Figure 8-40 represents a rectangular waveguide having sides a, ? ae
into half-space through a narrow resonant slot
 Using the results of Prob. ,
show that reflectionless transmission through the slot occurs when
a 0.54 cos?(r\/4b)
x a =(ay
sb -G)
When b/d < 0.7, the above formula can be approximated by
«24 (3)
x3 ~ (a
The waveguide is excited in the dominant mode.
rr b - |
*Fig. 8-40. A rectangular rr an*
waveguide radiating into Ce ess | '
half-space through a reso- ' ¥;
nant slot. bu-----

## Section 8-24: Consider the loop-fed rectangular cavity of Fig
 8-41. Assume that the loop
is small, so that the current on it may be assumed constant. Show that the elements
of the equivalent circuit (*Fig. 8-32) are given by Eqs. (8-181) where*

’
ao 24 sin (x) 80 (*)
oo - -“-- sin (+ sin {7
T ~ \/eabe 7 °
When c’ <c, this reduces to y
2rA_
go ., “*~_ sin (- )
TG c Veabe b
where A = c’d is the area of the loop.
6
5 A
vy
*Fig. 841. A loop-fed*
rectangular cavity. j---_ e----|
= | i

446 TIME-HARMONIC ELECTROMAGNETIC FIELDS

## Section 8-25: Show that the normalized mode vector for the dominant mode of the circular

cavity (Fig
 8-42) is
1
E, = u, ----__ JJ G fy
a Verb Ilan) Va
where 2, = 2.405.
ta)

pple sees

b ma 4 b

L Fe # ms 4

F
(2) (b)
*Fig. 8-42. A circular cavity with (a) probe feed, and (b) loop feed.*

## Section 8-26: Figure 8-42a represents a probe-fed circular cavity
 Assume sinusoidal distribution of current on the probe, and show that the elements of the equivalent circuit
(*Fig. 8-32) are given by Eqs. (8-181) where*

ao 1 d c

> = ton *5) J G 5)

1 ka Verb Juan) ( 7 oer
and zo, = 2.405.

## Section 8-27: Figure 8-42b represents a loop-fed circular cavity
 Assume uniform current
on the loop, and show that the elements of the equivalent circuit (*Fig. 8-32) are given*
by Eqs. (8-181) where

a ° (= ‘)
Ta Verb Jx(zo1) ‘a
Show that, when c ~ a, this reduces to
a Azo
Tat Verb
where A = (a - c)d is the area of the loop.

## Section 8-28: Reconsider Fig
 8-41 for the case of a small loop. Represent the loop by a
magnetic-current element Kl, according to *Fig. 3-3, and evaluate*
Re (aa) __ K1-H
ann nr
The result is the same as the small-loop answer in Prob. 8-24.

## Section 8-29: Reconsider Fig
 8-42b by the method outlined in Prob. 8-28. Show that the
result is the same as the small-loop answer of Prob. 8-26.

## Section 8-30: Show that the normalized H mode vector for the dominant mode of the
spherical cavity (Fig
 6-2) is

0.536 T\
; H = wy, 2:536 7, (2744 ) sin @
r Von @,

BIBLIOGRAPHY
A. Classical Books
1. Abraham, A., and R. Becker: ‘The Classical Theory of Electricity,’ Blackie
& Son, Ltd., Glasgow, 1932.
2. Heaviside, O.: “Electromagnetic Theory,” Dover Publications, New York,
1950 (reprint).
3. Jeans, J.: “Electric and Magnetic Fields,” Cambridge University Press,
London, 1933.
4, Maxwell, J. C.: “A Treatise on Electricity and Magnetism,” Dover Publications, New York, 1954 (reprint).
B. Introductory Books
1. Attwood, S.: “Electric and Magnetic Fields,’’ 3d ed., John Wiley & Sons,
Inc., New York, 1949.
2. Booker, H. G.: ‘An Approach to Electrical Science,” McGraw-Hill Book
Company, Inc., New York, 1959.
3. Harrington, R. F.: “Introduction to Electromagnetic Engineering,” McGraw-Hill Book Company, Inc., New York, 1958.
4. Hayt, W. H.: “Engineering Electromagnetics,” McGraw-Hill Book Company, Inc., New York, 1958.
5. Kraus, J. D.: “Electromagnetics,” McGraw-Hill Book Company, Inc., New
York, 1953.
6. Neal, J. P.: “Electrical Engineering Fundamentals,” McGraw-Hill Book
Company, Inc., New York, 1960.
7. Page, L., and N. Adams: “Principles of Electricity,” D. Van Nostrand Company, Inc., Princeton, N.J., 1931.
8. Peck, E. R.: “Electricity and Magnetism,’ McGraw-Hill Book Company,
Inc., New York, 1953.
9. Rogers, W. E.: “Introduction to Electric Fields,’ McGraw-Hill Book Company, Inc., New York, 1954.
10. Sears, F. W.: ‘Electricity and Magnetism,’ Addison-Wesley Publishing
Company, Reading, Mass., 1946.
11. Seely, S.: “Introduction to Electromagnetic Fields,” McGraw-Hill Book
Company, Inc., New York, 1958.
12. Shedd, P. C.: ‘Fundamentals of Electromagnetic Waves,” Prentice-Hall,
Inc., Englewood Cliffs, N.J., 1955.
13. Skilling, H. H.: “Fundamentals of Electric Waves,” 2d ed., John Wiley &
Sons, Inc., New York, 1948.
14. Spence, D., and R. Galbraith: “Fundamentals of Electrical Engineering,”
The Ronald Press Company, New York, 1955.
15. Ware, L. A.: “Elements of Electromagnetic Waves,” Pitman Publishing
Corporation, New York, 1949.
16. Weber, E.: “Electromagnetic Fields,” John Wiley & Sons, Inc., New York,
1950.
A7i

472 TIME-HARMONIC ELECTROMAGNETIC FIELDS
C. Intermediate and Advanced Books

1. Jordan, E.; ‘Electromagnetic Waves and Radiating Systems,” PrenticeHall, Inc., Englewood Cliffs, N.J., 1950.

2. King, R. W. P.: “Electromagnetic Engineering,” McGraw-Hill Book Company, Inc., New York, 1953.

3. Mason, M., and W. Weaver: ‘‘The Electromagnetic Field,” University of
Chicago Press, Chicago, 1929.

4. Ramo, S.,and J. R. Whinnery: “‘ Fieldsand Wavesin Modern Radio,” 2d ed.,
John Wiley & Sons, Inc., New York, 1953.

5. Schelkunoff, S. A.: “Electromagnetic Waves,” D. Van Nostrand Company,
Inc., Princeton, N.J., 1943.

6. Smythe, W. R.: “Static and Dynamic Electricity,” 2d ed., McGraw-Hill
Book Company, Inc., New York, 1950.

7. Stratton, J. A.: “Electromagnetic Theory,” McGraw-Hill Book Company,
Inc., New York, 1941.

D. Books on Special Topics

1. Aharoni, J.: “Antennae,” Clarendon Press, Oxford, 1946.

2. Bronwell, A., and R. E. Beam: ‘‘Theory and Application of Microwaves,”
McGraw-Hill Book Company, Inc., New York, 1947.

3. Kraus, J. D.: ‘Antennas,’ McGraw-Hill Book Company, Inc., New York,
1950.

4. Lewin, L.: ‘Advanced Theory of Waveguides,” Illiffe and Sons, London,
1951.

5. Marcuvitz, N.: “Waveguide Handbook,” MIT Radiation Laboratory Series,
vol. 10, McGraw-Hill Book Company, Inc., New York, 1951.

6. Mentzer, J. R.: “Scattering and Diffraction of Radio Waves,’ Pergamon
Press, New York, 1955.

7. Montgomery, C. G., R. H. Dicke, and E. M. Purcell (eds.): “Principles of
Microwave Circuits,’ MIT Radiation Laboratory Series, vol. 8, McGrawHill Book Company, Inc., 1948.

8. Moreno, T.: “Microwave Transmission Design Data,’”’ Dover Publications,
New York, 1958 (reprint).

9. Reich, H. J. (ed.): “Very High Frequency Techniques,” Radio Research
Laboratory, McGraw-Hill Book Company, Inc., New York, 1947.

10. Schelkunoff and Friis: “Antennas, Theory and Practice,” John Wiley &
Sons, Inc., New York, 1952.

11. Silver, S.: ‘Microwave Antenna Theory and Design,” Radiation Laboratory
Series, vol. 12, McGraw-Hill Book Company, Inc., New York, 1950.

12. Slater, J. C.: “‘ Microwave Electronics,” D. Van Nostrand Company, Inc.,
Princeton, N.J., 1950.

13. Watkins, D.: “Topics in Electromagnetic Theory,” John Wiley & Sons, Inc.,
New York, 1958.

14. Wait, J. R.: ‘Electromagnetic Radiation From Cylindrical Structures,”
Pergamon Press, New York, 1959.

APPENDIX A

---

## Appendix A: Vector Analysis

VECTOR ANALYSIS
We shall normally orient rectangular (z,y,z), cylindrical (p,c,z), and
spherical (r,6,c) coordinates as shown in Fig. A-1. Coordinate transformations are then given by
Z=pcosc=rsin'cos@
y = psincg =rsin '6singd
z=rcos@
p=Vitt+y?=rsind
o= tant 2 (A-1)
r= VEEEER - VET?
V/ 2
6 = tan-? ver & tante
z z
Transformations of the coordinate components of a vector among the
three coordinate systems are given by
Az = A,cos c - A,sin c
= A,sin 6cos c + Aecos 6cos c - Agsind
A, = A,sinc? + A, cos c
= A, sin @sin c + Ag cos @sin c + Agcos c
A, = A, cos @ - Agsin 6
A, = A.cosc+ A,sin c = A, sin 6+ Ags cos 0 (A-2)
As = - A, sin d+ A, cos c
A, = Az sin @cos c + A, sin @sin c+ A, cos 6
= A,sin@+ A, cos 6
Ae = A.cos'cos c+ A, cos @sin c - A, sin 6
= A,cos@- A,sin@
The coordinate-unit vectors in the three systems are denoted by (uz,ty,ts),
(u,,Ug,u,), and (u,,Ue,u4). Differential elements of volume are
dr = dx dy dz = pdpdcdz =r’ sin 6 dr dd do (A-8)

448 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Zz
7
a,
~
~
Ls Fig. A-1. Normal coordi| nate orientation.
6 {
|
I y
a
# el co 2
| ene, YP
x
differential elements of vector area are
ds = u, dy dz + u, dz dz + u,dzdy
= u,p dc dz + uy dpdz + u.pdpdcd (A-4)
= u,r? sin 6 d0dc + ugr sin 6 dr dd + ugr dr d'
and differential elements of vector length are
dl = u,dz + u, dy + u, dz
= u,dp + ugp dg + u, dz (A-5)
= u,dr + uor dd + ugr sin 6dc
The elementary algebraic operations are the same in all right-handed
orthogonal coordinate systems. Letting (u1,u2z,us) denote the unit
vectors and (A,,A;,,A3) the corresponding vector components, we have
addition defined by A+B = ui(A; + By) + u2(A2 + Bz) + usx(As + Bs) (A-6)
scalar multiplication defined by
A-B = A,B,+ A2Bz + AsBs (A-7)
and vector multiplication defined by
UW. U2 Us
AXB=/A1 Az A; (A-8)
B, B. B;
The above formula is a determinant, to be expanded in the usual manner.
The differential operators that we have occasion to use are the gradient
(Vw), divergence (V-A), curl (V xX A), and Laplacian (V?w). In
rectangular coordinates we can think of del (V) as the vector operator
=y2 a a ;
Vets tig, t 52 (A-9)

VECTOR ANALYSIS 449
and the various operations are
ow ew ow
Vo = uae t Uy 3y tus
0A 0A 0A
7 ie Ae ee op Se ee
ba ox ef oy + Oz
Uuou wu,
vxas|2 2 2 10)
~ lax dy a
A, A, A,
aw, dw, ew
2p = -_ - Vw = aa + aye + oe
In cylindrical coordinates we have
ow low ow
Vvu= Yea, t Yel ag t Ge
=o dyvay , date
VA bop (ite) +5 36 +3
_. (lad, aAg aA, _ OA,
VxA= (3 26 a) + ug (% Bp (A-11)
1a 10A
+ u,|- > (pA) - = 2A]
[:2 can - 24
la ow law , dw
2, = at -- - a
vow ae ee + dz?
In spherical coordinates we have
ow 1 dw 1 dw
vu = weg + wer ag + Mersin oop
_loa,, 1 9 . 1 aA,
ViA= Ra’ Ay) + tin 000 (Aesin 6) + rsin 6 06
_ 1 fa ‘ aA,
VxA= ana | 3p (Ag sin 6) 2A
1 1 0A, to)
+ wee Es er aer Ay) | (A-12)
1fa oA,
+ uy E (rAe) - 2
1c@ ow 1 af... ,dw 1 o’w
2, = -- 5 ich See Pelee SS.
Vw = Fo (: 4) + sind (sin 7 “3) + ain? ag?
A number of useful vector identities, which are independent of the
choice of coordinate system, are as follows. For addition and multiplica

450 TIME-HARMONIC ELECTROMAGNETIC FIELDS
tion we have
A=A-A
|Al? = A-A*
A+B=B+A
A-B=B-A
AxXxB=-BXA (A-13)
(A+B)-C=A-C+B-C
(A+ B)xC=AxC+BxC
A-BxC=B-CxXxA=C-AXB
AX (B x C) = (A- C)B - (A-B)C
For differentiation we have
VQ + w) = Vo + Vw
vV-(A+B)=vV-A+V-B
vVx(A+B)=VxXA+VXB
: Vow) =v Vwt+ wv
V-(wA) = wV-A+A>Vw
Vv xX (WA) =wV XA--AX Vw (A-14)
v-(AX B)=B-VxA--A-VXB
VA=V(V-A)-VXVXA
VX (vVw) = W X Vw
Vx Vw=0
VivxA=0
For integration we have
[[[ v- Aa = fads
[[vxA-ds= gaa
[[[ vx Aa=-fpaxds (A-15)
[[f vwar = fhwas
[[ax vwds=fwa
Finally, we have the Helmholtz identity
, ,
4rA = -V WA aay x wx Aa (4-16)
pF rr
valid if A is well-behaved in all space and vanishes at least as rapidly as
1 at infinity.

APPENDIX B

---

## Appendix B: Complex Permittivities

COMPLEX PERMITTIVITIES
The following is a table of relative a-c capacitivities c} and relative
dielectric loss factors c’ where
gob =f jf ad Ke
€ €0 €0
is the relative complex permittivity. The measurements, along with
many others, were reported in ‘‘Tables of Dielectric Materials” (vol.
IV, Mass. Inst. Technol., Research Lab. Insulation, Tech. Rept.). They
also appear in Part V of ‘Dielectric Materials and Applications,”
Technology Press, M.I.T., Cambridge, Mass., 1954.

2 83/382 Noe lSelrmol|So}]/8e}]ee
2 6 2 13 °&] 8 ~_ a 4
= 0} at ia a + oT lo
r=) oe
sles /Se/8e}Fol/ag}/es|Sa lag] ::
x 2B | MALT ’ e;ea;tx{ i:
AN | oo ) a a o a ey fot
oO
=)
S iE i. alos ~ + 2
eg | ii] i ila, | se a8 Bo|/&g |g
xX} ad se rc a ae] s+ ot )ort
oO
vy soe fey ny sods mix °
© i} re} ° aw 12
Sle] r:/ Se] e283 [te] 22/68) Salasl es
3 en atila 5 PATIL TA | etl wo
eds
rs
3
fn ed a ny x co] ey a
*)log | 6Qleg)/F8] a4 = 00 7o | Cn | Aw] Rw
alg eer a ~ 6 -O | HO | ign - a
3 i i a a a aD ©
§ [ot a
~ le re} ry 8 nt rey ire) ro)
BLS] SS Fs #8) 44/88) s8]2alae les
8 at] ee lat ia at] an] roy o
B f-p
2
2 . ~o n o oe wQ re}
& |/S/}/nS/28}]*e/]44/88 :i]2ea|l&g/k&e,
= Ae loo) at la an fo] 8 iro) o
< o nb i ca red oO
Sime] eSlseQglae@lag -t/ NB law] Rs
aL ar lot| gol ago] wa DPifdeal] 6? ] or
alrelA2g/S8e]5n]/se] ::]ex8 Rx Re
i io : a7 oe : 2 - : 7a
a Kr} a®]la ot foe] OM] i o
« e|~2 6 ro) re a) Dip | ©
Sy;rsl esl SeSlsesl/Re] ::}/ gs} aslyrs
~ nN on ae a7 yt Dot =o woo om
we Pe Pe fo Pe Pe oe |S
“eS gi "es 2} "ss a 2 a =
1°) ey Sd © ed red ey x 1 12
| a a a a a a a a a a
: : : : : : ss : :
: : : : : : 3 : :
. . . . . : s . .
: : : : : # tg]:
: : : : : 2 q ig]:
3 q . - : = a 1 .
4 ae -_ : 3 : $ ad 18] g
7 7 & : a > a
3 Fi s > a} : 4 x g6| 5
3 fa Fe] 2 a a < coal aa | 5
a 3 a Fi P ls | |€2/4
B g 5 5 3 4 8 |
8 & = 3 = o a 6'giu
s 2 % a 3 Hy asg|s
3 a g 3 a 5 |
& 3 $ 8 a = |
2/2 |8 |2 |e |B lB {gs} 2
g Cy o a & 3 a au] &
< a () iS) 5 i) & o 1o

Re
~ 7 7
82/8. 8
: wa
at = : Jaelszlesla, |
= ao na mF :
ag : 2 gg ve | 8
RTs =:
>. rma} : i ts /Se|i:/8 Pasa
Se 8 an seal _- =F
=e ea Dit RS i.
a a : = = ,
be - | : ,
ae D a5 fila ---~ c 6 Fae
bipoi ag al :
"i en eae
Bo “3 Dot : = - .
= : ~oO y :
sgl i:fae|::f 2g o° g S85 a
= | ae Bg 8 [S58] o>]
aH 3 laelse| sel 8
a o 3S 12/2 tes
ow] os 8 ° at
~ So “oO oS = 23/23/83 a =f
Ze |S a8 = _
“8 a e|B8o g/ 8
a ey &s 28 x ~ ~
9 19 sx] 6 : : :
8g [Fl SR | : ols
2s atla ‘ae - =
a se 5B) 3 ee
Ss g|2 |
3s a8/ 8 -- ae/s./8. 8
Bo 2 a 3
N@
: |g #8) 23 5 | os 12
a - Qo Dol - oo ~ ; mw ’
uh - ~ wp 8+ sSlia
Ron 23 ae ln te mE
“sg a S rx ag 8
£2 wm oP las = :
8s 2a KR ~ Bo eo as = fe! tes :
z : ° a ty “y
a Re 5% | cs - ria
s|/aes solo te Ry <o? 2
ssises IN] 6S = Sy red z
m4 os a - - ty :
an ae : Sy ws =
s"loas ste |
a ~ ly a4 3 : :
~ tye ed Z :
ty 7 :
ty 2 [-0F Z : ,
Saeed 7 : , 2
ss eae : |
ws S - , :
2 : = | : :
ie] a hae | : : |
& a cee at : | :
= : : a : : : |
2 : : : , | : | |
: ' : a : : |
: : : a : : G Z :
: | ' 32 : fy < : 3
: : : d ao] : B |: | i
d' |s E | bel: 8 |B 2 \2
: : : £ gs : 4 e F
7 g 5 gs . F
: PR a 2 5 : ' :
: 3 7 Sg gsig = E : :
lz lz (8 ye |e iy
3 5 e a Ee g : :
3 > 3 3 BB : i
: 2
: a * 453
3 ey E
5 4
So}

x J = ic) oD
S/S} SB8/88 R4| 88 By
aia Yee Eas oy ant a
S$ 1 eee peeeitaee fet St- ee foe.) + ro) ed 2
eet srt: :/e@gi Re ]esl48/%3e)/S68
X av Gian ss fool aoMXMi atria AT | 9
oO
=) wQ Min | 2 33s soe . - + fag Gacy
Ba |X Bl]os seo era eae Coca ieee
x a 6 lig ny sees eee ete teal Dot
oO
Bile 3 Seize 21/2 Rin | ato :ifao
g|/ S| 2a |2a}oe beepers [eae seed pects <n Pee} a 5 2
8 ay wor 16% pees |e ara PEEL eg ter:
a
3 © a x oD ~ a rel n
gli e|ee/28/eg/e8g}/"+/2e)/ er] 83/98
gi 7a »P ] 0 ~ 9 go Teall jis at] a?
e
tag 2 oO Gb eo oD oe st Q [oz
S/S] 8e2)/eQ8/S58/5,/F"/SS/%*e|/SQ/a8
a cai . 2 BD : an 2S bd oS :
8 a re} rr) ~ oO ae] a a oa 8
J ” $a a
o
ae Om | @ to | 2 o a ~ ed Q
B/S eBlag =sleagihel(RBsl ss} egies
7 lant] wo wo] Co a s a oN
af R=} ~ re © 2 2 Re}
2/8"/Ss/ae]So/Relse}/~s/Reg]Sg
TlLat)o® | wm? ] a 69 Co. eed] anata AP | oo %
2 x 2 2 2 x ~
oS, oe as eB) es Ne e3 ~ as 8g
trator} wor] + 09 aaTs AA | oo
es o 5 2 2 wp a 2
2] Be) 38) 83 182) ka /a3\t5 (88/88
aT] oA] oa] aw? |] o oR Ts oO |
. Ps re a ‘ . > “s a 2 t a ty te oro fy ty > o
a eee:
> 19 2 8 12 2
B a a a a a & a & a
- : : : : : a 5 =e
eee
1 : 7 : : 5 : g
8 a a ‘4 7 : ies} : a
= 3 g g : : : e : g
3 bi 3 3 i : : : i)
5 3 8 ‘2 : i : 2 : 3
3 oO a ia : : : 2 ~ Cy
CI aq : : - 5 >
Ss C} 3 b : : n be is fo]
Br EI = Ee We ot WI - HM USAe
ne 2 z
g a i a : 8. =
of fe Ceres er penws
> : : 3 : 3 bo
c |3 lis 3 3 - 3 |e {38
Bs $ 2 a7 alls ee |
oO oS oS > Q S
a a a a e io a a a

isc) ic] ao oOo i=}
Se ee] ee/ sa] Ss) a8) 28] e8 | 8
at] oP la a a i) oO a =
22/838 )/8_)/Se]4,/4s/2o2/238/58 xg 2s
° i ; 4 ‘s]e
amr laa |a amt {Nf a a SR }/LXA[S a
: Jefe. a ran |e 12
a ‘ : _ ah a 3S Pe Se} a
ae ar fot fot oD m4 one ral a
apelepals RRR
Soleo to en °o a a.
SQISSfp rr i itaal Sal] i ilenleal - i lee
‘ a) Le ee : [i] BS ]/e@S]::/ se
28/8 a Dipa a a a a
as|/3ss|s Ss ie! s Diten | So] ti | ee
a oltaz!Se]o: : ae
“ei1csic ‘ Lt slos}] °:/8
om} tala 8 a a oaePan | Bad 2 Had '
oS Ooo isc} fox - oO i=} i=} a
33/83/88 So t = = 2g | NS 15 | woe
= 2 e 2 ° a ta ta} o @|BZa
ont awa] a rd a a a o-7|/2e|ar nn
Oo oo oO fez] ay oOo i=} oo ano soe S
eR les | oul Solin faaltal eel Ss]: i} es
oP | wala 3 & a a oul Ro q°: g
RBlHS| SH] Solin} sel Safl iif rrp rtyi:
oS] oS] a 3 a a a tae aed chad oy
om 22 | 2 roy a © 4 . a
BS SB/SiA] Sw trp ae} ae Dt vt tt aa
oN | ae] a oy - at' tam can 7 Dot Dot
o 2 ry Q 4 °o ° a 1. Py 7
22/S38/Sa/8a [tn] 8e] Se] cy rcf irda:
a®%|/o8]n 8 x alla ot ae ht ey:
Se] she he | Pe | te fhe Pte | he | ke | ote
TEL TELS yp rey re] re] rs pes pes [es pes
f=) rey wD a fred wn 1 1 »
1% : : : : :
n3 7 : : : :
ne re : : :
2 7 } : : t
fs Bac} § : : :
$8 7 3 : : :
as q 3 : a :
| a a : 3 :
g 7 : g :
2°83 ‘Ss 5 a Bas 8
Se i s a g 3
a Fs 3 o 3
a a a a > Ee

APPENDIX G

---

## Appendix C: Fourier Series and Integrals

FOURIER SERIES AND INTEGRALS
A periodic function f(z) with period a and satisfying the Dirichlet
conditions can be expanded in a Fourier series
f(x) = 224 a, COS 2am + b, sin 2nn (C-1)
2 ” a ” a
n=l
2 a
where an = a f(z) cos (ea *) dz
2 fe 2 (C2)
=f in (=
bn = 2 | f(x) sin ( az +) de
Such a series converges to f(z) at each point of continuity and to the
mid-point of each discontinuity. Also, a finite Fourier series (n < N)
is a least-mean-square error approximation to f(z). Alternatively, the
Fourier series can be written as
fx) = > Cnei2ntlae (C-3)
nse
1 [@
where a= ff saertoeton ae (C4)
A comparison of Eq. (C-1) with Eq. (C-3) reveals that
Cp = Gn - jbn (€-5)
Equation (C-1) is called the trigonometric form, and Eq. (C-3) the exponential form of the Fourier series.
Now consider a nonperiodie function, as represented by Fig. C-la. In
a given interval, say 0 < z < a, the function can be represented by Eq.
(C-1). However, outside the given interval, the series does not equal
J(z), but instead the series gives a periodic extension of f(x), as represented by Fig. C-1b. Moreover, we can represent f(x) in the interval
0 << <a in terms of a Fourier series of arbitrary period b > a, but the
. series will not be unique until we specify the manner of extending the
function beyond s = a. In particular, if we choose a period 2a and take

FOURIER SERIES AND INTEGRALS 457
a _-_--_25 0 2a *
(a)
_=a 0 a 2a
- x
(b)
=, a 2a
x
(c)
~
-a a 2a x
(d)
Fig. C-1. (a) A function can be represented in the interval 0 < x < aby (b) a “‘complete” Fourier series, (c) a Fourier cosine series, and (d) a Fourier sine series.
the even extension of f(x) from a to 2a, as shown in Fig. C-1c, we have the
Fourier cosine series
f(z) = a + » A, cos (2 ) (C-6)
2 a
n=l
where A, = i i f(z) cos (@ 2) dx (C-7)
a jo a
Similarly, if we choose a period 2a and take the odd extension of f(x) from
a to 2a, as shown in Fig. C-1d, we have the Fourier sine series
f(@@) = » B, sin (= ) (C-8)
n=1
1 [c . [nw
where B= = f(z) sin( - az) dz (C-9)
a Jo a

458 TIME-HARMONIC ELECTROMAGNETIC FIELDS

The representation of Eq. (C-6) converges to f(x) on the closed interval
0 <a <a, while Eq. (C-8) converges to. f(x) on the open interval
0<a2<a. Atx =Oandz =a, Eq. (C-8) converges to zero, which is
the mid-point of the discontinuity in the extended function (see Fig.
C-1d).

A function f(z) can also be represented as a superposition of sinusoidal
functions in an infinite interval, say -« <x < «. In this case, the
summation must be replaced by an integration, and we have

1 fe .
f(z) = al F(w)e? dw (C-10)
2n J-«
where Fw) = / f(a)e** dx (C-11)
The f(w) is called the Fourier transform of f(x). Equation (C-11) is
called the direct transformation, and Eq. (C-10) is called the inverse
transformation. Sufficient conditions on f(x) for f(w) to exist are
[CZ u@laz< © (C-12)
and f(x) satisfies the Dirichlet conditions. The inversion [Eq. (C-10)]
then converges to f(z) at all points of continuity and to the mid-point of
points of discontinuity. Fourier integrals corresponding to the trigonometric series of Eq. (C-1) also exist, but we shall not consider them here.

A useful relationship between the Fourier coefficients a,, b,, cn, and the

integral of |f(x)|? over its period, known as Parseval’s theorem, is
: 1 ? 2 2 1
-] | f(a)? dx = Jaol*+ 5 ) (lanl? + bal?)
aso 2
Eh: (C-13)
- > tat
This is readily proved by substituting for f(z) in the left-hand term from
Eq. (C-1) or (C-3) and interchanging summation and integration. All
cross-product terms drop out because of orthogonality. Similarly, for
the Fourier integral, we have a Parseval theorem
° 1 fe
[Citeor ar = % [7 ion aw (ca)
or, more generally,
° 1 f°
[tear ae = % [7 teorareo) ao (C-15)

FOURIER SERIES AND INTEGRALS 459
The proof of Eq. (C-15) is summarized as follows
[r@rma = [7 [de [tone ar]or@ ae
1 f[? ° .
= Lf. F(w) [. g*(x)ei"= as| dw
A similar generalization of Eq. (C-13) can also be given.

Finally, the impulse function (delta function) is useful in Fourier
analysis. By definition, the impulse function 6(x) satisfies the integral
equation

b agra (fe) a <a’

[0 1@ raz ~ {I z'<aorr’ >b (C-16)
for all f(z). It is evident that 6(x) is not a function in the usual sense,
but its use can be justified by rigorous means.! It is helpful to visualize
the impulse function as

1
5 73 <e< 5
a(x) = c (C-17)
0 |z| > 3
where c is an appropriately small number. Such a picture gives an
intuitive justification of Eq. (C-16). From Eqs. (C-11) and (C-16), it
follows that
Bw) = [7 deer dx = 1 (C-18)
that is, the transform of the 6 function contains all frequencies in equal
amounts. The inverse of Eq. (C-18) is
i / * ater dw = 3(z) (C-19)
Qn Jie
which is a particularly simple and useful result. Our use of (x) will be
primarily as shorthand notation for Eq. (C-17).

1L. Schwartz, “Th'orie des distributions,” Actualities scientifiques et industrielles,

nos. 1091 and 1122, Hermann & Cie., Paris, 1950-1951.

APPENDIX D

---

## Appendix D: Bessel Functions

BESSEL FUNCTIONS
Bessel’s equation of order v is
d dy 2 2) 4) =
ch (2H) + v)y = 0 (D-1)
Solutions may be obtained by the method of Frobenius, the result being
en (-1)"(x)?™+"
aalz) = > ali + 1D
nee (D-2)
2,5) tenes
Fala) = ) ate
where m! = I'(m + 1) in general. As long as » is not an integer, these
are two independent solutions to Bessel’s equation. However, when
v = nis an integer, we have
J_n(z) = (-1)"J (2) (D-3)
and Eqs. (D-2) are no longer two independent solutions. In this case a
second solution may be obtained by a limiting procedure. It is conventional to define another solution to Bessel’s equation as
N(x) = J (x) cos vm - J_»(x) (D4)
sin or
where, for integral v = n,
N(x) = lim N,(z) (D-5)
pon
This limit exists and establishes a second solution to Bessel’s equation of
integral order. The J,(z) are called Bessel functions of the first kind of
order v, and the N,(z) are called Bessel functions of the second kind of
order v,

BESSEL FUNCTIONS 461
Of particular interest are integral orders of Bessel functions. From
Eq. (D-2) and (D-5), one can determine
10 SRO
m=0 . (D-6)
m 2m
Mele) = Pog sate) +2 YO (2) gem)
meal
for the zero-order functions, and
= -4)" 2m-tn
TAQ) = ie wat eam (3)
n-1
Na(a) = 2 log 2 J4(2) - 3 > a ‘Cm (D-7)
m=0
-} S wig ast (Z) f4om) + 60m +m)
forn >0, where log y = 0.5772 (Euler’s constant)
y = 1.781 , (D8)
om) =1+4+K+Ht--° +5
The Bessel functions have been tabulated over an extensive range of
orders and arguments, and tables are available. Figure D-1 shows
1.0
oe tT Te EP eT eT
oot Nese aL UL | YT Up BUT ib a)
2
os epee | DA Te
ANN KOMP RLS
Lani N\A LMS NAVIN
oot | LV AIA DANAUS AN
MBAS: 2 Seeks
oe tae fee Loe dE Te ee
0 2 4 6 8 10 12 14 16
Fig. D-1. Bessel functions of the first kind.

462 TIME-HARMONIC ELECTROMAGNETIC FIELDS
0.6
os =) pel ve tt | f tt tt tT |
of VIX A MNS
[ER INAS AZDORINZ
nos PRT PTT
oa tl a=
otf VFI tT tT tT tT tt ttt YT
ott AA | | Et TT ET TT
-10 WEEE
-vlf/f | | | tt EE tT Et dE
0 2 4 6 8 10 12 14 16
Fig. D-2. Bessel functions of the second kind.
curves for the lowest-order functions of the first kind, and Fig. D-2 shows
those for the second kind. For small arguments, we have from the series
J o(x) = 1
2 (D-9)
Nae) mp Zoe’?
1l/fz\
and, forv > 0, J.(xz) -> -( =
z0 vu! ve »! /2\° (D-10)
Na) > - wat) (2)
z= a x
provided Re (v) > 0. For large arguments, asymptotic series exist, the
leading terms of which are
J,(x) - Vz cos (« - ; - a)
7 (D-11}
2. TUT
N.(z) => zz SD (: -4a7 r)
provided |phase (x)| < 7.
For the expression of wave phenomena, it is convenient to define linear
combinations of the Bessel functions
H,(x) = Jo(x) + JNo(2) .
H(z) = Jx(z) - jN«(z) (D-12)
called Hankel functions of the first and second kinds. Small-argument

BESSEL FUNCTIONS 463
and large-argument formulas are obtained from those for J, and Ny. In
particular, the large-argument formulas become

;
H(z) == ire
re (D-13)
(2) 4d je e-iz
H(z) = 2 e
which place into evidence the wave character of the Hankel functions.
Derivative formulas and recurrence formulas can be obtained by differentiation of Eqs. (D-2). Letting B,(x) denote an arbitrary solution to
Bessel’s equation, we have
Bic) = Boa - 2B,
* (D-14)
Biz) = -Buyr + 2B.
which, in the special case v = 0, become
Biz) = -Bi(z) (D-15)
The difference of Eqs. (D-14) yields the recurrence formula
Boz) = =p, Be (D-16)
which is useful for calculating B,(z), n > 1, from a knowledge of Bo(x)
and B,(z). The Wronskian of Bessel’s equation is often encountered in
problem solving. This is
Jel2)NE(a) - Nola)Si(a) = 2 (D-17)
from which Wronskians for other pairs of solutions can be easily obtained.
When x = ju is imaginary, modified Bessel functions of the first and
second kind can be defined as
I,(u) = j°J(-ju)
Ku) =F (sy H.(-ju) (P18)
These are real functions for real u. General formulas for J, and K, can
be obtained from the corresponding formulas for J, and H,. Figure
D-3 shows curves of the zero- and first-order modified Bessel functions.
The large-argument formulas, obtained from Eqs. (D-11) and (D-12),
ev
I,(u) - =
adie (D-19)
Tv
K,(u) = Vz e

464 TIME-HARMONIC ELECTROMAGNETIC FIELDS
illustrate the evanescent character of the
5 modified Bessel functions. Derivative
Fi et tb EA formulas and recurrence formulas can be
Ii | | | VA readily obtained from Eqs. (D-14) to
3 A D-16).
| V; (
' \ | | 4 | Bessel functions of ordern + 14 are used
\ Sees ip in the solution of the Helmholtz equation
1 N i herical coordinates. In scalar-wave
WO in spherica
BS=enn problems, it is conventional to define
* ba 3 spherical Bessel functions as
Fie. D-3. Modified Bessel r
functions. ba(a) = Vz Baiy(z) - (D-20)
The b, are given the name and letter as the corresponding Bnyy. (For
example, jn is the spherical Bessel function of the first kind, ha is the
spherical Hankel function of the second kind, etc.) In a-c electromagnetic field problems, it is convenient to define the alternative spherical
Bessel functions
B,(z) = BS Briss() (D-21)
where B, is given the same name and symbol as the corresponding Bays.
The various formulas for 6, and B, can be obtained from the corresponding formulas for Bay. Of particular interest is the fact that asymptotic
expansions for Bay become exact, giving
J,(z) = C(x) sin (« - =) + D,(z) cos (« - =)
N(x) = Da(z) sin (« - a) - C,(z) cos (« - 5) (D-22)
A(z) = j-*[Da(z) - 5Ca(2)]e*
#,(x) = jo[Da(z) + jCa(x)le*
2m<n
-1)"(n + 2m)!
hi = ¥ _(-))" + 2m)1__
where Caz) bf Gimy Kn - Dm) lon)
2m<n--1 “ (D-23)
D(x) = (-))"( + 2m + D)!
ye A (2m + 1)'(n - 2m - 1)1(2z)?"*1
Note that A(x) -> jhe (D-24)
which is of interest in radiation problems.

APPENDIX E

---

## Appendix E: Legendre Functions

LEGENDRE FUNCTIONS
The associated Legendre equation is
1 d/.. ,dy m? _
ang ao (sin oft) + [oe +) - sno | y=0 (E-1)
This can be put into another common form by using the substitution
u = cos 0 (E-2)
in Eq. (E-1). The result is
d’y dy m2
pantee TT h pecesee_Acgnaans at -_ -- = i“
(1 - wu?) det 2u qu + [ve +1) rT | y=0 (E-3)
: When m = 0, the associated Legendre equation reduces to the ordinary
Legendre equation
a d
(1 = w) 54 - 2u 54 + ow + yy =0 (E+)
We shall first consider solutions to this special case and later generalize
to the associated Legendre equation.

In the spherical coordinate system, 0 < @ < 7;s0 we shall be interested
in solutions over the range -1 < u <1. In particular, for |1 - u| < 2,
the Legendre function of the first kind can be expressed as

N
_ (-1)™(v + m)! (1 - u\”
P.(u) = » “ml = m)t (2
m=0
sin vr (m-1-v)\m+)!(/1 - u\” _
337 » --taiyr a) 5)
m=N+1
where WN is the nearest integer N < v. As long as» is not an integer,
P.(u) and P,(-u) are two independent solutions to Legendre’s equation
[Eq. (E-4)]. If v =n is an integer, Eq. (E-5) becomes a finite series
called the Legendre polynomial of degree n. In this case,
P,(-u) = (-1)"Pa(u) (E-6)

466 TIME-HARMONIC ELECTROMAGNETIC FIELDS
and we no longer have two independent solutions. Another solution,
called the Legendre function of the second kind, is defined as
_ @ P,(u) cos vm - P.(-u)

Qu) = 5 - (-7)

When v = nis an integer, the limit
Q,(u) = lim Q,(u) (E-8)
von

exists and defines a second solution to Legendre’s equation.

The Legendre polynomials are of particular interest, because these are
the only solutions finite over the entire range 0 < @ <7. In this case,
only the first summation in Eq. (E-5) remains, which can be rearranged to

M
_ (-1)"(2n - 2m)! 2m
Pau) = » 2min - myn - Im)!“ (E-9)
m=0
where M = n/2 or (n - 1)/2, whichever is an integer. An alternative,
and sometimes more convenient, expression for the Legendre polynomials
is given by Rodrigues’ formula
= 1 da" 2 nm
P,(u) = Fat dur (uw? - 1) (E-10)
Some of the lower-degree polynomials are
Pou) = 1 Pru) =u Pa) = 487-1) yyy
P3(u) = W(5u? - 3u) Pa(u) = 1@(35u4 - 30u? + 3)
or, in terms of 6,
P (cos @) = 1 P,(cos 6) = cos 6
P2(cos 0) = 14(3 cos 26 + 1) (E-12)
P3(cos 6) = 14(5 cos 36 + 3 cos 6)
P,(cos 6) = %4(35 cos 46 + 20 cos 26 + 9)
Figure E-1 shows curves of the Legendre polynomials plotted against 6.

The Legendre functions of the second kind for integral v = n are infinite

at @=Oand @6=-7,oratu= +1. They can be expressed as
1
Qn(u) = Pa(s) | 46 og FES - om) |
(=1)"(_ + m)! 1-u\"
+ Y) Sprott gem (15-4)" es)
m=)

LEGENDRE FUNCTIONS 467
1.0 J
No eee Ty
“ARQ 7
ac AST eh Ar
el
oat WRAL TAL YY
at WAL VINEE
A, wan \
@ UN PVA AT
& Vo les
ae LAAT AN ive
on eat RAT
SERS aAL eis
- 06
RESERVES
-~ 08 NIX
cae TEESE
Fie. E-1. Legendre functions of the first kind, P.(cos @).
where c(m) is defined by Eq. (D-8). Some of the lower-order functions
are
1 1+
Qa(u) = 34 logtF* Que) = Flog = 1
2 (E-14)
Qi(u) = 3M =1pogitu_ du
, 4 I-u 2
or, in terms of 6,
Qo(cos 6) = log cot 7 Q:(cos 6) = cos 6 log cot gL 1
2 5 2 (E-15)
Q.(cos 0) = 14(3 cos? 6 - 1) log cot 5 - % cos 6
Figure E-2 shows curves of these functions plotted against 0.

Now consider the associated Legendre equation, Eq. (E-3). For
simplicity, we first take ,. to be an integer. If Eq. (E-4) is differentiated
m times, there results

a -w 4 -2umt yn 24 ~-mntms |Z =0
du® du du™
Letting w = [(1 - u)™] d™y/du™ in the above equation, we obtain Eq.
(E-3) with y replaced by w. Hence, solutions to the associated Legendre
equation are!
1 Smytheand others omit the factor (-1) on the right-hand side of these definitions.

468 TIME-HARMONIC ELECTROMAGNETIC FIELDS
Pam(u) = (-1)m(1 - weynle SP alo
i (E-16)
Qar(u) = (=1)m(1 = wtyer POLY
” du™
Note that all P,”(u) = 0 form > n. Some of the lower-order associated
Legendre polynomials are
Py(u) = -(1 - u*)* P3\(u) = 34(1 - u?)4(1 - 5u?)
P2(u) = -3(1 - u?)4u P3(u) = 15(1 - w)u (E-17)
P2(u) = 3(1 - u?) P3(u) = -15(1 - u?)*
while the P,,°(u) = P,(u) are given by Eq. (E-11). Some of the lowerorder associated Legendre functions of the second kind are
1+u u
= -(1 - yu) aU Sas
Qt = -a - uy (4 toe EY + S)
l+u, 3w--2
Q! = C= wy (s4utog AE 4 SEF) es)
ltu, 5u-3w
2=- (1 - u»%] 3 SES ges pale
at = a wy [36 log EY 4 |
while the Q,°(u) = Q,(u) are given by Eq. (E-14).
When m is not an integer, the situation becomes even more complicated. A standard formula for Legendre functions of the first kind,
TTT
ASE 4
NC |
INNS
Ss 2
4 @
oi | INS
EEL ET ETT A
TI SET
-4
-5
Fia. E-2. Legendre functions of the second kind, Qn(cos 6).

LEGENDRE FUNCTIONS 469
valid for [1 - u| < 2, is then
sin wr ut 1\7/2 l-u
P.°(u) = -- (w- nets) P( =n» 4+1,1-v, 15*) (E-19)
where F is the hypergeometric function
(y= 1)! y (a + m)\(@ + m)!
=] SSN Se xe eee TO gmt) s'
F(a,8,y,2) + @-pw@-1! , milly + m)! 2 (E-20)
For real u, the associated Legendre function of the second kind is defined
as
wi) - 7 Po®(u) cos (v + w)r - Po*(-u)

Q.°(u) = 2 sin (v + w)r (E-21)
The solutions P,”(u) and P,”(-w) are linearly independent, except when
u+ wisaninteger. In this latter case, the limit of Eq. (E-21) provides
a second solution.

Perhaps the simplest way to calculate the Legendre functionsis through
the recurrence formulas. Letting L,™(u) denote an arbitrary solution to
the associated Legendre equation, we have

(m - n - 1)L™,, + (2n + 1)uL,™ - (m+ n)Ip_, = 0 (E-22)
A recurrence formula in m also exists and is
Lantt ee + (m+ n)(n- m+ VL) =0 (E23)
for the range |u| < 1. Many formulas for derivatives also exist, some of
which are
Lat"(u) = pa [- nua + (n+ mea]
1
=To we [(n + 1)uL,.™ - (n - m+ DLR
_ mu rm 4 MH mn - mt V7 (E-24)
~~ = (1 - u?)# ™
mu 1
-'-_- m m+
_ Tow Towel ,
If m = 0 in the last formula, we have
Lu) = -(1 - u)¥L;(u) (E-25)
which is a useful special case.
Finally, some specializations of the argument will be of interest to us.

470 TIME-HARMONIC ELECTROMAGNETIC FIELDS
At 6 = 0, that is, at u = 1, the Q,” functions are infinite and
w/e (§it m=0
P,™(1) = (s m>0 (E-26)
At 6 = 1/2, that is, at u = 0,
1:3:5:+-:-™M+tm-1)
-Jjmtm 2298 rm = 4)
P,m(0) = (-1) 2-4-6°° Wm) n+ m even
0 n +m odd
0 n + m even
Qn™(0) =} (yy tntmtnt 2476 (m+ m - 1)
( 1) 1°3-5---(™m-m) n + m odd
i (E-27)
Some specializations involving derivatives are
. a
[Peo] = (vPro)
” ‘ae (E-28)
Om = (-1)'Q."47
[mer |= vero

---


---

*Notes generated from: Harrington R.F., "Time-Harmonic Electromagnetic Fields", IEEE Press*

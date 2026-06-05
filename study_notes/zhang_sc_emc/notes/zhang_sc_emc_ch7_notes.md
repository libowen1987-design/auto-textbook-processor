# Zhang《Spacecraft EMC Technologies》第7章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 7. Typical Spacecraft Electronic Component Selection and Module EMC Design

Chapter 7
Typical Spacecraft Electronic
Component Selection and Module EMC
Design
7.1
Selection of Typical Electronic Components
and Modules
7.1.1
Resistor
Resistors are the most commonly used electronic products, which can be divided
into three types by material, namely, composite carbon ﬁber, wirewound type, and
ﬁlm-type resistors. Wirewound resistors and ﬁlm chip resistors are more often used
in the space ﬁeld. Regardless of the resistor type, due to the presence of terminal
inductance and parasitic capacitance, their characteristics are different from an ideal
resistor in actual application. The equivalent resistor model in practical application
is shown in Fig. 7.1, where Ll is the lead inductance of the resistor, Cp is the parallel
combinationofaleadcapacitorandleakagecapacitor.Figure7.2showsthefrequency
characteristics of a resistor.
In Figs. 7.1 and 7.2, R is the resistor impedance in ; Ll is the lead inductance
(typical value is 5nH–15nH) in H; and Cp is the parasitic capacitance (typical value
is 1pF to 2pF) in F.
From the frequency characteristics of the resistor in Fig. 7.2, the characteristics
of the resistor and the ideal resistance are the same before the frequency is
1
2\piRC p .
After crossing the frequency
1
2\piRC p , as the frequency increases, the impedance of
the resistor decreases, which reﬂects the characteristics of a capacitor. At the reso-
nant frequency point
1
2$\pi$\sqrt
LlC p , the impedance of the resistor is the smallest. If the
frequency is higher than this resonant frequency, as the frequency increases, the
impedance of the resistor increases, which reﬂects the characteristics of inductance.
Wirewound resistors can withstand higher power than the ﬁlm chip resistors,
but they are made of wires that have signiﬁcant inductance characteristics at high
frequencies. From the circuit function perspectives, the inductance characteristics
of the wirewound resistor are acceptable, but from the EMC point of view, it may
cause RE or CE problems. The ﬁlm resistor is formed by placing a metal ﬁlm on
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_7
229


230
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.1 HF equivalent
model of resistor
Fig. 7.2 Resistor frequency
characteristic curve
an insulating substrate, and the ﬁlm chip resistors have good HF characteristics,
mainly in that it not only has the structural characteristics of the ﬁlm resistor, but
also eliminates the resistance lead. Therefore, if the resistance and power satisfy the
requirements, a ﬁlm chip resistor with a relatively small parasitic inductance and a
parasitic capacitance should be preferred.
7.1.2
Capacitors
Similar to resistors, there are many types of capacitors. For the purpose of suppressing
EMI, the more often used capacitor types are ceramic capacitors and tantalum elec-
trolytic capacitors. Tantalum electrolytic capacitors can achieve large capacitance
values in a small package, but their HF characteristics are not ideal. Therefore,
tantalum electrolytic capacitors are often used for interference suppression of CE. In
comparison with tantalum electrolytic capacitors, ceramic capacitors have a smaller
capacitance but maintain ideal characteristics at very high frequencies. Therefore,
ceramic capacitors are often used for interference suppression of RE.
The equivalent capacitor model in practical application is shown in Fig. 7.3,
where Ll is the lead inductance and RS is the equivalent series resistance. Figure 7.4
shows the frequency characteristics of the capacitor. It can be seen that as the
Fig. 7.3 HF equivalent
model of capacitor


7.1 Selection of Typical Electronic Components and Modules
231
Fig. 7.4 Frequency
characteristic curve of
capacitor
frequency increases, the impedance of the capacitor decreases linearly at a rate of −
20 dB/decade until the frequency point
1
2$\pi$\sqrtLlC , where the capacitive reactance of the
capacitor and the inductive reactance of the capacitive parasitic inductance are equal.
It is called the self-resonant frequency point of the capacitor. When the frequency
is higher than this point, the inductive reactance of the parasitic inductance of the
capacitor becomes a major part of the capacitance impedance and increases with the
frequency at a rate of +20 dB/decade.
In Figs. 7.3 and 7.4, C is the capacitor capacity in F, Ll is the lead inductance
(typicalvalueis5–20nH)inH,andRS istheequivalentseriesresistance(typicalvalue
of tantalum electrolytic capacitor is 2–8 , and that of the chip ceramic capacitor
can be ignored) in .
In the spacecraft application of ceramic capacitors and tantalum electrolytic
capacitors, the following should be considered:
(1) Chip ceramic capacitors with good HF characteristics is preferred;
(2) The capacity value of a single capacitor should not be too large; multiple
small-capacity capacitors are preferred to be used in parallel to improve HF
characteristics;
(3) For parallel capacitors used for bypassing noise currents, their impedance should
be lower than the impedance of their parallel circuits.
7.1.3
Inductors
The equivalent inductor model in practical application is shown in Fig. 7.5, where
Cp is the parasitic capacitance of the inductor (depending on the winding of the
inductor) and Rp is the equivalent series resistance. Figure 7.6 shows the frequency
characteristics of the inductor. The resistance is dominant at low frequencies, and as


232
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.5 HF equivalent
model of the inductor
Fig. 7.6 Frequency
characteristic curve of the
inductor
the frequency increases, the inductor begins to be prominent at
Rp
2\piL ; the impedance
increases at a rate of +20 dB/decade. As the frequency further increases, at the
frequency
1
2$\pi$\sqrt
LC p , the inductance of the inductor and the capacitive reactance of
the inductor parasitic capacitance are equal. This frequency point is called the self-
resonant frequency point of the inductor. When the frequency is higher than this point,
the capacitive reactance of the inductor parasitic capacitance becomes the main part
of the inductance impedance and decreases with the increase of the frequency at a
rate of −20 dB/decade.
In Figs. 7.5 and 7.6, L is the inductance of the inductor in H, Cp is the parasitic
capacitance (typical value is 2–10pF) in F, and Rp is the equivalent series resistance
in .
In spacecraft applications of inductors, the following design principles should be
followed:
(1) CM inductor cores generally use high magnetic permeability ferrite cores,
and DM inductor cores generally use low magnetic permeability iron–nickel–
molybdenum or iron–silicon–aluminum cores;
(2) The inductor is preferably wound in a single layer, and a certain space should
be left between the turns. In cases where the laminate must be used, it should
be superimposed while winding, try to avoid superimposing the second layer
after the ﬁrst layer;


7.1 Selection of Typical Electronic Components and Modules
233
(3) There must be a certain isolation space between the input and the output ends
of the inductor, so as not to cross or entangle them;
(4) Series inductors used to suppress interference currents should have a designed
impedance higher than the impedance of their series circuit.
7.1.4
Semiconductor Discrete Components
The commonly used semiconductor discrete components in spacecraft are the diodes
and ﬁeld-effect transistors (FET).
Diodes do not cause serious EMI problems in most applications. However, the
rectiﬁer diode in the DC/DC converter is one of the main interference sources because
its function is to rectify the switching signal. If the rectiﬁer diode is a fast recovery
diode, when the diode current is reversed to zero, the current waveform will produce
sharp edges, resulting in higher current spectral components and causing EMI. There-
fore, when selecting rectiﬁer diodes, it is recommended to select diodes with a
smoother reverse current waveform. Schottky diodes are preferred if the voltage
and current parameters meet degradation criteria.
TheFETisoneofthecorecomponentsintheDC/DCconverterandisalsothemost
important interference source. In a DC/DC converter, when the FET is switched ON
and OFF continuously, the harmonic component of the switching frequency becomes
an interference source, and a wide spectral component is generated. Since the inter-
ference spectrum component generated during the switching operation depends on
the rise and fall time of the pulse, and the rise and fall time of the pulse waveform
should be maximized in regard to EMC. If the voltage and current meet the degrada-
tion criteria, it is preferred to select FET switch tubes with shorter rising and falling
edge and shorter storage time. Note that the rise and fall time can only be increased
within a limited range; a big increase will result in excessive power consumption of
the FET switch tube, which will cause serious heat dissipation.
7.1.5
Transformer
Transformers are used in many electronic applications, but are mainly used in
DC/DC converters of electronic equipment. The transformer design should follow
the following principles:
(1) Under the premise of satisfying the structure and layout requirements of the
converter, select the core in the preferable sequence of the can-shaped core,
rectangular module (RM) core, toroidal core, and E-shaped core. When using
an E-shaped core, select that with a long shape (longer middle column), and
reduce the number of winding layers as much as possible to reduce the leakage
inductance of the transformer and the distributed capacitance of the winding.


234
7
Typical Spacecraft Electronic Component Selection …
(2) For transformers using a skeleton, the primary winding of the transformer (or a
part of the primary winding) is wound close to the innermost layer of the skeleton
to minimize the length of each turn and reduce the distributed capacitance of
the primary winding.
(3) For converters with higher power, the transformer design should preferably use
the winding scheme of a sandwich structure that divides the primary winding
into two halves.
(4) If the area of the core window permits, one option that can be considered is to add
a shield between the primary and secondary windings of the transformer. The
shield should be as short as possible, wider than the windings, and connected
to the primary winding.
(5) The lead wire of the transformer should be as short as possible.
7.1.6
Digital Circuit Devices
The rise time of the pulse waveform of a digital circuit device determines the amount
of its HF component, the shorter the rise time, the wider the frequency band of the
HF component. These HF harmonic components will radiate interference through
the antenna effect of the printed lines on the PCB. In addition, the inherent voltage
change rate (dV/dt) of the voltage waveform, together with the interaction of para-
sitic capacitance, produces CM CE interference. Table 7.1 shows the performance
parameters of the rise time and voltage change rate for three types of digital circuit
devices. From Table 7.1, CMOS 5 V logic devices have the longest rise time and
the lowest voltage change rate. Therefore, under the premise of meeting the circuit
performance requirements, the CMOS 5 V series are preferable to be used in the
logic device, which can limit the HF harmonic components to the maximum extent.
7.2
Functions, Components, and Features of Power Supply
and Distribution Electronics Equipment
According to the functions of different equipment, the spacecraft is divided into
multiple subsystems so as to meet the speciﬁc requirements of the mission. The
power supply and distribution electronic equipment generally belong to the overall
Table 7.1 Rise time and voltage change rate of different digital devices
Type of logic devices
Rise time (ns)
Voltage ﬂuctuation (V)
Voltage change rate dV/dt
(V/ns)
CMOS 5 V
100
5
0.05
CMOS 15 V
50
15
0.30
TTL
10
3
0.30


7.2 Functions, Components, and Features of Power Supply …
235
circuit subsystem. In general, the input of this equipment is connected to the power
subsystem—the power conditioning unit (PCU)—and is responsible for converging
and voltage—converting the power output from the power system; the output of
this equipment is connected to the spacecraft load equipment, providing stable and
reliable power for the spacecraft platform and load equipment, and functions as a key
link between the upper and the lower equipment. There are a large number of power
supplies and distribution equipment, which usually use standardized, modular, and
generalized designs to reduce the types of equipment and improve the generalization
and productization.
Thefunctionofearlypowersupplyanddistributionelectronicequipmentismainly
to converge and redistribute the power output from the power system. The internal
part of the equipment is basically composed of wires and relays. The wires are the
transmission paths, and the relays are used to control the switching of the power
supply paths. The power required by the command bus for relay action and by the
equipment state telemetry is all provided by external devices. Because the function
of early power supply and distribution electronic equipment is relatively simple, and
almost no internal active device is set, there is a low probability of EMI problem.
With the increased functions and tasks of the spacecraft, the power supply and
distribution equipment with only the power supply control function can no longer
meet the mission requirements. Figure 7.7 shows the block diagram of the current
spacecraft power supply and distribution equipment. A centralized power distribution
system is adopted. The equipment is not only responsible for distribution and control
of the 100 V primary bus generated by the power system, but also for converting the
100 V primary bus voltage into the required 28 V secondary bus voltage for the load
and the required 5, \pm12 V voltage inside the equipment, and performs the same power
supplycontroltothe28Vpowerdistributionpaths.Thepowersupplyanddistribution
Fig. 7.7 Block diagram of the spacecraft power supply and distribution equipment


236
7
Typical Spacecraft Electronic Component Selection …
equipment become a load of the primary bus on one hand, and the source of the
secondary bus on the other hand. Besides, unlike the analog telemetry transmission
of the early power supply and distribution equipment, the current equipment is also
installed with a data acquisition unit, which realizes the serial digital communication
of the measurement parameters and the data management subsystem (DMS).
The current spacecraft power supply and distribution equipment generally consist
of a power distribution unit, a power conversion unit, and a data acquisition unit.
The power distribution unit realizes the power OFF-and-ON sequence control of
each system load; the power conversion unit converts the primary bus voltage into
the secondary bus voltage required by the load; the data acquisition unit automat-
ically collects, processes, and communicates various status data. Each functional
module works in coordination to ﬁnally realize uniﬁed conﬁguration, management,
and control of spacecraft load power supply.
The power supply and distribution equipment need to realize power conversion,
and isolation between the primary and secondary buses is also required, so a DC/DC
converter is essential. However, due to the working principle of its switching circuit,
the DC/DC converter becomes a strong EMI source in the device.
The data acquisition unit (Fig. 7.8) is typically composed of an analog switch, an
A/D converter, a microprocessor and its peripheral circuits, and a serial communi-
cation port. During operation, select one-way analog switch to lead the signal to be
tested to the A/D converter and convert it into a digital amount, then the micropro-
cessorprocessesthedigitalamountandstoresitinthedataareaofthemicroprocessor,
and transmits it through the serial digital channel to the data management subsystems.
Therefore, the data acquisition unit is mostly composed of digital circuits, which are
both interference sources and EM sensitive areas.
Because the primary bus (100 V high voltage) and secondary bus (28 V low
voltage), analog circuits, and digital circuits often coexist in the spacecraft power
supply and distribution equipment, it is necessary to strengthen its EMC design
according to the EMI characteristics of the devices and the circuits.
7.3
EMC Design for Power Distribution Unit
The power distribution unit of the power supply and distribution equipment mainly
includes components such as relays, surface mount resistors, and capacitors. In
steady-state operations, since the relay does not actuate, it is equivalent to a resistive
line and will not become an EMI source. However, at the moment when the relay
is turned ON and OFF, due to its inductance characteristics, a voltage is generated
on the line package in order to maintain the original current of the line package,
and the voltage direction is opposite to that of the command (also called reverse
electromotive potential), and the size is equal to LdI/dt, where L is the inductance
value of the line package. As can be seen from the formula that the faster the line
package current changes, the larger the reverse electromotive force is, this will cause
damage to the equipment directly added to the command end equipment. Therefore,


7.3 EMC Design for Power Distribution Unit
237
Analogue 
Analogue 
switch 2
switch 3
Analogue 
switch 1
A/D converter
Microprocessor 
Watchdog 
Power-on reset 
circuit
Program 
memory
Data memory
Serial 
communication 
pot circuit
Fig. 7.8 Block diagram of the data acquisition unit
it is necessary to place a de-reversing circuit in the relay line package to limit the
reverse electromotive force. The de-reversing circuit will provide a loop for the line
package current to reduce the line package current dI/dt, thereby suppressing the
magnitude change of the reverse electromotive force.
There are usually two ways to suppress the reverse electromotive force generated
aftertheexcitationsignaloftherelaycoildisappears.Oneistoparallelconnectdiodes
at both ends of the relay coil, which can better suppress the reverse electromotive
force, but the coil energy decays slowly. The other is to parallel connect diode series
resistors at both ends of the relay coil, which have poorer suppression effect to the
reverse electromotive force compared with the ﬁrst method (the suppression effect
depends on the resistance value), but the winding energy decays faster. Generally, for
monostable EM relays, the second measure should be taken to shorten the response
time of the relay. For a bistable magnetic holding relay, the winding energy decaying
speed has no effect on the response time of the relay. Generally, the relay in the power
distribution unit is a magnetic holding relay, so the ﬁrst method is used to suppress
the transient interference generated by the relay.
In power supply and distribution equipment, the relay coil is mostly driven by a
switching transistor. When the transistor switch intercepts the current I through the
inductor, the inductor kicks back or the Faraday voltage across the inductor shorts
the diode. Thus, the diode clamps the collectors of the transistor to +Vcc, preventing
large collector-emitter voltages from damaging the transistor. The rapidly rising coil
current will ﬂow in the loop formed by the coil and the diode. In order to reduce


238
7
Typical Spacecraft Electronic Component Selection …
the RE of the current loop, the distance between the relay coil and the parallel diode
should be minimized, as shown in Fig. 7.9.
In the power supply and distribution equipment, there are generally two ways
to acquire the relay state telemetry: one is realized by the auxiliary contact of the
relay itself, the other is the indirect characterization of the relay state by the state of a
parallel small relay. Taking relay’s own auxiliary contact as a telemetry circuit has the
risk of short-circuiting of the telemetry circuit with the main circuit contact. In HV
power distribution, this risk is extremely hazardous to the safety of the spacecraft.
The use of a parallel small relay can effectively avoid this risk, but because the large
and small relay coils are connected in parallel, when the large relay is actuated, it
will interfere with the small relay, causing it to reverse. The reasons and the solution
will be discussed in the following paragraphs.
Figure 7.10 shows the schematic diagram of a typical magnetic holding relay
Fig. 7.9 Current loop
formed when the relay is in
operation
Switching 
transistor
Relay coil
Vcc 
Fig. 7.10 Diagram of
magnetic holding relay
connecting to a de-reversing
circuit
L
*
*
L
+
-
+
-
Set line package
Reset line 
package
Off 
Command Bus
Diode 
Diode 
On 


7.3 EMC Design for Power Distribution Unit
239
control with a de-reversing circuit. If a command is applied to the relay set (On) line
package, the inductance characteristic of the package at the end of the command will
(1) generate a left-positive right-negative reverse electromotive force on the set (On)
line package, and the reverse electromotive force is reversed through the diode
series circuit;
(2) due to the magnetic coupling relationship inside the relay, a right-positive left-
negative induced electromotive force is coupled to the relay reset (Off) line
package.
As can be seen from the actual test chart (Fig. 7.11), when the command bus is at
29 V, at the instant of the end of the command, the coupling voltage generated by the
set line mutual inductance coupling to the reset line package can reach about 10 V.
In a single relay circuit, the coupled induced electromotive force on the reset (Off)
line package is reversely turned OFF by the diode of the de-reversing circuit, and
there is no current in the de-reversing loop of the reset circuit, and no effect on the
relay. However, in the parallel circuit with large and small relays, the line package
of the small relay provides a bleeding path for the coupled induced electromotive
force on the large relay reset (Off) line package, as shown in Fig. 7.12. When the
amplitude and duration of the induced current i reach the critical value of the small
Fig. 7.11 Coupling voltage waveforms between the set and reset line packages of the magnetic
holding relay


240
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.12 Electrical
principle of small relay state
change
Command 
bus 
Diode 
Diode 
Off 
On 
Parallel small relay 
Reset line package
Set line package
Set line package 
Reset line package
Large relay
relay actuating current, the state of the small relay will be reversed, causing the
problem of inconsistent state of the large and small relays.
The simplest way to suppress this undesired induced current is to connect diodes
before the large relay coils. The anode of the diode is connected to the command bus,
and the cathode is connected to the relay coil. At the end of the command, the series
diode in the non-command coil is reverse-cutoff and breaks the interference current.
This method can not only block the interference current of the non-command coil at
the end of the turned-on command, but also ensure the parallel circuit of the large
and small relays to receive commands normally. The electrical schematic diagram is
shown in Fig. 7.13.


7.4 EMC Design of the DC/DC Converter Module …
241
Fig. 7.13 Electrical
principle of the induced
current suppression method
Command 
bus 
Diode  
Diode  
Off 
On 
Parallel small relay 
Reset line package
Set line package
Set line package
Reset line package
Large relay
7.4
EMC Design of the DC/DC Converter Module (EMI
Interference Analysis, Absorption Circuit Filter Design)
7.4.1
EMI Interference Analysis
The DC/DC converter module is composed of several DC/DC converters. The EMC
problem of the DC/DC converter is mainly due to the dv/dt and di/dt generated by
the switching action of the power semiconductor device. Figure 7.14 shows an HF
equivalent model of a DC/DC converter containing the LISN and parasitic parame-
ters. In the ﬁgure, Cds is the parasitic equivalent capacitance of the MOSFET, Cp is
the stray capacitance of the diode negative to the case, Cde is the stray capacitance
of the D-pole of the MOSFET to the casing, Ct is the stray capacitance between the
primary and secondary sides of the transformer, Cj is the diode junction capacitance,
Lep is the leakage inductance of the transformer primary stage to other windings,
and Les is the leakage inductance of the transformer secondary to other windings;
these parasitic parameters not only generate conducted interference current, but also
provide the corresponding conducted interference paths. In addition, there are two


242
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.14 HF equivalent model of DC/DC converter containing LISN and parasitic parameters
kinds of conducted interference in DC/DC converters: one is the switching harmonic
component of the switching action of the power semiconductor device, the other is
the oscillation due to the inﬂuence of parasitic parameters.
7.4.1.1
Switching Harmonic Components
In the DC/DC converter (refer to periodic signal spectrum envelope of digital circuits
in Sect. 2.1.2), when the MOSFET and the rectiﬁer diode are turned ON and OFF
continuously, a wide spectral component is generated. The harmonic component
of the switching frequency becomes the main interference source, its spectrum is
shown in Fig. 7.15. As can be seen from Fig. 7.15, the frequency bandwidth of the
switchingsignalisapproximately1/\pitr.Anincreaseoftr canreducetheHFharmonic
dBµV
Fig. 7.15 Switching frequency spectrum


7.4 EMC Design of the DC/DC Converter Module …
243
components of the switching frequency. In the design of a DC/DC converter module,
the value tr depends largely on the turn-on and turn-off rate of the MOSFET, so when
selecting a MOSFET, try to select the one with a lower turn-on and turn-off rate so
that the switching signal has less HF harmonic components.
7.4.1.2
Oscillation Interference
When the MOSFET and the rectiﬁer diode are turned ON and OFF continuously,
due to the inﬂuence of parasitic parameters, it will generate an oscillation effect
and result in interference. The interference current generated by the oscillation is
shown in Fig. 7.14. When it is detected by the LISN, it is possible to generate an
out-of-standard point when performing the conducted interference test.
The interference current generated by the oscillation can be classiﬁed into DM
and CM currents according to different conducted paths. The interference current
between the lines is the DM interference current, and that between the lines and the
ground is the CM interference current. Different methods are used for the suppression
of different types of interference currents.
1. Analysis of oscillation interference generated by MOSFET
When MOSFET is turned OFF, an oscillation effect occurs due to the inﬂuence of
parasitic parameters. When the switch Q1 is turned OFF and the secondary diode D1
is turned ON (loaded), the excitation inductance of the primary side is clamped, and
the energy of the primary leakage Lep is discharged through the parasitic capacitance
Cds of Q1. The main discharge loop is Lep-Cds-C1-Lep, oscillation occurs at this
moment, the oscillation frequency is
fmos =
1
2$\pi$\sqrtLepCds .
(7.4.1)
This is an attenuated oscillation wave whose initial oscillation peak is determined
by the Q value of the oscillation circuit:
Q =

L

C
R
.
(7.4.2)
The larger the Q value, the larger the peak value. In order to reduce the peak value,
the leakage inductance Lep of the transformer should be reduced, the Cds and the
circuit impedance R should be increased.
(1) CM interference current path
The MOSFET turn-on and turn-off produce an oscillation effect, and its CM inter-
ference path is shown in Fig. 7.16. A part of the interference current generated by
the oscillation is conducted from the parasitic capacitance Cde between the D-pole


244
7
Typical Spacecraft Electronic Component Selection …
D1
C2
Ct
Cj
C1
Cds
Cde
50Ω
50Ω
LISN
Cp
To Load
Q1
D
S
G
Lep
Les
CASE
Fig. 7.16 MOSFET CM interference paths
of the MOSFET and the casings to the casing, the positive line and the return line are
separated at the LISN (the CM current is detected in the CE102 test), and the positive
line interference current returns to the interference source through the input capac-
itor C1, while the return line interference current directly returns to the interference
source; the other part of the interference current is conducted to the secondary loop of
the power supply through the parasitic capacitance Ct between the primary side and
the secondary side of the transformer, and is conducted by the parasitic capacitance
Cp between the positive line or the rectiﬁer diode and the ground to the casing, and
the positive line and the return line conduction are also separated at the LISN. The
positive line interference current passes through the input capacitor and returns to
the interference source together with the return line interference.
(2) DM interference current path
The MOSFET turn-on and turn-off produce an oscillation effect, the DM interference
path is shown in Fig. 7.17. The interference current generated by the oscillation is
conducted from the positive line to the LISN positive line detection circuit (the
positive line DM current is detected in the CE102 test), and is output by the LISN
return line detection circuit (the return line DM current is detected in the CE102
test), and ﬁnally returns to the interference source through the return line.
2. Analysis of oscillation interference generated by rectiﬁer diode
When the rectiﬁer diode is turned ON and OFF, an oscillation effect occurs due to
the inﬂuence of parasitic parameters. When the MOSFET Q1 is turned ON and the
output diode D1 is turned OFF, if the secondary side magnetic exciting inductance
is clamped, the secondary side leakage inductance and the diode stray capacitance
oscillate. The oscillation frequency is calculated as


7.4 EMC Design of the DC/DC Converter Module …
245
Fig. 7.17 MOSFET DM interference path
f =
1
2$\pi$\sqrtLesC j .
(7.4.3)
(1) CM interference current path
The rectiﬁer diode turns ON and OFF to produce an oscillation effect. The CM
interference path is shown in Fig. 7.18. The interference current generated by the
oscillation is conducted from the parasitic capacitance Cj at both ends of the diode to
the secondary side of the transformer, and is conducted to the primary side loop of the
power source through the parasitic capacitance Ct between the primary side and the
Fig. 7.18 Rectiﬁer diode CM interference path


246
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.19 Rectiﬁer diode DM interference path
secondary side. A part of it in the original side positive line is directly conducted to
the positive line detection circuit of LISN (the CM current is detected in the CE102
test), the other part is conducted to the return line detection circuit of the LISN
through the input capacitor C1 (the CM current of the return line is detected in the
CE102 test), and then together conducted back to the interference source through the
parasitic capacitance Cp of the positive line or the rectiﬁer diode.
(2) DM interference current path
The rectiﬁer diode turns ON and OFF to produce an oscillation effect. The DM
interference path is shown in Fig. 7.19. The interference current generated by the
oscillation is conducted from the parasitic capacitance Cj at both ends of the diode to
the secondary transformer, then transmitted to the primary loop of the power supply
through the parasitic capacitance Ct between the primary side and the secondary side,
and conducted from the positive line to the LISN positive line detection circuit (the
positive line DM current is detected in the CE102 test), and is output from the LISN
return line detection circuit (the return line DM current is detected in the CE102
test), then conducted in the primary side return line and conducted to the casing
through the parasitic capacitance Cds between the D-pole of the MOSFET and the
S-pole and the parasitic capacitance Cde between the D-pole of the MOSFET and the
casing, and ﬁnally conducted back to the interference source through the parasitic
capacitance Cp on the positive line or the rectiﬁer diode.


7.4 EMC Design of the DC/DC Converter Module …
247
7.4.2
Absorption Circuit Design
The absorption circuit can reduce the voltage or current change rate of the switching
and rectifying devices in the circuit to suppress the EMI intensity of the interference
source. The basic principle is that the switching tube is provided with a bypass when
it is turned OFF, so that it absorbs the energy accumulated in the parasitic distribution
parameter, thereby suppressing the intensity of the interference.
The absorption circuit in the DC/DC converter is composed of a capacitor and a
resistor connected in series, and is placed in parallel with the rectiﬁer diode. The
capacitor acts as a discharge circuit for the charge stored in the diode junction
capacitor when the diode is turned OFF, smoothing the diode current and voltage
waveforms, thereby reducing the HF components. In addition, the device leads in the
absorption circuit should be shortened and placed close to the rectiﬁer diode as much
as possible, which effectively reduce the loop area formed by the rectiﬁer diode and
the absorption circuit to reduce the radiated emission.
The following guidelines should be followed in the absorption circuit design:
(1) Add an absorption circuit between the drain and source of the converter
switching transistor (MOSFET) and between the two poles of the rectiﬁer
(continuous) current diode to reduce the amplitude and rate of change of the
spike voltage. There are mainly three types of absorption circuits: capacitance
absorption circuits, RC resistance-capacitance absorption circuits, and RCD
absorption circuits, as shown in Fig. 7.20a, b, and c, respectively, where the
RCD absorption circuit has the best performance;
(2) The resistor, capacitor, or diode lead in the absorbing circuit should be as short as
possible, and placed as close to the switching tube and the rectiﬁer (continuous)
current diode as possible;
(3) Ferrite beads can be added to the transformer’s lead-out line to absorb
interference.
(a)              (b)               (c) 
Fig. 7.20 Three forms of absorption circuits


248
7
Typical Spacecraft Electronic Component Selection …
7.4.3
Power Filter Design
EMI ﬁlters are the most effective means of suppressing conducted interference
from the DC/DC converters. They can also improve EMC effectiveness, such as
CS (CS101), RE (RE102), cable bundle injection CS (CS114), and ESD (CS118).
A common EMI ﬁlter can be deﬁned as a low-pass network that is composed of
passive components such as inductors, capacitors, or resistors. It can also be designed
as a band-pass or high-pass ﬁlter according to actual requirements. Generally, it falls
into L-type, T-type, and -type circuits according to its form, as shown in Fig. 7.21.
7.4.3.1
Network Structure of EMI Power Filter
Figure 7.22 shows the basic network structure of a single-phase power EMI ﬁlter.
It is a passive network of lumped parameter elements. The dashed box represents
the metal-shielded enclosure outside the ﬁlter. In the ﬁlter network, there are only
two inductors (L1 and L2) and three capacitors (two CYs and one Cx). If this ﬁlter
is inserted to the input port of the DC/DC converter, i.e., the “power” of the ﬁlter is
terminated to the LISN, the “load” of the ﬁlter is terminated to the DC/DC converter.
Thus, L1 and one CY, L2 and another CY form two pairs of low-pass ﬁlters of
independent ports of L-E and N-E respectively, to suppress CM interference signals
existing on the power line. The L1 and L2 are two independent coils wound on the
same magnetic ring, called a CM inductor or a CM choke. In theory, a CM choke only
exhibits CM inductance, but for various reasons, there is a CM leakage inductance,
which may exhibit a certain DM inductance. Thus, the CM leakage inductance Le and
Fig. 7.21 Basic circuit form of common EMI ﬁlter


7.4 EMC Design of the DC/DC Converter Module …
249
Load  
Shielding enclosure
Power
Fig. 7.22 Network structure of EMI power ﬁlter
CX form another low-pass ﬁlter between the independent ports of L-N to suppress
the DM interference signal on the power supply, thereby suppressing the EMI signal
of the power supply system, and protecting the equipment from being inﬂuenced.
7.4.3.2
Basic Steps for EMI Filter Design
The design of the EMI ﬁlter ﬁrst needs to obtain the amount of insertion loss that
the ﬁlter should provide. With the corresponding signal separator, the interference
signal of the EUT can be separated into a CM and a DM interference signal when
there are no ﬁlter elements added. Using the above results, the speciﬁc parameters
of each component in the ﬁlter can be calculated. Then, the designed ﬁlter is added
to the power input end of the EUT, and by measuring whether the interference signal
meets the requirements, we can know whether the designed ﬁlter is qualiﬁed.
1. Measuring the original CM and DM signals
Measurements of the original CM and DM signal spectrum separation can be done
by establishing a dedicated conducted EMI test system, as shown in Fig. 7.23. The
interference signal is taken out by the power supply linear impedance stabilization
network (LISN); after the CM/DM signals are separated by the signal separator, they
are measured by the spectrum analyzer. The PC records and saves the measurement
result accordingly.
2. Determining the amount of attenuation
AftertheCMandDMsignalspectrumisobtained,theamountofattenuationprovided
by the CM ﬁlter (VAT T,C M)d B and the DM ﬁlter (VAT T,DM)d B can be calculated by
the following Eqs. (7.4.4) and (7.4.5), respectively.
(VAT T,C M)d B = (VACT,C M)d B −(VLimits)d B + 6d B
(7.4.4)


250
7
Typical Spacecraft Electronic Component Selection …
Signal separator 
Spectrum analyzer
PC
EUT 
Fig. 7.23 Schematic diagram of conducted EMI test system
(VAT T,DM)d B = (VACT,DM)d B −(VLimits)d B + 6d B,
(7.4.5)
where (VACT,C M)d B and (VACT,DM)d B are the spectral amplitudes of the out-of-
standard points in the CM and DM spectrum, respectively, in dB\muV. (VLimits)d B is
the speciﬁed limit values, also in dB\muV. The 6 dB is added to make the attenuation
amount have a certain margin, so that the suppression requirement will be more
stringent,andthepossibilitythattheamplitudeoftheinterferencesignalafterﬁltering
is still greater than the limit value is reduced.
3. Determining the corner frequencies
The CM and DM attenuations (VAT T,C M)d B and (VAT T,DM)d B are plotted on the
logarithmic paper according to the relationship between the corresponding frequen-
cies, the abscissa is Hz, and the ordinate is dB\muV, as shown in Fig. 7.24. Taking the
CM interference signal as an example, make a 40 dB/dec diagonal line on the loga-
rithmic coordinate, and move the line from the lowest frequency to the right, making
it tangential to the CM attenuation curve at one point, and the CM attenuation curve
is completely below this line. The diagonal line intersects the horizontal axis at a
point, and the frequency corresponding to this intersection is the corner frequency of
the CM ﬁlter f RCM. Similarly, the DM ﬁlter corner frequency f RDM can be obtained.
4. Calculation of components
The larger the inductance and capacitance value of the ﬁlter component, the stronger
the attenuation to the interference signal; the lower the corner frequency that can
be achieved, the better the suppression effect on the LF interference signal, but the
corresponding cost and the volume will also increase. In addition, according to the
material characteristics, when the inductance and the capacitance value is larger, the
resonance frequency of the element is lower and the HF characteristics are poorer,


7.4 EMC Design of the DC/DC Converter Module …
251
Fig. 7.24 Calculation of the
corner frequencies
Amount of attenuation 
dBuV
CM or DM attenuation 
Corner frequency
Frequency (MHz) 
so it cannot be increased without limitation. Considering that the change rate of the
capacitance to the volume is smaller than the inductance value, and the capacitor has
a ﬁxed capacitance value, the capacitor should be preferred for determining the CM
and DM ﬁlter components.
(1) Calculation of CM components
Calculation of CM components includes the CM inductor LC and CM capacitor CY.
Since the CM capacitor CY is connected between the L, N lines and the ground line,
based on the leakage current limitation, the capacitance value cannot be selected too
large. After selecting the CY value, using the CM corner frequency calculated in the
previous section, the required CM inductance value can be calculated by Eq. (7.4.6):
LC =

1
2\pi fRC M
2 1
2CY
.
(7.4.6)
(2) Calculation of DM components
Calculation of CM components includes the DM inductor LD and DM capacitors
CX1 and CX2. CX1 and CX2 use the same component value, which can be obtained by
DM inductance LD and DM ﬁlter corner frequency f RDM from Eq. (7.4.7).
CX! = CX2 =

1
2\pi fRDM
2
1
2L D
.
(7.4.7)
In the equation, f RDM can be obtained according to the description above, but
LD, CX1, and CX2 are unknown. Therefore, in determining the component value, the
designer has considerable ﬂexibility. If the LD value is set larger, the values of CX1
or CX2 can be set smaller, and vice versa. However, the effects of the ﬁlter on the


252
7
Typical Spacecraft Electronic Component Selection …
Table 7.2 Digital circuit chip
selection for the data
acquisition unit
No.
Name
Speciﬁcation
Type
1
CPU
80C32
CMOS 5 V
3
Integrated circuit
54AC series
CMOS 5 V
10
ROM
HS1-6664
CMOS 5 V
11
RAM
HM1-65642
CMOS 5 V
12
Timer
JC4060
CMOS 5 V
circuit itself must also be taken into account, such as the stability and performance
factors.
7.5
EMC Design for the Data Acquisition Unit
7.5.1
Selection of Appropriate Components
The focus of component selection in the data acquisition unit is the digital circuit
chip. It can be seen from the rise time and voltage change rates of various digital
devices given in Sect. 7.1.6 that CMOS 5 V logic devices have the maximum rise
time and minimum voltage change rate. If the clock frequency of the data acquisition
unit is 12 MHz, the operating frequency is about 2 MHz, and then the rise time of the
signal is about 1 \mus. The rise time of the CMOS 5 V logic device is 100 ns, which not
only meets the operational requirement, but also limits the HF harmonic components
to the maximum extent. Therefore, the CMOS 5 V series are suitable for most logic
devices in the data acquisition unit. Table 7.2 shows a general selection of digital
circuit chips for the data acquisition unit.
Except that the integrated circuit chip uses the dual in-line package, the resistors
and capacitors all use chip packages to reduce the parasitic inductance by reducing
the lead length.
7.5.2
PCB Design
In view of the function setting of the data acquisition unit, there are both analog
circuits and digital circuits in the PCB. The analog circuit mainly includes an A/D
converter,ananalogswitch,anoperationalampliﬁer,a5Vreferencevoltageregulator
source; the digital circuit mainly includes a single-chip microcomputer unit (MCU)
and its peripheral circuit, a program memory, and a watchdog circuit. The chips in
the analog circuit are low-speed circuits, and those in the digital circuit are medium-
and high-speed circuits, as shown in Fig. 7.25. Therefore, for the PCB layout, the
following measures can be taken to meet EMC requirements.


7.5 EMC Design for the Data Acquisition Unit
253
High-speed circuit 
Medium-speed 
circuit 
PCB  
Low-speed circuit 
Serial com 
port circuit 
Micro-processor
Watchdog 
Power-on 
reset 
Data 
memory 
Program 
memory 
A/D 
converter
Analog 
switch 1 
Analog 
switch 2 
Analog 
switch 3 
Fig. 7.25 Schematic diagram of the PCB layout
(1) Separate the low-level analog circuits and digital circuits by using isolated
ground layers to minimize mutual interference between digital and analog
circuits;
(2) Partition the layout of low-speed, medium-speed, high-speed logic circuits, the
lower part of the PCB is for the analog circuits, and the upper part is for the
digital circuits;
(3) Arrange the high-speed components in the area closest to the connector, and the
low-speed components farthest from the connector to reduce the line impedance
and the loop area of the high-speed signal;
(4) Set a separate power supply layer and ground layer, the power supply layer
should be close to the ground layer. The recommended four-layer layout
is signal-ground-power-signal layers; the eight-layer layout is signal-ground-
signal-ground-power-signal-ground-signal layers.
After the layout is completed, the following guidelines should be followed during
the wiring on the PCB of the data acquisition unit:
(1) Increase the width of the lines or the line area to reduce its inductance. If the
lines are laid too dense, it is easy to cause the lines around the transmission line
to induce interference current;
(2) Shorten the length of the parallel line, increase its spacing, or add a ground line
between the two signal lines to reduce the capacitance between the signal lines.
The longer the length of the parallel lines, the larger the mutual capacitance,
and the more interference coupled from one circuit to another;
(3) The top and bottom wiring are perpendicular to each other;


254
7
Typical Spacecraft Electronic Component Selection …
(4) Decoupling capacitors should be provided between the power layer and the
ground layer to suppress or reduce the spatial radiation caused by the PCB
resonance;
(5) Decoupling capacitors are placed on the power pins close to the chip to eliminate
the effects of transient processes on the circuit;
(6) Dispense dedicated return lines or assign multiple return lines to reduce the
current in each line so as to control the interference voltage induced on each
line. Thereasonis that boththeleadandtheprintedlines haveacertainresistance
and inductance. When the interference circuit (digital or analog circuit carrying
noise current) and the sensitive analog circuit share a return line, an interference
voltage will be induced in the sensitive analog circuit.
7.6
EMC Design for General-Purpose Processor Module
7.6.1
Introduction to the Processor Modules
General-purpose processor module (CPU) is the computing mechanism of satellite-
board electronic equipment, mainly composed of a BM3803 computer system based
on SPARC V8 architecture. It supports 1553B, ARINC659, and RS-422 bus commu-
nication. The core functions are data management, bus management, time manage-
ment, and task management. It is widely used in spacecraft data management and atti-
tude/orbit control subsystem equipment. The composition of the system is shown in
Fig. 7.26, where ROM is read-only memory, SRAM is static random access memory,
and SDRAM is synchronous dynamic random access memory.
 
Comm  
High performance 
computer 
System control 
Serial port 
Timer  
Watchdog 
Memory controller 
External terminate/GPIO 
Terminate 
Control signal 
Other devices and 
systems 
Buse 
ARINC659,1553B 
Power, clock sources 
rom
sram
sdram
Fig. 7.26 System composition of general-purpose processor module


7.6 EMC Design for General-Purpose Processor Module
255
Compared with the traditional C51-based MCU system, the general processor
module has greatly improved the data processing capability with ﬂexible program
conﬁguration and good scalability. However, from the EMC perspective, its main
frequency is between 50 and 75 MHz, the power consumption is 5 W, the bus speed
is 30 MHz, and the layout is more compact, so the EMC design is comparatively
more difﬁcult.
7.6.2
EMI Characteristics of Processor Modules
7.6.2.1
ARINC659 Internal Bus
The general-purpose processor module’s ARINC659 internal bus based on a time-
triggered mechanism can reduce the number of hardware by using a serial trans-
mission line. Each bus interface unit is connected to two buses. Each bus node uses
a dual bus interface unit with cross-checking between bus units, and also cross-
checking between the four buses, so that the bus has dual BIT capability. All these
help to increase data availability. The bus interface architecture block diagram and
bus transmission line structure and connection relationship are shown in Fig. 7.27.
The ARINC659 bus is a linear, multipoint communication bus that transmits
half-duplex serial data. It consists of a dual bus pair (A/B) that forms a dual-dual
conﬁguration bus. Each bus pair consists of an X and a Y bus. Each bus (Ax, Ay, Bx,
By) has a separate clock and data line. Therefore, the complete bus group consists
of 12 bus transmission lines. The ARINC659 bus with clock frequency of 30 MHz
 
IEEE1149.5 test bus 
Self-checking bus pair B
Self-checking bus pair A 
Clock 
Clock
Clock
Clock
Table
Table
Table
Table 
Memory 
Memory
Memory
Memory
Main computer 
Main computer 
Fig. 7.27 Diagram of ARINC659 bus structure


256
7
Typical Spacecraft Electronic Component Selection …
can transmit two bits of data at the same time. In addition, the bus deterministically
divides time and space through a table-driven proportional access protocol, ensuring
that only one task is performed at a time.
In terms of EMC radiation characteristics, the ARINC659 bus in four redundant
bus designs has 12 buses for radiation sources, and four of them are with 30 MHz
clock lines. In the working mode of the table-driven proportional access protocol, the
bus exhibits as in a periodic working mode, which are the key factors affecting the
external EM radiation intensity of the module. Under the premise of not changing the
principle design, the PCB trace of the bus signal and the rationality of the layout of
the devices should be analyzed to ﬁnd out the optimization method, in which LRM
is a line replaceable module, and BIU is a bus interface unit.
For the 12 ARINC659 buses inside the module, according to the principle of “the
current loop area formed by the interconnect lines is as small as possible”, the traces
should be optimized to reduce the loop area. From the layout point of view, there is
a large distance between the bus control chip and the bottom connector; placing the
interface chip close to the bottom connector can reduce the length of the high-speed
signal trace. In terms of the interlayer distribution, the 12 buses are distributed in
different layers, of which 6 signal lines are on the surface layer, 2 lines on the middle
layer with 2 ground planes on the upper and lower sides, 1 line on the middle layer
without complete reference ground plane on the upper and lower layers, and 3 lines
on the middle layer with only one layer of the complete ground plane on the top or
bottom side. This results in the signal lines with both strip lines and microstrip lines,
which does not satisfy the principle of “HF printed lines should use strip line and as
short as possible”.
In summary, the PCB design of a general-purpose processor module should be
optimized by the layout of sensitive devices and sensitive lines and the stacking of
sensitive lines.
7.6.2.2
CPU Chip BM3803 and Peripheral Cooperative Circuits
The CPU chip BM3803 of the general-purpose processor module and its peripheral
cooperative circuits include SRAM memory, level conversion circuit, etc., as shown
in Fig. 7.26.
In actual use, the operating clock of the CPU system is at 50 MHz. During normal
operation, the BM3803 obtains data from the SRAM and controls other peripheral
circuits by the data lines (39), the address lines (24), and the control lines (12) through
thelevelconversioncircuit.Sotheabovesignalsallworkperiodicallyaccordingtothe
frequency (or frequency division), and are widely distributed on the PCB, wherein 23
lines are on the surface layer, 13 lines are on the middle layer with complete ground
planes both above and below, 13 lines are on the middle layer without complete
ground plane either above or below, and 26 lines are on the middle layer with only
one complete ground plane either above or below. These lines are the main radiated
EMI source of BM3803.


7.6 EMC Design for General-Purpose Processor Module
257
According to the EMC characteristics of the CPU system, ﬁrstly, the strong and
general radiation among many signal lines must be distinguished. The so-called
strong radiation lines refer to the signal lines with the high change rate of frequency
(>10 MHz) or steep edges (<10 ns) during normal operation, such as the lower 8
bits of the address line; secondly, PCB wiring design should follow the concept
that the strip line must be selected for strong radiation; ﬁnally, the loop area of the
interconnect line is minimized as much as possible.
7.6.2.3
Crystal Oscillator
The operating clock of the crystal oscillator in the general processor module is
60 MHz/50 MHz. The internal circuit of the crystal oscillator generates large RF
current, which usually cannot be fully led into the ground plane by the ground
pins outside the crystal oscillator. As a result, the metal casing becomes an antenna
equipment, so the surrounding of the crystal oscillator is ﬁlled with near-ﬁeld EM
radiation. If there are devices or PCB wirings within the range of the radiated ﬁeld
(300mils in diameter), the RF signals from the crystal oscillator and harmonic will be
coupled to the devices or PCB signal lines. In the general-purpose processor module,
there are 60 MHz crystal oscillators that provide clocks for the bus management chip,
50 MHz crystal oscillators that provide clocks for the BM3803 chip, and other lower
frequency crystal oscillators. The harmonics of these crystal oscillators are the main
cause of excessive emission of EMC radiation. In a limited space, blocking the
coupling paths is an effective way of suppressing the EM radiation of the crystal
oscillators, so that the crystal oscillator circuits are isolated from the rest of the
devices and PCB lines.
7.6.3
EMC Design for the Processor Module
Due to the EM radiation of the general-purpose processor module, it is necessary
to optimize the PCB design of the module, identify the sensitive signals, deﬁne the
optimal wiring layer, and implement the targeted design constraints, as detailed in
the following:
The optimal wiring layer means that the adjacent upper and lower layers are
continuous ground planes. The optimal PCB wiring for the ARINC659 bus are as
follows:
(1) Sensitive lines are laid on the innermost layer but on the surface layer. The
spacing of sensitive lines should be greater than 120 mils.
(2) Each bus group contains signal lines D0, D1, and CLK; buses in the same group
are required to be arranged on the same signal layer.
(3) The wiring spacing between the ARINC659 signal-sensitive line and the bottom
plate connector should be less than 20 mm.


258
7
Typical Spacecraft Electronic Component Selection …
(4) For the bus management chip layout, AX and BX must be on the same side and
AY and BY must be on the same side.
The optimized PCB wiring for the CPU is as follows:
(1) Sensitive lines (data lines 24–31, address lines 0–7) are required to trace in the
inner layer and without microstrip lines. The spacing between sensitive lines
should be greater than 30 mils.
(2) Different types of sensitive lines should be grouped and routed according to their
categories. The signal lines of the same category can be bundled. The sensitive
lines of different categories should be arranged away from each other.
(3) All sensitive signal lines are at least 15 mm away from the mechanical frames.
The optimized PCB wiring for the crystal oscillator is as follows:
(1) The wiring of the crystal oscillator should be as close as possible to the load
and away from the interface.
(2) Centered on the output pin of the crystal oscillator, no devices or printed circuits
are allowed within the range of 300 mil (except for its own resistance and load).
(3) The crystal clock PCB trace should ﬁrst pass the matching resistor (as close as
possible to the clock output pin), then punch via holes to the “optimal wiring
layer”, and then to the load, the total number of vias should be no more than
two.
(4) If the crystal clock line is longer than 2 mm, it is necessary to design a protection
ground, with a line width 3 times wider than that of the crystal clock.
7.7
EMC Design for the Bus Management Module
7.7.1
Brief Description of the Characteristics of the Bus
Interface Module
The bus interface management module is the control core of the integrated business
unit of the integrated electronic equipment. As the RT of 1553B, the bus interface
management module realizes the communication with BC (the central management
unit), accepts the management of the BC, internally manages other modules in the
integrated business unit through the internal bus, and externally provides RS-422
interface, CSB interface, ML/DS interface, through which it achieves management
of other devices.
The bus interface management module is a central business management module
based on the core of the MCU 80C32, with a running frequency of about 11 MHz.
The module internally uses two ASIC chips (one is the master chip, the other is
the slave chip. The master chip is the BC end of the inner bus, the slave chip is
the RT end of the inner bus distributed in various modules, both ASIC chips have
a crystal oscillator of 11 MHz). The internal bus communication rate of the entire
integrated business unit is 115.2 kbps. The external CSB interface adopts a ﬁve-wire


7.7 EMC Design for the Bus Management Module
259
system, speciﬁcally the clock signal, command and instruction signal, telemetry data
indication signal, command data output, and telemetry data input. It functions as the
bus communication between the load devices and battery pack interface management
unit, and also as remote command transmission, telemetry parameter collection and
framing, system status BIT, and communicate with other devices in the satellite
through RS-422 interface. The bus management module also provides an ML/DS
interface to perform data communication functions with the PCU.
7.7.2
Features and Layout of the 1553B Interface Circuit
(Isolated Bus)
The 1553B features high speed and ﬂexibility, high communication efﬁciency, easy
modiﬁcation, expansion, and maintenance. In particular, as a redundancy design of
the bus, it improves the reliability of the system and is widely used in the space
ﬁeld. The 1553B bus generally adopts a direct coupling (stub) output mode, see
Fig. 7.28. The 1553B bus outputs the Manchester II dual-phase level code; looking
from the isolation transformer to the stub (toward the bus), the impedance is Z0,
so the characteristic impedance of the stub cable (nominally 78 ), the usual way
to connect the stub of the transformer (or direct) coupling terminal to the external
system connector is to use a 78  twisted-pair shielded wire, which can minimize
the impedance mismatch.
For all transceivers, the transformer center tap on their side, pin2, must be
grounded. The reason is that at any moment the chip is transmitting, only one trans-
former pin is driven, there is no instantaneous current on the other pin. Due to the
action of the autotransformer, the voltage on the other pin of the transformer will
swing the same amplitude to the opposite polarity.
When considering the placement, signal direction, and power distribution of the
1553B, which acts as an output/input interface, the following factors should also be
taken into account:
Direct coupling (stub)
Max. length300mm 
Stub with specified length
11.6VPP isolation transformer
Transformer coupling (long stub) 
Fig. 7.28 Schematic diagram of 1553B output circuit


260
7
Typical Spacecraft Electronic Component Selection …
(1) Isolation transformer: the isolation transformer should be placed as close as
possible to the corresponding TX/RX pin on the 1553B interface chip, so that
not only the voltage drop on the analog signal line can be limited during trans-
mission, but also the coupling interference can be reduced by shortening the
distance between the 1553B interface chip and the transformer. Severe inter-
ference can cause the bit error rate of the 1553B receiver to exceed the level
allowed by the MIL-STD-1553B standard. The recommended PCB layout is
shown in Fig. 7.29.
(2) Bus layout: Avoid 1553B signal lines close to other analog and digital signals
on the PCB, more importantly, avoid parallel layout of other high-speed analog
or digital signals with 1553B signal lines.
(3) There should be no ground or power layers under the transformer to prevent the
impact of transformer signal change on the power supply and the ground layers.
It is preferred to use a ground or power plane under the 1553B chip.
(4) Layout of the power supply and ground lines: The layout of the power supply
and the ground lines should be the focus of consideration. When the 1553B
bus is working, the working current path is as follows: output from −15 V
(or −12 or +5 V) power supply, passing through the output of the 1553B chip
transmitter, then ﬂowing to the center tap of the transformer through the isolation
(Top view)
Clock crystal oscillator 
Channel A power pin 
Channel B power pin 
Channel B  
decoupling capacitor 
Channel A  
decoupling capacitor 
Logic 
decoupling 
capacitor 
Fig. 7.29 Diagram of PCB layout of the 1553B interface circuit


7.7 EMC Design for the Bus Management Module
261
transformer pin. It is important to understand that the operating current loop is
through the center tap of the transformer, instead of the GNDA and GNDB pins
of the 1553B chip.
Minimizing the distributed impedance of the power supply along this path is
an important consideration in layout. For the input voltage of the power supply,
any resistor can cause a voltage drop and eventually reduce the output voltage of
the transmitter, which may be lower than the minimum voltage required by MIL-
STD-1553. In the worst case, the lowest supply voltage should be guaranteed and
the voltage drop should be calculated. The transceiver voltage passed between the
powersupplypinofthe1553Bchiptransceiverandthecentertapofthecorresponding
transformer cannot be lower than the speciﬁed minimum value (−13.5, −10.5, or
4.5 V).
In the transmission path of the power supply, due to the existence of various
inductive reactances that hinder the supply current, the chips with the instantaneous
high power demand, such as the 1553B chip, may result in an instantaneous large
drop in the supply voltage, which affects the function of the equipment. In order
to ensure the voltage stability of the circuit, it is necessary to increase the storage
capacitor around the circuit. For the selection of capacitor, refer to BULK capacitor
selection documentations.
(5) Analog and digital ground: In order to minimize the effect of ground noise on
the protocol/transceiver interface in the 1553B chip, the LOGIC GND pin and
the GNDA and GNDB pins should be connected to the +5 V power supply
loop instead of −15 V/−12 V power supply circuit. Note that the LOGIC GND,
GNDA, and GNDB pins are connected together inside the ACE/Mini-ACE and
must be connected to the same external ground.
(6) Decoupling capacitors—reducing HF ripple:
For the 1553B chip terminal, consider two different sizes of the decoupling
capacitors:
➀A relatively small capacitor, with a small effective series resistance (ESR)
and effective series inductance (ESI), which is often necessary to reduce HF
(1 MHz) supply ripple.
➁A relatively large capacitor. It is possible to use it to compensate for the
resistive voltage drop in the system power distribution.
For a +5 V logic input power supply, a 0.01 \muf capacitor is generally sufﬁcient.
For the transceiver power inputs, small decoupling capacitors are usually required
to eliminate the supply ripple generated by the 1 and 2 MHz current pulses caused by
the 1553B chip transceiver input supply. A low ESR/ESI capacitor of 2.2 \muf should
be sufﬁcient.
However, for the above two cases, if the voltage drop caused by the resistive
distribution impedance is greater than the difference between the minimum output
voltage of the power supply and the minimum input voltage required by the 1553B


262
7
Typical Spacecraft Electronic Component Selection …
chip transceiver, a larger decoupling capacitor is required in parallel. It is recom-
mended to place a 10 \muf external tantalum capacitor and a 0.1\muf capacitor as close
as possible to the transmitter +5 V input pin. The 70 pin in Fig. 7.29 is a −12 or −
15 V channel A power supply, and the 36 pin is a −12 or −15 V channel B power
supply. In addition, it is recommended to place a 0.1 \muf capacitor as close as possible
to the logic +5 V input pin.
7.7.3
The Features and Layout of RS-422 Interface Circuit
(Differential Bus)
RS-422 and RS-485 interfaces are commonly used interface circuits on satellites,
the electrical characteristics are balanced bidirectional interfaces. The interface
parameters are shown in Table 7.3.
The electrical characteristics of RS-422 and RS-485 are balanced bidirectional
interfaces, both of which use differential inputs. The differential characteristics of the
interface chip can effectively reduce the inﬂuence of CM noise on the communication
lines. The layout of the signal lines should be in accordance with the differential
wiring requirements:
(1) The length of the differential pair should be the same to prevent the signal phase
difference;
Table 7.3 RS-422 and RS-485 interface parameters
Parameters
RS-422
RS-485
Operation mode
Differential
Differential
Number of nodes
1 transmission
10 receive
1 transmission
32 receive
Maximum transmission cable length (m)
121.92
121.92
Maximum transmission rate (Mb/s)
10
10
Maximum drive output voltage (V)
−0.25 to +6
−7 to +12
Driver output signal level (minimum sttload) (V)
Load
\pm2.0
\pm1.5
Driver output signal level (maximum no load) (V)
No load
\pm6
\pm6
Driver load impedance ()
100
54
Swing rate (maximum)
–
–
Receiver input voltage range (V)
−10~+10
−7~+12
Receiver input threshold (mV)
\pm200
\pm200
Receiver input resistance (k)
4 (minimum)
\geq12
Driver CM voltage (V)
−3~+3
−1~+3
Receiver CM voltage (V)
−7~7
−7~+12


7.7 EMC Design for the Bus Management Module
263
(2) When wiring, the differential lines are placed close to each other to minimize the
loop area. The differential pair impedance matches with the terminal resistance
(RS-422/RS-485 requires 120 ). If necessary, the impedance can be matched
by adjusting the line width to reduce the noise. The distance between the differ-
ential pairs should be as short as possible and consistent to ensure the receiver’s
CM suppression capability;
(3) When wiring, the distance between two groups of differential pairs should be
greater than 4 times the distance between the two lines of the differential pair,
and the distance between one group of differential pairs and one other line should
be greater than 3 times the distance between the two lines of the differential pair;
(4) Reduce the number of vias. No copper cover should be available between the two
lines of the differential pair to avoid discontinuity of the differential impedance.
When via is unavoidable, the differential pair should be layered synchronously,
and a ground hole is set next to the differential line via;
In short, PCB design is basically to control the impedance, line length, line width,
and line spacing.
Interface design and PCB layout
(1) Add a current limiting resistor at the power supply end of the interface chip.
Since the current of the RS-422 interface is relatively large, the current limiting
resistor should not be too large;
(2) Add a decoupling capacitor at the power supply end of the interface chip.
According to the transmission rate, it is recommended to use 0.1 \muF and 1000 pf
capacitors.
(3) The driver and receiver should be as close as possible to the edge of the PCB
and close to the connector; shorten the differential line;
(4) Use multilayer PCB, the interface signal line must be very close to the ground
plane to ensure continuous impedance; it is not recommended to change layers;
make the differential signal line away from other signal lines on the PCB;
(5) When contacts are allocated on the connector, usually the positive and negative
attributes of adjacent (upper and lower, left and right) signals should be different,
and different differential pairs are separated by ground;
(6) The external cable can use a twisted pair. Shielded cables should be used as
much as possible. Use a 360^\circ loop connection for the shield grounding.
(7) If it is a one-to-multiple mode, note that the matching resistor needs to be placed
at the farthest receiver;
The default fault interface mode recommended by the RS-422 interface speciﬁ-
cation is shown in Fig. 7.30.
In practice, this method may cause damage to the chip at the transmission end
in the CS115 test. It is recommended to connect a magnetic bead on the differential
line of the transmission end. The magnetic bead should have a resistance value of
50  or more to suppress external interference damage to the transmitting chip, and
to suppress internal interference to conduct outward, as shown in Fig. 7.31. In the
case of large interference, the composition of the ZT resistor at the receiving end is


264
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.30 RS-422 Default fault interface mode
Fig. 7.31 Improved
transmission end
DIN
DY
Dz
Transmission end
Magnetic bead
Magnetic bead
Fig. 7.32 Improved
receiving end
Receiver 
Ground 
changed as shown in Fig. 7.32 to enhance the suppression of external interference.
For high-speed signals, pay attention to the effect of capacitors and beads on the
signal edges.
7.7.4
Features and Layout of CSB Circuit (Single-Ended
Bus)
The C-Serial Bus (CSB) Interface bus is a 5-wire serial bus including a clock line
(CLOCK),atransmissionremotecontrolline(CMD),atelemetrycontrolline(ACQ),
a remote control data line (DATA OUT), and a telemetry data line (DATA IN). The
bus is currently often used on satellite load compartments. The platform device acts


7.7 EMC Design for the Bus Management Module
265
as the BC terminal to control the load compartment equipment. One serial bus can
control up to 31 load equipment.
According to the interface requirements, the rising and falling edge is 0.2 \mus
minimum, and the clock’s minimum rising edge is 6 \mus. The actual measured rising
and falling edges on each signal line are around 1us. When the dielectric constant \varepsilonr
is at 4.5 for the FR4 PCB, the transmission delay is about 140 ns/in. Generally, the
rise time less than 4 times the signal transmission delay is regarded as a high-speed
signal. So, it can be seen that this signal is not a high-speed signal either by the edge
or the frequency.
Referring to the periodic signal spectrum envelope of digital circuits in Sect. 2.1.2,
the Fourier spectrum envelope is obtained as shown in Fig. 2.3, where the ﬁrst corner
frequency F1 is 10.6 kHz, and the second corner frequency F2 is 318 kHz, both at
the low-frequency end. The EMC technical requirements are 45–60 dB\muV/m in the
low-frequency range. If there is only this circuit on the PCB, there will be no EMI
problems. However, when using this circuit, the interference of other signals on the
internal PCB that are induced by the internal power supply and ground of the PCB
should be considered.
In the layout, the CSB should be designed as a single-ended signal, the circuit
should be away from other HF circuits. Preventing capacitive crosstalk between lines
and space-induced inductive crosstalk is a prerequisite for ensuring bus EMC, the
solution of which is to follow the 3W principle, that is, maintaining 3 times line width
between PCB lines; in addition, keep it away from thermal load, power distribution,
power command, relay, and other inductive loads and high-power drive devices, and
close to the PCB connector layout. The length difference of the CLOCK signal and
other signal lines should not be too large, to avoid the timing margin between the
signals to become smaller, causing timing problems during long-line transmission.
The interface power supply and the whole PCB power supply are recommended to
be separated by magnetic beads, and magnetic beads are added to ﬁlter HF on the
output ground line, so as to prevent HF interference of the power supply and the
ground on the PCB from being transmitted through the signal lines.
7.8
EMC Design for RF Circuit
The spacecraft integrated a large number of microwave RF equipment in a narrow
space, which occupies a wide operating bandwidth and has a large variation in oper-
ational signal power, and constitutes particularly prominent system EMC problem.
With new designs, new technologies, new processes widely applied to satellite
load technology, the emerging of new IF data processing systems, new broadband
transceiver equipment, and the increasing of operating frequency, the requirements
on system EMC are ever increasing. The traditional model for solving the equip-
ment EMC problem is no longer adaptable to the new development requirements,
which raises an urgent need to study EMC design and evaluation techniques for RF
equipment and subsystems in the future.


266
7
Typical Spacecraft Electronic Component Selection …
7.8.1
Scheme and Layout
Due to the existence of a high-gain ampliﬁer circuit in the RF circuit, in order to
avoid mutual interference between the circuits at all levels, the layout RF circuit
usually adopts an L-type or -type form. The advantages of this layout are that it
can achieve spatial isolation between the high-level signal circuit and the weak signal
circuit, reduce the positive feedback effect of the signal, and increase the stability of
the circuit operation.
Reasonable allocation of spectrum resources. Since the received signal of the
spacecraft is very weak, it requires that the platform equipment must have a very low
noise level in the receiver operating frequency band. In the spacecraft system-level
design, the corresponding electric ﬁeld RE limits are determined by the receiver
sensitivity on different frequency bands. In the speciﬁc RF equipment design, two
principles should be followed: First, ensure that the MF signals, local oscillator
signals, various intermediate signals, and main spurious signals of the equipment do
not appear in the receiving frequency band; second, in case the equipment frequency
cannot be completely avoided, select the same frequency device with a lower working
level, take measures such as spatial isolation or additional shielding to ensure that
the equipment does not affect the normal operational performance of the receiver.
Proper distribution of gain links and parameters in the RF circuit. The circuit
gain in space RF equipment is very high, especially in receiver products, which can
reach 70–90 dB. Ultrahigh gain circuit links need to be carefully designed to avoid
self-oscillation. Typically, multistage ampliﬁcation and processing circuits are used
to achieve the gain and signal quality of the whole equipment. For weak signal
circuits, the gain of each stage in the multistage ampliﬁcation and processing links
needs to be controlled at about 15–30 dB, which not only ensures that self-excitation
of the circuit does not occur, but also avoids too many links and stages that may
cause loss of standing waves, gain, and noise factor. Solid-state power ampliﬁer
circuits have better harmonic control due to device characteristics. Traveling wave
tube ampliﬁer has obvious nonlinear characteristics due to its inherent properties,
but has lower suppression capability for harmonic signals, and usually is only used
for the last stage power ampliﬁcation.
Cavity design. First, the power supply and RF circuits are isolated in different
cavities. The power supply line between the power supply and the RF takes the
form of a feedthrough ﬁlter. Second, different stages of RF circuits are arranged into
different cavities. This is mainly to prevent crosstalk or positive feedback between
various levels of the RF circuit, resulting in a poorer circuit performance.
7.8.2
Shielding Design
The main concern of RF equipment shielding is the casing of the equipment and the
interconnection cables. An early estimation of RF circuit design parameters and SE


7.8 EMC Design for RF Circuit
267
can be made on the basis of a large number of common cables and casing shielding
indexes and by referring to common SE database at the initial stage of product design,
so that corresponding shielding measures can be determined in advance.
Here is a case study example to illustrate the shielding index estimation in an
equipment design. The equipment to be designed is a solid-state ampliﬁer with only
three ports: a power and command port, an input RF port, and an output RF port.
Taking the RE102 test item as an example, the transmission channel radiated by the
product RF working signal is the product input RF cable and port, the output RF
cable and port, the low-frequency cable and port, and the housing gap. Assume that
the solid-state ampliﬁer has a gain of 50 dB and an input level of −10 dBm.
Estimation of the equipment signal RE is
E(dB\muV/m) = P(dBm) + 105
(7.8.1)
The transmitted ﬁeld strength can be estimated by tabularization, see Table 7.4.
The shielding indicator of different positions of the product is based on the
statistical value of the actual engineering measurement results. Different structural
designs, connector types, processing technologies, shielding treatment technologies
have different shielding effects, so it is necessary to accumulate empirical data in
engineering practice. The structure or connector can be selected according to the
abovementioned shielding evaluation results in engineering practice to meet the
requirements, as shown in Fig. 7.33.
Table 7.4 Estimation of the transmitted electric ﬁeld strength
Frequency
Transmission
position
Max
operating
level
(dBm)
Radiated
ﬁeld
strength
(dB\muV/m)
Shielding
indicator
(dBi)
Radiation
ﬁeld
strength
(dB\muV/m)
Limits
(dB\muV/m)
Conformity
Working
frequency
point
Casing
40
145
90
55
65
Conform
Working
frequency
point
Output port
and cable
40
145
80
65
65
Conform
Secondary
harmonic
Casing
10
115
90
25
70
Conform
Secondary
harmonic
Output port
and cable
10
115
80
35
70
Conform
Other
harmonics
and clutter
Output port
and cable
−10
95
80
15
45
Conform


268
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.33 Solid-state
ampliﬁer shielding
estimation
RF output 
LF connector
RF output 
Solid-state amplifier
7.8.3
Filter Grounding
7.8.3.1
Use of Attenuators, Filters, and Isolators
Suppression of reverse signal transmission by isolators. For internal signal
processing equipment such as receiver, an isolator can be used to suppress the
harmonic signal generated by the internal nonlinear device of the equipment from
entering the receiving link of the system, and avoid mutual interference between
adjacent channels of the satellite.
Suppression of out-of-band signals by ﬁlters. Moderate suppression of
harmonic signals can be achieved by using a chip ﬁltering module and microstrip
ﬁlters. For high-degree harmonic suppression, it is recommended to design a dedi-
cated passive cavity or coaxial ﬁlter. Since passive cavity ﬁlters are typically large
in size, they are usually placed on the side or top of the RF circuit housing.
Reducing clutter signals by attenuators. Inserting an attenuator at the input end
of the receiver can attenuate n times of the n-th order product in the receiver. For
example, a 3 dB attenuator can reduce the third-order intermodulation product by
9 dB, but the attenuation of the useful signal is still 3 dB.
7.8.3.2
Grounding of the RF Circuit
Grounding is the main concern in the design of RF circuits. Due to the high RF
frequency, in order to reduce the loss of the transmitted signal and achieve the control-
lability of the transmitted impedance, an outer shield layer of the RF cable and the
casing are usually used as the return path of the signal. A slight structural inﬂuence
on the cable and the casing will cause slight inductive, capacitive, or simultaneous
inductive and capacitive impedance on the return path. The actual equivalent AC
impedance will reach a higher level in the RF band, resulting in a signal leakage
during transmission.
The machining process also affects the circuit conditions. For example, a common
RF PCB substrate is typically screwed to the underside of the internal cavity of the
product. The surface treatment process and processing precision of the RF ceramic
substrate and processing precision of the printed circuits will have a great inﬂuence


7.8 EMC Design for RF Circuit
269
on the EM parameters of the RF circuit, mainly affecting the characteristics of the
passband edge, gain ﬂatness, and standing wave.
The effect of the mounting ﬁt of the ceramic substrate and the bottom surface
of the cavity on the EM parameters of the circuit. Both the ceramic substrate and
the bottom surface of the cavity have surface roughness and ﬂatness errors. These
machining errors will result in a dielectric layer between the substrate and the bottom
surface, which is created by the overlap of air, metal, and ceramic. Since the dielectric
constant of this dielectric layer is related to parameters such as the mechanical param-
eters of the ceramic substrate, the bottom surface of the cavity, and the mounting
pressure, it is very difﬁcult to control in practice. In the circuit design, it is impossible
to make accurate simulation estimation, and it is most likely to cause additional para-
sitic parameters in the RF circuit and result in a signiﬁcant deviation of the circuit
indicators. In general, the higher the operating frequency of the circuit, the greater the
impact of the processing and installation technique is. Especially in the Ka-band, the
processing accuracy of ceramic substrates and cavities is extremely high; otherwise,
it will have a direct inﬂuence on the circuit performance.
7.8.3.3
Inﬂuence of Foreign Objects
When a foreign object enters the RF microstrip line or the waveguide, a clutter signal
maybegeneratedintheoutput spectrumof theproduct. Speciﬁcally, thesurfaceof the
RF microstrip line is contaminated with a polymer medium or a conductive powder
medium, which may directly affect the RF electrical performance of the microstrip.
These foreign objects may cause a degradation of the output signal quality of the
product, accompanied by clutter. Foreign objects inside the passive channel will
form PIM interference products, and micro-discharge may occur in some high-power
waveguides.
7.8.4
Wiring Rules
7.8.4.1
Substrate
The application plates in RF circuit design are mostly microwave copper-clad dielec-
tric substrates and ceramic substrates. The advantages of the microwave copper-clad
dielectric substrate are lightweight, low microwave loss, relatively simple manu-
facturing process, short processing cycle, and wider application than conventional
ceramic substrates. Although the ceramic substrate is with the advantages of small
dielectric constant, high stability, and high line precision, due to its disadvantages
of the complicated manufacturing process and long cycle, it is not suitable for the
design of complex circuits.


270
7
Typical Spacecraft Electronic Component Selection …
7.8.4.2
Grounding
1. Grounding of HF circuit
The HF PCB should be bonded with the casing to ensure the lowest bonding
impedance between the PCB and the casing. In the PCB layout, the ground vias
should be placed in a large ground area, the maximum spacing of the vias is $\lambda$/10. In
order to prevent process problems such as vias overlapping, it is required that the via
spacing is no less than $\lambda$/60, and the speciﬁc value should be determined according
to the actual RF circuit.
2. Grounding of the microstrip PCB
In the microstrip PCB design, the bottom surface of the cavity is used as the grounding
surface to avoid the skin effect, and the silver plating is usually used to reduce the
ground impedance. The bottoms of some components are grounded metal shells,
which require designing some grounding holes in the projection area of the compo-
nent, and placing conductive layers in the projection area of the surface layer, but
cannot apply solder mask. The RF components are made of metal shells that have
grounding requirements, such as integrated ampliﬁers and ﬁlters. During assembly,
the shells should be tightly attached to the bottom plate to reduce the bonding resis-
tance between the shell and the structural ground. Grounding can also be further
improved by tablet compressing the device or spot welding between the shells and
the PCB.
7.8.4.3
Wiring
The resonance of the printed wires. For the design of HF signals, the length of
the wiring must not be an integer multiple of 1/4 of its wavelength, so as to avoid
resonance and antenna effects.
Printed wire length control. In the design, the wiring length should be as short
as possible to reduce the interference caused by too long traces, especially for some
important signal lines. For example, the local oscillator of a mixer with a relatively
higher frequency must be placed very close to the mixer.
Width change of the printed wires. The width of the wire on the PCB should
not be changed dramatically. If necessary, the trace width can be gradually changed.


7.9 EMC Design for RF Equipment Power Supply
271
7.9
EMC Design for RF Equipment Power Supply
7.9.1
Effect of Power Supply Noise on RF Equipment
The power supply circuit of RF equipment is usually designed as a separate module;
it can be packed in a separate housing, or in a separate cavity in the whole equipment
casing to ensure certain shielding isolation between the power supply circuit and the
RF circuit.
The main sources of the power line noise:
First is the EM noise generated by the power module itself, secondly, the noise
or interference signal on the primary power network transmitted to the RF circuit
through the power module, and ﬁnally, the interference signal inducted by the
secondary wire of the power module, as shown in Fig. 7.34.
The RF device is supplied directly by the secondary power line; the interference
signal on the DC power is directly coupled to the output carrier of the product, causing
parasitic clutter signals in the product. For some frequency synthesis circuits and
devices operating in nonlinear mode, the parasitic clutter signals caused by power
supply noise may be quite noticeable.
For the conducted interference of the primary power network above 20 kHz, the
suppression measures are mainly to optimize the input ﬁlter suppression character-
istics of the power supply circuit. For self-designed ﬁlter circuits, the effects of HF
parasitic parameters of the ﬁlter components must be considered. For commercial
power modules and EMI ﬁlters, it is recommended to use those matching products
in the manufacturer’s product description to achieve the best clutter suppression
effect. For multiple power modules sharing the same EMI ﬁlter, it is recommended
to purchase the same series of products from the same manufacturer, because their
input and output impedances are similar to each other, which helps to select a suitable
EMI ﬁlter. If combined power modules from different manufacturers are used due to
condition constraints, it is recommended to verify the effectiveness of the existing
EMI ﬁlter at the start of the circuit design. For audio interference signals, it may be
necessary to use the combined effects of the response characteristics of the power
module and various ﬁltering measures for interference suppression.
Globally, the switching frequency of the spacecraft-level power modules is about
60 kHz–2 MHz, and generally, the frequency of China-made modules is relatively
Power network 
interference 
Power switch noise
Power supply 
circuit 
Power 
adaptive 
circuit 
RF circuit 
Inducted noise on the 
interconnected wires
Fig. 7.34 Interference source on the secondary power line of an RF circuit


272
7
Typical Spacecraft Electronic Component Selection …
low,andthatofimportedmodulesisrelativelyhigh.Accordingtotheactualswitching
frequencyandamplitudeofthepowersupply,theoutputﬁltermustbesodesignedthat
the power switch noise is initially suppressed by the output ﬁlter of the power supply
circuit. In the power supply adaptive circuit of the RF circuit, a simple capacitor
resistance ﬁltering circuit can be added for secondary suppression.
Common RF equipment includes power modules and RF modules. There are three
ways for their power supply and communication interconnection, namely intercon-
necting cables with connectors, plug-in connectors, and self-deﬁned structures. The
external interference signal source is mainly the electric ﬁeld radiated induction of
the interconnecting wires; the corresponding EMC test item is RS103. Because of
the shorter length of this segment of interconnecting wire and the stronger coupling
capability for HF signals, the ﬁlter suppression is mainly targeted at HF interfer-
ence in the subsequent RF power adaptive circuit design. For multichannel modules,
the power supply and RF circuits are usually designed separately, each of which
constitutes a power multi-module equipment and an RF multi-module equipment,
which are interconnected by a long cable. The external interference consists of both
radiation and conduction. For such power supply and RF-separated equipment, the
interconnecting cable can detect both the radiated interference ﬁeld and the interfer-
ence signal of the adjacent cables. In the power supply adaptive circuit ﬁlter design,
both HF suppression and LF suppression should be considered.
The interference signals on the power line will often cause a clutter signal mixed
into the RF output spectrum. LF interference will enter the RF circuit through the
power supply line. If an interference excitation is applied at the power supply end of
the device, for RF devices operating in the nonlinear state, parasitic clutter signals
will be mixed in the output signal. Because of the ﬁltering and frequency selective
characteristics of the RF circuit itself, the interference signal in the passband will
eventually enter the subsequent circuit, together with the working signal.
7.9.2
Nonlinear Effects of Common Filter Component
Passive devices will exhibit nonideal characteristics at HF due to their own parasitic
parameters. For common capacitors, resistors, and inductors operating in HF circuits,
the actual measured parameters deviate signiﬁcantly from their nominal values. This
kind of common nonideal characteristics in ﬁlter components can seriously impair the
EM CE, RE, and immunity performance of the product. The components to be used
must be evaluated at the beginning of the design, so that the expected suppression
effect can be achieved within the working frequency range of the product. Resistors
of different types or from different manufacturers have different parasitic parameters.
Designers are advised to review the detailed speciﬁcations of the components in the
EMC design of the circuit to obtain the frequency range of the devices and the range
of parameters.
The common HF model of an electrical connection line is the resistance and
inductance in series. If there is a ground plane near the connection line, a distributed


7.9 EMC Design for RF Equipment Power Supply
273
Fig. 7.35 HF model of an
electrical connection line
capacitance to the ground should be added to the model. It can be seen from the model
that the impedance caused by the inductance component of the lead wire increases
continuously with the risen frequency, but the small distributed capacitance between
the lead wire and the housing is not enough to produce a signiﬁcant effect on the
transmission impedance. The HF characteristics of the lead can also be characterized
by electrical connection lines. In the actual circuit design, if the circuit is applied
in an HF environment, the chip components should be used as much as possible to
avoid the degradation or failure of the HF ﬁltering function caused by the leads. The
lead length should also be minimized where only pin components can be used. Note
that the component leads include the length of the trace on the PCB. An HF model
of the electrical connection line is shown in Fig. 7.35.
Common resistors can be roughly divided into wirewound resistors, metal ﬁlm
resistors, and composite carbon ﬁber resistors. The parasitic inductance inside the
wirewound resistor is the largest, and that of the ﬁlm and composite carbon ﬁber is
smaller. However, the noise of the wirewound resistor is the smallest, and that of
the composite carbon ﬁber resistor is the lowest. It can be seen from the resistance
model that the resistance in DC is purely resistive; in the LF band, the resistance
shows as capacitive, that is, the impedance decreases continuously; at the resonant
frequency of the capacitor and the inductor 1/\sqrtL * C, the resistor exhibits a minimum
impedance value; as the frequency increases, the parasitic inductance of the resistor
increases rapidly, eventually equals the open circuit impedance. An HF model of the
resistor is shown in Fig. 7.36.
The inductance shows a series inductance and parasitic resistance at LF. The actual
impedance is inductive; its value increases with increasing frequency. However, at
HF, the parasitic bypass capacitance has a greater inﬂuence, and the actual impedance
shows an increasing trend with frequency. An HF model of the inductor is shown in
Fig. 7.37.
Fig. 7.36 HF model of a
resistor


274
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.37 An HF model of
an inductance
Fig. 7.38 An HF model of
common capacitors
In the selection of ﬁlter capacitors, the effective use frequency of capacitors is
one of the important parameters. Common capacitive components include pins and
chips. It can be seen from the HF model in Fig. 7.38 that the capacitance ﬁrst exhibits
a capacitive impedance, and as the frequency increases, the impedance gradually
decreases; at the resonance point of the parasitic capacitance and inductance, the
impedancereachesaminimum;subsequently,theinﬂuenceoftheleadinductanceand
its own inductance is more prominent, causing the impedance to gradually increase.
In ﬁlter design, special attention should be attached to the effective frequency range
of the capacitor. A feedthrough capacitor is a special kind of capacitor that needs to
be mounted on the metal structure of an equipment to achieve the best ﬁltering effect.
Due to the special structure of the feedthrough capacitor, its HF model is similar to a
T-type ﬁlter. The impedance to ground is very small, and its effective use frequency
can reach GHz, which is very suitable for ﬁlter isolation of RF power supply lines,
as shown in Fig. 7.39.
Fig. 7.39 An HF model of a
feedthrough capacitor


7.10 RF Equipment EMC Structural Design
275
7.10
RF Equipment EMC Structural Design
7.10.1
Shielding Design
7.10.1.1
Calculation of Shielding Effectiveness (SE)
1. SE of discontinuous shield
In engineering applications, the shields inevitably have various gaps, cable holes,
etc., which will affect the shielding effectiveness. According to the barrel theory, the
actual SE of the shield is mainly determined by the minimum SE design, including
gaps, holes, and cable penetration.
(1) SE of gaps
Most of the gaps in the space RF equipment housing are installation gaps, which are
completely different from the design gaps such as optical windows, and there are
many factors affecting its SE. The current theoretical shielding calculation accuracy
of such gaps does not meet the engineering requirements. It is recommended that a
number of housing gap shielding index tests are performed regarding the common
design and processing technology, and using empirical values instead of theoretical
calculations in actual engineering to achieve better effectiveness.
The materials used in the housing, the spacing of the gap screws, the mounting
pressure, the surface roughness, the bonding ﬂatness, and the treatment process of
the bonding planes all affect the SE of the gap. To this end, it is recommended that
the SE of common RF equipment housing is 50–70 dB, and that of high sensitivity
receiver is 70–100 dB.
(2) SE of holes
The SE of holes is related to a number of factors, such as the characteristics of the
ﬁeld source, the distance from the source, the frequency, the maximum size, and area
of the hole. The SE of the holes can be analyzed by the following empirical formula:
SE = Aa + Ra + Ba + K1 + K2 + K3
(7.10.1)
where Aa is the transmission loss, Ra is the reﬂection loss, Ba is the multiple reﬂection
correction factor, and K1, K2, K3 are the correction terms introduced by the number
of holes.
Since the housing is generally designed with only one hole, the three correction
items K1, K2, and K3 can be ignored in SE calculation, so we have
SE = Aa + Ra + Ba
(7.10.2)


276
7
Typical Spacecraft Electronic Component Selection …
(1) Transmission loss Aa
According to the impact of the shape on the transmission loss, there are two types of
holes: round and rectangular holes.
Round hole:
A = 32 t
D
(7.10.3)
Rectangular hole:
A = 27.3 t
W
(7.10.4)
where t is the hole depth (cm), W is the length of the wide side of the rectangular
hole perpendicular to the electric ﬁeld (cm), and D is the diameter of the round hole
(cm).
(2) Reﬂection loss Ra
Ra = 20 lg (1 + N)2
4N
(7.10.5)
where N is the ratio of hole characteristic impedance to incident wave impedance,
wherein N = D/3.68r is applicable to round holes of near-ﬁeld magnetic ﬁeld,
N = W/\pir is applicable to rectangular holes of near-ﬁeld magnetic ﬁeld, N =
j5.79 \times 10−5 \times f \times D is applicable to round holes of near-ﬁeld electric ﬁeld,
N = j6.69 \times 10−5 \times f \times W is applicable to rectangular holes of near-ﬁeld electric
ﬁeld,
r is the distance from the source to the shield (cm), and
f is the EM wave frequency (MHz).
(3) Multiple reﬂection loss Ba
When Aa \geq10 dB, it can be ignored.
When Aa < 10 dB,
Ba = 20 lg

1 −(N −1)2
(N + 1)2 \times 10−0.1\timesAa

(7.10.6)
(3) Inﬂuence of cable on SE
If a conductor passes through the shield, the SE of the shield will be signiﬁ-
cantly degraded. A typical example is an interconnecting cable that passes through
equipment housing.


7.10 RF Equipment EMC Structural Design
277
Fig. 7.40 Cable passing
through the model
The HF EM electrical ﬁeld inside the microwave circuit cavity can be conducted
to the nearby LF connector through the space ﬁeld, line inductance, and between-line
inductance, then transmitted outward through the signal transmission wire to form a
signalcouplingpath.Theexternalinterferencesignalcanenterthecircuitthroughthis
path, and the internal working signal can also be transmitted to the outside through
this path to interfere with the sensitive devices nearby. Due to the complexity of the
EM ﬁeld in the housing, it is recommended to use simulation software to estimate
the interference signal, as shown in Fig. 7.40.
2. Comprehensive SE of single-layer housing
The actual SE of a shield is a comprehensive response of the shield itself and the
SE of various designs (gaps, holes, cable penetrations, etc.). According to the theory
of transmission lines, if the phases of EM waves transmitted by various defects are
approximated as the same, the overall shielding effectiveness SE is
SE = −20 lg
n
	
p=1
10−SEP/20
(7.10.7)
where SE is the comprehensive SE of the shield; SEP is the SE of various defects.
Thefollowingisabriefdescriptionofthecalculationprocessofthecomprehensive
SE.
Assume that the product housing is made of aluminum with a thickness of 1 mm,
the internal signal frequency is 2 GHz, the SE of the gap on the housing is 20 dB,
and that of the hole is 50 dB. The SE of the housing on the plane wave ﬁeld of the
internal RF signal is to be calculated.
(1) SE of continuous casing SE1
SE1 = A + R + B
(7.10.8)
For aluminum, \mur = 1, \sigmar = 0.61, f = 2 \times 109 Hz, and t = 1 mm.


278
7
Typical Spacecraft Electronic Component Selection …
Since A is much larger than 10 dB, B (multiple reﬂection correction factor) can
be ignored:
SE1 = A + R = 4647.8 dB
(7.10.9)
(2) The SE of the gap is known as SE2 = 20 dB, and the SE of the hole is SE3 =
50 dB.
(3) The overall SE of the housing is
SE = −20 lg
n
	
p=1
10−SEP/20 = 19.72 dB
(7.10.10)
Therefore, the overall SE of the product housing is 19.72 dB.
It can be seen from this case that the SE of the casing is affected by many factors
and conforms to the barrel theory. The actual SE generally depends on the worst SE
of the design element in the shield.
3. Double shielding
In order to increase the shielding effectiveness, a double-layer shielding scheme can
be used. The SE of the double shielding is
SE = SE1 + SE2 + C
(7.10.11)
where SE1, SE2 are the SE of the two shielding layers; C is the multiple reﬂection
correction factor between two shielding layers.
The correction factor C is a negative value, which mainly reﬂects that a certain
part of the EM wave penetrates the second shielding layer into the internal space
after multiple reﬂections in the space between the two shielding layers, resulting in
a reduction in SE. In addition, the space between the two shielding layers may also
cause resonance, which has a negative impact on the double shielding.
There are many factors inﬂuencing the correction factor C, which are very compli-
cated to analyze and not easy to quantify. In short, the SE of the double shielding is
not the simple sum of the SE of the two shielding layers, the actual SE is certainly
less than that.
7.10.1.2
Shielding Design Elements
1. Shielding design of gaps
When two parts are combined, the gap of the joint surfaces is the main factor affecting
the SE of the structural part.


7.10 RF Equipment EMC Structural Design
279
Table 7.5 Product housing shielding test data
Test frequency (GHz)
Housing SE (dB)
 (dB)
The housing is not installed
with a conductive rubber
gasket, and the cover screw
is normally assembled
The cover is installed with a
conductive rubber gasket;
the back cover screw is
normally assembled
1
39
66
27
2
39
56
17
3
27
64
37
4
36
66
30
5
32
55
23
6
19
58
39
7
32
78
46
8
−4
42
46
8.1 (housing resonance
frequency)
−9
35
44
9
20
60
40
10
42
63
21
12
26
62
36
14
17
65
48
16
30
60
30
18
34
67
33
According to the analysis of the gap shielding principles and combined with the
actual engineering experience, measures can be taken in the depth of the gap, the
processing precision of the contacting surfaces, the mounting pressure, the screw
spacing, the conductive gasket, and the conductive coating to improve the SE of the
product casing. See Sect. 6.4.2 for details.
At present, the SE of the conductive gasket cannot be simulated. Table 7.5 shows
the shielding test data before and after the installation of the conductive rubber gasket
on the product casing. It can be seen that after the installation of the conductive rubber
gasket, the SE of the casing is greatly improved, and especially remarkable in the
vicinity of the resonance frequency of the casing.
2.
Shielding design of holes
(1) Factors affecting the SE of holes
The main factors affecting the SE of holes include the maximum size, depth, spacing,
and number of holes, the most prominent of which is the maximum size and depth
of the hole. In design, round holes and square holes are preferable, long waist holes
should be avoided.


280
7
Typical Spacecraft Electronic Component Selection …
Table 7.6 Shielding effectiveness of typical holes
Thickness (mm)
Size (mm)
2 GHz
SE
4 GHz
SE
6 GHz
SE
8 GHz
SE
12 GHz
SE
14 GHz
SE
3
Round: F2
68.67
62.65
59.14
56.66
53.18
51.87
Round: F3
49.15
43.14
39.65
37.18
33.76
32.49
Round: F4
38.65
32.66
29.18
26.75
23.40
22.18
Square: wide side 2
67.41
61.40
57.89
55.42
51.96
50.66
Square: wide side 3
47.89
41.89
38.41
35.96
32.57
31.32
Square: wide side 4
37.40
31.42
27.96
25.54
22.25
21.06
2
Round: F2
52.67
46.65
43.14
40.66
37.18
35.87
Round: F3
38.48
32.48
28.98
26.52
23.10
21.82
Round: F4
30.65
24.66
21.18
18.75
15.40
14.18
Square: wide side 2
51.41
45.40
41.89
39.42
35.96
34.66
Square: wide side 3
37.23
31.23
27.74
25.29
21.90
20.65
Square: wide side 4
29.40
23.42
19.96
17.54
14.25
13.06
(2) Shielding of the box holes
The SE of the perforated metal sheet is related to the maximum size rather than the
area of the hole. Therefore, under the premise of meeting the requirements of use,
it is recommended that the hole be a round or hexagonal hole, then a square hole.
Do not use waist holes or even elongated holes. Generally, holes should be as small
as possible to ensure adequate SE. Since the SE can be improved by increasing the
thickness of the shielding layer, if the SE does not meet the design requirements, it
may be considered to locally thicken the shielding layer at the hole.
At lower frequencies, the hole has less effect on the SE of the cavity. In Table 7.6,
the RF signal \geq2 GHz is analyzed. The data in Table 7.6 does not take into account
the effects of the perforated cable. In practice, the perforated cable can degrade the
SE of the cavity.
Other design methods can be used to reduce the size of the holes and improve the
SE of the cavity, subject to external constraints such as product assembly.
3. Shield design of connectors
The shielding design of a connector refers to the shielding of the connector as well
as its housing and cables, instead of only the connector itself. Common electrical
connectors have shielding design speciﬁcations, for example, the theoretical SE of
common SMA connectors can reach 80–90 dB.
Installation: The mounting surface of the connector and the housing should ensure
good electrical conductivity. The more number of ﬁxing screws used, the larger the
mounting pressure, which can reduce the contact impedance and achieve better SE.
The mounting screw tightening torque is usually speciﬁed in the connector manual.
Commonly used ITT electrical connectors use 4-40UNC screws; the tightening


7.10 RF Equipment EMC Structural Design
281
Table 7.7 ITT connector
tightening torque
Torque (N m) Material
Screw status
0.55
Brass
Internal threads
0.66
Stainless steel Internal threads
0.33
Brass
No internal thread/through-hole
0.44
Stainless steel No internal thread/through-hole
0.33
Brass
External threads
0.44
Stainless steel External threads
torques are shown in Table 7.7. The contacting surfaces of the housing should be
ensured to have a good ﬂatness and roughness.
The connector SE can also be improved by applying a conductive coating. During
the design, a dedicated gap for conductive coating should be reserved for convenient
operation. It can also increase the depth of the gap and enhance the SE.
7.10.2
Cavity Resonance
7.10.2.1
Principle of Cavity Resonance
DuetotheshortEMwavelengthofthemicrowavefrequencyband,harmfulresonance
effects can be formed in metal housings of common equipment. Here, the internal
circuits and components of the microwave equipment are ignored, and the housing
is simpliﬁed into a cubic shielding cavity, as shown in Fig. 7.41.
According to the resonance cavity theory, the resonant frequency of the box f is
f =
1
2\sqrt\mu0\varepsilon0

m
w
2
+
n
h
2
+
 p
l
2
(Hz)
(7.10.12)
where w, h, l are the width, height, and length of the housing in m;
\mu0, \varepsilon0 are, respectively, the magnetic permeability and dielectric constant of the
air inside the housing, \mu0 = 4\pi \times 10−7H/m, \varepsilon0 = 8.85 \times 10−12F/m.
Then,
Fig. 7.41 Schematic of
simpliﬁed equipment
housing


282
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.42 Current intensity
distribution on the inner wall
of the cavity
f = 150

m
w
2
+
n
h
2
+
 p
l
2
(MHz)
(7.10.13)
where m, n, p = 0, 1, 2, 3, 4, …
When m, n, and p are different (no more than two of them are 0 at the same time),
the resonant frequency is also different, so a shielded box has multiple resonant
frequencies, but for a certain excitation source, the resonant frequency is unique.
When the metal cavity resonates, the EM ﬁeld induces a surface current on the
inner wall, as shown in Fig. 7.42, in which colors are used to indicate the distribution
of surface current on the inner wall of the cavity. Red indicates the high-intensity
surface current, and green indicates the low-intensity surface current. Figure 7.43
shows the direction and distribution of the induced current on the inner wall of the
metal cavity.
Fig. 7.43 Current
distribution on the inner wall
of the cavity


7.10 RF Equipment EMC Structural Design
283
Table 7.8 Box SE test data
Test frequency (GHz)
1
2
3
4
5
6
7
8
8.1
9
10
12
14
16
18
Box SE (dB)
39
39
27
36
32
19
32
– 4
– 9
20
42
26
17
30
34
Example: A rectangular shielding cavity has a length of 130 mm, a width of
100 mm, and a height of 20 mm. The lowest resonant frequency of the shielding
cavity is to be calculated.
In the case of TE-wave resonance, the lowest resonance frequency is TE101 mode
(i.e., m = 1, n = 0, and p = 1). Since the excitation direction of the ﬁeld in the
shielding cavity may be arbitrary, n = 0, so the w and l in the formula should be the
larger values in the length, width, and height.
fT E101 = 150

 1
0.13
2
+
 1
0.1
2
= 1.9 GHz
(7.10.14)
So, the minimum resonant frequency of the shielding cavity described above is
1.9 GHz. However, except for the TE101 mode, there may be resonance modes
such as TE102, TE103, TE201, TE301, and TE111, and the corresponding reso-
nant frequencies are 3.21 GHz, 4.65 GHz, 2.75 GHz, 3.77 GHz, and 7.74 GHz,
respectively.
Shielding cavity resonance is a detrimental phenomenon. When the excitation
source causes the shielding cavity to resonate, the SE is greatly reduced. In actual
product design, the housing rarely has a regular cubic shielding cavity, and the reso-
nant frequency of the cavity is not only related to its shape and size, but also to the gap
of the cavity, the internal partition walls and the installed PCBs, microwave chips,
and other factors. The above-simpliﬁed model can only provide a rough estimation.
The actual resonant frequency of the shielded cavity needs to be simulated by special
software. For example, HFSS and CST can be used for related simulation analysis.
Table 7.8 is the SE test data of a product housing, which is ﬁxed with a cover by
screws. From the data in the table, the SE is near the resonance frequency point of
8.1 GHz and is negative, indicating a gain.
7.10.2.2
Improved Design of Cavity Resonance
In the product design process, a variety of measures can be taken to improve the
impact of the shielding cavity on product performance.
1. Dividing the cavity
Dividing a large product housing into several small cavities is shown in Fig. 7.44.
Since the RF circuit has a high operating frequency, according to the functional
modules of the product, a large cavity can be divided into several small cavities
to increase the resonant frequency of the housing, prevent the circuit operating


284
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.44 Sub-cavity
structure
frequency and the resonant frequency from coinciding or closing, and reduce the
EM leakage. Besides, the small cavities with SE requirements are designed with a
separate cover plate to form a double shielding together with the cover of the large
cavity.
The size of each sub-cavity can be divided according to the operating frequency
of each module circuit, so the cavity resonance frequency will not coincide with the
circuit frequency, the overall resonance frequency of the housing is increased, but it
will increase the product weight and the difﬁculty of design and processing.
2. Using conductive gaskets
Adding conductive gaskets between the housing and the cover plate has two func-
tions: one is to reduce the EM leakage from the gap of the housing, the other is that
the conductive rubber gasket has a certain absorption of EM wave, thus reducing the
internal resonance effect in the cavity.
TheSEtestdataofaproductboxshowsthattheSEhasbeensigniﬁcantlyimproved
after a conductive rubber gasket is installed between the housing and the cover plate,
especially at the resonance frequency of 8.1 GHz, where the SE is improved by
44 dB.
Conductive rubber gaskets are easy to use and have good shielding effectiveness.
It is necessary to leave a mounting position in the structural design, and the designed
pressure should be smaller than the maximum pressure that the gasket can withstand.
3. Circuit modularization
For microwave circuits with very high frequencies, the internal cavity will inevitably
have resonance, in this case, the microwave circuit can be made into an MMIC
module. The size of the MMIC module can be further reduced, so that the effect of
resonance on the circuit can be eliminated. Furthermore, the MMIC module usually
uses the solder sealing process, so its own housing shielding index is very high. The
modules can be connected by microstrips, for which small channel structures can
be designed to accommodate the microstrips while avoiding resonances from large
sizes.


7.10 RF Equipment EMC Structural Design
285
7.10.3
Shielding of Filler Material
This section introduces the EM shielding materials that are often used to ﬁll the holes
or gaps. They are mainly conductive rubber, conductive adhesive, metal spiral tube,
wire mesh strip, ﬁnger spring, conductive cloth, etc.
7.10.3.1
Conductive Rubber
1. Composition and characteristics of conductive rubber
The rubber is ﬁlled with a certain proportion of metal particles, such as silver
powder,copperpowder,aluminumpowder,silver-platedcopperpowder,silver-plated
aluminum, and silver-plated glass balls. This kind of material has good electrical
conductivity while retaining a good elastic property of rubber.
Conductive rubber has been widely used due to the advantages of softness, corro-
sion resistant nature, low density, high elasticity, a wide range of shielding frequency,
and low price, and the excellent processing performance and can be mass-produced.
2. Classiﬁcation of conductive rubber
Therearemanykinds of conductiverubber currentlyusedintheﬁeldof EMshielding.
According to ﬁller materials, they can be classiﬁed into three types:
(1) Metal ﬁller conductive rubber, which is formed by combining metal ﬁber,
particle ﬁller with rubber, and has excellent conductive and magnetic properties;
(2) Wire mesh composite conductive rubber, which is made of double metal wire
layer woven on the rubber surface, and is more cost-efﬁcient than the metal ﬁller
conductive rubber;
(3) Nonmetallic ﬁller conductive rubber, which is made of a nonmetallic conductive
material such as carbon as ﬁller and rubber. It is featured by poor EM SE,
especially in the LF range.
3.
Shielding properties of conductive rubber
The SE values of two conductive rubbers with a thickness of 1 mm are given below
as a reference, see Table 7.9.
The SE values in Table 7.9 are the test values of the plane waves by the coaxial
method, which cannot give higher SE due to the test method limitation. According to
the EM ﬁeld theory, as the frequency increases, the electric ﬁeld SE also increases.
In practice, such electric ﬁeld SE can meet the requirements.
4. Use of conductive rubber
Before installing the cover, place a conductive rubber gasket under the cover. The
shape of the conductive rubber gasket is the same as that of the joint between the
cover and the casing, and screw holes are reserved. In order to maintain the ﬂatness


286
7
Typical Spacecraft Electronic Component Selection …
Table 7.9 Shielding effectiveness of conductive rubber
Frequency
(MHz)
SE (dB)
Frequency
(MHz)
SE (dB)
Silver–Silicone
rubber
Silver–Copper
silicone rubber
Silver–Silicone
rubber
Silver–Copper
silicone rubber
0.1
88
70
10
103
82
0.3
89
78
100
103
100
1.0
90
78
150
103
100
3.0
93
79
200
103
100
Fig. 7.45 Conductive rubber
gasket
between the cover and the casing after installation, the structure should be designed
to leave proper space for the conductive rubber gasket. Note that the conductive
rubber gasket requires a certain pressure to achieve good electrical conductivity; the
compression ratio is generally about 10% as shown in Fig. 7.45.
7.10.3.2
Conductive Adhesives
The most commonly used conductive adhesive is a mix of epoxy resin with silver
powder. It can adhere ﬁrmly to metal, plastic, and ceramic surfaces to reduce EM
leakage. This conductive adhesive is liquid before curing, has good ﬂuidity, and easily
penetrates into the joint surface to ﬁll the gap. It is difﬁcult to disassemble after curing
and becomes a permanent connection. When applied to the surface of a medium, the
surface resistance can be less than 1 /m2. After increasing the thickness of the
coating, the surface resistance can be further reduced. The conductive adhesive has a
working temperature range of −60 to +120 ^\circC and can be cured at room temperature.
The shear strength after curing is 840 kPa and the tensile strength is 1750 kPa.
The EM leakage caused by the gaps on the equipment casing, the ﬂange surface
of the waveguide, the vent hole, and the gap on the connector can all be shielded
by applying the conductive adhesive with a very high EM SE. Note that if there is a
nonconductive medium such as a lacquer layer on the coated surface, the SE of the
conductive adhesive will be signiﬁcantly degraded. When the conductive adhesive


7.10 RF Equipment EMC Structural Design
287
is applied, the oxide layer, the insulating varnish, etc., on the coated surface should
be removed to maintain good electrical conductivity.
7.10.3.3
Spiral Tubes
Metal spiral tubes are made of good conductive materials, such as a thin beryllium
copper or a narrow strip of stainless steel. Spiral tubes have a constant deformation
stiffness and excellent compression fatigue resistance, and are easy to contact with
uneven joint surfaces. Metal spiral tubes have the widest operating frequency, highest
shielding performance, best anti-aging and anti-fatigue performance among all types
of conductive gaskets. Among them, stainless steel spiral tube gasket features low
costandgoodperformance,canbecategorizedintoindustrial-gradeproducts.Copper
spiral tube gasket has an electrochemical corrosion potential very close to that of the
aluminum chassis, so it has excellent electrochemical corrosion resistance, and can be
categorizedintomilitary-gradeproductsandcanmeetextremelyharshenvironmental
requirements.
Spiral tubes are recommended to be installed in slots. The dimensions of the slots
should provide the necessary pressure while ensuring that the gasket is not subjected
to overpressure.
7.10.3.4
Comparison of Common Shielding Materials
The performance of shielding materials is usually compared with the SE, elas-
ticity and resilience, installation structure requirements, price, etc. The comparison
of the above shielding materials is shown in Table 7.10. The SE and installation
requirements are important indicators in engineering applications.
Table 7.10 Comparison of various shielding material performance
Shielding material
SE
Elasticity and
resilience
Installation
Price
Conductive rubber
Good HF SE
Good elasticity,
requires a certain
pressure
Slots are ﬁxed
between two contact
surfaces by screws
High
Conductive adhesive
Good HF SE
/
Apply before curing
High
Metal spiral tube
Excellent SE
(90–140 dB)
Good elasticity, but
cannot be
overcompressed
Slots that require
compression limit
Low


288
7
Typical Spacecraft Electronic Component Selection …
7.10.3.5
Internal Bonding of the Circuits
The housing contains microwave chips and PCBs inside. For the microwave chip
circuits with relatively high frequency, its mounting surface is designed as a blind
cavity; the PCB is designed as a through cavity. The microwave chip is mounted
on the housing through the carrier, and bonded by reﬂow welding; the PCB and
the carrier are connected to multi-points of the housing by screws. The contacting
surfaces among the housing, the carrier, and the PCB must be electrically conductive
(the housing often uses silver-plated aluminum alloy).
The cover plate and the housing are connected by screws, and both are electrically
treated for good bonding. A frame is designed inside the housing to divide the area
according to the circuit function, in order to avoid mutual crosstalk inside the circuit
on the one hand, and to ensure the bonding between the PCBs and the housing and
between the housing and the cover plate on the other hand, to reduce the bonding
impedance. If the bonding impedance of the housing and the cover plate cannot meet
the requirements due to processing accuracy limitation, a conductive material may be
added between the housing and the cover plate to reduce the bonding impedance, the
gap between the housing and the cover plates, thus improving the SE of the housing.
7.11
EMC Design for RF Equipment PCBs
and High-Speed Digital Circuits
IntheEMCdesignofRFequipmentPCBcircuits,twoobjectivesareofmainconcern:
the additional EM radiation caused by the operation of the PCB and its device board
or the ability to resist external EM radiation, and the suppression capability to para-
sitic conducted interference signals in external power supply, communication, and
command lines.
With the increase in the frequency and density of high-speed digital circuits, simu-
lation tools are more and more important in circuit design. At present, some simula-
tion software providers have integrated Signal Integrity (SI) and Power Integrity (PI)
inspection tools into their products, a few manufacturers even provide PCB radiated
ﬁeld simulation tools. In engineering practice, SI and PI inspections can detect certain
design defaults in advance, so worthy of promotion. In radiated ﬁeld simulation, the
parasitic parameters and models of the devices and circuits are still immature and
have considerable simulation errors, which need further research and development.


7.11 EMC Design for RF Equipment PCBs and High-Speed Digital Circuits
289
Table 7.11 Optimized settings of the 6-layer PCB
Scheme
Power layers
Ground layers
Signal layers
1
2
3
4
5
6
1
1
2
3
S1
G1
S2
P
G2
S3
2
1
2
3
S1
G1
S2
G2
P
S3
Table 7.12 Optimized settings of the 10-layer PCB
Scheme
Power
layers
Ground
layers
Signal
layers
1
2
3
4
5
6
7
8
9
10
1
1
4
5
S1
G1
S2
G2
S3
G3
P
S4
G4
S5
2
2
4
4
S1
G1
S2
G3
P1
P2
G3
S3
G4
S4
7.11.1
EMC Design of Multilayer PCB
7.11.1.1
PCB Layer Setting
In PCB design, in combination with the speciﬁcation requirements of the board, the
numberofPCBlayersmustbedeterminedaccordingtothepowersupplyoftheboard,
the types of grounding, the signal density, the operating frequency, and the number
of signals with special wiring requirements. The optimal setting principle is that the
signal layer is separated by the power and the ground layers to achieve minimum
coupling crosstalk. A layer with high speed, HF, or clock signal wiring requires an
adjacent ground layer to reduce the radiation loop area. Due to the development
of design and mechanic technology, the density of electronic assembly is becoming
increasingly higher, and multilayer PCBs are more and more used in actual products.
Tables 7.11, 7.12 and 7.13 show common optimal PCB layer designs.
7.11.1.2
High-Speed PCB Function Division and Layout
When designing a PCB, the circuits are ﬁrst divided into analog and digital circuits,
then subdivided into clock circuit, drive circuit, A/D conversion circuit, D/A conver-
sion circuit, I/O circuit, switching power supply, ampliﬁcation circuit, and frequency
conversion circuit according to their speciﬁc functions; ﬁnally, the whole circuit is
rationally modularized according to the signal ﬂow diagram. The overall require-
ments include the shortest wiring route, the non-interleaved functional modules, and
the minimum possibility of mutual interference between the circuit modules.


290
7
Typical Spacecraft Electronic Component Selection …
Table 7.13 Optimized settings of the 14-layer PCB
Scheme
Power layers
Ground layers
Signal layers
1
2
3
4
5
6
7
8
9
10
11
12
13
14
1
1
5
6
S1
G1
S2
G2
S3
G3
P
S4
G4
S5
G5
S6
G6
S7
2
2
5
5
S1
G1
S2
G2
S3
G3
P1
P2
G4
S4
G5
S5
G6
S6


7.11 EMC Design for RF Equipment PCBs and High-Speed Digital Circuits
291
7.11.2
Crosstalk and Reﬂection of High-Speed Digital
Signals
7.11.2.1
Crosstalk
In high-speed digital circuits, the signal transmitted on one trace may interfere
with adjacent traces, because the trace spacing on the PCB is relatively close. This
phenomenon is called crosstalk. The signal line that causes interference is usually
called the interference line, and the disturbed signal line is called the sensitive line.
The main factors affecting crosstalk are coupling length, line spacing, signal rise
time, dielectric thickness, dielectric constant, etc.
The design measures to avoid crosstalk include
(1) Reduce the parallel length between signal lines;
(2) Increase the spacing between the lines;
(3) Separate the adjacent signal layers by a ground or a power plane, or make the
signal lines perpendicular to each other;
(4) Use protective ground lines to isolate the interference lines and sensitive lines;
(5) Place the high-speed signal wiring in the inner layer.
7.11.2.2
Reﬂection
Reﬂection is a basic effect of a transmission line. When a signal propagates on a
transmission line, reﬂection occurs if the impedance is discontinuous. The incident
wave and the reﬂected wave are superimposed at the impedance change, and prop-
agate along the transmission line back to the source. When this happens, the signal
waveform is distorted, which can damage signal integrity and cause overshoot, under-
shoot, and ringing of the signal waveform. Reﬂections typically occur at the end of
the transmission line, the corners, vias, component leads, and where line width varies.
When the drive sends a signal into the transmission line, if the impedance at the
end of the transmission line and the characteristic impedance of the transmission line
are different, part of the signal is terminated to the ground, and the remaining part
will propagate back to the source along the transmission line.
If the source impedance is greater than that of the transmission line, it is called
an underloaded transmission line, and there will be “steps” on the load side.
If the source impedance is less than that of the transmission line, it is called an
overloaded transmission line, and the load end will ring.
Inhibition measures of reﬂection effect:
(1) Reduce the length of the transmission line, that is, the delay on the transmission
line, and let the reﬂected wave reach a steady state as soon as possible. In
engineering, multilayer PCB layout can be used to increase wiring density and
reduce line length to improve reﬂection;
(2) Suspending. According to the characteristic impedance of the transmission line,
a series resistance is added at the drive end to match the impedance of the source


292
7
Typical Spacecraft Electronic Component Selection …
with the transmission line, or a parallel resistance is added at the receiving end
to match the impedance of the load with the transmission line, so that the source
reﬂection coefﬁcient or the load reﬂection coefﬁcient is zero.
There are four common suspending methods. In series suspending method, also
called source suspending method, a matching resistor is inserted in series near the
source; in parallel suspending method, a matching resistor is inserted in parallel to the
load of the transmission line; in Thevenin suspending method, a matching pull-up or
pull-down resistor is added to the load of the transmission line; in diode suspending
method, similar to Thevenin suspending, the matching resistor is replaced by a diode.
7.11.3
Power Integrity (PI)
Power integrity refers to the degree to which the system power supply meets the
requirements of the device’s operating power speciﬁcations after passing through a
certain transmission network. In practical engineering, the power grounding has a
great inﬂuence on the stability of the power supply, so reducing grounding plane
noise is usually regarded as part of power integrity.
In electronic systems, the fundamental task of the power subsystem is to provide
stable voltage reference and sufﬁcient drive current for all devices, which requires
a low-impedance power and ground connection between the power subsystem and
the functional circuits. One of the commonly used design methods is the target
impedance method.
7.11.3.1
Target Impedance Method
Firstly, the target impedance method is to determine the target impedance of the
power network based on the voltage and power consumption requirements of the
system; secondly, design the power network so that its impedance is always lower
than the target impedance over the operating frequency range.
Estimation of the target impedance of the PCB is Z = Vin \cdot 5%
Imax
(7.11.1)
where V in is the circuit input power voltage, in V; Imax is the maximum power
consumption of all devices on the circuit divided by the supply voltage, which is the
maximum operating current of the circuit in unit A, assuming 5% as the allowable
voltage ﬂuctuation range.
Estimation of circuit noise bandwidth is
F = 0.35
Tr
(7.11.2)


7.11 EMC Design for RF Equipment PCBs and High-Speed Digital Circuits
293
where T r is the digital waveform rising edge time, in ns; F is the circuit noise
bandwidth, in GHz.
Taking an FPGA as an example, the power supply is 3.3 V, and it draws a maximum
current of 2 A on the rising edge of 0.2 ns, which causes a transient voltage drop of
the power supply voltage, and a transient boost (ground bounce) of the ground plane
voltage.
The target impedance is obtained as Z = 82.5 m, circuit noise bandwidth F =
1.75 GHz.
7.11.3.2
Decoupling Capacitor
In order to achieve low-impedance design, a large number of decoupling capacitors
are used in the power module subsystem, PCB stacking and wiring subsystem, and
power load subsystem, so that the overall problem is simpliﬁed to a local design
problem.
Decoupling capacitors are usually divided into three levels: device-level, PCB-
level, power-plane, and ground plane distributed capacitors. Chip capacitors are
recommended for decoupling capacitors.
The decoupling capacitor has the highest effective frequency due to the series
inductance. Over this frequency, the actual impedance of the capacitor will be raised
until the decoupling effect is lost. The most common way to expand the capacitor
frequency is to connect multiple capacitors in parallel.
The internal inductance of a chip capacitor is usually at 1–2 nH, and can be
additionally increased by 5–20 nH through the connection of a printed line and a
via. The internal lead of the chip may have an inductance of 3–15 nH. For discrete
capacitors assembled by leads, the additional inductance on the lead can be estimated
with an empirical value of 1 nH/mm.
The estimation of decoupling capacitors refers to Signal Integrity Analysis and
Design of High-Speed Circuits in the list of References.
7.11.3.3
Installation Design of Decoupling Capacitors
For common dual in-line components, it is recommended to install decoupling capac-
itors as shown in Fig. 7.46. Components with higher clock speeds more often use
multilayer PCB, which are powered by the power plane and the ground plane.
For decoupling capacitors with chip capacitors, multiple capacitors are arranged
in parallel based on the estimated capacity, and the power plane and the ground
plane are connected by vias.


294
7
Typical Spacecraft Electronic Component Selection …
Fig. 7.46 Installation position of a decoupling capacitor
7.12
Summary
The EMC design of the spacecraft’s electronic equipment should start from identi-
fying the EM characteristics of the components and modules, then is implemented in
component selection and module design of the power supply unit, DC/DC converter,
data acquisition unit, general-purpose processor module chip, bus interface circuits,
and RF equipment related modules, so as to lay a solid foundation for equipment-level
EMC requirements.

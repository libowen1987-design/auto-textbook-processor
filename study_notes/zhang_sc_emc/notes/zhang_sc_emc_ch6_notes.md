# Zhang《Spacecraft EMC Technologies》第6章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 6. EMC Design and Implementation of General Electronic Equipment

Chapter 6
EMC Design and Implementation
of General Electronic Equipment
6.1
Spacecraft Equipment-Level EMC Standards
and Speciﬁcations
The spacecraft equipment-level EMC standards include
(1) MIL-STD-461G-2015, Requirements for the Control of Electromagnetic Inter-
ference Characteristics of Subsystems And Equipment;
(2) MSFC-SPEC-521C-2013, Marshall Space Flight Center, Electromagnetic
Compatibility Requirements for Equipment and Subsystems;
(3) GSFC-STD-7000A-2013, Goddard Space Flight Center—General Environ-
mental Veriﬁcation Standard, Electromagnetic Compatibility Requirement;
(4) ECSS-E-20-07C-2012, ESA Space Engineering, Electromagnetic Compati-
bility;
(5) AIAA-S-121A-2017, Electromagnetic Compatibility Requirements for Space
Equipment and Systems;
(6) SMC-S-008-2008, Space and Missile Systems Center Standard, Electromag-
netic Compatibility Requirements for Space Equipment and System;
(7) ISO-14302-2002, Space Systems—Electromagnetic Compatibility Require-
ments;
Due to the main role of MIL-STD-461G in equipment-level EMC requirements,
it is taken as the reference baseline standard for other standards and speciﬁcations
to be compared with, and the technical requirements are summarized as shown in
Table 6.1. It highlights the common EMC requirements and provides reference for
spacecraft electronic equipment to implement the EMC design requirements. Among
them, two newly added test items to the MIL-STD-461G are: the lightning effect
(CS117)andhumanbodyelectrostaticeffect(CS118),whichsatisﬁestheinterference
control requirements at system-level E3, such as lightning and electrostatic, at the
equipment-level.
In other equipment-level EMC standards and speciﬁcations, besides the common
technical requirements, there are some special requirements:
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_6
155


156
6
EMC Design and Implementation of General Electronic Equipment
Table 6.1 Summary of technical requirements for spacecraft equipment-level EMC
Technical requirements
MIL-STD
-461G
MSFC-SPEC
-521C
GSFC-STD
-7000A
ECSS-E-S
T-20-07C
AIAA 
S-121
SMC-S-008
ISO-14302
CE101 power line conducted emission (CE)
\times
A
A-DM
A-DM
A
A
A
CE102 power line CE
A
A
A-DM
A-CM
A
A
A
CE106 antenna port CE
L
L
L
\times
L
L
L
CS101 power line conducted susceptibility (CS)
A
A
A
A
A
A
A
CS103 antenna port intermodulation CS
S
\times
S
\times
S
S
S
CS104 antenna port unwanted signal suppression 
CS 
S
\times
S
\times
S
S
S
CS105 antenna port cross-talk CS
S
\times
$\times \times \mathbf{S}$
S
\times
CS114 cable bundle injection CS
A
A
A
A
A
A
S
CS115 cable bundle injection pulse excitation CS
A
A
\times
S
A
\times
CS116 cable and power line dampen sinusoidal 
transient CS
A
A
$\times \times \mathbf{A}$
A
\times
CS117 cable and power line lightning induced 
transient CS
L
\times
\times
$\times \times \mathbf{L}$
\times
CS118 ESD sensitivity (Chinese EMC standard is 
CS112)
\times
$\times \times \mathbf{L}$
\times
L
L
RE101 magnetic field radiated emission (RE)
\times
S
S
\times
S
S
S
RE102 electric field RE
A
A
A
A
A
A
A
RE103 antenna harmonics and spurious output RE
L
L
L
$\times \times \mathbf{L}$
L
RS101 magnetic field radiated susceptibility (RS)
\times
S
S
S
S
S
S
RS103 electric field RS
A
A
A
A
A
A
A
Power line spike signal (time-domain) CE 
(Chinese standard is CE107)
\times
S
S
S
A
S
S
Ground CS (Chinese EMC Standard is CS102)
\times
\times
$\times \times \mathbf{A}$
S
\times
Power line spike signal sensitivity (Chinese EMC 
standard is CS106)
\times
A
S
S
A
A
A
Note A-required items, S-optional items based on equipment characteristics, L-optional items


6.1 Spacecraft Equipment-Level EMC Standards and Speciﬁcations
157
Fig. 6.1 Bundled cable emission limits (MSFC-SPEC-521C)
(1) MSFC-SPEC-521C
➀Similar to the emission item corresponding to CS114, CE108 is a bundled cable
CE from 150 kHz to 200 MHz applicable to interconnected cables of equipment,
as shown in Fig. 6.1;
➁CS109 is a structure current CS of 60 Hz-100 kHz applicable to equipment with
an operating frequency below 100 kHz and signal sensitivity level below 1 \muV,
as shown in Fig. 6.2. The maximum interference of 120 dB \muA can be applied
to investigate its anti-interference capability.
(2) GSFC-STD-7000A
➀Power and signal lines common-mode CE mainly controls the CM CE of cable
bundle of 150 kHz to 200 MHz, its corresponding requirements are CS114 and
CS115, as shown in Fig. 6.3. The CM CE test layout is shown in Fig. 6.4.
➁Start-up transient CE. It is to ensure that the equipment’s start-up current and
transient changes will not affect the protection devices in the power bus circuits,
suchasresistancewires.Therequirementandtestlayoutofthepower-ontransient
limit are shown in Figs. 6.5 and 6.6.
(3) ECSS-E-20-07C
➀Power line CM CE of the spacecraft electronic equipment;


158
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.2 Schematic diagram of structural current conducted susceptibility (MSFC-SPEC-521C)
Fig. 6.3 Common mode CE limit curve (GSFC-STD-7000A)


6.1 Spacecraft Equipment-Level EMC Standards and Speciﬁcations
159
Fig. 6.4 Diagram of the common-mode CE test layout (GSFC-STD-7000A)
Fig. 6.5 Start-up transient limit requirement (GSFC-STD-7000A)


160
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.6 Diagram of start-up transient test layout (GSFC-STD-7000A)
➁Power line CM CS;
➂DC magnetic ﬁeld emission, which requires to measure the DC magnetic
ﬁeld emission of the six planes of the EUT using a Helms coil.
(4) AIAA-S-121A
➀Power and signal cable RF common mode CE is applicable to all signal
lines and bus power lines on spacecraft. The requirements and test layout
for common-mode CE limit are shown in Figs. 6.7 and 6.8.
➁Ground line injection CS
If the spacecraft uses its structure as a bus current loop, a spike signal, an
audio signal, and a RF signal should be separately injected to check its
ability to resist the conducted interference from the grounding network, as
shown in Figs. 6.9, 6.10, 6.11, 6.12, and 6.13.
(5) SMC-S-008
➀Frequency-domain and time-domain CE from CM to structure
This requirement aims at controlling CM emission interference through struc-
tures and cables, thus protecting the sensitive equipment that takes the structure
as their reference baseline and that equipment sensitive to magnetic ﬁeld emis-
sions generated by current loops. The frequency-domain controlled frequency
band is 30 Hz to 50 MHz, and the time-domain controlled frequency band is
DC to 400 MHz. The EUT should be isolated from the ground plane by 5 cm
of insulating material, and the DC isolation resistance should not be less than
10 M. The CM CE limits in the frequency-domain are shown in Fig. 6.14.


6.1 Spacecraft Equipment-Level EMC Standards and Speciﬁcations
161
Common mode CE dBuA
Frequency MHz
Fig. 6.7 Limits of common-mode CE (AIAA-S-121A)
Line impedance 
stabilization network
Measuring probe
EUT
Measuring 
receiver
Data 
recording 
device
Measuring probe
Real/simulated 
load and signal
Fig. 6.8 Schematic diagram of common-mode CE test layout (AIAA-S-121A)


162
6
EMC Design and Implementation of General Electronic Equipment
Peak -8V
Time (\mus)
Fig. 6.9 Example of ground line spike injection signal characteristics (AIAA-S-121A)
Fig. 6.10 Schematic of ground line spike injection signal test layout (AIAA-S-121A)
➁Ripple and periodic transient CE from the power supply and command control
lines
This requirement aims at ensuring that the equipment functions properly without
affecting the performance by ripple and periodic transients on the power line.
Refer to the test method in CE102, the measurement receiver can be replaced by
time-domain measurement equipment such as an oscilloscope with a frequency
band coverage of 400 MHz.
➂CS of the power supply and command control lines


6.1 Spacecraft Equipment-Level EMC Standards and Speciﬁcations
163
Fig. 6.11 Example of ground line audio injection signal characteristics (AIAA-S-121A)
Fig. 6.12 Ground line audio injection signal test layout (AIAA-S-121A)
Fig. 6.13 Diagram of ground line RF injection signal test layout (AIAA-S-121A)


164
6
EMC Design and Implementation of General Electronic Equipment
Basic limits
Band: 0.1-30Hz 
Band: 50-400MHz
Common mode CE dBuA rms
Frequency Hz
Fig. 6.14 Common mode CE limits in frequency-domain (SMC-S-008)
This requirement is applicable to all equipment that uses an external power
supply. The controlled frequency range is 150 kHz to 50 MHz, and the injected
signal strength is 1 Vrms or 1 W. The test layout is shown in Fig. 6.15.
➃Ground wire injection of audio, RF, and spike signals
In order to ensure that the platform electronic equipment operates normally
in case there is interference in the ground reference, the following signals are
injected into the ground line:
(a)
1 Vrms sinusoidal voltage or corresponding current from 30 Hz to 150 kHz;
(b) A sinusoidal RF signal of 1 Vrms or 280 mArms from 150 kHz to 100 MHz;
(c)
A spike signal of 10 \mus width, 8 V or 16A.
EUT
Oscilloscope
Signal 
source
Single phase
grounding 
(SPG) 
Power 
Fig. 6.15 Diagram of power and command control lines CS test layout (SMC-S-008)


6.1 Spacecraft Equipment-Level EMC Standards and Speciﬁcations
165
See the AIAA or SMC-S-008 for the test block diagram.
➄DC magnetic ﬁeld and magnetic moment
The emission control of the DC magnetic ﬁeld is to protect sensitive equipment
such as magnetometers, low-energy particle detectors, photomultiplier tubes,
tape recorders, electron beam equipment, drum memories. The limit is required
to be 160 dB pT at 7 cm.
The control of DC magnetic moment is to ensure that the spacecraft attitude
stability is not affected. The magnetic moment limit of the three-axis stabilized
spacecraft equipment should not exceed 0.01 A m2/kg, and that of the spin-
stabilized spacecraft equipment should not exceed 0.004 A m2/kg.
The main DC magnetic ﬁeld interference may originate from the following equip-
ments: DC-DC converter, magnetic holding relay, traveling wave tube, coaxial
switch, transformer, inductor, solenoid valve, spiral tube, motor, torque rod,
ferrite isolator, circulators, tape recorders, and other permanent magnet devices;
current loops: cables, ground current paths in structures, low current paths in
equipment, assembled internal wires, transformer and inductor coils, solar array
conductors, solenoids, current paths caused by accidental thermocouples, hot
spot induced currents in spacecraft structures, etc.
➅RS of magnetic and electric ﬁeld spikes and power frequencies
This requirement is to ensure that the equipment does not exceed the performance
of the induced transient and power electromagnetic ﬁeld frequencies. The width
of the spike signal is 10 \mus and E = 200 V. The length of the sensing cable is
1.5 m, at least 3 rounds. The test layout is shown in Figs. 6.16 and 6.17.
➆Passive Intermodulation (PIM)
This requirement is to ensure that spacecraft RF transmitters and other equipment
do not generate PIM-related incidental signals and avoid impact on spacecraft
receivers.
AC
Spike signal generator
Voltage 
reducer
Autotrans
former 
At least 15cm
EUT
Harness 
Typical 
value
Functional support 
device for EUT
Fig. 6.16 Diagram of cable test layout (SMC-S-008)


166
6
EMC Design and Implementation of General Electronic Equipment
Spike signal generator
EUT
Voltage 
reducer
Coupled 
transformer
AC
Fig. 6.17 Diagram of chassis test layout (SMC-S-008)
Makesurethatthethermalcontrolcoverandthebraidedmetalmaterialshouldnot
produce PIM. The bonding resistance, including the attached contact resistance,
should be controlled in the range of 0.1–500 k; the semiconductor equipment
should not be exposed to the RF transmitter radiation range, and the ﬁeld strength
should be lower than 250 mV/m.
The operating frequency bands of corresponding equipment should be PIM
veriﬁed.
(6) ISO-14302
For power bus time-domain and frequency-domain conducted interference, the
time-domain ripple is measured by means of a direct jumper resistor and an
oscilloscope, and the measurement of voltage ripple in the frequency-domain
is similar. The start-up transient current control is shown in Fig. 6.18:
It is shown in the table of summary of spacecraft equipment-level EMC standard
speciﬁcations that the common requirements are mainly CE101, CE102, CE106,
CE107, CS101, CS102, CS106, CS114, CS115, CS116, CS118 (CS112),
RE101, RE102, RE103, RS101, and RS103, etc., other common requirements
such as CS103, CS104, CS105, and CS117 are yet to be promoted to the
spacecraft equipment-level.
Summarizing the characteristics of the above standard speciﬁcations, spacecraft
power and signal line CM CE (CE108 bundled cable CE), microwave passive
component EM leakage assessment, DC magnetic ﬁeld emission, and ground
CS (spike, ripple and RF interference), etc., are requirements that are to be
improved.


6.2 General EMC Design Requirements for Equipment
167
Time (ms)
Transient/steady state current A
Fig. 6.18 Start-up transient current control (ISO-14302)
6.2
General EMC Design Requirements for Equipment
6.2.1
Spacecraft Equipment EMC Design Principles
The spacecraft electronics EMC design is generally based on the EMC technical
requirements, construction speciﬁcations, and related standards for a spacecraft
model. In the speciﬁc designs, the following E3s are analyzed and considered:
(1) During the spacecraft electronic equipment design, it is required to consider
the worst EME case throughout the life cycle, such as design, development,
testing, storage, transporting, launch, and on-orbit operation, which are the input
environment conditions for equipment-level EMC design.
(2) When designing EMC for spacecraft electronic equipment, it is necessary to
determineareasonableEMCmarginandminimizeoverdesignandunderdesign.
(3) The EMC design of spacecraft electronic equipment should be integrated into
the system design, and implemented in the project model, proto ﬂight model
development and ﬂight model improvement. The EMC design should be part of
the electronic equipment design review.
(4) The EMC design of spacecraft electronic equipment should be considered in
conjunctionwiththefunctionalandperformancedesign,andfollowtheprinciple
of compromise, instead of pursuing the optimization of individual indicators.
The equipment EMC index and the functional performance indicators should
be considered comprehensively according to the integrity design concept and
based on the system functional performance and compatibility.


168
6
EMC Design and Implementation of General Electronic Equipment
(5) The spacecraft system includes electro-explosive devices (EED). In the EMC
design, it is required to focus on the safety margin of the EED. The EMC design
must be performed for the critical parameters, such as circuit interfaces, the
interfaces between the subsystems, and the interfaces between the system and
the environment.
(6) For the EMC design of spacecraft electronic equipment, the corresponding
limits should be determined according to different criteria on performance level,
working level, and survival level, and the pertinence of technical requirements
should be improved.
(7) For the EMC design of spacecraft electronic equipment, priority should be
given to such measures as bonding, grounding, and layout of equipment and
cables. The EMC should be improved without increasing the weight, and then
the necessary shielding and ﬁltering measures should be implemented on this
basis.
It should be particularly mentioned that the EMC data of spacecraft systems,
subsystems, and equipment is the most direct reﬂection of the EMC characteristics
of spacecraft systems, subsystems, and equipment, and is of vital importance for
EMC design. The EMC test data should be accumulated, analyzed, and managed on
system-level, subsystem-level, and equipment-level. This experimental data should
be an important support and a valuable guidance for the EMC analysis and design of
spacecraft systems, subsystems, and equipment in order to improve the pertinence
and effectiveness of EMC design.
6.2.2
EMC Design Basis for Spacecraft Electronic
Equipment
The EMC design requirements for spacecraft electronic equipment are primarily
derived from the overall technical requirements and standard speciﬁcations, as shown
in Table 6.2.
In terms of the particularity of the spacecraft power conditioning unit (PCU),
corresponding power line CE and susceptibility requirements are given, including
items and indicators such as power line CE frequency-domain, power line CE time-
domain, load transient CE, battery line CE, solar cell array conductor CE, and power
line differential mode CS.
The EMC design of spacecraft electronic equipment is performed based on the
following limit requirements to the corresponding interface circuits:
(1) Equipment power conducted interface: CE101, CE102, CE107, CS101, CS102,
and CS106;
(2) Equipment antenna interface: CE106, RE103, CS103, CS104, and CS105;
(3) Equipment interconnected cable conducted interface: CS112, CS114, CS115,
and CS116;


6.2 General EMC Design Requirements for Equipment
169
Table 6.2 Summary of EMC design requirements for spacecraft electronic equipment
Items
Title of item
Application
CE101
25 Hz to 10 kHz power line CE
Power and return lines of mechanical
and electrical equipment such as
spacecraft gyro and momentum wheel,
excluding equipment power supply
output wires
CE102
10 kHz to 10 MHz power line CE
All power and return lines for
electronic equipment, excluding the
equipment power supply output wires
CE106
10 kHz to 40 GHz antenna port CE
Antenna ports on transmitters,
receivers, ampliﬁers, etc., not for
equipment with nonremovable antenna
The part of the transmission state is not
applicable to the equipment
transmission signal bandwidth or \pm5%
frequency range of the fundamental
frequency (whichever is greater)
CE107
Power line spike signal(TD) CE
Applicable to spacecraft equipment
with built-in relay switches
CS101
25 Hz to 150 kHz power line CS
Applicable to equipment power lines,
excluding return line
CS102
25 Hz to 50 kHz ground line CS
Ground wire for all electronic
equipment
CS103
15 kHz to 10 GHz antenna port
intermodulation CS
Applicable to receiving equipment,
including receivers and ampliﬁers, etc.
CS104
25 Hz to 20 GHz antenna port
undesired signal suppression CS
Applicable to receiving equipment,
including receivers and ampliﬁers, etc.
CS105
25 Hz to 20 GHz antenna port cross
modulation CS
Applicable to receivers that process
AM signals (this requirement is
currently less demanding on
spacecraft)
CS106
Power line spike signal CS
Applicable to equipment power lines,
not including ground and return lines
CS114
10 kHz to 200 MHz cable bundle
injection CS
Applicable to all interconnected cables
and power cables for the equipment
CS115
Cable bundle injection pulse excited
CS
Applicable to all interconnected cables
and power cables for the equipment
CS116
10 kHz to 100 MHz cable and power
line damp sinusoidal transient CS
Applicable to the interconnected cable
and power cable of all equipment, the
power return does not need to be tested
separately
CS118/CS112a
ESD CS
Applicable to equipment operating in
the environment that is prone to ESD
of the human body and may contact
with the human body
(continued)


170
6
EMC Design and Implementation of General Electronic Equipment
Table 6.2 (continued)
Items
Title of item
Application
RE101
25 Hz to 100 kHz magnetic ﬁeld RE
Applicable to equipment that has
limitation requirements of alternating
magnetic ﬁeld radiation, such as the
magnetic torque of spacecraft, LF
receivers, and other equipment casings
and their cable interfaces, is not
applicable to antenna radiation
RE102
10 kHz to 40 GHz electrical ﬁeld RE
Applicable to electric ﬁeld RE from
equipment and casing, all
interconnected cables, and antennas
permanently mounted on the EUT
(receiver and standby transmitter).
This item is not applicable to the
transmitter’s fundamental transmit
signal bandwidth or \pm5% frequency
range of the fundamental frequency
(whichever is greater)
RE103
10 kHz to 40 GHz antenna harmonic
and spurious output RE
Applicable to transmitters with
nonremovable antennas and can
replace CE106. This item is not
applicable to the transmitter’s
fundamental transmitting signal
bandwidth or \pm5% frequency range of
the fundamental frequency (whichever
is greater)
RS101
25 Hz to 100 kHz magnetic ﬁeld RS
Applicable to the equipment casing
and all interconnected cables, not
suitable for the equipment antenna
RS103
10 kHz to 40 GHz electrical ﬁeld RS
Applicable to the equipment casing
and interconnected cable, not suitable
for the tuning frequency of the receiver
connected to the antenna
SE
Electromagnetic leakage evaluation
Applicable to microwave passive
equipment
aCS112 is the item name used in China
(4) Equipment chassis and cable radiation ﬁeld interface: RE101, RE102, RS101,
RS103, and RF leakage.
An example of the receiver EMC interface requirements is shown in Fig. 6.19.


6.3 General EMC Analysis, Design and Implementation
171
Power conducted interface: CE101, CE102, 
CE107, CS101, CS102 and CS106
Antenna 
interface: 
CE106, 
RE103, CS103, CS104 and 
CS105
Chassis and cable radiation field 
interface: RE101, RE102, RS101, 
RS103 and RF leakage
Interconnecting cable 
conducted interface: CS112, 
CS114, CS115 and CS116
Fig. 6.19 Example of receiver EMC interface requirements
6.3
General EMC Analysis, Design and Implementation
6.3.1
Steady-State CE Design (CE101, CE102, CE106)
6.3.1.1
Design Requirements
(1) CE101 design requirements
The CE101 requirements are applicable to DC power lines for electromechanical
equipment such as spacecraft gyros and momentum wheels, including positive and
return lines, but not including the output wires of the EUT power supply. These
power lines are powered by a power source other than the EUT. Curve 1 in Fig. 6.20
is applicable to the power supply line with a voltage greater than 28 V, and curve 2
is applicable to the power supply line with a voltage not exceeding 28 V.
(2) CE102 design requirements
TheCE102requirementisapplicabletoDCpowerlinesandreturnlinesforspacecraft
equipment, but not includes the output wires of EUT power supplies. These power
lines are powered by the power source other than the EUT. The baseline CE limit on
the supply line for general satellite equipment (with a supply voltage less than 28 V)
shall comply with the baseline limits deﬁned in Fig. 6.21.


172
6
EMC Design and Implementation of General Electronic Equipment
10
0
10
1
10
2
10
3
10
4
10
5
60
70
80
90
100
110
120
Frequency (Hz)
Limit value 2
Limit value 1
Limit value (dB\muA)
> 28V
≦28V
Limit 1
Limit 2
Fig. 6.20 Power line CE limits for spacecraft electromechanical equipment
If the supply line is higher than 28 V supply line, the CE limit can be relaxed
by 0.5 [20log(V) −20 log(28)] (where voltage V is in volts) on the baseline limit
in Fig. 6.21. For equipment with an operating voltage of 100 V, the CE limit can
be relaxed by 5.5 dB. The fundamental frequency of the switching frequency of the
satellite secondary power supply, as well as the second and third harmonic point
frequencies, can be relaxed by 5 dB.
(3) CE106 design requirements
The requirements are applicable to the antenna ports of the transmitter, receiver, and
ampliﬁer of the spacecraft, but not applicable to equipment with a nonremovable
antenna. For this nonremovable antenna equipment, the RE103 test item can be used
to test the transmitter and ampliﬁer in the transmitting state.
However, the requirements are not applicable to the operating bandwidth of the
transmitter under test (transmitting state) or within \pm5% of its fundamental frequency
(whichever is greater). According to the operating frequency range of the EUT, the
test starting frequency is shown in Table 6.3.
The upper limit of the test frequency is 40 GHz or 20 times the highest operating
frequency of the EUT, whichever is smaller. For equipment using waveguides, the


6.3 General EMC Analysis, Design and Implementation
173
10
4
10
5
10
6
10
7
10
8
40
50
60
70
80
90
100
110
Basic limit
Frequency (Hz)
Limits (dB\muV)
Fig. 6.21 Power line CE limits for spacecraft equipment
Table 6.3 Relationship
between EUT operating
frequency range and test
starting frequency
Operating frequency range
Test starting frequency
10 kHz to 3 MHz
10 kHz
3 MHz to 300 MHz
100 kHz
300 MHz to 3 GHz
1 MHz
3 GHz to 40 GHz
10 MHz
requirements are not applicable if the frequency is less than 0.8 times the waveguide
cutoff frequency.
The EUT antenna ports CE should not exceed the following limits:
(a)
Receiver: 34 dB \muV;
(b) Transmitter and ampliﬁer (standby state): 34 dB \muV;
(c)
Transmitter and ampliﬁer (transmitting state): All harmonic emissions and
spurious emissions except the second and third harmonics are at least 80 dB
lower than the fundamental level, and the second and third harmonics should be
suppressed to −20 dBm or 80 dB lower than the fundamental level, whichever
is lower for suppression requirement.


174
6
EMC Design and Implementation of General Electronic Equipment
6.3.1.2
Analysis of Steady-State CE Characteristics
Steady-state CE typically includes common-mode (CM) interference emissions and
differential mode (DM) interference emissions. For DM interference, it is usually
controllable at lower frequencies (below about 2 MHz), beyond which the differential
interference ﬁlter’s ability to attenuate EMI is reduced due to the resonance of the
device. DM interference emissions mainly come from the switching frequency of
the power supply and its harmonic noise. Therefore, the inﬂuence degree of DM
interference is related to the repetition rate of the signal or the waveform with fast
rise and fall time. For CM interference, it is mainly caused by current ﬂowing through
the ground plane and ﬂowing in the same direction in the high-level line and the return
line of the power supply and the signal. The nonideal characteristics of electronic
equipment, such as parasitic capacitance which constitutes a HF current path, is the
major cause of CM interference, while at the DC and lower frequencies, the inﬂuence
of CM interference is not signiﬁcant.
Themosteffectivetooltocontrolsteady-stateCEistheEMIﬁlter.Generally,inthe
ﬁlter design, both CM and DM interference should be considered and suppressed. In
order to make full use of the HF suppression performance of the ﬁlter, the ﬁlter must
be shielded and well bonded. In addition to the ﬁlter, another method of controlling
the steady-state CE is to control the rise/fall time of the switching signal and the
parameters of the relevant components to reduce the harmonics of the switching
frequency.
1. DM emission
In EMC design, when DM emission is considered, since the fundamental frequency
and harmonics of the switching frequency have a greater effect during the steady-state
CE test, their interference should be ﬁltered out using a ﬁlter. In the lower frequency
band (such as the kHz band), the noise mainly enters the power line in the form of
DM coupling, therefore, a “line-to-line” ﬁltering method should be adopted.
In the design of a power ﬁlter, consideration must be given to the following three
aspects:
➀
When selecting the ﬁlter front-end capacitor for steady-state interference
(CE101, CE102), whether the requirement of transient CE (CE107) is met
should also be considered;
➁
The capacitors and inductors in the ﬁlter may have resonance problems, which
will affect the CS of the equipment (CS101). Adding a resistor to the ﬁlter can
reduce this resonance; the added resistance may affect the DC voltage of the
circuit, so a damping resistor is to be arranged in parallel with the inductance
of the ﬁlter front end;


6.3 General EMC Analysis, Design and Implementation
175
➂
Although the line ﬁlter is mainly used to control the DM current, it also helps to
control the CM current by properly distributing the inductance on the high-level
line and the return line.
(2) CM emission
The main cause of CM conducted emissions is that the internal circuits of the equip-
ment generated by the parasitic capacitance or the formation of a capacitance between
the equipment and the equipment housing, thus providing an interference current path
to ground. This parasitic or “scatter” capacitance causes the interference current to
enter the input power line from the equipment housing through the circuit.
There are three main methods for suppressing CM interference:
➀Place a bypass capacitor near the switching equipment (interference source) of
the equipment to provide a shorter loop to the source, which can reduce both the
interference of the power line and the radiation loop area of the CM interference.
In practice, in order to control the resonance of the capacitor and the inductor
in the circuit, a bypass capacitor and a damping resistor are usually used at the
same time;
➁A CM ﬁlter can also be used in the front-end circuit to suppress CM interference.
Usually, a CM choke is used, where the inductance can effectively suppress CM
interference on the power line.
➂Using spacers on both sides of the mounting surface can also suppress CM inter-
ference. These kind of spacers can be connected to the power switch components
via leads to provide an alternating path for the current to help ensure that the CM
current does not affect the input power line.
Attention should be paid to the following issues when suppressing CM interfer-
ence:
➀The resonant frequency of the component should be controlled by both the differ-
ential ﬁlter and the CM bypass capacitor. Due to the resonant frequency, when
the CS101 test is performed, the interference may be ampliﬁed at the resonant
frequency, thereby affecting the anti-interference performance of the equipment;
➁Both the bypass and front-end CM ﬁlters have “line-to-ground” capacitance. The
maximum allowable capacitance value must be considered to limit the “line-to-
ground” capacitance, thus effectively controlling the leakage current from the
chassis to the structure;
➂The radiated coupling interference around the ﬁlter should be reduced. If there
is a large current loop in the circuit, care should be taken to keep away from
the input ﬁlter during wiring design. Besides, the length of the wire should be
reduced, a ferrite bead should be added to enhance the HF ﬁltering effect, and
the ﬁlter is also to be shielded and isolated to reduce the inﬂuence of the radiated
coupling on the ﬁlter.


176
6
EMC Design and Implementation of General Electronic Equipment
6.3.1.3
Steady-State CE Control
1. DM ﬁltering
The front-end ﬁlter of the power supply is generally designed and analyzed according
to the performance curve of the ﬁlter. For example, the single-stage ﬁlter has a lower
cornerfrequencyandtheattenuationperformancevarieswithaslopeof20dB/octave;
incontrast, thesingle-stageLCﬁlter has ahigher corner frequencyandtheattenuation
performance varies with a slope of 40 dB/octave; and the two-stage LC ﬁlter has an
even higher corner frequency and the attenuation performance varies with a slope of
80 dB/octave. In the ﬁlter design, it is necessary to consider the form of the corner
frequency and the ﬁlter to ensure that the conducted interference is controlled within
the required range.
The fundamental frequency signal attenuation should also be enhanced in the ﬁlter
design. For example, a 100 V power supply equipment produces a ripple voltage of
1.1 V (120 dB \muV). Based on equipment-level EMC requirements (such as MIL-
STD-461), the required CE102 emission limit at 30 kHz is 90 dB \muV, which means
the ﬁlter should provide at least 30 dB of attenuation.
To design a power ﬁlter with a speciﬁc attenuation performance for a speciﬁed
frequency, the values of ﬁlter inductance L and capacitance C must be determined.
Generally, L and C are determined by
LC \approx

1

A\omega2
(6.3.1)
where A is the required attenuation performance;
\omega is the angular frequency.
In practice, the high-order ﬁlters are used so that more small inductors can be
used to replace large inductors; and relatively large capacitors can be used to reduce
the characteristic impedance.
(2) CM ﬁltering
In general, the parasitic capacitance, housing baseplate impedance, and LISN or
power bus impedance together constitute an interference path. The signal amplitude
in the CM path can be obtained by Fourier transforming of the signal. When the
frequency is sufﬁciently high, the parasitic capacitance becomes a shortcut to inter-
fere with the return source. Here is an example to illustrate the CM ﬁltering analysis
and design process. Consider a switching frequency of 120 kHz in a 100 V switching
power supply, where the signal is a trapezoidal wave with a 50% duty cycle, with
a signal width of 3.3 \mus, a rise/fall time of 100 ns, and a frequency of interest of
600 kHz.
The ﬁrst corner frequency is
f1 =
1
$\pi$(3.3 \mus) = 95.5 kHz
(6.3.2)


6.3 General EMC Analysis, Design and Implementation
177
At the 600 kHz frequency of interest, the change is
 = 20 log
 600 kHz
95.5 kHz

= 16.0 dB
(6.3.3)
For a signal of 100 V at 600 kHz, the amplitude is
20 log(100 V) + 120 −16.0 dB = 144.0 dB \muV
(6.3.4)
Assume that the impedance of the CM path is
Z = 20 log

1
2$\pi$(600 kHz)(150 pF)

= 65.0 dB 
(6.3.5)
then, the value of CE102 on the LISN at 600 kHz is measured as
144.0 dB \muV −65.0 dB −6 dB + 20 log(50 ) = 107.0 dB \muV
(6.3.6)
According to the CE102 limit requirement of 600 kHz, the requirements for the
ﬁlter can be determined.
(3) CE simulation analysis
In the product design phase, it is necessary to estimate the internal switching
frequency and ripple strength of the product to guide the design or selection of
the power supply ﬁlter, so that all the equipments on the same power supply bus are
compatible.
The switching power supply circuit of spacecraft active equipment is basically
consisted of four parts: an input ﬁlter, an output ﬁlter, a switching circuit, and a
control circuit, as shown in Fig. 6.22. The CE102 analysis process has the following
steps:
Switching circuit
Input filter circuit
Output filter circuit
Control circuit
Power Inout
Power output
Fig. 6.22 Schematic diagram of switching power supply


178
6
EMC Design and Implementation of General Electronic Equipment
(1) Modeling: The switching circuit and components are equivalent to the simula-
tion circuit diagram, and input to the simulation software. The simulation circuit
diagram should include LISN (Line Impedance Stabilization Network), input
ﬁltering circuit, switching circuit, and load circuit. Among them, the switching
circuit and the load circuit should be properly simpliﬁed to reduce the compu-
tational complexity. This section only considers the effect of switching interfer-
ence along the power supply line, regardless of the spatial coupling effect inside
the power supply.
(2) Calculating the allowable emission values: Calculate the maximum allowable
CE values on the power switching frequency and its harmonics according to the
CE102 limit curve.
(3) Filter performance simulation: Simulate and calculate the reverse suppression
performance according to the designed circuit model of the input ﬁlter. If the
voltage ripple on the power input port is less than the maximum allowable CE
value after all the interference frequencies of the power supply are suppressed
by the input ﬁlter, the ﬁlter design meets the requirements; otherwise, the
ﬁlter design parameters need to be re-optimized until their reverse ﬁltering
suppression performance meets the requirements.
Figure 6.23 gives an example of a simulation model established by Pspice soft-
ware, which, based on the operating parameters of the selected switching elements
and the parameters of subsequent circuit power and impedance, a schematic diagram
of the simulation calculation is obtained. Through simulation calculation, the
frequency points f i (kHz) and amplitude V i (mV) of the switching noise of the
power supply circuit is determined (i = 1, 2, 3, …, N, representing the fundamental
frequency of the switching frequency and each harmonic).
A 1.6 A constant load current is given at the power load and reﬂected back to the
bus through the switching action of the Buck circuit, as shown by the green pointer in
Fig. 6.23. Figure 6.24 shows the spectrum analysis of the bus current. The maximum
noise current at the equivalent switching frequency of 100 kHz is 835.5 mA. The
C14
10u
C13
0.33u
C4
0.25u
L8
5uH
L3
290uH
L7 50uH
C10
7.5u
R7
50
C3
8u
D9
D1N5811/27C
R11
45
D11
1
2
R4
0.01
C2
0.25u
L6
50uH
R10
1.8
V2
TD = 0
TF = 1n
PW = 7.2u
PER = 10u
V1 = 0
TR = 1n
V2 = 10
C6
10u
0
0
R17
50m
R5
5
第二级C滤波电路
R9
0.01
R1
0.15
R12
5
D10
1
2
C8
1p
R6
1k
I
0
C15
0.5u
C11
1p
C5
1p
V
0
L5
350uH
R14
50
0
R16
10m
功率负载
R3
1k
0
C9
1p
C1
8u
V3
100Vdc
0
R2
10m
R19
50m
Buck电路
LISN
C7
10u
L1
80uH
C12
0.165u
R13
1000000k
R18
2
R20
7m
R15
10
第一级LC滤波电路
1st stage LC filter circuit
2nd stage C filter circuit
Buck circuit
Power load
Fig. 6.23 Diagram of the simulation circuit of the input bus EMI ﬁltering circuit


6.3 General EMC Analysis, Design and Implementation
179
Frequency
0Hz
1.0MHz
2.0MHz
3.0MHz
4.0MHz
5.0MHz
6.0MHz
7.0MHz
ID(M1)
0A
0.5A
1.0A
1.5A
(100.000K,835.449m)
Fig. 6.24 Bus current spectrum
calculation of the voltage ripple caused by the interference current at the output port
of the input ﬁlter is:
Vi(dB \muV) = 20 \times log(Ii(mA)) + 20 \times log(Zi) + 60
(6.3.7)
where Zi is the input impedance of the switching circuit.
Calculate the emission requirements for the corresponding frequency points
according to the limit curve in the equipment-level EMC standard or model EMC
technical requirements. For spacecraft electronic equipment operating at 100 V, the
limit V f at 100 kHz is approximately 80 dB \muV. The suppression requirement of the
input ﬁlter is calculated using the following Eq. (6.3.8).
The calculation of the suppression parameters required for each interference
frequency of the power circuit is
Yi = Vi(dB \muV) −V f (dB \muV) + 6 dB,
(6.3.8)
where, 6 dB is the EMC design margin, which can be changed according to the
requirements of the model.
The inverse suppression index for the input ﬁlter at 100 kHz is calculated as
Y = 118.4 dB \muV −80 dB \muV + 6 dB = 44.4 dB
(6.3.9)
Based on the calculated indicators, the input ﬁlter design can be calculated and
optimized for the ﬁlter to be used, so that the suppression index at each interference
frequency point satisﬁes the requirements of Y i.


180
6
EMC Design and Implementation of General Electronic Equipment
6.3.2
Transient CE Design (CE107)
6.3.2.1
Design Requirement
This requirement applies to DC input power lines for spacecraft equipment with
built-in switches.
For CE107, the voltage and current are limited. For the voltage limit, it is required
to be +50 to 150% of the rated voltage of the DC power line. The amplitude of the
spike signal for the reference is the voltage of the power supply voltage waveform
occurred at the moment of switching operation, instead of the 0 V on the oscillo-
scope’s vertical axis; for the current limit, it is generally determined according to the
spacecraft’s construction speciﬁcations.
6.3.2.2
Implementation of Transient CE Characteristics Analysis
and Control
CE107 is a CE control requirement in the time-domain, which limits the effects of
the surge voltage or current on the conducted EM characteristics of the power line
during the switching operation of the equipment or during operation mode shift.
Although the limit is based on the voltage in CE107 required by the equipment-level
EMC, it is more often to limit the amount of current in the transient CE requirements
of spacecraft electronic equipment.
The most effective way for transient CE EMC design is designing a ﬁltering
circuit. In order to reduce the surge interference and meet the transient emission
requirements, the ﬁrst thing to consider in the ﬁltering circuit design is the size of
the ﬁlter front-end capacitor. If it is too large, a transient emission at the input supply
line will be generated, which is dependent on the time constant of the ﬁltered RC
circuit. This may result in the contradiction between the results and the design of the
steady-state CE ﬁltering circuit, so it must be fully considered in the design process.
To reduce the effect of the large-capacity capacitor on the front end of the ﬁltering
circuit, an effective way is to use a soft start-up design to extend the power-on time.
Figure 6.25 shows a circuit design that uses a resistor to form a switching bypass.
As the circuit depicted in Fig. 6.25, the power-on time is delayed until the switch
is fully engaged. When the time constant of the designed RC circuit is smaller than
the time of the switching action, the transient effects caused by switching-on can be
minimized. If a delay type switch is used, the switch must not be engaged until the
large capacitor is charged to a level close to the input voltage, so the corresponding
additional circuit is not required. Moreover, the switch can be placed close to the
large capacitor instead of using a soft-start circuit to increase the delay time of the
switch. If the capacitance in the additional switching delay circuit is too large, there
is also a RC time constant problem. Generally, the resistance values range between
0.5 and 5 .


6.3 General EMC Analysis, Design and Implementation
181
+
-
R
C
Relay coil
Power circuit
Fig. 6.25 Soft-start switch circuit design
In the design of the ﬁltering circuit, the limits of voltage or current and transient
conducted interference on the line should be jointly considered. In the analysis and
design process, it is required to obtain the resistance between the power supply and
the equipment. If the resistance is unknown, the resistance value of the LISN can
be used. For example, if the power line voltage of a piece of equipment is 100 V,
the EMC standards require that the transient voltage not exceed 50% of the rated
voltage, or 50 V, for a duration of 10 \mus. Assuming the line resistance is 0.9 , then
50 V = 100 V \times
	
1 −e
−10 \mus
C\times0.9 

(6.3.10)
The resulted capacitance value is 16 \muF.
In addition to the above RC circuit design, transistors can also be used for soft-start
switch circuit design, as shown in Fig. 6.26. When using this method, the key is to
+
-
R
C
CT
Q
V
RT
Power circuit
Fig. 6.26 Soft-start switch circuit using MOSFET


182
6
EMC Design and Implementation of General Electronic Equipment
delay the establishment of the supply voltage after the transistor Q is started. In order
to satisfy the required switching characteristics, the RT and CT parameters should
be designed and selected to adjust the time parameters. When using a current-driven
transistor, an inductor should be designed at the primary end of the converter to delay
the start of the transistor. When selecting the inductor, the time constant of the LC
should meet the requirement of the delay time.
If it is found that the transient emission is not satisfactory after the design is
completed, and the circuit board can no longer be modiﬁed, then a soft-start switch
circuit can help. If the internal space of the equipment is not large enough and the
MOSFET is not suitable for installation outside the equipment casing, a relay-type
soft-start switch circuit can be used outside the equipment.
6.3.3
Steady-State CS Design (CS101, CS102, CS103, CS104,
CS105, CS114)
6.3.3.1
Design Requirements
1. CS101
This requirement is applicable to DC power lines for spacecraft equipment except
return lines.
The general CS101 limits for spacecraft equipment are shown in Table 6.4 and
Fig. 6.27. When tested at the speciﬁed test signal level, the EUT must not exhibit
any fault, performance degradation or deviations from the speciﬁed index values, or
exceed the speciﬁcation tolerances speciﬁed in a certain technical condition.
If a speciﬁed signal source is used, when the power shown in Fig. 6.28 is consumed
on a 0.5  load, in case that the voltage at the input of the sample power supply still
does not reach the required value, as long as the sample is not sensitive to this power
signal, it can also be regarded to meet this requirement.
2. CS102
This requirement is mainly applied to spacecraft equipment and subsystems sensitive
to ground line LF interference signals.
The limit requirement is that when 25 Hz to 50 kHz and 1 V open-circuit voltage
signal is injected in the ground line, the EUT must not exhibit any faults, performance
degradation or exceed the index tolerance speciﬁed in the product speciﬁcation.
Table 6.4 Relationship
between the EUT voltage and
the test signal
EUT supply voltage
Test signal magnitude
\geq28 V
Limit 1 performance level
\geq12 V and <28 V
Limit 2 performance level
\geq5 V and <12 V
Limit 3 performance level
<5 V
Limit 4 performance level


6.3 General EMC Analysis, Design and Implementation
183
10
1
10
2
10
3
10
4
10
5
95
100
105
110
115
120
125
130
限值1
限值2
限值3
限值4
Limit 1
Limit 2
Limit 3
Limit 4
Frequency (Hz)
Limit (dB\muV)
Fig. 6.27 Power line CS voltage limits for spacecraft equipment
3. CS103
This is applicable to spacecraft receivers such as RF receivers, preamps.
As speciﬁed in the EUT product speciﬁcation, the signal generator used in this
test should always be modulated in the same way as that used for EUT sensitivity. If
there is no corresponding regulation, the following modulation methods should be
used:
(1) AM receiver. The signal generator is amplitude modulated with a 400 Hz sine
wave, and the modulation degree is 30%;
(2) SSB receiver. The signal generator is not modulated.
(3) FM receiver. The signal generator is frequency modulated with a 1 kHz sine
wave, the frequency offset is 10 kHz;
(4) Pulse receiver. The modulation pulse is regulated so that 80% of its spectral
energy is within the receiver’s 3 dB bandwidth.
The standard reference output level shall be speciﬁed in the EUT product
speciﬁcation; if not, the following standard reference output shall be used:
(1) AM receiver: (S + N)/N = 10 dB
(2) SSB receiver: (S + N)/N = 10 dB.


184
6
EMC Design and Implementation of General Electronic Equipment
10
1
10
2
10
3
10
4
10
5
10
-2
10
-1
10
0
10
1
10
2
Frequency (Hz)
Power limit (W)
Fig. 6.28 Power line CS power limits for spacecraft equipment
(3) FM receiver:
Modulated: (S + N)/N = 10 dB;
Not modulated: The squelch level is 10 dB.
(4) Pulse receiver: (S + N)/N = 10 dB.
In the above formulas, S is the signal size, N is the noise of the receiver under
test.
4. CS104
This requirement is applicable to spacecraft receivers such as RF receivers, preamps.
The limit requirement is the same as that of CS103.
5. CS105
This requirement is applicable to receivers on spacecraft that process AM informa-
tion. The limit requirement is the same as that of CS103.


6.3 General EMC Analysis, Design and Implementation
185
10
-2
10
-1
10
0
10
1
10
2
40
50
60
70
80
90
100
89
Frequency (Hz)
Limit (dB\muA)
Fig. 6.29 Cable bundle injection CS limits for equipment outside the spacecraft
6. CS114
This requirement is applicable to equipment interconnected cables that are exposed
outside the spacecraft, including power cables. The limit requirements are shown in
Fig. 6.29.
6.3.3.2
Steady-State CS Characteristics Analysis
The steady-state CS design mainly aims to control the audio and RF interference
signal strength on the input power line and the interconnected cables of the electronic
equipment, and to improve the anti-radiated interference capability of the equipment.
1. Resonant frequency suppression of the power ﬁlter
The ﬁlter on the power line, in addition to meeting the requirements for steady-state
CE in (6.3.1) and transient CE in (6.3.2), must also meet the CS requirements.
To meet the steady-state CS requirements, it is necessary to control the resonant
frequency of the inductor and capacitor in the ﬁlter. The suppression resistor is
typically connected in series or in parallel with the ﬁlter element, which can reduce


186
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.30 Resonance
suppression ﬁltering circuits
RL
RC
L
C
(a) Filtering circuit for series resonance suppression resistor
R
L
C
(b) Filtering circuit for parallel resonance suppression resistor
its effect on power consumption while reducing resonance. The circuits of the series
and parallel resonance suppression resistors are shown in Fig. 6.30a, b, respectively.
For CM input ﬁlters, since the inductor has a certain impedance in the HF band,
the resonance suppression resistor is usually not used. Ferrites and coils also have a
certain resistance loss, which is equivalent to a series resistance in the circuit, thus
playing the role of a resonance suppression resistor.
In the circuit shown in Fig. 6.30a, (RL + RC) >

4L

C;
In the circuit shown in Fig. 6.30b, R >

L

4C.
2. Design of the signal ﬁlter
The ﬁlter in an analog signal line can be connected to a capacitor at the analog signal
output. The form of the ﬁlter is generally an RC low-pass ﬁlter network, and the ﬁlter
structure may be of L-, - or T-type. The CM interference on the signal line can be
ﬁltered using a ferrite magnetic ring.
The ﬁlter in a digital signal line can be connected to a low-pass ﬁlter. The ﬁlter
structure can be of L-, - or T-type, or an HF ﬁlter capacitor may be added to the
connector port.
The interference can be ﬁltered by installing a data line ﬁlter on the signal line and
connecting a bypass ﬁlter capacitor to the ground, as shown in Fig. 6.31. However,
Fig. 6.31 Signal line ﬁlter
Signal line


6.3 General EMC Analysis, Design and Implementation
187
note that the resonance effect of the ﬁlter capacitor will affect the ﬁltering perfor-
mance. Once the resonant frequency is exceeded, the capacitor will show inductance
characteristics, which will affect the ﬁltering effect.
If the signal line of the electronic equipment is required to be protected against
the steady-state conducted interference of CS114, in addition to the ﬁltering design,
cable shielding measures should also be considered. In the cable shielding design,
the connector and the cable should be 360^\circ shielded, thus avoiding “Pigtail” type
grounding. 360^\circ shielding coverage means there are no gaps or exposed areas
around the cable and connector root. After shielding, the DC impedance between
the connector and the cable shield shall not exceed 10 m. A double-end grounding
method is recommended.
6.3.3.3
Implementation of Steady-State CS Control
Taking CS101 as an example, the power bus interference voltage suppression require-
ment of single equipment is analyzed and calculated to ensure that the interference
applied by the CS101 test items does not cause a change in the output voltage.
The power line CS101 has an interference frequency of 25 Hz to 150 kHz, and
a maximum interference of 5.7 Vp–p can be superimposed on the bus. Assume that
the interference amplitude needs to be controlled within 100 mVp–p to ensure the
performance of the equipment, then the ﬁlter is required to provide a suppression
of more than −35.1 dB. Based on the above analysis, simulation analysis should be
done on the input ﬁlter and control loop.
6.3.4
Transient CS Design (CS106, CS115, CS116)
6.3.4.1
Design Requirements
1. CS106
This requirement is applicable to the input power line of spacecraft equipment with
the exception of ground and return lines.
The limit is 100% of the power supply voltage, and the signal form is shown in
Fig. 6.32.
2. CS115
This requirement is applicable to all interconnected cables for spacecraft equipment,
including power cables. The limit requirements are shown in Table 6.5.


188
6
EMC Design and Implementation of General Electronic Equipment
Time (\mus)
Voltage (v)
Vp -Peak voltage,V
Fig. 6.32 CS106 signal waveform
Table 6.5 Equipment-Level cable bundle injection excitation CS requirements
Equipment category Test requirements
Cat. I
(1) If the actual voltage of the cable is greater than or equal to 28 V, it is
required to pass the 5 A performance level
(2) If the actual voltage of the cable is greater than 12 V but less than
28 V, it is required to pass the 3 A performance level
(3) If the actual voltage of the cable is less than or equal to 12 V, it is
required to pass the 1 A performance level
Cat. II
Cat. III
(1) If the actual voltage of the cable is greater than or equal to 28 V, it is
required to pass the 3 A performance level
(2) If the actual voltage of the cable is less than 28 V, it is required to pass
the 1 A performance level
3. CS116
This requirement is applicable to all interconnected cables for spacecraft equipment,
including power cables. During the test, the EUT should meet the corresponding
susceptibility test criteria. The test should be carried out at least at the following
six frequencies: 10 kHz, 100 kHz, 1 MHz, 10 MHz, 30 MHz and 100 MHz. In this
test, the peak interference levels applied to the cables of different working voltages
shall be in accordance with Table 6.5. The interference peaks applied at different
frequency points are the current values in Table 6.5 multiplied by the peak current
coefﬁcients shown in Fig. 6.33.


6.3 General EMC Analysis, Design and Implementation
189
10
-2
10
-1
10
0
10
1
10
2
10
-2
10
-1
10
0
Frequency (Hz)
Peak current coefficient
Fig. 6.33 Cable bundle injection damping sinusoidal transient CS limit curve for spacecraft
equipment
6.3.4.2
Implementation of Transient CS Analysis and Control
The transient CS design of spacecraft electronic equipment is mainly implemented
to meet the requirements of CS106, CS115, and CS116. While the CS106 focuses on
the ﬁltering of spike signals on the power line, the CS115 and CS116 may consider
the combined protective design of ﬁltering and cable shielding.
The ﬁlter design of transient conducted interference is introduced by taking CS106
as an example. As shown in Fig. 6.34, assume that the power supply voltage of the
electronic equipment is 100 V and the CS106 requires the interference level to be
100% of the rated voltage, then the peak voltage superimposed on the input end of
the equipment is 200 V; if the front-end device of the equipment can only withstand
a port voltage of 180 V, in the actual test, at least a maximum voltage of 180 V should
be injected into that equipment port, so we have
Rs
(Rf + Rs) = 180 V −100 V
100 V
,
(6.3.11)
where Rs is the source resistance;
Rf is the ﬁlter equivalent resistance.


190
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.34 CS106 test
equivalent circuit model
Rf
DC
Rs
So
Rs
Rf
= 4
(6.3.12)
From the above equation, if the source resistance is large, it is relatively easy to
design the ﬁlter to meet the equivalent resistance requirement. However, if the source
resistance of the electronic equipment is small, it is difﬁcult to design a ﬁlter with a
small equivalent impedance.
When designing ﬁlters for interconnected signal cables, the capability of the ﬁlter
to withstand transient conducted interference should be improved, especially the
sustainability of multiple interferences of the ﬁltering circuit and components. There
have been a case in which an electronic equipment was under CS116 test, during
testing of each frequency point in the sequence, the cumulative effect of the injection
interference caused damage to the components of the interface circuit.
6.3.5
Radiated Emission Design (RE101, RE102, RE103)
6.3.5.1
Design Requirements
1. RE101
This requirement is generally applicable to the equipment on spacecraft with limited
requirement for alternating magnetic ﬁeld radiation, such as spacecraft magnetic
torque,LFreceivers,andallREininterconnectedcables,butnotapplicabletoantenna
radiation.


6.3 General EMC Analysis, Design and Implementation
191
10
1
10
2
10
3
10
4
60
70
80
90
100
110
120
130
140
150
85
3.5k
Frequency (Hz)
Limit (dBpT)
Fig. 6.35 RE101 limit curve
The incidental magnetic ﬁeld emission at 7 cm from the outer casing of the
spacecraft equipment shall not exceed the limits speciﬁed in Fig. 6.35.
2. RE102
This requirement is applicable to the electric ﬁeld RE of spacecraft equipment and
subsystems and their interconnected cables. This item is not applicable to the trans-
mitter’s fundamental transmit signal bandwidth or the \pm5% frequency range of the
fundamental frequency (whichever is greater). Incidental electric ﬁeld RE at 1 m from
the spacecraft equipment casing shall not exceed the limits speciﬁed in Fig. 6.36.
For speciﬁc spacecraft and launch vehicles, the corresponding operating frequency
bands shall be strictly protected according to the spacecraft RF receiving information
and the launch vehicle manuals. In the frequency band below 30 MHz, the vertical
polarization ﬁeld should meet the limit requirements. In the frequency band above
30 MHz, the horizontal polarization ﬁeld and the vertical polarization ﬁeld should
both meet the limit requirements.


192
6
EMC Design and Implementation of General Electronic Equipment
10
4
10
5
10
6
10
7
10
8
10
9
10
10
40
45
50
55
60
65
70
75
80
44
18G
Limits (dB\muV)
Fig. 6.36 Electric ﬁeld RE limits for spacecraft equipment
For different spacecraft equipment, the test frequency is shown in Table 6.6.
3. RE103
This requirement is applicable to transmitters with nonremovable antennas, and the
testitemscanreplacethatoftheCE106test.However,CE106testshouldbepreferred,
unless the design features of the equipment and subsystems affect its function. If the
harmonic and spurious emissions of the EUT are below the applicable limits for the
RE102 electric ﬁeld RE, it is considered to meet this requirement.
This requirement is not applicable to the EUT’s fundamental transmit signal band-
width or \pm5% of the fundamental frequency (whichever is greater). The starting
frequency of the test shall be determined according to the operating frequency range
Table 6.6 Relationship
between EUT operating
frequency and test frequency
EUT highest internal frequency
Test frequency
10 times the EUT highest internal
frequency <1 GHz
10 kHz to 1 GHz;
1–18 GHz strict band
10 times the EUT highest internal
frequency \geq1 GHz
10 kHz to 18 GHz;
18–40 GHz strict band


6.3 General EMC Analysis, Design and Implementation
193
of the EUT, see Table 6.6. The upper limit of the test frequency is 40 GHz or 20
times the highest operating frequency of the EUT, whichever is smaller. For equip-
ment using waveguides, this requirement is not applicable for frequency range below
0.8 times the waveguide cutoff frequency. Except for the second and third harmonics,
all harmonic emissions and spurious emissions should be at least 80 dB lower than
the fundamental level. The second and third harmonics should be suppressed to −
20 dBm or 80 dB lower than the fundamental frequency, whichever the suppression
requirement is lower.
6.3.5.2
Analysis of RE Characteristics
The RE design of spacecraft electronic equipment is mainly implemented to meet
the requirements of RE101, RE102, and RE103. The RE101 design focuses on the
control of magnetic ﬁeld RE of electronic equipment and its interconnected cables,
refer to Chap. 9 for details; the RE102 design focuses on the control of electric ﬁeld
RE of electronic equipment and its interconnected cables.
The most effective way to control the electric ﬁeld RE from a piece of electronic
equipment is to shield the casing of the equipment. If the shielding is well designed,
most of the EMI will be constrained inside the equipment. At this time, a good
grounding of the equipment casing will help to suppress the internal interference. In
addition, the conductor or cable has an antenna effect, and the interference signal also
generates EM radiation through the cable. Therefore, it is necessary to synchronously
control the conducted interference, especially the CM interference.
In the design of electronic equipment, when the interference generated by the
sourceexistsinformofavoltage,itisrequiredtotakeelectricﬁeldshieldingmeasures
to ensure a good grounding to the shielded casing, with a grounding resistance less
than 2.5 m. If the interference generated by the source exists in the form of a current,
the magnetic ﬁeld shielding measures should be considered. When the frequency
of the interference source is lower than 100 kHz, ferromagnetic materials with high
magnetic permeability may be used for shielding. Note that the shielding case should
avoid opening in the vertical direction of the magnetic ﬂux. If the frequency of the
interference source is higher than 100 kHz, it should be shielded with a good conduc-
tive material, and the thickness of the shielded casing should meet the requirements
of the mechanical structure.
If there is a large opening in the equipment housing, it is recommended to replace
the opening with an array of holes in the same area, as shown in Fig. 6.37.
6.3.5.3
Implementation of RE Control
For a particular EUT, there must be the frequency segment (point) where the RE is
out-of-limits. At the beginning of the design, an estimation of the RE value on the
frequency segment (point) where the RE may be out-of-limits, can help to ﬁnd the


194
6
EMC Design and Implementation of General Electronic Equipment
Replaced by
Fig. 6.37 A large opening is replaced by an array of holes
problem in advance, and improvement measures should be taken to improve the test
pass rate.
To estimate the RE value, it is required to calculate the frequency point at which
RE may be generated according to the product’s limit curve. Assume that Pt is the
maximum transmit power, the maximum limit value of Pt is the maximum power
value Pmax [dBm] of the frequency point in the circuit. In this case, if the SE of the
equipment casing at this frequency is SE, the required limit value is L [dB \muV/m],
the safety margin is SA [dB], let Lc be the exceeded radiation value, then
Lc = Pmax + 104.77 −L −|SE| + SA.
(6.3.13)
If the result of Lc is positive, there is a risk of RE102 exceeding the standard; if the
result of Lc is negative, the equipment is considered to meet the RE102 requirement.
Here is an example to describe the analysis process of a piece of equipment. There
is a local oscillator signal in a transponder, the signal frequency is 6.3 GHz and the
signal size is 10 dBm, which may have a risk of RE exceeding the standard and
requires an RE estimation. The required RE102 limit of the transponder at 6.3 GHz
frequency is 35 dB \muV/m, and there is also a special band requirement of 1.5 GHz
with a limit value of 10 dB \muV/m. Due to the presence of a 4-way circuit of the local
oscillator signal in the circuit, the frequency of 1.5 GHz just falls within the concave
frequency range, where the limit is 25 dB lower than that of the local oscillator
frequency, while the signal power level is only about 20 dB smaller than the local
oscillator signal, so there is also a risk of RE exceeding the standard. Therefore, the
SE of the transponder casing at the above frequency is about 60 dB. Substituting
these values into the Eq. (6.3.13)
At 6.3 GHz frequency : Lc = Pmax + 104.77 −L + SE
= 10 + 104.77 −60 −35 −6 = 25.77 > 0;
At 1.5 GHz frequency: Lc = Pmax + 104.77 −L + SE
= −10 + 104.77 −10 −65 −6 = 24.77 > 0;


6.3 General EMC Analysis, Design and Implementation
195
It is known that there is a risk of RE exceeding the standard on both frequencies.
According to the above analysis, shielding measures should be taken to the internal
circuits when a product is realized, such as designing a separate blind cavity for the
local oscillator circuit, increasing the bonding area of the cover plate to improve the
SE of the cavity, using feed-through capacitor, and shielding of vital interconnected
cables inside the equipment.
6.3.6
Radiated Susceptibility (RS) Design (RS101, RS103)
6.3.6.1
Design Requirements
1. RS101
Thisrequirementisgenerallyapplicabletotheequipmentinstallednearthespacecraft
magnetic moment bar and all its interconnected cables, but not applicable to the EUT
antenna.
When tested in the magnetic ﬁeld using the signal strength as shown in Fig. 6.38,
10
1
10
2
10
3
10
4
10
5
100
110
120
130
140
150
160
170
180
190
Frequency (Hz)
Limit (dBpT)
Fig. 6.38 RS101 limit curve


196
6
EMC Design and Implementation of General Electronic Equipment
10
-2
10
0
10
2
10
4
2
4
6
8
10
12
14
16
18
20
22
生存级
工作级
性能级
生存级
工作级
性能级
Frequency (MHz)
Limit (V/m)
Survival level 
Working level
Working level
Performance 
level
Performance 
level
Survival level 
Fig. 6.39 RS103 limit curve
the EUT shall not exhibit any fault, performance degradation or deviation from the
speciﬁed index value, or exceed the index tolerance speciﬁed by special technical
conditions.
2. RS103
This requirement is applicable to spacecraft equipment and subsystems and their
interconnected cables. Unless otherwise speciﬁed, it is not applicable to the operating
frequency band of the receivers which are connected with an antenna.
When tested in the radiated electric ﬁeld as required in Fig. 6.39, the EUT shall
meet the corresponding SE test criteria. At 30 MHz and below, it should meet the
vertical polarization ﬁeld requirements; above 30 MHz, it should meet both the
horizontal and vertical polarization ﬁeld requirements.
6.3.6.2
Analysis of RS Characteristics
The electromagnetic RS design of spacecraft electronic equipment is mainly imple-
mented to meet the requirement of RS101 for antimagnetic ﬁeld interference design,
and that of RS103 for anti-electric ﬁeld interference design. The external EM ﬁeld


6.3 General EMC Analysis, Design and Implementation
197
360^\circshielding
Fig. 6.40 Schematic diagram of electrical connectors shielding
can enter the inside of the equipment directly or in a coupled form to affect the circuit
inside the chassis and generate interference current in the cables.
The most effective way to protect against electromagnetic radiated interference
is to design an entire housing of equipment in the form of a Faraday cage to reduce
the effects of external electromagnetic ﬁelds on the internal circuits of the equip-
ment. However, in actual equipment design, there will be openings and electrical
connectors, which will reduce the SE of the equipment.
In addition, the area most susceptible to external RE is the electrical connector
through which the cable enters the housing. The basic principle is to design a 360^\circ
shielded cable, as shown in Fig. 6.40.
6.3.6.3
Implementation of RS Control
In the initial stage of product design, according to the susceptibility requirements
of the product, an estimation of the frequency points where susceptible phenomena
may occur can help to ﬁnd the defects of the product in advance, and corresponding
measures can be taken to improve the test pass rate, thus saving manpower and
material resources.
The RS103 test method is to apply a certain electric ﬁeld in the space where the
product is located to assess the susceptibility of the product to the electric ﬁeld. For
general microwave-based active equipment, the electric ﬁeld RS requires that the
output clutter suppression of the EUT is greater than 50 dBc. The RS103 analysis
usually uses Eq. (6.3.15).
The speciﬁc analysis process is:
(1) Analyze the signal frequency f (Hz) that may cause RS. In general, there are
two conditions that may cause product RS. One is that the interference signal
frequency coincides with the main operating frequency or frequency band of
the product, the other is that the LF interference signal is superimposed on the
operating frequency or frequency band of the product after modulated by the
internal circuit of the product. If there is a possible modulation, the frequencies
for both cases must be considered;
(2) Check the limit curves speciﬁed by the EMC technical requirements or speciﬁ-
cations of the product model, and obtain the interference value E (V/m) required
at the analysis frequency point;


198
6
EMC Design and Implementation of General Electronic Equipment
(3) Obtain the EM shielding value SE (dB) of the product housing at that frequency;
(4) Substitute the value into Eq. (6.3.3) to calculate the size of the interference
signal that ultimately leaks into the product
Pin = 20 log10 E + 162.79 −20 log10 f −SE,
(6.3.14)
where Pin is the magnitude of the interference signal leaking into the product in
dBm;
E is an externally applied electric ﬁeld in V/m;
F is the frequency in Hz;
SE is the electric ﬁeld SE of the equipment in dB;
(5) Further, analyze the potential impact of the interference signal on the equipment.
For example, for RF equipment such as transmitters and ampliﬁers, the clutter
suppression of the output signal can be directly calculated using Eq. (6.3.4)
S = Pin −Pmin + A + SA,
(6.3.15)
where S is the output clutter suppression in dB;
Pin is the interference signal entering the equipment in dBm;
Pmin is the minimum power value of the output signal in dBm;
A is the gain of the transmitter in dB;
SA is the safety margin in dB.
The analysis process is described by taking a solid-state ampliﬁer as an example
(1) The solid-state ampliﬁer operating frequency is 1.684 GHz and the working
bandwidth is 200 MHz. The most direct effect of the RS103 test is that when
the interference frequency is within its working band, it will generate clutter
interference at the output;
(2) In the EMC technical requirements, the RS103 test baseline for the solid-state
ampliﬁer is in the frequency range of 1–18 GHz, and the required interference
value is 20 V/m;
(3) Assume that the EM SE the solid-state ampliﬁer chassis and port can provide
at 1.684 GHz is 60 dB;
(4) Substitute the above data into Eq. (6.3.16)
Pin[dB m] = 20 log10 E + 162.79 −20 log10 f −SE
= 20 log10 20 + 162.79 −20 log10(1, 684, 000, 000) −60 = −55.72 (dB m)
(6.3.16)
(5) The magnitude of the output signal is 40 dBm and the gain is 60 dB; the output
clutter suppression obtained from Eq. (6.3.17) is
S = Pin −Pmin + A + SA = −55.72 −40 + 60 + 6 = −29.72
(6.3.17)


6.3 General EMC Analysis, Design and Implementation
199
The clutter suppression of the solid-state ampliﬁer is generally −50 dB, which
has a risk of exceeding the standard in the RS103 test. In the process of product
realization, it is necessary to improve the shielding design and take measures
such as coating conductive adhesive on the housing to improve the SE of the
equipment.
6.3.7
Electrostatic Discharge (ESD) Susceptibility Design
6.3.7.1
Design Requirements (CS112)
This requirement is applicable to equipment that may work in an environment that
is prone to human body ESD or that may contact with the human body. Since the
ESD test can have cumulative damage to components, this requirement is applicable
to the electrical test units or qualiﬁcation test units of spacecraft equipment and
subsystems. It is recommended not to conduct this test on ﬂight units.
This test typically uses a voltage with a contact discharge of \pm5 kV and an air
discharge of \pm10 kV. During the test, the EUT shall not exhibit any faults, perfor-
mance degradation or deviation from the speciﬁed limits, or exceed the speciﬁed
tolerances in the technical speciﬁcations. The test methods include direct discharge
and indirect discharge. The equipment contacting with the human body should
perform both direct and indirect discharge tests, other equipment only performs
indirect discharge. Use the limits speciﬁed in the corresponding requirements unless
otherwise speciﬁed, in the technical requirements documents.
6.3.7.2
Implementation of ESD Susceptibility Characteristics Analysis
and Control
The ESD protection design of spacecraft electronic equipment includes two aspects:
the anti-ESD design, and the process control of ESD protection during the
development.
In the ESD protection design, it is preferred to use the components with the
highest ESD susceptibility level available. The external ESDS protection network of
the component design should base on the full understanding of whether there is an
ESDS protection network within the selected components and its effectiveness. After
assembly of the ESDS components, use proper ESD protection design, consider the
printed board assembly I/O port as an extension of the ESDS component pins. The
ESD protection design and measures should be implemented on the lowest possible
assembly level, which can more effectively achieve the purpose of assembly and
equipment-level ESD reinforcement. Circuit analysis can determine if assemblies
and equipment with ESDS components are reinforced to achieve the required ESD
protection capability.


200
6
EMC Design and Implementation of General Electronic Equipment
The design focuses on ESD protection for CMOS devices. The signal voltage at
the input end of the CMOS circuit V i (including transient voltage) is limited within
the range of VSS \leqV i \leqVDD, and the excess input terminals are not suspended,
they are connected to VDD or VSS by the logic state and according to the speciﬁc
condition to control the rising and falling time of the input signal. When there is
a long line at the input end, with the parasitic inductance in the transmission line
and the increase of the parasitic capacitance between the transmission lines, the input
terminal is susceptible to external interference such as EDS or signal coupling. In this
case, an RC ﬁltering circuit can be used. The CMOS circuit power supply port end
is series connected to a resistor to limit the current, and the limiting resistance value
should be selected according to speciﬁc equipment. Moreover, decoupling capacitors
are installed near the power and ground pins in the CMOS circuit package.
The equipment casing should be a closed metal casing, with the bonding resistance
of the equipment not more than 0.2 m; the DC resistance between the electrical
connector housing and the box is not more than 2.5 m.
In addition, attention should be paid to the design of isolated conductors inside
the equipment. In principle, all metal structural parts and isolated conductors with a
surface area greater than 3 cm2 or a length greater than 25 cm should be bonded to
the structural ground, and the grounding resistance should be less than 100 M.
The ESD protection process control of spacecraft electronic equipment plays an
important role in the development of equipment. For electronic products with ESDS
voltagenotlessthan100V(HBM),inallstepsofthedevelopment,includingprocure-
ment, manufacturing, processing, assembly, integration, packaging, labeling, main-
tenance, failure analysis, testing, inspection, storage and transportation, the ESD
protection measures must meet the requirements, such as grounding/equipotential
connection system, personnel grounding, tool and equipment grounding, electro-
static protected area (EPA), packaging, marking, and personal safety. The electro-
static protection system consists of electrostatic protection grounding system and
facilities associated with the system, such as countertops, cabinets, shelves, antistatic
ground, antistatic work clothes and wristbands, antistatic workbench, antistatic trans-
port vehicles and packaging, antistatic tools. In order to ensure the safe and effective
operation of the electrostatic protection system, all components of the system shall
be fully tested in accordance with the test equipment, test items, test methods, result
processing methods, and test cycles speciﬁed in relevant standards. For electronic
products with static sensitive voltages not less than 100 V (HBM), relevant operations
should be performed in the EPA.
There are two types of EPAs, Type I and Type II. Type I EPA refers to areas for
direct contact and disposal of electrostatic sensitive devices, components (circuit
boards), such as warehouse, component screening, aging and testing, electrical
assembly, circuit board veneer debugging, maintenance, inspection and cleaning,
equipment debugging, and areas where cables directly connected to the static sensi-
tive equipment is located. Type II EPA refers to areas where static sensitive equip-
ment is disposed of, such as equipment environmental test, burning-in area, areas
with electrostatic sensitivity requirements, including assembly and ﬁnal assembly
and equipment warehouse, etc. The spacecraft products manufacturers and users


6.3 General EMC Analysis, Design and Implementation
201
Table 6.7 EPA arrangement requirements
No.
Required item
Type I EPA
Type II EPA
1
Labeling
\sqrt
\sqrt
2
Antistatic ground
\sqrt
\sqrt
3
Antistatic workbench
\sqrt
\sqrt
4
Antistatic storage shelves/cabinet
\sqrt
\sqrt
5
Antistatic chairs
\sqrt
◯
6
Antistatic mobile devices
△
◯
7
Antistatic packaging
\sqrt
◯
8
Antistatic clothes/caps
\sqrt
\sqrt
9
Antistatic shoes
\sqrt
\sqrt
10
Disposable antistatic shoe cover
\sqrt
\sqrt
11
Antistatic gloves, ﬁnger cots
△
△
12
Antistatic wrist strap
\sqrt
\sqrt
13
Antistatic tool
\sqrt
◯
14
Antistatic ion fan
△
◯
15
Antistatic coating, resistance reducer
◯
◯
16
Temperature and humidity measuring instrument
\sqrt
\sqrt
17
Human body static tester
\sqrt
\sqrt
18
Wrist strap tester
◯
◯
19
Wrist strap continuous detector
△
–
20
Electric iron tester
△
–
21
Noncontact electrostatic voltmeter
◯
◯
shall properly arrange EPA according to relevant requirements. The arrangement
requirements are shown in Table 6.7.
6.4
Design Cases
Currently, the main RF receiving frequency band of spacecraft is above 1 GHz. The
EMI frequency generated by the crystal oscillator or switching frequency harmonics
of the electronic equipment is in the kHz or MHz frequency band level, which will
not cause EMI to the HF receiving frequency band. However, because the harmonic
interference frequency band of the digital circuit described in Sect. 6.2.1 mainly
determined by the rise time and signal width time of various clocks or crystal oscil-
lator signals, not solely related to the frequency of the signal, and due to the high
sensitivity of the spacecraft RF receivers, the EM emissions of LF digital equipment
may still generate EMI at HF band.


202
6
EMC Design and Implementation of General Electronic Equipment
Assume that the digital circuit signal voltage amplitude is 5 V, the frequency is
872 kHz, and the signal rise time is 200 ps, we analyze the two frequency bands of
L-band (1350 MHz) and S-band (2050 MHz) used on the spacecraft, respectively.
Based on the trapezoidal periodic signal harmonic analysis method, the two corner
frequencies are
F1 =
1
$\pi$
	
1
 
872 \times 103
2

 = 555.13(kHz)
F2 =
1
$\pi$

200 \times 10−12 = 1.59(GHz)
(6.4.1)
According to the slope variation, the amplitude is about 65.2 dB \muV at 1350 MHz;
and about 60.1 dB \muV at 1.59 GHz.
It involves a capacitive load, where the capacitance value is 6 pF, l is 35 mm, h is
0.5 mm, let the distance D be 1 m, then
E

dB \muV

m

= V (dB \muV) + 2\pi f C(dBS) + 20 \times log(0.013 \times l \times 2h) + 40 log( fMHz)
=

37.7
@1350 MHz
43.5
@2050 MHz
(6.4.2)
Figure 6.41 shows the analysis results of an electric ﬁeld RE at a bandwidth of
50 MHz. The emission limits for these two bands are typically 15 and 25 dB \muV/m.
Therefore, even if the switching frequency is at the kHz level, there is still a relatively
1.32
1.33
1.34
1.35
1.36
1.37
1.38
x 10
9
0
20
40
60
E/(dBuV/m)
2.02
2.03
2.04
2.05
2.06
2.07
2.08
x 10
9
0
20
40
60
E/(dBuV/m)
Frequency/Hz
Frequency/Hz
Fig. 6.41 Electric ﬁeld radiated interference in the L and S bands


6.4 Design Cases
203
large order of electromagnetic RE in the L-band and S-band, so it is required to make
an effective EMC design.
Taking the computer of the attitude control subsystem as an example, the EMC test
was conducted after the qualiﬁcation test unit was completed, and it was found that
the RE102 item exceeded the speciﬁcations. According to the actual measurement
and analysis, it was determined that the problem of exceeding the standard in the
equipment RE102 test was related to the structure of the product and the EMC design
of the PCB. Due to the design problem of the PCB, the unintentional electric ﬁeld
radiation intensity was too large, and the chassis failed to shield the unintentional
electric ﬁeld radiation of the PCB, resulting in the equipment RE102 exceeding the
standard in the test.
Analysis of the test results shows that the out-of-tolerance frequency component
is the higher harmonic of the 8 MHz frequency source. By detecting and positioning
using a near-ﬁeld probe, it is found that the positions of the equipment RE102 radi-
ated emission is concentrated at 10 external connectors on the IO1 and IO2 boards.
Therefore, the EMC design of the PCB was improved by the following measures:
(1) Change the arrangement of main high-speed operating devices, such as ASIC
chips and crystal oscillators, centralize them to replace the original dispersed
arrangement, and move their positions on the PCB from originally near the
external connectors to away from these connectors;
(2) Add one ground layer each to the top second and bottom second layers to
suppress PCB radiation;
(3) Optimize the conﬁguration of the decoupling capacitors.
The speciﬁc changes are shown in Table 6.8.
Table 6.8 PCB design improvements
No. Item
Improvement measures
1
PCB layers
(1) Add one ground PCB layer each at the top second and bottom
second layers
(2) Optimize the division of power layers, change one power layer
to a ground layer, so that there are a total of 5 ground layers and
1 power layer
2
Chip layout
Concentrate the main high-speed operating devices, crystal
oscillators, etc. and move them away from the external connectors
3
Wiring design
The crystal oscillator directly outputs to the ASIC chip, and the
signals travel inside the PCB
4
Chip output
(1) The output ends of the crystal oscillator are connected in series
with the resistor outputs
(2) The ASIC chip output ﬂoating pin is replaced by a resistor to
the ground
5
Decoupling capacitor Change the decoupling capacitors from originally multiple sets of
single-value capacitors to multiple sets of ﬁve-value capacitors


204
6
EMC Design and Implementation of General Electronic Equipment
Besides, the shielded casing of the equipment was designed to a lip type, so as
to reduce the bonding resistance between the casing structures and improve the SE
of the casing. The equipment was EMC re-tested after these changes. Thereafter,
the original RE102 out-of-tolerance items meet the technical requirements of EMC,
which proved that the designs and improvements were effective.
6.4.1
PCB Design
6.4.1.1
PCB Layer Design
The number of signal layers is basically determined by the complexity of the
circuit, the density of the wiring and the operating frequency of the individual
board, the number of signals with speciﬁc wiring requirements, and the performance
requirements of the individual board.
The number of ground layers is determined by the requirements of the power and
signal layers.
During the design, the following should be considered:
(1) The critical signals of adjacent layers cannot cross the segmentation areas;
(2) The critical power layer should have a corresponding adjacent ground layer;
(3) Critical signal layers, such as high frequency, high-speed, clock, and other key
signals, must have an adjacent ground layer.
6.4.1.2
Classiﬁcation and Layout of Circuit Modules
1. Classiﬁcation of circuit modules
Circuit modules can be divided into the following types by their functions: clock
circuit, drive circuit, A/D conversion circuit, D/A conversion circuit, I/O circuit,
switching power supply, ampliﬁcation circuit, and frequency conversion circuit, etc.
A complete design contains module circuits of various functions. When designing
a PCB, we can classify the circuits according to the direction of the signal, thereby
to ensure the rationality of the layout, and achieve the objectives of shortening the
overall wiring path, non-crossing between different functional modules and reducing
the possible mutual interference between the modules.
Circuit modules can also be divided into HF, MF, and LF modules, according to
the operating frequency and rate of the signal, and modules of different frequencies
should be isolated from each other and not interlaced.


6.4 Design Cases
205
In addition, circuits can be divided into digital and analog by the signal type.
2. Layout
The layout of the circuits should be considered comprehensively. First, according
to the ﬂow relationship of the signals, the key high frequency or high-speed signal
traces should be as short as possible. Second, the layout should be neat and tidy.
Some basic points are as follows:
(1) Division of areas. Circuits with different functions should be arranged in
different areas, such as digital circuits, analog circuits, interface circuits, clock
circuits, power circuits; in the division of areas, the high voltage high current
signals should be completely separated from the weak signal of low voltage and
low current, and the HF signals are separated from the LF signals;
(2) The main components should be arranged according to the main signal ﬂow
direction in the circuit, and follow the principle of “ﬁrst big, small, difﬁcult
before easy” in the layout;
(3) For circuits with same structure, use “symmetric” standard layout as much as
possible;
(4) For circuits with large radiation, such as clock signal circuits, spatial isolation
should be made to keep them away from sensitive circuits and cable connectors;
(5) Digitalcircuitsandanalogcircuitsshouldbeplacedseparately.Inordertoreduce
the interference of digital circuits to analog circuits and make them compatible,
it is necessary to deﬁne different areas in the PCB layout. Firstly, it is preferred
to isolate them from space and reduce mutual coupling; secondly, digital and
analog conversion circuits, such as A/D or D/A conversion circuits, are placed
at the junction of digital and analog circuits in the direction of signal ﬂow, so
that the signal leads are the shortest; ﬁnally, the digital equipment and the trace
should be placed above the digital ground, while the analog equipment and the
trace are placed above the analog ground, it is prohibited to place them across
the segmentation area.
(6) LF digital I/O circuits and analog I/O circuits should be placed close to the
connector; devices such as clock circuits, high-speed circuits, and memories
should be arranged on the edge of the board; medium- and low-speed logic
devices are usually placed at the center position of the board;
(7) For circuits which have higher power and the driving part of control has strong
radiations, a separate cavity should be designed to keep it away from the cables,
connectors, the local opening of the box or the wiring slot;
(8) Installationofﬁltercomponentsgenerallyfollowstheprincipleofproximity,and
install them at the exit of the interference source. For example, the decoupling
capacitor should be as close as possible to the decisive power supply pin, the
power supply ﬁlter should be as close as possible to the input or the output of
the power supply, the ﬁlter of the local functional module should be close to the
input or output port of the module, and the ﬁlter of the external interface should
be close to the connector;


206
6
EMC Design and Implementation of General Electronic Equipment
(9) Coils are the most effective equipment for receiving and transmitting magnetic
ﬁelds. It should be kept away from the switching power supply, clock circuit,
high-power signal, and other sources in layout design. There should be no sensi-
tive signal lines such as high-speed lines and control lines passing under the
coils. If inevitable, considerations should be given to the direction of the coil to
make sure that the ﬁeld strength direction is parallel to the coil plane, so that
the magnetic lines passing through the coil are the least.
6.4.1.3
Application of PCB Grounding Design
Grounding design can eliminate coupling between the circuits and reduce the poten-
tial difference on the ground lines. Grounding is an important measure to suppress
EMI and improve the EMC of equipment. Proper grounding not only improves
the capability of EMI suppression, but also reduce the external EM radiation. The
following items should be noted in the ground design:
1. The ground reference plane should
(1) Provide a low impedance path and a stable reference voltage.
(2) Control the trace impedance.
(3) Reduce the loop area and EMI.
(4) Control the crosstalk by placing the trace close to the reference plane.
(5) Provide a certain degree of shielding by using the image effect of the refer-
ence plane. For example, when the distance between a cable and the refer-
ence plane is 1 mm, the shielding effect is \geq30 dB at a frequency of 100 kHz.
The closer the distance, the better the shielding effect will be.
2. Avoid slotting on the ground plane
In the PCB design, the space for the wiring layer is very limited, sometimes a long
strip may be divided on the ground plane to arrange the trace. If slotting on the ground
plane, the signal current will bypass the top of the ground slot and form a large loop,
which will increase the inductance of the signal path and slow the rise time of the
received signal, thus resulting in mutual inductance crosstalk.
3. The distance between the grounding points
The distance between the grounding points should be less than 1/20 of the highest
excitation frequency or harmonic wavelength, i.e. $\lambda$/20. For example, a $\lambda$/20 of a
100 MHz signal is 15 cm. If the distance between two ground points is greater than
15 cm, an RF radiation loop will be formed, which may become an energy source,
and cause EMI to exceed the speciﬁed limit.
If, in the design, the distance of the grounding points cannot be ensured to be less
than $\lambda$/20, using an additional metal foil connection or the like structure can also
eliminate the RF radiation generated by such a loop.


6.4 Design Cases
207
4. Grounding network
The impedance of the ground wire is composed of wire resistance and inductance.
When the frequency is high, the dominant inductance is the inducted reactance.
Increasing the wire width can reduce the impedance, but since the wire width and
inductance are logarithmically related, the wire width variation has little effect on
the inductance.
Laying a ground grid is equivalent to connecting multiple wires in parallel, which
can effectively reduce the ground inductance. In this case, be careful of the spacing of
the main wires. If the wires are far apart (greater than 10 mm), the mutual inductance
can be neglected.
5. Minimizing the loop area
The rule for minimizing the loop area is to minimize the area of the loop formed by
the signal line and its return. The smaller the loop area, the smaller the EMI radiated
to the outside.
6.4.1.4
PCB Layout Design
1. Minimizing the signal loop area
According to the rule that the smaller the loop area, the smaller the external radiation
and interference, when dividing the ground plane, the ground plane and important
signal trace should be considered to prevent problems caused by ground plane slot-
ting; in the double-layer board design, while sufﬁcient space is reserved for the power
supply, the double-sided spare portion should be ﬁlled with ground layers, and the
two-sided ground signals should be effectively connected by ground vias. The critical
signals should be isolated by ground wires as much as possible; and for HF signals,
considering the ground plane loop problem, it is recommended to use multilayer
boards, as shown in Fig. 6.42.
Fig. 6.42 Minimizing signal
loop area
Correct 
Incorrect 


208
6
EMC Design and Implementation of General Electronic Equipment
2. Shielding of the trace
According to the rule of the minimal signal loop, in order to minimize the loop area
of the signal, the important signal traces should be shielded, such as clock signals
and synchronization signals; for some important, higher frequency signals, coaxial
cable shielding design should be adopted. All laid wires should be isolated all-around
using ground lines, and necessary consideration should be given to how to effectively
combine the shielding ground with the actual ground plane, as shown in Fig. 6.43.
Note: When using shielding rules, make sure that the shielding layer is well-
grounded.
3. Control of trace orientation
The basic design requirement for the trace orientation is that the adjacent layers
should be an orthogonal structure, as shown in Fig. 6.44. But in practical engineering,
it is difﬁcult to achieve, so just do as much as possible in the design. Do not route
different signal lines in the same direction so as to reduce crosstalk; if the signal
frequency is high, it may be considered to use ground planes to isolate the wiring
layers or use ground lines to isolate the signal lines.
Fig. 6.43 Shielding of trace
Correct 
Incorrect 
Fig. 6.44 Control of trace
orientation
Correct 
Incorrect 


6.4 Design Cases
209
Fig. 6.45 Open-loop
inspection of the trace
Correct 
Incorrect    
For some complex equipment, if it is difﬁcult to implement the orthogonal prin-
ciple, pay attention to the outgoing direction of various signal lines, the same type
of signal lines should be put together.
4. Open-loop inspection of the trace
This is mainly to avoid the “antenna effect”, as shown in Fig. 6.45. At the end of the
antenna, the smaller the area, the more effective the emission will be. For HF signals,
avoid such a design.
5. Capacitor leads
The ground and power lines of the ﬁlter capacitor should be as thick and short as
possible.
When the printed conductor that suppresses the differential mode noise capacitor
is thin, the lead of the capacitor should be the shortest, as shown in Fig. 6.46.
6. Trace resonance
This is mainly for the design of HF signals, which requires that the length of the
wiring not to be an integer multiple of 1/4 of its wavelength, so as to avoid resonance
and antenna effects. If the EMI control requirements are rather strict, this rule should
be taken seriously. As shown in Fig. 6.47.
Fig. 6.46 Capacitor lead is
the shortest
Correct 
Incorrect 
Cx capacitor
Cx capacitor
Fig. 6.47 Resonance of the
trace
Incorrect 
Correct 


210
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.48 Trace length
control
Correct 
Incorrect 
7. Trace length control
The wiring length should be as short as possible, especially for important signal lines,
such as HF mixers, the local oscillator must be placed near the mixer, as shown in
Fig. 6.48.
8. Chamfering rules
When a wire turns at a right angle, the capacitance per unit length will increase, the
inductance will decrease, and the impedance at the sharp corner will become larger,
which will result in radiation and poor process performance. Therefore, in the PCB
design, avoid using right angles or sharp corner wiring when changing the direction
of the wiring, use a 45^\circ angle or rounded wiring instead, as shown in Fig. 6.49.
If the wires must be routed at right angles, especially in circuits with higher
frequencies, when the wire impedance is required, a chamfer design can be used.
Generally, the outside of the chamfer can be cut into a 45^\circ bevel angle, as shown in
Fig. 6.50a; if the microstrip lines on both sides of the corner are not equal in width,
use dimensions shown in Fig. 6.50b in the design. If the operating frequency is above
Ka or higher frequency band, it is required to conduct speciﬁc simulation analysis
of the size of the chamfer angle in combination with the circuit.
9. Change of Wire width
Do not change the width of the trace on the PCB suddenly and dramatically. Change
the width of the trace in a gradual way, if necessary, as shown in Fig. 6.51.
(a) Incorrect 
(b) Correct 
(c) Correct
Fig. 6.49 Chamfering rule


6.4 Design Cases
211
 (a) Matching right-angle corner size          (b) Matching right-angle corner size of 
of 50Ω microstrip line                       unequal width microstrip line
Fig. 6.50 The optimal size for the chamfer design
Fig. 6.51 Change in trace
width
Correct 
Incorrect 
Fig. 6.52 Isolated copper
layer control
Correct 
Incorrect 
10. Isolated copper layer control
The isolated copper layer may cause unpredictable problems, therefore, connecting
the isolated copper layer to other signal lines helps to improve the signal quality.
Usually, the isolated copper layer is grounded. If it is not easy to ground due to
circuit limitation, it can be removed, as shown in Fig. 6.52. In practical design, some
small thin copper chips are added to the vacant parts of some PCBs, mainly for the
convenience of PCB processing and also for preventing warpage of PCB.
11. 3W rules
The 3W rule means that in order to avoid crosstalk between two printed lines, the
line spacing (distance between centers of the two lines) should be kept at least three
times the line width, where W is the width of the line, as shown in Fig. 6.53.
When the frequency is high, if other lines are too close to the line, the RF signal
energy will be transmitted to the adjacent lines. In order to effectively solve such
problems, it is conﬁrmed by experiments that if a grounded isolation line is added
between adjacent signals, the impact between the signals will be greatly reduced,
that is, if the distance between the two signal lines is kept greater than 3 times
the interference signal width, it will effectively improve the crosstalk between the
adjacent signal lines. This is the so-called 3W rule.


212
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.53 3W rule
W
Wiring 
Power plane
Ground plane
RF radiation 
Wiring 
Power plane
Ground plane 
Fig. 6.54 RF radiation from the power plane
In addition to the line spacing, crosstalk is also related to the height h of the wiring
layer to the reference plane. The smaller the h, the better.
The 3 W rule keeps 70% of the electric ﬁelds from interfering with each other. To
achieve 98% of the electric ﬁeld without mutual interference, a 10W spacing can be
used.
12. 20H rule
In RF circuits, the coupling between the power plane and the ground plane may enter
free space, as shown in Fig. 6.54 (left). In higher frequency PCB designs, in order to
avoid the power plane layer radiating energy to free space, all power planes must be
smaller than the ground plane and indented 20H inward (H is the distance from the
power plane to the ground plane).
If the 20H rule is followed, the self-resonant frequency of the PCB’s power plane
and ground plane capacitance is increased by about 2–3 times. The 20H rule will
reduce the edge effect by 70%. If a 98% effect is to be achieved, a 100H rule must
be followed.
If there is a partition on the PCB, the partition can be designed according to the
20H rule. For example, the partition between the digital and analog areas can be
designed as shown in Fig. 6.55.
13. PCB wiring principles
The following basic principles should be followed in PCB wiring:
(1) The critical signal wires cannot be routed across the partition (including the
reference plane gap caused by vias and pads);
(2) No unrelated signal lines should go under sensitive equipment or circuits such
as ﬁlters and modulators. Since power lines and RF signal input and output lines
are also sensitive devices, try to avoid crosstalk between these signals.


6.4 Design Cases
213
Digital ground 
Digital power
Slot 
Analog ground
Analog power
Fig. 6.55 Digital and analog area boundary design rules
(3) The input and output lines of RF equipment (including ampliﬁers, ﬁlters, etc.)
should be arranged in a “dash-line” or “L-shaped” layout as much as possible
to keep the input and output signals apart, and neither be parallel nor crossed
with each other;
(4) When changing the layer of signal lines (especially critical signal lines), the
ground vias should be designed near the layered via;
(5) Strong radiated signals should be kept away from LF harnesses, connectors,
and sensitive equipment; sensitive signal lines should be kept away from strong
radiation sources and connectors in the housing;
(6) Increase the wiring width as much as possible while ensuring impedance
matching;
(7) The wiring length should be as short as possible. When the length of a wire is
greater than 1/20 of the corresponding wavelength of the noise frequency, it will
cause an antenna effect, and the noise will be radiated out through the wire.
6.4.2
Shielding Design
6.4.2.1
Shielding Design of Gaps
When two parts are combined, the gap between the joint surfaces is the main factor
affecting the SE of the structural part. According to the shielding principle of the gap
and in conjunction with the actual engineering experiences, the following methods
are usually adopted to improve the SE of the structural parts.
1. Increasing the depth of the gap
The depth of a gap at the joint of movable surfaces in the box depends on the
thickness of the shield and the bonding width (i.e., the width of overlap) of the two
joint surfaces. If a boss is added at the joint, as shown in Fig. 6.56, it will not only
increase the contact surface to facilitate fastening, but also increase the depth of the
gap t.
2. Improving the processing accuracy of the contact surfaces
The accuracy of the joint surfaces (roughness, ﬂatness, etc.) also has an effect on
the SE of the gap. However, due to factors such as the process technology and the


214
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.56 Method of increasing the depth of the gap
equipment machining accuracy, which are very difﬁcult to make changes, generally,
there is no speciﬁed requirement for surface accuracy of the parts in the actual design.
3. Installing conductive pads
Installing conductive pads between the bonding surfaces can reduce the gap and
improve the SE. The conductive pad is a highly elastic and deformable conductive
material sandwiched between the two end surfaces, which can ﬁll the gap after
compressed and deformed, so that the two mating surfaces have a good electrical
contact. Therefore, the conductive pads should have high electrical conductivity
and mechanical elasticity, corrosion resistance, and no chemical corrosion with the
contacting material. In addition, it should also be able to withstand high- and low-
temperature variations, and not age within the operating temperature range.
4. Applying conductive coating to the joints
Commonly used conductive coatings are conductive adhesives, conductive ﬁllers,
and conductive greases. Whatever type of conductive material to be used, the joint
surfaces must be cleaned, and any oil stains, lacquer layers, and oxide layers that
may affect conductivity must be removed before applying.
The following cautions should be observed when applying conductive adhesives
for coatings:
(1) The adhesive is to be applied on single equipment after commissioning and
before painting;
(2) The adhesive is to be applied at the gap between the waveguides in the cabin
after the waveguide assembly and debugging are completed;
(3) Conductive adhesive should be applied to materials with good conductivity,
never apply them to materials that are nonconductive protected, including
spraying with “three protective” paint, temperature-controlling paint, etc.;
protection measure can be taken only after the conductive adhesive is applied;
(4) After applying conductive adhesive, follow the requirements of the process
documents, and test the conductive adhesive after curing for 24 h.
5. Gap installation pressure
The gap radiation at the joint surfaces is closely related to the installation pressure.
When the pressure between the joint surfaces of the two parts reaches a certain
strength, the two parts will be so tightly combined that can be approximately regarded


6.4 Design Cases
215
Distance 
Pressure 
Fig. 6.57 Diagram of gap installation pressure
as a solid metal connection. However, in general, the two parts are ﬁxed by screws,
which can achieve an ideal gap pressure in its vicinity under the predetermined
installation torque, but as the distance away from the screw increases, the pressure
will continuously decrease along the length of the gap till the lowest value in the
middle of the two fastening screws is reached, as shown in Fig. 6.57. The area that
may cause EM leakage is the gap between the two broken lines, and the maximum
radiation point is in the middle of the two fastening screws.
For equipment with SE requirements, it is recommended to use titanium screws
for ﬂange connection of passive equipment, and grade 8.8 steel screws for cover
connection. Additional measures to improve the gap pressure include: reducing the
spacing between the screws to reduce the length of the pressure drop between the
screws, thereby reducing EM leakage; increasing the thickness and diameter of the
screw washers and the thickness of the cover plate at the gap for better pressure
transmission.
6. Adjusting the fastening screw spacing
Fastening the joint surfaces with screws is a common method for fastening structural
members. The distance between the two fastening screws d determines the maximum
gap length l, and l = d. However, the gap length l is usually is smaller than d. Based on
the multiple factors such as product structural design, the gap installation pressure,
the test data of the earlier products and others, the gap length l at the ﬂange connection
of the passive equipment is about d/5 to d/4, and the gap length l at the cover plate
joint is about d/4 to d/3.
In principle, the screw spacing should be much smaller than the wavelength of
the EM wave, and generally, the limit is less than $\lambda$/20.


216
6
EMC Design and Implementation of General Electronic Equipment
6.4.2.2
Shielding Design of Holes
1. Shielding of the vents
In the spacecraft equipment, one or more air vents should be designed on the chassis
to ensure that the internal air pressure of the spacecraft can quickly balance with
the external air pressure when entering the vacuum environment, so as to avoid
low-pressure electro-discharge.
In LF equipment, the vents have little effect on the SE of the product.
In HF equipment, the design of the vents must meet the following requirements:
(1) A/V > 1.7 \times 10−6/mm, where A is the total area of the vent and V is the volume
of the equipment;
(2) t/D > 6.25, where t is the vent depth and D is the vent diameter;
(3) The diameter of the vent should not exceed Φ 2 mm.
According to the above requirements, the SE of the chassis is greater than 100
dB, so the air vents does not need to be specially shielded.
2. Shielding of line-passing holes in the chassis
Since the SE of the perforated metal plate depends on the maximum size of the
opening rather than the area of the hole. Provided that the hole meets the require-
ments for use, it is recommended that the openings preferably be circular holes, or
hexagonal holes similar to circular holes, then square holes, but never waist holes
or even elongated holes. A hole with a max. size of 4–6 mm is recommended. The
speciﬁc opening size is related to the actual application and SE requirements. Gener-
ally, the hole should be as small as possible to ensure sufﬁcient SE. Since the SE can
be improved by increasing the thickness of the shielding layer, if the shielding perfor-
mance does not meet the design requirements, it is considered to locally increase the
thickness of the shielding layer at the opening.
At lower frequencies, the hole has less effect on the shielding performance of the
cavity, but in practical applications, the passing cable can signiﬁcantly degrade the
SE of the cavity. If it is limited by external conditions such as product assembly,
other design methods can also be used, such as reducing the size of the hole.
6.4.2.3
Cable Shielding Design
The cable design is critical to the SE of the structural components. The shielding
measures of the cable should be carefully considered during technical coordination
and detailed design. Refer to Chap. 2 for implementation.


6.4 Design Cases
217
6.4.2.4
Shielding Design of Connectors
1. Types of connectors
There are two types of commonly used cable connectors: LF and RF connectors.
In the ﬁeld of spacecraft technology, LF connectors are usually used to transmit LF
or baseband signals, with frequencies range from DC to 10 MHz. Moreover, RF
connectors are used for RF signals.
In addition to these common connectors, there are also some special connectors,
such as communication connectors, ﬁber-optical connectors.
(1) LF connectors
LF connectors are divided into metal and nonmetal by the material. Metal connectors
have good shielding effects, which can provide a good 360^\circ loop grounding for the
cable shielding layer, and minimize the termination impedance of the connector and
the shielding layer.
Metal connectors are especially suitable for space electronic equipment; selecting
adjacent pins intheconnector for signal transmissionlinepairs canreduceline-to-line
coupling and achieve impedance balance between the pair; different types of signals
should use different connectors; select the smaller size connectors if the number of
pins is sufﬁcient for use.
(2) RF connectors
Common RF connectors include SMA, SMB, TNC, N, K, and other types. Under the
normal condition of processing and installation, all types of connectors can satisfy
the design shielding speciﬁcations. For example, the design shielding index of the
SMA connector is about 80 dB, so please refer to the design shielding index to select
the proper connector types.
(3) Other connectors
Other connectors refer to communication type connector 1553B and special-purpose
connectors, such as ﬁber-optical connectors. The shielding index of some special
connectors is available in the product manuals, and that of the ﬁber-optical connector
is required to be calculated according to the waveguide transmission theory.
2. Connector shielding design
The shielding design of the connectors usually refers to the shielding design of the
connectors in combined use with the equipment casing and the cable, rather than the
connector itself alone.
A connector usually consists of a head and a base. The head is connected with the
cable, and the base is mounted on the chassis, as shown in Fig. 6.58.
Among the factors affecting cable SE, the connector openings, installation, and
the coupling of the connector core are critical.


218
6
EMC Design and Implementation of General Electronic Equipment
Chassis 
The gap between the 
connector and the chassis
Connector 
Fig. 6.58 RF connector shielding design method
(1) Opening: refers to the holes reserved for installation of the connector on
the casing, the smaller size the better, providing that it meets the connector
installation requirements.
(2) Installation: generally, the hardness of the material used in the connector is
greater than that of the material of the chassis. Using more ﬁxing screws for the
connector can reduce the length of the gap and increase the pressure between the
connector and the chassis, thus reducing the contact impedance between the two
parts. If necessary, use a connector with more ﬁxing screws. Commonly used
chassis materials are aluminum alloy and magnesium alloy. According to the
installation strength, the tightening torque of the ﬁxing screws is recommended.
If necessary, the SE can be enhanced by the following measures.
One is to install a conductive gasket under the connector so that there is no
gap left between the contacting surfaces of the connector and the chassis. The RF
signal needs good grounding. In this measure, the conductive performance of the
conductive gasket should be considered over its lifetime. Besides, the installation of
the conductive gasket will reduce the installation strength between the connector and
the chassis, so mechanical analysis is required to make sure the installation strength
meets the requirements. In addition, the shielding effect can be achieved by applying
a conductive coating. In the design, a gap for conductive paint should be reserved,
which will not only be convenient for operation, but also increase the depth of the
gap and enhance the SE.
Some LF connectors have rubber pads on the mounting ﬂange, see Fig. 6.59. The
rubber pads can be replaced with a conductive rubber gasket of the same size, to
reduce the contact impedance between the connector and the chassis and improve
the SE of the chassis.


6.4 Design Cases
219
Fig. 6.59 Connectors with
rubber pads
Rubber pad
(3) Coupling: If there is a large radiating circuit inside the chassis, the signal will
be coupled and radiated through the core wire of the connector and cable;
similarly, if there is a circuit with poor anti-interference capability inside the
chassis, external interference will be coupled through the cables and the core
of the connector into the chassis and affect the circuit performance. Therefore,
if there is an interference source or a sensitive circuit inside the chassis, it is
necessary to design shielding to the installation cavity of the connector. The
most easy way to design a special shielding cavity for the connector is to isolate
the signals and block the coupling paths of the interference signals.
6.4.3
Filter Design
In equipment design, besides proper shielding and grounding design, an effective
ﬁltering design to ﬁlter out unwanted emissions is also required. In order to meet the
standards or speciﬁcations, EMI ﬁlters are usually used. Since EMI ﬁlter is a low-
pass ﬁlter, they cannot completely eliminate the interference signals from conducted
emissions, but only reduce the transmitted interference signals to a certain extent and
enable the CE or susceptibility to meet the speciﬁcations.


220
6
EMC Design and Implementation of General Electronic Equipment
6.4.3.1
Power Filters
1. Types of power ﬁlters
The power ﬁlter typically uses a reﬂective ﬁlter that reﬂects the energy of interfering
frequency back to the noise source, allowing the DC current energy to enter the
equipment’s internal circuitry through the ﬁlter. The power ﬁlter is a low-pass ﬁlter,
the main forms include L, , and T. Among them, the -type has low suppression
of transient interference; the T-type has the highest suppression of transient signals,
but with large volume and weight; while the L-type gives consideration to both.
The main technical speciﬁcations of the ﬁlters are listed in Table 6.9.
In the design of a reﬂective power ﬁlter, you must know the power end impedance
and the load impedance. The more mismatched between the ﬁlter impedance and
the impedance on both sides of the circuit, the better the suppression performance.
The power end impedance typically uses the value of the power bus impedance on
the LISN impedance simulation system platform in the EMC test equipment. The
load impedance is dependent on the power switch circuit design. The impedance
characteristics of different types of interference and the choice of reﬂective ﬁlters
are shown in Table 6.10 and Table 6.11, respectively.
Table 6.9 Main technical speciﬁcations of the ﬁlters
Main parameters
Description
Design principles
Insertion loss
It is the most important indicator
of the ﬁlter, which reﬂects the
degree of suppression of the
noise signal by the ﬁlter
The insertion loss satisﬁes the
circuit suppression requirement.
Higher order ﬁlters are easy to
self-exciting
Frequency response
The ﬁlter has suppression
capability only within a certain
frequency range
Analyze the noise frequency
that may exist in the circuit, and
consider the insertion loss and
frequency to achieve the
suppression of HF noise signals
Impedance
characteristics/frequency
response
Due to the nonideal nature of the
components, the input and
output impedance of the ﬁlter
varies with frequency
For reﬂective ﬁlters, impedance
variations can also cause
suppression performance to
change
Rated current and voltage
Mainly depends on the
capability of withstanding
voltage and current of the
components
Consider the worst conditions
that may occur on the power
bus, especially the effects of
transient current and voltage
pulses, and reserve a certain
design margin


6.4 Design Cases
221
Table 6.10 Impedance characteristics of different types of interference
Type of interference
Power end impedance (LISN)
Switch circuit impedance
CM interference
Low impedance
High impedance
DM interference
High impedance
Low impedance
Table 6.11 Options for reﬂective ﬁlters
Filter structure
Source impedance
Load impedance
T-type ﬁlter
Very small
Small
-type ﬁlter
Very large
Large
L-type ﬁlter, inductance located at the load end
Very small
Large
L-type ﬁlter, inductance located at the power end
Very large
Small
2. Types and options of power ﬁlter devices
The types of power ﬁlter devices and the corresponding parameter characteristics
and applicable environment are shown in Table 6.12.
3. Power ﬁlter installation and use
Figure 6.60 shows a common power EMI ﬁlter. The ﬁlter should be well-grounded
during use and preferably mounted directly on the chassis. The ﬁlter should be placed
near the cable port, and the input line should be as short as possible and use twisted
pairs. The input and output cables should be isolated. The input wires of the ﬁlter
should be isolated from all other cables in the chassis. The installation and grounding
of the power ﬁlter are shown in Figs. 6.61 and 6.62.
6.4.3.2
Signal Filter Design
The signal ﬁlter is also a low-pass ﬁlter mainly used for ﬁltering out HF interference
on various signal lines. Since the signal source on the internal board of the equipment
can act as the receiving and transmitting antenna, it is emitting EMI to the outside
while at the same time receiving external EMI. Therefore, designing a signal ﬁlter
on the signal line is an effective way to solve the HF EMI problem.
According to the installation and shape, the signal line ﬁlters can be divided into
three types: PCB mounting ﬁlters, feed-through ﬁlters, and ﬁlter connectors.


222
6
EMC Design and Implementation of General Electronic Equipment
Table 6.12 Filter types and corresponding parameter characteristics and applicable environment
No.
Type of ﬁlter
Parameter characteristics
Applicable environment
1
Capacitor
A surface-mounted capacitor
or a three-terminal capacitor is
recommended in the power
circuit, which has a high
self-resonant frequency and is
suitable for HF interference
environments
Filtering of high frequency
CM interference signals
2
Inductance
Due to the inﬂuence of the
distributed inductance across
the inductor, the suppression
performance for high
frequency signals is degraded
Used for suppression of DM
signals at low and medium
frequencies
3
L-type
Though the source impedance
and the load impedance are
seriously mismatched, the
suppression effect is good
Can be used as a switching
power supply ﬁlter
4
T-type
It can effectively suppress
transient interference, but
requires two inductors, which
results in large ﬁlter volume
and power consumption
Suitable for equipment with
transient interference signals
5
-type
It has good suppression effect
on LF and easy to manufacture
Suitable for use as a ﬁlter, but
has poor suppression to
transient signals
6
Feed-through capacitor
The effective ﬁltering
frequency can be up to
hundreds of MHz
It can be used to suppress the
HF circuit signals from being
fed back to the power supply
circuit through the power line,
causing secondary emission
7
Stabilizer
An active device used for
secondary power supply
regulation, and also ﬁltering of
LF ripples
Applicable for products with
long secondary power leads or
followed by a highly sensitive
circuit
8
CM choke
Filtering the CM signals
Applicable for equipment with
a CM interference signal on
the power line
The PCB mounting ﬁlter is suitable for mounting on a PCB. It is low-cost and
convenient for installation, but the ﬁltering effect for high frequency is poor. The feed-
through ﬁlter is applicable to the shielded housing and has good HF ﬁltering charac-
teristics, suitable for a single wire to pass through the shield. The ﬁlter connector is
suitable for mounting on a shielded chassis and has good HF ﬁltering characteristics,
suitable for multiple wires to pass through the shield.
The utility of signal ﬁlters can be divided into the following categories:
(1) Feed-through the shield housing


6.4 Design Cases
223
Fig. 6.60 Common power EMI ﬁlter
Chassis
Capacitor
coupling
Field coupling
Radiation 
Power
Conducted
emission
Filter
Secondary
power
Poor
grounding
Coupling
of
the
input and output
cables of the filter
Fig. 6.61 Poor power supply ﬁlter installation and grounding
Chassis
Field 
coupling
Secondary 
power
Power
Filter bonding 
casing
Cable installation 
near the chassis
Fig. 6.62 Good power ﬁlter installation and grounding


224
6
EMC Design and Implementation of General Electronic Equipment
Any conductor is not allowed to pass through the shielding casing. Even if the SE
is higher, once a wire passes through the shield, its SE will be greatly degraded,
because the wire acts as an antenna for receiving emissions and susceptibility. When
a conductor is to pass through the shield, a ﬁlter connector or a feed-through ﬁlter
must be used to ﬁlter the transmitted interference signal received by the conductor
to the grounded shield to avoid interference to pass through the shield.
(2) Internal isolation of the equipment
The smaller the volume of the equipment, the higher the integration degree of the
devices, and the more serious the interference problem between the circuits. It is
especially so for the interference between the digital and the analog circuits, and
that between the strong signal and the weak signal circuits, which has become an
important impact factor in the indicators of electronic equipment. When there are
interconnecting lines between different circuits, ﬁltering is required to isolate the
mutualinterference.Inthiscase,ﬁlterconnectorsandfeed-throughﬁltersarerequired
on the interconnecting lines.
6.4.4
Implementation of Bonding and Grounding
6.4.4.1
Implementation of Bonding
Metal parts and electronic and electrical devices of spacecraft equipment should be
bonded to the grounding system of the satellite structure. The main requirements are
as follows:
(1) The casing material of the instrument and equipment should be electrically
conductive, and the material compatibility between the casing and the struc-
ture or the support should be veriﬁed. If a grounding circuit is required, it is
preferred to use the bonding strap grounding method to meet the requirements.
The common design of the bonding strap is shown in Fig. 6.63.
Fig. 6.63 Design of
common bonding straps


6.4 Design Cases
225
Fig. 6.64 Typical design of
a grounding pile
Chassis 
Grounding pile boss
Screw rod 
(2) A piece of equipment can be electrically bonded to the satellite structure through
mounting surface or grounding pile, and ensure that the DC resistance between
the metals does not exceed 10 m.
(3) The material of an equipment chassis that is electrically bonded by contacting
surfaces shall be electrically conductive and compatible with the structural
material of the mounting surface.
(4) Equipment that is electrically bonded by grounding piles should be connected
to the satellite structure with bonding wires (jumpers/straps).
(5) If a piece of equipment is installed on a composite material or a material with
low conductivity, its structure should be connected to the conductive structure of
the satellite by a grounding wire. Moreover, the DC resistance of the grounding
strap should be less than 10 m.
(6) The grounding pile should be connected to the equipment chassis with relevant
anti-loosen measures to ensure it will not loosen during the ﬁnal assembly.
The typical design of a grounding pile is shown in Fig. 6.64. All grounding
piles should be easy to access and should leave sufﬁcient operating space (it is
recommended that the distance from the grounding pile axis to the mounting
surface is 10–50 mm to facilitate the ﬁnal assembly operation).
Requirements: the screw rod should be securely ﬁxed on the structure, and a
standard nut and ﬂat pad are provided. The screw rod, nut, and ﬂat pad should be
gold plated.
6.4.4.2
Bonding Resistance
The HF impedance of the bonding resistor has special characteristics in the test. In
general product inspection, only the DC bonding resistance is required.
The bonding impedance requirements between structures are shown in Table 6.13.


226
6
EMC Design and Implementation of General Electronic Equipment
Table 6.13 Bonding requirements between structures
Bonding
Electrical performance
Between metal mounting surfaces
\leq10 m, minimum contact area >1 cm2
Between metal parts and carbon ﬁber parts
<100 
Between carbon ﬁber parts
<100 
Between carbon ﬁber skin and structural ground
<100 
Between rigid skin and structural ground
<100 
Between bracket, connector bracket, equipment
bracket and structural ground
<100 
6.4.5
Cable Design
6.4.5.1
Impedance Matching of Transmission Lines
When the transmitting and receiving conductors on the signal current loop are too
close, a strong coupling will occur, and their mutual capacitance and inductance will
combine to form a characteristic impedance Z0, where Z0 = \sqrtL/C. Whether be the
cable or the connector, including the wires on the PCB, its characteristic impedance
Z0 can always be calculated. Under the condition that the source and load impedances
are “matched” with the transmission line Z0, the transmission line forms a cable with
controllable impedance and no resonance, thus preventing the cable from becoming
a resonant antenna.
The matching of the transmission lines refers to the matching at both ends of the
source and the load of the cable. In this case, the matching provides a maximum
power transfer from the source to the load, but also results in a 50% voltage loss on
each interconnection. In non-RF equipment, the interconnection of common signals
is terminated only at one end of the transmission line without causing voltage loss.
Even with the best matching method, the transmission line will still have a slight
leakage. In use, the cable will always have Z0 changes due to such defects as large
anglebending,deformation,repeatedexpansionandcontraction,damageorimproper
use of connectors, which will cause performance degradation of the transmission line.


6.4 Design Cases
227
6.4.5.2
Design of Conductor Pairs
Even if transmission lines are not used, paired conductors should be adopted. The
principle is to provide a return path for the return current as close as possible to
the transmitting channel, so that even if the signals are single-ended and all their
return conductors are bonded to a common reference potential, it can still maintain
the normal operation.
The performance of a twisted pair is much better than a parallel pair. We can also
use three-strand, four-strand cables. The ultimate goal is to make the transmitting
and receiving paths of the signal in a fully twisted and closely contacted state. Using
a twisted pair of a balanced circuit and a CM choke, the upper limit of available
signal frequency may reach the order of tens of megahertz.
6.4.5.3
Cable Connectors
(1) Core arrangement of unshielded connectors
Conventional multiplex connectors must ensure to have one receiving pin next to
each transmitting signal pin and at least one receiving pin for every two transmitting
signals. This type of connector core arrangement facilitates balanced signals.
(2) Shielded connector
Shielded cables must form a 360^\circ shielding cover over its length, and should also
include the connector back-shells at both ends of the cable. The connector must form
a 360^\circ bonding with the back-shells.
6.5
Summary
During the EMC design of spacecraft electronic equipment, it is necessary to break-
down the EMC technical requirements by referring to Fig. 6.65, and determine the
corresponding control measures according to the EM characteristics of various ports,
such as bonding, grounding, layout, ﬁltering, and shielding, so that the EMC design
becomes an integral part of the electrical performance design of the equipment.


228
6
EMC Design and Implementation of General Electronic Equipment
Fig. 6.65 Schematic of relationships between equipment EMC requirements and EM characteris-
tics

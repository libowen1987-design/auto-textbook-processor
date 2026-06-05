# Zhang《Spacecraft EMC Technologies》第1章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 1. Introduction

Chapter 1
Introduction
With the increasing complexity of spacecraft electronic equipment and payloads,
electromagnetic compatibility (EMC) technology has become one of the key
technologies to ensure the successful implementation of space missions.
Spacecraft EMC technology is a practical engineering technology based on tradi-
tional theory. Based on many years of experience on EMC engineering projects in
the ﬁelds of aerospace, aviation, and vehicle, experts believe that the characteristics
of spacecraft EMC conform to Pareto’s law, that is, about 80% of EMC problems
are common, and the rest 20% are unique to various industries. This indicates that
technicians should focus on the study of spacecraft-speciﬁc EMC problems on the
basis of mastering EMC engineering techniques and methods.
Spacecraft EMC is characterized by meeting the speciﬁcations while taking into
account constraints such as weight, reliability, space environment, and cost. Some
EMCsolutionsthatcommonlyusedinotherindustries,suchasusingferriteabsorbing
rings on cables, adding shielding to the electromagnetic interference (EMI) circuits
within the equipment, etc., may not be the ﬁrst choice because they directly affect
the weight and reliability of the spacecraft equipment. So systematic design methods
such as bonding, grounding, and cable layout are preferred.
The EMCcharacteristics of the spacecraft are closely related to its electromagnetic
environment (EME). Spacecraft will generally experience various operation states
such as integration tests, launch, and on-orbit operation, so particular attention should
be paid to the effects of these conditions on EME:
(1) The integration test condition is generally referred to the assembly, electrical
performance test, and various environmental tests carried out in the puriﬁed
plants. It is necessary to consider the inﬂuence of the EME of different test areas
on the spacecraft and its electronic equipment, such as electrostatic control at
the assembly site, EM radiated interference at the electrical performance test
site, and conducted EMI in the power supply and ground during environmental
testing;
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_1
1


2
1
Introduction
(2) In the launch condition, the spacecraft shall be able to withstand the effects of
high-power EM radiation from tracking radars and measurement and control
equipment of the launch vehicle at the launch site;
(3) For spacecraft in the orbital operating condition, it is essential to consider the
combined effects of the space EM environment and other spacecraft on adjacent
orbits. For LEO spacecraft, considerations should be given to the EMI from
ground-based radars and communication signals.
In the development of spacecraft, more inherited and productized equipment will
be used in platform subsystems such as TT&C, attitude control, navigation and
positioning, and power supply and distribution, which will not only reduce the cost
of redesign, but also gradually improve their reliability according to their on-orbit
operations. However, whether this equipment is compatible with EME of the new
models of spacecraft requires joint analysis and evaluation by the EMC technicians
and product designers.
1.1
Particularities of Spacecraft EMC
The common EMC problems for spacecraft include conventional Conducted Emis-
sions (CE), Conducted Susceptibility (CS), Radiated Emissions (RE), and Radiated
Susceptibility (RS), while unique EMC problems include Passive InterModulation
(PIM), multipaction, space electrostatic effects, and DC magnetic ﬁeld control, etc.
Spacecraft generally has several wireless transmitting and receiving devices,
which are used for telemetry, telecontrol, tracking, communication, navigation,
and positioning. The mixed effect of these wireless transmitting frequencies may
result in PIM products, which may cause interference if falling within the receiver’s
frequency band. Therefore, measures should be taken to conduct frequency analysis
and control, and good electrical bonding methods should be adopted so as to prevent
PIM problems.
The multipaction effect of spacecraft is a resonant vacuum discharge that occurs
between two metal surfaces or on a single dielectric surface. It is usually excited
by an RF electric ﬁeld in a vacuum when the power, frequency, and gap size of the
internal structure in the microwave system satisfy certain conditions. Multipaction
depends on many factors such as vacuum, RF voltage, material surface characteristics
(contamination and surface process conditions). Multipaction may cause resonance
devices to be detuned, or transmitted microwave signal to be out of tune, or occur-
rence of narrow-band EMI close to the carrier frequency, or even erosion of compo-
nent surfaces, thus resulting in degradation of component performance or functional
failure. Therefore, RF microwave devices should be analyzed for sensitive charac-
teristics of multipaction, and related tests and veriﬁcations should be conducted if
necessary.
Space electrostatic effect is that when the spacecraft crosses the charged particle
region in the space (such as ionosphere or solar wind particle ﬂow), charges will


1.1 Particularities of Spacecraft EMC
3
accumulate on the surface of the spacecraft. Due to the difference in the conductive
properties of the surface materials, an electrostatic voltage may be formed, which
may be released as an electric arc in some circumstances. Such space electrostatic
discharge (ESD) may cause the spacecraft equipment to be reset or damaged. The
solutions are electrical bonding of different conductive surfaces and conductive treat-
ment to the insulating surfaces, so as to maximize the conductivity of the surface
materials.
The frequency of the DC or low frequency magnetic ﬁeld of spacecraft ranges
from 0 to 100 Hz, within which the magnetic ﬁeld radiation may affect the accuracy
of spacecraft attitude control or magnetic detection sensors. The solution is using
nonmagnetic materials as much as possible and adopting single-point grounding for
the primary power line.
The objective of EMC design is to ensure a considerable margin between potential
EM sensitive equipment and typical sources of interference. For example, high-
level EM radiation can interfere with sensitive devices such as analog sensors, and
some in-band low-level EM emissions can also cause interference with sensitive
communication receiving devices, so combined shielding and ﬁltering protection
methods should usually be adopted. The shielding method can be either applied to
a single cable or a module, or used for an integrated system. Taking into account
the weight limitation of spacecraft, it is recommended to use a metal foil tape for
shielding.
In the design of the spacecraft power distribution subsystem, in order to ensure
normal operation of each device, it is suggested to pay attention to the transient EMI
along the power line and conducted signal emissions. Appropriate power adjustment
design and conﬁguration of power supply ﬁlter and transient EM protection devices
should be taken to ensure a sufﬁcient margin between the source of interference and
sensitive devices.
Spacecraft EMC’s technical requirements are different from many other manda-
tory EMC standards. It has a certain ﬂexibility, can be tailored according to the
speciﬁc composition of the system and the EM characteristics of the mission, for
instance, increasing or decreasing the test items or tightening or relaxing of required
limiting values, etc., thus preventing overdesign or under design of the system while
effectively controlling EMI and protecting sensitive components.
EM simulation analysis and evaluation can be used as a test aid to predict the
EMC of the modules and components. If the module or component under evaluation
has a previous record of a successful ﬂight, and no technical state has changed and
the same space mission is performed, then the corresponding EMC test data can be
directly used for analogy analysis.
EMC technical requirements are usually broken down from “top-to-bottom”, and
are different from system level to subsystem level to equipment level. For example,
according to the radiated emissions and susceptibility requirements for modules
and components installed in a shielded chassis, the shielding effectiveness of the
chassis may be relaxed to a certain extent; also, to verify compliance with design
requirements, appropriate EMC tests and veriﬁcations shall be planned.


4
1
Introduction
1.2
Main Methods of EMI Interface Control
The EMI interface control of spacecraft system should mainly focus on the grounding
and bonding, cable interface, power supply characteristics, and shielding:
(1) Grounding can provide the current path and can be used as a reference for power
supply and signal, which can play an important role in multiple interface control.
The early spacecraft grounding design was mainly to prevent safety problems
in case of short-circuit current over-ﬂush, and also to prevent the electric charge
from accumulating between different metal surfaces and forming ESD. The
grounding design should also prevent the analog sensor from being disturbed
and control the remanence magnetic properties. Spacecrafts usually consist of a
variety of electronic equipment such as power supply, analog, and digital elec-
tronic equipment. The operating frequencies range from DC to 40 GHz or even
higher, and the current amplitudes range from nanoampere to hundred amps,
thus, the grounding methods (single-point or multi-point) should be adopted
according to different requirements. For spacecraft electronic equipment with
input power, thesingle-point groundingmethodis oftenused, sothat the“ground
loop” of the power current can be minimized by using the module structure as
a reference point; For low frequency analog circuits, single-point grounding at
both ends of the circuit and in the shielded cable can prevent ground loops; For
high frequency digital circuits, multipoint grounding in the circuit and shielding
will help to control the effect of transmission lines. In case of both high and low
frequency interference, hybrid grounding should be used.
Bonding is an important part of grounding. The low-impedance connections
between metal surfaces can reduce plasma charging and PIM effects, and good
bonding can improve the shielding effectiveness of the cables, chassis, and
spacecraft modules in high frequency bands. Grounding and bonding should be
evaluated separately for primary power supply, secondary power supply, analog,
digital, and RF (transmitter and receiver) equipment. Without careful grounding
analysis and design, certain EMC problems may occur in the later stages of the
project. For example, ground loops in the secondary power can interfere with
adjacent sensitive equipment; if detailed grounding analysis is not performed,
this problem is difﬁcult to be detected during normal tests and may be exposed
until on-orbit ﬂight.
(2) Cable is an interface for signal transmission. Such an interface should provide
effective suppression measures for the corresponding conducted EMI while
transmitting signals. A large quantity of cables is used on spacecraft to connect
equipment and components. The detailed information of connected nodes for
these cables is usually given in the Interface Data Sheet (IDS). The IDS infor-
mation facilitates the implementation of system EMC analysis and design. A
common EMC approach is to determine the “interference margin” for each inter-
face and establish an “interference control baseline” based on these margins.
The interference control baseline includes interference characteristics such as
cross-modulation, reﬂection, ground potential variation, and external inducted


1.2 Main Methods of EMI Interface Control
5
interference. A 6 dB margin added to all interference combinations is gener-
ally used as the interference control reference. Cable interface controls include
assembly of cables and connectors, cable shielding and grounding, and cable
layout and isolation. Because cable shielding will increase the weight, ﬁltering
of interface signal should be considered as the ﬁrst option, followed by shielding
treatment. In engineering practice, most EMI signals will be suppressed by the
ﬁlter inside the equipment.
(3) Power supply is the energy transmission interface of the equipment. While the
power supply provides the power to make the equipment operation normally,
the performance of the equipment should not be degraded due to its EMI such
as voltage drop, surge or ripple. A spacecraft is a system that uses a solar array
to provide DC power to its electronic devices while charging the battery. So,
ﬁrst, we should pay attention to the impact of conducted interference on the
equipment by the power distribution subsystem, and use ﬁlters and transient
protection devices to provide sufﬁcient voltage adjustment capability. Second,
pay attention to the magnetic ﬁeld emission of the power subsystem and try to
reduce its impact on spacecraft remanence control. It is necessary, therefore,
to analyze or test the emission level and susceptibility threshold of the power
port of the electronic devices to ensure that the required EMC design margin
is met. It is recommended that the power subsystem and the connected elec-
tronic equipment be considered as a complete veriﬁcation object for analysis and
testing. In spacecraft systems, it is crucial to control and optimize the EMC char-
acteristics of the power subsystem to ensure its compatibility with the system
operation. The Power Control Unit (PCU) is an important device responsible for
spacecraft power supply, battery charge and discharge control, regulation and
protection, the corresponding EMC technical requirements should be raised. For
example, speciﬁc requirements should be put on the EM conducted emission
and susceptibility characteristics of the PCU under different operation condi-
tions, It is necessary to prevent the transmission of interference signals by the
power supply, and also to avoid the power supply safety after being interfered
out of control.
(4) Shielding is aimed to control the EM radiation ﬁelds, including both the internal
EM ﬁeld in the spacecraft and the external EM ﬁeld that needs protection. For
example,thehigh-powertransmissionofaspacecraft’sexternalradiotransmitter
may cause radiated interference to the electronic devices on the spacecraft, so it
is necessary to make shielding design to the module for appropriate protection.
The electronic equipment of the spacecraft system must be interconnected by
cables, which requires to control the shielding effectiveness of the cables due to
the potential of crosstalk between long-distance parallel cables with interference
andsensitivesignals.SomeEMI-sensitiveoptoelectronicdevicesorcomponents
(e.g. infrared earth sensors, star tracker) may be placed in areas with strong EMI.
Therefore, it is necessary to consider corresponding EMI protections during
product development, such as separate shielding and overall shielding measures.
Note that the most critical issue in all shielding measures is to properly handle
the shield seams and the cables feed through the module.


6
1
Introduction
The spacecraft EMC design needs to be planned from the general system, and
implement it step by step into speciﬁc solutions for equipment, circuit boards, and
components. Attention should be paid to the implementation of EMC requirements
in the design review at the system level, subsystem level, and equipment level. Some-
times a short review of a circuit or a module at the early stages is more important than a
few weeks or even months of EMI troubleshooting in the later stages. In EMC design,
special considerations should be given to the circuits of critical equipment, such as
clocks, controllers (reset, interrupts, etc.), power regulators, low-level analog circuits,
and input/output (I/O) circuits. Among them, the clocks and power regulators usually
produce radiated emission interference; the signal circuits such as controller reset
and interrupt are susceptible to transient conducted interference; the low-level analog
circuits and power regulators are susceptible to interference from RF energy; the I/O
circuits are the important interface for connection between the internal and external
EM environment, and should pay attenuation to its corresponding EM radiation and
conduction characteristics.
All EMI problems begin with the circuits and also end at the circuits. Therefore,
in the spacecraft development, detailed analysis and design, consistent tracking and
evaluation, and extensive test veriﬁcations are required to ensure that all the system
EMC speciﬁcations are achieved.
1.3
Prospects for EMC Technology Development
1.3.1
Main Stages of EMC Technology Development
The development of EMC technology generally goes through three stages: trou-
bleshooting, speciﬁcations, and system analysis, and evaluation.
In the troubleshooting stage, the main tasks are to analyze the EMI-related
abnormal problem cases, and implement EMI control methods, such as bonding,
grounding, cable layout, ﬁltering, and shielding through relevant mechanism analysis
and experience summary, in accordance with relevant requirements or speciﬁcations.
In the speciﬁcation stage, in order to help the electronic equipment designers to
gain more EMC knowledge and engineering experience, special EMC engineering
manuals will be prepared to provide technical guidance and reference, and EMC
design and modiﬁcations will be integrated into product development. Taking into
account the EMC risks of the inherited and productized equipment in the new system,
in terms of the EMC characteristics of spacecraft safety and mission critical equip-
ment in high-level EM radiation environment, it is necessary to clarify the technical
requirements for EMI control and protection, and conduct veriﬁcations by using
standard EMC testing methods at both equipment and system levels.
With the increasing complexity of spacecraft electronic equipment, some space
EM environment effects are difﬁcult to be tested and veriﬁed on the ground.
Some anomalies may be represented only as slight changes of parameters or state


1.3 Prospects for EMC Technology Development
7
during equipment tests, but with the extension of the system cables and increasing
complexity of the interface, they may also have major impacts on space missions.
Therefore, it is necessary to analyze the worst EME envelope in the full lifetime from
the perspective of system engineering and make predictions about the combination
of EMI and particular space effects by means of mathematical models and simu-
lation tools. This will help the EMC technicians to make technical decisions more
effectively.
The spacecraft EMC technology is a constant lesson learning process from faults
and anomalies, which can provide more effective support for the development of
spacecraft and EMI control in the future. With the increasing number of EMI prob-
lems being found and solved, and standardized EMC regulations and simulation
analysis methods being continuously improved, it will support the development of
spacecraft with a better performance, higher reliability, and enhanced efﬁciency.
1.3.2
Main Problems at the Current Stage
Withahigherdegreeofcomprehensionandintegrationofspacecraftelectronicequip-
ment, an increasing number of electronic devices using autonomous control tech-
nologies on spacecraft, and more interference factors in the space EME, the demands
for EMC technologies by spacecraft are also increasing.
1.3.2.1
Increased EMI Problems Caused by Highly Integrated
Electronic Equipment and Devices
With the increasing integration of electronic devices, integrated circuits not only
accommodate more circuit units in a smaller area, but also include the functions
of the original stand-alone equipment and subsystems, such as System-On-a-Chip
(SOC) and MIllimeter-wave Monolithic Circuits (MMIC). These highly integrated
electronics typically operate at very low voltage and current, even a small EM energy
can cause the device to reset or malfunction, so they are very susceptible to EMI.
Because a large number of electronic devices and circuits are integrated together
and their original circuit isolation and shielding are replaced, any EMI can bring risk
to the entire equipment or subsystem. Therefore, the EMI problem may constitute a
serious potential impact on the missions and loads.
The EMC technicians must consider the design and test requirements of critical
components and equipment in a highly integrated environment.


8
1
Introduction
1.3.2.2
Increasing EMI Problems Due to High Integration of Electronic
Equipment
Program-controlledelectronicdevicesarewidelyusedonspacecraftwiththeincrease
of autonomous functions in communication, navigation, and attitude control. The
programed autonomous control requires the computer to process data such as ﬂight
attitude, signal characteristics, and environmental parameters provided by various
sensors,thenperformattitudeortemperatureadjustment,signalprocessing,andother
controls according to the presettings. The digital circuit of the control computer will
radiate more EM energy in the high frequency band, while many sensors are low-
level signal sensitive devices, which are susceptible to EMI, so it is necessary to take
measures to control the different EMI characteristics of the programed electronic
equipment.
1.3.2.3
The Increase of Interference Factors in EME
With the increasing coverage of mobile communication and broadcast/television
signals and the increasing application of ground equipment, such as military and
civilian weather radars, electronic countermeasure equipment in local battleﬁelds,
the space EME in which LEO spacecraft operate is deteriorating. EM signals trans-
mitted by ground communications and radars have constituted EMI to some meteo-
rological and navigation satellites. Furthermore, as the number of on-orbit spacecraft
increases, so does the EMI problem between spacecraft. In addition, as the propul-
sion of spacecraft is increasingly shifting from chemical to fully electric power, the
EME of the spacecraft itself is also affected. Therefore, the EMC technicians should
continue to follow the trend of changing EME on the ground, in the space and for
spacecraft itself, and there must be certain foresight and marginal requirements in
the spacecraft EMC design.
1.3.3
Development Trends
Spacecraft has evolved from early optical observation satellites to various areas such
as EM detection, navigation and positioning, communication and interconnection,
deep space exploration, manned exploration. Recently, new requirements of photo-
electric detection with multi remote sensing functions, multi-spacecraft formation
ﬂight, and spacecraft complexes are put forward. With the increasing complexity of
spacecraft EM payloads and integration of electronic devices and widespread use of
program-controlledelectronicdevices,thedemandsforspacecraftEMCtechnologies
are even more urgent.
The service lifetime of spacecraft has been extended from the early 2 or 3 years
to 5 or 8 years, and even some long-lifetime spacecraft are designed for 15–20 years.
Considering that in the long-term on-orbit operation, the anti-interference ability


1.3 Prospects for EMC Technology Development
9
of some electronic devices will be degraded at the end of lifetime and there is a
potential of EMI problem, it is required to have a certain margin in the design.
Moreover, for long-term space science research and exploration activities such as
manned spaceﬂight, considerations must be given to meet the requirement of different
payloads. The EM radiation environment of critical electronic equipment and the
safetyofastronautsshouldbeconsideredinthelayoutofequipmentandconﬁguration
of the operational frequency band.
Asthesizeandcomplexityofthespacecraftisincreasing,itbecomesmoredifﬁcult
to completely rely on traditional laboratory testing for detecting and controlling EMI
problems. So, it is necessary to strengthen the combination of analytical techniques
and laboratory testing methods, and extensively carry out EMC veriﬁcations.
The mechanism of critical circuits and the EM properties of core equipment
are the key to EMI analysis and control. Research on the mechanism of electronic
device interference should be continued to acquire corresponding data on the EM
susceptibility characteristics of the core equipment in order to provide technical
support for EMC design and EMI control.
The calculation of theoretical formulas, software simulation, laboratory testing
and on-site troubleshooting is an organic unity, which requires design manuals, simu-
lation tools, testing method and data analysis and processing capabilities. The scat-
tered equipment EM characteristics should be gradually integrated into system EMC
results to ensure successful operation of space systems.
Given the above, the complexity of the spacecraft EMI problem requires system-
atic analysis and interference identiﬁcation of the detection data. In many cases, this
involves the prediction of system level EMC problems based on equipment level EMI
data. In addition, EMC and integrated electrical testers must pay attention to the inter-
action of test information to ensure that the electronic equipment or system under
test is set up according to the ﬂight state of the spacecraft in orbit, and compared with
the ﬂight performance indicators. In terms of development trends, the EMC work
for complex spacecraft systems needs comprehensive support from various tech-
nologies, such as multi-EME effects (E3) simulation and analysis, collection and
comparison between EM anomaly and test data, and intelligent automated testing.
1.4
Summary
With the increasing sensitivity to EMI of electronic devices used in spacecraft, the
widespread use of program-controlled electronic devices, and the increase of inter-
ference factors in EME where the spacecraft operate, EMC technologies need to
address the special needs of spacecraft, while dealing with common EMI problems,
and intensive research should be conducted on interface control technologies such
as grounding, cable, power supply, and shielding, so as to provide more effective
technical support for the success of space missions.

# Zhang《Spacecraft EMC Technologies》第5章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 5. Analysis of Spacecraft System-Level Electromagnetic Compatibility

Chapter 5
Analysis of Spacecraft System-Level
Electromagnetic Compatibility
In the previous sections, the design requirements and analysis methods of bonding,
grounding, shielding, and cable layout in the electromagnetic environmental effects
(EME) of spacecraft systems were described. Starting from the aspects of EMI
margin, intra-system electromagnetic compatibility (EMC), the hazards of electro-
magnetic radiation to personnel and electric explosive devices (EED), etc., and elec-
tromagnetic spectrum compatibility, this chapter mainly addresses the basic methods
and processes of analysis.
5.1
Overview of Standards for Spacecraft System-Level
EMC
The design of the Chinese spacecraft is mainly based on the national standards, the
national military standards, and the standards of the aerospace industry. However,
there is no English version, so this book focuses on the introduction of international
spacecraft system-level EMC standards.
(1) MIL-STD-464C-2010, Electromagnetic Environmental Effects Requirements
for Systems, Department of Defense Interface Standard;
(2) AIAA-S-121A-2017, Electromagnetic Compatibility Requirements for Space
Equipment and Systems, American Institute of Aeronautics and Astronautics;
(3) SMC-S-008-2008, Electromagnetic Compatibility Requirements for Space
Equipment and System, Air Force Space Command, Space and Missile Systems
Center Standard;
(4) ECSS-E-ST-20C-2008, Space Engineering, Electrical and Electronic, European
Cooperation for Space Standardization;
(5) ECSS-E-ST-20-07C-2012, Space Engineering, Electromagnetic Compatibility,
European Cooperation for Space Standardization;
(6) ISO 14302-2002, Space Systems-Electromagnetic Compatibility Require-
ments, International Standard;
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_5
85


86
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Spacecraft system 
design report
Life cycle
E3 hardness
Internal 
EME
External 
RF EME
Cable layout
External RF 
EME
HPM 
sources
Lightning 
effect
EMP effect
Systematic 
analysis of EME
Subsystem and 
equipment EMI
Electrostatic 
charging control
System level EME 
requirements
EMRADHAZ
Electric bonding, 
grounding and 
isolation
Margins
Detailed design 
document of 
equipment
Equipment 
configuration 
information
Fig. 5.1 The relationship of the system-level EMC requirements
The system-level EMC requirements are also known as the EME requirements for
systems, which are to clarify the EMI control requirements by analyzing the impact of
the system’s internal and external electromagnetic environment on the system perfor-
mance. It mainly includes EMI margins, external RF electromagnetic environment,
high-power microwave (HPM) sources and electromagnetic pulse (EMP), light-
ning, electrostatic charge control, intra-system EMC, subsystem, equipment EMI
control and electromagnetic radiation hazards (EMRADHAZ), electrical bonding,
grounding, electromagnetic spectrum supportability, etc., their relationship is shown
in Fig. 5.1.
Table 5.1 is based on the key elements of MIL-STD-464C, in which other stan-
dard speciﬁcations are compared. Common types of electromagnetic environmental
effects and major limit requirements are marked respectively, providing an indicative
reference for EMC risk analysis and quantitative design of the system.
In addition to the common requirements of EME, the following are special
requirements in system-level EMC:
(1) AIAA-S-121A
➀Magnetic ﬁeld environment: in addition to focusing on an external RF electro-
magnetic environment, it is speciﬁcally required to control the magnetic dipole
moment of the spacecraft platform and to ensure that the subsystems and equip-
ment on the spacecraft are not degraded by an external or internal AC or DC
magnetic ﬁeld.
➁The electric current return network shall be designed with consideration for
system circuits and structures in order to control the effects of return currents on
system performance.


5.1 Overview of Standards for Spacecraft System-Level EMC
87
Table 5.1 Summary of spacecraft system-level EMC requirements
Technical
requirement
MIL-STD-464C
AIAA-S-121A
SMC-S-008
ECSS-E-ST-20C
ECSS-E-ST-20-07C
ISO
14302
Margins
A
A
A
A
A
Intra-system
EMC
A
A
A
A
A
External RF
EME
A
A
A
A
A
HPM sources
A
Lightning
A
S
S
S
S
EMP
A
S
S
Subsystem
and equipment
EMI
A
A
A
A
A
Electrostatic
charge control
A
A
A
A
A
EMRADHAZ
A
A
A
A
Life cycle, E3
hardness
A
A
A
A
Electrical
bonding
A
A
A
A
A
External
ground
A
A
A
A
A
TEMPEST
S
S
System
radiated
emission
A
A
A
EM spectrum
supportability
A
A
A
A
Magnetic ﬁeld
environment
A
A
A
System circuit
and structure
reference
A
A
Return current
control
A
A
Wiring
A
A
A
PIM
A
A
Legend A Application, S Procuring activity must specify in the procurement documentation


88
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
➂The wiring shall be grouped, isolated, and implemented with necessary shielding
design.
(2) SMC-S-008
➀The veriﬁcation method of electromagnetic interference margin in space system
is introduced, including electromagnetic self-compatibility and electromagnetic
interference margin in both conducted and radiated states.
a.
The basis of veriﬁcation: the adopted analysis and test methods shall fulﬁll
the respective approval procedures and comply with the corresponding
constraints.
b. Self-compatibilityveriﬁcation:theelectronicequipmentshallbefullyconﬁg-
ured and all equipment shall be deployed according to the working state
(including solar arrays). Moreover, all the equipments are veriﬁed in various
operating modes and frequency bands, and sensitive characteristics of
all uplink, downlink, and critical circuits are monitored to determine the
self-compatible performance of the system.
c.
Self-compatibility and EMI margin veriﬁcation of conducted emission:
during the self-compatibility veriﬁcation, the conducted emission data in the
frequency domain and time domain of the power lines and the critical circuits
are monitored and recorded, and then compared with the conducted suscep-
tibility characteristics of the equipment, so as to determine the conducted
EMI margin of the interface circuit under veriﬁcation.
d. Self-compatibility and EMI margin veriﬁcation of radiated emission: during
the self-compatibility veriﬁcation, the system electric and magnetic radiated
emission should meet the requirements and have the corresponding margin.
Note that the bandwidth of radiated emission measurements should include
not only the platform passband, but also the LNA bandwidth ±10%.
e.
External RFI compatibility and EMI margin veriﬁcation: during the self-
compatibility veriﬁcation, the radiated susceptibility tests (RS103) shall be
performed on the spacecraft system as required, in which the system shall
meet the 6 dB EMI margin requirements. If susceptibility is detected, the
susceptibility threshold should be determined. Note that the duration of the
test for RS103 should be at least 20 min to ensure adequate response time
for spacecraft equipment. Typically, the dwell time at each frequency point
should not be less than 3 s.
f.
External RFI compatibility and EMI margin veriﬁcation of EED: during the
external RFI compatibility test, 20 dB safety margin veriﬁcation shall be
performed for each EED on the spacecraft. The EED can be replaced by a
EED simulator, which may be an optical, electrical or a fuse simulator.
g. Self-compatibility and EMI margin veriﬁcation of PIM: during the system
self-compatibility test, the electric ﬁeld radiated emission and PIM products
should meet the requirements of RE102 and EMI margin.


5.1 Overview of Standards for Spacecraft System-Level EMC
89
h. Conducted emission and EMI margin veriﬁcation with external RFI: during
the external RFI compatibility test, monitor and record the conducted emis-
sion data in the time domain and frequency domain of the power lines and
the critical circuits. Compare this with the susceptibility characteristics of
the equipment, and determine the conducted EMI margin of the interface.
i.
PIM and EMI margin veriﬁcation with external RFI: during the external RFI
compatibility test, the interference data of electric ﬁeld radiated emission and
PIM products on the receiver are monitored and recorded to determine the
EMI margin of PIM interference and the receiver.
Table 5.2 gives an example of the spacecraft EMI margin veriﬁcation matrix
➁Spacecraft passive intermodulation
The RF transmissions from onboard equipment, or from external transmitters may
interact with the electronic equipment to produce unintentional signals such as PIM,
which will interfere with the onboard receiver. Protective measures, such as electrical
bonding and semiconductor device protection, should be taken.
Electrical bonding of equipment and contact between conductors or semiconduc-
tors shall have a resistance ranges 0.1–500 k.
Table 5.2 Spacecraft EMI margin veriﬁcation matrix (SMC-S-008)
Veriﬁcation item
Applicability
EMI
margin
Active
uplink
Rx
Ant.
Tx
Ant.
External
RF
(RS103)
Combine
a. Basic (veriﬁcation
method)
A
b. Self-compatibility
A
A
A
A
S
c. Self-compatibility
+ EMI margin
(CE)
A
A
S
S
S
S
b.
d. Self-compatibility
+ EMI margin
(RE)
A
A
A
A
S
S
b.
e. External RFI +
EMI margin
A
A
A
A
A
b.
f. External RFI +
EMI margin (EED)
A
A
S
S
A
A
e.
g. Self-compatibility
+ EMI margin
(PIM)
S
A
A
A
A
S
b.
h. CE + EMI margin
(external RFI)
S
A
S
S
S
A
e.
i. PIM + EMI
margin (external
RFI)
S
A
A
A
A
A
e.g.


90
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Semiconductor devices should be protected from exposure to RF transmitters or
external radiation sources, and the environmental ﬁeld strength within the working
band should not exceed 250 mV/m to reduce PIM.
The veriﬁcation frequency should cover 7th order intermodulation products.
(3) ECSS-E-ST-20-07C and ECSS-E-ST-20C
➀Spacecraft DC magnetic ﬁeld emission: DC magnetic ﬁeld emission may
impact on the magnetic sensor of payloads and the attitude control system
(ACS). The magnetic moment of small spacecraft should not exceed 1A ·
m2, and that of large spacecraft should not exceed 10A · m2. The solar array
needs separate control. If a low-orbit spacecraft has a magnetometer, the
impact of the platform on the deﬂection should be less than 1μT.
➁Radio frequency compatibility: it is necessary to determine the requirements
of harmonic and spurious emission limits of spacecraft antenna ports and the
susceptibility of receivers to out-of-band interference. The RF compatibility
analysis shall include the effects of intermodulation products.
➂Electrical Bonding requirements: the DC resistance between the equip-
ment bonding stud and the nearby spacecraft structure shall be less than
2.5 m. The DC resistance between the equipment grounding stud and
each connector should be less than 10 m. The DC resistance between the
unit’s housing and the ground reference point at the system-level should be
less than 20 m.
➃Shielding: the spacecraft should be structured as a “Faraday cage” and
consider apertures used for pressure drop during ascent and for outgassing.
➄Wiring: the cables shall be bunched according to the requirements of classi-
ﬁcation. Similar cables can be integrated into the same bundle. If different
cables are routed on parallel paths, they shall be separated by 5 cm or by
a metal screen. Wires and cables shall be marked so that the personnel can
distinguish the EMC category.
(4) ISO 14302
➀The electrical bonding part includes power current feeder and return
paths, shock and safety hazards, antenna counterpoise, RF potentials, static
discharge, and explosive atmosphere protection.
➁Electromagnetic radiation hazards, while considering the effects on fuels,
personnel and EED, should also ensure that electronically actuated thrusters
are not exposed to unsafe electromagnetic radiation levels.
According to spacecraft system-level EMC standards Table 5.2, the general
requirements commonly used are the EMI margin, inter-system EMC, intra-system
EMC, subsystem and equipment EMI control, electrostatic charging control, elec-
tromagnetic radiation hazards, life cycle E3 hardness, electrical bonding, external
grounding, EM spectrum compatibility management, etc. The inter-system EMC
includes the external RF electromagnetic environment and emission control. Other


5.1 Overview of Standards for Spacecraft System-Level EMC
91
common requirements, such as HPM, lightning, EMP, and TEMPEST are rarely
applied in the EMC of spacecraft.
In addition, spacecraft DC magnetic ﬁeld emission, electromagnetic self-
compatibility and EMI margin veriﬁcation, PIM and spectrum compatibility veri-
ﬁcation of systems are required to be improved.
5.2
Determination of EMI Margin
In order to guarantee the EMC of the spacecraft system throughout the whole life
cycle, a proper EMI margin shall be determined in the EMC analysis and the design
process. EMI margin is mainly used to analyze the differences in analysis techniques,
changes in coupling effects, variations in equipment and processes, ﬂuctuations in
environmental conditions, and variations in testing, etc. Spacecraft equipment is
classiﬁed into 4 categories based on their impact on mission and safety after being
subjected to electromagnetic interferences.
(1) EED: such as the EED control device.
(2) Category I: safety critical and mission critical equipment, EMI problem that
can result in serious injury or loss of life, delay of mission, or severe damage
to the spacecraft, such as Attitude Orbit Control Computer (AOCC), Telemetry
Tracking and Command (TT&C) transponder, Power Control Unit (PCU) or
Solar Array Drive Assembly (SADA), etc.
(3) Category II: EMI problem that can result in the degradation of spacecraft
capability, including loss of autonomous operational capability. This includes
equipment such as earth sensor or star tracker.
(4) Category III: EMI problem that can result in the loss of noncritical functions of
the spacecraft, such as some temperature sensors.
The EMI margin shall be veriﬁed at critical circuits under various operating condi-
tions. The requirements for the EMI margin in spacecraft standards are summarized
in Table 5.3.
Taking into account the consolidated requirements of EMC standard for the EMI
margin, the requirements of EMI margin for spacecraft equipment are as follows:
(1) EED: the EMI margin should be no less than 16.5–20 dB. It is recommended
to design and verify according to the 20 dB EMI margin.
(2) Category I: safety critical or mission critical equipment, the EMI margin shall
not be less than 12 dB.
(3) Category II: the EMI margin should not be less than 6 dB.
(4) Category III: the EMI margin should not be less than 0 dB.
If the EMI margin is based on the simulation analysis for the electromagnetic
emission and susceptibility data, then the margin of the category I and category II
equipment should be increased by 6 dB according to the above requirements.


92
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Table 5.3 Summary of EMI margin requirements in standards
Standards
EMI margin based on test (dB)
EMI margin based on analysis
(dB)
MIL-STD-464C
EIDs for maximum no-ﬁre
stimulus (MNFS) for safety
assurances
16.5
EIDs for MNFS for other
applications
6
Safety critical and mission
critical
6
AIAA-S-121
EID interfaces, RF level
referenced to DC no-ﬁre level
20
20
EID interfaces, RF level
referenced to RF no-ﬁre level
12
12
Category I or II critical circuit
6
12
All other equipment,
subsystems, and systems,
including Category III critical
circuits
0
0
SMC-S-008
EED interface, RF level
referenced to DC no-ﬁre level
20
EED interface, RF level
referenced to RF no-ﬁre level
12
–
Safety critical and mission critical equipment
Qualiﬁcation tests
12
18
Acceptance tests
6
All other equipment,
subsystem, and system
0
6
ECSS-E-ST-20C
Safety critical circuits
20
Mission critical circuits
6
5.3
Inter-system EMC Analysis
The inter-system EMC analysis of spacecraft includes: the EMC analysis between
spacecraft and launch vehicle and the EMC analysis between spacecrafts on-orbit.
The analysis of the spacecraft on-orbit includes RF ﬁeld strength analysis, multipath
analysis, and polarization isolation analysis of GEO spacecraft in near orbit.


5.3 Inter-system EMC Analysis
93
5.3.1
EMC Analysis of the Spacecraft with Launch Vehicle
EMC analysis and evaluation between the spacecraft and the launch vehicle are
required during the prelaunch and launch phase. In order to simplify the analysis,
some of the spacecraft’s RF equipment (except for Telemetry and navigation posi-
tioning) is shut down during the launch phase. This helps the analysis of EMC
between the spacecraft and launch vehicle. The separation plane of the spacecraft
and the launch vehicle is used as a reference for the analysis. Shown in Fig. 5.2.
The EMC analysis between the spacecraft and the launch vehicle mainly refers
to RF compatibility, that is, the inﬂuence of the spacecraft radiated emission on
the launch vehicle and the inﬂuence of the launch vehicle radiated emission on the
spacecraft. The electromagnetic radiation information of the launch vehicle and the
launch site can be obtained through EMC in the user manual of the launch vehicle.
The electromagnetic radiation characteristics of spacecraft during launch are usually
related to power supply, TT&C, and navigation and positioning equipment. The
information of spacecraft RF equipment should include frequency band, transmission
power, receiving sensitivity, and installation position. The EMC analysis results of
the spacecraft and the launch vehicle should be recorded in the Interface Control
Document (ICD). This information should be re-conﬁrmed during the system-level
EMC test and the general inspection before launch.
(1) Analysis of the inﬂuence of the spacecraft radiated emission on launch vehicle
The radiation emission of spacecraft generally consists of intended telemetry signal
and the unintentional electromagnetic emission of power supply and distribution
equipment.
Fig. 5.2 Separation plane of the spacecraft and the launch vehicle


94
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
➀The EMC analysis of the spacecraft telemetry signal to the launch vehicle is
mainlytoevaluatewhethertheelectricﬁeldintensityoftheelectromagneticemis-
sion signal exceeds the radiation sensitivity requirement of the launch vehicle in
this frequency range.
Assuming that the measured and controlled transmission power is Pt and the gain
in the analysis direction is Gt, the spatial power density at the distance R from the
antenna is Sav:
Sav = PtGt
4πR2
(5.3.1)
According to the Poynting vector, assuming the electric ﬁeld intensity at the
analysis position is E, then the power density can also be calculated as
Sav = |E|2
η0
,
(5.3.2)
where η0 is the impedance of free space wave, and its value is 120π.
The Eq. (5.3.1), is substituted into Eq. (5.3.2)
|E| =
√30PtGt
R
(5.3.3)
In general, R is 1 m. The radiation ﬁeld intensity of the spacecraft telemetry
signal is obtained through the Eq. (5.3.3), which then can be compared with the
corresponding radiation sensitivity requirements found in the user manual of the
launch vehicle. In this way, inter-system EMC can be determined if it fulﬁlls the
requirements.
➁The EMC analysis of spacecraft’s unintentional radiation emission to the launch
vehicle is mainly to check whether the electromagnetic radiation data or control
requirements of the spacecraft exceed the radiation sensitivity requirements in
the launch vehicle user manual or interface control documents.
(2) Analysis of electromagnetic radiation effects of launch vehicle on spacecraft
User manual (launch vehicle) or radiation emission characteristic in interface control
documents (launch vehicle) are primarily used as a reference to analyze the effect
of launch vehicle electromagnetic radiation emission to spacecraft. The analysis
consists of the critical position in the spacecraft such as command receiver of ﬁeld
strength or power density, then compare with the command receiver sensitivity to
determine whether the requirements of inter-system EMC are satisﬁed. In the analysis
process, the analysis table as shown in Table 5.4 is established.
Among them, through the distance between the launch vehicle transmitter and
the spacecraft sensitive equipment, the free space loss of electromagnetic signals is
calculated via Friis formula


5.3 Inter-system EMC Analysis
95
Table 5.4 Analysis of the impact of launch vehicle/site radiation on spacecraft
Launch vehicle/site
radiation frequency band
X frequency band
Y frequency band
……
Z frequency band
Radiation electric ﬁeld
intensity of the
spacecraft (dBμV/m)
Radiation electric ﬁeld
intensity of the
spacecraft (V/m)
Frequency (Hz)
Wavelength (m)
The worst-case gain of
the TC&R antenna (dBi)
The worst-case gain of
the TC&R antenna
(linear)
Free space loss (dB)
Loss of feeder, ﬁltering,
etc. (dB)
The maximum
interference level at the
TC&R receiver input
port (dBm)
TC&R receiver
interference magnitude
(dBm)
Margin (dB)
PR = GtG Rλ2
(4πr)2 Pt = G Rλ2
4π
PtGt
4πr2 ,
(5.3.4)
where:
PR—The power of receiving antenna port, W;
G R—The gain of the receiving antenna in the analysis direction (times);
Pt—Transmitter power, W;
Gt—The gain of the transmitting antenna in the analysis direction (times);
λ—Wavelength, m.
Transforming from Eq. (5.3.3) and (5.3.4), we have
PR =
E2
120π × G R × λ2
4π
(5.3.5)


96
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Table 5.5 Analysis of the impact of launch vehicle/site radiation on spacecraft
Launch vehicle/site
radiation frequency band
S band telemetry transmitter
S band beacon
C band responder
Radiation electric ﬁeld
intensity of the spacecraft
(dBμV/m)
148
107
107
Radiation electric ﬁeld
intensity of the spacecraft
(V/m)
25.1
0.22
0.22
Frequency (Hz)
2.2E+9
2.7E+9
4.2E+9
Wavelength (m)
136.3E−3
111.1E−3
71.4E−3
The worst-case gain of the
antenna (dBi)
2
2
2
The worst-case gain of the
antenna (linear)
1.58
1.58
1.58
Loss of feeder, ﬁltering,
etc. (dB)
90
90
90
The maximum interference
level at the receiver input
port (dBm)
−84
−127
−131
Receiver interference
magnitude (dBm)
−25
−25
−25
Margin (dB)
59
102
106
The free space loss can be calculated by the above equation. Table 5.4 can be
used to analyze whether the radiation emissions from the launch vehicle/site meets
the requirements of spacecraft EMC.
Table 5.5 is an EMC analysis example of the LM-3A series launch vehicle and
the DFH-4 communication satellite platform.
5.3.2
RF EMC Analysis of One Vehicle with Multi-satellite
Multi-satellite launch missions use one launch vehicle to deliver two or more satel-
lites to the desired orbit, which could greatly reduce the cost of launching a single
spacecraft. With the improvement of satellite integration and the progress of multi-
satellite launch technology, multi-satellite launch is getting more and more popular.
Compared with the traditional one-satellite launch, multi-satellite launch brings new
challenges to electromagnetic compatibility design. Multi-satellite launch EMC anal-
ysis is much more complicated than the two-factor analysis in one-satellite launching
case.
The common double-satellite launch with a series of arrangement is shown in
Fig. 5.3. The analysis of one-satellite launch EMC includes the following three


5.3 Inter-system EMC Analysis
97
Down-satellite
Up-Satellite
Launch Vehicle 
Fairing
a). Whole fairing model
b) Up-satellite fairing separation in flight
Fig. 5.3 Double-Satellite launch structure with a series arrangement
elements:launchvehicleself-compatibility,satelliteself-compatibility,compatibility
between launch vehicle and satellite. In multi-satellite launch, launch vehicle self-
compatibility and satellite self-compatibility is similar to one-satellite launch. The
compatibility between launch vehicle and satellite is changed to one vehicle with
multi-satellite. Additionally, compatibility among satellites is a new issue to be
considered in multi-satellite launch EMC. There will be some changes in ﬂying
state, electromagnetic modeling, and results judgments. For example, the impact
of fairing separation on up-satellite TT&C, multi-body modeling, same frequency
interference judgment of up and down-satellites.
There are two EMC key points in the actual multi-satellite launch engineering.
First, whether multi-satellites TT&C can function smoothly in launch mode? Second,
whether the satellites can properly work in the electromagnetic environment in the
fairing? The analysis procedures of the above two points are shown in Fig. 5.4.
(1) Establishment of satellite and launch vehicle’s physical structure
Although the basic dimensions of rockets and satellites are usually determined, the
position and size of the wave transmission window of launch vehicle fairing should
be customized and designed. At ﬁrst, three fundamental questions are to be solved.
How many windows would be ﬁtted? What are the sizes of the windows? Where are
the windows placed? All these are decided by the TT&C angle.
TT&C angle is the angle between the main lobe of TT&C station T&R antenna
and the main lobe of the vehicle/payload R&T antenna. It must make sure station


98
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Start of analysis
Physical Structure 
Establishment
Electromagnetic Model 
Establishment
TT&C Performance Validation
OK?
Internal Field Evaluation
OK?
End of analysis
Physical Structure 
Establishment
No
No
Yes
Yes
Fig. 5.4 Multi-satellites launch EMC analysis procedure
T&R antennas’ main lobe is corresponding to vehicle antennas’ main lobe, as shown
in Fig. 5.5. Moreover, the TT&C angle is calculated from the orbit and antenna
parameters.
TT&C angle is used to calculate the vehicle radiated area, which should cover the
TT&Cangleandcontainsomemargins.Additionally,radiatedareaonlyconsidersthe
line-of-sight factor in this step, and microwave transmitted effect will be concerned
in later steps. The hollows obtained by cutting the fairing with the radiated area
are the fairing windows, so the quantity, size, position of the fairing windows are
determined. Generally, multi fairing windows are used in multi-satellite launch, more
than one analysis loop should be carried out to optimize the fairing windows design,
which involves electromagnetic characteristics, structure strength, and operate area
analysis.
When the fairing windows are determined, the physical dimensions of the launch
vehicle and satellite are determined. The next step is the establishment of the
electromagnetic model of multi-satellites launch.


5.3 Inter-system EMC Analysis
99
Earth
Aerosphere
Radiated Area
Radiated Area
TT&C Station
Fig. 5.5 Sketch of radiated area and TT&C angle
(2) Establishment of the electromagnetic model
Launch vehicle is an electrical-large-scale object, therefore, launch vehicle and
fairing window modeling should choose high frequency methods, such as MLFMM,
UTD, PO, GP. The model should contain fairing, window, vehicle, payload, and
antenna structures. This kind of whole-body model is not only accurate but also
complex. However, it takes a lot of time and RAM to solve the problem by using
high frequency algorithm, so it becomes the bottleneck of practical application.
And it becomes more serious in multi-satellite launch case. So the model should be
simpliﬁed, usually, the whole launch vehicle and fairing window body model could
be transformed into a segment model, and the accuracy is sufﬁcient for engineering
applications.
The layouts of double-star launch with a series arrangement are shown in Fig. 5.6,
the whole launch vehicle and fairing window body model contains an integrated
vehicle, a payload body, and a window structure. The simpliﬁed model is developed
fromthewhole-bodymodel,whichmakesupofpayloadsurface,fairingmainsurface,
wave transmission windows. The computing area of the segment model is much
smaller than that of the whole body model, so computing time and memory will
greatly decrease. The metal surface could be served as an ideal surface without
thickness. Fairing windows could be regards as an air window, and its penetrating
characteristic is controlled by link margin.
Comparison of modeling methods is shown in Table 5.6.
(3) TT&C performance validation
TT&C performance is the most important factor in fairing design, which mainly
involves two cases, namely the launch tower test and the TT&C station test.


100
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
a). Whole body model of double-star launch with series arrangement
b). Simple segment model of up-satellite with fairing
c). Simple Segment model of down-satellite with fairing
Fig. 5.6 Whole body and segment model


5.3 Inter-system EMC Analysis
101
 
d) Simple segment model with up-half fairing separation
Fig. 5.6 (continued)
Table 5.6 Comparison of modeling methods
Algorithm
Model
Memory
consumption
Calculating time
UTD (uniform theory
of diffraction)
Whole-body model
<5 MB
15 angle division of
antenna space, 300 h
Simple segment model
<5 MB
15 angle division of
antenna space, 30 min
MLFMM (multilevel
fast multipole method)
Whole-body model
10% wavelength
Division, 1 TB
10 angle division of
antenna space, 8 h
Simple segment model
10% wavelength
Division, 750 MB
10 angle division of
antenna space, 8 h
A. Launch tower test.
In the launch tower test, the links between ground antennas and spacecraft antennas
should be unblocked. The most important thing is to ﬁnd the strongest gain point to
mount the ground antenna, and it will signiﬁcantly improve the link performance.
However, ground antennas can only be mounted on the long and narrow launch
tower. So the mounting position is limited by the launch tower structure. There are
two questions that need to be solved. Where should the ground antennas be placed?
How to adjust the position of the ground antenna to improve the link budget?


102
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.7 Option of ground
antenna position
R
Radiated Area
Ground Antenna 
Position Area
a). Vertical ground antenna position region 
R
Radiated Area
Ground Antenna 
Position Area
b). Horizontal ground antenna position region 
As shown in Fig. 5.7, launch vehicle model, radiated area, and launch tower are
integrated. The larger gain point is found, which is in the radiated area and launch
tower structure overlapped region. This point can be chosen as the ground antenna
mounting place.
Finally, tangential geometry is used to adjust the link budget, as shown in Fig. 5.8.
If the angle varies all the gain may change distinctly, so every adjustment should be
at least more than 1 h in other words, the position step length should be greater
than 2Rtg0.5l, which R is the horizontal distance between the ground antenna and
vehicle antenna. As shown in Eq. (5.3.6), step length can be generally approximated
to 0.035R.
Fig. 5.8 Ground antenna
position adjustment


5.3 Inter-system EMC Analysis
103
Fig. 5.9 Half-Space ideal
antenna pattern
2 tan 0.5◦≈2 tan 1◦≈0.035
(5.3.6)
B. TT&C station test
Communication with the ground station is the most important time in the launch
period, which is also the key point of TT&C validation. In this step, radiated area
is calculated accurately, and the microwave transmitted effect is taken into account.
And it is necessary to check whether the radiated area covers the TT&C angle or not.
An ideal half-space antenna is taken as an example. Its antenna pattern in free
space is shown in Fig. 5.9. The antenna pattern in Fig. 5.10 is calculated with the
fairing. The free space pattern is uniform and smooth. However, the radiation pattern
with the fairing becomes distorted. The radiated area remarkably decreases, so does
the cover proportion.
Because the radiated area with a fairing window is not symmetrical and ﬂuctuates
rapidly, it is not very suitable to use Cartesian and polar gain patterns to represent the
asymmetric pattern. And the reader cannot easily ascertain an accurate angle from the
3D gain pattern. So 2D gain pattern is preferred since it can clearly ascertain the theta
and phi angle, as shown in Fig. 5.11. Furthermore, 2D black-white map is used to
check the radiated area. The white points denote gain satisﬁes TT&C requirements,
and black points denote unsatisﬁed area.
Then TT&C angles are reloaded on the 2D black-white map. If TT&C angles are
all white, it denotes that the TT&C link satisﬁes the budget. If there are some black
blocks in TT&C angles, some adjustment measures should be adopted to improve
the TT&C performance.
A lot of satellites adopt spread spectrum communications in the same frequency
band to save spectrum resources, which use code division to distinguish different
satellites.Usualco-channelinterferencecouldbeacceptedinspreadspectrumTT&C,


104
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.10 Antenna pattern with the fairing
65
70
75
80
85
90
95
80
90
100
110
Phi
Theta
a). 2D radiated area
b). 2D TT&C black-white check
65
70
75
80
85
90
95
80
90
100
110
Phi
Theta
Fig. 5.11 TT&C station performance test
but if co-channel signals are far greater than the desired signals, TT&C will be
unlocked. In multi-satellite launch, several satellites use the same communication
frequency, so the communication signals become a co-channel interference to other
satellites, especially in the ﬂight structure variation process. For example, in a stage
in multi-satellite launch, up-satellite fairing was separated, but down-satellite fairing


5.3 Inter-system EMC Analysis
105
was still working. Signals intensity of up-satellite were much greater than that of the
down-satellites, so a compromise compatible design should be carried out, which
took power dividing and fairing windows into account. In case of a double-star
launch with a series arrangement, the comparison between simulation and ﬂying
results are shown in Table 5.7.
(4) Internal ﬁeld evaluation
If a fairing is available, power may reﬂect many times within it, or transmit through
the window, otherwise, microwave power radiated from the antenna will dissipate in
free space. Therefore, the internal ﬁeld environment in fairing is usually much worse
than the case without fairing, and the ﬁeld strength near the electronic equipment is
also signiﬁcantly increased. The example in Fig. 5.12 shows the E-ﬁeld distributing
change with and without fairing. In multi-satellite launch case, there are hollows in
Table 5.7 Comparison between simulation and ﬂying results
Item
Simulation results
Flying results
Link margin
Up link margin >57 dB
Down link margin >32 dB
Up link margin >55 dB
Down link margin >30 dB
Spread spectrum multi access
interference and signal ratio
<16.5 dB
<15 dB
Fig. 5.12 Comparison of
E-ﬁeld with and without
fairing
a). E-Field distributing without fairing
b). E-Field distributing with fairing


106
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
launch vehicle structure panels between satellites. The electromagnetic signal will
be mutually strengthened. So it is required to evaluate the internal ﬁeld and estimate
the effect on the equipment in fairing. If the equipment does not function well with
the internal ﬁeld, the equipment position should be adjusted, or shielding measures
should be taken. The position and size of the window could also be adjusted, which
can improve the direction and volume of power release.
The internal ﬁeld environment is usually evaluated by the segment model, and
much more accurate results could be evaluated by the whole-body model. The
evaluated results can be used to control the Radiated Emission (RE), Radiated
Susceptibility (RS) limits to make sure that the equipment function properly without
interference in fairing.
5.3.3
Analysis of Electromagnetic Radiation Field Intensity
During Spacecraft Rendezvous and Docking
During the rendezvous and docking of spacecraft, the RF devices such as microwave
ranging radar, telemetry, and data transmission on each spacecraft are in the working
state, and it is necessary to analyze the EMC between spacecraft under this condi-
tions. Figures 5.13 and 5.14 shows a schematic diagram of SZ and TG spacecraft
rendezvous and docking.
Most of the RF devices of Shenzhou spacecraft and Tiangong laboratory work
in the S band, with the space distance between 1 and 140 m during rendezvous
and docking. As two spacecrafts approach each other in space, RF signals from one
spacecraft radiate to another. It is necessary to analyze whether the spacecraft will
be disturbed or damaged in this external electromagnetic environment, for example,
whether the attitude control sensor will be disturbed and out of control. According to
Fig. 5.13 Schematic diagram of SZ and TG spacecraft rendezvous and docking


5.3 Inter-system EMC Analysis
107
Fig. 5.14 Schematic diagram of rendezvous and docking states
the analysis and calculation of RF parameters and distance, the ﬁeld strength in the
main beam of the spacecraft is about 20 V/m, and that of the side lobe is about 5 V/m,
which can be used as the basis for the veriﬁcation of radiated susceptibility between
spacecraft systems. In the development of spacecraft, the corresponding radiation
sensitivity test is carried out for the critical equipment and systems.
5.3.4
Analysis of Spacecraft Multipath Effect
The signal that the electromagnetic signal of the spacecraft reaches the ground station
receiver directly after launch, or the electromagnetic signal that the ground station
directly sends to the spacecraft receiver is a direct signal. However, due to a relatively
large number of payloads on the external of the spacecraft in a limited space, the
actual electromagnetic signal will be reﬂected by other structures on the spacecraft
before reaching the receiver. The reﬂected signals to the receiver are called multipath
signals. Due to the existence of multipath signals, the direct signals will be interfered,
so that the performance of the receiver will be degraded and the observed value will
deviate from the true value and the phenomenon of the so-called multipath error
is the multipath effect. The inﬂuence of multipath effect on the expected signal
amplitude and phase may lead to the phase shift of the input signal of the receiver
code tracking loop and carrier tracking loop and affect the signal acquisition and
tracking performance. In more serious cases, it may cause the receiver to lose lock and
work improperly. This multipath effect has a great impact on the range measurement
systems of the spacecraft, such as the navigation system and the TT&C system.
Taking the receiver of incoherent DLL type as an example, if the incoherent Dot
Product (DP) phase discrimination method is adopted, the solution expression of
multipath error is
E(δ, τ) =

R

t −d
2

−R

τ + d
2

R(τ)
+ α2

R

τ −δ −d
2

−R

τ −δ + d
2



108
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
× R(τ −δ) + α

R

τ −d
2

−R

τ + d
2

R(τ −δ) cos ϕm
+ α

R

τ −δ −d
2

−R

τ −δ + d
2

R(τ) cos ϕm,
(5.3.7)
where τ is the delay between local signal and direct signal; R(τ) is the autocorrelation
function of pseudo-random code sequence; d is the interval between the leading
correlator and the lagging correlator; δ is the delay between multipath signal and
direct signal; α is the amplitude ratio between multipath signal and direct signal (i.e.,
reﬂection coefﬁcient); ϕm is the relative phase between multipath signal and direct
signal.
After taking the correlator interval d, set the Eq. (5.3.8) to zero, that is, the relation
between δ and τ is obtained. The multipath error curve can be obtained by further
solving the relation. When solving the speciﬁc multipath error, we usually set cos ϕm
= 1 and −1, respectively, so as to obtain the two multipath error envelopes in the
worst-case. Therefore, the solved multipath error actually refers to the multipath
error envelope.
When analyzing the inﬂuence of the multipath effect on the receiver, for a speciﬁc
receiver, the receiver parameters are known. What needs to be known is the two
parameters of amplitude attenuation and time delay of the multipath signal gener-
ated by the spacecraft structure relative to the direct signal. Given the complexity
of the spacecraft structure, in order to obtain the amplitude attenuation and time
delay result through relatively accurate analysis, it is suggested to use the full-wave
analysis method in the electromagnetic simulation commercial software to analyze
the electromagnetic ﬁeld. The analysis process is as follows:
(1) In the simulation software, the antenna model with satellite and the model
without satellite are separately imported. Set plane wave excitation, the signal
form is frequency-domain signal. Calculate the receiving signal in the receiving
band of the target antenna. The analysis frequency band can extend a certain
frequency band on the basis of the receiving frequency band.
(2) Export the antenna receiving the signal for data analysis, for example, it can be
analyzed in Matlab software. The signal received by antenna without satellite is
direct wave signal, and the signal received by antenna with satellite minus the
signal received by antenna without satellite is multipath signal.
(3) In order to suppress the inﬂuence of side lobe, window function is added in the
multipath signal and direct wave signal analysis.
(4) Perform IFFT transformation on multipath signal and direct wave signal, and
transform the frequency-domain signal form of multipath signal and direct wave
signal into time-domain signal form.
(5) Compare multipath signals and direct wave signals in the same reference frame,
and obtain amplitude attenuation and time delay of multipath signals relative to
direct wave signals.
In some cases, in the analysis of the impact of the multipath effect on spacecraft, it
is expected to locate the source of the multipath signal, that is, positioning the speciﬁc


5.3 Inter-system EMC Analysis
109
Direct
wave signal
Multipath
signal
Incident plane wave
Antenna
Direct wave 
signal
Multipath
signal
Observation point
Antenna
(a) Method 1                  (b) Method 2 
Fig. 5.15 Multipath effect positioning diagram
location of the multipath effect, for the purpose of multipath interference treatment
and guidance test. Interference caused by the multipath effect can be divided into two
types. The ﬁrst is the scattering multipath, which is the sum of many delayed signals,
and there is no deterministic reﬂector. It can be simulated as the noise channel of
enveloping Rayleigh distribution. The second is the mirror multipath, which has a
deterministicreﬂectorandcanbesimulatedasoneorseveralpseudo-codemodulation
delay signal. In general analysis, mirror multipath action is considered.
As the multipath signal generated by mirror reﬂection has a strong inﬂuence, the
analysis of multipath effect can be carried out by geometrical optics or physical
optics. There are two analysis methods for multipath positioning:
Method 1: it can be assumed that the incident plane wave will have a specular
reﬂection on the spacecraft system, and the reﬂected wave will enter into the platform
or the load antenna to cause multipath effect. The schematic diagram is shown in
Fig. 5.15a.
Method 2: taking the platform or the load antenna as the transmitting source, set
the observation point and analyze the multipath effect of the electromagnetic wave
emitted by the antenna entering the observation point through the mirror reﬂection
on the spacecraft system. The schematic diagram is shown in Fig. 5.15b.
The above two methods are equivalent to each other according to the electro-
magnetic ﬁeld. The only difference is if multipath effects in multiple locations are
to be analyzed, method 1 requires multiple planar wave excitation and method
2 requires multiple observation points. Due to the complexity of the spacecraft
structure, asymptotic solvers of CST or XGTD software can be used for analysis.
During the rendezvous and docking experiments between “Shenzhou” (SZ) space-
craft and “Tiangong” (TG) space laboratory, it is found that the ranging signals
between the microwave ranging radar on SZ spacecraft and the transponder on TG
spacecraft will affect the measurement accuracy due to the multipath effect on the
cabin surface. By analyzing the inﬂuence on the interference path, the position of the


110
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.16 Interference paths on junction surface
multipath effect is determined. Finally, the problem is solved by adjusting the equip-
ment installation position to eliminate the reﬂection path and reducing the reﬂection
signal intensity, thus improving the signal-to-noise ratio (Figs. 5.16 and 5.17).
5.3.5
Polarization Isolation Analysis of GEO Spacecraft
in Near Orbit
Since the ﬁrst artiﬁcial satellite was put into use, with the increasing demand for
satellite applications in various countries, the number of satellites, such as satellites
for navigation, communications, remote sensing, relay, and scientiﬁc exploration
launched in the past decades have reached nearly a thousand. At present, the number
of on-orbit GEO satellites is about 400, which shows a more rapid development trend
with the increasing demand for various satellite applications. However, The geosta-
tionary orbit space is more and more “crowded”. As a scarce strategic resource,
the corresponding radio frequency orbit (especially geostationary orbit) resources
necessary for the development of space business systems have become an important
factor in the development of space business ﬁelds in various countries and industries.
There are many disputes among countries about the frequency and orbital coordi-
nation of satellite communication systems. For example, in early July 2010, the
PALAPA PAC-C146E satellite of Indonesia had an interaction with the COMPASS
system CHINASAT-35C satellite, which seriously affected the normal operation of


5.3 Inter-system EMC Analysis
111
Fig. 5.17 Transponder is affected by multipath
the system. With the increasing lack of frequency orbit resources, the frequency
sharing between GEO satellite systems becomes more and more complex.
Taking the linear polarization as an example, the polarization identiﬁcation Yd of
the downlink was analyzed. In the analysis process, the co-polarization waves from
the interference satellite were taken into account and received by the ground station
(co-polarization direction A//(ϕ) and cross polarization direction A//(ϕ)). The cross
polarization wave from the interfering satellite was also taken into account when it
was received by the ground station in the co-polarization direction map. However,
the additional isolation from cross polarization to cross polarization can be ignored
Yd = −10 lg

cos2 β + sin2 φ · 10−Dp(ϕb)

10 + sin2 β · 10−Dpsat

10
dB,
(5.3.8)
where ϕb is the ground station center isolation between satellites; Dp(ϕb) is the polar
decoupling of the expected ground station; Dp(ϕb) = A//(ϕb) −A+(ϕb) (dB), and
Dpsat is the polar decoupling of the interference satellite covering the area at the
desired ground station location (dB).
In the uplink case, for the receiving antenna of the desired satellite, the polarization
of the relative interference wave is identiﬁed as
Yu = −10 lg

cos2 β + sin2 β · 10−Dp(ψb)

10 + sin2 β · 10−Dpst

10
dB,
(5.3.9)
where ψb is the angle between the main radiation direction and the radiation direction
of the ground station; Dp(ψb) is the expected polar decoupling of the satellite;


112
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Dp(ψb) = S//(ψb) −S+(ψb) (dB); S// and S+ are the expected direction pattern
of the same polarization and cross polarization of the satellite antenna, respectively,
and Dpst is the polar decoupling of the disturbance ground station (dB).
If the interference wave is linear polarization (linear polarization can be derived
from two circular polarization vectors, namely, left circular polarization and right
circular polarization), the polarization received by the circular polarization expected
receiving antenna is identiﬁed as
Y = −10 lg 1
2

1 + 10−Dp(ϕ)

10
dB,
(5.3.10)
where Dp(ϕ) is the polarization decoupling of receiving antenna (dB).
Similarly, if the interference wave is linear polarization (the circular polarization
vector can be obtained by two orthogonal linear polarization vectors), the polarization
received by the linear polarization expected receiving antenna is identiﬁed by the
same formula.
In the above analysis, it is necessary to calculate the relative orientation angle β.
β is calculated as
β = |ε1 −ε2| + δ,
(5.3.11)
where ε1 and ε2 represent the polarization angle of expectation and interference
signals, respectively; and δ is the error.
5.4
EMC Limitation Analysis
In the process of designing the EMC speciﬁcation and technical requirements of
spacecraft, a crucial step is to analyze and determine the limits of the EMC test,
which is the basis for evaluating the EMC of spacecraft.
The analysis of the limits of the EMC test of spacecraft includes the following
steps:
(1) Determine the criteria. The determination of the EMC test limit value of the
spacecraft shall ﬁrst specify the criteria on which the criteria are based. For
example, AIAA-S-121A of system-level, MIL-STD-461G of subsystem-level
and equipment level, ECSS-E-ST-20-07C of imported European aerospace
products, etc. According to the standard requirements, the basis of the test
project and the project limit is deﬁned.
(2) Determine external electromagnetic environment requirements such as require-
ments for launch vehicle and launch site. Spacecraft in the launch process should
meet the external electromagnetic environment requirements of the launch
vehicle and launch site. Therefore, the spacecraft should be based on the launch
manual or ICD documents to clarify the external electromagnetic environment


5.4 EMC Limitation Analysis
113
on the spacecraft EMC requirements. The limits of EMC tests for spacecraft
shall be tailored to the requirements of the launch vehicle and the launch site
on the basis of the standard requirements.
(3) Determine the inherited requirements. If the spacecraft is the equipment type,
the limits of the spacecraft should be tailored on the basis of the limits of the
inherited spacecraft, as well as electromagnetic interference problems, found
in the development of the inherited spacecraft and the on-orbit phase. In other
words, the experience of the inherited spacecraft in the limited design should
be considered.
(4) Analyze the EMC of the current spacecraft. For the current model of elec-
tromagnetic characteristics, necessary systematic electromagnetic analysis is
carried out to determine the electromagnetic characteristics of the current space-
craft from the perspective of radiation and conduction. On this basis, the EMC
characteristics are reﬂected in the limit design.
(5) Analysis of electromagnetic radiation hazards. According to the characteristics
of the current spacecrafts, electromagnetic radiation hazards are analyzed. For
manned spacecraft, the radiation hazards effect of electromagnetic radiation
on human personnel are required to be considered. On this basis, the limits
determined in the previous step are tailored to ensure that the proper control of
electromagnetic radiation hazards in the lifetime of the spacecraft.
5.5
RF Compatibility Analysis for Spacecraft
5.5.1
RF Compatibility Analysis Type for Spacecraft
At present, the transmission of information between spacecraft and ground station
or inter-spacecraft is mainly based on the RF system. Therefore, spacecraft usually
have a relatively large number of RF systems and antennas, especially for satel-
lites with microwave loads, such as communications satellites, navigation satellites
and microwave remote sensing satellites, and their RF systems and antennas are
very complex. Such large numbers of RF devices, which range from high-powered
transmitters to highly sensitive receivers are deployed on a relatively small platform
of the spacecraft and may work with several frequency bands. Therefore, radiofre-
quency compatibility is an important issue for spacecraft, especially for microwave
payloads. The corresponding RF compatibility analysis is also the key process in the
EMC analysis of spacecraft.
The analysis of spacecraft RF compatibility generally includes two steps. One is
the analysis of spacecraft RF equipment coupling through the antenna, the other is
the analysis of the coupling between the RF device and other devices.


114
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
5.5.2
Analysis Method of Spacecraft RF Equipment
Intercoupling
The coupling analysis of spacecraft RF equipment is mainly to analyze whether the
RF equipment will cause interference to the RF receivers after the EMI radiated by
the transmitting antenna being received by the receiving antenna.
The coupling analysis of spacecraft RF equipment includes three steps. First,
the RF transceivers that need to be analyzed are identiﬁed by frequency analysis.
Then, the isolation between the corresponding transmitting and receiving antennas
is analyzed. Finally, the interference margin between the corresponding RF devices is
analyzed. Frequency analysis method is the same as Spectrum compatibility analysis
method described in Sect. 4.5. This paper mainly introduces the method of isolation
analysis between antennas and the method of interference margin analysis between
RF transceivers.
Isolation between spacecraft antennas refers to the attenuation consumed by RF
signals propagating from the transmitting antenna port to the receiving antenna port.
Antenna isolation indicates of electromagnetic coupling degree between transmit-
ting antenna and receiving antenna. The higher the spatial isolation, the lower the
coupling, and vice versa. In the process analysis, the spacecraft’s antenna structure
should be based on speciﬁc types and its working frequency, antenna size, as well
as the spacecraft overall to provide the EMC analysis personnel the input conditions
and parameters, such as complete structure model of antenna, the antenna far-ﬁeld
pattern or near-ﬁeld six radiating surface equivalent data, for selecting the appropriate
space isolation degree analysis method. With the mature developed and well applied
commercial electromagnetic simulation analysis software, the simulation analysis
of antenna isolation can guarantee relatively high accuracy and good visualization
effect. Therefore, this section mainly introduces the method of antenna isolation
analysis using commercial electromagnetic simulation analysis software. Antenna
isolation analysis has three main methods: S-parameter method, far-ﬁeld equivalent
excitation source method, and near-ﬁeld equivalent excitation source method.
5.5.2.1
S-Parameter Method
S-parameter method is actually a full-wave numerical calculation method, which
is generally applicable to the analysis of small size structures. At the same time,
the calculation area is truncated or simpliﬁed to meet the calculation requirements.
According to the engineering experience, the general intercept area should include
the area between the antennas and the ﬁve wavelength range near each antenna.
The main steps to analyze antenna isolation by S-parameter method are as follows:
(1) Set the transmitting antenna and receiving antenna excitation source port;
(2) Calculate S-parameters between two ports;
(3) Convert the spatial isolation result according to the calculation formula of S-
parameters.


5.5 RF Compatibility Analysis for Spacecraft
115
5.5.2.2
Far-Field Equivalent Excitation Source Method
For the antenna with large size (larger than ten wavelengths), it is difﬁcult to adopt
the full-wave numerical calculation method for the spacecraft or the whole antenna.
Therefore, the method of far-ﬁeld equivalent excitation source can be adopted for
analyzing, which is mainly used to simulate the spacecraft antenna through methods
such as moment method and ﬁnite element method, and then the calculated far-
ﬁeld results are converted based on the corresponding format, which serves as the
equivalent point feed source of the antenna. The distance between the antenna and
the surrounding simulation structure is required to meet the condition of the far-ﬁeld
(greater than the ratio of the diameter square to the wavelength).
After obtaining the antenna far-ﬁeld equivalent feed source model, the model is
substituted into the spacecraft model for simulation analysis. The position of the
far-ﬁeld equivalent feed source should be set according to the phase center of the
spacecraft antenna and the high frequency calculation method (e.g., physical optics
method and consistent geometric diffraction theory) can be used to calculate the
isolation between the spacecraft and the antenna. The main steps using this method
to calculate isolation are:
(1) Calculate the required far-ﬁeld pattern of each feed antenna;
(2) The feed source ﬁle is imported into the complete calculation structure, and
the far-ﬁeld feed source ﬁle is used as the secondary excitation and the whole
simulation calculation is conducted;
(3) Import the far-ﬁeld pattern of the receiving antenna, and set the far-ﬁeld equiv-
alent point source of the receiving antenna relative to the spacecraft according
to the antenna phase center;
(4) Check the calculation results and calculate the isolation with receiving and
transmitting power.
5.5.2.3
Near-Field Equivalent Excitation Source Method
For the antenna with large size (e.g., larger than ten wavelength), such as the reﬂector
antenna, when the antenna’s phase-centered position cannot be determined and the
electromagnetic calculation does not meet the condition of the far-ﬁeld, the far-ﬁeld
feed source cannot be used to calculate the isolation degree. In this case, the near-ﬁeld
equivalent source method can be used to analyze and calculate the isolation degree
between spacecraft antennas.
The near-ﬁeld equivalent source method is mainly based on an equivalent prin-
ciple, that is, the ﬁeld source and the scattering body are removed in a given volume,
and then the original ﬁeld source is equivalent to the electromagnetic ﬂow on the
equivalent closed surface. The ﬁeld distribution on the surface is consistent with the
original ﬁeld distribution, while the ﬁeld distribution in the inner region is zero. A
fully enclosed surface can be replaced by six apertures. The equivalent source of the
surface can be determined by reading the electromagnetic ﬁeld distribution of each
surface. The current on the closed surface is calculated according to Eq. (5.5.1),


116
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
	 ⃗JS = ˆn × ⃗H
⃗M = −ˆn × ⃗E ,
(5.5.1)
where ⃗JS is the equivalent surface current of the closed surface; ⃗M is the equivalent
surface magnetic ﬂow on the closed surface; ⃗H is the magnetic ﬁeld strength of the
closed surface; ⃗E is the magnetic ﬁeld strength of the closed surface; ˆn is the normal
direction of the closed surface.
The main steps of calculating isolation using the equivalent source method are as
follows:
(1) Calculate the near-ﬁeld cross-section ﬁeld of the equivalent antenna, and
generate the electric ﬁeld equivalent source and magnetic ﬁeld equivalent
source;
(2) The feed source ﬁle is imported into the complete calculation structure, then
the near-ﬁeld feed source ﬁle is used as the secondary excitation and used for
overall simulation calculation;
(3) Check calculation results and calculate isolation using the receiving and
transmitting power.
Noted that the current near-ﬁeld equivalence is only applicable to the emitter. For
the calculation of the isolation degree between two antennas, only one antenna can
be considered as near-ﬁeld equivalent, while the other can be considered as far-ﬁeld
equivalent excitation source or structural model.
After analyzing the isolation degree between antennas, the transmission power,
attenuation, and loss are quantiﬁed one by one. Compared with the sensitivity require-
ment of the RF receiver, the EMI margin of the RF receiver can be obtained, and the
conclusion of RF compatibility analysis can be given.
The effective power of the RF emission device at the RF receiver is calculated
according to formula (5.5.2),
PA( f, t, d, p) = PT ( f, t) + CT R( f, t, d, p),
(5.5.2)
where PA( f, t, d, p) is the effective power at the RF receiver; PT( f, t) is the power
of RF emission equipment; CTR( f, t, d, p) is the coupling degree between RF
transmitter and receiver; f is the frequency; t is time; d is the distance; p is power.
The EMI margin of RF emission equipment to RF receiver can be calculated by
the formula (5.5.3).
SM( f, t, d, p) = PR( f, t) −PA( f, t, d, p),
(5.5.3)
where SM( f, t, d, p) is the interference margin; PR( f, t) is the sensitivity of the RF
receiver.
If the calculated result of the interference margin is greater than 0, the EMC
requirements are met. If the calculation result is less than 0, the EMC requirements
are not satisﬁed. Otherwise, the RF system is in the critical state of EMC.


5.5 RF Compatibility Analysis for Spacecraft
117
Taking the example of analyzing the indication of interference in the RF receiving
band, PR is sensitivity. If the expressions of PA and PR are expanded and the
transceiver frequency has an interval of f , the interference margin is calculated
according to the formula (5.5.4),
SM( f, t, d, p) = PR( fR) −[PT( fE) −Lt1 −Lt2 −Ltr −Lr1 −Lr2],
(5.5.4)
where PR( fR) is the sensitivity threshold of the receiver in response to frequency
fE; uc =

N
i=1
c2
i u2
i is the transmitted power at the emission frequency fE; Lt1 is the
attenuation value of the calculated emission spectrum relative to the main spectrum;
Lt2 is the feed line loss of the transmitting system, including the mismatch loss of
non-designed frequency; Ltr is the spatial isolation between the transmitting and
receiving antennas; Lr1 is feeder loss between the antenna of the receiver and the
input port of the receiver, including mismatch loss of non-designed frequency; Lr2
is the attenuation value of the calculated receiving frequency relative to the normal
signal receiving band.
Formula (5.5.4) is the analysis equation of EMC residual between spacecraft RF
equipment, where Lt1, Lt2, Lr1, and Lr2 can be quantiﬁed according to the indicators
or behavioral level analysis proposed in the design scheme, and Ltr can be quantiﬁed
according to the spatial isolation analysis method described above.
For the analysis of the formula (5.5.4), the measured data of the EMC of the
equipment can also be used. The measured data of the EMC of the equipment mainly
includes the transmission emission data outside the transmitter band provided by
CE106, and the attenuation value of the emission spectrum relative to the main
spectrum can be obtained.
When the measured data of CE106 is available, the EMC safety margin can be
calculated by the formula (5.5.5),
SM( f, t, d, p) = PR( fR) −[P( fE) −LCE1 −Lt2 −Ltr −Lr1 −Lr2],
(5.5.5)
where LCE1 is the attenuation outside the frequency band of the transmitter obtained
from the measured results of CE106.
5.5.3
Method of Coupling Analysis Between Spacecraft RF
Equipment and Other Equipment
Coupling analysis between spacecraft RF equipment and other equipment aims to
determine whether the EMI caused by the coupling of RF equipment through the
antenna and other equipment will occur, which can be divided into two categories:
one is RF compatibility analysis of RF emission equipment and other equipment,
the other is RF compatibility analysis of RF receiver and other equipment. The


118
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
RF compatibility analysis of the RF emission equipment and other equipment is to
analyze the electric ﬁeld generated by the internal and external transmitting power
of the RF emission equipment through the antenna at the spacecraft equipment, and
to analyze whether the electric ﬁeld intensity is beyond the scope of the radiation
sensitivity requirements of other equipment. The next step is to calculate the in-
band and out-band emission power required to enable the RF emission equipment
to generate the required interference electric ﬁeld at other equipment through the
antenna, and to analyze whether the power is within the limit range of the transmitting
equipment. The RF compatibility analysis of RF receiver and other equipment is to
analyze the EMI generated by other equipment through the coupling of receiving
antenna, coupling the received in-band and out-of-band power at the RF port, and
to analyze whether the power is within the limit range of the receiver. In order to
meet the EMC of RF receiver, the in-band and out-of-band EMI requirements should
be satisﬁed at the receiving antenna interface, and the radiation emission control
requirements of other equipment should be analyzed.
5.5.3.1
Analysis of RF Emission Effect Between the Equipment
For analyzing the EMC between RF emission equipment and other equipment, the
internal and external emission characteristics of RF emission equipment should be
determined ﬁrst. The internal emission characteristics of RF emission equipment
include transmission frequency, bandwidth, and transmission power. Out-of-band
emission characteristics can be obtained by testing or analyzing. For analyzing the
out-of-band emission characteristics, the behavior-level simulation method can be
used. The behavior-level simulation model of the transmitter can be established with
ADS or other RF link analysis software to simulate, as well as to analyze, the various
frequency interference components and power levels generated by the transmitter.
In order to analyze the electric ﬁeld intensity generated by RF emission equipment
at the relevant position of the spacecraft through antenna, in addition to the far-
ﬁeld equivalent source method and near-ﬁeld equivalent method mentioned in the
previous section, the far-ﬁeld estimation method and structural source method can
also be adopted.
The far-ﬁeld estimation method is applicable to the situation when the spacecraft
electromagnetic model and the antenna electromagnetic model are not available
while the related spacecraft RF characteristic parameters can be obtained. Note that
the remote-ﬁeld estimation method is an estimation method adopted when the input
condition is insufﬁcient. The advantage is that the analysis is convenient and less
input parameters are needed. The drawback is that this method neglects the effect of
spacecraft structure and external parts on antenna radiation characteristics. Moreover,
the analytical error of this method is of great signiﬁcance.
According to the relative position between the antenna and other equipment, as
well as the antenna pattern, the ﬁeld strength of the spacecraft instrument can be
estimated.


5.5 RF Compatibility Analysis for Spacecraft
119
As far as the distance from the transmitting antenna is r, the ﬁeld strength at the
external equipment of the spacecraft in the position (θ, ϕ) of the transmitting antenna
can be calculated by the following formula
|E(θ, ϕ)| =
√60PtGt
r
F(θ, ϕ)

AT T
(5.5.6a)
or:
E =

30PtG
′
t
r

AT T ,
(5.5.6b)
where |E(θ, ϕ)| is the peak electric ﬁeld intensity at the external equipment of the
spacecraft, in V/m; E is the effective value of electric ﬁeld strength at the external
device of the spacecraft, in V/m; F(θ, ϕ) is the normalized directivity coefﬁcient
of the antenna in the direction of the incoming wave from the radiation electric
ﬁeld; Pt is the transmitted power, W; Gt is the main lobe gain of the transmitting
antenna; G
′
t is the gain of the transmitting antenna in the analysis direction; r is the
distance, in m; AT T is the attenuation coefﬁcient, which is 1 for the analysis of
the external environment of the spacecraft, or greater than 1 for the analysis of the
internal environment of the spacecraft, reﬂecting the shielding effectiveness of the
cabin.
Equation (5.5.6a) is applicable to the ﬁeld strength analysis when the antenna
main lobe gain and the side lobe gain relative to the main lobe gain inhibition index
are known. The result is the peak of ﬁeld strength. Multiply it by 1/
√
2 to get the
effective value of ﬁeld strength. Formula (5.5.6b) is applicable to the ﬁeld strength
analysis when the speciﬁc gain of the antenna is obtained, and the result shows the
effective value of ﬁeld strength.
The application of the structural source method is similar to that of the S-parameter
method mentioned in the previous section. Only the required analysis results can
be changed from the S-parameter to the ﬁeld strength at the concerned position.
The structural source method can completely include the effects of spacecraft struc-
ture and components on RF emission antenna radiation characteristics. The method
with the highest accuracy can include not only the effect of spacecraft structure and
components on RF emission antenna radiation pattern, but also the effect of near-
ﬁeld coupling between spacecraft structure and RF emission antenna structure. When
the electromagnetic model of spacecraft and antenna structure can be obtained and
the calculation amount is within the acceptable range, the electromagnetic model
method of antenna structure can be adopted. This method is modeled directly using
a three-dimensional structure model. The actual port excitation source is set up. The
whole model is divided into mesh to carry out the full-wave simulation analysis. The
analyzing steps of the method are as follows:
(1) The antenna element model is simulated and analyzed to verify that the
performance of the antenna element model meets the requirements;


120
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
(2) The spacecraft model is processed to meet the simulation analysis conditions;
(3) The antenna unit model is installed on the spacecraft model;
(4) The simulation is set up and conducted through the electromagnetic simulation
software, and data should be extracted after simulation.
5.5.3.2
Impact Analysis of RF Receiver
The EMC impact analysis of RF receiver can be divided into two steps. First, the
receiver is simulated by using ADS or other RF link analysis software, and the
maximum power value (RF receiver sensitivity threshold) is calculated. Then the
electromagnetic ﬁeld numerical simulation analysis software is used to analyze the
receiving antenna connected to the RF receiver, and to calculate the electric ﬁeld
intensity of the receiving antenna interface when the power of the input port of the
RF receiver reaches its sensitivity threshold.
The sensitivity index is usually given in the design of the receiver to determine the
inner and outer sensitivity of the RF receiver. If not, it can be calculated according
to the following formula
PR( f ) = −174 (dBm/Hz) + N F(dB) + 10 log B −SI (dB),
(5.5.7)
where PR( f ) denotes the sensitivity of the equivalent receiver at the analysis
frequency, in dBm; NF is noise coefﬁcient, in dB; B is the effective working band-
width of the receiver, in Hz; SI is the anti-interference performance of the receiver,
which is generally the signal to noise ratio or the signal to dry ratio, in dB; f is the
analysis frequency, in Hz.
The behavioral level simulation method can be used to calculate the sensitivity
limit out-of-band. The behavioral level simulation model of the receiving link is
established by using ADS or other RF link analysis software. By using the injection
method, the interference signal is injected into the receiving link for simulation. The
interference of the receiver is analyzed, and the power value of the interference signal
is calculated when the receiver works abnormally. The calculation of out-of-band
sensitivity threshold by behavioral level simulation method includes the following
four steps:
(1) The parameters required for the modeling of the interference source should be
determined, such as frequency, bandwidth, signal form (modulation signal or
single frequency signal), and the interference behavior-level simulation model
should be established;
(2) The parameters required by the behavioral level modeling of the disturbed
receiving system, such as operating bandwidth of the receiver, ampliﬁer, mixer,
and ﬁlter parameters, are required to be determined. A behavioral level model
of the receiving equipment is established to analyze the simulation analysis
and adjust the model parameters without interference, so that the working
performance of the receiving equipment can meet the requirements of technical
indexes.


5.5 RF Compatibility Analysis for Spacecraft
121
(3) The injection method is adopted to inject the interference signal into the system’s
behavior-level model and quantitative analysis is conducted;
(4) According to the technical requirements of the receiver, key index that may be
subject to interference are analyzed, therefore, the sensitivity threshold of the
radio frequency port band outside the receiver can be determined.
In addition to the far-ﬁeld equivalent source method, near-ﬁeld equivalent source
method, and structural source method mentioned in the previous section, the EMI
received by the receiving antenna can also be estimated by the remote-ﬁeld method.
Similarly, the remote-ﬁeld estimation method is used when the input condition is
insufﬁcient. The advantages are easy analysis and less input parameters, while the
disadvantage is the signiﬁcant analytical error. The analysis formula of the remote-
ﬁeld estimation method is as follows:
E =

4π
λ

30Pr
G
′
r

AT T
(5.5.8a)
or:
E =

Pr( f, t) · 240k2
F2(θ, ϕ) · Gr · γ · cos2 ξ

AT T
(5.5.8b)
where E is the radiation electric ﬁeld intensity, in V/m; Pr( f, t) is the sensitivity of
the receiver, in W; G
′
r is the gain of the receiving antenna in the analysis direction;
F(θ, ϕ) is the normalization direction coefﬁcient of the receiving antenna in the
direction (θ, ϕ) of the incoming wave from the radiation electric ﬁeld; Gr is the
main lobe gain of the receiving antenna; γ is the antenna port matching coefﬁcient;
cos2 ξ is the polarization matching coefﬁcient; ξ is the angle of polarization, in °; k
is wave number, in 1/m; λ is the wavelength, in m.
Formula (5.5.8a) is applicable to the ﬁeld strength analysis when the spacecraft
antenna information input is limited, and it is assumed that the interference and
antenna polarization match perfectly. If the matching characteristics of the antenna
port and the matching characteristics of interference and antenna polarization can be
obtained, Eq. (5.5.8b), can be used for ﬁeld strength analysis.
5.5.3.3
EMC Judgment
After electric ﬁeld analysis between the antenna and the equipment on the satellite
surface, the EMC between the interference resource equipment and the sensitive
equipment is determined according to the ﬁeld intensity at the sensitive equipment
end and the sensitivity threshold of the sensitive equipment according to the formula
(5.5.9),
SM = S −E,
(5.5.9)


122
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
where,S isthesensitivitythresholdofsensitiveequipment,indBμV/m;E istheinten-
sity of the interference electric ﬁeld, in dBμV/m; SM is electromagnetic interference
margin, in dB.
If SM > 0, it indicates that the EMC requirements are met between the RF device
and other devices, while if SM < 0, it indicates that the EMC requirements are not met
between the RF device and other devices, anti-EMI design (including RF spectrum
optimization and layout optimization) should be carried out between the antenna and
spacecraft external equipment. The interference signal intensity of the input port of
the receiver is reduced and the interference indication is raised to an acceptable level.
If SM = 0, the critical compatibility state between the RF device and other devices
is indicated.
An example of an RF compatibility analysis is given below. When a satellite
payload antenna is facing towards the sun sensor, the near-ﬁeld radiation interference
is large, and the radiation ﬁeld intensity is as high as 64 V/m, as shown in Fig. 5.18.
The maximum interference that the solar sensor can withstand under the interference
frequencyofthepayloadantennais40V/m.Theradiationﬁeldstrengthofthesatellite
load antenna to the solar sensor is greater than the sensitivity threshold. Therefore,
anti-EMI improvement is required.
The original coordinate position of the sun sensor is (85 mm, 3750 mm, −
880 mm). It is assumed that the position range of the sun sensor is (−15 mm <
x < 890 mm, 3000 mm < y < 3850 mm, −900 mm), as shown in the blue area in
Fig. 5.19.
Fig. 5.18 The load antenna radiation electric ﬁeld intensity near the sun sensor


5.5 RF Compatibility Analysis for Spacecraft
123
Fig. 5.19 The position range of the sun sensor
The emission antenna radiation around the star is analyzed using the analysis
method mentioned in this section. FEKO software is used to simulate and calculate
the electric ﬁeld radiation intensity of the payload transmitting antenna within the
layout range. The results are shown in Fig. 5.20.
According to the analysis, the sun sensor can be installed in position 2, position 3
or position 4 to reduce the inﬂuence of the load antenna on the sun sensor and meet
the compatibility requirements of the sensitive equipment.
5.6
Evaluation of Passive Intermodulation Using Full-Wave
Frequency-Domain Method with Nonlinear Circuit
Model
5.6.1
The Principle of Passive Intermodulation and Its Effect
on EMC
In multi-carrier communication environments, such as high-power measurement and
control systems, satellites, ship-borne communication systems, and terrestrial base
stations for mobile communication, since a transmit antenna can also be used as a
receive antenna, or anyway, the transmit antenna is located near the receive antenna, a
high-power transmitter and a high-sensitivity receiver in a limited space may generate
the interference sources-passive intermodulation (PIM) that must be suppressed. The


124
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Position 1
Position 2
Position 3
Position 4
Fig. 5.20 The electric ﬁeld intensity generated by the payload transmitting antenna in a position
where the sun sensor can be positioned
PIM is a phenomenon in which a new signal with a frequency different from the
carrier frequency is generated when two or more carrier signals pass through the
passive component with a nonlinear response. However, the PIM will bring about
serious consequences once it is produced. For the TT&C antenna on satellite, the
connection of the wire mesh inevitably generates a PIM phenomenon, resulting in
an increase of noise level, a decrease in the sensitivity of the receiver, and even the
entire communication system cannot work properly. For example, in the 1970s, the
3rd order PIM of communication satellite FLTSATCOM (US Fleet Communications
Satellite), the 13th order PIM of MAR1SAR (US Maritime Satellite), the 43th order
PIM of MARECS (European Maritime Satellite) and the 27th order PIM of IS-V
(International communication satellite number V) fell into the receiving passbands,
which caused interference and once affected the development progress and applica-
tion of some satellite systems. Most of the nonlinear devices, including waveguide
connectors, duplexers, ﬁlters, directional couplers, attenuators, splitters, combiners,
etc., may generate the intermodulation distortion. As the PIM distortion products
fall into the receiving band of the high-sensitivity receiver, it will directly affect the
capacity and quality of the communication system. The PIM has become a major
bottleneck and difﬁculty restricting the application of high-power, high-sensitivity
microwave communication, and TT&C systems.


5.6 Evaluation of Passive Intermodulation …
125
The generation mechanism of PIM is extremely complex, resulting in that PIM
products typically exhibit certain randomness. Therefore, in the case that the theo-
retical model is not mature enough, the most direct and effective way to solve the
PIM problem in the actual project is to measure the PIM products by experiment,
so as to check whether the PIM performance of the microwave device or system
is in compliance with the requirements. In addition, it is indispensable that a large
amount of test data as the ﬁrst-hand information for theoretical research to require
more accurate knowledge of the exact PIM mechanism. Therefore, in the early days
of PIM research, the work on the PIM test occupied a very important position. In
general, PIM tests can be divided into two categories according to their purpose:
the ﬁrst type is an inspection test, the purpose of which is to measure whether the
PIM index of the device or system under test meets the design requirements; the
second type is the positioning test, aiming at ﬁnding the exact location of the PIM
in a complex device or system to provide guidance for suppressing PIM.
Only by understanding the exact mechanism of PIM, it is more likely to control the
PIM level of the device or even the system through proper design, material selection,
processing technology, and other means in the actual project. Many years of research
have shown that the interaction of the electromagnetic ﬁeld with nonlinear junctions
and nonlinear materials in passive devices is the source of intermodulation. This
nonlinear response characteristic can be basically divided into two categories: mate-
rial nonlinearity and contact nonlinearity. In comparison, a lot of research has been
done on the PIM problem caused by material nonlinearity, but the exact mechanism
of PIM for contact nonlinearity is still uncertain until now, especially the nonlinear
contact problem of metal-metal junctions.
The junction is an important form of generating microwave signal. The interface
of substances with different nature will form a “junction”. For example, a PN junc-
tion is formed between a P-type semiconductor and an N-type semiconductor. The
semiconductors on both sides of the interface have different energy levels, so the
carriers (electrons and holes) generate a ﬂow, and the electron ﬂows from the region
N with a high energy level to the region P with a low energy level. Moreover, the
hole ﬂows from the region P to the region N until equilibrium, thus forming a space
charge region where positive and negative charges are accumulated on both sides of
the interface, this is the so-called “junction”. In order to achieve balance, the band
variation in the space charge region is curved, and there is a change in the potential
energy. The motion of the charge in it needs to overcome the potential energy, which
is called the barrier. Because of the existence of the barrier, the voltage and current
on the PN junction show a nonlinear relationship.
Similarly, a metal-semiconductor junction, also known as a Schottky junction,
can be formed between the metal and the semiconducting body. The PN junction
diode, the microwave oscillator made by the triode, and the ampliﬁer are important
components for electromagnetic signal generation and ampliﬁcation. The mixer of
the Schottky junction is the components to achieve the frequency relocation of the
electromagnetic signal (i.e., the generation of electromagnetic signals at the mixing
frequency).


126
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.21 The schematic
diagram of the energy level
on the MIM junction
Among the many metal-semiconductor junctions, also known as a Schottky junc-
tion, can be formed between the metal and the metals. The metal in the air is inevitably
oxidized, so the metal-metal junction is actually a metal-insulator-metal (MIM) junc-
tion. As shown in Fig. 5.21, the energy levels in the metal and oxidized insulators
in the MIM junction differ, and they also have volt-ampere nonlinear properties
that produce electromagnetic signals. When two or more electromagnetic waves
are incident on the MIM junction in the electromagnetic structure, the nonlinear
characteristics of the MIM junction will cause an alternating modulation effect on
the electromagnetic waves at multiple frequencies like the Schottky junction in the
microwave circuit. Electromagnetic signals are generated at multiple frequencies and
this phenomenon is known as intermodulation.
In the complicated engineering structure, the connection of the metal is inevitable,
so the MIM is widely distributed in the actual electromagnetic engineering struc-
ture, and the PIM becomes a universal phenomenon in the actual electromagnetic
engineering. Since the PIM is caused by nonlinear characteristics, not only the MIM
junction, but also the nonlinearity of the metal material itself will generate PIM. With
the development of engineering technology, metals containing nonlinear properties
(such as ferromagnetic materials) have been rarely used in electromagnetic engi-
neering. Therefore, the MIM junction has become a main factor for the generation
of PIM in the actual project.


5.6 Evaluation of Passive Intermodulation …
127
Fig. 5.22 Schematic diagram of the spectrum of intermodulation products
As with the active intermodulation generated by the nonlinearity of the microwave
ampliﬁer, PIM products of electromagnetic signals with two or more frequencies
(herein referred to as a carrier or fundamental wave in communication engineering)
in the communication system may fall in its own receiver band or in the adjacent
receiver band, as shown in Fig. 5.22. It can be seen that the frequency of the odd order
intermodulation products generated by the two carriers is very close to the funda-
mental waves itself, which will degrade the receiving performance of the receiver
and interfere with the normal operation of the communication system.
The strength of intermodulation products is expressed in dBc (or dB), which is
the difference between the level of each order PIM product and the decibel of the
carrier. If the PIM is caused by the nonlinearity of the MIM junction, the level of
the third-order PIM is often on the magnitude order of 100 dB or less, but in the
case of high-power transmission and high-sensitivity receiving, the effect is still not
negligible. So, it is necessary to analyze and design the PIM of the electromagnetic
system.
5.6.2
Analysis Method of PIM
The accelerated movement of electrons or the kinetic electrons in the medium can
radiate electromagnetic waves. In terms of the time domain, the characteristics
of current or medium often have time-varying characteristics. For the frequency-
domain, the generation of electromagnetic waves means the relocation of energy in
thefrequency-domain,i.e.,thenonlinearityleadstothegenerationofelectromagnetic
waves. When the electromagnetic behavior generated by an electromagnetic wave
is analyzed, a time-varying nonlinear excitation source or a time-varying medium
or nonlinear boundary condition can be added to the Time-domain Maxwell equa-
tions to perform Fourier transform on the generated electromagnetic ﬁeld to obtain


128
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
its frequency characteristics. However, many simulation software of Time domain
cannot directly calculate the time-varying boundary conditions, which affects the
solution of the multi-physics ﬁeld problem of time-varying boundary conditions.
When the nonlinear source or the boundary condition is weak and the area of its
operation is large, the error accumulation of the time-domain iteration also affects
the accuracy of its solution. Although the method of weighted residuals based on the
frequency-domain equations, such as ﬁnite element (FEM) and method of moments
(MoM), are very important in the electromagnetic analysis and design because of
their accuracy, the frequency-domain Maxwell’s equations cannot be directly applied
to this type of nonlinear problem. Therefore, the effective analysis of this type of
multi-physical ﬁeld electromagnetism problem caused by electromagnetic waves is
an important task in practical electromagnetic engineering.
As can be seen from the detailed analysis of the contradiction in the existing
analysis methods:
(1) The frequency-domain Maxwell’s equations cannot be directly applied to
this type of electromagnetic problem because it can only be solved at single
frequency, and the essence of electromagnetic waves is the relocation of elec-
tromagnetic waves in the frequency domain, so the nonlinear sources describing
this relocation or the boundary conditions and media cannot be fully integrated
into the frequency-domain form. However, the component of the frequency to be
analyzed or the equivalent effect can be added to the equations as an excitation
source.
(2) Althoughthetime-varyingboundaryconditioncannotbedirectlysolvedinmany
existing time-domain numerical methods, the time-varying excitation source is
the most common setting in the time-domain numerical algorithm. Therefore,
the variation of the electromagnetic ﬁeld affected by the time-varying boundary
conditions is added as a time-varying excitation source to the time-domain
Maxwell’s equations, and then the time-domain numerical method can be solved
smoothly.
5.6.3
Analysis of PIM Using Full-Wave Frequency-Domain
Method with Nonlinear Circuit Model
The nonlinear source which can generate the electromagnetic wave is the core to
analyze the multi-physical ﬁeld problem. In engineering, its characteristics often
have the locality in the space and regular variability in the time domain. The analysis
method of a time-varying nonlinear circuit similar to these features has been very
mature. Therefore, in order to accurately analyze the multi-physical ﬁeld problem
caused by electromagnetic waves, the analysis method of “Full-Wave Frequency-
Domain Method with Nonlinear Circuit Model” is proposed.
The “Full-Wave Frequency-Domain Method with Nonlinear Circuit Model”
method means that the nonlinear source generating electromagnetic wave is equiva-
lent to the nonlinear circuit when analyzing the multi-physical ﬁeld problem caused


5.6 Evaluation of Passive Intermodulation …
129
(a) wire mesh model;
 (b) metal junction model 
Fig. 5.23 Simulation model
by electromagnetic waves, and the input and output of the circuit are related to the
excitation in the electromagnetic wave analysis method (i.e., the Maxwell’s equa-
tions). Compared with the original time-domain simulation method, in the “Full-
Wave Frequency-Domain Method with Nonlinear Circuit Model” method, the anal-
ysis of the whole problem can be divided into several relatively independent steps.
The electromagnetic ﬁeld and the circuit calculation is, respectively, performed.
Although the analysis steps are added, each step is simpler and its error is controlled
in an independent calculation method, so that the accuracy of the overall simulation
can be improved.
It can be seen from Fig. 5.23 that there exists the conversion of electromagnetic
energy at several PIM frequencies in the whole PIM process, so it is obvious that
the frequency-domain analysis technique cannot be directly used to calculate the
PIM. If the time-domain analysis technique is adopted, when the magnitude order of
PIM is below 100 dB, i.e., the power level difference between the electromagnetic
wave on the illumination frequency and the electromagnetic wave power on the PIM
frequencyisabout100dB.Theerrorofdividingthegridinthetime-domainalgorithm
is generally approximately 40 dB, in this case, it is obvious that the time-domain
algorithm is not applicable.
A metal junction on the wire mesh is selected to study. The time-domain method
and the frequency-domain method based on the “Full-Wave Frequency-Domain
Method with Nonlinear Circuit Model” is, respectively used to calculate the PIM.
Two carrier frequencies are 11 GHz and 12.6 GHz, respectively, with the same power
of 100 W. The Horn is 0.3 m from the mesh surface, the length of the metal junction
is 0.45 mm, and the reﬂection coefﬁcient of metal mesh is 0.99.
The multi-scale equivalent method is used to replace the wire mesh by the solid
material with the same reﬂection coefﬁcient to extract the surface tangential electric
ﬁeld, and then the direction of the metal junction is taken into consideration to obtain


130
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
the tangential ﬁeld component across the junction. At last, the full-wave simulation
of FEM is used to extract the tangential ﬁeld of the surface, then the tangential ﬁelds
E1 and E2 under the double carriers are integrated to obtain the voltage V 1 and V 2
of the metal junction.
V1,2 =

E1,2(x, y, z) · dl
(5.6.1)
The volt-ampere characteristics corresponding to the general barrier model is
selected, i.e., the J-V model
J = J0

ϕ exp(−Aϕ1/2) −(ϕ + eV ) exp

−A(ϕ + eV )1/2
(5.6.2)
In
Eq.
(5.6.2),
J0
=
e/2πh(βs)2,
ϕ=(ϕ1+ϕ2 −eV )

2,
A
=
(4πβs/h)(2m)1/2, β is the correction factor,
β = 1 −
1
8(ϕ)2
 s2
s1
(ϕ −ϕ)2dx
(5.6.3)
ϕ = ϕ1 + (ϕ −eV )(x/s) −1.15λs2/x(s −x)
(5.6.4)
In Eq. (5.6.4),
λ = e2 ln 2

(8πε0εrs)
s = s1 −s2.
The parameters in the model are:
m—Electronic quality;
e—Electronic charge;
h—Planck constant;
s—The thickness of the oxide layer;
s1, s2—Fermi level barrier;
ϕ1—Barrier height between the electrode interface 1 and the insulating layer;
ϕ2—Barrier height between the electrode interface 1 and the insulating layer;
ϕ—Average barrier height;
εr—Relative dielectric constant;
ε0—Dielectric constant of free space;
V—Voltage across the metal junction.
When the electrons are tunneled, if the intermetallic oxide layer is thin, the metal
will generate an image force to the electrons, causing a change dramatically in the
height and shape of the barrier; the actual barrier height will be reduced, s1 and s2
are the boundary point of the actual barrier after being affected by the image force.


5.6 Evaluation of Passive Intermodulation …
131
Furthermore, the equivalent current ﬂowing through the metal junction is shown in
Eq. (5.6.5), where W is the contact area.
I = J · W = J0 · W

ϕ exp(−Aϕ1/2) −(ϕ + eV ) exp

−A(ϕ + eV )1/2
(5.6.5)
If the time-domain calculation method is used, according to the double carrier
model, the signal irradiated onto the metal junction is:
V = V1 cos(ω1t) + V2 cos(ω2t)
(5.6.6)
Assuming that the radius r of the metal wire is 50 μm, and the contact area
approximates to πr2, the current can be calculated. Using XFDTD based on the
time-domain algorithm, the metal junction is equivalent to the basic dipole, and the
calculated current is used as the pulse excitation of the dipole. The PIM radiation ﬁeld
is simulated, and the whole spectrum result is obtained in one calculation. As shown
in Fig. 5.24 is the time domain simulation spectrum of a 0.25 * 0.25m2 wire mesh.
From the results, it can be seen that the frequency spectrum after Fourier transform is
not accurate due to the accumulated truncation error of the intermodulation products
calculated by the time domain method is close to the magnitude of PIM. Compared
with the real spectrum, the calculated frequency and amplitude have errors, and
even produce non-existent spectrum. At the same time, the spectrum does not have
approximate symmetry, which shows that the time domain method has a large error
for low PIM evaluation. Meanwhile, the calculated PIM results of a metal junction
by time-domain method are shown in Table 5.8.
It can be seen from the results that the third-order PIM calculated by the time-
domain method is higher than the received carrier power, which does not conform
Fig. 5.24 The simulated spectrum of wire mesh by time-domain method


132
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Table 5.8 PIM calculation
results of a metal junction by
time-domain method
Item
Frequency (GHz)
Power (dBm)
Carrier 1
11
−236.5
Carrier 2
12.6
−208.1
3rd order
9.4
−220.9
5th order
7.8
−238.6
7th order
6.2
−244.9
to the facts. Moreover, the frequency spectrum does not have similar symmetry,
indicating that the error of the time-domain method is rather considerable.
The question now is how to solve the problem of weak PIM analysis of MIM
junctions? The reason for this problem is that the power difference between the illu-
mination waves and the PIM products requests a very high accuracy of ﬁeld calcu-
lation. In addition, separation of the illumination wave calculation and the analysis
of the PIM products into different independent analysis problems will reduce the
requirements for ﬁeld calculation accuracy. The generation process of PIM can be
divided into three steps after carefully examining the generation process of passive
intermodulation:
(1) Electromagnetic waves of two frequencies are irradiated onto the nonlinear
MIM junctions that may lead to PIM;
(2) The equivalent radiation source at each order of PIM frequency is generated
through the nonlinear effect of two incident electromagnetic waves on the MIM
junction;
(3) The equivalent radiation source at each order of the PIM frequency forms a
second radiation in the space.
Corresponding to the above simulation, the whole simulation analysis of the PIM
can be divided into three relatively independent but interconnected tasks:
(1) Simulate the ﬁeld distribution of the incident wave in the region to be calculated,
and the focus is to calculate the electromagnetic ﬁeld distribution on the MIM
junction;
(2) The analysis should be done at the MIM junction, which requires the model of
each order PIM source generated by two incident ﬁelds;
(3) Calculate the distribution of the secondary radiation ﬁeld for each order of PIM
source and its inﬂuence on the antenna of the receiver.
It can be seen that since these three problems are relatively independent, the weak
PIM products are not calculated together with the relatively strong illumination ﬁeld,
which reduces the stringent requirements for calculation accuracy. Thus, the analysis
problem of weak PIM from MIM junction can be solved. Task (1) and (3) consist
of the tasks for calculating the electromagnetic “ﬁeld” distribution for the two illu-
mination waves and the respective PIM frequencies, which can be performed by
the frequency-domain calculation method based on the weighted residual method


5.6 Evaluation of Passive Intermodulation …
133
to improve the accuracy. Task (2) involves the calculation of nonlinear characteris-
tics, and the calculation method of the nonlinear circuit can be used to obtain the
components of each intermodulation frequency. Therefore, this method can be called
the calculation method of “Full-Wave Frequency-Domain Method with Nonlinear
Circuit Model”.
The nonlinear model of the metal junction can be expanded according to the power
series by the voltage extracted using the simulation model of metal junction above,
and ﬁnally, the expression of the intermodulation products for each order can be
obtained.
The 3rd PIM product at the frequency 2 f2 −f1 is
YP I M3 = C3
3
4V 2
1 V2

+ C5
5
4V 4
1 V2 + 15
8 C5V 2
1 V 3
2

+ C7
105
64 V 6
1 V2 + 105
16 V 4
1 V 3
2 + 195
32 V 2
1 V 5
2

+ · · ·
+ C2n+1
1
22n
n−1

i=0
(2n + 1)!
i!(i + 1)!(n −i −1)!(n −i + 1)!V 2(n−i)
1
V 2i+1
2
+ · · · .
(5.6.7)
The 3rd PIM product at the frequency 2 f2 −f1 is
YP I M3 = 3
4C3

V 2
2 V1

+ C5
5
4V 4
2 V1 + 15
8 C5V 2
2 V 3
1

+ C7
105
64 V 6
2 V1 + 105
16 V 4
2 V 3
1 + 195
32 V 2
2 V 5
1

+ · · ·
+ C2n+1
1
22n
n−1

i=0
(2n + 1)!
i!(i + 1)!(n −i −1)!(n −i + 1)!V 2(n−i)
2
V 2i+1
1
+ · · · .
(5.6.8)
The two intermodulation products near the carrier frequency are considered in
priority, i.e., the 5th PIM product at the frequency 3 f1 −2 f2 and 3 f2 −2 f1, the 5th
PIM product at the frequency 3 f2 −2 f1 is
YP I M5 = 5
8C5V 3
1 V 2
2 + C7
105
64 V 5
1 V 2
2 + 35
16V 3
1 V 4
2

+ · · ·
+ C2n+1
1
22n
n−1

i=0
(2n + 1)!
i!(i + 1)!(n −i −1)!(n −i + 1)!V 2i+1
1
V 2(n−i)
2
+ · · · .
(5.6.9)
Finally, the PIM product at any odd order frequency 2i f1 + (2 j + 1) f2 can be
given as


134
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Table 5.9 PIM calculation
resulted by full-wave
frequency-domain method
with nonlinear circuit model
method
Item
Frequency (GHz)
Power (dBm)
Carrier 1
11
−203.5
Carrier 2
12.6
−202.3
3rd order
9.4
−237.4
5th order
7.8
−255.1
7th order
6.2
−280.6
YP I M(2m+1) =
∞

n=m
C2n+1
1
22n
n−1

k=m−1
(2n + 1)!
(k −j)!(k + j + 1)!(n −k −i)!(n −k + i)!V 2(n−k)
1
V 2k+1
2
.
(5.6.10)
The metal junction is equivalent to a dipole, and the passive intermodulation
product is equivalent to a secondary radiation source. The passive intermodulation
generated in space is calculated by the electromagnetic frequency-domain method,
and ﬁnally, the interference level of different order PIM is obtained at the receiving
port.
Table 5.9 shows the calculated PIM and the carrier power resulted from the Full-
Wave Frequency-Domain Method with Nonlinear Circuit Model Method. For a metal
junction, the generated radiation ﬁeld is very weak, so the PIM and the carrier power
are relatively low, but the results are consistent with the actual situation and more
logical than the time-domain method. Since the calculation by Full-Wave Frequency-
Domain Method is adopted, the precision is rather higher.
5.7
Cable Crosstalk Analysis
The spacecraft often adopts a multiline beam arrangement. The interline coupling
between lines often leads to electromagnetic compatibility problems. In general,
the analysis of interline coupling is divided into cases of low frequency and high
frequency. In the case of low frequency, that is, the length of the line is much smaller
than the wavelength, the lumped parameter method can be used for analysis. In the
case of high frequency, when the length of the line is greater than or equal to one
quarter wavelength, the method of the lumped parameter cannot be used for analysis,
but the distributed parameter theory can be used for analysis. This section mainly
analyzes the case of high frequency coupling. On this basis, the analysis method of
low frequency coupling is obtained.
According to the theory of the electromagnetic ﬁeld, there are distributed resis-
tances and inductances in cables, as well as distributed capacitances and distributed
conductance between cables. In the case of low frequency, when the wavelength is
longer than the line length, these distributed parameters have little inﬂuence on the


5.7 Cable Crosstalk Analysis
135
transmission of voltage and current on the line. At this point, the lumped parameter
theory can be used for analysis. However, when the frequency is higher, which the
line length can be compared with the wavelength, the distributed parameters on the
line have a great inﬂuence on the current and voltage. Therefore, the distributed
parameter theory should be used for analysis.
Based on the distributed parameter theory, there are resistance Rz, inductance
Lz, conductance Gz, and capacitance Cz on any inﬁnite wire element z,
where R, L, G, and C are distributed resistance, distributed inductance, distributed
conductance, and distributed capacitance of unit length on line, respectively. They
are related to the cable shape, size, wire material, and dielectric material parameters.
TheequivalentcircuitmodelofthetransmissionlineisshowninFig.5.25.Assume
that the voltage and current at the place z are u(z) and i(z), and the voltage and
current at the place z+z are u(z + z) and i(z + z). Since The equivalent circuit
model of the transmission line is shown in Fig. 5.25. Assume that the voltage and
current at the place z are u(z) and i(z), and the voltage and current at the place
z + z are u(z + z) and i(z + z). Since z ≪λ, for the uniform transmission
line, the transmission line equation is z ≪λ, for the uniform transmission line,
the transmission line equation is

dU
dz = −Z I
dI
dz = −YU ,
(5.7.1)
where
z
Δ
z
Δ
z
z
R z
Δ
L z
Δ
G z
Δ
C z
Δ
L
Z
L
Z
g
R
g
R
g
u
g
u
i
i
i
+ Δ
u
u
u
+ Δ
Fig. 5.25 Equivalent circuit of transmission line element z


136
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
	 Z = R + jωL
Y = G + jωC ,
where U and I are, respectively, the abbreviation of complex amplitude value U(z)
and I(z).
For the no-loss transmission line, the inﬂuences of R and G can be ignored. So
the equation of no-loss uniform transmission line can be obtained as follows:

dU
dz = −jωK I
dI
dz = −jωCU .
(5.7.2)
The solution of the above equation is

U(z) = A1e−jβz + A2e jβz
I(z) =
1
Z0

A1e−jβz + A2e jβz ,
(5.7.3)
where β = ω
√
LC and Z0 =

L

C are the characteristic impedance on the no-loss
transmission line. Suppose the voltage and current at the initial port z = 0 of the
cable are U(0) = U0 and I(0) = I0, then the voltage and current at any point on the
line can be expressed as

U(z) = U0 cos βz −j Z0I0 sin βz
I(z) = I0 cos βz −j U0
Z0 sin βz
(5.7.4)
The equivalent impedance of any point is
Z(z) = Z0
Z1 −j Z0 tan βz
Z0 −j Z1 tan βz ,
(5.7.5)
where: Z1 = U0

I0 is the input impedance at the initial port of the cable.
The two-parallel transmission line model above the ground plane is shown in
Fig. 5.26. The ground plane in the ﬁgure can also be regarded as the shield outer
conductor of the two-core shield cable or the reference conductor of the three-wire
transmission line. This is also the reason for more research on three-line transmission
line model. It is assumed that a cable with an interference source as the transmitting
line and a disturbed cable as the receiving line. The line length is l > λ. Set up
the coordinate system, where the coordinate is from x = 0 to x = l. At x = 0, an
excitation voltage ug = Us sin ωt is applied between the transmitting line and the
reference conductor. The conductor is surrounded by a no-loss uniform medium with
a dielectric constant of ε and a magnetic permeability of μ. The terminal impedances
of the transmitting circuit at x = 0 and at x = l are Z0G and Z1G, respectively, while
the terminal impedances of the receiving circuit are Z0R and Z1R, respectively. The
equivalent circuit is shown in Fig. 5.27.


5.7 Cable Crosstalk Analysis
137
Fig. 5.26 High frequency
coupling of the transmission
lines
l
g
u
x
0R
Z
0G
Z
1G
Z
1R
Z
O
Fig. 5.27 An equivalent
circuit for high frequency
coupling of a transmission
line
0G
Z
( )
0
GI
( )
GI
x
( )
GI
l
S
U
( )
0
G
U
( )
0
RI
( )
G
U
x
( )
RI
x
( )
G
U
l
( )
RI
l
1G
Z
0R
Z
1R
Z
( )
0
R
U
( )
R
U
x
( )
R
U
l
0
X =
X
l
=
x
Transmission line
Receiving line
Reference conductor
In the ﬁgure, UG(x) and UR(x), respectively represent the voltages of the trans-
mitting and receiving lines which are relative to the reference conductor at any point
on the line. IG(x) and IR(x) are the current on the transmitting line and the current
on the receiving line, respectively.
Based on the distributed parameter theory, the self-inductances of the transmitting
line and the receiving line are set as LG and L R, respectively, in unit length. The
self-capacitances are CG and CR, respectively. The mutual inductance and mutual
capacitance between two lines are L M and CM, respectively. The equivalent circuit
of a small segment of transmission line x can be obtained without considering the
loss resistance on the transmission line, which is shown in Fig. 5.28.


138
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
( )
GI
x
( )
RI
x
( )
G
U
x
( )
R
U
x
(
)
GI
x
x
+ Δ
(
)
RI
x
x
+ Δ
(
)
G
U
x
x
+ Δ
(
)
R
U
x
x
+ Δ
x
x
+ Δ
x
x
G
L
x
Δ
M
L
x
Δ
R
L
x
Δ
M
C
x
Δ
G
C
x
Δ
R
C
x
Δ
Transmission line
Receiving line
Reference conductor
Fig. 5.28 An equivalent circuit for high frequency coupling of the line x
According to the equivalent circuit shown in the ﬁgure, if x →0, the voltage
and current equation on the cable are
⎧
⎪⎪⎨
⎪⎪⎩
dUG(x)
dx
= −jω[LG IG(x) + L M IR(x)]
dUR(x)
dx
= −jω[L M IG(x) + L R IR(x)]
dIG(x)
dx
= −jω[(CG + CM)UG(x) −CMUR(x)]
dIR(x)
dx
= −jω[(CR + CM)UR(x) −CMUG(x)]
.
(5.7.6)
The termination condition of x = 0 and x = l are supposed to be
⎧
⎪⎪⎨
⎪⎪⎩
UG(0) = US −Z0G IG(0)
UR(0) = −Z0R IR(0)
UG(l) = −Z1G IG(l)
UR(l) = −Z1R IR(l)
.
(5.7.8)
Interference voltages UR(0) and UR(l) at both ends of the receiving line can be
obtained.
⎧
⎪⎪⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎪⎪⎩
UR(l) = S
D

−

Z1R
Z0R+Z1R

jωL MlIGD +

Z0R Z1R
Z0R+Z1R

jωCMlUGD
 
UR(0) = S
D

Z0R
Z1R + Z0R

jωL Ml
!
C + j2π

l

λ

√
1 −k2 α1GS
"
IGD
+

Z0R Z1R
Z0R + Z1R

jωCMl
!
C + j2π

l

λ

√
1 −k2
1
α1G
S
"
UGD
,
(5.7.9)
where


5.7 Cable Crosstalk Analysis
139
S = sin(βl)
βl
q = cos(βl)
α0R = Z0R
ZC R
α1R = Z1R
ZC R
α0G = Z0G
ZCG
α1G = Z1G
ZCG
ZCG = υLG

1 −k2
ZC R = υL R

1 −k2
υ = ω
β
k =
L M
√LG L R
UGD =
Z1G
Z1G + Z0G
US
IGD =
US
Z1G + Z0G
τG =
LGl
Z0G + Z1G
+ (CG + CM)l
Z0G Z1G
Z0G + Z1G
τR =
L Rl
Z0R + Z1R
+ (CR + CM)l
Z0R Z1R
Z0R + Z1R
.
In the above formula, ZC R is the characteristic impedance of the transmitting
circuit when the receiving circuit exists; ZCG is the characteristic impedance of the
receiving circuit in the presence of the transmitting circuit; k is the coupling coefﬁ-
cient; UGD and IGD are the voltage and current of the transmission line, respectively.
τG and τR are the time constants of transmitting and receiving circuits, respectively.
The above is the analysis of cable coupling in high frequency. In the case of low
frequency, the length of the cable is far less than the wavelength, that is, l ≪λ, then
	UR(l) = U L
R (l) + U C
R (l)
UR(0) = U L
R (0) + U C
R (0) ,
(5.7.10)
where
⎧
⎪⎪⎪⎪⎪⎨
⎪⎪⎪⎪⎪⎩
U L
R (l) = −
Z1R
Z0R+Z1R jωL MlIGD
U L
R (0) =
Z0R
Z0R+Z1R jωL MlIGD
U C
R (l) = U C
R (0) = 0 =
Z0R Z1R
Z0R+Z1R jωCMlUGD
IGD =
US
Z0G+Z1G
UGD =
Z1GUS
Z1G+Z1G
.
In the formula, the terminal voltages UR(l) and UR(0) on the interfered line are
the superpositions of the two interfering voltages. The U L
R is the mutual inductance
L M coupling between two lines, that is, the inductive coupling. U C
R is generated by
capacitance CM coupling between two lines, that is, the capacitive coupling. It is
consistent with the analysis results based on the lumped parameter model.
According to the formula, an equivalent circuit of the low frequency coupling
(inductive coupling and capacitive coupling) of the two transmission lines is shown
in Fig. 5.29.


140
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.29 An equivalent
circuit for low frequency
coupling of a transmission
line
M
GD
j L lI
ω
M
GD
j C lU
ω
( )
0
RI
( )
RI
l
( )
0
R
U
( )
R
U
l
0R
Z
1R
Z
+         -
In general, the above analysis method can be used to analyze the cable crosstalk in
the ideal state or the cable crosstalk after simplifying the practical problem. However,
for complex practical problems, the above analysis models and methods may have
large errors. With the development and maturity of commercial electromagnetic
simulation software, the complex cable crosstalk problem can be analyzed by means
of commercial electromagnetic simulation software.
An example of a cable crosstalk analysis based on CST is given. A cable bundle
consists of ﬁve low frequency cables, of which four are instruction lines and one
is the ground wire. Four command lines share one ground wire. All the ﬁve cables
are shielding cables with a length of 4640 mm. The ground wire is grounded at the
source end and load end, respectively. The ground plane is 10 cm away from the
cable. The design changes the impedance characteristics of the source terminal and
the load end, which are shown in Fig. 5.30. It is necessary to evaluate whether the
cable shield layer in new design needs to be grounded at the source terminal or at
both the source terminal and the load end.
For analytical evaluation, a non-shielded cable is laid as the receiving line at the
left side of the cable bundle, with a distance of 2 mm. Signals are injected into
instruction lines as the transmitting line. The choice of grounding mode is evaluated
by comparing the signals coupled to the receiving line in different grounding modes.
The analysis model is shown in Fig. 5.31.
Fig. 5.30 Source and load
impedance characteristics
Source
Load
1k
10k
30k
300k
0.01u
0.01u


5.7 Cable Crosstalk Analysis
141
Fig. 5.31 Analysis model of cable coupling
In the analysis process, 5, 10, 50, and 100 kHz sinusoidal signals are ﬁrstly injected
into the transmitting line to evaluate the transmission emission results of the cable
at the frequency concerned by using different grounding modes. Then, the input
instruction signal online is a pulse voltage with a voltage of 12 V and a pulse width
of 104 ms, the rising edge is 0.7 ms and the descending edge is 0.55 ms. The crosstalk
characteristics of the cable with different grounding modes for impulse interference
are analyzed.
Table 5.10 shows the four frequency points of 5, 10, 50, and 100 kHz, and
the difference of signal coupling on the receiving line between values obtained by
using the double-ended grounding of the shield layer and by using the single-ended
grounding of the source. It can be seen from the simulation results in Table 5.10
that, at the four frequency points concerned, the electromagnetic compatibility of the
double-endedgroundingofthecableshieldlayerisbetterthanthatofthesingle-ended
grounding of the cable shield layer.
Figure 5.32 shows the results of the analysis for transient signals. The red curve is
the result of analysis for the shield layer by using the single-ended grounding of the
Table 5.10 Steady-state analysis results
Frequency (kHz)
Signal difference between double-ended grounding and single-ended
grounding coupling line (dB)
5
−15.0
10
−16.6
50
−13.6
100
−13.5


142
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.32 Transient
coupling analysis results
 (a) Coupling signal analysis results 
(b) Result at the rising edge 
(c) Result at the descending edge 


5.7 Cable Crosstalk Analysis
143
source and the green curve is the result of analysis for the cable shield layer by using
the double-ended grounding. It can be seen from Fig. 5.32 that transient disturbances
by using the double-ended grounding mode of cable shield layer are smaller than that
by the single-ended grounding mode at the source of the shield layer. The reduction
of coupled disturbance exists not only in the signal level, but also in the slope of
the signal in the upper edge and lower edge. It is proved that the electromagnetic
compatibility of the double-ended grounding mode of the shield layer is better than
that of the single-ended grounding mode of the shield layer.
In the above example, steady-state analysis and transient analysis show that the
electromagnetic compatibility of the cable, which has changed the impedance charac-
teristics of the source terminal and of the load end, in double-ended grounding of the
shield layer is better than that of the single-ended grounding of the shield layer. It can
also be stated from the above example that the analysis results of cable crosstalk char-
acteristics can be directly obtained through the electromagnetic simulation analysis
software for commercial use.
5.8
Field-Cable Coupling Analysis
In the space electromagnetic ﬁeld, the coupling of a cable, whether shielded or not,
is an important cause of radiation sensitivity of the equipment or system.
If the height of the cable from the ground plane is h, and h is far less than the
length l and the wavelength of the cable is λ, that is, h ≪l and h ≪λ, a cable can be
regarded as a two-line transmission line model with its image of the ground plane,
as shown in Fig. 5.33. The connection impedances of the transmission line are Z0
and Z1. The characteristic impedance of the cable is
Zc =

(Zi + jωI)ωI
jk2
.
(5.8.1)
Fig. 5.33 Cable coupled
EMI model
E
H


144
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
The interference voltage or interference current of the cable coupled electromag-
netic ﬁeld can be calculated through the transmission line equation. If the cable is
shielded and has two terminals grounded, the terminal impedance is approximately
0, then the coupled interference current is
I = 4Eh
Zc
.
(5.8.2)
E is the space electric ﬁeld. If the interference of the spatial electromagnetic ﬁeld
has a vertically polarized E ﬁeld component, the component will have a coupling
effect at the end of the cable. However, this coupling effect can be ignored, because
the length of the cable is assumed to be much larger than the height of the cable from
the ground. Theoretically, since the terminal impedance is 0, the terminal current
should be inﬁnite. However, the actual connection impedance always exists, and the
current is different from the theoretical value of inﬁnity.
For isolated cables, although this problem does not generally arise on spacecraft,
the method of coupled interference analysis is given in this section. When both the
ends of the cable are not grounded, the coupling current will not be generated. If the
electric ﬁeld is perpendicular to the cable, the coupling current is generated when
there is a magnetic component perpendicular to the cable and an electric compo-
nent parallel to the cable. The strength of the coupled current depends on length,
impedance, and wavelength of the cable. If the length of the cable is less than λ

10,
the coupling current can be approximated as
I = 4π f Bl
Zc
π
λ
2  l
2
2 −1
2l2
2
(5.8.3)
Zc =

R2 + 2π f L2,
(5.8.4)
where f is the frequency; B is magnetic ﬂux density; l is the length of the cable; λ
is the wavelength; R is the cable resistance; L is the cable inductance.
The above analysis generally adopts an approximate analysis method. If more
accurate analysis results are desired, the multiconductor transmission line (MTLs)
model under external ﬁeld excitation can be used for analysis. As shown in the
Fig. 5.34, the external ﬁeld excitation multiconductor transmission line model is as
follows:
d
dz
 V (z, s)
I(z, s)

= Q(s)
V (z, s)
I(z, s)

+
VD(z, s)
ID(z, s)

Q(s) =
 0
−R
−G
0

+
 0
−L
−C
0

s,
(5.8.5)
where: V(z, s) and I(z, s) are voltage and current matrices respectively; VD(z, s) and
ID(z, s) are distributed voltage sources and current sources on MTLs respectively. R,


5.8 Field-Cable Coupling Analysis
145
Fig. 5.34 MTLs model
under ﬁeld excitation
G, L, and C are the unit length resistance, conductance, inductance, and capacitance
matrices of MTLs, respectively, s is the complex frequency.
The solution of the telegraph equation is
 V(l, s)
I(l, s)

= e Q(s)l
 V(0, s)
I(0, s)

+ J(s)
J(s) =
 l
0
e Q(s)(l−z)
 V D(z, s)
I D(z, s)

dz,
(5.8.6)
where l is the length of the transmission line.
Suppose the electric ﬁeld in the ﬁgure is
E(x, y, z) = E0

Axax + Ayay + Azaz

e−s(κx x+κy y+κzz),
(5.8.7)
where, κ is the propagation vector. The distribution source of MTLs is
 V D(z, s)
I D(z, s)

= Γ (s)e−sκzz,
where, Γ (s) is the transmission coefﬁcient of the transmission line. For the
transmission line with ground wire, it is deﬁned as
Γ (s) = E0
s In
0n
0n (G + sC)

· · · 2κx Axxi −2κy Azyi · · · | · · · 2Axxi + 2Ayyi · · ·
T
(5.8.8)
Let
M = −Q(s) −sκz I2n
(5.8.9)


146
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
then
J(s) = e Q(s)l
eMl −I2n

M−1Γ (s) = −e Q(s)l M−1Γ (s) + e−sκz I2n M−1Γ (s)
(5.8.10)
so, we have
 V(l, s)
I(l, s)

= e Q(s)l
	 V(0, s)
I(0, s)

−M−1Γ (s)
#
+ e−sκz I2nl M−1Γ (s)
= e Q(s)l
	 V(0, s)
I(0, s)

+
 V Dn(s)
I Dn(s)
#
+
 V Df (s)
I Df (s)

,
(5.8.11)
where
⎧
⎪⎪⎨
⎪⎪⎩
 V Dn(s)
I Dn(s)

= −M−1Γ (s)
 V Df (s)
I Df (s)

= e−sκz I2nl M−1Γ (s)
The above formula is the total equivalent source of the proximal set and the total
equivalent source of the remote set of MTLs. It can be seen that the equivalent
source is no longer related to the exponential matrix e Q(s)l of MTLs. This reduces
the difﬁculty of the solution and facilitates the realization of analysis.
The voltage and current of the external ﬁeld coupled to the cable can be obtained
by solving the telegraph equation. However, the above equation is difﬁcult to be
solved. Therefore, the numerical method is often used in practical application. The
following formula is an algorithm of the numerical solution by using FDTD, which
can greatly simplify the difﬁculty of the solution.
V n+1
k
=

C z
t + G
2 z
−1
C z
t −G
2 z

V n
k −

I n+1/ 2
k
−I n+1/ 2
k−1

I n+3/ 2
k
=

L z
t + R
2 z
−1
L z
t −R
2 z

I n+1/ 2
k
−

V n+1
k+1 −V n+1
k

V n+1
N+1 =

C z
t + G
2 z
−1
C z
t −G
2 z

V n
N+1 + ψDnV + ψDf V
+ 2RL

I n+1/ 2
N
+ ψDnI + ψDf I

,
(5.8.12)
where RL representstheterminalload;ψDnV andψDf V areequivalentvoltagesources
of near ﬁeld and far ﬁeld, respectively; ψDnI and ψDf I are equivalent current sources
of near ﬁeld and far ﬁeld, respectively.
The above method is used to analyze the effect of electromagnetic pulse on space-
craft cable. The model of the spacecraft is taken as the lifting stage. The analysis


5.8 Field-Cable Coupling Analysis
147
0.04
F
10k
100k
Fig. 5.35 The load circuit
Fig. 5.36 The cable size
0.49mm
1.1mm
model was taken from the part of the carrier, with a diameter of 3.63 m and a height
of 7.23 m. There are two wave transmission windows of size 0.3 m × 0.3 m on the
carrier. There are two shielding cables with the length of 2 m inside the carrier, and
the shielding layer of the cable is double-ended grounded. The cables are arranged in
parallel, one instruction line and one loop line. The cable source side has a resistance
of 50 , the load characteristics are shown in Fig. 5.35. The parameters of cable are
shown in Fig. 5.36. The radius of the inner conductor is 0.49 mm and the radius of
cable is 1.1 mm. The electromagnetic pulse adopts a dual-exponential pulse, with a
peak value of 65,000 V/m, a rise time of 1.67 ns, and a fall time of 25 ns. The direction
of the electromagnetic pulse is set as the direction of the carrier wave transmission
window.
Firstly, the internal electric ﬁeld of the electromagnetic pulse passing through the
carrier cabin and the wave transmission window is obtained by numerical calculation
method, and then the interference signal coupled on the cable is analyzed by the above
method. Figures 5.37 and 5.38 show the induced voltage waveform at the source and
load ends.
It can be seen from the ﬁgure that for the analysis of ﬁeld line coupling, especially
some time-domain characteristics, the analysis results can be obtained by using the
above method.
Theaboveformula-basedanalysismethodwillbeaffectedbydifferentcabletypes,
impedance characteristics, radiation ﬁeld characteristics, and environmental factors
in practical application, which may limit the application of the method or reduce


148
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
Fig. 5.37 The source
voltage induction
0
0.05
0.1
0.15
-200
-100
0
100
200
t/us
V/V
Fig. 5.38 The load induced
voltage induction
0
0.05
0.1
0.15
-1000
-500
0
500
1000
t/us
V/V
the accuracy of the analysis. In particular, the external environment should not be
pretreated by some other methods of electromagnetism analysis. At present, some
commercial electromagnetic simulation software, such as CST and EMC Studio,
is made available for analyzing the external electromagnetic interference of cable
coupling.
Figure 5.39 is an example of an analysis using CST software. The model in the
ﬁgure is a set of low frequency cables, consisting of ﬁve cables, of which four cables
areinstructioncablesandonecableisthegroundwire.Alltheﬁvecablesareshielding
cables, with a length of 4640 mm, forming a bundle. These Four instruction cables
Fig. 5.39 The analysis model of the external ﬁeld to cable coupling


5.8 Field-Cable Coupling Analysis
149
Fig. 5.40 Cable coupled external ﬁeld voltage signal
shareonegroundwire.Thecablesourceisaresistivecircuit,theloadendisaresistive-
capacitance circuit, and the shield layer is double-ended grounded. The shield layer
of shield cable is grounded at the load end. The incident electromagnetic wave is
assumed as a left-handed circular polarized electromagnetic wave. Its radiation is
located at the side of the cable with an angle of 45° to the ground plane. The induced
voltage of cable coupled with external ﬁeld interference under 1 GHz is analyzed.
Figure 5.40 shows the coupled interference voltage on one of the cables. It can
be seen from the ﬁgure that the coupling effect of the external ﬁeld on the cable can
be easily obtained through the three-dimensional electromagnetic ﬁeld simulation
analysis. In the frequency range of simulation, the interference coupling voltage
corresponding to each frequency point can be obtained more clearly.
5.9
The Hazards and Protection of Electromagnetic
Radiation to Personnel and EED
5.9.1
Quantiﬁcation Requirements for Electromagnetic
Radiation Hazards
5.9.1.1
The Importance of Electromagnetic Radiation Hazards
Protection
High strength electromagnetic energy may cause harmful human biological effects,
mistriggering of EED, degradation of performance or failure of critical safety circuits,
etc. Therefore, the hazards of electromagnetic radiation of the spacecraft system to
the personnel and the EED should be analyzed and controlled.


150
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
5.9.1.2
Quantiﬁcation Requirements of Personnel Hazards
by Electromagnetic Radiation
The quantiﬁcation requirements of electromagnetic radiation on human hazards are
required to be implemented according to national standards of electromagnetic radi-
ation protection or international standards. During the electric test period of the
spacecraft and when the astronauts work in and out of the space module, the testers
and the astronauts will be affected by the electromagnetic radiation generated by the
surrounding electrical and electronic equipment. It is necessary to analyze and eval-
uate the hazards of the electromagnetic environment according to the limit values set
by the electromagnetic radiation protection standards, so as to ensure the hazards of
electromagnetic radiation to personnel is identiﬁed and effectively controlled.
Since the limits of electromagnetic protection standards in different countries are
different in each frequency band, this section mainly addresses the requirements and
methods of international general speciﬁcations such as IEEE C95.1 and ICNIRP
(International Commission on Non-ionizing Radiation Protection).
Three requirements should be considered in personnel electromagnetic radiation
protection:
First, it is determined to control according to the occupational exposure limit or
nonoccupational exposure limit;
Second, the limit values set by the standards are related to the frequency band of
electromagnetic radiation and different parts of the human body. According to the
frequency band and intensity of the main electromagnetic radiation of the spacecraft,
it is necessary to determine the key positions and heights of the magnetic ﬁeld and
electric ﬁeld frequency band and the heads and chests of the personnel concerned.
Third, it is necessary to identify problems such as continuous wave, pulse wave,
and superposition of multiple electromagnetic radiation source ﬁelds, estimate the
power density, and analyze the measurement data.
(1) For the electromagnetic radiation in the continuous wave mode, the test results
of the electric ﬁeld sensor are average ﬁeld strength and peak ﬁeld strength,
both of which are equal.
(2) For the electromagnetic radiation of the pulse wave mode, the test result of the
antenna is the peak ﬁeld strength of the pulse wave, and the average ﬁeld strength
of the pulse wave can be calculated according to Eq. (5.9.1). If the average
ﬁeld strength is measured by the thermocouple type ﬁeld strength sensor, the
peak ﬁeld strength can be calculated by the formula (5.9.1). Formula (5.9.1) is
applicable to ideal pulse signals with a known pulse period and pulse width.
EV = E p

τ/T
(5.9.1)
EV —Average ﬁeld strength, V/m;
E p—Peak ﬁeld strength, V/m;
τ—Pulse width, s;


5.9 The Hazards and Protection of Electromagnetic Radiation …
151
T —Pulse period, s.
Electromagnetic radiation limits for different frequency bands and different parts
of personnel are given in the general standard. Electromagnetic radiation protection
of astronauts and spacecraft electrical measuring personnel in the manned space
program can be controlled and protected according to the relevant limits.
5.9.1.3
Quantiﬁcation Requirements of Electromagnetic Radiation
on EED
The EED is an independent unit or component that can produce an electrical explo-
sion. In the spacecraft system, EED mainly performs the functions of separating
spacecraft and launch vehicle, unlocking solar array and antenna, etc. High-intensity
electromagnetic radiation induces interference currents in the EED’s cables. It is
necessary to ensure that the EED does not separate or unlock the device by EMI.
The quantiﬁcation requirement of electromagnetic radiation on the EED is the
Maximum No-Fire Current (MNFC). In general, the resistance value of the bridge
wire of EED is required to calculate the response parameters such as current, voltage
or power that can be detected by the monitoring device. The margin requirement of
EED is generally 20 dB.
5.9.2
Electromagnetic Radiation Hazards Analysis
and Veriﬁcation
5.9.2.1
Analysis and Veriﬁcation of Electromagnetic Radiation
Hazards to Personnel
Three-axis electromagnetic ﬁeld measurement equipment is usually used for elec-
tromagnetic radiation detection at the exposure site. The measurement data can be
compared with the standard limit value to evaluate the electromagnetic radiation
hazards at the site.
In spacecraft systems analysis, electromagnetic emission may have multiple
sources of radiation working simultaneously. For the mixed broadband radiation
ﬁeld composed of multiple frequencies, it should ﬁrst be determined whether each
frequency meets the corresponding limit value, then the total radiation will not
exceed the limit value. The following formula can be used for the synthesis ﬁeld
strength analysis of multiple continuous wave radiation sources under different limit
conditions
E =

E2
1 + E2
2 + · · · + E2n.
(5.9.2)


152
5
Analysis of Spacecraft System-Level Electromagnetic Compatibility
5.9.2.2
Analysis and Validation of Electromagnetic Radiation Hazards
to EED
Because it is difﬁcult to verify according to the standard requirements at all frequen-
cies, the response of the EED device is measured according to the maximum test
capability, and then the maximum allowable environmental level is extrapolated
according to the test results. The extrapolation prerequisite is that the level of the
electromagnetic radiation response of the EED circuit in the test electromagnetic
environment is linear with that in the electromagnetic environment to be extrapolated.
(1) The safe excitation current of the EED is obtained by the following equation:
Ip/f = SMd ∗M N FC,
(5.9.3)
where
Ip/f—Safe excitation current of the EED, mA;
SMd—Decimal representation of safety margin (SM) (for example, the
decimal values of 20 dB and 16.5 dB are 0.1 and 0.15 respectively);
MNFC—Maximum Non-Ignition Current of an EED, mA.
(2) The response current of the EED under the electromagnetic environment level
is calculated
Ic = Ec∗It/Et,
(5.9.4)
where
Et—Electromagnetic environment level during the test, V/m;
Ec—Required electromagnetic environment level, V/m;
It—Measured induced current of the EED during the test, mA;
Ic—Required induction current of the EED in the electromagnetic environ-
ment, mA.
(3) Calculation of maximum permissible environmental level (MAE)
M AE = Et

Ip/f/It

,
(5.9.5)
where
MAE—Maximum permissible environmental level, V/m;
Et—Electromagnetic environment level during test, V/m;
Ip/f—Safe excitation of EED, mA;
It—Measured value of induction current of EED was measured during the
test, mA.


5.9 The Hazards and Protection of Electromagnetic Radiation …
153
If the response is not measured, the minimum detectable current of the EED
response monitoring equipment is taken as the induction current of the EED.
The electromagnetic radiation of the spacecraft system has potential hazards to
the astronauts and the electrical measuring personnel.
The electromagnetic radiation of the spacecraft system has potential radiation
hazards to the electric initiation device. It is necessary to analyze the radiation inten-
sity of the electromagnetic environment and its coupled current or power charac-
teristics, and determine to check whether the margin meets the requirements. The
sensitivity characteristics of EED can also be explored through experimental methods
to provide data support for determining margin control indicators.
5.10
Summary
The analysis of the EME of the spacecraft system is to go deep into the electro-
magnetic characteristics of the system, identify the EMI risk, and determine the
design limit. In order to provide professional guidance for EMC quantitative design,
it is necessary to analyze and calculate by means of simulation software or classical
formula from the aspects of safety margin, electromagnetic environment compati-
bility between systems, EMC within systems, electromagnetic radiation hazards to
personnel and EED, and electromagnetic spectrum compatibility.

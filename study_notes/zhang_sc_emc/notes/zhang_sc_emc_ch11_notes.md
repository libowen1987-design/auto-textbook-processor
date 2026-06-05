# Zhang《Spacecraft EMC Technologies》第11章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 11. Spacecraft System-Level EMC Test Verification

Chapter 11
Spacecraft System-Level EMC Test
Veriﬁcation
11.1
Electromagnetic Environmental Effect (E3) Test
11.1.1
Test Requirements
The system electromagnetic environment effect (E3) requirements are based on the
general development requirements or speciﬁcations in the contract, which include
the test content and speciﬁc test items. The E3 test shall be carried out according to
the test program. For a particular system, the standards can be tailored according to
its E3 characteristics.
In the test, all states or phases throughout the life cycle of the system, including the
development, assembly, storage, transportation, and launch of the spacecraft, as well
as the corresponding normal operation procedures for each state (or phase) described
above should be taken into account.
11.1.1.1
Classiﬁcation of Test Methods
The system E3 test methods are divided into safety margin, intra-system EMC,
external RF electromagnetic environment (EME), lightning, electromagnetic pulse,
subsystem and equipment EMI, electrostatic, hazard of electromagnetic radiation,
electric bonding and external grounding, emission control, spectrum compatibility,
etc.
11.1.1.2
Test Environment Requirements
The EME level should not affect the test results, and should be at least 6 dB below
the speciﬁed limit. The EME level should be recorded in the test report. If testing in
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_11
499


500
11
Spacecraft System-Level EMC Test Veriﬁcation
the outﬁeld, other technologies may be used to eliminate the environmental impact,
or the test is performed in a certain period of time and conditions where the EME
level is the lowest.
11.1.1.3
Test Site Requirements
The test site shall be selected in an anechoic enclosure, a shielded enclosure, or an
open test ﬁeld according to the test item requirement and the actual size of the SUT.
In order to prevent the SUT from interacting with the external environment, the test
is usually carried out in an anechoic or shielded enclosure. The test site shall provide
the necessary power supply, temperature and humidity, ventilation, ﬁre protection,
safety, and other support equipment to meet the proper operation of the system and
test equipment.
In order to reduce the reﬂection of EM waves and improve the accuracy and
repeatability of the test, when the system is under RE and RS testing, the inner
walls of the shielded enclosure should be applied with RF absorbing material. The
performance of the RF absorbing material should meet the requirements speciﬁed
in MIL-STD-461 or meet the EMC test requirements of spacecraft systems. The
boundary of SUT such as spacecraft and ground test antennas should have a distance
of no less than 1 m from the absorbing material in the anechoic enclosure.
During the test, all systems and equipment related to the test shall operate under
the conditions speciﬁed in the test program (if there is no explicit requirement,
normal operating state should be used). First, select the typical operating state of the
SUT designed with different operating states (including software-controlled state)
to obtain the system EMC characteristics under the typical operating state; second,
obtain the EMC characteristics of the subsystems and equipment in the operating
states where EMI is most likely to occur, and where EMI reaches the maximum or
the system is most sensitive to EMI.
11.1.2
Test Contents
Spacecraft system-level EMC performance should be veriﬁed on typical products.
Generally, the ﬁrst launched spacecraft in the series should implement a more
comprehensive EMC test and evaluation. The later models of the same series should
be selectively veriﬁed on items according to the requirements.
In general, the electronic equipment on the spacecraft has been separately tested
according to the EMC technical requirements (refer to Chap. 10). Though most
equipment can pass the EMC tests, the interface status (for example, an equipment
has multiple interfaces, only some of which have been tested due to the limited
capability of the ground test support equipment, a few interfaces have not been EMC
tested), and cable status (such as length, shielding, and grounding) may be different
from the actual situation; and a small amount of equipment may have some CE


11.1 Electromagnetic Environmental Effect (E3) Test
501
or RE test items exceeding the standards, but have been accepted by compromise
after EMC design risk analysis, and the EMC performances of related equipment are
planned to be measured and tested at the system level. Therefore, system-level EMC
veriﬁcations are divided into the following categories:
(1) The EMC tests between spacecraft intra-system electronic equipment under
typical operating conditions, including bonding, grounding, power lead
conducted interference, multiplication, EM spectrum compatibility, and mutual
interference tests;
(2) The EMC tests between the spacecraft system and external EME, including the
EME of the launch vehicles, launch site, and other spacecraft;
(3) Veriﬁcation for spacecraft safety margin and mission-critical equipment EMC
margins.
The spacecraft system-level EMC test items and methods are shown in Table 11.1.
11.1.2.1
Intra-System Electromagnetic Self-Compatibility Test
Before the system-level tests, the development organization should provide the EMC
test reports of each electronic equipment or subsystem in the SUT. Based on these test
results, the interference sources and sensitive equipment are classiﬁed, and the intra-
system electromagnetic self-compatibility test matrix of these sources and sensitive
equipment are ﬁnally determined and incorporated into the EMC test program, as
shown in Table 11.2.
During the self-compatibility test, the electronic equipment or subsystems as the
interference source shall operate in the maximum emission state, and those as the
sensitive equipment shall operate in the most sensitive state.
11.1.2.2
System EME Compatibility Test
This test is aimed to measure the spacecraft EM RE in the frequency band of 10 kHz
to 18 GHz (40 GHz) under various operating conditions.
For the ﬁrst launched satellite, this test is generally carried out during the proto
ﬂight model development stage of the satellite. During the test, the spacecraft shall
be placed on a bracket according to the actual installation connection state, and the
state of equipment layout, grounding, cable network should be consistent with the
actual state as much as possible. Unless otherwise speciﬁed, the horizontal distance
between EMC measurement antenna and SUT’s boundary shall be 1 m; the center
of the antenna is one-half the height of the SUT; the number of antenna positions
depends on the dimensions of the SUT’s boundary and the number of equipment
included in the SUT, and also depends on the pattern of the EMC antenna.


502
11
Spacecraft System-Level EMC Test Veriﬁcation
Table 11.1 Spacecraft system-level EMC test items and methods
Category
Test items
Test methods
Test sites
Intra-system EMC
tests
Bonding and grounding
performance
Bonding and grounding
resistance measurement
AIT workshop
Power lead conducted
interference test
System power bus
conducted transient
interference test
System power bus
conducted voltage
ripple test
System power bus
sweeping frequency CE
test
Multipaction
Multipaction
(multipactor) test
method
Multipaction
laboratory
Spectrum compatibility
Antennas isolation test
EMC chamber
RF leakage test
AIT workshop
Receiving antenna
in-band noise test
EMC chamber
EMC Source-Victim
test
RF equipment
combining radiated test
EMC chamber
System and external
EME
External EME
EMC test between
spacecraft system and
launch vehicle/launch
site
EMC chamber/launch
site
EMC veriﬁcation
between spacecraft
EMC chamber/launch
site
Critical equipment
margin
Margin veriﬁcation
EMC margin
veriﬁcation for
spacecraft critical
equipment
AIT workshop/EMC
chamber
11.1.2.3
System Primary Power Bus Transient Test
This test is to measure the pulse signals of the transient voltage or transient current
generated on the system primary power bus during switching on and off of various
switches and changing conditions of loads under normal operation of the space-
craft system, and to determine whether the transient pulse signals satisfy the system
primary power bus transient speciﬁcation requirements.


11.1 Electromagnetic Environmental Effect (E3) Test
503
Table 11.2 Intra-system electromagnetic self-compatibility test matrix
Interference source
Sensitive equipment
Equipment or subsystem 1
Equipment or subsystem 2
Equipment or
subsystem 3
……
OM 1
OM 2
OM 3
……
OM 1
OM 2
OM 3
……
Equipment or
subsystem 1
OM 1
/
OM 2
/
OM 3
/
……
/
Equipment or
subsystem 2
OM 1
/
OM 2
/
OM 3
/
……
/
Equipment or subsystem 3
/
……
/
Note OM operating mode


504
11
Spacecraft System-Level EMC Test Veriﬁcation
11.1.2.4
Multiplication Test
This test is designed to verify whether the multiplication effect will occur in the
SUT’s RF circuit under vacuum conditions, and verify the multiplication protection
design.
11.1.2.5
Test and Redesign Process
The E3 test and the redesign process are shown in Fig. 11.1.
5HGXFHULVNE\
GHVLJQDQGRUUHWHVW
5HTXLUHDGGLWLRQDO
WHVWV"
Modify the equipment installaon or 
EMC design
7HVW
+DVWKHULVN
EHHQUHGXFHGWR
WKHDFFHSWDEOH
OHYHO"
&DQWKHHTXLSPHQW
LQVWDOODWLRQRU
GHVLJQEHPRGLILHG"
$FFHSWRUUHIXVH
<HV
<HV
1R
1R
<HV
1R
Fig. 11.1 Flowchart of E3 test and redesign


11.1 Electromagnetic Environmental Effect (E3) Test
505
11.1.3
Evaluation of E3
The test data in different stages of spacecraft life-cycle development should be
compared with the requirements speciﬁed in the test program, and be evaluated
to determine whether the spacecraft system E3 test has achieved its objective and
make a reasonable evaluation and conclusion of the experimental results. The evalu-
ation result and conclusion will be used to determine the following EMC work. The
focuses of EMC work in various development stages are generally as follows:
(1) In the demonstration stage, the expected E3 and possible development risks are
evaluated in conjunction with the characteristics of the spacecraft operations,
and the rationality of the E3 requirements is conﬁrmed;
(2) In the scheme stage, the E3 designs and risk avoidance measures are evaluated
to conﬁrm their effectiveness;
➀Develop protective measures for potential EMI sources and sensitive
equipment;
➁According to the spacecraft performance, EMC requirements and frequency
management regulations, conduct research on the frequency utilization
issues, and propose the spacecraft EM spectrum characteristics management
requirements;
➂Develop reasonable EMI control measures (such as frequency and power
management and space isolation) for critical RF equipment (such as TT&C
equipment and payload).
(3) In the proto ﬂight model stage, the E3 capability level of the spacecraft should
be evaluated to conﬁrm the compliance with the E3 requirements.
➀Focus on the usage evaluation of the undesired response found in the EMC
test of the proto ﬂight model satellite to conﬁrm its inﬂuence on the entire
system/self-compatibility;
➁According to the test and analysis results, develop and implement corre-
sponding improvement measures in the ﬂight model stage.
(4) In the ﬂight model stage, conﬁrm the comprehensiveness and rationality of the
E3 of the spacecraft.
➀Test the spacecraft in the launch state and at each in-orbit operating state,
analyze and evaluate the EMC in the untested operating states;
➁Focus on the impact of exceeding limit problems in the test and analyze
the effects of in-orbit operation. Continuously track the spacecraft’s opera-
tion and conﬁrm the inﬂuence of the orbit environment and using time on
its EMC. The E3 risk assessment process and the critical equipment risk
assessment process are shown in Fig. 11.2 and Fig. 11.3, respectively.


506
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.2 Flowchart of E3
risk evaluation
Evaluate the compliance of 
the EMC technical 
requirements with the 
equipment
Confirm the degree of the spacecraft 
equipment satisfying EMC standard
Evidence: EMC test report or 
certification
List the EMC test items required by 
equipment-level EMC
Conduct difference analysis for key 
tests, determine test parameters 
requirement on performance
Confirm whether any test item is 
missed.
According to each test result,
the risk is graded as low, 
medium and high
Used for risk evaluation
11.2
Spacecraft Intra-System Self-Compatibility Test
11.2.1
Mutual Interference Test Matrix
The spacecraft intra-system frequency compatibility analysis and equipment EMC
test results can be used to determine the potential interference sources and sensitive


11.2 Spacecraft Intra-System Self-Compatibility Test
507
Fig. 11.3 Flowchart of
critical equipment risk
evaluation
risk evaluation against 
functional criticality
Confirm the device is critical or 
non-critical for security and mission
Confirm electromagnetic 
environment of the spacecraft 
Determine if critical risks are 
acceptable
Confirm whether any test item is 
missed
List all unacceptable risks
Used for Risk mitigation 
equipment and establish a mutual interference test matrix. The spacecraft intra-
system interference sources and sensitive equipment can be determined by
(1) Potential interference sources:
➀All intentional RF transmitters, such as TT&C transmitters, data transmis-
sion transmitters, radars;
➁All equipment that contain magnetic operating components, such as motors,
relays;
➂All equipment that contain frequency sources, such as the systems
containing switching power supply, clock oscillating circuits or processors;
➃All high-power equipment that can generate power line transients during
turning on or off;
➄All equipment that exceeding limits in the equipment-level EMC emission
test items.


508
11
Spacecraft System-Level EMC Test Veriﬁcation
(2) Potential sensitive equipment:
➀All RF receivers, such as TT&C receivers, reconnaissance receivers;
➁All equipment that are sensitive to LF magnetic ﬁeld, such as magnetic
torque meter;
➂All sensors that contain low-level voltage signal, such as star trackers,
infrared earth sensors.
➃All equipment that contain low-level voltage or current protection devices,
such as traveling wave tube ampliﬁers (TWTA);
➄All equipment that exceeding limits in the equipment-level EMC suscepti-
bility test items.
➅All critical equipment that are related with spacecraft safety.
The mutual interference test matrix under typical working conditions can be deter-
mined according to various equipment combinations under different operating states.
Using the principle of “from simple to complex”, the test can be carried out in the
sequence of one-to-one, multiple-to-one, and multiple-to-multiple.
Examples of spacecraft frequency compatibility analysis results are shown in
Table 11.3.
The mutual interference test matrix is established on the basis of the analysis, as
shown in Table 11.4:
11.2.2
Selection of Mutual Interference Test Conditions
When performing the mutual EMI test, it is recommended to set the operation state of
the interference source and sensitive equipment according to the following principles:
Table 11.3 Examples of spacecraft frequency compatibility analysis results
No
Interference source
Sensitive equipment
Interference path
Spacecraft
operating state
1
Local oscillator of
radar altimeter
(RAM)
Microwave scatter
meter (MSM)
RF leakage
Joint transmission
mode
2
Intermediate
frequency of the
altimeter
Microwave
radiometer (MRM)
RF leakage
Joint transmission
mode
3
C-band operating
frequency of radar
altimeter
MRM
RF leakage
Joint transmission
mode
4
Third harmonic of
USB transmitter
MRM
Antenna interference
Joint transmission
mode
5
Transmitting
frequency of USB
transmitter
Payload receiver
Antenna interference
Laser
communication
mode


11.2 Spacecraft Intra-System Self-Compatibility Test
509
Table 11.4 Examples of spacecraft mutual interference test matrix
Spacecraft working mode
Interference source and sensitive equipment
veriﬁcation pair
One-to-one test matrix (one interference source to one sensitive equipment)
Joint transmission mode
RAM →MSM
RAM →MRM
USB transmitter →MRM
Laser communication mode
USB transmitter →payload receiver
Multiple-to-one test matrix (multiple interference sources to one sensitive equipment)
Joint transmission mode
RAM, USB transmitter →MRM
(1) Requirements for the operation state setting of the interference source
➀All intentional RF transmitters should be in the maximum output power
working state;
➁The radiation frequency of all intentional RF transmitters should cover its
entire working frequency and the working frequency of the electronic equip-
ment, such as intermediate frequency, crystal oscillator frequency, clock
frequency, switching power supply frequency.
➂If the interference source equipment has multiple working modes, select the
typical working mode that reﬂects the EMI characteristics of the equipment.
➃All the interference source equipment should be set to the maximum load
state. For example, the electric drive should be set to the speciﬁed load state.
(2) Requirements for the working state setting of sensitive equipment:
➀Sensitive equipment should be set in the most sensitive working state. The
receiver’s susceptibility should be set at the threshold.
➁If the sensitive equipment has multiple working modes, their working prin-
ciples should be analyzed. If certain typical working modes can reﬂect its
EM sensitive characteristics, the typical working modes can be selected for
veriﬁcation;
➂The test shall cover the operating frequency bands of all RF receivers,
and the effects of the transmission of internal electronic equipment and
antenna coupling signals on the operation of the receiver should be taken
into account;
➃Susceptibility criteria should be established for sensitive equipment to char-
acterize the variation range of the operational speciﬁcations and parameters
of spacecraft electronic equipment.


510
11
Spacecraft System-Level EMC Test Veriﬁcation
11.2.3
Implementation of Mutual Interference Test
The mutual interference tests for spacecraft systems can be performed by the
following steps:
➀Prepare a matrix of mutual EMI test and select the test conditions;
➁Power on and operate in sequence the peripheral electronic equipment of the
spacecraft that are out of the mutual interference test matrix
➂Power on the ﬁrst sensitive equipment and set its working conditions, monitor
and ensure its performances meet the criteria;
➃Power on the ﬁrst interference equipment and set its working conditions, monitor
and record its working status and parameters; if there is a deviation from the
susceptibility criterion, determine the susceptibility threshold while ensuring the
equipment safety;
➄Shut down and powered off the ﬁrst interference equipment;
➅Power on and operate the other interference equipment in sequence, and repeat
steps 4 and 5 for test;
➆Shut down and powered off the ﬁrst sensitive equipment;
➇Repeat steps 6 and 7 for test of other sensitive equipment in sequence, and
complete the one-to-one mutual interference test;
➈Power on the ﬁrst sensitive equipment and repeat step 3 for test;
➉According to the multiple-to-one test matrix, power on and operate all the inter-
ference source equipment in sequence, monitor and record whether the working
status and indicators of the sensitive equipment meet the criteria; if there is a
deviation from the susceptibility criteria, determine the susceptibility threshold
while ensuring the equipment safety.
⃝
11
According to the methods in step 10, verify other sensitive equipment in
sequence, and complete the multiple-to-one mutual interference tests.
11.2.4
Evaluation of Mutual Interference Test
The evaluation of the test results includes the following aspects:
➀According to the test matrix requirements, determine whether all the combina-
tions are veriﬁed completely;
➁According to the susceptibility criteria of sensitive equipment, assess whether
the working status and parameters in the record meet the requirements, take them
as the basis for compatibility of the test results;
➂If there is any disturbance in the mutual interference test when using ground
power supply, the internal battery power supply of the spacecraft should be used
for troubleshooting to avoid the impact of external ground equipment on the test
results.


11.3 Spacecraft System EME Compatibility Test
511
11.3
Spacecraft System EME Compatibility Test
The external EME of the spacecraft mainly refers to the signals from the TT&C and
tracking radars of the launch vehicle and at the launch site, also the EME between
the spacecraft in “multi-satellite launch” and formation ﬂying spacecraft, as well as
the compatibility veriﬁcation of spacecraft and ground EME.
11.3.1
EMC Test of Spacecraft and Launch Vehicle/Launch
Site
The spacecraft EMC with the launch vehicle and the launch site needs to be veriﬁed
before acceptance at the AIT factory and launch. For the ﬁrst launched spacecraft,
following special tests such as joint rehearsal at the launch site should be arranged:
(1) The interference test of the spacecraft’s TT&C signals and the unintentional
radiated signals on the launch vehicle receiver;
(2) The interference tests of the radiated signals from the launch vehicle, the upper
stages, and the launch site on the spacecraft receiver.
The criteria for the EME compatibility test between the spacecraft and the launch
vehicle and the launch site are mostly the EMC correlation curves and tables in the
vehicle manuals or the satellite–rocket interface documents; while the criteria for the
launch site test is mostly the satellite–rocket EMC rehearsal program or the related
technical documents for overall examination.
11.3.1.1
Spacecraft System Electric Field RE Test
The spacecraft system electric ﬁeld RE test is usually aimed to obtain data at the
docking surface between the spacecraft and the launch vehicle. For example, the EM
radiation requirements of the LM-3A in China’s famous Long March series launch
vehicles on the satellite–rocket separation plane are shown in Fig. 11.4 and Table
11.5:
(1) During the test, the spacecraft is generally powered by internal batteries to
eliminate the inﬂuence of the external power lines on the test results;
(2) The EMC measuring antenna is usually placed 1 m from the satellite–rocket
docking surface (the AF of the measuring antenna is 1 m); attach importance
to the coverage of the receiving antenna’s 3 dB beam, increase the measuring
position if necessary; refer to the installation position of the receiving antenna
of the launch vehicle for the speciﬁc measuring azimuth and height;
(3) It is recommended to customize the spacecraft band-stop ﬁlter of the transmit-
ting frequency band and the band-pass ﬁlter of the receiving frequency band


512
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.4 Diagram of EM radiation requirement of LM-3A launch vehicle
Table 11.5 EM radiation
requirement of LM-3A
launch vehicle
Frequency (MHz)
Field strength (dBµV/m)
0.01–550
134
550–750
15
750–1000
134
1000–1500
140
1500–1700
10
1700–5580
140
5580–5910
35
5910–40000
140
to protect the measurement receiver and reduce the nonlinear fake signal and
improve the test accuracy; the known strong signals should be suppressed during
outﬁeld tests;
(4) Before testing in the shielding enclosure, the environment data of key frequency
bands should be collected; in outﬁeld test such as at the launch site and on the
tower, the environment data of the corresponding frequency band should be
monitored synchronously, and the inﬂuence of external interference on the test
result should be analyzed;
(5) If the signal measured in the receiving band of the launch vehicle does not
conform to the limit requirement, the interference sources shall be found out
one by one and the corresponding protective measures shall be implemented;
(6) If the interference signal still exceeds the interface document requirements after
processing, the satellite–rocket interface EM data should be coordinated, or a
desktop joint test veriﬁcation is prepared for as required.


11.3 Spacecraft System EME Compatibility Test
513
EMI receiver
RF filter bank
Receiving Antenna
Spacecraft
LNA
Fig. 11.5 Block diagram of spacecraft RE test
Fig. 11.6 Diagram of a satellite system RE test
The spacecraft system RE test ﬂow is shown in Fig. 11.5.
Figure 11.6 shows the diagram of a satellite system RE test.
11.3.1.2
Spacecraft System Electric Field RS Test
The launch vehicle may transmit signals with large transmission power from
telemetry, space-based TT&C, etc. at the launch state. The spacecraft must be able to
withstand the EMI from such signals at its launch state. For example, the transmis-
sion signal requirement proposed by a certain launch vehicle is 2.2–2.3 GHz, and the
transmission power is 10 W. According to the conversion, the design margin must
be increased correspondently. The spacecraft is set to the launch state for the electric
ﬁeld RS test in the frequency band of 2.2–2.3 GHz and electric ﬁeld strength of


514
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.7 Block diagram of system RS test
15 V/m, while all spacecraft subsystems normally transmit and receive commands.
The interference to the spacecraft is closely monitored to assess the interference
immunity capability of the spacecraft in this frequency band. The test is as shown in
Fig. 11.7.
It is recommended to conﬁgure a harmonic ﬁltering network for the ground power
ampliﬁertopreventtheharmonicsignaloftheampliﬁerfromfallingintothereceiving
band of the spacecraft and causing unexpected interference or damage (Fig. 11.8).
Fig. 11.8 RS test of the Sino-European satellite


11.3 Spacecraft System EME Compatibility Test
515
11.3.1.3
Veriﬁcation of Satellite–Rocket Compatibility
in the “Multi-satellite Launch” System
In Chap. 5, the EMC analysis methods of the “multi-satellite launch” system are
addressed.
The spacecraft in “multi-satellite launch” state shall verify its compatibility with
the launch vehicle respectively, that is, the compatibility with the launch vehicle
using the system electric ﬁeld RE and RS test methods described above shall be
veriﬁed for each spacecraft.
11.3.2
Inter-spacecraft EMC Test Veriﬁcation
11.3.2.1
Inter-spacecraft EMC Veriﬁcation in Launch State
The “multi-satellite launch” state is shown in Fig. 11.9.
In the launch stage of “multi-satellite launch”, the operation of each satellite
mainly involves the power supply and distribution, attitude control, data management
subsystems, and the TT&C receiver and transmitter. The compatibility between the
radiation transmitting and receiving equipment is the main issue among spacecraft.
Because of the difference between various development organization and their
geographical locations of the “multi-satellite launch” spacecraft, it is often at the
launch site that they are ﬁrst converged. The spacecraft interfaces need to be coordi-
nated, including the communication of joint rehearsal items such as RE and RS tests.
That is, the EM interface relationship between each spacecraft should be coordinated
Fig. 11.9 Diagram of ESA
system launch with double
Ariane (Sylda)
5)OLQNV
Umbilical cableV
IRUWRZHU
RF cables
8PELOLFDO
FDEOHVIRUWRZHU


516
11
Spacecraft System-Level EMC Test Veriﬁcation
in advance by using their EM emission and EM susceptibility data. Since the worst
case is that all spacecraft are working in the same fairing simultaneously, the test
veriﬁcation will use the analysis data of this working condition for reference. The
spacecraft veriﬁcation matrix is shown in Table 11.6.
Assume that the three spacecraft A, B, and C are launched by one rocket. The
TT&C frequency bands and receiver’s electric ﬁeld RE limits are shown in Table
11.7:
During the test and veriﬁcation, the electrical testers set the spacecraft in the
launch state, and the EMC testers detect the electric ﬁeld RE of the spacecraft. The
block diagram of test principle and limit settings are the same as those in Sect. 11.3.1,
the focus should be put on the EM emission data on the frequency band speciﬁed in
Table 11.7, to determine if the EMC requirements are satisﬁed.
The inﬂuence of the fairing on multi-satellite compatibility is mainly its impact on
the TT&C communication, which can be veriﬁed by the TT&C docking test between
the satellite and rocket.
11.3.2.2
In-Orbit Operating Spacecraft Compatibility Test
The EMC veriﬁcations between in-orbit operating spacecraft generally include two
cases, one is for formation ﬂying spacecraft, the other is for spacecraft that need to
rendezvous and dock in space, such as space stations.
1. Compatibility veriﬁcation for formation ﬂight spacecraft
Table 11.6 Veriﬁcation matrix among “multi-satellite launch” spacecraft
Veriﬁcation object
Spacecraft 1
Spacecraft 2
…
Spacecraft N
Spacecraft 1
/
\sqrt
\sqrt
\sqrt
Spacecraft 2
\sqrt
/
\sqrt
\sqrt
…
\sqrt
\sqrt
/
\sqrt
Spacecraft N
\sqrt
\sqrt
\sqrt
/
Table 11.7 Examples of electric ﬁeld RE limits for “multi-satellite launch” in the launch segment
Frequency band (MHz)
Limit requirement (dBµV/m)
Description
1500–1600
10
Navigation and positioning
frequency band
2030–2034
30
Spacecraft A TT&C receiving
frequency band
2045–2049
35
Spacecraft B TT&C receiving
frequency band
2054–2058
35
Spacecraft C TT&C receiving
frequency band


11.3 Spacecraft System EME Compatibility Test
517
According to the design requirements, the distance between in-orbit formation ﬂying
spacecraft is used by analytical data plus margin as the reference limit for EMC
interface veriﬁcation, as described in Chap. 5.
This test is done by using the same methods as the electric ﬁeld RE and RS tests
described in Sect. 11.3.1.
2. Rendezvous and docking spacecraft
Spacecraft that need to rendezvous and dock in space are required to undertake RF
compatibility veriﬁcation. If possible, the relevant spacecraft modules should be
placed in the EMC chamber for actual RF compatibility measurement. All EUTs
in the spacecraft system should be set to the in-orbit working state, including the
motion of the scanning antenna.
Since it is difﬁcult to achieve the spacecraft docking layout in the EMC chamber,
the EM interface method can be used to check mutual compatibility. The test method
is the same as that of the electric ﬁeld RE and RS test.
11.3.3
Compatibility Test Between Spacecraft and Ground
EME
LEO spacecraft are likely to be interfered with by ground EMI signals. For example,
the US National Oceanic and Atmospheric Administration’s meteorological satellites
NOAA-11 and NOAA-12 had repeatedly received false commands when ﬂying over
Europe in 1991. The ground controllers found these false commands in time and dealt
with them properly without causing serious consequences. The ground controllers
conﬁrmed that the false commands were due to the satellite’s susceptibility to civilian
VHF signals widely used in Europe, which was the EMI to the spacecraft by the VHF
signals in the ground EME. In order to verify the compatibility of the spacecraft with
the ground EME, the ground signal that may cause interference should be estimated
according to the receiving frequency band of the sensitive equipment during in-orbit
ﬂight, and compatibility veriﬁcation for the spacecraft system should be performed
based on the estimated frequency, ﬁeld strength, and other data.
Figure 11.10 shows the possible ground interference signals to the in-orbit
operating spacecraft.


518
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.10 Possible ground interference signals to the in-orbit operating spacecraft
11.4
EMC Margin Veriﬁcation for Critical Electronic
Equipment
11.4.1
Deﬁnition of Critical Electronic Equipment
and Margin Requirements
According to the impact severity on the mission caused by spacecraft failure,
spacecraft products can be classiﬁed into three categories:
(1) Category I—those may cause the planned launch delay or serious damage to
spacecraft, or reduce its lifetime, loss of function and major ﬂight malfunctions,
such as the pyrotechnic device, power conditioning unit (PCU), TT&C receiver,
central control unit, antenna controller;
(2) Category II—those may cause degradation of spacecraft functions, including
loss of any autonomous operation capabilities;
(3) Category III—those may cause damage to nonessential functions.


11.4 EMC Margin Veriﬁcation for Critical Electronic Equipment
519
Margin, also called “safety margin”, is one of the important parameters to evaluate
the EMC of a system. It is the ratio of the susceptibility threshold of the system
critical equipment to the actual interference value, and can be expressed as
Md B = Sd B −Id B
(11.4.1)
where MdB stands for the system margin, SdB stands for the susceptibility threshold
of the system, and IdB is the actual EMI value of the system.
(a)
When SdB > IdB, MdB > 0, the system is considered to be compatible;
(b) When SdB \approxIdB, MdB \approx0, the system is considered to be in a critical working
state;
(c)
When SdB < IdB, MdB < 0, the system may be considered incompatible.
The conformity should be veriﬁed by tests, analysis, or a combination thereof. In
engineering consideration of the uncertainty in testing and analysis, a 6–10 dB will
be added on the above MdB value to further increase the compatibility margin of the
system.
Conducted and radiated interference coupling paths are available for electronic
equipment, so conducted and radiated EMC margins are also available.
11.4.2
Electronic Equipment EMC Test Acceptance
11.4.2.1
General Requirements for Electronic Equipment EMC Test
Acceptance
Spacecraft shall perform environmental tests under different requirements at different
development stages. According to the model development process, qualiﬁcation tests
are carried out in the proto ﬂight model stage, and acceptance tests are carried out in
the ﬂight model development stage.
For the EMC tests, all the emission and susceptibility items should be tested on
the qualiﬁcation test units, and the test margin should be implemented according to
Sect. 11.4.1. For ﬂight model units, EMC acceptance tests are performed. For models
with moderate EME complexity, the ﬂight model EMC acceptance test generally
only covers the emission items, not includes the susceptibility items. For models
with complex EME, according to the EMC analysis requirements, acceptance tests
on susceptibility items shall be carried out on the ﬂight model units, and the test
margin is required to be at least 3 dB less than that of the qualiﬁcation test to prevent
potential damage to the ﬂight model product.
In the model development, it is possible that the identiﬁcation unit is put into
production later than the ﬂight model. In this case, the EMC qualiﬁcation test should
be performed on the electrical test unit for information collection, and the test results


520
11
Spacecraft System-Level EMC Test Veriﬁcation
of the electrical test unit and the product design are used to guide the design of the
ﬂight model.
If the ﬂight model unit is modiﬁed on the basis of the qualiﬁcation test unit for
technical reasons, the relevant modiﬁcation measures shall be implemented on the
identiﬁcation test unit to reverify all the test items.
11.4.2.2
Electronic Equipment EMC Test Acceptance Methods
Equipment EMC test acceptance refers to the approval of its EMC test results. The
EMC test results can prove whether the EUT satisﬁes the EMC standards, and the
speciﬁc out-of-standard frequencies and values are also given for those EUTs that do
not meet the standards. Analysis of EMC test results can help to identify the cause
of EMC damage and the impact paths of the unexpected EM emissions to various
sensors, and also helps to evaluate the extent to which the sensors are affected under
various working conditions as well as the effectiveness of the technical measures
taken in the development process. The speciﬁc acceptance analysis method is as
follows:
(1) For products with transmitting functions (including the local oscillator emis-
sions from various transmitters and receivers), it is necessary to verify its
unwanted emissions (transmissions other than the useful signals), i.e., the EM
noise and unwanted signals generated by the product itself and harmful to infor-
mation transmission, and compare them with the limits and the required margin
to determine if they meet the requirements. If the emission levels at some
frequency points are higher than the line of limit, it is deﬁned as some test
items of the EMC standards that are not passed. Such transmission may be
a spurious emission at a single frequency or multiple frequencies, or an out-
of-band emission due to the modulation process. EMC reinforcement may be
implemented when necessary.
(2) For products with sensitive circuits, their immunity to EMI must be tested. The
higher the sensitive, the lower the immunity is to EMI. There are many types of
EMIs, including transients, pulses, spikes, shock pulses, clicks by their wave-
forms. In general, different interferences are generated by the corresponding
analog interference sources, which can be tested and veriﬁed by applying the
speciﬁed standard method to the equipment.
(3) For the equipment and subsystems that cannot implement EMC requirements
during the acceptance, it is required to analyze the data and prepare an analysis
report: for the emission test items that do not meet the requirements, analyze the
interference source and its coupling path; for the susceptibility test items that do
not meet requirements, test its susceptibility threshold and analyze the strength
of conducted and transmitted interference in its EME. The person in charge of
the equipment and subsystems should request for relaxation of requirement and
concession of use in the form of a report. The EMC engineer should analyze
the request report and instruct the system-level EMC test for veriﬁcation; if it


11.4 EMC Margin Veriﬁcation for Critical Electronic Equipment
521
does not constitute an unacceptable impact on system performance, the EMC
engineer shall submit a written proposal to the chief engineer for approval.
11.4.3
Margin Veriﬁcation for Critical Electronic Equipment
The EMC margin veriﬁcation for critical electronic equipment is performed during
the test phase of the equipment development to ensure that the margins meet the
requirements speciﬁed in the model EMC speciﬁcation/technical requirements or the
corresponding standard speciﬁcations. The critical electronic equipment has different
EM susceptibility characteristics. The speciﬁc EME of the spacecraft should be
considered when performing corresponding test veriﬁcations of the conducted and
radiated margins.
11.4.3.1
Pyrotechnic Devices
An important component of the pyrotechnic device is the electric initiation device,
whose EMC margin should be no less than 20 dB. The pyrotechnic device and its
lead are installed outside the module, which is more sensitive to high-power radiated
interference from the transmitting antenna. Therefore, the focus of veriﬁcation is the
radiated margin. There are mainly three ways of veriﬁcation.
Assume that the RS limit of the electric ﬁeld environment of the pyrotechnic
device given in the model speciﬁcation/technical requirements is 20 V/m.
(1) According to the deﬁnition of the EMC margin, if the pyrotechnic device should
meet the margin requirement of 20 dB, it is necessary to apply a ﬁeld strength
of 20 V/m + 20 dB = 200 V/m to verify whether the pyrotechnic device is
interfered. If it is not interfered, it is veriﬁed that the system meets the margin
requirement of 20 dB.
(2) Apply an interference 20 V/m to the pyrotechnic device as required to conduct
the RS test, and measure the induced current It on the leads. The It measurement
can use the ﬁber-optic temperature measurement method, which has both high
test accuracy and stability. If the normal initiation current of the pyrotechnic
device is IMNP, the radiated margin is calculated as 20lg

IMNP
It

dB, and if
20lg

IMNP
It

> 20, the EMC margin requirement is satisﬁed.
(3) Method-to-increase-susceptibility: If the non-ignition current of the pyrotechnic
device is 1 A under normal working state, it is reduced to 100 mA (100 dBuA)
after subtracting the 20 dB margin. Then, apply a 20 V/m as required to the
pyrotechnic device to conduct the RS test, and replace the original 1 A fuse
with a 100 mA fuse to observe its response in real time. If the fuse is not blown,
the pyrotechnic device can reach the 20 dB margin.


522
11
Spacecraft System-Level EMC Test Veriﬁcation
11.4.3.2
Satellite-Borne Receiver
The satellite-borne receiver is more sensitive to electric ﬁeld RE, especially the radi-
ated interference signal in its receiving frequency band is easy to cause degradation
of its receiving performance. Therefore, the RE EMC margin in the receiving band
of the satellite receiver should be paid more attention, which should be \geq12 dB. It
can be veriﬁed by the following two methods.
Assuming that the receiver susceptibility is −105 dBm, the environmental ﬁeld
strength is 20 V/m outside the receiving band and 30 dBuV/m within the receiving
band.
(1) According to the deﬁnition of margin, if the receiver should meet the margin
requirement of 12 dB, the ﬁeld strength to be applied should be as following:
20 V/m + 12 dB = 79.4 V/m outside the receiving band and 30 dBuV/m + 12 dB
= 42 dBuV/m within the receiving band. Set the susceptibility of the receiver
to −105 dBm and monitor the receiver for interference. If it is not interfered
with, it is veriﬁed that the system meets the 12 dB margin requirement.
(2) Method-to-increase-susceptibility: provided that the applied ﬁeld strength is
unchanged (20 V/m outside the receiving band, 30 dBuV/m within the receiving
band), increase the receiver susceptibility to −105 dBm−12 dB =−117 dBm,
monitor the receiver for interference. If it is not interfered, it is veriﬁed that the
system meets the margin requirement of 12 dB.
11.4.3.3
Power Conditioning Unit
The power conditioning unit is a core equipment of the spacecraft power supply
subsystem, and its operation reliability directly affects the power supply security of
the spacecraft. The power conditioning unit is generally installed in the module, and
the EM radiation environment is relatively satisﬁed. However, because it is connected
to the power supply equipment such as the solar array, the battery, and the distributor,
the conducted interference on the power line is relatively worse, so the keystone is
to verify its conducted margin.
Refer to the power quality speciﬁcation/standard for the quality of the power
bus where the power conditioning unit is located. Assuming that a certain model
of power bus ripple is \leq600 mV, if it is to meet the 12 dB margin requirement for
Category I critical equipment, it is necessary to apply a 600 mV + 12 dB = 2.4 V
ripple interference to the power conditioning unit to verify it by CS101 test method,
and applied voltage limit value is 128 dBµV (2.4 V). During the test, monitor the
response of the power conditioning unit. If it is not interfered with, it is veriﬁed that
the system meets the 12 dB power line conducted a margin requirement.


11.4 EMC Margin Veriﬁcation for Critical Electronic Equipment
523
11.4.3.4
Traveling Wave Tube Ampliﬁer
Spacecraft electronic equipment such as the traveling wave tube ampliﬁer has the
low-voltage protection feature. When other equipment in the system are powered on
and startup, a large surge current is generated, which will cause a transient voltage
drop on the power line, resulting in the low-voltage protection equipment shutoff
or incompatible operation. For such equipment, the key point of veriﬁcation is the
transient conducted interference margin on the power line.
The implementation of related switch transient requirements can refer to
Sect. 6.3.2.
11.4.4
Spacecraft System EMC Margin Veriﬁcation
According to the deﬁnition of the margin, the system EMC margin can be tested by
an increased EME level method. As long as the system susceptibility threshold is
conﬁrmed to satisfy SdB \geqIdB + MdB, it can be determined that the system meets
the margin requirements, where SdB is the susceptibility, IdB is the EMI, and MdB is
the margin.
In the spacecraft system-level EMC margin test, it is not possible to cover the
susceptibility margin of each position in the system. The EMC status of the entire
spacecraft system can be determined by only testing the susceptibility margins of the
critical equipment in the system.
Combining with the engineering characteristics of the spacecraft system, the
following three methods are applicable to spacecraft system-level EMC margin tests:
(1) Increasedsusceptibilitymethod:subtractthesystemEMsusceptibilitythreshold
by the speciﬁed margin, so that the SUT is more sensitive to interference. If the
system performance does not deteriorate, it is veriﬁed that the system meets the
margin requirement;
(2) Comparison method: under the condition that the interference equipment in the
system is working, measure or evaluate the conducted interference at the critical
interface and the radiated interference at the installation place of the system
equipment, then determine the margin by comparing the measured results with
thesusceptibilitythresholdmeasuredinthelaboratoryforthesystemequipment.
It is not feasible to measure the susceptibility threshold of critical equipment at
each frequency point. For susceptibility test items, if the EUT is not interfered
with, the susceptibility limit in the test is directly used to calculate the margin
as the EMC test susceptibility threshold.
(3) Incremental method: When the interference source is working, measure the
maximum interference signal at the critical interface, then apply an interference
signal added with the speciﬁed margin to the system and observe the response of
the system equipment. If the system performance does not worsen, it is veriﬁed
that the system meets the margin requirement.


524
11
Spacecraft System-Level EMC Test Veriﬁcation
Both the conducted and radiated EMC margin tests can be realized by the above
methods. To perform the EMC margin test, the test system should consist of
three modules: an environmental-interference level acquisition module, a target-
level conversion module, and a target-level injection module. The function of the
environmental-level acquisition module is to quickly measure the EME interference
level at the measured point, including multiple sampling to obtain the maximum peak
value of the actual interference signals; the function of the target level conversion
module is to convert the EMI level into the target data signal (IdB + MdB), including
the correction of the test system, etc.; the function of the target level injection module
is to apply the target level to the critical points of the system.
11.4.4.1
Veriﬁcation of Conducted Margin
The block diagram of the conducted margin test is shown in Fig. 11.11.
For spacecraft systems, the timing of conducted margin test is when the sidewalls
of the spacecraft are not installed. The test method is to collect the spectrum data of
the input cables of critical equipment, including the conducted interference current
or voltage of 10 kHz–400 MHz on the power line and the signal line; then add the
required margin value to this data, and apply it to the corresponding power line and
signal line by CS101 and CS114 interference injection method, and monitor the
performance parameters of the satellite during this process to conﬁrm whether the
satellite is interfered. If it is not interfered with, then the system is veriﬁed to meet
the margin requirement, otherwise not.
If the interference injection test method is not used, the comparison method may
be used to estimate the conducted margin of the system. The steady-state ripple of
the conducted interference of a certain type of power bus is taken as an example. The
System critical 
equipment
Receiving device
Monitor 
probe
Monitor 
probe
Data recording device
Signal generator 
Power amplifier
Injection 
probe
Injection 
probe
Interconnecting 
cable
Fig. 11.11 Principle block diagram of conducted margin test


11.4 EMC Margin Veriﬁcation for Critical Electronic Equipment
525
Fig. 11.12 Waveform for
ripple test at the power input
of the infrared camera
manager on a satellite
Table 11.8 Margin estimation by comparison method
Test position
Measured ripple
peak–peak value
CS101 test limit for
the infrared camera
manager
EMC margin
Infrared camera manager
622 mV(115.9
dBµV)
126 dBµV
10.1 dB
ripple interference waveform at the power input end of the infrared camera manager
to be tested on this bus is shown in Fig. 11.12.
The estimated margin using the comparison method is shown in Table 11.8.
11.4.4.2
Radiated Margin Veriﬁcation
The block diagram of the radiated margin test is shown in Fig. 11.13.
Spacecraft SUT
Receiving device
Data recording device
Signal simulator
Power amplifier
Receiving antenna
Transmitting 
antenna
Fig. 11.13 Principle block diagram for radiated margin test


526
11
Spacecraft System-Level EMC Test Veriﬁcation
For spacecraft systems, the timing of the radiated margin test is when the space-
craft is in a wireless test state. The processes of the test are as follows: First, use
RE102 test method to collect the EM RE environment of the critical equipment on the
spacecraft; then use RS103 method to apply the acquired data plus margin, monitor
the performance parameters of the satellite during the process of applying interfer-
ence, and conﬁrm whether it is interfered. If it is not interfered with, the system is
veriﬁed to meet the margin requirement, otherwise it does not.
Combining with the EM characteristics of the critical electronic equipment, it is
possible to verify the radiated margin more easily by using the incremental method
and the increased susceptibility method. Now, we take the satellite-borne receiver as
an example.
Incremental method: The satellite-borne receiver is more sensitive to interference
in the receiving band, so the radiated margin is veriﬁed in the receiving band. First,
the noise level of the RF receiving band is measured, the obtained maximum noise
level is 80 dBµV/m, plus the system margin of 6 dB, the total interference is 86
dBµV/m, which is converted into 0.02 V/m. The RS test of the RF receiving system
is carried out according to the ﬁeld strength of 0.02 V/m, and the margin is veriﬁed.
The test curve is shown in Fig. 11.14.
An easier way is the increased susceptibility method. Assuming that the suscep-
tibility of the receiver in the normal operating state is −100 dBm, in order to verify
its margin, the susceptibility of the RF receiver can be increased when the external
EME and the operation state are unchanged. If the required system margin is 6 dB,
the susceptibility of the receiver is increased to −100 dBm −6 dB = −106 dBm. The
receiver susceptibility can be improved by adjusting the AGC level and the ground
control uplink signal, which means to reduce the AGC level by 6 dB.
Fig. 11.14 Interference applied in the receiving band of the satellite-borne receiver for radiated
margin test


11.5 Special System-Level EMC Test
527
11.5
Special System-Level EMC Test
11.5.1
Spacecraft Compensated Compact Range Payload
PIM Test
11.5.1.1
Overview of PIM Testing
In the 1960s and 1970s, there were several cases in which communication satel-
lite failures occurred due to the inﬂuence of PIM products. For example, the PIM
products of the 3rd order of FLTSATCOM (US Fleet Communications Satellite),
the 13th order of MARISAR (US Maritime Satellite), the 43th order of MARECS
(European Maritime Satellite), and the 27th order of IS-V (International Communi-
cation Satellite-V) fell into the receiving pass-bands and caused interference, which
once affected the development progress and utilization of some spacecraft systems.
In order to ensure the normal operation of the communication system and the
smooth communication transmission, research on PIM issues is imperative.
11.5.1.2
Satellite-Level Measurement Method
The satellite-level measurement method refers to the measurement of the PIM gener-
atedbythewholesatelliteafterthegeneralassembly.AlthoughthePIMofthesatellite
components and subsystem have been veriﬁed to meet the estimated speciﬁcations
during the development process, the satellite contains several subsystem cascades,
most of which have strong or weak nonlinearities, so even if all the subsystem PIM
indicators meet the requirements, the satellite-level PIM may still have problems;
moreover, during the general assembly process of such a large system, the techno-
logical level and interference between the systems will all cause the PIM to change.
Therefore, in order to identify the inﬂuences and locations of the PIM on the payload
or satellite platform and try to troubleshoot, it is necessary to use more sensitive
antenna probe to detect the PIM sensitive parts on the satellite, thus to ensure the
normal and reliable operation of the satellite in orbit (Fig. 11.15).
Satellite under test
Filters
Low noise amplifier
Spectrum analyzer
Receiving antenna 
Fig. 11.15 Principle block diagram for entire-satellite-level measurement method


528
11
Spacecraft System-Level EMC Test Veriﬁcation
11.5.1.3
Compensated Compact Range PIM Test
1. Compensated compact range PIM test principle
To test the inﬂuence of the PIM component that is outside the noise spectrum of the
payload pass-band, the compensated compact range transmitting device transmits
twouplinksignalsofdifferentfrequencies,whichreachthesatellitereceivingantenna
through the compensated compact range dual reﬂector system via the compensated
compact range transmitting feed source. The satellite transmits two downlink signals
of different frequencies, which reach the compensated compact range receiving feed
source through the compensated compact range dual reﬂector system, and received
bythecompensatedcompact rangereceivingdevice. Inorder toimprovethedetection
accuracy of PIM component, the signals are output by the spectrum analyzer on IF,
and ampliﬁed by the IF ﬁlter, then sent to the power meter for detection. The block
diagram of the compensated compact range radiated PIM detection system is shown
in Fig. 11.16.
2. Test procedure
➀Set the transmitting power of the uplink signal source according to the link
estimation, so that the satellite ampliﬁer works at the back-off level required
for test (e.g., 15 dB back-off);
➁The frequency synthesized signal source 1 and 2 output two carrier signals of
the frequencies f 1 and f 2, respectively, their corresponding satellite downlink
frequencies are f 11 and f 22, respectively;
➂Gradually increase the carrier signal power, so that the transponder channels
corresponding to the two carriers are in a saturated state;
Communication satellite payload
Transmitting
 antenna
Downlink 
Coupler 
Test system 
Uplink 
Coupler 
Transponder 
Fixed 
attenuator
Receiving 
antenna
IF 
signal
Spectrum 
analyzer 
Compensated 
compact range 
receiving feed 
source 
Power meter
IF filter 
amplifier
compensated 
compact range 
transmitting 
feed source
Frequency 
synthesized 
signal source 1 
Frequency 
synthesized 
signal source 2
Power 
synthesizer
Fig. 11.16 Block diagram of the compensated compact range radiated PIM detection system (for
detecting the effects of PIM components outside the noise spectrum of the payload pass-band)


11.5 Special System-Level EMC Test
529
➃The spectrum analyzer at the compensated compact range receiving feed
source receives the satellite downlink signal power with the frequency of f 11
and f 22. Then, use the power meter to measure the IF signal power that is
down-converted by the spectrum analyzer and output via the ﬁlter ampliﬁer.
➄The spectrum analyzer at the compensated compact range receiving feed
receives the part of PIM component f PIM = \pm mf 11 \pm nf 22 that falls into
the receiving band, where m and n are integers. Then, use the power meter to
measure the IF signal power that is down-converted by the spectrum analyzer
and output via the ﬁlter ampliﬁer. By comparing the downlink power corre-
sponding to fPIM with the downlink signal power, the interference of the PIM
component can be determined.
3. C-band PIM test items
The C-band PIM calculation frequency is shown in Table 11.9, and the test results
are shown in Fig. 11.17.
4. Ku-Band PIM test items
See Table 11.10 and Fig. 11.18.
5. Veriﬁcation tests
Transmitting: connect the signal source to the standard gain antenna through the
uplink cable, and replace the satellite transmit antenna to transmit the downlink
signal.
Receiving: the whole satellite payload EIRP test link is used.
The downlink estimation is shown in Table 11.11.
The C-band and Ku-band veriﬁcation test noise spectrum are shown in Fig. 11.19
and Fig. 11.20, respectively.
It can be seen from Fig. 11.19 and Fig. 11.20 that the compensated compact range
PIM test system noise spectrum in the C-band and Ku-band is below −88.5 dBm
and −83.5 dBm, respectively, while the entire satellite noise spectrum in the C-band
and Ku-band are −71.7 dBm and −72.6 dBm, respectively, which indicates that the
compensated compact range system meets the entire satellite PIM test requirements
dynamically.
6. Summary
The compensated compact range PIM test system does not directly test the PIM
products, instead, it directly tests the PIM signals that fall into the receiving band
and outside the receiving noise spectrum, which can truly reﬂect the impact of the
PIM product on the transponder system. If there is no PIM product or the PIM
effects are submerged in the transponder’s noise spectrum, the transponder system
will not be affected. At present, the compensated compact range PIM test is still at
a relatively preliminary stage. It is necessary to collect more test data in the future


530
11
Spacecraft System-Level EMC Test Veriﬁcation
Table 11.9 C-Band PIM calculation frequency
Downlink f1/(MHz)
Downlink f2/(MHz)
PIM/(MHz)
PIM
frequency/(MHz)
Uplink f1/(MHz)
Uplink f2/(MHz)
PIM downlink
frequency/(MHz)
Input power
(OBO)/dB
3470
4160
3 * f1 – 1 * f2
6250
6455
6385
4025
0 dB


11.5 Special System-Level EMC Test
531
Fig. 11.17 C-Band PIM test results
and further analyze the measurement accuracy and test capability of the current PIM
measurement system, to ensure that the test results can provide more accurate data
for model development.
11.5.2
Electric Propulsion Ignition State Entire Satellite
EMC Test
For EMC veriﬁcation between the satellite-borne propulsion system and the satellite,
the most direct way is as follows: install the electric propulsion system on the satellite,
power it on to normal operation, and monitor the satellite’s working state so as to
determinetheimpactoftheelectricpropulsionsystemonthesatelliteEMC.However,
due to the requirements for vacuum and low-temperature working environment of
the electric propulsion system, there will be special requirements for the entire test
site environment and test equipment.
Figure 11.21 shows a schematic diagram of the entire satellite EMC test of an
electric propulsion ignition state. In order to meet the requirements of the vacuum
and low-temperature environment for the normal operation of the electric propul-
sion system, the whole satellite is placed in a vacuum low-temperature tank after the


532
11
Spacecraft System-Level EMC Test Veriﬁcation
Table 11.10 Ku-Band PIM calculation frequency
Downlink f1/(MHz)
Downlink f2/(MHz)
PIM/(MHz)
PIM
frequency/(MHz)
Uplink f1/(MHz)
Uplink f2/(MHz)
PIM downlink
frequency/(MHz)
Input power
(OBO)/dB
12300
12708
4 * f1 – 5 * f2
14340
14050
14458
12590
0


11.5 Special System-Level EMC Test
533
Fig. 11.18 Ku-Band PIM test results
Table 11.11 Downlink estimation
Frequency
(GHz)
Signal source
(dBm)
Insertion loss
(dB)
Antenna gain
(dBi)
EIRP (dBW)
Whole satellite
EIRP (dBW)
3.968
−18
−8.23
19.98
−6.25
42.3
12.525
10
−14.83
19.3
14.47
53
electric propulsion system is installed on the satellite. During the test, the tank is vacu-
umed and maintained in the low-temperature environment to meet the requirements
of the normal operation of the electric propulsion.
In order to reduce the contamination to the inner wall of the tank by the plume
generated during the electric propulsion operation, an anti-sputter target is installed
in the FOV of the plume beam, which means that the plume is radiated onto the
anti-sputter target to avoid its effect on the vacuum tank.
During the test, the conducted compatibility between the electric propulsion
system and the satellite is veriﬁed mainly by monitoring the changes in the functions
and performance of the satellite subsystems when the whole satellite is in normal
operation. The satellite subsystems are powered on and operate normally, then the
equipment of the electric propulsion system are powered on, and switched to different
working modes to verify the operation of the satellite subsystems and equipment in
each transient and steady state. On the other hand, the electric propulsion subsystems


534
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.19 C-Band veriﬁcation test noise spectrum
Fig. 11.20 Ku-Band veriﬁcation test noise spectrum


11.5 Special System-Level EMC Test
535
Fig. 11.21 Schematic of
electric propulsion system
test in vacuum tank after
installed on the satellite
are powered on and operated normally to verify whether the other subsystems and
equipment of the satellite will affect the normal operation of the electric propulsion
subsystems during power on and off, working modes switching and stable operations.
On the one hand, in terms of radiated compatibility, the characteristic changes
of the communication signal after passing through the plume are required to be
tested. According to the theoretical analysis, the greater the density of the plume
plasma generated by the electric propulsion system, the harsher the impact on the
communication signal. Therefore, it is necessary to test the impact of the electric
propulsion system on the communication signal in different working conditions.
Generally, because the TT&C antenna adopts an omnidirectional design, it is very
likely that its beam will overlap with the plume, so the keystone of this test is the
impact of the plume generated by the electric propulsion system on the TT&C signals.
To this end, the beam directions of the satellite TT&C antenna and the ground antenna
can be adjusted so that the beams pass through the plume, then the impact of the
plume on the communication characteristics is evaluated by comparing the electric
propulsion at two states. e.g., different operating modes and non-operating, that
is, one state in which different density plumes are generated and the other state a
none-plume state.
In addition, the impact of RE during the electric propulsion operation on the satel-
lite RF payload is to be tested. The EM radiation generated by the electric propul-
sion and plume may directly reach the externally installed TT&C/communication
antennas and the feed source on the satellite, and inﬂuence the above systems. There-
fore, it is necessary to measure the EM radiation at external sensitive parts on the
satellite during electric propulsion operation. The antennas are usually installed at the
typical installation locations for the RF communication antenna feed to receive the
radiated spectrum generated by the electric propulsion and plume, and are analyzed
whether they will affect the communication frequencies commonly used on satellites.


536
11
Spacecraft System-Level EMC Test Veriﬁcation
Fig. 11.22 Diagram of
EMC test antennas
installation in electric
propulsion ignition state for
entire satellite EMC Test
An EMC test antenna can be set up at the satellite payload antenna feed location, as
shown in Fig. 11.22. The beam direction of the EMC test antenna should be the same
as that of the satellite feed beam, and the performance of the antenna in the module
must meet the requirements of the vacuum and low-temperature environment. The
polarization characteristics and frequency bands of the test antenna can be selected
according to actual needs. The test system shown in the ﬁgure includes four antennas,
one horizontal polarization test antenna of 1–18 GHz and three vertical polarization
test antennas of 1–18 GHz, 18–26.5 GHz, and 26.5 GHz–40 GHz, respectively.
The antenna in the module is connected to the ﬂange of the vacuum and low-
temperature tank wall through a waveguide, and is connected to the coaxial cable
through the waveguide convertor on the outer portion of the ﬂange. The coaxial
cable is connected with an attenuator or/and a ﬁlter and a preampliﬁer, ﬁnally to the
measurement receiver.
The test is conducted in an unshielded chamber by the following procedure:
(1) First, test the environmental EM radiation characteristics at the RF payload feed
position under the condition that neither the electric propulsion system nor the
satellite is powered on;
(2) Second, test the EM radiation characteristics of the satellite at the RF payload
feed position under the condition that the electric propulsion system is not
powered on while the satellite is powered on;
(3) Finally, test the EM radiation characteristics of the whole satellite at the RF
payload feed position under the condition that both the electric propulsion
system and the satellite are powered on.
Based on the test results of the above steps, and excluding the inﬂuence of the
environment and the satellite itself, the inﬂuence of the electric propulsion system
on the satellite RF payload is obtained.
Figure 11.23 shows the test curve in 26.5–31 GHz frequency band. From the test
results, the EM radiation of the electric propulsion meets the EMC limit requirements
in this frequency band. Relevant test data can be provided to satellite or payload


11.5 Special System-Level EMC Test
537
Fig. 11.23 Test result curve of 26.5–31 GHz frequency band in electric propulsion ignition state
entire satellite EMC Test
developers for data analysis of the impact of the electric propulsion on the payload
EMC.
11.5.3
System-Level Veriﬁcation of Large Spacecraft Such
as Space Stations
For large spacecraft systems such as space stations and those with large antennas, due
to their large size, it is impossible to place the entire system in the EMC chamber for
testing in the existing conditions. At present, equivalent or approximate substitution
methods are commonly used for EMC veriﬁcation of a large space system. For
example, a large deployable antenna cannot be tested in the deployed state in the
chamber, but its feed portion can be tested in the system EMC test. Importance can
be attached to the transmission and reception characteristics of the feed, and then its
EMI effects on the spacecraft system can be tested and analyzed.
For manned spacecraft and space stations where astronauts work and live, it is
required to consider the impact of EME on personnel, including the EME in and out of
the module and the comparison of the HERP (Hazard of EM Radiation to Personnel)


538
11
Spacecraft System-Level EMC Test Veriﬁcation
limits. In addition, extravehicular activity spacesuits are important equipment for
astronaut’s extravehicular activities, which require radiated compatibility veriﬁcation
according to the EME near the spacecraft and the space station, and conducted
compatibility veriﬁcation according to the power supply and signal characteristics
of the umbilical cable.
11.5.3.1
Fully Integrated Space Station/Module EMC Test
1. Critical system EMC test
The purpose of the EMC performance test of critical systems is to verify certain
system EMC performance that cannot be performed in the fully integrated space
station for all operation modes (such as the robot manipulator, turning mechanism).
The relevant EMC data will be collected during the system performance veriﬁcation,
then the EMC performance of critical systems are veriﬁed through analytical and
experimental simulation methods.
2. Desktop joint test and AIT phase EMC test
This test is mainly to verify the conducted EMC of the fully integrated space station
anddeterminethesafetymarginofconductedEMItoensurethatthenormaloperation
of the subsystem will not be affected by the conducted EMI from other subsystems.
The test objects in the desktop joint test phase are mainly the electrical interface
compatibility of the power distribution subsystem, wired LAN, and data management
subsystem. The test objects in AIT (Assembly, Integration, and Test) phase are the
power input ports of each critical sensitive subsystem, major communication links for
important ﬂight phases, important remote-control channels, and the various power
output ports of the fully integrated space station orbital module distributor.
3. EMC test with the launch vehicle in the launch phase
When the fully integrated space station is in the launch state, the EMC between the
space station and the launch vehicle is an important factor that must be considered.
Since the fully integrated space station and the launch vehicle are powered by their
respective batteries, there is no power connection between them, so the CE is not
considered in the EMC between the fully integrated space station and the launch
vehicle, only the RE will be tested, that is, to verify whether the electric ﬁeld RE
signal of the fully integrated space station will fall into the sensitive frequency band
of the launch vehicle’s RF receiver, and verify whether the RE signal of the launch
vehicle will interfere with the operation of the subsystems in the space station.
4. Self-compatibility test
The EMC between the subsystems of the fully integrated space station, also called
the self-compatibility of the fully integrated space station, refers to the compatibility


11.5 Special System-Level EMC Test
539
between various subsystems on the space station that contain electronic and electrical
equipment, including the thermal control, power supply, TT&C and communication,
propulsion and data management subsystems.
(1) Verify the compatibility between each subsystem of the space station in each
main operating state;
(2) Test and verify the compatibility of each subsystem under certain special oper-
ating modes (such as EMC-related ground uplink interference, failure mode,
and maintenance mode);
(3) Test and verify the compatibility of the astronaut system with the fully integrated
space station (including intra-vehicular and extravehicular);
(4) Obtain EMC test data of the core module in the rendezvous, docking, stopping,
evacuation, and various combined conditions, and provide input for subsequent
joint simulation.
The testing personnel should judge whether EMI occurs between the subsystems of
the fully integrated space station according to the changes of the monitored perfor-
mance parameters, and use EMC test equipment to locate and analyze the interference
sources and the coupling paths of interference.
11.5.3.2
Assembly EMC Analysis and Test
The purpose of the assembly EMC veriﬁcation is to verify the EMC performance of
the space station systems in a multi-module and multisystem state. Therefore, the
veriﬁcation of the space station must address the compatibility of rendezvous and
docking, the compatibility of each assembled state, and the compatibility with the
astronaut system.
Space station EMC analysis in the assembled state, such as frequency compat-
ibility analysis, antenna isolation analysis, extravehicular EME analysis, intra-
vehicular EME analysis (caused by extravehicular antenna radiation), should all
be completed in the assembled state.
First, EMC analysis and test should be conducted on the assembly units, including
the core module, the experimental module I, the experimental module II, the manned
spacecraftandthecargospacecraft,thespeciﬁcitemsmaybedeterminedbyreference
of the EMC analysis and test of the entire space station. Then, the assembly testing
and analysis are performed based on the analysis and test results of each assembly
unit.
1. Assembly EMC analysis
Based on the EMC analysis and test of the fully integrated space station, the following
analysis should be performed using the previous test data:


540
11
Spacecraft System-Level EMC Test Veriﬁcation
(1) Perform self-compatibility analysis between the assemblies according to the
simulation and actual measurement results of the fully integrated space station;
(2) Perform dynamic EMC analysis during rendezvous and docking according to
the simulation and actual measurement results in the rendezvous and docking
of the fully integrated space station;
(3) Perform compatibility analysis between the astronaut system and the space
station according to the simulation and actual measurement results of the fully
integrated space station.
2. Assembly EMC test
(1) Assembly conduction test
When conducting joint testing of multiple assemblies in the ATI hall, the EMC
conduction test on the interconnecting cables is simultaneously performed. This
test mainly focuses on the interface between each assembly unit and the systems
that are in grid-connected operation, such as the docking mechanism, 100 V grid-
connected power supply, and the intra-vehicular Ethernet system. The purpose is ﬁrst
to ensure the compatible operation of the assemblies in wired state, then to extract
the conducted interference data on the power line and the interconnecting cables.
At the same time, perform troubleshooting, failure locating, analysis, and solving of
possible conducted interferences.
(2) Assembly electrical test
According to the results of the assembly analysis, joint electrical tests shall be
performed on certain modules where radiated interference may occur so as to verify
the compatibility between the assemblies. If there are conditions, the EMC test in
the assembled state can be performed in a chamber environment by reference of the
previous rendezvous and docking simulation test in the EMC chamber. The electrical
assembly under test only needs to simulate the electrical performance of the inter-
ested equipment and the electrical boundary of the assembly, so not all equipment
are required to be installed.
11.6
Summary
The spacecraft system-level EMC test is a key program to verify the compliance of
the system’s overall EMC technical speciﬁcations, which requires the combined use
of analytical and testing methods, as shown in Fig. 11.24. In addition, it is neces-
sary to carry out hierarchical veriﬁcation according to the composition of spacecraft
electronic equipment to ensure the coverage of key EMC performance speciﬁcations.
With the increasing demand of spacecraft system-level E3 test and veriﬁcation,
new test methods are emerging, such as the Fast Fourier Transformation (FFT)
measurement method in emission tests and simultaneous multifrequency injection


11.6 Summary
541
Fig. 11.24 Diagram of the relationships between spacecraft EMC technologies
method in susceptibility tests, which will help to improve the coverage and efﬁciency
ofsystem-levelEMCtesting.Withthedevelopmentofnewmodelssuchasall-electric
(propulsion) spacecraft and nuclear-powered spacecraft, EMC technologies will play
an increasingly crucial and extensive role.


Bibliography
1. Gerke, Daryl, and William Kimmel. 2003. Military EMC and the Revival of EMC Systems
Engineering. In Interference technology, 2003 annual EMC guide. 99–105.
2. Gerke, Daryl, and William Kimmel. 2002. Focus on EMC in space. In Kimmel Gerke bullets
fall 2002. 2–3.
3. Gerke, Daryl, and William Kimmel. 2008. Successfully dealing with EMC in space systems
requires strong EMC engineering. In Interference technology.
4. Lukash, Jim, et al. 2004. Aerospace EMC at the centennial of ﬂight. In IEEE EMC symposium
2004 (Special Session MO-PM-WS-8). Workshop Notes, 258–301.
5. Sargent, Noel B., AI Solutions, Catherine C. Lewis. Manager’s role in electromagnetic
interference (EMI) control. NASA Glenn Research Center.
6. AIAA S-121A. 2017. Electromagnetic compatibility requirements for space equipment and
systems. American Institute of Aeronautics and Astronautics.
7. DEF-STAN-59-411 Part1. 2014. Electromagnetic compatibility part 1: Management and
planning.
8. ECSS-E-HB-20-07A. 2012. Space engineering. Electromagnetic compatibility handbook.
9. ECSS-E-ST-20C. 2008. Space engineering, electrical and electronic. European Cooperation
for Space Standardization.
10. ECSS-E-ST-20-07C. 2012. Space engineering, electromagnetic compatibility. European Coop-
eration for Space Standardization.
11. IEEE C95.1-1991. 1991. IEEE standard for safety levels with respect to human exposure to
radio frequency electromagnetic ﬁelds, 3 kHz to 300 GHz. IEEE Standard Board.
12. ISO 14302-2002. 2002. Space systems-electromagnetic compatibility requirements. British
Standard.
13. ITU-R S. 736-3. 1997. Estimation of polarization discrimination in calculations of inter-
ference between geostationary-satellite networks in the ﬁxed-satellite service. ITU Radio
Communication Assembly.
14. MIL-HDBK-237D. 2005. Electromagnetic environmental effects and spectrum supportability
guidance for the acquisition process.
15. MIL-HDBK-1512. 1997. Electro-explosive subsystems, electrically initiated, design require-
ments and test methods.
16. MIL-HDBK-1857. 1998. Grounding, bonding and shielding design practices.
17. MIL-HDBK-83575. 1998. General handbook for space vehicle wiring harness design and
testing.
18. MIL-STD-461G. 2015. Requirements for the control of electromagnetic interference charac-
teristics of subsystems and equipment. Department of Defense.
19. MIL-STD-464C. 2010. Electromagnetic environmental effects requirements for systems.
Department of Defense.
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9
543

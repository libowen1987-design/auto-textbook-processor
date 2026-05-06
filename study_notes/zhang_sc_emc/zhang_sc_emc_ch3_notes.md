# Zhang《Spacecraft EMC Technologies》第3章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 3. Electromagnetic Compatibility Management

Chapter 3
Electromagnetic Compatibility
Management
3.1
Overview of EMC Management Standards
The standards and manuals for EMC management mainly include:
(1) DEF-STAN-59-411
Part
1-2014,
Electromagnetic
Compatibility
Part1:
Management and Planning.
(2) MIL-HDBK-237D-2005, Electromagnetic Environmental Effects and Spec-
trum Supportability Guidance for the acquisition process.
DEF-STAN 59-411 Part 1 is the ﬁrst part of UK MOD’s EMC standards series.
It introduces EMC management and control from system-level to equipment-level
EMC design, risk control, personnel responsibilities, and testing. In the standard,
the chapter of the Roles and Responsibilities of EMC Management discuss the
requirement to clarify responsibilities, and stipulates the responsibilities and tasks of
systemEMCdesigners,equipmentEMCdesigners,andtheEMCworkinggroup.The
chapter of EMC Control Plan introduces the purpose and application, and discusses
the relevant contents.
MIL-HDBK-237D is the US DoD’s handbook on Electromagnetic Environment
Effects (E3) and spectrum supportability for the acquisition process. This hand-
book discusses the management work, purpose, and precautions in terms of E3 and
spectrum supportability for military equipment during different development phases,
including feasibility study, program, proto ﬂight model, ﬂight model and operation,
etc.
3.2
The Spacecraft EMC Management
The spacecraft system’s EMI control is a process of clarifying the technical require-
ments, implementing design measures, and continuously improving against the risks
exposed in veriﬁcation. Depending on different stages of development, the EMI
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_3
39


40
3
Electromagnetic Compatibility Management
risks should be identiﬁed as early as possible, and control measures should be imple-
mented hierarchically to ensure the pertinence and effectiveness of the design and
veriﬁcation. The EMC design should be integrated into the performance design of the
product, checked, and tracked through processes such as design review and test veri-
ﬁcation. A technical director should be designated to take charge of spacecraft EMC
management and given corresponding authorization to ensure the orderly perfor-
mance of the professional work. The core of EMC management is to control the
electrical interface compatibility. If not taken seriously, it may have an extremely
serious impact on the performance of the spacecraft and even the success of the
space mission.
In the EMC management, professional supervisors and developers from various
organizations should well communicate and coordinate regarding EM emissions and
susceptibility characteristics of the relevant equipment; propose technical require-
ments for the shielding effectiveness of the spacecraft module and the chassis, the
grounding resistance of the structure and equipment, and the EM interface control
between the electronic equipment according to the EME data that the spacecraft may
be in during the launch, on-orbit operation and recovery landing phases, thereby
ensuring that the organizational and technical management of EMC is fully imple-
mented through simulation analysis, program review, on-site inspection, and test
veriﬁcation.
(1) On the organizational management, an EMC technical supervisor should be
appointed for the speciﬁc spacecraft model, with clearly deﬁned responsibili-
ties. The responsibilities of the supervisor should include establishing an EMC
working group as needed to carry out the EMC related tasks, such as review
of the EMC Program (EMCP); analyzing reports, technical requirements, and
summary reports; organizing technical research on major EMI problems and
risk assessment on concession acceptance issues; conducting professional tech-
nical training for relevant personnel when necessary; supervising the EMC work
of the contracted units and their personnel through management activities, such
as technical document review, meeting review, and on-site inspection, so as to
ensure the EMI control measures are fully implemented.
(2) Onthetechnicalmanagement,accordingtothegeneralplanofthespacecraft,the
EMC designers should be clear about the electronic equipment conﬁguration,
principle, and the worst-case EME envelope during the life cycle; analyze the
EMI and susceptibility characteristic equipment and its coupling path; amend,
add to or subtract from, test items and limits in the EMC technical requirements
by referring to the common standards; carry out control tasks such as anal-
ysis, design, test, and veriﬁcation; evaluate the risks of productized and inher-
ited equipment in a new EME; and perform comprehensive EMC veriﬁcation
through equipment-level and system-level analysis, testing, or a combination of
both.


3.2 The Spacecraft EMC Management
41
Table 3.1 Main EMC management activities for spacecraft (DEF STAN 59-411 Part 1 Issue 2)
EMC management
activities
Large spacecraft,
complex EME
Medium and small
spacecraft, complex
EME
Medium and small
spacecraft, normal
EME
EMC and EME analysis
A
A
A
Compilation of EMC
control program
A
S
–
Appointment of EMC
designer
A
A
A
Appointment of EMC
technical supervisor
A
S
–
Establishment of EMC
working group
A
S
–
Compilation of EMC
technical requirements
and speciﬁcations
A
A
A
EM risk assessment
A
A
A
Compilation Testing
matrix and the program
A
A
A
Equipment-level EMC
test and report
A
A
A
System-level EMC test
and report
A
A
A
Evaluation of the impact
on EMC of the technical
status changes
A
A
A
Note A means applicable, S means suitable
In order to achieve system EMC, the relevant organizational and technical manage-
ment activities should be planned from the initial stage of the project according to the
scale of the spacecraft and the complexity of EME, so that EMC management covers
all levels of the system, subsystem, and equipment throughout the development
stages.
The main EMC management activities for spacecraft models are shown in
Table 3.1.
3.3
EMC Working Group
For spacecraft with complex EME, an EMC working group should be established
to guide the work of EMC supervisors at all levels and solve potential problems.
The EMC working group is generally established by the Project Ofﬁce at the initial
phase of the project. Members include user representatives and experts from various


42
3
Electromagnetic Compatibility Management
positions who are familiar with EMC, such as those responsible for the design,
production,testing,andtechnicalmanagementatspacecraftsystem,majorsubsystem
and equipment levels. The person in charge of the working group is also responsible
for ensuring that sufﬁcient information is obtained from manufacturers of various
equipment or subsystems as well as from system-level EMC management personnel,
including the technical requirements of the system EMC.
3.3.1
Responsibilities of the EMC Working Group
The EMC working group is responsible for review evaluation, supervising, and
guiding the EMC work, including:
(1) Assisting in the development of an EMC control plan;
(2) Assisting in the formulation of EMC requirements in Mission contract;
(3) Identifying system EMC issues during the full life cycle of the mission,
describing responsibilities and roles of the integrated team and its members in
the entire mission system, handling EMC issues, and decision-making process.
(4) Organizing EMC work reviews at various stages, and inviting EMC technical
experts, military representatives or users to participate;
(5) Assisting in the analysis and prediction research of EMC and estimating the
possible effects of E3;
(6) Assisting in the review of EMC designs, processes, and test documents;
(7) Assisting in the reporting of EMC results (design, test, analysis, and prediction);
(8) Organizing EMC technical exchange and training;
(9) Identifying potential EMC risks and design deﬁciencies and documenting and
ﬁling important decisions.
3.3.2
Tasks of the EMC Working Group
The main tasks of the EMC working group are to ensure that the performance degra-
dation caused by EMI to all electronic systems and equipment is minimized, the
balance between development progress and the cost-effectiveness of solving EMI
problems are considered, and optimized management measures are taken to enable
the spacecraft eventually meet the performance requirements.


3.3 EMC Working Group
43
3.3.3
Responsibilities of EMC Working Group
3.3.3.1
System-Level EMC Supervisor
The responsibility of the system-level EMC supervisor is to tailor the EMC standards
toensurethepertinenceandoperabilityofthespacecraft’sEMCdesign,development,
testing, and acceptance, including:
(1) Conducting system-level EMC analysis and design studies;
(2) Sorting EMC standards and developing system-level EMC technical require-
ments;
(3) Integrating the EM analysis, design requirements and improvement measures
of the system into the overall document and the overall design, so as to improve
the cost-effectiveness of solving EMI problems;
(4) Implementing work plan according to the overall mission, carrying out research,
calculation and simulation analysis of electronic equipment with potential EMI,
so as to solve the EMI problems and optimize the overall performance of the
system;
(5) Providing technical advice and guidance on EMI issues, and communicating
with EMC overall design departments on system and equipment levels;
(6) As the technical supervisor of the EM working group, coordinating the
recommendations and requirements of the EM supervisors in charge of each
equipment;
(7) Reviewing the equipment-level EMC design requirements, test programs, and
test reports, to ensure that the electronic equipment meet EMC requirements in
system integration;
(8) Summarizing the EMI problems and potential risks that may affect the overall
design of the system, and coordinating the EMI between the spacecraft and
larger systems and the EME;
(9) Drawing EMC conclusions between the spacecraft system/spacecraft and its
EME by testing, analysis, or a combination of both.
3.3.3.2
Equipment-Level EMC Designer
The equipment-level EMC supervisor is responsible for EMC-related work in EM
design, development, integration, installation, testing, and acceptance of relevant
equipment or subsystems, which includes:
(1) Establishing equipment-level EMC technical requirements, analysis reports, test
reports, and related supporting documents;
(2) Reporting the potential EMI problems to the EMC supervisors at subsystem,
system levels and the EMC working group, and maintaining effective communi-
cation with the project team, development department, design department, and
users;


44
3
Electromagnetic Compatibility Management
(3) Reviewing the equipment-level test reports, analyzing the causes of the out-of-
tolerance and predicting the impact on the system, and reﬂecting the relevant
acceptance or concession information in the overall EM performance report;
(4) Ensuring that the equipment being charged is compatible with its EME without
degrading its performance due to EMI;
(5) Ensuring that the equipment being charged does not degrade the performance
of other equipment or subsystems due to EMI;
(6) Cooperating with the system-level EMC supervisors to jointly analyze and
locate the common EMI problems if EMI problems occur among equipment;
(7) Proposing equipment improvement solutions to reduce or solve EMI problems;
(8) Providing design change information that may affect EM characteristics to
system-level EMC supervisors and the EMC Working Group.
3.4
EMC Control Program and Technical Requirements
EMC
3.4.1
Purpose of the EMC Control Program
The EMC Control Program is the top-level EMC management document in model
development and is a basis for all EMC work and planning.
The purposes for developing EMC control program are to predict the system EMI
problems at the initial stage of development, so that the management and engineering
technicians can take appropriate measures at the beginning according to the corre-
sponding requirements; to identify and control the EMI risk as early as possible,
and make EMC work an organic component of the spacecraft development; and to
achieve better cost-effectiveness while ensuring EMC of the spacecraft system.
3.4.2
Contents of the EMC Control Program and Technical
Requirements
Large spacecraft (such as manned spaceﬂight) have complex components, long on-
orbit cycles, and high development costs, which require effective methods to help
identify and control EMI risks. The EMC Control Program helps to guide devel-
opers to conduct EM risk analysis, reveal deﬁciencies in common standards and
speciﬁcations, assess the required resources, and deﬁne the responsibilities. Before
signing the development contract, the user/purchaser also needs an effective EMC
control program to ensure the implementation of the project. Therefore, the EMC
control program is a joint management tool for both the user and the development
department, and should be further reﬁned and improved with the development.


3.4 EMC Control Program and Technical Requirements EMC
45
The EMC Control Program generally includes the following contents:
(1) Technical description deﬁnes the purpose, interface, signal/data, and clock
block diagram of the platform, system, and equipment. Refer to relevant
technical documents;
(2) Applicability refers to the applicability status, for example, whether the EMI,
ESD, RADHAZ, PIM, etc., are applicable to the whole system and frequency
band. Explanations should be given if any item is not included;
(3) Requirement and the environment should be included in the document, both
at system-level and subsystem and equipment-level;
(4) Management and organization clariﬁes the need for project management and
organization to ensure implementation of EMI controls;
(5) Documentation ensures that standards and related documents are consistent
with EM requirements;
(6) Design strategy includes EMC risk assessment and preliminary EM risk
solution;
(7) EM veriﬁcation determines procedures for proving and guaranteeing EM
performance;
(8) Quality assurance procedures;
(9) Deﬁnitions and abbreviations in the EM control program.
The control program needs to be implemented in terms of both design and veriﬁcation
by corresponding EMC technical requirements. The EMC technical requirements are
derived from risk analysis and based on the perception of system EMI risks, which
is aimed to implement the speciﬁed control measures.
The EMC risk analysis basically includes:
(1) In terms of radiated interference, focusing on the analysis of intentional
transmissions inside and outside of the spacecraft, RF EME constituted by
the receiving equipment, unintentional local oscillators, and RF sensitive
equipment;
(2) In terms of conducted interference, focusing on the analysis of power quality
and interface signal characteristics; in which, power quality includes steady-
state and transient characteristics in time domain, audio and RF interference in
the frequency domain, and special interferences; interface signal characteristics
include parameters such as rise time, overshoot and timing jitter;
(3) Assessing whether the inherited and productized equipment can adapt to EME
of the new model;
(4) Determining the EMI margin and evaluating the safety of the power controller,
attitude control computer and EEDs, and the EM risks for mission-critical
equipment;
(5) Listing potential sources of EMI and sensitive equipment (serious levels);
(6) AnalyzingpossiblecouplingmodesandpropagationpathsbetweenEMIsources
and sensitive equipment;
(7) Evaluating the EMC work (development, production, testing, maintenance, and
training, etc.) of each subsystem and equipment.


46
3
Electromagnetic Compatibility Management
EME includes natural and man-made emissions, the frequencies of which range from
DC magnetic ﬁeld, electrostatic ﬁeld to radio communication, radar, infrared, and
laser frequency bands, usually not exceeding 40 GHz. In addition, EME also includes
normal operation, storage, and transportation stages. In development of electronic
equipment, it is necessary to consider the worst EME envelope that may be encoun-
tered, such as the required EMC performance in E3, ESD, passive intermodulation,
and micro-discharge.
As the basis for the development of EMC technical requirements, EME analysis
should be considered in equipment and system designs, the layout of equipment
(such as the minimum distance of interference and sensitive equipment), intentional
EM transmission, or ﬁeld strength of receiving equipment in frequency domain and
interference in time domain. In addition, special consideration should be given to the
environment generated by the equipment itself, for example, the modulation charac-
teristics of the transmitter should be accurately recorded to facilitate the simulation
of relevant signals in the sensitivity test of mission- and safety–critical equipment.
Some inherited and productized devices may increase the risk of incompatibility
due to differences in EME requirements or changes in particular speciﬁcations.
Emphasis should be placed on assessing productized equipment used for safety and
mission-critical functions, and reviewing the conformity with relevant design data
for risk control. The technical requirements for design and veriﬁcation should be
proposed based on EMC risk analysis.
The basic design requirements in EMC technical requirements are as follows:
(1) Determine the tailoring requirements for emission and sensitivity limits in
accordance with the spacecraft EMC risk analysis and standard speciﬁcations;
(2) Physical isolation measures in the equipment layout;
(3) Clarify methods of shielding, grounding, and bonding;
(4) Methods for equipment interconnecting, such as by wireless, cable or ﬁber, as
well as isolation principles for cables and waveguides;
(5) Considerations of both intentional and unintentional EM emission signals in
frequency planning;
(6) FortheEMIproblemtobesolved,itsimpactontheperformanceofthespacecraft
can be quantitatively analyzed by using necessary design tools and methods;
(7) EMC technical requirements should be speciﬁed according to special activities
(such as rendezvous and docking, astronauts extraterrestrial activity, and celes-
tial patrol exploration) to ensure the EMC performance of the system during the
lifetime;
Good EMC installation techniques, improved cable shielding efﬁciency, viable isola-
tion schemes, in-line ﬁltering, and carefully selected operating frequencies for new
equipment can all contribute to system EMC performance.


3.4 EMC Control Program and Technical Requirements EMC
47
Conformity of EMC technical requirements should be veriﬁed by testing and
experiments. The basic testing requirements are as follows:
(1) Describe the management relationship between testing and experiments;
(2) List the test criteria to be used;
(3) Explain the reasons for test items, and formulate corresponding requirements;
(4) Classify the requirements according to equipment-level, subsystem-level, and
system-level EMC testing;
(5) Describealltestproceduresandcontrolthecomplianceinallstagesfromproduct
development to testing;
(6) Describe the requirements for resources, such as models, functional test
equipment, test facilities, cables, simulators, loads, and software;
(7) Describe the functional performance requirements;
(8) Determine the failure procedure during the test;
(9) Describe the reporting procedure during and after the test.
Because of the particularity of EMI transmission and coupling, EMC test results are
difﬁcultly correlated with the equipment and subsystem levels with the system perfor-
mance. Therefore, products that pass the equipment-level EMC test only signiﬁcantly
reduce the risk of system EMI, the compatibility with the system after installation
cannot be guaranteed. It is for this reason that test requirements in EMC technical
requirements should include a series of tests and veriﬁcation procedures to prove the
EMC conformity, including veriﬁcations at equipment-level and system-level.
EMC testing of all equipment should be conducted in a certiﬁed laboratory. Before
testing, it is ensured that the functional performance meets test requirements. If the
functional performance is not met requirements after the EMC test, the relevant
failure conditions must be investigated and reported for evaluation of the impact
on the design and layout. Because some equipment EMC tests are conducted by
sampling, the test requirements should have a certain margin under the consideration
of the differences between technology and the products.
In addition, the quality assurance of the control program and technical require-
ments should also be considered during model development, including that:
(1) Each test item of the product must be implemented in accordance with standards;
(2) The performance should be tested and conﬁrmed before the veriﬁcation
measurement;
(3) The allowed deviation range should be identiﬁed on functions;
(4) The deviation concession procedure, if necessary;
(5) The test results depend on the conﬁguration should reﬂect the results of the ﬁnal
process drawing and change control.
Compromise of design requirements is usually based on known EME parameters.
But the EME will change during the mission cycle by using new technologies and
new systems, so the changes in the EME should be tracked and analyzed during the
lifetime to evaluate the possible risks.


48
3
Electromagnetic Compatibility Management
3.5
EMC Test Program and Report
3.5.1
EMC Test Program
Most of the tests in the EMC test program use standard methods. In order to ensure
the repeatability of the tests, it is necessary to be speciﬁed the conﬁguration of
the equipment under Test (EUT), power supply mode, characteristics of the analog
signals, and the performance of the related electromechanical load. The test program
usually includes the following:
(1) Detailed information of the EUT, such as power supply requirements, output
parameters, operating mode, electromechanical load, necessary functions of
the interface, connectors, and cables, size and weight, software and hardware
versions, and safety precautions during operation;
(2) Descriptionofthetestlayoutincludingcablelength,cabletype,paths,grounding
and bonding arrangement;
(3) Description of the test items and procedures to be used;
(4) Description of the modulation method required in the sensitivity test;
(5) The speed and duration of the scanning of the test equipment;
(6) Limit for each test item and degradation criteria for sensitivity tests;
(7) Isolation requirements for functional test equipment;
(8) Management, including the accreditation of the test laboratory, the fault proce-
dure during the test, whether supervision by the quality representative is needed
during the test, distribution of the test reports, dates of project start and end, and
the conﬁdentiality of the reports.
(9) Provide frequency analysis results for guiding the test and EMC requirements
for the launch vehicle.
3.5.2
EMC Test Report
The purpose of the EMC test report is to provide evidence for the contract, to demon-
strate that the equipment meets the requirements of the EMC test program, and to
provide proof of conformity.
The EMC test report shall include the product conformity test results provided by
the accredited laboratory which conducts the tests in accordance with the technical
requirements and test program. The report should also provide sufﬁcient technical
information and data to ensure that the tests cover typical operation states, has the
repeatability of data and phenomena under the same conditions, and provide technical
input for integrated analysis and veriﬁcation of complex spacecraft systems.


3.5 EMC Test Program and Report
49
The test report should have project identiﬁcation numbers, indicating which tests
were performed and whether there were any abnormalities in the test; check and
conﬁrm all the items one by one against the test program and detailed rules, and give
reasons if there is any deviation item; provide the necessary measurement equip-
ment calibration data to demonstrate the relationship between the test results and
the measurement limits; and provide the name list of persons who participate in the
tests.
The test report should at least include the following:
(1) The number of the EUT, including the serial number and the software version
used;
(2) In terms of the test, photos of the test layout, cable layout, bonding and
grounding, calibration date of the measuring devices, computer software
version, information of the measuring devices (measurement bandwidth, detec-
tion mode, scan rate, dwelling time, etc.), conformity of the test with the program
and the detailed rules, etc.;
(3) In terms of the test results, a summary of the test results, charts of test results
and limits, conclusions obtained from the test results, improvement measures
for the failed items, etc.;
(4) The dates on which the test begins and ends;
(5) Participants in the test, including supervisors of test engineers and accredited
laboratories, product representatives and quality management personnel;
(6) A unique identiﬁcation and records of the test laboratory.
Test reports should be distributed and archived, and under appropriate database
management.
Paper reports should be documented and archived. Electronic reports can support
the comparison of EM risk analysis and the results of other test items.
3.6
EMC Management in the Main Stages of Spacecraft
Development
Spacecraft development is generally divided into the following stages: feasibility
demonstration, scheme, Proto Flight Model (PFM) development, and ﬂight model
development. The content and depth of EMC management in each stage are different;
but the potential EMI problems should be identiﬁed and solved as early as possible.
3.6.1
Feasibility Demonstration Stage
The EMC management tasks during the feasibility demonstration stage mainly
include:


50
3
Electromagnetic Compatibility Management
(1) Conducting preliminary statistical analysis on the spectrum parameters of RF
equipment (including antennas) according to relevant provisions on spacecraft
performance, EMC requirements, and frequency management; and proposing
spacecraft radio working frequency bands and EM spectrum characteristics
control requirements according to the mission requirements;
(2) Identifying the E3 problems that should be considered during the system’s life-
time, including EMC, EMI, and EM-radiated hazards, analyzing the expected
EME in which the spacecraft will operate, and comparing the effects of E3 on
different options available for the spacecraft.
3.6.2
Scheme Stage
The main management tasks during the scheme stage:
(1)
Establish an EMC working group according to the development, carry out
EMC review at the time of design review, and exchange the difﬁcult problems
and improvement measures of EMI;
(2)
Formulate preliminary EMC technical requirements, including
➀Selecting and tailoring applicable EMC standards;
➁Proposing optimal installation layout guidelines for spacecraft subsystems
and equipment, especially antennas and cables;
➂Assisting the project team to prepare the interface requirements for EMC
between spacecraft and large systems such as launch vehicles, launch sites,
and ground monitoring stations.
(3)
Conduct a feasibility study on frequency resources and make risk assessments;
(4)
Carry out system-level E3 analysis for the spacecraft based on the EMC
parameters of the whole satellite, and present an analysis report. The analysis
may involve frequency analysis, inter-antenna coupling analysis, RF equip-
ment behavioral level simulation analysis, analysis of coupling between the
antenna/equipment housing and cables, analysis of deck shielding performance
and analysis of EMC characteristics of system-critical equipment;
(5)
Conduct E3 analysis for newly developed subsystems (electronic equipment)
or those with considerable technical status changes and propose basic EMC
design plans; conduct preliminary tests on engineering prototypes and submit
the test reports to the working group, and corporate them in the database;
(6)
Conduct E3 analysis for electronic equipment with complete inheritance and
little technical status change, and report the potential out-of-tolerance items to
the EMC working group.
(7)
Reﬁne requirements for all on-orbit conditions and related designs, e.g., system
(platform) antenna design, and conduct a technical review of the spacecraft
preliminary scheme.
(8)
Develop a preliminary EMC control plan.


3.6 EMC Management in the Main Stages of Spacecraft Development
51
(9)
Determine the test items and veriﬁcation requirements, and develop an EMC
test plan.
(10) Conduct necessary EMC technical training.
3.6.3
Proto Flight Model Development Stage
In the proto ﬂight model development stage, the EMC management focuses on imple-
menting the EMC Control Program and Technical Requirements, including EMC
designing, simulation testing to the equipment and subsystems, improving the design
against the problems exposed in simulation tests, conducting EMC test and veriﬁ-
cation of equipment-, subsystem-, and system-level products, reviewing EMC test
out-of-tolerance applications, organizing EMC system-level tests, test veriﬁcation of
satellite–rocket docking and the launch site.
The EMC management requirements in this stage:
(1)
Formulate EMC technical requirements: Determine the main EMC design
points in the proto ﬂight model stage; identify the limit requirements for CE,
CS, RE, and RS and items for veriﬁcation according to the inheritance differ-
ence of electronic equipment; determine the grounding and bonding require-
ments; initially determine the composition of the power supply and distribution
subsystem and the required equipment for transient interference suppression;
plan the structures of grounding/isolation wiring diagrams and the locations of
the load point of SPG; determine the traces of the power lines and signal lines
and the layout of equipment electrical connectors, as well as related shielding
protection measures; determine EMC test requirements for spacecraft systems
and methods of margin veriﬁcation;
(2)
Present periodic reports on the progress of frequency work and risk control;
(3)
Provide the required frequencies used inside the equipment of each subsystem
and the interface as the input for EMC analysis of the spacecraft system;
(4)
Consider the EMC requirements for grounding and bonding when determining
the production process and installation requirements;
(5)
Set the key factors of EMC risk control, participate in and review the EMC
part of the design review of critical equipment;
(6)
Carry out EMC designs for the electrical test unit and qualiﬁcation test unit
of newly developed electronic equipment according to the requirements of
system EMC technology;
(7)
Track the equipment and subsystem-level EMC tests, control, and check their
test status and working conditions.
(8)
Conduct analysis on the design margin according to the EME, and based on
the analysis results, give recommendations for improving the EMC design,
when the COTS equipment does not meet the EMC requirements, or the newly
developed equipment is out of tolerance in the test.
(9)
Analyze and summarize the EMI problems found in commissioning and
testing, prepare test programs and rules for EM self-compatibility tests, verify


52
3
Electromagnetic Compatibility Management
whether the requirements in the Mission Statement are met, and improve and
perfect the design plan. If the system is out of tolerance, its impact should be
analyzed and a reference opinion should be given for improving and perfecting
the system design.
(10) Comprehensively analyze the EMC performance of the spacecraft system and
summarize the EMC work in this stage.
3.6.4
Flight Model Development Stage
The EMC management requirements during the ﬂight model development stage:
(1)
Develop EMC technical requirements based on system-level EMC design and
the test points at this stage;
(2)
Analyze the compatibility of productized and fully inherited equipment with
the system EME, and arrange necessary supplementary tests;
(3)
Monitor the impact of newly added equipment and its change with design
status on the system EME, and conduct a corresponding veriﬁcation test;
(4)
Propose EMC analysis and testing requirements. It is not allowed, in principle,
to conduct a sensitivity test and experiment that exceeds the EME level on the
ﬂight model;
(5)
Continuously track EMC issues during product development and timely
conduct risk assessment and interference control;
(6)
Review the impact of the design of each subsystem of the spacecraft ﬂight
model on the system EMC, focus on the EMC-related problems found in the
proto ﬂight model development stage, and implement process supervision and
control on the corresponding improvement measures and plans;
(7)
Implement the system level EMC, and supervise the speciﬁc EMC require-
ments for structural design, production process and installation layout of the
sub-systems and the equipment ﬂight model;
(8)
Implement spacecraft system-level EMC tests (e.g., inter-system, intra-system,
RF leakage, and passive intermodulation tests) and submit test reports;
(9)
If the spacecraft does not meet the requirements of the launch vehicle, the
project team shall consult with the launch vehicle party, and the later shall give
a written proof of whether the out-of-tolerance affects the compatibility;
(10) Participate in joint testing of the spacecraft with large systems such as launch
vehicles, launch sites, and ground monitoring stations at the launch site, and
submit test reports; all test data are stored in the database form and shared by
each model.
(11) Aim at the EMC-related problems found in the proto ﬂight model development
stage, conﬁrm the implementation of improvement measures and plans in the
ﬂight model development stage;
(12) Carry out necessary EMC test veriﬁcation or analysis for equipment with
design changes;


3.6 EMC Management in the Main Stages of Spacecraft Development
53
Table 3.2 Feasibility of EMI
control measures in each
development stage
Scheme stage
Proto ﬂight model
stage
Flight model stage
PCB layout design
Unsuitable
Impossible
Logic sequence
planning
Unsuitable
Impossible
Grounding plans
Very unsuitable
Impossible
Filtering
Possible
Ferrite ﬁltering
only
Shielding
Possible
Cable shielding
only
Physical isolation
Difﬁcult
High cost
Transient
suppression
Possible
Very limited
Cable layout
Possible
Unsuitable
Connector
selection
Unideal
Impossible
(13) Complete equipment-level EMC tests according to the test items speciﬁed in
the EMC technical requirements;
(14) Determine the impact of this change on the equipment and the system
EME through tests or analysis, if the equipment status is changed (such as
replacement of components) after the EMC veriﬁcation test.
3.7
Summary of Main EMC Work in Each Development
Stage
The spacecraft EMC work requires implementing frequency control of the interfer-
ence sources, taking isolation measures for the coupling paths, and providing ﬁltering
and shielding protection for the interference sensitive equipment. These tasks need to
be implemented as early as possible with reference to Table 3.2 and further deepened
according to Table 3.3.
3.8
Summary
The spacecraft EMC management runs through the whole development process of
the product. Spacecraft with complex EM characteristics should be managed by
specialized technical personnel, and if necessary, an EMC working group should
be established. System-level EMC management personnel are responsible for EMI
analysis to assess possible risks, and develop EMC control programs and tech-
nical requirements based on the above analysis; equipment-level EMC management


54
3
Electromagnetic Compatibility Management
Table 3.3 EMC management in each stage of spacecraft development
No.
Item name
Feasibility
demonstration
stage
Scheme stage
Proto ﬂight model
stage
Flight model
stage
1
EMC
Working
group
Can be established
for large and
complex EM
payload spacecraft
EMC
coordination
between parties
of spacecraft,
launch vehicle
and launch site
2
EMC
analysis
Compare the
E3 effects of
different
schemes,
conduct
preliminary
EM spectrum
analysis, and
recommend
available RF
operating
frequency
bands
Analyze the
frequencies,
antenna coupling,
cabin shielding
performance,
simulation of RF
equipment on
behavioral level,
antenna and
equipment/cable
coupling, and
EMC critical
equipment
characteristics
Applicability
analysis for EMC
issues of
productized and
inherited
equipment,
margin and risk
assessment for
out-of-tolerance
equipment in
EMC testing
Improve the
EMC model,
replace design
data with test
and process
data, and
evaluate the
EMC margin
and risks
3
Technical
requirements
for EMC
design
Initially
sorting the
control
measures of
EMI and EM
radiated
hazards
Select and tailor
EMC standards
and propose
recommendations
on equipment,
antenna, and cable
layout
Determine CE,
CS, RE, and RS
limit requirements
on systems,
subsystems, and
equipment levels,
and identify
technical
speciﬁcations for
bonding,
grounding, and
isolation
Track and
control the EMI
problems
identiﬁed in the
proto ﬂight
model stage and
the EMC
characteristics
of the newly
added and
technical status
changed
equipment
4
EMC test
EMC test
programs, rules
and reports for
equipment in
technical research
System-level and
special (RF
leakage, launch
site, etc.)
equipment-level
EMC test
programs, rules,
reports, and
summary of EMC
issues
System-level
and special (RF
leakage, launch
site, etc.) EMC
test programs,
rules, reports,
and summary of
EMC issues


3.8 Summary
55
Fig. 3.1 V-Type representation of the product life cycle
personnel are responsible to breakdown the general EMC technical requirements
into equipment-level EMC design requirements and test programs, and to track
related design and veriﬁcation work. System-level EMC technicians are respon-
sible for summarizing the equipment-level EMC veriﬁcation reports, determining
system-level EMC-veriﬁed items and subjects, and completing system acceptance
testing.
The V-type presentation of the product life cycle is shown in Fig. 3.1.

# Zhang《Spacecraft EMC Technologies》第10章

> 本笔记基于 PDF 原文提取，100% 来源于原书内容。

## 10. EMC Test Verification of Spacecraft Electronic Equipment

Chapter 10
EMC Test Veriﬁcation of Spacecraft
Electronic Equipment
10.1
Description of Interpolations and Factors
in Computer-Based Test Software
In the EMC test veriﬁcation, some items can be implemented by computer-based
automation tests. In numerical calculations, the parameters of various sensor factors
and cable losses are calculated according to the linear interpolation method, as shown
in Fig. 10.1.
As shown in Fig. 10.1, assume that the values of the coordinates (xa, ya), (xb, yb),
and xc are known, the value of yc is calculated as
(yc −ya)/(yb −ya) = (xc −xa)/(xb −xa)
(10.1.1)
Assume that the values on either side of the equation are β, then
β = (xc −xa)/(xb −xa), β = (yc −ya)/(yb −ya)
(10.1.2)
yc = ya + β(yb −ya) = (1 −β)ya + βyb
(10.1.3)
Taking a cable as an example, if the insertion loss is known to be 1.1 dB at
500 MHz frequency and 1.3 dB at 1 GHz frequency, the insertion loss at 800 MHz
frequency is calculated as
β = (0.8 −0.5)/(1 −0.5) = 0.6
(10.1.4)
yc = 1.1 + 0.6 × (1.3 −1.1) = 1.22(dB)
(10.1.5)
Therefore, the insertion loss is 1.22 dB at the 800 MHz frequency of the cable.
In the EMC test software, most of the test results are converted into logarithmic
form, and then calculated by addition or subtraction, as shown in the following
© Beijing Institute of Technology Press and Springer Nature Singapore Pte Ltd. 2020
H. Zhang et al., Spacecraft Electromagnetic Compatibility Technologies, Space Science
and Technologies, https://doi.org/10.1007/978-981-15-4782-9_10
393


394
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Fig. 10.1 Example of test
factor calculation
X axis
Y axis
equation:
X = Xa + F
(10.1.6)
where X is the result of the software test in dB;
Xa is the reading on the measuring instrument in dB;
F is the compensation factor in dB.
Note: The insertion loss factor is generally positive, F > 0; the gain factor is
generally negative, F < 0.
10.2
Description of Parameter Settings of Bandwidth
and Step Size for Electronic Equipment EMC Testing
Electronic equipment EMC testing should use standard test methods and speciﬁed
parameters such as bandwidth, step size, and dwell time. For emission testing, the
measurement bandwidth setting is shown in Table 10.1. The swept frequency step
should be less than or equal to half the bandwidth; sometimes, in order to improve the
sensitivity of the test system, the measurement bandwidth will be reduced to ensure
that the test sensitivity of the system is at least 6 dB lower than the limit. Generally, in
thefrequencybandabove10kHz,itisrecommendedthatthemeasurementbandwidth
is no less than 1 kHz. For the susceptibility testing, the measurement step size should
be consistent with the standard requirements in the spacecraft operating frequency
band, as shown in Table 10.2. Note that the dwell time of the test should correspond
to the response time of the EUT in sensitive conditions.


10.3 Main Computer-Based EMC Test Methods
395
Table 10.1 Test bandwidth and measurement time for emission testing
Frequency range
6 dB bandwidth/kHz
Min. dwell timea, b, c/s
Min. measurement time
(analog measurement
receiver)
25 Hz to 1 kHz
0.01
0.15
0.015 s/Hz
1 kHz to 10 kHz
0.1
0.015
0.15 s/Hz
10 kHz to 150 kHz
1
0.015
0.015 s/kHz
150 kHz to 30 MHz
10
0.015
1.5 s/MHz
30 MHz to 1 GHz
100
0.015
0.15 s/MHz
>1 GHz
1000
0.015
15 s/GHz
Note aThe dwell time rule only applies to stepping EMI receivers and spectrum analyzers
bOptional scanning technology: for the spectrum analyzer of stepping EMI receivers, when the
maximum hold function is used, and the total scanning time is no less than the min. measurement
time speciﬁed above, multiple faster sweeps can be used
cFor FFT-based receivers, the dwell time should be larger than the repetition period of the pulse
interference signal
Table 10.2 Parameters for
susceptibility testing
Frequency range
Analog scans
max. scan ratea
Stepped scans
max. step size
25 Hz to 1 MHz
0.0333 f 0/s
0.05 f 0
1 MHz to 30 MHz
0.00667 f 0/s
0.01 f 0
30 MHz to 1 GHz
0.00333 f 0/s
0.005 f 0
1 GHz to 40 GHz
0.00167 f 0/s
0.0025 f 0
1 GHz to 18 GHz
GSFC-STD-7000A
0.00667 f 0/s
0.01 f 0
Note as is the time in seconds
10.3
Main Computer-Based EMC Test Methods
10.3.1
CE101 Power Leads Conducted Emission Test
This test can use computer-based test method. The components of the CE101
calibration and test system are shown in Figs. 10.2 and 10.3, respectively.
When performing the test system calibration, a 1, 3, and 10 kHz calibration signal
(sine wave) is applied to the current probe separately by a signal generator, with a
signal level at least 6 dB lower than the limit; check the current with an oscilloscope
and a resistor and conﬁrm whether the current waveform is a sine wave; the measure-
ment receiver scans in the normal operation mode to conﬁrm that the measured value
is within ±3 dB of the measured value of oscilloscope.


396
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Signal 
generator
Amplifier 
(As required)
Oscilloscope 
(high impedance)
Current probe
Date recorder
Measurement 
receiver
R
Fig. 10.2 CE101 test system calibration setup
EUT
LISN
LISN
5cm
50ΩLoad  
Power leads
50Ω Load
Current probe
Measurement 
receiver
Fig. 10.3 CE101 test system conﬁguration


10.3 Main Computer-Based EMC Test Methods
397
10.3.1.1
Relationship Among CE101 Measurement Data
During the test, the output voltage is read from the current probe, and the interference
current on the power lead is calculated according to the calibrated transfer impedance.
In practical measurement, the transfer impedance of the current probe is generally
obtained by calibration. Usually, the reciprocal of the transfer impedance is used and
its logarithm is taken. The relationship among the measured data can be written as
I = V + F + CL
(10.3.1)
where I is the interference current on the power lead in dBμA;
V is the reading on the receiver in dBμV;
F is the conversion factor of the current probe in dB (1/) or dBS;
CL is the cable loss in dB.
10.3.1.2
Selection of CE101 Current Probe Parameters and Precautions
The CE101 test uses a current probe as a sensor for measurement, which needs to
give attention to the units and parameters of its calibration data.
First, note that in the CE101 test, if the measured cable is connected through the
AP of a shielded chamber, there may be a 50 Hz induced operating frequency signal
in the part of the chamber, which may be coupled on the test cable through the ground
loop. It can be seen from the above equation that, for a given receiver reading and
cable loss, the larger the conversion factor F of the current probe, the higher the
background noise of the measurement system. Therefore, it is necessary to select a
current probe with a smaller conversion factor.
Second, the conversion factor of the current probe is classiﬁed into two types:
transfer admittance and transfer impedance; if transfer admittance is used as the
calibration data, a positive value should be taken; if it is a transfer impedance, a
negative value should be taken:
I (dBμA) = V (dBμV) + S[dBS or dB(1/)]
(10.3.2)
or I (dBμA) = V (dBμV) −R(dB)
(10.3.3)
Figures 10.4 and 10.5 show examples of the transfer impedance and transfer
admittance data of the current probes from two different manufacturers. Although
their units are different, as mentioned earlier, the two parameters are reciprocal, so
they can be directly inverted by each other.
It can be seen that the transfer impedance of Probe 1 is about −29 dB near the
50 Hz frequency, and the transfer admittance of Probe 2 is about 75 dB (1/) near
the 50 Hz frequency, so selection of Probe 1 helps to reduce the effect of the ground
loop on the test results.


398
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Transfer impedance (dB ohms)
Frequency
-13
-18
-23
-28
-33
-38
-43
10Hz
100Hz
1kHz
10kHz
100kHz
1MHz
10MHz
Fig. 10.4 Example of transfer impedance data of current probe 1
Current probe factor in db(1/Ω)
Frequency
10Hz
100Hz
1kHz
10kHz
100kHz
1MHz
10MHz
0Hz
100MHz
40
30
20
10
0
-10
-20
80
70
60
50
Fig. 10.5 Example of transfer admittance data of current probe 2
Therefore, whenconﬁguringtheCE101test system, thecurrent probewithsmaller
transfer admittance should be selected as much as possible. The test results are shown
in Figs. 10.6 and 10.7.


10.3 Main Computer-Based EMC Test Methods
399
Frequency/LOG
Amplitude (dBuA)
CE101-Submarine (DC)
Fig. 10.6 Example of test results for a probe with larger transfer admittance
Frequency/LOG
Amplitude (dBuA)
CE101 (GJB151B) applicable to submarine limit (DC)
Fig. 10.7 Example of test results for a probe with smaller transfer admittance
10.3.1.3
CE101 Calibration and Test Flow
The CE101 calibration and test software ﬂow are shown in Fig. 10.8 and Fig. 10.9,
respectively.


400
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, frequency, 
minimum signal output level, 
and close the signal output
Oscilloscope
Set the channels, 
impedance 1M
, reading 
mode RMS
Signal source
Turn on the signal 
output
Oscilloscope
Adjust the horizontal axis 
according to frequency and 
take the reading
Adjust the vertical axis 
according to the reading
Take the oscilloscope 
reading
Calculate the current value
Oscilloscope reading/resistance (1
)
and convert them to dBμA
Equal?
Calculate the limit at 
the calibration 
frequency-6dB
Signal source
Adjust the output level 
according to the difference 
with the limit
Signal source
Set the 
calibration
frequency
Receiver setting
Set the parameters, such as RBW 
starting frequency, ending frequency 
attenuation and reference level 
according to scan rules
Take the receiver 
reading
The
receiver’s
reading
Calculate the current value dBμA
Receiver readings on the calibration 
frequency dBμV + probe factor +
cable loss
Display the final results of 
calibration
Next frequency
End of 
Calibration
No
All equipment 
exit the program-
control (local)
Calculate the corresponding parameters 
of the probe factor and cable loss 
according to the reading
Fig. 10.8 CE101 calibration logics
10.3.2
CE102 Power Lead Conducted Emission Test
This test can use computer-based test method. The CE102 test system calibration
setup and the CE102 test system conﬁguration are shown in Figs. 10.10 and 10.11,
respectively.
The test system should be calibrated before testing. The signal generator outputs
a signal to the output of the LISN power supply at 10 kHz, 100 kHz, 2 MHz, and
10 MHz, respectively, and the level is at least 6 dB below the limit. At 10 and 100 kHz,
use an oscilloscope to conﬁrm that it is a sine wave and measure the signal RMS
level. The oscilloscope input impedance can be 50  or higher. At 2 and 10 MHz,
directly use the signal level output from the 50  signal generator. The measurement
receiver scans with the bandwidth, step size, and dwell time speciﬁed in Table 10.1


10.3 Main Computer-Based EMC Test Methods
401
Check equipment connection 
status, program-controlled 
initialization of all equipment
Test required 
frequency range
Receiver setting
Set the parameters, such as RBW 
starting frequency, ending frequency 
attenuation and reference level 
according to scan rules
Calculate the current value 
dBμA,
The receiver readings on the 
test frequency dBμV+probe
factor+cable loss
Display the test results
Next test 
frequency band
End of test
No
All equipment exit the 
program-control
(local)
Divide the segment of the tested span 
according to the RBW on different 
frequency bands, and give the starting 
frequency and ending frequency of 
each segment
Yes
Display the final test results
Calculate the corresponding 
parameters of the probe factor 
and cable loss according to 
the test frequency
Take the receiver 
reading
The receiver’s
reading
Fig. 10.9 CE101 test software ﬂowchart
Fig. 10.10 CE102 test
system calibration setup
Power input
(power off)
Type-T coaxial 
connector
Signal 
generator
Signal output port
Oscilloscope 
Measurement 
receiver
20dB attenuator
Only for 10kHz and 
100kHz calibration
LISN
Data 
recording 
device


402
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
EUT
LISN
LISN
20dB
50
Load 
Power leads
Signal output 
port
Attenuator 
Measurement 
receiver
Fig. 10.11 CE102 test system setup
to verify that the measurement is within ±3 dB of the injected signal level. The
correction factors include the 20 dB attenuator, the insertion loss of the 0.25 μF
coupling capacitor in the LISN.
10.3.2.1
Relationship Among CE102 Measurement Data
The basic principle of LISN is shown in Fig. 10.12. The CE102 measures the coupling
voltage at the 0.25 μF capacitor port of the LISN and estimates the interference
Signal output port
Power supply
50Ω load or the
50Ω input port of
the 
measurement 
receiver
50µH
8µF
0.25µF
EUT
5Ω
1kΩ
Fig. 10.12 Diagram of LISN principle and composition


10.3 Main Computer-Based EMC Test Methods
403
CE test port, 
built-in pulse 
limit protector
RE test port
Fig. 10.13 Schematic diagram of the input port of the EMI receiver
voltage on the power lead according to the correction factor of the LISN. The
relationship among the measurement data is
UR = Uc + F + CL + 20
(10.3.4)
where UR is the interference voltage on the power line in dBμV;
Uc is the reading of the receiver in dBμV;
F is the correction factor of LISN in dB;
CL is the cable loss in dB;
20 is the insertion loss of a ﬁxed attenuator in dB.
10.3.2.2
Precautions for CE102 Test
First, in the CE102 test, a 20 dB attenuator should be connected between the LISN and
the receiver to avoid overload or damage to the receiver when the 0.25 μF capacitor
is coupled to an excessively high interference voltage.
Second, note that many EUTs may generate excessive transient pulses at the
moment of power-on, and may cause overload or damage to the receiver. There-
fore, a time-division method can be adopted, in which the EUT is powered on before
connecting to the receiver. Besides, notice that all current EMI measurement receivers
have a dedicated test port with a built-in limit protector. The cable for CE measure-
ments should be connected to this port to better ensure the safety of the receiver
during CE testing (Fig. 10.13).
10.3.2.3
CE102 Calibration and Test Procedure
The CE102 calibration and test software ﬂow is shown in Fig. 10.14 and Fig. 10.15,
respectively.


404
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Fig. 10.14 CE102 calibration relationships
10.3.3
CS101 Power Lead Conducted Susceptibility Test
The CS101 test setup is shown in Fig. 10.16. The test sequence is arranged as follows:
ﬁrst, the EUT is powered on and warmed up to a stable operate state in no-interference
condition; select a power lead of the EUT for testing; then adjust the signal generator
to the lowest test frequency and gradually increase the signal level until the required
voltage limit or the veriﬁed power value (whichever is smaller), which is taken as
the required signal level. Keep the signal level no lower than the required signal
level, scan within the test frequency range, monitor the EUT for susceptibility; if
susceptibility occurs, determine the susceptibility threshold level. Finally, repeat the
above steps for the other power leads to be tested.


10.3 Main Computer-Based EMC Test Methods
405
Check equipment connection 
status, program-controlled 
initialization of all equipment
Test required 
frequency range
Receiver setting
Set the parameters, such as RBW 
starting frequency, ending frequency 
attenuation and reference level 
according to scan rules
Take the receiver 
reading
The receiver’s
reading
Calculation of voltage value 
dBμV
Receiver readings on the test 
frequency 
dBμV+ 
LISN 
factor + CL + attenuator loss 
(20)
Display the test results
Next test 
frequency band
End of test
No
All equipment exit the 
program-control
(local)
Divide the segment of the tested span 
according to the RBW on different 
frequency bands, and give the starting 
frequency and ending frequency of 
each segment
Yes
Display the final test results
Calculate the corresponding 
parameters of the LISN factor 
and cable loss according to 
the test frequency
Fig. 10.15 CE102 test software ﬂowchart
EUT
LISN
LISN
High potential line
Return line
Power
leads
Coupling
transformer
Power
amplifier
Signal
generator
Oscilloscope
(high
impedance)
Isolation
transformer
Excitation
and
monitoring
equipment
10 F
Fig. 10.16 DC power lead CS101 test system setup


406
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Special consideration should be made when performing CS101 tests because the
oscilloscope’s safety ground wire is disconnected and there is a risk of electric shock.
For the test conﬁguration shown in Fig. 10.16, a differential probe can be used for the
test. In this case, the oscilloscope is not supplied through the isolation transformer
while maintaining ground connection, thus electric shock hazard can be avoided.
However, note that the applicable voltage of the differential probe should be greater
than the supply voltage of the EUT.
Before testing, the test system needs to be calibrated. Adjust the signal generator
to the lowest test frequency, gradually increase the signal level until the oscilloscope
indicates that the voltage reaches the voltage level corresponding to the maximum
power limit, and check whether the output waveform is a sine wave. Scan within
the required frequency range and record the signal generator settings required to
maintain the power limit, the calibration process is completed.
ThepurposeoftheCS101testsystemcalibrationistoobtaintheoutputpowerlimit
ofthepowersourcewhenthespeciﬁedpowerlimitisreachedat0.5.Thecalibration
is generally performed according to the calibration curve deﬁned in MIL-STD-461G
(Fig. 10.17).
It can be seen from the limits speciﬁed by the standards that, in fact, the test is
an “OR” relationship, that is, the calibration is ﬁrst performed to obtain the output
value of the power source when the corresponding power limit is reached on the 0.5
 resistor, and then in practical testing, the interference voltage on the EUT power
lead is monitored in real time. When the interference voltage reaches the standard
limit or the output of the power source reaches the calibration limit, it is considered
having reached the speciﬁed limit as long as either of them satisﬁes the standards.
Frequency (Hz)
Limit level (W)
10
100
1k
10k
100k
1MHz
25
5k
150k
80
100
10
1
0.1
0.01
0.09
Fig. 10.17 CS101 calibration curve


10.3 Main Computer-Based EMC Test Methods
407
10.3.3.1
Precautions for CS101 Test
The CS101 limits include both power and voltage, and it is considered to meet
the standard requirements as long as either of the limits is met. During the CS101
calibration, the dissipation power value at each frequency point on the 0.5  standard
resistance and the voltage value across the resistor should be recorded according
to the standard regulation. The two values can be converted to each other on the
standard resistance. For example, the 80 W power corresponds to 6.31 V RMS
voltage, because the power cannot be directly measured or read at low frequencies.
Inordertofacilitatecalculationorsoftwareimplementation,thesoftwarewilldirectly
measure the voltage value rather than the power.
During the test, the output power is controlled by controlling the output level of the
low-frequency signal source, i.e., the input power of the audio ampliﬁer. Therefore,
the CS101 calibration records the output level of each frequency point of the signal
source, as shown in Fig. 10.18.
Attentionshallbepaidtothefollowingaspectsintheconnectionoftestequipment:
The CS101 test connection is shown in Fig. 10.19. The EUT is connected to
the power supply through the LISNs. The LF signal source output is connected to
the audio ampliﬁer. The interference signal is injected into the power lead of the
EUT through the coupling transformer. A 10 μF feedthrough capacitor is parallel-
connected between the positive and negative leads of the power lead, and the magni-
tude of the interference injected between the positive and negative leads is monitored
by an oscilloscope or a voltmeter. The 10 μF feedthrough capacitor forms a short
circuit for the injected signal, so that the injected interference signal only ﬂows to the
EUT not to the LISN, which not only prevents the power supply from interference,
Frequency /LOG
Received level (V)
Frequency /LOG
Output level (dBm)
Limit monitoring
Signal source output level monitoring
CS101 (151B) power limit
Fig. 10.18 Example of calibration curve for CS101 injection voltage and signal source output level


408
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Memory oscilloscope
Audio amplifier
Fibre-optical-LAN/GPIB converter
0.5 
precision resistor
Injection transformer
Fibre-optical 
connection line
Fibre-optical-LAN/GPIB 
converter
Control computer
Arbitrary waveform 
generator
GPIB control bus
Ω
Fig. 10.19 Example of CS101 test layout
but also improves the injection efﬁciency and avoids possible voltage division of the
injection signal at the LISN port.
(1) If an oscilloscope is used to monitor the injection voltage, note that it should be
supplied by a isolation transformer. Also, when using GPIB program-control, a
GPIB isolator should be used to avoid accidental grounding of the oscilloscope
due to grounding of the communication port. Because, during the test, if the
ground end of the oscilloscope’s single-ended probe is connected to the ground
of the oscilloscope, and the oscilloscope is grounded, it may cause the negative
or return line of the EUT to be grounded through the ground terminal of the
probe, which may affect the effect of the injection interference test. Therefore, it
is speciﬁed in the equipment-level EMC requirements that a differential probe
can be used to avoid the inﬂuence of the ground terminal. Here the voltage
parameters of the differential probe should be paid attention to.
(2) In the AC power supply interference test, because the interference signal is
superimposed on the AC power supply signal, and the AC voltage is much
higher than the amplitude of the injection voltage, generally it is necessary to
ﬁlter out the power supply voltage with a ﬁlter. However, note that the stopband
of the ﬁlter is very narrow. If the frequency of the actual power grid is deviated,
the power supply frequency may not be completely ﬁltered out, thus affecting
the test result. To this end, it is recommended to use a regulated power supply
to ensure the correct power supply frequency.


10.3 Main Computer-Based EMC Test Methods
409
10.3.3.2
CS101 Calibration and Test Procedure
The CS101 calibration and test software ﬂow is shown in Fig. 10.20 and Fig. 10.21,
respectively.
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave,
frequency, output level,
close the minimum signal 
output
Oscilloscope
Set the channels, impedance 
1MΩ, reading mode RMS
Signal source
Turn on the 
signal output
Oscilloscope
Adjust the horizontal axis 
according to frequency and 
take the reading
Adjust the vertical axis 
according to the reading
Take the oscilloscope 
reading
Calculation of the power
Oscilloscope reading2/resistance(0.5 )
Equal?
Required power 
value
Signal source
Adjust the output level 
according to the difference 
with the limit
No
Signal source
Set the calibration 
frequencies
Record
Output level of the signal 
source
Yes
Next frequency?
Yes
End of calibration
Close the output of the 
signal source
No
All equipment
Exit program-control
(local)
Does the power 
reach the max.
input level of the 
amplifier?
No
Display the calibration 
curve
Continue or stop test 
depending on the max. 
input level
Yes
Caution:
Turn on the 
power
amplifier and 
confirm
Oscilloscope
reading
Suddenly disappear
Fig. 10.20 CS101 calibration ﬂowchart


410
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, 
frequency, output level, 
close the minimum signal 
output
Oscilloscope
Set the channels, impedance 
1MΩ, reading mode RMS
Signal source
Turn on the 
signal output
Oscilloscope
Adjust the horizontal axis 
according to frequency and 
take the reading
Adjust the vertical axis 
according to the reading
Take the oscilloscope 
reading
Calculation of the voltage
Convert the reading into dBμV
Equal?
Calculate the limit at 
this frequency point
Signal source
Adjust the output level 
according to the difference 
with the limit
No
Signal source
Set the calibration 
frequencies
Record the monitored voltage 
and output level of the signal 
source
Yes
Next frequency?
Yes
End of test
Close the output of the 
signal source
No
All equipment
Exit program-control
(Local)
Is calibrated level 
reached
No
Display the test curve
Caution:
Turn on the 
power
amplifier and 
confirm
Oscilloscope
reading
Suddenly disappear
Yes
Fig. 10.21 CS101 test ﬂowchart
10.3.4
CS114 Bulk Cable Injection Conducted Susceptibility
Test
The CS114 test system setup is shown in Fig. 10.22. For EUTs with redundant cables
for safety reasons, such as multiple data buses, tests can be conducted by the way
of simultaneous injection using multiple cables. During the test, the EUT is ﬁrst
powered-up and preheated to a stable operating state. Adjust the signal generator to
10 kHz with 1 kHz pulse modulation, 50% duty cycle. Then, feed the forward power
determined by calibration into the injection probe while monitoring the induced
current and scanning within the test frequency range as required, and conﬁrm whether


10.3 Main Computer-Based EMC Test Methods
411
EUT
LISN
Injection probe
Measurement
receiver B
Monitor probe
Monitor probe
Injection probe
5cm
5cm
5cm
5cm
Interconnecting
cables
Power input
Actual or simulated loads and signals
Measurement
receiver A
Directional coupler
Signal generator
Amplifier
Use the dotted-
line paths when 
test the power 
line
Fig. 10.22 CS114 test system conﬁguration
the EUT performance is degraded. If susceptibility occurs, determine the suscepti-
bility threshold level. Finally, repeat the above test procedure for each bulk cable
connected to other connectors of the EUT.
Before testing, the test system needs to be calibrated. Adjust the signal generator
to 10 kHz but do not modulate; increase the signal level, and monitor the current
ﬂow through the center conductor of the calibration ﬁxture with the receiver A until
reaching the standard speciﬁed current; record the forward power that is fed into the
injection probe and measured by the receiver B; scan within the test frequency band
and record the forward power required to reach the speciﬁed current.
In the formal tests, the smaller one of the following two forward powers should be
taken: the forward power determined during the calibration and the forward power at


412
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
the moment when the monitored current is equal to the corresponding limit current
plus 6 dB.
10.3.4.1
Relationship Among the CS114 Measurement Data
The CS114 test system needs to be calibrated on a 50  calibration ﬁxture according
to the limit of CS114. By measuring the forward power of the directional coupler,
the output power of each frequency point of the power ampliﬁer can be obtained. In
the actual test, the output power of the power ampliﬁer is monitored and compared
with the calibration value, and the induced current value on the cable under test is
simultaneously monitored. If the induced current value is 6 dB higher than the limit
or the power ampliﬁer output power reaches the calibration value, it is considered to
meet the limit requirements.
The calibration of the CS114 is performed by measurement on a standard 50 
impedance ﬁxture. The relationship among the measurement data is as follows:
I = U + (−34) + CL + A
(10.3.5)
where I is the induced current on the cable under test in dBμA;
U is the receiver reading in dBμV;
CL is the cable loss in dB;
−34 is the converted value of voltage and current under 50  impedance, 20 lg50;
A is the attenuation of the attenuator in dB.
10.3.4.2
Precautions for CS114 Test
(1) When injecting a large current for testing, it is required to protect the
measuring equipment such as the receiver.
When performing Curve 5 calibration as shown in Fig. 10.23, the maximum injection
current value is 109 dBμA, and the output voltage of the calibration ﬁxture is 109 +
34 = 143 (dBμV). If the calibration is monitored by the receiver, an external 36 dB
attenuator is required to ensure that the maximum input power of the receiver port
does not exceed 0 dBm, or 107 dBμV. Therefore, an attenuator of 40 dB or above is
usually conﬁgured for CS114 Curve 5 calibration.
(2) The power measurement for different signal modulation methods
In the CS114 test, a continuous wave signal is commonly used in the calibration, and
a pulse modulation signal is used in the test. The signal is shown in Fig. 10.24.
When measuring the pulse modulation signal using a mean power meter, the
obtained result is the average power of the signal; but according to the standard
requirements, the test should be based on the peak power of the signal.


10.3 Main Computer-Based EMC Test Methods
413
Curve 5
Curve 4
Curve 3
Curve 2
Curve 1
Limit (dBµA)
Frequency (Hz)
80
70
69
60
50
40
30
120
110
100
90
57
49
43
37
97
85
77
71
65
89
83
109
100k
1M
10M
10k
100M
1G
400M
30M
Fig. 10.23 CS114 calibration curve
Fig. 10.24 Schematic
diagram of signal modulation
Pulse 
t
Generally, peak detectors are used for emission and susceptibility tests in the
frequency domain. A peak detector is used to detect the peak value of the modulation
envelope in the receiver’s passband. The receiver is scaled by using the RMS value
of a sine wave that can produce the same peak indication. When the measurement
instruments with other detection modes (such as oscilloscope, nonfrequency selective
voltmeter, or broadband ﬁeld strength meter) are used for susceptibility test, the test
values need to be corrected so that the readings are corrected to the equivalent of the
RMS of the modulation envelope peak. The correction factor can be determined by
comparing the detector’s response to signals with equal peak levels with or without
modulation.
Figure 10.25 shows the test of the pulse modulation signals in the average and
peak measurement states of the power meter.
Therefore, in the software test, the mean power drop caused by pulse modula-
tion, and additional corrections should be considered. Similarly, when measuring
the CS114 induced current, since the applied interference signal is also a pulse
modulation signal, which is a wideband signal, if a spectrum analyzer or a receiver
is used for measurement with different resolution bandwidths, the test results are


414
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(
)
10lg 10 40
6.02dB
=
= −
Average power
Pulse power
Duty factor
Function is set to ON
Average power 
=10lg(PW/PRI)
Pulse width
Pulse repetition interval
Fig. 10.25 Average and peak measurement test of the pulse modulation signal
different. Therefore, this error that may be caused by the resolution bandwidth needs
to be considered in the measurement. It is recommended to use the largest possible
resolution bandwidth for measurements.
The pulse modulation speciﬁed in the EMC speciﬁcation is 50% duty cycle, that
is, 10 lg (0.5) = −3 (dB).
10.3.4.3
CS114 Calibration and Test Procedures
The CS114 calibration and test software ﬂow is shown in Fig. 10.26 and Fig. 10.27,
respectively.
10.3.5
RE101 Magnetic Field Radiated Emission Test
The RE101 test system setup is shown in Fig. 10.28. During the test, the EUT is ﬁrst
powered-up and preheated to a stable operating state. Place a loop antenna 7 cm away
from the EUT surface or the electrical connector and parallel to the EUT surface or
the axis of the electrical connector. Set the measurement receiver to the required
bandwidth and measurement time, and scan within the applicable frequency range to
ﬁnd out the frequency or frequency band of the maximum radiation. Then, adjust the
measurement receiver to a predetermined frequency or frequency band, monitor its
output while moving the loop antenna (maintaining a distance of 7 cm) near the EUT
surface or the electrical connector, and scale the maximum radiation determined at


10.3 Main Computer-Based EMC Test Methods
415
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, 
frequency, output level, 
close the minimum signal 
output
Set the receiver
Set the power meter
Signal source
Signal output turn 
on
Receiver
Adjust the center 
frequency span and 
reference level 
according to the 
frequency
Take the receiver’s
max. reading
Calculation of current
Receiver’s reading+attenuation-34
Equal?
Calculation of the limit 
at this frequency point
Signal source
Adjust the output level 
according to the difference 
with the limit
No
Signal source
Set the calibration 
frequencies
Record
The output level and the power 
meter reading
Yes
Next frequency?
End of calibration
Turn off signal output, 
power amplifier set to 
Standby
No
All equipment exit 
program-control
(local)
Does the power 
reach the max input 
level of the 
amplfier?
No
Display the 
calibration curve
Continue or stop the test at 
the maximum input level
Yes
Power amplifier
Set to operate
Read the forward and reverse 
power on the power meter
Replace the 
current probe?
Replace the current 
probe and confirm
Yes
No
Is the reflected 
power or standing 
wave ratio 
excessive
Fig. 10.26 CS114 calibration ﬂowchart
each frequency. At a distance of 7 cm from the maximum radiation point, change the
directions of the loop antenna to obtain the maximum reading on the measurement
receiver and record it. Select at least two maximum radiation frequencies for each
octave below 200 Hz, and at least 3 maximum radiation frequencies for each octave
above 200 Hz. Repeat the above procedures. Finally, repeat the above test steps for
each surface of the EUT and each electrical connector.
During the test, the test system needs to be calibrated as follows. Apply a 50 kHz
calibration signal, with amplitude at least 6 dB lower than the difference between the
limit and the correction coefﬁcient of the loop antenna. Adjust the center frequency
of the measurement receiver to 50 kHz, record the measured level, and make sure
that the measured value of the test system is within ±3 dB of the injected signal
level.


416
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, 
frequency, output level, 
close the minimum signal 
output
Set the receiver
Set the power meter
Signal source
Signal output turn 
on
Read the forward and 
reflected power on the 
power meter
Equal?
Read the calibration 
injection power at this 
frequency
Read the 
maximum value 
of the receiver
No
Signal source
Set the 
calibration
frequencies
Add a 1kHz, 50% duty cycle pulse modulation 
and dwell a specified time, turn off modulation, 
record the monitored power and signal source 
output level
Yes
Next frequency?
End of test
Turn off signal output, 
amplifier set to Standby
No
All equipment exit 
program-control
(local)
Meet the max. 
current
requirement?
No
Display the test 
curve
Yes
Power amplifier
Set to operate
Replace the 
current probe?
Yes
Replace the current 
probe and confirm
Yes
Signal source
Adjust the output level 
according to the difference 
with the limit
Calculation
Receiver’s
reading+probe
factor
Read the probe factor 
at this frequency
Is the reflected 
power or the 
standing wave ratio 
excessive?
Yes
Fig. 10.27 CS114 test ﬂowchart
LISN
EUT
7cm
Power 
input
Receiving loop 
antenna
Measurement 
receiver
Fig. 10.28 RE101 test system setup


10.3 Main Computer-Based EMC Test Methods
417
10.3.5.1
Relationship Among RE101 Measurement Data
The magnetic ﬁeld radiated strength of the EUT is calculated by measuring the port
voltage of the magnetic ﬁeld antenna and using the antenna correction factor. The
relationship among the measurement data is
H = U + AF + CL
(10.3.6)
where H is the magnetic ﬁeld strength radiated by the EUT in dBpT;
U is the receiver reading in dBμV;
AF is the magnetic ﬁeld antenna correction factor in dBpT/μV;
CL is the cable loss in dB.
10.3.5.2
Precautions for RE101 Test
The RE101 test is required to cover different orientations of the EUT, including the
front, back, left, right, and top surfaces. Note that the antenna correction factor is
related to the distance, and ensure that the measurement distance is maintained at
7 cm.
10.3.5.3
RE101 Test Procedure
The RE101 test software ﬂow is shown in Fig. 10.29.
10.3.6
RE102 Electric Field Radiated Emission Test
The RE102 test system setup is shown in Fig. 10.30. For the test antenna, at the
range of 10 kHz to 30 MHz, a 104 cm rod antenna with an impedance matching
network should be used, the outer conductor of the signal output connector should
be bonded with the antenna matching network housing; if the impedance matching
network includes a preampliﬁer (active rod antenna), overload protection should be
taken into account; if a square counterpoise is used, each side should have a length
of at least 60 cm. At the range of 30–200 MHz, a biconical antenna should be used,
with 137 cm from tip to tip. At the range of 200 MHz to 1 GHz, a double-ridged horn
antenna should be used, with a typical opening dimension of 69.0 cm × 94.5 cm.
At the range of 1–18 GHz, a double-ridged horn antenna with a typical opening
dimension of 24.2 cm × 13.6 cm is used.
The test method is
(1) Conﬁrm that the environmental level meets the requirements;
(2) Power-up and preheat the test equipment to reach a stable operating state.


418
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Check equipment connection 
status, program-controlled 
initialization of all equipment
Frequency range 
required by the 
test
Receiver setting
Set the RBW staring frequency, end 
frequency attenuation and reference 
level parameters as specified by 
scanning
Calculation of the magnetic 
field strength dBpT
Receiver reading at the 
frequency dB
V+antenna
factor+cable loss
Display the test result
Next segment
End of test
No
All equipment 
exit program-
control (local)
Segment the test span according to 
the RBW of different frequency 
bands,
and give the starting 
frequency and the ending frequency 
of each segment.
Yes
Display the final test result
According to the test 
frequency
Calculate the corresponding 
antenna factor and cable loss 
parameters
Take the receiver reading
Receiver reading
Fig. 10.29 RE101 test ﬂowchart
120cm
80cm~90cm
1m
Boundary of the 
test setup
Ground plane
Antenna 
Fig. 10.30 RE102 test system setup


10.3 Main Computer-Based EMC Test Methods
419
(3) Perform the calibration evaluation of the test system. Evaluate the entire test
system from the antenna to the data output device at the highest working
frequency of the antenna; for the rod antenna with a passive matching network,
the evaluation is done at its center frequency of each frequency band; for
the active rod antenna, the evaluation is done at the lowest frequency, center
frequency, and the highest test frequency.
➀Apply a check signal to the coaxial cable at the antenna connection point,
the level being at least 6 dB lower than the difference between the limit and
the antenna coefﬁcient.
➁For the 104 cm rod antenna, remove the rod and apply a signal to the antenna
matching network via a 10 pF capacitor connected to the rod antenna base.
Do not use any calibration ﬁxtures or injection network.
➂The measurement receiver scans in the normal data scan mode, make sure
that the measured value is within ±3 dB of the injected signal level.
➃Use the antenna or stub radiator to radiate signals at the highest test
frequency of each antenna, adjust the measurement receiver to the applied
signalfrequency,checkwhetherthereceivedsignalisappropriate,andverify
that each antenna is in normal working condition.
(4) Power-up and preheat the EUT to a stable operating state.
(5) Perform RE measurement of the EUT and related cables. Set the measurement
receiver’s bandwidth and measurement time according to the requirements, and
scan within the applicable frequency range. The antenna adopts the vertical
polarization direction at 30 MHz or lower, and both horizontal and vertical
polarization at 30 MHz or above. Perform tests at each predetermined antenna
position.
During the rod antenna test, the antenna counterpoise is prohibited from being elec-
trically bonded to the ground plane. The shield of the rod antenna matching network
coaxial cable should be electrically bonded to the ground plane with the shortest
possible distance (the excess length is no more than 10 cm). A ferrite bead is placed
near the midsection of the coaxial cable between the antenna matching network and
the ground plane, and its impedance is 20–30  at 20 MHz.
In the RE102 test, attach importance to the test antenna position. For all arrange-
ments, the antenna should be 1 m away from the front edge of the test setup boundary
and 120 cm above the ground plate, to ensure that any part of the antenna is at least
1 m away from the wall of the shielded enclosure and no less than 0.5 m from the
ceiling. The number of antenna placements depends on the boundary size of the
EUT test conﬁguration, the number of sub-equipment contained in the EUT and the
antenna pattern. For the test below 200 MHz, the principle of antenna setting is that
if the test boundary width is not more than 3 m, the antenna is placed on the center
vertical line of the test boundary width; if the test boundary width is greater than
3 m, multiple antenna positions are selected, and the number of antenna positions
is obtained by dividing the test boundary width (in m) with 3 and rounded up to
the nearest integer. For the test between 200 MHz to 1 GHz, the number of antenna


420
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
placements should be sufﬁcient, so that the entire width of each EUT housing and
the ﬁrst 35 cm line segment of its terminated wire/cable are within the 3 dB lobe
width of the antenna. For the test at no lower than 1 GHz, the number of antenna
placements should be sufﬁcient, so that the entire width of each EUT housing and the
ﬁrst 7 cm line segment of its terminated wire/cable are within the 3 dB beamwidth
of the antenna.
10.3.6.1
Relationship Among RE102 Measurement Data
The electric ﬁeld radiated strength of the EUT is calculated by measuring the
port voltage of the receiving antenna and depending on the antenna factor. When
measuring the electric ﬁeld RE of the EUT, if a preampliﬁer is used, the inﬂu-
ence of the preampliﬁer gain on the measurement result should be calculated. The
relationship among the measurement data is as follows:
E = V + CL2 −GLNA + CL1 + AF
(10.3.7)
where E is the electric ﬁeld strength radiated by the EUT in dBμV/m;
V is the receiver’s reading in dBμV;
CL1, CL2 are the cable loss of the two cable sections in dB;
GLNA is the gain of the external preampliﬁer in dB;
AF is the antenna correction factor of the electric ﬁeld in dB (1/m);
Generally, the antenna factor and preampliﬁer gain use the calibration data in the
laboratory, and the cable loss uses the self-calibrated data in the laboratory.
10.3.6.2
Selection of RE102 Sensor Parameters and Precautions
The basic setup of the RE102 test is shown in Fig. 10.31.
RE102 is a regular EMC test item, in which not many measuring devices or
accessories are used, but several integration problems must be considered, and will
Antenna factor 
(AF)
EUT
Cable L1
Cable L2
Preamplifier gain GLNA
Noise factor (NF)
Background noise of the 
measurement receiver or 
spectrometer
1m
Fig. 10.31 RE102 test system setup


10.3 Main Computer-Based EMC Test Methods
421
be described from the aspects of the preampliﬁer, ambient noise and receiving system
sensitivity, respectively.
1. Preampliﬁer
The function of the preampliﬁer is to amplify the weak signals to offset the signal
attenuation caused by cable loss, and improve the sensitivity of the measurement
system. However, if there is a strong external signal, it may cause the preampliﬁer to
saturate or a nonlinear false signal, resulting in a deviation of the measurements. The
preampliﬁer should be used in the linear region as much as possible, so that when
abnormal data occurs, an external attenuator can be used to assist in determining
whether there is a false signal.
In addition, the parameters of the preampliﬁer consist of the gain G and the noise
factor NF, so its characteristics should be considered comprehensively.
2.
Sensitivity of the ambient noise receiving system
(1) The calculation formula of the noise power is
N = k × T × B
(10.3.8)
where N is the ambient noise power and N0 is the ambient noise power at room
temperature;
k is the Boltzmann constant, k = 1.38 × 10−23 J/K;
T is the temperature. Room temperature is 290 K;
B is the measurement bandwidth in Hz. At room temperature, when B = 1 Hz,
N0 = −174 dBm/Hz; since thermal noise and measurement bandwidth B change
according to the law of 10 × lg(B), when B = 10 kHz: N = −174 dBm + 10 × lg(10
× 103) = −134 dBm.
(2) Sensitivity of the receiving system
The sensitivity of the receiver is related to ambient thermal noise, and can be
calculated as
S = N0 + G + N F
(10.3.9)
where S is the sensitivity of the receiver;
N0 is the input ambient noise of the preampliﬁer, typically it is −174 dBm/Hz;
G is the gain of the preampliﬁer in dB;
NF is the noise factor of the preampliﬁer in dB.
Then, the noise factor of the system is calculated as:
N F = (Si/Ni)/(So/No)
(10.3.10)


422
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
where NF is the noise factor, i.e., the ratio of the input S/N to the output S/N;
So is the output signal;
No is the output noise;
Si is the input signal;
Ni is the input noise.
When So = Si × G, then
N F = (Si/Ni)/(Si × G/No) = N0/Ni × G
(10.3.11)
Expressed in a logarithm function:
N F = N0 −Ni −G, then N0 = Ni + G + N F
(10.3.12)
The output thermal noise of the ampliﬁer at room temperature is
N0 = −174 + G + N F
(10.3.13)
After the above noise passing a L2 attenuation cable, the noise at the receiver
input port is
Pi = −174 + G + N F −CL2
(10.3.14)
In actual test, there will be two cases: the thermal noise is lower than the receiver
sensitivity or higher than the receiver sensitivity.
(1) When the thermal noise is lower than the receiver sensitivity:
N0 + G + N F −CL2 < S
(10.3.15)
where S is the receiver sensitivity in dBm/Hz;
N0 is the input ambient noise of the preampliﬁer, typically is −174 dBm/Hz, then
E = S + 10 lg(B) + AF + CL1 + CL2 −G
(10.3.16)
It can be seen from the above equation that, when the parameters such as S, B, AF,
CL1, and CL2 are lower, and the parameter G is larger, the sensitivity of the system
is higher.
However, to meet the requirements of the above equation, for example, assuming
the receiver sensitivity is −160 dBm/Hz, then
G(dB) + N F(dB) −CL2(dB) < −160 −(−174) = 14
(10.3.17)


10.3 Main Computer-Based EMC Test Methods
423
Since the receiver sensitivity at low-frequency band is even lower, unless G is
very small, or CL2 is very large, otherwise, it is very difﬁcult to meet the conditions
of the above equation.
(3) When the thermal noise of the receiver input port is higher than the receiver
sensitivity:
N0 + G + N F −CL2 > S
(10.3.18)
then,
G(dB) + N F(dB) −CL2(dB) > S(dBm/Hz) −(−174)
(10.3.19)
The measurement at the receiver is the thermal noise of the input port, i.e.,
−174(dBm/Hz) + G(dB) + N F(dB) −CL2(dB)
(10.3.20)
According to the above equation:
E = V + 10 lg(B) + AF + CL1 + CL2 −G
=−174 + G + N F −CL2 + 107 + 10 lg(B) + AF + CL1 + CL2 −G
=−174 + N F + 107 + 10 lg(B) + AF + CL1
(10.3.21)
where 107 is the conversion from dBm to dBμV, then
E = −174 + N F + 107 + 10 lg(B) + AF + CL1
(10.3.22)
It follows from the above equation that, when N0 + G + NF −CL2 > S, the system
sensitivity is related to the noise factor of the preampliﬁer NF, the measurement
bandwidth B, the antenna factor AF, and the cable loss from the antenna to the
preampliﬁer; In this case, the system sensitivity can be improved by using a lower
NF preampliﬁer, a smaller bandwidth and a lower AF antenna (higher gain) and a
shorter connection cable between the antenna and the preampliﬁer.
In general, the EMC test uses a wideband preampliﬁer, its NF in the LF band is
typically 1–2 dB, and that in the HF band is 2–4 dB, so there is limited space for
improving the NF of the preampliﬁer.
Because the test bandwidth B is already speciﬁed in the relevant EMC standards,
unless there is a particular high requirement for the system noise, the test bandwidth
is generally set according to the standards. It should be noted that if the test bandwidth
is modiﬁed, the test stepping size also needs to be modiﬁed to satisfy the regulation
of the test stepping size being at least B/2.


424
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
A lower NF antenna may be used, which means antenna gain is higher. However,
the problem caused by the higher gain antenna is that the beamwidth becomes
narrower. For EMI testing, it means that more test positions are needed to ensure
coverage of the EUT;
Since the cable loss in the LF band is lower, the preampliﬁer is often installed in
the control room for the LF band. However, in the HF band, the preampliﬁer must
be installed at the back of the antenna due to cable loss. The shorter the cable, the
better.
10.3.6.3
RE102 Inspection and Testing Procedure
The RE102 calibration and test software ﬂow are shown in Fig. 10.32 and Fig. 10.33,
respectively.
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, frequency, 
output level minimum signal 
output to OFF
Signal source
Set level to the value of the 
limit-AF-6dB, signal output 
ON
Calculation
The limit at the calibration 
frequency and AF
Signal source
Set the 
calibration
frequency
Receiver setting
Set the starting frequency, ending 
frequency RBW, attenuation, 
reference level according to 
scanning
Calculation of the electric field 
strength dBμV/m
Receiver reading at calibration 
frequency dBμV+AF+CL-
preamplifier gain
Display the final calibration 
result
Next frequency?
Yes
End of calibration
No
All equipment exit 
program-control
(local)
Calculation of the AF, CL and 
preamplifier gain at 
corresponding frequency
Read
Receiver’s reading
Receiver’s
reading
Fig. 10.32 RE102 system inspection ﬂow


10.3 Main Computer-Based EMC Test Methods
425
Check equipment connection 
status, program-controlled 
initialization of all equipment
Frequency
range
required by 
the test
Receiver setting
Set the starting frequency, ending 
frequency RBW, attenuation, 
reference level according to 
scanning
Calculation of the electric field 
strength dBμV/m
Receiver reading at calibration 
frequency dBμV+AF+CL-
preamplifier gain
Display the test result
End the test?
End of the test
Yes
All equipment exit 
program-control
(local)
Segment the test span according to RBW at 
different frequency band, give out the 
starting and ending frequencies of each 
segment
Display the final test result
Replace the 
antenna?
No
No
Prompt to 
replace
antenna
Yes
Calculation of the AF, CL and
preamplifier gain at 
corresponding frequency
Read
Receiver’s reading
Receiver’s
reading
No
Fig. 10.33 RE102 test ﬂow
10.3.7
RS103 Electric Field Radiated Susceptibility Test
The RS103 test system setup is shown in Fig. 10.34, the test can be done either by
the electric ﬁeld sensor method or receiving antenna method.
The electric ﬁeld sensor test method procedure: The signal generator is modulated
using a 1 kHz, 50% duty cycle pulse to generate an electric ﬁeld at the starting
frequency using an appropriate transmitting antenna and an ampliﬁer, then gradually
increase the electric ﬁeld level until the limit value is reached. Scan within the test
frequency range as required, keep the electric ﬁeld at the required limit, and monitor
the EUT for susceptibility. During the test, the placement of the electric ﬁeld probe
should avoid the inﬂuence of EUT reﬂection, that is, the electric ﬁeld sensor is aligned
with the transmitting antenna, and the distance from the electric ﬁeld sensor to the
EUT and the transmitting antenna are the same. When the frequency is not higher
than 1 GHz, the electric ﬁeld sensor should be at least 30 cm above the ground plane;
when the frequency is higher than 1 GHz, it should be placed at the height of the


426
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
EUT
LISN
(a) Electric field sensor method
Electric field 
sensor
Antenna 
RF amplifier
Signal generator
Excitation and 
monitoring 
device
Shielding 
enclosure
Electric field 
sensor display
B
(b) Receiving antenna method
Shielding 
chamber
Receiving 
antenna
Transmitting 
antenna
Signal generator 
RF amplifier
RF amplifier
Power meter
Data recording 
device
Attenuator 
Measurement 
receiver
Data recording 
device
1.5m
3m
Fig. 10.34 RS103 test system conﬁguration


10.3 Main Computer-Based EMC Test Methods
427
irradiation area of the EUT. Do not place the electric ﬁeld sensor on the edge of the
antenna’s main beam. Make sure that the ﬁeld strength of the electric ﬁeld sensor is
generated by the fundamental frequency rather than the harmonics or other spurious
emissions. Also, make sure that the peak value rather than the average level of the
modulated waveform corresponds to the speciﬁed test level. When using an electric
ﬁeld sensor to monitor the modulated test signal, if the reading is smaller than the
peak detection reading, the measured indicator should be converted into the peak
value.
Calibration is required prior to testing. Record the amplitude of the EUT’s radiated
emissions displayed on the electric ﬁeld sensor display and, if necessary, change the
position of the electric ﬁeld sensor until the amplitude is less than 10% of the test
ﬁeld strength limit.
The receiving antenna test method procedure: The signal is modulated by the
signal generator with a 1 kHz, 50% duty cycle pulse to generate an electric ﬁeld at
the starting frequency by using an appropriate transmitting antenna and an ampliﬁer,
then the input power is gradually increased to the recorded value during calibration.
Scan within the test frequency range as required, adjust the input power according to
the calibration data, and monitor the EUT on susceptibility. If susceptibility occurs,
the susceptibility threshold level shall be determined. When the transmitting antenna
is vertically polarized, the test should be conducted in the entire test frequency bands;
if the transmitting antenna is horizontally polarized, the test is performed only above
30 MHz. Repeat the test for each required antenna position. In the microwave test
frequency band, attach importance to the coverage of the transmitting antenna beam.
Calibration is also required before testing. In the frequency band >1 GHz, replace
the receiving antenna with a signal generator and connect it to the coaxial cable,
adjust the signal to the output level of 0 dBm at the highest frequency required
for the test, and adjust the receiver to the frequency of the signal generator. After
considering all losses, make sure that the measured value is within ±3 dB of the
injected signal level. Connect the receiving antenna to the coaxial cable and use
another signal generator to set the pulse modulation to 1 kHz, 50% duty cycle.
Use an appropriate transmitting antenna and ampliﬁer to establish an electric ﬁeld
at the starting frequency, and gradually increase the ﬁeld strength up to the limit,
scan within the test frequency band, and record the power level required to feed the
transmitting antenna for maintaining the required electric ﬁeld strength. Replace the
antenna or change the conﬁguration and repeat the above procedure. Note that the
receiver should not be overloaded or damaged during calibration.
During the test, attach importance to the position and arrangement of the test
antenna. The antenna shall be placed 1 m or more away from the test setup boundary
as required below:
(1) At 10 kHz to 200 MHz, when D ≤3 m, the antenna is placed on the centerline
of the test setup boundary edge, which includes all EUT enclosures and the


428
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
exposed 2 m interconnecting and power lines. If the interconnecting line is
shorter than 2 m in the actual installation of the platform, an interconnecting
line shorter than 2 m is allowed; when D > 3 m, multiple antenna positions N
may be used, and the number of antenna positions N is taken by dividing the
width of the boundary (in m) by 3 and rounding up to the nearest integer.
(2) At 200 MHz to 1 GHz, the antenna should have a sufﬁcient number of placement
positions so that the entire width of each EUT enclosure and the ﬁrst 35 cm line
segment of the terminated wire/cable are within the 3 dB beamwidth of the
antenna.
(3) At 1 GHz or above, the antenna should have a sufﬁcient number of placement
positions so that the entire width of each EUT enclosure and the ﬁrst 7 cm line
segment of the terminated wire/cable are within the 3 dB beamwidth of the
antenna.
10.3.7.1
Relationship Among RS103 Measurement Data
The RS103 test conﬁguration is shown in Fig. 10.35.
E = PSG −CL1 + G AM P −CL2 + TAF
(10.3.23)
where E is the electric ﬁeld strength at a distance of 1 m from the RE antenna in
dBV/m;
PSG is the output power of the signal source in dBm;
T AF is the antenna factor of the RE antenna at 1 m distance in dB(1/m);
CL1, CL2 are cable loss, directional coupler loss, respectively, in dB;
GAMP is the ampliﬁer gain in dB.
Signal generator
Amplifier 
Forward 
return 
coupler
Antenna factor
RF power 
meter
Amplifier 
output
Measurement 
unit
F/O link
Display unit
Output 
Fig. 10.35 Diagram of RS103 test conﬁguration


10.3 Main Computer-Based EMC Test Methods
429
Antenna
Fig. 10.36 Relationship between transmitting antenna distance and its diameter
10.3.7.2
Precautions for RS103 Test
In this test, the beamwidth of the antenna should be taken into account. In many cases,
in order to reduce the power of the ampliﬁer, a high-gain antenna is considered to
be adopted, but this will result in a narrower beamwidth, which requires more test
positions for larger sized EUTs to meet the test coverage requirements (Fig. 10.36).
In the RS103 test, the closed-loop control method is used, that is, the electric
ﬁeld is controlled by the real-time reading of the electric ﬁeld probe. Because the
test uses a 1 kHz, 50% duty cycle pulse modulation signal, while currently, the main
electric ﬁeld probes measure the RMS of the electric ﬁeld, the difference between
the RMS and the peak value should be noticed and corrected during calibration (refer
to Sect. 10.3.4 Description of CS114 for details).
In addition, it is regulated by the standards that the EUT should be installed on
a conductive table with a ground plane. The metal plate will have a considerable
impact on the electric ﬁeld test value of the horizontal test in the LF band. Therefore,
in the actual test, the electric ﬁeld probe should be placed properly away from the
metal table to reduce such impact.
10.3.7.3
RS103 Test Process
The RS103 test software ﬂow is shown in Fig. 10.37.


430
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Check equipment connection 
status, program-controlled 
initialization of all equipment
Signal source
Set the sine wave, frequency, 
output level minimum signal 
output to OFF
Set the field 
strength meter
Signal source
Signal output 
set to ON
Set the operating 
range of the field 
strength meter
Electric field probe 
reading
Electric field probe reading+ 
probe correction factor+ pulse 
modulation correction
Equal?
Electric field limit
Signal source
Adjust the output level 
according to the difference 
with the limit
No
Signal source
Set the test 
frequency
Record
Output level of the signal 
source
Forward power and field 
strength
Yes
End of the test
Turn off the signal source 
output, set the amplifier to 
Standby
All equipment exit program-
control (local)
Does the power 
reach the 
maximum output 
level of the 
amplifier?
No
Continue or stop the test 
depending on the max input 
level
Yes
Set the power 
amplifier to operate 
mode
Read the forward and reverse 
power on the power meter
Probe correction 
factor
End of the 
test?
Yes
No
Is the reflective 
power or SWR 
excessive
Yes
Fig. 10.37 RS103 test ﬂow
10.4
Main Non-Programmed EMC Test Methods
10.4.1
CE107 Power Lead Spike Signal (Time Domain)
Conducted Emission
Considering that the limit requirement depends on the amount of voltage, only
the LISN test method is retained in the EMC equipment speciﬁcations. The test
conﬁguration is shown in Fig. 10.38.
During the test, connect the oscilloscope voltage probe between one power line at
the output of the LISN and its ground, and as close as possible to the LISN. Power-up
and preheat the test equipment to a stable operating state. Turn ON and OFF various


10.4 Main Non-Programmed EMC Test Methods
431
EUT
LISN
LISN
50
50
Oscilloscope (high 
impedance)
Load 
Load 
Power line
Fig. 10.38 CE107 Voltage test system conﬁguration
switches of the EUT (including state shifting switch and power switch) under typical
operating condition, repeat the above operations at least ﬁve times, and measure the
maximum amplitude of the spike signal generated by the EUT during the switching
operation. If there is a potential of synchronization, the EUT switching should be
set between the peak and zero values of the supply voltage. Then repeat the above
process and go through all power lines to be tested.
CE107 test has canceled the inductive method and the current probe method. The
reason for canceling the inductive method is that the technical speciﬁcations of the
25 μH inductor are not clearly deﬁned, so different test results may be obtained. The
reason for canceling the current probe method is that the limit speciﬁed by CE107
is the voltage limit, while the physical quantity measured by the current probe is
the current. However, in the transient CE of the spacecraft power line, the current
limit is often used, so the current probe method is also presented here, and the test
conﬁguration is shown in Fig. 10.39. The test method is similar to the voltage test
method.
10.4.2
CS103 Antenna Port Intermodulation Conducted
Susceptibility
The CS103 test system conﬁguration is shown in Fig. 10.40. In case that the receiver
can provide interference indications because no signal is received, a signal generator
C can be used to generate the fundamental signal.
The CS103 test method is as follows:
(1) Set the output of signal generator B to zero, tune the signal generator A to the
EUT tuning frequency f 0 and modulate it as required. Adjust its output level
so that the EUT produces a standard reference output level, and record the


432
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
EUT
LISN
LISN
50
50
Power line
Load 
Load 
Current probe
Attenuator 
Oscilloscope 
Fig. 10.39 CE107 current test system conﬁguration
EUT
A
Monitoring 
device
Measurement 
receiver
Triple-port network
Triple-port network
(If necessary)
Filter, attenuator
(If necessary)
Signal generator C
(If necessary)
Signal generator A
Filter, attenuator
(If necessary)
Triple-port network
Filters, attenuators
(If necessary)
Signal generator B 
Fig. 10.40 CS103 test system conﬁguration


10.4 Main Non-Programmed EMC Test Methods
433
output level V 10 and frequency f 0 of signal generator A. Set the output of signal
generator A to zero, repeat the above steps for the signal generator B and record
the output level V 20.
(2) Set the output of signal generator B to zero, and modulate the signal generator A
as required, adjust its output level, so that it is equal to the sum of the speciﬁed
limit level and the level V 10 obtained from step (1), and maintain this output
level unchanged. Then gradually increase the frequency of signal generator A
until the EUT has no response, record the frequency f 1, and maintain the signal
generator A at f 1, then, f = f 1 −f 0.
(3) Set the output of the signal generator A to zero, but not modulate the signal
generator B. Tune the frequency of the signal generator B to f 2 = f 1 + f
= f 0 + 2f, then let the output levels of the signal generator A and B equal
to the sum of the speciﬁed limit level and V 10, V 20 respectively, observe the
intermodulation products. At this time, if the EUT has no obvious response,
then gradually increase the output levels of the two signal generators until the
EUT responds. Maintain the output level, and ﬁne-tune the frequency of the
signal generator B to maximize the EUT response and record the frequency
of the signal generator B. To observe the m order intermodulation products,
gradually increase the frequency of the signal generator B starting from f 2 until
10 f 0 or 10 GHz (whichever is smaller) while maintaining a constant output
level, and observe the intermodulation products.
(4) Set the output of the signal generator A to zero. If the EUT still responds, it
indicates that the product is not caused by intermodulation; if the response disap-
pears, it indicates that the response is an intermodulation product. The measure-
ment receiver can be used to identify whether the intermodulation products are
from the EUT or the harmonics of the signal generator or the test devices.
(5) If the result indicates that the response occurred in step (3) is caused by the
intermodulation, then reduce the output levels of the two signal generators by
the same amount until the EUT reaches the standard reference output level,
record the output levels of the two signal generators V 1 and V 2, and calculate
the intermodulation suppression level as follows:
Sim = (V1 −V10) or (V2 −V20)
(10.4.1)
where Sim is the m order intermodulation suppression level in dB;
V 1, V 2 are the output levels of the signal generator A and B obtained from this
step in dBμV;
V 10, V 20 are the output levels of the signal generator A and B obtained from
step (1) in dBμV.
(6) Adjust the frequencies of the signal generator A and B to f 1 = f 0 −f and f 2
= f 0 −2f respectively, and repeat steps (2)–(5).
(7) To observe the m order intermodulation products, slowly reduce the frequency
of the signal generator B until 0.1 f 0 or 15 kHz (whichever is greater) while
maintaining a constant level.


434
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.4.3
CS104 Antenna Port Undesired Signal Rejection CS
Test
The CS104 test system conﬁguration is shown in Fig. 10.41. All signal generators
may output a considerable amount of harmonics and spurious signals, which may be
ﬁltered out if necessary. For frequency-hopping receivers, a single signal generator
method can be used, which is more suitable for receivers that search for signals and
capture. The dual signal generator method is more suitable for most receivers, still
certain receivers may require both methods to measure them in order to completely
characterize them.
The process of CS104 test is as follows:
(1) Set the output of the signal generator B to zero, tune the signal generator A to
the EUT tuning frequency f 0 as speciﬁed, and modulate it as required. Adjust its
output level so that the EUT produces a standard reference output level, record
the output level V 10, and frequency f 0 of the signal generator A. Set the output
EUT
Monitoring 
device
Measurement 
receiver
Triple-port network
Signal generator A
Filters, attenuators
(If necessary)
Triple-port network
(If necessary)
Filters, attenuators 
(If necessary)
Signal generator B
(If necessary)
Fig. 10.41 CS104 test system conﬁguration


10.4 Main Non-Programmed EMC Test Methods
435
of the signal generator A to zero, repeat the above step for signal generator B,
and record the output level V 20.
(2) Switch on the two signal generators, signal generator A is modulated as required,
and signal generator B is not modulated.
(3) Adjust the signal generator A to the level obtained from step (1), adjust the
signal generator B to be equal to the sum of the required limit value and V 20.
(4) Scan and check all the responses with signal generator B over the frequency
range to be tested.
(5) To ensure that the measurement is the EUT’s spurious response rather than the
harmonic or spurious output of the signal generator, the measurement receiver
can be used to identify whether the spurious response is from the EUT or from
the signal generator’s harmonics or the measurement devices.
(6) When a true spurious response is obtained, the output level of the signal gener-
ator B should be lowered until the EUT regains the standard reference output,
record the output level V of the signal generator, and calculate the spurious
response suppression level as follows:
Ss = V −V20
(10.4.2)
where Ss is the spurious response suppression level in dB;
V is the output level of the signal generator B obtained from this step in dBμV;
V 20 is the output level of the signal generator B obtained from step (1) in dBμV.
(7) If the output level of the signal generator B is applied according to step (3), and
the EUT does not respond when scanning as in step (4), it is allowed increase
the output level of the signal generator B, and re-scan as in step (4) until the
EUT has a spurious response. Repeat step (6) to determine the spurious response
suppression level.
10.4.4
CS105 Antenna Port Cross Modulation CS Test
The CS105 test system conﬁguration is shown in Fig. 10.42. The signal generator
frequency may drift during the test, so it should be ﬁne-tuned to ensure the maximum
response is measured. For frequency-hopping receivers, a feasible method is to select
a tuning frequency within the frequency-hopping range, and conﬁgure the signal
generator as described above, then evaluate the receiver by frequency hopping.
The CS105 test method is as follows:
(1) Set the output of signal generator B to zero, tune signal generator A to the EUT
tuning frequency f 0 as speciﬁed, and modulate it as required. Adjust its output
level so that the EUT produces a standard reference output level, record the
output level V 10 and frequency f 0 of signal generator A. Set the output of signal
generator A to zero, repeat the above step for signal generator B and record the
output level V 20.


436
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
EUT
Monitoring 
device
Measurement 
receiver
Triple port network
Signal generator A 
Filters, attenuators
(If necessary)
Triple-port network
(If necessary)
Filters, attenuators
(If necessary)
Signal generator B 
Fig. 10.42 CS105 test system conﬁguration
(2) Switch on the two signal generators, the signal generator A is modulated as
speciﬁed, the signal generator B is not modulated. Adjust the output level of
signal generator A so that it is 10 dB higher than the level V 10 obtained from
step (1).
(3) Adjust the output level of the signal generator B to be equal to the sum of the
speciﬁed limit level in the speciﬁcation and the level V 20 obtained from step
(1).
(4) Starting from the frequency at which the level of the EUT response curve or the
selectivity curve is equal to the level obtained from step (3), adjust the frequency
of the signal generator B until f 0 ± f IF (where f IF is the intermediate frequency
of the EUT), and monitor the EUT output and observe the intermodulation
product.
(5) When the response is found, remove the modulation of the signal generator
A, if the response disappears at this time, it indicates that it is generated by
the intermodulation. The measurement receiver can also be used to identify


10.4 Main Non-Programmed EMC Test Methods
437
whether the intermodulation product is from the EUT or from the signal gener-
ator’s harmonics or the measurement device. Reduce the output level of the
signal generator B again until the EUT resumes generating the standard refer-
ence output, and record the level and frequency of the signal generator B. The
difference between this level and the level V 20 in step (1) is the intermodulation
suppression level.
10.4.5
CS106 Power Lead Spike Signal CS Test
The CS106 test system conﬁguration is shown in Fig. 10.43. Since the oscilloscope’s
safety ground wire is disconnected, there may be a shock hazard; special care should
be taken during the test. For the test conﬁguration shown in the ﬁgure, a differential
probe can be used for testing. In this case, the oscilloscope can be supplied not via
the isolation transformer, while continuing to maintain the ground connection so as
to avoid shock hazard.
During the CS106 test, ﬁrst power-on and preheat the EUT to reach a stable
operating state, and select a power line for testing. Then adjust the output of the
spike generator to the minimum, and increase the signal level until the power line
reaches the required voltage or the calibration setting. This level is the required signal
level. Finally, maintain the signal level no lower than the required signal level, test
the EUT ungrounded input line with 5–10 Hz pulse repetition frequency (PRF) and
with both the positive and negative polarity. The test time for each polarity is no less
than 5 min. Monitor the EUT for susceptibility. If susceptibility occurs, identify the
susceptibility threshold level and the phase on the AC waveform. Repeat the above
steps for other power lines and conditions to be tested.
Before the test, the test system needs to be calibrated. Adjust the spike generator
to the minimum output, increase the signal level until the voltage indicated by the
oscilloscope reaches the limit, conﬁrm the output waveform and pulse width, and
record the set value of the spike generator.
EUT
LISN
LISN
10
F
Simulation and 
monitoring 
device
Isolation 
transformer
Oscilloscope
(high 
impedance)
Spike 
signal 
generator
High 
potential line
Return line
Power line
Fig. 10.43 CS106 test system conﬁguration


438
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.4.6
CS118 ESD Susceptibility Test
The CS118 test is divided into direct discharge and indirect discharge.
Direct discharge: refers to direct discharge of the EUT, suitable for the points
and surfaces on the EUT that are accessible by personnel during normal use. The
discharge frequency is once per second, 30 times per point (surface). There are
following exceptions (no discharge is applied to the following points):
(1) Points and surfaces that are accessible only during maintenance.
(2) Points and surfaces that are accessible to the end user during maintenance.
(3) Points and surfaces that are no longer accessible after the equipment is installed
and ﬁxed or after use according to the instructions.
(4) Points that are accessible to the coaxial connector or multicore connector which
has a metal outer casing. In this case, only the outer casing of the connector is
applied with contact discharge.
(5) The accessible points in nonconductive connectors, for which only air discharge
tests may be performed.
(6) The parts that are susceptible to electrostatic discharge for functional reasons,
or have ESD warning labels.
(7) No contact discharge test shall be performed on insulating surfaces; only air
discharge may be performed.
Indirect discharge: refers to discharge of the coupling plate near the EUT to simulate
the human body discharge of objects near the EUT.
(1) For equipment directly mounted on the satellite deck or directly connected to
the structural ground, only contact discharge on the vertical coupling plate, and
the distance between the coupling plate and the test equipment surface is 0.1 m.
The discharge frequency is once per second and 30 times per point (surface).
(2) For equipment with no installation surface directly connected to the satel-
lite structure, contact-discharge may be performed on both the horizontal and
vertical coupling plates, and the distance between the coupling plate and the
test surface is 0.1 m. The discharge frequency is once per second and 30 times
per point (surface).
(3) When performing contact discharge on the vertical coupling plate, tests should
be conducted at different positions on all four surfaces of the EUT.
Contact discharge method is preferred for both direct and indirect discharge, and
air discharge method is left with nothing better than the second choice. Contact
discharge should use the sharp electrode tip of the ESD generator, and air discharge
the circular electrode tip of the ESD generator.
In the ESA standards, the ESD test method is different from the human body
static test, by using a 20 cm coupling line. The test system conﬁguration is shown in
Fig. 10.44.


10.4 Main Non-Programmed EMC Test Methods
439
Discharge 
interval
Blocking 
resistor
ESD or high voltage 
DC power
Coupling 
The injection line is closely 
coupled with the test cable 
bundle
High voltage 
capacitor
Current probe
Test cable bundle 
Attenuation resistor
Current probe
Blocking 
resistor
Fig. 10.44 ESD test conﬁguration in ECSS-E-ST-20-07C
10.4.7
CS115 and CS116 Bulk Cable Injection Transient CS
Tests
The CS115 and CS116 test system setup is shown in Fig. 10.45. Place the monitor
probe at 5 cm from the EUT connector. If the total length of the connector and its
enclosure exceeds 5 cm, the monitor probe should be placed as close as possible to
the connector enclosure. Place the injection probe at 5 cm from the monitor probe.
During the CS115 test, ﬁrst power-up and preheat the EUT to a stable operating
state, and the pulse signal generator output is at least the calibrated amplitude. Then,
apply the test signal at the speciﬁed PRF and test duration, and monitor whether the
EUT is degraded. If the EUT is susceptible, identify the susceptibility threshold level,
and record the induced peak on the bulk cable measured by the oscilloscope. Finally,
repeat the above test procedure for each bulk cable connected to other connectors of
the EUT.
Beforetesting, thetest systemneeds tobecalibrated. Adjust thepulsesignal gener-
ator according to the required rise time, pulse width, and PRF. When increasing the
signal level, monitor the current ﬂow through the center conductor of the calibration
ﬁxture with an oscilloscope, until it reaches the speciﬁed current in the standards, and
conﬁrm the rise time, fall time, pulse width of the pulse waveform, and PRF. Since
it is an inducted coupling, the pulse waveform cannot be accurately reproduced.
Record the amplitude setting value of the pulse signal generator.


440
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
EUT
LISN
Injection probe
Monitor probe
Monitor probe
Injection probe
5cm
5cm
5cm
5cm
Interconnecting
cable
Power input
Actual or simulated loads and 
signals
Memory
oscilloscope (50Ω)
Drive Cable
Use the dotted 
line paths for 
power line test
CS115-pulse signal 
generator
CS116-damped
sinusoidal transient 
signal generator
Fig. 10.45 CS115 and CS116 test system setup


10.4 Main Non-Programmed EMC Test Methods
441
In the CS116 test, ﬁrst power-up and preheat the EUT to a stable operating state,
adjust the damped sinusoidal transient signal generator to 10 kHz. Then apply a test
signal to each cable or power lead of the EUT in sequence as required, and gradually
increase the output level of the damped sinusoidal transient signal generator until the
peak current of the monitor probe reaches the current limit, but the maximum output
cannotexceedthecalibratedsettingvalue.Recordthemeasuredpeakcurrent,monitor
the EUT for performance degradation and, if susceptible, identify the susceptibility
threshold level. Finally, repeat the above test procedure for other frequencies as
required.
Before testing, the test system needs to be calibrated. Set the frequency of the
damped sinusoidal transient signal generator to 10 kHz, gradually increase the ampli-
tude of the damped sinusoidal transient signal generator to the peak current limit.
Record the set value of the damped sinusoidal signal generator and conﬁrm that the
waveform meets the requirements. Repeat the above calibration processes for each
required frequency.
10.4.7.1
Relationship Among CS115 and CS116 Measurement Data
The CS115 test limit is the current value of 5 A, and the CS116 test limit the current
value of 10 A, which can be converted into a voltage value by a 50  calibration
ﬁxture, that is:
the current value is converted into voltage as U = I × R = 250 (V).
Because the voltage value is out of the oscilloscope’s scope, it is recommended
to connect a 40 dB attenuator to the input of the oscilloscope, from
A = 20 lg(V1/V2)
(10.4.3)
where the 40 dB attenuator is equivalent to a 100-fold attenuation of the voltage
value, so the 250 V voltage is measured as 2.5 V on the oscilloscope.
Because it is a pulse signal with relative small average power and a high peak
voltage, it is recommended to use a high-voltage attenuator and a high-voltage load.
10.4.7.2
Precautions for CS115 and CS116 Test
The signal characteristics of the CS115 are shown in Fig. 10.46.
In the CS115 test, the rising edge of the pulse signal is less than 2 ns, which
needs to use an oscilloscope with the corresponding bandwidth. Generally, it is
evaluated according to the “knee” frequency of the signal. The “knee” frequency can
be expressed as the following formula:
fknee = 0.5/Trise
(10.4.4)


442
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(Minimum)
Repeat frequency = 30Hz
Fig. 10.46 CS115 signal characteristics
where f knee is the knee frequency in Hz;
T rise is the rise time of the signal in s.
In the CS115 test, the rising edge is 2 ns, so the knee frequency of the pulse signal
is about 250 MHz.
The oscilloscope is generally measured at a 3 dB bandwidth. If a 250 MHz band-
width oscilloscope is used to measure a 250 MHz signal amplitude, the voltage will
drop by 3 dB at 250 MHz, i.e., 0.707 times, and the amplitude error is about 30%,
which is hardly acceptable. To accurately measure the rise time, it is recommended
to select a oscilloscope bandwidth 2 to 3 times the signal bandwidth. The relationship
between measurement bandwidth and accuracy is shown in Table 10.3.
Note that the intensity of the injected interference of CS115 and CS116 is rather
high. The injection intensity should be determined according to the EUT parameters,
such as the working voltage, and by reference of the spacecraft EMC technical
requirements, so as to avoid damage to the sensitive equipment during the test.
Table 10.3 Relationship
between measurement
bandwidth and accuracy
Accuracy (%)
Gaussian response
Maximum ﬂatness
response
20
f BW = 1.0 × f knee
f BW = 1.0 × f knee
10
f BW = 1.3 × f knee
f BW = 1.2 × f knee
3
f BW = 1.9 × f knee
f BW = 1.4 × f knee


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
443
10.5
Measurement Uncertainty Analysis of Electronic
Equipment EMC Test
The measurement uncertainty indicates the technical capability level of the test. The
aim of test process control is to minimize the measurement uncertainty to meet the
test performance requirements. Analyzing the measurement uncertainty of EMC test
items and identifying the inﬂuence components and size of each measurement uncer-
tainty helps to acknowledge and control the key points of the inﬂuence components
during the test and improve the repeatability, consistency, and accuracy of the EMC
test results, thereby achieving the objective of controlling the EMC test quality and
improving the technical capability level of laboratory EMC testing. The measurement
uncertainty analysis items in this section include: CE101, CE102, CE106/RE103,
CS101, CS103/CS104/CS105, CS114, CS115, CS116, CS118, RE101, RE102,
RS101, and RS103 in MIL-STD-461G: 2015, and CS106 in MIL-STD-461F: 2007.
The measurement uncertainty analysis uses GUM method, refer to ISO/IEC
Guide 98-3:2008 Uncertainty of Measurement—Part 3: Guide to the Expression
of Measurement Uncertainty.
The general procedure for measurement uncertainty evaluation using the GUM
is shown in Fig. 10.47.
The estimation of measurement uncertainty has the following steps:
(1) Determine the quantities to be measured and methods of measurement according
to the test items, including the measurement principle, procedure, equipment,
conﬁguration, and conditions.
(2) Analyze and list the sources of uncertainty that have a signiﬁcant impact on the
measurement results, and establish a measurement model required for measure-
ment uncertainty evaluation, that is, establish a functional relationship between
Assessing the standard uncertainty ui
Calculating the combined standard uncertainty uc
Determining the expanded uncertainty U or Up
Reporting the measurement results
Analyzing the source of uncertainty and establish a measurement model
Fig. 10.47 General procedure for uncertainty evaluation using GUM method


444
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
the quantity to be measured Y and all inﬂuencing quantities. The measure-
ment model shall include all input quantities Xi that have an inﬂuence on the
measurement uncertainty and can be expressed as
Y = f (X1, X2, X3, . . . , XN)
(10.5.1)
Let the estimated value of the input quantity Xi be xi, the estimated value of the
quantity to be measured Y be y, then the measurement model can be written as
y = f (x1, x2, x3, . . . , xN)
(10.5.2)
In the EMC test, in fact, there are some factors that have an inﬂuence on the test
results but no clear functional relationship is established. Then, if the inﬂuence
components (in dB) related to these factors are added in the above equation, and
the estimated values of these inﬂuence components are zero, but the measure-
ment uncertainty of these inﬂuence quantities are not zero, then the ﬁnal formula
is written as
y = f (x1, x2, x3, . . . , xN) + δz1 + δz2 + δz3 + · · · + δzN
(10.5.3)
(3) Determine the standard uncertainty u(xi) for each input quantity. The assessing
methods for the uncertainty of each input quantity include Type A evaluation of
uncertainty by the statistical analysis of the measurement sample and Type B
evaluation for uncertainty by estimation of an assumed probability distribution
based on experience or other information, both of which can be characterized
by a standard deviation; the standard uncertainty for each input quantity can be
assessed either by Type A or Type B evaluation.
(4) Determinethestandarduncertaintycomponentui(y)correspondingtoeachinput
quantity, the calculation formula is
ui(y) = ciu(xi) = ∂f
∂xi
u(xi)
(10.5.4)
(5) Combine each standard uncertainty component u(xi) to obtain the combined
standard uncertainty.
Suppose there are N sources of uncertainty, that is, there are N uncertainty
components ui, where i = 1, 2, …, N. If the uncertainty components are not
correlated, then the combined uncertainty can be calculated as follows:
uc =




N

i=1
c2
i u2
i
(10.5.5)
(6) Determine the coverage factor k of the possible value distribution of the quantity
to be measured Y.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
445
(7) Determine the expanded uncertainty, which is obtained by the combined
standard uncertainty multiplied by the coverage factor k:
U = kuc
(10.5.6)
In the EMC test, the coverage factor is generally taken as k = 2, and the expanded
uncertainty retains 1 to 2 signiﬁcant ﬁgures.
(8) Finish the measurement results report.
The measurement results can be expressed as follows:
Y = y ± U
(10.5.7)
where Y is the quantity to be measured;
y is the estimated value of the quantity to be measured Y;
U is the expanded uncertainty.
10.5.1
Uncertainty Analysis of Common Inﬂuence
Components of EMC Items
10.5.1.1
Uncertainty Introduced by the Receiver
The estimation of receiver reading uncertainty is the experimental standard deviation
of the average reading of multiple measurements, using Type A evaluation, with the
standard uncertainty being the experimental standard deviation of the mean.
Generally, it is only measured once in actual measurement. Veriﬁed by rele-
vant tests, the uncertainty can be assessed using the data given in CISPR16-4-
2: 2014 Speciﬁcation for Radio Disturbance and Immunity Measuring Apparatus
and Methods. Part 4-2: Uncertainties, Statistics and Limit Modeling - Measurement
Instrumentation Uncertainty, that is, the uncertainty is taken as u(V r) = 0.10 dB.
The factors affecting the accuracy of the receiver reading include the correction
values of the inaccurate receiver sinewave voltage, the unsatisfactory receiver pulse
amplitude response, the unsatisfactory receiver PRF response and the receiver noise
ﬂoor effect, etc.
1. Uncertainty of the receiver sinewave voltage inaccuracy correction value
u(δVsw)
The tolerance limit of the receiver sine wave voltage accuracy given by CISPR16-4-2
is ±2.0 dB, the estimated correction value is taken as 0, and has a uniform distribution
of a half-width 2.0 dB, i.e.,


446
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
u(δVsw) = 2.0
√
3
dB = 1.2 dB
(10.5.8)
The estimated value of the inﬂuence component of the sinewave voltage accu-
racy can also be obtained by referring to the receiver’s product speciﬁcation. For
example, it is obtained from the product speciﬁcation of a certain type of receiver
that the measurement uncertainty is: at <3 GHz, under 95% conﬁdence, and without
preselector/preampliﬁer, the uncertainty U = 0.5 dB; In case with a preselector but
no preampliﬁer, the uncertainty U = 1.0 dB.
u(δVsw) = 0.5
2 dB = 0.25 dB
(10.5.9)
In addition, the estimation of the inﬂuence component of the sinewave voltage
accuracy can be obtained from the calibration report of the receiver, together with
its expanded uncertainty and coverage factor.
2. Uncertainty of the unsatisfactory receiver pulse amplitude response correc-
tion value u(δVpa)
The tolerance limit of the receiver pulse amplitude response given in CISPR16-4-2
is ±1.5 dB, the estimation of the correction value is taken as 0, and has a uniform
distribution of half-width 1.5 dB, i.e.,
u

δVpa

= 1.5
√
3
dB = 0.87 dB
(10.5.10)
Also refer to the receiver’s veriﬁcation certiﬁcate.
3. Uncertainty of the receiver noise ﬂoor inﬂuence correction value u(δVnf)
For a certain test item, if the noise ﬂoor of the receiver is much lower than the
speciﬁed limit of the item in MIL-STD-461G, the effect of the receiver noise ﬂoor on
the result of a measurement that is close to the limit can be neglected. In another case,
the inﬂuence of the receiver noise ﬂoor proximity is evaluated based on the actual
performance of the receiver and actual test conditions. For example, the tolerance
limit of the receiver noise ﬂoor proximity is ±0.5 dB, the estimation of the correction
value is taken as 0, and the coverage factor is 2.
u(δVnf) = 0.5
2 dB = 0.25 dB
(10.5.11)
4. Peak detection without considering the impact of PRF response
The MIL-STD EMI measurements adopt peak detection. The peak detector detects
the peak of the modulation envelope in the receiver’s passband, and the peak detection
does not need to consider the effect of the PRF response.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
447
Thereceiver’sresponsestothepulseandmodulationsignalofvariousdetectorsare
different. The peak detector can detect the maximum level of the signal envelope, this
characteristic can ensure to reﬂect the worst case of the transmitted data. Figure 10.48
shows the output of several waveforms by the peak detector, and the output results
are the same.
Figure 10.49 shows the relative values of the displayed level and peak display
levels for different detectors and PRFs. From Fig. 10.49, the response to different
PRFs, quasi-peak detectors, RMS detectors, and average detectors are different, but
for the peak detector, the value is the same regardless of the PRF.
Fig. 10.48 Peak detector responses
-80
-70
-60
-50
-40
-30
-20
-10
0
1
10
100
1000
10000
Level/dB
Pulse repetition rate/Hz
PK
RMS
AV
OP
Fig. 10.49 Relative values of level and peak display levels for different detectors and PRFs


448
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
In the evaluation of measurement uncertainty, it is common practice to refer to peer
experiences, which is no exception to the evaluation of EMC measurement uncer-
tainty of spacecraft electronic equipment. For example, CISPR 16-4-2: 2014 Electro-
magnetic Compatibility of Technical Equipment, Speciﬁcation for Radio Disturbance
and Immunity Measuring Apparatus and Methods. Part 4-2, Uncertainties, Statistics
and Limit Modelling. Measurement Instrumentation Uncertainty et al. Taking the
vertically polarized radiated disturbance in 200 MHz to 1 GHz in CISPR 16-4-2
standards as an example, its inﬂuence component on the receiver’s PRF response is
considered to be ±1.5 dB with a rectangular distribution, the standard uncertainty
component is 0.87 dB. However, it is inapplicable if these criteria are referred by
the MIL-STD measurement uncertainty evaluation to consider the inﬂuence compo-
nent of the receiver PRF response, since it will artiﬁcially increase the measurement
uncertainty; moreover, the size of the component is considerably large. Commercial
standards generally use quasi-peak detection, while it is regulated that MIL-STD
EMI measurements use peak detection, which does not need to consider the effects
of receiver PRF response.
10.5.1.2
Uncertainty Introduced by the Oscilloscope
The main inﬂuence components in oscilloscope voltage measurement include: oscil-
loscope readings, correction values of the peak sampling inﬂuence at the oscilloscope
sampling point, and measurement system repeatability.
The inﬂuence factors of the oscilloscope reading include the oscilloscope vertical
resolution, LF linearity, HF linearity, offset resolution, etc. The uncertainty intro-
duced by the oscilloscope reading given by the veriﬁcation certiﬁcate is U = 2% =
0.17 dB, with a uniform probability distribution, k = 2, therefore:
u(Vr) = 0.17
2
dB = 0.085 dB
(10.5.12)
The peak sampling inﬂuence at the oscilloscope sampling point is related to the
oscilloscope’s sampling rate. For example, an oscilloscope with a sampling rate of 1
GS/s has 109 sampling points per second; for a peak pulse signal with a rising edge of
10 ns, an oscilloscope with a sampling rate of 1 GS/s may have 11 sampling points,
so the sampling rate has little effect. For a peak pulse signal with a rising edge of
2 ns, the oscilloscope with a sampling rate of 1 GS/s may have 3 sampling points,
which requires an evaluation of the effect of the sampling rate on the test result. For
3 sampling points, the estimated inﬂuence is 3%, then U = 3% = 0.26 dB, with a
uniform probability distribution, k = 2, therefore:
u(Vr) = 0.26
2
dB = 0.13 dB
(10.5.13)


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
449
10.5.1.3
Uncertainty Introduced by Mismatch
In EMC testing, impedance mismatch has an effect on the test results because the
transmittedsignalwillbereﬂectedatthepointofimpedancemismatch.Thefollowing
is an example of the analysis of the inﬂuence introduced by the mismatch between
a 30 MHz and 200 MHz band biconical antenna and the receiver. The connection is
shown in Fig. 10.50. One cable is represented by a two-port network, the biconical
antennawithareﬂectioncoefﬁcientofΓ e andthereceiverwithareﬂectioncoefﬁcient
of Γ r are connected to port 1 and 2 of the two-port network, respectively. The two-
port network can be characterized by S parameters, and the correction value of the
mismatch error is
δM = 20 lg
(1 −ΓeS11)(1 −ΓrS22) −S2
21ΓeΓr

(10.5.14)
The parameters Γ e, Γ r, S11, S21, and S22 are all complex numbers, typically, only
the modulus values are known. If only the modulus values or limit values of these
parameters are known, it is impossible to calculate δM, but it can be determined by
the above formula that the estimated value of δM does not exceed the limit value
range δM±, which is
δM± = 20 lg
	
1 ±
|Γe∥S11| + |Γr∥S22| + |Γe∥Γr∥S11∥S22| + |Γe∥ΓrS21|2
(10.5.15)
The coaxial cables connected to the biconical antenna and the receiver is well
matched, so it can be considered that |S11| ≪1 and |S22| ≪1, then the above equation
can be simpliﬁed as
δM± = 20 lg

1 ± |Γe∥Γr∥S21|2
(10.5.16)
Fig. 10.50 Schematic
diagram of mismatch error
analysis
Γe
Γr
S11S21
Cable 
S12S22
Measurement 
receiver
1
2
Biconical 
antenna


450
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Fig. 10.51 VSWR curve of
a certain type biconical
antenna
In the frequency range of 30–200 MHz, the maximum insertion loss of the cable
is 1.8 dB, then |S21|=0.81.
CISPR 16-1-1: 2018 Speciﬁcation for Radio Disturbance and Immunity
Measuring Apparatus and Methods—Part 1-1: Radio Disturbance and Immunity
Measuring Apparatus—Measuring Apparatus requires that the RF attenuation of the
receiver in the frequency range of 30–200 MHz is 10 dB or more, and the voltage
standing wave ratio (VSWR) does not exceed 1.2. In the frequency range of 30–
200 MHz, VSWR < 1.2, Γ r = (VSWR −1)/(VSWR + 1) < 0.09. The VSWR of the
receiver can also be obtained from the receiver technical speciﬁcation or measured
data.
For example, Fig. 10.51 shows the VSWR curve of a certain type of receiving
antenna. In the frequency range of 30 MHz to 200 MHz, VSWR < 30, then Γ e =
(VSWR −1)/(VSWR + 1) < 0.94.
Substitute these data into the above equation, we have
δM± = 20 lg |

1 ± |Γe∥Γr∥S21|2
| = 20 lg |

1 ± 0.94 × 0.09 × 0.812
| = 20 lg |(1 ± 0.056)|
(10.5.17)
then, δM+ = 0.47 dB, δM = −0.50 dB.
The probability distribution of δM approximates an inverse sine distribution (U-
shaped distribution), and its half-width is no greater than (δM+ −δM−)/2, the
standard uncertainty is half-width divided by
√
2. Thus, the standard uncertainty
introduced by mismatch is
u(δM) = δM+ −δM−
2
√
2
= 0.34 dB
(10.5.18)
To simplify the calculation, δM± = 20 lg(1 ± |Γ e||Γ r||S21|2) can be expressed as


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
451
δM± = 20 lg

1 ± |Γe∥Γr∥S21|2
= 20 ln(1 ± |Γe||Γr||S21|2)
ln10
(10.5.19)
Since |Γ e||Γ r||S21|2 ≪1, if performing Taylor expansion to the natural logarithm
in the above formula, then: ln(1 ± |Γ e||Γ r||S21|2) ≈± |Γ e||Γ r||S21|2 and
20
ln10 = 8.68,
that is
δM± = ±8.68|Γe∥Γr∥S21|2
(10.5.20)
The standard uncertainty is the half-width divided by
√
2, i.e., the standard
uncertainty introduced by the mismatch is
u(δM) = δM+ −δM−
2
√
2
= 8.68|Γe∥Γr∥S21|2/
√
2 = 6.14|Γe∥Γr∥S21|2
(10.5.21)
Substitute |Γ e| = 0.94, |Γ r| = 0.09, S21| = 0.81 into the above equation, then u(δM)
= 0.34 dB. The standard uncertainty introduced by the mismatch can be calculated
using the simpliﬁed equation 6.14|Γ e||Γ r||S21|2.
In addition, when CISPR 16-1-1 requires that the receivers RF attenuation is 0 dB
in the frequency range of 30–200 MHz, the VSWR does not exceed 2.0, that is, in the
frequency range of 30–200 MHz, VSWR < 2.0, Γ r = (VSWR −1)/(VSWR + 1) <
0.33. Substitute |Γ e| = 0.94, |Γ r| = 0.33, S21| = 0.81 into u(δM) = 6.14|Γ e||Γ r||S21|2,
then u(δM) = 1.25 dB. It can be seen that the mismatch has a large effect on the
measurement result, so effective measures should be taken to reduce the mismatch
during the test.
10.5.1.4
Uncertainty Introduced by Frequency Interpolation
When the calibration coefﬁcient is obtained by calculating the interpolation between
the data of adjacent calibration frequencies, its uncertainty is related to the calibra-
tion frequency interval of the equipment calibration coefﬁcients and its function with
frequency. For example, Fig. 10.52 shows the calibration coefﬁcient of the secondary
transmitted impedance of a current monitor probe (the number of calibration frequen-
cies is different), and the calculated deviation by logarithmic interpolation is no more
than 0.2 dB. The estimate of the correction value of the monitor probe coefﬁcient
interpolation error is 0, and has a uniform distribution of a certain half-width.
u

δC Fpf

= 0.2
√
3
dB = 0.12 dB
(10.5.22)


452
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Frequency/MHz
Transmission impedance/dBΩ
Fig. 10.52 Current monitor probe calibration coefﬁcient curve
10.5.1.5
Uncertainty Introduced by Acceptability Window of Target
Value
In the EMC susceptibility test, an automatic test is often used, but in order to achieve
the target value, it often needs to set a tolerance in the automatic test software. The
smaller the tolerance setting is, the closer it is to the target value, but the longer
the adjustment time of the automatic test software. The acceptability window of
the target value is usually a set parameter, i.e., the tolerance that is accepted by the
software and within the acceptability window of the target level value. For example,
the tolerance of target value acceptability window is taken as 0.5 dB, and subjects to
uniform distribution, then
u(δLAW) = a
k = 0.5
√
3
dB = 0.29 dB
(10.5.23)
10.5.1.6
Uncertainty Introduced by Measurement Repeatability
Measurement system repeatability refers to the standard deviation of a series of
repeated measurement readings for a stable EUT. For example, in the CE102 50 kHz
frequency port voltage measurement, 10 independent measurements are performed
on the same stable EUT, the measured data are: 55.46, 55.28, 55.35, 55.21, 55.36,
55.44, 55.21, 55.32, 55.48, 55.25 dBμV, the arithmetic mean is 55.34 dBμV, and the
experimental standard deviation is 0.10 dB. In the actual measurement, it is generally
only measured once, that is, in practical applications, usually a single measurement
value is used as the ﬁnal measurement result. Therefore, in the uncertainty evalua-
tion, the standard deviation of a single measurement is used to express the standard
uncertainty, that is, the standard uncertainty is u = 0.10 dB. If the average value


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
453
is used as the measurement result, the standard uncertainty is u = 0.10 dB/√n, =
0.10 dB/
√
10 = 0.03 dB.
10.5.2
Evaluation and Analysis of Measurement Uncertainty
of Each EMC Item
10.5.2.1
CE101 Measurement Accuracy Inﬂuence Analysis
ThefollowingkeyinﬂuencequantitiesintheCE101measurementsshouldbenoticed:
(1) In the CE101 frequency range of 30 Hz to 10 kHz, the level amplitude is related
to the coupling mode of the receiver, which should be set to DC coupling in this
band. If AC coupling mode is set, the measured amplitude level of the receiver
is too small.
The DC voltage may damage the diode of the receiver mixer and cannot be
applied to the receiver. In order to measure the signal with a DC component, a
coupling capacitor needs to be added. However, the DC blocking capacitor may
cause power attenuation. The lower the frequency, the greater the attenuation is.
Therefore, the coupling capacitor is not suitable for extremely low frequencies,
and DC coupling is used instead, that is, there is no coupling capacitor between
the RF input and the ﬁrst mixer.
(2) In the CE101 frequency range of 30 Hz to 10 kHz, the margin between the
receiver’s noise level and the CE101 limit is relatively small, which requires to
use a current probe with appropriate transfer impedance, so that the EME level
of the CE101 test system is at least 6 dB lower than the speciﬁed limit. The
small signal-to-noise ratio (S/N) has a greater impact on the test results.
If the ambient level U0 is 6 dB lower than the EUT level U1, i.e., the ambient
level is half of the EUT level U0 = 0.5 U1, then the size of the synthesized
signal U2 is
U 2
2 = U 2
0 + U 2
1 = 0.25U 2
1 + U 2
1 = 1.25U 2
1
(10.5.24)
Taking the log of both sides and express them with decibels, it is known that U2
is 0.97 dB larger than U1, that is, when the EME level is 6 dB lower than the
speciﬁed limit, the deviation from the test result is 0.97 dB. Other corresponding
relationships can be similarly calculated, as shown in Table 10.4.
(3) Avoid 50 Hz power frequency interference to the measurement results. If the test
cable is transferred through the EMC chamber adapter plate, there are several
cases in which the 50 Hz power frequency exceeds the CE101 limit. At this
time, a current probe and a receiver can be directly connected by a cable that is
not connected through the chamber adapter plate.


454
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Table 10.4 Deviation dB
caused by signal-to-noise
ratio
dB value lower than the limit
Resulting deviation (dB)
1
2.539
2
2.124
3
1.764
4
1.455
5
1.193
6
0.973
10
0.414
20
0.043
30
0.004
(4) For large current loads, the CE101 measurement uses a LISN of 5 μH, the
measurement frequencybandis 30Hzto150kHz, andtheterminationfrequency
is 150 kHz, instead of 10 kHz.
10.5.2.2
CE102 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of CE102 measurements, the
following key inﬂuence quantities need to be noticed:
(1) Give priority to the test setup, especially the ground connection, including the
cable laying of the EUT, especially the grounding condition of the AC power
supply of the EUT, and the grounding of the LISN itself.
(2) Ensure that the correction factor is correct, including the cable, attenuator, and
the 0.25 μF voltage division coefﬁcient of the LISN.
(3) When calibrating the CE102 test system, the measurement values of the receiver
are required to be within ±3 dB of the injected signal level at 10 kHz, 100 kHz,
2 MHz, and 10 MHz. It should be noted that the impedance of the LISN is
relatively small at the two frequencies of 10 and 100 kHz (about 5.2  at
the frequency of 10 kHz, and about 25  at the frequency of 100 kHz), if
terminated with a 50  internal resistance signal source, its divided voltage is
smaller than the output voltage indicated by the actual signal source, and the
coaxial transmission line needs to split when connected to the LISN, which may
cause different degrees of attenuation to the two frequencies of 10 and 100 kHz.
Therefore, at the frequency of 10 kHz, the measurement value of the receiver is
about 15 dB smaller than the output indication value of the signal source; at the
frequency of 100 kHz, it is about 3 dB smaller than the output indication value
of the signal source. At the two frequencies of 2 and 10 MHz, the measurement
values of the receiver are basically consistent with the signal source injected
signal level.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
455
(4) When the LISN power supply output is connected to a terminal plate to supply
the EUT, make sure that the terminal plate is not ﬁltered with a lightning
protection, so as to avoid the test result being too small.
(5) The LISN used in the CE102 test speciﬁes the circuit diagram and the parameters
of the electronic components used, as shown in Fig. 10.12. But the parameters
of the civil LISN are different from the LISN used in CE102 testing, which may
cause deviations in the CE102 measurement results.
(6) When performing the CE102 test, the LISN monitoring terminal needs to termi-
nate a matching load. If a lower power LISN is used to match the load, it is easy
to cause damage to the matching load and incorrect resistance values, resulting
in a deviation of the measurement result.
(7) In the CE102 test, the receiver should be prevented from overload. The 20 dB
attenuator speciﬁed in the test method is used to protect the receiver. If there
is a possible overload, a suppression ﬁlter can be used to attenuate the power
frequency. Besides, a correction factor must be added to the transmitted data to
correct the insertion loss of the ﬁlter which is a function of frequency.
(8) Foralargecurrentload,theCE102measurementusesa5μHLISN,themeasure-
ment frequency band is 150 kHz to 10 MHz, and the starting frequency is
150 kHz instead of 10 kHz.
10.5.2.3
CE106/RE103 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of CE106/RE103 EM emission
measurements, the following key inﬂuence quantities are required to be noticed:
(1) When conducting the CE106 test to the transmitter and ampliﬁer and RE103
test to the transmitter in the transmitting state, the receiver may not use the test
bandwidth speciﬁed in Table 10.1. It can be adjusted according to the actual
operating frequencies of the test transmitter and ampliﬁer. The selected band-
width should ensure to measure the maximum signal. The bandwidth of the
receiver should maintain unchanged during measurements of the EM emissions
of all other frequency bands of CE106/RE103.
(2) When a rejection network is used to reject the fundamental frequencies of the
CE106 transmitter and ampliﬁer and the RE103 transmitter, other parts of the
frequency may also be rejected. In this case, the loss at other frequency bands
should be used as a correction coefﬁcient. In addition, each time when the
rejectionnetworkisadjustedtorejectdifferentmainfrequencies,thelossatother
frequency bands is different. It is necessary to use a vector network analyzer
to test the real-time loss, and introduce the test data into the test software of
CE106/RE103 as the correction coefﬁcient.
(3) Generally, the rejection bandwidth of the rejection network is narrow, smaller
than the transmission bandwidth of most current transmitters. If the test is only
for certain speciﬁc transmitters, special ﬁlters can be developed according to
the speciﬁc frequencies.


456
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(4) During the test, make sure that the input power of the transmitter is smaller than
the maximum input power of the receiver, so as to avoid damage to the receiver;
another condition that is uneasy to be aware is that, when the input signal
exceeds the linear working area of the receiver and falls into the nonlinear area,
harmonics, or intermodulation products may be generated inside the receiver,
resulting in incorrect measurement results. These signals are not the signals
of the EUT itself and may lead to misjudgments in this case. The source of
the intermodulation products of the receiver can be identiﬁed by adjusting the
receiver’s built-in attenuator. If the relative level of harmonics and intermod-
ulation products remains the same when the built-in attenuation is increased,
it indicates that the signal is from the EUT. If the relative level of harmonics
and intermodulation products changes, then indicates that some of the distortion
comes from the inside of the receiver, and the measurement results are incorrect.
10.5.2.4
CS101 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the CS101 power line test results,
the following key inﬂuence quantities are required to be noticed:
(1) During the CS101 test, it has been a difﬁcult point as to how to monitor the ripple
interference signals when using AC power supply on the EUT. The following
monitoring methods may be used: using a differential probe; using a band-stop
or a high-pass ﬁlter; using a high-voltage probe, but the oscilloscope needs to
ﬂoat; using a current probe and a spectrum analyzer; using a ripple monitor.
(2) In most cases, the audio power ampliﬁer requires to be protected since it often
operates under conditions of low impedance, mismatch, and high-power output.
The current generated on the primary winding of the coupling transformer by the
large current of the EUT may overload and damage the audio power ampliﬁer.
This problem can be solved either by adding another coupling transformer and
connecting a dummy load to the secondary stage of the coupling transformer
with the same current and opposite phase, or connecting a small load in the
primary stage of the coupling transformer in series to reduce the probability of
the audio power ampliﬁer matching a load with a particularly small impedance.
(3) When the circuit is initiated, the DC–DC power converter will generate a large
voltage at the primary stage of the coupling transformer, thereby damaging the
power ampliﬁer. One precaution is to connect a 5  resistor on the primary coil
and disconnect the transformer when the circuit is initiated, or power on the
power ampliﬁer after the DC–DC power converter is turned on.
(4) Whether the voltage level of the applied ripple signal measured on the EUT
power supply reaches the limit value, or the power value reaches the power
limit, it is considered that the CS101 requirement is met.
(5) Under the low impedance condition, the cable impedance has a greater inﬂuence.
In this case, the monitoring position of the applied ripple voltage should be as
close as possible to the input end of the EUT to reduce the inﬂuence of the
voltage division of the cable.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
457
(6) Prevent the injected signal waveform from distortion during the test. Saturation
of the power ampliﬁer or coupling transformer may cause waveform distortion,
make sure that the injected signal remains a sinusoidal signal.
10.5.2.5
CS103/CS104/CS105 Measurement Accuracy Inﬂuence
Analysis
In order to ensure the consistency and accuracy of the CS103/CS104/CS105 test
results, the following key inﬂuence quantities are required to be noticed:
(1) Ensure that the cable attenuation, three-port network insertion loss, and other
correction coefﬁcients are correct and are input to the test software.
(2) Ensure that the parameter settings of the receiver are correct, including the scan
stepping, coupling mode, etc.
10.5.2.6
CS106 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the CS106 power line spike
susceptibility test results, the following key inﬂuence quantities are required to be
noticed:
(1) Since the applied signal is continuous, according to Kirchhoff’s voltage law, the
voltage at the output of the transient signal generator is distributed over a loop
consisting of the EUT input impedance and the source impedance. Because part
of the induced voltage is distributed across the source impedance, the transient
signal level speciﬁed by the limit is measured at the EUT input. To reduce
the voltage drop across the source impedance, a 10 μF capacitor should be
connected across the power supply terminal.
(2) A 5  noninductive resistor is required for transient signal generator calibration.
Whether the transient signal level measured on the EUT input power line reaches
the limit value, or the transient signal generator reaches the calibration position,
it is considered that the CS106 requirement is met.
(3) MIL-STD-461F requires that the spike signal generator source impedance is no
larger than 2 , MIL-STD-462D: 1993 TEST METHOD STANDARD FOR
MEASUREMENT OF ELECTROMAGNETIC INTERFERENCE CHARAC-
TERISTICS requires that the source impedance of the spike signal generator is
0.06  under the condition of having an injection transformer.
(4) MIL-STD-461F requires that the peak voltage value (V p) of the spike signal
generator is 0–400 V, the peak value of the reverse voltage (V s) is ≤30% × V p,
the rise time (tr) is 1.5 μs ± 0.5 μs, fall time (tf) is (3.5 ± 0.5) μs, pulse width
(td) is 5.0 (1 ± 22%) μs, reverse pulse width (ts) is ≤20 μs, PRF is 3–10 Hz;
MIL-STD-461D: 1993 REQUIREMENTS FOR THE CONTROL OF ELEC-
TROMAGNETIC INTERFERENCE EMISSIONS AND SUSCEPTIBILITY
requires that the pulse width of the peak signal generator is 0.15, 5, 10 μs, and
the PRF is 3 pps to 10 pps.


458
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.5.2.7
CS114 Measurement Accuracy Inﬂuence Analysis
The CS114 test item involves many instruments and equipment and complicated
processes, and there are many factors affecting the test results. In order to ensure
the consistency and accuracy of the CS114 cable bundle injection test results, the
following key inﬂuence quantities are required to be noticed:
(1) Set an appropriate receiver bandwidth during the test, and ensure that the set
bandwidth meets the measurement requirements. In the case that the signal-to-
noise ratio does not affect the test result, the bandwidth setting value is based
on the maximum signal obtained by the test.
(2) Ensure the accuracy of the test conﬁguration. The center conductor of the cali-
bration device is susceptible to deformation or damage; it should be properly
maintained, regularly measured, and periodically inspected to ensure its normal
functions and indicators.
(3) Ensure that the insertion loss of the injection probe meets the standard require-
ments. The insertion loss of the injection probe has an inﬂuence on the consis-
tency of the test results; make sure that the insertion loss on the frequency band
used by the injection probe meets the standard requirements during the test,
especially in the frequency band of 10 kHz to 400 MHz when two injection
probes are used.
(4) Make sure that the probe status is correct during the test. The CS114 test item
uses an injection probe to the output signal and test the signal with a monitor
probe. These probes may affect the test result. Make sure that the probes are
in a good state; the two halves of the probe are well aligned and ﬁxed to avoid
forward/rear or left/right misalignment or untightened.
(5) The power ampliﬁer performance indicators are important parameters affecting
the CS114 signal output, including the power ampliﬁer’s noise level, the
harmonics, and the gain stability. Ensure that the performance indicators of the
power ampliﬁer are normal. Measures such as periodic metering, preheating for
a certain period of time before use, and adding an adjustable ﬁlter at the rear
end of the power ampliﬁer, can reduce the inﬂuence of the power ampliﬁer on
the test results.
(6) Attach importance to the impact of mismatch on the CS114 test. In CS114 test,
the mismatch affects the test results in many aspects, especially the mismatch
between the directional coupler and the injection probe (power output link). It
is recommended to monitor the reverse port of the directional coupler and its
impact. For systems with sufﬁcient output power, it is recommended to connect
an attenuator between the directional coupler and the injection probe to improve
the mismatch.
(7) Ensure that the LISN is terminated with a 50  matching load. In the CS114
test, the LISN should be terminated with a matching load and ensure that it is
50  or be conﬁgured with a large power load. The low-power load is easily
damaged, and needs to be inspected periodically.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
459
(8) Give priority to the veriﬁcation of the CS114 measurement system. Calibration
is the premise and important part of the CS114 test. Keep abreast of the test
system performance changes by accumulating veriﬁcation data.
10.5.2.8
CS115 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the CS115 cable bundle injection
pulse excitation test results, the following key inﬂuence quantities are required to be
noticed:
(1) Due to the Gibbs phenomenon, as shown in Fig. 10.53, when reading the ampli-
tude of the waveform, the maximum value of the glitch on the waveform angle
cannot be directly read by an oscilloscope, use a cursor for measurement instead.
(2) In the CS115 test, the real-time waveform is to be tested. If the current probe
frequency response is not smooth, the monitoring waveform will be distorted,
as shown in Fig. 10.54. It is recommended to use a current probe with a smooth
frequency response to transmission impedance.
(3) The accuracy of the test conﬁguration should be guaranteed. The center
conductor of the calibration device is susceptible to deformation or damage, it
should be properly maintained, regularly measured, and periodically inspected
to ensure its normal functions and indicators.
(4) Make sure that the probe status is correct during the test. The CS115 test item
uses an injection probe to output signal and test the signal with a monitor probe.
These probes may affect the test result. Make sure that the probes are in a good
state; the two halves of the probe are well aligned and ﬁxed to avoid forward/rear
or left/right misalignment or untightened.
(5) The veriﬁcation of the CS115 measurement system should be attached impor-
tance to. Calibration is the premise and important part of the CS115 test. Keep
Fig. 10.53 Gibbs phenomenon of the waveform


460
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
CS115 
Standard 
waveform
CS115 waveform
monitored by a
current probe with
non-smooth 
frequency 
response
Fig. 10.54 Waveform distortion
abreast of the test system performance changes by accumulating veriﬁcation
data.
10.5.2.9
CS116 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the CS116 cable and power line
damped sinusoidal transient test results, the following key inﬂuence quantities are
required to be noticed:
(1) The rated power of the attenuator and the current injection probe should meet
the requirements during the test to ensure that they will not be damaged by the
injected signal, and the performance will not be changed due to the excessively
large injected signal. The rated power of the attenuator generally refers to the
average power. The peak power and voltage caused by the injected susceptibility
signal may damage the attenuator. For example, for the CS116 limit value of
10 A, the attenuator will have a level as high as 500 V (10 A × 50 ) and
the corresponding peak power is 5 kW ((500 V)2/50 ). Similarly, the current
injection probe may change its magnetic properties due to a pulse signal.
(2) Whether the level of the damped sinusoidal signal measured on the EUT cable
reaches the limit value, or the damped sinusoidal signal generator reaches the
veriﬁcation output position, it is considered that the CS116 requirements are
met.
(3) Ensure the accuracy of the test conﬁguration. The center conductor of the cali-
bration device is susceptible to deformation or damage; it should be properly
maintained, regularly measured, and periodically inspected to ensure its normal
functions and indicators.
(4) Make sure the probe state is correct during the test. The CS116 test item uses an
injection probe to output signal and tests the signal with a monitor probe. These
probes may affect the test result. Make sure that the probes are in a good state;


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
461
the two halves of the probe are well aligned and ﬁxed to avoid forward/rear or
left/right misalignment or untightened.
(5) Attach importance to the veriﬁcation of the CS116 measurement system. Cali-
bration is the premise and important part of the CS116 test. Keep abreast of the
test system performance changes by accumulating veriﬁcation data.
10.5.2.10
CS118 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the CS118 ESD susceptibility test
results, the following key inﬂuence quantities are required to be noticed:
(1) The temperature and humidity of the test environment have a great inﬂuence on
the ESD. Make sure that the ambient temperature is between 15 and 35 °C and
the relative humidity is 30–60%.
(2) The discharge time interval shall be too small. It should be no less than 1 s to
ensure that the ESD transmitter has enough time to charge, and also to determine
whether the EUT has failed.
(3) The test conﬁguration has a great inﬂuence on the ESD. Ensure that the test
conﬁguration meets the standard requirements, including the metal grounding
plates, discharging resistors, grounding wires, etc.
10.5.2.11
RE101 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the RE101 magnetic ﬁeld emission
measurements, the following key inﬂuence quantities are required to be noticed:
(1) Ensure that the receiver parameter settings are correct, including the scan
stepping, coupling mode, etc.
(2) Use a correct loop antenna factor and latest loop antenna calibration data, and
timely update them in software.
10.5.2.12
RE102 Measurement Accuracy Inﬂuence Analysis
The RE102 test results are affected by many factors, including measurement equip-
ment and chamber environment. To ensure the consistency and accuracy of RE102
electric ﬁeld measurements, the following key inﬂuence quantities are required to be
noticed:
(1)
Ensure that the test conﬁguration is correct. The test conﬁguration has a signiﬁ-
cant impact on the RE test results. It is recommended that the reference labora-
tory is correctly conﬁgured, ensure that the receiving antenna remains vertical,
the test height is 1.2 m, the test distance is 1 m, and is placed at a position on the
platform with the least reﬂection effect, the test cables are arranged according
to speciﬁcations.


462
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(2)
It is recommended to add measurement calibration of the built-in ampliﬁer of
the receiver. With the increasing number of receivers with HF built-in ampli-
ﬁers (previously purchased receivers typically have ampliﬁers up to 3.6 GHz),
which have considerable deviations in testing; it is recommended to add the
calibration of the receiver’s built-in ampliﬁer in the reference laboratory during
the receiver measurement veriﬁcation.
(3)
Ensure that objects irrelevant to the test in the chamber do not affect the
test results. Metal reﬂectors have a signiﬁcant inﬂuence on the measurement
results. It is recommended to remove all objects irrelevant to the test out of
each reference laboratory’s semi-anechoic chamber during the test, especially
metal objects. If there are some objects that cannot be removed, they should
be placed as far as possible from the receiving antenna.
(4)
For the consistency of the test, it is recommended to use a receiving antenna that
complies with the recommended size of the MIL-STD-461G standard, because
the type and external dimensions of the antenna have a certain inﬂuence on the
test results.
(5)
Put the inﬂuence of coefﬁcient interpolation into the ﬁrst place. When the
calibration curve frequency interval of the measuring device is sparse and the
coefﬁcient ﬂatness of the measuring device is poor, the deviation introduced
by the coefﬁcient interpolation will be very large. It is recommended that each
EMC laboratory perform at least one test to the measurement device coefﬁcient
with a sufﬁcient frequency interval (whether by own or by a measurement
calibration agency) to evaluate the effect of coefﬁcient interpolation, especially
for low noise preampliﬁers with poor partial gain ﬂatness.
(6)
Prevent saturation of the low-noise preampliﬁer. When using a low-noise
preampliﬁer in testing, pay attention to its operating conditions, especially
the maximum allowable input power, to avoid saturation of the low noise
preampliﬁer and measurement errors.
(7)
Pay attention to the veriﬁcation of the RE102 measurement system. By veri-
fying the RE102 test system according to the MIL-STD-461G requirements,
it is possible to effectively ﬁnd problems in the receivers, cables, connectors,
etc., and avoid various mistakes. It is recommended that all military EMC labo-
ratories institutionalize the veriﬁcation of the regular test systems, and specify
the interval of the system veriﬁcation, the veriﬁcation conﬁguration, and the
criterion for abnormality of test results.
(8)
RE102 is not applicable to the transmitter’s fundamental frequency transmit
signal bandwidth or the range of ±5% fundamental frequency (whichever is
greater). If performing RE102 test on the transmitter, it is required to prevent
the receiver from overload or damage.
(9)
Both rod antenna veriﬁcation and rod antenna AF calibration use 10 pF capac-
itors, but the two capacitors are quite different, so do not mix them. The 10 pF
capacitor for veriﬁcation only conﬁgured with a 10 pF capacitor without other
components; while that used for AF calibration not only has a 10 pF capacitor,
but also a 39  resistor and a 10  resistor, and the calibration process is more
complex than the veriﬁcation and has more steps.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
463
Fig. 10.55 Alternate spacecraft RE limit 1—extended frequency and low emissions
(10) When there is a low background noise requirement in the electric ﬁeld RE test,
e.g., some concave frequency bands for Alternate Spacecraft Radiated Emis-
sions Limit speciﬁed by the AAIA S-121A-2017 Electromagnetic Compati-
bility Requirements for Space Equipment and Systems as shown in Fig. 10.55,
the electric ﬁeld RE limits are particularly small. For example, in the NASA
Deep Space operating band of 7150–7190 MHz, the electric ﬁeld RE limit is 20
dBμV/m, which requires the test system to have a low background noise ﬂoor.
In this case, one of the following methods or a combination thereof may be
taken: if the receiver has a built-in ampliﬁer in the test frequency band, turn on
the built-in low-noise ampliﬁer; properly reduce the receiver bandwidth (the
step size is set to less than or equal to half of the bandwidth, small bandwidth
test may double the test time); set the receiver’s built-in attenuator and the
minimum attenuation to zero, and the receiver automatic attenuation is auto-
matically checked to protect the receiver; use an external low noise ampliﬁer
and load the gain factor of the low noise ampliﬁer into the software.
10.5.2.13
RS101 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of the RS101 magnetic ﬁeld RE
measurements, the following key inﬂuence quantities are required to be noticed:
(1) If the measurement result is deviated due to correction coefﬁcient problems,
including those in the cables, receiving loop antennas, current clamps, etc., the
correction coefﬁcient needs to be highly cautioned.
(2) Pay attention to the test arrangement, including the state of the cable, the distance
of the antenna, and the position of the current clamp.


464
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(3) Attach importance to the calibration of the measurement system. By calibrating
the RE101 test system, it is possible to ﬁnd many mistakes and avoid the devia-
tion of the test results. It is recommended that the EMC laboratories institution-
alize the calibration work of the regular test systems, and specify the interval of
the system calibration, the calibration setup, and the criterion for test results.
(4) Ensure a stable output power of the audio power ampliﬁer. The output power
is not monitored in real time during actual testing. The audio power ampliﬁer
working in a nonlinear region may result in a large distortion of the waveform
output, so it should operate in the linear region to avoid deviation.
(5) The real-time monitored current during the RS101 test can reach above 10
amperes, an appropriate current probe should be used to avoid saturation and
deviation of the test result.
(6) Ensure that the parameter settings of the test instrument (the spectrum analyzer
or receiver) connected to the current probe is correct, including coupling mode,
bandwidth, and attenuation and detection mode.
10.5.2.14
RS103 Measurement Accuracy Inﬂuence Analysis
In order to ensure the consistency and accuracy of RS103 electric ﬁeld RE
measurements, the following key inﬂuence quantities are required to be noticed:
(1) The reﬂection of the chamber has an inﬂuence on the RS test results. Make sure
that the reﬂection of the chamber does not affect the test results, including the
reﬂection of the chamber itself, the metal plates, the cabinet, etc.
(2) Various types of ﬁeld strength probes have different performance (frequency
response, linearity of ﬁeld strength, etc.). Certain probes have poor frequency
response ﬂatness at some parts of the frequency band. Therefore, the measured
ﬁeld strength of the ﬁeld strength probe must be corrected with the correction
coefﬁcient.
(3) Different types of transmitting antennas have different dimensions; ensure that
the EUT is within the 3 dB beamwidth of the transmitting antenna, including
both the horizontally polarized and vertically polarized 3 dB beamwidth. If the
EUT cannot be covered in the 3 dB beamwidth of the transmitting antenna,
it can be achieved by moving the antenna or testing at multiple locations and
multiple times.
(4) Ensure that the power ampliﬁer’s harmonics, noise, and other performance do
not affect the test results.
(5) In the real-time ﬁeld strength feedback measurement, when the frequency band
is below 1 GHz, the ﬁeld strength probe may be seriously affected by the reﬂec-
tion of grounding metal plate and the EUT, so the probe must be 30 cm higher
than the grounding metal plate; when the frequency band is above 1 GHz, due
to the higher directivity of the antenna and smaller illuminating area, this effect
is not so obvious.


10.5 Measurement Uncertainty Analysis of Electronic Equipment EMC Test
465
(6) The RS103 test does not specify the speciﬁc test height of the transmitting
antenna, unlike the RE102 which speciﬁes the height of the receiving antenna
at 1.2 m, it only requires that the transmitting antenna is aligned with the EUT.
(7) It is speciﬁed in the speciﬁcation that the transmitting antenna is 1 m or more
away from the EUT. If the power ampliﬁer has sufﬁcient power, the transmitting
antenna can be placed farther away from the EUT, so that the 3 dB beamwidth
of the transmitting antenna has a larger coverage.
10.6
EMC Tests for Special Equipment
10.6.1
PCU EMC Test Methods
The power conditioning unit (PCU) is used to control, condition and protect the
spacecraft power subsystem, and provide an interface for other subsystems of the
spacecraft. Its normal operation is the basis to ensure the normal power supply of
all subsystems of the spacecraft. As one of the most important subsystems of the
spacecraft, the PCU has a very high power, especially with the development of large-
capacity satellite platforms, the power of the PCU has increased to tens of thousands
watts. Its conducted emission becomes a key area of concern for spacecraft EMC.
At present, the main PCU EMC power line CE test methods is performed according
to the MIL-STD-461G requirements. This is reasonable for radiated-type testing,
but there are many problems with conducted-type testing: First, due to the high-
power characteristics of the PCU, the CE102 test of its input power line is basically
exceeding the standard, and cannot accurately reﬂect the application characteristics
in the system; secondly, as a power supply equipment, the large number of output
power lines of the PCU are lack of testing. The RE characteristics of the output
power lines directly affect the EMC of the spacecraft equipment, but the CE102 test
is not applicable to the output lines; thirdly, for test items such as CS114, CS115,
and CS116, due to the small magnitude, it can hardly affect the high-power cables
such as the PCU power lines, so it seems unnecessary to test them. Therefore, adap-
tive modiﬁcation of the PCU conducted EMC test methods should be made based
on the conduction test methods. The following are the PCU conducted EMC test
requirements and methods.
10.6.1.1
Power Bus Frequency-Domain CE Test
The power bus frequency-domain CE test is mainly the PCU output line CE test, its
purpose is to examine and limit the CE interference generated by the PCU output
line that may be unbearable by the powered equipment from the frequency-domain
perspective. The working condition of the EUT requires that the PCU should operate
under at least two working conditions: the earth shadowed period condition and the


466
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
illuminated period battery charge regulation (BCR) condition, and the conditioning
shunt switch tube should operate at a duty ratio of 50%.
The power bus frequency-domain CE test frequency band ranges from 10 kHz to
10 MHz, and the test limit is shown in Fig. 10.56.
The test system conﬁguration is shown in Fig. 10.57. The test position is on
the PCU output power line, as close as possible to the PCU. The distance between
the power line and the ground plane is at least 5 cm. During the test, a differential
10
100
1000
10000
90
95
100
105
110
115
120
10kHz~10MHz,104
dBuV
KHz
Fig. 10.56 Test limits
Battery line
Solar array line
Output power bus
Differential 
probe
Oscilloscope
Receiver 
10μF capacitor
Fig. 10.57 Test conﬁguration


10.6 EMC Tests for Special Equipment
467
probe is connected to the positive and negative terminals of the PCU output line. An
oscilloscope is used to monitor the signal of the power line. After conﬁrmed to be
correct, the signal data is output through the oscilloscope DC blocking function, and
further ﬁltered by the DC blocking capacitor to ﬁlter out the DC component, then
tested with the receiver.
10.6.1.2
Power Bus Time-Domain CE Test
The power bus time-domain CE test mainly performs the PCU output line CE test.
The purpose of this test is to examine and limit the CE interference generated by
the PCU output line that may be unbearable by the powered equipment from the
time-domain perspective. The power bus time-domain CE test requires that the PCU
should operate under at least two working conditions: the earth shadowed period
condition and the illuminated period BCR condition, and the conditioning shunt
switch tube should operate at a duty ratio of 50%.
The limit requirements for the power bus time-domain CE test are
(1) When the measurement bandwidth is ≥50 MHz, the peak-to-peak value is
≤1.4 V;
(2) The spike duration ts ≤5 μs.
The test conﬁguration is shown in Fig. 10.58. The test position is in the PCU output
power line. During the test, the PCU output line is connected to a noninductive
simulated load, a current probe is connected to the power line for testing, and an
oscilloscope is used to monitor the test result. The oscilloscope bandwidth is required
to be no less than 100 MHz.
Battery line
Solar array line
Output power bus
Current probe
Oscilloscope
Fig. 10.58 Test conﬁguration


468
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Fig. 10.59 Test
conﬁguration
Receiver 
Current probe
Battery line
Solar array line
Output power bus
10.6.1.3
Battery Line CE Test
The battery line CE test mainly performs the PCU battery line CE test. The purpose
of this test is to examine and limit the CE interference generated by the PCU on
the battery line that may be unbearable by the battery from the frequency-domain
perspective. The battery line CE test requires that the PCU should operate under at
least two working conditions: the earth shadowed period condition and the illumi-
nated period BCR condition, and the conditioning shunt switch tube should operate
at a duty ratio of 50%.
The battery line CE test frequency range is 1 kHz to 50 MHz. If the switching
frequency and 4 times switching frequency are not within the test frequency range,
the test frequency range should be extended to include the switching frequency and
4 times switching frequency. The test limit requirements are
(1) <111 dBμA, at switching frequency;
(2) <99 dBμA, at frequencies other than the switching frequency.
The battery line CE test conﬁguration is shown in Fig. 10.59. The test is conducted
on the PCU battery line. The test mainly uses a current probe and a receiver. During
the test, the current probe is stuck on the battery line, and the receiver is used for test
data acquisition.
10.6.1.4
Solar Array Line CE Test
The solar array line CE test is performed on the PCU solar array line. This test aims
to examine and limit the CE interference generated by the PCU on the solar array
line that may be unbearable by the solar array. The solar array line CE test requires


10.6 EMC Tests for Special Equipment
469
Fig. 10.60 Test
conﬁguration
Output power bus
Battery line
Current probe
Solar array line
Oscilloscope
the PCU to operate in the S3R condition, and the conditioning shunt switch tube
operates at a 50% duty cycle.
The test limit requirement is current change rate dI/dt ≤10 A/μs.
The test conﬁguration is shown in Fig. 10.60. This test is performed on the PCU
solar array line, and a 500 nF capacitor is arranged at a distance of 1 m from the PCU.
Test equipment includes a current probe, a current converter, and an oscilloscope.
The current probe is connected to the solar array line, and the output is connected to
the oscilloscope through the current probe to perform the current transient conducted
characteristics test.
10.6.1.5
Load Transient CE Test
The load transient CE test aims to verify that when a PCU-powered equipment has a
state transition, the PCU power output line does not generate transient interference
that is unbearable by other powered equipment. This test is mainly performed when
the PCU is the earth shadowed period working condition.
Load transients CE test requirement is: dI/dt ≥1 A/μs. During the load transient
change, the bus voltage change rate requirement is: dV/dt ≤1 V/μs.
In addition to the bus voltage change rate requirements, the bus voltage change
requirements are shown in Fig. 10.61: when the load transient is greater than 400 μs
but not exceeding 4.5 ms, the bus voltage does not exceed the average bus voltage
±3 V; beyond 4.5 ms, the bus voltage does not exceed the average bus voltage ±0.3 V;
at any time, the bus voltage does not exceed the average bus voltage ±3.7 V.
The load transient CE test conﬁguration is shown in Fig. 10.62. This test is
performed on the PCU output power line. The load transient characteristics are simu-
lated using an electronic load. To avoid ground loops, a current probe ampliﬁer and
pulse signal generator are powered by an isolation transformer. When interference
is applied by the electronic load, the oscilloscope and the probe are used to monitor
the voltage change characteristics of the power line.


470
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
400
s
4.5ms
Voltage 
Average bus voltage +3.7V
Average bus voltage +3.0V
Average bus voltage +0.3V
Average bus voltage
Average bus voltage -0.3V
Time /s
Average bus voltage -3.0V
Average bus voltage -3.7V
Fig. 10.61 Voltage limit requirement
Battery line
Solar array line
Output power bus
Voltage probe
Current probe
Electric load
Pulse generator
Oscilloscope
Isolation
transformer
Fig. 10.62 Test conﬁguration
10.6.1.6
Power Bus CS Test
ThepowerbusCStestismainlyusedtotestandverifywhetherthePCUcanwithstand
the conducted EMI caused by various electrical equipment. The requirements for the
PCU state setting in this test are shown in Table 10.5.
The power line CS interference injection level is shown in Fig. 10.63. During the


10.6 EMC Tests for Special Equipment
471
Table 10.5 Test conﬁguration
Power (P/kW)
BDR quantity
CAPA quantity
SAS current min (A)
Curve
3 < P ≤6
3
1
2.5
1
6 < P ≤9
4
1
3
1
9 < P ≤12
5
1
3
2
12 < P ≤15
6
1
3.5
2
15 < P ≤18
7
1
3.5
2
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
3
10
4
50
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
μ
10Hz-508Hz
10Hz-508Hz
10kHz-200kHz
10MHz-50MHz
Curve 1
Curve 2
Voltage /dB
Frequency /kHz
Fig. 10.63 Magnitude of the interference injection
test, the peak-to-peak value of the bus ripple voltage is required to be less than 4.7 V,
and the PCU cannot be interfered.
The power bus CS test conﬁguration is shown in Fig. 10.64. This test is performed
on the PCU output power line. During the test, the interference injection signal is
of a square wave signal form within the frequency band of 30–500 Hz, and a sine
wave signal form within the frequency band of 500 Hz–50 MHz. A current probe and
a receiver are used to verify the magnitude of the interference injection. A voltage
probe and an oscilloscope are used to monitor the bus ripple characteristics on the
power line.


472
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(b) Sine wave signal test configuration 
Battery line
Solar array line
Output power bus
Current probe
Voltage probe
Resistor 
Oscilloscope
Receiver 
Power amplifier
Sine wave 
generator 
(a) Pulse signal test configuration
Battery line
Solar array line
Output power bus
Voltage probe
Current probe
Electric load
Oscilloscope 
Fig. 10.64 Test conﬁguration
10.6.1.7
Signal Line CS Test
The CS114, CS115, and CS116 tests are performed on the signal line of the PCU,
and the test magnitude and methods are the same as those required for the general
electronic equipment in EMC testing. For the power line, due to its large power, it is
not recommended to perform the CS114, CS115, and CS116 test.


10.6 EMC Tests for Special Equipment
473
10.6.2
Electric Propulsion EMC Test Method
As a new type of space power system, electric propulsion has a higher propellant
working substance utilization efﬁciency, which can greatly improve the orbital life-
time of spacecraft and has become an indispensable technical means for long-life and
high-reliability communication satellite engineering applications. There are a variety
of international satellite platforms that use electric propulsion. For example, the BSS-
601HP satellite platform uses four thrusters, the BSS-702 satellite platform uses the
electric propulsion system as a standard conﬁguration, and the LS-1300 satellite plat-
form uses four SPT-100 thrusters. While the application of electric propulsion does
improve the satellite capabilities, it also has compatibility problems with the satellite,
one of which is the EMC problem. During normal operations, the electric propul-
sion system will produce steady-state CE and RE on the power line, that means, the
electric propulsion system will generate steady-state conducted interference and radi-
ated interference; moreover, the electric propulsion system will have state switching
during operation, which, on the one hand, will cause voltage and current ﬂuctuations
of the system, and on the other hand, will cause changes in radiated emissions. There-
fore, the electric propulsion system will generate transient-conducted interference
and transient-radiated interference. The plume generated during the operation of the
electric propulsion system can be regarded as an anisotropic medium; its parameters
are characterized by
ω2
p = Nee2
ε0me
(10.6.1)
εeq =

1 −
ω2p
ω2
(10.6.2)
where ωp is the frequency of the plume;
Ne is the local area particle density;
e, me are the charge and particle mass.
This medium has an impact on the electromagnetic wave characteristics of
spacecraft communications:
(1) Amplitude attenuation effect: affecting the communication signal strength;
(2) Time lag effect: affecting signal propagation time.
In view of the EMI characteristics of the electric propulsion system, the electric
propulsion technology is mainly used on communication satellites. The EMC prob-
lems of the propulsion system in the communication satellites include: the inﬂu-
ence of the CE on the satellite; the CE self-compatibility of the propulsion system;
the inﬂuence of the steady-state RE of the propulsion system on the satellite; the
radiated effect of the state switching process on satellite; the effect of the plume


474
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
CP
O
X
Y
Thruster
Wave obsorbing 
material
Wave penetrating tank
Wave-obsorbing wall
(for blocking the shielding gate of 
the chamber)
Shielding gate
Fig. 10.65 Test conﬁguration
generated during the propulsion system operation on the amplitude attenuation of
the communication EM wave.
It is also necessary to consider the different test requirements with conventional
electrical equipment in an EMC chamber. The thruster must be tested under vacuum
conditions. An example of a test environment is given in Fig. 10.65, where the ion
thruster is placed in a wave penetrating tank, which is again placed in the EMC
chamber. Normally, the wave penetrating tank installed in the chamber will damage
the shield of the chamber to some extent, resulting in a decrease in the shielding
effectiveness of the chamber. Therefore, when performing a radiated-type EMC test,
it is necessary to test the EME of the chamber before the formal test to reduce its
impact on the test results.
According to the test environment requirements of the electric propulsion system
and the EMC requirements of the satellite, the EMC test items of the electric propul-
sion system mainly include: the wave penetrating tank penetrance test, the steady-
state CE test of the electric propulsion system, and the transient CE test of the electric
propulsion system, the steady-state RE test of the electric propulsion system, the
transient RE test of the electric propulsion system and the test of the inﬂuence of
electromagnetic propulsion plume on communication EM wave. The descriptions of
these tests are as follows.


10.6 EMC Tests for Special Equipment
475
10.6.2.1
Wave Penetrating Tank Penetrance Test
The wave penetrating tank penetrance test is mainly to test the penetrance of the
corresponding position of the wave penetrating tank in which the thruster works.
The purpose of the test is to evaluate the wave penetrating characteristics of the wave
penetrating tank, so as to accurately assess the measured EM radiation characteristics
of the thruster. The test positions should be selected between the thruster installation
position and the test antenna. Usually, the penetrance tests are performed at two
positions: the end surface and the sidewall of the wave penetrating tank.
The test conﬁguration is shown in Fig. 10.67, the penetrance of the wave pene-
trating tank is obtained by comparison. Two sets of antennas are used for transmitting
and receiving EM waves. First, place the two antennas inside and outside of the wave
penetrating tank, respectively. The internal antenna is placed at the position where
the thruster is installed, the external antenna is placed at the position of the RE test
antenna (the thruster RE test distance is generally required to be 1 m, so the distance
between the two antennas should also be 1 m). In addition, a vector network analyzer
is used in the test. Obtain the transmission of the EM wave (the transmission char-
acteristics of the penetrating tank) passing through the entire test system of the wave
penetrating tank from the S21 measurement result of the vector network analyzer.
Then, remove the receiving and transmitting antennas from the wave penetrating
tank, and place them at the same distance from the previous step, ensure there is no
obstruction between the antennas, and then perform the S21 measurement. Use the
measurement result as the reference data (the reference transmission characteristics).
By comparing the two measurement results, that is, the transmission characteristics
of the wave penetrating tank and the reference transmission characteristic data, the
inﬂuence of the wave penetrating tank on the EM wave propagation, i.e., the pene-
trance of the wave penetrating tank is obtained. The test schematic is shown in
Fig. 10.66.
In the wave penetrating tank penetrance test, because the test environment and
the characteristics of the receiving and transmitting antennas will cause certain
interference to the test results, it is necessary to process the test data, the speciﬁc
processing methods are basically the same as the test of the impact of the plume on
the communication EM waves, and will be explained in the following sections.
10.6.2.2
Steady-State CE Test of the Electric Propulsion System
The purpose of the steady-state CE test of the electric propulsion system is to test the
primary power CE characteristics of the electric propulsion system to assess whether
it will affect the primary power supply of the satellite. During the test, the primary
power supply bus of the PPU is powered by the power supply LISN, and the electric
propulsion system operates in a stable state. The test block diagram is shown in
Fig. 10.67.
To ensure the comprehensiveness of the test, the electric propulsion system can
be set to different operating modes and tested in each mode.


476
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(a) Wave penetrance test on the penetrating tank end surface
(b) Wave penetrance test on the penetrating tank side wall
Transmitting 
antenna
Receiving 
antenna
Wave penetrating tank
Vacuum tank
Vector network analyzer
Vacuum 
tank
Transmitting 
antenna
Receiving 
antenna
Vector network analyzer
Wave penetrating 
tank
Fig. 10.66 Diagram of wave penetrating tank penetrance test


10.6 EMC Tests for Special Equipment
477
20dB 
attenuator 
Power input
LISN
Measurement 
receiver
PPU primary bus 
Fig. 10.67 Block diagram of steady-state CE test of the electric propulsion system
10.6.2.3
Transient CE Test of Electric Propulsion System
The electric propulsion system transient CE test is conducted on the primary power
line of the propulsion system and the PPU power output line to evaluate whether
the propulsion system will cause transient-conducted interference in the primary
power line and whether the ﬂuctuations in the PPU output power line will affect the
equipment powered by the PPU during different operating modes or mode switching.
This test reﬂects conducted EMC within and outside the propulsion system. The
transient CE test of the electric propulsion system is mainly to test the transient
characteristics during the modes switching.
The transient CE test of the electric propulsion system is divided into two
conditions:
(1) Transient current test: connect the current probe to the input and output lines of
the PPU, set the oscilloscope to the trigger mode, and capture the surge current
by the oscilloscope during the mode switching of the electric propulsion system.
The test block diagram is shown in Fig. 10.68.
(2) Transient voltage test: in some high-voltage lines, since the current is very
small, it is difﬁcult to measure the transient current. In this case, the transient
voltage test can be performed. During the test, connect the high-voltage probe,
set the oscilloscope to the trigger mode, and capture the surge voltage by the
oscilloscope during the mode switching of the electric propulsion system. The
test block diagram is shown in Fig. 10.69.
Figure 10.70 shows a picture of the transient CE test. During the high-voltage line
test, pay special attention to safety matters, including the safety of both the test
personnel and the equipment in the high-pressure environment.


478
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Positive line of 
the LISN
Return line of the 
LISN
Oscilloscope 
Current probe
PPU power line 
Fig. 10.68 Block diagram of transient current test
Oscilloscope 
Positive line of 
the LISN
Return line of the 
LISN
High-voltage probe
PPU power line 
Fig. 10.69 Block diagram transient voltage test
10.6.2.4
Steady-State RE Test of the Electric Propulsion System
The steady-state RE test of the electric propulsion system aims to test the unin-
tentional electromagnetic RE during the stable operation of the system to evaluate
whether it will affect the spacecraft system and other subsystems and equipment. The
test is performed under the condition that the electric propulsion system operates in a
stable state, using a receiving antenna, a preampliﬁer, and a receiver at two positions


10.6 EMC Tests for Special Equipment
479
Fig. 10.70 Testing pictures
(a) Picture of the transient current test
(b) Picture of transient voltage test
of the wave penetrating tank 1 m away from the ion thruster. The test block diagram
is shown in Fig. 10.71, and the system test schematic is shown in Fig. 10.72.
To ensure the comprehensiveness of the test, the test can be conducted in different
operating modes of the electric propulsion system.
10.6.2.5
Transient RE Test of Electric Propulsion System
The electric propulsion system transient RE test is to test the unintentional electro-
magnetic RE of the electric propulsion system during the working state or working
mode switching to evaluate whether it will affect the spacecraft system and other
subsystems and equipment. It is required is to test the transient process of state
switching. The test is generally divided into two cases:


480
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
ESU40 i
Active rod antenna
HFH2-Z6
Preamplifier 
SCU01
Preamplifier 
SCU18A
Preamplifier 
SCU26
Preamplifier 
SCU40
Biconical antenna 
HK116
Bi-ridge horn antenna 
EATON96000
Bi-ridge horn antenna 
E03115
Horn antenna QSH20S20
Horn antenna QSH22k20
Fig. 10.71 Test block diagram
Vacuum tank 
Position 1
Antenna
Antenna 
EM 
radiation 
property 
test device
Position 2
Wave 
penetrating 
tank
Fig. 10.72 System test schematic diagram
(1) Frequency-domain (FD) test: a ground antenna and a spectrum analyzer are
adopted. The spectrum analyzer is set to the maximum holding mode during
the electric propulsion system working mode switching to test the FD transient
RE. The test block diagram is shown in Fig. 10.73.
(2) Time-domain (TD) test: a ground antenna and an oscilloscope are adopted to test
in the frequency range of 10 kHz to 30 MHz. The oscilloscope is set to the trigger
mode to test the TD transient RE during the electric propulsion system working
mode switching. The test block diagram is shown in Fig. 10.74. During the
test, pay attention to the power supply settings of the oscilloscope to eliminate
interference from the ground power supply. Also, note that the sensitivity of
the spectrum analyzer and the oscilloscope is different. If the signal is large, an


10.6 EMC Tests for Special Equipment
481
Spectrum 
analyzer
Active rod antenna
HFH2-Z6
Preamplifier 
SCU01
Preamplifier 
SCU18A
Preamplifier 
SCU26
Preamplifier 
SCU40
Biconical antenna 
HK116
Dual-ridge horn antenna 
EATON96000
Dual-ridge horn antenna 
E03115
Horn antenna QSH20S20
Horn antenna QSH22k20
Fig. 10.73 Block diagram of FD transient RE test


482
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Oscilloscope 
Active rod antenna HFH2-Z6
Fig. 10.74 Block diagram of TD transient RE test
Measurement  
Max. electricity
When rising
When falling
Min. electricity
At present 
Average 
Minimum 
Maximum 
Standard 
deviation
Count 
Fig. 10.75 Time-domain test results
attenuator should be added. In the time-domain test, the preampliﬁer of the rod
antenna should be turned off.
Figure 10.75 shows the time-domain test results curve.
10.6.2.6
Test of Inﬂuence of Electrical Propulsion Plume
on Communication
The plume generated during the electric propulsion operation will affect the EM
waves passing through it. Therefore, this test mainly tests the inﬂuence of the plume
on the communication EM wave as well as on the amplitude and delay of the commu-
nication EM wave. Two sets of antennas are used as the transmitting and the receiving
antenna, respectively, and are placed on both sides of the wave penetrating tank. The
antenna face should be as close as possible to the wave penetrating tank to reduce
the inﬂuence of the environment, and the two antennas point to each other, so that
the plasma plume passes through the EM wave transmission path. Connect the two
antennas to the vector network analyzer via a cable, and read the S21 results from the
analyzer under different working states of the electric propeller, which reﬂects the


10.6 EMC Tests for Special Equipment
483
transmission of the entire system link. Compare the effects of plasma plumes on trans-
mission in different states. The test block diagram is shown in Fig. 10.76. During the
test, the effects of the plume on the EM wave are usually tested in two scenarios: the
Fig. 10.76 Inﬂuence of
plume on communication
EM wave amplitude and time
delay
(a) Vertical layout
(b) Oblique layout
Vacuum tank
Vacuum 
tank
Plasma plume
Plasma plume
Vector network analyzer
Vector network analyzer
Transmitting antenna
Transmitting 
antenna
Receiving antenna
Receiving 
antenna
Propeller 
Propeller 
Wave penetrating tank
Wave penetrating tank


484
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
simulated EM wave passes through the plume vertically and obliquely. When eval-
uating the inﬂuence of the plume on the amplitude and delay of the communication
EM wave, the two antennas need to be co-polarized.
The electric propulsion will produce different plumes under different grid supply
voltages and beam currents. The grid supply current affects the ion velocity of the
plume, and the grid beam current affects the ion concentration of the plume, and
thereby affect the characteristics of the plume. To this end, during the test, the
impact of the plume generated by different combinations of voltage and current on
communication will be tested according to the requirements of the working mode.
Figure 10.77 shows the test results of the effects of plume generated by an electric
propulsion system on 1–5 GHz EM waves.
Similar to the data processing of the wave penetrance test, the test data of the inﬂu-
ence of the plume on the communication EM wave test must also be processed due
to the multipath interference from the environment and test antenna sidelobes. In the
data processing system, the data obtained from the test is a frequency-domain signal,
while the distance gate is an application in the time domain. The data processing
process is shown in Fig. 10.78. The entire data processing includes a process of FD
data →TD data →FD data.
10.6.3
PIM Test Method
10.6.3.1
Precautions for PIM Test
(1)
ThePIMtestneedstousecontinuouswave(CW),makesurethattheconnection
is tight;
(2)
This test generally uses a two-way carrier. Alternatively, it can also be
conducted in a multi-carrier state, which requires a multichannel frequency
synthesizer and additional equipment such as a signal source, a CW power
ampliﬁer;
(3)
Do not connect the EUT before the test. The PIM level of the system itself
is ﬁrst tested; the return loss of the absorbing material of the low PIM wave-
absorbing chamber is required to be lower than −25 dB; the PIM level of the
low PIM wave-absorbing chamber is at least 10 dB lower than the PIM of the
EUT;
(4)
Pay attention to the safety of high- and low-temperature test equipment, due
to the lack of self-protection awareness of oxygen deﬁciency in a nitrogen
environment, special attention should be paid to the safety of test personnel
during low-temperature liquid nitrogen ﬁlling;
(5)
Since fasteners such as metal screws are PIM sources, they cannot be used
in the low PIM chamber. Nylon cables or wooden structures can be used for
chamber construction;
(6)
PIM detection system capability veriﬁcation: connect the PIM source at the
location where the EUT is to be connected, detect the PIM level on the spectrum


10.6 EMC Tests for Special Equipment
485
(a) Plume transmission characteristics as a function of voltage (vertical layout)
1
1.5
2
2.5
3
3.5
4
4.5
5
-1.5
-1
-0.5
0
0.5
1
1.5
2
2.5
3
3.5
4
4.5
5
0
10
20
30
40
50
800V
900V
1000V
1100V
1200V
1300V
1400V
1500V
Frequency (GHz)
Frequency (GHz)
Plume transmission characteristics as a function of voltage (vertical layout)
Transmission factor 
difference (dB)
Transmission phase 
difference (°) 
(b) Plume transmission characteristics as a function of voltage (vertical layout)
Plume transmission characteristics as a function of voltage (vertical layout)
Frequency (GHz)
Frequency (GHz)
Transmission factor 
difference (dB)
Transmission phase 
difference (degree)
Voltage (V)
Voltage (V)
Fig. 10.77 Test results


486
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
(c) Plume transmission characteristics as a function of beam current (oblique layout)
1
1.5
2
2.5
3
3.5
4
4.5
5
-4
-3
-2
-1
0
1
1.5
2
2.5
3
3.5
4
4.5
5
0
20
40
60
80
100
0.6A
0.7A
0.8A
0.9A
1A
1.1A
1.2A
Frequency (GHz)
Plume transmission characteristics as a function of current (oblique layout)
Frequency (GHz)
Transmission factor 
difference (dB)
Transmission phase 
difference (°)
(d) Plume transmission characteristics as a function of beam current (oblique layout)
Plume transmission characteristics as a function of current (oblique layout)
Frequency (GHz)
Transmission factor 
difference (dB)
Transmission phase 
difference (°)
Voltage (V)
Voltage (V)
Frequency (GHz)
Fig. 10.77 (continued)


10.6 EMC Tests for Special Equipment
487
FD data
Window data
Inverse Fourier
transform
TD data
Distance 
gate
Fourier 
transform
FD data
Fig. 10.78 Data processing sequence
analyzer;forradiationorre-radiationPIMtest,thePIMsourceshouldbeplaced
at the front end of the EUT in the low PIM chamber; change the frequency
values of the two signals f 1 and f 2, and check whether the PIM frequency
value detected by the test system changes with f 1 and f 2, and whether it is
consistent with the calculated result;
(7)
The receiving sensitivity of the spectrum analyzer used in the PIM detection
system is required to be less than −130 dBm, and the resolution bandwidth can
be up to 1 Hz; the equipment used in the test such as the frequency synthesizer,
transceiver duplexer, low PIM ﬁlter, receiving ﬁlter, high-power load are all
required to have low PIM design;
(8)
Re-radiation PIM test is suitable for testing the PIM level generated by RF
components and equipment exposed in the EM ﬁeld of RF signal transmission,
such as antenna reﬂection surface, reﬂective surface test samples, antenna
support structure, reﬂective surface support arm, antenna insulation protection
hardware (e.g., insulation felt pad), complete satellite insulation protection
hardware;
(9)
The low PIM RF components and equipment used in the test should be prop-
erly protected with clean protective cap or special tape during storage to
avoid contamination or air oxidation, which may result in a decrease in PIM
performance;
(10) Clean the EUT, the RF component of the test system and the coaxial connector
or waveguide interface of the connection cable with absolute ethanol before
the test;
(11) During the test connection between the RF components and equipment,
stress on the coaxial connector or the waveguide interface should be avoided,
otherwise the test result of the EUT PIM performance will be affected;
(12) KeepthePIMwave-absorbingchambercleanandavoidunnecessaryimpurities
such as wire and slag falling into the wave-absorbing chamber, causing the PIM
level of the PIM chamber to rise;
(13) During the interval of the radiation or re-radiation PIM test, check the temper-
ature change of the local wave-absorbing material in the low PIM wave-
absorbing chamber to avoid excessive radiated power for a long time, causing
the temperature of the local wave-absorbing material to rise, eventually leading
to a wave-absorbing material ﬁre accident.


488
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.6.3.2
PIM Measurement System
The equipment-level PIM measurement system is mainly divided into transmis-
sion measurement method, reﬂection measurement method, radiation measurement
method, and re-radiation measurement method.
(1) Transmission measurement method
The transmission measurement method is characterized by a relatively simple prin-
ciple, intuitive connection block diagram and easy to implement, and can be used
for PIM measurement of common dual-port microwave components, as shown in
Fig. 10.79.
(2) Reﬂection measurement method
Reﬂection measurement method allows for measurement of most non-radiative
single-port, dual/multi-port components on the satellite, and the PIM measure-
ments of the antenna itself and the feed, such as antennas, beam-forming networks,
duplexers, coaxial cables, high-power loads, adapters, isolators. As shown in
Fig. 10.80, this method is used as a general measurement method for general compo-
nents and subsystems. It is especially important that the antenna and its feed are one
Signal 
source1
Signal 
source2
Power 
amplifier1
Power 
amplifier 2
Synthesizer
Filter
EUT
Spectrum 
analyzer 
Fig. 10.79 Transmission measurement method
Signal 
source1
Signal 
source2
Power 
amplifier1
Power 
amplifier2
Synthesizer
Coupler
EUT
Load
Filter
Spectrum 
analyzer 
Fig. 10.80 Reﬂection measurement method


10.6 EMC Tests for Special Equipment
489
Signal 
source2
Power 
amplifier2
Signal 
source1
Power 
amplifier1
Synthesizer
Filter
Spectrum 
analyzer 
Wave-absorbing chamber
Receiving 
antenna
Radiating
EUT in 
thermost
Fig. 10.81 Radiation measurement method
of the main sources of satellite PIM, so this method is the most important for satellite
PIM measurements.
(3) Radiation measurement method
Radiation measurement method allows for the measurement of components with
energy radiation function, such as horn, vibrator, spiral, microstrip antennas, and
reﬂector antenna and array antenna installed with main feed. In an effort to prevent
external EMI and improve the accuracy and reliability of measurement data, the radi-
ating components are required to be placed in the shielded wave-absorbing chamber.
The PIM temperature cycle experiments can use standard laboratory general-purpose
thermostat. This method needs to use the corresponding receiving antenna to detect
the PIM, so the measurement result is the total PIM value of the radiating component
and the receiving antenna, as shown in Fig. 10.81.
(4) Re-radiation measurement method
The re-radiation measurement method is used to measure the PIM generated by
components irradiated by the RF signal in an open space, such as PIM test for
antenna reﬂection surface, antenna support structure, support rod, antenna thermal
control ﬁlm, ﬂight vehicle structure, and propeller. It needs a special thermal cycle
chamber, a wave-absorbing chamber, and a receiving antenna to detect the signals.
Since the actual application is exposed to open space, which requires determining
the measurement environment, the thermal cycle chamber and the wave-absorbing
chamber used for the measurement should be assessed, evaluated, and compared with
the results of the evaluation algorithm. The measurement requires special facilities,
and the measurement results have to be converted, therefore, it is not suitable for the
PIM measurement of general components. The test method is shown in Fig. 10.82.


490
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
Signal 
source1
Power amplifier1
Filter 
Spectrum analyzer
Transmission 
antenna
Wave absorbing chamber
Receiving 
antenna
Filter
EUT
Signal 
source2
Power amplifier2
Filter
Transmission antenna
Fig. 10.82 Re-radiation measurement method
10.6.4
Secondary Emission Multiplication Test Method
(1) Secondary emission multiplication effect is a vacuum discharge phenomenon
that occurs in the RF alternating occasions between two faces, caused by
secondary electron emission. For RF components and equipment, this is often
found in the small gaps of sensitive parts where alternating electric ﬁelds exist.
(2) Multipaction test threshold value: When a secondary emission multiplication
effect occurs in the RF component and the device, the peak voltage value,
threshold value, and threshold value analysis calculated by added RF peak power
are all given by a single-carrier status.
(3) Peak power: It is used only for the single-carrier operating state, and it is the
pulse peak power of the single-carrier pulse signal.
(4) Peak envelope power: It is used only for the multi-carrier operating state. It is
the maximum envelope peak power of the multi-carrier composite signal under
in-phase synthesis state, and is expressed by (n2P).
(5) Average power: In the single-carrier operating state, it is the equivalent average
power of the single-carrier pulse signal; in the multi-carrier operating state, it
is the sum of the single-carrier powers of each channel, PV =
N
i=1
Pi.
(6) P20 power: The time during which electrons travel between the gaps 20 times
is deﬁned as T 20, and then the maximum power level with T 20 dwell time in a
synthesis envelope period is the P20 power.
10.6.4.1
Secondary Emission Multiplication Effect Veriﬁcation
1. Basic requirements for veriﬁcation
The secondary emission multiplication effect (multiplication performance) of space-
craft RF components and equipment needs to be sufﬁciently veriﬁed to prove that
the product meets the margin requirements at each development stage, including the


10.6 EMC Tests for Special Equipment
491
analysis margin requirements in the design phase and the test margin requirements
in the delivery phase. It is usually veriﬁed at component level, but is also allowed to
verify at the subsystem level.
2. Veriﬁcation phases and levels
The veriﬁcation phases of the secondary emission multiplication effect (multiplica-
tion performance) of spacecraft RF components and equipment include the analytical
veriﬁcation at the design phase, the evaluation-level test veriﬁcation for the evalu-
ation product, and the acceptance test veriﬁcation for the PFM and ﬂight model
product.
For products that do not meet the test veriﬁcation conditions, they are allowed to be
veriﬁed only by means of analytical veriﬁcation, however, the margin requirements
for analytical veriﬁcation is required to be met.
3. Veriﬁcation speciﬁcations
For the secondary emission multiplication effect (multiplication performance) of
spacecraft RF components and equipment, it is necessary to develop veriﬁcation
plans and speciﬁcations so that the product is fully veriﬁed for this effect in order to
sufﬁciently indicate the safety of the product during on-orbit operation.
The veriﬁcation plans and speciﬁcations should be developed in the early stage
of product design, updated according to the speciﬁc conditions of different stages,
and controlled in a continuous valid state.
4. Ways of veriﬁcation
The veriﬁcation of the secondary emission multiplication effect (multiplication
performance) of spacecraft RF components and equipment includes the following
three ways:
(1) Analytical veriﬁcation only;
(2) Evaluation-level test veriﬁcation only;
(3) Acceptance-level test veriﬁcation only.
For critical RF components and equipment, unless they surely cannot meet test
veriﬁcation conditions, they are allowed to be veriﬁed only by analytical veriﬁca-
tion; for products that meet test veriﬁcation conditions, in addition to the analyt-
ical veriﬁcation in the initial design, their secondary emission multiplication effect
(multiplication performance) is required to be veriﬁed by the test veriﬁcation method.
5. Product classiﬁcation
Spacecraft RF components and equipment can be divided into the following three
categories:
Category I: the RF transmission paths of the products are composed of metals
whose secondary electron emission performance is known, or whose metal surfaces


492
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
have been subjected to nonorganic treatment in order to increase the multiplication
threshold;
Category II: the RF transmission paths of the products contain mediums or
other materials whose secondary emission multiplication effect (multiplication
performance) are known.
Category IIII: products other than the ﬁrst and second categories.
6. Single-carrier operating state product
(1) Veriﬁcation margin requirements
For products with a single-carrier operating state, the secondary emission multipli-
cation effect veriﬁcation margin requirements are shown in Table 10.6.
(2) Veriﬁcation process
For the single-carrier case, the secondary emission multiplication effect veriﬁcation
process is shown in Fig. 10.83. The conditions for the analysis are
(1) There has been a similar product design that has been veriﬁed before;
(2) The geometry of the device allows for accurate electric ﬁeld calculations;
(3) The multiplication sensitive area of the device is identical to a known design,
and there is an established relationship between the analysis results and the test
results of this known design.
7. Multi-carrier operating state product
(1) Veriﬁcation margin requirements
For products with a multi-carrier operating state, due to the current limited research
level, the secondary emission multiplication effect veriﬁcation margin requirement is
only proposed for the Category I products, as shown in Table 10.7. For the Category
II and III products, additional veriﬁcation margin requirements are needed.
For Category I products, if the secondary emission multiplication effect threshold
is higher than the peak envelope power (n2P), the veriﬁcation margin is determined
on the basis of the relative peak envelope power according to Table 10.7. If the
threshold is lower than the peak envelope power (n2P), the veriﬁcation margin is
determined by reference to the higher power value of P20 or the average power PV,
as shown in Table 10.8.
Table 10.6 Secondary emission multiplication effect veriﬁcation margin for single-carrier
operating state product
Way of veriﬁcation
Veriﬁcation margin (dB)
1
Analytical veriﬁcation
8
10
12
2
Evaluation-level veriﬁcation
6
6
10
3
Acceptance-level veriﬁcation
3
3
4


10.6 EMC Tests for Special Equipment
493
Start of 
verification
Analyze
Do the analyze 
conditions met?
Analysis margin
Cat. I > 8dB
Cat. II > 10dB
Cat. III > 12dB
Evaluation test?
Test margin
Cat. I > 6dB
Cat. II > 6dB
Cat. III > 10dB
Acceptance test?
Test margin
Cat. I > 3dB
Cat. II > 3dB
Cat. III > 4dB
Verification
failed
Verification
passed
Yes
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
No
No
No
Fig. 10.83 Veriﬁcation process for the single-carrier case
Table 10.7 Multi-carrier
secondary emission
multiplication effect
veriﬁcation margin (the
threshold is higher than the
peak envelope power)
Way of veriﬁcation
Veriﬁcation margin (dB)
(relative to peak envelope
power)
1
Analytical veriﬁcation
6
2
Evaluation-level veriﬁcation
3
3
Acceptance-level veriﬁcation
0
Table 10.8 Multi-carrier
secondary emission
multiplication effect
veriﬁcation margin (threshold
is lower than peak envelope
power)
Way of veriﬁcation
Veriﬁcation margin (dB)
(relative to the higher power
of P20 or PV)
1
Analytical veriﬁcation
6
2
Evaluation-level veriﬁcation
6
3
Acceptance-level veriﬁcation
4


494
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
State of 
verification
Analyze?
Do the analysis 
conditions met?
Analysis margin
Cat. I > 6dB
Evaluation
test?
Test margin
Cat. I > 3dB
or > 6dB
Acceptance
test
Test margin
Cat. I > 0dB
or > 4dB
Verification
failed
Verification
passed
Yes
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
No
No
No
Fig. 10.84 Veriﬁcation process for multi-carrier case
(2) Veriﬁcation process
For the multi-carrier case, the veriﬁcation process of the secondary emission multi-
plication effect (multiplication performance) is shown in Fig. 10.84. The conditions
for analysis are the same as the single-carrier case.
10.6.4.2
Analysis Method
1. Electric ﬁeld strength analysis
The EM ﬁeld full-wave numerical simulation calculation software can be used to
calculate the ﬁeld strength value in the RF path of the product. It is required to
calculate and determine the ﬁeld strength values of all working frequencies of the
product at possible gaps.


10.6 EMC Tests for Special Equipment
495
2. Material and surface treatment status
Check and conﬁrm the material and surface treatment status of the product to deter-
mine the secondary emission state of the material and surface treatment during the
analysis of the secondary emission multiplication effect.
3. Identiﬁcation and determination of critical areas
The critical areas of the secondary emission multiplication effect should be identiﬁed
and determined for all critical parts of the product RF path.
The critical areas can be identiﬁed and determined by the following factors:
(1) Local ﬁeld strength value (voltage value);
(2) Locations of all critical gaps;
(3) All working frequencies;
(4) Secondary emission state of the material and surface treatment.
4. Susceptibility analysis of secondary emission multiplication effect
The dedicated software “Multipaction Calculator/ESA” can be used to analyze the
susceptibility of the secondary emission multiplication effect (multiplication perfor-
mance), to check whether the product falls into the sensitive region of the multipactor
under the working condition, and to determine the multiplication threshold at each
frequency and each gap.
Based on the simulation calculation results, the multiplication margins at each
frequency and each gap are determined as the secondary emission multiplication
effect (multiplication performance) analytical veriﬁcation result.
The susceptibility analysis of secondary emission multiplication effect (multipli-
cation performance) must consider the worst case of the product caused by possible
deformation of the material and the corresponding dimensional changes, processing
tolerance range, and other factors under the working condition.
5. Analysis of venting capacity of vents
Finally, for closed-structure products, it is required to verify that the vent design
meets the requirements, that is, to verify that the number and size of the vents can
reduce the internal pressure of the product to below 1.5 × 10−3 Pa before an RF
power is applied into the RF path.
Calculation and analysis of venting capacity can be performed using the dedicated
Multipaction Calculator (ESA) software.


496
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.6.4.3
Test Conditions
1. Cleanliness
The assembly, testing, and delivery of spacecraft RF components and equipment
must be carried out in an environment that meets cleanliness conditions, including the
secondary emission multiplication (multiplication performance) test environments,
where corresponding pollution prevention measures should be taken, such as anti-
pollution protective covers. Gloves must be worn as required when contacting the
product.
2. Vacuum
The vacuum requirements include.
(1) The environmental vacuum in the vacuum tank should be lower than 1.5 × 10−3
Pa.
(2) The vacuum in the critical area of the product RF path should also be lower than
1.5 × 10−3 Pa. Therefore, the environmental vacuum should be maintained for
a period of time before the multiplication test. For speciﬁc time requirements,
refer to the special technical conditions.
(3) For closed-structure RF components and equipment, the environmental vacuum
should be maintained for a certain period of time before the multiplication
test (usually 4–6 h for waveguide EUT, 24 h for coaxial system). For open-
structure RF components and equipment, such as open-structure antennas, the
environmental vacuum should be maintained for 2 h before the multiplication
test.
(4) For RF components and equipment consisting of a large quantity of composite
materials, the test vacuum can be reduced to 1.3 × 10−2 Pa, but should be
maintained for more than 24 h.
3. Test temperature
The test temperature requirements are
(1) The multiplication test is carried out in three test temperature states: low
temperature, normal temperature, and high temperature.
(2) The test temperature and control accuracy of the low- and high-temperature
states are speciﬁed in the special technical conditions.
(3) The temperature for low- and high-temperature test is generally determined by
the thermal control designer according to the minimum and maximum working
temperatures that the RF components and equipment can reach under actual
on-orbit operation.


10.6 EMC Tests for Special Equipment
497
4. Test frequency
If detailed analytical veriﬁcation of the secondary emission multiplication effect
(multiplication performance) has been performed at the initial stage of design, the
frequency at which the worst analytical veriﬁcation result is obtained should be taken
as the test frequency; if no detailed analytical veriﬁcation has been performed, the
test frequency can be selected by two cases:
(1) For products of nonresonant operating mode, select the lowest operating
frequency;
(2) For products with resonant operating characteristics, the center frequency, and
the frequencies at the edge of each frequency band should be selected.
5. Free electrons
The requirements for free electronic are as follows:
(1) Make sure that there is at least 102 free electrons around the product in the
duration of one microwave pulse peak; if the continuous wave (CW) is used for
the test, no free electrons are required.
(2) In order to ensure sufﬁcient uniformity of low-energy free electrons, multiplica-
tion test should be performed after the free-electron emission source works for
a certain period of time. For the speciﬁc time requirements, refer to the special
technical conditions.
(3) For closed-structure RF components and equipment, generally, the free-electron
emission source should operate for a certain period of time (4–6 h for closed
waveguide EUT, 24 h for the coaxial system) before the multiplication test. For
open-structure RF components and equipment, such as open-structure antennas,
usually the free-electron emission source should operate for 2 h before the
multiplication test.
(4) Any of the following free-electron sources can be used in the test:
➀Radiative β source: it can provide high-energy electrons, which can pass
through the metal cover plate on the surface of the product and enter the
critical areas of the RF path to form low-energy electrons that can induce
secondary emission multiplication effect in critical areas;
➁UV laser source: it can send the UV laser from the vents of the product
to the critical areas inside the RF path via the optical ﬁber, and the local
photoelectric effect of the UV laser can generate the free electrons required
to induce the secondary emission multiplication effect;
➂Electron gun: it can generate a beam of free electrons with known energy
and ﬂux characteristics;
➃Tungsten wire point emission: apply a few thousand volts of a negative
voltage to the tungsten wire to enable the tungsten wire point to emit free
electrons, and form low-energy electrons that can induce the secondary
emission multiplication effect.


498
10
EMC Test Veriﬁcation of Spacecraft Electronic Equipment
10.7
Summary
The EMC test of spacecraft electronic equipment is the most widely used technology
and method. This chapter ﬁrst introduces the common equipment-level EMC test
methods, and based on this, further describes the principle of computer-based tests.
Moreover, the test methods that are unique to spacecraft such as PCU EMC test,
electric propulsion EMC test, PIM test, and multiplication test are introduced, as a
reference for readers in their work.
In addition to the conventional EMC tests and those for spacecraft-speciﬁc equip-
ment such as PCU and electric propellers, considerations should also be paid to the
performance test requirements for special environments such as vacuum and low
temperature by Hui Yan satellites, and special measuring devices should be prepared
accordingly. Later, the requirements of ground wire crosstalk and transient test will
also be addressed.
In the future, with the development of veriﬁcation requirements for spacecraft
electronic equipment, the testing methods, and means, such as those for the ground
crosstalk and transient testing requirements, should also advance with the times.

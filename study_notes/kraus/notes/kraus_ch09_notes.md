# Kraus《Antennas》2nd Edition — Chapter 9
> **中英双语版**



## Chapter 9: Stub and Microstrip Antennas



496 1. ARRAYS OF DIPOLES AND OF APERTURES 3143 ADAPTIVE ARRAYS AND SMART ANTENNAS 497



design is also wetl adapted to microstrip or printed circuit construction. The



array shown has an endpoint input impedance of 50. for an impedance of



300 Q for the individual chains. The current attenuation from input to matched Direction of arrival



output is about 10 dB, which is considered optimum. Higher attenuation reduces 2 and return



the gain due to the larger taper in current distribution while lower attenuation ———_—. _



lowers the gain because more power is lost in the matched load. Average aperture



efficiencies are typically about 50 percent.



By bending the chain elements, Hendriksson, Markus and Tiuri have devel- > 6 &§ § § 8 2 BL pipote



oped a circularly polarized chain array. elements



11-12 RETRO-ARRAYS. THE VAN ATTA ARRAY. If a wave inci-



dent on an array is received and transmitted back in the same direction, the array J}+——— Equal length



acts as a retro-reflector ot retro-array. The passive squarc-corner reflector crs petween



(Sec. 12-3) does the same thing.



In general, cach element of a retro-array reradiates a signal which is the



conjugate of the received signal. The Van Atta array of Fig. 11-51 is an example.”



The 8 identical elements may be 4/2 dipoles, shown in end view in the figure.



With element pairs (1 and 8, 2 and 7, 3 and 6, and 4 and 5) connected by identical q .



equal-length cables, as indicated, a wave arriving at any angle θ is transmitted ‘ Figure 11-51 Kight-clement Van Atta retro-array. Element pairs are connected by equal length lines.



back in the same direction. The array shown in Fig. 11-51, like the square-corner i



reflector, is passive. An adaptive (active) array (Sec. 11-13) can also be made i] Also, by suitable signal processing, performance may be further enhanced,



retrodirective by using a mixer to produce a conjugate phase shift for each giving simulated patterns’ of higher resolution and lower sidelobes. In addition,



element.’ An advantage of an active array is that the elements need not be by appropriate sampling and digitizing the signuls at the terminals of each



arranged in a line or, in a 2-dimensional case, in a plane, Active retro-arrays can element and processing them with a computer, a very intelligent or smart antenna



also incorporate amplifiers.* can, in principle, be built. For a given number of clements, such an antenna’s



capabilities are limited, mainly by the ingenuity of the programmer and the avail-



11-13, ADAPTIVE ARRAYS AND SMART ANTENNAS. The able computer power. Thus, for example, multiple beams may be simultaneously



antenna elements and their transmission-line interconnections discussed so far. directed toward many signals arriving from different directions within the field of



produce a beam or beams in predetermined directions. Thus, when receiving, view of the antenna (ideally =2z sr for a planar array). These antennas are some-



these arrays look in a given direction regardless of whether any signals are arriv- times called Digital Beam Forming (DBF) antennas.”



ing from that direction or not. However, by processing the signals from the indi- As a rudimentary example of an adaptive array, a simpic 2-element system



vidual elements, an array can become active and react intelligently to its is shown in Fig. 11-52 with 7/2 spacing between the elements at the signal fre-



environment, steering its beam toward a desired signal while simultaneously quency f,. Let each element be a 4/2 dipole seen end-on in Fig. 11-52 so that the



steering a null toward an undesired, interfering signal and thereby maximizing patterns of the elements are uniform in the plane of the page. With elements



the signal-to-noise ratio of the desired signal. The term adaptive array is applied operating in phase, the beam is broadside (up in the figure).



to this kind of antenna. Consider now the case of a signal at 30” from broadside as suggested in



Fig. 11-S2 so that the wave arriving at element 2 travels 4/4 farther than to



element 1, thus retarding the phase of the signal by 90° at element 2. Each



‘ J. Hendriksson, K. Markus and M. Tiuri, "A Circularly Polarized Traveling-Wave Chain Antenna,” clement is equipped with its own mixer, Voltage-Controlled Oscillator (VCO),



European Microwave Conf., Brighton, September 1979. intermediate frequency amplifier and phase detector. An oscillator at the interme-



* LC. Van Atta, “ Electromagnetic Reflector,” U.S. Patent 2,909,002, Oct. 6, £959.



°C. ¥. Pon, “ Retrodirective Array Using the Heterodyne Method " JEEE Trans. Ants. Prop, AP-12, _



176-180, March 1964, ; . * Simulated patterns are ones that exist only in the signal-processing domain.



IEEE Ten oe i Ae tre Ri pevodirective Array for Satellite Communications, * H. Steyskal, “ Digital Beamforming Antennas,” Microwave J., 30, 107-124, January 1987



A981) ARRAYS OF DIPOLES AND OF APERTURES 1183 ADAPTIVE ARRAYS AND SMART ANTENNAS 499



quai phase front 30° 330°



Incoming of incoming signal i J



signal direction " at frequency J. i VJ



Dipole 1. Fao" g7Dinole 2 .



Mixer (9 (<9 QMixer iN CEMENTS Figure 11-53. Patterns of 2clement aduptive array for



Z\ signals from 0 and 30° directions, For the 0° signal, nulls are



<| at 90 and 270° while for the 30° signal, nulls are at 210 and



iF fl 180° 2\0" 330°, These patterns are identical with those of Figs. 4-1 and



(i) In our rudimentary 2-clement example, the beam will be in the 0° direction



iF veterence Vyi2 ) for a signal from the 0° direction and at 30° for a signal from that direction, as



Vite oscillator shown by the patterns in Fig. 11-53. If interfering signals are arriving from the



210 and 330° directions when the main signal is at 30°, the nulls at 210 and 330°



Final (summing) will suppress the interference. However, an interfering signal at 150° would be at



amplifier a pattern maximum, the same as the desired signal at 30°. To provide more



i with signal-processing circuitry effective adaptation to its environment, an array with more elements and more



Figure 11-52 Two-element adaptive array with signat-p sophisticated signal processing is required. For example, the main beam may be



steered toward the desired signal by changing the progressive phase difference



diate frequency f, is connected to each phase detector as reference. The phase between elements, while, independently, one or more nulls are steered toward



detector compares the phase of the downshified signal with the phase of the refer- interfering signals by modifying the array element amplitudes with digitally con-



P P ; ‘ r j ig signals by



ence oscillator and produces a voltage proportional to the phase difference. This 7 trolled attenuators.



voltage, in turn, advances or retards the phase of the VCO output so as to reduce |



the phase differerice to zero (phase locking). The voltage for the VCO of element . . . . co.



| would ideally be equal in magnitude but of opposite sign to the voltage for the 11-13a Literature on Adaptive Arrays. There is au extensive literature on



VCO of element 2 sc that the downshifted signals from both elements are locked adaptive arrays. Three special issues of the IEEE Transactions on Antennas and



oreemen i Propagation have been devoted to adaptive arrays. They are: vol. AP-12, March



in phase, making 1964; vol. AP-24, September 1976; and vol. AP-34, March 1986. Additional refer-



S1 = b2= bo a ences are as follows:



where φ_n = phase of downshifted signal from element 1 Bickmore, R. W.: “Time Versus Space in Antenna Theory,” in R. C. Hansen



6, = phase of downshifted signal from element 2 {ed.}, Microwace Scanning Antennas, vol. 3, Academic Press, 1966,



o = phase of reference oscillator pp. 289-339. -



, Biank, S.: “An Algorithm for the Empirical Optimization of Antenna Arrays,”



With equal gain from both IF amplifiers the voltages V, and V; from both IEEE Trans, Ants, Prop, AP-31 685-689, July 1983.



elements should be equal so that Butler, J. L.: “ Digital, Matrix, and Intermediate Frequency Scanning,” in R. C.



_ Hansen (ed.), Microwave Scanning Antennas, vol. 3, Academic Press, 1966,



Mids = Vilbs @ pp. 217-288



making the voltage from the summing amplifier proportional to 2V, (=2¥;) and Dinger, R. J.: “A Computer Study of Interference Nulling.by Reactively Steered



maximizing the response of the array to the incoming signal by steering the beam ___ Adaptive Arrays,” Ant. Prop. Soc. Int. Symp. Proc., 2, 807-810, 1984



onto the incoming signal. In our example, 45° phase corrections of opposite sign Einarsson, O.: Optimization of Planar Arrays, EEE Trans, Ants. Prop., AP-27,



would be required by the VCOs (+ for element 1, —for element 2). 86-92, January 1979.



500 11 ARRAYS OF DIPOLES AND OF APERTURES q UIs LOW-SIDELOBE ARRAYS SOT



Ersoy, O.: “Real Discrete Fourier Transform,” IEEE Trans. Acoustics, Speech, | RAN eR CS SARE



nd Signal Processing, ASSP-33, 880-882, August 1985. a“ ELOR AE Sates’ ;



Fan, H.. E. 1. El-Masry and W. K. Jenkins: “ Resolution Enhancement of Digital i : . RE SSS ES



Beamformers,” IEEE Trans. Acoustics, Speech, and Signal Processing, NAS ANSE SSSR SSS ESE



ASSP-32, 1041-1052, October 1984. QS ERNE SSSR SRNR SERVERS.



Griffiths, L. J., and C. W. Sim: “An Alternative Approach to Linearly Con- Y ERRERESSSS ESSEC EEE RE SS



strained Adaptive Beamforming.” IEEE Trans. Ants, Prop, AP-30, SSE SSS SSSR RRR



Gupta, L J. and A. A. Ksienski: * Effect of Mutual Coupling on the Performance 4 ys : *



of Adaptive Arrays,” IEEE Trans. Ants. Prop. AP-31, 7285-791, September } a N NN as



Hansen, RC.: “Gain Limitations of Lacge Antennas” IRE Trans. Anes. Prop. RRS IUS_ As clement cn aray for emai ening the ca om spe



AP-8, 491-495, September 1960. Colorado * :



Hatcher, B. R.: “Granularity of Beam Positions in Digital Phased Arrays,” Proc.



IEEE, 56, November 1968. !



Johnson, FI. W., and C. §, Burrus: “The Design of Optimal DET Algorithms 1f-l4 MICROSTRIP ARRAYS, Printed circuit and microstrip techniques



Using Dynamic Programming,” IEEE Trans, Acoustics, Speech. and ul facilitate the construction of multielement arrays for microwave frequencies.' The



Signal Processing, ASSP-31, 378-387, April 1983, i Kraus grid and Tiuri chain arrays (Sec. 11-11b) are examples. The 896-element



Laxpati, SR: “Planar Array Synthesis with Prescribed Pattern Nulls,” IEEE microstrip antenna for space research shown in Fig. 11-54 is another. All ele-



Trans. Ants, Prop., AP-30, 1176-1183, November 1982. . ments are photoctched from one side of a printed circuit board. The corporate



Mucci, R. A.; “A Comparison of Efficient Beamforming Algorithms,” IEEE structure feed has amplitude taper in the narrow dimension. The 9.5 x 2.4m



Trans, Acoustics, Speech, and Signal Processing, ASSP-32, 548-558, June array has a 34-dBi gain at 4 ~ 30 cm



1984, Although the microstrip clement is inherently narrowband, log-periodic



Ricardi, L. J.; “Adaptive Antennas,” in R.C. Johnson and H. Jasik (eds.), patch arrays have achieved bandwidths of 4 to 1.* Patch (or microstrip) antennas



Antenna Engineering Handbook, McGraw-Hill, 1984, chap. 22. : are discussed further in Chap. 16.



Shelton, J, P., and K. S. Kelleher: “Multiple Beams from Linear Arrays,” [RE



Trans. Ants. Prop. AP-9, 154-161, March 1961 q 11-15 LOW-SIDELOBE ARRAYS. ideally it may be desirable for an



Sorenson, H. V,, M. T. Heideman and C. S. Burrus: “On Computing the Split- antenna to have a narrow, well-defined beam with no sidelobes, or at least none



Radix FFT,” JEEE Trans. Acoustics, Speech, and Signal Processing, ASSP- above a certain prescribed level. A prime factor affecting the sidelobe level is the



34, 152-156, February 1986. aperture distribution (Sec. 11-22). Although some distributions _ yield



Steinberg, B. D.: “ Design Approach for a High-Resolution Microwave Imaging (theoretically) zero sidelobes, they may be more difficult of realization on reflector



Radio Camera,” J. Franklin Inst., 296, 415-432, December 1973 4 antennas than on phased arrays. The typical large parabolic reflector antenna



Volakis, J, L., and J. D. Young: “ Phase Linearization of a Broad-Band Antenna (Chap. 12) may also have significant sidelobes due to other causes such as aper-



Response in Time Domain,” IEEE Trans, Ants. Prop, AP-30, 309-313, ture blocking and diffraction from its prime focus feed or Cassegrain reflector,



March 1982. from struts of the supporting structure, from feed spillover, from surface irregu-



Vo, T. B.: “Null Steering by Controlling Current Amplitudes Only,” Ant. Prop. larities and from the edge of the parabola. The edge diffraction may be reduced



Soc. Int. Symp. Proc.,2, 811-814, 1984. by using a rolled edge (see Sec. 18-3d). Although offset feeds or integral horn



Waldron, T. P.. S. K. Chin and R. J. Naster: “ Distributed Beamstecring Control reflectors may have significantly lower minor lobes, accurate construction tech-



of Phased Array Radars,” Microwave J.. 29, 133-146, September 1986. niques providing precise amplitude and phase control of all elements of a phased



Weber, M. E., and R. Heisler: “A Frequency-Domain Beamforming Algorithm



for Wideband Coherent Signal Processing.” J. Acoustic Society of '* a oe



America, 76, October 1984. ‘ H.G. Oltman and D. A. Huebner, “ Electromagnetically Coupled Microstrip Dipoles,” IEEE Trans.



Wheeler, H. A.: “The Grating-Lobe Series for the Impedance Variation in a Anis. Prop, AP-29, 151 157, January 1981



Planar Phased-Array Antenna,” IEEE Trans. Ants. Prop, AP-14, 707- * P.S. Hall, “Microstrip Antenna Array with Multi-Octave Bandwidth,” Microwave J. 29, 133-139,



714, November 1966. March 1986.



50211. ARRAYS OF DIPOLES AND OF APERTCRES sae onoanee antennas 503



array have resulted in phased array designs witn sidelobe levels down 50 dB or



more. This is as good or better than has been achieved to date with reflector ‘a



antennas.' However, phased arrays are inherently narrower band than reflector



11-16 LONG-WIRE ANTENNAS. Most of the preceding parts of this



chapter deal with arrays of individual, discrete elements (usually 7/2 long) inter-



connected by transmission lines. A linear wire antenna, many wavelengths long,



may also be regarded as an array of 1/2 elements but connected in a continuous f ¥ stone cn oe



linear fashion with each clement serving as both a radiator and a transmission



line. The long-wire antennas discussed in this section are the V, rhombic and



Beverage types. The V antenna may be either unterminated {with standing wave) 4



or terminated {with traveling wave). The rhombic and Beverage antennas are



almost always terminated (with traveling wave)



11-16a V Antennas.’ By assuming a sinusoidal (standing-wave) current dis- Venere”



tribution, the pattern of a long thin wire antenna can be calculated as described kK



in Chap. 5. A typical pattern is shown in Fig. 11-5Sa for a wire 24 tong. The main |



lobes are at an angle f = 36° with respect to the wire. By arranging two such ! w



wires in a V with an included angle y = 72° as in Fig. 11-55d, a bidirectional



pattern can be obtained, This pattern is the sum of the patterns of the individual



wires or legs. Although an included angle y = 2f results in the alignment of the



major lobes at zero elevation angle (wires horizontal) and in free space, it is



necessary to make 7 somewhat less than 28 in order to obtain alignment at ele- 90° <a) . Figure 11-85 (a) Calculated pattern of 22 wire with



vation angles greater than zero.’ This is because the space pattern of a single wire S standing wave, (b) V antenna of two such wires, (¢)



is conical, being obtained by revolving the pattern of Fig. 11-55a, for example, a 128 terminated V antenna with legs 24 long and (d) V



with the wire as the axis. iN w antenna of cylindrical conductors 1.254 long with



If the legs of the thin-wire V antenna are terminated in their characteristic 20 measured pattern,



impedance, as in Fig. 11-55e, so that the wires carry only an outgoing traveling



wave, the back-radiation is greatly reduced. The patterns of the individual wires sisting of two cylindrical conductors 1.254 long and 2/20 diameter with an



can be calculated, assuming a single traveling wave as done in Chap. 5. included angle y = 90° has the highly unidirectional pattern’ of Fig. 11-55d.



A similar effect may be produced without terminations by the use of V



conductors of considerable thickness, The reflected. wave on such a conductor 11-16b Rhombic .Antennas.? A rhombic antenna may be regarded as a



may be small compared to the outgoing wave, and a condition approaching that double-V type. The wires at the end remote from the feed end are in close prox-



of a single traveling (outgoing). wave may result. For example, a V antenna con- imity, as in Fig. 11-56a. A terminating resistance, usually 600 to 800 Q, can be



_ ‘A. Dorne, in Very High Frequency Techniques, Radio Research Laboratory Staff, McGraw-Hill,



1 HE, Schrank, * Low Sidelobe Phased Array Antennas.” JEEE Ant. Prop. Soc. Newsletter, 28, 5-9, New York, 1947, chap. 4, p. 115.



April 1983 2 £. Bruce, “Development in Short-wave Directive Antennas,” Proc. IRE, 19, 1406-1433, August



* PS. Caner, C. W. Hanseli and N. E. Lindenblad, “Development of Directive Transmitting 1931.



Antennas by R. C, A. Communications, Inc..” Proc. IRE, 19, 1773-1842, October 1931 E. Bruce, A.C. Beck and LR. Lowry, “Horizontal Rhombie Antennas,” Proc. IRE, 23, 24-46,



P.S, Carter, “Circuit Relations in Radiating Systems and Applications to Antenna Problems.” Proc. January 1935.



1RE_20, 1004-1041, June (932 AE. Harper, Rhombic Antenna Design, Van Nostrand,-New York, 1941.



> The A.R.R.L. Antenna Book, American Radio Relay League, West Hartford, Conn., 1984, p. 7-4. Donald Foster, “ Radiation from Rhombic Antennas,” Proc. IRE, 28, 1327-1353, October 1937.



504 11 ARRAYS OF DIPOLES AND OF APERTURES 1.16 LONG-WIRE ANTENNAS 505



Ae The pattern of a rhombic antenna may be calculated as the sum of the



1 >» Sy Patterns of four tilted wires cach with a single outgoing traveling wave. The effect



2 ° Sy of a perfectly conducting ground may be introduced by the method of images.



FNM sot ; For a horizontal rhombic of perfectly conducting wire above a perfectly conduct.



as Syren ing plane ground, Bruce, Beck and Lowry? give the relative field intensity E in



AS Terminatiog 3 the vertical plane coincident with the rhombic axis® as a function of 2, ¢, L, and



4 is tesistance H, as + Ps Mea aK



w Es eco sn se ain ee” mm



where x = elevation angle with respect to ground



= half included side angle of rhombic antenna



Azimuthal pattern at «~ 10° H, = H// = height of rhombic antenna above ground



» L, = Li =leg length



Figure 11-56 Yerminated rhombic A, = 2nH , = 2nH/A)



antenna (a) with azimuthal pattern (>) L, = 2ab, = abi



and vertical plane pattern (¢) for a y = (1 —sin ¢ cos 22



' shombic 64 long on each leg. @ = 70’, ;



i) arene tine : ipsa A uniform antenna current is assumed and mutual coupling is neglected,



Vertical pattern Rhombic Antenna Design, Van Nos. lowing the procedure of Bruce, Beck and Lowry, the various parameters



te trand, New York, 1941) may be determined as follows. For the maximum E condition, E is maximized



with respect to H,, that is, we make .



conveniently connected at this location so that there is substantially a single CE



outgoing traveling wave on the wires. The length of cach leg is L, and half of the 2H 0 Q)



included side angle is ¢. The calculated patterns' of a terminated rhombic with . *



legs 64 long are shown in Fig. 11-56b and c. The rhombic is assumed to be 1.14 which yields



above a perfectly conducting ground, and ¢ = 70°. 1 cos (2nH, sin 2) = 0



In designing a rhombic antenna, the angle θ, the leg length and the height . ‘



above ground may be so chosen that (1) the maximum of the main lobe coincides which is satisfied when



with the desired elevation angle « (alignment design) or (2) the maximum relative n



field intensity E for a constant antenna current is obtained at the desired cle- nH, sina=n 2



vation angle a (maximum E design).



If the height above ground is less than that required for these designs, align- where n = 1, 3, 5,...



ment may be obtained by increasing the leg length. If the height is maintained ey . _



but the leg length is reduced, alignment may be obtained by changing the angle For the lowest practical height, n = 1. Therefore,



@. As a third possibitity, if both the height and the teg length are reduced, the 1



angle θ can be changed to produce alignment. Any of these 3 modifications H.= Tana (3)



results in a so-called compromise design? having reduced gain. If moderate depar- sin



tures from optimum performance are acceptable, a rhombic antenna can be oper-



ated without adjustment over a frequency band of the order of 2 to 1.



> E, Bruce, A.C. Beck and L. R. Lowry, “Horizontal Rhombic Antennas,” Proc. IRE, 23, 24-26,



“From A’E Harpen Rionbie Amoma Design Van Nostrand, New York, 1941 {The tadiaton in his plane is horizontally polarized. However, in other planes the polarization is



506 1 ARRAYS OF DIFOLES AND OF APERTURES Ite LONG-WIRE Antennas 507



Equation (3) gives the height H, for the antenna. To find the feg length, E is Table 12-1 Design formulas for terminaied rhombic



maximized with respect to L,, obtaining antennast



4 21 — sin @ cos 9) @ thembic amtewmn Forme



. . . . Maximum E at t



Finally, by maximizing E with respect to ¢ and introducing the condition of (4), elevation angle 2 "aa



Substituting (5} back into (4) yields Ano,



Li= Gna 6) lobe with elevation "Fang



Equations (3), (5) and (6) then give the height in wavelengths H,, the half- φ = 90° - x



side angle ¢ and the leg length in wavelengths L,, for maximum E at the desired 1, - 237



elevation angle a. This is for a uniform antenna current. It does not follow that er a



the field intensity at the desired elevation angle is a maximum for a given power Reduced height Hf ==>”



input to the antenna, However, it is probably very close to this condition. It is Compromise design tan [lot sin? .



also of interest that for the maximum E condition the maximum point of the for alignment at p, = Hn lnk sin? 2) | orl



main lobe of radiation is not, in general, aligned with the desired elevation angle. elevation angle a sma 2x sin a tan (Hf, sin 2)



In the alignment design the maximum point of the main tobe of radiation is where Hf, — TF ana Wm



aligned with the desired elevation angle 2. For this condition, E at x is slightly a



less than for the maximum E condition. Alignment is accomplished by maximiz- Reduced length £ n.-—



ing E with respect to « and introducing the condition of (3). This gives Compromise design a” asin x



0371 clevation angle x 6 = avesin | 44 937!



i—sin ¢ cos x where Li = LjA



Substituting (7) in (1) and maximizing the resulting relation for the field with Reduced height H’ Solve this equation for



respect to gives and length £ KH,



Compromise design, = ————#a_



o=90 —% {8) for alignment at sin @ tan a tan (H; sin 2) 4m tan (WL)



elevation angle x 1 — sin § 00s x £



as before. Finally substituting (8) in (7) we obtain where = —————— and L, = 2n =



L,= 3. ie) 4 IRE, 23, 24-26, January 1935. row. Mer tal Rhombic Antennas. P



Equations (3), (8) and (9) then give H_n, φ_n and L_n, for alignment of the be adjusted to coincide with the optimum elevation angle of downcoming waves.



maximum point of the main lobe of radiation with the desired elevation angie 2. This Multiple Unit Steerable Antenna,' or MUSA, is a vertically steerabic system



Only the length is different in the alignment design, being 0.371/0.5 = 0.74 of the of this kind for long-distance short-wave reception of horizontally polarized



value for the maximum E design. downcoming waves.



The above design relations are summarized in Table 11-1 together with



design formulas for 3 kinds of compromise designs.



An end-to-end receiving array of a number of rhombics may be so con- TAT. Fri Goan “A Mune



° . a I. T. is and C. B. Feldman, “A Muitiple Unit St bl . ”



nected as to provide an electrically controllable vertical plane pattern which can Prov. IRE.28 S4 917, July 1937, laple Unit Stesrable Antenna for Shor Wave Reception,



S08 11 ARRAYS OF DIPOLES AND OF APERTURES hay curtain arrays 509



pf Direction of Direction of eS E



propagation ‘ propagation



Pertect conductor Imperfect conductor x



de ariiter _g Termumation zB, Receiver lana



Figure 11-57 (a) Wave front over a perfect conductor, (6) Wave front over imperfect conductor.



tel Beverage antenna @



11-16¢ Beverage Antennas. The electric field of a wave traveling along a per-



fectly conducting surface is perpendicular to the surface as in Fig. 11-S7a.



However, if the surface is an imperfect conductor, such as the earth's surface or



ground, the clectric ficld lines have a forward tilt near the surface as in



Fig. 11-57b. Hence, the field at the surface has a vertical component E, and a Flee us ee of 4/2 dipoles with reflectors, (b) symmetrical Bruce untenna, (cl Sterba



horizontal component E,.' The component E, is associated with that part of the oleate cueal nisin poke array. Arrows indicate instantaneous current directions and dots



wave that enters the surface and is dissipated as heat. The E, component con-



linues to travel along the surface. \ .



‘The fact that a horizontal component E, exists is applied in the wave largely absorbed in the termination. Hence, the antenna exhibits a directional



antenna of Beverage, Rice and Kellogg for receiving vertically polarized waves.2 pattern in the horizontal plane with maximum response in the direction of the



This antenna consists of a long horizontal wire terminated in its characteristic termination {to the left in Fig. 11-57c). The Beverage antenna finds application as



impedance at the end toward the transmitting station as in Fig. 11-57c. The a receiving antenna in the low- and medium-frequency range.



ground ucts as the imperfect conductor. The emfs induced along the antenna by



the E, component, as the wave travels toward the receiver, all add up in the same



phase at the receiver. Energy from a wave arriving from the opposite direction is 11-17 CURTAIN ARRAYS. In short-wave communications the curtain



type of array finds many applications. As an example, a curtain type is illustrated



in Fig. 11-S8q that consists of an array of 4/2 dipotes with a similar curtain at a



Soe distance of about 4/4 acting as a reflector.’ If the array is large in terms of wave-



Actually the wave exhibits elliptical cross-field, ie, the electric vector describes an ellipse whose lengths, the reflector curtain is nearly equivaient to a large sheet reflector.



plane is parallel to the direction of propagation. However, the axial ratio of this ellipse is usually very



2H. H. Beverage, C. W. Rice and E. W. Kellogg, “The Wave Antenna, a New Type of Highly -_—



Directive Antenna,” Trans. AIEE, 42, 215, 1923 ”HBriickmann, Antennen, ihre Theorie und Technik, S. Hirzel, Leipzig, 1939, p. 300.



510 11 ARRAYS OF DIPOLES AND OF APERTURES 1149 FOLDED DIPOLE ANTENNAS “STI



arrows indicate the instantaneous current directions and the dots the locations of



[3 current minima. The radiation normal to this loop is horizontally polarized.



; ie } Consider now the situation shown in Fig. 11-59. Here the loop is fed at the



» | same location. However, the toop is continuous and is fed at a point by an unbai-



3 _ anced line. In this case, the antenna currents flowing to the feed point are equal



Ground plane and in phase, so that the current distribution on the antenna must be as indi-



cated. The radiation normal to this loop is vertically polarized.



at o The location at which an antenna is energized also may, be important. For



example, two 7/2 elements have in-phase currents when symmetrically fed as in



Fig. 11-59¢ but out-of-phase currents when fed from one end as in Fig. 11-59d,



For the currents to be in phase when the array is fed from one end requires that



3 3-4 -—3— the line between the elements be transposed as in Fig, 11-59e.



2 2 11-19 FOLDED DIPOLE ANTENNAS. A simple 4/2 dipole has a ter-



i | minal resistance of about 70 Q so that an impedance transformer is required to



we) (a) te) match this antenna to a 2-wire line of 300 to 600 © characteristic impedance.



However, the terminal resistance of the modified 2/2 dipole shown in Fig, 11-60a



Figure 11-59 (a) Loop with 2-wire feed for horizontal polarization, {b) loop with {-wire feed from is nearly 300 Q so that it can be directly connected to a 2-wire line having a



coaxial line for vertical polarization, (c} center-fed broadside array of (wo 4/2 dipoles, (d) end-fed characteristic impedance of the same value. This “ultra close-spaced type of



end-tire array of two 4 2 dipoles and (e) end-fed broadside array of two 4/2 dipoles. Arrows indicate array” is called a folded dipole. More specifically the one in Fig. 11-60a is a



instantaneous current directions and dots indicate current minimum points. 2-wire folded 2/2 dipole. The antenna consists of 2 closely spaced 4/2 elements



connected together at the outer ends. The currents in the elements are substan-



tially equal and in phase.



Several other examples of curtain arrays are the Bruce type of Fig. 11-586, Assuming that both conductors of the dipole have the same diameter, the



the Sterha type! of Fig. 11-58¢ and the Chireix-Mesny type? of Fig. 11-58d. The approximate value of the terminal impedance may be deduced very simply as



arrows are located at or near current maxima and indicate the instantancous



current direction. The small dots indicate the locations of current minima.



1i-18 LOCATION AND METHOD OF FEEDING ANTENNAS. er S| 2 1, 1



It is interesting to note the effect that the method and location of feeding has on



the characteristics of an antenna. As illustrations, let us consider the following 2-wire an



If an antenna is fed with a balanced 2-wire line, equal out-of-phase currents dipole



must flow at the feed point. Thus, a square loop LA in perimeter and fed at the te w



bottom as in Fig. 1t-59a must have the current distribution indicated. The



‘ E. J. Sterba. “Theoretical and Practical Aspects of Directional Transmitting Systems,” Proc. IRE, s wire



19. (184-1215, July 1931 dipole te)



iceix, stem of Directional Aerials for Transmission on Short Waves,” Exp. Wire-



lessund Wiese Brg. 6235. May 129 ; Figure 1-60 Folded dipotes.



512 11 ARRAYS OF DIPOLES AND OF APERTURES it FOLDED DIPOLE ANTENNAS S13



foliows.! Let the emf V applied to the antenna terminals be divided between the 2 a ——3——_+ — x +



dipoles as in Fig. 11-60b. Then oF



where [, = current at terminals of dipote 1 3 3



I= current at terminals of dipole 2 | -7p>-—1 a en



Z,, = self-impedance of dipole 1



7:1 = mutual impedance of dipoles? and 2 —a. -—— Ss



Since I, = /,, (1) becomes



V = 20,(Zy, + Z12) (2) (dy



Further, since the 2 dipoles are close together, usually d is of the order of 2/100, Tota!



Z,, = Z,,. Thus, the terminal impedance Z of the antenna is given by 1



Taking Z,, x 70 +j0Q for a 4/2 dipole, the terminal impedance of the 2-wire .



| folded dipole becomes i



* For a 3-wire folded 4/2 dipole as in Fig. 11-60c the terminal resistance calculated Tout



in this way is 9 x 70 = 630 ©. In general, for a folded 4/2 dipole of N wires, the oe



terminal resistance is 70N? Q. Equal currents in all wires are assumed.



; ‘ 2 . Figure 11-61 (a) Three-wire folded 4/2 dipole, () &-wire folded 7/2 dipole, (c) 2-wire 34/4 antenna, (d)



Several other types of folded-wire antennas? are shown in Fig. 11-61. The i 4-wire 34/8 antenna and (e) 2-wire 3//8 stub antenna, Arrows indicate instantaneous current direc-



one at (a) is a 3-wire type which differs from the one in Fig. 1!-60c in that there tions and dots indicate current minimum points. (After Kraus.)



arc no closed loops. The measured terminal resistance of this antenna is about .



3200 ©. ‘The antenna at (b) is a 4-wire type with a measured terminal resistance of



about 1400 @ Thus far, all the folded dipoles discussed have been 4/2 types. The : ; Co .



total current distribution for these types is nearly sinusoidal, the same as fora | The measured terminal resistance of the 2-wire 34/4 dipole is about 450 Q, of the



simple 7/2 dipole. Folded dipoles of length other than 4/2 are illustrated in 4-wire 34/8 dipole about 225 Q and of the 2-wire 34/8 stub antenna about 225 Q.



Fig. 11-61¢ and d. The one at (c) is a 2-wire type 34/4 long and that at (@)isa An application of the 3-wire folded 7/2 dipole of Fig. 11-61a to a WBJK



4-wire type 3//8 long. The instantaneous current directions, the current distribu- array with 2/5 spacing is shown in Fig. 11-62." The impedance of each folded



tion on the individual conductors and the total current distribution are also indi- dipole in free space is about 1200 Q (resistive) but in the array is reduced to



cated. Half of the 2-wire 34/4 dipole can be operated with a ground plane as in 300 Q. which transforms via a 4/4 600-0 line to 1200 Q. At the junction of the



Fig. 11-61e, yielding the 34/8 stub antenna with total current distribution shown. two transformers the impedance is half {200 Q, or 600 , matching a 600-2 line



to the transmitter or receiver. Thus, the W8JK array is fed entirely by lines of



constant impedance (600 9) with no resonant stubs or tuning adjustments



'R. w. P. King, H.R. Mimno and A. H. Wing, Transmission Lines, Antennas and Ware Guides,



McGraw-Hill, New York, 1945, p, 224,



W. ¥.B, Roberts, “Input Impedance of a Folded Dipole.” RCA Rev, 8, 289 300, June 1947, which



treats folded dipoles with conductors of equal diameter and also unequal diameter. 1 Kum Tui Tue Flavop Beam Antenna” Radi 243, 10-16, N



? J.D. Kraus," Multi-wire Dipole Antennas,” Electronics, 13, 26-27, January 1940. J.D, Kraus, “Twin-Three Flat-Top Beam Antenna,” Ratio, no. 243, 10-16, November 1939,



51411 annavs OF DIPOLES AND OF APERTURES 1121 CONTINUOUS APERTURE DisTRIBUTION S15



"adiation » Crossover



‘ Figure 11-62 W8)K array, with



' 3-wire [olded dipole elements fed by



\ 6008 fine, transmission lines of constant



any length impedance. The dipoles are separ-



f ated by wooden or plastic spreaders



and supported by nylon rope. a Ch



q Figure 11-64 (a) Two-wire folded dipole and (6) as modified (o form single-torn loop. (c) Four-wire



11-20 MODIFICATIONS OF FOLDED DIPOLES. Consider a folded dipole and (d) as modified to form 2-turn loop.



2-wire folded dipole shown in Fig. 11-63a. The terminal resistance is approx-



imately 300 Q. By modifying the dipole to the general form shown in Fig. 11-63), A 2-wire folded 4/2 dipole is also shown in Fig. 11-64a. The arrows indicate



wide range of terminal resistances can be obtained, depending on the value of the instantaneous current direction and the small dots indicate the locations of



D, This arrangement is called a T-match antenna.' Dimensions in wavelengths for current minima. By pulling the dipole wires apart at the center, the single-turn



providing an impedance match to a 600 © line are shown in Fig. 11-63c. loop antenna of Fig. 11-64h is obtained. The length of cach side is 7/4. The loop



has a Jower termina! resistance than the folded dipole.



dr A 4-wire folded 4/2 dipole is shown in Fig. 11-64c. This dipole is the same



" — a type as shown in Fig. 11-61b. It is, however, sketched in a different manner. By



ko z — fp pulling this dipole apart at the center the 2-turn loop or quad antenna of Fig. 11+



[Fossa aoe ded dipole Fae __ The directivity of all the types shown in Fig. 11-64 is nearly the same as for



simple 4/2 dipole, although the types at (b) and (d) are equivalent to 2 horizon-



(@) ®) tal dipoles stacked ~0.18A giving a small increase, With the loop types vertical



aan and the terminals at the lowest corner, the radiation normal to the plane of the



r0.12\4 loops is horizontally polarized.



~0.0001 to 0 oond 5 - T-match 11-21 CONTINUOUS APERTURE DISTRIBUTION.? Extending



~0.01\—" obo our discussion of Sec. 4-14, consider now a continuous-current sheet or field dis-



Figure 11-63 Folded dipole and T-match antennas.



TD Ra ' The following sections (11-21 through 11-25) are from J, D. Kraus, Radio Astronomy, 2nd ed.,



J.D. Kraus and S, S. Sturgeon, “The T-Matched Antenna,” QST, 24, 24-25, September 1940. Cygnus-Quasar, 1986.



S132 FOURIER TRANSFORM RELATIONS 517



516 11 ARRAYS OF DIPOLES AND OF APERTURES



where ff = 22/4. For a uniform aperture distribution [E(x) = E,).(3) reduces to



| F(g)| = 22 [ eitasin’ dy “



and on axis (¢ = 0) we have



Field 7 1E(g)| = = 5



distribution ee #) 2roh Ing (5)



'/ 7 where A = aperture area (=ay,)



t— E, = electric field in aperture plane



« Aperture |}, D For unidirectional radiation from the aperture (in direction @ = 0 but not in



direction @ = 180°), | E is twice the value gi in (5).



Figure 11-68 Aperture of width a and amplitude distribution E(x! intecration ¥ ui a wi lue given in (5)



tribution over,an aperture as in Fig. 11-65. Assuming a current or field perpen- {E(d)| = ky Bal si Sin 7 (6)



dicular to the page () direction) that is uniform with respect to y. the clectric field



at a distance r from an elemental aperture dx dy is! where



=- = EE 6 i dx dy {l) ky = S2 7



ak = — ju del = — ara 7)



Paniel j From (4-14-17) the ficld of a long array of m discrete sources of spacing d is



iaj f = & > dy. i al}, Vs m~ .



where #7, = vector potential (- tn (ff > dv. in gener ) = ng, 50 LiBa'/2) sin 6) ®)



J, = current density, A m=? (Be E sin p

## 中文翻译

> **中文：** 第9章介绍**短柱天线(Stub Antennas)**和**微带天线(Microstrip Antennas)**。短柱天线是传输线短路或开路段的辐射应用；微带天线是用印刷电路工艺制作的低剖面天线。

### 9-1 短柱天线
利用传输线短截线（stub）的末梢效应实现辐射。常见类型包括单极子天线（四分之一波长）和倒L/F形天线。

### 9-2 微带天线
微带天线（贴片天线）由介质基板上的金属贴片和接地平面组成，特点是低剖面、轻量、易集成。
- **矩形贴片**：最常见，工作在基本模式TM$_{01}$或TM$_{10}$，辐射来自贴片边缘的缝隙
- **圆形贴片**：可设计多种模式
- **馈电方式**：微带线馈电、同轴探针馈电、耦合馈电

### 9-3 微带天线参数
- 辐射边长度$L \approx \lambda_0/(2\sqrt{\varepsilon_{\text{eff}}})$
- 带宽通常仅百分之几（2-5%），可通过厚基板或开槽展宽
- 增益通常5-8 dBi

### 9-4 应用
移动通信（手机天线）、GPS、卫星通信、相控阵、可穿戴设备。
